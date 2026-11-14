#!/usr/bin/env python3
"""Evaluate the retained actual Phi_C on all four R2-valued T3 targets."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

P, Q = 47, 47**4


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(data, sort_keys=True, separators=(",", ":"))+"\n").encode()
    temp = path.with_suffix(path.suffix+".new")
    temp.write_bytes(gzip.compress(raw, mtime=0))
    temp.replace(path)


class T3Norm:
    def __init__(self, args):
        import p41_r2_matrix as r
        from p41_actual_differentials47 import ActualModel
        from p41_projective_jet_frames47 import ProjectiveJetFrames, install_exact_float_mm
        from p41_miller_unit_atlas47 import MillerUnitAtlas
        from p41_ordinary_B_fibre47 import Engine as BEngine
        from p41_ordinary_t2_etale_norm47 import SplitNorm
        install_exact_float_mm(r)
        self.a = a = ActualModel(args.script_dir)
        self.r, self.np, self.args = r, a.np, args
        self.inputs = dict(a.inputs)
        self.based = read(args.based_points)
        self.inputs[args.based_points.name] = sha(args.based_points)
        self.bases = a.read("p41_hecke3_abel_bases_checkpoint.json.gz")
        self.family = self.bases["families"][0]
        self.v1 = r.from_json(self.family["v_coefficients"])
        self.fb = r.from_json(self.based["f_b_coefficients"])
        BEngine.load(self, args.second_kind_certificate, args.multiplication,
                     args.transport_directory, args.principal_expression)
        self.preparer = MillerUnitAtlas.__new__(MillerUnitAtlas)
        self.preparer.a, self.preparer.r, self.preparer.np = a, r, a.np
        self.helper = ProjectiveJetFrames(a)
        self.support = read(args.support)
        assert self.support["complete_actual_T3_support"]
        assert self.support["source_disk_id"] == self.disk_id
        assert self.support["raw_level_determinant_mod41"] == 3
        assert self.support["total_target_degree"] == 4
        assert self.flat["combined_function_to_actual_A1_t"]["f0_integer_exponent"] == 0
        self.W0 = r.from_json([x["W_actual_values_in_R2"] for x in self.support["branch_records"]])
        assert self.W0[0].shape == (4, 73)
        self.inputs.update(a.inputs)
        self.inputs[args.support.name] = sha(args.support)
        self.dependency_sources = {name+".py":sha(sys.modules[name].__file__) for name in [
            "p41_ordinary_B_fibre47","p41_projective_jet_frames47",
            "p41_miller_unit_atlas47","p41_ordinary_t2_etale_norm47"]}
        # This sealed routine is independent of ell and number of points:
        # it evaluates all real functions and verifies all455 divisor relations.
        self.process_chart = lambda chart: SplitNorm.process(self, chart)

    def run(self):
        from p41_miller_unit_atlas47 import ONE, ZERO, add, mul, log_unit
        charts, rows, caches = [], [], []
        self.args.cache_dir.mkdir(parents=True, exist_ok=True)
        for index, chart in enumerate(self.helper.iter_charts(
                self.W0, order=27, max_points=4, label=self.disk_id+"_T3")):
            path = self.args.cache_dir/(self.disk_id+"_T3_chart"+str(index)+"_jets27.json.gz")
            cache = {name:[self.r.to_json(x) for x in chart[name]] for name in ["W","V2","V3"]}
            cache.update({name:self.r.to_json(chart[name]) for name in ["frame","coordinate"]})
            cache.update({"indices_0based":chart["indices_0based"],"input_sha256":self.inputs,
                          "source_sha256":sha(__file__),"order":27})
            save(path,cache)
            result = self.process_chart(chart)
            charts.append(result)
            rows.extend(result["rows"])
            caches.append({"basename":path.name,"sha256":sha(path),"bytes":path.stat().st_size})
        assert sorted(x["target_branch_0based"] for x in rows) == [0,1,2,3]
        norm, logarithm = ONE, ZERO
        for row in rows:
            norm = mul(norm,row["actual_Phi_value"])
            logarithm = add(logarithm,row["actual_log_Phi_value"])
        assert norm[1] == logarithm[1] == 0 and log_unit(norm) == logarithm
        output = {
            "level":41,"auxiliary_prime":P,"precision":4,"modulus":Q,"disk_id":self.disk_id,
            "complete_actual_principal_norm_on_T3_P":True,"actual_target_degree":4,
            "target_kernel_polynomial_ascending":self.support["kernel_polynomial_ascending"],
            "actual_function":"Phi_C, divisor=scale*(P_center-P_minus3)-A1(t)",
            "actual_norm_Phi_T3_P_mod47four":norm[0],
            "actual_log_norm_Phi_T3_P_mod47four":logarithm[0],
            "all_four_actual_target_disks_prepared":True,
            "all455_actual_distinguished_relations_in_each_disk":True,
            "f0_may_be_nonunit_and_its_exact_final_integer_exponent_is_zero":True,
            "rows":rows,"charts":charts,"jet_cache_manifest":caches,
            "input_sha256":self.inputs,"dependency_sources_sha256":self.dependency_sources,
            "source_sha256":sha(__file__),
            "complete_actual_local_sigma_F3_height":False,
            "complete_all53_local_QC_heights":False,"complete_common_roots":False,
        }
        save(self.args.output,output)
        print("PASS ACTUAL T3 PRINCIPAL NORM",self.disk_id,norm[0],logarithm[0],
              "SHA",sha(self.args.output),flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ["script-dir","support","principal-expression","transport-directory",
                 "based-points","second-kind-certificate","multiplication","cache-dir","output"]:
        ap.add_argument("--"+name,type=Path,required=True)
    args = ap.parse_args()
    sys.path.insert(0,str(args.script_dir.resolve()))
    T3Norm(args).run()


if __name__=="__main__":
    main()

