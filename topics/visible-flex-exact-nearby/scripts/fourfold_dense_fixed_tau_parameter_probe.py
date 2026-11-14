#!/usr/bin/env python3
"""Floating check of the exact fixed-tau parameter-reference residual identity.

The saved rows are Y,L,Z, with Z the fixed-x parameter reference. For any
constant d, zref=Z+t_p sin(tau)*v+exp(L)*d. Both the directly differentiated
residual and the cancelled formula are evaluated on actual saved polynomials.
Endpoint velocities are deflated before differentiation. This is diagnostic,
not a continuous residual bound or a true-trajectory certificate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from fourfold_dense_residual_probe import load_reference, dense_value_and_derivative
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_affine_second_variation import ActualAffineSecondField


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dot(a, b):
    return np.sum(a*b, axis=-1)


def radial_b_w(geometry, radial, theta):
    jets = geometry.paired_jets(np.full_like(theta, radial), theta)
    _, fx, ft, fxx, fxt, ftt, _, fxxt, fxtt, _ = jets
    c = np.cross(ft, fx)
    cx = np.cross(fxt, fx)+np.cross(ft, fxx)
    m, n, G = dot(c, fxt), dot(c, ftt), dot(c, c)
    mx, nx, Gx = dot(cx, fxt)+dot(c, fxxt), dot(cx, ftt)+dot(c, fxtt), 2*dot(c,cx)
    return -mx/n+m*nx/n**2, Gx/n-G*nx/n**2


def quotient_tau(field, tau):
    """Analytic tau derivative of Q, with root deflation in the collar."""
    sine, cosine = float(np.sin(tau)), float(np.cos(tau))
    s, t = abs(sine), field.root
    if s < .999:
        _, K, _ = field.target_jets(t*s)
        qs = (-t*K[1,0]*(1-s*s)-2*s*K[0,0])/(1-s*s)**2
    else:
        points, weights = leggauss(field.root_quadrature)
        I, Is = 0., 0.
        for u, weight in zip((points+1)/2, weights/2):
            _, K, _ = field.target_jets(t*(1-u*(1-s)))
            I += weight*K[1,0]
            Is += weight*t*u*2*K[2,0]
        qs = t*(Is*(1+s)-I)/(1+s)**2
    return qs*np.sign(sine)*cosine


def evaluate(field, tau, state, derivative, sign, d):
    geom, t, tp = field.geometry, field.root, field.root_p
    sine, cosine = float(np.sin(tau)), float(np.cos(tau))
    radial, xtau = t*sine, t*cosine
    theta, L, Z = state
    raw = geom.principal_quantities(np.full_like(theta, radial), theta, columns=True)
    m,n,G,mt,nt,Gt,mp,np_,Gp = (raw[k] for k in (
        "m","n","G","m_theta","n_theta","G_theta",
        "m_parameter","n_parameter","G_parameter"))
    b,w = -m/n,G/n
    bt,wt = -mt/n+m*nt/n**2,Gt/n-G*nt/n**2
    bp,wp = -mp/n+m*np_/n**2,Gp/n-G*np_/n**2
    bx,wx = radial_b_w(geom, radial, theta)
    Qjets = field.q_derivatives(tau)
    Q = Qjets[0]
    sq = np.sqrt(Q)
    Qtau = quotient_tau(field, tau)
    v,vt = b+sign*w*cosine*sq,bt+sign*wt*cosine*sq
    # Chain differentiation along the actual saved reference Y. No vx with
    # a 1/sqrt(-K) factor is evaluated at either endpoint.
    v_tau = (xtau*bx+bt*derivative[0]
        +sign*((xtau*wx+wt*derivative[0])*cosine*sq
               +w*(-sine*sq+cosine*Qtau/(2*sq))))
    _, K, _ = field.target_jets(radial)
    fixed_forcing = (xtau*bp+sign*t*cosine*cosine*sq*wp
                     -sign*t*w*K[0,1]/(2*sq))
    actual = field.evaluate(tau, theta, sign)
    f,ft = xtau*v,xtau*vt
    e0,e1 = derivative[0]-f,derivative[1]-ft
    eZ = derivative[2]-ft*Z-fixed_forcing
    A,Aprime,q = tp*sine,tp*cosine,np.exp(L)
    zref = Z+A*v+q*d
    zref_tau = derivative[2]+Aprime*v+A*v_tau+q*derivative[1]*d
    direct = zref_tau-actual["f_theta"]*zref-actual["f_parameter"]
    cancelled = eZ+A*vt*e0+q*d*e1
    # This separately locates the unpaid floating near-root quotient error.
    # For the true root and exact derivatives both scalar defects vanish.
    # Do not silently subtract this diagnostic from the reported residual.
    parameter_quotient_defect = cosine*cosine*Qjets[1]+K[0,1]+A*K[1,0]
    time_quotient_defect = cosine*Qtau-2*sine*Q+t*K[1,0]
    predicted_defect = sign*w/(2*sq)*(A*time_quotient_defect-t*parameter_quotient_defect)
    return dict(direct=direct,cancelled=cancelled,zref=zref,
                e0=e0,e1=e1,eZ=eZ,A_vtheta_e0=A*vt*e0,q_d_e1=q*d*e1,
                parameter_quotient_defect=np.broadcast_to(parameter_quotient_defect,theta.shape),
                time_quotient_defect=np.broadcast_to(time_quotient_defect,theta.shape),
                predicted_quotient_identity_defect=predicted_defect,
                discrepancy_after_quotient_defect=direct-cancelled-predicted_defect,
                field_consistency=np.maximum(abs(f-actual["f"]),abs(ft-actual["f_theta"])))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object",type=Path,required=True)
    p.add_argument("--root-certificate",type=Path,required=True)
    p.add_argument("--trace",type=Path,required=True)
    p.add_argument("--incoming-branch",type=Path)
    p.add_argument("--segments",type=int,nargs="+",default=[0,1,130,274,419,548,549])
    p.add_argument("--rays",type=int,default=8)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args()
    arrays=load_reference(args.trace)
    meta=json.loads(str(arrays["metadata"]));identity=meta["identity"]
    if identity["source_sha256"]!=digest(args.object) or identity["root_certificate_sha256"]!=digest(args.root_certificate):
        raise ValueError("reference object/root mismatch")
    if int(meta.get("first_accepted_segment",0)):
        raise ValueError("use a whole branch or its initial chunk")
    geom,_=load_exact_object(args.object,identity["quarter_nodes"])
    root=json.loads(args.root_certificate.read_text())
    field=ActualAffineSecondField(geom,root["root_center"])
    n=arrays["accepted_state"].shape[-1]
    indices=np.unique(np.floor(np.arange(args.rays)*n/args.rays).astype(int))
    incoming=np.zeros(n)
    incoming_sha=None
    if args.incoming_branch:
        previous=json.loads(args.incoming_branch.read_text())
        if (previous["identity"]["source_sha256"]!=identity["source_sha256"]
            or not np.array_equal(previous["final_angles"],arrays["accepted_state"][0,0])):
            raise ValueError("incoming branch does not meet this reference")
        incoming=np.asarray(previous["final_parameter_column"])
        incoming_sha=digest(args.incoming_branch)
    tau0=float(arrays["accepted_tau"][0])
    state0,_=dense_value_and_derivative(arrays["dense_y_old"][0],arrays["dense_F"][0],
        (tau0-arrays["dense_t_old"][0])/arrays["dense_h"][0],arrays["dense_h"][0])
    initialraw=geom.principal_quantities(np.full(n,field.root*np.sin(tau0)),state0[0])
    b0=-initialraw["m"]/initialraw["n"]
    d=(incoming-state0[2]-field.root_p*np.sin(tau0)*b0)/np.exp(state0[1])
    records=[]
    for segment in args.segments:
        if not 0<=segment<len(arrays["dense_h"]):
            raise ValueError("segment outside saved branch")
        left,right=arrays["accepted_tau"][segment:segment+2]
        for fraction in (0.,.5,1.):
            tau=float(left+(right-left)*fraction)
            state,derivative=dense_value_and_derivative(
                arrays["dense_y_old"][segment,:,indices].T,
                arrays["dense_F"][segment][:,:,indices],
                (tau-arrays["dense_t_old"][segment])/arrays["dense_h"][segment],
                arrays["dense_h"][segment])
            values=evaluate(field,tau,state,derivative,float(identity["sign"]),d[indices])
            records.append(dict(segment=int(segment),fraction=fraction,tau=tau,
                maximum_identity_discrepancy=float(np.max(abs(values["direct"]-values["cancelled"]))),
                maximum_field_discrepancy=float(np.max(values["field_consistency"])),
                maximum_after_quotient_defect=float(np.max(abs(values["discrepancy_after_quotient_defect"]))),
                maximum_absolute={key:float(np.max(abs(value))) for key,value in values.items()},
                direct_per_ray=values["direct"].tolist(),cancelled_per_ray=values["cancelled"].tolist()))
    last=len(arrays["dense_h"])-1
    endstate=arrays["accepted_state"][-1]
    endraw=geom.principal_quantities(np.full(n,field.root*np.sin(arrays["accepted_tau"][-1])),endstate[0])
    reconstructed=(endstate[2]+field.root_p*np.sin(arrays["accepted_tau"][-1])*(-endraw["m"]/endraw["n"])
                   +np.exp(endstate[1])*d)
    expected=np.asarray(arrays["final_parameter_column"])+np.exp(endstate[1])*incoming
    report=dict(kind="floating_actual_dense_fixed_tau_parameter_residual_identity_probe",
        source_sha256=digest(__file__),object_sha256=digest(args.object),
        dependency_sha256={name:digest(Path(__file__).with_name(name)) for name in (
            "fourfold_dense_residual_probe.py", "fourfold_phase_symmetric_geometry.py",
            "fourfold_phase_affine_second_variation.py", "fourfold_mixed_jet_algebra.py")},
        root_certificate_sha256=digest(args.root_certificate),trace_sha256=digest(args.trace),
        incoming_branch_sha256=incoming_sha,trace_identity=identity,indices=indices.tolist(),
        root_parameter_derivative=field.root_p,
        identity="zref=Z+A*v+q*d; residual=eZ+A*v_theta*e0+q*d*e1",
        maximum_identity_discrepancy=max(row["maximum_identity_discrepancy"] for row in records),
        maximum_after_quotient_defect=max(row["maximum_after_quotient_defect"] for row in records),
        endpoint_parameter_column_reconstruction_max=float(np.max(abs(reconstructed-expected))),
        samples=records,limitations=["Floating diagnostics at selected times and rays only.",
        "No continuous parameter, time, or complex-angle bound is proved.",
        "Finite primitive, root-centre, FFT/trig and quotient quadrature errors remain unpaid.",
        "The exact identity does not make q a true Jacobian or Z a true variation."])
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:report[k] for k in ("maximum_identity_discrepancy",
        "endpoint_parameter_column_reconstruction_max")}))


if __name__=="__main__":main()
