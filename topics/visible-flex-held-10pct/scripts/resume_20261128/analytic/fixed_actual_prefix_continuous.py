#!/usr/bin/env python3
"""Fresh Cartesian geometry/metric certificates for a real fixed actual-DN return.

Run geometry, tables, metric, cut, or preflight in a fresh process. The source
is accepted under its own fixed-metric KIND before importing geometry from a
preserved original tree. Only source initialization and output provenance
change; the reviewed interval formulas and proof loops are retained. Every
new returned field requires its own complete certificates.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import copy
import hashlib
import importlib
import inspect
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
GEO = HERE.parent/'geometry'
sys.path.insert(0, str(HERE))
import fixed_actual_cartesian_prefix as reader
from fixed_actual_cartesian_prefix import sha, load, ref, model

SCRIPTS, REPO = reader.SCRIPTS, reader.REPO
SOURCE_KIND = reader.SOURCE_KIND
SCHEMA = 'original-support-fixed-actual-DN-Cartesian-continuous-entry-v1'
REVIEWED_BASE_SHA256 = {
    'cartesian_prefix_interval_geometry.py': '1e4554834e66dc72a8942bc9a844225704d478a07e248084aa4531ef891990dc',
    'cartesian_prefix_metric_tables.py': 'ab8c9fb208cfa984c80768144545c9e558682eefa23169364eed9cb7986b82ba',
    'cartesian_prefix_metric.py': '935dc0ec201161396e11d25ace0de29e456e2c713618b1469cb78d1cea004ab3',
    'cartesian_prefix_cut_metric.py': 'a5b8f4f821f6b284cb124d8f2c90d471271b91f16218c8ff6157f93d609892a7',
    'cartesian_prefix_metric_target.py': 'a8bb9135d8ad56a0589db3c5d582a91cc85a8c4b1fd5a5632264cccf53d7ca77',
    'cartesian_prefix_curvature_rounding.py': 'e094c1440e487fdd72137e7e20519b98c43addd4a6d5ead82e05fda88f3dbed5',
}


def write(path, value):
    temporary = Path(str(path)+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


class FixedActualContext:
    def __init__(self, phase):
        self.phase, self.payload, self.execution = phase, None, None
        self.adapter_sources = {**reader.reader_sources(), str(Path(__file__).resolve()):sha(__file__)}

    def capture(self, run, record, view, provenance):
        run = Path(run).resolve()
        physical = ref(run.parent/'physical.npz')
        if physical != view['physical'] or provenance['model_kind'] != model.KIND:
            raise ValueError('The current fixed physical field/model identity changed')
        payload = dict(source_kind=SOURCE_KIND, source_model_kind=model.KIND,
            actual_fixed_source_verified=True, fixed_metric=True,
            source_run=str(run), source_run_sha256=sha(run),
            physical_file=physical, physical_sha256=physical['sha256'],
            fixed_problem=copy.deepcopy(record['fixed_problem']),
            frozen_complete_metric=copy.deepcopy(record['frozen_profile']),
            parameter_zero_meaning=model.PARAMETER_ZERO,
            source_mean_nodes=record['mean_nodes'], source_mean_gauss_order=6,
            full_height_binding=view['height_reference'], full_height_packet=view['packet'],
            full_height_definition=provenance['full_height_definition'],
            full_height_binary_sha256=provenance['full_height_binary_sha256'],
            raw_candidate_used_as_final_height=False,
            final_height_bitwise_equal_raw_candidate=provenance['raw_height_bitwise_equal'],
            original_anchor_coupling_summary=provenance['original_anchor_coupling_summary'],
            actual_fixed_gate_provenance=copy.deepcopy(provenance))
        if self.payload is not None and payload != self.payload:
            raise ValueError('One verifier attempted to mix two actual fixed fields or metrics')
        self.payload = payload
        return payload

    def accept(self, run):
        record, physical, view, provenance = reader.accepted_fixed(run)
        self.capture(run, record, view, provenance)
        return record, physical, view, provenance

    def load_prefix(self, run):
        record, prefix, view, provenance = reader.load_fixed_prefix(run)
        self.capture(run, record, view, provenance)
        return record, prefix

    def physical_sha(self):
        if self.payload is None or ref(self.payload['physical_file']['path']) != self.payload['physical_file']:
            raise ValueError('The bound actual fixed physical field changed')
        return self.payload['physical_sha256']

    def require_report(self, report):
        if self.payload is None or report.get('fixed_actual_adapter_schema') != SCHEMA:
            raise ValueError('Require a fresh report for this own fixed actual-DN field')
        for key, value in self.payload.items():
            if report.get(key) != value:
                raise ValueError('The report belongs to a different fixed field/target: '+key)
        if report.get('fixed_actual_adapter_sources') != self.adapter_sources:
            raise ValueError('The report does not bind this explicit fixed-source entry')
        for path, digest in self.adapter_sources.items():
            if sha(path) != digest:
                raise ValueError('A fixed-source adapter changed: '+path)

    def save(self, path, value):
        record = dict(value)
        if 'source_sha256' in record:
            record['reused_main_source_sha256'] = record['source_sha256']
        record['source_sha256'] = sha(__file__)
        record.update(fixed_actual_adapter_schema=SCHEMA, fixed_actual_phase=self.phase,
            fixed_actual_adapter_sources=dict(self.adapter_sources),
            fixed_actual_execution_adapter=self.execution,
            requested_source_kind=SOURCE_KIND, source_record_relabelled_or_rewritten=False,
            accepted_original_replaced=False, old_other_field_bounds_reused=False)
        sources = dict(record.get('source_hashes', {}))
        sources.update(self.adapter_sources)
        if self.payload is not None:
            if sha(self.payload['source_run']) != self.payload['source_run_sha256']:
                raise ValueError('The genuine accepted fixed run changed during verification')
            self.physical_sha()
            record.update(self.payload)
            sources.update(self.payload['actual_fixed_gate_provenance']['actual_geometry_provider_sources'])
        else:
            record.update(actual_fixed_source_verified=False, source_kind=None)
        record['source_hashes'] = sources
        write(path, record)


def proof_modules(context):
    if context.payload is None:
        raise ValueError('Acceptance must precede geometry imports across frozen source trees')
    for name, digest in REVIEWED_BASE_SHA256.items():
        if sha(GEO/name) != digest:
            raise ValueError('The reviewed interval algebra changed: '+name)
    sys.path[:0] = [str(GEO), str(HERE.parent/'tail'), str(SCRIPTS/'resume_20261126')]
    result = {}
    for phase, name in (('geometry','cartesian_prefix_interval_geometry'),
                        ('tables','cartesian_prefix_metric_tables'),
                        ('metric','cartesian_prefix_metric'),('cut','cartesian_prefix_cut_metric')):
        value = importlib.import_module(name)
        if Path(value.__file__).resolve() != GEO/(name+'.py'):
            raise ValueError('Use a fresh process; an interval module belongs to another source tree')
        result[phase] = value
    return result


def metric_classes(bases):
    metric, cut = bases['metric'], bases['cut']

    class FixedActualNewMetric(metric.NewMetric):
        def __init__(self, report_path, context):
            self.context, self.report_path = context, Path(report_path).resolve()
            self.record = r = load(self.report_path)
            if (r.get('status') != 'complete_angular_three_jet_interval_tables'
                    or r.get('right_sector_endpoint_gram_equals_left_exactly') is not True):
                raise ValueError('Require this fixed field\'s complete fresh angular tables')
            for path, digest in r['source_hashes'].items():
                if sha(path) != digest:
                    raise ValueError('A bound angular construction source changed: '+path)
            for name in ('defining_jets', 'angular_tables'):
                reader.checked(r[name])
            run = Path(r['source_run'])
            if sha(run) != r['source_run_sha256']:
                raise ValueError('The actual fixed source run changed')
            source, physical, view, provenance = context.accept(run)
            context.require_report(r)
            self.fixed_source_record, self.fixed_height_view = source, view
            self.fixed_provenance = provenance
            obj = model.load_model(dict(source_run=str(run.resolve()), repo=str(REPO)))
            obj.initial(physical.p)
            self.target = metric.FrozenTarget(obj.flow(physical.p[0]), source)
            with np.load(r['defining_jets']['path'], allow_pickle=False) as data:
                self.knots = data['knots'].copy()
                self.P = len(data['planar_modes'])
                self.field = metric.HermiteIntervals(self.knots, data['jets'])
                self.lift = metric.HermiteIntervals(self.knots, data['lift_jets'])
                self.chart = metric.HermiteIntervals(self.knots, data['chart_jets'])
                self.width = metric.fq(data['center_width'])
                self.pm, self.hm = data['planar_modes'].copy(), data['height_modes'].copy()
            if (metric.fq(self.knots[0]) != 0 or metric.fq(self.knots[-1]) != self.target.end
                    or np.any(self.pm % 3 != 1) or np.any(self.hm % 3 != 0)):
                raise ValueError('The complete fixed map and frozen target domains differ')
            with np.load(r['angular_tables']['path'], allow_pickle=False) as data:
                self.tables = {name:metric.pair(data[name].copy()) for name in data.files}
            self.N = int(r['angular_boxes_per_sector'])
            if self.tables['point_lift_0'].x[0].shape != (self.N,3):
                raise ValueError('Missing complete actual angular table columns')
            self.grid = sorted(set(self.field.x+self.target.grid+[self.width]))

    class FixedActualCutMetric(cut.CutMetric, FixedActualNewMetric):
        def __init__(self, tables, bundle, outdir, context, width=.04):
            FixedActualNewMetric.__init__(self, tables, context)
            self.cut_width = metric.fq(width)
            self.cut_start = self.target.end-self.cut_width
            if not 0 < self.cut_width or self.cut_start <= self.width:
                raise ValueError('The exact center and cut repairs must have disjoint strips')
            self.cap = reader.load_complete_tail(bundle, Path(outdir)/'verified-shared-node-index.json',
                self.fixed_source_record, self.fixed_height_view, self.fixed_provenance)
            with np.load(self.record['defining_jets']['path'], allow_pickle=False) as data:
                if np.any(data['lift_jets'][:,:,-1] != 0) or np.any(data['chart_jets'][:,:,-1] != 0):
                    raise ValueError('The full core lift and material chart must have zero cut two-jets')
                jets = data['jets'][:,:,-1].copy()
            pm, hm, coeff, self.cut_definition = cut.complete_cut_coefficients(
                jets, self.pm, self.hm, self.cap.cut_jets, self.cap.pm, self.cap.hm,
                self.cap.parameters['rCut'], self.cap.parameters['wCut'])
            self.cut_tables = cut.cut_angular_tables(pm, hm, coeff, self.N,
                self.tables['psi_boxes'], self.tables['angular_width'])
            self.tables.update(self.cut_tables)
            self.cut_definition.update(cut_width_exact=str(self.cut_width),
                cut_start_exact=str(self.cut_start), prefix_end_exact=str(self.target.end),
                correction='sum_j (-L)^j H_j((end-s)/L) Delta_j(psi)',
                zero_extension='s <= end-L', all_original_tail_modes_retained=True,
                full_height_identity_checked=True, tail_near_cut_reparameterization_certified=False,
                source_kind=SOURCE_KIND, source_model_kind=model.KIND,
                fixed_problem=context.payload['fixed_problem'],
                full_height_binding=context.payload['full_height_binding'],
                full_height_packet=context.payload['full_height_packet'],
                full_height_definition=context.payload['full_height_definition'],
                full_height_binary_sha256=context.payload['full_height_binary_sha256'],
                raw_candidate_used_as_final_height=False,
                actual_tail_provenance=self.cap.actual_fixed_tail_provenance)
            self.grid = [s for s in sorted(set(self.grid+[self.cut_start])) if s >= self.cut_start]
            output = Path(outdir)/'complete-cut-angular-tables.npz'
            np.savez(output, planar_modes=pm, height_modes=hm,
                cut_coefficient_enclosures=np.asarray(coeff.x),
                **{name:np.asarray(value.x) for name,value in self.cut_tables.items()})
            self.cut_data = ref(output)

    return FixedActualNewMetric, FixedActualCutMetric


def adapted_main(phase, context, bases, classes):
    """Only the honest source initializer/output metadata differ from old loops."""
    base = bases[phase]
    original = inspect.getsource(base.main)
    changed = original
    if phase in ('geometry', 'tables'):
        replacements = {'record, prefix = load_actual_prefix(args.source_run)':
            'record, prefix = fixed_load_prefix(args.source_run)',
            "record['physical_sha256']":'fixed_current_physical_sha()'}
    elif phase == 'metric':
        replacements = {'verifier=NewMetric(a.tables)':'verifier=fixed_new_metric(a.tables)'}
    else:
        replacements = {
            'verifier=CutMetric(args.tables,args.geometry_bundle,out,args.cut_width)':
                'verifier=fixed_cut_metric(args.tables,args.geometry_bundle,out,args.cut_width)',
            'old_metric=inherit_metric(verifier,args.base_metric,target)':
                'old_metric=fixed_inherit_metric(verifier,args.base_metric,target)',
            'old_geometry=inherit_geometry(verifier,args.base_geometry,args.base_curvature)':
                'old_geometry=fixed_inherit_geometry(verifier,args.base_geometry,args.base_curvature)'}
    for before, after in replacements.items():
        if changed.count(before) != 1:
            raise ValueError('The original interval-loop entry changed: '+before)
        changed = changed.replace(before,after)
    context.execution = dict(adapter=ref(__file__), phase=phase,
        reused_proof_loop_source=ref(base.__file__),
        original_main_sha256=hashlib.sha256(original.encode()).hexdigest(),
        executed_main_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        explicit_entry_replacements=replacements, interval_formula_methods_modified=False,
        accepted_original_replaced=False, fixed_source_gate_keeps_own_KIND=True)
    def inherit_metric(verifier, path, target):
        context.require_report(load(path))
        return bases['cut'].inherit_metric(verifier,path,target)
    def inherit_geometry(verifier,path,rational):
        context.require_report(load(path))
        return bases['cut'].inherit_geometry(verifier,path,rational)
    NewMetric, CutMetric = classes
    namespace = dict(base.__dict__)
    namespace.update(save=context.save, fixed_load_prefix=context.load_prefix,
        fixed_current_physical_sha=context.physical_sha,
        fixed_new_metric=lambda path:NewMetric(path,context),
        fixed_cut_metric=lambda tables,bundle,out,width:CutMetric(tables,bundle,out,context,width),
        fixed_inherit_metric=inherit_metric, fixed_inherit_geometry=inherit_geometry)
    exec(compile(changed,str(Path(__file__).resolve())+'::'+phase,'exec'),namespace)
    return namespace['main']


def preflight(arguments):
    parser = argparse.ArgumentParser(description='Accept the own fixed-actual source without constructing a Cartesian field')
    parser.add_argument('--source-run',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    args = parser.parse_args(arguments)
    out = args.outdir.resolve()
    if out == REPO or REPO in out.parents:
        raise ValueError('Actual execution records belong outside the source repository')
    out.mkdir(parents=True,exist_ok=False)
    context, started = FixedActualContext('preflight'), time.monotonic()
    report = dict(status='checking_actual_fixed_source',source_run=str(args.source_run.resolve()),
        source_run_sha256=sha(args.source_run),full_height_binding_verified=False,
        new_prefix_geometry_constructed=False,nonlinear_solves_executed=0,
        metric_certified=False,geometry_certified=False,C2_limit_proved=False,complete_surface=False)
    code = 0
    try:
        context.accept(args.source_run)
        report.update(status='actual_fixed_source_gate_passed_without_geometry',full_height_binding_verified=True)
    except Exception as error:
        report.update(status='actual_fixed_source_gate_rejected',error=repr(error));code=1
    report.update(seconds=time.monotonic()-started,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    context.save(out/'preflight.json',report)
    return code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase',choices=('geometry','tables','metric','cut','preflight'))
    options, rest = parser.parse_known_args()
    if options.phase == 'preflight':
        return preflight(rest)
    if '--help' in rest or '-h' in rest:
        # Showing inherited options must not import geometry before acceptance.
        print('Pass --source-run and --outdir for geometry/tables; --tables and --outdir for metric/cut.\n'
              'Other options are unchanged from scripts/resume_20261128/geometry/cartesian_prefix_'+
              {'geometry':'interval_geometry','tables':'metric_tables','metric':'metric','cut':'cut_metric'}[options.phase]+'.py.\n'
              'cut additionally requires --geometry-bundle, --base-metric, --base-geometry, --base-curvature; '
              '--cut-width selects its explicit new repair width.')
        return 0
    flag = '--source-run' if options.phase in ('geometry','tables') else '--tables'
    if rest.count(flag) != 1:
        raise ValueError('Exactly one actual source/table input is required: '+flag)
    selected = Path(rest[rest.index(flag)+1]).resolve()
    run = selected if flag == '--source-run' else Path(load(selected)['source_run'])
    context = FixedActualContext(options.phase)
    context.accept(run)  # Critical ordering: actual gate before proof imports.
    bases = proof_modules(context)
    classes = metric_classes(bases)
    entry = adapted_main(options.phase,context,bases,classes)
    sys.argv = [str(Path(__file__).resolve())+'::'+options.phase,*rest]
    return entry()


if __name__ == '__main__':
    raise SystemExit(main())
