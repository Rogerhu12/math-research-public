"""Keep exactly the paid sufficient statistics of the original finite peak rule.

No original geometry, row, epigraph, or acceptance formula is replaced.
Every completed radial block contributes its literal maxima, coincident-angle
maxima, and first maximizing angle. An interrupted prefix is an Actions
artifact, never a fabricated completed scan or an array of missing values.
"""
import copy
import gzip
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np


class PeakSummary:
    def __init__(self):
        self.rows = {}
        self.columns = {}

    def append(self, name, array, ratio):
        if array.ndim != 2 or not np.all(np.isfinite(array)):
            raise ArithmeticError('Nonfinite actual peak field')
        width = array.shape[1]
        if name in self.columns and self.columns[name] != width:
            raise ArithmeticError('Actual angular field width changed within a scan')
        self.columns[name] = width
        values = np.column_stack((np.max(array, axis=1),
            np.max(array[:, ::ratio], axis=1), np.argmax(array, axis=1)))
        self.rows.setdefault(name, []).append(values)

    def packed(self):
        return {name: np.concatenate(parts, axis=0) for name, parts in self.rows.items()}


def install(driver):
    """Install only the observer storage and its mathematically identical consumer."""
    active = []
    minimum = {'mean_E_min', 'det_min', 'z_min', 'area_min'}
    maximum = {'mean_E_max', 'ball_radius_max', 'abs_y_max'}

    class Observer:
        def __init__(self, model, args, deadline, reference_q):
            self.model, self.args, self.deadline = model, args, deadline
            self.reference_q = np.asarray(reference_q, dtype=float).copy()
            self.s, self.theta, self.nr, self.nt = model.s, model.theta, model.nr, model.nt
            self.completed, self.radial_block_calls = 0, 0
            self.pending = None
            active[:] = [self]

        def scan(self, q):
            driver.check(self.deadline)
            started = time.monotonic()
            summary = PeakSummary()
            norms = driver.NormAccumulator(self.reference_q)
            report, attainers = None, {}
            # The original driver always uses twice the actual complete angle grid.
            if self.nt % 2:
                raise ArithmeticError('Original complete angular inclusion was lost')
            self.pending = dict(q=np.asarray(q, dtype=float).copy(), started=started,
                complete_stop=0, inflight=None, summary=summary, norms=norms,
                report=None, attainers=attainers)
            for first in range(0, self.nr, self.args.scan_radial_block):
                driver.check(self.deadline)
                stop = min(first+self.args.scan_radial_block, self.nr)
                self.pending['inflight'] = [first, stop]
                block = driver.sliced_model(self.model, slice(first, stop))
                item, fields, eta = driver.hard.complete_scan(
                    block, q, self.args.mean_E_floor, self.args.det_floor)
                norms.add(block, block.cache, first)
                self.radial_block_calls += 1
                driver.COUNTS['complete_fine_radial_blocks'] += 1
                driver.COUNTS['fine_radial_points_evaluated'] += stop-first
                if report is None:
                    report = copy.deepcopy(item)
                    self.pending['report'] = report
                else:
                    for key in minimum:
                        report[key] = min(report[key], item[key])
                    for key in maximum:
                        report[key] = max(report[key], item[key])
                for name, value in fields.items():
                    # This is the original subtraction order, before any maximum.
                    array = -value.v+(0 if name == 'positive_height' else self.args.geometry_margin)
                    summary.append(name, array, 2)
                    candidate = dict(item['geometry_attainers'][name])
                    candidate['radial_index'] += first
                    if name not in attainers or candidate['value'] < attainers[name]['value']:
                        attainers[name] = candidate
                summary.append('metric', eta, 2)
                for name in ('eta_attainer', 'curvature_attainer'):
                    candidate = dict(item[name])
                    candidate['radial_index'] += first
                    if first == 0 or candidate['value'] > report[name]['value']:
                        report[name] = candidate
                self.pending['complete_stop'] = stop
                self.pending['inflight'] = None
                del block, fields, eta
            worst = min(attainers, key=lambda name: attainers[name]['value'])
            working = {name: max(0., -(value['value']-(0 if name == 'positive_height'
                        else self.args.geometry_margin))) for name, value in attainers.items()}
            report.update(radial_nodes=self.nr, theta_nodes=self.nt,
                geometry_attainers=attainers, worst_geometry_group=worst,
                geometry_violation_max=max(0., -attainers[worst]['value']),
                working_geometry_violation_max=max(working.values()),
                working_geometry_violation_by_group=working,
                eta_max=float(max(np.max(x[:,0]) for x in summary.rows['metric'])),
                complete_fine_scan=True, radial_grid_identity=driver.identity(self.s),
                continuous_radial_or_angular_coverage_certified=False,
                reference_reach_norm_observation=norms.report(q[-1]),
                scan_seconds=time.monotonic()-started,
                original_peak_decisions_use_exact_paid_row_summaries=True)
            self.completed += 1
            driver.COUNTS['complete_fine_scans'] += 1
            self.pending = None
            return report, summary, None

        def save_pending(self, path):
            p = self.pending
            if p is None:
                return {'interrupted_fine_prefix_present': False,
                        'all_complete_fine_reports_remain_in_original_events': True}
            if p['complete_stop'] == 0:
                return dict(interrupted_fine_prefix_present=False, complete_prefix_stop=0,
                    q_identity=driver.identity(p['q']), inflight_block=p['inflight'],
                    unfinished_first_block_cost_remains_in_original_global_counters=True)
            norms = p['norms']
            rows = p['summary'].packed()
            if any(len(value) != p['complete_stop'] for value in rows.values()):
                raise ArithmeticError('A paid peak field does not have the complete prefix length')
            attainers = p['attainers']
            worst = min(attainers, key=lambda name: attainers[name]['value'])
            working = {name:max(0., -(value['value']-(0 if name == 'positive_height'
                else self.args.geometry_margin))) for name,value in attainers.items()}
            prefix = copy.deepcopy(p['report'])
            prefix.update(radial_nodes=p['complete_stop'], theta_nodes=self.nt,
                geometry_attainers=attainers, worst_geometry_group=worst,
                geometry_violation_max=max(0., -attainers[worst]['value']),
                working_geometry_violation_max=max(working.values()),
                working_geometry_violation_by_group=working,
                eta_max=float(np.max(rows['metric'][:,0])), complete_fine_scan=False,
                radial_grid_identity=driver.identity(self.s[:p['complete_stop']]),
                reference_reach_norm_observation=norms.report(p['q'][-1]),
                scan_seconds=time.monotonic()-p['started'],
                continuous_radial_or_angular_coverage_certified=False)
            def accumulator_value(value):
                if isinstance(value,np.ndarray):
                    return value.tolist()
                if isinstance(value,float) and not math.isfinite(value):
                    return {'uninitialized_accumulator_sentinel':repr(value)}
                return value
            payload = dict(schema='r707-original-fine-paid-prefix-v1',
                q=p['q'].tolist(), q_identity=driver.identity(p['q']),
                p=self.model.par.p, material_sha256=self.model.field.material_mesh_sha256,
                fine_radial_nodes=self.s.tolist(), fine_radial_identity=driver.identity(self.s),
                fine_theta_nodes=self.nt, coincident_working_theta_nodes=self.nt//2,
                original_model_source_sha256=driver.MODEL_SHA256,
                original_driver_source_sha256='c0c5c1c82808ea7b54ad68cc5bfee0a921726dc2bf8dfa2ac725600859133e02',
                actual_tail_primitive_partition_receipt=self.model.tail_quadrature,
                actual_tail_height_identities={name:driver.identity(getattr(self.model,name))
                    for name in ('tail_height','tail_height1','tail_height2')},
                actual_theta_identity=driver.identity(self.theta),
                original_thresholds={k:getattr(self.args,k) for k in (
                    'mean_E_floor','det_floor','geometry_margin','pending_peak_tolerance',
                    'metric_exchange_absolute','metric_exchange_relative',
                    'restoration_exchange_absolute','restoration_exchange_relative')},
                complete_prefix_stop=p['complete_stop'], inflight_block=p['inflight'],
                original_first_block_report_accumulator=p['report'], prefix_report=prefix,
                geometry_attainers=attainers,
                peak_columns=p['summary'].columns,
                paid_peak_rows={k:v.tolist() for k,v in rows.items()},
                norm_accumulator={k:accumulator_value(v) for k,v in vars(norms).items()},
                seconds_including_incomplete_block=time.monotonic()-p['started'],
                incomplete_prefix_is_not_a_complete_fine_qualification=True,
                cooperative_clock_checked_only_between_complete_blocks=True,
                no_unsampled_fields_or_rows_created=True)
            raw=(json.dumps(payload,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
            packed=gzip.compress(raw,mtime=0)
            Path(path).write_bytes(packed)
            return dict(interrupted_fine_prefix_present=True, path=str(path),
                bytes=len(packed), sha256=hashlib.sha256(packed).hexdigest(),
                decoded_bytes=len(raw), decoded_sha256=hashlib.sha256(raw).hexdigest(),
                complete_prefix_stop=p['complete_stop'], fine_radial_nodes=self.nr,
                q_identity=driver.identity(p['q']), inflight_block=p['inflight'],
                actual_paid_rows_only=True, qualification_complete=False)

    def peaks(observer, fields, eta, nodes, nt, phase, extra, covered, args):
        if not isinstance(fields, PeakSummary) or observer.nt != 2*nt:
            raise ValueError('The exact original twofold angular peak summary is required')
        pending, urgent, pending_angle, urgent_angle = [], [], False, False
        angular_witnesses = {}
        for name, rows in fields.packed().items():
            if name == 'metric' and phase != 'metric':
                continue
            base = extra if (phase == 'geometry_restoration' or name == 'metric') else 0.
            actual_limit = max(base, covered[name])
            cutoff = (max(args.metric_exchange_absolute,args.metric_exchange_relative*max(0.,actual_limit))
                if name == 'metric' else max(args.restoration_exchange_absolute,
                                             args.restoration_exchange_relative*max(0.,actual_limit)))
            rowmax = rows[:,0]
            candidates = {int(np.argmax(rowmax))}
            candidates.update(i for i in range(1,len(rowmax)-1)
                if rowmax[i]>=rowmax[i-1] and rowmax[i]>=rowmax[i+1])
            for index in sorted(candidates):
                value = float(rowmax[index])
                if value <= base+args.pending_peak_tolerance:
                    continue
                s = float(observer.s[index])
                if np.min(abs(nodes-s)) > 1.e-12:
                    pending.append(s)
                    if value > actual_limit+cutoff:
                        urgent.append(s)
                if fields.columns[name] > 1:
                    old_angle_value = float(rows[index,1])
                    if value > max(base,old_angle_value)+args.pending_peak_tolerance:
                        pending_angle = True
                        is_urgent = value > max(actual_limit,old_angle_value)+cutoff
                        witness = dict(field=name,s=s,theta=float(observer.theta[int(rows[index,2])]),
                            fine_value=value,coincident_old_angle_maximum=old_angle_value,
                            backend_extra_or_zero=base,actual_group_cover=covered[name],
                            angular_excess=value-max(base,old_angle_value),urgent=bool(is_urgent),
                            candidate_current_complete_backend_rows_feasible=True)
                        if name not in angular_witnesses or witness['angular_excess']>angular_witnesses[name]['angular_excess']:
                            angular_witnesses[name] = witness
                        urgent_angle = urgent_angle or is_urgent
        return sorted(set(pending)),sorted(set(urgent)),pending_angle,urgent_angle,list(angular_witnesses.values())

    driver.FineObserver, driver.peak_proposals = Observer, peaks

    def save(path):
        return (active[0].save_pending(path) if active else
                {'interrupted_fine_prefix_present':False,'observer_not_constructed':True})
    return save
