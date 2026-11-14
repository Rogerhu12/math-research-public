"""Full-angle finite physical-point objective for the independent B32 entry.

All angular samples are retained.  Codazzi and Gauss are evaluated at two
actual interior points of each P1 cell; node Gauss is retained separately.
This is an explicitly new finite discretization, not a continuous bound.
Known round Codazzi terms cancel analytically.  No second form is divided.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import numpy as np

from fd2d_gc_archive_arrays import identity
from fd2d_gc_local_normal_system import LocalNormalSystem
from fd2d_gc_r181_b_round_raw import REPRESENTATION


def _maximum(value):return float(np.max(abs(np.asarray(value)),initial=0.))


def complete_point_packet(view,parameters):
    p=np.asarray(parameters,float)
    delta,tail=p[view.profile_slice],p[view.tail_slice]
    ops=view.operators(delta);lift=view.lifting(delta,tail)
    gp=np.zeros(lift['values'].shape+(view.parameter_count,))
    gps=np.zeros_like(gp);gpx=np.zeros_like(gp)
    for section,values,svalues,xvalues in (
        (view.tail_slice,lift['parameters'],lift['x_parameters'],lift['xi_parameters']),
        (view.profile_slice,lift['profile_parameters'],lift['profile_s_parameters'],lift['profile_xi_parameters'])):
        gp[:,:,:,section]=values;gps[:,:,:,section]=svalues;gpx[:,:,:,section]=xvalues
    P=view.parameter_count;jet=ops['jet'];N=view.N
    ap=np.zeros((N,P));cp=np.zeros((N,P));kp=np.zeros((N,P))
    ap[:,view.profile_slice]=jet['a_parameters']
    cp[:,view.profile_slice]=jet['c_parameters']
    kp[:,view.profile_slice]=jet['K_parameters']
    invp=-ap[None,:,:]/(view.coords['u_xi'][:,:,None]*jet['a'][None,:,None]**2)
    return dict(view=view,ops=ops,lift=lift,gp=gp,gps=gps,gpx=gpx,
                ap=ap,cp=cp,kp=kp,invp=invp)


def point_rows(packet,index,raw,raw_s=None,*,node_weights=None,cell_width=None,
               jacobian=True):
    """Rows at one physical point, with [node fields..., all p] columns."""
    q=packet;v=q['view'];i=int(index);y=np.asarray(raw,float)
    E,O,Ex,Ox=v.E,v.O,v.Ex,v.Ox
    nc,mc,lc=E@y[:v.e],O@y[v.e:v.d],E@y[v.d:]
    nx,mx,lx=Ex@y[:v.e],Ox@y[v.e:v.d],Ex@y[v.d:]
    lift=q['lift'];L=lift['values'][:,i];Lx=lift['xi'][:,i]
    n,m,l=nc+L[:,0],mc+L[:,1],lc+L[:,2]
    jet=q['ops']['jet'];K=jet['K'][i]
    G=n*l-m*m-K
    gp,gps,gpx=q['gp'][:,i],q['gps'][:,i],q['gpx'][:,i]
    Ga=np.concatenate((l[:,None]*E,-2*m[:,None]*O,n[:,None]*E),axis=1) if jacobian else None
    Gp=(l[:,None]*gp[:,0]+n[:,None]*gp[:,2]-2*m[:,None]*gp[:,1]-q['kp'][i]) if jacobian else None
    result=dict(gauss=G,fields=np.stack((n,m,l),axis=-1),gauss_raw=Ga,gauss_parameters=Gp)
    if raw_s is None:return result
    if node_weights is None or cell_width is None or len(node_weights)!=2:
        raise ValueError('Actual two-node P1 weights and positive cell width required')
    y_s=np.asarray(raw_s,float);h=float(cell_width)
    if not h>0:raise ValueError('Positive physical cell width required')
    inv=q['ops']['inv'][:,i];adv=q['ops']['adv'][:,i];c=jet['c'][i]
    reference=lift['round_reference'];S0=reference['values'][i]
    other=lift['round_increment'][:,i]
    other_s=lift['x'][:,i]-reference['ds'][i]
    fn=(inv*Lx[:,1]+c*(other[:,2]-other[:,0])+adv*Lx[:,0]-other_s[:,0]
        +(c-reference['c0'][i])*(S0[2]-S0[0]))
    fm=inv*Lx[:,2]-2*c*other[:,1]+adv*Lx[:,1]-other_s[:,1]
    Cn=E@y_s[:v.e]-(inv*mx+c*(lc-nc)+adv*nx)-fn
    Cm=O@y_s[v.e:v.d]-(inv*lx-2*c*mc+adv*mx)-fm
    result['codazzi']=np.stack((Cn,Cm),axis=-1)
    if not jacobian:return result
    invp,cp=q['invp'][:,i],q['cp'][i]
    fnp=(invp*(mx+Lx[:,1])[:,None]+inv[:,None]*gpx[:,1]
        +cp[None,:]*(l-n)[:,None]+c*(gp[:,2]-gp[:,0])
        +adv[:,None]*gpx[:,0]-gps[:,0])
    fmp=(invp*(lx+Lx[:,2])[:,None]+inv[:,None]*gpx[:,2]
        -2*cp[None,:]*m[:,None]-2*c*gp[:,1]
        +adv[:,None]*gpx[:,1]-gps[:,1])
    Aj=np.concatenate((adv[:,None]*Ex-c*E,inv[:,None]*Ox,c*E),axis=1)
    Bj=np.concatenate((np.zeros_like(E),adv[:,None]*Ox-2*c*O,inv[:,None]*Ex),axis=1)
    derivative_n=np.c_[E,np.zeros((v.work,v.q-v.e))]
    derivative_m=np.c_[np.zeros((v.work,v.e)),O,np.zeros((v.work,v.e))]
    result['codazzi_raw']=[np.stack((sign*derivative_n/h-t*Aj,
            sign*derivative_m/h-t*Bj),axis=1)
        for sign,t in zip((-1,1),node_weights)]
    result['codazzi_parameters']=-np.stack((fnp,fmp),axis=1)
    return result


class RoundB32PointObjective:
    """A bounded-memory local normal / same finite-value consumer."""
    def __init__(self,problem,*,order=2,point_batch=8,
                 codazzi_weight=1.,gauss_weight=1.,gap_weight=1.):
        if problem.representation_kind!=REPRESENTATION:
            raise TypeError('Select the explicit independent new B32 round provider')
        if int(order)!=order or not 1<=order<=8:raise ValueError('Explicit finite Gauss order 1..8 required')
        if int(point_batch)!=point_batch or point_batch<2:raise ValueError('Use a bounded batch with at least two points')
        self.problem=problem;self.order=int(order);self.point_batch=int(point_batch)
        self.codazzi_weight=float(codazzi_weight);self.gauss_weight=float(gauss_weight);self.gap_weight=float(gap_weight)
        if min(self.codazzi_weight,self.gauss_weight,self.gap_weight)<=0:raise ValueError('Keep all equation groups with positive weights')
        nodes,ww=np.polynomial.legendre.leggauss(self.order)
        self.tau=(nodes+1)/2;self.weights=ww/2
        self.length=float(problem.x[-1]-problem.x[0]);h=problem.h
        self.node_weights=np.r_[h[0]/2,(h[:-1]+h[1:])/2,h[-1]/2]/self.length
        self.points=(problem.x[:-1,None]+h[:,None]*self.tau).ravel()
        self._views={}

    def definition(self):
        p=self.problem
        return dict(schema='fd2d-R181-B32-full-angle-physical-point-objective-v1',
            source=identity(__file__),K=p.K,work=p.work,mesh=p.x.tolist(),
            component_order=['n','m','l'],codazzi_point_order=self.order,
            normalized_cell_points=self.tau.tolist(),normalized_cell_weights=self.weights.tolist(),
            node_gauss='all physical mesh nodes; Voronoi length weights / total length',
            cell_equations='full unprojected physical Codazzi and Gauss at every declared Gauss point',
            angular_normalization='sqrt(2/work); all actual angular points retained',
            radial_normalization='sqrt(cell_length/total_length*Gauss_average_weight)',
            weights=dict(Codazzi=self.codazzi_weight,Gauss=self.gauss_weight,gap=self.gap_weight),
            boundary='exact central-cylinder and cut raw coefficients eliminated by the recorded map',
            gap=dict(target=p.gap,scale=p.gap_scale),
            reference_Codazzi_terms_cancelled_analytically=True,
            projected_only_Gauss_or_Codazzi=False,
            continuous_or_exact_surface_certificate=False)

    def _packet(self,parameters,points,key):
        if key not in self._views:
            self._views[key]=self.problem.radial_view(points)
        view=self._views[key]
        view._operator_cache.clear()
        return complete_point_packet(view,parameters)

    def consume(self,vector,*,jacobian=False):
        p=self.problem;y,parameters=p.unpack(vector)
        projected=p.impose_linear_boundary_values(vector)
        boundary_error=_maximum(projected-vector)
        if boundary_error>1e-12:raise ValueError('The explicit central/cut boundary map was not imposed')
        normal=LocalNormalSystem(p) if jacobian else None
        total_squared=0.;groups={};counts={};maxG=0.;maxC=0.;maxk=0.;minimum_n=np.inf
        def add(residual,J,nodes,label):
            nonlocal total_squared
            r=np.asarray(residual,float).reshape(-1)
            if not np.all(np.isfinite(r)):raise FloatingPointError('Nonfinite finite objective')
            value=float(r@r);total_squared+=value
            groups[label]=groups.get(label,0.)+value;counts[label]=counts.get(label,0)+len(r)
            if normal is not None:normal.add(r,J,nodes,label=label)
        def geometry(row):
            nonlocal maxG,maxC,maxk,minimum_n
            n,m,l=row['fields'].T
            maxG=max(maxG,_maximum(row['gauss']))
            if 'codazzi' in row:maxC=max(maxC,_maximum(row['codazzi']))
            radius=np.hypot(n-l,2*m)
            maxk=max(maxk,float(np.max(np.maximum(abs(n+l+radius),abs(n+l-radius)))/2))
            minimum_n=min(minimum_n,float(np.min(n)))
        angular=np.sqrt(2./p.work)
        # Node Gauss; each local block has one raw field node and all p.
        for start in range(0,p.N,self.point_batch):
            stop=min(start+self.point_batch,p.N)
            # A singleton final batch uses a neighbouring point only as an
            # evaluation view, without adding or dropping any residual row.
            begin=start if stop-start>=2 else start-1
            points=p.x[begin:stop]
            packet=self._packet(parameters,points,('nodes',begin,stop))
            for j in range(start,stop):
                row=point_rows(packet,j-begin,y[j],jacobian=jacobian);geometry(row)
                scale=self.gauss_weight*angular*np.sqrt(self.node_weights[j])
                J=None if not jacobian else scale*np.c_[row['gauss_raw'],row['gauss_parameters']]
                add(scale*row['gauss'],J,(j,),'node_Gauss')
        # True differential Codazzi/Gauss at the full fixed finite point set.
        qcount=len(self.points)
        for start in range(0,qcount,self.point_batch):
            stop=min(start+self.point_batch,qcount);begin=start if stop-start>=2 else start-1
            packet=self._packet(parameters,self.points[begin:stop],('cells',begin,stop))
            for k in range(start,stop):
                cell,gindex=divmod(k,self.order);tau=float(self.tau[gindex]);h=p.h[cell]
                raw=(1-tau)*y[cell]+tau*y[cell+1]
                row=point_rows(packet,k-begin,raw,(y[cell+1]-y[cell])/h,
                    node_weights=(1-tau,tau),cell_width=h,jacobian=jacobian);geometry(row)
                common=angular*np.sqrt(h/self.length*self.weights[gindex])
                cscale=common*self.codazzi_weight;gscale=common*self.gauss_weight
                if jacobian:
                    blocks=row['codazzi_raw']
                    Cj=cscale*np.concatenate((blocks[0],blocks[1],row['codazzi_parameters']),axis=2).reshape(2*p.work,2*p.q+p.parameter_count)
                    Gj=gscale*np.c_[(1-tau)*row['gauss_raw'],tau*row['gauss_raw'],row['gauss_parameters']]
                else:Cj=Gj=None
                add(cscale*row['codazzi'],Cj,(cell,cell+1),'point_Codazzi')
                add(gscale*row['gauss'],Gj,(cell,cell+1),'point_Gauss')
        _,axes=p.core(parameters[p.central_slice])
        gap=float(axes['gap']);gaprow=self.gap_weight*(gap-p.gap)/p.gap_scale
        Jgap=np.zeros((1,p.parameter_count)) if jacobian else None
        if jacobian:Jgap[0,p.central_slice]=self.gap_weight*np.asarray(axes['gap_jacobian'],float)/p.gap_scale
        add([gaprow],Jgap,(),'gap')
        diagnostics=dict(norm=float(np.sqrt(total_squared)),residual_squared=total_squared,
            groups=groups,row_counts=counts,full_finite_Gauss_maximum=maxG,
            full_finite_Codazzi_maximum=maxC,formal_curvature_samples_maximum=maxk,
            full_n_samples_minimum=minimum_n,actual_gap=gap,target_gap=p.gap,
            central_A=float(axes['A']),central_B=float(axes['B']),
            raw_boundary_map_error=boundary_error,continuous_certificate=False,
            node_count=p.N,quadrature_point_count=qcount,angular_work=p.work,
            normal_bytes=(normal.storage_bytes() if normal is not None else None))
        if normal is not None:
            diagnostics['normal_squared_value_difference']=float(normal.residual_squared-total_squared)
            normal.info=dict(objective_definition=self.definition(),actual_diagnostics=diagnostics)
        return diagnostics,normal


def small_gap_parameter_certificate(problem,vector,*,profile_box=.08):
    """A continuous central positivity sufficient bound plus exact domains.

    R181's a0<201/200 and |material mean cos|<=1 imply
    n_core >=200/201-2*sum(abs(c_j)) for the selected circle base.
    This small-gap branch chooses the positive margin 1/10 explicitly.
    """
    if problem.base_kind!='circle':raise ValueError('This particular small-gap domain uses the exact circle base')
    _,p=problem.unpack(vector)
    central=[Fraction.from_float(float(v)) for v in p[problem.central_slice]]
    lower=Fraction(200,201)-2*sum((abs(v) for v in central),Fraction())
    tail=problem.tail_control_box.certificate(p[problem.tail_slice])
    radius=problem.profile_radius_domain_certificate(p[problem.profile_slice])
    box=Fraction.from_float(float(profile_box))
    delta=[Fraction.from_float(float(v)) for v in p[problem.profile_slice]]
    passed=(lower>=Fraction(1,10) and tail['passed'] and radius['passed'] and all(abs(v)<=box for v in delta))
    return dict(passed=passed,central_continuous_curvature_lower_exact=str(lower),
        central_floor='1/10',central_proof='a0<201/200 from accurate moments; every material cosine mean lies in [-1,1]',
        tail=tail,profile=radius,explicit_outer_profile_box=str(box),
        sampled_central_positivity_not_substituted_for_this_bound=True)
