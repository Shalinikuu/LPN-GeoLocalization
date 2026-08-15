# Jetson Orin Nano Benchmark Package

Model:
AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION

Provenance:
LOCAL_REIMPLEMENTATION

This is not an official MobileGeo model or official MobileGeo
deployment benchmark.

Input:
[B, 3, 224, 224]

Preprocessing reference:
ImageNet mean = [0.485, 0.456, 0.406]
ImageNet std  = [0.229, 0.224, 0.225]

Output:
[B, 2048]

Output descriptors are L2-normalized.

Checkpoint SHA256:
adc64177582638690b841c1be390b7d05dfb27f4d2001b3d52fb74455020b807

REFERENCE-HOST WARNING:
The model was exported on a non-Orin reference host.
Tesla T4 / Google Colab timings must never be reported as
Jetson Orin Nano latency.

ACTUAL ORIN NANO EXECUTION:

Step 1:
python3 probe_orin_environment.py

Step 2 — FP32:
python3 benchmark_orin_nano.py --model AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION_torchscript.pt --precision fp32 --warmup 100 --iterations 1000 --output orin_nano_fp32_result.json

Step 3 — optional FP16:
python3 benchmark_orin_nano.py --model AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION_torchscript.pt --precision fp16 --warmup 100 --iterations 1000 --output orin_nano_fp16_result.json

BENCHMARK SCOPE:
Model forward only.

Excluded:
- image disk decoding
- resizing
- normalization
- retrieval similarity search
- camera acquisition
- GPS/geodetic processing

TENSORRT:
Do not build a TensorRT engine on Tesla T4 and report it as
an Orin Nano engine/result.

If TensorRT is evaluated, build the engine on the actual
Jetson Orin Nano with its installed JetPack/TensorRT stack.

REPORTING RESTRICTIONS:
- not official MobileGeo
- retrieval is not verified UAV pose
- CRS remains unverified
- no WGS84 claim
- no meter-level geodetic claim
- no T4 timing as Orin Nano timing
