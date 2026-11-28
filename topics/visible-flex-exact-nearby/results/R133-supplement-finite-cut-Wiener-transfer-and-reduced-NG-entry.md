# R133 FWT: finite-cut Wiener transfer and the reduced actual NG entry

2026-11-28, visible-exact-astra-b0d5a16-20261128 / cap_world.

**New analytic consequence of the complete W and NG objects.**
At the same true cut $L=9/10$, let $c_L$ be NG's full raw moving
Euclidean-pair low96 $L^2$ error and let $h_H$ bound its complete
high96 $H^1$ error. The actual physical nonmean curvature satisfies

$$
\boxed{\quad
\|\gamma\|_{A^0_\theta}
\le\frac{13}{200}|\delta|+4c_L+\frac1{16}h_H .
\quad}                                                        \tag{FWT.1}
$$

Here it suffices that $c_L\le10^{-11}$ and $h_H\le2^{-10}$.
The finite low part is transferred through an entire Wiener inverse
angle. The unknown high part is used only in a real $H^1$ estimate.
Both means, the one original reflection normalization and all
physical frequency factors remain explicit.

Consequently, for the actual selected $\delta_*$, NG's complete
whole-collar rows give the improved sufficient entry

$$
\boxed{\quad
64c_L+\min\{145Z_S+748Z_L,\ 489Z_S+10Z_L\}
\le1.74\,10^{-11}.
\quad}                                                        \tag{FWT.2}
$$

The original full-collar state hypothesis and the three unknown
receivers are still required. This theorem does not assign them
values, produce an exact core solution or replace the independent
high $H^{8193}$ tail gate. It supplies a strictly weaker explicit
low entry condition, without changing any successful numerical
target or mixing entries from different NG rows.

## FWT.3. Same selected cut and complete finite-frequency lift

Use exactly the definitions and accepted complete scalar data of
[W](R133-supplement-known-finite-cut-Wiener-angle-and-sharp-low-curvature-entry.md).
Thus $Q_\delta=Q_0+\delta Z$, $|\delta|\le d=10^{-10}$,
the true cut is $L=9/10$, $\eta=\eta_0$ is fixed, and the negative
mean $m_\delta=\Pi v_\delta$ is retained. The known $v_\delta$
has angular degree at most96. Moving and physical frequencies
are $4j$; circle measure is normalized. Set

$$
h=1/256,\quad \sigma=1/4096,\quad R_X=15/4096,
\qquad \|a\|_{A_h}=\sum_{j\in\mathbb Z}e^{4h|j|}|a_j|.
\tag{FWT.3}
$$

For any real degree96 function $w$, including its mean, weighted
Cauchy--Schwarz gives

$$
\|w\|_{A_h}
\le\left(1+2\sum_{j=1}^{96}e^{j/32}\right)^{1/2}\|w\|_2
\le37\|w\|_2.                                          \tag{FWT.4}
$$

To verify the elementary constant without a new enclosure of the
old cut, monotonicity yields
$\sum_{j=1}^{96}e^{j/32}\le32e^{1/32}(e^3-1)$.
The series inequalities $e^{1/32}<32/31$ and $e<11/4$ imply
$e^3<21$. Therefore the squared coefficient is less than
$1+40960/31<37^2$. Both signed directions and the mean occur in
this calculation. No factor $384$ has been used to replace the
finite low norm by an $H^1$ norm.

Split the actual second-component error at this cut as

$$
v-v_\delta=w+q,\qquad
w=\Pi_{\le96}(v-v_\delta),\quad q=H_{96}(v-v_\delta),
\quad \varepsilon=\|w\|_2\le c_L\le10^{-11}.
\tag{FWT.5}
$$

In particular $\Pi q=0$ exactly. The projection of the reflected
real state has the same even parity. Introduce only the actual
intermediate finite function

$$
v_f=v_\delta+w,\quad m_f=m_\delta+\mu,\quad
\mu=\Pi w,\quad j_f=v_f/m_f.                            \tag{FWT.6}
$$

This function is not assumed to solve a PDE. Its role is to use the
known finite angular support before the separate real value-map
estimate is applied. It is never substituted for the original
selected background in a Green inverse.

## FWT.4. Complete inverse angle and reciprocal of the finite perturbation

W.4, W.11, W.18 and W.3 give

$$
|m_\delta|>16/5,\quad
\|j_\delta-1\|_{A_h}<7/500<1/64,\quad
\|v_\delta^{-1}\|_{A_h}\le20/63,
\quad \|(j_\delta)_\phi\|_{A^0}<.054057.                 \tag{FWT.7}
$$

For the last bound use W.10 directly and
$\|e_\phi\|_{A^0}<2.456636503$; this is a finite selected
perturbation of W's already accepted complete base derivative.
It does not evaluate a new cut coefficient.

Since $|\mu|\le\varepsilon$,
$|m_f|>16/5-\varepsilon>25/8$, with $m_f<0$. The exact mean-aware
identity

$$
j_f-j_\delta=\frac{w-j_\delta\mu}{m_f}
\tag{FWT.8}
$$

and (FWT.4) imply

$$
\|j_f-j_\delta\|_{A_h}
\le\frac8{25}\left(37+\frac{507}{500}\right)\varepsilon
\le13\varepsilon.                                     \tag{FWT.9}
$$

Thus $\|j_f-1\|_{A_h}<7/500+13\varepsilon<1/64$ and

$$
\|I(j_f-1)\|_{A_h}
<7/2000+13\varepsilon/4<R_X.                            \tag{FWT.10}
$$

The complete contraction used in W.14--16 therefore constructs
the actual inverse $\Phi_f=\mathrm{id}+X_f$ in the same
closed $A_\sigma$ ball as $\Phi_\delta$.
Its Lipschitz constant is less than $1/64$; its self-map property
is (FWT.10). Subtraction of the two fixed-point equations gives

$$
\|X_f-X_\delta\|_{A_\sigma}
\le\frac{64}{63}\frac14
                \|j_f-j_\delta\|_{A_h}
\le\frac{208}{63}\varepsilon.                          \tag{FWT.11}
$$

Both inverses have the original reflection constant. Positivity
$j_f>63/64$ identifies the fixed point with the true real inverse
of the same increasing lift. An independently shifted physical
angle is not introduced.

The full reciprocal series also converges. From (FWT.4),(FWT.7),

$$
\|v_f^{-1}\|_{A_h}
\le\frac{20/63}{1-(20/63)37\varepsilon}<\frac{159}{500}.
\tag{FWT.12}
$$

The known selected reciprocal derivative has a useful uniform
bound on this same width. W.9 and finite-band lifting of $e_\phi$
give

$$
\|(j_\delta)_\phi\|_{A_h}
<\frac53(.054057)+\frac5{16}(13)d<\frac{91}{1000}.
$$

Here $\|e_\phi\|_{A_h}<5\|e_\phi\|_{A^0}<13$.
Consequently

$$
\|(v_\delta^{-1})_\phi\|_{A_h}
\le\frac5{16}\left(\frac{64}{63}\right)^2\frac{91}{1000}
<\frac3{100}.                                         \tag{FWT.13}
$$

This estimate concerns the known finite selected reference and
its complete reciprocal; no unknown derivative is being bounded.

Put $C_f=v_f^{-1}\circ\Phi_f$. The exact decomposition is

$$
C_f-C_\delta
=(v_f^{-1}-v_\delta^{-1})\circ\Phi_f
  +v_\delta^{-1}\circ\Phi_f-v_\delta^{-1}\circ\Phi_\delta.
\tag{FWT.14}
$$

W's complete composition estimate, (FWT.4),(FWT.11--13) yield

$$
\begin{split}
\|C_f-C_\delta\|_{A_\sigma}
&\le\left(37\frac{20}{63}\frac{159}{500}
         +\frac3{100}\frac{208}{63}\right)\varepsilon\\
&=\frac{671}{175}\varepsilon\le4\varepsilon.
\end{split}                                                    \tag{FWT.15}
$$

The complete physical means are still
$\Pi_\theta C_f=1/m_f$ and $\Pi_\theta C_\delta=1/m_\delta$.
They occur in (FWT.14); no mean is set to zero. Their independent
matching equation remains, even though the nonmean projection of
(FWT.15) is contractive.

## FWT.5. Reverify every reference hypothesis before using the real high part

The reference assumptions of
[J.4](R133-supplement-shape-and-mean-separated-physical-inner-curvature-trace.md)
must be paid for $v_f$, not merely cited for $v_\delta$.
The mean and $63/64<j_f<65/64$ were just proved. Since the exact
difference (FWT.8) has degree at most96,

$$
\|(j_f)_\phi\|_\infty
<.054057+384(13)\varepsilon<1/16.                       \tag{FWT.16}
$$

For the physical curvature derivatives, combine W.1 and (FWT.15)
before applying a derivative estimate to the complete analytic
function:

$$
\|C_f-\widehat C\|_{A_\sigma}
\le(13/200)d+4\varepsilon\le4.65\,10^{-11}.
\tag{FWT.17}
$$

The complete already paid reference bounds used in W.27 give

$$
\begin{split}
\|(C_f)_\theta\|_{A^0}
&<.020269146+4096(4.65\,10^{-11})<1/48,\\
\|(C_f)_{\theta\theta}\|_\infty
&<24(.020269146)+2(4096)^2(4.65\,10^{-11})<1/2.
\end{split}                                                    \tag{FWT.18}
$$

In particular $\|(C_f)_\theta\|_\infty<1/32$ and
$\|P_{\ne0}C_f\|_{A^0}<1/192$. Equations (FWT.6),(FWT.9),
(FWT.16),(FWT.18) establish every part of J.4 for this precise
intermediate function. This is a new finite-reference construction;
it is not a $C^0$ to $C^1$ inference about an arbitrary unknown.

Now suppose $\|q\|_{H^1}\le h_H\le2^{-10}$. Apply the real
shape theorem J.1 with reference $v_f$ and perturbation $q$.
Its mean is exactly zero by (FWT.5), so its full shape/mean formula
reduces to

$$
\|P_{\ne0}(C(v)-C_f)\|_{A^0_\theta}
\le\frac1{16}\|q_\phi\|_2\le\frac1{16}h_H.
\tag{FWT.19}
$$

The unknown $q$ is evaluated only on the real circle. Its actual
inverse angle is the one in J.3; no high-frequency analytic strip
is assumed. Adding W.24, (FWT.15) and (FWT.19) proves (FWT.1).
The proof works for all finite low corrections in the stated
ball, rather than for one convenient trial or one collocation
output.

## FWT.6. Consume the entire actual NG rows in their original units

The successful
[NG actual conclusion](R133-supplement-actual-adjustable-nested-collar-geometry-and-direct-angular-trace.md)
remains unchanged. Assume its original same real continuous
two-sided $H^1$ state on $[17/20,19/20]$, residual-zero equation,
full selected difference $C^0$ radius $\rho=10^{-4}$ and original
mean/log-speed conditions. Let $Z_L,Z_S$ be exactly its ordinary
$dr$ norms of the original radial $P$-weighted low96 and shell33..96
states. Let $c_L$ be its raw unweighted complete pair trace in
NGA.4. Both means belong to $Z_L$ and $c_L$. No second $P$,
amplitude scaling or change of angular measure occurs.

Its two complete whole rows imply

$$
h_H<1.012\,10^{-11}+B,
\quad B=\min\{145Z_S+748Z_L,\ 489Z_S+10Z_L\}.
\tag{FWT.20}
$$

Each expression is a full NC or BD row for the same selected
geometry. The minimum chooses a full valid bound; coefficients
from the two rows are not exchanged. The constant contains the
full original source and conditional high-body contribution.
No old upper is subtracted to obtain an unknown source or trace.

For the actual selected member use the already proved whole bound

$$
|\delta_*|<d_*=
\frac{9368259853002}{10^{23}}
\tag{FWT.21}
$$

from the original NIF/NA selected identity. Condition (FWT.2)
implies $c_L\le2.71875\,10^{-13}<10^{-11}$ and
$h_H<2.752\,10^{-11}<2^{-10}$, so the domain of (FWT.1) has
been verified by the same gate. Its actual curvature consequence is

$$
\begin{split}
\|\gamma\|_{A^0_\theta}
&<\frac{13}{200}d_*+
              \frac{1.012\,10^{-11}+1.74\,10^{-11}}{16}\\
&=7.8093689044513\,10^{-12}
 <\frac{10^{-9}}{128}.
\end{split}                                                    \tag{FWT.22}
$$

Thus the original physical tail low-entry inequality is strict.
Uniformly for all $|\delta|\le10^{-10}$, the same proof instead
accepts the explicit gate $64c_L+B\le1.08\,10^{-11}$, whose
curvature upper is $7.8075\,10^{-12}<10^{-9}/128$.

The original NGA.7 required $385c_L+B\le9.5\,10^{-12}$.
Every such input passes (FWT.2). When $B=0$, the new allowed
$c_L=2.71875\,10^{-13}$ is more than eleven times its old
$9.5\,10^{-12}/385$ allowance. These are comparisons of two
sufficient conditions, not reported values of the unknown traces.

## FWT.7. Remaining matching and geometry responsibilities

The known cut difference has full $H^1$ size bounded by
$|\delta_*|(\|\zeta\|_{A^0}+\|\zeta_\phi\|_{A^0})<4d_*$.
The finite low part has $H^1$ norm at most $385c_L$, and the high
part is bounded by (FWT.20). Under (FWT.2) their total is far below
$2^{-10}$. Thus the original real low neighbourhood used in the
physical value-map and higher-tail conversion is preserved.

The separate same-state $H^{8193}$ hypothesis is unchanged. This
proof does not derive it from (FWT.20), extrapolate a narrow
high-regularity collar to the entire core, or turn the low-entry
inequality into a Lipschitz estimate for two unrelated states.
The full physical $B$ function, independent $C$ mean and all
waist/phase/world equations remain to be solved.

Likewise a completed right cap in its $10^{-4}$ moving ball pays
only its actual right-hand portion of the collar. It does not
supply the left side, a state matching at $L$, $Z_L$, $Z_S$ or
the fullcore $C^0$ estimate. After those equations and complete
frame periodicity are genuinely solved, the final geometry theorem
may identify the waist mean and propagate position periodicity.
They cannot be assumed in advance to delete an independent mean
or holonomy equation. The eventual metric is frozen only for the
same solved member, with the original fixed $\eta_0$ and one
world height constant.

## FWT.8. First exact-rational consequence check

`scripts/fourfold_codazzi_finite_cut_wiener_saved_bounds.py` has one
new execution with all19 comparisons passed. Its whole source SHA256
is `5e9e19e5d5129cc2b21d4aad46bfd95b1396698155fed32af83b7bbc37bc2f8c`.
The entire3910-byte result has SHA256
`3e4b4329a8ef28b81fb5662ccff5817f25ec8fe9c5eb91fd4328d98860be08cb`.
It checks the finite Wiener coefficient, complete inverse-angle and
reciprocal domains, every new J.4 constant, both new NG entry gates
and the full original real low neighbourhood. All arithmetic is
exact rational arithmetic on the displayed proved constants.

The script first reads the two whole original successful cut/NG
scientific publications and checks their existing SHA256 identities.
It calls none of their scientific producers. All old coefficients,
geometry selections, integral bounds and verdicts remain untouched.
The new output explicitly records that no values have been assigned to
the unknown $c_L,Z_L,Z_S$, and retains the unproved fullcore/topic status.
