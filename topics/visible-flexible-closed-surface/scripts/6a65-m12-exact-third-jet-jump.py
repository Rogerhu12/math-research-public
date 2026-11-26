#!/usr/bin/env python3
"""One exact third-jet witness in the original normalized M12 source.

Only the last known original blob is required. This certifies a regularity
constraint on an exactly isometric C3 correction, not a uniform metric-error
lower bound and not a failure of C2 convergence under refinement.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'
LAST_SHA='89fe80d3453aa25978c343f7d58d51a31dd1d3fe37e6fffcdd48cfc31b551249'
LAST_GIT='1a9cce86c3ad6e88bc07dedb465a08066a62a5ab'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def q(x):return Q.from_float(float(x))
def load(name,p):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--blob-file',type=Path)
    ap.add_argument('--source-transport',choices=('git-blob-api','raw-known-commit'),default='raw-known-commit')
    args=ap.parse_args();start=time.monotonic()
    if args.out.exists():raise FileExistsError('Fresh exact witness report required')
    manifest=args.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    if sha(manifest)!=MANIFEST_SHA:raise ValueError('Changed original source manifest')
    m=json.loads(manifest.read_text());info=m['files'][-1]
    if info['sha256']!=LAST_SHA or info['rows']!=406 or info['columns']!=567:raise ValueError('Different original last span block')
    producer=load('third_jump_original_blob_table',args.scripts/'6a65-m12-stream-tail-exact-endpoint.py')
    reader=load('third_jump_checked_payload',args.scripts/'6a65-m12-stream-tail-query-and-source-bounds-recovered.py')
    helper=load('third_jump_original_quartic',args.scripts/'6a65-m12-tail-polynomial-continuous-bounds-recovered.py')
    if args.blob_file:raw=args.blob_file.read_bytes()
    else:
        headers={'User-Agent':'M12-exact-third-jet-witness','Accept':'application/vnd.github+json'}
        if os.environ.get('M12_RECOVERY_TOKEN'):headers['Authorization']='Bearer '+os.environ['M12_RECOVERY_TOKEN']
        raw=reader.recover_payload(producer,LAST_GIT,info,args.source_transport,headers)
    if len(raw)!=info['bytes'] or hashlib.sha256(raw).hexdigest()!=LAST_SHA:raise ValueError('Original payload identity mismatch')
    if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=LAST_GIT:raise ValueError('Original Git object mismatch')
    a=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(info['rows'],info['columns'])
    C=m['format']['coefficientCount'];P=len(m['format']['planarModes'])
    if C!=141 or P!=128:raise ValueError('Incomplete original angular source')
    v=a[:,2:2+4*C].reshape(len(a),4,C)
    rg=m['radialGeometry'];beta=Q(int(rg['normalization']['numerator']),int(rg['normalization']['denominator']))
    lengths=[beta*q(a[i+1,-1]) for i in (len(a)-3,len(a)-2)]
    if min(lengths)<=0:raise ArithmeticError('Original source length is nonpositive')
    jumps=[]
    for j in range(C):
        endjets=[]
        for i,L in zip((len(a)-3,len(a)-2),lengths):
            _,b,_=helper.span_controls(Q(0),q(v[i,1,j]),q(v[i+1,1,j]),q(v[i,2,j]),q(v[i+1,2,j]),q(v[i+1,3,j]),L)
            endjets.append((12*(b[2]-2*b[1]+b[0])/L**2,12*(b[4]-2*b[3]+b[2])/L**2))
        jumps.append(endjets[1][0]-endjets[0][1])
    A=[sum(jumps[:P],Q(0)),Q(0),-sum(jumps[P:],Q(0))]
    p=m['parameters'];eta=q(p['delta0'])*q(p['etaRatioAtN0']);cut=Q(rg['outerAnchor']);r=cut-lengths[-1]
    # Reviewed original alpha>90, w<=16/15; on x in [0,1/2] of j8:
    # chi>=1/2, r_old>=cuff, sqrt(12)<4, weight=1.
    width_lower=90*q(p['rCuff'])*eta/(16*Q(481,225))
    if not lengths[-1]<width_lower:raise ArithmeticError('Cannot place the node inside analytic n0/j8')
    if p['warpWeightLevels'][0][-1]!=1 or p['capMode']!='cut-preserving':raise ValueError('Different last-segment analytic definition')
    if not A[0]<-Q(168,100) or not A[2]<-Q(77,10000):raise ArithmeticError('Declared strict nonzero witness did not hold')
    # An explicit separate C2 patch removes this complete Fourier jump.
    # Q(r,u)=-A(u)*delta^3*B((r-r0)/delta), delta=L_right/3.
    # B(y)=y^3/6 on [0,1], and y^3*(1-S3(y-1))/6 on [1,2],
    # with S3(t)=35t^4-84t^5+70t^6-20t^7. B is zero outside [0,2].
    # B'''(0+)=1; its cutoff is C3 at y=1 and y=2.
    first=[Q(0),Q(0),Q(0),Q(1,6)]
    cubic=[Q(1,6),Q(1,2),Q(1,2),Q(1,6)]
    cutoff=[Q(1),Q(0),Q(0),Q(0),Q(-35),Q(84),Q(-70),Q(20)]
    second=[Q(0)]*11
    for i,x in enumerate(cubic):
        for j,y in enumerate(cutoff):second[i+j]+=x*y
    bd=[]
    for d in range(3):
        polys=[]
        for src in (first,second):
            f=src[:]
            for _ in range(d):f=[i*f[i] for i in range(1,len(f))]
            polys.append(max(map(abs,helper.bernstein(f))))
        bd.append(max(polys))
    modes=m['format']['planarModes']+m['format']['heightModes']
    Aj=[sum((abs(v)*abs(k)**j for v,k in zip(jumps,modes)),Q(0)) for j in range(3)]
    delta=lengths[1]/3
    jets={(d,j):delta**(3-d)*bd[d]*Aj[j] for d in range(3) for j in range(3-d)}
    physical={'Q':jets[0,0],'Qs':jets[1,0],'Qu':jets[0,1],
              'Qss':jets[2,0]+6*jets[1,0],'Qsu':jets[1,1],'Quu':jets[0,2]}
    ppatch=physical['Qs']+physical['Qu']/r;old=Q(257212,10**13)
    patch_metric=old+2*(1+old)*ppatch+ppatch*ppatch
    index=sum(i['rows']-1 for i in m['files'])-1
    out={'schema':'6a65-original-M12-exact-third-jet-jump-v1','script_sha256':sha(__file__),
         'manifest_sha256':MANIFEST_SHA,'original_blob_git_sha':LAST_GIT,'original_blob_sha256':LAST_SHA,
         'original_blob_bytes':len(raw),'original_quartic_helper_sha256':sha(helper.__file__),
         'source_node_index':index,'source_span_left':index-1,'source_span_right':index,
         'normalization_exact':str(beta),'radius_exact':str(r),'radius_display':float(r),
         'left_span_length_exact':str(lengths[0]),'right_span_length_exact':str(lengths[1]),
         'analytic_j8_width_lower_exact':str(width_lower),'strictly_inside_n0_j8':True,
         'Cartesian_third_jet_jump_at_material_angle_zero_exact':list(map(str,A)),
         'Cartesian_third_jet_jump_display':list(map(float,A)),
         'strict_jump_x_upper':'-42/25','strict_jump_z_upper':'-77/10000',
         'complete_coefficient_jump_stream_sha256':hashlib.sha256(('\n'.join(map(str,jumps))+'\n').encode()).hexdigest(),
         'exact_uses_derived_position_columns':False,'exact_uses_displayed_radius_differences':False,
         'inherited_analytic_hypotheses':'Reviewed original alpha>90 and w<=16/15; original n0/j8 raw override, positive radial Jacobian; original accurate source C2 construction.',
         'conclusion_scope':'No ambient-reflection-preserving C3 Cartesian correction can give an exact isometric immersion at this circle; source and correction must obey Y(r,-u)=diag(1,-1,1)Y(r,u). Current real D3 simple quintic knot fields are included.',
         'separate_constructive_C2_patch':{'applied_to_any_actual_CI_field':False,
              'complete_Fourier_third_jump_cancelled_exactly':True,'new_third_jumps_at_cutoff_endpoints':False,
              'support_left_exact':str(r),'support_right_exact':str(r+2*delta),'delta_exact':str(delta),
              'cutoff_derivative_Bernstein_upper_exact':list(map(str,bd)),
              'full_jump_angular_l1_jets_exact':list(map(str,Aj)),
              'physical_two_jet_upper':{k:{'upper_exact':str(v),'display':float(v)} for k,v in physical.items()},
              'target_differential_upper_exact':str(ppatch),
              'original_baseline_plus_patch_metric_triangle_upper':float(patch_metric),
              'original_baseline_plus_patch_metric_triangle_upper_exact':str(patch_metric),
              'fixed_original_g_unchanged':True,'all_other_source_jumps_removed':False,'exact_isometry_proved':False},
         'uniform_metric_error_lower_bound_proved':False,'C2_refinement_obstructed':False,
         'exact_isometry_excluded_for_all_C2_corrections':False,'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,indent=2,allow_nan=False))

if __name__=='__main__':main()
