"""Geographic and location-identity split validation."""


def validate_zero_location_overlap(
    train_location_ids,
    test_location_ids,
):
    train_ids = set(train_location_ids)
    test_ids = set(test_location_ids)

    overlap = sorted(
        train_ids.intersection(test_ids)
    )

    return {
        "forbidden_location_overlap": len(overlap),
        "overlapping_location_ids": overlap,
        "passed": len(overlap) == 0,
    }
