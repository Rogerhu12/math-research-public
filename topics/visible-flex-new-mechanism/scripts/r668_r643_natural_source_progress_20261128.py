"""Bounded R668 progress inside a genuine R643 successor with its paid source and tail receipt."""
import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path

import r668_paid_source_windows_20261128 as win
import r668_resumable_dense_column_20261128 as dense

proof=win.proof
germ=proof.old.germ
SCHEMA='R668-paid-R643-source-progress-v1'
FIELD='R668_same_source_progress'
ROWS=('finite_M_to_true_infinite_germs','paid_finite_Cauchy_roundoff',
      'dense_ODE_and_connector_core_normalizations','original_envelope_normalizations',
      'original_forced_tail_multiplier_and_scale','literal_coefficient_realization',
      'same_reference_E_and_mean_branch_numerical_evaluation')
ORDER=(2,4,'forced_j4_C',6,8,10,12,14,16,18,20,22)
BOUND_FILES=((proof,'572c73b76ad30eb3a1751076d81b9cebf4b0ce994e91a78cf155ab81fac1d165'),
             (win,'d9de81f40d4f83c72abbbd1c495d9087c64f1d990c5e99620314dd1615f7a228'),(dense,'57f2cbb1e0c604f46763c3c47f57e07024933d28707e0206e968f90fdc0a1460'))
for module,sha in BOUND_FILES:
    if hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()!=sha:
        raise ValueError('different published source proof')
SOURCE=germ.sha(Path(__file__).read_bytes())


def inherited(literal_final,expected_sha):
    """The normal successor's own hash-bound input supplies both arguments."""
    if germ.sha(literal_final.encode())!=expected_sha:
        raise ValueError('previous natural terminal source packet identity differs')
    final=json.loads(literal_final)
    p=final.get(FIELD)
    if p is not None and (p['schema']!=SCHEMA or p['proof_source_sha256']!=SOURCE
            or p['target']!=germ.TARGET or p['model']!=germ.MODEL or p['contract']!=germ.CONTRACT
            or p['fixed_seed']!=germ.SEED or p['seven_original_rows']!=final['current_accepted_tail_receipt']['old_source_error_accounting']):
        raise ValueError('source packet belongs to a different material, field, model or proof')
    return p


def weighted_component(run,complete):
    passed=[j for j in germ.MODES if complete.get(str(j),{}).get('meets_half_denominator_threshold')]
    actual=run.response
    seed=run.tail.joint.seed_response
    reference=run.tail.model.q_reference
    def magnitude(v):
        return max(abs(Fraction(str(float(v)))),abs(Fraction.from_float(float(v))))
    amp=max(Fraction(1,100000),magnitude(run.tail.model.amplitude))
    def moments(vector,first):
        return [win.qtext(sum((amp*magnitude(vector[i+first])*j**a
                    for i,j in enumerate(range(4,23,2)) if j in passed),Fraction(0))) for a in range(4)]
    return {'ordinary_post_modes_with_proved_normalized_M25_difference':passed,
            'remaining_ordinary_modes':[j for j in germ.MODES if j not in passed],
            'exponential_factor_for_covered_addends':'exp(-2000)',
            'exact_coefficient_multipliers_by_angular_order_0_1_2_3':{
                'accepted_post':moments(actual,0),'fixed_seed_post':moments(seed,0),
                'reference_post':moments(reference,1)},
            'domains':['108<=u<=alpha26: normalized difference radial orders 0..3 divided by W',
                       'u>=alpha26: omitted true tail radial orders 0..3 divided by W',
                       'mouth<=r<=R: normalized difference radial orders 0..2'],
            'pre_tanh_and_forced_and_uncovered_addends_are_separate':True}


class NaturalProgress:
    def __init__(self,run,previous=None):
        self.tail=run.tail
        self.qid=None
        self.certificate={}
        self.root_snapshot=None
        self.last_root_snapshot=-float('inf')
        self.started=time.monotonic()
        self.spent=0.
        self.generator=self.stream=None
        self.kind=self.which=None
        self.prior=previous
        self.balls={} if previous is None else dict(previous['peak_balls'])
        self.windows={} if previous is None else dict(previous['partial_seed_windows'])
        self.columns={} if previous is None else dict(previous['completed_denominators'])
        self.active={} if previous is None else dict(previous['partial_native_columns'])
        self.flat={} if previous is None else dict(previous['proved_j4_flat_at_mouth'])
        self.issues={} if previous is None else dict(previous['uncertified_columns_or_windows'])
        self.cumulative_seconds=0. if previous is None else previous['cumulative_proof_seconds']
        self.static=None if previous is None else previous['static_literal_and_envelope_parts']
        self.refresh(run)
        models=self.tail.model.old.modes
        self.owners={str(int(m.mode)):m for m in models}
        self.owners['forced_j4_C']=self.tail.model.old.old.forced
        if self.static is None:
            values=win.literals(self.tail,run.response)
            self.current_literal=values.pop('current_1566q_canonical_display')
            self.static={'literals':values,'envelope':win.envelope_geometry(self.tail)}

    def refresh(self,run):
        paid=run.accepted_tail
        if self.tail is not run.tail or paid['actual_response_sha256']!=germ.sha(germ.canonical(run.response.tolist())):
            raise ValueError('current accepted response and existing tail receipt must agree')
        if self.qid==paid['actual_response_sha256']:
            return
        req=proof.old.live_thresholds(self.tail,run.response,paid)
        c=req['original_component']
        if set(c['seven_original_source_rows'])!=set(ROWS):
            raise ValueError('the source ledger must contain the seven exact original rows')
        self.certificate=c
        self.requirements=req
        self.qid=c['actual_response_sha256']
        self.current_literal=win.literal_vector(germ.canonical(run.response.tolist()).decode(),run.response)
        self.weighted=weighted_component(run,self.columns)
        for key,row in self.columns.items():
            reqrow=req['additional_forced_boundary_observation'] if key=='forced_j4_C' else req['same_actual_mode_precision_requirements'][key]
            val=float.fromhex(row['signed_observation_hex'])
            if ((val.hex()!=reqrow['actual_forced_j4_homogeneous_core_C_hex']) if key=='forced_j4_C'
                    else (abs(val).hex()!=reqrow['observed_abs_core_A_hex'])):
                raise ValueError('carried denominator differs from actual source observation')

    def ball_key(self,key):
        owner=self.owners[key]
        j=4 if key=='forced_j4_C' else int(key)
        data=owner.flat.finite_inner_data
        return '|'.join([str(j),float(owner.flat.alpha).hex(),float(data['z_alpha_first']).hex()])

    def choose(self):
        for name in ORDER:
            key=str(name)
            bkey=self.ball_key(key)
            if bkey not in self.balls and bkey not in self.issues:
                j=4 if name=='forced_j4_C' else name
                self.kind,self.which='initial',bkey
                self.generator=win.initial_ball(self.owners[key].flat,j,self.windows.setdefault(bkey,{}))
                return True
        for name in ORDER:
            key=str(name)
            bkey=self.ball_key(key)
            if bkey not in self.balls or key in self.columns or key in self.issues:
                continue
            self.kind,self.which='dense',key
            j=4 if name=='forced_j4_C' else name
            self.stream=dense.DenseStream(self.owners[key],j,name=='forced_j4_C',self.balls[bkey],.0002)
            initial=self.active.get(key)
            if initial is None and j==4:
                fkey=self.flat_key(key)
                initial=self.flat.get(fkey)
            self.generator=self.stream.work(initial)
            return True
        return False

    def flat_key(self,key):
        return self.ball_key(key)+'|'+float(self.owners[key].flat.display_log).hex()

    def store_active(self):
        if self.kind=='dense' and self.stream is not None:
            if self.stream.anchor is not None:
                self.active[self.which]=self.stream.packet()
            if self.stream.j==4 and self.stream.flat_at_mouth is not None:
                self.flat[self.flat_key(self.which)]=self.stream.flat_at_mouth

    def tick(self,run):
        self.refresh(run)
        now=time.monotonic()
        # The nonlinear solver keeps its entire final readout reserve. All state
        # is retained over slices and naturally serialized under the original FINAL.
        credit=8.+.03*(now-self.started)-self.spent
        stop=min(now+min(25.,max(0.,credit)),run.solver_deadline)
        if now>=stop:
            return
        started=time.monotonic()
        try:
            if started-self.last_root_snapshot>=120:
                self.root_snapshot=win.root_observations(self.tail)
                self.last_root_snapshot=started
            while time.monotonic()<stop:
                if self.generator is None and not self.choose():
                    break
                try:
                    next(self.generator)
                except StopIteration as end:
                    if self.kind=='initial':
                        self.balls[self.which]=end.value
                        self.windows.pop(self.which,None)
                    else:
                        self.store_active()
                        self.columns[self.which]=end.value
                        self.weighted=weighted_component(run,self.columns)
                        self.active.pop(self.which,None)
                    self.generator=self.stream=None
                    self.kind=self.which=None
                except (ArithmeticError,LookupError,ValueError) as exc:
                    self.store_active()
                    self.issues[self.which]={'kind':self.kind,'error':type(exc).__name__,'message':str(exc)}
                    self.generator=self.stream=None
                    self.kind=self.which=None
        finally:
            self.store_active()
            self.spent+=time.monotonic()-started

    def final(self,run):
        # A rules/clock checkpoint only serializes already-computed proof state.
        self.store_active()
        c=self.certificate
        raw=c['seven_original_source_rows']
        paidc={key:dict(status='unresolved',original=raw[key],components=[],missing=[])
               for key in ROWS}
        parts=[
            (['R658 exact unnormalized finite/infinite difference',self.weighted],
             ['nonlinear pre-tanh columns, whole forced response and remaining normalized addends']),
            (['peak_balls: exact finite z, actual paid z error and peak displacement',
              'the paid display is used as a common positive gauge in R658'],
             ['any missing peak ball and its propagation through each actual column']),
            (['completed_denominators and partial_native_columns: genuine cone, absolute rim error and continuous native-cell log suprema'],
             ['remaining dense traversal, normalized core pair/cutoff and full dense jet error, including physical chart bridges']),
            ([self.static['envelope']],['tight four scale upper/error and cutoff/jet uncertainties at all original normalization nodes']),
            ([self.static['literals']['original_frozen_force_scale'],'forced_j4_C if its own rim proof completed'],
             ['j2 forcing jets, nonzero forced particular column, boundary quotient and return-core dependence']),
            (['static literal vector errors; current_1566q_canonical_display'],
             ['knot movement, operator arithmetic and all basis/jet amplification in the continuous field']),
            ([self.root_snapshot],['continuous angular errors, uniform signed derivative gap, source input and radial interpolation, root derivative and integral propagation'])]
        for key,(covered,missing) in zip(ROWS,parts):
            paidc[key].update(components=covered,missing=missing)
        return {'schema':SCHEMA,'proof_source_sha256':SOURCE,'target':c['same_target_sha256'],
                'model':c['joint_model_sha256'],'contract':c['source_contract_sha256'],'fixed_seed':germ.SEED,
                'accepted_response':self.qid,'accepted_tail':c['consumed_R643_tail_receipt_sha256'],
                'solver_accepted_q_at_FINAL':run.accepted_tail['actual_response_sha256'],
                'response_specific_parts_are_for_last_paid_safe_point':True,
                'seven_original_rows':raw,'seven_row_progress':paidc,
                'peak_balls':self.balls,'partial_seed_windows':self.windows,
                'completed_denominators':self.columns,'partial_native_columns':self.active,
                'proved_j4_flat_at_mouth':self.flat,'uncertified_columns_or_windows':self.issues,
                'static_literal_and_envelope_parts':self.static,'current_1566q_canonical_display':self.current_literal,
                'cumulative_proof_seconds':self.cumulative_seconds+self.spent,'proof_seconds_this_run':self.spent,
                'native_counts_contain_inherited_or_shared_prefixes_and_must_not_be_summed':True,
                'formal_global_metric_or_README_certified':False,'additional_ODE_root_FFT_J':0}


def at_paid_safe_point(run,previous=None):
    """Call after restore has an accepted q and matching receipt, then at natural solver safe points."""
    if (run.tail is None or run.accepted_tail is None or run.rules.failed or time.monotonic()>=run.solver_deadline
            or getattr(run,'r668_source_failure',None) is not None):
        return
    try:
        owner=getattr(run,'r668_source_progress',None)
        if owner is None:
            start=time.monotonic()
            owner=NaturalProgress(run,previous)
            owner.spent+=time.monotonic()-start
            run.r668_source_progress=owner
        owner.tick(run)
    except (ArithmeticError,LookupError,ValueError,TypeError,AttributeError) as exc:
        run.r668_source_failure={'type':type(exc).__name__,'message':str(exc),
                                 'prior_closed_and_partial_proofs_retained':True}


def attach_final(final,run,previous=None):
    owner=getattr(run,'r668_source_progress',None)
    if owner is not None:
        final[FIELD]=owner.final(run)
    elif previous is not None:
        final[FIELD]=previous
    if getattr(run,'r668_source_failure',None) is not None:
        final['R668_source_progress_failure']=run.r668_source_failure


def install_on_natural_successor(driver,previous_final_json,expected_previous_final_sha):
    """Install only in the new successor's already prepared driver, immediately before its main()."""
    previous=inherited(previous_final_json,expected_previous_final_sha)
    cls=driver.CoupledRun
    # The successor defines accepted_tail and its own extend_final; the original root/time
    # checks run first. Installing never starts a job or changes the PDE/trial/acceptance.
    original_check=cls.check
    original_extend=driver.extend_final
    if getattr(cls,'_r668_bound',False):
        raise ValueError('R668 already attached to this natural successor')
    def check(run,solver=False):
        original_check(run,solver=solver)
        if solver and getattr(run,'restored',False) and run.current is not None:
            at_paid_safe_point(run,previous)
    def finish(final,run):
        original_extend(final,run)
        attach_final(final,run,previous)
    cls.check=check
    driver.extend_final=finish
    cls._r668_bound=True
