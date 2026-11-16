#!/usr/bin/env python3
"""R883: original t=a^3 first-order frame from retained original three-jets.
All new arithmetic is restricted to this public repository's GitHub Actions.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

RESULT="R883-original-t-first-order-frame"
FINAL="p41-original-t-first-order-frame-certificate.json"
PRIME=1000000753
ZETA=549966761
SROOT=99932770
LEVEL=82
ORDERS=3
EPS=[0]+[1]*144+[2]*127
IDENTITY_KEYS=("node_key","ordinary_power","original_recipe","factor_nodes",
               "integer_scale","original_reference_index")
SOURCE_KEYS=("result","run_id","source_commit","core_sha256","manifest_sha256")

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(4*1024*1024),b""):
            h.update(block)
    return h.hexdigest()

def spec(path):
    p=Path(path)
    return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p)}

def plain(v):
    return {k:v[k] for k in ("file","bytes","sha256")}

def read(path):
    p=Path(path)
    with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open(encoding="utf-8")) as f:
        return json.load(f)

def save(path,value):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    q=p.with_name(p.name+".tmp")
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False)+"\n").encode()
    q.write_bytes(gzip.compress(raw,mtime=0) if p.suffix==".gz" else raw)
    q.replace(p)

def check(path,value):
    assert spec(path)==plain(value),str(path)
    return Path(path)

def source_identity(value):
    return {k:str(value[k]) for k in SOURCE_KEYS}

def mul(a,b):
    assert len(a)==len(b)==ORDERS
    return [sum(a[i]*b[n-i] for i in range(n+1))%PRIME for n in range(ORDERS)]

class CriterionFailure(RuntimeError):
    pass

class BudgetStop(RuntimeError):
    pass

class Job:
    def __init__(self,args):
        self.args=args;self.item=read(args.config);self.out=args.out
        self.out.mkdir(parents=True,exist_ok=True)
        assert os.environ.get("GITHUB_ACTIONS")=="true"
        assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
        assert sha(__file__)==self.item["core_sha256"]
        self.started=time.monotonic();self.deadline=self.started+60*args.budget_minutes
        self.tag=self.item["actual_configuration"]
        assert self.tag["result"]==RESULT and self.tag["source_sha256"]==sha(__file__)
        assert self.tag["prime"]==PRIME and self.tag["orders"]==ORDERS
        self.sources=self.item["prepared_sources"]
        self.stage_refs={}
        self.source_cache={}

    def budget(self):
        if time.monotonic()>self.deadline:
            raise BudgetStop("original first-order consumer budget")

    def path(self,name):
        assert name.startswith("R883-") and Path(name).name==name
        return self.out/(name+".json.gz")

    def stage(self,name,produce):
        p=self.path(name)
        if p.exists():
            data=read(p)
            assert data["result"]==RESULT and data["configuration"]==self.tag and data["complete"] is True
        else:
            self.budget()
            data=dict(produce(),result=RESULT,configuration=self.tag,complete=True)
            save(p,data)
        self.stage_refs[name]=spec(p)
        return data

    def source(self,label,name):
        key=(label,name)
        if key in self.source_cache:
            return self.source_cache[key]
        src=self.sources[label]
        p=check(Path(src["directory"])/name,src["files"][name])
        d=read(p)
        assert d["complete"] is True
        if "result" in d:
            assert d["result"]==src["identity"]["result"]
        cfg=d["configuration"]
        assert cfg["result"]==src["identity"]["result"] and cfg["source_sha256"]==src["identity"]["core_sha256"]
        assert fingerprint(cfg)==src["configuration_sha256"]
        self.source_cache[key]=d
        return d

    def ref(self,label,name):
        return {"source_group":label,**plain(self.sources[label]["files"][name])}

    def audit(self):
        def produce():
            theta=self.source("R807","R807-original-nonzero-pole-clearing-theta.json.gz")
            ix=self.source("R807","R807-original-four-M6-pole-clearing-coordinate-index.json.gz")
            n692=self.source("R807","R807-exact-V4-M6-index-692-from-kernel.json.gz")
            n693=self.source("R807","R807-exact-V4-M6-index-693.json.gz")
            plan=self.source("R801","R801-original-recipe-dependency-plan.json.gz")
            audit=self.source("R872","R872-source-audit.json.gz")
            linear=self.source("R872","R872-point-linearization.json.gz")
            jets=self.source("R872","R872-V2-original-point-jet-matrix.json.gz")
            for label in ("R775","R786"):
                assert source_identity(theta["configuration"]["retained_artifacts"][label])==source_identity(plan["configuration"]["retained_artifacts"][label])
            assert source_identity(theta["configuration"]["retained_artifacts"]["R805"])==source_identity(jets["configuration"]["sources"]["R805"])
            assert theta["theta_nonzero_by_original_independent_M2_input"] is True
            assert theta["theta_at_P0_and_P1_has_two_zeros_by_original_E6_principal_parts"] is True
            assert theta["original_M2_integer_scale"]==str(LEVEL**2)
            assert ix["all_four_members_verified_in_all1100_real_coordinates"] is True
            assert ix["ordinary_V4_integer_scale"]==str(LEVEL**8)
            assert ix["original_M6_integer_scale"]==str(LEVEL**6)
            assert ix["original_theta_M2_integer_scale"]==str(LEVEL**2)
            assert ix["four_original_M6_recipes"]["692"]=={"kind":"level_one","name":"E6"}
            assert ix["four_original_M6_recipes"]["693"]=={"kind":"level_one","name":"eta12"}
            for i,d in ((692,n692),(693,n693)):
                assert d["basis_dimension"]==962 and d["basis_integer_scale"]==str(LEVEL**8)
                assert d["all1100_rows_verified"] is True
                assert len(d["solution_numerators"])==962 and int(d["solution_common_denominator"])>0
                assert plain(ix["coordinate_stages"][str(i)])==plain(self.ref("R807",
                    "R807-exact-V4-M6-index-692-from-kernel.json.gz" if i==692 else "R807-exact-V4-M6-index-693.json.gz"))
                assert d["original_V4_basis_index"]==ix["original_V4_basis_index"]
            assert n692["M6_index"]==692 and n692["source_M6_recipe"]=={"kind":"level_one","name":"E6"}
            assert n692["exact_global_V4_membership_certified"] is True
            assert n693["label"]=="M6-index-693" and n693["mode"]=="member"
            assert n693["individual_V4_membership_claimed"] is True
            assert plain(theta["M6_index692_cleared_coordinate_stage"])==plain(self.ref("R807","R807-exact-V4-M6-index-692-from-kernel.json.gz"))
            assert plan["old_rows_or_basis_selection_recomputed"] is False
            assert plan["configuration"]["level"]==LEVEL
            assert audit["all_original_W_polynomial_coefficients_are_integral_at_this_place"] is True
            assert audit["all_original_scales_preserved"] is True
            assert audit["exact_local_source"]["formal_branch_is_original_P0_by_normalization_and_Hensel_uniqueness"] is True
            for value in (audit,linear,jets):
                assert value["prime"]==PRIME
            assert linear["original_zeta_root"]==audit["original_zeta_root"]==ZETA
            assert linear["chosen_local_parameter"]==audit["chosen_local_parameter"]=="z_minus_z0"
            assert linear["chosen_parameter_derivative_is_a_unit"] is True
            assert jets["matrix_shape"]==[273,418] and jets["row_orders"]==list(range(273))
            assert jets["normal_basis_degrees"]==EPS and jets["normal_integer_scale_applied_again"] is False
            assert len(jets["matrix_mod_prime"])==273 and all(len(r)==418 for r in jets["matrix_mod_prime"])
            expected=[{"normal_basis_row":i,"power_of_z":j} for i in range(272) for j in range(3-EPS[i])]
            assert jets["V2_basis"]==expected
            assert jets["exact_matrix_definition"]["source_point_jets"]==jets["source_point_jets"]
            assert (2*ZETA+1)%PRIME==SROOT and (SROOT*SROOT+3)%PRIME==0
            return {
                "source_identities":{k:v["identity"] for k,v in self.sources.items()},
                "actual_selected_file_counts":{k:len(v["files"]) for k,v in self.sources.items()},
                "original_R775_R786_and_R805_identities_match":True,
                "original_V4_order":"R786 original power4 indices0..961; R801 o04-iXXXX",
                "original_82_scales_applied_again":False,
                "original_M6_indices":[692,693],"original_t":"a^3=1/2+E6/(48*s*eta^12)",
                "source_theorem":"R872 equations872.34-872.35, original R802 marked P0",
                "exact_local_source":audit["exact_local_source"],
                "source_point_jets":jets["source_point_jets"],
                "chosen_local_parameter":"rho=z-z0",
                "original_zeta_root":ZETA,"original_s_root":SROOT,"prime":PRIME,
                "old_Hensel_jets_inverse_basis_or_q_coefficients_recomputed":False}
        return self.stage("R883-original-source-audit",produce)

    def leaves(self):
        def produce():
            jets=self.source("R872","R872-V2-original-point-jet-matrix.json.gz")
            linear=self.source("R872","R872-point-linearization.json.gz")
            positions={(row["normal_basis_row"],row["power_of_z"]):i for i,row in enumerate(jets["V2_basis"])}
            beta=[[int(jets["matrix_mod_prime"][r][positions[(i,0)]])%PRIME for r in range(ORDERS)] for i in range(272)]
            z=[int(jets["matrix_mod_prime"][r][positions[(0,1)]])%PRIME for r in range(ORDERS)]
            assert beta[0]==[1,0,0]
            assert z==[linear["z0_mod_prime"],1,0]
            assert beta[1][0]==linear["w0_mod_prime"]
            leaves=[beta[0],[(z[r]-beta[72][r])%PRIME for r in range(ORDERS)]]
            leaves.extend(beta[i-1] for i in range(2,146))
            assert len(leaves)==146
            return {"source_V2_jets":self.ref("R872","R872-V2-original-point-jet-matrix.json.gz"),
                "source_point_linearization":self.ref("R872","R872-point-linearization.json.gz"),
                "orders":[0,1,2],"leaf_jets_mod_prime":leaves,
                "exact_leaf_definition":{"0":"1","1":"z-beta72","2_through145":"beta_(i-1)"},
                "beta_source_columns":[positions[(i,0)] for i in range(272)],
                "z_source_column":positions[(0,1)],
                "only_existing_three_coefficients_copied":True,"new_Hensel_jets_computed":False}
        return self.stage("R883-original-M2-three-jet-leaves",produce)

    def recipes(self):
        def produce():
            plan=self.source("R801","R801-original-recipe-dependency-plan.json.gz")
            nodes={d["node_key"]:d for d in plan["nodes"]}
            assert len(nodes)==len(plan["nodes"])
            memo={};visiting=set()
            def leaves(key):
                if key in memo:
                    return memo[key]
                assert key not in visiting
                visiting.add(key);d=nodes[key]
                assert fingerprint({k:d[k] for k in IDENTITY_KEYS})==d["node_fingerprint"]
                power=d["ordinary_power"]
                assert d["integer_scale"]==str(LEVEL**(2*power))
                if power==1:
                    i=d["original_reference_index"]
                    assert not d["factor_nodes"] and 0<=i<146
                    assert key=="o01-i"+str(i).zfill(4)
                    result=[i]
                else:
                    assert len(d["factor_nodes"])==2
                    result=sorted(leaves(d["factor_nodes"][0])+leaves(d["factor_nodes"][1]))
                    assert len(result)==power
                visiting.remove(key);memo[key]=result
                return result
            rows=[]
            for i in range(962):
                key="o04-i"+str(i).zfill(4);d=nodes[key]
                assert d["ordinary_power"]==4 and d["original_reference_index"]==i
                old=d["original_input_segments"][0]
                assert old["producer"]=="R786" and old["file"]=="R786-exact-power-4-row-"+str(i).zfill(4)+".json.gz"
                assert old["first"]==0
                rows.append({"original_V4_index":i,"source_node_key":key,
                    "node_fingerprint":d["node_fingerprint"],"original_M2_leaf_indices":leaves(key),
                    "original_R786_source":old})
            return {"source_recipe_plan":self.ref("R801","R801-original-recipe-dependency-plan.json.gz"),
                "original_V4_monomials":rows,"dimension":962,
                "all_original_recipe_identities_verified":True,
                "basis_order_reselected":False,"old_q_tails_recomputed":False}
        return self.stage("R883-original-V4-recipe-bridge",produce)

    def evaluate(self):
        def produce():
            leaf=self.leaves()["leaf_jets_mod_prime"]
            recipes=self.recipes()["original_V4_monomials"]
            monomials=[]
            for row in recipes:
                value=[1,0,0]
                for i in row["original_M2_leaf_indices"]:
                    value=mul(value,leaf[i])
                monomials.append(value)
            results={};units={}
            for i,name in ((692,"R807-exact-V4-M6-index-692-from-kernel.json.gz"),
                           (693,"R807-exact-V4-M6-index-693.json.gz")):
                d=self.source("R807",name)
                den=int(d["solution_common_denominator"])%PRIME
                if not den:
                    self.fail("original_R807_denominator_nonunit",{"M6_index":i,"source":self.ref("R807",name)})
                inv=pow(den,-1,PRIME);assert den*inv%PRIME==1
                nums=[int(v)%PRIME for v in d["solution_numerators"]]
                result=[sum(nums[j]*monomials[j][r] for j in range(962))*inv%PRIME for r in range(ORDERS)]
                results[str(i)]=result;units[str(i)]={"denominator_mod_prime":den,"inverse_mod_prime":inv}
            theta=self.source("R807","R807-original-nonzero-pole-clearing-theta.json.gz")
            coeffs=theta["theta_in_original_integer_scaled_M2_basis"]
            assert len(coeffs)==146
            theta_jet=[0]*ORDERS;theta_units=[]
            for i,(a,b) in enumerate(coeffs):
                den=int(b)%PRIME
                if not den:
                    self.fail("original_theta_denominator_nonunit",{"index":i,"source":self.ref("R807","R807-original-nonzero-pole-clearing-theta.json.gz")})
                inv=pow(den,-1,PRIME)
                assert den*inv%PRIME==1
                scale=int(a)%PRIME*inv%PRIME
                theta_units.append({"index":i,"denominator_mod_prime":den,"inverse_mod_prime":inv})
                for r in range(ORDERS):
                    theta_jet[r]=(theta_jet[r]+scale*leaf[i][r])%PRIME
            assert theta_jet[0]==theta_jet[1]==0
            if not theta_jet[2]:
                self.fail("theta_order_two_unit_criterion_failed",{"theta_three_jet_mod_prime":theta_jet})
            return {"M6_cleared_three_jets_mod_prime":results,"theta_three_jet_mod_prime":theta_jet,
                "all_R807_coordinate_denominators_units":True,"coordinate_denominator_units":units,
                "theta_denominator_units":theta_units,
                "theta_exact_order_at_least_two_source":"R807 original principal-parts proof",
                "theta_exact_order_two_certified":True,
                "source_leaf_jets":self.stage_refs["R883-original-M2-three-jet-leaves"],
                "source_V4_recipes":self.stage_refs["R883-original-V4-recipe-bridge"],
                "source_coordinates":{str(i):self.ref("R807",name) for i,name in (
                    (692,"R807-exact-V4-M6-index-692-from-kernel.json.gz"),
                    (693,"R807-exact-V4-M6-index-693.json.gz"))},
                "source_theta":self.ref("R807","R807-original-nonzero-pole-clearing-theta.json.gz"),
                "common_theta_and_82_scales_cancelled_exactly":True,
                "new_local_V4_coefficients_per_section":ORDERS,
                "characteristic_zero_coefficients_expanded":False}
        return self.stage("R883-original-cleared-section-three-jets",produce)

    def fail(self,kind,data):
        self.stage("R883-criterion-failure-"+kind,lambda:dict(data,criterion=kind,
            exact_characteristic_zero_statement_disproved=False,
            modular_zeros_used_as_exact_vanishing=False))
        raise CriterionFailure(kind)

    def frame(self):
        def produce():
            e=self.evaluate()
            a=e["M6_cleared_three_jets_mod_prime"]["692"]
            b=e["M6_cleared_three_jets_mod_prime"]["693"]
            if not b[0]:
                self.fail("cleared_eta12_constant_nonunit",{
                    "N692_three_jet_mod_prime":a,"N693_three_jet_mod_prime":b,
                    "no_unproved_modular_initial_factor_cancelled":True})
            invb=pow(b[0],-1,PRIME);assert b[0]*invb%PRIME==1
            factor=48*SROOT%PRIME;invf=pow(factor,-1,PRIME)
            assert factor*invf%PRIME==1
            ratio=[a[0]*invb%PRIME]
            for r in range(1,ORDERS):
                ratio.append((a[r]-sum(b[j]*ratio[r-j] for j in range(1,r+1)))*invb%PRIME)
            assert mul(b,ratio)==a
            t=[(pow(2,-1,PRIME)+ratio[0]*invf)%PRIME,ratio[1]*invf%PRIME,ratio[2]*invf%PRIME]
            assert t[0]==0
            if not t[1]:
                self.fail("original_t_first_order_nonunit",{"original_t_first_three_coefficients_mod_prime":t})
            c=t[1]
            assert c==(a[1]*b[0]-a[0]*b[1])*invf*invb*invb%PRIME
            return {"source_evaluation":self.stage_refs["R883-original-cleared-section-three-jets"],
                "original_t_identity":"t=a^3=1/2+N692/(48*s*N693)",
                "common_exact_factors_cancelled":["same original theta","same original82^6 M6 scale"],
                "original_P0_t_constant_exactly_zero_source":"R802 / R872 equation872.34 at marked P0",
                "exact_zero_not_inferred_from_modular_zero":True,
                "N693_constant_mod_prime":b[0],"N693_constant_inverse_mod_prime":invb,
                "original_s_root":SROOT,"factor48s_mod_prime":factor,"factor48s_inverse_mod_prime":invf,
                "quotient_all_three_coefficients_multiplied_back":True,
                "original_t_first_three_coefficients_mod_prime":t,
                "original_t_over_rho_constant_mod_prime":c,
                "exact_c_expression":{
                    "kind":"source_bound_original_jet_expression",
                    "formula":"(a1*b0-a0*b1)/(48*s*b0^2)",
                    "a":"original N692/tau^4 three-jet","b":"original N693/tau^4 three-jet",
                    "jet_evaluation_stage":self.stage_refs["R883-original-cleared-section-three-jets"],
                    "underlying_original_Hensel_source":self.audit()["exact_local_source"],
                    "rho":"z-z0","field":"original K=Q(s), s^2=-3",
                    "all_denominators_units_at_original_p753_place":True},
                "original_t_first_order_unit_certified":True,
                "exact_characteristic_zero_c_rational_expansion_computed":False,
                "frame_conversion":"L*rho^(-m)=(L*c^m)*t^(-m)*(1+O(t))",
                "actual_c_powers_mod_prime":{str(m):pow(c,m,PRIME) for m in (254,1205,1457)},
                "R879_original_reference_frame":"c^254/U272; U272 retained from R879, not normalized to1",
                "R887_original_principal_frame":"L_f*ell_C*c^1205; both original factors retained",
                "reference_U272_or_Qf_leading_constants_newly_evaluated":False,
                "full_rigidification_or_height_computed":False}
        return self.stage("R883-original-t-first-order-unit-and-frame-DAG",produce)

    def run(self):
        if (self.out/FINAL).exists():
            c=read(self.out/FINAL)
            assert c["configuration"]==self.tag and c["complete"] is True
            for r in c["stages"].values():
                check(self.out/r["file"],r)
            self.stage_refs=dict(c["stages"])
            return c
        self.audit();self.leaves();self.recipes();self.evaluate();self.frame()
        c={"result":RESULT,"complete":True,"configuration":self.tag,"p":41,"prime":PRIME,
           "original_zeta_root":ZETA,"original_s_root":SROOT,
           "stages":dict(self.stage_refs),"actual_complete_math_stage_count":len(self.stage_refs),
           "actual_original_t_first_order_unit_certified":True,
           "original_t_frame_DAG_source_certified":True,
           "old_Hensel_jets_inverse_q_tail_or_basis_recomputed":False,
           "characteristic_zero_c_expanded":False,"all_Picard_frames_evaluated":False,
           "five_original_Lj_RR128_or144_computed":False,"height_or_period_computed":False,
           "seconds":time.monotonic()-self.started}
        save(self.out/FINAL,c)
        return c

def main():
    sys.set_int_max_str_digits(0)
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--budget-minutes",type=float,required=True)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    job=None;code=1;error=None;final=None
    try:
        job=Job(a);final=job.run();code=0
    except BudgetStop as e:
        code=124;error={"type":"BudgetStop","message":str(e)}
    except CriterionFailure as e:
        code=2;error={"type":"CriterionFailure","message":str(e)}
    except BaseException as e:
        traceback.print_exc();error={"type":type(e).__name__,"message":str(e)}
    receipt={"result":RESULT,"complete":code==0,"exit_code":code,"error":error,
        "source_sha256":sha(__file__),"configuration_sha256":fingerprint(job.tag) if job else None,
        "certificate_sha256":sha(a.out/FINAL) if final else None,
        "actual_original_t_first_order_unit_certified":bool(final),
        "actual_complete_math_stage_count":len(job.stage_refs) if job else 0,
        "seconds":time.monotonic()-job.started if job else None}
    save(a.out/"core-receipt.json",receipt)
    print("R883_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)
if __name__=="__main__":
    main()
