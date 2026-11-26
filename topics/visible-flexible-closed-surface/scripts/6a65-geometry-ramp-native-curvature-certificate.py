#!/usr/bin/env python3
"""Whole-domain own curvature of the same raw first-15-cell ramp field.

Consumes R227's independently proved tight Gram intervals. Cartesian first
and second jets use exact Fourier coefficients, local angular Taylor boxes,
radial Bernstein hulls and every weighted high-frequency coefficient.
All decisions use the existing 96-bit directed integer interval arithmetic.
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


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class WholeDomain:
    def __init__(self,gram,cert,model,report,cutoff):
        self.gram,self.cert,self.model,self.report=gram,cert,model,report
        self.I=cert.I
        self.pi=cert.pi_interval()
        self.cutoff=cutoff
        self.trig={}
        arc=tuple(Q(q) for q in report['exactEllipticArcRadiusInterval'])
        self.a0box=(min(arc[0],model.a0),max(arc[1],model.a0))
        self.qlo=model.v*model.ramp/self.a0box[1]
        self.qhi=model.v*model.ramp/self.a0box[0]

    def phase(self,index,count):
        residue=index%(2*count)
        key=(residue,count)
        if key not in self.trig:
            numerator=residue if residue<=count else residue-2*count
            self.trig[key]=self.cert.sincos(self.pi*Q(numerator,count))
        return self.trig[key]


class Cell:
    def __init__(self,whole,index):
        self.w,self.index=whole,index
        self.I=whole.I
        self.g,self.cert,self.model=whole.gram,whole.cert,whole.model
        C,bits,L,sx0=self.g.ActualRamp.cell(self.model,index)
        self.C,self.bits,self.L,self.sx0=C,bits,L,sx0
        self.scale=1 << bits
        self.row=whole.report['rows'][index]
        if self.row['index']!=index:
            raise ValueError('Complete ordered R227 rows required')
        self.epsE=Q(self.row['completeRawNativeGramBounds']['Eminus1']['rational'])
        self.epsF=Q(self.row['completeRawNativeGramBounds']['F']['rational'])
        self.epsG=Q(self.row['completeRawNativeGramBounds']['GminusTarget'][0]['rational'])
        D=self.model.degree
        self.high=list(range(D-whole.cutoff))+list(range(D+whole.cutoff+1,2*D+1))
        self.terms=[]
        self.remainders=[]
        for j in range(6):
            pterms=[]
            prem=[]
            for order in range(4):
                dterms=[]
                dremainders=[]
                for d in range(3):
                    terms=[]
                    for k in range(1,whole.cutoff+1):
                        a=2*C[j][d][0][D+k]*k**order
                        b=-2*C[j][d][1][D+k]*k**order
                        if order%4==1:a,b=b,-a
                        elif order%4==2:a,b=-a,-b
                        elif order%4==3:a,b=-b,a
                        if a or b:
                            terms.append((k,self.I(Q(a,self.scale)),self.I(Q(b,self.scale))))
                    dterms.append(terms)
                    remainder=sum(2*k**(order+2)*(abs(C[j][d][0][D+k])+abs(C[j][d][1][D+k]))
                                  for k in range(1,whole.cutoff+1))
                    dremainders.append(self.I(Q(remainder,self.scale)))
                pterms.append(dterms)
                prem.append(dremainders)
            self.terms.append(pterms)
            self.remainders.append(prem)
        U=self.g.angular(C,D)
        UU=self.g.angular(U,D)
        self.tail={
            (1,0):self.g.vector_bernstein_l1(C,bits,L,1,self.high),
            (0,1):self.g.vector_bernstein_l1(U,bits,L,0,self.high),
            (2,0):self.g.vector_bernstein_l1(C,bits,L,2,self.high),
            (1,1):self.g.vector_bernstein_l1(U,bits,L,1,self.high),
            (0,2):self.g.vector_bernstein_l1(UU,bits,L,0,self.high),
        }
        self.full_bounds=dict(
            X=self.g.vector_bernstein_l1(C,bits,L),
            Xs=self.g.vector_bernstein_l1(C,bits,L,1),
            Xss=self.g.vector_bernstein_l1(C,bits,L,2),
            Xtheta=self.g.vector_bernstein_l1(U,bits,L),
            Xstheta=self.g.vector_bernstein_l1(U,bits,L,1),
            Xthetatheta=self.g.vector_bernstein_l1(UU,bits,L),
        )
        self.angle_cache={}
        self.weight_cache={}
        self.ratio_cache={}

    def angle_boxes(self,index,count):
        key=(index,count)
        if key in self.angle_cache:
            return self.angle_cache[key]
        delta=self.w.pi/count
        boxes=[]
        for j in range(6):
            points=[]
            for order in range(4):
                values=[]
                for d in range(3):
                    value=self.I(Q(self.C[j][d][0][self.model.degree],self.scale)) if order==0 else self.I(0)
                    for k,a,b in self.terms[j][order][d]:
                        sn,cs=self.w.phase(k*(2*index+1),count)
                        value+=a*cs+b*sn
                    values.append(value)
                points.append(values)
            row=[]
            for order in range(3):
                out=[]
                for d in range(3):
                    slope=points[order+1][d].absupper()
                    error=self.cert.upper_i(delta*self.I.raw(slope,slope)
                        +delta.square()*self.remainders[j][order][d]/2)
                    out.append(points[order][d]+self.I.raw(-error.hi,error.hi))
                row.append(out)
            boxes.append(row)
        self.angle_cache[key]=boxes
        return boxes

    def weights(self,lo,hi,order):
        key=(lo,hi,order)
        if key in self.weight_cache:
            return self.weight_cache[key]
        degree=5-order
        span=hi-lo
        rows=[]
        for i in range(degree+1):
            row=[]
            for j in range(order,6):
                value=sum(Q(math.comb(j-order,m)*math.comb(i,m),math.comb(degree,m))
                    *lo**(j-order-m)*span**m for m in range(min(i,j-order)+1))
                value*=Q(math.factorial(j),math.factorial(j-order))/self.L**order
                row.append(self.I(value))
            rows.append(row)
        self.weight_cache[key]=rows
        return rows

    def jets(self,index,count,lo,hi):
        angle=self.angle_boxes(index,count)
        result={}
        for r,q,name in ((1,0,'S'),(0,1,'U'),(2,0,'SS'),(1,1,'SU'),(0,2,'UU')):
            weights=self.weights(lo,hi,r)
            values=[]
            for d in range(3):
                controls=[]
                for weight in weights:
                    controls.append(sum((weight[j-r]*angle[j][q][d] for j in range(r,6)),self.I(0)))
                box=self.I.raw(min(z.lo for z in controls),max(z.hi for z in controls))
                values.append(box+self.I(-self.tail[(r,q)],self.tail[(r,q)]))
            result[name]=values
        return result

    def ratio(self,lo,hi):
        key=(lo,hi)
        if key not in self.ratio_cache:
            def J(t):
                return sum((v*t**p for p,v in self.g.JCOEFF.items()),Q(0))
            left=(self.sx0+lo*self.L)/self.model.ramp
            right=(self.sx0+hi*self.L)/self.model.ramp
            if not 0<=left<=right<=1:
                raise ValueError('Actual radial interval outside the certified ramp')
            self.ratio_cache[key]=self.I(1+self.w.qlo*J(left),1+self.w.qhi*J(right))
        return self.ratio_cache[key]

    def geometry(self,index,count,lo,hi):
        q=self.jets(index,count,lo,hi)
        E=self.I(1-self.epsE,1+self.epsE)
        F=self.I(-self.epsF,self.epsF)
        sin2,cos2=self.w.phase(2*(2*index+1),count)
        width=2*self.w.pi/count
        absolute=sin2.absupper()
        error=self.cert.upper_i(width*self.I.raw(absolute,absolute)+width.square()/2)
        cs=cos2+self.I.raw(-error.hi,error.hi)
        ell=(self.model.A**2+self.model.B**2)/2+self.I((self.model.B**2-self.model.A**2)/2)*cs
        global_lower=self.I(self.model.B**2)
        global_upper=self.I(self.model.A**2)
        ell=self.I.raw(max(ell.lo,global_lower.lo),min(ell.hi,global_upper.hi))
        G=self.ratio(lo,hi).square()*ell+self.I(-self.epsG,self.epsG)
        D=E*G-F.square()
        if D.lo<=0:
            raise ArithmeticError('No positive local Gram determinant')
        rootD=D.sqrt()
        normal=self.cert.scale(1/rootD,self.cert.cross(q['S'],q['U']))
        L,M,N=(self.cert.dot(normal,q[name]) for name in ('SS','SU','UU'))
        a=L/E
        b=(M-F*a)/rootD
        d=(E*N-2*F*M+F.square()*a)/D
        trace=a+d
        tr=trace.absupper()
        kappa=(self.I.raw(tr,tr)+((a-d).square()+4*b.square()).sqrt())/2
        return dict(curvature=self.cert.upper_i(kappa),area=rootD,E=E,F=F,G=G,
                    shape00=a,shape01=b,shape11=d)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--master',type=Path,required=True)
    ap.add_argument('--gram-report',type=Path,required=True)
    ap.add_argument('--scripts-dir',type=Path,required=True)
    ap.add_argument('--gram-checker',type=Path,default=Path(__file__).with_name('6a65-geometry-ramp-native-gram-certificate.py'))
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--cell',type=int,action='append')
    ap.add_argument('--angular-cells',type=int,default=64)
    ap.add_argument('--max-depth',type=int,default=8)
    ap.add_argument('--curvature-cap',default='10')
    args=ap.parse_args()
    if args.output.exists():
        raise FileExistsError('Fresh actual curvature certificate required')
    if args.angular_cells<16 or args.angular_cells>1024 or not 0<=args.max_depth<=12:
        raise ValueError('Bounded explicit angular/subdivision domain required')
    start=time.monotonic()
    gram=load('actual_ramp_integer_Gram_source',args.gram_checker)
    cert_path=args.scripts_dir/'6a65-m12-r137-continuous-domain.py'
    cert=load('actual_ramp_integer_geometry',cert_path)
    report=json.loads(args.gram_report.read_text())
    if (report.get('allFirst15PolynomialCellsProved') is not True
        or report['source']['masterSHA256']!=sha(args.master)
        or report['source']['entrySHA256']!=sha(args.gram_checker)):
        raise ValueError('Actual R227 full Gram proof and same master required')
    model=gram.ActualRamp(args.master)
    whole=WholeDomain(gram,cert,model,report,report['lowFourierCutoff'])
    cap=cert.I(Q(args.curvature_cap))
    selected=list(range(15)) if args.cell is None else args.cell
    if not selected or len(set(selected))!=len(selected) or any(j<0 or j>=15 for j in selected):
        raise ValueError('Distinct polynomial cells 0..14 required')
    rows=[]
    total=0
    global_bound=cert.I(0)
    for j in selected:
        cell=Cell(whole,j)
        leaf=0
        splits=0
        depth_used=0
        bound=cert.I(0)
        lower=None
        worst=None
        proof_hash=hashlib.sha256()
        def consume(index,count,lo,hi,depth):
            nonlocal leaf,splits,depth_used,bound,lower,worst
            try:
                data=cell.geometry(index,count,lo,hi)
                if data['curvature'].hi>=cap.lo:
                    raise ArithmeticError('Current box is too broad for the actual own-curvature cap')
            except ArithmeticError as exc:
                if depth>=args.max_depth:
                    raise ArithmeticError(f'Actual cell {j}; theta {index}/{count}; radial [{lo},{hi}]: {exc}') from exc
                splits+=1
                if depth%2==0:
                    consume(2*index,2*count,lo,hi,depth+1)
                    consume(2*index+1,2*count,lo,hi,depth+1)
                else:
                    mid=(lo+hi)/2
                    consume(index,count,lo,mid,depth+1)
                    consume(index,count,mid,hi,depth+1)
                return
            if data['curvature'].hi>bound.hi:
                bound=data['curvature']
                worst=dict(angularIndex=index,angularSubdivisions=count,radialLo=str(lo),radialHi=str(hi))
            lower=data['area'] if lower is None else cert.I.raw(min(lower.lo,data['area'].lo),min(lower.lo,data['area'].lo))
            proof_hash.update((json.dumps(dict(angularIndex=index,angularSubdivisions=count,
                radialLo=str(lo),radialHi=str(hi),bounds={key:[value.lo,value.hi] for key,value in data.items()}),sort_keys=True)+'\n').encode())
            leaf+=1
            depth_used=max(depth_used,depth)
        for k in range(args.angular_cells):
            consume(k,args.angular_cells,Q(0),Q(1),0)
        total+=leaf
        global_bound=cert.max_upper(global_bound,bound)
        row=dict(index=j,curvatureUpper=bound.display(),areaLower=cert.lower_i(lower).display(),
            provedLeaves=leaf,binarySplits=splits,maximumDepth=depth_used,worstCertifiedBox=worst,
            allIntegerLeafRowsSHA256=proof_hash.hexdigest(),
            exactWholeCellCartesianNormBounds={key:gram.upper(value) for key,value in cell.full_bounds.items()},
            exactWeightedHighFrequencyTwoJetBounds={str(key):gram.upper(value) for key,value in cell.tail.items()})
        rows.append(row)
        print(json.dumps(dict(event='actual-whole-ramp-curvature-cell',index=j,
            curvatureUpper=bound.display(),leaves=leaf,splits=splits,seconds=time.monotonic()-start)),flush=True)
    out=dict(schema='6a65-actual-coupled-gap-first15-raw-native-ramp-whole-curvature-v1',
        source=dict(masterSHA256=sha(args.master),gramReportSHA256=sha(args.gram_report),
            gramSourceSHA256=sha(args.gram_checker),integerArithmeticSHA256=sha(cert_path),entrySHA256=sha(__file__)),
        lowFourierCutoff=whole.cutoff,allSavedHighFrequenciesRetained=True,
        initialAngularCells=args.angular_cells,maximumAllowedDepth=args.max_depth,
        curvatureCap=args.curvature_cap,certifiedCellIndices=selected,
        allFirst15PolynomialCellsProved=selected==list(range(15)),
        ownCurvatureUpper=global_bound.display(),provedLeaves=total,rows=rows,
        method='Exact Fourier coefficients; local angular second-order Taylor boxes; radial Bernstein hulls; R227 tight actual Gram; genuine Cartesian unit normal and orthonormal shape spectrum',
        rawNativeFieldOnly=True,lastExactCoastRepairCellExcluded=True,
        normalizedFieldCertified=False,ODEErrorCertified=False,wholeRampCertified=False,
        wholeClosedReachCertified=False,seconds=time.monotonic()-start,
        OSExitCode=None,externalExitReceiptRequired=True)
    args.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual-whole-ramp-curvature-complete',reportSHA256=sha(args.output),
        ownCurvatureUpper=global_bound.display(),provedLeaves=total,seconds=out['seconds'])),flush=True)


if __name__=='__main__':
    main()
