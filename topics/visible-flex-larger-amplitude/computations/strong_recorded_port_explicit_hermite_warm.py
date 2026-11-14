"""Select a verified unaccepted Hermite input only for the first matching live H.

The original recorded audited packet/ready and all numerical sources remain
unchanged. This subclass changes only the first live constructor's input path,
and only when the complete requested H has the exact bits of the declared
warm input. Original solve/cache/audit behavior handles every result. A later
return to the same H cannot reset the last completed checkpoint. Selection and
actual constructor delivery are reported separately; neither is acceptance.
"""
from __future__ import annotations

import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
IO = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}
GENERATOR = 'strong_full_flow_hermite_warm_v3.py'
GENERATOR_SHA = 'f60cba658e06d364b4dd5b894bd3ec97ab8877cf7b76fe4be771b2f8e62138da'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    p = Path(path)
    data = p.read_bytes()
    return json.loads(gzip.decompress(data) if p.suffix == '.gz' else data)


def equations(value):
    return {key: item for key, item in value.items() if key not in IO}


def verified_warm(warm_file, report_file, primary_file, packet_file):
    """Check the frozen generator's full provenance, never certify its new state."""
    paths = list(map(Path, (warm_file, report_file, primary_file, packet_file)))
    warm_file, report_file, primary_file, packet_file = paths
    warm, report, primary, packet = map(read, paths)
    checks = {}

    def check(name, condition):
        if not condition:
            raise ValueError('Explicit first-live warm identity failed: '+name)
        checks[name] = True

    check('frozen_generator_source', sha(HERE/GENERATOR) == GENERATOR_SHA)
    check('reported_warm_only_and_applicable',
          report.get('schema') == 'full-flow-hermite-warm-input-v1'
          and report.get('applicable') is True and report.get('output_written') is True
          and report.get('new_target_accepted') is False
          and report.get('no_response_or_flow_snapshot_fabricated') is True
          and report.get('ODE_Node_Newton_residual_calls') == 0
          and report.get('all_MJS_unchanged') is True)
    check('all_generator_checks_passed', bool(report.get('checks')) and all(v is True for v in report['checks'].values()))
    check('warm_output_hash', report['output']['sha256'] == sha(warm_file)
          and report['output']['bytes'] == warm_file.stat().st_size)
    check('warm_never_claims_response_or_acceptance',
          warm.get('status') == 'cubic-hermite-full-flow-warm-only'
          and warm.get('new_target_accepted') is False and 'response' not in warm)
    for key in ('source_sha256', 'input_sha256'):
        check(key+'_same_in_report_and_warm', report[key] == warm['provenance'][key])
        for name, expected in report[key].items():
            check(key+':'+name, Path(name).is_file() and sha(name) == expected)
    check('generator_is_explicitly_bound',
          report['source_sha256'].get(str((HERE/GENERATOR).resolve())) == GENERATOR_SHA)
    command = report['command']
    for key, path in (('--current-primary', primary_file), ('--current-packet', packet_file)):
        check('one_recorded_'+key, command.count(key) == 1)
        bound = Path(command[command.index(key)+1])
        check('current_identity_'+key, bound.resolve() == path.resolve()
              and report['input_sha256'].get(str(bound)) == sha(path))
    check('current_primary_is_actually_accepted',
          primary.get('solver_success') is True and primary.get('audit_pending') is False)
    check('current_packet_is_genuinely_audited',
          packet['request'].get('audit') is True and packet['request'].get('jacobian') is True
          and packet['response'].get('converged') is True and packet['response'].get('audit') is not None)
    checkpoint, saved = warm['checkpoint'], packet['response']['checkpoint']
    check('all_nonIO_checkpoint_parameters_identical', equations(checkpoint['parameters']) == equations(saved['parameters']))
    modes = int(checkpoint['parameters']['modes'])
    states = np.asarray(checkpoint['states'], dtype=np.float64)
    raw_states = np.asarray(checkpoint['rawStates'], dtype=np.float64)
    saved_states = np.asarray(saved['states'], dtype=np.float64)
    raw_node = np.asarray(checkpoint['rawNode'], dtype=np.float64)
    saved_node = np.asarray(saved['rawNode'], dtype=np.float64)
    height = np.asarray(checkpoint['cutHeight'], dtype=np.float64)
    check('full_states_shape_and_finite', states.shape == saved_states.shape == tuple(report['complete_state_shape'])
          and states.shape[1] == 2*modes and np.all(np.isfinite(states)))
    check('all_rawNode_values_and_order_identical', raw_node.shape == saved_node.shape
          and raw_node.tobytes() == saved_node.tobytes())
    check('rawNode_is_complete_valid_original_index_list', raw_node.ndim == 1
          and np.all(np.isfinite(raw_node)) and np.all(raw_node == np.floor(raw_node))
          and raw_node[0] == 0 and raw_node[-1] == len(states)-1
          and np.all(np.diff(raw_node) > 0))
    check('full_rawStates_match_original_indexed_states_bits',
          raw_states.shape == (len(raw_node), 2*modes)
          and raw_states.tobytes() == states[raw_node.astype(np.int64)].tobytes())
    check('full_height_finite_and_report_bits_identical', height.shape == (modes,)
          and np.all(np.isfinite(height))
          and height.tobytes() == np.asarray(report['complete_height'], np.float64).tobytes())
    check('no_flow_snapshot_for_new_uncertified_state',
          warm['provenance']['no_flow_Jacobian_snapshot_assigned_to_this_unaccepted_state'] is True
          and 'fullTangentSnapshot' not in checkpoint)
    record = dict(scope=__doc__, source_file=str(Path(__file__).resolve()), source_sha256=sha(__file__),
        warm_file=str(warm_file.resolve()), warm_sha256=sha(warm_file),
        report_file=str(report_file.resolve()), report_sha256=sha(report_file),
        primary_file=str(primary_file.resolve()), primary_sha256=sha(primary_file),
        initial_audited_packet=str(packet_file.resolve()), initial_audited_packet_sha256=sha(packet_file),
        complete_state_shape=list(states.shape), complete_raw_state_shape=list(raw_states.shape),
        full_raw_node_count=len(raw_node),
        complete_height=height.tolist(), applicability=report['applicability'],
        all_identity_checks=checks, same_target_only=True, first_live_only=True,
        new_target_accepted=False, numerical_response_or_audit_supplied=False,
        all_original_nonlinear_and_final_acceptance_gates_required=True)
    return record, height


def make_first_warm_port_class(Base, warm_file, report_file, primary_file, packet_file):
    """Wrap the unchanged exact audited port, never its numerical worker."""
    class ExplicitFirstLiveWarm(Base):
        def __init__(self, *args, **kwargs):
            record, height = verified_warm(warm_file, report_file, primary_file, packet_file)
            super().__init__(*args, **kwargs)
            if Path(self._last_checkpoint).resolve() != Path(packet_file).resolve():
                raise ValueError('The original audited initial checkpoint identity changed')
            if self._live is not None:
                raise ValueError('Explicit first warm must be installed before any live worker')
            self._first_warm_record = record
            self._first_warm_height = height
            self._first_live_warm_choice_done = False
            self._first_live_warm_selected = False
            self._first_live_warm_delivered = False
            self.provenance['explicit_unaccepted_first_live_Hermite_warm'] = dict(
                **record, choice_observed=False, selected=False,
                actual_original_constructor_delivery_observed=False)
            self._write_manifest()

        def solve(self, height, jacobian=True, audit=False):
            h = np.asarray(height, dtype=np.float64)
            if (not self._first_live_warm_choice_done
                    and h.shape == (self.M,) and np.all(np.isfinite(h))
                    and not np.array_equal(h, self.saved_height)):
                self._first_live_warm_choice_done = True
                self._first_live_warm_selected = bool(self._live is None
                    and h.tobytes() == self._first_warm_height.tobytes())
                entry = self.provenance['explicit_unaccepted_first_live_Hermite_warm']
                entry.update(choice_observed=True, selected=self._first_live_warm_selected,
                    complete_request_height=h.tolist(), no_live_worker_before_choice=self._live is None,
                    reason=('complete_H_bits_match_before_first_live' if self._first_live_warm_selected
                            else 'complete_H_bits_differ_or_live_worker_already_exists_original_warm_retained'))
                if self._first_live_warm_selected:
                    entry['original_last_checkpoint'] = str(self._last_checkpoint)
                    entry['original_last_checkpoint_sha256'] = sha(self._last_checkpoint)
                    self._last_checkpoint = Path(self._first_warm_record['warm_file'])
                self._write_manifest()
                self._event(kind='explicit-first-live-warm-choice',
                    selected=self._first_live_warm_selected,
                    delivered_to_original_constructor=False,
                    unaccepted_initial_guess_only=True)
            return super().solve(height, jacobian=jacobian, audit=audit)

        def _ensure_live(self):
            newly_created = self._live is None
            super()._ensure_live()
            if (newly_created and self._first_live_warm_selected
                    and not self._first_live_warm_delivered):
                live = self.provenance['live_configurations'][-1]
                cfg = read(live['file'])
                expected = Path(self._first_warm_record['warm_file'])
                if (Path(cfg['initialCheckpoint']).resolve() != expected.resolve()
                        or Path(live['warm']).resolve() != expected.resolve()
                        or live['warm_sha256'] != self._first_warm_record['warm_sha256']
                        or sha(expected) != self._first_warm_record['warm_sha256']):
                    raise ValueError('The actual original live constructor did not receive the selected complete warm')
                self._first_live_warm_delivered = True
                entry = self.provenance['explicit_unaccepted_first_live_Hermite_warm']
                entry.update(actual_original_constructor_delivery_observed=True,
                    actual_live_configuration=live, original_live_constructor_returned=True,
                    original_worker_residual_and_full_acceptance_still_required=True)
                self._write_manifest()
                self._event(kind='explicit-first-live-warm-constructor-receipt',
                    initialCheckpoint=str(expected), sha256=sha(expected),
                    unaccepted_initial_guess_only=True,
                    no_claim_of_worker_convergence_or_audit=True)

    return ExplicitFirstLiveWarm
