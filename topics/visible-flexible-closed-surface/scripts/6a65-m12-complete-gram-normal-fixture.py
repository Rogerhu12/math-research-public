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
    ap.add_argument('--consumer',type=Path,default=Path(__file__).with_name('6a65-m12-complete-gram-normal-preconditioner.py'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();began=time.monotonic()
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
    S=np.zeros_like(H)
    for lower,channels in op.blocks.old_groups:
        L=np.zeros((nb,nb))
        for d in range(lower.shape[0]):
            if d<nb:
                j=np.arange(nb-d);L[j+d,j]=lower[d,:nb-d]
        for a in channels:
            indices=np.arange(nb)*nc+a;S[np.ix_(indices,indices)]=L@L.T
    P=H+op.blocks.eta*S
    eye=np.eye(dimension);right=np.column_stack([op.unpack(eye[:,i]).ravel() for i in range(dimension)])
    x=rng.normal(size=dimension);y=rng.normal(size=J.shape[0]);physical=right@x
    raw_J_error=rel(op.raw_matvec(physical),J@physical)
    raw_JT_error=rel(op.raw_transpose(y).ravel(),J.T@y)
    J_error=rel(op.matvec(x),J@right@x);JT_error=rel(op.rmatvec(y),right.T@J.T@y)
    lhs=float(np.dot(op.matvec(x),y));rhs=float(np.dot(x,op.rmatvec(y)))
    physical_gradient=J.T@y
    recovery_error=rel(op.blocks.physical_gradient(op.blocks.transpose(physical_gradient)).ravel(),physical_gradient)
    true_normal=J.T@(J@physical+linear.residual.ravel())
    normal_error=rel(op.physical_normal_residual(physical).ravel(),true_normal)
    eig=np.linalg.eigvalsh(right.T@H@right)
    off=H.copy()
    for a in range(nc):
        indices=np.arange(nb)*nc+a;off[np.ix_(indices,indices)]=0
    endpoint=max(float(np.max(abs(B@coeff))) for B in basis.matrices([0.,1.]))
    checks={'full_H_relative_error':rel(assembled,H),
        'equilibrated_P_whitening_relative_error':rel(right.T@P@right,eye),
        'physical_J_relative_error':raw_J_error,'physical_JT_relative_error':raw_JT_error,
        'right_preconditioned_J_relative_error':J_error,'right_preconditioned_JT_relative_error':JT_error,
        'adjoint_relative_error':abs(lhs-rhs)/max(np.finfo(float).tiny,abs(lhs),abs(rhs)),
        'physical_gradient_recovery_relative_error':recovery_error,
        'unregularized_physical_normal_relative_error':normal_error,
        'minimum_lambda0_normal_eigenvalue':float(eig[0]),'maximum_lambda0_normal_eigenvalue':float(eig[-1]),
        'off_channel_H_fraction':float(np.linalg.norm(off)/np.linalg.norm(H)),
        'endpoint_correction_two_jets_max':endpoint}
    for key,value in checks.items():
        if key.endswith('relative_error') and value>2e-10:raise ArithmeticError(key+' = '+str(value))
    if not (-2e-10<=eig[0]<=eig[-1]<=1+2e-10):raise ArithmeticError('lambda=0 spectrum bound failed')
    if op.blocks.receipt['alias_frequency_pairs']==0 or not np.any(basis.pm<0):
        raise ArithmeticError('Signed mode / actual discrete alias cases were not exercised')
    if checks['off_channel_H_fraction']<=.01 or endpoint!=0:
        raise ArithmeticError('Nontrivial full coupling and exact zero endpoint jets required')
    result={'schema':'6a65-M12-complete-Gram-normal-nonzero-finite-fixture-v1',
        'script_sha256':sha(__file__),'consumer_sha256':sha(args.consumer),
        'original_stream_sha256':sha(stream_path),'R244_helper_sha256':sha(generic_path),
        'seed':263244,'nonzero_coefficients':int(np.count_nonzero(coeff)),
        'columns':dimension,'physical_rows':J.shape[0],'angular_nodes':N,
        'order':order,'all_three_Gram_rows_and_all_coupled_channels':True,
        'dense_J_formed_only_for_this_small_finite_fixture':True,'checks':checks,
        'assembly':op.blocks.receipt,'all_checks_passed':True,'actual_exit':0,
        'actual_M12_whole_half_solve_performed':False,'new_refinement_improvement_claimed':False,
        'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2,allow_nan=False))
if __name__=='__main__':main()
