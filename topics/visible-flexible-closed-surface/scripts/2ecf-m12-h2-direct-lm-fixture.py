#!/usr/bin/env python3
"""Nonzero coupled-M12 finite interface check against an independent dense J.

The small analytic background is not an M12 whole-half field. Its signed
planar columns and all three physical Gram rows use the production basis;
the independent dense Jacobian is formed by direct sine/cosine formulae.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def dense_band(band):
    n=band.shape[1];out=np.zeros((n,n))
    for d in range(band.shape[0]):
        j=np.arange(n-d);out[j+d,j]=band[d,:n-d];out[j,j+d]=band[d,:n-d]
    return out
def rel(a,b):return float(np.linalg.norm(a-b)/max(np.finfo(float).tiny,np.linalg.norm(b)))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,required=True)
    ap.add_argument('--consumer',type=Path,default=None)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();began=time.monotonic()
    if args.consumer is None:args.consumer=args.scripts/'6a65-m12-complete-gram-normal-preconditioner.py'
    lm=load('new_h2_lm_consumer',Path(__file__).with_name('2ecf-m12-h2-direct-lm.py'))
    if args.out.exists():raise FileExistsError('Fresh finite check report required')
    stream_path=args.scripts/'6a65-streaming-cartesian-full-gram.py'
    generic_path=args.scripts/'6a65-cartesian-complete-radial-normal.py'
    stream=load('fixture_original_m12_stream',stream_path);new=load('fixture_new_m12_normal',args.consumer)
    mesh=np.array([0.,.09,.2,.31,.47,.66,.78,.91,1.]);N=24;order=3;T=1.7
    class Basis(stream.bvp.Basis):
        def __init__(self):
            super().__init__(mesh,order);self.nb-=6
        def matrices(self,z):
            z=np.asarray(z);H=1+.2*z+.1*z*z;Hq=(.2+.2*z)/T
            p0=self.spline(z)[:,3:-3];p1=self.spline(z,nu=1)[:,3:-3];p2=self.spline(z,nu=2)[:,3:-3]
            return [csr_matrix(p0),csr_matrix(p1/(T*H[:,None])),
                    csr_matrix(p2/(T*T*H[:,None]**2)-p1*Hq[:,None]/(T*H[:,None]**3))]
    basis=Basis();gx,gw=np.polynomial.legendre.leggauss(4)
    nodes=((mesh[:-1]+mesh[1:])[:,None]/2+(mesh[1:]-mesh[:-1])[:,None]*gx/2).ravel()
    weights=((mesh[1:]-mesh[:-1])[:,None]*gw/2).ravel()*T*(1+.2*nodes+.1*nodes**2)
    def background(z,N):
        u=2*np.pi*np.arange(N)/N;s=T*(np.asarray(z)+.1*np.asarray(z)**2+np.asarray(z)**3/30)
        s=s[:,None];u=u[None,:];zero=np.zeros((len(z),N))
        X=np.stack(((1+.1*s)*np.cos(u)+.025*np.cos(2*u),
                    (1+.12*s)*np.sin(u)+.02*np.sin(3*u),
                    .5*s+.03*np.sin(2*u)+.02*s*s*np.cos(u)),axis=-1)
        Xs=np.stack((.1*np.cos(u)+zero,.12*np.sin(u)+zero,.5+.04*s*np.cos(u)),axis=-1)
        Xt=np.stack((-(1+.1*s)*np.sin(u)-.05*np.sin(2*u),
                     (1+.12*s)*np.cos(u)+.06*np.cos(3*u),
                     .06*np.cos(2*u)-.02*s*s*np.sin(u)),axis=-1)
        Xss=np.stack((zero,zero,.04*np.cos(u)+zero),axis=-1)
        Xst=np.stack((-.1*np.sin(u)+zero,.12*np.cos(u)+zero,-.04*s*np.sin(u)),axis=-1)
        Xtt=np.stack((-(1+.1*s)*np.cos(u)-.1*np.cos(2*u),
                      -(1+.12*s)*np.sin(u)-.18*np.sin(3*u),
                      -.12*np.sin(2*u)-.02*s*s*np.cos(u)),axis=-1)
        bb=1+.07*np.cos(3*u)+.03*s
        return np.stack((X,Xs,Xt,Xss,Xst,Xtt),axis=1),bb
    rng=np.random.default_rng(263244)
    coeff=rng.normal(size=(basis.nb,basis.na))*2e-4
    linear=stream.StreamingLinearized(basis,nodes,weights,background,coeff,N,block=4)
    op=new.CompleteGramRightPreconditioned(linear,eta=1e-5,helper_path=generic_path,assembly_block=4)
    nr,nc,nb=len(nodes),basis.na,basis.nb;dimension=nc*nb
    u=2*np.pi*np.arange(N)/N;beta=np.zeros((N,nc,3));derivative=np.zeros_like(beta)
    for a,k in enumerate(basis.pm):
        beta[:,a,0]=np.cos(k*u);beta[:,a,1]=np.sin(k*u)
        derivative[:,a,0]=-k*np.sin(k*u);derivative[:,a,1]=k*np.cos(k*u)
    for a,k in enumerate(basis.zm,start=len(basis.pm)):
        beta[:,a,2]=np.cos(k*u);derivative[:,a,2]=-k*np.sin(k*u)
    xs,xt,bb=linear.Xs,linear.Xt,linear.bb
    A=np.zeros((nr,N,3,nc));B=np.zeros_like(A)
    A[:,:,0]=2*np.einsum('suc,uac->sua',xs,beta)
    A[:,:,1]=np.sqrt(2)*np.einsum('suc,uac->sua',xt,beta)/bb[:,:,None]
    B[:,:,1]=np.sqrt(2)*np.einsum('suc,uac->sua',xs,derivative)/bb[:,:,None]
    B[:,:,2]=2*np.einsum('suc,uac->sua',xt,derivative)/(bb*bb)[:,:,None]
    dense=(np.einsum('si,sura->suria',linear.B1.toarray(),A)+
           np.einsum('si,sura->suria',linear.B0.toarray(),B))*linear.weight[:,:,None,None,None]
    J=dense.reshape(nr*N*3,dimension);H=J.T@J;assembled=dense_band(op.blocks.normal_band)
    S2=lm.h2_bands(linear)
    # Independent direct derivative rows in Cartesian coordinates.
    B0,B1,B2=[b.toarray() for b in basis.matrices(nodes)]
    second=np.zeros_like(beta)
    for a,k in enumerate(basis.modes):second[:,a]=-int(k)**2*beta[:,a]
    components=[np.einsum('si,uac->sucia',B2,beta),np.sqrt(2)*np.einsum('si,uac->sucia',B1,derivative),
        np.einsum('si,uac->sucia',B0,second),np.einsum('si,uac->sucia',B1,beta),
        np.einsum('si,uac->sucia',B0,derivative),.1*np.einsum('si,uac->sucia',B0,beta)]
    R=np.concatenate([(v*np.sqrt(weights[:,None,None,None,None]/N)).reshape(nr*N*3,dimension) for v in components])
    expected_S=R.T@R
    packed_S=np.zeros_like(op.blocks.normal_band);lm.add_h2(packed_S,S2,1.)
    actual_S=dense_band(packed_S)
    grad=J.T@linear.residual.ravel();lam=3e-4
    direct,factor,scale,fact=lm.factor_solve(op.blocks.normal_band,S2,lam,grad.reshape(nb,nc))
    expected=np.linalg.solve(H+lam*expected_S,-grad)
    Jraw,JTraw=lm.raw_ops(new,linear)
    actual_normal=JTraw(Jraw(direct)+linear.residual.ravel())+lam*lm.apply_h2(S2,direct)
    screen=lm.derivative_control_bounds(basis,coeff,T)
    checks={'H2_band_relative_error':rel(actual_S,expected_S),
        'H2_operator_relative_error':rel(lm.apply_h2(S2,coeff).ravel(),expected_S@coeff.ravel()),
        'actual_regularized_normal_relative_error':float(np.linalg.norm(actual_normal)/np.linalg.norm(grad)),
        'dense_to_banded_physical_direction_relative_error':rel(direct.ravel(),expected),
        'minimum_H2_eigenvalue':float(np.linalg.eigvalsh(expected_S)[0]),
        'nonzero_off_channel_Gram_fraction':float(np.linalg.norm(H-np.diag(np.diag(H)))/np.linalg.norm(H))}
    for k,v in checks.items():
        if k.endswith('relative_error') and v>2e-10:raise ArithmeticError(k+' '+str(v))
    if checks['minimum_H2_eigenvalue']<=0:raise ArithmeticError('Nonpositive H2')
    result={'schema':'2ecf-M12-H2-direct-LM-nonzero-finite-fixture-v1','script_sha256':sha(__file__),
        'LM_source_sha256':sha(Path(lm.__file__)),'complete_Gram_source_sha256':sha(args.consumer),
        'nonzero_coefficients':int(np.count_nonzero(coeff)),'unknowns':dimension,'actual_rows':J.shape[0],
        'complete_Gram_rows_and_all_cross_channels':True,'increment_only_regularization':True,
        'checks':checks,'control_screen':screen,'factor':fact,'all_checks_passed':True,'actual_exit':0,
        'actual_M12_whole_half_solve_performed':False,'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2,allow_nan=False))
if __name__=='__main__':main()
