"""Physical material-angle predictor for the two-parameter design family.

This only initializes the original BVP. It never changes the physical port,
full Frenet residual, admissible-root guard or solver acceptance tolerance.
Both physical meridian parameters are predicted, while the exact core is
rebuilt for the declared target q and local-circle homotopy.
"""
import hashlib
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly,CubicSpline
from material_warm_restart import values_at


def restart(obj,BVP,records,settings):
    from fixed_metric_mode3_bvp import merge_profile_mesh
    if obj.fixed or len(records) not in (1,2):raise ValueError('One or two design records required')
    target_settings=dict(settings);old=[]
    for rec in records:
        if not rec['solver_success']:raise ValueError('Only accepted checkpoints may be predictors')
        if rec['config']['base_mode']!=4:raise ValueError('Wrong mode')
        if rec['plateau_settings']['bimodal_eta']!=target_settings['bimodal_eta']:raise ValueError('Changing eta requires a separate declared predictor')
        if rec['physical_port']['parameters']!=obj.port['parameters']:raise ValueError('Different physical tail')
        for k,v in obj._reference_cfg.items():
            if k not in ('delta','vd') and rec['profile'].get(k)!=v:raise ValueError('Different profile family: '+k)
        settings.clear();settings.update(rec['plateau_settings'])
        q=float(rec['gauge_amplitude']);M=int(rec['config']['modes'])
        previous=BVP(rec['profile'],rec['physical_port'],q,M,rec['config']['angular'],False,q)
        previous.pscale=np.asarray(rec['central_correction_scales']);previous.bcweights=np.full(M,.01)
        p=np.asarray(rec['parameters']);initial=previous.initial(p).copy();f=previous.flow(p[0])
        mesh=np.asarray(rec['mesh']);pp=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),mesh,extrapolate=True,axis=1)
        Nlift=max(4096,128*M);f.geo(np.array([0.]),Nlift);lift=f.exact_lift_cache[Nlift][0]
        spline=CubicSpline(np.linspace(0,2*np.pi,Nlift+1),np.concatenate((lift,lift[:1])),bc_type='periodic')
        old.append(dict(rec=rec,obj=previous,f=f,p=p,pp=pp,q=q,M=M,initial=initial,lift=spline,mesh=mesh))
    settings.clear();settings.update(target_settings)
    latest=old[-1];ratio=obj.q/latest['q'];par=np.zeros(obj.M)
    if len(old)==1:
        for j,key in ((0,'delta'),(1,'vd')):
            base=latest['rec']['profile'][key]
            par[j]=base+(latest['rec']['physical_profile'][key]-base)*ratio**2-obj._reference_cfg[key]
        for j in range(2,min(obj.M,latest['M'])):
            par[j]=latest['p'][j]*latest['obj'].pscale[j-1]*ratio**2/obj.pscale[j-1]
        weights=[1.]
    else:
        before=old[0]
        if not before['q']<latest['q'] or before['rec']['plateau_settings']!=latest['rec']['plateau_settings']:raise ValueError('Ordered q at fixed core homotopy required')
        factor=(obj.q-latest['q'])/(latest['q']-before['q'])
        factor2=(obj.q**2-latest['q']**2)/(latest['q']**2-before['q']**2)
        for j,key in ((0,'delta'),(1,'vd')):
            vl=latest['rec']['physical_profile'][key];vb=before['rec']['physical_profile'][key]
            par[j]=vl+factor2*(vl-vb)-obj._reference_cfg[key]
        for j in range(2,min(obj.M,latest['M'])):
            vl=latest['p'][j]*latest['obj'].pscale[j-1]/latest['q']
            vb=before['p'][j]*before['obj'].pscale[j-1]/before['q'] if j<before['M'] else 0.
            par[j]=obj.q*((1+factor)*vl-factor*vb)/obj.pscale[j-1]
        weights=[-factor,1+factor]
    obj.initial(par);f=obj.flow(par[0])
    t=latest['obj'].inverse_chart(latest['mesh'],latest['p'][0])
    t=merge_profile_mesh(t,np.unique(np.r_[obj.chart_breaks,obj.inverse_chart(np.r_[.5*f.prefix_end,.9*f.prefix_end,.75*f.end],par[0])]))
    s=obj.chart(t,par[0])[0];N=max(2048,64*max([obj.M]+[v['M']for v in old]));B=f.basis(N)[0]
    y=np.empty((obj.n,len(t)));pullback_residual=0.
    for first in range(0,len(t),24):
        sl=slice(first,first+24);g=f.geo(s[sl],N);theta=g['theta'];target=np.zeros((len(s[sl]),N,3))
        for weight,v in zip(weights,old):
            sold=v['obj'].chart(t[sl],v['p'][0])[0];e=v['f'].geo(sold,1)['e'][:,None];psi=theta.copy()
            for _ in range(40):
                update=(psi-e*np.sin(4*psi)/4-theta)/(1-e*np.cos(4*psi));psi-=update
                if float(abs(update).max())<2e-14:break
            residual=float(abs(psi-e*np.sin(4*psi)/4-theta).max());pullback_residual=max(pullback_residual,residual)
            if residual>1e-12:raise FloatingPointError('Material-angle pullback did not converge')
            V=v['q']*values_at(v['pp'](sold),psi,4,v['M'])
            u=np.clip((sold-.5*v['f'].prefix_end)/(.4*v['f'].prefix_end),0.,1.)
            h=v['f'].profile(sold)[0]*(1-u**3*(10-15*u+6*u*u))
            V+=h[:,None,None]*v['lift'](np.mod(psi,2*np.pi));target+=weight*V/v['q']
        base=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)*f.profile(s[sl])[0][:,None,None]
        target-=(g['pos']-base)/obj.q;y[:,sl]=f.project(target,B)
    before_bc=float(abs(obj.bc(y[:,0],y[:,-1],par)).max());repair=obj.initial(par)-y[:,0]
    cutoff=(f.Tu if f.direction=='outward' else f.Td)/2;y+=repair[:,None]*np.maximum(0.,1-s/cutoff)[None,:]**3
    diagnostic=dict(method='dual-parameter-design-material-angle-predictor',q_inputs=[v['q']for v in old],q_target=obj.q,secant_weights=weights,radial_nodes=len(t),angular_projection=N,pullback_residual=pullback_residual,
      predicted_delta=obj._reference_cfg['delta']+par[0],predicted_vd=obj._reference_cfg['vd']+par[1],inlet_repair_coefficient_max=float(abs(repair).max()),scaled_bc_before=before_bc,scaled_bc_after=float(abs(obj.bc(y[:,0],y[:,-1],par)).max()),
      source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Only an initial guess; unchanged full equations, root guards and solver tolerance')
    if len(old)==1 and obj.q==latest['q'] and obj.M==latest['M'] and target_settings==latest['rec']['plateau_settings']:
        diagnostic['same_chart_identity_max']=float(abs(y-latest['pp'](latest['obj'].chart(t,latest['p'][0])[0])).max())
    return t,y,par,diagnostic
