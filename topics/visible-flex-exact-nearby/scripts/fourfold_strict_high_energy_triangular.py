#!/usr/bin/env python3
"""Complete integer derivative energy hierarchy for the actual strict core.

Consumes the true nine-field rectangle and its complete closed-circle base
energy certificate. Every finite coefficient, its recorded error radius, the
whole omitted angular complement and the whole omitted time complement enter
every requested derivative order. Higher coefficient derivatives drive only
lower-to-higher triangular entries; the diagonal uses the true characteristic
first derivative. No finite frequency cutoff or high inverse is inferred.
"""
from __future__ import annotations
import argparse, gzip, io, json, math, time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb, acb, acb_mat, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_strict_core_energy import CompleteEnergyFields,sha,read,save
from fourfold_phase_strict_core_kernel_tame_energy import positive_range,up

NAMES=("a","b","c","tau","sigma","alpha","v","gamma","kappa")
USED=("alpha","v","gamma","tau","sigma")

def checked(path):
    d=read(path)
    if (not d.get("complete") or d.get("kind") !=
            "actual_strict_negative_half_derivative_energy_inputs"):
        raise ValueError("complete true strict-core base energy required")
    source=Path(__file__).with_name("fourfold_phase_strict_core_energy.py")
    if sha(source)!=d["source_sha256"]:raise ValueError("base energy source changed")
    for name,digest in d["dependency_sha256"].items():
        if sha(source.with_name(name))!=digest:raise ValueError("base dependency changed: "+name)
    for key in ("full_real_radial_interval_paid","full_real_theta_circle_paid",
                "strict_negative_target_curvature_proved"):
        if not d.get(key):raise ValueError("missing actual base gate: "+key)
    if not d["identity"].get("uniform_in_the_entire_real_parameter_interval"):
        raise ValueError("whole real parameter family missing")
    fpath=Path(d["input_field_report"]["path"])
    if sha(fpath)!=d["input_field_report"]["sha256"]:raise ValueError("nine-field input changed")
    return d,CompleteEnergyFields(fpath)

def stirling_rows(n):
    rows=[[1]]
    for j in range(1,n+1):
        last=rows[-1];new=[0]*(j+1)
        for l in range(1,j+1):
            new[l]=(last[l-1] if l-1<len(last) else 0)+(l*last[l] if l<len(last) else 0)
        rows.append(new)
    return rows

def power_tail(start,q,n,stirling):
    """Exact rational-function sum of k^n q^k, k>=start."""
    den=1-q
    if not 0<q<1:raise ValueError("nonconvergent full angular complement")
    moments=[]
    for ell in range(n+1):
        moments.append(sum((arb(stirling[ell][j])*math.factorial(j)*q**j/den**(j+1)
                            for j in range(ell+1)),arb(0)))
    return (q**start*sum((math.comb(n,ell)*arb(start)**(n-ell)*moments[ell]
                          for ell in range(n+1)),arb(0))).upper()

def high_moments(fields,coefficients,order):
    doc=fields.doc
    stream=Path(doc["arrays"]["path"])
    if sha(stream)!=doc["arrays"]["sha256"]:raise ValueError("true field arrays changed")
    with np.load(io.BytesIO(gzip.decompress(stream.read_bytes())) if stream.suffix==".gz" else stream,
                 allow_pickle=False) as arr:
        errors=np.array(arr["positive_coefficient_error_radii"],copy=True)
    if (errors.shape!=(len(NAMES),doc["time_terms"],fields.K+1)
            or np.any(~np.isfinite(errors)) or np.any(errors<0)):
        raise ValueError("invalid saved full coefficient error tensor")
    S=exact_arb(Fraction(doc["normalized_angular_strip"]))
    R=exact_arb(Fraction(doc["outer_time_radius"]))
    m=doc["time_terms"];K=fields.K
    if not S>0 or not R>1:raise ValueError("true bidisk missing")
    q=(-S).exp();stirling=stirling_rows(order)
    weights=[[arb(1) if n==0 else arb(0) for n in range(order+1)]]
    for k in range(1,K+1):weights.append([arb(2)*(4*k)**n for n in range(order+1)])
    retained_angular=[]
    for n in range(order+1):
        retained_angular.append(sum((weights[k][n]*q**k for k in range(K+1)),arb(0)))
    output={};records={}
    for name in USED:
        M=up(doc["whole_true_coefficient_moduli"][name])
        chosen_error=[sum((arb(float(z)) for z in errors[NAMES.index(name),:,k]),arb(0)).upper()
                      for k in range(K+1)]
        finite=[abs(v).upper() for v in coefficients[name]]
        time_ratio=R**(-m)/(1-1/R)
        # Each full true Fourier coefficient has BOTH enclosures. Intersect
        # before multiplying by large high-order weights, so uniform nodal
        # interval noise is not mistaken for a real high-frequency tail.
        joint_frequency=[min(finite[k]+chosen_error[k]+M*q**k*time_ratio,
                             M*q**k).upper() for k in range(K+1)]
        norms=[];rows=[]
        for n in range(order+1):
            f=sum((weights[k][n]*finite[k] for k in range(K+1)),arb(0)).upper()
            e=sum((weights[k][n]*chosen_error[k] for k in range(K+1)),arb(0)).upper()
            angular=(2*M*arb(4)**n*power_tail(K+1,q,n,stirling)).upper()
            radial=(M*R**(-m)/(1-1/R)*retained_angular[n]).upper()
            intersected=sum((weights[k][n]*joint_frequency[k]
                             for k in range(K+1)),arb(0)).upper()
            total=(intersected+angular).upper()
            if not total.is_finite() or not total>=0:raise ValueError("nonfinite true high moment")
            norms.append(total)
            rows.append(dict(physical_angular_derivative=n,
                finite_whole_real_interval=ball_record(f),
                all_selected_coefficient_errors=ball_record(e),
                complete_unretained_angular_complement=ball_record(angular),
                complete_retained_angle_unretained_time=ball_record(radial),
                retained_true_Fourier_bounds_after_Cauchy_intersection=ball_record(intersected),
                whole_true_derivative_A_norm=ball_record(total)))
        output[name]=norms;records[name]=rows
    output["d"]=[(output["tau"][j]+output["sigma"][j+1]).upper() for j in range(order)]
    records["d"]=dict(exact_definition="d=tau+partial_theta sigma",
        whole_true_derivative_A_norms=[ball_record(z) for z in output["d"]])
    return output,records

def matrix_rows(A):
    return [[ball_record(A[i,j].real) for j in range(A.ncols())] for i in range(A.nrows())]

def positive_matrix_bound(A):
    rows=[sum((abs(A[i,j]).upper() for j in range(A.ncols())),arb(0)).upper()
          for i in range(A.nrows())]
    cols=[sum((abs(A[i,j]).upper() for i in range(A.nrows())),arb(0)).upper()
          for j in range(A.ncols())]
    schur=(max(rows)*max(cols)).sqrt().upper()
    frob=sum((abs(A[i,j]).upper()**2 for i in range(A.nrows()) for j in range(A.ncols())),arb(0)).sqrt().upper()
    return min(schur,frob).upper()

def weighted_principal(A,k):
    weights=[arb(math.comb(k,j)).sqrt() for j in range(k+1)]
    return acb_mat([[A[i,j]*weights[i]/weights[j] for j in range(k+1)] for i in range(k+1)])

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--energy-report",type=Path,required=True)
    ap.add_argument("--order",type=int,default=10)
    ap.add_argument("--angles",type=int,default=4096)
    ap.add_argument("--bits",type=int,default=256)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise ValueError("new output path required")
    if not 1<=args.order<=24:raise ValueError("finite requested energy order out of range")
    ctx.prec=args.bits;start=time.monotonic()
    doc,fields=checked(args.energy_report)
    left,right=map(Fraction,doc["exact_physical_interval"])
    values,coefficients,_=fields.evaluate(left,right,args.angles)
    amin,amax=positive_range(doc,"alpha");gmin,gmax=positive_range(doc,"gamma")
    lmin,lmax=positive_range(doc,"lambda_weight")
    if doc["energy_weight"]["kind"] not in ("minus_actual_target_curvature","positive_exact_constant"):
        raise ValueError("the triangular formula requires a radial positive energy weight")
    moments,moment_records=high_moments(fields,coefficients,args.order+1)
    fchar=[];bchar=[]
    for j in range(args.angles):
        alpha=values["alpha"]["value"][j];gamma=values["gamma"]["value"][j]
        alpha_t=values["alpha"]["theta"][j];gamma_t=values["gamma"]["theta"][j]
        vt=values["v"]["theta"][j]
        if not alpha>0 or not gamma>0:raise ValueError("true hyperbolic coefficient unresolved")
        nu_t=(gamma*alpha_t+alpha*gamma_t)/(2*(alpha*gamma).sqrt())
        fchar.append(max(arb(0),(-vt+abs(nu_t).upper()).upper()))
        bchar.append(max(arb(0),(vt+abs(nu_t).upper()).upper()))
    first_forward=max(fchar).upper();first_backward=max(bchar).upper()
    base_forward=up(doc["constants"]["base_energy_rate_forward"])/2
    base_backward=up(doc["constants"]["base_energy_rate_backward"])/2
    size=args.order+1
    matrices={side:acb_mat(size,size) for side in ("forward","backward")}
    for j in range(size):
        matrices["forward"][j,j]=max(arb(0),base_forward+j*first_forward).upper()
        matrices["backward"][j,j]=max(arb(0),base_backward+j*first_backward).upper()
        for ell in range(j):
            n=j-ell
            C0=arb(math.comb(j,ell));C1=arb(math.comb(j+1,ell))
            terms=[
                C0*moments["v"][n]*(lmax/gmin).sqrt(),
                C0*moments["alpha"][n]*(lmax/amin).sqrt(),
                C1*moments["v"][n+1]*(gmax/gmin).sqrt(),
                C1*moments["alpha"][n+1]*(gmax/amin).sqrt(),
                C0*moments["d"][n]*(amax/lmin).sqrt(),
                C1*moments["gamma"][n+1]*(amax/gmin).sqrt(),
                C1*moments["v"][n+1]*(amax/amin).sqrt()]
            gain=sum((z*z for z in terms),arb(0)).sqrt().upper()
            for A in matrices.values():A[j,ell]=gain
    L=exact_arb(right-left)
    maps={side:(L*A).exp() for side,A in matrices.items()}
    hmin=min(amin,gmin,lmin);hmax=max(amax,gmax,lmax)
    bounds={}
    for side,A in maps.items():
        rows=[]
        for k in range(size):
            N=positive_matrix_bound(weighted_principal(A,k))
            rows.append(dict(integer_angular_order=k,P_s=str(Fraction(2*k+1,2)),
                derivative_energy_map_norm=ball_record(N),
                full_physical_Cauchy_bound=ball_record((N*(hmax/hmin).sqrt()).upper()),
                ordinary_L1_Hk_source_to_Pkhalf=ball_record((N*(amax/hmin).sqrt()).upper())))
        bounds[side]=rows
    uniform={}
    for k in range(size):
        uniform[str(Fraction(2*k+1,2))]=max(
            up(bounds[side][k]["full_physical_Cauchy_bound"]) for side in bounds).upper()
    integer_S={}
    for s in range(1,args.order+1):
        value=(uniform[str(Fraction(2*s-1,2))]*uniform[str(Fraction(2*s+1,2))]).sqrt().upper()
        integer_S[str(s)]=ball_record(value)
    out=dict(kind="actual_strict_core_complete_integer_derivative_hierarchy",
        complete=True,proved=True,source_sha256=sha(__file__),bits=args.bits,
        input_energy_report=dict(path=str(args.energy_report),sha256=sha(args.energy_report)),
        input_field_report=dict(path=str(fields.path),sha256=sha(fields.path)),
        identity=doc["identity"],exact_physical_interval=list(map(str,(left,right))),
        order=args.order,angular_closed_cells=args.angles,energy_weight=doc["energy_weight"],
        physical_frequency="4*k, k in Z; zero frequency retained with Sobolev weight one",
        exact_state="Z_j=(partial_theta^j u, partial_theta^(j+1) u, partial_theta^j p), p=a*u_r+b*u_theta",
        exact_energy="e_j^2=int(lambda*|u_j|^2+gamma*|q_j|^2+alpha*|p_j|^2)",
        exact_top_block="H_j=H_0+2*j*diag(0,[[-v_theta,nu_theta],[nu_theta,-v_theta]]); nu=sqrt(alpha*gamma)",
        exact_lower_source="See R46 supplement: binomial commutators keep every lower derivative and d=tau+sigma_theta.",
        full_true_derivative_moments=moment_records,
        first_characteristic_derivative_rates=dict(
            forward=ball_record(first_forward),backward=ball_record(first_backward)),
        base_sqrt_energy_rates=dict(forward=ball_record(base_forward),backward=ball_record(base_backward)),
        triangular_comparison_generators={side:matrix_rows(A) for side,A in matrices.items()},
        whole_interval_comparison_maps={side:matrix_rows(A) for side,A in maps.items()},
        endpoint_energy_equivalence=dict(lower=ball_record(hmin),upper=ball_record(hmax)),
        full_Cauchy_and_ordinary_source=bounds,
        uniform_forward_backward_integer_P_s=integer_S,
        whole_fourier_operator=True,mean_retained=True,entire_parameter_family=True,
        coefficient_derivatives_in_exponential="Only the base signed rate and first characteristic angular derivative appear on the diagonal; all higher derivatives are strictly lower triangular.",
        composition_rule="At a shared radius the actual energies are identical. Compose the triangular maps before applying endpoint Sobolev equivalence; never multiply that equivalence per leaf.",
        full_strict_interval_proved=False,full_R46_strong_remainder_proved=False,
        whole_return_Rstar_proved=False,effective_cutoff_proved=False,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            "fourfold_phase_strict_core_energy.py","fourfold_phase_strict_core_kernel_tame_energy.py",
            "fourfold_phase_core_energy_fields.py","fourfold_phase_beta_bulk_interval.py",
            "fourfold_phase_beta_interval.py")},
        wall_seconds=time.monotonic()-start)
    save(args.out,out)
    print(dict(out=str(args.out),sha256=sha(args.out),seconds=out["wall_seconds"],
        integer_P_s={k:v["ball"] for k,v in integer_S.items()},
        first_characteristic_rates=out["first_characteristic_derivative_rates"]),flush=True)

if __name__=="__main__":main()

