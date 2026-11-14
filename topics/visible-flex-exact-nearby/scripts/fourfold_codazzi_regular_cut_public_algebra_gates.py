#!/usr/bin/env python3
"""Public Actions algebra gates for the complete local projector validator.

These explicit synthetic objects verify matrix/sign/mean conventions.
They are not actual candidate cells or a substitute for their verification.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,ctx
from fourfold_codazzi_regular_cut_interval_model import Field,DirectedFFT,physical_reference,raw_generator
from fourfold_codazzi_regular_cut_projector_validator import validate_cell,sha,save


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('preserve the original public algebra gate outcome')
    ctx.prec=256;ctx.cap=6;started=time.monotonic()
    document=dict(kind='public_complete_193_state_projector_algebra_gates_v1',complete=False,failure=None,gates=[],
        source_sha256=sha(__file__),actual_candidate_cells_validated=0,
        actual_continuous_inverse_proved=False)
    def gate(name,test):
        document['gates'].append(dict(name=name,passed=bool(test)))
        if not test:raise ValueError('public full-state algebra gate failed: '+name)
    try:
        fft=DirectedFFT()
        u,V,_=physical_reference(np.zeros((4,65)),Fraction(0),Fraction(0),Fraction(1,100),Fraction(1),[Fraction(0)]*65,fft)
        scalar={key:Field.scalar([value],fft) for key,value in dict(beta=0,gamma=1,K=-1,s=-1).items()}
        matrices,error,_=raw_generator(u,V+scalar['s'],scalar);all_entries=True
        for k,matrix in enumerate(matrices):
            for i in range(193):
                for j in range(193):
                    expected=0
                    if k==0 and i<96 and j==96+i+1:expected=-4*(i+1)
                    if k==0 and i>96 and j==i-97:expected=4*(i-96)
                    all_entries=all_entries and matrix[i,j].contains(arb(expected))
        gate('all193 squared skew reference entries and the independent mean',all_entries)
        gate('complete unaliased reference rounding budget',error<arb('1e-9'))
        Q=np.zeros((193,96));A=arb_mat(193,193)
        for j in range(1,97):
            Q[j-1,j-1]=2**-.5;Q[96+j,j-1]=-2**-.5
            A[j-1,96+j]=A[96+j,j-1]=4*j
        result=validate_cell([A,arb_mat(193,193),arb_mat(193,193),arb_mat(193,193)],arb(0),Q,Q,Fraction(0),Fraction(1,1000),24)
        gate('full synthetic continuous Gram lower',arb(result['whole_polynomial_smallest_singular_lower']['lower'])>arb('.999999999'))
        gate('complete signed stable forward bound',arb(result['complete_forward_signed_rate_mu']['upper'])<arb('-3.9999999'))
        gate('complete complementary bound includes the neutral mean',arb(result['complete_backward_signed_rate_nu']['upper'])<arb('1e-7'))
        gate('complete exact saved-anchor projector interface',arb(result['complete_left_interface_projector_jump']['upper'])<arb('1e-12'))
        # A genuine principal-angle interface requires sec/tan, not 1/sin.
        cosine=arb(3)/5;sine=arb(4)/5;pplus=1/cosine;qminus=sine/cosine
        gate('actual angle interface keeps both secant and tangent fees',
             (cosine*pplus-sine*arb(0)).contains(arb(1))
             and (sine*pplus+cosine*arb(0)-qminus).contains(arb(0))
             and pplus>1 and qminus>sine)
        document.update(complete=True,synthetic_hyperbolic_complete_local_certificate=result,
            numerical_results_must_come_from_this_public_run=True)
    except BaseException as error:
        document['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:
        document['seconds']=time.monotonic()-started;save(a.out,document)
    print(dict(complete=True,public_synthetic_gates=len(document['gates']),actual_candidate_cells=0),flush=True)


if __name__=='__main__':main()
