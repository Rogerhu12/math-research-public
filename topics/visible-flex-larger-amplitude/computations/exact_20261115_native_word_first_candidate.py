#!/usr/bin/env python3
"""Select the one-word proposal on the complete saved and fresh native models.

Only Actions executes this child. It never calls the native map, RHS, J,
ODE, QR or a nonlinear trial. It binds the full ten-array fresh snapshot,
then checks all129248 affine rows for the separate sparse proposal. Actual
acceptance remains the original parent's ten no-J trials and original norm.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib,json,os
from pathlib import Path
import struct,time,traceback

HERE=Path(__file__).resolve().parent
PARENT_NAME='exact_20261115_native_word_first_parent.py'
PARENT_SHA='8cd7027df2f7039302dbdc1ed15068c6cf48d6645bc236d74e6e5b1e7dd387e8'
SYSTEM_NAME='exact_20261115_native_word_first_current576_system.py'
SYSTEM_SHA='2c6c012d9f2306f2ac13d240510eb8086b74d2b60ff318aa9e359dd72c05a3a8'
SCHEMA='native-word-first-complete-current576-proposal-v1'

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for block in iter(lambda:f.read(1<<20),b''):h.update(block)
 return h.hexdigest()
def load(name,digest):
 p=HERE/name
 if sha(p)!=digest:raise ValueError('Pinned first-word source changed: '+name)
 m=importlib.import_module(p.stem)
 if Path(m.__file__).resolve()!=p:raise ValueError('Pinned first-word source import path')
 return m

def main():
 if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public':
  raise RuntimeError('Candidate arithmetic belongs only to public repository Actions')
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--snapshot-directory',type=Path,required=True)
 p.add_argument('--snapshot-result-sha256',required=True)
 p.add_argument('--parent-binding',type=Path,required=True)
 p.add_argument('--parent-binding-sha256',required=True)
 p.add_argument('--out',type=Path,required=True)
 a=p.parse_args();out=a.out.resolve()
 if out.exists() or out.is_relative_to(a.snapshot_directory.resolve()) or a.snapshot_directory.resolve().is_relative_to(out):
  raise ValueError('Independent new word-candidate output directory required')
 out.mkdir(parents=True);(out/'large-arrays').mkdir()
 P=load(PARENT_NAME,PARENT_SHA);S=load(SYSTEM_NAME,SYSTEM_SHA);started=time.monotonic()
 report=dict(schema=SCHEMA,source_sha256=sha(__file__),system_source_sha256=SYSTEM_SHA,parent_source_sha256=PARENT_SHA,
  completed=False,selected_for_original_trials=False,native_accepted=False,task_completed=False,
  no_new_RHS_J_ODE_QR_or_nonlinear_trial_in_this_child=True,
  candidate_only_not_a_Newton_solution_or_final_equation=True,
  original32_iteration_budget_and_ten_trial_body_unchanged=True)
 try:
  P.require(sha(a.parent_binding)==a.parent_binding_sha256,'Exact parent binding bytes')
  old=P.read(a.parent_binding)
  P.require(old['schema']=='native-word-first-parent91-complete-binding-v1','Complete actual91 parent binding schema')
  system=S.NoJPrimalCurrent576System(a.snapshot_directory,a.snapshot_result_sha256)
  P.require(system.iteration==0 and system.sequence==0 and system.native_call==1,'One proposal on first original correction only')
  P.require(system.parent==old['parent_failed73'],'Same complete failed73 parent chain')
  P.require(system.current_state_sha256==P.STATE_SHA,'Literal old raw base, not rejected trial or projected seed')
  report.update(native_call=system.native_call,nonlinear_iteration=system.iteration,snapshot_sequence=system.sequence,
   current_state_sha256=system.current_state_sha256,snapshot_result=system.snapshot_result,
   new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
   parent_binding=dict(file=a.parent_binding.name,**P.digest(a.parent_binding)),
   old_complete_model_result=old['old_complete_model_screen'],
   original_actual_current_withJ_norm=system.current_records['norm'])
  report['input_binding']=P.write(out/'input-binding.json.gz',system.binding)
  raw={name:system.raw(name) for name in P.SHAPES}
  # All fresh stages/arrays were byte/shape/source checked by the complete
  # system adapter. Only this one-column proposal has nonzero model action.
  J=system.stage_raw(10)
  delta,unit,proposal,h=P.make_word_delta(raw['base-states'])
  P.require(proposal['exact_candidate_increment']==old['word_proposal']['exact_candidate_increment'],
            'The same original adjacent word proposal, not an altered QR direction')
  P.require(P.digest(P.safe(a.parent_binding.parent,old['word_proposal']['single_word_delta']['file']))['sha256']==hashlib.sha256(delta).hexdigest(),
            'New sparse proposal has the exact parent-screened complete delta bytes')
  fresh=P.screen_complete_model(raw,J,h,out/'fresh-complete-model','first-live-fresh-withJ-complete576-model')
  old_decrease=old['old_complete_model_screen']['predicted_strict_decrease']
  fresh_decrease=fresh['predicted_strict_decrease']
  P.require(type(old_decrease) is bool and type(fresh_decrease) is bool,'Explicit model selection booleans')
  selected=old_decrease and fresh_decrease
  entries=[]
  for name,data in [('complete-word-delta',delta),('proposed-unit-trial-states',unit)]:
   path=out/'large-arrays'/ (name+'.f64le');path.write_bytes(data)
   entry=dict(name=name,**P.descriptor(path,out),dtype='<f8',order='C',shape=[577,224])
   entries.append(entry)
  delta_entry,unit_entry=entries
  rows=[];negative_zeros=0
  for n in range(577):
   values=[struct.unpack_from('<d',delta,8*(n*224+j))[0] for j in range(224)]
   negative=[j for j in range(224) if P.word(delta,n*224+j)==1<<63]
   negative_zeros+=len(negative)
   rows.append(dict(node=n,state=values,negative_zero_columns=negative))
  delta_entry.update(finite=577*224,negative_zero=negative_zeros)
  packet=dict(schema='native-word-first-complete-original-coordinate-proposal-v1',
   source_sha256=sha(__file__),system_source_sha256=SYSTEM_SHA,parent_source_sha256=PARENT_SHA,
   snapshot_result=system.snapshot_result,new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
   input_binding=system.binding,native_call=1,nonlinear_iteration=0,snapshot_sequence=0,
   current_state_sha256=system.current_state_sha256,M=112,K=224,depth=576,
   delta_float64le_sha256=delta_entry['sha256'],proposed_unit_trial_state_sha256=unit_entry['sha256'],
   word_proposal=proposal,rows=rows,selected_for_original_trials=selected,
   original_q0_cut_far_not_projected=True,unmodified_other_state_coordinates_in_unit_trial=True,
   original_ten_trial_body_must_execute=True,original_strict_native_norm_and_domain_are_the_only_step_acceptance=True,
   native_accepted=False,task_completed=False)
  report['direction_checkpoint']=P.write(out/'word-direction-checkpoint.json.gz',packet)
  report['array_manifest']=P.write(out/'word-array-manifest.json',dict(
   schema='native-word-first-proposal-array-manifest-v1',source_sha256=sha(__file__),
   snapshot_result=system.snapshot_result,new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
   arrays=entries,native_accepted=False))
  report.update(completed=True,selected_for_original_trials=selected,
   selection_rule='strict exact saved-affine infinity decrease on both complete old and complete fresh129248 rows; proposal selector only',
   selection_does_not_accept_a_nonlinear_step=True,
   fallback='none' if selected else 'same-fresh-snapshot full original R273 direction',
   old_model_predicted_strict_decrease=old_decrease,fresh_model_predicted_strict_decrease=fresh_decrease,
   fresh_complete_model_result=fresh,word_proposal=proposal,native_delta=delta_entry,
   proposed_unit_trial_states=unit_entry,
   old_vs_fresh_eight_array_raw_identity={name:dict(old=old['original_arrays'][name]['sha256'],
      fresh=hashlib.sha256(data).hexdigest(),equal=old['original_arrays'][name]['sha256']==hashlib.sha256(data).hexdigest()) for name,data in raw.items()},
   fresh_full_J_raw_sha256=system.arrays['stage-jacobians']['raw_sha256'],
   old_full_J_descriptor_only=old['original_context']['raw_array_sha256']['stage-jacobians'],
   old_J_not_substituted_for_fresh_J=True)
 except Exception as error:
  report['actual_error']=repr(error);report['actual_traceback']=traceback.format_exc()
 finally:
  report['elapsed_seconds']=time.monotonic()-started
  full=P.write(out/'result.json.gz',report)
  keys=('completed','selected_for_original_trials','actual_error','native_call','nonlinear_iteration','snapshot_sequence',
   'current_state_sha256','new_matrix_identity_sha256','snapshot_result','native_delta','proposed_unit_trial_states',
   'direction_checkpoint','array_manifest','old_model_predicted_strict_decrease','fresh_model_predicted_strict_decrease','fallback')
  summary={key:report[key] for key in keys if key in report}
  summary.update(schema=SCHEMA,source_sha256=sha(__file__),system_source_sha256=SYSTEM_SHA,
   parent_source_sha256=PARENT_SHA,full_result=full,native_accepted=False,task_completed=False)
  P.write(out/'summary.json',summary)
 print(json.dumps(dict(event='complete_first_word_proposal_finished',completed=report['completed'],
  selected_for_original_trials=report['selected_for_original_trials'],native_accepted=False)),flush=True)
 return 0 if report['completed'] else 2

if __name__=='__main__':raise SystemExit(main())
