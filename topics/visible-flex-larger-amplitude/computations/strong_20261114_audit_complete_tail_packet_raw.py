#!/usr/bin/env python3
"""Portable original current-H audit from raw states without optional snapshots.

All original raw-state validation, nonlinear solve, full Jacobian, metric and
audit tests remain. Only the optional preloaded full-flow predictor is declined;
fresh full-flow tangents are generated and saved normally by the original code.
"""
import hashlib,json,sys
from pathlib import Path
import strong_full_tangent_tail_client as client
import strong_20261114_audit_complete_tail_packet as entry

def main():
 prefix=Path(sys.argv[sys.argv.index('--out-prefix')+1]);prefix.parent.mkdir(parents=True,exist_ok=True)
 record=dict(scope=__doc__,wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),retained_entry_sha256=hashlib.sha256(Path(entry.__file__).read_bytes()).hexdigest(),optional_snapshot_preload=False,all_original_mathematical_gates_preserved=True)
 prefix.with_name(prefix.name+'-raw-start.json').write_text(json.dumps(record,indent=2)+'\n')
 old=client.checkpoint_snapshot;client.checkpoint_snapshot=lambda config:None
 try:entry.main()
 finally:client.checkpoint_snapshot=old
if __name__=='__main__':main()
