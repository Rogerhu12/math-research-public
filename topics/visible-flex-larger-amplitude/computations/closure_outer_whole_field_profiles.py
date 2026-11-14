#!/usr/bin/env python3
"""True whole-field Wronskian columns on actual outer cells11/10.

Every original material position is retained.  The already certified
R67 forward column and R73 backward adjoint anchors are used at each
segment.  One actual Taylor transition is computed per subpanel and
consumed in both directions.  The true inner slope, global mu11 and
both physical P=h_theta/(r*w), K=h_r/w components are retained.

This saves rigorous pointwise columns and source integrals, not an
endpoint-only norm.  The whole-field nonlinear gates are paid by a
separate ordered prefix/suffix consumer.  No completed outer PDE is
claimed by producing these geometry columns.
"""
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import resource
import tempfile
import time

from flint import arb,ctx

from closure_outer_adjoint_source import actual_panel_bounds,transpose
from closure_outer_taylor_shared_flow import taylor_global,root_global,raw_source_identity
from closure_outer_two_cell_adjoint import compact_ball,compact_upper
from closure_projective_interval_column import ProjectiveColumn
from closure_real_head_source_enclosure import exact_q,power2
from closure_real_linear_head_enclosure import PositiveKernels,positive_scale_bounds
from closure_split_joint_io_v2 import digest,read_field,iter_array
from closure_taylor_cut_slope_v2 import (ball,endpoint,record,intersect,rough_radius,
    monotone_parts,column_record,restore_column,save)
from tail_r33_middle_ordered_physical import SourceValues


EXPECTED={
 'closure_outer_adjoint_source.py':'776dbfd8cabd06247c8ddc38d989e1f833e7be96c44adfc9d4bfad927687eee0',
 'closure_outer_taylor_shared_flow.py':'81d8bd9ad3da434eb8ab98d381a32a09bbe7aca5fa3be8a0bfe493ccd62455b7',
 'closure_outer_two_cell_adjoint.py':'184667ec3f78b9d99d2a5fe28465c243ecee0e6ba4d4685199e72bd9bef0899a',
 'closure_projective_interval_column.py':'45997a1d5be6326a1ebbe85ac4240ea7d9dde1c2fb6acdf832460dade89e4f97',
 'closure_real_head_source_enclosure.py':'97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47',
 'closure_real_linear_head_enclosure.py':'1b8023b53eeca7a0ef28816a99b1b7d4a43f025c2482afae9e88db572e174b8e',
 'closure_taylor_cut_slope_v2.py':'8e150b6fe16c33da98043bc7ebe952abf123e2f7c8da8ebbfb10bfec700fb5ea',
 'tail_r33_middle_ordered_physical.py':'ac1bb495b33a37f7f88b6b7258a88a466c205cb452141668b6c454f88386008e'}


def scaled(column,value):
    amp=column.absolute_lower.union(column.absolute_upper)
    lo,hi=positive_scale_bounds((value.lower(),value.upper()),amp)
    if column.sign<0:lo,hi=-hi,-lo
    return lo.union(hi)


def partial_units(column,A,B,adjoint=False):
    """All partial true columns, retaining the common signed amplitude.

For positive a,b and AB<1/4, every forward partial transition has
T00,T11 in [1-AB,1], T01 in [0,A], T10 in [-B,0].  The backward
height adjoint is T^t eta; chi=(-eta_v,eta_q).
"""
    p=(A*B).upper()
    if not p<arb(1)/4:raise ArithmeticError('Subdivide partial-flow sign envelope')
    d=(1-p).lower().union(arb(1))
    ap=arb(0).union(A);bm=(-B).union(arb(0))
    u=column.unit()
    if adjoint:
        e0=d*u[0]+bm*u[1]
        e1=ap*u[0]+d*u[1]
        return [-e1,e0]
    return [d*u[0]+ap*u[1],bm*u[0]+d*u[1]]


def physical(h,mode,mu,r,w,units,column):
    """P sine amplitude and K cosine amplitude; BOTH normalized by w."""
    u=mode*mode-4;scale=(r/h.rc)**u
    pq=-mode*r**3*scale/w
    kq=mode*mode*r**3*scale/w
    kv=h.sqrt12*mu/(r**4*w*w*scale)
    return [scaled(column,pq*units[0]),
            scaled(column,kq*units[0]+kv*units[1])]


def derivative_density(g,sigma,rho,input_cutoff):
    """Complete source derivative on a genuine whole-field ball.

V=sqrt(c0/4) is a fixed positive envelope for the original candidate.
The candidate has cutoff40, arbitrary unknown nonmean perturbations
have cutoff M and strong norm <=rho relative to V.  A unit direction
has P+K norm <=V, P_theta<=M V and K_theta-P<=(M+1)V.
All mean/inverse terms are differentiated exactly.
"""
    raw=(ball(g['complete_mean_abs']).upper()/4).sqrt().upper()
    vm,ve=compact_upper(raw)
    # Define the norm by this EXACT upward dyadic.  Both the derivative
    # density and the persisted physical output denominator use it.
    V=arb(vm)*power2(ve)
    if not V>0:raise ArithmeticError('A positive actual candidate envelope is required')
    w=ball(g['w']);r=ball(g['radius']);rx=ball(g['radius_x'])
    if not w>0 or not r>0 or not rx>0 or not w.upper()<=arb(1)/2:
        raise ArithmeticError('The true positive background domain is required')
    E=(1+w*w).upper();s=(rx/r).upper();ell=abs(ball(g['log_w_x'])).upper()
    M=input_cutoff
    R=(sigma+rho)*V
    T=(40*sigma+M*rho)*V
    U=(41*sigma+(M+1)*rho)*V
    if not R<arb(1)/64:raise ArithmeticError('The entire candidate+field mean domain is unpaid')
    c=4*R*R;dc=16*R*V
    lead=c+R+E*T
    if not lead<1:raise ArithmeticError('The entire candidate+field Wiener inverse is unpaid')
    dlead=dc+(1+M*E)*V
    q=E*s*U*U+E*ell*(R+T)**2
    dq=2*(M+1)*(E*s*U+E*ell*(R+T))*V
    mn=ell*(2*c*(R+E*T)+c*c)
    dmn=2*ell*(dc*(R+E*T+c)+c*(1+M*E)*V)
    density=((dq+dmn)/(1-lead)+(q+mn)*dlead/(1-lead)**2).upper()
    return V,density,R.upper(),lead.upper()


def restore_matrix(rows):return [[ball(x) for x in row] for row in rows]
def matrix_records(rows):return [[record(x) for x in row] for row in rows]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('ready','flow','adjoint','refined-source','out-prefix'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--source-summary',type=Path,action='append',required=True)
    p.add_argument('--precision',type=int,default=256)
    p.add_argument('--order',type=int,default=24)
    p.add_argument('--remainder-bits',type=int,default=100)
    p.add_argument('--root-bits',type=int,default=160)
    p.add_argument('--rss-kib',type=int,default=40960)
    p.add_argument('--field-radius',default='1/16')
    p.add_argument('--input-cutoff',type=int,default=92)
    p.add_argument('--resume',type=Path)
    a=p.parse_args();began=time.monotonic()
    if a.order<4 or a.precision<a.root_bits+32 or a.input_cutoff<40:
        raise ValueError('Keep validated Taylor precision and all20 original modes')
    ctx.prec,ctx.cap,ctx.threads=a.precision,a.order+2,1
    for name,sha in EXPECTED.items():
        if digest(Path(__file__).with_name(name))!=sha:
            raise ValueError('A frozen mathematical implementation changed: '+name)
    paths=[a.ready,a.flow,a.adjoint,a.refined_source]+a.source_summary
    hashes={str(path):digest(path) for path in paths}
    flow=json.loads(a.flow.read_text());adj=json.loads(a.adjoint.read_text())
    new=json.loads(a.refined_source.read_text())
    if (not all(flow['gates'].values()) or not adj['all_gates']
            or not new['all_gates'] or not new['same_exact_candidate']
            or flow['config']['modes']!=[2,4] or adj['modes']!=[2,4]
            or adj['counts']['original_material']!=10793 or new['cell']!=10):
        raise ValueError('The complete actual source/linear/adjoint inputs are required')
    if adj['input_hashes'].get(str(a.flow))!=hashes[str(a.flow)]:
        raise ValueError('The original true adjoint uses another actual flow')
    originals={}
    for path in a.source_summary:
        doc=json.loads(path.read_text());n=doc['cell']
        if n not in (10,11) or n in originals or not doc['all_gates']:
            raise ValueError('Supply the two complete original source records')
        if adj['input_hashes'].get(str(path))!=hashes[str(path)]:
            raise ValueError('The original adjoint source identity changed')
        originals[n]=doc
    if sorted(originals)!=[10,11]:raise ValueError('Both actual source cells are required')
    if new['original_source_summary']!=next(str(x) for x in a.source_summary
        if json.loads(x.read_text())['cell']==10):
        raise ValueError('The refined five moments define another candidate')
    ready=dict(rationalDeepModel=read_field(a.ready,'rationalDeepModel'),
               shallowSourceParameters=read_field(a.ready,'shallowSourceParameters'))
    identities=[raw_source_identity(ready,n) for n in (11,10)]
    h=SourceValues(ready);del ready
    positive=PositiveKernels(h,12,4)
    cells={n:positive.source_cell(n) for n in (11,10)};h.cells.update(cells)
    mu=ball(flow['config']['global_mu_star'])
    source_docs={11:originals[11],10:new}
    order=[(n,j) for n in (11,10) for j in range(9)]
    groups={(n,g['segment']):g for n,d in source_docs.items() for g in d['groups']}
    if sorted(groups)!=sorted(order):raise ValueError('All18 complete source segments are required')
    for g in groups.values():
        if digest(Path(g['path']))!=g['sha256']:raise ValueError('A true source group changed')
        hashes[g['path']]=g['sha256']
    slope_path=next(Path(x) for x in flow['input_hashes'] if 'closure-taylor-cut-' in x)
    if digest(slope_path)!=flow['input_hashes'][str(slope_path)]:
        raise ValueError('The shared true inner slope changed')
    hashes[str(slope_path)]=digest(slope_path)
    slope=json.loads(slope_path.read_text());srows={x['mode']:x for x in slope['rows']}
    b=ball(slope['cut_radius']);R=ball(next(x for x in flow['cell_rows'] if x['cell']==10)['radius'])
    W={m:ball(next(x for c in flow['cell_rows'] if c['cell']==10 for x in c['modes']
                 if x['mode']==m)['S0_true_Q'])*(h.rc/R)**(m*m-4) for m in (2,4)}
    if any(x.contains(0) for x in W.values()):raise ArithmeticError('The true global Wronskian is not separated from zero')
    sigma=arb(17)/16;rho=exact_q(Fraction(a.field_radius))
    if not 0<rho<1:raise ValueError('Use an explicit positive relative field radius below1')
    flow_stem=str(a.flow)[:-5];adj_stem=str(a.adjoint)[:-5]
    anchor_paths=[]
    for n,j in order:
        anchor_paths.extend([Path(flow_stem+f'-cell{n:03d}-seg{j}.json'),
            Path(adj_stem+f'-completed-cell{n:03d}-segment{j}.json')])
    for path in anchor_paths:hashes[str(path)]=digest(path)
    config=dict(cells=[11,10],modes=[2,4],input_cutoff=a.input_cutoff,
        precision=a.precision,order=a.order,remainder_bits=a.remainder_bits,
        root_bits=a.root_bits,field_radius=a.field_radius,
        parameter_amplitude_sigma='17/16',global_mu_star=record(mu),
        cut_radius=record(b),outer_radius=record(R),
        true_Wronskians={str(m):record(w) for m,w in W.items()},
        source_hashes=EXPECTED,entrypoint_sha256=digest(__file__),input_hashes=hashes,
        physical_variables='P=h_theta/(r*w), K=h_perp,r/w; both contain the displayed 1/w factors',
        profile_endpoint_bits=80)
    completed=[];profile_groups=[]
    counts=dict(original_material=0,taylor=0,root_brackets=0,rejected=0)
    greatest=arb(0);max_mean=arb(0);max_leading=arb(0)
    if a.resume:
        old=json.loads(a.resume.read_text())
        if old['config']!=config:raise ValueError('Recovery uses another actual problem or source')
        completed=[tuple(x) for x in old['completed_groups']]
        if completed!=order[:len(completed)]:raise ValueError('Recovery is not the original forward group order')
        profile_groups=old['profile_groups'];counts=old['counts']
        greatest=ball(old['greatest_balanced_Taylor_remainder'])
        max_mean=ball(old['maximum_mean_input_radius']);max_leading=ball(old['maximum_leading_norm'])
        for g in profile_groups:
            if digest(Path(g['path']))!=g['sha256']:raise ValueError('A completed true profile changed')
    def guard():
        peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak>a.rss_kib:raise MemoryError('Observed whole-field owned RSS exceeded stop threshold: '+str(peak))
    def true_phi_at(index):
        if index==0:
            return [ProjectiveColumn([(h.rc/b)**(m*m-4),
                (b/h.rc)**(m*m-4)*ball(srows[m]['true_slope_mu_outer'])]) for m in (2,4)]
        n,j=order[index-1]
        cp=json.loads(Path(flow_stem+f'-cell{n:03d}-seg{j}.json').read_text())
        if cp['config']!=flow['config']:raise ValueError('A true forward anchor has another source')
        out=[]
        for k,m in enumerate((2,4)):
            centre=restore_column(cp['columns'][k][0]).values()
            basis=restore_column(cp['columns'][k][2]).values()
            delta=(b/h.rc)**(m*m-4)*ball(srows[m]['true_minus_shared_exact_slope'])
            out.append(ProjectiveColumn([centre[i]+delta*basis[i] for i in range(2)]))
        return out
    def eta_at_right(index):
        if index==len(order)-1:return [ProjectiveColumn([arb(1),arb(0)]) for m in (2,4)]
        n,j=order[index+1]
        cp=json.loads(Path(adj_stem+f'-completed-cell{n:03d}-segment{j}.json').read_text())
        if cp['config']!=adj['config']:raise ValueError('A true adjoint anchor has another source')
        return [restore_column(cp['adjoint_columns'][k][0]) for k in range(2)]
    active=None
    try:
        for gi,(n,j) in enumerate(order):
            if (n,j) in completed:continue
            group=groups[n,j];path=Path(group['path']);segment=cells[n]['segments'][j]
            right_anchor=json.loads(Path(flow_stem+f'-cell{n:03d}-seg{j}.json').read_text())
            segment['physical_outer_radius']=ball(right_anchor['radius'])
            if gi==0:
                segment['physical_inner_radius']=b
            else:
                pn,pj=order[gi-1]
                left_anchor=json.loads(Path(flow_stem+f'-cell{pn:03d}-seg{pj}.json').read_text())
                segment['physical_inner_radius']=ball(left_anchor['radius'])
            forward=true_phi_at(gi);eta=eta_at_right(gi)
            expected_forward=true_phi_at(gi+1)
            expected_eta_cp=json.loads(Path(adj_stem+f'-completed-cell{n:03d}-segment{j}.json').read_text())
            expected_eta=[restore_column(expected_eta_cp['adjoint_columns'][k][0]) for k in range(2)]
            monotone=monotone_parts(segment,a.root_bits)
            out=Path(str(a.out_prefix)+f'-cell{n:03d}-segment{j}-profiles.json.gz')
            partial=out.with_name(out.name+'.partial')
            if out.exists() or partial.exists():raise FileExistsError('Use fresh true whole-field profile names')
            subcount=0;original_count=0
            with tempfile.TemporaryFile(mode='w+b',dir=a.out_prefix.parent) as spool:
                offsets=[]
                # Source groups retain exact true radius anchors; one source
                # row at a time also bounds memory independently of mode count.
                for g in iter_array(path,'panels'):
                    if g['panel']!=original_count or g['segment']!=j:
                        raise ValueError('The actual original source positions changed')
                    left,right=Fraction(g['x_left']),Fraction(g['x_right'])
                    if original_count==0:
                        if left!=0:raise ValueError('Missing source segment left endpoint')
                        segment['physical_inner_radius']=ball(g['radius_left'])
                    if right==1:segment['physical_outer_radius']=ball(g['radius_right'])
                    V,density,mradius,lbound=derivative_density(g,sigma,rho,a.input_cutoff)
                    max_mean=max(max_mean,mradius);max_leading=max(max_leading,lbound)
                    N={str(x['mode']):x['complete_source_cosine'] for x in g['selected_cosine_sources']}
                    radius=ball(g['radius_left'])
                    parts=[(max(left,lo),min(right,hi),sgn) for lo,hi,sgn in monotone
                           if max(left,lo)<min(right,hi)]
                    if not parts or parts[0][0]!=left or parts[-1][1]!=right:
                        raise ArithmeticError('The exact source/root partition has a gap')
                    original_subcount=0
                    for lo,hi,sgn in parts:
                        segment['_monotone_sign']=sgn
                        stack=[(lo,hi,0)]
                        while stack:
                            aa,cc,depth=stack.pop()
                            try:
                                T,next_radius,error=(root_global(h,segment,aa,cc,radius,[2,4],mu)
                                    if sgn==0 else taylor_global(h,segment,aa,cc,radius,[2,4],
                                        a.order,power2(-a.remainder_bits),mu))
                                local=[actual_panel_bounds(h,segment,aa,cc,radius,g,m,mu) for m in (2,4)]
                                rr,_=rough_radius(h,segment,aa,cc,radius)
                                rr=intersect(rr,ball(g['radius']))
                                ww=intersect(h.source_point(segment,exact_q(aa).union(exact_q(cc)))['w'],ball(g['w']))
                                # Every unit/whole-physical box is a bound on
                                # all points, not merely the two endpoints.
                                profiles=[];advanced=[]
                                for k,m in enumerate((2,4)):
                                    A,B,J=local[k]
                                    units=partial_units(forward[k],A,B)
                                    qv=[scaled(forward[k],u) for u in units]
                                    pk=physical(h,m,mu,rr,ww,units,forward[k])
                                    trial=restore_column(column_record(forward[k]));trial.advance(T[k])
                                    advanced.append(trial)
                                    profiles.append(dict(mode=m,qv=[record(x) for x in qv],
                                        physical_PK=[record(x) for x in pk],
                                        A=record(A),B=record(B),J=record(J)))
                            except (ArithmeticError,ValueError,ZeroDivisionError) as error0:
                                if sgn==0 or depth>=40:
                                    raise ArithmeticError('Unresolved whole-field true panel '+
                                        str((n,j,g['panel'],aa,cc,sgn))+': '+str(error0)) from error0
                                mid=(aa+cc)/2
                                stack.extend([(mid,cc,depth+1),(aa,mid,depth+1)])
                                counts['rejected']+=1
                                continue
                            payload=dict(panel=g['panel'],subpanel=original_subcount,
                                x_left=str(aa),x_right=str(cc),radius=record(rr),w=record(ww),
                                source_envelope=record(V),whole_low46_source_derivative_density=record(density),
                                sources=N,flows=[matrix_records(t) for t in T],phi=profiles)
                            offsets.append(spool.tell())
                            spool.write(json.dumps(payload,separators=(',',':')).encode()+b'\n')
                            radius=next_radius;forward=advanced
                            original_subcount+=1;subcount+=1
                            counts['root_brackets' if sgn==0 else 'taylor']+=1
                            if sgn:greatest=max(greatest,error)
                            guard()
                    intersect(radius,ball(g['radius_right']))
                    original_count+=1;counts['original_material']+=1
                if original_count!=group['panels'] or right!=1:
                    raise ValueError('The whole original source segment was not processed')
                # Independent signed endpoint identities detect a wrong gauge,
                # source order, or use of the finite Robin slope.
                for k in range(2):
                    for z in range(2):intersect(forward[k].values()[z],expected_forward[k].values()[z])
                active=gzip.open(partial,'wt',compresslevel=9)
                active.write(json.dumps(dict(cell=n,segment=j,original_panels=original_count,
                    source_group_path=str(path),source_group_sha256=group['sha256'],
                    true_Wronskians={str(m):record(w) for m,w in W.items()},
                    panels_reverse_radial_order=True,subpanels=subcount,
                    coordinate_convention=config['physical_variables'],
                    complete_true_source_slope_not_finite_Robin=True,
                    compact='All displayed pairs are outward80bit lower/upper dyadics; positive fields upper dyadics'))[:-1]+',"panels":[\n')
                written=0
                for offset in reversed(offsets):
                    spool.seek(offset);part=json.loads(spool.readline())
                    dx=exact_q(Fraction(part['x_right'])-Fraction(part['x_left']))
                    rr,ww=ball(part['radius']),ball(part['w'])
                    rows=[]
                    for k,m in enumerate((2,4)):
                        old=part['phi'][k];A,B,J=(ball(old[z]) for z in ('A','B','J'))
                        units=partial_units(eta[k],A,B,adjoint=True)
                        cqv=[scaled(eta[k],v) for v in units]
                        cpk=physical(h,m,mu,rr,ww,units,eta[k])
                        fqv=[ball(x) for x in old['qv']]
                        fpk=[ball(x) for x in old['physical_PK']]
                        # The global W is the same constant at every point.
                        intersect(fqv[0]*cqv[1]-fqv[1]*cqv[0],W[m])
                        integrals={}
                        for name,values in (('phi',fqv),('chi',cqv)):
                            value=values[0]*J*dx
                            absolute=(abs(values[0]).upper()*J.upper()*dx).upper()
                            integrals[name]=dict(signed=compact_ball(value),absolute=compact_upper(absolute))
                        rows.append(dict(mode=m,phi_qv=[compact_ball(v) for v in fqv],
                            chi_qv=[compact_ball(v) for v in cqv],
                            phi_physical_PK=[compact_ball(v) for v in fpk],
                            chi_physical_PK=[compact_ball(v) for v in cpk],
                            integrals=integrals,complete_candidate_source=compact_ball(ball(part['sources'][str(m)]))))
                        e=restore_column(column_record(eta[k]));e.advance(transpose(restore_matrix(part['flows'][k])))
                        eta[k]=e
                    outrow=dict(panel=part['panel'],subpanel=part['subpanel'],
                        x_left=part['x_left'],x_right=part['x_right'],
                        radius=compact_ball(rr),w=compact_ball(ww),
                        source_envelope=compact_ball(ball(part['source_envelope'])),
                        whole_low46_source_derivative_density=compact_upper(ball(part['whole_low46_source_derivative_density'])),
                        modes=rows)
                    if written:active.write(',\n')
                    active.write(json.dumps(outrow,separators=(',',':')));written+=1
                    guard()
                for k in range(2):
                    for z in range(2):intersect(eta[k].values()[z],expected_eta[k].values()[z])
                active.write('\n]}\n');active.close();active=None
            if partial.stat().st_size>5*1024*1024:
                raise ValueError('A complete profile group exceeds the5MB repository cap')
            partial.rename(out)
            profile_groups.append(dict(cell=n,segment=j,path=str(out),bytes=out.stat().st_size,
                sha256=digest(out),original_panels=original_count,subpanels=subcount,
                forward_anchor_intersects=True,backward_anchor_intersects=True,
                Wronskian_identity_intersects_on_every_subpanel=True))
            completed.append((n,j))
            cp=dict(status='Complete actual whole-field Wronskian profile group',config=config,
                completed_groups=completed,profile_groups=profile_groups,counts=counts,
                greatest_balanced_Taylor_remainder=record(greatest),
                maximum_mean_input_radius=record(max_mean),maximum_leading_norm=record(max_leading),
                elapsed_seconds=time.monotonic()-began,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            save(Path(str(a.out_prefix)+f'-completed-cell{n:03d}-segment{j}.json'),cp)
            print(json.dumps(dict(event='whole_field_profile_group_complete',cell=n,segment=j,
                original_panels=original_count,subpanels=subcount,bytes=out.stat().st_size,
                elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=cp['peak_RSS_KiB'])),flush=True)
        if completed!=order or counts['original_material']!=10793:
            raise ValueError('The complete original two-cell range is missing')
        gates=dict(same_real_metric_and_original_source_positions=True,
            true_linear_head_slope_with_explicit_Wronskian_error=True,
            global_mu11_no_interface_reweighting=True,
            all18_segments_and10793_original_panels=True,
            both_columns_and_both_physical_components_everywhere=True,
            partial_flow_signs_and_Taylor_remainders_paid=True,
            all_global_Wronskians_separated_and_pointwise_identities_checked=True,
            full_low46_field_directions_complete_mean_and_inverse_density=True,
            every_forward_and_backward_anchor_intersects=True,
            new_background_integrals_not_needed=True)
        result=dict(status='Complete true whole-field geometry; ordered Green consumer still required',
            config=config,gates=gates,all_gates=True,counts=counts,profile_groups=profile_groups,
            source_identity=identities,input_hashes=hashes,
            whole_field_Green_formula='s<=r: chi(r)*phi_q(s)*J(s)/W; s>r: phi(r)*chi_q(s)*J(s)/W',
            affine_outer_candidate_endpoint_lift_must_be_retained=True,
            complete_outer_PDE_or_all_frequency_contraction_claimed=False,
            ordered_Green_numeric_norms_not_yet_consumed=True,
            greatest_balanced_Taylor_remainder=record(greatest),
            maximum_mean_input_radius=record(max_mean),maximum_leading_norm=record(max_leading),
            elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(Path(str(a.out_prefix)+'.json'),result);guard()
        print(json.dumps(dict(event='complete_whole_field_profiles',all_gates=True,
            counts=counts,elapsed_seconds=result['elapsed_seconds'],peak_RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    except Exception as error:
        if active is not None:active.close()
        save(Path(str(a.out_prefix)+'-failure.json'),dict(status='Incomplete true whole-field profile attempt',
            error=repr(error),config=config,completed_groups=completed,profile_groups=profile_groups,
            counts=counts,elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        raise


if __name__=='__main__':main()
