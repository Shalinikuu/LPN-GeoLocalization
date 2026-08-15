import torch
import torch.nn as nn
import torch.nn.functional as F

from torchvision.models import mobilenet_v3_large


MODEL_NAME = "AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION"
MODEL_PROVENANCE = "LOCAL_REIMPLEMENTATION"


class AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION(nn.Module):

    def __init__(self):

        super().__init__()

        self.backbone = mobilenet_v3_large(
            weights=None
        ).features

        self.pool = nn.AdaptiveAvgPool2d(
            (4, 1)
        )

        self.fcs = nn.ModuleList([
            nn.Linear(
                960,
                512
            )
            for _ in range(4)
        ])


    def forward(self, x):

        x = self.backbone(x)

        x = self.pool(x)

        parts = []

        for index, fc in enumerate(self.fcs):

            part = x[:, :, index, 0]

            part = fc(part)

            parts.append(part)

        descriptor = torch.cat(
            parts,
            dim=1
        )

        descriptor = F.normalize(
            descriptor,
            p=2,
            dim=1
        )

        return descriptor
