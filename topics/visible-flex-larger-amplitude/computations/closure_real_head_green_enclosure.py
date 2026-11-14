#!/usr/bin/env python3
"""Validated low-window two-boundary Green bounds from real head columns.

The physical momentum is P=mu_n*Xi_n.  A far-admissible column phi and a
backward column psi with Q(cut)=0, Xi_12(cut)=1 give the constant physical
Wronskian W=mu_12*phi_Q(cut).  This program uses their whole-cell bounds,
not a subtraction of large Cauchy propagators.  The complete R23 nonlinear
source is projected onto the explicitly computed low window.  Frequencies
outside that window and the nonlinear far graph remain separate inputs.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, power2, ball_record
from closure_projective_interval_column import ProjectiveColumn


def endpoint(x):
    return arb((int(x['mantissa']), int(x['binary_exponent'])))


def ball(x):
    return endpoint(x['lower']).union(endpoint(x['upper']))


def upper(x):
    return abs(x).upper()


def maximum(a, b):
    return a.union(b).upper()


def mat(x):
    return [[ball(v) for v in row] for row in x]


def mv(a, x):
    return [a[i][0]*x[0]+a[i][1]*x[1] for i in range(2)]


def inverse_unimodular(a):
    # The exact gauge flow has determinant one.  Taking cofactors of its
    # entrywise enclosure is valid; dividing by an interval determinant
    # would introduce an artificial near-singular interval calculation.
    return [[a[1][1], -a[0][1]], [-a[1][0], a[0][0]]]


def ceil_log2_upper(x):
    y=x.upper()
    if not y > 0:
        raise ArithmeticError('A strictly positive kernel majorant is required')
    mantissa, exponent=y.man_exp()
    mantissa, exponent=int(mantissa), int(exponent)
    return exponent+mantissa.bit_length()-(1 if mantissa & (mantissa-1)==0 else 0)


def load_json(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),raw


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--columns',required=True,type=Path)
    parser.add_argument('--ready',required=True,type=Path)
    parser.add_argument('--out-prefix',required=True,type=Path)
    parser.add_argument('--precision',type=int,default=192)
    args=parser.parse_args();ctx.prec=args.precision
    started=time.monotonic()
    data,raw=load_json(args.columns);ready,ready_raw=load_json(args.ready)
    if hashlib.sha256(ready_raw).hexdigest() not in data['input_hashes'].values():
        raise ValueError('The ready file is not the one certified by the columns')
    if not data['all_reference_R23_balls_paid']:
        raise ValueError('The complete reference source has no paid R23 balls')
    rc=exact_q(ready['rationalDeepModel']['physicalParameters']['rCuff'])
    rho=(arb(11)*arb(2).log()/4).exp()
    rows=data['cell_rows'];cells=[r['cell'] for r in rows];count=len(cells)
    if cells != list(range(data['start_physical_node'],data['far_physical_node'])):
        raise ValueError('Expected contiguous outward-to-inward cell order')
    # Exponents give an exact dyadic upper bound, with at most one bit of
    # inflation per cell-pair.  Taking the supremum over diagonal Fourier
    # blocks is the weighted l1 operator norm; there is no mode-count factor.
    gamma=[[None]*count for _ in range(count)]
    mode_summaries=[];group_hashes={}
    for group_ref in data['column_groups']:
        path=Path(group_ref['path']);group,group_raw=load_json(path)
        digest=hashlib.sha256(group_raw).hexdigest()
        if digest != group_ref['sha256']:
            raise ValueError('A column group hash differs from its manifest')
        group_hashes[str(path)]=digest
        group_rows=group['cell_rows']
        if [r['cell'] for r in group_rows] != cells:
            raise ValueError('Column group cell order differs')
        mu=[ball(r['mu']) for r in group_rows]
        mu_ratio=[x/mu[0] for x in mu]
        for col,m in enumerate(group['modes']):
            entry=group['endpoint_rows'][col]
            glo=endpoint(entry['Q_gain']['lower']);ghi=endpoint(entry['Q_gain']['upper'])
            if not (glo>0 or ghi<0):
                raise ArithmeticError('The real low-height chart contains zero')
            gain_lower=glo if glo>0 else -ghi
            phiQ=[];phiXi=[];psiQ=[];psiXi=[]
            u=m*m-4
            cut_r=ball(group_rows[0]['r_outer'])
            psi=ProjectiveColumn([arb(0),(cut_r/rc)**u])
            for k,row in enumerate(group_rows):
                linear=row['linear_rows'][col]
                if linear['mode'] != m:
                    raise ValueError('A column order mismatch was found')
                phiQ.append(upper(ball(linear['column_Q_sup']))/gain_lower)
                phiXi.append(upper(ball(linear['column_Xi_sup']))/gain_lower)
                radius=ball(row['r_inner']).union(ball(row['r_outer']))
                backward=mat(linear['gauge_backward_majorant'])
                within=mv(backward,psi.absolute_uppers())
                psiQ.append(upper((radius/rc)**u)*within[0])
                psiXi.append(upper((rc/radius)**u)*within[1])
                psi.advance(inverse_unimodular(mat(linear['gauge_matrix'])))
                if k+1<count:
                    psi.multiply_component(1,rho)
            wq=arb((1+m)**3);wx=arb(1+m)
            phi_norm=[wq*q+wx*x for q,x in zip(phiQ,phiXi)]
            psi_norm=[wq*q+wx*x for q,x in zip(psiQ,psiXi)]
            local_max=None
            for k in range(count):
                for n in range(count):
                    if k>n:
                        value=mu_ratio[n]*phi_norm[k]*psiQ[n]
                    elif k<n:
                        value=mu_ratio[n]*psi_norm[k]*phiQ[n]
                    else:
                        # Q and Xi suprema may occur at different points.
                        # Maximize the two components separately before
                        # taking their weighted sum; max of the sums is not
                        # sufficient for R23's sum-of-component sup norm.
                        value=mu_ratio[n]*(wq*phiQ[k]*psiQ[n]
                            +wx*maximum(phiXi[k]*psiQ[n],psiXi[k]*phiQ[n]))
                    exponent=ceil_log2_upper(value)
                    if gamma[k][n] is None or exponent>gamma[k][n]:
                        gamma[k][n]=exponent
                    if k==n and (local_max is None or exponent>local_max):
                        local_max=exponent
            mode_summaries.append(dict(mode=m,
                absolute_physical_Wronskian_lower_bound=ball_record(mu[0].lower()*gain_lower),
                maximum_diagonal_kernel_log2_upper=local_max,
                cut_cell_psi_Q_bound=ball_record(psiQ[0]),
                cut_cell_psi_Xi_bound=ball_record(psiXi[0])))
        print(json.dumps(dict(event='column_group',modes=group['modes'],
            seconds=time.monotonic()-started,
            RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    reference=[ball(row['whole_cell_reference_X']).upper() for row in rows]
    source=[ball(row['complete_source_L1_bound']).upper() for row in rows]
    response=[];eta=arb(0)
    for k in range(count):
        value=sum((power2(gamma[k][n])*source[n] for n in range(count)),arb(0))
        ratio=value/reference[k]
        eta=maximum(eta,ratio)
        response.append(dict(cell=cells[k],reference_X_upper=ball_record(reference[k]),
            projected_complete_source_response_bound=ball_record(value),
            response_relative_to_reference=ball_record(ratio),
            log2_response_bound=ball_record(value.log()/arb(2).log())))
    # A ball of radius X_ref about the exact linear reference lies in 2 X_ref.
    # R23 gives map displacement <=4 eta and Lipschitz constant <=8 eta in
    # the cell-weighted max norm.  This is a projected pointwise equation,
    # not the source worker's compressed Galerkin inverse.
    doubled_balls=all(2*ball(row['relative_to_R23_radius']).upper()<1 for row in rows)
    mapping=4*eta;lip=8*eta
    projected_gate=bool(doubled_balls and mapping<1 and lip<1)
    result=dict(status='Validated real low-window boundary-value Green envelope; all-frequency nonlinear matching is not asserted',
        modes=data['modes'],reference_modes=data['reference_modes'],tau=data['tau'],cells=cells,
        input_source='R23 full nonlinear source, including its full pointwise mean branch, projected only at the output onto the stated low window',
        gamma_log2_upper=gamma,
        gamma_semantics='Gamma[k,n] <= 2**gamma_log2_upper[k][n] maps the cell-n L1_r W_tau scalar Xi-source norm to the cell-k sum of weighted component suprema; diagonal Fourier block norms take a supremum, not a sum over modes.',
        response_rows=response,mode_summaries=mode_summaries,
        maximum_response_relative_to_reference=ball_record(eta),
        doubled_reference_R23_balls_paid=doubled_balls,
        projected_pointwise_fixed_point=dict(gate_paid=projected_gate,
            relative_radius=1,mapping_displacement_bound=ball_record(mapping),
            contraction_bound=ball_record(lip),
            equation='P_low of the full pointwise vector field, with all nonmean modes outside the stated window set to zero only in this auxiliary projected problem; its mean is the full holonomy root.',
            boundary='Exact linear R18 modal far subspaces and fixed saved low cut heights of the reference; this is not the full nonlinear R18 far graph.',
            scope='Only this auxiliary projected boundary-value problem follows if gate_paid is true. No original numerical worker, full-frequency solution, or closed surface is thereby certified.'),
        input_hashes={str(args.columns):hashlib.sha256(raw).hexdigest(),
            str(args.ready):hashlib.sha256(ready_raw).hexdigest(),**group_hashes},
        entrypoint_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        projective_column_sha256=hashlib.sha256(Path(__file__).with_name('closure_projective_interval_column.py').read_bytes()).hexdigest(),
        source_enclosure_sha256=hashlib.sha256(Path(__file__).with_name('closure_real_head_source_enclosure.py').read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['The source-to-state bound is validated only for the explicitly computed modal window, not for j>46.',
            'R18 nonlinear low far errors and high far traces require their own coupled boundary correction.',
            'The output high-frequency shallow heights are free to change when the full nonlinear problem is solved.',
            'The saved binary node-12 heights define the exact linear reference; they do not enclose a numerical entire nonlinear trajectory.',
            'The current outer physical cut and prefix still require their separate real-source and matching interfaces.'])
    out=Path(str(args.out_prefix)+'.json.gz')
    encoded=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(encoded)>=5_000_000:raise ArithmeticError('Repository file cap exceeded')
    out.write_bytes(encoded)
    summary={k:v for k,v in result.items() if k not in ('gamma_log2_upper','response_rows','input_hashes')}
    summary.update(first_cell=response[0],output=str(out),output_bytes=len(encoded),
        output_sha256=hashlib.sha256(encoded).hexdigest())
    Path(str(args.out_prefix)+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(output=str(out),max_relative_response=str(eta),
        projected_gate=projected_gate,first_response=response[0]['log2_response_bound']['display'],
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
