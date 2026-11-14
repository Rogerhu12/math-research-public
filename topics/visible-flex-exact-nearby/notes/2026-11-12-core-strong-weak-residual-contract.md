# Complete strong weak-residual interface for the actual finite core

**Status.** The identities and finite-majorant construction below are proved.
The complete positive-half local flow input has already been calculated for
the exact family $\delta_5+[-10^{-9},10^{-9}]$. The new all-Fourier coefficient
rectangles and weak-residual Gram arrays have not yet run: the restored native
executor disconnected again before either computation, and the CI collector
failed before runner allocation. No numerical weak-source constant is claimed.

The entry points are:

- `fourfold_phase_core_exact_reference.py`: an exactly continuous finite reference;
- `fourfold_phase_core_field_polynomial.py`: the actual five coefficient fields, with a complete infinite remainder;
- `fourfold_phase_core_weak_residual.py`: separate scalar and divergence loads in four strong angular norms.

All physical ports remain at $r=\pm1/4$. The genuine root $H^{1/3}$ contact
is not substituted for the ordinary-cut $H^{1/2}$ lift.

## 1. Exact continuous reference with prescribed two-sided heights

For an accepted positive leaf, let $u=(r-c)/h$, $h>0$, and let the exact
dyadic generator coefficients $F_i$ and exact dyadic transfer center $T$
be those already saved in its paid flow package. Define the rational
polynomial $Z$ by the previously proved recurrence. Put
$$
 R(u)=Z(u)Z(-1)^{-1}
       +\frac{u+1}{2}\left(T-Z(1)Z(-1)^{-1}\right).              \tag{1}
$$
Both identities
$$
 R(-1)=I,\qquad R(1)=T                                        \tag{2}
$$
are exact rational identities. Thus the small saved-transfer selection fee
does not create an uncharged jump: it becomes the explicit affine term in
(1), whose derivatives enter the actual residual below.

Let $P_j=T_j\cdots T_1$ be the exact dyadic joining products. On leaf $j$ set
$$
 \Phi(r)=R_j(u)P_{j-1}.
$$
This gives an exactly continuous full Cauchy state $\Phi$ on $[0,1/4]$.
The state is $(w,p/8)$; physical flux is restored by multiplying its lower
slot by $8$.

The correct radial parities are
$$
 a,c,\tau,\sigma \text{ even in }r,\qquad b\text{ odd in }r.
$$
Both $b$ and $\sigma$ are odd in the angular variable, a different assertion.
With $J=\operatorname{diag}(I,-I)$, define the negative reference by
$\Phi(-r)=J\Phi(r)J$. This gives exact continuity of both state slots at the
waist; it does not require the finite reference to have matching all-order
jets there.

Write $P=\Phi(1/4)$ and $P_w$ for its height rows. The two-sided height map is
$$
 {\cal H}=\begin{pmatrix}P_wJ\\P_w\end{pmatrix}.
$$
Whenever its **finite** inverse is verified, $\Phi(r){\cal H}^{-1}$ gives
the reference columns with exactly the prescribed $18$ endpoint height
coefficients. All angular means are retained. The inverse is enclosed by
directed matrix arithmetic, not assumed from a floating determinant.
This finite inverse does not assert invertibility of the whole infinite
core Dirichlet problem.

The reference $w$ is continuous and piecewise smooth, hence in the appropriate
energy test space. The reference $p_N$ is also exactly continuous. Therefore
$p_{N,r}$ has no hidden interface delta function. A jump of the *physical*
flux $a w_r+bw_\theta$ is already represented by the divergence load below.

## 2. Exact weak source decomposition

Use the actual R37 coefficients with
$$
 H=\tau+\sigma_\theta,\qquad
 Lw=\partial_r(a w_r+bw_\theta)
       +\partial_\theta(bw_r+cw_\theta)+Hw.
$$
The self-adjoint weak form, with the usual conjugates for complex tests, is
$$
 {\mathfrak b}(w,v)=\int
   (a w_r+bw_\theta)v_r
  +(bw_r+cw_\theta+\sigma w)v_\theta
  +(\sigma w_\theta-\tau w)v.                                \tag{3}
$$
Angular integrals use the normalized periodic measure; the physical
frequencies are $4k$.

Let $P_N$ be the retained physical Fourier projection and $P_H=I-P_N$.
For the finite reference define
$$
 \begin{aligned}
 R_r&=a w_r+bw_\theta-p_N,\\
 R_\theta&=P_H(bw_r+cw_\theta+\sigma w),\\
 R_0&=\sigma w_\theta-\tau w-p_{N,r}
      -\partial_\theta P_N(bw_r+cw_\theta+\sigma w).
 \end{aligned}                                               \tag{4}
$$
Integration by parts of only the continuous finite $p_N$ and the periodic
finite angular term gives exactly
$$
 {\mathfrak b}(w,v)-[p_Nv]_{-1/4}^{1/4}
   =\int R_rv_r+R_\theta v_\theta+R_0v.                       \tag{5}
$$
The pure high scalar load is particularly simple:
$$
 P_HR_0=P_H(\sigma w_\theta-\tau w).                          \tag{6}
$$
No uncomputed radial or angular derivative of a geometric coefficient has
been introduced. The implementation retains `radial_all`,
`radial_high`, `angular_high`, `scalar_all`, and `scalar_high`
separately. Low finite-reference defects are not deleted.

## 3. Complete actual coefficient rectangle

Fix one exact scalar germ and one accepted real leaf. A fresh actual
domain calculation proves
$$
 |g(u,x)|\le M_g,\qquad |u|\le R,\quad |\operatorname{Im}x|\le S,
 \qquad x=4\theta,                                           \tag{7}
$$
for each $g=a,b,c,\tau,\sigma$ and every parameter in the same eta interval.
This new bidisk is an actual geometric denominator/modulus proof. The
previous outer domain at real angles is not silently upgraded to (7).
The waist uses the previously paid removable $F_z/r$ quotient.

On the time circle $|u|=\rho$, $1<\rho<R$, take $N_t$ nodes and $L$ real
angular nodes. For $|k|\le K<L/2$, define
$$
 A_k=\frac{e^{-(L-|k|)S}+e^{-(L+|k|)S}}{1-e^{-LS}},
 \quad W_k=e^{-|k|S}+A_k,\quad q=(\rho/R)^{N_t}.
$$
The complete joint time/angular alias for coefficient $(i,k)$ is bounded by
$$
 M_g R^{-i}\left(A_k+W_k\frac{q}{1-q}\right).                  \tag{8}
$$
Indeed, angular folding produces the holomorphic sum
$\sum_\ell g_{k+\ell L}(u)$; its radial Taylor coefficients have modulus
at most $M_gR^{-i}W_k$. Only time aliases $i+\ell N_t$, $\ell\ge1$,
occur. Equation (8) includes every angular and time translate.

The native samples are directed enclosures of the true coefficient field,
including the complete infinite primitive. The Acb DFT encloses their
arithmetic and input errors. Chosen coefficients are exact binary64 dyadics.
For even fields their positive coefficients are real; for angularly odd
$b,\sigma$ their coefficients divided by $i$ are real. Exact angular parity
defines all negative coefficients and the odd zero coefficient. Time
conjugacy applies to these rotated real coefficients, with no false
real projection at a complex radial point.

The complete rectangle complement on real $|u|\le1$ splits into:

1. all time orders at $|k|>K$, bounded directly by
   $2M_g\sum_{k>K}(4k)^j e^{-kS}$;
2. only the retained angular modes but $i\ge m$, bounded by
   $M_gR^{-m}(1-R^{-1})^{-1}
       \sum_{|k|\le K}(4|k|)^j e^{-|k|S}$.

These sets are disjoint and include the corner. Adding every selected
coefficient error proves full $A_0,A_1,A_2$ error bounds $E_{g,j}$.
A small finite tail never replaces either infinite complement.

For the diagonal norm
$$
 \|v\|_{H^s}^2=|v_0|^2+\sum_{k\ne0}(4|k|)^{2s}|v_k|^2,
$$
the multiplier error follows from the complete $(1+4|k|)^s$ coefficient
sum. For $s=0,1/2,1,3/2$ the bounds are respectively
$$
 E_0,\quad E_0+\sqrt{E_0E_1},\quad E_0+E_1,\quad
 \sqrt{(E_0+E_1)(E_0+2E_1+E_2)}.                              \tag{9}
$$
They control the actual parameter variation as well as all numerical and
truncation errors. They are not merely norms of the finite saved polynomial.

## 4. Complete finite products and an operator-valued Gram majorant

Each finite coefficient has angular support through $K$, and the reference
has support through $N$. Every product in (4) therefore retains all modes
$-K-N,\ldots,K+N$. Its exact time-polynomial degree is retained in full.
No projected output row is silently discarded.

For one residual component, let
$$
 C(u)=\sum_{i=0}^{d}u^i C_i
$$
be its complete finite operator from endpoint heights to the chosen angular
output space. Let $G_i=C_i^*\Lambda^{2s}C_i$.
For any exact positive numbers $\lambda_i$ on the nonzero rows,
weighted Cauchy--Schwarz gives the positive-semidefinite inequality
$$
 \int_{-1}^1 C(u)^*\Lambda^{2s}C(u)\,du
 \preceq
 \left(\sum_i\lambda_i\right)
 \sum_i\frac{2G_i}{(2i+1)\lambda_i}.                           \tag{10}
$$
The implementation chooses directed positive upper dyadics proportional to
$\sqrt{2\|G_i\|/(2i+1)}$; any such positive choice is valid.
Multiplying (10) by the exact physical halfwidth $h$ gives a finite Gram
**majorant** in $L^2(dr;H^s_\theta)$. It is not mislabeled as the exact
residual Gram. All matrices retain their complete endpoint column space,
including the mean.

Let $G$ denote this exact majorant, $\widehat G$ its selected dyadic
Hermitian center, and let $e_G\ge\|G-\widehat G\|$ be paid. Suppose
the actual-minus-finite residual operator has norm at most $e$ in the same
space and $\|C\|\le c$. Then
$$
 R_{\rm true}^*R_{\rm true}
 \preceq \widehat G+(e_G+2ce+e^2)I.                           \tag{11}
$$
This follows directly from
$\|Cz+Ez\|^2\le\|Cz\|^2+(2ce+e^2)\|z\|^2$.
The reported diagonal radius in (11) includes arithmetic selection and the
complete actual coefficient errors.

## 5. Actual-minus-finite source fees

For each of the four stated $H^s$ norms, let $W_s,W_{r,s},W_{\theta,s}$
be complete real-time operator bounds of the finite reference.
They are calculated from all exact reference coefficients, not from a radial
sample. Let $e_{a,s},\ldots,e_{\sigma,s}$ be the multiplier errors from (9).
Set
$$
 \begin{aligned}
 e_r&=e_{a,s}W_{r,s}+e_{b,s}W_{\theta,s},\\
 e_\theta&=e_{b,s}W_{r,s}+e_{c,s}W_{\theta,s}
                          +e_{\sigma,s}W_s,\\
 e_0&=e_{\sigma,s}W_{\theta,s}+e_{\tau,s}W_s.
 \end{aligned}
$$
Then the complete difference fees in $L^2(dr;H^s)$ are $\sqrt{2h}$ times
$e_r$ for both radial outputs, $e_\theta$ for the high angular output,
$e_0$ for the high scalar output, and $e_0+4Ne_\theta$ for the all-mode
scalar output. The last factor uses exactly
$\|\partial_\theta P_N\|\le4N$; it is not charged to the high scalar output
where that term is absent.

The same positive-half coefficient rectangle is used on the negative side
with its **correct radial parity**: only $b$ changes sign. The reference
uses the reflected Cauchy state and physical derivative $-\partial_s$.
The scalar family and physical normalization therefore stay identical on
both halves.

For a complete cover, the leaf Gram majorants and their radii may be summed
in the same endpoint input coordinates. This provides genuine complete
weighted body-source bounds once all leaves have actually run. It does not
supply the missing high inverse or its dual constants.

## 6. What this pays, and what it does not

Equation (11) can be used with the actual joint high weak-solver contract.
For a one-derivative inverse loss, the half-weighted residual must be charged
in that contract. A lone $H^{-1/2}$ boundary flux error does not supply it.
The four explicit output norms permit the needed choice without changing
the mathematical input.

The two exterior regular traces/fluxes, ordinary-cut high heights, high
physical fluxes, full mean sector, and the actual coefficient-to-frame
multipliers remain separate ports. The core body Gram does not erase them.
No complete high Schur constant or final $21\times21$ inverse is concluded
from these source formulas alone.

## 7. Strong cap flux from the complete complementary mismatch

This section corrects the earlier undefined use of the word "residual".
The quantity below is the **full primal/dual complementary mismatch**, not
merely the weak PDE residual of the primal trial. A true primal solution
paired with an arbitrary equilibrated dual flux can have zero primal PDE
residual and nonzero DN error.

Work on the same complete cap $[c,R]$, $c=1/4$, with the actual positive
coefficient matrix $B$ and the exact radial exterior Robin form $\Gamma$.
As in R95, $\Gamma$ is positive on the nonmean modes, $\Gamma1=0$, and the
regular mean trace and its conjugate flux remain separate ports. Write
$D=\partial_\theta$ in the physical coordinate components. The exact
radial Robin operator commutes with $D$.

Let $u$ be the true complete-cap solution for an input $(a,\xi)$, let $V$
be a conforming primal trial with exactly the same two prescribed inputs,
and let $j=(p,q)$ be an equilibrated dual trial. Thus $\operatorname{div}j=0$
in the full cap, including the interfaces, and its regular mean flux is
retained. The dual trial is not required to satisfy the Robin condition
of the primal trial. Its full nonmean Robin mismatch is charged explicitly.

Define the **unweighted** mismatch pair
$$
 z=B\nabla V-j,\qquad z_R=\Gamma V_R^\perp+p_R^\perp.           \tag{12}
$$
For a body/boundary pair $\zeta=(\zeta_b,\zeta_R)$ use
$$
 \|\zeta\|_*^2
 =\int_c^R\zeta_b^*B^{-1}\zeta_b
   +\langle\Gamma^{-1}\zeta_R,\zeta_R\rangle ,
 \qquad
 R_0=\|(z,z_R)\|_*,
 \quad R_1=\|(Dz,Dz_R)\|_* .                                 \tag{13}
$$
The inverse $\Gamma^{-1}$ acts only on the nonmean boundary slot. In
particular, differentiating the weighted vector $B^{-1/2}z$ is **not** the
definition of $R_1$. The quantity $R_0^2$ is exactly
$$
 R_0^2=E(V)-2\operatorname{Re}L(j,(a,\xi))+D(j).
$$
It includes the whole body, graft and genuine Robin/tail contribution.
A complete directed upper bound for this complementary gap may be used
for $R_0^2$. Neither a partial radial integral nor the primal PDE residual
norm may replace it.

Put $e=u-V$; it has zero prescribed inputs. For any such zero-input
variation $v$, use the map
$$
 {\cal G}v=(B\nabla v,\Gamma v_R^\perp).
$$
The true-minus-dual mismatch is
$$
 \chi=(B\nabla u-j,\Gamma u_R^\perp+p_R^\perp)
      =(z,z_R)+{\cal G}e.
$$
Let $\mathscr E$ be the closed space of pairs whose unweighted pairing
with $(\nabla v,v_R^\perp)$ vanishes for every zero-input $v$.
The true equation and the exact divergence identity for $j$ imply
$\chi\in\mathscr E$, while $\mathcal G e\in\mathscr E^{\perp_*}$.
Consequently,
$$
 \|\chi\|_*^2+\|e\|_{\mathfrak b}^2=R_0^2,
 \qquad \|e\|_{\mathfrak b}\le R_0.                           \tag{14}
$$
This is the complementary-energy projection identity, not an estimate
inferred from primal residuals alone.

Assume that the following complete coefficient bound is finite:
$$
 C_B=\operatorname*{ess\,sup}_{(r,\theta)}
       \|B^{-1/2}(DB)B^{-1/2}\|.
$$
Since $D\Gamma=\Gamma D$ and the regular mean derivative is zero,
$$
 D\chi=(Dz+(DB)\nabla e,\ Dz_R)+{\cal G}(De).
$$
The space $\mathscr E$ is preserved by $D$: the test $Dv$ has the same zero
inputs, and angular integration by parts gives the assertion. Therefore
$D\chi$ is the $\|\cdot\|_*$-orthogonal projection of
$(Dz+(DB)\nabla e,Dz_R)$ onto $\mathscr E$. This gives the sharper factor-one
bound
$$
 \boxed{\quad
 \|D\chi\|_*\le R_1+C_B R_0.
 \quad}                                                     \tag{15}
$$
It also gives $\|De\|_{\mathfrak b}\le R_1+C_B R_0$.
The identities follow first for angularly smooth inputs; difference
quotients give the same conclusion whenever the displayed weighted
quantities are finite. No radial differentiability across a spline
interface is required by this argument.

Let $d=(-p_L,p_{R,0})$ be the exact dual boundary output, and let $S_c(a,\xi)$
be the true complete-cap DN output. For the same actual cap, suppose the
full-domain lift of a left trace supported on $|k|>N$ has energy at most
$C_{\mathrm{lift},N}^2\|h\|_{\dot H^{1/2}}^2$ with regular input zero.
Pairing $D\chi$ with that lift proves
$$
 \boxed{\quad
 \|\Pi_{>N}(S_c(a,\xi)-d)_L\|_{\dot H^{1/2}}
 \le C_{\mathrm{lift},N}(R_1+C_B R_0).
 \quad}                                                     \tag{16}
$$
Here
$\|D\Pi_{>N}f\|_{\dot H^{-1/2}}=\|\Pi_{>N}f\|_{\dot H^{1/2}}$
holds exactly for the physical frequencies $4k$. The regular flux error
keeps its independent estimate
$$
 |(S_c(a,\xi)-d)_{\mathrm{reg}}|
 \le C_{\mathrm{lift,reg}}R_0.                               \tag{17}
$$
It is not removed by differentiating the nonmean left flux.

For actual computation the new derivative input is explicitly
$$
 Dz=B\nabla(DV)+(DB)\nabla V-Dj,\qquad
 Dz_R=\Gamma(DV_R)^\perp+(Dp_R)^\perp .
$$
Its complete weighted squared norm can be integrated as a matrix-valued
quantity over the same exact trial columns. This preserves the full
finite input space and all cross terms.

The old full gap pays $R_0$, but it does **not** pay $R_1$ or $C_B$.
Those two quantities, and any lift constant used uniformly in the eta
family, must be certified for that same full actual family before (16)
gives a numerical strong-flux error. The previously saved point-only
ordinary-cut lift constant is not automatically a uniform eta bound.
No new numerical cap derivative or strong-flux certificate is asserted
here.

## 8. Reproduction after executor recovery

From the topic directory, first run the already saved global core collector.
For a chosen accepted leaf, run the coefficient entry with its exact saved
leaf report, then use that complete output in the weak-residual entry.
Both positive and negative sides use the same leaf index and coefficient
identity. Missing rectangles or rejected bidisks stop that leaf explicitly.

The native source dependencies, complete coefficient package hashes and
reference input identities are part of every report. Packages above 1 MB
are gzip-compressed, and no binary package is passed through a connector.
The current new sources are replayable work, not fabricated results from
the unavailable executor.
