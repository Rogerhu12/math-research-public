"""R129 consumer: exact P1 raw corrections plus full endpoint liftings.

Recovered from the recorded source after the executor became unavailable.
Arrays define continuous piecewise-linear Fourier corrections in computational x.
All l,m,n remain independent; radial derivatives are actual cell slopes. At nodes
the side selects only a derivative: every value and angular derivative is shared.

This is a floating evaluator of the bound mathematical functions, not an interval
certificate. Fixed-u frame reconstruction selects the actual map of R119/R124.
"""
from __future__ import annotations
import gzip
import hashlib
import io
import json
from math import comb,factorial
from pathlib import Path
import numpy as np
from fd2d_balanced_curvature_core import FixedBalancedGeometry,BalancedCurvatureCore
from fd2d_gc_design_profile import CoastDesignProfile
from fd2d_gc_design_profile_positive import PositiveCoastDesignProfile
from fd2d_flat_developable_family import FlatDevelopableFamily
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily
from fd2d_gc_three_field_residual import native_residuals,native_angular_residuals

SCHEMA='fd2d-raw-three-field-piecewise-linear-exact-lifting-v1'
HERE=Path(__file__).resolve().parent


def identity(path):
    path=Path(path);data=path.read_bytes()
    return dict(path=str(path.resolve()),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())


def load_arrays(path):
    path=Path(path)
    if path.suffix=='.gz':
        with gzip.open(path,'rb') as handle:data=handle.read()
        with np.load(io.BytesIO(data),allow_pickle=False) as archive:
            return {key:archive[key].copy() for key in ('mesh','corrections','parameters')}
    with np.load(path,allow_pickle=False) as archive:
        return {key:archive[key].copy() for key in ('mesh','corrections','parameters')}


def locate_bound(owner,row):
    old=Path(row.get('path',row.get('file','')))
    options=(old,Path(owner).parent/old.name,HERE.parent/'notes'/old.name,HERE/old.name)
    for path in options:
        if path.is_file() and identity(path)['sha256']==row['sha256']:return path
    raise ValueError('Missing or changed bound input: '+old.name)


def step5(t):
    t=np.asarray(t,float);z=np.clip(t,0.,1.);active=(t>0.)&(t<1.)
    return (z**3*(10-15*z+6*z*z),
            np.where(active,30*z*z*(1-z)**2,0.),
            np.where(active,60*z*(1-z)*(1-2*z),0.))


def _product_derivative(q,left,right,order):
    out=np.zeros_like(q)
    for j in range(order+1):
        k=order-j
        a=factorial(left)//factorial(left-j)
        b=factorial(right)//factorial(right-k)
        out+=comb(order,j)*a*b*(-1)**k*q**(left-j)*(1-q)**(right-k)
    return out


def curvature_second_y(family,y,tail_kind):
    """Analytic alpha'''(y), including clipped endpoints."""
    y=np.asarray(y,float);raw=(np.abs(y)-family.flat_radius)/family.width
    q=np.clip(raw,0.,1.);inside=(raw>0.)&(raw<1.);count=family.parameter_count
    if tail_kind=='positive_bernstein':
        degree=count-1;third=np.zeros_like(q)
        for i,p in enumerate(family.coefficients):
            third+=630*comb(degree,i)*p*_product_derivative(q,i+4,degree-i+4,2)
    elif tail_kind=='signed_bubble':
        third=family.coefficients[0]*2520*q*q*(1-q)**2*(3-14*q+14*q*q)
        bubbles=count-1
        if bubbles:
            x=2*q-1;T=np.empty(q.shape+(bubbles,))
            T1=np.zeros_like(T);T2=np.zeros_like(T);T3=np.zeros_like(T)
            T[...,0]=1.
            if bubbles>1:T[...,1]=x;T1[...,1]=2.
            for j in range(2,bubbles):
                T[...,j]=2*x*T[...,j-1]-T[...,j-2]
                T1[...,j]=4*T[...,j-1]+2*x*T1[...,j-1]-T1[...,j-2]
                T2[...,j]=8*T1[...,j-1]+2*x*T2[...,j-1]-T2[...,j-2]
                T3[...,j]=12*T2[...,j-1]+2*x*T3[...,j-1]-T3[...,j-2]
            pp=[1024*_product_derivative(q,5,5,j) for j in range(4)]
            basis=pp[3][...,None]*T+3*pp[2][...,None]*T1+3*pp[1][...,None]*T2+pp[0][...,None]*T3
            third+=basis@family.coefficients[1:]
    else:raise ValueError('Unknown explicit tail_kind')
    return np.where(inside,third/family.width**3,0.)


class RawLiftedNativeField:
    def __init__(self,arrays,candidate,*,reference_T,blend_interval,
                 profile_kind='legacy_coast',tail_kind='signed_bubble',
                 base_kind='balanced_seed',geometry=None):
        self.arrays_path,self.candidate_path=Path(arrays),Path(candidate)
        data=load_arrays(arrays)
        self.nodes,self.values,self.parameters=(data[k] for k in ('mesh','corrections','parameters'))
        if not all(q.dtype==np.float64 and np.all(np.isfinite(q)) for q in (self.nodes,self.values,self.parameters)):
            raise ValueError('Defining arrays must be finite binary64')
        if self.nodes.ndim!=1 or len(self.nodes)<2 or np.any(np.diff(self.nodes)<=0):
            raise ValueError('Radial nodes must be strictly increasing')
        if self.values.ndim!=2 or self.values.shape[0]!=len(self.nodes):
            raise ValueError('Correction array must have shape (nodes,3K+2)')
        self.K=(self.values.shape[1]-2)//3;self.e,self.d=self.K+1,2*self.K+1
        if self.K<1 or self.values.shape[1]!=3*self.K+2 or self.parameters.shape!=(2*self.K+2,):
            raise ValueError('Inconsistent raw correction/parameter dimensions')
        self.profile_kind,self.tail_kind,self.base_kind=profile_kind,tail_kind,base_kind
        profiles=dict(legacy_coast=CoastDesignProfile,positive_clock=PositiveCoastDesignProfile)
        tails=dict(signed_bubble=FlatDevelopableFamily,positive_bernstein=PositiveFlatDevelopableFamily)
        if profile_kind not in profiles or tail_kind not in tails:
            raise ValueError('An explicit supported profile_kind/tail_kind is required')
        self.profile=profiles[profile_kind](candidate,reference_T=reference_T)
        self.profile.set_parameter(self.parameters[-1])
        self.geometry=FixedBalancedGeometry() if geometry is None else geometry
        self.core=BalancedCurvatureCore(self.parameters[:self.K],base_kind=base_kind,geometry=self.geometry)
        self.tail=tails[tail_kind](self.parameters[self.K:-1],cut_radius=.8,cuff_radius=.32,flat_radius=.34,plane_height=1.25)
        self.blend_interval=tuple(float(q) for q in blend_interval)
        if not 0<=self.blend_interval[0]<self.blend_interval[1]<=self.profile.end:
            raise ValueError('The recorded fixed-x blend is outside the domain')
        if self.nodes[0]!=0. or abs(self.nodes[-1]-self.profile.end)>1e-12:
            raise ValueError('The stored radial arrays do not cover this profile chart')
        self.frequencies=2*np.arange(self.K+1,dtype=float)
        self._inverse_seed_cache={}
        for q in (self.nodes,self.values,self.parameters):q.flags.writeable=False

    @classmethod
    def from_definition(cls,path):
        path=Path(path);meta=json.loads(path.read_text())
        if meta['schema']!=SCHEMA:raise ValueError('Wrong raw native definition schema')
        for row in meta['sources']:locate_bound(path,row)
        geometry=FixedBalancedGeometry(moments=locate_bound(path,meta['moments']),means=locate_bound(path,meta['means']))
        return cls(locate_bound(path,meta['arrays']),locate_bound(path,meta['candidate_input']),
                   reference_T=meta['radial_chart']['reference_T'],blend_interval=meta['blend_interval'],
                   geometry=geometry,**{k:meta[k] for k in ('profile_kind','tail_kind','base_kind')})

    def definition(self):
        files=['fd2d_gc_raw_native_field.py','fd2d_gc_three_field_residual.py',
               'fd2d_balanced_curvature_core.py','fd2d_gc_design_profile.py',
               'fd2d_gc_design_profile_positive.py','fd2d_flat_developable_family.py',
               'fd2d_positive_flat_developable_family.py']
        return dict(schema=SCHEMA,arrays=identity(self.arrays_path),candidate_input=identity(self.candidate_path),
            sources=[identity(HERE/f) for f in files],moments=identity(self.geometry.moments_path),
            means=identity(self.geometry.means_path),profile_kind=self.profile_kind,tail_kind=self.tail_kind,
            base_kind=self.base_kind,node_count=len(self.nodes),mode_count=self.K,
            correction_order='[n_0,n_2,...,n_2K,m_2,...,m_2K,l_0,l_2,...,l_2K]',
            parameters_order='[central K, tail K+1, physical T]',
            radial_interpolation='Exact continuous piecewise-linear binary node corrections in x',
            node_derivative='One-sided actual cell slope; side affects no value or angular derivative',
            independent_l_saved=True,no_shape_denominator=True,
            cut_correction_exactly_zero=bool(np.all(self.values[-1]==0.)),
            cut_correction_absolute_max=float(np.max(np.abs(self.values[-1]))),
            central_l_correction_exactly_zero=bool(np.all(self.values[0,self.d:]==0.)),
            central_m_correction_exactly_zero=bool(np.all(self.values[0,self.e:self.d]==0.)),
            radial_chart=self.profile.definition(),blend_interval=list(self.blend_interval),
            angular_chart='Fixed seed normal-to-material angle; beta quintic on the recorded x interval',
            angular_chart_formula='u=(1-beta(x))*U_seed(xi)+beta(x)*xi',
            central_definition=self.core.definition(),
            lifting=dict(component_order=['n','m','l'],tail_start_fraction=.42,
                tail_end='profile computational end',seed_end='min(.55,.4*profile.end)',
                seed_n='1/rho_seed(xi) for balanced_seed; 1/a0 for circle',
                radial_weights='quintic step; no angular truncation of either lifting'),
            actual_map='R119 fixed physical u, F_x=J*F*A, X_x=J*F*e1',
            full_residual_certified=False,closed_surface=False)

    def state(self,x,*,side='right'):
        if side not in ('left','right'):raise ValueError('side must be left or right')
        x=np.asarray(x,float)
        if np.any(x<self.nodes[0]) or np.any(x>self.nodes[-1]):
            raise ValueError('Outside the defining radial interval')
        j=np.clip(np.searchsorted(self.nodes,x,side=side)-1,0,len(self.nodes)-2)
        width=self.nodes[j+1]-self.nodes[j];t=(x-self.nodes[j])/width
        slope=(self.values[j+1]-self.values[j])/width[...,None]
        value=self.values[j]+t[...,None]*(self.values[j+1]-self.values[j])
        value=np.where((t==0)[...,None],self.values[j],np.where((t==1)[...,None],self.values[j+1],value))
        return value,slope,j

    def chart(self,x,xi):
        x,xi=np.broadcast_arrays(np.asarray(x,float),np.asarray(xi,float))
        q=self.geometry.material_coordinate(xi)
        u0,rho0,rhop0=(np.asarray(q[k],float) for k in ('u','u_phi','u_phi_phi'))
        left,right=self.blend_interval
        beta,bx,bxx=step5((x-left)/(right-left));bx,bxx=bx/(right-left),bxx/(right-left)**2
        displacement=u0-xi;U=xi+(1-beta)*displacement;om=1+(1-beta)*(rho0-1)
        if np.any(om<=0):raise FloatingPointError('Positive angular chart not represented')
        return dict(u=U,u_x=-bx*displacement,u_xi=om,u_xixi=(1-beta)*rhop0,
                    u_x_xi=-bx*(rho0-1),u_xx=-bxx*displacement,beta=beta)

    def invert_angle(self,x,u):
        x,u=np.broadcast_arrays(np.asarray(x,float),np.asarray(u,float))
        turns=np.floor(u/(2*np.pi));target=u-turns*(2*np.pi)
        lo,hi=np.zeros_like(u),np.full_like(u,2*np.pi)
        key=(target.shape,target.tobytes())
        if key not in self._inverse_seed_cache:
            if len(self._inverse_seed_cache)>=2:self._inverse_seed_cache.clear()
            self._inverse_seed_cache[key]=np.asarray(self.geometry.normal_angle(target),float)
        left,right=self.blend_interval;beta=step5((x-left)/(right-left))[0]
        xi=(1-beta)*self._inverse_seed_cache[key]+beta*target
        for _ in range(96):
            jet=self.chart(x,xi);error=jet['u']-target
            done=np.abs(error)<=32*np.finfo(float).eps*(1+np.abs(target))
            if np.all(done):return xi+turns*(2*np.pi)
            lo=np.where((error<0)&~done,xi,lo);hi=np.where((error>0)&~done,xi,hi)
            trial=xi-error/jet['u_xi'];margin=.05*(hi-lo)
            bad=(trial<=lo+margin)|(trial>=hi-margin)|~np.isfinite(trial)
            xi=np.where(done,xi,np.where(bad,(lo+hi)/2,trial))
        raise ArithmeticError('Numerical inversion of the exact monotone angular chart did not finish')

    def _seed(self,xi):
        rho=np.asarray(self.geometry.radius(xi),float);rhop=np.asarray(self.geometry.radius_derivative(xi),float)
        if self.base_kind=='circle':
            return np.full_like(rho,1/float(self.geometry.a0)),np.zeros_like(rho),np.zeros_like(rho)
        k,D,u2,u4,c=(float(getattr(self.geometry,q)) for q in ('k','D','u2','u4','c'))
        s2,c2=np.sin(2*xi),np.cos(2*xi);th=np.tanh(k*(c2-c));sech=1-th*th
        rhopp=2*D*k*c2*sech+4*D*k*k*s2*s2*th*sech-4*u2*c2-16*u4*np.cos(4*xi)
        return 1/rho,-rhop/rho**2,2*rhop*rhop/rho**3-rhopp/rho**2

    def evaluate_native(self,x,xi,*,side='right'):
        """Broadcast point pairs; x[:,None],xi[None,:] make a tensor grid."""
        x,xi=np.broadcast_arrays(np.asarray(x,float),np.asarray(xi,float));shape=x.shape
        xf,pf=x.ravel(),xi.ravel()
        coef,coefx,cell=self.state(xf,side=side);chart=self.chart(xf,pf);target=self.profile.jet(xf)
        a,ap,app,J=(np.asarray(target[k],float) for k in ('a','a_s','a_ss','radial_scale'))
        U,Ux,om,omxi,Uxxi=(chart[k] for k in ('u','u_x','u_xi','u_xixi','u_x_xi'))
        phase=pf[:,None]*self.frequencies;co,si=np.cos(phase),np.sin(phase);freq=self.frequencies
        bases=(co,si[:,1:],co)
        bases1=(-si*freq,co[:,1:]*freq[1:],-si*freq)
        bases2=(-co*freq**2,-si[:,1:]*freq[1:]**2,-co*freq**2)
        sections=(slice(0,self.e),slice(self.e,self.d),slice(self.d,None))
        sums=lambda cc,bb:np.stack([np.einsum('ij,ij->i',cc[:,ss],b) for ss,b in zip(sections,bb)],axis=-1)
        value=sums(coef,bases);dx=sums(coefx,bases);dxi=sums(coef,bases1)
        dxixi=sums(coef,bases2);dxxi=sums(coefx,bases1)
        sn,cs=np.sin(U),np.cos(U);y=a*sn;curve=self.tail.angle_jets(y)
        k,ky=(curve[q] for q in ('kappa','kappa_y'));kyy=curvature_second_y(self.tail,y,self.tail_kind)
        vv=np.stack((cs*cs,-sn*cs,sn*sn),axis=-1)
        vu=np.stack((-2*sn*cs,sn*sn-cs*cs,2*sn*cs),axis=-1)
        vuu=np.stack((-2*(cs*cs-sn*sn),4*sn*cs,2*(cs*cs-sn*sn)),axis=-1)
        yx=ap*J*sn+a*cs*Ux;yxi=a*cs*om
        yxixi=a*(-sn*om*om+cs*omxi);yxxi=ap*J*cs*om+a*(-sn*Ux*om+cs*Uxxi)
        mul=lambda b,v:b[:,None]*v
        raw=mul(k,vv);rawx=mul(ky*yx,vv)+mul(k*Ux,vu);rawxi=mul(ky*yxi,vv)+mul(k*om,vu)
        rawxixi=(mul(kyy*yxi*yxi+ky*yxixi,vv)+mul(2*ky*yxi*om,vu)
                  +mul(k*om*om,vuu)+mul(k*omxi,vu))
        rawxxi=(mul(kyy*yx*yxi+ky*yxxi,vv)+mul(ky*(yx*om+yxi*Ux),vu)
                +mul(k*Ux*om,vuu)+mul(k*Uxxi,vu))
        end=self.profile.end;tail_length=.58*end
        wt,wtx,_=step5((xf-.42*end)/tail_length);wtx=wtx/tail_length
        seed_end=min(.55,.4*end);wc,wcx,_=step5(xf/seed_end);wc,wcx=1-wc,-wcx/seed_end
        seed,seedxi,seedxixi=self._seed(pf)
        value+=mul(wt,raw);dx+=mul(wtx,raw)+mul(wt,rawx)
        dxi+=mul(wt,rawxi);dxixi+=mul(wt,rawxixi);dxxi+=mul(wtx,rawxi)+mul(wt,rawxxi)
        value[:,0]+=wc*seed;dx[:,0]+=wcx*seed
        dxi[:,0]+=wc*seedxi;dxixi[:,0]+=wc*seedxixi;dxxi[:,0]+=wcx*seedxi
        result={}
        for j,name in enumerate(('n','m','l')):
            for suffix,arr in (('',value),('_x',dx),('_xi',dxi),('_xixi',dxixi),('_x_xi',dxxi)):
                result[name+suffix]=arr[:,j].reshape(shape)
        result.update({k:np.asarray(v).reshape(shape) for k,v in
            dict(a=a,a_s=ap,a_ss=app,J=J,s=target['s'],x=xf,xi=pf,u=U,U_x=Ux,U_xi=om,
                 U_xixi=omxi,U_x_xi=Uxxi,cell=cell).items()})
        return result

    def physical(self,x,u,*,side='right'):
        xi=self.invert_angle(x,u);out=self.evaluate_native(x,xi,side=side)
        om,omxi=out['U_xi'],out['U_xixi'];drift=out['U_x']/om
        for name in ('l','m','n'):
            out[name+'_u']=out[name+'_xi']/om
            out[name+'_uu']=(out[name+'_xixi']-out[name+'_u']*omxi)/om**2
            out[name+'_s']=(out[name+'_x']-drift*out[name+'_xi'])/out['J']
        out['requested_u']=np.broadcast_to(np.asarray(u,float),np.shape(xi))
        out['angle_inverse_error']=out['u']-out['requested_u']
        return out

    def residuals(self,x,xi,*,side='right',angular=False):
        q=self.evaluate_native(x,xi,side=side)
        names=('a','a_s','a_ss','l','m','n','J','U_x','U_xi','l_xi','m_xi','n_xi','m_x','n_x')
        result=native_residuals(**{k:q[k] for k in names})
        if angular:
            names=('a','a_s','l','m','n','J','U_x','U_xi','U_x_xi','U_xixi',
                   'l_xi','m_xi','n_xi','l_xixi','m_xixi','n_xixi','m_x_xi','n_x_xi')
            result.update(native_angular_residuals(**{k:q[k] for k in names}))
        return result

    def body_initial(self,u):return body_initial_from_core(self.core,u)

    def body_rhs(self,x,state,u):
        q=self.physical(x,u)
        return body_rhs_from_fields(state,**{k:q[k] for k in ('J','l','m','l_u','m_u','l_uu','m_uu')})

    def body_jets(self,x,state,u):
        q=self.physical(x,u)
        return actual_body_twojet(state,a=q['a'],l=q['l'])


def pack_body_state(X,F,r,b,v,q):
    return np.concatenate((X,np.asarray(F).reshape(np.shape(X)[:-1]+(9,)),r,b,v,q),axis=-1)


def unpack_body_state(state):
    y=np.asarray(state,float)
    if y.shape[-1]!=24:raise ValueError('Body state is [X3,F9,r3,b3,r_u3,b_u3]')
    return y[...,:3],y[...,3:12].reshape(y.shape[:-1]+(3,3)),y[...,12:15],y[...,15:18],y[...,18:21],y[...,21:24]


def body_initial_from_core(core,u):
    g=core.evaluate_material(u);X=np.asarray(g['X'],float)
    F=np.stack([np.asarray(g[k],float) for k in ('e1','e2','N')],axis=-1)
    zero=np.zeros_like(np.asarray(u,float));a0=float(core.a0)
    r=np.stack((a0*np.asarray(g['n'],float),zero,zero),axis=-1)
    b=np.stack((zero,np.full_like(zero,a0),zero),axis=-1)
    v=np.stack((a0*np.asarray(g['n_u'],float),zero,zero),axis=-1)
    return pack_body_state(X,F,r,b,v,np.zeros_like(r))


def body_rhs_from_fields(state,*,J,l,m,l_u,m_u,l_uu,m_uu):
    """R124 radial system in x while holding physical u fixed."""
    X,F,r,b,v,q=unpack_body_state(state)
    l,m,lu,mu,luu,muu,J=np.broadcast_arrays(l,m,l_u,m_u,l_uu,m_uu,J)
    zero=np.zeros_like(l);alpha=np.stack((m,-l,zero),axis=-1)
    alphau=np.stack((mu,-lu,zero),axis=-1);alphauu=np.stack((muu,-luu,zero),axis=-1)
    A=np.zeros(l.shape+(3,3));A[...,0,2]=-l;A[...,1,2]=-m;A[...,2,0]=l;A[...,2,1]=m
    e1=np.zeros_like(r);e1[...,0]=1.
    FX=F[...,0];FF=F@A
    rr=np.cross(r,alpha)+alphau
    bb=-np.cross(alpha,b)+np.cross(r,e1)
    vv=np.cross(v,alpha)+np.cross(r,alphau)+alphauu
    qq=-np.cross(alpha,q)-np.cross(alphau,b)+np.cross(v,e1)
    return pack_body_state(FX,FF,rr,bb,vv,qq)*J[...,None]


def actual_body_twojet(state,*,a,l):
    """Actual Cartesian derivatives; auxiliary n is deliberately not used."""
    X,F,r,b,v,q=unpack_body_state(state)
    a=np.broadcast_to(np.asarray(a,float),X.shape[:-1]);l=np.broadcast_to(np.asarray(l,float),X.shape[:-1])
    e1=np.zeros_like(b);e1[...,0]=1.
    apply=lambda z:np.einsum('...ij,...j->...i',F,z)
    tss=np.zeros_like(b);tss[...,2]=l
    Xs=F[...,0];Xu=apply(b);Xss=apply(tss);Xsu=apply(np.cross(r,e1));Xuu=apply(np.cross(r,b)+q)
    E=np.sum(Xs*Xs,axis=-1);cross=np.cross(Xs,Xu);area=np.linalg.norm(cross,axis=-1)
    if np.any(area<=0):raise FloatingPointError('This numerically evaluated actual map is not immersed')
    N=cross/area[...,None];ff=np.sum(Xs*Xu,axis=-1)/a;gg=np.sum(Xu*Xu,axis=-1)/a**2
    error_matrix=np.empty(a.shape+(2,2));error_matrix[...,0,0]=E-1
    error_matrix[...,0,1]=error_matrix[...,1,0]=ff;error_matrix[...,1,1]=gg-1
    metric_error=np.max(np.abs(np.linalg.eigvalsh(error_matrix)),axis=-1)
    return dict(X=X,X_s=Xs,X_u=Xu,X_ss=Xss,X_su=Xsu,X_uu=Xuu,N=N,outward_normal=-N,
        induced_metric_orthonormal=np.stack((E,ff,gg),axis=-1),
        actual_second_form_orthonormal=np.stack((np.sum(N*Xss,axis=-1),
            np.sum(N*Xsu,axis=-1)/a,np.sum(N*Xuu,axis=-1)/a**2),axis=-1),
        metric_relative_operator_error=metric_error,
        frame_orthogonality_error=np.max(np.abs(np.swapaxes(F,-1,-2)@F-np.eye(3)),axis=(-2,-1)),
        scope='Floating actual ODE-map two-jets; integration and coefficient errors require posterior bounds.')
