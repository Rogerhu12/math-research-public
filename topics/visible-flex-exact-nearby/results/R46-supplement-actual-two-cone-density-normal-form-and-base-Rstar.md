# R46 supplement: the actual two-cone density normal form and its complete base remainder

**Proved, for the original complete cap realization.** The actual old-object
feedback, with its two independent regular ports, now has a complete scalar
first-order normal form on both nonzero Fourier cones. Its coefficients are
the actual R106 geometric coefficient and its angular reflection. The full
nonmean coefficient is retained. The exact R102 mean and arithmetic apply
to both blocks.

This also gives a full unweighted strong remainder in the two base windows

$$
H_N^0\longrightarrow H_N^{4/3},\qquad
H_N^{-4/3}\longrightarrow H_N^0,\qquad N=2^{20}.       \tag{D.1}
$$

The directed full-space bound is

$$
R_{*,N}<2.840874\,10^{200}.                              \tag{D.2}
$$

This is a finite, very coarse bound. It is not a practically usable cutoff,
a finite-head inverse, a fixed positive angular-weight estimate, or a
nonlinear existence theorem. In particular it does not close the topic's
completion criteria. Its purpose is to identify the actual full coefficient
and close the complete base operator identity, rather than leave a
conditional principal-symbol assertion.

The original large root/strict propagation constants still dominate (D.2).
The new finite word calculus itself costs less than
$1.295742\,10^{147}$ at gain two. A separate exact improvement using the
actual scattering transmissions reduces the cost of triangular elimination.
The final full base reconstruction costs less than $124.036203$; all
ordinary/contact source columns are given below in their original units.

No certificate for the new deep-tail profile is imported. Re-instantiating
the cap for a different true Robin realization remains a separate operation.

## 1. Precisely the already constructed actual operator

Use the complete negative scattering and full positive-cap operators from
R46-supplement-actual-central-scattering-and-complete-base-source.md and
the explicit word from
R46-supplement-actual-strong-scattering-and-return-operator-word.md.
All Hilbert spaces use normalized circle measure, with the previously
specified regular-slot normalization.

The exact complete negative scattering is an onto unitary

$$
\mathscr S=
\begin{pmatrix}A_e&U_e\\V_e&D_e\end{pmatrix},
\qquad \|\mathscr S\|_{L^2}=1.
$$

The full positive-cap direct sum $\mathscr R$ is onto unitary, including
both independent regular coordinates. Set

$$
\mathscr S_{\rm ext}=\operatorname{diag}(\mathscr S,I_{\rm reg}),
\qquad \mathcal A=I-\mathscr R^*\mathscr S_{\rm ext}.      \tag{D.3}
$$

The original complete scattering word is

$$
\mathscr S_0=\begin{pmatrix}0&U\\V&0\end{pmatrix},
\qquad U=M_B^*,\quad V=M_C,
$$

and its already proved bounds, with $g=4/3$, are

$$
[\mathscr S-\mathscr S_0]_+,\ 
[\mathscr S-\mathscr S_0]_-\le R_S,\quad
R_S<2.983109\,10^{130},                                  \tag{D.4}
$$

$$
\|\mathscr S_0\|_{H_N^s\to H_N^s}\le T_g
<5.683778\,10^{58},\qquad |s|\le g .
$$

Here $[F]_+=\|F:H_N^0\to H_N^g\|$ and
$[F]_-=\|F:H_N^{-g}\to H_N^0\|$. Thus
$[F^*]_+=[F]_-$, not $[F]_+$. The complete cap bound is

$$
[\mathscr R+I]_\pm,\ [\mathscr R^*+I]_\pm
\le C_{\rm cap}<7.698073\,10^{11}.                        \tag{D.5}
$$

Each scalar block difference in (D.4) has the corresponding bound.
All blocks in this section are the complete operators, including means.

## 2. Triangular elimination with the actual transmissions

The actual blocks $U_e,V_e$ are $L^2$ contractions. Define

$$
L_e=\begin{pmatrix}I&-U_e\\0&I\end{pmatrix},\qquad
R_e=\begin{pmatrix}I&0\\-V_e&I\end{pmatrix},                \tag{D.6}
$$

and extend by the identity on the two regular slots. They and their exact
triangular inverses have base norm at most two. This is not a high-Sobolev
contraction claim.

Let $\mathscr S_{\rm off,ext}=
\operatorname{diag}((0,U_e;V_e,0),I_{\rm reg})$. Then exactly

$$
E_a=\mathcal A-(I+\mathscr S_{\rm off,ext})
=-(\mathscr R^*+I)\mathscr S_{\rm ext}
  +\operatorname{diag}(A_e,D_e,0_{\rm reg}),              \tag{D.7}
$$

so $\|E_a\|_{L^2}\le3$. The complete forward bound is

$$
[E_a]_+\le C_{\rm cap}+R_S=:E_+.                         \tag{D.8}
$$

For the opposite window, take the adjoint before estimating:

$$
E_a^*=-\mathscr S_{0,\rm ext}^*(\mathscr R+I)
      -(\mathscr S_{\rm ext}-\mathscr S_{0,\rm ext})^*
             (\mathscr R+I)
      +\operatorname{diag}(A_e^*,D_e^*,0).
$$

The first term uses the model at its output index $g$; the next uses the
actual base bound $\|\mathscr R+I\|\le2$. Consequently

$$
[E_a]_-\le \max(1,T_g)C_{\rm cap}+3R_S=:E_- .             \tag{D.9}
$$

Now use $L_m=(I,-U;0,I)$ and $R_m=(I,0;-V,I)$ only in estimates.
Each difference $L_e-L_m,R_e-R_m$ has both strong bounds at most $R_S$.
Direct multiplication gives the exact equation

$$
L_e\mathcal A R_e
=\operatorname{diag}(I-U_eV_e,I,2I_{\rm reg})+L_eE_aR_e.  \tag{D.10}
$$

For the forward strong error, write
$L_e=L_m+(L_e-L_m)$ and keep $R_e$ at its actual base norm two.
Thus

$$
[L_eE_aR_e]_+
\le2(1+T_g)E_++6R_S.
$$

For the opposite window, take the adjoint of the entire product and write
$R_e^*=R_m^*+(R_e^*-R_m^*)$. Its last factor $L_e^*$ again has base norm
two, and the middle factor has base norm at most three. Hence

$$
[L_eE_aR_e]_-
\le2(1+T_g)E_-+6R_S.                                    \tag{D.11}
$$

There is no use of a base contraction at a high output index.

The exact replacement of the actual return by the old explicit word is

$$
U_eV_e-UV=(U_e-U)V_e+U(V_e-V).                            \tag{D.12}
$$

In the forward window the first factor of the first term supplies the
gain, while $V_e$ is a base contraction; the second term uses $U$ only at
its output index. For the opposite window, use

$$
(U_eV_e-UV)^*=(V_e^*-V^*)U_e^*+V^*(U_e^*-U^*).
$$

It follows in both cases that the bound is at most $(1+T_g)R_S$.
Combining (D.10)--(D.12) gives

$$
L_e\mathcal A R_e
=\operatorname{diag}(I-UV,I,2I_{\rm reg})+R_w,             \tag{D.13}
$$

$$
\begin{split}
[R_w]_+&\le2(1+T_g)E_++6R_S+(1+T_g)R_S,\\
[R_w]_-&\le2(1+T_g)E_-+6R_S+(1+T_g)R_S .
\end{split}                                              \tag{D.14}
$$

The directed bounds are respectively
$5.086598\,10^{189}$ and $1.186873\,10^{190}$.
The actual triangular operations require no new inverse or finite-block
invertibility assumption. All their domains are valid: for example
$U_e=U+(U_e-U)$ and (D.4) imply finite bounds on both signed spaces.

## 3. An exact full-mean symmetric density calculus

On every normalized circle set

$$
\Lambda_n=\max(1,|n|),\quad
Q_H=\Lambda^{1/2}C_H\Lambda^{-1/2},\quad
C_Hf=f\circ H,\quad
A(f)=\Lambda^{-1/2}M_f\Lambda^{-1/2}.                     \tag{D.15}
$$

Here $A(f)$ includes its mean row and mean column. A real $f$ gives a
selfadjoint $A(f)$. The actual restricted phases will be compressed to
their original cones; introducing (D.15) does not discard their means
or change the actual propagation.

For every real orientation-preserving degree-one diffeomorphism,
ordinary change of variables proves exactly

$$
\begin{split}
Q_H^*A(f)Q_H
  &=A\left((f/H')\circ H^{-1}\right),\\
Q_H^{-*}A(f)Q_H^{-1}
  &=A\left((f\circ H)H'\right).
\end{split}                                              \tag{D.16}
$$

Indeed all adjacent half powers cancel, and
$C_H^*M_fC_H=M_{(f/H')\circ H^{-1}}$.
No asymptotic quantization rule is used. In particular, with
$H^*f=(f\circ H)H'$ and $E_H=Q_H-Q_H^{-*}$,

$$
Q_HA(f)=A(H^*f)Q_H+E_HA(f).                              \tag{D.17}
$$

The error is entirely the already recognizable cross-cone/mean discrepancy
between $Q_H$ and its flux companion. There is no unspecified scalar
subprincipal correction in (D.17).

The exact group law remains $Q_HQ_G=Q_{G\circ H}$.
For a product $Q_1\cdots Q_k$, its difference from its inverse adjoint
is the ordinary finite telescoping sum with one $E_{H_i}$ in each term.
This gives the quantitative covariance cost below without estimating
new, long composed phase symbols by a narrower strip.

### 3.1 Complete cross and adjoint bounds

Suppose $H$ is analytic on $|\Im x|\le s$, is real on the real axis,
and satisfies $\Re H'\ge c>0$ there. Let $M\ge|H'|$.
Put

$$
a={s\min(1,c)\over2},\qquad
Z_p(a)=\sum_{n\in\mathbb Z}(1+|n|/N)^p e^{-2a|n|},
$$

and let $Z_{p,1}$ have the additional factor $|n|$.
Shifting the Fourier contour by $s/2$ gives, for opposite signs,

$$
|(C_H)_{kj}|\le e^{-a(|k|+|j|)},\qquad
|(Q_H)_{kj}|\le\sqrt{\Lambda_k/\Lambda_j}
                  e^{-a(|k|+|j|)}.                     \tag{D.18}
$$

On nonzero rows and columns the exact flux companion has entries
$\operatorname{sgn}(k)\operatorname{sgn}(j)(Q_H)_{kj}$.
On the mean, $Q_He_0=e_0$; its companion's mean-input column is
$\Lambda^{-1/2}H'$. Its mean-output row on nonzero inputs vanishes.
The remaining mean-output row of $Q_H$ obeys the same contour estimate.

Squaring (D.18) and summing all modes proves the Hilbert--Schmidt bounds
in both windows $0\to2$ and $-2\to0$.
Using $\Lambda_n\le1+|n|$, an intentionally larger common bound for
$E_H$, its adjoint, and every cross/mean projection needed below is

$$
e_H=8(1+M)\sqrt{(Z_4(a)+Z_{4,1}(a))Z_4(a)}.              \tag{D.19}
$$

The displayed factor also covers the separate mean-input and mean-output
rows. For instance their sums are bounded by $M\sqrt{Z_4}$ and
$\sqrt{Z_4}$, respectively, and
$\sqrt{(Z_4+Z_{4,1})Z_4}\ge\sqrt{Z_4}$.
Both infinite opposite-cone rectangles are retained.
For an inverse map one may use the same bound since
$E_{H^{-1}}=-E_H^*$. Real translations have $E_H=0$ exactly.

### 3.2 Ordered phases, products and mean paths

If $f$ has analytic modulus $M_f$ on width $s_f$, all its Fourier
coefficients satisfy $|f_l|\le M_fe^{-s_f|l|}$.
For the ordered phase $M_f\Lambda^{-1}$,

$$
\left|\Lambda_j^{-1}
 -(\Lambda_k\Lambda_j)^{-1/2}\right|
\le{|k-j|\over\Lambda_k\Lambda_j}.                        \tag{D.20}
$$

Moreover

$$
{J_N(k)^2\over\Lambda_k\Lambda_j}
\le1+{1+|k-j|\over N^2},
\qquad J_N(k)=(1+k^2/N^2)^{1/2};
$$

the analogous input-weight bound holds by exchanging $j,k$.
Young's inequality therefore bounds the two complete order-two windows by

$$
o_f=M_f\sum_l
 |l|\left[1+{1+|l|\over N^2}\right]e^{-s_f|l|}.            \tag{D.21}
$$

No finite head is removed. For cross-cone or nontrivial mean paths,
$|k-j|\ge\max(|k|,|j|)$, and an available common strong bound for $A(f)$ is

$$
x_f=M_f\sum_l(1+l^2/N^2)e^{-s_f|l|}.                     \tag{D.22}
$$

For constant phases both errors are zero. Their artificially extended
mean value is removed by the original exterior cone projections.
If an intermediate path passes through that mean, its entry and exit
are paid by (D.19) or (D.22).

Write $M_{p,N}(f)$ for the already proved complete multiplier bound.
Use

$$
a_f=M_{2,N}(f),\qquad
a_f^{(1)}=\sqrt2\,M_{3/2,N}(f).                           \tag{D.23}
$$

The first bounds $A(f)$ and its ordered version on $|s|\le2$.
The second bounds $A(f)$ at gain one in each shifted window needed
to compose two such factors. This follows from
$J_N^{1/2}\Lambda^{-1/2}\le2^{1/4}$.
Thus every term with two or more phases is a genuine gain-two operator,
including its mean paths.

## 4. A finite complete word bound

After normalizing the constant Airy flux factor, the full return $UV$
contains fourteen map factors and fourteen first-phase factors.
Conjugation by the final actual root label adds two map factors.
The precise counts are

| Factor | Map count | Phase count |
|---|---:|---:|
| Actual physical root cut angle | 4 | 0 |
| Actual tilted graph flow | 4 | 4 |
| Constant-section Airy translation | 4 | 4 |
| Complete actual strict flow | 2 | 2 |
| Original full root potential phase | 0 | 4 |
| Actual final root circle and inverse | 2 | 0 |

All four original branch/cone combinations occur. An adjoint factor has
the same real coefficient, with the prescribed sign reversed, and uses
the opposite strong window.

Let $q_i\ge1$ bound each map, its inverse and adjoints on $|s|\le2$.
Let $e_i$ be (D.19). For each phase use $a_j,a_j^{(1)},o_j,x_j$
from (D.21)--(D.23), with the exact constant-phase specialization.
Set

$$
P_Q=\prod_iq_i,\quad P_A=\prod_j(1+a_j),\quad P=P_QP_A,
\quad E=\sum_ie_i,\quad A_0=\sum_ja_j,\quad A_1=\sum_ja_j^{(1)},
$$

and $O=\sum o_j$, $X=\sum x_j$.
Only graph and strict ordered phases need (D.21); the root phase was
already symmetrically ordered.

Here is a full finite bound for all operations used below:

$$
R_{\rm calc}
\le 8P(E+O+X)+P A_1^2+P A_0E+o_b.                       \tag{D.24}
$$

For completeness, this can be obtained without an infinite symbol expansion.
First insert the positive/negative/mean projections between the actual
factors. The physical angle factors are the only initially uncompressed
nonconstant factors; their cross and mean errors are bounded by (D.19).
Split a graph or strict compressed product into its map and phase.
The extra term is a cross map followed by a phase; its bound is at most
$e_i a_j$. Replace its ordered phase using (D.21), and replace adjoint
map factors by inverse maps using $E_H^*$.

On each fixed cone, remove the now internal projections. The difference
between $\Pi F_1\cdots F_r\Pi$ and
$\Pi F_1\Pi\cdots\Pi F_r\Pi$ is the finite telescoping sum with one
$\Pi F_i(I-\Pi)$ at the first omitted interface. Use (D.19) or (D.22)
there, ordinary bounds elsewhere, and include both cones and the actual
mean row/column. The factor eight in (D.24) exceeds the sum of these
projection, split-product, adjoint and ordering fees after division by
their corresponding factors in $P$; $a_j/(1+a_j)\le1$ and $q_i\ge1$.

Expand the resulting fourteen factors $I+iA(f_j)$ as a finite polynomial.
All subsets containing at least two phases have total strong cost at most
$PA_1^2$: select an ordered pair to supply the two gains, pay all remaining
phases at ordinary order, and sum. This overcounts subsets with more
than two phases and is consequently an upper bound.

For a singleton phase, use (D.17) to move it to the output side.
The prefix discrepancy from its inverse adjoint has strong bound at most
the corresponding finite sum of $e_i$ times all other map bounds.
Summing the singleton phases gives $PA_0E$.
The remaining zeroth-order maps combine by their exact group law.
The coefficient is the exact sum of the pulled-back real one-forms.
Finally use (D.21) for the actual final $b$ to return to the R104 ordering;
this is $o_b$.

This proves (D.24) simultaneously in $0\to2$ and $-2\to0$.
Embedding gives (D.1). No multiplier at an unproved large window is used.
No coefficient below a frequency cutoff is omitted.

## 5. Actual half words, signs and the full finite-part coefficient

Write the exactly amplitude-antidiagonal normalized root-cut model as

$$
M_R=2\gamma_0
\begin{pmatrix}0&p\\q&0\end{pmatrix},\qquad
\kappa=(2\gamma_0)^2.
$$

The complete transfer word then has the scalar blocks

$$
M_B=q^*W_-p,\qquad M_C=p^*W_+q,\qquad
U=p^*W_-^*q,\qquad V=p^*W_+q .                           \tag{D.25}
$$

All phases and every map in $p,q,W_\pm$ are the original ones.
In particular $p$ contains the $e^{-i\pi/4}$ Airy factor, and $q$ the
$e^{i\pi/4}$ factor. Thus $M_B$ has constant phase $-i$,
whereas both $U$ and $V$ have constant phase $i$.
The real positive scalar $(2\gamma_0)^2$ has canceled exactly against
$\kappa$; it is not normalized away without its conormal determinant.

Let $P$ be the actual R77 half-return on the physical root angle and let
its root canonical representative be obtained by the actual map
$x_{\rm root}=qY_0(\theta)$.
For positive Fourier input, $M_B$ is the forward physical characteristic
propagation: its label map is $P^{-1}$ and its first coefficient has
the negative imaginary sign of the original minus amplitude.
The complete coefficient is the first-phase one-form integrated along
that actual forward characteristic.

This identification is pointwise. The strict contribution is R46 (5.7)
with physical frequency $4|n|$; hence its coefficient in the normalized
circle phase is $\widehat h_{\rm strict}/4$.
The two original symmetric root phases are exactly

$$
{1\over2q}\int_0^L
 {V(\xi,\phi-\sigma\varepsilon\,2\xi^{3/2}/3)\over\sqrt\xi}\,d\xi .
$$

The fixed-section Airy term is
$-5/(48qL^{3/2})$ at each occurrence.
The actual graph contribution uses
$\mathcal F=(L-\chi)(V+5/(16\xi^2))/q$, its full conormal and its
actual characteristic labels.
These are precisely the finite terms in R46 (9.3).

Coordinate and height covariance is the exact R46 (7.2) identity, and
(D.16) is its full angular operator counterpart.
The common strict/root cut fluxes cancel as the exact one-forms in
R106-supplement-complete-actual-forward-phase.md, equations (4)--(6).
Both the angular-divergence term and the root transport boundaries remain.
Consequently the complete first coefficient, after the original saved
input label, is exactly the certified $h_{\rm fwd}$, not its mean.

Radial reflection from R77 sends the opposite physical traversal to this
same one-form with its exact one-form pullback. Equivalently, before
moving its phase to the output, the opposite traversal has coefficient
$P_*h=(h/P')\circ P^{-1}$. Formula (D.17) changes this to $h$.
Its error has already been included in (D.24).

Now put $\chi=H\circ J\circ\Phi$ from the actual R101 circle theorem and

$$
C(x)=qY_0(\chi(x)/4),\qquad
h(x)=h_{\rm fwd}((J\circ\Phi)(x),p_\infty)(J\circ\Phi)'(x).
                                                               \tag{D.26}
$$

The exact R77 square identity and the actual irrational R101 return give
$\chi^{-1}P\chi=T_{d_*}$ with the fixed natural lift.
After conjugation by $Q_C$, the two positive-cone half words are therefore

$$
U_+\equiv V_+\equiv i(I+iA(h))Q_{d_*}.                    \tag{D.27}
$$

Throughout this section $\equiv$ means equality up to the explicit finite
order-two error already bounded by (D.24). It is not an unpaid
asymptotic-symbol relation.

## 6. The retained negative cone is not assumed to be the conjugate block

Let $\mathcal Kf=\overline f$ be the anti-linear real structure.
The actual real coefficients and the two original amplitude signs give

$$
\mathcal Kp\mathcal K=q,\qquad
\mathcal KW_+\mathcal K=W_- .
$$

These statements include the purified finite mean phases:
complex conjugation exchanges $e^{i\pi/4}$ and $e^{-i\pi/4}$.
The original root coefficients satisfy
$a_{\sigma\varepsilon}=a_{-\sigma,-\varepsilon}$, and
the four graph/strict branches have the same corresponding sign relation.
Applying these exact relations to (D.25) gives

$$
\mathcal KU\mathcal K=V^*,\qquad
\mathcal KV\mathcal K=U^*,\qquad
\mathcal K(UV)\mathcal K=(UV)^*.                          \tag{D.28}
$$

Thus the retained root-plus negative cone is an adjoint-conjugate return,
not a block that may simply be declared the complex conjugate of the
positive return. The difference matters to the sign of the real
first-order phase.

The map $C$ is real, so $\mathcal KQ_C\mathcal K=Q_C$.
The map $Q_C$ is not declared ordinary unitary. When the adjoint of a
root-word conjugation is moved back to the circle convention, its
$Q_C^{-*}$ and $Q_C^*$ differ from $Q_C$ and $Q_C^{-1}$ by
$E_C$ and $E_C^*$, respectively. Those two finite terms are included in
the circle-factor fees in (D.24). Taking the adjoint and conjugation
of (D.27) in this paid calculus, using the separately paid opposite
window, gives the original negative-cone half words

$$
U_-\equiv V_-\equiv iQ_{-d_*}(I+iA(h)).                   \tag{D.29}
$$

Real translations commute with $\Lambda$ and have exact covariance.
Set

$$
\omega=2d_*,\qquad b(x)=h(x)+h(x+d_*).                    \tag{D.30}
$$

Keeping the product order, (D.27) gives

$$
(I-UV)_+\equiv I+(I+iA(b))Q_\omega ,
$$

whereas (D.29) gives

$$
(I-UV)_-\equiv I+Q_{-\omega}(I+iA(b)).                    \tag{D.31}
$$

The quadratic phase products are among the terms paid in $PA_1^2$.
The two displayed orderings are different.

For the positive cone apply the exact rotation conjugation
$Q_\omega(\cdot)Q_{-\omega}$. It turns its first formula in (D.31) into
$I+Q_\omega(I+iA(b))$.
For the negative cone use the **complex-linear** isometry

$$
(J_{\rm ref}f)(x)=f(-x).
$$

It reindexes that cone by $j\ge1$, sends $Q_{-\omega}$ to $Q_\omega$,
and sends $A(b)$ to $A(b(-x))$ without changing $i$.
Thus the two actual R104 blocks have precisely

$$
\boxed{
I+Q_\omega(I+iT_{b_+}D^{-1}),\qquad
I+Q_\omega(I+iT_{b_-}D^{-1}),\quad
b_+(x)=b(x),\quad b_-(x)=b(-x).
}                                                        \tag{D.32}
$$

Here $D e_j=je_j$ on $j\ge1$ and $T_f=\Pi_+M_f\Pi_+$.
The symmetric-to-ordered difference is (D.21).
Both blocks have the same $+\beta/j$ sign in their scalar diagonal.
In particular the positive R102 arithmetic is used directly on both,
rather than assumed to apply to an unverified conjugate block.

The complete R106 geometric return theorem proves that (D.30) is exactly
$b_{\rm geom}$. It now is the operator coefficient in (D.32), since
all propagation, cap, mean, adjoint and ordering errors have been paid.
Therefore

$$
\sup_{|\Im x|\le1/4096}|b_\pm(x)|
<26409.294891526<26410,
$$

$$
\langle b_\pm\rangle=\beta,\qquad
37.00989598323246<\beta<37.04013657837160.                 \tag{D.33}
$$

Both analytic nonmean norms, including every uncomputed Fourier mode,
are exactly the complete R106 bounds on width $1/8192$.
The reflection is an isometry for all their symmetric Fourier weights.

## 7. The actual root-circle transformation is paid

The definition of the exact root chart gives $Y_0'=2U_0$.
Thus (D.26) has

$$
C'(x)={q\over2}U_0(\chi(x)/4)\,
 H'((J\circ\Phi)(x))(J\circ\Phi)'(x).                    \tag{D.34}
$$

The new consumer evaluates the original exact dyadic $H$ through all
516 positive frequencies on 2048 closed angle cells.
At each center the full polynomial derivative is evaluated in Arb;
the whole cell is included with
$\pi\|H''\|_\infty/2048$, where the latter bound is the complete finite
coefficient sum. No sampled lower bound is used.
The same finite coefficients give its full complex derivative modulus.

The exact R101 movements are used for $J\circ\Phi$; its displacement and
derivative domains are kept separate. The original complete $U_0$ bounds
are valid at every image, including the whole real affine parameter box.
The result at the actual $p_\infty$ is

$$
C'>m_C>.172234148706,\qquad
|C'|<M_C<6.794131324991
\quad\text{on }|\Im x|\le1/4096.                         \tag{D.35}
$$

Only the lower bound is real. On the smaller strip

$$
s_C=\min\{(1/4096)/4,\ m_C(1/4096)/(8M_C)\},
$$

Cauchy's estimate gives $\Re C'\ge m_C/2$.
That smaller strip, not the whole original strip, is used in (D.19).

The full real inverse jets are obtained without assuming a large complex
inverse domain. If $F_j$ bounds $C^{(j)}$ and $G_j$ bounds
$(C^{-1})^{(j)}$, set

$$
G_1=1/m_C,\qquad
G_n={1\over m_C}\sum_{k=2}^nF_k
 B_{n,k}(G_1,\ldots,G_{n-k+1}),\quad 2\le n\le4.          \tag{D.36}
$$

This is the exact differentiated inverse identity with its positive
majorant. Real Faà di Bruno, the actual $L^2$ Jacobian, and the full
Leibniz multiplier for the adjoint give the integer composition bounds
through three. Interpolation and duality then pay every needed half
index. Since
$\|\Lambda^{1/2}J_N^{-1/2}\|\le\sqrt N$ and
$\|J_N^{1/2}\Lambda^{-1/2}\|\le2^{1/4}$,
the complete map/inverse/adjoint bound on $|s|\le2$ is

$$
q_{C,2}<385948425.394 .                                  \tag{D.37}
$$

A much smaller **base-only** bound follows directly from the exact circle
$H^{1/2}$ double-integral seminorm. The geodesic circle distances satisfy
$d(Cx,Cy)\le M_Cd(x,y)$, and
$2d/\pi\le2\sin(d/2)\le d$ for $0\le d\le\pi$.
After the change of both variables, the seminorm comparison is at most
$(\pi M_C/(2m_C))^2$. The mean is bounded by the ordinary $L^2$ Jacobian.
For the inverse use its real derivative bounds $1/M_C$ and $1/m_C$.
Consequently both $Q_C$ and $Q_C^{-1}$ have

$$
q_{C,0}\le
\sqrt{\max(M_C,1/m_C)+(\pi M_C/(2m_C))^2}
<62.018101357.                                           \tag{D.38}
$$

This estimate includes the actual nonconstant mean-output functional.
It is independent of $N$ and is not transferred to a higher index.

## 8. The complete full-space remainder

Conjugate the first scalar block in (D.13) by $Q_C$, keeping the second
root block and both regular slots unchanged.
The old error uses $q_{C,2}$ at its high end and $q_{C,0}$ at its base end.
For the opposite window this follows by taking its adjoint.
The full new bound is therefore

$$
R_{\pm,N}=q_{C,2}q_{C,0}[R_w]_\pm+R_{\rm calc}.           \tag{D.39}
$$

The cone rotations and linear reflection from Section 6 are exact
isometries and add no norm fee. The mean of the normalized first scalar
model is the block $2$; the second root block is $I$, and the two regular
blocks are $2I_{\rm reg}$. Every actual coupling among these blocks is
still present in the complete remainder.

The executed values are

| Quantity | Strict outward bound |
|---|---:|
| Complete finite order-two word calculus | $1.295742\,10^{147}$ |
| Full forward strong remainder | $1.217518\,10^{200}$ |
| Full opposite strong remainder | $2.840874\,10^{200}$ |
| Common unscaled strong bound | $3.026346\,10^{208}$ |

For the last row use $J_1\le N J_N$, so one factor $N^{4/3}$ suffices
in either base window. Complex interpolation gives the actual unweighted
gain $4/3$ for $-4/3\le s\le0$.
It does not grant every positive $s$, a fixed Gevrey/analytic weight,
or any same-width source estimate.

## 9. Complete sources and exact reconstruction

The unchanged original physical right hand side of (D.3) is

$$
\mathscr R^*(t-h_{\rm cap}),\qquad
t=(s_{\rm neg},\,i\sqrt{\pi c_A/\ell}\,\lambda).
$$

The two components of $\lambda$ are the independent physical regular
mean fluxes. The full negative affine source has the original five
ordinary source spaces from the central scattering theorem. Neither
root mean is removed.

After the actual triangular operation the source is
$L_e\mathscr R^*(t-h_{\rm cap})$.
Its base cost is at most two, since $\mathscr R$ is unitary.
The final root-circle operation costs $q_{C,0}$.
The subsequent positive rotation, negative linear reflection and
orthogonal cone split cost one.
The directed final base source bounds are

| Original source space | Final $L^2$ output bound |
|---|---:|
| Complete strict-core ordinary source | $1.070903\,10^{67}$ |
| Either canonical-root ordinary source | $1.306068\,10^{69}$ |
| Either correctly pulled tilted-graph source | $1.222833\,10^{55}$ |
| Negative five-space Euclidean direct sum | $1.847091\,10^{69}$ |
| Paired positive local ordinary source | $116513.354388$ |
| Paired positive local weak source | $58250.796151$ |
| Two independent physical regular mean fluxes | $466.965917$ |

These are exactly the earlier physical source norms multiplied by
$2q_{C,0}$. In particular the graph source remains
$(L-\chi)f_c/q$ in its actual foliation measure, and the canonical source
retains its exact height/density factor. A weak source is not renamed
an ordinary density.

For reconstruction, first undo the cone reflection and positive rotation.
The latter inverse is $Q_{-\omega}$ on the positive cone; the former
inverse is the same $J_{\rm ref}$. Reassemble both cones and the first
root mean, undo $Q_C$ by $Q_C^{-1}$, and finally apply $R_e$.
The complete base bound is

$$
2q_{C,0}<124.036203.                                     \tag{D.40}
$$

The maps in (D.6) have exact triangular inverses, and all source and
reconstruction operations retain their actual regular and mean rows.
No homogeneous regular condition has replaced a nonzero independent
regular source.

The table is a base-source theorem. Applying an inverse with one
derivative loss will require its corresponding stronger source window;
that additional statement is not inferred from this table.

## 10. Executed input and exact scope

The complete consumer is
scripts/fourfold_actual_return_symmetric_density_normal_form.py.
It binds the full word, graph, strict, cap, source, root and actual final
circle reports, verifies the exact finite initial-label identity, and
reuses all original native geometry. Its only new finite geometric
evaluation is the closed 2048-cell derivative cover of the already
specified exact finite $H$.

The small report is
notes/2026-11-13-actual-two-cone-density-normal-form.json.
It contains every directed factor, each word count, the entire inverse
jet calculation, both strong windows, all final source columns, and
the unchanged full analytic nonmean phase bounds.

Reproduce from the topic directory:

~~~bash
python3 scripts/fourfold_actual_return_symmetric_density_normal_form.py \
  --out notes/2026-11-13-actual-two-cone-density-normal-form.json
~~~

The consumer requires a fresh output path. All displayed values above
are outward rounded from full Arb intervals.

This closes the same-object identification of $b_\pm$ and the full base
unweighted $R_*$ for the old complete feedback. It leaves explicit the
remaining effective tasks: a useful high-frequency remainder bound and
cutoff, every actual finite-head/mean/regular Schur row, the required
stronger ordinary-source window, and any positive angular-weight
estimate needed by the nonlinear inverse. No completion flag for those
tasks is set by this theorem.
