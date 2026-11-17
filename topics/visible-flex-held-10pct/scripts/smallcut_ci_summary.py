#!/usr/bin/env python3
"""Print compact finite-prefix results and hashes; never upload generated arrays."""
import argparse,hashlib,json,os
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--directory',type=Path,required=True);a=p.parse_args()
rows=json.loads((a.directory/'continuation.json').read_text()) if (a.directory/'continuation.json').exists() else []
hashes={str(x.relative_to(a.directory)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(a.directory.glob('*')) if x.is_file()}
report=dict(scope='Finite open-prefix computation; not a closed flexible surface.',run_id=os.getenv('GITHUB_RUN_ID'),run_attempt=os.getenv('GITHUB_RUN_ATTEMPT'),git_sha=os.getenv('GITHUB_SHA'),rows=rows,output_sha256=hashes)
print('HELD10_COMPACT_RESULT='+json.dumps(report,separators=(',',':')))
if os.getenv('GITHUB_STEP_SUMMARY'):
 with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as f:
  f.write('## Finite small-cut prefix\n\nNo closed-surface claim.\n\n| stage | solved | metric L1 | curvature | height | endpoint H |\n|---|---|---|---|---|---|\n')
  for z in rows:f.write('| '+ ' | '.join(str(z.get(k,'')) for k in ('name','success','metric_l1','kappa_sample','height_max','terminal_height_coeff_max'))+' |\n')
  f.write('\nAll generated arrays remain temporary. Run ID: '+str(report['run_id'])+'\n')
