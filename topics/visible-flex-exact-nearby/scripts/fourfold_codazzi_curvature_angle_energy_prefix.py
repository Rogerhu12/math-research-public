#!/usr/bin/env python3
"""Full Fourier Cauchy energy for the actual reciprocal candidate on [0,.2].

All radial candidate polynomials, the actual compact target, both means,
and exact dyadic coordinate-jump fees are retained. The estimate uses the
complete curvature-angle energy identity, not a finite Fourier inverse.
It does not cross the turning point or solve the full boundary problem.
"""
from __future__ import annotations
import argparse,gzip,json,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_metric_defect import record,save,sha


def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))
def dyadic(x):return Fraction.from_float(float(x))


def bump_jets(left,right):
    a,b=Fraction(1,20),Fraction(9,50)
    if right<=a or left>=b:return arb(0),arb(0),arb(0)
    if left<a or right>b:raise ValueError('a complete box crosses a compact bump seam')
    width=exact_arb(b-a);t=(real_interval(left,right)-exact_arb(a))/width
    p=t*(1-t);z=1-2*t
    return 4096*p**6,24576*p**5*z/width,24576*p**4*(5*z*z-2*p)/(width*width)


def target_bounds(row,left,right,nu):
    q={k:box_from_record(row['true_target_coefficients'][k]) for k in ('a','a1','a2','E','E1','K','K1','beta')}
    a,a1,a2,E,E1,K,K1,beta=(q[k] for k in ('a','a1','a2','E','E1','K','K1','beta'))
    h,h1,h2=bump_jets(left,right);ee=(nu*h).exp();En=E*ee
    N=K+nu*beta*h1/(2*E);betap=a2/a-beta*beta
    Np=K1+nu*(betap*h1+beta*h2)/(2*E)-nu*beta*h1*E1/(2*E*E)
    Kn=N/ee;Knp=(Np-nu*h1*N)/ee
    gap=En-a1*a1
    if not a>0 or not En>0 or not gap>0 or not Kn<0:
        raise ValueError('the entire new-target negative rotational chart is unresolved')
    s=-a*(En/gap).sqrt();sr=beta*s*(1-Kn*s*s)
    return dict(gamma=En.sqrt()/a,beta=beta,K=Kn,K1=Knp,s=s,s1=sr)


def polynomial_ranges(saved,nodes,j,left,right):
    t=real_interval(left-nodes[j],right-nodes[j]);cc=saved['piece_coefficients'][:,j,:]
    values=[];derivatives=[]
    for col in cc.T:
        c=[arb(float(x)) for x in col]
        values.append(((c[0]*t+c[1])*t+c[2])*t+c[3])
        derivatives.append((3*c[0]*t+2*c[1])*t+c[2])
    return values,derivatives


def absolute_sum(values,weights=None):
    if weights is None:return sum((abs(x) for x in values),arb(0)).upper()
    return sum((abs(x)*w for x,w in zip(values,weights)),arb(0)).upper()


def actual_jump(saved,nodes,j):
    left=saved['piece_coefficients'][:,j-1,:];right=saved['piece_coefficients'][-1,j,:]
    h=nodes[j]-nodes[j-1];out=[]
    for col,z in zip(left.T,right):
        q=dyadic(col[0])
        for x in col[1:]:q=q*h+dyadic(x)
        out.append(dyadic(z)-q)
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--target',type=Path,default=Path('notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz'))
    ap.add_argument('--type-cover',type=Path,default=Path('notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve every complete full-energy attempt')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));native=read(args.target);types=read(args.type_cover)
    if (meta['coordinates']!=COORDINATES or meta['object_sha256']!=native['object_sha256']
        or not native['complete'] or native['exact_requested_interval']!=['0','1/5']
        or not types['complete'] or not types['exactly_one_real_K_root']
        or types['inputs'].get(str(args.target))!=sha(args.target)):
        raise ValueError('complete same-object target/candidate/type inputs are required')
    nuq=Fraction(meta['exact_float_nu']);nulo,nuhi=map(Fraction,types['exact_nu_interval'])
    if not nulo<=nuq<=nuhi or nuq!=dyadic(meta['nu']):raise ValueError('actual fixed nu is outside the proved type interval')
    alpha=exact_arb(dyadic(meta['amplitude']));nu=exact_arb(nuq);m=int(meta['modes']);freq=list(range(4,4*m+1,4))
    nodes=list(map(dyadic,saved['radial_nodes']));right=Fraction(1,5)
    target_nodes=[Fraction(row['interval'][0]) for row in native['rows']]+[right]
    cuts=sorted({Fraction(0),right,Fraction(1,20),Fraction(9,50)}|
        {q for q in nodes if 0<q<right}|{q for q in target_nodes if 0<q<right})
    if nodes[0]!=0 or nodes[-1]<right:raise ValueError('no extrapolation outside the actual candidate')
    doc=dict(kind='actual_full_Fourier_curvature_angle_energy_prefix',complete=False,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.candidate,args.target,args.type_cover)},
        object_sha256=meta['object_sha256'],candidate_metadata=meta,actual_fixed_nu=str(nuq),
        exact_amplitude=str(dyadic(meta['amplitude'])),exact_interval=['0','1/5'],
        parameter_half_width=native['parameter_half_width'],whole_affine_parameter_interval=True,
        complete_primitive_tail=True,all_Fourier_variations_retained=True,both_mean_variations_retained=True,
        rows=[],jumps=[],failure=None,turning_connection_not_proved=True,full_body_BVP_inverse_not_proved=True,
        original_finite_BVP_outcome_not_changed=True,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_reciprocal_candidate_tools.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_beta_bulk_interval.py',
            'fourfold_phase_metric_defect.py')})
    forward=arb(0);backward=arb(0);gap_by_piece={};last=time.monotonic()
    try:
        for index,(left,end) in enumerate(zip(cuts,cuts[1:])):
            j=min(bisect_right(nodes,left)-1,len(nodes)-2);k=bisect_right(target_nodes,left)-1
            row=native['rows'][k];tl,tr=map(Fraction,row['interval'])
            if not nodes[j]<=left<end<=nodes[j+1] or not tl<=left<end<=tr:
                raise ValueError('common exact target/candidate refinement failed')
            a=target_bounds(row,left,end,nu);y,yr=polynomial_ranges(saved,nodes,j,left,end)
            U=abs(alpha)*absolute_sum(y[:m]);Ut=abs(alpha)*absolute_sum(y[:m],freq)
            Vt=abs(alpha)*absolute_sum(y[m+1:],freq);Vne=absolute_sum(y[m+1:]);Vrne=absolute_sum(yr[m+1:])
            v=a['s']+alpha*(y[m]+arb(0,Vne));vr=a['s1']+alpha*(yr[m]+arb(0,Vrne))
            if not v<0:
                doc['failed_row']=dict(interval=[str(left),str(end)],candidate_piece=j,native_row=k,
                    v=record(v));raise ValueError('complete Fourier negative v enclosure is unresolved')
            gap=(-v.upper()).lower();vmax=(-v.lower()).upper();gap_by_piece[j]=min(gap_by_piece.get(j,gap),gap).lower()
            t=vr/v;osc=(t.upper()-t.lower()).upper()
            quadratic_u=arb(0).union((U*U).upper())
            quadratic_v=(gap*gap).lower().union((vmax*vmax).upper())
            angular=arb(0,Ut);cross=arb(0,(U*Vt/gap).upper());mean_fee=arb(0,osc/2)
            G1=a['gamma']*(angular+cross)/2-a['beta']*(1+3*quadratic_u+a['K']*quadratic_v)+mean_fee
            G2=a['gamma']*(-3*angular+cross)/2+a['beta']*(1-quadratic_u-3*a['K']*quadratic_v)+a['K1']/(2*a['K'])+mean_fee
            gf=max(arb(0),G1.upper(),G2.upper()).upper();gb=max(arb(0),-G1.lower(),-G2.lower()).upper()
            length=exact_arb(end-left);forward=(forward+length*gf).upper();backward=(backward+length*gb).upper()
            doc['rows'].append(dict(interval=[str(left),str(end)],candidate_piece=j,native_row=k,
                actual_scalar_germ=row['actual_scalar_germ'],v=record(v),v_abs_lower=record(gap),
                actual_K=record(a['K']),actual_K1=record(a['K1']),gamma=record(a['gamma']),beta=record(a['beta']),
                full_U_A0=record(U),full_u_theta_A0=record(Ut),full_v_theta_A0=record(Vt),
                v_r_over_v=record(t),v_r_over_v_oscillation_upper=record(osc),
                energy_diagonal_1=record(G1),energy_diagonal_2=record(G2),
                forward_log_rate=record(gf),backward_log_rate=record(gb),
                cumulative_forward_log=record(forward),cumulative_backward_log=record(backward)))
            if time.monotonic()-last>20:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(rows=len(doc['rows']),right=str(end),forward=forward.str(10),backward=backward.str(10)),flush=True);last=time.monotonic()
        logjump=arb(0)
        for j in range(1,len(nodes)-1):
            if not 0<nodes[j]<right:continue
            delta=actual_jump(saved,nodes,j)
            dv=(abs(alpha)*sum((abs(exact_arb(z)) for z in delta[m:]),arb(0))).upper()
            gap=min(gap_by_piece[j-1],gap_by_piece[j]).lower();eps=(dv/gap).upper()
            if not eps<1:raise ValueError('an exact physical coordinate jump loses the energy comparison')
            fee=(((1+eps)/(1-eps)).log()/2).upper();logjump=(logjump+fee).upper()
            doc['jumps'].append(dict(radius=str(nodes[j]),full_exact_v_jump_A0=record(dv),
                adjacent_negative_v_gap=record(gap),relative_jump=record(eps),sqrt_energy_log_fee=record(fee)))
        doc.update(complete=True,all_continuous_radial_boxes_passed=True,all_exact_PPoly_interfaces_paid=True,
            bounds={k:record(z) for k,z in dict(forward_log_integral=forward,backward_log_integral=backward,
                exact_coordinate_jump_log_fee=logjump,forward_energy_norm_Cauchy_gain=(forward+logjump).exp().upper(),
                backward_energy_norm_Cauchy_gain=(backward+logjump).exp().upper(),
                minimum_actual_v_abs=min(gap_by_piece.values()).lower()).items()})
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),jumps=len(doc['jumps']),
        bounds=doc.get('bounds'),wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
