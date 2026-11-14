#!/usr/bin/env python3
"""Same actual .75 body: real fold jets and two-way fixed-r graph ports.

The actual graph is not replaced by a constant canonical radial section.
Two differentiated symmetrized energies and the complete second-row
transport avoid a q^{-1} conversion of the whole state.  The input is H1,
not a claimed same-space inverse.  All modes and both means remain.
"""
from __future__ import annotations
import argparse,gzip,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--germ',type=Path,default=Path('notes/2026-11-13-R133-actual-alpha075-complex-turning-germ.json.gz'))
    ap.add_argument('--fold',type=Path,default=Path('notes/2026-11-13-R133-actual-alpha075-fold-Airy-contract.json.gz'))
    ap.add_argument('--balanced',type=Path,default=Path('notes/2026-11-13-R133-actual-alpha075-balanced-fold-ports-v3.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;t0=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every complete graph-port attempt')
    g,f,b=map(read,(args.germ,args.fold,args.balanced))
    for d,name in ((g,'fourfold_codazzi_turning_complex_germ.py'),
                   (f,'fourfold_codazzi_actual_fold_Airy_contract.py'),
                   (b,'fourfold_codazzi_balanced_fold_ports_v3.py')):
        if not d['complete'] or d['source_sha256']!=sha(Path(__file__).with_name(name)):
            raise ValueError('complete unchanged actual coefficient/fold inputs required')
    if (f['actual_candidate_inputs']!=g['inputs'] or b['actual_candidate_inputs']!=g['inputs']
        or f['inputs'][str(args.germ)]!=sha(args.germ)
        or b['inputs'][str(args.germ)]!=sha(args.germ)
        or b['inputs'][str(args.fold)]!=sha(args.fold)):
        raise ValueError('same actual candidate, root and full affine parameter identity required')
    fu=lambda k:box_from_record(f['bounds'][k]).upper()
    gu=lambda k:box_from_record(g['bounds'][k]).upper()
    gl=lambda k:box_from_record(g['bounds'][k]).lower()
    bu=lambda k:box_from_record(b['bounds'][k]).upper()
    z=lambda x:box_from_record(x).upper()
    R=exact_arb(Fraction(g['complex_radial_radius']));sig=exact_arb(Fraction(g['physical_theta_strip']))
    R1=(arb(1)/512)**2;Tb=arb(2)**-34;delta=arb(2)**-36;h=arb(2)**-37
    ri=fu('inverse_u_image');MG=fu('MG');MH=fu('MH');t=ri/R1;Q=4/sig
    Gdiff=(MG*t/(1-t)).upper()
    Gmin=(arb(2)/3*gl('Re_aq_lower')-Gdiff).lower()
    Gr=(MG/R1/(1-t)**2).upper();Grr=(2*MG/R1**2/(1-t)**3).upper()
    Gtheta=(arb(2)/3*gu('aqtheta')+Q*Gdiff).upper()
    ga=z(g['complex_intrinsic_coefficients']['gamma']['modulus_upper'])
    kmax=fu('kmax');kmin=box_from_record(f['bounds']['kmin']).lower()
    ptheta2=(ga*kmax.sqrt()*z(g['candidate_v_derivative_Astrip'][2])).upper()
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
    D1=8192*bu('diag0');E1=8192*bu('off0')
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
        ('same actual candidate full eta germ and complete fold consumed',True),
        ('real inverse image radius strictly inside complete analytic germ',ri<R1 and ri<R),
        ('root angular first and second jets retained before Cauchy tail',Gmin>0),
        ('complete real chart and physical angle Jacobians positive',Jmin>0 and circle_fee<arb(1)/1000),
        ('complete real source matrix inverse positive before division',Amin-Ma*Ttheta*Jnorm>0 and DeltaMin>0),
        ('actual fixed-r graph lies strictly beyond the inner negative port',lengthMin>0),
        ('whole graph and all foliation leaves inside actual inverse rectangle',graphQmax<Tb),
        ('two-way graph foliation is uniformly spacelike',p*qmax<arb(1)/4),
        ('complete coefficient first derivatives include mixed T derivatives',radialMargin>0 and localHX.is_finite()),
        ('two energy layers and true scalar second-row transport are finite',all(x.is_finite() for x in (energy0,energy1,scalarGain))),
        ('ordinary physical H1 source includes radial and angular first derivatives',source1.is_finite()),
        ('full mean-compatible Airy reconstruction pays capped Fourier weight',frequencyMeanFactor>1),
        ('both physical means and every Fourier mode retained',True),
        ('ordinary-state reconstruction does not use inverse q or quarter-power delta',True),
        ('source domain is exact between-graph image with its true two-dimensional Jacobian',True),
    ]
    names=('ri','Gdiff','Gmin','Gr','Grr','Gtheta','Gtheta2','Grtheta','Cmin','Cmax','Cr','Ctheta','Crr','Crtheta','Ctheta2',
      'Htheta','Htheta2','Xr','Xthetafee','Trmin','Trmax','Ttheta','Trr','Trtheta','Ttheta2','Jmin','Jmax','circle_fee',
      'rX','thetaX','rT','thetaT','bmin','bmax','frame','logr','logtheta','logX','logT','FX','FT','Amin','Asup','Ksmall','Ainv',
      'ATr','ATtheta','ATX','ATT','Mf0','MfX','MfT','sourceL2','sourceH1X','sourceHthird','stateL2','DeltaMin','diagReal','offReal',
      'graphQmin','graphQmax','graphXfee','graphXmin','graphXmax','graphSlope','graphSecond','graphFrameX','graphPhysicalH1toU',
      'graphUtoPhysicalL2','lengthMin','lengthMax','qmin','qmax','foliationDen','foliationDenX','af','afX','df','dfX',
      'principalSpatial','principalDerivative','radialMargin','D1','E1','DT','ET','vH','vHX','localH','localHX','energy0','energy1',
      'scalar22','scalar21','scalarGain','PS0','PSX','leaf_rX','leaf_thetaX','measure','source0','source1','cE0','cE1','sE0','sE1',
      'cU2','sU2','cH','sH','cState','sState','frequencyMeanFactor','cAiry','sAiry','forwardPhysicalData','forwardPhysicalSource',
      'reverseAiryPhysicalData','reverseAiryPhysicalSource')
    vals=locals();complete=all(bool(v) for _,v in gates)
    doc=dict(kind='actual_same_body_fixed_physical_radial_graph_to_full_Airy_ports',complete=complete,proved=complete,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.germ,args.fold,args.balanced)},
        actual_candidate_inputs=g['inputs'],object_sha256=g['object_sha256'],exact_amplitude=g['exact_amplitude'],
        actual_fixed_nu=g['actual_fixed_nu'],whole_affine_parameter_interval=True,
        exact_parameter_half_width=g['exact_parameter_half_width'],exact_center_parameter=g['exact_center_parameter'],
        physical_fixed_radial_section='rstar(eta)-1/137438953472',canonical_negative_inner_section='-1/68719476736',
        real_geometry_scope='entire real inverse image of |T|<=2^-34, all real X; fixed-r graph derivatives at r=rstar-2^-37',
        full_source_scope='complete physical H1(dr dtheta) on the exact domain between T=-2^-36 and the actual fixed-r graph; no extension or rectangular replacement',
        forward_scope='canonical ordinary H1 two-state data to original physical L2 two-state trace on the fixed-r circle',
        reverse_scope='original physical H1 two-state data on the fixed-r circle to the full padded Airy E norm at T=-2^-36',
        derivative_loss_explicit=True,full_original_means_and_all_frequencies=True,
        graph_to_constant_T_identity_assumed=False,delta_quarter_power_reconstruction_used=False,
        inside_common_germ_outer_strict_segment_attached=False,positive_regular_graph_attached=False,
        full_feedback_inverse_or_nonlinear_body_solution_proved=False,
        bounds={n:record(vals[n]) for n in names},gates=[dict(name=n,passed=bool(v)) for n,v in gates],
        seconds=time.monotonic()-t0,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in ('fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')})
    save(args.out,doc)
    print(dict(complete=complete,gates=len(gates),out=str(args.out),sha256=sha(args.out),
        energy0=energy0.str(14),energy1=energy1.str(14),sourceH1X=sourceH1X.str(14),
        forwardPhysicalData=forwardPhysicalData.str(14),forwardPhysicalSource=forwardPhysicalSource.str(14),
        reverseAiryPhysicalData=reverseAiryPhysicalData.str(14),reverseAiryPhysicalSource=reverseAiryPhysicalSource.str(14)),flush=True)
    if not complete:raise SystemExit(1)


if __name__=='__main__':main()
