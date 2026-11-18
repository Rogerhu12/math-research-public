#!/usr/bin/env python3
"""Derive explicit lambda=1 interfaces without modifying frozen partial readers.

Read the four frozen source texts, apply only the declared endpoint dispatch,
dependency and scope changes, parse the resulting Python ASTs, and write new
owned files. Do not import a numerical model, bind a synthetic checkpoint,
construct a core, evaluate a Jacobian/flow, or run any solver.

The production checkpoint kind string still contains 'partial_lift'. This
historical schema label is preserved, while exact lambda=1, strength=1 and
the actual literal_R44_endpoint branch provide the explicit dispatch. The
original PathEnvironment, M8 physical controls/scales/base+p0, native gates,
full lift and its parameter derivatives are not changed.
"""
import argparse
import ast
import datetime
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PARENTS = {
    'm3_trace_path_prefix.py': '5a918498f3f91fb173c60ada1983f8cb89e64083e36c6ab55f3913ec7c55bd3a',
    'm3_trace_path_pending_inner.py': '203fb3c82d7377794b089b6acf79017b1c984036be0ea2451f995405cedba3f0',
    'resume_m3_trace_path_pending_v2.py': 'aa146dd6a68cbc22ee89ab684a6ef30d5a67dac44bff8b97613dd3aa845f29ae',
    'finish_m3_trace_path_saved_audit.py': 'fff945cb062369b2f821bee39c76b2c4cb74ffcef9e1dd237dfe9315340b115c',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def derive(parent, name, description, replacements):
    source = HERE/parent
    if sha(source) != PARENTS[parent]:
        raise ValueError('Frozen partial interface changed: '+parent)
    original = source.read_text()
    text = original
    start = text.index('"""')
    stop = text.index('"""', start+3)+3
    patches = [(text[start:stop], '"""'+description+'\n"""'), *replacements]
    for before, after in patches:
        if text.count(before) != 1:
            raise ValueError('A declared endpoint source anchor is not unique: '+before[:90])
        text = text.replace(before, after, 1)
    restored = text
    for before, after in reversed(patches):
        if restored.count(after) != 1:
            raise ValueError('A declared endpoint reverse anchor is not unique')
        restored = restored.replace(after, before, 1)
    if restored != original:
        raise ValueError('A source changed beyond its explicit endpoint transforms')
    ast.parse(text, filename=str(HERE/name))
    return dict(parent=ref(source), output_name=name, text=text,
        syntax_only=True, literal_transforms=[dict(before=a, after=b) for a, b in patches],
        exact_parent_recovered_by_reverse_transforms=True)


def sources():
    endpoint = derive('m3_trace_path_prefix.py', 'm3_trace_path_endpoint.py',
        '''Explicit completed M8 lambda=1 reader for the literal R44 endpoint.

The historical wire kind contains partial_lift; it is not used to guess the
mathematics. This reader requires exact lambda=1/strength=1 and the actual
literal_R44_endpoint branch. The original PathEnvironment uses the existing
R44 seven-control core and complete integral lift at this endpoint. Its full
physical p, fixed gauge/scales/warp, base+p0 and saved quintic are retained.

Binding is metadata-only. Native construction uses the unchanged source
factory; position() explicitly runs the original mean primitive if called.
The defining inlet is Gamma, while numerical inversion/quadrature and whole
metric/geometry certification remain separate. No completed endpoint is
invented; a real accepted prefix/audit/tail is required.''', [
        ("not 0. < design['lambda_value'] < 1.", "design['lambda_value'] != 1."),
        ("raise ValueError('This reader is solely the positive intermediate M8 path')",
         "raise ValueError('This reader is solely the literal lambda=1 M8 endpoint')"),
        ("if (definition['settings'] != r['core_round_settings'] or",
         "if (definition['branch'] != 'literal_R44_endpoint' or\n            definition['settings'] != r['core_round_settings'] or"),
        ("represented_field='All 25 saved physical quintic components plus the actual partial-lift Flow.geo.',",
         "represented_field='All 25 saved physical quintic components plus the actual lambda=1 full-lift Flow.geo.',\n            endpoint_dispatch=dict(lambda_value=1., branch='literal_R44_endpoint', full_lift_strength=1.,\n                historical_wire_kind=KIND, defining_inlet_is_Gamma=True),"),
        ("exact_circular_inlet_claim=False)",
         "exact_circular_inlet_claim=False,\n            numerical_circle_certificate_scope='The defining R44 inlet is circular on its protected arc; no new bound on its floating evaluation or full surface follows.')"),
    ])
    pending = derive('m3_trace_path_pending_inner.py', 'm3_trace_path_endpoint_inner.py',
        '''Bind a real successful M8 lambda=1 returned inner before its pending tail.

Use explicit raw/sidecar/failure files and the endpoint reader's exact lambda
and literal_R44_endpoint dispatch. Preserve the historical wire kind, all
eight physical parameters, seven controls/scales, base+p0, cubic and full RMS.
Metadata binding evaluates no equations. native_model() restores the actual
full-lift endpoint model but invokes no inner solve, mean, C2 export or DN.''', [
        ('from m3_trace_path_prefix import (KIND, CONTROL_PATH, M3, checked_file,',
         'from m3_trace_path_endpoint import (KIND, CONTROL_PATH, M3, checked_file,'),
        ("if (definition['settings'] != raw['core_round_settings'] or",
         "if (definition['branch'] != 'literal_R44_endpoint' or\n            definition['settings'] != raw['core_round_settings'] or"),
        ("core_settings=r['core_round_settings'], path_definition=r['path_definition'],",
         "core_settings=r['core_round_settings'], path_definition=r['path_definition'],\n            endpoint_dispatch=dict(lambda_value=1., branch='literal_R44_endpoint', full_lift_strength=1.),"),
    ])
    resume = derive('resume_m3_trace_path_pending_v2.py', 'resume_m3_trace_path_endpoint_pending.py',
        '''Resume an actual lambda=1 M8 returned inner with the original outer budget.

Only the explicit endpoint binder/dependency selection differs from the
executed generic partial-path recovery. The endpoint model uses the existing
R44 core and full lift. Retain actual p/scales/base+delta and all seven slots;
reuse a genuine exact-H full response, then follow the original actual BC,
remaining outer indices, five-point domain guard, mean/metric and seam.
No accepted inner or initializer is repeated; unknown H uses the original DN.
The historical checkpoint wire kind is retained and explicitly dispatched.''', [
        ('from m3_trace_path_pending_inner import bind_pending_inner',
         'from m3_trace_path_endpoint_inner import bind_pending_inner'),
        ('from m3_trace_path_prefix import checked_file, exact_numbers',
         'from m3_trace_path_endpoint import checked_file, exact_numbers'),
        ("for file in (Path(__file__).resolve(), HERE/'m3_trace_path_pending_inner.py', CONTINUATION,",
         "for file in (Path(__file__).resolve(), HERE/'m3_trace_path_endpoint_inner.py',\n                 HERE/'m3_trace_path_endpoint.py', CONTINUATION,"),
    ])
    seam = derive('finish_m3_trace_path_saved_audit.py', 'finish_m3_trace_path_endpoint_seam.py',
        '''Complete only a real lambda=1 M8 physical seam after its prefix audit.

Use the explicit literal_R44_endpoint/full-strength reader and the original
saved full p/scales/base+delta and quintic. Rebuild the necessary original
core/inlet once, then call only the unchanged original seam_audit with its
true exact-H accepted response. Retain the earlier prefix audit bit for bit;
no new inner, worker, DN, prefix audit, mean primitive or C2 export is run.
The original cut mean two-jets are evaluated. No endpoint result is invented.''', [
        ('from m3_trace_path_prefix import (CONTROL_PATH, KIND, TracePathBinding,',
         'from m3_trace_path_endpoint import (CONTROL_PATH, KIND, TracePathBinding,'),
        ("definition['settings'] != cp['core_round_settings'] or",
         "definition['branch'] != 'literal_R44_endpoint' or\n            definition['settings'] != cp['core_round_settings'] or"),
        ("HERE/'m3_trace_path_prefix.py',", "HERE/'m3_trace_path_endpoint.py',"),
    ])
    return [endpoint, pending, resume, seam]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path, required=True)
    args = parser.parse_args()
    prepared = sources()
    if args.record.exists() or any((HERE/item['output_name']).exists() for item in prepared):
        raise FileExistsError('Keep existing prepared/executed interfaces unchanged')
    for item in prepared:
        target = HERE/item['output_name']
        with target.open('x') as stream:
            stream.write(item.pop('text'))
        item['derived'] = ref(target)
    record = dict(scope=__doc__, preparer=ref(__file__), command=[sys.executable, *sys.argv],
        utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), interfaces=prepared,
        original_files_unchanged=all(sha(HERE/name) == digest for name, digest in PARENTS.items()),
        model_imports=0, core_constructions=0, synthetic_checkpoint_bindings=0,
        equation_evaluations=0, BVP_calls=0, DN_calls=0,
        endpoint_acceptance_claim=False, numerical_source_or_gate_changes=False)
    with args.record.open('x') as stream:
        json.dump(record, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(record=ref(args.record), derived=[item['derived'] for item in prepared],
                         syntax_only=True, new_mathematical_executions=0)), flush=True)


if __name__ == '__main__':
    main()
