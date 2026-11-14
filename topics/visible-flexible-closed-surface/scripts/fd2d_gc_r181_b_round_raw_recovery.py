"""Explicit new B32 round-reference raw three-field entry: recovery source.

This uses only published R181 inputs and published local formulas. It is a
new source/schema; unavailable 87bde source bytes or runs are not claimed.
Changing physical deltas changes g. No old coast/native field is loaded.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import copy,json
import numpy as np
from scipy import sparse
from fd2d_gc_archive_arrays import identity
from fd2d_balanced_curvature_core import FixedBalancedGeometry
from fd2d_gc_raw_lifted_dae import CertifiedReference,step5,mesh_for
from fd2d_gc_blended import BlendedIntrinsicGC
from fd2d_gc_raw_bump_dae import RawBumpDAE,positive_profile_linear_domain
from fd2d_gc_radial_bump_profile import (
    RadialBumpProfile,rational,tail_lifting_profile_jacobian)
from fd2d_dyadic_bernstein_tail import (
    DyadicBernsteinControlBox,DyadicBernsteinFlatDevelopableFamily)
from fd2d_gc_r181_b_round_reference_recovery import (
    R181BRecoveryRoundReference,DEFAULT_CANDIDATE,CANDIDATE_SHA256,checked_candidate)

REPRESENTATION='fd2d-R181-B32-recovery-round-full-function-raw-P1-v1'


class ExplicitB32RadialProfile(RadialBumpProfile):
    """Same analytic R181 target; return its defining exact cut label."""
    def jet(self,s):
        out=super().jet(s);points=np.atleast_1d(np.asarray(s,float))
        at=points==self.end
        if not np.any(at):return out
        out={k:(v.copy() if isinstance(v,np.ndarray) else v) for k,v in out.items()}
        for key,value in (('a',4/5),('a_s',-1.),('a_ss',0.),('c',-5/4),('K',0.)):
            out[key][at]=value
        return out
    def definition(self):
        out=super().definition()
        out.update(explicit_endpoint_label=['4/5','-1','0'],
            endpoint_rule='s==the recorded floating end labels the accurate cut',
            scalar_interval_reader='R181BRecoveryArbProfile',
            endpoint_label_not_an_equality_of_rounded_and_accurate_lengths=True)
        return out


class R181BRecoveryRoundRawBumpDAE(RawBumpDAE):
    def __init__(self,source=DEFAULT_CANDIDATE,*,modes=7,max_step=.04,gap=.05,
                 gap_scale=.64,base_kind='circle',supports=None):
        self.source=Path(source);checked_candidate(source)
        if int(modes)!=modes or not 1<=int(modes)<=31:
            raise ValueError('This entry declares central/raw K in 1..31')
        if not 0<float(max_step)<1 or not float(gap_scale)>0 or float(gap)<0:
            raise ValueError('Positive mesh scale and fixed gap normalization required')
        if base_kind not in ('circle','balanced_seed'):
            raise ValueError('Explicit actual central base required')
        self.K=int(modes);self.e=self.K+1;self.d=2*self.K+1;self.q=3*self.K+2
        self.gap=float(gap);self.gap_scale=float(gap_scale);self.base_kind=base_kind
        self.representation_kind=REPRESENTATION
        self.profile_kind='physical_bumps'
        self.tail_kind='degree15_eight_dyadic_Bernstein_box'
        self.geometry=FixedBalancedGeometry()
        self.reference=R181BRecoveryRoundReference(source)
        self.profile=ExplicitB32RadialProfile(source,count=7,supports=supports,collar_guard=.02)
        self.J=self.profile.parameter_count
        if self.J!=7:raise ValueError('This explicitly published new entry uses seven physical bumps')
        self.tail_count=16;self.parameter_count=self.K+16+self.J
        self.central_slice=slice(0,self.K)
        self.tail_slice=slice(self.K,self.K+16)
        self.profile_slice=slice(self.K+16,self.parameter_count)
        self.tail_parameter_slice=self.tail_slice;self.profile_parameter_slice=self.profile_slice
        self.tail_class=DyadicBernsteinFlatDevelopableFamily
        self.tail_control_box=DyadicBernsteinControlBox()
        matching=[p for p in self.profile.segments if p.get('label')=='partial_return_matching_coast']
        if len(matching)!=1:raise ValueError('Explicit new matching coast missing')
        self.fixed_base_T=self.base_reference_T=float(matching[0]['L'])
        # A fixed chart of this NEW metric. No R139/ruling atlas is borrowed.
        self.blend=(3/8,4/5)
        self.chart=BlendedIntrinsicGC(self.profile,maximum_mode=2*self.K+1,
            oversample=4,reference=CertifiedReference(self.geometry),blend_interval=self.blend)
        central=float(self.profile.central_end)
        self.seed_window=(central,max(min(.55,.4*self.profile.end),central+.05*(self.profile.end-central)))
        self.tail_window=(.42*self.profile.end,self.profile.end)
        x=mesh_for(self.profile,max_step,self.blend)
        self.x=np.unique(np.r_[x,self.profile.supports.ravel(),self.seed_window,self.tail_window])
        if self.x[0]!=0. or self.x[-1]!=self.profile.end or np.any(np.diff(self.x)<=0):
            raise ValueError('New physical mesh is inconsistent')
        self.N=len(self.x);self.h=np.diff(self.x)
        self.size=self.N*self.q+self.parameter_count
        self.residual_size=self.N*self.q+2*self.K+2
        theta=np.asarray(self.chart.theta,float);self.work=len(theta)
        frequency=2*np.arange(self.K+1)
        self.E=np.cos(theta[:,None]*frequency);self.O=np.sin(theta[:,None]*frequency[1:])
        self.Ex=-np.sin(theta[:,None]*frequency)*frequency
        self.Ox=np.cos(theta[:,None]*frequency[1:])*frequency[1:]
        self.PE=2*self.E.T/self.work;self.PE[0]*=.5;self.PO=2*self.O.T/self.work
        mu=np.asarray(self.geometry.mu[:self.K],float)
        self.core_basis=self.E[:,1:]-mu
        self.core_coefficients=np.vstack((-mu,np.eye(self.K)))
        rho=np.asarray(self.geometry.radius(theta),float)
        if base_kind=='circle':
            self.seed=np.full_like(rho,1/float(self.geometry.a0));self.seed_xi=np.zeros_like(rho)
        else:
            self.seed=1/rho
            self.seed_xi=-np.asarray(self.geometry.radius_derivative(theta),float)/rho**2
        self.coords={k:np.asarray(v,float) for k,v in self.chart.coordinates(self.x).items()}
        self.select=np.zeros((self.d,self.q));self.select[:,:self.d]=np.eye(self.d)
        self._operator_cache={}
        self._last_c=self._last_core=self._last_axes=None
        self.fixed_central_nodes=np.flatnonzero(self.x<=central)
        self.additional_fixed_field_indices=np.empty(0,dtype=int)
        self.trace_gauge_pairs=np.empty((0,2),dtype=int)
        self.inactive_field_indices=np.empty(0,dtype=int)
        self.base_lower_bound=Fraction(4,5)
        self.radius_floor=Fraction(1,10)
        self.base_lower_provenance='R181 section 3 for exact candidate '+CANDIDATE_SHA256
        self.profile_domain=positive_profile_linear_domain(self.profile,self.base_lower_bound,self.radius_floor)

    def parameter_layout(self):
        return dict(central=[0,self.K],tail=[self.K,self.K+16],
            physical_profile=[self.K+16,self.parameter_count],
            central_parameter_count=self.K,tail_parameter_count=16,profile_count=self.J,
            parameter_count=self.parameter_count,raw_components=['n','m','l'],
            raw_even_modes=self.K+1,raw_odd_modes=self.K,
            unknowns=self.size,legacy_projected_equation_count=self.residual_size,
            actual_point_objective_count='declared separately; no added rows to square the system')

    def tail(self,coefficients):
        return DyadicBernsteinFlatDevelopableFamily(np.asarray(coefficients,float),
            cut_radius=.8,cuff_radius=.32,flat_radius=.34,plane_height=1.25)

    def impose_linear_boundary_values(self,vector):
        z=np.array(vector,float,copy=True)
        if z.shape!=(self.size,):raise ValueError('Wrong packed new B32 size')
        y,p=self.unpack(z)
        y[self.fixed_central_nodes]=0.
        y[self.fixed_central_nodes,:self.e]=self.core_coefficients@p[self.central_slice]
        y[-1]=0.
        return z

    def initial_vector(self):
        return self.impose_linear_boundary_values(np.zeros(self.size))

    def profile_radius_domain_certificate(self,delta):
        d=tuple(rational(v) for v in np.asarray(delta,float))
        if len(d)!=self.J:raise ValueError('Wrong actual delta count')
        dom=self.profile_domain;lower=self.radius_floor-self.base_lower_bound
        values=[sum((d[j] for j in subset),Fraction()) for subset in dom['subsets']]
        passed=all(v>=lower for v in values)
        bound=min([self.base_lower_bound]+[self.base_lower_bound+v for v in values])
        return dict(passed=passed,exact_arithmetic=True,
            base_lower_exact='4/5',radius_floor_exact='1/10',
            conservative_global_lower_exact=str(bound),
            candidate_sha256=CANDIDATE_SHA256,proof='R181 section 3 and active-support subset inequality',
            violated_rows=[j for j,v in enumerate(values) if v<lower])

    def parameter_domain(self,vector,central_curvature_maximum=None,central_curvature_minimum=0.):
        try:
            _,p=self.unpack(vector)
            if p.shape!=(self.parameter_count,) or not np.all(np.isfinite(p)):return False
            if not self.tail_control_box.certificate(p[self.tail_slice])['passed']:return False
            if not self.profile_radius_domain_certificate(p[self.profile_slice])['passed']:return False
            core,_=self.core(p[self.central_slice]);d=core.definition()
            lower=Fraction(d['conservative_curvature_lower_exact'])
            upper=Fraction(d['conservative_curvature_upper_exact'])
            if not lower>rational(central_curvature_minimum):return False
            if central_curvature_maximum is not None and upper>rational(central_curvature_maximum):return False
            return True
        except (ValueError,FloatingPointError,OverflowError):return False

    def radial_view(self,points):
        points=np.asarray(points,float)
        if points.ndim!=1 or len(points)<2 or np.any(np.diff(points)<=0):
            raise ValueError('Use at least two distinct increasing physical points')
        if points[0]<0 or points[-1]>self.profile.end:
            raise ValueError('View outside the explicit new prefix')
        view=copy.copy(self);view.x=points.copy();view.N=len(points);view.h=np.diff(points)
        view.size=view.N*view.q+view.parameter_count
        view.residual_size=view.N*view.q+2*view.K+2
        view.coords={k:np.asarray(v,float) for k,v in view.chart.coordinates(points).items()}
        view.fixed_central_nodes=np.flatnonzero(points<=view.profile.central_end)
        view._operator_cache={}
        return view

    def lifting(self,delta,tail_parameters):
        ops=self.operators(delta);jet=ops['jet'];a,av=jet['a'],jet['a_s']
        U,Us,Uxi=(self.coords[k] for k in ('u','u_s','u_xi'))
        sn,cs=np.sin(U),np.cos(U);position=a[None,:]*sn
        family=self.tail(tail_parameters);curve=family.angle_jets(position)
        k,ky,kp,kyp=(np.asarray(curve[key],float) for key in
            ('kappa','kappa_y','kappa_jacobian','kappa_y_jacobian'))
        v=np.stack((cs*cs,-sn*cs,sn*sn),axis=-1)
        vu=np.stack((-2*sn*cs,sn*sn-cs*cs,2*sn*cs),axis=-1)
        ys=av[None,:]*sn+a[None,:]*cs*Us;yx=a[None,:]*cs*Uxi
        raw=k[...,None]*v
        raw_s=(ky*ys)[...,None]*v+(k*Us)[...,None]*vu
        raw_xi=(ky*yx)[...,None]*v+(k*Uxi)[...,None]*vu
        rawp=v[...,None]*kp[...,None,:]
        rawsp=v[...,None]*(ys[...,None]*kyp)[...,None,:]+vu[...,None]*(Us[...,None]*kp)[...,None,:]
        rawxp=v[...,None]*(yx[...,None]*kyp)[...,None,:]+vu[...,None]*(Uxi[...,None]*kp)[...,None,:]
        t0,t1=self.tail_window;wt,wq=step5((self.x-t0)/(t1-t0));wts=wq/(t1-t0)
        c0,c1=self.seed_window;w,q=step5((self.x-c0)/(c1-c0));wc,wcs=1-w,-q/(c1-c0)
        extra=self.seed-1/float(self.geometry.a0)
        Q=wt[None,:,None]*raw
        Qs=wt[None,:,None]*raw_s+wts[None,:,None]*raw
        Qxi=wt[None,:,None]*raw_xi
        Q[:,:,0]+=extra[:,None]*wc
        Qs[:,:,0]+=extra[:,None]*wcs
        Qxi[:,:,0]+=self.seed_xi[:,None]*wc
        reference=self.reference.jet(self.x)
        lift=Q+reference['values'][None,:,:]
        lift_s=Qs+reference['ds'][None,:,:]
        lp=wt[None,:,None,None]*rawp
        lps=wt[None,:,None,None]*rawsp+wts[None,:,None,None]*rawp
        lpx=wt[None,:,None,None]*rawxp
        inv,adv,c=ops['inv'],ops['adv'],jet['c']
        fn=(inv*Qxi[:,:,1]+c[None,:]*(Q[:,:,2]-Q[:,:,0])
            +adv*Qxi[:,:,0]-Qs[:,:,0]
            +(c-reference['c0'])[None,:]*(reference['values'][:,2]-reference['values'][:,0])[None,:])
        fm=inv*Qxi[:,:,2]-2*c[None,:]*Q[:,:,1]+adv*Qxi[:,:,1]-Qs[:,:,1]
        fp_n=(inv[...,None]*lpx[:,:,1]+c[None,:,None]*(lp[:,:,2]-lp[:,:,0])
            +adv[...,None]*lpx[:,:,0]-lps[:,:,0])
        fp_m=(inv[...,None]*lpx[:,:,2]-2*c[None,:,None]*lp[:,:,1]
            +adv[...,None]*lpx[:,:,1]-lps[:,:,1])
        forcing=np.concatenate((np.einsum('ew,wn->ne',self.PE,fn),
            np.einsum('kw,wn->nk',self.PO,fm)),axis=1)
        fp=np.concatenate((np.einsum('ew,wnp->nep',self.PE,fp_n),
            np.einsum('kw,wnp->nkp',self.PO,fp_m)),axis=1)
        profile_j=tail_lifting_profile_jacobian(jet,self.coords,family,wt,wts)
        return dict(values=lift,x=lift_s,xi=Qxi,parameters=lp,
            x_parameters=lps,xi_parameters=lpx,
            profile_parameters=profile_j['values'],profile_s_parameters=profile_j['s'],
            profile_x_parameters=profile_j['s'],profile_xi_parameters=profile_j['xi'],
            forcing=forcing,forcing_parameters=fp,tail=family,alpha=np.asarray(curve['alpha'],float),
            round_reference=reference,round_increment=Q,
            central_weight=wc,tail_weight=wt)

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
            (float(axes['gap'])-self.gap)/self.gap_scale]
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
        block(row,offset+self.central_slice.start,np.asarray(axes['gap_jacobian'],float)[None,:]/self.gap_scale)
        matrix=sparse.coo_matrix((np.concatenate(vv),(np.concatenate(rr),np.concatenate(cc))),
            shape=(self.residual_size,self.size)).tocsc()
        matrix.eliminate_zeros()
        return residual,matrix,data

    def definition(self):
        import fd2d_gc_raw_bump_dae as raw
        import fd2d_gc_radial_bump_profile as bump
        import fd2d_dyadic_bernstein_tail as tail
        import fd2d_balanced_curvature_core as central
        return dict(schema=REPRESENTATION,source=identity(__file__),
            candidate=identity(self.source),
            sources=dict(generic_raw=identity(raw.__file__),physical_bumps=identity(bump.__file__),
                tail=identity(tail.__file__),central=identity(central.__file__)),
            parameter_layout=self.parameter_layout(),mesh=self.x.tolist(),K=self.K,work=self.work,
            profile=self.profile.definition(),round_reference=self.reference.definition(),
            atlas=self.chart.chart_definition(),tail_domain=self.tail_control_box.definition(),
            central_base=self.base_kind,central_definition=self.core(np.zeros(self.K))[0].definition(),
            lifting=dict(round='full S0(s), not projected',seed='wc*(fixed central base-1/a0) e_n',
                tail='wt*T(a_delta(s),U(s,xi); sixteen actual controls)',
                seed_window=list(self.seed_window),tail_window=list(self.tail_window),
                round_forcing='A_delta Q-Q_s+(A_delta-A_0)S0; all delta and Us chain terms retained'),
            eliminated_exact_cylinder_nodes=self.fixed_central_nodes.tolist(),
            cut_raw='all zero; actual complete unprojected tail lifted',
            gap_target=self.gap,gap_normalization=self.gap_scale,
            old_R139_coast_old_atlas_or_old_normal_used=False,
            previous_unavailable_source_SHA_claimed=False,
            continuous_embedding_or_strong_goal_certificate=False)


def checkpoint_arrays(problem,vector):
    y,p=problem.unpack(problem.impose_linear_boundary_values(vector))
    definition=problem.definition()
    return dict(schema=np.asarray('fd2d-R181-B32-recovery-explicit-field-archive-v1'),
        representation_kind=np.asarray(REPRESENTATION),
        mesh=np.asarray(problem.x,float),corrections=np.asarray(y,float),parameters=np.asarray(p,float),
        modes=np.asarray(problem.K),base_kind=np.asarray(problem.base_kind),
        central_parameter_count=np.asarray(problem.K),tail_parameter_count=np.asarray(16),
        profile_count=np.asarray(problem.J),parameter_count=np.asarray(problem.parameter_count),
        profile_kind=np.asarray('physical_bumps'),tail_kind=np.asarray(problem.tail_kind),
        profile_supports=np.asarray(problem.profile.supports,float),
        fixed_base_T=np.asarray(problem.fixed_base_T),
        candidate_path=np.asarray(str(problem.source)),
        candidate_sha256=np.asarray(CANDIDATE_SHA256),
        gap_target=np.asarray(problem.gap),gap_scale=np.asarray(problem.gap_scale),
        complete_definition=np.asarray(json.dumps(definition,sort_keys=True,separators=(',',':'))),
        physical_g_changed_from_old_7c3=np.asarray(True),
        exact_continuous_solution_claimed=np.asarray(False))
