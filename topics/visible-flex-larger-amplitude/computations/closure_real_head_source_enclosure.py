#!/usr/bin/env python3
"""Rigorous real-source radius and port enclosures for the rational new metric.

For 12<=n<160 the cap is inactive and chi=1 except at the protected inner
collar. We stop strictly before that collar and enclose all deeper widths by
R22. Curvature redistribution is integrated by its exact total-variation
primitive. The free warp uses Arb/Acb integrals and explicit positive tails.
No shooting state, ODE solution or floating source integral is certified here.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

import flint
from flint import acb, arb, ctx, fmpq


def exact_q(x):
    q = x if isinstance(x, Q) else Q.from_float(x)
    return arb(fmpq(q.numerator, q.denominator))


def power2(exponent):
    return arb((1, exponent))


def zero_to(bound):
    if not bound >= 0:
        raise ValueError('A positive upper bound is required')
    return arb(0).union(bound)


def dyadic_endpoint(x):
    a, b = x.man_exp()
    return dict(mantissa=str(a), binary_exponent=int(b))


def ball_record(x):
    if not x.is_finite():
        raise ArithmeticError('A nonfinite ball cannot be recorded')
    return dict(lower=dyadic_endpoint(x.lower()),
                upper=dyadic_endpoint(x.upper()), display=str(x))


class RealHead:
    def __init__(self, ready, start=12, far=96, exact_through=23,
                 rel_bits=100, abs_bits=160):
        if not 12 <= start <= exact_through < far <= 159:
            raise ValueError('Require 12<=start<=exact_through<far<=159')
        self.ready = ready
        self.params = ready['rationalDeepModel']['physicalParameters']
        self.data = {x['n']: x for x in ready['shallowSourceParameters']['cells']}
        self.rc = exact_q(self.params['rCuff'])
        self.eps_phys = exact_q(self.params['epsilonScale'])
        self.eps = self.eps_phys/self.rc**7
        self.alpha = exact_q(ready['rationalDeepModel']['frozenWarpAlpha'])
        self.d0 = exact_q(Q(ready['rationalDeepModel']['exactSourceConstants']['delta0']))
        self.c0 = exact_q(Q(ready['rationalDeepModel']['exactSourceConstants']['etaRatioAtN0']))
        self.a = arb(11)/4
        self.sqrt12 = arb(12).sqrt()
        self.log2 = arb(2).log()
        self.rho = (self.a*self.log2).exp()
        self.start, self.far = start, far
        self.exact_through = exact_through
        self.rel_tol, self.abs_tol = power2(-rel_bits), power2(-abs_bits)
        self.integral_count = 0
        self.cells = {}
        self.node_radii = {}
        delta_far = self.d0*power2(-far)
        W_far = power2(21)*(arb(7)*delta_far.log()/4).exp()
        ratio_W = (-arb(7)*self.log2/4).exp()
        self.tail_bound = self.rc*(326*delta_far+11*W_far/(1-ratio_W))
        radius = self.rc+zero_to(self.tail_bound)
        self.node_radii[far] = radius
        for n in range(far-1, start-1, -1):
            cell = self.make_cell(n)
            cell['inner_radius'] = radius
            for segment in cell['segments']:
                segment['physical_inner_radius'] = radius
                radius += segment['width']
            cell['outer_radius'] = radius
            self.cells[n] = cell
            self.node_radii[n] = radius

    def make_cell(self, n):
        row = self.data[n]
        delta = self.d0*power2(-n)
        c = self.c0*(-arb(n)*self.log2/2).exp()
        mu = self.eps_phys*(self.a*delta.log()).exp()
        # Sum of all exact unwarped source lengths strictly inside cell n.
        q32 = (-arb(3)*self.log2/2).exp()
        after = 3*delta+6*self.c0*self.d0*q32**(n+1)/(1-q32)
        inner_log_r = self.rc.log()+after/self.sqrt12
        logs = [arb(0), exact_q(row['R']).log()-delta.log(),
                delta.log()-exact_q(row['alpha']).log(), -delta.log(),
                self.a*self.log2]
        pieces = [(0, 0, c), (0, 1, c), (1, 1, arb(1)),
                  (1, 2, c), (2, 2, arb(1)), (2, 3, c),
                  (3, 3, arb(1)), (3, 4, c), (4, 4, c)]
        segments = []
        offset = arb(0)
        for j, (lo, hi, ratio) in enumerate(pieces):
            length = delta*ratio
            segment = dict(n=n, j=j, length=length, log_mu=mu.log(),
                log_r0=inner_log_r+offset/self.sqrt12,
                log_p0=logs[lo], log_jump=logs[hi]-logs[lo],
                transition=lo != hi, delta=delta)
            segment['critical_points'] = self.critical_points(segment)
            pieces_tv = [arb(0), *segment['critical_points'], arb(1)]
            f = [self.normal_slope(self.source_point(segment, x)['w']) for x in pieces_tv]
            tv = sum((abs(b-a) for a, b in zip(f, f[1:])), arb(0))
            segment['curvature_width'] = tv/8
            segment['free_width'], segment['free_defect'], segment['free_method'] = self.free_width(segment, arb(1))
            segment['width'] = segment['curvature_width']+self.alpha*segment['free_width']
            if not segment['width'] > 0:
                raise ArithmeticError('A cell width lost positivity')
            segments.append(segment)
            offset += length
        return dict(n=n, delta=delta, mu=mu, segments=segments,
                    width=sum((s['width'] for s in segments), arb(0)))

    @staticmethod
    def smooth(x):
        return x*x*x*(10+x*(-15+6*x))

    @staticmethod
    def smooth_derivative(x):
        return 30*x*x*(1-x)*(1-x)

    @staticmethod
    def normal_slope(w):
        return w/(1+w*w).sqrt()

    def source_point(self, segment, x):
        log_r = segment['log_r0']+segment['length']*x/self.sqrt12
        smooth = self.smooth(x) if segment['transition'] else arb(0)
        dsmooth = self.smooth_derivative(x) if segment['transition'] else arb(0)
        log_w = segment['log_mu']+segment['log_p0']+segment['log_jump']*smooth-7*log_r
        ro, w = log_r.exp(), log_w.exp()
        log_w_x = segment['log_jump']*dsmooth-7*segment['length']/self.sqrt12
        return dict(ro=ro, ro_x=segment['length']*ro/self.sqrt12,
                    w=w, log_w=log_w, log_w_x=log_w_x)

    def critical_points(self, segment):
        if not segment['transition'] or segment['log_jump'] < 0:
            return []
        if not segment['log_jump'] > 0:
            raise ArithmeticError('The sign of a log jump is undecided')
        t = (7*segment['length']/(30*self.sqrt12*segment['log_jump'])).sqrt()
        if not 0 < t < arb(1)/4:
            raise ArithmeticError('The exact two-critical-point formula is outside its domain')
        root = (1-4*t).sqrt()
        # Stable evaluation of (1-sqrt(1-4t))/2.
        lo = 2*t/(1+root)
        return [lo, 1-lo]

    def free_width(self, segment, stop):
        ro0 = segment['log_r0'].exp()
        q = segment['length']*stop/self.sqrt12
        dr = ro0*q.expm1()
        if segment['n'] > self.exact_through:
            W = power2(21)*(arb(7)*segment['delta'].log()/4).exp()
            loss = zero_to(W*W*dr)
            return dr-loss, loss, 'zero-to-W^2-dr exact positive remainder'
        if not segment['transition']:
            w0 = self.source_point(segment, arb(0))['w']
            terms = [w0**(2*k)*ro0*(-(-(14*k-1)*q).expm1())/(14*k-1)
                     for k in range(1, 4)]
            upper = terms[0]-terms[1]+terms[2]
            loss = upper-zero_to(w0**8*dr)
            return dr-loss, loss, 'three exact geometric-series integrals with signed fourth remainder'

        log_w0=segment['log_mu']+segment['log_p0']-7*segment['log_r0']
        positive_scale=segment['length']*ro0/self.sqrt12*(2*log_w0).exp()
        def integrand(x, analytic):
            # A meromorphic exponential/rational function: poles produce a
            # nonfinite ball automatically, so no branch-cut flag is needed.
            delta_log_r=segment['length']*x/self.sqrt12
            delta_log_w=segment['log_jump']*self.smooth(x)-7*delta_log_r
            w2=(2*(log_w0+delta_log_w)).exp()
            # Extract a positive left-end factor. This also certifies tiny
            # partial intervals whose physical integral is below abs_tol.
            return (delta_log_r+2*delta_log_w).exp()/(1+w2)

        loss = acb.integral(integrand, acb(0), acb(stop),
            rel_tol=self.rel_tol, abs_tol=self.abs_tol,
            deg_limit=64, eval_limit=20000, depth_limit=30)
        self.integral_count += 1
        if not loss.is_finite() or not loss.imag.contains(0):
            raise ArithmeticError('Free warp integral failed to give a finite real enclosure')
        loss = positive_scale*loss.real
        if not loss > 0:
            raise ArithmeticError('Free warp loss lost positivity')
        return dr-loss, loss, 'Arb/Acb rigorous meromorphic integral'

    def port(self, physical_node):
        if physical_node not in self.node_radii or physical_node >= 159:
            raise ValueError('Port must be in the enclosed chi=1 region')
        # The point is the inner port of cell node-1, so use that cell mu.
        n = physical_node-1
        delta = self.d0*power2(-n)
        q32 = (-arb(3)*self.log2/2).exp()
        after = 3*delta+6*self.c0*self.d0*q32**(n+1)/(1-q32)
        ro = self.rc*(after/self.sqrt12).exp()
        mu = self.eps_phys*(self.a*delta.log()).exp()
        w = mu/ro**7
        E = 1+w*w
        dr_dro = self.alpha/E+7*w/(8*ro*E*E.sqrt())
        wr = (-7*w/ro)/dr_dro
        r = self.node_radii[physical_node]
        return dict(physical_node=physical_node, normalization_cell=n,
                    radius=r, old_radius=ro, mu=mu, w=w, wr=wr,
                    E=E, Ep=2*w*wr,
                    meridian_curvature=wr/(E*E.sqrt()),
                    angular_curvature=w/(r*E.sqrt()),
                    next_inner_cell_Xi_factor=self.rho)

    def physical_point(self, n, j, x):
        """Enclose one rational-coordinate point of the SAME real source."""
        q = Q(x)
        if not 0 <= q <= 1:
            raise ValueError('The source coordinate must lie in [0,1]')
        stop = exact_q(q)
        segment = self.cells[n]['segments'][j]
        g = self.source_point(segment, stop)
        if q == 0:
            partial = arb(0)
        elif q == 1:
            partial = segment['width']
        else:
            critical = []
            for root in segment['critical_points']:
                if root < stop:
                    critical.append(root)
                elif not root > stop:
                    raise ArithmeticError('Refine precision: a requested point overlaps a critical root ball')
            points = [arb(0), *critical, stop]
            f = [self.normal_slope(self.source_point(segment,t)['w']) for t in points]
            tv = sum((abs(b-a) for a,b in zip(f,f[1:])),arb(0))
            free, _, _ = self.free_width(segment, stop)
            partial = tv/8+self.alpha*free
        r = segment['physical_inner_radius']+partial
        E = 1+g['w']**2
        rx = abs(g['w']*g['log_w_x'])/(8*E*E.sqrt())+self.alpha*g['ro_x']/E
        wr = g['w']*g['log_w_x']/rx
        return dict(r=r, drdx=rx, logw=g['log_w'], dlogwdx=g['log_w_x'],
                    w=g['w'], wr=wr, E=E, Ep=2*g['w']*wr,
                    oldR=g['ro'], oldDrdx=g['ro_x'])

    def physical_interval(self, n, j, left, right):
        """Enclose every point of a rational-coordinate closed panel.

        Radius uses monotonicity and two certified integrals; all derivatives
        come from the same defining integrand. This is not an ODE enclosure.
        """
        left, right = Q(left), Q(right)
        if not 0 <= left <= right <= 1:
            raise ValueError('A panel inside [0,1] is required')
        a = self.physical_point(n,j,left)
        b = self.physical_point(n,j,right)
        g = self.source_point(self.cells[n]['segments'][j],exact_q(left).union(exact_q(right)))
        r = a['r'].union(b['r'])
        E = 1+g['w']**2
        rx = abs(g['w']*g['log_w_x'])/(8*E*E.sqrt())+self.alpha*g['ro_x']/E
        if not r > 0 or not rx > 0 or not g['w'] > 0:
            raise ArithmeticError('Subdivide the panel to retain positive source denominators')
        wr = g['w']*g['log_w_x']/rx
        return dict(r=r, drdx=rx, logw=g['log_w'], dlogwdx=g['log_w_x'],
                    w=g['w'], wr=wr, E=E, Ep=2*g['w']*wr,
                    oldR=g['ro'], oldDrdx=g['ro_x'])

    def linear_generator_interval(self, n, j, left, right, mode, balanced=False):
        """A rigorous coefficient matrix, not its fundamental solution."""
        if not isinstance(mode,int) or mode < 2 or mode%2:
            raise ValueError('A positive even physical mode is required')
        g = self.physical_interval(n,j,left,right)
        r, rx, w = g['r'],g['drdx'],g['w']
        mu = self.cells[n]['mu']
        nu = arb(mode*mode*(mode*mode-1))/12
        d = (mode*mode-4)*rx/r
        a = self.sqrt12*mu*rx/(r**8*w)
        b = -nu*self.sqrt12*rx*r**6*w/mu
        if balanced:
            a *= nu
            b /= nu
        return [[d,a],[b,-d]]

    def outer_cut_scalars(self):
        """Exact endpoint slope scalars; the outer radius integral is separate.

        oldCut is a captured binary auxiliary parameter in the frozen factory.
        It is not silently replaced by the recomputed real source radius.
        """
        if self.params['capMode'] != 'cut-preserving':
            raise ValueError('This outer endpoint formula needs cut-preserving mode')
        q32 = (-arb(3)*self.log2/2).exp()
        total = 6*self.d0+6*self.c0*self.d0/(1-q32)
        ro = self.rc*(total/self.sqrt12).exp()
        nominal_cut = exact_q(self.params['rCut'])
        captured_old_cut = exact_q(self.params['oldCut'])
        j0 = nominal_cut/captured_old_cut
        w = self.eps_phys*(self.a*(2*self.d0).log()).exp()/ro**7
        wr = -7*w/(ro*j0)
        E = 1+w*w
        return dict(nominal_cut_radius=nominal_cut,
                    captured_binary_old_cut=captured_old_cut,
                    true_unwarped_outer_radius=ro,
                    cut_collar_j0=j0,w=w,wr=wr,E=E,Ep=2*w*wr)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--ready', required=True, type=Path)
    p.add_argument('--source-ledger', required=True, type=Path)
    p.add_argument('--response', type=Path)
    p.add_argument('--out', required=True, type=Path)
    p.add_argument('--start', type=int, default=12)
    p.add_argument('--far', type=int, default=96)
    p.add_argument('--exact-through', type=int, default=23)
    p.add_argument('--precision', type=int, default=192)
    args = p.parse_args()
    ctx.prec = args.precision
    started = time.monotonic()
    ready_raw = args.ready.read_bytes()
    ready = json.loads(ready_raw)
    ledger_raw = args.source_ledger.read_bytes()
    ledger = json.loads(ledger_raw)
    if not all(ledger['checks'].values()):
        raise ValueError('The R22 source hypotheses were not all paid')
    if hashlib.sha256(ready_raw).hexdigest() not in ledger['input_hashes'].values():
        raise ValueError('The paid source ledger belongs to a different ready file')
    head = RealHead(ready, args.start, args.far, args.exact_through)
    ports = {}
    for n in (args.start, 16, 24, 32, 64, args.far):
        if n in head.node_radii:
            ports[str(n)] = {k:ball_record(v) if isinstance(v, arb) else v
                            for k,v in head.port(n).items()}
    panels = []
    for j in (1,3,5,7):
        left,right=Q(127,256),Q(129,256)
        g=head.physical_interval(args.start,j,left,right)
        matrix=head.linear_generator_interval(args.start,j,left,right,2)
        panels.append(dict(cell=args.start,segment=j,left=str(left),right=str(right),
            scope='Every real source point on this closed panel; coefficient matrix only, no ODE trajectory',
            source={k:ball_record(v) for k,v in g.items()},
            physical_mode=2,linear_matrix=[[ball_record(v) for v in row] for row in matrix]))
    comparisons = None
    outer = head.outer_cut_scalars()
    outer_comparisons = None
    hashes = {str(args.ready):hashlib.sha256(ready_raw).hexdigest(),
              str(args.source_ledger):hashlib.sha256(ledger_raw).hexdigest()}
    if args.response:
        raw = args.response.read_bytes()
        response = json.loads(gzip.decompress(raw) if args.response.suffix=='.gz' else raw)
        saved = response['response']['endpointCanonicalTrace']
        actual = head.port(saved['physicalNode'])
        comparisons = {key:ball_record(exact_q(saved[key])-actual[key]) for key in ('radius','w','mu')}
        jets=response['response']['jets']
        outer_comparisons={name:ball_record(exact_q(jets[saved_name])-outer[name])
            for name,saved_name in [('w','backgroundSlope'),('wr','backgroundSecond'),('E','E'),('Ep','Ep')]}
        outer_comparisons['saved_binary_cut_radius']=ball_record(exact_q(jets['radius']))
        hashes[str(args.response)] = hashlib.sha256(raw).hexdigest()
    rows = []
    for n, c in sorted(head.cells.items()):
        rows.append(dict(cell=n, width=ball_record(c['width']),
            curvature_width=ball_record(sum((s['curvature_width'] for s in c['segments']),arb(0))),
            free_loss=ball_record(sum((s['free_defect'] for s in c['segments']),arb(0))),
            free_methods=[s['free_method'] for s in c['segments']]))
    start_radius = head.node_radii[args.start]
    checks = dict(all_source_hypotheses_paid=True,
        current_radius_is_positive=start_radius > 0,
        radius_interval_width_below_2pow_minus96=start_radius.rad()*2 < power2(-96),
        deeper_radius_tail_below_2pow_minus99=head.tail_bound < power2(-99))
    if not all(checks.values()):
        raise AssertionError(checks)
    out = dict(status='Rigorous enclosures of the explicitly defined REAL source only; no nonlinear trajectory certificate',
        arithmetic=dict(library='python-flint',version=flint.__version__,precision_bits=ctx.prec,
                        endpoints='Outward Arb endpoints stored as exact mantissa*2^binary_exponent'),
        parameters=dict(start=args.start,far=args.far,exact_free_integrals_through=args.exact_through),
        checks=checks,ports=ports,cell_widths=rows,closed_panel_examples=panels,
        deeper_radius_tail=ball_record(head.tail_bound),
        stored_binary_minus_real_source=comparisons,
        outer_cut=dict(scalars={k:ball_record(v) for k,v in outer.items()},
            stored_binary_minus_real_scalars=outer_comparisons,
            real_radius_definition='R_out = r_c + the sum of all exact physical cell-width integrals; frozen binary warp alpha is not recalibrated',
            real_radius_status='The n>=12 part is enclosed here. The complete cap/valley/weighted warp integral over cells0..11 is not yet enclosed, so R_out is NOT asserted equal to nominal binary rCut or saved cut radius.',
            captured_old_cut_convention='The factory-captured oldCut binary auxiliary constant is retained in j0=rCut/oldCut. Replacing it by the true unwarped radius would be a distinct arithmetic convention.'),
        exact_source_convention='Fixed dyadic d0,c0,r_c,epsilon_phys,warp alpha and saved finite R_n,alpha_n; all exp/log/powers/integrals evaluated as real functions',
        coordinate_convention='At physical node k the stored endpoint Xi uses mu_(k-1); for the adjoining inner cell k multiply Xi by 2^(11/4)',
        integral_count=head.integral_count,elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        input_hashes=hashes,entrypoint_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        limits=['No finite Galerkin or radial ODE error is inferred from these source intervals.',
                'The numerical stored source and this real source are distinct arithmetic objects; their displayed differences are explicit enclosures.',
                'No complete shallow trace, Green inverse or prefix matching is supplied here.'])
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),checks=checks,
        radius_at_start=str(start_radius),source_differences=comparisons,
        integral_count=head.integral_count,elapsed_seconds=out['elapsed_seconds'],peak_RSS_KiB=out['peak_RSS_KiB'])))


if __name__ == '__main__':
    main()
