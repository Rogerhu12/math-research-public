#!/usr/bin/env python3
"""Paired u4/v7/b6 entry representation with an unchanged frozen metric.

This independent module does not alter the published source or cap. Its CLI
uses only artificial inputs. Research initialization is a separate Actions
audit, not an optimizer.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from numpy.polynomial.polynomial import polyval,polyder

from frame_collar_bvp import HERMITE,periodic_operator,target_frame,atomic_save
from frame_collar_enriched import angular_basis
from frame_collar_residual_audit import digest
from frame_independent_height import IndependentHeightProblem
from frame_fixed_height_primitive import FixedPrimitiveProblem


def cutoff_jets(x,length):
    x=np.asarray(x,float);chi=np.zeros_like(x);first=np.zeros_like(x);second=np.zeros_like(x)
    plateau=(x>=0)&(x<=length/3);chi[plateau]=1.
    transition=(x>length/3)&(x<length);y=(3*x[transition]/length-1)/2
    for order,out in [(0,chi),(1,first),(2,second)]:
        out[transition]=polyval(y,polyder(HERMITE[0],order))*(3/(2*length))**order
    return chi,first,second


def weight_jets(x,length,power):
    x=np.asarray(x,float);chi,cp,cpp=cutoff_jets(x,length)
    z=x/length;v=z**power;vp=power*z**(power-1)/length
    vpp=power*(power-1)*z**(power-2)/length**2
    return (1+chi*(v-1),cp*(v-1)+chi*vp,
            cpp*(v-1)+2*cp*vp+chi*vpp)


def compact_power_jets(x,length,power):
    x=np.asarray(x,float);chi,cp,cpp=cutoff_jets(x,length)
    return (x**power*chi,power*x**(power-1)*chi+x**power*cp,
            power*(power-1)*x**(power-2)*chi+2*power*x**(power-1)*cp+x**power*cpp)


class PolynomialPanelIntegral:
    """Common integral of piecewise polynomial vector columns, degree <=18.

    Ten-point Gauss is exact in exact arithmetic on each declared polynomial
    piece. The floating evaluation is still not an interval certificate.
    """
    def __init__(self,evaluate,nodes_exact,columns):
        self.evaluate=evaluate;self.nodes_exact=sorted(set(map(Q,nodes_exact)))
        self.nodes=np.array([float(x) for x in self.nodes_exact]);self.columns=int(columns)
        self.gx,self.gw=leggauss(10);self.prefix=None;self.cache={}
    def integrate(self,left,right):
        left=np.asarray(left,float);right=np.asarray(right,float)
        half=(right-left)/2;mid=(right+left)/2
        points=mid[:,None]+half[:,None]*self.gx[None,:]
        values=self.evaluate(points.ravel()).reshape(len(left),10,self.columns)
        return half[:,None]*np.einsum('nqc,q->nc',values,self.gw)
    def __call__(self,points):
        t=np.asarray(points,float);clipped=np.clip(t,self.nodes[0],self.nodes[-1])
        if self.prefix is None:self.prefix=np.vstack((np.zeros((1,self.columns)),
            np.cumsum(self.integrate(self.nodes[:-1],self.nodes[1:]),axis=0)))
        missing={}
        for value in np.unique(clipped):
            key=float(value).hex()
            if key in self.cache:continue
            i=int(np.searchsorted(self.nodes,value,side='right')-1)
            if i==len(self.nodes)-1 or value==self.nodes[i]:self.cache[key]=self.prefix[i].copy()
            else:missing[key]=(i,float(value))
        if missing:
            keys=list(missing);left=np.array([self.nodes[missing[k][0]] for k in keys])
            right=np.array([missing[k][1] for k in keys]);partial=self.integrate(left,right)
            for key,val in zip(keys,partial):self.cache[key]=self.prefix[missing[key][0]]+val
        return np.stack([self.cache[float(x).hex()] for x in clipped.ravel()]).reshape(t.shape+(self.columns,))


class EntryWeightedHeightBasis:
    def __init__(self,original,length_exact):
        self.original=original;self.count=original.count
        self.left_exact=original.left_exact;self.right_exact=original.right_exact
        self.left=original.left;self.right=original.right
        self.length_exact=Q(length_exact);self.length=float(self.length_exact)
        end=self.left_exact+self.length_exact
        nodes=[self.left_exact,self.left_exact+self.length_exact/3,end]
        nodes += [Q(x) for x in original.identity['clamped_knots_exact'] if self.left_exact<Q(x)<end]
        self.correction_integral=PolynomialPanelIntegral(
            lambda t:(weight_jets(t-self.left,self.length,4)[0]-1)[:,None]*original.evaluate(t),nodes,self.count)
        self.identity={'schema':'paired-entry-weighted-center-speed-basis-v1',
            'original_basis':original.identity,'entry_length_exact':str(self.length_exact),
            'entry_weight_power':4,'cutoff_definition':'plateau through x=ell/3, then 1-S9((3*x/ell-1)/2), zero at ell',
            'weight_definition':'1-chi+chi*(x/ell)^4',
            'speed_free_columns_start_at_order_7':True,
            'integral_definition':'original exact primitive plus integral_0^t [(W4-1)*C_j]',
            'correction_polynomial_piece_nodes_exact':[str(x) for x in sorted(set(nodes))],
            'single_constant_continuation_after_entry_support':True}
        self.identity_sha256=digest(self.identity)
    def evaluate(self,t,order=0):
        t=np.asarray(t,float);w,wp,wpp=weight_jets(t-self.left,self.length,4)
        B=self.original.evaluate(t)
        if order==0:return w[...,None]*B
        Bs=self.original.evaluate(t,1)
        if order==1:return wp[...,None]*B+w[...,None]*Bs
        if order==2:return wpp[...,None]*B+2*wp[...,None]*Bs+w[...,None]*self.original.evaluate(t,2)
        raise ValueError('height basis jets are defined through order two')
    def integral(self,t):
        return self.original.integral(t)+self.correction_integral(t)


class EntrySpecification:
    def __init__(self,problem,length_exact,mean_nodes=1024):
        if problem.metric_free:raise ValueError('entry audit must hold the already selected metric fixed')
        self.problem=problem;self.original_source=problem.source;self.port=problem.port
        self.left_exact=problem.height_basis.left_exact;self.left=float(self.left_exact)
        self.length_exact=Q(length_exact);self.length=float(self.length_exact)
        patch_left=problem.seed.length_exact*(1-problem.seed.flat_fraction_exact)-problem.source.support_exact
        if self.length_exact<=0 or self.left_exact+self.length_exact>=patch_left:
            raise ValueError('entry support must end strictly before the existing tail patch')
        self.mean_nodes=int(mean_nodes)
        if self.mean_nodes<4 or self.mean_nodes%4:raise ValueError('entry mean uses a full multiple-of-four circle')
        self.C=-float(problem.source.entry_c3)
        self.c0=problem.source.source_state.copy();self.c0.setflags(write=False)
        basis=problem.source.field_basis.full
        # The old source computes its floating endpoint as cf*L, whereas the
        # exact identity is the rational product.  The two binary64 results
        # can differ by one ulp.  Evaluate the right-hand spline endpoint at
        # its own stored knot, never just outside extrapolate=False.
        self.source_knot_left=float(problem.source.field_basis.left)
        self.taylor={j:np.asarray(basis.derivative(j)(self.source_knot_left)[3:-3])/factorial(j) for j in [3,4,5]}
        self.identity={'schema':'paired-entry-u4-v7-b6-definition-v1',
            'original_source_model':problem.source.model_definition(),
            'immutable_original_c0_exact':[str(Q.from_float(float(x))) for x in self.c0],
            'entry_left_exact':str(self.left_exact),'entry_length_exact':str(self.length_exact),
            'cutoff':'chi=1 on [0,ell/3]; 1-S9((3*x/ell-1)/2) on (ell/3,ell); zero outside the outward entry',
            'C_definition':'10*seed.mu/(first_seed_segment_length)^3, unchanged by body log perturbations O(x^5)',
            'fixed_u_correction':'-chi*sum_{j=3,4} x^j (original_c0_u spline Taylor coefficient j)',
            'fixed_v_correction':'chi*(V7(theta)*x^7-sum_{j=3,4,5} x^j original_c0_v spline Taylor coefficient j)',
            'V7':'side*C^2*k_theta/(7*a0*k^3), exact ellipse arclength function',
            'b0_correction':'(B6-original_b0_6)*x^6*chi',
            'B6':'-side*C^2*exact_material_mean(k^(-2))/2',
            'original_b0_6':'-side*exact_material_mean(beta3^2+v3^2)/2 at immutable original c0',
            'current_u_v_coordinates':'original raw coefficient labels; weighted difference from immutable c0',
            'free_weight_powers':{'u':2,'v':5,'height':4},
            'all_current_fields_preserve_known_u4_v7_b6':True,
            'higher_Cauchy_jets_or_connection_existence_not_claimed':True,
            'mean_and_material_inverse_evaluation_rules_not_physical_identity':True}
        self.identity_sha256=digest(self.identity)
        self._mean=None
    def angle_data(self,theta):
        source=self.original_source
        angular,first,_=angular_basis(self.port,theta,source.angular_modes,source.phi_modes,source.core_direction)
        out={}
        for name in ['u','v','beta']:
            matrix=self.c0[source.slices[name]].reshape(source.radial_free,-1)
            out[name]={j:(angular[name]@(self.taylor[j]@matrix),
                          first[name]@(self.taylor[j]@matrix)) for j in [3,4,5]}
        phi,_=self.port.phase(theta);s,c=np.sin(phi),np.cos(phi)
        A,B,a0=self.port.major,self.port.minor,self.port.a0
        q=np.sqrt(A*A*s*s+B*B*c*c);delta=A*A-B*B;side=self.port.side
        scale=-3*side*self.C**2*delta/(7*a0*a0*A*A*B*B)
        out['V7']=scale*s*c*q**3
        out['V7_theta']=scale*a0*(q*q*(c*c-s*s)+3*delta*s*s*c*c)
        k=a0*A*B/q**3
        out['k']=k
        out['beta3']=source.entry_coefficients(theta)['beta']+out['beta'][3][0]
        out['v3']=out['v'][3][0]
        return out
    def mean_data(self):
        if self._mean is None:
            theta=np.arange(self.mean_nodes)*2*np.pi/self.mean_nodes;data=self.angle_data(theta)
            target=-self.port.side*self.C**2*np.mean(data['k']**-2)/2
            old=-self.port.side*np.mean(data['beta3']**2+data['v3']**2)/2
            self._mean={'B6':float(target),'old_b0_6':float(old),'correction':float(target-old),
                'entry_mean_angular_nodes':self.mean_nodes,'not_an_interval_integral_bound':True}
        return self._mean


class EntryRepairGrid:
    def __init__(self,original,spec):
        self.original=original;self.spec=spec;self._jac={}
        self.angle=spec.angle_data(original.theta)
        self.x=original.radial-spec.left
        self.weights={name:weight_jets(self.x,spec.length,p) for name,p in [('u',2),('v',5)]}
        self.powers={j:compact_power_jets(self.x,spec.length,j) for j in [3,4,5,7]}
    def __getattr__(self,name):return getattr(self.original,name)
    def fields(self,state):
        fields=self.original.fields(state)
        source=self.spec.original_source
        for name in ['u','v']:
            delta=(np.asarray(state[source.slices[name]])-self.spec.c0[source.slices[name]]).reshape(source.radial_free,-1)
            extra=[np.einsum('ri,ik,tk->rt',self.bases[j],delta,self.angular[name]) for j in range(3)]
            extra_theta=np.einsum('ri,ik,tk->rt',self.bases[0],delta,self.angular_first[name])
            w,wp,wpp=self.weights[name]
            for order,key in [(0,'value'),(1,'s'),(2,'ss')]:
                fixed=np.zeros_like(fields[name][key])
                for degree in ([3,4] if name=='u' else [3,4,5]):
                    fixed-=self.powers[degree][order][:,None]*self.angle[name][degree][0][None,:]
                if name=='v':fixed+=self.powers[7][order][:,None]*self.angle['V7'][None,:]
                correction=((w-1)[:,None]*extra[0] if order==0 else
                    wp[:,None]*extra[0]+(w-1)[:,None]*extra[1] if order==1 else
                    wpp[:,None]*extra[0]+2*wp[:,None]*extra[1]+(w-1)[:,None]*extra[2])
                fields[name][key]=fields[name][key]+fixed+correction
            fixed=np.zeros_like(fields[name]['theta'])
            for degree in ([3,4] if name=='u' else [3,4,5]):
                fixed-=self.powers[degree][0][:,None]*self.angle[name][degree][1][None,:]
            if name=='v':fixed+=self.powers[7][0][:,None]*self.angle['V7_theta'][None,:]
            fields[name]['theta']+=fixed+(w-1)[:,None]*extra_theta
        return fields
    def basis_jacobian(self,name,kind='value'):
        if name not in ['u','v']:return self.original.basis_jacobian(name,kind)
        key=(name,kind)
        if key in self._jac:return self._jac[key]
        w,wp,wpp=self.weights[name]
        if kind in ['value','theta']:radial=w[:,None]*self.bases[0]
        elif kind=='s':radial=wp[:,None]*self.bases[0]+w[:,None]*self.bases[1]
        elif kind=='ss':radial=wpp[:,None]*self.bases[0]+2*wp[:,None]*self.bases[1]+w[:,None]*self.bases[2]
        else:raise ValueError('unsupported entry basis derivative')
        angle=self.angular_first[name] if kind=='theta' else self.angular[name]
        answer=np.einsum('ri,tk->rtik',radial,angle).reshape(len(self.radial),len(self.theta),-1)
        self._jac[key]=answer;return answer


class EntrySource:
    def __init__(self,original,spec):self.original=original;self.spec=spec;self._entry_grids={}
    def __getattr__(self,name):return getattr(self.original,name)
    def grid_for(self,radial,theta):
        key=(np.asarray(radial,float).tobytes(),np.asarray(theta,float).tobytes())
        if key not in self._entry_grids:
            self._entry_grids[key]=EntryRepairGrid(self.original.grid_for(radial,theta),self.spec)
        return self._entry_grids[key]
    def frame(self,state,grid):
        fields=grid.fields(state);fields['_theta']=grid.theta[None,:];return target_frame(fields)
    def space_definition(self):
        out=dict(self.original.space_definition());out.update(
            schema='paired-entry-natural-cap-frame-space-v1',entry_repair=self.spec.identity,
            free_parameter_columns='raw u/v coefficients with radial W2/W5 weighted differences from original c0')
        return out
    def model_definition(self):
        return {'schema':'paired-entry-natural-cap-source-v1','unrepaired_model':self.original.model_definition(),
            'entry_repair':self.spec.identity,'space_definition':self.space_definition()}


class EntryRepairProblem(IndependentHeightProblem):
    def __init__(self,unrepaired,state,entry_length='81/500',*,entry_mean_nodes=1024,
                 uniform_panels=120,primitive_order=8):
        self.unrepaired=unrepaired
        self.entry=EntrySpecification(unrepaired,entry_length,entry_mean_nodes)
        source=EntrySource(unrepaired.source,self.entry)
        super().__init__(source,unrepaired.height_free,height_angular_nodes=unrepaired.height_angular_nodes,
            frozen_metric_definition=unrepaired.metric_model(state))
        self.height_basis=EntryWeightedHeightBasis(unrepaired.height_basis,self.entry.length_exact)
        self.height_base_definition={'schema':'paired-entry-immutable-height-base-v1',
            'unrepaired_height_base':unrepaired.height_base_definition,
            'entry_repair':self.entry.identity,
            'definition':'original immutable b0 plus (B6-old_b0_6)*x^6*chi',
            'all_angular_means_are_exact_integrals_in_the_mathematical_definition':True}
        self.original_primitive=FixedPrimitiveProblem(unrepaired,uniform_panels,primitive_order)
        tc=self.entry.left_exact;ell=self.entry.length_exact
        self.fixed_correction_integral=PolynomialPanelIntegral(
            lambda t:compact_power_jets(t-self.entry.left,self.entry.length,6)[0][:,None],
            [tc,tc+ell/3,tc+ell],1)
    def height_baseline(self,t):
        t=np.asarray(t,float);old=self.unrepaired.height_baseline(t)
        coefficient=self.entry.mean_data()['correction']
        powers=compact_power_jets(t-self.entry.left,self.entry.length,6)
        return {key:old[key]+coefficient*powers[j] for j,key in enumerate(['b0','b0_s','b0_ss'])}
    def identity(self,state):
        out=super().identity(state);out.update(schema='paired-entry-independent-height-fixed-metric-v1',
            current_tangent_free_columns='radial W2/W5 weights, same raw u/v coefficient labels',
            entry_repair=self.entry.identity,
            fixed_height_and_field_bases_are_new_not_old_state_replay=True)
        return out
    def evaluation_definition(self):
        out=super().evaluation_definition();out.update(
            reference_height_integral='query-independent original b0 primitive plus piecewise polynomial entry correction',
            original_b0_evaluator=self.original_primitive.evaluation_definition(),
            entry_mean_angular_nodes=self.entry.mean_nodes,
            source_spline_left_evaluated_at_its_stored_endpoint=self.entry.source_knot_left,
            entry_basis_primitive='10-point Gauss on full polynomial-piece union, degree at most18; exact in exact arithmetic',
            no_continuous_quadrature_error_bound=True)
        return out
    def geometry(self,state,radial,theta,quadrature_order=4,*,jacobian=False,full_two_jet_jacobian=False):
        data=super().geometry(state,radial,theta,quadrature_order,jacobian=jacobian,
            full_two_jet_jacobian=full_two_jet_jacobian)
        t=np.asarray(radial,float);coefficient=self.entry.mean_data()['correction']
        center=(self.port.initial_center_z+self.original_primitive.fixed_primitive(t)
                +coefficient*self.fixed_correction_integral(t)[:,0]
                +self.height_basis.integral(t)@np.asarray(state)[self.slices['height']])
        data['center']=center
        data['X'][...,2]=data['metric']['a'][:,None]*data['primitive'][...,2]+center[:,None]
        if jacobian and full_two_jet_jacobian:
            # The frozen generic helper assembles its final Bss term from the
            # original shared grid.bases. Replace just that term by fieldwise
            # weighted Bss; every other chain-rule term already dispatches to
            # the overridden basis_jacobian.
            grid=self.source.grid_for(t,theta);frame=self.source.frame(self.latent_state(state),grid)
            for name in ['u','v']:
                old=np.einsum('ri,tk->rtik',grid.bases[2],grid.angular[name]).reshape(len(t),len(theta),-1)
                difference=grid.basis_jacobian(name,'ss')-old
                dTss=frame['Tpart'][name][...,None]*difference[:,:,None,:]
                data['jac_Xss'][...,self.slices[name]]+=(data['metric']['a'][:,None,None,None]
                                                       *periodic_operator(dTss,-1))
        return data
    def evaluation_variant(self,state,*,heat_order=None,height_angular_nodes=None,
                           entry_mean_nodes=None,uniform_panels=None,primitive_order=None):
        underlying=self.unrepaired.evaluation_variant(state,heat_order=heat_order,
            height_angular_nodes=height_angular_nodes)
        variant=EntryRepairProblem(underlying,state,str(self.entry.length_exact),
            entry_mean_nodes=self.entry.mean_nodes if entry_mean_nodes is None else entry_mean_nodes,
            uniform_panels=self.original_primitive.uniform_panels if uniform_panels is None else uniform_panels,
            primitive_order=self.original_primitive.primitive_order if primitive_order is None else primitive_order)
        if self.identity(state)!=variant.identity(state):raise ArithmeticError('entry evaluator changed physical identity')
        return variant
    def frozen_metric_copy(self,state):
        if self.metric_free:raise ArithmeticError('entry audit unexpectedly acquired metric variables')
        return self,np.asarray(state,float).copy()


def developer_check():
    from frame_fixed_height_primitive_audit import artificial_carrier,load_selected_report
    report,raw=artificial_carrier();base,state,_=load_selected_report(report,raw)
    problem=EntryRepairProblem(base,state,'3/25',entry_mean_nodes=64,uniform_panels=16,primitive_order=4)
    tc,tf=problem.height_basis.left,problem.height_basis.right
    t=np.unique(np.r_[np.linspace(0,base.seed.length,17),tc,tc+.01,tc+.04,tc+.08,tc+.12,tf])
    theta=np.arange(24)*2*np.pi/24
    data=problem.geometry(state,t,theta,4,jacobian=True,full_two_jet_jacobian=True)
    direction=np.sin(np.arange(problem.nunknown)+.6);direction/=np.linalg.norm(direction);step=2e-7
    plus=problem.geometry(state+step*direction,t,theta,4);minus=problem.geometry(state-step*direction,t,theta,4)
    errors={}
    for key in ['X','Xs','Xt','Xss','Xst','Xtt']:
        fd=(plus[key]-minus[key])/(2*step);an=np.einsum('rtcn,n->rtc',data['jac_'+key],direction)
        errors[key]=float(np.linalg.norm(fd-an)/max(1e-30,np.linalg.norm(fd)))
    rr,J,_=problem.direct_residual_and_jacobian(state,t,theta,4)
    rp=problem.direct_residual_and_jacobian(state+step*direction,t,theta,4,jacobian=False)[0]
    rm=problem.direct_residual_and_jacobian(state-step*direction,t,theta,4,jacobian=False)[0]
    objective=float(np.linalg.norm((rp-rm)/(2*step)-J@direction)/max(1e-30,np.linalg.norm((rp-rm)/(2*step))))
    sample=np.array([tc+.017,tc+.061,tc+.108,tc+.19]);dt=1e-6
    integral_fd=(problem.height_basis.integral(sample+dt)-problem.height_basis.integral(sample-dt))/(2*dt)
    integral_error=float(np.max(abs(integral_fd-problem.height_basis.evaluate(sample))))
    original=FixedPrimitiveProblem(base,16,4).geometry(state,t,theta,4)
    after=t>=tc+problem.entry.length
    outside=max(float(np.max(abs(data[key][after]-original[key][after])))
        for key in ['Xs','Xt','Xss','Xst','Xtt'])
    shift=data['X'][after]-original['X'][after];shift[...,2]-=shift[0,0,2]
    outside_shift=float(np.max(abs(shift)))
    core=t<=tc
    core_error=max(float(np.max(abs(data[key][core]-original[key][core]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt'])
    sparse=np.array([0.,tc,tf,base.seed.length]);ss=problem.geometry(state,sparse,theta,4)
    indexes=np.searchsorted(t,sparse)
    query_error=max(float(np.max(abs(ss[key]-data[key][indexes]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt'])
    variant=problem.evaluation_variant(state,entry_mean_nodes=128,uniform_panels=32,primitive_order=6)
    same_identity=problem.identity(state)==variant.identity(state)
    metric_same=problem.metric_model(state)['mathematical_definition']==base.metric_model(state)['mathematical_definition']
    basis_end=max(float(np.max(abs(problem.height_basis.evaluate(np.array([tc,tf]),j)))) for j in range(3))
    result={'schema':'paired-entry-repair-artificial-check-v1','artificial_inputs_only':True,
        'research_geometry_evaluated':False,'optimization_performed':False,
        'complete_position_two_jet_Jacobian_relative_errors':errors,
        'direct_metric_shape_Jacobian_relative_error':objective,
        'weighted_height_primitive_derivative_error':integral_error,
        'outside_entry_nonposition_derivative_difference':outside,
        'outside_entry_position_is_one_common_vertical_translation_error':outside_shift,
        'core_position_two_jet_difference':core_error,
        'sparse_dense_query_position_two_jet_difference':query_error,
        'height_endpoint_value_first_second_error':basis_end,
        'same_physical_identity_under_evaluation_refinement':same_identity,
        'same_complete_fixed_metric_definition_as_selected_source':metric_same,
        'new_model_not_claimed_same_original_physical_field':problem.identity(state)!=base.identity(state),
        'entry_mean_coefficients_artificial':problem.entry.mean_data(),
        'known_leading_only_not_exact_connection_or_convergence_claim':True}
    result['passed']=bool(max(errors.values())<3e-5 and objective<3e-5 and integral_error<1e-7
        and outside<1e-10 and outside_shift<1e-10 and core_error<1e-10 and query_error<1e-10
        and basis_end==0 and same_identity and metric_same)
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check-only',action='store_true',required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    result=developer_check();result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    atomic_save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
