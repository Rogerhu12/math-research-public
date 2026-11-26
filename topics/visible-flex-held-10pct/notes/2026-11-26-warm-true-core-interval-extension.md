# True-core interval inputs for the R65 and R68 phase families

Date: 2026-11-26. Session: Astra-held10-06bbeb395471 / fixed_metric.

This extends the mathematical core-input interface used in R62. It does
not reuse R62's old lambda-.002 coefficients, inverse radius, beta bound,
Gamma derivative constants, metric bounds, or geometry bounds. It does not
certify a new field, a complete prefix, a true tail, or a closed family.
The new reusable part is a proved parameter-dependent interval construction
and its executed small API check. The real-field exporter is gated on a
genuinely accepted versioned warm field and defaults to literal lambda one.

## 1. Precisely the core being enclosed

Let the original frozen support data have frequencies `m=3j`, and define

\[
 A(\phi)=\phi+\sum_m\frac{b_m}{m}\sin(m\phi),\qquad
 b_m=(1-m^2)a_m,\qquad
 \rho(\phi)=A'(\phi)=1+\sum_m b_m\cos(m\phi).
\]

Every saved coefficient `a_m`, physical phase control `d_j`, lambda, `S`,
transition width `b`, and target curvature `k` is interpreted as its exact
saved binary rational. The period is the mathematical `P=2*pi/3`, not the
source's rounded period. Write `L=P/2` and `phi_0=A^{-1}`. This sufficient
oracle requires

\[
 B_0:=\sum_m|b_m|<1,
 \quad \rho_-=1-B_0,\quad\rho_+=1+B_0,
 \quad S+b<L,\quad k>0,\quad0<\lambda\le1.
\]

Thus `1/rho_+ <= kappa_0=phi_0' <= 1/rho_-`. This is an explicitly checked
sufficient support-inverse domain, not a claim that every convex support
core satisfies the l1 condition.

Let `W` be the same symmetric complement window as R53/R65. In its
transition it is the exact polynomial

\[
 W(t)=126t^5-420t^6+540t^7-315t^8+70t^9,
 \qquad W'(t)=630t^4(1-t)^4,
\]

and it is zero on the protected arc and one outside the transition.
The original R53 true phase is `Phi_0(u;lambda)`, with its beta computed
from the true inverse and exact window integral. The new phase is

\[
 \Phi(u)=\Phi_0(u;\lambda)+
 \sum_{j=1}^{M}\frac{d_j}{N_j}\frac{W(u)\sin(\omega_j u)}{\omega_j},
 \qquad \omega_j=3j,
 \quad N_j=1+\frac{630}{256b\omega_j}.
\]

The normalization `N_j` in this mathematical definition is exact; the
source's floating evaluation is not substituted for it. The numerical
provider evaluates this same declared formula approximately. Its actual
cached values are compared with independently obtained interval outputs,
and the complete prefix is to be audited again using those true inputs.

With `nu=exp(i Phi)`, the normalized closed curve is defined by true
integration of `Gamma'=i nu`. Its sector translation is fixed by

\[
 J=\int_0^P i e^{i\Phi(u)}\,du,
 \qquad \Gamma(0)=\frac{J}{e^{iP}-1}.
\]

The phase satisfies `Phi(P-u)=P-Phi(u)`: the baseline has this symmetry,
`W(P-u)=W(u)`, and `sin(3j(P-u))=-sin(3ju)`. Therefore the normalized origin
is real. The code still checks that its independent imaginary-origin
interval contains zero; it does not erase a floating imaginary residual.
Rotation extends the sector to the complete true-period curve.

The new phase increment is globally C4, because `W` is C4. Consequently
the new curve is at least C5. The old R53 C6 label is not transferred.
The derivatives through Gamma4 needed below exist continuously.

## 2. A fresh inverse radius and a fresh beta bound

For a positive rational strip width `r`, set

\[
 B(r)=\sum_m |b_m|\cosh(mr).
\]

Choose `r` with `B(r)<1`. On every disc `|w|<=r` about a real inverse
point, the nonlinear part of `A(phi+w)-A(phi)` has derivative bounded by
`B(r)`. Hence its boundary modulus is at least `r(1-B(r))`. Rouche's theorem
gives a single inverse branch for every material disc of radius

\[
 R<r(1-B(r)),
\]

and its displacement from the center inverse point is bounded by `r`.
The local branches agree with the unique real inverse, so they provide the
uniform analytic continuation needed for the inverse Taylor remainder.
The implementation starts with `r=1/16`, halves until a rigorous upper
bound for `B(r)` is below `(1+B_0)/2`, and takes
`R=3*r*(1-B_upper)/4`. All inequalities are checked with outward bounds.

The exact dyadic inverse Taylor construction and its Cauchy tail are the
R62 construction, applied to these newly computed data. It uses a floating
inverse only as a seed for interval Newton; the seed is never accepted as
an exact inverse value. Taylor cells have half-width at most `R/8`.

There is also a coarse beta bound available before doing any numerical
primitive. Let `chi=1-W`, and let

\[
 \Omega=\int_0^{S+b}\chi(v)
       \bigl(k-\kappa_0(L+v)\bigr)\,dv,
 \qquad \beta=-\frac{\Omega}{L-S-b/2}.
\]

Since `integral chi=S+b/2`,

\[
 |\beta|\le
 \frac{(S+b/2)
 \max\{|k-1/\rho_-|,|k-1/\rho_+|\}}
 {L-S-b/2}=:\beta_*.
\]

This bound does not assume the old numerical `beta<3`, nor does it assume
beta is positive. The actual beta interval is then computed by the already
proved exact window-polynomial primitive and the new inverse Taylor bounds.

## 3. Uniform complex and real curvature bounds for position quadrature

The position primitive is integrated separately on every analytic branch
of the window. It is not declared globally analytic across the C4 joins.
For a radius `R_p<=R`, put

\[
 \eta=R_p/b,\qquad s=1/4+\eta+\eta^2,
 \quad W_c=1+630\eta s^4,\quad W_{1c}=630s^4/b.
\]

These bound the analytic extension of each relevant window piece and its
first material derivative about any real point of that piece. Indeed,
`|t(1-t)| <= 1/4+eta+eta^2`; integrate the derivative from a real point,
where `0<=W<=1`, to bound `W` itself. Constant window pieces obey the same
bounds. Let `K_0=(1-B_upper)^(-1)`. The baseline curvature obeys

\[
 |\kappa_{base}|\le
 K_0+\lambda\bigl((1+W_c)(k+K_0)+\beta_* W_c\bigr).
\]

For the new controls, the inequalities
`|sin(omega z)|,|cos(omega z)| <= exp(omega R_p)` give the additional bound

\[
 \sum_j\frac{|d_j|}{N_j}
 \left(W_c+\frac{W_{1c}}{\omega_j}\right)e^{\omega_jR_p}.
\]

Their sum is a computable `K_c(R_p)`. Halve `R_p` until the rigorous
inequality `R_p K_c(R_p)<1/2` holds. The phase is real on the real axis;
therefore `|Im Phi(u+z)| <= K_c|z|` on the chosen analytic extension and

\[
 |i e^{i\Phi(u+z)}|\le e^{1/2}<2.
\]

This supplies the position-integral Cauchy bound without reusing the old
`kappa<2.5` estimate. All integration intervals are split at both true
window joins, the sector midpoint, sector ends, and dyadic Taylor cells.
When a boundary is enclosed by a tiny interval, both of its dyadic
endpoints and the intervening microscopic interval are covered.

A valid coarse real bound is

\[
 K_r=1/\rho_-+
 \lambda(k+1/\rho_-+\beta_*)+\sum_j|d_j|.
\]

The last term follows from `|W cos+W' sin/omega|/N_j <= 1`.

For GL12 on a real interval of length `ell` inside one analytic piece,
Cauchy's estimate and the exact Gauss remainder give the component error

\[
 2\ell C_{12}(\ell/R_p)^{24},\qquad
 C_{12}=\frac{(12!)^4}{25(24!)^2}.
\]

The inherited exact Legendre root brackets and exact polynomial
evaluations also bound the distances from the literal NumPy nodes/weights
to the true GL12 rule. If these bounds are `epsilon_x` and `epsilon_w`
(the latter the sum of weight errors), their additional error is at most

\[
 \ell\epsilon_w/2+K_r\ell^2\epsilon_x/2.
\]

For a partition one can replace `ell^2` by total length times maximum
piece length. Thus neither the floating quadrature rule nor a blanket
libm accuracy assertion is used as an exact primitive.

## 4. True Gamma3/Gamma4 and physical-control l1 bounds

Write `c_j=d_j/N_j` and `Delta Phi=sum c_j W sin(omega_j u)/omega_j`.
Direct differentiation gives

\[
\begin{aligned}
 \Delta\kappa&=\sum_j c_j\left(W\cos\omega_j u+
                       W'\sin\omega_j u/\omega_j\right),\\
 \Delta\kappa'&=\sum_j c_j\left(2W'\cos\omega_j u+
                    (W''/\omega_j-W\omega_j)\sin\omega_j u\right),\\
 \Delta\kappa''&=\sum_j c_j\left((3W''-W\omega_j^2)\cos\omega_j u+
                    (W'''/\omega_j-3W'\omega_j)\sin\omega_j u\right).
\end{aligned}
\]

The interval oracle evaluates these formulas on each true material box.
Useful global, finite-control norm bounds also follow by setting

\[
 A_r=\sum_j |d_j|\omega_j^r/N_j,\quad r=-1,0,1,2,
\]

and using

\[
 D_1=630/(256b),\quad D_2=2520/(64b^2),
 \quad D_3=(7560/16+5040/64)/b^3.
\]

Then

\[
\begin{aligned}
 |\Delta\Phi|&\le A_{-1},\\
 |\Delta\kappa|&\le A_0+D_1A_{-1},\\
 |\Delta\kappa'|&\le A_1+2D_1A_0+D_2A_{-1},\\
 |\Delta\kappa''|&\le A_2+3D_1A_1+3D_2A_0+D_3A_{-1}.
\end{aligned}
\]

These use the actual physical controls read from the reconstructed core,
not a guessed interpretation of auxiliary `p` or a legacy support vector.
They therefore also expose any versioned parameter-scale difference.

The required Cartesian material jets are

\[
\begin{aligned}
 \Gamma'&=i\nu, &\Gamma''&=-\kappa\nu,\\
 \Gamma'''&=-(\kappa'+i\kappa^2)\nu, &
 \Gamma''''&=(\kappa^3-\kappa''-3i\kappa\kappa')\nu.
\end{aligned}
\]

Consequently their norms are bounded directly by

\[
 |\Gamma'''|=\sqrt{(\kappa')^2+\kappa^4},\qquad
 |\Gamma''''|=\sqrt{(\kappa^3-\kappa'')^2+9\kappa^2(\kappa')^2}.
\]

These exact squared expressions are nonnegative. Intersecting an outward
interval for such a square sum with `[0,infinity)` before taking its square
root is valid; it only removes tiny negative lower endpoints introduced
by outward rounding of zero. No Frenet-domain quantity is clipped.

Positive curvature of the complete new core is checked on a covering
partition, with local subdivision if a lower bound is unresolved. Failure
to prove positivity is an explicit failed input certificate, not permission
to reuse a floating guard or old positive bound.

## 5. The unchanged mean rule and the new output contract

The mean graph uses the literal array
`2*np.pi*np.arange(1168)/1168`, SHA-256
`f4834f978de38046e374b020d2a928d293fc405f794159e40e2271f4ee9bd9cf`.
Each entry is an exact binary rational. It is **not** replaced by the
mathematical uniform angle `2*pi*j/1168`. The core itself still has the true
mathematical period. This separates two different definitions correctly.

At each unchanged literal `psi`, the exporter rigorously evaluates
`theta0=psi-e*sin(3psi)/3`, the true core jets there, and the complete actual
finite projection vector `I=initial(p)`. It constructs

\[
 H(\psi)=\Gamma(\theta_0(\psi))-e^{i\theta_0(\psi)}-q\,I\cdot B(\psi)
\]

and its first two psi derivatives by the exact chain rule. No new projection
or mean normalization is inserted. The arrays `H,H1,H2` have shape
`(2,1168,3)`, where the first axis is lower/upper. The array hash, literal
node hash, run/raw/physical identities, actual current mode count, provider,
loader, oracle and interval kernel are bound in the JSON certificate.

`warm_export_true_core_inputs.py` writes `mean1168-core.json` and
`mean1168-core-intervals.npz`. Optional `--external-nodes N` writes
`external-core.json` and `external-core-intervals.npz`, with point and full
closed-angle-box jets through Gamma4. These arrays have the R62 field
names so the dynamic-M continuation of its metric/mean algorithms can
consume them. The certificate's `complete=true` means the explicitly
named core-input construction completed; `complete_surface=false` remains
explicit. The default gate requires actual accepted lambda one. An
intermediate lambda needs an explicit diagnostic flag and is labelled.

The actual-DN branch uses the separate strict actual-DN acceptance helper
and its read-only geometry adapter. It never silently replaces an actual
nonlinear boundary by the linear one for acceptance.

## 6. Executed API check and remaining work

`check_warm_true_core.py` actually constructed a small synthetic M2 core
at lambda one with nonzero controls approximately `(0.001,-0.0002)`.
This was not a BVP field. The true inverse, weighted primitive, true beta,
position primitive, and continuous curvature-jet boxes ran in 25.7 seconds.
At eleven test angles the floating source F/Ft/Ftt lay within the independent
intervals; the maximum position interval width was `1.61e-12`. The protected
center interval enclosed the literal target curvature and zero derivative
jets. The whole synthetic sector received a positive curvature lower bound.
These small-example constants are not transferred to any actual candidate.

R62's field/profile/chart exact shared-C2 representation remains applicable
algebraically after explicit mode-count generalization. The actual new
field must nevertheless recompute its endpoint corrections, radial mean
integral, full relative metric, curvature/support/diameter, central patch,
bridge seam, and all full-tail and closed-family quantities. The oracle
does not pay any of those obligations or establish a C2 limit.

The first checkpoint supported exactly the R65 full-period frequencies
`omega_j=3j`. The extension below adds the explicitly different R68/v3
complementary-arc family. Neither its finite span nor its new numerical
bounds are identified with the R65 family.

## 7. Explicit v3 complementary-arc extension

To avoid a notation conflict with the sector halfperiod used above, put
`L0=P/2=pi/3` and `Lc=L0-S`. The exact v3 definition is

\[
 \omega_j=\frac{j\pi}{L_c},\qquad
 v(u)=\begin{cases}u,&u<L_0,\\u-P,&u>L_0,\end{cases}
 \qquad
 \Delta\Phi(u)=\sum_{j=1}^M
       \frac{d_jW(u)\sin(\omega_jv(u))}{\omega_j+D_1},
 \quad D_1=\frac{630}{256b}.
\]

Here the local material input lies in one true sector `[0,P]`; periodic
extension handles the other sectors. The source's binary64 period, `Lc`,
frequencies, and denominators are evaluation approximations only. The
oracle constructs `P`, `Lc`, and every `omega_j` from outward high-precision
intervals for the mathematical pi and the exact frozen rational `S`, then
converts outward to binary intervals. It verifies `Lc>b>0`. The same true
frequency formula is used for every truncation, and no frequency fitting
or interpolation from a saved floating array is permitted.

The coordinate has a branch change at `L0`, which lies strictly inside
the open protected interval `(L0-S,L0+S)` where `W` and its first four
derivatives vanish. Thus the physical phase increment is identically zero
near that branch change. Outside it, `dv/du=1`. A query provably on one
side uses that branch; an unresolved query encloses both branches. An
interval crossing the midpoint uses the interval absolute value and the
sign interval `[-1,1]` for the window derivatives, rather than choosing
the sign of a sampled midpoint. The exact protected zero is returned when
all needed window jets vanish. A query too wide for the inherited local
inverse/trigonometric enclosures must be subdivided; it is not accepted
by interpreting a midpoint as the whole box.

At sector ends, `v=0` on both sides after periodic extension and the window
is locally constant one, so this phase increment is analytic across the
periodic cut. At a protected endpoint, `v=+/-Lc` and `sin(omega_j v)=0`.
The fifth-order vanishing of `W` therefore gives sixth-order vanishing of
each product there. At the join with the region `W=1`, the difference from
the constant window has only fifth-order vanishing in general. Hence the
whole phase basis is globally at least C4 and the curve at least C5;
this argument does not assert global C5 regularity for the phase basis.
All joins used by the position integral are in the true partition:
sector ends, `L0`, `L0+/-S`, `L0+/- (S+b)`, transition midpoints, and the
dyadic inverse cells. No special cut is required at an interior sine zero.

Reflection gives `v(P-u)=-v(u)` away from the protected branch point.
Together with the symmetric window, the increment is odd under
`u -> P-u`. The same true phase-reflection and normalized-closure argument
from section 1 therefore applies. The independent imaginary-origin
interval must still enclose zero. At lambda one, the whole protected
interval has exactly the prescribed baseline constant curvature; the new
phase is identically zero there. This fact concerns the core alone and
does not supply an uncomputed surface or a closed family.

Let `c_j=d_j/(omega_j+D1)` and let `s_j=sin(omega_j v)`,
`cbar_j=cos(omega_j v)`. Differentiation on each nonzero window branch gives

\[
\begin{aligned}
 \Delta\Phi&=\sum_j c_jWs_j,\\
 \Delta\kappa&=\sum_j c_j(\omega_jW\bar c_j+W's_j),\\
 \Delta\kappa'&=\sum_j c_j\bigl(2\omega_jW'\bar c_j+
                      (W''-\omega_j^2W)s_j\bigr),\\
 \Delta\kappa''&=\sum_j c_j\bigl((3\omega_jW''-\omega_j^3W)\bar c_j+
                      (W'''-3\omega_j^2W')s_j\bigr).
\end{aligned}
\]

The zero extension makes these the continuous phase-through-third jets
also at every join. The oracle evaluates them using the true frequency
intervals. The core Gamma3/Gamma4 formulas in section 4 are unchanged.

For position quadrature, the additional complex curvature bound is now

\[
 \sum_j|d_j|\,
 \frac{\omega_jW_c+W_{1c}}{\omega_j+D_1}
 e^{\omega_jR_p}.
\]

This uses the analytic continuation of the current piece; translating the
real coordinate by `P` does not change its imaginary part. A protected
piece has the zero continuation. The frequency intervals and outward
exponentials produce a rigorous upper bound. The radius-halving rule,
real bound `Kr`, exact GL12-rule brackets, and its new position error then
follow exactly as in section 3. The inequality
`(omega*|W|+|W'|)/(omega+D1) <= 1` on the real axis still gives the
`sum |d_j|` term of `Kr`. This is an algebraic reuse of the proof, not a
reuse of its old numeric radius or constants.

For useful global control bounds define the true quantities

\[
 C_r=\sum_j\frac{|d_j|\omega_j^r}{\omega_j+D_1},
 \qquad r=0,1,2,3.
\]

If the true frequency is enclosed by rational endpoints
`0<omega_j^- <= omega_j <= omega_j^+`, the exact rational

\[
 C_r^+=\sum_j
 \frac{|d_j|(\omega_j^+)^r}{\omega_j^-+D_1}
\]

is an upper bound for `C_r`. It is not labelled the exact value of the
generally irrational sum. With the same rigorous `D1,D2,D3` as section 4,

\[
\begin{aligned}
 |\Delta\Phi|&\le C_0^+,\\
 |\Delta\kappa|&\le C_1^++D_1C_0^+,\\
 |\Delta\kappa'|&\le C_2^++2D_1C_1^++D_2C_0^+,\\
 |\Delta\kappa''|&\le C_3^++3D_1C_2^++3D_2C_1^++D_3C_0^+.
\end{aligned}
\]

The stored metadata says `phase_l1_rational_upper_bounds` and binds both
frequency endpoints. These bounds can also be applied to the difference
of two physical `d` vectors after zero extension, provided the entire
baseline, true frequency rule and window are identical. Such a finite
difference estimate by itself is not a proof of a Cauchy limit.

## 8. v3 bindings and the executed small check

The exporter now accepts explicit v2 and v3 linear model kinds through
their own `accepted_input`; the true-DN kind continues through the separate
strict `accepted_actual_input` and read-only geometry loader. The v3 input
also checks the actual core family against the complete declared
`phase_basis`. Its JSON includes the full `warm_definition`, its canonical
SHA, `phase_basis`, `linear_source_model_kind`, both `basis_anchor_v2_run`
and `basis_anchor_v2_sha256`, the exact original radial-chart record, and
the actual raw and physical hashes. All directly used provider, loader,
oracle, and interval-kernel source files are hashed. The array contract is
unchanged: actual complete initial projection, actual current M, and the
same literal mean1168 nodes. The Fourier state basis remains `3j`; these
state frequencies are not replaced by the new phase-control frequencies.

`check_warm_true_core.py --family v3` actually completed the final synthetic
M2 test at lambda one in 26.94 seconds. It checked 32 angles, including the
two binary neighbours of every true-window join, the branch midpoint, and
the sector endpoints. Floating source positions and first two jets were
inside the independently constructed intervals; the maximum position
interval width was `1.607e-12`. Eight additional material angles passed
an independently differentiated high-precision phase-through-third-jet
diagnostic. The true frequencies were enclosed, the supported increment
at the branch point was exactly zero, and the two sector ends had common
periodic jet enclosures. The full synthetic core curvature partition had
no unresolved positivity cells. These are small API checks on a synthetic
core, not accepted BVP fields, and none of their numerical constants is
transferred to a real field. The real-field exporter has not been run on
an accepted lambda-one candidate in this session.

The same final oracle also reran `--family v2` in 20.98 seconds, preserving
the original R65 path: all eleven source two-jet diagnostics lay inside
their true intervals and its synthetic curvature partition remained
positive. This only checks the retained implementation branch; it does
not create a new research conclusion about an old accepted field.
