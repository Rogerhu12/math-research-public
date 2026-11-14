"""Global positive angular atlas with a frozen natural-ruling coast patch.

Central/cut open neighborhoods retain the original chart. Values and all
angular derivatives have identical traces at patch interfaces. Radial jets
are one-sided there, with the coast side as the default solver convention.
The physical material metric is unchanged; all maps are parameter-frozen.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_k0_ruling_chart import FrozenRulingChart
from fd2d_k0_native_gc import native_from_inlet
from fd2d_k0_ruling_coast import ruling_coordinates


def step5_jets(x,left,right):
    t=np.clip((np.asarray(x,float)-float(left))/(float(right)-float(left)),0.,1.)
    value=t**3*(10.-15.*t+6.*t*t)
    first=30.*t*t*(1.-t)**2/(right-left)
    second=60.*t*(1.-t)*(1.-2.*t)/(right-left)**2
    return value,first,second


class FrozenRulingAtlas:
    def __init__(self,original_chart,inlet_path,*,entry_start=.55,exit_stop=1.4):
        self.original=original_chart;self.inlet_path=Path(inlet_path)
        self.ruling=FrozenRulingChart(self.inlet_path)
        self.entry_s=float(self.ruling.entry_s);self.length=float(self.ruling.length)
        self.exit_s=self.entry_s+self.length;self.entry_start=float(entry_start);self.exit_stop=float(exit_stop)
        if not 0<=self.entry_start<self.entry_s<self.exit_s<self.exit_stop<self.original.candidate.end:
            raise ValueError('Ordered interior atlas patch intervals are required')
        self.theta=self.original.theta;self._labels=[]
        here=Path(__file__).resolve().parent
        self._definition=dict(schema='fd2d-global-positive-frozen-ruling-atlas-v1',
            source_sha256=identity(__file__)['sha256'],inlet_sha256=identity(inlet_path)['sha256'],
            dependencies={name:identity(here/name)['sha256'] for name in
                ('fd2d_k0_ruling_chart.py','fd2d_k0_native_gc.py','fd2d_k0_ruling_coast.py','fd2d_balanced_curvature_core.py')},
            candidate_sha256=self.ruling.base.candidate_sha256,
            original_chart=self.original.chart_definition(),
            entry_transition=[self.entry_start,self.entry_s],coast=[self.entry_s,self.exit_s],
            exit_transition=[self.exit_s,self.exit_stop],smoothstep_degree=5,
            entry_formula='(1-S5)*U_old(s,xi)+S5*U_seed(xi)',
            coast_formula='Frozen R139 ruling map, label xi is fixed inlet seed-normal angle',
            exit_formula='(1-S5)*U_exit(xi)+S5*U_old(s,xi)',
            elsewhere='original chart on open central and cut neighborhoods',
            interface_values_and_angular_jets='same whole functions on both sides',
            interface_radial_jets='one-sided; coordinates side=coast default, or left/right explicitly',
            a_c=float(self.ruling.a),v=float(self.ruling.v),
            positive_U_xi='positive convex combinations of original/seed/frozen-exit derivatives, and R139 D>0 within coast',
            parameters_frozen=True,physical_g_changed=False,
            physical_metric='ds^2+a_delta(s)^2 du^2',
            coordinate_metric='(1+a_delta^2 U_s^2) ds^2+2 a_delta^2 U_s U_xi ds dxi+a_delta^2 U_xi^2 dxi^2',
            selected_actual_reconstruction='fixed physical material u',
            field_interface='shared P1 coefficient value and common full physical lifting trace; U_s continuity is not assumed')

    def __getattr__(self,name):
        original=self.__dict__.get('original')
        if original is None:raise AttributeError(name)
        return getattr(original,name)
    def __copy__(self):return self
    def __deepcopy__(self,memo):memo[id(self)]=self;return self
    def chart_definition(self):return dict(self._definition)

    def label_data(self,coordinate):
        xi=np.atleast_1d(np.asarray(coordinate,np.longdouble))
        if xi.ndim!=1 or not np.all(np.isfinite(xi)):raise ValueError('A finite one-dimensional fixed label array is required')
        for index,(old,data) in enumerate(self._labels):
            if np.array_equal(old,xi):
                if index:self._labels.insert(0,self._labels.pop(index))
                return data
        data=self.ruling.inlet_at_label(xi)
        n,m,nu,mu=data['n'],data['m'],data['n_u'],data['m_u']
        k=m/n;ku=mu/n-m*nu/n**2
        kuu=data['m_uu']/n-m*data['n_uu']/n**2-2*mu*nu/n**2+2*m*nu*nu/n**3
        data=dict(data,k=k,k_u=ku,k_uu=kuu,label=xi.copy())
        self._labels.insert(0,(xi.copy(),data));del self._labels[8:]
        return data

    def ruling_jet(self,s,coordinate=None,*,include_native=False):
        s=float(s);xi=self.theta if coordinate is None else coordinate;data=self.label_data(xi)
        sigma=0. if s==self.entry_s else self.length if s==self.exit_s else s-self.entry_s
        if not 0<=sigma<=self.length:raise ValueError('Ruling formula requested outside the frozen coast')
        c=ruling_coordinates(self.ruling.a,self.ruling.v,sigma,data['k'],data['k_u'],data['k_uu'])
        h,hp=data['inlet_chart_derivative'],data['inlet_chart_second']
        out=dict(u=data['u']+c['material_shift'],u_s=c['U_s'],u_xi=c['U_t']*h,
            u_ss=c['U_ss'],u_sxi=c['U_st']*h,u_xixi=c['U_tt']*h*h+c['U_t']*hp,D=c['D'])
        if include_native:out['native']=native_from_inlet(self.ruling.a,self.ruling.v,sigma,data)
        return out

    def coordinates(self,s,coordinate=None,*,side='coast'):
        if side not in ('coast','left','right'):raise ValueError('Use coast, left, or right one-sided chart jets')
        x=np.atleast_1d(np.asarray(s,float));xi=np.atleast_1d(np.asarray(self.theta if coordinate is None else coordinate,np.longdouble))
        if x.ndim!=1 or xi.ndim!=1 or not np.all(np.isfinite(x)):raise ValueError('Finite one-dimensional positions and labels required')
        old=self.original.coordinates(x,coordinate=xi)
        names=('u','u_s','u_xi','u_ss','u_sxi','u_xixi')
        out={name:np.array(old[name],np.longdouble,copy=True) for name in names}
        data=self.label_data(xi)
        seed=dict(u=data['u'],u_xi=data['inlet_chart_derivative'],u_xixi=data['inlet_chart_second'])
        entry=(x>=self.entry_start)&(x<self.entry_s)
        coast=(x>=self.entry_s)&(x<=self.exit_s)
        leave=(x>self.exit_s)&(x<=self.exit_stop)
        if side=='left':entry|=x==self.entry_s;coast&=x!=self.entry_s
        if side=='right':leave|=x==self.exit_s;coast&=x!=self.exit_s
        if np.any(entry):
            q,qp,qpp=step5_jets(x[entry],self.entry_start,self.entry_s)
            q,qp,qpp=(a[None,:] for a in (q,qp,qpp))
            for name in ('u','u_xi','u_xixi'):
                out[name][:,entry]=(1-q)*old[name][:,entry]+q*seed[name][:,None]
            out['u_s'][:,entry]=(1-q)*old['u_s'][:,entry]+qp*(seed['u'][:,None]-old['u'][:,entry])
            out['u_sxi'][:,entry]=(1-q)*old['u_sxi'][:,entry]+qp*(seed['u_xi'][:,None]-old['u_xi'][:,entry])
            out['u_ss'][:,entry]=(1-q)*old['u_ss'][:,entry]-2*qp*old['u_s'][:,entry]+qpp*(seed['u'][:,None]-old['u'][:,entry])
        for j in np.flatnonzero(coast):
            jet=self.ruling_jet(x[j],xi)
            for name in names:out[name][:,j]=jet[name]
        if np.any(leave):
            end=self.ruling_jet(self.exit_s,xi)
            q,qp,qpp=step5_jets(x[leave],self.exit_s,self.exit_stop)
            q,qp,qpp=(a[None,:] for a in (q,qp,qpp))
            for name in ('u','u_xi','u_xixi'):
                out[name][:,leave]=(1-q)*end[name][:,None]+q*old[name][:,leave]
            out['u_s'][:,leave]=q*old['u_s'][:,leave]+qp*(old['u'][:,leave]-end['u'][:,None])
            out['u_sxi'][:,leave]=q*old['u_sxi'][:,leave]+qp*(old['u_xi'][:,leave]-end['u_xi'][:,None])
            out['u_ss'][:,leave]=q*old['u_ss'][:,leave]+2*qp*old['u_s'][:,leave]+qpp*(old['u'][:,leave]-end['u'][:,None])
        if np.any(out['u_xi']<=0) or not all(np.all(np.isfinite(out[name])) for name in names):
            raise FloatingPointError('Frozen positive atlas produced a nonpositive/nonfinite derivative')
        out['advection']=out['u_s']/out['u_xi']
        out['frozen_ruling_label']=np.broadcast_to(xi[:,None],out['u'].shape)
        return out


def invert_original_chart_on_grid(original_chart,s,material_u,*,tolerance=1e-13,max_iterations=100):
    """Actual same-material warm coordinates, with all errors returned.

    Target is a (labels, radial nodes) array. Only unfinished scalar entries
    are reevaluated. P1 interpolation and Fourier projection are separate.
    """
    s=np.asarray(s,float);target=np.asarray(material_u,np.longdouble)
    if target.ndim!=2 or target.shape[1]!=len(s):raise ValueError('Expected labels-by-radial-node material targets')
    beta=np.broadcast_to(np.asarray(original_chart.blend(s)[0],np.longdouble)[None,:],target.shape).ravel()
    shape=target.shape;u=target.ravel();t=u.copy();width=np.longdouble(np.pi)
    lo=u-width;hi=u+width;done=np.zeros(len(u),bool);last=np.full(len(u),np.inf,np.longdouble)
    for iteration in range(int(max_iterations)):
        ids=np.flatnonzero(~done)
        if not len(ids):break
        ref=original_chart.reference.reference_coordinate(t[ids])
        uu=np.asarray(ref['u'],np.longdouble);vv=np.asarray(ref['u_theta'],np.longdouble)
        f=t[ids]+(1-beta[ids])*(uu-t[ids])-u[ids]
        derivative=1+(1-beta[ids])*(vv-1)
        if np.any(derivative<=0):raise FloatingPointError('Old positive chart derivative failed')
        last[ids]=f;good=abs(f)<=tolerance;done[ids[good]]=True
        active=ids[~good];fa=f[~good];da=derivative[~good]
        lo[active]=np.where(fa<0,t[active],lo[active]);hi[active]=np.where(fa>0,t[active],hi[active])
        trial=t[active]-fa/da
        if iteration>=40:trial=(lo[active]+hi[active])/2
        else:trial=np.where((trial<=lo[active])|(trial>=hi[active]),(lo[active]+hi[active])/2,trial)
        t[active]=trial
    if not np.all(done):raise RuntimeError('Original-chart warm inverse did not reach its explicit tolerance')
    # A complete returned-coordinate residual is paid independently of flags.
    q=original_chart.reference.reference_coordinate(t)
    full=t+(1-beta)*(np.asarray(q['u'],np.longdouble)-t)-u
    maximum=float(np.max(abs(full),initial=0.))
    if maximum>tolerance:raise RuntimeError('Returned old coordinate missed the explicit tolerance')
    return t.reshape(shape),dict(method='active-entry safeguarded Newton then bisection',
        iterations=iteration+1,maximum_material_residual=maximum,tolerance=float(tolerance),
        material_targets=target.size,physical_metric_changed=False)
