#!/usr/bin/env python3
"""Pay the complete Hminus1 root Cauchy window and affine seam source norm.

Uses only the two original completed native inputs. All mathematics runs
in the public repository Actions, with actual process and failure records.
No original target, response or fold is recomputed.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,sys,time
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
REPAIR="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
PINS={"root_germ":"397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864",
      "root_budget":"10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f"}
G_SOURCE="a3ad50b828c69d3e6f1e9254c1f266535171741ee2cd675d1569ef8f0fac0491"
B_SOURCE="4a3ee217b21cabda6ae3dea052f27ff82f03b4218294145dc2f812891688e03e"

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)
def exact(value):
    x=Fraction(value);return arb(x.numerator)/x.denominator
def upper(value):return arb(value["upper"]).upper()
def lower(value):return arb(value["lower"]).lower()
def rec(value):
    x=arb(value);return dict(ball=x.str(60),lower=x.lower().str(60),upper=x.upper().str(60))
def power(x,p,q):return (arb(x).log()*p/q).exp()
def save(path,document):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(document,indent=2,allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,mtime=0)
    temp=path.with_name(path.name+".partial");temp.write_bytes(raw);temp.replace(path)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in PINS:p.add_argument("--"+name.replace("_","-"),type=Path,required=True)
    p.add_argument("--out",type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError("preserve every actual negative-one Cauchy outcome")
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematics runs only on the actual public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0"):
        raise RuntimeError("the exact directed arithmetic runtime changed")
    ctx.prec=256;started=time.monotonic()
    doc=dict(kind="actual_full_real_delta_negative_one_root_Cauchy_budget",complete=False,proved=False,
        source_sha256=sha(__file__),runtime=runtime,public_repository=PUBLIC,
        public_run_id=os.environ.get("GITHUB_RUN_ID"),public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        candidate_sha256=CANDIDATE,background_definition_sha256=REPAIR,
        explicit_direction_definition_sha256=DIRECTION,
        actual_intrinsic_parameter="eta_0",inputs={},gates=[],failure=None,
        all_full_frequency_states_sources_and_independent_even_mean_retained=True,
        full_delta96_and_quadratic_band192_paid=True,
        original_native_germ_and_response_recomputed=False,
        reverse_direction_not_inferred_from_old_forward_energy=True,
        root_reflection_finite_constant_strong_return_or_nonlinear_existence_claimed=False,
        positive_source_Sobolev_window_transferred=False,
        milliscale_radial_domain_certified=False,
        prescribed_affine_seam_source_contract_retained=True)
    def check(name,ok):
        ok=bool(ok);doc["gates"].append(dict(name=name,passed=ok))
        if not ok:raise ValueError("actual negative-one root Cauchy gate failed: "+name)
    try:
        for key,expected in PINS.items():
            path=getattr(a,key)
            if sha(path)!=expected:raise ValueError("a completed input changed: "+key)
            doc["inputs"][key]=dict(path=str(path),sha256=expected,bytes=path.stat().st_size)
        germ,rb=read(a.root_germ),read(a.root_budget)
        check("the two complete actual native identities and all original family coordinates remain",
            germ["complete"] and germ["proved"] and germ["source_sha256"]==G_SOURCE
            and germ["candidate_sha256"]==CANDIDATE and germ["all_finite_candidate_modes_retained"]
            and rb["complete"] and rb["proved"] and rb["source_sha256"]==B_SOURCE
            and str(rb["public_run_id"])=="43594466882"
            and rb["candidate_sha256"]==CANDIDATE and rb["background_definition_sha256"]==REPAIR
            and rb["explicit_direction_definition_sha256"]==DIRECTION
            and rb["actual_independent_even_mean_preserved"]
            and len(rb["response_repaired_complete_coefficient_upper"])==193
            and all(x["passed"] for x in rb["gates"]))
        R=Fraction(9,10**6);delta=Fraction(1,10**8)
        roots=list(map(Fraction,germ["root_interval"]))
        cell=list(map(Fraction,germ["exact_candidate_piece_interval"]))
        check("the entire real negative root interval and every actual real family parameter stay in the same piece",
            Fraction(rb["exact_complex_parameter_radius"])==delta
            and Fraction(rb["exact_outer_radial_radius"])==Fraction(1,100000)
            and Fraction(germ["complex_radial_radius"])==Fraction(1,100000)
            and Fraction(rb["exact_moving_Wiener_strip"])==Fraction(1,1024)
            and roots==list(map(Fraction,rb["exact_root_interval"]))
            and cell[0]<roots[0]-R and roots[1]<cell[1]
            and germ["actual_candidate_piece"]==rb["exact_candidate_and_response_piece"]==2549
            and germ["compact_bump_identically_zero_on_entire_actual_germ"]
            and germ["domain_contains_disks_about_every_true_parameter_root"])
        intr=germ["complex_intrinsic_coefficients"]
        kr_low=lower(intr["K1"]["real"]);kr_high=upper(intr["K1"]["real"])
        q2=(exact(R)*kr_high).upper()
        U=[upper(x) for x in rb["full_family_U_angular_norms"]]
        V=[upper(x) for x in rb["full_family_V_angular_norms"]]
        b=upper(rb["beta_abs_upper"]);gamma=upper(rb["gamma_abs_upper"])
        eta=(gamma*upper(rb["full_complex_mean_abs_upper"])).upper()
        amax=exact(Fraction(63,50))
        check("the true intrinsic real slope and complete characteristic coefficient satisfy the regular weight hypotheses",
            kr_low>59 and kr_high>0 and q2<exact(Fraction(61,100000))
            and eta<amax and gamma<exact(Fraction(28,25)) and b<exact(Fraction(211,1000)))
        check("complete full-family physical angular coefficient norms through two meet the declared strict bounds",
            len(U)==len(V)==5
            and all(U[j]<exact(v) for j,v in enumerate(("0.630","2.615","11.365")))
            and all(V[j]<exact(v) for j,v in enumerate(("1.791","2.803","12.378"))))
        W=(1+q2).sqrt().upper();qmax=q2.sqrt().upper()
        theta_inverse=amax.exp().upper()
        check("the regular raw reconstruction and exact physical frequency-lag bounds are uniform at the root",
            W<exact(Fraction(1001,1000)) and qmax<exact(Fraction(1,40))
            and theta_inverse<4 and power(arb(769),1,3)<10
            and 2*amax<arb(1).exp())
        l11=(b*(1+3*U[0]**2+q2*V[0]**2)).upper()
        l22=(b*(1+U[0]**2+3*q2*V[0]**2)).upper()
        ell=(2*b*U[0]*V[0]).upper()
        l11_phi=(b*(6*U[0]*U[1]+2*q2*V[0]*V[1])).upper()
        l22_phi=(b*(2*U[0]*U[1]+6*q2*V[0]*V[1])).upper()
        ell_phi=(2*b*(U[1]*V[0]+U[0]*V[1])).upper()
        check("the complete local reaction and first angular derivatives are finite",
            all(x.is_finite() for x in (l11,l22,ell,l11_phi,l22_phi,ell_phi)))
        diagonal=(10*(l11+l11_phi+l22+l22_phi)).upper()
        cross=(4*(qmax+W)*(ell+ell_phi)).upper()
        loc=(diagonal+cross).upper()
        d1=(b*(U[0]**2+q2*V[0]**2)).upper()
        d2=(2*b*(U[0]*U[1]+q2*V[0]*V[1])).upper()
        drift=(d1/2+exact(Fraction(40,3))*(d1+d2)).upper()
        Iminus1=(arb(17).sqrt()/4).upper()
        primitive=(8*b*Iminus1*(U[1]+V[1])
                   *(W*(U[0]+U[1])+q2*(V[0]+V[1]))).upper()
        mean=(4*gamma*(q2*V[1]+U[1])).upper()
        check("the new diagonal and cross multiplier costs are paid on the declared negative-one window",
              diagonal<40 and cross<15 and loc<55)
        check("the four-thirds logarithmic lag loss and full drift energy are paid",
              drift<12)
        check("the exact old primitive maps Hminus1 to L2 and its ordered products are paid",
              Iminus1<exact(Fraction(33,32)) and primitive<33)
        check("the genuine independent even mean remains in the new weighted energy",
              mean<12)
        total=(loc+drift+primitive+mean).upper()
        check("the complete negative-one energy growth is below112",
              total<112)
        growth=(112*exact(R)).exp().upper()
        raw=(4*W*growth).upper()
        root_factor=exact(Fraction(41,10))
        source_length=exact(R).sqrt()
        check("the full negative-one Cauchy and complete ordinary-source bounds close",
            Fraction(3,1000)**2==R and raw<root_factor)
        density=(root_factor*Iminus1).upper()
        check("the original primitive after genuine propagation has the paid L2 output factor",
              density<exact(Fraction(17,4)))
        doc.update(exact_real_parameter_radius=str(delta),exact_negative_radial_length=str(R),
            exact_root_interval=list(map(str,roots)),actual_original_piece=2549,
            exact_root_state_norm="sqrt(||h1(root)||_Hminus2/3^2+||h2(root)||_Hminus1^2)",
            ordinary_source_norm="L2_rho(Hminus2/3 x Hminus2/3), normalized circle, complete even mean",
            sharper_anisotropic_source_norm="L2_rho(Hminus2/3 x Hminus1)",
            output_norm="sup_0<=rho<=9e-6 complete pair Hminus1",
            propagation_direction="from rho=0 root to increasing rho on the negative side",
            root_state_factor=str(Fraction(41,10)),
            ordinary_source_factor_inside_bracket=str(Fraction(3,1000)),
            affine_seam_factor_inside_bracket="1",
            affine_seam_input_norm="sum sqrt(||j1||_Hminus2/3^2+||j2||_Hminus1^2)",
            propagated_old_primitive_output_factor=str(Fraction(17,4)),
            only_the_stated_negative_one_Sobolev_window_proved=True,
            no_reverse_estimate_inferred=True,
            true_energy_weight="Lambda^-1*theta*diag(1/w,1); w^2=q^2+Lambda^-2/3*exp(-rho*Lambda^2/3)",
            theta_weight="exp[-(63/50)(1-exp(-rho*Lambda^2/3))]",
            exact_full_background_degree=96,exact_full_quadratic_band=192,maximum_physical_lag=768,
            logarithmic_multiplier_derivative_bound="4/3",
            finite_lag_multiplier_bound="10*(1+abs(physical_lag))",
            finite_lag_derivative_commutator_bound="(40/3)*abs(physical_lag)*(1+abs(physical_lag))",
            complete_U_angular_norms=[rec(x) for x in U],
            complete_V_angular_norms=[rec(x) for x in V],
            bounds={name:rec(value) for name,value in dict(Krho_lower=kr_low,Krho_upper=kr_high,
                q_squared_upper=q2,gamma=gamma,beta=b,eta=eta,w_upper=W,
                theta_inverse_upper=theta_inverse,L11=l11,L22=l22,ell=ell,
                L11_phi=l11_phi,L22_phi=l22_phi,ell_phi=ell_phi,
                local_diagonal_growth=diagonal,local_cross_growth=cross,local_growth=loc,
                drift_phi=d1,drift_phiphi=d2,drift_growth=drift,
                primitive_Hminus1_to_L2=Iminus1,primitive_growth=primitive,
                genuine_mean_rank_growth=mean,total_growth=total,
                energy_exponential=growth,actual_raw_state_factor=raw,
                old_primitive_after_propagation_factor=density).items()},
            complete=True,proved=True)
    except Exception as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
        doc["seconds"]=time.monotonic()-started;save(a.out,doc);raise
    doc["seconds"]=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,gates=len(doc["gates"]),bounds=doc["bounds"],seconds=doc["seconds"])),flush=True)

if __name__=="__main__":main()
