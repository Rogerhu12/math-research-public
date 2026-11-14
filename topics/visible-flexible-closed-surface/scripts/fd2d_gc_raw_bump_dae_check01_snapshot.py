#!/usr/bin/env python3
"""Raw independent n,m,l GC equations with physical radial bump designs.

The base candidate's T and physical domain are fixed. Parameters are
[central c(K), positive tail b(K+1), radial delta(J)]. The original raw
equations remain unchanged in meaning and are rectangular when J!=1.
All Jacobian columns here are analytic; no finite T difference is used.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import sparse
from fd2d_gc_raw_lifted_dae import RawLiftedDAE,step5
from fd2d_gc_radial_bump_profile import (RadialBumpProfile,rational,
    tail_lifting_profile_jacobian)


def positive_profile_linear_domain(profile,base_lower_bound,radius_floor=0.):
    """Conservative continuous a>floor domain as explicit linear inequalities.

    Caller supplies a proved base lower bound B. On a support interval the
    condition B+sum(min(delta_j,0))>=floor is equivalent to requiring
    sum(delta_j,j in S)>=floor-B for every subset S of its active supports.
    Empty S is omitted after checking B>floor. Endpoint zero jets are exact.
    """
    base,floor=rational(base_lower_bound),rational(radius_floor)
    if not base>floor:
        raise ValueError('A strict base margin is required')
    knots=np.unique(np.r_[0.,profile.end,profile.supports.ravel()]);subsets=set()
    for left,right in zip(knots[:-1],knots[1:]):
        mid=(left+right)/2
        active=tuple(np.flatnonzero((profile.supports[:,0]<mid)&(mid<profile.supports[:,1])))
        for size in range(1,len(active)+1):
            subsets.update(combinations(active,size))
    subsets=sorted(subsets);matrix=np.zeros((len(subsets),profile.parameter_count))
    for i,subset in enumerate(subsets):
        matrix[i,list(subset)]=1.
    return dict(matrix=matrix,lower=np.full(len(subsets),float(floor-base)),
        subsets=[list(q) for q in subsets],base_lower_fraction=str(base),
        radius_floor_fraction=str(floor),lower_fraction=str(floor-base),
        scope='Sufficient continuous positive-metric domain conditional on the supplied base bound')


class RawBumpDAE(RawLiftedDAE):
    def __init__(self,source,*,modes=15,max_step=.04,gap=.9,profile_count=7,
                 supports=None,collar_guard=.02,base_kind='balanced_seed',
                 blend=(.58,1.4),include_support_knots=True,
                 base_lower_bound=None,base_lower_provenance=None,radius_floor=.1):
        # The old constructor creates only basis tables. At its reference T
        # the positive clock is exactly physical s, so this is the same grid
        # and fixed angular chart before optional support-knot subdivision.
        super().__init__(source,modes=modes,max_step=max_step,gap=gap,blend=blend,
            base_kind=base_kind,profile_kind='positive_clock',tail_kind='positive_bernstein')
        self.base_reference_T=self.profile.reference_T
        self.profile=RadialBumpProfile(source,count=profile_count,supports=supports,
            collar_guard=collar_guard)
        self.J=self.profile.parameter_count
        self.central_slice=slice(0,self.K)
        self.tail_slice=slice(self.K,2*self.K+1)
        self.profile_slice=slice(2*self.K+1,2*self.K+1+self.J)
        self.tail_parameter_slice=self.tail_slice
        self.profile_parameter_slice=self.profile_slice
        self.fixed_base_T=self.base_reference_T
        self.parameter_count=2*self.K+1+self.J
        if include_support_knots:
            self.x=np.unique(np.r_[self.x,self.profile.supports.ravel()])
        self.N=len(self.x);self.h=np.diff(self.x)
        self.size=self.N*self.q+self.parameter_count
        self.residual_size=self.N*self.q+2*self.K+2
        self.profile_kind='physical_bumps'
        self.chart.candidate=self.profile
        self.coords={k:np.asarray(v,float) for k,v in self.chart.coordinates(self.x).items()}
        self._operator_cache={}
        self.base_lower_bound=base_lower_bound
        self.base_lower_provenance=base_lower_provenance
        if base_lower_bound is not None and not base_lower_provenance:
            raise ValueError('Identify the proof packet for the supplied base radius lower bound')
        self.profile_domain=(None if base_lower_bound is None else
            positive_profile_linear_domain(self.profile,base_lower_bound,radius_floor))

    def parameter_layout(self):
        return dict(central=[self.central_slice.start,self.central_slice.stop],
            tail=[self.tail_slice.start,self.tail_slice.stop],
            physical_profile=[self.profile_slice.start,self.profile_slice.stop],
            base_coast_T_fixed=self.base_reference_T,parameter_count=self.parameter_count,
            raw_unknowns=self.size,raw_equations=self.residual_size,
            unknowns_minus_equations=self.size-self.residual_size,
            physical_profile_definition=self.profile.definition())

    def impose_linear_boundary_values(self,vector):
        z=np.array(vector,float,copy=True);y,p=self.unpack(z)
        y[0]=0.;y[-1]=0.;y[0,:self.e]=self.core_coefficients@p[self.central_slice]
        return z

    def parameter_domain(self,vector,central_curvature_maximum=None,central_curvature_minimum=0.):
        _,p=self.unpack(vector)
        if not np.all(np.isfinite(p)):
            return False
        tail=p[self.tail_slice]
        if np.min(tail)<0. or np.max(tail)>1.2:
            return False
        if central_curvature_maximum is not None:
            n=self.seed+self.core_basis@p[self.central_slice]
            if n.min()<central_curvature_minimum or n.min()<=0. or n.max()>central_curvature_maximum:
                return False
        delta=p[self.profile_slice]
        if self.profile_domain is not None:
            dom=self.profile_domain
            if np.any(dom['matrix']@delta<dom['lower']):
                return False
        try:
            self.operators(delta)
        except (FloatingPointError,ValueError):
            return False
        return True

    def operators(self,delta):
        delta=np.asarray(delta,float)
        if delta.shape!=(self.J,):
            raise ValueError('Expected the explicit physical profile vector')
        if not np.array_equal(self.profile.coefficients,delta):
            self.profile.set_parameters(delta)
        key=delta.tobytes()
        if key in self._operator_cache:
            return self._operator_cache[key]
        jet=self.profile.jet(self.x);a,c=jet['a'],jet['c']
        inv=1/(self.coords['u_xi']*a)
        adv=self.coords['advection'];op=np.zeros((self.N,self.d,self.q))
        for j in range(self.N):
            op[j,:self.e,:self.e]=self.PE@(adv[:,j,None]*self.Ex)-c[j]*np.eye(self.e)
            op[j,:self.e,self.e:self.d]=self.PE@(inv[:,j,None]*self.Ox)
            op[j,:self.e,self.d:]=c[j]*np.eye(self.e)
            op[j,self.e:,self.e:self.d]=self.PO@(adv[:,j,None]*self.Ox)-2*c[j]*np.eye(self.K)
            op[j,self.e:,self.d:]=self.PO@(inv[:,j,None]*self.Ex)
        result=dict(jet=jet,op=op,inv=inv,adv=adv)
        if len(self._operator_cache)>=4:
            self._operator_cache.pop(next(iter(self._operator_cache)))
        self._operator_cache[key]=result
        return result

    def lifting(self,delta,tail_parameters):
        # Parent lifting needs only self.operators and fixed weights/chart.
        # Its argument name T has no further role in those exact formulas.
        out=super().lifting(delta,tail_parameters)
        w,wq=step5((self.x-.42*self.profile.end)/(.58*self.profile.end))
        ws=wq/(.58*self.profile.end)
        extra=tail_lifting_profile_jacobian(self.operators(delta)['jet'],self.coords,
            out['tail'],w,ws)
        out['profile_parameters']=extra['values']
        out['profile_s_parameters']=extra['s']
        out['profile_x_parameters']=extra['s']
        out['profile_xi_parameters']=extra['xi']
        return out

    def evaluate(self,vector,*,jacobian=False):
        vector=np.asarray(vector,float)
        if vector.shape!=(self.size,):
            raise ValueError('Wrong full raw-bump vector dimension')
        y,p=self.unpack(vector);c=p[self.central_slice];b=p[self.tail_slice];delta=p[self.profile_slice]
        ops=self.operators(delta);lift=self.lifting(delta,b)
        fields=np.stack((self.E@y[:,:self.e].T,self.O@y[:,self.e:self.d].T,
            self.E@y[:,self.d:].T),axis=-1)+lift['values']
        n,m,l=(fields[:,:,j] for j in range(3))
        f=np.einsum('ndq,nq->nd',ops['op'],y)+lift['forcing']
        cod=(y[1:,:self.d]-y[:-1,:self.d])/self.h[:,None]-.5*(f[1:]+f[:-1])
        full_gauss=n*l-m*m-ops['jet']['K'][None,:]
        gauss=(self.PE@full_gauss[:,:-1]).T
        _,axes=self.core(c)
        left=y[0,:self.d].copy();left[:self.e]-=self.core_coefficients@c
        residual=np.r_[cod.ravel(),gauss.ravel(),y[-1,self.d:],left,y[-1,:self.d],
            (float(axes['gap'])-self.gap)/self.gap]
        if len(residual)!=self.residual_size:
            raise ArithmeticError('Wrong original equation count')
        all_parameters=np.zeros(fields.shape+(self.parameter_count,))
        all_parameters[:,:,:,self.tail_slice]=lift['parameters']
        all_parameters[:,:,:,self.profile_slice]=lift['profile_parameters']
        data=dict(fields=fields,fields_parameters=all_parameters,
            fields_parameter_scope='Raw node coefficients independent; compose exact central boundary map separately',
            full_gauss=full_gauss,codazzi_cells=cod,
            projected_gauss=gauss,axes=axes,lift=lift,parameters=p,
            physical_profile_parameters=delta.copy(),profile_jet=ops['jet'])
        if not jacobian:
            return residual,data
        rr=[];cc=[];vv=[]
        def block(row,col,values):
            values=np.atleast_2d(np.asarray(values,float));ii,jj=np.nonzero(values)
            rr.append(ii+row);cc.append(jj+col);vv.append(values[ii,jj])
        offset=self.N*self.q;jet=ops['jet'];a=jet['a']
        dx=np.stack((self.Ex@y[:,:self.e].T,self.Ox@y[:,self.e:self.d].T,
            self.Ex@y[:,self.d:].T),axis=-1)+lift['xi']
        gp=lift['profile_parameters'];gpx=lift['profile_xi_parameters'];gps=lift['profile_s_parameters']
        inv=ops['inv'][...,None];adv=ops['adv'][...,None]
        invp=-jet['a_parameters'][None,:,:]/(self.coords['u_xi'][...,None]*a[None,:,None]**2)
        cp=jet['c_parameters'][None,:,:];cv=jet['c'][None,:,None]
        fpn=invp*dx[:,:,1,None]+inv*gpx[:,:,1,:]+cp*(l-n)[...,None]+cv*(gp[:,:,2,:]-gp[:,:,0,:])+adv*gpx[:,:,0,:]-gps[:,:,0,:]
        fpm=invp*dx[:,:,2,None]+inv*gpx[:,:,2,:]-2*cp*m[...,None]-2*cv*gp[:,:,1,:]+adv*gpx[:,:,1,:]-gps[:,:,1,:]
        fp=np.concatenate((np.einsum('ew,wnp->nep',self.PE,fpn),
                           np.einsum('kw,wnp->nkp',self.PO,fpm)),axis=1)
        gaussp=l[...,None]*gp[:,:,0,:]+n[...,None]*gp[:,:,2,:]-2*m[...,None]*gp[:,:,1,:]-jet['K_parameters'][None,:,:]
        for j in range(self.N-1):
            row=j*self.d
            block(row,j*self.q,-self.select/self.h[j]-.5*ops['op'][j])
            block(row,(j+1)*self.q,self.select/self.h[j]-.5*ops['op'][j+1])
            block(row,offset+self.tail_slice.start,-.5*(lift['forcing_parameters'][j]+lift['forcing_parameters'][j+1]))
            block(row,offset+self.profile_slice.start,-.5*(fp[j]+fp[j+1]))
        row0=(self.N-1)*self.d;tailp=lift['parameters']
        for j in range(self.N-1):
            row=row0+j*self.e
            state=np.concatenate((self.PE@(l[:,j,None]*self.E),
                self.PE@(-2*m[:,j,None]*self.O),self.PE@(n[:,j,None]*self.E)),axis=1)
            block(row,j*self.q,state)
            bcol=l[:,j,None]*tailp[:,j,0,:]+n[:,j,None]*tailp[:,j,2,:]-2*m[:,j,None]*tailp[:,j,1,:]
            block(row,offset+self.tail_slice.start,self.PE@bcol)
            block(row,offset+self.profile_slice.start,self.PE@gaussp[:,j,:])
        row=row0+(self.N-1)*self.e
        block(row,(self.N-1)*self.q+self.d,np.eye(self.e));row+=self.e
        block(row,0,self.select)
        core=np.zeros((self.d,self.K));core[:self.e]=-self.core_coefficients
        block(row,offset+self.central_slice.start,core);row+=self.d
        block(row,(self.N-1)*self.q,self.select);row+=self.d
        block(row,offset+self.central_slice.start,np.asarray(axes['gap_jacobian'],float)[None,:]/self.gap)
        matrix=sparse.coo_matrix((np.concatenate(vv),(np.concatenate(rr),np.concatenate(cc))),
            shape=(self.residual_size,self.size)).tocsc()
        matrix.eliminate_zeros()
        return residual,matrix,data

    def warm_from_standard(self,mesh,corrections,parameters,*,candidate_sha256=None):
        """Same angular corrections, P1 evaluation on a subdivided physical grid.

        Old parameters must be [central,tail,T] for this same candidate.
        The added physical delta is zero. No new nonlinear solve is claimed.
        """
        mesh=np.asarray(mesh,float);y=np.asarray(corrections,float);p=np.asarray(parameters,float)
        if y.shape!=(len(mesh),self.q) or p.shape!=(2*self.K+2,):
            raise ValueError('Warm input must use the same Fourier order and old parameter layout')
        if candidate_sha256 is not None and str(candidate_sha256)!=self.profile.source_identity['sha256']:
            raise ValueError('Warm input belongs to another physical candidate')
        if abs(p[-1]-self.base_reference_T)>2e-14:
            raise ValueError('Warm physical T does not equal this candidate T')
        if mesh[0]!=self.x[0] or abs(mesh[-1]-self.x[-1])>2e-14 or np.any(np.diff(mesh)<=0):
            raise ValueError('Wrong physical warm domain')
        yy=np.column_stack([np.interp(self.x,mesh,y[:,j]) for j in range(self.q)])
        pp=np.r_[p[:2*self.K+1],np.zeros(self.J)]
        return self.impose_linear_boundary_values(np.r_[yy.ravel(),pp])

    def diagnostics(self,vector,data=None):
        residual,current=self.evaluate(vector)
        if data is None:
            data=current
        fields,p=data['fields'],data['parameters'];n,m,l=(fields[:,:,j] for j in range(3))
        radius=np.hypot(l-n,2*m);axes=data['axes']
        return dict(residual_maximum=float(np.max(abs(residual))),
            residual_rms=float(np.linalg.norm(residual)/np.sqrt(len(residual))),
            full_gauss_node_maximum=float(np.max(abs(data['full_gauss']))),
            formal_curvature_node_maximum=float(np.max(np.maximum(abs(l+n+radius),abs(l+n-radius)))/2),
            A=float(axes['A']),B=float(axes['B']),gap=float(axes['gap']),
            base_coast_T_fixed=self.base_reference_T,
            tail_coefficients=p[self.tail_slice].tolist(),profile_deltas=p[self.profile_slice].tolist(),
            minimum_n=float(n.min()),maximum_n=float(n.max()),
            minimum_central_curvature=float((self.seed+self.core_basis@p[self.central_slice]).min()),
            minimum_radius_at_nodes=float(data['profile_jet']['a'].min()),
            exact_cut_lifting=True,cut_n_mean_omitted=False,
            cut_correction_maximum=float(np.max(abs(self.unpack(vector)[0][-1]))),
            nonlinear_finite_solution=False,continuous_certificate=False)
