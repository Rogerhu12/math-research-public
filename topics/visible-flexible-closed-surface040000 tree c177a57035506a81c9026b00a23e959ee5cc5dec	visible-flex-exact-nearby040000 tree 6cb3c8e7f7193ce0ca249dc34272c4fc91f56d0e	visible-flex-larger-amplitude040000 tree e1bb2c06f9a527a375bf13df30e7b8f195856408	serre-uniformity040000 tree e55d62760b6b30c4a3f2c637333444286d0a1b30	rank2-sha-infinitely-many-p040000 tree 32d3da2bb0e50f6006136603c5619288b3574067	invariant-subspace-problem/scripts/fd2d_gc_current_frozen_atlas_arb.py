"""Continuous Arb two-jets for the actual fixed seed/R139/R149 atlas.

The declared mathematical functions are evaluated directly. A saved endpoint
shortcut that replaces sigma=f-e by stored L is not made a second definition
of the same trace. R149 explicitly sets the outgoing whole function to N(f).
All original scalar labels, the discrepancy, and exact input identities are
retained. No approximate material inverse, PDE, or body integration is used.
"""
from __future__ import annotations
from dataclasses import dataclass,replace
from fractions import Fraction as F
from pathlib import Path
import gzip
import hashlib
import json
import numpy as np
from flint import arb,ctx

from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_current_native_interval import (
    aq,rational,rational_pair,interval,angle_interval,square,power,
    bound_record,UnresolvedInterval,Jet,ChartBox,require_positive)
from fd2d_gc_r136_arb_profile import ends,hull,_moment

HERE=Path(__file__).resolve().parent
NOTES=HERE.parent/'notes'
SCHEMA='fd2d-current-complete-frozen-R149-atlas-Arb-v1'


def record_interval(row):
    def endpoint(pair):
        if len(pair)==2:return F(int(pair[0]))*F(2)**int(pair[1])
        sign,m,e,bits=map(int,pair)
        return F(-m if sign else m)*F(2)**e
    return interval(endpoint(row['lower_binary']),endpoint(row['upper_binary']))


def intersect_lower(value,lower,label):
    lo=max(value.lower(),lower.lower())
    if lo>value.upper():raise ArithmeticError('Bound conflicts with '+label)
    return lo.union(value.upper())


@dataclass(frozen=True)
class TwoJet:
    """True six-entry jet in physical s and fixed computation label xi."""
    value: arb
    s: arb
    xi: arb
    ss: arb
    sxi: arb
    xixi: arb

    @staticmethod
    def constant(x):
        return TwoJet(x if isinstance(x,arb) else aq(x),arb(0),arb(0),arb(0),arb(0),arb(0))

    @staticmethod
    def coerce(x):return x if isinstance(x,TwoJet) else TwoJet.constant(x)

    def __add__(self,x):
        x=TwoJet.coerce(x)
        return TwoJet(*(getattr(self,k)+getattr(x,k) for k in self.keys()))
    __radd__=__add__
    def __neg__(self):return TwoJet(*(-getattr(self,k) for k in self.keys()))
    def __sub__(self,x):return self+-TwoJet.coerce(x)
    def __rsub__(self,x):return TwoJet.coerce(x)+-self

    @staticmethod
    def keys():return ('value','s','xi','ss','sxi','xixi')

    def __mul__(self,x):
        x=TwoJet.coerce(x)
        return TwoJet(self.value*x.value,
            self.s*x.value+self.value*x.s,
            self.xi*x.value+self.value*x.xi,
            self.ss*x.value+2*self.s*x.s+self.value*x.ss,
            self.sxi*x.value+self.s*x.xi+self.xi*x.s+self.value*x.sxi,
            self.xixi*x.value+2*self.xi*x.xi+self.value*x.xixi)
    __rmul__=__mul__

    def unary(self,value,first,second):
        return TwoJet(value,first*self.s,first*self.xi,
            first*self.ss+second*square(self.s),
            first*self.sxi+second*self.s*self.xi,
            first*self.xixi+second*square(self.xi))

    def reciprocal(self):
        if not(self.value>0 or self.value<0):raise UnresolvedInterval('Two-jet reciprocal contains zero')
        q=1/self.value
        return self.unary(q,-q*q,2*q*q*q)
    def __truediv__(self,x):return self*TwoJet.coerce(x).reciprocal()
    def __rtruediv__(self,x):return TwoJet.coerce(x)*self.reciprocal()
    def squared(self):return self.unary(square(self.value),2*self.value,arb(2))
    def sqrt(self):
        require_positive(self.value,'two-jet square-root value')
        q=self.value.sqrt();return self.unary(q,1/(2*q),-1/(4*q*q*q))
    def sin(self):
        sn,cs=self.value.sin_cos();return self.unary(sn,cs,-sn)
    def cos(self):
        sn,cs=self.value.sin_cos();return self.unary(cs,-sn,-cs)
    def atan(self):
        den=1+square(self.value)
        return self.unary(self.value.atan(),1/den,-2*self.value/(den*den))
    def tanh(self):
        q=self.value.tanh();d=1-square(q)
        return self.unary(q,d,-2*q*d)
    def native(self):return Jet(self.value,self.s,self.xi,self.xixi,self.sxi)
    def record(self):return {k:bound_record(getattr(self,k)) for k in self.keys()}


def union_jets(rows):
    rows=list(rows)
    if not rows:raise ValueError('No jets to union')
    return TwoJet(*(hull(getattr(r,key) for r in rows) for key in TwoJet.keys()))


def step_jet(lo,hi,left,right):
    """Whole interval C2 clamped quintic, with physical radial derivatives."""
    lo,hi,left,right=map(rational,(lo,hi,left,right))
    if lo>hi or left>=right:raise ValueError('Invalid quintic step interval')
    if hi<=left:return TwoJet.constant(0)
    if lo>=right:return TwoJet.constant(1)
    tl,tr=max(F(0),(lo-left)/(right-left)),min(F(1),(hi-left)/(right-left))
    t=interval(tl,tr);width=aq(right-left)
    def exact(q):return q*q*q*(10-15*q+6*q*q)
    value=interval(exact(tl),exact(tr))
    ds=30*square(t)*square(1-t)/width
    dss=60*t*(1-t)*(1-2*t)/(width*width)
    if lo<left or hi>right:
        ds=ds.union(arb(0));dss=dss.union(arb(0))
    return TwoJet(value,ds,arb(0),dss,arb(0),arb(0))


class FrozenAtlasArb:
    """Saved complete chart identity plus exact seed and ruling functions.

    ``parts`` is a bound CurrentNativeIntervalPieces object. Mathematical
    source input checks are inherited from that object and cross-checked
    against the old continuous R139 and exact 512-mode chart-tail packets.
    """
    def __init__(self,parts,*,moments=None,
            means=NOTES/'2026-11-12-fd2d-balanced-weighted-means-512-02.json.gz',
            chart_tail=NOTES/'2026-11-12-fd2d-balanced-chart-fourier-tail-01.json',
            ruling_proof=NOTES/'2026-11-12-fd2d-k0-ruling-angular-certificate-01.json',
            precision=256):
        ctx.prec=max(int(ctx.prec),int(precision))
        self.precision=int(ctx.prec);self.parts=parts;self.reader=parts.reader
        ref=self.reader.coast_reference
        moments=Path(ref.geometry.moments_path) if moments is None else Path(moments)
        self.paths=dict(moments=moments,means=Path(means),chart_tail=Path(chart_tail),
            ruling_proof=Path(ruling_proof),inlet=Path(ref.inlet_path))
        self.inputs={key:identity(p) for key,p in self.paths.items()}
        moment=json.loads(moments.read_text())
        packed=Path(means).read_bytes()
        uncompressed=gzip.decompress(packed) if Path(means).suffix=='.gz' else packed
        means_data=json.loads(uncompressed);tail=json.loads(Path(chart_tail).read_text())
        proof=json.loads(Path(ruling_proof).read_text())
        if (tail['schema']!='fd2d-exact-balanced-material-chart-C4-Fourier-tail-v1'
                or tail['means']['sha256']!=self.inputs['means']['sha256']
                or tail['means_uncompressed_sha256']!=hashlib.sha256(uncompressed).hexdigest()
                or tail['moments']['sha256']!=self.inputs['moments']['sha256']
                or means_data['exact_moment_report']['sha256']!=self.inputs['moments']['sha256']
                or means_data['parameters']!=moment['parameters']
                or not means_data['source_moment_intervals_remain_valid']):
            raise ValueError('The complete exact seed/chart packets are not the same input')
        candidate=identity(self.reader.candidate_path)['sha256']
        if (not proof.get('passed') or proof.get('unresolved')
                or proof['inlet_sha256']!=self.inputs['inlet']['sha256']
                or proof['moments_sha256']!=self.inputs['moments']['sha256']
                or proof['candidate_sha256']!=candidate):
            raise ValueError('The existing complete R139 proof belongs to other functions')
        self.moment=moment;self.proof=proof
        self.a0=_moment(moment['enclosures']['a0'])
        self.adjust={k:_moment(moment['enclosures'][k]) for k in ('u0','u2','u4')}
        self.seed_par={k:aq(F(moment['parameters'][k])) for k in ('r','D','c','k')}
        self.mu=[]
        for j,row in enumerate(means_data['rows'],1):
            if row['j']!=j or row['angular_mode']!=2*j:raise ValueError('Nonconsecutive material mean modes')
            enclosure=_moment(row['material_weighted_mean'])
            # Use the stored exact endpoint midpoint, not the midpoint of
            # an already rounded Arb union.
            def exact(q):
                sign,m,e,bits=map(int,q)
                return F(-m if sign else m)*F(2)**e
            data=row['material_weighted_mean']
            self.mu.append((exact(data['binary_lower'])+exact(data['binary_upper']))/2)
        if len(self.mu)!=tail['retained_even_modes'] or len(self.mu)!=512:
            raise ValueError('Use the complete bound 512-mode chart input')
        self.U_error=[_moment(row['total_uniform_error']).upper() for row in tail['rows']]
        if [q['derivative_order'] for q in tail['rows']]!=list(range(5)):
            raise ValueError('The complete chart remainder derivative orders differ')
        inlet=load_npz(ref.inlet_path)
        self.a,self.v=(aq(float(inlet[k])) for k in ('a','v'))
        self.nc=tuple(rational(v) for v in inlet['n_phi_cos'])
        self.mc=tuple(rational(v) for v in inlet['m_phi_sin'])
        self.freq=tuple(int(v) for v in inlet['frequencies'])
        if self.freq!=tuple(range(0,2*len(self.nc),2)) or len(self.mc)!=len(self.nc)-1:
            raise ValueError('Frozen inlet is not the declared finite D2 real series')
        self.metadata=self.reader.angular_atlas_definition
        self.entry_start,self.entry=map(rational,self.metadata['entry_transition'])
        e,self.exit=map(rational,self.metadata['coast'])
        f,self.exit_stop=map(rational,self.metadata['exit_transition'])
        if e!=self.entry or f!=self.exit or self.metadata['inlet_sha256']!=self.inputs['inlet']['sha256']:
            raise ValueError('The actual full atlas support/input does not match')
        self.stored_length=rational(ref.length)
        self.exit_sigma=self.exit-self.entry
        self.blend=tuple(map(rational,self.reader.blend_interval))
        if not 0<=self.entry_start<self.entry<self.exit<self.exit_stop<parts.mesh[-1]:
            raise ValueError('Actual four-patch atlas endpoints are not ordered')
        self._global_bounds(proof)
        self._angular_cache={}
        self._binding=dict(schema=SCHEMA,source=identity(__file__),native_binding_sha256=parts.binding_sha256,
            inputs=self.inputs,original_atlas_definition=self.metadata,
            exact_exit_sigma=rational_pair(self.exit_sigma),stored_reference_length=rational_pair(self.stored_length),
            difference=rational_pair(self.exit_sigma-self.stored_length),precision=self.precision,
            mathematical_semantics='R149 E(xi)=N(f,xi); sigma=s-e on the closed coast, including its endpoint',
            numerical_endpoint_shortcut='Old sigma=L at the rounded endpoint is a numerical evaluation shortcut; its difference is not silently zero',
            exact_seed='Published moment-defined rho/a0 and full U; 512-mode midpoint is only an enclosure representation',
            all_unknown_parameter_dependence=False)
        content=dict(self._binding,inputs={k:dict(bytes=v['bytes'],sha256=v['sha256']) for k,v in self.inputs.items()})
        content['source']={k:self._binding['source'][k] for k in ('bytes','sha256')}
        self.binding_sha256=hashlib.sha256(json.dumps(content,sort_keys=True,separators=(',',':')).encode()).hexdigest()

    def _global_bounds(self,proof):
        boxes=proof['boxes'];arcs=[]
        for row in boxes:
            l=F(*map(int,row['left_pi_over_two']));r=F(*map(int,row['right_pi_over_two']))
            if l>=r:raise ValueError('Nonpositive old certified angular cell')
            arcs.append((l,r))
        arcs.sort()
        if arcs[0][0]!=0 or arcs[-1][1]!=1 or any(a[1]!=b[0] for a,b in zip(arcs,arcs[1:])):
            raise ValueError('The bound R139 packet does not cover the complete quarter circle')
        pa,pv,pL=(record_interval(proof[k]) for k in ('a','v','coast_length'))
        if not pa.contains(self.a) or not pv.contains(self.v) or not pL.contains(aq(self.stored_length)):
            raise ValueError('Frozen reference scalar inputs are outside the original certified domain')
        self.n_lower=min(record_interval(row['n']).lower() for row in boxes)
        self.rho_lower=min(record_interval(row['rho']).lower() for row in boxes)
        self.D_old_lower=min(self.a.lower(),min(record_interval(row['D_end']).lower() for row in boxes))
        Bmax=max(abs(record_interval(row['B'])).upper() for row in boxes)
        rho0=self.a/self.v
        extra=max(F(0),self.exit_sigma-self.stored_length)
        # w_sigma=(rho0+sigma)/Q <= 1+sigma/rho0; D=a+w*B.
        perturb=aq(extra)*(1+aq(max(self.stored_length,self.exit_sigma))/rho0.lower())*Bmax
        self.D_lower=(self.D_old_lower-perturb).lower()
        self.h_lower=(self.rho_lower/self.a0.upper()).lower()
        require_positive(self.n_lower,'frozen full inlet n bound')
        require_positive(self.D_lower,'full ruling denominator with exact exit sigma')
        require_positive(self.h_lower,'exact seed material derivative bound')
        kabs=aq(sum(abs(v) for v in self.mc))/self.n_lower
        sigma=aq(max(self.exit_sigma,self.stored_length))
        Qmax=(rho0*rho0+(1+kabs*kabs)*sigma*(2*rho0+sigma)).sqrt().upper()
        self.ruling_Uxi_lower=(self.D_lower*self.h_lower/(self.v.upper()*Qmax)).lower()
        self.global_Uxi_lower=min(arb(1),self.h_lower,self.ruling_Uxi_lower)
        self.global_proof=dict(original_complete_box_count=len(boxes),
            n_lower=bound_record(self.n_lower),seed_h_lower=bound_record(self.h_lower),
            original_D_lower=bound_record(self.D_old_lower),
            exact_exit_extension_upper=bound_record(perturb),D_lower=bound_record(self.D_lower),
            U_xi_lower=bound_record(self.global_Uxi_lower),
            extension_formula='extra_sigma*(1+sigma_max/rho0_min)*max|B|; follows from exact w_sigma=rho/Q',
            angular_coverage='D2 exact reflection/pi-periodicity of the immutable finite inlet and exact seed',
            applies_to_reference_chart_only=True,unknown_field_n_positive_inferred=False)

    def angular(self,lo,hi,*,angle_unit='pi'):
        key=(rational(lo),rational(hi),angle_unit)
        if key in self._angular_cache:return self._angular_cache[key]
        phi=angle_interval(lo,hi,angle_unit)
        z=TwoJet(phi,arb(0),arb(1),arb(0),arb(0),arb(0))
        c2=(2*z).cos();c4=(4*z).cos();par=self.seed_par
        rho=par['r']+par['D']*(1-(par['k']*(c2-par['c'])).tanh())/2
        rho+=self.adjust['u0']+self.adjust['u2']*c2+self.adjust['u4']*c4
        rho=replace(rho,value=intersect_lower(rho.value,self.rho_lower,'certified exact seed radius'))
        h=rho/self.a0
        U=phi
        for j,mu in enumerate(self.mu,1):U+=aq(mu/j)*(2*j*phi).sin()
        error=self.U_error[0];U+=(-error).union(error)
        seed=TwoJet(U,arb(0),h.value,arb(0),arb(0),h.xi)
        n=[arb(0) for unused in range(4)];m=[arb(0) for unused in range(4)]
        for j,f in enumerate(self.freq):
            sn,cs=(f*phi).sin_cos();a=aq(self.nc[j])
            basis=(cs,-f*sn,-f*f*cs,f*f*f*sn)
            for d in range(4):n[d]+=a*basis[d]
            if j:
                b=aq(self.mc[j-1]);basis=(sn,f*cs,-f*f*sn,-f*f*f*cs)
                for d in range(4):m[d]+=b*basis[d]
        n[0]=intersect_lower(n[0],self.n_lower,'certified frozen inlet n')
        k=[m[0]/n[0]]
        k.append((m[1]-n[1]*k[0])/n[0])
        k.append((m[2]-n[2]*k[0]-2*n[1]*k[1])/n[0])
        k.append((m[3]-n[3]*k[0]-3*n[2]*k[1]-3*n[1]*k[2])/n[0])
        ku=k[1]/h.value
        kux=k[2]/h.value-k[1]*h.xi/(h.value*h.value)
        kuxx=(k[3]/h.value-2*k[2]*h.xi/(h.value*h.value)
              -k[1]*h.xixi/(h.value*h.value)+2*k[1]*square(h.xi)/(h.value*h.value*h.value))
        result=dict(phi=z,seed=seed,rho=rho,h=h,
            nc=TwoJet(n[0],arb(0),n[1],arb(0),arb(0),n[2]),
            mc=TwoJet(m[0],arb(0),m[1],arb(0),arb(0),m[2]),
            k=TwoJet(k[0],arb(0),k[1],arb(0),arb(0),k[2]),
            k_material_derivative=TwoJet(ku,arb(0),kux,arb(0),arb(0),kuxx))
        if len(self._angular_cache)>=32:self._angular_cache.pop(next(iter(self._angular_cache)))
        self._angular_cache[key]=result
        return result

    def ruling(self,lo,hi,angular,*,fixed_endpoint=False):
        lo,hi=map(rational,(lo,hi))
        if not self.entry<=lo<=hi<=self.exit:raise ValueError('The full frozen ruling formula is restricted to its saved support')
        sigma=TwoJet(interval(lo-self.entry,hi-self.entry),arb(1),arb(0),arb(0),arb(0),arb(0))
        if fixed_endpoint:sigma=TwoJet.constant(aq(self.exit_sigma))
        rho0=self.a/self.v;r=sigma+rho0;delta=sigma*(2*rho0+sigma)
        k=angular['k'];Q=(rho0*rho0+(1+k.squared())*delta).sqrt()
        w=delta/(rho0+Q);B=self.v*(1+k.squared())-angular['k_material_derivative']
        D=self.a+w*B
        D=replace(D,value=intersect_lower(D.value,self.D_lower,'complete ruling D'))
        U=angular['seed']-(k*w/(rho0+w)).atan()/self.v
        # Preserve the exact D/(vQ) cancellation before taking enclosures.
        # This is the same derivative as the differentiated angle formula.
        angular_jacobian=D*angular['h']/(self.v*Q)
        identity_residuals=dict(xi=U.xi-angular_jacobian.value,
            sxi=U.sxi-angular_jacobian.s,xixi=U.xixi-angular_jacobian.xi)
        U=replace(U,xi=intersect_lower(angular_jacobian.value,self.ruling_Uxi_lower,'complete ruling U_xi'),
            sxi=angular_jacobian.s,xixi=angular_jacobian.xi)
        n=self.a*angular['nc']*Q.squared()/(D*r.squared())
        ratio=k*rho0/Q
        return dict(U=U,fields=(n,n*ratio,n*ratio.squared()),D=D,Q=Q,
            differentiated_angle_identity_residuals=identity_residuals,
            exact_sigma=[rational_pair(lo-self.entry),rational_pair(hi-self.entry)],
            computational_label='same fixed inlet seed-normal xi',
            reference_GC_for_current_delta_asserted=False)

    def _old(self,lo,hi,angular):
        beta=step_jet(lo,hi,*self.blend)
        return angular['phi']+(1-beta)*(angular['seed']-angular['phi'])

    def _piece(self,kind,lo,hi,angular):
        if kind=='old':return self._old(lo,hi,angular)
        if kind=='entry':
            q=step_jet(lo,hi,self.entry_start,self.entry)
            return (1-q)*self._old(lo,hi,angular)+q*angular['seed']
        if kind=='coast':return self.ruling(lo,hi,angular)['U']
        if kind=='exit':
            q=step_jet(lo,hi,self.exit,self.exit_stop)
            end=self.ruling(self.exit,self.exit,angular,fixed_endpoint=True)['U']
            return (1-q)*end+q*self._old(lo,hi,angular)
        raise ValueError('Unknown actual atlas piece')

    def box(self,radial_lo,radial_hi,angular_lo,angular_hi,*,angle_unit='pi',side='both'):
        lo,hi=map(rational,(radial_lo,radial_hi))
        if side not in ('left','right','coast','both'):raise ValueError('Explicit atlas side required')
        if not self.parts.mesh[0]<=lo<=hi<=self.parts.mesh[-1]:raise ValueError('Use the recorded old domain; accurate terminal extension is a separate wrapper')
        angular=self.angular(angular_lo,angular_hi,angle_unit=angle_unit)
        pieces=[('old',self.parts.mesh[0],self.entry_start),('entry',self.entry_start,self.entry),
            ('coast',self.entry,self.exit),('exit',self.exit,self.exit_stop),('old',self.exit_stop,self.parts.mesh[-1])]
        rows=[];used=[]
        for kind,left,right in pieces:
            a,b=max(left,lo),min(right,hi)
            if a>b:continue
            if lo==hi:
                if side=='left' and left==lo and left!=self.parts.mesh[0]:continue
                if side=='right' and right==hi and right!=self.parts.mesh[-1]:continue
                if side=='coast' and lo in (self.entry,self.exit) and kind!='coast':continue
            rows.append(self._piece(kind,a,b,angular));used.append(kind)
        if not rows:raise ValueError('No atlas side selected')
        U=union_jets(rows)
        U=replace(U,xi=intersect_lower(U.xi,self.global_Uxi_lower,'global atlas positive angular derivative'))
        return dict(U=U,chart=ChartBox(U.xi,U.s,U.xixi,U.sxi),angular=angular,
            pieces=used,radial_side=side,binding_sha256=self.binding_sha256,
            full_function_coverage_of_requested_box=True,angular_inverse_used=False,
            moving_material_drift=U.s/U.xi)

    def definition(self):
        return dict(self._binding,binding_sha256=self.binding_sha256,
            complete_reference_jet_orders=['value','s','xi','ss','sxi','xixi'],
            exact_exit_alignment='One complete function N(f,xi) supplies both the closed coast and outgoing fixed trace',
            fixed_reference_parameters='Saved inlet a,v,n_phi_cos,m_phi_sin are exact dyadic inputs, independent of current profile delta',
            continuous_global_chart_positivity=self.global_proof,
            full_current_field_enclosed=False,whole_surface_certificate=False)
