"""Outward two-sided R748 Volterra and cap-gluing bounds on one even height and fixed g."""
import re
from decimal import Decimal
import argparse
import hashlib
import json
from pathlib import Path

from r726_closed_spinor_fourier import public
from r734_true_dyadic_tail import I, monotone_trans


ZERO,ONE=I(0),I(1)
HALF=ONE/2
A0,B0=I(".075"),I(".22")
LEFT,RIGHT=I(".105"),I(".175")
HALF_PI=I("1.570796326794896620")  # Strict rational upper bound.
NAMES=("u","u_r","u_phi","u_rr","u_rphi","u_phiphi")


def interval(value):
    if isinstance(value,(tuple,list)) and len(value)==2:
        lo,hi=value
    elif isinstance(value,(str,int,Decimal)) and not isinstance(value,bool):
        lo=hi=value
    else:
        raise ValueError("use an exact decimal or a two-endpoint decimal enclosure")
    if any(not isinstance(v,(str,int,Decimal)) or isinstance(v,bool) for v in (lo,hi)):
        raise ValueError("binary floats are not proof endpoints")
    z=I(lo,hi)
    if not z.lo.is_finite() or not z.hi.is_finite():
        raise ValueError("nonfinite proof input")
    return z


def nn(value):
    z=interval(value)
    if z.lo<0:
        raise ValueError("negative magnitude enclosure")
    return I(z.hi)


def high(x):
    return I(x.hi)


def absmax(x):
    return I(x.norm())


def root(x):
    if x.hi==0:
        return ZERO
    return high(monotone_trans(I(x.hi),"sqrt"))


def minimum(*values):
    return I(min(q.hi for q in values))


def maximum(*values):
    return I(max(q.hi for q in values))


def cap_bounds(cap,r,sin_theta,cos_theta,s_floor):
    """Propagate complete homogeneous height trace errors to W,H and the six real scaled jets."""
    z,p,q,t,v,w=(nn(cap[k]) for k in NAMES)
    c=I(cos_theta.lo)
    # At a cap E=1, E'=0, A>=s. The rigid cap has A*>=cos(theta).
    s=I(s_floor.lo)
    if s.lo<=0 or c.lo<=0:
        raise ValueError("cap chart lacks positive margin")
    amin=s
    P=sin_theta+p
    Q=r*sin_theta+q
    da=p*(2*sin_theta+p)/(amin+c)
    ds=(p*(2*sin_theta+p)+(q/r)*(2*sin_theta+q/r))/(s+c)
    ar=P*t/amin
    beta_r=Q*t/(amin**2*r*s)
    abeta=Q*t/(amin*r*s)
    da_phi=(p*(sin_theta+v)+sin_theta*v)/amin+sin_theta**2*da/(amin*c)
    six=[z,root(da**2+p**2),q/r,root(ar**2+abeta**2+t**2),
         root(da_phi**2+(da/c)**2+v**2)/r,w/r**2]
    dc=(p*Q+sin_theta*q)/amin+r*sin_theta**2*da/(amin*c)
    dd=r*(ds+da)/amin
    H=root(dc**2+dd**2)
    sr=(P*t+(Q/r**2)*(v+q/r))/s
    val=(ds+2*da/c)/amin**2
    W=val+(r/amin**2)*(sr/s+ar/amin)+P*Q*beta_r/amin**2
    if "H_upper" in cap:
        H=minimum(H,nn(cap["H_upper"]))
    if "W_upper" in cap:
        W=minimum(W,nn(cap["W_upper"]))
    return high(W),high(H),[str(k.hi) for k in six],all(k.hi==0 for k in (z,p,q,t,v,w))


def clipped(x):
    return I(max(Decimal(0),min(Decimal(1),x.lo)),max(Decimal(0),min(Decimal(1),x.hi)))


def smooth(x):
    return clipped(x**3*(10+x*(-15+6*x)))


def bump_max(lo,hi):
    if lo.lo<=HALF.hi and hi.hi>=HALF.lo:
        return ONE/4
    z=I(hi.hi if hi.hi<HALF.lo else lo.lo)
    return high(z*(1-z))


def weight(left,right):
    width=RIGHT-LEFT
    vl=clipped((I(left.lo)-LEFT)/width)
    vh=clipped((I(right.hi)-LEFT)/width)
    lo=I((1-smooth(vh)).lo)
    hi=I((1-smooth(vl)).hi)
    derivative=30*bump_max(vl,vh)**2/width
    return lo,hi,high(derivative),bump_max(lo,hi)


def cell_data(edge,left,right):
    h=high(right-left)
    E=I(interval(edge["E_lower"]).lo)
    sig=I(interval(edge["normal_s_lower"]).lo)
    A=nn(edge["A_upper"])
    if min(E.lo,sig.lo,A.lo,h.lo)<=0 or sig.lo>1:
        raise ValueError("invalid continuous chart or radial cell")
    masses=[]
    left_m=[];right_m=[]
    if "D_absolute_upper" in edge:
        rate=nn(edge["D_absolute_upper"])/(I(left.lo)*monotone_trans(E,"sqrt")*sig**3)
        masses.append(rate*h)
        left_m.append(rate*h**2/2)
        right_m.append(rate*h**2/2)
    if "Q_L1_upper" in edge:
        masses.append(nn(edge["Q_L1_upper"]))
    if not masses:
        raise ValueError("whole-cell scalar sup or integrated nonnegative defect required")
    mass=minimum(*masses)
    left_m.append(h*mass);right_m.append(h*mass)
    for name,out in (("Q_left_first_moment_upper",left_m),("Q_right_first_moment_upper",right_m)):
        if name in edge:
            out.append(nn(edge[name]))
    return dict(h=h,E=E,s=sig,A=A,mass=mass,l=minimum(*left_m),r=minimum(*right_m))


def advance(data,initial,order,side):
    W,H=initial
    outer=[]
    for i in order:
        z=data[i]
        H=high(H+z["A"]*(z["h"]*W+z[side]))
        W=high(W+z["mass"])
        outer.append((W,H))
    return outer


def two_cap_bound(edges,cells,boundary,proof_sha256,eta_target=None,
                  representation="exact_radial_development"):
    """Conditioned on one even true height, E(a,b)=1,E'(a,b)=0 and all supplied continuum enclosures.

    No interpolation of finite samples. Q=|D|/(r sqrt(E) s^3). Optional cell
    first moments use distances to the left and right true endpoints respectively.
    """
    public()
    if not isinstance(proof_sha256,str) or not re.fullmatch("[a-f0-9]{64}",proof_sha256):
        raise ValueError("identify the continuous evidence to which this calculation applies")
    r=list(map(interval,edges))
    if len(r)!=len(cells)+1 or not cells or (r[0].lo,r[0].hi)!=(A0.lo,A0.hi) or (r[-1].lo,r[-1].hi)!=(B0.lo,B0.hi):
        raise ValueError("a complete original .075 to .22 material cover is required")
    if any(y.lo<=x.hi for x,y in zip(r,r[1:])):
        raise ValueError("radial endpoint enclosures are not strictly ordered")
    z=[cell_data(c,r[i],r[i+1]) for i,c in enumerate(cells)]
    if representation not in ("exact_radial_development","validated_C2_representative"):
        raise ValueError("unknown representation under certificate")
    numerical=representation=="validated_C2_representative"
    ct=monotone_trans(ONE-I(".27")**2,"sqrt")
    wi,hi,si,ci=cap_bounds(boundary["inner_height_errors"],A0,I(".27"),ct,z[0]["s"])
    wo,ho,so,co=cap_bounds(boundary["outer_height_errors"],B0,ZERO,ONE,z[-1]["s"])
    if numerical:
        for side,seams in (("inner",si),("outer",so)):
            extra=boundary[side+"_implementation_six_upper"]
            if len(extra)!=6:
                raise ValueError("all six normalized implementation traces are needed")
            seams[:]=[str((I(x)+nn(y)).hi) for x,y in zip(seams,extra,strict=True)]
        ci=all(Decimal(x)==0 for x in si)
        co=all(Decimal(x)==0 for x in so)
    inner=advance(z,(wi,hi),range(len(z)),"r")
    outer=advance(z,(wo,ho),reversed(range(len(z))),"l")[::-1]
    wa=wi+outer[0][0]
    ha=hi+outer[0][1]
    # Reflection gives R=1 at both real axes. Horizontal centre and normalized
    # material axis lengths must come from this height, including the true tails.
    cx=interval(boundary["C_x"])
    plus=interval(boundary["L_plus"]);minus=interval(boundary["L_minus"])
    if min(plus.lo,minus.lo)<=0:
        raise ValueError("invalid projected radial axis integrals")
    stride=B0-A0*ct
    jp=absmax(cx+plus-stride)
    jm=absmax(cx+stride-minus)
    anchor=maximum(jp,jm)
    turn=minimum(I(2),HALF_PI*wa)
    # For the inner endpoint angular path integrate |R-1|<=distance*wa.
    anchor_span=anchor+HALF_PI*ha+A0*minimum(HALF_PI**2*wa/2,2*HALF_PI)
    cum=ZERO; worst=ZERO; report=[]
    for i,c in enumerate(z):
        cum=high(cum+c["h"]*c["A"])
        lo,hh,wp,bmax=weight(r[i],r[i+1])
        vspan=anchor_span+turn*cum
        if "join_position_upper" in cells[i]:
            vspan=minimum(vspan,nn(cells[i]["join_position_upper"]))
        turn_c=turn
        if "rotation_chord_upper" in cells[i]:
            turn_c=minimum(turn,nn(cells[i]["rotation_chord_upper"]))
        hi_c,ho_c=inner[i][1],outer[i][1]
        blend=maximum((1-lo)*ho_c+lo*hi_c,(1-hh)*ho_c+hh*hi_c)
        er=high(wp*vspan/monotone_trans(c["E"],"sqrt"))
        ep=high(blend/I(r[i].lo))
        if numerical:
            er=high(er+nn(cells[i]["relative_implementation_r_upper"]))
            ep=high(ep+nn(cells[i]["relative_implementation_phi_upper"]))
        e=root(er**2+ep**2)
        loss=minimum(ONE,bmax*turn_c**2)
        lower=(Decimal(1) if loss.hi==0 else
               monotone_trans(I(max(Decimal(0),(1-loss).lo)),"sqrt").lo)
        margin=I(max(Decimal(0),(I(lower)-e).lo))
        eta=maximum(2*e+e**2,1-margin**2)
        rr=loss+2*er+er**2
        mixed=loss/2+er+ep+er*ep
        angular=loss+2*ep+ep**2
        worst=maximum(worst,eta)
        report.append(dict(cell=i,outer_W=str(outer[i][0].hi),inner_W=str(inner[i][0].hi),
               outer_H=str(ho_c.hi),inner_H=str(hi_c.hi),Q_mass=str(c["mass"].hi),
               relative_Gram_rr_mixed_angular=[str(v.hi) for v in (rr,mixed,angular)],
               relative_Gram_operator=str(eta.hi)))
    target=None if eta_target is None else interval(eta_target)
    if target is not None and target.lo<0:
        raise ValueError("a nonnegative target is required")
    return dict(conditional_on_continuous_proof=proof_sha256,all_cell_eta_upper=str(worst.hi),cells=report,
                cap_six_scaled_order=["position","r","phi/r","rr","rphi/r","phiphi/r^2"],
                cap_six_bounds=[si,so],conditional_exact_seams=ci and co,
                axis_anchor_upper=[str(jp.hi),str(jm.hi)],rotation_chord_upper=str(turn.hi),
                representation=representation,
                conditional_eta_gate=None if target is None else worst.hi<=target.lo,
                conditional_eta_and_exact_rims=None if target is None else (worst.hi<=target.lo and ci and co),
                establishes_input_proofs_or_global_reach=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input",required=True,type=Path)
    parser.add_argument("--output",type=Path)
    parser.add_argument("--proof",type=Path,help="verify the identified external evidence bytes")
    args=parser.parse_args()
    public()
    data=args.input.read_bytes()
    payload=json.loads(data)
    if args.proof is not None and hashlib.sha256(args.proof.read_bytes()).hexdigest()!=payload["proof_sha256"]:
        raise ValueError("external continuous-bound evidence has a different identity")
    report=two_cap_bound(**payload)
    report["input_sha256"]=hashlib.sha256(data).hexdigest()
    report["provided_evidence_bytes_verified"]=args.proof is not None
    if args.output is None:
        print("R749_TWO_CAP_BOUND",json.dumps(report,sort_keys=True,separators=(",",":")),flush=True)
    else:
        args.output.write_text(json.dumps(report,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
        summary={k:v for k,v in report.items() if k!="cells"}
        summary["cell_count"]=len(report["cells"])
        summary["report_sha256"]=hashlib.sha256(args.output.read_bytes()).hexdigest()
        print("R749_TWO_CAP_BOUND",json.dumps(summary,sort_keys=True,separators=(",",":")),flush=True)


if __name__=="__main__":
    main()
