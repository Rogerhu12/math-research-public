# R133 supplement: a positive drift representation and complete relative angular fold bounds

2026-11-16, visible-exact / phase_inverse.

**Pure analytic theorem and a finite new-target contract.** The true fold gap on the original strict interval is a sum of positive contributions transported by the drift alone. Differentiating that identity gives complete relative angular bounds without first bounding the full gap from above and then dividing by a separate lower bound. The old characteristic derivative records also bound this drift flow: the angular variational equations depend only on the same angular derivatives of the drift.

The theorem below supplies ordinary relative derivatives of orders 1 through 14. Its numerical predecessor set is the two complete WGS files, containing 35 consumed old scalar records. A future consumer has five complete groups with 10, 14, 14, 28 and 14 new records. The new arithmetic consists of finite positive rational expressions, finite coefficient convolutions and maxima of directed endpoints. It requires no new exponential, square root, logarithm, characteristic solve or radial integration.

No new bound is evaluated in this note. The old WGS phase, flow, coefficient and mixed-jet conclusions remain immutable. The new output is a strict geometric predecessor; the complete forcing, physical means, negative reception, waist endpoints, finite columns and signed normalization remain separate objects.

## WDG1. One actual gap and the original strict domain

Use the same repaired real reference and selected member admitted by WGS and WUA, restricted to
$$
 0\le r\le c,\qquad
 c=\frac{76285779072683}{320000000000000}.
 \tag{WDG.1}
$$
The physical angle has period $\pi/2$ and Fourier frequencies $4j$. Derivatives below are ordinary derivatives in this angle. The original real parameter range, fixed intrinsic parameter, continuous reference, actual root labels and all original radial interfaces are unchanged.

Write
$$
 a(r)=\eta(r)q(r)>0,\qquad
 D=\partial_r-d(r,\phi)\partial_\phi,\qquad
 \Phi_\sigma=X-\sigma\omega,\qquad \sigma=\pm1.
 \tag{WDG.2}
$$
Here $d=-\beta I(u_{\rm bg}^2+K v_{\rm bg}^2)$ is the original physical drift. It is a known coefficient, not an unknown state. The background symbols $u_{\rm bg},v_{\rm bg}$ are distinct from the fold derivatives below.

The actual strict fold has
$$
 p_\sigma=\partial_\phi\Phi_\sigma>0,\qquad
 x=X_\phi=\frac{p_++p_-}{2}>0,\qquad
 \omega>0,\quad t=-T=\left(\frac{3\omega}{2}\right)^{2/3}>0 .
 \tag{WDG.3}
$$
The complete saved strict phase lower is denoted $m_\Phi>0$, so $p_\pm\ge m_\Phi$ and $x\ge m_\Phi$.

The true characteristic equations are
$$
 D\Phi_\sigma=\sigma a\,\partial_\phi\Phi_\sigma .
 \tag{WDG.4}
$$
Taking their difference and sum gives
$$
 D\omega=-a x,\qquad DX=-a\omega_\phi .
 \tag{WDG.5}
$$
These identities use the true root-labelled lifts. No value of a lift is replaced by zero, and no winding or additive constant is changed. The actual root $r_*$ is outside the present strict calculation. A root enclosure endpoint is not substituted for $r_*$ in a physical initial condition.

The calculations hold on each original radial piece and concatenate across the original continuous interfaces. Only the indicated one-sided radial derivatives will be used by a later mixed-jet construction. This theorem itself differentiates in $\phi$, not in $r$, and requires no new radial regularity.

## WDG2. Positive drift representation, with the cut term retained

Let $\chi_{s\leftarrow r}(\phi)$ solve
$$
 \frac{d}{ds}\chi_{s\leftarrow r}(\phi)
       =-d\bigl(s,\chi_{s\leftarrow r}(\phi)\bigr),
 \qquad \chi_{r\leftarrow r}(\phi)=\phi ,
 \qquad r\le s\le c .
 \tag{WDG.6}
$$
This is the drift flow. It is generally different from either characteristic flow with velocity $-d\mp a$. Its real lift is orientation preserving.

The chain rule in the true radial variable gives
$$
 \frac{d}{ds}\omega\bigl(s,\chi_{s\leftarrow r}(\phi)\bigr)
       =-a(s)x\bigl(s,\chi_{s\leftarrow r}(\phi)\bigr).
$$
Therefore
$$
 \boxed{\quad
 \omega(r,\phi)=
   \omega\bigl(c,\chi_{c\leftarrow r}(\phi)\bigr)
   +\int_r^c a(s)x\bigl(s,\chi_{s\leftarrow r}(\phi)\bigr)\,ds .
 \quad}
 \tag{WDG.7}
$$
Both the cut term and every integrand are positive. The coefficient $a(s)$ has no angular dependence. The ordinary $ds$ measure, the complete interval and all original pieces are retained. Formula (WDG.7) is not a subtraction of the two phase upper bounds.

For a fixed $r,\phi$, division by the positive $\omega(r,\phi)$ turns the cut contribution and the radial contribution into a probability measure on the disjoint union of one cut atom and $[r,c]$:
$$
 \lambda_c=\frac{\omega(c,\chi_{c\leftarrow r})}{\omega(r,\phi)},
 \qquad
 d\lambda(s)=
   \frac{a(s)x(s,\chi_{s\leftarrow r})}{\omega(r,\phi)}\,ds,
 \qquad \lambda_c+\int_r^c d\lambda=1 .
 \tag{WDG.8}
$$
This measure is used only after differentiating (WDG.7). It is not differentiated as if its dependence on $\phi$ were constant.

Consequently, if complete constants $K_b,B_b$ satisfy
$$
 \left|\partial_\phi^b
       \omega(c,\chi_{c\leftarrow r}(\phi))\right|
 \le K_b\,\omega(c,\chi_{c\leftarrow r}(\phi)),
$$
$$
 \left|\partial_\phi^b
       x(s,\chi_{s\leftarrow r}(\phi))\right|
 \le B_b\,x(s,\chi_{s\leftarrow r}(\phi))
 \qquad(r\le s\le c),
 \tag{WDG.9}
$$
then
$$
             |\partial_\phi^b\omega(r,\phi)|
       \le \max(K_b,B_b)\,\omega(r,\phi).
 \tag{WDG.10}
$$
For $r=c$, the integral vanishes and the same bound includes the cut atom. There is no missing endpoint case.

All angular differentiations under the integral are justified by the complete uniform finite derivative envelopes below. The original interval is finite, its piecewise coefficients are integrable, and the resulting bounds are uniform on every shorter interval. No boundary term arises from an angular derivative of fixed radial endpoints.

## WDG3. Why the complete old flow envelopes also bound the drift flow

The relevant comparison theorem is stronger than equality or closeness of two saved flow numbers. Consider a velocity
$$
                  -d(s,\phi)-\nu(s),
 \tag{WDG.11}
$$
where $\nu$ is radial. The original characteristic choices are $\nu=\pm a$, and the drift choice is $\nu=0$. For every $j\ge1$,
$$
 \partial_\phi^j(d+\nu)=\partial_\phi^j d .
$$
Thus the angular variational equations have exactly the same coefficient envelopes for all three choices, even though their trajectories differ.

WX.4--9 proves from the specific complete positive forward and reverse comparison products that
$$
       \exp\!\left(\int_I\|d_\phi(s)\|_\infty\,ds\right)
                   \le F_1
 \tag{WDG.12}
$$
for every shorter real interval $I\subseteq[0,c]$ and both orientations. This is a consequence of the positive algorithm, including both first diagonal products. It is not obtained by inverting an arbitrary evolution norm.

With $J=\partial_\phi\chi$, the first variational equation is
$\dot J=\pm d_\phi J$, with $J=1$ initially. Its forcing-free comparison depends only on (WDG.12). WX.12--13 gives the complete second and third derivative envelopes from
$$
 \dot\chi_{\phi\phi}
      =\pm d_\phi\chi_{\phi\phi}
           \pm d_{\phi\phi}\chi_\phi^2 ,
$$
$$
 \dot\chi_{\phi\phi\phi}
      =\pm d_\phi\chi_{\phi\phi\phi}
       \pm3d_{\phi\phi}\chi_\phi\chi_{\phi\phi}
       \pm d_{\phi\phi\phi}\chi_\phi^3 .
 \tag{WDG.13}
$$
The finite-support estimates used there concern $d_\phi$, whose complete label bandwidth is 192, and hence are unchanged for (WDG.11). DX.14--17 does the same for order four, with every Bell term retained.

For completeness, let $\mathsf B_{b,k}$ be the ordinary exponential partial Bell polynomial defined by
$$
 \mathsf B_{b,k}(F)
  =\frac{b!}{k!}[z^b]
        \left(\sum_{j=1}^b\frac{F_j}{j!}z^j\right)^k .
 \tag{WDG.14}
$$
The $b$-th variational equation has the term
$\pm d_\phi\chi^{(b)}$ plus
$$
       \sum_{k=2}^b
             \pm d^{(k)}\mathsf B_{b,k}
                        (\chi',\ldots,\chi^{(b-k+1)}).
$$
The already successful WGS function complete_higher_flow_and_cut uses, for $b=5,\ldots,15$, the complete positive recurrence
$$
 F_b=cF_1\sum_{k=2}^b D_k
                   \mathsf B_{b,k}(F_1,\ldots,F_{b-k+1}),
 \qquad D_k\ge\|d^{(k)}\|_\infty ,
 \tag{WDG.15}
$$
with outward record endpoints. Its normalized coefficient for $d$ is multiplied by $k!$ before it enters $D_k$. Variation of constants, followed by the complete interval-length bound $c$, proves (WDG.15) for every shorter interval and either orientation. The highest flow derivative on the right is strictly below $b$.

The induction therefore proves
$$
 \|\partial_\phi^b\chi_{s\leftarrow r}\|_\infty\le F_b,
       \qquad 1\le b\le14,\quad 0\le r,s\le c ,
 \tag{WDG.16}
$$
using the exact previously saved $F_b$. The same proof applies to inverse directed maps. No old recurrence, matrix exponential, $D_k$ norm, flow derivative or characteristic is evaluated again.

This argument does not assert that the $\nu=0,\pm a$ maps are identical. It proves that the complete old comparison envelopes cover the additional map because the entire angular variational system and its input inequalities have the same form. Radial derivatives of the flows would contain derivatives of $\nu$; they are not supplied by (WDG.16).

## WDG4. Relative cut derivatives from the full holomorphic cut input

At the original cut, the FA/DX domain gives a complete holomorphic bound
$$
        |T_\phi(c,\phi)|\le Y_c
       \quad\text{on }|\operatorname{Im}\phi|<s_F,\qquad
        s_F=\frac3{128},
 \tag{WDG.17}
$$
and a genuine positive real lower $t(c,\phi)\ge t_c^->0$. The saved $Y_c$ is a full-strip modulus of the true $T_\phi$. It is not a real supremum promoted to a strip norm. Its radial Schwarz restriction and original fold disk were already part of FA admission.

Let $T_j$ denote the complete ordinary cut derivative upper for $t$. Read the four saved $T_1,\ldots,T_4$ unchanged. Only orders five through fourteen are new targets:
$$
       T_j=\frac{(j-1)!\,Y_c}{s_F^{\,j-1}},
                         \qquad 5\le j\le14.
 \tag{WDG.18}
$$
For an open strip, apply Cauchy's estimate at every smaller radius and pass to the limit. These estimates include both Fourier signs and the full analytic function. No Airy remainder is differentiated.

Put
$$
    A(z)=\sum_{j=1}^{14}\frac{T_j}{j!\,t_c^-}z^j .
 \tag{WDG.19}
$$
At a fixed real angle $\phi_0$, the normalized Taylor coefficients of
$t(c,\phi_0+z)/t(c,\phi_0)$ are bounded by those of $1+A(z)$. Since
$\omega_c=(2/3)t_c^{3/2}$, its relative Taylor coefficients satisfy
$$
 C_b=b!\sum_{k=1}^b
            \left|\binom{3/2}{k}\right|[z^b]A(z)^k
       \ \ge\
       \sup_\phi\frac{|\partial_\phi^b\omega(c,\phi)|}
                         {\omega(c,\phi)},
                    \qquad1\le b\le14 .
 \tag{WDG.20}
$$
This is a finite formal coefficient identity. For coefficient $b$, only
powers $k\le b$ contribute. It needs no numerical condition such as
$A(1)<1$, no infinite-series truncation and no fractional power of a
complex $T$. The power $3/2$ is differentiated at positive real $t$;
its coefficient factors are exact rational binomial coefficients.

The constant factors $2/3$ and $t(c,\phi_0)^{3/2}$ cancel in this relative
identity. In particular (WDG.20) does not pay a complete $\omega_c$ upper
and then divide it by a separate $\omega_c$ lower. The only new cut
denominator is the original $t_c^-$, used in every relevant coefficient
of (WDG.19).

All $C_b$ in (WDG.20) are **ordinary** relative derivative bounds.
A later normalized jet uses $C_b/b!$. A consumer must not multiply a
stored ordinary bound by another factorial merely because an intermediate
coefficient array is normalized.

## WDG5. Complete relative bulk derivatives and composition

Let $P_j$ be the saved complete ordinary bound for the $j$-th angular
derivative of either true strict phase. For $1\le b\le14$,
$$
 |x^{(b)}|
   =\left|\tfrac12\bigl(\Phi_+^{(b+1)}
                            +\Phi_-^{(b+1)}\bigr)\right|
   \le P_{b+1}.
$$
Both phases are retained in this identity. Since $x\ge m_\Phi$, define
$$
                      X_b=\frac{P_{b+1}}{m_\Phi},
       \qquad
       \frac{|x^{(b)}|}{x}\le X_b,\qquad1\le b\le14 .
 \tag{WDG.21}
$$
The half sum introduces no additional factor two. No upper bound for
$x$ itself is needed to normalize (WDG.21).

Apply the complete ordinary chain rule to each positive summand in
(WDG.7). With the same $\mathsf B_{b,k}$ from (WDG.14), set
$$
 K_b=\sum_{k=1}^b C_k\,
              \mathsf B_{b,k}(F_1,\ldots,F_{b-k+1}),
$$
$$
 B_b=\sum_{k=1}^b X_k\,
              \mathsf B_{b,k}(F_1,\ldots,F_{b-k+1}).
 \tag{WDG.22}
$$
The complete old all-shorter $F_j$ cover the cut map and every
intermediate $s$-map. Equations (WDG.20)--(WDG.22) prove (WDG.9), since the
relative bound for the undifferentiated positive function is taken at the
same point where its derivative is evaluated.

It follows that
$$
 \boxed{\quad
 R^\omega_b=\max(K_b,B_b),\qquad
 \frac{|\partial_\phi^b\omega(r,\phi)|}{\omega(r,\phi)}
           \le R^\omega_b,\qquad
 1\le b\le14,\quad0\le r\le c .
 \quad}
 \tag{WDG.23}
$$
Each maximum is a comparison of the two complete directed endpoint bounds
for the same derivative. It is not an entrywise selection between
operators, and it is not a subtraction of norms. In a numerical consumer,
save the whole $K_b$ and $B_b$ records first, read their outward uppers
back, then save their maximum.

The range ends at fourteen for a specific reason: $x^{(b)}$ requires
$\Phi^{(b+1)}$, and the saved individual phase derivatives end at fifteen.
No relative order fifteen follows from this argument. The separate WSJ
identity $t_\phi=\omega_\phi/\sqrt t$ can supply certain absolute edge
derivatives; it does not extend (WDG.23) to $b=15$.

## WDG6. Exact relation to the scaled mixed packet

The fixed saved path is
complete_new_graphs / complete_new_relative_omega_angular_conclusion /
new_records / complete_strict_relative_omega_angular_orders_1_through_14.
It is an ordered list of fourteen complete record objects; entry $b-1$
bounds the ordinary ratio in (WDG.23).

At a frozen real base point, WSJ uses
$$
 {\cal J}F_{p,q}
       =\frac{t_0^p}{p!\,q!}
                    \partial_r^p\partial_\phi^q F,\qquad
 t_0=t(r_0,\phi_0).
$$
Therefore its initial relative-gap row is
$$
             W_{0,0}=1,\qquad
             |W_{0,b}|\le R^\omega_b/b!,\quad1\le b\le14 .
 \tag{WDG.24}
$$
This is the only conversion of the final ordinary record to a normalized
angular coefficient. The scale $t_0$ is frozen; it is not differentiated
as a coefficient.

The rest of the complete mixed route retains the actual equations
$$
 (p_\sigma)_r=\partial_\phi[(d+\sigma a)p_\sigma],\qquad
 \omega_r=d\omega_\phi-a x,\qquad
 X_r=d x-a\omega_\phi .
 \tag{WDG.25}
$$
Together with the full $a_r,a_{rr},d_r,d_{rr}$ predecessors, these are
triangular recurrences. They do not follow from an assumption that angular
control also bounds radial derivatives. In particular
$$
 \omega_{rr}=(d_r+d d_\phi)\omega_\phi
             +(d^2+a^2)\omega_{\phi\phi}
             -2ad x_\phi-(a_r+a d_\phi)x
 \tag{WDG.26}
$$
retains the derivatives of $\eta,q,d$.

WSJ.7--22 proves the full frozen mixed packet on its stated index sets.
It keeps the full $H^{-1}$, both phase reciprocals, every $t$-power,
$\mu^{-1}$, leading gauge, complete forcing and nonzero first-transport
cut trace. A relative gap bound is not a substitute for any of those
factors. In particular no complete inverse is replaced by its determinant
alone.

The local analytic root packet stays on its original domain. The drift
proof neither extends a real probability argument to a complex disk nor
uses $t^{-1}$ at the true root. Both physical mean coordinates, the scalar
mean ODE, $J,J_r$, all 3070 original interfaces, ordinary source measures,
jump norms, cut terms, positive/root response and the four waist endpoints
retain their original equations and order.

The actual 96 physical columns exist by their separate theorem. Their
still uncomputed signed normalization, the original finite factors,
$\nu$, Theta rows, and independent radial function inputs are not supplied
by (WDG.23).

## WDG7. Minimal complete numerical predecessor set

Only two existing scientific files are needed to obtain the 35 numerical
inputs. They are the complete WGS main and its bound companion from the
same run. Their exact identities are in WDG10.

| Records | Exact path within the admitted original file | Count | Endpoint |
|---|---|---:|---|
| $F_1,\ldots,F_4$ | companion / copied_original_scalar_records / flow_1 through flow_4 | 4 | upper |
| $F_5,\ldots,F_{14}$ | main / complete_higher_flow_and_cut_conclusion / flow_orders_5_through_15 / indices 0 through 9 | 10 | upper |
| $P_2,\ldots,P_{15}$ | main / complete_higher_flow_and_cut_conclusion / complete_strict_phase_angular_orders_1_through_15 / indices 1 through 14 | 14 | upper |
| $m_\Phi$ | main / complete_higher_flow_and_cut_conclusion / strict_phase_lower | 1 | positive lower |
| $T_1,\ldots,T_4$ | companion / copied_original_scalar_records / cut_t_1 through cut_t_4 | 4 | upper |
| $Y_c$ | companion / copied_original_scalar_records / y_cut | 1 | upper |
| $t_c^-$ | companion / copied_original_scalar_records / t_cut_lower | 1 | positive lower |

Each is a complete original object of shape {ball: original_string}.
No old numerical record is reformatted or replaced by a copied display
midpoint. The exact map of all 35 original objects has canonical UTF-8
length 3858 bytes, including its one final newline, and SHA-256
37315df6f0535d9fc8f742c1b753077e4d14afba64cb78a44930d01aae5112ce.
This is a text-copy identity, not a numerical computation.

The complete main's 36 fields, 24 successful gates, actual return code,
complete/proved status, runtime, source and math-module identities remain
part of admission. Its complete_original_inputs_file must identify the
actual full companion filename, byte count and SHA. Their run, attempt,
checkout, event, manifest, source and math-module identities agree exactly.

Retain the original main parameters, derivative certificate, strict
phase/flow scope and retained scope, together with the complete companion
scope objects. In particular the full-strip meaning of $Y_c$, the
original fixed intrinsic parameter, physical derivative convention and
all-shorter/both-orientations qualification must survive into the new
consumer. A filename or a positive number alone is not a domain certificate.

The old successful WGS graph has 437 slots. The 35 copied predecessors
are a deliberately small consumed subset; the original complete files
and all other successful slots remain immutable at their original paths.
The old two historical gzip stages are not restored or decoded again.
The companion already contains their complete qualified projection.

The former complete original mathematics and its historical formatter
failure remain distinguished exactly as in WGS admission. A new reader
must not reinterpret an old wrapper failure as scientific failure or
authorize a rerun of completed quantities.

## WDG8. Five fixed new groups and directed saving

The finite new-target graph is:

| New complete group | Exact complete output | New records |
|---|---|---:|
| cut high derivatives | ordinary $T_5,\ldots,T_{14}$, (WDG.18) | 10 |
| relative cut gap | ordinary $C_1,\ldots,C_{14}$, (WDG.20) | 14 |
| relative bulk derivative | ordinary $X_1,\ldots,X_{14}$, (WDG.21) | 14 |
| full transported contributions | ordinary $K_1,\ldots,K_{14}$ and $B_1,\ldots,B_{14}$, (WDG.22) | 28 |
| complete relative gap | ordinary $R^\omega_1,\ldots,R^\omega_{14}$, (WDG.23) | 14 |

The total is 80 genuinely new saved scalar targets. No final graph slot
copies an old successful mathematical target under a new name. The 35
original records are retained separately and unchanged.

A concrete single-science schema uses the following five conclusion keys:

1. complete_new_cut_T_high_angular_conclusion, containing
   ordinary_cut_T_orders_5_through_14;
2. complete_new_relative_cut_omega_conclusion, containing
   ordinary_relative_cut_omega_orders_1_through_14;
3. complete_new_relative_bulk_x_conclusion, containing
   ordinary_relative_bulk_x_orders_1_through_14;
4. complete_new_transport_relative_conclusion, containing
   ordinary_cut_contribution_orders_1_through_14 and
   ordinary_bulk_contribution_orders_1_through_14;
5. complete_new_relative_omega_angular_conclusion, containing
   complete_strict_relative_omega_angular_orders_1_through_14.

All arrays contain complete {ball: string} records and have the fixed
lengths above. Their mathematical declarations include ordinary angular
normalization, the exact strict interval, the true cut, the same selected
reference and the absence of a new root-domain assertion.

Finite coefficient extraction in (WDG.14) and (WDG.20) may use exact
integer/rational combinatorial coefficients and finite positive
convolutions. Internal polynomial coefficients are working arithmetic,
not additional separately declared scientific targets. All terms through
the requested degree are retained; no data-dependent polynomial cutoff is
introduced.

The first graph reads $Y_c$ and the exact $s_F=3/128$. The second
reads the saved new $T_5,\ldots,T_{14}$ together with old $T_1,\ldots,T_4$
and the positive lower for $t_c$. The third reads the old $P_2,\ldots,P_{15}$
and positive lower for $p_\pm$. The fourth reads the complete saved
$C,X$ arrays and old $F_1,\ldots,F_{14}$. The fifth reads the complete
saved fourth graph before taking the two uppers' maxima.

Every new record is durably saved in the complete current prefix and
printed before a formatting or size gate can fail. Successors use the
record read back from that saved representation. A complete graph is not
declared until every fixed record and scope field exists. Failure retains
all completed graphs, every produced record and the precise unfinished
target. No scientific graph may be automatically recomputed to repair an
operational failure.

Only $m_\Phi$ and $t_c^-$ are denominator records, and both use a
strictly positive lower endpoint. Every old norm upper and every saved
new upper is directed outward before it enters a positive expression.
Rational binomial signs are removed only in the complete coefficient
majorant of (WDG.20); the exact identity is established before this
triangle inequality.

The computation has zero new scalar exponentials, logarithms, square
roots, fractional numerical powers, ODE solves or radial integrals.
The notation $t^{3/2}$ in the proof produces only its finite rational
Taylor coefficients; a numerical implementation need not evaluate that
fractional power. All old flow and phase targets remain read-only.

## WDG9. What this proves and what the next complete candidate must retain

Equations (WDG.7), (WDG.16) and (WDG.23) prove a complete analytic recipe
for the same actual strict gap. Once its 80 new scalar targets are
evaluated under the complete old input admission, its final 14 records
are valid inputs to WSJ's separately indexed mixed construction.

No numerical improvement is asserted in advance. A new same-operator
candidate must carry the full new mixed geometry into the complete
leading/forcing/transport calculation, then into the complete nonmean
residual and its original receivers. The old WRT terminal regrouping,
old mean bounds, every jump, all four endpoints, positive/root source
terms and the finite factors remain available as complete unchanged
objects. Nothing may be subtracted from their old upper bounds.

A full old fallback can be retained for a requested derivative only with
the same actual function, domain, normalization and norm. A new full
coefficient bound and a safe old full coefficient bound may be compared
after each complete bound has been saved; this does not identify old
group maxima with individual derivative values. Pure geometric suprema
are not Fourier-Wiener bounds without their own valid conversion.

The purpose of the new construction is specific: avoid making every
angular derivative inherit a large radial derivative solely through an
old total-degree group, while preserving the entire true radial problem.
A successful finite scalar graph alone would still not prove a physical
incoming inverse, finite signed normalization, final metric Schur
inverse or nonlinear solution.

## WDG10. Complete immutable evidence

All listed source bodies were read as text. No old scientific module was
imported, no historical gzip restored, and no new scientific arithmetic
was executed for this proof.

| Evidence | Git blob | Bytes | SHA-256 |
|---|---|---:|---|
| WUA actual real fold and characteristic identities | 7b89251dcd51e8cb78fd3e8e42905114ef982ebf | 40111 | 9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad |
| WX complete positive products and shorter flow theorem | ef394649b79b06e27d7d3a36bdf98a7fcd801039 | 20033 | c5157bbb14b300c1a418642e96917b49f0f90c1ebc3571a124a26b863adc9ae1 |
| DX complete holomorphic cut and fourth flow theorem | f89dda096499d6ca8ee07afd0ffecf2b490ecb41 | 15978 | 6b493e3792c6863f9a65d8d52d994697d37de416157b68ed21f2cee51182f58b |
| WGS complete sufficient mixed-jet contract | 4980f1a2c119b6470afc24a2fc662c75fa210479 | 28978 | 4d3638fe6ae8793b937d4c7f57a4c092d59d41df94991722d8b622ed958e576e |
| WGS original no-entry finite math source | afa3b49b2035be07abee6a7f9041899c135dcdea | 31846 | cb9c9aa0f7e5749967ece4e51210f359b4c58eecc7f83a05040607543ac47621 |
| WGS complete actual main, run 43820816332/1 | 32ff92c516fcc5c43f3619930d4845d294289270 | 72251 | 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e |
| WGS complete original-input companion, same run | d6d13860e322d82ce354c8c0d0eb0f279ca63b3c | 31632 | 3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66 |
| WSJ separate scaled mixed-jet recipe | 10c6e4220377b772692095347f096e5d897afc5e | 31568 | 217cdff81516dd827122987ba6abe9a2cdacb6597d01fe9b4ee58a47faa8960d |

The two numerical input files are
notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json
and complete-original-inputs.json in the same directory, under
topics/visible-flex-exact-nearby. Their full byte identities, not these
printed labels alone, determine the admitted input.

The primary proof links are [WUA](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md),
[WX](R133-supplement-complete-true-waist-coordinates-from-saved-positive-products.md),
[DX](R133-supplement-complete-fourth-angle-derivatives-from-saved-cut-and-flow-bounds.md),
[WGS](R133-supplement-complete-global-fold-and-free-first-transport-finite-jets.md),
and [WSJ](R133-supplement-scaled-strict-mixed-jets-and-exact-fold-inverses.md).
The WGS source is scripts/fourfold_codazzi_global_fold_free_transport_jet_math.py.

The new 80-target contract is unexecuted at publication of this lemma.
The main theorem is the exact positive representation, the justified
reuse of all-shorter drift derivative envelopes, and the full relative
angular recipe through order fourteen.
