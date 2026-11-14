# R133: consuming the whole cap into the true cut

The original public cap run `43583838015` completed all 1,977 true closed
cells and the unchanged final boundary/Green consumer. The new small
consumer takes its original complete native SHA256
`69f55939742b26988690e54b7f5636eb591a351063b93187feeb38c1f6611ebe`,
the original complete local trial-Hessian native `cf055cac...`, and the
original complete moving cut native `528e2f47...`. No residual row or
large trial array is recomputed.

The physical full-parameter cap bound is
`epsilon_cap < 1.127829e-4`. The separately established trial-sensitive
Hessian bridge gives, at the actual affine centre only,

$$
e=\frac{\epsilon_{\rm cap}+E_H(T)}{1-\chi}.
$$

The new producer pays this number into all three complete cut outputs:
the 96 low odd rows, the independent mean row, and every unretained
moving odd output. Their errors are respectively

$$
\eta_J=\eta_{J,T}+\|\mathcal S\|e,\qquad
\eta_M=\eta_{M,T}+e,\qquad
\eta_H=\eta_{H,T}+\|\mathcal S\|e.
$$

It keeps the whole-parameter physical certificate separate from the
actual-moving bridge's `eta=eta0` scope. All unknown high inputs and
independent ordinary, divergence, regular and mean source columns remain
separate complete operator contracts.

## Directed complete finite boundary checks

In the original orthonormal moving basis the true low boundary is
`B=[I,J;0,M]`, with 97 rows and 193 columns. Subtracting `e` from the
directed true-trial zeroth mean entry gives a strictly positive lower
bound `m_*` for `|M_0|`. The exact right inverse that first sets
`x_0=g_mean/M_0`, all other even input coordinates to zero, and then
solves the odd identity has norm bounded by the Euclidean norm of

$$
\begin{pmatrix}1&\|J e_0\|/m_*\\0&1/m_*\end{pmatrix}.
$$

This is a construction of an independent-data right inverse, not a
deletion of the other 96 even input columns. It proves that the true low
boundary has rank 97 and a 96-dimensional kernel.

Let `Q` denote all 193-by-96 original saved binary64 frame entries,
interpreted as exact dyadic numbers, and set
`P=Q(Q*Q)^(-1)Q*`. The producer multiplies the complete matrices in
320-bit Arb arithmetic. If

$$
\delta=\|Q^*Q-I\|_F<1,\qquad
\eta_B=(\eta_J^2+\eta_M^2)^{1/2},
$$

then

$$
r:=\frac{\|\widehat BQ\|_F+\eta_B\sqrt{1+\delta}}
 {\sqrt{1-\delta}}\ge\|BP\|.
$$

If `l` bounds the explicit right inverse above, then
`sigma_min(B)>=1/l`. Because
`B(I-P)B*=BB*-BPB*`, the full 97-row restriction to the exact
orthogonal complement has

$$
\sigma_{\min}(B|_{\operatorname{ran}(I-P)})
 \ge\sqrt{l^{-2}-r^2}.
$$

A positive radicand pays the actual complete right-boundary rank gate of
the continuous projector theorem. Its inverse norm is at most the
reciprocal of this lower bound, and the corresponding right feedback is
at most that inverse norm times `r`. Equal dimensions also give a
true-low-kernel projector gap at most `l r`.

These are finite *low-row* facts. The exact kernel is not asserted to
annihilate the separately retained moving high output. No continuous
body inverse or global high feedback is inferred from the boundary
rank. The next coordinate change by a radial weight must transform both
this boundary and the full frame, then pay its own Gram and norm fees.

## Actual execution protocol

The new public workflow downloads only the 17.97 MB complete-result
artifact, not the 767 MB large preparation. The pinned input manifest
contains seven source files and two original native inputs. Both the
original mathematical child exits and the complete native identity are
checked before the new calculation. All exact outcomes, including a
failure, are retained in the new process; a complete result requires all
14 new gates to pass. Before submission only source parsing, the seven
source hashes, the workflow YAML and its manifest hash were checked
locally. The new directed arithmetic gates run in this public
repository's Actions.
