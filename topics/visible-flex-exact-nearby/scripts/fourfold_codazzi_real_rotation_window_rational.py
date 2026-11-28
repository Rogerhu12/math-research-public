"""Read the whole R31 outcome and check the new ASQ24 low-norm and parameter margins exactly."""
import argparse
import gzip
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import re

NATIVE="d6e59dfa851fb7d385f6281389221408cc132f90be8c2b1577fdd2be9a348d61"
FILES={
 "results/R133-supplement-actual-physical-Wiener-conjugacy-strip.md":"1e8d001a5878da2894b4c9ab88baf00555ca8364b23f49df8c827c23a7da88c3",
 "results/R144-supplement-full-off-constraint-principal-return-Hessian.md":"e77c6e41b3ff7f40085d4a65821e6858795412e9aa5e743188a74a3da9684e21",
 "results/R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md":"b1751a475c30ec9ca823681598b60326befc85909d462a5ff7b18acaad237c23",
 "scripts/fourfold_codazzi_phase_explicit_family_R31.py":"df58ef8806461a03870e413e6a8d564947c3cd20a6074127a14a8d4bae5d0163",
 "notes/phase_small_consumers_ci/run-43586895661-1/consumers/process.json":"3319762cb2bb007f616f712c1a3f257e6aba18382e2abd321a770cd6abe53072",
 "results/R31-actual-parameter-circle-normalization.md":"e564eec1fce55ea2c341d5af9be8f5a8bede2f057062667823ad0a7a9b992f09"}

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def run(topic,native):
    raw=native.read_bytes()
    assert len(raw)==3560 and sha(raw)==NATIVE
    old=json.loads(gzip.decompress(raw))
    for name,expected in FILES.items():
        assert sha((topic/name).read_bytes())==expected
    process=json.loads((topic/next(k for k in FILES if k.endswith("process.json"))).read_bytes())
    steps=[r for r in process["steps"] if r["name"]=="R31"]
    assert str(process["run_id"])=="43586895661" and str(process["run_attempt"])=="1" and process["complete"]
    assert len(steps)==1 and steps[0]["exit_code"]==0 and steps[0]["native_sha256"]==NATIVE
    assert old["complete"] and old["source_sha256"]==steps[0]["mathematical_source_sha256"]==FILES["scripts/fourfold_codazzi_phase_explicit_family_R31.py"]
    assert old["gates"] and all(x["passed"] for x in old["gates"])
    assert old["exact_family"]=="F_delta(x)=4G(P_delta(G^{-1}(x/4))); Q_delta=Qbar+delta Z, nu_delta=nu0+delta"
    assert old["actual_affine_parameter"]=="eta_0" and old["exact_parameter_radius"]=="1/100000000" and old["sigma0"]=="1/20" and old["circle_K"]=="17/4"
    checks=[]
    def lt(label,x,y):
        assert x<y,(label,x,y)
        checks.append(label)
    for name,upper in {"normalized_uniform_P":"2.208","normalized_uniform_Q":"2.432","normalized_uniform_T":"55.92",
       "complete_return_second_angular":".629","complete_return_first_parameter":".541",
       "complete_return_mixed_parameter":"2.267","exact_parameter_change_bound":"9.369e-11"}.items():
        val=old[name]["upper"]
        match=re.fullmatch(r"\[([-.+\deE]+) \+/- ([-.+\deE]+)\]",val)
        assert match is not None
        v,r=map(F,match.groups())
        lt(name,v+abs(r),F(upper))
    d,H,H1,k =map(F,("9.369e-11","8.85e-7",".000222","6e-12"))
    P,Q,T,K=map(F,("2.208","2.432","55.92","17/4"))
    e=F("2.71") # e>1+1+1/2+1/6+1/24+1/120>2.71
    lt("physical metric radius",d+k,F("1e-10"))
    lt("Wiener composition",F(".04")+H,F(".063"))
    lt("true normalized B",P/(1-H1),F("2.21"))
    lt("positive true pivot difference",T*d+Q*H+P*H1/(1-H1),F(".001"))
    h2=H1/(e*F(".0465"))
    lt("B derivative",Q*(1+H1)/(1-H1)+P*h2/(1-H1)**2,F("2.45"))
    lt("primitive u",K*F("2.45"),11)
    lt("primitive u derivative",K*(2/(e*F(".04")))**2*F("2.21"),3300)
    lt("real H second derivative",F(".016385")*128/e,F(".8"))
    lt("whole flow ordinary gain",F("1.08")*F("1.220"),F("1.318"))
    lt("logJ strong piece",2*F(".239")*2*6*(14+1),132)
    lt("logJ ordinary piece",F(".629")*F("1.318"),2)
    lt("J difference strong",F("1.08")*132,143)
    lt("J difference ordinary",F("1.08")*2,3)
    lt("folded source derivative",2*F(".49")*(2*6*19+4*15+47),430)
    lt("parameter flow strong",F("1.08")*F(".541")*132,78)
    lt("parameter flow ordinary",F("1.08")*(2*F(".541")+430+F("2.267")*F("1.318")),470)
    lt("true f value",4*F("1.017")*F("1.318"),F("5.37"))
    lt("true f prime strong",F("1.017")*143/F(".983"),155)
    lt("true f prime ordinary",(F("1.017")*3+F(".8")*F("1.318")*F("1.08"))/F(".983"),6)
    lt("true f k strong",4*F("1.017")*78,318)
    lt("true f k ordinary",4*(F("1.017")*470+F(".8")*F("1.318")*F(".541")),1920)
    lt("normalized h inverse second",h2/(1-H1)**3,F(".002"))
    lt("f zero mixed",(F(".002")*2*P+Q/(1-H1))*(1+H1),3)
    lt("f zero second",F(".002")*P**2+T/(1-H1),57)
    lip=1/(1-3300*k)
    lt("moving f value coefficient",(22+F("2.21"))*lip,25)
    lt("moving f input comparison",F("5.37")*lip,F("5.38"))
    xi,E=F("1e-7"),F("1e-12")
    difference=318*xi+1920*E+57*k+33*k+(155*xi+6*E+3*k)*11+3300*(25*k+F("5.4")*E)
    lt("uniform moving parameter lower",F(".048")*(1+3300*k),F(".049")-difference)
    lt("fixed branch barriers",F("5.38"),F(".048")*114)
    lt("fixed branch full metric room",114*F("5e-14"),k)
    lt("regular branch positive rate",F(".021"),F(".048")-F("5.38")*F(".005"))
    lt("regular branch barriers",F("5.38"),F(".021")*260)
    lt("regular branch full metric room",260*F("2e-14"),k)
    lt("all slope interpolation inputs",F("2e-14")+F(".005")*k,F("1e-12"))
    return dict(kind="ASQ24_whole_R31_and_Sobolev_rotation_margins_v1",historical_run="43586895661/1",
                whole_input_count=1+len(FILES),whole_R31_sha256=NATIVE,passed=checks,complete=True,
                old_scientific_targets_recomputed=0)

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--topic",type=Path,required=True)
    p.add_argument("--whole-R31",dest="native",type=Path,required=True)
    args=p.parse_args()
    print(json.dumps(run(args.topic,args.native),sort_keys=True,separators=(",",":")))
