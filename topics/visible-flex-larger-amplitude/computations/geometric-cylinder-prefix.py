#!/usr/bin/env python3
"""Cylindrical graph and nearby-pair screening of a saved strong-core prefix.

Recursively includes every input segment. A common Hermite two-jet is used
at a shared endpoint and the original one-sided discrepancies are reported.
All reported extrema and point-pair searches are samples, not interval
certificates. The reflected surface has boundary and no closed-surface
reach claim is made.
"""
from __future__ import annotations
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[k]='1'
import argparse,gzip,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly
from scipy.spatial import cKDTree
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;TOPIC=HERE.parent;REPO=HERE.parents[2]


def load(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m


geo=load('geometric_cylinder_geometry',HERE/'geometric-alternative-geometry.py')
control=load('geometric_cylinder_control',HERE/'alternative-controlled-profile.py')


def json_read(path):
    raw=path.read_bytes();return json.loads(gzip.decompress(raw)if path.suffix=='.gz'else raw)


def resolve_input(name,parent):
    p=Path(name)
    for q in (p,REPO/p,TOPIC/p,parent.parent/p):
        if q.exists():return q.resolve()
    raise FileNotFoundError(name)


def history(path,seen=None):
    seen=set()if seen is None else seen;path=path.resolve()
    if path in seen:raise ValueError('Cyclic input history')
    seen.add(path);d=json_read(path);rows=[]
    if d.get('input'):
        prior=resolve_input(d['input'],path)
        if hashlib.sha256(prior.read_bytes()).hexdigest()!=d['input_sha256']:
            raise ValueError('Input ancestor hash differs: '+str(prior))
        rows=history(prior,seen)
    rows.append((path,d));return rows


def lift(y,old,new):
    out=np.zeros(3*new+2);out[:old+1]=y[:old+1]
    out[new+1:new+old+1]=y[old+1:2*old+1]
    out[2*new+1:2*new+old+2]=y[2*old+1:]
    return out


def quintic(s,Y,D,Q):
    h=np.diff(s)[:,None]
    e0=Y[1:]-Y[:-1]-h*D[:-1]-h*h*Q[:-1]/2
    e1=D[1:]-D[:-1]-h*Q[:-1];e2=Q[1:]-Q[:-1]
    u=10*e0-4*h*e1+h*h*e2/2;v=-15*e0+7*h*e1-h*h*e2
    w=6*e0-3*h*e1+h*h*e2/2
    c=np.stack((w/h**5,v/h**4,u/h**3,Q[:-1]/2,D[:-1],Y[:-1]))
    return PPoly.construct_fast(c,s,extrapolate=False,axis=0)


class Trajectory:
    def __init__(self,path):
        self.history=history(path);self.cfg=self.history[-1][1]['config']
        self.M=max(d['config']['M']for _,d in self.history)
        self.probe=control.make_probe(self.cfg,M=self.M,N=1024)
        self.A=self.cfg['A'];self.seams=[];self.manifest=[]
        S=[];Y=[];D=[];Q=[]
        for path,d in self.history:
            cfg=d['config'];m=cfg['M'];probe=control.make_probe(cfg)
            ss=np.array([r['s']for r in d['rows']]);yy=np.asarray(d['coefficient_states'])
            if len(ss)!=len(yy):raise ValueError('Incomplete coefficient history')
            dd=[];qq=[]
            for s,y in zip(ss,yy):
                dy,d2y=geo.finite_ode_jets(probe,float(s),y);dd.append(lift(dy,m,self.M));qq.append(lift(d2y,m,self.M))
            yy=np.array([lift(y,m,self.M)for y in yy]);dd=np.asarray(dd);qq=np.asarray(qq)
            if S:
                if abs(ss[0]-S[-1])>2e-12:raise ValueError('A radial gap occurs in the input chain')
                old=(Y[-1],D[-1],Q[-1]);new=(yy[0],dd[0],qq[0]);differences=[]
                for x,y in zip(old,new):
                    value=self.probe.jet(y-x)[0]
                    differences.append(float(np.linalg.norm(value,axis=1).max()))
                self.seams.append(dict(s=float(ss[0]),position_jump_sample=differences[0],
                    first_radial_jet_jump_sample=differences[1],second_radial_jet_jump_sample=differences[2],
                    common_jet='Right segment endpoint jet, used on both adjacent Hermite spans.'))
                if differences[0]>1e-9 or differences[1]>1e-7 or differences[2]>1e-5:
                    raise ValueError('Input seam discrepancy too large for the stated reconstruction: '+str(differences))
                Y[-1]=yy[0];D[-1]=dd[0];Q[-1]=qq[0]
                ss=ss[1:];yy=yy[1:];dd=dd[1:];qq=qq[1:]
            S.extend(ss.tolist());Y.extend(yy);D.extend(dd);Q.extend(qq)
            self.manifest.append(dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                modes=m,original_angular=cfg['N'],start=float(d['rows'][0]['s']),end=float(d['reached_s']),
                source_metric_sample=d.get('whole_sample_max_metric'),source_kappa_sample=d.get('whole_sample_max_kappa')))
        self.s=np.asarray(S)
        if self.s[0]!=0:raise ValueError('History does not start at the core')
        self.end=float(self.s[-1]);self.pp=quintic(self.s,np.asarray(Y),np.asarray(D),np.asarray(Q))

    def basis(self,N):
        phi=2*np.pi*np.arange(N)/N;n=2*np.arange(self.M+1)
        return phi,n,np.cos(n[:,None]*phi),np.sin(n[:,None]*phi)

    def jets(self,Y,basis):
        phi,n,C,Sn=basis;r=Y[:,:self.M+1];t=Y[:,self.M+1:2*self.M+1];z=Y[:,2*self.M+1:]
        R=r@C;T=t@Sn[1:];Z=z@C
        Rp=(-r*n)@Sn;Tp=(t*n[1:])@C[1:];Zp=(-z*n)@Sn
        Rpp=(-r*n*n)@C;Tpp=(-t*n[1:]**2)@Sn[1:];Zpp=(-z*n*n)@C
        return tuple(geo.world(v,phi)for v in
            (np.stack((R,T,Z),axis=-1),np.stack((Rp-T,Tp+R,Zp),axis=-1),
             np.stack((Rpp-2*Tp-R,Tpp+2*Rp-T,Zpp),axis=-1)))

    def geometry(self,s,basis):
        X,Xp,Xpp=self.jets(self.pp(s),basis);Xs,Xsp,_=self.jets(self.pp(s,1),basis)
        Xss,_,_=self.jets(self.pp(s,2),basis)
        E=np.sum(Xs*Xs,axis=2);F=np.sum(Xs*Xp,axis=2);G=np.sum(Xp*Xp,axis=2)
        normal=np.cross(Xp,Xs);normal/=np.linalg.norm(normal,axis=2)[:,:,None]
        L=np.sum(Xss*normal,axis=2);M=np.sum(Xsp*normal,axis=2);N=np.sum(Xpp*normal,axis=2)
        determinant=E*G-F*F;trace=(L*G+N*E-2*M*F)/determinant
        kd=(L*N-M*M)/determinant;K=(abs(trace)+np.sqrt(np.maximum(0,trace*trace-4*kd)))/2
        R=np.linalg.norm(X[:,:,:2],axis=2)
        beta_s=(X[:,:,0]*Xs[:,:,1]-X[:,:,1]*Xs[:,:,0])/R**2
        beta_p=(X[:,:,0]*Xp[:,:,1]-X[:,:,1]*Xp[:,:,0])/R**2
        z_s=Xs[:,:,2];z_p=Xp[:,:,2];J=beta_p*z_s-beta_s*z_p
        rho0=1-3*self.A*np.cos(2*basis[0])+15*self.A/(10*math.sqrt(2))*np.cos(4*basis[0])
        aa=np.array([self.probe.profile(float(v))[0]for v in s])
        metric=np.maximum.reduce((abs(E-1),abs(F)/(aa[:,None]*rho0[None,:]),abs(G/(aa[:,None]**2*rho0[None,:]**2)-1)))
        return dict(X=X,Xs=Xs,Xp=Xp,normal=normal,K=K,R=R,beta=np.arctan2(X[:,:,1],X[:,:,0]),
            beta_s=beta_s,beta_phi=beta_p,beta_theta=beta_p/rho0[None,:],
            J_phi=J,J_theta=J/rho0[None,:],z_s_at_fixed_beta=J/beta_p,
            z_beta=z_p/beta_p,metric=metric,star_support=np.sum(X*normal,axis=2))


def scalar_extreme(value,s,phi,X,minimum):
    flat=int(np.argmin(value)if minimum else np.argmax(value));i,j=np.unravel_index(flat,value.shape)
    return dict(value=float(value[i,j]),s=float(s[i]),phi=float(phi[j]),point=X[i,j].tolist())


def radial_grid(traj,radial):
    """Merge floating-point duplicates, not genuine short radial spans.

    Source nodes and the uniform grid can encode the same real number with
    different last bits. Keeping both makes height divided differences divide
    roundoff by an artificial O(eps) step.
    """
    ordered=np.sort(np.r_[np.linspace(0,traj.end,radial),traj.s])
    tol=64*np.finfo(float).eps*max(1.,abs(traj.end));out=[ordered[0]]
    for value in ordered[1:]:
        if value-out[-1]>tol:out.append(value)
    out=np.asarray(out);out[0]=traj.s[0];out[-1]=traj.end
    return out


def cylindrical_screen(traj,angular,radial):
    start=time.time();ss=radial_grid(traj,radial);basis=traj.basis(angular)
    phi=basis[0];keys_min=('R','beta_phi','beta_theta','J_phi','J_theta','z_s_at_fixed_beta','star_support')
    keys_max=('K','metric');lo={k:None for k in keys_min};hi={k:None for k in keys_max}
    zbeta=0.;D=0.;winding_lo=math.inf;winding_hi=-math.inf;max_beta_step=0.;heights=[]
    grid_beta=2*np.pi*np.arange(256)/256;A=1+traj.A-traj.A/(10*math.sqrt(2));p=np.array([0.,A,0.]);witness=None
    for first in range(0,len(ss),12):
        s=ss[first:first+12];g=traj.geometry(s,basis)
        for k in keys_min:
            q=scalar_extreme(g[k],s,phi,g['X'],True)
            if lo[k]is None or q['value']<lo[k]['value']:lo[k]=q
        for k in keys_max:
            q=scalar_extreme(g[k],s,phi,g['X'],False)
            if hi[k]is None or q['value']>hi[k]['value']:hi[k]=q
        q=scalar_extreme(np.linalg.norm(g['X']-p,axis=2),s,phi,g['X'],True)
        if witness is None or q['value']<witness['value']:witness=q
        zbeta=max(zbeta,float(abs(g['z_beta']).max()));D=max(D,2*float(np.linalg.norm(g['X'],axis=2).max()))
        for beta,z in zip(g['beta'],g['X'][:,:,2]):
            step=np.angle(np.exp(1j*(np.roll(beta,-1)-beta)))
            winding=float(step.sum()/(2*np.pi));winding_lo=min(winding_lo,winding);winding_hi=max(winding_hi,winding)
            max_beta_step=max(max_beta_step,float(abs(step).max()))
            lift=np.r_[beta[0],beta[0]+np.cumsum(step)]
            if np.any(np.diff(lift)<=0):raise ValueError('Sampled cylindrical angle is not monotone')
            target=lift[0]+np.mod(grid_beta-lift[0],2*np.pi)
            heights.append(np.interp(target,lift,np.r_[z,z[0]]))
    heights=np.asarray(heights);dz=np.diff(heights,axis=0)/np.diff(ss)[:,None]
    r0=lo['R']['value'];m=lo['z_s_at_fixed_beta']['value']
    inverse=np.array([[1/m,math.pi*zbeta/(2*m*r0)],[0,math.pi/2]])
    C=float(np.linalg.norm(inverse,2))
    return dict(radial_samples=len(ss),minimum_radial_sample_spacing=float(np.diff(ss).min()),angular=angular,minima=lo,maxima=hi,
        winding_min=winding_lo,winding_max=winding_hi,maximum_sample_angle_step=max_beta_step,
        fixed_beta_height_difference_quotient_min=float(dz.min()),fixed_beta_height_samples=256,
        top_height_min=float(heights[-1].min()),top_height_max=float(heights[-1].max()),
        top_bottom_height_gap_min=float(2*heights[-1].min()),maximum_abs_z_beta=zbeta,
        conditional_product_chart_inverse_Lipschitz_C=C,
        conditional_distance_bound_rule='If continuous r0,m,L bounds hold, |F(p)-F(q)| >= sqrt((delta_s)^2+(r0*cyclic_delta_beta)^2)/C.',
        D_reflected_prefix_sample=D,target_three_percent_D=.03*D,
        sampled_curvature_radius=1/hi['K']['value'],sampled_curvature_radius_over_D=1/(D*hi['K']['value']),
        core_major_witness_distance_sample=witness,seconds=time.time()-start)


def pair_screen(traj,screen,angular=256,radial=81,query_radial=41,query_angular=64):
    start=time.time();s=radial_grid(traj,radial);basis=traj.basis(angular)
    xs=[];ns=[]
    for first in range(0,len(s),16):
        g=traj.geometry(s[first:first+16],basis);xs.append(g['X']);ns.append(g['normal'])
    up=np.concatenate(xs);normal=np.concatenate(ns);down=up[:0:-1].copy();dn=normal[:0:-1].copy()
    down[:,:,2]*=-1;dn[:,:,2]*=-1
    X=np.concatenate((down,up)).reshape(-1,3);normals=np.concatenate((dn,normal)).reshape(-1,3)
    full_s=np.r_[-s[:0:-1],s];S=np.repeat(full_s,angular);P=np.tile(basis[0],len(full_s))
    Beta=np.arctan2(X[:,1],X[:,0]);tree=cKDTree(X);r0=screen['minima']['R']['value']
    js=np.unique(np.round(np.linspace(0,len(full_s)-1,query_radial)).astype(int))
    ks=np.unique(np.round(np.arange(query_angular)*angular/query_angular).astype(int)%angular)
    query=np.array([j*angular+k for j in js for k in ks]);thresholds=[.25,.5,1.]
    best={str(v):None for v in thresholds};unresolved={str(v):0 for v in thresholds}
    brute_force_fallbacks={str(v):0 for v in thresholds};all_ids=np.arange(len(X))
    radius=2*screen['target_three_percent_D'];near_thresholds=[0.,.25,.5,1.]
    qbest={str(v):None for v in near_thresholds};counts={str(v):0 for v in near_thresholds}
    def separation(ids,i):
        db=abs((Beta[ids]-Beta[i]+np.pi)%(2*np.pi)-np.pi)
        return np.sqrt((S[ids]-S[i])**2+(r0*db)**2)
    def record(i,j,d):
        chord=X[j]-X[i];den=2*max(abs(normals[i]@chord),abs(normals[j]@chord))
        return dict(distance=float(d),product_chart_separation=float(separation(np.array([j]),i)[0]),
            minimum_ordered_normal_chord_quotient=float(d*d/den)if den>0 else None,
            first=dict(s=float(S[i]),phi=float(P[i]),beta=float(Beta[i]),point=X[i].tolist()),
            second=dict(s=float(S[j]),phi=float(P[j]),beta=float(Beta[j]),point=X[j].tolist()))
    for first in range(0,len(query),32):
        inds=query[first:first+32];k=64
        while True:
            ds,idx=tree.query(X[inds],k=min(k,len(X)),workers=1)
            db=abs((Beta[idx]-Beta[inds,None]+np.pi)%(2*np.pi)-np.pi)
            sep=np.sqrt((S[idx]-S[inds,None])**2+(r0*db)**2)
            if np.all(np.any(sep>=thresholds[-1],axis=1))or k>=min(32768,len(X)):break
            k*=2
        for eta in thresholds:
            valid=(sep>=eta)&(ds>1e-12);ok=np.any(valid,axis=1);pos=np.argmax(valid,axis=1)
            unresolved[str(eta)]+=int(np.sum(~ok))
            for row in np.flatnonzero(ok):
                ii=int(inds[row]);jj=int(idx[row,pos[row]]);distance=float(ds[row,pos[row]])
                if best[str(eta)]is None or distance<best[str(eta)]['distance']:best[str(eta)]=record(ii,jj,distance)
            for row in np.flatnonzero(~ok):
                ii=int(inds[row]);valid_ids=all_ids[separation(all_ids,ii)>=eta]
                brute_force_fallbacks[str(eta)]+=1
                if not len(valid_ids):continue
                dd=np.sum((X[valid_ids]-X[ii])**2,axis=1);where=int(np.argmin(dd));jj=int(valid_ids[where])
                distance=math.sqrt(float(dd[where]));unresolved[str(eta)]-=1
                if best[str(eta)]is None or distance<best[str(eta)]['distance']:best[str(eta)]=record(ii,jj,distance)
        for ii in inds:
            ids=np.asarray(tree.query_ball_point(X[ii],radius),int);delta=X[ids]-X[ii]
            dd=np.sum(delta*delta,axis=1);sep=separation(ids,ii)
            den=2*np.maximum(abs(delta@normals[ii]),abs(np.sum(delta*normals[ids],axis=1)))
            quotient=np.divide(dd,den,out=np.full_like(dd,np.inf),where=den>1e-18)
            for eta in near_thresholds:
                mask=(dd>1e-16)&(sep>=eta);counts[str(eta)]+=int(np.sum(mask))
                if not np.any(mask):continue
                jj=int(np.flatnonzero(mask)[np.argmin(quotient[mask])]);value=float(quotient[jj])
                if qbest[str(eta)]is None or value<qbest[str(eta)]['minimum_ordered_normal_chord_quotient']:
                    qbest[str(eta)]=record(int(ii),int(ids[jj]),math.sqrt(float(dd[jj])))
        if first and first%512==0:print(json.dumps(dict(event='pair_progress',queries_done=first,total=len(query))),flush=True)
    return dict(target_points=len(X),query_points=len(query),pair_angular=angular,pair_radial=len(full_s),
        nearest_pairs_under_product_separation=best,unresolved_query_counts=unresolved,
        brute_force_fallback_counts=brute_force_fallbacks,
        normal_chord_search_radius=radius,minimum_normal_chord_quotients_in_radius=qbest,
        accepted_ordered_pair_counts=counts,seconds=time.time()-start,
        scope='All targets in the stated finite cloud, selected source queries. Product separation uses signed s and cylindrical beta. Normal-chord quotients are diagnostics; with-boundary reach is not certified.')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angular',type=int,default=1024);p.add_argument('--radial',type=int,default=401)
    p.add_argument('--pair-angular',type=int,default=256);p.add_argument('--pair-radial',type=int,default=81)
    p.add_argument('--query-radial',type=int,default=41);p.add_argument('--query-angular',type=int,default=64)
    p.add_argument('--skip-pairs',action='store_true');a=p.parse_args();begin=time.time()
    q=Trajectory(a.input);r=dict(scope=__doc__,input=str(a.input),manifest=q.manifest,seam_checks=q.seams,
        common_modes=q.M,end_s=q.end,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    r['cylindrical']=cylindrical_screen(q,a.angular,a.radial)
    a.out.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(dict(event='cylinder',seams=q.seams,screen=r['cylindrical'])),flush=True)
    if not a.skip_pairs:r['pairs']=pair_screen(q,r['cylindrical'],a.pair_angular,a.pair_radial,a.query_radial,a.query_angular)
    r['seconds']=time.time()-begin
    r['caveats']=['Sample positivity is not a continuous-domain proof.','At a changed Fourier cutoff, original seam jets differ; the reported common-jet Hermite correction makes the reconstruction C2.',
       'This reconstruction is not a new solved finite ODE trajectory.','The doubled prefix has two boundary circles; no closed-surface or boundary-cone reach certificate is supplied.']
    a.out.write_text(json.dumps(r,indent=2)+'\n')
    if not a.skip_pairs:print(json.dumps(dict(event='pairs',result=r['pairs'])),flush=True)


if __name__=='__main__':main()
