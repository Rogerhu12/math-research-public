#!/usr/bin/env python3
"""Compare actual full and half changed-H tail responses to the accepted A tangent.

This reads complete converged original tail packets. A changed-H response is
not acceptance of its prefix, and unaudited packets remain unaudited. The
comparison uses every H coordinate and the original 98-by-32 full Jacobian,
with the source block layout (slope, second, two means, height).
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,gzip,hashlib,json
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))
def main():
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('baseline','full','half','out'):p.add_argument('--'+k,type=Path,required=True)
 a=p.parse_args();paths=[a.baseline,a.full,a.half];d=[read(f) for f in paths];M=len(d[0]['request']['height']);io={'traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint'}
 cfg=[{k:v for k,v in x['config'].items() if k not in io} for x in d]
 if cfg[0]!=cfg[1] or cfg[0]!=cfg[2]:raise ValueError('Physical/numerical tail configuration changed')
 for x in d:
  if not x['response']['converged'] or x['response']['residual']>x['config']['solveTolerance']:raise ValueError('An original full tail solve did not converge')
 H=[np.array(x['request']['height']) for x in d];J=[np.array(x['response']['heightJetJacobian']).reshape(3*M+2,M) for x in d]
 blocks=[('slope',0,M),('second',M,M),('meanSlopeCorrection',2*M,1),('meanSecondCorrection',2*M+1,1)]
 out=dict(scope=__doc__,source_sha256=sha(__file__),inputs=[dict(file=str(f),sha256=sha(f)) for f in paths],all_nonIO_tail_parameters_equal=True,complete_H_half_affinity_max_error=float(abs(H[2]-(H[0]+H[1])/2).max()),cases=[],original_tail_solve_tolerance=d[0]['config']['solveTolerance'],new_prefix_solution=False)
 for k,label in [(1,'full'),(2,'half')]:
  dh=H[k]-H[0];linear=J[0]@dh;r=d[k]['response'];base=d[0]['response'];row=dict(label=label,complete_H=H[k].tolist(),max_height_change=float(abs(dh).max()),original_nonlinear_residual=r['residual'],audit_present=r.get('audit') is not None,blocks={})
  for name,offset,count in blocks:
   actual=np.atleast_1d(r['jets'][name])-np.atleast_1d(base['jets'][name]);defect=actual-linear[offset:offset+count];jd=J[k][offset:offset+count]-J[0][offset:offset+count]
   row['blocks'][name]=dict(max_actual_jet_change=float(abs(actual).max()),max_defect_from_A_full_tangent=float(abs(defect).max()),full_defect=defect.tolist(),max_J_change=float(abs(jd).max()),relative_J_change=float(abs(jd).max()/max(1.,abs(J[0][offset:offset+count]).max())))
  out['cases'].append(row)
 out['observed_full_to_half_defect_ratios']={name:out['cases'][0]['blocks'][name]['max_defect_from_A_full_tangent']/out['cases'][1]['blocks'][name]['max_defect_from_A_full_tangent'] for name,_,_ in blocks}
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(out=str(a.out),ratios=out['observed_full_to_half_defect_ratios']),indent=2))
if __name__=='__main__':main()
