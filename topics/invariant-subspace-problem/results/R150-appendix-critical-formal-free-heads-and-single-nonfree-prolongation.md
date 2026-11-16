# The original critical free heads and a single nonfree positive prolongation

Author: Astra-ISP-789f / literature_audit, with GPT-6 Astra Pro.
Date: 2026-11-16.

This note proves the two algebraic facts used by the next positive-certificate
consumer. It asserts no new numerical connection rank or local length.

Work over the actual number field $k=\mathbb Q[\alpha]$ associated with one
of $F_+,F_-,E_8$, put $t=s-\alpha$, and let $R=k[[t]]$. Every map below is
the original seventeen-equation map, with all degree-at-most-three source
multipliers and all nonconstant target monomials of degree at most five.

## 1. The thirteen formal-free leading directions

The previously verified original low map $S(t):R^{36}\longrightarrow R^{51}$
has generic rank 27, constant rank 25, and positive Smith exponents $(e,e)$,
where $e=3$ for the two cubic fields and $e=2$ for the octic field.
The six identically zero low columns are restored in the actual 36-column
representation. This is the complete original low map, not the quadratic
high-support ansatz.

Since its target is free, $\ker S$ is saturated in $R^{36}$. The quotient
$R^{36}/\ker S$ is isomorphic to the torsion-free module $\operatorname{im}S$,
which is free over the DVR $R$. Thus the kernel is a direct summand of rank
nine, and its reduction modulo $t$ has dimension nine.

The actual constant-unit recursion retains eleven independent low leading
heads, and its first nonzero residual at order $e$ has rank two. Its
nine-dimensional residual kernel is exactly the reduction of $\ker S$:
every formal kernel element lies in that residual kernel, and both spaces
have dimension nine. Consequently these nine leading directions admit
infinite formal lifts in the original low coordinates.

The low embedding is a polynomial identity in the original physical
equations: outside its 51 rows, all original source products vanish.
Therefore these are also genuine formal kernels of the full 6188-source
map. The additional four pure directions are exact original kernels.
The actual original leading vectors of these nine plus four directions
are independent. The full original generic corank is thirteen, so these
thirteen directions exhaust the reductions of full formal kernels.

For completeness, the full formal kernel is also a saturated direct
summand of the free 4367-coordinate dual domain, by the same argument.
Thus the phrase "all formal-free leading directions" includes the
reduction assertion; it is not merely a statement about generic dimension.

The first-exit consumer retains the nine low exit-null columns, two
independent exit axes, and the four pure directions separately. Its actual
spanning identity expresses all eleven residual columns through those
two axes, and its full leading-rank check retains their independence.
Any surviving linear combination with nonzero coordinates on those two
exit axes is therefore outside the thirteen-dimensional formal-free
leading space.

These inputs and the exact all-source checks are in:

- [Complete critical high kernels](R150-appendix-complete-critical-high-kernels-seven-in-all-three-number-fields.md).
- [Original weak low-jet generator](../notes/2026-11-16-r150-critical-weak-quadratic-positive-jets-789f.py).
- [Complete first-exit consumer](../notes/2026-11-16-r150-critical-complete-first-exit-789f.py).

## 2. Why one further positive chain can suffice

Suppose the complete first exit at order $e$ has rank one. The full
constant corank is fifteen and the generic corank is thirteen, so exactly
two positive Smith directions exist. Since all earlier full connections
are zero, one positive exponent is exactly $e$, and the other is at least
$e+1$.

Take the surviving head with nonzero exit-axis coordinates from Section 1.
A genuine cochain
$$
\lambda(t)=\lambda_0+t\lambda_1+\cdots+t^{e+1}\lambda_{e+1},
\qquad
A(t)^T\lambda(t)=O(t^{e+2}),
$$
with that same leading head forces the remaining positive exponent to be
at least $e+2$. Indeed, in Smith coordinates a head outside the free
subspace can survive through this order only in a positive direction
whose exponent is at least $e+2$. The direction of exponent $e$ is already
excluded at the first exit.

For either cubic field this gives total positive length at least
$3+5=8$. Together with the previously paid upper bound eight, it gives
the exact spectrum $(3,5)$. This is a conditional conclusion: the new
cochain and every original source product must actually be verified.
Failure of a restricted correction ansatz is not a full negative
connection result.

For the octic field, a rank-one first exit at $e=2$ would already give
length at least five, hence exact spectrum $(2,3)$ under its paid upper
bound five. No further extension is needed for that branch.

## 3. The genuine first derivative of the quadratic coefficients

Let $\Phi$ be the exact monic minimal polynomial of $\alpha$. The original
physical quadratic coefficients are rational polynomials in $s$.
Their construction uses the fixed rational inverse of $J_3$ and polynomial
operations on the original moment, Hankel and polarization tensors. It
does not invert a polynomial in the parameter.

Compute this same physical expression in
$$
\widetilde R=\mathbb Q[s]/(\Phi(s)^2).
$$
For each resulting coefficient $q(s)$, define
$$
q_0=q(s)\bmod\Phi,\qquad q_1=q'(s)\bmod\Phi.
$$
Both are well-defined independently of the chosen representative in
$\widetilde R$: if representatives differ by $\Phi^2H$, their derivatives
differ by $2\Phi\Phi'H+\Phi^2H'$, which vanishes modulo $\Phi$.
Consequently
$$
q(\alpha+t)=q_0+tq_1+O(t^2).
$$
There is no missing factorial in the first coefficient.

The consumer must compare every $q_0$ with the already paid original
quadratic constant, and compare both values and first derivatives of
all original pure and linear coefficients with their independently
generated 26-coefficient parameter polynomials. Its use of derivatives
is only an exact coefficient calculation; no closure of the original
ideal under differentiation is assumed.

At the next page, the previously constructed leading chain has normal
degree at most one before order $e$, and degree at most two at order $e$.
Thus its forcing at order $e+1$ uses only the genuine quadratic orders
zero and one. Higher quadratic orders must not be filled with zeros;
the action routine must reject any product that would need an uncomputed
quadratic order.

## 4. A finite positive correction ansatz with complete verification

Write the actual original constant equations as
$$
F_i=q_i d^2+(L_i+cC_i+dD_i)n+Q_i(n,n).
$$
Seek a high correction supported on the same 162 coordinates as the
complete constant high kernel:
$$
d^2u\cdot n+cd^2v_c\cdot n+d^3v_d\cdot n,\qquad T_0+cT_c+dT_d.
$$
For a prescribed high right-hand side supported on the original
$n_j,cn_j,dn_j$ source rows, the equations are
$$
LT_c+qv_c^T=Y_c,\qquad
LT_d+qv_d^T=Y_d,\qquad
LT_0+CT_c+DT_d+qu^T=Y_0.
$$
They are ordinary-monomial equations. Diagonal dual values of a symmetric
tensor are not halved.

The actual identities $Lv=0$ and $Lz=q$, with $L$ of rank eight, allow the
first two equations to be solved through the original eight-unit block
and a symmetry system of size $36$ by $18$. Their homogeneous symmetric
solutions are generated by $vv^T,vz^T+zv^T,zz^T$, with the corresponding
one-normal corrections $0,-v,-z$. The remaining equation uses the
already paid 153-by-60 system and its genuine rank-53 unit.

Any successful particular solution must be multiplied through all 6018
original high source rows, not merely the 459 possibly nonzero rows.
Its homogeneous ambiguity is the complete seven-column high kernel
already proved. The low equation then retains all seven high returns
and both original exit residuals, together with their genuine shifted
cochains and the original 86-column low unit.

The resulting full chain is accepted only after checking every original
6188 source at every order and preserving its nonfree leading head.
No solution in this support means only that this positive-certificate
ansatz did not supply a prolongation.
