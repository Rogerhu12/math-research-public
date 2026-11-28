#!/usr/bin/env python3
"""Construct and optimize an actual nonelliptic H65 field through the complete R205 cuff."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import copy
from fractions import Fraction
import importlib.util
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace
import time

import numpy as np
from scipy.interpolate import BPoly, BSpline
from scipy.optimize import lsq_linear


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


here = Path(__file__).parent
core = load(here/"2ecf-strong-hf-fixed-metric-full-spectral-position.py", "stadium_joint_solver")
carrier = load(here/"2ecf-strong-hf-refined-spectral-carrier.py", "stadium_true_old_carrier")
shapes = load(here/"2ecf-strong-stadium-support-physical-H65.py", "stadium_support")
hf = core.hf
c = core.c
pairs = core.full.two.PAIRS
polynomials = core.full.two.POLY


def step(t):
    return (t**3*(10+t*(-15+6*t)), 30*t*t*(1-t)**2, 60*t*(1-t)*(1-2*t))


class Clock:
    def __init__(self, old, b, end, extra):
        self.old = old
        self.b = b
        self.oldend = old.jets([end])[0][0]
        self.extra = float(extra)
        self.L = self.oldend-b
        if self.extra < 0 or self.L <= 0:
            raise ValueError("Positive new material clock required")

    def relative(self, old_s):
        t = np.clip((old_s-self.b)/self.L, 0., 1.)
        w, dw, ddw = step(t)
        return old_s+self.extra*w, 1+self.extra*dw/self.L, self.extra*ddw/self.L**2

    def jets(self, x):
        s, h, hx = self.old.jets(x)
        out, q, qp = self.relative(s)
        return out, q*h, qp*h*h+q*hx

    def physical_matrices(self, basis, x):
        return c.Clock.physical_matrices(self, basis, x)


class Prefix:
    def __init__(self, args, b):
        self.src = json.loads(args.stadium.read_text())
        if (self.src["entry"] != c.sha(shapes.__file__) or self.src["ramp"] != c.sha(args.stadium_ramp)
                or self.src["coast"] != c.sha(args.stadium_coast)):
            raise ValueError("Actual new native support and both new physical masters required")
        sp = self.src["exact"]
        self.support = shapes.Support(sp["offset"], sp["power"])
        self.warm = load(args.scripts/"6a65-geometry-cauchy-unit-t-warm.py", "stadium_true_material_ports")
        m = self.warm.WarmMaster(args.stadium_ramp,args.stadium_coast,coast_length=self.src["coastLength"])
        self.master = m
        m.central = self.support
        m.candidate = object.__new__(self.warm.p.Candidate)
        m.candidate.length = m.ramp
        m.candidate.v = m.v
        m.candidate.ellipse = SimpleNamespace(A=float(self.support.A),B=float(self.support.B),a0=1.)
        self.b = b
        q = Fraction.from_float
        self.coastlen = float(q(b)-q(m.c)-q(m.ramp))
        self.coastdiff = float(q(m.c)+q(m.ramp)+q(m.coast)-q(b))
        self.start_radius = m.curve.a+m.v*m.coast
        angle_cache = {}
        ramp_cache = {}
        orig = m.ramp_port
        def angles(u):
            key = u.tobytes()
            if key not in angle_cache:
                theta = self.support.theta(u)
                rh = self.support.rho(theta)
                angle_cache[key] = (np.exp(1j*theta[:,None]*m.wave), 1/rh, -self.support.rho(theta,1)/rh**3)
            return angle_cache[key]
        def ramp_port(i,u,repair=True):
            key = i,u.tobytes(),repair
            if key not in ramp_cache:
                ramp_cache[key] = self.support.port(m.c,u) if i == 0 else orig(i,u,repair)
            return ramp_cache[key]
        m.angles = angles
        m.ramp_port = ramp_port

    def rows(self, x, u):
        m = self.master
        end = float(Fraction.from_float(m.c)+Fraction.from_float(m.ramp))
        sample = self.support.port(0.,u)
        jets = np.zeros((len(x),6,len(u),3))
        f = np.zeros((len(x),3))
        for i,xx in enumerate(x):
            if xx <= m.c:
                sample["P"][:,2] = xx
                row = self.warm.packet_from_port(sample)
            elif xx < end:
                row = m.jet(xx,u)
            else:
                tau = max(0.,self.coastlen-(self.b-xx))
                w, dw, ddw = step(tau/self.coastlen)
                sigma = tau+self.coastdiff*w
                derivative = 1+self.coastdiff*dw/self.coastlen
                second = self.coastdiff*ddw/self.coastlen**2
                if xx == self.b:
                    sigma,derivative,second = m.coast,1.,0.
                row = self.warm.packet_from_port(m.coast_port(sigma,u))
                row["Xss"] = row["Xss"]*derivative**2 + row["Xs"]*second
                row["Xs"] = row["Xs"]*derivative
                row["Xsu"] = row["Xsu"]*derivative
                row.update(f=m.curve.a+m.v*sigma,fs=m.v*derivative,fss=m.v*second)
            jets[i] = np.stack([row[k] for k in ("X","Xs","Xu","Xss","Xsu","Xuu")])
            f[i] = [row[k] for k in ("f","fs","fss")]
        return jets,f


def difference(new,old):
    return {k: np.asarray(new[k])-np.asarray(old[k])
        for k in ("P","V","A","Pu","Vu","Au","Puu","Vuu","Auu")}


def add_lift(jets, coordinate, port, length, factor):
    ind = np.flatnonzero((coordinate > 0) & (coordinate < length))
    t = coordinate[ind]/length
    for jet,(i,j) in enumerate(pairs):
        tt = np.stack([t**(a-i)*(math.factorial(a)//math.factorial(a-i)) for a in range(i,6)],axis=1)
        w = (tt @ polynomials[:3,i:].T)*length**(np.arange(3)-i)
        D = np.stack([port[k+"u"*j] for k in ("P","V","A")])
        jets[ind,jet] += factor*np.einsum("nr,ruj->nuj",w,D,optimize=True)


def stream_carrier(args):
    """Evaluate each physical old block once, retaining one set of actual full coordinates."""
    saved=json.loads(args.prepared.read_text())
    observer=json.loads(args.observer.read_text())
    target=json.loads(args.diagonal.read_text())
    warp=json.loads(args.warp.read_text())
    sw=json.loads(args.warm.read_text())
    sr=json.loads(args.refined_state.read_text())
    meta=sr["model"]
    for key,path in (("physicalSource",args.field),("baseAngleClock",args.angular_clock),("target",args.diagonal),
            ("warp",args.warp),("prepared",args.prepared),("parent",args.parent),("observer",args.observer),
            ("ramp",args.ramp),("coast",args.coast),("literalParent",args.warm)):
        if meta[key]!=c.sha(path):raise ValueError(("Old literal physical source differs",key))
    if (meta["actualMetric"]!=c.stable(target["definition"]) or sw["model"]["physicalBasis"]!=meta["trueCarrierBasis"]
            or meta["actualMetric"]!=warp["fixedMetric"] or args.frequency!=meta["angularFrequency"]):
        raise ValueError("Changed actual physical clock or Cartesian carrier")
    stream=load(args.scripts/"6a65-cartesian-complete-stream.py","stadium_stream")
    freq=load(args.helpers/"2ecf-polar-fourier-refinement.py","stadium_all_channels")
    radius=load(args.helpers/"2ecf-polar-log-radius-operator.py","stadium_cache")
    def restore(desc):
        obj=object.__new__(stream.HalfTurnBasis)
        obj.definition=desc["sourceChartBasis"]
        obj.knots=np.asarray(obj.definition["physicalKnots"])
        obj.degree=5;obj.breaks=np.unique(obj.knots)
        obj.c,obj.end=obj.breaks[[0,-1]]
        obj.full_count=len(obj.knots)-6;obj.nb=obj.full_count-6
        obj.M=int(obj.definition["maxAngularFrequency"]);obj.channels=freq.full_channels(obj.M)
        obj.na=len(obj.channels);obj.dimension=obj.na*obj.nb
        obj.modes=np.array([k for _,k,_ in obj.channels])
        obj._spline=BSpline(obj.knots,np.eye(obj.full_count),5,extrapolate=False)
        if obj.dimension!=desc["dimension"]:raise ValueError("Literal source has different dimension")
        return obj
    raw24=restore(meta["trueCarrierBasis"])
    raw32=restore(meta["physicalBasis"])
    clock=hf.d.SquareClock(raw24,np.array([float.fromhex(v) for v in target["definition"]["CEradialHex"]]))
    B24=c.physical_basis(raw24,clock,meta["actualMetric"]);B32=c.physical_basis(raw32,clock,meta["actualMetric"])
    Z24=np.asarray(sw["totalCoefficients"]).reshape(B24.nb,B24.na)
    Z32=np.asarray(sr["totalRefinedCoefficients"]).reshape(B32.nb,B32.na)
    arb=core.full.two.ArbitraryHF(args)
    p=core.full.two.Wave(arb.orig.knots,warp["pFrequencies"],False)
    q=core.full.two.Wave(arb.orig.knots,warp["qFrequencies"],True)
    factor=warp["actualG10Trials"][warp["chosen"]]["factor"]
    pv=factor*np.array([float.fromhex(v) for v in warp["pCoefficientHex"]])
    qv=factor*np.array([float.fromhex(v) for v in warp["qCoefficientHex"]])
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","true_M32_shift").direct_packet
    physical={}
    for name,data in list(saved["caches"].items())+[("independent",observer)]:
        if c.sha(data["files"]["jets"])!=data["SHA256"]["jets"]:raise ValueError("Actual complete outside source differs")
        x=np.asarray(data["physicalNodes"] if name=="independent" else data["nodes"])
        u=np.asarray(data["angles"])
        if u.ndim==0:u=2*np.pi*np.arange(int(u))/int(u)
        jsrc=np.load(data["files"]["jets"],mmap_mode="r")
        jets=np.zeros((len(x),6,len(u),3))
        ks=np.flatnonzero(x>raw24.end)
        jets[ks]=jsrc[ks]
        inds=np.flatnonzero((x>raw24.c)&(x<=raw24.end))
        for start in range(0,len(inds),6):
            k=inds[start:start+6];xx=x[k]
            actual=arb.actual(xx,u,p,q,pv,qv)
            _,h,hx=clock.jets(xx)
            jets[k]=c.physical_jet(actual,h,hx)
            if name=="independent":
                jets[k]+=direct(B24,xx,Z24,u)+direct(B32,xx,Z32,u)
            else:
                jets[k]+=B24.packet(B24.matrices(xx),Z24,len(u))+B32.packet(B32.matrices(xx),Z32,len(u))
        physical[name]=radius.ArrayCache(x,u,jets,np.zeros((len(x),3)))
        print(json.dumps(dict(event="one_actual_source_group",group=name,radials=len(x),angles=len(u))),flush=True)
    return saved["definition"],B32,clock,physical,physical.pop("independent"),{},dict(stream=stream),radius,meta


def field(args):
    initial = time.monotonic()
    args.metric_sextic=.2
    args.curvature_tau=2.
    definition,basis,oldclock,physical,g11,weights,mods,radius,meta = stream_carrier(args)
    definition = copy.deepcopy(definition)
    raw = copy.copy(basis)
    del raw.matrices
    raw.definition = basis.definition["sourceChartBasis"]
    b = raw.c
    newclock = Clock(oldclock,b,raw.end,args.extra)
    cut = newclock.jets([raw.end])[0][0]
    pref = Prefix(args,b)
    definition["pointConfig"]["central_a"] = float(pref.support.A)
    old = core.full.two.ArbitraryHF(args)
    cache = dict(**physical,independent=g11)
    saved = json.loads(args.prepared.read_text())
    preliminary = {}
    ports = {}
    S = cut-b
    center = pref.start_radius
    v = pref.master.v
    controls = np.array([center,center+S*v/5,center+2*S*v/5,.8+2*S/5,.8+S/5,.8])
    profile = BPoly(controls[:,None], [b,cut],extrapolate=False)
    for name,obj in cache.items():
        x = obj.nodes
        old_s,h0,_ = oldclock.jets(x)
        s,q,qp = newclock.relative(old_s)
        _,h,hx = newclock.jets(x)
        for j in range(0,len(x),12):
            sl=slice(j,j+12)
            obj.jets[sl] = c.physical_jet(obj.jets[sl],q[sl],qp[sl])
        obj.s,obj.h,obj.hx = s,h,hx
        if name != "independent":
            weights[name] = {k:.5*np.asarray(w)*h for k,w in saved["caches"][name]["weights"].items()}
        iz = np.flatnonzero(x<=b)
        mat = raw.matrices(x)
        rad = np.zeros((len(x),3))
        obj.jets[iz],rad[iz] = pref.rows(x[iz],obj.u)
        active = (x>b)&(x<=raw.end)
        ex = x>raw.end
        for k in range(3):
            rad[active,k] = profile(s[active],nu=k)
        rad[ex,0] = .8-(s[ex]-cut)
        rad[ex,1] = -1.
        preliminary[name] = rad
        obj.radius = rad.copy()
        ports[name] = difference(pref.master.coast_port(pref.master.coast,obj.u),old.ports[0](obj.u))
    print(json.dumps(dict(event="full_actual_stadium_ports",shape=pref.src["exact"]["A"],seconds=time.monotonic()-initial,
        maximumPortChanges={k:float(np.linalg.norm(v,axis=-1).max()) for k,v in ports["training"].items()},
        material=[b,cut],bernstein=controls.tolist())),flush=True)
    fitname = "training"
    fit_length = args.fit_length
    for name,obj in cache.items():
        add_lift(obj.jets,obj.s-b,ports[name],fit_length,1.)
    train = cache[fitname]
    pos = (train.nodes>b)&(train.nodes<raw.end)
    x = train.nodes[pos]
    low=[];high=[]
    for name in ("training","observer"):
        packet = cache[name].jets[pos,2]
        G = np.sum(packet*packet,axis=-1)
        low.append(G.min(axis=1));high.append(G.max(axis=1))
    desired = .5*np.log((np.min(low,axis=0)+np.max(high,axis=0))/2)-np.log(preliminary[fitname][pos,0])
    newB = c.physical_basis(raw,newclock,"provisional")
    B,_,Bss = [a.toarray() for a in newB.matrices(x)]
    w = np.sqrt(weights[fitname]["metric"][pos])
    A = np.vstack((w[:,None]*B,args.fit_smoothing*w[:,None]*Bss,1e-6*np.eye(raw.nb)))
    rhs = np.r_[w*desired,np.zeros(len(x)+raw.nb)]
    sol = lsq_linear(A,rhs,bounds=(-.3,.3),tol=5e-13)
    if not sol.success:raise ArithmeticError("New positive angular metric fit failed")
    al = sol.x
    spec = dict(schema="positive-support-new-H65-longer-material-quintic-exp-log-radius-v1",
        entry=c.sha(__file__),support= pref.src["exact"],ramp=pref.src["ramp"],coast=pref.src["coast"],
        baseClock=meta["actualMetric"],delta=float(args.extra).hex(),outerQuintic=controls.tolist(),
        radiusKnots=raw.knots.tolist(),logExpCoefficientsHex=[float(z).hex() for z in al],
        sewnAtChart=[b,raw.end],physicalEnds=[b,cut],fitLiftLength=fit_length,smoothing=args.fit_smoothing,
        centralProfile="1 then actual original normalized H65 ramp and corrected coast",
        chart="snew=sold+extra*H5((sold-b)/(oldcut-b)), extended constantly at ends",
        positiveClockDerivativeAtLeastOneRelativeToOriginal=True,endpointPositionJetOrderPreserved=2)
    digest = c.stable(spec)
    basis = c.physical_basis(raw,newclock,digest)
    for name,obj in cache.items():
        a,aa,aaa = preliminary[name].T
        d,dd,ddd = (m@al for m in basis.matrices(obj.nodes))
        obj.radius = np.exp(d)[:,None]*np.column_stack((a,aa+a*dd,aaa+2*aa*dd+a*(ddd+dd**2)))
    lengths = sorted(set(args.lengths+[fit_length]))
    scores=[]
    current = fit_length
    for ell in lengths:
        for name,obj in physical.items():
            add_lift(obj.jets,obj.s-b,ports[name],current,-1.)
            add_lift(obj.jets,obj.s-b,ports[name],ell,1.)
        actual = hf.sample(physical,mods,saved,definition,newclock,args)
        cost = max(v["metric"]/args.metric_scale for v in actual.values())
        cost = max(cost,max(v["curvature"]/args.curvature_scale for v in actual.values()))
        scores.append(dict(length=ell,selection=cost,G10=actual))
        print(json.dumps(dict(event="stadium_length",length=ell,selection=cost,metric=max(v["metric"] for v in actual.values()),
            curvature=max(v["curvature"] for v in actual.values()),held=min(v["held"] for v in actual.values()))),flush=True)
        current = ell
    best = min(scores,key=lambda row:row["selection"])
    ell = best["length"]
    for name,obj in cache.items():
        add_lift(obj.jets,obj.s-b,ports[name],fit_length if name=="independent" else current,-1.)
        add_lift(obj.jets,obj.s-b,ports[name],ell,1.)
    independent = hf.sample({"independent":g11},mods,saved,definition,newclock,args)["independent"]
    expected = sum(v["original"] for v in best["G10"].values()),independent["metric"]
    if args.resume:
        st=json.loads(args.resume.read_text())
        if st["model"]["stadiumTarget"] != digest or st["model"]["liftLength"] != ell:
            raise ValueError("Different new actual stadium geometry or target")
        z=np.asarray(st["coefficients"]).reshape(basis.nb,basis.na)
        direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","stadium_independent").direct_packet
        for name,obj in cache.items():
            for j in range(0,len(obj.nodes),18):
                sl=slice(j,j+18);x=obj.nodes[sl]
                obj.jets[sl]+=direct(basis,x,z,obj.u) if name=="independent" else basis.packet(basis.matrices(x),z,len(obj.u))
        expected=st["stages"][-1]["allG10"]["original"],st["stages"][-1]["independent"]["metric"]
    receipt=dict(entry=c.sha(__file__),schema="new-actual-full-stadium-through-original-developed-tail-v1",
        newG=spec,newGSHA=digest,oldSource=meta,selectedLength=ell,trainingTrials=scores,
        independent=independent,scoreUsesG11=False,seconds=time.monotonic()-initial)
    c.save(Path(str(args.prefix)+"-source.json"),receipt)
    info=dict(stadiumEvaluator=c.sha(__file__),stadiumTarget=digest,actualMetric=digest,
        originalHFCarrier=meta,physicalBasis=basis.definition,centralSupport=pref.src["exact"],
        maximumMaterial=cut,additionalLength=args.extra,liftLength=ell,stadiumReceipt=Path(str(args.prefix)+"-source.json").name,
        inheritedFixedGIterations=0,newTarget=True,newPositions=True,newPrefix=True,heldPhaseCenterA=float(pref.support.A),
        trueG10Rows=4291840,independentG11UsedForTraining=False,
        actualPriorNewStadiumStage=c.sha(args.resume) if args.resume else None)
    print(json.dumps(dict(event="selected_actual_stadium_field",length=ell,G11=independent,fixedMetric=digest,
        totalOriginal=expected[0],seconds=time.monotonic()-initial)),flush=True)
    return definition,basis,newclock,physical,g11,weights,mods,radius,info,expected


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    hf.args_hf(ap)
    for k in ("diagonal","warp","warm","refined-state","stadium","stadium-ramp","stadium-coast","prefix"):
        ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--resume",type=Path)
    ap.add_argument("--frequency",type=int,default=32)
    ap.add_argument("--extra",type=float,default=.018)
    ap.add_argument("--fit-length",type=float,default=.42)
    ap.add_argument("--fit-smoothing",type=float,default=.00004)
    ap.add_argument("--lengths",type=float,nargs="+",default=[.20,.30,.42,.55,.68,.80])
    ap.add_argument("--metric-scale",type=float,default=.13)
    ap.add_argument("--curvature-scale",type=float,default=18.)
    ap.add_argument("--original-weight",type=float,default=1.)
    ap.add_argument("--coordinate-scale",type=float,default=.035)
    ap.add_argument("--betas",nargs="+",type=float,default=[20.,55.,110.])
    ap.add_argument("--iterations",type=int,default=64)
    ap.add_argument("--ridge",type=float,default=1e-6)
    ap.add_argument("--block",type=int,default=36)
    ap.add_argument("--source-only",action="store_true")
    args=ap.parse_args()
    if args.source_only:
        field(args)
    else:
        # Carrier.prepare calls the literal original source's prepare; avoid a recursive override.
        original_prepare=core.full.prepare
        def new_prepare(args):
            core.full.prepare=original_prepare
            return field(args)
        core.full.prepare=new_prepare
        core.main(args)
