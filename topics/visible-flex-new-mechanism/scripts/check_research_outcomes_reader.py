# Pure read-only printer-branch fixture for a public workflow heredoc.
# No geometry/optimizer import, no retained artifact, no old growth checks.
import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile

script = Path(os.environ["VISIBLE_NEW_SCRIPTS"]) / "print_research_outcomes.py"
spec = importlib.util.spec_from_file_location("printer_branch_fixture", script)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def old_recursive_boolean_lines(value, prefix=""):
    if isinstance(value, dict):
        for key, item in value.items():
            name = prefix + str(key)
            if isinstance(item, bool):
                yield name + ": " + ("true" if item else "false")
            elif isinstance(item, dict):
                yield from old_recursive_boolean_lines(item, name + ".")

with tempfile.TemporaryDirectory(prefix="read-only-printer-fixture-") as temporary:
    folder = Path(temporary)
    dev = {
        "schema": "artificial-printer-branch-only-v1",
        "artificial_inputs_only": True,
        "research_candidate_geometry_evaluated_or_optimized": False,
        "passed": True,
        "new_conservative_growth_check": {
            "direct_new_assertion": False,
            "nested_toy_records": {
                "model_" + str(i): {
                    "nested_repeated_true": True,
                    "nested_repeated_false": False,
                    "deeper": {"another_record_flag": True}
                } for i in range(1200)
            }
        }
    }
    dev_raw = (json.dumps(dev, separators=(",", ":")) + "\n").encode()
    recursive_bytes = len(("\n".join(old_recursive_boolean_lines(dev)) + "\n").encode())
    assert recursive_bytes > 20_000, "fixture must reproduce the old expansion mechanism"
    assert len(dev_raw) < 1_000_000, "fixture remains inside the existing input-size limit"
    (folder / "printer-artificial-development.json").write_bytes(dev_raw)

    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        module.print_development_diagnostics(folder)
    direct = captured.getvalue()
    required_false = "new_conservative_growth_check.direct_new_assertion: false"
    assert "passed: true" in direct
    assert required_false in direct, "the direct false assertion was hidden"
    assert "nested_toy_records.model_" not in direct, "nested toy data were recursively dumped"
    assert len(direct.encode()) < 20_000, "new bounded developer view still expands too much"

    audit = {
        "schema": "same-g-spectral-metric-conservative-trust-growth-audit-v1",
        "status": "artificial-printer-empty-tables-only",
        "phase": "no-scientific-computation",
        "artificial_inputs_only": True,
        "research_candidate_geometry_evaluated_or_optimized": False,
        "initial_state": {},
        "final_state": {},
        "initial_current_constraints": {},
        "initial_doubled_constraints": {},
        "final_full_grid_constraints": {},
        "final_doubled_constraints": {},
        "metric_spectral_trust_growth_stage": {
            "status": "artificial-empty-scientific-tables",
            "solver": {
                "models": [],
                "linear_program_invocation_count": 0
            },
            "checkpoint": {
                "accepted_iterates": [],
                "recovery_events": [],
                "active_row_pool_history": [],
                "fine_physical_row_pool_history": []
            }
        }
    }
    (folder / "printer-artificial-audit.json").write_text(
        json.dumps(audit, separators=(",", ":")) + "\n", encoding="utf-8")
    captured = io.StringIO()
    old_argv = sys.argv
    try:
        sys.argv = [str(script), "--results", str(folder)]
        with contextlib.redirect_stdout(captured):
            module.main()
    finally:
        sys.argv = old_argv
    complete = captured.getvalue()
    science = complete.find("RESEARCH OUTCOMES --")
    development = complete.find("DEVELOPMENT OUTCOMES")
    assert 0 <= science < development, "scientific observations were not printed first"
    assert required_false in complete, "the false assertion was lost through main()"
    assert "MODEL TABLE" in complete and "TRUST/GROWTH TABLE" in complete
    assert len(complete.encode()) < 35_000
    assert set(p.name for p in folder.iterdir()) == {
        "printer-artificial-development.json", "printer-artificial-audit.json"
    }, "the read-only printer wrote an extra file"
    print("New printer branch fixture passed on artificial text only.")
    print("printer source SHA256:", hashlib.sha256(script.read_bytes()).hexdigest())
    print("old recursive developer expansion bytes:", recursive_bytes)
    print("new developer-view bytes:", len(direct.encode()))
    print("complete artificial empty-table log bytes:", len(complete.encode()))
    print("direct false assertion retained; science precedes development; no geometry or optimizer called.")
