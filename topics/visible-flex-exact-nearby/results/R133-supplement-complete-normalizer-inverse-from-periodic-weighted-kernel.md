# Complete normalizer inverse from the periodic weighted kernel

**Status.** Proved analytic refinement for the same complete real normalizer in CN and NW. This result retains both weighted mean conditions. It introduces a new positive scalar bound that can read the successful NW exponential verbatim. It does not repeat the cohomological solve, any Fourier budget, or the exponential evaluation.

## 1. The fixed operator and circle

Use the physical circle and normalized norm from CN:
$$
 \ell=\frac{\pi}{2},\qquad
 \langle f\rangle=\frac1\ell\int_0^\ell f(x)\,dx,\qquad
 I=\partial_x^{-1}(1-\Pi),\qquad \Pi f=\langle f\rangle .
 \tag{NPK.1}
$$
The real, zero-mean coefficient $w$ and its zero-mean primitive $p=Iw$ are the same coefficients already constructed in NW. In particular, $w$ is not either individual incoming or outgoing principal coefficient. Write
$$
 a=e^p>0,\qquad N=\operatorname{Id}+M_w I .
 \tag{NPK.2}
$$
The available regularity $w\in H^2$, $p\in H^3$ is more than sufficient for the formulas below. Every result applies to complex inputs, with real $a,w,p$. The inverse is the same inverse on the full scalar circle; it is not an inverse of a high-frequency compression.

Let the already saved positive bounds satisfy
$$
 \|w\|_\infty\le W_0,\qquad
 \|w\|_{\mathcal W_{1/3}}\le W_{1/3},\qquad
 \|p\|_\infty\le P_0,\qquad E_0\ge e^{P_0}.
 \tag{NPK.3}
$$
In the successful NW consumer, $E_0$ is the single previously evaluated low-order exponential. No new exponential is needed for this refinement.

## 2. Both weighted means in one exact kernel

For an input $f\in L^2$, the complete CN inverse first forms
$$
 m_f=\frac{\langle af\rangle}{\langle a\rangle},\qquad
 u=I\{a(f-m_f)\},\qquad
 \kappa=-\frac{\langle a^{-1}u\rangle}{\langle a^{-1}\rangle},
 \qquad z=a^{-1}(u+\kappa),\qquad h=f-wz .
 \tag{NPK.4}
$$
The two weighted means have different purposes: the first makes $a(f-m_f)$ have zero ordinary mean; the second makes $z$ have zero ordinary mean.

To combine them without discarding either one, define the nonnormalized Lebesgue integrals
$$
 A(x)=\int_0^x a(t)\,dt,\qquad A_\ell=A(\ell)>0,\qquad
 d\nu(y)=\frac{a(y)^{-1}\,dy}{\int_0^\ell a(s)^{-1}\,ds}.
 \tag{NPK.5}
$$
Thus $\nu$ is a positive probability measure. On the fixed coordinate interval $[0,\ell]$, put
$$
 G(x,t)=\mathbf 1_{\{t\le x\}}-\frac{A(x)}{A_\ell},\qquad
 \overline G(t)=\int_0^\ell G(y,t)\,d\nu(y).
 \tag{NPK.6}
$$
Values at the diagonal and at the endpoints have no effect on the integral operator. Then the exact kernel formula is
$$
 z(x)=
 \int_0^\ell
 \frac{a(t)}{a(x)}
 \bigl(G(x,t)-\overline G(t)\bigr) f(t)\,dt .
 \tag{NPK.7}
$$

Indeed, the primitive with value zero at $x=0$ is
$$
 u_0(x)=\int_0^x a(t)(f(t)-m_f)\,dt
       =\int_0^\ell a(t)G(x,t)f(t)\,dt .
 \tag{NPK.8}
$$
It is periodic because $u_0(\ell)=u_0(0)=0$. The CN primitive $u$ differs from $u_0$ by a constant. Subtracting the $a^{-1}$-weighted mean removes exactly that constant, so
$$
 u+\kappa=u_0-\int_0^\ell u_0(y)\,d\nu(y).
 \tag{NPK.9}
$$
Substitution gives (NPK.7). This derivation keeps the first mean through the term $A(x)/A_\ell$, and the second through $\overline G(t)$.

For each $x$, $\int_0^\ell a(t)G(x,t)\,dt=0$. Hence the kernel also gives $z=0$ when $f$ is constant. This agrees with $N^{-1}1=1$; it does not assert that $\Pi N^{-1}=\Pi$.

## 3. The range-one estimate and the physical length factor

Fix $0<t<\ell$. Since $A$ is increasing, the two pieces of $G(\cdot,t)$ have range contained in
$$
 -\frac{A(t)}{A_\ell}
 \ \le\ G(x,t)\ \le\
 1-\frac{A(t)}{A_\ell}.
 \tag{NPK.10}
$$
This interval has length exactly one. Its $\nu$-average belongs to the same interval. Consequently
$$
 |G(x,t)-\overline G(t)|\le1
 \quad\hbox{for almost every }(x,t).
 \tag{NPK.11}
$$
No lower bound on either weighted mean is used to separate them into successive amplification factors.

The integral in (NPK.7) is with respect to ordinary $dt$, while every $L^2$ norm is normalized as in (NPK.1). Cauchy--Schwarz therefore gives
$$
 \begin{aligned}
 |z(x)|
 &\le a(x)^{-1}\int_0^\ell a(t)|f(t)|\,dt\\
 &\le \ell\,a(x)^{-1}\|a\|_2\|f\|_2,\\
 \|z\|_2
 &\le \ell\,\|a^{-1}\|_2\|a\|_2\|f\|_2 .
 \end{aligned}
 \tag{NPK.12}
$$
The factor $\ell=\pi/2$ is thus the physical circumference, not a normalized-measure factor equal to one.

Let $\operatorname{osc}p=\sup p-\inf p$. Positivity gives
$$
 \|a^{-1}\|_2\|a\|_2
 \le e^{\operatorname{osc}p}
 \le e^{2P_0}
 \le E_0^2.
 \tag{NPK.13}
$$
The middle inequality uses the complete bound $\|p\|_\infty\le P_0$. It does not use an estimate for $w$ as though it were an estimate for $p$.

Combining (NPK.4) and (NPK.12)--(NPK.13) proves the complete $L^2$ bound
$$
 \boxed{\displaystyle
 \|N^{-1}\|_{L^2\to L^2}
 \le K_{0,\mathrm{ker}}
 :=1+\frac{\pi}{2}\,W_0 E_0^2.}
 \tag{NPK.14}
$$
When $w=0$, this bound is exactly one.

The kernel produces $z\in L^2$, and the equation
$z'=f-m_f-wz$ then gives $z\in H^1$. Its zero ordinary mean yields $Ih=z$, so $Nh=f$. CN already proves uniqueness and the two-sided inverse; this argument concerns that same inverse, rather than a new formal right inverse. The actual output mean remains $\langle h\rangle=m_f$. All independent physical mean and charge rows retain their original transformed functionals.

## 4. The same negative window by the proved adjoint bootstrap

Let
$$
 C_I=\frac{\sqrt{17}}4,\qquad
 B=W_{1/3}.
 \tag{NPK.15}
$$
PIB applied to the same real coefficient $w$, with mean zero, gives
$$
 \boxed{\displaystyle
 \|N^{-1}\|_{H^{-4/3}\to H^{-4/3}}
 \le K_{-,\mathrm{ker}}
 :=1+C_I B+C_I^2 B W_0 K_{0,\mathrm{ker}}.}
 \tag{NPK.16}
$$
The first use is the actual complete $L^2$ inverse from (NPK.14). The subsequent adjoint regularity and duality are the already proved PIB construction. The two bounds therefore describe one and the same full-circle inverse.

If $K_0^{\mathrm{old}}$ and $K_-^{\mathrm{old}}$ are evaluated NW norm bounds, one may retain
$$
 \begin{aligned}
 K_0^{\mathrm{use}}&=\min\{K_0^{\mathrm{old}},K_{0,\mathrm{ker}}\},\\
 K_-^{\mathrm{new}}&=1+C_I B+C_I^2 B W_0 K_0^{\mathrm{use}},\\
 K_-^{\mathrm{use}}&=\min\{K_-^{\mathrm{old}},K_-^{\mathrm{new}}\}.
 \end{aligned}
 \tag{NPK.17}
$$
Each minimum selects between complete norm bounds for the same inverse on its stated space. It is not an entrywise minimum of operators. In a directed implementation, each complete candidate must be outwardly stored before comparison, and the selected record is retained verbatim. A tie may retain the old record. A logarithmic-only bound must not be inserted into (NPK.16) or (NPK.17) as an evaluated norm.

All four bounds also apply to the rotated $N_-^{-1}$, because rotation is unitary on both spaces. The full forward norm of $N$ is the saved NW forward norm and is not recalculated here.

## 5. Complete conditional global-sign consequences

This section preserves NW's conditional hypothesis: the complete strong remainder $E:H^{-4/3}\to L^2$ has a separately supplied bound $C_E$. Neither NW nor the present lemma supplies that complete $C_E$.

Use the already saved whole constants
$$
 F_- \ge \|N\|_{H^{-4/3}\to H^{-4/3}},\qquad
 C_{wZ}\ge\|[N,Z]\|_{H^{-4/3}\to L^2},
 \tag{NPK.18}
$$
where the exact full sign operator is
$Z=\Pi+i\Pi_+-i\Pi_-$, including its mean action. Let $Q_*$ and $A_-$ denote the saved NW positive majorants
$$
 Q_*=\frac12\{V_0W_{1/3}+|\mu|(W_{1/3}+W_0)\},
 \qquad A_-=1+\frac{V_{4/3}}4,
 \tag{NPK.19}
$$
with their original directed upper records. They are read, not recomputed.

Replacing the two inverse bounds in the already proved ordered NW formulas gives a new complete candidate
$$
 \begin{aligned}
 B_Z^{\mathrm{new}}
   &=K_0^{\mathrm{use}} C_{wZ} K_-^{\mathrm{use}} F_-,\\
 A_Z^{\mathrm{new}}
   &=B_Z^{\mathrm{new}} A_-,\\
 A_{\mathrm{Cay}}^{\mathrm{new}}
   &=K_0^{\mathrm{use}}Q_*+A_Z^{\mathrm{new}},\\
 B_{\mathrm{Cay}}^{\mathrm{new}}
   &=K_0^{\mathrm{use}}F_-+B_Z^{\mathrm{new}}.
 \end{aligned}
 \tag{NPK.20}
$$
The left inverse acts in $L^2$, the right inverse acts in $H^{-4/3}$, and the final $N$ acts on the input $H^{-4/3}$ space. No factors are commuted or omitted. These are complete affine coefficient records for the same conditional expressions as NW. The two coefficients of an affine bound are not independently minimized across unrelated affine candidates.

The complete remainder conclusion remains conditional on $C_E$. The selected physical principal inverse, the complete incoming map, the finite Schur matrix, the given-head Poisson problem, and the full return are not certified by this refinement. The separate linear-to-exponential scalar fee in NW is unchanged; no old linear remainder is renamed as a Cayley remainder.

## 6. Scope of a future scalar consumer

A consumer may read the successful NW actual receipt and its immutable source/manifest identities. The necessary old scalar fields are the complete $W_0,B,E_0,C_I$, the two evaluated inverse-window records, and, if (NPK.20) is requested, the complete saved $F_-,C_{wZ},Q_*,A_-$. All original mean and parameter scope flags remain part of the read contract.

The only new arithmetic is the kernel square/product bound (NPK.14), the adjoint product (NPK.16)--(NPK.17), and any explicitly requested complete new products in (NPK.20). There is no new Fourier solve, target enclosure, branch transport, cohomological divisor computation, or exponential evaluation. The old NW success remains immutable. A failure to improve a whole candidate is a valid complete outcome and does not imply noninvertibility.

No numerical value of (NPK.14), (NPK.16), or (NPK.20) is asserted in this analytic note.

## 7. Immutable primary evidence

All paths are relative to `topics/visible-flex-exact-nearby/`.

| Primary | Exact identity and use |
|---|---|
| CN, `results/R133-supplement-exact-full-circle-subprincipal-normalizer-and-strong-remainder-budget.md` | Blob `df47da70f4831a651f99628b914e4be99d88da12`; 15615 bytes; SHA256 `427387a2f3836d95b5f79546f0c6d41e8d6307abbb76611073d2801364fda9db`. CN.13--16 supplies the exact same inverse and its two weighted means. |
| PIB, `results/R133-supplement-complete-principal-inverse-adjoint-bootstrap-from-L2.md` | Blob `b1cb6bfa236729b8002f30097b55969cbfbab9e8`; 11316 bytes; SHA256 `2d74b71c0584cb5ec1af849b6fb5756e48da58bf313d72be62d582d557d23acb`. The negative-window estimate uses its complete adjoint bootstrap and same-inverse conclusion. |
| NW, `results/R133-supplement-complete-cohomological-normalizer-windows-and-global-sign-correction.md` | Blob `dbe97d3caa9e61b557ef22ac2b0f4606f6cfc27f`; 19754 bytes; SHA256 `1469fdd05417284743e7857aabe0324ee67ccb1b7dbaa003461364d8c9447938`. The true $w,p$, two-window convention, complete global sign and affine scope are unchanged. |
| Successful NW execution, `notes/cohomological_normalizer_windows_sign_ci/run-43775614821-1/execution.json` | Blob `1215ffc9eb7b4171b661483fea474e2b65ca2f28`; 35204 bytes; SHA256 `1e327e83dafb5d09ec98acc6ba887ae28962a7f242be7e82692a864c2f93cb0b`. Scientific child exit status zero; 20 complete gates. Its embedded canonical science has 24234 bytes and SHA256 `55019238a3b762aaeace163a81da85b3c63c3034679ca23521d3c41b28b9e7aa`. This note only identifies the already successful input; it does not rerun it. |
