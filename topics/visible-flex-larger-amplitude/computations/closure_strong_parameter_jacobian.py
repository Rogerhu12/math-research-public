#!/usr/bin/env python3
"""Stream the full paid R58 derivative in its exact W coordinates.

Every coefficient is a positive upper for the original complete641 operator
on rho=2^-30. The R57 support zeros and the actual R55/two-material source12
bounds are unchanged. Only linear algebra is prepared, not a new head solve.
The40-bit dyadic rounding is outward; no small nonzero entry is discarded.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import gc as garbage
import gzip
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx
from closure_real_head_source_enclosure import power2, ball_record
from closure_real_head_green_enclosure import ball
from closure_split_joint_io_v2 import digest, read, iter_array, metadata_without_array, label, validate_common
from closure_two_material_joint_verify import compact, labelled_power


def upward(value, bits=40):
    if not value >= 0:
        raise ArithmeticError('A positive derivative upper became negative or undecidable')
    top = value.upper()
    if top == 0:
        return [0, 0]
    m, e = top.man_exp()
    m, e = int(m), int(e)
    shift = max(0, m.bit_length()-bits)
    if shift:
        m, e = (m+(1 << shift)-1) >> shift, e+shift
    out = compact([m, e])
    if not out >= top:
        raise ArithmeticError('A compact positive endpoint was rounded inward')
    return [m, e]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('joint','low','split','density','low-edge','low-column','domain','lifts','out','summary'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--high-edge',type=Path,action='append',required=True)
    p.add_argument('--rss-limit-mib',type=int,default=120)
    args = p.parse_args(); ctx.prec = 192; start = time.monotonic()
    if args.out.exists() or args.summary.exists() or args.out.suffix != '.gz':
        raise FileExistsError('Use fresh compressed Jacobian and summary paths')
    paths = [getattr(args,k) for k in ('joint','low','split','density','low_edge','low_column','domain','lifts')]+args.high_edge
    hashes = {str(v):digest(v) for v in paths}
    joint, domain, lifts = read(args.joint), read(args.domain), read(args.lifts)
    if not joint['whole_head_closed'] or not all(joint['gates'].values()) or not domain['all_gates'] or not all(domain['gates'].values()):
        raise ValueError('The actual strong complete head and full parameter domain must already be paid')
    for k in ('low','split','density','low_edge','low_column'):
        path = str(getattr(args,k))
        if joint['input_hashes'].get(path) != hashes[path]:
            raise ValueError('An original actual R58 derivative input changed: '+k)
    for path in args.high_edge:
        if joint['input_hashes'].get(str(path)) != hashes[str(path)]:
            raise ValueError('A true mixed-material input changed')
    if (domain['input_hashes'].get(str(args.joint)) != hashes[str(args.joint)]
            or domain['input_hashes'].get(str(args.density)) != hashes[str(args.density)]
            or domain['rescaled_lifts']['path'] != str(args.lifts)
            or domain['rescaled_lifts']['sha256'] != hashes[str(args.lifts)]):
        raise ValueError('The actual parameter lift/domain identity differs')
    low, split, density = read(args.low), metadata_without_array(args.split,'gamma_rows'), read(args.density)
    cells = validate_common(low,split,density,hashes,args.density)
    N, dim, inf, zi = 213,641,639,640
    if cells != list(range(12,225)) or joint['dimension'] != dim or len(joint['rows']) != dim:
        raise ValueError('Every original coordinate and cell is required')
    W = []
    for i,row in enumerate(joint['rows']):
        if row['index'] != i or any(row[k] != v for k,v in label(i,N).items()):
            raise ValueError('A full641 coordinate was reordered')
        W.append(ball(row['metric_weight']))
        if not W[-1].is_exact() or not W[-1] > 0:
            raise ValueError('The exact original positive weight is required')
    rho, lam = ball(joint['physical_domain']), ball(domain['lambda_upper'])
    if rho != power2(-30) or lam != arb(3970)/4096:
        raise ValueError('The original uniform domain/upper bound changed')
    A = [ball(row['V_over_w_upper']).upper() for row in density['rows']]
    ns = [(3*rho+216*v*(1+rho)**2).upper() for v in A]
    zstar, CD = power2(split['z_log2']), labelled_power(low['raw_D_constant'])
    if zstar != ball(joint['independent_far_z']):
        raise ValueError('The independent true deep parameter normalization differs')
    column = read(args.low_column)
    if not column['full46_and_all_deeper_targets'] or column['target_cells'] != cells[1:] or column['modes'] != list(range(2,93,2)):
        raise ValueError('The full real radial source12 column is required')
    if column['input_hashes'].get(str(args.low_edge)) != hashes[str(args.low_edge)]:
        raise ValueError('The paid source-column integral changed')
    replacements = {}
    for row in column['rows']:
        k,n = row['output_cell']-12,row['source_cell']-12
        if n != 0 or not 1 <= k < N or row['complete_modes'] != list(range(2,93,2)):
            raise ValueError('A radial replacement range differs')
        if compact(low['gamma_upper']['corr'][k][n]) != ball(row['combined_corr']):
            raise ValueError('The old positive material comparison changed')
        replacements[(k,n)] = (ball(row['DQ_corr_from_low']).upper(),ball(row['DQ_corr_from_near']).upper())
    if len(replacements) != 212:
        raise ValueError('A deeper radial target was omitted')
    covers = {}
    for path in args.high_edge:
        doc = read(path)
        if doc['target_density_sha256'] != hashes[str(args.density)] or not doc['full_mean_inverse_remainder_unchanged'] or not doc['complete_quadratic_new_variation_unchanged']:
            raise ValueError('The independent near material has another full nonlinear scope')
        for band in doc['bands']:
            support = band['first_mode'],band['last_mode']
            for row in band['rows']:
                key = row['output_cell']-12,row['source_cell']-12
                if support in covers.setdefault(key,{}):
                    raise ValueError('A near comparison window was repeated')
                covers[key][support] = ball(row['gamma']['low_to_near_quadratic']).upper()
    expected = {(94,96),(98,104),(106,112),(114,128),(130,192)}
    if any(set(v) != expected for v in covers.values()) or not covers:
        raise ValueError('The complete actual near range is required')
    near_material = {k:max(v.values()) for k,v in covers.items()}
    families = ('main','corr','base','remainder')
    if any(len(low['gamma_upper'][f]) != N or any(len(r) != N for r in low['gamma_upper'][f]) for f in families):
        raise ValueError('The complete four low kernels are required')
    beta_low = [(ball(row['B_low']).upper()*4*CD*zstar*zstar).upper() for row in low['rows']]
    beta_z = (ball(low['E_B_low']).upper()*4*CD*zstar).upper()
    rows_written, all_coefficients, max_row = [],0,arb(0)
    seen = set()
    partial = args.out.with_suffix(args.out.suffix+'.partial')
    if partial.exists():
        raise FileExistsError('Do not overwrite a recoverable partial matrix')
    with gzip.open(partial,'wt',encoding='utf-8',compresslevel=6) as dst:
        dst.write('{"rows":[')
        def save_row(i, raw):
            nonlocal all_coefficients,max_row
            if i in seen or len(raw) != dim:
                raise ValueError('A complete original row was duplicated or shortened')
            seen.add(i); packed=[]; total=arb(0)
            for j,v in enumerate(raw):
                if not v >= 0:
                    raise ArithmeticError('A complete positive coefficient is invalid')
                if v == 0:
                    continue
                pair = upward((v*W[j]/W[i]).upper())
                packed.append([j,*pair]); total += compact(pair)
            total = total.upper()
            if not total < lam:
                raise ArithmeticError('Outward compact derivative lost the actual contraction margin')
            row = dict(index=i,**label(i,N),coefficients=packed,row_sum_upper=ball_record(total))
            if rows_written: dst.write(',')
            dst.write(json.dumps(row,separators=(',',':')))
            rows_written.append(dict(index=i,**label(i,N),entries=len(packed),row_sum_upper=ball_record(total)))
            max_row=max(max_row,total); all_coefficients+=len(packed)
            if len(rows_written)%32 == 0:
                print(json.dumps(dict(event='positive_derivative_rows',rows=len(rows_written),last_index=i,seconds=time.monotonic()-start,RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > args.rss_limit_mib*1024:
                raise MemoryError('The owned derivative job exceeded its explicit RSS cap')
        for k in range(N):
            row=[arb(0) for _ in range(dim)]
            for n in range(N):
                gm,gc,gq,gr=[compact(low['gamma_upper'][f][k][n]) for f in families]
                c0=(gm+3*gc).upper();cl=cn=c0
                if (k,n) in replacements:
                    dl,dn=replacements[(k,n)];cl=min(c0,(gm+dl).upper());cn=min(c0,(gm+dn).upper())
                ep=(3*rho*gq+216*(1+rho)**2*gr).upper()
                row[n]=(cl+ep).upper();row[N+n]=(cn+ep).upper();row[2*N+n]=ep;row[inf]+=ep
            row[inf]=row[inf].upper();row[zi]=beta_low[k];save_row(k,row)
        farrow=[arb(0) for _ in range(dim)]
        for n in range(N):
            fm,fc,fq,fr=[compact(low['far_z_source_upper'][f][n]) for f in families]
            f0=(fm+3*fc).upper();fe=(3*rho*fq+216*(1+rho)**2*fr).upper()
            farrow[n]=farrow[N+n]=((f0+fe)/zstar).upper();farrow[2*N+n]=(fe/zstar).upper();farrow[inf]+=fe/zstar
        farrow[inf]=farrow[inf].upper();farrow[zi]=beta_z;save_row(zi,farrow)
        del low,column;garbage.collect()
        count=0
        for k,data in enumerate(iter_array(args.split,'gamma_rows')):
            if data['output_cell'] != cells[k] or len(data['sources']) != N-k:
                raise ValueError('The complete causal output/source range differs')
            out={g:[arb(0) for _ in range(dim)] for g in ('near','rest')}
            for n,entry in enumerate(data['sources'],k):
                if entry['source_cell'] != cells[n]:
                    raise ValueError('The complete causal source position differs')
                for group in ('near','rest'):
                    h=ball(entry[group+'_gamma']).upper();c=(3*h).upper()
                    if group=='near' and (k,n) in near_material:c=min(c,near_material[(k,n)])
                    e=(h*ns[n]).upper();row=out[group]
                    row[n]=(c+e).upper() if group=='near' else e
                    row[N+n]=(c+e).upper();row[2*N+n]=(c+e).upper()
                    row[inf]+=e if group=='near' else c+e
                count+=1
            for group,offset in [('near',N),('rest',2*N)]:
                row=out[group];row[inf]=row[inf].upper();row[zi]=(4*ball(split['cells'][k]['far_boundary_'+group]).upper()).upper();save_row(offset+k,row)
        if count != N*(N+1)//2:raise ValueError('An original causal entry was omitted')
        hi=[arb(0) for _ in range(dim)];ghi=ball(density['gamma_high']).upper()
        for n in range(N):
            hi[n]=hi[N+n]=(ghi*ns[n]).upper();hi[2*N+n]=(ghi*(3+ns[n])).upper();hi[inf]+=ghi*(3+ns[n])
        hi[inf]=hi[inf].upper();hi[zi]=(4*ball(split['deep_high_boundary']).upper()).upper();save_row(inf,hi)
        if seen != set(range(dim)):raise ValueError('Not all641 original rows were saved')
        metadata=dict(status='Complete actual R58 derivative positive upper in the exact W metric',dimension=dim,
            mathematical_matrix='Jbar_ij >= J_ij W_j/W_i; every nonzero is rounded outward to40 significant dyadic bits, with no exponent cutoff.',
            all_rows_contracting=True,maximum_row_sum=ball_record(max_row),lambda_upper=ball_record(lam),
            parameter_domain=str(args.domain),parameter_domain_sha256=hashes[str(args.domain)],
            parameter_lifts=str(args.lifts),parameter_lifts_sha256=hashes[str(args.lifts)],
            physical_domain=joint['physical_domain'],independent_far_z=joint['independent_far_z'],
            metric_weights=[r['metric_weight'] for r in joint['rows']],
            row_order='Explicit original index; rows are streamed low,far,interleaved near/rest,infinite. Missing sparse entries are exact structural zeros only.',
            exact_supports=joint['exact_supports'],all46_low_directions_retained=True,
            complete_mean_inverse_quadratic_and_true_far_retained=True,
            original_causal_entry_count=count,stored_nonzero_coefficients=all_coefficients,
            input_hashes=hashes,source_sha256=digest(Path(__file__)),
            helper_hashes={name:digest(Path(__file__).with_name(name)) for name in ('closure_two_material_joint_verify.py','closure_split_joint_io_v2.py','closure_real_head_source_enclosure.py','closure_real_head_green_enclosure.py')},
            new_kernels=0,new_radial_integrations=0,new_matrix_inverses=0,
            elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        dst.write('],'+json.dumps(metadata,separators=(',',':'))[1:])
    if partial.stat().st_size>=5_000_000:raise ValueError('Matrix output exceeds the repository file cap')
    partial.rename(args.out)
    summary=dict(metadata,rows=rows_written,output=str(args.out),output_sha256=digest(args.out),bytes=args.out.stat().st_size)
    args.summary.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='done',rows=len(seen),entries=all_coefficients,maximum_row_sum=str(max_row),seconds=metadata['elapsed_seconds'],RSS_KiB=metadata['peak_RSS_KiB'],sha256=summary['output_sha256'],bytes=summary['bytes'])),flush=True)


if __name__=='__main__':main()
