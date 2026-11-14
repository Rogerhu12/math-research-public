#!/usr/bin/env python3
"""Keep published height constraints while replaying their numerical arrays.

The public input bytes and complete mathematical state are checked by the
driver. Here only a clearly recorded binary64 evaluation replay tolerance is
allowed. Published A, b, cap intercept and their original definition hash are
retained exactly. Fresh X/Xs/T belong to a separately identified objective
evaluation. This is not a quadrature or continuous-error certificate.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import traceback

import numpy as np

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_height_polytope import HeightPolytope
from frame_height_polytope_audit import proposal_polytope


REPLAY_EPS_MULTIPLIER=64


def bitwise_equal(a,b):
    a=np.asarray(a,dtype=np.float64);b=np.asarray(b,dtype=np.float64)
    return a.shape==b.shape and np.array_equal(a.view(np.uint64),b.view(np.uint64))


def evaluated_scalar(record):
    value=float(record['binary64'])
    if not np.isfinite(value) or str(Q.from_float(value))!=record['exact_binary64_rational']:
        raise ValueError('inconsistent published exact binary64 scalar')
    return value


def array_sha(value):
    return hashlib.sha256(np.ascontiguousarray(value,dtype=np.float64).tobytes()).hexdigest()


class PublishedHeightRows(HeightPolytope):
    """Original numerical constraints, with explicit fresh evaluation data.

    numerical_definition/sha256 are the original published constraint record,
    including the hash of the source X used when it was published. X/base are
    fresh evaluations of that same mathematical reference for the new quartic
    objective and its numerical diagnostics. They are *not* asserted to have
    that old input_X hash; replay_evaluation_definition binds them separately.
    """
    def __init__(self,fresh,published_record,replay):
        self.__dict__=fresh.__dict__.copy()
        definition=copy.deepcopy(published_record['definition'])
        self.A=np.array(definition['row_A_evaluated'],dtype=float,copy=True)
        self.b=np.array(definition['row_b_evaluated'],dtype=float,copy=True)
        self.cap_intercept=evaluated_scalar(definition['cap_intercept_evaluated'])
        self.cap_target=evaluated_scalar(definition['cap_target_evaluated'])
        self.cap_row=np.array([evaluated_scalar(x) for x in definition['cap_row_evaluated']])
        nr=len(self.radial);self.row_lower=-self.b[:nr].copy();self.row_upper=self.b[nr:2*nr].copy()
        self.row_metadata=copy.deepcopy(definition['row_witnesses'])
        self.numerical_definition=definition;self.sha256=published_record['definition_sha256']
        self.replay_evaluation_definition=copy.deepcopy(replay)
        self.replay_evaluation_sha256=digest(replay)
        for value in [self.A,self.b,self.cap_row,self.row_lower,self.row_upper]:value.setflags(write=False)
        if (digest(self.numerical_definition)!=self.sha256 or
            not bitwise_equal(self.A,definition['row_A_evaluated']) or
            not bitwise_equal(self.b,definition['row_b_evaluated'])):
            raise ArithmeticError('published constraint arrays or hash changed during restoration')

    def record(self):
        out=super().record()
        out.update(published_constraint_definition_and_sha_preserved=True,
            objective_reference_arrays_are_bound_separately=True,
            replay_evaluation_definition=self.replay_evaluation_definition,
            replay_evaluation_sha256=self.replay_evaluation_sha256)
        return out


def retain_published_rows(fresh,published_record):
    """Check one same-model replay, then install the original row arrays."""
    if not isinstance(fresh,HeightPolytope):raise TypeError('a freshly evaluated HeightPolytope is required')
    old=published_record['definition'];new=fresh.numerical_definition
    if digest(old)!=published_record['definition_sha256']:
        raise ValueError('published numerical polytope digest mismatch')
    if set(old)!=set(new):raise ValueError('published numerical definition fields changed')
    # All provenance, exact coefficient/basis/grid identities, I bytes, bounds,
    # ball and signed-height targets remain literal equality checks. Only the
    # numerical X hash and explicitly compared floating reductions may differ.
    allowed={'input_X_sha256','row_b_evaluated','row_witnesses',
             'cap_intercept_evaluated','cap_target_evaluated'}
    strict_differences=[key for key in old if key not in allowed and old[key]!=new[key]]
    if strict_differences:
        raise ValueError('mathematical/source/grid/row-matrix replay mismatch: '+','.join(strict_differences))
    oldA=np.asarray(old['row_A_evaluated'],float);oldb=np.asarray(old['row_b_evaluated'],float)
    if (not bitwise_equal(oldA,fresh.A) or oldb.shape!=fresh.b.shape
            or not np.all(np.isfinite(oldb))):
        raise ValueError('published row matrix or finite boundary layout differs')
    if fresh.horizontal_failure!=published_record.get('horizontal_failure'):
        raise ValueError('the fixed horizontal-ball failure diagnosis changed')
    old_intercept=evaluated_scalar(old['cap_intercept_evaluated'])
    old_target=evaluated_scalar(old['cap_target_evaluated'])
    scale=max(1.,fresh.ball_radius,abs(old_intercept),abs(old_target),
        float(np.max(abs(fresh.base))),float(np.max(abs(fresh.G@fresh.current))),
        float(np.max(abs(oldb))),float(np.max(abs(fresh.b))))
    tolerance=REPLAY_EPS_MULTIPLIER*np.finfo(float).eps*scale
    b_difference=float(np.max(abs(oldb-fresh.b)))
    scalar_differences={'cap_intercept':abs(old_intercept-fresh.cap_intercept),
                        'cap_target':abs(old_target-fresh.cap_target)}
    if b_difference>tolerance or max(scalar_differences.values())>tolerance:
        raise ValueError('published-row replay exceeds the explicit floating tolerance: '+
            json.dumps({'b_max_difference':b_difference,'scalar_differences':scalar_differences,
                        'replay_tolerance':tolerance,'scale':scale}))
    nr,nt=fresh.X.shape[:2];witnesses=old['row_witnesses']
    if len(witnesses)!=2*nr+1:raise ValueError('published row witnesses have a different layout')
    half=np.sqrt(np.maximum(fresh.ball_radius**2-fresh.horizontal_squared,0.))
    worst_witness_difference=0.;changed_witness_locations=0
    for k,witness in enumerate(witnesses[:-1]):
        i=k if k<nr else k-nr
        if set(witness)!={'kind','radial_index','angular_index','t','theta','compressed_bound'}:
            raise ValueError('unexpected published witness metadata')
        j=int(witness['angular_index'])
        if (witness['radial_index']!=i or not 0<=j<nt or
                witness['t']!=float(fresh.radial[i]) or witness['theta']!=float(fresh.theta[j])):
            raise ValueError('published compression witness uses different coordinates')
        expected=-oldb[k] if k<nr else oldb[k]
        if float(witness['compressed_bound'])!=expected:
            raise ValueError('published witness bound is inconsistent with its unchanged row')
        if k<nr and witness['kind']=='signed_height_lower':value=fresh.zmin-fresh.base[i,j]
        elif k<nr and witness['kind']=='ball_lower':value=-half[i,j]-fresh.base[i,j]
        elif k>=nr and witness['kind']=='ball_upper':value=half[i,j]-fresh.base[i,j]
        else:raise ValueError('published witness kind is inconsistent with its row')
        difference=abs(float(value)-expected)
        worst_witness_difference=max(worst_witness_difference,difference)
        if difference>tolerance:
            raise ValueError('the original compression witness no longer reproduces its row within replay tolerance')
        nw=fresh.row_metadata[k]
        changed_witness_locations+=int(witness['kind']!=nw['kind'] or j!=nw['angular_index'])
    if witnesses[-1]!={'kind':'common_cap_height_lower','target':old_target}:
        raise ValueError('published cap-row witness changed')
    replay={'schema':'published-height-rows-fresh-array-replay-v1',
        'published_numerical_definition_sha256':published_record['definition_sha256'],
        'fresh_numerical_definition_sha256':fresh.sha256,
        'published_input_X_sha256':old['input_X_sha256'],'fresh_input_X_sha256':new['input_X_sha256'],
        'common_input_I_sha256':new['input_I_sha256'],
        'fresh_reference_X_sha256':array_sha(fresh.X),
        'fresh_reference_base_sha256':array_sha(fresh.base),
        'same_mathematical_provenance_coefficients_grid_I_bounds_and_row_A':True,
        'published_A_b_cap_intercept_target_and_definition_hash_retained_bitwise':True,
        'fresh_X_bytes_equal_to_the_published_source_hash':old['input_X_sha256']==new['input_X_sha256'],
        'fresh_X_bitwise_equality_is_not_required_after_same_model_validation':True,
        'floating_row_b_max_difference':b_difference,
        'floating_cap_scalar_differences':scalar_differences,
        'original_witness_bound_max_difference':worst_witness_difference,
        'fresh_argmax_or_kind_changes_within_original_witness_tolerance':changed_witness_locations,
        'replay_tolerance_definition':'64*binary64_epsilon*max(1,R,abs(cap intercept),abs(cap target),max(abs(base)),max(abs(G@c)),max(abs(old b)),max(abs(fresh b)))',
        'binary64_epsilon':float(np.finfo(float).eps),'scale_evaluated':scale,
        'replay_tolerance_evaluated':float(tolerance),
        'tolerance_is_only_for_floating_replay_not_for_optimization_feasibility':True,
        'not_a_proven_roundoff_quadrature_or_continuous_error_bound':True,
        'particular_CPU_kernel_or_reduction_cause_not_asserted':True,
        'current_objective_arrays_are_separate_from_published_constraint_identity':True}
    return PublishedHeightRows(fresh,published_record,replay)


def restore_published_polytope(problem,reference,data,prior):
    record=prior['height_stage']['polytope'];definition=record['definition']
    if [str(Q.from_float(float(x))) for x in reference[problem.slices['height']]]!=definition['reference_current_coefficients']:
        raise ValueError('published polytope reference height coefficients differ')
    # Reconstruct the entire mathematical provenance from the real problem;
    # do not just copy the old provenance into an unchecked new polytope.
    override=definition['provenance'].get('artificial_constraint_override')
    artificial=bool(prior.get('artificial_inputs_only'))
    if override is not None and not artificial:raise ValueError('research constraints cannot use an artificial override')
    fresh,_=proposal_polytope(problem,reference,data,prior['configuration'],
        artificial=artificial,artificial_override=override)
    return retain_published_rows(fresh,record)


def developer_check():
    radial=np.array([0.,.4,1.]);theta=np.arange(4)*np.pi/2
    X=np.zeros((3,4,3));X[...,0]=np.array([.2,.1,-.1,-.2]);X[...,1]=.1
    X[...,2]=np.array([.3,.4,.5])[:,None]
    I=np.array([[0.,0.],[.12,.03],[.2,.15]]);c=np.array([.1,-.2])
    kwargs=dict(side=1,cap_intercept=.6,cap_row=I[-1],cap_target=.3,
        coefficient_lower=[-1.,-1.],coefficient_upper=[1.,1.],ball_radius=2.,
        minimum_signed_height=0.,radial=radial,theta=theta,
        provenance={'artificial_array_fixture_only':True,'frozen_physical_model':'same exact toy'})
    old=HeightPolytope(X,I,c,**kwargs);record=old.record()
    changed=X.copy();changed[...,2]=np.nextafter(changed[...,2],np.inf)
    fresh=HeightPolytope(changed,I,c,**{**kwargs,'cap_intercept':np.nextafter(.6,np.inf)})
    restored=retain_published_rows(fresh,record)
    rejection={}
    bad=copy.deepcopy(record);bad['definition']['row_b_evaluated'][1]+=1e-6
    bad['definition']['row_witnesses'][1]['compressed_bound']=-bad['definition']['row_b_evaluated'][1]
    bad['definition_sha256']=digest(bad['definition'])
    calls={'non_roundoff_row_change':lambda:retain_published_rows(fresh,bad),
        'changed_sample_node':lambda:retain_published_rows(HeightPolytope(changed,I,c,
            **{**kwargs,'radial':np.nextafter(radial,np.inf)}),record),
        'changed_reference_coefficient':lambda:retain_published_rows(HeightPolytope(changed,I,c+[0.,1e-6],**kwargs),record),
        'changed_mathematical_provenance':lambda:retain_published_rows(HeightPolytope(changed,I,c,
            **{**kwargs,'provenance':{'different_model':True}}),record)}
    for name,call in calls.items():
        try:call();rejection[name]=False
        except ValueError:rejection[name]=True
    from frame_height_quartic import FixedTangentHeightQuartic
    U=np.zeros_like(X);U[...,2]=1.;T=np.zeros_like(X);T[...,1]=1.
    objective=FixedTangentHeightQuartic({'X':changed,'Xs':U,'T':T,'radial':radial,'theta':theta},I,restored)
    objective_uses_fresh=(objective.definition['frozen_arrays']['X']['sha256']==array_sha(changed))
    kept=(bitwise_equal(restored.A,old.A) and bitwise_equal(restored.b,old.b)
        and restored.cap_intercept.hex()==old.cap_intercept.hex() and restored.sha256==old.sha256
        and restored.numerical_definition==old.numerical_definition)
    return {'schema':'published-height-row-roundoff-replay-artificial-check-v1',
        'passed':bool(kept and objective_uses_fresh and all(rejection.values())),
        'artificial_array_inputs_only':True,'research_geometry_evaluated':False,'optimizer_calls':0,
        'one_ulp_replay_accepted_without_changing_original_constraints':kept,
        'objective_X_uses_the_explicit_fresh_evaluation':objective_uses_fresh,
        'published_constraint_sha256':restored.sha256,
        'fresh_array_replay_sha256':restored.replay_evaluation_sha256,
        'replay':restored.replay_evaluation_definition,'rejected_inputs':rejection}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check-only',action='store_true',required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    try:answer=developer_check()
    except Exception as exc:
        answer={'schema':'published-height-row-roundoff-replay-artificial-check-v1','passed':False,
            'artificial_array_inputs_only':True,'research_geometry_evaluated':False,'optimizer_calls':0,
            'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()}
    answer['source_files_sha256']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in [Path(__file__).name,'frame_height_polytope.py','frame_height_polytope_audit.py','frame_height_quartic.py']}
    atomic_save(args.out,answer);print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
    if not answer['passed']:raise SystemExit(1)


if __name__=='__main__':main()
