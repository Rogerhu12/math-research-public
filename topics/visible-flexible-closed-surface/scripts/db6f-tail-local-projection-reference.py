#!/usr/bin/env python3
"""High-precision local projection diagnostics, not an interval certificate.

At most four fixed inputs; no root, RHS, RK, flow, or new engine. Decimal
80/120 digit stability is numerical evidence, not an outward error bound.
Both table models freeze identical binary E,w2,p,pt,L,U coefficients.
"""
import argparse
from decimal import Decimal as D, localcontext
import gzip
import hashlib
import json
from pathlib import Path
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def bd(value):
    return D.from_float(float(value))


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def pi_decimal(prec):
    with localcontext() as context:
        context.prec = prec + 20
        threshold = D(10) ** (-prec - 14)

        def atan_inverse(n):
            x = D(1) / n
            x2, term, total, k = x*x, x, x, 1
            while True:
                term *= -x2
                add = term / (2*k+1)
                total += add
                if abs(add) < threshold:
                    return total
                k += 1

        return 16*atan_inverse(5)-4*atan_inverse(239)


def sincos_decimal(x, prec):
    x2 = x*x
    ss, cc, st, ct = x, D(1), x, D(1)
    threshold = D(10) ** (-prec - 12)
    for k in range(1, 4*prec):
        st *= -x2 / ((2*k)*(2*k+1))
        ct *= -x2 / ((2*k-1)*(2*k))
        ss += st
        cc += ct
        if max(abs(st), abs(ct)) < threshold:
            return ss, cc
    raise RuntimeError('Diagnostic trigonometric Taylor iteration cap')


def basis_for(raw, model, prec):
    M, N, spacing = raw['modes'], raw['quadrature'], raw['spacing']
    if model == 'rounded-table':
        return [[bd(v) for v in row] for row in raw['cs']], \
               [[bd(v) for v in row] for row in raw['sn']]
    assert model == 'ideal-grid' and N % 4 == 0
    with localcontext() as context:
        context.prec = prec + 18
        pi, sq2, quarter = pi_decimal(prec), D(2).sqrt(), N//4
        base = [sincos_decimal(2*pi*k/N, prec) for k in range(quarter)]
        sin, cos = [], []
        for k in range(N):
            q, r = divmod(k, quarter)
            s, c = base[r]
            sine, cosine = ((s,c),(c,-s),(-s,-c),(-c,s))[q]
            sin.append(sine)
            cos.append(cosine)
        cs, sn = [], []
        for n in range(N):
            indices = [(spacing*j*n) % N for j in range(1, M+1)]
            cs.append([D(1)]+[sq2*cos[k] for k in indices])
            sn.append([sq2*sin[k] for k in indices])
        return cs, sn


def reference(case, raw_basis, model, prec, cache):
    key = (case['basisKey'], model, prec)
    if key not in cache:
        cache[key] = basis_for(raw_basis, model, prec)
    cs, sn = cache[key]
    pnt, coeff = case['point'], case['frozenCoefficients']
    M, N = pnt['options']['modes'], pnt['options']['quadrature']
    J = M+1
    with localcontext() as context:
        context.prec = prec
        L, p, pt, Uc = ([bd(v) for v in coeff[name]] for name in ('L','p','pt','U'))
        E, v = bd(pnt['geometry']['E']), bd(pnt['geometry']['w2'])
        quad, q2sum, flux, uksum = [D(0)]*J, [D(0)]*J, [D(0)]*M, [D(0)]*M
        B, BL = [D(0)]*(J*J), [D(0)]*(J*J)
        minimum = {k: D('Infinity') for k in ('A','D','S')}
        for n in range(N):
            c, si = cs[n], sn[n]
            P = sum((p[j]*si[j] for j in range(M)), D(0))
            Pt = sum((pt[j+1]*c[j+1] for j in range(M)), D(0))
            Lv = L[0] + sum((L[j+1]*c[j+1] for j in range(M)), D(0))
            U = sum((Uc[j]*si[j] for j in range(M)), D(0))
            K = Lv-Pt
            T = 2*K+K*K+E*P*P
            u, S, A = v*T, 1-v*P*P, 1+Lv+v*Pt
            disc = 1-u
            for k, z in (('A',A),('D',disc),('S',S)):
                minimum[k] = min(minimum[k], z)
            assert min(A,disc,S) > bd(pnt['options']['projectionFloor'])
            sd = disc.sqrt()
            fc = u*(2+sd)/(2*sd*(1+sd)*(1+sd))
            gc = v*(P*P+S*T/(1+sd))/(S*sd)
            q2 = (Lv*Lv+E*P*P-Pt*Pt)/2
            q = q2+T*fc+(1+K)*Pt*gc
            am = Lv+v*Pt
            bm = am+(1+am)*(1/(disc*sd)-1)
            UK = U*K
            nonlinear_flux = UK+U*(1+K)*gc
            for i in range(J):
                quad[i] += q*c[i]
                q2sum[i] += q2*c[i]
                for j in range(i+1):
                    weight = c[i]*c[j]
                    B[i*J+j] += bm*weight
                    BL[i*J+j] += Lv*weight
            for j in range(M):
                flux[j] += nonlinear_flux*si[j]
                uksum[j] += UK*si[j]
        quad, q2sum = [z/N for z in quad], [z/N for z in q2sum]
        flux, uksum = [z/N for z in flux], [z/N for z in uksum]
        for i in range(J):
            for j in range(i+1):
                B[i*J+j] = (D(1) if i==j else D(0)) + B[i*J+j]/N
                BL[i*J+j] /= N
                B[j*J+i] = B[i*J+j]
                BL[j*J+i] = BL[i*J+j]
        return dict(quad=quad, moments=[L[j]+quad[j] for j in range(J)], B=B,
                    nonlinearFlux=flux, q2=q2sum, BL=BL, UK=uksum,
                    physicalNonlinearMomentumRHS=[bd(f)*z for f,z in zip(case['physicalFluxMultipliers'],flux)],
                    minimum=minimum)


def difference(left, right):
    return [bd(x)-y for x,y in zip(left,right)]


def stats(diff, rows=None):
    if not diff:
        return {'maximum_absolute':'0'}
    index = max(range(len(diff)), key=lambda j: abs(diff[j]))
    out = dict(maximum_absolute=str(abs(diff[index])), maximum_index=index,
               highest_four_maximum_absolute=str(max(abs(v) for v in diff[-4:])),
               last_component_absolute=str(abs(diff[-1])))
    if rows:
        out['maximum_absolute_row_sum'] = str(max(sum(abs(v) for v in diff[i*rows:(i+1)*rows])
                                                   for i in range(rows)))
    return out


def serialize_reference(ref):
    return {k:({a:str(b) for a,b in v.items()} if isinstance(v,dict) else [str(z) for z in v])
            for k,v in ref.items()}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--summary', type=Path, required=True)
    ap.add_argument('--precision-low', type=int, default=80)
    ap.add_argument('--precision-high', type=int, default=120)
    args = ap.parse_args()
    assert 40 <= args.precision_low < args.precision_high <= 200
    if args.out.exists() or args.summary.exists():
        raise FileExistsError('Refusing to overwrite diagnostic results')
    data = read(args.input)
    assert 1 <= len(data['values']) <= 4
    start, cache, cases, summaries = time.monotonic(), {}, [], []
    quantities = ['quad','moments','B','nonlinearFlux','physicalNonlinearMomentumRHS']
    isolated = {'q2OriginalNumeric':'q2','q2RewrittenNumeric':'q2','q2Analytic':'q2',
                'BLnumeric':'BL','BLanalytic':'BL','UKnumeric':'UK','UKanalytic':'UK'}
    for case in data['values']:
        per_model, high_refs = {}, {}
        J = case['point']['options']['modes']+1
        with localcontext() as context:
            context.prec = args.precision_high+10
            for model in ('rounded-table','ideal-grid'):
                low = reference(case,data['bases'][case['basisKey']],model,args.precision_low,cache)
                high = reference(case,data['bases'][case['basisKey']],model,args.precision_high,cache)
                stability = {key: stats([a-b for a,b in zip(low[key],high[key])], J if key in ('B','BL') else None)
                             for key in quantities+['q2','BL','UK']}
                errors = {}
                for method in ('original','algebraSameTable','analyticLowProjection'):
                    errors[method] = {key:stats(difference(case[method][key],high[key]),J if key=='B' else None)
                                      for key in quantities}
                polynomial_errors = {key:stats(difference(case['isolatedPolynomials'][key],high[ref]),
                                                      J if ref=='BL' else None)
                                     for key,ref in isolated.items()}
                per_model[model] = dict(reference_precision_difference=stability,
                    methods=errors, isolated_polynomials=polynomial_errors)
                high_refs[model] = high
            table_effect = {key:stats([a-b for a,b in zip(high_refs['rounded-table'][key],high_refs['ideal-grid'][key])],
                                        J if key in ('B','BL') else None)
                            for key in quantities+['q2','BL','UK']}
            method_change = {key:stats([bd(a)-bd(b) for a,b in zip(case['analyticLowProjection'][key],case['original'][key])],
                                           J if key=='B' else None) for key in quantities}
            ideal = per_model['ideal-grid']['methods']
            stability_max = max(D(v['maximum_absolute']) for m in per_model.values()
                                for v in m['reference_precision_difference'].values())
            scale = case['originalScale']
            summary = dict(id=case['id'],root_status=case['point']['origin'],
                original_scale=scale,guard=case['guard'],pointwiseMagnitudes=case['pointwiseMagnitudes'],
                ideal_reference_quad_highest_mode=str(high_refs['ideal-grid']['quad'][-1]),
                ideal_reference_q2_highest_mode=str(high_refs['ideal-grid']['q2'][-1]),
                maximum_reference_precision_difference=str(stability_max),
                ideal_grid_max_errors={method:{k:z['maximum_absolute'] for k,z in item.items()}
                                      for method,item in ideal.items()},
                ideal_grid_highest_four_quad_errors={method:item['quad']['highest_four_maximum_absolute']
                                                    for method,item in ideal.items()},
                ideal_grid_highest_quad_error={method:item['quad']['last_component_absolute']
                                               for method,item in ideal.items()},
                new_minus_old={key:z['maximum_absolute'] for key,z in method_change.items()},
                table_effect={key:z['maximum_absolute'] for key,z in table_effect.items()},
                maximum_new_moment_change_over_original_scale=None if scale is None else
                    str(D(method_change['moments']['maximum_absolute'])/bd(scale)))
            cases.append(dict(id=case['id'],models=per_model,
                high_precision_references={key:serialize_reference(val) for key,val in high_refs.items()},
                rounded_table_minus_ideal_grid=table_effect,new_minus_old=method_change))
            summaries.append(summary)
        print(json.dumps(dict(point=case['id'],finished=True,
            ideal_errors=summary['ideal_grid_max_errors'],reference_precision_difference=summary['maximum_reference_precision_difference'])),flush=True)
    meta=dict(status='COMPLETED-numerical-local-projection-comparison-NOT-an-interval-certificate',scope=__doc__,
        input=str(args.input),input_sha256=sha(args.input),script_sha256=sha(__file__),
        precisions=[args.precision_low,args.precision_high],input_definition=data['values'][0]['inputDefinition'],
        original_root_calls_in_this_script=0,new_engine_implemented=False,global_solver_run=False,
        seconds=time.monotonic()-start)
    report={**meta,'cases':cases}
    encoded=gzip.compress((json.dumps(report,indent=2)+'\n').encode(),mtime=0)
    if len(encoded)>=5_000_000:
        raise ValueError('Diagnostic output exceeds per-file limit')
    args.out.write_bytes(encoded)
    summary={**meta,'full_report':str(args.out),'full_report_sha256':sha(args.out),'cases':summaries}
    args.summary.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(finished=True,points=len(cases),seconds=meta['seconds'],
                         bytes=len(encoded),sha256=sha(args.out))),flush=True)


if __name__ == '__main__':
    main()
