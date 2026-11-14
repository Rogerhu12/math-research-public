# R740 — Even valuations of the actual finite toric norms

Date: 2026-11-14. Status: **proved**.

This result concerns the original finite factor $N_h$ in R588/R727.
It proves an exact assertion in characteristic zero, rather than lifting
the square congruence of R727 to higher powers of $p$.
It does not yet assert that the original period product
$P_h=S_{2,h}S_{3,h}/C_0^2$ has even valuation.

## 1. Statement and fixed original objects

Let $p\ge41$, $p\equiv5\pmod6$, and $n=p+1$.
Let $h$ be a primitive positive label:

$$
1\le h<n,\qquad h\equiv1\pmod6,\qquad (h,n)=1.
\tag{740.1}
$$

Use the same character, split vector, period basis, and CM torus as R727:

$$
\theta_h(y)=[y]^{-h(p-1)},\qquad
G(e_r,e_s)=p\delta_{rs}-1,
$$
$$
\mathsf T=\mathsf T_\zeta
=\left\{
\begin{pmatrix}a&-b\\ b&a+b\end{pmatrix}:(a,b)\ne(0,0)
\right\}/\mathbf F_p^\times,
\qquad
A_{\mathsf T}=\frac1{p+1}\sum_{t\in\mathsf T}t,
$$
$$
u_h=A_{\mathsf T}e_0,\qquad
N_h=G\left(e_0,\sum_{t\in\mathsf T}te_0\right)
=(p+1)G(u_h,u_h).
\tag{740.2}
$$

The torus and split vector are transported together if the period basis
is changed; this proof never replaces the original pair by a different one.

For the selected $p$-adic embedding, there are an actual stable
$\mathbf Z_p$-lattice $L_h$ in the original finite representation,
a primitive generator $w_h$ of $L_h^{\mathsf T}$, and $c_h\in\mathbf Z_p\setminus\{0\}$
such that

$$
u_h=c_hw_h,\qquad G(w_h,w_h)\in\mathbf Z_p^\times.
\tag{740.3}
$$

Consequently

$$
\boxed{
N_h=(p+1)c_h^2G(w_h,w_h),\qquad
v_p(N_h)=2v_p(c_h)\in2\mathbf Z_{\ge0}.
}
\tag{740.4}
$$

The proof identifies the nondegenerate quotient of a concrete Gram
lattice modulo $p$. It requires neither an assumed self-dual old
Hodge lattice for $\theta_h$ nor a claim about an unspecified
Jordan–Hölder constituent.

## 2. The original finite representation is orthogonal over $\mathbf Q_p$

Let $\mathcal G=\mathrm{PGL}_2(\mathbf F_p)$, and let $V_h$ be the
primitive cuspidal representation in the R727 left-module model.
Its dimension is $p-1$; the vectors $e_r$, $r\in\mathbf F_p$, have the
single relation $\sum_re_r=0$. The upper Borel acts by affine
permutations, and the Weyl matrix is

$$
we_r=-\frac1p\sum_{y\in\mathbf F_{p^2}^{\times}}
       \theta_h(y)e_{r\operatorname N(y)+\operatorname{Tr}(y)}.
\tag{740.5}
$$

The character values are in the unramified quadratic extension of
$\mathbf Q_p$. Its Frobenius sends $\theta_h(y)$ to
$\theta_h(y)^p=\theta_h(y)^{-1}$.
The substitution $y\mapsto y^p$ preserves every norm/trace fiber.
Thus each coefficient of (740.5) is fixed by this Frobenius and lies
in $\mathbf Q_p$. Together with the rational Borel matrices this
defines $V_h$ over $\mathbf Q_p$.

The same substitution shows that the matrices are real in the
complex coefficient field. The invariant Hermitian form of R727
therefore becomes the invariant symmetric bilinear form $G$ displayed
in (740.2). Its extension to $\mathbf Q_p$ is nondegenerate on $V_h$.
We retain this form itself, without multiplying it by a
possibly nonunit scalar.

There is one useful elementary dimension check. For $t\in\mathsf T$,
$t\ne1$, choose a nonscalar lift with eigenvalues $\lambda,\lambda^p$.
The actual character of (740.5) satisfies

$$
\operatorname{Tr}(t\mid V_h)
=-\theta_h(\lambda)-\theta_h(\lambda)^{-1}.
\tag{740.6}
$$

For completeness, this follows directly from the displayed model.
Write a representative $g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$,
$c\ne0$, and $\Delta=ad-bc$. Its Bruhat decomposition gives, before
quotienting by $\sum e_r$, the matrix

$$
e_r\longmapsto-\frac1p\sum_y\theta_h(y)
e_{\frac{\Delta}{c^2}((r+d/c)\operatorname N(y)+\operatorname{Tr}(y))+a/c}.
\tag{740.7}
$$

This matrix kills the constant vector, so its trace is the trace
on $V_h$. If $\operatorname N(y)\ne c^2/\Delta$, there is exactly
one fixed $r$. The resulting partial sum is zero: the total
character sum is zero, and so is the sum on
$\operatorname N(y)=c^2/\Delta$, because the primitive character is
nontrivial on $\mu_{p+1}$. In the exceptional norm fiber all $p$
values of $r$ are fixed exactly when

$$
\operatorname{Tr}(y)=-c(a+d)/\Delta.
$$

Its two elements are $-c/\lambda$ and $-c/\lambda^p$.
Since $\theta_h$ is trivial on $\mathbf F_p^\times$, this proves
(740.6). Every nonidentity element of the original $\mathsf T$
has $c\ne0$, so no case is omitted.

The primitive nontrivial character on $\mathsf T$ has total sum zero.
Averaging (740.6), with $\operatorname{Tr}(1\mid V_h)=p-1$, yields

$$
\dim_{\mathbf Q_p}V_h^{\mathsf T}
=\frac{(p-1)-(-1)-(-1)}{p+1}=1.
\tag{740.8}
$$

## 3. An actual stable integral Gram lattice

R727 (727.15)–(727.16) proves, from the original Weyl matrix, that

$$
G(e_0,ge_0)\in\mathbf Z_p\qquad(g\in\mathcal G).
\tag{740.9}
$$

The denominator $1/p$ in (740.5) cancels against the $p\delta_{rs}$
part of $G$; the remaining constant part vanishes because
$\sum_y\theta_h(y)=0$. This proves integrality for the one Bruhat
cell, while the Borel case is immediate.

Define the orbit lattice

$$
L_h=\sum_{g\in\mathcal G}\mathbf Z_p\,ge_0\subset V_h.
\tag{740.10}
$$

The group is finite, so this is a finitely generated
$\mathbf Z_p$-module. It spans $V_h$; indeed the affine translates
of $e_0$ already give all $e_r$.
It is torsion-free, of rank $p-1$, and is $\mathcal G$-stable.
Invariance and (740.9) give

$$
G(ge_0,g'e_0)=G(e_0,g^{-1}g'e_0)\in\mathbf Z_p.
\tag{740.11}
$$

Hence $G(L_h,L_h)\subset\mathbf Z_p$.
The lattice is not assumed to be self-dual. Its reduction may have
a large radical, and the next sections treat that radical explicitly.

Put $k=\mathbf F_p$, $\overline L_h=L_h/pL_h$, and let
$\operatorname{Rad}\overline G$ be the radical of the reduced pairing.

## 4. Exact identification of the Gram quotient

Set

$$
h_0=\min(h,n-h),\qquad r=h_0-1.
\tag{740.12}
$$

Since $h$ is primitive and odd, the midpoint $h_0=n/2$ is impossible.
Thus $r$ is even and

$$
0\le r\le(p-3)/2,\qquad 2r<p-1.
\tag{740.13}
$$

Replacing $\theta_h$ by its inverse leaves every matrix in (740.5)
unchanged, again by $y\mapsto y^p$. Consequently we may use
$\theta_{h_0}$ for the finite model without changing $V_h$, $G$,
$e_0$, or $\mathsf T$. This is only an equality of finite matrices;
it does not change the positive cubic marking in the original
period formulas.

The full R727 fiber identity, valid for every odd $1\le h_0<p$,
gives

$$
G(e_0,ge_0)\bmod p
=-P_r\!\left(\frac{ad+bc}{ad-bc}\right),
\quad
g=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\tag{740.14}
$$

Consider the explicit $k[\mathcal G]$-module

$$
S_r=\operatorname{Sym}^{2r}(k^2)\otimes\det^{-r},\qquad
v=X^rY^r.
\tag{740.15}
$$

The central scalars act trivially, so this really is a
$\mathcal G$-module. With $E_i=X^{2r-i}Y^i$, its invariant
symmetric form is

$$
B(E_i,E_j)=
\begin{cases}
(-1)^i/\binom{2r}{i},&i+j=2r,\\
0,&i+j\ne2r.
\end{cases}
\tag{740.16}
$$

This is the usual contraction from the alternating determinant
pairing on $k^2$; the twist $\det^{-r}$ on each factor cancels the
factor $\det^{2r}$ of the contraction.
All the binomial coefficients are nonzero in $k$, by (740.13),
so the form is nondegenerate. Also $B(v,v)\ne0$.
Normalize

$$
b=-B/B(v,v).
\tag{740.17}
$$

The middle coefficient of
$(aX+cY)^r(bX+dY)^r\Delta^{-r}$ shows

$$
\begin{aligned}
b(v,gv)
&=-\Delta^{-r}\sum_{j=0}^{r}
  \binom rj^2(ad)^j(bc)^{r-j}\\
&=-P_r\!\left(\frac{ad+bc}{\Delta}\right).
\end{aligned}
\tag{740.18}
$$

The second equality is the elementary binomial expression for
the Legendre polynomial. It is a polynomial identity after
multiplication by $\Delta^r$ and is valid also when $ad$ or $bc$
vanishes.

We record why the orbit of $v$ spans $S_r$. In fact $S_r$ is
irreducible over $k$. The diagonal subgroup has distinct weights
on $E_0,\ldots,E_{2r}$ because $2r<p-1$. Projecting to a diagonal
weight, any nonzero submodule contains a monomial. Applying one
unipotent subgroup and interpolating its polynomial in its
parameter, of degree at most $2r<p$, gives $X^{2r}$; applying the
opposite unipotent subgroup gives every monomial. The relevant
binomial coefficients are units. This also covers $r=0$.
Thus $k[\mathcal G]v=S_r$.

Let the free module $k[\mathcal G]$ map onto $\overline L_h$ by
$[g]\mapsto\overline{ge_0}$ and onto $S_r$ by $[g]\mapsto gv$.
For every pair $g,g'$ the two Gram entries agree, by invariance,
(740.14), and (740.18).

If $\sum a_g\overline{ge_0}=0$, pairing with all
$\overline{g'e_0}$ shows that $\sum a_ggv$ is orthogonal to
every $g'v$. Nondegeneracy and the orbit-spanning statement imply
$\sum a_ggv=0$. Therefore there is a well-defined surjection

$$
\varphi:\overline L_h\twoheadrightarrow S_r
\tag{740.19}
$$

sending $\overline{ge_0}$ to $gv$.
The same Gram identity proves that its kernel is exactly the
radical, not merely a submodule of it:

$$
\boxed{
\overline L_h/\operatorname{Rad}\overline G
\ \simeq\ (S_r,b)
}
\tag{740.20}
$$

as a module with nondegenerate pairing.

## 5. The torus line survives the radical

Because $|\mathsf T|=p+1$ is a unit in $\mathbf Z_p$,
$A_{\mathsf T}$ is an integral idempotent on $L_h$.
Thus

$$
L_h^{\mathsf T}=A_{\mathsf T}L_h
$$

is a direct summand. By (740.8) it has rank one, and reduction
commutes with invariants:

$$
(L_h^{\mathsf T})/pL_h^{\mathsf T}
=(\overline L_h)^{\mathsf T},\qquad
\dim_k(\overline L_h)^{\mathsf T}=1.
\tag{740.21}
$$

There is exactly one invariant line in $S_r$ as well.
Over $k_2=\mathbf F_{p^2}$, diagonalize the nonsplit torus.
If its two eigenvalues are $\lambda,\lambda^p$, the
$\det^{-r}$-normalized weights are

$$
(\lambda/\lambda^p)^{\,r-i},\qquad 0\le i\le2r.
\tag{740.22}
$$

As $\mathsf T$ varies, $\lambda/\lambda^p$ runs through
$\mu_{p+1}$. The integer exponents range from $-r$ to $r$,
with $2r<p-1<p+1$. Only the exponent zero is divisible by
$p+1$. Hence $\dim_{k_2}(S_r\otimes k_2)^{\mathsf T}=1$,
and descent gives $\dim_k S_r^{\mathsf T}=1$.

The averaging idempotent makes taking $\mathsf T$-invariants
exact in characteristic $p$ too. Applying it to (740.19) gives

$$
0\longrightarrow
(\operatorname{Rad}\overline G)^{\mathsf T}
\longrightarrow(\overline L_h)^{\mathsf T}
\longrightarrow S_r^{\mathsf T}
\longrightarrow0.
\tag{740.23}
$$

Both right-hand spaces have dimension one. Therefore

$$
(\operatorname{Rad}\overline G)^{\mathsf T}=0.
\tag{740.24}
$$

Let $w_h$ generate the free rank-one module $L_h^{\mathsf T}$.
Its reduction is nonzero and spans
$(\overline L_h)^{\mathsf T}$, because that module is a direct
summand. Suppose $G(w_h,w_h)\equiv0\pmod p$.
For every $\bar x\in\overline L_h$, invariance gives

$$
\overline G(\bar w_h,\bar x)
=\overline G(\bar w_h,A_{\mathsf T}\bar x).
\tag{740.25}
$$

The vector $A_{\mathsf T}\bar x$ is a multiple of $\bar w_h$,
so the right side is zero. Thus $\bar w_h$ would belong to
$(\operatorname{Rad}\overline G)^{\mathsf T}$, contradicting
(740.24). This proves the unit assertion in (740.3).

## 6. Exact even valuation and the remaining period question

Since $u_h=A_{\mathsf T}e_0\in L_h^{\mathsf T}$, write
$u_h=c_hw_h$ with $c_h\in\mathbf Z_p$. The factor $N_h$ is
nonzero: the finite formulas make it a cyclotomic conjugate
of $N_1$, and R727 at $h=1$ gives $N_1\equiv-1\pmod p$.
Consequently $c_h\ne0$.

The averaging operator is self-adjoint for $G$ and idempotent.
Thus $G(e_0,u_h)=G(u_h,u_h)$, proving the final equality in
(740.2). Substitution now proves (740.4). In particular, if
$N_h\equiv0\pmod p$, then $v_p(N_h)\ge2$; if a retained
calculation only gives $N_h\equiv0\pmod{p^4}$, this theorem
alone does not distinguish $4,6,8,\ldots$.

The distinction from the original $M_2$ is essential. The actual
norm and tame phase of R727 remain

$$
\frac{M_{2,h}^2}{\zeta^2}
=-\frac{8N_hC_0^2}{(p+1)^2}P_h,\qquad
P_h=\frac{S_{2,h}S_{3,h}}{C_0^2}.
\tag{740.26}
$$

Since all displayed fixed factors except $N_h$ and $P_h$ are
$p$-adic units,

$$
2v_p(M_{2,h})=v_p(N_h)+v_p(P_h).
\tag{740.27}
$$

When $P_h\ne0$, (740.4) shows that $v_p(M_{2,h})$ is an integer
if and only if $v_p(P_h)$ is even. No assertion about that
second parity is proved here. In particular, this result does
not by itself improve the deep-disc threshold in R737, prove
that the two selected $C$ coefficients are units, or exclude
the original height zeros.

## Sources and dependencies

- R727 §§3–5: the original finite model, integral Weyl pairings,
  the full fiber identity, and the unchanged torus/split marking.
- R588 and R727 §2: the original $N_h$, $C_0$, and $M_{2,h}$ norm
  with its tame phase.
- The Gram-quotient and torus-line arguments above are direct
  proofs in the finite model. For related characteristic-$p$
  matrix coefficients, see U. K. Anandavardhanan,
  [Simultaneous nonvanishing of the correlation constant](https://arxiv.org/pdf/2507.14616),
  §§2–3. This paper is not used to infer the higher $p$-adic
  valuation assertion from a modulo-$p$ square.
