#!/usr/bin/env python3
"""Continuous exact R137 exit derivative bounds for the R233 Gamma95 input.

Uses outward 96-bit integer interval Taylor jets. The point labels are
native Gamma angles; the material exit angle is a proved degree-one map.
No numerical arclength inverse, sampled maxima, or fitted port is used.
"""
from __future__ import annotations
import os
for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[name]="1"
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

COAST_SHA="f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d"
PORT_REPORT_SHA="23fd5b56609e5b35725758a5a822ce893e61c6b8204db7b3e29ef592ba221b0f"


def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp)
    sys.modules[name]=m
    sp.loader.exec_module(m)
    return m


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def vector_norm_upper(v,cert):
    return cert.upper_i(cert.norm2(v).sqrt())


def exact_outlet(gamma,arc,f0,v,length,alg,cert):
    """Entire interval jet through native-angle derivatives, exact R137."""
    I=cert.I
    gp=alg.vderivative(gamma)
    speed=alg.sqrt(alg.dot(gp,gp))
    inverse=alg.inv(speed)
    T=alg.vscale(inverse,gp)
    Du=lambda z:alg.mul(alg.scale(arc,inverse),alg.derivative(z))
    Duv=lambda z:alg.vscale(alg.scale(arc,inverse),alg.vderivative(z))
    Tu=Duv(T)
    K=alg.sqrt(alg.dot(Tu,Tu))
    U=alg.vscale(alg.inv(K),Tu)
    ratio_v=alg.scale(v,alg.inv(K))
    one=alg.constant(1,len(ratio_v))
    rad=alg.sub(one,alg.mul(ratio_v,ratio_v))
    if rad[0].lo<=0:
        raise ArithmeticError("Cannot prove positive inlet director square root")
    d=alg.vadd(alg.vneg(alg.vscale(ratio_v,U)),
              alg.vscale(alg.sqrt(rad),alg.cross(T,U)))
    normal=alg.cross(d,T)
    n=alg.scale(1/f0,alg.dot(Tu,normal))
    m=alg.scale(1/f0,alg.dot(Duv(d),normal))
    if n[0].lo<=0:
        raise ArithmeticError("Exact Gamma inlet has unproved positive n")
    k=alg.mul(m,alg.inv(n))
    ku=Du(k)
    one=alg.constant(1,len(k))
    kk=alg.add(one,alg.mul(k,k))
    r0=f0/v
    r=r0+length
    delta=length*(2*r0+length)
    root=alg.sqrt(alg.add(alg.constant(r0.square(),len(kk)),alg.scale(delta,kk)))
    w=alg.scale(delta,alg.inv(alg.add(alg.constant(r0,len(root)),root)))
    A=alg.add(alg.constant(r0,len(w)),alg.mul(kk,w))
    D=alg.add(alg.constant(f0,min(len(w),len(ku))),
              alg.mul(w,alg.sub(alg.scale(v,kk),ku)))
    if D[0].lo<=0:
        raise ArithmeticError("Exact exit is not certified before ruling focus")
    Ut=alg.mul(D,alg.inv(alg.scale(v,A)))
    if Ut[0].lo<=0:
        raise ArithmeticError("Exact exit material map is not increasing")
    kexit=alg.scale(r0,alg.mul(k,alg.inv(A)))
    lam=alg.scale(f0,alg.mul(alg.mul(n,kk),alg.inv(D)))
    exit_kk=alg.mul(kexit,kexit)
    l=alg.mul(lam,alg.mul(exit_kk,
          alg.inv(alg.add(alg.constant(1,len(exit_kk)),exit_kk))))
    c=alg.add(alg.constant(r0,len(w)),w)
    b=alg.mul(k,w)
    # In the unchanged tangent plane, radial/azimuthal axes rotate by -beta.
    V=alg.vscale(alg.constant(1/r,len(c)),
                alg.vadd(alg.vscale(c,d),alg.vneg(alg.vscale(b,T))))
    Texit=alg.vscale(alg.constant(1/r,len(c)),
                alg.vadd(alg.vscale(b,d),alg.vscale(c,T)))
    acceleration=alg.vscale(l,normal)
    # u_exit derivative = (1/U_t) D_u_inlet; no inverse is evaluated.
    conversion=alg.mul(alg.scale(arc,inverse),alg.inv(Ut))
    Vu=alg.vscale(conversion,alg.vderivative(V))
    Au=alg.vscale(conversion,alg.vderivative(acceleration))
    Tu_exit=alg.vscale(conversion,alg.vderivative(Texit))
    return dict(
        V=[z[0] for z in V], Vu=[z[0] for z in Vu],
        A=[z[0] for z in acceleration], Au=[z[0] for z in Au],
        T=[z[0] for z in Texit], Tu=[z[0] for z in Tu_exit],
        D=D[0], Ut=Ut[0], k=k[0], n=n[0], principal=lam[0],
        l=l[0], l_u=alg.mul(conversion,alg.derivative(l))[0])


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--scripts",type=Path,required=True)
    p.add_argument("--port-source",type=Path,required=True)
    p.add_argument("--port-report",type=Path,required=True)
    p.add_argument("--coast-master",type=Path,required=True)
    p.add_argument("--cells",type=int,default=2048)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh continuous exit report required")
    if sha(args.coast_master)!=COAST_SHA or sha(args.port_report)!=PORT_REPORT_SHA:
        raise ValueError("Same R233 exact Gamma/arc input required")
    cert=load(args.scripts/"6a65-m12-r137-continuous-domain.py","coast_exit_integer")
    port=load(args.port_source,"coast_exit_Fourier")
    alg=port.Series(cert)
    I=cert.I
    report=json.loads(args.port_report.read_text())
    if report["fullAngularDomainCertified"] is not True:
        raise ValueError("A full R233 primitive/arc certificate is required")
    box=lambda row:I(Q(row["lo"]),Q(row["hi"]))
    arc=box(report["accurateRawArc"])
    f0=box(report["exactTargetRadius"])
    with np.load(args.coast_master,allow_pickle=False) as master:
        co,si=port.real_curve(master["curve_modes"],master["curve_coefficients"])
        v=I(Q.from_float(float(master["v"])))
        length=I(Q.from_float(float(master["length"])))
    if len(co)!=96 or args.cells<512:
        raise ValueError("Complete Gamma95 and explicit continuous angular domain required")
    curve=port.Fourier(co,si,cert,max_order=11)
    pi=cert.pi_interval()
    trig={}
    def phase(index,count):
        key=(index%(2*count),count)
        if key not in trig:
            residue=key[0]
            n=residue if residue<=count else residue-2*count
            trig[key]=cert.sincos(pi*Q(n,count))
        return trig[key]
    start=time.monotonic()
    upper={key:I(0) for key in ("V","Vu","A","Au","T","Tu","l_u","principal")}
    lower={"D":None,"Ut":None}
    allrows=hashlib.sha256()
    for j in range(args.cells):
        points=curve.point(j,args.cells,phase,order=10)
        values=curve.box(points,pi/args.cells,order=8)
        jets=curve.series(values,order=8)
        out=exact_outlet(jets,arc,f0,v,length,alg,cert)
        record={}
        for key in upper:
            z=vector_norm_upper(out[key],cert) if isinstance(out[key],list) else I.raw(out[key].absupper(),out[key].absupper())
            if z.hi>upper[key].hi:
                upper[key]=z
            record[key]=str(z.upper())
        for key in lower:
            x=out[key].lower()
            if lower[key] is None or x<lower[key]:
                lower[key]=x
            record[key]=str(x)
        allrows.update(json.dumps(record,sort_keys=True,separators=(",",":")).encode()+b"\n")
        if j%256==0:
            print(json.dumps(dict(event="continuous_actual_coast_exit",cell=j,total=args.cells,
                Au=float(upper["Au"].upper()),Vu=float(upper["Vu"].upper()),
                seconds=time.monotonic()-start)),flush=True)
    output=dict(schema="6a65-R233-accurate-coast-exit-full-angular-derivative-bounds-v1",
        source=dict(entrySHA256=sha(__file__),coastMasterSHA256=COAST_SHA,
            portPrimitiveReportSHA256=PORT_REPORT_SHA,portSourceSHA256=sha(args.port_source),
            integerSourceSHA256=sha(args.scripts/"6a65-m12-r137-continuous-domain.py")),
        exactRawArc=report["accurateRawArc"],exactTargetRadius=report["exactTargetRadius"],
        coastLength=str(length.lower()),v=str(v.lower()),integerBits=cert.BITS,
        angularCells=args.cells,fullAngularDomainCertified=True,
        evaluatedPhysicalSection="actual accurate R137 coast exit",
        materialInverseNumericallyEvaluated=False,
        exactFormula="V=(c*d-b*T)/r; T_exit=(b*d+c*T)/r; A=l*N; d/du_exit=(arc/q)/U_t*d/dtheta",
        derivativeUpper={key:dict(rational=str(z.upper()),display=float(z.upper())) for key,z in upper.items()},
        domainLower={key:dict(rational=str(z),display=float(z)) for key,z in lower.items()},
        allIntegerRowsSHA256=allrows.hexdigest(),
        angularSpeedOfWholeWindowCertified=False,wholeWindowImmersionCertified=False,
        wholeClosedReachCertified=False,seconds=time.monotonic()-start,
        OSExitCode=None,externalExitReceiptRequired=True)
    args.output.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps(dict(event="accurate_exit_complete",reportSHA256=sha(args.output),
        seconds=output["seconds"],bounds=output["derivativeUpper"])),flush=True)


if __name__=="__main__":
    main()

