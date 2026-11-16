# R133 supplement: complete dyadic Airy source blocks in the original strong window

2026-11-16, visible-exact / root.

**Proved analytic block estimate; no numerical evaluation.** The full WUA negative-side source and its true impulses admit an estimate on complete input frequency bands. The slower root-collar contribution has band power $5/3$, with every output frequency and both physical means retained. Summation over bands therefore supplies the original $H^{-4/3}$ strong window. It avoids the half-order cost of applying a column square sum to the leading oscillatory part.

The proof uses the exact compactly supported real potential, a finite Jost derivative argument, weighted Fourier row and column sums, and the actual parity inverse on fixed Sobolev windows. No diagonal-output assumption, old numerical rerun, replacement of the original primitive by $1/n$, or unproved three-phase inequality is used. The separate positive/root and waist terms remain part of the whole physical operator.

## WUB1. Fixed trial, physical spaces and finite regularity

Use precisely WUA's selected real member, continuous repaired coefficients, actual true root, natural reflected high root input, original period $\pi/2$, and physical frequencies $n=4|j|\ge388$. Its complete height, mean completion, first source and true jumps are
$$
\begin{aligned}
f_n&=P n^{7/6}{\cal U}_{n,\epsilon}^{\rm ext}
                    (w_0+n^{-1}w_1^{\rm ext}),\\
g_{2,n}&=0,\\
g_{1,n}&=J{\mathscr Q}f_n+
                 F_{{\rm mean},n}k_2-z_nR_{\rm mean},\\
j_{n,\lambda}&=(J[\partial_r f_n]_\lambda,0),\qquad
[\partial_rf_n]_\lambda
       =P n^{1/6}{\cal U}_{n,\epsilon}^{\rm ext}
                                   ([\partial_rw_1]_\lambda).
\end{aligned}
\tag{WUB.1}
$$
All projections, the independent physical mean equation, the original $I$, the full $J$, and the complete ordered ${\mathscr Q}$ remain as in WUA.34--47. The true state mean is not zero merely because $g_2=0$.

Write $\rho=r_*-r$. WUA's real fold has
$$
0<t_*\le\frac{-T}{\rho}\le t^*<\infty,\qquad
\inf_{r,\phi}\Phi_{\pm,\phi}>0,\qquad
\Phi_\pm=X\mp\frac23(-T)^{3/2}.
\tag{WUB.2}
$$
At $\rho=0$ the quotient is its actual root limit. The same compactness argument supplies positive lower bounds and finite angular jets for $X_\phi$, $T/\rho$, and the two phases. The jets are ordinary angular derivatives, uniformly on the finite original pieces and their one-sided closures. In particular
$$
\sup|\partial_\phi^kT|/\rho<\infty
$$
for each finite $k$ used below. This follows near the root from its admitted analytic germ and away from the root by division by the positive $\rho$; it does not posit one holomorphic radial extension through every seam.

The genuine reference is
$$
Y_{TT}=(n^2T-V_{\rm ext}(T,n))Y,\qquad
V_{\rm ext}=\chi_V V,
\tag{WUB.3}
$$
with exactly WUA's fixed real $C^{64}$ cutoff, equal to zero on $T\le-L$, $L=1/2000$, and equal to the original potential near zero. Its full fundamental matrix is $F_n(T)S_n$ in the free negative region, where $S_n=Z_{\rm ext}(-L)$ and $\|S_n^{\pm1}\|<6/5$. Both reference columns and the original nonzero $C_n,\beta_n$ remain. This matrix acts on the reference input, not on a substituted physical port.

The retained WUA scalar expansion is the exact finite identity
$$
{\mathscr Q}f_n=n^{1/6}P{\cal U}^{\rm ext}_{n,\epsilon}(r_n)
                   +{\cal E}_{6,n},\qquad
\|{\cal E}_{6,n}(r)\|_2
 \le C_6 n^{-17/6}(1+t_*n^{2/3}\rho)^{-1/4}.
\tag{WUB.4}
$$
The complete amplitudes $r_n$ have uniform finite angular jets. For this proof append four angular differentiations to their explicit finite $N=6$ product/primitive algorithm. All means and exact terminal $I/J$ factors stay in ${\cal E}_{6,n}$, as in WUA.31--37; they are not treated as local amplitudes.

The resulting list uses only finitely many derivatives of the actual coefficients, $w_0,w_1$, and $V_{\rm ext}$. The six inverse-power steps, differential order two and four appended angular derivatives are within the fixed $C^{64}$ qualification. The profile argument below requires five Jost derivatives because $Y_T/n$ contains the first derivative of a Jost amplitude. There is no all-$s$ claim based on that cutoff. No derivative is taken of an interval upper bound.

For $N=388\,2^\ell$, $\ell=0,1,\ldots$, let $\Delta_N$ be the original root input projection onto
$$
                         N\le4|j|<2N.
\tag{WUB.5}
$$
These projections are orthogonal in the original natural input norm, before a selected chart or $N_i$ is applied. Actual reflection and reality constraints are retained. A full signed or two-reference estimate can be restricted through its genuine isometric input realization; all fixed reference component factors are included in the constants.

## WUB2. An exact finite Jost derivative lemma

This elementary lemma supplies an oscillatory representation with controlled angular amplitudes. Fix $t_0>0$. Suppose $q$ has the finite derivative bounds
$$
       |q^{(k)}(t)|\le Q_k t^{-k-2}\quad(t\ge t_0),
                    \qquad 0\le k\le K,
\tag{WUB.6}
$$
where the $Q_k$ are nonnegative finite constants. The forward oscillatory solution of
$$
                         z''+(1+q)z=0
$$
is defined by $z_+(t)=e^{it}a_+(t)$, with $a_+\to1$ at infinity, through
$$
a_+(t)=1+\frac1{2i}\int_t^\infty
                (1-e^{2i(s-t)})q(s)a_+(s)\,ds.
\tag{WUB.7}
$$
Iteration of this backward Volterra equation converges: its $m$-th iterated absolute integral is bounded by
$(\int_t^\infty|q|)^m/m!$. Therefore
$$
                 |a_+(t)|\le A:=e^{Q_0/t_0}.
\tag{WUB.8}
$$
The same construction with the opposite signs gives $z_-=e^{-it}a_-$. For real $q$ the two solutions are complex conjugates. Their constant Wronskian, in the order $(z_+,z_-)$, is $-2i$, as follows by taking the limit at infinity. Thus they form a basis on the entire admitted interval.

Differentiation of (WUB.7), followed where necessary by integration in the $s$ variable, gives the exact identities
$$
a_+^{(k)}(t)=\int_t^\infty e^{2i(s-t)}
                         (qa_+)^{(k-1)}(s)\,ds,\qquad k\ge1,
\tag{WUB.9}
$$
and
$$
a_+^{(k)}(t)
 =-\frac{(qa_+)^{(k-1)}(t)}{2i}
  -\frac1{2i}\int_t^\infty e^{2i(s-t)}
                              (qa_+)^{(k)}(s)\,ds.
\tag{WUB.10}
$$
For a finite $K$, the required differentiability and boundary limits first follow inductively from (WUB.7) and
$a_+''+2ia_+'+qa_+=0$. They give the coarse finite derivative bounds $O(t^{-1})$; hence the products in (WUB.9)--(WUB.10) are integrable and the boundary term at infinity vanishes. The sharper induction below is consequently legitimate. It is not a differentiation of a pointwise error estimate.

In the last integrand of (WUB.10), isolate the term $q\,a_+^{(k)}$. Every other factor is controlled by lower derivatives. Backward Gronwall then proves
$$
                     |a_\pm^{(k)}(t)|\le C_k t^{-k-1},
                              \quad 1\le k\le K.
\tag{WUB.11}
$$
Here is a completely finite positive recursion for these constants. Empty sums are zero:
$$
\begin{aligned}
C_k=\frac{e^{Q_0/(2t_0)}}2\Bigg[
&A Q_{k-1}
 +\frac1{t_0}\sum_{l=0}^{k-2}
            {k-1\choose l}Q_l C_{k-1-l}
 +\frac{A Q_k}{k+1}\\
&+\frac1{(k+2)t_0}\sum_{l=1}^{k-1}
                  {k\choose l}Q_l C_{k-l}\Bigg].
\end{aligned}
\tag{WUB.12}
$$
Indeed the boundary term with $a_+$ undifferentiated is
$A Q_{k-1}t^{-k-1}$. Each other boundary product has one extra $t^{-1}$. In the integrated lower terms, $q^{(k)}a_+$ gives $A Q_k t^{-k-1}/(k+1)$; every other term has one extra $t^{-1}/(k+2)$. The retained highest derivative has kernel $|q|/2$, giving the exponential displayed in (WUB.12). The proof for $a_-$ is identical in absolute value.

In particular all $(t\partial_t)^m a_\pm$ for $m\le K$ are bounded, and all $(t\partial_t)^m a_\pm'$ for $m+1\le K$ are bounded on $t\ge t_0$. Only the stated finite list is used.

## WUB3. Apply the lemma to the complete genuine reference

Put $s=-T>0$, $t=(2/3)n s^{3/2}$, and $z=s^{1/4}Y(-s)$. Direct differentiation of (WUB.3) gives
$$
z_{tt}+(1+q_n(t))z=0,\qquad
q_n(t)=\frac5{36t^2}+
                    \frac{V_{\rm ext}(-s,n)}{n^2s}.
\tag{WUB.13}
$$
There is no new scalar approximation. At fixed input $n$,
$t\partial_t=(2/3)s\partial_s$, and
$$
t^2q_n(t)=\frac5{36}+\frac49s^2V_{\rm ext}(-s,n).
\tag{WUB.14}
$$
Thus (WUB.6) holds uniformly in every admitted input frequency, with the explicit finite recipe
$$
Q_k=
 \sup_{s>0,\ n\ge388}
 \left|
 \prod_{h=0}^{k-1}
       \left(\frac23s\partial_s-2-h\right)
 \left(\frac5{36}+\frac49s^2V_{\rm ext}(-s,n)\right)
 \right| .
\tag{WUB.15}
$$
The empty product defines $Q_0$. These suprema are finite: outside $s\le L$ the potential term is exactly zero; inside it, every derivative includes the actual cutoff derivatives and the old potential jets on their admitted domain. Only $k\le5$ is required for the four angular derivative estimate below. The original $j^{-2}$ dependence stays in its qualified compact range. No derivative in $j$ is needed.

Take $t_0=1$. In the free region the Jost solutions have the exact Airy normalization fixed at $s=\infty$. In particular, the $+$ solution equals the continuation of
$$
\sqrt\pi\,n^{1/6}e^{-i\pi/4}s^{1/4}
       \{\operatorname{Bi}(-n^{2/3}s)+i\operatorname{Ai}(-n^{2/3}s)\};
$$
the minus solution is its conjugate. This normalization follows from the real leading Airy limits
[DLMF 9.7.9--12](https://dlmf.nist.gov/9.7).
It only fixes the constant basis at infinity. Its derivatives are controlled by (WUB.7)--(WUB.12), rather than by differentiating an asymptotic remainder.

Consequently each actual genuine column is, for $t\ge1$, a fixed input-frequency linear combination of the two exact profiles
$$
 y_\pm(s)=\frac{n^{-1/6}s^{-1/4}}{\sqrt\pi}
             e^{\pm i(t+\pi/4)}a_\pm(t,n).
\tag{WUB.16}
$$
The coefficients are the original complete $S_n$ combined with the fixed Ai/Bi-to-Jost change of basis. They are independent of $r,\phi$, uniformly bounded, and retain the original root shear. They are not commuted through a selected input map.

The second profile is also exact:
$$
 \frac{\partial_T y_\pm}{n}
 =\frac{n^{-1/6}s^{-1/4}}{\sqrt\pi}
       e^{\pm i(t+\pi/4)}\sqrt{s}
       \left[\left(\frac1{6t}\mp i\right)a_\pm-a_\pm'\right].
\tag{WUB.17}
$$
This explicitly explains the fifth Jost derivative requirement. Because $s/\rho$ and its angular jets have positive bounded qualifications, derivatives of $\log s$ are bounded; hence
$$
\partial_\phi t=t\,\frac32\,\partial_\phi\log s
$$
and its finite higher chain rules turn (WUB.11) into uniform angular amplitude bounds.

In the full expression $e^{i\epsilon nX}(aY+bY_T/n)$, the two exponentials in (WUB.16)--(WUB.17) are precisely the two original true phases, with the appropriate sign relabelling. The remaining amplitude, after factoring $n^{-1/6}\rho^{-1/4}$, has uniformly bounded angular derivatives through order four whenever $(a,b)$ does. The input-dependent $S_n$, $V_{\rm ext}$ and finite powers of $n^{-1}$ do not need input-frequency derivatives. No third phase occurs.

## WUB4. The root region and a uniform complete profile block

Choose a fixed $R_0>0$ such that
$$
             \frac23t_*^{3/2}R_0^{3/2}\ge1.
$$
This is an unevaluated positive choice. For a band $n\in[N,2N)$, use a fixed scalar partition in $\rho N^{2/3}/R_0$, with a near part supported on $\rho\le2R_0N^{-2/3}$ and a far part supported on $\rho\ge R_0N^{-2/3}$. It is used only to estimate the already exact source. The partition is radial, has no angular derivatives, and is never differentiated radially or inserted into the trial equation. Therefore it creates no cutoff source or seam.

On the far part, $t\ge1$, so WUB3 supplies the two-phase representation and uniform angular amplitude derivatives. On the near part, the scaled variable $n^{2/3}T$ stays in a fixed compact interval. WUA.27 bounds both full profiles there. Differentiating their exact scalar ODE gives finite scaled derivatives
$$
 |\partial_T^kY|\le C_k^{\rm near}N^{2k/3}
$$
for the required finite list, with the companion derivative row in its actual normalization. Every $\partial_\phi^kT$ is $O(\rho)$, so the chain rule yields uniform angular derivatives on this near region. This uses the exact ODE, the actual $V_{\rm ext}$ jets and the complete profile initial normalization. It differentiates no old numerical upper.

The near expression has the single phase $X$, a true uniformly nondegenerate real circle diffeomorphism. The far expression has the two phases $\Phi_\pm$, also uniformly nondegenerate. All three are actual frequency-independent maps for each $r$.

For reference, the full-output weighted Fourier estimate is elementary. Suppose
$$
{\cal F}_N x=\sum_{N\le4|j|<2N}x_j a_j(\phi)e^{i4j\Phi(\phi)}
$$
and the $a_j\circ\Phi^{-1}$ have uniform angular derivatives through order four. After the true angle change, its complete Fourier matrix has entries
$\widehat{a_j\circ\Phi^{-1}}(k-j)$. At nonzero $\ell$, four integrations by parts bound their magnitude by $D_4/(4|\ell|)^4$, while the zero coefficient is bounded by $D_0$.

For $0\le d\le2$, the elementary Bessel weight inequality gives
$$
 \Lambda_k^{-d}\le
     2^{d/2}N^{-d}\Lambda_{k-j}^{d}
       \quad\hbox{when }4|j|\ge N.
\tag{WUB.18}
$$
Both weighted row and column sums are therefore bounded by
$$
 2^{d/2}N^{-d}
 \left[D_0+D_4\sum_{\ell\ne0}
                 \frac{\Lambda_\ell^d}{(4|\ell|)^4}\right].
\tag{WUB.19}
$$
The series converges for these $d$. It includes $k=0$ and all low outputs; no diagonal support has been assumed. Schur's inequality gives the complete operator estimate.

Returning through $\Phi$ costs its actual $H^{-d}$ composition bound. Such a finite bound follows from the positive derivative lower and the finite jets: the adjoint is the inverse composition times its Jacobian, its $L^2,H^2$ bounds follow by the product and chain rules, and duality/interpolation supplies $H^{-d}$, $0\le d\le2$. All these maps are on the full circle before the genuine parity projections.

Combining the near and far representations, and absorbing their fixed overlap constants, proves the following uniform block statement. For any admitted family of amplitudes $v_n(r,\phi)$ with uniformly bounded angular derivatives through order four,
$$
 \left\|\sum_{N\le n_j<2N}x_j
             P{\cal U}^{\rm ext}_{n_j,\epsilon_j}(v_{n_j})(r)
                  \right\|_{H^{-d}}
 \le C_{v,d}N^{-d}b_N(\rho)\|x\|_{\ell^2},
 \qquad 0\le d\le2,
\tag{WUB.20}
$$
where
$$
                 b_N(\rho)=(1+N^{2/3}\rho)^{-1/4}.
\tag{WUB.21}
$$
Indeed $b_N$ is bounded below by a fixed positive constant in the near support, and in the far support it is comparable to $N^{-1/6}\rho^{-1/4}$. The constants retain $t_*,t^*,R_0$, every phase and amplitude derivative, both reference components and the original reflection realization. They are finite symbolic recipes, not evaluated small numbers.

This is an operator estimate for the actual complete band. It does not follow from declaring the individual column profiles orthogonal.

## WUB5. The genuine angular inverse in the required negative windows

The inverse used here is exactly the original angular
$J=A^{-1}:H^s_{{\rm even},0}\to H^{s+1}_{\rm odd}$.
It is not a stable root-trace inverse and not a new full-signed inverse.

JI supplies its explicit full real strict-interval formula with a uniformly positive scalar denominator and the complete smooth coefficient multipliers. The original local angular inverse supplies the overlapping root neighbourhood. Uniqueness identifies them where both are defined. Finite product/chain estimates for their actual coefficients give uniform finite constants for the following three maps on the complete negative radial interval:
$$
\begin{aligned}
 J &:H^{-5/3}_{{\rm even},0}\longrightarrow H^{-2/3}_{\rm odd},\\
 J &:H^{-2}_{{\rm even},0}\longrightarrow H^{-1}_{\rm odd},\\
 J &:L^2_{{\rm even},0}\longrightarrow H^1_{\rm odd}.
\end{aligned}
\tag{WUB.22}
$$
Their constants are separate positive recipes. No previously saved $J_0$ number is silently reused in a negative window.

For clarity, the strict formula is a finite composition of the same old primitive, smooth multipliers and complete smooth scalar functionals, divided by JI's nonzero scalar denominator. The primitive gains one angular derivative on every fixed nonmean Sobolev space. A smooth multiplier is bounded in each of the finite windows in (WUB.22), and the finite scalar rows have the corresponding dual regularity. The compact radial domain, its finite pieces and the already positive denominator give uniform constants. The same fixed-window elliptic identity or the qualified local formula gives the root bounds. This establishes (WUB.22) without a new Fourier inverse or a numerical solve.

Since $J$ has odd range, the actual primitive additionally gives
$$
       IJ:H^{-2}_{{\rm even},0}\longrightarrow L^2_{{\rm even},0}
                  \quad\hbox{bounded uniformly in }r.
\tag{WUB.23}
$$
The $I:H^{-1}_{\rm odd}\to L^2$ factor has its true full-frequency bound, including the lowest nonzero frequency. It is not replaced by an input-frequency $1/N$.

The powers $N^{-5/3}$ and $N^{-2}$ used below come instead from the full-output estimate (WUB.20) before applying these fixed bounded maps. Thus the argument charges low-frequency leakage as well as the main oscillation.

## WUB6. Complete ordinary sources, including the terminal and mean pieces

Let $x$ be supported in one band (WUB.5). Apply (WUB.20) with $d=5/3$ to the retained amplitude $r_n$ in (WUB.4). The input multiplier $n^{1/6}$ is at most $(2N)^{1/6}$ on that band. Then (WUB.22) yields
$$
 \left\|\sum_jx_j J\big[n_j^{1/6}
             P{\cal U}^{\rm ext}_{n_j,\epsilon_j}(r_{n_j})\big](r)
                                      \right\|_{H^{-2/3}}
          \le A_{\rm col}N^{-3/2}b_N(\rho)\|x\|_2 .
\tag{WUB.24}
$$
All amplitudes in the complete ordered residual are included. The full $J$, including its old means and nonlocal terms, acts after this complete estimate.

There are at most $N$ scalar signed Fourier slots in this band. The actual reflected realization or fixed number of retained reference columns contributes its stated fixed factor. Applying a column square bound only to the exact terminal remainder in (WUB.4) gives
$$
 \left\|\sum_jx_j{\cal E}_{6,n_j}(r)\right\|_2
       \le A_6 N^{-7/3}b_N(\rho)\|x\|_2.
\tag{WUB.25}
$$
This is the explicit half-order cost for that already faster remainder. The profile factor with $t_*$ in (WUB.4) is comparable to (WUB.21), with its complete positive comparison constant retained in $A_6$. A terminal $I$ or $J$ inside ${\cal E}_{6,n}$ receives no further unproved $1/N$.

WUA's complete physical mean estimate is
$$
 |F_{{\rm mean},n}|+|z_n|\le A_m n^{-23/6}.
$$
Multiplying by the actual $k_2,R_{\rm mean}$, and retaining their one-sided angular norms, gives the band estimate
$$
 \left\|\sum_jx_j(F_{{\rm mean},n_j}k_2
                    -z_{n_j}R_{\rm mean})(r)\right\|_{H^{-2/3}}
               \le A_M N^{-10/3}\|x\|_2 .
\tag{WUB.26}
$$
The mean equation, its integrating factor, the complete adjoint tests and the root value have not been discarded. The square bound in (WUB.26) concerns only this entire faster mean contribution.

Now use precisely WUC's original collar
$[c_{\rm PW},r_*]$, $c_{\rm PW}=r_+-1/200$, of length
$\ell_{\rm col}=r_*-c_{\rm PW}$. In ordinary physical $dr=-d\rho$,
$$
 \left(\int_0^{\ell_{\rm col}}b_N(\rho)^2\,d\rho\right)^{1/2}
                \le\sqrt2\,\ell_{\rm col}^{1/4}N^{-1/6}.
\tag{WUB.27}
$$
The inequality is the direct integral of the integrable majorant
$N^{-1/3}\rho^{-1/2}$. No singular value at $\rho=0$ is substituted pointwise.

Combining (WUB.24)--(WUB.27), with the actual $J:L^2\to H^1$ bound on (WUB.25), proves the **complete band source estimate**
$$
 \|g_1\Delta_N:
       L^2_{\rm nat}\to L^2([c_{\rm PW},r_*];H^{-2/3})\|
                   \le C_{\rm col}^{\rm block}N^{-5/3}.
\tag{WUB.28}
$$
A positive recipe for $C_{\rm col}^{\rm block}$ retains separately the leading $N^{-5/3}$, terminal $N^{-5/2}$, and mean $N^{-10/3}$ contributions just obtained, then uses $N\ge388$ only to place them under the displayed power. Their actual constants are not evaluated here. The second ordinary source is exactly zero, so this is a member of PW's complete $H^{-2/3}\oplus\mathbb C$ pair-source space. It does not make the second physical state zero.

For the strict interval $[0,c_{\rm PW}]$, apply (WUB.20) with $d=2$, then the actual $IJ$ in (WUB.23). The retained source obeys
$$
 \|I J[n^{1/6}P{\cal U}^{\rm ext}(r_n)]\Delta_N\|_{L^2_\phi}
                  \le A_{\rm st}N^{-11/6}b_N(\rho).
\tag{WUB.29}
$$
Here $\rho\ge\ell_{\rm col}>0$, so the true ordinary $L^1_r$ norm has band power $N^{-2}$. The complete terminal part in (WUB.25) has power at least $N^{-5/2}$ after this strict profile bound; the mean part in (WUB.26) is faster as well. Their true bounded operator factors stay in the positive constant. Therefore
$$
 \|Ig_1\Delta_N:
       L^2_{\rm nat}\to L^1([0,c_{\rm PW}];L^2_\phi)\|
                 \le C_{\rm st,vol}^{\rm block}N^{-2}.
\tag{WUB.30}
$$
This is ordinary $dr$, with the same full source as (WUB.28) restricted to the other interval. It uses no unproved radial smoothing or output orthogonality.

## WUB7. Every true seam and the unchanged complete receiver

At each actual interior seam, WUA.46--47 proves the exact jump in (WUB.1). The coefficient
$[\partial_rw_1]_\lambda$ has finite actual angular jets on its two sides. Its radial forcing may jump; its value and the physical mean remain continuous. The cutoff potential and the estimation partition from WUB4 create no state jump.

For a collar seam, its distance $\rho_\lambda>0$ from the true root is fixed. Use (WUB.20) with $d=5/3$, followed by (WUB.22), to obtain
$$
 \|j_{1,\lambda}\Delta_N:L^2_{\rm nat}\to H^{-2/3}\|
 \le C_\lambda N^{-3/2}b_N(\rho_\lambda)
 \le C_\lambda\rho_\lambda^{-1/4}N^{-5/3}.
\tag{WUB.31}
$$
The second jump component is exactly zero by the true state transmission identity. All its full mixed $H^{-2/3}\oplus H^{-1}$ coordinates are thus paid. There is no missing mean input.

For a strict seam, (WUB.20) with $d=2$ and (WUB.23) similarly give
$$
             \|Ij_{1,\lambda}\Delta_N\|_{L^2\to L^2}
                           \le C'_\lambda N^{-2}.
\tag{WUB.32}
$$
The finite sums of these constants are retained. This includes the complete original 3070-interface list and any other true collar interface required by the original pieces. An artificial subdivision contributes zero only when the actual value identity proves it. A true seam at the chosen split is assigned once to an admitted impulse port. No jump receives a radial-length factor.

A discrepancy at $r_*$ itself is the separate positive/root trace in WUC.21. It is not assigned a positive $\rho_\lambda$, included in (WUB.31), or set to zero.

Use the same complete old PW/SP receiving constants $C_O,C_R,C_1$ in their original input spaces, exactly as WUC.4 and WUC.18. They already include the entire singular root conversion, strict propagation, two evolving mean coordinates, radial density factors and endpoint units. The cut is still $c_{\rm PW}$, not the newer strict cut or the canonical potential cutoff.

Let ${\cal T}_{\rm neg}$ be the received waist state from the complete negative ordinary source and all its true jumps with zero root input. Set
$$
 A=C_O C_{\rm col}^{\rm block}
                 +C_R C_{\rm col,j}^{\rm block},\qquad
 B=C_1(C_{\rm st,vol}^{\rm block}
                    +C_{\rm st,j}^{\rm block}).
\tag{WUB.33}
$$
The complete operator estimate is
$$
 \boxed{\quad
 \|{\cal T}_{\rm neg}\Delta_N:
                 L^2_{\rm nat}\to{\cal Y}_0\|
                   \le A N^{-5/3}+B N^{-2}.
 \quad}
\tag{WUB.34}
$$
Here ${\cal Y}_0$ is the original primitive-density pair and both full stored means at the waist. The receiving evolution may mix angular frequencies and may generate a nonzero mean. Its full norm has been applied only after the source and impulse maps were proved in the exact admitted spaces.

If WUR's correlated first-row route is substituted for the strict term, it is a separately qualified whole observation of the same source, with its complete $O_0m_{11}$ fee and its actual target units. Formula (WUB.34) uses the original full-state $C_1$ route and needs no new evaluation of that alternative product.

## WUB8. Sum the actual bands and restore the original strong window

For $0\le\sigma<5/3$, the original band norm obeys
$$
\|\Delta_Nx\|_2\le3^\sigma N^\sigma
                       \|\Delta_Nx\|_{H^{-\sigma}},
$$
because $(1+n^2)^{1/2}\le3N$ on $N\le n<2N$, $N\ge388$. Apply the triangle inequality in the full output space, then Cauchy--Schwarz only over the **orthogonal input bands**. Define the unevaluated positive expression
$$
 {\cal S}_a(N_0)
     =\left(\sum_{\ell=0}^\infty
                       (N_0\,2^\ell)^{-2a}\right)^{1/2}
     =\frac{N_0^{-a}}{\sqrt{1-2^{-2a}}},\qquad a>0.
\tag{WUB.35}
$$
It follows that
$$
 \boxed{\quad
 \|{\cal T}_{\rm neg}:H^{-\sigma}_{\rm nat,97}\to{\cal Y}_0\|
 \le3^\sigma\left[
       A{\cal S}_{5/3-\sigma}(388)
        +B{\cal S}_{2-\sigma}(388)\right],
                 \qquad 0\le\sigma<5/3.
 \quad}
\tag{WUB.36}
$$
The actual extension is unique from the smooth input core. No orthogonality of output waves, phases or propagated bands is assumed.

In particular $\sigma=4/3$ is admitted, with the two positive summability gaps $1/3$ and $2/3$. This is a new complete negative-source qualification in the original strong window. WUC's earlier strict column criterion $1<\sigma<7/6$ remains correct for its own method; its threshold was not a claim that the actual source map failed at a larger exponent.

The same formula starting at a higher original band gives its explicit source tail. It does not by itself provide a final physical high-block inverse. The final selected graph uses its actual input maps and complete error, not just this source subtotal.

## WUB9. The same whole operator and the numerical boundary

WUC.21 remains the exact decomposition
$$
 \mathfrak D_0(\Psi_A-V_{\rm old})(0)
 =\mathfrak D_0{\cal E}_h(0,r_*)
                   \{e^+(r_*)-P_Fh^G(r_*)\}
       +{\cal T}_{\rm neg}
       +{\cal E}_{\rm waist}.
\tag{WUB.37}
$$
WES.38--39 supplies the complete last map on $H^{-4/3}$, including the nonzero root shear/scattering matrix, the second-order waist normalizer, the exact old primitive ranks and the physical mean endpoint. The first map retains the original complete positive correction and finite-root-complement products; an already received product is not multiplied by $C_R$ again.

The new result (WUB.36) changes only the middle qualification. Every actual left waist observation, the true right $N_i$, the full leading map, the complete algebraic coefficient difference and each physical mean/metric/head equation retain their original places. An identity changing the split must be proved before comparing whole bounds. No term is removed by subtracting two norm uppers.

A numerical contract based on this theorem would require complete new finite budgets for: the $Q_k$ through order five and recursion (WUB.12); the fold/phase gaps and angular jets; all retained $r_n$ and true-jump amplitude jets; the actual negative-window $J,IJ$ norms; the complete WUA terminal and mean tests; and the full old receiver/coordinate factors in (WUB.33)--(WUB.37). The constants in this proof are unevaluated. In particular no exponential or new scalar product has been computed locally.

The theorem proves a genuine all-output band estimate and the resulting $H^{-4/3}$ source map. It does not certify a useful numerical cutoff, invert the actual finite physical square, eliminate an unknown infinite radial head, prove a nonzero metric Schur, or construct the nonlinear fixed-metric family.

## WUB10. Immutable evidence

All repository paths below are relative to the topic results directory. The already successful mathematics is read-only.

| Primary and exact use | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WUA, full real trial, exact finite $N=6$ scalar source, complete mean and seams | 7b89251dcd51e8cb78fd3e8e42905114ef982ebf | 40111 | 9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad |
| JI, the actual full real angular inverse and overlap uniqueness | 839fa641fe9ce3758ee69cfe3cb4299f59a3a239 | 11769 | 01e4a33be5d895ccbfc949310a86bf561c8dccdfe1c1eff973fa1298fcc91cf1 |
| WUR, complete parity/mean source identities and actual strict receiving units | a1a7520488196fc8edefe6649a2e82661bedf4ca | 23938 | 948ad1928003feae6ee4a183b7d4136b673000cee6507100a6bbca917947bde1 |
| WUC, unchanged PW cut, complete source/impulse spaces and original receiving constants | 0ab392b063763cf2abe31d20b7879d670b0efc6c | 21833 | 6ced5a9365db6823d4dd6044be69b177cba126b6cefc7f2a3e1165cc897f0f58 |
| WES, same old-target complete waist comparison | 02ca30d6e063e9bdfd158d8401361db74e92ce77 | 31293 | 8aa7eb5d210ed73b3e3e2b3c166432292725a603c23dda4d4d9c0a8292d72b00 |
| PW, complete original negative receiving theorem and both mean units | d22fc84975785bfdf0e0ba91b100d53c9d4c32a3 | 16459 | 246c81ac387392c75a3267faaa934a7f0a4b978fdad8b8ac7cbbd4bd5c413562 |
| SP actual, the unchanged complete 20-gate receiver | 9998526894560d41523454334a444f062fe371a4 | 35259 | a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12 |
| WGT, distinction between whole-column and whole-band high-block criteria | 2827aec2afb53d395218c7d6dbf488083eb66df4 | 20433 | 231ff8b11d405591cdd23c56831a33796a61976cb813165787b6212dd2511d08 |

The exact scalar basis normalization in WUB3 uses only the real leading limits in the official [DLMF Airy section 9.7](https://dlmf.nist.gov/9.7), equations 9.7.9--12. The new finite derivative estimates are proved in WUB2, so no external unquoted Jost theorem or asymptotic derivative remainder is required.

WUA is [the global genuine trial](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md); WUC is [the original root-window reception](R133-supplement-root-window-interpolation-and-complete-negative-source-reception.md); WES is [the complete waist comparison](R133-supplement-selected-free-waist-exact-scattering-and-complete-endpoint-comparison.md). All original parameter, cutoff, mean and input conventions in those proofs remain attached.
