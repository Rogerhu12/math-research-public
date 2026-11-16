# R889 — Actual theta distribution, original sigma connection, and the same-label fifth jet

Date: 2026-11-16. Status: proved comparison of actual theta operators and the original first-$p$ sigma coefficients. The result identifies an integral jet of an explicitly specified section at each original label. It does not prove that this jet, its Legendre factor, or the original modular-quotient normal coefficient is nonzero.

## 1. Original data and the parameter of the distribution

Retain the original curve, differential, sigma normalization, and tame six-level marking:
$$
E_0:y^2=x^3-1,\qquad
\omega=\frac{dx}{2y}=dz,\qquad
D=\frac d\omega,\qquad \sigma(z)=z+O(z^7).
\tag{889.1}
$$
Let $p\ge41$, $p\equiv5\pmod6$, and put $k=\mathbf F_{p^2}$. All special-fiber constructions below are over this fixed field. Write
$$
L_m=O_{E_0}(mO),\qquad
\mathcal H=H^0(E_0,L_{6p}),\qquad
s_a s_b=s_{a+b}.
\tag{889.2}
$$
As in R878, a section is represented as $R s_{6p}$, where $R$ is rational with poles bounded by $6pO$.

Use R589 (589.6)--(589.10)'s integral CM parameter $Y$, of tangent one. Its reduction satisfies
$$
E_0[p]=\operatorname{Spec}k[Y]/(Y^{p^2}),\qquad
a_t^*Y=tY\quad(t^{p+1}=1),
$$
$$
\omega=(1+O(Y^{p^2-1}))\,dY,\qquad
Y=z+O(z^{p^2}).
\tag{889.3}
$$
Here $a_t$ is the actual CM action on the finite group scheme, and the second displayed relation is only used in degrees strictly below $p^2$. No global elliptic-curve automorphism corresponding to a general $t$ is assumed.

For a rational function $R$ define the translation distributions
$$
d_jR=[Y^j]R(P+P_Y).
\tag{889.4}
$$
The point $P_Y$ is the formal point in the parameter (889.3). For $j<p$,
$$
d_j=\frac{D^j}{j!},\qquad Dd_j=d_jD.
\tag{889.5}
$$
The commutation follows from translation invariance of $D$. The first identity follows from (889.3), or from the distributions of $\ker F=\alpha_p$. For $j=p$, the symbol $d_p$ always means (889.4), not $D^p/p!$.

Keep exactly the original R574 constant and rational primitive:
$$
B=(-1)^{(p-1)/2-(p-2)/3}
 \binom{(p-1)/2}{(p-2)/3}\in\mathbf F_p^\times,
$$
$$
q=-B^{-1}D^{p-2}x,\qquad
Dq=1,\qquad D^p=0,\qquad D^{p-1}x=-B.
\tag{889.6}
$$
In the parameter $Y$,
$$
q=-B^{-1}Y^{-p}+Y+O(Y^p).
\tag{889.7}
$$
Indeed R574 fixes the unique polar term and its coefficient. Equation (889.3) preserves this polar part, and $Dq=1$ determines all regular coefficients of degrees less than $p$. The constant is zero by oddness.

## 2. The actual $p$th theta coefficient

Let $\tau:E_0[p]\to\mathcal G_p(L_{6p})$ be R878's canonical symmetric section
$$
\tau(u)=g\,\iota(g)^{-1},\qquad
g\text{ lying over }u/2.
\tag{889.8}
$$
Use the action convention in which its rational-frame action has the form
$$
\rho(\tau(P_Y))R(P)=g_Y(P)R(P+P_Y),\qquad
g_0=1,
$$
$$
\operatorname{div}_P(g_Y)=6p[-P_Y]-6p[O].
\tag{889.9}
$$
The divisor equality is an equality of Cartier divisors over the finite scheme, not just of reduced supports. Thus the infinitesimal action on the Cartier frame $s_{6p}$ is $+D$. This fixes the translation sign throughout this paper.

On $\ker F$, the restriction of $\tau$ is a group splitting: the commutator pairing is trivial there. It equals the canonical splitting from
$L_{6p}=F^*L_6^{(p)}$. The splitting is unique over $k$, since
$\operatorname{Hom}_k(\alpha_p,\mathbf G_m)=0$. Therefore
$$
g_Y=1+hY^p+O(Y^{p+1}),
$$
$$
\Theta_p:=[Y^p]\rho(\tau(P_Y))=d_p+h.
\tag{889.10}
$$
The last term denotes multiplication by a rational function.

We determine this actual multiplier, including its constant. It has no poles away from $O$. Near $O$, let $U=Y(P)$ and let $\mathcal F(U,Y)$ be the formal addition law. By (889.9),
$$
g_Y=\mathcal V(U,Y)\frac{\mathcal F(U,Y)^{6p}}{U^{6p}},
\tag{889.11}
$$
where $\mathcal V$ is regular and invertible and $\mathcal V(U,0)=1$. In characteristic $p$, the first positive $Y$-degree in the displayed quotient is $p$. Its coefficient is
$$
6U^{-p}\left(\frac{\partial\mathcal F}{\partial Y}(U,0)\right)^p.
$$
Since the parenthesized series has constant one, (889.10)--(889.11) prove that $h$ has pole order at most $p$, with leading polar term $6U^{-p}$.

The theta commutator identity is
$$
\rho(\tau(P_S))\rho(\tau(P_Y))
=e(P_S,P_Y)\rho(\tau(P_Y))\rho(\tau(P_S)).
\tag{889.12}
$$
Its coefficient of $S Y^p$ gives
$$
[D,\Theta_p]=\kappa\,\operatorname{id}
\tag{889.13}
$$
for some $\kappa\in k$. There are no extra terms here: all coefficients of $S Y^j$ in the pairing for $j<p$ vanish because the pairing is trivial on $\ker F\times\ker F$, and the pairing is one if either argument is zero. Since $D$ commutes with $d_p$, (889.13) says $Dh=\kappa$.

Consequently $h-\kappa q$ is a $p$th power in $k(E_0)$ and has pole bounded by $pO$. Its $p$th root has pole bounded by $O$, so is constant. Comparison of the leading poles gives $\kappa=-6B$. Finally inversion of the curve sends $\tau(P_Y)$ to $\tau(P_{-Y})$ and preserves the symmetric rational frame. Thus $h$ is odd. So is $q$, and the remaining constant is zero.

We have proved the exact operator identity
$$
\boxed{\Theta_p=d_p-6Bq.}
\tag{889.14}
$$
Define
$$
\boxed{Q=-\frac{\Theta_p}{6B}
       =q-\frac{d_p}{6B}.}
\tag{889.15}
$$
It is an actual distribution operator on $\mathcal H$, not a Weyl operator chosen from an abstract representation.

## 3. A second exact translation identity

The operator $d_p$ commutes with $D$, so $D(d_pq)=0$. Translation raises the pole bound of $q$ by at most $p$ at this distribution order; hence $d_pq$ has poles bounded by $2pO$. It is therefore a $p$th power of an element of $H^0(E_0,L_2)$:
$$
d_pq=a x^p+b.
\tag{889.16}
$$
In the original $\mu_6$ action, $q$ has weight $1$ and $d_p$ lowers weight by $p$. Thus $d_pq$ has weight $1-p\equiv2\pmod6$, the same as $x^p$, and its constant term $b$ is zero.

For the remaining scalar, use (889.7) and
$\binom{-p}{p}=-1$ in characteristic $p$. The leading polar term of $d_pq$ is $B^{-1}Y^{-2p}$. It follows that
$$
\boxed{d_pq=B^{-1}x^p.}
\tag{889.17}
$$
This fixes the coefficient in the sigma connection below; a change of the $p$th distribution parameter would not be harmless here.

The Hasse product rule now gives, for $0\le j<p$ and $f\in k(E_0)$,
$$
d_p(q^j f^p)
=j B^{-1}q^{j-1}x^p f^p+q^j(Df)^p.
\tag{889.18}
$$
Indeed $d_1q=1$, $d_jq=0$ for $2\le j<p$, and the only positive translation degree below or equal to $p$ in $f(P+P_Y)^p$ is $(Df)^pY^p$. For $q^j$, the putative term selecting $p$ copies of $Y$ is absent when $j<p$.

The restriction on $j$ is essential. In particular,
$d_p(q^p)=1$; it is not given by the right side of (889.18) with $j=p$.
The full Hasse product rule also records the noncommutativity explicitly:
$$
\boxed{[d_p,q]=d_{p-1}+B^{-1}x^p.}
\tag{889.18a}
$$
No power of $Q$ below is expanded by treating $d_p$ and multiplication by $q$ as commuting operators.

## 4. The original sigma-six Bell connection

On $k(E_0)[\eta]$ put
$$
\delta=D-x\partial_\eta,\qquad
\nabla_6=\delta+6\eta.
\tag{889.19}
$$
Thus $\delta\eta=-x$. For $\eta$ specialized to the original zeta primitive, $\nabla_6$ is exactly the derivative of $f\sigma^6$ divided by $\sigma^6$. There is no change of the Gaussian or of the invariant differential.

Define the Frobenius-semilinear substitution
$$
\Phi\!\left(\sum_j f_j\eta^j\right)
=\sum_j f_j^p(-Bq)^j.
\tag{889.20}
$$
For a polynomial $P$ of degree at most $p-1$ in $\eta$, equation (889.18) gives
$$
d_p\Phi(P)=\Phi(\delta P),
$$
$$
\boxed{
Q\Phi(P)=-\frac1{6B}\Phi(\nabla_6P).
}
\tag{889.21}
$$
In the first equation, $\delta$ differentiates coefficients before Frobenius. Both equations retain that semilinearity.

Starting from $\eta$-independent $f$, every intermediate polynomial
$\nabla_6^r f$ has degree at most $r$. Hence
$$
\boxed{
Q^r(f^p)=\left(-\frac1{6B}\right)^r
 \Phi(\nabla_6^r f),\qquad 0\le r\le p.
}
\tag{889.22}
$$
The step giving $r=p$ still has input degree $p-1$ and is valid. The identity is not asserted at larger $r$.

For clarity, its first failure beyond that range has an exact value. The Jacobson identity and (889.6) give
$$
\nabla_6^p=B\partial_\eta+
  6(\eta^p+Bq).
\tag{889.23}
$$
Here $\delta(\eta^p+Bq)=B$, while
$\Phi(\eta^p+Bq)=0$. Therefore, for $\eta$-independent $f$,
$$
\Phi(\nabla_6^p f)=0,\qquad
\boxed{\Phi(\nabla_6^{p+1}f)=6B f^p.}
\tag{889.24}
$$
This is the original first Cartier boundary, with the factor six appropriate to $\sigma^6$. In particular the ideal generated by $\eta^p+Bq$ is not preserved by $\delta$. A formal quotient by that relation cannot remove the boundary.

At an actual nonzero prime-to-$p$ torsion point $P_0$, R574 (574R.15) gives
$$
-Bq(P_0)=e_{P_0}^p,\qquad e_{P_0}=E_1^*(P_0).
\tag{889.25}
$$
So (889.22) specializes to
$$
Q^r(f^p)(P_0)=
 \left(-\frac1{6B}\right)^r
 \bigl((\nabla_6^r f)(P_0,e_{P_0})\bigr)^p,
 \qquad 0\le r<p.
\tag{889.26}
$$
The evaluation is made where $f$ is regular. For $f\in H^0(E_0,L_6)$ this includes every nonzero six-torsion point. The completed value, its sign, and its Frobenius are exactly the original ones. In characteristic zero the Bell value here is the ordinary derivative at $t=0$ of
$$
f(P_0+t)
\left(
 \frac{\sigma(P_0+t)}{\sigma(P_0)}
 \exp\!\left(-\frac{\overline{z_{P_0}}}{A_\Lambda}t\right)
\right)^6,
\qquad A_\Lambda=\operatorname{Area}(\mathbf C/\Lambda)/\pi,
\tag{889.27}
$$
using R574's same completed-zeta normalization. Thus (889.26) does not insert an arbitrary six-torsion phase.

## 5. The actual finite creation operator and its projections

Equations (889.6), (889.14) imply
$$
[D,Q]=1.
\tag{889.28}
$$
Both operators commute with the actual six-primary theta group. For the canonically normalized $M_t$ of R878/R881, equivariance of $Y$ and of $\tau$ gives
$$
M_t Q M_t^{-1}=t^p Q=t^{-1}Q.
\tag{889.29}
$$
This is the actual CM theta action, not a scaling action guessed from the local formula for $q$.

Let
$$
\mathcal H_0=\ker D
 =\{f^p s_{6p}:f\in H^0(E_0,L_6)\}.
\tag{889.30}
$$
R878 proves that it has dimension six and $M_t$ acts trivially on it. Equation (889.28) gives
$$
D^rQ^r v=r!\,v\quad(v\in\mathcal H_0,\ 0\le r<p).
$$
The $p$ subspaces $Q^r\mathcal H_0$ are independent by successive application of the highest power of $D$, and their dimensions sum to $6p$. Hence
$$
\boxed{
\mathcal H=\bigoplus_{r=0}^{p-1}Q^r\mathcal H_0,\qquad
M_t|_{Q^r\mathcal H_0}=t^{-r}.
}
\tag{889.31}
$$
Moreover $DQ^pv=0$ for $v\in\mathcal H_0$, whereas $Q^pv$ has character $t^{-p}=t$. This character is absent from $\mathcal H_0$, so $Q^pv=0$. Since $Q$ commutes with its powers and the subspaces in (889.31) span, this proves
$$
Q^p=0\quad\text{on }\mathcal H.
\tag{889.32}
$$
This nilpotence has now been established for the specific theta distribution (889.15), rather than inferred for an arbitrarily chosen lift of a Weyl generator.

The vacuum projection and the individual weight projections have exact formulas:
$$
V_0=\sum_{j=0}^{p-1}\frac{(-1)^j}{j!}Q^jD^j,
$$
$$
\boxed{
\mathsf e_{-r}R=\frac{Q^r}{r!}V_0D^rR
\quad(0\le r<p).
}
\tag{889.33}
$$
To check them, apply the first sum to $Q^s v$ and use
$\sum_j(-1)^j\binom sj=\mathbf1_{s=0}$. All factorials are units. In particular (889.22) supplies the actual sigma expression for each vector in these weight spaces.

## 6. Exact first-$p$ jet of a Frobenius-source section

For an integral original section $f\sigma^6$ put
$$
c_n(f)=[z^n](f(z)\sigma(z)^6),\qquad n\ge0.
\tag{889.34}
$$
Here $f\in H^0(E_0,L_6)$ is lifted in the original integral rational basis; for example $f=x$ or $f=-xy$. Coefficients with $n<p$ are integral, as in R702. Reduction of the formula below is independent of the chosen integral coefficients of the lift.

The local frame of $L_{6p}$ at $O$ is
$$
\epsilon_{6p}=s_{6p}/Y^{6p}.
$$
Thus the local coefficient of $R s_{6p}$ is $Y^{6p}R$. This is an integral local frame of the actual line bundle; it does not use an ordinary reduction of the entire sigma series.

We claim
$$
\boxed{
Y^{6p}Q^r(f^p)\equiv
 \sum_{k=0}^r
 \frac{r!}{k!}(-6B)^{\,k-r}
 c_{r-k}(f)^pY^k
 \pmod{Y^p},
 \qquad 0\le r<p.
}
\tag{889.35}
$$

Here is a proof retaining the first Cartier correction. Let $\mathscr E(Y)$ be the original zeta primitive truncated to exponents strictly less than $p$, including its polar term $Y^{-1}$. Its coefficients are integral: integration can first introduce a $p$ denominator at exponent $p$. For $0\le m<p$, put
$$
U_m(Y)=Y^6(\nabla_6^m f)|_{\eta=\mathscr E(Y)}.
\tag{889.36}
$$
Then
$$
U_m(Y)\in\mathcal O[[Y]],\qquad
U_m(0)=m!\,c_m(f).
\tag{889.37}
$$
Indeed at the full characteristic-zero primitive,
$\nabla_6^mf=\sigma^{-6}D^m(f\sigma^6)$, which has pole bounded by $6O$. Also
$$
[\partial_\eta,\nabla_6]=6,\qquad
\partial_\eta^j\nabla_6^mf
 =6^j\frac{m!}{(m-j)!}\nabla_6^{m-j}f.
\tag{889.38}
$$
Changing the full primitive by $O(Y^p)$ therefore changes this expression only in degrees at least $p-6$. No negative degree or the coefficient of $Y^{-6}$ is changed. The truncated expression itself is integral because $f,D,\mathscr E$ are integral. Its constant after multiplication by $Y^6$ is the one in (889.37), since $Y/\sigma$ has constant one.

Reduce now modulo $p$. Equation (889.7) gives
$$
\Delta(Y):=-Bq-\mathscr E(Y)^p
 \equiv-BY\pmod{Y^p}.
\tag{889.39}
$$
Use the polynomial Taylor formula in $\eta$, (889.38), and (889.20):
$$
Y^{6p}\Phi(\nabla_6^rf)
 =\sum_{k=0}^r
 \binom rk6^k\Delta(Y)^k U_{r-k}(Y)^p.
\tag{889.40}
$$
Every $U_{r-k}$ is regular. Modulo $Y^p$, its $p$th power is its constant's $p$th power; insert (889.37) and (889.39), and then multiply by $(-1/(6B))^r$ using (889.22). This is precisely (889.35).

Thus the coefficient $c_m(f)$ has the explicit actual-theta realization
$$
\boxed{
c_m(f)^p=\frac{(-6B)^m}{m!}
 \left.(Y^{6p}Q^m(f^p))\right|_{Y=0},
 \qquad 0\le m<p.
}
\tag{889.41}
$$
The section $Q^m(f^p)s_{6p}$ is nonzero when $f\ne0$, but its value in (889.41) can vanish. This distinction is indispensable.

## 7. The original same-label product and the fifth jet

Now use exactly R770's two original sections and indices:
$$
F=x\sigma^6=z^4\sum_{i\ge0}f_i z^{6i},\qquad
G=-xy\sigma^6=z\sum_{j\ge0}g_j z^{6j},
$$
$$
p=6N+5,\quad i+j=N-1,\quad
h=6i+7,\quad 7\le h\le p-4.
\tag{889.42}
$$
Put
$$
a=h-1=6i+6,\qquad b=p-h=6j+4,
\qquad a+b=p-1.
\tag{889.43}
$$
Define the specified actual tensor section
$$
\mathcal S_h=
 \bigl(Q^a(x^p)s_{6p}\bigr)
 \boxtimes
 \bigl(Q^b((-xy)^p)s_{6p}\bigr).
\tag{889.44}
$$
In the product of the two local frames from §6, let $\mathcal J_{2,3}$ extract the coefficient of $Y^2T^3$. Equation (889.35) gives
$$
\mathcal J_{2,3}(\mathcal S_h)
=\frac{a!\,b!}{2!\,3!}(-6B)^{5-a-b}(f_i g_j)^p.
$$
Since $a$ is even, $\binom{p-1}{a}=1\bmod p$, so Wilson's theorem gives $a!b!=-1$. Also $B\in\mathbf F_p^\times$. Hence the full constant simplifies to
$$
\boxed{
\mathcal J_{2,3}(\mathcal S_h)
=\frac{(6B)^5}{12}(f_i g_j)^p.
}
\tag{889.45}
$$
This realizes the actual fifth lift $2+3$ through the original finite theta distribution, with no factorial crossing $p$. It does not extend R884's nonintegral coefficient functional to all of $\mathcal H$. It uses a different, explicitly specified Frobenius-source section and an integral jet of $L_{6p}$.

The character direction is fixed by (889.29). Under the opposite action
$M_t\boxtimes M_t^{-1}$ of R881,
$$
\mathcal S_h\text{ has character }
t^{-a+b}=t^{-2h}.
\tag{889.46}
$$
This is the inverse of the character $\chi^{2h}$ selecting the original $W_{\mu_h}$ in R881. To place the section in that character space, one can use the explicit factor flip, without changing the label:
$$
\mathcal S_h^{\rm flip}
=\bigl(Q^b((-xy)^p)s_{6p}\bigr)
 \boxtimes
 \bigl(Q^a(x^p)s_{6p}\bigr),
$$
$$
\boxed{
\mathcal P_{2h}\mathcal S_h^{\rm flip}
 =\mathcal S_h^{\rm flip},\qquad
\mathcal J_{3,2}(\mathcal S_h^{\rm flip})
 =\frac{(6B)^5}{12}(f_i g_j)^p.
}
\tag{889.47}
$$
The product frame and its jet are flipped at the same time. This is an actual identity of sections and jets, not an identification of the flipped section with the original split vector or with R886's contraction.

Keep the original $s=\sqrt{-3}$ and impose the actual primitive condition $(h,p+1)=1$. Because $h-1$ is even,
$P_{h-1}(1/s)\in\mathbf F_p$. Thus
$$
\boxed{
P_{h-1}(1/s)\mathcal J_{3,2}(\mathcal S_h^{\rm flip})
=\frac{(6B)^5}{12}
 \bigl(P_{h-1}(1/s)f_i g_j\bigr)^p.
}
\tag{889.48}
$$
All displayed outside factors are units. The original same-$h$ nonvanishing is therefore exactly the nonvanishing of this specified integral fifth jet with its same original Legendre factor.

No labels have been merged. In particular the integer pair $(a,b)$ is retained in (889.44)--(889.47). The projector $\mathcal P_{2h}$ alone does not distinguish $h$ from $h+(p+1)/2$; R881's determinant-quadratic distinction and the original period marking still apply.

## 8. What remains for the original source

The result supplies three specific comparisons previously absent from the enlarged-theta construction:

1. the exact $p$th distribution in its original rational frame, (889.14);
2. its first-$p$ intertwining with the original sigma connection and completed six-torsion values, (889.22), (889.26);
3. the full original same-label product as an integral fifth jet of the specified character section, (889.45)--(889.48).

It does not identify
$\mathcal S_h^{\rm flip}$ with
$\mathcal P_{2h}(x s_{6p}\boxtimes(-xy)s_{6p})$,
with R886's $\Gamma_h$, or with its split contraction $\mathcal C_h$.
Those sources use different constructions, and the generic norm-model comparison still does not justify dropping the divisions by $p$ or their tame multiplicity vectors.

Likewise, a nonzero weight vector in (889.31) need not have nonzero value at $O$, as (889.41) makes explicit. Nonzero curvature, an invertible full comparison matrix, or the nonvanishing of an unscreened sum cannot replace the simultaneous specified jet and Legendre condition in (889.48). The actual R706/R739 zero examples remain compatible with every formula here.

The next arithmetic task is the original split/period or ramified-source comparison for these specified vectors, or a direct nonvanishing proof for their fifth jets on the primitive and Legendre-visible set. No new prime scan or executed arithmetic is used in this proof.

## Sources

- [R574](R574-completed-zeta-Cartier-input.md), (574R.4), (574R.7), (574R.15), (574R.20)--(574R.21): original $D,B,q$, completed torsion values, and the Cartier boundary.
- [R589](R589-specified-type-three-coefficient-and-actual-CM-unit-criterion.md), (589.6)--(589.12): actual integral CM parameter, finite-group action, and primitive-coefficient integrality. The same parameter and differential range are retained in [R855](R855-original-primitive-higher-Abel-unit-from-cubic-Cartier.md), (855.13).
- [R702](R702-first-pole-block-and-uniform-shifted-units.md), §§1--3: the original finite sigma-integrality range and its first pole.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md), §§1--3: original $F,G$, label $h$, critical indices, and required common product.
- [R878](R878-original-finite-theta-action-and-section-projections.md), §§2--5: actual symmetric theta section, Cartier splitting, normalized $M_t$, and derivative filtration.
- [R881](R881-original-integral-theta-lift-and-cuspidal-test-vector.md), §§5--7: the sign of the original $\chi^{2h}$ character and its full determinant extension.
- [R884](R884-original-enlarged-theta-lattice-coefficient-pole.md) and [R886](R886-original-two-flag-theta-descent-and-split-contraction.md): the distinct full-lattice denominator and original contraction interfaces retained in §8.
