"""Exact angular Cauchy trace rebase, using the actual complete signed Fourier polynomials at the root."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from hashlib import sha256
from importlib.metadata import version
from math import factorial
from pathlib import Path
import json,os,subprocess,sys
from flint import acb,arb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as A
import fourfold_codazzi_true_characteristic_seed_admission as S
from fourfold_codazzi_exterior_signed_potential_moment import edges,PRE,PRE_SHA
from fourfold_codazzi_variable_cutoff_moments import coefficients,L
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_ratio_live_rules import canonical,gate
from fourfold_codazzi_true_ratio_prefix import replace,record_failure
from fourfold_codazzi_true_phase_original_inputs import check

WIDTH=Q(1,512)
ORDER=4
N=388


def fields(read):
    names=['complete-background-root-series','leading-complete-a0','leading-complete-Q','first-correction-degree-000','first-correction-degree-001']
    for k in range(9,15):names+=['background-inputs-degree-%03d'%k,'background-main-degree-%03d'%k]
    ss,_,ids=S.admit(read,names);bg=ss[names[0]]
    check(all(bg[k] for k in ('complete_mean_at_all_orders_retained','positive_order_value_repair_derivatives_exactly_zero',
          'original_65_and_193_rows_retained','zero_bump_germ_and_fixed_eta0')),'same real physical family and all finite coordinates')
    c={k:A.unpack_series(v) for k,v in bg['series'].items()}
    for n in range(9,15):
        i=ss['background-inputs-degree-%03d'%n];m=ss['background-main-degree-%03d'%n]
        check(i['degree']==m['degree']==n,'original complete true signed root degree')
        for k in ('K','beta','gamma','s','u','v','k'):c[k].append(A.LP.restore(i['coefficients'][k]))
        for k in ('eta','a'):c[k].append(A.LP.restore(m[k]))
    a0=A.unpack_series(ss[names[1]]['coefficients']);q=A.unpack_series(ss[names[2]]['coefficients'])[0].scalar_value()
    w=[[A.LP.restore(ss['first-correction-degree-%03d'%k][key]) for k in range(2)] for key in ('a1','b1')]
    a,b=w;d=c['d'][0]
    check(a0[0].coefficient(0).contains(1) and all(z.contains(0) for k,z in enumerate(a0[0].c,a0[0].lo) if k)
          and all(z.contains(0) for z in a[0].c) and q.imag.contains(0) and q.real.lower()>0,'true root normalization and positive DT')
    # SE.9 makes both angular drifts of a0 and a1 exactly zero at the root.
    return c,(q.real,-a0[1],-a[1],b[0],-b[1]-d*b[0].theta()),ids


def add(*zs):return [sum(r,arb(0)).upper() for r in zip(*zs)]
def mul(a,b):return [sum((a[i]*b[j-i] for i in range(j+1)),arb(0)).upper() for j in range(ORDER+1)]
def times(a,v):return [(b*v).upper() for b in a]
def norm(a):return [(a.norm(WIDTH,j)/factorial(j)).upper() for j in range(ORDER+1)]


def readback(c,row):
    lam,u,a,b,bp=row;zero=arb(0);one=arb(1)
    # The full unit disk in zeta gives the original closed z square.
    h=arb(0,exact(Q(1,9409)).upper());co=coefficients(c,acb(h,h))
    V=co[0];V1=-co[1]/exact(3*L)
    gamma=b+V
    d0=bp-b*u;d1=-b*a
    g0=(norm(d0));g1=norm(d1);m=exact(Q(1,N));cn=lam.lower()
    defect=times(add(g0,times(g1,m)),m*m)
    gap=(cn-defect[0]).lower()
    if gap<=0:return dict(inverted=False,root_c=edges(lam),Wiener_subtracted_gap=edges(gap))
    # Normalized positive derivative convolution for inverse of the whole original symbol.
    inv=[one/gap]
    for j in range(1,ORDER+1):inv.append((sum((defect[i]*inv[j-i] for i in range(1,j+1)),zero)/gap).upper())
    S0=gamma.scale(V1);T=gamma.scale(V*lam);H=a.scale(V)
    # Combine the complete signed amplitude before the common norm, including the mean.
    W=d0.scale(-V1)+gamma.scale(V*V*lam)-V1*V1*lam
    X=(a*gamma).scale(V1)
    ss,tt,hh,bb=map(norm,(S0,T,H,b));wx=add(norm(W),times(norm(X),m))
    # tilde E = n^(8/3) diag(1,n^(-2/3)) M_F^-1 E diag(1,n^(2/3)).
    m13=m.root(3)
    y11=times(mul(mul(bb,tt),inv),m13**4)
    y12=add(times(ss,m13**2),times(mul(mul(bb,hh),inv),m13**5),
            times(mul(mul(bb,wx),inv),m13**8))
    y21=mul(tt,inv)
    y22=add(times(mul(hh,inv),m13),times(mul(wx,inv),m13**4))
    # Sum entries before the lag-wise supremum: this bounds the full uniform
    # matrix Wiener majorant even when the maximizing input labels differ.
    upper=[(3*sum(vals,arb(0))).upper() for vals in zip(y11,y12,y21,y22)]
    phys=[(v*m13**8).upper() for v in upper]
    return dict(inverted=True,root_c=edges(lam),root_V_box=[edges(V.real),edges(V.imag)],root_Bprime_box=[edges(V1.real),edges(V1.imag)],
           Wiener_subtracted_gap=edges(gap),normalized_real_angle_derivatives_full_inverse_denominator=[edges(v)[1] for v in inv],
           relative_determinant_defect_upper=edges(defect[0]/cn)[1],analytic_width=str(WIDTH),
           normalized_weighted_angular_derivative_caps_of_n8over3_correction=[edges(v)[1] for v in upper],
           normalized_weighted_angular_derivative_caps_of_actual_correction=[edges(v)[1] for v in phys],
           complete_angle_trace_correction_under_one_percent=bool(phys[0]<exact(Q(1,100))),
           complete_angle_trace_correction_under_one_tenth=bool(phys[0]<exact(Q(1,10))))


def run(a):
    check(os.environ['GITHUB_ACTIONS']=='true' and os.environ['GITHUB_REPOSITORY']=='Rogerhu12/math-research-public'
          and os.environ['GITHUB_RUN_ATTEMPT']=='1' and sys.version_info[:3]==(3,12,14) and version('python-flint')=='0.9.0','original contour-root public single scientific entry')
    gate();ctx.prec=320
    raw=(a.repo/PRE).read_bytes();check((len(raw),sha256(raw).hexdigest())==(27645,PRE_SHA),'original common scalar root qualification')
    v=json.loads(raw);s=v['actual_scientific_receipt'];case=s['cases'][0]
    check(v['actual_returncode']==0 and v['complete'] and s['proved'] and s['complete'] and case['proved'] and case['complete']
          and case['exact_complex_z_square_halfwidth']=='1/9409' and case['fixed_intrinsic_parameter']=='eta_0'
          and all(g['passed'] for g in s['gates']),'same original complete frequency square')
    def read(c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=a.repo)
    c,inputs,ids=fields(read);check(len(ids)==23,'all unique historical native files and full 17 original field stages')
    d=readback(c,inputs)
    cert=dict(kind='R149_true_matched_full_angular_root_Cauchy_traces',run=os.environ['GITHUB_RUN_ID'],attempt=1,
         event_commit=os.environ['GITHUB_SHA'],complete=True,proved=True,physical_frequency_floor=388,
         complete_two_state_matching_qualified=d['inverted'],exact_root_physical_state_error_zero=d['inverted'],
         original_input_count=len(ids),original_receipts_sha256=sha256(canonical(ids)).hexdigest(),original_potential_sha256=PRE_SHA,
         old_scientific_targets_recomputed=0,negative_volume_or_positive_Poisson_or_full_high_inverse_claimed=False,
         actual=d,last_rule_read_head=gate())
    replace(a.receipt,canonical(cert));print('GRT_WHOLE_SMALL_RECEIPT',canonical(cert).decode().strip(),flush=True)


if __name__=='__main__':
    p=ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--receipt',type=Path,required=True);a=p.parse_args()
    try:run(a)
    except Exception as exc:
        record_failure(a.receipt,exc)
        raise
