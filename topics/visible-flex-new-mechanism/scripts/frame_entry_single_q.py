#!/usr/bin/env python3
"""One exact elliptic Q angular column, preserving the fixed height reference.

Only artificial --check-only is exposed. The new coefficient is inserted in
the v block; a zero new coefficient exactly contains the old mathematical
field. No actual candidate or solver is selected by this module.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import numpy as np

from frame_collar_bvp import atomic_save,periodic_operator,target_frame
from frame_collar_residual_audit import digest
from frame_collar_enriched import rational_knots
from frame_independent_height import IndependentHeightProblem
from frame_entry_paired_repair import EntryRepairProblem,weight_jets
from frame_entry_bounded_height import BoundedEntryHeightProblem
from frame_fixed_height_primitive_audit import artificial_carrier,load_selected_report
from frame_entry_short_bounded_audit import implementation_hashes as short_hashes


def implementation_hashes():
    out=short_hashes()
    out[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return out


class EllipticNormalizedQ:
    """Q=k_theta/k^3 normalized by its exact algebraic/elliptic supremum."""
    def __init__(self,port):
        if port.A_exact<port.B_exact:
            raise ValueError('major>=minor is required for this declared angular direction')
        if port.A_exact==port.B_exact:
            raise ValueError('a circular core has Q=0 and does not acquire a zero parameter column')
        self.port=port;A=port.major;B=port.minor;Delta=A*A-B*B
        u=4*Delta-2*B*B;root=np.sqrt(u*u+20*Delta*B*B)
        self.sstar=(u+root)/(10*Delta) if u>=0 else 2*B*B/(root-u)
        self.denominator=np.sqrt(self.sstar*(1-self.sstar))*(B*B+Delta*self.sstar)**1.5
        if not 0<self.sstar<1 or self.denominator<=0:
            raise ArithmeticError('positive exact-sup evaluation failed')
        self.raw_Q_sup=3*Delta*self.denominator/(port.a0*A*A*B*B)
        self.identity={'schema':'exact-elliptic-normalized-Q-angular-direction-v1',
            'core_physical_identity':port.identity,'k':'material turning speed, not spatial curvature',
            'Q':'k_theta/k^3',
            'Delta':'A^2-B^2',
            'sstar':'unique root in (0,1) of B^2+(4*Delta-2*B^2)*s-5*Delta*s^2=0',
            'normalizing_D':'sqrt(sstar*(1-sstar))*(B^2+Delta*sstar)^(3/2)',
            'normalized_Q':'-sin(phi)*cos(phi)*(B^2+Delta*sin(phi)^2)^(3/2)/normalizing_D',
            'raw_Q_sup':'3*Delta*normalizing_D/(a0*A^2*B^2)',
            'material_phase':'the unchanged exact ellipse arclength inverse',
            'pi_periodic_and_reflection_odd':True,
            'normalization_is_an_exact_definition_not_a_sampled_maximum':True}
    def evaluate(self,theta):
        phi,error=self.port.phase(theta);s=np.sin(phi);c=np.cos(phi)
        A=self.port.major;B=self.port.minor;Delta=A*A-B*B
        q2=B*B+Delta*s*s
        value=-s*c*q2**1.5/self.denominator
        first=-self.port.a0*((c*c-s*s)*q2+3*Delta*s*s*c*c)/self.denominator
        return value,first,error


class SingleQGrid:
    def __init__(self,problem,original):
        self.problem=problem;self.original=original;self._jac={}
        t=original.radial
        w,wp,wpp=weight_jets(t-problem.entry.left,problem.entry.length,5)
        B,Bs,Bss=(original.bases[j][:,0] for j in range(3))
        self.radial_Q=[w*B,wp*B+w*Bs,wpp*B+2*wp*Bs+w*Bss]
        self.angular_Q,self.angular_Q_theta,self.arc_inverse_error=problem.Q.evaluate(original.theta)
    def __getattr__(self,name):return getattr(self.original,name)
    def column(self,kind='value'):
        if kind=='theta':return self.radial_Q[0][:,None]*self.angular_Q_theta[None,:]
        index={'value':0,'s':1,'ss':2}[kind]
        return self.radial_Q[index][:,None]*self.angular_Q[None,:]
    def fields(self,state):
        old=self.problem.to_old(state)
        f=self.original.fields(self.problem.base.latent_state(old))
        coefficient=float(np.asarray(state)[self.problem.q_index])
        for key in ['value','s','ss','theta']:
            f['v'][key]=f['v'][key]+coefficient*self.column(key)
        return f
    def basis_jacobian(self,name,kind='value'):
        key=(name,kind)
        if key not in self._jac:
            original=self.original.basis_jacobian(name,kind)
            self._jac[key]=(np.concatenate((original,self.column(kind)[...,None]),axis=-1)
                            if name=='v' else original)
        return self._jac[key]


class SingleQSource:
    def __init__(self,problem):
        self.problem=problem;self._grids={}
        # This facade takes the new independent-height layout directly. It
        # must not accidentally advertise the old auxiliary-beta layout.
        self.nunknown=problem.nunknown;self.slices=dict(problem.slices)
    def __getattr__(self,name):return getattr(self.problem.base.source,name)
    def grid_for(self,radial,theta):
        key=(np.asarray(radial,float).tobytes(),np.asarray(theta,float).tobytes())
        if key not in self._grids:
            self._grids[key]=SingleQGrid(self.problem,self.problem.base.source.grid_for(radial,theta))
        return self._grids[key]
    def frame(self,state,grid):
        f=grid.fields(state);f['_theta']=grid.theta[None,:]
        return target_frame(f)
    def space_definition(self):
        return {'schema':'paired-entry-one-Q-column-tangent-space-v1',
            'old_exact_space':self.problem.base.source.space_definition(),
            'angular_direction':self.problem.Q.identity,
            'radial_direction':'W5(x)*first retained original clamped quintic B3(t)',
            'radial_basis_identity':{'degree':5,'clamped_knots_exact':self.problem.radial_knots,
                'selected_full_spline_index':3,'zero_extension_outside_active_interval':True},
            'radial_basis_for_field_is_the_old_shared_field_basis_not_height_weight_W4':True,
            'old_radial_field_knots':self.problem.radial_knots,
            'new_column_location':'last column of independent v block',
            'all_old_columns_are_retained_with_their_original_coefficients':True,
            'zero_new_coefficient_contains_old_exact_field':True,
            'only_a_required_v8_direction_is_added_not_a_full_Cauchy_solution':True}
    def model_definition(self):
        return {'schema':'one-Q-independent-height-source-v1',
            'old_source_model':self.problem.base.source.model_definition(),
            'space_definition':self.space_definition(),
            'parameter_input':'complete new independent-height state; height entries do not affect T',
            'no_variable_auxiliary_beta':True}


def complete_tangent_parameter_jets(grid,fields,frame,name,order=2):
    """Analytic parameter columns for T, T_s, T_theta and optionally T_ss."""
    B=grid.basis_jacobian(name);Bs=grid.basis_jacobian(name,'s');Bt=grid.basis_jacobian(name,'theta')
    part=frame['Tpart'][name]
    result={'T':part[...,None]*B[:,:,None,:],
        'Ts':frame['Ts_value_part'][name][...,None]*B[:,:,None,:]+part[...,None]*Bs[:,:,None,:]}
    v=fields['v']['value'];psi=fields['_theta']+fields['u']['value']
    H=np.stack((-np.sin(psi),np.cos(psi),np.zeros_like(v)),axis=-1)
    N=np.stack((np.cos(psi),np.sin(psi),np.zeros_like(v)),axis=-1)
    ez=np.zeros_like(H);ez[...,2]=1.
    c=1/np.sqrt(1+v*v);cv=-v*c**3;cvv=(2*v*v-1)*c**5
    dv=c**3;dvv=-3*v*c**5
    Tuu=-c[...,None]*H;Tuv=-cv[...,None]*N
    Tvv=cvv[...,None]*H+dvv[...,None]*ez
    pt=1+fields['u']['theta'];vt=fields['v']['theta']
    value_theta=(pt[...,None]*Tuu+vt[...,None]*Tuv) if name=='u' else (pt[...,None]*Tuv+vt[...,None]*Tvv)
    result['Ttheta']=value_theta[...,None]*B[:,:,None,:]+part[...,None]*Bt[:,:,None,:]
    if order<2:return result
    us,vs,uss,vss=(fields[a][b] for a,b in [('u','s'),('v','s'),('u','ss'),('v','ss')])
    A=-c*us*us+cvv*vs*vs+cv*vss
    Bn=-2*cv*us*vs-c*uss
    if name=='u':
        value=Bn[...,None]*H-A[...,None]*N
        first=(-2*c*us)[...,None]*H+(-2*cv*vs)[...,None]*N
    else:
        cvvv=3*v*(3-2*v*v)*c**7;dvvv=3*(4*v*v-1)*c**7
        value=((-cv*us*us+cvvv*vs*vs+cvv*vss)[...,None]*H+
               (-2*cvv*us*vs-cv*uss)[...,None]*N+
               (dvvv*vs*vs+dvv*vss)[...,None]*ez)
        first=(2*cvv*vs)[...,None]*H+(-2*cv*us)[...,None]*N+(2*dvv*vs)[...,None]*ez
    Bss=grid.basis_jacobian(name,'ss')
    result['Tss']=value[...,None]*B[:,:,None,:]+first[...,None]*Bs[:,:,None,:]+part[...,None]*Bss[:,:,None,:]
    return result


class SingleQProblem:
    def __init__(self,base):
        if base.metric_free:raise ValueError('complete metric must already be frozen')
        self.base=base;self.Q=EllipticNormalizedQ(base.port);self.entry=base.entry
        # Use the original field knots, not the independent height count.
        self.radial_knots=[str(x) for x in rational_knots(base.seed,base.source.radial_free)]
        self.slices={};nu=base.slices['u'].stop-base.slices['u'].start
        nv=base.slices['v'].stop-base.slices['v'].start
        self.slices['u']=slice(0,nu);self.slices['v']=slice(nu,nu+nv+1)
        self.q_index=nu+nv;self.slices['height']=slice(self.q_index+1,self.q_index+1+base.height_free)
        self.tangent_count=nu+nv+1
        self.nunknown=base.nunknown+1;self.slices['metric']=slice(self.nunknown,self.nunknown)
        self.metric_free=0;self.source=SingleQSource(self)
    def __getattr__(self,name):return getattr(self.base,name)
    def lift_state(self,old):
        old=np.asarray(old,float)
        if old.shape!=(self.base.nunknown,):raise ValueError('old full parameter layout required')
        return np.insert(old,self.q_index,0.)
    def to_old(self,state):
        state=np.asarray(state,float)
        if state.shape!=(self.nunknown,) or not np.all(np.isfinite(state)):
            raise ValueError('finite complete single-Q state required')
        return np.delete(state,self.q_index)
    def initial_state(self):return self.lift_state(self.base.initial_state())
    def latent_state(self,state):
        self.to_old(state)
        return np.asarray(state,float)
    def metric(self,state,radial,jacobian=False):return self.base.metric(self.to_old(state),radial,jacobian)
    def metric_model(self,state):return self.base.metric_model(self.to_old(state))
    def height_jets(self,state,radial):return self.base.height_jets(self.to_old(state),radial)
    def identity(self,state):
        state=np.asarray(state,float);old=self.base.identity(self.to_old(state))
        old=copy.deepcopy(old)
        old.update(schema='fixed-metric-one-Q-column-independent-height-v1',
            source_T_scalar_family=self.source.space_definition(),
            current_tangent_free_columns='all old radial W2/W5 columns plus one W5*B3*normalized_Q v column',
            same_current_T_space_as_polynomial_entry=False,
            parent_T_space_is_exactly_contained_at_zero_new_coefficient=True,
            new_parameter_layout={name:[sl.start,sl.stop] for name,sl in self.slices.items()},
            normalized_Q_parameter_index=self.q_index,
            exact_coefficients={name:[str(Q.from_float(float(x))) for x in state[self.slices[name]]]
                                for name in ['u','v','height']},
            immutable_height_reference_is_the_old_model_not_recomputed_using_new_Q=True,
            no_claim_total_v8_paid_at_arbitrary_current_coefficients=True,
            no_optimization_or_error_improvement_claim=True)
        return old
    def evaluation_definition(self):
        result=copy.deepcopy(self.base.evaluation_definition())
        result.update(one_Q_sup_evaluation={'sstar':float(self.Q.sstar),
            'algebraic_denominator':float(self.Q.denominator),'raw_Q_sup':float(self.Q.raw_Q_sup)},
            common_center_evaluation='unchanged base geometry with fixed 4-angle grid, center only',
            old_query_independent_primitive_used_without_row_refitting=True)
        return result
    def geometry(self,state,radial,theta,quadrature_order=4,*,jacobian=False,full_two_jet_jacobian=False):
        state=np.asarray(state,float);old=self.to_old(state);t=np.asarray(radial,float);theta=np.asarray(theta,float)
        # Reuse the authoritative old common primitive; its center is independent
        # of the query angle grid and of every current tangent coefficient.
        reference=self.base.geometry(old,t,np.arange(4)*np.pi/2,quadrature_order)
        if theta.ndim!=1 or len(theta)<4 or len(theta)%4:
            raise ValueError('positive multiple-of-four complete angular grid required')
        expected=theta[0]+np.arange(len(theta))*2*np.pi/len(theta)
        if not np.allclose(theta,expected,rtol=0,atol=128*np.finfo(float).eps*max(1.,np.max(abs(theta)))):
            raise ValueError('uniform full angular grid required')
        grid=self.source.grid_for(t,theta);f=grid.fields(state);f['_theta']=theta[None,:];frame=target_frame(f)
        metric=reference['metric'];a,ap,app=(metric[k] for k in ['a','a_s','a_ss'])
        P,Ps,Pss=(periodic_operator(frame[k],-1) for k in ['T','Ts','Tss'])
        height=reference['height'];center=reference['center']
        X=a[:,None,None]*P;X[...,2]+=center[:,None]
        Xs=ap[:,None,None]*P+a[:,None,None]*Ps;Xs[...,2]+=height['b'][:,None]
        Xss=app[:,None,None]*P+2*ap[:,None,None]*Ps+a[:,None,None]*Pss
        Xss[...,2]+=height['b_s'][:,None]
        Xt=a[:,None,None]*frame['T'];Xst=ap[:,None,None]*frame['T']+a[:,None,None]*frame['Ts']
        Xtt=a[:,None,None]*frame['Ttheta']
        out={'X':X,'Xs':Xs,'Xt':Xt,'Xss':Xss,'Xst':Xst,'Xtt':Xtt,
            'T':frame['T'],'Ts':frame['Ts'],'Tss':frame['Tss'],'Ttheta':frame['Ttheta'],
            'metric':metric,'height':height,'center':center,'primitive':P,'radial':t,'theta':theta,
            'auxiliary_R_not_used_as_metric_residual':True}
        if not jacobian:return out
        names=['X','Xs','Xt','T']+(['Xss','Xst','Xtt'] if full_two_jet_jacobian else [])
        blocks={name:[] for name in names}
        for name in ['u','v']:
            jets=complete_tangent_parameter_jets(grid,f,frame,name,2 if full_two_jet_jacobian else 1)
            dP,dPs=(periodic_operator(jets[k],-1) for k in ['T','Ts'])
            blocks['X'].append(a[:,None,None,None]*dP)
            blocks['Xs'].append(ap[:,None,None,None]*dP+a[:,None,None,None]*dPs)
            blocks['Xt'].append(a[:,None,None,None]*jets['T']);blocks['T'].append(jets['T'])
            if full_two_jet_jacobian:
                dPss=periodic_operator(jets['Tss'],-1)
                blocks['Xss'].append(app[:,None,None,None]*dP+2*ap[:,None,None,None]*dPs+a[:,None,None,None]*dPss)
                blocks['Xst'].append(ap[:,None,None,None]*jets['T']+a[:,None,None,None]*jets['Ts'])
                blocks['Xtt'].append(a[:,None,None,None]*jets['Ttheta'])
        def vertical(values):
            answer=np.zeros(X.shape+(self.height_free,));answer[:,:,2,:]=values[:,None,:];return answer
        zero=np.zeros(X.shape+(self.height_free,))
        blocks['X'].append(vertical(self.height_basis.integral(t)))
        blocks['Xs'].append(vertical(self.height_basis.evaluate(t)))
        blocks['Xt'].append(zero);blocks['T'].append(zero)
        if full_two_jet_jacobian:
            blocks['Xss'].append(vertical(self.height_basis.evaluate(t,1)))
            blocks['Xst'].append(zero);blocks['Xtt'].append(zero)
        for name in names:out['jac_'+name]=np.concatenate(blocks[name],axis=-1)
        out['parameter_Jacobian_contains_complete_position_two_jets']=bool(full_two_jet_jacobian)
        return out
    def direct_residual_and_jacobian(self,state,radial,theta,quadrature_order=4,*,jacobian=True):
        return IndependentHeightProblem.direct_residual_and_jacobian(self,state,radial,theta,
            quadrature_order,jacobian=jacobian)
    def evaluation_variant(self,state,**kwargs):
        variant=SingleQProblem(self.base.evaluation_variant(self.to_old(state),**kwargs))
        if self.identity(state)!=variant.identity(state):raise ArithmeticError('evaluation changed physical field')
        return variant
    def frozen_metric_copy(self,state):return self,np.asarray(state,float).copy()


def developer_check():
    original,raw=artificial_carrier();old,state,_=load_selected_report(original,raw)
    paired=EntryRepairProblem(old,state,'3/25',entry_mean_nodes=64,uniform_panels=8,primitive_order=3)
    bounded=BoundedEntryHeightProblem(paired,state,uniform_panels=8,primitive_order=3)
    results=[]
    # Artificial field and height counts intentionally differ; the new
    # direction must use field knots and must not borrow the height count.
    for base in [paired,bounded]:
        p=SingleQProblem(base);x=p.lift_state(state)
        t=np.unique(np.r_[np.linspace(0,base.seed.length,13),base.entry.left,base.entry.left+.04,
                          base.entry.left+base.entry.length,base.source.active_end])
        theta=np.arange(24)*2*np.pi/24
        zero=p.geometry(x,t,theta,3);before=base.geometry(state,t,theta,3)
        warm={k:float(np.max(abs(zero[k]-before[k]))) for k in ['X','Xs','Xt','Xss','Xst','Xtt']}
        x[p.q_index]=.003
        data=p.geometry(x,t,theta,3,jacobian=True,full_two_jet_jacobian=True)
        direction=np.sin(np.arange(p.nunknown)+.3);direction[p.q_index]=1.;direction/=np.linalg.norm(direction)
        step=2e-7;plus=p.geometry(x+step*direction,t,theta,3);minus=p.geometry(x-step*direction,t,theta,3)
        errors={}
        for key in ['X','Xs','Xt','Xss','Xst','Xtt']:
            fd=(plus[key]-minus[key])/(2*step);an=np.einsum('rtcn,n->rtc',data['jac_'+key],direction)
            errors[key]=float(np.linalg.norm(fd-an)/max(1e-30,np.linalg.norm(fd)))
        r,J,_=p.direct_residual_and_jacobian(x,t,theta,3)
        rp=p.direct_residual_and_jacobian(x+step*direction,t,theta,3,jacobian=False)[0]
        rm=p.direct_residual_and_jacobian(x-step*direction,t,theta,3,jacobian=False)[0]
        direct=float(np.linalg.norm((rp-rm)/(2*step)-J@direction)/max(1e-30,np.linalg.norm((rp-rm)/(2*step))))
        test=np.array([.17,.43,1.21,2.37]);dh=1e-6
        q,qt,_=p.Q.evaluate(test)
        fd=(p.Q.evaluate(test+dh)[0]-p.Q.evaluate(test-dh)[0])/(2*dh)
        angular=float(np.max(abs(fd-qt)))
        ports=np.array([0.,base.entry.left,base.source.active_end,base.seed.length])
        col=p.source.grid_for(ports,theta)
        port_error=max(float(np.max(abs(col.column(k)))) for k in ['value','s','ss','theta'])
        results.append({'old_height_schema':base.height_base_definition['schema'],
            'new_dimension':p.nunknown,'zero_column_warm_six_jet_errors':warm,
            'complete_position_two_jet_Jacobian_relative_errors':errors,
            'direct_metric_shape_Jacobian_relative_error':direct,
            'Q_theta_centered_difference_error':angular,
            'Q_column_full_port_two_jet_error':port_error,
            'height_reference_identity_unchanged':p.height_base_definition==base.height_base_definition,
            'complete_metric_identity_unchanged':p.metric_model(x)==base.metric_model(state)})
    passed=bool(len(results)==2 and all(max(x['zero_column_warm_six_jet_errors'].values())<1e-10
        and max(x['complete_position_two_jet_Jacobian_relative_errors'].values())<1e-5
        and x['direct_metric_shape_Jacobian_relative_error']<1e-5
        and x['Q_theta_centered_difference_error']<1e-6 and x['Q_column_full_port_two_jet_error']<1e-10
        and x['height_reference_identity_unchanged'] and x['complete_metric_identity_unchanged'] for x in results))
    return {'schema':'single-Q-entry-column-artificial-check-v1','artificial_inputs_only':True,
        'research_candidate_evaluated_or_optimized':False,'cases':results,'passed':passed}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check-only',action='store_true',required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();out=developer_check();out['source_files_sha256']=implementation_hashes()
    atomic_save(args.out,out);print(json.dumps({'out':str(args.out),'passed':out['passed']}),flush=True)
    if not out['passed']:raise SystemExit(1)


if __name__=='__main__':main()
