#!/usr/bin/env python3
"""True-integral interval oracle for an actual versioned warm phase core.

This reuses the already proved support-inverse Taylor and exact GL12-rule
machinery. It recomputes every bound from the frozen actual anchor and phase
controls, including lambda=1. The old small-lambda constants are not reused.
The source floating core is used for inverse seeds only. All d_j, anchor
coefficients and window inputs are interpreted as their literal rationals;
The R65 full-period and R68 complementary-arc families are distinct.
For the latter, P=2*pi/3 and omega_j=j*pi/(P/2-S) are true constants;
the provider's floating frequencies are never substituted for them.
"""
import bisect
from fractions import Fraction as Q
import importlib.util
import math
from pathlib import Path
import sys
import time
import numpy as np
import mpmath as mp


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj


def build_oracle(core,support_dir,mean_kernel,interval_kernel,*,degree=24,
                 cells_per_unit=128,progress=None):
    old=module('_warm_validated_original_inverse',Path(support_dir)/'r53_validated_material_core.py')
    fq,mpq,mplo,mphi=old.fq,old.mpq,old.mplo,old.mphi
    Parent=old.ValidatedMaterialCore

    class WarmOracle(Parent):
        def __init__(self):
            self.started=time.monotonic()
            self.warm_core=core
            self.core=baseline=core.baseline
            if core.base_mode!=3 or baseline.curvature_blend!=1.:
                raise ValueError('Use the declared threefold fixed-target R53 warm baseline')
            self.base=module('_warm_validated_mean_kernel',mean_kernel)
            self.K=module('_warm_validated_interval_kernel',interval_kernel)
            self.base.K=self.K
            self.I=self.base.I
            mp.mp.dps=90;mp.iv.dps=75
            self.a=[fq(x) for x in baseline.original.coefficients]
            self.m=[int(x) for x in baseline.original.frequencies]
            self.b=[(1-m*m)*a for m,a in zip(self.m,self.a)]
            size=sum(map(abs,self.b))
            self.rho_min,self.rho_max=1-size,1+size
            if self.rho_min<=0:
                raise ValueError('This sufficient inverse certificate requires the actual support rho l1 sum below one')
            self.lam=fq(baseline.homotopy)
            self.S,self.width,self.k=map(fq,(baseline.halfwidth,baseline.transition,baseline.k))
            if not (0<self.lam<=1 and self.S>0 and self.width>0 and self.k>0):
                raise ValueError('Invalid frozen warm target/window parameters')
            self.Tmp,self.Lmp=2*mp.iv.pi/3,mp.iv.pi/3
            self.T,self.L=self.from_mp(self.Tmp),self.from_mp(self.Lmp)
            if not float(self.rat(self.S+self.width).x[1])<float(self.L.x[0]):
                raise ValueError('The protection window does not fit the true half-sector')
            self.d=[fq(x) for x in core.controls]
            if not self.d:
                raise ValueError('At least one physical phase control is required')
            D1=Q(630,256)/self.width
            declared=getattr(core,'phase_basis_kind',None)
            if declared not in (None,'complementary_arc_sine_v1'):
                raise ValueError('No true-integral oracle for this declared phase family')
            self.phase_basis_family=declared or 'full_period_sine_v1'
            self.complementary=declared=='complementary_arc_sine_v1'
            if self.complementary:
                self.complement_Lmp=self.Lmp-mpq(self.S)
                self.complement_L=self.from_mp(self.complement_Lmp)
                if not float(self.complement_L.x[0])>float(self.rat(self.width).x[1]):
                    raise ValueError('The true complementary halfwidth must exceed the transition width')
                self.frequency_mp=[j*mp.iv.pi/self.complement_Lmp
                                   for j in range(1,len(self.d)+1)]
                self.freq=self.arr_mp(self.frequency_mp)
                self.frequency_lower=[fq(x) for x in self.freq.x[0]]
                self.frequency_upper=[fq(x) for x in self.freq.x[1]]
                self.coef=self.stack([self.rat(d) for d in self.d])/(self.freq+self.rat(D1))
                self.normalizations=None
            else:
                self.w=[3*(j+1) for j in range(len(self.d))]
                self.frequency_mp=[mpq(w) for w in self.w]
                self.freq=self.I(np.asarray(self.w,int))
                self.frequency_lower=self.frequency_upper=list(map(Q,self.w))
                self.normalizations=[1+D1/w for w in self.w]
                self.phase_coefficients=[d/n for d,n in zip(self.d,self.normalizations)]
                self.coef=self.stack([self.rat(c) for c in self.phase_coefficients])
            gap=max(abs(1/self.rho_min-self.k),abs(1/self.rho_max-self.k))
            D=self.L-self.rat(self.S+self.width/2)
            bound=self.rat((self.S+self.width/2)*gap)/D
            self.beta_abs_coarse=fq(self.K.up(bound.absolute_upper()))
            self.beta_coarse_upper=float(self.beta_abs_coarse)
            self.r=Q(1,16)
            target=(1+size)/2
            for _ in range(80):
                B=sum((mpq(abs(b))*(mp.iv.exp(m*mpq(self.r))+mp.iv.exp(-m*mpq(self.r)))/2
                       for b,m in zip(self.b,self.m)),mp.iv.mpf(0))
                upper=fq(self.K.up(float(mphi(B))))
                if upper<target:
                    break
                self.r/=2
            else:
                raise ArithmeticError('No certified positive complex support strip was resolved')
            self.strip_B=self.from_mp(B)
            self.strip_B_upper=upper
            self.R=Q(3,4)*self.r*(1-upper)
            self.position_R=self.R
            for _ in range(80):
                K=self._complex_curvature_bound(self.position_R)
                if K*self.position_R<Q(1,2):
                    self.complex_kappa_bound=K
                    break
                self.position_R/=2
            else:
                raise ArithmeticError('The position quadrature analytic radius was not resolved')
            self.degree=int(degree)
            if self.degree<8:
                raise ValueError('The inverse Taylor degree must be at least eight')
            need=max(int(cells_per_unit),math.ceil(4/min(self.R,self.position_R)),
                     math.ceil(max(self.frequency_upper)))
            self.cells_per_unit=1
            while self.cells_per_unit<need:
                self.cells_per_unit*=2
            self.h=Q(1,2*self.cells_per_unit)
            self.real_kappa_coarse=(1/self.rho_min+self.lam*(self.k+1/self.rho_min+
                                      self.beta_abs_coarse)+sum(map(abs,self.d)))
            self._inverse_taylor()
            if progress:progress(dict(stage='warm_true_inverse',seconds=time.monotonic()-self.started,
                                      cells_per_unit=self.cells_per_unit))
            self._build_omega()
            if progress:progress(dict(stage='warm_true_weighted_primitive',
                                      seconds=time.monotonic()-self.started))
            self._gauss_rule()
            self._build_position()
            self.seconds=time.monotonic()-self.started

        def _complex_curvature_bound(self,R):
            eta=Q(R)/self.width
            sigma=Q(1,4)+eta+eta*eta
            W=1+630*eta*sigma**4
            W1=630*sigma**4/self.width
            oldK=1/(1-self.strip_B_upper)
            baseline=oldK+self.lam*((1+W)*(self.k+oldK)+self.beta_abs_coarse*W)
            total=mpq(baseline)
            if self.complementary:
                D1=Q(630,256)/self.width
                for d,w in zip(self.d,self.frequency_mp):
                    total+=mpq(abs(d))*(w*mpq(W)+mpq(W1))/(w+mpq(D1))*mp.iv.exp(w*mpq(R))
            else:
                for d,w,n in zip(self.d,self.w,self.normalizations):
                    total+=mpq(abs(d)*(W+W1/w)/n)*mp.iv.exp(w*mpq(R))
            return fq(self.K.up(float(mphi(total))))

        def _build_omega(self):
            # Same already proved exact weighted-polynomial integration;
            # no old beta<3 or small-lambda assertion is transplanted.
            first=self.L+self.rat(self.S)
            last=first+self.rat(self.width)
            grid=[first,first+self.rat(self.width/2),last]
            for j in range(self.count+1):
                q=Q(j,self.cells_per_unit)
                if float(first.x[1])<float(q)<float(last.x[0]):
                    grid.append(self.rat(q))
            grid.sort(key=lambda x:float((x.x[0]+x.x[1])/2))
            if not all(float(a.x[1])<float(b.x[0]) for a,b in zip(grid[:-1],grid[1:])):
                raise ArithmeticError('Unresolved true weighted-integral partition')
            self.og=grid;self.opieces=[];self.ocumulative=[self.I(0)]
            for left,right in zip(grid[:-1],grid[1:]):
                origin,anti=self._weighted_piece(left,right)
                piece=(left,origin,anti)
                self.opieces.append(piece)
                self.ocumulative.append(self.ocumulative[-1]+self._weighted_part(piece,right))
            self.omegaS=self.rat(self.k*self.S)-(self.inverse(first)-self.L)
            self.omegaEnd=self.omegaS+self.ocumulative[-1]
            self.beta=-self.omegaEnd/(self.L-self.rat(self.S+self.width/2))

        def window_jets(self,theta):
            theta=self.I(theta)
            x=theta-self.L
            if float(x.x[1])<0:
                sign,z=-1,-x
            elif float(x.x[0])>0:
                sign,z=1,x
            else:
                sign=self.I(-1,1)
                z=self.I(0,max(-float(x.x[0]),float(x.x[1])))
            W,_=self._window_scalar(z)
            tl=(z-self.rat(self.S))/self.rat(self.width)
            lo=max(0.,float(tl.x[0]));hi=min(1.,float(tl.x[1]))
            if lo>hi:
                return W,self.I(0),self.I(0),self.I(0)
            t=self.I(lo,hi)
            a=t*(1-t)
            first=sign*630*a**4/self.rat(self.width)
            second=2520*a**3*(1-2*t)/self.rat(self.width**2)
            third=sign*(7560*a.sq()*(1-2*t).sq()-5040*a**3)/self.rat(self.width**3)
            if float(tl.x[0])<0 or float(tl.x[1])>1:
                first=self.hull(first,self.I(0));second=self.hull(second,self.I(0))
                third=self.hull(third,self.I(0))
            return W,first,second,third

        def phase_increment(self,theta):
            theta=self.I(theta)
            W,W1,W2,W3=self.window_jets(theta)
            if self.complementary:
                # v jumps at P/2, strictly inside the protected W=0 arc.
                # The interval test uses the true boundary enclosures;
                # ambiguous broad boxes are covered by both branches.
                if all(np.all(np.asarray(z.x)==0) for z in (W,W1,W2,W3)):
                    return self.I(0),self.I(0),self.I(0),self.I(0)
                if float(theta.x[1])<float(self.L.x[0]):
                    return self._complement_increment_at(theta,(W,W1,W2,W3))
                if float(theta.x[0])>float(self.L.x[1]):
                    return self._complement_increment_at(theta-self.T,(W,W1,W2,W3))
                first=self._complement_increment_at(theta,(W,W1,W2,W3))
                second=self._complement_increment_at(theta-self.T,(W,W1,W2,W3))
                return tuple(self.hull(a,b) for a,b in zip(first,second))
            sn,cs=self.sincos(self.freq*theta)
            w=self.freq;c=self.coef
            return ((c*W*sn/w).sum(),
                (c*(W*cs+W1*sn/w)).sum(),
                (c*(2*W1*cs+(W2/w-W*w)*sn)).sum(),
                (c*((3*W2-W*w.sq())*cs+(W3/w-3*W1*w)*sn)).sum())

        def _complement_increment_at(self,v,window):
            W,W1,W2,W3=window
            w,c=self.freq,self.coef
            sn,cs=self.sincos(w*v)
            return ((c*W*sn).sum(),
                (c*(w*W*cs+W1*sn)).sum(),
                (c*(2*w*W1*cs+(W2-w.sq()*W)*sn)).sum(),
                (c*((3*w*W2-w**3*W)*cs+(W3-3*w.sq()*W1)*sn)).sum())

        def phase(self,theta):
            theta=self.I(theta)
            phi,kappa=Parent.phase(self,theta)
            shape=np.shape(theta.x[0])
            flat=self.I(np.ravel(theta.x[0]),np.ravel(theta.x[1]))
            values=[self.phase_increment(flat.item(j)) for j in range(np.size(flat.x[0]))]
            def array(index):
                return self.I(np.array([float(v[index].x[0]) for v in values]).reshape(shape),
                              np.array([float(v[index].x[1]) for v in values]).reshape(shape))
            return phi+array(0),kappa+array(1)

        def curvature_jets(self,theta,known_kappa=None):
            kk,ku,kuu=Parent.curvature_jets(self,theta,None)
            _,c1,c2,c3=self.phase_increment(theta)
            return (kk+c1 if known_kappa is None else known_kappa),ku+c2,kuu+c3

        def _quad_error(self,length,maxwidth=None):
            length=Q(length);width=length if maxwidth is None else Q(maxwidth)
            analytic=length*2*self.gauss_C*(width/self.position_R)**24
            rule=(length*self.gauss_weight_l1/2+
                  self.real_kappa_coarse*length*width*self.gauss_node_gap/2)
            return analytic+rule

        def phase_l1_bounds(self):
            D1=Q(630,256)/self.width
            D2=Q(2520,64)/self.width**2
            D3=(Q(7560,16)+Q(5040,64))/self.width**3
            if self.complementary:
                # These are rational upper bounds for irrational sums,
                # not rounded values asserted equal to those sums.
                C={r:sum((abs(d)*hi**r/(lo+D1) for d,lo,hi in
                          zip(self.d,self.frequency_lower,self.frequency_upper)),Q(0))
                   for r in range(4)}
                return dict(phase=C[0],kappa=C[1]+D1*C[0],
                    kappa_u=C[2]+2*D1*C[1]+D2*C[0],
                    kappa_uu=C[3]+3*D1*C[2]+3*D2*C[1]+D3*C[0])
            A={r:sum((abs(d)*Q(w)**r/n for d,w,n in
                       zip(self.d,self.w,self.normalizations)),Q(0)) for r in (-1,0,1,2)}
            return dict(phase=A[-1],kappa=A[0]+D1*A[-1],
                kappa_u=A[1]+2*D1*A[0]+D2*A[-1],
                kappa_uu=A[2]+3*D1*A[1]+3*D2*A[0]+D3*A[-1])

        def all_angle_curvature_bounds(self,max_depth=12):
            out={key:0. for key in ('kappa','kappa_u','kappa_uu','Gamma3','Gamma4')}
            lower=math.inf;cells=0;unresolved=0
            todo=[(float(l.x[0]),float(r.x[1]),0) for l,r in zip(self.pg[:-1],self.pg[1:])]
            while todo:
                lo,hi,depth=todo.pop()
                k,ku,kuu=self.curvature_jets(self.I(lo,hi))
                if float(k.x[0])<=0 and depth<max_depth:
                    middle=(lo+hi)/2
                    todo.extend([(lo,middle,depth+1),(middle,hi,depth+1)])
                    continue
                cells+=1;lower=min(lower,float(k.x[0]))
                unresolved+=int(float(k.x[0])<=0)
                for key,value in (('kappa',k),('kappa_u',ku),('kappa_uu',kuu)):
                    out[key]=max(out[key],value.absolute_upper())
                for name,squared in (('Gamma3',ku.sq()+k**4),
                                     ('Gamma4',(k**3-kuu).sq()+9*k.sq()*ku.sq())):
                    # These exact expressions are sums of squares. Outward
                    # roundoff at zero can give a tiny negative lower bound;
                    # intersecting with their proved nonnegative range is
                    # valid and does not clip a geometric domain condition.
                    if np.any(squared.x[1]<0):
                        raise ArithmeticError('An impossible negative upper norm-square bound')
                    nonnegative=self.I(np.maximum(0.,squared.x[0]),squared.x[1])
                    out[name]=max(out[name],nonnegative.sqrt().absolute_upper())
            return dict(**out,kappa_lower=lower,positive_curvature_certified=unresolved==0,
                        unresolved_positive_curvature_cells=unresolved,covered_cells=cells)

        def metadata(self):
            value=dict(core_kind=('true-R68-complementary-phase-integral' if self.complementary
                                  else 'true-R65-supported-phase-integral'),
                phase_basis_family=self.phase_basis_family,
                anchor_support_exact=[str(v) for v in self.a],phase_controls_exact=[str(v) for v in self.d],
                true_period='2*pi/3',true_sector_halfperiod='pi/3',
                frequencies_lower_exact=[str(v) for v in self.frequency_lower],
                frequencies_upper_exact=[str(v) for v in self.frequency_upper],
                homotopy_exact=str(self.lam),S_exact=str(self.S),b_exact=str(self.width),k_exact=str(self.k),
                rho_lower_exact=str(self.rho_min),support_complex_radius_exact=str(self.r),
                support_complex_B_upper_exact=str(self.strip_B_upper),inverse_radius_exact=str(self.R),
                position_radius_exact=str(self.position_R),complex_kappa_bound_exact=str(self.complex_kappa_bound),
                beta_abs_coarse_exact=str(self.beta_abs_coarse),
                beta_interval=list(map(float,self.beta.x)),
                phase_l1_rational_upper_bounds={k:str(v) for k,v in self.phase_l1_bounds().items()},
                source_float_frequencies_not_used_as_true_constants=True,
                global_phase_basis_regular_order_at_least=4,
                global_curve_regular_order_at_least=5,
                cells_per_unit=self.cells_per_unit,inverse_degree=self.degree,
                inverse_seed_max_width=self.inverse_seed_max_width,
                source_float_inverse_used_only_as_seed=True,
                old_small_lambda_numeric_bounds_reused=False,
                old_core_or_prefix_certificate_reused=False)
            if self.complementary:
                value.update(complementary_halfwidth='pi/3-S',frequency_definition='j*pi/(pi/3-S)',
                    complementary_halfwidth_interval=list(map(float,self.complement_L.x)),
                    phase_basis='W(u)*sin(omega_j*v)/(omega_j+630/(256*b))',
                    coordinate='v=u below pi/3, v=u-2*pi/3 above; W=0 near the branch change',
                    same_finite_span_as_R65=False)
            else:
                value.update(frequency_definition='3*j',
                    normalizations_exact=[str(v) for v in self.normalizations])
            return value

    return WarmOracle()
