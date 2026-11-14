#!/usr/bin/env python3
"""R501 complete lattice phase and CM exchange of the actual four sources."""
from pathlib import Path
import json
import sympy as s

def main():
    D=s.symbols("D");om=(-1+D)/2
    red=lambda z:s.rem(s.Poly(s.expand(z),D),s.Poly(D**2+3,D)).as_expr()
    cj=lambda z:red(z.subs(D,-D))
    mul=lambda x,y,m:((x[0]*y[0]-x[1]*y[1])%m,
                      (x[0]*y[1]+x[1]*y[0]-x[1]*y[1])%m)
    g7=(40,195);g19=(87,144)
    inv7=((g7[0]-g7[1])%272,(-g7[1])%272)
    gD=mul(g19,mul(inv7,inv7,272),272)
    assert gD==(0,239)
    grot=(271,271)  # omega^-1=omega^2=-1-omega
    assert mul(grot,gD,272)==(239,0)  # -33
    assert (239*239)%272==1
    a7=(3,1);abar7=(2,-1);a19=(5,2)
    # Ordinary integer multiplication, without reduction.
    im=lambda x,y:(x[0]*y[0]-x[1]*y[1],
                   x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
    acomp=im(a19,im(abar7,abar7))
    assert acomp==(25,-9)
    assert acomp[0]**2-acomp[0]*acomp[1]+acomp[1]**2==931

    ga=(5+D)/2
    y=[D,2*D,ga,(5-D)/2,1,2]
    w=[D,2*D,ga,(5-D)/2,3*D,4]
    c=37+3*D;r=1-2*om
    dv=[0,0,0,0,1+3*om,1]
    kval=[red(-(10+om)*yi+om*di) for yi,di in zip(y,dv)]
    expected=[(3-19*D)/2,3-19*D,-23-6*D,(7*D-49)/2,
              -(23+3*D)/2,-(39+D)/2]
    assert all(red(x-z)==0 for x,z in zip(kval,expected))
    assert all(red(wi-c*yi-r*wi-4*ki)==0 for wi,yi,ki in zip(w,y,kval))
    normk=sum(red(ki*cj(ki)) for ki in kval)
    herm=red(sum(cj(red(wi*r))*ki for wi,ki in zip(w,kval)))
    E=2*s.expand(herm).coeff(D)
    assert normk==3159 and herm==-788-331*D and E==-662
    assert (2*normk-E/2)%4==1
    assert red(r*cj(r))==7

    pts=[(m,n) for m in range(4) for n in range(4)]
    idx={t:i for i,t in enumerate(pts)}
    norm=lambda t:(t[0]**2-t[0]*t[1]+t[1]**2)%4
    det=lambda t,z:t[0]*z[1]-t[1]*z[0]
    rot=lambda t:((t[0]+2*t[1])%4,(-2*t[0]+3*t[1])%4)
    DD=s.zeros(16);K=s.zeros(16);F=s.diag(*[s.I**((-norm(t))%4) for t in pts])
    at=lambda t:-s.Rational((-1)**norm(t),4)
    for j,t in enumerate(pts):
        assert norm(rot(t))==(3*norm(t))%4 and rot(rot(t))==t
        DD[idx[rot(t)],j]=s.I**norm(t)
        for i,z in enumerate(pts):
            zz=((z[0]+t[0])%4,(z[1]+t[1])%4)
            K[i,j]=at(zz)*s.I**((-det(t,z))%4)
    assert DD**2==s.eye(16)
    e0=s.zeros(16,1);e0[0]=1;e1=K*e0;e2=F**2*e1;q=F*e1;h=e1+e2
    assert DD*e0==e0 and DD*e1==q and DD*q==e1 and DD*e2==h-q
    u=e0+h/2;v=e1-h/2;z=q-h/2
    src=s.Matrix.hstack(u,v,z,h)
    D4=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    K4=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,-1,0],[0,0,0,-1]])
    F4=s.Matrix([[1,0,0,0],[0,0,-1,0],[0,1,0,0],[0,0,0,1]])
    assert DD*src==src*D4
    seen={tuple(s.eye(4))};todo=[s.eye(4)]
    while todo:
        x=todo.pop()
        for G in [D4,K4,F4]:
            qx=G*x
            if tuple(qx) not in seen:seen.add(tuple(qx));todo.append(qx)
    assert len(seen)==96

    # A fixed primitive-CM period anchor for the weighted quarter branch.
    t=s.symbols("t");s3=s.sqrt(3)
    ee=-1-s3
    assert s.simplify(-(ee**3+4)/(3*ee**2)-(-1+s3))==0
    duplication=s.factor(t**4-4*t**3+8*t+4)
    assert duplication==(t*t-2*t-2)**2

    report={
        "whole_g7_mod272":list(g7),"whole_g19_mod272":list(g19),
        "g_D_without_geometric_rotation":list(gD),
        "g_mathscrD_mod272":[239,0],
        "mathscrD_definition":"R_omega,Y * omega^-1 * N19,Y * Nbar7,Y^2",
        "whole_primitive_anchor":"S(2Y), N7=-1, Nbar7=-1, N19=omega, R_omega=1",
        "single_CM_composite":[25,-9],"single_CM_norm":931,
        "raw_first_Y_space":"[2]^*S34; mathscrD restricts to identity on this entire subspace",
        "translation_multiplier_r_in_Zomega":[1,-2],
        "translation_period_vector_k_in_Zomega":[[-8,-19],[-16,-38],[-29,-12],[-21,7],[-13,-3],[-20,-1]],
        "norm_k_sum":3159,
        "sum_conjugate_wr_times_k":"-788-331delta",
        "integer_alternating_sum":-662,
        "complete_lattice_phase":"i^Norm(ell)",
        "whole_source_identity":"mathscrD f_t=i^Norm(4t) f_((1-2omega)t)",
        "source_action_in_u_v_z_h":[list(map(int,D4.row(i))) for i in range(4)],
        "whole_source_group_order":len(seen),
        "complete_new_line_rows":{"v":"+Snew tensor Lambda_old","z":"-Snew tensor Lambda_old"},
        "complete_reference_rows":{"v":"+Href tensor Lambda_ref","z":"-Href tensor Lambda_ref"},
        "companion_warning":"The same five physical L companions are kept, not identified only by masses.",
        "mixed_domain_warning":"The geometric R_omega and every actual CM fiber must be transported before restricting a Y-mixed pipe.",
        "quarter_anchor":"b=-1 real primitive Omega0 -> b=1 Omega=iOmega0; Norm1 has e=-1-sqrt3, Norm3 has e=-1+sqrt3",
        "weighted_quarter_sign":"-i(c-conjugate(c))"
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(report,indent=2)+"\n")
    print("R501 complete CM ratio, absolute lattice phase, whole four-source exchange, group96 verified.")

if __name__=="__main__":main()
