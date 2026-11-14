#!/usr/bin/env python3
"""The explicit saturated-source Gaussian six-cap model entry point."""
from pathlib import Path

from frame_collar_polygonal_heat import main
from polygonal_tail_saturated_heat_extension import SaturatedGaussianPolygonalExtension


if __name__=='__main__':
    main(extension_factory=SaturatedGaussianPolygonalExtension,
        extra_source_files=('polygonal_tail_saturated_heat_extension.py',Path(__file__).name),
        model_label='saturated-reflection-Gaussian-c_equals_cap_width_over_4')
