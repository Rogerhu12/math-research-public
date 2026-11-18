#!/usr/bin/env python3
"""Read a frozen three-stage RK flow with a validated scalar-arithmetic port.

The float backend uses V8 sqrt/log1p/expm1 through the companion bridge and
must reproduce every original root judgment operand and all 3 x 42 outputs
bitwise. Multiprecision requires that exact baseline from this source version.
Static original binary64 geometry/coefficient/trig values are interpreted as
exact binary rationals. No profile/trig reevaluation, tail solve, Jacobian,
physical model mutation, or checkpoint update is performed.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import struct
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    p = Path(path)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix == '.gz' else p.read_text())


def packed(values):
    return struct.pack('<'+'d'*len(values), *values)


def numeric_sha(values):
    return hashlib.sha256(packed(values)).hexdigest()


def numeric_identity(value):
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, (float, int)):
        return ('binary64', struct.pack('<d', value).hex())
    if isinstance(value, list):
        return [numeric_identity(v) for v in value]
    if isinstance(value, dict):
        return {k: numeric_identity(value[k]) for k in sorted(value)}
    raise TypeError(type(value))


class V8Float:
    name = 'float64-with-original-v8-transcendentals'

    def __init__(self, bridge, node):
        self.process = subprocess.Popen([node, str(bridge), 'serve'], stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        self.requests = 0

    @staticmethod
    def make(value):
        return float(value)

    @staticmethod
    def public(value):
        return value

    def request(self, value):
        self.process.stdin.write(json.dumps(value, separators=(',', ':'))+'\n')
        self.process.stdin.flush()
        line = self.process.stdout.readline()
        if not line:
            raise RuntimeError('Original scalar bridge ended: '+self.process.stderr.read())
        self.requests += 1
        return json.loads(line)

    def root_transcendentals(self, rows, need_jac):
        out = self.request(dict(operation='root_rows', D=[r['D'] for r in rows],
                                u=[r['u'] for r in rows], needJac=need_jac))
        return out['sqrtD'], out['bmNonlinear']

    def sqrt(self, value):
        return self.request(dict(operation='sqrt', value=value))['value']

    def close(self):
        self.process.stdin.close()
        returncode = self.process.wait(timeout=10)
        error = self.process.stderr.read()
        self.process.stdout.close()
        self.process.stderr.close()
        if returncode != 0:
            raise RuntimeError('Original scalar bridge failed: '+error)


class MPArithmetic:
    name = 'mpmath-frozen-binary64-coefficients'

    def __init__(self, dps):
        import mpmath
        self.mp = mpmath.mp.clone()
        self.mp.dps = dps
        self.dps = dps
        self.version = mpmath.__version__
        self.requests = 0

    def make(self, value):
        # mpf(float) imports its exact binary64 value, not the printed decimal.
        return self.mp.mpf(float(value))

    def public(self, value):
        if value is None or isinstance(value, (str, bool, int)):
            return value
        if isinstance(value, list):
            return [self.public(v) for v in value]
        if isinstance(value, dict):
            return {k: self.public(v) for k, v in value.items()}
        return self.mp.nstr(value, self.dps+8)

    def root_transcendentals(self, rows, need_jac):
        sqrt_d = [self.mp.sqrt(r['D']) for r in rows]
        bm = [self.mp.expm1(-self.make(1.5)*self.mp.log1p(-r['u'])) for r in rows] if need_jac else None
        return sqrt_d, bm

    def sqrt(self, value):
        return self.mp.sqrt(value)

    def close(self):
        pass


class DomainFailure(RuntimeError):
    pass


class FrozenEngine:
    """Original sequential projected root, split flux, and ordinary RK formulas."""

    def __init__(self, capsule, fixture, arithmetic):
        self.backend = b = arithmetic
        self.M = capsule['modes']
        self.J = self.M+1
        self.size = 2*self.M+2
        self.nq = capsule['independent_quadrature_nodes']
        self.frequency = [(j+1)*capsule['spacing'] for j in range(self.M)]
        self.cos = [[b.make(v) for v in row] for row in capsule['trig']['state_cos']]
        self.sin = [[b.make(v) for v in row] for row in capsule['trig']['state_sin']]
        self.rules = capsule['root_rules']
        self.floor = b.make(self.rules['floor'])
        self.tolerance = b.make(self.rules['tolerance'])
        self.fallback_tolerance = b.make(self.rules['fallback_tolerance'])
        self.scale_floor = b.make(self.rules['scale_floor'])
        self.halves = [b.make(v) for v in self.rules['halving_factors']]
        self.zero = b.make(0)
        self.one = b.make(1)
        self.two = b.make(2)
        self.half = b.make(.5)
        self.infinity = float('inf')
        self.events = []
        self.root_outcomes = []
        self.coefficients = {}
        for point in fixture['points']:
            key = (point['profile'], packed([point['x']]))
            converted = {name: [b.make(v) for v in value] if isinstance(value, list) else b.make(value)
                         for name, value in point['coefficients'].items()}
            if key in self.coefficients and self.coefficients[key] != converted:
                raise ValueError('Inconsistent duplicate original coefficient point')
            self.coefficients[key] = converted

    def emit(self, event, **values):
        self.events.append(dict(event=event, **self.backend.public(values)))

    def evaluate(self, L, Q, g, need_jac=True):
        self.emit('evaluate_start', L=list(L), Q=list(Q), needJac=need_jac)
        M, J, nq = self.M, self.J, self.nq
        p = [g['pNumerator'][j]*Q[j]/g['pDenominator'] for j in range(M)]
        pt = [self.zero]+[self.frequency[j]*p[j] for j in range(M)]
        quad = [self.zero for _ in range(J)]
        B = [[self.zero for _ in range(J)] for _ in range(J)]
        if need_jac:
            for i in range(J):
                B[i][i] = self.one
        rows = []
        min_d = min_s = min_a = self.infinity
        max_quad = self.zero
        for n in range(nq):
            P = Pt = U = self.zero
            Lv = L[0]
            co, si = self.cos[n], self.sin[n]
            for j in range(M):
                m = self.frequency[j]
                P += p[j]*si[j]
                Pt += pt[j+1]*co[j+1]
                Lv += L[j+1]*co[j+1]
                U += (-m*L[j+1]+(m*m-1)*p[j])*si[j]
            K = Lv-Pt
            T = self.two*K+K*K+g['E']*P*P
            u = g['w2']*T
            D = self.one-u
            S = self.one-g['w2']*P*P
            A = self.one+Lv+g['w2']*Pt
            dp = D > self.floor
            sp = S > self.floor if dp else None
            ac = dp and sp
            ap = A > self.floor if ac else None
            self.emit('domain', n=n, D=D, S=S, A=A, floor=self.floor,
                      D_pass=dp, S_compared=dp, S_pass=sp, A_compared=ac, A_pass=ap)
            if not (dp and sp and ap):
                raise DomainFailure('momentum branch D/S/A rejected')
            rows.append(dict(P=P, Pt=Pt, L=Lv, K=K, U=U, T=T, u=u, D=D, S=S, A=A))
        sqrt_d, bm_nonlinear = self.backend.root_transcendentals(rows, need_jac)
        for n, row in enumerate(rows):
            P, Pt, Lv, K, T, u, D, S, A = (row[k] for k in ('P', 'Pt', 'L', 'K', 'T', 'u', 'D', 'S', 'A'))
            sd = sqrt_d[n]
            fc = u*(self.two+sd)/(self.two*sd*(self.one+sd)*(self.one+sd))
            gc = g['w2']*(P*P+S*T/(self.one+sd))/(S*sd)
            q = self.half*(K*K+g['E']*P*P)+K*Pt+T*fc+(self.one+K)*Pt*gc
            max_quad = max(max_quad, abs(q))
            min_d, min_a, min_s = min(min_d, D), min(min_a, A), min(min_s, S)
            co = self.cos[n]
            for i in range(J):
                quad[i] += q*co[i]/nq
            if need_jac:
                am = Lv+g['w2']*Pt
                bm = am+(self.one+am)*bm_nonlinear[n]
                for i in range(J):
                    for j in range(i+1):
                        B[i][j] += bm*co[i]*co[j]/nq
            row['sd'], row['quad'] = sd, q
        if need_jac:
            for i in range(J):
                for j in range(i):
                    B[j][i] = B[i][j]
        moments = [v+quad[j] for j, v in enumerate(L)]
        self.emit('evaluate_end', moments=moments, minD=min_d, minS=min_s, minA=min_a, maxQuad=max_quad)
        return dict(moments=moments, quad=quad, B=B, rows=rows,
                    minD=min_d, minS=min_s, minA=min_a, maxQuad=max_quad)

    def solve_spd(self, B, right):
        J = self.J
        L = [[self.zero for _ in range(J)] for _ in range(J)]
        out = [self.zero for _ in range(J)]
        tmp = [self.zero for _ in range(J)]
        for i in range(J):
            for j in range(i+1):
                v = B[i][j]
                for k in range(j):
                    v -= L[i][k]*L[j][k]
                if i == j:
                    self.emit('spd_positive', i=i, value=v, positive=v > 0)
                    if not v > 0:
                        raise DomainFailure('momentum Newton matrix not SPD')
                    L[i][j] = self.backend.sqrt(v)
                else:
                    L[i][j] = v/L[j][j]
        for i in range(J):
            v = right[i]
            for j in range(i):
                v -= L[i][j]*tmp[j]
            tmp[i] = v/L[i][i]
        for i in range(J-1, -1, -1):
            v = tmp[i]
            for j in range(i+1, J):
                v -= L[j][i]*out[j]
            out[i] = v/L[i][i]
        return out

    def root(self, state, g, x):
        target = [self.zero]+[g['targetFactor']*state[self.M+j] for j in range(self.M)]
        L = list(target)
        Q = state[:self.M]
        self.emit('root_start', state=list(state), x=x, target=target, L=L)
        for it in range(self.rules['iterations']):
            e = self.evaluate(L, Q, g, True)
            residual = [v-target[j] for j, v in enumerate(e['moments'])]
            err = max(map(abs, residual))
            scale = max(self.scale_floor, e['maxQuad'], *map(abs, target))
            threshold = self.tolerance*scale
            accepted = err <= threshold
            self.emit('root_stop', iteration=it, err=err, scale=scale, tolerance=self.tolerance,
                      threshold=threshold, accepted=accepted)
            if accepted:
                self.emit('root_return', iteration=it, err=err, scale=scale, roundoffFallback=False)
                self.root_outcomes.append(dict(iteration=it, err=err, scale=scale, fallback=False))
                return L, e
            step = self.solve_spd(e['B'], residual)
            accepted = False
            for k, fac in enumerate(self.halves):
                trial = [v-fac*step[j] for j, v in enumerate(L)]
                self.emit('trial_start', k=k, fac=fac, trial=trial)
                try:
                    v = self.evaluate(trial, Q, g, False)
                    er = max(abs(z-target[j]) for j, z in enumerate(v['moments']))
                    improves = er < err
                    tolerance_compared = not improves
                    within_tolerance = er <= threshold if tolerance_compared else None
                    accepted = improves or within_tolerance
                    self.emit('trial_judgment', k=k, er=er, err=err, scale=scale, threshold=threshold,
                              improves=improves, tolerance_compared=tolerance_compared,
                              within_tolerance=within_tolerance, accepted=accepted)
                    if accepted:
                        L = trial
                        break
                except Exception as error:
                    self.emit('trial_caught', k=k, message=str(error))
            if not accepted:
                threshold = self.fallback_tolerance*scale
                accepted = err <= threshold
                self.emit('fallback_judgment', err=err, scale=scale, tolerance=self.fallback_tolerance,
                          threshold=threshold, accepted=accepted)
                if accepted:
                    self.emit('root_return', iteration=it, err=err, scale=scale, roundoffFallback=True)
                    self.root_outcomes.append(dict(iteration=it, err=err, scale=scale, fallback=True))
                    return L, e
                raise RuntimeError('momentum Newton line search failed')
        raise RuntimeError('momentum Newton iteration limit')

    def rhs(self, state, profile, x):
        g = self.coefficients[(profile, packed([x]))]
        L, root = self.root(state, g, x)
        flux = [self.zero for _ in range(self.M)]
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
            p = g['pNumerator'][j]*state[j]/g['pDenominator']
            linear_flux = -m*L[j+1]+(m*m-1)*p
            derivative[j] = g['sigma']*((m*m-4)*state[j]+g['qLNumerator']*L[j+1]/g['r3'])
            derivative[self.M+j] = 4*g['sigma']*state[self.M+j]+g['fluxPrefactor']*m*(linear_flux+flux[j])
        derivative[2*self.M] = g['meanFactor']*L[0]
        derivative[2*self.M+1] = g['meanFactor']
        return derivative, root['minA'], root['minD']

    def flow(self, fixture):
        state = [self.backend.make(v) for v in fixture['initial42']]
        min_a = min_d = self.infinity

        def increment(v, f, h):
            return [x+h*f[j] for j, x in enumerate(v)]

        def field(v, profile, step, label, x):
            nonlocal min_a, min_d
            self.emit('rk_field', profile=profile, step=step, label=label, x=x)
            f, ma, md = self.rhs(v, profile, x)
            min_a, min_d = min(min_a, ma), min(min_d, md)
            return f

        for i, grid in enumerate(fixture['grid']):
            for k, point in enumerate(grid):
                # Abscissas are original binary64 coefficient lookup keys.
                x, original_h = point['x'], point['h']
                h = self.backend.make(original_h)
                a = field(state, i, k, 'a', x)
                b = field(increment(state, a, h/2), i, k, 'b', x+original_h/2)
                c = field(increment(state, b, h/2), i, k, 'c', x+original_h/2)
                d = field(increment(state, c, h), i, k, 'd', x+original_h)
                for j in range(self.size):
                    state[j] += h*(a[j]+2*b[j]+2*c[j]+d[j])/6
        return state, min_a, min_d


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--capsule-summary', type=Path, required=True)
    p.add_argument('--bridge', type=Path, required=True)
    p.add_argument('--node', default='node')
    p.add_argument('--precision', choices=('float', 'mp'), default='float')
    p.add_argument('--dps', type=int, default=60)
    p.add_argument('--validated-baseline', type=Path)
    p.add_argument('--out-prefix', type=Path, required=True)
    a = p.parse_args()
    summary = load(a.capsule_summary)
    for key in ('coefficients', 'reference'):
        if sha(summary[key]['path']) != summary[key]['sha256']:
            raise ValueError('Original capsule identity changed')
    for key in ('source_sha256', 'additional_original_root_sources'):
        for path, value in summary[key].items():
            if sha(path) != value:
                raise ValueError('Original bound source changed: '+path)
    for value in summary['traced_source'].values():
        if sha(value['path']) != value['sha256']:
            raise ValueError('Original traced source changed')
    if summary['source_sha256'].get(str(a.bridge.resolve())) != sha(a.bridge):
        raise ValueError('The scalar bridge differs from the reference exporter')
    capsule = load(summary['coefficients']['path'])
    reference = load(summary['reference']['path'])
    if (capsule['modes'], capsule['spacing'], capsule['steps'], capsule['original_tail_gate']) != (20, 4, 16, 2e-9):
        raise ValueError('Only the prescribed unchanged discrete model is supported')
    if a.precision == 'mp':
        if a.validated_baseline is None:
            raise ValueError('Multiprecision requires an exact float baseline from this source version')
        baseline = load(a.validated_baseline)
        if (not baseline.get('all_original_operands_and_judgments_bitwise_identical') or
                not baseline.get('all_three_outputs42_bitwise_identical') or
                baseline['source_sha256'] != sha(__file__) or baseline['bridge_sha256'] != sha(a.bridge) or
                baseline['capsule_summary_sha256'] != sha(a.capsule_summary)):
            raise ValueError('The required exact baseline does not bind these sources and inputs')
        if not 40 <= a.dps <= 150:
            raise ValueError('Only an explicit 40 to 150 digit finite readout is supported')
    out_raw = Path(str(a.out_prefix)+'-raw.json.gz')
    out_summary = Path(str(a.out_prefix)+'-summary.json')
    out_failure = Path(str(a.out_prefix)+'-mismatch.json.gz')
    for path in (out_raw, out_summary, out_failure):
        if path.exists():
            raise ValueError('A frozen output exists: '+str(path))
    a.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    arithmetic = V8Float(a.bridge, a.node) if a.precision == 'float' else MPArithmetic(a.dps)
    rows, scalars = [], []
    started = time.monotonic()
    try:
        for fixture, ref in zip(capsule['fixtures'], reference['rows'], strict=True):
            engine = FrozenEngine(capsule, fixture, arithmetic)
            began = time.monotonic()
            state, min_a, min_d = engine.flow(fixture)
            if a.precision == 'float':
                same_output = packed(state) == packed(ref['state'])
                first_mismatch = None
                for k, (left, right) in enumerate(zip(engine.events, ref['events'])):
                    if numeric_identity(left) != numeric_identity(right):
                        first_mismatch = dict(index=k, port=left, original=right)
                        break
                same_trace = first_mismatch is None and len(engine.events) == len(ref['events'])
                if not same_output or not same_trace:
                    mismatch = dict(stage=fixture['stage'], all42_equal=same_output,
                                    port42=state, original42=ref['state'], first_trace_mismatch=first_mismatch,
                                    port_trace_length=len(engine.events), original_trace_length=len(ref['events']))
                    out_failure.write_bytes(gzip.compress((json.dumps(mismatch)+'\n').encode(), mtime=0))
                    raise RuntimeError('Exact float baseline failed; no tolerance or multiprecision continuation is allowed')
            target = [arithmetic.make(v) for v in fixture['targetNode40']]
            port_ratio = arithmetic.make(fixture['portRatio'])
            scale = arithmetic.make(fixture['normalizationScale'])
            physical = [v if j < engine.M else v/port_ratio for j, v in enumerate(state[:2*engine.M])]
            residual = [v-target[j] for j, v in enumerate(physical)]
            maximum = max(abs(v)/scale for v in residual)
            component = max(range(len(residual)), key=lambda j: abs(residual[j]))
            original = [arithmetic.make(v) for v in ref['state']]
            difference = [v-original[j] for j, v in enumerate(state)]
            iterations = {}
            for root in engine.root_outcomes:
                key = str(root['iteration'])
                iterations[key] = iterations.get(key, 0)+1
            row = dict(stage=fixture['stage'], state=arithmetic.public(state),
                       residual=arithmetic.public(residual), events=engine.events,
                       minA=arithmetic.public(min_a), minD=arithmetic.public(min_d),
                       root_outcomes=arithmetic.public(engine.root_outcomes))
            rows.append(row)
            scalar = dict(stage=fixture['stage'], all42_original_bitwise_identical=a.precision == 'float',
                          all_original_root_trace_bitwise_identical=a.precision == 'float',
                          root_calls=len(engine.root_outcomes), root_iteration_counts=iterations,
                          root_roundoff_fallbacks=sum(r['fallback'] for r in engine.root_outcomes),
                          maximum_reported_root_relative_residual=arithmetic.public(max(r['err']/r['scale'] for r in engine.root_outcomes)),
                          normalized_residual=arithmetic.public(maximum), peak_component=component,
                          maximum_all42_change=arithmetic.public(max(map(abs, difference))),
                          maximum_mean2_change=arithmetic.public(max(map(abs, difference[2*engine.M:]))),
                          output42_float64_sha256=numeric_sha([float(v) for v in state]),
                          original42_sha256=ref['state42_sha256'], trace_events=len(engine.events),
                          minA=arithmetic.public(min_a), minD=arithmetic.public(min_d),
                          seconds=time.monotonic()-began)
            scalars.append(scalar)
            print(json.dumps(dict(event='frozen_arithmetic_stage_complete', **scalar)), flush=True)
    finally:
        arithmetic.close()
    context = dict(source_sha256=sha(__file__), bridge_sha256=sha(a.bridge),
                   capsule_summary_path=str(a.capsule_summary.resolve()), capsule_summary_sha256=sha(a.capsule_summary),
                   original_coefficients=summary['coefficients'], original_reference=summary['reference'],
                   precision=a.precision, arithmetic=arithmetic.name, dps=a.dps if a.precision == 'mp' else None,
                   mpmath_version=getattr(arithmetic, 'version', None),
                   validated_baseline_sha256=sha(a.validated_baseline) if a.validated_baseline else None,
                   command=sys.argv, scope='Read-only three-stage flow at frozen original binary64 coefficients and original RK16. Float identity is exact; MP is a finite arithmetic readout with unchanged root tests, not a rigorous error bound or a continuous ODE solve.',
                   coefficient_convention='Static Number subexpressions are frozen before state multiplication: pNumerator/pDenominator, targetFactor, sigma, fluxPrefactor, qLNumerator, r3, meanFactor; plus geometry E/w2, trig, grid and all root rule constants. MP recomputes state-dependent P, Pt, L, U, K, T, D/S/A, nonlinear moments/Jacobian, Cholesky, root steps/decisions, split flux and all RK state arithmetic.',
                   original_root_rules=capsule['root_rules'], whole_tail_evaluated=False,
                   nonlinear_tail_solver_invoked=False, physical_checkpoint_written=False,
                   production_source_changed=False)
    raw = dict(**context, rows=rows)
    out_raw.write_bytes(gzip.compress((json.dumps(raw, ensure_ascii=False)+'\n').encode(), mtime=0))
    output = dict(**context, all_original_operands_and_judgments_bitwise_identical=a.precision == 'float',
                  all_three_outputs42_bitwise_identical=a.precision == 'float',
                  named_results=scalars, raw=dict(path=str(out_raw.resolve()), sha256=sha(out_raw)),
                  scalar_bridge_requests=arithmetic.requests, seconds=time.monotonic()-started)
    out_summary.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(event='terminal', summary=str(out_summary.resolve()), sha256=sha(out_summary))), flush=True)


if __name__ == '__main__':
    main()
