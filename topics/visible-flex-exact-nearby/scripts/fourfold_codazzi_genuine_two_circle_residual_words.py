"""Signed projected old-circle words for GNJ. Every coefficient jet is on physical r,phi.

No angular bandwidth, numerical import, or finite inverse is selected here.
The calling directed backend supplies the full products, rank maps and means.
"""


class Words:
    """The U.1--11 operators on one original radially enclosed circle.

    Background scalar fields u,v,d and their listed derivatives support
    ordinary coefficient field addition, subtraction and product. All radial
    scalars beta,K,eta and derivatives support ordinary scalar arithmetic.
    Backend operations are specified in the closing function below.
    """
    def __init__(self,b,*,u,v,d,u_phi,v_phi,d_phi,u_phiphi,v_phiphi,
                 u_r,v_r,v_rphi,beta,beta_r,K,K_r,eta,eta_r,m):
        self.b=b
        self.u,self.v,self.d=u,v,d
        self.up,self.vp,self.dp=u_phi,v_phi,d_phi
        self.upp,self.vpp,self.vrp=u_phiphi,v_phiphi,v_rphi
        self.ur,self.vr=u_r,v_r
        self.beta,self.K,self.eta,self.m=beta,K,eta,m
        self.c=-2*beta
        self.cr=-2*beta_r
        self.cB=-2*beta*K
        self.cBr=-2*(beta_r*K+beta*K_r)
        sc=b.scale
        one=b.constant(1)
        self.ell=sc(self.c,u*v)
        self.e0=sc(-beta,one+sc(3,u*u)+sc(K,v*v))
        base=one-u*u-sc(3*K,v*v)
        self.b0=sc(beta,base)
        qp=b.constant(eta_r/eta)+d_phi
        self.tQ=qp+self.e0
        self.T0=self.tQ+self.b0
        ell_r=sc(self.cr,u*v)+sc(self.c,u_r*v+u*v_r)
        ell_p=sc(self.c,u_phi*v+u*v_phi)
        e_p=sc(-beta,sc(6,u*u_phi)+sc(2*K,v*v_phi))
        self.rQ=ell_r-d*ell_p+sc(eta,e_p)+sc(self.c*eta,u_phi*u)-self.ell*qp
        b0_r=sc(beta_r,base)-sc(beta,sc(2,u*u_r)+sc(3*K_r,v*v)+sc(6*K,v*v_r))
        b0_p=sc(-beta,sc(2,u*u_phi)+sc(6*K,v*v_phi))
        vac=self.ell*self.ell-sc(4*beta*eta,v*u_phi)
        self.V0=self.tQ*self.b0-(b0_r-d*b0_p)-sc(K,vac)
        self.v_minus_m=v-b.constant(m)

    def A(self,z):
        return self.b.add(self.b.scale(self.eta,self.b.partial(z)),self.L(z))

    def tip(self,p,q,z):
        return self.b.T(p,self.b.I(self.b.T(q,z)))

    def A_nonlocal(self,z):
        return self.b.scale(self.c,self.tip(self.vp,self.u,z))

    def B_nonlocal(self,z):
        return self.b.scale(self.cB,self.tip(self.vp,self.v,z))

    def C_nonlocal(self,z):
        return self.b.scale(self.c,self.tip(self.up,self.v,z))

    def E_nonlocal(self,z):
        return self.b.scale(self.c,self.tip(self.up,self.u,z))

    def L(self,z):
        return self.b.add(self.b.T(self.ell,z),self.A_nonlocal(z))

    def Bop(self,z):
        return self.b.add(self.b.T(self.b0,z),self.B_nonlocal(z))

    def differentiated_tip(self,k,kr,p,pr,q,qr,z):
        b=self.b
        return b.add(b.scale(kr,self.tip(p,q,z)),b.scale(k,self.tip(pr,q,z)),b.scale(k,self.tip(p,qr,z)))

    def C_commutator(self,p,p_phi,q,q_phi,z):
        """U.3 in physical multiplication order, including both rank words."""
        b=self.b
        qz=b.T(q,z)
        y=b.I(qz)
        term1=b.add(b.T(self.d*p_phi,y),b.scale(-1,b.R(p,self.dp,y)))
        term2=b.T(p,b.I(b.T(self.dp,qz)))
        term3=b.T(p,b.I(b.add(b.T(self.d*q_phi,z),b.scale(-1,b.R(q,self.dp,z)))))
        return b.add(term1,term2,term3)

    def SAC(self,z):
        b=self.b
        core=b.add(b.scale(-1,b.R(self.up,self.v,z)),self.tip(self.upp,self.v,z),
                   b.R(self.vp,self.u,z),self.tip(self.vp,self.up,z))
        nc=self.C_nonlocal(z)
        return b.add(b.scale(self.c*self.eta,core),b.scale(-1,b.R(self.ell,self.ell,z)),
            b.T(self.ell,nc),self.A_nonlocal(b.T(self.ell,z)),self.A_nonlocal(nc))

    def SQ(self,z):
        b=self.b
        na_r=self.differentiated_tip(self.c,self.cr,self.vp,self.vrp,self.u,self.ur,z)
        comm=self.C_commutator(self.vp,self.vpp,self.u,self.up,z)
        ne=self.E_nonlocal(z)
        return b.add(na_r,b.scale(-self.c,comm),b.R(self.ell,self.dp,z),
            b.scale(-self.c*self.eta,b.R(self.up,self.u,z)),b.scale(self.c*self.eta,self.tip(self.upp,self.u,z)),
            b.scale(-1,b.R(self.ell,self.e0,z)),b.R(self.tQ,self.ell,z),b.T(self.ell,ne),
            self.A_nonlocal(b.T(self.e0,z)),self.A_nonlocal(ne),b.scale(-1,b.T(self.tQ,self.A_nonlocal(z))))

    def RQ(self,z):
        return self.b.add(self.b.T(self.rQ,z),self.SQ(z))

    def SV0(self,z):
        b=self.b
        nb_r=self.differentiated_tip(self.cB,self.cBr,self.vp,self.vrp,self.v,self.vr,z)
        comm=self.C_commutator(self.vp,self.vpp,self.v,self.vp,z)
        return b.add(b.scale(-1,b.R(self.tQ,self.b0,z)),b.scale(-1,b.R(self.b0,self.dp,z)),
            b.T(self.tQ,self.B_nonlocal(z)),b.scale(-1,nb_r),b.scale(self.cB,comm),b.scale(-self.K,self.SAC(z)))

    def known_rhs(self,*,Fw,Fh,Fy,Fg,Fq,local):
        """Use the five original unprojected amplitude outputs and G.9 once.

        Each F already carries its proper signed input density power. For a
        common two-order input, sum the two correctly weighted columns in each
        F first. local is the complete projected local expression G.9.
        """
        b=self.b
        f,h,g=b.P(Fw),b.P(Fh),b.P(Fg)
        e=b.add(g,b.scale(-1,self.L(h)),b.scale(-1,self.Bop(f)))
        # This is a physical coefficient vector times a PHYSICAL scalar
        # functional. It is not T_(v_phi) applied to a projected constant.
        pv=b.coeff_P(self.v)
        coeff=b.scale(self.cB,b.coeff_T(self.vp,b.coeff_I(pv)))+b.coeff_P(self.T0)
        Kw=b.add(self.SV0(f),b.scale(-1,self.SQ(h)),b.scale(-self.cB,b.T(self.vp,b.I(b.P(Fq)))),
            b.rank_vector(b.coeff_P(self.rQ),b.Pi(Fh)),
            b.scale(self.cB,b.rank_vector(b.coeff_P(self.vp),b.Pi(Fy))),
            b.rank_vector(coeff,b.Pi(Fg)),
            b.scale(-1,b.rank_vector(b.coeff_P(self.V0),b.Pi(Fw))))
        return dict(f=f,h=h,e=e,Kw=Kw,local=local)

    def residuals(self,data,*,first_trial,second_trial):
        """Evaluate two true residues and the physical even-mean approximation.

        first_trial(e) returns a finite physical nonmean trial in the domain
        of A. second_trial(k) chooses another such trial. Each receives the
        signed directed right side. Projecting the actually read-back trial
        enforces the true degree-zero constraint, including exceptional
        physical frequency zero on a shifted input band.
        """
        b=self.b
        f,h,e,Kw,local=(data[k] for k in ("f","h","e","Kw","local"))
        v=b.P(first_trial(e))
        q=b.add(self.A(v),b.scale(-1,e))
        k=b.add(local,Kw,b.scale(-1,self.RQ(v)))
        t=b.P(second_trial(k))
        p=b.add(self.A(t),b.scale(-1,k))
        h1=b.add(h,v)
        # Pi must be taken before P; T(u,h1) would give a spurious zero.
        mean=b.scale(2*self.beta*self.m,b.add(b.Pi(b.mul(self.u,h1)),
                          b.scale(self.K,b.Pi(b.mul(self.v_minus_m,f)))))
        return dict(v_trial=v,t_trial=t,first_complete_residual=q,second_complete_residual=p,
            complete_signed_trial_even_mean=mean,first_rhs=e,second_rhs=k,known_nonlocal=Kw)


def contract():
    """Small public operator inventory. No scientific call is made at import."""
    return dict(
        coefficient_fields="signed original physical-angle scalar fields with ordinary +,-,*",
        scalar_to_field="constant(a)",
        scale="scale(a,x) multiplies a radial scalar against a coefficient, column, or mean functional",
        add="add(*x) sums same-type signed columns or mean functionals",
        projected_words="T(f,x)=P(f P x), R(f,g,x)=P(f Pi(g P x))",
        unprojected_product="mul(f,x)=f x",
        column_ops=["P(x)","Pi(x)","I(x)=partial_inverse P x","partial(x)"],
        coefficient_ops=["coeff_P(f)","coeff_I(f)","coeff_T(f,g)=P(f P g)"],
        rank_vector="rank_vector(f,a) forms physical f times the column's scalar mean functional, with its true labels",
        source_rows=["first_complete_residual:H^-8/3","second_complete_residual:H^-5/3",
                     "t_trial:H^-2/3","complete_signed_trial_even_mean:scalar"],
        given_physical_jets=["u","v","d","u_phi","v_phi","d_phi","u_phiphi","v_phiphi",
            "u_r","v_r","v_rphi","beta","beta_r","K","K_r","eta","eta_r","m=Pi(v)"])
