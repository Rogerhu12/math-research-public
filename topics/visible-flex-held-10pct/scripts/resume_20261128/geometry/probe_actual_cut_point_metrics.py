#!/usr/bin/env python3
"""Bound exact finite angular-point metric norms of an actual cut definition.

This reuses the SHA-bound actual cut angular tables and original exact defining
jets. It neither rebuilds the 1152-stage bundle nor repeats accepted interval
leaves. A --width value defines a separately labelled cut-width design variant;
it never changes or relabels the parent field or inherited certificates.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import time

import cartesian_prefix_cut_metric as original
from cartesian_prefix_metric import NewMetric, I, fq, operator_upper, sha, np

ORIGINAL_SHA='a5b8f4f821f6b284cb124d8f2c90d471271b91f16218c8ff6157f93d609892a7'
DURABLE_SHA='d0c6f2ecbe86cf7a1995398344cf61cb7c1fa8ec087ba7e06c138c8cb6bb4144'


def binding(parent):
    if sha(original.__file__)!=ORIGINAL_SHA:
        raise ValueError('The original numerical cut definition changed')
    r=json.loads(parent.read_text())
    if (r.get('status') not in ('continuous_cut_prefix_unresolved',
            'continuous_full_cut_prefix_metric_geometry_certified')
            or r.get('source_sha256')!=DURABLE_SHA):
        raise ValueError('Require the actual original durable cut return')
    original.check_sources(r)
    for path,digest in ((r['table_report'],r['table_report_sha256']),
            (r['geometry_bundle'],r['geometry_bundle_sha256']),
            (r['cut_data']['path'],r['cut_data']['sha256'])):
        if sha(path)!=digest:raise ValueError('Actual cut binding changed: '+str(path))
    v=object.__new__(original.CutMetric)
    NewMetric.__init__(v,r['table_report'])
    if v.record['source_run_sha256']!=r['source_run_sha256']:
        raise ValueError('The complete actual prefix differs')
    with np.load(r['cut_data']['path'],allow_pickle=False) as data:
        needed={f'{tag}_cut_{j}' for tag in ('point','box') for j in range(4)}
        if set(data.files)!=needed|{'planar_modes','height_modes','cut_coefficient_enclosures'}:
            raise ValueError('The complete cut angular schema changed')
        v.cut_tables={k:I.raw(data[k].copy()) for k in needed}
    v.tables.update(v.cut_tables)
    return r,v


def point(v,s):
    values,meta=v.evaluate(s,s,'point','radial')
    aa,bb,cc=[x.v for x in values]
    trace=(aa+cc)/2
    root=(((aa-cc)/2).sq()+bb.sq()).sqrt()
    eigen=[trace+root,trace-root]
    lower=lambda x:np.maximum(0,np.maximum(x.x[0],-x.x[1]))
    norm_lower=np.maximum(lower(eigen[0]),lower(eigen[1]))
    j=int(np.argmax(norm_lower))
    return dict(s_exact=str(s),angular_index=j,angular_count_per_sector=v.N,
        angle_definition='psi=2*pi*j/(3*N), original exact material chart at phase zero',
        witness_operator_lower=float(norm_lower[j]),
        all_finite_angular_points_operator_upper=operator_upper([aa,bb,cc]),
        witness_gram_intervals=[[float(a.x[0][j]),float(a.x[1][j])] for a in (aa,bb,cc)],
        witness_eigenvalue_intervals=[[float(a.x[0][j]),float(a.x[1][j])] for a in eigen],
        **meta)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent-cut',type=Path,required=True)
    ap.add_argument('--outdir',type=Path,required=True)
    ap.add_argument('--width',type=str)
    args=ap.parse_args();parent=args.parent_cut.resolve();out=args.outdir.resolve()
    if out.exists() or 'math-research-public' in out.parts:
        raise ValueError('Use a fresh scratch result directory')
    start=time.monotonic();r,v=binding(parent)
    width=(Q(r['cut_definition']['cut_width_exact']) if args.width is None
           else fq(float(args.width)))
    v.cut_width=width;v.cut_start=v.target.end-width
    if not width>0 or not v.cut_start>v.width:
        raise ValueError('The cut and central repairs must remain disjoint')
    original_width=Q(r['cut_definition']['cut_width_exact'])
    grid=sorted({s for s in v.grid if s>=v.cut_start}|{v.cut_start,v.target.end})
    queries=sorted(set(grid+[(a+b)/2 for a,b in zip(grid[:-1],grid[1:])]))
    if width==original_width and r.get('status')=='continuous_cut_prefix_unresolved':
        boundary=Q(r['unresolved_interval'][0])
        queries=[s for s in queries if s>=boundary]
    out.mkdir(parents=True)
    rec=dict(status='actual_point_interval_queries_running',source_sha256=sha(__file__),
        parent_cut=dict(path=str(parent),sha256=sha(parent)),
        numerical_source_sha256=ORIGINAL_SHA,source_run_sha256=r['source_run_sha256'],
        geometry_bundle_sha256=r['geometry_bundle_sha256'],cut_data=r['cut_data'],
        cut_width_exact=str(width),parent_cut_width_exact=str(original_width),
        same_parent_field=(width==original_width),
        width_variant_is_new_cut_design=(width!=original_width),
        complete_continuous_metric_certificate=False,whole_surface=False,
        accepted_parent_leaves_recomputed=0,finite_point_count=len(queries))
    (out/'summary.json').write_text(json.dumps(rec,indent=2)+'\n')
    rows=[]
    with (out/'point-intervals.jsonl').open('x') as f:
        for s in queries:
            row=point(v,s);rows.append(row)
            f.write(json.dumps(row,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno())
    witness=max(rows,key=lambda row:row['witness_operator_lower'])
    violates=fq(witness['witness_operator_lower'])>Q(1,1000000)
    rec.update(status=('actual_cut_point_metric_violation_certified' if violates
                       else 'finite_point_bounds_only_no_continuous_certificate'),
        actual_completed_queries=len(rows),witness=witness,
        point_lower_exceeds_exact_one_millionth=violates,
        point_journal_sha256=sha(out/'point-intervals.jsonl'),seconds=time.monotonic()-start)
    (out/'summary.json').write_text(json.dumps(rec,indent=2,allow_nan=False)+'\n')
    print(json.dumps(rec,allow_nan=False),flush=True)


if __name__=='__main__':main()
