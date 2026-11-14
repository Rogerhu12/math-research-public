#!/usr/bin/env python3
"""Strict metric bound of the saved actual R137 ruled Cartesian surface.

Finite Laurent products are convolved in Acb before cancellation is bounded.
The exact balanced material derivative h is enclosed by its certified first
512 Fourier means and an analytic infinite remainder.  No numerical fit or
new PDE solution is introduced.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from pathlib import Path
import numpy as np
import flint
from flint import arb,acb,acb_poly,ctx
from fd2d_k0_ruling_angular_certificate import moment,bounds


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)
def magnitude_upper(x):return max(abs(x.lower()),abs(x.upper())).upper()
def from_bounds(row):
    def part(k):
        m,e=row[k];return arb((int(m),int(e)))
    return part('lower_binary').union(part('upper_binary'))


class Laurent:
    def __init__(self,coefficients=(0,),offset=0):
        self.poly=coefficients if isinstance(coefficients,acb_poly) else acb_poly(coefficients)
        self.offset=int(offset)
    @staticmethod
    def scalar(x):return Laurent([acb(x)])
    def aligned(self,offset):
        return acb_poly([acb(0)]*(self.offset-offset)+[self.poly[j] for j in range(len(self.poly))])
    def __add__(self,other):
        if not isinstance(other,Laurent):other=Laurent.scalar(other)
        offset=min(self.offset,other.offset)
        return Laurent(self.aligned(offset)+other.aligned(offset),offset)
    __radd__=__add__
    def __neg__(self):return Laurent(-self.poly,self.offset)
    def __sub__(self,other):return self+-other if isinstance(other,Laurent) else self+(-other)
    def __rsub__(self,other):return -self+other
    def __mul__(self,other):
        if isinstance(other,Laurent):return Laurent(self.poly*other.poly,self.offset+other.offset)
        return Laurent(self.poly*acb(other),self.offset)
    __rmul__=__mul__
    def derivative(self):
        return Laurent([self.poly[j]*acb(0,j+self.offset) for j in range(len(self.poly))],self.offset)
    def norm_upper(self):
        # Rectangle modulus bound avoids any convention about complex
        # absolute-value intervals while remaining valid coefficientwise.
        total=arb(0)
        for j in range(len(self.poly)):
            c=self.poly[j];total+=magnitude_upper(c.real)+magnitude_upper(c.imag)
        return total.upper()
    @staticmethod
    def coefficients(mapping):
        lo,hi=min(mapping),max(mapping)
        return Laurent([mapping.get(j,acb(0)) for j in range(lo,hi+1)],lo)


def dot(a,b):return sum((x*y for x,y in zip(a,b)),Laurent.scalar(0))
def vector_norm_upper(values):return sum((x*x for x in values),arb(0)).sqrt().upper()


def main():
    root=Path(__file__).resolve().parent.parent
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    ap.add_argument('--moments',type=Path,default=root/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json')
    ap.add_argument('--means',type=Path,default=root/'notes/2026-11-12-fd2d-balanced-weighted-means-512-02.json.gz')
    ap.add_argument('--ruling-certificate',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-angular-certificate-01.json')
    ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--metric-target',default='1e-6')
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();ctx.prec=args.precision
    saved=np.load(args.inlet,allow_pickle=False);mom=load(args.moments);means=load(args.means);ruling=load(args.ruling_certificate)
    if ruling['inlet_sha256']!=digest(args.inlet) or ruling['moments_sha256']!=digest(args.moments):raise ValueError('Ruling input mismatch')
    if means['exact_moment_report']['sha256']!=digest(args.moments) or not means['source_moment_intervals_remain_valid']:raise ValueError('Mean interval definition mismatch')
    if not ruling['passed'] or ruling['unresolved']:raise ValueError('Complete positive ruling map not certified')
    if [row['angular_mode'] for row in means['rows']]!=list(range(2,1025,2)):raise ValueError('Expected the complete 512 mean packet')
    a=from_bounds(ruling['a']);v=from_bounds(ruling['v']);length=from_bounds(ruling['coast_length'])
    a0=moment(mom['enclosures']['a0'])
    raw=saved['frame_fourier'][:,:9];nyquist=len(raw)-1;fields=[]
    for q in range(9):
        cs={0:acb(arb(float(raw[0,q].real)))}
        for j in range(1,nyquist):
            re,im=arb(float(raw[j,q].real)),arb(float(raw[j,q].imag))
            cs[j]=acb(re,im);cs[-j]=acb(re,-im)
        edge=arb(float(raw[-1,q].real))/2
        cs[nyquist]=acb(edge);cs[-nyquist]=acb(edge)
        fields.append(Laurent.coefficients(cs))
    X,e1,e2=fields[:3],fields[3:6],fields[6:9]
    Xp=[f.derivative() for f in X];e1p=[f.derivative() for f in e1];e2p=[f.derivative() for f in e2]
    ncs={0:acb(arb(float(saved['n_phi_cos'][0])))};mcs={0:acb(0)}
    for freq,c in zip(saved['frequencies'][1:],saved['n_phi_cos'][1:]):
        ncs[int(freq)]=acb(arb(float(c))/2);ncs[-int(freq)]=acb(arb(float(c))/2)
    for freq,c in zip(saved['frequencies'][1:],saved['m_phi_sin']):
        mcs[int(freq)]=acb(0,-arb(float(c))/2);mcs[-int(freq)]=acb(0,arb(float(c))/2)
    n,m=Laurent.coefficients(ncs),Laurent.coefficients(mcs)
    hcs={0:acb(1)}
    for row in means['rows']:
        mu=moment(row['material_weighted_mean']);f=int(row['angular_mode'])
        hcs[f]=acb(mu);hcs[-f]=acb(mu)
    h=Laurent.coefficients(hcs)
    par=mom['parameters'];strip_magnitude=(arb(par['r'])+arb(par['D']))/a0
    decay=(-arb(1)/10).exp()
    htail=(2*strip_magnitude*(-arb(513)/10).exp()/(1-decay)).upper()
    e=[e1,e2];gram=[[dot(ei,ej) for ej in e] for ei in e]
    H=[[gram[i][j]-(1 if i==j else 0) for j in range(2)] for i in range(2)]
    Hbound=[[p.norm_upper() for p in row] for row in H]
    Hop=(max(Hbound[0][0],Hbound[1][1])+Hbound[0][1]).upper()
    C=[Xp[j]-a*h*e2[j] for j in range(3)]
    B=[n*e1p[j]-m*e2p[j]-v*h*(m*e1[j]+n*e2[j]) for j in range(3)]
    nmax,mmax=n.norm_upper(),m.norm_upper()
    e1max=[x.norm_upper() for x in e1];e2max=[x.norm_upper() for x in e2]
    Cbounds=[(C[j].norm_upper()+magnitude_upper(a)*htail*e2max[j]).upper() for j in range(3)]
    Bbounds=[(B[j].norm_upper()+magnitude_upper(v)*htail*(mmax*e1max[j]+nmax*e2max[j])).upper() for j in range(3)]
    TC=[dot(ei,C) for ei in e];TB=[dot(ei,B) for ei in e]
    gram_abs=[[(Hbound[i][j]+(1 if i==j else 0)).upper() for j in range(2)] for i in range(2)]
    TCbounds=[(TC[i].norm_upper()+magnitude_upper(a)*htail*gram_abs[i][1]).upper() for i in range(2)]
    TBbounds=[(TB[i].norm_upper()+magnitude_upper(v)*htail*(mmax*gram_abs[i][0]+nmax*gram_abs[i][1])).upper() for i in range(2)]
    Cnorm,Bnorm=vector_norm_upper(Cbounds),vector_norm_upper(Bbounds)
    TCnorm,TBnorm=vector_norm_upper(TCbounds),vector_norm_upper(TBbounds)
    rows=[];target=arb(args.metric_target);global_bound=arb(0);worst=None
    for j,row in enumerate(ruling['boxes']):
        nlo=from_bounds(row['n']).lower();rholo=from_bounds(row['rho']).lower()
        Dlo=min(a.lower(),from_bounds(row['D_end']).lower())
        kaphi=from_bounds(row['kappa_entry']).upper();hlo=(rholo/a0.upper()).lower()
        if not (nlo>0 and hlo>0 and Dlo>0):raise ValueError('Missing positive scalar bound')
        beta=((kaphi/nlo).sqrt()/(hlo*Dlo)).upper()
        radial_factor=(length.upper()/nlo).upper()
        qbound=(TCnorm+radial_factor*TBnorm).upper();dbound=(Cnorm+radial_factor*Bnorm).upper()
        U=(Hop+2*beta*qbound+beta*beta*dbound*dbound).upper()
        if U>global_bound:global_bound=U;worst=j
        rows.append(dict(quarter_angle_left=row['left_pi_over_two'],quarter_angle_right=row['right_pi_over_two'],
            n_lower=bounds(nlo),h_lower=bounds(hlo),D_lower=bounds(Dlo),covector_beta_upper=bounds(beta),
            full_radial_metric_error_upper=bounds(U)))
    report=dict(schema='fd2d-actual-ruled-whole-metric-convolution-Arb-v1',actual_execution=True,
        source_sha256=digest(__file__),inlet_sha256=digest(args.inlet),moments_sha256=digest(args.moments),means_sha256=digest(args.means),ruling_certificate_sha256=digest(args.ruling_certificate),
        flint_version=flint.__version__,precision_bits=args.precision,finite_material_modes=512,
        h_infinite_tail_upper=bounds(htail),full_Laurent_products_no_frequency_truncation=True,
        frame_Gram_operator_error_upper=bounds(Hop),C_component_upper=list(map(bounds,Cbounds)),B_component_upper=list(map(bounds,Bbounds)),
        tangent_C_components_upper=list(map(bounds,TCbounds)),tangent_B_components_upper=list(map(bounds,TBbounds)),
        C_vector_upper=bounds(Cnorm),B_vector_upper=bounds(Bnorm),tangent_C_vector_upper=bounds(TCnorm),tangent_B_vector_upper=bounds(TBnorm),
        radial_parameter_coverage='All 0<=w<=W(phi); W<=L; D bounded at both endpoints using its affine formula',
        angular_coverage='Global Fourier coefficient bounds for actual Cartesian residuals; certified scalar D2 n,m,h,D cover the complete circle',
        target_metric='The exact flat coast metric ds^2+(a+v sigma)^2 du^2 pulled back by the R137 ruling coordinate map',
        exact_frame_or_Gauss_Codazzi_assumed=False,actual_Cartesian_surface=True,
        global_metric_error_upper=bounds(global_bound),worst_scalar_box=worst,metric_target=args.metric_target,
        passed=bool(global_bound<target),boxes=rows,global_embedding_certificate=False,reach_certificate=False,
        strict_bounds_in_binary_fields=True,displays_not_outward_rounded=True,seconds=time.monotonic()-started)
    raw=(json.dumps(report,indent=2,allow_nan=False)+'\n').encode()
    if args.out.suffix=='.gz':args.out.write_bytes(gzip.compress(raw,mtime=0))
    else:
        if len(raw)>1000000:raise ValueError('Data over 1 MB require .gz')
        args.out.write_bytes(raw)
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),passed=report['passed'],metric_upper_display=float(global_bound),Gram_upper_display=float(Hop),tangent_C_upper_display=float(TCnorm),tangent_B_upper_display=float(TBnorm),seconds=report['seconds'])),flush=True)
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
