#!/usr/bin/env python3
"""Exact S9 six-segment developable cap with algebraic physical identity.

The six cap normals and widths are defined over Q(sqrt(3)). Floating numbers
only evaluate this fixed model. No research candidate is evaluated by the CLI;
--check-only uses a different artificial radius and amplitude list.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from bent_flat_tail_port import Jet22,exact,digest


def s9_derivative(x,order=0):
    x=np.asarray(x,float);z=np.clip(x,0.,1.)
    if order==0:
        y=np.minimum(z,1-z)
        lower=y**5*(126+y*(-420+y*(540+y*(-315+70*y))))
        return np.where(z<=.5,lower,1-lower)
    if not 1<=order<=4:raise ValueError('S9 derivatives zero through four are supported')
    n=order-1;out=np.zeros_like(z)
    for k in range(n+1):
        coefficient=(630*math.comb(n,k)*math.factorial(4)//math.factorial(4-k)*
                     math.factorial(4)//math.factorial(4-(n-k))*(-1)**(n-k))
        out+=coefficient*z**(4-k)*(1-z)**(4-(n-k))
    return np.where((x>0)&(x<1),out,0.)


def algebraic(rational=0,sqrt3=0):
    return {'rational_part':str(Q(rational)),'sqrt3_coefficient':str(Q(sqrt3))}


NORMALS_EXACT=[
    [algebraic(1),algebraic()],
    [algebraic(Q(1,2)),algebraic(0,Q(1,2))],
    [algebraic(Q(-1,2)),algebraic(0,Q(1,2))],
    [algebraic(-1),algebraic()],
    [algebraic(Q(-1,2)),algebraic(0,Q(-1,2))],
    [algebraic(Q(1,2)),algebraic(0,Q(-1,2))]]


class PolygonalFlatTail:
    """C5 cap on 0<=r<=R, with s derivatives along core-to-cap dr/ds=-1.

    Each point of the closed source disk belongs to at most one open cap.
    The scalar formulas may therefore add their zero-background increments.
    Evaluation outside the source disk is rejected, rather than assuming that
    overlapping cylindrical formulas there still give an isometry.
    """
    def __init__(self,outer_radius='137/500',held_radius='11/50',
                 amplitudes=('3/16','1/8','1/8','3/16','1/8','1/8'),side=1):
        self.outer_exact=exact(outer_radius);self.cut_exact=exact(held_radius)
        self.amplitudes_exact=tuple(exact(x) for x in amplitudes)
        if not self.outer_exact>self.cut_exact>0 or 3*self.outer_exact**2<=4*self.cut_exact**2:
            raise ValueError('the held disk must lie strictly inside the exact hexagon inradius')
        if len(self.amplitudes_exact)!=6 or not all(0<x<Q(3,4) for x in self.amplitudes_exact) or side not in [-1,1]:
            raise ValueError('six amplitudes in (0,3/4) and side +/-1 required')
        if any(self.amplitudes_exact[j]!=self.amplitudes_exact[(j+3)%6] or
               self.amplitudes_exact[j]!=self.amplitudes_exact[(-j)%6] for j in range(6)):
            raise ValueError('this port requires twofold and theta-reflection amplitude symmetry')
        self.outer=float(self.outer_exact);self.cut=float(self.cut_exact)
        self.side=int(side);self.amplitudes=np.asarray([float(x) for x in self.amplitudes_exact])
        root3=np.sqrt(3.)
        self.normals=np.array([[1,0],[.5,root3/2],[-.5,root3/2],[-1,0],[-.5,-root3/2],[.5,-root3/2]])
        self.offset=self.outer*root3/2;self.bend_width=self.outer*(1-root3/2)
        self.identity={'schema':'S9-algebraic-six-cap-flat-tail-v1','source_outer_radius':str(self.outer_exact),
            'held_closed_disk_radius':str(self.cut_exact),'side':self.side,'cap_count':6,
            'cap_order':'normal angle j*pi/3, j=0..5; vertices pi/6+j*pi/3',
            'normals_Q_sqrt3':NORMALS_EXACT,
            'chord_offset_Q_sqrt3':algebraic(0,self.outer_exact/2),
            'bend_width_Q_sqrt3':algebraic(self.outer_exact,-self.outer_exact/2),
            'amplitudes_exact':[str(x) for x in self.amplitudes_exact],
            'smoothstep_polynomial_coefficients':['0']*5+['126','-420','540','-315','70'],
            'smoothstep_extension':'0 on x<=0; 1 on x>=1',
            'cap_coordinate_definition':'u_j=normal_j dot q-chord_offset',
            'alpha_j_definition':'alpha_j(u)=A_j*S9(u/bend_width)',
            'Y_j_definition':'integral_0^u cos(alpha_j(v)) dv; Y_j(u)=u for u<=0',
            'H_j_definition':'integral_0^u sin(alpha_j(v)) dv; H_j(u)=0 for u<=0',
            'position_definition':'(q,side*h)+sum_j((Y_j(u_j)-u_j)*normal_j,-side*H_j(u_j))',
            'radial_derivative_dr_dt':-1,
            'height_definition':'one h from the common anchored R28 center, never fitted separately by cap',
            'physical_domain':'closed source disk |q|<=source_outer_radius; at most one cap is active',
            'regularity':'alpha_j C4, P C5 across every chord and vertex',
            'symmetry':'twofold rotation and theta reflection; generally not sixfold',
            'algebraic_width_not_replaced_by_a_binary64_number':True,
            'quadrature_is_evaluation_not_physical_definition':True}
        self.identity_sha256=digest(self.identity)

    def _domain(self,radius):
        r=np.asarray(radius,float)
        slack=64*np.finfo(float).eps*max(1.,self.outer)
        if np.any(r<0) or np.any(r>self.outer+slack):
            raise ValueError('the accurate disjoint-cap formula is restricted to its closed source disk')

    def alpha_jets(self,cap,excess,maximum=4):
        x=np.asarray(excess,float)/self.bend_width
        if not 0<=maximum<=4:raise ValueError('angle derivatives through order four only')
        return [self.amplitudes[cap]*s9_derivative(x,k)/self.bend_width**k for k in range(maximum+1)]

    def scalar_jets(self,radius,theta):
        radius,theta=np.broadcast_arrays(np.asarray(radius,float),np.asarray(theta,float));self._domain(radius)
        radial=Jet22.variable(radius,0,-1.);angle=Jet22.variable(theta,1)
        cosine,sine=angle.cos(),angle.sin()
        u=Jet22.constant(np.zeros_like(radius));v=Jet22.constant(np.zeros_like(radius))
        beta_delta=Jet22.constant(np.zeros_like(radius))
        for j,n in enumerate(self.normals):
            a=cosine*n[0]+sine*n[1];b=-sine*n[0]+cosine*n[1]
            excess=radial*a-self.offset
            if not np.any(excess.c[0,0]>0):continue
            alpha=excess.compose(self.alpha_jets(j,excess.c[0,0],4));C,S=alpha.cos(),alpha.sin()
            denominator=1-(1-C)*b*b
            u=u+((1-C)*a*b/denominator).atan()
            v=v-self.side*b*S/(1-b*b*S*S).sqrt()
            beta_delta=beta_delta+self.side*(a*S/C).atan()
        beta=-self.side*np.pi+beta_delta
        return {'u':u.result(),'v':v.result(),'beta':beta.result(),
            'tail_physical_identity_sha256':self.identity_sha256,
            'radial_derivative_convention':'dr/ds=-1 along core-to-cap',
            'floating_jets_are_not_interval_bounds':True,
            'disjointness_is_a_property_of_the_exact_source_disk':True}

    def cap_displacements(self,cap,excess,quadrature_order=32):
        excess=np.asarray(excess,float);span=np.clip(excess,0,self.bend_width)
        nodes,weights=leggauss(int(quadrature_order));local=span[...,None]*(nodes+1)/2
        angle=self.amplitudes[cap]*s9_derivative(local/self.bend_width)
        # cos(alpha)-1=-2 sin(alpha/2)^2 avoids subtracting nearly equal integrals.
        D=np.sum(-2*np.sin(angle/2)**2*weights,axis=-1)*span/2
        H=np.sum(np.sin(angle)*weights,axis=-1)*span/2
        extra=np.maximum(excess-self.bend_width,0)
        D+=extra*(-2*np.sin(self.amplitudes[cap]/2)**2)
        H+=extra*np.sin(self.amplitudes[cap])
        return D,H

    def position_jets(self,radius,theta,height=0.,quadrature_order=32):
        r,theta=np.broadcast_arrays(np.asarray(radius,float),np.asarray(theta,float));self._domain(r)
        zero=np.zeros_like(r);c,s=np.cos(theta),np.sin(theta)
        er=np.stack((c,s,zero),axis=-1);et=np.stack((-s,c,zero),axis=-1)
        X=r[...,None]*er;X[...,2]=self.side*np.broadcast_to(height,r.shape)
        Xs=-er.copy();Xt=r[...,None]*et;Xss=np.zeros_like(X)
        Xst=-et.copy();Xtt=-r[...,None]*er
        normal=np.stack((zero,zero,np.ones_like(r)),axis=-1)
        curvature=np.zeros_like(r);total_drop=np.zeros_like(r)
        for j,n2 in enumerate(self.normals):
            a=c*n2[0]+s*n2[1];b=-s*n2[0]+c*n2[1];excess=r*a-self.offset
            alpha,ap=self.alpha_jets(j,excess,1);C,S=np.cos(alpha),np.sin(alpha)
            n=np.array([n2[0],n2[1],0.]);D,H=self.cap_displacements(j,excess,quadrature_order)
            X+=D[...,None]*n;X[...,2]-=self.side*H;total_drop+=H
            Xs+=(a*(1-C))[...,None]*n;Xs[...,2]+=self.side*a*S
            Xt+=(r*b*(C-1))[...,None]*n;Xt[...,2]-=self.side*r*b*S
            Xss+=(-a*a*S*ap)[...,None]*n;Xss[...,2]-=self.side*a*a*C*ap
            Xst+=(b*(1-C)+r*a*b*S*ap)[...,None]*n
            Xst[...,2]+=self.side*(b*S+r*a*b*C*ap)
            Xtt+=(r*a*(1-C)-r*r*b*b*S*ap)[...,None]*n
            Xtt[...,2]+=self.side*(r*a*S-r*r*b*b*C*ap)
            normal+=(self.side*S)[...,None]*n;normal[...,2]+=C-1
            curvature+=abs(ap)
        return {'X':X,'Xs':Xs,'Xtheta':Xt,'Xss':Xss,'Xst':Xst,'Xtt':Xtt,
            'normal':normal,'principal_curvature_absolute':curvature,'height_drop':total_drop,
            'integral_quadrature_order':int(quadrature_order),
            'tail_physical_identity_sha256':self.identity_sha256,
            'quadrature_and_floating_jets_are_not_interval_bounds':True}

    def analytic_budget(self):
        maximum=max(self.amplitudes_exact)
        selected=(self.outer_exact==Q(137,500) and maximum<=Q(3,16))
        return {'maximum_amplitude_exact':str(maximum),
            'curvature_upper_formula':'315*Amax/(128*R*(1-sqrt(3)/2))',
            'all_cap_normal_chord_lower_formula':'128*R*(1-sqrt(3)/2)*cos(Amax)^2/(315*Amax)',
            'height_drop_upper_formula':'Amax*R*(1-sqrt(3)/2)/2',
            'uniform_exact_normal_chord_lower_when_selected':'3/40' if selected else None,
            'uniform_exact_lower_is_strict':bool(selected),
            'global_cap_embedding_follows_from_horizontal_strong_monotonicity':True,
            'whole_surface_reach_not_implied':True,
            'proof_source':'results/R44-S9-six-cap-exact-embedding-and-normal-chord.md'}


def developer_check():
    from frame_collar_bvp import target_frame
    rows=[];step=1e-6
    theta=np.array([.11,.43,.69,1.19,1.71,2.25,3.42,4.88,5.81])
    radius=np.array([.88,.85,.87,.86,.88,.89,.87,.84,.82])
    artificial_amplitudes=['1/7','1/9','1/9','1/7','1/9','1/9']
    for side in [1,-1]:
        tail=PolygonalFlatTail('9/10','3/5',artificial_amplitudes,side)
        f=tail.scalar_jets(radius,theta);f['_theta']=theta
        frame=target_frame(f);position=tail.position_jets(radius,theta,.31)
        fp=tail.scalar_jets(radius-step,theta);fm=tail.scalar_jets(radius+step,theta)
        gp=tail.scalar_jets(radius,theta+step);gm=tail.scalar_jets(radius,theta-step)
        scalar_errors={}
        for name in ['u','v','beta']:
            for key,fd in [('s',(fp[name]['value']-fm[name]['value'])/(2*step)),
                           ('ss',(fp[name]['s']-fm[name]['s'])/(2*step)),
                           ('theta',(gp[name]['value']-gm[name]['value'])/(2*step)),
                           ('st',(gp[name]['s']-gm[name]['s'])/(2*step)),
                           ('tt',(gp[name]['theta']-gm[name]['theta'])/(2*step)),
                           ('ss_theta',(gp[name]['ss']-gm[name]['ss'])/(2*step))]:
                scalar_errors[name+'_'+key]=float(np.max(abs(f[name][key]-fd)))/max(1.,float(np.max(abs(f[name][key]))))
        xp=tail.position_jets(radius-step,theta,.31);xm=tail.position_jets(radius+step,theta,.31)
        tp=tail.position_jets(radius,theta+step,.31);tm=tail.position_jets(radius,theta-step,.31)
        position_errors={}
        for key,fd in [('Xs',(xp['X']-xm['X'])/(2*step)),('Xss',(xp['Xs']-xm['Xs'])/(2*step)),
                       ('Xtheta',(tp['X']-tm['X'])/(2*step)),('Xst',(tp['Xs']-tm['Xs'])/(2*step)),
                       ('Xtt',(tp['Xtheta']-tm['Xtheta'])/(2*step))]:
            position_errors[key]=float(np.max(abs(position[key]-fd)))/max(1.,float(np.max(abs(position[key]))))
        frame_error=max(float(np.max(abs(frame['T']-position['Xtheta']/radius[:,None]))),
                        float(np.max(abs(frame['V']-position['Xs']))))
        residual=frame['Vtheta']+frame['T']-radius[:,None]*frame['Ts']
        E=np.sum(position['Xs']**2,axis=-1);F=np.sum(position['Xs']*position['Xtheta'],axis=-1)
        G=np.sum(position['Xtheta']**2,axis=-1)/radius**2
        period=tail.scalar_jets(radius,theta+np.pi);reflection=tail.scalar_jets(radius,-theta)
        symmetry=max(float(np.max(abs(period[name]['value']-f[name]['value']))) for name in ['u','v','beta'])
        symmetry=max(symmetry,max(float(np.max(abs(reflection[name]['value']-(-1 if name!='beta' else 1)*f[name]['value']))) for name in ['u','v','beta']))
        vertices=np.pi/6+np.arange(6)*np.pi/3;at_vertex=tail.scalar_jets(tail.outer,vertices)
        vertex_error=max(float(np.max(abs(at_vertex[name][key]-(-side*np.pi if name=='beta' and key=='value' else 0))))
            for name in ['u','v','beta'] for key in ['value','s','ss','theta','st','ss_theta'])
        pos24=tail.position_jets(radius,theta,.31,24);pos48=tail.position_jets(radius,theta,.31,48)
        outside_rejected=False
        try:tail.scalar_jets(tail.outer+.01,np.array([0.]))
        except ValueError:outside_rejected=True
        rows.append({'side':side,'scalar_jet_relative_errors':scalar_errors,
            'position_jet_relative_errors':position_errors,'target_frame_error':frame_error,
            'integrability_error':float(np.max(abs(residual))),
            'metric_error':float(max(np.max(abs(E-1)),np.max(abs(F)),np.max(abs(G-1)))),
            'symmetry_error':symmetry,'vertex_jets_error':vertex_error,
            'quadrature_doubling_position_difference':float(np.max(abs(pos24['X']-pos48['X']))),
            'outside_source_disk_rejected':outside_rejected,'physical_identity_sha256':tail.identity_sha256})
    p=[Q(0)]*5+[Q(x) for x in [126,-420,540,-315,70]];endpoints=[]
    for order in range(5):
        endpoints.append([str(p[0]),str(sum(p,Q(0)))])
        p=[(i+1)*p[i+1] for i in range(len(p)-1)]
    passed=(endpoints[0]==['0','1'] and all(row==['0','0'] for row in endpoints[1:]) and
        all(max(row['scalar_jet_relative_errors'].values())<3e-6 and max(row['position_jet_relative_errors'].values())<3e-6 and
            max(row['target_frame_error'],row['integrability_error'],row['metric_error'],row['symmetry_error'],
                row['vertex_jets_error'],row['quadrature_doubling_position_difference'])<1e-9 and row['outside_source_disk_rejected'] for row in rows))
    return {'schema':'S9-six-cap-port-development-v1','checks':rows,'exact_S9_endpoint_jets':endpoints,
        'passed':bool(passed),'artificial_inputs_only':True,'research_geometry_evaluated':False,'optimization_performed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args();out=developer_check()
    out['source_files_sha256']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in [Path(__file__).name,'bent_flat_tail_port.py','cosine_connector_radial_seed.py',
                     'frame_collar_bvp.py','ellipse_frame_port.py']}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'passed':out['passed']}),flush=True)
    if not out['passed']:raise SystemExit(1)


if __name__=='__main__':main()
