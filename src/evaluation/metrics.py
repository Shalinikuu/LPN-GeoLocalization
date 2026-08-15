"""Common retrieval metrics.

Metrics must be computed from complete saved rankings.
"""

import numpy as np


def recall_at_k(
    rankings,
    positive_ids,
    k,
):
    retrieved = rankings[:k]

    return float(
        any(
            candidate in positive_ids
            for candidate in retrieved
        )
    )


def average_precision(
    ranked_ids,
    positive_ids,
):
    positive_ids = set(positive_ids)

    if not positive_ids:
        return 0.0

    precision_values = []
    positives_found = 0

    for rank, candidate_id in enumerate(
        ranked_ids,
        start=1,
    ):
        if candidate_id in positive_ids:
            positives_found += 1
            precision_values.append(
                positives_found / rank
            )

    if not precision_values:
        return 0.0

    return float(
        np.sum(precision_values)
        / len(positive_ids)
    )
