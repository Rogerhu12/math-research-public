#!/usr/bin/env python3
"""Complete finite regularized root one-form on the exact saved reference.

This adapter preserves every finite mode and every root/cut term. Its samples
are finite approximations; true geometry errors are supplied separately, only
on the paid real-time image. Finite complex-time norms do not enlarge the true
geometry domain. No completed whole-root phase integral is claimed here.
"""
from __future__ import annotations
import argparse, time
from fractions import Fraction
from pathlib import Path
from flint import arb, acb, ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha,stored,decode
from fourfold_subprincipal_root_regularized_transport import source_error_bound
from fourfold_fourier_local_taylor import finite_taylor_evaluate
from fourfold_complete_reference_segment import CompleteReferenceSegment
from fourfold_retarget_reference_jets import RetargetReference
from fourfold_phase_unified_scalar_time_circle import exact_time
from fourfold_phase_field_time_turn_collar import PiTime

FIELDS=("source_even","source_odd","cut_m3","cut_m1","cut_regular","root_field")
PARITY={"source_even":1,"source_odd":-1,"cut_m3":1,"cut_m1":1,
        "cut_regular":-1,"root_field":-1}


def full_row(encoded,parity):
    coeff=encoded["positive_coefficients"]
    K=len(coeff)-1
    row=[acb(0) for _ in range(2*K+1)]
    for k,pair in enumerate(coeff):
        value=decode(pair)
        z=acb(value) if parity>0 else acb(0,value)
        if k==0 and parity<0 and not value.is_zero():
            raise ValueError("odd finite field has nonzero mean")
        row[K+k]=z
        if k:row[K-k]=z.conjugate()
    return row


def add_centered(left,right,multiplier=1):
    KL,KR=(len(left)-1)//2,(len(right)-1)//2
    K=max(KL,KR)
    out=[acb(0) for _ in range(2*K+1)]
    for k,z in enumerate(left):out[k+K-KL]+=z
    for k,z in enumerate(right):out[k+K-KR]+=multiplier*z
    return out


def row_norm(row,physical_strip):
    K=(len(row)-1)//2
    return sum((abs(z)*(4*abs(k-K)*physical_strip).exp()
                for k,z in enumerate(row)),arb(0)).upper()


class CompleteRootReference:
    def __init__(self,report_path):
        self.path=Path(report_path)
        self.doc=read(self.path)
        d=self.doc
        if (not d.get("complete") or not d.get("proved")
            or d.get("kind")!="R106_complete_finite_regularized_root_one_form_reference"
            or not d.get("all_output_convolution_modes_retained")
            or not d.get("no_missing_radial_rows")):
            raise ValueError("complete finite seven-field source required")
        producer=Path(__file__).with_name("fourfold_subprincipal_root_regularized_fft.py")
        if d["source_sha256"]!=sha(producer):
            raise ValueError("finite regularization producer bytes differ")
        if sha(d["input_report_path"])!=d["input_report_sha256"]:
            raise ValueError("actual seven-field source changed")
        self.input=read(d["input_report_path"])
        if (self.input["identity"]!=d["identity"] or self.input["root"]!=d["root"]
            or self.input["working_rho_radius"]!=d["error_outer_rho_radius"]
            or self.input["working_physical_angle_strip"]!=d["error_outer_physical_angle_strip"]):
            raise ValueError("source approximation domain/root identity differs")
        for name,digest in d["dependencies"].items():
            if sha(Path(__file__).with_name(name))!=digest:
                raise ValueError("finite source dependency changed "+name)
        self.rows={name:[] for name in FIELDS}
        self.fees={name:[] for name in FIELDS}
        cursor=0
        for entry in d["shards"]:
            if entry["first_row"]!=cursor or sha(entry["path"])!=entry["sha256"]:
                raise ValueError("finite source shard gap or byte mismatch")
            block=read(entry["path"])
            if (block["identity"]!=d["identity"] or block["sigma"]!=d["sigma"]
                or block["input_report_sha256"]!=d["input_report_sha256"]
                or block["radial_scale_dyadic"]!=d["radial_scale_dyadic"]):
                raise ValueError("finite source shard identity differs")
            for rr in block["rows"]:
                if rr["radial_row"]!=cursor:raise ValueError("finite row gap")
                expected=set(FIELDS) if cursor==0 else set(FIELDS)-{"root_field"}
                if set(rr["fields"])!=expected:raise ValueError("finite field row is incomplete")
                for name in FIELDS:
                    if name=="root_field" and cursor:
                        self.rows[name].append([acb(0)])
                        self.fees[name].append(arb(0))
                    else:
                        one=rr["fields"][name]
                        self.rows[name].append(full_row(one,PARITY[name]))
                        self.fees[name].append(stored(one["finite_arithmetic_Wiener_error"]).upper())
                cursor+=1
            if entry["last_row"]!=cursor-1:raise ValueError("shard last row differs")
        if cursor!=d["finite_rows_done"]:raise ValueError("incomplete full finite source")
        self.scale=decode(d["radial_scale_dyadic"])
        self.root=stored(d["root"])
        self.cut=Fraction(d["original_fixed_physical_cut"])
        self.Sout=Fraction(d["working_physical_angle_strip"])
        self.Sin=Fraction(d["error_outer_physical_angle_strip"])
        self.R=Fraction(d["error_outer_rho_radius"])
        if not self.scale>0 or not self.root>exact_arb(self.cut):
            raise ValueError("invalid actual root/cut scale")

    def coefficients(self,name,rho):
        """All finite Fourier coefficients at this complete complex rho ball."""
        out=[acb(0)]
        z=acb(rho)/self.scale
        for row in reversed(self.rows[name]):
            out=add_centered([z*v for v in out],row)
        return out

    def modulus(self,name,rho_radius,physical_strip):
        """Full finite norm, even outside the actual geometry approximation disk."""
        r=arb(rho_radius)/self.scale
        S=arb(physical_strip)
        if not r>=0 or not S>=0:raise ValueError("invalid finite modulus domain")
        return sum((r**j*row_norm(row,S) for j,row in enumerate(self.rows[name])),arb(0)).upper()

    def finite_fee(self,name,rho_radius):
        """Whole finite-FFT/dyadic-choice fee on the original paid angle strip."""
        z=arb(rho_radius)/self.scale
        return sum((z**j*v for j,v in enumerate(self.fees[name])),arb(0)).upper()

    def true_source_error(self,rho_radius):
        """Uniform true H minus finite H on a requested smaller radial disk.

        The finite choice errors are reweighted at the requested radius.
        Consequently a complete reference segment slightly beyond the saved
        physical cut can still be used when it remains inside the paid outer
        error disk; the old cut-specific source fee is not silently extended.
        """
        r=arb(rho_radius).upper()
        R=exact_arb(self.R)
        if not 0<r<R:raise ValueError("true source leaves its paid error disk")
        c=r.sqrt().upper()
        # c rounding is enclosed by one final outward radius increase.
        r=(c*c).upper()
        if not r<R:raise ValueError("rounded root coordinate leaves its error disk")
        Sin,Sout=exact_arb(self.Sin),exact_arb(self.Sout)
        if not Sin>Sout:raise ValueError("missing true angular error margin")
        errors={key:stored(value).upper() for key,value in self.doc["complete_input_errors"].items()}
        true={key:stored(value).upper() for key,value in self.doc["true_input_moduli_on_error_bidisk"].items()}
        finite={key:stored(value).upper() for key,value in self.doc["finite_input_norms_on_error_bidisk"].items()}
        paid=source_error_bound(outer_radius=R,working_radius=r,s_radius=c,
            first_angle_loss=(Sin-Sout)/2,second_angle_loss=(Sin-Sout)/2,
            G_bound=true["G"],q_bound=true["q"],k_bound=true["kstar"],
            G_error=errors["G"],q_error=errors["q"],k_error=errors["kstar"],
            finite_q_bound=finite["q"],finite_k_bound=finite["kstar"])
        geometric=paid["regularized_source_sup_error"]+errors["Sreg"]/(Sin-Sout)
        finite_fee=self.finite_fee("source_even",r)+c*self.finite_fee("source_odd",r)
        return (geometric+finite_fee).upper()


class RootReferenceSegment:
    def __init__(self,field,reference,segment,*,root_side,
                 left=Fraction(0),right=Fraction(1)):
        if root_side not in (-1,1):raise ValueError("physical root side is +/-1")
        if not isinstance(field,CompleteRootReference):raise ValueError("validated finite source required")
        if not isinstance(reference,RetargetReference):raise ValueError("validated complete reference required")
        self.field,self.root_side=field,root_side
        self.reference=CompleteReferenceSegment(reference,"forward",segment,left,right)
        r=self.reference
        if not r.h>0:raise ValueError("this adapter uses the chronological forward leg")
        ident=field.doc["identity"]
        if (r.identity["target_exact_delta_fraction"]!=ident["exact_center_parameter"]
            or r.identity["target_object_sha256"]!=field.input["object_sha256"]):
            raise ValueError("finite source and saved reference use different actual centers")
        if r.identity["retarget_descriptor_sha256"]!="097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052":
            raise ValueError("not the validated complete delta5 reference")
        # Frozen true sampler: f_tau=-r_tau*(M+sign*wave*W)/D.
        # With v_phys=b/a-sign*sqrt(-K)/a and inward s, sigma=-side*sign.
        self.sigma=-root_side*r.identity["branch_sign"]
        if field.doc["sigma"]!=self.sigma:
            raise ValueError("wrong actual inward branch for this physical root")
        self.orientation=-root_side
        self.identity={"finite_root_source_path":str(field.path),
            "finite_root_source_sha256":sha(field.path),
            "reference":r.identity,"root_side":root_side,
            "inward_sigma":self.sigma,"integration_orientation":self.orientation,
            "root_to_cut_integral":True,"original_fixed_physical_cut":str(field.cut)}

    def _root_endpoint(self):
        r=self.reference
        index=0 if self.root_side<0 else 1
        subspan=Fraction(r.identity["normalized_subspan"][index])
        required=Fraction(0) if self.root_side<0 else Fraction(1)
        time=exact_time(r.identity["exact_segment_time_rows"][index])
        desired=PiTime(Fraction(0),Fraction(self.root_side,2))
        if subspan!=required or not (time-desired).is_zero():
            raise ValueError("this reference segment does not contain the exact root endpoint")
        return -1 if self.root_side<0 else 1

    def coordinates(self,u):
        r=self.reference
        tau=acb(r.center)+acb(r.h)*u
        eta=acb(arb.pi()/2)-self.root_side*tau
        # These exact values prevent a spurious pi-enclosure residue at the root.
        for endpoint in (-1,1):
            if u==acb(endpoint):
                try:root_endpoint=self._root_endpoint()
                except ValueError:root_endpoint=None
                if root_endpoint==endpoint:eta=acb(0)
        s=(2*self.field.root).sqrt()*(eta/2).sin()
        dsdu=-self.root_side*r.h*(self.field.root/2).sqrt()*(eta/2).cos()
        return s,s*s,dsdu

    def sample(self,u,nodes,label_width=Fraction(0),*,anchors=256,
               finite_radius=Fraction(1,32),tail_target="1e-30"):
        """Finite source H(s,Y)Y_x ds/du, oriented from the root to its cut."""
        tick,cpu=time.monotonic(),time.process_time()
        u=acb(u);s,rho,dsdu=self.coordinates(u)
        Y,_,Yx=self.reference.grid(u,nodes,Fraction(label_width))
        coeff=add_centered(self.field.coefficients("source_even",rho),
                           self.field.coefficients("source_odd",rho),s)
        values,diag=finite_taylor_evaluate(coeff,Y,anchors=anchors,
            radius=finite_radius,tail_target=tail_target)
        result=[self.orientation*dsdu*q*v for v,q in zip(values,Yx)]
        return result,{"complete_finite_evaluation":diag,
            "root_coordinate_real":ball_record(s.real),
            "root_coordinate_imaginary":ball_record(s.imag),
            "seconds":time.monotonic()-tick,"cpu_seconds":time.process_time()-cpu,
            "mean_retained":True,"coefficient_of_normalized_label_dx":True,
            "R104_final_frame_normalization_included":False}

    def finite_outer_modulus(self,time_radius,label_width):
        """Entire finite composition modulus; no true geometry domain claim."""
        Ru=exact_arb(Fraction(time_radius))
        if not Ru>=1:raise ValueError("outer time radius must cover the real interval")
        b=self.reference.bounds(Fraction(time_radius),Fraction(label_width))
        center=(arb.pi()/2-self.root_side*self.reference.center)/2
        w=abs(self.reference.h)*Ru/2
        sabs=((2*self.field.root).sqrt()*
             (abs(center.sin())*w.cosh()+abs(center.cos())*w.sinh())).upper()
        dabs=(abs(self.reference.h)*(self.field.root/2).sqrt()*
             (abs(center.cos())*w.cosh()+abs(center.sin())*w.sinh())).upper()
        rhoabs=(sabs*sabs).upper()
        width=b["physical_theta_image_strip"]
        H=(self.field.modulus("source_even",rhoabs,width)
            +sabs*self.field.modulus("source_odd",rhoabs,width)).upper()
        return {"finite_source_one_form_modulus":(H*b["full_q_modulus"]*dabs).upper(),
            "finite_H_modulus":H,"complex_s_modulus":sabs,
            "complex_rho_modulus":rhoabs,"complex_dsdu_modulus":dabs,
            "physical_theta_image_strip":width,"reference_q_modulus":b["full_q_modulus"],
            "true_field_extension_claimed":False}

    def real_time_error(self,label_width,*,image_nodes=512,image_order=8):
        """Whole real reference-segment geometry fee only, before flow correction."""
        r=self.reference
        lo,hi=r.center-r.h,r.center+r.h
        pi2=arb.pi()/2
        if not lo>-pi2 or not hi<pi2:
            # Exact root endpoint can meet rather than lie strictly inside.
            left_ok=lo>-pi2
            right_ok=hi<pi2
            try:root_endpoint=self._root_endpoint()
            except ValueError:root_endpoint=None
            left_ok=left_ok or (self.root_side<0 and root_endpoint==-1)
            right_ok=right_ok or (self.root_side>0 and root_endpoint==1)
            if not left_ok or not right_ok:
                raise ValueError("physical sine branch not certified")
        # Monotonicity of sin on this exact physical branch controls all time.
        tau_far=lo if self.root_side>0 else hi
        rho_upper=(self.field.root*(1-self.root_side*tau_far.sin())).upper()
        if not rho_upper>0:raise ValueError("root side/radial domain unresolved")
        image=r.real_time_image(Fraction(label_width),nodes=image_nodes,p=image_order)
        if not image.get("complete_real_time_image_proved"):
            raise ValueError("complete real-time image gate missing")
        width=stored(image["physical_theta_image_strip"]).upper()
        if not width<exact_arb(self.field.Sout):
            raise ValueError("real reference image leaves the paid true root angle strip")
        fee=self.field.true_source_error(rho_upper)
        # For real time, |sin|,|cos|<=1; this suffices without a q lower bound.
        q=r.bounds(Fraction(1),Fraction(label_width))["full_q_modulus"]
        ds=abs(r.h)*(self.field.root/2).sqrt()
        return {"complete_real_time_geometry_error_proved":True,
            "actual_radial_upper":ball_record(rho_upper),
            "complete_H_approximation_error":ball_record(fee),
            "uniform_density_error_before_true_flow_correction":ball_record((fee*q*ds).upper()),
            "reference_q_modulus":ball_record(q),
            "reference_image":image,
            "true_ray_transport_error_included":False}

    def cut_nodes(self,nodes,label_width=Fraction(0),**evaluation):
        """Complete fixed-physical-cut endpoint at its actual parameter time."""
        cut=exact_arb(self.field.cut)
        ratio=cut/self.field.root
        if not 0<ratio<1:raise ValueError("physical cut is not strictly inside root")
        tau=self.root_side*ratio.asin()
        u=(tau-self.reference.center)/self.reference.h
        if not u.lower()>=-1 or not u.upper()<=1:
            raise ValueError("the whole parameter cut must lie in this one reference segment")
        s=(self.field.root-cut).sqrt()
        rho=self.field.root-cut
        coeff=[v/(s*s*s) for v in self.field.coefficients("cut_m3",rho)]
        coeff=add_centered(coeff,self.field.coefficients("cut_m1",rho),1/s)
        coeff=add_centered(coeff,self.field.coefficients("cut_regular",rho))
        Y,_,Yx=self.reference.grid(acb(u),nodes,Fraction(label_width))
        values,diag=finite_taylor_evaluate(coeff,Y,**evaluation)
        return [v*q for v,q in zip(values,Yx)],{
            "actual_cut_time":ball_record(tau),"actual_normalized_cut_time":ball_record(u),
            "whole_parameter_cut_in_one_segment":True,
            "finite_evaluation":diag,
            "complete_endpoint_field_approximation_error":self.field.doc["complete_cut_sup_error"],
            "error_requires_paid_real_image_and_multiplication_by_reference_q":True}

    def root_nodes(self,nodes,label_width=Fraction(0),**evaluation):
        endpoint=self._root_endpoint()
        Y,_,Yx=self.reference.grid(acb(endpoint),nodes,Fraction(label_width))
        values,diag=finite_taylor_evaluate(self.field.rows["root_field"][0],Y,**evaluation)
        return [v*q for v,q in zip(values,Yx)],{
            "exact_root_endpoint":endpoint,"finite_evaluation":diag,
            "complete_endpoint_field_approximation_error":self.field.doc["complete_root_field_sup_error"],
            "error_requires_paid_real_image_and_multiplication_by_reference_q":True}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("root_source",type=Path)
    p.add_argument("--descriptor",type=Path,default=Path(
        "data/phase_ring_continuation/step5_retargeted_reference/descriptor.json"))
    p.add_argument("--segment",type=int,required=True)
    p.add_argument("--root-side",type=int,choices=(-1,1),required=True)
    p.add_argument("--label-width",type=Fraction,default=Fraction(1,1024))
    p.add_argument("--time-real",type=Fraction,default=Fraction(0))
    p.add_argument("--time-imag",type=Fraction,default=Fraction(0))
    p.add_argument("--nodes",type=int,default=512)
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError("new output required")
    ctx.prec=a.bits
    field=CompleteRootReference(a.root_source)
    reference=RetargetReference(a.descriptor)
    model=RootReferenceSegment(field,reference,a.segment,root_side=a.root_side)
    u=acb(exact_arb(a.time_real),exact_arb(a.time_imag))
    values,diagnostic=model.sample(u,a.nodes,a.label_width)
    real=model.real_time_error(a.label_width)
    outer=model.finite_outer_modulus(Fraction(3,2),a.label_width)
    report={"kind":"R106_complete_finite_root_reference_sample","complete":True,
      "source_sha256":sha(__file__),"identity":model.identity,
      "bits":a.bits,"nodes":a.nodes,"label_width":str(a.label_width),
      "input_time":{"real":str(a.time_real),"imaginary":str(a.time_imag)},
      "sample_modulus":ball_record(max(abs(v).upper() for v in values)),
      "finite_evaluation":diagnostic,"real_time_error":real,
      "finite_outer_bounds":{k:ball_record(v) if isinstance(v,arb) else v for k,v in outer.items()},
      "complete_phase_integral_proved":False,"true_ray_correction_included":False}
    save(a.out,report)
    if a.out.stat().st_size>=5_000_000:raise ValueError("output exceeds repository limit")
    print({"complete_sample":True,"out":str(a.out),"sha256":sha(a.out)},flush=True)


if __name__=="__main__":
    main()
