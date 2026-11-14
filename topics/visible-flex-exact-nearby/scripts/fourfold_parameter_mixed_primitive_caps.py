#!/usr/bin/env python3
"""Actual cap budgets with an independent primitive grid on unsampled germs.

Every model still encloses the same infinite target and pays its own full
primitive error. Only the main germ is sampled for density reconstruction.
This diagnostic keeps the main Q fixed and reconstructs the complete center
and uniform cap ledgers at each requested neighboring-germ Q.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import time
import traceback
from flint import ctx

from fourfold_phase_parameter_time_circle import ParameterTimeCircleField
from fourfold_phase_uniform_parameter_time_circle import UniformParameterTimeCircleField
from fourfold_phase_parameter_cap_uniform import complete_parameter_caps
from fourfold_complete_reference_segment import CompleteReferenceSegment
from fourfold_retarget_reference_jets import RetargetReference
from fourfold_phase_beta_affine import sha
from fourfold_saved_circle_field_multidomain_budget import read
from fourfold_forward_density_pipeline_Q1024_v3 import save


def main():
    p=argparse.ArgumentParser(description=__doc__)
    base=Path('data/phase_ring_continuation')
    p.add_argument('--descriptor',type=Path,default=base/'step5_retargeted_reference/descriptor.json')
    p.add_argument('--domain',type=Path,required=True)
    p.add_argument('--reference-certificate',type=Path,required=True)
    p.add_argument('--local-root-jets',type=Path,default=base/'type_fixed_step02_d5_step5_local_parameter_root_jets_h1e14.json')
    p.add_argument('--wide-root-jets',type=Path,default=base/'type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json')
    p.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    p.add_argument('--main-nodes',type=int,default=384)
    p.add_argument('--cap-nodes',default='128,384')
    p.add_argument('--root-nodes',type=int,default=1024)
    p.add_argument('--bits',type=int,default=256)
    p.add_argument('--radial-degree',type=int,default=40)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec,ctx.cap=args.bits,7
    started,cpu=time.monotonic(),time.process_time()
    doc,old=read(args.domain),read(args.reference_certificate)
    if not old.get('complete') or not old.get('complete_continuous_true_density_proved'):
        raise ValueError('a complete actual g0 reference certificate is required')
    if old['domain_sha256']!=sha(args.domain):
        raise ValueError('the diagnostic changes the actual source domain')
    sl,sr=map(Fraction,doc['normalized_subspan'])
    ref=CompleteReferenceSegment(RetargetReference(args.descriptor),doc['leg'],doc['segment'],sl,sr)
    if ref.identity!=old['identity']['reference']:
        raise ValueError('the diagnostic changes the exact finite reference')
    image=old['real_reference_gate']['image'];q=old['real_reference_gate']['q']
    main_index=int(old['true_crossing_caps']['main_germ_index'])
    if not 0<=main_index<len(doc['germs']):raise ValueError('invalid saved actual main germ')
    result=dict(kind='actual_mixed_primitive_grid_parameter_cap_budgets',complete=False,
        source_sha256=sha(__file__),descriptor_sha256=sha(args.descriptor),
        domain_path=str(args.domain),domain_sha256=sha(args.domain),
        reference_certificate_path=str(args.reference_certificate),reference_certificate_sha256=sha(args.reference_certificate),
        main_germ_index=main_index,main_primitive_nodes=args.main_nodes,root_nodes=args.root_nodes,
        neighboring_germs_never_sampled=True,actual_density_completion_claimed=False,
        exact_parameter_half_width=str(args.half_width),bits=args.bits,cases=[],
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_parameter_time_circle.py','fourfold_phase_uniform_parameter_time_circle.py',
            'fourfold_phase_parameter_cap_uniform.py','fourfold_phase_parameter_cap_budget.py',
            'fourfold_complete_reference_segment.py')})
    save(args.out,result)
    before=time.process_time()
    common=dict(root_nodes=args.root_nodes,radial_degree=args.radial_degree)
    center_main=ParameterTimeCircleField(args.descriptor,args.domain,args.local_root_jets,
        nodes=args.main_nodes,germ=main_index,**common)
    uniform_main=UniformParameterTimeCircleField(args.descriptor,args.domain,args.local_root_jets,
        args.wide_root_jets,half_width=args.half_width,nodes=args.main_nodes,germ=main_index,
        central=center_main,**common)
    result['shared_main_initialization_cpu_seconds']=time.process_time()-before
    for nodes in map(int,args.cap_nodes.split(',')):
        case=dict(neighbor_primitive_nodes=nodes,complete=False,models=[])
        tick=time.process_time()
        try:
            central=[None]*len(doc['germs']);uniform=[None]*len(doc['germs'])
            central[main_index],uniform[main_index]=center_main,uniform_main
            for j in range(len(central)):
                if j==main_index:continue
                start=time.process_time()
                central[j]=ParameterTimeCircleField(args.descriptor,args.domain,args.local_root_jets,
                    nodes=nodes,germ=j,**common)
                split=time.process_time()
                uniform[j]=UniformParameterTimeCircleField(args.descriptor,args.domain,args.local_root_jets,
                    args.wide_root_jets,half_width=args.half_width,nodes=nodes,germ=j,
                    central=central[j],**common)
                case['models'].append(dict(germ=j,center_cpu_seconds=split-start,
                    uniform_extra_cpu_seconds=time.process_time()-split))
            center_cap=complete_parameter_caps(central,ref,image,q)
            uniform_cap=complete_parameter_caps(uniform,ref,image,q)
            if center_cap['main_germ_index']!=main_index or uniform_cap['main_germ_index']!=main_index:
                raise ValueError('the actual parameter cap geometry selects a different main germ')
            case.update(complete=True,center_cap=center_cap,uniform_cap=uniform_cap,
                        parameter_root_tube_and_actual_ordinary_crossings_recomputed=True)
        except Exception as exc:
            case.update(failure=type(exc).__name__+': '+str(exc),traceback=traceback.format_exc())
        case['additional_neighbor_and_caps_cpu_seconds']=time.process_time()-tick
        result['cases'].append(case);save(args.out,result)
        print(dict(nodes=nodes,complete=case['complete'],failure=case.get('failure'),
                   cpu=case['additional_neighbor_and_caps_cpu_seconds']),flush=True)
    result.update(complete=all(c['complete'] for c in result['cases']),
                  cpu_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-started,
                  sampling_and_full_density_not_performed=True)
    save(args.out,result)
    return 0 if result['complete'] else 2


if __name__=='__main__':raise SystemExit(main())
