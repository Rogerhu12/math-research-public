#!/usr/bin/env python3
"""Two explicitly isolated float arithmetic variants on three frozen stages.

Arm A changes only the point-root unknown to ell=L-target and computes its
mathematically equivalent residual ell+quad(target+ell,Q). Arm B uses the same
root and additionally splits the RHS into its literal frozen-coefficient
linear matrix plus ell/nonlinear-flux terms. The original RK formula, V8
scalar functions, projection arithmetic, domains, tolerances and iteration
limits remain. No production, full-tail, or full-flow Jacobian is changed.
"""
import argparse
import gc
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys
import time
import traceback
import mpmath as mp

BASE_SHA256 = 'a4e5297beb66c218b0b716ff27992830f2d5db6a56655ffab76c9a9b7a4af819'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


BASE_PATH = Path(__file__).with_name('probe_frozen_stage_multiprecision.py')
if sha(BASE_PATH) != BASE_SHA256:
    raise ValueError('The exactly validated original finite evaluator changed')
spec = importlib.util.spec_from_file_location('frozen_stage_original', BASE_PATH)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


class ShiftedRootEngine(base.FrozenEngine):
    def __init__(self, capsule, fixture, arithmetic, arm):
        super().__init__(capsule, fixture, arithmetic)
        self.arm = arm
        self.current_ell = None

    def root(self, state, g, x):
        target = [self.zero]+[g['targetFactor']*state[self.M+j] for j in range(self.M)]
        ell = [self.zero for _ in range(self.J)]
        Q = state[:self.M]
        self.emit('shifted_root_start', state=list(state), x=x, target=target, ell=list(ell))
        for it in range(self.rules['iterations']):
            L = [target[j]+v for j, v in enumerate(ell)]
            e = self.evaluate(L, Q, g, True)
            residual = [v+e['quad'][j] for j, v in enumerate(ell)]
            err = max(map(abs, residual))
            formed_moment_err = max(abs(v-target[j]) for j, v in enumerate(e['moments']))
            scale = max(self.scale_floor, e['maxQuad'], *map(abs, target))
            threshold = self.tolerance*scale
            accepted = err <= threshold
            self.emit('shifted_root_stop', iteration=it, ell=list(ell), L=L, quad=list(e['quad']),
                      err=err, formedMomentErr=formed_moment_err, scale=scale,
                      tolerance=self.tolerance, threshold=threshold, accepted=accepted)
            if accepted:
                self.current_ell = list(ell)
                self.emit('shifted_root_return', iteration=it, err=err, scale=scale, roundoffFallback=False)
                self.root_outcomes.append(dict(iteration=it, err=err, formedMomentErr=formed_moment_err,
                                               scale=scale, fallback=False))
                return L, e
            # Same original point-root Newton matrix and Cholesky code. Under
            # the change of unknown dL=dell; no new inverse or tolerance is used.
            step = self.solve_spd(e['B'], residual)
            accepted = False
            for k, fac in enumerate(self.halves):
                trial = [v-fac*step[j] for j, v in enumerate(ell)]
                trial_L = [target[j]+v for j, v in enumerate(trial)]
                self.emit('shifted_trial_start', k=k, fac=fac, trialEll=trial, trialL=trial_L)
                try:
                    v = self.evaluate(trial_L, Q, g, False)
                    er = max(abs(z+v['quad'][j]) for j, z in enumerate(trial))
                    improves = er < err
                    tolerance_compared = not improves
                    within_tolerance = er <= threshold if tolerance_compared else None
                    accepted = improves or within_tolerance
                    self.emit('shifted_trial_judgment', k=k, er=er, err=err, scale=scale,
                              threshold=threshold, improves=improves,
                              tolerance_compared=tolerance_compared, within_tolerance=within_tolerance,
                              accepted=accepted)
                    if accepted:
                        ell = trial
                        break
                except Exception as error:
                    self.emit('shifted_trial_caught', k=k, message=str(error))
            if not accepted:
                threshold = self.fallback_tolerance*scale
                accepted = err <= threshold
                self.emit('shifted_fallback_judgment', err=err, scale=scale,
                          tolerance=self.fallback_tolerance, threshold=threshold, accepted=accepted)
                if accepted:
                    self.current_ell = list(ell)
                    self.emit('shifted_root_return', iteration=it, err=err, scale=scale, roundoffFallback=True)
                    self.root_outcomes.append(dict(iteration=it, err=err, formedMomentErr=formed_moment_err,
                                                   scale=scale, fallback=True))
                    return L, e
                raise RuntimeError('momentum Newton line search failed')
        raise RuntimeError('momentum Newton iteration limit')

    def rhs(self, state, profile, x):
        if self.arm == 'root-only':
            # Exact original source operation tree after the new root returns L.
            return super().rhs(state, profile, x)
        g = self.coefficients[(profile, base.packed([x]))]
        L, root = self.root(state, g, x)
        ell = list(self.current_ell)
        flux = [self.zero for _ in range(self.M)]
        # This nonlinear angular projection is the unchanged original formula.
        # It reads the represented total L through root rows; there is no extra
        # compensated projection, row splitting, or scalar precision change.
        for n, row in enumerate(root['rows']):
            K, P, sd, S, U = (row[key] for key in ('K', 'P', 'sd', 'S', 'U'))
            u = g['w2']*(self.two*K+K*K+g['E']*P*P)
            factor = (K+u/(self.one+sd)+g['w2']*P*P*sd)/(S*sd)
            f = U*factor
            for j in range(self.M):
                flux[j] += f*self.sin[n][j]/self.nq
        derivative = [self.zero for _ in range(self.size)]
        for j in range(self.M):
            m = self.frequency[j]
            # Literal frozen primitive coefficients only. In particular,
            # pref*targetFactor is NOT replaced with sigma.
            a11 = g['sigma']*(m*m-4)
            a12 = g['sigma']*g['qLNumerator']*g['targetFactor']/g['r3']
            a21 = g['fluxPrefactor']*m*(m*m-1)*g['pNumerator'][j]/g['pDenominator']
            a22 = 4*g['sigma']-g['fluxPrefactor']*m*m*g['targetFactor']
            q_correction = g['sigma']*g['qLNumerator']*ell[j+1]/g['r3']
            momentum_correction = g['fluxPrefactor']*m*(-m*ell[j+1]+flux[j])
            derivative[j] = a11*state[j]+a12*state[self.M+j]+q_correction
            derivative[self.M+j] = a21*state[j]+a22*state[self.M+j]+momentum_correction
        # target[0]=0, so the original mean formula is already an ell formula.
        derivative[2*self.M] = g['meanFactor']*L[0]
        derivative[2*self.M+1] = g['meanFactor']
        return derivative, root['minA'], root['minD']


def save_gz(path, data):
    path.write_bytes(gzip.compress((json.dumps(data, ensure_ascii=False)+'\n').encode(), mtime=0))
    return dict(path=str(path.resolve()), sha256=sha(path))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--capsule-summary', type=Path, required=True)
    p.add_argument('--float-baseline', type=Path, required=True)
    p.add_argument('--mp90-summary', type=Path, required=True)
    p.add_argument('--bridge', type=Path, required=True)
    p.add_argument('--node', default='node')
    p.add_argument('--arm', choices=('root-only','root-and-linear-split'), required=True)
    p.add_argument('--out-prefix', type=Path, required=True)
    a = p.parse_args()
    cs, original_baseline, mp_summary = base.load(a.capsule_summary), base.load(a.float_baseline), base.load(a.mp90_summary)
    if (not original_baseline['all_original_operands_and_judgments_bitwise_identical'] or
            not original_baseline['all_three_outputs42_bitwise_identical'] or
            original_baseline['source_sha256'] != BASE_SHA256 or
            original_baseline['capsule_summary_sha256'] != sha(a.capsule_summary) or
            mp_summary['validated_baseline_sha256'] != sha(a.float_baseline) or
            mp_summary['source_sha256'] != BASE_SHA256 or
            mp_summary['capsule_summary_sha256'] != sha(a.capsule_summary) or
            mp_summary['precision'] != 'mp' or mp_summary['dps'] != 90 or
            original_baseline['bridge_sha256'] != sha(a.bridge)):
        raise ValueError('The frozen exact baseline/MP90/source identities differ')
    for key in ('source_sha256','additional_original_root_sources'):
        for path,digest in cs[key].items():
            if sha(path) != digest: raise ValueError('A bound original source changed: '+path)
    for ref in (cs['coefficients'],cs['reference'],mp_summary['raw']):
        if sha(ref['path']) != ref['sha256']: raise ValueError('A frozen original input/readout changed')
    capsule = base.load(cs['coefficients']['path'])
    reference = base.load(cs['reference']['path'])
    original_states = {r['stage']:r['state'] for r in reference['rows']}
    del reference
    precise = base.load(mp_summary['raw']['path'])
    precise_states = {r['stage']:r['state'] for r in precise['rows']}
    del precise
    gc.collect()
    paths = {name:Path(str(a.out_prefix)+'-'+name+('.json' if name=='summary' else '.json.gz'))
             for name in ('raw','summary','failure')}
    for path in paths.values():
        if path.exists(): raise ValueError('A frozen result already exists: '+str(path))
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    context = dict(scope=__doc__,arm=a.arm,source_sha256=sha(__file__),base_source_sha256=BASE_SHA256,
        bridge_sha256=sha(a.bridge),capsule_summary=dict(path=str(a.capsule_summary.resolve()),sha256=sha(a.capsule_summary)),
        float_baseline=dict(path=str(a.float_baseline.resolve()),sha256=sha(a.float_baseline)),
        mp90_summary=dict(path=str(a.mp90_summary.resolve()),sha256=sha(a.mp90_summary)),
        command=sys.argv,root_rules=capsule['root_rules'],
        original_RK_unchanged=True,original_projection_unchanged=True,original_scalar_functions_unchanged=True,
        full_flow_jacobian_computed=False,complete_tail_solver_invoked=False,physical_checkpoint_written=False,
        production_source_changed=False,
        derivative_scope='Point-root Newton matrix code is inherited unchanged; ell-to-L has identity derivative. No new complete flow or tail Jacobian is computed. Arm B uses the literal frozen-coefficient linear matrix, including a22=4*sigma-pref*m*m*targetFactor; it makes no rounded-coefficient identity substitution.')
    arithmetic = base.V8Float(a.bridge,a.node)
    rows,scalars = [],[]
    mp.mp.dps = 140
    began = time.monotonic()
    try:
        for fixture in capsule['fixtures']:
            engine=ShiftedRootEngine(capsule,fixture,arithmetic,a.arm)
            start=time.monotonic()
            try:
                state,min_a,min_d=engine.flow(fixture)
            except Exception as error:
                save_gz(paths['failure'],dict(**context,stage=fixture['stage'],error=repr(error),
                    traceback=traceback.format_exc(),events=engine.events,root_outcomes=engine.root_outcomes))
                raise
            expected=[mp.mpf(v)for v in precise_states[fixture['stage']]]
            old=[mp.mpf(float(v))for v in original_states[fixture['stage']]]
            actual=[mp.mpf(float(v))for v in state]
            errors=[actual[j]-expected[j]for j in range(42)]
            old_errors=[old[j]-expected[j]for j in range(42)]
            scale=mp.mpf(float(fixture['normalizationScale']))
            ratio=mp.mpf(float(fixture['portRatio']))
            normalized=[abs(errors[j]if j<20 else errors[j]/ratio)/scale for j in range(40)]
            original_normalized=[abs(old_errors[j]if j<20 else old_errors[j]/ratio)/scale for j in range(40)]
            physical=[v if j<20 else v/fixture['portRatio']for j,v in enumerate(state[:40])]
            residual=[v-fixture['targetNode40'][j]for j,v in enumerate(physical)]
            target_norm=max(map(abs,residual))/fixture['normalizationScale']
            root_iterations={}
            for root in engine.root_outcomes:
                key=str(root['iteration']);root_iterations[key]=root_iterations.get(key,0)+1
            scalar=dict(stage=fixture['stage'],root_calls=len(engine.root_outcomes),
                root_iterations=root_iterations,root_fallbacks=sum(r['fallback']for r in engine.root_outcomes),
                max_stable_root_relative_residual=max(r['err']/r['scale']for r in engine.root_outcomes),
                max_formed_moment_root_relative_residual=max(r['formedMomentErr']/r['scale']for r in engine.root_outcomes),
                maximum_all42_error_to_mp90=mp.nstr(max(map(abs,errors)),32),
                maximum_original_all42_error_to_mp90=mp.nstr(max(map(abs,old_errors)),32),
                maximum_mean2_error_to_mp90=mp.nstr(max(map(abs,errors[40:])),32),
                maximum_normalized_physical_error_to_mp90=mp.nstr(max(normalized),32),
                maximum_original_normalized_physical_error_to_mp90=mp.nstr(max(original_normalized),32),
                mp_error_peak_component=max(range(40),key=lambda j:normalized[j]),
                fixed_target_normalized_residual=target_norm,
                fixed_target_peak_component=max(range(40),key=lambda j:abs(residual[j])),
                output42_sha256=base.numeric_sha(state),minA=min_a,minD=min_d,seconds=time.monotonic()-start)
            scalars.append(scalar)
            rows.append(dict(stage=fixture['stage'],state=state,residual=residual,events=engine.events,
                             root_outcomes=engine.root_outcomes))
            print(json.dumps(dict(event='shifted_stage_complete',**scalar)),flush=True)
    finally:
        arithmetic.close()
    raw=save_gz(paths['raw'],dict(**context,rows=rows))
    result=dict(**context,named_results=scalars,raw=raw,seconds=time.monotonic()-began,
                conclusion_scope='Only finite three-stage arithmetic accuracy against the frozen MP90 readout. A smaller fixed-target residual is not the selection criterion and supplies no tail or prefix acceptance.')
    paths['summary'].write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(event='terminal',summary=str(paths['summary'].resolve()),sha256=sha(paths['summary']))),flush=True)


if __name__=='__main__':main()
