#!/usr/bin/env python3
"""R120 full waist-even diagonal target two-jet sensitivity.

This preserves the whole affine parameter interval and complete Fourier tail.
A finite floating optimization selects a dyadic target perturbation. All
reported source bounds for that chosen perturbation are interval bounds on
complete angular cells, with all primitive tails and the whole parameter box. The copied source expression is
R117 (117.23), exactly the expression used by the frozen original producer.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time
import numpy as np
from scipy.optimize import minimize_scalar,linprog
from flint import arb,acb,ctx
import fourfold_phase_two_jet_newton_source as original
from fourfold_phase_two_jet_newton_source import *
from fourfold_phase_newton_source_centered import CenteredSource,CenteredPolynomial
from fourfold_phase_correlated_curvature import Polynomial
from fourfold_phase_beta_bulk_box import DirectedFFT,arb_box,reduce_box

def point_enclosures(self,angles):
    if angles<self.grid or angles&(angles-1):raise ValueError('angle grid')
    if angles==self.grid:c=self.c
    else:
        c=zeros((angles,));modes=np.asarray([k if k<self.grid//2 else k-self.grid for k in range(self.grid)])
        c[modes%angles]=self.c
    samples=self.fft.fft(c,inverse=True)*angles
    if not np.all((samples.imag.lo<=0)&(samples.imag.hi>=0)):raise ValueError('real point sample lost reality')
    values=samples.pad(arb_box(self.error),real_only=True).real
    magnitude=arb_box((self.norm()+self.error).upper()).hi
    lo=np.maximum(values.lo,-magnitude);hi=np.minimum(values.hi,magnitude)
    if not np.all(lo<=hi):raise ValueError('inconsistent point sample')
    return Box(lo,hi)

def actual_peak(value):
    lower=np.where(value.lo>0,value.lo,np.where(value.hi<0,-value.hi,0.))
    index=int(np.argmax(lower));n=len(lower)
    return dict(physical_angle_over_pi=str(Fraction(index,2*n)),
                sample_index=index,number_of_angles=n,
                signed_source_interval=range_record(value[index]),
                pointwise_abs_lower=record(arb(float(lower[index]))),
                all_sample_abs_upper=record(box_abs_upper(value)))

class DiagnosticSource(CenteredSource):
    def source_budget(self,left,right,cap_ground):
        radial=acb(real_interval(left,right))
        FF,YY,a,EF,EY,tail=self.first_two_jets(radial)
        F=[[self.lift(FF[j][:,k],EF[j][0]) for k in range(3)]
           for j in range(3)]
        Y=[[self.lift(YY[j][:,k],EY[j]) for k in range(3)]
           for j in range(2)]
        frequency=np.asarray(self.frequency)
        zz=YY[0]*CBox(0.,Box(frequency[:,None]))
        zz[:,0]=zz[:,0]-YY[0][:,1]
        zz[:,1]=zz[:,1]+YY[0][:,0]
        ezz=(EF[0][2]+2*EF[0][1]+EF[0][0]).upper()
        Z=[self.lift(zz[:,k],ezz) for k in range(3)]
        zero=F[0][0].coerce(0)
        first=[F[1],Y[0]]
        second=[[F[2],Y[1]],[Y[1],Z]]
        aa=[]
        for value in a[:3]:
            q=value.to_acb()
            if not q.imag.contains(0):raise ValueError("radius jet is not real")
            aa.append(q.real)
        if not aa[0]>0:raise ValueError("positive physical radius unresolved")
        a2=zero.coerce(aa[0]*aa[0])
        Epoly=dot(F[1],F[1]);E1poly=2*dot(F[1],F[2])
        E,E1=Epoly.mean(),E1poly.mean()
        if not E>0:raise ValueError("positive target radial metric unresolved")
        K0=-aa[2]/(aa[0]*E)+aa[1]*E1/(2*aa[0]*E*E)
        mixed=dot(F[1],Y[0])
        # Exact R33 unit tangent identity: g_theta,theta = a^2.
        gp=[[Epoly,mixed],[mixed,a2]]
        fp=[[-nonmean(Epoly),-nonmean(mixed,True)],
            [-nonmean(mixed,True),zero]]
        # Derivative index comes first: df[k][i][j] = partial_k f_ij.
        dr_mix=dot(F[2],Y[0])+dot(F[1],Y[1])
        dt_mix=dot(Y[1],Y[0])+dot(F[1],Z)
        dfp=[
            [[-nonmean(E1poly),-nonmean(dr_mix,True)],
             [-nonmean(dr_mix,True),zero]],
            [[-nonmean(2*dot(F[1],Y[1]),True),-nonmean(dt_mix,True)],
             [-nonmean(dt_mix,True),zero]]]
        C=cross(Y[0],F[1])
        G=dot(C,C);T=dot(F[0],F[0]);S=dot(C,F[0])
        L=dot(C,F[2]);M=dot(C,Y[1]);N=dot(C,Z)
        Delta=L*N-M*M-G*G*K0
        # det(g0)-det(gamma) = a^2*f_rr + gamma_rtheta^2
        # follows from f_theta,theta=0 and f_rtheta=-gamma_rtheta.
        determinant_defect=a2*fp[0][0]+mixed*mixed
        Gmetric=Epoly*a2-mixed*mixed
        tp=[dot(F[0],first[i]) for i in range(2)]
        ff2=[[dot(F[0],second[i][j]) for j in range(2)] for i in range(2)]
        lower_conn=[[[dot(first[l],second[i][j]) for j in range(2)]
                     for i in range(2)] for l in range(2)]
        polys={"G":G,"G_metric":Gmetric,"T":T,"S":S,"L":L,"M":M,"N":N,
               "Delta":Delta,"determinant_defect":determinant_defect}
        for i in range(2):
            polys[f"t{i}"]=tp[i]
            for j in range(2):
                polys[f"g{i}{j}"]=gp[i][j]
                polys[f"f{i}{j}"]=fp[i][j]
                polys[f"FF2{i}{j}"]=ff2[i][j]
                for k in range(2):
                    polys[f"df{k}{i}{j}"]=dfp[k][i][j]
                    polys[f"conn{k}{i}{j}"]=lower_conn[k][i][j]
        if cap_ground:polys["F_z"]=F[0][2]
        boxes={key:value.angular_cells(self.curvature_angles)
               for key,value in polys.items()}
        gdet=intersect(boxes["G"],boxes["G_metric"],"cross-square = metric determinant")
        tt,ss=boxes["T"],boxes["S"]
        if not all(np.all(v.lo>0) for v in (gdet,tt,ss)):
            raise ValueError("immersion/star-shaped chart positivity unresolved")
        g=[[boxes[f"g{i}{j}"] for j in range(2)] for i in range(2)]
        f=[[boxes[f"f{i}{j}"] for j in range(2)] for i in range(2)]
        df=[[[boxes[f"df{k}{i}{j}"] for j in range(2)] for i in range(2)]
            for k in range(2)]
        t=[boxes[f"t{i}"] for i in range(2)]
        t2=[[g[i][j]+boxes[f"FF2{i}{j}"] for j in range(2)] for i in range(2)]
        gamma=inverse2(g,gdet)
        rt=sqrt_box_arb(tt)
        rho=Box(1.)/rt
        rho1=[-t[i]/(tt*rt) for i in range(2)]
        rho2=[[3*t[i]*t[j]/(square_box(tt)*rt)-t2[i][j]/(tt*rt)
               for j in range(2)] for i in range(2)]
        smetric=[[g[i][j]/tt-t[i]*t[j]/square_box(tt)
                  for j in range(2)] for i in range(2)]
        sdet=square_box(ss)/(square_box(tt)*tt)
        sinv=inverse2(smetric,sdet)
        j_u=ss/(tt*rt)
        # <U_l,U_ij> in inner products of F0,F1,F2; all large t_l*t_ij
        # terms have been cancelled algebraically before interval division.
        s_lower=[[[boxes[f"conn{l}{i}{j}"]/tt
                    -(g[l][i]*t[j]+g[l][j]*t[i]+t[l]*boxes[f"FF2{i}{j}"])/square_box(tt)
                    +2*t[l]*t[i]*t[j]/(square_box(tt)*tt)
                   for j in range(2)] for i in range(2)] for l in range(2)]
        cg=[[[sum((gamma[k][l]*boxes[f"conn{l}{i}{j}"] for l in range(2)),Box(0.))
               for j in range(2)] for i in range(2)] for k in range(2)]
        cs=[[[sum((sinv[k][l]*s_lower[l][i][j] for l in range(2)),Box(0.))
               for j in range(2)] for i in range(2)] for k in range(2)]
        bf=[[[cg[k][i][j]-cs[k][i][j] for j in range(2)] for i in range(2)]
            for k in range(2)]
        g0=[[arb_box(E),Box(0.)],[Box(0.),arb_box(aa[0]*aa[0])]]
        g0inv=[[arb_box(1/E),Box(0.)],[Box(0.),arb_box(1/(aa[0]*aa[0]))]]
        covg=[[[df[k][i][j]
                -sum((cg[m][k][i]*f[m][j]+cg[m][k][j]*f[i][m]
                      for m in range(2)),Box(0.))
                 for j in range(2)] for i in range(2)] for k in range(2)]
        dconn=[[[sum((g0inv[k][l]*(covg[i][j][l]+covg[j][i][l]-covg[l][i][j])
                      for l in range(2)),Box(0.))/2
                  for j in range(2)] for i in range(2)] for k in range(2)]
        tau=[trace2(bf[k],sinv) for k in range(2)]
        dtau=[trace2(dconn[k],sinv) for k in range(2)]
        q=bilinear(f,tau,tau)+2*bilinear(g0,tau,dtau)+bilinear(g0,dtau,dtau)
        for i in range(2):
            for j in range(2):
                for u in range(2):
                    for v in range(2):
                        bi=[bf[k][i][j] for k in range(2)]
                        bu=[bf[k][u][v] for k in range(2)]
                        di=[dconn[k][i][j] for k in range(2)]
                        du=[dconn[k][u][v] for k in range(2)]
                        q=q-sinv[i][u]*sinv[j][v]*(
                            bilinear(f,bi,bu)+2*bilinear(g0,bi,du)+bilinear(g0,di,du))
        zdiff=[]
        for i in range(2):
            z=sum((f[i][k]*tau[k]+g0[i][k]*dtau[k] for k in range(2)),Box(0.))
            z=z-sum((sinv[j][l]*(f[k][l]*bf[k][i][j]+g0[k][l]*dconn[k][i][j])
                     for j in range(2) for l in range(2) for k in range(2)),Box(0.))
            zdiff.append(z)
        hrho=[[rho2[i][j]-sum((cs[k][i][j]*rho1[k] for k in range(2)),Box(0.))
               for j in range(2)] for i in range(2)]
        # This whole expression is rational in T. Avoid a second independent
        # enclosure of rho^2 and rho*rho_i in the actual source.
        hf=[[8*t[i]*t[j]/(square_box(tt)*tt)-2*t2[i][j]/square_box(tt)
             +2*sum((cs[k][i][j]*t[k] for k in range(2)),Box(0.))/square_box(tt)
             for j in range(2)] for i in range(2)]
        trf=trace2(f,sinv)
        curvature=2*(arb_box(K0)*boxes["determinant_defect"]-boxes["Delta"]/gdet)/sdet
        pieces={
            "connection_and_trace":(q-2*trf)/tt,
            "correlated_curvature":curvature/tt,
            "density_gradient":-4*bilinear(sinv,t,zdiff)/square_box(tt),
            "density_hessian":inner2(hf,f,sinv),
            "density_trace":-trace2(hf,sinv)*trf}
        compatibility=sum(pieces.values(),Box(0.))
        source=-compatibility/2
        material=j_u*source
        # Exact source response to phi(r) dr^2 in the fixed material target.
        hr=[[-cs[0][i][j] for j in range(2)] for i in range(2)]
        tr=trace2(hr,sinv);nr=sinv[0][0]
        z=[(tr if i==0 else Box(0.))-sum((hr[i][j]*sinv[j][0] for j in range(2)),Box(0.)) for i in range(2)]
        dr2=[[Box(1.),Box(0.)],[Box(0.),Box(0.)]]
        ca=(square_box(tr)-inner2(hr,hr,sinv)-2*nr)/tt
        ca=ca-4*bilinear(sinv,t,z)/square_box(tt)
        ca=ca+inner2(hf,dr2,sinv)-trace2(hf,sinv)*nr
        aa_col=-ca/2
        col=[sinv[0][0],sinv[1][0]]
        bb_col=-(tr*nr-bilinear(hr,col,col))/(2*tt)
        ht=[[-cs[1][i][j] for j in range(2)] for i in range(2)]
        trt=trace2(ht,sinv);nt=sinv[1][1]
        zt=[(trt if i==1 else Box(0.))-sum((ht[i][j]*sinv[j][1] for j in range(2)),Box(0.)) for i in range(2)]
        dt2=[[Box(0.),Box(0.)],[Box(0.),Box(1.)]]
        ct=(square_box(trt)-inner2(ht,ht,sinv)-2*nt)/tt
        ct=ct-4*bilinear(sinv,t,zt)/square_box(tt)
        ct=ct+inner2(hf,dt2,sinv)-trace2(hf,sinv)*nt
        gg_col=-ct/2
        gpp_col=Box(1.)/(2*tt*sdet)
        self.last_G_column=gg_col;self.last_Gprimeprime_column=gpp_col;self.last_G=aa[0]*aa[0]
        self.last_source=source;self.last_E_column=aa_col;self.last_Eprime_column=bb_col
        self.last_E=E;self.last_Eprime=E1;self.last_density=j_u
        return dict(exact_radial_interval=list(map(str,(left,right))),
            exact_scalar_germ=list(map(str,self.cell)),
            source_peak=actual_peak(source),E_column_peak=actual_peak(aa_col),
            Eprime_column_peak=actual_peak(bb_col),target_E=record(E),target_Eprime=record(E1),
            actual_K0=record(K0),complete_primitive_error=record(tail))

def fraction_arb(v):
    v=Fraction(v);return arb(v.numerator)/v.denominator

def rigorous_pair_lower(q,ae,ag,cc,budget):
    if not np.all(cc.lo>0):raise ValueError('positive Gsecond response required')
    qq=q/cc;ee=ae/cc;gg=ag/cc
    mid=(qq.lo+qq.hi)/2;ip=int(np.argmax(mid));im=int(np.argmin(mid))
    eps=arb_box(arb(0,fraction_arb(budget)))
    difference=qq[ip]-qq[im]+eps*(ee[ip]-ee[im])+eps*(gg[ip]-gg[im])
    denom=Box(1.)/cc[ip]+Box(1.)/cc[im]
    lower=Box(max(0.,float(difference.lo)))/denom
    return dict(max_abs_E_and_G_changes=str(budget),Gsecond_change='arbitrary real',
                angular_indices=[ip,im],normalized_difference=range_record(difference),
                unavoidable_source_C0_lower=record(arb(float(lower.lo))))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    p.add_argument('--nodes',type=int,default=512);p.add_argument('--angles',type=int,default=16384)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=192;ctx.cap=4;original.Polynomial=CenteredPolynomial
    target=DiagnosticSource(args.object,args.half_width,args.nodes,args.angles);cuts=common_cells(target)
    i=bisect_right(cuts,Fraction(0))-1;target.set_cell(cuts[i],cuts[i+1]);start=time.monotonic()
    row=target.source_budget(Fraction(0),Fraction(0),False)
    q=target.last_source;columns=[target.last_E_column,target.last_G_column,target.last_Gprimeprime_column]
    mids=np.stack([(x.lo+x.hi)/2 for x in columns],axis=1);qm=(q.lo+q.hi)/2
    grid=np.arange(0,args.angles,max(1,args.angles//512));C=mids[grid];Q=qm[grid]
    A=np.concatenate([np.column_stack([C,-np.ones(len(grid))]),np.column_stack([-C,-np.ones(len(grid))])])
    b=np.concatenate([-Q,Q]);choices=[]
    for budget in [Fraction(1,1000),Fraction(1,100),None]:
        bounds=[(-float(budget),float(budget))]*2 if budget is not None else [(-.9*float(target.last_E.lower()),4*float(target.last_E.upper())),(-.9*float(target.last_G.lower()),4*float(target.last_G.upper()))]
        opt=linprog([0,0,0,1],A_ub=A,b_ub=b,bounds=bounds+[(None,None),(0,None)],method='highs')
        if not opt.success:raise ValueError('candidate target selection failed: '+opt.message)
        ds=list(map(lambda x:Fraction(float(x)),opt.x[:3]))
        candidate=q
        for d,c in zip(ds,columns):candidate=candidate+arb_box(fraction_arb(d))*c
        if not target.last_E+fraction_arb(ds[0])>0 or not target.last_G+fraction_arb(ds[1])>0:raise ValueError('target positivity at waist')
        choices.append(dict(E_G_budget=str(budget),exact_changes=list(map(str,ds)),
            floating_candidate_objective=float(opt.fun),verified_whole_angle_source_peak=actual_peak(candidate),
            new_target_E=record(target.last_E+fraction_arb(ds[0])),new_target_G=record(target.last_G+fraction_arb(ds[1]))))
    definition,_,_,center=load_definition(args.object)
    doc=dict(kind='actual_R117_full_waist_even_diagonal_target_jet_sensitivity',complete=True,
        whole_real_angular_circle=True,whole_radial_domain=False,waist_reflection_preserved=True,
        exact_center_parameter=str(center),exact_half_width=str(args.half_width),
        object_sha256=sha(args.object),source_sha256=sha(__file__),
        centered_source_sha256=sha(Path(__file__).with_name('fourfold_phase_newton_source_centered.py')),
        origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        original=row,target_G=record(target.last_G),column_order=['E(0)','G(0)','Gsecond(0)'],
        column_C0_upper=list(map(lambda c:record(box_abs_upper(c)),columns)),
        candidates=choices,
        pair_certificates=[rigorous_pair_lower(q,columns[0],columns[1],columns[2],d) for d in [Fraction(1,10000),Fraction(1,1000),Fraction(1,100)]],
        angles=args.angles,primitive_nodes=args.nodes,bits=192,wall_seconds=time.monotonic()-start,
        limitations=['This selects only a waist two-jet of a possible new fixed diagonal target.',
                     'No global radial target, old-operator certificate transport, full strong inverse or Newton convergence is claimed.',
                     'Floating LP selects dyadics only; complete interval reevaluation certifies their displayed bounds, not global optimality.'])
    save(args.out,doc);print(json.dumps(doc),flush=True)

if __name__=='__main__':main()
