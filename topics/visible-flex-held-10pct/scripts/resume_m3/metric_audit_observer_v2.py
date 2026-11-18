#!/usr/bin/env python3
"""Observe the original metric audit with whole-module code identity (v2).

The loaded audit is compared with its code object compiled from the complete
SHA-bound original module. Python can emit equivalent but different method
call instructions for an isolated function snippet, so that snippet is not
a valid bytecode identity baseline. No original module is executed here.

Derive only the frozen audit function, retaining its single original metric
FFT and sum in temporary variables, then observing those existing arrays.
All old equations, samples, original result scalars and gates are unchanged.
The three component maxima, radial locations and dominant FFT bins are small
diagnostics, not a continuous bound or a new acceptance gate. Observation
errors are recorded without replacing the original audit result.

Preparation reads source text/AST only. install() belongs in a future owned
runner after its real adaptive module has been loaded. The caller must bind
this source in its launch plan; never patch a source used by an active run,
or rerun an old audit merely to obtain these additional observations.
"""
import argparse
import ast
import datetime
import hashlib
import json
from pathlib import Path
import types

ORIGINAL_SHA = '958a9e2e428f8d64dfc786bed515bad77a208433fa16af7cbbe6f03b1bcc7ebe'
COMPONENTS = ('E_minus_1', 'F_over_a', 'G_over_a_squared_minus_1')
OLD_LINE = "        out['metric_l1']=max(out['metric_l1'],float(np.max(np.sum(abs(np.fft.fft(errors,axis=1)/N),axis=1))));out['flow_defect']=max(out['flow_defect'],float(np.linalg.norm(Fs-fr['Vnormal'],axis=2).max()))"
NEW_LINE = """        metric_fft=np.fft.fft(errors,axis=1)/N
        metric_rows=np.sum(abs(metric_fft),axis=1)
        out['metric_l1']=max(out['metric_l1'],float(np.max(metric_rows)));out['flow_defect']=max(out['flow_defect'],float(np.linalg.norm(Fs-fr['Vnormal'],axis=2).max()))
        metric_observer.observe(s,first,errors,metric_fft,metric_rows,N)"""


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def derive(source):
    source = Path(source).resolve()
    if sha(source) != ORIGINAL_SHA:
        raise ValueError('The frozen original metric audit source changed')
    text = source.read_text()
    tree = ast.parse(text, filename=str(source))
    matches = [node for node in tree.body
               if isinstance(node, ast.FunctionDef) and node.name == 'audit']
    if len(matches) != 1:
        raise ValueError('Require the one original audit function')
    original = ast.get_source_segment(text, matches[0])
    patches = [
        ('    for first in range(0,len(ss),32):',
         '    metric_observer=__original_metric_observer_factory()\n    for first in range(0,len(ss),32):'),
        (OLD_LINE, NEW_LINE),
        ('    return out', "    out['metric_observation']=metric_observer.finish(out,N)\n    return out"),
    ]
    derived = original
    for before, after in patches:
        if derived.count(before) != 1:
            raise ValueError('The declared original audit anchor is not unique')
        derived = derived.replace(before, after, 1)
    restored = derived
    for before, after in reversed(patches):
        if restored.count(after) != 1:
            raise ValueError('The declared observer reverse anchor is not unique')
        restored = restored.replace(after, before, 1)
    if restored != original:
        raise ValueError('The observed audit changed beyond its declared blocks')
    ast.parse(derived, filename=str(Path(__file__).resolve())+'::observed_audit')
    details = dict(original_source=ref(source), observer_source=ref(__file__),
        original_function_sha256=hashlib.sha256(original.encode()).hexdigest(),
        derived_function_sha256=hashlib.sha256(derived.encode()).hexdigest(),
        literal_transforms=[dict(before=a, after=b) for a, b in patches],
        exact_reverse_transforms=True, old_metric_fft_calls=1, new_metric_fft_calls=1,
        original_metric_arithmetic_order='fft(errors,axis=1), divide by N, abs, sum axis1, max, float, max with previous scalar',
        additional_model_or_equation_evaluations=0, acceptance_gates_changed=False)
    return original, derived, details


class MetricObserver:
    def __init__(self):
        self.rows = [None, None, None]
        self.errors = []
        self.observed_radial_samples = 0

    def observe(self, s, first, errors, transformed, sums, N):
        # Observe only already-created arrays; never write through their views.
        # A diagnostic failure must not add a mathematical stopping condition.
        try:
            import numpy as np
            self.observed_radial_samples += len(s)
            if not np.all(np.isfinite(sums)) or not np.all(np.isfinite(transformed)):
                self.errors.append('A nonfinite existing metric array was observed')
                return
            for component, label in enumerate(COMPONENTS):
                radial = int(np.argmax(sums[:, component]))
                value = float(sums[radial, component])
                old = self.rows[component]
                if old is not None and not value > old['metric_l1']:
                    continue
                amplitude = np.abs(transformed[radial, :, component])
                index = int(np.argmax(amplitude))
                point = int(np.argmax(np.abs(errors[radial, :, component])))
                signed = index if index <= N // 2 else index - N
                self.rows[component] = dict(component=label, metric_l1=value,
                    radial_sample_index=int(first + radial), s=float(s[radial]),
                    dominant_signed_fft_bin=int(signed),
                    dominant_absolute_fft_bin=int(abs(signed)),
                    dominant_fft_coefficient_abs=float(amplitude[index]),
                    pointwise_max_abs=float(abs(errors[radial, point, component])),
                    pointwise_max_psi_index=point,
                    pointwise_max_signed_value=float(errors[radial, point, component]))
        except Exception as error:
            self.errors.append(type(error).__name__+': '+str(error))

    def finish(self, original, N):
        values = [row for row in self.rows if row is not None]
        worst = max(values, key=lambda row: row['metric_l1']) if values else None
        return dict(scope='Additional observations from the original single metric FFT; all prior scalar outputs retain their original arithmetic. No additional model/flow/integral/FFT or acceptance threshold.',
            components=self.rows, worst=worst,
            observed_radial_samples=self.observed_radial_samples, angular_samples=int(N),
            worst_matches_original_metric=(worst is not None and worst['metric_l1'] == original['metric_l1']),
            diagnostic_errors=self.errors,
            frequency_scope='Signed bin of the original uniformly sampled audit psi grid; not a physical high-mode remainder, continuous-angle bound or error-source proof.',
            tie_rule='First original radial sample and first FFT bin at an exactly tied maximum.',
            original_gate_unchanged=True)


def install(adaptive_module):
    """Install solely on the supplied newly loaded module in this process."""
    current = adaptive_module.audit
    if getattr(current, '_original_metric_observer_installed', False):
        raise ValueError('The observation is already installed in this module')
    source = Path(adaptive_module.__file__).resolve()
    original, derived, details = derive(source)
    if not isinstance(current, types.FunctionType):
        raise ValueError('The original audit function was replaced')
    space = dict(current.__globals__)
    baseline = dict(space)
    exec(compile(original, str(source)+'::original_audit_identity', 'exec'), baseline)
    expected = baseline['audit']
    whole_module_code = compile(source.read_text(), str(source), 'exec')
    candidates = [value for value in whole_module_code.co_consts
                  if isinstance(value, types.CodeType) and value.co_name == 'audit']
    if len(candidates) != 1:
        raise ValueError('Require one original audit code object in the complete module')
    expected_code = candidates[0]
    for name in ('co_code', 'co_consts', 'co_names', 'co_varnames', 'co_freevars', 'co_cellvars'):
        if getattr(current.__code__, name) != getattr(expected_code, name):
            raise ValueError('The loaded original audit differs from the bound source')
    if current.__defaults__ != expected.__defaults__ or current.__kwdefaults__ != expected.__kwdefaults__:
        raise ValueError('The original audit defaults changed')
    space['__original_metric_observer_factory'] = MetricObserver
    exec(compile(derived, str(Path(__file__).resolve())+'::observed_audit', 'exec'), space)
    result = space['audit']
    result._original_metric_observer_installed = True
    details['loaded_identity_baseline'] = 'Compile the complete SHA-bound original module; select its unique audit CodeType without executing the module'
    result._original_metric_observer_provenance = details
    adaptive_module.audit = result
    return details


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--record', type=Path, required=True)
    args = parser.parse_args()
    _, _, details = derive(args.source)
    record = dict(scope=__doc__, utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        preparation=details, model_imports=0, model_instances=0, mathematical_calls=0,
        source_and_AST_only=True, actual_audit_execution=False)
    with args.record.open('x') as stream:
        json.dump(record, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(record=ref(args.record), source=ref(__file__), source_and_AST_only=True)), flush=True)


if __name__ == '__main__':
    main()
