#!/usr/bin/env python3
"""Explicit read-only schema bridge for the recovered formal PM/PA outputs.

This does not rerun either producer.  Old geometry, moments, jets, full J,
mean bounds, gates, and formal resources remain byte-identified inputs.
New names are aliases.  Missing wr, physical primitive, and mean-height
enclosures follow by exact rational arithmetic from those same inputs.
Derived gzip files are local reproducible views, not old primary evidence.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
import argparse
import copy
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource

PM = "notes/2026-11-12-tail-outer-cell0-seg7-part0-physical-r-moments-r1-summary.json"
PMR = PM.replace("-summary.json", "-resource.json")
PA = "notes/2026-11-12-tail-outer-cell0-seg7-part0-physical-r-audit-r1-summary.json"
PAR = PA.replace("-summary.json", "-resource.json")
CANDIDATE = "notes/2026-11-12-tail-outer-cell0-seg7-substage-r1.json.gz"
READY = "notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json"
EXPECTED = {
    PM: "b899a0915927680dfc133456083b1af591e9347d59a2d1957a0bd6af0cad6687",
    PMR: "b167e48cfb99146ad93db7370dc544e00c7db11b51e7fbc5b366ddb203bbc7f6",
    PA: "75bdfe5d5bcc4fc66fde91ff098f18159fd483c7f5b2017762513f7f7e0e1978",
    PAR: "4555b1bfb814362fd2de27c14e6109997b7940932fe0f5f14c97e6941efc72ea",
    CANDIDATE: "7da554bdb467fe2b997a01971dd4917003fd5deeb36978e200e1457ea3c8fddf",
    READY: "563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6",
}


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


def plain_read(path):
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt") as stream:
        return json.load(stream)


def dyadic(value):
    if isinstance(value, dict):
        m, e = int(value["mantissa"]), int(value["binary_exponent"])
    else:
        m, e = map(int, value)
    return Q(m) * Q(2) ** e


def interval(value):
    if isinstance(value, dict):
        result = dyadic(value["lower"]), dyadic(value["upper"])
    else:
        result = tuple(map(dyadic, value))
    if result[0] > result[1]:
        raise ValueError("Reversed original interval")
    return result


def directed(value, upper, bits=160):
    value = Q(value)
    if not value:
        return [0, 0]
    if value.denominator & (value.denominator-1) == 0:
        m, exponent = value.numerator, 1-value.denominator.bit_length()
        while m % 2 == 0:
            m //= 2
            exponent += 1
        shift = max(0, abs(m).bit_length()-bits)
        unit = 1 << shift
        rounded = -((-m)//unit) if upper else m//unit
        return [rounded, exponent+shift]
    exponent = abs(value.numerator).bit_length() - value.denominator.bit_length() - bits
    scaled = value / (Q(2) ** exponent)
    m = -((-scaled.numerator) // scaled.denominator) if upper else scaled.numerator // scaled.denominator
    return [m, exponent]


def ball_record(value):
    lo, hi = value if isinstance(value, tuple) else (value, value)
    a, b = directed(lo, False), directed(hi, True)
    return {"lower": dict(mantissa=str(a[0]), binary_exponent=a[1]),
            "upper": dict(mantissa=str(b[0]), binary_exponent=b[1]),
            "display": "Exact directed rational-derived enclosure; no new source evaluation"}


def compact(value):
    return [directed(value[0], False, 40), directed(value[1], True, 40)]


def times(a, b):
    products = [x*y for x in a for y in b]
    return min(products), max(products)


def intersection(*values):
    lo, hi = max(x[0] for x in values), min(x[1] for x in values)
    if lo > hi:
        raise ValueError("Two enclosures of one true primitive do not intersect")
    return lo, hi


def write_derived(path, rows):
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=6) as stream:
            for row in rows:
                stream.write((json.dumps(row, separators=(",", ":"), allow_nan=False) + "\n").encode())
    checksum = digest(temporary)
    if path.exists():
        if digest(path) != checksum:
            raise ValueError("Existing derived view has different exact bytes; use a fresh directory")
        temporary.unlink()
    else:
        temporary.replace(path)
    return checksum


class LegacyReader:
    def __init__(self, topic, derived_root, rss_limit_mib=96):
        self.topic, self.derived_root = Path(topic).resolve(), Path(derived_root).resolve()
        self.limit = rss_limit_mib
        self.derived_root.mkdir(parents=True, exist_ok=True)
        self.source_sha = digest(__file__)
        self.checked = {}
        for name, expected in EXPECTED.items():
            self.check(self.topic/name, expected)
        self.pm, self.pa, self.candidate = [plain_read(self.topic/name) for name in (PM, PA, CANDIDATE)]
        for name, summary in ((PM, self.pm), (PA, self.pa), (CANDIDATE, self.candidate)):
            if not summary.get("gates") or not all(v is True for v in summary["gates"].values()):
                raise ValueError("A complete original mathematical gate is absent: " + name)
            self.verify_dependencies(summary)
        self.formal(PM, PMR)
        self.formal(PA, PAR)
        if (self.pm["nodes"] != self.pa["nodes"] or self.pm["nodes"] != self.candidate["nodes"]
                or self.pa["total_panels"] != self.pm["counts"]["final_panels"]
                or self.pa["input_hashes"].get(PM) != EXPECTED[PM]
                or self.pm["input_hashes"].get(CANDIDATE) != EXPECTED[CANDIDATE]
                or self.pm["input_hashes"].get(READY) != EXPECTED[READY]):
            raise ValueError("The two old executions are not the same physical candidate origin")
        for key in ("cell", "segment", "modes", "tau"):
            if self.pm[key] != self.pa[key] or self.pm[key] != self.candidate[key]:
                raise ValueError("Original source identity mismatch: " + key)
        self.views = {}
        self.groups = []
        self.part_views = []
        self.total_mean = Q(0)
        self.total_change = Q(0)
        self.normalize()

    def memory(self):
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > 1024*self.limit:
            raise MemoryError("Owned legacy schema normalization exceeded observed RSS")
        return peak

    def path(self, name):
        path = Path(name)
        return path if path.is_absolute() else self.topic/path

    def check(self, path, expected):
        path = Path(path)
        if not path.is_file() or digest(path) != expected:
            raise ValueError("Restore the exact original bytes; do not rewrite: " + str(path))
        self.checked[str(path)] = expected

    def verify_dependencies(self, record):
        for group in ("input_hashes", "original_candidate_input_hashes", "original_moment_inputs"):
            for name, expected in record.get(group, {}).items():
                self.check(self.path(name), expected)
        for group in ("source_hashes", "original_candidate_source_hashes"):
            for name, expected in record.get(group, {}).items():
                self.check(self.topic/"computations"/Path(name).name, expected)

    def formal(self, summary, resource_name):
        record = plain_read(self.topic/resource_name)
        if record["exitcode"] != 0 or record["termination_signal"] is not None:
            raise ValueError("The old complete producer has no formal successful exit")
        command = record["command"]
        prefix = command[command.index("--out-prefix")+1]
        if self.path(prefix+"-summary.json") != self.topic/summary:
            raise ValueError("The old formal resource belongs to a different output")

    def original_rows(self, group, summary, expected_kind, pm):
        path = self.path(group["output"])
        self.check(path, group["output_sha256"])
        rows = []
        header = trailer = False
        covered, stop = Q(group["source_left"]), Q(group["source_right"])
        with gzip.open(path, "rt") as stream:
            for line in stream:
                row = json.loads(line)
                if row["kind"] == "header":
                    if (header or rows or row["input_hashes"] != summary["input_hashes"]
                            or row["source_hashes"] != summary["source_hashes"]
                            or row["part"] != group["part"]):
                        raise ValueError("Original full primary header identity differs")
                    header = row
                    continue
                if row["kind"] == "trailer":
                    if trailer or not row["complete"] or row["panels"] != len(rows):
                        raise ValueError("Original complete trailer differs")
                    trailer = row
                    continue
                if not header or trailer or row["kind"] != expected_kind or row["panel"] != len(rows):
                    raise ValueError("Original row kind/order differs")
                left, right = Q(row["source_left"]), Q(row["source_right"])
                if left != covered or not left < right <= stop:
                    raise ValueError("Original continuous source cover differs")
                if not pm and (not row["complete_mean_of_defined_new_candidate"]
                        or row["actual_derivative_coordinate"] != "physical r"
                        or any(dyadic(v) <= 0 for v in row["gates_lower"].values())):
                    raise ValueError("Original complete mean or physical-derivative gate absent")
                rows.append(row)
                covered = right
        if not (header and trailer and covered == stop and len(rows) == group["panels"]):
            raise ValueError("The whole original primary was not read")
        return header, rows, trailer

    def normalize(self):
        audit_parts = {row["part"]: row for row in self.pa["parts"]}
        origin_parts = {row["part"]: row for row in self.candidate["parts"]}
        for group in self.pm["parts"]:
            part = group["part"]
            audit = audit_parts[part]
            if any(group[k] != audit[k] for k in ("part", "source_left", "source_right", "panels", "true_width")):
                raise ValueError("The old moment/audit partitions differ")
            mh, mr, mt = self.original_rows(group, self.pm,
                "complete_new_physical_substage_moment_leaf", True)
            ph, pr, pt = self.original_rows(audit, self.pa,
                "complete_new_physical_substage_R64_J_R77_leaf", False)
            width = interval(group["true_width"])
            rleft = interval(self.pm["nodes"][part]["radius"])
            old_cmax = interval(origin_parts[part]["bounds"]["complete_mean_abs"]["value"])[1]
            if min(width[0], rleft[0]) <= 0 or old_cmax < 0:
                raise ValueError("Original true width/radius/mean bound is invalid")
            new_m, new_p = [], []
            mean, change = Q(0), Q(0)
            for m, p in zip(mr, pr):
                if any(m[k] != p[k] for k in ("panel", "source_left", "source_right")):
                    raise ValueError("Original moments and physical fields do not share a leaf")
                mm, pp = copy.deepcopy(m), copy.deepcopy(p)
                u = intersection(interval(m["u"]), (Q(0), Q(1)))
                radius, w, ell = interval(m["radius"]), interval(m["w"]), interval(m["log_w_r"])
                offset = intersection(times(u, width),
                    (radius[0]-rleft[1], radius[1]-rleft[0]), (Q(0), width[1]))
                if interval(m["source_radius_x"])[0] <= 0 or w[0] <= 0 or interval(m["width"])[0] <= 0:
                    raise ValueError("Original positive physical geometry lost")
                mm.update(kind="complete_physical_substage_moment_leaf", part=part,
                    x_left=m["source_left"], x_right=m["source_right"], source_width=m["width"],
                    wr=ball_record(times(w, ell)), physical_offset=ball_record(offset),
                    legacy_schema_aliases_only=True)
                pp.update(mode="physical", complete_mean=True, derivative_coordinate="physical r",
                    legacy_schema_aliases_only=True)
                pp["source"]["source_radius_x"] = compact(interval(m["source_radius_x"]))
                cm = dyadic(p["bounds_upper"]["complete_mean_abs"])
                mass = min(interval(m["width"])[1]*w[1],
                    interval(m["moments"]["00"])[1]+interval(m["moments"]["01"])[1])
                if min(cm, mass) < 0:
                    raise ValueError("Original mean/positive mass is negative")
                mean += cm*mass
                change += (cm+old_cmax)*mass
                new_m.append(mm)
                new_p.append(pp)
            for header in (mh, ph):
                header["legacy_schema_bridge"] = dict(reader_sha256=self.source_sha,
                    original_kind_and_all_numeric_fields_preserved=True)
            ph.update(mode="physical", new_candidate_definition=True)
            moment_path = self.derived_root/f"legacy-part{part:02d}-moments.jsonl.gz"
            field_path = self.derived_root/f"legacy-part{part:02d}-fields.jsonl.gz"
            ms = write_derived(moment_path, [mh, *new_m, mt])
            ps = write_derived(field_path, [ph, *new_p, pt])
            g = copy.deepcopy(group)
            g.update(path=str(moment_path), sha256=ms,
                total_true_positive_moments=group["total_true_physical_moments"],
                bytes=moment_path.stat().st_size,
                legacy_primary_origin=dict(path=str(self.path(group["output"])), sha256=group["output_sha256"]))
            p = copy.deepcopy(audit)
            p.update(path=str(field_path), sha256=ps, bytes=field_path.stat().st_size,
                mean_correction_height_abs=ball_record(mean),
                mean_height_change_from_original_abs=ball_record(change),
                legacy_primary_origin=dict(path=str(self.path(audit["output"])), sha256=audit["output_sha256"]))
            self.groups.append(g)
            self.part_views.append(p)
            self.total_mean += mean
            self.total_change += change
            self.memory()
        self.pm = copy.deepcopy(self.pm)
        self.pa = copy.deepcopy(self.pa)
        self.pm.update(groups=self.groups, whole_original_segment_covered=self.pm["whole_segment_moment_cover"])
        self.pa.update(parts=self.part_views, mode="physical", panels=self.pa["total_panels"],
            whole_original_segment_covered=self.pa["whole_segment_candidate_audited"],
            original_candidate_input_hashes=self.candidate["input_hashes"],
            mean_height_uses_one_global_constant=True,
            endpoint_nonmean_two_jets_exact_by_construction=True,
            two_fixed_mean_endpoint_heights_not_implicitly_claimed=True,
            total_mean_correction_height_abs=ball_record(self.total_mean),
            total_mean_height_change_from_original_abs=ball_record(self.total_change))
        for record in (self.pm, self.pa):
            record["legacy_schema_bridge"] = dict(reader_sha256=self.source_sha,
                old_original_formal_resource_unchanged=True, original_nodes_unchanged=True,
                no_original_mathematical_bound_changed=True,
                new_derivations=["wr=w*log_w_r", "physical_offset in width*u and radius-r_left",
                    "mean height from true positive I00+I01 and complete mean bound"],
                new_Arb_integral_ODE_Node_or_producer_rerun=False)
        self.views[str((self.topic/PM).resolve())] = self.pm
        self.views[str((self.topic/PA).resolve())] = self.pa

    def read(self, path):
        key = str(self.path(path).resolve())
        return copy.deepcopy(self.views[key]) if key in self.views else plain_read(self.path(path))

    def report(self):
        return dict(schema="explicit-original-PM-PA-legacy-reader-v1",
            author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
            source_sha256=self.source_sha, original_inputs_and_sources=self.checked,
            derived_views=[dict(path=g["path"], sha256=g["sha256"], bytes=g["bytes"],
                origin=g["legacy_primary_origin"]) for g in self.groups+self.part_views],
            original_formal_resources=[str(self.topic/PMR), str(self.topic/PAR)],
            original_panels=self.pa["panels"],
            gates=dict(all_original_hashes_verified=True, original_formal_PM_PA_exit0=True,
                all_111_original_moment_and_field_rows_present=True,
                original_numeric_moments_jets_J_and_gates_unchanged=True,
                all_aliases_and_new_rational_enclosures_explicit=True,
                no_new_mean_root_integral_ODE_Arb_or_Node=True),
            peak_RSS_KiB=self.memory())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", type=Path, required=True)
    parser.add_argument("--derived-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--rss-limit-mib", type=int, default=96)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh explicit legacy-reader execution report")
    reader = LegacyReader(args.topic, args.derived_root, args.rss_limit_mib)
    result = reader.report()
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(dict(event="complete_exact_legacy_reader", out=str(args.out),
        gates=result["gates"], original_panels=result["original_panels"],
        peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
