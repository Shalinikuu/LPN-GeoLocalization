"""Common retrieval-model adapter interface."""

from abc import ABC, abstractmethod
from typing import Any, List, Optional


class BaseRetrievalAdapter(ABC):
    """Common interface used by every retrieval backend."""

    model_name: str = "UNDEFINED"
    provenance_label: str = "UNDEFINED"

    @abstractmethod
    def encode_query(self, image: Any):
        """Return one normalized query descriptor."""
        raise NotImplementedError

    @abstractmethod
    def encode_gallery(self, images: List[Any]):
        """Return normalized gallery descriptors."""
        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        descriptor,
        top_k: int,
        optional_roi: Optional[Any] = None,
    ):
        """Return ranked retrieval candidates."""
        raise NotImplementedError
