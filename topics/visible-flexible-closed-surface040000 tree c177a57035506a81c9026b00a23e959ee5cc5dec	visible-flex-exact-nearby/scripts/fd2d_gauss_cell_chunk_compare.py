#!/usr/bin/env python3
"""One actual-input comparison of whole and cell-block assembly, separate processes."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,json,time,resource,datetime
from pathlib import Path
import numpy as np
from fd2d_gc_raw_bump_turn_mesh import TurnResolvedRawBumpDAE
from fd2d_gc_archive_arrays import identity,load_npz,save_npz

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--candidate',type=Path,required=True);ap.add_argument('--field',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--mode',choices=['whole','chunk'],required=True);args=ap.parse_args()
 start=time.monotonic();here=Path(__file__).resolve().parent
 if any(args.out.parent.glob(args.out.name+'*')):raise FileExistsError('Use a new unique output stem')
 from fd2d_gc_gauss_cell_codazzi import gauss_cell_codazzi as whole
 from fd2d_gc_gauss_cell_codazzi_chunked import gauss_cell_codazzi as chunk
 saved=load_npz(args.field);problem=TurnResolvedRawBumpDAE(args.candidate,modes=int(saved['modes']),max_step=.04,profile_count=int(saved['profile_count']),supports=saved['profile_supports'],base_kind=str(saved['base_kind']),blend=tuple(saved['blend']))
 if not np.array_equal(problem.x,saved['mesh']):raise ValueError('Actual saved mesh mismatch')
 if problem.seed_weight_definition!=json.loads(str(saved['seed_weight_definition'])):raise ValueError('Actual seed definition mismatch')
 z=np.r_[saved['corrections'].ravel(),saved['parameters']];direction=np.random.default_rng(141560).standard_normal(len(z));direction/=np.linalg.norm(direction)
 print(json.dumps(dict(stage='bound_actual_input',mode=args.mode,nodes=problem.N,size=problem.size,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
 result=(whole if args.mode=='whole' else chunk)(problem,z,order=2,high_weight=1.,jacobian=True)
 peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 arrays={key:result[key] for key in ('retained_residual','high_residual','retained_cells','omitted_codazzi_cells','full_codazzi_cells','point_gauss','quadrature_points')}
 for key in ('retained','high'):arrays[key+'_Jd']=result[key+'_jacobian']@direction
 packet=save_npz(args.out.with_name(args.out.name+'-values.npz'),**arrays)
 report=dict(schema='fd2d-gauss-cell-assembly-actual-input-run-v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),mode=args.mode,source=identity(__file__),helpers=[identity(here/n) for n in ('fd2d_gc_gauss_cell_codazzi.py','fd2d_gc_gauss_cell_codazzi_chunked.py')],candidate=identity(args.candidate),field=identity(args.field),unknowns=problem.size,nodes=problem.N,info=result['info'],arrays=packet,helper_peak_rss_kib=peak,whole_process_peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,seconds=time.monotonic()-start,nonlinear_solve_performed=False,continuous_certificate=False)
 args.out.with_name(args.out.name+'-report.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(dict(mode=args.mode,seconds=report['seconds'],helper_peak_rss_kib=peak,values=packet,low_nnz=result['retained_jacobian'].nnz,high_nnz=result['high_jacobian'].nnz)),flush=True)
 return 0
if __name__=='__main__':raise SystemExit(main())
