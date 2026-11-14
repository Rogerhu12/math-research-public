# R150 appendix — a rank-one outside mean with third-cumulant support at most four has zero third moment

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved for the complete original critical equations**.

## 1. Statement

Let $y=a v(s)\ne0$ be a physical rank-one mean.
Let $H,V$ be the original physical Hankel cumulants, and write
$$
T_3=y^3-6yH+4V,\qquad W=\operatorname{ess}(T_3).
$$
Assume complete original criticality and
$$
\dim\operatorname{ess}(V)\le4,\qquad y\notin W.
$$

**Theorem.**
$$
\boxed{T_3=0.}
\tag{1.1}
$$
Equivalently, a nonzero third tensor in this third-cumulant
range must have its mean inside its essential space.

This is a restriction on $\operatorname{ess}(V)$, not on a
presupposed common space for all three cumulants.
All physical jet multiplicities, vanishing lower coefficients
and infinity are retained.

## 2. The only possible nonzero case has an exact disjoint four-divisor

Suppose for contradiction that $T_3\ne0$.
The
[zero-centered-linear-section theorem](R150-appendix-rank-one-mean-zero-centered-linear-section-has-zero-third-tensor.md),
combined with the highest two-variable argument, already
shows that a rank-one-mean nonzero critical third tensor has
essential dimension at least four.

Choose a covector $\lambda$ with
$$
\lambda|_W=0,\qquad\lambda(y)=1,
$$
and put $j=I-y\lambda$.
Applying $j$ to all three factors of $T_3$ gives
$$
T_3=4j^{\otimes3}V.
\tag{2.1}
$$
Thus its essential dimension is no larger than that of $V$.
It follows that both dimensions are exactly four, and that
$j$ is injective on $\operatorname{ess}(V)$.
In particular
$$
y\notin\operatorname{ess}(V).
$$

The exact finite binary apolar theorem for a Hankel cubic
of essential dimension four gives its unique physical
length-four divisor $R$.
Its four jets span $\operatorname{ess}(V)$.
The mean point is not in $R$; otherwise its value would lie
in that space.

Contracting $T_3$ by $\lambda$ gives
$$
V\lambda=\frac12H+yH\lambda-\frac14y^2.
$$
Both $V\lambda$ and $H$ are physical Hankel quadratics.
For physical $y$, the product $yz$ is Hankel exactly when
$z$ is in its physical tangent space $T_s$.
Therefore, setting $z=H\lambda-y/4$,
$$
H\lambda=y/4+z,\qquad
H=2V\lambda-2yz,\qquad z\in T_s.
\tag{2.2}
$$
A second contraction gives
$$
V\lambda^2=
\left(\frac18+\frac{\lambda(z)}2\right)y+z.
\tag{2.3}
$$

The left side belongs to $E_R$, while the right side belongs
to $T_s$.
Since $R$ is disjoint from $s$, the physical divisor $R+2s$
has length six. Its jets are linearly independent, including
at infinity. Hence $E_R\cap T_s=0$.
Equation (2.3) is therefore zero.
It gives $z=-y/12$, and (2.2) becomes
$$
\boxed{
V\lambda^2=0,\qquad
H=\frac16y^2+H_R,\quad H_R=2V\lambda,\qquad
M=H-\frac12y^2=-\frac13y^2+H_R.
}
\tag{2.4}
$$

On the Artin algebra of $R$, the exact top coefficients of $V$
make its local Frobenius pairings nondegenerate.
The zero contraction in (2.4) thus means
$$
\lambda^2=0\quad\text{on }R.
\tag{2.5}
$$
Independence of the four residual physical jets ensures that
no zero contraction is hidden by cancellation between blocks.

If $\lambda=0$ on $R$, then $H_R=0$ and (2.1) says $T_3=4V$.
The original highest map $J_3$ is invertible, so its vanishing
would force $V=0$, a contradiction.
Thus a nonzero square-zero function on $R$ is necessary.
It remains to examine the five possible multiplicity types
of a length-four divisor.

## 3. Complete low-gradient normalization

Weighted scaling permits $y=v(s)$.
The physical mean is disjoint from $R$, so the five directions
consisting of $y$ and the four jets of $R$ are independent.
Their coefficients in the complete mean-gradient vector
can therefore be compared.

Use the unchanged full normalized mean gradient
$$
\Gamma=(F^2-2b+2\tau_2)y-4FHp+8HKHp
       +4V(p,p,\cdot)-8V:(KHK),
$$
$$
p=Ky,\quad F=\frac12y^{\mathsf T}Ky=0,\quad
b=p^{\mathsf T}Hp,\quad\tau_2=\operatorname{tr}((KH)^2).
\tag{3.1}
$$
Complete criticality gives $\Gamma=0$.

The following blocks retain the coefficient $y^2/6$ in (2.4).
Replacing it by a centered or ordinary second moment would
change the crucial factors $8/3$.

## 4. Types $1+1+1+1$, $2+1+1$ and $3+1$

On a reduced algebra every square-zero function is zero,
so type $1+1+1+1$ is already excluded.

For type $2+1+1$, (2.5) makes $\lambda$ zero on both simple
blocks and a multiple of the first nilpotent on the double block.
Let $X,U_1$ be its value and genuine first jet.
Then
$$
H_R=hX^2,
$$
and the coefficient $v_1$ of the exact double block of $V$
is nonzero. The component of (3.1) along $U_1$ is exactly
$$
\Gamma_{U_1}=\frac83v_1\,K(y,X)^2.
\tag{4.1}
$$
Hence $K(y,X)=0$.
The tensor $M=-y^2/3+hX^2$ is now supported on the isotropic
span of these two physical values, so $MKM=0$.

For type $3+1$, a nonzero square-zero function on the triple
block has order two. Thus again $H_R=hX^2$.
Writing its Taylor second jet as $U_2$, the nonzero top
coefficient $v_2$ of $V$ gives
$$
\Gamma_{U_2}=\frac83v_2\,K(y,X)^2.
\tag{4.2}
$$
The same conclusion follows.

At any complete critical point $MKM=0$ forces $T_3=0$ by
the already proved centered zero-section theorem.
This contradicts the present nonzero third tensor and
excludes both multiplicity types.

## 5. Type $2+2$

Let $X,U_1$ and $Z,W_1$ be the two double blocks.
Both top cubic coefficients $v_1,w_1$ are nonzero.
The square-zero condition gives
$$
H_R=hX^2+kZ^2,
$$
where either quadratic coefficient may be zero.
Put
$$
l_1=K(y,X),\qquad l_2=K(y,Z),\qquad g=K(X,Z).
$$
Direct expansion of the complete original vector (3.1) gives
$$
\begin{aligned}
\Gamma_y&=4hk\,g^2,\\
\Gamma_{U_1}&=\frac83v_1l_1^2-8v_1k\,g^2,\\
\Gamma_{W_1}&=\frac83w_1l_2^2-8w_1h\,g^2.
\end{aligned}
\tag{5.1}
$$

If $hk\ne0$, the first equation gives $g=0$, and the other
two give $l_1=l_2=0$.
If $h=0,k\ne0$, the last equation gives $l_2=0$.
If $k=0,h\ne0$, the middle equation gives $l_1=0$.
If both vanish, $M$ is just the physical rank-one tensor
$-y^2/3$.

In every case
$$
M=-y^2/3+hX^2+kZ^2
$$
satisfies $MKM=0$.
Again the centered zero-section theorem contradicts $T_3\ne0$.
No nonvanishing assumption on $h,k$ was omitted.

## 6. Type $4$

Let $X,U_1,U_2,U_3$ be the value and Taylor jets at the
quadruple point. Its exact cubic tensor is
$$
\begin{aligned}
V={}&v_0X^3+3v_1X^2U_1+
3v_2(X^2U_2+XU_1^2)\\
&+v_3(3X^2U_3+6XU_1U_2+U_1^3),
\qquad v_3\ne0.
\end{aligned}
\tag{6.1}
$$
A square-zero function on this block has order at least two.
Consequently
$$
H_R=h_0X^2+2h_1XU_1.
\tag{6.2}
$$
The value $h_1=0$ is allowed.

Set
$$
l_0=K(y,X),\qquad l_1=K(y,U_1),\qquad
g=K(U_1,U_1).
$$
The physical jet identities include
$$
K(X,X)=K(X,U_1)=0,\qquad
K(X,U_2)=-g/2.
\tag{6.3}
$$
From the component of (3.1) along $U_3$,
$$
\Gamma_{U_3}=\frac83v_3l_0^2,
$$
we obtain $l_0=0$.
With that substitution its component along $U_1$ is
$$
\Gamma_{U_1}=\frac83v_3l_1^2,
$$
so $l_1=0$.

The physical mean now pairs to zero with all of (6.2).
Thus
$$
MKM=h_1^2g\,X^2.
\tag{6.4}
$$
If $h_1=0$, this is already zero.
If $h_1\ne0$, the sole remaining potentially nonzero component
of the complete mean vector is
$$
\Gamma_X=8h_1v_3g^2.
\tag{6.5}
$$
It gives $g=0$, and (6.4) is again zero.

For clarity, (6.5) uses the actual Taylor normalization.
After $l_0=l_1=0$, $Hp=0$, $\tau_2=0$ and $V(p,p,\cdot)=0$.
The only surviving contraction in $V:(KHK)$ is
$$
2h_1V(KX,KU_1,\cdot)=-h_1v_3g^2X,
$$
using (6.1) and (6.3).
Multiplication by the coefficient $-8$ in (3.1) gives (6.5).
This proof is local in a genuine projective parameter and
therefore includes a quadruple point at infinity.

The centered zero-section theorem again yields $T_3=0$,
the final contradiction.

## 7. Conclusion and exact author record

Every length-four multiplicity type has been excluded.
Thus the original outside-mean assumptions with
$\operatorname{ess}(V)\le4$ force (1.1).

The accompanying
[exact block verifier](../notes/2026-11-14-rank-one-outside-low-V-blocks-verify.js)
reconstructs the full vector (3.1) for the four nonreduced
types. It checks (4.1), (4.2), all of (5.1), the two successive
jet equations in type $4$, (6.5), and its four other zero
components after the stated substitutions.
All twelve symbolic BigInt identities passed, as recorded
in the [execution receipt](../notes/2026-11-14-rank-one-outside-low-V-blocks-verification.json).

The high-essential-dimension rank-one problem remains open
for outside means with $\operatorname{ess}(V)\ge5$, and for
the inside-mean sections not covered by the previously proved
zero-$A_yM$ theorem.
No general assumption that $MKM=0$ was made in this proof;
it was derived in each allowed residual support type.
