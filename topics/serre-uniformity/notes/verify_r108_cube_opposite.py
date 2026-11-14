#!/usr/bin/env python3
"""R108 exact verification; depends on the two committed R99/R106 finite-field generators."""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
HERE=Path(__file__).resolve().parent
DEFAULT=HERE/"r108_cube_opposite_parity_certificate.json"


def module(name: str, filename: str):
    spec=importlib.util.spec_from_file_location(name,HERE/filename)
    out=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


def finite_data() -> dict:
    F=module("r99_finite","verify_r99_d3_multifrey.py").finite_field_data()
    G=module("r106_finite","verify_r106_cube_ii.py").finite_fields()
    # The proof supplies the literal equality (F) and scaling by 2 (G)
    # between these original Frey models and the current two branches.
    return {"F":F,"G":G}


def gp_program(data: dict) -> str:
    checks=[[[r["q"],r["trace_squares_B"]] for r in data[s]] for s in ("F","G")]
    return "default(parisizemax,400000000);\nchecks="+json.dumps(checks)+";\n"+r"""
print("VERSION|",version());
M=mfinit([768,2,12],0); E=mfeigenbasis(M);print("SPACE|",mfdim(M),"|",#E);
for(j=1,#E,my(f=E[j],P=mfparams(f)[4],c=mfcoefs(f,97));print("FORM|",j,"|",P,"|",poldegree(P),"|",lift(c[12]),"|",lift(c[14]));for(sg=1,2,my(g=0,ds=vector(#checks[sg]));for(i=1,#checks[sg],my(q=checks[sg][i][1],S=checks[sg][i][2],v=q);for(k=1,#S,v*=norm(Mod(lift(c[q+1]^2-S[k]),P)));ds[i]=v;g=gcd(g,v));print("SIEVE|",sg,"|",j,"|",g,"|",ds)));
K=nfinit(z^2-3);r=Mod(z,z^2-3);
RH=rnfequation(K,y^4+16*y^3+18*(2+r)*y^2-27*(2+r)^2,1);
H=nfinit(RH[1]);rh=RH[2];zh=Mod(y,RH[1])-RH[3]*rh;xh=zh/3;fh=xh^3+4*xh^2+(2+rh)*xh;
for(j=1,2,my(d=[1,2][j],S=rnfequation(H,x^2-81*d*fh,1),L=nfinit(S[1]),yh=S[2],rl=subst(lift(rh),y,yh),Pr=idealprimedec(L,2));if(#Pr!=1,error("unexpected prime splitting"));my(P=Pr[1],Bref=ellinit([0,4*d,0,(2+rl)*d^2,0],L));print("FIELD|",d,"|",L.pol,"|",L.disc,"|",P.e,"|",P.f,"|",elllocalred(Bref,P)[1]);for(sg=1,2,for(k=1,4,my(ab=[[1,0],[1,2],[0,1],[2,1]][k],a=ab[1],b=ab[2],sign=[1,-1][sg],h=(a^2+sign*3*b^2)/2,B=ellinit([0,4*a,0,2*(a^2+rl*h),0],L),R=elllocalred(B,P),Bm=ellchangecurve(B,R[3]),V=vector(4,i,if(R[3][i]==0,999,idealval(L,R[3][i],P))),A=vector(5,i,if(Bm[i]==0,999,idealval(L,Bm[i],P))));print("MODEL|",d,"|",sign,"|",a,"|",b,"|",R[1],"|",R[2],"|",idealval(L,Bm.disc,P),"|",V,"|",A,"|",[if(a%2==1,999,32-2*V[1]),32-4*V[1],32+V[2]-6*V[1]]))));
quit
"""


def generate(gp: str) -> dict:
    data=finite_data()
    run=subprocess.run([gp,"-fq"],input=gp_program(data),text=True,
                       stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    errors=[s for s in run.stderr.splitlines() if "***" in s and "Warning:" not in s]
    if run.returncode or errors:
        raise RuntimeError(run.stdout+run.stderr)
    result={"schema":"R108-opposite-parity-v1","level":768,
            "finite_fields":data,"forms":[],"sieves":{"F":[],"G":[]},
            "point_fields":[],"local_models":[]}
    for line in run.stdout.splitlines():
        a=line.split("|")
        if a[0]=="VERSION":
            result["pari_version_used"]=json.loads(a[1])
        elif a[0]=="SPACE":
            result["dimension"],result["orbit_count"]=map(int,a[1:])
        elif a[0]=="FORM":
            result["forms"].append({"index":int(a[1]),"coefficient_polynomial":a[2],
                                    "degree":int(a[3]),"a11":a[4],"a13":a[5]})
        elif a[0]=="SIEVE":
            sg=("F","G")[int(a[1])-1]
            result["sieves"][sg].append({"index":int(a[2]),"gcd_Dq":int(a[3]),
                                         "Dq_in_prime_order":json.loads(a[4])})
        elif a[0]=="FIELD":
            result["point_fields"].append({"d":int(a[1]),"polynomial":a[2],
                "discriminant":int(a[3]),"e_over_Q2":int(a[4]),
                "f_over_F2":int(a[5]),"reference_conductor":int(a[6])})
        elif a[0]=="MODEL":
            result["local_models"].append({"d":int(a[1]),"sign":int(a[2]),
                "a":int(a[3]),"b":int(a[4]),"conductor_exponent":int(a[5]),
                "pari_kodaira_code":int(a[6]),"minimal_discriminant_valuation":int(a[7]),
                "change_u_r_s_t_valuations":json.loads(a[8]),
                "minimal_a1_a2_a3_a4_a6_valuations":json.loads(a[9]),
                "parameter_plus_4_delta_a2_a4_a6_lower_bounds":json.loads(a[10])})
        elif line.strip():
            raise RuntimeError("Unexpected GP output: "+line)
    assert (result["dimension"],result["orbit_count"])==(28,10)
    expected=[2**12,0,0,2**12,0,0,2**24,2**24,2**24,2**28]
    for sg in ("F","G"):
        assert [s["gcd_Dq"] for s in result["sieves"][sg]]==expected
    for f in result["point_fields"]:
        assert (f["discriminant"],f["e_over_Q2"],f["f_over_F2"],f["reference_conductor"])==(2**48*3**20,8,2,0)
    assert len(result["local_models"])==16
    for m in result["local_models"]:
        odd=m["a"]%2==1
        good=odd and ((m["d"]==1 and m["b"]==0) or (m["d"]==2 and m["b"]==2))
        typ=(0,1,0) if good else ((4,-2,12) if odd else (8,-1,12))
        assert (m["conductor_exponent"],m["pari_kodaira_code"],
                m["minimal_discriminant_valuation"])==typ
        assert m["change_u_r_s_t_valuations"]==([4,0,0,4] if good else [3,0,0,4])
        changes=([999,16,8] if good else ([999,20,14] if odd else [26,20,14]))
        assert m["parameter_plus_4_delta_a2_a4_a6_lower_bounds"]==changes
        vals=m["minimal_a1_a2_a3_a4_a6_valuations"]
        if not good and odd:
            assert all(vals[i]>=i+1 for i in range(4)) and vals[4]==5
        if not odd:
            assert vals[0]>=1 and vals[1]>=2 and vals[2]>=2
            assert vals[3]==2 and vals[4]==3
    return result


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gp",default=shutil.which("gp"))
    ap.add_argument("--certificate",type=Path,default=DEFAULT)
    modes=ap.add_mutually_exclusive_group()
    modes.add_argument("--write",action="store_true")
    modes.add_argument("--check",action="store_true")
    args=ap.parse_args()
    if not args.gp:
        ap.error("supply --gp /path/to/gp")
    result=generate(args.gp)
    if args.write:
        args.certificate.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
        print("Wrote",args.certificate)
    else:
        saved=json.loads(args.certificate.read_text())
        saved["pari_version_used"]=result["pari_version_used"]
        assert saved==result,"Recomputed certificate differs"
        print("R108: both complete sieves and all 16 local models match")
    print("a even is excluded; I has Y=1 mod8; III odd-X has Y=-1 mod8; unique d fixed")


if __name__=="__main__":
    main()

