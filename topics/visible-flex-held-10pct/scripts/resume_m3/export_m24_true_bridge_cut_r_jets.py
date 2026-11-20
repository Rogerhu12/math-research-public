#!/usr/bin/env python3
"""True C2 M24 bridge cut trace in R=ahat(s), for future common-node use.

The map is the current lambda .002 mean1168 graph. The target radius ahat
has already been unified with the true tail; the actual map radius a_star
and its nonzero endpoint differences are retained. Intervals enclose the
specified computable-real trace; their midpoints do not define a new trace.
No tail field is attached and no nonlinear solve is performed.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import mpmath as mp
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fq(x):return Q.from_float(float(x))
def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod)
    return mod
def derivative(p):return [(i+1)*p[i+1] for i in range(len(p)-1)]
def value(p,x):
    v=Q(0)
    for a in p[::-1]:v=v*x+a
    return v


def exact_endpoint_jets(physical,q):
    """The shared-Hermite convention selects the last left endpoint jet."""
    z=np.load(physical);x=z['x'];c=z['c']
    if c.shape[0]!=6 or c.shape[2]!=73:raise ValueError('Expected the frozen M24 quintic')
    h=fq(x[-1])-fq(x[-2]);rows=[[],[],[]]
    for j in range(c.shape[2]):
        p=[fq(c[5-k,-1,j]) for k in range(6)]
        for order in range(3):
            rows[order].append(q*value(p,h));p=derivative(p)
    return fq(x[-1]),rows


def interval_array(b,rows):
    z=[b.I.rational(q) for q in rows]
    return b.I(np.asarray([t.x[0] for t in z]),np.asarray([t.x[1] for t in z]))


def stored_interval(b,row):
    lo=b.I.rational(Q(row['lower_exact'])).x[0]
    hi=b.I.rational(Q(row['upper_exact'])).x[1]
    return b.I(lo,hi)


def mean_at_exact_cut(b,Y,a,ap,app,psi):
    """Full original mean1168 and its s derivative, with e=e'=e''=0."""
    M=24;N=len(psi);frequencies=np.arange(1,M+1)*3
    mp.iv.dps=80
    coslo=np.empty((M,N));coshi=np.empty((M,N));sinlo=np.empty((M,N));sinhi=np.empty((M,N))
    for j,m in enumerate(frequencies):
        for k,p in enumerate(psi):
            x=mp.iv.mpf(float(p))*int(m)
            c=mp.iv.cos(x);s=mp.iv.sin(x)
            coslo[j,k]=b.K.dn(float(c.a));coshi[j,k]=b.K.up(float(c.b))
            sinlo[j,k]=b.K.dn(float(s.a));sinhi[j,k]=b.K.up(float(s.b))
    co,sn=b.I(coslo,coshi),b.I(sinlo,sinhi)
    y=b.D(interval_array(b,Y[0]),interval_array(b,Y[1]))
    aa=b.D(a,ap);aa_s=b.D(ap,app);fr=b.I(frequencies[:,None])
    r=y.item(slice(1,M+1)).expand();t=y.item(slice(M+1,2*M+1)).expand();z=y.item(slice(2*M+1,None)).expand()
    R=y.item(0)+(r*co).sum();Rp=-(r*(fr*sn)).sum();Rpp=-(r*(fr.sq()*co)).sum()
    T=(t*sn).sum();Tp=(t*(fr*co)).sum();Tpp=-(t*(fr.sq()*sn)).sum()
    Zp=-(z*(fr*sn)).sum();Zpp=-(z*(fr.sq()*co)).sum()
    U=[(Rp-T)/aa,1+(Tp+R)/aa,Zp/aa]
    V=[-1+(Rpp-2*Tp-R)/aa,(Tpp+2*Rp-T)/aa,Zpp/aa]
    un=b.norm(U);kap_a=b.norm(b.cross(U,V))/(un*un*un)
    tangent=[x/un for x in U];proj=b.dot(tangent,V)
    nn=[x-proj*t for x,t in zip(V,tangent)];nv=b.norm(nn)
    normal=[x/nv for x in nn];binormal=b.cross(tangent,normal)
    alpha=-aa_s/kap_a;root=1-alpha.sq()
    if np.any(root.v.x[0]<=0):raise ArithmeticError('The actual mean-node Frenet root is not proved positive')
    beta=root.sqrt()
    # The original convection term and its s derivative both vanish at cut.
    mean=(alpha*normal[2]+beta*binormal[2]).sum()/N
    return mean,float(np.min(root.v.x[0]))


def exact_fourier_field_jets(Y):
    """Cartesian horizontal complex and vertical cosine coefficients of qY."""
    M=24;planar=[];height=[]
    modes=sorted([1]+[1+sign*3*j for j in range(1,M+1) for sign in (-1,1)])
    for row in Y:
        c={1:row[0]}
        for j in range(1,M+1):
            c[1+3*j]=(row[j]+row[M+j])/2
            c[1-3*j]=(row[j]-row[M+j])/2
        planar.append([c[m] for m in modes]);height.append([Q(0)]+row[2*M+1:])
    return modes,list(range(0,73,3)),planar,height


def assemble_R_trace(b,Y,a_jets,mean,Zc,E,w,wR):
    """Return coefficient intervals; exact recipes are documented in JSON."""
    pm,hm,pq,hq=exact_fourier_field_jets(Y)
    pp=[interval_array(b,row) for row in pq];hh=[interval_array(b,row) for row in hq]
    indicator_p=np.asarray([int(m==1) for m in pm]);indicator_h=np.asarray([int(m==0) for m in hm])
    for j,A in enumerate(a_jets):pp[j]=pp[j]+b.I(indicator_p)*A
    for j,Z in enumerate((Zc,mean.v,mean.d)):hh[j]=hh[j]+b.I(indicator_h)*Z
    sqrtE=b.I.rational(E).sqrt();c2=-b.I.rational(w*wR)/sqrtE
    pR=[pp[0],-sqrtE*pp[1],b.I.rational(E)*pp[2]+c2*pp[1]]
    hR=[hh[0],-sqrtE*hh[1],b.I.rational(E)*hh[2]+c2*hh[1]]
    return pm,hm,pR,hR,pq,hq


def scalar_report(x):
    lo=float(np.asarray(x.x[0]));hi=float(np.asarray(x.x[1]))
    return {'lower':lo,'upper':hi,'lower_exact':str(fq(lo)),'upper_exact':str(fq(hi))}
def tensor(values):return np.stack([np.stack(v.x,axis=0) for v in values],axis=0)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('source-run','physical','reference-seam','bridge-jet-certificate','height-contract',
              'mean-cache','mean-kernel','interval-kernel','out-npz','out'):
        ap.add_argument('--'+k,type=Path,required=True)
    a=ap.parse_args();started=time.monotonic()
    run=json.loads(a.source_run.read_text());ref=json.loads(a.reference_seam.read_text())
    bridge=json.loads(a.bridge_jet_certificate.read_text());height=json.loads(a.height_contract.read_text())
    runsha=sha(a.source_run);physha=sha(a.physical)
    assert runsha=='c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a'
    assert physha=='f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d'
    assert ref['source_run_sha256']==bridge['run_sha256']==height['run_sha256']==runsha
    assert ref['physical_sha256']==height['physical_sha256']==physha
    assert ref['status']=='bridge_true_tail_reference_seam_certified'
    assert ref['old_R60_map_and_mean_unchanged'] and ref['target_radius_common_two_jet_exact']
    assert ref['bridge_jet_certificate_sha256']==sha(a.bridge_jet_certificate)
    assert run['modes']==24 and run['prefix_audit']['samples_psi']==height['mean_nodes']==1168
    q=fq(run['gauge_q']);se,Y=exact_endpoint_jets(a.physical,q)
    sb=fq(float(bridge['source_endpoints']['prefix_end']))
    assert se==fq(float(bridge['source_endpoints']['end'])) and se>sb
    assert se-sb==Q(bridge['source_endpoints']['exact_span'])
    cutoff=[Q(1),Q(0),Q(0),-Q(10),Q(15),-Q(6)];cutoffjet=[]
    for _ in range(3):cutoffjet.append(value(cutoff,Q(1)));cutoff=derivative(cutoff)
    assert cutoffjet==[0,0,0]
    lift_right=fq(.9)*sb
    assert se>sb>lift_right
    # e=warp*h*cutoff has zero two-jet; the core lift is identically zero
    # on an open neighborhood of se because its right window is <sb.
    b=load_module('_bridge_cut_fixed_mean',a.mean_kernel)
    b.K=load_module('_bridge_cut_interval_kernel',a.interval_kernel)
    assert sha(a.mean_kernel)=='ab08dc1dc7f24f6e92e3d64fcc530767cb66f5ae5a2940f953460a3274b6a1a5'
    assert sha(a.interval_kernel)=='6234c458d303dfd2e47dcf1e1a6ee54a3d466118a8aea4d76f66013154c034e7'
    Rc,w,wR=map(Q,(ref['cut_R_exact'],ref['cut_w_exact'],ref['cut_wR_exact']))
    assert wR==-7*w/Rc
    E=1+w*w;gap=Q(ref['reused_radius_gap_triangle_exact'])
    # A is the unique true primitive; this enclosure does not choose A=Rc.
    A=b.I(b.I.rational(Rc-gap).x[0],b.I.rational(Rc+gap).x[1])
    Ap=stored_interval(b,ref['bridge_actual_a_prime']);App=stored_interval(b,ref['bridge_actual_a_second'])
    Bp=-1/b.I.rational(E).sqrt();Bpp=b.I.rational(-w*wR/E**2)
    with np.load(a.mean_cache) as nc:psi=np.asarray(nc['psi'],float)
    assert len(psi)==1168 and np.array_equal(psi,2*np.pi*np.arange(1168)/1168)
    psisha=hashlib.sha256(psi.tobytes()).hexdigest()
    assert psisha=='f4834f978de38046e374b020d2a928d293fc405f794159e40e2271f4ee9bd9cf'
    mean,root=mean_at_exact_cut(b,Y,A,Ap,App,psi)
    Zc=stored_interval(b,height['cut_primitive_Z'])
    pm,hm,pR,hR,pq,hq=assemble_R_trace(b,Y,(A,Ap,App),mean,Zc,E,w,wR)
    for v in pR+hR:
        if not v.finite():raise ArithmeticError('Nonfinite trace enclosure')
    # Bounds on perturbation coefficients, with the exact background cut
    # subtracted only for this diagnostic; no actual trace term is erased.
    ip=b.I(np.asarray([int(m==1) for m in pm]))
    pdef=[pR[0]-b.I.rational(Rc)*ip,pR[1]-ip,pR[2]]
    def l1_upper(v):
        upper=np.maximum(np.abs(v.x[0]),np.abs(v.x[1]));return float(b.I(upper).sum().x[1])
    horizontal=[l1_upper(v) for v in pdef]
    height_nonzero=[l1_upper(v.item(slice(1,None))) for v in hR]
    targetjet=[b.I.rational(Rc),Bp,Bpp]
    bindings={'run_sha256':runsha,'physical_sha256':physha,'mean_nodes':1168,'psi_sha256':psisha,
        'source_sha256':sha(__file__),'reference_seam_sha256':sha(a.reference_seam),
        'height_contract_sha256':sha(a.height_contract),'A_scope':'unique true actual bridge primitive; no midpoint or forced cut radius',
        'Z_scope':'same mean1168 true primitive symbol Z_cut; interval is enclosure only'}
    exact={'qY_s_jets':[[str(x) for x in row] for row in Y],
        'qY_planar_s_jets':[[str(x) for x in row] for row in pq],
        'qY_height_s_jets':[[str(x) for x in row] for row in hq]}
    np.savez_compressed(a.out_npz,planar_modes=np.asarray(pm,int),height_modes=np.asarray(hm,int),
        planar_R_jets=tensor(pR),height_R_jets=tensor(hR),actual_a_jets=tensor([A,Ap,App]),target_a_jets=tensor(targetjet),
        mean_0_1=tensor([mean.v,mean.d]),qY_s_jets=tensor([interval_array(b,row) for row in Y]),
        exact_endpoint_data_json=np.asarray(json.dumps(exact)),bindings_json=np.asarray(json.dumps(bindings)))
    report={'status':'actual_linear_bridge_true_cut_R_trace_enclosed','source_sha256':sha(__file__),
        'run_sha256':runsha,'physical_sha256':physha,
        'inputs_sha256':{k:sha(getattr(a,k)) for k in ('reference_seam','bridge_jet_certificate','height_contract','mean_cache','mean_kernel','interval_kernel')},
        'npz_sha256':sha(a.out_npz),'mean_nodes':1168,'psi_sha256':psisha,'q_exact':str(q),
        's_cut_exact':str(se),'R_cut_exact':str(Rc),'target_w_exact':str(w),'target_wR_exact':str(wR),
        'e_cut_value_first_second_exact':list(map(str,cutoffjet)),
        'lift_cut_value_first_second_exact':['0','0','0'],'lift_zero_open_neighborhood':True,
        'shared_Y_endpoint_rule':'Last left exact binary polynomial value/first/second, exactly the common-Hermite terminal definition',
        'target_radius_cut_jets':[scalar_report(x) for x in targetjet],
        'actual_map_radius_cut_jets':[scalar_report(x) for x in (A,Ap,App)],
        'actual_minus_target_radius_jets':[scalar_report(x-y) for x,y in zip((A,Ap,App),targetjet)],
        'M_cut':scalar_report(mean.v),'M_prime_cut':scalar_report(mean.d),'frenet_root_lower':root,
        'Z_cut_symbol_interval':height['cut_primitive_Z'],
        'planar_modes':pm,'height_modes':hm,'horizontal_perturbation_R_jet_l1_upper':horizontal,
        'height_nonzero_mode_R_jet_l1_upper':height_nonzero,
        'actual_height_mean_R_jet_intervals':[scalar_report(v.item(0)) for v in hR],
        'exact_trace_recipes':{
            'planar_s_jets':'P_j = qY_planar_s_j + delta_(m=1) * (A,A_s,A_ss)_j',
            'height_s_jets':'H_j = qY_height_s_j + delta_(m=0) * (Z_cut,M,M_s)_j',
            'R_first':'F_R = F_s / ahat_s = -sqrt(E) F_s',
            'R_second':'F_RR = (F_ss - F_R ahat_ss) / ahat_s^2 = E F_ss - w*w_R/sqrt(E) F_s',
            'A':'1 minus the exact integral of sin(phi_source) from the bridge entry; last phase analytically extended to s_cut',
            'M':'The exact equal-weight sum at the preserved 1168 literal psi nodes of the actual a_star/qY Frenet velocity; original convection and its derivative vanish at this cut',
            'Z_cut':'The same exact prefix+bridge mean1168 radial primitive, not a selected point of its interval',
            'common_node_use':'Both adjoining pieces must reference these same computable-real expressions. Independent interval-midpoint or rounded choices do not give exact C2 identity'},
        'target_metric_changed_here':False,'actual_bridge_map_modified':False,
        'tail_field_attached':False,'warm025_trace_matched':False,'future_full_H_trace_matched':False,
        'background_integrals_recomputed':False,'nonlinear_solves':0,'core_evaluations':0,
        'seconds':time.monotonic()-started}
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','M_cut','M_prime_cut','frenet_root_lower',
        'horizontal_perturbation_R_jet_l1_upper','height_nonzero_mode_R_jet_l1_upper','npz_sha256','seconds')}),flush=True)


if __name__=='__main__':main()
