# R142 input: the actual R127 complete mean, height and embedded annulus

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-13.

**Proved for the existing full-frequency R127 family.** On the original two physical cells 11 and 10, the complete algebraic mean restores the missing mean evolution equation. The same field therefore defines a complete Darboux height and a single-valued (C^2) isometric **embedded annulus**. All real parameters in the original R100 six-unit-axes times transverse weighted-ℓ1 radius (1/32), and all common real angular phases, are covered. The metric is the original fixed R26 metric. No new metric, outer cells 0 through 9, or closed surface is asserted here.

The new exact consumer also pays the complete mean-height correction and gives a full physical two-jet and analytic Cauchy interface at node 10. This conclusion does not require the separate 46-parameter cut map to have passed. Gluing to the already existing inner tail does require that same complete cut equation; the conditional gluing statement is explicit in Section 6.

## 1. Actual input and the normalization bridge

The primary input is the completed R127 certificate

`joint1200-r1-certificate.json.gz`, SHA256
`36242d95a210e6aee3e38c994d0a70b61fa1fbb2df672a9ab3f4783bcca93ca1`.

It is the full (1200)-component Banach problem, not a Fourier truncation: low modes 2 through 92, all middle modes through 34814, and every even high mode of absolute value at least 34816. Its original full mean and inverse, all 25 comparison blocks and 10793 source leaves, and the original mixed boundary conditions remain fixed.

The `physical` field of [R98](../results/R98-mixed-density-low-middle-high-closure.md), [R106](../results/R106-physical-correlation-and-complete-mean-remainder.md), and [R127](../results/R127-complete-low-middle-high-mixed-boundary-family.md) is already the *relative* field

\[
P=\frac{h_\theta}{rw},\qquad \bar K=\frac{h_{\perp,r}}w.
\tag{1}
\]

It is not the unnormalized slope (h_r), and no extra factor of (w), (r_x), or Fourier pair 2 is available. The complete scalar mean is (c), and (K=c+\bar K).

Let (R_j) be the actual stored complete physical radius on block (J_j). The fresh consumer reconstructs each original formula

\[
(10+U_j+r_j)V_{j,\max}+b_jh_j\le R_j,
\qquad
b_j=\begin{cases}18555&j=5,\\R_{\mathrm{profile},\max}&j=21,\\V_{j,\max}&\text{otherwise},\end{cases}
\tag{2}
\]

from the same 1150 low radii, 25 middle radii, 25 high radii, and physical conversions. All 25 exact inequalities pass. The common moving strip is everywhere strictly greater than (1/64). Summing the fixed, mode-first radial suprema over the finite block cover gives a legitimate global bound at constant strip (1/64):

\[
\mathcal R:=\sum_{j=0}^{24}R_j
 =5.979972094066725\ldots\,10^{-12}<2^{-37}.
\tag{3}
\]

This uses (\sum_m\sup_r\le\sum_j\sum_m\sup_{J_j}), never the reverse interchange. At each individual radius the sharper bound is

\[
R_{\max}=\max_jR_j
=2.018369496869698\ldots\,10^{-12}<2^{-38}.
\tag{4}
\]

The actual outgoing node-10 bound is the last block bound,

\[
R_{10}=3.681532503212271\ldots\,10^{-15}<2^{-47}.
\tag{5}
\]

Every decimal in this note is a display of an exact rational or an outward dyadic. The primary keeps the exact outward values.

## 2. The projected system is the complete system

Put (s=r_x/r>0), (\ell=w_x/w), (z=w^2\le1/4), (E=1+z\le5/4), and

\[
T=P_\theta,\quad U=\bar K_\theta-P,\quad y=1+K,
\quad S=1-zP^2,\quad D=ES-zy^2,
\]
\[
L=y+ET,\qquad N_\Omega=1+\frac{zyT}{S},\qquad
\Omega=\frac{N_\Omega}{\sqrt D}.
\tag{6}
\]

The mean in the original contraction is the complete root

\[
\mathcal M=\frac{\langle\Omega\rangle-1}{z}=0,
\qquad |c|\le4R^2.
\tag{7}
\]

For any one of the radii (R) used in (3)--(5), or the original local radii, set

\[
p=R/3,\quad k=R/3+4R^2,\quad
v=p^2/4,\quad u=(2k+k^2+5p^2/4)/4.
\]

The exact consumer pays all of the following positive lower bounds:

\[
S\ge1-v,\quad D\ge1-u,\quad y\ge1-k,
\quad L\ge1-4R^2-5R/4,
\]
\[
N_\Omega\ge1-\frac{(1+k)R}{4(1-v)},\qquad
\mathcal M_c=\left\langle\frac{L}{D^{3/2}}\right\rangle
\ge\frac{1-4R^2-5R/4}{(1+u)^2}.
\tag{8}
\]

Each displayed lower bound is greater than (1/2). These inequalities hold in the corresponding Wiener algebra as needed for the inverse, and on the real angles for positive square roots. The mean root is (C^1) radially on each chart, by its original complete analytic construction and the positive implicit derivative. R127's equations give the needed radial regularity at any strictly smaller positive angular strip.

For clarity, write the *unprojected* quotient as

\[
\mathcal N_{\rm full}
=\frac{EsU^2+\ell\{(K+T)^2+z(2KT+T^2-P^2)\}}{L}.
\tag{9}
\]

The R127 fixed point gives exactly

\[
f_P:=P_x-sK_\theta+(s+\ell)P=0,
\qquad
\Pi_\perp f_K=0,
\]
\[
f_K:=K_x+\ell(2K+T)-\mathcal N_{\rm full}.
\tag{10}
\]

Here (\Pi_\perp) removes only the angular constant. It retains *all* nonzero modes; this assertion would not follow from a finite Galerkin system.

By [R75, (75.11)](../results/R75-complete-mean-transport-and-shear-constraint.md), with the same complete angular measure,

\[
\mathcal M_x+2\ell\mathcal M
=\left\langle W(f_K-\alpha f_P)\right\rangle,
\qquad W=L D^{-3/2},\quad\alpha=EU/L.
\tag{11}
\]

Equations (7) and (10) make the left side and (f_P) zero. The other equation in (10) says (f_K=a(x)) is an angular constant. Thus (a(x)\langle W\rangle=0). The strictly positive bound (8) proves

\[
\boxed{f_P=f_K=0.}
\tag{12}
\]

In particular the complete mean evolves by the exact equation

\[
c_x=-2\ell c+\langle\mathcal N_{\rm full}\rangle.
\tag{13}
\]

No zero coefficient of the numerator is discarded before the infinite inverse, and the scalar root is not held fixed during differentiation. The identity concerns the existing exact R127 solution. It does not replace an actual derivative of a numerical candidate by its ODE right-hand side.

## 3. One complete height and the actually paid mean primitive

Choose one real number (h_0(r_{12})) for the entire two-cell interval. Define

\[
h_\perp=rw\,\partial_\theta^{-1}P,
\qquad
h_0(r)=h_0(r_{12})+\int_{r_{12}}^r w(\rho)(1+c(\rho))\,d\rho.
\tag{14}
\]

The first equation of (12) proves

\[
(h_\perp)_r=w\bar K,\quad h_\theta=rwP,\quad h_r=w(1+K).
\tag{15}
\]

Consequently this is one (C^2) height, analytic in angle, piecewise smooth in the original physical radius. Both complete equations imply the full Darboux equation by the exact identity in [R44](../results/R44-compatible-outer-height-and-continuous-defect.md). Across node 11 and source-chart seams, R127 keeps the same physical traces; the fixed R26 background and the complete equation give the same physical two-jets. A change of source chart is not a reset of (14).

The original five positive R48 moments obey the exact identity

\[
I_{00}+I_{01}=\int_{\mathrm{cell}}w\,dr,
\tag{16}
\]

because their two nonnegative basis functions sum to one. This identity is independent of the finite candidate used to produce those background moments. We consume the original cell-11 complete 5545-panel recovery and the sharper same-object cell-10 5248-panel Taylor moments. Their fixed ready-file SHA is the same original
`563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6`.
Both actual resource records have formal exit zero.

Let (R_n^{\rm cell}=\max_{J_j\subset\mathrm{cell}\ n}R_j). The scalar mean obeys (\sup|c|\le4(R_n^{\rm cell})^2), hence its entire primitive correction is bounded by (4(R_n^{\rm cell})^2(I_{00}+I_{01})_{\rm upper}). The actual results are:

| Cell | (\int w\,dr), upper | Complete (\sup|c|), upper | Mean-height correction, upper |
| --- | ---: | ---: | ---: |
| 11 | (5.502017192740257\,10^{-10}) | (4.705566399361823\,10^{-33}) | (2.589010723086962\,10^{-42}) |
| 10 | (2.231828505680733\,10^{-9}) | (1.629526170357616\,10^{-23}) | (3.636822957756883\,10^{-32}) |

The total non-background mean-height change is strictly below

\[
3.636822958015784\,10^{-32}.
\tag{17}
\]

This is a paid bound for the *same exact field*, not a Gauss-rule estimate for a different saved mean. The primary separately stores the background integral interval and this correction, and their combined interval under the single convention (h_0(r_{12})=0). One may later change the single global additive constant. One may not independently reset it at node 11, prescribe a second terminal mean height without paying its integral condition, or identify a finite sampled primitive with (14).

## 4. Actual node-10 Cauchy data, full two-jet and infinite tail

The source background at nodes 12, 11 and 10 is read from the four original one-panel source groups that are also pinned by the successful signed geometry. Radius, (w), (r_x) and (\ell) are the original true intervals. In particular

\[
|w_r|\le \frac{w_+\max(|\ell_-|,|\ell_+|)}{(r_x)_-}.
\tag{18}
\]

No derivative of a rounded background fit is introduced. At node 11 we use both valid one-sided bounds for the same physical object. Their exact equality follows from the R26 definition and R127 physical matching, not merely from intersecting numerical intervals.

For a port radius (R), write (p=R/3), (k=R/3+4R^2), (L_-=1-4R^2-5R/4). The unprojected quotient satisfies

\[
\|\mathcal N_{\rm full}/(s+|\ell|)\|_{0}
\le B(R):=\frac{(23/18)R^2+10R^3+16R^4}{L_-}
<\frac32R^2.
\tag{19}
\]

The zero coefficient is included in (19). Thus

\[
|h_0''-w_r|\le4|w_r|R^2+(w/r+|w_r|)B(R).
\tag{20}
\]

The other full physical jet bounds follow from (15), the minimum nonzero frequency 2, and the exact identity

\[
h_{rr}-w_r
=\frac{EwU^2/r+w_r(-K-T+w^2KT-w^2P^2)}{L}.
\tag{21}
\]

In particular

\[
\begin{aligned}
|h_\perp|&\le rwR/6,& |h_r-w|&\le wk,& |h_\theta|&\le rwR/3,\\
|h_{r\theta}|&\le wR,& |h_{\theta\theta}|&\le rwR,\\
|h_{rr}-w_r|&\le\frac{(5/4)wR^2/r+|w_r|(k+R+kR/4+p^2/4)}{L_-}.
\end{aligned}
\tag{22}
\]

These are full angular Fourier norm bounds and therefore pointwise bounds. The node-10 values are:

| Quantity | Strict outward upper bound |
| --- | ---: |
| (\|P\|_{1/64,1}+\|\bar K\|_{1/64,1}) | (3.681532503212272\,10^{-15}) |
| (|h_\perp|) | (1.401857849902089\,10^{-26}) |
| (|h_r-w|) | (5.593432789966824\,10^{-25}) |
| (|h_\theta|) | (2.803715699804178\,10^{-26}) |
| (|h_{rr}-w_r|) | (1.942177908610981\,10^{-24}) |
| (|h_{r\theta}|) | (1.678029836989974\,10^{-24}) |
| (|h_{\theta\theta}|) | (8.411147099412534\,10^{-26}) |
| (|h_0'-w|) | (2.471088554495430\,10^{-38}) |
| (|h_0''-w_r|) | (1.857838163143517\,10^{-37}) |

The relative data are analytic at width (1/64). For any even cutoff (M\ge2), the entire signed tail at width (1/128) has strong norm at most

\[
R_{10}e^{-M/128}
\le R_{10}\left(1+\frac{M}{128\cdot4096}\right)^{-4096}.
\tag{23}
\]

The right side is computed with exact rational arithmetic and is strictly positive. For (M=34816), the actual exported bound is below (1.565756695434168\,10^{-129}). No floating underflow zero or finite support is asserted. More generally, for angular derivative order (q\ge1), lowering the strip to (1/128) gives

\[
\|\partial_\theta^q(P,\bar K)\|_{1/128,0}
\le(q-1)!128^{q-1}R_{10}.
\tag{24}
\]

Indeed (m^q/(1+m)\le m^{q-1}) and (e^{m/128}\ge(m/128)^{q-1}/(q-1)!). This provides the genuine infinite-dimensional Cauchy trace for a later outer continuation calculation.

## 5. Single-valued development and embedding of the whole annulus

Let (p_{m phys}=wP), (k_{m phys}=w(1+K)). The metric (q=g-dh^2) is positive definite because (D>0). Complete Darboux makes it flat, by [R32, (32.10)](../results/R32-height-development-and-global-tail-graph.md). Equivalently use the explicit complete connection of [R41, Section 5](../results/R41-exact-angular-connection-inverse.md):

\[
a=r\sqrt S,\quad u=-\frac{k_{m phys}p_{m phys}}{\sqrt S},
\quad v=-\frac{\sqrt D}{\sqrt S},\quad
\gamma_\theta=\Omega,\quad
\gamma_r=\frac{k_{m phys}(\partial_\theta k_{m phys}-p_{m phys})}{rS\sqrt D}.
\tag{25}
\]

The two angle derivatives form a closed one-form. On the angular cover, define (t=(\cos\gamma,\sin\gamma)) and its left unit normal (n). The closed horizontal vector form is

\[
X_\theta=a t,\qquad X_r=u t+v n.
\tag{26}
\]

It remains necessary to prove *translation* holonomy, not only rotational holonomy. The original even modes and complete algebra preserve (\pi)-periodicity of (S,D,\Omega,a,u,v). The complete mean condition gives (\langle\Omega\rangle=1), so

\[
\gamma(r,\theta+\pi)-\gamma(r,\theta)=\pi,
\qquad X_\theta(r,\theta+\pi)=-X_\theta(r,\theta).
\tag{27}
\]

The full angular integral of (X_\theta) is exactly zero. Thus the plane development is single-valued on the entire annulus; height periodicity follows from the zero mean of (P). A single planar translation and rotation, and the one height constant already specified, are the remaining rigid gauges. The piecewise closed-form construction and physical two-jet matching give (C^2) regularity across the finite source-chart seams, exactly as in R32's weak connection argument.

All the positive branch gates were paid in Section 2. In particular (a>0) and (\Omega>0), so every radial level is a regular strictly convex closed plane curve of turning number one. This assertion follows from its tangent-angle parametrization, not from plotted samples.

For a direct global injectivity proof, reparametrize each convex curve by the outward Gauss angle (\phi), and let (s(r,\phi)) be its support function. Holding (\phi) fixed only adds a tangential reparametrization term to (X_r). Therefore

\[
\partial_r s(r,\phi)=X_r\cdot(-n)=-v=\frac{\sqrt D}{\sqrt S}>0.
\tag{28}
\]

On real angles (S\le1), so a paid rational lower bound is (D_-), since (\sqrt D\ge\sqrt{D_-}\ge D_-) when (0<D_-\le1). The primary verifies this bound greater than (1/2) using the global radius (3). Hence distinct radial levels enclose strictly nested convex domains. No two levels intersect, and each level is one-to-one. The positive Jacobian in (26) gives the local diffeomorphism. It follows that (X) maps the compact two-cell annulus one-to-one onto the region between its two nested convex boundary curves. Consequently (F=(X,h)) is a (C^2) embedding and

\[
F^*\langle\ ,\ \rangle=E(r)\,dr^2+r^2d\theta^2
\tag{29}
\]

exactly. This is an annulus statement; a closed surface, reach and visible motion do not follow from it.

R127's actual parameter continuity in its full Banach ball, the analytic mean root, the explicit complete equation, and formulas (14), (21), (25)--(26) give (C^2) continuity for real parameters after fixing the same rigid gauges. Common real phase translations preserve every bound and every even-mode/period identity used above.

## 6. Exact inner gluing and the remaining outer continuation

If the same R127 field and the same R100 inner field satisfy their complete 46-parameter cut equation, then all low physical traces at node 12 agree. The higher physical traces already agree by the prescribed R127 boundary data. Thus (P,\bar K), and their angular derivatives agree at that node. The complete scalar roots agree by uniqueness on the paid branch. Formula (21), with the same true (r,w,w_r), then proves equality of the entire physical height two-jet.

There is only one mean-height constant to align. Choose it once to equal the inner height at node 12. The horizontal trace and frame are similarly aligned by one planar rigid motion; equations (25)--(26) then match their complete first and second physical derivatives. This gives a (C^2) same-metric gluing, retaining the inner field's independent far coordinate and flat-cuff limits. It is not an additional nonlinear solve and does not create a free outer mean slope. This paragraph is conditional on the complete cut equation; R127 alone did not prove it.

The genuinely remaining outward problem starts at the *actual node-10 full trace* just constructed. It must solve the complete equations (9)--(12) on the unchanged real background through cells 9 down to 0. In particular it must preserve a positive branch (S,D,y,N_\Omega,L), pay the entire even high-frequency propagation and analytic-width consumption, and use the same full root when the small R33 ball is no longer appropriate. The existing R64/R66 general-mean candidate is a possible comparison object but is not this exact Cauchy solution: its retained radial residual cannot be set to zero. Nor does the small, strictly positive tail bound (23) by itself pay a positive analytic loss across ten uncomputed cells.

The endpoint tuple paid here consists of the original (g) and physical radius, the genuine analytic (P,\bar K) trace, its complete mean, the single accumulated mean height, the complete Darboux second derivative, and its full infinite remainder. No new independent mean-slope boundary condition remains. Full outer propagation, its true terminal geometry, reach on the whole surface, and the README closed-family/amplitude criteria remain separate obligations.

## 7. Actual execution and saved result

The fresh source is
`2026-11-13-exact-resume-r127-mean-height-bridge-v1.py`, SHA256
`0764ee7d946ab1144a09705d4623a33018c4940f2229b18794b5712fba5aace6`.

Input manifest SHA256:
`608c11a4d3e294518e6e5230a450481e1b2c59154c8e6fdcd822fcf0be2fccb2`.
It pins 17 input files, including the original proofs and completed resources. The new producer uses only exact `Fraction` arithmetic and outward 160-bit dyadics. It rechecks all 25 complete physical-radius formulas, the 18 groups and 10793-leaf count, the unchanged original head normalization, all required branch inequalities, positive background moments, the four true endpoint source identities, and nonzero exact tail bounds. Serialization has 158 independent outward comparisons.

The owned command actually completed with formal wait4 **exit 0**, no signal, wall **0.742245674 seconds**, peak **19536 KiB**. All **175 gates** passed. There was no new ODE, source integration, Newton solve or Fourier truncation.

Primary: `r127-mean-height-bridge-r1.json`, SHA256
`b26c36452bc651f8d1ce55f9da23b6c904ad209878c268787a38cdce45612ae5`.

Resource: `r127-mean-height-bridge-r1-resource.json`, SHA256
`dc6a9d12e7fb0915e31b743d08c3f7c4d09000e52a09c2bbcc3600b0eec1484f`.

The complete chain in Sections 2 and 5 was independently read by geometry_audit. In particular the review checked the constant-residual argument, exact half-turn cancellation of translation holonomy, and support-function monotonicity. This review did not substitute for any actual arithmetic or expand the conclusion beyond the original two-cell annulus.
