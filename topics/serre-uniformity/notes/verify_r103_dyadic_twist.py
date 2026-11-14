#!/usr/bin/env python3
"""Exact degree-16 local-field certificate for R103 (standard Python + PARI/GP)."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
DEFAULT = Path(__file__).with_name("r103_dyadic_twist_certificate.json")

GP_PROGRAM = r"""
default(parisizemax,400000000);
print("VERSION|",version());
K=nfinit(z^2-3); r=Mod(z,z^2-3);
RH=rnfequation(K,y^4+16*y^3+18*(2+r)*y^2-27*(2+r)^2,1);
H=nfinit(RH[1]); rh=RH[2]; zh=Mod(y,RH[1])-RH[3]*rh; xh=zh/3;
fh=xh^3+4*xh^2+(2+rh)*xh;
if(!polisirreducible(RH[1]),error("base polynomial reducible"));
print("BASE|",H.pol,"|",H.disc,"|",RH[3]);
for(j=1,2,my(d=[1,2][j],S=rnfequation(H,x^2-81*d*fh,1),L=nfinit(S[1]),yh=S[2],rl=subst(lift(rh),y,yh),zl=subst(lift(zh),y,yh),wl=Mod(x,S[1])-S[3]*yh,Pr=idealprimedec(L,2)); if(!polisirreducible(S[1]),error("point polynomial reducible")); if(#Pr!=1,error("unexpected prime splitting")); my(P=Pr[1],B0=ellinit([0,4*d,0,(2+rl)*d^2,0],L),Pt=[d*zl/3,d*wl/9]); if(ellmul(B0,Pt,3)!=[0],error("not 3-torsion")); print("FIELD|",d,"|",L.pol,"|",L.disc,"|",P.e,"|",P.f,"|",S[3]); print("REFERENCE|",d,"|",elllocalred(B0,P)[1]); for(k=1,2,my(h=[2,6][k],B=ellinit([0,4,0,2*(1+rl*h),0],L),R=elllocalred(B,P),Bm=ellchangecurve(B,R[3]),V=vector(4,i,if(R[3][i]==0,999,idealval(L,R[3][i],P))),A=vector(5,i,if(Bm[i]==0,999,idealval(L,Bm[i],P)))); print("MODEL|",d,"|",h,"|",R[1],"|",R[2],"|",idealval(L,Bm.disc,P),"|",V,"|",A,"|",[32-4*V[1],32+V[2]-6*V[1]])));
quit
"""


def generate(gp: str) -> dict:
    run = subprocess.run([gp, "-fq"], input=GP_PROGRAM, text=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    errors = [line for line in run.stderr.splitlines()
              if "***" in line and "Warning:" not in line]
    if run.returncode or errors:
        raise RuntimeError(run.stdout + run.stderr)
    out = {"schema": "R103-dyadic-twist-v1", "fields": [], "models": []}
    for line in run.stdout.splitlines():
        s = line.split("|")
        if s[0] == "VERSION":
            out["pari_version_used"] = json.loads(s[1])
        elif s[0] == "BASE":
            out["base_polynomial"] = s[1]
            out["base_discriminant"] = int(s[2])
            out["base_rnfequation_k"] = int(s[3])
        elif s[0] == "FIELD":
            out["fields"].append({
                "d": int(s[1]), "polynomial": s[2], "discriminant": int(s[3]),
                "e_over_Q2": int(s[4]), "f_over_F2": int(s[5]),
                "rnfequation_k": int(s[6])})
        elif s[0] == "REFERENCE":
            next(f for f in out["fields"] if f["d"] == int(s[1]))[
                "reference_conductor"] = int(s[2])
        elif s[0] == "MODEL":
            out["models"].append({
                "d": int(s[1]), "H": int(s[2]),
                "conductor_exponent": int(s[3]), "pari_kodaira_code": int(s[4]),
                "minimal_discriminant_valuation": int(s[5]),
                "change_u_r_s_t_valuations": json.loads(s[6]),
                "minimal_a1_a2_a3_a4_a6_valuations": json.loads(s[7]),
                "H_plus_8_delta_a4_a6_lower_bounds": json.loads(s[8])})
        elif line.strip():
            raise RuntimeError("Unexpected GP output: " + line)
    assert out["base_discriminant"] == 2**16 * 3**10
    assert out["base_rnfequation_k"] == 0
    assert len(out["fields"]) == 2 and len(out["models"]) == 4
    for f in out["fields"]:
        assert f["discriminant"] == 2**48 * 3**20
        assert (f["e_over_Q2"], f["f_over_F2"], f["reference_conductor"]) == (8,2,0)
    signatures = []
    for m in out["models"]:
        good = (m["d"], m["H"]) in ((1,2), (2,6))
        if good:
            assert (m["conductor_exponent"], m["pari_kodaira_code"],
                    m["minimal_discriminant_valuation"]) == (0,1,0)
            assert m["change_u_r_s_t_valuations"] == [6,4,2,10]
            assert m["H_plus_8_delta_a4_a6_lower_bounds"] == [8,0]
        else:
            assert (m["conductor_exponent"], m["pari_kodaira_code"],
                    m["minimal_discriminant_valuation"]) == (4,-2,12)
            assert m["change_u_r_s_t_valuations"] == [5,4,2,10]
            assert m["H_plus_8_delta_a4_a6_lower_bounds"] == [12,6]
            a = m["minimal_a1_a2_a3_a4_a6_valuations"]
            assert all(a[i] >= i+1 for i in range(4)) and a[4] == 5
        signatures.append([m["d"],m["H"],"good" if good else "II*"])
    assert signatures == [[1,2,"good"],[1,6,"II*"],[2,2,"II*"],[2,6,"good"]]
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gp", default=shutil.which("gp"))
    ap.add_argument("--certificate", type=Path, default=DEFAULT)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if not args.gp:
        ap.error("supply --gp /path/to/gp")
    actual = generate(args.gp)
    if args.write:
        args.certificate.write_text(json.dumps(actual, ensure_ascii=False, indent=2)+"\n")
        print("Wrote", args.certificate)
    else:
        expected = json.loads(args.certificate.read_text())
        expected["pari_version_used"] = actual["pari_version_used"]
        assert expected == actual, "Recomputed certificate differs"
        print("R103: exact fields, torsion points, local models and stability bounds match")
    print("All odd parameters covered by H=2 or 6 mod 8; unique necessary twist remains")


if __name__ == "__main__":
    main()

