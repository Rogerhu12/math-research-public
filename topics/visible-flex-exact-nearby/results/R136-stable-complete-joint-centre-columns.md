# R136：完整 W2C 联合中心核的稳定源列表示

2026-11-20. Session `visible-exact-astra-ac637-20261120`, subtask `joint_kernel`.

**Status:** the exact representation and its interval inclusion argument below
are proved. Its source implementation has passed an AST parse only. No new
scientific bound, successful finite gate, or closed isometric family is claimed.
This fills the graph4 implementation gap identified in the preceding HANDOFF;
it does not recompute the completed WPS, WVC or WCTR targets.

Source: `scripts/fourfold_codazzi_collar_dual_feedback_math.py`, class
`CompleteJointCentreColumns`, reached by `complete_weighted_graph_operators`
and `CompleteGraphNorms.complete`. Other mathematical graph definitions,
their target names, the original four Schur blocks and both right-hand sides,
all seven independent ports, and the actual tail inverse remain unchanged.

## 1. The same signed operator

Use the notation of
`results/R133-supplement-joint-centre-Green-kernel-and-complete-collar-cross-terms.md`
(WJK), particularly (JK.7), (JK.13), (JK.14), and (JK.21). The implemented map is

$$
\mathcal H_c=G_f\{M_c+B_{LH,c}F B_c\},
\qquad M_c=(A_{L,c}-D_f)S^{-1},\qquad B_c=B_{HL,c}S^{-1}.
\tag{C1}
$$

It uses the original WVC reference, not WCTR. The low fibre contains all193
coordinates, including the physical mean; the output contains all193 original
root/mean/weighted-outer observations. Both exterior copies of the high centre
coupling have support

$$
K_0=\{(\epsilon,j):\epsilon=0,1,\quad97\le j\le160\},
\qquad \dim K_0=128.
\tag{C2}
$$

The low input and returned low output of the feedback term are supported in
$33\le j\le96$, with both parities. This follows from the actual degree64
centre bandwidth and the absence of a high returned mean row. The direct
$G_fM_c$ term retains the entire low193 fibre; in particular its mean is not
removed by the feedback support observation.

## 2. Exact intermediate high support

Let

$$
K_1=\{(\epsilon,j):\epsilon=0,1,\quad97\le j\le224\},
\qquad \dim K_1=256.
\tag{C3}
$$

In the expression for $F$ between its two exterior $K_0$ projections, every
word has at most three multiplications by $A_c$ (or its diagonal-reference
difference). Primitive kernels, scalar cutoffs and the modal $G_0$ preserve
angular indices; $G_0$ is itself supported in $K_0$. Every $A_c$ multiplication
changes an index by at most64. Consequently a path of length at most three
from an index at most160 to another index at most160 cannot contain an
intermediate index greater than224: the first and last intermediate indices
are each at distance at most64 from their respective exterior endpoint.
For a two-factor word this conclusion is immediate, and a one-factor word
has no intermediate index at all.

Thus inserting the $K_1$ projection at the intermediate stages of the complete
exterior joint kernel is an exact support reduction. It is **not** the
assertion that $A_c$ preserves $K_1$. The complete primal residual may reach288;
the actual family difference may reach416; the true corrected high state is
infinite-dimensional. These three independent scopes, and every graph1--3
receiver norm, are unchanged. The reduction applies only after the two
external $K_0$ contractions in (C1).

## 3. One source point retained as a parameter

Fix a source point $s$. An implementation encloses every such $s$ in one
whole original source panel, rather than replacing $s$ by a quadrature node.
Write $g_s(r)=G_0(r,s)$ on $K_0$. All applications of $G_0$ to ordinary
matrix fields use the existing stable signed prefix/suffix action
`apply_G_to_matrix_field`, with the same reference profiles. They never divide
by a global decaying transfer factor or multiply independently bounded growing
and decaying semiseparable factors.

The body contribution is exactly

$$
F_{bb}(r,s)=
\chi(r)\chi(s)
\left(2-\frac{\chi(r)^2+\chi(s)^2}{2}\right)g_s(r)
 +\chi(r)\chi(s)
 \big[G_0(\chi^2(A_c-D_0)g_s)\big](r).
\tag{C4}
$$

The interior factor in the second term is restricted to $K_0$ because both
adjacent reference Green factors already have exactly that support. This
is WJK's body cancellation before numerical enclosure. The individual
primal/dual residuals keep their cutoff derivatives in their original graphs.

For $s$ on the collar, $chi(s)=0$, so (C4) vanishes identically. For $s$ off
the collar, the kernels $U(r,s)$ and $\mathcal S(r,s)$ of WJK.16 and WJK.19
vanish identically. The implementation uses these support identities to avoid
forming products with an exactly zero factor; it does not omit a small term.

## 4. All five collar terms

Let $\mathcal S=L_cU-P_c$ and let

$$
k_0(r,s)=[\chi'(r)I-\chi(r)(A_c(r)-D_0(r))]
                G_0(r,s)\chi(s).
\tag{C5}
$$

The source-column routine computes

$$
 F_{\rm cross}(r,s)=U(r,s)
   +V(r,s)P_b(s)[I-\chi(s)^2\Pi_0]
   -[P_0\mathcal S_s](r)-[V(k_{0,s}+\mathcal S_s)](r).
\tag{C6}
$$

This is exactly (JK.21). Its four displayed summands contain the five collar
terms in (JK.8), including the full $-VL_cU$ interaction.

When $s$ is on the collar, put $T_s=I+\int_s^c A_c(u)\,du$. Then

$$
 U(r,s)=
 \begin{cases}
  \mathbf1_{s<r}\left[I+\int_s^r A_c(u)\,du\right],&r\le c,\\
  \psi(r)T_s,&r>c,
 \end{cases}
\tag{C7}
$$

and

$$
 \mathcal S(r,s)=
 \begin{cases}
  -\mathbf1_{s<r}A_c(r)\int_s^r A_c(u)\,du,&r\le c,\\
  [\psi'(r)I-\psi(r)A_c(r)]T_s,&r>c.
 \end{cases}
\tag{C8}
$$

The $P_0\mathcal S$ term is obtained by applying $G_0$ to the complete signed
field $\chi\mathcal S_s$ and multiplying its output by $\chi$. The true
$\psi'$ and body $A_c$ transition terms in (C8) remain present.

When $s$ is off the collar, the direct $V$ term in (C6), after its external
$K_0$ restriction, is

$$
\mathbf1_{r\le c}\psi(s)(1-\chi(s)^2)
\left[-I+\int_r^c A_c(u)\,du\right].
\tag{C9}
$$

For either case define, in the ordinary radial pairing,

$$
 t_0=J^*\big[\psi(k_{0,s}+\mathcal S_s)\big],\qquad
 t_1=J^*(A_ct_0).
\tag{C10}
$$

Here

$$
 (J^*f)(r)=\mathbf1_{r\le c}\int_r^R f(u)\,du.
\tag{C11}
$$

Then the last term of (C6) equals $+t_0-t_1$. The integral in (C11) extends
to the actual outer endpoint $R$ both times; the cutoff is applied to its
source in the first integral, not used to change that upper endpoint.
The second integrand is supported on the collar because $t_0$ is, which is
an exact output-support fact. The first integral retains the entire initial
transition. The intermediate field $t_0$ is kept on $K_1$, and $t_1$ is returned
to $K_0$ by the exact support argument in Section2.

Equations (C4), (C6)--(C11) therefore produce precisely the required
$\Pi_0F(r,s)\Pi_0$, with no differentiated head input and no radial derivative
of an enclosure of a coefficient norm.

## 5. Same-point combination and all observations

For the fixed source point, form the ordinary low matrix field

$$
 h_s(r)=B_{LH,c}(r)\,F(r,s)\,B_{HL,c}(s)S(s)^{-1}.
\tag{C12}
$$

It has128 active input columns, which are embedded into their actual positions
in the full low193 input. Apply the complete original $G_f$ to this field.
The source action returns both its whole body field and its full193 atomic
observation values. Finally form

$$
 K_c(r,s)=G_f(r,s)M_c(s)+(G_fh_s)(r),
\quad
 K_c^{\rm atom}(s)=G_f^{\rm atom}(s)M_c(s)+(G_fh_s)^{\rm atom}.
\tag{C13}
$$

Only after these signed additions are complete does `complete_schur` take
entrywise magnitudes. The factors $S(s)^{-1}$, $S(r)$, nonzero-mode $\sqrt2$
normalization, and outer $H^{-5/6}$ Riesz weights all belong to their original
providers and occur exactly once. The returned zero feedback mean is not
used to remove the direct physical mean or its independent root observation.

## 6. Whole-box interval inclusion

Every coefficient matrix is an enclosure on the entire requested radial box.
For a fixed source panel the source parameter $s$ ranges over the entire
panel throughout (C4)--(C13). When a source and evaluation box overlap, the
Green kernel is enclosed by the hull of its two ordered triangles. A collar
Heaviside factor is enclosed by the hull of its zero and ordered values.
The ordered primitive uses the actual possible nonnegative interval length,
including the genuine enclosed root. Thus no uncertain root endpoint is
substituted for the true root.

Multiplication and addition preserve inclusion for the same underlying
values; correlations that the interval implementation forgets can only widen
the resulting enclosure. Ordinary integrals use signed whole-box ranges
times directed length intervals. Stable modal integrals use their proved
positive signed-mass ranges and signed coefficient ranges. These operations
therefore enclose all exact columns of (C13). No norm bound of a summand is
subtracted from another norm bound.

The final continuous-plus-atomic Schur test is identical to the original
full componentwise test, except that its loops traverse source panels first.
Body terms receive the correct source and observation panel lengths; atomic
rows receive source length but no fictitious atom length. Both row and
column sums cover all193 coordinates with the original strictly positive
comparison weights. The square root of the complete maximal row/column
ratio product bounds the same whole operator in (C1).

Only one source-panel column is retained at a time. Each stage consists of
fixed-width128 or256 matrix fields and stable prefix/suffix states. There is
no semiseparable factor whose rank grows with the expression DAG, and no
full radial-by-radial kernel array. This is a structural storage reduction;
runtime and numerical sharpness still require the first actual public run.

### Executable storage and loop structure

The actual comparison partition has153 original parents, already including
the eight subpanels per doubling band, plus at most two cutoff joins. Thus
$N\le155$ in this backend. The24480 original finite reference cells remain
part of the same mathematical comparison but are not this kernel's loop
index. No partition or mathematical domain is coarsened by this distinction.

The original generic symbolic kernel builder is now retained only as
`_uncompressed_joint_operator_graph`. The scientific entry point builds the
bounded-width column interface directly. This also avoids eager zero endpoint
matrices that the generic integral constructors would otherwise allocate with
their accumulated factor ranks, even before their first numerical evaluation.

The $A_{10}$ and $B_{LH}$ matrices are cached once per original coefficient
parent. The provider encloses its coefficient by the same whole-parent hull
on every subbox, so this cache key does not change any enclosure. The
$A_{00}$ submatrix shares the corresponding $A_{10}$ scalar objects. At the
maximum155-panel count these two complete caches contain at most
$155(256\cdot128+128\cdot128)=7,618,560$ scalar slots; the actual parent cache
has only153 keys. The other centre views need only small caches. In particular,
$A_{01}$ is used only on the collar, and $A_{11}$ is needed only for the one
collar source panel.

Since $J^*$ has output only on the first collar panel, its implementation keeps
one complete body-tail integral and the current collar partial integral.
It does not keep155 suffix matrices. Exact zero-support information may skip
a source panel; the mathematical integral still extends to $R$. The second
$J^*$ source is exactly zero off the collar, and the first source is exactly
zero where $\psi=0$. No small nonzero term is removed.

The stable $G$ action caches belong to one source-panel closure. They are
released before the next source panel. The common reference profile cache
depends only on mode and radial box, not on the source-panel history.
For128 source columns and155 radial panels, the high action uses at most
about7.64 million forcing/full-integral/boundary scalar slots; the low action,
including its independent mean, uses about11.52 million. Together with the
fixed coefficient caches these are about26.8 million scalar slots, plus
small matrices and the shared reference profiles. They grow linearly with
$N$ in peak storage, not quadratically with the number of source panels.
This count does not assert a measured byte footprint or running time.

The full componentwise Schur sum still covers every one of the
$155^2\cdot193^2=894,907,225$ possible body entries. To avoid repeated Python
scalar validation and weighted arithmetic at each entry, the fixed
python-flint backend forms one directed entrywise absolute-upper matrix per
tile, then performs the weighted row and column contractions as native
`arb_mat` matrix-vector products. The Python loop thereafter has193 entries
per tile. All weights and lengths are taken at their proper directed
endpoints. Finiteness is checked on every resulting nonnegative weighted
row and column; a nonfinite absolute entry cannot cancel in such a sum.
`arb.abs_upper()` returns an exact floating-point upper bound rounded upward,
as specified in the [python-flint0.9.0 Arb documentation](https://python-flint.readthedocs.io/en/stable/arb.html#flint.arb.abs_upper).
This changes the arithmetic organization only; it does not replace the
complete signed kernel by a separate-term triangle bound or weaken the
finite gate.

## 7. Verification and unchanged obligations

The modified source was parsed with Python `ast.parse`; no numerical package
or scientific function was executed locally. No old target was reevaluated.
The current graph still owes its three new row/column/norm outputs and the
subsequent complete finite comparison. Existing failed sufficient gates
remain failed and do not prove singularity. The complete positive/negative
physical inverse, true parameter Schur condition, nonlinear iteration and
matching, and the final exact closed fixed-metric family remain separate
unpaid obligations.
