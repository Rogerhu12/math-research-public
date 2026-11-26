#!/usr/bin/env python3
"""Complete continuous old-terminal versus accurate R137 inlet port bounds.

The curve is the saved Gamma95 real Fourier sum. Every old terminal P/V/A
mode is retained. Same-native-angle Taylor differences are certified first;
the exact central-to-Gamma arc inverse and all two-jet composition terms are
then paid. The exact target is the frozen dyadic ellipse perimeter plus the
dyadic ramp increment, not the distinct narrow target box of original R224.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time
import numpy as np


RAMP_SHA='0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7'
COAST_SHA='f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d'
ARC_LO=Q(79658596287913338895451555727,79228162514264337593543950336)
ARC_HI=Q(79658596287972559706017116211,79228162514264337593543950336)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def upq(q,bits=160):
    if q<0:
        raise ValueError("Nonnegative bound required")
    s=1<<bits
    return Q((q.numerator*s+q.denominator-1)//q.denominator,s)


class Series:
    def __init__(self,cert):
        self.cert=cert
        self.I=cert.I

    def add(self,a,b):
        return [x+y for x,y in zip(a,b)]

    def neg(self,a):
        return [-x for x in a]

    def sub(self,a,b):
        return self.add(a,self.neg(b))

    def constant(self,x,n):
        return [self.I(x)]+[self.I(0) for _ in range(n-1)]

    def scale(self,c,a):
        return [self.I(c)*x for x in a]

    def mul(self,a,b):
        n=min(len(a),len(b))
        return [sum((a[j]*b[k-j] for j in range(k+1)),self.I(0)) for k in range(n)]

    def inv(self,a):
        if a[0].lo<=0<=a[0].hi:
            raise ArithmeticError("Taylor inverse has possible zero constant")
        result=[1/a[0]]
        for k in range(1,len(a)):
            result.append(-sum((a[j]*result[k-j] for j in range(1,k+1)),self.I(0))/a[0])
        return result

    def sqrt(self,a):
        if a[0].lo<=0:
            raise ArithmeticError("Taylor square root has no positive constant")
        result=[a[0].sqrt()]
        for k in range(1,len(a)):
            result.append((a[k]-sum((result[j]*result[k-j] for j in range(1,k)),self.I(0)))/(2*result[0]))
        return result

    def derivative(self,a):
        return [(j+1)*a[j+1] for j in range(len(a)-1)]

    def vderivative(self,a):
        return [self.derivative(x) for x in a]

    def vscale(self,c,a):
        return [self.mul(c,x) for x in a]

    def vadd(self,a,b):
        return [self.add(x,y) for x,y in zip(a,b)]

    def vneg(self,a):
        return [self.neg(x) for x in a]

    def dot(self,a,b):
        result=self.mul(a[0],b[0])
        for d in range(1,3):
            result=self.add(result,self.mul(a[d],b[d]))
        return result

    def cross(self,a,b):
        return [self.sub(self.mul(a[1],b[2]),self.mul(a[2],b[1])),
                self.sub(self.mul(a[2],b[0]),self.mul(a[0],b[2])),
                self.sub(self.mul(a[0],b[1]),self.mul(a[1],b[0]))]

    def inlet(self,gamma,arc,f0,v):
        gp=self.vderivative(gamma)
        speed=self.sqrt(self.dot(gp,gp))
        inverse=self.inv(speed)
        tangent=self.vscale(inverse,gp)
        tangent_theta=self.vderivative(tangent)
        Tu=self.vscale(self.scale(arc,inverse),tangent_theta)
        Tu_length=self.sqrt(self.dot(Tu,Tu))
        unit_curvature=self.vscale(self.inv(Tu_length),Tu)
        r=self.scale(v,self.inv(Tu_length))
        rad=self.sub(self.constant(1,len(r)),self.mul(r,r))
        if rad[0].lo<=0:
            raise ArithmeticError("Actual inlet does not certify |T_u|>v")
        director=self.vadd(self.vneg(self.vscale(r,unit_curvature)),
            self.vscale(self.sqrt(rad),self.cross(tangent,unit_curvature)))
        normal=self.cross(director,tangent)
        director_theta=self.vderivative(director)
        normal_curvature_numerator=self.dot(tangent_theta,normal)
        if normal_curvature_numerator[0].lo<=0:
            raise ArithmeticError("Actual inlet angle curvature lost positive orientation")
        mixed=self.dot(director_theta,normal)
        acceleration_scalar=self.scale(arc/f0,self.mul(self.mul(mixed,mixed),
            self.inv(self.mul(speed,normal_curvature_numerator))))
        acceleration=self.vscale(acceleration_scalar,normal)
        return dict(V=director,A=acceleration,q=speed,
            TuLength=Tu_length[0],normalCurvatureNumerator=normal_curvature_numerator[0])


class Fourier:
    def __init__(self,co,si,cert,max_order=13):
        self.co,self.si,self.cert=co,si,cert
        self.I=cert.I
        self.degree=len(co)-1
        self.max_order=max_order
        self.terms=[]
        self.absolute=[]
        for r in range(max_order+1):
            terms=[]
            bounds=[]
            for d in range(3):
                row=[]
                total=abs(co[0][d]) if r==0 else Q(0)
                for k in range(1,self.degree+1):
                    a,b=co[k][d]*k**r,si[k][d]*k**r
                    total+=abs(a)+abs(b)
                    if r%4==1:
                        a,b=b,-a
                    elif r%4==2:
                        a,b=-a,-b
                    elif r%4==3:
                        a,b=-b,a
                    if a or b:
                        row.append((k,self.I(a),self.I(b)))
                terms.append(row)
                bounds.append(total)
            self.terms.append(terms)
            self.absolute.append(bounds)

    def point(self,index,count,phase,order=12):
        values=[]
        for r in range(order+1):
            row=[]
            for d in range(3):
                val=self.I(self.co[0][d]) if r==0 else self.I(0)
                for k,a,b in self.terms[r][d]:
                    sn,cs=phase(k*(2*index+1),count)
                    val+=a*cs+b*sn
                row.append(val)
            values.append(row)
        return values

    def box(self,point,halfwidth,order=11):
        values=[]
        for r in range(order+1):
            row=[]
            for d in range(3):
                slope=self.I.raw(point[r+1][d].absupper(),point[r+1][d].absupper())
                error=self.cert.upper_i(halfwidth*slope+halfwidth.square()*self.I(self.absolute[r+2][d])/2)
                row.append(point[r][d]+self.I.raw(-error.hi,error.hi))
            values.append(row)
        return values

    def series(self,values,order=11):
        return [[values[r][d]/math.factorial(r) for r in range(order+1)] for d in range(3)]


def real_curve(modes,coeff):
    lookup={int(k):row for k,row in zip(modes,coeff)}
    degree=max(abs(k) for k in lookup)
    co=[[Q.from_float(float(x.real)) for x in lookup[0]]]
    si=[[Q(0)]*3]
    for k in range(1,degree+1):
        cp,cm=lookup.get(k,[0j]*3),lookup.get(-k,[0j]*3)
        co.append([Q.from_float(float(a.real))+Q.from_float(float(b.real)) for a,b in zip(cp,cm)])
        si.append([Q.from_float(float(b.imag))-Q.from_float(float(a.imag)) for a,b in zip(cp,cm)])
    return co,si


def old_port_fourier(model,node,port,cutoff=95):
    values=model.port(node)[port]
    D=model.degree
    scale=1<<model.input_bits
    co=[[Q(values[d][0][D],scale) for d in range(3)]]
    si=[[Q(0)]*3]
    for k in range(1,cutoff+1):
        co.append([Q(2*values[d][0][D+k],scale) for d in range(3)])
        si.append([Q(-2*values[d][1][D+k],scale) for d in range(3)])
    tails=[]
    for r in range(3):
        tails.append(sum((Q(2*k**r*(abs(values[d][0][D+k])+abs(values[d][1][D+k])),scale)
            for d in range(3) for k in range(cutoff+1,D+1)),Q(0)))
    return co,si,tails


def spectral_speed_residual(co,si,model,abox,gram):
    D=len(co)-1
    bits=max(gram.dyadic_bits(x/2) for row in co+si for x in row)
    C=[[[[0]*(2*D+1) for _ in range(2)] for _ in range(3)]]
    for d in range(3):
        C[0][d][0][D]=gram.scaled(co[0][d],bits)
        for k in range(1,D+1):
            re=gram.scaled(co[k][d]/2,bits)
            im=gram.scaled(-si[k][d]/2,bits)
            C[0][d][0][D+k]=C[0][d][0][D-k]=re
            C[0][d][1][D+k],C[0][d][1][D-k]=im,-im
    U=gram.angular(C,D)
    maximum=max(abs(x).bit_length() for row in U for pair in row for part in pair for x in part)
    packbits=2*maximum+(12*3*(2*D+1)).bit_length()+3
    G=gram.packed_gram(U,U,packbits,True)[0]
    pbox=(1+model.v*model.ramp/(2*abox[1]),1+model.v*model.ramp/(2*abox[0]))
    pbits=200
    mid=(pbox[0]+pbox[1])/2
    pmid=Q((2*mid.numerator*(1<<pbits)+mid.denominator)//(2*mid.denominator),1<<pbits)
    target_error=max(abs(pmid**2-pbox[0]**2),abs(pmid**2-pbox[1]**2))
    h0=(model.A**2+model.B**2)/2
    h2=(model.B**2-model.A**2)/4
    target=[pmid**2*h0,pmid**2*h2]
    outbits=max(2*bits,*(gram.dyadic_bits(x) for x in target))
    R=[[x<<(outbits-2*bits) for x in part] for part in G]
    for k,h in ((2*D,target[0]),(2*D-2,target[1]),(2*D+2,target[1])):
        R[0][k]-=gram.scaled(h,outbits)
    exact=[]
    for r in range(3):
        numerator=sum(abs(k)**r*(abs(R[0][k+2*D])+abs(R[1][k+2*D]))
            for k in range(-2*D,2*D+1))
        target_norm=model.A**2 if r==0 else 2**(r-1)*(model.A**2-model.B**2)
        exact.append(upq(Q(numerator,1<<outbits)+target_error*target_norm))
    return exact,pbox


def vector_bound(series,order,cert):
    return sum((Q(series[d][order].absupper(),cert.SCALE)*math.factorial(order) for d in range(3)),Q(0))


def taylor_difference(pointA,pointB,boxA,boxB,halfwidth,r,cert,order=6):
    # Point/box inputs are ordinary Taylor coefficients (derivative/factorial).
    total=Q(0)
    for j in range(r,r+order):
        factor=Q(math.factorial(j),math.factorial(j-r))*halfwidth**(j-r)
        total+=factor*sum((Q((pointA[d][j]-pointB[d][j]).absupper(),cert.SCALE) for d in range(3)),Q(0))
    j=r+order
    remainder=sum((Q((boxA[d][j]-boxB[d][j]).absupper(),cert.SCALE) for d in range(3)),Q(0))
    total+=Q(math.factorial(j),math.factorial(order))*halfwidth**order*remainder
    return upq(total)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--master',type=Path,required=True)
    ap.add_argument('--coast-master',type=Path,required=True)
    ap.add_argument('--gram-report',type=Path,required=True)
    ap.add_argument('--scripts-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--angular-cells',type=int,default=2048)
    ap.add_argument('--cell',type=int,action='append')
    args=ap.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh final-port continuous result required")
    if sha(args.master)!=RAMP_SHA or sha(args.coast_master)!=COAST_SHA:
        raise ValueError("This certificate consumes the published actual coupled-gap masters")
    start=time.monotonic()
    gp=args.scripts_dir/'6a65-geometry-ramp-native-gram-certificate.py'
    hp=args.scripts_dir/'6a65-m12-r137-continuous-domain.py'
    arcproof=args.scripts_dir.parent/'results/R225-gap105-strict-perimeter-and-normalization.md'
    prooftext=arcproof.read_text()
    if str(ARC_LO.numerator) not in prooftext or str(ARC_HI.numerator) not in prooftext or COAST_SHA not in prooftext:
        raise ValueError("Published same-master exact R225 arc enclosure required")
    gram=module(gp,'actual_final_port_gram')
    cert=module(hp,'actual_final_port_integer')
    I=cert.I
    algebra=Series(cert)
    model=gram.ActualRamp(args.master)
    report=json.loads(args.gram_report.read_text())
    if report['source']['masterSHA256']!=RAMP_SHA:
        raise ValueError("Same actual Gram input required")
    abox=tuple(map(Q,report['exactEllipticArcRadiusInterval']))
    f0=I(abox[0],abox[1])+I(model.v*model.ramp/2)
    with np.load(args.coast_master,allow_pickle=False) as c:
        co,si=real_curve(c['curve_modes'],c['curve_coefficients'])
        coast_length=Q.from_float(float(c['length']))
    if len(co)!=96:
        raise ValueError("Complete saved Gamma95 required")
    speed_residual,pbox=spectral_speed_residual(co,si,model,abox,gram)
    qmin=I((pbox[0]*model.B)**2-speed_residual[0]).sqrt().lower()
    point_speed_error=upq(speed_residual[0]/(qmin+pbox[0]*model.B))
    # A second exact integral enclosure, now tied to the new f0, intersects
    # R225 rather than relabeling its original target box.
    arc=I(max(ARC_LO,f0.lower()-point_speed_error),min(ARC_HI,f0.upper()+point_speed_error))
    if arc.lo<=0:
        raise ArithmeticError("Accurate perimeter is not positive")
    curve=Fourier(co,si,cert)
    old={}
    tails={}
    for p,name in enumerate(('P','V','A')):
        oc,os,ot=old_port_fourier(model,16,p)
        old[name]=Fourier(oc,os,cert)
        tails[name]=ot
    N=args.angular_cells
    selected=list(range(N)) if args.cell is None else args.cell
    if N<64 or len(set(selected))!=len(selected) or any(not 0<=j<N for j in selected):
        raise ValueError("Distinct valid continuous angular cells required")
    pi=cert.pi_interval()
    trig={}
    def phase(index,count):
        residue=index%(2*count)
        key=(residue,count)
        if key not in trig:
            numerator=residue if residue<=count else residue-2*count
            trig[key]=cert.sincos(pi*Q(numerator,count))
        return trig[key]
    half=pi/N
    halfq=half.upper()
    same={name:[Q(0)]*3 for name in ('V','A')}
    derivatives={name:[Q(0)]*4 for name in ('V','A')}
    speed_derivatives=[Q(0)]*3
    coast_bounds={}
    rows_hash=hashlib.sha256()
    for position,j in enumerate(selected):
        cp=curve.point(j,N,phase)
        cb=curve.box(cp,half)
        center=algebra.inlet(curve.series(cp),arc,f0,I(model.v))
        whole=algebra.inlet(curve.series(cb),arc,f0,I(model.v))
        local={}
        for name in ('V','A'):
            op=old[name].point(j,N,phase)
            ob=old[name].box(op,half)
            opj=old[name].series(op)
            obj=old[name].series(ob)
            bounds=[]
            for r in range(3):
                bound=taylor_difference(center[name],opj,whole[name],obj,halfq,r,cert)+tails[name][r]
                same[name][r]=max(same[name][r],bound)
                bounds.append(gram.upper(bound))
            local[name]=bounds
            for r in range(4):
                derivatives[name][r]=max(derivatives[name][r],upq(vector_bound(whole[name],r,cert)))
        for r in range(3):
            speed_derivatives[r]=max(speed_derivatives[r],upq(Q(whole['q'][r].absupper(),cert.SCALE)*math.factorial(r)))
        # Re-evaluate the actual complete R137 geometry with the new target
        # interval as part of this new port-consumption result.
        geometry=cert.geometry(cb[:5],arc,f0,I(model.v),I(coast_length),[I(x) for x in co[0]])
        if geometry['D'].lo<=I(Q(9,10)).hi or geometry['nonzero_principal_curvature'].hi>=I(Q(19,2)).lo:
            raise ArithmeticError("Same Gamma95 coast did not pass the explicit new f0 box")
        for key,value in geometry.items():
            coast_bounds[key]=value if key not in coast_bounds else cert.hull(coast_bounds[key],value)
        rows_hash.update((json.dumps(dict(index=j,portDifferences=local),sort_keys=True)+'\n').encode())
        if (position+1)%128==0 or position==len(selected)-1:
            print(json.dumps(dict(event='actual-port-angular-domain-covered',cells=position+1,total=len(selected),
                maximumSameAngle={key:[gram.upper(x) for x in val] for key,val in same.items()},
                seconds=time.monotonic()-start)),flush=True)
    delta_a=max(abs(arc.lower()-f0.upper()),abs(arc.upper()-f0.lower()))
    ellfirst=(model.A**2-model.B**2)/(2*model.B)
    e0=point_speed_error
    e1=upq(speed_residual[1]/(qmin+pbox[0]*model.B)
        +speed_residual[0]*(speed_derivatives[1]+pbox[1]*ellfirst)/(qmin+pbox[0]*model.B)**2)
    speed_zero=upq(e0+delta_a*model.A/abox[0])
    speed_first=upq(e1+delta_a*ellfirst/abox[0])
    angle_error=upq(pi.upper()*speed_zero/qmin)
    angle_first=upq((speed_zero+speed_derivatives[1]*angle_error)/qmin)
    angle_second=upq((speed_first+speed_derivatives[2]*angle_error
        +(2*angle_first+angle_first**2)*speed_derivatives[1])/qmin)
    alpha_error=upq(delta_a/arc.lower())
    alpha_max=1+alpha_error
    # Complete full-frequency P difference at the same native theta.
    P0=model.port(16)[0]
    D=model.degree
    scale=1<<model.input_bits
    P_same=[]
    gamma_bounds=[sum(row,Q(0)) for row in curve.absolute[:4]]
    for r in range(3):
        value=Q(0)
        for d in range(3):
            if r==0:
                value+=abs(co[0][d]-Q(P0[d][0][D],scale))
            for k in range(1,D+1):
                a=co[k][d] if k<len(co) else Q(0)
                b=si[k][d] if k<len(si) else Q(0)
                value+=k**r*(abs(a-Q(2*P0[d][0][D+k],scale))+abs(b+Q(2*P0[d][1][D+k],scale)))
        centerfree=gamma_bounds[r]-(sum(map(abs,co[0]),Q(0)) if r==0 else 0)
        P_same.append(upq(value+alpha_error*centerfree))
    complete={}
    for name in ('P','V','A'):
        source=P_same if name=='P' else same[name]
        deriv=[alpha_max*x for x in gamma_bounds] if name=='P' else derivatives[name]
        complete[name]=[
            upq(source[0]+deriv[1]*angle_error),
            upq(source[1]+deriv[2]*angle_error+deriv[1]*angle_first),
            upq(source[2]+deriv[3]*angle_error+deriv[2]*(2*angle_first+angle_first**2)+deriv[1]*angle_second)]
    out=dict(schema='6a65-actual-new-gap-final-ramp-accurate-coast-complete-port-difference-v1',
        source=dict(masterSHA256=RAMP_SHA,coastMasterSHA256=COAST_SHA,gramReportSHA256=sha(args.gram_report),
            arcProofSHA256=sha(arcproof),gramCheckerSHA256=sha(gp),integerArithmeticSHA256=sha(hp),entrySHA256=sha(__file__)),
        exactTargetDefinition='a_ellipse of frozen exact dyadic A/B plus dyadic v*ramp/2',
        newTargetRadius=f0.display(),publishedR225RawArc=[str(ARC_LO),str(ARC_HI)],
        sharpenedAccurateRawArc=arc.display(),
        nativeSquaredSpeedResidual=[gram.upper(x) for x in speed_residual],
        qMinimum=str(qmin),
        oldFullPositionFourierDegree=model.degree,newAccurateCurveFourierDegree=95,
        oldLowComparisonCutoff=95,allOldHighFrequenciesRetained=True,
        oldHighFrequencyPortDerivativeBounds={key:[gram.upper(x) for x in val] for key,val in tails.items()},
        TaylorDifferenceOrder=6,integerBits=cert.BITS,
        angularCells=N,selectedCellIndices=selected,
        sameNativeAnglePortDerivativeBounds={'P':[gram.upper(x) for x in P_same],
            **{key:[gram.upper(x) for x in val] for key,val in same.items()}},
        exactArcInverseBounds={key:gram.upper(val) for key,val in dict(
            thetaDifference=angle_error,firstDerivativeMinusOne=angle_first,secondDerivative=angle_second,
            alphaMinusOne=alpha_error,zeroMeanSpeedResidual=speed_zero,
            zeroMeanSpeedResidualDerivative=speed_first).items()},
        actualCentralAngleCompletePortDerivativeBounds={key:[gram.upper(x) for x in val] for key,val in complete.items()},
        actualCoastPortGlobalNativeDerivativeBounds={key:[gram.upper(x) for x in val] for key,val in derivatives.items()},
        allContinuousPortRowsSHA256=rows_hash.hexdigest(),
        newTargetWholeCoastBounds={key:val.display() for key,val in coast_bounds.items()},
        fullAngularDomainCertified=selected==list(range(N)),
        completePortBoundsApplyOnlyWhenFullAngularDomainTrue=True,
        originalR224TargetBoxSilentlyReused=False,
        finalHermiteCellCertified=False,normalizedLastCellCertified=False,
        wholeRampCertified=False,exactIsometryClaimed=False,wholeClosedReachCertified=False,
        seconds=time.monotonic()-start,OSExitCode=None,externalExitReceiptRequired=True)
    args.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual-continuous-complete-port-result',reportSHA256=sha(args.output),
        fullAngularDomainCertified=out['fullAngularDomainCertified'],
        portBounds=out['actualCentralAngleCompletePortDerivativeBounds'],
        arcInverse=out['exactArcInverseBounds'],seconds=out['seconds'])),flush=True)


if __name__=='__main__':
    main()

