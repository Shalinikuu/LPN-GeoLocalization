"""Sample4Geo common benchmark adapter."""

from .base_adapter import BaseRetrievalAdapter


class Sample4GeoAdapter(BaseRetrievalAdapter):
    model_name = "Sample4Geo"
    provenance_label = "OFFICIAL_CHECKPOINT_BASELINE"

    def encode_query(self, image):
        raise NotImplementedError

    def encode_gallery(self, images):
        raise NotImplementedError

    def search(self, descriptor, top_k, optional_roi=None):
        raise NotImplementedError
