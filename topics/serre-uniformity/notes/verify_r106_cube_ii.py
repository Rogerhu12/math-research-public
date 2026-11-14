#!/usr/bin/env python3
"""R106: exact cube-family-II multi-Frey and dyadic certificate.

Only Python's standard library and PARI/GP are needed.  --write regenerates,
--check recomputes and compares.  No GRH/class-group or numerical recognition.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
QS = (11,13,23,37,47,59,61,71,73,83,97)
DEFAULT = Path(__file__).with_name("r106_cube_ii_certificate.json")


def leg(a: int, q: int) -> int:
    z = pow(a % q, (q-1)//2, q)
    return -1 if z == q-1 else z


def tr(q: int, a2: int, a4: int, a6: int = 0) -> int:
    return -sum(leg(x**3+a2*x*x+a4*x+a6,q) for x in range(q))


def finite_fields() -> list[dict]:
    rows = []
    for q in QS:
        assert all(q % n for n in range(2,math.isqrt(q)+1))
        roots = [r for r in range(q) if r*r % q == 3]
        assert len(roots) == 2
        inv2, inv4 = pow(2,-1,q), pow(4,-1,q)
        ta = tr(q,0,-1)
        allowed = []
        for a,b in [(a,1) for a in range(q)] + [(1,0)]:
            G = 27*b**4-18*a*a*b*b-a**4
            T = G*inv4 % q
            if T == 0:
                continue
            X = (T+9*a*a*b*b) % q
            W = a*b*(a**4+27*b**4)*inv4 % q
            assert (X**3-27*W*W-T**3) % q == 0
            te, tem = tr(q,0,-X,-2*W), tr(q,0,-X,2*W)
            assert (te == ta) == (tem == ta)
            if te != ta:
                continue
            h = (a*a-3*b*b)*inv2 % q
            ts = [tr(q,4*a,2*(a*a+r*h)) for r in roots]
            assert ts[0]**2 == ts[1]**2
            allowed.append([a,b,ts[0]])
        S = sorted({t*t for _,_,t in allowed})
        tb1 = tr(q,4,2*(1-roots[0]))
        tc1 = leg(1+roots[0],q)*tb1
        assert [1,1,tb1] in allowed
        rows.append({"q":q, "sqrt3":roots[0], "trace_A":ta,
                     "trace_squares_B":S, "projective_representatives":allowed,
                     "trace_B1":tb1, "trace_C1":tc1})
    return rows


def gp_program(rows: list[dict]) -> str:
    checks = [[r["q"],r["trace_squares_B"]] for r in rows]
    return "default(parisizemax,400000000);\nchecks="+json.dumps(checks)+";\n"+r"""
print("VERSION|",version());
M=mfinit([1536,2,12],0); E=mfeigenbasis(M);
print("SPACE|",mfdim(M),"|",#E);
for(j=1,#E,my(f=E[j],P=mfparams(f)[4],c=mfcoefs(f,97),g=0,ds=vector(#checks));for(i=1,#checks,my(q=checks[i][1],S=checks[i][2],v=q);for(k=1,#S,v*=norm(Mod(lift(c[q+1]^2-S[k]),P)));ds[i]=v;g=gcd(g,v);print("COEF|",j,"|",q,"|",lift(c[q+1])));print("FORM|",j,"|",P,"|",poldegree(P),"|",g,"|",ds));
K=nfinit(z^2-3); r=Mod(z,z^2-3); u=1+r; P2=idealprimedec(K,2)[1];
B1=ellinit([0,4,0,2*(1-r),0],K);print("B1_J|",lift(B1.j));print("B1_J_POLY|",minpoly(B1.j));
for(i=1,4,my(d=[1,-1,2,-2][i],C=ellinit([0,4*d*u,0,2*(1-r)*u^2*d^2,0],K),R=elllocalred(C,P2),Cm=ellchangecurve(C,R[3]));print("C1_LOCAL|",d,"|",R[1],"|",R[2],"|",idealval(K,Cm.disc,P2)));
RH=rnfequation(K,y^4+16*y^3+36*(1-r)*y^2-108*(1-r)^2,1);
if(!polisirreducible(RH[1]),error("base polynomial reducible"));
H=nfinit(RH[1]); rh=RH[2]; zh=Mod(y,RH[1])-RH[3]*rh; xh=zh/3; fh=xh^3+4*xh^2+2*(1-rh)*xh;
print("BASE|",H.pol,"|",H.disc,"|",RH[3]);
for(j=1,2,my(d=[1,2][j],S=rnfequation(H,x^2-81*d*fh,1),L=nfinit(S[1]),yh=S[2],rl=subst(lift(rh),y,yh),zl=subst(lift(zh),y,yh),wl=Mod(x,S[1])-S[3]*yh,Pr=idealprimedec(L,2));if(!polisirreducible(S[1]),error("point polynomial reducible"));if(#Pr!=1,error("prime splitting"));my(P=Pr[1],Bref=ellinit([0,4*d,0,2*(1-rl)*d^2,0],L),Pt=[d*zl/3,d*wl/9]);if(ellmul(Bref,Pt,3)!=[0],error("not three torsion"));print("FIELD|",d,"|",L.pol,"|",L.disc,"|",P.e,"|",P.f,"|",elllocalred(Bref,P)[1]);for(k=1,4,my(h=[-1,3,7,11][k],B=ellinit([0,4,0,2*(1+rl*h),0],L),R=elllocalred(B,P),Bm=ellchangecurve(B,R[3]),V=vector(4,i,if(R[3][i]==0,999,idealval(L,R[3][i],P))),A=vector(5,i,if(Bm[i]==0,999,idealval(L,Bm[i],P))));print("MODEL|",d,"|",h,"|",R[1],"|",R[2],"|",idealval(L,Bm.disc,P),"|",V,"|",A,"|",[80-4*V[1],80+V[2]-6*V[1]])));
quit
"""


def exact_gp(gp: str, rows: list[dict]) -> dict:
    run = subprocess.run([gp,"-fq"], input=gp_program(rows), text=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    errors = [x for x in run.stderr.splitlines() if "***" in x and "Warning:" not in x]
    if run.returncode or errors:
        raise RuntimeError(run.stdout+run.stderr)
    out = {"forms":[], "C1_at_P2":[], "point_fields":[], "local_models":[]}
    cs = {}
    for line in run.stdout.splitlines():
        a = line.split("|")
        if a[0] == "VERSION":
            out["pari_version_used"] = json.loads(a[1])
        elif a[0] == "SPACE":
            out["dimension"],out["orbit_count"] = map(int,a[1:])
        elif a[0] == "COEF":
            cs.setdefault(int(a[1]),{})[a[2]] = a[3]
        elif a[0] == "FORM":
            j=int(a[1])
            out["forms"].append({"index":j,"coefficient_polynomial":a[2],
                                 "degree":int(a[3]),"gcd_Dq":int(a[4]),
                                 "Dq_in_prime_order":json.loads(a[5]),
                                 "coefficients":cs[j]})
        elif a[0] in ("B1_J","B1_J_POLY"):
            out[a[0].lower()]=a[1]
        elif a[0] == "C1_LOCAL":
            out["C1_at_P2"].append(list(map(int,a[1:])))
        elif a[0] == "BASE":
            out["x_coordinate_field"]={"polynomial":a[1],"discriminant":int(a[2]),
                                        "rnfequation_k":int(a[3])}
        elif a[0] == "FIELD":
            out["point_fields"].append({"d":int(a[1]),"polynomial":a[2],
                                         "discriminant":int(a[3]),"e_over_Q2":int(a[4]),
                                         "f_over_F2":int(a[5]),"reference_conductor":int(a[6])})
        elif a[0] == "MODEL":
            out["local_models"].append({"d":int(a[1]),"H":int(a[2]),
                "conductor_exponent":int(a[3]),"pari_kodaira_code":int(a[4]),
                "minimal_discriminant_valuation":int(a[5]),
                "change_u_r_s_t_valuations":json.loads(a[6]),
                "minimal_a1_a2_a3_a4_a6_valuations":json.loads(a[7]),
                "H_plus_16_delta_a4_a6_lower_bounds":json.loads(a[8])})
        elif line.strip():
            raise RuntimeError("Unexpected GP output: "+line)
    assert (out["dimension"],out["orbit_count"]) == (64,13)
    assert [f["degree"] for f in out["forms"]] == [2,2,2,2,4,4,4,4,4,4,8,8,16]
    assert [f["gcd_Dq"] for f in out["forms"]] == [
        0,0,0,0,2**12,2**12,2**20*3**4,2**20*3**4,
        2**12*3**4,2**12*3**4,2**48,2**24,2**80]
    assert out["C1_at_P2"] == [[1,14,3,15],[-1,14,3,15],[2,14,3,15],[-2,14,3,15]]
    assert out["x_coordinate_field"]["discriminant"] == 2**22*3**10
    for f in out["point_fields"]:
        assert (f["discriminant"],f["e_over_Q2"],f["f_over_F2"],f["reference_conductor"]) == (2**58*3**20,16,1,0)
    assert len(out["local_models"]) == 8
    for m in out["local_models"]:
        good=m["H"]%8 == 7
        assert (m["conductor_exponent"],m["pari_kodaira_code"],
                m["minimal_discriminant_valuation"]) == ((0,1,0) if good else (12,2,12))
        assert m["change_u_r_s_t_valuations"] == ([14,12,6,26] if good else [13,12,6,26])
        assert m["H_plus_16_delta_a4_a6_lower_bounds"] == ([24,8] if good else [28,14])
        if not good:
            assert m["minimal_a1_a2_a3_a4_a6_valuations"][4] == 1
    twists=[]
    for d in (1,-1,2,-2):
        target={str(q):str(leg(d,q)*next(r["trace_C1"] for r in rows if r["q"]==q)) for q in (11,13)}
        hits=[f["index"] for f in out["forms"] if all(f["coefficients"][q]==t for q,t in target.items())]
        assert len(hits)==1
        twists.append({"d":d,"orbit_index":hits[0]})
    assert twists == [{"d":1,"orbit_index":4},{"d":-1,"orbit_index":1},
                      {"d":2,"orbit_index":3},{"d":-2,"orbit_index":2}]
    out["twist_identification"]=twists
    return out


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gp",default=shutil.which("gp"))
    ap.add_argument("--certificate",type=Path,default=DEFAULT)
    modes=ap.add_mutually_exclusive_group()
    modes.add_argument("--write",action="store_true")
    modes.add_argument("--check",action="store_true")
    ap.add_argument("--finite-only",action="store_true")
    args=ap.parse_args()
    rows=finite_fields()
    if args.finite_only:
        print(json.dumps(rows,indent=2));return
    if not args.gp:
        ap.error("supply --gp /path/to/gp")
    result={"schema":"R106-cube-II-v1","level":1536,"weight":2,
            "nebentypus_Kronecker_discriminant":12,
            "definition_Dq":"q * product_s Norm(a_q(f)^2-s)",
            "finite_fields":rows,"exact_pari":exact_gp(args.gp,rows)}
    if args.write:
        args.certificate.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
        print("Wrote",args.certificate)
    else:
        saved=json.loads(args.certificate.read_text())
        saved["exact_pari"]["pari_version_used"]=result["exact_pari"]["pari_version_used"]
        assert saved==result,"Recomputed certificate differs"
        print("R106: all finite-field, newform, reference and complete dyadic data match")
    print("13 orbits; 9 excluded for p>37; four B1 twists remain; Y=1 mod 8 is necessary")


if __name__=="__main__":
    main()

