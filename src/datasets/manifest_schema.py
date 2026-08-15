"""Dataset and georeferenced-map manifest schemas."""

FRAME_REQUIRED_COLUMNS = [
    "frame_id",
    "path",
    "split",
    "class_id",
    "altitude",
    "altitude_reference",
    "source_view",
]

TILE_REQUIRED_COLUMNS = [
    "map_id",
    "tile_id",
    "path",
    "split",
    "crs",
    "pixel_bounds",
    "geographic_center",
    "geographic_polygon",
    "gsd_m_per_pixel",
    "pyramid_level",
    "source_date",
    "sha256",
]
