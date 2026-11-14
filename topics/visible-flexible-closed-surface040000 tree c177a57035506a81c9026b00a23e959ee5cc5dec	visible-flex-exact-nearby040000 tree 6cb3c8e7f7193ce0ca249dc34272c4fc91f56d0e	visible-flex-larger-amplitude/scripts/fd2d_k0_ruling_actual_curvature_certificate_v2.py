#!/usr/bin/env python3
"""Arb curvature certificate of the ACTUAL finite ruled Cartesian surface.

No orthonormal-frame, exact metric, Gauss, or Codazzi identity is assumed.
All true first/second jets come from the saved finite Fourier definition.
Only scalar interval boxes are retained; no angle-pair matrix is formed.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from pathlib import Path
import numpy as np
import flint
from flint import arb,ctx
from fd2d_k0_ruling_angular_certificate import moment,bounds


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dot(a,b):return sum((x*y for x,y in zip(a,b)),arb(0))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def add(a,b):return [x+y for x,y in zip(a,b)]
def mul(c,a):return [c*x for x in a]


def quadratic_range(coefficients,left,right):
    """Enclose a scalar quadratic by its three Bernstein coefficients."""
    p0,p1,p2=coefficients;h=right-left
    b0=p0+p1*left+p2*left**2
    b1=b0+(h/2)*(p1+2*p2*left)
    b2=p0+p1*right+p2*right**2
    return b0.union(b1).union(b2)


class ActualRuledIntervals:
    def __init__(self,inlet,candidate,moments,position_modes):
        p=np.load(inlet,allow_pickle=False);can=json.loads(Path(candidate).read_text())
        if str(p['candidate_sha256'].item())!=digest(candidate):raise ValueError('Candidate binding mismatch')
        mom=json.loads(Path(moments).read_text())
        a0=moment(mom['enclosures']['a0'])
        last=next(q for q in reversed(can['segments']) if q['kind']=='hermite')
        self.a=(a0+arb(float(last['jet1'][0]))).union(arb(float(p['a'])))
        self.v=arb(float(last['jet1'][1])).union(arb(float(p['v'])))
        self.L=arb(float(p['coast_length']));self.rho0=self.a/self.v
        freqs=[int(x) for x in p['frequencies']]
        self.nc={f:arb(float(c)) for f,c in zip(freqs,p['n_phi_cos'])}
        self.mc={f:arb(float(c)) for f,c in zip(freqs[1:],p['m_phi_sin'])}
        raw=p['frame_fourier'][:,:9];nyquist=len(raw)-1
        self.stop=min(position_modes,nyquist);self.cos=[];self.sin=[]
        for j in range(len(raw)):
            weight=1 if j in (0,nyquist) else 2
            self.cos.append([weight*arb(float(x)) for x in raw[j].real])
            self.sin.append([arb(0) if j in (0,nyquist) else -weight*arb(float(x)) for x in raw[j].imag])
        self.tails=[[sum((j**d*(abs(self.cos[j][q])+abs(self.sin[j][q])) for j in range(self.stop+1,len(raw))),arb(0)) for q in range(9)] for d in range(3)]
        self.tail_balls=[[arb(0,tuple(map(int,x.upper().man_exp()))) for x in row] for row in self.tails]
        self.waves=sorted(set(range(1,self.stop+1))|set(freqs[1:]))

    def angle_box(self,left,right,den):
        phi=(2*arb.pi()*left/den).union(2*arb.pi()*right/den)
        fields=[[self.tail_balls[d][q]+(self.cos[0][q] if d==0 else 0) for q in range(9)] for d in range(3)]
        n=[arb(self.nc[0]),arb(0),arb(0)];m=[arb(0),arb(0),arb(0)]
        for f in self.waves:
            sn,cs=(phi*f).sin_cos()
            if f in self.nc:
                cn,cm=self.nc[f],self.mc[f]
                n[0]+=cn*cs;n[1]-=f*cn*sn;n[2]-=f*f*cn*cs
                m[0]+=cm*sn;m[1]+=f*cm*cs;m[2]-=f*f*cm*sn
            if f<=self.stop:
                for q in range(9):
                    cc,ss=self.cos[f][q],self.sin[f][q]
                    base=cc*cs+ss*sn
                    fields[0][q]+=base
                    fields[1][q]+=f*(-cc*sn+ss*cs)
                    fields[2][q]-=f*f*base
        if not n[0]>0:return None
        k=m[0]/n[0]
        kp=m[1]/n[0]-m[0]*n[1]/n[0]**2
        kpp=m[2]/n[0]-m[0]*n[2]/n[0]**2-2*m[1]*n[1]/n[0]**2+2*m[0]*n[1]**2/n[0]**3
        X=[row[:3] for row in fields];e1=[row[3:6] for row in fields];e2=[row[6:9] for row in fields]
        G=add(e1[0],mul(-k,e2[0]))
        Gp=add(add(e1[1],mul(-kp,e2[0])),mul(-k,e2[1]))
        Gpp=add(add(add(e1[2],mul(-kpp,e2[0])),mul(-2*kp,e2[1])),mul(-k,e2[2]))
        C0=cross(G,X[1]);C1=cross(G,Gp)
        W=self.L*(2*self.rho0+self.L)/(self.rho0+(self.rho0**2+(1+k*k)*self.L*(2*self.rho0+self.L)).sqrt())
        E=dot(G,G);fnum=dot(C0,Gp)
        area_coeff=(dot(C0,C0),2*dot(C0,C1),dot(C1,C1))
        numerator_coeff=(E*dot(C0,X[2])-2*dot(G,X[1])*fnum,
            E*(dot(C0,Gpp)+dot(C1,X[2]))-2*dot(G,Gp)*fnum,
            E*dot(C1,Gpp))
        return dict(n=n[0],W=W,X=X,G=G,Gp=Gp,Gpp=Gpp,C0=C0,C1=C1,E=E,fnum=fnum,
            area_coeff=area_coeff,numerator_coeff=numerator_coeff)

    @staticmethod
    def radial_box(data,left,right,den):
        # Include every physical w in this tau strip.  Endpoint widening is
        # outward and allowed: the exact quadratic is defined beyond its
        # narrow actual strip as well.
        wlo=(arb(left)/den*data['W']).lower()
        whi=(arb(right)/den*data['W']).upper()
        area2=quadratic_range(data['area_coeff'],wlo,whi)
        if not area2>0:return None
        numerator=quadratic_range(data['numerator_coeff'],wlo,whi)
        bound=(abs(numerator)+(numerator**2+4*data['fnum']**2*area2).sqrt())/(2*area2*area2.sqrt())
        return dict(area2=area2,curvature_absolute=bound,Gaussian_curvature=-data['fnum']**2/area2**2)


def main():
    root=Path(__file__).resolve().parent.parent
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    ap.add_argument('--candidate',type=Path,default=root/'notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json')
    ap.add_argument('--moments',type=Path,default=root/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json')
    ap.add_argument('--initial-angle-boxes',type=int,default=256)
    ap.add_argument('--radial-boxes',type=int,default=16)
    ap.add_argument('--maximum-angle-depth',type=int,default=8)
    ap.add_argument('--position-modes',type=int,default=96)
    ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--curvature-bound',default='73/10')
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    start=time.monotonic();ctx.prec=args.precision
    definition=ActualRuledIntervals(args.inlet,args.candidate,args.moments,args.position_modes)
    target=arb(args.curvature_bound);records=[];bad=[];calls=0;radial_calls=0
    def visit(left,right,den,depth):
        nonlocal calls,radial_calls
        calls+=1;data=definition.angle_box(left,right,den)
        rows=[];success=data is not None
        if success:
            for r in range(args.radial_boxes):
                radial_calls+=1;value=definition.radial_box(data,r,r+1,args.radial_boxes)
                if value is None or not value['curvature_absolute']<target:
                    success=False;break
                rows.append(value)
        if success:
            envelope={key:rows[0][key] for key in rows[0]}
            for row in rows[1:]:
                for key in envelope:envelope[key]=envelope[key].union(row[key])
            records.append(dict(angle_left_over_2pi=[left,den],angle_right_over_2pi=[right,den],depth=depth,
                n=bounds(data['n']),W=bounds(data['W']),radial_uniform_cells=args.radial_boxes,
                all_radial_cells_verified=True,radial_envelope={key:bounds(x) for key,x in envelope.items()}))
        elif depth<args.maximum_angle_depth:
            visit(2*left,left+right,2*den,depth+1);visit(left+right,2*right,2*den,depth+1)
        else:
            bad.append(dict(angle_left_over_2pi=[left,den],angle_right_over_2pi=[right,den],depth=depth,reason='Strict actual area/curvature enclosure did not close'))
    for j in range(args.initial_angle_boxes):
        visit(j,j+1,args.initial_angle_boxes,0)
        if (j+1)%16==0:
            print(json.dumps(dict(progress=j+1,total_initial=args.initial_angle_boxes,accepted_angles=len(records),unresolved=len(bad),seconds=time.monotonic()-start)),flush=True)
    report=dict(schema='fd2d-actual-finite-ruled-curvature-Arb-v2',actual_execution=True,
        source_sha256=digest(__file__),inlet_sha256=digest(args.inlet),candidate_sha256=digest(args.candidate),moments_sha256=digest(args.moments),
        interval_helper_sha256=digest(Path(__file__).with_name('fd2d_k0_ruling_angular_certificate.py')),
        flint_version=flint.__version__,precision_bits=args.precision,position_modes_explicit=definition.stop,
        all_remaining_modes_included_as_exact_l1_derivative_tails=True,
        derivative_tail_bounds=[[bounds(x) for x in row] for row in definition.tails],a=bounds(definition.a),v=bounds(definition.v),coast_length=bounds(definition.L),
        strict_curvature_claim='max(abs(actual principal curvatures)) < '+args.curvature_bound,
        strict_immersion_claim='actual |F_w cross F_phi|^2 > 0 on the complete parameter cylinder',
        angular_cover='Complete [0,2pi], without symmetry assumption on finite Cartesian coefficients',
        radial_cover='All 0<=w<=W(phi), via tau=w/W(phi) in [0,1]',
        normal_and_metric_from_actual_Cartesian_jets=True,orthonormal_frame_assumed=False,
        exact_Gauss_Codazzi_or_developability_assumed=False,
        metric_certificate=False,global_embedding_certificate=False,full_reach_certificate=False,
        radial_polynomial_dependency_preserved=True,radial_range_method='Exact quadratic Bernstein convex hull',
        bounded_storage='Only three aggregate radial enclosures retained per accepted angle box',
        passed=not bad,accepted_angle_boxes=len(records),accepted_radial_boxes=args.radial_boxes*len(records),
        interval_angle_evaluations=calls,interval_radial_evaluations=radial_calls,unresolved=bad,boxes=records,
        strict_bounds_in_exact_binary_fields=True,numerical_displays_not_outward_rounded=True,seconds=time.monotonic()-start)
    raw=(json.dumps(report,indent=2,allow_nan=False)+'\n').encode()
    if args.out.suffix=='.gz':args.out.write_bytes(gzip.compress(raw,mtime=0))
    else:
        if len(raw)>1000000:raise ValueError('Data over 1 MB must be written to an .json.gz output')
        args.out.write_bytes(raw)
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),bytes=args.out.stat().st_size,uncompressed_bytes=len(raw),passed=report['passed'],angles=report['accepted_angle_boxes'],radial_boxes=report['accepted_radial_boxes'],unresolved=len(bad),seconds=report['seconds'])),flush=True)
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
