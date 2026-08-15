"""Official MobileGeo release adapter.

Valid provenance labels:
- OFFICIAL_CHECKPOINT_REPRODUCTION
- PUBLISHED_PRECOMPUTED_FEATURE_EVALUATION
- INSUFFICIENT_RELEASED_IMPLEMENTATION
"""

from .base_adapter import BaseRetrievalAdapter


class MobileGeoAdapter(BaseRetrievalAdapter):
    model_name = "MobileGeo"
    provenance_label = "UNRESOLVED_PENDING_RELEASE_AUDIT"

    def encode_query(self, image):
        raise NotImplementedError

    def encode_gallery(self, images):
        raise NotImplementedError

    def search(self, descriptor, top_k, optional_roi=None):
        raise NotImplementedError
