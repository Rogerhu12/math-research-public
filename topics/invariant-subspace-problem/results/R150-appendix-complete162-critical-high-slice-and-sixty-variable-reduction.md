# The complete 162-coordinate critical high slice and its 153-by-60 reduction

Author: Astra-ISP-789f / literature_audit, with GPT-6 Astra Pro.
Date: 2026-11-16.

This note specifies the exact source-level reduction used by the accompanying
number-field consumer. It does not assume that a residue kernel lifts.

Fix one of the actual characteristic-zero fields defined by $F_+$, $F_-$ or
$E_8$, and write the original seventeen equations in the paid co-moving
coordinates as
$$
F_i=q_i d^2+\sum_{j=2}^{10}(L_{ij}+cC_{ij}+dD_{ij})n_j
       +\sum_{2\leq j\leq l\leq10}Q_{i,jl}n_jn_l.
$$
Every coefficient is taken from the original physical generator. Products and
dual values use ordinary monomials. In particular, a symmetric matrix $T$
records the value on $n_jn_l$ directly; its diagonal is not divided by two.

The complete high matrix has all 6018 source rows with a nonempty normal
multiplier and all 4266 complementary target coordinates. The low complement
is all 170 pure-multiplier rows and the 101 target coordinates consisting of
the twenty pure coordinates and the eighty-one one-normal coordinates whose
$d$ exponent is at most one.

## 1. Exact equations on the declared support

Consider the 162-coordinate support
$$
d^2u\cdot n+cd^2v_c\cdot n+d^3v_d\cdot n,\qquad
T_0+cT_c+dT_d,
$$
where the second expression denotes the dual values on ordinary two-normal
monomials. Thus $u,v_c,v_d$ each have nine entries, and each $T$ is a symmetric
nine-by-nine matrix.

For the source multipliers $n_j$, $cn_j$ and $dn_j$, the complete original
products give respectively
$$
LT_0+CT_c+DT_d+qu^T=0,\qquad
LT_c+qv_c^T=0,\qquad
LT_d+qv_d^T=0.
$$
These are all the potentially nonzero high-source rows on this support.

Indeed, a one-normal source with tangent degree two produces no retained
one-normal or two-normal coordinate. A source with at least two normal
factors meets the pure term only in tangent degree at least two, whereas the
retained two-normal coordinates have tangent degree at most one. Its linear
and quadratic terms have normal degree at least three and are also absent.
This checks all original source sectors, rather than merely the displayed
459 equations. The consumer nevertheless multiplies the constructed columns
by all 6188 original rows and verifies that the last 6018 vanish.

## 2. Genuine reduction to sixty variables

The original matrix $L$ has the paid exact rank eight and kernel $Kv_0$.
The consumer solves $Lz=q$ using an actual eight-by-eight unit and verifies
all seventeen equations. It also checks that $v_0,z$ are independent. These
are characteristic-zero gates; the residue calculation does not supply them.

Suppose these gates pass. If a symmetric $T$ satisfies $LT+qv^T=0$, then every
column of $T$ belongs to $\operatorname{span}(v_0,z)$. Symmetry therefore gives
$$
T=a\,v_0v_0^T+b(v_0z^T+zv_0^T)+c\,zz^T,\qquad
v=-bv_0-cz.
$$
The reverse implication follows by multiplying by $L$ and using $Lv_0=0$ and
$Lz=q$. It holds on diagonal coordinates as well: the mixed symmetric tensor
has diagonal $2(v_0)_jz_j$, while an independently specified diagonal entry
of $T_0$ is an ordinary monomial value with no extra factor.

Apply this formula separately to $(T_c,v_c)$ and $(T_d,v_d)$. The only
remaining unknowns are the 45 ordinary symmetric entries of $T_0$, the nine
entries of $u$, and the three coefficients of each of $T_c,T_d$. The first
displayed equation is then exactly a 153-by-60 linear system over the
original number field.

The reconstruction is injective: the first 54 coordinates recover $T_0,u$,
and the independence of $v_0,z$ makes their three symmetric tensors
independent. Thus the exact kernel of this small system parametrizes the
entire declared 162-coordinate slice, without discarding its zero-leading
parameters.

## 3. When the slice becomes the complete high kernel

The independently verified complete residue matrix has rank 4259. Its
whole-row rational scalings and prescribed residue place give the valid
characteristic-zero bound
$$
\dim_K\ker H\leq4266-4259=7.
$$
If the small system produces seven independent characteristic-zero columns
and all 6018 original high-source products vanish, they form the complete
kernel of $H$. No lifting of finite-field kernel coordinates occurs.

If fewer than seven columns are obtained, the consumer reports only their
actual span and the upper bound seven. It does not assert completeness or a
new local Smith connection.

Once completeness is paid, the remaining constant return is the original
170-by-101 low block together with the seven original high returns. The
subsequent Taylor connection still requires this entire low equation and
the original lower cochain terms.
