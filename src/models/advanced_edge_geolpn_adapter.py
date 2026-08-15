"""Adapter for AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION.

This file must never describe the checkpoint as official MobileGeo.
"""

from .base_adapter import BaseRetrievalAdapter


class AdvancedEdgeGeoLPNAdapter(BaseRetrievalAdapter):
    model_name = "AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION"
    provenance_label = "LOCAL_REIMPLEMENTATION"

    def encode_query(self, image):
        raise NotImplementedError(
            "Connect the validated local model implementation here."
        )

    def encode_gallery(self, images):
        raise NotImplementedError(
            "Connect the validated local model implementation here."
        )

    def search(self, descriptor, top_k, optional_roi=None):
        raise NotImplementedError(
            "Connect the common retrieval index here."
        )
