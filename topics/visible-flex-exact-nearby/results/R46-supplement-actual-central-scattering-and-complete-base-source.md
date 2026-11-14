# R46 supplement: actual two-ended negative scattering and complete base source wiring

This theorem constructs the complete two-ended scattering operator of the
same actual central negative component. Both nonconstant root-to-physical-cut
connectors and all 215 strict cells have already been paid. The conclusion
is on the entire original R39 root amplitude Hilbert space, including both
root means:

\[
\boxed{\|\mathscr S\|_{L^2\oplus L^2}
       =\|\mathscr S^{-1}\|_{L^2\oplus L^2}=1.}              \tag{S.1}
\]

This is the actual complete scattering, rather than a finite compression
or its leading characteristic map. Its construction requires one infinite
Cauchy block inverse; both its injectivity and surjectivity are proved
below from the true flux identities, with inverse norm at most one.
The affine conversion of a complete Cauchy source has norm at most
\(\sqrt2\).

The two original full positive caps then give a concrete augmented
unitary feedback realization, with both independent regular flux rows
and all source terms retained. No inverse of this feedback is asserted.
The \(4/3\) returned normal form, fixed angular weight, and larger
Sobolev scattering window are separate obligations.

All statements here concern the old complete R74/R94 infinite-tail
Robin realization. A proposed change of a deep tail profile does not
inherit its full cap Poisson or reflection operator. The unchanged
finite body and collars can be reused separately.

## 1. Same exact target, cuts, amplitudes and full Cauchy evolution

The object is
type_fixed_step02_d5_exact_affine_step5_object.json, SHA256
91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848.
The entire parameter box remains

\[
p_5=-7789843107295549/4611686018427387904,\qquad
|p-p_5|\le10^{-9}.
\]

The strict cuts are the exact pair

\[
r=\pm r_c,\qquad
r_c=268136140016943/1125899906842624.
\]

The full negative physical-graph theorem supplies the two-row maps
\(K_L,K_R\) from each original root Airy amplitude to its actual
physical cut amplitude. The left map is the actual radial reflection
of the complete right map, including conormal reversal, height, angle,
the exact mean matrix, and source. It is not a height-only trace map.
The complete strict theorem supplies the actual propagation
\(C_{\rm st}\) from the left cut to the right cut. Therefore

\[
\mathscr T=K_R^{-1}C_{\rm st}K_L                            \tag{S.2}
\]

is the complete root-to-root Cauchy operator.
Every factor is already proved onto with a bounded inverse on \(L^2\)
amplitudes. Thus so is \(\mathscr T\).

Use the original R39 columns

\[
D_\pm(\xi,n)=c\lambda_n^{-1/3}
 [\operatorname{Bi}(-\xi\lambda_n^{2/3})
   \pm i\operatorname{Ai}(-\xi\lambda_n^{2/3})]\quad(n\ne0),
\]

\[
D_\pm(\xi,0)=c(1\pm i\xi/\pi),\qquad
c=(-\operatorname{Ai}'(0)/\operatorname{Ai}(0))^{-1/2}.
\]

Their full determinant is \(-2ic^2/\pi\) at every frequency.
Their flux matrix is exactly

\[
F_*^*\frac{\pi c_A}{2i}
\begin{pmatrix}0&I\\-I&0\end{pmatrix}F_*
=J,\qquad J=\operatorname{diag}(I,-I),\qquad c_A=c^{-2}.
                                                               \tag{S.3}
\]

Each \(\xi\) coordinate points into the negative component: to the
right at the left root and to the left at the right root.
The actual radial reflection proves that the two canonical periods are
equal. All intervening density/height changes preserve the full Green
form. Thus the radial Green identity, first for smooth data and then
by the paid bounded extensions, gives

\[
\mathscr T^*J\mathscr T=-J.
\]

Its already proved onto inverse gives the second identity as well:

\[
\boxed{\mathscr T^*J\mathscr T
       =\mathscr T J\mathscr T^*=-J.}                       \tag{S.4}
\]

The sign is essential: the two inward root coordinates have opposite
physical radial orientations. No weak height trace is identified with
a normalized amplitude, and no unknown endpoint multiplier is omitted.
The internal nonsmooth scalar-germ knots introduce no flux jump:
the complete strict certificate already verifies the genuine matching
jets and weak joining of the actual coefficients.

The normalized angular Sobolev weights are
\((1+n^2/N^2)^{s/2}\). At \(s=0\), \(N\) has no effect on the norm.
The scale \(N=2^{20}\) below merely selects an already computed set of
valid comparison constants. In averaged root measure, use
\(d\phi/\ell\); both roots use the same \(\ell\).

## 2. The actual infinite block inverse is onto

Write

\[
\mathscr T=\begin{pmatrix}A&B\\C&D\end{pmatrix}.             \tag{S.5}
\]

All four blocks act on the full root \(L^2\), including its mean.
Both sides of (S.4) imply

\[
B^*B=I+D^*D,\qquad BB^*=I+AA^*,                            \tag{S.6}
\]

\[
C^*C=I+A^*A,\qquad CC^*=I+DD^*.                            \tag{S.7}
\]

In particular \(B\) and \(B^*\) are bounded below by one.
The first fact gives a closed injective range for \(B\); the second
gives \(\ker B^*=0\), so that range is dense and hence all of \(L^2\).
Therefore

\[
\|B^{-1}\|\le1.
\]

The same argument gives \(\|C^{-1}\|\le1\).
These statements do not use a numerical singular value, Fredholm
index, a high-frequency approximation, or a finite-dimensional
truncation of either block.

## 3. Full two-ended scattering and exact source folding

Put

\[
x=(z_{L,+},z_{R,+}),\qquad y=(z_{L,-},z_{R,-}).
\]

For a homogeneous solution, solve the first row of
\(z_R=\mathscr Tz_L\) with the true \(B^{-1}\). This gives

\[
\boxed{
\mathscr S=
\begin{pmatrix}
-B^{-1}A&B^{-1}\\
C-DB^{-1}A&DB^{-1}
\end{pmatrix},\qquad y=\mathscr Sx.}                        \tag{S.8}
\]

Equation (S.4) rearranges exactly to
\(\|z_{L,+}\|^2+\|z_{R,+}\|^2
 =\|z_{L,-}\|^2+\|z_{R,-}\|^2\). Hence \(\mathscr S\)
is isometric. Given arbitrary \(y\), use

\[
z_{L,+}=C^{-1}(z_{R,-}-Dz_{L,-}),\qquad
z_{R,+}=Az_{L,+}+Bz_{L,-}.
\]

This proves surjectivity and (S.1).

For a complete affine Cauchy source

\[
z_R=\mathscr Tz_L+g,\qquad g=(g_+,g_-),
\]

the same exact elimination gives

\[
y=\mathscr Sx+s,\qquad
s=\binom{-B^{-1}g_+}{g_--DB^{-1}g_+}.                     \tag{S.9}
\]

The first source column is an isometry:

\[
\binom{-B^{-1}}{-DB^{-1}}^*
\binom{-B^{-1}}{-DB^{-1}}
 =(B^{-1})^*(I+D^*D)B^{-1}=I.
\]

The other source column \((0,I)^t\) is also isometric.
By the triangle inequality and two-term Cauchy--Schwarz,

\[
\boxed{\|s\|\le\sqrt2\,\|g\|.}                             \tag{S.10}
\]

In particular the large full Cauchy bound is not multiplied into
(S.10) again. Both signs of the first column in (S.9) are retained.

## 4. Actual ordinary-source columns from all three negative pieces

Use the frozen full graph/root theorem's notation:
\(K\) bounds root-to-cut, \(K_i\) cut-to-root;
\(S_r,S_g\) are its complete canonical-root and tilted-graph
ordinary-source gains. Let \(C_0,S_0\) be the new requested-window
strict amplitude/inverse and ordinary-source bounds at window zero.

For sources in the left collar, core, and right collar, their exact
local relations are

\[
z_{\rm cut,L}=K_Lz_L+g_L,\qquad
z_{\rm cut,R}=C_{\rm st}z_{\rm cut,L}+g_{\rm st},\qquad
z_{\rm cut,R}=K_Rz_R+g_R.
\]

Consequently the whole Cauchy source is

\[
\boxed{g=K_R^{-1}(C_{\rm st}g_L+g_{\rm st}-g_R).}           \tag{S.11}
\]

The right-collar minus sign comes from solving its complete affine
relation. Its coefficient is not replaced by a local normal derivative.

Together with (S.10), the five complete two-ended source gains are

\[
\begin{array}{c|c|c}
\text{input}&\text{source norm}&\text{gain to }s\\ \hline
\text{strict core}
 &L^1(dr;H_N^{-1/2})&\sqrt2\,K_i S_0\\
\text{left canonical collar}
 &L^1(d\xi;H_N^{-1/3})&\sqrt2\,K_i C_0 S_r\\
\text{left tilted graph}
 &L^1(dt;H_N^{-1/2})&\sqrt2\,K_i C_0 S_g\\
\text{right canonical collar}
 &L^1(d\xi;H_N^{-1/3})&\sqrt2\,K_i S_r\\
\text{right tilted graph}
 &L^1(dt;H_N^{-1/2})&\sqrt2\,K_i S_g .
\end{array}                                               \tag{S.12}
\]

The core norm is that of the original ordinary physical scalar \(f\).
The two collar norms are the exact transformed densities specified in
the graph theorem, with its true height/Piola scalar term. They are
not untransformed physical \(L^1_rH^s_\theta\) norms.
When the nonconstant physical cut is obtained by traversing the
overlapping constant-canonical collar and returning along the graph,
both norms use the same valid source extension. The opposite oriented
overlap cancels in the exact solution; its two norm costs are both
retained in (S.12). Arbitrarily unrelated collar and graph sources
would define a different problem.

No weak divergence source is renamed as any of the ordinary inputs
in (S.12). All mean outputs and mean source charges are retained in
(S.9)–(S.12). The exact root mean trace is still

\[
U_0=c(z_++z_-)_0,\qquad
(U_\xi)_0=ic(z_+-z_-)_0/\pi.
\]

The grounded physical constant is not generally the constant
canonical root height after the actual positive height change.
Its true source/flux compatibility is not replaced by deleting this
Fourier mean.

### 4.1 Use the actual reflection and the shorter core propagation

The full fixed-direction bounds (S.12) remain valid, but their left
collar columns unnecessarily propagate through the whole core.
R77's actual radial reflection exchanges the two roots by unitary
permutations of their complete R39 waves. It maps the two canonical
source norms and their matching graph extensions to the same norms
at the other root. Therefore the actual two-ended source column at
the left root has the same norm as its reflected right-root column.
For each collar one may use the better of the two complete bounds
in (S.12). This uses linearity of the actual source operator; it
does not change the homogeneous scattering operator.

For the core source, split its radial support at zero, retaining the
same ordinary density \(f\). On \(r\ge0\), the Cauchy source reaches
the right cut inside one positive half-core. On \(r<0\), use the
reflected orientation and reach the left cut. For \(L^1_r\) sources
the sum of the two restricted norms is exactly the whole radial
norm, so no additional factor two is charged.

Here the shorter physical \(\mathcal P_{0,N}\) Cauchy bound is itself
computed from the existing closed cells. Write

\[
G_f=\sum_{\text{215 cells}}|I_i|
          \max(0,g_{0,f,i})/2,\qquad
G_b=\sum_{\text{215 cells}}|I_i|
          \max(0,g_{0,b,i})/2.
\]

These are the original forward and backward base-energy rates; no
half of a possibly nonsymmetric rate is presumed.
Let \(e_N=\sqrt{h_{+,N}/h_{-,N}}\) be the single already paid global
energy equivalence. The positive half-index has forward bound
\(e_Ne^{G_f}\) and backward bound \(e_Ne^{G_b}\).
The exact flux adjoint supplies the negative half-index in the
opposite direction. Thus interpolation at index zero gives the
common, all-subinterval half-core bound

\[
\mathfrak E^{\rm half}_{0,N}
 \le e_Ne^{(G_f+G_b)/2}.                                  \tag{S.12a}
\]

It retains the two physical rows and the mean. Multiplication by
the unchanged inverse normal frame \(I_N(0)\), followed by the
same complete cut-to-root map and (S.10), gives the actual core
source gain

\[
\sqrt2\,K_iI_N(0)\mathfrak E^{\rm half}_{0,N}.              \tag{S.12b}
\]

At \(N=2^{20}\), the directed consumer finds

\[
G_f<32.221701,\quad G_b<47.257246,\quad
\mathfrak E^{\rm half}_{0,N}<1.427754\,10^{25}.
\]

The resulting complete source bounds are

| Actual ordinary-source input | Gain to the full two-ended \(s\) |
|---|---:|
| Entire strict core \(L^1(dr;H_N^{-1/2})\) | \(<8.633789\,10^{64}\) |
| Either canonical root collar | \(<1.052974\,10^{67}\) |
| Either matching tilted-graph source | \(<9.858673\,10^{52}\) |
| Euclidean direct sum of all five source spaces | \(<1.489155\,10^{67}\) |

The last line is the square root of the sum of the five squared
column bounds. The same-extension condition for each collar/graph
pair is unchanged. This is a complete source bound, not a new
regularity statement for arbitrary mixed-coordinate physical loads.

## 5. The two complete positive caps and the regular units

Take precisely the complete cap reflection proved in
R45-supplement-actual-exact-positive-cap-Airy-contact-and-four-thirds.md,
with the original R74/R94 whole-tail Robin form.
Its physical root/regular Hilbert space is
\(L^2(d\phi)\oplus\mathbb C\), and its full augmented reflection
\(\mathscr R_+\) is onto unitary. Its affine source is

\[
(y,b_{\rm old})=\mathscr R_+(x,a_{\rm old})+h_{\rm old}.
\]

To match the averaged root convention of sections 1–4, use

\[
a=a_{\rm old}/\sqrt\ell,\qquad
b=b_{\rm old}/\sqrt\ell.
\]

Indeed the identification
\(D_\ell:(x,a)\mapsto(x,\sqrt\ell a)\) has
\(\|D_\ell(x,a)\|_{\rm old}=\sqrt\ell\|(x,a)\|_{\rm new}\).
Thus

\[
\widehat{\mathscr R}_+
 =D_\ell^{-1}\mathscr R_+D_\ell
\]

is still onto unitary. The full source norm is divided by
\(\sqrt\ell\), including its regular output. This is a common exact
normalization, not an unpaid change of the relative regular weight.

The physical regular waves remain

\[
a_{\rm old}=\frac{\sqrt{\pi c_A}}2(\zeta-i\lambda),\qquad
b_{\rm old}=\frac{\sqrt{\pi c_A}}2(\zeta+i\lambda).
\]

Consequently their exact independent flux row is

\[
\boxed{b-a=i\sqrt{\pi c_A/\ell}\,\lambda.}                 \tag{S.13}
\]

Here \(\lambda\) is the true normalized physical regular mean flux.
It is retained as data or as an additional compatibility unknown;
it has not been set to zero inside the cap operator.
The conjugate physical mean \(\zeta\) is likewise retained.

The actual quarter-period satisfies
\(\ell=2\pi/q_c\), with the complete interval from the cap report.
The paired two-cap source norms are the Euclidean sums of the two
physical-measure local source norms. Their gains to the new \(h\) are
therefore the old \(377.600482\) ordinary and \(188.781182\) weak
gains, each multiplied by \(1/\sqrt{\ell_-}\). There is no extra
factor two for the direct sum of the two caps.

The same normalization commutes with the root Sobolev weight and
with weight one on the regular slot. Hence the old full-cap two-sided
\(4/3\) remainder bound remains valid, including all mean and regular
input columns. For \(N\ge1\), the normalized weights
\((1+n^2/N^2)^{2/3}\) are bounded by the physical
\(\langle q_cn\rangle^{4/3}\), so this also pays the stated base
scaled smoothing in both directions. It does not supply a larger
window or a fixed positive angular weight.

## 6. Exact augmented feedback, without eliminating the regular rows

Order the two complete cap factors by a fixed unitary permutation as
root pair first and regular pair second, and call their direct sum
\(\mathscr R\). It is onto unitary on

\[
\mathscr H=(L^2_{\rm av}\oplus L^2_{\rm av})\oplus\mathbb C^2.
\]

Put \(u=(x,a)\). The cap equations are

\[
(y,b)=\mathscr R u+h.
\]

The negative solution is \(y=\mathscr Sx+s\), and (S.13) is
\(b=a+i\sqrt{\pi c_A/\ell}\lambda\). Thus, with

\[
\mathscr S_{\rm ext}=\operatorname{diag}(\mathscr S,I_{\mathbb C^2}),
\qquad
t=(s,i\sqrt{\pi c_A/\ell}\lambda),
\]

the actual entire old component/cap system is exactly

\[
\mathscr R u+h=\mathscr S_{\rm ext}u+t,
\]

or equivalently

\[
\boxed{(I-\mathscr U)u=\mathscr R^*(t-h),\qquad
\mathscr U=\mathscr R^*\mathscr S_{\rm ext}.}               \tag{S.14}
\]

Both factors in \(\mathscr U\) are actual onto unitaries; hence

\[
\|\mathscr U\|=\|\mathscr U^{-1}\|=1,\qquad
\|I-\mathscr U\|\le2.                                    \tag{S.15}
\]

The finite regular identity in \(\mathscr S_{\rm ext}\) is simply
the displayed rearrangement of (S.13); the true regular flux and
source contact stay explicitly in \(t-h\). It is not a substitute
regular-tail condition.

The conjugate cap, rather than an unlabelled copy of the cap
reflection, occurs in (S.14), because both original root graphs were
written as \(z_-\) versus \(z_+\) in the same inward-negative
canonical frame. This fixes the feedback sign before any Maslov or
first-order reduction.

If a solution of (S.14), its regular conditions and any specified
finite gauge constraints is supplied, the complete component solvers
join with equal true height and opposite outward conormal and give
the corresponding global linear weak solution. Conversely every
such solution satisfies (S.14). This equivalence does not prove that
\(I-\mathscr U\) is injective or onto. A unitary \(\mathscr U\)
can have eigenvalue one, so (S.15) is not an inverse certificate.

## 7. Executed finite consumer and remaining scope

The small consumer is
scripts/fourfold_actual_central_scattering_and_source.py.
It reads the frozen complete graph, requested-window strict, and exact
positive-cap reports; verifies their producers, dependencies and inputs;
matches their object-path/object-hash field aliases and every exact
origin, direction and parameter interval; and verifies the exact common
physical cuts. It evaluates (S.2), (S.12), the period conversion and
the explicit regular flux factor at 320-bit directed precision.
No native field is resampled and no infinite block is truncated.

The complete result is
notes/2026-11-13-actual-central-scattering-and-source.json.
Its full scalar input and output table preserves each negative source
column separately. The exact norm-one scattering and feedback-product
bounds come from (S.4)–(S.15), not from a numerical matrix test.

Its full root-to-root Cauchy comparison is
\(<4.983413\,10^{120}\), while the true scattering and feedback-product
norms are exactly one. These statements concern different operators.
The complete positive local source gains in the common averaged-root
and balanced-regular units are

\[
939.349576\quad\hbox{(ordinary)},\qquad
469.627374\quad\hbox{(weak)}.
\]

The independent physical regular flux to its wave difference in
(S.13) has gain \(<3.764756\).

The additional consumer
scripts/fourfold_actual_central_scattering_reflected_source.py
produces notes/2026-11-13-actual-central-scattering-reflected-source.json.
It preserves the original complete fixed-direction report, checks
all 215 adjacent native cells and their two directed rate budgets,
and implements only the new reflection and half-index interpolation
in section 4.1. It does not change the native fields or discard an
unsuccessful parameter box.

From the topic directory, use a new output path:

~~~sh
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_actual_central_scattering_and_source.py \
  --scale 1048576 --bits 320 \
  --out /tmp/actual-central-scattering-independent.json
python3 scripts/fourfold_actual_central_scattering_reflected_source.py \
  --bits 320 \
  --out /tmp/actual-central-short-source-independent.json
~~~

The actual first-order normal form of (S.14), its entire returned strong
remainder, all required weighted/source windows, finite Schur inverse,
regular compatibility and nonlinear integration remain open. This
theorem pays the genuine base scattering/source interface on which
those later steps must operate.
