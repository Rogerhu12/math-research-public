#!/usr/bin/env python3
"""Use the actual R230 prefix/tail source Hessians in an R249 field transfer.

Only the prefix differential of the same saved C+W is additionally bounded.
The source is unchanged; all global C2, support, activity and true-cuff bounds
remain those of the actual full R249 report. No sampled derivative is used.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

R249_SHA='c7e5f4c82616ed43103e234ca774a6e5e95cb46e93dc18c6b2463654911fb632'
R236_SHA='f69035fe51642d30f2a1a5079c3e67f36c8cb05257df89be650cb5b015327db9'
CERT_SHA='6bc46eeeb91bb979c19c2167250ced2a8362ae92b8f8b53eacd8595408e2af57'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def packet(v,side='upper'):return {side+'_exact':str(v),'display':float(v)}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('scripts','data','field','grid','result','correction-bounds','source-bounds','two-jet-report','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--angular-cells',type=int,default=128)
    ap.add_argument('--max-prefix-depth',type=int,default=2)
    args=ap.parse_args();began=time.monotonic()
    if args.out.exists():raise FileExistsError('Fresh same-field regional output required')
    if not 0<=args.max_prefix_depth<=6:raise ValueError('Unsupported prefix refinement')
    two=read(args.two_jet_report);source=read(args.source_bounds);change=read(args.correction_bounds)
    result=read(args.result);grid=read(args.grid)
    if two['script_sha256']!=R249_SHA:raise ValueError('The proved local two-jet producer changed')
    if sha(args.scripts/'2ecf-m12-local-material-two-jet-budget.py')!=R249_SHA:
        raise ValueError('Actual R249 source is not the proved version')
    for key,path in [('field_sha256',args.field),('grid_sha256',args.grid),('solver_result_sha256',args.result),
                     ('correction_receipt_sha256',args.correction_bounds),('source_receipt_sha256',args.source_bounds)]:
        if two[key]!=sha(path):raise ValueError('Actual full two-jet input differs: '+key)
    if not all(two[k] for k in ('same_original_metric','same_actual_field','all_original_spans_and_all_angles','central_correction_included')):
        raise ValueError('Complete same-field R249 coverage required')
    if result['source'].get('source_regularization') or result.get('source_regularization'):
        raise ValueError('This version is for the original Q-free source only')
    old_path=args.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py'
    cert_path=args.scripts/'6a65-m12-r137-continuous-domain.py'
    if sha(old_path)!=R236_SHA or sha(cert_path)!=CERT_SHA:raise ValueError('Frozen exact helper changed')
    old=load('regional_R236',old_path);cert=load('regional_intervals',cert_path)
    notes=args.scripts.parent/'notes'
    names=[('2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json',old.META_SHA),
           ('2026-11-09-db6f-root-exact-bridge-m12.json',old.BRIDGE_SHA),
           ('2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json',old.MANIFEST_SHA)]
    for name,expected in names:
        if sha(notes/name)!=expected:raise ValueError('Original material input changed: '+name)
    if sha(args.data)!=old.DATA_SHA or change['script_sha256']!=old.R226_SHA:
        raise ValueError('Original data or actual central normalization receipt changed')
    if change['field_sha256']!=sha(args.field) or change['grid_sha256']!=sha(args.grid):
        raise ValueError('Actual correction receipt changed')
    if not source['continuous_all_spans_and_all_angles'] or not source['exact_common_cut_change_included']:
        raise ValueError('Both source regions must have the original complete proof')
    if source['tail_cache_sha256']!=result['query_cache_sha256'] or source['tail_report_sha256']!=result['query_report_sha256']:
        raise ValueError('Original complete tail identity differs')
    metric=old.LocalMetric(*[read(notes/n) for n,_ in names],change,cert)
    angular=old.AngularBoxes(cert,args.angular_cells,8,max_mode=max(48,2*grid['order']))
    speed,error=old.central_speed_polynomial(args.data)
    denominator=[max(old.floorfp(metric.Jmin**2),lo-error) for lo,hi in angular.enclose(speed,old.SCALE)]
    if min(denominator)<=0:raise ArithmeticError('Unresolved positive material angle scale')
    with np.load(args.field,allow_pickle=False) as data:
        coeff=data['coefficients'];knots=data['unit_knots'];pm=data['planar_modes'];zm=data['vertical_modes']
        if not np.all(np.isfinite(coeff)) or not np.all(np.isfinite(knots)):raise ValueError('Nonfinite field')
        if not np.array_equal(pm,np.arange(-grid['order'],grid['order']+1)*3+1) or not np.array_equal(zm,np.arange(grid['order']+1)*3):
            raise ValueError('Complete actual D3 angular basis required')
        coeff=[[old.fq(x) for x in row] for row in coeff];knots=list(map(old.fq,knots))
    if any(knots.count(t)>3 for t in set(knots) if 0<t<1):raise ValueError('Actual correction is not globally C2')
    pieces=old.extract_bezier(knots,coeff)
    if len(pieces)!=two['radial_pieces']:raise ValueError('Different full saved radial partition')
    # q=T*z and the true prefix ends at q=S. If lo*Tlo>=Shi the
    # entire piece is certainly in the tail. Every other piece is included
    # in the prefix sup, even if only a tiny uncertain slice intersects it.
    prefix=[(i,a,b,c,0) for i,(a,b,c) in enumerate(pieces) if a*metric.Tlo<metric.Shi]
    selected=len(prefix);accepted=[];digest=hashlib.sha256();quick=Q(1,2500000)
    while prefix:
        i,a,b,c,depth=prefix.pop()
        p,row=old.one_piece_bound(c,a,b,pm,zm,metric,angular,denominator,quick,cert)
        if p>quick and depth<args.max_prefix_depth:
            left,right=old.split_bezier(c);mid=(a+b)/2
            prefix.extend([(i,mid,b,right,depth+1),(i,a,mid,left,depth+1)]);continue
        p=old.up(p);row.update(element=i,depth=depth,total_differential_upper=str(p))
        digest.update((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode())
        accepted.append((p,row))
    prefix_p=max(p for p,row in accepted)
    values=two['rational_quantities']
    eta=Q(values['displacement']['upper_exact']);global_p=Q(values['target_differential']['upper_exact'])
    prefix_p=min(prefix_p,global_p)
    cw=Q(values['change_scaled_second_jets']['upper_exact']);eps=Q(values['metric_triangle']['upper_exact'])
    d=Q(257212,10**13);K0=Q(4763997235009095,562949953421312);R=Q(2131902881202937,1125899906842624)
    if eps>=1:raise ArithmeticError('Inherited whole-domain immersion bound is insufficient')
    cxp=Q(source['prefix_original_C_X']['upper_exact']);cxt=Q(source['tail_original_C_X']['upper_exact'])
    nu=lambda p:(3*p+p*p)/(1-d)
    kp=(K0*(1+d)+nu(prefix_p)*cxp+cw)/(1-eps)
    kt=(K0*(1+d)+nu(global_p)*cxt+cw)/(1-eps)
    K=max(K0,kp,kt);D=2*(R+eta);support=Q(737,1000)-Q(19,10)*nu(global_p)-eta
    loss=2400*eta*(1+9*eta)**2
    geometry=bool(eta<1/K0 and R+eta<2 and support>1/K and K<2000 and loss<Q(44016,10**5))
    quant={'prefix_differential':packet(prefix_p),'tail_differential':packet(global_p),
           'prefix_source_CX':packet(cxp),'tail_source_CX':packet(cxt),'prefix_curvature':packet(kp),
           'tail_curvature':packet(kt),'whole_curvature':packet(K),'diameter':packet(D),
           'support':packet(support,'lower'),'reach_over_D':packet(1/(K*D),'lower'),
           'held_over_D':packet((Q(19989114,10**8)-2*eta)/D,'lower')}
    output={'schema':'2ecf-M12-regional-source-normal-continuous-geometry-v1','script_sha256':sha(__file__),
      'field_sha256':sha(args.field),'grid_sha256':sha(args.grid),'solver_result_sha256':sha(args.result),
      'correction_receipt_sha256':sha(args.correction_bounds),'source_receipt_sha256':sha(args.source_bounds),
      'actual_two_jet_report_sha256':sha(args.two_jet_report),'R249_producer_sha256':R249_SHA,
      'R236_helper_sha256':R236_SHA,'interval_helper_sha256':CERT_SHA,'same_original_Q_free_source_and_g':True,
      'same_actual_saved_field_no_refit':True,'all_prefix_spans_and_all_angles_continuously_covered':True,
      'prefix_boundary_uncertainty_included_by_superset':True,'tail_uses_complete_inherited_global_p':True,
      'entire_phase_interval_by_original_orbit_structure':True,'prefix_selected_original_pieces':selected,
      'prefix_accepted_subpieces':len(accepted),'prefix_row_stream_sha256':digest.hexdigest(),
      'prefix_worst_subpiece':max(accepted,key=lambda item:item[0])[1],
      'rational_quantities':quant,'whole_geometry_conditions':geometry,
      'reach_over_D_above_003':bool(geometry and 1/(K*D)>Q(3,100)),
      'metric_bound_improved':False,'exact_isometry_proved':False,'README_completion_claim':False,
      'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(output,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'output':str(args.out),'report_sha256':sha(args.out),
      'quantities':{k:v['display'] for k,v in quant.items()},'whole_geometry_conditions':geometry,
      'seconds':output['seconds']},indent=2),flush=True)

if __name__=='__main__':main()
