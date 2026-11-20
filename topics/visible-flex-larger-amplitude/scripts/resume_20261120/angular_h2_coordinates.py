#!/usr/bin/env python3
"""Positive angular-H2 transition on the complete physical-height step norm.

Every original mode stays. This is a stronger update norm, not the geometric
bending energy. The parameter nu_c is fixed before a direction is computed.
"""
import numpy as np


def make_scale(problem,base_scale_module,height_module,nu_c=24.):
    q=problem;nu_c=float(nu_c)
    if not np.isfinite(nu_c)or nu_c<1:
        raise ValueError('The declared angular transition must be finite and >=1')
    scale=base_scale_module.make_scale(q)
    frequencies=np.r_[0.,q.freq,q.freq,0.,q.freq]
    transition=np.sqrt(1+(frequencies/nu_c)**2)
    nc=q.M-q.K;na0=2*q.M+1;nai=(q.J-2)*q.n;ne=(q.J-1)*q.n
    scale[:nc]/=np.sqrt(1+(q.freq[q.K:]/nu_c)**2)
    at=nc
    scale[at:at+na0]/=transition[:na0];at+=na0
    scale[at:at+nai].reshape(q.J-2,q.n)[:]/=transition[None];at+=nai
    scale[at:at+ne].reshape(q.J-1,q.n)[:]/=transition[None];at+=ne
    scale[at:at+ne].reshape(q.J-1,q.n)[:]*=np.diff(q.mesh)[:,None]/transition[None];at+=ne
    if at!=len(scale)-1:raise ValueError('The complete integrated layout changed')
    scale[-1]=height_module.height_scale(q.S)
    if not np.isfinite(scale).all()or np.any(scale<=0):
        raise ValueError('The new complete scale must be strictly positive and finite')
    metadata=dict(nu_c=nu_c,transition='sigma_nu=sqrt(1+(nu/nu_c)^2)',
        A='1/(sqrt(w)*sqrt(1+nu^2)*sigma_nu)',
        E='1/(sqrt(h)*sqrt(1+nu^2)*sigma_nu)',
        D='sqrt(h)/(sqrt(1+nu^2)*sigma_nu)',
        core='1/((1+nu^2)*sigma_nu)',H='sqrt(7*S^3/120), composed with the unchanged physical-height A',
        squared_norm_ratio_to_previous_per_mode='1+(nu/nu_c)^2 for A/E/D and free core; H unchanged',
        low_mode_maximum_squared_ratio=float(1+(24/nu_c)**2),
        largest_squared_ratio=float(1+(q.freq[-1]/nu_c)**2),
        minimum_scale=float(scale.min()),maximum_scale=float(scale.max()),
        core_chain='A core c_nu induces R=c_nu and T=-nu*c_nu; the new core squared coefficient cost is (1+nu^2)^2*(1+nu^2/nu_c^2)*c_nu^2',
        core_angular_H2_equivalence_lower=1/nu_c**2,
        core_angular_H2_equivalence_upper=1.,
        all_original_modes_retained=True,exact_physical_bending_energy=False)
    return scale,metadata


def coarse_norm(basis,coordinates,height_map,nu_c=24.):
    """Literal new inverse(A^-1 B)/scale norm, separated by coefficient mode."""
    h=coordinates.h;w=coordinates.w
    Y,U,A=basis.node_jets[:,:,0],basis.node_jets[:,:,1],basis.node_jets[:,:,2]
    E=np.diff(U,axis=1)/h[None]-.5*(A[:,:-1]+A[:,1:])
    D=np.diff(Y,axis=1)/h[None]-.5*(U[:,:-1]+U[:,1:])
    radial=(A*w[None])@A.T+(E*h[None])@E.T+(D/h[None])@D.T
    gram=np.zeros((basis.dimension,basis.dimension));radial_index,channel=basis.pairs.T
    for j,(_,mode,_)in enumerate(basis.channels):
        ii=np.flatnonzero(channel==j);ri=radial_index[ii];nu=2*mode
        gram[np.ix_(ii,ii)]=(1+nu**2)*(1+(nu/nu_c)**2)*radial[np.ix_(ri,ri)]
    gram[-1,:]=0.;gram[:,-1]=0.;gram[-1,-1]=1/coordinates.scale[-1]**2
    diagonal=np.sqrt(np.diag(gram));normalized=gram/diagonal[:,None]/diagonal[None]
    chol=np.linalg.cholesky(normalized)
    probe=np.sin(np.arange(basis.dimension)+.125)
    literal_vector=coordinates.inverse(height_map.inverse_free(basis.free_direction(probe)),affine=False)/coordinates.scale
    literal=float(literal_vector@literal_vector);separated=float(probe@gram@probe)
    difference=abs(literal-separated)/max(1.,abs(literal))
    if difference>2e-10:
        raise ValueError('The new angular norm disagrees with the literal complete inverse')
    return diagonal,chol,dict(
        norm='||DoubleIntegrated.inverse(A^-1 B alpha, affine=False)/new_scale||^2',
        angular_squared_factor='(1+nu^2)*(1+(nu/nu_c)^2)',nu_c=nu_c,
        diagonal_min=float(diagonal.min()),diagonal_max=float(diagonal.max()),
        normalized_condition=float(np.linalg.cond(normalized)),
        separated_to_literal_probe_relative_difference=difference,
        whitening='R=diag(diagonal)^(-1) chol(normalized)^(-T); R^T G R=I',
        dimension=basis.dimension,geometry_calls=0)


def new_map_check(problem,coordinates,lift,transpose,size,seed=2026112006):
    """One check of the new diagonal indexing/full transpose and endpoints."""
    rng=np.random.default_rng(seed)
    z=rng.standard_normal(size);z/=np.linalg.norm(z)
    g=rng.standard_normal(problem.free_size);g/=np.linalg.norm(g)
    left=float(lift(z)@g);right=float(z@transpose(g))
    error=abs(left-right)/max(1e-30,abs(left),abs(right))
    raw=coordinates.scale*coordinates.project(z[:coordinates.size])
    endpoint=float(np.max(np.abs(coordinates.endpoint(raw))))
    if error>2e-9 or endpoint>2e-10:
        raise ValueError('The new angular diagonal map fails its necessary transpose/endpoint check')
    return dict(seed=seed,adjoint_left=left,adjoint_right=right,
        adjoint_relative_difference=error,endpoint_maximum=endpoint,
        scope='New positive per-mode scale and matching coarse inverse only; no repeated Gram or curvature-cotangent certificate')
