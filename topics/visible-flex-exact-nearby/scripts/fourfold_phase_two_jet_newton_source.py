#!/usr/bin/env python3
"""R117 actual Newton source using correlated two-jets of the R33 candidate.

This initial-source producer keeps the complete primitive Fourier remainder,
forms the small nonmean metric defect before taking absolute values, and uses
R117 (117.23). All angular cells cover the entire real physical circle.
Each radial domain is either an explicitly named point or one exact scalar
germ. Its output does not certify an unlisted radial interval, a strong inverse,
an analytic strip, an updated Newton neighborhood, or convergence.

The target diag(mean_theta(|F_r|^2),a^2) is chosen for the initial R33 object.
It must be frozen during a later Newton iteration. This script must not be
reused on an updated surface while silently redefining that target.

Written during an unavailable native executor. Native execution, including
an AST/import check, must be reported separately.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_correlated_curvature import (
    CorrelatedCurvature, Polynomial, dot, cross, sqrt_box_arb,
    box_abs_upper, range_record, sha)
from fourfold_phase_metric_defect import save, record
from fourfold_phase_cap_scaled_body import common_cells
from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_bulk_interval import real_interval
from fourfold_phase_beta_bulk_box import Box, CBox, zeros, arb_box, square_box

def clone_coefficient(c):
    return CBox(Box(c.real.lo.copy(),c.real.hi.copy()),
                Box(c.imag.lo.copy(),c.imag.hi.copy()))

def nonmean(poly, exact_zero_mean=False):
    """The nonmean projection is a contraction in the COMPLETE Fourier A0 norm."""
    if exact_zero_mean and not poly.mean().contains(0):
        raise ValueError("structural zero angular mean is not enclosed")
    c=clone_coefficient(poly.c);c[0]=0
    return Polynomial(c,poly.error,poly.degree,poly.fft)

def intersect(a,b,name):
    lo,hi=np.maximum(a.lo,b.lo),np.minimum(a.hi,b.hi)
    if np.any(lo>hi):raise ValueError("inconsistent exact identity: "+name)
    return Box(lo,hi)

def inverse2(a,det):
    if not np.all(det.lo>0) or not np.all(a[0][0].lo>0):
        raise ValueError("positive definite two-metric unresolved")
    return [[a[1][1]/det,-a[0][1]/det],
            [-a[1][0]/det,a[0][0]/det]]

def trace2(a,inv):
    return sum((inv[i][j]*a[i][j] for i in range(2) for j in range(2)),Box(0.))

def bilinear(a,x,y):
    return sum((a[k][l]*x[k]*y[l] for k in range(2) for l in range(2)),Box(0.))

def inner2(a,b,inv):
    return sum((inv[i][k]*inv[j][l]*a[i][j]*b[k][l]
                for i in range(2) for j in range(2)
                for k in range(2) for l in range(2)),Box(0.))

def nonnegative_root_upper(value):
    endpoint=float(np.max(value.hi))
    if not math.isfinite(endpoint) or endpoint<0:
        raise ValueError("nonnegative tensor norm upper bound unresolved")
    return arb(endpoint).sqrt().upper()

def norm3_upper(a,inv):
    value=sum((inv[i][u]*inv[j][v]*inv[k][w]*a[i][j][k]*a[u][v][w]
               for i in range(2) for j in range(2) for k in range(2)
               for u in range(2) for v in range(2) for w in range(2)),Box(0.))
    return nonnegative_root_upper(value)

class TwoJetNewtonSource(CorrelatedCurvature):
    def first_two_jets(self,radial):
        # The existing fixed-candidate primitive constructor also returns
        # higher unused jets. No third geometric derivative or its error
        # is used in the source below.
        P,a=self.unit_finite_data(radial)
        _,_,a,z=self.last_scalar
        F=[]
        for j in range(3):
            v=zeros((self.nodes,3))
            for h in range(j+1):
                v=v+math.comb(j,h)*a[j-h]*P[h]
            v[0,0]=v[0,0]+a[j];v[0,2]=v[0,2]+z[j]
            F.append(v)
        frequency=np.asarray(self.frequency)
        Y=[]
        for j in range(2):
            v=F[j]*CBox(0.,Box(frequency[:,None]))
            v[:,0]=v[:,0]-F[j][:,1]
            v[:,1]=v[:,1]+F[j][:,0]
            Y.append(v)
        tail=self.unit_tail_errors(radial,self.metric_tail_strip)[0]
        EF=[]
        for j in range(3):
            row=[]
            for q in range(3):
                bound=arb(0)
                for h in range(j+1):
                    primitive=(math.factorial(h)/self.tail_radius**h
                        *math.factorial(q)*(4/self.metric_tail_strip)**q*tail)
                    coefficient=arb(float(np.max(a[j-h].magnitude_upper()))).upper()
                    bound+=math.comb(j,h)*coefficient*primitive
                row.append(bound.upper())
            EF.append(row)
        EY=[(EF[j][0]+EF[j][1]).upper() for j in range(2)]
        return F,Y,a,EF,EY,tail

    def source_budget(self,left,right,cap_ground):
        radial=acb(real_interval(left,right))
        FF,YY,a,EF,EY,tail=self.first_two_jets(radial)
        F=[[self.lift(FF[j][:,k],EF[j][0]) for k in range(3)]
           for j in range(3)]
        Y=[[self.lift(YY[j][:,k],EY[j]) for k in range(3)]
           for j in range(2)]
        frequency=np.asarray(self.frequency)
        zz=YY[0]*CBox(0.,Box(frequency[:,None]))
        zz[:,0]=zz[:,0]-YY[0][:,1]
        zz[:,1]=zz[:,1]+YY[0][:,0]
        ezz=(EF[0][2]+2*EF[0][1]+EF[0][0]).upper()
        Z=[self.lift(zz[:,k],ezz) for k in range(3)]
        zero=F[0][0].coerce(0)
        first=[F[1],Y[0]]
        second=[[F[2],Y[1]],[Y[1],Z]]
        aa=[]
        for value in a[:3]:
            q=value.to_acb()
            if not q.imag.contains(0):raise ValueError("radius jet is not real")
            aa.append(q.real)
        if not aa[0]>0:raise ValueError("positive physical radius unresolved")
        a2=zero.coerce(aa[0]*aa[0])
        Epoly=dot(F[1],F[1]);E1poly=2*dot(F[1],F[2])
        E,E1=Epoly.mean(),E1poly.mean()
        if not E>0:raise ValueError("positive target radial metric unresolved")
        K0=-aa[2]/(aa[0]*E)+aa[1]*E1/(2*aa[0]*E*E)
        mixed=dot(F[1],Y[0])
        # Exact R33 unit tangent identity: g_theta,theta = a^2.
        gp=[[Epoly,mixed],[mixed,a2]]
        fp=[[-nonmean(Epoly),-nonmean(mixed,True)],
            [-nonmean(mixed,True),zero]]
        # Derivative index comes first: df[k][i][j] = partial_k f_ij.
        dr_mix=dot(F[2],Y[0])+dot(F[1],Y[1])
        dt_mix=dot(Y[1],Y[0])+dot(F[1],Z)
        dfp=[
            [[-nonmean(E1poly),-nonmean(dr_mix,True)],
             [-nonmean(dr_mix,True),zero]],
            [[-nonmean(2*dot(F[1],Y[1]),True),-nonmean(dt_mix,True)],
             [-nonmean(dt_mix,True),zero]]]
        C=cross(Y[0],F[1])
        G=dot(C,C);T=dot(F[0],F[0]);S=dot(C,F[0])
        L=dot(C,F[2]);M=dot(C,Y[1]);N=dot(C,Z)
        Delta=L*N-M*M-G*G*K0
        # det(g0)-det(gamma) = a^2*f_rr + gamma_rtheta^2
        # follows from f_theta,theta=0 and f_rtheta=-gamma_rtheta.
        determinant_defect=a2*fp[0][0]+mixed*mixed
        Gmetric=Epoly*a2-mixed*mixed
        tp=[dot(F[0],first[i]) for i in range(2)]
        ff2=[[dot(F[0],second[i][j]) for j in range(2)] for i in range(2)]
        lower_conn=[[[dot(first[l],second[i][j]) for j in range(2)]
                     for i in range(2)] for l in range(2)]
        polys={"G":G,"G_metric":Gmetric,"T":T,"S":S,"L":L,"M":M,"N":N,
               "Delta":Delta,"determinant_defect":determinant_defect}
        for i in range(2):
            polys[f"t{i}"]=tp[i]
            for j in range(2):
                polys[f"g{i}{j}"]=gp[i][j]
                polys[f"f{i}{j}"]=fp[i][j]
                polys[f"FF2{i}{j}"]=ff2[i][j]
                for k in range(2):
                    polys[f"df{k}{i}{j}"]=dfp[k][i][j]
                    polys[f"conn{k}{i}{j}"]=lower_conn[k][i][j]
        if cap_ground:polys["F_z"]=F[0][2]
        boxes={key:value.angular_cells(self.curvature_angles)
               for key,value in polys.items()}
        gdet=intersect(boxes["G"],boxes["G_metric"],"cross-square = metric determinant")
        tt,ss=boxes["T"],boxes["S"]
        if not all(np.all(v.lo>0) for v in (gdet,tt,ss)):
            raise ValueError("immersion/star-shaped chart positivity unresolved")
        g=[[boxes[f"g{i}{j}"] for j in range(2)] for i in range(2)]
        f=[[boxes[f"f{i}{j}"] for j in range(2)] for i in range(2)]
        df=[[[boxes[f"df{k}{i}{j}"] for j in range(2)] for i in range(2)]
            for k in range(2)]
        t=[boxes[f"t{i}"] for i in range(2)]
        t2=[[g[i][j]+boxes[f"FF2{i}{j}"] for j in range(2)] for i in range(2)]
        gamma=inverse2(g,gdet)
        rt=sqrt_box_arb(tt)
        rho=Box(1.)/rt
        rho1=[-t[i]/(tt*rt) for i in range(2)]
        rho2=[[3*t[i]*t[j]/(square_box(tt)*rt)-t2[i][j]/(tt*rt)
               for j in range(2)] for i in range(2)]
        smetric=[[g[i][j]/tt-t[i]*t[j]/square_box(tt)
                  for j in range(2)] for i in range(2)]
        sdet=square_box(ss)/(square_box(tt)*tt)
        sinv=inverse2(smetric,sdet)
        j_u=ss/(tt*rt)
        # <U_l,U_ij> in inner products of F0,F1,F2; all large t_l*t_ij
        # terms have been cancelled algebraically before interval division.
        s_lower=[[[boxes[f"conn{l}{i}{j}"]/tt
                    -(g[l][i]*t[j]+g[l][j]*t[i]+t[l]*boxes[f"FF2{i}{j}"])/square_box(tt)
                    +2*t[l]*t[i]*t[j]/(square_box(tt)*tt)
                   for j in range(2)] for i in range(2)] for l in range(2)]
        cg=[[[sum((gamma[k][l]*boxes[f"conn{l}{i}{j}"] for l in range(2)),Box(0.))
               for j in range(2)] for i in range(2)] for k in range(2)]
        cs=[[[sum((sinv[k][l]*s_lower[l][i][j] for l in range(2)),Box(0.))
               for j in range(2)] for i in range(2)] for k in range(2)]
        bf=[[[cg[k][i][j]-cs[k][i][j] for j in range(2)] for i in range(2)]
            for k in range(2)]
        g0=[[arb_box(E),Box(0.)],[Box(0.),arb_box(aa[0]*aa[0])]]
        g0inv=[[arb_box(1/E),Box(0.)],[Box(0.),arb_box(1/(aa[0]*aa[0]))]]
        covg=[[[df[k][i][j]
                -sum((cg[m][k][i]*f[m][j]+cg[m][k][j]*f[i][m]
                      for m in range(2)),Box(0.))
                 for j in range(2)] for i in range(2)] for k in range(2)]
        dconn=[[[sum((g0inv[k][l]*(covg[i][j][l]+covg[j][i][l]-covg[l][i][j])
                      for l in range(2)),Box(0.))/2
                  for j in range(2)] for i in range(2)] for k in range(2)]
        tau=[trace2(bf[k],sinv) for k in range(2)]
        dtau=[trace2(dconn[k],sinv) for k in range(2)]
        q=bilinear(f,tau,tau)+2*bilinear(g0,tau,dtau)+bilinear(g0,dtau,dtau)
        for i in range(2):
            for j in range(2):
                for u in range(2):
                    for v in range(2):
                        bi=[bf[k][i][j] for k in range(2)]
                        bu=[bf[k][u][v] for k in range(2)]
                        di=[dconn[k][i][j] for k in range(2)]
                        du=[dconn[k][u][v] for k in range(2)]
                        q=q-sinv[i][u]*sinv[j][v]*(
                            bilinear(f,bi,bu)+2*bilinear(g0,bi,du)+bilinear(g0,di,du))
        zdiff=[]
        for i in range(2):
            z=sum((f[i][k]*tau[k]+g0[i][k]*dtau[k] for k in range(2)),Box(0.))
            z=z-sum((sinv[j][l]*(f[k][l]*bf[k][i][j]+g0[k][l]*dconn[k][i][j])
                     for j in range(2) for l in range(2) for k in range(2)),Box(0.))
            zdiff.append(z)
        hrho=[[rho2[i][j]-sum((cs[k][i][j]*rho1[k] for k in range(2)),Box(0.))
               for j in range(2)] for i in range(2)]
        # This whole expression is rational in T. Avoid a second independent
        # enclosure of rho^2 and rho*rho_i in the actual source.
        hf=[[8*t[i]*t[j]/(square_box(tt)*tt)-2*t2[i][j]/square_box(tt)
             +2*sum((cs[k][i][j]*t[k] for k in range(2)),Box(0.))/square_box(tt)
             for j in range(2)] for i in range(2)]
        trf=trace2(f,sinv)
        curvature=2*(arb_box(K0)*boxes["determinant_defect"]-boxes["Delta"]/gdet)/sdet
        pieces={
            "connection_and_trace":(q-2*trf)/tt,
            "correlated_curvature":curvature/tt,
            "density_gradient":-4*bilinear(sinv,t,zdiff)/square_box(tt),
            "density_hessian":inner2(hf,f,sinv),
            "density_trace":-trace2(hf,sinv)*trf}
        compatibility=sum(pieces.values(),Box(0.))
        source=-compatibility/2
        material=j_u*source
        covs=[[[df[k][i][j]
                -sum((cs[m][k][i]*f[m][j]+cs[m][k][j]*f[i][m]
                      for m in range(2)),Box(0.))
                 for j in range(2)] for i in range(2)] for k in range(2)]
        f0=nonnegative_root_upper(inner2(f,f,sinv))
        f1=norm3_upper(covs,sinv)
        rho_norms=[box_abs_upper(rho),
                   nonnegative_root_upper(bilinear(sinv,rho1,rho1)),
                   nonnegative_root_upper(inner2(hrho,hrho,sinv))]
        R1=[t[i]/rt for i in range(2)]
        R2=[[t2[i][j]/rt-t[i]*t[j]/(tt*rt)
             -sum((cs[k][i][j]*R1[k] for k in range(2)),Box(0.))
             for j in range(2)] for i in range(2)]
        R_norms=[box_abs_upper(rt),
                 nonnegative_root_upper(bilinear(sinv,R1,R1)),
                 nonnegative_root_upper(inner2(R2,R2,sinv))]
        # Covariant two-jet of U:(material,g0)->(sphere,sigma).
        # Its coordinate coefficients are Gamma_s-Gamma_0 = -(BF+D).
        hu=[[[bf[k][i][j]+dconn[k][i][j] for j in range(2)]
             for i in range(2)] for k in range(2)]
        L1=nonnegative_root_upper(trace2(smetric,g0inv))
        L2s=sum((smetric[k][l]*g0inv[i][u]*g0inv[j][v]*hu[k][i][j]*hu[l][u][v]
                 for k in range(2) for l in range(2)
                 for i in range(2) for j in range(2)
                 for u in range(2) for v in range(2)),Box(0.))
        L2=nonnegative_root_upper(L2s)
        composition=max(arb(1),L1,(L1*L1+L2).upper())
        all_arrays=[source,material]+list(pieces.values())
        if not all(np.all(np.isfinite(v.lo)) and np.all(np.isfinite(v.hi)) for v in all_arrays):
            raise ValueError("nonfinite source enclosure")
        row=dict(
            exact_radial_interval=list(map(str,(left,right))),
            exact_scalar_germ=list(map(str,self.cell)),
            whole_real_angular_circle=True,angular_cells=self.curvature_angles,
            physical_angular_half_width=record(arb.pi()/(4*self.curvature_angles)),
            frozen_initial_target="diag(mean_theta(|F_r|^2),a^2); no later target reset",
            target_radial_metric_0_1=list(map(record,(E,E1))),target_K0=record(K0),
            spherical_Newton_scalar_source_C0_upper=record(box_abs_upper(source)),
            material_P_volume_source_C0_upper=record(box_abs_upper(material)),
            spherical_compatibility_C0_upper=record(box_abs_upper(compatibility)),
            complete_source_piece_C0_upper={k:record(box_abs_upper(v)) for k,v in pieces.items()},
            metric_defect_spherical_C0_C1=list(map(record,(f0,f1))),
            rho_spherical_derivative_norms_0_2=list(map(record,rho_norms)),
            reciprocal_rho_spherical_derivative_norms_0_2=list(map(record,R_norms)),
            material_target_to_sphere_map_two_jet=dict(
                first_derivative_Hilbert_Schmidt_upper=record(L1),
                second_covariant_derivative_Hilbert_Schmidt_upper=record(L2),
                ambient_C2_composition_factor_upper=record(composition),
                convention="max(1,L1,L1^2+L2); material derivatives use the fixed target g0 connection"),
            radial_projection_density=range_record(j_u),
            geometric_chart_ranges={k:range_record(v) for k,v in (
                ("G",gdet),("T",tt),("S",ss),("det_s",sdet))},
            correlated_Delta_A0_upper=record(Delta.norm()+Delta.error),
            determinant_defect_A0_upper=record(determinant_defect.norm()+determinant_defect.error),
            complete_primitive_A_sigma_error=record(tail),
            complete_polynomial_A0_remainders={k:record(v.error) for k,v in polys.items()},
            exact_finite_support_degrees={k:v.degree for k,v in polys.items()},
            full_mean_retained=True,
            limitations=[
                "This is the initial R33 candidate with its explicitly chosen target, at exactly the listed radial domain.",
                "The entire real theta circle and affine parameter interval are enclosed; no complex angular strip is claimed.",
                "The P volume density is j_u times the spherical source. Further ground-state, canonical, and strong Sobolev transformations are not free.",
                "No corrected-operator residual, strong inverse, nonlinear neighborhood, whole closed-surface coverage or convergence is certified."])
        if cap_ground:
            fz=boxes["F_z"]
            if not np.all(fz.lo>0):
                raise ValueError("requested positive vertical cap ground state unresolved")
            ground=fz/rt
            row["vertical_ground_state"]=range_record(ground)
            row["grounded_divergence_volume_source_C0_upper"]=record(box_abs_upper(ground*material))
            row["grounded_source_convention"]="Y_z*P(Y_z*v)=div(Y_z^2*A*grad v); source Y_z*j_u*(-C(rho^2 f)/2). The separate fixed-type operator correction is retained elsewhere."
        return row

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--half-width",type=Fraction,default=Fraction(1,10**9))
    p.add_argument("--nodes",type=int,default=512)
    p.add_argument("--angles",type=int)
    p.add_argument("--points",type=Fraction,nargs="+")
    p.add_argument("--left",type=Fraction);p.add_argument("--right",type=Fraction)
    p.add_argument("--cap-ground",action="store_true")
    p.add_argument("--bits",type=int,default=192)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec,ctx.cap=args.bits,4
    if args.half_width<0:raise ValueError("nonnegative parameter half-width required")
    if args.nodes<=0 or args.nodes&(args.nodes-1):raise ValueError("power-of-two nodes required")
    if args.points and (args.left is not None or args.right is not None):
        raise ValueError("choose radial points or one interval, not both")
    started=time.monotonic()
    definition,_,_,delta=load_definition(args.object)
    target=TwoJetNewtonSource(args.object,args.half_width,args.nodes,args.angles)
    common=common_cells(target)
    domains=[(v,v) for v in args.points] if args.points else [(args.left,args.right)]
    if any(a is None or b is None or a>b for a,b in domains):
        raise ValueError("supply points or a valid continuous interval")
    doc=dict(kind="actual_R117_correlated_two_jet_Newton_source",complete=False,
        full_closed_surface_source_complete=False,full_strong_inverse_complete=False,
        updated_neighborhood_complete=False,nonlinear_family_complete=False,
        source_sha256=sha(__file__),object_path=str(args.object),object_sha256=sha(args.object),
        origin_sha256=definition["origin_inputs"]["sha256"],
        direction_sha256=definition["direction"]["sha256"],
        exact_center=str(delta),exact_half_width=str(args.half_width),
        exact_parameter_interval=[str(delta-args.half_width),str(delta+args.half_width)],
        primitive_nodes=args.nodes,product_grid=target.product_grid,
        angular_cells=target.curvature_angles,bits=args.bits,rows=[])
    save(args.out,doc)
    for left,right in domains:
        index=min(len(common)-2,bisect_right(common,(left+right)/2)-1)
        span=common[index:index+2]
        if not span[0]<=left<=right<=span[1]:
            raise ValueError("requested radial interval crosses an exact common scalar germ")
        target.set_cell(*span)
        row=target.source_budget(left,right,args.cap_ground)
        doc["rows"].append(row);doc["wall_seconds"]=time.monotonic()-started
        save(args.out,doc)
        print(json.dumps(dict(r=list(map(str,(left,right))),
            spherical_source=row["spherical_Newton_scalar_source_C0_upper"],
            material_source=row["material_P_volume_source_C0_upper"],
            metric_C01=row["metric_defect_spherical_C0_C1"],
            seconds=doc["wall_seconds"])),flush=True)
    doc.update(complete=True,wall_seconds=time.monotonic()-started,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            "fourfold_phase_correlated_curvature.py","fourfold_phase_metric_defect.py",
            "fourfold_phase_cap_parameter_comparison.py","fourfold_phase_cap_scaled_body.py",
            "fourfold_phase_beta_affine.py","fourfold_phase_beta_parameter_germ.py",
            "fourfold_phase_beta_bulk_interval.py","fourfold_phase_beta_bulk_box.py",
            "fourfold_phase_beta_interval.py","fourfold_phase_root_interval.py",
            "fourfold_phase_uniform_tail.py")})
    save(args.out,doc)

if __name__=="__main__":main()
