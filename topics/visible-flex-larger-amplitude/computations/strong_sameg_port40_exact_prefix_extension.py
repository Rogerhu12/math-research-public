#!/usr/bin/env python3
"""Reuse the real saved 64-mode linear transfer to extend only port entries.

Author: strong_recovery (GPT-6 Astra Pro, AI assisted), 2026-11-13.
Keep every physical parameter, physical cut field and the original32 slopes
bit for bit. Append frequencies66..80 from the actually saved original-g
4096-step transfer. This is a finite linear initialization port, not a new
nonlinear tail response. The original --frozen-port identity gate is required.
No source, curve, ODE or mathematical acceptance criterion is changed.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import importlib.util
import json
import math
import struct
import sys

HERE=Path(__file__).resolve().parent
EXPECTED={
 'computations/alternative-neck-provider-smallcut30-port32-r2048.json':'7d3f77821453ccd81ca8eaba9634c899127455b76ec1b95ba27fb130503d4100',
 'computations/tail_smallcut30_port64_r4096.json':'af9482cfbd026c048c621d1aa5c78633c08f9d351b97d64ea6f3ee6366378d79',
 'notes/2026-11-12-tail-linear64-r4096-shared.json':'ad19f6592e0d658a96fce9f46459ad97aff8f3f4b0604135e28b63acb1c44571',
 'computations/geometric-fixed-dual-prefix.py':'f189c8f94880ff5455a140a686219a1805399e1d45a3809e176630bb92772280',
}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False)
def bits(v):return b''.join(struct.pack('<d',float(x)) for x in v)
def write(path,value):
 data=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
 if path.exists():
  if path.read_bytes()!=data:raise FileExistsError(path)
 else:path.write_bytes(data)

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);p.add_argument('--report',type=Path,required=True);a=p.parse_args()
 gates={}
 def check(k,v):
  if not v:raise ValueError(k)
  gates[k]=True
 for path,wanted in EXPECTED.items():check('sha:'+path,sha(path)==wanted)
 old_path=Path(next(iter(EXPECTED)));old=json.loads(old_path.read_text())
 ext=json.loads(Path('computations/tail_smallcut30_port64_r4096.json').read_text())
 run=json.loads(Path('notes/2026-11-12-tail-linear64-r4096-shared.json').read_text())
 check('same_physical_parameters',canonical(old['parameters'])==canonical(ext['parameters']))
 check('same_untagged_physical_cut',canonical({k:v for k,v in old['cut'].items() if k!='_prefix_bridge'})==canonical(ext['cut']))
 check('original_modes_preserved',old['modes']==list(range(2,65,2)) and ext['modes'][:32]==old['modes'])
 check('original_slopes_all_bits_preserved',bits(ext['linearSlope'][:32])==bits(old['linearSlope']))
 check('actual_original_linear_run',run['steps']==4096 and run['far']==48 and run['spacing']==2 and run['modes']==64 and run['source_revision']=='869436630c99aa5a68afb55bd8877c826034d117')
 check('all_physical_config_keys_same',all(canonical(run['config'].get(k))==canonical(v) for k,v in old['parameters'].items()))
 rows={r['mode']:r for r in run['rows']};added=list(range(66,81,2));slopes=[rows[m]['slope'] for m in added]
 check('added_actual_rows_match_saved_port',bits(slopes)==bits(ext['linearSlope'][32:40]) and all(math.isfinite(x) for x in slopes))
 new=copy.deepcopy(old);new.update(scope=__doc__,modes=old['modes']+added,linearSlope=old['linearSlope']+slopes,
  exact_prefix_extension=dict(source_sha256=EXPECTED,preserved_count=32,added_frequencies=added,
   old_linear_values_preserved_bitwise=True,parameters_and_all_cut_fields_preserved=True,
   actual_saved_transfer_used=True,new_nonlinear_response_computed=False))
 write(a.out,new)
 spec=importlib.util.spec_from_file_location('sameg_port_extension_original_gate',HERE/'geometric-fixed-dual-prefix.py');utility=importlib.util.module_from_spec(spec);sys.modules[spec.name]=utility;spec.loader.exec_module(utility)
 port,verified=utility.verify_port({'physical_port_sha256':sha(old_path)},a.out,old_path)
 check('original_prefix_extension_gate_passed',verified['kind']=='exact_prefix_preserving_extension' and verified['old_mode_values_identical'] and verified['physical_parameters_and_cut_canonical_bytes_identical'])
 write(a.report,dict(scope=__doc__,all_checks=True,gates=gates,original_port=str(old_path),original_port_sha256=sha(old_path),output={'file':str(a.out),'sha256':sha(a.out)},source_sha256={**EXPECTED,str(Path(__file__)) :sha(__file__)},original_verification=verified,added_rows=[rows[m] for m in added],Node_ODE_or_J_calls=0))
 print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),checks=len(gates),report_sha256=sha(a.report))),flush=True)

if __name__=='__main__':main()
