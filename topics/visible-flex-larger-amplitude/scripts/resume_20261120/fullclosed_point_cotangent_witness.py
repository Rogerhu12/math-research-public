#!/usr/bin/env python3
"""Exact full-free transpose of one physical six-jet cotangent.

This includes every declared three-jet observation of the two-node common
quintic, the constrained core jets, every
free core coefficient's analytic circle-lift chain, and the global height.
It is not a curvature or reach certificate.
"""
import numpy as np
from types import SimpleNamespace


def pullback(problem, prepared, stage, angle, cotangent):
    q=problem;M=q.M;n=q.n
    nu=q.freq;phi=float(q.phi[angle])
    co=np.cos(np.r_[0.,nu]*phi);si=np.sin(nu*phi)
    b0=np.zeros((3,n));b1=np.zeros((3,n));b2=np.zeros((3,n))
    b0[0,:M+1]=co;b0[1,M+1:2*M+1]=si;b0[2,2*M+1:]=co
    b1[0,1:M+1]=-nu*si;b1[1,:M+1]=co
    b1[0,M+1:2*M+1]=-si;b1[1,M+1:2*M+1]=nu*co[1:]
    b1[2,2*M+2:]=-nu*si
    b2[0,:M+1]=-(1+np.r_[0.,nu*nu])*co
    b2[1,1:M+1]=-2*nu*si
    b2[0,M+1:2*M+1]=-2*nu*co[1:]
    b2[1,M+1:2*M+1]=-(1+nu*nu)*si
    b2[2,2*M+2:]=-nu*nu*co[1:]
    xi=np.asarray(cotangent['F']);alpha=np.asarray(cotangent['Fs'])
    beta=np.asarray(cotangent['Fphi']);gamma=np.asarray(cotangent['Fss'])
    delta=np.asarray(cotangent['Fsphi']);epsilon=np.asarray(cotangent['Fphiphi'])
    gy=xi@b0+beta@b1+epsilon@b2
    gu=alpha@b0+delta@b1
    ga=gamma@b0
    stage_gradient=np.stack((gy,gu,ga))
    jets_gradient=np.zeros((q.J,3,n))
    if hasattr(q,'observation_cells'):
        cell=int(q.observation_cells[stage])
        jets_gradient[cell:cell+2]+=(q.observation_weights[stage].T@stage_gradient).reshape(2,3,n)
    elif stage%2:
        cell=stage//2
        jets_gradient[cell:cell+2]=(q.mid_weights[cell].T@stage_gradient).reshape(2,3,n)
    else:
        jets_gradient[stage//2]=stage_gradient
    chi,cp,cpp,f,fp,fpp=q.lift_scalar[stage]
    er,et=prepared.er[angle],prepared.et[angle]
    rho,rhop=prepared.rho[angle],prepared.rho_phi[angle]
    gtheta=(f*(xi@et)+fp*(alpha@et)+fpp*(gamma@et)
            -f*rho*(beta@er)-fp*rho*(delta@er)
            -f*(epsilon@(rhop*er+rho*rho*et)))
    grho=f*(beta@et)+fp*(delta@et)-2*f*rho*(epsilon@er)
    grhop=f*(epsilon@et)
    core=(gtheta*(q.qfreq/nu)*si+grho*q.qfreq*co[1:]
          -grhop*nu*q.qfreq*si)
    height=chi*xi[2]+cp*alpha[2]+cpp*gamma[2]
    result=q._free_adjoint(jets_gradient,height)
    result[:M-q.K]+=core[q.K:]
    return result


class _PointView:
    def __init__(self, original, cell, phi, weights, lift):
        self.original=original
        self.phi=np.array([phi]);self.N=1;self.P=1
        self.observation_cells=np.array([cell],dtype=int)
        self.observation_weights=np.asarray(weights)[None]
        self.lift_scalar=np.asarray(lift)[None]
    def __getattr__(self,name):
        return getattr(self.original,name)


def _at_context(problem,prepared,cell,u,phi,observed_module):
    q=problem;cell=int(cell);u=float(u);phi=float(phi)
    if not 0<=cell<q.J-1 or not 0<=u<=1 or not np.isfinite(phi):
        raise ValueError('The geometric witness must lie in an actual original cell')
    h=q.mesh[cell+1]-q.mesh[cell]
    weights=observed_module.hermite_weights(h,u)
    lift=np.asarray(q._lift_scalar(float(q.mesh[cell]+h*u)))
    co=np.cos(q.freq*phi);si=np.sin(q.freq*phi)
    rho=1.+co@(q.qfreq*prepared.core)
    rhop=-si@(q.freq*q.qfreq*prepared.core)
    delta=si@((q.qfreq/q.freq)*prepared.core)
    er=np.array([np.cos(delta),np.sin(delta),0.])
    et=np.array([-np.sin(delta),np.cos(delta),0.])
    view=_PointView(q,cell,phi,weights,lift)
    p=SimpleNamespace(rho=np.array([rho]),rho_phi=np.array([rhop]),
                      er=er[None],et=et[None])
    return view,p,co,si,weights,lift


def pullback_at(problem,prepared,cell,u,phi,cotangent,observed_module):
    view,p,_,_,_,_=_at_context(problem,prepared,cell,u,phi,observed_module)
    return pullback(view,p,0,0,cotangent)


def fields_at(problem,prepared,cell,u,phi,observed_module):
    q=problem;M=q.M;nu=q.freq
    _,p,co,si,weights,lift=_at_context(q,prepared,cell,u,phi,observed_module)
    c0=np.r_[1.,co]
    y,v,acc=weights@prepared.jets[int(cell):int(cell)+2].reshape(6,q.n)
    def synth(a):
        return np.array([c0@a[:M+1],si@a[M+1:2*M+1],c0@a[2*M+1:]])
    def angular(a,order=1):
        r,t,z=a[:M+1],a[M+1:2*M+1],a[2*M+1:]
        R,T,Z=c0@r,si@t,c0@z
        Rp,Tp,Zp=-si@(nu*r[1:]),co@(nu*t),-si@(nu*z[1:])
        if order==1:return np.array([Rp-T,Tp+R,Zp])
        return np.array([-co@(nu*nu*r[1:])-2*Tp-R,
                         -si@(nu*nu*t)+2*Rp-T,-co@(nu*nu*z[1:])])
    chi,cp,cpp,f,fp,fpp=lift
    er,et=p.er[0],p.et[0];rho,rhop=p.rho[0],p.rho_phi[0]
    F=synth(y)+f*er;V=synth(v)+fp*er;ss=synth(acc)+fpp*er
    F[2]+=chi*prepared.height;V[2]+=cp*prepared.height;ss[2]+=cpp*prepared.height
    return dict(F=F,Fs=V,Fss=ss,Fphi=angular(y)+f*rho*et,
        Fsphi=angular(v)+fp*rho*et,
        Fphiphi=angular(y,2)+f*(rhop*et-rho*rho*er))


def witness_geometry(problem,prepared,witness,geometry_module,observed_module):
    cell,u,phi=int(witness['cell']),float(witness['u']),float(witness['phi'])
    fields=fields_at(problem,prepared,cell,u,phi,observed_module)
    area=float(np.linalg.norm(np.cross(fields['Fs'],fields['Fphi'])))
    if not np.isfinite(area) or area<=0:
        return dict(complete=False,cell=cell,u=u,phi=phi,area=area)
    try:
        principal=[geometry_module.curvature_cotangent(fields,j)[0]for j in (0,1)]
    except np.linalg.LinAlgError as error:
        return dict(complete=False,cell=cell,u=u,phi=phi,area=area,error=repr(error))
    return dict(complete=True,cell=cell,u=u,phi=phi,
        s=float(problem.mesh[cell]+(problem.mesh[cell+1]-problem.mesh[cell])*u),
        principal_curvatures=principal,maximum_absolute_principal_curvature=max(abs(k)for k in principal),
        radius=float(np.linalg.norm(fields['F'])),area=area,
        scope='Actual arbitrary-point witness only; no continuous maximum enclosure')


def derivative_checks(problem,x,geometry_module,base_scale,curvature_location,seed=2026112002):
    """Three necessary checks of this new full-core/node/H transpose only."""
    q=problem;p=q.prepare(x);rng=np.random.default_rng(seed)
    direction=base_scale*rng.standard_normal(q.free_size)
    step=1e-30
    pc=q.prepare(x+1j*step*direction)
    records=[]
    for stage,angle in ((1,min(137,q.N-1)),(q.P-2,min(91,q.N-1))):
        fields=q.six_jets(p,stage);complex_fields=q.six_jets(pc,stage)
        cotangent={key:rng.standard_normal(3) for key in fields}
        value=sum(cotangent[key]@complex_fields[key][angle] for key in fields)
        predicted=float(pullback(q,p,stage,angle,cotangent)@direction)
        actual=float(np.imag(value)/step)
        difference=abs(actual-predicted)/max(1.,abs(actual),abs(predicted))
        records.append(dict(kind='arbitrary_sixjet_contraction',stage=stage,angle=angle,
                            analytic=predicted,complex_step=actual,relative_difference=difference))
    stage,angle,branch=curvature_location
    fields=geometry_module.single_fields(q,p,stage,angle)
    value,cotangent,metadata=geometry_module.curvature_cotangent(fields,branch)
    complex_fields=geometry_module.single_fields(q,pc,stage,angle)
    actual=float(np.imag(geometry_module.analytic_kappa(complex_fields,branch))/step)
    predicted=float(pullback(q,p,stage,angle,cotangent)@direction)
    difference=abs(actual-predicted)/max(1.,abs(actual),abs(predicted))
    records.append(dict(kind='selected_signed_principal_curvature',stage=stage,angle=angle,
                        branch=branch,analytic=predicted,complex_step=actual,
                        relative_difference=difference,principal_metadata=metadata))
    maximum=max(r['relative_difference']for r in records)
    if maximum>2e-9:
        raise ValueError('New complete point cotangent fails its independent directional check')
    return dict(seed=seed,step=step,maximum_relative_difference=maximum,records=records,
                scope='New full-free point transpose only; no repeated whole-model or continuous certificate')


def build_tangent_projector(problem,x,geometry_module,transpose,coordinate_size,*,
        reach_ratio=.03,safety=.98,active_band=.025,max_rows=16,rank_tolerance=1e-10,
        top_curvature=16,top_radius=2,witnesses=(),observed_module=None):
    """Homogeneous compatible tangency to selected near-active point products."""
    q=problem;p=q.prepare(x)
    scan,locations,radial_locations=geometry_module.scan_geometry(q,x,
        top_curvature=top_curvature,top_radius=top_radius)
    if not scan['complete']:
        raise ValueError('Cannot form active geometry rows at a singular point sample')
    radii=[]
    for stage,angle in radial_locations:
        fields=geometry_module.single_fields(q,p,stage,angle)
        radius=float(np.linalg.norm(fields['F']))
        cot={key:np.zeros(3)for key in fields};cot['F']=2*fields['F']/radius
        radii.append((2*radius,pullback(q,p,stage,angle,cot),(stage,angle)))
    radii.append((2.,np.zeros(q.free_size),('fixed_core',)))
    gheight=np.zeros(q.free_size);gheight[-1]=2*np.sign(p.height)
    radii.append((2*abs(float(p.height)),gheight,('cap_height',)))
    candidates=[]
    for stage,angle,branch in locations:
        fields=geometry_module.single_fields(q,p,stage,angle)
        value,cot,meta=geometry_module.curvature_cotangent(fields,branch)
        for diameter,_,rloc in radii:
            product=reach_ratio*diameter*abs(value)
            if product>=safety-active_band:
                candidates.append((product,(stage,angle,branch),value,cot,meta,diameter,rloc,False))
    witness_records=[]
    if witnesses and observed_module is None:
        raise ValueError('Arbitrary witnesses require the original Hermite weight source')
    for witness in witnesses:
        cell,u,phi=int(witness['cell']),float(witness['u']),float(witness['phi'])
        fields=fields_at(q,p,cell,u,phi,observed_module)
        values=[geometry_module.curvature_cotangent(fields,j)for j in (0,1)]
        branch=int(np.argmax([abs(v[0])for v in values]))
        value,cot,meta=values[branch]
        # The strongest current diameter partner of every supplied actual
        # witness is mandatory; other near-active partners remain eligible.
        strongest=max(range(len(radii)),key=lambda j:radii[j][0])
        for j,(diameter,_,rloc) in enumerate(radii):
            product=reach_ratio*diameter*abs(value)
            if j==strongest or product>=safety-active_band:
                candidates.append((product,('arbitrary',cell,u,phi,branch),value,cot,meta,
                                   diameter,rloc,j==strongest))
        witness_records.append(dict(cell=cell,u=u,phi=phi,current_branch=branch,current_kappa=value))
    if sum(c[-1]for c in candidates)>max_rows:
        raise ValueError('The selected maximum row count would drop a required actual witness')
    candidates.sort(key=lambda item:(not item[-1],-item[0]))
    candidates=candidates[:max_rows]
    rows=[];metadata=[]
    radius_map={tuple(loc):(diameter,g)for diameter,g,loc in radii}
    for product,location,value,cot,meta,diameter,rloc,mandatory in candidates:
        if location[0]=='arbitrary':
            _,cell,u,phi,branch=location
            dk=pullback_at(q,p,cell,u,phi,cot,observed_module)
        else:
            stage,angle,branch=location
            dk=pullback(q,p,stage,angle,cot)
        dD=radius_map[tuple(rloc)][1]
        free_gradient=reach_ratio*(diameter*np.sign(value)*dk+abs(value)*dD)
        row=transpose(free_gradient)
        norm=float(np.linalg.norm(row))
        if not np.isfinite(norm) or norm<=0:
            raise ValueError('A selected geometric tangent has no finite positive coordinate norm')
        rows.append(row/norm)
        metadata.append(dict(product=product,margin=safety-product,curvature_point=location,
            radius_point=rloc,curvature=value,diameter=diameter,gradient_coordinate_norm=norm,
            principal_metadata=meta,mandatory_actual_witness=mandatory))
    if rows:
        matrix=np.stack(rows);del rows
        gram=matrix@matrix.T
        eigenvalues,eigenvectors=np.linalg.eigh(gram)
        keep=eigenvalues>rank_tolerance*eigenvalues[-1]
        Q=(eigenvectors[:,keep]/np.sqrt(eigenvalues[keep])).T@matrix
        # Reorthogonalize the retained numerical row space before repeated
        # matrix-free projection; this changes no selected row-space rank.
        Q=np.linalg.qr(Q.T,mode='reduced')[0].T
        orthogonality=float(np.max(np.abs(Q@Q.T-np.eye(Q.shape[0]))))
        spectrum=eigenvalues.tolist()
    else:
        matrix=np.zeros((0,coordinate_size));Q=matrix
        spectrum=[];orthogonality=0.
    def project(v):
        return v-Q.T@(Q@v) if len(Q) else v.copy()
    report=dict(current_scan=scan,selection='highest sampled products among top separated curvature/radius locations with r>=safety-active_band',
        reach_ratio=reach_ratio,safety=safety,active_band=active_band,max_rows=max_rows,
        top_curvature=top_curvature,top_radius=top_radius,selected_rows=len(metadata),
        retained_rank=len(Q),relative_eigenvalue_cutoff=rank_tolerance,
        reorthogonalization='Householder QR on the retained eigenspace row basis',
        normalized_row_gram_eigenvalues=spectrum,orthonormal_rows_error=orthogonality,
        arbitrary_witnesses=witness_records,rows=metadata,projector='P=I-Q^T Q; homogeneous z0=0, selected current-step tangent only',
        scope='Numerical active-step slice; original nonlinear field and all original Gram rows remain. True point screening still decides acceptance.')
    return project,matrix,Q,report,locations
