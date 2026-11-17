"""Create a source-identical nonlinear worker with only a named physical factory change.

The original root, flow, guards, Newton solve, diagnostics and audit are unchanged.
All relative source imports are made absolute. Physical warm comparisons include
outerCellDesign, preventing a design change being called same-metric refinement.
"""
import argparse,hashlib,json,re
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('topic',type=Path);p.add_argument('out',type=Path);a=p.parse_args()
src=a.topic/'scripts/78718-prefix-tail-tangent-fourier-worker.mjs';s=src.read_text();s=s.replace("from './closing_weighted_tail.mjs'", "from '"+str(a.out.parent/'hybrid_outer_factory.mjs')+"'")
s=re.sub(r"'\./([^']+)'",lambda m:repr(str(a.topic/'scripts'/m[1])),s)
s=s.replace("['pulseCaps','valleyCaps'", "['outerCellDesign','pulseCaps','valleyCaps'")
a.out.write_text(s)
(a.out.parent/'hybrid_worker_transform.json').write_text(json.dumps(dict(scope=__doc__,source=str(src),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),output=str(a.out),output_sha256=hashlib.sha256(a.out.read_bytes()).hexdigest()),indent=2)+'\n')
