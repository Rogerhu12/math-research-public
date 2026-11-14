#!/usr/bin/env python3
"""Complete old-operator root potential density from the seven analytic fields.

Pays C and H=k*rho^(5/2)*(Fcal/mu)-5/16 on a full complex bidisk.
The complete canonical potential is obtained by exact signed-characteristic
identities and second-order root deflation, never by a positive-side chart.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import acb,arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_bulk_box import CBox,zeros,DirectedFFT,arb_box
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_subprincipal_root_parameter_transfer import load_transferred
from fourfold_negative_collar_root_fourier_budget import record


def modulus(z):return arb(float(np.max(z.magnitude_upper()))).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--fields',type=Path,default=Path('notes/2026-11-13-R106-seven-field-full-parameter-transfer.json'))
    ap.add_argument('--rho-radius',type=Fraction,default=Fraction(279,1000000))
    ap.add_argument('--physical-strip',type=Fraction,default=Fraction(11,5000))
    ap.add_argument('--start-strip',type=Fraction,default=Fraction(3,2000))
    ap.add_argument('--radial-angles',type=int,default=128)
    ap.add_argument('--angles',type=int,default=2048)
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise ValueError('new complete root-potential output required')
    ctx.prec=a.bits;tick=time.monotonic()
    d,rows,scale=load_transferred(a.fields)
    R,S,S1=map(exact_arb,(a.rho_radius,a.physical_strip,a.start_strip))
    R0,S0=exact_arb(Fraction(d['working_rho_radius'])),exact_arb(Fraction(d['working_physical_angle_strip']))
    if not 0<R<R0 or not 0<S1<S<S0:raise ValueError('full coefficient margins are missing')
    Nr,Nt=a.radial_angles,a.angles
    if Nr&(Nr-1) or Nt&(Nt-1) or Nr<=d['degree'] or Nt<=2*d['K']:
        raise ValueError('insufficient complete finite evaluation grids')
    # The exact leading relation G(0)+U0(0)/8=0 is respected before
    # interval evaluation; retained finite coefficients keep their true errors.
    rows['Z']=[{k:c+rows['U0'][n][k]/8 for k,c in row.items()}
               for n,row in enumerate(rows['G'])]
    errors={name:stored(d['complete_approximant_errors'][name]['complete_sup_error']).upper()
            for name in ('G','q','Sreg','Ltheta','U0','U1')}
    errors['Z']=errors['G']+errors['U0']/8
    specs=(('Z','Z',0,0),('q','q',0,0),('S_theta','Sreg',0,1),
        ('Lt','Ltheta',0,0),('Lt_theta','Ltheta',0,1),('U','U0',0,0),
        ('U_rho','U0',1,0),('U_theta','U0',0,1),('q_theta','q',0,1),
        ('U1','U1',0,0),('U1_rho','U1',1,0),('U1_theta','U1',0,1))
    names=[sp[0] for sp in specs];data=zeros((Nr,Nt,len(names)))
    movement={name:arb(0) for name in names};tails={}
    radial_gap=arb.pi()/Nr;angular_gap=arb.pi()/Nt
    for j,(name,base,ar,at) in enumerate(specs):
        for n,row in enumerate(rows[base]):
            if n<ar:continue
            radial=(R/scale)**n
            if ar:radial*=n/R
            for k,c in row.items():
                z=c*radial*(-4*int(k)*S).exp()*(acb(0,4*int(k)) if at else 1)
                data[(n-ar)%Nr,int(k)%Nt,j]=CBox.from_acb(z)
                movement[name]+=abs(z).upper()*((n-ar)*radial_gap+abs(int(k))*angular_gap)
        tails[name]=errors[base]/((R0-R) if ar else (S0-S) if at else 1)
    fft=DirectedFFT();data=fft.fft(data,inverse=True)*Nr
    data=fft.fft(data,axis=1,inverse=True)*Nt
    fields={name:data[...,j].pad(arb_box((movement[name]+tails[name]).upper()))
            for j,name in enumerate(names)}
    Z,q,St,Lt,Ltt,U,Ur,Ut,qt,U1,U1r,U1t=(fields[name] for name in names)
    Ulo=arb(float(np.min(U.real.lo))).lower()
    if not Ulo>0:raise ValueError('true complete root U0 is not separated')
    k=1/(2*U);kt=-Ut/(2*U*U);C=-(Ur+q*Ut)/U-qt
    radial=zeros((Nr,1))
    for n in range(Nr):radial[n,0]=CBox.from_acb(R*acb(0,2*arb.pi()*n/Nr).exp())
    radial=radial.pad(arb_box((R*radial_gap).upper()))
    H=k*Z+radial*(k*U1+C)/4+radial*radial*k*(St-U1r/2-(qt*U1+q*U1t)/2)
    H+=radial**3*k*(kt*Lt+k*Ltt)/2
    MC,Mq,Mk,MH=map(modulus,(C,q,k,H))
    Mu=modulus(U);movement_flow=(2*Mq*R+arb(2)/3*Mk*R**(arb(3)/2)).upper()
    margin=(S-S1-movement_flow).lower()
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('all nested exact signed and common root paths stay in the full coefficient bidisk',margin>0)
    e=(MC*R).exp()-1
    gate('the complete deflated root quotient has the root logarithm',e<arb(1)/4)
    # F_sigma=exp(I_sigma), |I_sigma|<=MC*R; |Delta-1|<=e.
    ratio=((4*MC*R).exp()).upper()
    difference=(2*((2*MC*R).exp()-1)*(2*MC*R).exp()).upper()
    MN=(MH*ratio+arb(5)/16*difference).upper()
    MV=(MN/(R*R*(1-e)**(arb(4)/3))).upper()
    reference=arb(5050);Mres=(MV+reference).upper()
    report=dict(kind='actual_complete_negative_root_potential_from_seven_fields',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        input_path=str(a.fields),input_sha256=sha(a.fields),identity=d['identity'],root=d['root'],
        rho_radius=str(a.rho_radius),physical_field_strip=str(a.physical_strip),
        physical_characteristic_start_strip=str(a.start_strip),radial_phase_cells=Nr,angular_cells=Nt,
        exact_radial_degree=d['degree'],complete_positive_fourier_modes=d['K'],
        complete_field_errors_and_closed_joint_cell_gaps_retained=True,
        leading_cancellation='Z=G+U0/8; Z(0)=0 exactly for the true fields',
        exact_density='rho^(5/2)*Fcal/mu=G+3*U0/4+rho*(U1/4-U0_rho/2-(q*U0)_theta/2)+rho^2*(Sreg_theta-U1_rho/2-(q*U1)_theta/2)+rho^3*(k*Ltheta)_theta/2',
        exact_H='H=k*rho^(5/2)*Fcal/mu-5/16=k*Z+rho*(k*U1+C)/4+rho^2*k*(Sreg_theta-U1_rho/2-(q*U1)_theta/2)+rho^3*k*(k*Ltheta)_theta/2',
        exact_canonical_potential='V composed with Psi = [((H+5/16)*Delta^2/(F_plus*F_minus))-5/16]/(rho^2*Delta^(4/3))',
        removable_order_two='The numerator vanishes to order two at rho=0 by the already proved actual local canonical potential identity; the global complex characteristic identities analytically continue that same function.',
        complete_moduli={name:record(value) for name,value in dict(
            C=MC,q=Mq,kstar=Mk,U0=Mu,H=MH,Delta_minus_one=e,
            Delta_squared_over_Fproduct=ratio,Delta_squared_over_Fproduct_minus_one=difference,
            potential_numerator=MN,full_canonical_potential_pullback=MV,
            full_shifted_5050_residual_pullback=Mres).items()},
        U0_real_lower=record(Ulo),nested_characteristic_angle_movement=record(movement_flow),
        complete_characteristic_angle_margin=record(margin),
        full_Cauchy_derivative_tails={name:record(v.upper()) for name,v in tails.items()},
        full_finite_cell_movements={name:record(v.upper()) for name,v in movement.items()},
        gates=gates,all_modes_mean_and_parameter_values_retained=True,
        positive_canonical_chart_used=False,
        canonical_full_fixed_xi_angular_strip_proved=False,
        complete_shifted_Airy_propagation_proved=False,
        full_returned_Rstar_proved=False,
        scope='Complete potential composed with the true negative characteristic chart on the full complex physical bidisk. A fixed-xi canonical angle domain and complete shifted-Airy/source/frame consumers remain separate.',
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_subprincipal_root_parameter_transfer.py','fourfold_subprincipal_root_regularized_fft_v2.py',
            'fourfold_phase_beta_bulk_box.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py')},
        seconds=time.monotonic()-tick)
    save(a.out,report)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),moduli=report['complete_moduli'],
        margin=report['complete_characteristic_angle_margin'],seconds=report['seconds']),flush=True)

if __name__=='__main__':main()
