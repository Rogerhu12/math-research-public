"""Analytic position variation of the exact normalized R21 rectifying core.

See notes/f6curve_core_variation.md. Astra curve_transition, AI-assisted,
2026-11-08. The calculus is exact; FFT/arc inversion remain floating point.
No alteration of the core, profile, or boundary conditions is made.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import json,time
from pathlib import Path
from types import MethodType
import numpy as np
from f6direct_sparse_core import SparseReflectedCore,geometry,jets


def variation_jets(phi,modes,radius_derivatives,order=2):
    """Fixed-phi unit physical coefficient variations, including normalized R.

    Column zero is the halfwidth direction (all curve variations zero).
    Column j>=1 is the physical Fourier coefficient of modes[j]. Return
    (order+1,M,N,3); this utility supports arbitrary derivative order.
    """
    phi=np.asarray(phi);modes=np.asarray(modes);M=len(modes)
    result=np.zeros((order+1,M,len(phi),3));er=np.exp(1j*phi)
    for j,m in enumerate(modes[1:],1):
        m=int(m);dR=radius_derivatives[j]
        if m%4==0:
            ep=np.exp(1j*(m+1)*phi);em=np.exp(1j*(1-m)*phi)
            for k in range(order+1):
                z=.5*((1j*(m+1))**k*ep+(1j*(1-m))**k*em)+dR*(1j**k)*er
                result[k,j,:,0]=z.real;result[k,j,:,1]=z.imag
        else:
            e=np.exp(1j*m*phi)
            for k in range(order+1):
                z=dR*(1j**k)*er
                result[k,j,:,0]=z.real;result[k,j,:,1]=z.imag
                result[k,j,:,2]=((1j*m)**k*e).real
    return result


def core_variation_data(par,modes,arc_nodes,theta,arc_relative_cutoff=8e-15):
    """Reusable fixed-phi variation cache in unit physical coefficients.

    Includes exact-core phi, base geometry, normalized dR, delta arc and
    delta a0. The zeroth column corresponds to delta halfwidth=1. The data
    can also initialize full-II variation using higher variation_jets.
    """
    modes=np.asarray(modes);theta=np.asarray(theta);M=len(modes)
    core=SparseReflectedCore(par['R'],par['radial'],par['height'],arc_nodes)
    port=core.evaluate(par['halfwidth'],theta);phi=port['phi']
    g=geometry(phi,par['R'],par['radial'],par['height'])
    grid=2*np.pi*np.arange(arc_nodes)/arc_nodes
    d1=jets(grid,par['R'],par['radial'],par['height'],1)[1]
    speed=np.linalg.norm(d1,axis=-1);T=d1/speed[:,None]
    er=np.c_[np.cos(grid),np.sin(grid),np.zeros(arc_nodes)]
    et=np.c_[-np.sin(grid),np.cos(grid),np.zeros(arc_nodes)]
    tr=np.sum(T*er,axis=1);tt=np.sum(T*et,axis=1);den=float(tt.mean())
    if abs(den)<1e-10:raise FloatingPointError('Core radius normalization derivative is too small')
    dv=np.zeros((M,arc_nodes));dR=np.zeros(M)
    for j,m in enumerate(modes[1:],1):
        m=int(m);co=np.cos(m*grid);si=np.sin(m*grid)
        raw=-m*si*tr+co*tt if m%4==0 else -m*si*T[:,2]
        dR[j]=-float(raw.mean())/den;dv[j]=raw+dR[j]*tt
    cf=np.fft.rfft(dv,axis=1)/arc_nodes;da0=cf[:,0].real
    threshold=arc_relative_cutoff*max(1.,float(np.max(abs(dv))))
    active=np.flatnonzero(np.max(abs(cf[:,1:-1]),axis=0)>threshold)
    K=int(active[-1]+1) if len(active) else 0
    dS=da0[:,None]*phi[None,:]
    if K:
        k=np.arange(1,K+1);ac=cf[:,1:K+1]/(1j*k[None,:])
        for start in range(0,len(phi),512):
            e=np.exp(1j*k[:,None]*phi[None,start:start+512])-1
            dS[:,start:start+512]+=2*np.real(ac@e)
    restk=np.arange(K+1,cf.shape[1]-1)
    # Anchoring the primitive at phi=0 contributes exp(ik phi)-1. Do not
    # assume numerically computed Fourier coefficients are exactly real.
    omitted=4*np.sum(abs(cf[:,K+1:-1])/restk[None,:],axis=1) if len(restk) else np.zeros(M)
    omitted+=abs(cf[:,-1])/(arc_nodes//2)
    return dict(core=core,port=port,geometry=g,phi=phi,theta=theta,modes=modes,
                radius_derivatives=dR,arc_derivatives=dS,a0_derivatives=da0,
                radius_normalization_derivative=den,arc_derivative_retained_degree=K,
                arc_derivative_discrete_omitted_l1=omitted,arc_relative_cutoff=arc_relative_cutoff)


def position_variations(data,halfwidth):
    """Return unit physical parameter delta F[M,N,3] at fixed theta."""
    g=data['geometry'];j=variation_jets(data['phi'],data['modes'],data['radius_derivatives'],2)
    dg,dd1,dd2=j;v=g['speed'];T=g['T'];B=g['B']
    dv=np.einsum('np,mnp->mn',T,dd1)
    dT=(dd1-T[None,:,:]*dv[:,:,None])/v[None,:,None]
    c=np.cross(g['d1'],g['d2']);cn=np.linalg.norm(c,axis=1)
    dc=np.cross(dd1,g['d2'][None,:,:])+np.cross(g['d1'][None,:,:],dd2)
    dB=(dc-B[None,:,:]*np.einsum('np,mnp->mn',B,dc)[:,:,None])/cn[None,:,None]
    ds=data['arc_derivatives']-data['a0_derivatives'][:,None]*data['theta'][None,:]
    dF=dg+halfwidth*(dB+g['w'][None,:,None]*dT)-T[None,:,:]*ds[:,:,None]
    dF[0]=B
    return dF


def initial_parameter_jacobian(self,p):
    if getattr(self,'_analytic_core_jac_p',None) is not None and np.array_equal(p,self._analytic_core_jac_p):return self._analytic_core_jac_value
    par=self.parameters(p);nt=max(256,16*int(self.even[-1]));theta=2*np.pi*np.arange(nt)/nt
    data=core_variation_data(par,self.even,self.arc_nodes,theta)
    dF=position_variations(data,par['halfwidth']);B,_,_=self.basis(nt)
    norm=np.sum(B*B,axis=(1,2));J=np.einsum('mpc,kpc->km',dF,B,optimize=True)/norm[:,None]
    J*=self.pscale[None,:]/self.q
    self._analytic_core_jac_p=p.copy();self._analytic_core_jac_value=J
    self.analytic_core_jac_audit=dict(method='Exact rectifying-core position variation with torsion variation cancelled',
        arc_nodes=self.arc_nodes,projection_nodes=nt,radius_normalization_derivative=data['radius_normalization_derivative'],
        arc_derivative_retained_degree=data['arc_derivative_retained_degree'],
        maximum_discrete_omitted_arc_l1=float(np.max(data['arc_derivative_discrete_omitted_l1'])),
        maximum_radius_normalized_mean_derivative=float(np.max(abs(data['a0_derivatives']))),
        scope='Floating-point derivative implementation; arc cutoff bound concerns the discrete Fourier interpolant, not unsampled continuum or roundoff.')
    return J


def install_analytic_core_jacobian(obj):
    obj.initial_parameter_jacobian=MethodType(initial_parameter_jacobian,obj)


def check(path=None,out=None):
    from curve_stable_prefix_bvp import load_checkpoint
    from f6curve_outward_bvp import OutwardPrefix
    from f6curve_sparse_run import install_sparse
    root=Path(__file__).parent.parent
    path=Path(path) if path else root/'notes/f6curve_outward_base6_m28_q0075_local_sparse.json.gz'
    d=load_checkpoint(path);cfg=d['config'];obj=OutwardPrefix(cfg['modes'],cfg['amplitude'],cfg['delta'],cfg['v_up'],cfg['v_down'],cfg['ramp'],cfg['cycles'],cfg['angular'],cfg['base_mode'],compute_stable=False);obj.h0=d['h0'];p=np.asarray(d['parameters'])
    install_sparse(OutwardPrefix);start=time.monotonic();J=initial_parameter_jacobian(obj,p);analytic_seconds=time.monotonic()-start
    columns=sorted(set([0,1,2,obj.M//2,obj.M-2,obj.M-1]));rows=[];fd_start=time.monotonic()
    for column in columns:
        for factor in (4.,1.,.25,.0625):
            step=(2e-5 if column==0 else 2e-6/(obj.pscale[column]*(column+1)**2))*factor
            v=np.zeros(obj.M);v[column]=step
            fd=(-obj.initial(p+2*v)+8*obj.initial(p+v)-8*obj.initial(p-v)+obj.initial(p-2*v))/(12*step)
            error=float(np.max(abs(fd-J[:,column])));scale=float(np.max(abs(J[:,column])))
            rows.append(dict(column=column,physical_mode=int(obj.even[column]),factor=factor,normalized_parameter_step=step,max_abs_error=error,jacobian_scale=scale,relative_error=error/max(1e-300,scale)))
    result=dict(author='Astra curve_transition; AI-assisted',scope='Analytic exact-core position Jacobian compared with the unchanged five-point physical-parameter difference over four step sizes. Numerical implementation check, not interval proof.',input=str(path),modes=obj.M,amplitude=obj.q,analytic_seconds=analytic_seconds,selected_fd_seconds=time.monotonic()-fd_start,analytic_audit=obj.analytic_core_jac_audit,rows=rows)
    out=Path(out) if out else root/'notes/f6curve_core_variation_check.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':
    import argparse
    pa=argparse.ArgumentParser();pa.add_argument('--input');pa.add_argument('--out');a=pa.parse_args();check(a.input,a.out)
