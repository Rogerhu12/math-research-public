#!/usr/bin/env python3
"""Read the single alpha=1 LM trial using the unchanged 8192 cubic auditor."""
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
MATRIX_SHA='ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4'
DIRECTION_SHA='5629db05e0cc7b014c6eb4375badb35ea1d408f40d8cdbccef88122e6150798e'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main(a):
 t=time.perf_counter()
 if sha(a.matrix_source)!=MATRIX_SHA or sha(a.direction)!=DIRECTION_SHA:raise ValueError('Frozen source/direction changed')
 s=importlib.util.spec_from_file_location('lm_audit_mf',a.matrix_source);mf=importlib.util.module_from_spec(s);s.loader.exec_module(mf)
 p,P,identities=mf.initialize(a);identities.update({str(a.direction):DIRECTION_SHA,str(Path(__file__)):sha(__file__)})
 with np.load(a.direction,allow_pickle=False)as d:
  if not np.array_equal(d['Y'],P.Y)or not np.array_equal(d['U'],P.U):raise ValueError('Direction base is not the original 1662 Y/U')
  Y=P.Y+d['dY'];U=P.U+d['dU']
 result=dict(schema='one-LM-fullstep-physical-cubic-audit-v1',source_sha256=sha(__file__),identities=identities,
  direction_file_sha256=DIRECTION_SHA,alpha=1.,candidate_YU_sha256=p.binary_sha(Y,U),
  complete_residual=P.summary(P.residual(Y,U)),physical=P.physical_samples(Y,U),
  nonlinear_solve_executed=False,accepted_parent=False,continuous_geometry_certified=False,
  definition='Literal original Y+dY/U+dU, all 602 nodes and 601 actual common-cubic midpoints, angles8192; no new solve or initial-warm re-audit.',seconds=time.perf_counter()-t)
 p.assert_sources(identities);a.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
 print(json.dumps(dict(output=str(a.out),sha256=sha(a.out),**result),allow_nan=False),flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','problem-source','warm','polynomial-source','matrix-source','direction','out'):a.add_argument('--'+key,type=Path,required=True)
 main(a.parse_args())
