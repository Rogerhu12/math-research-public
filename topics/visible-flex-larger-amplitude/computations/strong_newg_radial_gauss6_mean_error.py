#!/usr/bin/env python3
"""Pay the actual positive Gauss6 radial mean rule on every original interval.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
At every exact production angle, enclose Vz and its full s derivative on
whole actual radial boxes. A positive-weight Wasserstein/Peano bound pays
Gauss6 after subtracting the best constant derivative interval midpoint.
The explicit repaired field is C2 across the original seams. All original
cells and every possible final partial cell use one zero-height anchor.
The angular alias, original libm/evaluation and affine-node rounding remain
separate. No high-order derivative or ideal Gauss-table accuracy is assumed.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import ast
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import textwrap
import time
import numpy as np

HERE=Path(__file__).resolve().parent
ORIGINAL=HERE/'strong_newg_complex_angular_mean_strip.py'
ORIGINAL_SHA='013a0355bbd7a85d4fe64cabda6faa3140929caf85335986a44f083fe29be336'
HEIGHT_SOURCE_SHA='e621ee2e9e8a706332b3839122a8ec57e1c5c2cfe82a48a759dcdad0548c54b2'
HEIGHT_FUNCTION_SHA='ad9ba92e667ebbf572c6d31622959b804aba482d506e6523a7538e33569cd282'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def dy(z):return F(int(z[0]))*F(2)**int(z[1])
def rat(q):q=F(q);return {'numerator':str(q.numerator),'denominator':str(q.denominator)}
def binary(x):return F.from_float(float(x))


REAL_RETURN='''        # All actual angles here are real. Extracting their enclosed real
        # parts is exact even if outward arithmetic put tiny intervals on zero.
        pr,psr,wr,wsr,dr,dsr=[q[0] for q in (P,Ps,W,Ws,D,Ds)]
        ur,usr,vr,vsr=[q[2][0] for q in (U,Us,V,Vs)]
        cc=cvecdot(U,V)[0]
        ccs=ca(cvecdot(Us,V),cvecdot(U,Vs))[0]
        az=R.sub(R.mul(pr,vr),R.mul(cc,ur))
        azs=R.sub(R.add(R.mul(psr,vr),R.mul(pr,vsr)),R.add(R.mul(ccs,ur),R.mul(cc,usr)))
        zr,zsr=Z[2][0],Zs[2][0]
        root=VERIFIED_REAL_SQRT(dr)
        numerator=R.add(R.neg(R.mul(R.mul(t,pr),az)),R.mul(root,zr))
        numerator_s=R.add(R.neg(R.add(R.mul(R.add(R.mul(ts,pr),R.mul(t,psr)),az),R.mul(R.mul(t,pr),azs))),
                          R.add(R.mul(R.div(dsr,R.mul(R.const(2),root)),zr),R.mul(root,zsr)))
        normal=R.div(numerator,wr)
        normal_s=R.sub(R.div(numerator_s,wr),R.div(R.mul(numerator,wsr),R.square(wr)))
        nur=R.div(R.mul(bp,Q[0]),rho[0])
        nusr=R.sub(R.div(R.mul(bpp,Q[0]),rho[0]),R.div(R.mul(R.mul(R.square(bp),Q[0]),qp[0]),R.square(rho[0])))
        value=R.add(normal,R.mul(R.mul(nur,radius),ur))
        derivative=R.add(normal_s,R.add(R.mul(R.mul(nusr,radius),ur),R.mul(nur,R.add(R.mul(t,ur),R.mul(radius,usr)))))
        means=[R.div(R.isum(v),R.const(N)) for v in (value,derivative)]
        record.update(exact_N_point_mean_value_derivative_intervals=[[str(binary(x)) for x in v] for v in means],
                      all_N_exact_mean_angles_enclosed_on_the_whole_radial_interval=True)
        return True,record
'''


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('background','state-repair','radial','table','background-source','domain','primary','height-source','out'):
        p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh complete radial Gauss6 certificate required')
    if sha(ORIGINAL)!=ORIGINAL_SHA or sha(a.height_source)!=HEIGHT_SOURCE_SHA:
        raise ValueError('Actual original interval construction or height source changed')
    heights=a.height_source.read_text();functions=[n for n in ast.walk(ast.parse(heights)) if isinstance(n,ast.FunctionDef) and n.name=='height_integral']
    if len(functions)!=1:raise ValueError('Unique original height integration function required')
    n=functions[0];height=textwrap.dedent(''.join(heights.splitlines(keepends=True)[n.lineno-1:n.end_lineno]))
    if hashlib.sha256(height.encode()).hexdigest()!=HEIGHT_FUNCTION_SHA:raise ValueError('Original positive per-cell Gauss6 rule changed')
    source=ORIGINAL.read_text();changes=[
        ("psi=2*arb.pi()*context['helper'].interval(F(j,N),F(j+1,N))",'psi=2*arb.pi()*aq(F(j,N))'),
        ('ts=np.array([-R.qi(ts_cap)[1],R.qi(ts_cap)[1]])','ts=ACTUAL_SECOND_INTERVAL(piece,left,right)'),
    ]
    transformed=source
    for old,new in changes:
        if transformed.count(old)!=1:raise ValueError('Exact original mean construction moved')
        transformed=transformed.replace(old,new,1)
    first=transformed.index('        def cap(z):');last=transformed.index('    records=[];failed=[];',first)
    saved_tail=transformed[first:last]
    transformed=transformed[:first]+REAL_RETURN+'    return locals()\n'+transformed[last:]
    restored=transformed.replace(REAL_RETURN+'    return locals()\n',saved_tail,1)
    for old,new in reversed(changes):restored=restored.replace(new,old,1)
    if restored!=source:raise ValueError('Exact quadrature/derivative adapter reversal failed')
    ns={'__file__':str(ORIGINAL),'__name__':'actual_signed_radial_mean_context'}
    exec(compile(transformed,'<actual-signed-radial-mean-context>','exec'),ns)
    argv=sys.argv;sys.argv=[argv[0]]
    for key in ('background','state_repair','radial','table','background_source','domain','primary','out'):
        sys.argv+=['--'+key.replace('_','-'),str(getattr(a,key))]
    try:c=ns['main']()
    finally:sys.argv=argv
    R=c['R'];helper=c['context']['helper'];aq=ns['aq'];upper=ns['upper'];arb=ns['arb']
    sqrt_checks=0
    def verified_sqrt(v):
        nonlocal sqrt_checks
        if np.any(v[0]<=0):raise ArithmeticError('Positive actual square-root interval required')
        lo=R.down(np.sqrt(v[0]));hi=R.up(np.sqrt(v[1]))
        # Squared endpoint inequalities are checked with outward basic
        # arithmetic; validity does not assume a libm error constant.
        for unused in range(8):
            badlo=R.up(lo*lo)>v[0];badhi=R.down(hi*hi)<v[1]
            if not np.any(badlo|badhi):break
            lo=np.where(badlo,R.down(lo),lo);hi=np.where(badhi,R.up(hi),hi)
        if np.any(R.up(lo*lo)>v[0]) or np.any(R.down(hi*hi)<v[1]):
            raise ArithmeticError('Actual sqrt endpoints failed their squared rational-side test')
        sqrt_checks+=2*v.shape[1]
        return np.array([lo,hi])
    def second_interval(piece,left,right):
        seg=piece['seg'];L=piece['L'];h=piece['h'];u0=(left-piece['s0'])/h;u1=(right-piece['s0'])/h
        if seg['kind']=='hermite':
            b=ns['binary'](seg['k0'])*L;V=ns['binary'](seg['v1']);cc=3*V-2*b;d=b-2*V
            value=aq(L/h**2)*helper.polyeval([b,2*cc,3*d],helper.interval(u0,u1))
        else:
            lo,hi,unused=piece['piece'];span=hi-lo;tt=helper.interval((u0-lo)/span,(u1-lo)/span)
            norm=piece['norm'];phase=helper.polyeval(norm,tt);derivative=[j*v for j,v in enumerate(norm) if j]
            value=aq(L/(h*h*span))*phase.cos()*helper.polyeval(derivative,tt)
            value+=arb(0,aq(dy(piece['row']['Gauss_derivative_comparison_first_second_upper'][1])))
        value+=arb(0,aq(dy(piece['row']['quintic_repair_uniform_C0_C1_C2_upper'][2])))
        return R.ai(value)
    ns['VERIFIED_REAL_SQRT']=verified_sqrt;ns['ACTUAL_SECOND_INTERVAL']=second_interval
    domain=c['domain'];rows=[];failed=[];cursor=F(0);cells={};N=1360
    for i,row in enumerate(domain['rows']):
        left,right=map(F,row['s_interval'])
        if left!=cursor:raise ArithmeticError('Complete actual radial coverage has a gap')
        Y,Ys=c['states_on'](row['original_interval'],left,right)
        ok,data=c['enclose'](row,Y,Ys,F(0),N)
        record=dict(atom=i,original_interval=row['original_interval'],background_piece=row['background_piece'],
            s_interval=row['s_interval'],positive_domain=ok,**data)
        rows.append(record);cursor=right
        if ok:
            value,derivative=[list(map(F,z)) for z in data['exact_N_point_mean_value_derivative_intervals']]
            j=row['original_interval']
            if j not in cells:cells[j]=dict(value=value,derivative=derivative,atoms=[])
            else:
                for key,new in [('value',value),('derivative',derivative)]:
                    cells[j][key]=[min(cells[j][key][0],new[0]),max(cells[j][key][1],new[1])]
            cells[j]['atoms'].append(i)
        else:failed.append(i)
        if len(rows)%128==0:print(json.dumps(dict(event='actual_whole_radial_mean_gauss6_progress',atoms=len(rows),failed=len(failed),rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    complete=cursor==c['L'] and len(rows)==3326;passed=complete and not failed
    g,w=np.polynomial.legendre.leggauss(6)
    nodes=[(1+binary(x))/2 for x in g];raw_weights=[binary(x)/2 for x in w];mass=sum(raw_weights);weights=[x/mass for x in raw_weights]
    if not (len(nodes)==6 and nodes==sorted(nodes) and 0<nodes[0]<nodes[-1]<1 and min(weights)>0 and sum(weights)==1):
        raise ArithmeticError('Actual positive six-point probability table failed')
    W1=F(0);location=F(0);cdf=F(0)
    for node,weight in [*zip(nodes,weights),(F(1),F(0))]:
        if cdf<=location:fee=(node*node-location*location)/2-cdf*(node-location)
        elif cdf>=node:fee=cdf*(node-location)-(node*node-location*location)/2
        else:fee=((cdf-location)**2+(node-cdf)**2)/2
        if fee<0:raise ArithmeticError('Positive exact transport contribution failed')
        W1+=fee;location=node;cdf+=weight
    moment=abs(sum(x*y for x,y in zip(nodes,weights))-F(1,2));mass_error=abs(mass-1)
    mesh=list(map(binary,c['primary']['mesh']));payments=[];total=F(0)
    if passed:
        if set(cells)!=set(range(len(mesh)-1)):raise ArithmeticError('An original Gauss6 cell was omitted')
        for i in range(len(mesh)-1):
            cell=cells[i];h=mesh[i+1]-mesh[i];lo,hi=cell['derivative'];middle=(hi+lo)/2;oscillation=(hi-lo)/2
            fcap=max(map(abs,cell['value']))
            peano=h*h*(oscillation*W1+abs(middle)*moment);normalization=h*fcap*mass_error
            fee=peano+normalization;total+=fee
            payments.append(dict(original_interval=i,physical_interval=[str(mesh[i]),str(mesh[i+1])],
                complete_source_atoms=cell['atoms'],mean_value_interval=list(map(str,cell['value'])),
                mean_derivative_interval=list(map(str,cell['derivative'])),
                exact_derivative_midpoint=str(middle),exact_derivative_radius=str(oscillation),
                radial_quadrature_error_upper=upper(aq(fee)),exact_error_before_rounding=str(fee),
                same_bound_covers_every_final_partial_cell=True))
    out=dict(schema='actual-q106-complete-positive-Gauss6-radial-mean-error-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        original_complex_source_sha256=ORIGINAL_SHA,original_height_function_sha256=HEIGHT_FUNCTION_SHA,
        exact_reversible_signed_mean_context_sha256=hashlib.sha256(transformed.encode()).hexdigest(),
        input_sha256={**c['inputs'],str(a.height_source):HEIGHT_SOURCE_SHA},
        primary_sha256=domain['primary_sha256'],background_comparison_definition_sha256=domain['background_comparison_definition_sha256'],
        state_comparison_definition_sha256=domain['state_comparison_definition_sha256'],
        complete_radial_cover=complete,all_domain_and_quadrature_gates=passed,complete_atoms=len(rows),failed_atoms=failed,
        whole_radial_interval_mean_rows=rows,exact_mean_angular=N,verified_square_root_endpoint_inequalities=sqrt_checks,
        numpy_version=np.__version__,actual_binary_gauss_table=[dict(node=rat(x),raw_weight=rat(y),normalized_weight=rat(z)) for x,y,z in zip(nodes,raw_weights,weights)],
        exact_table_mass=rat(mass),exact_weight_mass_error=rat(mass_error),exact_normalized_first_moment_defect=rat(moment),
        exact_unit_interval_Wasserstein1=rat(W1),per_original_cell=payments,
        full_anchored_radial_quadrature_H_error_upper=upper(aq(total)) if passed else None,
        full_anchored_radial_quadrature_H_error_display=float(total) if passed else None,
        mean_scope='Exact production N=1360 angular mean on the explicit C2 comparison, then the actual binary positive radial six-node table interpreted exactly.',
        bound_formula='h^2*(W1*(dmax-dmin)/2 + abs((dmax+dmin)/2)*moment_defect) + h*value_cap*abs(table_mass-1)',
        partial_cell_scope='Prefix uses complete previous original cells and one final subinterval; its h and h^2 bounds are no larger than that original cell, so the sum of all original-cell fees is uniform in final s.',
        no_cellwise_anchor_reset=True,angular_alias_paid_here=False,
        original_floating_node_affine_arithmetic_libm_or_coordinate_alignment_paid=False,
        original_g_PDE_reach_or_closed_surface_certified=False,new_ODE_Node_Newton_calls=0,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    with a.out.open('wb') as f:
        with gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0) as z:z.write((json.dumps(out,separators=(',',':'))+'\n').encode())
    print(json.dumps(dict(event='actual_whole_radial_gauss6_mean_finished',all_gates=passed,atoms=len(rows),failed=len(failed),
        H_error=out['full_anchored_radial_quadrature_H_error_display'],path=str(a.out),sha256=sha(a.out))),flush=True)

if __name__=='__main__':main()
