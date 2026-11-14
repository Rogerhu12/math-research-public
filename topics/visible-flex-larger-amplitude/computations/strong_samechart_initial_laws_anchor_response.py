#!/usr/bin/env python3
"""Original full-J responses with the corrected first-append provider anchor.

General mode preserves the original complete response calculation. Explicit
--only-missing-from instead computes only frontload and vd at the exact old
accepted q122 state, retaining the six successful original columns in their
separate recovery packet. It does not pretend the old half arrays existed.
Every newly evaluated external column keeps the original full/half forcing,
complete matrix solve/backward checks and original 2e-4 external half gate.
Both new half directions and forcing vectors are saved for faithful recovery.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
import strong_initial_laws_disk_control_response as laws
import strong_samechart_initial_laws_response as samechart

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_initial_laws_disk_control_response.py': '42db431d26f8cc87b56f3e8baf38b7afba38816f701d185efd1955028afe9750',
    'strong_samechart_initial_laws_response.py': '2395db1d8cea3e9bba3cc02221bdb59793128357b71ae9f63991675bd7e7a6eb',
    'strong_monotone_initial_speed.py': '12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',
    'strong_monotone_initial_speed_anchor.py': '583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument('--only-missing-from', type=Path)
    p.add_argument('--anchor-source-record', type=Path)
    own, remaining = p.parse_known_args()
    for name, expected in EXPECTED.items():
        if sha(HERE/name) != expected:
            raise ValueError('Frozen response/anchor source differs: '+name)
    missing = None
    if own.only_missing_from:
        partial = json.loads(own.only_missing_from.read_text())
        if (not partial.get('partial_recovery') or not partial.get('finished')
                or partial.get('original_eight_control_job_finished')
                or partial.get('original_eight_control_job_exitcode') != 1
                or not partial.get('all_six_original_external_full_and_half_gates_observed')
                or partial['fields'] != ['delta', 'boost_length', 'boost_speed', 'vu',
                                        'descending_turn_curvature', 'start_acceleration']
                or partial['unavailable_fields'] != ['initial_speed_frontload', 'vd']):
            raise ValueError('Expected the explicit six-completed/two-missing recovery packet')
        for item in partial['tangent_arrays']:
            path = Path(item['file'])
            if sha(path) != item['sha256']:
                raise ValueError('An original or recovered complete direction changed')
        missing = dict(file=str(own.only_missing_from), sha256=sha(own.only_missing_from),
            source_sha256=partial['source_sha256'], baseline=partial['baseline'],
            modes=partial['modes'], angular=partial['angular'], nodes=partial['nodes'],
            original_six_full_and_half_forcings_not_recomputed=True,
            new_fields=['initial_speed_frontload', 'vd'])
        if not own.anchor_source_record:
            for key in ('--response-checkpoint', '--response-raw', '--response-tail'):
                if remaining.count(key) != 1:
                    raise ValueError('Require explicit original same-state '+key)
                path = Path(remaining[remaining.index(key)+1])
                if partial['source_sha256'].get(str(path)) != sha(path):
                    raise ValueError('The missing-column point differs from the completed-six point')
            if '--response-fields' in remaining:
                if remaining[remaining.index('--response-fields')+1] != 'initial_speed_frontload,vd':
                    raise ValueError('Missing-only mode may compute exactly the two missing fields')
            else:
                remaining += ['--response-fields', 'initial_speed_frontload,vd']
    previous = laws.transformed_source

    def transformed():
        source, prior = previous()
        edits = [
            ('                    import strong_monotone_initial_speed as frontload_hook\n',
             '                    import strong_monotone_initial_speed_anchor as frontload_hook\n'),
            ("            rows.append(item);arrays.append(save_array('external-'+field,direction))\n",
             "            rows.append(item);arrays.append(save_array('external-'+field,direction))\n"
             "            arrays.append(save_array('external-half-'+field,half))\n"
             "            arrays.append(save_array('forcing-full-'+field,forcings[0]))\n"
             "            arrays.append(save_array('forcing-half-'+field,forcings[1]))\n"),
        ]
        if missing is not None:
            edits.append((
                '    if len(set(fields))!=len(fields) or not set(primary)<=set(fields) or not set(fields)<=allowed:',
                "    if fields!=('initial_speed_frontload','vd') or not set(fields)<=allowed:"))
            start = source.index('        Z=np.column_stack([directions[name] for name in primary])')
            end = source.index("        raise RuntimeError('Actual fixed control response complete; no new BVP or worker requested')", start)
            original_block = source[start:end]
            replacement = '''        result=dict(scope=__doc__,schema='fixed-actual-external-columns-v1',finished=True,
            inspection_only=True,new_solution=False,tail_worker_started=False,
            complete_eight_exchange_not_claimed=True,input_identity=input_report,source_sha256=hashes,
            fields=list(fields),external_responses=rows,physical_core_parameter_scales=parameter_units.tolist(),
            modes=self.M,angular=self.nt,nodes=m,
            baseline=dict(profile=baseline_cfg,core=baseline_core.tolist(),gauge=self.q,
                numerical_reference_knots=self._neck_knots.tolist(),reference_coefficients=self.ref_coeff.tolist(),
                actual_physical_bc_max=physical_bc,accepted_rms_max=float(np.max(solution.rms_residuals)),
                raw_state_bitwise_equal=True),
            tangent_arrays=arrays,all_new_full_half_and_forcing_arrays_saved=True,
            previous_completed_six=DISK_WRAPPER_PROVENANCE['first_append_anchor_response']['missing_only'],
            original_six_external_fields_recomputed=False,full_original_external_half_and_matrix_gates_preserved=True,
            jacobian_seconds=jac_seconds,factor_seconds=factor_seconds,seconds=time.monotonic()-start,
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,counters=counters.copy(),
            radial_batch_size=opts.radial_batch_size,collocation_batch_size=opts.collocation_batch_size,
            disk_block_storage=dict(adapter=DISK_WRAPPER_PROVENANCE,configuration=DISK_WRAPPER_CONFIGURATION,
                stats=dict(disk_runtime.stats),original_full_field_checks_preserved=True,
                numerical_backward_check_is_not_an_interval_inverse_certificate=True),
            limitations=['Only the two original missing external columns are computed here.',
                'The successful six original fields are retained in the linked separate packet.',
                'New combined eight-column warm data must retain the explicit missing-old-half limitation.',
                'All future actual full-H nonlinear BVP and physical audit gates are required.'])
        output.write_text(json.dumps(result,indent=2)+'\\n')
'''
            edits.append((original_block, replacement))
        changed = source
        for before, after in edits:
            if changed.count(before) != 1:
                raise ValueError('Original anchor/retained-response source site is not unique')
            changed = changed.replace(before, after, 1)
        reverse = changed
        for before, after in reversed(edits):
            if reverse.count(after) != 1:
                raise ValueError('Source reverse anchor is not unique')
            reverse = reverse.replace(after, before, 1)
        if reverse != source:
            raise ValueError('An undeclared original response operation changed')
        ast.parse(changed, filename='<original-response-correct-first-append-anchor>')
        import strong_monotone_initial_speed_anchor as anchor
        record = dict(prior)
        record['source_sha256'] = {**prior['source_sha256'],
            str(HERE/'strong_monotone_initial_speed_anchor.py'): EXPECTED['strong_monotone_initial_speed_anchor.py'],
            str(Path(__file__)): sha(__file__)}
        record['prior_transformed_source_sha256'] = prior['transformed_source_sha256']
        record['transformed_source_sha256'] = hashlib.sha256(changed.encode()).hexdigest()
        record['explicit_transforms'] = list(prior['explicit_transforms'])+[
            dict(before=a, after=b, replacements=1) for a, b in edits]
        record['first_append_anchor_response'] = dict(scope=__doc__,
            provider_source_identity=anchor.source_identity(), missing_only=missing,
            original_complete_raw_H_tail_J_identity_preserved=True,
            original_full_field_and_external_half_step_gates_preserved=True,
            additional_half_and_forcing_storage_only=True,
            exact_reverse_recovers_original_initial_laws_response=True)
        return changed, record

    if own.anchor_source_record:
        source, record = transformed()
        with own.anchor_source_record.open('x') as stream:
            json.dump(dict(prepared=True, actual_response_executed=False, source_bytes=len(source.encode()),
                provenance=record), stream, indent=2, allow_nan=False)
            stream.write('\n')
        print(json.dumps(dict(prepared=True, actual_response_executed=False,
            transformed_source_sha256=record['transformed_source_sha256'])))
        return
    old_argv = sys.argv
    laws.transformed_source = transformed
    sys.argv = [old_argv[0], *remaining]
    try:
        samechart.main()
    finally:
        laws.transformed_source = previous
        sys.argv = old_argv


if __name__ == '__main__':
    main()
