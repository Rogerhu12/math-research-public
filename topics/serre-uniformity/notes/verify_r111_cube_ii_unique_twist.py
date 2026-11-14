#!/usr/bin/env python3
"""R111: the five-division local certificate and unique family-II twist.

Uses Python's standard library and PARI/GP.  --write regenerates the small
certificate; --check recomputes all fields and local models from scratch.
No stored number-field cache, class group, GRH assumption, or numerical test.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
DEFAULT = Path(__file__).with_name("r111_cube_ii_unique_twist_certificate.json")


def residue_table() -> list[dict]:
    rows = []
    for a in (1, 5, 7, 11, 13, 17, 19, 23):
        eta = 1 if a % 3 == 1 else -1
        unramified_sign = 1 if a % 8 in (1, 3) else -1
        candidates = (eta, -2 * eta)
        chosen = [d for d in candidates if (1 if d > 0 else -1) == unramified_sign]
        assert len(chosen) == 1
        rows.append({"a_mod_24": a, "a_mod_3_symbol": eta,
                     "minus_two_over_a": unramified_sign,
                     "six_over_a": eta * unramified_sign, "unique_d": chosen[0]})
    assert [r["unique_d"] for r in rows] == [1, -1, -2, 2, -2, 2, 1, -1]
    return rows


GP_PROGRAM = r"""
default(parisizemax,400000000);
print("VERSION|",version());
K=nfinit(z^2-3);r=Mod(z,z^2-3);B1=ellinit([0,4,0,2*(1-r),0],K);
D=elldivpol(B1,5,y);P=5^11*subst(D,y,y/5);
if(poldegree(P)!=12 || pollead(P)!=1,error("wrong scaled five-division polynomial"));
print("RELATIVE_POLYNOMIAL|",lift(P));
RH=rnfequation(K,P,1);PH=polredbest(RH[1],1);
if(!polisirreducible(PH[1]),error("x-coordinate field reducible"));
H=nfinit(PH[1]);rh=subst(lift(RH[2]),y,PH[2]);
zh=PH[2]-RH[3]*rh;xh=zh/5;fh=xh^3+4*xh^2+2*(1-rh)*xh;
if(rh^2!=3 || substvec(lift(P),[y,z],[zh,rh])!=0,error("x-coordinate embedding"));
print("X_FIELD|",H.pol,"|",H.disc,"|",vector(#idealprimedec(H,2),i,[idealprimedec(H,2)[i].e,idealprimedec(H,2)[i].f]));
S=rnfequation(H,x^2-625*fh,1);PL=polredbest(S[1],1);
if(!polisirreducible(PL[1]),error("point field reducible"));
L=nfinit(PL[1]);hl=subst(lift(S[2]),x,PL[2]);rl=subst(lift(rh),y,hl);
xl=subst(lift(xh),y,hl);wl=PL[2]-S[3]*hl;yl=wl/25;
B=ellinit([0,4,0,2*(1-rl),0],L);
if(rl^2!=3 || !ellisoncurve(B,[xl,yl]) || yl==0,error("point embedding"));
if(ellmul(B,[xl,yl],5)!=[0],error("not a five-torsion point"));
Pr=idealprimedec(L,2);
print("POINT_FIELD|",L.pol,"|",L.disc,"|",vector(#Pr,i,[Pr[i].e,Pr[i].f]));
sel=select(k->Pr[k].f==1,vector(#Pr,i,i));
if(#sel!=1,error("expected a unique residue-degree-one prime"));
Q=Pr[sel[1]];
print("LOCAL_POWERS|",vector(4,i,nfislocalpower(L,Q,[2,-2,-1,5][i],2)));
for(j=1,2,my(h=[-1,7][j],E=ellinit([0,4,0,2*(1+rl*h),0],L),R=elllocalred(E,Q),Em=ellchangecurve(E,R[3]),V=vector(4,i,if(R[3][i]==0,999,idealval(L,R[3][i],Q))),A=vector(5,i,if(Em[i]==0,999,idealval(L,Em[i],Q))));if(R[1]!=0,error("not good reduction"));print("MODEL|",h,"|",R[1],"|",R[2],"|",idealval(L,Em.disc,Q),"|",V,"|",A,"|",ellap(Em,Q),"|",[80-4*V[1],80+V[2]-6*V[1]]));
quit
"""


def exact_gp(gp: str) -> dict:
    run = subprocess.run([gp, "-fq"], input=GP_PROGRAM, text=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    errors = [s for s in run.stderr.splitlines() if "***" in s and "Warning:" not in s]
    if run.returncode or errors:
        raise RuntimeError(run.stdout + run.stderr)
    out = {"local_models": []}
    for line in run.stdout.splitlines():
        a = line.split("|")
        if a[0] == "VERSION":
            out["pari_version_used"] = json.loads(a[1])
        elif a[0] == "RELATIVE_POLYNOMIAL":
            out["scaled_five_division_polynomial"] = a[1]
        elif a[0] in ("X_FIELD", "POINT_FIELD"):
            out[a[0].lower()] = {"polynomial": a[1], "discriminant": int(a[2]),
                                 "primes_over_2_e_f": json.loads(a[3])}
        elif a[0] == "LOCAL_POWERS":
            out["local_square_tests_2_minus2_minus1_5"] = json.loads(a[1])
        elif a[0] == "MODEL":
            out["local_models"].append({"H": int(a[1]), "conductor_exponent": int(a[2]),
                "pari_kodaira_code": int(a[3]), "minimal_discriminant_valuation": int(a[4]),
                "change_u_r_s_t_valuations": json.loads(a[5]),
                "minimal_a1_a2_a3_a4_a6_valuations": json.loads(a[6]),
                "good_reduction_trace_over_F2": int(a[7]),
                "H_plus_16_delta_a4_a6_lower_bounds": json.loads(a[8])})
        elif line.strip():
            raise RuntimeError("Unexpected GP output: " + line)
    assert out["x_field"]["discriminant"] == 2**66 * 3**12 * 5**22
    assert out["point_field"]["discriminant"] == 2**174 * 3**24 * 5**46
    assert out["x_field"]["primes_over_2_e_f"] == [[8, 1], [8, 2]]
    assert out["point_field"]["primes_over_2_e_f"] == [[16, 1], [16, 2]]
    assert out["local_square_tests_2_minus2_minus1_5"] == [1, 0, 0, 0]
    assert [m["H"] for m in out["local_models"]] == [-1, 7]
    for m in out["local_models"]:
        assert (m["conductor_exponent"], m["pari_kodaira_code"],
                m["minimal_discriminant_valuation"], m["good_reduction_trace_over_F2"]) == (0, 1, 0, -2)
        assert m["change_u_r_s_t_valuations"] == [14, 12, 6, 26]
        assert m["minimal_a1_a2_a3_a4_a6_valuations"] == [8, 0, 0, 1, 1]
        assert m["H_plus_16_delta_a4_a6_lower_bounds"] == [24, 8]
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gp", default=shutil.which("gp"))
    ap.add_argument("--certificate", type=Path, default=DEFAULT)
    modes = ap.add_mutually_exclusive_group()
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    ap.add_argument("--residue-table-only", action="store_true")
    args = ap.parse_args()
    rows = residue_table()
    if args.residue_table_only:
        print(json.dumps(rows, indent=2))
        return
    if not args.gp:
        ap.error("supply --gp /path/to/gp")
    result = {"schema": "R111-cube-II-unique-twist-v1", "residue_table": rows,
              "exact_pari": exact_gp(args.gp)}
    if args.write:
        args.certificate.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        print("Wrote", args.certificate)
    else:
        saved = json.loads(args.certificate.read_text())
        saved["exact_pari"]["pari_version_used"] = result["exact_pari"]["pari_version_used"]
        assert saved == result, "Recomputed certificate differs"
        print("R111: all fields, local square tests, minimal models, traces and residues match")
    print("Unique family-II d for a=1,5,7,11,13,17,19,23 mod24: 1,-1,-2,2,-2,2,1,-1")


if __name__ == "__main__":
    main()
