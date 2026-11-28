#!/usr/bin/env python3
"""Exact all-mode C-infinity regularization of original finite M12 seams.

The fixed target metric is never changed.  Only the original piecewise
quintic perturbation is regularized inside disjoint physical-r windows.
Every original nodal position/tangent/second derivative is preserved, and
all derivatives are unchanged at each window endpoint.  The new source is
NOT asserted to be isometric or to satisfy the complete topic conditions.

The output contains scalar exact-Fraction budgets and a reproducible hash.
Optional numerical correction coefficients are scratch-only regenerable
data; they must not be committed to the repository.
"""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.util, json, math, time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def q(x): return Q.from_float(float(x))
def packet(x): return {'exact':str(x),'display':float(x)}

def higher_end_jets(f0,f1,s0,s1,mid,L):
    """Original integrated-quartic position's derivatives 3,4,5."""
    v0,v1=L*s0,L*s1
    bubble=16*mid-8*(f0+f1)-2*(v0-v1)
    c2=-3*f0+3*f1-2*v0-v1+bubble
    c3=2*f0-2*f1+v0+v1-2*bubble
    c4=bubble
    L2=L*L;L3=L2*L;L4=L3*L
    left=(2*c2/L2,6*c3/L3,24*c4/L4)
    right=((2*c2+6*c3+12*c4)/L2,(6*c3+24*c4)/L3,24*c4/L4)
    return left,right

def transition(t):
    """C-infinity flat switch and first two derivatives, float evaluation.

    Bounds |S'|<=8, |S''|<=120 are proved independently in the note.
    Never used as a rigorous arithmetic enclosure.
    """
    t=np.asarray(t,dtype=np.longdouble)
    s=np.zeros_like(t);s1=np.zeros_like(t);s2=np.zeros_like(t)
    s[t>=1]=1
    active=(t>0)&(t<1)
    x=t[active]
    z=1/(1-x)-1/x
    positive=z>=0
    val=np.empty_like(z)
    val[positive]=1/(1+np.exp(-z[positive]))
    ez=np.exp(z[~positive]);val[~positive]=ez/(1+ez)
    z1=1/x**2+1/(1-x)**2
    z2=-2/x**3+2/(1-x)**3
    s[active]=val;s1[active]=val*(1-val)*z1
    s2[active]=val*(1-val)*((1-2*val)*z1*z1+z2)
    return s,s1,s2

def correction_coefficients(radius,center,delta,jumps):
    """Return Q,Q_r,Q_rr coefficient rows from a 3 x C jump matrix.

    A radial material consumer converts these to s and theta using the
    same original r_s,r_ss,rho,rho' as WholePosition.tail_point.
    """
    r=np.asarray(radius,dtype=np.longdouble);x=r-np.longdouble(center)
    d=np.longdouble(delta);J=np.asarray(jumps,dtype=np.longdouble)
    t=(x+d)/(2*d);s,s1,s2=transition(t)
    # Q = S Delta on the left, (S-1) Delta on the right.
    weight=s-(x>=0);w1=s1/(2*d);w2=s2/(4*d*d)
    D=x[...,None]**3*J[0]/6+x[...,None]**4*J[1]/24+x[...,None]**5*J[2]/120
    D1=x[...,None]**2*J[0]/2+x[...,None]**3*J[1]/6+x[...,None]**4*J[2]/24
    D2=x[...,None]*J[0]+x[...,None]**2*J[1]/2+x[...,None]**3*J[2]/6
    ans=np.stack((weight[...,None]*D,
                  w1[...,None]*D+weight[...,None]*D1,
                  w2[...,None]*D+2*w1[...,None]*D1+weight[...,None]*D2),axis=-2)
    ans[(x<=-d)|(x>=d)]=0
    return ans

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--divisor',type=int,default=64)
    ap.add_argument('--last-blocks',type=int,default=0,
                    help='0 covers every finite original span; positive is explicitly only a suffix diagnostic')
    ap.add_argument('--cache-dir',type=Path)
    ap.add_argument('--scratch-npz',type=Path)
    args=ap.parse_args()
    if args.divisor<4:raise ValueError('Disjoint windows require divisor >=4')
    if args.out.exists():raise FileExistsError(args.out)
    if args.scratch_npz and args.scratch_npz.exists():raise FileExistsError(args.scratch_npz)
    began=time.monotonic();mp=args.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    if sha(mp)!=MANIFEST_SHA:raise ValueError('Original manifest changed')
    m=json.loads(mp.read_text());fmt=m['format'];C=fmt['coefficientCount']
    modes=fmt['planarModes']+fmt['heightModes']
    if C!=141 or len(modes)!=C:raise ValueError('Incomplete original Fourier source')
    p=load('smooth_original_blob_table',args.scripts/'6a65-m12-stream-tail-exact-endpoint.py')
    rd=load('smooth_original_recovery',args.scripts/'6a65-m12-stream-tail-query-and-source-bounds-recovered.py')
    rg=m['radialGeometry'];beta=Q(int(rg['normalization']['numerator']),int(rg['normalization']['denominator']))
    full_files=m['files'];first=max(0,len(full_files)-args.last_blocks) if args.last_blocks else 0
    selected=full_files[first:]
    total_finite_spans=sum(z['rows']-1 for z in full_files)
    # A suffix is accumulated from the known exact outer anchor backwards.
    # All center locations are filled after all its exact lengths are known.
    previous_row=None;previous_end=None;previous_L=None
    max_native={(a,b):Q(0) for a in range(3) for b in range(3-a)}
    maxima={};digest=hashlib.sha256();recovered=[];windows=[];span_lengths=[]
    span_count=0;node_count=0
    for bi,info in enumerate(selected,first):
        name=Path(info['path']).name;key=name.split('-raw')[1].split('.f64')[0].replace('-part','-')
        blob=p.BLOBS[key]
        cache=None if args.cache_dir is None else args.cache_dir/name
        if cache is not None and cache.exists():raw=cache.read_bytes()
        else:
            raw=rd.recover_payload(p,blob,info,'raw-known-commit',{})
            if cache is not None:
                cache.parent.mkdir(parents=True,exist_ok=True);cache.write_bytes(raw)
        if len(raw)!=info['bytes'] or hashlib.sha256(raw).hexdigest()!=info['sha256']:raise ValueError('Wrong payload')
        if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=blob:raise ValueError('Wrong Git object')
        raw_array=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(info['rows'],info['columns'])
        if previous_row is not None and not np.array_equal(raw_array[0],previous_row):raise ValueError('Broken shared original source node')
        v=raw_array[:,2:2+4*C].reshape(len(raw_array),4,C)
        for i in range(len(raw_array)-1):
            L=beta*q(raw_array[i+1,-1]);span_lengths.append(L)
            if L<=0:raise ValueError('Nonpositive original source span')
            left=[];right=[]
            for j in range(C):
                a,b=higher_end_jets(q(v[i,1,j]),q(v[i+1,1,j]),q(v[i,2,j]),q(v[i+1,2,j]),q(v[i+1,3,j]),L)
                left.append(a);right.append(b)
            if previous_end is not None:
                jumps=[[left[j][k]-previous_end[j][k] for j in range(C)] for k in range(3)]
                delta=min(previous_L,L)/args.divisor
                A=[[sum((abs(jumps[k][j])*abs(modes[j])**b for j in range(C)),Q(0)) for b in range(3)] for k in range(3)]
                for b in range(3):
                    bounds=[delta**3*A[0][b]/6+delta**4*A[1][b]/24+delta**5*A[2][b]/120,
                            Q(7,6)*delta**2*A[0][b]+delta**3*A[1][b]/3+Q(3,40)*delta**4*A[2][b],
                            10*delta*A[0][b]+Q(37,12)*delta**2*A[1][b]+Q(3,4)*delta**3*A[2][b]]
                    for a in range(3-b):
                        if bounds[a]>max_native[a,b]:
                            max_native[a,b]=bounds[a];maxima[str((a,b))]=span_count
                line=[str(span_count),str(delta)]+[str(x) for row in jumps for x in row]
                digest.update(('\t'.join(line)+'\n').encode())
                if args.scratch_npz:
                    windows.append((span_count,delta,np.array([[np.longdouble(x.numerator)/np.longdouble(x.denominator) for x in row] for row in jumps],dtype=np.longdouble)))
                node_count+=1
            previous_end=right;previous_L=L;span_count+=1
        previous_row=raw_array[-1].copy();recovered.append({'block':bi,'sha256':info['sha256'],'git_blob':blob})
        print(json.dumps({'block':bi,'finite_spans_processed':span_count,'internal_seams_smoothed':node_count,'seconds':time.monotonic()-began}),flush=True)
    outer=Q(rg['outerAnchor']);inner=outer-sum(span_lengths,Q(0))
    if first==0 and inner!=Q(rg['innerAnchor']):raise ArithmeticError('Complete source radial normalization mismatch')
    physical={'Q':max_native[0,0],'Qs':max_native[1,0],'Qu':max_native[0,1],
              'Qss':max_native[2,0]+6*max_native[1,0],'Qsu':max_native[1,1],'Quu':max_native[0,2]}
    ptarget=physical['Qs']+physical['Qu']/inner
    old=Q(257212,10**13);metric=old+2*(1+old)*ptarget+ptarget**2
    npz_receipt=None
    if args.scratch_npz:
        centers=[];r=inner
        for length in span_lengths[:-1]:r+=length;centers.append(np.longdouble(r.numerator)/np.longdouble(r.denominator))
        np.savez_compressed(args.scratch_npz,centers=np.asarray(centers,dtype=np.longdouble),
             delta=np.asarray([np.longdouble(z[1].numerator)/np.longdouble(z[1].denominator) for z in windows]),
             jumps=np.asarray([z[2] for z in windows]),planar_modes=fmt['planarModes'],height_modes=fmt['heightModes'])
        npz_receipt={'sha256':sha(args.scratch_npz),'bytes':args.scratch_npz.stat().st_size,
                     'scope':'Numerical evaluator coefficients; not an interval enclosure and not a repository deliverable'}
    report={'schema':'m12-exact-C-infinity-finite-source-seam-regularization-v1',
      'script_sha256':sha(__file__),'manifest_sha256':MANIFEST_SHA,'divisor':args.divisor,
      'complete_original_finite_tail':first==0,'all_original_finite_spans':total_finite_spans,
      'selected_spans':span_count,'internal_seams_smoothed':node_count,
      'selected_inner_exact':str(inner),'outer_exact':str(outer),'original_blocks':recovered,
      'every_original_node_zero_two_jets_of_correction':True,
      'all_derivatives_unchanged_at_window_endpoints':True,
      'disjoint_windows':True,'all_internal_polynomial_seams_C_infinity':True,
      'original_finite_tail_outer_endpoint_third_jets_unchanged':True,
      'deep_collar_and_prefix_seams_smoothed':False,'same_original_g':True,
      'complete_Fourier_modes':C,'exact_jump_and_window_stream_sha256':digest.hexdigest(),
      'native_r_u_six_jet_upper':{str(k):packet(v) for k,v in max_native.items()},
      'physical_s_u_six_jet_upper':{k:packet(v) for k,v in physical.items()},
      'maxima_at_selected_source_node':maxima,
      'physical_target_first_jet_bound':packet(ptarget),
      'original_R21_baseline_plus_Q_metric_triangle_upper':packet(metric),
      'hypotheses':'Inherited same original r_s magnitude <=1 and r_ss magnitude <=6; target ds^2+r^2 du^2; finite source uses original normalized physical r increments.',
      'exact_solution_proved':False,'any_new_nonlinear_solver_acceptance':False,
      'new_candidate_full_reach_and_noncongruence_paid':False,
      'numerical_scratch_npz':npz_receipt,'seconds':time.monotonic()-began}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'report':str(args.out),'seconds':report['seconds'],'physical_s_u_six_jet_display':{k:float(v) for k,v in physical.items()},'metric_triangle_display':float(metric)}),flush=True)

if __name__=='__main__':main()
