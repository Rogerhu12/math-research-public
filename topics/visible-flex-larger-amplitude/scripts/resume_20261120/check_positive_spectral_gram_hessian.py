#!/usr/bin/env python3
"""One small independent point-Hessian/factor/native-RHS verification."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


ROOT=Path(__file__).resolve().parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def relative(a,b):
    return float(np.linalg.norm(np.asarray(a)-np.asarray(b))/max(1.e-300,np.linalg.norm(a),np.linalg.norm(b)))


def independent_polynomial_gradient(r,p):
    E=np.stack((np.stack((r[...,0],r[...,1]),axis=-1),
                np.stack((r[...,1],r[...,2]),axis=-1)),axis=-2)
    Q=(E@E+p.epsilon**2*np.eye(2))/p.scale**2
    W=np.broadcast_to(np.eye(2),E.shape).astype(E.dtype).copy()
    for _ in range(p.k-1):W=W@Q
    H=.5*(E@W+W@E)
    gradient=np.stack((H[...,0,0],H[...,0,1]+H[...,1,0],H[...,1,1]),axis=-1)
    return gradient,np.trace(W@Q,axis1=-2,axis2=-1)


def main():
    output=ROOT/'positive-spectral-hessian-small-check.json'
    if output.exists():raise FileExistsError('Preserve the one completed verification')
    old=load('hessian_check_R660',ROOT/'positive_spectral_gram_weights.py')
    new=load('hessian_check_R664',ROOT/'positive_spectral_gram_hessian.py')
    p=old.Parameters(p=8,epsilon=.001,scale=.05)
    rng=np.random.default_rng(20261120664)
    r=.02*rng.normal(size=(3,4,3))
    r[0,0]=[0.,0.,0.]
    r[0,1]=[.02,0.,.02]
    r[0,2]=[-.02,0.,-.02]
    r[0,3]=[.02,1.e-15,.02+2.e-15]
    blocks=new.HessianBlocks(r,p)
    v=rng.normal(size=r.shape);w=rng.normal(size=r.shape)
    h=1.e-30
    cg,cl=independent_polynomial_gradient(r+1j*h*v,p)
    actual=blocks.apply(v);expected=cg.imag/h
    expected_gradient,_=independent_polynomial_gradient(r,p)
    primitive=new.primitive_gradient(r,p)
    old_gradient=old.Blocks(r,p).apply(r)
    point_errors=[]
    for a,b in zip(actual.reshape(-1,3),expected.reshape(-1,3)):
        point_errors.append(relative(a,b))
    adj_left=float(np.sum(blocks.whiten(v)*w))
    adj_right=float(np.sum(v*blocks.whiten(w,transpose=True)))
    rhs=blocks.inverse_transpose(primitive)
    inverse_residual=blocks.whiten(rhs,transpose=True)
    J=rng.normal(size=(3,4,3,7));pw=.2+rng.random((3,4))
    normal,gradient=blocks.normal_and_gradient(J,r,pw)
    eye=np.broadcast_to(np.eye(3),r.shape[:-1]+(3,3))
    L=blocks.apply_columns(eye)
    explicit_normal=np.einsum('abri,abrs,absj,ab->ij',J,L,J,pw)
    explicit_gradient=np.einsum('abri,abr,ab->i',J,expected_gradient,pw)
    direction=rng.normal(size=7)
    jv=np.einsum('...ri,i->...r',J,direction)
    cs_gradient=independent_polynomial_gradient(r+1j*h*jv,p)[0].imag/h
    factor=p.k/p.scale**2
    hessian_quadratic=2*factor*float(direction@normal@direction)
    cs_quadratic=2*factor*float(np.sum(pw[...,None]*jv*cs_gradient))

    class Native:
        P,N,free_size=3,4,7
        multiplicity=np.array([2.,4.,4.,2.])
        full_N=float(multiplicity.sum())
        def __init__(self):self.sqrt=np.sqrt(self.multiplicity)[None,:,None]
        def residual(self,x):return (self.sqrt*(r+np.einsum('...ri,i->...r',J,x))).ravel()
        def unweight(self,z):return np.asarray(z).reshape(3,4,3)/self.sqrt
        def jvp(self,x,d):return (self.sqrt*np.einsum('...ri,i->...r',J,d)).ravel()
        def vjp(self,x,z):return np.einsum('abri,abr->i',J,self.sqrt*np.asarray(z).reshape(3,4,3))

    native=Native();radial=np.array([.2,.4,.7])
    bridge=new.NativeLinearization(native,np.zeros(7),radial,p,spectral_module=old)
    native_weights=radial[:,None]*native.multiplicity[None,:]
    native_normal,native_gradient=blocks.normal_and_gradient(J,r,native_weights)
    result=dict(schema='one-small-independent-positive-residual-hessian-check-v1',
        source_sha256=sha(ROOT/'positive_spectral_gram_hessian.py'),
        probe_source_sha256=sha(__file__),R660_source_sha256=sha(ROOT/'positive_spectral_gram_weights.py'),
        parameters=p.as_dict(),seed=20261120664,point_shape=list(r.shape),columns=7,
        cases='zero, positive and negative repeated eigenvalue, near-repeat, mixed random full blocks',
        point_hessian_complex_step_relative_error=relative(actual,expected),
        maximum_point_relative_error=max(point_errors),
        primitive_gradient_independent_polynomial_error=relative(primitive,expected_gradient),
        primitive_gradient_R660_error=relative(primitive,old_gradient),
        true_phi_first_derivative_error=relative(2*factor*np.sum(primitive*v,axis=-1),cl.imag/h),
        factor_adjoint_relative_error=relative(adj_left,adj_right),
        inverse_transpose_true_gradient_rhs_error=relative(inverse_residual,primitive),
        coarse_normal_relative_error=relative(normal,explicit_normal),
        coarse_true_gradient_relative_error=relative(gradient,explicit_gradient),
        coarse_second_directional_derivative_error=relative(hessian_quadratic,cs_quadratic),
        native_normal_relative_error=relative(bridge.normal(direction),native_normal@direction),
        native_true_gradient_rhs_error=relative(bridge.gradient,native_gradient),
        raw_block_minimum_eigenvalue=float(np.linalg.eigvalsh(L).min()),
        coarse_normal_minimum_eigenvalue=float(np.linalg.eigvalsh(normal).min()),
        metadata=blocks.metadata(),normal_is_full_x_hessian=False,
        no_actual_closed_candidate_rerun=True,numerical_check_not_outward_certificate=True)
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));print('REPORT_SHA256',sha(output))


if __name__=='__main__':main()
