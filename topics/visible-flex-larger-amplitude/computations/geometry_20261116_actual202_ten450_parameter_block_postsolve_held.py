#!/usr/bin/env python3
"""R452: original R425 after actual202/205 parameter choice and shared field.

Only the frozen R438 held wrapper's explicit producer/reader registry and
output identities change. Its complete original geometry CLI, dependencies,
owned process, absolute deadline, return handling and <=90KB necessary reader
remain in the source view below. Metric/reach success is never a prerequisite.
No scientific implementation is copied or evaluated by this text adapter.
Author: AI, 2026-11-16.
"""
from __future__ import annotations
import hashlib
from pathlib import Path
import types

BASE_NAME = "geometry_20261116_current_C_ten450_original_or_refined_block_postsolve_held.py"
BASE_SHA = "119ec38cc9351a2d040ce8c7101b933e1e572d19deabb7baf62c4c1cec62eada"
SCHEMA = 'R452-actual202-ten450-parameter-block-same-job-held-after-shared-v1'
INPUT_SCHEMA = SCHEMA + "-input-v1"
READBACK_SCHEMA = SCHEMA + "-necessary-v1"
PROCEDURE_NAME = 'geometry_20261116_actual202_ten450_parameter_block_postsolve.py'
PROCEDURE_SHA = '89a90b2d5d762510c228c5d3a4f6fe27a573c890b760268aecace2a44ab9e010'
PROCEDURE_SCHEMA = 'R452-actual202-accurate-ten450-first-parameter-block-postsolve-v1'
READER_NAME = 'root_20261116_actual202_ten450_parameter_block_postsolve_necessary.py'
READER_SHA = 'e3a4a70277c3267ff412e1ac3f63590be135ed28f5cfc3c1e553e4e2e9cd7f3c'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def replace_once(text, before, after):
    require(text.count(before) == 1, "The exact frozen R438 source fragment changed")
    return text.replace(before, after, 1)


path = Path(__file__).resolve().with_name(BASE_NAME)
raw = path.read_bytes()
require(hashlib.sha256(raw).hexdigest() == BASE_SHA, "Keep the complete frozen R438 held source")
text = raw.decode("utf-8")
registry_start = text.index("SUPPORTED_POSTSOLVE = {\n")
registry_end = text.index("\nPARAMETERS = (", registry_start)
old_registry = text[registry_start:registry_end]
new_registry = '''SUPPORTED_POSTSOLVE = {
    "''' + PROCEDURE_NAME + '''": dict(
        sha256="''' + PROCEDURE_SHA + '''",
        schema="''' + PROCEDURE_SCHEMA + '''",
        input_schema="''' + PROCEDURE_SCHEMA + '''-input-v1"),
}'''
REPLACEMENTS = (
    ('SCHEMA = "R438-current-C-ten450-original-or-refined-block-same-job-held-after-shared-v1"',
     'SCHEMA = "' + SCHEMA + '"'),
    ('POSTREAD = "root_20261115_current_C_ten450_postsolve_necessary.py"',
     'POSTREAD = "' + READER_NAME + '"'),
    ('POSTREAD: "79296f4ff205542cf99091ada7fd9a7055e68ffb04173bd242592769c8d4ca2f"',
     'POSTREAD: "' + READER_SHA + '"'),
    (old_registry, new_registry),
    ('Use the independent R438 held runtime input schema',
     'Use the independent R452 held runtime input schema'),
    ('Declare only the complete explicit R438 held input fields',
     'Declare only the complete explicit R452 held input fields'),
    ('module_name = "_R438_held_"', 'module_name = "_R452_held_"'),
    ('Use a fresh independently owned R438 held output',
     'Use a fresh independently owned R452 held output'),
    ('R438 held owns a sibling, never the previous geometry input tree',
     'R452 held owns a sibling, never the previous geometry input tree'),
    ('event="R438_original_R425_invocation_returned"',
     'event="R452_original_R425_invocation_returned"'),
    ('Read this frozen R438 held source, never relabel a different wrapper',
     'Read this frozen R452 held source, never relabel a different wrapper'),
    ('The actual R438 held runtime recipe/output identity differs',
     'The actual R452 held runtime recipe/output identity differs'),
    ('BEGIN_R438_CURRENT_C_ORIGINAL_OR_REFINED_BLOCK_HELD_NECESSARY',
     'BEGIN_R452_CURRENT_TEN_PARAMETER_BLOCK_HELD_NECESSARY'),
    ('END_R438_CURRENT_C_ORIGINAL_OR_REFINED_BLOCK_HELD_NECESSARY',
     'END_R452_CURRENT_TEN_PARAMETER_BLOCK_HELD_NECESSARY'),
    ('event="R438_held_necessary_readback_identity"',
     'event="R452_held_necessary_readback_identity"'),
    ('delimiter = "R438_HELD_"', 'delimiter = "R452_HELD_"'),
)
for before, after in REPLACEMENTS:
    text = replace_once(text, before, after)
VIEW_IDENTITY = dict(
    original_source=dict(file=str(path), bytes=len(raw), sha256=BASE_SHA),
    actual_source_view_bytes=len(text.encode("utf-8")),
    actual_source_view_sha256=hashlib.sha256(text.encode("utf-8")).hexdigest(),
    actual_parameter_procedure=dict(file=PROCEDURE_NAME, sha256=PROCEDURE_SHA),
    actual_parameter_reader=dict(file=READER_NAME, sha256=READER_SHA),
    original_R425_scientific_CLI_or_gates_changed=False,
    original_three_dependency_producer_checks_changed=False,
    original_owned_process_and_absolute_deadline_body_changed=False,
    complete_parameter_process_quiet_included_by_actual_reader=True,
)
VIEW = types.ModuleType("_R452_original_R438_held_view")
VIEW.__file__ = str(Path(__file__).resolve())
exec(compile(text, VIEW.__file__ + ":independent-R438-held-view", "exec"), VIEW.__dict__)
ORIGINAL_PERSIST = VIEW.Procedure.persist
ORIGINAL_READBACK = VIEW.build_readback


def persist(self):
    self.report["original_R438_held_source_view"] = VIEW_IDENTITY
    ORIGINAL_PERSIST(self)


def build_readback(args):
    value = ORIGINAL_READBACK(args)
    value["original_R438_held_source_view"] = VIEW_IDENTITY
    return value


VIEW.Procedure.persist = persist
VIEW.build_readback = build_readback
main = VIEW.main
if __name__ == "__main__":
    raise SystemExit(main())
