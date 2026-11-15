#!/usr/bin/env python3
"""Exact five-column null-height coordinates in the existing nine-height family.

Pure arithmetic and artificial development only; no optimizer, report loader,
or research candidate is constructed here.  Real geometry remains Actions-only.
The physical coefficients are rational affine images.  A rounded nine-vector
is an evaluation diagnostic, never the exact zero-integral physical identity.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import numpy as np


def digest(value):
    raw=json.dumps(value,sort_keys=True,separators=(',',':'),
                   ensure_ascii=False,allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def _trim(p):
    p=list(map(Q,p))
    while len(p)>1 and p[-1]==0:p.pop()
    return tuple(p or [Q(0)])


def _add(p,q):
    out=[Q(0)]*max(len(p),len(q))
    for i,v in enumerate(p):out[i]+=v
    for i,v in enumerate(q):out[i]+=v
    return _trim(out)


def _scale(p,c):return _trim([Q(c)*x for x in p])


def _mul(p,q):
    out=[Q(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]+=x*y
    return _trim(out)


def _diff(p,order=1):
    for _ in range(order):p=tuple(Q(i)*p[i] for i in range(1,len(p))) or (Q(0),)
    return _trim(p)


def _primitive(p):return (Q(0),)+tuple(x/Q(i+1) for i,x in enumerate(p))


def _value(p,x):
    x=Q(x);out=Q(0)
    for v in reversed(p):out=out*x+v
    return out


def _affine(p,a,b):
    """Exact coefficients of p(a+b*x)."""
    out=(Q(0),)
    for v in reversed(p):out=_add(_mul(out,(Q(a),Q(b))),(v,))
    return out


def _combine(columns,weights):
    out=(Q(0),)
    for p,c in zip(columns,weights):out=_add(out,_scale(p,c))
    return out


def _bspline_panel(knots,midpoint):
    """All degree-five B splines as exact polynomials in normalized u."""
    current=[(Q(1),) if knots[i]<=midpoint<knots[i+1] else (Q(0),)
             for i in range(len(knots)-1)]
    for degree in range(1,6):
        next_values=[]
        for i in range(len(current)-1):
            left=knots[i+degree]-knots[i]
            right=knots[i+degree+1]-knots[i+1]
            p=(Q(0),)
            if left:p=_add(p,_mul(current[i],(-knots[i]/left,1/left)))
            if right:p=_add(p,_mul(current[i+1],(knots[i+degree+1]/right,-1/right)))
            next_values.append(p)
        current=next_values
    return current


S9=(Q(0),)*5+(Q(126),Q(-420),Q(540),Q(-315),Q(70))
CUTOFF='plateau through x=ell/3, then 1-S9((3*x/ell-1)/2), zero at ell'
EXPECTED_LAYOUT={'u':[0,81],'v':[81,154],'height':[154,163],
                 'normalized_Q_index':153,'physical_count':163}
DIRECTION_LABELS=['entry0-compensate3','entry1-compensate3',
                  'entry2-compensate3','tail6-compensate8','tail7-compensate8']


class ExactFiveHeightBasis:
    """Exact W4-weighted nine basis columns and five compact null columns.

    Work in u=(t-left)/Delta. Each stored polynomial uses its own panel
    coordinate v in [0,1], avoiding floating cancellation in large u powers.
    All integrals used in the identity are computed with rational arithmetic.
    """
    def __init__(self,source_definition):
        self.source_definition=copy.deepcopy(source_definition)
        d=self.source_definition
        if d.get('schema')!='paired-entry-weighted-center-speed-basis-v1':
            raise ValueError('the actual paired-entry height basis definition is required')
        original=d.get('original_basis',{})
        if original.get('schema')!='independent-center-speed-quintic-basis-v1':
            raise ValueError('unexpected original height family')
        if original.get('degree')!=5 or original.get('free_count')!=9:
            raise ValueError('this five-direction map requires the original nine quintic columns')
        interval=original.get('interval_exact',[])
        if len(interval)!=2:raise ValueError('exact height interval missing')
        self.left_exact,self.right_exact=map(Q,interval)
        if not self.left_exact<self.right_exact:raise ValueError('positive interval required')
        self.delta=(self.right_exact-self.left_exact)/10
        if Q(d.get('entry_length_exact','0'))!=self.delta:
            raise ValueError('the declared entry length must equal the existing knot spacing')
        if d.get('entry_weight_power')!=4 or d.get('cutoff_definition')!=CUTOFF:
            raise ValueError('unexpected W4 definition')
        if d.get('weight_definition')!='1-chi+chi*(x/ell)^4':
            raise ValueError('unexpected W4 polynomial formula')
        expected=[self.left_exact]*6+[self.left_exact+i*self.delta for i in range(1,10)]+[self.right_exact]*6
        actual=list(map(Q,original.get('clamped_knots_exact',[])))
        if actual!=expected:raise ValueError('actual exact knot vector differs')
        if original.get('retained_columns')!='3 through count+2 inclusive; discard first and last three':
            raise ValueError('actual retained-column semantics differ')
        if original.get('zero_extension_of_speed_basis_outside_interval') is not True:
            raise ValueError('zero extension must be part of the original definition')
        self.left=float(self.left_exact);self.right=float(self.right_exact)
        self.normalized_knots=[Q(0)]*6+list(map(Q,range(1,10)))+[Q(10)]*6
        self.breaks=[Q(0),Q(1,3)]+list(map(Q,range(1,11)))
        self.panel_nodes_exact=[self.left_exact+self.delta*x for x in self.breaks]
        self.panel_nodes=np.array([float(x) for x in self.panel_nodes_exact])
        self.physical_panels=[];self.physical_prefix=[[Q(0)]*9]
        chi=_add((Q(1),),_scale(_affine(S9,Q(-1,2),Q(3,2)),-1))
        ramp=_add((Q(1),),_mul(chi,(Q(-1),0,0,0,Q(1))))
        for a,b in zip(self.breaks[:-1],self.breaks[1:]):
            mid=(a+b)/2
            if mid<Q(1,3):weight=(Q(0),)*4+(Q(1),)
            elif mid<1:weight=ramp
            else:weight=(Q(1),)
            all_columns=_bspline_panel(self.normalized_knots,mid)
            global_columns=[_mul(p,weight) for p in all_columns[3:12]]
            local=[_affine(p,a,b-a) for p in global_columns]
            self.physical_panels.append(local)
            width=self.delta*(b-a)
            old=self.physical_prefix[-1]
            self.physical_prefix.append([old[j]+width*_value(_primitive(local[j]),1)
                                         for j in range(9)])
        self.integrals=tuple(self.physical_prefix[-1])
        if any(x<=0 for x in self.integrals):raise ArithmeticError('positive basis integrals required')
        if self.integrals[3]!=self.delta or self.integrals[6]!=self.delta:
            raise ArithmeticError('unweighted integral identity failed')
        if self.integrals[7]!=Q(5,6)*self.delta or self.integrals[8]!=Q(2,3)*self.delta:
            raise ArithmeticError('last-column integral identity failed')
        H=[[Q(0)]*5 for _ in range(9)]
        for j in range(3):H[j][j]=-1;H[3][j]=self.integrals[j]/self.integrals[3]
        H[6][3]=1;H[8][3]=Q(-3,2)
        H[7][4]=1;H[8][4]=Q(-5,4)
        self.H=tuple(tuple(map(Q,row)) for row in H)
        self.H_float=np.array([[float(x) for x in row] for row in self.H])
        if any(sum(self.integrals[j]*self.H[j][k] for j in range(9)) for k in range(5)):
            raise ArithmeticError('exact integral null identity failed')
        self.null_panels=[];self.null_prefix=[[Q(0)]*5]
        for i,columns in enumerate(self.physical_panels):
            local=[_combine(columns,[self.H[j][k] for j in range(9)]) for k in range(5)]
            self.null_panels.append(local)
            width=self.panel_nodes_exact[i+1]-self.panel_nodes_exact[i]
            old=self.null_prefix[-1]
            self.null_prefix.append([old[k]+width*_value(_primitive(local[k]),1) for k in range(5)])
        if any(self.null_prefix[-1]):raise ArithmeticError('null primitive did not close exactly')
        self.supports=[(self.left_exact,self.left_exact+7*self.delta)]*3+[
            (self.left_exact+4*self.delta,self.right_exact),
            (self.left_exact+5*self.delta,self.right_exact)]
        polynomial_record={'nodes':[str(x) for x in self.panel_nodes_exact],
            'physical':[[[str(q) for q in p] for p in cols] for cols in self.physical_panels],
            'null':[[[str(q) for q in p] for p in cols] for cols in self.null_panels]}
        self.identity={'schema':'exact-five-null-height-directions-in-original-nine-v1',
            'source_height_basis_definition':self.source_definition,
            'physical_integrals_exact':[str(q) for q in self.integrals],
            'height_map_exact':[[str(q) for q in row] for row in self.H],
            'directions':DIRECTION_LABELS,
            'null_support_intervals_exact':[[str(a),str(b)] for a,b in self.supports],
            'exact_piece_polynomials_sha256':digest(polynomial_record),
            'physical_height_basis_not_replaced':True,
            'no_geometric_feasibility_or_error_certificate':True}
        self.identity_sha256=digest(self.identity)

    def values(self,points,order=0,*,integral=False,null=True):
        if order not in (0,1,2):raise ValueError('only height two-jets are provided')
        if integral and order:raise ValueError('primitive has its own value call')
        t=np.asarray(points,float)
        if not np.all(np.isfinite(t)):raise ValueError('finite query points required')
        columns=5 if null else 9
        panels=self.null_panels if null else self.physical_panels
        prefix=self.null_prefix if null else self.physical_prefix
        out=np.zeros(t.shape+(columns,),float)
        for index,value in np.ndenumerate(t):
            if value<=self.left:continue
            if value>=self.right:
                if integral and not null:out[index]=[float(x) for x in self.integrals]
                continue
            panel=min(len(panels)-1,int(np.searchsorted(self.panel_nodes,value,side='right')-1))
            width=self.panel_nodes[panel+1]-self.panel_nodes[panel]
            v=(value-self.panel_nodes[panel])/width
            for j,p in enumerate(panels[panel]):
                if null:
                    a,b=self.supports[j]
                    if value<=float(a) or value>=float(b):continue
                if integral:
                    out[index+(j,)]=float(prefix[panel][j])+width*np.polynomial.polynomial.polyval(
                        v,[float(x) for x in _primitive(p)])
                else:
                    out[index+(j,)]=np.polynomial.polynomial.polyval(
                        v,[float(x) for x in _diff(p,order)])/width**order
        return out

    def evaluation_definition(self):
        return {'schema':'exact-piece-polynomial-local-coordinate-floating-evaluation-v1',
            'source_identity_sha256':self.identity_sha256,
            'arithmetic':'binary64 Horner on each normalized panel',
            'zero_extension_is_exact_function_support_not_small_value_threshold':True,
            'piece_integral_prefixes_are_exact_rationals_before_float_evaluation':True,
            'finite_floating_evaluation_not_a_continuous_error_enclosure':True}


class FiveHeightCoordinates:
    """159 independent coordinates, with exact underlying 163 physical values."""
    def __init__(self,reference_state,reference_identity,actual_layout,basis):
        if actual_layout!=EXPECTED_LAYOUT:
            raise ValueError('derive the actual SingleQ layout before constructing this map')
        self.layout=copy.deepcopy(actual_layout)
        self.basis=basis
        state=np.asarray(reference_state,float)
        if state.shape!=(163,) or not np.all(np.isfinite(state)):
            raise ValueError('complete finite original 163 state required')
        self.reference_state=state.copy();self.reference_state.flags.writeable=False
        self.reference_identity=copy.deepcopy(reference_identity)
        exact=reference_identity.get('exact_coefficients',{})
        for name,(a,b) in [('u',(0,81)),('v',(81,154)),('height',(154,163))]:
            if exact.get(name)!=[str(Q.from_float(float(v))) for v in state[a:b]]:
                raise ValueError('original canonical exact coefficients do not match the actual reference')
        if reference_identity.get('height_basis_definition')!=basis.source_definition:
            raise ValueError('canonical height basis differs from the actual basis used')
        self.reference_exact=tuple(Q.from_float(float(x)) for x in state[154:])
        self.reference_sha256=digest(reference_identity)
        self.M=np.zeros((163,159));self.M[:154,:154]=np.eye(154);self.M[154:,154:]=basis.H_float
        self.definition={'schema':'original-family159-independent-five-height-null-coordinates-v1',
            'physical_dimension':163,'independent_dimension':159,
            'reference_physical_sha256':self.reference_sha256,
            'reference_height_exact':[str(q) for q in self.reference_exact],
            'source_height_basis_definition':basis.source_definition,
            'null_basis_definition':basis.identity,
            'actual_original_layout':actual_layout,
            'coordinate_layout':{'u':[0,81],'v':[81,154],'height_null':[154,159]},
            'physical_coefficients_are_exact_affine_rationals_not_float_projection':True,
            'no_replacement_of_permanent_c0_or_b0':True}
        self.definition_sha256=digest(self.definition)

    @classmethod
    def from_problem(cls,problem,reference_state):
        actual={name:[problem.slices[name].start,problem.slices[name].stop]
                for name in ['u','v','height']}
        actual.update(normalized_Q_index=int(problem.q_index),physical_count=int(problem.nunknown))
        basis=ExactFiveHeightBasis(problem.height_basis.identity)
        return cls(reference_state,problem.identity(reference_state),actual,basis)

    @staticmethod
    def validate(q):
        q=np.asarray(q,float)
        if q.shape!=(159,) or not np.all(np.isfinite(q)):
            raise ValueError('finite complete 159 independent coordinates required')
        return q

    def initial_state(self):return np.r_[self.reference_state[:154],np.zeros(5)]

    def exact_heights(self,q):
        q=self.validate(q)
        tau=[Q.from_float(float(v)) for v in q[154:]]
        return tuple(self.reference_exact[j]+sum(self.basis.H[j][k]*tau[k] for k in range(5))
                     for j in range(9))

    def physical_exact(self,q):
        q=self.validate(q)
        return tuple(Q.from_float(float(v)) for v in q[:154])+self.exact_heights(q)

    def reference_evaluation_state(self,q):
        """Original evaluator at current u/v, immutable reference heights c*."""
        q=self.validate(q);out=self.reference_state.copy();out[:154]=q[:154]
        return out

    def physical_identity(self,q):
        q=self.validate(q);out=copy.deepcopy(self.reference_identity)
        out['exact_coefficients']={
            'u':[str(Q.from_float(float(x))) for x in q[:81]],
            'v':[str(Q.from_float(float(x))) for x in q[81:154]],
            'height':[str(x) for x in self.exact_heights(q)]}
        return out

    def rounded_physical_evaluation(self,q):
        """Diagnostic only: these rounded heights do not define the exact field."""
        q=self.validate(q);out=self.reference_state.copy();out[:154]=q[:154]
        heights=self.exact_heights(q)
        if np.any(q[154:]!=0):out[154:]=[float(x) for x in heights]
        errors=[Q.from_float(float(out[154+j]))-heights[j] for j in range(9)]
        return out,{'exact_height_coefficients':[str(x) for x in heights],
            'coefficient_rounding_errors_exact':[str(x) for x in errors],
            'rounding_cap_integral_error_exact':str(sum(self.basis.integrals[j]*errors[j] for j in range(9))),
            'rounding_does_not_replace_the_exact_null_physical_definition':True}

    def exact_box_decision(self,q,lower,upper):
        lo=np.asarray(lower,float);hi=np.asarray(upper,float)
        if lo.shape!=(163,) or hi.shape!=(163,) or not np.all(np.isfinite(lo)) or not np.all(np.isfinite(hi)):
            raise ValueError('finite original physical bounds required')
        if np.any(lo>hi):raise ValueError('invalid original physical bounds')
        p=self.physical_exact(q)
        violations=[j for j in range(163) if not Q.from_float(float(lo[j]))<=p[j]<=Q.from_float(float(hi[j]))]
        return {'exact_original_box_pass':not violations,
                'violating_physical_indices':violations,'physical_dimension':163,
                'height_comparison_uses_exact_affine_values_not_rounded_nine_vector':True}

    def physical_box_rows(self,q,lower,upper):
        """A step <= rhs in independent coordinates; all original box rows."""
        p=self.physical_exact(q);lo=np.asarray(lower,float);hi=np.asarray(upper,float)
        self.exact_box_decision(q,lo,hi)
        upper_gap=[Q.from_float(float(hi[j]))-p[j] for j in range(163)]
        lower_gap=[p[j]-Q.from_float(float(lo[j])) for j in range(163)]
        return np.vstack((self.M,-self.M)),np.array([float(x) for x in upper_gap+lower_gap]),{
            'row_semantics':'original physical upper then lower bounds; no independent height box substitute',
            'physical_indices':list(range(163))+list(range(163))}

    def normalized_physical_map(self,physical_scale):
        scale=np.asarray(physical_scale,float)
        if scale.shape!=(163,) or not np.all(np.isfinite(scale)) or np.any(scale<=0):
            raise ValueError('positive original physical scale required')
        return self.M/scale[:,None]

    def physical_norms(self,independent_step,physical_scale):
        step=self.validate(independent_step)
        v=self.normalized_physical_map(physical_scale)@step
        return {'infinity':float(np.max(abs(v))),'L1':float(np.sum(abs(v))),
                'not_norms_of_the_five_height_coordinate_numbers':True}

    def mapped_rows(self,original_physical_jacobian):
        J=np.asarray(original_physical_jacobian,float)
        if J.ndim!=2 or J.shape[1]!=163 or not np.all(np.isfinite(J)):
            raise ValueError('finite original 163-column rows required')
        return J@self.M


def artificial_basis_definition():
    left=Q(1,10);right=Q(11,10);delta=(right-left)/10
    original={'schema':'independent-center-speed-quintic-basis-v1',
        'interval_exact':[str(left),str(right)],'degree':5,'free_count':9,
        'clamped_knots_exact':[str(left)]*6+[str(left+i*delta) for i in range(1,10)]+[str(right)]*6,
        'retained_columns':'3 through count+2 inclusive; discard first and last three',
        'zero_extension_of_speed_basis_outside_interval':True,
        'cubic_zero_at_both_ends_preserves_speed_value_first_and_second_derivatives':True,
        'primitive':'I_j(t)=integral_0^t C_j(s) ds; one constant continuation after the interval',
        'no_fifth_order_endpoint_weight_added':True}
    return {'schema':'paired-entry-weighted-center-speed-basis-v1',
        'original_basis':original,'entry_length_exact':str(delta),'entry_weight_power':4,
        'cutoff_definition':CUTOFF,'weight_definition':'1-chi+chi*(x/ell)^4'}


def developer_check():
    b=ExactFiveHeightBasis(artificial_basis_definition())
    # Check the exact last-span formula and the whole-interval Wronskian.
    tail=[_affine(p,1,-1) for p in b.physical_panels[-1][6:9]]
    expected=[(0,0,0,0,0,Q(1,120)),
              (0,0,0,0,Q(5,24),Q(-137,1440)),
              (0,0,0,Q(5,3),Q(-125,72),Q(415,864))]
    d6=_add(tail[0],_scale(tail[2],Q(-3,2)))
    d7=_add(tail[1],_scale(tail[2],Q(-5,4)))
    W=_scale(_add(_mul(d6,_diff(d7)),_scale(_mul(d7,_diff(d6)),-1)),-1/b.delta)
    expected_W=(Q(0),)*6+(Q(900,1728)/b.delta,Q(-882,1728)/b.delta,Q(203,1728)/b.delta)
    ref=.001*np.sin(np.arange(163)+.2)
    ref[154:]=[.4,.3,.2,.99,0.,0.,.1,.2,.3]
    canonical={'schema':'artificial-original-physical-family',
        'height_basis_definition':b.source_definition,
        'exact_coefficients':{name:[str(Q.from_float(float(v))) for v in ref[a:z]]
            for name,a,z in [('u',0,81),('v',81,154),('height',154,163)]},
        'immutable_b0':'artificial-no-geometry'}
    m=FiveHeightCoordinates(ref,canonical,copy.deepcopy(EXPECTED_LAYOUT),b)
    q=m.initial_state();moved=q.copy();moved[154]=.2
    lo=np.r_[np.full(154,-8.),np.full(9,-1.)];hi=-lo
    nonbinary=q.copy();nonbinary[154]=.1
    exact=m.exact_heights(nonbinary)
    raw,rounding=m.rounded_physical_evaluation(nonbinary)
    null=sum(b.integrals[j]*(exact[j]-m.reference_exact[j]) for j in range(9))
    outside=np.array([0.,b.left,float(b.left_exact+7*b.delta),b.right,2.])
    zero=b.values(outside,integral=True)
    step=np.zeros(159);step[-2]=1.
    norms=m.physical_norms(step,np.ones(163))
    points=np.array([.121,.162,.248,.399,.588,.809,1.037])
    eps=1e-7
    fdp=(b.values(points+eps,integral=True)-b.values(points-eps,integral=True))/(2*eps)
    fdd=(b.values(points+eps)-b.values(points-eps))/(2*eps)
    err0=float(np.max(abs(fdp-b.values(points))))
    err1=float(np.max(abs(fdd-b.values(points,1))))
    checks={
        'exact_rational_total_integral_null':null==0 and all(x==0 for x in b.null_prefix[-1]),
        'exact_last_span_coefficients':all(_trim(a)==_trim(z) for a,z in zip(tail,expected)),
        'exact_Wronskian_coefficients':_trim(W)==_trim(expected_W),
        'zero_coordinates_preserve_original_canonical':m.physical_identity(q)==canonical,
        'zero_coordinates_preserve_original_float_bits':raw.shape==(163,) and np.array_equal(
            m.reference_evaluation_state(q).view(np.uint64),ref.view(np.uint64)),
        'coupled_compensation_box_violation_detected':m.exact_box_decision(moved,lo,hi)['violating_physical_indices']==[157],
        'nonbinary_exact_coefficients_not_replaced_by_rounding':any(Q(x)!=0 for x in rounding['coefficient_rounding_errors_exact']),
        'entry_primitive_zero_after603_analogue':bool(np.all(zero[2:,0:3]==0)),
        'all_cap_primitives_exactly_zero_at_and_after_right':bool(np.all(zero[3:]==0)),
        'physical_L1_not_coordinate_L1':norms['L1']==2.5 and norms['infinity']==1.5,
        'primitive_and_derivative_artificial_differences':err0<2e-7 and err1<2e-6,
        'all_endpoint_height_two_jets_zero':all(np.max(abs(b.values(np.array([b.left,b.right]),j)))==0 for j in range(3))}
    return {'schema':'five-null-height-arithmetic-artificial-development-v1',
        'passed':all(checks.values()),'checks':checks,
        'primitive_finite_difference_error':err0,'density_finite_difference_error':err1,
        'original_physical_dimension':163,'independent_dimension':159,
        'artificial_inputs_only':True,'research_geometry_or_optimizer_invocations':0,
        'evaluated_only_when_explicitly_called':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args();result=developer_check()
    text=json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    if args.out:args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(text)
    print(text,end='')
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
