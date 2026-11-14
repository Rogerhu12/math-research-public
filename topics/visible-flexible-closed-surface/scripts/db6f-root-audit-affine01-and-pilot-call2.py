#!/usr/bin/env python3
"""Audit two closed negative records; never run a BVP, DN, or worker."""
import argparse, hashlib, importlib.util, json
from pathlib import Path
from collections import Counter

ap=argparse.ArgumentParser(); ap.add_argument('--out',type=Path,required=True); a=ap.parse_args()
topic=Path(__file__).resolve().parents[1]; n=topic/'notes'; pre='2026-11-09-db6f-'
helper=topic/'scripts/db6f-prefix-tail-linear-continuation-client-v2.py'
assert hashlib.sha256(helper.read_bytes()).hexdigest()=='6d278d78e275df2e0e66db3eb0edb592321fecc22c1c229eacd53f5869166d15'
spec=importlib.util.spec_from_file_location('closed_packet_helpers',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
files=[helper,Path(__file__)]
def named(name): return n/(pre+name)
def checked(name,sha=None):
 p=named(name)
 if sha: assert m.identity(p)['sha256']==sha
 files.append(p);return m.read(p)
ag=checked('root-spectral-affine-m14q512-01-guard-launch.json','ce1d05787e40c3b9cd3ff42443ef3de66f275c9be3135ff5c6b430e6cabc2b92')
assert len(ag['bound_files'])==113
for row in ag['bound_files']:m.verify(row)
assert ag['per_process_RLIMIT_DATA_bytes']==1536*1024*1024
al=checked('prefix-spectral-affine-m14q512-01-launch.json','e45c553ea6832525c6a2719a197dbcc49a7ee5dd77badfb4b363e19a4b974a83')
assert ag['command']==al['command'] and ag['source_launch']==m.identity(named('prefix-spectral-affine-m14q512-01-launch.json'))
ac=checked('root-spectral-affine-m14q512-01-guard-completion.json','4c6470451712d61c36c767267d9211bb1e1feafa7f791520ce49eee9719a0601')
ar=checked('prefix-spectral-affine-m14q512-01-reproduction.json','05f117461c7dba5c0d174d95ca963ef213a1c1ffab4f4108c8b43487e99180a1')
asu=checked('prefix-spectral-affine-m14q512-01-summary.json','db6ee7040b3092ebb06253e542f7ab00b33fd860de35f34fbbd756c960721c01')
assert ac['binding_sha256']==m.identity(named('root-spectral-affine-m14q512-01-guard-launch.json'))['sha256']
assert ac['actual_child_exit_code']==2 and ac['tool_exit_observed_by_root'] is False
for d in (ar,asu):
 assert d['status']=='FROZEN_AFFINE_DIAGNOSTIC_EXCEPTION' and d['success'] is False
 assert d['error_type']=='MemoryError' and d['requested_process_exit_code']==2
 assert d['actual_new_DN_calls']==0 and d['actual_nonlinear_tail'] is False and d['frozen_affine_dn'] is True
 assert d['runtime_newton_identity_is_original'] is True and d['initial_nodes']==2633
 assert d['settings']==al['settings']
assert len(ar['spectral_solver_records'])==1
sr=ar['spectral_solver_records'][0]
assert sr['status']=='WEIGHTED_COLLOCATION_EXCEPTION' and sr['error']=='MemoryError()'
assert (sr['initial_nodes'],sr['state_components'],sr['parameters'],sr['maximum_nodes'])==(2633,43,14,6500)
assert sr['original_tol']==2e-9 and sr['original_bc_tol']==1e-8 and sr['weights']==al['weights']
assert not Path(al['checkpoint_output']).exists()
assert not list(n.glob(Path(al['coefficient_output_pattern']).name))
alog=named('prefix-spectral-affine-m14q512-01-run.log');files.append(alog)
assert m.identity(alog)['sha256']=='048a18d0401f2900639a74edb5fd8223a286acb497e91c3c1ccfb504f6d1ae36'
log=alog.read_text();assert '4.75e-07' in log and '2.09e-14' in log and '2414' in log and 'MemoryError' in log
pg=checked('root-linear-dn-pilot-v2-01-guard-launch.json','ac6ecb605fdb14d5af91e7cc00520d21673bab006d00f8108556b7876871e54d')
assert len(pg['bound_files'])==161
for row in pg['bound_files']:m.verify(row)
plpath=Path(pg['original_pilot_launch']['path']);m.verify(pg['original_pilot_launch']);files.append(plpath);pl=m.read(plpath)
policy=m.read(pl['policy']['path']);boot=m.read(pl['bootstrap_packet']['path']);goal=m.read(pl['target_packet']['path'])
p2=Path(pl['record_prefix']+'_0002.json.gz');files.append(p2)
assert m.identity(p2)['sha256']=='c6889ba47c662ac0c66898b8abc7a087c61ecc1bf3675fdc1a6110e12a490f67'
r2=m.read(p2);cfg=m.read(pl['config']['path'])
assert set(r2)=={'request','response','config','source_sha256'}
assert m.canonical(r2['config'])==m.canonical(cfg)
assert m.canonical(r2['source_sha256'])==m.canonical(policy['source_sha256']) and len(r2['source_sha256'])==9
req=r2['request'];assert set(req)=={'height','jacobian','audit'} and req['jacobian'] is False and req['audit'] is False
origin=m.np.asarray(boot['request']['height'],float);target=m.np.asarray(goal['request']['height'],float)
assert m.same_height(req['height'],origin+(1/8)*(target-origin)) and not m.same_height(req['height'],target)
resp=r2['response'];assert set(resp)=={'failed','lastIteration','checkpoint'}
assert resp['lastIteration']['iteration']==7 and resp['lastIteration']['norm']==0.08024434977172676
# The same live process supplies these parameters in its already-closed bootstrap.
first=m.read(Path(pl['record_prefix']+'_0001.json.gz'))
parameters=first['response']['checkpoint']['parameters'];m.validate_checkpoint(resp['checkpoint'],15,parameters)
assert m.same_height(resp['checkpoint']['cutHeight'],req['height'])
active=Path(cfg['trialDiagnosticFile']);raw=active.read_bytes();selected=[];rows=[]
for line in raw.splitlines(keepends=True):
 if not line.endswith(b'\n'):continue
 row=json.loads(line)
 if row.get('call')==2: selected.append(line);rows.append(row)
proof=m.classify_original_failure(r2,2,rows,cfg['maxIterations'])
assert proof and proof['kind']=='closed-known-numerical-ten-trial-rejection' and proof['iteration_groups']==8
closed=named('root-linear-dn-pilot-v2-01-call002-closed-trials.jsonl');payload=b''.join(selected)
if closed.exists(): assert closed.read_bytes()==payload
else:
 with closed.open('xb') as f:f.write(payload)
files.append(closed)
# Only the immutable selected call is bound. The active file is not advertised as frozen.
report={'status':'CLOSED_AFFINE_RESOURCE_FAILURE_AND_ORIGINAL_PILOT_CALL2_FAILURE_VERIFIED',
 'affine':{'source_bindings_rehashed':113,'guard_child_exit_code':2,'actual_final_tool_exit_observed':False,'tool_handle_lost':True,'program_error':'MemoryError','per_process_data_cap_bytes':1536*1024*1024,'initial_nodes':2633,'printed_next_nodes':5047,'printed_weighted_rms':'4.75e-07','printed_bc_residual':'2.09e-14','printed_values_are_rounded_not_final_certificates':True,'new_checkpoint_exists':False,'new_coefficient_files_exist':False,'actual_new_dn_calls':0,'original_runtime_newton_identity':True,'mathematical_nonexistence_not_inferred':True},
 'pilot_call2':{'source_bindings_rehashed':161,'physical_call':2,'linear_path_tau':'1/8','last_iteration':resp['lastIteration'],'classification':proof,'trial_kind_counts':dict(Counter(row['kind'] for row in rows)),'checkpoint_shape':[865,30],'raw_shape':[13,30],'jacobian_requested':False,'audit_requested':False,'no_success_or_target_goal_inferred':True,'pilot_final_tool_exit_not_observed':True},
 'files':[m.identity(p) for p in files], 'solver_calls':0,'scope':'Closed failed calls only. No new coupled prefix, final seam, continuous metric, geometry or G5 claim.'}
with a.out.open('x') as f:json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'status':report['status'],'affine_sources':113,'pilot_sources':161,'pilot_call2_norm':resp['lastIteration']['norm'],'trial_rows':len(rows),'report':m.identity(a.out)},ensure_ascii=False))
