#!/usr/bin/env python3
"""True quarter-cut multipliers uniformly on the exact eta parameter family.

This replays the actual infinite-primitive Fourier proof at r=1/4. It adds
complete H^1 and H^(3/2) multiplier errors through the existing A0/A1/A2
budgets; no root-port bound is transferred to this ordinary physical cut.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_beta_affine import load_definition, provenance
from fourfold_phase_beta_parameter_germ import ParameterGermMixin
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_core_low_coefficients import extend_half
from fourfold_phase_cap_scaled_body import common_cells
from fourfold_phase_cap_energy_interval import sha
from fourfold_phase_cut_interface_fourier import InterfaceTarget, NAMES, geometric_tail, positive_sum


class FamilyInterfaceTarget(InterfaceTarget):
    direction_scalars = ParameterGermMixin.direction_scalars

    def __init__(self, object_path, half_width, nodes, angles, *radii):
        half_width=Fraction(half_width)
        if not half_width>0:
            raise ValueError('a positive exact family half-width is required')
        super().__init__(object_path,nodes,angles,*radii)
        definition,_,direction,center=load_definition(object_path)
        ParameterGermMixin.initialize_parameter(
            self,object_path,half_width,definition,direction,center)
        self.centered_parameter_ball=exact_arb(-half_width).union(exact_arb(half_width))

    def scalars(self,center,direction):
        central=super().scalars(center,direction)
        if not hasattr(self,'centered_parameter_ball'):
            return central
        changes=self.direction_scalars(center,direction)
        result=[]
        for value,change in zip(central,changes):
            if isinstance(value,np.ndarray):
                row=np.empty(value.shape,object)
                for index in np.ndindex(value.shape):
                    row[index]=value[index]+self.centered_parameter_ball*change[index]
                result.append(row)
            else:
                result.append(value+self.centered_parameter_ball*change)
        return tuple(result)


def family_provenance(target,path):
    identity=provenance(target,path)
    identity.update(
        exact_center_parameter=str(target.parameter_center),
        exact_parameter_half_width=str(target.parameter_half_width),
        exact_parameter_interval=[str(x) for x in target.parameter_interval],
        uniform_in_the_entire_real_parameter_interval=True,
        parameter_arithmetic='Complete central and direction scalar germs first, then the single centered increment p in [-eta,eta].',
        exact_delta_fraction_scope='This names the center; all proved multipliers cover exact_parameter_interval.')
    return identity


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    ap.add_argument('--primitive-nodes',type=int,default=512)
    ap.add_argument('--angles',type=int,default=2048)
    ap.add_argument('--keep',type=int,default=512)
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--normalized-strip',type=Fraction,default=Fraction(1,16))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec,ctx.cap=args.bits,4
    if not 0<args.keep<args.angles//2:raise ValueError('the retained Fourier modes must exclude Nyquist')
    wall,cpu=time.monotonic(),time.process_time()
    target=FamilyInterfaceTarget(args.object,args.half_width,args.primitive_nodes,args.angles,arb('.003'),arb('.0025'),arb('.32'))
    cuts=common_cells(target);r=Fraction(1,4);k=bisect_right(cuts,r)-1
    target.set_cell(cuts[k],cuts[k+1]);radial=acb(exact_arb(r))
    coefficient,_,_,errors,real=target.complete_fast_data(radial)
    if not real:raise ValueError('the interface radius must be mathematically real')
    values=target.values(radial,coefficient,errors)
    strip=exact_arb(args.normalized_strip)
    if not strip>0:raise ValueError('a positive true angular strip is required')
    moduli,domain=target.moduli(radial,coefficient,errors,strip)
    centers=np.empty((len(NAMES),args.keep+1),float)
    fees=np.empty_like(centers);records={}
    for index,name in enumerate(NAMES):
        full=extend_half(values[name],1)
        transformed=target.fast_fourier.fft(full)/args.angles
        if np.any(transformed.imag.lo>0) or np.any(transformed.imag.hi<0):
            raise ValueError('a real even interface function lost its real Fourier coefficients')
        for lag in range(args.keep+1):
            alias=moduli[name]*((-(args.angles-lag)*strip).exp()
                +(-(args.angles+lag)*strip).exp())/(1-(-args.angles*strip).exp())
            true=transformed[lag].to_acb().real+arb(0,alias.upper())
            chosen=float(true.mid())
            radius=abs(true-arb(chosen)).upper()
            saved_fee=float(np.nextafter(float(radius),np.inf)) if radius else 0.
            if not np.isfinite(saved_fee):raise ValueError('nonfinite saved Fourier coefficient error')
            centers[index,lag],fees[index,lag]=chosen,saved_fee
        tails=[geometric_tail(args.keep,strip,j,moduli[name]) for j in range(3)]
        selected=[positive_sum(fees[index],j) for j in range(3)]
        error=[(a+b).upper() for a,b in zip(selected,tails)]
        finite=[positive_sum(np.abs(centers[index]),j) for j in range(3)]
        half_finite=arb(abs(float(centers[index,0])))
        for lag in range(1,args.keep+1):
            half_finite+=2*abs(arb(float(centers[index,lag])))*arb(1+4*lag).sqrt()
        half_error=(error[0]+(error[0]*error[1]).sqrt()).upper()
        strong_errors = {
            'H0': error[0],
            'Hhalf': half_error,
            'H1': (error[0]+error[1]).upper(),
            'Hthreehalf': ((error[0]+error[1])*(error[0]+2*error[1]+error[2])).sqrt().upper(),
            'H2': (error[0]+2*error[1]+error[2]).upper()}
        strong_finite = {}
        for label,power in (('H0',arb(0)),('Hhalf',arb(1)/2),('H1',arb(1)),
                            ('Hthreehalf',arb(3)/2),('H2',arb(2))):
            value=arb(abs(float(centers[index,0])))
            for lag in range(1,args.keep+1):
                value+=2*abs(arb(float(centers[index,lag])))*arb(1+4*lag)**power
            strong_finite[label]=value.upper()
        discarded=[]
        for cutoff in (8,16,32,64,128,256):
            if cutoff>args.keep:continue
            norms=[]
            for j in (0,1,2):
                value=tails[j]
                for lag in range(cutoff+1,args.keep+1):
                    value+=2*(abs(arb(float(centers[index,lag])))+arb(float(fees[index,lag])))*(4*lag)**j
                norms.append(value.upper())
            discarded.append(dict(physical_index_cutoff=cutoff,
                complete_true_discarded_A0=ball_record(norms[0]),
                complete_true_discarded_A1=ball_record(norms[1]),
                complete_true_discarded_Hhalf_multiplier_bound=ball_record((norms[0]+(norms[0]*norms[1]).sqrt()).upper()),
                complete_true_discarded_A2=ball_record(norms[2]),
                complete_true_discarded_H1_multiplier_bound=ball_record((norms[0]+norms[1]).upper()),
                complete_true_discarded_Hthreehalf_multiplier_bound=ball_record(((norms[0]+norms[1])*(norms[0]+2*norms[1]+norms[2])).sqrt().upper())))
        records[name]=dict(whole_true_complex_strip_modulus=ball_record(moduli[name]),
            selected_coefficient_error_A012=list(map(ball_record,selected)),
            complete_unretained_tail_A012=list(map(ball_record,tails)),
            complete_polynomial_error_A012=list(map(ball_record,error)),
            finite_selected_polynomial_A012=list(map(ball_record,finite)),
            Hhalf_multiplier_error=ball_record(half_error),
            true_Hhalf_multiplier_norm_upper=ball_record((half_finite+half_error).upper()),
            complete_multiplier_errors={key:ball_record(value) for key,value in strong_errors.items()},
            complete_true_multiplier_norms={key:ball_record((strong_finite[key]+value).upper())
                                            for key,value in strong_errors.items()},
            discarded_true_multiplier=discarded)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    arrays=args.out.with_suffix('.npz')
    np.savez_compressed(arrays,positive_fourier_coefficients=centers,
        positive_coefficient_error_radii=fees,physical_indices=np.arange(args.keep+1))
    identity=family_provenance(target,args.object)
    identity.pop('source_sha256');identity.pop('dependency_sha256')
    result=dict(kind='uniform_eta_complete_physical_quarter_cut_interface_multipliers',complete=True,
        **identity,source_sha256=sha(__file__),
        exact_physical_radius='1/4',selected_common_scalar_span=list(map(str,target.cell)),
        exact_function_names=list(NAMES),quarter_primitive_nodes=args.primitive_nodes,
        angular_nodes=args.angles,retained_positive_indices=args.keep,bits=args.bits,
        normalized_angular_strip=str(args.normalized_strip),domain=domain,
        true_infinite_primitive_error_budgets=list(map(ball_record,errors)),
        functions=records,
        exact_finite_definition='c0+2*sum_{k=1..K} c_k*cos(4*k*theta), with saved binary64 c_k interpreted exactly',
        coefficient_contract='The true positive Fourier coefficient is real and lies in c_k+[-r_k,r_k] with saved binary64 r_k exact; negative coefficients are equal by exact real-even angular symmetry.',
        arrays=dict(path=str(arrays),sha256=sha(arrays),bytes=arrays.stat().st_size),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_affine.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_beta_parameter_germ.py','fourfold_phase_cut_interface_fourier.py',
            'fourfold_phase_core_low_coefficients.py','fourfold_phase_actual_positive_cap.py',
            'fourfold_phase_cap_scaled_body.py')},
        CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall,
        scope=['Actual r=1/4 physical Fourier interface for every parameter in the exact stated eta interval. A new whole-family complex angular domain is proved at this cut.',
               'All selected coefficient arithmetic, infinite primitive errors, complete DFT aliases and unretained Fourier tails are paid.',
               'These multipliers do not certify the radial two-channel propagation, omitted-mode Schur feedback, or a nonlinear solution.'])
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(complete=True,domain=domain,errors={
        name:records[name]['complete_polynomial_error_A012'][0]['ball'] for name in NAMES},
        CPU_seconds=result['CPU_seconds'],wall_seconds=result['wall_seconds']),indent=2),flush=True)


if __name__=='__main__':main()
