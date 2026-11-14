# R105: exact dihedral reduction of the actual core and complete low ports

2026-11-12, reproduce-newton.

**Status.** The symmetry reduction and error-transfer statements in this
paper are proved. Two small replay entries are supplied. Neither the new
10-dimensional global composition nor the new 6-dimensional inverse has
executed: the native executor is unavailable and the latest CI retry
failed before a runner or any mathematical step was allocated. The
174-span/175-leaf positive-half local certificates remain the actual
numerical inputs. Their local error sum is not a global propagation bound.

The object is the same explicitly symmetric exact affine family with
center
$$
 \delta_5=-7789843107295549/4611686018427387904,
 \qquad |\delta-\delta_5|\le10^{-9}.                         \tag{105.1}
$$
No change of surface, physical cut, Fourier normalization or parameter
interval is made. All cuts below are the physical $r=\pm c$, $c=1/4$.
The complete high weak problem and both physical Cauchy channels are not
replaced by an assumed infinite-core DN map.

## 1. The actual invariant operator and source class

Use the R32/R37 scalar $w$ in the actual physical R88 formulation. R71
proves covariance of the reconstruction under the exact group generated
by fourfold rotation, angular reflection and waist reflection. In the
material coordinates, the scalar invariant class is
$$
 w(r,\theta+\pi/2)=w(r,\theta),\quad
 w(r,-\theta)=w(r,\theta),\quad
 w(-r,\theta)=w(r,\theta).                                 \tag{105.2}
$$
The actual scalar operator is
$$
 Lw=\partial_r(a w_r+bw_\theta)
       +\partial_\theta(bw_r+cw_\theta)+Hw,\qquad
 H=\tau+\partial_\theta\sigma.                             \tag{105.3}
$$
Here $c$ denotes the modified angular principal coefficient, not the
unmodified coefficient of the original graph. The exact parities are

| coefficient | angular reflection | waist reflection |
|---|---|---|
| $a,c,\tau$ | even | even |
| $b$ | odd | odd |
| $\sigma$ | odd | even |
| $H$ | even | even |

In particular, the angularly odd $\sigma$ is radially even. These parities
prove that $L$ commutes with both scalar reflections. The physical
projection onto $k=-N,\ldots,N$ also commutes with them. Its two Cauchy
variables are $(w,p/s)$, where
$$
 p=P_N(a w_r+bw_\theta),\qquad s=8                         \tag{105.4}
$$
in the existing complete local-flow data. Angular reflection acts the
same way on both slots; waist reflection acts as
$(w(r),p(r))\mapsto(w(-r),-p(-r))$.

The restriction in (105.2) is permissible for the invariant nonlinear
construction only when the geometry, target metric, source, prescribed
flat set, operator realization and reconstruction retain that same
action. R71 supplies the reconstruction covariance. Averaging a solution
does not solve a noninvariant prescribed source. Nothing here asserts
surjectivity on the omitted representations.

## 2. The ordinary-cut groundstates and the two regular ports

Write $Y_z=F_z/|F|$. It is angularly even and radially odd. The positive
groundstates used on the two actual caps are
$$
 Y_-(r,\theta)=-Y_z(r,\theta)\quad(r<0),\qquad
 Y_+(r,\theta)=Y_z(r,\theta)\quad(r>0).                      \tag{105.5}
$$
Thus their values at the two cuts are the same positive function $Y$.
For an invariant $w$, the grounded traces satisfy
$$
 U_-=\frac{w(-c,\theta)}{Y_-(-c,\theta)}
     =\frac{w(c,\theta)}{Y_+(c,\theta)}=U_+ .                \tag{105.6}
$$
The mean regular input on each corresponding complete exterior is also
exchanged with the **same sign**. Denote these two genuine ports by
$\xi_-,\xi_+$; their dual fluxes $\lambda_-,\lambda_+$ remain part of the
same self-adjoint form.

The groundstate flux $p_{Y_z}=a(Y_z)_r+b(Y_z)_\theta$ is radially even.
The left positive groundstate has flux $-p_{Y_z}$ at the reflected point.
Together with the left outward-conormal sign, this gives the same
energy shear at both cuts. Consequently the existing finite assembly
correctly has two copies of the same cap compression and two copies of
the same negative projected shear $-Yp_{Y_z}$. There is no uncharged sign
change of a cap or regular slot in this reduction.

The normalized translation trace used in the saved bordered candidate is
$$
 t=\tfrac12(-e_{0,-}+e_{0,+}-e_{\xi,-}+e_{\xi,+}).            \tag{105.7}
$$
It is angularly even and odd under the simultaneous exchange of the
two cuts and two regular ports. This is the correct representation of
the retained $z$-translation compatibility, not a reason to delete an
arbitrary mean load.

## 3. Two commuting involutions and the exact dimensions

The saved full low space has coordinate order
$$
 (U_{-,-N:N},\,U_{+,-N:N},\,\xi_-,\,\xi_+,\,\lambda_b),
 \qquad \dim=4N+5,                                         \tag{105.8}
$$
where $\lambda_b$ is the translation-border variable. Angular reflection
$\mathcal S$ reverses $k$ on each height block and fixes the two regular
coordinates and the border. Waist reflection $\mathcal J$ exchanges the
two height blocks, exchanges the two regular coordinates, and sends
$\lambda_b\mapsto-\lambda_b$. Both are self-adjoint unitary involutions;
they commute.

For the actual self-adjoint low realization, all its components commute
with these two involutions. The border respects this assertion because
$\mathcal J_0 t=-t$ on the unbordered space:
$$
 \operatorname{diag}(\mathcal J_0,-1)
 \begin{pmatrix}A&t\\t^*&0\end{pmatrix}
 \operatorname{diag}(\mathcal J_0,-1)
 =\begin{pmatrix}A&t\\t^*&0\end{pmatrix}.                    \tag{105.9}
$$
The exact joint projectors are
$$
 \Pi_{\alpha,\rho}=\frac14(I+\alpha\mathcal S)
                              (I+\rho\mathcal J),
 \qquad \alpha,\rho\in\{+1,-1\}.                            \tag{105.10}
$$

| angular sign $\alpha$ | waist sign $\rho$ | dimension | retained scalar ports |
|---|---|---:|---|
| $+$ | $+$ | $N+2$ | paired cosine mean and paired regular mean |
| $+$ | $-$ | $N+3$ | antisymmetric cosine mean, regular mean and translation border |
| $-$ | $+$ | $N$ | no angular means; both physical sides remain paired |
| $-$ | $-$ | $N$ | no angular means; both physical sides remain paired |

For $N=4$, the old angular decomposition $13+8$ is therefore the more
precise decomposition
$$
 21=6+7+4+4.                                               \tag{105.11}
$$
The full invariant Newton problem uses the first sector. Its one regular
coordinate is the normalized pair
$(\xi_-,\xi_+)=(\xi,\xi)/\sqrt2$, not a condition setting either port to
zero. The angular mean also remains. The border belongs to the second
sector because the compatible invariant source has zero component in
that representation.

R71 independently shows that an invariant scalar source has zero
projection on all first spherical harmonics: fourfold rotation removes
the $x,y$ components and waist reflection removes the $z$ component.
The constant spherical harmonic is not removed. Any other genuine
invariant kernel, cokernel or compatibility condition must still be
handled; the dimension count proves none of them absent.

## 4. One fixed Hermitian norm and selected centers

Let the chosen finite height norm be
$$
 \|u\|_{H^s_N}^2=|u_0|^2+
             \sum_{0<|k|\le N}(4|k|)^{2s}|u_k|^2,
 \qquad s\ge0,                                             \tag{105.12}
$$
with weight one on each regular coordinate and the border. Its diagonal
weight $W_s$ commutes with $\mathcal S,\mathcal J$. A self-adjoint form
matrix $A$ is represented on Euclidean normalized coordinates by
$W_s^{-1}AW_s^{-1}$, not by the generally non-Hermitian similarity
$W_s A W_s^{-1}$. The normalized cosine and sine bases and paired side
bases are unitary in these coordinates. For $s=0$ this is exactly the
Euclidean Fourier coefficient norm of the existing paid-low report.

An actual target commutes exactly with the involutions. A selected
floating or dyadic center need not. Before claiming exact zero cross
blocks, replace a center $\widehat A$ by
$$
 \overline A
 =\frac14\sum_{\alpha,\rho\in\{0,1\}}
      \mathcal S^\alpha\mathcal J^\rho\,
      \frac{\widehat A+\widehat A^*}{2}\,
      \mathcal J^\rho\mathcal S^\alpha .                    \tag{105.13}
$$
Hermitian projection and this finite unitary average are contractive
relative to every actual Hermitian commuting target. Thus any separately
proved error $\|A_\star-\widehat A\|\le\varepsilon$ remains valid for
$\overline A$. The norm of the change of center may be reported, but need
not be added again when this contraction is the comparison being used.
Compression by any $\Pi_{\alpha,\rho}$ also does not increase the error.

This statement does not manufacture an error bound for the old floating
core. The currently paid cap/interface fees remain partial until the
actual core and complete high feedback are included. For $s\ge0$,
$\|W_s^{-1}\|\le1$ permits an already paid Euclidean form error as a
conservative error in (105.12); it does not transfer an inverse norm
between the different weighted realizations.

## 5. Direct use of all 175 original local matrices

Let $Q_c$ be the exact isometry with columns
$$
 e_0,\quad (e_k+e_{-k})/\sqrt2,\quad 1\le k\le N,
 \qquad U_c=\operatorname{diag}(Q_c,Q_c).                   \tag{105.14}
$$
Each actual positive local transfer $T_j^\star(\delta)$ commutes with
angular reflection. If its saved exact dyadic center $T_j$ obeys the
already paid uniform error $\|T_j^\star-T_j\|\le\epsilon_j$, then
$$
 \|U_c^*T_j^\star U_c-U_c^*T_jU_c\|\le\epsilon_j.            \tag{105.15}
$$
The compressed centers in (105.15) are used as the **exact algebraic**
expressions in $1/\sqrt2$ and the original dyadic entries. No intermediate
binary midpoint is selected. Acb matrix arithmetic encloses these
expressions and their products. There is consequently no extra local
selection fee to invent or omit. A final saved binary matrix receives
its own explicitly paid selection fee.

The complete-cover checks from the original collector are reused:
all 174 original spans, all 175 accepted leaves, exact adjacent real
endpoints, full eta identity, every report and array hash, and all producer
dependencies. No rejected interval is discarded and no missing leaf is
filled with zero. The local errors remain parameter-uniform; they are not
independent random errors.

Let $P_j$ be the exact products of the compressed centers. Directed prefix
inverses give
$$
 B_*=\sum_j\|P_j^{-1}\|\epsilon_j\|P_{j-1}\|,\qquad
 \|P^\star-P\|\le\|P\|(e^{B_*}-1)=e_P .                    \tag{105.16}
$$
For $N=4$, all matrices in this computation have dimension $10$ instead
of $18$. Equation (105.16) still requires actual matrix arithmetic.
The existing scalar sum of local errors is not substituted for it.

For waist-even solutions, $w_r(0)=0$ and $b(0)=0$, hence $p(0)=0$ exactly.
Write the positive angular-even transfer in two $(N+1)$-dimensional slots,
$$
 P=\begin{pmatrix}A&B\\C&D\end{pmatrix}.
$$
If $A^\star$ is certified invertible, the desired finite core DN matrix is
$$
 \boxed{\quad \Lambda_{++}^\star=s\,C^\star(A^\star)^{-1}.
 \quad}                                                   \tag{105.17}
$$
The normalized paired cut heights are
$(w_-,w_+)=(Q_c v,Q_c v)/\sqrt2$. The two outward fluxes coincide and their
normalized paired output is $\sqrt2$ times either one. These factors
cancel, giving (105.17) with no additional factor two.

Only this finite $A$ inverse is used. It is not necessary to invert the
complete positive $P^\star$, the full reflected transfer, or a
Dirichlet block in an omitted odd representation. In particular, an
odd-sector pole cannot be used to conclude that the desired finite
problem is singular.

For $q=\|A^{-1}\|$, $qe_P<1$, set
$$
 q_\star=\frac{q}{1-qe_P},\qquad
 d_Q=\frac{q^2e_P}{1-qe_P}.
$$
Then a complete direct error for (105.17) is
$$
 \|\Lambda_{++}^\star-sCA^{-1}\|
 \le s\big(e_Pq_\star+\|C\|d_Q\big).                        \tag{105.18}
$$
The true finite DN is Hermitian by the same physical Green identity with
zero waist flux. Hermitian projection therefore contracts (105.18);
the final binary selection error is then added.

## 6. The six-dimensional cap/core candidate and all omitted sources

Let $Y_c=Q_c^*P_NM_YP_NQ_c$ and
$S_c=Q_c^*P_NM_{Yp_Y}P_NQ_c$. Let $C_c$ be the angular-even compression of
the actual complete positive-cap DN on the $N+1$ cosine inputs plus its
regular mean. In the normalized waist-even space the finite low candidate is
$$
 A_{++}^{(N)}
 =\begin{pmatrix}Y_c^*\Lambda_{++}^{(N)}Y_c-S_c&0\\0&0\end{pmatrix}
      +C_c .                                               \tag{105.19}
$$
The block notation means that the first summand acts on the $N+1$ height
coordinates; all height/regular cross terms of $C_c$ remain. Both identical
cap copies and both identical shear copies reduce to one copy because the
paired inputs carry the factor $1/\sqrt2$. The translation border has
zero compression to this sector.

Equation (105.19) is a finite candidate assembly. It does not assert that
the product $YU$ has no omitted angular modes or that the whole infinite
core DN exists. High heights generated by $Y$, high cap and shear fluxes,
core scalar and divergence sources, and the paired regular output all
remain in the complete symmetric high weak problem. A low matrix inverse
is useful only after the required strong feedback fees are paid in the
same norm and physical ports.

The residuals of the strong weak-source contract retain these parities
for invariant $w$:
$$
 R_r:\text{ angular even, radial odd},\qquad
 R_\theta:\text{ angular odd, radial even},\qquad
 R_0:\text{ angular even, radial even}.                     \tag{105.20}
$$
These are the correct vector/gradient representations. In particular,
the odd angular divergence component must not be discarded merely
because the scalar solution is angularly even. Its pairing with the
odd derivative of an even test function is part of the true equation.
Restriction of the complete source Gram to the invariant input columns
is contractive; all its Fourier tails and stated Sobolev weights remain
necessary.

## 7. Replay entries and present scope

The whole-eta finite core entry is
scripts/fourfold_phase_core_even_collect.py. From the topic directory:
~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_phase_core_even_collect.py \
  --cover-root data/core_uniform_flow_ci/43307149760 \
  --bits 256 \
  --out notes/native_core_20261112/complete_uniform_even_core.json
~~~
It reuses the complete already calculated local input and writes either
the new true finite $5$-height DN radius or an explicit failure. Its
prefix trace is retained. It does not relabel the old floating block.

The independent small-candidate decomposition is
scripts/fourfold_phase_low_block_dihedral.py:
~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_phase_low_block_dihedral.py \
  --height-order 0 --bits 256 \
  --out notes/native_core_20261112/finite_low_dihedral.json
~~~
This entry reads the existing paid-low selected matrix, takes the exact
group average (105.13), and encloses all four joint finite inverses.
It preserves the partial-fee scope of that input. The default center-only
interface is not promoted to the eta family. A failed odd inverse is
recorded and does not by itself prevent evaluation of the desired even
block.

Both new entries are unexecuted at the time of writing. No claim that
the desired inverse is smaller, nonsingular or sufficient for the final
strong inverse is inferred from the reduction. The actual R101 circle
conjugacy does not fill this remaining operator gap.
