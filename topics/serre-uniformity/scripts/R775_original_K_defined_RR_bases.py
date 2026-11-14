#!/usr/bin/env python3
"""R775: actual determinant-semilinear K bases, reusing all R771 E1 input.

New exact arithmetic is executed only in public repository GitHub Actions.
The old R771 group, E1 rows, M2 seeds, and level-one rows are hash-checked
and read verbatim; no old basis arithmetic is invoked.
"""
import argparse
import os
from pathlib import Path
import sys
import time

import flint
from flint import nmod_poly
import R771_original_quotient_RR_bases as old

RESULT = "R775-p41-original-K-defined-RR-bases"
FINAL = "p41-original-K-defined-RR-basis-certificate.json"
OLD_CORE_SHA = "9cda269687a01c95c9c20695be771706bbddd37b1b8fedc8b9258386c3965d46"
OLD_CERT_SHA = "9eb870af949167895daa4e180c16848860f8fea1c9efe1b105ab3cd3a667009f"
OLD_MANIFEST_SHA = "024ed12029720cc1c5d7ec0612aa484b04cdde8f763fceb852a0fdeabc2c3d74"
PROOF_SHA = "30006eca29d55c9b2e227f490e0ec9ffe128073f1c49c6dab25d3e532f4db59d"
OLD_RUN = "43628998192"
OLD_SOURCE = "49abc04d7867c9f56911866494692c597cf642d7"
P, N, ELL, MAX_EXP = old.P, old.N, old.ELL, old.MAX_EXP
sha, read, save = old.sha, old.read, old.save


def rename(name):
    return "R775-"+name[5:] if name.startswith("R771-") else name


class Job(old.Job):
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        assert sha(old.__file__) == OLD_CORE_SHA
        assert sha(args.proof) == PROOF_SHA
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.retained = args.retained
        cp = self.retained/"p41-original-quotient-RR-basis-certificate.json"
        mp = self.retained/"full-outputs-manifest.json"
        assert sha(cp) == OLD_CERT_SHA and sha(mp) == OLD_MANIFEST_SHA
        self.original, self.manifest = read(cp), read(mp)
        assert self.original["complete"]
        assert self.original["configuration"]["source_sha256"] == OLD_CORE_SHA
        assert self.original["M2_dimension"] == 146
        assert self.original["M6_dimension"] == 694
        assert self.original["M12_dimension"] == 1514
        assert self.original["M2_actual_minor"]["determinant_mod_ell"] == 550
        self.manifest_rows = {row["file"]: row for row in self.manifest["files"]}
        self.original_tag = self.original["configuration"]
        self.xi82 = self.original_tag["xi82_mod_ell"]
        self.xi_powers = [pow(self.xi82, j, ELL) for j in range(N)]
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__),
            "python_flint": flint.__version__, "R772_proof_sha256": PROOF_SHA,
            "R771_core_sha256": OLD_CORE_SHA, "R771_run_id": OLD_RUN,
            "R771_source_commit": OLD_SOURCE,
            "R771_certificate_sha256": OLD_CERT_SHA,
            "R771_manifest_sha256": OLD_MANIFEST_SHA,
            "p": P, "level": N, "prime": ELL, "max_exponent_qY": MAX_EXP,
            "xi41_mod_ell": old.XI41, "xi82_mod_ell": self.xi82,
            "sqrt_minus_three_mod_ell": old.SQRTM3,
            "parameter": "qY=Q^3=exp(2*pi*i*tau/82), original reference coset0",
            "K_defined_recipe": "sum_det_d xi82^(j*d82) times B_r|g_d",
            "determinant_exponent": "odd lift modulo82, not the bare residue modulo41",
            "seed_trace": "one_half sum_H82, equivalently126 actual H82/{+-I} terms",
            "arithmetic_descent": "standard GL2 curve overQ, original Y overK by u=24sqrt(-3)(2t-1)",
            "q_series_coefficient_field_not_claimed_K": True,
        }

    def path(self, name):
        return self.out/(rename(name)+".json.gz")

    def store(self, name, value):
        return super().store(rename(name), value)

    def retained_stage(self, name):
        assert Path(name).name == name
        row = self.manifest_rows[name]
        path = self.retained/name
        assert path.is_file() and sha(path) == row["sha256"]
        assert path.stat().st_size == row["bytes"]
        data = read(path)
        assert data["complete"] and data["configuration"] == self.original_tag
        return data

    def group(self):
        return self.retained_stage("R771-original-level82-Eisenstein-label-group.json.gz")

    def eisenstein(self):
        table = []
        for a in range(N):
            data = self.retained_stage("R771-Eisenstein-row-"+str(a).zfill(2)+".json.gz")
            assert data["first_label_coordinate"] == a
            assert data["last_exponent"] == MAX_EXP
            rows = data["series_by_second_coordinate"]
            assert len(rows) == N
            table.append([nmod_poly(row, ELL) for row in rows])
        return table

    def level_one(self):
        data = self.retained_stage("R771-original-E4-E6-eta12-and-RR-denominators.json.gz")
        return {key: nmod_poly(data[key], ELL) for key in ("E4", "E6", "eta12")}

    def determinant_cosets(self, group):
        name = "R775-determinant-cosets"
        prior = self.cached(name)
        if prior and prior["complete"]:
            return prior
        identity = (1, 0, 0, 1)
        candidates = {1: identity}
        for a in range(P):
            for b in range(P):
                det = (a*a+a*b+b*b) % P
                if det and det not in candidates:
                    candidates[det] = (a, -b % P, b, (a+b) % P)
        assert set(candidates) == set(range(1, P))
        H = {tuple(h) for h in group["H82"]}
        assert len(H) == 252
        rows = []
        for d in range(1, P):
            gp = candidates[d]
            g = tuple(gp[i]+P*((identity[i]-gp[i]) % 2) for i in range(4))
            d82 = d if d % 2 else d+P
            assert (g[0]*g[3]-g[1]*g[2]) % N == d82
            invdet = pow(d82, -1, N)
            gi = tuple(invdet*x % N for x in (g[3], -g[1], -g[2], g[0]))
            assert old.mm(g, gi, N) == identity
            assert {old.mm(old.mm(g, h, N), gi, N) for h in H} == H
            rows.append({"det_mod41": d, "det_mod82": d82, "matrix": list(g)})
        assert rows[0]["matrix"] == list(identity)
        assert len({r["det_mod82"] for r in rows}) == 40
        return self.store(name, {"complete": True, "cosets": rows,
            "H82_order": 252, "GL_group_order": 10080,
            "all_representatives_normalize_original_H82": True,
            "original_mod2_component": "identity",
            "original_mod41_component": "matrix(a,-b;b,a+b), norm a^2+a*b+b^2"})

    def transported_seed(self, index, group, cosets, table, original_first):
        """Cache each new coset image; the determinant-one row is read verbatim."""
        name = "R775-seed-images-"+str(index).zfill(3)
        prior = self.cached(name)
        seed = self.original["M2_exact_seeds"][index]
        if prior is not None:
            assert prior["seed_index"] == index and prior["original_seed"] == seed
            rows = prior["images"]
        else:
            rows = []
        if prior and prior["complete"]:
            assert len(rows) == 40
            return [nmod_poly(r["coefficients_mod_ell"], ELL) for r in rows]
        H = [tuple(h) for h in group["H82_mod_center"]]
        assert len(H) == 126
        first, second = seed["lambda"], seed["mu"]
        for position in range(len(rows), 40):
            spec = cosets["cosets"][position]
            g = tuple(spec["matrix"])
            if position == 0:
                retained = original_first["basis"][index]
                assert retained["recipe"] == seed
                ans = nmod_poly(retained["coefficients_mod_ell"], ELL)
                reused = True
            else:
                ans = nmod_poly([], ELL)
                for h in H:
                    hg = old.mm(h, g, N)
                    a, b = old.action(first, hg)
                    c, d = old.action(second, hg)
                    ans += old.product(table[a][b], table[c][d])
                ans = ans.truncate(MAX_EXP+1)
                reused = False
            rows.append({"det_mod41": spec["det_mod41"],
                         "det_mod82": spec["det_mod82"],
                         "coefficients_mod_ell": old.coefficients(ans),
                         "old_determinant_one_row_reused": reused})
            self.store(name, {"complete": len(rows) == 40, "seed_index": index,
                             "original_seed": seed, "images": rows,
                             "completed_coset_images": len(rows)})
        return [nmod_poly(r["coefficients_mod_ell"], ELL) for r in rows]

    def k_weight_two(self, group, table, cosets):
        first = self.retained_stage("R771-basis-M2.json.gz")
        assert first["rank"] == 146
        assert [r["recipe"] for r in first["basis"]] == self.original["M2_exact_seeds"]
        current_seed, current_images = None, None

        def recipes():
            for r, seed in enumerate(self.original["M2_exact_seeds"]):
                for j in range(40):
                    yield {"kind": "det_semilinear_E1_pair_trace",
                           "R771_seed_index": r, "j": j,
                           "lambda": seed["lambda"], "mu": seed["mu"],
                           "phase": "xi82^(j*det(g)_mod82)",
                           "exact_global_field": "K"}

        def evaluate(recipe):
            nonlocal current_seed, current_images
            r, j = recipe["R771_seed_index"], recipe["j"]
            if current_seed != r:
                current_images = self.transported_seed(r, group, cosets, table, first)
                current_seed = r
            ans = nmod_poly([], ELL)
            for spec, value in zip(cosets["cosets"], current_images):
                ans += value*self.xi_powers[(j*spec["det_mod82"]) % N]
            return ans.truncate(MAX_EXP+1)

        return self.select("R775-basis-M2", [], recipes(), evaluate, 146, 273, 40)


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New exact arithmetic belongs to the public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--retained", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        job = Job(args)
        final = args.output/FINAL
        if final.exists():
            cert = read(final)
            assert cert["complete"] and cert["configuration"] == job.tag
            for row in cert["stages"]:
                assert sha(args.output/row["file"]) == row["sha256"]
            save(args.output/"core-receipt.json", {
                "result": RESULT, "complete": True, "source_sha256": sha(__file__),
                "certificate_sha256": sha(final), "reused_complete": True})
            return
        group, table = job.group(), job.eisenstein()
        cosets = job.determinant_cosets(group)
        first = job.k_weight_two(group, table, cosets)
        spaces, polys = job.powers(first)
        full = job.augment(spaces, polys, job.level_one())
        stages = [{"file": p.name, "bytes": p.stat().st_size, "sha256": sha(p)}
                  for p in sorted(args.output.glob("R775-*.json.gz"))]
        cert = {
            "result": RESULT, "complete": True, "configuration": job.tag,
            "p": P, "level": N, "prime": ELL, "source_quotient_genus": 127,
            "M2_dimension": 146, "M2_actual_minor": first["actual_nonzero_minor"],
            "M2_actual_K_recipes": [r["recipe"] for r in first["basis"]],
            "M2_processed_candidates": first["processed_candidates"],
            "M6_dimension": full[6]["rank"], "M6_actual_minor": full[6]["actual_nonzero_minor"],
            "M12_dimension": full[12]["rank"], "M12_actual_minor": full[12]["actual_nonzero_minor"],
            "power_basis_dimensions": {str(k): spaces[k]["rank"] for k in range(1, 7)},
            "all_recipes_defined_over_original_K": True,
            "RR_basis": "new_K_defined_F_i/(eta12/2-sqrt(-3)*E6/144)^2",
            "RR_divisor": "2*(t)_0, degree1640",
            "selected_actual_map_index": 4, "selected_actual_map_degree": "1206",
            "unknown_original_map_coefficients_field": "L=K(b), degree7 overK",
            "reference_cusp_coefficient_field": "M=L(xi41), degree40 overL",
            "actual_original_y_or_beta_or_height_computed": False,
            "full_characteristic_zero_q_series_computed": False,
            "old_E1_group_level_one_and_original_M2_recomputed": False,
            "old_topology_periods_Hom_lattice_or_degrees_recomputed": False,
            "stages": stages, "seconds": time.monotonic()-job.started}
        save(final, cert)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(final), "M2_dimension": 146,
            "M6_dimension": 694, "M12_dimension": 1514,
            "all_recipes_defined_over_original_K": True})
        print({"result": RESULT, "complete": True}, flush=True)
    except BaseException as error:
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "error": type(error).__name__+": "+str(error), "completed_stages_preserved": True})
        raise


if __name__ == "__main__":
    main()
