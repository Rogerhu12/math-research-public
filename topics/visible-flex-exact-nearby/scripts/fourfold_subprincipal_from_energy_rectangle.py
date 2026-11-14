#!/usr/bin/env python3
"""Actual strict-core phase fields from one completed R110 nine-field rectangle.

No geometric primitive is resampled. Each saved coefficient error is reweighted
on the requested physical complex-angle strip, and both infinite complements
are recomputed there. The true alpha/gamma branch is verified on complete
boundary circles, not inferred from real positivity. Root finite parts and the
whole returned phase are outside this program's scope.
"""
from __future__ import annotations
import argparse
from collections import deque
from fractions import Fraction
import gzip
import hashlib
import io
import json
from pathlib import Path
import time
import traceback
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cut_interface_fourier import geometric_tail
from fourfold_phase_strict_core_energy import CompleteEnergyFields,FIELDS,USED,ODD

RAY_REPORT_SHA="6463e62641b9187045016c63ee633816676a75baf941ea01375a6ae36f1a1863"
PARAMETER_CERTIFICATE="data/phase_ring_continuation/type_fixed_step02_d5_step5_fixed_tau_parameter_source_certificate.json"
PARAMETER_CERTIFICATE_SHA="08b6fb2f3be32b7d2657d756e547134dcb55a54bb67a89d5f44a7fcd2f9f6e76"
PHASE_FIELDS=("reduced_density_full_d","radial_log_mu_flux","angular_log_mu_flux",
              "log_mu_r","log_mu_theta","physical_drift","physical_half_separation")

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(path):
    data=Path(path).read_bytes()
    if Path(path).suffix==".gz":
        data=gzip.decompress(data)
    return json.loads(data.decode("utf8"))

def stored_upper(row):
    value=arb(row["upper"] if isinstance(row,dict) and "upper" in row else
              row["ball"] if isinstance(row,dict) else str(row))
    return value.upper()

def pad_complex(value,radius):
    if not radius>=0:
        raise ValueError("negative complex enclosure radius")
    error=arb(0,radius.upper())
    return acb(value)+acb(error,error)

def real_interval(left,right):
    if not left<=right:
        raise ValueError("reversed actual radial interval")
    return exact_arb(left).union(exact_arb(right))

def compressed_save(path,doc):
    data=(json.dumps(doc,indent=2,allow_nan=False)+"\n").encode("utf8")
    path=Path(path)
    if path.suffix==".gz":
        data=gzip.compress(data,mtime=0)
    elif len(data)>1_000_000:
        raise ValueError("a report over 1 MB must use .json.gz")
    if len(data)>=5_000_000:
        raise ValueError("report exceeds repository single-file bound")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(data)


class ComplexPhaseFields(CompleteEnergyFields):
    """The exact same chosen rectangle, with new complete strip errors."""
    def __init__(self,path,physical_strip):
        super().__init__(path)
        self.physical_strip=Fraction(physical_strip)
        if not self.physical_strip>0:
            raise ValueError("positive physical angle strip required")
        self.S=exact_arb(Fraction(self.doc["normalized_angular_strip"]))
        self.s=exact_arb(self.physical_strip)
        self.R=exact_arb(Fraction(self.doc["outer_time_radius"]))
        self.h_arb=exact_arb(self.h)
        self.decay=self.S-4*self.s
        if not self.decay>0 or not self.R>1:
            raise ValueError("requested strip/radius is outside the true field domain")
        record=self.doc["arrays"]
        path=Path(record["path"])
        if sha(path)!=record["sha256"]:
            raise ValueError("field rectangle changed")
        stream=(io.BytesIO(gzip.decompress(path.read_bytes()))
                if path.suffix==".gz" else path)
        with np.load(stream,allow_pickle=False) as data:
            radii=np.array(data["positive_coefficient_error_radii"],copy=True)
        self.m=self.raw["alpha"].shape[0]
        if (radii.shape!=(len(FIELDS),self.m,self.K+1)
            or np.any(~np.isfinite(radii)) or np.any(radii<0)):
            raise ValueError("missing full chosen-coefficient error rectangle")
        if (self.doc["time_terms"]!=self.m
            or self.doc["positive_fourier_keep"]!=self.K):
            raise ValueError("finite rectangle metadata differs")
        self.exp_errors={}
        self.error_records={}
        exp=[(4*k*self.s).exp() for k in range(self.K+1)]
        inverse_R=1/self.R
        time_tail=self.R**(-self.m)/(1-inverse_R)
        time_radial_tail=(self.R**(-self.m)*
             (self.m/(1-inverse_R)+inverse_R/(1-inverse_R)**2)/self.h_arb)
        for name in USED:
            M=stored_upper(self.doc["whole_true_coefficient_moduli"][name])
            if not M>=0:
                raise ValueError("negative true outer modulus")
            selected=[arb(0) for _ in range(3)]
            selected_r=[arb(0) for _ in range(3)]
            for i in range(self.m):
                for k in range(self.K+1):
                    e=arb(float(radii[FIELDS.index(name),i,k]))*exp[k]
                    for j in range(3):
                        weight=(1 if k==0 and j==0 else 0 if k==0 else 2*(4*k)**j)
                        selected[j]+=weight*e
                        selected_r[j]+=weight*i*e/self.h_arb
            angle=[]
            angle_r=[]
            time_error=[]
            time_r=[]
            for j in range(3):
                tail=arb(0) if name=="kappa" else geometric_tail(self.K,self.decay,j,M)
                angle.append(tail.upper())
                angle_r.append((tail/(self.h_arb*(self.R-1))).upper())
                angular=arb(1) if j==0 else arb(0)
                if name!="kappa":
                    for k in range(1,self.K+1):
                        angular+=2*(4*k)**j*(-k*self.decay).exp()
                time_error.append((M*time_tail*angular).upper())
                time_r.append((M*time_radial_tail*angular).upper())
            errors=[[(selected[j]+angle[j]+time_error[j]).upper() for j in range(3)],
                    [(selected_r[j]+angle_r[j]+time_r[j]).upper() for j in range(3)]]
            self.exp_errors[name]=errors
            self.error_records[name]=dict(
                complete_value_error_A012=list(map(ball_record,errors[0])),
                complete_physical_r_error_A012=list(map(ball_record,errors[1])),
                selected_coefficient_error_A012=list(map(ball_record,selected)),
                selected_physical_r_error_A012=list(map(ball_record,selected_r)),
                angular_complement_A012=list(map(ball_record,angle)),
                angular_complement_physical_r_A012=list(map(ball_record,angle_r)),
                retained_angle_time_complement_A012=list(map(ball_record,time_error)),
                retained_angle_time_complement_physical_r_A012=list(map(ball_record,time_r)),
                true_outer_field_modulus=ball_record(M))

    def boundary_cells(self,left,right,nodes):
        """All real r in [left,right], every top-boundary angular gap."""
        if not self.left<=left<right<=self.right:
            raise ValueError("radial interval is outside the paid rectangle")
        if nodes%2 or nodes<=2*self.K:
            raise ValueError("even node count greater than 2K required")
        u=real_interval((left-self.center)/self.h,(right-self.center)/self.h)
        gap=arb.pi()/(4*nodes)
        real_delta=arb(0,gap.upper())
        values={}
        for name in USED:
            coeff=[[],[]]
            raw=self.raw[name]
            for k in range(self.K+1):
                value,derivative=arb(0),arb(0)
                for number in raw[:,k][::-1]:
                    derivative=derivative*u+value
                    value=value*u+arb(float(number))
                coeff[0].append(value)
                coeff[1].append(derivative/self.h_arb)
            moments={}
            samples={}
            for dr in (0,1):
                M=[arb(0) for _ in range(3)]
                for k,c in enumerate(coeff[dr]):
                    size=abs(c).upper()*(4*k*self.s).exp()
                    for dt in range(3):
                        weight=(1 if k==0 and dt==0 else 0 if k==0 else 2*(4*k)**dt)
                        M[dt]+=weight*size
                M=[(M[j]+self.exp_errors[name][dr][j]).upper() for j in range(3)]
                moments[dr]=M
                for dt in (0,1):
                    data=[acb(0) for _ in range(nodes)]
                    data[0]=acb(coeff[dr][0]) if dt==0 else acb(0)
                    for k in range(1,self.K+1):
                        positive=acb(0,coeff[dr][k]) if name in ODD else acb(coeff[dr][k])
                        negative=-positive if name in ODD else positive
                        data[(-k)%nodes]=positive*acb(0,4*k)**dt*(-4*k*self.s).exp()
                        data[k%nodes]=negative*acb(0,-4*k)**dt*(4*k*self.s).exp()
                    z=acb.dft(data)
                    samples[dr,dt]=[pad_complex(v,self.exp_errors[name][dr][dt]) for v in z]
            value=[samples[0,0][j]+real_delta*samples[0,1][j]
                   +pad_complex(0,gap*gap*moments[0][2]/2) for j in range(nodes)]
            theta=[samples[0,1][j]+pad_complex(0,gap*moments[0][2])
                   for j in range(nodes)]
            radial=[samples[1,0][j]+real_delta*samples[1,1][j]
                    +pad_complex(0,gap*gap*moments[1][2]/2) for j in range(nodes)]
            values[name]=dict(value=value,theta=theta,radial=radial)
        return values,gap

    def phase_cell(self,left,right,nodes):
        value,gap=self.boundary_cells(left,right,nodes)
        minima={name:min(v.real.lower() for v in value[name]["value"])
                for name in ("alpha","gamma","kappa")}
        if any(not z>0 for z in minima.values()):
            raise ValueError("actual alpha/gamma/-K0 complex boundary not separated: "+
                             str({name:str(z) for name,z in minima.items()}))
        moduli={name:arb(0) for name in PHASE_FIELDS}
        max_identity=arb(0)
        for j in range(nodes):
            alpha=value["alpha"]["value"][j]
            gamma=value["gamma"]["value"][j]
            v=value["v"]["value"][j]
            ar,at=value["alpha"]["radial"][j],value["alpha"]["theta"][j]
            gr,gt=value["gamma"]["radial"][j],value["gamma"]["theta"][j]
            a=1/alpha;b=v/alpha;c=v*v/alpha-gamma
            # Separate right-half-plane roots keep the analytic real branch.
            mu=gamma.sqrt(analytic=True)/alpha.sqrt(analytic=True)
            Lr=(gr/gamma-ar/alpha)/2
            Lt=(gt/gamma-at/alpha)/2
            d=value["tau"]["value"][j]+value["sigma"]["theta"][j]
            D=(d-(a*Lr*Lr+2*b*Lr*Lt+c*Lt*Lt)/4)/mu
            Vr=(a*Lr+b*Lt)/mu
            Vt=(b*Lr+c*Lt)/mu
            nu=alpha*mu
            fields=dict(reduced_density_full_d=D,radial_log_mu_flux=Vr,
                angular_log_mu_flux=Vt,log_mu_r=Lr,log_mu_theta=Lt,
                physical_drift=v,physical_half_separation=nu)
            for name,z in fields.items():
                if not z.is_finite():
                    raise ValueError("nonfinite actual phase field: "+name)
                moduli[name]=max(moduli[name],abs(z).upper())
            for branch in (-1,1):
                velocity=v-branch*nu
                residual=Vt-velocity*Vr-branch*(Lr+velocity*Lt)
                if not residual.contains(0):
                    raise ValueError("the exact characteristic flux identity failed")
                max_identity=max(max_identity,abs(residual).upper())
        return dict(left=str(left),right=str(right),angle_nodes=nodes,
            exact_physical_boundary_height=str(self.physical_strip),
            complete_closed_angular_gap=ball_record(gap),
            positive_real_lower={name:ball_record(z) for name,z in minima.items()},
            full_strip_moduli={name:ball_record(z) for name,z in moduli.items()},
            characteristic_identity_residual_modulus=ball_record(max_identity),
            extension="Schwarz reflection covers the lower boundary; harmonic minimum separates alpha/gamma throughout; maximum modulus gives all phase fields on the full closed strip.")


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--field-report",type=Path,required=True)
    p.add_argument("--ray-tube",type=Path,default=Path(
        "notes/2026-11-12-R106-actual-all-time-ray-tube.json"))
    p.add_argument("--parameter-certificate",type=Path,default=Path(PARAMETER_CERTIFICATE))
    p.add_argument("--left",type=Fraction)
    p.add_argument("--right",type=Fraction)
    p.add_argument("--physical-strip",type=Fraction,default=Fraction(1,800))
    p.add_argument("--angles",type=int,default=4096)
    p.add_argument("--max-depth",type=int,default=16)
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--resume",action="store_true")
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    started,cpu=time.monotonic(),time.process_time()
    model=ComplexPhaseFields(args.field_report,args.physical_strip)
    if sha(args.ray_tube)!=RAY_REPORT_SHA:
        raise ValueError("the complete actual ray certificate differs")
    ray=read(args.ray_tube)
    rayp=Fraction(ray["proved_region"]["parameter_center"])
    rayeta=Fraction(ray["proved_region"]["parameter_half_width"])
    pleft,pright=map(Fraction,model.doc["identity"]["exact_parameter_interval"])
    if not pleft<=rayp-rayeta<=rayp+rayeta<=pright:
        raise ValueError("the field rectangle does not cover the actual ray family")
    if model.doc["identity"]["object_sha256"]!=ray["provenance"]["actual_object_sha256"]:
        raise ValueError("field and ray geometry differ")
    image=Fraction(ray["bounds"]["physical_image_strip"]["exact"])
    if not image<args.physical_strip:
        raise ValueError("true whole-time rays do not fit the requested phase field strip")
    left=model.left if args.left is None else args.left
    right=model.right if args.right is None else args.right
    if sha(args.parameter_certificate)!=PARAMETER_CERTIFICATE_SHA:
        raise ValueError("the complete fixed-tau family certificate changed")
    parameter=read(args.parameter_certificate)
    rbulk=Fraction(parameter["exact_bulk_radial_cover"][1])
    if not (parameter.get("proved") and max(abs(left),abs(right))<=rbulk):
        raise ValueError("the claimed ray integral is outside the already paid central bulk; use a root-collar interface there")
    cert_left,cert_right=map(Fraction,parameter["exact_parameter_interval"])
    if not cert_left<=rayp-rayeta<=rayp+rayeta<=cert_right:
        raise ValueError("ray family is outside the fixed-tau core certificate")
    identity=dict(source_sha256=sha(__file__),field_report_path=str(args.field_report),
        field_report_sha256=sha(args.field_report),ray_tube_path=str(args.ray_tube),
        ray_tube_sha256=sha(args.ray_tube),
        parameter_certificate_path=str(args.parameter_certificate),
        parameter_certificate_sha256=sha(args.parameter_certificate),
        physical_angle_strip=str(args.physical_strip),
        exact_radial_interval=[str(left),str(right)],angles=args.angles,bits=args.bits,
        object_sha256=model.doc["identity"]["object_sha256"],
        exact_parameter_interval=model.doc["identity"]["exact_parameter_interval"],
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            "fourfold_phase_core_energy_fields.py","fourfold_phase_strict_core_energy.py",
            "fourfold_phase_cut_interface_fourier.py","fourfold_phase_beta_interval.py",
            "fourfold_phase_beta_bulk_interval.py")})
    doc=dict(kind="actual_strict_subprincipal_fields_from_complete_energy_rectangle",
        complete=False,identity=identity,complex_error_budget=model.error_records,
        accepted=[],failed_attempts=[],pending=[],geometry_resampled=False,
        full_root_finite_part_paid=False,complete_return_phase_paid=False)
    if args.resume and args.out.exists():
        previous=read(args.out)
        if previous.get("identity")!=identity:
            raise ValueError("resume scientific identity differs")
        doc=previous
        if doc.get("complete"):
            print(json.dumps({"complete":True,"reused":True,"sha256":sha(args.out)}));return
    done=sorted((Fraction(row["left"]),Fraction(row["right"])) for row in doc["accepted"])
    queue=deque()
    cursor=left
    for a,b in done:
        if not cursor<=a<b<=right:
            raise ValueError("saved subprincipal coverage overlaps or leaves the interval")
        if cursor<a:queue.append((cursor,a,0))
        cursor=b
    if cursor<right:queue.append((cursor,right,0))
    def checkpoint():
        doc["pending"]=[[str(a),str(b),depth] for a,b,depth in queue]
        doc["wall_seconds"]=time.monotonic()-started
        doc["cpu_seconds"]=time.process_time()-cpu
        compressed_save(args.out,doc)
    checkpoint()
    try:
        while queue:
            a,b,depth=queue.popleft()
            try:
                row=model.phase_cell(a,b,args.angles)
                row["depth"]=depth
                doc["accepted"].append(row)
            except (ValueError,ZeroDivisionError) as exc:
                doc["failed_attempts"].append(dict(left=str(a),right=str(b),
                    depth=depth,reason=str(exc)))
                if depth>=args.max_depth:
                    queue.appendleft((a,b,depth));checkpoint();raise
                mid=(a+b)/2
                queue.appendleft((mid,b,depth+1));queue.appendleft((a,mid,depth+1))
            checkpoint()
            print(json.dumps({"accepted":len(doc["accepted"]),"pending":len(queue),
                              "wall_seconds":doc["wall_seconds"]}),flush=True)
        ordered=sorted(doc["accepted"],key=lambda row:Fraction(row["left"]))
        cursor=left;mass=arb(0)
        for row in ordered:
            a,b=Fraction(row["left"]),Fraction(row["right"])
            if a!=cursor or not a<b<=right:
                raise ValueError("final exact closed radial coverage failed")
            mass+=exact_arb(b-a)*stored_upper(row["full_strip_moduli"]["reduced_density_full_d"])
            cursor=b
        if cursor!=right:
            raise ValueError("actual phase field coverage incomplete")
        J=exact_arb(Fraction(ray["bounds"]["true_label_J_modulus"]["exact"]))
        doc.update(complete=True,pending=[],
            full_strip_moduli={name:ball_record(max(stored_upper(row["full_strip_moduli"][name])
                                  for row in ordered)) for name in PHASE_FIELDS},
            full_strip_reduced_density_absolute_integral=ball_record(mass.upper()),
            true_label_primary_integral_modulus=ball_record((J*mass/2).upper()),
            exact_current_label_strip=ray["proved_region"]["label_strip"],
            reduced_density_convention="Dfull=(d-grad(log mu)^t A grad(log mu)/4)/mu with d=tau+physical_theta_derivative(sigma); its separate S is exactly zero.",
            endpoint_bookkeeping="Only outer endpoints of a union of matching radial pieces should be added. Internal true boundary terms cancel; do not pay or omit them inconsistently.")
        checkpoint()
    except Exception as exc:
        doc["failure"]=repr(exc);doc["traceback"]=traceback.format_exc();checkpoint()
        raise
    print(json.dumps({"complete":True,"out":str(args.out),"sha256":sha(args.out),
        "actual_radial_pieces":len(doc["accepted"])}),flush=True)

if __name__=="__main__":
    main()
