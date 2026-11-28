"""The genuine R745 two-valley profile in the actual R738 material coordinates."""
import math
import numpy as np
from scipy.special import expit
from r738_negative_tail_and_macro_source import A0,B0,FIRST,RATIO,SIGNS,stepp

H=.56
RAMP=.018
TOP=.006
EPS=.0002
BEG=(.081,.124,.167)
MID=(.102,.145,.188)
CUT={s:(A0 if s==-1 else B0)-s*RATIO[s]*np.ldexp(1/512,-FIRST[s]) for s in SIGNS}
CENTER=MID[1]


def smooth_ramp(x):
    if x<=-EPS:return 0.
    if x>=EPS:return x
    t=(x+EPS)/(2*EPS)
    return 280*EPS*t**5*(1/20+t*(-1/10+t*(1/14-t/56)))


def bump(r):
    for s in BEG:
        if s-EPS<r<s+2*RAMP+TOP+EPS:
            x=r-s
            if x>RAMP+TOP/2:x=2*RAMP+TOP-x
            if x>=RAMP+EPS:return H
            return H/RAMP*(smooth_ramp(x)-smooth_ramp(x-RAMP))
    return 0.


def slope_ramp(x):
    if x<=-EPS:return 0.
    if x>=EPS:return 1.
    t=(x+EPS)/(2*EPS)
    return 140*t**4*(.25+t*(-.6+t*(.5-t/7)))


def bump_prime(r):
    for s in BEG:
        if s-EPS<r<s+2*RAMP+TOP+EPS:
            x=r-s;sign=1.
            if x>RAMP+TOP/2:x=2*RAMP+TOP-x;sign=-1.
            return sign*H/RAMP*(slope_ramp(x)-slope_ramp(x-RAMP))
    return 0.


def germ(r,sign):
    rim=A0 if sign==-1 else B0
    xi=abs(r-rim);edge=RATIO[sign]*np.ldexp(1/512,-FIRST[sign])
    t=max(0.,min(1.,(xi-edge)/EPS));y=edge+EPS*(t-t**4*(2.5-3*t+t*t))
    w=.5*(y/RATIO[sign])**4
    return w/np.hypot(1.,w)


def slopes(r,eta):
    if r<CUT[-1]-8*np.spacing(r) or r>CUT[1]+8*np.spacing(r):raise ValueError('Wrong physical bulk radius.')
    if r<MID[0]:
        v=germ(r,-1);dv=np.zeros(2)
    elif r>MID[2]:
        v=germ(r,1);dv=np.zeros(2)
    else:
        i=int(r>MID[1]);v=H*expit(eta[i]);dv=np.zeros(2);dv[i]=v*(1-v/H)
    h=bump(r);a=v+(1-v/H)*h
    return a/np.sqrt(1-a*a),dv*(1-h/H)/(1-a*a)**1.5


def physical_slope_prime(r,eta):
    w,_=slopes(r,eta);h=bump(r)
    if MID[0]<=r<=MID[2]:
        v=H*expit(eta[int(r>MID[1])]);dv=0.
    else:
        s=-1 if r<MID[0] else 1;v=germ(r,s)
        rim=A0 if s==-1 else B0
        xi=abs(r-rim);edge=RATIO[s]*np.ldexp(1/512,-FIRST[s])
        t=max(0.,min(1.,(xi-edge)/EPS));y=edge+EPS*(t-t**4*(2.5-3*t+t*t))
        raw=.5*(y/RATIO[s])**4
        dv=-s*2*y**3/RATIO[s]**4*(1-stepp(t)[0])/(1+raw*raw)**1.5
    return ((1-v/H)*bump_prime(r)+dv*(1-h/H))*(1+w*w)**1.5


def pieces(sign):
    limits=[CUT[-1],CUT[-1]+EPS,CUT[1]-EPS,CUT[1],*MID]
    for s in BEG:
        for c in (s,s+RAMP,s+RAMP+TOP,s+2*RAMP+TOP):limits.extend((c-EPS,c+EPS))
    v=sorted(set(limits))
    return [r for r in (v if sign==-1 else v[::-1]) if (r<=CENTER if sign==-1 else r>=CENTER)]


def coordinate(v):
    if not (0<v<H):raise ValueError('Each physical valley is strictly between 0 and .56.')
    return math.log(v/(H-v))


def port_data(final,records):
    """Read retained real R738 cell lines and the R734 literal. No transfer is evaluated again."""
    from r738_negative_tail_and_macro_source import checked_line
    class ReadOnly:
        def __init__(self,p):self.records=p
        def once(self,k,f):raise KeyError('Missing genuine completed R738 negative unit '+k)
    b=ReadOnly(records);ports={}
    for s in SIGNS:
        for j in (2,3):
            for n in range(FIRST[s],0):
                if f'r738_certified_line_{s}_{j}_{n}' not in records:raise KeyError('Incomplete R738 cut.')
            z=checked_line(final,s,j,b,0)
            if not z['available']:raise ValueError('Wrong certified paid negative normalization.')
            ports[s,j]=z
    return ports
