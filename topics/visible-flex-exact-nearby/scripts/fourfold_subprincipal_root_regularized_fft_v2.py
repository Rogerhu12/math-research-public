#!/usr/bin/env python3
"""Complete finite seven-field root source, with full convolution and paid errors.

Input: a completed actual seven-field root Fourier report. Output: exact dyadic
Laurent/Taylor references for the regular source, complete cut and root field.
No true-ray integration or R104 cutoff is asserted here. All convolution modes
are kept; FFT padding is an exact finite algorithm, not a truncation argument.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import acb,arb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha,stored,decode,dyadic
from fourfold_subprincipal_root_regularized_transport import (
    fadd,fscale,ftheta,source_error_bound,full_polynomial_norm)

NAMES=("G","q","kstar","Sreg","Ltheta","U0","U1")
PARITY={"G":1,"q":-1,"kstar":1,"Sreg":-1,"Ltheta":-1,"U0":1,"U1":1}


def complete_product(left,right):
    """Exact finite Laurent product enclosed by an acb DFT and its inverse."""
    if not left or not right:return {}
    lo1,hi1=min(left),max(left);lo2,hi2=min(right),max(right)
    nout=hi1-lo1+hi2-lo2+1
    N=1
    while N<nout:N*=2
    a=[acb(0) for _ in range(N)];b=[acb(0) for _ in range(N)]
    for k,v in left.items():a[k-lo1]=acb(v)
    for k,v in right.items():b[k-lo2]=acb(v)
    A,B=acb.dft(a),acb.dft(b)
    c=acb.dft([x*y for x,y in zip(A,B)],inverse=True)
    return {lo1+lo2+k:c[k] for k in range(nout)}


def checked_save(path,doc):
    save(path,doc)
    if Path(path).stat().st_size>=5_000_000:
        raise ValueError("complete output shard exceeds single-file limit")


def load_fields(report_path):
    report=read(report_path)
    source=Path(__file__).with_name("fourfold_subprincipal_root_fourier_v2.py")
    if (not report.get("complete") or not report.get("proved")
        or not report.get("root_auxiliary_fields_included")
        or report.get("preserved_fields")!=list(NAMES)
        or report["source_sha256"]!=sha(source)
        or not report.get("no_missing_radial_rows")):
        raise ValueError("actual complete seven-field input is absent or changed")
    for name,digest in report["dependencies"].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("actual field dependency changed "+name)
    for item in report["outer_geometry_inputs"]:
        if sha(item["path"])!=item["sha256"]:
            raise ValueError("actual outer field certificate changed")
    if (sha(report["object_path"])!=report["object_sha256"]
        or sha(report["root_certificate_path"])!=report["root_certificate_sha256"]):
        raise ValueError("actual object/root input changed")
    rows={name:[] for name in NAMES};cursor=0;K=report["K"]
    for item in report["coefficient_shards"]:
        if item["first_row"]!=cursor or sha(item["path"])!=item["sha256"]:
            raise ValueError("actual coefficient shard gap or SHA mismatch")
        block=read(item["path"])
        if (block["identity"]!=report["identity"] or block["N"]!=report["N"]
            or block["K"]!=K
            or block["radial_scale_dyadic"]!=report["radial_scale_dyadic"]):
            raise ValueError("coefficient shard has another scientific identity")
        for row in block["rows"]:
            if row["radial_row"]!=cursor or set(row["fields"])!=set(NAMES):
                raise ValueError("coefficient row gap or missing field")
            for name in NAMES:
                positive=row["fields"][name]["positive_coefficients"]
                if len(positive)!=K+1:raise ValueError("incomplete actual Fourier row")
                values={}
                for k,pair in enumerate(positive):
                    v=decode(pair)
                    if PARITY[name]<0:
                        if k==0 and not v.is_zero():raise ValueError("odd mean is not zero")
                        z=acb(0,v)
                    else:z=acb(v)
                    values[k]=z
                    if k:values[-k]=z.conjugate()
                rows[name].append(values)
            cursor+=1
        if cursor!=item["last_row"]+1:raise ValueError("coefficient shard endpoint mismatch")
    if cursor!=report["degree"]+1:raise ValueError("incomplete actual radial polynomial")
    return report,rows,decode(report["radial_scale_dyadic"])


def encode_row(row,parity,physical_strip):
    """Choose a new exact real/odd finite row; pay all finite DFT roundoff."""
    K=max((abs(k) for k in row),default=0)
    out=[];err=arb(0)
    for k in range(K+1):
        z=acb(row.get(k,0))
        other=acb(row.get(-k,0)).conjugate()
        real=z.real.intersection(other.real)
        imag=z.imag.intersection(other.imag)
        if parity>0:
            if not imag.contains(0):raise ValueError("even exact product lost parity")
            v=real
        else:
            if not real.contains(0):raise ValueError("odd exact product lost parity")
            v=imag
        mid=arb(0) if k==0 and parity<0 else v.mid()
        if k==0 and parity<0 and not v.contains(0):
            raise ValueError("exact odd coefficient mean is not zero")
        out.append(dyadic(mid))
        err+=(1 if k==0 else 2)*(4*physical_strip*k).exp()*abs(v-mid)
    return {"positive_coefficients":out,"parity":"even" if parity>0 else "odd",
            "finite_arithmetic_Wiener_error":ball_record(err.upper())},err.upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("input_report",type=Path)
    p.add_argument("--sigma",type=int,choices=(-1,1),default=1)
    p.add_argument("--working-strip",type=Fraction,default=Fraction(1,800))
    p.add_argument("--cut",type=Fraction,default=Fraction(268136140016943,1125899906842624))
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--rows-per-shard",type=int,default=2)
    p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if a.out_dir.exists():raise ValueError("preserve earlier finite source; choose a new output")
    if a.rows_per_shard<1:raise ValueError("positive complete shard size required")
    ctx.prec=a.bits;wall,cpu=time.monotonic(),time.process_time()
    input_report,rows,scale=load_fields(a.input_report)
    R=exact_arb(Fraction(input_report["working_rho_radius"]))
    Sin=exact_arb(Fraction(input_report["working_physical_angle_strip"]))
    Sout=exact_arb(a.working_strip)
    if not 0<Sout<Sin:raise ValueError("two physical angle losses are required")
    d1=d2=(Sin-Sout)/2
    root=stored(input_report["root"])
    rho_cut=root-exact_arb(a.cut)
    if not rho_cut>0 or not rho_cut.upper()<R:
        raise ValueError("actual whole-family cut outside finite-error disk")
    cmin=rho_cut.sqrt().lower();cmax=rho_cut.sqrt().upper()
    r=rho_cut.upper()
    # Enclose sqrt rounding when selecting a uniform complex s disk.
    if not cmax*cmax<R:raise ValueError("rounded s disk exhausts radial error margin")
    r=(cmax*cmax).upper()
    errors={name:stored(input_report["complete_approximant_errors"][name]["complete_sup_error"]).upper()
            for name in NAMES}
    finite_input={name:full_polynomial_norm(rows[name],R/scale,Sin) for name in NAMES}
    true_input={name:min(stored(input_report["complete_true_outer_bounds"][name]).upper(),
                        (finite_input[name]+errors[name]).upper()) for name in NAMES}
    paid=source_error_bound(outer_radius=R,working_radius=r,s_radius=cmax,
        first_angle_loss=d1,second_angle_loss=d2,
        G_bound=true_input["G"],q_bound=true_input["q"],k_bound=true_input["kstar"],
        G_error=errors["G"],q_error=errors["q"],k_error=errors["kstar"],
        finite_q_bound=finite_input["q"],finite_k_bound=finite_input["kstar"])
    source_geometry=(paid["regularized_source_sup_error"]+
                     errors["Sreg"]/(Sin-Sout)).upper()
    cut_geometry=(errors["G"]/(3*cmin*cmin*cmin)+paid["B1_sup_error"]/cmin
                  +errors["U0"]/(4*cmin*cmin*cmin)+errors["U1"]/(4*cmin)
                  +errors["Ltheta"]/4).upper()
    root_geometry=(errors["Ltheta"]/4).upper()
    G,q,k=rows["G"],rows["q"],rows["kstar"]
    row=lambda rr,n:rr[n] if n<len(rr) else {}
    G0=G[0]
    B1=fadd(fscale(row(G,1),-1/scale),
            fscale(ftheta(complete_product(q[0],G0)),-acb(2)/3))
    count=max(len(G)-2,len(q),len(k),len(rows["Sreg"]),len(rows["U0"]),
              len(rows["U1"]),len(rows["Ltheta"]),1)
    a.out_dir.mkdir(parents=True)
    report={"kind":"R106_complete_finite_regularized_root_one_form_reference",
        "complete":False,"proved":False,"source_sha256":sha(__file__),
        "input_report_path":str(a.input_report),"input_report_sha256":sha(a.input_report),
        "identity":input_report["identity"],"root":input_report["root"],
        "sigma":a.sigma,"original_fixed_physical_cut":str(a.cut),
        "actual_rho_cut":ball_record(rho_cut),"s_cut_lower":ball_record(cmin),
        "s_cut_upper":ball_record(cmax),"bits":a.bits,
        "radial_variable":input_report["radial_variable"],
        "radial_scale_dyadic":input_report["radial_scale_dyadic"],
        "working_physical_angle_strip":str(a.working_strip),
        "error_outer_rho_radius":input_report["working_rho_radius"],
        "error_outer_physical_angle_strip":input_report["working_physical_angle_strip"],
        "physical_angular_derivative_multiplier":4,
        "fields":{
            "source_even":"R_sigma(s,theta)+d_theta Sreg(s^2,theta), even s powers",
            "source_odd":"s times these rho rows, with actual sigma",
            "cut_m3":"s^-3 times these rho rows",
            "cut_m1":"s^-1 times these rho rows",
            "cut_regular":"these rho rows",
            "root_field":"sigma Ltheta(0,theta)/4"},
        "full_cut_definition":"cut=s^-3*cut_m3+s^-1*cut_m1+cut_regular",
        "finite_rows_done":0,"shards":[],
        "complete_input_errors":{name:ball_record(v) for name,v in errors.items()},
        "finite_input_norms_on_error_bidisk":{name:ball_record(v) for name,v in finite_input.items()},
        "true_input_moduli_on_error_bidisk":{name:ball_record(v) for name,v in true_input.items()},
        "geometric_source_error":ball_record(source_geometry),
        "geometric_cut_error":ball_record(cut_geometry),
        "geometric_root_field_error":ball_record(root_geometry),
        "regularized_source_error_terms":{name:ball_record(v) for name,v in paid.items()},
        "all_output_convolution_modes_retained":True,
        "continuous_true_ray_integral_proved":False,"effective_R104_cutoff_proved":False,
        "dependencies":{name:sha(Path(__file__).with_name(name)) for name in
          ("fourfold_subprincipal_root_regularized_transport.py",
           "fourfold_subprincipal_root_fourier_v2.py","fourfold_phase_root_fourier_fit.py")}}
    def checkpoint():
        report["wall_seconds"]=time.monotonic()-wall;report["cpu_seconds"]=time.process_time()-cpu
        checked_save(a.out_dir/"report.json",report)
    checkpoint()
    fees={name:arb(0) for name in report["fields"]}
    norms={name:arb(0) for name in report["fields"]}
    pending=[]
    for n in range(count):
        even=fadd(fscale(row(G,n+2),1/(scale*scale)),
            fscale(ftheta(complete_product(row(q,n+1),G0)),acb(2)/(3*scale)),
            fscale(ftheta(complete_product(row(q,n),B1)),-2),
            ftheta(row(rows["Sreg"],n)))
        odd=fadd(
            fscale(ftheta(complete_product(row(k,n+1),G0)),-acb(2*a.sigma)/(3*scale)),
            fscale(ftheta(complete_product(row(k,n),B1)),2*a.sigma))
        cm3=fadd(fscale(G0,-acb(1)/3) if n==0 else {},
                  fscale(row(rows["U0"],n),-acb(1)/4))
        cm1=fadd(B1 if n==0 else {},fscale(row(rows["U1"],n),-acb(1)/4))
        regular=fscale(row(rows["Ltheta"],n),-acb(a.sigma)/4)
        allrows={"source_even":(even,1),"source_odd":(odd,-1),
                 "cut_m3":(cm3,1),"cut_m1":(cm1,1),"cut_regular":(regular,-1)}
        if n==0:allrows["root_field"]=(fscale(rows["Ltheta"][0],acb(a.sigma)/4),-1)
        encoded={"radial_row":n,"fields":{}}
        for name,(v,parity) in allrows.items():
            er,fee=encode_row(v,parity,Sout);encoded["fields"][name]=er
            rw=(r/scale)**n if name!="root_field" else arb(1)
            fees[name]+=rw*fee
            # The true finite expression is bounded before the new dyadic choice.
            norms[name]+=rw*full_polynomial_norm([v],1,Sout)
        pending.append(encoded);report["finite_rows_done"]=n+1
        if len(pending)==a.rows_per_shard or n+1==count:
            path=a.out_dir/f"regular_rows_{pending[0]['radial_row']:04d}_{n:04d}.json.gz"
            checked_save(path,{"kind":"R106_exact_dyadic_complete_root_one_form_reference",
                "identity":report["identity"],"sigma":a.sigma,
                "input_report_sha256":report["input_report_sha256"],
                "radial_scale_dyadic":report["radial_scale_dyadic"],"rows":pending})
            report["shards"].append({"path":str(path),"sha256":sha(path),
                "first_row":pending[0]["radial_row"],"last_row":n})
            pending=[];checkpoint()
            print({"finite_rows":n+1,"total":count,"wall_seconds":report["wall_seconds"]},flush=True)
    source_finite=(fees["source_even"]+cmax*fees["source_odd"]).upper()
    cut_finite=(fees["cut_m3"]/cmin**3+fees["cut_m1"]/cmin+fees["cut_regular"]).upper()
    report.update(complete=True,proved=True,
        complete_finite_arithmetic_errors={name:ball_record(v.upper()) for name,v in fees.items()},
        finite_expression_moduli={name:ball_record(v.upper()) for name,v in norms.items()},
        complete_source_sup_error=ball_record((source_geometry+source_finite).upper()),
        complete_cut_sup_error=ball_record((cut_geometry+cut_finite).upper()),
        complete_root_field_sup_error=ball_record((root_geometry+fees["root_field"]).upper()),
        no_missing_radial_rows=([n for b in report["shards"] for n in
          range(b["first_row"],b["last_row"]+1)]==list(range(count))),
        source_integral_contract="actual integral of source(s,Theta)*J ds; no extra normalization factor",
        root_integral_contract="actual J0 times root_field(Theta0)",
        phase_not_yet_proved="No true-ray composition, endpoint-position approximation, strict-region or frame loss is silently included.")
    if not report["no_missing_radial_rows"]:raise ValueError("complete finite source shard gap")
    checkpoint()
    print({"complete":True,"out":str(a.out_dir/"report.json"),"sha256":sha(a.out_dir/"report.json"),
           "source_error":report["complete_source_sup_error"]},flush=True)


if __name__=="__main__":
    main()
