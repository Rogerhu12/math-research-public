"""Keep the flat-cut v1 physical metric and supply the old coast API labels.

This modifies only interface metadata, never the segment functions.  The
background flat-tail height span is exactly zero.  Nonzero R128 bending has
an angular height function and is not represented by a scalar tail span.
"""
from __future__ import annotations
import argparse, copy, hashlib, json, time
from pathlib import Path
import numpy as np
from fd2d_flat_cut_prefix_candidate import FlatCutCandidate
from fd2d_gc_design_profile import CoastDesignProfile


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    args=parser.parse_args(); started=time.monotonic(); stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh compatibility output stem')
    original=json.loads(args.source.read_text()); bundle=copy.deepcopy(original)
    changes=[]
    for segment in bundle['segments']:
        if segment.get('label')=='flat_cut_quadratic_brake':
            segment['label']='cut_second_jet_brake'
            segment['geometric_role']='flat_cut_quadratic_brake'
            changes.append('terminal piece label only')
    if len(changes)!=1:
        raise ValueError('Exactly one terminal flat brake was expected')
    bundle['cut'].update(tail_height_span=0.,tail_height_span_known=True,
        tail_height_span_scope='exact rotational A=0 background; bent tail position uses R128 full cut port')
    bundle['inputs']['flat_cut_coast_compatibility']=dict(
        source_file=args.source.name,source_sha256=digest(args.source),
        adapter=Path(__file__).name,adapter_sha256=digest(__file__),
        same_physical_metric=True)
    target=stem.with_name(stem.name+'-candidate.json')
    target.write_text(json.dumps(bundle,indent=2)+'\n')
    profile=CoastDesignProfile(target)
    base=FlatCutCandidate(original)
    compatible=FlatCutCandidate(bundle)
    grid=np.unique(np.concatenate([np.linspace(p['s0'],p['s1'],9) for p in base.segments]))
    original_values=np.array(base.profile(grid)); new_values=np.array(profile.profile(grid))
    if not np.array_equal(original_values,new_values):
        raise AssertionError('Compatibility changed a scalar metric value')
    cut=profile.jet([profile.end]); checks=[]
    for factor in (.9,1.,1.1):
        T=profile.reference_T*factor; profile.set_parameter(T)
        end=profile.jet([profile.end])
        checks.append(dict(T=T,positive_radial_scale=profile.minimum_radial_scale,
            physical_deep_coast=profile.current.segments[profile.model.deep]['L'],
            cut_jet=[float(end[key][0]) for key in ('a','a_s','a_ss')]))
    profile.set_parameter(profile.reference_T)
    angles=2*np.pi*np.arange(32)/32
    old=base.reference(np.full(32,base.end),angles)
    new=compatible.reference(np.full(32,compatible.end),angles)
    report=dict(schema='fd2d-flat-cut-coast-compatibility-v1',
        source_file=args.source.name,source_sha256=digest(args.source),
        adapter_sha256=digest(__file__),candidate_file=target.name,candidate_sha256=digest(target),
        scalar_metric_bitwise_equal=True,maximum_scalar_difference=float(abs(original_values-new_values).max()),
        cut_jet=[float(cut[key][0]) for key in ('a','a_s','a_ss')],
        A0_full_cut_two_jet_differences={key:float(abs(old[key]-new[key]).max()) for key in ('X','X_s','X_u','X_ss','X_su','X_uu')},
        T_reference=profile.reference_T,T_maximum=profile.model.Tmax,
        physical_parameter_checks=checks,coast_definition=profile.definition(),
        background_cut_height=compatible.background_cut_height,
        tail_height_span=0.,tail_height_span_scope=bundle['cut']['tail_height_span_scope'],
        seconds=time.monotonic()-started,
        scope='Actual coast API initialization and unchanged scalar definition. New T is new physical g; no nonround seam solution.')
    output=stem.with_name(stem.name+'-report.json');output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))


if __name__=='__main__':main()
