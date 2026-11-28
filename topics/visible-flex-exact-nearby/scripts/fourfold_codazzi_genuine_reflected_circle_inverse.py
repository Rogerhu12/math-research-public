"""JI.11 and both GNJ source rows on an actual reflected original circle.

The coefficient fields here are unshifted physical functions. A column can
contain one or several shifted oscillatory blocks and independent unshifted
physical output. The primitive and physical constant functional act on this
whole representation. No finite inverse or inherited collar gap is used.
"""


def require(ok,message):
    if not ok:
        raise ValueError(message)


class ReflectedInverse:
    def __init__(self,b,words,*,circle,qualify_background):
        """qualify_background checks the authentic old r,phi and reflected family.

        coeff_exp(z), coeff_Pi(z) and real_ball(z) are additional backend
        operations. real_ball returns an interval containing the REAL value
        after the caller has proved the reality of that expression.
        """
        require(words.b is b,"same directed physical coefficient and column backend")
        require(qualify_background(circle,words) is True,
                "one complete original real reflected u odd, v even, radial beta and eta")
        eta=b.real_ball(words.eta)
        require(eta.is_finite() and (eta.lower()>0 or eta.upper()<0),"actual radial eta separated from zero on this circle")
        alpha=2*words.beta/eta
        iv=b.coeff_I(words.v)
        ell=b.scale(alpha,b.coeff_I(words.u*words.v))
        a=b.coeff_exp(b.scale(-1,ell))
        ainv=b.coeff_exp(ell)
        one=b.constant(1)
        positive_term=one-b.scale(alpha,words.u*iv)
        D=b.real_ball(b.coeff_Pi(a*positive_term))
        require(D.is_finite() and D.lower()>0,"new JI.5 full positive denominator on this actual radial circle")
        self.b,self.words,self.circle=b,words,circle
        self.a,self.ainv,self.iv,self.eta,self.alpha=a,ainv,iv,eta,alpha
        self.c_weight=a*words.u
        self.mean_source=b.scale(-1,positive_term)
        self.D=D

    def _signed_formula(self,f):
        """Linear expression on one summand; its inverse interpretation is on the qualified reflected sum."""
        b=self.b
        k=b.I(f)
        c=b.scale(1/(self.eta*self.D),b.Pi(b.mul(self.c_weight,k)))
        F=b.add(b.scale(1/self.eta,b.mul(self.words.u,k)),b.rank_vector(self.mean_source,c))
        p=b.mul(self.ainv,b.I(b.mul(self.a,F)))
        return b.add(b.scale(1/self.eta,k),b.scale(self.alpha,b.mul(self.words.v,p)),
                     b.scale(self.alpha,b.rank_vector(self.iv,c)))

    def apply(self,f,*,qualify_rhs,source_role):
        """The qualification checks the authentic full physical input or its exact reflection pairing.

        A backend representing an entire real input as a simultaneous signed
        band may retain both signs internally. A bare unreflected plane wave
        is never given an independent two-sided-inverse interpretation.
        """
        require(qualify_rhs(self.circle,source_role,f) is True,
                "the same original reflected even mean-zero input, including admissible paired sign decomposition")
        return self._signed_formula(f)

    def apply_signed_components(self,parts,*,qualify_sum,source_role):
        """Distribute the linear expression only after its SAME physical sum has been qualified.

        The returned parts reconstruct J of that sum. Individual addends have
        no independently asserted parity or inverse equation.
        """
        require(isinstance(parts,(list,tuple)) and parts and qualify_sum(self.circle,source_role,parts) is True,
                "actual physical sum of these signed input components is the original even nonmean map")
        return [self._signed_formula(f) for f in parts]

    def physical_source(self,data,*,qualify_rhs):
        """GNJ.2--4 directly at both exact J applications on the same physical cell."""
        b,w=self.b,self.words
        v=self.apply(data["e"],qualify_rhs=qualify_rhs,source_role="first_e")
        k=b.add(data["local"],data["Kw"],b.scale(-1,w.RQ(v)))
        g1=self.apply(k,qualify_rhs=qualify_rhs,source_role="second_local_Kw_minus_RQv")
        g2=b.scale(2*w.beta*w.m,b.add(b.Pi(b.mul(w.u,b.add(data["h"],v))),
                                      b.scale(w.K,b.Pi(b.mul(w.v_minus_m,data["f"])))))
        return dict(first_exact_J=v,whole_second_rhs=k,first_physical_source=g1,
                    independent_physical_even_mean=g2,actual_radial_D_J=self.D)
