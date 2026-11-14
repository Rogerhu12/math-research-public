#!/usr/bin/env python3
"""Exact F224 radius ledger plus explicitly nonrigorous linear-scale diagnostics.

The rational comparisons check the new cutoff/angle proof in the companion
scaled-deep-map note. The floating log-gain section is separate: it does not
assert that the actual nonlinear shallow trace matches the exact deep graph.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path


def two(k):
    return F(2**k) if k >= 0 else F(1,2**(-k))


def load(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),raw


def logsum(values):
    values=[x for x in values if x is not None]
    if not values:return None
    top=max(values)
    return top+math.log2(sum(2**(x-top) for x in values))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--linear-report',type=Path,required=True)
    p.add_argument('--tail-response',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    own_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    linear,linear_raw=load(args.linear_report)
    tail,tail_raw=load(args.tail_response)
    parameters=linear['model']['physicalParameters']
    ep=F.from_float(parameters['epsilonScale'])
    rc=F.from_float(parameters['rCuff'])
    en=ep/rc**7
    Mbar=lambda n:51611*(n+10)
    exp=dict(
        forced_gain=F(6812+15*24)-F(6501,2)*199,
        stronger_raw_correction=F(13396)-F(723,2)*199,
        correction_jets=F(6826+15*24)-F(3248)*199,
        F192_A=F(60*24)-F(3,4)*199,
        F192_K=F(27+320)-F(11,2)+72*24-F(3,4)*199,
        F192_radius_use=F(256+60*24-1924)-F(3,4)*199,
        F224_A=F(60*24)-F(3,4)*231,
        F224_K=F(27+320)-F(11,2)+72*24-F(3,4)*231,
        F224_radius_use=F(256+60*24-1900)-F(3,4)*231,
        F224_nonlinear_Lipschitz=F(1+27+320)-F(11,2)+72*24-F(3,4)*231-1900,
        current_slope_F192=F(6+15)-F(7,4)*199,
    )
    beta_upper=3*two(-199)+4*two(-298)+128*two(-149)
    checks=dict(
        epsilon_normalization=two(14)<en<two(15),
        short_transfer_at192=(48*Mbar(192)**4)**2 < 2**199,
        short_transfer_monotone=F(203,202)**8<2,
        M192_below_2pow24=Mbar(192)<2**24,
        M224_below_2pow24=Mbar(224)<2**24,
        M315_below_2pow24=Mbar(315)<2**24,
        M_coefficient=F(73728*7,10)*202+3<=Mbar(192),
        angular_beta=256*beta_upper<two(-133),
        angular_gap=two(-133)<F(1,48),
        three_derivative_loss=145**3<2**22,
        forced_gain=exp['forced_gain']<0,
        stronger_raw_correction=exp['stronger_raw_correction']<0,
        correction_jets=exp['correction_jets']<0,
        A_monotone_from192=F(60,202)<F(3,4)*F(2,3),
        B_monotone_after315=F(72,325)<F(3,8)*F(2,3),
        F192_radius=exp['F192_radius_use']<-2,
        F224_radius=exp['F224_radius_use']<-2,
        d_below_3over16=F(1,2**11)<F(3,16)**4,
        F192_contraction=two(-11)+F(3,16)<F(1,4),
        F224_contraction=two(-27)+F(3,16)<F(1,4),
        F224_height_inverse=2_000_000<2**21,
        F224_height_parameter_inside_state=two(-1924)<two(-1900)/4,
        F224_height_contraction=4+21+1897-1924<=-2,
        F224_height_free_term=21-1947<=-1924-2,
        F224_height_quadratic_term=3+21+1897-1924<=-3,
        projection_labels_inside_R17=two(60-1900)<F(1,4),
        current_slope=exp['current_slope_F192']<0,
    )
    coef=F(339300)*F(16,9)*9**8
    nu=lambda j:F(j*j*(4*j*j-1),3)
    checks.update(
        balanced_drift_constant=coef**2 < 2**91,
        balanced_spectral_gap=all((256*nu(j))**2>257**2*2**(j-1) for j in range(2,47)),
        d_below_3over20=F(1,2**11)<F(3,20)**4,
        balanced_projections=F(76,63)<2,
        balanced_common_Green=6+4+512<2**10,
        balanced_eta_F224=F(50)-F(231,2)<-65,
        balanced_height_error=5-65<=-60,
        nonlinear_trace_coefficient=7+3*21+1897==1967,
        numerical_boundary_inside_chart=two(-2048)<two(-1947),
        nonlinear_boundary_remainder=1967-2048<=-81,
        combined_boundary_error=two(-60)+two(-81)<two(-59),
        mean_cut_constant=19**6<2**26,
        mean_height_series=(F(235,234)**30)**4 < 2,
    )

    # An arithmetic scale diagnostic using the existing finite linear ray.
    # It is deliberately not part of any PASS assertion.
    far_run=max(linear['runs'],key=lambda x:x['far'])
    far=far_run['far']
    heights=tail['request']['height']
    tau=math.log(2)/4
    rows=[]
    for row,height in zip(far_run['rows'],heights):
        mode=row['mode'];nu=mode*mode*(mode*mode-1)/12;d=2**(-2.75)
        t00=1-65*nu;t10=65*d*nu*(nu-1);t11=d*(1-(65/64)*nu)
        tr=t00+t11
        eig=.5*(tr-math.sqrt(tr*tr-4*d))
        slope=t10/(eig-t11)
        entry=dict(mode=mode,physical_cut_height=height,
                   linear_log_height_gain=row['logAbsoluteHeightGain'],
                   ideal_raw_large_eigenvalue=eig,ideal_raw_slope=slope)
        for n in [224,512]:
            if not height:
                entry['F'+str(n)]=None
                continue
            log_Qnorm=(math.log(abs(height))-row['logAbsoluteHeightGain']
                       -(n+1-far)*math.log(abs(eig))+3*math.log(float(rc)))
            log_zeta=math.log(float(en))+5.5*(math.log(.006)-n*math.log(2))
            log_z=(log_Qnorm-log_zeta+mode*tau)/math.log(2)
            entry['F'+str(n)]=dict(mathematical_port=n,source_physical_node=n+1,
                                   log2_abs_Q_normalized=log_Qnorm/math.log(2),
                                   log2_abs_low_height_coordinate=log_z,
                                   log2_raw_pair_norm=log_z+math.log2(1+abs(slope)))
        rows.append(entry)
    z224=logsum([x['F224']['log2_abs_low_height_coordinate'] for x in rows if x['F224']])
    diagnostics=dict(
        status='UNVERIFIED numerical linear scale estimate; not a trace inclusion certificate',
        method='Use actual cut heights only to label finite linear rays, then ideal raw inward gains beyond the recorded far. Mathematical F is physical node F+1.',
        caveats=[
            'The nonlinear depth8 endpoint has not been propagated by this calculation.',
            'Whole linear gains are finite RK4 data; radial and interval errors are not enclosed.',
            'The finite far condition is not the exact nonlinear F224 trace.',
            'Unrepresented high Fourier modes are not set to zero in the theorem.',
        ],
        source_far=far,source_steps=linear['steps'],tau_F=tau,rows=rows,
        log2_low_height_l1_F224=z224,
        numerical_margin_to_2pow_minus1947=None if z224 is None else -1947-z224,
    )
    result=dict(
        status='PASS' if all(checks.values()) else 'FAIL',
        exact_checks=checks,
        rational_log2_bounds={k:dict(exact=str(v),decimal=float(v)) for k,v in exp.items()},
        chosen_constants=dict(local_start=192,exact_chart_port=224,
                              gamma='h/2',cutoff_exponent=6144,
                              c_star='2^-256',C_star='2^320',
                              state_radius='2^-1900',parameter_radius='2^-1924',
                              low46_height_radius='2^-1947'),
        epsilon_normalized=dict(exact=str(en),decimal=float(en)),
        numerical_linear_diagnostic=diagnostics,
        input_hashes={str(args.linear_report):hashlib.sha256(linear_raw).hexdigest(),
                      str(args.tail_response):hashlib.sha256(tail_raw).hexdigest()},
        entrypoint_sha256=own_hash,
        scope='Exact constant comparisons for the full F224 proof; the separate floating diagnostic is not a shallow nonlinear match.',
    )
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],checks=len(checks),
                          failed=[k for k,v in checks.items() if not v],
                          linear_only_log2_z_F224=z224,
                          linear_only_margin_bits=diagnostics['numerical_margin_to_2pow_minus1947'],
                          output=str(args.out))))
    if not all(checks.values()):raise SystemExit(1)


if __name__=='__main__':
    main()
