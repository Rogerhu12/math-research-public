"""Outward interval bounds for A-integral and the two warp buffers.

This is a background-only certificate for the explicit finite source alpha
decimals. The deep exact root sequence is handled by the separate N160 lemma.
No nonlinear surface or reach assertion is made here.
"""
from pathlib import Path
import json
import sys
import mpmath as mp

mp.iv.dps = 40
I = mp.iv.mpf


def hull(lo, hi):
    return I([lo.a, hi.b])


def quintic(x):
    def point(t):
        return t**3 * (10 + t * (-15 + 6*t))
    return hull(point(x.a), point(x.b))


def dquintic(x):
    def point(t):
        return 30*t*t*(1-t)*(1-t)
    a, b = point(x.a), point(x.b)
    lo = a if a.a <= b.a else b
    hi = I(15)/8 if x.a <= I('.5') <= x.b else (a if a.b >= b.b else b)
    return hull(lo, hi)


def seventh(t):
    return t**4*(35-84*t+70*t*t-20*t**3)


def cap_scalar(z, L):
    if z.b <= -L:
        return z
    if z.a >= L:
        return I(0)
    # Endpoint inputs can straddle a breakpoint only through outward rounding;
    # using the branch whose formula contains the exact endpoint is continuous.
    t=(z+L)/(2*L)
    def J(y):
        return y**5*(7-14*y+10*y*y-I('2.5')*y**3)
    v=t-J(t) if t.b <= I('.5') else I('.5')-J(1-t)
    return -L+2*L*v


def cap_derivative(z,L):
    if z.b <= -L:
        return I(1)
    if z.a >= L:
        return I(0)
    t=(z+L)/(2*L)
    return 1-seventh(t) if t.b <= I('.5') else seventh(1-t)


def cap(a, ap, c, cp, L):
    z=a-c
    if z.b <= -L:
        return a,ap
    if z.a >= L:
        return c,cp
    zzlo=max(z.a,-L);zzhi=min(z.b,L)
    low=cap_scalar(z.a,L) if z.a < -L else cap_scalar(zzlo,L)
    high=cap_scalar(z.b,L) if z.b > L else cap_scalar(zzhi,L)
    # cap_scalar is increasing, cap_derivative is decreasing.
    g=c+hull(low,high)
    d=hull(cap_derivative(z.b,L),cap_derivative(z.a,L))
    return g,d*ap+(1-d)*cp


def report(x):
    return {'interval':str(x),'lo_approx':float(x.a),'hi_approx':float(x.b)}


def run(path,subdivisions=32):
    data=json.loads(Path(path).read_text());cfg=data['config']
    assert cfg['orientation']==1 and cfg['protectCell']==160
    assert cfg['capMode']=='cut-preserving' and cfg['width']==.45
    assert cfg['rCut']==.6 and cfg['wCut']==.5 and cfg['curvatureBound']>=6
    assert cfg.get('delta0',.006)==.006 and cfg.get('R',64)==64
    assert cfg.get('prefixR',2)==2 and cfg.get('prefixReturnStart',8)==8 and cfg.get('prefixEnd',15)==15
    rc=I(3)/20; rcut=I(3)/5; wc=I(1)/2; delta0=I(3)/500
    root=mp.iv.sqrt(12); a=I(11)/4; ln2=mp.iv.log(2); eta0=delta0/20
    Y=6*delta0+6*eta0/(1-mp.iv.power(2,-I(3)/2))
    logeps=mp.iv.log(wc)+7*mp.iv.log(rc)+7*Y/root-a*mp.iv.log(2*delta0)
    oldcut=rc*mp.iv.exp(Y/root); K=I(str(cfg['curvatureBound']))
    # The finite/deep matching radius exceeds rc by less than 1e-48.
    after159=3*delta0/mp.iv.power(2,159)+6*eta0*mp.iv.power(2,-240)/(1-mp.iv.power(2,-I(3)/2))
    assert (after159/root).b<I('.5')
    assert (2*rc*after159/root).b<I('1e-48')
    Aupper=I(0); rows=[]; wmax=I(0)
    for n in range(160):
        delta=delta0/mp.iv.power(2,n);c=I(1)/20/mp.iv.power(2,I(n)/2)
        R=I(2) if n<8 else mp.iv.power(2,I(5*n-27)/8) if n<=15 else I(64)
        alpha=I(data['finiteCalibrations'][n]['alpha'])
        beta=I(str((cfg.get('valleyControls') or [])[n] if n<len(cfg.get('valleyControls',[])) else 0))
        after=3*delta0/mp.iv.power(2,n)+6*eta0*mp.iv.power(2,-I(3)*(n+1)/2)/(1-mp.iv.power(2,-I(3)/2))
        logr0=mp.iv.log(rc)+after/root
        logmu=logeps+a*mp.iv.log(delta)
        lp=[mp.iv.log(delta),mp.iv.log(R),2*mp.iv.log(delta)-mp.iv.log(alpha),I(0),mp.iv.log(delta)+a*ln2]
        caps=[cfg['slopeCap'],cfg.get('pulseCaps',[[]])[n][0] if n<len(cfg.get('pulseCaps',[])) else cfg['slopeCap'],cfg.get('valleyCaps',[])[n] if n<len(cfg.get('valleyCaps',[])) else cfg['slopeCap'],cfg.get('pulseCaps',[[]])[n][1] if n<len(cfg.get('pulseCaps',[])) else cfg['slopeCap'],cfg['slopeCap']]
        logcaps=[mp.iv.log(I(str(v))) for v in caps]
        offset=I(0);cellA=I(0)
        for j in range(9):
            length=delta*(1 if j in [2,4,6] else c)
            i=j//2
            l0=lp[i];l1=lp[i+1] if j%2 else l0
            c0=logcaps[i];c1=logcaps[i+1] if j%2 else c0
            if j==3:l1+=beta
            if j==4:l0+=beta;l1+=beta
            if j==5:l0+=beta
            segA=I(0)
            for k in range(subdivisions):
                x=I([k,k+1])/subdivisions;S=quintic(x);dS=dquintic(x)
                logr=logr0+(offset+length*x)/root
                r=mp.iv.exp(logr);rx=length*r/root
                raw=logmu+l0+(l1-l0)*S-mp.iv.log(delta)-7*logr
                rawp=(l1-l0)*dS-7*length/root
                lc=c0+(c1-c0)*S;lcp=(c1-c0)*dS
                g,gp=cap(raw,rawp,lc,lcp,I(str(cfg['capTransition'])))
                if n==0 and j==8:g,gp=raw,rawp
                if n==0 and j==7:
                    g,gp=raw+(1-S)*(g-raw),rawp+(1-S)*(gp-rawp)-dS*(g-raw)
                chi=I(1);j0=I(1)
                if n==159 and j==0:chi=S
                if n==0 and j==8:chi=1-S;j0=1+(rcut/oldcut-1)*S
                w=mp.iv.exp(g);E=1+w*w
                v=abs(w*gp)/mp.iv.power(E,I(3)/2)
                integrand=rx*j0*(1-chi)+chi*v/K
                # Sum upper endpoints as intervals to preserve directed rounding.
                segA+=integrand.b/subdivisions
                if w.b>wmax.b:wmax=w.b
            offset+=length;cellA+=segA
        Aupper+=cellA
        if n<20 or n==159:rows.append({'cell':n,'A_upper':report(cellA)})
    maxweight=max(max(r) for r in cfg.get('warpWeightLevels',[[1]]))
    Bupper=I(str(maxweight))*(oldcut-rc)
    targetlower=I('.45')-I('1e-48')
    alphaLower=(targetlower-Aupper)/Bupper
    # The cut collar has log length eta0/sqrt(12); source slope decreases.
    collarMinRadius=oldcut*mp.iv.exp(-eta0/root)
    collarMaxSlope=wc*mp.iv.exp(7*eta0/root)
    # w/(1+w²)^(3/2) increases on this interval, because w<1/sqrt(2).
    assert (2*collarMaxSlope**2).b<1
    Emax=1+collarMaxSlope**2
    C=7*collarMaxSlope/(collarMinRadius*mp.iv.power(Emax,I(3)/2)*K)
    J=rcut/oldcut
    bufferConditions={'J_minus_C':report(J-C),'alphaLower_over_Emax_minus_C_plus_1':report(alphaLower/Emax-C+1)}
    assert alphaLower.a>0,'A enclosure too wide to prove a positive warp'
    assert (J-C).a>0,'cut collar endpoint condition failed'
    assert (alphaLower/Emax-C+1).a>0,'free-width lower bound inadequate for cut buffer'
    assert (wmax/rc).b<K,'global angular curvature coarse bound exceeds K'
    deepPortSlopeUpper=wc*64/(6*delta0)*(I(10)/9)*mp.iv.power(2,-I(7)*159/4)
    deepPortCurvatureUpper=7*deepPortSlopeUpper/rc
    assert deepPortCurvatureUpper.b<K
    return {'scope':'Outward interval background-only bounds with exact displayed finite alpha decimals; no nonrotational theorem.',
            'input':str(path),'interval_dps':mp.iv.dps,'subdivisions_per_segment':subdivisions,
            'A_upper':report(Aupper),'B_upper':report(Bupper),'warp_alpha_lower':report(alphaLower),
            'max_slope_upper':report(wmax),'angular_curvature_upper':report(wmax/rc),
            'deep_port_curvature_upper':report(deepPortCurvatureUpper),
            'cut_buffer_conditions':bufferConditions,'cut_collar_C':report(C),'cut_collar_J':report(J),
            'cell_A_upper':rows,
            'conclusion':'For this exact finite background, the free warp coefficient is positive, both buffered ends and every chi=1 segment satisfy |kappa_mer|<=K; angular curvature is <K. Unchanged n>=160 is handled separately.'}


if __name__=='__main__':
    result=run(sys.argv[1],int(sys.argv[3]) if len(sys.argv)>3 else 32)
    out=json.dumps(result,indent=2)+'\n'
    if len(sys.argv)>2:Path(sys.argv[2]).write_text(out)
    print(json.dumps({k:result[k] for k in ['subdivisions_per_segment','A_upper','warp_alpha_lower','max_slope_upper','cut_buffer_conditions','conclusion']}))
