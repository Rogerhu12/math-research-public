#!/usr/bin/env python3
"""Complete growing-post height, fixed target metric and full-S Jacobian.

Pure new source: no actual input, numerical request or workflow is invented.
A future public Actions scope must bind its genuine completed original q,
the full field identity, numerical policy, mean brackets and all inherited
costs. The factory reconstructs the original model once from the frozen
literal source and arguments, using its unchanged mouths. Every original
nonmean coefficient remains a parameter;
H and amplitude belong to the frozen target reference and do not back off.

New columns comprise higher compact angular responses, explicit genuine
rapid-flat analytic post tails on the WHOLE (rc,drop_end), and independent
core P0 lifts. Every dependent mode through2J is in the actual height and
all six spatial/parameter jets. The full core tau path starts at the literal
old field and reaches the continuous-target core map. Numerical means and
root/quadrature values approximate that fixed definition; their errors are
not silently called continuous certificates.
"""
from collections import defaultdict
from dataclasses import replace
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace
from weakref import WeakKeyDictionary
import numpy as np
from scipy.integrate import quad,quad_vec

HERE = Path(__file__).resolve().parent
CHAIN_FILE = 'r618_fixed_metric_numerical_chain_20261127.py'
CHAIN_SHA = '0668d1afbcdcd5e0c0c16d3784c322d6e0bba3639c547d8ae0bd42900ff09815'
ORIGINAL_DRIVER_SHA = '6850c9e7f561aadfbc749536b181e1e5e32ff6fddfa6ea3b2de9d08d91b2cfb0'
COUNTS = defaultdict(int)
JET_KEYS = ('f','fr','frr','ft','ftt','frt')
_RESTORED_ORIGINALS = WeakKeyDictionary()


def _json_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
                                     allow_nan=False).encode()).hexdigest()


def _array_sha(value):
    array = np.asarray(value,dtype='<f8')
    return hashlib.sha256(json.dumps(list(array.shape),separators=(',',':')).encode()
                          +b'\n'+array.tobytes(order='C')).hexdigest()


def _reconstruction_text(frozen_identity):
    owner = json.loads(frozen_identity.source_state_json)
    while 'reconstruction_source_JSON' not in owner:
        if 'previous_scope_input_JSON' not in owner:
            raise ValueError('complete original reconstruction cannot be recovered from the actual source')
        owner = json.loads(owner['previous_scope_input_JSON'])
    return owner['reconstruction_source_JSON']


def _bound_chain():
    path = HERE/CHAIN_FILE
    if hashlib.sha256(path.read_bytes()).hexdigest() != CHAIN_SHA:
        raise RuntimeError('complete fixed-E numerical chain changed')
    spec = importlib.util.spec_from_file_location('r618_actual_fixed_metric_chain',path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


chain = _bound_chain()


def _pad(a,n):
    if len(a) > n:
        raise ValueError('growing core band would discard an original frequency')
    answer = np.zeros(n,dtype=float)
    answer[:len(a)] = a
    return answer


def _separable(radial,coefficients,modes,theta):
    """Six complete jets of radial(r) times a positive-even cosine sum."""
    co,si = np.cos(modes[:,None]*theta),np.sin(modes[:,None]*theta)
    a = coefficients@co
    at = -(coefficients*modes)@si
    att = -(coefficients*modes*modes)@co
    return {'f':radial[:,0,None]*a,'fr':radial[:,1,None]*a,
        'frr':radial[:,2,None]*a,'ft':radial[:,0,None]*at,
        'ftt':radial[:,0,None]*att,'frt':radial[:,1,None]*at}


class GrowingPostFixedMetricHeight:
    """A real height model and analytic parameter operator, not a row filter.

    policy is explicit future-scope input. Required entries:
      mean_points, core_points, root_steps, root_tolerance,
      mean_bracket_radius {lambda,shift,zeta},
      core_lift_epsabs, core_lift_epsrel, quadrature_limit,
      mean_height_epsabs, mean_height_epsrel,
      core_lift_cutoff_left, core_lift_cutoff_right,
      tail_degrees (the full ordered list0..K),
      tail_gaussian_denominator, tail_cutoff_left, tail_cutoff_right.
    Finite quadrature and observed brackets are never rigorous certificates.
    """
    @classmethod
    def restore_from_frozen_reference(cls,original_driver,actual_q_json,amplitude,
            frozen_identity,maximum_independent_mode,policy,*,deadline,attempts):
        """Unique original-object provenance, with one charged reconstruction.

        The complete reconstruction arguments are literal mathematical-field
        input, not a second caller-supplied namespace. The original restore
        path reuses its paid q, knots, force and every mouth; its existing
        ODE counters/attempt receipts remain authoritative. This adds no
        inner-DtN solve, old diagnostic or numerical acceptance gate.
        """
        chain.public_only()
        path = HERE/'r613_full_position_height_20261127.py'
        if (hashlib.sha256(path.read_bytes()).hexdigest() != ORIGINAL_DRIVER_SHA
                or Path(original_driver.restore_model.__code__.co_filename).resolve() != path.resolve()):
            raise ValueError('the exact original reconstruction implementation is required')
        definition = json.loads(frozen_identity.mathematical_field_json)
        reconstruction_text = _reconstruction_text(frozen_identity)
        reconstruction_sha = hashlib.sha256(reconstruction_text.encode()).hexdigest()
        if reconstruction_sha != definition['reconstruction_source_sha256']:
            raise ValueError('literal original reconstruction differs before any reconstruction work')
        arguments = definition['all_literal_parameters']['original_reconstruction_arguments']
        if not isinstance(arguments,dict) or not all(isinstance(k,str) for k in arguments):
            raise TypeError('literal complete original reconstruction arguments required')
        arguments_json = json.dumps(arguments,sort_keys=True,separators=(',',':'),allow_nan=False)
        args = SimpleNamespace(**json.loads(arguments_json))
        COUNTS['original_bound_reconstruction_attempts'] += 1
        original = original_driver.restore_model(json.loads(reconstruction_text),args,deadline,attempts)
        receipt = {'target_sha256':frozen_identity.target_sha256,
            'reconstruction_source_sha256':reconstruction_sha,
            'original_driver_sha256':ORIGINAL_DRIVER_SHA,
            'original_reconstruction_arguments_JSON':arguments_json,
            'original_reconstruction_arguments_sha256':hashlib.sha256(arguments_json.encode()).hexdigest(),
            'original_object_constructed_by_bound_restore_once':True,
            'old_inner_DtN_or_readout_replayed':False}
        _RESTORED_ORIGINALS[original] = (original_driver,receipt)
        try:
            return cls(original_driver,original,actual_q_json,amplitude,frozen_identity,
                       maximum_independent_mode,policy)
        finally:
            _RESTORED_ORIGINALS.pop(original,None)

    def __init__(self,original_driver,original_model,actual_q_json,amplitude,
                 frozen_identity,maximum_independent_mode,policy):
        chain.public_only()
        source_path = HERE/'r613_full_position_height_20261127.py'
        if hashlib.sha256(source_path.read_bytes()).hexdigest() != ORIGINAL_DRIVER_SHA:
            raise RuntimeError('original complete1130q source binding differs')
        self.driver,self.old = original_driver,original_model
        self.compact,self.base = original_driver.compact,original_driver.base
        if not isinstance(original_model,original_driver.FullPositionHeight):
            raise TypeError('the actual original full-position model is required')
        if [int(mode.mode) for mode in original_model.modes] != list(range(2,23,2)):
            raise ValueError('every original true inner/connector/core mode must remain present')
        self.identity = frozen_identity
        for raw,digest in ((frozen_identity.source_state_json,frozen_identity.source_state_sha256),
                (frozen_identity.mathematical_field_json,frozen_identity.mathematical_field_sha256)):
            if hashlib.sha256(raw.encode()).hexdigest() != digest:
                raise ValueError('complete frozen identity literal bytes differ')
        payload = (frozen_identity.source_state_sha256+'\n'
                   +frozen_identity.mathematical_field_sha256+'\n').encode()
        if hashlib.sha256(payload).hexdigest() != frozen_identity.target_sha256:
            raise ValueError('complete frozen target identity differs')
        definition = json.loads(frozen_identity.mathematical_field_json)
        reference_source = json.loads(frozen_identity.source_state_json)
        required = ('actual_accepted_q_sha256','completed_public_origin',
            'reconstruction_source_sha256','all_source_sha256','radial_domain',
            'accurate_inner_tail_definition','complete_connector_core_definition',
            'all_literal_parameters','unresolved_evaluation_errors')
        if any(key not in definition for key in required):
            raise ValueError('a whole mathematical field definition, not radial samples, is required')
        if (definition.get('canonical_mean_points') != 512
                or definition.get('metric_definition') != 'continuous_turning_root_of_this_fixed_reference_height'
                or definition.get('metric_derivative_definition') != '2_W_Wr_plus_2_continuous_weighted_G_mean'
                or reference_source['actual_1130q_JSON'] != actual_q_json
                or reference_source['origin'] != definition['completed_public_origin']
                or reference_source['amplitude'] != amplitude):
            raise ValueError('actual completed reference, canonical height, or fixed-root definition changed')
        reconstruction_text = _reconstruction_text(frozen_identity)
        if hashlib.sha256(reconstruction_text.encode()).hexdigest() != definition['reconstruction_source_sha256']:
            raise ValueError('same complete original mouths and reconstruction identity differ')
        registered = _RESTORED_ORIGINALS.get(original_model)
        if (registered is None or registered[0] is not original_driver
                or registered[1]['target_sha256'] != frozen_identity.target_sha256
                or registered[1]['reconstruction_source_sha256'] != definition['reconstruction_source_sha256']
                or vars(original_model.args) != json.loads(registered[1]['original_reconstruction_arguments_JSON'])):
            raise ValueError('use restore_from_frozen_reference; arbitrary original objects have no bound provenance')
        self.original_reconstruction_receipt = dict(registered[1])
        repository_root = HERE.parents[2]
        for filename,digest in definition['all_source_sha256'].items():
            path = (repository_root/filename).resolve()
            if not path.is_relative_to(repository_root) or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                raise ValueError('full frozen mathematical-source binding differs: '+filename)
        if hashlib.sha256(actual_q_json.encode()).hexdigest() != definition['actual_accepted_q_sha256']:
            raise ValueError('literal accepted reference q differs from frozen field identity')
        self.q_reference = np.asarray(json.loads(actual_q_json),dtype=float)
        if (self.q_reference.shape != (1130,) or self.old.nq != 1130
                or not np.all(np.isfinite(self.q_reference)) or amplitude != 1e-5):
            raise ValueError('all original1130q and original non-small-backoff amplitude required')
        self.amplitude,self.par = float(amplitude),self.old.par
        self.minimum,self.deadline = self.old.minimum,self.old.deadline
        self.original_q_json = actual_q_json
        self.policy = json.loads(json.dumps(policy,sort_keys=True,separators=(',',':'),allow_nan=False))
        self.response_model_sha256 = _json_sha({'target_sha256':self.identity.target_sha256,
            'actual_q_sha256':definition['actual_accepted_q_sha256'],
            'maximum_independent_mode':maximum_independent_mode,'policy':self.policy,
            'original_reconstruction_arguments_sha256':registered[1]['original_reconstruction_arguments_sha256'],
            'complete_height_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'complete_chain_source_sha256':CHAIN_SHA})
        self.J = int(maximum_independent_mode)
        if self.J < 32 or self.J%2:
            raise ValueError('nested independent even band must include all original modes through32')
        self.modes = np.arange(2,self.J+1,2,dtype=int)
        self.core_modes = np.arange(2,2*self.J+1,2,dtype=int)
        self.extra_compact_modes = np.arange(34,self.J+1,2,dtype=int)
        self.core_free_modes = np.arange(4,self.J+1,2,dtype=int)
        self.tail_degrees = np.asarray(policy['tail_degrees'],dtype=int)
        if (self.tail_degrees.ndim != 1 or len(self.tail_degrees) == 0
                or not np.array_equal(self.tail_degrees,np.arange(len(self.tail_degrees)))):
            raise ValueError('all radial tail polynomial degrees0..K must be retained')
        for key in ('mean_points','core_points'):
            if int(policy[key]) != policy[key] or policy[key]%4 or policy[key] <= 4*self.J:
                raise ValueError('fixed mean/core rules must resolve every2J polynomial mode')
        if (set(policy['mean_bracket_radius']) != {'lambda','shift','zeta'}
                or min(policy['mean_bracket_radius'].values()) <= 0
                or not policy['root_tolerance'] > 0 or int(policy['root_steps']) < 1):
            raise ValueError('explicit whole reference-chart bracket policy required')
        self.tail_left,self.tail_right = float(policy['tail_cutoff_left']),float(policy['tail_cutoff_right'])
        self.tail_denominator = float(policy['tail_gaussian_denominator'])
        self.core_lift_left = float(policy['core_lift_cutoff_left'])
        self.core_lift_right = float(policy['core_lift_cutoff_right'])
        if not (self.base.R0 <= self.tail_left < self.tail_right <= self.driver.complete.CORE_LEFT):
            raise ValueError('analytic tail cutoff must overlap the body and vanish before the core')
        if not (self.par.core_start < self.core_lift_left < self.driver.complete.CORE_LEFT
                and self.core_lift_left < self.core_lift_right < self.par.R):
            raise ValueError('new core P0 lift must overlap compact support, not leave a common zero seam')
        if not (0 < self.tail_denominator <= 40):
            raise ValueError('declared rapid-flat tail must retain the R618 quadratic-source exponent margin')
        self.old_count = 1129
        self.compact_count = len(self.extra_compact_modes)*self.compact.COMPACT_NB
        self.tail_count = len(self.modes)*len(self.tail_degrees)
        self.core_free_count = len(self.core_free_modes)
        self.compact_start = self.old_count
        self.tail_start = self.compact_start+self.compact_count
        self.core_start = self.tail_start+self.tail_count
        self.tau_index = self.core_start+self.core_free_count
        self.nq = self.tau_index+1
        self.cache,self.target_cache,self.radial_lift_cache = {},{},{}
        self.original_work_radii = self.compact.radial_grid(self.old,1)
        self.original_fine_radii = self.compact.radial_grid(self.old,2)
        self.last_trace_key,self.last_trace = None,None
        original_trace = self.old.core_trace(self.q_reference,self.amplitude)
        self.pc_reference = _pad(original_trace['pc'],len(self.modes))
        self.pr_reference = _pad(original_trace['prc'],len(self.core_modes))
        self.original_core_correction = _pad(original_trace['cc'],len(self.core_modes))
        self.P1_reference = self.pr_reference+self.original_core_correction
        self.core_theta = 2*np.pi*np.arange(int(policy['core_points']))/int(policy['core_points'])
        self.core_cos = np.cos(self.modes[:,None]*self.core_theta)
        self.core_sin = np.sin(self.modes[:,None]*self.core_theta)
        self.core_all_cos = np.cos(self.core_modes[:,None]*self.core_theta)
        self.core_target_reference = self._core_target(self.pc_reference)
        self.core_delta_reference = self.core_target_reference['target']-self.P1_reference
        u = self.core_target_reference['u']
        Ptt = self.core_target_reference['Ptt']
        P1 = self.P1_reference@self.core_all_cos
        self.frozen_core_e = self.core_target_reference['e']
        self.frozen_core_er = -2*(np.mean(P1/u**3)
            +np.mean(Ptt/u)/(self.par.R*(1+self.par.alpha)))/np.mean(u**-3)
        self.frozen_finite_profile = replace(self.par,gain_height=float(self.q_reference[0]))
        COUNTS['models_constructed_without_replaying_inner_mouths'] += 1

    def initial_response(self):
        """Literal zero response and tau0; no reference q is manufactured."""
        chain.public_only()
        return np.zeros(self.nq)

    def _check_response(self,response):
        value = np.asarray(response,dtype=float)
        if value.shape != (self.nq,) or not np.all(np.isfinite(value)) or not 0 <= value[self.tau_index] <= 1:
            raise ValueError('complete finite response and tau in[0,1] required')
        self.driver.check(self.deadline)
        return value

    def _field_identity(self,response,data,*,include_angles=True):
        """Exact field/grid identity; no scientific values are recomputed."""
        identity = {'same_frozen_target_sha256':self.identity.target_sha256,
            'response_model_sha256':self.response_model_sha256,
            'response_sha256':_json_sha(np.asarray(response,dtype=float).tolist()),
            'radial_grid_sha256':_array_sha(data['r'])}
        if data.get('response_model_sha256') != self.response_model_sha256:
            raise ValueError('prepared data belongs to another response model')
        keys = ['radial_grid_sha256']
        if include_angles:
            identity.update(position_angle_grid_sha256=_array_sha(data['theta']),
                fixed_mean_angle_grid_sha256=_array_sha(data['fixed_mean_data']['theta']))
            keys += ['position_angle_grid_sha256','fixed_mean_angle_grid_sha256']
        if any(data.get(key) != identity[key] for key in keys):
            raise ValueError('prepared radial or angular grid changed after its fields were formed')
        return identity

    def _require_same_state(self,response,data,state):
        expected = self._field_identity(response,data)
        if (not np.array_equal(response,state.get('response'))
                or any(state.get(key) != value for key,value in expected.items())):
            raise ValueError('state must have the same target, response, model and complete grids')
        return expected

    def _core_target(self,pc):
        """One same continuous e(P) approximated by its fixed angular rule.

        The polynomial and its parameter derivative use exact finite Laurent
        convolution, so modes above the old44 or an output Nyquist are never
        silently dropped. The mean root/roundoff error remains unresolved.
        """
        self.driver.check(self.deadline)
        COUNTS['complete_core_target_attempts'] += 1
        P,Pt,Ptt = pc@self.core_cos,-(pc*self.modes)@self.core_sin,-(pc*self.modes**2)@self.core_cos
        reference = float(np.max(-2*P))
        def function(gap):
            u2 = gap+reference+2*P
            if np.any(u2 <= 0):
                raise ArithmeticError('continuous-core root approximation left positivity')
            u = np.sqrt(u2)
            return float(np.mean((1-u2)/(u*(1+u)))),float(-.5*np.mean(u**-3)),u
        # The small noncircular core has u^2 close to1. The strict left
        # endpoint stays positive rather than evaluating a singular gap0.
        left = np.finfo(float).eps*max(1.,abs(reference))
        right = 2.+float(np.max(abs(2*P)))
        gap,u,receipt = chain._root(function,left,right,-1,1.,int(self.policy['root_steps']),
            float(self.policy['root_tolerance']),'core_scalar_root_evaluations')
        e = gap+reference
        den = np.mean(u**-3)
        de_pc = -2*np.mean(self.core_cos/u[None,:]**3,axis=1)/den
        J,c,R = self.J,self.par.alpha/(1+self.par.alpha),self.par.R
        indexes = np.arange(-J,J+1)
        a = np.zeros(2*J+1,dtype=complex)
        a[J+self.modes] = pc/2
        a[J-self.modes] = pc/2
        at,att = 1j*indexes*a,-indexes*indexes*a
        u2poly = 2*a.copy();u2poly[J] += e
        S = .5*float(np.sum(self.modes**2*pc*pc))
        poly = (c*np.convolve(u2poly,att)-np.convolve(at,at))/R
        poly[2*J] += (2*c+1)*S/R
        target = 2*np.real(poly[2*J+self.core_modes])
        jac = np.empty((len(self.core_modes),len(self.modes)))
        constant_derivative = np.empty(len(self.modes))
        for column,j in enumerate(self.modes):
            COUNTS['complete_core_laurent_parameter_columns'] += 1
            h = np.zeros_like(a);h[J+j] = h[J-j] = .5
            ht,htt = 1j*indexes*h,-indexes*indexes*h
            du2 = 2*h.copy();du2[J] += de_pc[column]
            dpoly = (c*(np.convolve(du2,att)+np.convolve(u2poly,htt))
                     -2*np.convolve(at,ht))/R
            dpoly[2*J] += (2*c+1)*j*j*pc[column]/R
            jac[:,column] = 2*np.real(dpoly[2*J+self.core_modes])
            constant_derivative[column] = float(np.real(dpoly[2*J]))
        COUNTS['complete_core_target_evaluations'] += 1
        COUNTS['complete_core_root_angular_points'] += len(P)
        return {'pc':pc.copy(),'e':float(e),'u':u,'P':P,'Pt':Pt,'Ptt':Ptt,'S':S,
            'de_pc':de_pc,'target':target,'target_jac_pc':jac,'root_receipt':receipt,
            'constant_roundoff_observation':float(abs(poly[2*J])),
            'constant_derivative_roundoff_observation':constant_derivative,
            'all_dependent_modes':self.core_modes.copy(),
            'continuous_root_and_roundoff_certified':False}

    def _core_linear_directions(self,indices):
        nc = len(indices)
        dpc = np.zeros((len(self.modes),nc))
        dpr = np.zeros((len(self.core_modes),nc))
        dtau = np.zeros(nc)
        oldm = self.driver.MODES
        c = self.par.alpha/(1+self.par.alpha)
        for local,index in enumerate(indices):
            if index < self.old_count:
                oldindex = int(index)+1
                if oldindex < self.old.nm:
                    dpc[oldindex,local] = -(oldm[oldindex]**2-1)/self.par.R*self.amplitude
                    dpr[oldindex,local] = -c/self.par.R*oldm[oldindex]**2*dpc[oldindex,local]
                elif oldindex < self.compact.OLD_NQ:
                    mode,bsindex = divmod(oldindex-self.old.nm,self.old.nb)
                    dpr[mode,local] = self.amplitude*self.old.core_k*(self.par.alpha+2)/self.old.bulk_scale*self.old.core_B[bsindex]
            elif self.core_start <= index < self.tau_index:
                j = self.core_free_modes[index-self.core_start]
                dpc[j//2-1,local] = self.amplitude
            elif index == self.tau_index:
                dtau[local] = 1.
        return dpc,dpr,dtau

    def core_trace(self,response):
        response = self._check_response(response)
        key = response.tobytes()
        if key == self.last_trace_key:
            return self.last_trace
        indices = np.arange(self.nq)
        dpc,dpr,_ = self._core_linear_directions(indices)
        pc = self.pc_reference+dpc@response
        pr_delta = dpr@response
        if np.array_equal(pc,self.pc_reference):
            target = self.core_target_reference
        else:
            target = self._core_target(pc)
        tau = float(response[self.tau_index])
        correction_delta = (target['target']-self.core_target_reference['target']
                            -pr_delta+tau*self.core_delta_reference)
        P1_coeff = target['target']-(1-tau)*self.core_delta_reference
        P1 = P1_coeff@self.core_all_cos
        u,Ptt,Pt,P = [target[k] for k in ('u','Ptt','Pt','P')]
        er = -2*(np.mean(P1/u**3)+np.mean(Ptt/u)/(self.par.R*(1+self.par.alpha)))/np.mean(u**-3)
        c = self.par.alpha/(1+self.par.alpha)
        D = -self.par.R*P1+c*u*u*Ptt-Pt*Pt-self.par.R*er/2
        delta = self.core_delta_reference@self.core_all_cos
        expected = self.par.R*(1-tau)*(delta-np.mean(delta/u**3)/np.mean(u**-3))
        result = dict(target)
        result.update(tau=tau,correction_delta=correction_delta,P1_coeff=P1_coeff,P1=P1,
            zeta=(target['e']-self.frozen_core_e)/2,
            zeta_r=(er-self.frozen_core_er)/2,effective_e_r=float(er),D=D,
            fixed_e=self.frozen_core_e,fixed_e_r=self.frozen_core_er,
            full_tau_core_identity_difference_observation=float(np.max(abs(D-expected))),
            complete_core_D_observation=float(np.max(abs(D))),
            original_j2_core_amplitude_unchanged=bool(pc[0] == self.pc_reference[0]),
            tau_equals_one_target_core_map_selected=bool(tau == 1.),
            all_2J_dependent_modes_in_actual_height=True)
        self.last_trace_key,self.last_trace = key,result
        return result

    def core_direction(self,trace,indices):
        dpc,dpr,dtau = self._core_linear_directions(indices)
        dtarget = trace['target_jac_pc']@dpc
        dcc = dtarget-dpr+self.core_delta_reference[:,None]*dtau
        dP = self.core_cos.T@dpc
        dPt = -self.core_sin.T@(self.modes[:,None]*dpc)
        dPtt = -self.core_cos.T@(self.modes[:,None]**2*dpc)
        de = trace['de_pc']@dpc
        dP1 = self.core_all_cos.T@(dtarget+self.core_delta_reference[:,None]*dtau)
        u,P1,Ptt = [trace[k][:,None] for k in ('u','P1','Ptt')]
        du = (de[None,:]+2*dP)/(2*u)
        den = np.mean(u**-3,axis=0)
        dden = np.mean(-3*du/u**4,axis=0)
        dnum = (np.mean(dP1/u**3-3*P1*du/u**4,axis=0)
                +np.mean(dPtt/u-Ptt*du/u**2,axis=0)/(self.par.R*(1+self.par.alpha)))
        der = -2*dnum/den-trace['effective_e_r']*dden/den
        c = self.par.alpha/(1+self.par.alpha)
        dD = (-self.par.R*dP1+c*((de[None,:]+2*dP)*Ptt+u*u*dPtt)
              -2*trace['Pt'][:,None]*dPt-self.par.R*der[None,:]/2)
        return {'correction_delta':dcc,'P':dP,'Pt':dPt,'Ptt':dPtt,'P1':dP1,
            'e':de,'zeta':de/2,'zeta_r':der/2,'effective_e_r':der,'D':dD,
            'fixed_e':np.zeros(len(indices)),'fixed_e_r':np.zeros(len(indices)),
            'all_tau_and_implicit_core_root_terms_retained':True}

    def _W_at_core_delta(self,delta):
        COUNTS['new_core_lift_W_integrand_queries'] += 1
        if delta <= 0:
            return np.inf
        r = self.par.R-delta
        finite = float(self.base.gain.finite_slope(self.frozen_finite_profile,np.asarray([r]))[0][0])
        span = self.par.R-self.par.core_start
        t = 1-delta/span
        if t <= 0:
            return finite
        denominator = (delta/span)*(2-delta/span)
        chi = float(self.base.step2(np.asarray([t/self.base.CORE_ONSET_FRACTION]))[0][0])
        return finite+chi*self.par.core_scale*t**self.par.beta/denominator**self.par.alpha

    def _core_lift(self,r,W,Wr):
        left,right = self.core_lift_left,self.core_lift_right
        chi,chir,chirr = self.base.step2((r-left)/(right-left))
        chir /= right-left;chirr /= (right-left)**2
        A = np.zeros(len(r));errors = np.zeros(len(r))
        exponent = 1/(1-self.par.alpha)
        for index in np.flatnonzero(r > left):
            value = float(r[index])
            if value not in self.radial_lift_cache:
                delta = self.par.R-value
                def integrand(x):
                    self.driver.check(self.deadline)
                    if x == 0:
                        return 0.
                    distance = delta*x**exponent
                    return delta*exponent*x**(exponent-1)/self._W_at_core_delta(distance)
                integral,error = quad(integrand,0.,1.,epsabs=float(self.policy['core_lift_epsabs']),
                    epsrel=float(self.policy['core_lift_epsrel']),limit=int(self.policy['quadrature_limit']))
                self.radial_lift_cache[value] = (-float(integral),float(error))
                COUNTS['new_core_lift_radial_integrals'] += 1
            A[index],errors[index] = self.radial_lift_cache[value]
        Ar = np.zeros(len(r));Arr = np.zeros(len(r))
        active = r > left
        Ar[active] = 1/W[active]
        Arr[active] = -Wr[active]/W[active]**2
        lift = np.stack([chi*A,chir*A+chi*Ar,chirr*A+2*chir*Ar+chi*Arr],axis=1)
        return lift,errors

    def _tail_columns(self,r):
        """Explicit true rapid-flat jets, NEVER zero below a numerical mouth.

        The exact function is exp(-(u^2-u_left^2)/a)*x^k*chi(r),
        u=ELL/(r-rc), x=(r-rc)/(right-rc), and a<=40. At rc it is
        defined by its true infinite-order zero germ. Finite floating
        underflow is reported; it is not a new mathematical zero interval.
        """
        rc,ell = self.base.RC,self.base.ELL
        columns = np.zeros((len(r),len(self.tail_degrees),3))
        active = (r > rc)&(r < self.tail_right)
        rr = r[active];u = ell/(rr-rc)
        x = (rr-rc)/(self.tail_right-rc)
        anchor = ell/(self.tail_left-rc)
        logg = -(u*u-anchor*anchor)/self.tail_denominator
        g = np.exp(logg)
        l1 = 2*u**3/(self.tail_denominator*ell)
        l2 = -6*u**4/(self.tail_denominator*ell*ell)
        gr,grr = g*l1,g*(l1*l1+l2)
        cut,cutr,cutrr = self.base.step2((rr-self.tail_left)/(self.tail_right-self.tail_left))
        cut,cutr,cutrr = 1-cut,-cutr/(self.tail_right-self.tail_left),-cutrr/(self.tail_right-self.tail_left)**2
        a0,a1,a2 = g*cut,gr*cut+g*cutr,grr*cut+2*gr*cutr+g*cutrr
        width = self.tail_right-rc
        for column,k in enumerate(self.tail_degrees):
            z0 = x**k
            z1 = np.zeros_like(x) if k == 0 else k*x**(k-1)/width
            z2 = np.zeros_like(x) if k < 2 else k*(k-1)*x**(k-2)/width**2
            columns[active,column,:] = np.stack([a0*z0,a1*z0+a0*z1,
                a2*z0+2*a1*z1+a0*z2],axis=1)
        COUNTS['analytic_true_tail_radial_points'] += len(rr)
        COUNTS['analytic_true_tail_threejet_values'] += int(columns.size)
        COUNTS['analytic_true_tail_exponential_underflow_observations'] += int(np.count_nonzero(g == 0))
        return columns

    def _angular_view(self,radial,ntheta):
        data = dict(radial)
        theta = 2*np.pi*np.arange(int(ntheta))/int(ntheta)
        data['theta'] = theta
        data['cos'] = np.cos(np.asarray(self.base.MODES)[:,None]*theta)
        data['sin'] = np.sin(np.asarray(self.base.MODES)[:,None]*theta)
        data['column_cos'] = np.cos(self.old.column_modes[:,None]*theta)
        data['column_sin'] = np.sin(self.old.column_modes[:,None]*theta)
        data['core_all_cos'] = np.cos(self.driver.CORE_MODES[:,None]*theta)
        data['core_all_sin'] = np.sin(self.driver.CORE_MODES[:,None]*theta)
        data['forced_cos4'],data['forced_sin4'] = np.cos(4*theta),np.sin(4*theta)
        data['paid_height_cache'] = {}
        return data

    def _complete_radial_data(self,data):
        r = data['r']
        dh = self.q_reference[0]-self.par.gain_height
        W,Wr = data['w0']+dh*data['gain_w'],data['wr0']+dh*data['gain_wr']
        if np.any(W <= 0):
            raise ArithmeticError('the frozen original W left its positive interior domain')
        data['frozen_W'],data['frozen_Wr'] = W,Wr
        # All28 original compact radial functions are reused, not rebuilt.
        first = self.compact.OLD_NQ-1
        data['compact_radial_dictionary'] = data['new_columns'][:,first:first+self.compact.COMPACT_NB,:]
        if data['compact_radial_dictionary'].shape[1] != self.compact.COMPACT_NB:
            raise ValueError('all original compact radial basis columns required')
        data['new_core_lift'],data['new_core_lift_quad_error_observation'] = self._core_lift(r,W,Wr)
        data['analytic_tail_columns'] = self._tail_columns(r)
        return data

    def prepare(self,r,ntheta):
        chain.public_only()
        r = np.asarray(r,dtype=float)
        if len(r) < 2 or np.any(np.diff(r) <= 0) or ntheta%4 or ntheta <= 4*self.J:
            raise ValueError('all ordered original radial points and every2J output mode required')
        required = self.original_work_radii if ntheta < 512 else self.original_fine_radii
        if not np.all(np.isin(required,r)):
            raise ValueError('a new grid may add points but cannot discard any original retained radius')
        key = (r.tobytes(),int(ntheta))
        if key in self.cache:
            return self.cache[key]
        data = dict(self.old.prepare(r,int(ntheta)))
        self._complete_radial_data(data)
        mean = self._angular_view(data,int(self.policy['mean_points']))
        data['fixed_mean_data'] = mean
        data['growing_core_cos'] = np.cos(self.core_modes[:,None]*data['theta'])
        data['growing_core_sin'] = np.sin(self.core_modes[:,None]*data['theta'])
        odd = np.arange(1,int(ntheta)//2,2,dtype=int)
        data['all_position_odd_modes'] = odd
        data['complete_position_projection'] = self.driver.position.projection(data['theta'],odd)
        dr = np.empty_like(r)
        dr[0],dr[-1] = (r[1]-r[0])/2,(r[-1]-r[-2])/2
        dr[1:-1] = (r[2:]-r[:-2])/2
        data['position_radial_units'] = np.sqrt(dr/dr.sum())
        data.update(response_model_sha256=self.response_model_sha256,
            radial_grid_sha256=_array_sha(data['r']),
            position_angle_grid_sha256=_array_sha(data['theta']),
            fixed_mean_angle_grid_sha256=_array_sha(data['fixed_mean_data']['theta']))
        self.cache[key] = data
        return data

    def _reference_jets(self,data):
        if 'literal_reference_jets' not in data:
            values = self.old.height_jets(self.q_reference,self.amplitude,data)
            data['literal_reference_jets'] = dict(zip(JET_KEYS,values))
        return data['literal_reference_jets']

    def height_jets(self,response,data,trace=None):
        chain.public_only()
        COUNTS['complete_height_evaluation_attempts'] += 1
        response = self._check_response(response)
        if trace is None:
            trace = self.core_trace(response)
        reference = self._reference_jets(data)
        old_delta = np.r_[0.,response[:self.old_count]]
        plain = dict(zip(JET_KEYS,self.old.delta_jets(old_delta,self.amplitude,data)))
        answer = {key:reference[key]+plain[key] for key in JET_KEYS}
        correction = _separable(data['core_radial'],trace['correction_delta'],self.core_modes,data['theta'])
        for key in JET_KEYS:
            answer[key] += correction[key]
        for start,count,modes,radial in (
                (self.compact_start,self.compact_count,self.extra_compact_modes,data['compact_radial_dictionary']),
                (self.tail_start,self.tail_count,self.modes,data['analytic_tail_columns'])):
            if count == 0:
                continue
            coefficients = self.amplitude*response[start:start+count].reshape(len(modes),radial.shape[1])
            fields = np.einsum('rbk,jb->rjk',radial,coefficients)
            co,si = np.cos(modes[:,None]*data['theta']),np.sin(modes[:,None]*data['theta'])
            extra = (fields[:,:,0]@co,fields[:,:,1]@co,fields[:,:,2]@co,
                -(fields[:,:,0]*modes)@si,-(fields[:,:,0]*modes*modes)@co,
                -(fields[:,:,1]*modes)@si)
            for key,value in zip(JET_KEYS,extra):
                answer[key] += value
        core_free = _separable(data['new_core_lift'],
            self.amplitude*response[self.core_start:self.tau_index],self.core_free_modes,data['theta'])
        for key in JET_KEYS:
            answer[key] += core_free[key]
        COUNTS['actual_complete_height_radial_angular_points'] += int(answer['f'].size)
        return answer

    def height_direction(self,trace,indices,data,core_block=None):
        chain.public_only()
        nr,nt,nc = len(data['r']),len(data['theta']),len(indices)
        answer = {key:np.zeros((nr,nt,nc)) for key in JET_KEYS}
        theta = data['theta']
        for local,index in enumerate(indices):
            radial = None
            if index < self.old_count:
                radial = self.amplitude*data['new_columns'][:,index,:]
                j = self.old.column_modes[index]
            elif index < self.tail_start:
                mode,basis = divmod(index-self.compact_start,self.compact.COMPACT_NB)
                radial = self.amplitude*data['compact_radial_dictionary'][:,basis,:]
                j = self.extra_compact_modes[mode]
            elif index < self.core_start:
                mode,basis = divmod(index-self.tail_start,len(self.tail_degrees))
                radial = self.amplitude*data['analytic_tail_columns'][:,basis,:]
                j = self.modes[mode]
            elif index < self.tau_index:
                radial = self.amplitude*data['new_core_lift']
                j = self.core_free_modes[index-self.core_start]
            if radial is not None:
                co,si = np.cos(j*theta),np.sin(j*theta)
                values = (radial[:,0,None]*co,radial[:,1,None]*co,radial[:,2,None]*co,
                    -j*radial[:,0,None]*si,-j*j*radial[:,0,None]*co,-j*radial[:,1,None]*si)
                for key,value in zip(JET_KEYS,values):
                    answer[key][:,:,local] = value
        core = self.core_direction(trace,indices) if core_block is None else core_block
        coefficients = core['correction_delta']
        co,si = np.cos(self.core_modes[:,None]*theta),np.sin(self.core_modes[:,None]*theta)
        a = co.T@coefficients
        at = -si.T@(self.core_modes[:,None]*coefficients)
        att = -co.T@(self.core_modes[:,None]**2*coefficients)
        v,vr,vrr = data['core_radial'].T
        values = (v[:,None,None]*a,vr[:,None,None]*a,vrr[:,None,None]*a,
            v[:,None,None]*at,v[:,None,None]*att,vr[:,None,None]*at)
        for key,value in zip(JET_KEYS,values):
            answer[key] += value
        COUNTS['actual_complete_height_direction_columns_at_radii'] += nr*nc
        return answer,core

    def _target(self,data,index):
        r = float(data['r'][index])
        if r not in self.target_cache:
            reference = {key:value[index] for key,value in self._reference_jets(data).items()}
            self.target_cache[r] = chain.frozen_reference_metric(r,
                data['frozen_W'][index],data['frozen_Wr'][index],reference,
                inner_chart=r <= float(self.compact.PATCH_KNOTS[0][0]),
                root_steps=int(self.policy['root_steps']),root_tolerance=float(self.policy['root_tolerance']),
                target_sha256=self.identity.target_sha256)
        return self.target_cache[r]

    def _mean_state(self,target,jets,seed=0.,literal_zero=False):
        chart = 'lambda' if target['inner_chart'] else ('zeta' if target['W'] >= 1 else 'shift')
        if literal_zero:
            # Exact reference identity: E* was defined from this very field.
            # Numerical residual observations are retained rather than used
            # to manufacture a nonzero correction to the literal old height.
            state = chain._connection(chain.geometry_from_split(target,jets,0.,chart),0.)
            state['root_receipt'] = {'exact_same_reference_definition_used':True,
                'floating_residual_observation':state['root_value'],
                'continuous_root_errors_certified':False}
            return state
        width = float(self.policy['mean_bracket_radius'][chart])
        return chain.solve_mean(target,jets,chart=chart,bracket=(-width,width),seed=seed,
            root_steps=int(self.policy['root_steps']),root_tolerance=float(self.policy['root_tolerance']))

    def evaluate(self,response,data,accepted_mean_seed=None):
        chain.public_only()
        COUNTS['complete_fixed_metric_evaluation_attempts'] += 1
        response = self._check_response(response)
        field_identity = self._field_identity(response,data)
        trace = self.core_trace(response)
        mean_data = data['fixed_mean_data']
        mean_jets = self.height_jets(response,mean_data,trace)
        output_jets = self.height_jets(response,data,trace)
        mean_states,output_states,positions = [],[],[]
        zero = bool(np.all(response == 0))
        for index,r in enumerate(data['r']):
            self.driver.check(self.deadline)
            target = self._target(mean_data,index)
            seed = 0. if accepted_mean_seed is None else accepted_mean_seed[index]['x']
            mean = self._mean_state(target,{k:v[index] for k,v in mean_jets.items()},seed,zero)
            state = chain.state_on_output_grid(mean,{k:v[index] for k,v in output_jets.items()})
            position = chain.position_state(state,data['theta'],data['primitive'])
            mean_states.append(mean);output_states.append(state);positions.append(position)
        S = np.stack([p['S'] for p in positions])
        co,si = data['complete_position_projection']
        values = np.stack([S[:,:,0]@co.T,S[:,:,1]@si.T],axis=1)
        residual = (values*data['position_radial_units'][:,None,None]/self.amplitude).ravel()
        if not np.all(np.isfinite(residual)):
            raise ArithmeticError('nonfinite complete fixed-E position residual')
        COUNTS['complete_fixed_metric_evaluations'] += 1
        return {**field_identity,'response':response.copy(),'core':trace,'mean_jets':mean_jets,
            'height_jets':output_jets,'mean_states':mean_states,'output_states':output_states,
            'positions':positions,'S':S,'residual':residual,
            'conditional_eta_identity_observation':float(max(np.max(p['eta']) for p in positions)),
            'max_abs_output_mean_a_minus_one_observation':float(max(abs(p['output_mean_a_minus_one_observation']) for p in positions)),
            'max_abs_output_mean_R_alias_observation':float(max(abs(p['output_mean_R_alias_observation']) for p in positions)),
            'max_abs_output_Nyquist_a_minus_one_observation':float(max(abs(p['output_Nyquist_a_minus_one_observation']) for p in positions)),
            'actual_metric_not_qualified_by_S_alone':True,
            'same_frozen_target_sha256':self.identity.target_sha256,
            'mean_points_independent_of_position_grid':int(self.policy['mean_points']),
            'all_original_mouths_retained':True,'new_tail_is_true_analytic_not_homogeneous_DtN':True,
            'continuous_metric_or_README_certified':False}

    def jacobian(self,response,data,state,block_columns=16):
        chain.public_only()
        COUNTS['complete_fixed_metric_jacobian_attempts'] += 1
        response = self._check_response(response)
        self._require_same_state(response,data,state)
        nr = len(data['r']);co,si = data['complete_position_projection']
        rows_per_r = 2*len(data['all_position_odd_modes'])
        J = np.empty((nr*rows_per_r,self.nq))
        for first in range(0,self.nq,block_columns):
            self.driver.check(self.deadline)
            indices = np.arange(first,min(self.nq,first+block_columns))
            core_block = self.core_direction(state['core'],indices)
            mean_H,_ = self.height_direction(state['core'],indices,data['fixed_mean_data'],core_block)
            output_H,_ = self.height_direction(state['core'],indices,data,core_block)
            projected = np.empty((nr,2,len(data['all_position_odd_modes']),len(indices)))
            for radial_index in range(nr):
                dm = chain.mean_direction(state['mean_states'][radial_index],
                    {k:v[radial_index] for k,v in mean_H.items()})
                ds = chain.output_direction(state['output_states'][radial_index],
                    {k:v[radial_index] for k,v in output_H.items()},dm)
                dS = chain.position_direction(state['output_states'][radial_index],
                    state['positions'][radial_index],ds)
                projected[radial_index,0] = co@dS[:,0,:]
                projected[radial_index,1] = si@dS[:,1,:]
            J[:,indices] = (projected*data['position_radial_units'][:,None,None,None]/self.amplitude).reshape(-1,len(indices))
            COUNTS['complete_fixed_metric_analytic_columns'] += len(indices)
        COUNTS['complete_fixed_metric_analytic_jacobians'] += 1
        if not np.all(np.isfinite(J)):
            raise ArithmeticError('nonfinite full fixed-E height/mean/core/position Jacobian')
        return J

    def exact_tail_source_observation(self,data):
        """True supplied analytic columns' L_j f, not a fake homogeneous mouth.

        These values may be consumed as the real inhomogeneous data in a
        later R618 affine forced-DtN construction. They do not assert the
        nonlinear required source already equals this supplied source.
        """
        chain.public_only()
        r,W,Wr = data['r'],data['frozen_W'],data['frozen_Wr']
        fields = data['analytic_tail_columns']
        result = np.empty((len(r),len(self.modes),len(self.tail_degrees)))
        for index,j in enumerate(self.modes):
            result[:,index,:] = (r[:,None]*W[:,None]*fields[:,:,2]
                +r[:,None]*Wr[:,None]*fields[:,:,1]-j*j*Wr[:,None]*fields[:,:,0])
        COUNTS['analytic_tail_true_source_values'] += int(result.size)
        return {'L_j_columns':result,'exact_formula':'r*W*frr+r*Wr*fr-j*j*Wr*f',
            'source_is_not_zero_or_an_already_solved_nonlinear_forcing':True,
            'finite_inner_mouth_not_replaced_by_zero_below_it':True,
            'continuous_tail_error_certified':False}

    def coefficient_fields(self,response,data,state=None):
        """All raw pre-tanh and post-tanh coefficients, with NO2J clipping.

        This is the actual new field's input to a later shared R606/R615
        error pass. Such a pass must also charge the SAME mean-root and
        fixed-reference errors and the new lift/tail errors; the old
        zero-radial-error observation is not a certificate for this model.
        """
        chain.public_only()
        response = self._check_response(response)
        field_identity = self._field_identity(response,data)
        if state is not None:
            self._require_same_state(response,data,state)
        trace = self.core_trace(response) if state is None else state['core']
        V,L,old_modes = self.driver.majorant.coefficient_fields(self.old,self.q_reference,self.amplitude,data)
        combined = np.zeros((len(data['r']),len(self.core_modes),3))
        for old_index,j in enumerate(old_modes):
            combined[:,j//2-1,:] += L[:,old_index,:]
        for column,j in enumerate(self.old.column_modes):
            combined[:,j//2-1,:] += self.amplitude*response[column]*data['new_columns'][:,column,:]
        combined += data['core_radial'][:,None,:]*trace['correction_delta'][None,:,None]
        for start,count,modes,radial in (
                (self.compact_start,self.compact_count,self.extra_compact_modes,data['compact_radial_dictionary']),
                (self.tail_start,self.tail_count,self.modes,data['analytic_tail_columns'])):
            if count:
                coeff = self.amplitude*response[start:start+count].reshape(len(modes),radial.shape[1])
                fields = np.einsum('rbk,jb->rjk',radial,coeff)
                for index,j in enumerate(modes):
                    combined[:,j//2-1,:] += fields[:,index,:]
        for index,j in enumerate(self.core_free_modes):
            combined[:,j//2-1,:] += (self.amplitude*response[self.core_start+index]
                                    *data['new_core_lift'])
        result = {**field_identity,'pre_tanh_threejet_coefficients':V,
            'all_post_tanh_threejet_coefficients':combined,'all_post_modes':self.core_modes.copy(),
            'fixed_canonical_tanh_mean_points':512,'same_frozen_target_sha256':self.identity.target_sha256,
            'all_original_plus_all_new_post_coefficients_combined_before_norms':True,
            'true_analytic_tail_not_zero_below_numerical_mouth':True,
            'unresolved_errors':['original_true_DtN_and_ODE_evaluation',
                'same_continuous_reference_E_and_Er_evaluation','same_mean_root_and_mean_derivative',
                'new_core_root_and_convolution_roundoff','new_reciprocal_W_lift_quadrature',
                'explicit_tail_float_underflow_and_roundoff','continuous_radial_and_time_coverage'],
            'continuous_metric_majorant_already_certified':False}
        if state is not None:
            W = data['frozen_W'];Wr = data['frozen_Wr']
            s = np.asarray([v['s'] for v in state['mean_states']])
            sr = np.asarray([v['s_r'] for v in state['mean_states']])
            e = np.asarray([v['target']['e'] for v in state['mean_states']])
            er = np.asarray([v['target']['e_r'] for v in state['mean_states']])
            result.update(effective_mean_W=W-s,effective_mean_Wr=Wr-sr,
                effective_split_e=e+2*W*s-s*s,
                effective_split_er=er+2*Wr*s+2*(W-s)*sr,
                effective_split_formed_without_E_minus_large_W_squared=True)
        COUNTS['complete_growing_coefficient_radial_points'] += len(data['r'])
        return result

    def _mean_point_query(self,response,r,trace,indices):
        """Actual field query for the mean-height integral, charging all work.

        Calling the original compact preparer at N4 obtains its full SAME
        radial fields cheaply; N4 is never a scientific angular rule here.
        The height/mean functional is then evaluated at the fixed declared
        mean_points. Two ordered radii are needed by the unchanged original
        radial bookkeeping. No original output row or retained node is lost.
        """
        self.driver.check(self.deadline)
        if r == self.par.R:
            return np.zeros(1+len(indices))
        if not self.minimum <= r < self.par.R:
            raise ValueError('true cap-to-mouth data must cover queries below the numerical mouth')
        partner = float(np.nextafter(r,self.par.R))
        if partner < self.par.R:
            pair,index = np.asarray([r,partner]),0
        else:
            pair,index = np.asarray([np.nextafter(r,self.minimum),r]),1
        key = (pair.tobytes(),4)
        caches = []
        seen = set()
        obj = self.old
        while obj is not None and id(obj) not in seen:
            seen.add(id(obj))
            if hasattr(obj,'cache'):
                caches.append((obj.cache,key,key in obj.cache))
            obj = getattr(obj,'old',None)
        mean_key = (pair.tobytes(),self.amplitude)
        canonical_preexisting = mean_key in self.old.canonical_mean_cache
        try:
            radial = dict(self.compact.CompactResponseHeight.prepare(self.old,pair,4))
            self._complete_radial_data(radial)
            data = self._angular_view(radial,int(self.policy['mean_points']))
            jets = self.height_jets(response,data,trace)
            target = self._target(data,index)
            mean = self._mean_state(target,{k:v[index] for k,v in jets.items()},
                                    literal_zero=bool(np.all(response == 0)))
            result = np.empty(1+len(indices));result[0] = mean['s']
            if len(indices):
                H,_ = self.height_direction(trace,indices,data)
                direction = chain.mean_direction(mean,{k:v[index] for k,v in H.items()})
                result[1:] = direction['s']
            COUNTS['new_mean_height_integrand_queries'] += 1
            COUNTS['new_mean_height_parameter_integrand_values'] += len(indices)
            return result
        finally:
            # These are new quadrature-query caches only. Counters and all
            # existing work/fine caches are untouched; failed calls remain
            # in the cumulative cost ledger.
            for cache,cache_key,preexisting in caches:
                if not preexisting:
                    cache.pop(cache_key,None)
            if not canonical_preexisting:
                self.old.canonical_mean_cache.pop(mean_key,None)

    def integrate_mean_height(self,response,data,tail_anchor,indices=()):
        """Actual Z mean and optional parameter derivative, anchored at rc.

        The mathematical function is h-h_ref=integral_rc^r s(t)dt. The
        unchanged finite-DtN evaluator does not evaluate below its mouth,
        so its true cap-to-first-node integral/error must be supplied with
        explicit provenance. There is NO default zero continuation. At the
        literal zero response s is identically zero by definition, and that
        exact identity needs no new tail approximation.

        scipy's reported quadrature errors are retained as observations,
        never silently upgraded to rigorous enclosures. Endpoint values
        also return the common translation of the central column and the
        reflection center needed to keep the chosen inner held cap fixed.
        """
        chain.public_only()
        response = self._check_response(response)
        indices = np.asarray(indices,dtype=int)
        if (indices.ndim != 1 or np.any(indices < 0) or np.any(indices >= self.nq)
                or len(set(indices.tolist())) != len(indices)):
            raise ValueError('distinct actual parameter directions required')
        field_identity = self._field_identity(response,data,include_angles=False)
        response_sha = field_identity['response_sha256']
        r = np.asarray(data['r'])
        zero = bool(np.all(response == 0))
        if zero and len(indices) == 0:
            return {**field_identity,'mean_height_offset':np.zeros(len(r)),
                'central_column_translation_and_reflection_center_offset':0.,
                'exact_same_reference_zero_entry':True,'same_frozen_target_sha256':self.identity.target_sha256,
                'all_geometric_errors_certified':False}
        if not isinstance(tail_anchor,dict):
            raise ValueError('actual true cap-to-first-node mean integral and provenance required')
        expected = {'target_sha256':self.identity.target_sha256,'response_sha256':response_sha,
            'response_model_sha256':self.response_model_sha256,
            'cap_radius':self.base.RC,'mouth_radius':float(r[0]),'parameter_indices':indices.tolist()}
        for key,value in expected.items():
            if tail_anchor.get(key) != value:
                raise ValueError('true mean-height tail anchor differs: '+key)
        if not tail_anchor.get('true_tail_evidence') or 'unresolved_errors' not in tail_anchor:
            raise ValueError('true infinite-tail provenance and unresolved errors cannot be omitted')
        start = np.asarray(tail_anchor['integral_and_directions'],dtype=float)
        error = np.asarray(tail_anchor['absolute_error_bounds_or_unresolved_radii'],dtype=float)
        if start.shape != (1+len(indices),) or error.shape != start.shape or np.any(error < 0):
            raise ValueError('complete mean and parameter tail integrals/errors required')
        trace = self.core_trace(response)
        values = np.empty((len(r),len(start)));values[0] = start
        cumulative = start.copy();quad_error = 0.
        endpoints = np.r_[r,self.par.R]
        for interval,(left,right) in enumerate(zip(endpoints[:-1],endpoints[1:])):
            self.driver.check(self.deadline)
            value,estimate = quad_vec(lambda t:self._mean_point_query(response,float(t),trace,indices),
                float(left),float(right),epsabs=float(self.policy['mean_height_epsabs']),
                epsrel=float(self.policy['mean_height_epsrel']),
                limit=int(self.policy['quadrature_limit']),norm='max')
            cumulative += value;quad_error += float(estimate)
            if interval+1 < len(r):
                values[interval+1] = cumulative
            COUNTS['new_mean_height_radial_integral_intervals'] += 1
        return {**field_identity,'mean_height_offset':values[:,0],
            'mean_height_parameter_directions':values[:,1:],
            'parameter_indices':indices.copy(),
            'central_column_translation_and_reflection_center_offset':float(cumulative[0]),
            'central_column_translation_parameter_directions':cumulative[1:],
            'tail_anchor_value_and_errors':tail_anchor,
            'quad_error_estimate_observation':quad_error,
            'mean_root_and_quadrature_errors_rigorously_enclosed':False,
            'same_frozen_target_sha256':self.identity.target_sha256,
            'physical_definition_is_true_cap_anchored_integral_not_finite_mouth_zero':True,
            'all_geometric_errors_certified':False}

    def geometry_with_mean_height(self,response,data,state,mean_height):
        """Actual anchored X, complete height jets and angular/mixed X jets.

        The lower half reflects about the returned moving common center;
        the central cylinder translates with that center. Its length is
        unchanged, while the chosen top held cap is fixed by the integral
        anchor. As in the paid source, planar Yrr needs a direct same-position
        derivative readout; it is not supplied by inventing a third height
        jet from these six. No whole-domain/time embedding is claimed.
        """
        chain.public_only()
        response = self._check_response(response)
        field_identity = self._require_same_state(response,data,state)
        mean_identity = self._field_identity(response,data,include_angles=False)
        if any(mean_height.get(key) != value for key,value in mean_identity.items()):
            raise ValueError('mean integral must have the same target, response, model and complete radii')
        f = state['height_jets']
        dh = self.q_reference[0]-self.par.gain_height
        href = data['h0']+dh*data['gain_height']
        offset = np.asarray(mean_height['mean_height_offset'])
        if offset.shape != href.shape:
            raise ValueError('complete mean integral on every original radius required')
        Y = np.stack([v['Y'] for v in state['positions']])
        Z = href[:,None]+offset[:,None]+f['f']
        X = np.concatenate([Y,Z[:,:,None]],axis=2)
        Yr = np.stack([v['Yr'] for v in state['positions']])
        Yt = np.stack([v['Yt'] for v in state['positions']])
        Yrt = np.stack([v['Yrt'] for v in state['positions']])
        Ytt = np.stack([v['Ytt'] for v in state['positions']])
        p = np.stack([v['p'] for v in state['output_states']])
        p0r = np.asarray([v['p0_r'] for v in state['output_states']])
        return {**field_identity,'X':X,'Xr':np.concatenate([Yr,p[:,:,None]],axis=2),
            'Xt':np.concatenate([Yt,f['ft'][:,:,None]],axis=2),
            'Xrt':np.concatenate([Yrt,f['frt'][:,:,None]],axis=2),
            'Xtt':np.concatenate([Ytt,f['ftt'][:,:,None]],axis=2),
            'Zrr':p0r[:,None]+f['frr'],
            'planar_Yrr_requires_same_actual_position_derivative_readout':True,
            'central_column_translation_and_reflection_center_offset':
                mean_height['central_column_translation_and_reflection_center_offset'],
            'same_frozen_target_sha256':self.identity.target_sha256,
            'continuous_embedding_curvature_reach_or_README_certified':False}

    def embed_response(self,response,larger):
        """Literal nested-space embedding; target/reference/amplitude stay fixed."""
        chain.public_only()
        response = self._check_response(response)
        if (larger.identity.target_sha256 != self.identity.target_sha256
                or larger.original_q_json != self.original_q_json or larger.J < self.J
                or larger.amplitude != self.amplitude
                or not np.array_equal(larger.tail_degrees[:len(self.tail_degrees)],self.tail_degrees)):
            raise ValueError('only the same target and nested complete dictionaries may be embedded')
        for key in ('tail_gaussian_denominator','tail_cutoff_left','tail_cutoff_right',
                    'core_lift_cutoff_left','core_lift_cutoff_right'):
            if larger.policy[key] != self.policy[key]:
                raise ValueError('nested tail function definitions changed')
        out = np.zeros(larger.nq)
        out[:self.old_count] = response[:self.old_count]
        for index,j in enumerate(self.extra_compact_modes):
            target = int(np.flatnonzero(larger.extra_compact_modes == j)[0])
            nb = self.compact.COMPACT_NB
            out[larger.compact_start+target*nb:larger.compact_start+(target+1)*nb] = response[self.compact_start+index*nb:self.compact_start+(index+1)*nb]
        for index,j in enumerate(self.modes):
            target = int(np.flatnonzero(larger.modes == j)[0])
            for degree in range(len(self.tail_degrees)):
                out[larger.tail_start+target*len(larger.tail_degrees)+degree] = response[self.tail_start+index*len(self.tail_degrees)+degree]
        for index,j in enumerate(self.core_free_modes):
            target = int(np.flatnonzero(larger.core_free_modes == j)[0])
            out[larger.core_start+target] = response[self.core_start+index]
        out[larger.tau_index] = response[self.tau_index]
        return out

    def cumulative_cost_receipt(self):
        """No resets: failures, root attempts and genuine new queries remain."""
        chain.public_only()
        d = self.driver
        return {'original_reconstruction_provenance':dict(self.original_reconstruction_receipt),
            'response_model_sha256':self.response_model_sha256,
            'new_growing_height_counts':dict(COUNTS),
            'new_fixed_metric_mean_and_position_counts':dict(chain.COUNTS),
            'original_base_counts':dict(d.base.COUNTS),
            'original_forced_counts':dict(d.paid.NEW_COUNTS),
            'original_complete_height_counts':dict(d.complete.COUNTS),
            'original_compact_basis_counts':dict(d.compact.NEW),
            'original_factored_high_mode_counts':dict(d.high.COUNTS),
            'original_paid_mouth_reconstruction_counts':dict(d.resume.NEW),
            'original_coefficient_majorant_counts':dict(d.majorant.COUNTS),
            'original_function_counts':dict(d.parent.EXTRA),
            'original_gain_counts':dict(d.base.gain.COUNTS),
            'original_full_spectrum_counts':dict(d.compact.full.NEW),
            'new_inner_DtN_RHS_for_analytic_tail_columns':0,
            'analytic_tail_columns_not_claimed_homogeneous_or_nonlinearly_solved':True,
            'overlapping_counters_not_disjoint_work':True,
            'prior_scope_costs_remain_in_literal_frozen_source_identity':True}
