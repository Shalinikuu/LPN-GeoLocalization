"""UltraVPR common benchmark adapter."""

from .base_adapter import BaseRetrievalAdapter


class UltraVPRAdapter(BaseRetrievalAdapter):
    model_name = "UltraVPR"
    provenance_label = "OFFICIAL_CHECKPOINT"

    def encode_query(self, image):
        raise NotImplementedError

    def encode_gallery(self, images):
        raise NotImplementedError

    def search(self, descriptor, top_k, optional_roi=None):
        raise NotImplementedError
