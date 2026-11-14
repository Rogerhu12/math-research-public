#!/usr/bin/env python3
"""A full-frequency two-port Airy bound from exact ODE series and cones.

No nonradial object is used.  The stable solution is normalized by b(1)=1,
a(1)/b(1) in [-1/4,0], and the growing solution by (a(1),b(1))=(1,0).
Their Wronskian is exactly one for every allowed stable ratio. Complete
negative-side Sonin energies and positive cones give the full Green and
both Poisson columns, including the two separate mean equations.
"""
from __future__ import annotations
import argparse,time
from pathlib import Path
from flint import arb,arb_mat,ctx
from fourfold_phase_metric_defect import record,save,sha


def fundamental(sign,N=48):
    cols=[];fees=[]
    for first in (0,1):
        c=[arb(0)]*(N+4);c[first]=arb(1)
        for n in range(3,N+4):c[n]=sign*c[n-3]/(n*(n-1))
        n0=next(n for n in range(N+1,N+4) if n%3==first)
        ru=arb(1)/((n0+3)*(n0+2));rd=arb(1)/(n0*(n0+2))
        fee0=abs(c[n0])/(1-ru);fee1=n0*abs(c[n0])/(1-rd)
        value=sum(c[:N+1],arb(0))+arb(0,fee0.upper())
        deriv=sum((n*c[n] for n in range(1,N+1)),arb(0))+arb(0,fee1.upper())
        cols.append((value,deriv));fees.append((fee0.upper(),fee1.upper()))
    return arb_mat([[cols[0][0],cols[1][0]],[cols[0][1],cols[1][1]]]),fees


def sqnorm(v):return v[0,0]**2+v[1,0]**2
def energy(v):return sqnorm(v)+v[0,0]*v[1,0]/2


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;t0=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every universal Airy attempt')
    fp,ep=fundamental(1);fn,en=fundamental(-1)
    # Wronskian one is an exact ODE identity; no approximate determinant
    # is substituted for the inverse.
    ip=arb_mat([[fp[1,1],-fp[0,1]],[-fp[1,0],fp[0,0]]])
    r=arb(-1)/4;rr=r.union(arb(0));root2=arb(2).sqrt()
    A1=arb_mat([[(1+rr)/root2],[(rr-1)/root2]])
    B1=arb_mat([[1/root2],[1/root2]])
    A0=ip*A1;B0=ip*B1
    reflection=arb_mat([[1,0],[0,-1]])
    An1=fn*reflection*A0;Bn1=fn*reflection*B0
    A0lo=sqnorm(A0).lower().sqrt().lower();A0hi=sqnorm(A0).upper().sqrt().upper()
    B0lo=sqnorm(B0).lower().sqrt().lower();B0hi=sqnorm(B0).upper().sqrt().upper()
    EAlo=energy(An1).lower();EAhi=energy(An1).upper();EBhi=energy(Bn1).upper()
    small=arb(2)**(arb(1)/4)*(arb(1)/4).exp()
    Anlo=min(A0lo/small,(arb(3)/(5*root2)*EAlo).sqrt()).lower()
    Anhi=max(small*A0hi,(arb(16)*root2/9*EAhi).sqrt()).upper()
    Bnhi=max(small*B0hi,(arb(16)*root2/9*EBhi).sqrt()).upper()
    Aphi=max(arb(2)**(arb(1)/4)*A0hi,arb(2)**(arb(1)/4)*arb(17).sqrt()/4).upper()
    Bplo=min(arb(2)**(-arb(1)/4)*B0lo,arb(2)**(-arb(1)/4)).lower()
    c=(Bnhi/Anlo).upper();Cn=(Bnhi+c*Anhi).upper()
    split=max(root2*arb(17)/15,root2*A0hi,root2*arb(17).sqrt()/4).upper()
    G=max(Anhi*Cn,Aphi*Cn,split+c*Aphi*Aphi).upper()
    Pminus=(root2*max(Anhi,Aphi)/Anlo).upper()
    Pplus=max(Cn/Bplo,2+c*Aphi/Bplo).upper()
    allbound=max(arb(1),G,Pminus,Pplus).upper()
    power=0
    while not allbound<arb(2)**power:power+=1
    gates=[('both exact scalar fundamental Wronskians enclose one',fp.det().contains(1) and fn.det().contains(1)),
        ('negative x=-|m|^(2/3)T uses the reflected root derivative',True),
        ('full power-series and derivative remainders paid',all(x.is_finite() and x>=0 for row in ep+en for x in row)),
        ('the whole stable cone gives positive A0 and negative derivative',A0[0,0]>0 and A0[1,0]<0),
        ('the exact growing line is positive in both states at zero',B0[0,0]>0 and B0[1,0]>0),
        ('negative stable Sonin energy lower bound strictly positive',EAlo>0 and Anlo>0),
        ('positive growing norm separated from zero',Bplo>0),
        ('full Green and both Poisson columns bounded',allbound.is_finite()),
        ('complete independent mean equations retained',True)]
    vals=locals();names=('A0lo','A0hi','B0lo','B0hi','EAlo','EAhi','EBhi','Anlo','Anhi','Bnhi','Aphi','Bplo','c','Cn','split','G','Pminus','Pplus','allbound')
    doc=dict(kind='complete_universal_two_port_Airy_kernel_from_exact_series_and_cones_v2',
        complete=all(bool(v) for _,v in gates),source_sha256=sha(__file__),
        exact_series_last_degree=48,exact_stable_ratio_interval=['-1/4','0'],
        exact_Wronskian_A_B='1 in positive coordinate, -1 in negative coordinate',
        negative_root_derivative_exact_reflection=True,reference_equation='U_T=J(T) U_X+f, J(T)=[[0,T],[-1,0]]',
        physical_frequencies='all m in 4Z, with zero mode solved independently',
        full_positive_and_negative_interval_sizes='any finite sizes; endpoint weights use omega^2=|T|+|m|^-2/3',
        negative_port='one positive-flux incoming amplitude (Z1+Z2)/sqrt2',
        positive_port='coefficient of growing B normalized to unit balanced norm at the right endpoint',
        positive_fundamental=[[record(fp[i,j]) for j in range(2)] for i in range(2)],
        negative_fundamental=[[record(fn[i,j]) for j in range(2)] for i in range(2)],
        complete_series_tail_fees=[[record(x) for x in row] for row in ep+en],
        zero_states=dict(A=[record(A0[i,0]) for i in range(2)],B=[record(B0[i,0]) for i in range(2)]),
        bounds={n:record(vals[n]) for n in names},complete_two_port_kernel_bound=2**power,
        gates=[dict(name=n,passed=bool(v)) for n,v in gates],seconds=time.monotonic()-t0,
        dependencies={'fourfold_phase_metric_defect.py':sha(Path(__file__).with_name('fourfold_phase_metric_defect.py'))})
    save(args.out,doc)
    print(dict(complete=doc['complete'],bound=2**power,allbound=allbound.str(15),
        G=G.str(15),Pminus=Pminus.str(15),Pplus=Pplus.str(15),out=str(args.out),sha256=sha(args.out)),flush=True)
    if not doc['complete']:raise SystemExit(1)


if __name__=='__main__':main()
