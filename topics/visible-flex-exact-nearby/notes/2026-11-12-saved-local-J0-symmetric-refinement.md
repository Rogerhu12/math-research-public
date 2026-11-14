# Saved first integrals recover the exact symmetric local J0 term

Date: 2026-11-12. This note proves the transformation used by
[scripts/fourfold_saved_first_local_J0_symmetric_ci.py](../scripts/fourfold_saved_first_local_J0_symmetric_ci.py).
Its numerical report must be read separately: the identity alone does not
assert an improved numerical bound or R31 acceptance.

## 1. Exact local identity and the sign of the bracket

Work in the same normalized label $x$ and normalized local time $u\in[-1,1]$
as the saved density leaves. The signed physical time halfwidth is already
included in every coefficient. For the exact finite density
$g(u,x)=\sum_{i=0}^{m}g_i(x)u^i$, put

$$
G(x)=\int_{-1}^{1}g(u,x)\,du
    =2\sum_{\substack{e\ge0\\e\ {\rm even}}}\frac{g_e(x)}{e+1},
\qquad
J(x)=\int_{-1}^{1}g_x(u,x)\int_{-1}^{u}g(v,x)\,dv\,du .
$$

The coefficient of $g'_m g_n$ in $J$ is exactly

$$
c_{mn}=\frac{I_{m+n+1}-(-1)^{n+1}I_m}{n+1},
\quad
I_j=\begin{cases}2/(j+1),&j\ {\rm even},\\0,&j\ {\rm odd}.\end{cases}
$$

Odd/odd terms vanish, even/even terms sum to $G'G/2$, and the two mixed
orders have opposite signs. Thus

$$
J=\frac12G'G+
\sum_{\substack{e\ {\rm even}\\o\ {\rm odd}}}
\frac{2}{(e+o+2)(e+1)}
\bigl(g'_o g_e-g'_e g_o\bigr). \tag{1}
$$

This agrees with the ordered integral in
[fourfold_parameter_ordered_defect.py](../scripts/fourfold_parameter_ordered_defect.py)
and its rational coefficient `chronological_weight(m,n)`.
For a real trigonometric polynomial, $G'G/2=(G^2)'/4$ has exactly zero mean.
The implementation checks that the interval product encloses zero and then
uses this identity for its mean. It retains every other product frequency,
up to twice the degree of $G$.

## 2. The removable part is a component of a positive budget

For positive-frequency rows with exact negative conjugates, define

$$
\|f\|_\sigma=|f_0|+2\sum_{k=1}^{K}|f_k|e^{k\sigma}.
$$

The audited density kernels computed the local fee by the explicit
positive expression

$$
B_{\rm old}\ge
\frac12U_0U_1+
\sum_{e\ {\rm even},\,o\ {\rm odd}}
\frac{2}{(e+o+2)(e+1)}
\left(U(g'_o)U(g_e)+U(g'_e)U(g_o)\right), \tag{2}
$$

where $U_0\ge\|G\|_\sigma$, $U_1\ge\|G'\|_\sigma$, and every $U$ is a directed
upper bound. The original function returns the upper endpoint of this
whole positive sum. Before using (2), the script verifies the original
source SHA and compares the Python abstract syntax trees of
`coefficient_norms` and `first_integral_and_local_second_bound` with the
reviewed composition-v9 kernel. A different formula remains unrefined.

The saved first-integral coefficient balls enclose the same complete $G$.
The lower endpoint of each complex absolute-value ball bounds from below
the magnitude of every enclosed coefficient. Weighted sums, rounded
downward, therefore give

$$
0\le L_0\le\|G\|_\sigma,\qquad
0\le L_1\le\|G'\|_\sigma.
$$

The omitted bracket sum in (1) consequently has norm at most

$$
B_{\rm bracket}\le
\operatorname{up}\left(B_{\rm old}
              -\operatorname{down}(L_0L_1/2)\right). \tag{3}
$$

Indeed $L_0L_1/2\le U_0U_1/2$, an explicitly identified component of the
positive budget (2). This argument does not subtract the norm of a computed
term from a bound on the norm of a potentially cancelling sum.

All endpoints in (3) use Arb; decimal ball records are read outward.
Correction coefficients remain full complex balls, with their radii present
for any later midpoint selection.

## 3. The complete flow allows a partially refined set of leaves

Let $C_1$ and $C_2^{\rm cross}$ be the original complete first integral and
all ordered cross-leaf second integrals. For any verified subset
$\mathcal M$ use

$$
\widetilde C_2=C_2^{\rm cross}
             +\sum_{j\in\mathcal M}\frac12G'_jG_j.
$$

Starting with the original whole-flow local fee $B$, the new fee is

$$
\widetilde B=
\operatorname{up}\left(B-
 \sum_{j\in\mathcal M}^{\rm downward}L_{0,j}L_{1,j}/2\right). \tag{4}
$$

Every unprocessed leaf keeps its full previous fee. Missing native scientific
files, unsupported formulas, or absent saved integrals are explicitly listed;
none is treated as zero.

All true-minus-finite source fees, chronological terms of order at least
three, exact partitions and fixed-reference data remain unchanged. The new
finite polynomial and new fee must be used together.

The report proves a transformation of the previously verified complete flow
index. It does not claim to revalidate every geometric dependency. Its
original index is

`data/phase_ring_continuation/step5_complete_flow_ci_43301401638/g0/index.json.gz`

with SHA256

`4174c3edde41f5c8ab12b036d4760c20ec987e475158aa2855ea08158ff7cb45`.

The complete accumulator SHA, every processed leaf and first integral SHA,
the finite-density coefficient SHA, and generating source SHA are checked
and retained.

## 4. Joining the actual parameter endpoint

The center and hybrid chronological builders retain center $2J_{11}$ but
their zeroth local terms are zero. Before applying the present correction,
a caller must verify that both builders use exactly the same ordered g0
witnesses as the original complete g0 index and the expected original
zeroth polynomial and fee.

It may then add the correction to $D_0$ and subtract the verified removed
budget from the zeroth local fee, keeping parameter rows 1 and 2 and their
old fees. R86 permits separate finite approximations to the three true
parameter derivatives; the finite approximations need not themselves form
a differentiable finite family.

The builders record these per-leaf witnesses. An explicit checked extension
must consume the new correction; changing an old report's source identity
would not justify its acceptance by the original endpoint loader.

R31 still needs the corrected finite endpoint, actual finite
reparameterization residual, all true errors, parameter movement and its
other gates. Equations (1)--(4) alone do not establish acceptance.

## 5. Reproduction

From the topic directory:

`python -u scripts/fourfold_saved_first_local_J0_symmetric_ci.py --materialize`

The native helper checks out only tracked exact dependency paths. Its output
directory is `data/phase_ring_continuation/step5_local_J0_symmetric_ci/`,
containing full coefficient balls, report and file manifest. The small
summary is `notes/2026-11-12-ci-local-J0-symmetric-summary.json`. The workflow
preserves these original bytes before terminal Git publication.

## 6. First actual computation

Run `43306162239` completed successfully, using Python 3.12.14,
python-flint 0.9.0 and 256-bit arithmetic. The transformation itself took
27.17 seconds. Native Git preserved the original output bytes in commit
`7165eec6cea549b6e56d3961e61797bdce6e6827`.

Of the 555 original leaves, 330 had the exact required scientific files in
the checked-out snapshot; the other 225 retained their full fees.
Directed bounds give

$$
B_{\rm old}<5.001013\cdot10^{-15},\qquad
\widetilde B<2.459203\cdot10^{-15}.
$$

The sum of explicitly removable budget components was greater than
$2.5418097\cdot10^{-15}$. The complete added correction has
$A_{3/1024}$ norm less than $3.480705\cdot10^{-16}$.
All infinite source errors and chronological tails remain paid.

The full report SHA256 is
`f77211c4d7710dae2a737558ceae980c4d780666d4f91f2a730004981802d301`;
the complete coefficient file SHA256 is
`27d9815a2c0ae5d23b6825b0a978a920db1fb8af005f6e9423da394950320834`.
The summary records every remaining dominant leaf and the original file
identities. The remaining fee is concentrated in segments 280--293; the
largest individual remainder is segment 287, below $5.690041\cdot10^{-16}$.
The still unchanged 225 leaves contributed only about $1.997\cdot10^{-18}$
to the old total.

This computation does not meet the required R31 accuracy by itself.
The next actual refinement will retain the full local ordered integral of
the dominant leaves, including their signed brackets.

Immediately after both native pulls, the workflow compared the root and
topic READMEs. Both differences were empty at read main commits
`ec923bbd107798cdf1cf87cee14ece957c8363b4` and
`426636142ef197916ab12036a2610465d07b8305`; those log entries were read and
the latter was recorded in HANDOFF.
