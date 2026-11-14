#!/usr/bin/env python3
"""Thin R241 cover entry for the explicitly bound shared-background geometry.

The frozen full-state spatial algorithm, all block/cap/marker/diameter/reach
gates, and every supplied position/normal/curvature/metric envelope remain
unchanged.  Only the extra original-bundle/descriptor arguments, the geometry
loader binding and output identity/schema are adapted.  There is no fallback
to the original independent-table background and no new numerical fixture.
Use only after the genuine complete parent, its own source closed bundle,
descriptor and NEW shared-background render exist.  Public Actions only.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

from geometry_20261114_large_core_saved_prefix import actions_only, sha
import geometry_20261114_full_state_continuous_cover as original
import geometry_20261114_shared_background_closed_assembly as geometry


HERE = Path(__file__).resolve().parent
SCHEMA = "R37-R241-complete-shared-background-spatial-cover-budget-v1"
EXPECTED_SOURCES = {
    "geometry_20261114_full_state_continuous_cover.py":
        "c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6",
    "geometry_20261114_shared_background_closed_assembly.py":
        "ac635c11aa31925a4175876ffa2c8b959766629aebf9e3abaf97a68ca0e096cb",
    "geometry_20261114_continuous_cover_budget_v3.py":
        "3362fc35c09b98a8feb10706f2b126c9bc45e7d45a4294c928b4b72e59d2c7a1",
    "geometry_20261114_held_hausdorff_cover.py":
        "3ba8a0d02266d2b057862c0741dc0a6f65c1276514adab8e403852d69a55809c",
}


def check_sources():
    for name,digest in {**original.EXPECTED_SOURCES,**EXPECTED_SOURCES}.items():
        if sha(HERE/name) != digest:
            raise ValueError("A frozen spatial/input source changed: "+name)
    geometry.check_sources()


def build_program():
    """Reuse the exact original transformed gate body; change input binding only."""
    baseline = original.build_program(original.GATE_SOURCE.read_text())
    program = original.replace_once(baseline,
        "    parser.add_argument('--basename', default='surface')", """    parser.add_argument('--basename', default='surface')
    parser.add_argument('--source-directory', type=Path, required=True)
    parser.add_argument('--source-basename', default='surface')
    parser.add_argument('--descriptor', type=Path, required=True)""")
    program = original.replace_once(program,
        "schema='R37-R241-complete-full-state-spatial-cover-budget-v1'",
        "schema='"+SCHEMA+"'")
    program = original.replace_once(program,
        "paths['normals'],args.checkpoint,args.port,args.config,args.tail_response,args.complete)},",
        "paths['normals'],args.checkpoint,args.port,args.config,args.tail_response,args.complete,args.descriptor)},")
    program = original.replace_once(program,
        "    result['closed_C2_inlet_normalization_enabled']=field_binding['inlet_normalization']['enabled']", """    result['closed_C2_inlet_normalization_enabled']=field_binding['inlet_normalization']['enabled']
    result['shared_background_consumer']=dict(
        loader='geometry_20261114_shared_background_closed_assembly.load_shared_bundle',
        wrapper_sha256=SHARED_CONSUMER_SOURCES['geometry_20261114_shared_background_closed_assembly.py'],
        descriptor_sha256=field_binding['shared_background_geometry']['descriptor_sha256'],
        exact_background_payload_sha256=field_binding['shared_background_geometry']['exact_background_payload_sha256'],
        original_full_state_adapter_sha256=SHARED_CONSUMER_SOURCES['geometry_20261114_full_state_continuous_cover.py'],
        original_R241_source_body_sha256=SHARED_CONSUMER_SOURCES['geometry_20261114_continuous_cover_budget_v3.py'],
        original_transformed_gate_program_sha256=ORIGINAL_TRANSFORMED_PROGRAM_SHA256,
        this_transformed_gate_program_sha256=TRANSFORMED_PROGRAM_SHA256,
        geometry_source_catalog=SHARED_CONSUMER_SOURCES,
        source_changes_only_CLI_schema_loader_binding_and_provenance=True,
        original_spatial_and_cap_and_marker_and_diameter_gates_unchanged=True,
        original_position_normal_metric_curvature_envelopes_retained=True,
        source_metric_not_replaced_by_geometric_Bprime=True,
        no_legacy_loader_fallback=True,
        continuous_envelopes_certified_here=False)""")
    return baseline,program


def main():
    actions_only()
    check_sources()
    baseline,program = build_program()
    namespace = dict(__name__="_complete_shared_background_R241_v1",
        __file__=str(Path(__file__).resolve()),
        # Deliberate binding, not the frozen original loader.  Its new prefix
        # guard rejects old-background reconstruction even if called elsewhere.
        load_full_bundle=geometry.load_shared_bundle,
        direct_centers=original.direct_centers,
        direct_normals_and_children=original.direct_normals_and_children,
        position_writer=original.position_writer,
        EXPECTED_SOURCES=original.EXPECTED_SOURCES,
        SHARED_CONSUMER_SOURCES=EXPECTED_SOURCES,
        ORIGINAL_TRANSFORMED_PROGRAM_SHA256=hashlib.sha256(baseline.encode()).hexdigest(),
        TRANSFORMED_PROGRAM_SHA256=hashlib.sha256(program.encode()).hexdigest())
    exec(compile(program,str(original.GATE_SOURCE)+"::<shared-background-loader-adapter>","exec"),namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()
