"""Continuous R643 metric and off-solution curvature on source-bound interior material slabs."""
import hashlib
from fractions import Fraction
from pathlib import Path

import r649_complete_offsolution_curvature_20261128 as shape
import r672_existing_r643_material_data_20261128 as material
import r672_material_angular_ring_20261128 as alg

I,rat,mag=alg.I,alg.rat,alg.iv.mag
EPS=rat('1e-6')
SCHEMA='R672-same-86da-continuous-material-ring-v1'


for module,expected in ((shape,'a2f765c580d7209b8549f10547d17c39b71a84b33dcbb0d9008311017e2a23fb'),
                        (material,'8ed67dd778712d0d62fd568a3500ac8405fb2b2532e2c3ccaabf925cbb051a35')):
    if hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()!=expected:
        raise ValueError('different original curvature formula or material source')


def metric(d,f):
    a=shape.abs_i(d)
    return (a+alg.iv.iv.sqrt_i(shape.square_sum(a,2*f)))/2


def envelope(q):
    return max(x.hi for x in q)


def ring_values(cell,n,degree,check=None):
    """Both exact angular vertices and whole sectors, including all periodic primitives."""
    shape.public_only()
    missing=cell['unresolved_errors']
    evidence={'same_field_identity':cell['material']['origin'],
              'continuous_enclosure_status':'conditional_on_declared_input_errors' if missing else 'all_declared_input_errors_enclosed',
              'unresolved_errors':list(missing)}
    z=alg.ring(cell['radial'],n,degree,check=check)
    htheta=2*alg.PI/n
    margins={'min_b_over_r':float('inf'),'min_u':float('inf'),'min_N':float('inf'),'min_A':z['A'].lo}
    out=[[],[]]
    for level in (0,1):
        for i in range(n):
            if check is not None:
                check()
            rr,g,frame=z['raw'][level][i],z['loc'][level][i],z['frames'][level][i]
            if level==1:
                margins['min_b_over_r']=min(margins['min_b_over_r'],(g['b'].c[0]/rr['r'].c[0]).lo)
                margins['min_u']=min(margins['min_u'],g['u'].c[0].lo)
                margins['min_N']=min(margins['min_N'],g['N'].c[0].lo)
            E=rr['E'].c[0]
            chi=1/alg.iv.iv.sqrt_i(E)
            S=[piece[1][level][i]*chi for piece in z['pi']['H']]
            T,JT=frame['T'],frame['JT']
            st=S[0]*T[0]+S[1]*T[1]
            sn=-(S[0]*JT[0]+S[1]*JT[1])
            v,u=g['v']*chi,g['u']*chi
            d=2*(v*st+u*sn)+S[0]**2+S[1]**2
            f=g['b']/rr['r']*st
            row={'d':d.c[0],'f':f.c[0],'eta':metric(d.c[0],f.c[0]),
                 'd_theta':d.c[1]/htheta,'f_theta':f.c[1]/htheta}
            if z['has_third'] and level==1:
                raw={k:v.c[0] for k,v in rr.items()}
                means={'A':z['A'],'G':z['G'],'Gr':z['Gr'],'Pi_a':z['pa'][level][i].c[0],
                       'Pi_R':z['pr'][level][i].c[0],'Pi_Rr':z['prr'][level][i].c[0]}
                kernel=shape.full_radial_defect_kernel(raw,means,input_evidence=evidence)
                theta=alg.angle(n,i,degree,True).c[0]
                pih=[v[1][level][i].c[0] for v in z['pi']['H']]
                pihr=[v[1][level][i].c[0] for v in z['pi']['Hr']]
                arc=shape.arc_input_from_complete_vector_primitives(kernel,theta,pih,pihr,primitive_evidence=evidence)
                a=arc['arc_intervals']
                r,b,q,pt=raw['r'],kernel['b'],raw['q'],raw['pt']
                bs=(r*a['r_s']-q*a['q_s'])/b
                P,Ps,sT,sn0,dsT,dsn=[a[k] for k in ('P','P_s','sT','sn','ssT','ssn')]
                V0=-P*q/b
                V0s=-(Ps*q+P*a['q_s'])/b+P*q*bs/b**2
                row['d_s']=2*((V0s+a['U0']*a['h'])*sT+(a['U0_s']-V0*a['h'])*sn0
                       +(V0+sT)*dsT+(a['U0']+sn0)*dsn)
                row['f_s']=(bs/r-b*a['r_s']/r**2)*sT+b/r*(dsT-a['h']*sn0)
                try:
                    curv=shape.actual_arc_curvature(a,input_evidence=evidence)
                    row['principal']=curv['actual_principal_curvature_intervals']
                    row['abs_principal_upper']=curv['actual_absolute_principal_curvature_upper'].hi
                except ArithmeticError as exc:
                    row['shape_unresolved']=str(exc)
            out[level].append(row)
    return {'schema':SCHEMA,'material':cell['material'],'unresolved_errors':list(missing),
            'maximum_paid_input_radii_by_source_family_and_radial_order':cell['maximum_paid_input_radii_by_source_family_and_radial_order'],
            'n':n,'raw_formula_lower_margins':margins,'vertices':out[0],'sectors':out[1],'E':cell['radial']['E'],'source_evidence':evidence,
            'source_evidence_sha256':cell['source_evidence_sha256'],'radial_evidence_sha256':cell['radial_evidence_sha256'],
            'third_endpoint_evidence_sha256':cell['third_endpoint_evidence_sha256']}


def width(x):
    return (I(x.hi)-x.lo).hi


def hull_many(v):
    return I(min(x.lo for x in v),max(x.hi for x in v))


def slab(run,i,body,left=None,right=None):
    """Optional exact endpoint rings preserve paid node cancellations; direct interiors also stand alone."""
    origin=material.identity(run)
    data,_=run.current
    nt=len(data['theta'])
    n=body['n']
    rs=[float(x) for x in data['r'][i:i+2]]
    if len(rs)!=2 or n%nt or (body['material']['origin']!=origin or body['material']['r_hex']!=[v.hex() for v in rs]):
        raise ValueError('different material slab or incommensurate paid angular grid')
    fractions=tuple(map(Fraction,body['material'].get('cell_fraction',('0','1'))))
    lo,hi=fractions
    if not 0<=lo<hi<=1 or (fractions!=(0,1) and (left is not None or right is not None)):
        raise ValueError('subslabs use their direct continuous bound; parent vertices cannot be relabeled')
    for end,r in [(left,rs[0]),(right,rs[1])]:
        if end is not None and (end['material']!={'origin':origin,'r_hex':[r.hex(),r.hex()]} or end['n']!=n):
            raise ValueError('endpoint belongs to another material point or grid')
    theta_width=2*alg.PI/nt
    s_width=(I(rs[1])-rs[0])*rat(hi-lo)*alg.iv.iv.sqrt_i(body['E'])
    ref=n//nt
    eta=0.
    curvs=[]
    missing=set(body['unresolved_errors'])
    used=False
    worst_vertex=worst_transport=0.
    for j in range(nt):
        parts=body['sectors'][j*ref:(j+1)*ref]
        bound=envelope([p['eta'] for p in parts])
        if left is not None and right is not None and all('d_s' in p for p in parts):
            # Form the endpoint interval from actual signed d,f, including recomposition, the
            # entire angular primitive, source radii and evaluation roundoff at the true vertex.
            corners=[]
            for endpoint,k in ((left,i),(right,i+1)):
                for jj in (j,(j+1)%nt):
                    vertex=endpoint['vertices'][jj*ref]
                    old=material.paid_corner(run,k,jj)
                    pd=old['d']; pf=old['f']
                    sd=mag(vertex['d']-pd); sf=mag(vertex['f']-pf)
                    corners.append((vertex,pd,pf,sd,sf,old['legacy_eta']))
            deltas=[]
            for field in ('d','f'):
                ds=hull_many([p[field+'_s'] for p in parts])
                dt=hull_many([p[field+'_theta'] for p in parts])
                # For each direction use the strongest of the Lipschitz and signed derivative
                # oscillation bounds; both compare the same endpoint linear interpolant.
                ls=min((I(mag(ds))/2).hi,(I(width(ds))/4).hi)
                lt=min((I(mag(dt))/2).hi,(I(width(dt))/4).hi)
                deltas.append((s_width*ls+theta_width*lt).hi)
            DD,DF=deltas
            absolute=max(metric(I(mag(v['d'])),I(mag(v['f']))).hi for v,*_ in corners)
            by_norm=(I(absolute)+metric(I(DD),I(DF))).hi
            # A second independent bound starts at the actual represented row and directly
            # pays its signed endpoint error. No archived scalar maximum is used as a grid.
            represented=max((metric(pd,pf)+metric(I(sd),I(sf))).hi for _,pd,pf,sd,sf,_ in corners)
            by_paid=(I(represented)+metric(I(DD),I(DF))).hi
            worst_vertex=max(worst_vertex,max(metric(I(x[3]),I(x[4])).hi for x in corners))
            worst_transport=max(worst_transport,metric(I(DD),I(DF)).hi)
            dmax=(I(max(mag(c[0]['d']) for c in corners))+DD).hi
            fmax=(I(max(mag(c[0]['f']) for c in corners))+DF).hi
            mixed=metric(I(dmax),I(fmax)).hi
            sharper=min(bound,by_norm,by_paid,mixed)
            if sharper<bound:
                missing.update(left['unresolved_errors']+right['unresolved_errors'])
                used=True
            bound=sharper
        eta=max(eta,bound)
        if all('principal' in p for p in parts):
            curvs.extend(p['principal'] for p in parts)
    principal=None
    if len(curvs)==n:
        principal=[hull_many([pair[k] for pair in curvs]) for k in (0,1)]
    return {'schema':SCHEMA,'material':body['material'],'paid_radial_edge':i,'maximum_paid_input_radii_by_source_family_and_radial_order':body['maximum_paid_input_radii_by_source_family_and_radial_order'],
            'n_contiguous_periodic_sectors':n,'raw_formula_lower_margins':body['raw_formula_lower_margins'],
            'physical_arc_gap_upper':s_width.hi,'angular_gap_upper':theta_width.hi,
            'worst_certified_vertex_recomposition_change':worst_vertex if left is not None and right is not None and all('d_s' in x for x in body['sectors']) else None,
            'worst_signed_material_interpolation_radius':worst_transport if left is not None and right is not None and all('d_s' in x for x in body['sectors']) else None,
            'metric_upper':eta,'metric_below_threshold_for_supplied_inputs':eta<=EPS.lo,
            'principal_curvature_intervals_for_supplied_inputs':None if principal is None else [[v.lo,v.hi] for v in principal],
            'max_absolute_principal_curvature_upper':None if principal is None else max(map(mag,principal)),
            'signed_vertex_interpolation_used':used,'unresolved_source_or_radial_errors':sorted(missing),
            'witnessed_bounds_are_conditional_on_mathematical_source_certificates':True,
            'endpoint_evidence':None if not used else [{'material':z['material'],'source_sha256':z['source_evidence_sha256'],
                'third_endpoint_evidence_sha256':z['third_endpoint_evidence_sha256']} for z in (left,right)],
            'source_evidence_sha256':body['source_evidence_sha256'],'radial_evidence_sha256':body['radial_evidence_sha256'],
            'third_endpoint_evidence_sha256':body['third_endpoint_evidence_sha256']}


def covered_body(run,slabs,extension):
    """Verify full material coverage and consume the same paid true-tail receipt without rerunning it."""
    origin=material.identity(run)
    data,_=run.current
    radii=list(map(float,data['r']))
    visited={}
    nslabs=0
    missing=set()
    eta=0.
    ks=[]
    for s in slabs:
        i=s['paid_radial_edge']
        if (not 0<=i<len(radii)-1 or s['schema']!=SCHEMA or s['material']['origin']!=origin
                or s['material']['r_hex']!=[radii[i].hex(),radii[i+1].hex()]):
            raise ValueError('duplicate or incorrect material edge in continuous coverage')
        span=tuple(map(Fraction,s['material'].get('cell_fraction',('0','1'))))
        if not 0<=span[0]<span[1]<=1:
            raise ValueError('invalid material subinterval')
        visited.setdefault(i,[]).append(span)
        nslabs+=1
        eta=max(eta,s['metric_upper'])
        if s['max_absolute_principal_curvature_upper'] is not None:
            ks.append(s['max_absolute_principal_curvature_upper'])
        missing.update(s['unresolved_source_or_radial_errors'])
    tail=None
    if extension is not None:
        t=extension['R648']
        c=extension['R650']
        if (c['producer_sha256']!='6f41a819162387dfac71d294156e8c92963bce0c2b0486c64cac150aae95bfc3'
                or t['producer_sha256']!='82258e61964f97f89c27c192c85acb1d52f43b63a486dcc53fde2bd3cefb875f'
                or extension['actual_response_sha256']!=origin['q'] or extension['original_R643_tail_receipt_sha256']!=origin['paid_tail']
                or t['same_target_sha256']!=origin['target'] or t['actual_response_sha256']!=origin['q']
                or t['same_literal_source_contract_sha256']!=origin['contract']
                or t['consumed_preceding_tail_receipt_sha256']!=origin['paid_tail']
                or c['consumed_R648_receipt_sha256']!=material.germ.sha(material.germ.canonical(t))
                or c['old_source_error_accounting']!=run.tail.contract['source_error_accounting']):
            raise ValueError('different already-paid whole-tail evidence')
        mouth=t['true_original_numerical_mouth']
        if not mouth['lo']<=radii[0]<=mouth['hi']:
            raise ValueError('true tail does not match first interior ring')
        sh=c['R649_same_actual_tail_curvature']
        tail={'metric_upper':t['whole_true_tail_actual_relative_metric_operator_upper']['hi'],
              'absolute_curvature_upper':sh.get('actual_absolute_principal_curvature_upper',{}).get('hi'),
              'source_evidence':c['actual_same_field_and_source_errors']}
        if tro:=tail['source_evidence'].get('unresolved_errors'):
            missing.update(str(x.get('category',x)) if isinstance(x,dict) else str(x) for x in tro)
        eta=max(eta,tail['metric_upper'])
    full=0
    for spans in visited.values():
        spans=sorted(spans)
        if any(a[1]>b[0] for a,b in zip(spans,spans[1:])):
            raise ValueError('overlapping or repeated material edges')
        full+=int(spans[0][0]==0 and spans[-1][1]==1 and all(a[1]==b[0] for a,b in zip(spans,spans[1:])))
    complete=full==len(radii)-1
    return {'schema':SCHEMA,'origin':origin,'covered_finite_edges':full,'reported_material_subslabs':nslabs,'required_finite_edges':len(radii)-1,
            'finite_plus_true_tail_coverage':complete and tail is not None,
            'maximum_metric_upper_on_covered_pieces':eta if visited or tail is not None else None,
            'maximum_curvature_upper_on_covered_pieces':(
                max(ks+([tail['absolute_curvature_upper']] if tail else []))
                if (ks or tail) and len(ks)==nslabs and (tail is None or tail['absolute_curvature_upper'] is not None) else None),
            'true_tail':tail,'unresolved_source_or_radial_errors':sorted(missing),
            'outer_regular_collar_not_covered':[radii[-1],float(run.model.par.R)],
            'whole_closed_surface_or_time_family_certified':False}

class ExistingMaterialCover:
    """Use the next necessary R643 body instance; caches belong to this single accepted q."""
    def __init__(self,run):
        self.origin=material.identity(run)
        self.grid=material.paid_grid(run)
        self.nodes={}
        self.vertices={}
        self.run=run

    def node(self,i):
        if i not in self.nodes:
            self.nodes[i]=material.source_node(self.run,i)
        return self.nodes[i]

    def edge(self,i,bundle,*,angular_refinement=1,degree=3,check=None):
        if material.identity(self.run)!=self.origin or type(angular_refinement) is not int or angular_refinement<1:
            raise ValueError('existing accepted data or positive angular refinement differs')
        a,b=self.node(i),self.node(i+1)
        n=len(self.run.current[0]['theta'])*angular_refinement
        area=material.radial_cell(a,b,**bundle['edge'])
        body=ring_values(area,n,degree,check)
        ends=[]
        for k,node,spec in ((i,a,bundle.get('left')),(i+1,b,bundle.get('right'))):
            if spec is None:
                ends.append(None)
                continue
            point=material.radial_cell(node,node,**spec)
            key=(k,n,degree,tuple(sorted(point['source_evidence_sha256'].items())),
                 point['third_endpoint_evidence_sha256'])
            if key not in self.vertices:
                self.vertices[key]=ring_values(point,n,degree,check)
            ends.append(self.vertices[key])
        return slab(self.run,i,body,*ends)
