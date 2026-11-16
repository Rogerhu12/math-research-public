#!/usr/bin/env python3
"""Five exact original one-Z coefficients and the original constant-term DAG."""
import argparse
from fractions import Fraction
import importlib.util
import os
from pathlib import Path
import sys
import time
import traceback

RESULT = "R852-original-one-Z-coefficients-and-constant-DAG"
FINAL = "p41-original-one-Z-coefficients-certificate.json"
PREFIX = "R852-one-Z-"
DAG_SHA = "afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b"
ZA_SHA = "268fa3fbb9647d7f6f3f781534d9425e09c45ad7945e9aea9a9abd2082834d97"
POINT_SHA = "97a8fb3f185660468e6637358c9c29b34bfe8630599f36fa7e7f58ef6acb582b"
JET_SHA = "555e3c6c877ef2b3fb64f0dfe17f463f49fd6ca83bb1a1faedc2db562724547b"
PQ = [(165,67),(93,67),(100,67),(168,67),(371,134)]
STRATEGY = {
    "original_point": "f=f4(c1), original degree1206 Hom map",
    "original_parameter": "z=a-1; c1 slash exactly once",
    "original_differential": "dx/(2y)",
    "C_formula": "3*((2-p_j/q_j)*a+rho_j*sigma^j(a)+sigma^(-j)(rho_j^(-1)*a))",
    "D_formula": "3*original_secant(f,T^j*f)*original_h_(f+T^j*f)",
    "C_exact_evaluation": "original twelve tangents paired with 3*((2-p_j/q_j)*I+T^j+T^(-j))*f",
    "inverse_Hom_action": "T^(-j)=T^(21-j); original T^7=zeta^2 is retained",
    "elliptic_row": "7*tr_chi_L(C_j*Z+D_j)",
    "trace": "tr_chi_L=c_chi/14*Trace_(L41/Q41), outer factor7 retained",
    "single_Z": "original Z_b(f(c1)); not numerically evaluated here",
    "original_733_nodes_retained_without_changes": True,
    "old_point_additions_or_Hom_matrices_recomputed": False,
    "unit_chart_solved_or_original_height_evaluated": False,
    "budget_excluded_from_mathematical_identity": True,
}

class BudgetStop(Exception):
    pass

def load_io(path):
    import hashlib
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == DAG_SHA
    spec = importlib.util.spec_from_file_location("R852_frozen_exact_DAG", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def enc(q):
    q = Fraction(q)
    return [str(q.numerator), str(q.denominator)]

def matvec(A, v):
    return [sum(a*b for a,b in zip(row,v)) for row in A]

def tangent_vector(value):
    assert len(value) == 2
    out = []
    for component in value:
        denominator = int(component["denominator"])
        assert denominator != 0 and len(component["numerator"]) <= 7
        out.extend(Fraction(int(component["numerator"][i]),denominator)
                   if i < len(component["numerator"]) else Fraction(0)
                   for i in range(7))
    assert len(out) == 14
    return out

def rank_minor(columns):
    """Return an exact row minor; no modular rank or probabilistic assertion."""
    matrix = [list(row) for row in zip(*columns)]
    pivots, selected = {}, []
    for index, original in enumerate(matrix):
        row = list(original)
        for col in sorted(pivots):
            c = row[col]
            row = [x-c*y for x,y in zip(row,pivots[col])]
        if any(row):
            col = next(i for i,x in enumerate(row) if x)
            a = row[col]
            pivots[col] = [x/a for x in row]
            selected.append(index)
    cols = sorted(pivots)
    minor = [[matrix[i][j] for j in cols] for i in selected]
    A, determinant = [list(row) for row in minor], Fraction(1)
    for k in range(len(A)):
        index = next(i for i in range(k,len(A)) if A[i][k])
        if index != k:
            A[k],A[index] = A[index],A[k]
            determinant = -determinant
        pivot = A[k][k]
        determinant *= pivot
        for i in range(k+1,len(A)):
            multiplier = A[i][k]/pivot
            for j in range(k+1,len(A)):
                A[i][j] -= multiplier*A[k][j]
            A[i][k] = Fraction(0)
    assert determinant != 0
    return {
        "rank":len(pivots), "selected_original_rows":selected,
        "selected_columns":cols, "minor_determinant":enc(determinant),
        "matrix_rows_in_original_fourteen_coordinate_order":[[enc(x) for x in row] for row in matrix],
        "exact_echelon_pivots":[{"column":i,"row":[enc(x) for x in pivots[i]]} for i in cols],
        "no_modular_rank_substituted":True,
    }

class Job:
    def __init__(self,args):
        self.args,self.started = args,time.monotonic()
        self.io = load_io(args.dag_core)
        self.out = Path(args.output)
        self.out.mkdir(parents=True,exist_ok=True)
        self.config = c = self.io.read(args.config)
        assert c["result"] == RESULT and c["p"] == 41
        assert c["core_sha256"] == self.io.sha(__file__)
        assert c["dag_core_sha256"] == DAG_SHA and 0 < args.budget_minutes <= 300
        assert c["proofs"]["ZA"]["sha256"] == ZA_SHA
        assert set(c["proofs"]) == {"ZA","method"}
        for row in c["proofs"].values():
            path = (Path(args.topic)/row["path"]).resolve()
            assert path.is_relative_to(Path(args.topic).resolve())
            assert self.io.sha(path) == row["sha256"]
        assert set(c["expanded_sources"]) == {"CM","DAG","JETS","NONTORSION","POINTS","R791"}
        self.sources = {name:self.io.Source(name,item,args.retained)
                        for name,item in c["expanded_sources"].items()}
        self.tag = {
            "result":RESULT,"source_sha256":c["core_sha256"],"p":41,
            "dag_core_sha256":DAG_SHA,"proofs":c["proofs"],
            "source_identities":{name:source.identity for name,source in self.sources.items()},
            "transport_parent_identity":c["transport_parent_identity"],
            "strategy":STRATEGY,
        }
        self.prepare()

    def budget(self):
        if time.monotonic()-self.started > self.args.budget_minutes*60:
            raise BudgetStop("All completed original one-Z stages preserved.")

    def path(self,name):
        return self.out/(PREFIX+name+".json.gz")

    def get(self,name):
        path = self.path(name)
        if not path.exists():
            return None
        value = self.io.read(path)
        assert value["result"] == RESULT and value["configuration"] == self.tag
        assert value["complete"] is True
        return value

    def put(self,name,payload):
        self.budget()
        value = {"result":RESULT,"configuration":self.tag,"complete":True,**payload}
        self.io.save(self.path(name),value)
        print("R852_STAGE "+name+" "+self.io.sha(self.path(name)),flush=True)
        return value

    def ref(self,name):
        return self.io.spec(self.path(name))

    def prepare(self):
        jets,points,hom = (self.sources[k] for k in ("JETS","POINTS","R791"))
        assert jets.certificate["point_program_node_count"] == 733
        assert jets.certificate["original_comparison_first_jets_as_exact_expressions"] is True
        for label,identity in jets.tag["source_identities"].items():
            assert self.sources[label].identity == identity
        self.jet_spec = jets.certificate["jet_program"]
        self.point_spec = points.certificate["point_program"]
        assert self.jet_spec["sha256"] == JET_SHA and self.point_spec["sha256"] == POINT_SHA
        self.old = jets.stage(self.jet_spec)
        self.points = points.stage(self.point_spec)
        assert len(self.old["nodes"]) == self.old["node_count"] == 733
        assert len(self.points["nodes"]) == self.points["node_count"] == 529
        assert self.old["nodes"][:529] == self.points["nodes"]
        assert self.old["imported_R844_nodes_unchanged"] is True
        self.hom = hom.stage(hom.files[self.io.HOM])
        self.tangents = hom.stage(hom.files[self.io.TANGENTS])
        self.hom_ref,self.tangent_ref = hom.ref(self.io.HOM),hom.ref(self.io.TANGENTS)
        self.h_values = self.tangents["actual_L_coefficients_h_i_over_ds_at_c1"]
        assert len(self.h_values) == 12
        assert self.tangents["coordinate"] == "s=a-1 at the original c1"
        assert self.tangents["original_c1_slash_count"] == 1
        assert self.tangents["original_map_index"] == 4
        assert self.hom["all_84_coordinates_verified"] is True
        assert self.hom["gamma_order"] == 21 and self.hom["gamma_seventh_power"] == "zeta^2"
        assert self.sources["NONTORSION"].certificate["all_nonzero_original_L_Hom_values_nontorsion_consequence"] is True
        self.point_by_id = {p["id"]:p for p in self.points["point_records"]}
        self.base = self.point_by_id[self.points["point_labels"]["f"]]
        assert self.base["nonzero_word_value_nontorsion"] is True
        assert self.base["original_Hom_coordinates"] == [str(int(i==4)) for i in range(12)]
        if self.get("source-audit") is None:
            self.put("source-audit",{
                "original_point_program":points.ref(self.point_spec["file"]),
                "original_jet_program":jets.ref(self.jet_spec["file"]),
                "original_tangents":self.tangent_ref,"original_Hom_actions":self.hom_ref,
                "original_nontorsion":self.sources["NONTORSION"].ref(self.sources["NONTORSION"].item["certificate"]["file"]),
                "original_529_and_733_nodes_unchanged":True,
                "all_original_parent_child_identities_verified":True,
                "old_numeric_arithmetic_recomputed":False,
            })

    def program(self):
        saved = self.get("coefficient-program")
        if saved is not None:
            return saved
        p = self.io.Program()
        for node in self.old["nodes"]:
            payload = {k:v for k,v in node.items() if k!="id"}
            assert self.io.fingerprint(payload) == node["id"]
            assert node["id"] not in p.known and all(i in p.known for i in node["inputs"])
            p.nodes.append(dict(node));p.known[node["id"]] = payload
        imported = set(p.known)
        assert len(imported) == 733
        def existing(operation,inputs):
            payload = {"operation":operation,"inputs":list(inputs)}
            key = self.io.fingerprint(payload)
            assert key in imported and p.known[key] == payload
            return key
        def sigma(root,k):
            if k == 0:
                return root
            assert 1 <= k <= 6
            return p.node("original_L_automorphism",(root,),power=k,
                original_transport_source=self.hom_ref,action="sigma_gamma^power",
                field_generator_image_key="field_sigma_b",fixes_zeta=True,
                applies_to_all_exact_leaves_and_constants=True,
                original_unit_chart_is_conjugated_as_a_whole=True)
        def rational(value):
            value = Fraction(value)
            return p.node("rational",numerator=str(value.numerator),denominator=str(value.denominator))
        h_nodes = {}
        rho_nodes = {}
        for node in self.old["nodes"]:
            if node["operation"] != "source_field_element":
                continue
            if node["source_key"] == "actual_L_coefficients_h_i_over_ds_at_c1":
                i = node["source_index"]
                assert node["source"] == self.tangent_ref and node["exact_value"] == self.h_values[i]
                assert i not in h_nodes
                h_nodes[i] = node["id"]
            elif node["source_key"] == "rho_iterates_zero_through_seven":
                i = node["source_index"]
                assert node["source"] == self.hom_ref
                assert node["exact_value"] == self.hom["rho_iterates_zero_through_seven"][i]
                assert i not in rho_nodes
                rho_nodes[i] = node["id"]
        assert set(h_nodes) == set(range(12)) and set(rho_nodes) == set(range(1,6))
        def linear_combination(word):
            terms = [p.mul(rational(x),h_nodes[i]) if x!=1 else h_nodes[i]
                     for i,x in enumerate(word) if x]
            assert terms
            root = terms[0]
            for term in terms[1:]:
                root = p.add(root,term)
            return root
        a = self.old["roots"]["f_h"]
        assert a == self.old["roots"]["h0"] == h_nodes[4]
        C = [[int(x) for x in row] for row in self.hom["gamma_matrix"]]
        assert len(C) == 12 and all(len(row)==12 for row in C)
        baseword = [int(i==4) for i in range(12)]
        roots,rows = dict(self.old["roots"]),[]
        three = p.rational(3)
        branches = {row["label"]:row for row in self.points["addition_branches"]}
        for eta in self.points["five_original_eta_addition_inputs"]:
            self.budget()
            j = eta["j"];rnum,q = map(int,eta["original_rj"]);pn = 2*q+rnum
            assert (pn,q) == PQ[j-1]
            Tpoint = self.point_by_id[self.points["point_labels"]["T"+str(j)+"f"]]
            assert Tpoint["construction"]["power"] == j
            assert Tpoint["construction"]["T_seventh_power"] == "[zeta^2]"
            word_plus = [int(x) for x in Tpoint["original_Hom_coordinates"]]
            word_minus = list(baseword)
            # Application of the frozen operator to the new inverse-direction RHS.
            for _ in range(21-j):
                word_minus = matvec(C,word_minus)
            word = [3*(Fraction(2*q-pn,q)*baseword[i]+word_plus[i]+word_minus[i])
                    for i in range(12)]
            rho = rho_nodes[j]
            inverse_rho_candidates = [n["id"] for n in self.old["nodes"]
                if n["operation"]=="inverse" and n["inputs"]==[rho]
                and n["nonzero_certificate"].get("power")==j]
            assert len(inverse_rho_candidates) == 1
            inverse_rho = inverse_rho_candidates[0]
            branch = branches["g"+str(j)]
            assert branch["type"] == "different_nonopposite_original_Hom_words_secant"
            assert branch["inputs"] == [self.base["id"],Tpoint["id"]]
            x,y = (self.base["coordinates"][k] for k in ("x","y"))
            xx,yy = (Tpoint["coordinates"][k] for k in ("x","y"))
            denominator = existing("add",(xx,existing("negate",(x,))))
            assert denominator == branch["denominator"]
            inverse = branch["inverse"]
            assert p.known[inverse]["operation"] == "inverse"
            assert p.known[inverse]["inputs"] == [denominator]
            numerator = existing("add",(yy,existing("negate",(y,))))
            slope = existing("multiply",(numerator,inverse))
            term_forward = p.mul(rho,sigma(a,j))
            term_backward = sigma(p.mul(inverse_rho,a),7-j)
            croot = p.mul(three,p.add(p.add(p.mul(rational(Fraction(2*q-pn,q)),a),term_forward),term_backward))
            h_g = self.old["roots"]["g"+str(j)+"_h"]
            droot = p.mul(three,p.mul(slope,h_g))
            homroot = linear_combination(word)
            roots["C_"+str(j)],roots["D_"+str(j)] = croot,droot
            roots["C_"+str(j)+"_original_Hom_linear_combination"] = homroot
            rows.append({
                "j":j,"p":str(pn),"q":str(q),"original_rj":eta["original_rj"],
                "C":croot,"D":droot,"C_original_Hom_linear_combination":homroot,
                "C_original_Hom_coordinates":[enc(x) for x in word],
                "Tj_original_Hom_coordinates":[str(x) for x in word_plus],
                "Tminusj_original_Hom_coordinates":[str(x) for x in word_minus],
                "original_rho":rho,"original_inverse_rho":inverse_rho,
                "original_secant":slope,"original_secant_inverse":inverse,
                "original_g_tangent":h_g,"original_g_point_id":eta["g_point_id"],
                "transport_identity":"h(T^j f)=rho_j*sigma^j(a); h(T^(-j)f)=sigma^(-j)(rho_j^(-1)*a)",
                "identity_source":self.hom_ref,"identity_proof":self.config["proofs"]["ZA"],
                "single_Z_trace_row":{"outer_multiplier":"7","C":croot,"D":droot,
                    "Z":"Z_b(f(c1)), still unevaluated","normalized_trace_degree":"14",
                    "original_role_scale":"c_chi, unchanged"},
            })
        assert len(rows) == 5
        assert p.nodes[:733] == self.old["nodes"]
        assert not any(n["operation"] in ("inverse","unit_chart_solve","linear_response","source_field_element")
                       for n in p.nodes[733:])
        return self.put("coefficient-program",{
            "format":"source-bound-exact-arithmetic-DAG","nodes":p.nodes,"node_count":len(p.nodes),
            "roots":roots,"five_original_one_Z_rows":rows,"original_jet_program":self.sources["JETS"].ref(self.jet_spec["file"]),
            "imported_original_node_count":733,"imported_original_nodes_unchanged":True,
            "new_inverse_count":0,"new_point_addition_count":0,
            "original_sigma_applies_to_entire_unit_chart":True,"original_T7_phase_preserved":True,
            "actual_41_Z_computed":False,"actual_height_computed":False,
        })

    def exact_coefficients(self,program):
        saved = self.get("five-exact-C-coordinates")
        if saved is not None:
            return saved
        tangents = [tangent_vector(value) for value in self.h_values]
        rows,columns = [],[]
        for item in program["five_original_one_Z_rows"]:
            self.budget()
            word = [Fraction(int(a),int(b)) for a,b in item["C_original_Hom_coordinates"]]
            vector = [sum((word[i]*tangents[i][k] for i in range(12)),Fraction(0)) for k in range(14)]
            columns.append(vector)
            rows.append({
                "j":item["j"],"original_p":item["p"],"original_q":item["q"],
                "C_root":item["C"],"equal_original_Hom_linear_combination_root":item["C_original_Hom_linear_combination"],
                "original_Hom_coordinates":item["C_original_Hom_coordinates"],
                "exact_original_L_coordinates":[enc(x) for x in vector],
                "nonzero":any(vector),"D_root":item["D"],
            })
        minor = rank_minor(columns)
        return self.put("five-exact-C-coordinates",{
            "basis":"1,b,...,b^6,zeta,zeta*b,...,zeta*b^6; original b and zeta",
            "encoding":"fourteen reduced rational numerator/denominator pairs",
            "original_tangent_source":self.tangent_ref,"coefficient_program":self.ref("coefficient-program"),
            "five_coefficients":rows,"exact_rational_rank_witness":minor,
            "five_C_coefficients_nonzero":all(row["nonzero"] for row in rows),
            "five_C_coefficients_Q_linearly_independent":minor["rank"]==5,
            "no_new_field_model_or_tangent_reconstruction":True,
            "D_coefficients_remain_original_point_DAG_expressions":True,
            "actual_41_values_or_height_nonvanishing_proved":False,
        })

    def manifest(self):
        rows = [self.ref(name) for name in ("source-audit","coefficient-program","five-exact-C-coordinates")
                if self.get(name) is not None]
        self.io.save(self.path("stage-manifest"),{
            "result":RESULT,"configuration":self.tag,"complete":True,"stages":rows,
            "completed_stage_count":len(rows),"retained_for_active_continuation_only":True,
        })
        return rows

    def run(self):
        if (self.out/FINAL).exists():
            cert = self.io.read(self.out/FINAL)
            assert cert["complete"] is True and cert["configuration"] == self.tag
            return cert
        program = self.program()
        exact = self.exact_coefficients(program)
        stages = self.manifest()
        cert = {
            "result":RESULT,"configuration":self.tag,"complete":True,"p":41,
            "original_map_index":4,"original_map_degree":1206,
            "source_audit":self.ref("source-audit"),"coefficient_program":self.ref("coefficient-program"),
            "five_exact_C_coordinates":self.ref("five-exact-C-coordinates"),
            "stage_manifest":self.ref("stage-manifest"),"complete_math_stage_count":len(stages),
            "original_one_Z_coefficient_program_certified":True,
            "five_C_coefficients_in_original_L_exactly_expanded":True,
            "five_C_coefficients_nonzero":exact["five_C_coefficients_nonzero"],
            "five_C_coefficients_Q_linearly_independent":exact["five_C_coefficients_Q_linearly_independent"],
            "exact_C_coefficient_rational_rank":exact["exact_rational_rank_witness"]["rank"],
            "five_D_coefficients_as_original_exact_DAG":True,
            "original_seven_and_normalized_trace_scale_preserved":True,
            "original_T7_phase_and_whole_expression_Galois_action_preserved":True,
            "imported_original_node_count":733,"coefficient_program_node_count":program["node_count"],
            "new_point_addition_count":0,"new_inverse_count":0,
            "old_mathematical_computations_repeated":False,
            "actual_41_response_balls_computed":False,"actual_41_Z_computed":False,
            "D_coefficients_expanded_as_rational_coordinates":False,
            "actual_Y_Picard_period_computed":False,"actual_height_computed":False,
            "height_nonzero_proved":False,"original_CM_candidate_A1_accepted":False,
            "all_p_uniformity_proved":False,"seconds":time.monotonic()-self.started,
        }
        self.io.save(self.out/FINAL,cert)
        print("R852_COMPLETE "+str(program["node_count"])+" rank="+str(cert["exact_C_coefficient_rational_rank"]),flush=True)
        return cert

def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematics only in Rogerhu12/math-research-public Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for flag in ("config","retained","output","topic","dag-core"):
        parser.add_argument("--"+flag,type=Path,required=True)
    parser.add_argument("--budget-minutes",type=float,default=30)
    args = parser.parse_args()
    io = load_io(args.dag_core)
    args.output.mkdir(parents=True,exist_ok=True)
    job,certificate,error,code = None,None,None,0
    try:
        job = Job(args)
        certificate = job.run()
    except BudgetStop as exc:
        error,code = str(exc),75
    except Exception:
        error,code = traceback.format_exc(),1
        print(error,flush=True)
    if job is not None:
        job.manifest()
    io.save(args.output/"core-receipt.json",{
        "result":RESULT,"source_sha256":io.sha(__file__),"complete":code==0,
        "process_exit_code":code,"error":error,
        "configuration":job.tag if job is not None else None,
        "certificate_sha256":io.sha(args.output/FINAL) if certificate is not None else None,
    })
    return code

if __name__ == "__main__":
    raise SystemExit(main())
