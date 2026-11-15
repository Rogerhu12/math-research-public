#!/usr/bin/env python3
"""R795: new ordinary power6 qY0..81 rows from completed power1/5 rows."""
import argparse
from functools import lru_cache
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpz_poly

RESULT = "R795-exact-original-power6-short-basis"
FINAL = "p41-exact-original-power6-short-basis-certificate.json"
P, LEVEL, ELL, XI, CYC, PACK = 41, 82, 739, 538, 40, 79
BOUND, ROWS, POWER, DIMENSION = 81, 82, 6, 1506
PACK_LENGTH = PACK*ROWS
R793_PROOF_SHA = "6f716b64432227244a46d91f01ae2f46ba6d4a5f893666693ed07dec9e2e5cab"
R775_POWER6 = "R775-basis-power-6.json.gz"
R775_POWER6_SHA = "05c5580b73eeba72b832e2a871221c19c482baf1c9656cab62a0c2c694ffafa1"
R786_CERT_SHA = "dc6c23568f80b861d839280846c3250063abdfb2716a20481779816bb7cd37d9"
R786_INDEX_SHA = "0bb7cfeda48d6759f1553dec74485a28dc16e31cf3d500a095963888973c9b35"
R786_INVENTORY_SHA = "f8bf6c1d9968b0acd3664b2480efbe9d6563a0a61ef4bd027fff3bf96a4d3f02"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))+"\n").encode("utf-8")
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb",
                               mtime=0, compresslevel=2) as compressed:
                compressed.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


class Retained:
    def __init__(self, root, label, spec):
        self.directory, self.spec = Path(root)/label, spec
        mp = self.directory/"full-outputs-manifest.json"
        assert sha(mp) == spec["manifest_sha256"]
        manifest = read(mp)
        assert manifest["result"] == spec["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        run, core, initial = (self.raw(name) for name in
                             ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert run["result"] == spec["result"] and str(run["workflow_run_id"]) == str(spec["run_id"])
        assert run["source_commit"] == spec["source_commit"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
        assert initial["source_commit"] == spec["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == spec["core_sha256"]
        name = spec["certificate_name"]
        assert self.files[name]["sha256"] == core["certificate_sha256"] == spec["files"][name]
        self.certificate = self.raw(name)
        assert self.certificate["complete"] is True and self.certificate["result"] == spec["result"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == spec["core_sha256"] and self.tag["python_flint"] == "0.9.0"

    def raw(self, name, expected=None):
        assert Path(name).name == name
        row = self.files[name]
        if expected is not None:
            assert row["sha256"] == expected
        if name in self.spec["files"]:
            assert row["sha256"] == self.spec["files"][name]
        path = self.directory/name
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        return read(path)

    def get(self, name, expected=None):
        value = self.raw(name, expected)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def get_spec(self, spec):
        assert self.files[spec["file"]]["bytes"] == spec["bytes"]
        return self.get(spec["file"], spec["sha256"])


class BudgetStop(RuntimeError):
    pass


def multiply(a, b):
    product = a.mul_low(b, PACK_LENGTH)
    answer = []
    for n in range(ROWS):
        block, offset = [0]*P, PACK*n
        for r in range(2*CYC-1):
            block[r % P] += int(product[offset+r])
        answer.append([block[r]-block[40] for r in range(CYC)])
    return answer


class Job:
    def __init__(self, args):
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.config = read(args.config)
        assert flint.__version__ == "0.9.0"
        assert self.config["producer_inputs_pending"] is False
        assert self.config["result"] == RESULT and self.config["p"] == P
        assert self.config["core_sha256"] == sha(__file__)
        assert self.config["ordinary_power"] == POWER and self.config["ordinary_power_dimension"] == DIMENSION
        assert self.config["basis_bound_qY"] == BOUND
        assert sha(args.proof) == self.config["R793_proof_sha256"] == R793_PROOF_SHA
        assert sha(args.method) == self.config["R795_method_sha256"]
        assert set(self.config["retained_artifacts"]) == {"R775", "R786"}
        self.r775, self.r786 = (Retained(args.retained, name, self.config["retained_artifacts"][name])
                                for name in ("R775", "R786"))
        assert self.r775.certificate["power_basis_dimensions"]["6"] == DIMENSION
        assert self.r775.certificate["all_recipes_defined_over_original_K"] is True
        stages775 = {row["file"]: row for row in self.r775.certificate["stages"]}
        assert stages775[R775_POWER6]["sha256"] == R775_POWER6_SHA
        self.basis = self.r775.get_spec(stages775[R775_POWER6])
        assert self.basis["rank"] == DIMENSION and len(self.basis["basis"]) == DIMENSION
        assert self.basis["characteristic_zero_independence_certified_by_unit_reduction"] is True
        assert self.basis["coefficient_bound"] >= 272*POWER
        minor = self.basis["actual_nonzero_minor"]
        assert minor["prime"] == ELL and int(minor["determinant_mod_ell"]) % ELL
        assert minor["rows"] == minor["columns"] == DIMENSION
        assert self.r775.tag["xi41_mod_ell"] == XI and self.r775.tag["prime"] == ELL
        cert786 = self.r786.certificate
        assert self.r786.files[self.r786.spec["certificate_name"]]["sha256"] == R786_CERT_SHA
        assert cert786["basis_in_original_R775_saved_order"] is True
        assert cert786["exact_power5_basis_dimension"] == 1234
        assert cert786["exact_K_basis_prefix_bound_qY"] == 128
        assert cert786["basis_index"]["sha256"] == R786_INDEX_SHA
        assert cert786["stages_manifest"]["sha256"] == R786_INVENTORY_SHA
        self.index = self.r786.get_spec(cert786["basis_index"])
        inventory = self.r786.get_spec(cert786["stages_manifest"])
        self.stage_rows = {row["file"]: row for row in inventory["files"]}
        assert self.index["dimension"] == 1234
        assert [row["index"] for row in self.index["basis_rows"]] == list(range(1234))
        old_prefix = self.r786.tag["R775_completed_prefix_producer"]
        for name in ("R775-basis-M2.json.gz", "R775-basis-power-5.json.gz"):
            assert old_prefix["files"][name] == stages775[name]["sha256"]
        self.tag = {"result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R793_proof_sha256": sha(args.proof), "R795_method_sha256": sha(args.method),
            "retained_artifacts": self.config["retained_artifacts"],
            "p": P, "level": LEVEL, "ordinary_power": POWER, "ordinary_power_dimension": DIMENSION,
            "basis_bound_qY": BOUND, "basis_integer_scale": str(LEVEL**(2*POWER)),
            "original_reference_cusp": "coset0; qY=Q^3=exp(2*pi*i*tau/82)",
            "new_E1_or_old_power1_to5_arithmetic": False}
        T = fmpz_poly([0, 1])
        self.chebyshev = [fmpz_poly([2]), T]
        for _ in range(2, 21):
            self.chebyshev.append(T*self.chebyshev[-1]-self.chebyshev[-2])
        self.real_modulus = fmpz_poly([1])
        for value in self.chebyshev[1:]:
            self.real_modulus += value
        assert self.real_modulus.degree() == 20 and self.real_modulus[20] == 1
        self.xipowers = [pow(XI, r, ELL) for r in range(CYC)]

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes:
            raise BudgetStop("Completed new power6 rows retained; resume the same exact configuration.")

    def path(self, name):
        assert name.startswith("R795-") and Path(name).name == name
        return self.out/(name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        data = read(path)
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def store(self, name, data):
        save(self.path(name), dict(data, complete=True, configuration=self.tag))
        return file_spec(self.path(name))

    @lru_cache(maxsize=160)
    def original_factor(self, power, index):
        assert power in (1, 5) and 0 <= index < (146 if power == 1 else 1234)
        name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
        spec = self.stage_rows[name]
        if power == 5:
            indexed = self.index["basis_rows"][index]
            assert indexed["index"] == index and indexed["file"] == name
            assert indexed["sha256"] == spec["sha256"] and indexed["bytes"] == spec["bytes"]
        row = self.r786.get_spec(spec)
        assert row["weight"] == 2*power and row["bound_qY"] == 128
        assert row["integer_scale"] == str(LEVEL**(2*power))
        assert row["original_R775_finite_coefficients_verified"] is True
        old = row["integer_qY_xi_coefficients"]
        assert len(old) == 129 and all(len(values) == CYC for values in old)
        packed = [0]*PACK_LENGTH
        for n, values in enumerate(old[:ROWS]):
            for r, value in enumerate(values):
                packed[PACK*n+r] = int(value)
        return fmpz_poly(packed)

    def real_coordinates(self, rows):
        output = []
        for n, values in enumerate(rows):
            cyclic = [0]*P
            for r, value in enumerate(values):
                cyclic[(r+10*n) % P] += value
            reduced = [value-cyclic[40] for value in cyclic[:40]]+[0]
            assert all(reduced[r] == reduced[41-r] for r in range(1, 21))
            real = fmpz_poly([reduced[0]])
            for r in range(1, 21):
                real += self.chebyshev[r]*reduced[r]
            real %= self.real_modulus
            output.append([str(real[r]) for r in range(20)])
        return output

    def row(self, index):
        original = self.basis["basis"][index]
        recipe = original["recipe"]
        assert recipe["kind"] == "product"
        assert recipe["left_power"] == 1 and recipe["right_power"] == 5
        name = "R795-exact-power-6-row-"+str(index).zfill(4)
        old = self.cached(name)
        if old:
            assert old["index"] == index and old["recipe"] == recipe
            return file_spec(self.path(name))
        self.budget()
        left = self.original_factor(1, recipe["left_index"])
        right = self.original_factor(5, recipe["right_index"])
        rows = multiply(left, right)
        finite = original["coefficients_mod_ell"]
        finite_scale = pow(LEVEL, 2*POWER, ELL)
        for n, values in enumerate(rows):
            actual = sum(a*b for a, b in zip(values, self.xipowers)) % ELL
            expected = finite_scale*(int(finite[n]) if n < len(finite) else 0) % ELL
            assert actual == expected, (index, n, "original R775 mod739 coefficient")
        factors = []
        for power, position in ((1, recipe["left_index"]), (5, recipe["right_index"])):
            old_name = "R786-exact-power-"+str(power)+"-row-"+str(position).zfill(4)+".json.gz"
            factors.append(dict(self.stage_rows[old_name], power=power, index=position))
        return self.store(name, {"index": index, "recipe": recipe, "weight": 12,
            "bound_qY": BOUND, "integer_scale": str(LEVEL**12),
            "integer_qY_xi_coefficients": [[str(value) for value in row] for row in rows],
            "integer_v_t_coefficients": self.real_coordinates(rows),
            "v_parameter": "v=xi41^-10*qY", "t_parameter": "t=xi41+xi41^-1",
            "original_R786_factor_rows": factors,
            "original_R775_finite_coefficients_verified": True,
            "all_original_phase_involutions_verified": True, "averaging_used": False,
            "old_factor_rows_recomputed": False, "coefficients_after_qY81_generated": False})

    def run(self):
        final = self.out/FINAL
        if final.exists():
            cert = read(final)
            assert cert["complete"] is True and cert["configuration"] == self.tag
            inventory = cert["stage_manifest"]
            assert sha(self.out/inventory["file"]) == inventory["sha256"]
            for row in read(self.out/inventory["file"])["files"]:
                assert sha(self.out/row["file"]) == row["sha256"]
                assert (self.out/row["file"]).stat().st_size == row["bytes"]
        else:
            rows = []
            for index in range(DIMENSION):
                rows.append(dict(self.row(index), index=index))
                if index % 32 == 0 or index+1 == DIMENSION:
                    print(json.dumps({"stage": "exact_power6_q0_to81", "complete_rows": index+1,
                                      "total_rows": DIMENSION, "seconds": time.monotonic()-self.started}), flush=True)
            index = self.store("R795-exact-power6-basis-index", {"basis_rows": rows,
                "dimension": DIMENSION, "ordinary_power": POWER, "bound_qY": BOUND,
                "integer_scale": str(LEVEL**12), "basis_selection_recomputed": False,
                "short_prefix_injectivity": "R793: 20*82>deg(6L)=1632",
                "actual_inherited_R775_minor": self.basis["actual_nonzero_minor"]})
            manifest = self.store("R795-exact-stages-manifest", {"files": [file_spec(path)
                for path in sorted(self.out.glob("R795-*.json.gz"))
                if path.name != "R795-exact-stages-manifest.json.gz"]})
            cert = {"result": RESULT, "configuration": self.tag, "complete": True,
                "p": P, "ordinary_power": POWER, "exact_power6_basis_dimension": DIMENSION,
                "exact_K_basis_prefix_bound_qY": BOUND, "basis_integer_scale": str(LEVEL**12),
                "basis_in_original_R775_saved_order": True,
                "all_original_R775_mod739_short_series_compared": True,
                "all_original_real_cyclotomic_transports_verified": True,
                "old_E1_M2_power1_to5_or_Laurent_recomputed": False,
                "coefficients_after_qY81_generated": False,
                "actual_multiplication_table_polar_divisor_beta_eta_or_height_computed": False,
                "basis_index": index, "stage_manifest": manifest,
                "actual_inherited_R775_power6_minor": self.basis["actual_nonzero_minor"],
                "seconds": time.monotonic()-self.started}
            save(final, cert)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(final),
            "exact_power6_dimension": DIMENSION, "exact_prefix_qY": BOUND,
            "actual_multiplication_table_polar_divisor_beta_eta_or_height_computed": False})
        return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "method", "proof", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        return Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "completed_stages_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
