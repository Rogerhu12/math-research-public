#!/usr/bin/env python3
"""R643 same-E chain with the real mean height left as a coupled unknown.

No trial mean root, 1/W trial coordinate, or division by the mean coefficient.
The true accepted seed mean is fixed input.  Every trial and derivative uses
p=-W+s_seed+delta_m_r+f_r and the complete off-solution six-jet equations.
Finite primitives remain observations; actual position derivatives and all
source/angle/radial errors still need their declared consumers.
Science only in the repository's public Actions environment.
"""
from collections import defaultdict
from decimal import Decimal, localcontext
import hashlib
import math
from pathlib import Path

import numpy as np

SCHEMA = 'r643-unsolved-mean-complete-fixed-E-chain-v1'
ORIGINAL_CHAIN_SHA = '0668d1afbcdcd5e0c0c16d3784c322d6e0bba3639c547d8ae0bd42900ff09815'
JET_KEYS = ('f', 'fr', 'frr', 'ft', 'ftt', 'frt')
ZERO, ONE, TWO, THREE = map(Decimal, (0, 1, 2, 3))


def dec(value):
    if isinstance(value, Decimal):
        return value
    if isinstance(value, str):
        return Decimal(value)
    value = float(value)
    if not math.isfinite(value):
        raise ArithmeticError('finite actual value required by the explicit mean chain')
    return Decimal.from_float(value)


def mean(values):
    return sum(values, ZERO) / Decimal(len(values))


class UnsolvedMeanChain:
    @staticmethod
    def policy_descriptor():
        return {
            'schema': SCHEMA,
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'original_chain_sha256': ORIGINAL_CHAIN_SHA,
            'minimum_decimal_precision': 100,
            'additional_target_guard_digits': 20,
            'maximum_decimal_precision': 4096,
            'trial_mean_roots': False,
            'divides_by_W_or_mean_coefficient_in_trials_or_directions': False,
            'same_reference_e_E_Er_split_kept_before_geometry': True,
            'complete_off_solution_weight_and_phase_terms': True,
            'canonical_F_and_G_rows_both_retained': True,
            'roundoff_source_and_continuous_errors_enclosed': False,
        }

    def __init__(self, original_chain, policy, check_clock):
        original_chain.public_only()
        if hashlib.sha256(Path(original_chain.__file__).read_bytes()).hexdigest() != ORIGINAL_CHAIN_SHA:
            raise ValueError('same unchanged original fixed-E source required')
        if policy != self.policy_descriptor() or not callable(check_clock):
            raise ValueError('complete explicit-mean source policy and actual clock required')
        self.original = original_chain
        self.policy = dict(policy)
        self.check_clock = check_clock
        self.counts = defaultdict(int)
        self.counts['explicit_mean_chains'] = 1

    def _float(self, value):
        result = float(value)
        if not math.isfinite(result):
            raise ArithmeticError('complete explicit geometry has no finite array representation')
        if result == 0 and value:
            self.counts['decimal_to_binary64_underflow_observations'] += 1
        return result

    @staticmethod
    def _long(value):
        answer = np.longdouble(str(value))
        if not np.isfinite(answer):
            raise ArithmeticError('complete explicit coefficient cannot fit longdouble')
        return answer

    def explicit_state(self, target, jets, seed_mean, delta_mean):
        """One true trial on one angle grid, with no trial scalar elimination.

        delta_mean=(delta_m,delta_m_r,delta_m_rr) is the same actual radial
        function; it is not an independently assigned slope at each radius.
        The frozen seed's Decimal x/s_r are retained before adding the change.
        """
        self.original.public_only()
        self.check_clock()
        if (seed_mean['target']['target_sha256'] != target['target_sha256']
                or seed_mean['target']['r'] != target['r']):
            raise ValueError('the real seed mean must belong to the same frozen radial target')
        j_float = self.original._jets(jets)
        if not isinstance(target.get('split_reference'), dict):
            raise ValueError('the same persistent fixed-reference split is required')
        change = np.asarray(delta_mean, dtype=float)
        if change.shape != (3,) or not np.all(np.isfinite(change)):
            raise ValueError('actual mean height and both radial jets required')
        split = target['split_reference']
        precision = max(self.policy['minimum_decimal_precision'],
                        int(split['precision']) + self.policy['additional_target_guard_digits'])
        if precision > self.policy['maximum_decimal_precision']:
            raise ArithmeticError('declared explicit-mean Decimal capacity exceeded')
        self.counts['explicit_geometry_attempts'] += 1
        self.counts['maximum_decimal_precision_used'] = max(
            self.counts['maximum_decimal_precision_used'], precision)
        with localcontext() as ctx:
            ctx.prec = precision
            r, W, Wr = map(dec, (target['r'], target['W'], target['W_r']))
            scale2 = W * W if split['normalization'] == 'W_squared' else ONE
            eta = scale2 * dec(split['centre_decimal']) + scale2 * dec(split['offset_decimal'])
            E = ONE + W * W + eta
            Er = TWO * W * Wr + dec(split['e_r_decimal'])
            sx = dec(seed_mean['x_decimal'])
            if seed_mean['chart'] == 'lambda':
                seed_s = W * sx
            elif seed_mean['chart'] == 'zeta':
                # This is only decoding the fixed seed supplied by the old
                # chart. No trial unknown or parameter is divided by W.
                seed_s = sx / W
            else:
                raise ValueError('same literal accepted split seed is required')
            s = seed_s + dec(change[1])
            sr = dec(seed_mean['s_r_decimal']) + dec(change[2])
            j = {key: tuple(dec(value) for value in j_float[key]) for key in JET_KEYS}
            fields = {key: [] for key in (
                'p', 'pr', 'q', 't', 'b', 'u', 'N', 'a_minus_one', 'C',
                'M', 'B', 'omega', 'D', 'R', 'v', 'K', 'ut')}
            coefficients = {key: [] for key in (
                'ap_plus_W', 'aq', 'at_plus_W_over_r',
                'Rp_plus_Wr', 'Rq', 'Rt_plus_Wr_over_r', 'Rrt')}
            raw_ap, raw_Rp = [], []
            for fr, frr, q, t, frt in zip(j['fr'], j['frr'], j['ft'], j['ftt'], j['frt']):
                b2 = r*r-q*q
                if b2 <= 0:
                    raise ArithmeticError('explicit mean trial lost b positivity')
                b = b2.sqrt()
                p, pr = -W+s+fr, -Wr+sr+frr
                n = q*q/(b*(r+b)) + r*r*p*t/(b*b*b)
                du2 = W*W+eta-r*r*p*p/b2
                u2, N = ONE+du2, ONE+n
                if E <= 0 or u2 <= 0 or N <= 0:
                    raise ArithmeticError('explicit mean trial left the same positive energy component')
                u = u2.sqrt()
                am1 = (TWO*n+n*n-du2)/(u*(N+u))
                C = E*t+r*p
                M = r+p*t-q*q/r
                B = frt-q/r
                omega = r*r/(u*u*u*b*b*b)
                D = C*pr-E*B*B-Er*M/TWO
                R = omega*D
                v = -p*q/b
                K = r*r*p*B/(u*b*b*b)
                ut = -r*r*p*frt/(u*b2)-r*r*p*p*q*t/(u*b2*b2)
                values = (p,pr,q,t,b,u,N,am1,C,M,B,omega,D,R,v,K,ut)
                for name, value in zip(fields, values):
                    fields[name].append(value)
                ap = omega*C
                aq = (r*q/(u*b**3)+THREE*r*r*p*t*q/(u*b**5)
                      +N*r*r*p*p*q/(u**3*b**4))
                at = r*r*p/(u*b**3)
                Rp = omega*(r*pr-Er*t/TWO+THREE*D*r*r*p/(u*u*b2))
                Rq = omega*(TWO*E*B/r+Er*q/r
                     +THREE*D*(r*r*p*p*q/(u*u*b2*b2)+q/b2))
                Rt = omega*(E*pr-Er*p/TWO)
                Rrt = -TWO*omega*E*B
                for name, value in zip(coefficients,
                        (ap+W,aq,at+W/r,Rp+Wr,Rq,Rt+Wr/r,Rrt)):
                    coefficients[name].append(value)
                raw_ap.append(ap)
                raw_Rp.append(Rp)
            F, G = mean(fields['a_minus_one']), mean(fields['R'])
            A = ONE+F
            if A <= 0:
                raise ArithmeticError('positive normalized turning mean is required')
            answer = {key: np.asarray([self._float(v) for v in values],dtype=float)
                      for key, values in fields.items()}
            answer.update(
                target=target, jets=j_float, E=self._float(E), E_r=self._float(Er),
                s=self._float(s), s_r=self._float(sr),
                s_decimal=str(s), s_r_decimal=str(sr),
                p0=self._float(-W+s), p0_r=self._float(-Wr+sr),
                F=self._float(F), G=self._float(G), A=self._float(A),
                F_decimal=str(F), G_decimal=str(G), A_decimal=str(A),
                mean_ap_long=self._long(mean(raw_ap)),
                mean_Rp_long=self._long(mean(raw_Rp)),
                mean_coefficient_decimal=str(mean(raw_ap)),
                centered_coefficients={key: np.asarray([self._long(v) for v in values],
                                                      dtype=np.longdouble)
                                       for key, values in coefficients.items()},
                explicit_mean_chain_source_sha256=self.policy['source_sha256'],
                trial_mean_root_or_mean_coefficient_division=False,
                source_angular_and_roundoff_errors_enclosed=False,
                seed_mean_source='fixed_actual_accepted_split_seed',
                numerical_mean_height_change=change.copy())
        self.counts['explicit_geometry_radial_states'] += 1
        self.counts['explicit_geometry_angular_points'] += len(j_float['f'])
        self.counts['explicit_decimal_input_jet_scalars'] += 6*len(j_float['f'])
        return answer

    @staticmethod
    def _finite(value):
        answer = np.asarray(value,dtype=float)
        if not np.all(np.isfinite(answer)):
            raise ArithmeticError('complete explicit direction cannot fit finite arrays')
        return answer

    def direction(self, state, jets, delta_s, delta_sr, *, canonical_mean=False):
        """All original off-solution terms, retaining the two true mean jets."""
        self.original.public_only()
        self.check_clock()
        if state.get('explicit_mean_chain_source_sha256') != self.policy['source_sha256']:
            raise ValueError('one same-source explicit state required')
        H = {key: np.asarray(jets[key],dtype=np.longdouble) for key in JET_KEYS}
        shape = H['f'].shape
        if (len(shape)!=2 or shape[0]!=len(state['p'])
                or any(value.shape!=shape for value in H.values())):
            raise ValueError('all six same-angle parameter jets required')
        ds,dsr = np.asarray(delta_s,dtype=np.longdouble),np.asarray(delta_sr,dtype=np.longdouble)
        if ds.shape!=(shape[1],) or dsr.shape!=ds.shape:
            raise ValueError('same actual mean derivative columns required')
        r,W,Wr = map(np.longdouble,(state['target']['r'],state['target']['W'],state['target']['W_r']))
        p,q,t,b,u,N,v,K = [np.asarray(state[key],dtype=np.longdouble)[:,None]
                          for key in ('p','q','t','b','u','N','v','K')]
        c = {key:value[:,None] for key,value in state['centered_coefficients'].items()}
        dp,dpr = H['fr']+ds[None,:],H['frr']+dsr[None,:]
        dq,dt,dpt = H['ft'],H['ftt'],H['frt']
        db = -q*dq/b
        du = -r*r*p*dp/(u*b*b)-r*r*p*p*q*dq/(u*b**4)
        dN = r*q*dq/b**3+r*r*(t*dp+p*dt)/b**3+3*r*r*p*t*q*dq/b**5
        # Pointwise formulas retain all backgrounds. Only exact positive
        # Fourier zero means license the centered scalar contractions.
        da = -W*dp-W/r*dt+c['ap_plus_W']*dp+c['aq']*dq+c['at_plus_W_over_r']*dt
        dR = (-W*dpr-Wr*dp-Wr/r*dt+c['ap_plus_W']*dpr
              +c['Rp_plus_Wr']*dp+c['Rq']*dq+c['Rt_plus_Wr_over_r']*dt+c['Rrt']*dpt)
        dv = -(q*dp+p*dq)/b+p*q*db/b**2
        dB = dpt-dq/r
        BB = np.asarray(state['B'],dtype=np.longdouble)[:,None]
        dK = r*r*(BB*dp+p*dB)/(u*b**3)-K*(du/u+3*db/b)
        aa = np.longdouble(1)+np.asarray(state['a_minus_one'],dtype=np.longdouble)[:,None]
        dut = aa*dv+v*da-K*db-b*dK
        answer = {key:self._finite(value) for key,value in
                  dict(p=dp,pr=dpr,b=db,u=du,N=dN,a=da,R=dR,v=dv,K=dK,ut=dut).items()}
        if canonical_mean:
            if shape[0] < 512:
                raise ValueError('the original full canonical mean rule is retained')
            avg = lambda value: np.mean(value,axis=0,dtype=np.longdouble)
            dF = (state['mean_ap_long']*ds
                  +avg(c['ap_plus_W']*H['fr']+c['aq']*dq+c['at_plus_W_over_r']*dt))
            dG = (state['mean_ap_long']*dsr+state['mean_Rp_long']*ds
                  +avg(c['ap_plus_W']*H['frr']+c['Rp_plus_Wr']*H['fr']
                       +c['Rq']*dq+c['Rt_plus_Wr_over_r']*dt+c['Rrt']*dpt))
            answer.update(F=self._finite(dF),G=self._finite(dG))
        self.counts['complete_explicit_direction_columns_at_radii'] += shape[1]
        self.counts['complete_explicit_direction_angular_points'] += int(np.prod(shape))
        return answer

    def position(self, state, canonical_mean, theta, primitive):
        """Discretize the complete R643 continuous periodic-position formula."""
        self.original.public_only()
        self.check_clock()
        if state['target']['r'] != canonical_mean['target']['r']:
            raise ValueError('same-radius canonical scalar constraints required')
        F,G,A = canonical_mean['F'],canonical_mean['G'],canonical_mean['A']
        if A <= 0:
            raise ArithmeticError('positive actual normalization required')
        pi = lambda value: primitive@value
        pa,pr = pi(state['a_minus_one']),pi(state['R'])
        psi = theta+np.pi/2+pa/A
        T = np.stack([np.cos(psi),np.sin(psi)],axis=1)
        JT = np.stack([-T[:,1],T[:,0]],axis=1)
        b,u,N,v,ut = [state[key] for key in ('b','u','N','v','ut')]
        Q = pr-pa*G/A
        V = N[:,None]*T+ut[:,None]*JT
        multiplier = b*Q/A
        integrand = (F/A)*V+multiplier[:,None]*JT
        defect = pi(integrand)
        E,r = state['E'],state['target']['r']
        S = defect/np.sqrt(E)
        pred = v[:,None]*T-u[:,None]*JT
        Y,Yt,Yr = pi(b[:,None]*T),b[:,None]*T,pred+defect
        psir = (state['K']+pr)/A-pa*G/A**2
        br = (r-state['q']*state['jets']['frt'])/b
        bt = -state['q']*state['t']/b
        Yrt = br[:,None]*T+(b*psir)[:,None]*JT
        Ytt = bt[:,None]*T+(b*(1+state['a_minus_one'])/A)[:,None]*JT
        de = (2*np.sum(defect*pred,axis=1)+np.sum(defect*defect,axis=1))/E
        cross = b*np.sum(defect*T,axis=1)/(r*np.sqrt(E))
        eta = (abs(de)+np.sqrt(de*de+4*cross*cross))/2
        alternating = (-1.)**np.arange(len(theta))
        self.counts['complete_normalized_position_angular_points'] += len(theta)
        return dict(
            primitive=primitive,T=T,JT=JT,pa=pa,pr=pr,Q=Q,V=V,multiplier=multiplier,
            A=A,F=F,G=G,S=S,Y=Y,Yt=Yt,Yr=Yr,Yrt=Yrt,Ytt=Ytt,
            eta=eta,pred=pred,psir=psir,
            outward_ratio=-np.sum(Yr*JT,axis=1)/u,
            angular_closure_observation=np.mean(Yt,axis=0),
            output_minus_canonical_mean_a_observation=float(state['F']-F),
            output_minus_canonical_mean_R_observation=float(state['G']-G),
            output_Nyquist_a_minus_one_observation=float(np.mean(state['a_minus_one']*alternating)),
            output_Nyquist_R_observation=float(np.mean(state['R']*alternating)),
            finite_primitive_is_not_a_continuous_or_direct_position_certificate=True,
            continuous_formula_includes_all_F_and_G_terms=True,
            same_fixed_E_and_real_unsolved_mean_height=True)

    def position_direction(self, state, position, direction, canonical_direction):
        self.original.public_only()
        self.check_clock()
        pi = lambda value: position['primitive']@value
        A,F,G = [position[key] for key in ('A','F','G')]
        dA,dG = canonical_direction['F'][None,:],canonical_direction['G'][None,:]
        pa,Q = position['pa'][:,None],position['Q'][:,None]
        dpa,dpr = pi(direction['a']),pi(direction['R'])
        dpsi = dpa/A-pa*dA/A**2
        dQ = dpr-G*dpa/A-pa*dG/A+pa*G*dA/A**2
        b,ut,N = [state[key][:,None] for key in ('b','ut','N')]
        dm = (direction['b']*Q+b*dQ)/A-b*Q*dA/A**2
        m = position['multiplier'][:,None]
        pieces = []
        for component in range(2):
            T,JT = position['T'][:,component,None],position['JT'][:,component,None]
            dV = (direction['N']*T+N*JT*dpsi
                  +direction['ut']*JT-ut*T*dpsi)
            dH = dA/A**2*position['V'][:,component,None]+F/A*dV+dm*JT-m*T*dpsi
            pieces.append(pi(dH)/np.sqrt(state['E']))
        answer = np.stack(pieces,axis=1)
        if not np.all(np.isfinite(answer)):
            raise ArithmeticError('complete coupled same-E position direction is not finite')
        self.counts['complete_normalized_position_direction_angular_points'] += answer.size
        return answer
