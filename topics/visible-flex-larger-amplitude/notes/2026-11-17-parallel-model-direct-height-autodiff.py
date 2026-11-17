#!/usr/bin/env python3
"""Geometry homotopy and free-metric design for the direct-height solver.

Amplitude below one is a synthetic, locally compatible cut used only as an
optimization path; it is not an accepted prefix family.  Amplitude one uses
the original true Cartesian 0/1/2 jets.  Metric variables are design variables;
they must be frozen before any convergence claim.  All reported geometric
errors are literal sampled Gram errors after radial quadrature.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
import autograd.numpy as anp
from autograd import value_and_grad,make_jvp,make_vjp
from autograd.extend import primitive,defvjp,defjvp
from scipy.optimize import minimize,least_squares
from scipy.sparse.linalg import LinearOperator
from scipy.interpolate import BSpline

HERE=Path(__file__).parent
spec=importlib.util.spec_from_file_location('direct_height_base',HERE/'2026-11-17-parallel-model-direct-height-gram.py')
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
spec=importlib.util.spec_from_file_location('angular_height_helper',HERE/'2026-11-17-parallel-model-angular-reconstruct.py')
angular=importlib.util.module_from_spec(spec);spec.loader.exec_module(angular)

@primitive
def drows(v):return base.derivative(v,axis=1)
@primitive
def dline(v):return base.derivative(v,axis=0)
defvjp(drows,lambda ans,v:lambda g:-drows(g))
defvjp(dline,lambda ans,v:lambda g:-dline(g))
defjvp(drows,lambda g,ans,v:drows(g))
defjvp(dline,lambda g,ans,v:dline(g))

class Design(base.DirectHeight):
    def __init__(self,args):
        defaults=dict(metric_knots='[0.005,0.015,0.04,0.08,0.15,0.25,0.4]',angular_basis='material',
                      actual_curvature_weight=0.,actual_curvature_limit=6.8,freeze_metric=False,scaling='norm',function_tolerance=1e-20,
                      metric_height_coupling=True)
        for k,v in defaults.items():
            if not hasattr(args,k):setattr(args,k,v)
        if args.height_knots=='segments':
            raw=json.loads(args.background.read_text());r0=json.loads(args.trace.read_text())['r']
            ks=[v['r']-r0 for v in raw['rows'] if v['x'] in (0,1)]
            ks.extend(json.loads(args.metric_knots));ks.extend([.001,.003])
            args.height_knots=json.dumps(sorted(set(ks)))
        super().__init__(args)
        self.base_source_sha=self.source_sha;self.source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        mk=np.array(json.loads(args.metric_knots));mk=np.unique(mk[(mk>0)&(mk<self.L)])
        mt=np.r_[np.repeat(0.,4),mk,np.repeat(self.L,4)];mn=len(mt)-4
        ms=BSpline(mt,np.eye(mn),3);mf=np.arange(3,mn-3)
        self.ng=min(args.metric_modes,len(mf));self.MB=[ms(self.x,j)[:,mf[:self.ng]] for j in range(3)]
        self.metric_spline=ms;self.metric_free=mf[:self.ng]
        self.nheight=self.n;self.n+=self.ng
        self.oldlogw=np.log(self.w);self.oldlogwr=self.wr/self.w
        if args.amplitude!=1:self.set_homotopy_cut(args.amplitude)
        self.hppj=base.derivative(self.hpj,axis=1)
        self.base_hpp=self.base[0]@self.hppj
        self.base_hrr=(self.wr+self.base[2]@self.delta_mean)[:,None]+self.base[2]@self.hjets
        dw=self.width*np.einsum('q,cq->c',self.gw,self.w.reshape(self.r.shape))
        primitive=(np.r_[0,np.cumsum(dw)[:-1]][:,None]+self.width[:,None]*(self.w.reshape(self.r.shape)@self.gI.T)).ravel()
        self.base_H=(self.h0mean[0]+primitive+self.base[0]@self.delta_mean)[:,None]+self.base[0]@self.hjets
        self.base_increment_offset=0.
        if args.angular_basis=='physical':
            self.C=np.cos(self.phi[:,None]*self.freq);self.Cp=-np.sin(self.phi[:,None]*self.freq)*self.freq
            self.Cpp=-self.C*self.freq**2
        else:
            rc=np.array(self.trace['rho_cos_coefficients']);rf=2*np.arange(1,len(rc)+1)
            rhop=-np.sin(self.phi[:,None]*rf)@(rf*rc)
            self.Cpp=-rhop[:,None]*np.sin(self.theta[:,None]*self.freq)*self.freq-self.rho[:,None]**2*self.C*self.freq**2
        u=np.clip(self.x/self.join_width,0,1);mask=self.x<self.join_width
        ch=(1-10*u**3+15*u**4-6*u**5)*mask
        cp=(-30*u*u+60*u**3-30*u**4)/self.join_width*mask
        cpp=(-60*u+180*u*u-120*u**3)/self.join_width**2*mask
        self.correct_Frr=(2*cp+self.x*cpp)[:,None,None]*self.delta_Fr+(ch+2*self.x*cp+.5*self.x*self.x*cpp)[:,None,None]*self.delta_Frr
        self.calls=0;self.best=float('inf');self.started=time.perf_counter();self.last_info=None
        self._vg=value_and_grad(lambda x:.5*anp.sum(self.ad_residual(x)**2))

    def set_homotopy_cut(self,lam):
        if not 0<=lam<=1:raise ValueError('Homotopy amplitude must lie in [0,1]')
        t=self.trace;r=t['r'];w=t['w'];wr=t['w_r'];z=w*w;E=1+z
        f=2*np.arange(1,t['M']+1);hc=np.array(t['height_cos_coefficients']);vc=np.array(t['height_r_cos_coefficients']);rc=np.array(t['rho_cos_coefficients'])
        def analytic(phi,c):
            co=np.cos(phi[:,None]*f);si=np.sin(phi[:,None]*f)
            rho=1+co@rc;rhop=-si@(f*rc)
            h=t['height_mean']+lam*(co@hc);hp=-lam*si@(f*hc);hpp=-lam*co@(f*f*hc)
            K=c+lam*(co@vc)/w;Kp=-lam*(si@(f*vc))/w
            P=hp/(r*w*rho);T=(hpp*rho-hp*rhop)/(r*w*rho**3);V=Kp/rho
            S=1-z*P*P;A=2*K+K*K+E*P*P;D=1-z*A;L=1+K+E*T
            B=A/(np.sqrt(D)*(1+np.sqrt(D)))+(1+K)*T/(S*np.sqrt(D))
            kr=-(wr/w)*(2*K+T)+(E/r*(V-P)**2+(wr/w)*((K+T)**2+z*(2*K*T+T*T-P*P)))/L
            return dict(h=h,hp=hp,hpp=hpp,hr=w*(1+K),hrp=w*Kp,hrr=wr*(1+K)+w*kr,
                        hrpp=-lam*co@(f*f*vc),rho=rho,rhop=rhop,S=S,D=D,L=L,B=B)
        c=0.
        for iteration in range(40):
            u=analytic(self.phi,c);mean=float(np.mean(self.rho*u['B']));mu=float(np.mean(self.rho*u['L']/u['D']**1.5))
            if abs(mean)<2e-14:break
            step=-mean/mu
            for shrink in range(30):
                with np.errstate(invalid='ignore',divide='ignore'):
                    trial=analytic(self.phi,c+step)
                if min(np.min(trial['D']),np.min(trial['L']))>0 and np.isfinite(trial['B']).all() and abs(np.mean(self.rho*trial['B']))<abs(mean):break
                step*=.5
            c+=step
        u=analytic(self.phi,c);hrrp=analytic(self.phi.astype(complex)+1j*1e-25,c)['hrr'].imag/1e-25
        self.h0mean=np.array([np.mean(u[k]) for k in ('h','hr','hrr')])
        self.hjets=np.array([u[k]-v for k,v in zip(('h','hr','hrr'),self.h0mean)])
        self.hpj=np.array([u['hp'],u['hrp'],hrrp])
        initial=angular.reconstruct_slice(r=r,w=w,wr=wr,h=u['h'],hr=u['hr'],hrr=u['hrr'],
            h_phi=u['hp'],h_phiphi=u['hpp'],hr_phi=u['hrp'],hr_phiphi=u['hrpp'],rho=self.rho,rho_phi=u['rhop'])
        self.alpha0=initial['alpha'];self.xy0=initial['F'][:,:2]
        if lam==0:
            self.alpha0=self.theta+np.pi/2;self.xy0=r*np.column_stack((np.cos(self.theta),np.sin(self.theta)))
        self.delta_mean=np.array([0.,self.h0mean[1]-w,self.h0mean[2]-wr])
        self.base_hp=self.base[0]@self.hpj;self.base_hrp=self.base[1]@self.hpj
        self.base_hr=(self.w+self.base[1]@self.delta_mean)[:,None]+self.base[1]@self.hjets
        fake=[]
        for key in ('h','hr','hrr'):
            value=np.zeros((self.N,3));value[:,2]=u[key];fake.append((value,None,None))
        self._initial_correction(fake)
        self.true_Fr0=self.constructed_Fr0;self.true_Frr0=self.constructed_Frr0
        self._initial_correction(fake)
        self.homotopy=dict(amplitude=lam,mean_root=c,weighted_mean=float(np.mean(self.rho*u['B'])),
                           boundary_minimum_D=float(u['D'].min()),boundary_minimum_L=float(u['L'].min()),
                           scope='Synthetic locally compatible cut; not an accepted prefix')

    def graph(self,x,lib):
        coupling=float(self.args.metric_height_coupling)
        xx=x[:self.nheight];c=lib.reshape(xx[:-1],(self.M+1,self.nf))*self.height_scale;end=xx[-1]*self.height_scale
        gc=x[self.nheight:];logw=self.oldlogw+lib.dot(self.MB[0][:,:self.ng],gc)
        w=lib.exp(logw);wr=w*(self.oldlogwr+lib.dot(self.MB[1][:,:self.ng],gc));E=1+w*w
        radial=lib.dot(self.B[0],lib.transpose(c[1:]));radial_r=lib.dot(self.B[1],lib.transpose(c[1:]))
        hp=self.base_hp+lib.dot(radial,self.Cp.T)
        hr=self.base_hr+coupling*(w-self.w)[:,None]+(lib.dot(self.B[1],c[0])+self.Bend[1]*end)[:,None]+lib.dot(radial_r,self.C.T)
        hrp=self.base_hrp+lib.dot(radial_r,self.Cp.T)
        r=self.flat_r[:,None];rho=self.rho[None,:]
        S=1-(hp/(r*rho))**2;D=E[:,None]*S-hr*hr
        Sf=lib.where(lib.real(S)>self.args.branch_floor,S,self.args.branch_floor)
        Df=lib.where(lib.real(D)>self.args.branch_floor,D,self.args.branch_floor)
        a=lib.sqrt(Df/Sf);q=r*rho*lib.sqrt(Sf);b=-hr*hp/q
        A=hr*(hrp-hp/r)/(r*rho*Sf*lib.sqrt(Df));shape=(self.nc,len(self.gx),self.N)
        AA=lib.reshape(A,shape);da=self.width[:,None]*lib.einsum('q,cqn->cn',self.gw,AA)
        before=lib.concatenate((lib.zeros_like(da[:1]),lib.cumsum(da,axis=0)[:-1]),axis=0)
        alpha=self.alpha0+before[:,None,:]+self.width[:,None,None]*lib.einsum('ij,cjn->cin',self.gI,AA)
        alpha=lib.reshape(alpha,(-1,self.N));tt=lib.stack((lib.cos(alpha),lib.sin(alpha)),axis=-1);nn=lib.stack((lib.sin(alpha),-lib.cos(alpha)),axis=-1)
        V=b[:,:,None]*tt+a[:,:,None]*nn;VV=lib.reshape(V,(*shape,2))
        dx=self.width[:,None,None]*lib.einsum('q,cqnk->cnk',self.gw,VV)
        before_xy=lib.concatenate((lib.zeros_like(dx[:1]),lib.cumsum(dx,axis=0)[:-1]),axis=0)
        xy=self.xy0+before_xy[:,None,:,:]+self.width[:,None,None,None]*lib.einsum('ij,cjnk->cink',self.gI,VV)
        xy=lib.reshape(xy,(-1,self.N,2))+self.correct_xy;Vr=V+self.correct_Fr;xp=drows(xy)
        er=(lib.sum(Vr*Vr,axis=2)+hr*hr)/E[:,None]-1
        gr=(lib.sum(xp*xp,axis=2)+hp*hp)/(r*rho)**2-1
        fr=(lib.sum(Vr*xp,axis=2)+hr*hp)/(lib.sqrt(E)[:,None]*r*rho)
        ae=self.alpha0+lib.sum(da,axis=0);xe=self.xy0+lib.sum(dx,axis=0)
        te=lib.stack((lib.cos(ae),lib.sin(ae)),axis=-1);ne=lib.stack((lib.sin(ae),-lib.cos(ae)),axis=-1)
        turn=1+dline(ae-self.phi)-self.rho;T=dline(xe)-self.r1*self.rho[:,None]*te;circle=xe-self.r1*ne
        increment=lib.sum(self.width[:,None]*self.gw*lib.reshape(self.w+coupling*(w-self.w),self.r.shape))+end+self.base_increment_offset
        curvature=lib.abs(wr)/E**1.5
        result=dict(er=er,gr=gr,fr=fr,S=S,D=D,turn_end=turn,T_end=T,circle_end=circle,
                    height_increment=increment,hr=hr,hp=hp,w=w,wr=wr,reference_curvature=curvature,
                    radial_increment=dx)
        if hasattr(self,'deep_base_height'):
            ii=int(np.argmin(abs(self.edges-self.deep_r)))
            changed_mean=coupling*lib.sum(self.width[:ii,None]*self.gw*lib.reshape(w-self.w,self.r.shape)[:ii])
            deep_height=self.deep_base_height+changed_mean+lib.dot(self.deep_B,c[0])+self.deep_Bend*end
            deep_height=deep_height+lib.dot(lib.dot(c[1:],self.deep_B),self.C.T)
            result['deep_height']=deep_height
        if self.args.actual_curvature_weight>0 or lib is np:
            hpp=self.base_hpp+lib.dot(radial,self.Cpp.T)
            hrr=self.base_hrr+(coupling*(wr-self.wr)+lib.dot(self.B[2],c[0])+self.Bend[2]*end)[:,None]+lib.dot(lib.dot(self.B[2],lib.transpose(c[1:])),self.C.T)
            Sr=-2*hp*hrp/(r*rho)**2+2*hp*hp/(r**3*rho*rho)
            Dr=2*w[:,None]*wr[:,None]*S+E[:,None]*Sr-2*hr*hrr
            Sfr=lib.where(lib.real(S)>self.args.branch_floor,Sr,0)
            Dfr=lib.where(lib.real(D)>self.args.branch_floor,Dr,0)
            qr=rho*lib.sqrt(Sf)+r*rho*Sfr/(2*lib.sqrt(Sf))
            ar=a*(Dfr/Df-Sfr/Sf)/2;br=-(hrr*hp+hr*hrp)/q+hr*hp*qr/(q*q)
            Vrr=(br+a*A)[:,:,None]*tt+(ar-b*A)[:,:,None]*nn+self.correct_Frr
            xp2=drows(xp);vrp=drows(Vr)
            Frr=lib.concatenate((Vrr,hrr[:,:,None]),axis=2)
            Fr=lib.concatenate((Vr,hr[:,:,None]),axis=2);Fp=lib.concatenate((xp,hp[:,:,None]),axis=2)
            Frp=lib.concatenate((vrp,hrp[:,:,None]),axis=2);Fpp=lib.concatenate((xp2,hpp[:,:,None]),axis=2)
            cross=lib.cross(Fr,Fp);norm=lib.sqrt(lib.maximum(lib.sum(cross*cross,axis=2),1e-20));unit=cross/norm[:,:,None]
            ee=lib.sum(Frr*unit,axis=2);ff=lib.sum(Frp*unit,axis=2);gg=lib.sum(Fpp*unit,axis=2)
            ga=lib.sum(Fr*Fr,axis=2);gm=lib.sum(Fr*Fp,axis=2);gc=lib.sum(Fp*Fp,axis=2)
            perp=lib.maximum(gc-gm*gm/ga,1e-20);s11=ee/ga
            s12=(ff-gm/ga*ee)/lib.sqrt(ga*perp);s22=(gg-2*gm/ga*ff+(gm/ga)**2*ee)/perp
            actual_curvature=(lib.sqrt((s11+s22)**2+1e-24)+lib.sqrt((s11-s22)**2+4*s12*s12+1e-24))/2
            result['actual_curvature']=actual_curvature
            if lib is np:
                ww=(coupling*(w-self.w)).reshape(self.r.shape);dw=self.width*np.einsum('q,cq->c',self.gw,ww)
                prefix=np.r_[0,np.cumsum(dw)[:-1]]
                primitive=(prefix[:,None]+self.width[:,None]*(ww@self.gI.T)).ravel()
                H=self.base_H+(primitive+self.B[0]@c[0]+self.Bend[0]*end)[:,None]+radial@self.C.T
                result.update(F=np.concatenate((xy,H[:,:,None]),axis=2),Fr=Fr,Frr=Frr,Fphi=Fp,Frphi=Frp,Fphiphi=Fpp,
                              alpha=alpha,xy_end=xe,alpha_end=ae,hrr=hrr,
                              xy_nodes=self.xy0+np.concatenate((np.zeros_like(dx[:1]),np.cumsum(dx,axis=0)),axis=0),
                              alpha_nodes=self.alpha0+np.concatenate((np.zeros_like(da[:1]),np.cumsum(da,axis=0)),axis=0))
        return result

    def ad_residual(self,x):
        z=self.graph(x,anp);N=np.sqrt(self.N);rq=np.sqrt((self.width[:,None]*self.gw/self.L).ravel())
        blocks=[anp.ravel(z[k]*self.wquad) for k in ('er','gr','fr')]
        blocks.extend((anp.ravel(self.args.end_weight*z['turn_end']/self.rho/N),
                       anp.ravel(self.args.end_weight*z['T_end']/(self.r1*self.rho[:,None])/N),
                       anp.ravel(self.args.end_weight*z['circle_end']/self.r1/N)))
        blocks.append(anp.ravel(self.args.branch_weight*anp.maximum(self.args.branch_margin-z['D'],0)*self.wquad))
        blocks.append(self.args.curvature_weight*anp.maximum(z['reference_curvature']-self.args.curvature_limit,0)*rq)
        if self.args.actual_curvature_weight>0:
            blocks.append(anp.ravel(self.args.actual_curvature_weight*anp.maximum(z['actual_curvature']-self.args.actual_curvature_limit,0)*self.wquad))
        H=self.h0mean[0]+z['height_increment']
        blocks.append(anp.array([self.args.height_weight*anp.maximum(H-self.args.height_limit,0)]))
        if getattr(self.args,'cap_length_weight',0)>0:
            i=int(np.argmin(abs(self.edges-self.deep_r)))
            deep=self.xy0+anp.sum(z['radial_increment'][:i],axis=0)
            radial_need=self.r1-anp.sqrt(anp.sum(deep*deep,axis=1))
            needed=anp.sqrt(radial_need**2+(H-z['deep_height'])**2)
            ww=anp.reshape(z['w'],self.r.shape)[i:]
            available=anp.sum(self.width[i:,None]*self.gw*anp.sqrt(1+ww*ww))
            blocks.append(self.args.cap_length_weight*anp.maximum(needed-available,0)/self.cap_width/N)
            whole_need=anp.sqrt((self.r1-anp.sqrt(anp.sum(self.xy0*self.xy0,axis=1)))**2+(H-self.cut_height)**2)
            whole_available=anp.sum(self.width[:,None]*self.gw*anp.sqrt(1+anp.reshape(z['w'],self.r.shape)**2))
            blocks.append(self.args.cap_length_weight*anp.maximum(whole_need-whole_available,0)/self.L/N)
        return anp.concatenate(blocks)

    def reconstruct(self,x):return self.graph(x,np)

    def objective(self,x):
        value,grad=self._vg(x);self.calls+=1
        if value<self.best:
            self.best=float(value);z=self.reconstruct(x);self.last_info=self.diagnostics(z)
            self.last_info['sampled_reference_curvature']=float(np.max(z['reference_curvature']))
            self.last_info['sampled_actual_curvature']=float(np.max(z['actual_curvature']))
            self.save_design(x,float(value),False)
            if self.calls==1 or self.calls%self.args.log_every==0:
                print(json.dumps(dict(event='improved',call=self.calls,cost=float(value),gradient_max=float(np.max(abs(grad))),
                                      seconds=time.perf_counter()-self.started,**self.last_info)),flush=True)
        return value,grad

    def save_design(self,x,cost,finished,optimizer=None):
        report=dict(scope=__doc__,source_sha256=self.source_sha,base_source_sha256=self.base_source_sha,
                    trace_sha256=hashlib.sha256(self.trace_raw).hexdigest(),background_sha256=self.bg.sha256,
                    parameters={k:str(v) if isinstance(v,Path) else v for k,v in vars(self.args).items()},
                    modes=self.M,angles=self.N,variables=self.n,height_variables=self.nheight,metric_variables=self.ng,
                    panels=self.nc,gauss=len(self.gx),r0=self.r0,r1=self.r1,coefficients=np.asarray(x).tolist(),
                    homotopy=getattr(self,'homotopy',None),diagnostics=self.last_info,cost=cost,finished=finished,
                    optimizer=optimizer,seconds=time.perf_counter()-self.started,closed_surface=False,reach_certificate=False)
        self.args.out.write_text(json.dumps(report,indent=2)+'\n')

def load_coefficients(old,q):
    x=np.zeros(q.n);v=np.array(old['coefficients']);om=old['modes'];p=old['parameters']
    if abs(old['r0']-q.r0)>1e-12 or abs(old['r1']-q.r1)>1e-12:raise ValueError('Height warm projection requires the same radial interval')
    ki=np.array(json.loads(p['height_knots']));ki=np.unique(ki[(ki>0)&(ki<q.L)])
    t=np.r_[np.repeat(0.,4),ki,np.repeat(q.L,4)];nb=len(t)-4;nf=nb-6
    oh=old.get('height_variables',(om+1)*nf+1);h=v[:oh]
    co=np.zeros((nb,om+1));co[3:nb-3]=h[:-1].reshape(om+1,nf).T;co[-3:,0]=h[-1]
    oldangle=q.phi if p.get('angular_basis','material')=='physical' else q.theta
    oldC=np.column_stack((np.ones(q.N),np.cos(oldangle[:,None]*(2*np.arange(1,om+1)))))
    newC=np.column_stack((np.ones(q.N),q.C));change=np.linalg.lstsq(newC,oldC,rcond=1e-13)[0]
    co=co@change.T*p.get('coefficient_scale',.1)/q.height_scale
    sp=BSpline(t,co,3);newinner=np.unique(q.spline.t[4:-4])
    for knot in newinner:
        if not np.any(np.isclose(ki,knot,rtol=0,atol=1e-14)):sp=sp.insert_knot(float(knot))
    if len(sp.t)==len(q.spline.t) and np.allclose(sp.t,q.spline.t,rtol=0,atol=1e-14):newco=sp.c
    else:
        sample=np.unique(np.r_[q.x,np.linspace(0,q.L,4*len(q.spline.c))])
        newco=np.linalg.lstsq(q.spline(sample),sp(sample),rcond=1e-13)[0]
    x[:q.nheight-1]=newco[q.free].T.ravel();x[q.nheight-1]=newco[-1,0]
    oldmetric=v[oh:]
    if len(oldmetric) and q.ng:
        mi=np.array(json.loads(p.get('metric_knots',p['height_knots'])));mi=np.unique(mi[(mi>0)&(mi<q.L)])
        mt=np.r_[np.repeat(0.,4),mi,np.repeat(q.L,4)];mc=np.zeros(len(mt)-4);mc[3:3+len(oldmetric)]=oldmetric
        target=BSpline(mt,mc,3)(q.x);x[q.nheight:]=np.linalg.lstsq(q.MB[0],target,rcond=1e-13)[0]
    return x

def main(args):
    q=Design(args);x=np.zeros(q.n)
    if args.input:
        old=json.loads(args.input.read_text());x=load_coefficients(old,q)
        oldlam=old['parameters'].get('amplitude',1.)
        if args.rescale_input and oldlam>0 and args.amplitude!=oldlam:
            x[:q.nheight]*=args.amplitude/oldlam
    elif args.amplitude>0:
        # Feasibility initialization acts only on the height part with fixed g.
        old_n,old_ng=q.n,q.ng;q.n=q.nheight;q.ng=0
        x[:q.nheight]=base.DirectHeight.positive_mean_start(q,x[:q.nheight])
        q.n=old_n;q.ng=old_ng
    if hasattr(q,'prepare_initial'):x=q.prepare_initial(x)
    value,grad=q.objective(x)
    if args.max_nfev==0:return
    if args.method in ('lbfgs','armijo'):
        scale=np.ones(q.n)
        if not args.no_diagonal_scale and args.scaling=='norm':
            directional=make_jvp(q.ad_residual)(x)
            for j in range(q.n):
                e=np.zeros(q.n);e[j]=1.;column=directional(e)[1]
                scale[j]=min(1e3,1/max(float(np.linalg.norm(column)),1e-12))
            print(json.dumps(dict(event='column-scaling',minimum=float(scale.min()),maximum=float(scale.max()))),flush=True)
        elif not args.no_diagonal_scale and args.scaling=='heuristic':
            weight=(q.width[:,None]*q.gw/q.L).ravel()
            curvature_scale=max(0.,args.actual_curvature_weight)
            for j,m in enumerate(np.r_[0,q.freq]):
                norm=q.height_scale*np.sqrt(np.sum(weight[:,None]*(q.B[1]**2+(1+m*m)**2*q.B[0]**2+curvature_scale**2*q.B[2]**2),axis=0))
                scale[j*q.nf:(j+1)*q.nf]=1/np.maximum(norm,1e-3)
            scale[q.nheight-1]=1/max(q.height_scale*np.sqrt(np.sum(weight*(q.Bend[1]**2+curvature_scale**2*q.Bend[2]**2))),1e-3)
            scale[q.nheight:]=min(300.,10/max(np.sqrt(args.amplitude),.01))
        def scaled(v):
            value,gradient=q.objective(v*scale);return value,gradient*scale
        bounds=[(None,None)]*q.nheight+[(x[j]/scale[j],x[j]/scale[j]) if args.freeze_metric else (-args.metric_bound/scale[j],args.metric_bound/scale[j]) for j in range(q.nheight,q.n)]
        if args.method=='lbfgs':
            sol=minimize(scaled,x/scale,jac=True,method='L-BFGS-B',bounds=bounds,
                         options={'maxiter':args.max_nfev,'maxfun':4*args.max_nfev,'maxls':30,'ftol':args.function_tolerance,'gtol':args.tolerance,'maxcor':30})
            final=sol.x*scale;status=dict(success=bool(sol.success),message=str(sol.message),nfev=sol.nfev,nit=sol.nit,variable_scale=scale.tolist())
        else:
            # Fixed-ratio backtracking avoids interpolation through a huge
            # invalid-geometry trial causing a spurious zero-step convergence.
            v=x/scale;value,g=scaled(v);memory=[];evaluations=1;success=False;message='Iteration limit reached'
            lower=np.array([-np.inf if a is None else a for a,b in bounds]);upper=np.array([np.inf if b is None else b for a,b in bounds])
            for iteration in range(args.max_nfev):
                projected=g.copy();projected[(v<=lower)&(g>0)]=0.;projected[(v>=upper)&(g<0)]=0.
                if np.max(abs(projected))<args.tolerance:
                    success=True;message='Projected gradient tolerance reached';break
                direction=projected.copy();weights=[]
                for ss,yy,rr in reversed(memory):
                    aa=rr*np.dot(ss,direction);weights.append(aa);direction-=aa*yy
                if memory:
                    ss,yy,_=memory[-1];direction*=max(1e-12,min(1e8,np.dot(ss,yy)/np.dot(yy,yy)))
                for (ss,yy,rr),aa in zip(memory,reversed(weights)):
                    direction+=ss*(aa-rr*np.dot(yy,direction))
                direction=-direction
                if np.dot(direction,projected)>=0:direction=-projected;memory=[]
                direction/=max(1.,float(np.linalg.norm(direction)))
                step=1.;accepted=False
                for backtracks in range(45):
                    candidate=np.clip(v+step*direction,lower,upper);delta=candidate-v
                    if np.max(abs(delta))==0:break
                    new_value,new_gradient=scaled(candidate);evaluations+=1
                    if np.isfinite(new_value) and np.all(np.isfinite(new_gradient)) and new_value<=value+1e-4*np.dot(g,delta):
                        accepted=True;break
                    step*=.5
                if not accepted:message='Armijo backtracking stalled';break
                ss=candidate-v;yy=new_gradient-g;sy=np.dot(ss,yy)
                if sy>1e-12*np.linalg.norm(ss)*np.linalg.norm(yy):
                    memory.append((ss,yy,1/sy));memory=memory[-25:]
                v,value,g=candidate,new_value,new_gradient
                if iteration%20==0:
                    print(json.dumps(dict(event='armijo-step',iteration=iteration+1,cost=float(value),step=step,backtracks=backtracks,gradient_max=float(abs(g).max()))),flush=True)
            final=v*scale;status=dict(success=success,message=message,nfev=evaluations,nit=iteration+1,variable_scale=scale.tolist())
    else:
        def fun(v):return np.asarray(q.ad_residual(v))
        def jac(v):
            vjp,res=make_vjp(q.ad_residual)(v);jvp=make_jvp(q.ad_residual)(v)
            return LinearOperator((len(res),q.n),matvec=lambda d:jvp(np.asarray(d).ravel())[1],
                                  rmatvec=lambda d:vjp(np.asarray(d).ravel()),dtype=float)
        sol=least_squares(fun,x,jac=jac,method='trf',tr_solver='lsmr',x_scale=args.operator_scale,
                          max_nfev=args.max_nfev,ftol=args.tolerance,xtol=args.tolerance,gtol=args.tolerance,
                          tr_options={'atol':1e-5,'btol':1e-5,'maxiter':args.linear_iterations})
        final=sol.x;status=dict(success=bool(sol.success),message=str(sol.message),nfev=sol.nfev,njev=sol.njev)
    z=q.reconstruct(final);q.last_info=q.diagnostics(z);q.last_info['sampled_reference_curvature']=float(z['reference_curvature'].max());q.last_info['sampled_actual_curvature']=float(z['actual_curvature'].max())
    cost=float(np.sum(np.asarray(q.ad_residual(final))**2)/2);q.save_design(final,cost,True,status)
    printed_status={k:v for k,v in status.items() if k!='variable_scale'}
    print(json.dumps(dict(event='done',cost=cost,seconds=time.perf_counter()-q.started,optimizer=printed_status,**q.last_info)),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--trace',type=Path,required=True);p.add_argument('--background',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--input',type=Path);p.add_argument('--rescale-input',action='store_true')
    p.add_argument('--modes',type=int,default=8);p.add_argument('--angles',type=int,default=512)
    p.add_argument('--gauss',type=int,default=4);p.add_argument('--metric-stride',type=int,default=64);p.add_argument('--panel-refinement',type=int,default=1)
    p.add_argument('--height-knots',default='[0.005,0.015,0.04,0.08,0.15,0.25,0.4]')
    p.add_argument('--metric-knots',default='[0.005,0.015,0.04,0.08,0.15,0.25,0.4]');p.add_argument('--angular-basis',choices=['physical','material'],default='physical')
    p.add_argument('--decay-length',type=float,default=.08);p.add_argument('--coefficient-scale',type=float,default=.1)
    p.add_argument('--join-width',type=float,default=.01);p.add_argument('--branch-floor',type=float,default=1e-4)
    p.add_argument('--branch-margin',type=float,default=1e-3);p.add_argument('--branch-weight',type=float,default=100.)
    p.add_argument('--curvature-limit',type=float,default=6.8);p.add_argument('--curvature-weight',type=float,default=10.)
    p.add_argument('--height-limit',type=float,default=1.21);p.add_argument('--height-weight',type=float,default=10.)
    p.add_argument('--actual-curvature-weight',type=float,default=0.);p.add_argument('--actual-curvature-limit',type=float,default=6.8)
    p.add_argument('--amplitude',type=float,default=1.);p.add_argument('--metric-modes',type=int,default=5);p.add_argument('--metric-bound',type=float,default=4.)
    p.add_argument('--end-weight',type=float,default=1.);p.add_argument('--max-nfev',type=int,default=300)
    p.add_argument('--tolerance',type=float,default=1e-9);p.add_argument('--log-every',type=int,default=10)
    p.add_argument('--method',choices=['lbfgs','gauss-newton'],default='lbfgs');p.add_argument('--operator-scale',type=float,default=.1)
    p.add_argument('--linear-iterations',type=int,default=40);p.add_argument('--no-positive-start',action='store_true')
    p.add_argument('--no-diagonal-scale',action='store_true')
    p.add_argument('--freeze-metric',action='store_true');p.add_argument('--scaling',choices=['norm','heuristic'],default='norm')
    main(p.parse_args())
