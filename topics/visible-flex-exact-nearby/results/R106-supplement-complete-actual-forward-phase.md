# R106 supplement: the complete actual forward finite-part phase

## 1. Result and precise normalization

For the actual step5 family

\[
 p_5=-7789843107295549/4611686018427387904,\qquad
 |p-p_5|\le10^{-9},
\]

let \(x\) be the saved normalized \(2\pi\)-periodic input label and
\(\Theta(r,x,p)\) the complete actual forward characteristic, with physical
angle \(\Theta(x+2\pi)=\Theta(x)+\pi/2\).
Let \(h_{\rm fwd}(x,p)\,dx\) be the R106/R46 finite-part first-phase
one-form for the entire passage between the two actual roots.
Then

\[
 \boxed{\ \sup_{p,\ |\Im x|\le1/2048}|h_{\rm fwd}(x,p)|<13205.\ } \tag{1}
\]

Both root finite parts, the complete strict-region reduced density,
its angular divergence, all endpoint contributions and every mean are
included. The physical cuts are exactly

\[
 r=\pm r_c,\qquad r_c=268136140016943/1125899906842624.
\]

The proof cancels their common fluxes as exact one-forms before taking any
absolute bound. It does not delete an endpoint contribution.
The coefficient already contains \(J=\Theta_x\); there is no further
factor \(4\) or \(1/4\).

This is the complete forward coefficient on the saved input label.
The second leg, complete Ai/contact/port return realization, strong
propagator remainder and R101 circle-frame conjugacy remain required before
identifying the complete R104 coefficient \(b\). Consequently (1) is not a
completed PDE inverse or an effective R104 cutoff certificate.

## 2. New complete complex strict-region fields

The native producer
[current complex bulk](../scripts/fourfold_subprincipal_current_bulk_complex.py)
evaluates the four original-height fields \(D,S,V_r,L_\theta\) from
R106 (106.8)--(106.13), before any angular mean. It uses the unchanged
directed finite Fourier/primitive engine and independent infinite-primitive
errors. The exact origin/direction scalar germs are formed first and the
single shared affine parameter is then applied.

Each closed radial cell and every physical angle
\(|\Im\theta|\le1/640\) are enclosed together. The finite radial scalar
polynomials are chosen on their exact common knot spans. The angular cover
is the existing full complex rectangular cover around the actual finite
Fourier nodes, with every finite angular shift and true infinite tail paid.
It is not a finite-angle sample bound.
The required positive-real denominator tests are performed before division.

For the waist cell \(0\le r\le2^{-20}\), the exact odd functions \(F_z\) and
\(F_{\theta,z}\) vanish at \(0\). Thus

\[
 \frac{F_z(r)}r=\int_0^1F_{r,z}(ur)\,du,\qquad
 \frac{F_{\theta,z}(r)}r=\int_0^1F_{r\theta,z}(ur)\,du.
\]

The whole-cell \(F_{r,z}\) enclosure has positive real part. The ratio of these
two averages is therefore enclosed by the same interval quotient used in the
producer. This pays the smooth \(\ell\) at the waist without dividing by a
box containing \(F_z=0\).

The first complete run had a large wrapping bound and was retained unchanged.
The separate
[refinement producer](../scripts/fourfold_subprincipal_current_bulk_refine.py)
reuses an old leaf only after checking its complete certificate. Otherwise
it evaluates both exact half-cells, retaining the unchanged actual fields
and all errors. Every accepted leaf is checked, every parent interval is
filled without a gap, and the final cover is exactly \([0,r_c]\).
The refinement quotas select cells; they are not assumptions about the
actual functions. No cell is accepted unless its true bounds satisfy them.

The complete refinement has \(654\) closed leaves and gives

\[
\begin{aligned}
 I_D&=\int_0^{r_c}\sup_{\theta,p}|D(r,\theta,p)|\,dr
       <4364.527957551426,\\
 I_S&=\int_0^{r_c}\sup_{\theta,p}|S(r,\theta,p)|\,dr
       <2.158933925541127 .
\end{aligned}                                                  \tag{2}
\]

Here the supremum includes the whole physical complex strip and the whole
real parameter interval. Exact radial reflection preserves these moduli on
the negative half. These are current-step5 complex bounds, not a transfer
of the old real-only derivative certificate or of an angular mean.

## 3. The complete actual ray

The already proved complete integrated-source ray certificate is

    notes/2026-11-13-R106-integrated-source-ray-refinement.json

It covers all \(550\) segments of the actual forward leg, the full parameter
interval, and \(|\Im x|\le s_0=1/1024\). Its exact rational bounds are

\[
 |\Im\Theta|\le\frac{8212533}{8000000000}
 =0.001026566625<\frac1{900}<\frac1{800}<\frac1{640},
 \qquad
 |J|\le J_*=\frac{8213877}{7812500}=1.051376256.                 \tag{3}
\]

The complete strict fields and complete regularized root source are therefore
valid at every point of these actual rays. This includes the actual moving
root times and actual fixed-cut times; no midpoint time is substituted.
For fixed \(p\), the cut time is independent of \(x\), so differentiating the
strict \(S\)-integral in \(x\) creates no moving-limit term.

The consumer checks both original true-ray input hashes and its exact
arithmetic producer, the parameter identities, the complete leg and gates,
and both strict/root image inclusions.

## 4. Exact cancellation of both physical-cut fluxes

Write the physical branch sign as \(\varsigma\). On the strict region, R106
gives

\[
 h_{\rm strict}
 =\frac12\int_{-r_c}^{r_c} D(r,\Theta)J\,dr
  +\frac12\partial_x\int_{-r_c}^{r_c}S(r,\Theta)\,dr
  -\frac14[J(V_r+\varsigma L_\theta)]_{-r_c}^{r_c}.             \tag{4}
\]

At root side \(\epsilon=\pm1\), use inward root coordinate
\(\rho=t(p)-\epsilon r=s^2\). The local branch sign and local flux are

\[
 \sigma_\epsilon=-\epsilon\varsigma,\qquad
 V_{\rho,\epsilon}=-\epsilon V_r,\qquad
 V_{\rho,\epsilon}+\sigma_\epsilon L_\theta
      =-\epsilon(V_r+\varsigma L_\theta).                     \tag{5}
\]

The exact complete root formula has transport boundary

\[
 B(s,\theta)=s^{-3}B_{-3}(\theta)+s^{-1}B_{-1}(\theta),
 \qquad
 B_{-3}=-G_0/3,\quad
 B_{-1}=-G_1-\frac23\partial_\theta(q_0G_0),
\]

analytic source \(H_\sigma=R_\sigma+\partial_\theta S_{\rm reg}\), root
field \(Z_\sigma=\sigma L_\theta(0)/4\), and the local cut flux
\(-J_{\rm local}(V_\rho+\sigma L_\theta)/4\).

Pull the root formula back by the actual global root-label map
\(\eta_\epsilon(x)=\Theta(\epsilon t(p),x)\).
Uniqueness of the nonsingular inward ODE gives

\[
 J_{\rm local}(s,\eta_\epsilon(x))\,\eta_\epsilon'(x)
      =J_{\rm global}(r,x).                                  \tag{6}
\]

In particular, after this pullback the local cut flux in (5) equals
\(+\epsilon J_{\rm global}(V_r+\varsigma L_\theta)/4\).
The strict endpoint contribution at that same side is
\(-\epsilon J_{\rm global}(V_r+\varsigma L_\theta)/4\).
They cancel exactly at each actual cut, including every mean and every
parameter value.

The two root contributions to the full finite part are taken on the positive
inward interval from root to cut. At the right root the reversed physical
radial limit and \(dr=-d\rho\) cancel. Thus both reduced root pieces enter the
full passage, with their actual inward signs from (5), and both are bounded
by the formula below. The root coordinate is the original fixed physical
\(\rho\); the R83 root-anchored canonical map has leading coefficient \(1\),
so the extra R106 (106.32) coordinate finite part is zero.

Equations (4)--(6) leave the exact full phase as the strict \(D,S\) integrals
plus the two complete root transport boundaries, regularized source
integrals and root fields. This proves the cancellation before a modulus
or mean is taken.

## 5. Complete root transport budget

The complete seven-field/source errors and actual root interval are those of
the preceding
[actual root finite-part proof](R106-supplement-actual-root-finite-part.md).
The source report is

    data/R106/root_regularized_native_degree64_plus/report.json

For its original physical strip \(1/800\), let \(M_H,M_Z\) be the complete
true moduli. The consumer reconstructs the full finite \(B_{-1}\) from all
seven-field coefficients with complete padded finite products. Let
\(\widehat B_{-3},\widehat B_{-1}\) denote these finite expressions,
\(e_G\) the complete true \(G\)-error, and \(e_B\) the complete true
\(B_{-1}\)-error already paid with the original two angular losses. Then

\[
 M_B=
 \frac{\|\widehat B_{-3}\|+e_G/3}{c_{\min}^3}
 +\frac{\|\widehat B_{-1}\|+e_B}{c_{\min}}                     \tag{7}
\]

is a complete uniform bound for the transport boundary at the actual cut.
The finite expressions are evaluated by the full weighted coefficient sums,
not by sampling. Their enclosed finite arithmetic is included.
The two root pieces after exact flux cancellation are therefore bounded by

\[
 2J_*(M_B+c_{\max}M_H+M_Z)
 <4193.956019434616.                                          \tag{8}
\]

There is no extra factor from the local root Jacobian in (8), because (6)
identifies its product with the global Jacobian already bounded by (3).
The actual true global angular image is inside the source strip at all root
times, so the whole source error domain is respected.

## 6. Strict angular derivative and the final bound

The strict \(D\)-contribution is bounded by \(J_*I_D\); the two radial halves
cancel the factor \(1/2\) in (4). The analytic function

\[
 F(x)=\int_{-r_c}^{r_c}S(r,\Theta(r,x))\,dr
\]

has supremum at most \(2I_S\) on \(|\Im x|\le s_0\).
With \(s=1/2048\), Cauchy gives supremum of \(|F'|/2\) at most
\(I_S/(s_0-s)\).
Consequently the complete budget is

| Included actual contribution | Outward upper bound |
| --- | ---: |
| strict reduced density \(J_*I_D\) | \(4588.761063217745\) |
| strict angular divergence \(I_S/(s_0-s)\) | \(4421.496679508228\) |
| both roots after exact common flux cancellation | \(4193.956019434616\) |
| complete forward finite part | \(13204.213762160587\) |

This proves (1). All estimates are uniform in the whole actual parameter
interval. The calculation does not infer a signed Fourier coefficient from
an unsigned modulus.

There is also a complete infinite Fourier consequence. For integer
\(0\le q\le12\), set \(s_w=1/4096\), \(z=e^{-(s-s_w)}\) and let \(M\) be the
unrounded final bound in the report. Then

\[
 M_{q,s_w}(h_{\rm fwd}-\langle h_{\rm fwd}\rangle)
 \le 2^{q/2+1}M\,q!\left((1-z)^{-q-1}-1\right).               \tag{9}
\]

Indeed \(|h_n|\le M e^{-s|n|}\),
\(\langle n\rangle^q\le(n+1)^q
\le q!\binom{n+q}{q}\) for \(n\ge1\), and the generating series of the
binomial coefficients sums the entire omitted-frequency complement.
The report gives these directed values. They bound the complete nonmean
forward coefficient, not a finite truncation and not the unidentified full
R104 return coefficient.

## 7. Executed files and reproduction

The retained complete reports are:

| Report | SHA256 |
| --- | --- |
| original complete complex bulk | fba2f161b4a2f646f1550cd4578f416ceca0189048d3e7c82ad1fc6efd1ee091 |
| refined complete complex bulk | 96a1b25ec8620981cccf01dc4b9f43a7ba5b73227636e711eae0ae296cae2646 |
| complete actual forward phase | 665dfc44fbfcb46d5efdf43a943de95631af9becdad444c2a7eceb5cd99c1e03 |

Their paths are, respectively:

    notes/2026-11-13-R106-current-full-complex-bulk-native.json.gz
    notes/2026-11-13-R106-current-full-complex-bulk-refined-native.json.gz
    notes/2026-11-13-R106-actual-complete-forward-phase.json

The final consumer is
[complete forward budget](../scripts/fourfold_subprincipal_complete_forward_budget.py).
It independently recomputes the exact leaf cover and radial sums, checks
the actual root/ray/bulk identities and domains, reconstructs the complete
finite transport counterterm, and retains the uncancelled bound as a
separate diagnostic.

~~~bash
python3 scripts/fourfold_subprincipal_current_bulk_complex.py \
  --out notes/2026-11-13-R106-current-full-complex-bulk-native.json.gz
python3 scripts/fourfold_subprincipal_current_bulk_refine.py \
  notes/2026-11-13-R106-current-full-complex-bulk-native.json.gz \
  --out notes/2026-11-13-R106-current-full-complex-bulk-refined-native.json.gz
python3 scripts/fourfold_subprincipal_complete_forward_budget.py \
  --out notes/2026-11-13-R106-actual-complete-forward-phase.json
~~~

The refinement used exact quotas \(75\) and \(1/100\), \(192\)-bit scalar
Arb inputs and the frozen directed finite engine, with \(512\) primitive
nodes and \(1024\) angular cells. It took about \(754\) seconds and completed
all \(654\) leaves. The final budget uses \(256\)-bit Arb arithmetic.
All producers require fresh output paths and preserve the earlier evidence.
