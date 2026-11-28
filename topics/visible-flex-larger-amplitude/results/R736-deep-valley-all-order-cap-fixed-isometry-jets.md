# R736 — All-order cap-fixed nonlinear isometry jets on the actual deep-valley tail

2026-11-28. **Proved.** A nonzero higher-mode bending from R735 extends to a single compatible sequence of actual smooth displacement coefficients solving the nonlinear isometry equations to every finite order in amplitude on a fixed one-cap tail. Each coefficient and all its material derivatives vanish at the fixed marked cap. Each finite truncation is a genuine family on the same material tail and the same metric, with metric error $O(|\lambda|^{N+1})$ after order $N$. The result includes a forced inverse on all generated angular modes, including the mean. It does not prove that the amplitude series converges, that the error vanishes at fixed nonzero amplitude, or that the other end of the complete surface can be closed.

## 1. The sharp phase exponent of the original homogeneous line

Fix $0<u_*\le .001$ inside the pure deep tail of [R690](R690-quasimonotone-tail-and-deep-valley-input.md). Use $u=S-s$, $v=(d_0/u)^4$, $v_n=2\pi n+\pi/2$ and the exact axisymmetric base $F_*$. For fixed integer $l\ge2$, take the canonical state $Y=(y,z)$ and the half-period factorizations (3)–(8) of [R735](R735-deep-valley-cap-flat-infinitesimal-bending-lines.md). Constants may depend on the particular mode. On either half, the positive coefficient associated with the deep valley satisfies
$$
 \log\int_I\mathcal B=4\pi n+o(n).
 \tag{1}
$$
For the upper bound, on the whole cell $\sqrt v+v(1+\sin v)\le 2v_{n+1}+\sqrt{v_{n+1}}=4\pi n+O(\sqrt n+1)$. All other factors in $\mathcal B$ are bounded or polynomial in $n$. For the lower bound use a one-sided window of width $v_n^{-1/2}$ next to the adjacent sine-$+1$ endpoint (use $v_{n+1}$ for the other half). On this window $v(1+\sin v)\ge 2v_n-O(1)$, the factor $1/c$ is bounded below by a constant times $e^{2v_n-O(1)}$, and the product of the window length and $j(v)$ is bounded below by a constant times $n^{-7/4}$. This proves (1). The positive peak factors satisfy $|\log\int_I\mathcal A|=o(n)$ by R735. The half-period relative errors $O(n^{-5/2})$ preserve these logarithmic limits.

With $D_n,E_n$ from R735 (8), it follows by substitution that
$$
 \log D_n=4\pi n+o(n),\qquad |\log E_n|=o(n).
 \tag{2}
$$
The subtractive terms in $D_n$ have subexponential logarithmic size, whereas its leading term has (1). For the stable ratios in R735 (9), $E_n/D_n\le\mu_n\le E_n/(D_n-1)$; hence $\log\mu_n=-4\pi n+o(n)$. The nonzero homogeneous line constructed there satisfies
$$
 \lim_{n\to\infty}\frac{\log|y(v_n)|}{n^2}=-2\pi .
 \tag{3}
$$
The full state and every finite material derivative obey the corresponding upper bound throughout the cells: for every $\eta>0$ their norms are $O_\eta(e^{-(2\pi-\eta)n^2})$. Indeed R735's half-transfer and recovery factors are $e^{O(n)}$ and so are all fixed-order coefficients needed to differentiate the punctured ODE. Equation (3) concerns an actual nonzero component and will ensure uniqueness at larger decay rates.

## 2. Backward propagation with the correct exponential cost

Let $\mathcal T_l(v,w)$ propagate the homogeneous $l$th canonical system from $w$ back to $v\le w$. For every $\eta>0$, if $v$ lies in cell $n$ and $w$ in cell $j\ge n$ (both sufficiently late), then
$$
 \|\mathcal T_l(v,w)\|
 \le C_\eta \exp\{(2\pi+\eta)(j^2-n^2)+C_\eta(j+n+1)\}.
 \tag{4}
$$
To prove this without applying an exponential to the largest singular coefficient, change the physical state at a valley to $(y_{n+1},y_n)$. From (7) of R735 its first new coordinate is $\alpha_n[(1-P_nq_n^+)y_n+P_nz(v_n)]$. The determinant of the change is $-\alpha_nP_n$, so this change and its inverse have norm at most $e^{Cn}$ using the previously proved endpoint bounds. The single-cell companion matrix in these new coordinates and its inverse are
$$
 \begin{pmatrix}-D_i&-E_i\\1&0\end{pmatrix},\qquad
 \begin{pmatrix}0&1\\-1/E_i&-D_i/E_i\end{pmatrix}.
$$
Both norms have log at most $4\pi i+o(i)$ by (2). Summing $4\pi i+o(i)$ from $n$ to $j$, including harmless one-index endpoint shifts, yields at most $(2\pi+\eta)(j^2-n^2)+C_\eta(j+n+1)$. Only the two outer coordinate changes are applied. Every partial half transfer has determinant one and norm $\le e^{Ci}$ by R735, so its inverse has the same Euclidean operator norm. Initial/terminal fractions of cells merely add $C(j+n+1)$ to the logarithm. This proves (4).

Write $\mathcal D_\sigma$ for smooth functions of the punctured tail such that, for each finite number of physical-$u$ derivatives and every $\eta>0$, their cell suprema are $O_\eta(e^{-(\sigma-\eta)n^2})$. Finite-dimensional vectors and finite angular Fourier fields are treated coefficientwise; all their angular derivatives are included. Each component in $\mathcal D_\sigma$, $\sigma>0$, extends flat in $u$ at zero. Indeed $u^{-1}$ grows only polynomially in $n$. We have
$$
 \mathcal D_\sigma\mathcal D_\nu\subset\mathcal D_{\sigma+\nu}.
 \tag{5}
$$
Multiplication or division by any of the nonvanishing scalar factors whose derivatives (including those of the inverse) are $\le e^{C_k n}$ at each fixed order preserves these classes. This includes $a,c$ and their inverses on the open tail when used as multipliers, as well as $j=|du/dv|$; coordinate changes between $v$ and $u$ introduce only polynomial factors in $v$. Pointwise reciprocation of an arbitrary forced term is not part of this assertion.

Consider $Y_v=\mathcal H_l(v)Y+g(v)$ with the matrix of (3) in R735. If $l\ge2$ and $g\in\mathcal D_\sigma$ for $\sigma>2\pi$, define
$$
 Y(v)=-\int_v^\infty\mathcal T_l(v,w)\,g(w)\,dw .
 \tag{6}
$$
The integral is absolutely convergent. In fact choose a positive loss smaller than $(\sigma-2\pi)/4$ in (4) and in the forcing bound. The series over $j\ge n$ is dominated by a Gaussian tail: its terms are bounded by
$$
 C\exp\{-(2\pi+\epsilon)n^2
        -(\sigma-2\pi-2\epsilon)j^2+C_\epsilon(j+n+1)\}.
$$
Each $v$ cell has length $2\pi$. By taking $\epsilon$ arbitrarily small and absorbing linear terms, the sum is $O_\eta(e^{-(\sigma-\eta)n^2})$ for every $\eta>0$. Differentiate in $v$ to verify the forced equation; local uniform convergence and $\partial_v\mathcal T_l=\mathcal H_l(v)\mathcal T_l$ justify the derivative. Higher physical derivatives follow from the forced ODE, (5), and the bounds on coefficients in R735 §4. Thus $Y\in\mathcal D_\sigma$. Extend to the remaining compact interior of $0<u\le u_*$ by the regular forced ODE, keeping the same solution. This is the unique solution in $\mathcal D_\sigma$: any difference is cap-vanishing homogeneous, which R735 makes either zero or a multiple of the stable line; (3) excludes that line for $\sigma>2\pi$.

The constants and the radial start of the asymptotic estimates may vary with $l$. This construction makes no simultaneous large-frequency, radius-of-convergence, or uniform analytic norm estimate.

## 3. The forced three-component metric operator

Let a general cylindrical displacement have components $(U,V,W)$ in $(e_r,e_\theta,e_z)$, using upper-case $V$ now for the **ordinary tangential component**. Set $b=a_s$, $c=z_*'(s)>0$ on the open tail. In normalized metric entries prescribe the three first variations $(e,f,g)$ by
$$
 2(bU_s+cW_s)=e,\quad
 [b(U_\theta-V)+cW_\theta+a V_s]/a=f,\quad
 2(U+V_\theta)/a=g .
 \tag{7}
$$
These follow directly by differentiating the actual induced metric; $f$ is the single normalized off-diagonal entry. For the $l$th complex angular coefficient, $l\ge1$, let $E,F,G$ be the three right sides. Then
$$
 U=aG/2-ilV,\quad
 V_s=-(l^2-1)(b/a)V-(ilc/a)W+F-ilbG/2,\quad
 W_s=(ilb/c)V_s+[E/2-b(aG/2)_s]/c .
 \tag{8}
$$
Thus writing $V=i\widehat V$ reduces the homogeneous part exactly to R735 (2), with complex forcing allowed. Changing to its canonical coordinates multiplies forcing terms and their derivatives only by finite products of $a^{\pm l^2}$, $b$, $c^{\pm1}$, $j$, constants and derivatives already covered in §2. The explicit $V_s$ in the final (8) includes its new forcing and must be substituted in full. Consequently a prescribed finite angular mode in $\mathcal D_\sigma$ remains in that class in (6), and the recovered $U,V,W$ belong to the same class.

For $l=1$ the canonical $\mathcal B$ coefficient vanishes exactly, so the homogeneous propagator consists only of an upper triangular shear with integral of $\mathcal A$. That integral is finite to the cap since $j\,dv=|du|$ and $c$ is bounded. Formula (6) works with bounded transfer and gives the same unique flat inverse for every $\sigma>0$. For $l=0$, (7) instead gives
$$
 U=aG/2,\qquad (V/a)_s=F/a,\qquad
 W_s=[E/2-b(aG/2)_s]/c .
$$
Integrate the last two from $s=S$ with zero cap values. Their sources lie in $\mathcal D_\sigma$, so these integrals and all their derivatives do too (the physical interval to the endpoint has finite length and the Gaussian tail bounds apply). Uniqueness among flat solutions is immediate. Negative Fourier modes follow by conjugacy of the real equations. Thus all components of an arbitrary finite-mode real forcing in $\mathcal D_\sigma$, $\sigma>2\pi$, have a unique finite-mode real inverse in the same decay class. No angular mean constraint has been dropped.

## 4. Compatible formal solution of every finite nonlinear order

Fix a nonzero real $m\ge2$ parity field $Y_1$ from R735. By §1 it lies in $\mathcal D_{2\pi}$. Inductively write
$$
 F_\lambda^{[N]}=F_*+\sum_{i=1}^N\lambda^iY_i .
 \tag{9}
$$
Suppose $Y_1,\ldots,Y_{k-1}$ have been constructed with $Y_i\in\mathcal D_{2\pi i}$ and with cylindrical angular frequencies at most $im$. At amplitude order $k\ge2$ the target metric has zero new coefficient. Prescribe the right sides of (7) to be
$$
 \begin{aligned}
 e_k&=-\sum_{i+j=k,\ i,j\ge1}(Y_i)_s\cdot(Y_j)_s,\\
 f_k&=-a^{-1}\sum_{i+j=k,\ i,j\ge1}(Y_i)_s\cdot(Y_j)_\theta,\\
 g_k&=-a^{-2}\sum_{i+j=k,\ i,j\ge1}(Y_i)_\theta\cdot(Y_j)_\theta .
 \end{aligned}
 \tag{10}
$$
All sums contain the actual ordered pairs from the product expansion; there is no extra factor of two in the single mixed entry. The derivatives in (10) are *world derivatives*, hence include rotation of $e_r,e_\theta$. When expressed in that same frame the angular connection maps each individual frequency to itself, and Euclidean dot products add at most the two frequency bounds. So these sources have frequencies at most $km$, including a possible nonzero mean. By (5) they are in $\mathcal D_{2\pi k}$. Sections 2–3 solve (7) for a real $Y_k$ with frequencies at most $km$ in this same decay class. This definition is independent of any later truncation order. By (7),(10) the coefficient of $\lambda^k$ in all three normalized Gram defects vanishes identically on the whole tail. Induction proves (9) through every finite order.

For any fixed $N$, the finite sum (9) therefore has zero Gram coefficients at orders $1,\ldots,N$. Its remaining coefficients run only up to $2N$, are smooth and bounded on the fixed compact material tail, and are built from (10)'s same fields. The normalized metric error is $O_N(|\lambda|^{N+1})$ uniformly, also after any prescribed finite material differentiations with its own constant. All displacement jets at the cap are zero; the exact marked cap and its metric can be adjoined without change. The compact embedded initial cap-and-tail patch remains embedded for sufficiently small $|\lambda|$ for each fixed $N$ by openness of embeddings in $C^1$ on a compact manifold with boundary (or by the local immersion charts and a positive minimum over separated parameter pairs). Its first variation is the nonzero $Y_1$. This is the fixed actual $a,S$ and fixed tail domain for all $N$.

A smooth-amplitude realization, with no assertion of analytic convergence, is also possible. Let $\chi$ be a smooth cutoff equal to one near zero and supported in $[-1,1]$. Replace $\lambda^iY_i$ in the infinite realization by $\chi(\lambda/r_i)\lambda^iY_i$, choosing $r_i\downarrow0$ so that for every derivative of total order $\le i-1$ in amplitude and material coordinates, the maximum norm of that term is at most $2^{-i}$. Such a choice exists because a derivative involving at most $i-1$ amplitude differentiations is $O(r_i)$ or smaller; each fixed coefficient is smooth and bounded with all derivatives on the compact patch. The series converges in every fixed $C^j$ topology and realizes the coefficients of (9) exactly as its amplitude Taylor jets. It keeps the cap fixed and has metric defect flat in $\lambda$ at zero. Flatness in amplitude permits a nonzero defect at every fixed $\lambda\ne0$. Neither this realization nor the compatible formal series supplies a fixed-nonzero-amplitude refinement to zero error.

The new result is all-order solvability of the actual one-cap nonlinear jet equations, with an explicit inverse free of finite-order obstructions in every generated mode. It does not match an inner Fejér collar, resolve the finite-amplitude global isometry problem, or certify whole-surface reach. No scientific code, forced integral or numerical continuation was run for this proof.
