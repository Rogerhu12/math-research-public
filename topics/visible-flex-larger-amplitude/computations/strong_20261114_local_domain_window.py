#!/usr/bin/env python3
"""Extract the failed physical-s window from an already completed full response.

No new flow, derivative, nonlinear solve, or LP is run. Point-response arrays
retain all 32 modes and 1280 angles. Candidate per-radius minima were saved by
the original complete readout. Control contributions below are evaluated at
the baseline window witness, not claimed to be nonlinear candidate derivatives.
"""
import argparse,gzip,hashlib,io,json
from pathlib import Path
import numpy as np

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--report',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();d=json.loads(a.report.read_text())
 ar=Path(d['point_response_array']['file']);ar=ar if ar.exists() else a.report.parent/ar.name
 if sha(ar)!=d['point_response_array']['sha256']:raise ValueError('Complete point response bytes differ')
 raw=ar.read_bytes();z=np.load(io.BytesIO(gzip.decompress(raw) if ar.suffix=='.gz' else raw),allow_pickle=False)
 base=z['baseline_gap'];derivative=z['derivative_gap'];names=z['controls'].tolist();reference=z['reference_s'];tau=z['material_tau']
 s=np.asarray(d['baseline']['physical_s']);indices=np.flatnonzero((s>=1.59)&(s<=2.01));ii,j=np.unravel_index(np.argmin(base[indices]),base[indices].shape);i=int(indices[ii]);j=int(j)
 baseline=dict(physical_s=float(s[i]),reference_s=float(reference[i]),material_tau=float(tau[i]),psi=float(2*np.pi*j/1280),row=i,angle_index=j,gap=float(base[i,j]),radial_points=len(indices),complete_control_derivatives={name:float(derivative[i,j,k]) for k,name in enumerate(names)})
 candidates=[]
 for c in d['candidates']:
  ss=np.asarray(c['physical_s']);ix=np.flatnonzero((ss>=1.59)&(ss<=2.01));gap=np.asarray(c['gap_min_by_radius']);wi=int(ix[np.argmin(gap[ix])]);weights=np.array([c['physical_steps'][name] for name in names]);predicted=base+derivative@weights
  candidates.append(dict(factor=c['factor'],physical_s=float(ss[wi]),reference_s=float(reference[wi]),material_tau=float(tau[wi]),row=wi,radial_points=len(ix),minimum_actual_warm_gap=float(gap[wi]),ap=float(c['ap'][wi]),q_lat_min=float(c['q_lat_min_by_radius'][wi]),full_angular_minimum_retained=True,nonlinear_solution=False,linear_predicted_minimum_on_baseline_window=float(predicted[indices].min()),linear_global_error_bound_observed=c['linear_gap_error_max'],contributions_at_baseline_window_witness={name:float(derivative[i,j,k]*weights[k]) for k,name in enumerate(names)},predicted_gap_at_baseline_window_witness=float(predicted[i,j])))
 out=dict(scope=__doc__,source_sha256=sha(__file__),input_report=dict(file=str(a.report),sha256=sha(a.report)),input_points=dict(file=str(ar),sha256=sha(ar)),physical_window=[1.59,2.01],baseline=baseline,candidates=candidates,new_nonlinear_solution=False)
 a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
