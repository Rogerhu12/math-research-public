#!/usr/bin/env python3
"""Finite radial linear resonance diagnostics for chosen mode-two designs.
No conclusion about the full nonradial nonlinear Jacobian is implied.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,importlib.util,json,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
import numpy as np

def main():
 p=argparse.ArgumentParser();p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--profile',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--modes',type=int,default=24);a=p.parse_args();start=time.time()
 spec=importlib.util.spec_from_file_location('m2wrap',Path(__file__).with_name('numerical-m2-prefix.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);ad=m.load(a.source_topic)
 chart=json.loads((a.source_topic/'notes/2026-11-09-950f-prefix-adaptive-chart.json').read_text());cfg=json.loads(a.profile.read_text());port=json.loads(a.port.read_text());Flow,_=ad.build_classes(chart);f=Flow(cfg,port,a.modes,.001,max(128,16*a.modes),2,warp_q=.001)
 rows=[]
 for j in range(a.modes):
  line=f.backward_line(j);c=np.asarray(line.core,float);row={'mode':2*(j+1),'normalized_core_f':float(c[0]/np.linalg.norm(c)),'normalized_core_g':float(c[1]/np.linalg.norm(c)),'g_over_f':float(c[1]/c[0]),'logscale':float(line.logscale)};rows.append(row)
 out={'scope':__doc__,'profile':cfg,'rows':rows,'seconds':time.time()-start};a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'nearest_zero_g':sorted(rows[1:],key=lambda r:abs(r['normalized_core_g']))[:5],'seconds':out['seconds']}),flush=True)
if __name__=='__main__':main()
