#!/usr/bin/env python3
"""Same-field finite641 substitution with actual centre mass and full T.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Uses the R106 exact quadratic and R116 complete mean/inverse Hessian.
The old complete low/far affine comparison remains an intersected bound.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
from flint import arb,arb_mat,ctx

PINS={
 'jacobian':('2026-11-12-closure-strong-parameter-jacobian-r1.json.gz','7b9d5f6bafe69879246ee5edffbfdd280bfec0b5207c5ea6f79959fc3b61dfc4'),
 'split':('2026-11-12-tail-r42-strong-same-tau-r1-split.json.gz','b31ba4868bf825fe19981af820f92d798161df027519992b9380a4b9f7f6b5dd'),
 'density':('2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
 'low':('2026-11-12-closure-strong-same-tau-four-green-r1.json.gz','841c42ff527f2ca3846abf7ede8e9e03eb296a1f979cf7b01f48069197d312ac'),
}


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)


def ab(v):
    if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
    if 'upper' in v:return ab(v['upper'])
    if 'mantissa' in v:return arb(int(v['mantissa']))*arb(2)**int(v['binary_exponent'])
    return arb(int(v['numerator']))/int(v['denominator'])


def ex(v):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    if 'upper' in v:return ex(v['upper'])
    if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']),int(v['denominator']))


def pack(z,bits=160):
    if not z.is_finite():raise ArithmeticError('Every complete finite-map coefficient must be finite')
    t=z.upper()
    if not t>=0:raise ArithmeticError('Positive comparison became negative')
    if t==0:return ['0',0]
    m,e=t.man_exp();m,e=int(m),int(e);q=max(0,m.bit_length()-bits)
    if q:m,e=(m+(1<<q)-1)>>q,e+q
    if not ab([m,e])>=t:raise ArithmeticError('Outward dyadic rounding failed')
    return [str(m),e]


def up(z):return ab(pack(z))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('topic','modal-input','source-summary','source-resource','old-bootstrap','old-resource','out-prefix'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--steps',type=int,default=128);p.add_argument('--rss-kib',type=int,default=98304)
    a=p.parse_args();ctx.prec=256;ctx.threads=1;started=time.monotonic();out=Path(str(a.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('Preserve original actual nonlinear bootstrap attempts')
    if not 1<=a.steps<=512:raise ValueError('Declare a finite substitution count')
    sys.path.insert(0,str(a.topic/'computations'))
    from closure_split_joint_io_v2 import read_field,iter_array,metadata_without_array
    paths={k:a.topic/'notes'/v[0] for k,v in PINS.items()};ids={}
    for k,path in paths.items():
        if sha(path)!=PINS[k][1]:raise ArithmeticError('Pinned original input differs: '+k)
        ids[k]=dict(path=str(path),sha256=sha(path))
    for k in ('modal_input','source_summary','source_resource','old_bootstrap','old_resource'):
        path=getattr(a,k);ids[k]=dict(path=str(path),sha256=sha(path))
    old,oldusage,modal,source,usage=(read(getattr(a,k)) for k in ('old_bootstrap','old_resource','modal_input','source_summary','source_resource'))
    if not(old['all_gates'] and all(old['gates'].values()) and old['schema']=='visible-flex-same-R100-full641-finite-positive-bootstrap-v1'
           and oldusage['exitcode']==0 and oldusage['termination_signal'] is None and modal['all_gates'] and source['all_gates']
           and all(source['gates'].values()) and source['all213_original_cells'] and usage['exitcode']==0 and usage['termination_signal'] is None):raise ArithmeticError('Completed actual same-field inputs required')
    if source['input_hashes'].get(str(a.modal_input))!=sha(a.modal_input) or source['input_hashes'].get(str(paths['density']))!=sha(paths['density']):raise ArithmeticError('Source and centre modal inputs differ')
    if not(modal['schema']=='inner-R100-Cs-Lambda-restricted-profile-modal-input-v1' and ex(modal['R100_envelope_scale'])==F(257,256) and 0<ex(modal['domain']['S_product_radius'])<=1 and 0<ex(modal['domain']['T_l1_radius'])<=F(1,32) and modal['domain']['simultaneous_original_coordinates'] and source['domain']==modal['domain'] and modal['cells']==list(range(12,225)) and modal['modes']==list(range(2,93,2))):raise ArithmeticError('Actual restricted original R100 parameter profile required')
    W=list(map(ab,old['same_original_metric_weights']));v=arb_mat(641,1)
    for i,z in enumerate(old['full641_checkpoints'][-1]['all641_W_scaled_caps']):v[i,0]=ab(z)
    S=arb(257)/256;Theta=arb(16705)/16384;Z=arb(2)**-2200
    density=read(paths['density']);split=metadata_without_array(paths['split'],'gamma_rows')
    C=[ab(r['Cs_common_cap']) for r in modal['rows']]
    L=[ab(r['Lambda_common_cap_on_domain']) for r in modal['rows']]
    B=[ab(r['Cs_plus_Lambda_common_cap']) for r in modal['rows']]
    aa=[up(S*ab(r['V_over_w_upper'])) for r in density['rows']]
    # Actual source kernels: field target divides by V', far target does not.
    base=read_field(paths['low'],'base');GL=arb_mat(213,213)
    if len(base)!=213 or any(len(row)!=213 for row in base):raise ArithmeticError('Complete low base source matrix required')
    for k,row in enumerate(base):
        for n,z in enumerate(row):GL[k,n]=S*ab(z)
    del base
    gf=read_field(paths['low'],'far_z_source_upper');GF=arb_mat(1,213)
    for n,z in enumerate(gf['base']):GF[0,n]=S*S*ab(z)/Z
    del gf
    ML=arb_mat(214,641);seen=set()
    for row in iter_array(paths['jacobian'],'rows'):
        i=row['index']
        if i<213 or i==640:
            k=i if i<213 else 213;seen.add(i)
            for j,m,e in row['coefficients']:ML[k,j]=Theta*ab([m,e])
    if seen!=set(list(range(213))+[640]):raise ArithmeticError('All original low/far affine rows required')
    GH={g:arb_mat(213,213) for g in ('near','rest')};pure={g:[arb(0)]*213 for g in GH};farhigh={g:[] for g in GH}
    q={g:[ab(r['source_common_mass']['common_d'][band]) for r in source['rows']] for g,band in [('near','near94to184'),('rest','rest186to8190'),('infinite','infinite8192up')]}
    for k,row in enumerate(iter_array(paths['split'],'gamma_rows')):
        if row['output_cell']!=k+12 or len(row['sources'])!=213-k:raise ArithmeticError('Complete original causal triangles required')
        for n,e in enumerate(row['sources'],k):
            if e['source_cell']!=n+12:raise ArithmeticError('Original causal source reordered')
            for g in GH:GH[g][k,n]=S*ab(e[g+'_gamma']);pure[g][k]+=GH[g][k,n]*q[g][n]
        for g in GH:farhigh[g].append(ab(split['cells'][k]['far_boundary_'+g])/S)
    GI=S*ab(density['gamma_high']);PI=up(GI*sum(q['infinite'],arb(0)));FI=ab(split['deep_high_boundary'])/S
    direct_far=ab(modal['far_common_on_domain'])/Z
    lowbase=[ab(old['affine_source_W_scaled'][i]) for i in list(range(213))+[640]]
    # Original high far derivatives are4F_i with respect to e_z; R100
    # uniform Theta inflation remains safe after changing the target norm.
    fhighcoef={g:[Theta*4*ab(split['cells'][k]['far_boundary_'+g]) for k in range(213)] for g in GH}
    ficoef=Theta*4*ab(split['deep_high_boundary'])
    hist=[];vectors=[];source_final=None;map_final=None
    def checkpoint(step):
        hs=[up(v[i,0]*W[i]*ab(old['point_physical_epsilon_prime'])) for i in (213,426,639)]
        hist.append(dict(step=step,head_complete_balanced_P_K_by_band=list(map(pack,hs))))
        vectors.append(dict(step=step,all641_W_scaled_caps=[pack(v[i,0]) for i in range(641)]))
        print(json.dumps(dict(event='same_R100_complete_nonlinear641_finite_substitution',step=step,head_display=list(map(str,hs)),elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    checkpoint(0)
    for step in range(1,a.steps+1):
        raw=[up(v[i,0]*W[i]) for i in range(641)];Src=arb_mat(213,1);H={g:arb_mat(213,1) for g in ('near','rest','infinite')};sources=[]
        for n in range(213):
            lo,ne,re,hi=raw[n],raw[213+n],raw[426+n],raw[639];t=up(lo+ne+re+hi);var=up(L[n]+t)
            if not(t+L[n]<arb(2)**-30 and aa[n]*(B[n]+t)<arb(1)/128):raise ArithmeticError('Complete original source Hessian domain unpaid')
            # Low/far source is N(Cs+Lambda+e)-N(Cs).
            rlow=up(270*aa[n]*(C[n]+var)*(C[n]*var+var*var/2))
            Src[n,0]=up((arb(23)/9)*C[n]*var+(arb(23)/18)*var*var+rlow)
            # High source is N(Cs+Lambda)+DN and complete new-square/T.
            rhi=up(270*aa[n]*(B[n]+t)*(B[n]*t+t*t/2));sq=up((arb(23)/18)*t*t)
            active={'near':lo+ne+re,'rest':ne+re+hi,'infinite':re+hi}
            for g in H:H[g][n,0]=up((arb(23)/9)*B[n]*active[g]+sq+rhi)
            if step==a.steps:sources.append(dict(cell=n+12,total_error=pack(t),low_lambda_plus_error=pack(var),low_complete_source=pack(Src[n,0]),high_complete_mean_inverse_difference=pack(rhi),high_new_quadratic=pack(sq),high_sources={g:pack(H[g][n,0]) for g in H}))
        oldlow=ML*v;newlow=GL*Src;newfar=(GF*Src)[0,0]+direct_far;high={g:GH[g]*H[g] for g in GH};infinite=GI*sum((H['infinite'][n,0] for n in range(213)),arb(0))
        nxt=[v[i,0] for i in range(641)]
        for k in range(213):
            affine=up(oldlow[k,0]+lowbase[k]);generic=up(newlow[k,0]/W[k]+ML[k,640]*v[640,0])
            nxt[k]=min(nxt[k],affine,generic)
            for g,off in [('near',213),('rest',426)]:nxt[off+k]=min(nxt[off+k],up((pure[g][k]+farhigh[g][k]+high[g][k,0]+fhighcoef[g][k]*raw[640])/W[off+k]))
        nxt[640]=min(nxt[640],up(oldlow[213,0]+lowbase[213]),up(newfar/W[640]+ML[213,640]*v[640,0]))
        nxt[639]=min(nxt[639],up((PI+FI+infinite+ficoef*raw[640])/W[639]))
        for i,z in enumerate(nxt):
            if not(z.is_finite() and z>0 and z<=v[i,0]):raise ArithmeticError('Complete monotone finite substitution failed')
            v[i,0]=z
        if step&(step-1)==0 or step==a.steps:checkpoint(step)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned actual nonlinear641 RSS guard')
        if step==a.steps:source_final=sources
    result=dict(schema='same-R100-restricted-complete-nonlinear641-finite-bootstrap-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,
      gates=dict(same_existing_full_R100_field=True,exact_restricted_original_profile_inside_unit_six_and_T1over32=True,all213_source_target_ranges=True,
        all641_original_coordinates=True,full_source_complete_mean_and_inverse=True,all_true_far_and_E_Lambda_retained=True,
        exact_quadratic_centre_supports_only=True,full_new_quadratic_not_deleted=True,complete_Hessian_domains=True,
        all_actual_finite_positive_outward_steps=True),
      input_identities=ids,source_sha256=sha(__file__),domain=modal['domain'],parent_full_domain=modal['parent_full_domain'],steps=a.steps,checkpoints=hist,full641_checkpoints=vectors,last_source_rows=source_final,
      same_original_metric_weights=old['same_original_metric_weights'],point_physical_epsilon_prime=old['point_physical_epsilon_prime'],head_strip=old['head_strip'],head_bands=old['head_bands'],
      constants=dict(Q='23/18',DQ='23/9',complete_T_Hessian='270 R',S='257/256',Theta='16705/16384'),
      low_raw_source_kernel='S times original base field Green; far usesS^2 original base/Z; actual E Lambda is added only in consistency',
      finite_substitution='Same existing field, intersect old finite caps with complete source/Green images and original low/far affine images',
      new_fixedpoint_claimed=False,outer_cut_or_closed_surface_claimed=False,elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
    if out.stat().st_size>=5_000_000:raise ArithmeticError('Split complete actual bootstrap artifact')
    print(json.dumps(dict(all_gates=True,path=str(out),sha256=sha(out),bytes=out.stat().st_size,elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
