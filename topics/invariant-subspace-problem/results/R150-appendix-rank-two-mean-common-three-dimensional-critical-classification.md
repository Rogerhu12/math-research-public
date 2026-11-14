# R150 appendix — rank-two means with a common three-dimensional support

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved** for the original complete cubic critical system.

## 1. The common-space theorem

Let $y,H,V$ be the original six-mode physical Hankel tensors, let
$T_3=y^3-6yH+4V$, and suppose
$$
\operatorname{rank}\operatorname{Cat}(y)=2,\qquad
\operatorname{ess}(T_3)=W,\quad \dim W=3.
$$
Assume in addition that all three tensors are supported on $W$.
Then
$$
\nabla\mathcal Q_3=0
\quad\Longleftrightarrow\quad
W\in\{W_+,W_-\}\ \text{ and }\ Q_\pm\mid T_3|_W.
\tag{1.1}
$$
In particular all three original matched first Bell cubics vanish.

The new point is that $W$ need not initially be a physical jet
space. No nonsecant hypothesis is used in the two-dimensional
residual argument below. A common space of dimension four is not
covered by this theorem.

## 2. The exact support dichotomy does not require a nonsecant mean

The Hankel matrix $H$ and the first flattening of $V$ have ranks at
most three. The binary apolar argument in §6 of
[the common-jet appendix](R150-appendix-length-three-common-jets-and-inside-mean-critical-dichotomy.md)
gives unique minimal physical divisors $D_H,D_V$ of those lengths,
including the empty divisor for a zero tensor.

For completeness, their degree-ten and degree-fifteen moment
functionals have symmetric apolar Hilbert functions. If $r=b_5\le3$
and $a$ is the first nonzero relation degree, monotonicity after $a$
and symmetry give
$$
a=b_{a-1}\ge b_5=r\ge b_{d-a+1}=a.
$$
Thus $a=r$, the degree-$r$ relation is unique up to a nonzero scalar,
and division and the local decomposition give the exact divisor.
Every top local coefficient is nonzero.

Put $C=D_H\vee D_V$. Its length is initially at most six. All its
jets lie in $W$, while any physical jets of total length at most six
are independent. Hence $\deg C\le3$.

If $\deg C=3$, $W=E_C$ and the hypothesis that $y,H,V$ share this
physical divisor is fulfilled. The
[rank-two common physical length-three classification](R150-appendix-rank-two-mean-common-length-three-physical-critical-classification.md)
proves (1.1).

Otherwise essential dimension three forces
$$
\deg C=2,\qquad U=E_C,\qquad y\notin U,\qquad W=\mathbb Cy\oplus U.
\tag{2.1}
$$
The rest of the proof treats (2.1). In fact it does so for every
nonzero $y\notin U$, without a condition on its catalecticant.

## 3. The rank-free residual block identities

Use the basis $y$ followed by a physical basis of $U$, with dual
variables $t,x_1,x_2$. Then
$$
T_3=t^3-6tH(x,x)+4V(x,x,x).
\tag{3.1}
$$
The exact possible Hankel forms are
$$
\begin{array}{ll}
C=s_1+s_2:&
H=h_1x_1^2+h_2x_2^2,\quad V=v_1x_1^3+v_2x_2^3;\\
C=2s:&
H=h_0x_1^2+2h_1x_1x_2,\quad
V=v_0x_1^3+3v_1x_1^2x_2.
\end{array}
\tag{3.2}
$$
Their essential supports together equal $U$; their separate ranks
may decrease.

Write
$$
K|_W=\begin{pmatrix}2F&l^{\mathsf T}\\l&G\end{pmatrix}.
$$
The original Hankel identity gives $\operatorname{tr}(GH)=0$.
The complete second gradient is the vanishing on the physical
projection of the quadratic
$$
N=T_{3,Ky}-F T_2+4HKH.
$$
Its exact blocks are
$$
N_{00}=F,\qquad N_{0U}=-2(Hl)^{\mathsf T},\qquad
N_{UU}=-2FH+4V_l+4HGH.
\tag{3.3}
$$
The coefficient along $y$, independent of $U$, in the complete
mean gradient is
$$
F^2-2l^{\mathsf T}Hl+2\operatorname{tr}((GH)^2)=0.
\tag{3.4}
$$
These are contractions of (3.1) and the full original gradients.
They use only the direct sum (2.1), not the rank of the mean.
Their detailed derivation is also displayed in §§2–5 of
[the isotropy appendix](R150-appendix-inside-mean-critical-support-is-isotropic.md).

## 4. The residual common space is totally isotropic

The physical image is either an irreducible conic or an irreducible
cubic, by the highest-moment projection theorem.

In the cubic case there is no nonzero quadratic relation, so $N=0$.
Equation (3.3) gives
$$
F=0,\qquad Hl=0,\qquad V_l+HGH=0.
\tag{4.1}
$$
If $H$ is invertible, these give $l=0,G=0$.
If its rank is at most one, (3.2) says that $H$ is zero or a scalar
square of a physical point, hence $HGH=0$.
Then $Hl=V_l=0$ and the exact union of their supports is $U$, so
$l=0$.

For two distinct supports and rank at most one $H$, at least the
other support has a nonzero $V$ coefficient. Evaluating the highest
identity at the first support gives $4v_2 k_{12}^3=0$, hence $G=0$.
For a double jet, rank at most one means $H=h_0x_1^2$ and exact
union support requires $v_1\ne0$. If the tangent self-pairing were
nonzero, the value and tangent polars would have orders two and one,
while $l=0$ makes the mean polar have order at least two.
The term $12v_1p_0^2p_1$ in the highest identity would be the unique
term of order five. Thus that self-pairing is zero, again giving $G=0$.

For a conic image, factor (3.1) with its $t^3$ coefficient normalized:
$$
T_3=(t-A)\,Q,\qquad
Q=t^2+At+A^2-6H,\qquad 4V=-A^3+6AH.
\tag{4.2}
$$
Here $A$ is a linear form on $U$. The conic is nondegenerate.

The matrix $H$ has rank two. If it were zero, $T_3=t^3-A^3$ would
have at most two essential variables. If it had rank one at two
distinct supports, take $H=h_1x_1^2$ and
$A=a_1x_1+a_2x_2$. Essential dimension three requires $a_2\ne0$;
the forbidden mixed coefficients of $V$ give
$a_2(a_1^2-2h_1)=a_1a_2^2=0$, a contradiction.
For a double jet, the absent $x_2^3$ coefficient forces $A$ along
$x_1$, again leaving only two essential variables.

Put $d=A^{\mathsf T}H^{-1}A$. The same mixed coefficient conditions
in (3.2) give $d=0$ or $4$: for two distinct points either $A=0$ or
both $a_i^2=2h_i$; for a double jet $A$ is along the value direction
and the corresponding entry of $H^{-1}$ is zero.

Since $N$ is a quadratic relation and its $t^2$ coefficient is $F$,
$N=FQ$. Comparison of blocks and contraction of (4.2) give
$$
Hl=-\frac F4 A,\qquad s=A^{\mathsf T}l=-Fd/4,
$$
$$
4HGH=(s+2F)(AA^{\mathsf T}-2H).
\tag{4.3}
$$
Taking the trace after multiplication by $H^{-1}$ yields
$$
0=\frac F{16}(8-d)(d-4).
$$
For $d=0$ this gives $F=0$. For $d=4$, (4.3) gives
$l^{\mathsf T}Hl=F^2/4$ and $\operatorname{tr}((GH)^2)=F^2/2$.
Equation (3.4) then gives $3F^2/2=0$. In both cases (4.3) implies
$l=G=0$.

We have proved, in every rank-free residual case,
$$
K|_W=0,\qquad W=W^{\perp_K}.
\tag{4.4}
$$

## 5. Conic images give the two original physical planes

The physical projection of a maximal isotropic $W$ has a common
zero divisor equal, including multiplicities, to its intersection
with the physical curve. The divisor contains $C$, of length two.
A conic image has common divisor degree one or three; it must
therefore have degree three.

Its three independent physical jets lie in $W^{\perp_K}=W$, so
$W$ is a physical length-three space. The original isotropic jet
classification gives $W=W_\pm$.

## 6. The rank-free cubic residual is empty

For a cubic image, (4.4) instead gives an exact common divisor of
degree two, namely $C$. After dividing by it, the three polars
$
P=p_y/G_C,\quad A=p_0/G_C,\quad B=p_1/G_C
$
are independent binary cubics with no common zero, and they give
the normalization of an irreducible cubic. Their equation is exactly
(3.1) with (3.2).

We record why the published original-kernel exclusions apply here
without their earlier nonsecant-mean starting hypothesis. Their
elimination hypotheses are precisely (3.1), (3.2), (4.4), the exact
intersection divisor $C$, and independence of $P,A,B$. All have
just been proved without a mean-rank assumption.

For $C=2s$, isotropy gives $s=0,2,-6,\infty$.
At $0,\infty$ both physical cubics $A,B$ vanish at $s$; the highest
equation then forces $P(s)=0$, a forbidden common zero.
At $2,-6$, the value cubic is respectively
$$
-(z-2)(3z^2-17z+6),\qquad (z+6)(5z^2+65z+66).
$$
Each has three different roots. The highest equation modulo $A$
is $P^3=0$, forcing $P$ to be proportional to $A$, again impossible.
This is the entire argument of
[the double-jet residual exclusion](R150-appendix-inside-mean-double-jet-residual-exclusion.md).

For two distinct points, the same equation is
$$
P^3-6P(h_s A^2+h_t B^2)+4(v_s A^3+v_t B^3)=0,
\qquad (h_i,v_i)\ne(0,0).
\tag{6.1}
$$
The proofs in
[the reduced-polar appendix](R150-appendix-inside-mean-reduced-support-and-simple-polars.md)
use only isotropy, the exact simple intersection divisor, and (6.1).
They exclude $0,2,-6,\infty$ as support points and prove that $A,B$
are coprime squarefree cubics. In particular this deduction imposes
no further rank on $y$.

Finally every irreducible rational plane cubic is singular.
The pure cubic-polynomial calculation in
[the interior-node appendix](R150-appendix-inside-mean-interior-node-exclusion.md)
excludes every singular point with three nonzero coordinates for
(6.1) and the original two physical cubics. A singular point with
zero mean coordinate either makes the cubic reducible or makes
$(h_i,v_i)=(0,0)$ at one support. The only remaining type is, after
permutation and scaling, $[1:0:1]$. Its parametrization forces
$$
C_{22}(A,B)=J(A,B)^2,\qquad C_{13}(A,B)=0.
$$
The exact original-kernel resultants in §§3–4 of
[the complete inside-support appendix](R150-appendix-inside-mean-complete-critical-support-classification.md)
exclude these identities for every remaining support pair:
the two displayed integer elimination factors have coprime
quotients, with the separate $s=-1$ chart also having a nonzero
resultant. Those calculations concern only the two physical
cubics, their coefficients, and the singular point; neither $P$
nor $y$ is subject to a catalecticant-rank premise in them.

Thus these are the same already proved algebraic contradictions
under their full actual hypotheses. We have explicitly supplied
the previously nonsecant-dependent support and isotropy deductions
by §§2–4, rather than assuming their broader applicability.
The cubic residual is empty.

## 7. Sufficiency, matched values, and remaining scope

Necessity of $W=W_\pm$ is now proved for every common
three-dimensional support with rank-two mean.
The full ordinary-moment functional generated by $y,H,V$ through
degree six is supported on $W$, so
[the original isotropic-plane criterion](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)
gives the converse and the complete condition in (1.1).
It also gives the vanishing of all three original matched Bell values.

The argument has not assumed that every rank-two-mean critical point
has a common three-dimensional support. The common dimension-four
case remains a separate task, as do lower mean rank, higher essential
dimension of $T_3$, natural Jacobian powers, and the operator inverse.
