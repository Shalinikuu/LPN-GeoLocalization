# Notebook 07 — Jetson Orin Nano Deployment Benchmark

## Status

**REFERENCE-HOST PREPARATION COMPLETE**

## Important limitation

An actual Jetson Orin Nano was not available in the current runtime. The detected reference host was a Tesla T4 on x86_64.

Therefore no latency, throughput, memory, or power measurement from this runtime is reported as a Jetson Orin Nano performance result.

## Model

**AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION**

- Provenance: `LOCAL_REIMPLEMENTATION`
- Parameters: 4,940,080
- Descriptor dimension: 2,048
- Input: `[B, 3, 224, 224]`
- Output descriptor: L2 normalized
- Preprocessing status: `PROVISIONAL_IMAGENET_NORMALIZATION`

## Checkpoint

- SHA256: `adc64177582638690b841c1be390b7d05dfb27f4d2001b3d52fb74455020b807`
- Strict checkpoint load: PASS

## TorchScript export

- SHA256: `b2de023d5aa71ef2013840b22945d1629b9739eb419feccd49b35c726004a02f`
- Maximum eager/export absolute error: 8.568167686462e-08
- Minimum eager/export cosine similarity: 0.999999880791
- Maximum descriptor norm error: 1.788139343262e-07
- Validated batch sizes: 1, 2, 4, 8
- Numerical equivalence: PASS

## ONNX

- ONNX Python package available: False
- ONNX exported: False
- ONNX checker passed: False

ONNX was optional for reference-host completion. Its absence does not invalidate the TorchScript deployment package.

## Jetson Orin Nano package

- Deployment ZIP SHA256: `d62c1aff79890a45569ac5464ec8a91ba0b317f3eb45212d23b22eb3b5862a2f`

The package contains:

- validated TorchScript model
- exact model definition
- Orin environment probe
- actual target benchmark runner
- deployment model manifest
- benchmark README

## Actual Orin Nano benchmark

- Hardware measured: **No**
- Latency measured: **No**
- Throughput measured: **No**
- Target CUDA memory measured: **No**
- Power measured: **No**

**Status: PENDING EXECUTION ON ACTUAL JETSON ORIN NANO**

## Reporting restrictions

- Tesla T4 timing is not Jetson Orin Nano timing.
- No TensorRT engine was built on the T4.
- Any TensorRT engine must be built on the target Jetson / JetPack / TensorRT environment.
- This is not an official MobileGeo deployment result.
- Retrieval alone is not verified UAV pose.
- CRS remains `UNVERIFIED`.
- WGS84 is not claimed.
- Meter-level geodetic accuracy is not claimed.

## Reference-host GPU metadata clarification

The original Notebook 07 Cell 1 console output reported:

- GPU: `Tesla T4`
- CUDA compute capability: `7.5`
- Machine: `x86_64`
- Jetson platform detected: `False`
- Orin Nano identity detected: `False`

The GPU and compute-capability fields were not preserved in the
machine-readable Cell 1 JSON artifacts, and the later runtime no
longer exposed CUDA. Therefore these values are retained only as
`USER_PROVIDED_NOTEBOOK07_CELL1_CONSOLE_OUTPUT` provenance.

They are not used to create or support any Jetson Orin Nano
latency, throughput, memory, power, or TensorRT performance claim.

