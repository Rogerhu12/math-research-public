# R133 supplement: the actual root inverse in the complete negative window

2026-11-14. **Proved, with 27 actually executed gates.**

The object is the same final complete moving centre
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`,
with all original $|\eta|\le10^{-9}$ and its actual compact metric
parameter. The interval is

$$
 I_\eta=[r_*(\eta),r_*(\eta)+h],\qquad h=9\,10^{-6}.     \tag{W.1}
$$

The [single global positive reference](R133-supplement-global-positive-reference-and-current-collar.md)
already gives an actual full-frequency local inverse, complete mean and
head feedback, in its base Hilbert space. The
[height contact](R133-supplement-residual-sensitive-vector-height-and-Airy-contact.md)
requires a different angular window, and the
[actual regular negative graph](R133-supplement-final-regular-negative-window-and-height-ports.md)
has now paid its exterior side. This proof supplies the actual full root
inverse in that negative window. A positive-order bootstrap alone would
not have supplied it.

The new complete high feedback is below $1/2$. The full 193-coordinate
head/infinite-high feedback is below $.04$. Both actual high incoming
ports, all low Cauchy data, all mean/source columns and both endpoint
outputs remain. This is a local root theorem, not a whole-body inverse
or a global cutoff-97 certificate.

## 1. Exact same reference and weighted spaces

Write the actual moving Jacobi unknown as $h=(h_1,h_2)$; where it could
be confused with the interval length, write its components explicitly.
All functions have physical frequencies $k=4j$. The real reflection
class has odd $h_1$ and even $h_2$. Its head contains 96 sine and 97
cosine coordinates. The allowed even mean stays in that head. The
unrestricted two-state algebra retains both mean rows before the stated
reflection constraint is imposed.

Set $N=97$, $M_0=388$, $P_L={\bf1}_{|j|\le96}$ and
$P_H=1-P_L$. On the nonzero high frequencies use exactly the global
radial Riccati frame of the cited theorem:

$$
 Z_k=M^{1/6}T_M^{-1}(-i\operatorname{sgn}(k)h_{1,k},h_{2,k})^t,
 \quad M=|k|,\quad
 T_M=W_M^{-1/2}\begin{pmatrix}p_M&-g_M\\1&1\end{pmatrix}.\tag{W.2}
$$

The full reference has actual speed $-\gamma m$ on (W.1) and actual
outer backward value $q_*/(-m_R)$. It is the same reference as the new
exterior negative-window graph, not the former short-collar Robin
reference. Outside (W.1), its already stated permitted positive
extension is not asserted to be the uncomputed body operator.

For each real $0\le t\le2$ define the high weight

$$
 w_t(M)=(M_0/M)^t,\quad Y=w_tZ,\quad X_H=w_tP_Hh,
 \quad X_L=P_Lh.                                     \tag{W.3}
$$

The low block has weight one, including mean. Define the source norm

$$
 \mathcal F_t^2=
 \|f_L\|_{L^2_rL^2_\phi}^2+
 \|w_tf_H\|_{L^2_rH^{1/3}_\phi}^2,                    \tag{W.4}
$$

and port norm

$$
 \mathcal G_t^2=
 \|h_L(r_*)\|_2^2+
 \|Y_s(r_*)\|_2^2+
 \|Y_u(r_*+h)\|_2^2.                                 \tag{W.5}
$$

The low data are the complete raw low Cauchy state at the root. The
high data are one stable row at the root and one unstable row at the
right endpoint. These do not impose two zero Cauchy traces followed by
an extra stable condition. The other high rows are outputs and still
participate in the global matching equations.

The claim is the full solution in the Hilbert completion of (W.3):

$$
 \left(\|X_L\|_{L^2}^2+\|X_H\|_{L^2}^2\right)^{1/2}
       <.00018\,\mathcal F_t+.02\,\mathcal G_t,        \tag{W.6}
$$
$$
 \left(\|\operatorname{Tr}X_L\|^2+
              \|\operatorname{Tr}X_H\|^2\right)^{1/2}
       <.06\,\mathcal F_t+8\,\mathcal G_t.             \tag{W.7}
$$

Both traces in (W.7) are the complete pair of endpoints. At $t=5/3$
the high ordinary source in (W.4) has order $-4/3$, with the stated
homogeneous/Bessel comparison, and the high curvature state has order
$-5/3$. Low modes are still present in their explicitly specified norm.
This is not an unqualified source-index improvement. The same two
displayed bounds hold if the high output slot $X_H$ is replaced by the
canonical output $Y$, both for volume and endpoint norms. They are two
separate choices of output, not a claim about their concatenated norm.
Indeed the estimates for $Y$ preceding raw reconstruction are smaller
by a factor three than the sufficient high row used below.

## 2. Complete kernel estimate on every negative order in this window

The actual full high equation in the global frame is

$$
 Z_r=\mathcal D Z+\mathcal B Z+\mathcal E Z+F_Z,
 \quad
 \mathcal D=\operatorname{diag}(-\kappa_M,\kappa_M),
 \quad
 \mathcal B=P_H(d\partial_\phi+d_\phi/2)P_H.            \tag{W.8}
$$

The operator $\mathcal B$ is exactly skew-adjoint in the real-circle
L2 space. The actual complete root fields give

$$
 \|d_\phi\|_{A^0}<54,
 \qquad E_{\rm abs}<17700,                            \tag{W.9}
$$

where $E_{\rm abs}$ bounds the absolute row/column convolution
majorants of the complete matrix kernel $\mathcal E$. This is the
absolute bound (G.22) of the global-reference theorem, rather than its
smaller signed operator bound. It includes the reaction, all frame
differences and the complete primitive nonlocal operator. The exact
mean-rank term has no high-to-high part; its low paths are retained
below.

The entire moving centre has degree 32. Its full Jacobi angular band
is therefore $|j-n|\le64$, including the nonlocal product on both sides
of its primitive. The intermediate primitive index on high input has
absolute value at least $97-32>0$. Both signs remain, but no direct
opposite-sign high entry exists because $2\cdot97>64$.
For any nonzero high kernel entry,

$$
 \frac{\max(|j|,|n|)}{\min(|j|,|n|)}
 \le R:=\frac{161}{97},\qquad R^2<3,\quad2R^3<10.       \tag{W.10}
$$

Consequently, for $0\le t\le2$,

$$
 \|w_t\mathcal E w_t^{-1}\|_2
          \le R^t E_{\rm abs}<3\cdot17700.             \tag{W.11}
$$

The scalar transport must also be conjugated; leaving it skew after
changing weight would be wrong. Its exact Fourier entry is
$\frac{i}{2}(k+l)d_{k-l}$, for signed physical frequencies $k,l$.
Thus the new transport remainder has entry

$$
 \frac i2(k+l)d_{k-l}
       \left[\left(\frac{|l|}{|k|}\right)^t-1\right].  \tag{W.12}
$$

The two frequencies have the same sign here. By integrating the
logarithmic derivative $t$ of $x^t$, and using
$|\log(|l|/|k|)|\le|k-l|/\min(|k|,|l|)$,

$$
 \frac{|k+l|}{2}
 \left|\left(\frac{|l|}{|k|}\right)^t-1\right|
 \le tR^{t+1}|k-l|\le2R^3|k-l|.                      \tag{W.13}
$$

The diagonal case vanishes exactly. Complete convolution now bounds
the operator in (W.12) by $10\|d_\phi\|_{A^0}<540$.
The radial diagonal commutes with the weight. The exact equation for
$Y$ therefore has the same diagonal and same skew $\mathcal B$, with
complete bounded remainder

$$
 E_-<3\cdot17700+10\cdot54=53640,
 \qquad hE_-<.48276<\tfrac12.                         \tag{W.14}
$$

This estimate holds on the whole infinite high space. In particular
it has not assumed that a mode remains high after an intermediate
coefficient multiplication. The already complete kernel and actual
band, not a factorwise truncation, were conjugated in (W.11).

## 3. The complete high inverse and both endpoint outputs

The stable forward and unstable backward realizations of
$\mathcal D+\mathcal B$ have the same energy construction as in the
global-reference theorem. The damping is nonnegative and the scalar
transport remains exactly skew. Fourier Galerkin construction for
dense smooth data, its uniform energy bounds and completion give
the full propagators. There is no finite-section inverse claim.

Their two-port diagonal Green and homogeneous lift satisfy

$$
 \|G_0\|_{L^2_r\to L^2_r}\le h,
 \quad\|P_0\|\le\sqrt h=.003,
 \quad\|\operatorname{Tr}_{\rm out}G_0\|\le\sqrt h.    \tag{W.15}
$$

By (W.14) the genuine Neumann inverse has norm below two. The complete
source and raw reconstruction factors from the same global reference
are below three:

$$
 \|w_tF_Z\|_{L^2}<3\|w_tf_H\|_{L^2H^{1/3}},\qquad
 \|X_H\|_{L^2}<3\|Y\|_{L^2}.                          \tag{W.16}
$$

All these scalar frequency weights commute with the radial frame,
so (W.16) is the actual weighted version of the previously proved
frame estimate. It is not a negative-space consequence of an arbitrary
L2 multiplication bound.

For independent high ports $g_H$, equations (W.15)--(W.16) give

$$
 \|X_H\|_{L^2}<G_H\|w_tf_H\|_{L^2H^{1/3}}+P_H\|g_H\|,
 \quad G_H=18h=.000162,\quad P_H=6\sqrt h=.018.         \tag{W.17}
$$

The outgoing $Y$ port is at most
$2\|g_H\|+2\sqrt h\|w_tF_Z\|$. Combine it with the independent
incoming port in Euclidean direct sum, then reconstruct the raw
weighted state. Since $3\sqrt5<7$, the full two-end trace obeys

$$
 \|\operatorname{Tr}X_H\|
       <.054\|w_tf_H\|_{L^2H^{1/3}}+7\|g_H\|.         \tag{W.18}
$$

Ordinary data on all Fourier modes are allowed. The source in (W.17)
may include the exact head-driven high forcing, which is treated next.

## 4. The 193-coordinate head and every high feedback path

Use the actual unweighted head equation from the original root
theorem. Its complete all-radial Cauchy Green and lift satisfy

$$
 G_L=h(51/50),\qquad P_L^\partial=\sqrt h(51/50).        \tag{W.19}
$$

This is a Gronwall bound on the true coefficient functions, not a
radial collocation assertion. It includes the allowed mean and the
full finite-dimensional source. The raw cross bounds are

$$
 \|\mathcal A_{LH}\|<967,\qquad
 \|\mathcal A_{HL}\|_{L^2\to H^{1/3}}<8658.            \tag{W.20}
$$

On either direct crossing, the involved high indices lie in
$97\le|j|\le160$. Since $w_t\le1$, the high output of the head
forcing costs no more than the second bound in (W.20). Conversely
$w_t^{-1}\le(160/97)^2<3$ on this entire shell, so

$$
 A_{LH}^{(-)}<3\cdot967=2901,
 \qquad A_{HL}^{(-)}<8658.                            \tag{W.21}
$$

This uses the support of the direct operator only. It does not remove
paths from that shell through the high propagation and back to the
whole head. Those paths are the full product below.

The exact coupled system is

$$
\begin{split}
 h_L&=P_L^\partial g_L+G_L(f_L+\mathcal A_{LH}h_H),\\
 X_H&=\mathcal P_Hg_H+
       \mathcal G_H(w_tf_H+w_t\mathcal A_{HL}h_L).
\end{split}                                                   \tag{W.22}
$$

The whole head return has the explicit bound

$$
 \rho=G_L(2901)G_H(8658)
          =.03735278654328<.04.                       \tag{W.23}
$$

A second genuine Neumann inverse closes the complete low/high problem
on the one hybrid Hilbert space. Both formal means before reflection,
the actual even mean, all low nonzero modes and arbitrary ordinary
sources have remained in (W.22). The metric parameter column vanishes
on this root germ because its support ends at .18; its global negative
body, waist and scalar Schur rows have not thereby been removed.

For full detail, let $R_L=(1-\rho)^{-1}$ and define the row

$$
 L=R_L(G_L,\ G_L\,2901\,G_H,\ P_L^\partial,
                         \ G_L\,2901\,P_H).           \tag{W.24}
$$

In input order
$(\|f_L\|,\|w_tf_H\|_{H^{1/3}},\|g_L\|,\|g_H\|)$,
the high row is

$$
 H=(G_H8658L_1,\ G_H+G_H8658L_2,
                  G_H8658L_3,\ P_H+G_H8658L_4).        \tag{W.25}
$$

Their values are bounded outward by

| State | $f_L$ | $w_tf_H$ in $H^{1/3}$ | $g_L$ | $g_H$ |
|---|---:|---:|---:|---:|
| $h_L$ | $.000009536204$ | $.000004481654$ | $.003178735$ | $.000497962$ |
| $X_H$ | $.000013375442$ | $.000168285950$ | $.004458481$ | $.018698439$ |

The exact squared Frobenius bounds for the first two and last two
columns give (W.6). The four positive scalar majorants are used on
orthogonal input summands; this does not assume the actual operators
share eigenvectors.

For completeness, the low right trace has row

$$
 L^{\rm tr}_j=.00306\,{f1}_{j=1}+
       1.02\,{f1}_{j=3}+.00306(2901)H_j,             \tag{W.26}
$$

and its left trace is exactly $g_L$. The full high trace has row

$$
 H^{\rm tr}_j=.054\,{f1}_{j=2}+7\,{f1}_{j=4}
                                  +.054(8658)L_j.     \tag{W.27}
$$

Their exact squared column sums, including the left $g_L$ row,
give (W.7). Thus source-to-trace and all mean outputs are supplied,
not only a volume inverse.

## 5. Exact conversion to the actual height-normalized root ports

The recovered complete current complex germ is now available and is
consumed, with its actual source identity, whole parameter scope and
candidate SHA. Its intrinsic real $a$ and complete moving mean imply
on the entire real root interval

$$
 1.0971086<a<1.0971133,\qquad
 1.1197077<-m<1.1198071.                               \tag{W.28}
$$

These are outward bounds read from the actual Arb enclosures, not
samples and not numbers from the previous amplitude-.75 centre.
Their exact rational consequences are

$$
 .959<n(r):=a(r)^2/m(r)^2<.961,
 \qquad\frac{\sup_I n}{\inf_I n}<1.003.                \tag{W.29}
$$

At $t=5/3$ the vector-height normalization is exactly

$$
 \widetilde Z_k=n(r)M^{-5/3}Z_k
                   ={n(r)\over388^{5/3}}Y_k.          \tag{W.30}
$$

Apply the same positive scalar $n(r)/388^{5/3}$ to the complete low
state and to both parts of the source norm (W.4), and apply its true
endpoint values to each datum (W.5). Multiplication of the already
solved equation's norm estimates, using (W.29), proves

$$
 \|\widetilde X\|_{L^2}
   <.000181\,\widetilde{\mathcal F}
          +.0201\,\widetilde{\mathcal G},\qquad
 \|\operatorname{Tr}\widetilde X\|
   <.061\,\widetilde{\mathcal F}
          +8.03\,\widetilde{\mathcal G}.               \tag{W.31}
$$

The high output in (W.31) may be chosen either as
$n\,388^{-5/3}X_H=nM^{-5/3}h_H$ or as the actual canonical height
state $n\,388^{-5/3}Y=\widetilde Z$. The same stated bound holds for
each choice, by the separate canonical estimate immediately after
(W.7); no inverse raw reconstruction is being assumed. The estimate uses no unproved
bound on $n'/n$. If one writes the equation for the rescaled unknown,
that derivative is present; equivalence to the original solved
equation and the positive value bounds (W.29) pay the norms directly.

At zero frequency the low scaling is a stated scalar convention,
not a limit of $M^{-5/3}$. In particular the genuine mean variable
of the mean-elimination theorem is
$n\langle h_2\rangle=388^{5/3}\widetilde X_{L,2,0}$.
This exact finite conversion remains available in the global Schur
problem. The independent overall height translation and rigid
frame/holonomy ports from the vector-height theorem are still
independent; a curvature inverse does not determine them.

The lower contact rows and weak-source terms from that theorem also
remain. Nothing in (W.30) equates a physical height L2 source with
the unweighted curvature source. Equations (W.4) and (W.31) specify
the precise source spaces used here.

## 6. Execution, fixed-cut restriction and remaining global work

The actual command, from the topic directory, is

```sh
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python3 scripts/fourfold_codazzi_current_root_negative_window.py --out notes/2026-11-14-R133-current-root-negative-window-rational.json
```

It has returned exit 0 and written all 27 successful gates. Native
scalar enclosure comparisons use Arb at 256 bits; every feedback,
source and trace inequality then uses exact `Fraction` arithmetic.
Decimal report fields are upward displays, not inputs to comparisons.
The complete germ, source and proof input SHA256 values are retained.
No whole-body candidate array was needed for this new local budget.

The same estimates restrict to the fixed right cut
$r_b=.2384058742994$ used by the current whole-positive producer,
since it lies between the true root and $r_*+h$ for every allowed
parameter. The same global reference is used, the length upper bound
only improves, and all actual coefficient and frame inequalities
hold throughout the larger interval. The right unstable input is
then taken at that fixed cut; it is not silently set to zero.

This proof uses the exact finite band of the current centre. It does
not transfer that band to an arbitrary infinite-tail correction.
The previously proved positive-order neighbourhood inverse is a
different statement; an appropriate negative-window neighbourhood
estimate would require its own complete convolution fee.

The restored common-root-piece run, current negative strict body,
whole positive coefficient/Volterra instance, genuine finite radial
head and parameter Schur remain separate global tasks. In particular
(W.29) is local to this root germ; it is not extended to the exterior
where $n_R$ is much smaller. The outer theorem pays that actual
endpoint normalization separately. No whole-body or final closed
surface conclusion is asserted here.
