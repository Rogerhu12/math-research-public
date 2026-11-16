# R150: all high-normal basis targets have integral source cost 8515 at 31

Author: ChatGPT (AI), literature_audit.  
Date: 2026-11-16 UTC.  
Status: exact source-degree consequence of the completed whole-module theorem and the previously proved original integral degree reduction; no new matrix calculation.

## 1. The complete original module and the result

Put $p=31$, $D=\mathbb Z_{(31)}$, $R=D[s]$, and $x=s-2$. Retain the complete original map
$$
A:R^{6188}\longrightarrow V=R^{4367},\qquad L=\operatorname{im}A.
$$
Its source coordinates are the seventeen original equations multiplied by all original moment monomials of degree at most three. In the ordinary binomial coordinates
$$
z_j=\sum_{a=0}^j\binom ja(-s)^{j-a}m_a,
$$
let $W$ be the rank-4212 coordinate summand spanned by
$$
w_\beta=\prod_{j=0}^{10}z_j^{\beta_j},\qquad
|\beta|\le5,\qquad \sum_{j=2}^{10}\beta_j\ge2.
\tag{1.1}
$$
Write
$$
h_*=s^3F_+^2F_-^2E_8,\qquad h_0=xh_*.
$$
Here $\deg h_*=23$ and its leading coefficient $3125$ is a unit of $D$.

The [complete whole-module theorem over $D$](R150-appendix-whole-normal-square-module-over-D31-is-generated-by-nine-squares.md) proves
$$
(W+L)/L=\sum_{j=2}^{10}R[z_j^2],\qquad
\operatorname{Ann}_R((W+L)/L)=h_*(p^5,p^2x,x^2).
\tag{1.2}
$$
In particular, for a fixed polynomial $q\in D[s]$,
$$
h_*qW\subseteq L
\quad\Longleftrightarrow\quad
q(2)\in p^5D,\qquad q'(2)\in p^2D.
\tag{1.3}
$$
The implication from the two conditions to membership follows by ordinary division by $x^2$:
$$
q(s)=q(2)+xq'(2)+x^2r(s),\qquad r\in D[s].
$$
The converse follows from the exact annihilator in (1.2).

For every nonzero $q$ satisfying (1.3), and separately for every one of the 4212 basis monomials in (1.1), there is an original integral source
$$
Ay_{q,\beta}=h_*q\,w_\beta,\qquad
y_{q,\beta}\in D[s]^{6188},
$$
with
$$
\boxed{\operatorname{cost}(y_{q,\beta})
\le\max\{8515,124+\deg q\}.}
\tag{1.4}
$$
For $q=0$ the zero source suffices. In particular, all three families
$$
p^5h_*w_\beta,\qquad p^2h_0w_\beta,\qquad x^2h_*w_\beta
\tag{1.5}
$$
have original sources of cost at most $8515$ over $D[s]$.

## 2. The integral reduction with the exact degree-298 divisor

The [uniform integral source-reduction theorem](R150-appendix-uniform-source-bound8655-over-all-powers-of31.md) uses the specified original maximal submatrix $B_*=A[I_*,J_*]$. Its determinant retains its actual normalization:
$$
D_*=\det B_*,\qquad
H_*=8835,\qquad \deg D_*=8769,\qquad
\operatorname{lc}(D_*)\in D^\times.
$$
The natural determinant order is $66$, all original-column replacement orders are at least $66$, and all cofactor orders are at least $55$. These are properties of that complete original submatrix, not of a new minor selected for the targets in (1.1).

The [complete coefficient-exponent theorem, Section 6](R150-appendix-complete-coefficient31-exponent-six-and-exact-original-p2h0-sources.md), substitutes the exact monic common divisor
$$
K'=\Delta_{\rm aff}\in D[s],\qquad \deg K'=298
$$
into the same reduction. Only $K'$ is monic; neither $D_*$ nor its adjugate is rescaled. Thus
$$
d_*=D_*/K'\in D[s],\qquad \deg d_*=8471,
\qquad \operatorname{lc}(d_*)\in D^\times.
\tag{2.1}
$$

For every original source column $A_\ell$, the original replacement-minor identities give
$$
P_\ell=\operatorname{adj}(B_*)(A_\ell)_{I_*}/K'
\in D[s]^{4354},\qquad
A_{J_*}P_\ell=d_*A_\ell.
\tag{2.2}
$$
The quotient is integral because $K'$ is monic and the remainder vanishes over $\mathbb Q[s]$. The identity holds on all 4367 original outputs.

Fix any already proved member $b\in L$, with any original source $Ay=b$. Then
$$
T_b=\operatorname{adj}(B_*)b_{I_*}/K'\in D[s]^{4354},
$$
since the numerator is an integral source combination of those in (2.2). Divide each nonbasic source coefficient by the leading-unit polynomial $d_*$, transfer its quotient using (2.2), and keep its remainder. This preserves the target and stays in $D[s]^{6188}$.

The original source weights are
$$
a_{m^\alpha N_i}=20+10|\alpha|,\qquad
a_{m^\alpha\Gamma_i}=25+10|\alpha|,\qquad |\alpha|\le3.
$$
The output weight of $m^\gamma$ is $10|\gamma|$. Define
$$
\operatorname{cost}(y)=
\max_{y_\ell\ne0}\bigl(\deg_s y_\ell+a_\ell-10\bigr),\qquad
\tau(b)=\max_{b_\gamma\ne0}
\bigl(\deg_s b_\gamma+10|\gamma|\bigr).
$$
The three complete degree-reduction branches are
$$
\begin{aligned}
\text{nonbasic remainder}&\le8471-1+45=8515,\\
\text{original-column transfer}&\le8835+55-66-298-11=8515,\\
\text{target adjugate}&\le8835+\tau(b)-55-298-10-8471
=\tau(b)+1.
\end{aligned}
$$
Consequently the general exact statement is
$$
\boxed{b\in L\quad\Longrightarrow\quad
\exists\,y\in D[s]^{6188}: Ay=b,
\quad\operatorname{cost}(y)\le\max\{8515,\tau(b)+1\}.}
\tag{2.3}
$$
The original proof also applies to every existing congruence solution modulo $p^n$. In this appendix membership is already exact by (1.2), so no finite-precision lifting argument is needed to use (2.3).

## 3. The target-weight calculation for all 4212 basis monomials

For $w_\beta$ in (1.1), put
$$
d=|\beta|,\qquad \omega=\sum_{j=0}^{10}j\beta_j.
$$
Each $z_j$ has original moment degree one and parameter degree at most $j$. Therefore $w_\beta$ has original moment degree $d$, and every original moment coefficient has parameter degree at most $\omega$. In particular,
$$
d\le5,\qquad\omega\le10d\le50.
$$
This is the same original coordinate estimate used in the [rational whole-$W$ source theorem, Section 3](R150-appendix-all-high-normal-source-cost8391-and-rank-one-bell-eighth-powers.md). Including the parameter multiplier $q$ gives
$$
\tau(h_*q\,w_\beta)
\le23+\deg q+\omega+10d
\le123+\deg q.
\tag{3.1}
$$
Equations (1.3), (2.3), and (3.1) prove (1.4). For the three ideal generators in (1.5), the target-adjugate branch is respectively at most

| Multiplier on $w_\beta$ | Degree of $q$ | Target branch $\tau+1$ | Complete source bound |
|---|---:|---:|---:|
| $p^5h_*$ | 0 | 124 | 8515 |
| $p^2h_0=p^2xh_*$ | 1 | 125 | 8515 |
| $x^2h_*$ | 2 | 126 | 8515 |

Scalar powers of $p$ do not increase the parameter degree. Every source in the table still uses the original seventeen equations and moment multipliers of degree at most three.

## 4. Exact common coefficient exponents and the scope of the bound

The exact annihilator (1.2) also proves
$$
p^e h_*W\subseteq L\quad\Longleftrightarrow\quad e\ge5,
$$
and
$$
p^e h_0W\subseteq L\quad\Longleftrightarrow\quad e\ge2.
\tag{4.1}
$$
Thus five and two are the exact common coefficient-denominator exponents for these two whole-$W$ families. Their necessity is already detected by each of the nine original square targets. No assertion is made that every other individual basis monomial needs the common maximum.

Equivalently, each $h_*w_\beta$ has a rational original source with $31$-adic denominator exponent at most five, and each $h_0w_\beta$ has one with exponent at most two, both with cost at most $8515$. Other primes in rational coefficient denominators are not constrained by this statement.

For a general element $w=\sum_\beta r_\beta(s)w_\beta\in W$, the coefficients $r_\beta$ may have arbitrarily large parameter degrees. Formula (2.3), with the actual value of $\tau(h_*qw)$, is the general statement. The bound $123+\deg q$ is specifically for the basis monomials in (1.1); it is not a fixed bound for arbitrary parameter-polynomial combinations.

This appendix proves existence and weighted degree bounds. It does not expand the 4212 source vectors, bound their coefficient heights, or change the degree-three original source family. The leading-unit argument used here is the paid one over $D=\mathbb Z_{(31)}$; no corresponding numerical bound over $\mathbb Z_{(127)}$ is inferred. The separate non-rank-one Bell and unrestricted Jacobian questions remain unchanged.
