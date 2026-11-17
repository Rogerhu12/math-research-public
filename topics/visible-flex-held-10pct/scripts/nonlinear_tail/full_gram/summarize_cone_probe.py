"""Keep scalar results and hashes; never persist generated Gram or state arrays."""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('reports',type=Path,nargs='+');p.add_argument('--out',type=Path,required=True);a=p.parse_args();runs=[]
for path in a.reports:
 d=json.loads(path.read_text());rows=[]
 for record in d['rows']:
  row={k:v for k,v in record.items()if k!='Gram'}
  if 'Gram'in record:
   J=record['M']+1;G=np.asarray(record['Gram']).reshape(J,J);e=np.linalg.eigvalsh(G)
   row.update(gram_negative_eigenvalues=int((e<0).sum()),gram_eigen_min=float(e.min()),gram_min_absolute_eigenvalue=float(abs(e).min()),gram_condition_2=float(max(abs(e))/min(abs(e))))
  rows.append(row)
 runs.append(dict(source_report_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),module_sha256=d['module_sha256'],input_sha256=d['input_sha256'],source_sha256=d['source_sha256'],rows=rows))
summary=dict(scope=__doc__,meaning='Independent seeds on exact cone references in nonsingular finite indefinite charts; no amplitude passage through Gram singularities and no infinite-mode inverse.',numpy=np.__version__,runs=runs)
a.out.write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({'runs':len(runs),'cases':sum(len(x['rows'])for x in runs),'all_success':all(r['success']for x in runs for r in x['rows'])}))
