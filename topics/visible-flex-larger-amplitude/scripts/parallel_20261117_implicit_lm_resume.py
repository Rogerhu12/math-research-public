#!/usr/bin/env python3
"""Exact-source startup patch for the interrupted927f run, not a new budget.

Replays only unfinished direction2 from accepted002 at damp.25. Directions0/1,
initial column norms and accepted audits are reused. Observed lost partial64+
LSMR work is recorded separately, not called a returned direction or a failure.
"""
import argparse,hashlib,json,os,sys
from pathlib import Path
BASE_SHA='927f403f984c88471dedaf14988b6cd25ebd44b5ce3d0a1e6a0bcc57ea20cc0d'
CHECKPOINT_SHA='84b1f854dabfbacca654be5b91a46cf4946b2198c9b5c3bc859d3a6a8319e821'
LOG_SHA='16940942748d446f68fa9b8823e88a14f96959b413eee444cbd1ccee7aae06a1'
STATE_SHA='6198aa6e3b1fe8f4c86bd443882912c279eef692bd69a4f013e9cd1488b929b5'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--base-source',type=Path,required=True)
 p.add_argument('--emit-source',type=Path,required=True);p.add_argument('--emit-only',action='store_true');a,rest=p.parse_known_args()
 if sha(a.base_source)!=BASE_SHA:raise ValueError('Original927f source identity changed')
 text=a.base_source.read_text();generator_sha=sha(__file__)
 def replace(old,new):
  nonlocal text
  if text.count(old)!=1:raise ValueError('Expected a unique literal source marker: '+old[:80])
  text=text.replace(old,new,1)
 def region(start,end,new):
  if text.count(start)!=1 or text.count(end)!=1:raise ValueError('Ambiguous source region')
  replace(text[text.index(start):text.index(end)],new)
 replace("MATRIX_SHA=",f"RECOVERY_BASE_SHA='{BASE_SHA}'\nRECOVERY_GENERATOR_SHA='{generator_sha}'\nRECOVERY_CHECKPOINT_SHA='{CHECKPOINT_SHA}'\nRECOVERY_LOG_SHA='{LOG_SHA}'\nRECOVERY_STATE_SHA='{STATE_SHA}'\nMATRIX_SHA=")
 replace("identities[str(ls_source)]=sha(ls_source);p.assert_sources(identities)",
 "identities[str(ls_source)]=sha(ls_source);identities.update({str(a.recovery_base_source):RECOVERY_BASE_SHA,str(a.recovery_generator_source):RECOVERY_GENERATOR_SHA,str(a.resume_checkpoint):RECOVERY_CHECKPOINT_SHA,str(a.interruption_log):RECOVERY_LOG_SHA});p.assert_sources(identities)")
 region(" with np.load(a.first_direction,allow_pickle=False)as d:"," policy=dict(",''' resume=json.loads(gzip.decompress(a.resume_checkpoint.read_bytes()))
 if (resume['source_sha256'],resume['accepted_algebraic_steps'],resume['directions_used'],resume['damp_next'])!=(RECOVERY_BASE_SHA,2,2,.25):raise ValueError('Wrong frozen accepted002 checkpoint')
 if not np.array_equal(resume['mesh'],P.x):raise ValueError('Recovered mesh changed')
 archive=Path(resume['state_archive'])
 if sha(archive)!=RECOVERY_STATE_SHA or resume['state_archive_sha256']!=RECOVERY_STATE_SHA:raise ValueError('Accepted002 archive changed')
 identities[str(archive)]=RECOVERY_STATE_SHA
 Y=np.array(resume['states']);U=np.array(resume['independent_velocities'])
 with np.load(archive,allow_pickle=False)as stored:
  if not np.array_equal(Y,stored['Y'])or not np.array_equal(U,stored['U']):raise ValueError('Checkpoint and accepted002 differ')
 R=P.residual(Y,U)
 if P.summary(R)!=resume['residual_summary']:raise ValueError('Recovered complete residual changed')
 log=[json.loads(line)for line in a.interruption_log.read_text().splitlines()]
 last=log[-1]
 if (last.get('event'),last.get('direction_index'),last.get('damp'),last.get('matvecs'),last.get('rmatvecs'))!=('LM_budget_linear_progress',2,.25,64,64):raise ValueError('Wrong observed partial direction')
 if len(resume['history'])!=2 or resume['history'][-1]['direction_index']!=1 or not resume['history'][-1]['accepted']:raise ValueError('Completed history changed')
 recovery=dict(original_source_sha256=RECOVERY_BASE_SHA,generator_source_sha256=RECOVERY_GENERATOR_SHA,
  checkpoint_sha256=RECOVERY_CHECKPOINT_SHA,interruption_log_sha256=RECOVERY_LOG_SHA,accepted_state_archive_sha256=RECOVERY_STATE_SHA,
  restored_accepted_steps=2,restored_completed_direction_count=2,restarted_unfinished_direction_index=2,restarted_damp=.25,
  observed_lost_partial_matvec_lower_bound=64,observed_lost_partial_rmatvec_lower_bound=64,
  lost_partial_total_actions_unknown=True,completed_direction2_or_trial_saved=False,
  interruption_cause='Unknown; old executor session returned Unknown process id, log stopped without terminal output. No algorithm failure or termination signal is inferred.',
  scientific_budget_refreshed=False,completed_steps_recomputed=False)
''')
 region(" history=[dict(direction_index=0", " state_file=None;state_sha=None",''' if policy!=resume['policy']:raise ValueError('Original24/20 acceptance policy changed')
 history=resume['history'];accepted=2;directions=2;damp=.25;J=None;failure=None
''')
 region(" save_state();emit(event='LM_budget_start_cached_zero'", " while directions<MAX_DIRECTIONS",''' save_state();emit(event='LM_budget_resumed_after_executor_interruption',source_sha256=source_sha,recovery=recovery,
  accepted=accepted,directions_completed=directions,direction_to_resume=2,damp=damp,raw_SSE=R['cost'],base_YU_sha256=p.binary_sha(Y,U))
''')
 replace("source_sha256=source_sha,identities=identities,\n  M=P.M", "source_sha256=source_sha,identities=identities,recovery=recovery,\n  M=P.M")
 replace("schema='complete-Pr-LM-checkpoint-v1',source_sha256=source_sha,identities=identities,", "schema='complete-Pr-LM-checkpoint-v1',source_sha256=source_sha,identities=identities,recovery=recovery,")
 replace("'first-physical','work','out')", "'first-physical','work','out','recovery-base-source','recovery-generator-source','resume-checkpoint','interruption-log')")
 compile(text,str(a.emit_source),'exec');a.emit_source.write_text(text)
 print(json.dumps(dict(event='LM_recovery_source_generated',path=str(a.emit_source),sha256=sha(a.emit_source))),flush=True)
 if not a.emit_only:
  os.execv(sys.executable,[sys.executable,str(a.emit_source),*rest,'--recovery-base-source',str(a.base_source),'--recovery-generator-source',str(Path(__file__))])
if __name__=='__main__':main()
