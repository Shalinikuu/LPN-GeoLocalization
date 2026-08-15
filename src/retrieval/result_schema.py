"""Standard retrieval handoff record schema."""

RETRIEVAL_STATUSES = {
    "ACCEPTED_FOR_VERIFICATION",
    "AMBIGUOUS",
    "OUT_OF_MAP",
    "INVALID_INPUT",
    "SYSTEM_ERROR",
}

REQUIRED_QUERY_FIELDS = [
    "frame_id",
    "capture_timestamp_ns",
    "camera_calibration_id",
    "model_name",
    "model_version",
    "checkpoint_sha256",
    "preprocessing_hash",
    "map_id",
    "map_hash",
    "index_hash",
    "search_mode",
    "top_k_candidates",
    "top1_top2_margin",
    "calibrated_topk_probability",
    "candidate_geographic_dispersion_m",
    "retrieval_status",
    "decode_ms",
    "preprocess_ms",
    "inference_ms",
    "search_ms",
    "end_to_end_ms",
]
