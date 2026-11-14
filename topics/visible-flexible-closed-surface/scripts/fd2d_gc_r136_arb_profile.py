"""The accurate R136 physical radial profile, with explicit Arb remainders.

The target is the shared-jet/phase-integral definition in R136. Candidate's
40-point Gauss evaluations are not defining constants or dense polynomials.
This module neither changes g nor equates independently evaluated sin(phi)
jets to derivatives of a numerical quadrature/interpolation program.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import copy
import gzip
import hashlib
import json

import numpy as np
from flint import arb, ctx

from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_current_native_interval import (
    aq,rational,rational_pair,interval,power,square,bound_record,
    UnresolvedInterval,ProfileBox)

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
SCHEMA='fd2d-R136-accurate-physical-profile-Arb-v1'
RAMP=F(2,25)
AREA=F(23,25)
TARGET_RADIUS=F(4,5)


def dyadic_endpoint(value):
    m,e=value.man_exp()
    return F(int(m))*F(2)**int(e)


def ends(value):
    return dyadic_endpoint(value.lower()),dyadic_endpoint(value.upper())


def hull(values):
    values=list(values)
    if not values:raise ValueError('Empty interval hull')
    out=values[0]
    for value in values[1:]:out=out.union(value)
    return out


def _encode(value):
    if isinstance(value,arb):
        return {'arb_dyadic_endpoints':[rational_pair(q) for q in ends(value)]}
    if isinstance(value,F):return {'exact_rational':rational_pair(value)}
    if isinstance(value,dict):return {k:_encode(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [_encode(v) for v in value]
    if isinstance(value,np.generic):return value.item()
    return value


def _decode(value):
    if isinstance(value,dict):
        if set(value)=={'arb_dyadic_endpoints'}:
            lo,hi=(F(int(n),int(d)) for n,d in value['arb_dyadic_endpoints'])
            return interval(lo,hi)
        if set(value)=={'exact_rational'}:
            n,d=value['exact_rational'];return F(int(n),int(d))
        return {k:_decode(v) for k,v in value.items()}
    if isinstance(value,list):return [_decode(v) for v in value]
    return value


def _moment(row):
    def endpoint(data):
        sign,m,e,bits=map(int,data)
        return F(-m if sign else m)*F(2)**e
    return interval(endpoint(row['binary_lower']),endpoint(row['binary_upper']))


def poly_add(a,b):
    out=[arb(0) for unused in range(max(len(a),len(b)))]
    for j,v in enumerate(a):out[j]+=v
    for j,v in enumerate(b):out[j]+=v
    return out


def poly_scale(a,b):return [v*b for v in a]


def poly_mul(a,b):
    out=[arb(0) for unused in range(len(a)+len(b)-1)]
    for j,v in enumerate(a):
        for k,w in enumerate(b):out[j+k]+=v*w
    return out


def derivative(a,order=1):
    a=list(a)
    for unused in range(order):a=[j*a[j] for j in range(1,len(a))]
    return a or [arb(0)]


def poly_value(a,t):
    out=arb(0)
    for value in reversed(a):out=out*t+value
    return out


def affine(a,offset,scale):
    out=[arb(0)]
    for value in reversed(a):
        out=poly_mul(out,[offset,scale]);out[0]+=value
    return out[:len(a)]


def bernstein_range(a,lo,hi):
    """Finite exact polynomial range after affine restriction to [0,1]."""
    lo,hi=map(rational,(lo,hi))
    if lo>hi:raise ValueError('Reversed polynomial range')
    if lo==hi:return poly_value(a,aq(lo))
    p=affine(a,aq(lo),aq(hi-lo));n=len(p)-1
    return hull(sum((aq(F(comb(i,j),comb(n,j)))*p[j] for j in range(i+1)),arb(0))
                for i in range(n+1))


def hermite(length,j0,j1):
    c0,c1,c2=aq(j0[0]),length*aq(j0[1]),length*length*aq(j0[2])/2
    d=aq(j1[0])-c0-c1-c2
    v=length*aq(j1[1])-c1-2*c2
    b=length*length*aq(j1[2])-2*c2
    return [c0,c1,c2,10*d-4*v+b/2,-15*d+7*v-b,6*d-3*v+b/2]


def phase_branches(piece):
    p0,p1,L=piece['p0'],piece['p1'],piece.get('L')
    d=p1-p0;kind=piece['kind']
    if kind=='turn':
        left=[arb(0),arb(0),arb(0),aq(1/(RAMP*RAMP)),aq(-1/(2*RAMP**3))]
        middle=[aq(-RAMP/2),arb(1)]
        right=[aq(AREA)]
        for n,factor in ((3,-1/(RAMP*RAMP)),(4,1/(2*RAMP**3))):
            right=poly_add(right,[aq(factor*comb(n,j)*(-1)**j) for j in range(n+1)])
        out=[]
        for lo,hi,values in ((F(0),RAMP,left),(RAMP,AREA,middle),(AREA,F(1),right)):
            values=poly_scale(values,d/aq(AREA));values[0]+=p0
            out.append((lo,hi,values))
        return out
    if kind=='phase_bridge':
        q0,q1=L*piece['ps0'],L*piece['ps1']
        return [(F(0),F(1),[p0,q0,3*d-2*q0-q1,-2*d+q0+q1])]
    if kind=='brake':return [(F(0),F(1),[p0,arb(0),d])]
    if kind in ('coast','coast_to'):return [(F(0),F(1),[p0])]
    raise ValueError('Unsupported explicit phase kind '+str(kind))


def sine_taylor_branch(phi,lo,hi,order):
    """Polynomial integral with a real-axis, explicit uniform remainder."""
    center,width=(lo+hi)/2,(hi-lo)/2
    shifted=affine(phi,aq(center),aq(width))
    constant=shifted[0];delta=list(shifted);delta[0]=arb(0)
    radius=sum((abs(v).upper() for v in delta[1:]),arb(0)).upper()
    sn,cs=constant.sin_cos();cycle=(sn,cs,-sn,-cs)
    sine=[arb(0)];term=[arb(1)]
    for k in range(order+1):
        sine=poly_add(sine,poly_scale(term,cycle[k%4]/factorial(k)))
        if k!=order:term=poly_mul(term,delta)
    remainder=(power(radius,order+1)/factorial(order+1)).upper()
    normalized=aq(width)*sum((aq(F(2,j+1))*sine[j] for j in range(0,len(sine),2)),arb(0))
    error=(aq(hi-lo)*remainder).upper()
    normalized+=(-error).union(error)
    primitive=[arb(0)]+[aq(width)*v/(j+1) for j,v in enumerate(sine)]
    primitive[0]-=poly_value(primitive,arb(-1))
    return dict(lo=lo,hi=hi,phi=phi,phi_sine_polynomial=sine,
        normalized_primitive=primitive,normalized_integral=normalized,
        phase_delta_radius=radius,uniform_sine_remainder=remainder,
        normalized_integral_error=error,
        centered_coordinate='y=(2*tau-lo-hi)/(hi-lo)')


def _raw_rational(value):
    return rational(value)


def _phase_end_derivative(raw,piece,at):
    kind=piece['kind']
    if kind=='phase_bridge':return piece['ps0' if at==0 else 'ps1']
    if kind=='brake':return arb(0) if at==0 else 2*(piece['p1']-piece['p0'])/piece['L']
    return arb(0)


class R136ArbProfile:
    """Accurate fixed physical target; derivatives are its true derivatives.

    ``piece_box`` specifies a named one-sided branch without confusing a
    rounded resolved knot with the accurate physical endpoint. ``physical_box``
    evaluates actual fixed physical s and unions all possibly intersected
    accurate pieces. The separate ``endpoint_jets`` uses the exact cut label.
    """
    def __init__(self,candidate,*,moments=ROOT/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json',
            radius_certificate=ROOT/'notes/2026-11-12-fd2d-peak-spacer34-radius-certificate-02.json',
            field_arrays=None,precision=256,taylor_order=24):
        if int(precision)<128 or int(taylor_order)<12:
            raise ValueError('Use a declared interval precision and explicit Taylor order')
        ctx.prec=int(precision)
        self.precision,self.order=int(precision),int(taylor_order)
        self.paths=dict(candidate=Path(candidate),moments=Path(moments),radius_certificate=Path(radius_certificate))
        self.inputs={k:identity(p) for k,p in self.paths.items()}
        bundle=json.loads(Path(candidate).read_text())
        certificate=json.loads(Path(radius_certificate).read_text())
        moment=json.loads(Path(moments).read_text())
        if (not certificate.get('passed') or certificate.get('candidate_sha256')!=self.inputs['candidate']['sha256']
                or certificate.get('a0_source_sha256')!=self.inputs['moments']['sha256']):
            raise ValueError('R136 radius proof does not bind this candidate/a0 input')
        if (bundle.get('schema')!='fd2d-frozen-ellipse-metric-v2-shared-jets'
                or bundle.get('ellipse')!={'A':1.4,'B':.5}
                or bundle.get('cut',{}).get('r')!=.8
                or bundle['segments'][-1].get('exact_endpoint_phase')!='-pi/2'):
            raise ValueError('This consumer binds the explicit R136 flat-cut target only')
        self.bundle=bundle
        self.a0=_moment(moment['enclosures']['a0'])
        self.symbolic_cut=aq(TARGET_RADIUS)
        self.base_lower=TARGET_RADIUS
        self.delta=tuple();self.supports=tuple();self.field_binding=None
        if field_arrays is not None:self._bind_bumps(field_arrays)
        self.pieces,self.join_identities=self._resolve()
        self.end=self.pieces[-1]['s1']
        self.central_length=rational(bundle['segments'][0]['L'])
        if any(left<=self.central_length or right>=ends(self.end)[0] for left,right in self.supports):
            raise ValueError('Saved physical bumps must avoid the accurate central and cut neighborhoods')
        self.source=identity(__file__)
        self.input_binding_sha256=self._content_binding()

    def _content_binding(self):
        data=dict(schema=SCHEMA,inputs={k:dict(bytes=v['bytes'],sha256=v['sha256']) for k,v in self.inputs.items()},
            source_sha256=identity(__file__)['sha256'],precision=self.precision,order=self.order,
            delta=[rational_pair(v) for v in self.delta],supports=[[rational_pair(v) for v in p] for p in self.supports],
            semantic_geometry=dict(ellipse_A='7/5',ellipse_B='1/2',cut_radius='4/5',terminal_phase='-pi/2',
                ramp='2/25',ramp_integral='23/25',other_raw_inputs='binary64 dyadic'))
        return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()

    def _bind_bumps(self,field_arrays):
        saved=load_npz(field_arrays)
        if str(saved['profile_kind'])!='physical_bumps':raise ValueError('Expected fixed physical-s bumps')
        if str(saved['candidate_sha256'])!=self.inputs['candidate']['sha256']:
            raise ValueError('Actual field and accurate base candidate differ')
        shallow=[p for p in self.bundle['segments'] if p.get('label')=='partial_return_matching_coast']
        if len(shallow)!=1 or float(saved['fixed_base_T'])!=float(shallow[0]['L']):
            raise ValueError('The saved fixed base coast parameter differs from this accurate candidate')
        counts=[int(saved[k]) for k in ('central_parameter_count','tail_parameter_count','profile_count')]
        p=np.asarray(saved['parameters'])
        supports=np.asarray(saved['profile_supports'])
        if p.dtype!=np.float64 or p.shape!=(sum(counts),) or supports.shape!=(counts[2],2):
            raise ValueError('Explicit independent-tail/profile layout is required')
        if not np.all(np.isfinite(p)) or not np.all(np.isfinite(supports)):
            raise ValueError('Nonfinite actual physical input')
        self.delta=tuple(rational(v) for v in p[counts[0]+counts[1]:])
        self.supports=tuple(tuple(rational(v) for v in row) for row in supports)
        if any(a>=b for a,b in self.supports):raise ValueError('A bump support has nonpositive width')
        self.paths['field_arrays']=Path(field_arrays)
        self.inputs['field_arrays']=identity(field_arrays)
        self.field_binding=dict(layout=dict(central=[0,counts[0]],tail=[counts[0],sum(counts[:2])],
            profile=[sum(counts[:2]),sum(counts)]),saved_mesh_sha256=hashlib.sha256(
                np.ascontiguousarray(saved['mesh']).tobytes()).hexdigest(),
            native_profile_kind='physical_bumps',computational_coordinate='physical s',
            field_representation_kind=str(saved['representation_kind']))

    def _resolve(self):
        raw=copy.deepcopy(self.bundle['segments'])
        pieces=[];pv=pa=pp=arb(0);pp_exact=F(0);previous_raw=None
        joins=[]
        for index,source in enumerate(raw):
            p=dict(index=index,kind=source['kind'],label=source.get('label',''),raw=source)
            if 'L' in source:
                p['L_exact']=rational(source['L']);p['L']=aq(p['L_exact'])
            if p['kind']=='hermite':
                if 'jet0' not in source or 'jet1' not in source:
                    raise ValueError('Shared raw Hermite jets are required')
                p['jet0']=tuple(map(rational,source['jet0']));p['jet1']=tuple(map(rational,source['jet1']))
                p['radius_polynomial']=hermite(p['L'],p['jet0'],p['jet1']);p['radius_polynomial'][0]+=self.a0
                pv,pa,pp=aq(p['jet1'][1]),aq(p['jet1'][2]),None;pp_exact=None
                if index==1:
                    ok=previous_raw['kind']=='coast' and previous_raw['p0']==0 and p['jet0']==(F(0),F(0),F(0))
                    reason='constant cylinder and exact zero initial shared jet'
                else:
                    ok=previous_raw['kind']=='hermite' and previous_raw['jet1']==source['jet0']
                    reason='identical shared Hermite endpoint jets'
            else:
                p['p0_exact']=rational(source.get('p0',0));p['p0']=aq(p['p0_exact'])
                p['p1_exact']=rational(source.get('p1',source.get('p0',0)));p['p1']=aq(p['p1_exact'])
                if source.get('start_from_previous'):
                    if pp is None:
                        if not pv>-1 or not pv<1:raise UnresolvedInterval('Initial exact asin branch not resolved')
                        p['p0']=pv.asin();p['p0_exact']=None
                    else:p['p0'],p['p0_exact']=pp,pp_exact
                if 'end_phase_add' in source:
                    p['p1']=p['p0']+aq(source['end_phase_add'])
                    p['p1_exact']=(None if p['p0_exact'] is None else p['p0_exact']+rational(source['end_phase_add']))
                if 'end_radial_speed' in source:
                    p['p1']=aq(source['end_radial_speed']).asin();p['p1_exact']=None
                if source.get('exact_endpoint_phase')=='-pi/2':
                    p['p1']=-arb.pi()/2;p['p1_exact']=None
                if p['kind'] in ('coast','coast_to'):
                    p['p1'],p['p1_exact']=p['p0'],p['p0_exact']
                if source.get('length_from_turn_rate'):
                    denominator=rational(source['K'])*AREA
                    if p['p0_exact'] is not None and p['p1_exact'] is not None:
                        p['L_exact']=abs(p['p1_exact']-p['p0_exact'])/denominator;p['L']=aq(p['L_exact'])
                    else:
                        p['L_exact']=None;p['L']=abs(p['p1']-p['p0'])/aq(denominator)
                for key in ('ps0','ps1'):
                    if key in source:p[key]=aq(source[key])
                if source.get('start_second_from_previous'):
                    cosine=p['p0'].cos()
                    if not cosine>0:raise UnresolvedInterval('Inherited phase derivative has an unresolved cosine')
                    p['ps0']=pa/cosine
                if source.get('end_from_cut'):
                    raise ValueError('R136 has an explicitly flat phase bridge, not the older w-dividing brake')
                if index:
                    before=pieces[-1]
                    phase_shared=bool(source.get('start_from_previous'))
                    if before['kind']=='hermite':
                        derivative_shared=(before['jet1'][2]==0 and p['kind'] in ('coast','turn'))
                        reason='asin of shared Hermite speed, zero terminal acceleration and common radius'
                    elif source.get('start_second_from_previous'):
                        derivative_shared=True;reason='shared phase and inherited exact second radial jet'
                    else:
                        last_raw=raw[index-1]
                        old_ps=(rational(last_raw.get('ps1',0)) if before['kind']=='phase_bridge' else F(0))
                        new_ps=(rational(source.get('ps0',0)) if p['kind']=='phase_bridge' else F(0))
                        derivative_shared=old_ps==new_ps
                        reason='shared phase and matching phase derivative; radius inherited by integration'
                    ok=phase_shared and derivative_shared
                else:
                    ok=(p['kind']=='coast' and p['p0_exact']==0 and p['L_exact']>0)
                    reason='explicit initial constant cylinder'
                p['branches']=[sine_taylor_branch(phi,lo,hi,self.order) for lo,hi,phi in phase_branches(p)]
                p['normalized_integral']=sum((b['normalized_integral'] for b in p['branches']),arb(0))
                pp,pp_exact=p['p1'],p['p1_exact'];pv=pp.sin()
                pa=pp.cos()*_phase_end_derivative(source,p,1)
            if not ok:raise ValueError('R136 shared two-jet identity was not established at raw piece '+str(index))
            if index:joins.append(dict(left=index-1,right=index,identity=reason,exact_shared_two_jet=True))
            pieces.append(p);previous_raw=source
        s=arb(0);s_exact=F(0);radius=self.a0
        for index,p in enumerate(pieces):
            source=raw[index]
            p['s0'],p['s0_exact'],p['a_start']=s,s_exact,radius
            if p['kind']=='coast_to':
                if source.get('radius_after_next')!=.8 or index+1!=len(pieces)-1:
                    raise ValueError('The only derived coast must compensate the exact final 4/5 cut')
                following=pieces[index+1]
                target=self.symbolic_cut-following['L']*following['normalized_integral']
                velocity=p['p0'].sin()
                if not velocity<0:raise UnresolvedInterval('Final deep coast direction unresolved')
                p['L']=(target-radius)/velocity;p['L_exact']=None;radius=target
            elif p['kind']=='hermite':radius=self.a0+aq(p['jet1'][0])
            else:radius+=p['L']*p['normalized_integral']
            if not p['L']>0:raise UnresolvedInterval('An accurate physical piece length is not strictly positive')
            if index==len(pieces)-1:
                if p['label']!='cut_second_jet_brake' or source.get('ps1')!=0:
                    raise ValueError('The exact final flat two-jet contract changed')
                # The preceding coast was defined to make this an identity.
                radius=self.symbolic_cut
            p['a_end']=radius;p['s1']=s+p['L']
            p['s1_exact']=(None if s_exact is None or p.get('L_exact') is None else s_exact+p['L_exact'])
            s,s_exact=p['s1'],p['s1_exact']
            if p['kind']!='hermite':
                running=p['a_start']
                for b in p['branches']:
                    b['radius_polynomial']=poly_scale(b['normalized_primitive'],p['L'])
                    b['radius_polynomial'][0]+=running
                    b['radius_error']=(abs(p['L']).upper()*aq(b['hi']-b['lo'])*b['uniform_sine_remainder']).upper()
                    b['radius_left']=running
                    running+=p['L']*b['normalized_integral']
                    b['radius_right']=running
        return pieces,joins

    def _bump_jets(self,s_lo,s_hi,order=3):
        lo,hi=map(rational,(s_lo,s_hi));out=[arb(0) for unused in range(order+1)]
        for delta,(left,right) in zip(self.delta,self.supports):
            if delta==0 or hi<=left or lo>=right:continue
            width=right-left
            tl,tr=max(F(0),(lo-left)/width),min(F(1),(hi-left)/width)
            t=interval(tl,tr)
            for d in range(order+1):
                if d==0:
                    # The exact scalar range of t(1-t) avoids losing the
                    # rigorous 0<=psi<=1 bound on a wide physical box.
                    endpoint=(tl*(1-tl),tr*(1-tr))
                    ql=min(endpoint)
                    qr=F(1,4) if tl<=F(1,2)<=tr else max(endpoint)
                    value=aq(1024*delta)*interval(ql**5,qr**5)
                else:
                    value=arb(0)
                    for k in range(d+1):
                        j=d-k;factor=comb(d,k)*factorial(5)//factorial(5-k)
                        factor*=((-1)**j)*factorial(5)//factorial(5-j)
                        value+=factor*power(t,5-k)*power(1-t,5-j)
                    value*=aq(1024*delta/(width**d))
                if lo<left or hi>right:value=value.union(arb(0))
                out[d]+=value
        return out

    def _finish(self,base,s_lo,s_hi,metadata):
        # R136 supplies an independent global base-radius lower bound.
        lower=max(base[0].lower(),aq(self.base_lower).lower())
        if lower>base[0].upper():raise ArithmeticError('Interval conflicts with the bound R136 radius theorem')
        base=list(base);base[0]=lower.union(base[0].upper())
        increments=self._bump_jets(s_lo,s_hi)
        values=[a+b for a,b in zip(base,increments)]
        a,ap,app,appp=values
        result=dict(a=a,a_s=ap,a_ss=app,a_sss=appp,base_jets=tuple(base),bump_jets=tuple(increments),
            physical_coordinate='s',true_analytic_derivatives=True,
            radial_third_derivative_scope='piecewise one-sided or hull of the explicitly listed sides',
            input_binding_sha256=self.input_binding_sha256,**metadata)
        if a>0:
            result.update(c=ap/a,K=-app/a,K_s=-appp/a+app*ap/(a*a),
                          target_metric_positive_on_box=True)
        else:
            result.update(c=None,K=None,K_s=None,target_metric_positive_on_box=False)
        return result

    def piece_box(self,index,t_lo=0,t_hi=1,*,include_bumps=True):
        p=self.pieces[int(index)];lo,hi=map(rational,(t_lo,t_hi))
        if not 0<=lo<=hi<=1:raise ValueError('Use a normalized accurate piece interval in [0,1]')
        jets=[]
        if p['kind']=='hermite':
            c=p['radius_polynomial']
            base=[bernstein_range(derivative(c,d),lo,hi)/power(p['L'],d) for d in range(4)]
            if lo==hi and lo in (0,1):
                raw=p['jet0' if lo==0 else 'jet1']
                base[:3]=[self.a0+aq(raw[0]),aq(raw[1]),aq(raw[2])]
            jets.append(base)
        else:
            for branch in p['branches']:
                l,r=max(lo,branch['lo']),min(hi,branch['hi'])
                if l>r:continue
                phi=bernstein_range(branch['phi'],l,r)
                ps=bernstein_range(derivative(branch['phi']),l,r)/p['L']
                pss=bernstein_range(derivative(branch['phi'],2),l,r)/(p['L']*p['L'])
                sn,cs=phi.sin_cos()
                yl=(2*l-branch['lo']-branch['hi'])/(branch['hi']-branch['lo'])
                yr=(2*r-branch['lo']-branch['hi'])/(branch['hi']-branch['lo'])
                radius=poly_value(branch['radius_polynomial'],interval(yl,yr))
                error=branch['radius_error'];radius+=(-error).union(error)
                if lo==hi==0:radius=p['a_start']
                if lo==hi==1:radius=p['a_end']
                jets.append([radius,sn,cs*ps,cs*pss-sn*square(ps)])
        if not jets:raise ValueError('No accurate analytic branch covers the requested interval')
        base=[hull(row[d] for row in jets) for d in range(4)]
        if int(index)==len(self.pieces)-1 and lo==hi==1:
            # This is a target-radius identity: cos(-pi/2)=0 and phi_s=0.
            # It does not assign a radial derivative to any R155 II field.
            base[:4]=[self.symbolic_cut,arb(-1),arb(0),arb(0)]
        physical=p['s0']+p['L']*interval(lo,hi)
        sl,sr=ends(physical)
        metadata=dict(piece_indices=[int(index)],normalized_interval=[rational_pair(lo),rational_pair(hi)],
            physical_s_enclosure=physical,complete_requested_domain=True,
            coordinate='named accurate physical piece',side=('right' if lo==hi==0 else 'left' if lo==hi==1 else 'piece interior/closed box'))
        if include_bumps:return self._finish(base,sl,sr,metadata)
        return dict(a=base[0],a_s=base[1],a_ss=base[2],a_sss=base[3],base_jets=tuple(base),**metadata)

    def physical_box(self,s_lo,s_hi,*,side='both'):
        lo,hi=map(rational,(s_lo,s_hi))
        if side not in ('left','right','both'):raise ValueError('Explicit radial side must be left, right or both')
        if lo>hi or lo<0 or hi>ends(self.end)[0]:
            raise UnresolvedInterval('Fixed physical interval is not proved inside the accurate domain; use endpoint_jets for the true cut')
        boxes=[];indices=[]
        for p in self.pieces:
            start,end=ends(p['s0']),ends(p['s1'])
            if hi<start[0] or lo>end[1]:continue
            if lo==hi and p.get('s0_exact')==lo and side=='left' and p['index']!=0:continue
            if lo==hi and p.get('s1_exact')==lo and side=='right' and p['index']!=len(self.pieces)-1:continue
            tau=(interval(lo,hi)-p['s0'])/p['L'];tl,tr=ends(tau)
            tl,tr=max(F(0),tl),min(F(1),tr)
            if tl>tr:continue
            boxes.append(self.piece_box(p['index'],tl,tr,include_bumps=False));indices.append(p['index'])
        if not boxes:raise UnresolvedInterval('Accurate physical piece membership was not enclosed')
        base=[hull(q[key] for q in boxes) for key in ('a','a_s','a_ss','a_sss')]
        return self._finish(base,lo,hi,dict(piece_indices=indices,physical_s_exact=[rational_pair(lo),rational_pair(hi)],
            complete_requested_domain=True,coordinate='fixed accurate physical s',requested_side=side,
            possible_piece_sides_unioned=len(indices)>1))

    def endpoint_jets(self):
        # Bumps are known to be supported away from the true cut only after
        # the accurate endpoint lower enclosure has been checked.
        if any(right>=ends(self.end)[0] for unused,right in self.supports):
            raise UnresolvedInterval('A declared physical bump may reach the accurate cut')
        result=self.piece_box(len(self.pieces)-1,1,1)
        result.update(coordinate='true accurate cut label, not rounded Candidate.end',
                      accurate_physical_endpoint=self.end,exact_two_jet_identity=True,
                      s_third_side='interior/left')
        return result

    def interface_jets(self,index):
        if not 1<=int(index)<len(self.pieces):raise ValueError('Expected an internal raw piece interface')
        return dict(left=self.piece_box(index-1,1,1),right=self.piece_box(index,0,0),
            shared_two_jet_identity=self.join_identities[index-1],
            common_third_jet_claimed=False,accurate_interface=self.pieces[index]['s0'])

    def shifted(self,removed_cylinder_length):return ShiftedR136ArbProfile(self,removed_cylinder_length)

    def definition(self):
        lower=self.base_lower+sum((min(F(0),v) for v in self.delta),F(0))
        return dict(schema=SCHEMA,input_binding_sha256=self.input_binding_sha256,inputs=self.inputs,
            source=self.source,precision_bits=self.precision,taylor_order=self.order,
            target_definition='R136 shared raw two-jets and accurate phase integrals, not numerical resolved coefficients',
            exact_geometry=dict(ellipse_A='7/5',ellipse_B='1/2',cut_radius='4/5',terminal_phase='-pi/2',
                                ramp='2/25',ramp_integral='23/25'),
            raw_input_semantics='Other raw numerical data are their binary64 dyadic rationals; derived phase/length/integral values remain accurate analytic quantities.',
            a0=bound_record(self.a0),accurate_physical_endpoint=bound_record(self.end),
            central_cylinder_length=rational_pair(self.central_length),
            piece_count=len(self.pieces),analytic_phase_branch_count=sum(len(p.get('branches',[])) for p in self.pieces),
            join_identities=self.join_identities,
            field_binding=self.field_binding,physical_delta_exact=[rational_pair(v) for v in self.delta],
            bump_supports_exact=[[rational_pair(v) for v in row] for row in self.supports],
            continuous_global_radius_lower_exact=rational_pair(lower),
            target_metric_positive_by_R136_bound=bool(lower>0),
            derivative_semantics='True derivatives of the accurate analytic target; one-sided a_sss and K_s, no extra global C3 requirement.',
            runtime_radius_evaluator='Candidate.phase_integral: 40-point floating Gauss per explicit phase branch; no profile ODE/dense interpolation in this bound chain.',
            numerical_Gauss_evaluator_derivative_substituted=False,
            prior_floating_body_results_transferred=False,whole_embedding_certificate=False)

    def save_packet(self,path):
        path=Path(path)
        if path.exists():raise FileExistsError(path)
        payload=dict(definition=self.definition(),bundle=self.bundle,pieces=self.pieces,
            a0=self.a0,end=self.end,central_length=self.central_length,delta=self.delta,supports=self.supports,
            precision=self.precision,order=self.order,inputs=self.inputs,join_identities=self.join_identities,
            field_binding=self.field_binding,source=self.source,input_binding_sha256=self.input_binding_sha256)
        raw=(json.dumps(_encode(payload),sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
        if path.suffix=='.gz':
            with path.open('wb') as stream:
                with gzip.GzipFile(filename='',fileobj=stream,mode='wb',mtime=0) as out:out.write(raw)
        else:path.write_bytes(raw)
        return dict(**identity(path),uncompressed_bytes=len(raw),uncompressed_sha256=hashlib.sha256(raw).hexdigest())

    @classmethod
    def from_packet(cls,path,*,expected_sha256=None):
        path=Path(path);raw=gzip.decompress(path.read_bytes()) if path.suffix=='.gz' else path.read_bytes()
        packet_identity=identity(path)
        if expected_sha256 is not None and packet_identity['sha256']!=expected_sha256:
            raise ValueError('The actual closed profile packet hash differs')
        encoded=json.loads(raw)
        ctx.prec=max(int(ctx.prec),int(encoded['precision']))
        data=_decode(encoded)
        if data['definition']['schema']!=SCHEMA or data['source']['sha256']!=identity(__file__)['sha256']:
            raise ValueError('Wrong packet schema or actual interval source')
        ctx.prec=max(int(ctx.prec),int(data['precision']))
        obj=cls.__new__(cls)
        for name in ('bundle','pieces','a0','end','central_length','delta','supports','precision','order',
                     'inputs','join_identities','field_binding','source','input_binding_sha256'):
            setattr(obj,name,data[name])
        obj.paths={k:Path(v['path']) for k,v in obj.inputs.items()}
        obj.symbolic_cut=aq(TARGET_RADIUS);obj.base_lower=TARGET_RADIUS
        if obj._content_binding()!=obj.input_binding_sha256:
            raise ValueError('Profile packet input binding or exact physical parameters changed')
        obj.packet_identity=packet_identity
        return obj


class ShiftedR136ArbProfile:
    """Exact translation of the parent's restricted physical domain.

    This is a scalar view for the declared removal of part of the initial
    cylinder, not a claim that deleting a cylinder preserves the original
    untrimmed domain. The parent's accurate cut is translated as a label.
    """
    def __init__(self,parent,removed_cylinder_length):
        self.parent=parent;self.shift=rational(removed_cylinder_length)
        if not 0<=self.shift<parent.central_length:
            raise ValueError('Only an exact sublength of the initial constant cylinder is removed')
        self.end=parent.end-aq(self.shift)

    def physical_box(self,s_lo,s_hi,*,side='both'):
        result=self.parent.physical_box(rational(s_lo)+self.shift,rational(s_hi)+self.shift,side=side)
        return dict(result,coordinate='new physical s, parent s=new s+exact shift',shift_exact=rational_pair(self.shift))

    def endpoint_jets(self):
        result=self.parent.endpoint_jets()
        return dict(result,accurate_physical_endpoint=self.end,shift_exact=rational_pair(self.shift),
                    parent_cut_label_used=True)

    def definition(self):
        return dict(schema='fd2d-R136-exact-cylinder-restriction-translation-v1',
            parent_binding_sha256=self.parent.input_binding_sha256,shift_exact=rational_pair(self.shift),
            formula='a_new(s)=a_parent(s+shift); the same translation applies to every saved physical bump',
            accurate_physical_endpoint=bound_record(self.end),new_cylinder_length=rational_pair(self.parent.central_length-self.shift),
            new_physical_domain_is_parent_restriction=True,parent_floating_end_promoted_to_exact=False)
