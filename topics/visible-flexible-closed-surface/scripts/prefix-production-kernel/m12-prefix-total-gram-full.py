#!/usr/bin/env python3
"""Complete original-prefix correlated total Gram with analytic refinements.

Every true source/chart/target/C/W intersection is covered by a validated
outer rectangle. Source common-cut and angular cutoff pieces, both ramps,
and the exact-root bridge are explicitly consumed. Only the actual saved
field is certified; no endpoint sample or partial run is a complete result.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,io,json,sys,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np

def load(name,path):
    if name in sys.modules:return sys.modules[name]
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
source=load('m12_original_prefix_full_interval_source',Path(__file__).with_name('m12-original-prefix-source-interval.py'))
base=source.base;kern=source.kern;I,Jet,LD=kern.I,kern.Jet,kern.LD;arrq=base.arrq;fq=base.fq
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def packet(v):return {'upper_exact':str(kern.exact(v)),'display':float(v)}

def intersections(D,piece):
    wl=max(F(0),piece[0]*D.Klo);wr=min(D.end,piece[1]*D.Khi)
    if wr<=wl:return {},(wl,wr)
    cells=[i for i in range(len(D.mesh)-1) if D.mesh[i+1]>wl and D.mesh[i]<wr];groups={};segments=[]
    for cell in cells:
        nl=max(D.mesh[cell],wl);nr=min(D.mesh[cell+1],wr)
        for j,ch in enumerate(D.chart_pieces):
            jl=max(nl,ch['left']);jr=min(nr,ch['right'])
            if jr<=jl:continue
            for pk,tp in enumerate(D.target_pieces):
                pl=max(jl,tp['native_left']);pr=min(jr,tp['native_right'])
                if pr<=pl:continue
                for active,cl,cr in ((True,F(0),D.lamhi*D.h),(False,D.lamlo*D.h,D.end)):
                    ll=max(pl,cl);rr=min(pr,cr)
                    if rr<=ll:continue
                    common=cell>=D.common_start
                    row={'cell':cell,'left':ll,'right':rr,'chart':j,'target':pk,'central_active':active,'common_cut_active':common,'radial_depth':0}
                    groups.setdefault((j,pk,active,common),[]).append(row);segments.append((ll,rr))
    covered=wl
    for l,r in sorted(segments):
        if l>covered:raise ArithmeticError('Whole-prefix analytic common refinement leaves a gap')
        covered=max(covered,r)
    if covered<wr:raise ArithmeticError('Uncovered end of whole-prefix element envelope')
    return groups,(wl,wr)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('scripts','data','field','grid','result','correction-bounds','query-report','query-cache','out'):ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--full-prefix',action='store_true');ap.add_argument('--elements',type=int,nargs='+')
    ap.add_argument('--angular',type=int,default=32);ap.add_argument('--max-angular',type=int,default=128)
    ap.add_argument('--nr',type=int,default=6);ap.add_argument('--na',type=int,default=12);ap.add_argument('--batch',type=int,default=8)
    ap.add_argument('--target',default='0.000000002');ap.add_argument('--max-radial-depth',type=int,default=5)
    a=ap.parse_args();began=time.monotonic();threshold=F(a.target)
    if a.full_prefix==bool(a.elements):raise ValueError('Choose full prefix or explicit elements')
    if a.out.exists():raise FileExistsError('A complete report must be new')
    paths=[Path(__file__),Path(base.__file__),Path(kern.__file__),Path(base.centralmod.__file__),Path(source.__file__)]
    frozen={p.name:sha(p) for p in paths}
    notes=a.scripts.parent/'notes';metap=notes/'2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json';bridgep=notes/'2026-11-09-db6f-root-exact-bridge-m12.json'
    old=load('full_prefix_original_native_cells',a.scripts/'6a65-m12-up-patch-exact-geometry-budget.py');B=load('full_prefix_original_Bernstein',a.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py');supplier=load('full_prefix_original_chart',a.scripts/'78718-prefix-metric-supplier-storage-v1.py')
    if sha(a.data)!=B.DATA_SHA or sha(metap)!=B.META_SHA or sha(bridgep)!=B.BRIDGE_SHA:raise ValueError('Original exact source definition differs')
    meta=json.loads(metap.read_text());bridge=json.loads(bridgep.read_text());grid=json.loads(a.grid.read_text());result=json.loads(a.result.read_text());cor=json.loads(a.correction_bounds.read_text())
    for r in (result,cor):
        if r['field_sha256']!=sha(a.field) or r['grid_sha256']!=sha(a.grid):raise ValueError('Same-field binding differs')
    if not result['original_exact_metric_unchanged'] or not cor['continuous_all_knots_and_all_angles']:raise ValueError('Original target/finite C2 field facts missing')
    with np.load(io.BytesIO(gzip.decompress(a.data.read_bytes())),allow_pickle=False) as f:raw={k:f[k].copy() for k in ('mesh','jets','mean_increments')}
    D=source.FullSource(raw,meta,bridge,supplier,old,a.query_report,a.query_cache,result)
    rows=[[fq(x) for x in row] for row in raw['jets'][:,0,:]];arc=cor['central_arc_and_partial_primitive_proof']
    C=base.centralmod.Central(rows,D.warp*D.chart[0][0],2*D.warp*D.chart[0][2]/D.end**2,(F(arc['mean_arc_radius_lower_exact']),F(arc['mean_arc_radius_upper_exact'])))
    with np.load(a.field,allow_pickle=False) as f:
        knots=list(map(fq,f['unit_knots']));coef=[[fq(x) for x in row] for row in f['coefficients']];pm=f['planar_modes'].copy();zm=f['vertical_modes'].copy()
        if np.iscomplexobj(f['coefficients']) or not np.all(np.isfinite(f['coefficients'])):raise ValueError('Real finite coefficients required')
    if not np.array_equal(pm,3*np.arange(-grid['order'],grid['order']+1)+1) or not np.array_equal(zm,3*np.arange(grid['order']+1)):raise ValueError('Exact D3/reflection Fourier structure changed')
    pieces=B.extract_bezier(knots,coef)
    elements=[i for i,p in enumerate(pieces) if p[0]*D.Klo<D.end] if a.full_prefix else a.elements
    angle_cache={};angle_boxes={};records=[];covered_elements=[];element_rows=[]
    def angles(count):
        if count not in angle_boxes:
            e=[kern.PI*F(j,3*count) for j in range(count+1)]
            angle_boxes[count]=I(np.array([[x.lo for x in e[:-1]]]),np.array([[x.hi for x in e[1:]]]))
        return angle_boxes[count]
    def save_progress():
        out={'complete_certificate':False,'field_sha256':sha(a.field),'requested_elements':elements,'completed_elements':covered_elements,
             'completed_actual_intersection_pieces':len(records),'maximum_so_far':max((r['relative_metric_upper']['display'] for r in records),default=0),
             'last_rows':records[-8:],'seconds':time.monotonic()-began,'frozen_sources':frozen}
        p=a.out.with_suffix(a.out.suffix+'.progress.json');tmp=p.with_suffix(p.suffix+'.tmp');tmp.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');tmp.replace(p)
    print(json.dumps({'initialized_seconds':time.monotonic()-began,'elements':len(elements),'central_audit':C.audit,'bridge_audit':D.bridge_target.audit}),flush=True)
    for element in elements:
        p=pieces[element];groups,envelope=intersections(D,p)
        if not groups:continue
        W=base.SavedW(p,pm,zm,D.total);startrows=len(records)
        for (j,pk,active,common),group in groups.items():
            ch=D.chart_pieces[j];tp=D.target_pieces[pk];todo=[group[k:k+a.batch] for k in range(0,len(group),a.batch)]
            while todo:
                chunk=todo.pop(0);native=D.native_batch([r['cell'] for r in chunk]);consumer=base.PrefixPiece(native,W,C,D.lam,D.total,ch['coefficients'],ch['origin'],D.end,tp['evaluator'],D.h,active,angle_cache)
                left=arrq([r['left'] for r in chunk]);right=arrq([r['right'] for r in chunk]);radial=I(left.lo[:,None],right.hi[:,None])
                count=a.angular;b=time.monotonic()
                while True:
                    enclosures=kern.tensor_enclose(consumer,radial,angles(count),a.nr,a.na)
                    norm=kern.matrix_norm_bound(*[row['upper'] for row in enclosures])
                    if kern.exact(np.max(norm))<=threshold or count>=a.max_angular:break
                    count=min(2*count,a.max_angular)
                retry=[]
                for ix,part in enumerate(chunk):
                    maximum=np.max(norm[ix])
                    if kern.exact(maximum)>threshold and part['radial_depth']<a.max_radial_depth:
                        mid=(part['left']+part['right'])/2
                        retry.extend([{**part,'right':mid,'radial_depth':part['radial_depth']+1},
                                      {**part,'left':mid,'radial_depth':part['radial_depth']+1}]);continue
                    worst=int(np.argmax(norm[ix]));detail=[]
                    for row in enclosures:
                        detail.append({k:packet(np.max(v[ix])) for k,v in row.items() if k not in ('node_min','node_max')})
                    rec={'element':element,'source_cell':part['cell'],'native_outer_interval':[str(part['left']),str(part['right'])],
                         'source_chart_piece':ch['source_index'],'chart_cutoff_active':ch['cutoff_active'],
                         'target_kind':tp['kind'],'target_piece':tp['piece'],'original_common_cut_active':common,
                         'original_central_C_active':active,'angular_fundamental_boxes':count,'radial_depth':part['radial_depth'],
                         'relative_metric_upper':packet(maximum),'below_B':kern.exact(maximum)<=threshold,
                         'worst_angular_box':worst,'component_bounds':detail}
                    records.append(rec)
                if retry:todo[0:0]=[retry[k:k+a.batch] for k in range(0,len(retry),a.batch)]
                print(json.dumps({'element':element,'last_source_cell':chunk[-1]['cell'],'pieces_done':len(records),
                    'batch_max':float(np.max(norm)),'angular':count,'radial_retry':len(retry),'batch_seconds':time.monotonic()-b,'seconds':time.monotonic()-began}),flush=True)
                save_progress()
        covered_elements.append(element);element_rows.append({'element':element,'native_outer_envelope':list(map(str,envelope)),
            'intersection_leaves':len(records)-startrows,'continuous_upper':max((r['relative_metric_upper']['display'] for r in records[startrows:]),default=0)})
        for path in paths:
            if sha(path)!=frozen[path.name]:raise RuntimeError('Loaded implementation changed during an element certificate')
        element_dir=a.out.with_suffix(a.out.suffix+'.elements');element_dir.mkdir(exist_ok=True)
        element_report={'schema':'2ecf-original-M12-complete-prefix-element-total-Gram-v1','complete_actual_element_prefix_intersection':True,
            'whole_prefix_complete':False,'frozen_sources':frozen,'data_sha256':sha(a.data),'field_sha256':sha(a.field),
            'grid_sha256':sha(a.grid),'solver_result_sha256':sha(a.result),'correction_bounds_sha256':sha(a.correction_bounds),
            'query_report_sha256':sha(a.query_report),'query_cache_sha256':sha(a.query_cache),'meta_sha256':sha(metap),'bridge_sha256':sha(bridgep),
            'original_exact_g_retained':True,'actual_original_X_plus_C_plus_saved_W':True,'Q_source_regularization_included':False,
            'all_angles_by_verified_D3_and_reflection':True,'element':element_rows[-1],
            'requested_B_exact':str(threshold),'below_B':all(r['below_B'] for r in records[startrows:]),
            'all_intersections':records[startrows:],'central_exact_arclength':C.audit,'bridge_exact_target':D.bridge_target.audit,
            'common_cut_source':D.common_audit,'tensor_degrees':[a.nr,a.na],'seconds_to_complete_element':time.monotonic()-began}
        ep=element_dir/f'element-{element:04d}.json'
        if ep.exists():raise FileExistsError('Per-element certificates must not be overwritten')
        ep.write_text(json.dumps(element_report,indent=2,allow_nan=False)+'\n')
        save_progress()
    for p in paths:
        if sha(p)!=frozen[p.name]:raise RuntimeError('Loaded implementation changed during certificate run')
    worst=max(records,key=lambda r:F(r['relative_metric_upper']['upper_exact']));maximum=F(worst['relative_metric_upper']['upper_exact'])
    complete=a.full_prefix and covered_elements==elements
    out={'schema':'2ecf-original-M12-whole-prefix-correlated-total-Gram-v1','frozen_sources':frozen,
        'data_sha256':sha(a.data),'field_sha256':sha(a.field),'grid_sha256':sha(a.grid),'solver_result_sha256':sha(a.result),
        'correction_bounds_sha256':sha(a.correction_bounds),'query_report_sha256':sha(a.query_report),'query_cache_sha256':sha(a.query_cache),
        'meta_sha256':sha(metap),'bridge_sha256':sha(bridgep),'original_exact_g_retained':True,'actual_original_X_plus_C_plus_saved_W':True,
        'Q_source_regularization_included':False,'old_uniform_source_d0_not_added':True,'full_nonlinear_Gram_before_absolute_values':True,
        'all_angles_by_verified_D3_and_reflection':True,'all_source_chart_target_C_W_actual_intersections_covered':True,
        'original_common_cut_and_chart_cutoff_explicitly_included':True,'whole_prefix_complete':complete,'whole_surface_complete':False,
        'requested_B_exact':str(threshold),'below_B':maximum<=threshold,'relative_metric_upper_exact':str(maximum),'relative_metric_upper':float(maximum),
        'worst_intersection':worst,'elements':element_rows,'all_intersections':records,'central_exact_arclength':C.audit,
        'bridge_exact_target':D.bridge_target.audit,'common_cut_source':D.common_audit,'tensor_degrees':[a.nr,a.na],
        'complete_real_interval_jet_remainders_paid':True,'exact_isometry_proved':False,'README_completion_claim':False,'seconds':time.monotonic()-began}
    a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps({'report':str(a.out),'complete_prefix':complete,'metric_upper':float(maximum),'seconds':out['seconds']}),flush=True)
if __name__=='__main__':main()
