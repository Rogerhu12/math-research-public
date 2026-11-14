#!/usr/bin/env python3
"""Independent Cartesian-basis algebra for the conditional flat endpoint.

The author uses an orthonormal frame and general symbolic functions. This
checker starts with the nonorthonormal Cartesian derivative basis
(F_r,F_theta,n) and independent jet symbols. It performs no ODE/PDE solve.
The analytic, uniqueness, limiting and all-pair proofs require full reading.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s

TOPIC=Path(__file__).resolve().parents[1]


def ident(path):
    path=Path(path).resolve();raw=path.read_bytes()
    return {'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publication',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();assert not args.out.exists();files={}
    def bind(path):
        row=ident(path);assert files.get(row['path'],row)==row;files[row['path']]=row;return row
    publication=json.loads(args.publication.read_text());bind(args.publication)
    for row in publication['files']:
        path=Path(row['path']);path=path if path.is_absolute() else TOPIC/path
        actual=bind(path);assert actual['bytes']==row['bytes'] and actual['sha256']==row['sha256']
        if '-sources' in path.stem and path.suffix=='.json':
            for source in json.loads(path.read_text())['files']:
                src=Path(source['path']);src=src if src.is_absolute() else TOPIC/src
                seen=bind(src);assert seen['bytes']==source['bytes'] and seen['sha256']==source['sha256']
    r,E=s.symbols('r E',positive=True)
    Ep,A,B,C,Ar,At,Br,Bt,Cr,Ct=s.symbols('Ep A B C Ar At Br Bt Cr Ct',real=True)
    def dr(x):
        return s.diff(x,r)+s.diff(x,E)*Ep+s.diff(x,A)*Ar+s.diff(x,B)*Br+s.diff(x,C)*Cr
    def dt(x):
        return s.diff(x,A)*At+s.diff(x,B)*Bt+s.diff(x,C)*Ct
    checks=[]
    def zero(name,value):
        assert s.cancel(s.expand(value))==0,name;checks.append(name)
    # Columns are the derivatives of (F_r,F_theta,n) in the same basis.
    P=s.Matrix([[Ep/(2*E),0,-A/E],[0,1/r,-B/r**2],[A,B,0]])
    T=s.Matrix([[0,-r/E,-B/E],[1/r,0,-C/r**2],[B,C,0]])
    metric=s.diag(E,r**2,1)
    mr=metric.applyfunc(dr)-P.T*metric-metric*P
    mt=metric.applyfunc(dt)-T.T*metric-metric*T
    for i in range(3):
        for j in range(3):
            zero('Cartesian_metric_r_'+str(i)+str(j),mr[i,j])
            zero('Cartesian_metric_theta_'+str(i)+str(j),mt[i,j])
    curvature=P.applyfunc(dt)-T.applyfunc(dr)+T*P-P*T
    gauss=A*C-B**2-r*Ep/(2*E)
    cod1=Br-At-(Ep/(2*E)-1/r)*B
    cod2=Cr-Bt-C/r-r*A/E
    zero('Cartesian_integrability_Gauss',curvature[0,1]-gauss/E)
    zero('Cartesian_integrability_first_Codazzi',curvature[2,0]+cod1)
    zero('Cartesian_integrability_second_Codazzi',curvature[2,1]+cod2)
    imposed={Ep:2*E*(A*C-B**2)/r,Br:At+((A*C-B**2)/r-1/r)*B,Cr:Bt+C/r+r*A/E}
    for i in range(3):
        for j in range(3):zero('all_Cartesian_compatibility_'+str(i)+str(j),curvature[i,j].subs(imposed,simultaneous=True))
    # Independent change of basis: Q=(F_r,F_theta,n) diag(-1/sqrt(E),1/r,1).
    change=s.diag(-1/s.sqrt(E),1/r,1)
    U=change.inv()*(P*change+change.applyfunc(dr))
    V=change.inv()*T*change
    wantedU=s.Matrix([[0,0,A/s.sqrt(E)],[0,0,-B/r],[-A/s.sqrt(E),B/r,0]])
    wantedV=s.Matrix([[0,1/s.sqrt(E),B/s.sqrt(E)],[-1/s.sqrt(E),0,-C/r],[-B/s.sqrt(E),C/r,0]])
    for i in range(3):
        for j in range(3):
            zero('inward_orthonormal_U_'+str(i)+str(j),U[i,j]-wantedU[i,j])
            zero('inward_orthonormal_V_'+str(i)+str(j),V[i,j]-wantedV[i,j])
    zero('position_mixed_derivative_commutes',s.Matrix(P[:,1]-T[:,0]).dot(P[:,1]-T[:,0]))
    # Exact C3 orientation: on a horizontal plane R(-omega)-R(omega) has
    # squared norm three on every unit vector when omega=2pi/3.
    ux,uy=s.symbols('ux uy',real=True)
    c=-s.Rational(1,2);t=s.sqrt(3)/2
    R=s.Matrix([[c,-t],[t,c]])
    reverse=(R.T-R)*s.Matrix([ux,uy])
    zero('opposite_winding_C3_norm',reverse.dot(reverse)-3*(ux**2+uy**2))
    # The weighted sufficient-class estimate follows directly by division
    # by k*r*w/sqrt(E), including the absolute value of w_r.
    k,w,z,bb=s.symbols('k w abs_wr b_squared',positive=True)
    bound=(bb+r*w*z/E)/(k*r*w/s.sqrt(E))
    zero('weighted_A_bound',bound-(s.sqrt(E)*bb/(k*r*w)+z/(k*s.sqrt(E))))
    for row in files.values():assert ident(row['path'])==row
    report={'status':'PASS_INDEPENDENT_CARTESIAN_FLAT_ENDPOINT_ALGEBRA','scope':__doc__,
            'script':ident(Path(__file__)),'sympy_version':s.__version__,
            'sources':sorted(files.values(),key=lambda row:row['path']),
            'identity_count':len(checks),'identities':checks,
            'analytic_proofs_checked_separately':True,'candidate_reads':0,
            'ODE_PDE_BVP_DN_RK_or_geometry_backend_calls':0,
            'nonrotational_solution_or_closed_surface_constructed':False}
    raw=(json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode();assert len(raw)<100000
    with args.out.open('xb') as f:f.write(raw)
    print(json.dumps({'status':report['status'],'identity_count':len(checks),'sources':len(files),
                      'solver_calls':0,'report':ident(args.out)}))


if __name__=='__main__':main()
