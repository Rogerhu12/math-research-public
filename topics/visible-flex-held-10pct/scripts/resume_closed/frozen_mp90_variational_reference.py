#!/usr/bin/env python3
"""Independent variational readout on the already saved three MP90 trajectories.

Preparation only checks immutable sources, event identities and array shapes.
The separately authorized run evaluates analytic partial derivatives and linear
systems at the saved state/L values. It never calls the nonlinear RHS, Newton
root solver, nonlinear RK flow, original engine, native library, tail or BVP.

This is a finite numerical reference for the implicit moment-equation Jacobian
at the saved approximate roots. It is not the derivative of finite stopping
rules and is not a continuous-flow or geometric certificate.
"""
import argparse
import ast
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys
import time

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[4]
CAPSULE_SUMMARY = WORK / 'n4_work/parts32-frozen-mp-baseline-v1/capsule-summary.json'
CAPSULE_SUMMARY_SHA = '3785fff5412ec751d2275d3f774b6c7503bfecb7ad781a38068f811f06ab35f7'
MP90_SUMMARY = WORK / 'n4_work/parts32-frozen-mp90-v1/readout-summary.json'
MP90_SUMMARY_SHA = '316203483014a16efb7a9793c62e2c903e0925a946cd9a30a7ed869b76f766e6'
BASELINE = WORK / 'n4_work/parts32-frozen-mp-baseline-v1/float-summary.json'
MP90_RAW_SHA = 'bd5af94f99245a6404d9e0e6df178e82f9c2120ae1389f9c59b2b386c80e05d6'
COEFFICIENT_SHA = 'e7152958611721905b239ad4bbdda10b54a58459a8dbd153fb02db159fde283a'
BASELINE_SHA = 'c188de016b4963b1db896df9d3c2a7f09da201f66834acfd317f651c4488f4dc'
ORIGINAL_EVALUATOR_SHA = 'a4e5297beb66c218b0b716ff27992830f2d5db6a56655ffab76c9a9b7a4af819'
OBSERVER = HERE.parent / 'resume_n4/observe_command_live.py'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def load(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def payload_sha(value):
    raw = json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def write_json(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def binary_key(value):
    return struct.pack('<d', float(value))


def check_ref(item):
    if sha(item['path']) != item['sha256']:
        raise ValueError('Frozen input/source changed: ' + item['path'])


def package_sources():
    # find_spec does not execute mpmath or any mathematical evaluator.
    spec = importlib.util.find_spec('mpmath')
    if spec is None or spec.origin is None:
        raise ValueError('The bound mpmath package is unavailable')
    root = Path(spec.origin).resolve().parent
    return {str(path): sha(path) for path in sorted(root.rglob('*.py'))}


def immutable_inputs():
    for path, expected in ((CAPSULE_SUMMARY, CAPSULE_SUMMARY_SHA),
                           (MP90_SUMMARY, MP90_SUMMARY_SHA),
                           (BASELINE, BASELINE_SHA)):
        if sha(path) != expected:
            raise ValueError('Different original summary: ' + str(path))
    cs, ms, bs = load(CAPSULE_SUMMARY), load(MP90_SUMMARY), load(BASELINE)
    if (not bs['all_original_operands_and_judgments_bitwise_identical'] or
            not bs['all_three_outputs42_bitwise_identical'] or
            bs['source_sha256'] != ORIGINAL_EVALUATOR_SHA or
            bs['capsule_summary_sha256'] != CAPSULE_SUMMARY_SHA):
        raise ValueError('Different original exact float-baseline identity')
    if cs['coefficients']['sha256'] != COEFFICIENT_SHA or ms['raw']['sha256'] != MP90_RAW_SHA:
        raise ValueError('Different frozen coefficients or MP90 trajectory')
    for item in (cs['coefficients'], cs['reference'], ms['raw']):
        check_ref(item)
    if (ms['precision'] != 'mp' or ms['dps'] != 90 or
            ms['capsule_summary_sha256'] != CAPSULE_SUMMARY_SHA or
            ms['validated_baseline_sha256'] != BASELINE_SHA or
            ms['source_sha256'] != ORIGINAL_EVALUATOR_SHA):
        raise ValueError('MP90 summary no longer binds the original exact baseline')
    sources = {}
    for key in ('source_sha256', 'additional_original_root_sources'):
        for path, digest in cs[key].items():
            if sha(path) != digest:
                raise ValueError('Original frozen source changed: ' + path)
            sources[path] = digest
    for item in cs['traced_source'].values():
        check_ref(item)
        sources[item['path']] = item['sha256']
    capsule, raw = load(cs['coefficients']['path']), load(ms['raw']['path'])
    if (raw['precision'] != 'mp' or raw['dps'] != 90 or
            raw['mpmath_version'] != '1.3.0' or
            raw['source_sha256'] != ORIGINAL_EVALUATOR_SHA or
            raw['original_coefficients'] != cs['coefficients'] or
            raw['capsule_summary_sha256'] != CAPSULE_SUMMARY_SHA or
            raw['validated_baseline_sha256'] != BASELINE_SHA or
            raw['original_root_rules'] != capsule['root_rules']):
        raise ValueError('MP90 raw provenance differs from its original definition')
    if ((capsule['modes'], capsule['spacing'], capsule['steps'],
         capsule['quadrature'], capsule['independent_quadrature_nodes'],
         capsule['original_tail_gate']) != (20, 4, 16, 512, 128, 2e-9) or
            [f['stage'] for f in capsule['fixtures']] != [43, 38, 175] or
            [r['stage'] for r in raw['rows']] != [43, 38, 175]):
        raise ValueError('Only the authorized three original stages are supported')
    return cs, ms, capsule, raw, sources


def trajectory_records(fixture, row, M=20):
    """Parse identity/provenance only; no MP arithmetic or RHS evaluation.

    The accepted current L belongs to the needJac=True evaluation attached to
    root_stop. On a fallback it is NOT the last rejected line-search trial L.
    The current saved MP90 data have no fallbacks; this parser still distinguishes
    the two cases explicitly rather than guessing from the last evaluate event.
    """
    expected = [(profile, step, label, x)
                for profile, grid in enumerate(fixture['grid'])
                for step, point in enumerate(grid)
                for label, x in zip('abcd', (point['x'], point['x'] + point['h']/2,
                                            point['x'] + point['h']/2,
                                            point['x'] + point['h']))]
    records, current, evaluation, stop, fallback = [], None, None, None, None
    for index, event in enumerate(row['events']):
        kind = event['event']
        if kind == 'rk_field':
            if current is not None or len(records) >= len(expected):
                raise ValueError('Missing or duplicate root return')
            profile, step, label, x = expected[len(records)]
            if ((event['profile'], event['step'], event['label']) != (profile, step, label) or
                    binary_key(event['x']) != binary_key(x)):
                raise ValueError('Saved RK field identity/order differs from original grid')
            current = dict(stage=fixture['stage'], profile=profile, step=step,
                           label=label, x_binary64_hex=float(x).hex(),
                           rk_field_event=index, x=x)
            evaluation = stop = fallback = None
        elif kind == 'root_start':
            if current is None or 'state' in current or binary_key(event['x']) != binary_key(current['x']):
                raise ValueError('Missing or repeated saved root_start')
            if len(event['state']) != 2*M+2 or len(event['target']) != M+1:
                raise ValueError('Saved root state/target shape changed')
            current.update(state=event['state'], target=event['target'], root_start_event=index)
        elif kind == 'evaluate_start':
            if current is None or 'state' not in current:
                raise ValueError('An evaluation is not attached to its actual root state')
            if len(event['L']) != M+1 or event['Q'] != current['state'][:M]:
                raise ValueError('Saved L shape or Q identity differs from root_start')
            evaluation = dict(L=event['L'], needJac=event['needJac'],
                              evaluate_start_event=index, ended=False)
        elif kind == 'evaluate_end':
            if evaluation is None:
                raise ValueError('evaluate_end without evaluate_start')
            evaluation['ended'] = True
        elif kind == 'root_stop':
            if evaluation is None or not evaluation['needJac'] or not evaluation['ended']:
                raise ValueError('root_stop does not follow the full current-root evaluation')
            stop = dict(**evaluation, iteration=event['iteration'], accepted=event['accepted'],
                        err=event['err'], scale=event['scale'],
                        root_stop_event=index)
            fallback = None
        elif kind == 'fallback_judgment':
            fallback = event
        elif kind == 'root_return':
            if current is None or stop is None or event['iteration'] != stop['iteration']:
                raise ValueError('Root return/current-root identity mismatch')
            is_fallback = bool(event['roundoffFallback'])
            if (not is_fallback and not stop['accepted']) or (
                    is_fallback and (fallback is None or not fallback['accepted'])):
                raise ValueError('Saved root return has no corresponding original acceptance')
            if event['err'] != stop['err'] or event['scale'] != stop['scale']:
                raise ValueError('Root return residual/scale does not match current root_stop')
            current.update(L=stop['L'], accepted_evaluate_event=stop['evaluate_start_event'],
                           root_stop_event=stop['root_stop_event'], root_return_event=index,
                           original_iteration=stop['iteration'],
                           original_roundoff_fallback=is_fallback,
                           original_err=event['err'], original_scale=event['scale'])
            records.append(current)
            current = evaluation = stop = fallback = None
    if current is not None or len(records) != len(expected) or len(records) != 64:
        raise ValueError('The complete original 64-root trajectory was not recovered')
    outcomes = [dict(iteration=r['original_iteration'], err=r['original_err'],
                     scale=r['original_scale'], fallback=r['original_roundoff_fallback'])
                for r in records]
    if outcomes != row['root_outcomes'] or any(x['fallback'] for x in outcomes):
        raise ValueError('Different original MP90 root outcomes')
    return records


def trajectory_summary(records):
    return dict(stage=records[0]['stage'], original_roots=len(records),
                original_RK_steps=len(records)//4,
                root_state_and_L_identity_sha256=payload_sha(records),
                original_fallbacks=sum(r['original_roundoff_fallback'] for r in records),
                original_max_root_iterations=max(r['original_iteration'] for r in records))


def prepare(directory):
    cs, ms, cap, raw, sources = immutable_inputs()
    records = [trajectory_records(f, r) for f, r in zip(cap['fixtures'], raw['rows'], strict=True)]
    directory = Path(directory).resolve()
    directory.mkdir(parents=True, exist_ok=False)
    sources[str(Path(__file__).resolve())] = sha(__file__)
    sources[str(OBSERVER)] = sha(OBSERVER)
    plan = dict(scope=__doc__,source=ref(__file__),source_sha256=sources,
        capsule_summary=ref(CAPSULE_SUMMARY),mp90_summary=ref(MP90_SUMMARY),
        original_validated_float_baseline=ref(BASELINE),
        coefficients=cs['coefficients'],saved_mp90_raw=ms['raw'],
        mpmath_sources=package_sources(),mpmath_version='1.3.0',derivative_dps=90,
        trajectories=[trajectory_summary(r) for r in records],
        output_prefix=str(directory/'reference'),
        state_convention='Restore saved MP90 decimal strings at the same90-digit precision; static float coefficients enter mpf from their exact binary64 values.',
        derivative_convention='Analytic local partials and pivoted-LU implicit linear systems at saved approximate roots; no derivative of finite Newton stopping decisions.',
        independence='Explicit quotient/chain partials, not native dual code; pivoted MP LU, not native Cholesky. No native library is imported.',
        RK_convention='Only variational RK along the saved a/b/c/d states and L values. b and c remain separate even at the same abscissa.',
        port_convention='Tangent input columns are the original stage input. Later physical comparison divides output pi rows by portRatio only; no input-column rescaling.',
        precision_scope='Numerical variational reference at an already approximate90-digit trajectory. No interval/continuous-flow assertion.',
        metadata_only=True,new_derivative_evaluations=False,
        nonlinear_flow_or_root_invoked=False,original_MP_trajectory_rerun=False,
        native_library_loaded=False,tail_or_BVP_invoked=False)
    plan['identity_sha256'] = payload_sha(plan)
    path = directory/'plan.json'
    write_json(path, plan)
    command = [sys.executable, str(Path(__file__).resolve()), '--run-plan', str(path)]
    observer = [sys.executable, str(OBSERVER), '--out', str(directory/'resource.json'),
                '--log', str(directory/'process.log'), '--', *command]
    write_json(directory/'launch-command.json', dict(plan=ref(path), command=command,
                                                    observer_command=observer))
    print(json.dumps(dict(plan=ref(path), source_count=len(sources),
                          mpmath_source_count=len(plan['mpmath_sources']),
                          trajectories=plan['trajectories'],metadata_only=True,
                          no_new_mathematical_evaluation=True)), flush=True)


def explicit_local_partials(mp, Lv, P, Pt, E, W):
    """Independent analytic chain/quotient formulas; no dual/native code."""
    K = Lv-Pt
    T = 2*K+K*K+E*P*P
    u = W*T
    S = 1-W*P*P
    sd = mp.sqrt(1-u)
    den_fc = 2*sd*(1+sd)**2
    num_fc = u*(2+sd)
    fc = num_fc/den_fc
    inner_gc = P*P+S*T/(1+sd)
    den_gc = S*sd
    gc = W*inner_gc/den_gc
    q_partial = []
    for dK, dP, dPt in ((1, 0, 0), (0, 1, 0), (-1, 0, 1)):
        dT = 2*(1+K)*dK+2*E*P*dP
        du = W*dT
        dsd = -du/(2*sd)
        dS = -2*W*P*dP
        dnum_fc = du*(2+sd)+u*dsd
        dden_fc = 2*(1+sd)*(1+3*sd)*dsd
        dfc = (dnum_fc*den_fc-num_fc*dden_fc)/den_fc**2
        dinner_gc = (2*P*dP+(dS*T+S*dT)/(1+sd)-S*T*dsd/(1+sd)**2)
        dden_gc = dS*sd+S*dsd
        dgc = W*(dinner_gc*den_gc-inner_gc*dden_gc)/den_gc**2
        dq = (K*dK+E*P*dP+Pt*dK+K*dPt+fc*dT+T*dfc+
              Pt*gc*dK+(1+K)*gc*dPt+(1+K)*Pt*dgc)
        q_partial.append(dq)
    numerator = K+u/(1+sd)+W*P*P*sd
    factor = numerator/den_gc
    factor_partial = []
    for dK, dP in ((1, 0), (0, 1)):
        dT = 2*(1+K)*dK+2*E*P*dP
        du = W*dT
        dsd = -du/(2*sd)
        dS = -2*W*P*dP
        dn = dK+du/(1+sd)-u*dsd/(1+sd)**2+W*(2*P*sd*dP+P*P*dsd)
        dd = dS*sd+S*dsd
        factor_partial.append((dn*den_gc-numerator*dd)/den_gc**2)
    return q_partial, factor, factor_partial


def pivoted_linear_solve(mp, B, right):
    """One independently pivoted MP LU for every column; no SPD assumption."""
    perm, lower, upper = mp.lu(B)
    answer = perm*right
    J, columns = right.rows, right.cols
    for i in range(J):
        for col in range(columns):
            answer[i,col] = (answer[i,col]-
                mp.fsum(lower[i,k]*answer[k,col] for k in range(i)))/lower[i,i]
    for i in range(J-1, -1, -1):
        if upper[i,i] == 0:
            raise ValueError('Singular saved-root implicit linear system')
        for col in range(columns):
            answer[i,col] = (answer[i,col]-
                mp.fsum(upper[i,k]*answer[k,col] for k in range(i+1,J)))/upper[i,i]
    residual = B*answer-right
    scale = 1+max(abs(v) for v in right)
    return answer, max(abs(v) for v in residual)/scale, min(abs(upper[i,i]) for i in range(J))


class SavedTrajectoryVariational:
    def __init__(self, mp, capsule, fixture):
        self.mp = mp
        self.M = M = capsule['modes']
        self.K, self.J, self.size = 2*M, M+1, 2*M+2
        self.nq = capsule['independent_quadrature_nodes']
        self.frequency = [(j+1)*capsule['spacing'] for j in range(M)]
        self.cos = mp.matrix([[mp.mpf(float(v)) for v in row] for row in capsule['trig']['state_cos']])
        self.sin = mp.matrix([[mp.mpf(float(v)) for v in row] for row in capsule['trig']['state_sin']])
        self.floor = mp.mpf(float(capsule['root_rules']['floor']))
        self.coefficients = {}
        for point in fixture['points']:
            key = (point['profile'], binary_key(point['x']))
            values = {k: [mp.mpf(float(v)) for v in value] if isinstance(value,list)
                      else mp.mpf(float(value)) for k,value in point['coefficients'].items()}
            if key in self.coefficients and self.coefficients[key] != values:
                raise ValueError('Conflicting frozen coefficient lookup')
            self.coefficients[key] = values
        self.calls = 0
        self.max_linear_residual = mp.mpf(0)
        self.min_abs_pivot = mp.inf

    def jacobian_at_saved_root(self, record):
        mp, M, K, J, nq = self.mp, self.M, self.K, self.J, self.nq
        g = self.coefficients[(record['profile'], binary_key(record['x']))]
        state = [mp.mpf(value) for value in record['state']]
        L = [mp.mpf(value) for value in record['L']]
        a = [g['pNumerator'][j]/g['pDenominator'] for j in range(M)]
        p = [g['pNumerator'][j]*state[j]/g['pDenominator'] for j in range(M)]
        B, right = mp.eye(J), mp.matrix(J,K)
        for j in range(M):
            right[j+1,M+j] = g['targetFactor']
        angle_rows = []
        for n in range(nq):
            co, si = [self.cos[n,i] for i in range(J)], [self.sin[n,j] for j in range(M)]
            # Original accumulation order restores the local saved-root values;
            # the derivative formulas/linear solver below are independent.
            P, Pt, Lv, U = mp.mpf(0), mp.mpf(0), L[0], mp.mpf(0)
            for j in range(M):
                m = self.frequency[j]
                P += p[j]*si[j]
                Pt += m*p[j]*co[j+1]
                Lv += L[j+1]*co[j+1]
                U += (-m*L[j+1]+(m*m-1)*p[j])*si[j]
            kval = Lv-Pt
            D = 1-g['w2']*(2*kval+kval*kval+g['E']*P*P)
            S, A = 1-g['w2']*P*P, 1+Lv+g['w2']*Pt
            if not (D>self.floor and S>self.floor and A>self.floor):
                raise ValueError('The restored saved root is outside its original derivative domain')
            qp, factor, fp = explicit_local_partials(mp,Lv,P,Pt,g['E'],g['w2'])
            for i in range(J):
                for k in range(J):
                    B[i,k] += qp[0]*co[i]*co[k]/nq
            for j in range(M):
                chain = qp[1]*a[j]*si[j]+qp[2]*self.frequency[j]*a[j]*co[j+1]
                for i in range(J):
                    right[i,j] -= chain*co[i]/nq
            angle_rows.append((co,si,U,factor,fp))
        dL, lin_res, pivot = pivoted_linear_solve(mp,B,right)
        self.max_linear_residual = max(self.max_linear_residual,lin_res)
        self.min_abs_pivot = min(self.min_abs_pivot,pivot)
        dN = mp.matrix(M,K)
        for co,si,U,factor,fp in angle_rows:
            for col in range(K):
                dP = a[col]*si[col] if col<M else mp.mpf(0)
                dPt = self.frequency[col]*a[col]*co[col+1] if col<M else mp.mpf(0)
                dLv, dU = dL[0,col], mp.mpf(0)
                for j in range(M):
                    m = self.frequency[j]
                    dLv += dL[j+1,col]*co[j+1]
                    dU += (-m*dL[j+1,col]+((m*m-1)*a[j] if col==j else 0))*si[j]
                derivative_flux = dU*factor+U*(fp[0]*(dLv-dPt)+fp[1]*dP)
                for j in range(M):
                    dN[j,col] += derivative_flux*si[j]/nq
        result = mp.matrix(self.size,K)
        for j in range(M):
            m = self.frequency[j]
            for col in range(K):
                result[j,col] = g['sigma']*((m*m-4 if col==j else 0)+
                                            g['qLNumerator']*dL[j+1,col]/g['r3'])
                result[M+j,col] = ((4*g['sigma'] if col==M+j else 0)+
                    g['fluxPrefactor']*m*(-m*dL[j+1,col]+
                        ((m*m-1)*a[j] if col==j else 0)+dN[j,col]))
        for col in range(K):
            result[K,col] = g['meanFactor']*dL[0,col]
        # The last mean RHS is a frozen coefficient, so its derivative is zero.
        if any(not mp.isfinite(v) for v in result):
            raise ValueError('Nonfinite independent RHS Jacobian')
        self.calls += 1
        return result

    def variational_rk(self, fixture, records, progress):
        mp, K = self.mp, self.K
        tangent = mp.matrix(self.size,K)
        for j in range(K):
            tangent[j,j] = 1
        offset = 0
        for profile, grid in enumerate(fixture['grid']):
            for step, point in enumerate(grid):
                group = records[offset:offset+4]
                if [(r['profile'],r['step'],r['label']) for r in group] != [
                        (profile,step,label) for label in 'abcd']:
                    raise ValueError('Variational stage ordering differs from saved trajectory')
                h = mp.mpf(float(point['h']))
                derivatives = [self.jacobian_at_saved_root(r) for r in group]
                ka = derivatives[0]*tangent[:K,:]
                kb = derivatives[1]*(tangent+h*ka/2)[:K,:]
                kc = derivatives[2]*(tangent+h*kb/2)[:K,:]
                kd = derivatives[3]*(tangent+h*kc)[:K,:]
                tangent = tangent+h*(ka+2*kb+2*kc+kd)/6
                offset += 4
                progress(dict(profile=profile,step=step,derivative_sites=self.calls))
        if offset != len(records) or self.calls != 64:
            raise ValueError('Incomplete variational readout')
        return tangent


def run(plan_path):
    plan_path = Path(plan_path).resolve()
    plan = load(plan_path)
    identity = plan.pop('identity_sha256')
    if payload_sha(plan) != identity or plan['derivative_dps'] != 90:
        raise ValueError('The reviewed variational plan changed')
    plan['identity_sha256'] = identity
    for mapping in (plan['source_sha256'],plan['mpmath_sources']):
        for path,digest in mapping.items():
            if sha(path) != digest:
                raise ValueError('Bound derivative/library source changed: '+path)
    cs,ms,cap,raw,_ = immutable_inputs()
    records = [trajectory_records(f,r) for f,r in zip(cap['fixtures'],raw['rows'],strict=True)]
    if [trajectory_summary(r) for r in records] != plan['trajectories']:
        raise ValueError('Parsed original root-state/L identities changed')
    import mpmath
    if mpmath.__version__ != plan['mpmath_version']:
        raise ValueError('Different mpmath version')
    mp = mpmath.mp.clone()
    mp.dps = plan['derivative_dps']
    prefix = Path(plan['output_prefix'])
    raw_path, summary_path = Path(str(prefix)+'-raw.json.gz'),Path(str(prefix)+'-summary.json')
    event_path = Path(str(prefix)+'-progress.jsonl')
    if any(p.exists() for p in (raw_path,summary_path,event_path)):
        raise FileExistsError('Do not overwrite a mathematical execution')
    rows,summaries = [],[]
    began = time.monotonic()
    def emit(value):
        with event_path.open('a') as stream:
            stream.write(json.dumps(value,separators=(',',':'))+'\n')
        print(json.dumps(value,separators=(',',':')),flush=True)
    for fixture,saved in zip(cap['fixtures'],records,strict=True):
        engine = SavedTrajectoryVariational(mp,cap,fixture)
        stage_began = time.monotonic()
        tangent = engine.variational_rk(fixture,saved,lambda v:emit(dict(stage=fixture['stage'],**v)))
        serial = [[mp.nstr(tangent[i,j],mp.dps+8) for j in range(engine.K)]
                  for i in range(engine.size)]
        row = dict(stage=fixture['stage'],tangent42_by40=serial,
                   saved_trajectory_identity=trajectory_summary(saved),
                   tangent_serialization_sha256=payload_sha(serial))
        rows.append(row)
        summary = dict(stage=fixture['stage'],derivative_sites=engine.calls,
            seconds=time.monotonic()-stage_began,
            tangent_serialization_sha256=row['tangent_serialization_sha256'],
            maximum_absolute_entry=mp.nstr(max(abs(v) for v in tangent),32),
            maximum_scaled_implicit_linear_residual=mp.nstr(engine.max_linear_residual,32),
            minimum_absolute_pivot=mp.nstr(engine.min_abs_pivot,32),
            pivot_scope='An observed LU pivot, not a matrix condition estimate or rigorous lower bound.')
        checkpoint_path = Path(str(prefix)+f"-stage-{fixture['stage']}.json.gz")
        checkpoint = dict(plan=ref(plan_path),source=ref(__file__),row=row,summary=summary,
                          derivative_dps=mp.dps,nonlinear_flow_or_root_invoked=False)
        with checkpoint_path.open('xb') as stream:
            stream.write(gzip.compress((json.dumps(checkpoint,separators=(',',':'),
                allow_nan=False)+'\n').encode(),mtime=0))
        summary['stage_checkpoint'] = ref(checkpoint_path)
        summaries.append(summary)
        emit(dict(event='independent_variational_stage_finished',**summary))
    output = dict(plan=ref(plan_path),source=ref(__file__),derivative_dps=mp.dps,
                  mpmath_version=mpmath.__version__,rows=rows,
                  nonlinear_flow_or_root_invoked=False,
                  independent_derivative_evaluations=True,
                  saved_trajectory_recomputed=False,
                  scope=__doc__)
    encoded=(json.dumps(output,separators=(',',':'),allow_nan=False)+'\n').encode()
    with raw_path.open('xb') as stream:
        stream.write(gzip.compress(encoded,mtime=0))
    for mapping in (plan['source_sha256'],plan['mpmath_sources']):
        for path,digest in mapping.items():
            if sha(path) != digest:
                raise ValueError('A bound source changed during derivative evaluation: '+path)
    write_json(summary_path,dict(plan=ref(plan_path),source=ref(__file__),raw=ref(raw_path),
        named_results=summaries,seconds=time.monotonic()-began,
        derivative_dps=mp.dps,original_trajectory_dps=90,
        new_derivative_evaluations=True,nonlinear_flow_or_root_invoked=False,
        original_MP_trajectory_rerun=False,continuous_error_bound=False,
        native_comparison_performed=False,whole_tail_or_DN_invoked=False,
        scope='Finite implicit-equation variational reference on exactly paired saved approximate MP90 states and roots; not a derivative of the stopping algorithm.'))
    print(json.dumps(dict(summary=ref(summary_path),raw=ref(raw_path))),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    option=parser.add_mutually_exclusive_group(required=True)
    option.add_argument('--prepare',type=Path)
    option.add_argument('--run-plan',type=Path)
    args=parser.parse_args()
    if args.prepare is not None:
        prepare(args.prepare)
    else:
        run(args.run_plan)


if __name__ == '__main__':
    main()
