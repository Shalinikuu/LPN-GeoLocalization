"""Exact cosine-similarity retrieval index."""

import numpy as np


def l2_normalize(array, axis=-1, eps=1e-12):
    array = np.asarray(array, dtype=np.float32)

    norm = np.linalg.norm(
        array,
        axis=axis,
        keepdims=True,
    )

    return array / np.maximum(norm, eps)


def cosine_topk(
    query_descriptor,
    gallery_descriptors,
    top_k=10,
):
    query = l2_normalize(
        query_descriptor
    ).reshape(1, -1)

    gallery = l2_normalize(
        gallery_descriptors
    )

    scores = (
        query @ gallery.T
    ).reshape(-1)

    top_k = min(
        int(top_k),
        len(scores),
    )

    indices = np.argsort(
        -scores
    )[:top_k]

    return indices, scores[indices]
