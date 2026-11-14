#!/usr/bin/env python3
"""Complete true radial target coefficients without an approximate PDE solution.

Every box lies in one actual scalar germ. All original Fourier primitive
tails and the whole real affine parameter interval are paid by the provider.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import math
import time
from flint import ctx
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_phase_two_jet_newton_source import common_cells, load_definition, record, save, sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--right',type=Fraction,default=Fraction(1,5))
    ap.add_argument('--max-step',type=Fraction,default=Fraction(1,2000))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    ap.add_argument('--nodes',type=int,default=512)
    ap.add_argument('--angles',type=int,default=4096)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or a.right<=0 or a.max_step<=0:
        raise ValueError('new output and positive exact radial settings required')
    ctx.prec=a.bits;ctx.cap=4;started=time.monotonic()
    target=CodazziCoefficientTarget(a.object,a.half_width,a.nodes,a.angles)
    definition,_,_,center=load_definition(a.object)
    all_cuts=common_cells(target)
    if a.right>all_cuts[-1]:raise ValueError('target endpoint leaves actual scalar germ domain')
    cuts=[Fraction(0),*[x for x in all_cuts if 0<x<a.right],a.right]
    deps=('fourfold_phase_newton_source_centered.py','fourfold_phase_two_jet_newton_source.py',
          'fourfold_phase_metric_defect.py','fourfold_phase_beta_bulk_interval.py',
          'fourfold_phase_beta_bulk_box.py')
    out=dict(kind='actual_complete_fixed_target_Codazzi_coefficient_cover',
        complete=False,failure=None,continuation_certified=False,closed_surface_complete=False,
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,
        original_target_unchanged=True,exact_requested_interval=['0',str(a.right)],
        exact_center_parameter=str(center),parameter_half_width=str(a.half_width),
        object_sha256=sha(a.object),origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],source_sha256=sha(__file__),
        coefficient_provider_sha256=sha(Path(__file__).with_name('fourfold_phase_codazzi_coefficients.py')),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in deps},
        bits=a.bits,primitive_nodes=a.nodes,angular_grid=a.angles,max_step=str(a.max_step),
        no_PDE_candidate_used=True,rows=[],covered_interval=['0','0'])
    endpoint=Fraction(0)
    try:
        for cell,(l,r) in enumerate(zip(cuts,cuts[1:])):
            count=math.ceil((r-l)/a.max_step)
            for part in range(count):
                left=l+(r-l)*part/count;right=l+(r-l)*(part+1)/count
                if left!=endpoint:raise ValueError('noncontiguous exact target cover')
                coefficients=target.coefficients(left,right)
                out['rows'].append(dict(cell=cell,part=part,interval=[str(left),str(right)],
                    actual_scalar_germ=list(map(str,target.cell)),
                    strict_negative_target=bool(coefficients['K']<0),
                    true_target_coefficients={key:record(value) for key,value in coefficients.items()}))
                endpoint=right;out['covered_interval']=['0',str(endpoint)]
                out['wall_seconds']=time.monotonic()-started
                save(a.out,out)
                print(dict(row=len(out['rows']),right=str(right),K=coefficients['K'].str(10),
                    seconds=out['wall_seconds']),flush=True)
        if endpoint!=a.right:raise ValueError('requested endpoint not covered')
        out['complete']=True
    except Exception as exc:
        out['failure']=repr(exc)
    out['wall_seconds']=time.monotonic()-started;save(a.out,out)
    print(dict(complete=out['complete'],failure=out['failure'],rows=len(out['rows']),
        seconds=out['wall_seconds']),flush=True)


if __name__=='__main__':main()
