#!/usr/bin/env python3
"""Direct C2 height design, differentiated through literal radial geometry.

The input is a true accepted-prefix node, including its common 0/1/2 jets.
The scalar metric is frozen.  Finite height B-splines are optimized against
the actual Cartesian Gram entries and a round outer circle.  No P/K, L, or
positive-height-slope chart is imposed.  S,D positivity is checked separately.
Quadrature, angular sampling, and the finite outer axisymmetric condition all
require independent refinement; a successful optimizer is not an exact tail.
"""
from __future__ import annotations
import argparse,hashlib,json,sys,time
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import least_squares,linprog

SCRIPTS=Path(__file__).resolve().parents[1]/'scripts'
sys.path.insert(0,str(SCRIPTS))
from parallel_20261117_dynamic_tail import Background
from parallel_20261117_frenet_symbol import Frenet

def derivative(value,axis=-1):
    n=value.shape[axis];mult=1j*np.fft.fftfreq(n,d=1/n);mult[n//2]=0
    shape=[1]*value.ndim;shape[axis]=n
    def real(v):return np.fft.ifft(np.fft.fft(v,axis=axis)*mult.reshape(shape),axis=axis).real
    if np.iscomplexobj(value):return real(value.real)+1j*real(value.imag)
    return real(value)

def gauss_integrator(order):
    z,w=np.polynomial.legendre.leggauss(order);V=np.polynomial.legendre.legvander(z,order-1)
    I=np.empty_like(V)
    for j in range(order):
        p=np.zeros(order);p[j]=1;q=np.polynomial.legendre.legint(p)
        I[:,j]=(np.polynomial.legendre.legval(z,q)-np.polynomial.legendre.legval(-1.,q))/2
    return (z+1)/2,w/2,np.linalg.solve(V.T,I.T).T

def distinct_knots(values):
    """Merge duplicate source endpoints that differ only by roundoff.

    Keeping adjacent one-ulp values as two spline knots creates an artificial
    subcell whose curvature no practical quadrature can resolve.
    """
    ordered=np.sort(np.asarray(values,dtype=float))
    if not len(ordered):return ordered
    tol=16*np.finfo(float).eps*max(1.,float(np.max(abs(ordered))))
    result=[ordered[0]]
    for value in ordered[1:]:
        if value-result[-1]>tol:result.append(value)
    return np.array(result)

def boundary_fundamentals(x,L,tau):
    x=np.asarray(x);v=1-x/L;e=np.exp(-x/tau)
    f=e*v**3;fp=-e*(v**3/tau+3*v*v/L)
    fpp=e*(v**3/tau**2+6*v*v/(tau*L)+6*v/L**2)
    f1=-1/tau-3/L;f2=f1*f1-3/L**2
    polys=[np.array([1.,-f1,f1*f1-f2/2]),np.array([0.,1.,-f1]),np.array([0.,0.,.5])]
    out=[]
    for degree in range(3):
        columns=[]
        for c in polys:
            p=c[0]+x*(c[1]+x*c[2]);dp=c[1]+2*x*c[2];ddp=2*c[2]+0*x
            columns.append(f*p if degree==0 else fp*p+f*dp if degree==1 else fpp*p+2*fp*dp+f*ddp)
        out.append(np.array(columns).T)
    return out

class DirectHeight:
    def __init__(self,args):
        self.args=args;self.source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();self.trace_raw=args.trace.read_bytes();self.trace=json.loads(self.trace_raw)
        self.bg=Background(args.background,'physical-r');self.N=args.angles;self.M=args.modes
        t=self.trace;self.r0=float(t['r']);self.r1=float(getattr(args,'end_radius',None) or self.bg.r[-1]);self.L=self.r1-self.r0
        if abs(self.bg.r[0]-self.r0)>1e-12:raise ValueError('Trace and metric left radii must coincide')
        if 'frenet_rr_state' not in t:raise ValueError('A true 2-jet node trace is required')
        q=Frenet(t['M'],self.N);self.phi=q.angle;self.freq=2*np.arange(1,self.M+1)
        rho_coeff=np.array(t['rho_cos_coefficients']);rf=2*np.arange(1,len(rho_coeff)+1)
        self.rho=1+np.cos(self.phi[:,None]*rf)@rho_coeff
        self.theta=self.phi+np.sin(self.phi[:,None]*rf)@(rho_coeff/rf)
        if self.rho.min()<=0:raise ValueError('Material angle density is not positive')
        self.C=np.cos(self.theta[:,None]*self.freq)
        self.Cp=-self.rho[:,None]*np.sin(self.theta[:,None]*self.freq)*self.freq
        states=[np.array(t[key]) for key in ('frenet_state','frenet_r_state','frenet_rr_state')]
        jets=[q.jet(s) for s in states]
        self.h0mean=np.array([s[2*t['M']+1] for s in states])
        self.hjets=np.array([z[0][:,2]-v for z,v in zip(jets,self.h0mean)])
        self.hpj=np.array([z[1][:,2] for z in jets])
        cp,sp=np.cos(self.phi),np.sin(self.phi)
        def cart(v):return np.column_stack((cp*v[:,0]-sp*v[:,1],sp*v[:,0]+cp*v[:,1]))
        self.xy0=cart(jets[0][0]);self.true_Fr0=cart(jets[1][0]);self.true_Frr0=cart(jets[2][0])
        tangent0=cart(jets[0][1]);self.alpha0=np.unwrap(np.arctan2(tangent0[:,1],tangent0[:,0]))
        # Cubic splines have common second jets at every simple interior knot.
        raw=np.array(json.loads(args.height_knots));inner=distinct_knots(raw[(raw>0)&(raw<self.L)])
        args.height_knots=json.dumps(inner.tolist())
        knots=np.r_[np.repeat(0.,4),inner,np.repeat(self.L,4)];nb=len(knots)-4
        spline=BSpline(knots,np.eye(nb),3);self.spline=spline;self.free=np.arange(3,nb-3)
        self.nf=len(self.free);self.n=(self.M+1)*self.nf+1
        # Quadrature panels use real source-segment endpoints and all height knots.
        chosen=[row['r'] for i,row in enumerate(self.bg.rows)
                if i%args.metric_stride==0 or row['x'] in (0,1)]
        edges=distinct_knots(np.r_[self.r0,chosen,self.r1,self.r0+inner])
        if args.panel_refinement>1:
            edges=np.unique(np.r_[(edges[:-1,None]+np.diff(edges)[:,None]*np.linspace(0,1,args.panel_refinement+1)).ravel(),self.r1])
        self.edges=edges;self.width=np.diff(edges);self.nc=len(self.width)
        self.gx,self.gw,self.gI=gauss_integrator(args.gauss)
        self.r=edges[:-1,None]+self.width[:,None]*self.gx;self.flat_r=self.r.ravel()
        self.x=self.flat_r-self.r0
        self.w,self.wr=self.reference_metric(self.flat_r)
        self.E=1+self.w*self.w
        self.base=boundary_fundamentals(self.x,self.L,args.decay_length)
        self.B=[spline(self.x,nu)[:,self.free] for nu in range(3)]
        self.Bend=[spline(self.x,nu)[:,-3:].sum(axis=1) for nu in range(3)]
        self.delta_mean=np.array([0.,self.h0mean[1]-t['w'],self.h0mean[2]-t['w_r']])
        self.base_hr=self.w+self.base[1]@self.delta_mean
        self.base_hp=self.base[0]@self.hpj
        self.base_hrp=self.base[1]@self.hpj
        self.base_hr=self.base_hr[:,None]+self.base[1]@self.hjets
        self.height_scale=args.coefficient_scale
        self.wquad=np.sqrt((self.width[:,None]*self.gw/self.L).ravel())[:,None]/np.sqrt(self.N)
        self.join_width=min(args.join_width,self.L/4)
        self._initial_correction(jets)
        self.calls=0;self.best=float('inf');self.started=time.perf_counter();self.last_info=None

    def reference_metric(self,r):
        w=np.exp(self.bg.spline(r));return w,w*self.bg.spline(r,1)

    def _initial_correction(self,jets):
        t=self.trace;r=self.r0;rho=self.rho;hp=self.hpj[0];hr=jets[1][0][:,2];hrr=jets[2][0][:,2];hrp=self.hpj[1]
        w=t['w'];wr=t['w_r'];E=1+w*w;S=1-(hp/(r*rho))**2;D=E*S-hr*hr
        if min(S.min(),D.min())<=0:raise ValueError('The true cut lacks the positive projection branch')
        q=r*rho*np.sqrt(S);qr=(r*rho*rho-hp*hrp)/q
        a=np.sqrt(D/S);b=-hr*hp/q
        Sr=-2*hp*hrp/(r*rho)**2+2*hp*hp/(r**3*rho*rho)
        Dr=2*w*wr*S+E*Sr-2*hr*hrr
        ar=a*(Dr/D-Sr/S)/2;br=-(hrr*hp+hr*hrp)/q+hr*hp*qr/(q*q)
        A=hr*(hrp-hp/r)/(r*rho*S*np.sqrt(D))
        tt=np.column_stack((np.cos(self.alpha0),np.sin(self.alpha0)))
        nn=np.column_stack((np.sin(self.alpha0),-np.cos(self.alpha0)))
        V=b[:,None]*tt+a[:,None]*nn
        Vr=(br+a*A)[:,None]*tt+(ar-b*A)[:,None]*nn
        self.constructed_Fr0=V;self.constructed_Frr0=Vr
        self.delta_Fr=self.true_Fr0-V;self.delta_Frr=self.true_Frr0-Vr
        u=np.clip(self.x/self.join_width,0,1);mask=self.x<self.join_width
        chi=(1-10*u**3+15*u**4-6*u**5)*mask
        chip=(-30*u*u+60*u**3-30*u**4)/self.join_width*mask
        self.correct_xy=(self.x*chi)[:,None,None]*self.delta_Fr+.5*(self.x*self.x*chi)[:,None,None]*self.delta_Frr
        self.correct_Fr=(chi+self.x*chip)[:,None,None]*self.delta_Fr+(self.x*chi+.5*self.x*self.x*chip)[:,None,None]*self.delta_Frr

    def fields(self,x):
        c=x[:-1].reshape(self.M+1,self.nf)*self.height_scale;end=x[-1]*self.height_scale
        radial=self.B[0]@c[1:].T;radial_r=self.B[1]@c[1:].T
        hp=self.base_hp+radial@self.Cp.T
        hr=self.base_hr+(self.B[1]@c[0]+self.Bend[1]*end)[:,None]+radial_r@self.C.T
        hrp=self.base_hrp+radial_r@self.Cp.T
        return hp,hr,hrp,end

    def positive_mean_start(self,x):
        """A linear feasibility solve for mean-slope positivity, not a PDE solve."""
        hp,hr,_,_=self.fields(x);S=1-(hp/(self.flat_r[:,None]*self.rho))**2
        bound=np.sqrt(np.maximum(self.E[:,None]*S-.01,1e-10))
        mean=np.mean(hr,axis=1);perp=hr-mean[:,None]
        hi=np.min(bound-perp,axis=1)-mean;lo=np.max(-bound-perp,axis=1)-mean
        A=self.height_scale*np.column_stack((self.B[1],self.Bend[1]));k=A.shape[1]
        blocks=np.block([[A,np.zeros_like(A)],[-A,np.zeros_like(A)],
                         [np.eye(k),-np.eye(k)],[-np.eye(k),-np.eye(k)]])
        b=np.r_[hi,-lo,np.zeros(2*k)]
        sol=linprog(np.r_[np.zeros(k),np.ones(k)],A_ub=blocks,b_ub=b,
                    bounds=[(None,None)]*k+[(0,None)]*k,method='highs')
        if sol.success:
            x=x.copy();x[:self.nf]+=sol.x[:self.nf];x[-1]+=sol.x[self.nf]
        print(json.dumps(dict(event='positive-mean-initializer',success=bool(sol.success),message=sol.message,
                              minimum_D=float(self.reconstruct(x)['D'].min()))),flush=True)
        return x

    def reconstruct(self,x):
        hp,hr,hrp,endheight=self.fields(x);r=self.flat_r[:,None];rho=self.rho[None,:]
        S=1-(hp/(r*rho))**2;D=self.E[:,None]*S-hr*hr
        Sf=np.where(S.real>self.args.branch_floor,S,self.args.branch_floor+0*S)
        Df=np.where(D.real>self.args.branch_floor,D,self.args.branch_floor+0*D)
        root=np.sqrt(Df);a=np.sqrt(Df/Sf);q=r*rho*np.sqrt(Sf);b=-hr*hp/q
        A=hr*(hrp-hp/r)/(r*rho*Sf*root)
        shape=(self.nc,len(self.gx),self.N)
        AA=A.reshape(shape);delta_alpha=self.width[:,None]*np.einsum('q,cqn->cn',self.gw,AA)
        before=np.concatenate((np.zeros_like(delta_alpha[:1]),np.cumsum(delta_alpha,axis=0)[:-1]),axis=0)
        alpha=self.alpha0+before[:,None,:]+self.width[:,None,None]*np.einsum('ij,cjn->cin',self.gI,AA)
        alpha=alpha.reshape((-1,self.N))
        tt=np.stack((np.cos(alpha),np.sin(alpha)),axis=-1);nn=np.stack((np.sin(alpha),-np.cos(alpha)),axis=-1)
        V=b[:,:,None]*tt+a[:,:,None]*nn;VV=V.reshape((*shape,2))
        delta_xy=self.width[:,None,None]*np.einsum('q,cqnk->cnk',self.gw,VV)
        before_xy=np.concatenate((np.zeros_like(delta_xy[:1]),np.cumsum(delta_xy,axis=0)[:-1]),axis=0)
        xy=self.xy0+before_xy[:,None,:,:]+self.width[:,None,None,None]*np.einsum('ij,cjnk->cink',self.gI,VV)
        xy=xy.reshape((-1,self.N,2))+self.correct_xy
        Vr=V+self.correct_Fr;xp=derivative(xy,axis=1)
        er=(np.sum(Vr*Vr,axis=2)+hr*hr)/self.E[:,None]-1
        gr=(np.sum(xp*xp,axis=2)+hp*hp)/(r*rho)**2-1
        fr=(np.sum(Vr*xp,axis=2)+hr*hp)/(np.sqrt(self.E)[:,None]*r*rho)
        alpha_end=self.alpha0+np.sum(delta_alpha,axis=0);xy_end=self.xy0+np.sum(delta_xy,axis=0)
        tangent_end=np.stack((np.cos(alpha_end),np.sin(alpha_end)),axis=-1)
        normal_end=np.stack((np.sin(alpha_end),-np.cos(alpha_end)),axis=-1)
        alpha_phi_end=1+derivative(alpha_end-self.phi)
        T_end=derivative(xy_end,axis=0)-self.r1*self.rho[:,None]*tangent_end
        circle_end=xy_end-self.r1*normal_end
        return dict(er=er,gr=gr,fr=fr,S=S,D=D,alpha_end=alpha_end,xy_end=xy_end,
                    turn_end=alpha_phi_end-self.rho,T_end=T_end,circle_end=circle_end,
                    height_increment=float(np.sum(self.width[:,None]*self.gw*self.w.reshape(self.r.shape)))+endheight,
                    hr=hr,hp=hp)

    def residual(self,x,record=True):
        z=self.reconstruct(x)
        out=np.concatenate(tuple((z[key]*self.wquad).ravel() for key in ('er','gr','fr'))+
                           ((self.args.end_weight*z['turn_end']/self.rho/np.sqrt(self.N)).ravel(),
                            (self.args.end_weight*z['T_end']/(self.r1*self.rho[:,None])/np.sqrt(self.N)).ravel(),
                            (self.args.end_weight*z['circle_end']/self.r1/np.sqrt(self.N)).ravel()))
        if record and not np.iscomplexobj(x):
            self.calls+=1;cost=float(np.dot(out,out)/2)
            if cost<self.best:
                self.best=cost;self.last_info=self.diagnostics(z)
                if self.args.out:self.save(x,cost,False)
                if self.calls==1 or self.calls%self.args.log_every==0:
                    print(json.dumps(dict(event='improved',call=self.calls,cost=cost,seconds=time.perf_counter()-self.started,**self.last_info)),flush=True)
        return out

    def jacobian(self,x):
        base=self.residual(x,record=False);J=np.empty((len(base),self.n));h=1e-25
        for j in range(self.n):
            xx=x.astype(complex);xx[j]+=1j*h;J[:,j]=self.residual(xx,record=False).imag/h
        return J

    def diagnostics(self,z):
        er,gr,fr=(z[k].real for k in ('er','gr','fr'))
        op=(abs(er+gr)+np.sqrt((er-gr)**2+4*fr*fr))/2
        return dict(sampled_gram=float(np.max(op)),minimum_S=float(z['S'].real.min()),minimum_D=float(z['D'].real.min()),
                    endpoint_turn=float(np.max(abs(z['turn_end'].real))),endpoint_T=float(np.max(abs(z['T_end'].real))),
                    endpoint_circle=float(np.max(abs(z['circle_end'].real))),
                    terminal_mean_height=float(self.h0mean[0]+z['height_increment'].real),
                    max_height_radial_derivative=float(np.max(abs(z['hr'].real))))

    def save(self,x,cost,finished,solver=None):
        report=dict(scope=__doc__,trace_sha256=hashlib.sha256(self.trace_raw).hexdigest(),background_sha256=self.bg.sha256,
                    source_sha256=self.source_sha,parameters={k:str(v) if isinstance(v,Path) else v for k,v in vars(self.args).items()},
                    modes=self.M,angles=self.N,variables=self.n,panels=self.nc,gauss=len(self.gx),r0=self.r0,r1=self.r1,
                    initial_Fr_correction=float(np.max(abs(self.delta_Fr))),initial_Frr_correction=float(np.max(abs(self.delta_Frr))),
                    coefficients=np.asarray(x).real.tolist(),cost=cost,diagnostics=self.last_info,finished=finished,
                    optimizer=solver,seconds=time.perf_counter()-self.started,closed_surface=False,reach_certificate=False)
        self.args.out.write_text(json.dumps(report,indent=2)+'\n')

def main(args):
    model=DirectHeight(args);x=np.zeros(model.n)
    if args.input:
        old=json.loads(args.input.read_text());oldx=np.array(old['coefficients'])
        if len(oldx)!=model.n:raise ValueError('Initial height coefficient dimensions differ')
        x=oldx
    elif not args.no_positive_start:x=model.positive_mean_start(x)
    r=model.residual(x);print(json.dumps(dict(event='initial',variables=model.n,panels=model.nc,residuals=len(r),**model.last_info)),flush=True)
    if args.max_nfev==0:return
    sol=least_squares(model.residual,x,jac=model.jacobian,method='trf',tr_solver='lsmr',x_scale='jac',
                      max_nfev=args.max_nfev,ftol=args.tolerance,xtol=args.tolerance,gtol=args.tolerance,
                      tr_options={'atol':1e-7,'btol':1e-7,'maxiter':200},verbose=0)
    model.last_info=model.diagnostics(model.reconstruct(sol.x));model.save(sol.x,float(sol.cost),True,
        dict(success=bool(sol.success),status=int(sol.status),message=sol.message,nfev=sol.nfev,njev=sol.njev,optimality=float(sol.optimality)))
    print(json.dumps(dict(event='done',cost=sol.cost,nfev=sol.nfev,success=bool(sol.success),seconds=time.perf_counter()-model.started,**model.last_info)),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--trace',type=Path,required=True);p.add_argument('--background',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--input',type=Path)
    p.add_argument('--modes',type=int,default=3);p.add_argument('--angles',type=int,default=512)
    p.add_argument('--gauss',type=int,default=4);p.add_argument('--metric-stride',type=int,default=64);p.add_argument('--panel-refinement',type=int,default=1)
    p.add_argument('--height-knots',default='[0.005,0.015,0.04,0.08,0.15,0.25,0.4]')
    p.add_argument('--decay-length',type=float,default=.08);p.add_argument('--coefficient-scale',type=float,default=.1)
    p.add_argument('--join-width',type=float,default=.01);p.add_argument('--branch-floor',type=float,default=1e-4)
    p.add_argument('--end-weight',type=float,default=1.);p.add_argument('--max-nfev',type=int,default=100)
    p.add_argument('--tolerance',type=float,default=1e-10);p.add_argument('--log-every',type=int,default=5)
    p.add_argument('--no-positive-start',action='store_true')
    main(p.parse_args())
