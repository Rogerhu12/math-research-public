#!/usr/bin/env python3
"""Observe the same whole-half field at original tail microspan points.

Exact source radii/coefficients are supplied by the companion checked
streamer. Each radius is mapped back by the R223 common-chart inverse.
The same saved Cartesian B-spline field and physical-s six-jet packet are
then used at that point. This is a finite numerical observer, not a
continuous metric enclosure. Raw point arrays remain temporary.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

LD=np.longdouble
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result);return result

def point_metric(packet,bb):
    a,b=packet[:,1],packet[:,2]
    e=np.sum(a*a,axis=-1)-1
    f=np.sum(a*b,axis=-1)/bb
    g=np.sum(b*b,axis=-1)/(bb*bb)-1
    op=np.abs((e+g)/2)+np.sqrt(((e-g)/2)**2+f*f)
    angles=np.argmax(op,axis=1)
    return op[np.arange(len(op)),angles],angles

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('scripts','data','grid','query-report','query-cache','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--field',type=Path);ap.add_argument('--result',type=Path)
    ap.add_argument('--reference-only',action='store_true')
    ap.add_argument('--angular',type=int);ap.add_argument('--block',type=int,default=12)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh microspan observation required')
    if args.reference_only:
        if args.field or args.result:raise ValueError('Reference-only observer takes no saved field')
    elif not args.field or not args.result:
        raise ValueError('Actual field observer requires both field and result')
    start=time.monotonic()
    whole=load('microspan_same_whole_model',args.scripts/'6a65-m12-entire-half-cartesian-bvp.py')
    joint=load('microspan_same_joint_model',args.scripts/'6a65-m12-global-common-cut-position-recovered.py')
    bg_module=load('microspan_original_background',args.scripts/'6a65-m12-original-tail-background.py')
    grid=json.loads(args.grid.read_text());query=json.loads(args.query_report.read_text())
    args.background_tolerance=grid['background_tolerance']
    notes,meta_path,bridge_path,meta,native,chart=whole.definition(args,joint,bg_module)
    for key,path in [('data_sha256',args.data),('common_meta_sha256',meta_path),('bridge_sha256',bridge_path),
                     ('joint_source_sha256',Path(joint.__file__)),('background_source_sha256',Path(bg_module.__file__))]:
        if grid[key]!=sha(path):raise ValueError('Changed same-field definition '+key)
    tail=whole.TailQueries(args.query_report,args.query_cache)
    if not args.reference_only:
        result=json.loads(args.result.read_text())
        for key,path in [('field_sha256',args.field),('grid_sha256',args.grid),
                         ('query_report_sha256',args.query_report),('query_cache_sha256',args.query_cache)]:
            if result[key]!=sha(path):raise ValueError('Actual saved field/source mismatch '+key)
    with np.load(args.query_cache,allow_pickle=False) as cache:
        fractions=cache['diagnostic_fraction'].copy()
        radii=cache['diagnostic_radius'].copy()
        values=cache['diagnostic_coefficients'].copy()
        source_spans=cache['diagnostic_source_span'].copy()
    if len(radii)==0 or len(radii)!=query['diagnostic_query_count']:
        raise ValueError('Original source-span diagnostic queries were not regenerated')
    lookup={whole.exact_key(r):values[i] for i,r in enumerate(radii)}
    if len(lookup)!=len(radii):raise ValueError('Diagnostic radii collide at numerical precision')
    base_coefficient=tail.coefficient
    def coefficient(r):
        key=whole.exact_key(r)
        return lookup[key] if key in lookup else base_coefficient(r)
    tail.coefficient=coefficient
    src=joint.CommonCutSource(args.data,meta_path,bridge_path,args.query_report,args.query_cache)
    unused,c=joint.ad.exact_section(args.data,Q(0));central=joint.ad.NativeCurve(c,512,32)
    position=whole.WholePosition(src,central,chart,tail,joint)
    mesh=np.asarray(grid['unit_mesh']);basis=whole.basis_for(joint,mesh,grid['order'],chart)
    if args.reference_only:
        coeff=np.zeros((basis.nb,basis.na))
    else:
        with np.load(args.field,allow_pickle=False) as field:
            coeff=field['coefficients'].copy()
            if not np.array_equal(field['unit_knots'],basis.knots) or not np.array_equal(field['planar_modes'],basis.pm) or not np.array_equal(field['vertical_modes'],basis.zm):
                raise ValueError('Saved field basis identity mismatch')
    if coeff.shape!=(basis.nb,basis.na):raise ValueError('Incomplete saved Cartesian field')
    N=args.angular or 2*grid['angular']
    if N<=2*(3*grid['order']+1):raise ValueError('Aliased Cartesian field observer')
    z=np.asarray([float(chart.inverse_radius(r)) for r in radii])
    roundtrip=np.asarray([chart.radius(x)[0]-r for x,r in zip(z,radii)],LD)
    if np.max(abs(roundtrip))>LD('1e-14'):raise ArithmeticError('Original-radius/common-q inverse did not settle')
    before=np.empty(len(z));after=np.empty(len(z))
    before_angle=np.empty(len(z),int);after_angle=np.empty(len(z),int)
    for sl in joint.stream.chunks(len(z),args.block):
        packets=[];radii_target=[]
        for r in radii[sl]:
            p,bb=position.tail_point(r,N);packets.append(p);radii_target.append(bb)
        p=np.asarray(packets);bb=np.asarray(radii_target)
        before[sl],before_angle[sl]=point_metric(p,bb)
        p+=joint.stream.packet(basis,basis.matrices(z[sl]),coeff,N)
        after[sl],after_angle[sl]=point_metric(p,bb)
    qi0=int(np.argmax(before));qi1=int(np.argmax(after))
    source_rows=[]
    for source_span in np.unique(source_spans):
        ids=np.flatnonzero(source_spans==source_span)
        a=ids[np.argmax(before[ids])];b=ids[np.argmax(after[ids])]
        source_rows.append({'source_span':int(source_span),'points':len(ids),
                            'before_peak':float(before[a]),'after_peak':float(after[b]),
                            'after_peak_q':float(z[b]*chart.total),'after_peak_r':str(radii[b])})
    source_rows.sort(key=lambda row:row['after_peak'],reverse=True)
    def peak(i,metric,angle):
        return {'metric_peak':float(metric[i]),'radius_exact':str(fractions[i]),
                'radius_numerical':str(radii[i]),'common_q_numerical':float(z[i]*chart.total),
                'source_span':int(source_spans[i]),'angle_index':int(angle[i]),'angular_nodes':N,
                'whole_basis_element':min(len(mesh)-2,max(0,int(np.searchsorted(mesh,z[i],side='right')-1)))}
    raw=Path(str(args.out)+'.npz')
    np.savez_compressed(raw,radius_fraction=fractions,radius=radii,unit_common_coordinate=z,
                        source_span=source_spans,metric_before=before,metric_after=after,
                        before_peak_angle=before_angle,after_peak_angle=after_angle,
                        inverse_radius_roundtrip=roundtrip)
    report={'schema':'6a65-M12-actual-field-original-microspan-observer-v1',
            'script_sha256':sha(__file__),'reference_only':args.reference_only,
            'field_sha256':sha(args.field) if args.field else None,'result_sha256':sha(args.result) if args.result else None,
            'grid_sha256':sha(args.grid),'query_report_sha256':sha(args.query_report),
            'query_cache_sha256':sha(args.query_cache),'raw_observation_sha256':sha(raw),
            'data_sha256':sha(args.data),'points':len(radii),'source_spans':len(source_rows),
            'angular_nodes':N,'window_exact':query['diagnostic_window_exact'],
            'original_span_subdivisions':query['diagnostic_subdivisions'],
            'inverse_common_q_to_radius_max_residual_numerical':str(np.max(abs(roundtrip))),
            'before':peak(qi0,before,before_angle),'after':peak(qi1,after,after_angle),
            'top_source_spans_after':source_rows[:12],
            'same_original_g':True,'same_actual_field_and_physical_s_jets':True,
            'observer_only_no_finite_space_refit':True,'continuous_metric_certificate':False,
            'exact_isometry_proved':False,'raw_retention':'Temporary runner/local cache only; never Git/artifact/release.',
            'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,indent=2,allow_nan=False))

if __name__=='__main__':main()

