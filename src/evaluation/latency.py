"""Latency-summary utilities."""

import numpy as np


def latency_summary(values_ms):
    values = np.asarray(
        values_ms,
        dtype=np.float64,
    )

    if values.size == 0:
        return {
            "count": 0,
            "p50_ms": None,
            "p95_ms": None,
            "p99_ms": None,
        }

    return {
        "count": int(values.size),
        "p50_ms": float(np.percentile(values, 50)),
        "p95_ms": float(np.percentile(values, 95)),
        "p99_ms": float(np.percentile(values, 99)),
        "mean_ms": float(np.mean(values)),
    }
