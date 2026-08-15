#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime, timezone

import argparse
import json
import platform
import subprocess
import time

import numpy as np
import torch


MODEL_NAME = "AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION"
MODEL_PROVENANCE = "LOCAL_REIMPLEMENTATION"


def safe_command(command):

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }

    except Exception as exc:

        return {
            "returncode": None,
            "stdout": "",
            "stderr": repr(exc),
        }


def read_device_tree_models():

    paths = [
        Path("/proc/device-tree/model"),
        Path("/sys/firmware/devicetree/base/model"),
    ]

    values = []

    for path in paths:

        if not path.is_file():
            continue

        try:

            value = (
                path.read_bytes()
                .replace(b"\x00", b"")
                .decode(
                    "utf-8",
                    errors="ignore",
                )
                .strip()
            )

            if value:
                values.append(value)

        except Exception:
            pass

    return values


def summarize(values):

    values = np.asarray(
        values,
        dtype=np.float64,
    )

    return {
        "count": int(values.size),
        "mean_ms": float(values.mean()),
        "std_ms": float(values.std()),
        "min_ms": float(values.min()),
        "p50_ms": float(np.percentile(values, 50)),
        "p90_ms": float(np.percentile(values, 90)),
        "p95_ms": float(np.percentile(values, 95)),
        "p99_ms": float(np.percentile(values, 99)),
        "max_ms": float(values.max()),
    }


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--model",
        default=(
            "AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION_"
            "torchscript.pt"
        ),
    )

    parser.add_argument(
        "--warmup",
        type=int,
        default=100,
    )

    parser.add_argument(
        "--iterations",
        type=int,
        default=1000,
    )

    parser.add_argument(
        "--precision",
        choices=[
            "fp32",
            "fp16",
        ],
        default="fp32",
    )

    parser.add_argument(
        "--output",
        default="orin_nano_benchmark_result.json",
    )

    parser.add_argument(
        "--allow-non-orin-debug",
        action="store_true",
    )

    args = parser.parse_args()


    if not torch.cuda.is_available():

        raise RuntimeError(
            "CUDA is required."
        )


    device_tree_models = (
        read_device_tree_models()
    )

    combined_model = (
        " | ".join(
            device_tree_models
        )
        .lower()
    )


    jetson_detected = bool(
        device_tree_models
        or
        Path(
            "/etc/nv_tegra_release"
        ).is_file()
        or
        Path(
            "/usr/bin/tegrastats"
        ).is_file()
    )


    orin_detected = bool(
        "orin"
        in combined_model
    )


    nano_detected = bool(
        "orin nano"
        in combined_model
    )


    actual_orin_nano = bool(
        jetson_detected
        and
        orin_detected
        and
        nano_detected
    )


    if (
        not actual_orin_nano
        and
        not args.allow_non_orin_debug
    ):

        raise RuntimeError(
            "Actual Jetson Orin Nano was not detected. "
            "Benchmark refused."
        )


    model_path = Path(
        args.model
    )

    if not model_path.is_file():

        raise FileNotFoundError(
            model_path
        )


    device = torch.device(
        "cuda"
    )


    model = torch.jit.load(
        str(
            model_path
        ),
        map_location=device,
    )

    model.eval()


    if args.precision == "fp16":

        model = model.half()

        input_tensor = torch.randn(
            1,
            3,
            224,
            224,
            device=device,
            dtype=torch.float16,
        )

    else:

        model = model.float()

        input_tensor = torch.randn(
            1,
            3,
            224,
            224,
            device=device,
            dtype=torch.float32,
        )


    torch.cuda.empty_cache()

    torch.cuda.reset_peak_memory_stats()


    with torch.inference_mode():

        for _ in range(
            args.warmup
        ):

            _ = model(
                input_tensor
            )


    torch.cuda.synchronize()


    gpu_latencies_ms = []

    wall_latencies_ms = []


    with torch.inference_mode():

        for _ in range(
            args.iterations
        ):

            start_event = torch.cuda.Event(
                enable_timing=True
            )

            end_event = torch.cuda.Event(
                enable_timing=True
            )


            torch.cuda.synchronize()

            wall_start = time.perf_counter()

            start_event.record()

            output = model(
                input_tensor
            )

            end_event.record()

            torch.cuda.synchronize()

            wall_end = time.perf_counter()


            gpu_latencies_ms.append(
                float(
                    start_event.elapsed_time(
                        end_event
                    )
                )
            )

            wall_latencies_ms.append(
                float(
                    (
                        wall_end
                        - wall_start
                    )
                    * 1000.0
                )
            )


    if tuple(
        output.shape
    ) != (
        1,
        2048,
    ):

        raise RuntimeError(
            f"Unexpected output shape: "
            f"{tuple(output.shape)}"
        )


    descriptor_norm = float(
        torch.linalg.vector_norm(
            output.float(),
            dim=1,
        ).item()
    )


    peak_allocated = int(
        torch.cuda.max_memory_allocated()
    )

    peak_reserved = int(
        torch.cuda.max_memory_reserved()
    )


    gpu_summary = summarize(
        gpu_latencies_ms
    )

    wall_summary = summarize(
        wall_latencies_ms
    )


    result = {
        "created_at_utc": datetime.now(
            timezone.utc
        ).isoformat(),

        "model": MODEL_NAME,

        "model_provenance": (
            MODEL_PROVENANCE
        ),

        "official_mobilegeo_model": False,

        "actual_orin_nano_runtime": (
            actual_orin_nano
        ),

        "result_label": (
            "ACTUAL_JETSON_ORIN_NANO_MEASUREMENT"
            if actual_orin_nano
            else
            "NON_ORIN_DEBUG_MEASUREMENT_"
            "NOT_VALID_AS_ORIN_RESULT"
        ),

        "hardware": {
            "platform": platform.platform(),

            "machine": platform.machine(),

            "device_tree_model": (
                device_tree_models
            ),

            "cuda_gpu": (
                torch.cuda.get_device_name(
                    0
                )
            ),

            "cuda_compute_capability": (
                "%d.%d"
                %
                torch.cuda.get_device_capability(
                    0
                )
            ),

            "torch_version": (
                torch.__version__
            ),

            "cuda_version": (
                torch.version.cuda
            ),

            "nv_tegra_release": (
                Path(
                    "/etc/nv_tegra_release"
                ).read_text(
                    errors="ignore"
                ).strip()
                if Path(
                    "/etc/nv_tegra_release"
                ).is_file()
                else None
            ),

            "nvpmodel": safe_command(
                [
                    "nvpmodel",
                    "-q",
                ]
            ),

            "jetson_clocks": safe_command(
                [
                    "jetson_clocks",
                    "--show",
                ]
            ),

            "uname": safe_command(
                [
                    "uname",
                    "-a",
                ]
            ),
        },

        "benchmark": {
            "input_shape": [
                1,
                3,
                224,
                224,
            ],

            "output_shape": [
                1,
                2048,
            ],

            "precision": (
                args.precision
            ),

            "warmup_iterations": (
                args.warmup
            ),

            "measured_iterations": (
                args.iterations
            ),

            "scope": (
                "MODEL_FORWARD_ONLY_"
                "PREPROCESS_AND_IMAGE_DECODE_EXCLUDED"
            ),

            "gpu_event_latency": (
                gpu_summary
            ),

            "synchronized_wall_latency": (
                wall_summary
            ),

            "throughput_from_gpu_mean_images_per_second": (
                1000.0
                /
                gpu_summary[
                    "mean_ms"
                ]
            ),

            "throughput_from_wall_mean_images_per_second": (
                1000.0
                /
                wall_summary[
                    "mean_ms"
                ]
            ),

            "peak_torch_cuda_allocated_bytes": (
                peak_allocated
            ),

            "peak_torch_cuda_reserved_bytes": (
                peak_reserved
            ),

            "descriptor_norm": (
                descriptor_norm
            ),
        },

        "reporting_constraints": {
            "power_consumption_measured": False,

            "end_to_end_camera_pipeline_measured": False,

            "retrieval_accuracy_measured_here": False,

            "retrieval_is_verified_uav_pose": False,
        },
    }


    output_path = Path(
        args.output
    )

    output_path.write_text(
        json.dumps(
            result,
            indent=2,
        ),
        encoding="utf-8",
    )


    latency_csv = output_path.with_name(
        output_path.stem
        + "_latencies.csv"
    )


    with open(
        latency_csv,
        "w",
        encoding="utf-8",
    ) as file:

        file.write(
            "iteration,gpu_event_ms,"
            "synchronized_wall_ms\n"
        )

        for index, (
            gpu_ms,
            wall_ms,
        ) in enumerate(
            zip(
                gpu_latencies_ms,
                wall_latencies_ms,
            ),
            start=1,
        ):

            file.write(
                f"{index},"
                f"{gpu_ms:.9f},"
                f"{wall_ms:.9f}\n"
            )


    print("=" * 80)

    print(
        "ACTUAL ORIN NANO:",
        actual_orin_nano
    )

    print(
        "GPU:",
        torch.cuda.get_device_name(
            0
        )
    )

    print(
        "Precision:",
        args.precision
    )

    print(
        "GPU mean latency:",
        f"{gpu_summary['mean_ms']:.3f} ms"
    )

    print(
        "GPU p50 latency:",
        f"{gpu_summary['p50_ms']:.3f} ms"
    )

    print(
        "GPU p95 latency:",
        f"{gpu_summary['p95_ms']:.3f} ms"
    )

    print(
        "GPU p99 latency:",
        f"{gpu_summary['p99_ms']:.3f} ms"
    )

    print(
        "Wall mean latency:",
        f"{wall_summary['mean_ms']:.3f} ms"
    )

    print(
        "Peak allocated CUDA memory:",
        f"{peak_allocated / (1024**2):.2f} MiB"
    )

    print(
        "Output:",
        output_path
    )

    print(
        "Latency CSV:",
        latency_csv
    )

    print("=" * 80)


if __name__ == "__main__":
    main()
