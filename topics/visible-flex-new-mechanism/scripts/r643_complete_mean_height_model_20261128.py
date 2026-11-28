#!/usr/bin/env python3
"""R643 complete1566-column same-E model with a true free mean height.

Retain all1472 original hard-tau1 angular response columns, append94 real
mean-height columns, and hard-eliminate both mean core traces by the SAME
current core map.  The fixed accepted seed mean is evaluated once at each
needed radius; trials and every new Jacobian direction have no mean root.
The original cap-to-mouth definition is not replaced by a numerical zero.
"""
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
CENTERED_SHA = 'fe1d8a07343152bc981a94cd00c311b826fc283afa1c6b020e9b7de59c04bda3'
CHAIN_SHA = 'cc11c8514f4fa76ee0e8184cb1bdcc2bad0877ebb62b8214346300c016de5c96'
SEED_RESPONSE_SHA = '19519575f7b4a8100cf9813851c258188ad4a0063edad05eb1b5b332b83f2cc7'
SEED_FINAL_SHA = '1fb5abfdf70e6c8154938b07ec5bd3353b68735c0dd5fd49f704204e65bd024e'
TARGET_SHA = '86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5'
SCHEMA = 'r643-complete1566-free-mean-same-E-model-v1'


def _load(name, filename, digest):
    path = HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError('source-bound coupled component changed: '+filename)
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


centered = _load('r643_original_centered_seed','r618_fourier_centered_model_20261128.py',CENTERED_SHA)
explicit = _load('r643_actual_explicit_mean_chain','r643_unsolved_mean_fixed_metric_chain_20261128.py',CHAIN_SHA)
height = centered.height


def _sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
                                     allow_nan=False).encode()).hexdigest()


class CompleteMeanHeight:
    @staticmethod
    def policy_descriptor():
        return {
            'schema':SCHEMA,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'owned_centered_model_source_sha256':CENTERED_SHA,
            'explicit_chain_policy':explicit.UnsolvedMeanChain.policy_descriptor(),
            'seed_run_id':46117718197,'seed_job_id':140895158286,
            'seed_source_commit':'19de4da31f4f6139a2547f2ada7949271a492a00',
            'seed_FINAL_sha256':SEED_FINAL_SHA,
            'seed_response_sha256':SEED_RESPONSE_SHA,
            'same_target_sha256':TARGET_SHA,
            'mean_plateau_left':.50,'mean_plateau_right':.65,
            'mean_bulk_columns':61,'mean_compact_columns':28,'mean_tail_columns':4,
            'mean_plateau_columns':1,'all_mean_columns':94,
            'all_old_hard_tau_columns':1472,'all_new_free_columns':1566,
            'mean_parameter_height_unit':1e-5,
            'mean_core_trace_policy':'same_numerical_current_core_root_and_complete_weighted_derivative',
            'continuous_core_trace_formula':'R643_equations_22_23',
            'all_F_and_rG_rows_retained':True,
            'same_frozen_E_and_reference_H_amplitude':True,
            'finite_seed_mean_evaluations_do_not_certify_continuous_seed_branch':True,
        }

    def __init__(self, owned, seed_response, natural_terminal, policy, safe_point=None):
        centered.chain.public_only()
        if type(owned) is not centered.FourierCenteredHeight:
            raise TypeError('one genuinely source-bound original centered model required')
        owned.guard()
        if policy != self.policy_descriptor():
            raise ValueError('complete mean-space identity must precede all new arithmetic')
        literal = natural_terminal['literal_FINAL_JSON']
        final = json.loads(literal)
        if (hashlib.sha256(literal.encode()).hexdigest()!=SEED_FINAL_SHA
                or natural_terminal['run_id']!=46117718197
                or natural_terminal['job_id']!=140895158286
                or natural_terminal['source_commit']!='19de4da31f4f6139a2547f2ada7949271a492a00'
                or final['actual_response_identity']['sha256']!=SEED_RESPONSE_SHA
                or final['actual_checkpoint']['hard_tau']!=1.
                or final['same_frozen_target_sha256']!=TARGET_SHA):
            raise ValueError('only the real completed centered terminal may supply the fixed mean seed')
        self.seed_response = owned._check_response(seed_response).copy()
        if (_sha(self.seed_response.tolist())!=SEED_RESPONSE_SHA
                or not np.array_equal(self.seed_response,np.asarray(final['actual_response']))
                or self.seed_response[owned.tau_index]!=1.
                or owned.nq!=1473 or owned.J!=48 or owned.old.nb!=61
                or owned.identity.target_sha256!=TARGET_SHA
                or len(owned.tail_degrees)!=4 or owned.compact.COMPACT_NB!=28):
            raise ValueError('the full actual1473 seed and original dictionaries must remain')
        self.owned = owned
        self.policy = json.loads(json.dumps(policy,sort_keys=True,separators=(',',':')))
        self.policy_sha = _sha(self.policy)
        self.source_sha = self.policy['source_sha256']
        self.old_free = owned.tau_index
        self.mean_count = 94
        self.nq = self.old_free+self.mean_count
        self.mean_start = self.old_free
        self.safe_point = safe_point
        self.counts = defaultdict(int)
        self.counts['complete_mean_models_constructed'] = 1
        self.chain = explicit.UnsolvedMeanChain(centered.chain,
                         self.policy['explicit_chain_policy'],self.check)
        self.seed_trace = owned.core_trace(self.seed_response)
        self.seed_mean_cache = {}
        self.seed_mean_height_cache = {}
        self.prepared_cache = {}
        self.current_source_receipt = {
            key:natural_terminal[key] for key in (
                'run_id','job_id','source_commit','raw_job_log_bytes','raw_job_log_sha256')}
        self.current_source_receipt.update(FINAL_JSON_bytes=len(literal.encode()),FINAL_JSON_sha256=SEED_FINAL_SHA)
        self.model_sha256 = _sha({'policy':self.policy,
            'same_target_sha256':owned.identity.target_sha256,
            'same_owned_model_sha256':owned.response_model_sha256,
            'same_seed_response_sha256':SEED_RESPONSE_SHA,
            'same_natural_terminal_sha256':SEED_FINAL_SHA})
        self.owned_provenance = owned.guard()

    def __getattr__(self,name):
        return getattr(self.owned,name)

    def check(self):
        self.owned.driver.check(self.owned.deadline)
        if self.safe_point is not None:
            self.safe_point()

    def guard(self):
        if (_sha(self.policy)!=self.policy_sha
                or hashlib.sha256(Path(__file__).read_bytes()).hexdigest()!=self.source_sha
                or self.owned.guard()!=self.owned_provenance):
            raise ValueError('the complete coupled model or owned reference changed')
        return {'schema':SCHEMA,'model_sha256':self.model_sha256,
                'same_target_sha256':self.identity.target_sha256,
                'fixed_seed_response_sha256':SEED_RESPONSE_SHA,
                'all_angular_free_columns':self.old_free,'all_mean_columns':self.mean_count,
                'all_free_columns':self.nq}

    def _check(self,response):
        self.check()
        q = np.asarray(response,dtype=float)
        if q.shape!=(self.nq,) or not np.all(np.isfinite(q)):
            raise ValueError('all1566 finite coupled coordinates required')
        return q

    def angular_response(self,response):
        response = self._check(response)
        return np.r_[response[:self.old_free],1.]

    def initial_response(self):
        centered.chain.public_only()
        return np.r_[self.seed_response[:self.old_free],np.zeros(self.mean_count)]

    def _mean_dictionary(self,data):
        nr = len(data['r'])
        first = self.owned.old.nm-1
        bulk = np.asarray(data['new_columns'][:,first:first+self.owned.old.nb,:])
        if bulk.shape!=(nr,61,3):
            raise ValueError('all61 original true bulk radial functions required')
        d1 = (self.owned.old.core_k*(self.par.alpha+2)/self.owned.old.bulk_scale
              *np.asarray(self.owned.old.core_B))
        homogeneous_bulk = bulk-data['core_radial'][:,None,:]*d1[None,:,None]
        compact = data['compact_radial_dictionary']
        tail = data['analytic_tail_columns']
        left,right = self.policy['mean_plateau_left'],self.policy['mean_plateau_right']
        c,cr,crr = self.base.step2((data['r']-left)/(right-left))
        plateau = np.stack([c,cr/(right-left),crr/(right-left)**2],axis=1)[:,None,:]
        answer = np.concatenate([homogeneous_bulk,compact,tail,plateau],axis=1)
        if answer.shape!=(nr,94,3) or not np.all(np.isfinite(answer)):
            raise ArithmeticError('complete94-column mean dictionary is not finite')
        self.counts['complete_mean_dictionary_threejet_values'] += answer.size
        return answer

    def prepare(self,r,ntheta):
        self.guard()
        centered.chain.public_only()
        r = np.asarray(r,dtype=float)
        key = (r.tobytes(),int(ntheta))
        if key in self.prepared_cache:
            return self.prepared_cache[key]
        # Owned prepare enforces every original work/fine radial point.
        data = dict(self.owned.prepare(r,ntheta))
        data['mean_dictionary'] = self._mean_dictionary(data)
        data['joint_model_sha256'] = self.model_sha256
        data['joint_grid_role'] = 'fine' if int(ntheta)>=512 else 'work'
        self.prepared_cache[key] = data
        return data

    def _identity(self,response,data):
        if data.get('joint_model_sha256')!=self.model_sha256:
            raise ValueError('same new source-bound prepared data required')
        return {'joint_model_sha256':self.model_sha256,
                'same_frozen_target_sha256':self.identity.target_sha256,
                'response_sha256':_sha(np.asarray(response).tolist()),
                'radial_grid_sha256':height._array_sha(data['r']),
                'theta_grid_sha256':height._array_sha(data['theta'])}

    def _require(self,response,data,state):
        expected = self._identity(response,data)
        if (not np.array_equal(response,state.get('response'))
                or any(state.get(key)!=value for key,value in expected.items())):
            raise ValueError('same full response, frozen E and complete grids required')
        return expected

    def _seed_means(self,data):
        mean_data = data['fixed_mean_data']
        missing = [i for i,r in enumerate(data['r']) if float(r) not in self.seed_mean_cache]
        if missing:
            seed_jets = self.owned.height_jets(self.seed_response,mean_data,self.seed_trace)
            for i in missing:
                self.check()
                target = self.owned._target(mean_data,i)
                self.counts['fixed_seed_mean_queries_attempted'] += 1
                value = self.owned._mean_state(target,
                            {key:values[i] for key,values in seed_jets.items()})
                # Only the actual seed scalar and its same target are needed
                # by later trials. Retain that paid information, not512
                # duplicate seed angular arrays at every stencil query.
                retained = {key:value[key] for key in
                    ('target','x_decimal','chart','s','s_r','s_r_decimal','root_receipt')}
                self.seed_mean_cache[float(data['r'][i])] = retained
                self.counts['fixed_seed_mean_queries_completed'] += 1
        return [self.seed_mean_cache[float(r)] for r in data['r']]

    def mean_change(self,response,data,trace):
        response = self._check(response)
        if np.array_equal(trace['pc'],self.seed_trace['pc']):
            dzeta,dzeta1 = 0.,0.
        else:
            # Same numerical core map/derivative as every retained old
            # angular column. The exact continuous formula is R643(22).
            dzeta = trace['zeta']-self.seed_trace['zeta']
            dzeta1 = trace['zeta_r']-self.seed_trace['zeta_r']
        result = (data['new_core_lift']*dzeta+data['core_radial']*dzeta1
                  +self.amplitude*np.einsum('rbk,b->rk',data['mean_dictionary'],
                                            response[self.mean_start:]))
        if not np.all(np.isfinite(result)):
            raise ArithmeticError('actual mean height change has nonfinite jets')
        return result

    def evaluate(self,response,data):
        self.guard()
        response = self._check(response)
        identity = self._identity(response,data)
        self.counts['complete_joint_evaluations_attempted'] += 1
        z = self.angular_response(response)
        trace = self.owned.core_trace(z)
        change = self.mean_change(response,data,trace)
        means = self._seed_means(data)
        mean_jets = self.owned.height_jets(z,data['fixed_mean_data'],trace)
        output_jets = self.owned.height_jets(z,data,trace)
        ms,os,positions = [],[],[]
        for i,r in enumerate(data['r']):
            self.check()
            target = means[i]['target']
            mean_state = self.chain.explicit_state(target,
                {key:value[i] for key,value in mean_jets.items()},means[i],change[i])
            output_state = self.chain.explicit_state(target,
                {key:value[i] for key,value in output_jets.items()},means[i],change[i])
            position = self.chain.position(output_state,mean_state,data['theta'],data['primitive'])
            ms.append(mean_state);os.append(output_state);positions.append(position)
        S = np.stack([p['S'] for p in positions])
        F,G = np.asarray([s['F'] for s in ms]),np.asarray([s['G'] for s in ms])
        co,si = data['complete_position_projection']
        ps = np.stack([S[:,:,0]@co.T,S[:,:,1]@si.T],axis=1).reshape(len(F),-1)
        rows = np.concatenate([ps,F[:,None],(data['r']*G)[:,None]],axis=1)
        residual = (rows*data['position_radial_units'][:,None]/self.amplitude).ravel()
        if not np.all(np.isfinite(residual)):
            raise ArithmeticError('complete coupled residual is not finite')
        self.counts['complete_joint_evaluations_completed'] += 1
        self.counts['complete_joint_rows_evaluated'] += len(residual)
        return dict(identity,response=response.copy(),angular_response=z,core=trace,
            mean_change=change,mean_seed_states=means,mean_jets=mean_jets,height_jets=output_jets,
            mean_states=ms,output_states=os,positions=positions,S=S,F=F,G=G,residual=residual,
            conditional_eta_identity_observation=float(max(np.max(p['eta']) for p in positions)),
            all_original_position_rows_retained=True,all_canonical_F_and_rG_rows_retained=True,
            trial_mean_roots=False,continuous_metric_or_README_certified=False)

    def mean_direction(self,trace,indices,data):
        nr,nc = len(data['r']),len(indices)
        answer = np.zeros((nr,3,nc))
        mask = indices < self.old_free
        if np.any(mask):
            selected = indices[mask]
            core = self.owned.core_direction(trace,selected)
            answer[:,:,mask] = (data['new_core_lift'][:,:,None]*core['zeta'][None,None,:]
                              +data['core_radial'][:,:,None]*core['zeta_r'][None,None,:])
        if np.any(~mask):
            mean_indices = indices[~mask]-self.mean_start
            answer[:,:,~mask] = self.amplitude*np.transpose(
                data['mean_dictionary'][:,mean_indices,:],(0,2,1))
        return answer

    def angular_direction(self,trace,indices,data):
        nr,nt,nc = len(data['r']),len(data['theta']),len(indices)
        answer = {key:np.zeros((nr,nt,nc)) for key in height.JET_KEYS}
        mask = indices < self.old_free
        if np.any(mask):
            directions,_ = self.owned.height_direction(trace,indices[mask],data)
            for key,value in directions.items():
                answer[key][:,:,mask] = value
        return answer

    def _jacobian_rows(self,response,data,state,block_columns):
        nr = len(data['r'])
        co,si = data['complete_position_projection']
        nm = len(data['all_position_odd_modes'])
        rows_per_r = 2*nm+2
        J = np.empty((nr*rows_per_r,self.nq))
        for first in range(0,self.nq,block_columns):
            self.check()
            indices = np.arange(first,min(self.nq,first+block_columns))
            dmean = self.mean_direction(state['core'],indices,data)
            Hm = self.angular_direction(state['core'],indices,data['fixed_mean_data'])
            Ho = self.angular_direction(state['core'],indices,data)
            values = np.empty((nr,rows_per_r,len(indices)))
            for i in range(nr):
                self.check()
                dm = self.chain.direction(state['mean_states'][i],
                       {key:value[i] for key,value in Hm.items()},dmean[i,1],dmean[i,2],
                       canonical_mean=True)
                do = self.chain.direction(state['output_states'][i],
                       {key:value[i] for key,value in Ho.items()},dmean[i,1],dmean[i,2])
                ds = self.chain.position_direction(state['output_states'][i],
                                                   state['positions'][i],do,dm)
                values[i,:nm] = co@ds[:,0,:]
                values[i,nm:2*nm] = si@ds[:,1,:]
                values[i,2*nm] = dm['F']
                values[i,2*nm+1] = data['r'][i]*dm['G']
            J[:,indices] = (values*data['position_radial_units'][:,None,None]
                             /self.amplitude).reshape(-1,len(indices))
            self.counts['full_joint_J_columns_at_radial_points'] += nr*len(indices)
        if not np.all(np.isfinite(J)):
            raise ArithmeticError('complete1566-column coupled Jacobian is not finite')
        self.counts['full_joint_J_entries_evaluated'] += J.size
        return J

    def jacobian(self,response,data,state,block_columns=16):
        self.guard()
        response = self._check(response)
        self._require(response,data,state)
        self.counts['complete_joint_J_attempts'] += 1
        answer = self._jacobian_rows(response,data,state,int(block_columns))
        self.counts['complete_joint_J_completed'] += 1
        return answer

    @staticmethod
    def _slice_data(data,first,last,nr):
        answer = {}
        for key,value in data.items():
            if key=='fixed_mean_data':
                answer[key] = CompleteMeanHeight._slice_data(value,first,last,nr)
            elif isinstance(value,np.ndarray) and value.ndim and value.shape[0]==nr:
                answer[key] = value[first:last]
            else:
                answer[key] = value
        return answer

    def jacobian_row_blocks(self,response,data,state,radial_block=48,block_columns=16):
        """A genuine complete row pass, suitable for the existing full QR.

        Repeating this iterator is a second paid full analytic J pass.
        No rows, frequencies or columns are screened by residual magnitude.
        """
        self.guard()
        response = self._check(response)
        self._require(response,data,state)
        nr = len(data['r'])
        self.counts['complete_joint_J_row_passes_attempted'] += 1
        for first in range(0,nr,int(radial_block)):
            last = min(nr,first+int(radial_block))
            sub = self._slice_data(data,first,last,nr)
            small = dict(state)
            for name in ('mean_states','output_states','positions'):
                small[name] = state[name][first:last]
            yield first,last,self._jacobian_rows(response,sub,small,int(block_columns))
        self.counts['complete_joint_J_row_passes_completed'] += 1

    def combined_direction(self,response,direction,data,state):
        """One exact full direction without retaining an nr*N*1566 array."""
        self._require(response,data,state)
        direction = np.asarray(direction,dtype=float)
        if direction.shape!=(self.nq,) or not np.all(np.isfinite(direction)):
            raise ValueError('one complete finite coupled direction required')
        full = np.r_[direction[:self.old_free],0.]
        core = self.owned.core_direction(state['core'],np.arange(self.owned.nq))
        cc = core['correction_delta']@full
        def angular(view):
            values = self.owned.old.delta_jets(
                np.r_[0.,full[:self.owned.old_count]],self.amplitude,view)
            answer = dict(zip(height.JET_KEYS,values))
            correction = height._separable(view['core_radial'],cc,self.core_modes,view['theta'])
            for key in answer:
                answer[key] += correction[key]
            for start,count,modes,radial in (
                (self.compact_start,self.compact_count,self.extra_compact_modes,view['compact_radial_dictionary']),
                (self.tail_start,self.tail_count,self.modes,view['analytic_tail_columns'])):
                if count:
                    coeff = self.amplitude*full[start:start+count].reshape(len(modes),radial.shape[1])
                    fields = np.einsum('rbk,jb->rjk',radial,coeff)
                    co,si = np.cos(modes[:,None]*view['theta']),np.sin(modes[:,None]*view['theta'])
                    pieces = (fields[:,:,0]@co,fields[:,:,1]@co,fields[:,:,2]@co,
                        -(fields[:,:,0]*modes)@si,-(fields[:,:,0]*modes*modes)@co,
                        -(fields[:,:,1]*modes)@si)
                    for key,value in zip(height.JET_KEYS,pieces):
                        answer[key] += value
            lift = height._separable(view['new_core_lift'],
                    self.amplitude*full[self.core_start:self.tau_index],
                    self.core_free_modes,view['theta'])
            for key in answer:
                answer[key] += lift[key]
            return answer
        mean_delta = (data['new_core_lift']*(core['zeta']@full)
                      +data['core_radial']*(core['zeta_r']@full)
                      +self.amplitude*np.einsum('rbk,b->rk',data['mean_dictionary'],
                                                direction[self.mean_start:]))
        self.counts['combined_actual_angular_and_mean_directions'] += 1
        return {'canonical_jets':angular(data['fixed_mean_data']),
                'output_jets':angular(data),'mean_jets':mean_delta}

    def coefficient_fields(self,response,data,state=None):
        if state is not None:
            self._require(response,data,state)
        angular = self.angular_response(response)
        result = self.owned.coefficient_fields(angular,data)
        result['actual_explicit_mean_change_threejets'] = self.mean_change(
            response,data,self.owned.core_trace(angular))
        result['same_fixed_seed_mean_response_sha256'] = SEED_RESPONSE_SHA
        result['mean_function_is_fixed_seed_plus_actual94_column_and_hard_trace_change'] = True
        result['mean_seed_continuous_evaluation_errors_enclosed'] = False
        return result

    def cumulative_cost_receipt(self):
        self.guard()
        return {
            'same_completed_seed_origin':self.current_source_receipt,
            'same_frozen_target_sha256':self.identity.target_sha256,
            'complete_coupled_model_provenance':self.guard(),
            'new_complete_mean_model_counts':dict(self.counts),
            'new_explicit_mean_chain_counts':dict(self.chain.counts),
            'fixed_seed_and_reference_reconstruction_full_actual_costs':self.owned.cumulative_cost_receipt(),
            'inherited_terminal_costs_retained_by_scope_input_not_added_again':True,
            'trial_mean_roots_replayed':False,
            'counters_are_overlapping_and_not_disjoint_costs':True,
        }
