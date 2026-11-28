#!/usr/bin/env python3
"""General first-order material frame, true R680 anchor and finite reconstruction."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import time
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import qr,svd
from r659_finite_tilt_latitude_system_20261128 import dot, emit, mean_free, primitive, rz_frame
from r669_true_finite_tilt_reach_continuation_20261128 import angular_derivative,trust_step
from r683_proper_phase_metric_transport_20261128 import ProperPhase,positive_part,shell,shell_ok


def cross(a,b): return np.cross(a,b)


def turn(frame,axis,f):
    P,T,N=frame; co=np.cos(f)[...,None]; si=np.sin(f)[...,None]
    if axis==0: return P,co*T+si*N,-si*T+co*N
    if axis==1: return co*P-si*N,T,si*P+co*N
    return co*P+si*T,-si*P+co*T,N


class Frame(ProperPhase):
    def __init__(self,spec,count):
        super().__init__(spec,count)
        self.blocks=[(i,j) for i in range(3) for j in range(int(i!=1),self.K+1)]
        self.body=len(self.blocks)*self.na; self.size=self.body+3*self.nc

    def center(self,x,r):
        cc=x[self.body+self.nc:].reshape(2,self.nc)
        I=(self.spl.antiderivative()(r)-self.spl.antiderivative()(self.b))[:,2:-2]@cc.T
        return self.cbase(np.ascontiguousarray(r,dtype=np.float64).tobytes())+np.stack((I[:,0],np.zeros(len(r)),I[:,1]),axis=-1)

    def at(self,r,azimuths,weights=None):
        g=super().at(r,azimuths,weights); phi=g['phi']; g['wave']=[]; g['wave_p']=[]
        for i,j in self.blocks:
            if i==1: w,wp=np.cos(j*phi),-j*np.sin(j*phi)
            else: w,wp=np.sin(j*phi),j*np.cos(j*phi)
            g['wave'].append(w);g['wave_p'].append(wp)
        return g

    def state(self,x,g,level,frozen=None):
        self.count['full_frame_states']+=1
        nr,np_=len(g['r']),len(g['phi']); dim=(nr,np_,3); r=g['r'][:,None]
        p=g['qx']*g['r']; dp=g['qxx']*g['r']+p/g['r']; cf=np.cos(g['phi']); sf=np.sin(g['phi'])
        z=-p[:,None]*(1.01+cf); zr=-dp[:,None]*(1.01+cf); zp=p[:,None]*sf
        base=1+z*z; rho=x[self.body:self.body+self.nc]; d=g['C'][0]@rho
        mug=.5*np.log1p((1.01**2+.5)*p*p)
        e=np.exp((1-level)*.5*np.log(base)+level*mug[:,None]+d[:,None]) if frozen is None else np.broadcast_to(frozen[:,None],base.shape)
        ep=e*(1-level)*z*zp/base if frozen is None else np.zeros_like(e)
        P=rz_frame(np.broadcast_to(g['er'],dim),g['q'][:,None]); T=rz_frame(np.broadcast_to(g['et'],dim),g['q'][:,None])
        N=rz_frame(np.broadcast_to(g['ez'],dim),g['q'][:,None])
        fr=(P,T,N); Omr=np.zeros(dim); Omr[...,1]=g['qx'][:,None]; Omrr=np.zeros(dim);Omrr[...,1]=g['qxx'][:,None]
        Omp=N.copy(); axes=[]; co=x[:self.body].reshape(len(self.blocks),self.na)
        ids=np.array([i for i,j in self.blocks]); waves=np.array(g['wave']); wphi=np.array(g['wave_p'])
        for axis in range(3):
            choose=ids==axis; g0,g1,g2=[M@co[choose].T for M in g['A']]
            f=g0@waves[choose]; fp=g0@wphi[choose]; fx=g1@waves[choose]; fxx=g2@waves[choose]
            V=fr[axis]; Vi=cross(Omr,V); Vp=cross(Omp,V); axes.append((V,Vi,Vp))
            Omrr=Omrr+fxx[...,None]*V+fx[...,None]*Vi
            Omr=Omr+fx[...,None]*V; Omp=Omp+fp[...,None]*V; fr=turn(fr,axis,f)
        # The last fixed rotation about the current T leaves it C² even at the actual C¹ slope joins.
        T=fr[1]; Tr=cross(Omr,T); Trr=cross(Omrr,T)+cross(Omr,Tr); Tp=cross(Omp,T)
        P,T,N=turn(fr,1,-np.arctan(z)); orad=Omr-zr[...,None]/base[...,None]*T
        op=Omp-zp[...,None]/base[...,None]*T
        Pr=cross(orad,P); Pp=cross(op,P)
        EP=e[...,None]*P; EPp=ep[...,None]*P+e[...,None]*Pp; G=EPp-T-r[...,None]*Tr
        cc=x[self.body+self.nc:].reshape(2,self.nc); b0=g['C'][0]@cc.T; b1=g['C'][1]@cc.T
        C0=np.stack((b0[:,0],np.zeros(nr),b0[:,1]),axis=1)+rz_frame(g['w'][:,None]*g['ez'],g['q'])
        C1=np.stack((b1[:,0],np.zeros(nr),b1[:,1]),axis=1)+rz_frame(g['dw'][:,None]*g['ez']+g['w'][:,None]*g['qx'][:,None]*np.array([1.,0,0]),g['q'])
        gap=C0-EP.mean(axis=1); closure=T.mean(axis=1)
        a=dot(Pr,N)/e; b=(dot(Pp,N)/r+dot(Tr,N)/e)/2; k=dot(Tp,N)/r
        return dict(P=P,T=T,N=N,Tr=Tr,Tp=Tp,Trr=Trr,Pr=Pr,Pp=Pp,e=e,EP=EP,EPp=EPp,G=G,axes=axes,
                    gap=gap,closure=closure,C0=C0,C1=C1,abc=(a,b,k),r=r,fixed_reference=frozen is not None,design_e=np.exp(mug+d) if frozen is None else frozen)


def cones(st,T0,ang):
    a,b,k=st['abc']; N=st['N']; vals=[]
    for s in (1,-1):
        vals.extend((1+s*T0*(a+k)/2,(1+s*T0*a)*(1+s*T0*k)-(T0*b)**2))
    vals.extend((N[...,2],math.sin(ang)*N[...,0]+math.cos(ang)*N[...,2])); return vals


def directional(sys,x,g,st,level,n):
    beta=np.linspace(-np.pi,np.pi,n,endpoint=False); dr=np.stack((np.cos(beta),np.sin(beta)),axis=1)
    signs=np.array([[1.],[-1.]])
    A=np.abs(np.angle(np.exp(1j*(beta+sys.ang)))); B=np.abs(beta); T0=.03; span=sys.b-sys.a
    def raw(S,C):
        m=np.maximum(0.,(A+B-S/T0)/2)
        if S<T0*np.max(abs(A-B)):
            raise FloatingPointError('No meeting of the two actual end tangent cones.')
        U=np.where(m>0,T0*(np.sin(A)+np.sin(B)-2*np.sin(m)),S-T0*(A-np.sin(A)+B-np.sin(B)))
        D0=np.array([sys.b-sys.a*math.cos(sys.ang),sys.a*math.sin(sys.ang)])
        return (dr@D0)[None,:]+signs*(dr@C)[None,:]-U[None,:],np.cos(m)
    C=sys.center(x,np.array([sys.a]))[0,[0,2]]; S=span*(g['weights']@st['design_e'])
    f,ds=raw(S,C); f0,_=raw(span*(g['weights']@np.sqrt(g['anchor_E'])),sys.cbase(np.array([sys.a]).tobytes())[0,[0,2]])
    z=(f-(1-level)*(np.maximum(f0,0.)+1e-12)+.0003*level)/span
    return z,ds,dr,signs,float(-f.max()),float(S)


def equations(sys,x,g,level,opt,guards,fixed=None):
    st=sys.state(x,g,level,fixed); wr=np.sqrt(g['weights']); nphi=len(g['phi']); wt=wr[:,None]/math.sqrt(nphi)
    G,gap,closure=st['G'],st['gap'],st['closure']; parts=[(wt[...,None]*G).ravel(),(wr[:,None]*gap[:,[0,2]]).ravel(),wr*closure[:,1]]
    st['primary_rows']=sum(len(p) for p in parts); coeff=[]
    for ref,val in zip(guards,cones(st,opt['T'],sys.ang)):
        y,yp=positive_part(ref-val,opt['smooth_width']); parts.append((wt*opt['guard_weight']*y).ravel()); coeff.append(-opt['guard_weight']*yp)
    st['chain']=coeff
    z,ds,dr,sg,margin,S=directional(sys,x,g,st,level,opt['work_betas'])
    y,yp=positive_part(z,opt['smooth_width']); norm=math.sqrt(z.size)
    st.update(lb=yp/norm,ds=ds,dir=dr,sg=sg,margin=margin,S=S); parts.append((y/norm).ravel())
    return np.concatenate(parts),st


def assemble(sys,g,st,opt,fixed):
    nr,nphi=len(g['r']),len(g['phi']); r=st['r']; P,T,N=st['P'],st['T'],st['N']; e=st['e']; G=st['G']
    wt=np.sqrt(g['weights'][:,None]/nphi); wr=np.sqrt(g['weights']); ncols=sys.size-(sys.nc if fixed else 0)
    mask=[a!=0 for a in st['chain']]; nbase=st['primary_rows']; J=np.zeros((nbase+sum(m.sum() for m in mask),ncols),order='F')
    a,b,k=st['abc']; T0=opt['T']; zero=np.zeros_like(a)
    def insert(slot,mat,dG,dgap,dclos,da,db,dk,dn):
        cols=mat.shape[1]; where=slice(slot,slot+cols)
        h=nr*nphi*3; J[:h,where]+=(dG[...,None]*(wt[...,None,None]*mat[:,None,None,:])).reshape(h,cols)
        J[h:h+2*nr,where]+=(dgap[:,[0,2],None]*(wr[:,None,None]*mat[:,None,:])).reshape(2*nr,cols)
        J[h+2*nr:nbase,where]+=(wr*dclos)[:,None]*mat
        changes=[]
        for s in (1,-1):
            changes.extend((s*T0*(da+dk)/2,s*T0*((1+s*T0*k)*da+(1+s*T0*a)*dk)-2*T0*T0*b*db))
        changes.extend((dn[...,2],math.sin(sys.ang)*dn[...,0]+math.cos(sys.ang)*dn[...,2]))
        offset=nbase
        for v,active,chain in zip(changes,mask,st['chain']):
            ir=np.nonzero(active)[0]; end=offset+len(ir)
            if len(ir): J[offset:end,where]+=(wt*chain*v)[active,None]*mat[ir]
            offset=end
    zvec=np.zeros_like(P); zgap=np.zeros_like(st['gap']); zclose=np.zeros(nr)
    for j,(side,mode) in enumerate(sys.blocks):
        V,Vr,Vp=st['axes'][side]; wave=g['wave'][j][None,:,None]; wavep=g['wave_p'][j][None,:,None]
        z=V*wave; zp=Vp*wave+V*wavep; zx=Vr*wave
        # Frame dot products eliminate the common rigid rotation parts from the II derivatives.
        def bend(zx,zp):
            return (dot(cross(zx,P),N)/e,(dot(cross(zp,P),N)/r+dot(cross(zx,T),N)/e)/2,dot(cross(zp,T),N)/r)
        main=cross(z,G)+cross(zp,st['EP'])-r[...,None]*cross(zx,T)
        insert(j*sys.na,g['A'][0],main,-(e[...,None]*cross(z,P)).mean(axis=1),cross(z,T)[...,1].mean(axis=1),*bend(zx,zp),cross(z,N))
        insert(j*sys.na,g['A'][1],-r[...,None]*cross(z,T),zgap,zclose,*bend(z,zvec),zvec)
    if not fixed:
        insert(sys.body,g['C'][0],st['EPp'],-st['EP'].mean(axis=1),zclose,-a,-dot(st['Tr'],N)/(2*e),zero,zvec)
    for j,axis in enumerate((0,2)):
        v=zgap.copy();v[:,axis]=1
        insert(sys.body+(j+int(not fixed))*sys.nc,g['C'][0],zvec,v,zclose,zero,zero,zero,zvec)
    lm=st['lb']!=0
    if lm.any():
        ii,jj=np.nonzero(lm); more=np.zeros((len(ii),ncols)); factor=st['lb'][lm,None]
        if not fixed:
            more[:,sys.body:sys.body+sys.nc]=-factor*st['ds'][jj,None]*((g['weights']*st['design_e'])@g['C'][0])[None,:]
        s0=sys.body+int(not fixed)*sys.nc
        for j in (0,1):
            more[:,s0+j*sys.nc:s0+(j+1)*sys.nc]=factor*st['sg'][ii]*st['dir'][jj,j,None]*sys.intc/(sys.b-sys.a)
        J=np.vstack((J,more))
    keep=np.r_[np.ones(nbase,dtype=bool),*[m.ravel() for m in mask],lm.ravel()]
    sys.count['full_material_matrices']+=1;sys.count['all_free_columns']+=ncols
    return J,keep


def physical(sys,x,g,st,level,opt,nbeta,full=True):
    T=st['T']; r=st['r']; rd=r[...,None]; U=primitive(T); Ur=primitive(st['Tr']); Urr=primitive(st['Trr'])
    H=mean_free(T); D=st['C0'][:,None,:]+U+rd*Ur
    rr=st['C1'][:,None,:]+2*Ur+rd*Urr; rp=H+rd*mean_free(st['Tr']); pp=rd*angular_derivative(H)
    area=cross(D,H); det=dot(area,area)
    if det.min()<=1e-18 or not np.isfinite(det).all(): raise FloatingPointError('Singular reconstructed physical immersion.')
    n=area/np.sqrt(det)[...,None]; a,b,c=dot(D,D),dot(D,H),dot(H,H)
    L,M,N=dot(n,rr),dot(n,rp)/r,dot(n,pp)/(r*r)
    def curvature(nn):
        mean=(c*L-2*b*M+a*nn)/(2*det); gauss=(L*nn-M*M)/det
        return np.abs(mean)+np.sqrt(np.maximum(0.,mean**2-gauss))
    kfft=curvature(N); Ncontinuous=dot(n,st['Tp'])/r
    kcontinuous=curvature(Ncontinuous); kabs=np.maximum(kfft,kcontinuous)
    ic=np.unravel_index(kabs.argmax(),kabs.shape)
    def location(value):
        i,j=np.unravel_index(value.argmax(),value.shape)
        return [float(g['r'][i]),float(g['phi'][j])]
    e=st['e']; ec=st['design_e'][:,None]
    def metrics(t):
        z=a/t**2-1; y=b/t; w=c-1
        val=np.abs((z+w)/2)+np.sqrt(((z-w)/2)**2+y*y); j=np.unravel_index(val.argmax(),val.shape)
        return float(val[j]),[float(g['r'][j[0]]),float(g['phi'][j[1]])]
    inp,ia=metrics(e); rot,ii=metrics(ec)
    C=sys.center(x,np.array([sys.a]))[0,[0,2]]
    sh=dict(actual_center=C,min_outer_normal=float(np.min(n[...,2])),min_inner_normal=float(np.min(n[...,2]*math.cos(sys.ang)+n[...,0]*math.sin(sys.ang))),
            max_abs_curvature=float(kabs[ic]))
    geo=shell(sys,x,g,dict(U=rz_frame(U,-g['q'][:,None])),sh)
    detail=dict(actual_geometry=geo,sampled_whole_geometry_gate=shell_ok(geo),sampled_design_eta=inp,design_attainer=ia,
                sampled_rotational_eta=rot,rotational_attainer=ii,sampled_max_abs_actual_curvature=float(kabs[ic]),
                curvature_attainer=[float(g['r'][ic[0]]),float(g['phi'][ic[1]])],
                sampled_odd_grid_interpolant_curvature=float(kfft.max()),sampled_odd_grid_curvature_attainer=location(kfft),
                sampled_continuous_Tphi_curvature_estimate=float(kcontinuous.max()),sampled_continuous_Tphi_curvature_attainer=location(kcontinuous),
                sampled_true_Tphi_minus_odd_grid_angular_derivative=float(np.max(np.linalg.norm(st['Tp']-angular_derivative(T),axis=-1))))
    if full:
        z,ds,dr,sg,margin,S=directional(sys,x,g,st,level,nbeta)
        formal_inv=-primitive(st['G'])+st['gap'][:,None,:]
        Gp=angular_derivative(st['EP'])-T-rd*st['Tr']
        inv=-primitive(Gp)+st['gap'][:,None,:]
        gap=st['gap']; dG=float(np.max(np.sqrt(dot(st['G'],st['G']).mean(axis=1))))
        gamma=float(np.max(np.linalg.norm(gap,axis=-1))); mn=float(np.min(e))
        alpha=(gamma+np.pi/math.sqrt(3)*dG)/mn; beta=(sys.b-sys.a)*dG/sys.a
        # Only an independent sample of the analytical continuous-defect estimate.
        budget=math.hypot(alpha,beta)
        frame=np.stack((st['P'],T,st['N']),axis=-1); ft=np.swapaxes(frame,-1,-2)
        overlap=ft@np.roll(frame,-1,axis=1); product=np.broadcast_to(np.eye(3),(len(r),3,3)).copy()
        for j in range(T.shape[1]): product=product@overlap[:,j]
        boundary={}
        for i,label,angle in ((0,'inner',sys.ang),(-1,'outer',0.)):
            if abs(g['r'][i]-(sys.a if i==0 else sys.b))<1e-12:
                expected=rz_frame(np.broadcast_to(g['er'],(1,T.shape[1],3)),np.array([[angle]]))[0]
                et=rz_frame(np.broadcast_to(g['et'],(1,T.shape[1],3)),np.array([[angle]]))[0]
                def maxrow(v):return float(np.max(np.linalg.norm(v,axis=-1)))
                boundary[label]=dict(actual_center=sys.center(x,g['r'][i:i+1] if i==0 else g['r'][-1:])[0].tolist(),
                                     centered_position_max=maxrow(r[i,0]*(U[i]-expected)),radial_unit_frame_max=maxrow(st['P'][i]-expected),
                                     true_Fr=maxrow(D[i]-expected),true_Fphi=maxrow(r[i,0]*(H[i]-et)),true_Frr=maxrow(rr[i]),
                                     true_Frphi=maxrow(rp[i]-et),odd_interpolant_Fphiphi=maxrow(pp[i]+r[i,0]*expected),
                                     continuous_Fphiphi=maxrow(r[i,0]*(st['Tp'][i]+expected)))
        # Same actual spline state at nested odd angles. Work in radial blocks to limit transient memory.
        aliases={key:[0.,0.] for key in ('T','Tr','Trr')}
        for start in range(0,len(g['r']),16):
            sl=slice(start,start+16); ng=sys.at(g['r'][sl],3*T.shape[1]); fs=st['e'][sl,0] if st['fixed_reference'] else None
            nested=sys.state(x,ng,level,fs)
            for key in aliases:
                lo,hi=st[key][sl],nested[key]
                aliases[key][0]=max(aliases[key][0],float(np.max(np.linalg.norm(lo.mean(axis=1)-hi.mean(axis=1),axis=-1))))
                aliases[key][1]=max(aliases[key][1],float(np.max(np.linalg.norm(primitive(lo)-primitive(hi)[:,::3],axis=-1))))
        detail.update(explicit_SO3_loop_product_error=float(np.max(abs(product-np.eye(3)))),
                      explicit_frame_orthogonality_error=float(np.max(abs(ft@frame-np.eye(3)))),
                      sampled_frame_reflection_meridian_angle_integral=float((sys.b-sys.a)*g['weights']@(st['abc'][0][:,0]*e[:,0])),
                      sampled_physical_reflection_meridian_angle_integral=float((sys.b-sys.a)*g['weights']@(L[:,0]/np.sqrt(a[:,0]))),
                      nested_angle_counts=[T.shape[1],3*T.shape[1]],nested_mean_and_primitive_differences=aliases,
                      prescribed_angle=sys.ang,actual_rim_pose_readout=boundary,sampled_compatibility_Linf=float(np.max(np.linalg.norm(st['G'],axis=-1))),sampled_uniform_in_radius_angle_RMS=dG,
                      sampled_true_center_velocity_gap=gamma,ring_unit_tangent_closure=float(np.max(np.linalg.norm(st['closure'],axis=-1))),
                      sampled_recovered_radial_frame_error=float(np.max(np.linalg.norm(D-st['EP'],axis=-1))),
                      odd_grid_primitive_identity_error=float(np.max(np.linalg.norm(D-st['EP']-inv,axis=-1))),
                      continuous_formula_on_grid_alias=float(np.max(np.linalg.norm(D-st['EP']-formal_inv,axis=-1))),
                      sampled_EP_angular_derivative_alias=float(np.max(np.linalg.norm(Gp-st['G'],axis=-1))),
                      sampled_true_angular_constraint=margin,sampled_future_rotational_meridian=S,
                      sampled_continuous_defect_metric_estimate=2*budget+budget*budget,
                      sampled_actual_hoop_b_min=float(np.min(N)),sampled_frame_hoop_b_min=float(np.min(st['abc'][2])),
                      sampled_e_range=[float(np.min(e)),float(np.max(e))],sampled_frozen_or_proposed_E_range=[float(ec.min()**2),float(ec.max()**2)])
    return detail


def lift(old,x,new):
    z=np.zeros(new.size); old_idx={b:i for i,b in enumerate(old.blocks)}
    added=[u for u in new.knots[new.degree+1:-new.degree-1] if not np.any(np.isclose(u,old.knots,rtol=0,atol=1e-14))]
    def move(row,pad):
        f=BSpline(old.knots,np.pad(row,pad),5)
        for knot in added: f=f.insert_knot(float(knot))
        return f.c[pad:-pad]
    for j,b in enumerate(new.blocks):
        if b in old_idx:
            i=old_idx[b]; z[j*new.na:(j+1)*new.na]=move(x[i*old.na:(i+1)*old.na],3)
    for i in range(3):
        z[new.body+i*new.nc:new.body+(i+1)*new.nc]=move(x[old.body+i*old.nc:old.body+(i+1)*old.nc],2)
    return z


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'
            or not os.environ.get('GITHUB_RUN_ID','').isdigit()): raise SystemExit('Scientific execution requires public Actions.')
    ap=argparse.ArgumentParser();ap.add_argument('--geometry',required=True);ap.add_argument('--max-seconds',required=True,type=float)
    args=ap.parse_args(); opt=json.loads(Path(args.geometry).read_text()); start=time.perf_counter(); elapsed=lambda:time.perf_counter()-start
    count=Counter(); sys=Frame(opt['base'],count); x=np.zeros(sys.size); frozen=None; trust=opt['initial_trust']; phase=0.; steps=0; history=[]; last_c=None
    def fixed_on(g):
        if frozen is None: return None
        fs,rho=frozen
        p=g['qx']*g['r']; return np.exp(.5*np.log1p((1.01**2+.5)*p*p)+fs.spl(g['r'])[:,2:-2]@rho)
    def guards(g):
        ref=sys.state(np.zeros(sys.size),g,0.); return [np.minimum(.8*v,cap) for v,cap in zip(cones(ref,opt['T'],sys.ang),(.3,.22,.3,.22,.4,.4))]
    def check(y,level,nr,np_):
        g=sys.grid(nr,np_,True); st=sys.state(y,g,level,fixed_on(g)); return physical(sys,y,g,st,level,opt,opt['fine_betas'])
    try:
        anchor=check(x,0.,opt['check_order'],opt['check_angles'])
        if not (anchor['sampled_design_eta']<1.e-10 and anchor['sampled_compatibility_Linf']<1.e-9 and anchor['sampled_whole_geometry_gate']):
            raise ArithmeticError('Actual R680 frame at zero homotopy was not reproduced.')
        emit('true_general_anchor',data=anchor,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),all_parameters=x.tolist())
        stages=list(opt['stages'])
        for i,stage in enumerate(stages):
            if elapsed()>args.max_seconds-opt['reserve_seconds']:break
            if stage['K']!=sys.K or stage['spans']!=sys.nsp:
                old=sys;sys=Frame(dict(old.spec,body_modes=stage['K'],radial_spans=stage['spans']),count);x=lift(old,x,sys);count['exact_space_prolongations']+=1
            g=sys.grid(stage['order'],stage['angles']); gf=sys.grid(opt['check_order'],opt['check_angles'],True); bounds=guards(g)
            fixed=fixed_on(g); ff=fixed_on(gf); frozen_now=frozen is not None; phase=stage['level']; free=np.ones(sys.size,dtype=bool)
            if frozen_now: free[sys.body:sys.body+sys.nc]=False
            def evaluate(y):return equations(sys,y,g,phase,opt,bounds,fixed)
            res,st=evaluate(x); trust=max(trust,opt['retarget_trust']); nacc=0; why='iteration_limit'
            emit('new_frame_stage',stage=i,level=phase,all_columns=sys.size,actual_free_columns=int(free.sum()),start_norm=float(np.linalg.norm(res)),frozen=frozen_now)
            for it in range(stage['iterations']):
                if elapsed()>args.max_seconds-opt['reserve_seconds']:why='scientific_budget';break
                J,keep=assemble(sys,g,st,opt,frozen_now)
                if it==0:
                    dx=np.sin(np.arange(1,J.shape[1]+1)*.543);dx/=np.linalg.norm(dx); v=np.zeros(sys.size);v[free]=dx; jv=J@dx; err=[]
                    for h in (3e-7,7e-8):
                        fd=(evaluate(x+h*v)[0]-evaluate(x-h*v)[0])/(2*h);err.append(float(np.linalg.norm(jv-fd[keep])/max(1e-15,np.linalg.norm(jv))))
                    emit('full_physical_frame_derivative',stage=i,original_free_columns=len(dx),errors=err)
                    if min(err)>5e-5:raise ArithmeticError('Actual full material-frame Jacobian did not contract correctly.')
                Q,R=qr(J,mode='economic',check_finite=False,overwrite_a=True); rhs=Q.T@res[keep];del Q,J
                U,sv,vt=svd(R,full_matrices=False,check_finite=False); force=-(U.T@rhs); count['all_free_QR_SVD']+=1
                if it==0:emit('complete_new_frame_singular_values',stage=i,values=sv.tolist())
                least=max(1e-19,6e-14*float(sv[0])**2);loss=float(res@res);ok=False
                for j in range(15):
                    delta,pred,mu=trust_step(sv,vt,force,trust,least);trial=x.copy();trial[free]+=delta; count['actual_frame_trials']+=1
                    try:
                        rn,sn=evaluate(trial);new=float(rn@rn);gain=(loss-new)/pred if pred>0 else -math.inf
                        if new<loss and gain>.02:
                            wk=physical(sys,trial,g,sn,phase,opt,opt['work_betas'],False)
                            if wk['sampled_whole_geometry_gate']:
                                ck=physical(sys,trial,gf,sys.state(trial,gf,phase,ff),phase,opt,opt['work_betas'],False)
                                if ck['sampled_whole_geometry_gate']:
                                    res,st,x=rn,sn,trial;steps+=1;nacc+=1;ok=True;last_c=ck
                                    if gain>.7 and np.linalg.norm(delta)>.8*trust:trust=min(1.75*trust,opt['max_trust'])
                                    elif gain<.2:trust*=.65
                                    emit('actual_frame_accepted',stage=i,level=phase,iteration=it,total_accepted=steps,norm=math.sqrt(new),
                                         independent=ck,trust=trust,damping=mu,all_parameters=x.tolist(),seconds=elapsed());break
                                count['rejected_by_independent_shell']+=1
                            else:count['rejected_by_work_shell']+=1
                    except FloatingPointError as exc:
                        emit('inadmissible_frame_trial',stage=i,iteration=it,trial=j,reason=str(exc));count['candidate_regular_domain_rejections']+=1
                    trust*=.38
                    if trust<1.e-10:break
                if not ok:why='no_admissible_reducing_step';break
                if np.linalg.norm(res)<opt['work_goal']:why='work_tolerance';break
            ans=check(x,phase,opt['stage_order'],opt['stage_angles']);info=dict(stage=i,level=phase,accepted=nacc,reason=why,
                 independent=ans,fixed=frozen_now,work_norm=float(np.linalg.norm(res)),seconds=elapsed());history.append(info)
            emit('frame_stage_terminal',**info,space=sys.spec,all_parameters=x.tolist(),counts=dict(count))
            if (phase==1. and not frozen_now and ans['sampled_rotational_eta']<=opt['freeze_eta'] and ans['ring_unit_tangent_closure']<=opt['freeze_eta']
                and ans['sampled_whole_geometry_gate'] and ans['sampled_true_angular_constraint']>=0):
                # This E is an analytic radial spline function and has no angular reference quadrature.
                frozen=(sys,x[sys.body:sys.body+sys.nc].copy());need=check(x,phase,opt['stage_order'],opt['stage_angles'])
                if not (need['sampled_rotational_eta']<=opt['freeze_eta'] and need['ring_unit_tangent_closure']<=opt['freeze_eta']
                        and need['sampled_whole_geometry_gate'] and need['sampled_true_angular_constraint']>=0):frozen=None
                else:
                    fixed_stage=dict(opt['fixed_stage'],spans=2*sys.nsp,K=max(sys.K+2,opt['fixed_stage']['K']))
                    if fixed_stage['spans']>48:
                        fixed_stage.update(order=4,angles=65)
                    stages[:]=stages[:i+1]+[fixed_stage];emit('actual_radial_E_frozen',space=sys.spec,log_spline=frozen[1].tolist(),physical=need)
        crossgrids={}
        for key,order,nangle in [('radius_only',opt['final_order'],opt['stage_angles']),('angle_only',opt['stage_order'],opt['final_angles']),
                                 ('both',opt['final_order'],opt['final_angles'])]:crossgrids[key]=check(x,phase,order,nangle)
        emit('terminal',stages=history,attempted_level=phase,actual_space=sys.spec,all_parameters=x.tolist(),accepted=steps,trust=trust,
             fixed_metric=None if frozen is None else dict(space=frozen[0].spec,log_radial_coefficients=frozen[1].tolist()),
             independent_crossed=crossgrids,counts=dict(count),elapsed_seconds=elapsed(),certified_all_points=False,README_completion_claim=False)
    except Exception as exc:
        emit('incomplete',reason=str(exc),actual_space=sys.spec,all_parameters=x.tolist(),last_independent=last_c,
             counts=dict(count),elapsed_seconds=elapsed());raise


if __name__=='__main__':main()
