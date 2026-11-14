#!/usr/bin/env python3
"""Exact dyadic nodal choice and joint time/angle Parseval error transport.

The chosen nodes define a new finite interpolation polynomial.  The true
node error, including real-parameter interval width, is paid in its full
normalized l2 norm before any transform. No coefficient is declared exact
from a ball and no analytic alias or omitted coefficient is suppressed.
"""
from fractions import Fraction
import numpy as np
from flint import arb,acb
from fourfold_forward_density_pipeline_Q1024_v3 import dyadic_midpoint
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb


def joint_circle_midpoint_l2(sampler,N,Nt,m,rho,callback,*,bits=160):
    if Nt<2 or Nt%2 or not 0<m<=Nt:
        raise ValueError("invalid actual time DFT dimensions")
    rho=arb(rho)
    if not rho>0 or not rho.is_exact():
        raise ValueError("an exact positive time-circle radius is required")
    values=None;squares=None;orders=None
    for j in range(Nt//2+1):
        u=acb(rho) if j==0 else(acb(-rho) if j==Nt//2
            else rho*acb(0,2*arb.pi()*j/Nt).exp())
        sampled,timing=sampler(u,N)
        if sampled.ndim!=2 or sampled.shape[0]!=N or any(not z.is_finite() for z in sampled.flat):
            raise ValueError("invalid true parameter sample")
        if orders is None:
            orders=sampled.shape[1];values=np.empty((Nt,N,orders),object)
            squares=[arb(0)for _ in range(orders)]
        if sampled.shape[1]!=orders:
            raise ValueError("parameter source count changed between nodes")
        real_time=j in (0,Nt//2);multiplicity=1 if real_time else 2
        local=[arb(0)for _ in range(orders)]
        for k in range(N):
            for order in range(orders):
                z=sampled[k,order]
                if real_time and not z.imag.contains(0):
                    raise ValueError("the actual real-time field is not enclosed as real")
                chosen=acb(dyadic_midpoint(z.real,bits),
                           arb(0) if real_time else dyadic_midpoint(z.imag,bits))
                error=abs(z-chosen).upper()
                local[order]+=error**2
                values[j,k,order]=chosen
                if not real_time:
                    values[Nt-j,k,order]=chosen.conjugate()
        for order in range(orders):
            squares[order]+=multiplicity*local[order]
        callback(dict(time_node=j,exact_dyadic_nodal_choices=True,
            normalized_angular_RMS_errors=[ball_record((v/N).sqrt().upper())for v in local],
            **timing))
    result=np.empty((orders,m,N),object)
    for order in range(orders):
        for k in range(N):
            transformed=acb.dft(list(values[:,k,order]))
            for i in range(m):
                result[order,i,k]=transformed[i]/(Nt*rho**i)
    rms=[(v/(Nt*N)).sqrt().upper() for v in squares]
    return result,rms


def joint_retained_rectangle_error(rms,m,K,rho,strip,*,frequency_scale=1,time_radius=1):
    """Full finite weighted l1 consequence of the normalized 2D l2 bound."""
    rms,rho,s,r=map(arb,(rms,rho,strip,time_radius))
    if not rms>=0 or not rho>0 or not s>=0 or not r>=0 or m<1 or K<0:
        raise ValueError("invalid joint DFT error parameters")
    temporal=sum(((r/rho)**(2*i)for i in range(m)),arb(0))
    angular=arb(1)+2*sum(((2*frequency_scale*k*s).exp()for k in range(1,K+1)),arb(0))
    return (rms*(temporal*angular).sqrt()).upper()
