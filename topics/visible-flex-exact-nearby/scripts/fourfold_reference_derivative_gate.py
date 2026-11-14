#!/usr/bin/env python3
"""Continuous nonzero Y_x gate for finite Fourier/Bernstein references.

R68 section 4: for each of the eight real-time Bernstein controls, certify
Re(1/4+U_j'(x)) on both complex initial-label boundaries. Exact Fourier
reality makes the two real parts equal. Boundary real parts are finite real
trigonometric polynomials whose positive-frequency coefficients are multiplied by cosh(kS).
A directed DFT supplies local Taylor coefficients, and a complete Fourier
bound pays the remainder on every closed angular cell.

Optional retarget corrections remain symbolic: forward Q*a and backward
Q*(Q_forward,end*a). Their entire C1 Wiener fees are subtracted from the base
control lower bounds. No product Fourier truncation is performed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_series, ctx

from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_affine import sha
from fourfold_native_series_fft import NativeSeriesFFT
from fourfold_retarget_reference_jets import (
    RetargetReference, segment_arrays, time_value,
)


def saved_lower(row):
    return arb(row['lower']).lower()


def saved_upper(row):
    return arb(row['upper']).upper()


def finite_Wiener_bounds(coefficients, width):
    """Zeroth and first normalized initial-label derivatives."""
    zero, first = arb(0), arb(0)
    for k, value in enumerate(coefficients):
        value = acb(value)
        if not value.is_finite():
            raise ValueError('nonfinite exact Fourier coefficient')
        if k == 0:
            if value.imag != 0:
                raise ValueError('non-real Fourier mean')
            zero += abs(value)
        else:
            weighted = 2*abs(value)*(k*width).exp()
            zero += weighted
            first += k*weighted
    return zero.upper(), first.upper()


class BoundaryTaylorGate:
    def __init__(self, degree, nodes, width, order=6):
        if (nodes < 2 or nodes & (nodes-1) or not nodes > 2*degree
                or order < 2 or not width >= 0):
            raise ValueError('invalid exact finite boundary grid')
        self.degree, self.nodes, self.width, self.order = degree, nodes, width, order
        self.half_cell = arb.pi()/nodes
        self.transform = NativeSeriesFFT()
        self.basis, self.remainder_weight, self.norm_weight = {}, {}, {}
        for k in range(1, degree+1):
            hyperbolic = (k*width).cosh()
            factor = acb(hyperbolic)
            row = [factor]
            for derivative in range(1, order):
                factor = factor*acb(0,k)*self.half_cell/derivative
                row.append(factor)
            self.basis[k] = row
            self.remainder_weight[k] = (
                2*hyperbolic*(k*self.half_cell)**order/math.factorial(order)).upper()
            self.norm_weight[k] = (2*(k*width).exp()).upper()

    def evaluate(self, real, imag):
        """Eight (or fewer) U controls, with all nonnegative Fourier modes."""
        if (real.shape != imag.shape or real.ndim != 2
                or real.dtype != np.dtype('float64') or imag.dtype != np.dtype('float64')
                or real.shape[0] < 1
                or real.shape[1] != self.degree+1
                or not np.all(np.isfinite(real)) or not np.all(np.isfinite(imag))
                or np.any(imag[:,0] != 0)):
            raise ValueError('invalid exact real Fourier control array')
        controls, N, order = real.shape[0], self.nodes, self.order
        started, cpu = time.monotonic(), time.process_time()
        coefficients = np.empty((N, controls), dtype=object)
        coefficients.fill(acb_series([0]*order, prec=order))
        remainders, upper_norms = [], []
        for control in range(controls):
            coefficients[0,control] = acb_series([acb(arb(1)/4)]+[acb(0)]*(order-1),prec=order)
            remainder, upper_norm = arb(0), arb(1)/4
            for k in range(1,self.degree+1):
                derivative = acb(0,k)*acb(arb(float(real[control,k])),
                                           arb(float(imag[control,k])))
                positive = [derivative*weight for weight in self.basis[k]]
                negative = [acb(v.real,-v.imag) for v in positive]
                coefficients[k,control] = acb_series(positive,prec=order)
                coefficients[-k,control] = acb_series(negative,prec=order)
                remainder += abs(derivative)*self.remainder_weight[k]
                upper_norm += abs(derivative)*self.norm_weight[k]
            remainders.append(remainder.upper())
            upper_norms.append(upper_norm.upper())
        values = self.transform.fft(coefficients,inverse=True)*N
        del coefficients
        results = []
        for control in range(controls):
            minimum = None
            minimum_node = None
            minimum_center_upper = None
            center_node = None
            for node in range(N):
                jet = values[node,control]
                if not all(jet[i].is_finite() and jet[i].imag.contains(0) for i in range(order)):
                    raise ValueError('real boundary-derivative transform lost reality or finiteness')
                variation = sum((abs(jet[i].real) for i in range(1,order)),arb(0)).upper()
                lower = (jet[0].real.lower()-variation-remainders[control]).lower()
                center_upper = jet[0].real.upper()
                if minimum is None or lower < minimum:
                    minimum, minimum_node = lower, node
                if minimum_center_upper is None or center_upper < minimum_center_upper:
                    minimum_center_upper, center_node = center_upper, node
            results.append(dict(
                full_boundary_real_part_lower=minimum,
                full_strip_derivative_modulus_upper=upper_norms[control],
                cell_remainder_upper=remainders[control],
                minimum_lower_node=minimum_node,
                minimum_center_upper=minimum_center_upper,
                minimum_center_upper_node=center_node,
                negative_boundary_control_value_proved=bool(minimum_center_upper < 0),
                angular_nodes=N,taylor_order=order))
        del values
        return results, dict(wall_seconds=time.monotonic()-started,
                             cpu_seconds=time.process_time()-cpu)

    @staticmethod
    def record(row):
        return {key:ball_record(value) if isinstance(value,arb) else value
                for key,value in row.items()}


def save_report(path, report):
    payload=(json.dumps(report,indent=2)+'\n').encode()
    if path.suffix == '.gz':
        payload=gzip.compress(payload,mtime=0)
    if len(payload)>5_000_000:
        raise ValueError('report exceeds repository file limit; choose .json.gz')
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.writing')
    temporary.write_bytes(payload)
    temporary.replace(path)


def read_report(path):
    raw=path.read_bytes()
    if path.suffix=='.gz':raw=gzip.decompress(raw)
    return json.loads(raw)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--manifest',type=Path)
    group.add_argument('--retarget-descriptor',type=Path)
    parser.add_argument('--leg',choices=('forward','backward'),default='forward')
    parser.add_argument('--widths',default='1/512')
    parser.add_argument('--nodes',type=int,default=2048)
    parser.add_argument('--max-nodes',type=int,default=8192)
    parser.add_argument('--taylor-order',type=int,default=6)
    parser.add_argument('--first-segment',type=int,default=0)
    parser.add_argument('--max-segments',type=int,default=0)
    parser.add_argument('--bits',type=int,default=160)
    parser.add_argument('--resume',action='store_true')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    started,cpu=time.monotonic(),time.process_time()
    ctx.prec,ctx.cap=args.bits,args.taylor_order
    if (args.bits<128 or args.nodes<2 or args.nodes&(args.nodes-1)
            or args.max_nodes<args.nodes or args.max_nodes&(args.max_nodes-1)):
        raise ValueError('invalid precision or power-of-two grid sizes')
    widths=list(map(Fraction,args.widths.split(',')))
    if not widths or any(s<=0 for s in widths):
        raise ValueError('strictly positive normalized initial-label strips required')
    retarget=None
    if args.retarget_descriptor:
        retarget=RetargetReference(args.retarget_descriptor)
        manifest_path,manifest=retarget.base[args.leg]
    else:
        manifest_path=args.manifest
        manifest=json.loads(manifest_path.read_text())
    if (not manifest.get('complete') or manifest['time_basis']!='bernstein'
            or manifest['time_degree']!=7 or manifest['fields']!=['U','L']
            or manifest['leg']!=args.leg
            or not manifest['continuous_by_shared_endpoint_coefficients']):
        raise ValueError('complete continuous degree-seven Fourier/Bernstein reference required')
    first=args.first_segment
    stop=manifest['segment_count'] if args.max_segments==0 else min(
        manifest['segment_count'],first+args.max_segments)
    if not 0<=first<stop<=manifest['segment_count']:
        raise ValueError('empty or invalid requested segment range')
    if not args.nodes>2*manifest['Fourier_degree']:
        raise ValueError('initial angular grid must strictly exceed twice the finite Fourier degree')
    identity=dict(manifest_path=str(manifest_path),manifest_sha256=sha(manifest_path),
        retarget_descriptor=None if retarget is None else str(args.retarget_descriptor),
        retarget_descriptor_sha256=None if retarget is None else sha(args.retarget_descriptor),
        leg=args.leg,source_sha256=sha(__file__),bits=args.bits,
        first_segment=first,stop_segment=stop,widths=list(map(str,widths)),
        nodes=args.nodes,max_nodes=args.max_nodes,taylor_order=args.taylor_order,
        coordinate='normalized initial label x, period 2*pi; q=partial_x physical Y')
    report=dict(kind='continuous_finite_reference_initial_derivative_gate',
        complete=False,identity=identity,segments=[],
        definition='Y=x/4+U, optionally plus the exact symbolic retarget product',
        proof='Bernstein convexity in real time; conjugate boundary real parts; '
              'finite unaliased DFT and closed-cell Taylor remainder; harmonic minimum principle',
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_native_series_fft.py','fourfold_retarget_reference_jets.py',
            'fourfold_phase_beta_interval.py','fourfold_shared_dense_reference.py')},
        limitations=['Only a sufficient positive-real-part gate; failure does not prove a zero',
            'No true field or flow accuracy is used or inferred',
            'Time is real; the initial-label strip is complex',
            'The finite retarget Q is only a specified coefficient function, not an asserted Jacobian'])
    if args.resume and args.out.exists():
        previous=read_report(args.out)
        if previous['identity']!=identity:
            raise ValueError('resume identities or numerical gates changed')
        report=previous
        if report.get('complete'):
            print(json.dumps(dict(complete=True,reused_completed_gate=True)),flush=True)
            return
        if report.get('stopped_on_unproved_sufficient_gate'):
            raise ValueError('previous sufficient gate was unproved; use a new output with revised settings')
    engines={}
    static_bounds={}
    for s in widths:
        width=exact_arb(s)
        if retarget is None:
            static_bounds[s]=None
        else:
            a0,a1=finite_Wiener_bounds(retarget.a[0],width)
            if args.leg=='backward':
                q0,q1=finite_Wiener_bounds(retarget.forward_end[0],width)
                static_bounds[s]=((q0*a0).upper(),(q1*a0+q0*a1).upper())
            else:
                static_bounds[s]=(a0,a1)
    already=len(report['segments'])
    if [row['segment'] for row in report['segments']]!=list(range(first,first+already)):
        raise ValueError('resume segment records are not contiguous')
    previous_end=previous_Q_end=None
    if first+already>0:
        real,imag,_=segment_arrays(manifest_path,manifest,first+already-1,['U','L'])
        previous_end=(real[-1].copy(),imag[-1].copy())
        if retarget is not None:
            qp,qdoc=retarget.Q[args.leg]
            qr,qi,_=segment_arrays(qp,qdoc,first+already-1,['Qtilde'])
            previous_Q_end=(qr[-1].copy(),qi[-1].copy())
    for index in range(first+already,stop):
        real,imag,base_source=segment_arrays(manifest_path,manifest,index,['U','L'])
        if previous_end is not None and (not np.array_equal(previous_end[0],real[0])
                or not np.array_equal(previous_end[1],imag[0])):
            raise ValueError('base reference has a genuine endpoint coefficient jump')
        previous_end=(real[-1].copy(),imag[-1].copy())
        t0,t1=map(time_value,manifest['exact_time_endpoints'][index:index+2])
        if not manifest['time_orientation']*(t1-t0)>0:
            raise ValueError('nonpositive exact time segment')
        Qreal=Qimag=Qsource=None
        if retarget is not None:
            qp,qdoc=retarget.Q[args.leg]
            Qreal,Qimag,Qsource=segment_arrays(qp,qdoc,index,['Qtilde'])
            if Qreal.dtype != np.dtype('float64') or Qimag.dtype != np.dtype('float64'):
                raise ValueError('retarget Q coefficients must be the saved exact binary64 inputs')
            if previous_Q_end is not None and (
                    not np.array_equal(previous_Q_end[0],Qreal[0])
                    or not np.array_equal(previous_Q_end[1],Qimag[0])):
                raise ValueError('retarget Q has a genuine endpoint coefficient jump')
            previous_Q_end=(Qreal[-1].copy(),Qimag[-1].copy())
        rows={}
        for s in widths:
            width=exact_arb(s)
            fees=[arb(0) for _ in range(8)]
            if retarget is not None:
                b0,b1=static_bounds[s]
                for control in range(8):
                    coefficient=[acb(arb(float(a)),arb(float(b)))
                                 for a,b in zip(Qreal[control],Qimag[control])]
                    q0,q1=finite_Wiener_bounds(coefficient,width)
                    fees[control]=(q1*b0+q0*b1).upper()
            N=args.nodes
            while True:
                key=(s,N)
                if key not in engines:
                    engines[key]=BoundaryTaylorGate(manifest['Fourier_degree'],N,width,args.taylor_order)
                controls,timing=engines[key].evaluate(real[:,0,:],imag[:,0,:])
                corrected=[(row['full_boundary_real_part_lower']-fee).lower()
                           for row,fee in zip(controls,fees)]
                passed=all(value>0 for value in corrected)
                negative=any(row['negative_boundary_control_value_proved'] for row in controls)
                if passed or negative or N>=args.max_nodes:
                    break
                N*=2
            upper_values=[(row['full_strip_derivative_modulus_upper']+fee).upper()
                          for row,fee in zip(controls,fees)]
            rows[str(s)]=dict(
                positive_real_part_gate_proved=passed,
                real_part_lower=ball_record(min(corrected)),
                modulus_upper=ball_record(max(upper_values)),
                retarget_C1_fees=[ball_record(v) for v in fees],
                control_bounds=[BoundaryTaylorGate.record(row) for row in controls],
                final_angular_nodes=N,timing=timing)
        report['segments'].append(dict(segment=index,base_source=base_source,
            Q_source=Qsource,exact_times=manifest['exact_time_endpoints'][index:index+2],
            widths=rows,continuous_with_previous_checked=index>0,
            Q_continuous_with_previous_checked=bool(retarget is not None and index>0)))
        report['elapsed_seconds_this_process']=time.monotonic()-started
        report['cpu_seconds_this_process']=time.process_time()-cpu
        save_report(args.out,report)
        if (index-first)%10==0 or index+1==stop:
            print(json.dumps(dict(segment=index,
                bounds={s:row['real_part_lower']['ball'] for s,row in rows.items()},
                passed={s:row['positive_real_part_gate_proved'] for s,row in rows.items()},
                cpu_seconds=report['cpu_seconds_this_process'])),flush=True)
        if not all(row['positive_real_part_gate_proved'] for row in rows.values()):
            report['stopped_on_unproved_sufficient_gate']=True
            save_report(args.out,report)
            raise SystemExit('positive-real-part sufficient gate not proved; saved diagnostic, no zero claim')
    report['complete']=True
    summaries={}
    for s in map(str,widths):
        bounds=[row['widths'][s] for row in report['segments']]
        summaries[s]=dict(
            minimum_real_part_lower=ball_record(min(saved_lower(row['real_part_lower']) for row in bounds)),
            maximum_modulus_upper=ball_record(max(saved_upper(row['modulus_upper']) for row in bounds)),
            every_segment_passed=all(row['positive_real_part_gate_proved'] for row in bounds))
    report['global_bounds_on_requested_region']=summaries
    report['full_branch_nonzero_proved']=bool(first==0 and stop==manifest['segment_count']
        and all(row['every_segment_passed'] for row in summaries.values()))
    report['elapsed_seconds_this_process']=time.monotonic()-started
    report['cpu_seconds_this_process']=time.process_time()-cpu
    save_report(args.out,report)
    print(json.dumps(dict(complete=True,full_branch_nonzero_proved=report['full_branch_nonzero_proved'],
                         global_bounds=summaries),indent=2),flush=True)


if __name__=='__main__':
    main()

