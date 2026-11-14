#!/usr/bin/env python3
"""Exact symbolic moving-frame identities with all three residual sources.

The scalar metric identity is beta'=beta gamma'/gamma-a^2 gamma^2 K.
No equation is imposed on Ru, Rv, or their mean R0. The output records exact
rational simplifications, not floating samples or a PDE existence claim.
"""
import argparse,hashlib,json
from pathlib import Path
import sympy as s

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,required=True);a0=ap.parse_args()
    if a0.out.exists():raise FileExistsError('preserve the original exact identity record')
    a,b,g,K,m,u,v,d,Sbar,up,vp,gp,Ru,Rv,R0=s.symbols('a beta gamma K m u v d Sbar up vp gamma_r Ru Rv R0')
    S=u*u+K*v*v;dp=-b*(S-Sbar)
    ur=d*up+g*m*K*vp-b*u*(1+S)+Ru
    vr=d*vp-g*m*up+b*v*(1-S)+Rv
    mr=b*m*(1-Sbar)+R0;br=b*gp/g-a*a*g*g*K
    tau=d*v/m-g*u
    p=b*tau/g;q=a*(g*K*v+d*u/m);t=a*d/m
    A=b*v/(g*m);B=a*u/m;C=a/m
    def skew(x,y,z):return s.Matrix([[0,-x,-y],[x,0,-z],[y,z,0]])
    Ar=skew(p,q,t);Ap=skew(A,B,C)
    def dr(z):return s.diff(z,a)*a*b+s.diff(z,b)*br+s.diff(z,g)*gp+s.diff(z,u)*ur+s.diff(z,v)*vr+s.diff(z,m)*mr
    def dphi(z):return s.diff(z,u)*up+s.diff(z,v)*vp+s.diff(z,d)*dp
    curvature=Ap.applyfunc(dr)-Ar.applyfunc(dphi)+Ar*Ap-Ap*Ar
    expected=skew(b*(Rv-v*R0/m)/(g*m),a*(Ru-u*R0/m)/m,-a*R0/(m*m))
    fr=s.Matrix([a*g,a*tau,0]);fp=s.Matrix([0,a*v/m,0])
    torsion=Ar*fp+fp.applyfunc(dr)-Ap*fr-fr.applyfunc(dphi)
    expected_torsion=s.Matrix([0,a*(Rv-v*R0/m)/m,0])
    I=s.Matrix([[fr.dot(fr),fr.dot(fp)],[fr.dot(fp),fp.dot(fp)]])
    II=a*a*v*s.Matrix([[g*g*K+d*d/(m*m),d/(m*m)],[d/(m*m),1/(m*m)]])
    identities={
      'all_nine_frame_curvature_entries':all(s.cancel(x)==0 for x in curvature-expected),
      'all_three_position_torsion_entries':all(s.cancel(x)==0 for x in torsion-expected_torsion),
      'radial_normal_connection_cancels_inverse_v':s.cancel(g*(K*v+u*u/v)+tau*u/v-(g*K*v+d*u/m))==0,
      'mixed_normal_connection_cancels_inverse_v':s.cancel(g*u/v+tau/v-d/m)==0,
      'first_form_determinant':s.cancel(I.det()-a**4*g*g*v*v/(m*m))==0,
      'second_form_determinant_ratio':s.cancel(II.det()/I.det()-K)==0,
      'physical_shape_trace':s.cancel(s.trace(I.inv()*II)-(K*v+(1+u*u)/v))==0,
      'complete_mean_source_not_set_to_zero':R0 in set.union(*(x.free_symbols for x in expected)),
      'both_full_residual_sources_retained':Ru in set.union(*(x.free_symbols for x in expected)) and Rv in set.union(*(x.free_symbols for x in expected)),
    }
    doc=dict(kind='exact_complete_moving_frame_curvature_and_position_torsion',complete=all(identities.values()),
      gates=identities,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),sympy_version=s.__version__,
      exact_arithmetic='rational-function cancellation over Q[a,beta,gamma,K,m,u,v,d,Sbar,up,vp,gamma_r,Ru,Rv,R0]',
      assumptions=['a>0','gamma>0','m<0','v<0','beta_r=beta*gamma_r/gamma-a^2*gamma^2*K','d_phi=-beta*(u^2+K*v^2-Sbar)','Sbar=mean_phi(u^2+K*v^2)','R0=mean_phi(Rv)'],
      denominator_cancellation_does_not_remove_physical_curvature_gap=True,
      all_ordinary_residual_sources_and_mean_retained=True,infinite_dimensional_inverse_proved=False,
      nonlinear_PDE_solution_proved=False,closed_surface_proved=False)
    a0.out.write_text(json.dumps(doc,indent=2)+'\n');print(json.dumps(doc,indent=2))
    if not doc['complete']:raise RuntimeError('an exact moving frame identity failed')

if __name__=='__main__':main()
