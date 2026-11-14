# R114 — Actual eighteen-block local-V solution of the m94/m96 projected equation

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

**Proved, with completed actual linear enclosure and exact nonlinear budget.** Fix a real parameter in the original R74 twenty-axis domain and its common angular phase. Let $C_L$ be the same complete low46 projected solution furnished by R91/R101, with the original outer low boundary targets. On the true outer cells 11 and 10, the equation

$$
v=M_{\mathrm{bd},\{94,96\}}+
\mathcal G_{\{94,96\}}\Pi_{\{\pm94,\pm96\}}\mathcal N(C_L+v)
\tag{1}
$$

has a unique solution in the explicit eighteen-block ball below. The two true head components, complete mean small root and full inverse denominator remain present. The complete weighted contraction constant is strictly less than $1/2$.

Equation (1) keeps $C_L$ fixed. It is the declared two-mode projected equation. Its solution does not assert the other nonmean equations, low feedback, all middle frequencies, infinite high feedback, all-46 cut matching, or a closed surface. In particular, $C_L+v$ is not asserted to solve the full outer PDE.

## 1. Same exact problem and norms

Keep R104's order $J_0,\ldots,J_{17}$, namely cell11 segments 0–8 followed by cell10 segments 0–8. The background is the same R26/R87 real source and actual physical radius. The positive piecewise constant $V_I$ is the original R84/R90 dyadic on each of the 10793 source leaves. No candidate, degree, source profile, flow tolerance, or physical endpoint is changed.

With $\tau_*=18/125$, define

$$
X_i(v)=\sum_{m\in\{\pm94,\pm96\}}(1+|m|)
\left[
\sup_{x\in J_i}\frac{e^{\tau_*|m|}|P_m(x)|}{V_I(x)}
+\sup_{x\in J_i}\frac{e^{\tau_*|m|}|K_m(x)|}{V_I(x)}
\right].
\tag{2}
$$

The two component suprema and all Fourier modes are summed separately. The physical functions are continuous at the true interfaces; $V_I$ is only the fixed norm weight. This defines a complete space on the closed subspace satisfying the interfaces.

R101 gives the complete low46 centre norm less than 10 and explicit complete source caps $b_{94},b_{96}$ at the same constant strip. Its real R100 domain contains the real R74 domain: R100 retains the first six R74 axes and certifies that the other fourteen old axes together occupy less than $.046804$ of its forty-axis weighted $\ell^1$ ball. Thus the R78 head data and the R101 centre/source data may be used together on the stated real R74 restriction. No bound for the larger R100 head is inferred from the R78 packet.

## 2. True source origins with the actual target V divisor

Use the signed trace-zero system $Y=F(P_{\sin},K_{\cos})^T$, $F=\sqrt{rw^3}$, from R104. For every source origin $a_j$, preserve both signed columns of $A_{j,m}(x)=\Phi_m(x,a_j)$ to the actual target. The old independent radial and $|\log w|$ integrals $I_{j,m,a,0}^{(p)},I_{j,m,a,1}^{(p)}$ remain unchanged, for $p=2,1,0$.

The added readout is exactly

$$
\frac{|A_{j,m,\nu1}(x)|I_{j,m,a,1}^{(p)}(x)
      +|A_{j,m,\nu2}(x)|I_{j,m,a,0}^{(p)}(x)}{F(x)V_I(x)}.
\tag{3}
$$

For each true target subpanel the strictly positive lower endpoint of $F V_I$ is used before taking its component supremum. The complete current subpanel's nonnegative source integral is charged before the target supremum, so the ordered source/target diagonal is included. This is the same conservative whole-subpanel argument as R104, now in the actual local-$V$ norm.

Summing the two component suprema and two source materials, and multiplying by $1+m$ once, gives $\gamma^{(p),V}_{ijm}$ for every $j\le i$, both actual modes, and all three materials. Set

$$
G_{ij}=\max_{m=94,96}\gamma^{(2),V}_{ijm},\qquad G_{ij}=0\quad(j>i).
\tag{4}
$$

This maximum applies to a shared fixed source modal mass, with no mode-count factor. For the separately known pure centre caps retain instead the sum

$$
R_i=\sum_{j\le i}\sum_{m=94,96}\gamma^{(2),V}_{ijm}b_m.
\tag{5}
$$

Both genuine physical initial columns receive the same target-$V$ readout. The balanced head argument of the preceding proved head-lift note is applied separately on each target block, giving $H_i$. It uses the common R78 near-band mass only once, the correct $P$-input factor $1/B_b$, and the paid head-to-output strip loss.

The new producer additionally evaluates the exact correlated weak rows $C=K_{\cos}+mP_{\sin}$ and $U=-P_{\sin}-mK_{\cos}$ before absolute value. Those valid readouts remain in the packet for subsequent source estimates; they are not needed to improve a bound without actually being consumed here.

## 3. Full nonlinear source and derivative on each block

Let $X_i(v)\le r_i$. On a leaf in $J_i$, the complete physical strong input is bounded by $(10+r_i)V_I$. The exact consumer verifies

$$
(10+r_i)V_{i,\max}<2^{-34}<1/64
\quad\hbox{for all eighteen blocks}.
\tag{6}
$$

Consequently the complete R33/R98 mean root and inverse denominator are defined on the whole convex ball and all line segments used below. This domain check precedes the fixed-point conclusion; it is not inferred from a putative solution.

R98's complete quotient estimate, in fixed radial Fourier masses, gives

$$
\|\mathcal N(C_L+v)-\mathcal N(C_L)\|_{\text{weak},J_j}
\preceq c_{\rm bg} V_I^2(40r_j+2r_j^2).
\tag{7}
$$

The notation means the same source-density norm used by (3), with the complete mean and inverse retained. Along the same whole ball, its complete derivative satisfies

$$
\|D\mathcal N(C_L+v)[\delta v]\|_{\text{weak},J_j}
\preceq4c_{\rm bg}V_I^2(10+r_j)X_j(\delta v).
\tag{8}
$$

This follows from the actual complete derivative bound, not by differentiating an upper estimate. Applying the true causal kernel yields

$$
X_i(Tv)\le\Phi_i(r):=H_i+R_i+
\sum_{j\le i}G_{ij}(40r_j+2r_j^2),
\tag{9}
$$

and the positive derivative comparison

$$
J_{ij}=4G_{ij}(10+r_j)\quad(j\le i),\qquad J_{ij}=0\quad(j>i).
\tag{10}
$$

The centre source in (5) includes its whole inverse tail; replacing it by an identically zero quadratic high source is not part of this proof.

## 4. Explicit radii and a complete contraction metric

In increasing causal order set

$$
A_i=H_i+R_i+\sum_{j<i}G_{ij}(40r_j+2r_j^2),
\qquad
r_i=\operatorname{up}_{96}\frac{2A_i}{1-40G_{ii}}.
\tag{11}
$$

Every denominator is strictly positive. The actual saved dyadics, rather than the unevaluated expression, are then substituted in the full eighteen inequalities $\Phi_i(r)<r_i$.

For the distance norm choose $q=1/2$ and recursively set

$$
W_i=\operatorname{up}_{96}
\frac{1+\sum_{j<i}J_{ij}W_j}{1/2-J_{ii}}.
\tag{12}
$$

Every denominator is positive. The exact consumer then verifies every complete row $(JW)_i/W_i<1/2$, with all earlier sources included. These are finite positive weights, so

$$\|v\|_W=\max_i X_i(v)/W_i$$

is an equivalent complete norm. Equations (6), (9), and (12) prove that the complete nonlinear map of (1) preserves the closed ball and is a strict contraction there. Banach's theorem gives the claimed solution and uniqueness within that ball. The real symmetry and common-phase subspaces are preserved. Continuous dependence on the original real parameters follows from the same uniform contraction and the already proved continuous head and low-centre families.

## 5. Actual values and physical interface

All eighteen self-map and distance rows passed using exact Fraction arithmetic. The principal displays are

$$
\max_i r_i=0.5659044912555777\ldots<\frac{567}{1000},
$$
$$
\max_i\Phi_i(r)/r_i=0.5013874011456986\ldots<\frac{503}{1000},
$$
$$
\max_i(JW)_i/W_i=0.4999999999187707\ldots<\frac12,
$$
$$
\max_i(10+r_i)V_{i,\max}=9.35339107968022\ldots\,10^{-13}<2^{-34}.
\tag{13}
$$

The largest radius is at cell10/segment7. Representative earlier radii are $r_0=2.84679\ldots\,10^{-21}$, $r_3=2.22403\ldots\,10^{-16}$ and $r_{12}=2.80154\ldots\,10^{-7}$. The actual target-$V$ normalization changes the limiting diagonal comparison at cell10/segment3 from the old physical-radius $40\Gamma_1\approx43427$ to $40G_{12,12}\approx0.002774803$. This changes the positive comparison ball; neither number is a lower bound for the true nonlinear operator.

The physical strong norm over the whole two-cell interval must also pay separate radial component suprema. A valid bound is the sum over all blocks:

$$
\|v\|_{\mathrm{ph},\tau_*}
\le\sum_{i=0}^{17}r_iV_{i,\max}
<2^{-62}.
\tag{14}
$$

The exact sum has display $1.3614960338518304\cdot10^{-19}$. It is recorded in `2026-11-13-exact-resume-localV-physical-interface.json`; each $V_{i,\max}$ is recovered exactly as the saved domain bound divided by $10+r_i$. Thus this two-mode contribution is also below the R98 given-middle physical cap $2^{-43}$. Formula (14) does not count uncomputed middle modes or establish the high fixed point.

All formal comparisons use the saved integers and exponents. The displayed decimals in this note are not input parameters.

## 6. Completed computation and reproducibility

The actual producer is `2026-11-13-exact-resume-localV-correlated-v8.py`, SHA256 `e17ec73745972cd2bc012c4bade80269b2712368515ceaaf02c3d5d7ec7a8234`. Its completed primary is `2026-11-13-exact-resume-localV-r3.json.gz`, 513887 bytes, SHA256 `0eb5b16386948b6939c745198f4a5aba418e75f8bfffd61e9fcf40f5b619abfb`.

The actual full run terminated with exit 0: wall 238.677367210 seconds, peak 44928 KiB. All twelve enclosure gates are true. The complete original physical tensor was reproduced bitwise against the fresh recovered R104 primary. Counts are unchanged: 18 original source segments, 10793 leaves, 10872 Taylor subpanels, 8 root brackets and 71 subdivision rejections. Precision 256, order 24, root bits 160 and remainder gate $2^{-100}$ are unchanged.

The v6 attempt reached thirteen complete groups and then hit the inherited one-megabyte uncompressed checkpoint limit. The v7 attempt stopped during dependency preflight after a filename-extension error. These failed attempts are retained, with their actual resources. The completed v8 run only changes new tensor output serialization to streaming gzip and keeps original input names. It was replayed from the original inputs because the earlier checkpoints do not serialize all active source-origin state; no unsupported checkpoint recovery was claimed.

`2026-11-13-exact-resume-localV-budget-consumer.py` consumes the full successful primary, the fresh original R104 primary, the completed balanced-head ledger and the R101 exact complete-source summary. Its actual exact output is `2026-11-13-exact-resume-localV-budget-r1.json`. It took approximately $.3644$ seconds and peaked at 23272 KiB. It includes every original source position, all three source materials, both modes and all eighteen radii/distance rows. No new ODE, radial integral or Arb operation is used by this consumer.

The legacy one-radius diagnostic fields in the linear primary remain false. They concern the old aggregate scalar test and are not altered. The new conclusion uses the distinct, explicitly defined eighteen-block norm and its completed full row checks.

## 7. Remaining interface

The remaining middle modes $98,100,\ldots,5758$ require true uniform kernel/source bounds. The low and infinite high feedback equations also remain in the full coupled problem. Weakening an analytic strip, suppressing uncomputed source projections, assigning a zero high initial trace, or applying a two-mode norm to the full middle block would change the proof obligations and is not justified by (1)–(14).
