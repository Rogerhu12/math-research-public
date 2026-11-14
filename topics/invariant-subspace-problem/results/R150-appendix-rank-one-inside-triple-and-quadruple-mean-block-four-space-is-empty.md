# R150 appendix — a rank-one inside mean cannot occupy a triple or quadruple block in the common four-space

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved**, using the original highest identity.

## 1. Statement and complete local alternatives

Suppose the original tensors satisfy
$$
y=a v(s),\quad a\ne0,\qquad
\operatorname{ess}(T_3)=W,\quad \dim W=3,\quad y\in W,
$$
and their minimal common space has dimension four.
It is the physical space $E_g$ of an exact length-four divisor by
§2 of
[the rank-one outside-section appendix](R150-appendix-rank-one-mean-outside-essential-three-section-is-empty.md);
that physical-support lemma does not assume the mean is outside.

**Theorem.** If $T_3(Kv)\equiv0$, the multiplicity of $s$ in $g$
cannot be three or four.

All complex coefficients, every zero lower coefficient, every
genuine local jet coordinate and the point at infinity are included.
The mean multiplicities one and two are treated separately in
[the double-mean-block four-space appendix](R150-appendix-rank-one-inside-double-mean-block-four-space-is-empty.md).

Weighted scaling permits $y=u_0=v(s)$: divide $y,H,V$ by
$a,a^2,a^3$, respectively. It preserves the highest identity and
all essential supports.

Let $\lambda$ generate $\operatorname{ann}_{E_g}W$.
Then $\lambda(y)=0$ and
$$
H\lambda=z\in\operatorname{span}(u_0,u_1),\qquad
V\lambda=yz,\qquad z\ne0.
\tag{1.1}
$$
The last assertion follows from minimality of the common space.

Let $j$ be the local order of $\lambda$ at $s$.
The exact local lengths of $H,V$ at $s$ are equal:
if $z$ has length $r=1$ or $2$, their top-coefficient Frobenius
pairings give $n_H-j=r=n_V-j$.
At every other support $\lambda$ vanishes on all the actual
$H,V$ jets, hence on their exact union.
Thus the multiplicity at $s$ is
$$
n=n_H=n_V,\qquad j=n-r,\qquad r\in\{1,2\}.
\tag{1.2}
$$
In particular both top coefficients at $s$ are nonzero.

For $n=3,4$, all possibilities are
$$
(n,j)=(3,2),(3,1),(4,3),(4,2).
\tag{1.3}
$$
When $j<n-1$, a genuine formal local parameter can be chosen so that
$\lambda(v(\epsilon))=\epsilon^j$ to the needed jet order.
This is obtained by taking a $j$th root of its nonzero leading unit;
it changes only the physical Taylor basis, not $K$.
For $j=n-1$ the standard local parameter already has the required
zero lower coefficients, and only a nonzero normalization is needed.

Write $u_i$ for Taylor jets, and $h_i,v_i$ for the local moment
coefficients. The physical polynomial forms are
$$
H_s=\sum_{i+k<n}h_{i+k}u_i u_k,\qquad
V_s=\sum_{i+k+l<n}v_{i+k+l}u_i u_k u_l.
\tag{1.4}
$$
Equation (1.1) gives, respectively,
$$
\begin{array}{c|c}
r=1&v_{n-1}=h_{n-1}\\
r=2&v_{n-2}=h_{n-2},\quad 2v_{n-1}=h_{n-1}.
\end{array}
\tag{1.5}
$$

## 2. Triple block with order-two annihilator

Here $g=3s+t$, $t\ne s$, and
$$
W=\operatorname{span}(u_0,u_1,w),\qquad w=v(t).
$$
Use $X=u_0,Y=u_1,Z=u_2,L=w$ as polynomial directions.
Write the residual tensors as $H_t=h_L L^2,V_t=v_L L^3$;
their coefficients are not both zero.
With
$$
A=1-6h_0+4v_0,\qquad B=12(v_1-h_1),
$$
the exact full tensor after $v_2=h_2\ne0$ is
$$
T_3=X\bigl(A X^2+BXY+6h_2Y^2-6h_L L^2\bigr)+4v_L L^3.
\tag{2.1}
$$

Put $k=K(u_0,w)$ and $\ell=K(u_1,w)$.
We first have $k=0$.
Otherwise the residual physical polar is a unit at $s$, and the
highest identity there first gives $v_L=0$.
The term $-6h_Lp_0p_L^2$ then has strictly smaller order than all
remaining terms, by the exact consecutive orders of $p_0,p_1$.
It gives $h_L=0$, contradicting exact support at $t$.

### 2.1 The residual cubic coefficient is zero

If $v_L=0$, then $h_L\ne0$ and the highest identity, after cancelling
the nonzero $p_0$, gives the quadratic relation
$$
A p_0^2+Bp_0p_1+6h_2p_1^2-6h_Lp_L^2=0.
\tag{2.2}
$$
At $t$, where $p_0(t)=p_L(t)=0$, this forces $\ell=0$.

If $K(u_1,u_1)\ne0$, the exact orders at $s$ are two and one for
$p_0,p_1$, while $p_L$ has order at least two because $k=\ell=0$.
The term $6h_2p_1^2$ is then the unique order-two term of (2.2),
a contradiction. Thus $K(u_1,u_1)=0$.

All pairings on $\operatorname{span}(u_0,u_1,w)$ now vanish.
The original
[isotropic length-three jet classification](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)
excludes every nonreduced divisor of type $2+1$.
This finishes the zero-$v_L$ case.

### 2.2 The residual cubic coefficient is nonzero

Suppose $v_L\ne0$.
If the image is a conic, its nondegenerate equation $Q$ divides
(2.1). On the line $X=0$, the third tensor restricts to $4v_LL^3$.
The restrictions of its quadratic and linear factors are nonzero,
so $Q|_{X=0}$ is a nonzero scalar times $L^2$.
Thus the physical value coordinate $X$ is a tangent line to this
conic. Since $W$ contains the complete physical tangent block
$\operatorname{span}(u_0,u_1)$, this contradicts the
[physical first-jet conic theorem](R150-appendix-no-conic-tangent-coordinate-from-physical-first-jet.md).

If the image is an irreducible cubic, its equation is (2.1).
The point
$$
P=[X:Y:L]=[0:1:0]
$$
is smooth because the $X$ derivative there is $6h_2\ne0$.
In its local chart $Y=1$, the coordinate $L$ is a local parameter
and $X$ has order exactly three: the line $X=0$ meets the cubic
only at $P$, with multiplicity three.

If $\ell\ne0$, the physical point $t$ maps to $P$ without a
basepoint. Its $L$ coordinate is its own physical polar and has
self order at least two. This contradicts the order-one local
parameter at a smooth point of the cubic normalization.
Hence $\ell=0$.

Let $m$ be the self order of $p_0$ at $s$.
If $m=2$, the common divisor of the three polars at $s$ has exact
order one: $p_1$ has order one and $p_L$ at least two.
After dividing, $s$ maps to $P$ but its $X$ coordinate has order one,
contradicting the just proved order three.
If $m\ge3$, the common divisor at $s$ has order at least two;
it has at least one further order at the different point $t$,
because $k=\ell=0$. Its total degree would be at least three.
A cubic image of three quintics instead has common degree exactly
two and covering degree one. This is again impossible.

Every alternative for (2.1) has been excluded.

## 3. Triple block with order-one annihilator

Choose the local parameter with $\lambda(u_1)=1$ and
$\lambda(u_0)=\lambda(u_2)=0$. Then
$$
W=\operatorname{span}(u_0,u_2,w),\qquad
v_1=h_1,\quad 2v_2=h_2\ne0.
$$
The complete third tensor is
$$
T_3=X^2(A X-6h_2Z)-6h_LXL^2+4v_LL^3.
\tag{3.1}
$$

If $v_L=0$, exact residual support gives $h_L\ne0$.
Cancelling the physical factor $p_0$ in the highest identity
forces
$$
p_0\mid p_L^2.
$$
The two physical points are distinct.
This contradicts the
[distinct physical polar square-divisibility exclusion](R150-appendix-distinct-physical-value-polars-never-square-divide.md).

If $v_L\ne0$, put $\alpha=h_L/(2v_L)$.
Completing the cube gives the exact identity
$$
T_3=4v_L(L-\alpha X)^3+
X^2\bigl[(A+4v_L\alpha^3)X-6h_2Z-12v_L\alpha^2L\bigr].
\tag{3.2}
$$
The three displayed directions are independent, because the
bracket has nonzero $Z$ coefficient.
The repeated direction $X$ is physical.
The cubed direction $L-\alpha X$ lies in the secant plane of two
different physical points, is not parallel to $X$, and has
catalecticant rank at most two.
The pure
[physical repeated-factor/secant-cube theorem](R150-appendix-no-physical-repeated-factor-secant-cuspidal-companion.md)
excludes this cusp. It includes $\alpha=0$.
Thus both residual coefficient cases are impossible.

## 4. Quadruple block with order-three annihilator

Now $g=4s$ and
$$
W=\operatorname{span}(u_0,u_1,u_2),\qquad v_3=h_3\ne0.
$$
With $X=u_0,Y=u_1,Z=u_2$ and
$$
C=12(v_2-h_2),\qquad D=6(2v_2-h_2),
$$
the complete third tensor is
$$
T_3=A X^3+B X^2Y+C X^2Z+DXY^2+
12h_3XYZ+4h_3Y^3.
\tag{4.1}
$$

Let $p_0,p_1,p_2$ be the value, first and Taylor second polars,
and let their exact orders at $s$ be $(m,m-1,m-2)$.
The two last terms in (4.1) have common order $3m-3$.
Every earlier term has order at least $3m-2$.
Their combined coefficient is the leading coefficient of
$$
4h_3p_1(p_1^2+3p_0p_2).
\tag{4.2}
$$

It never vanishes for the original $K$.
At a generic finite point, put $q=q(s,s)\ne0$.
The leading coefficients of $p_0,p_1,p_2$ are $-q,2q,-q$,
so (4.2) has nonzero coefficient $56h_3q^3$.

At $s=2,-6$, let $b=q_s(s,s)=q_z(s,s)\ne0$.
The three leading coefficients are $-b,b,b$, and (4.2) has
coefficient $-8h_3b^3\ne0$.
The remaining exceptional local data, including infinity, are:
$$
\begin{array}{c|ccc|c}
s&[p_0]_{\rm lead}&[p_1]_{\rm lead}&[p_2]_{\rm lead}
&[(4.2)]_{\rm lead}/h_3\\ \hline
0&5&-32&54&-234752\\
\infty&-1&5&-8&980
\end{array}
$$
Their orders are $(4,3,2)$.
All these values are obtained directly from the unchanged original
matrix; the accompanying verifier checks both the symbolic generic
coefficients and every exceptional contact.

Thus the unique lowest-order contribution to the highest identity
is nonzero. This excludes the entire case (4.1).

## 5. Quadruple block with order-two annihilator

Choose the local parameter so that
$\lambda(u_2)=1,\lambda(u_0)=\lambda(u_1)=\lambda(u_3)=0$.
Now
$$
W=\operatorname{span}(u_0,u_1,u_3),\qquad
v_2=h_2,\quad 2v_3=h_3\ne0.
$$
Write $U=u_3$. The exact full tensor is
$$
T_3=A X^3+B X^2Y+6h_2XY^2-6h_3X^2U+2h_3Y^3.
\tag{5.1}
$$
Put $\alpha=h_2/h_3$ and complete the cube:
$$
T_3=2h_3(Y+\alpha X)^3+
X^2\bigl[(A-2h_3\alpha^3)X+
(B-6h_3\alpha^2)Y-6h_3U\bigr].
\tag{5.2}
$$
The bracket contains the nonzero third-jet direction $U$.
The repeated direction $X$ is physical.
The cubed direction $Y+\alpha X$ is a genuine tangent direction,
has catalecticant rank at most two, and is not parallel to $X$.
The three directions are independent.
The same physical repeated-factor/secant-cube theorem excludes
(5.2), completing the fourth and last local alternative.

## 6. Complete conclusion and exact record

The four pairs in (1.3) exhaust all mean multiplicities three
and four, retaining the full conormal tangent defect.
Each has been excluded by the original highest identity.
No coefficient division was made before its nonvanishing was proved.

Author files:

- [exact tensor and contact verifier](../notes/2026-11-14-rank-one-higher-mean-block-four-space-verify.js);
- [execution record](../notes/2026-11-14-rank-one-higher-mean-block-four-space-verification.json).

The verifier uses actual BigInt polynomial arithmetic to check
all four complete tensor expansions, both cube completions,
the generic original-$K$ contact coefficients and the four
exceptional finite/infinite leading terms.
All fourteen checks passed in code mode.
The local algebra, normalization-fiber arguments and use of the
already proved pure kernel obstructions are proved in the text.

Together with the separate multiplicity-one/two exclusion, this
closes the inside rank-one-mean common four-space.
The complete rank-one essential-three classification can therefore
use the already proved common three-space theorem.
Natural Jacobian powers, higher essential dimension, and the
ordinary Hilbert ISP are not consequences of this local exclusion.
