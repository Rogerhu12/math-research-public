#!/usr/bin/env python3
"""Actual nonmean root G,q,k and optional endpoint Fourier-Taylor references.

Run in the topic directory. This is a new executable entry point; merely saving
it is not an execution certificate. The output defines exact dyadic references
and pays geometry balls, DFT roundoff, all aliases and both omitted complements.
Original-height reduced density is kept. No angular average substitutes for G.
Optional Sreg,Ltheta,U0,U1 preserve the complete endpoint and exact-derivative
terms. Their tails require the newly executed common-root bidisk certificate.
"""
from __future__ import annotations
import argparse, json, math, time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import acb, acb_series, arb, ctx
from fourfold_phase_beta_interval import (
    add_real_cauchy_error, array_derivative, ball_record,
    series_constant, vector_cross, vector_dot)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_root_fourier_fit import read, save, sha, dyadic, stored
from fourfold_subprincipal_root_fields import RootPhaseModel

MIGRATION_PATH = "notes/2026-11-13-R106-whole-parameter-root-density.json"
MIGRATION_SHA = "e465844f0880356afd80829a4fc782856db7fc61e513be2669d84a61e80f8a09"
COARSE_PATH = "notes/2026-11-13-R106-coarse-root-finite-part.json"
COARSE_SHA = "da377ff1bd64f53b436eee714bda394f288cea8c41e167da0a680ea1ab4d6f4e"
BASE_FIELDS = ("G", "q", "kstar")
AUXILIARY_FIELDS = ("Sreg", "Ltheta", "U0", "U1")
PARITY = {"G": 1, "q": -1, "kstar": 1, "Sreg": -1,
          "Ltheta": -1, "U0": 1, "U1": 1}


def checked_save(path, value):
    save(path, value)
    if Path(path).stat().st_size >= 5_000_000:
        raise ValueError("output exceeds repository single-file limit; use fewer rows per shard")


def genuine_node_fields(F, X, Frr, Y, Frt, Ftt, K, kap, scale):
    """Same exact six-jet formula as frozen root_density_taylor, before mean."""
    normal = vector_cross(Y, X)
    nr1, nr2 = vector_cross(Frt, X), vector_cross(Y, Frr)
    nt1, nt2 = vector_cross(Ftt, X), vector_cross(Y, Frt)
    nr = [nr1[c]+nr2[c] for c in range(3)]
    nt = [nt1[c]+nt2[c] for c in range(3)]
    area2, radius2, support = vector_dot(normal, normal), vector_dot(F, F), vector_dot(normal, F)
    l, m, n = [vector_dot(normal, w) for w in (Frr, Frt, Ftt)]
    aa, bb, cc = -n/area2, m/area2, -l/area2
    for name, value in (("area2", area2), ("radius2", radius2),
                        ("support", support), ("a0", aa), ("Fz", F[2])):
        if not value[0].real > 0:
            raise ValueError("unresolved actual nodal root denominator "+name)
    actualK = (l*n-m*m)/(area2*area2)
    omega, chat = (actualK-K)/aa, (bb*bb+K)/aa
    FX, FY = vector_dot(F, X), vector_dot(F, Y)
    d = (aa*(vector_dot(X, X)-FX*FX/radius2)
         +2*bb*(vector_dot(X, Y)-FX*FY/radius2)
         +cc*(vector_dot(Y, Y)-FY*FY/radius2))/radius2
    lzr = vector_dot(nr, F)/support-vector_dot(normal, nr)/area2-FX/radius2
    lzt = vector_dot(nt, F)/support-vector_dot(normal, nt)/area2-FY/radius2
    Lrho, Ltheta = kap.derivative()/(scale*kap)+2*lzr, -2*lzt
    ell = Y[2]/F[2]-FY/radius2
    A = -aa/(16*kap)
    B = -(aa*Lrho-bb*Ltheta)/(4*kap)
    C = (d+omega*(ell*ell+ell*Ltheta)
         -(aa*Lrho*Lrho-2*bb*Lrho*Ltheta+chat*Ltheta*Ltheta)/4)/kap
    rho = acb_series([0, acb(scale)])
    G = A+rho*B+rho*rho*C
    # Positive physical root -> inward rho reverses the mixed coefficient.
    q, kstar = -bb/aa, kap/aa
    identity = G[0]*kstar[0]+acb(1)/16
    if not identity.real.contains(0) or not identity.imag.contains(0):
        raise ValueError("actual leading identity k0*G0=-1/16 failed")
    return {"G": G, "q": q, "kstar": kstar,
            "Sreg": omega*ell/kap, "Ltheta": Ltheta,
            "U0": aa/(2*kap), "U1": (aa*Lrho-bb*Ltheta)/kap}


def angular_complement(N, K, outer_physical, inner_physical):
    """Sup of complete nonretained/aliased angular modes for a unit strip bound."""
    So, Si = 4*outer_physical, 4*inner_physical
    if not So > Si >= 0 or not 0 <= K < N//2:
        raise ValueError("invalid full Fourier layout")
    denom = 1-(-So*N).exp()
    alias = arb(0)
    for k in range(-K, K+1):
        alias += (Si*abs(k)).exp()*(
            (-So*(N-abs(k))).exp()+(-So*(N+abs(k))).exp())/denom
    gap = So-Si
    tail = 2*(-gap*(K+1)).exp()/(1-(-gap).exp())
    return alias.upper(), tail.upper()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--root-certificate", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json"))
    p.add_argument("--half-width", type=Fraction, default=Fraction(1, 10**9))
    p.add_argument("--nodes", type=int, default=512)
    p.add_argument("--angles", type=int, default=1024)
    p.add_argument("--keep", type=int, default=450)
    p.add_argument("--degree", type=int, default=24)
    p.add_argument("--precision", type=int, default=36)
    p.add_argument("--bits", type=int, default=256)
    p.add_argument("--working-radius", type=Fraction, default=Fraction(7, 25000))
    p.add_argument("--working-strip", type=Fraction, default=Fraction(1, 800))
    p.add_argument("--rows-per-shard", type=int, default=4)
    p.add_argument("--domain-report", type=Path, help="optional newly completed wider common root bidisk")
    p.add_argument("--include-root-aux", action="store_true",
                   help="also preserve Sreg,Ltheta,U0,U1; requires a complete actual bidisk report")
    p.add_argument("--out-dir", type=Path, required=True)
    a = p.parse_args()
    names = BASE_FIELDS+AUXILIARY_FIELDS if a.include_root_aux else BASE_FIELDS
    if a.include_root_aux and not a.domain_report:
        raise ValueError("root auxiliary tails require a newly executed actual common bidisk")
    if a.out_dir.exists():
        raise ValueError("new output directory required; preserve any prior partial")
    if not 0 < a.half_width <= Fraction(1, 10**9):
        raise ValueError("requested parameter family outside paid actual box")
    if a.angles < a.nodes or a.angles % 2 or not 0 <= a.keep < a.angles//2:
        raise ValueError("invalid true angular grid")
    if a.precision < a.degree+8 or a.rows_per_shard < 1:
        raise ValueError("insufficient actual coefficient precision or shard layout")
    if sha(MIGRATION_PATH) != MIGRATION_SHA or sha(COARSE_PATH) != COARSE_SHA:
        raise ValueError("completed outer geometry certificate bytes changed")
    mig, coarse = read(MIGRATION_PATH), read(COARSE_PATH)
    if not mig["complete"] or not coarse["complete"]:
        raise ValueError("incomplete actual outer root geometry")
    if Fraction(mig["proved_region"]["complex_root_radius"]) != Fraction(1, 2500):
        raise ValueError("unexpected paid true root disk")
    if Fraction(mig["proved_region"]["physical_theta_strip"]) != Fraction(1, 320):
        raise ValueError("unexpected paid true angle strip")
    ctx.prec, ctx.cap = a.bits, 10
    started, cpu = time.monotonic(), time.process_time()
    model = RootPhaseModel(a.object, a.half_width, a.root_certificate,
                          Fraction(1, 320), nodes=a.nodes, refine_steps=3)
    target = model.target
    ident = provenance(target, a.object)
    expected_center = Fraction(mig["proved_region"]["parameter_center"])
    if sha(a.object) != "91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848":
        raise ValueError("not the paid exact delta5 object")
    if target.parameter_center != expected_center:
        raise ValueError("actual affine center mismatch")
    ctx.cap = a.precision
    target.angles = a.angles
    outer_radius, outer_strip = Fraction(1,2500), Fraction(1,320)
    outer_inputs=[{"path":MIGRATION_PATH,"sha256":MIGRATION_SHA},
                  {"path":COARSE_PATH,"sha256":COARSE_SHA}]
    bounds = {"G": exact_arb(Fraction(mig["bounds"]["safe_G_bound"])),
              "q": exact_arb(Fraction(coarse["bounds"]["q_safe"]["exact_upper"])),
              "kstar": exact_arb(Fraction(coarse["bounds"]["kstar_safe"]["exact_upper"]))}
    if a.domain_report:
        domain=read(a.domain_report)
        source_name=domain.get("source_file","fourfold_subprincipal_root_bidisk_domain.py")
        if source_name not in ("fourfold_subprincipal_root_bidisk_domain.py",
                              "fourfold_subprincipal_root_bidisk_boundary.py",
                              "fourfold_subprincipal_root_bidisk_boundary_v2.py"):
            raise ValueError("unknown actual root-bidisk producer")
        source=Path(__file__).with_name(source_name)
        if (not domain.get("complete") or not domain.get("proved")
            or domain.get("kind")!="R106_actual_common_root_Gqk_bidisk"
            or domain["source_sha256"]!=sha(source)
            or domain["object_sha256"]!=sha(a.object)
            or domain["root_certificate_sha256"]!=sha(a.root_certificate)
            or domain["rows_done"]!=domain["angles"]
            or len(domain["qk_cells"])!=domain["angles"]):
            raise ValueError("wider common bidisk is incomplete or changed")
        did=domain["identity"]
        for name in ("origin_inputs_sha256","direction_sha256","exact_center_parameter"):
            if did[name]!=ident[name]:raise ValueError("wider domain actual identity mismatch")
        if Fraction(did["exact_parameter_half_width"])<a.half_width:
            raise ValueError("wider domain omits part of the requested parameter box")
        for name,digest in domain["dependencies"].items():
            if sha(Path(__file__).with_name(name))!=digest:
                raise ValueError("wider domain dependency changed "+name)
        outer_radius=Fraction(domain["outer_rho_radius"])
        outer_strip=Fraction(domain["outer_physical_angle_strip"])
        bounds={"G":stored(domain["uniform_G_bound"]).upper(),
                "q":stored(domain["uniform_q_bound"]).upper(),
                "kstar":stored(domain["uniform_kstar_bound"]).upper()}
        if a.include_root_aux:
            aux=domain.get("uniform_root_auxiliary_bounds",{})
            if set(aux)!=set(AUXILIARY_FIELDS):
                raise ValueError("actual auxiliary moduli are not complete")
            bounds.update({name:stored(aux[name]).upper() for name in AUXILIARY_FIELDS})
        outer_inputs.append({"path":str(a.domain_report),"sha256":sha(a.domain_report)})
    R, S=exact_arb(outer_radius),exact_arb(outer_strip)
    r, s = exact_arb(a.working_radius), exact_arb(a.working_strip)
    if not 0 < r < R or not 0 <= s < S:
        raise ValueError("approximation domain is not inside true paid domain")
    # This second target call is at the full requested precision.
    cf, radius, E, C, K = target.target(model.root, model.scale, model.budget)
    K = acb_series([0]+[K[j] for j in range(1,K.prec)], prec=K.prec)
    k2 = acb_series([-K[j+1]/model.scale for j in range(K.prec-1)], prec=K.prec-1)
    if not k2[0].real > 0:
        raise ValueError("unresolved actual target root branch")
    kap = k2.sqrt()
    fields = []
    for b in range(3):
        values = target.evaluate(target.angular(cf, b))
        for key in np.ndindex(values.shape):
            values[key] = add_real_cauchy_error(values[key], model.budget["field_errors"][b],
                                                model.scale, model.budget["radial_radius"])
        fields.append(values)
    F, Y, Ftt = fields
    half = {name: [] for name in names}
    a.out_dir.mkdir(parents=True)
    report = {"kind":"R106_actual_nonmean_root_G_q_k_Fourier_Taylor",
       "preserved_fields":list(names),"root_auxiliary_fields_included":a.include_root_aux,
       "complete":False,"proved":False,"source_sha256":sha(__file__),
       "identity":ident,"object_path":str(a.object),"object_sha256":sha(a.object),
       "root_certificate_path":str(a.root_certificate),"root_certificate_sha256":sha(a.root_certificate),
       "root":ball_record(model.root),"root_common_spans":model.spans,
       "outer_geometry_inputs":outer_inputs,
       "outer_rho_radius":str(outer_radius),"outer_physical_angle_strip":str(outer_strip),
       "complete_true_outer_bounds":{name:ball_record(value) for name,value in bounds.items()},
       "working_rho_radius":str(a.working_radius),"working_physical_angle_strip":str(a.working_strip),
       "radial_variable":"w=rho/scale; the saved coefficient at row n multiplies w**n",
       "radial_scale_dyadic":dyadic(model.scale),"angular_variable":"exp(4*i*k*physical_theta)",
       "degree":a.degree,"series_precision":a.precision,"N":a.angles,"K":a.keep,
       "primitive_nodes":a.nodes,"bits":a.bits,"rows_done":0,"coefficient_shards":[],"nodal_shards":[],
       "parity":{name:("even, real cosine coefficients" if PARITY[name]>0
                       else "odd, imaginary positive coefficients") for name in names},
       "root_auxiliary_convention":(
           "Sreg=s*S; V_rho=s^-3*U0+s^-1*U1; inward Lrho_regular and original-height Ltheta"),
       "full_nonmean_return_phase_proved":False,"effective_R104_cutoff_proved":False,
       "dependencies":{name:sha(Path(__file__).with_name(name)) for name in (
        "fourfold_subprincipal_root_fields.py","fourfold_phase_beta_interval.py",
        "fourfold_phase_beta_parameter_germ.py","fourfold_phase_root_cauchy_frame_ci_v1.py",
        "fourfold_phase_root_fourier_fit.py","fourfold_native_series_fft.py")}}
    def checkpoint():
        report["wall_seconds"]=time.monotonic()-started
        report["cpu_seconds"]=time.process_time()-cpu
        checked_save(a.out_dir/"report.json",report)
    checkpoint()
    node_pending=[]
    for j in range(a.angles//2+1):
        Fj, Yj, Fttj = list(F[j]), list(Y[j]), list(Ftt[j])
        Xj=[v.derivative()/(-model.scale) for v in Fj]
        Frrj=[v.derivative()/(-model.scale) for v in Xj]
        Frtj=[v.derivative()/(-model.scale) for v in Yj]
        out=genuine_node_fields(Fj,Xj,Frrj,Yj,Frtj,Fttj,K,kap,model.scale)
        for name in names:
            if out[name].prec <= a.degree:
                raise ValueError("unknown actual radial coefficient would be filled")
            row=[]
            for n in range(a.degree+1):
                z=out[name][n]
                if not z.imag.contains(0):
                    raise ValueError("true real radial Taylor coefficient lost its real axis")
                row.append(z.real)
            if PARITY[name]<0 and j in (0,a.angles//2):
                if any(not v.contains(0) for v in row):
                    raise ValueError("exact odd endpoint failed")
                row=[arb(0) for _ in row]
            half[name].append(row)
        node_pending.append({"index":j,"normalized_angle_over_pi":str(Fraction(2*j,a.angles)),
            "fields":{name:[ball_record(v) for v in half[name][-1]] for name in names}})
        if len(node_pending)==32 or j==a.angles//2:
            path=a.out_dir/f"nodes_{node_pending[0]['index']:05d}_{j:05d}.json.gz"
            checked_save(path,{"kind":"R106_actual_nonmean_root_Taylor_nodes",
                "source_sha256":sha(__file__),"identity":ident,
                "radial_scale_dyadic":dyadic(model.scale),"degree":a.degree,
                "grid":a.angles,"nodes":node_pending})
            report["nodal_shards"].append({"path":str(path),"sha256":sha(path),
                "first":node_pending[0]["index"],"last":j})
            node_pending=[]
        report["rows_done"]=j+1
        if j%32==0:
            checkpoint()
            print({"actual_half_nodes":j+1,"total":a.angles//2+1},flush=True)
    del fields,F,Y,Ftt,cf
    alias, omitted=angular_complement(a.angles,a.keep,S,s)
    weight=[(4*s*k).exp() for k in range(a.keep+1)]
    # Exact Parseval transport of all nodal interval errors into retained
    # weighted l1, plus independent actual DFT and dyadic-choice errors.
    weight_l2=(1+2*sum((w*w for w in weight[1:]),arb(0))).sqrt()
    totals={name:{"node_dft_choice":arb(0),"alias":arb(0),"omitted_angle":arb(0)} for name in names}
    pending=[]
    for n in range(a.degree+1):
        encoded={"radial_row":n,"fields":{}}
        for name in names:
            vhalf=[half[name][j][n] for j in range(a.angles//2+1)]
            full=vhalf+[PARITY[name]*v for v in reversed(vhalf[1:-1])]
            mid=[v.mid() for v in full]
            radii=[abs(v-c).upper() for v,c in zip(full,mid)]
            rms=(sum((v*v for v in radii),arb(0))/a.angles).sqrt()
            transformed=[v/a.angles for v in acb.dft([acb(v) for v in mid])]
            coefficients=[];roundoff=arb(0)
            for k in range(a.keep+1):
                z=transformed[k]
                if PARITY[name]>0:
                    if not z.imag.contains(0):raise ValueError("even DFT not real")
                    value=z.real
                else:
                    if not z.real.contains(0):raise ValueError("odd DFT not imaginary")
                    value=z.imag
                if k==0 and PARITY[name]<0:
                    middle=arb(0)
                else:
                    middle=value.mid()
                coefficients.append(dyadic(middle))
                roundoff+=(1 if k==0 else 2)*weight[k]*abs(value-middle)
            node_fee=(weight_l2*rms+roundoff).upper()
            radial_weight=(r/model.scale)**n
            true_coefficient_bound=bounds[name]*(model.scale/R)**n
            fees={"node_dft_choice":node_fee,
                  "alias":true_coefficient_bound*alias,
                  "omitted_angle":true_coefficient_bound*omitted}
            for label,value in fees.items():totals[name][label]+=radial_weight*value
            encoded["fields"][name]={"positive_coefficients":coefficients,
                                    "radial_coefficient_node_error":ball_record(node_fee)}
        pending.append(encoded)
        if len(pending)==a.rows_per_shard or n==a.degree:
            path=a.out_dir/f"coefficients_{pending[0]['radial_row']:04d}_{n:04d}.json.gz"
            checked_save(path,{"kind":"R106_exact_dyadic_root_reference_coefficients",
                 "identity":ident,"N":a.angles,"K":a.keep,
                 "radial_scale_dyadic":dyadic(model.scale),"rows":pending})
            report["coefficient_shards"].append({"path":str(path),"sha256":sha(path),
                 "first_row":pending[0]["radial_row"],"last_row":n})
            pending=[];checkpoint()
    errors={}
    for name in names:
        radial_tail=bounds[name]*(r/R)**(a.degree+1)/(1-r/R)
        pieces={**totals[name],"omitted_radial":radial_tail}
        errors[name]={"complete_sup_error":ball_record(sum(pieces.values(),arb(0)).upper()),
                      "pieces":{label:ball_record(value.upper()) for label,value in pieces.items()},
                      "norm_semantics":"complete sup on working complex bidisk; not an asserted full Wiener norm"}
    report.update(complete=True,proved=True,complete_approximant_errors=errors,
       proof="R106 root Taylor formula before angular mean; coefficient Cauchy on the pinned complete bidisk; full signed DFT aliases and omitted radial complement are separately paid.",
       no_missing_radial_rows=[x for item in report["coefficient_shards"] for x in range(item["first_row"],item["last_row"]+1)]==list(range(a.degree+1)))
    if not report["no_missing_radial_rows"]:raise ValueError("coefficient shard coverage failed")
    checkpoint()
    print({"complete":True,"report":str(a.out_dir/"report.json"),
           "sha256":sha(a.out_dir/"report.json"),
           "errors":{name:errors[name]["complete_sup_error"] for name in names}},flush=True)


if __name__=="__main__":
    main()
