#!/usr/bin/env python3
"""Directed complete-time domain coverage with sharp sine endpoints.

Each actual scalar germ is covered explicitly.  Passed full-angle domains
may be inherited only after an exact-object/germ check and a directed disk
inclusion.  A false or unfinished index is not a whole-branch certificate.
No reference trajectory coefficients or actual-flow errors are computed here.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
from types import SimpleNamespace
import time

from flint import arb, ctx

from fourfold_phase_beta_affine import AffineBulkTarget, sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_field_time_germ_union import common_knots, reflected_common_domain
from fourfold_phase_field_time_refined_root import prepare_refined_root
from fourfold_phase_field_time_turn_collar import PiTime, TurnCollarTimeModel
from fourfold_phase_full_angle_time_domain import document, hashed, frame_membership, real_anchor
from fourfold_phase_full_angle_sine_domain import invariant_enclosures
from fourfold_phase_sine_time_geometry import SineGermTimeModel, sine_radial_displacement
from fourfold_phase_time_outer_taylor_gate import time_disk_range


def fraction_endpoint(value):
    return Fraction(str(value.fmpq()))


def pi_time(value):
    if isinstance(value, str):
        return PiTime(Fraction(value))
    if 'kind' in value:
        return PiTime.from_record(value)
    return PiTime(Fraction(value['rational']), Fraction(value['pi_coefficient']))


def write_report(path, report):
    path=Path(path);raw=(json.dumps(report,indent=2)+'\n').encode()
    if len(raw)>1_000_000 and path.suffix!='.gz':
        raise ValueError('a report larger than 1MB requires gzip')
    data=gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw
    if len(data)>5_000_000:raise ValueError('split a report below the repository size limit')
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.tmp');tmp.write_bytes(data);tmp.replace(path)


def sharp_cover(target,root,left,right):
    """Separate exact endpoint evaluations on the physical monotone branch."""
    if (right-left).ball()>0:a,b=left,right
    elif (left-right).ball()>0:a,b=right,left
    else:raise ValueError('time orientation is not strictly separated')
    halfpi=PiTime(Fraction(0),Fraction(1,2))
    if not (a+halfpi).nonnegative() or not (halfpi-b).nonnegative():
        raise ValueError('the actual interval leaves the physical sine branch')
    ra=-root if (a+halfpi).is_zero() else root*a.ball().sin()
    rb=root if (halfpi-b).is_zero() else root*b.ball().sin()
    lo,hi=fraction_endpoint(ra.lower()),fraction_endpoint(rb.upper())
    legal_left,legal_right=reflected_common_domain(target)
    if not legal_left<lo<=hi<legal_right:
        raise ValueError('sharp radial image leaves the actual common physical domain')
    cuts=common_knots(target)
    cells=[(a,b)for a,b in zip(cuts,cuts[1:])if a<=hi and b>=lo]
    if (not cells or not cells[0][0]<=lo<=hi<=cells[-1][1]
            or any(a[1]!=b[0]for a,b in zip(cells,cells[1:]))):
        raise ValueError('complete sharp radial germ coverage failed')
    return cells,dict(ordered_exact_time_endpoints=[a.record(),b.record()],
        radial_endpoint_balls=[ball_record(ra),ball_record(rb)],
        exact_outward_radial_bounds=[str(lo),str(hi)],
        physical_monotonicity_branch='[-pi/2,pi/2]',positive_root=ball_record(root))


def actual_anchor(model,r59):
    """Reflect according to the actual germ, also when a span meets zero."""
    left,right=model.cell
    if right<=0:reflect=True
    elif left>=0:reflect=False
    else:reflect=bool(model.center.upper()<0)
    proxy=(SimpleNamespace(cell=(-right,-left),center=-model.center,
        root=model.root,tau0=-model.tau0,h=-model.h) if reflect else model)
    u,lower,report=real_anchor(proxy,r59)
    report.update(explicit_radial_reflection_used=reflect,
        actual_germ_span=list(map(str,model.cell)),
        reflection_identity='D,W,K even and M odd; tau_center and halfwidth both reflected')
    return u,lower,report


def domain_gate(model,r59,N,K,R,S,narrow,wide,turn):
    """R65's full gate, with germ-based anchor selection at the waist."""
    started=time.monotonic();ua,base,anchor=actual_anchor(model,r59)
    alpha=abs(ua).upper();Rb,Sb=exact_arb(R),exact_arb(S)
    if not alpha<Sb:raise ValueError('the genuine germ anchor leaves the larger time disk')
    rows,coarse,KM,analytic_K,fees=invariant_enclosures(model,N,K,R,S,narrow,wide)
    D=rows[0]
    anchor_tail=(D['narrow_modulus']*(alpha/Sb)**model.precision/(1-alpha/Sb)).upper()
    variation=(sum((D['full'][i]*(Rb**i+alpha**i)for i in range(1,model.precision)),arb(0))
        +D['time_tail']+anchor_tail).upper()
    lower=(base-variation).lower()
    if turn:
        if not model.outer>=Sb:raise ValueError('turn Q is not paid on the larger time disk')
        Qrange,Qtail=time_disk_range(model.Q,Rb,Sb,abs(model.Q_outer).upper())
        positive=Qrange.real.lower();H=abs(model.eta1)*Rb
        sine=(abs(model.eta0.sin())*H.cosh()+abs(model.eta0.cos())*H.sinh()).upper()
        rt=(abs(model.root)*sine).upper();wave=(sine*abs(Qrange).sqrt()).upper()
        curvature=dict(kind='root_deflated_Q',Q_real_lower=ball_record(positive),
            Q_modulus=ball_record(abs(Qrange).upper()),full_Q_time_tail=ball_record(Qtail),
            full_radial_Q_tail=ball_record(model.Q_tail),curvature_radial_radius=ball_record(model.RK),
            exact_time_endpoint_locations=model.endpoint_locations)
    else:
        if not analytic_K:raise ValueError('ordinary curvature is not analytic on the larger disk')
        Krange,Ktail=time_disk_range(model.K,Rb,Sb,KM);positive=(-Krange).real.lower()
        rt=(abs(model.root)*(abs(model.h)*Rb).cosh()).upper();wave=abs(Krange).sqrt().upper()
        curvature=dict(kind='ordinary_negative_curvature',minus_K_real_lower=ball_record(positive),
            K_modulus=ball_record(abs(Krange).upper()),K_time_tail=ball_record(Ktail),
            K_larger_time_modulus=ball_record(KM))
    passed=bool(lower>0 and positive>0)
    row=dict(common_span=list(map(str,model.cell)),anchor=anchor,passed=passed,
        D_lower=ball_record(lower),full_D_difference_from_actual_anchor=ball_record(variation),
        curvature=curvature,time_and_Fourier_fees=fees,
        invariant_bounds={r['name']:dict(whole_strip_time_modulus=ball_record(r['modulus']),
            true_time_coefficient_norms=[ball_record(v)for v in r['full']],
            retained_DFT_coefficient_norms=[ball_record(v)for v in r['retained']],
            larger_time_narrow_angle_modulus=ball_record(r['narrow_modulus']),
            larger_time_wide_angle_modulus=ball_record(r['wide_modulus']),
            full_time_tail=ball_record(r['time_tail']))for r in rows})
    if passed:
        M,W=rows[1]['modulus'],rows[2]['modulus']
        f=(rt*(M+wave*W)/lower).upper()
        f1=(rt*((coarse['M1']+wave*coarse['W1'])/lower+
            (M+wave*W)*coarse['D1']/lower**2)).upper()
        f2=(rt*((coarse['M2']+wave*coarse['W2'])/lower+
            (2*(coarse['M1']+wave*coarse['W1'])*coarse['D1']+
             (M+wave*W)*coarse['D2'])/lower**2+
            2*(M+wave*W)*coarse['D1']**2/lower**3)).upper()
        row['true_field_moduli']={k:ball_record(v)for k,v in
            dict(f=f,f_theta=f1,f_theta2=f2,r_tau=rt,wave_factor=wave).items()}
    row['elapsed_seconds']=time.monotonic()-started
    return row


class Domains:
    def __init__(self,object_sha,root_sha):
        self.object_sha,self.root_sha=object_sha,root_sha;self.rows={};self.loaded=set()

    def add(self,path):
        path=Path(path);digest=sha(path)
        if digest in self.loaded:return
        doc=document(path)
        if (not doc.get('complete') or not doc.get('proved_full_physical_angle_and_complex_time_domain')
            or doc.get('target_object_sha256')!=self.object_sha
            or doc.get('target_root_sha256')!=self.root_sha):return
        a,b=map(pi_time,doc['exact_time_endpoints']);c,h=(a+b)/2,(b-a)/2
        R,s=Fraction(doc['time_radius']),Fraction(doc['physical_theta_strip'])
        for j,row in enumerate(doc['germs']):
            if not row.get('passed') or 'true_field_moduli' not in row:continue
            cell=tuple(map(Fraction,row['common_span']))
            for reflect in (False,True):
                key=(-cell[1],-cell[0])if reflect else cell
                self.rows.setdefault(key,[]).append(dict(path=str(path),sha256=digest,
                    row=j,cell=key,c=-c if reflect else c,h=-h if reflect else h,R=R,s=s,
                    reflect=reflect,bound=row))
        self.loaded.add(digest)

    def inherit(self,cell,c,h,R,s):
        for old in self.rows.get(cell,[]):
            if old['s']<s:continue
            identical=(c==old['c'] and (h==old['h'] or h==-old['h']) and R<=old['R'])
            if identical:
                proof=dict(identical_exact_center_and_radius=True)
            else:
                need=(abs((c-old['c']).ball())+exact_arb(R)*abs(h.ball())).upper()
                paid=(exact_arb(old['R'])*abs(old['h'].ball())).lower()
                if not need<paid:continue
                proof=dict(required_physical_time_radius=ball_record(need),
                    inherited_physical_time_radius=ball_record(paid),
                    strict_disk_inclusion_margin=ball_record((paid-need).lower()))
            bound=old['bound']
            return dict(common_span=list(map(str,cell)),passed=True,
                inherited=dict(path=old['path'],sha256=old['sha256'],germ_index=old['row'],
                    reflected_time_and_germ=old['reflect'],both_branch_signs_valid=True,**proof),
                D_lower=bound['D_lower'],curvature=bound['curvature'],
                true_field_moduli=bound['true_field_moduli'])
        return None


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--retarget',type=Path,required=True);p.add_argument('--legs',default='forward,backward')
    p.add_argument('--segments',default='all');p.add_argument('--out-directory',type=Path,required=True)
    p.add_argument('--index',type=Path,required=True);p.add_argument('--resume',action='store_true')
    p.add_argument('--seed',type=Path,action='append',default=[])
    p.add_argument('--R59',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_parameter_modulus_complex_angle_1over64.json.gz'))
    p.add_argument('--angles',type=int,default=512);p.add_argument('--cutoff',type=int,default=255)
    p.add_argument('--primitive-nodes',type=int,default=512);p.add_argument('--root-nodes',type=int,default=512)
    p.add_argument('--time-order',type=int,default=40);p.add_argument('--bits',type=int,default=160)
    p.add_argument('--time-radius',default='3');p.add_argument('--larger-time-radius',default='4')
    p.add_argument('--theta-strip',default='1/64');p.add_argument('--wider-theta-strip',default='1/32')
    p.add_argument('--radial-radius',default='3/1000');p.add_argument('--E-radius',default='1/400')
    p.add_argument('--curvature-radius',default='3/1250');p.add_argument('--radial-degree',type=int,default=64)
    p.add_argument('--max-depth',type=int,default=10)
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=max(21,args.time_order+4);started=time.monotonic()
    desc=document(args.retarget);op,obj=hashed(desc['target_object']);rp,_=hashed(desc['target_root'])
    r59=document(args.R59);delta=Fraction(int(obj['delta_fraction']['numerator']),int(obj['delta_fraction']['denominator']))
    member=frame_membership(obj,r59,delta)
    R,S,s,w,R0,RE=map(Fraction,(args.time_radius,args.larger_time_radius,args.theta_strip,
        args.wider_theta_strip,args.radial_radius,args.E_radius))
    if not S>R>1 or not 0<s<=Fraction.from_float(r59['angular_strip_width'])<w or not R0>RE>0:
        raise ValueError('invalid actual analytic radii')
    # The root enclosure is independent of the chosen field representation.
    package=prepare_refined_root(op,rp,nodes=args.root_nodes)
    target=AffineBulkTarget(op,args.primitive_nodes,args.primitive_nodes,
        exact_arb(R0),exact_arb(RE),exact_arb(Fraction(8,25)))
    if target.affine_delta!=package.exact_delta:raise ValueError('true root and field parameter differ')
    legs=args.legs.split(',');grids={}
    for leg in legs:
        if leg not in ('forward','backward'):raise ValueError('invalid leg')
        gp,grid=hashed(desc['old_'+leg+'_reference']);grids[leg]=(gp,grid)
    requested=[]
    for leg,(_,grid) in grids.items():
        count=len(grid['exact_time_endpoints'])-1
        if args.segments=='all':indices=range(count)
        elif ':' in args.segments:
            first,last=map(int,args.segments.split(':'));indices=range(first,last)
        else:indices=list(map(int,args.segments.split(',')))
        if any(i<0 or i>=count for i in indices):raise ValueError('segment outside true grid')
        requested.extend((leg,i)for i in indices)
    common=dict(kind='sharp_endpoint_complete_germ_and_complex_time_domain_cover',
        source_sha256=sha(__file__),retarget_descriptor_sha256=sha(args.retarget),
        target_object_sha256=sha(op),target_root_sha256=sha(rp),R59_sha256=sha(args.R59),
        exact_delta_fraction=str(delta),membership=member,
        time_grid_sha256={leg:sha(path)for leg,(path,_) in grids.items()},
        time_radius=str(R),larger_time_radius=str(S),physical_theta_strip=str(s),
        wider_physical_theta_strip=str(w),radial_radius=str(R0),E_radius=str(RE),
        angles=args.angles,cutoff=args.cutoff,primitive_nodes=args.primitive_nodes,
        independent_root_nodes=args.root_nodes,time_order=args.time_order,bits=args.bits,
        requested_cases=[list(row)for row in requested],refined_root=package.provenance,
        dependency_sha256={name:sha(Path(__file__).with_name(name))for name in
            ['fourfold_phase_sine_time_geometry.py','fourfold_phase_full_angle_sine_domain.py',
             'fourfold_phase_full_angle_time_domain.py','fourfold_phase_field_time_turn_collar.py',
             'fourfold_phase_field_time_refined_root.py','fourfold_phase_field_time_germ_union.py']})
    index=dict(**common,complete=False,cases=[],limitations=[
        'Only listed complete leaves certify domains; this is not a true-flow residual or KAM proof',
        'Sharp separate endpoint bounds and all intersecting actual germs are retained',
        'Reflections and inherited domains bind the identical exact object and germ'])
    if args.resume and args.index.exists():
        old=document(args.index)
        for k,v in common.items():
            if old.get(k)!=v:raise ValueError('resume identity differs: '+k)
        index=old
    domains=Domains(sha(op),sha(rp))
    for path in args.seed:domains.add(path)
    if args.resume and args.out_directory.exists():
        for path in sorted(args.out_directory.glob('*.json.gz')):domains.add(path)
    args.out_directory.mkdir(parents=True,exist_ok=True)
    done={(r['leg'],r['segment'])for r in index['cases']if r.get('proved')}
    def save():
        index['elapsed_seconds_this_process']=time.monotonic()-started;write_report(args.index,index)
    save()

    def attempt(leg,i,a,b,l,r,depth,label,sign):
        ta,tb=a+(b-a)*l,a+(b-a)*r;c,h=(ta+tb)/2,(tb-ta)/2
        path=args.out_directory/f'{leg}_{i:04d}_{label}.json.gz'
        if args.resume and path.exists():
            saved=document(path)
            if saved.get('complete') and saved.get('proved_full_physical_angle_and_complex_time_domain'):
                checks=dict(source_sha256=common['source_sha256'],target_object_sha256=sha(op),
                    target_root_sha256=sha(rp),exact_time_endpoints=[ta.record(),tb.record()],
                    normalized_subspan=[str(l),str(r)],time_radius=str(R),larger_time_radius=str(S),
                    physical_theta_strip=str(s),wider_physical_theta_strip=str(w),
                    primitive_nodes=args.primitive_nodes,bits=args.bits,angles=args.angles,
                    cutoff=args.cutoff,time_order=args.time_order)
                if any(saved.get(key)!=value for key,value in checks.items()):
                    raise ValueError('completed leaf identity or analytic radii changed')
                domains.add(path)
                return [dict(path=str(path),sha256=sha(path),normalized_subspan=[str(l),str(r)])],[]
        cells,cover=sharp_cover(target,package.root,ta,tb)
        doc=dict(kind='sharp_actual_time_interval_domain',complete=False,
            source_sha256=common['source_sha256'],target_object_sha256=sha(op),target_root_sha256=sha(rp),
            retarget_descriptor_sha256=sha(args.retarget),R59_sha256=sha(args.R59),
            time_grid_manifest_sha256=common['time_grid_sha256'][leg],
            exact_delta_fraction=str(delta),leg=leg,segment=i,branch_sign=sign,
            exact_time_endpoints=[ta.record(),tb.record()],normalized_subspan=[str(l),str(r)],
            time_radius=str(R),larger_time_radius=str(S),physical_theta_strip=str(s),wider_physical_theta_strip=str(w),
            sharp_real_germ_cover=cover,required_common_spans=[list(map(str,v))for v in cells],
            germs=[],depth=depth,independent_root_nodes=args.root_nodes,primitive_nodes=args.primitive_nodes,
            bits=args.bits,angles=args.angles,cutoff=args.cutoff,time_order=args.time_order,
            dependency_sha256=common['dependency_sha256'])
        write_report(path,doc);failure=None
        try:
            for cell in cells:
                row=domains.inherit(cell,c,h,R,s)
                if row is None:
                    turn=bool(c.p or h.p)
                    if turn:
                        if len(cells)!=1:raise ValueError('exact endpoint needs its unique actual root germ')
                        side=1 if c.ball()>0 else -1
                        model=TurnCollarTimeModel(op,rp,ta,tb,side=side,nodes=args.primitive_nodes,
                            order=args.time_order,radial_degree=args.radial_degree,outer_radius=S,
                            curvature_radius=Fraction(args.curvature_radius),radial_radius=R0,E_radius=RE,
                            branch_sign=sign)
                    else:
                        if not sine_radial_displacement(package.root,c.ball(),h.ball(),R)<exact_arb(RE):
                            raise ValueError('exact sine image needs an accurate time subdivision')
                        model=SineGermTimeModel(op,rp,c.q,h.q,refined_root=package,cell=cell,
                            nodes=args.primitive_nodes,order=args.time_order,outer_radius=R,
                            radial_radius=R0,E_radius=RE,branch_sign=sign)
                    row=domain_gate(model,r59,args.angles,args.cutoff,R,S,s,w,turn)
                doc['germs'].append(row);write_report(path,doc)
                if not row['passed']:raise ValueError('complete D/curvature gate did not pass')
            doc.update(complete=True,complete_common_span_coverage=len(doc['germs'])==len(cells),
                proved_full_physical_angle_and_complex_time_domain=True)
            write_report(path,doc);domains.add(path)
            print(json.dumps(dict(leg=leg,segment=i,label=label,proved=True,germs=len(cells),
                inherited=sum('inherited'in v for v in doc['germs']))),flush=True)
            return [dict(path=str(path),sha256=sha(path),normalized_subspan=[str(l),str(r)])],[]
        except (ValueError, ZeroDivisionError) as error:
            failure=type(error).__name__+': '+str(error);doc['failure']=failure;write_report(path,doc)
        failed=[dict(path=str(path),sha256=sha(path),error=failure,normalized_subspan=[str(l),str(r)])]
        if depth>=args.max_depth:return [],failed
        mid=(l+r)/2
        left,lf=attempt(leg,i,a,b,l,mid,depth+1,label+'0',sign)
        right,rf=attempt(leg,i,a,b,mid,r,depth+1,label+'1',sign)
        return left+right,failed+lf+rf

    for leg,i in requested:
        if (leg,i)in done:continue
        grid=grids[leg][1];a,b=map(PiTime.from_record,grid['exact_time_endpoints'][i:i+2])
        leaves,failed=attempt(leg,i,a,b,Fraction(0),Fraction(1),0,'r',int(grid['trace_identity']['sign']))
        intervals=sorted((Fraction(x['normalized_subspan'][0]),Fraction(x['normalized_subspan'][1]))for x in leaves)
        proved=bool(intervals and intervals[0][0]==0 and intervals[-1][1]==1
            and all(x[1]==y[0]for x,y in zip(intervals,intervals[1:])))
        index['cases']=[row for row in index['cases']if(row['leg'],row['segment'])!=(leg,i)]
        index['cases'].append(dict(leg=leg,segment=i,proved=proved,leaves=leaves,failed_attempts=failed));save()
        print(json.dumps(dict(leg=leg,segment=i,complete=True,proved=proved,leaves=len(leaves),
            failed_attempts=len(failed),elapsed=time.monotonic()-started)),flush=True)
    index['complete']=True
    index['proved_all_requested_cases']=bool(len(index['cases'])==len(requested)and all(v['proved']for v in index['cases']))
    index['whole_both_branches']=bool(index['proved_all_requested_cases'] and set(legs)=={'forward','backward'}
        and args.segments=='all')
    save();print(json.dumps(dict(complete=True,all_requested=index['proved_all_requested_cases'],
        whole_both_branches=index['whole_both_branches'],sha256=sha(args.index))),flush=True)


if __name__=='__main__':main()
