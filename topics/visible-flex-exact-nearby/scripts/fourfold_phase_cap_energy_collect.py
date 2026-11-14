#!/usr/bin/env python3
"""Assemble actual cap complementary-energy enclosures from complete pieces.

This certifies the retained physical input/output compression of the full cap
form, including its regular mean port. It does not assert a bound for omitted
boundary outputs or the full core/cap Schur inverse. Partial covers produce
only a missing-piece report, never a full-cap spectral claim.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

import numpy as np
from flint import arb,acb,acb_mat,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_energy_interval import FiniteTrial,sha
from fourfold_phase_cap_wiener_cover import read_json,write_json


def matrix(values):
    return acb_mat([[acb(float(z[0]),float(z[1])) for z in row] for row in values])


def adjoint(value):
    return acb_mat([[value[j,i].conjugate() for j in range(value.nrows())]
                    for i in range(value.ncols())])


def frobenius(value):
    return sum((abs(value[i,j])**2 for i in range(value.nrows())
                for j in range(value.ncols())),arb(0)).sqrt().upper()


def choose_hermitian(value):
    n=value.nrows();chosen=acb_mat(n,n)
    binary=np.zeros((n,n),complex)
    for i in range(n):
        real=float(value[i,i].real.mid())
        chosen[i,i]=real;binary[i,i]=real
        for j in range(i+1,n):
            z=(value[i,j]+value[j,i].conjugate())/2
            real,imag=float(z.real.mid()),float(z.imag.mid())
            chosen[i,j],chosen[j,i]=acb(real,imag),acb(real,-imag)
            binary[i,j],binary[j,i]=complex(real,imag),complex(real,-imag)
    return chosen,binary,frobenius(value-chosen)


def choose_constant_kernel_center(value,mean_index):
    n=value.nrows();last=n-1
    projector=acb_mat(n,n)
    for j in range(n):projector[j,j]=1
    for i in (mean_index,last):
        for j in (mean_index,last):projector[i,j]-=acb(arb(1)/2)
    projected=projector*value*projector
    _,binary,_=choose_hermitian(projected)
    for i in range(n):
        if i in (mean_index,last):continue
        z=projected[i,mean_index]
        entry=complex(float(z.real.mid()),float(z.imag.mid()))
        binary[i,mean_index]=entry;binary[mean_index,i]=entry.conjugate()
        binary[i,last]=-entry;binary[last,i]=-entry.conjugate()
    diagonal=float(projected[mean_index,mean_index].real.mid())
    binary[mean_index,mean_index]=binary[last,last]=diagonal
    binary[mean_index,last]=binary[last,mean_index]=-diagonal
    chosen=acb_mat([[acb(float(z.real),float(z.imag)) for z in row] for row in binary])
    if any(chosen[i,mean_index]+chosen[i,last]!=0 for i in range(n)):
        raise ValueError('the explicitly selected cap center lost its exact constant gauge kernel')
    return chosen,binary,frobenius(projected-chosen)


def hermitian_norm_bound(value):
    # For an exact Hermitian matrix H, rho(H)=||H||2.  Any complete interval
    # enclosure of H^(2^j), followed by the maximum absolute row sum, gives
    # a true 2-norm upper bound after its 2^j-th root. No floating eigenvalue
    # or unverified eigensolver is used.
    if any(value[i,j]!=value[j,i].conjugate() for i in range(value.nrows())
           for j in range(value.ncols())):
        raise ValueError('the selected finite gap matrix is not exact Hermitian data')
    power=value;exponent=1;records=[]
    for step in range(5):
        rows=[sum((abs(power[i,j]).upper() for j in range(power.ncols())),arb(0)).upper()
              for i in range(power.nrows())]
        upper=max(rows)
        bound=(upper**(arb(1)/exponent)).upper()
        records.append(dict(power=exponent,row_sum=ball_record(upper),norm_bound=ball_record(bound)))
        if step<4:power=power*power;exponent*=2
    return min(arb(x['norm_bound']['ball']).upper() for x in records),records


def add_rows(report,expected_left,expected_right,total,errors):
    rows=sorted(report['intervals'],key=lambda row:Fraction(row['exact_radial_interval'][0]))
    cursor=expected_left
    for row in rows:
        left,right=map(Fraction,row['exact_radial_interval'])
        if left!=cursor or not left<right:
            raise ValueError('the completed energy report has a gap, overlap, or nonpositive interval')
        cursor=right
        for index,key in enumerate(('primal_energy','dual_energy')):
            total[index]+=matrix(row[key]['matrix_middle'])
            errors[index]+=arb(row[key]['full_operator_error']['ball']).upper()
    if cursor!=expected_right:
        raise ValueError('the completed energy report does not cover its full exact declared interval')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trial',type=Path,default=Path('notes/2026-11-12-cap-space-boundary4-interior16-P2.json'))
    parser.add_argument('--body-manifest',type=Path,action='append',default=[])
    parser.add_argument('--graft',type=Path,default=Path('data/cap_physical4_energy/graft_and_true_tail.json.gz'))
    parser.add_argument('--bits',type=int,default=320)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();ctx.prec=args.bits
    trial=FiniteTrial(args.trial)
    if not args.body_manifest:
        args.body_manifest=[Path(x) for x in (
            'data/cap_physical4_energy/body_native_0250_0800_narrow/manifest.json',
            'data/cap_physical4_energy/body_wiener_0800_3000/manifest.json',
            'data/cap_physical4_energy/body_wiener_0900_3000_vector/manifest.json')]
    allowed={sha(Path(__file__).with_name(x)) for x in (
        'fourfold_phase_cap_native_cover.py','fourfold_phase_cap_native_cover_v2.py','fourfold_phase_cap_wiener_cover.py',
        'fourfold_phase_cap_wiener_cover_v2.py')}
    needed=[j for j in range(trial.cells) if Fraction(float(trial.mesh[j+1]))<=3]
    complete={};inputs=[]
    for path in args.body_manifest:
        if not path.exists():continue
        manifest=read_json(path);identity=manifest['identity']
        if (identity['source_sha256'] not in allowed
            or identity['object_sha256']!=trial.report['object_sha256']
            or identity['trial_report_sha256']!=sha(args.trial)
            or identity['exact_trial_arrays']!=trial.report['arrays']):
            raise ValueError('a cap body proof uses a different actual graph, exact finite trial or allowed kernel')
        for name,digest in identity['dependency_sha256'].items():
            if sha(Path(__file__).with_name(name))!=digest:
                raise ValueError('an actual cap proof dependency changed: '+name)
        inputs.append(dict(path=str(path),sha256=sha(path)))
        for item in manifest['elements']:
            if not item['complete']:continue
            element=item['element'];part=Path(item['path'])
            if sha(part)!=item['sha256']:
                raise ValueError('completed body energy matrices changed on disk')
            report=read_json(part)
            if not report['complete'] or report['identity']!=identity:
                raise ValueError('an element report and its actual cover identity differ')
            a,b=map(lambda x:Fraction(float(x)),trial.mesh[element:element+2])
            if report['exact_radial_interval']!=[str(a),str(b)] or element not in needed:
                raise ValueError('wrong exact finite trial element in the body cover')
            if element in complete:
                raise ValueError('overlapping independently selected body proofs need an explicit selection')
            complete[element]=report
            inputs.append(dict(path=str(part),sha256=item['sha256']))
    missing=[j for j in needed if j not in complete]
    answer=dict(kind='true_physical_cap_complementary_energy_compression',complete=False,
        source_sha256=sha(__file__),object_sha256=trial.report['object_sha256'],
        exact_delta_fraction=trial.report['exact_delta_fraction'],
        exact_trial_report=dict(path=str(args.trial),sha256=sha(args.trial)),
        boundary_physical_modes=trial.B,interior_trial_modes=trial.M,regular_mean_port_retained=True,
        completed_body_elements=sorted(complete),missing_body_elements=missing,
        input_reports=inputs,bits=args.bits,
        scope='Physical finite input/output compression of the complete true positive cap; no omitted-output or whole core/cap inverse bound is claimed.')
    if missing:
        write_json(args.out,answer)
        print(json.dumps(dict(complete=False,missing_body_elements=missing)),flush=True)
        return
    graft=read_json(args.graft)
    if (not graft['complete'] or graft['object_sha256']!=trial.report['object_sha256']
        or graft['trial_report_sha256']!=sha(args.trial)
        or graft['source_sha256']!=sha(Path(__file__).with_name('fourfold_phase_cap_graft_tail_energy.py'))):
        raise ValueError('the true graft/tail energy is incomplete or belongs to another exact input')
    for name,digest in graft['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError('an actual graft/tail proof dependency changed: '+name)
    answer['input_reports'].append(dict(path=str(args.graft),sha256=sha(args.graft)))
    total=[acb_mat(trial.d,trial.d),acb_mat(trial.d,trial.d)];fees=[arb(0),arb(0)]
    for element in needed:
        a,b=map(lambda x:Fraction(float(x)),trial.mesh[element:element+2])
        add_rows(complete[element],a,b,total,fees)
    add_rows(graft,Fraction(3),Fraction(25,8),total,fees)
    for j,key in enumerate(('primal_energy','dual_energy')):
        tail=graft['infinite_tail'][key]
        total[j]+=matrix(tail['matrix_middle'])
        fees[j]+=arb(tail['full_operator_error']['ball']).upper()
    E,Ebin,Eround=choose_hermitian(total[0]);D,Dbin,Dround=choose_hermitian(total[1])
    Eerror,Derror=(fees[0]+Eround).upper(),(fees[1]+Dround).upper()
    T=matrix(graft['infinite_tail']['exact_boundary_T'])
    gap=E-T-adjoint(T)+D
    gapnorm,norm_steps=hermitian_norm_bound(gap)
    exact_center=(E+T+adjoint(T)-D)/2
    # The true augmented grounded cap has the exact kernel U=1, xi=1:
    # its entire gradient and nonmean Robin trace vanish. Projecting both
    # sides onto that kernel's orthogonal complement does not increase the
    # operator error. The stored dyadic center is then chosen with exactly
    # opposite mean/xi columns, rather than declaring a floating trial sum exact.
    center,centerbin,centerround=choose_constant_kernel_center(exact_center,trial.B)
    radius=(gapnorm/2+max(Eerror,Derror)+centerround).upper()
    arrays=args.out.with_suffix('.npz')
    np.savez_compressed(arrays,primal_energy_center=Ebin,dual_energy_center=Dbin,
        actual_cap_compression_center=centerbin,
        exact_boundary_T=np.array([[complex(float(T[i,j].real.mid()),float(T[i,j].imag.mid()))
                                   for j in range(trial.d)] for i in range(trial.d)]))
    answer.update(complete=True,exact_radial_cover=['1/4','25/8'],
        arrays=dict(path=str(arrays),sha256=sha(arrays),bytes=arrays.stat().st_size),
        primal_total_operator_error=ball_record(Eerror),dual_total_operator_error=ball_record(Derror),
        accumulated_matrix_rounding=[ball_record(Eround),ball_record(Dround)],
        full_gap_norm_upper=ball_record(gapnorm),gap_norm_power_bounds=norm_steps,
        full_actual_primal_dual_gap_upper=ball_record((gapnorm+Eerror+Derror).upper()),
        final_center_selection_error=ball_record(centerround),
        exact_constant_kernel_in_saved_center=True,
        constant_kernel_projection='P=I-vv*/2, v=e_left_mean+e_regular_mean; the true grounded form annihilates v exactly, so projection is contractive for the enclosure error.',
        true_cap_compression_operator_radius=ball_record(radius),
        mathematical_statement='For every retained physical boundary+regular-mean vector g, (T+T*-Dtrue)[g,g] <= Strue[g,g] <= Etrue[g,g]; the operator norm of the true retained compression minus saved_center is at most the recorded radius.')
    write_json(args.out,answer)
    print(json.dumps(dict(complete=True,true_cap_compression_radius=answer['true_cap_compression_operator_radius'],
        full_gap_norm=answer['full_gap_norm_upper'])),flush=True)


if __name__=='__main__':main()
