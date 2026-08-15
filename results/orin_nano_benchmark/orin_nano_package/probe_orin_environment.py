#!/usr/bin/env python3

from pathlib import Path

import json
import platform
import subprocess

import torch


def command(cmd):

    try:

        result = subprocess.run(
            cmd,
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


models = []

for path in [
    Path("/proc/device-tree/model"),
    Path("/sys/firmware/devicetree/base/model"),
]:

    if not path.is_file():
        continue

    try:

        value = (
            path.read_bytes()
            .replace(
                b"\x00",
                b""
            )
            .decode(
                "utf-8",
                errors="ignore",
            )
            .strip()
        )

        if value:
            models.append(value)

    except Exception:
        pass


report = {
    "platform": platform.platform(),

    "machine": platform.machine(),

    "device_tree_model": models,

    "torch_version": torch.__version__,

    "cuda_available": (
        torch.cuda.is_available()
    ),

    "cuda_version": (
        torch.version.cuda
    ),

    "gpu": (
        torch.cuda.get_device_name(
            0
        )
        if torch.cuda.is_available()
        else None
    ),

    "compute_capability": (
        torch.cuda.get_device_capability(
            0
        )
        if torch.cuda.is_available()
        else None
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

    "tegrastats_exists": (
        Path(
            "/usr/bin/tegrastats"
        ).is_file()
    ),

    "nvpmodel": command(
        [
            "nvpmodel",
            "-q",
        ]
    ),

    "jetson_clocks": command(
        [
            "jetson_clocks",
            "--show",
        ]
    ),

    "uname": command(
        [
            "uname",
            "-a",
        ]
    ),
}


print(
    json.dumps(
        report,
        indent=2,
    )
)
