#!/usr/bin/env python3
"""The reviewed closed-map atlas with an honest fixed actual-DN source entry.

Only the source and full-height acceptance constructor is new. The complete
finite tail, Cartesian cut Hermite formulas, material phase chart, short
cylinder and canonical R67 marker use the reviewed original implementation.
Numerical queries or meshes are not continuous metric/embedding certificates.
Importing this module constructs no geometry and does not pre-cache a provider
from the wrong frozen tree before the actual fixed-return gate runs.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import qr_fixed_actual_cartesian_prefix as reader


def load_closed_map(source_run, bundle, node_check, *, cylinder_half_length=0.,
                    cut_width=.04, canonical_r67_marker=False):
    record,prefix,view,provenance = reader.load_fixed_prefix(source_run)
    _,old,_ = reader.geometry_libraries(record)

    class FixedActualClosedMap(old.ActualClosedMapV2):
        def __init__(self):
            self.record,self.prefix = record,prefix
            self.fixed_height_view = view
            self.actual_fixed_provenance = provenance
            self.cap = reader.load_complete_tail(bundle,node_check,record,view,provenance)
            self.target = old.ActualCutTarget(prefix,self.cap)
            if (not np.isfinite(cut_width) or cut_width <= 0
                    or cut_width >= prefix.flow.end-prefix.center_width):
                raise ValueError('Use one explicit positive cut width disjoint from the center repair')
            self.prefix.end_lift = old.CartesianCutLift(prefix,self.target,cut_width)
            self.phase_chart = old.PhaseAngleChart(prefix)
            self.end = prefix.flow.end
            self.a,self.Rcut = float(self.cap.cuff),self.target.R
            self.cylinder_half_length = float(cylinder_half_length)
            if not 0 <= self.cylinder_half_length <= .005:
                raise ValueError('The recorded total short-cylinder length is at most .01')
            self.marker_strength = 0.
            self.marker_radius = self.a/2
            self.r67_marker = None
            marker_source = None
            if canonical_r67_marker:
                # The reviewed marker module is in the already selected
                # original geometry tree; its actual bytes enter provenance.
                marker_path = Path(old.SCRIPTS)/'resume_20261128/tail/universal_threefold_marker.py'
                marker = reader.module('_fixed_actual_reviewed_threefold_marker',marker_path)
                self.r67_marker = marker.UniversalThreefoldMarker(self.marker_radius)
                marker_source = reader.ref(marker_path)
            native = old.checked(self.cap.bundle['native_record'])
            native_manifest = old.checked(native['manifest'])
            self.source_topic = Path(native_manifest['source_topic'])
            self.background = old.Background(self.source_topic,
                self.cap.bundle['accepted_packet']['path'])
            self.Zcap = (self.target.zcut+self.target.mean+
                self.background.sample(self.a)['heightFromRToCut'])
            self.definition_provenance = dict(source=reader.ref(__file__),
                source_kind=reader.SOURCE_KIND, source_model_kind=reader.model.KIND,
                actual_fixed_source=provenance,
                actual_complete_tail=self.cap.actual_fixed_tail_provenance,
                original_atlas_source=reader.ref(old.__file__),
                complete_cut_width_exact=str(old.Fraction(float(cut_width))),
                cylinder_half_length_exact=str(old.Fraction(self.cylinder_half_length)),
                canonical_R67_marker=bool(canonical_r67_marker),
                canonical_R67_marker_source=marker_source,
                full_tail_mean_retained=True, complete_saved_spectrum_retained=True,
                source_record_relabelled_or_rewritten=False,
                continuous_certificate_inherited=False, C2_limit_proved=False,
                complete_surface_claimed=False)

    return FixedActualClosedMap()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-run',type=Path,required=True)
    parser.add_argument('--geometry-bundle',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    parser.add_argument('--cut-width',type=float,default=.04)
    parser.add_argument('--cylinder-half-length',type=float,default=0.)
    parser.add_argument('--canonical-r67-marker',action='store_true')
    args = parser.parse_args()
    out = args.outdir.resolve()
    if out == reader.REPO or reader.REPO in out.parents:
        raise ValueError('Actual geometry records belong outside the source tree')
    out.mkdir(parents=True,exist_ok=False)
    value = load_closed_map(args.source_run,args.geometry_bundle,out/'verified-node-index.json',
        cut_width=args.cut_width,cylinder_half_length=args.cylinder_half_length,
        canonical_r67_marker=args.canonical_r67_marker)
    try:
        from qr_fixed_actual_prefix_continuous import write
        report = dict(status='own_fixed_actual_complete_map_constructed',
            definition=value.definition_provenance,
            verified_node_index=reader.ref(out/'verified-node-index.json'),
            geometry_bundle=reader.ref(args.geometry_bundle),
            complete_field_constructed=True, nonlinear_solves_executed=0,
            metric_certified=False,reach_certified=False,held_set_certified=False,
            C2_limit_proved=False,readme_completion_claimed=False)
        write(out/'definition.json',report)
        print(reader.json.dumps(dict(status=report['status'],report=reader.ref(out/'definition.json'))),flush=True)
    finally:
        value.close()


if __name__ == '__main__':
    main()
