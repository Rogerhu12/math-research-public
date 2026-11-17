#!/usr/bin/env python3
"""Rational planar-core budgets across eta; no nonlinear surface claims."""
import json,math
from pathlib import Path
from fractions import Fraction as F
import audit_large_radius_core as I

def coefficients(eta):
    C=15*(1+2*eta);cm={k:I.trig_moment(k)for k in [1,3,4,5,7,8,9]};sm={k:I.trig_moment(k,True)for k in [1,3,5,7,9]}
    mass=I.A+I.B/2
    integral=I.sub(I.point(C*mass),I.scale(I.add(I.scale(cm[4],1+eta),I.scale(cm[8],eta)),15))
    beta=I.neg(I.div(integral,I.sub(I.scale(I.pi_bounds(),F(1,4)),I.point(mass))))
    i0=I.add(cm[1],sm[1]);p4=I.add(I.add(cm[3],cm[5]),I.sub(sm[5],sm[3]));p8=I.add(I.add(cm[7],cm[9]),I.sub(sm[9],sm[7]))
    i1=I.sub(I.scale(i0,C),I.scale(I.add(I.scale(p4,1+eta),I.scale(p8,eta)),F(15,2)))
    correction=I.add(beta,I.sub(i1,I.mul(beta,i0)))
    center_per_q=I.sub(I.point(C+1+F(26,21)*eta),correction)
    return C,beta,center_per_q

def row(eta,q,gain8=F('10.954140806620659')):
    C,beta,cq=coefficients(eta);R=1+q*C;center=I.scale(cq,q)
    peak=1 if eta<=F(1,3)else eta+(1+eta)**2/(8*eta)
    lower=I.add(I.point(1-15*q*peak),I.scale(beta,q))
    phase=I.A-F(1,2000)/R;shift=I.scale(I.mul(center,I.sin_bounds(phase)),2)
    return dict(eta=str(eta),q=str(q),R=str(R),beta=I.show(beta),center=I.show(center),rho_lower=I.show(lower),
        held_shift=I.show(shift),held_ratio_D2p65=I.show(I.scale(shift,F(20,53))),
        primary_support_amplitude=str((1+eta)*q),mode8_support_amplitude=str(F(5,21)*eta*q),
        mode8_linear_normal_displacement_scale=float(F(5,21)*eta*q*gain8),
        warning='The last column uses a sampled current-profile linear gain and is not a nonlinear estimate. Full rho is for zero complementary controls only.')

if __name__=='__main__':
    rows=[row(F(e),F(q))for e,q in [('0','.058'),('.05','.053'),('.1','.049'),('.15','.045'),('.25','.04'),('.5','.03'),('1','.02')]]
    out=dict(scope=__doc__,rows=rows)
    Path('large-radius-eta-screen.json').write_text(json.dumps(out,indent=2)+'\n')
    for r in rows:print(json.dumps({k:(float(F(v[0]))if isinstance(v,list)else v)for k,v in r.items()if k not in ['warning','beta']}),flush=True)
