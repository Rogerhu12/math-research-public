"""Fresh suffix positions, actual metric jets, and physical row weights outside every G11 radius."""
import json
import numpy as np
from scipy.interpolate import BSpline


def add(args,core,carried):
    definition,basis,clock,physical,g11,weights,mods,radius,meta,expected,refined=carried
    full=core.full;c=core.c;two=full.two
    raw=json.loads(args.fresh_radius.read_text())
    if (raw["prepared"]!=c.sha(args.prepared) or raw["observer"]!=c.sha(args.observer)
        or raw["diagonal"]!=c.sha(args.diagonal) or raw["ramp"]!=c.sha(args.ramp) or raw["coast"]!=c.sha(args.coast)
        or raw["originalNineRowMaxDifference"]>5e-8):raise ValueError("Actual matched extra radius rows required")
    x=np.asarray(raw["chartNodes"]);u=np.arange(args.extra_angles)*2*np.pi/args.extra_angles
    tr=physical["training"].nodes
    if np.intersect1d(x,np.r_[tr,g11.nodes]).size or np.any(np.diff(x)<=0):
        raise ValueError("Additional radial labels must be independent from original G10 and G11")
    diag=json.loads(args.diagonal.read_text());spec=diag["definition"]
    warp=json.loads(args.warp.read_text())
    nt=np.load(args.field)
    af=BSpline(nt["alphaKnots"],np.pad(nt["alpha"],(3,3)),5,extrapolate=False)
    cg=np.asarray([float.fromhex(a) for a in spec["CGangularHex"]])
    target=BSpline(spec["basis"]["physicalKnots"],np.pad(cg,(3,3)),5,extrapolate=False)
    def angular_target(xx,jets):
        a,ax,axx=jets.T
        h,hx,hxx=(af(xx,nu=i) for i in (0,1,2))
        d,dx,dxx=(target(xx,nu=i) for i in (0,1,2))
        # The log target equals alpha plus half the logarithm of 1+Bcg.
        log=h+.5*np.log1p(d);lx=hx+.5*dx/(1+d)
        lxx=hxx+.5*(dxx/(1+d)-dx**2/(1+d)**2)
        sc=np.exp(log);r=a*sc;rx=(ax+a*lx)*sc
        rxx=(axx+2*lx*ax+a*(lxx+lx**2))*sc
        _,v,dv=clock.jets(xx)
        return np.column_stack((r,rx/v,rxx/v**2-rx*dv/v**3))
    rz=angular_target(x,np.asarray(raw["baseRadiusJets"]))
    old_radius=np.load(json.loads(args.prepared.read_text())["caches"]["training"]["files"]["radius"],mmap_mode="r")
    indices=np.flatnonzero((tr>=basis.c)&(tr<=basis.end))[::24]
    discrepancy=float(np.max(abs(angular_target(tr[indices],old_radius[indices])-physical["training"].radius[indices])))
    if discrepancy>5e-8:raise ArithmeticError("Fresh actual transformed angular target does not reproduce old rows")
    arb=two.ArbitraryHF(args);p=two.Wave(arb.orig.knots,warp["pFrequencies"],False);q=two.Wave(arb.orig.knots,warp["qFrequencies"],True)
    factor=warp["actualG10Trials"][warp["chosen"]]["factor"]
    coeff=lambda k:factor*np.asarray([float.fromhex(a) for a in warp[k]])
    pv,qv=coeff("pCoefficientHex"),coeff("qCoefficientHex")
    pos=json.loads(args.warm.read_text());z=np.asarray(pos.get("totalCoefficients",pos["coefficients"]))
    # The literal warm Cartesian field uses the prior raw physical knot vector.
    oldspec=meta["trueCarrierBasis"]["sourceChartBasis"];M=oldspec["maxAngularFrequency"]
    old=BSpline(oldspec["physicalKnots"],np.pad(z.reshape(-1,3*(2*M+1)),((3,3),(0,0))),5,extrapolate=False)
    sw=np.ones((3,len(u),2*M+1))
    sw[1:,:,0]=0.
    modes=np.arange(1,M+1)
    for j in range(3):
        sw[j,:,1::2]=modes**j*np.cos(u[:,None]*modes+j*np.pi/2)
        sw[j,:,2::2]=modes**j*np.sin(u[:,None]*modes+j*np.pi/2)
    packet=np.empty((len(x),6,len(u),3))
    for j in range(0,len(x),12):
        s=slice(j,j+12);xx=x[s]
        jets=arb.actual(xx,u,p,q,pv,qv)
        for col,(i,k) in enumerate(two.PAIRS):
            jets[:,col]+=np.einsum("rck,uk->ruc",old(xx,nu=i).reshape(len(xx),3,-1),sw[k],optimize=True)
        _,v,dv=clock.jets(xx)
        packet[s]=c.physical_jet(jets,v,dv)
        if args.refined_state:packet[s]+=basis.packet(basis.matrices(xx),refined,len(u))
    # Voronoi weights on the full original physical-chart interval, followed by
    # the same ds/dx derivative and old S normalization as G10. No old row shrinks.
    edge=np.r_[basis.c,.5*(x[:-1]+x[1:]),basis.end]
    _,h,_=clock.jets(x)
    w=args.extra_weight*np.diff(edge)*h/basis.end
    groupweights={k:mult*w for k,mult in (("metric",1.),("curvature",.01),("geometry",10.))}
    physical["extra"]=radius.ArrayCache(x,u,packet,rz);weights["extra"]=groupweights
    stream=mods["stream"];cfg=stream.point.PointConfig(**definition["pointConfig"])
    ar=core.load(args.scripts/"6a65-geometry-area-ratio-power-two.py","extra_actual_14_cost")
    total=0.;peak=0.;cp=0.
    for i in range(0,len(x),24):
        s=slice(i,i+24);jets=packet[s]
        ww={k:v[s,None]/len(u) for k,v in groupweights.items()}
        pt=stream.point.PointLinearized(jets.swapaxes(1,2),rz[s,0,None],cfg,ww)
        stat=pt.statistics();total+=stat["squaredNorm"]+ar.AreaPacket(jets,rz[s,0,None],ww["metric"],.5).stats["squaredNorm"]
        peak=max(peak,stat["maxRelativeMetric"]);cp=max(cp,stat["maxCurvature"])
    meta.update(extraRadiusSupplier=c.sha(args.fresh_radius),extraRadials=len(x),extraAngles=len(u),relativeExtraWeight=args.extra_weight,
        originalG10Rows=4291840,additionalPhysicalRows=len(x)*len(u)*14,freshNonG11=True,targetJetRebuildMaxDifference=discrepancy,
        initialExtraPhysicalCost=float(total),initialExtraMetric=peak,initialExtraCurvature=cp)
    return definition,basis,clock,physical,g11,weights,mods,radius,meta,(expected[0]+total,expected[1]),refined
