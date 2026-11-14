"""Explicit complete-field dispatch for the existing R124 body consumer.

This adapter does not define new curvature fields. It reuses the frozen
independent-tail native reader and its actual saved P1 mesh. The body-only
``physical`` entry requests its existing angular two-jet interface, so an
exact cut query never asks for an unclaimed radial II derivative.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import time
import numpy as np
from fd2d_gc_archive_arrays import load_npz
from fd2d_gc_raw_native_field import identity, locate_bound
from fd2d_balanced_curvature_core import FixedBalancedGeometry
from fd2d_gc_independent_tail_native_field import (
    IndependentTailPositiveTraceNativeField, SCHEMA as INDEPENDENT_SCHEMA)

HERE = Path(__file__).resolve().parent
BODY_VIEW_SCHEMA = 'fd2d-complete-native-angular-body-view-v1'


def _atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError('Use a fresh explicit binding output: '+str(path))
    temporary = path.with_name(path.name+'.tmp-'+str(os.getpid()))
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    os.replace(temporary, path)


def _array_identity(value):
    value = np.asarray(value)
    return dict(shape=list(value.shape), dtype=value.dtype.str,
        c_order_bytes_sha256=hashlib.sha256(value.tobytes(order='C')).hexdigest())


class ActualBodyAngularView:
    """Body-only view; full radial/native queries remain on ``native``.

    The generic body screen only consumes J,a,l,m, their angular two-jets,
    and complete n/m/l values at the cut. This route changes no function
    or material coordinate. It does not extend the radial cut contract.
    """
    def __init__(self, native):
        if not isinstance(native, IndependentTailPositiveTraceNativeField):
            raise TypeError('Require the explicit independent-tail complete native reader')
        self.native = native

    def __getattr__(self, name):
        return getattr(self.native, name)

    def physical(self, x, u, *, side='right'):
        return self.native.physical_angular(x, u, side=side)

    def definition(self):
        # Keep the exact already-supported native schema reloadable. The
        # adapter contract is a separate packet, never a replacement field.
        return self.native.definition()

    def body_adapter_definition(self):
        n = self.native
        return dict(schema=BODY_VIEW_SCHEMA, source=identity(__file__),
            native_class=type(n).__module__+'.'+type(n).__name__,
            native_schema=INDEPENDENT_SCHEMA,
            input_field=identity(n.arrays_path), candidate=identity(n.candidate_path),
            mode_count=n.K, node_count=len(n.nodes),
            central_parameter_count=n.central_parameter_count,
            tail_parameter_count=n.tail_parameter_count, profile_count=n.profile_count,
            parameter_layout=n.explicit_parameter_layout,
            actual_arrays={key:_array_identity(value) for key,value in
                (('mesh',n.nodes),('corrections',n.values),('parameters',n.parameters))},
            body_physical_dispatch='native.physical_angular(x,u,side=side)',
            native_radial_cut_contract_extended=False,
            actual_saved_mesh_retained=True, field_or_metric_changed=False,
            full_coast_and_terminal_maps_retained=True,
            mesh_or_parameter_dimension_inferred_from_legacy_K_plus_one=False,
            auxiliary_n_substituted_into_actual_X_uu=False,
            geometry_sources=[identity(HERE/name) for name in (
                'fd2d_gc_raw_native_field.py','fd2d-metric-raw-body-screen.py')],
            body_ODE_run_by_factory=False, geometry_certificate=False)


def load_actual_body_reader(native_definition):
    """Load exactly the named current native schema, including source SHA checks."""
    path = Path(native_definition)
    meta = json.loads(path.read_text())
    if meta.get('schema') != INDEPENDENT_SCHEMA:
        raise ValueError('No inferred legacy dispatch: require the explicit independent-tail native definition')
    return ActualBodyAngularView(IndependentTailPositiveTraceNativeField.from_definition(path))


def bind_saved_body_reader(field, *, foundation_definition):
    """Bind another saved current field to explicitly identified fixed inputs.

    Only the candidate, fixed central packets, reference inlet/cache and
    source identities come from the foundation. Every mesh, coefficient,
    count, window, atlas and nonlinear representation packet comes from
    the selected field itself and is checked by the frozen native reader.
    A previous field's geometry conclusion is never transferred.
    """
    path = Path(foundation_definition)
    meta = json.loads(path.read_text())
    if meta.get('schema') != INDEPENDENT_SCHEMA:
        raise ValueError('The foundation must be an explicit independent-tail native definition')
    for row in meta['sources']:
        locate_bound(path, row)
    geometry = FixedBalancedGeometry(moments=locate_bound(path,meta['moments']),
        means=locate_bound(path,meta['means']))
    cache = meta.get('reference_cache_input')
    native = IndependentTailPositiveTraceNativeField(field,
        locate_bound(path,meta['candidate_input']),
        reference_inlet=locate_bound(path,meta['reference_inlet_input']),
        reference_cache=None if cache is None else locate_bound(path,cache),
        collar_guard=float(meta['collar_guard']), geometry=geometry)
    return ActualBodyAngularView(native)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--foundation-definition', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args = ap.parse_args()
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'*')):
        raise FileExistsError('Use a fresh binding-only diagnostic prefix')
    started = time.monotonic()
    reader = bind_saved_body_reader(args.field, foundation_definition=args.foundation_definition)
    definition_path = Path(str(args.out_prefix)+'-definition.json')
    adapter_path = Path(str(args.out_prefix)+'-adapter.json')
    _atomic_json(definition_path, reader.definition())
    _atomic_json(adapter_path, reader.body_adapter_definition())
    # This is a definition/transport check only, with no field sample,
    # native-jet comparison, body solve, residual, Jacobian or BVP.
    reloaded = load_actual_body_reader(definition_path)
    saved = load_npz(args.field)
    arrays = {}
    for key, attribute in (('mesh','nodes'),('corrections','values'),('parameters','parameters')):
        old, first, second = saved[key], getattr(reader,attribute), getattr(reloaded,attribute)
        same = all(v.dtype == old.dtype and v.shape == old.shape
            and v.tobytes(order='C') == old.tobytes(order='C') for v in (first,second))
        arrays[key] = dict(**_array_identity(old), bind_and_reload_bytewise_equal=same)
        if not same:
            raise AssertionError('The native binding changed actual defining bytes: '+key)
    packets = {}
    for key in ('nested_angular_definition','angular_atlas_definition',
                'coast_reference_definition','gauss_l_definition',
                'positive_trace_definition','seed_weight_definition','atlas_mesh_definition'):
        original = json.loads(str(saved[key]))
        packets[key] = original == getattr(reader.native,key) == getattr(reloaded.native,key)
        if not packets[key]:
            raise AssertionError('The native binding changed a saved definition: '+key)
    report = dict(schema='fd2d-actual-body-reader-binding-only-check-v1',
        source=identity(__file__), input_field=identity(args.field),
        foundation_definition=identity(args.foundation_definition),
        native_definition=identity(definition_path), adapter_definition=identity(adapter_path),
        mode_count=reader.K, node_count=len(reader.nodes),
        central_parameter_count=reader.central_parameter_count,
        tail_parameter_count=reader.tail_parameter_count,profile_count=reader.profile_count,
        parameter_layout=reader.explicit_parameter_layout,
        actual_arrays=arrays, saved_definition_packets_unchanged=packets,
        full_coast_inactive_l_nodes=reader.gauss_l_definition['inactive_l_raw_nodes'],
        terminal_inactive_trace_nodes=reader.positive_trace_definition['inactive_raw_trace_nodes'],
        trace_gauge_pair_count=len(reader.trace_gauge_pairs),
        checked_future_131_node_entity=False,
        future_mesh_rule='Same explicit reader consumes the saved actual mesh and validates all whole-hat packets; no fixed node count',
        field_evaluation_calls=0, native_jet_comparison_repeated=False,
        body_ODE_runs=0, residual_or_Jacobian_calls=0, BVP_runs=0,
        continuous_geometry_certificate=False, passed=True,
        seconds=time.monotonic()-started)
    report_path = Path(str(args.out_prefix)+'-report.json')
    _atomic_json(report_path, report)
    print(json.dumps(dict(report=str(report_path), passed=True,
        nodes=reader.nodes.size, modes=reader.K, parameter_count=reader.parameter_count,
        body_ODE_runs=0, seconds=report['seconds'])),flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
