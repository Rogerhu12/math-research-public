"""Accurate analytic R181 B32 profile, explicitly rebuilt from main inputs.

New recovery identity; not a rebind of an old R136 packet and not a claim
about the unavailable 87bde source bytes.  The complete scalar pieces are
resolved afresh. Local interval formulas are the frozen R171 formulas.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import copy,gzip,hashlib,json
import numpy as np
from flint import arb,ctx
from fd2d_gc_archive_arrays import identity
from fd2d_gc_r136_arb_profile import (
    R136ArbProfile,aq,rational,rational_pair,interval,ends,bound_record,
    hermite,phase_branches,sine_taylor_branch,poly_scale,UnresolvedInterval,
    _moment,_encode,_decode,_phase_end_derivative,AREA)
from fd2d_gc_r181_b_round_reference_recovery import (
    DEFAULT_CANDIDATE,CANDIDATE_SHA256,checked_candidate)

ROOT=Path(__file__).resolve().parent.parent
SCHEMA='fd2d-R181-B32-recovery-accurate-profile-Arb-v1'
TARGET_RADIUS=F(4,5)
FORMULA_SHA256='7bcc33f75b3c3264934110c71c549e18d7ad92cb2681a317980e3844c72323c6'
MOMENTS_SHA256='0da13490030b82f536a921a97083b38f606ab604e7c7195c9053fb7975fa4b03'


class R181BRecoveryArbProfile(R136ArbProfile):
    def __init__(self,candidate=DEFAULT_CANDIDATE,*,
            moments=ROOT/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json',
            field_arrays=None,supports=None,delta=None,precision=256,taylor_order=24):
        import fd2d_gc_r136_arb_profile as formula
        if int(precision)<128 or int(taylor_order)<12:
            raise ValueError('Declare interval precision and Taylor order')
        if identity(formula.__file__)['sha256']!=FORMULA_SHA256:
            raise ValueError('Frozen local interval formulas differ')
        if identity(moments)['sha256']!=MOMENTS_SHA256:
            raise ValueError('Accurate common a0 moment source differs')
        ctx.prec=int(precision);self.precision=int(precision);self.order=int(taylor_order)
        proof=ROOT/'results/R181-shorter-phase-prefixes-and-an-explicit-variable-cut-budget.md'
        self.paths=dict(candidate=Path(candidate),moments=Path(moments),
            radius_proof=proof,inherited_interval_source=Path(formula.__file__))
        self.inputs={k:identity(v) for k,v in self.paths.items()}
        self.bundle=checked_candidate(candidate)
        self.a0=_moment(json.loads(Path(moments).read_text())['enclosures']['a0'])
        self.symbolic_cut=aq(TARGET_RADIUS);self.base_lower=TARGET_RADIUS
        self.delta=tuple();self.supports=tuple();self.field_binding=None
        if field_arrays is not None:
            if supports is not None or delta is not None:
                raise ValueError('Choose saved field OR explicit new support definition')
            self._bind_bumps(field_arrays)
        elif supports is not None:
            supports=np.asarray(supports,float)
            if supports.ndim!=2 or supports.shape[1]!=2 or not len(supports):
                raise ValueError('Explicit nonempty J by 2 support array required')
            values=np.zeros(len(supports)) if delta is None else np.asarray(delta,float)
            if values.shape!=(len(supports),) or not np.all(np.isfinite(values)):
                raise ValueError('Explicit physical deltas required')
            if not np.all(np.isfinite(supports)) or np.any(supports[:,0]>=supports[:,1]):
                raise ValueError('Positive finite support widths required')
            self.supports=tuple(tuple(rational(x) for x in row) for row in supports)
            self.delta=tuple(rational(x) for x in values)
            self.field_binding=dict(kind='explicit new B32 physical supports',
                field_archive_not_claimed=True)
        elif delta is not None:
            raise ValueError('Deltas require explicitly defined supports')
        self.pieces,self.join_identities=self._resolve()
        self.end=self.pieces[-1]['s1']
        self.central_length=F(13,128)
        if rational(self.bundle['segments'][0]['L'])!=self.central_length:
            raise ValueError('Exact new central length differs')
        if any(left<=self.central_length or right>=ends(self.end)[0] for left,right in self.supports):
            raise ValueError('Supports must avoid accurate central and cut neighborhoods')
        self.source=identity(__file__)
        self.input_binding_sha256=self._content_binding()

    def _content_binding(self):
        data=dict(schema=SCHEMA,
            inputs={k:dict(bytes=v['bytes'],sha256=v['sha256']) for k,v in self.inputs.items()},
            source_sha256=identity(__file__)['sha256'],
            inherited_local_formula_sha256=FORMULA_SHA256,
            precision=self.precision,order=self.order,
            delta=[rational_pair(v) for v in self.delta],
            supports=[[rational_pair(v) for v in row] for row in self.supports],
            mathematical_target='R181 B_standard_cut; C=13/128; redeepen=9/2; cut=4/5; new exact phase integrals')
        return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()

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
                        if p['kind']=='phase_bridge' and source.get('start_second_from_previous'):
                            derivative_shared=True
                            reason='shared Hermite speed via asin and inherited exact a_ss=cos(phi)*phi_s'
                        else:
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
            if not ok:raise ValueError('R181 B32 shared two-jet identity was not established at raw piece '+str(index))
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

    def definition(self):
        out=super().definition()
        out['schema']=SCHEMA
        out['target_definition']='R181 B32 shared jets and freshly resolved accurate phase integrals'
        out['radius_proof']='R181 section 3; this exact new candidate has a>=4/5'
        out['target_metric_positive_by_R181_bound']=out.pop('target_metric_positive_by_R136_bound')
        out['inherited_local_interval_formula_sha256']=FORMULA_SHA256
        out['old_physical_packet_rebound']=False
        out['unavailable_87bde_source_bytes_recreated']=False
        return out

    @classmethod
    def from_packet(cls,path,*,expected_sha256=None):
        path=Path(path);packed=path.read_bytes()
        ident=identity(path)
        if expected_sha256 is not None and ident['sha256']!=expected_sha256:
            raise ValueError('Closed new packet hash differs')
        raw=gzip.decompress(packed) if path.suffix=='.gz' else packed
        encoded=json.loads(raw);ctx.prec=max(int(ctx.prec),int(encoded['precision']))
        data=_decode(encoded)
        if (data['definition']['schema']!=SCHEMA or
                data['source']['sha256']!=identity(__file__)['sha256'] or
                data['inputs']['candidate']['sha256']!=CANDIDATE_SHA256 or
                data['inputs']['inherited_interval_source']['sha256']!=FORMULA_SHA256):
            raise ValueError('Wrong explicit new interval schema or source identity')
        obj=cls.__new__(cls)
        for name in ('bundle','pieces','a0','end','central_length','delta','supports',
                     'precision','order','inputs','join_identities','field_binding',
                     'source','input_binding_sha256'):
            setattr(obj,name,data[name])
        obj.paths={k:Path(v['path']) for k,v in obj.inputs.items()}
        obj.symbolic_cut=aq(TARGET_RADIUS);obj.base_lower=TARGET_RADIUS
        if obj._content_binding()!=obj.input_binding_sha256:
            raise ValueError('New physical input binding changed')
        obj.packet_identity=ident
        return obj
