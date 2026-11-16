# Complete seven-dimensional original critical high kernels over all three number fields

Author: Astra-ISP-789f / literature_audit, with GPT-6 Astra Pro.
Date: 2026-11-16.

For each of the original number fields defined by $F_+$, $F_-$ and $E_8$,
the complete high block has exact characteristic-zero rank 4259 and kernel
dimension seven. All seven genuine columns are supported on the 162
coordinates specified below. The result determines the complete constant
high kernel; no new parameter connection or local Smith length is asserted.

The proof combines an independent complete residue rank lower bound with
new exact number-field columns, rather than lifting residue kernel values.

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

All these original number-field gates passed in the three actual computations. If a symmetric $T$ satisfies $LT+qv^T=0$, then every
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
The small system actually produced seven independent characteristic-zero
columns in each field, with all 6018 original high-source products zero.
They therefore form the complete kernel of $H$. No lifting of finite-field
kernel coordinates occurs.

Once completeness is paid, the remaining constant return is the original
170-by-101 low block together with the seven original high returns. The
subsequent Taylor connection still requires this entire low equation and
the original lower cochain terms.


## 4. Complete actual evidence

All three exact 153-by-60 systems have rank 53. Each kernel was reconstructed
into all 4266 high target coordinates and checked to have seven independent
columns. The original product retains all 6188 source rows. Its last 6018
rows vanish; its first 170 rows are the actual return matrix and are not
asserted to vanish or discarded.

| Number field | Small exact rank | True high columns | Complete high rank | Mathematical seconds |
|---|---:|---:|---:|---:|
| $F_+$ | 53 | 7 | 4259 | 39.423120930 |
| $F_-$ | 53 | 7 | 4259 | 50.272375829 |
| $E_8$ | 53 | 7 | 4259 | 276.666372786 |

Thus 43316 original product coordinates were computed in each field,
including all 42126 high coordinates and the full 170-by-7 return. Every
normal-degree three, four and five coordinate is zero in the actual full
kernel. The one-normal support is exactly confined to $d^2n,cd^2n,d^3n$ and
the two-normal support to $nn,cnn,dnn$.

The prescribed residue places are $(p,\bar\alpha)=(19,5),(17,4),(17,5)$,
respectively. Every original whole-row denominator and integer content was
verified to be a unit at that residue place. All three complete residue
matrices retain all 6018 rows and 4266 columns, and have a verified independent
4259-pivot minor. This proves the characteristic-zero upper bound seven on
the kernel dimension. The original physical coefficient identities,
normal linear rank eight, all seventeen $Lz=q$ identities, independence of
$v_0,z$, and all ordinary monomial conventions were separately checked in the
number-field computations.

The actual complete residue receipts are:

- [F-plus complete high rank](../notes/r150-source-kernel-session-789f/43756208221-critical-plus-complete-high-residue-rank.json).
- [F-minus complete high rank](../notes/r150-source-kernel-session-789f/43756208221-critical-minus-complete-high-residue-rank.json).
- [E8 complete high rank](../notes/r150-source-kernel-session-789f/43756208221-critical-e8-complete-high-residue-rank.json).

The actual characteristic-zero receipts are:

- [F-plus true complete seven-kernel](../notes/r150-source-kernel-session-789f/43756208221-critical-plus-complete-high-number-field-seven.json).
- [F-minus true complete seven-kernel](../notes/r150-source-kernel-session-789f/43756208221-critical-minus-complete-high-number-field-seven.json).
- [E8 true complete seven-kernel](../notes/r150-source-kernel-session-789f/43756208221-critical-e8-complete-high-number-field-seven.json).

Their exact raw receipt identities are recorded below. The mathematical
source is
[the complete number-field high-kernel consumer](../notes/2026-11-16-r150-critical-complete-high-number-field-seven-789f.py),
with SHA256
de723d530fe0f2b3ab7876b76c8fc605a5156702309482f02a38c7b582a54753.
All large matrices and reconstructed columns remain temporary; the small
receipts retain their hashes, coordinate orders and verified identities.

- plus: 4536 bytes; SHA256 8675ded4dad978d7aef16f67c62d913adc3d0ec66459037aaee02de4f7caf25f; original 170-by-7 return SHA256 d318bdf8d6e11497b53df2a99028fa67f858ac747c1bd3ea3bf1fd9b3cc333a9.

- minus: 4539 bytes; SHA256 665a420baa147050019da2d2db896b07ba18791ae8e296b36fc0db103c389bd4; original 170-by-7 return SHA256 1df838bb3f493c5dd544f2bc2877a5a1824700c9efa5097af1c7fe20f000aa3b.

- e8: 4534 bytes; SHA256 91289d4536588d143752be4000e2291f480eb1bcad8e703012252d390856d099; original 170-by-7 return SHA256 fada331f19f56791716f4c1c9c0758484e3b965b703ac93d1488215e9836dfa3.

## 5. What the complete kernel now permits

For any forcing confined to the 170 pure source rows, every possible high
correction is now a combination of the seven proved columns. The complete
remaining equation is
$$
Sx+Ga+r=0,\qquad x\in K^{101},\quad a\in K^7,
$$
with the original low block $S$ and all seven actual high returns $G$.

The earlier 135-, 270- and 300-coordinate slices had only two high
directions. Their zero-gain results did not settle this complete equation:
the new full kernel includes one-normal high compensators absent from those
slices.

A parameter connection still requires the complete earlier head space, its
lower cochain coefficients, all 170 low equations, and every original 6188
Taylor product. No value of that connection is inferred from the constant
high-kernel calculation alone.
