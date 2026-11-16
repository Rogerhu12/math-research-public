# R150: integral source cost 26410 for every high-normal basis target at 127

Author: ChatGPT (AI), literature_audit.  
Date: 2026-11-16 UTC.  
Status: exact existence and degree bound from the completed original infinity spectra and whole-module theorem. No new determinant or source array is computed.

## 1. Result in the complete original source module

Put $p=127$, $D=\mathbb Z_{(127)}$, and $R=D[s]$. Retain
$$
A:R^{6188}\longrightarrow V=R^{4367},\qquad
L=\operatorname{im}A,
$$
with all original seventeen equations and all moment multipliers of degree at most three. In the ordinary original binomial coordinates
$$
z_j=\sum_{a=0}^j\binom ja(-s)^{j-a}m_a,
$$
let $W$ be the rank-4212 coordinate summand with basis
$$
w_\beta=\prod_{j=0}^{10}z_j^{\beta_j},\qquad
|\beta|\le5,\qquad\sum_{j=2}^{10}\beta_j\ge2.
$$
Use $h_*=s^3F_+^2F_-^2E_8$, of degree 23 and leading coefficient 3125, a unit of $D$.

The [complete whole-$W$ theorem at 127](R150-appendix-whole-normal-square-module-at127-has-one-extra-coefficient-torsion-direction.md) proves
$$
\operatorname{Ann}_R((W+L)/L)=h_*(127,s+64).
\tag{1.1}
$$
Therefore, for $q\in D[s]$,
$$
h_*qW\subseteq L\quad\Longleftrightarrow\quad q(63)\in127D.
\tag{1.2}
$$
Indeed, modulo 127 the ideal $(127,s+64)$ is the kernel of evaluation at $s=63$.

For every nonzero $q$ satisfying (1.2), each of the 4212 basis targets has an original source
$$
Ay_{q,\beta}=h_*q\,w_\beta,\qquad
y_{q,\beta}\in D[s]^{6188},
$$
with
$$
\boxed{\operatorname{cost}(y_{q,\beta})
\le\max\{26410,124+\deg q\}.}
\tag{1.3}
$$
In particular the two complete families $127h_*w_\beta$ and $(s+64)h_*w_\beta$ have original integral sources of cost at most $26410$. The common coefficient exponent one is necessary for the former whole-$W$ family, by the nonzero extra summand in (1.1); this does not say that the nine diagonal targets themselves require a factor 127.

## 2. A literal original minor with a 127-unit leading coefficient

The [complete rational infinity theorem](R150-appendix-infinity-complete-tenth-connection-one-and-full-characteristic-zero-spectrum66.md), Section 1, proves the positive Smith spectrum of the original natural matrix $A^\infty(u)$:
$$
(1,1,1,1,3,4,4,4,5,6,7,8,10,11).
$$
The [independent complete prime-127 qualification](R150-appendix-complete-original-infinity-prime127-spectrum66-and-affine-gauss-bound299.md), Sections 1--4, proves the same spectrum over $\mathbb F_{127}[[u]]$, with all original source and output coordinates retained. In both characteristics the generic rank is $r=4354$, and
$$
\delta_r=66,\qquad\delta_{r-1}=55.
\tag{2.1}
$$
The prime-127 qualification also checks the required original normalization and coordinate denominators as units. Its Section 5, equation (5.1), states the equality of the minima over the literal original homogeneous maximal minors.

The maximal-minor ideal of $\overline{A^\infty}$ has valuation 66. Hence at least one of its finitely many original $r$-by-$r$ minors has a nonzero coefficient of $u^{66}$. Choose its original row and column sets $I,J$, and put
$$
B=A[I,J],\qquad D_B=\det B.
$$
Every original characteristic-zero maximal minor has valuation at least 66 by (2.1). Thus the chosen natural determinant has no earlier nonzero coefficient, and its coefficient at $u^{66}$ is a unit of $D$.

For the original source and output weights $a_\ell,b_i$ put
$$
H=\sum_{\ell\in J}a_\ell-\sum_{i\in I}b_i.
$$
The exact natural homogenization is
$$
B^\infty(u)=\operatorname{diag}(u^{-b_i})
B(1/u)\operatorname{diag}(u^{a_\ell}),
$$
so
$$
\det B^\infty(u)=u^H D_B(1/u).
$$
It follows that
$$
\boxed{\deg D_B=H-66,\qquad
\operatorname{lc}(D_B)\in D^\times.}
\tag{2.2}
$$
This selects an existing literal original minor. Its index sets are not enumerated here, and no numerical value of its leading coefficient is asserted. In particular, it is not identified with the previously specified prime-31 minor or the old order-243 minor.

## 3. The exact affine divisor is integral at 127

Let $K'=\Delta_{\rm aff}$ be the monic full rational gcd of the original maximal minors. The [completed degree-298 theorem](R150-appendix-exact-affine-divisor298-unmultiplied-nine-sources-and-rank-one-bell16.md) gives
$$
\deg K'=298.
$$
We recall why $K'\in D[s]$ follows from (2.2), independently of any prime-31 integrality assertion.

Normalize $D_B$ temporarily by its unit leading coefficient to obtain a monic polynomial $P\in D[s]$. Over $\mathbb Q[s]$ write $P=K'Q$ with both factors monic. For a nonzero rational polynomial $f$, let $v(f)$ be the minimum 127-adic valuation of its coefficients. Gauss's content equality is
$$
v(fg)=v(f)+v(g).
$$
To see it directly, scale each factor to have integral coefficients with at least one unit coefficient. Their two nonzero reductions have nonzero product over the residue field. Since a monic polynomial has $v\le0$, whereas $v(P)=0$, the equality forces
$$
v(K')=v(Q)=0.
$$
Thus both monic factors belong to $D[s]$. Return now to the actual, unrescaled determinant and its actual adjugate. We have
$$
d_*=D_B/K'\in D[s],\qquad
q_*:=\deg d_*=H-364,\qquad
\operatorname{lc}(d_*)\in D^\times.
\tag{3.1}
$$

## 4. Cofactors, replacements, and complete source reduction

Every original-column replacement of $B^\infty$ is another original maximal minor, or is zero. Every cofactor is an original $(r-1)$-minor. Equation (2.1) therefore supplies the bounds
$$
\deg\bigl(\operatorname{adj}(B)A_{\ell,I}\bigr)_j
\le H-a_j+a_\ell-66,
$$
$$
\deg(\operatorname{adj}B)_{ji}
\le H-a_j+b_i-55.
\tag{4.1}
$$
These are consequences of the complete original matrix's determinantal valuations. They do not rely on a special source complement at prime 31.

Monic division by $K'$ gives
$$
P_\ell=\operatorname{adj}(B)A_{\ell,I}/K'\in D[s]^r,
\qquad A_JP_\ell=d_*A_\ell.
\tag{4.2}
$$
The identity holds on all 4367 outputs: it holds on $I$ by the adjugate identity, and projection to $I$ is injective on the rational generic image, since $B$ is a nonzero maximal minor.

For any already proved exact member $b\in L$, membership gives
$$
T_b=\operatorname{adj}(B)b_I/K'\in D[s]^r.
$$
Divide its given nonbasic source coefficients by $d_*$, transfer the quotients with (4.2), and keep remainders $r_\ell$ of degree less than $q_*$. The resulting source satisfies
$$
d_*y_J=T_b-\sum_{\ell\notin J}P_\ell r_\ell.
\tag{4.3}
$$
All operations are in $D[s]$. They are the same original degree-reduction construction as in the [uniform integral reduction theorem](R150-appendix-uniform-source-bound8655-over-all-powers-of31.md), but (2.2), (3.1), and (4.1) establish its hypotheses for this independently selected prime-127 minor.

Use the original weights
$$
a_{m^\alpha N_i}=20+10|\alpha|,\qquad
a_{m^\alpha\Gamma_i}=25+10|\alpha|,\qquad |\alpha|\le3,
$$
and $b_{m^\beta}=10|\beta|$. Define
$$
\operatorname{cost}(y)=\max_{y_\ell\ne0}(\deg_s y_\ell+a_\ell-10),
\qquad
\tau(b)=\max_{b_i\ne0}(\deg_s b_i+b_i^{\rm wt}).
$$
Since $\max a_\ell=55$, (3.1)--(4.3) give the three bounds
$$
\begin{aligned}
\text{nonbasic}&\le q_*-1+45=H-320,\\
\text{original-column transfer}&\le H+55-66-298-11=H-320,\\
\text{target adjugate}&\le H+\tau(b)-55-298-10-q_*
=\tau(b)+1.
\end{aligned}
$$
Thus
$$
b\in L\quad\Longrightarrow\quad
\exists\,y\in D[s]^{6188}:Ay=b,\qquad
\operatorname{cost}(y)\le\max\{H-320,\tau(b)+1\}.
\tag{4.4}
$$

## 5. A bound using only the complete original weight dictionaries

There are $\binom{13}{3}=286$ original degree-three monomial multipliers in eleven moment variables. The greatest original source weight is 55, occurring on the $6\cdot286=1716$ cubic $\Gamma$ sources. The next greatest weight is 50, occurring on $11\cdot286=3146$ cubic $N$ sources. Every other source weight is smaller. Consequently, for any set of 4354 distinct original columns,
$$
\sum_{\ell\in J}a_\ell
\le1716\cdot55+(4354-1716)\cdot50
=226280.
\tag{5.1}
$$
The original positive moment degrees one through five have output counts
$$
11,\quad66,\quad286,\quad1001,\quad3003,
$$
and weights $10,20,30,40,50$, respectively. Their full weight sum is
$$
11\cdot10+66\cdot20+286\cdot30+1001\cdot40+3003\cdot50
=200200.
$$
Selecting 4354 of the 4367 outputs omits exactly thirteen, each of weight at most 50. Hence
$$
\sum_{i\in I}b_i\ge200200-13\cdot50=199550.
\tag{5.2}
$$
Equations (5.1)--(5.2) imply
$$
H\le26730,\qquad H-320\le26410.
$$
Together with (4.4), this proves for every already paid exact integral member
$$
\boxed{\exists\,y:Ay=b,\qquad
\operatorname{cost}(y)\le\max\{26410,\tau(b)+1\}.}
\tag{5.3}
$$
The weight counts are those of the complete original dictionaries. They are not the counts of a previously compressed 5528-column presentation.

## 6. Applying the bound to the entire $W$ basis

For $w_\beta$ in Section 1, set $d=|\beta|$ and $\omega=\sum j\beta_j$. Its original moment degree is $d$ and every parameter coefficient has degree at most $\omega$. Thus
$$
d\le5,\qquad\omega\le50,
\qquad\tau(h_*q\,w_\beta)\le23+\deg q+\omega+10d
\le123+\deg q.
$$
Membership is supplied by (1.2), so (5.3) proves (1.3). The target branches for $q=127$ and $q=s+64$ are at most 124 and 125; both are below 26410.

This is an existence and weighted source-degree theorem. It does not enumerate the selected minor's index sets, expand its determinant or the 4212 source vectors, or bound their coefficient heights. A polynomial combination of basis vectors with unbounded parameter coefficients must use its actual $\tau$ in (5.3). The statement retains only the same degree-at-most-three moment multipliers; it does not transfer this cost to a later higher-degree Bell ideal identity.

No numerical computation is added here. The arithmetic input is precisely the completed original infinity spectrum at 127, its rational counterpart, the exact affine divisor of degree 298, and the complete whole-$W$ annihilator. The unrestricted non-rank-one Bell and ordinary invariant-subspace questions remain open.
