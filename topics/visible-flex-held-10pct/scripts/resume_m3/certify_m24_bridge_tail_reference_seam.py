#!/usr/bin/env python3
"""Unify the actual bridge target metric with the true 4.625 tail cut.

The R60 surface and its mean remain unchanged.  A precisely defined final
length-L Hermite correction changes only the target radius, matches the true
tail's arc-length radius two-jet, and has zero two-jet at its left endpoint.
This is an explicitly new global reference metric, not an assertion that the
previous rounded source profile or a missing nonrotating tail already agrees.
"""
import argparse,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
from fractions import Fraction as Q
from math import comb

def module(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(sp);sys.modules[name]=mod;sp.loader.exec_module(mod);return mod
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def fq(x):return Q.from_float(float(x))
def outward_upper(x):
    y=float(x)
    return math.nextafter(y,math.inf) if fq(y)<x else y
def literal(x):
    x=str(x)
    if x.startswith('np.float64(') and x.endswith(')'):x=x[len('np.float64('):-1]
    return fq(float(x))
def der(p):return [(k+1)*p[k+1] for k in range(len(p)-1)]
def val(p,x):
    v=Q(0)
    for c in p[::-1]:v=v*x+c
    return v
def bernstein_sup(p):
    n=len(p)-1
    return max(abs(sum((p[j]*Q(comb(k,j),comb(n,j)) for j in range(k+1)),Q(0))) for k in range(n+1))

H=[[Q(1),0,0,-Q(10),Q(15),-Q(6)],
   [0,Q(1),0,-Q(6),Q(8),-Q(3)],
   [0,0,Q(1,2),-Q(3,2),Q(3,2),-Q(1,2)]]

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('source-run','physical','bridge-jet-certificate','tail-constants',
                 'tail-normalization-certificate','tail-oracle','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--length',default='1/1000')
    a=p.parse_args();start=time.monotonic();L=Q(a.length)
    run=json.loads(a.source_run.read_text());old=json.loads(a.bridge_jet_certificate.read_text())
    assert old['status']=='exact_moment_and_true_parameter_bounds_passed'
    assert old['run_sha256']==sha(a.source_run)
    mod=module('_bridge_reference_true_tail',a.tail_oracle)
    tail=mod.Q060TrueBackgroundOracle(a.tail_constants,a.tail_normalization_certificate,digits=80)
    cut=tail.at_source(0,8,Q(1));assert tail.evaluations==0
    Rc=fq(tail.constants['parameters']['rCut']);wc=fq(tail.constants['parameters']['wCut'])
    wr=-7*wc/Rc;E=1+wc*wc
    assert Rc==fq(run['physical_tail_cut']['radius'])
    q=tail.qi;iv=tail.iv
    # These exact cut identities are supplied by the bound true oracle; the
    # real normalization parameter is not replaced by a floating midpoint.
    for key,target in [('r',Rc),('w',wc),('h_RR',wr),('E',E),('E_R',2*wc*wr)]:
        target=q(target)
        assert tail.lo(cut[key])<=tail.lo(target) and tail.hi(cut[key])>=tail.hi(target)
    params=old['source_parameters']
    peak,eps,L1,L2,L3=[literal(params[key]) for key in ('peak','eps','L1','L2','L3')]
    span=Q(old['source_endpoints']['exact_span'])
    assert 0<L<L3 and span>L1+L2
    u=(span-L1-L2)/L3
    phi=peak-eps*u*u;phip=-2*eps*u/L3
    actual_first=-iv.sin(q(phi));actual_second=-iv.cos(q(phi))*q(phip)
    true_first=-1/iv.sqrt(q(E));true_second=q(-wc*wr/E**2)
    d1=true_first-actual_first;d2=true_second-actual_second
    def absupper(x):return max(abs(mod.mpf_fraction(tail.lo(x))),abs(mod.mpf_fraction(tail.hi(x))))
    # Reuse the already executed complete-bridge integral comparison.  Add
    # both sides of its comparison triangle, and the literal plateau-sine
    # coefficient error; this deliberately conservative sum avoids any new
    # background integration.
    upper=lambda row:Q(row['upper_exact'])
    radial_gap=(upper(old['endpoint_pulled_primitive_vs_R59_piecewise_jet_bounds']['sin'][0])
        +upper(old['same_literal_parameters_primitive_physical_jet_bounds']['sin'][0])
        +abs(L2)*upper(old['frozen_plateau_trig_constant_errors']['sin']))
    assert radial_gap<Q(1,10**11)
    d=[Q(1,10**11),absupper(d1),absupper(d2)]
    coeff=[]
    for j,h in enumerate(H):
        c=h;row=[]
        for k in range(3):
            assert val(c,Q(0))==(1 if j==k else 0) and val(c,Q(1))==0
            row.append(bernstein_sup(c)*L**(j-k));c=der(c)
        coeff.append(row)
    gaps=[sum((coeff[j][k]*d[j] for j in range(3)),Q(0)) for k in range(3)]
    # True a_* is globally above .299 by the existing bridge proof.
    lower_record=old['true_primitive_radius_lower']
    assert Q(lower_record['lower_exact'])>Q(299,1000)
    new_lower=Q(299,1000)-gaps[0];assert new_lower>0
    eta=gaps[0]/new_lower
    metric_increment=2*eta+eta*eta
    old_metric=Q(93,10**8)
    new_metric=(1+eta)**2*old_metric+metric_increment
    assert new_metric<Q(9301,10**10)
    out={
        'status':'bridge_true_tail_reference_seam_certified',
        'source_sha256':sha(__file__),'source_run_sha256':sha(a.source_run),
        'physical_sha256':sha(a.physical),'bridge_jet_certificate_sha256':sha(a.bridge_jet_certificate),
        'tail_oracle_sha256':sha(a.tail_oracle),'tail_provenance':tail.provenance,
        'cut_locator':[0,8,'1'],'cut_R_exact':str(Rc),'cut_w_exact':str(wc),
        'cut_wR_exact':str(wr),'old_JS_cut_w_exact':str(fq(run['physical_tail_cut']['backgroundSlope'])),
        'old_JS_cut_wR_exact':str(fq(run['physical_tail_cut']['backgroundSecond'])),
        'old_JS_minus_true_w_exact':str(fq(run['physical_tail_cut']['backgroundSlope'])-wc),
        'old_JS_minus_true_wR_exact':str(fq(run['physical_tail_cut']['backgroundSecond'])-wr),
        'bridge_terminal_phase_exact':str(phi),'bridge_terminal_phase_derivative_exact':str(phip),
        'bridge_terminal_normalized_u_minus_one_exact':str(u-1),
        'bridge_actual_a_prime':tail.bounds(actual_first),'bridge_actual_a_second':tail.bounds(actual_second),
        'true_tail_arc_a_prime':tail.bounds(true_first),'true_tail_arc_a_second':tail.bounds(true_second),
        'true_tail_minus_bridge_a_prime':tail.bounds(d1),'true_tail_minus_bridge_a_second':tail.bounds(d2),
        'bridge_actual_a_end_contract':'Rc plus an unknown signed value in the proved radius gap; unique true primitive, not a chosen interval parameter',
        'reused_radius_gap_triangle_exact':str(radial_gap),'reused_radius_gap_triangle_upper':outward_upper(radial_gap),
        'patch_length_exact':str(L),'endpoint_radius_correction_bounds_exact':[str(x) for x in d],
        'target_radius_correction_0_1_2_upper':[outward_upper(x) for x in gaps],
        'new_radius_lower_exact':str(new_lower),'metric_radius_transfer_exact':str(metric_increment),
        'new_complete_bridge_metric_upper':outward_upper(new_metric),
        'new_complete_bridge_metric_upper_exact':str(new_metric),
        'new_reference_metric_explicit':True,'old_R60_map_and_mean_unchanged':True,
        'target_radius_common_two_jet_exact':True,'no_new_background_integrals':tail.evaluations==0,
        'nonrotating_Cartesian_tail_seam_proved':False,'full_tail_solve_asserted':False,
        'scope':'One explicit global target-g definition before freezing; not fixed-old-g refinement and not a tail-map construction',
        'seconds':time.monotonic()-start}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({key:out[key] for key in ['status','old_JS_minus_true_w_exact','old_JS_minus_true_wR_exact',
        'true_tail_minus_bridge_a_prime','true_tail_minus_bridge_a_second','reused_radius_gap_triangle_upper',
        'target_radius_correction_0_1_2_upper','new_complete_bridge_metric_upper','no_new_background_integrals','seconds']}),flush=True)
if __name__=='__main__':main()
