#!/usr/bin/env python3
"""Exact closed same-g curvature family in ONE fixed balanced-seed chart.

psi_j(phi)=cos(2*j*phi)-mu_j, with mu_j defined by the exact material-weighted
integral. Tight dyadic certificates bound the numerical representatives of
all moments and means. base_kind='balanced_seed' retains the old d meaning;
base_kind='circle' includes the exact radius-a0 circle at d=0. Both use the
same physical metric and the same fixed u(phi)=arc_seed(phi)/a0.

Finite Gauss quadrature evaluates the exact integral definition. This module
does not certify its point-evaluation error or a complete strong surface.
"""
from __future__ import annotations
import os
for _thread_variable in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_thread_variable]='1'
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import numpy as np
from fd2d_metric_curvature_core import LD,PI,PERIOD,HALF_PI,EPS,gauss_rule,exact_rational,to_ld,SupportSeed

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
DEFAULT_MOMENTS=ROOT/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json'
DEFAULT_MEANS=ROOT/'notes/2026-11-12-fd2d-balanced-weighted-means-01.json'


def identity(path):
    path=Path(path)
    return dict(file=str(path.resolve()),bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def dyadic(parts):
    sign,mantissa,exponent,bits=map(int,parts)
    if sign not in (0,1) or mantissa<0:raise ValueError('Invalid exact dyadic endpoint')
    q=Fraction((-1 if sign else 1)*mantissa)
    return q*(2**exponent) if exponent>=0 else q/Fraction(2**(-exponent))


def interval_pair(row):
    lo,hi=dyadic(row['binary_lower']),dyadic(row['binary_upper'])
    if lo>hi:raise ValueError('Reversed exact interval')
    return lo,hi


def representative(pair):
    lo,hi=pair;value=to_ld((lo+hi)/2);q=exact_rational(value)
    error=max(abs(q-lo),abs(q-hi))
    return value,error


def upper_float(q):
    value=float(q)
    return float(np.nextafter(value,np.inf)) if Fraction(value)<q else value


class QuarterPrimitive:
    """Finite numerical primitive on [0,pi/2], batched to bound memory."""
    def __init__(self,function,panels=64,order=24):
        self.function=function;self.panels=int(panels);self.order=int(order)
        self.gx,self.gw=gauss_rule(self.order)
        self.width=HALF_PI/self.panels
        self.edges=np.linspace(LD(0),HALF_PI,self.panels+1,dtype=LD)
        self.nodes=self.edges[:-1,None]+self.width*self.gx
        raw=np.asarray(function(self.nodes.ravel()),dtype=LD)
        if raw.ndim==1:raw=raw[:,None]
        self.components=raw.shape[-1]
        self.node_values=raw.reshape(self.panels,self.order,self.components)
        values=self.width*np.sum(self.node_values*self.gw[None,:,None],axis=1,dtype=LD)
        self.cumulative=np.concatenate((np.zeros((1,self.components),dtype=LD),np.cumsum(values,axis=0,dtype=LD)))

    def at(self,q):
        q=np.asarray(q,dtype=LD);shape=q.shape;flat=q.ravel()
        if np.any(flat<0) or np.any(flat>HALF_PI):raise ValueError('Quarter primitive outside its interval')
        out=np.empty((len(flat),self.components),dtype=LD)
        for first in range(0,len(flat),128):
            x=flat[first:first+128]
            ids=np.clip(np.floor(x/self.width).astype(int),0,self.panels-1)
            width=x-self.edges[ids]
            nodes=self.edges[ids,None]+width[:,None]*self.gx
            values=np.asarray(self.function(nodes.ravel()),dtype=LD).reshape(len(x),self.order,self.components)
            out[first:first+len(x)]=self.cumulative[ids]+width[:,None]*np.sum(values*self.gw[None,:,None],axis=1,dtype=LD)
        return out.reshape(shape+(self.components,))


class FixedBalancedGeometry:
    """Numerical representative of the EXACT moment-defined fixed seed."""
    def __init__(self,moments=DEFAULT_MOMENTS,means=DEFAULT_MEANS,*,panels=64,order=24):
        self.moments_path,self.means_path=Path(moments),Path(means)
        self.moments=json.loads(self.moments_path.read_text());self.means=json.loads(self.means_path.read_text())
        if self.means['exact_moment_report']['sha256']!=identity(self.moments_path)['sha256']:
            raise ValueError('Weighted means bind a different exact moment report')
        if self.means['parameters']!=self.moments['parameters']:
            raise ValueError('Mean and moment packets define different seeds')
        if not self.means['source_moment_intervals_remain_valid']:
            raise ValueError('The input does not assert valid source moment intervals')
        self.parameters=self.moments['parameters']
        self.r,self.D,self.c,self.k,self.A,self.B=[to_ld(self.parameters[key]) for key in ('r','D','c','k','A','B')]
        self.intervals={key:interval_pair(self.moments['enclosures'][key]) for key in ('a0','u0','u2','u4')}
        self.numeric_errors={key:abs(exact_rational(getattr(self,key))-exact_rational(self.parameters[key]))
                             for key in ('r','D','c','k','A','B')}
        for key,pair in self.intervals.items():
            value,error=representative(pair);setattr(self,key,value);self.numeric_errors[key]=error
        self.mu_intervals=[interval_pair(row['material_weighted_mean']) for row in self.means['rows']]
        if [row['angular_mode'] for row in self.means['rows']]!=list(range(2,2*len(self.mu_intervals)+1,2)):
            raise ValueError('The certified mean modes are not consecutive even modes')
        mu=[representative(pair) for pair in self.mu_intervals]
        self.mu=np.array([p[0] for p in mu],dtype=LD);self.mu_numeric_errors=[p[1] for p in mu]
        self.panels,self.order=int(panels),int(order)
        self._primitive=QuarterPrimitive(self._moment_integrand,self.panels,self.order)
        self._original_ellipse=None
        self._basis_cache={};self._axis_cache={}

    def radius(self,phi):
        phi=np.asarray(phi,dtype=LD)
        th=np.tanh(self.k*(np.cos(2*phi)-self.c))
        return self.r+self.D*(1-th)/2+self.u0+self.u2*np.cos(2*phi)+self.u4*np.cos(4*phi)

    def radius_derivative(self,phi):
        phi=np.asarray(phi,dtype=LD)
        th=np.tanh(self.k*(np.cos(2*phi)-self.c))
        return self.D*self.k*np.sin(2*phi)*(1-th*th)-2*self.u2*np.sin(2*phi)-4*self.u4*np.sin(4*phi)

    def _moment_integrand(self,phi):
        rho=self.radius(phi)
        return np.stack((rho,rho*np.sin(phi),rho*np.cos(phi)),axis=-1)

    @staticmethod
    def reduce(phi):
        phi=np.asarray(phi,dtype=LD);wrapped=np.mod(phi,PERIOD)
        quadrant=np.clip(np.floor(wrapped/HALF_PI).astype(int),0,3)
        local=wrapped-quadrant*HALF_PI
        q=np.where(quadrant%2,HALF_PI-local,local)
        sx=np.where((quadrant==0)|(quadrant==3),LD(1),LD(-1))
        sy=np.where(quadrant<2,LD(1),LD(-1))
        return np.clip(q,0,HALF_PI),quadrant,sx,sy

    def material_coordinate(self,phi):
        phi=np.asarray(phi,dtype=LD);q,quadrant,sx,sy=self.reduce(phi)
        integral=self._primitive.at(q)[...,0]
        integral=np.where(q==0,LD(0),np.where(q==HALF_PI,self.a0*HALF_PI,integral))
        quarter=self.a0*HALF_PI
        arc=np.select((quadrant==0,quadrant==1,quadrant==2),
                      (integral,2*quarter-integral,2*quarter+integral),4*quarter-integral)
        u=np.floor(phi/PERIOD)*PERIOD+arc/self.a0
        return dict(u=u,u_phi=self.radius(phi)/self.a0,u_phi_phi=self.radius_derivative(phi)/self.a0)

    def normal_angle(self,u):
        u=np.asarray(u,dtype=LD);q,quadrant,sx,sy=self.reduce(u);target=self.a0*q
        arc=self._primitive.cumulative[:,0].copy();arc[-1]=self.a0*HALF_PI
        j=np.clip(np.searchsorted(arc,target,side='right')-1,0,self.panels-1)
        lo,hi=self._primitive.edges[j].copy(),self._primitive.edges[j+1].copy()
        phi=lo+(hi-lo)*(target-arc[j])/(arc[j+1]-arc[j])
        ends=(q==0)|(q==HALF_PI)
        for iteration in range(40):
            residual=self._primitive.at(phi)[...,0]-target
            residual=np.where(ends,LD(0),residual)
            done=abs(residual)<=48*EPS*np.maximum(LD(1),abs(target))
            if np.all(done):break
            lo=np.where((residual<0)&~done,phi,lo);hi=np.where((residual>0)&~done,phi,hi)
            trial=phi-residual/self.radius(phi)
            bad=(trial<=lo)|(trial>=hi)|~np.isfinite(trial)
            phi=np.where(done,phi,np.where(bad,(lo+hi)/2,trial))
        phi=np.where(q==0,LD(0),np.where(q==HALF_PI,HALF_PI,phi))
        residual=self._primitive.at(phi)[...,0]-target
        residual=np.where(ends,LD(0),residual)
        if np.max(abs(residual),initial=LD(0))>512*EPS*np.maximum(LD(1),np.max(abs(target),initial=LD(0))):
            raise ArithmeticError('Fixed balanced material-angle inversion did not converge')
        small=phi
        wrapped=np.select((quadrant==0,quadrant==1,quadrant==2),
                          (small,PI-small,PI+small),PERIOD-small)
        return np.floor(u/PERIOD)*PERIOD+wrapped

    def seed_position(self,phi):
        q,quadrant,sx,sy=self.reduce(phi);integrals=self._primitive.at(q)
        Is,Ic=integrals[...,1],integrals[...,2]
        Is=np.where(q==HALF_PI,self.A,Is);Ic=np.where(q==HALF_PI,self.B,Ic)
        return np.stack((sx*(self.A-Is),sy*Ic,np.zeros_like(q)),axis=-1)

    def original_eccentric_coordinate(self,theta):
        if self._original_ellipse is None:self._original_ellipse=SupportSeed()
        return self._original_ellipse.reference_coordinate(theta)


class BalancedCurvatureCore:
    """A closed central family with exact weighted means and a fixed chart."""
    def __init__(self,coefficients=(),*,base_kind='balanced_seed',geometry=None,panels=None,order=None):
        if base_kind not in ('balanced_seed','circle'):raise ValueError('Unknown exact central base')
        self.base_kind=base_kind
        self.geometry=(FixedBalancedGeometry(panels=64 if panels is None else panels,order=24 if order is None else order)
                       if geometry is None else geometry)
        self.a0=self.geometry.a0;self.exact_coefficients=tuple(exact_rational(x) for x in coefficients)
        self.d=np.array([to_ld(x) for x in self.exact_coefficients],dtype=LD);self.J=len(self.d)
        if self.J>len(self.geometry.mu):raise ValueError('More curvature modes than certified weighted means')
        self.mu=self.geometry.mu[:self.J];self.modes=2*np.arange(1,self.J+1,dtype=LD)
        self.panels=int(self.geometry.panels if panels is None else panels)
        self.order=int(self.geometry.order if order is None else order)
        key=(self.J,self.panels,self.order)
        if self.J and key not in self.geometry._basis_cache:
            geom,modes,mu=self.geometry,self.modes.copy(),self.mu.copy()
            def integrand(phi):
                return geom.radius(phi)[:,None]*(np.cos(phi[:,None]*modes)-mu)
            self.geometry._basis_cache[key]=QuarterPrimitive(integrand,self.panels,self.order)
        self._basis_primitive=self.geometry._basis_cache.get(key)
        self._position_primitive=None

    def _basis_integrand(self,phi):
        phi=np.asarray(phi,dtype=LD)
        return self.geometry.radius(phi)[:,None]*(np.cos(phi[:,None]*self.modes)-self.mu)

    def curvature(self,phi):
        """Fast fixed-phi n and its parameter basis; no position quadrature."""
        phi=np.asarray(phi,dtype=LD);rho=self.geometry.radius(phi)
        basis=np.cos(phi[...,None]*self.modes)-self.mu
        n0=1/rho if self.base_kind=='balanced_seed' else np.full_like(phi,1/self.a0)
        derivative=(-self.geometry.radius_derivative(phi)/rho**2 if self.base_kind=='balanced_seed' else np.zeros_like(phi))
        derivative-=np.sin(phi[...,None]*self.modes)@(self.modes*self.d)
        return dict(n=n0+basis@self.d,n_phi=derivative,parameter_basis=basis,rho_seed=rho)

    def turn_basis(self,phi):
        phi=np.asarray(phi,dtype=LD)
        if not self.J:return np.empty(phi.shape+(0,),dtype=LD)
        q,quadrant,sx,sy=self.geometry.reduce(phi)
        value=self._basis_primitive.at(q)
        # Each exact weighted mean makes its quarter integral exactly zero.
        value=np.where(((q==0)|(q==HALF_PI))[...,None],LD(0),value)
        return value*np.where(quadrant%2,LD(-1),LD(1))[...,None]

    def _frame(self,phi):
        phi=np.asarray(phi,dtype=LD);rho=self.geometry.radius(phi);rhop=self.geometry.radius_derivative(phi)
        coordinate=self.geometry.material_coordinate(phi)
        base_turn=phi if self.base_kind=='balanced_seed' else coordinate['u']
        T0=np.stack((-np.sin(base_turn),np.cos(base_turn),np.zeros_like(phi)),axis=-1)
        N0=np.stack((-np.cos(base_turn),-np.sin(base_turn),np.zeros_like(phi)),axis=-1)
        Q=self.turn_basis(phi);delta=Q@self.d
        sd,cd=np.sin(delta),np.cos(delta)
        T=cd[...,None]*T0+sd[...,None]*N0;N=cd[...,None]*N0-sd[...,None]*T0
        basis=np.cos(phi[...,None]*self.modes)-self.mu
        n0=1/rho if self.base_kind=='balanced_seed' else np.full_like(phi,1/self.a0)
        n=n0+basis@self.d
        nphi=(-rhop/rho**2 if self.base_kind=='balanced_seed' else np.zeros_like(phi))-np.sin(phi[...,None]*self.modes)@(self.modes*self.d)
        difference=(-2*np.sin(delta/2)**2)[...,None]*T0+sd[...,None]*N0
        return dict(rho=rho,rhop=rhop,T=T,N=N,n=n,n_phi=nphi,turn_basis=Q,
                    curvature_basis=basis,delta_turn=delta,difference=difference,coordinate=coordinate)

    def _position_integrand(self,phi):
        f=self._frame(phi)
        return f['rho'][:,None]*f['difference']

    def _base_position(self,phi):
        if self.base_kind=='balanced_seed':return self.geometry.seed_position(phi)
        u=self.geometry.material_coordinate(phi)['u']
        return self.a0*np.stack((np.cos(u),np.sin(u),np.zeros_like(u)),axis=-1)

    @staticmethod
    def gc_columns(data):
        return np.concatenate((data['n'][...,None],data['m'][...,None],data['X'],data['e1'],data['e2'],data['N']),axis=-1)

    def evaluate_normal_angle(self,phi):
        phi=np.asarray(phi,dtype=LD);f=self._frame(phi);X=self._base_position(phi)
        if np.any(self.d!=0):
            if self._position_primitive is None:self._position_primitive=QuarterPrimitive(self._position_integrand,self.panels,self.order)
            q,quadrant,sx,sy=self.geometry.reduce(phi);I=self._position_primitive.at(q)
            correction=np.stack((sx*(I[...,0]-self._position_primitive.cumulative[-1,0]),sy*I[...,1],np.zeros_like(q)),axis=-1)
            X=X+correction
        zero=np.zeros_like(X);e1=zero.copy();e1[...,2]=1
        rho,rhop=f['rho'],f['rhop'];n=f['n'];T,N=f['T'],f['N']
        out=dict(X=X,X_u=self.a0*T,X_uu=self.a0**2*n[...,None]*N,
            X_phi=rho[...,None]*T,X_phi_phi=rhop[...,None]*T+(rho*rho*n)[...,None]*N,
            X_s=e1,X_ss=zero.copy(),X_su=zero.copy(),X_s_phi=zero.copy(),
            e1=e1,e2=T,N=N,n=n,m=np.zeros_like(phi),l=np.zeros_like(phi),
            n_phi=f['n_phi'],n_u=f['n_phi']*self.a0/rho,phi=phi,**f['coordinate'])
        out['coordinate']='phi: fixed seed normal angle; u: fixed physical material angle; X_u/X_uu always material derivatives'
        out['gc_values']=self.gc_columns(out)
        return out

    def evaluate_material(self,u):
        return self.evaluate_normal_angle(self.geometry.normal_angle(u))

    def evaluate_reference_angle(self,theta):
        coordinate=self.geometry.original_eccentric_coordinate(theta)
        out=self.evaluate_material(coordinate['u'])
        first,second=coordinate['u_theta'],coordinate['u_theta_theta']
        out.update(theta=np.asarray(theta,dtype=LD),u_theta=first,u_theta_theta=second,
            X_theta=out['X_u']*first[...,None],
            X_theta_theta=out['X_uu']*first[...,None]**2+out['X_u']*second[...,None])
        return out

    def jvp_normal_angle(self,phi,direction):
        phi=np.asarray(phi,dtype=LD);v=np.asarray(direction,dtype=LD)
        if v.shape!=self.d.shape:raise ValueError('Wrong curvature direction dimension')
        f=self._frame(phi);Qv=f['turn_basis']@v;dn=f['curvature_basis']@v
        dT=f['N']*Qv[...,None];dN=-f['T']*Qv[...,None]
        def integrand(x):
            frame=self._frame(x);turn=frame['turn_basis']@v
            return frame['rho'][:,None]*frame['N']*turn[:,None]
        primitive=QuarterPrimitive(integrand,self.panels,self.order)
        q,quadrant,sx,sy=self.geometry.reduce(phi);I=primitive.at(q)
        X=np.stack((sx*(I[...,0]-primitive.cumulative[-1,0]),sy*I[...,1],np.zeros_like(q)),axis=-1)
        rho,rhop,n=f['rho'],f['rhop'],f['n'];zero=np.zeros_like(X)
        dcurvature_vector=dn[...,None]*f['N']+n[...,None]*dN
        out=dict(X=X,X_u=self.a0*dT,X_uu=self.a0**2*dcurvature_vector,
            X_phi=rho[...,None]*dT,X_phi_phi=rhop[...,None]*dT+rho[...,None]**2*dcurvature_vector,
            X_s=zero.copy(),X_ss=zero.copy(),X_su=zero.copy(),X_s_phi=zero.copy(),
            e1=zero.copy(),e2=dT,N=dN,n=dn,m=np.zeros_like(phi),l=np.zeros_like(phi),
            n_phi=-np.sin(phi[...,None]*self.modes)@(self.modes*v))
        out['n_u']=out['n_phi']*self.a0/rho
        out['gc_values']=self.gc_columns(out)
        return out

    def jvp_material(self,u,direction):
        """Parameter JVP at fixed physical u; the seed chart is parameter independent."""
        return self.jvp_normal_angle(self.geometry.normal_angle(u),direction)

    def jvp_reference_angle(self,theta,direction):
        """Parameter JVP at the common original ellipse's fixed eccentric angle."""
        coordinate=self.geometry.original_eccentric_coordinate(theta)
        out=self.jvp_material(coordinate['u'],direction)
        first,second=coordinate['u_theta'],coordinate['u_theta_theta']
        out.update(X_theta=out['X_u']*first[...,None],
            X_theta_theta=out['X_uu']*first[...,None]**2+out['X_u']*second[...,None])
        return out

    def axis_intercepts_and_jacobian(self):
        # D2 makes the half-period center exactly (integral_x,0,0).
        # Static basis primitives are cached across all d; a BVP boundary call
        # then requires only two matrix products and pointwise trig in delta.
        key=(self.J,self.panels,self.order,self.base_kind)
        if key not in self.geometry._axis_cache:
            gx,gw=gauss_rule(self.order);width=HALF_PI/self.panels
            edges=np.linspace(LD(0),HALF_PI,self.panels+1,dtype=LD)
            x=(edges[:-1,None]+width*gx).ravel()
            weights=(width*np.broadcast_to(gw,(self.panels,self.order))).ravel()
            rho=self.geometry.radius(x);Q=self.turn_basis(x)
            turn=x if self.base_kind=='balanced_seed' else self.geometry.material_coordinate(x)['u']
            T0=np.stack((-np.sin(turn),np.cos(turn)),axis=-1)
            N0=np.stack((-np.cos(turn),-np.sin(turn)),axis=-1)
            self.geometry._axis_cache[key]=(weights*rho,Q,T0,N0)
        factor,Q,T0,N0=self.geometry._axis_cache[key]
        delta=Q@self.d;sd,cd=np.sin(delta),np.cos(delta)
        difference=(-2*np.sin(delta/2)**2)[:,None]*T0+sd[:,None]*N0
        N=cd[:,None]*N0-sd[:,None]*T0
        A0=self.geometry.A if self.base_kind=='balanced_seed' else self.a0
        B0=self.geometry.B if self.base_kind=='balanced_seed' else self.a0
        A=A0-factor@difference[:,0];B=B0+factor@difference[:,1]
        JA=-(factor*N[:,0])@Q
        JB=(factor*N[:,1])@Q
        return dict(A=A,B=B,gap=A-B,A_jacobian=JA,B_jacobian=JB,gap_jacobian=JA-JB,
                    interpretation='axis intercepts; they equal axis supports if the actual curve is convex')

    def definition(self):
        weighted=sum((abs(d)*(1+max(abs(lo),abs(hi))) for d,(lo,hi) in
                      zip(self.exact_coefficients,self.geometry.mu_intervals)),Fraction())
        lower=(Fraction(100,317) if self.base_kind=='balanced_seed' else Fraction(1,1)/self.geometry.intervals['a0'][1])-weighted
        upper=(Fraction(250,57) if self.base_kind=='balanced_seed' else Fraction(1,1)/self.geometry.intervals['a0'][0])+weighted
        mean_error=sum((abs(d)*error for d,error in zip(self.exact_coefficients,self.geometry.mu_numeric_errors)),Fraction())
        return dict(schema='fd2d-balanced-fixed-normal-curvature-central-definition-v1',base_kind=self.base_kind,
            source=identity(__file__),exact_moments=identity(self.geometry.moments_path),exact_weighted_means=identity(self.geometry.means_path),
            parameters=self.geometry.parameters,coefficients_exact=[str(x) for x in self.exact_coefficients],
            curvature_definition=('1/rho_seed(phi)' if self.base_kind=='balanced_seed' else '1/a0')+'+sum d_j*(cos(2*j*phi)-exact_mu_j)',
            material_map='u(phi)=integral_0^phi rho_seed/a0; same fixed map for every d and both base kinds',
            exact_mean_definition='mu_j=(1/(2*pi*a0))*integral_0^(2*pi)rho_seed(phi)*cos(2*j*phi)dphi',
            exact_position_definition='gamma_base + integral_0^phi rho_seed*(T_d-T_base) - (1/2)*integral_0^pi rho_seed*(T_d-T_base)',
            exact_closed_D2_curve=True,exact_central_metric='ds^2+a0^2*du^2',
            conservative_curvature_lower_exact=str(lower),conservative_curvature_upper_exact=str(upper),
            global_convexity_proved_by_l1_bound=bool(lower>0),
            numerical_constant_error_upper={key:upper_float(error) for key,error in self.geometry.numeric_errors.items()},
            numerical_mean_error_upper=[upper_float(error) for error in self.geometry.mu_numeric_errors[:self.J]],
            curvature_constant_error_from_mean_representatives_upper_exact=str(mean_error),
            raw_quarter_turn_basis_integral_numerical_defect=([float(x) for x in self._basis_primitive.cumulative[-1]] if self.J else []),
            quadrature_panels=self.panels,quadrature_order=self.order,
            point_evaluation_is_interval_certified=False,whole_BVP_solved=False,closed_surface=False)
