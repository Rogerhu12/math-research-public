#!/usr/bin/env python3
"""Actual finite-input R178 constants and a few pointwise interval comparisons."""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,gzip,json,resource,time,traceback
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import ProfileBox,ChartBox,connection_box,bound_record,aq
from fd2d_gc_current_primitive_interval_v2 import norm_upper
from fd2d_gc_r136_arb_profile import ends
from fd2d_gc_dyadic_tail_accurate_last_cell import DyadicTailAccurateLastCell
from fd2d_gc_terminal_forcing_majorant import (
    terminal_forcing_majorant,terminal_forcing_integrals,encode)


def write_packet(path,value):
    raw=(json.dumps(encode(value),sort_keys=True,separators=(',',':'),
                    allow_nan=False)+'\n').encode()
    with path.open('wb') as stream:
        with gzip.GzipFile(filename='',fileobj=stream,mode='wb',mtime=0) as out:
            out.write(raw)
    return dict(**identity(path),uncompressed_bytes=len(raw))


def run(args):
    started=time.monotonic();ctx.prec=args.precision
    outputs={key:args.out_prefix.with_name(args.out_prefix.name+suffix)
             for key,suffix in (('report','-report.json'),('majorant','-majorant.json.gz'))}
    args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if any(path.exists() for path in outputs.values()):
        raise FileExistsError('Do not overwrite an actual terminal-forcing run')
    report=dict(schema='fd2d-R178-terminal-forcing-actual-check-v1',
        source=identity(__file__),passed=False,
        field=identity(args.field),profile_packet=identity(args.profile_packet),
        whole_F_J_BVP_body_evaluated=False,whole_surface_certificate=False)
    try:
        terminal=DyadicTailAccurateLastCell(args.field,args.profile_packet,
            profile_sha256=report['profile_packet']['sha256'])
        majorant=terminal_forcing_majorant(terminal)
        report['majorant']=write_packet(outputs['majorant'],majorant)
        report['binding']=dict(
            actual_terminal_binding=terminal.definition()['binding_sha256'],
            accurate_profile_target=terminal.profile.input_binding_sha256,
            exact_domain_upper='6/5',
            tail_certificate=terminal.tail_control_certificate,
            majorant_source=identity(Path(__file__).with_name(
                'fd2d_gc_terminal_forcing_majorant.py')))
        report['coefficients']=encode(majorant['H_norm_upper_coefficients'])
        report['K_s_constant']=encode(majorant['K_s_absolute_over_tau_squared_upper'])
        report['tau_upper']=encode(majorant['tau_upper'])
        samples=[]
        for t in (F(1,2),F(7,8),F(1)-F(1,2**12)):
            tau_lo,tau_hi=ends(terminal.length*(1-aq(t)))
            envelope=terminal_forcing_integrals(majorant,tau_hi)
            for angle in (F(0),F(1,4),F(1,2)):
                q=terminal.box(t,t,angle,angle)
                p=q['profile']
                profile=ProfileBox(p['a'],p['a_s'],p['a_ss'],p['a_sss'])
                actual=connection_box(q['fields'],profile,
                                      ChartBox(arb(1),arb(0),arb(0),arb(0)))
                hnorm=norm_upper(actual['h_vector'])
                if not hnorm<=aq(envelope['H_sup_upper']):
                    raise AssertionError('A selected strict H point enclosure exceeds the analytic majorant')
                Ks=abs(profile.curvature_jet().s).upper()
                Ks_bound=majorant['K_s_absolute_over_tau_squared_upper']*tau_hi**2
                if not Ks<=aq(Ks_bound):
                    raise AssertionError('A selected accurate K_s enclosure exceeds the analytic phase bound')
                if not actual['G'].contains(0):
                    raise AssertionError('The pointwise interval does not contain the exact algebraic G=0')
                samples.append(dict(t=str(t),u_pi=str(angle),
                    tau_lower=str(tau_lo),tau_upper=str(tau_hi),
                    actual_interval_H_norm_upper=bound_record(hnorm),
                    analytic_H_upper=encode(envelope['H_sup_upper']),
                    actual_interval_K_s_abs_upper=bound_record(Ks),
                    analytic_K_s_upper=encode(Ks_bound),
                    actual_G_enclosure=bound_record(actual['G'])))
        report['nine_local_point_comparisons']=samples
        report['exact_continuous_proof_independent_of_point_samples']=True
        report['terminal_integral_contributions']=[
            encode(terminal_forcing_integrals(majorant,eps)) for eps in
            (majorant['tau_upper'],F(1,2**20),F(1,2**30),F(1,2**40),F(1,2**50))]
        report['actual_initial_D_C_bounds_supplied']=False
        report['whole_angle_terminal_forcing_bound']=True
        report['actual_G_zero_proved_algebraically']=True
        report['cut_radial_II_derivative_assigned']=False
        if identity(args.field)!=report['field']:
            raise AssertionError('Actual input archive changed')
        report['actual_field_unchanged']=True
        report['passed']=True
    except Exception as exc:
        report['error']=dict(type=type(exc).__name__,message=str(exc),
                             traceback=traceback.format_exc())
        raise
    finally:
        report['seconds']=time.monotonic()-started
        report['peak_rss_kib']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        outputs['report'].write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(passed=report['passed'],report=str(outputs['report']),
            seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'],
            whole_surface_certificate=False),allow_nan=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--field',type=Path,required=True)
    parser.add_argument('--profile-packet',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--precision',type=int,default=256)
    run(parser.parse_args())
