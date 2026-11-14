#!/usr/bin/env python3
"""Compact provenance and honest sampled-domain summary for outward probes."""
import argparse,hashlib,json
from pathlib import Path

P=Path(__file__).resolve().parent.parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
 pa=argparse.ArgumentParser();pa.add_argument('--out',type=Path,required=True);a=pa.parse_args()
 out=dict(scope='Finite nonlinear strong-core outward/coast/developable-prefix research. No closed surface or continuous rigorous error bound claimed.',source_sha256={p.name:sha(p)for p in (P/'computations').glob('alternative-*.py')},physical_core=dict(A=.38,h='1+A*cos(2*phi)-A/(10*sqrt(2))*cos(4*phi)',material_angle_derivative='rho0 = h + h_phi_phi'),runs=[])
 for p in sorted((P/'notes').glob('alternative-outward-*.json')):
  d=json.loads(p.read_text())
  if 'config' not in d or 'rows' not in d:continue
  r=d['rows'];c=d['config'];row=dict(file=p.name,sha256=sha(p),bytes=p.stat().st_size,config=c,status=d['status'],reached_s=d['reached_s'],radial_sample_count=len(r),whole_sample_max_metric=max(v['metric_sample']for v in r),whole_sample_max_surface_kappa=max(v['surface_kappa_sample']for v in r),whole_sample_min_domain_margin=min(v['margin']for v in r),whole_sample_max_radius=max(v['max_radius']for v in r),whole_sample_max_height=max(v['height_max']for v in r),final=r[-1])
  if 'coefficient_states' in d:row['saved_all_radial_coefficient_states']=True
  if 'source_sha256' in d:row['source_sha256_recorded_in_run']=d['source_sha256']
  out['runs'].append(row)
 out['developable_runs']=[]
 for p in sorted((P/'notes').glob('alternative-flat-m*-width*.json')):
  d=json.loads(p.read_text());out['developable_runs'].append(dict(file=p.name,sha256=sha(p),bytes=p.stat().st_size,config=d['config'],maxima=d['maxima'],minima=d['minima'],seam=d['seam']))
 out['interpretation']=[
  'M24/48/72 with end_s=.8 and no coast use exactly one physical metric and interval; only finite angular spaces/quadratures change.',
  'Coast runs share the same profile: original polynomial through s=.8; a second derivative .48*(1-u)^2 on [.8,.9]; then slope .464. The profile has continuous a second derivative.',
  'M48/72/96/128 coast runs decrease error. The extra M160 run at loose tolerances develops high-mode numerical contamination and is retained as a failed refinement, not hidden or treated as evidence of nonexistence.',
  'The reported entire-domain maxima are maxima over all stored radial/angle samples, not proved continuous suprema.',
  'Ruled maps preserve their actual incoming first jet. Their second-jet mismatch is explicitly reported and still needs a small exact joining construction before calling the finite concatenation C2.',
  'A width .3 developed strip crosses its characteristic Jacobian zero and is rejected; a width .15 remains inside the sampled real domain.',
  'Negative support relative to the original center prevents using the old star-shaped reach argument unchanged; it does not prove lack of embedding or insufficient reach.',
  'No closed cap, full tail match, full-surface Hausdorff lower bound, or full-time reach certificate has yet been constructed.'
 ]
 a.out.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(output=str(a.out),ivp_runs=len(out['runs']),ruled_runs=len(out['developable_runs']),bytes=a.out.stat().st_size)))
if __name__=='__main__':main()
