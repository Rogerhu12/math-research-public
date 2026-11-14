#!/usr/bin/env python3
"""Public numerical gates for signed two-ended Green port conventions.

These explicit systems test the implementation and its actual directed
environment.  They do not replace any original 5970-cell verification.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_signed_positive_Green_ports import (
    exact,record,continuous_port,interface_port,serialize_port,NeedsRefinement,
    apply_backward,apply_forward,whole_segment)


def save(path,document):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(document,indent=2)+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    path.write_bytes(raw)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual public signed Green algebra outcome')
    document=dict(kind='actual_public_signed_positive_Green_port_algebra_gates_v1',
        complete=False,failure=None,gates=[],actual_original_matrix_cells_recomputed=0,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        core_source_sha256=hashlib.sha256(Path(__file__).with_name('fourfold_codazzi_signed_positive_Green_ports.py').read_bytes()).hexdigest())
    def gate(name,ok):
        document['gates'].append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError('actual public positive Green gate failed: '+name)
    try:
        h=Fraction(1,100);r=exact(Fraction(1,100))
        port=continuous_port(arb(-2),arb(-3),arb(0),arb(0),h,r)
        gate('entire_suffix_no_pole_on_uncoupled_negative_rates',port['no_pole_entire_suffix_margin']>0)
        gate('both_negative_rates_remain_signed_in_the_exact_endpoint_port',
            abs(port['rho_left']-r*(-5*exact(h)).exp())<arb('1e-70')
            and abs(port['z_from_z']-(-3*exact(h)).exp())<arb('1e-70')
            and abs(port['p_from_p']-(-2*exact(h)).exp())<arb('1e-70'))
        gate('uncoupled_sources_include_terminal_feedback_and_both_signs',
            abs(port['z_from_f']-r*(-3*exact(h)).exp()*(1-(-2*exact(h)).exp())/2)<arb('1e-70')
            and abs(port['z_from_g']-(1-(-3*exact(h)).exp())/3)<arb('1e-70')
            and abs(port['p_from_f']-(1-(-2*exact(h)).exp())/2)<arb('1e-70')
            and port['p_from_g']<arb('1e-70') and port['p_from_z']<arb('1e-70'))
        coupled=continuous_port(arb(-1),arb(-2),arb(3),exact(Fraction(1,16)),h,exact(Fraction(1,20)))
        z=apply_backward(coupled,arb(5),arb(2),arb(3))
        qleft=coupled['rho_left']*4+z
        pr=apply_forward(coupled,arb(4),arb(5),arb(2),arb(3))
        T,K=coupled['transfer_matrix'],coupled['integrated_transfer_matrix']
        qr=T[1][0]*4+T[1][1]*qleft+K[1][0]*2-K[1][1]*3
        gate('all_four_coupled_constant_source_coefficients_match_the_original_system',
            abs(pr-(T[0][0]*4+T[0][1]*qleft+K[0][0]*2-K[0][1]*3))<arb('1e-65')
            and abs(qr-exact(Fraction(1,20))*pr-5)<arb('1e-65'))
        whole=whole_segment(coupled,arb(4),arb(5),arb(2),arb(3))
        gate('complete_cell_norm_upper_includes_both_actual_endpoints',
            whole['p']>=4 and whole['p']>=pr and whole['q']>=qleft and whole['q']>=qr)
        jump=interface_port(exact(Fraction(4,5)),exact(Fraction(1,10)))
        gate('genuine_secant_tangent_jump_and_both_interface_sources',
            abs(jump['rho_left']-exact(Fraction(43,26)))<arb('1e-70')
            and abs(jump['p_from_p']-exact(Fraction(25,13)))<arb('1e-70')
            and abs(jump['p_from_z']-exact(Fraction(20,13)))<arb('1e-70')
            and abs(jump['z_from_a']-exact(Fraction(5,26)))<arb('1e-70')
            and abs(jump['p_from_a']-exact(Fraction(15,13)))<arb('1e-70')
            and jump['z_from_b']==1)
        refused=False
        try:continuous_port(arb(0),arb(0),arb(10),arb(10),Fraction(1),arb(1))
        except NeedsRefinement:refused=True
        gate('a_failed_full_suffix_gate_cannot_be_promoted_by_endpoint_sampling',refused)
        document.update(complete=True,uncoupled=serialize_port(port),coupled=serialize_port(coupled),
            true_angle_jump=serialize_port(jump),whole_segment={k:record(v) for k,v in whole.items()},
            actual_global_original_Green_inverse_proved=False)
    except BaseException as error:
        document['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:document['seconds']=time.monotonic()-started;save(a.out,document)
    print(json.dumps(dict(complete=True,gates=len(document['gates']),seconds=document['seconds'])),flush=True)


if __name__=='__main__':main()
