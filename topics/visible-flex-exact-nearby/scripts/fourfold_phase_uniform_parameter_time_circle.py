#!/usr/bin/env python3
"""Uniform real-parameter tube of the actual complex-time parameter sources.

The center's proved D and curvature branch domains are extended by an
explicit parameter mean-value bound. Native interval parameter jets are
then evaluated on the whole real box. No complex-parameter strip, center
g2-to-box substitution, or third-parameter derivative is assumed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, acb, ctx

from fourfold_phase_parameter_time_circle import (
    CentralParameterTarget, ParameterTimeCircleField, ParameterRootDeflation,
    majorant_complex_scalars, lower, upper,
)
from fourfold_phase_beta_parameter_germ import ParameterGermMixin
from fourfold_phase_fixed_tau_parameter_bounds import (
    sha, read, save, interval, absup, composed_norm, quotient_norm, multiply,
)
from fourfold_phase_real_parameter_forcing import normalized_total
from fourfold_phase_beta_interval import series_derivative, ball_record
from fourfold_phase_beta_bulk_interval import exact_arb, complex_pad
from fourfold_phase_unified_scalar_time_circle import complex_record
from fourfold_native_series_fft import NativeSeriesFFT


class UniformParameterTarget(CentralParameterTarget):
    def initialize_parameter(self, object_path, half_width, definition, direction, center):
        # The exact same formal scalar direction as CentralParameterTarget,
        # now with one real shared parameter interval kept through every germ.
        ParameterGermMixin.initialize_parameter(self, object_path, half_width, definition, direction, center)


def uniform_root_parameters(field, central, wide_jets_path):
    wide=read(wide_jets_path)
    if not (wide["proved"] and wide["object_sha256"]==sha(field.object_path)
            and wide["point_root_sha256"]==sha(field.root_path)):
        raise ValueError("the uniform root witness belongs to another actual family")
    lo,hi=map(Fraction,wide["exact_parameter_interval"])
    p0=central.target.parameter_center
    if not lo<=p0-field.half_width<p0+field.half_width<=hi:
        raise ValueError("requested real parameter tube leaves the proved simple-root branch")
    tpwide,tppwide=interval(wide["root_parameter_first"]),interval(wide["root_parameter_second"])
    root=central.root+arb(0,(exact_arb(field.half_width)*absup(tpwide)).upper())
    target=UniformParameterTarget(field.object_path,field.half_width,field.nodes,field.nodes,
        field.R0,field.RE,field.sigma)
    target.fourier=NativeSeriesFFT()
    target.set_cell(*map(Fraction,field.base.root_package.provenance["root_common_span"]))
    oldcap,ctx.cap=ctx.cap,7
    try:
        scale=exact_arb(Fraction(1,4096))
        budget=target.parameter_input_budget2(acb(root),field.R0,field.sigma,field.RE)
        data=target.parameter_target2(acb(root),scale,budget)
        K,Kp,Kpp=data["K"],data["Kp"],data["Kpp"]
        Kr=series_derivative(K,-scale)[0].real
        Krr=series_derivative(K,-scale,2)[0].real
        Krp=series_derivative(Kp,-scale)[0].real
        if not K[0].real.contains(0) or not Kr>0:
            raise ValueError("uniform actual simple-root box failed")
        tp=-Kp[0].real/Kr
        tpp=-(Kpp[0].real+2*Krp*tp+Krr*tp**2)/Kr
        if not tp.overlaps(tpwide) or not tpp.overlaps(tppwide):
            raise ValueError("uniform implicit jets disagree with the proved real branch")
        tp,tpp=tp.intersection(tpwide),tpp.intersection(tppwide)
        return root,tp,tpp,dict(proved=True,center_parameter_only=False,
            exact_center_parameter=str(p0),exact_parameter_half_width=str(field.half_width),
            exact_parameter_interval=[str(p0-field.half_width),str(p0+field.half_width)],
            wide_simple_root_jets_sha256=sha(wide_jets_path),
            refined_central_root=ball_record(central.root),
            actual_root_tube=ball_record(root),true_root_parameter_first=ball_record(tp),
            true_root_parameter_second=ball_record(tpp),positive_Kr=ball_record(Kr),
            full_infinite_parameter_mean=True,
            inclusion="t(p) in t(p0)+[-eta*sup_I|tprime|,eta*sup_I|tprime|]; then the actual implicit formulas are evaluated on the entire root/p box")
    finally:
        ctx.cap=oldcap


class UniformRootDeflation(ParameterRootDeflation):
    def __init__(self,field,degree=40,radius=Fraction(3,1250)):
        self.field,self.degree,self.RK=field,int(degree),exact_arb(radius)
        if degree<4 or not field.R0>field.RE>self.RK>0:
            raise ValueError("invalid uniform radial deflation domain")
        self.target=UniformParameterTarget(field.object_path,field.half_width,
            field.nodes,field.nodes,field.R0,field.RE,field.sigma)
        self.target.fourier=NativeSeriesFFT()
        self.target.set_cell(*map(Fraction,field.base.root_package.provenance["root_common_span"]))
        oldcap=ctx.cap
        try:
            ctx.cap=degree+6
            budget=self.target.parameter_input_budget2(acb(field.root),field.R0,field.sigma,field.RE)
            data=self.target.parameter_target2(acb(field.root),self.RK,budget)
            K,Kp,Kpp=data["K"],data["Kp"],data["Kpp"]
            Kr,Krr=series_derivative(K,-self.RK),series_derivative(K,-self.RK,2)
            Krp=series_derivative(Kp,-self.RK)
            totals=[K,Kp+field.tp*Kr,Kpp+2*field.tp*Krp+field.tp**2*Krr+field.tpp*Kr]
            if any(not v[0].real.contains(0) for v in totals):
                raise ValueError("uniform actual root constants are inconsistent")
            self.coefficients=[[acb((-v[j+1]/self.RK).real) for j in range(degree)] for v in totals]
            ctx.cap=7
            disk=complex_pad(acb(field.root),self.RK)
            budget=self.target.parameter_input_budget2(disk,field.R0,field.sigma,field.RE)
            data=self.target.parameter_target2(disk,arb(1),budget)
            K,Kp,Kpp=data["K"],data["Kp"],data["Kpp"]
            Kr,Krr=series_derivative(K,-1),series_derivative(K,-1,2)
            Krp=series_derivative(Kp,-1)
            self.bounds=[absup(K[0]),(absup(Kp[0])+absup(field.tp)*absup(Kr[0])).upper(),
                (absup(Kpp[0])+2*absup(field.tp)*absup(Krp[0])
                 +absup(field.tp)**2*absup(Krr[0])+absup(field.tpp)*absup(Kr[0])).upper()]
            if not all(v.is_finite() for v in self.bounds):
                raise ValueError("nonfinite uniform root disk moduli")
            self.domain=dict(radius=str(radius),degree=degree,whole_real_parameter_tube=True,
                K_total_parameter_moduli=list(map(ball_record,self.bounds)),
                a_modulus_lower=ball_record(data["a"][0].abs_lower()),
                E_modulus_lower=ball_record(data["E"][0].abs_lower()),
                all_three_exact_root_constants_removed_for_every_real_parameter=True)
        finally:
            ctx.cap=oldcap


class UniformParameterTimeCircleField(ParameterTimeCircleField):
    def __init__(self,descriptor,domain,local_root_jets,wide_root_jets,*,
                 half_width=Fraction(1,10**12),nodes=512,root_nodes=1024,
                 outer=Fraction(3),germ=-1,radial_degree=40,central=None):
        if not Fraction(half_width)>0:
            raise ValueError("positive real parameter tube required")
        central=central or ParameterTimeCircleField(descriptor,domain,local_root_jets,
            nodes=nodes,root_nodes=root_nodes,outer=outer,germ=germ,radial_degree=radial_degree)
        self.central=central
        for name in ("base","object_path","root_path","nodes","local_root_jets",
                     "outer","strip","sign","turn","R0","RE","sigma",
                     "exact_tau0","exact_h","tau0","h","cell"):
            setattr(self,name,getattr(central,name))
        self.half_width=Fraction(half_width)
        self.wide_root_jets=Path(wide_root_jets)
        self.root,self.tp,self.tpp,self.root_parameter_refinement=uniform_root_parameters(
            self,central,self.wide_root_jets)
        self.target=UniformParameterTarget(self.object_path,self.half_width,nodes,nodes,
            self.R0,self.RE,self.sigma)
        self.target.fourier=NativeSeriesFFT();self.target.set_cell(*self.cell)
        H=abs(self.h)*self.outer
        self.center=self.root*self.tau0.sin()
        self.radial_enlargement=(abs(self.root)*(abs(self.tau0.sin())*(H.cosh()-1)
                                               +abs(self.tau0.cos())*H.sinh())).upper()
        common=self.target.parameter_input_budget2(acb(self.center),self.R0+self.radial_enlargement,
            self.sigma,self.RE+self.radial_enlargement)
        self.common_budgets=[]
        for row in common:
            copy=dict(row);copy["radial_radius"],copy["E_radius"]=self.R0,self.RE
            self.common_budgets.append(copy)
        self.deflation=UniformRootDeflation(self,radial_degree) if self.turn else None
        self.moduli=self.complete_source_moduli()

    def complete_source_moduli(self):
        oldcap,ctx.cap=ctx.cap,7
        try:
            tau=complex_pad(acb(self.tau0),abs(self.h)*self.outer)
            sine,cosine=tau.sin(),tau.cos()
            radial=complex_pad(acb(self.center),self.radial_enlargement)
            geometry=majorant_complex_scalars(self.target,radial,self.strip)
            r1,r2=absup(self.tp*sine),absup(self.tpp*sine)
            D,M,W=[composed_norm(geometry[key],r1,r2) for key in ("D","M","W")]
            eta=exact_arb(self.half_width)
            Dcenter=lower(self.base.selected["D_lower"])
            Dfee=(eta*D[1]).upper()
            Dmin=(Dcenter-Dfee).lower()
            if not Dmin>0:
                raise ValueError("uniform real-parameter D extension failed")
            drift=quotient_norm(M,D,Dmin,(M[0]/Dmin).upper())
            wave=quotient_norm(W,D,Dmin,(W[0]/Dmin).upper())
            curvature=self.base.selected["curvature"]
            if self.turn:
                angle=acb(self.base.eta0)+self.base.eta1*complex_pad(acb(0),self.outer)
                Q=self.deflation.quotient_parameter_series(angle)
                qnorm=[absup(Q[j]) for j in range(3)]
                Qcenter=lower(curvature["Q_real_lower"])
                Qfee=(eta*qnorm[1]).upper()
                minimum=(Qcenter-Qfee).lower()
                if not minimum>0:
                    raise ValueError("uniform real-parameter deflated Q branch extension failed")
                square=[qnorm[0].sqrt().upper(),
                    (qnorm[1]/(2*minimum.sqrt())).upper(),
                    (qnorm[2]/(2*minimum.sqrt())+qnorm[1]**2/(8*minimum**(arb(3)/2))).upper()]
                square=[absup(angle.sin())*x for x in square]
                extra=dict(deflated_Q_normalized_parameter_bounds=list(map(ball_record,qnorm)),
                    central_Q_real_lower=ball_record(Qcenter),
                    parameter_Q_perturbation_upper=ball_record(Qfee),
                    actual_uniform_Q_real_lower=ball_record(minimum))
            else:
                data=self.target.parameter_target2(radial,arb(1),self.common_budgets)
                total=normalized_total(data["K"],data["Kp"],data["Kpp"],arb(1),
                    self.tp*sine,self.tpp*sine)
                knorm=[absup(v) for v in total]
                Kcenter=lower(curvature["minus_K_real_lower"])
                Kfee=(eta*knorm[1]).upper()
                minimum=(Kcenter-Kfee).lower()
                if not minimum>0:
                    raise ValueError("uniform real-parameter ordinary curvature branch extension failed")
                square=[knorm[0].sqrt().upper(),
                    (knorm[1]/(2*minimum.sqrt())).upper(),
                    (knorm[2]/(2*minimum.sqrt())+knorm[1]**2/(8*minimum**(arb(3)/2))).upper()]
                extra=dict(K_normalized_parameter_bounds=list(map(ball_record,knorm)),
                    central_minus_K_real_lower=ball_record(Kcenter),
                    parameter_K_perturbation_upper=ball_record(Kfee),
                    actual_uniform_minus_K_real_lower=ball_record(minimum))
            inner=[d+w for d,w in zip(drift,multiply(square,wave))]
            rtau=[absup(self.root*cosine),absup(self.tp*cosine),absup(self.tpp*cosine)/2]
            result=multiply(rtau,inner);result[2]*=2
            if not all(v.is_finite() for v in result):
                raise ValueError("nonfinite actual uniform parameter source moduli")
            return dict(proved=True,whole_real_parameter_tube=True,
                f=ball_record(result[0]),fp=ball_record(result[1]),fpp=ball_record(result[2]),
                central_D_lower=ball_record(Dcenter),parameter_D_perturbation_upper=ball_record(Dfee),
                actual_uniform_D_lower=ball_record(Dmin),
                tangent_imaginary_bound=ball_record(geometry["tangent_imaginary_bound"]),
                parameter_mean_value_used_only_on_real_parameter_lines=True,**extra)
        finally:
            ctx.cap=oldcap

    def identity(self):
        result=super().identity()
        result.update(kind="actual_uniform_real_parameter_time_circle_sources",
            source_sha256=sha(__file__),actual_center_parameter_only=False,
            whole_real_parameter_tube=True,exact_parameter_half_width=str(self.half_width),
            exact_parameter_interval=list(map(str,self.target.parameter_interval)),
            wide_root_jets_sha256=sha(self.wide_root_jets),
            central_parameter_source_sha256=sha(Path(__file__).with_name("fourfold_phase_parameter_time_circle.py")),
            uniform_root_parameter_refinement=self.root_parameter_refinement)
        result["limitations"]=[
            "A fixed selected analytic spline germ; actual crossings still require parameter cap fees.",
            "The entire real parameter interval is included, but no complex parameter domain is claimed.",
            "Sampling is not a finite Fourier/time or density certificate without its complete reconstruction fees."]
        return result


def main():
    p=argparse.ArgumentParser(description=__doc__);base=Path("data/phase_ring_continuation")
    p.add_argument("--descriptor",type=Path,default=base/"step5_retargeted_reference/descriptor.json")
    p.add_argument("--domain",type=Path,required=True)
    p.add_argument("--local-root-jets",type=Path,default=base/"type_fixed_step02_d5_step5_local_parameter_root_jets_h1e14.json")
    p.add_argument("--wide-root-jets",type=Path,default=base/"type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json")
    p.add_argument("--half-width",type=Fraction,default=Fraction(1,10**12))
    p.add_argument("--primitive-nodes",type=int,default=512);p.add_argument("--root-nodes",type=int,default=1024)
    p.add_argument("--angles",type=int,default=512);p.add_argument("--bits",type=int,default=256)
    p.add_argument("--outer",type=Fraction,default=Fraction(3));p.add_argument("--radial-degree",type=int,default=40)
    p.add_argument("--out",type=Path,required=True);args=p.parse_args()
    ctx.prec,ctx.cap=args.bits,7;started,cpu=time.monotonic(),time.process_time()
    model=UniformParameterTimeCircleField(args.descriptor,args.domain,args.local_root_jets,
        args.wide_root_jets,half_width=args.half_width,nodes=args.primitive_nodes,
        root_nodes=args.root_nodes,outer=args.outer,radial_degree=args.radial_degree)
    report=dict(**model.identity(),complete=False,samples=[])
    save(args.out,report)
    for u in (acb(0),acb(1),acb(0,1)):
        values,timing=model.sample(u,args.angles)
        center,_=model.central.sample(u,args.angles)
        if any(not (a.real.overlaps(b.real) and a.imag.overlaps(b.imag))
               for a,b in zip(values.flat,center.flat)):
            raise ValueError("uniform parameter and actual center source enclosures disagree")
        report["samples"].append(dict(u=complex_record(u),all_center_parameter_orders_overlap=True,
            maximum_component_radii=[ball_record(max(max(v.real.rad().upper(),v.imag.rad().upper())
                                                       for v in values[:,j])) for j in range(3)],
            maximum_source_moduli=[ball_record(max(absup(v) for v in values[:,j])) for j in range(3)],
            **timing))
        save(args.out,report);print(dict(u=str(u),passed=True,elapsed=time.monotonic()-started),flush=True)
    report.update(complete=True,wall_seconds=time.monotonic()-started,cpu_seconds=time.process_time()-cpu)
    save(args.out,report);print(dict(complete=True,sha256=sha(args.out),wall=report["wall_seconds"]),flush=True)


if __name__=="__main__":
    main()
