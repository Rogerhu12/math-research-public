#!/usr/bin/env python3
"""Same-candidate finite-Horner source probe on one existing true panel.

No background quadrature, ODE, or change of five true moments is made.
Subpanels/points retain the original full-panel H/moment and geometric
enclosures, so they are explicitly not claimed to be sharp point values.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import resource
import time

from flint import arb,ctx
from closure_real_head_source_enclosure import exact_q
from closure_split_joint_io_v2 import read,read_field,iter_array,digest
from closure_shared_slope_cut_interface import ball,record
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_candidate_domain import endpoint_candidate,nonnegative_integral
from tail_outer_weighted_compatible import make_weighted_candidate,cell_source_coordinate,weighted_panel_fields as original_fields
from tail_outer_centered_quartic_fields_v2 import weighted_panel_fields as centered_fields,finite,intersection,rational_identity_checks
from tail_outer_full_mean_residual_bounds import full_mean_residual_bounds
from closure_outer_candidate_source_record import signed_source_bounds


EXPECTED={
 'tail_outer_centered_quartic_fields_v2.py':'671f6b0c02b3a59dcac79129dc8e73cff4baebe9ec477ee5509e3425f9fb086b',
 'tail_outer_weighted_compatible.py':'03c88b010447c78e4fb6bb26f0d3704fafd23510d16cc00084f315daa07f3d1b',
 'tail_outer_candidate_domain.py':'17d6b7d85be80f8f40b3eec411ae49a73c51c6b624d030df57b94202a7d08690',
 'closure_outer_candidate_source_record.py':'544bab2538a33ac32c546d980e08dc0d95fea383d5f25aed894fea9ce27c3d34',
 'tail_outer_full_mean_residual_bounds.py':'16f9d2d5c2e858686aff9d332df4cc565606481ab45a46d6a9080db29317c8af'}


def main():
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('cell-manifest','source-summary','ports','response','ready','out'):
  p.add_argument('--'+key,type=Path,required=True)
 p.add_argument('--segment',type=int,default=3);p.add_argument('--panel',type=int,default=0)
 p.add_argument('--rss-kib',type=int,default=40960)
 a=p.parse_args();ctx.prec=192;began=time.monotonic()
 if a.out.exists():raise FileExistsError('Use a fresh same-candidate probe')
 for name,sha in EXPECTED.items():
  if digest(Path(__file__).with_name(name))!=sha:raise ValueError('A frozen mathematical helper changed: '+name)
 identities=rational_identity_checks()
 paths=[getattr(a,k) for k in ('cell_manifest','source_summary','ports','response','ready')]
 hashes={str(path):digest(path) for path in paths}
 material=read(a.cell_manifest);summary=read(a.source_summary);ports=read(a.ports)
 if not all(material['checks'].values()) or not summary['all_gates']:raise ValueError('The original complete true packages are required')
 n=material['cell']
 if n!=summary['cell'] or n not in (10,11):raise ValueError('Keep the original small-domain two-cell candidate')
 for path in (a.cell_manifest,a.ports,a.response,a.ready):
  if summary['input_hashes'].get(str(path))!=hashes[str(path)]:raise ValueError('The source recorder used another actual candidate')
 meta=material['original_metadata'];tau=Fraction(1,64)
 cp=read_field(a.response,'response')['checkpoint']
 ready=read(a.ready);h=SourceValues(ready);h.params=ready['rationalDeepModel']['physicalParameters'];cell=OuterCell(h,n)
 prows={r['physical_node']:r for r in ports['rows']}
 left,unused=endpoint_candidate(cell,'inner',n+1,cp['rawStates'][n+1],prows[n+1],ball(meta['inner_radius']),tau,8)
 right,unused=endpoint_candidate(cell,'outer',n,cp['rawStates'][n],prows[n],ball(meta['outer_radius']),tau,8)
 moments={k:nonnegative_integral(v,strict=True) for k,v in meta['total_positive_moments'].items()}
 candidate=make_weighted_candidate(left,right,moments);modes=sorted(left['H'])
 if modes!=list(range(2,41,2)):raise ValueError('All20 original candidate modes are required')
 weights={m:((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}
 mg=next(g for g in material['groups'] if g['source_segment']==a.segment)
 sg=next(g for g in summary['groups'] if g['segment']==a.segment)
 for group in (mg,sg):
  if digest(Path(group['path']))!=group['sha256']:raise ValueError('The original complete panel group changed')
  hashes[group['path']]=group['sha256']
 g=next(r for i,r in enumerate(iter_array(mg['path'],'panels')) if i==a.panel)
 old=next(r for r in iter_array(sg['path'],'panels') if r['panel']==a.panel)
 if (g['x_left'],g['x_right'])!=(old['x_left'],old['x_right']):raise ValueError('The source and real material positions differ')
 prefix={k:nonnegative_integral(v) for k,v in g['prefix_moments'].items()}
 suffix={k:nonnegative_integral(v) for k,v in g['suffix_moments'].items()}
 xl,xr=Fraction(g['x_left']),Fraction(g['x_right']);xm=(xl+xr)/2
 cases=[('old_full',xl,xr,False),('centered_full',xl,xr,True),
        ('centered_left_half',xl,xm,True),('centered_right_half',xm,xr,True),
        ('centered_midpoint',xm,xm,True)]
 rows=[]
 for name,lo,hi,new in cases:
  if name=='old_full':u,ux=ball(g['u']),ball(g['u_x'])
  else:
   x=exact_q(lo).union(exact_q(hi))
   u,ux=cell_source_coordinate([s['length'] for s in cell.segments],a.segment,x)
   u,ux=intersection(u,ball(g['u'])),intersection(ux,ball(g['u_x']))
  H,K,Kx=(centered_fields if new else original_fields)(candidate,u=u,u_x=ux,prefix_moments=prefix,suffix_moments=suffix)
  r,w,rx,ell=[ball(g[k]) for k in ('radius','w','radius_x','log_w_x')]
  norms={key:arb(0) for key in ('P_tau','K_tau','Kx_tau','nonmean_L_tau')}
  for m in modes:
   hc,k,kx=[finite(2*f[m].real) for f in (H,K,Kx)]
   norms['P_tau']+=weights[m]*abs(m*hc/(r*w)).upper()
   norms['K_tau']+=weights[m]*abs(k).upper()
   norms['Kx_tau']+=weights[m]*abs(kx).upper()
   norms['nonmean_L_tau']+=weights[m]*abs(k-(1+w*w)*m*m*hc/(r*w)).upper()
  norms={k:finite(v).upper() for k,v in norms.items()}
  if not norms['P_tau']+norms['K_tau']<arb(1)/64:raise ArithmeticError('The complete mean work domain failed')
  full=full_mean_residual_bounds(H,K,Kx,modes=modes,weights=weights,radius=r,radius_x=rx,w=w,log_w_x=ell,norms=norms)
  signed=signed_source_bounds(H,K,full,modes=modes,radius=r,radius_x=rx,w=w,log_w_x=ell,norms=norms,tau=tau,selected=[2,4])
  if name=='old_full' and signed['selected_cosine_sources']!=old['selected_cosine_sources']:raise ArithmeticError('The original source mathematics was not reproduced bitwise')
  rows.append(dict(case=name,x_left=str(lo),x_right=str(hi),
      same_original_candidate=True,original_full_panel_geometry_and_moment_caps_retained=True,
      complete_mean_domain=True,nonmean_slope_2=record(2*K[2].real),
      nonmean_height_2=record(2*H[2].real),relative_sine_slope_2=record(-4*H[2].real/(r*w)),
      complete_mean_abs=record(full['complete_mean_abs']),**signed))
  if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('The same-panel source probe exceeded its owned RSS guard')
 gates=dict(original_N2_N4_reproduced_bitwise=True,exact_same_true_five_moments_and_endpoint_jets=True,
  all20_candidate_modes_and_complete_mean_retained=True,finite_centered_Horner_and_finite_intersections=True,
  no_new_source_integrals_or_ODE=True,subpanel_point_scope_does_not_claim_tight_geometry_or_height=True)
 out=dict(status='Actual same-candidate source-range probe with finite quartic evaluation',
   cell=n,segment=a.segment,panel=a.panel,gates=gates,all_gates=True,identity_checks=identities,
   original_bubble_coefficient_2=record(candidate['bubble_coefficient'][2]),
   original_positive_bubble_integral=record(candidate['total_moments']['b']),
   rows=rows,input_hashes=hashes,source_hashes=EXPECTED,source_sha256=digest(__file__),
   elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 a.out.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(output=str(a.out),all_gates=True,
  rows=[dict(case=r['case'],N4=str(ball(next(v for v in r['selected_cosine_sources'] if v['mode']==4)['complete_source_cosine']))) for r in rows],
  peak_RSS_KiB=out['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
