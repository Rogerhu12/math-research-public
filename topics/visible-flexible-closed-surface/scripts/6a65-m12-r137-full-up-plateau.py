#!/usr/bin/env python3
"""Exact-form R137 on the WHOLE up affine plateau of the original M12 g.

Reuse R220 interval arithmetic without modifying its frozen input or script.
The new raw inlet is the rational native cross-section at Tu*eps. Its exact
arc normalization targets the original PHYSICAL radius at sigma=Tu*eps.
Old-map comparisons therefore evaluate native s=lambda*sigma, explicitly.
The adjoining nonflat ramps and complete old Cartesian ports remain unpaid.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np

HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out


ad=module('full_up_adapter',HERE/'6a65-m12-r137-fixed-metric-adapter.py')
cert=module('full_up_certifier',HERE/'6a65-m12-r137-continuous-domain.py')
I=cert.I


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--angles',type=int,default=1024);ap.add_argument('--cells',type=int,default=8192)
    ap.add_argument('--panels',type=int,default=256);ap.add_argument('--gauss',type=int,default=24)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh output required')
    start=time.monotonic()
    metapath=HERE.parent/'notes'/ad.base.META_NAME
    src=ad.base.Source(args.data,metapath);cfg=src.meta['frozen_profile']
    delta,v,eps=[Q(float(cfg[k])) for k in ('delta','vu','ramp')]
    if cfg['direction']!='outward' or cfg['cycles']!=1:raise ValueError('Unexpected profile')
    Tu=delta/(v*(1-eps));sigma0=Tu*eps;length=Tu*(1-2*eps)
    intercept=1-delta*eps/(2*(1-eps));f0=intercept+v*sigma0
    bridgepath=HERE.parent/'notes/2026-11-09-db6f-root-exact-bridge-m12.json'
    bridge=json.loads(bridgepath.read_text());rescale=bridge['arclength_rescale']
    lam=(Q(rescale['lo'])+Q(rescale['hi']))/2
    source_cell,c=ad.exact_section(args.data,sigma0)
    raw=ad.NativeCurve(c,args.panels,args.gauss);curve=ad.FixedRadiusCurve(raw,float(f0))
    u=2*np.pi*np.arange(args.angles)/args.angles
    left=ad.supplier.at_material(float(f0),float(v),0.,u,lambda t:curve.inlet(t,float(v)))
    right=ad.supplier.at_material(float(f0),float(v),float(length),u,lambda t:curve.inlet(t,float(v)))
    oldleft=ad.old_packet(src,ad.base.ld(lam*sigma0),u,ad.base.ld(lam))
    oldright=ad.old_packet(src,ad.base.ld(lam*(sigma0+length)),u,ad.base.ld(lam))
    numerical={'angles':args.angles,'arc_gauss_panels':args.panels,'arc_gauss_order':args.gauss,
       'raw_arc_radius':raw.a,'normalization':curve.normalization,
       'left_metric_sampled':float(np.max(left['metric'])),'right_metric_sampled':float(np.max(right['metric'])),
       'endpoint_curvature_sampled':float(max(np.max(left['actual_curvature']),np.max(right['actual_curvature']))),
       'minimum_D_sampled':float(min(float(f0),np.min(right['D']))),
       'minimum_Ut_sampled':float(np.min(right['U_t'])),
       'left_old_full_twojet_difference':{key:ad.normmax(left[key]-oldleft[key]) for key in oldleft},
       'right_old_full_twojet_difference':{key:ad.normmax(right[key]-oldright[key]) for key in oldright}}
    np.savez_compressed(str(args.out)+'.ports.npz',u=u,**{'left_'+key:left[key] for key in oldleft},
                        **{'right_'+key:right[key] for key in oldright})
    cells,arc,quadrature=cert.curve_cells(c,args.cells)
    center=[I(0),I(0),I(c[-1])];bounds={};rows=hashlib.sha256()
    for j,data in enumerate(cells):
        try:g=cert.geometry(data,arc,I(f0),I(v),I(length),center)
        except ArithmeticError as exc:raise ArithmeticError(f'Whole plateau angular interval {j}: {exc}') from exc
        for key,value in g.items():bounds[key]=value if key not in bounds else cert.hull(bounds[key],value)
        rows.update(json.dumps({key:[value.lo,value.hi] for key,value in sorted(g.items())},sort_keys=True).encode()+b'\n')
    kr=I.raw(bounds['ratio'].absupper(),bounds['ratio'].absupper())
    ruling_length=cert.upper_i(I(length)*(1+kr.square()).sqrt())
    lambda_lower=cert.lower_i(bounds['nonzero_principal_curvature'])
    M=(len(c)-2)//3;raw_gap=2*sum((c[2*M+j] for j in range(1,M+1,2)),Q(0))
    height_gap=I(raw_gap)*I(f0)/arc
    if height_gap.lo<=0:raise ArithmeticError('Noncircular height witness not proved')
    out={'schema':'6a65-M12-whole-up-plateau-exact-form-continuous-domain-v1',
       'script_sha256':ad.sha(__file__),'data_sha256':ad.base.DATA_SHA,'geometry_sha256':ad.sha(metapath),
       'exact_bridge_sha256':ad.sha(bridgepath),
       'dependencies':{name:ad.sha(HERE/name) for name in ('6a65-m12-r137-fixed-metric-adapter.py','6a65-m12-r137-continuous-domain.py','6a65-geometry-r137-exact-inlet-consumer.py','fd2d_k0_ruling_coast.py')},
       'source_native_cross_section_exact':str(sigma0),'source_cell':int(source_cell),
       'physical_sigma_start_exact':str(sigma0),'physical_sigma_end_exact':str(sigma0+length),
       'physical_length_exact':str(length),'physical_f0_exact':str(f0),'physical_slope_exact':str(v),
       'input_distinction':'Raw gamma taken at native s=Tu*eps; new physical interval starts at sigma=Tu*eps. The old comparison is at native lambda*sigma, not at the raw extraction coordinate.',
       'exact_new_geometry':'Same raw exact rational Fourier and exact arclength normalization as R220, with new whole-plateau entry, length and original physical target radius.',
       'arc_radius_interval':arc.display(),'arc_proof':quadrature,'angular_cells':args.cells,
       'whole_angle_and_radial_bounds':{key:value.display() for key,value in bounds.items()},
       'normalized_height_gap':height_gap.display(),'ruling_length_upper':ruling_length.display(),
       'green_bounds':{'C0':cert.upper_i(ruling_length.square()/(2*lambda_lower)).display(),
                       'ruling_C1':cert.upper_i(ruling_length/lambda_lower).display(),
                       'ruling_C2':cert.upper_i(1/lambda_lower).display()},
       'angular_interval_rows_sha256':rows.hexdigest(),'numerical_ports':numerical,
       'complete_original_affine_plateau_consumed':True,'full_continuous_domain_certified':True,
       'adjoining_nonflat_ramps_consumed':False,'old_cartesian_ports_matched':False,
       'whole_closed_surface_constructed':False,'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,indent=2,allow_nan=False))


if __name__=='__main__':main()
