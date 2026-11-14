#!/usr/bin/env python3
"""Evaluate the new first-turn scalar profile interface and every scalar join.

This is a geometry/interface computation only. It starts no Flow IVP, Jacobian,
BVP, or tail worker, and produces no new nonlinear surface. It checks complete
segment identity at eps=.08, all a/a'/a'' joins, both complete endpoint jets,
and the unchanged finite bridge and physical tail interfaces.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,gzip,hashlib,importlib.util,json,math,sys
from pathlib import Path
import numpy as np
import strong_20261114_descending_turn_ramp as adapter

def read(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--accepted',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();accepted=read(a.accepted);cfg=accepted['frozen_profile'];path=Path(__file__).with_name('alternative-neck-provider.py')
 spec=importlib.util.spec_from_file_location('first_turn_interface_original_provider',path);provider=importlib.util.module_from_spec(spec);spec.loader.exec_module(provider)
 import strong_initial_speed_pulse as pulse
 import strong_monotone_initial_speed_anchor as frontload
 pulse.install(provider);frontload.install(provider)
 old=provider.NeckPrefix(cfg);port=provider.tagged_port(read(a.port),cfg);bridge=provider.NeckTerminalBridge(port['cut']);old_segments=canonical(old.segments);bridge_segments=canonical(bridge.segments)
 adapter.install(provider);base=provider.NeckPrefix(cfg)
 if canonical(base.segments)!=old_segments:raise ValueError('Default eps does not reproduce every A segment')
 checks=[]
 for eps in (.08,.07,.09,.12):
  profile={**cfg,adapter.FIELD:eps};neck=provider.NeckPrefix(profile);tagged=provider.tagged_port(read(a.port),profile);br=provider.NeckTerminalBridge(tagged['cut'])
  if tagged!=port or canonical(br.segments)!=bridge_segments:raise ValueError('The finite bridge or physical tail port changed')
  pieces=[*neck.segments,*[{**s,'s0':neck.end+s['s0'],'s1':neck.end+s['s1'],'h0':neck.height+s['h0'],'h1':neck.height+s['h1']} for s in br.segments]]
  jumps=[]
  for left,right in zip(pieces[:-1],pieces[1:]):
   l=np.array(provider.piece_jet(left,1.),float);r=np.array(provider.piece_jet(right,0.),float)
   def xyz(jet,z):
    a0,ap,app=jet;zp=math.sqrt(1-ap*ap);return np.array([[a0,0.,z],[ap,0.,zp],[app,0.,-ap*app/zp]])
   cartesian=xyz(l,left['h1'])-xyz(r,right['h0'])
   jumps.append(dict(physical_s=left['s1'],left_kind=left['kind'],right_kind=right['kind'],difference=(l-r).tolist(),background_XYZ_012_jet_difference=cartesian.tolist()))
  inlet=np.array(neck.profile(0.),float);neck_end=np.array(neck.profile(neck.end),float);terminal=np.array([x[0] for x in br.profile(br.end)],float)
  original_inlet=np.array(old.profile(0.),float);original_neck=np.array(old.profile(old.end),float);original_terminal=np.array([x[0] for x in bridge.profile(bridge.end)],float)
  if not np.array_equal(inlet,original_inlet) or not np.array_equal(terminal,original_terminal):raise ValueError('A complete endpoint jet changed')
  error=max(max(abs(np.array(q['difference'])).max(),abs(np.array(q['background_XYZ_012_jet_difference'])).max()) for q in jumps)
  if error>5e-12 or abs(neck_end-original_neck).max()>5e-12:raise ValueError('A full scalar jet join failed')
  i=next(i for i,s in enumerate(neck.segments) if s['kind']=='turn' and s['p0']>0>s['p1']);turn=neck.segments[i]
  # The first turn's endpoint slopes/second jets, and its angle endpoints/peak K,
  # are preserved. Its end radius is allowed to vary in this new metric design.
  before=old.segments[i]
  for k in ('p0','p1','K'):
   if turn[k]!=before[k]:raise ValueError('First-turn angle endpoint or peak curvature changed')
  if eps==.08 and canonical(neck.segments)!=old_segments:raise ValueError('Explicit eps=.08 changed A segments')
  checks.append(dict(eps=eps,new_prefix_metric=(eps!=.08),all_A_segments_exact_at_default=(canonical(neck.segments)==old_segments),prefix_length=neck.end,background_prefix_height=neck.height,first_turn=dict(index=i,length=turn['length'],p0=turn['p0'],p1=turn['p1'],peak_K=turn['K'],start_jet=np.array(provider.piece_jet(turn,0.),float).tolist(),end_jet=np.array(provider.piece_jet(turn,1.),float).tolist()),inlet_jet=inlet.tolist(),prefix_bridge_jet=neck_end.tolist(),physical_cut_jet=terminal.tolist(),complete_scalar_endpoint_jets_identical=True,all_background_Cartesian_012_joins_checked=True,changed_prefix_height_allowed=True,max_join_jump=float(error),all_joins=jumps,physical_tail_port_and_complete_bridge_exact=True))
 out=dict(scope=__doc__,source_sha256=sha(__file__),adapter_sha256=sha(adapter.__file__),provider_sha256=sha(path),accepted_sha256=sha(a.accepted),port_sha256=sha(a.port),default_A_all_segment_structure_bitwise_identical=True,checks=checks,all_new_values_are_new_prefix_metrics=True,tail_metric_and_cut_unchanged=True,new_nonlinear_solution=False,actual_BVP_control_response_not_yet_computed=True)
 a.out.parent.mkdir(exist_ok=True,parents=True);a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(out=str(a.out),default_A_identical=True,max_jump=max(x['max_join_jump'] for x in checks))))
if __name__=='__main__':main()
