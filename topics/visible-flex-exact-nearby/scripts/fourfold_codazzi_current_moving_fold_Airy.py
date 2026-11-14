#!/usr/bin/env python3
"""Current moving body: true physical fold, all-mode Airy and fixed-r ports.

Every coefficient is recomputed from the supplied complete new physical
complex germ. Universal Airy32 is the sole object-independent numerical
input. No old-centre native turning constant is transferred. The local
ordinary H1 source and the exact graph trace scope are preserved.
"""
from __future__ import annotations
import argparse,gzip,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,acb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))
def upper(d,k):return box_from_record(d['bounds'][k]).upper()
def lower(d,k):return box_from_record(d['bounds'][k]).lower()
def scalar_snapshot(ns):return {k:record(v) for k,v in ns.items() if isinstance(v,arb)}


def fold_contract(g,z_radius,fold_radius,canonical_radius):
    d=g
    B=d['bounds'];u=lambda k:box_from_record(B[k]).upper();l=lambda k:box_from_record(B[k]).lower()
    C=d['complex_intrinsic_coefficients']
    az=lambda k:acb(box_from_record(C[k]['real']),box_from_record(C[k]['imag']))
    R=exact_arb(Fraction(d['complex_radial_radius']));sig=exact_arb(Fraction(d['physical_theta_strip']))
    Z=exact_arb(z_radius);rho=exact_arb(fold_radius);Tb=exact_arb(canonical_radius)
    Md,MP,Ld,LP=u('d'),u('aq'),u('dtheta'),u('aqtheta')
    epsilon=(Z*Z*Md+arb(2)/3*Z**3*MP).upper()
    lam=(Z*Z*Ld+arb(2)/3*Z**3*LP).upper()
    Jflow=(lam.exp()-1).upper()
    MG=(arb(2)/3*MP*lam.exp()).upper()
    MH=(epsilon/(Z*Z)).upper()
    t=rho/(Z*Z)
    Gdiff=(MG*t/(1-t)).upper()
    Gmin=(arb(2)/3*l('Re_aq_lower')-Gdiff).lower()
    Gprime=(MG/(Z*Z)/(1-t)**2).upper()
    Cmax=((arb(3)/2*MG)**(arb(2)/3)).upper()
    Cmin=((arb(3)/2*Gmin)**(arb(2)/3)/2).lower()
    Cr=(Gprime/(arb(3)/2*Gmin)**(arb(1)/3)).upper()
    Ctheta=(4*Cmax/sig).upper()
    Xr=(MH/(1-t)**2).upper();Xthetafee=(4*rho*MH/sig).upper()
    Trmin=(Cmin-rho*Cr).lower();Trmax=(Cmax+rho*Cr).upper()
    Ttheta=(rho*Ctheta).upper()
    Jmin=(Trmin-Trmax*Xthetafee-Xr*Ttheta).lower()
    Jmax=(Trmax*(1+Xthetafee)+Xr*Ttheta).upper()
    kmin=box_from_record(C['K1']['real']).lower();kmax=box_from_record(C['K1']['modulus_upper']).upper()
    bmin=(Cmin/kmax).sqrt().lower();bmax=(Cmax/kmin).sqrt().upper()
    frame=max(bmax.sqrt(),1/bmin.sqrt()).upper()
    DeltaMin=(l('Re_a_lower')*Jmin/bmax).lower()
    Asup=(Trmax+Md*Ttheta).upper()
    Ksmall=(rho*kmax).upper();Jprincipal=max(arb(1),Ksmall)
    Ainv=((Asup+u('a')*Ttheta*Jprincipal)/DeltaMin).upper()
    logr=(arb(1)/2*(Cr/Cmin+kmax/((R-rho)*kmin))).upper()
    logtheta=(Ctheta/(2*Cmin)).upper()
    logT=(((1+Xthetafee)*logr+Xr*logtheta)/Jmin).upper()
    logX=((Ttheta*logr+Trmax*logtheta)/Jmin).upper()
    Vmax=(frame**2*Ainv*u('complete_L_matrix')+(logT+logX)/2).upper()
    # Holomorphic inverse on |T|<=Tb, |Im X|<=sig/4.  The Picard
    # unknowns use radii rho/4 and sig/8, with their weighted max norm.
    ru=rho/4;rt=sig/8
    inverse_u_image=(Tb/Cmin).upper();inverse_theta_image=(ru*MH).upper()
    invrow1=(Tb/Cmin**2*(Cr+Ctheta*rt/ru)).upper()
    invrow2=(Xr*ru/rt+4*ru*MH/sig).upper()
    inverse_lipschitz=max(invrow1,invrow2).upper()
    source2D=(frame*Ainv*Jmax.sqrt()).upper()
    state2D=(frame/Jmin.sqrt()).upper()
    physical_angle_to_X_min=(Jmin/Trmax).lower()
    physical_angle_to_X_max=(Jmax/Trmin).upper()
    gates=[
        ('actual blown-up disk inside the new proved complex radial disk',Z*Z<R),
        ('complete actual characteristic displacement inside its physical angular margin',epsilon<sig/32),
        ('true Picard and inverse angular derivatives are contractions',lam<arb(1)/4 and Jflow<arb(1)/4),
        ('true odd label difference divided by z cubed has positive real part',Gmin>0),
        ('actual fold radial derivative and full Jacobian separated',Trmin>0 and Jmin>0),
        ('actual full two-line frame and source inverse separated',DeltaMin>0 and bmin>0),
        ('whole canonical complex product lies inside the same new candidate germ',inverse_u_image<ru and inverse_theta_image<rt),
        ('two-variable true inverse chart is a strict contraction',inverse_lipschitz<arb(1)/4),
        ('complete original local potential and physical source finite',Vmax.is_finite() and source2D.is_finite()),
    ]
    return dict(bounds=scalar_snapshot(locals()),gates=[dict(name=n,passed=bool(v)) for n,v in gates])


def balanced_contract(g,f,air,half_width):
    a=lambda k:box_from_record(f['bounds'][k]).upper()
    lo=lambda k:box_from_record(f['bounds'][k]).lower()
    b=lambda k:box_from_record(g['bounds'][k]).upper()
    delta=exact_arb(half_width);T_outer=15*delta/4;Kair=arb(air['complete_two_port_kernel_bound']);Q=8/exact_arb(Fraction(g['physical_theta_strip']))
    diag0=((a('Asup')*max(b('complete_L11'),b('complete_L22'))
        +b('a')*a('Ttheta')*a('Ksmall')*b('complete_g'))/lo('DeltaMin')+a('logT')/2).upper()
    off0=((a('Asup')*b('complete_g')+b('a')*a('Ttheta')*max(b('complete_L11'),b('complete_L22')))
        /(lo('bmin')*lo('DeltaMin'))+a('logX')/2).upper()
    diag1=diag0*Q;diag2=2*diag0*Q*Q;off1=off0*Q
    # Full mean-preserving cap norm, followed by the extra 1/6 Sobolev
    # interpolation needed to reconstruct the whole physical L2 state.
    md0=(2*diag0**(arb(5)/6)*(diag0+diag1)**(arb(1)/6)).upper()
    md1=(2*diag1**(arb(5)/6)*(diag1+diag2)**(arb(1)/6)).upper()
    mdS=(md0**(arb(5)/6)*(md0+md1)**(arb(1)/6)).upper()
    moS=(off0**(arb(5)/6)*(off0+off1)**(arb(1)/6)).upper()
    balanced_matrix=(mdS+moS).upper()
    B=(2*delta*Kair).upper();P=(2*Kair*delta.sqrt()).upper()
    contraction=(B*balanced_matrix).upper();resolvent=(1/(1-contraction)).upper()
    balanced_source=(B*resolvent).upper();balanced_ports=(P*resolvent).upper()
    # Exact true two-dimensional physical source map. The source norm is
    # the full physical H1 norm (including its radial derivative).
    rX=(a('Ttheta')/lo('Jmin')).upper();thetaX=(a('Trmax')/lo('Jmin')).upper()
    sourceL2=a('source2D')
    sourceH1=(sourceL2*(1+Q+rX+thetaX)).upper()
    sourceHthird=(sourceL2**(arb(2)/3)*sourceH1**(arb(1)/3)).upper()
    physical_source=(a('state2D')*balanced_source*sourceHthird).upper()
    physical_ports=(a('state2D')*balanced_ports).upper()
    trace_reconstruct=(a('frame')/lo('physical_angle_to_X_min').sqrt()).upper()
    trace_source=(2*Kair*delta.sqrt()*(1+balanced_matrix*balanced_source)).upper()
    trace_ports=(2*Kair+2*Kair*delta.sqrt()*balanced_matrix*balanced_ports).upper()
    physical_trace_source=(trace_reconstruct*trace_source*sourceHthird).upper()
    physical_trace_ports=(trace_reconstruct*trace_ports).upper()
    # Same exact Airy norm from the inner negative boundary to the outer
    # canonical section. No q-energy or delta-dependent frame conversion.
    length=T_outer-delta
    negative_integral=(length*balanced_matrix).upper()
    negative_Cauchy=(64*(64*negative_integral).exp()).upper()
    negative_L2_source=(negative_Cauchy*length.sqrt()).upper()
    negative_physical_H1_source=(negative_L2_source*sourceHthird).upper()
    # Physical trace H^(1/3) supplies an inner balanced port. This bound
    # uses the actual curve Jacobian and the complete original frame.
    comp0=a('physical_angle_to_X_max').sqrt()
    comp1=max(comp0,1/lo('physical_angle_to_X_min').sqrt())
    frame_Hthird=(a('frame')*(1+Q)**(arb(1)/3)).upper()
    physical_trace_to_balanced=(frame_Hthird*comp0**(arb(2)/3)*comp1**(arb(1)/3)).upper()
    fixed_physical_radial_offset=delta/2
    fixed_r_T_min=(2*lo('Cmin')*fixed_physical_radial_offset).lower()
    fixed_r_T_max=(a('Cmax')*fixed_physical_radial_offset).upper()
    gates=[
        ('complete object-independent two-port Airy kernel includes both source columns',Kair<=32),
        ('canonical strip fits the actual new complex inverse',delta<T_outer and T_outer<upper(f,'Tb')),
        ('actual removable upper-right quotient is bounded before multiplication',off0.is_finite()),
        ('complete full-frequency balanced matrix absorbed on one Hilbert space',contraction<arb(1)/8),
        ('whole ordinary physical H1 source and both mean outputs retained',sourceHthird.is_finite()),
        ('negative two-sided complete Airy propagation stays finite',negative_Cauchy.is_finite()),
        ('true fixed-r graph lies inside the complete negative annulus',delta<fixed_r_T_min and fixed_r_T_max<T_outer),
    ]
    return dict(bounds=scalar_snapshot(locals()),gates=[dict(name=n,passed=bool(v)) for n,v in gates])


def real_graph_contract(g,f,b):
    fu=lambda k:upper(f,k)
    gu=lambda k:upper(g,k)
    gl=lambda k:lower(g,k)
    bu=lambda k:upper(b,k)
    z=lambda x:box_from_record(x).upper()
    R=exact_arb(Fraction(g['complex_radial_radius']));sig=exact_arb(Fraction(g['physical_theta_strip']))
    R1=fu('Z')**2;Tb=fu('Tb');delta=bu('delta');h=delta/2
    ri=fu('inverse_u_image');MG=fu('MG');MH=fu('MH');t=ri/R1;Q=4/sig
    Gdiff=(MG*t/(1-t)).upper()
    Gmin=(arb(2)/3*gl('Re_aq_lower')-Gdiff).lower()
    Gr=(MG/R1/(1-t)**2).upper();Grr=(2*MG/R1**2/(1-t)**3).upper()
    Gtheta=(arb(2)/3*gu('aqtheta')+Q*Gdiff).upper()
    ga=z(g['complex_intrinsic_coefficients']['gamma']['modulus_upper'])
    kmax=fu('kmax');kmin=box_from_record(f['bounds']['kmin']).lower()
    ptheta2=(ga*kmax.sqrt()*z(g['physical_v_derivative_sup'][2])).upper()
    Gtheta2=(arb(2)/3*ptheta2+2*Q**2*Gdiff).upper();Grtheta=(Q*Gr).upper()
    den=(arb(3)/2*Gmin)**(arb(1)/3)
    Cmin=(den**2).lower();Cmax=fu('Cmax')
    Cr=(Gr/den).upper();Ctheta=(Gtheta/den).upper()
    Crr=(Grr/den+Gr**2/(2*den**4)).upper()
    Crtheta=(Grtheta/den+Gr*Gtheta/(2*den**4)).upper()
    Ctheta2=(Gtheta2/den+Gtheta**2/(2*den**4)).upper()
    Htheta=(Q*MH).upper();Htheta2=(2*Q**2*MH).upper()
    Xr=(MH/(1-t)**2).upper();Xthetafee=(ri*Htheta).upper()
    Trmin=(Cmin-ri*Cr).lower();Trmax=(Cmax+ri*Cr).upper()
    Ttheta=(ri*Ctheta).upper();Trr=(2*Cr+ri*Crr).upper()
    Trtheta=(Ctheta+ri*Crtheta).upper();Ttheta2=(ri*Ctheta2).upper()
    Jmin=(Trmin*(1-Xthetafee)-Xr*Ttheta).lower()
    Jmax=(Trmax*(1+Xthetafee)+Xr*Ttheta).upper()
    circle_fee=(Xthetafee+Xr*Ttheta/Trmin).upper()
    rX=(Ttheta/Jmin).upper();thetaX=(1/(1-circle_fee)).upper()
    rT=((1+Xthetafee)/Jmin).upper();thetaT=(Xr/Jmin).upper()
    bmin=(Cmin/kmax).sqrt().lower();bmax=(Cmax/kmin).sqrt().upper()
    frame=max(bmax.sqrt(),1/bmin.sqrt()).upper()
    logr=(arb(1)/2*(Cr/Cmin+kmax/((R-ri)*kmin))).upper()
    logtheta=(Ctheta/(2*Cmin)).upper()
    logX=(rX*logr+thetaX*logtheta).upper();logT=(rT*logr+thetaT*logtheta).upper()
    FX=(frame*logX/2).upper();FT=(frame*logT/2).upper()
    Md=gu('d');Ma=gu('a');Ld=gu('dtheta');La=gu('atheta')
    Amin=(Trmin-Md*Ttheta).lower();Asup=(Trmax+Md*Ttheta).upper()
    # The actual first-order radial matrix is A I-a Ttheta J(K).
    Ksmall=(ri*kmax).upper();Jnorm=max(arb(1),Ksmall)
    Ainv=(1/(Amin-Ma*Ttheta*Jnorm)).upper()
    dr=(Md/(R-ri)).upper();ar=(Ma/(R-ri)).upper()
    Ar=(Trr+dr*Ttheta+Md*Trtheta).upper()
    Atheta=(Trtheta+Ld*Ttheta+Md*Ttheta2).upper()
    ATr=(Ar+(ar*Ttheta+Ma*Trtheta)*Jnorm+Ma*Ttheta*kmax).upper()
    ATtheta=(Atheta+(La*Ttheta+Ma*Ttheta2)*Jnorm).upper()
    ATX=(rX*ATr+thetaX*ATtheta).upper();ATT=(rT*ATr+thetaT*ATtheta).upper()
    Mf0=(frame*Ainv).upper()
    MfX=(FX*Ainv+frame*Ainv**2*ATX).upper()
    MfT=(FT*Ainv+frame*Ainv**2*ATT).upper()
    sourceL2=(Jmax.sqrt()*Mf0).upper()
    sourceH1X=(Jmax.sqrt()*(Mf0+MfX+Mf0*(rX+thetaX))).upper()
    sourceHthird=(sourceL2**(arb(2)/3)*sourceH1X**(arb(1)/3)).upper()
    stateL2=(frame/Jmin.sqrt()).upper()
    # Real matrix bounds use correlation before dividing. Derivative bounds
    # below still use the already-proved complete complex product envelope.
    DeltaMin=(Amin**2-Ma**2*Ttheta**2*Ksmall).lower()
    lmax=max(gu('complete_L11'),gu('complete_L22'));gg=gu('complete_g')
    diagReal=((Asup*lmax+Ma*Ttheta*Ksmall*gg)/DeltaMin+logT/2).upper()
    offReal=((Asup*gg+Ma*Ttheta*lmax)/(bmin*DeltaMin)+logX/2).upper()
    # Exact fixed physical circle r=rstar-h, expressed in canonical X.
    graphQmin=(h*Cmin).lower();graphQmax=(h*Cmax).upper()
    graphXfee=(h*Htheta).upper();graphXmin=(1-graphXfee).lower()
    graphXmax=(1+graphXfee).upper()
    graphSlope=(h*Ctheta/graphXmin).upper()
    graphSecond=(h*Ctheta2/graphXmin**2+h**2*Ctheta*Htheta2/graphXmin**3).upper()
    graphFrameX=(frame*logtheta/(2*graphXmin)).upper()
    graphPhysicalH1toU=(frame**2*graphXmax+graphFrameX**2*graphXmax+frame**2/graphXmin).sqrt().upper()
    graphUtoPhysicalL2=(frame/graphXmin.sqrt()).upper()
    lengthMin=(graphQmin-delta).lower();lengthMax=(graphQmax-delta).upper()
    qmin=delta.sqrt();qmax=graphQmax.sqrt()
    p=graphSlope;p2=graphSecond;L=lengthMax
    foliationDen=(1-p**2*graphQmax).lower()
    foliationDenX=(2*p*p2*graphQmax+p**3).upper()
    af=(L/foliationDen).upper()
    afX=(p/foliationDen+L*foliationDenX/foliationDen**2).upper()
    df=(af*p*graphQmax).upper()
    dfX=(afX*p*graphQmax+af*p2*graphQmax+af*p**2).upper()
    principalSpatial=(dfX+df*p/delta+qmax*afX+af*p/qmin).upper()
    principalDerivative=(dfX+qmax*afX+af*p/qmin).upper()
    radialMargin=(Tb-graphQmax).lower()
    D0=diagReal;E0=offReal
    D1=(8/sig)*bu('diag0');E1=(8/sig)*bu('off0')
    DT=(bu('diag0')/radialMargin).upper();ET=(bu('off0')/radialMargin).upper()
    vH=(D0+qmax*E0).upper()
    vHX=(D1+p*DT+qmax*(E1+p*ET)+p*E0/qmin).upper()
    localH=(af*(1+p*qmax)*vH).upper()
    localHX=(afX*(1+p*qmax)*vH+af*(p2*qmax+p**2/qmin)*vH
        +af*(1+p*qmax)*vHX).upper()
    energy0=(qmax/qmin*(principalSpatial/2+localH).exp()).upper()
    energy1=(energy0*principalDerivative.exp()).upper()
    scalar22=(af*(D0+p*graphQmax*E0)).upper()
    scalar21=(af*(E0+p*D0)).upper()
    scalarGain=(dfX/2+scalar22).exp().upper()
    # Source is differentiated in the actual (tau,X) foliation, before
    # comparing to the full ordinary physical H1(dr dtheta) norm.
    PS0=(af*(1+p*Jnorm)*Mf0).upper()
    PSX=(afX*(1+p*Jnorm)*Mf0+af*(p2*Jnorm+p**2)*Mf0
        +af*(1+p*Jnorm)*(MfX+p*MfT)).upper()
    leaf_rX=(rX+p*rT).upper();leaf_thetaX=(thetaX+p*thetaT).upper()
    measure=(Jmax/lengthMin).sqrt().upper()
    source0=(measure*PS0).upper()
    source1=(measure*(PSX+PS0*(leaf_rX+leaf_thetaX))).upper()
    # Columns: complete ordinary H1 initial state; complete physical H1
    # source on the exact between-graph domain. These are separate linear
    # columns and may subsequently be added by Minkowski.
    cE0=energy0;cE1=(energy1*(1+localHX*cE0)).upper()
    sE0=(energy0*source0).upper();sE1=(energy1*(localHX*sE0+source1)).upper()
    cU2=(scalarGain*(1+af*cE1+scalar21*cE0)).upper()
    sU2=(scalarGain*(af*sE1+scalar21*sE0+source0)).upper()
    cH=(cE0**2+cE1**2).sqrt().upper();sH=(sE0**2+sE1**2).sqrt().upper()
    cState=(cE0**2+cU2**2).sqrt().upper();sState=(sE0**2+sU2**2).sqrt().upper()
    frequencyMeanFactor=((arb(17).sqrt()/4)**(arb(1)/3)).upper()
    cAiry=(cH**2+qmin**(arb(2)/3)*cU2**(arb(5)/3)*cH**(arb(1)/3)+frequencyMeanFactor*cU2**2).sqrt().upper()
    sAiry=(sH**2+qmin**(arb(2)/3)*sU2**(arb(5)/3)*sH**(arb(1)/3)+frequencyMeanFactor*sU2**2).sqrt().upper()
    forwardPhysicalData=(graphUtoPhysicalL2*cState).upper()
    forwardPhysicalSource=(graphUtoPhysicalL2*sState).upper()
    reverseAiryPhysicalData=(cAiry*graphPhysicalH1toU).upper()
    reverseAiryPhysicalSource=sAiry
    gates=[
        ('complete new real inverse image lies inside the actual analytic disk',ri<R1 and ri<R),
        ('new physical root angular first and second jets retained',Gmin>0 and Gtheta2.is_finite()),
        ('actual real chart and true angular Jacobians separated',Jmin>0 and circle_fee<arb(1)/1000),
        ('full real source matrix inverted only after positive gate',Amin-Ma*Ttheta*Jnorm>0 and DeltaMin>0),
        ('actual fixed-r graph is strictly beyond the negative inner port',lengthMin>0),
        ('whole graph foliation stays within the actual complex inverse',graphQmax<Tb),
        ('actual graph foliation uniformly spacelike in both directions',p*qmax<arb(1)/4),
        ('mixed canonical T derivatives included in whole first commutator',radialMargin>0 and localHX.is_finite()),
        ('complete source pays full physical radial and angular derivatives',source1.is_finite()),
        ('full mean-compatible capped Airy reconstruction finite',cAiry.is_finite() and sAiry.is_finite()),
        ('ordinary-state reconstruction uses scalar second row without inverse q',True),
    ]
    return dict(bounds=scalar_snapshot(locals()),gates=[dict(name=n,passed=bool(v)) for n,v in gates])


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--germ',type=Path,default=Path('notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz'))
    ap.add_argument('--airy',type=Path,default=Path('notes/2026-11-13-R133-universal-two-port-Airy-v2-native.json.gz'))
    ap.add_argument('--z-radius',type=Fraction,default=Fraction(1,512))
    ap.add_argument('--fold-radius',type=Fraction,default=Fraction(1,2**26))
    ap.add_argument('--canonical-radius',type=Fraction,default=Fraction(1,2**34))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,2**36))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;t0=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every current-body turning attempt')
    g,air=read(args.germ),read(args.airy)
    doc=dict(kind='current_moving_body_complete_physical_fold_Airy_and_fixed_radial_ports',complete=False,proved=False,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.germ,args.airy)},failure=None)
    try:
        if (not g['complete'] or not g['proved'] or not g['whole_affine_parameter_interval']
            or not g['all_finite_candidate_modes_retained']
            or not g['physical_candidate_is_analytic_inverse_angle_pullback_not_finite_physical_Fourier']
            or g['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_moving_turning_complex_germ.py'))):
            raise ValueError('complete new-centre true physical complex germ required')
        if (not air['complete'] or not air['negative_root_derivative_exact_reflection']
            or air['source_sha256']!=sha(Path(__file__).with_name('fourfold_full_two_port_Airy_universal_v2.py'))):
            raise ValueError('complete correctly oriented universal full two-port Airy kernel required')
        f=fold_contract(g,args.z_radius,args.fold_radius,args.canonical_radius)
        b=balanced_contract(g,f,air,args.half_width)
        p=real_graph_contract(g,f,b)
        gates=f['gates']+b['gates']+p['gates']
        doc.update(complete=all(v['passed'] for v in gates),proved=all(v['passed'] for v in gates),gates=gates,
            fold=f,balanced=b,real_ports=p,actual_candidate_inputs=g['inputs'],candidate_sha256=g['candidate_sha256'],
            object_sha256=g['object_sha256'],exact_amplitude=g['exact_amplitude'],actual_fixed_nu=g['actual_fixed_nu'],
            whole_affine_parameter_interval=True,exact_parameter_half_width=g['exact_parameter_half_width'],
            exact_center_parameter=g['exact_center_parameter'],actual_root_interval=g['root_interval'],
            actual_candidate_piece=g['actual_candidate_piece'],exact_candidate_piece=g['exact_candidate_piece_interval'],
            scales=dict(z_radius=str(args.z_radius),fold_radius=str(args.fold_radius),canonical_radius=str(args.canonical_radius),
                canonical_half_width=str(args.half_width),physical_radial_offset=str(args.half_width/2),
                true_physical_theta_strip=g['physical_theta_strip']),
            original_physical_local_Jacobi_at_actual_approximate_centre=True,
            all_modes_two_mean_states_and_both_full_port_columns=True,
            complete_source_scope='ordinary physical H1(dr dtheta) on each exact inverse-image domain; no angular-only substitution',
            negative_forward_graph_scope='canonical ordinary H1 initial two-state data to physical fixed-r L2 trace',
            negative_reverse_graph_scope='physical fixed-r H1 trace to complete padded Airy E at T=-delta',
            derivative_loss_explicit=True,old_nonradial_numerical_constants_transferred=False,
            real_physical_inverse_angle_constructed=True,actual_fold_constructed=True,
            physical_fixed_circle='rstar(eta)-delta/2, with its actual nonconstant canonical graph',
            outside_PPoly_interfaces_and_positive_regular_graph_attached=False,
            moving_variation_residual_bridge_assumed_zero=False,
            full_feedback_inverse_or_nonlinear_body_solution_proved=False)
    except Exception as exc:doc['failure']=f'{type(exc).__name__}: {exc}'
    doc['seconds']=time.monotonic()-t0
    doc['dependencies']={n:sha(Path(__file__).with_name(n)) for n in ('fourfold_codazzi_rotational_cap_jacobi.py',
        'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')}
    save(args.out,doc)
    summary=dict(complete=doc['complete'],out=str(args.out),sha256=sha(args.out),failure=doc['failure'],seconds=doc['seconds'])
    if 'gates' in doc:summary.update(gates=len(doc['gates']),failed=[x['name'] for x in doc['gates'] if not x['passed']],
        balanced_contraction=upper(doc['balanced'],'contraction').str(14),
        graph_reverse_physical_H1_to_Airy=upper(doc['real_ports'],'reverseAiryPhysicalData').str(14),
        graph_forward_H1_to_physical_L2=upper(doc['real_ports'],'forwardPhysicalData').str(14))
    print(summary,flush=True)
    if not doc['complete']:raise SystemExit(1)


if __name__=='__main__':main()
