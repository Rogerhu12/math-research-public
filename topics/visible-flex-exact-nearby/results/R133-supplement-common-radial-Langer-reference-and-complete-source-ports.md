# R133 supplement: a common radial Langer coordinate for the full Fourier-diagonal reference

2026-11-15, visible-exact / phase_inverse.

**Proved analytic identities.** The exact physical Fourier-diagonal reference has a common principal radial coordinate for every nonzero Fourier label. Its complete frequency dependence is retained in a zero-order radial potential and a nonzero scalar gauge. The two physical source rows transform without differentiating an ordinary source. The leading normalization is tied exactly to the original closed Airy amplitude.

This result gives no new numerical domain, potential bound, selected positive Green map, strong remainder, or cutoff inverse. It applies to the same finite-background explicit family and fixed intrinsic $\eta_0$. The original independent mean and full nonradial coupling remain separate equations.

## 1. Exact reference and a removable frequency parameter

Use (R.1)--(R.29) of
[the exact physical Fourier diagonal reference](R133-supplement-exact-physical-Fourier-diagonal-radial-reference-and-complete-mean.md).
For the present degree $M\le96$ background and $|j|\ge97$, write
$n=4|j|$, $\epsilon=\operatorname{sgn}j$, and $z=j^{-2}$.
The old physical Fourier coefficients are bilinear complex-family coefficients, with $u$ odd and $v$ even.

Define finite rational functions
$$
 \begin{split}
 D_{uu}(z)&=\sum_{\ell=1}^M
       {2\ell^2z\over1-\ell^2z}\,u_\ell u_{-\ell},\\
 D_{vv}(z)&=\sum_{\ell=1}^M
       {2\ell^2z\over1-\ell^2z}\,v_\ell v_{-\ell},\\
 \alpha(z)&={b\over i}\sum_{\ell=1}^M
       {\ell\over1-\ell^2z}\,u_\ell v_{-\ell},\qquad
 a(z)=\eta+z\alpha(z),\\
 E(z)&=\langle e\rangle-2bD_{uu}(z),\qquad
 B(z)=\langle B_{\rm coef}\rangle-2bK D_{vv}(z).
 \end{split}
 \tag{C.1}
$$
Here $B_{\rm coef}=b(1-u^2-3Kv^2)$; it is not the scalar $B(z)$.
All quantities retain their physical $r,\delta$ dependence.

The paired identities (R.14) imply exactly
$$
 A_j=i\epsilon n\,a(j^{-2}),\qquad
 E_j=E(j^{-2}),\qquad B_j=B(j^{-2}).
 \tag{C.2}
$$
No large-$j$ expansion is used. The denominators are uniformly nonzero on
$|z|\le97^{-2}$, since
$|1-\ell^2z|\ge1-M^2/97^2>0$.
The functions in (C.1) are therefore holomorphic in this disk wherever the original radial coefficients are holomorphic.

The apparent division by $z$ in the principal difference is removable:
$$
 {16\over z}\{a(z)^2-\eta^2\}
       =16\{2\eta\alpha(z)+z\alpha(z)^2\}.
 \tag{C.3}
$$
The right side defines its value at $z=0$.
Thus the whole set $|j|\ge97$ can be represented by a single rational-frequency parameter on $0\le z\le97^{-2}$.
A numerical enclosure over that set would be new mathematics and is not asserted here.

This analyticity in $z$ uses the exact finite degree of the explicit background. It is not transferred to an unknown infinite-Fourier PDE correction: the omitted primitive intermediate mode must be reconsidered for that different background.

## 2. The common principal coordinate

Let $r_*$ be the same true simple root, $\rho=r_*-r$, and
$$
 K(r)=-\rho k(\rho),\qquad
 a_\infty(\rho)=\eta(\rho)\sqrt{k(\rho)},\qquad
 a_*=\eta_*\sqrt{k_*}.
$$
Choose the original branches from positive real root data.
On a star-shaped common radial germ define
$$
 \bar A(\rho)={3\over2}\int_0^1s^{1/2}a_\infty(s\rho)\,ds,
 \qquad T(r)=-\rho\,\bar A(\rho)^{2/3}.
 \tag{C.4}
$$
The integral yields
$$
 2\rho\bar A_\rho+3\bar A=3a_\infty,\qquad
 \kappa:=T_r=a_\infty\bar A^{-1/3},\qquad
 T\kappa^2=K\eta^2,\qquad
 \kappa_*=a_*^{2/3}.
 \tag{C.5}
$$
The positive branches at the root fix the analytic powers.
The construction requires the actual nonvanishing gaps for $k,\eta,\bar A$ on the claimed domain. It does not supply those gaps on an enlarged domain automatically.

This $T$ depends on the original radial principal coefficient $\eta$, not on the Fourier label or on $a(z)$.
It is the radial reference of the already used fold.
It does not replace the full nonradial fold $(T_{\rm old}(r,\phi),X_{\rm old}(r,\phi))$.

## 3. Complete trace, difference, and gauge

The diagonal coefficients obey
$$
 \begin{split}
 E(z)+B(z)&=-4b\langle S\rangle
                      -2b\{D_{uu}(z)+KD_{vv}(z)\},\\
 E(z)-B(z)&=-2b\{1+\langle u^2\rangle-K\langle v^2\rangle\}
                      -2bD_{uu}(z)+2bKD_{vv}(z).
 \end{split}
 \tag{C.6}
$$
These retain both nonradial squares and the repaired physical mean.

Assume $a(z,r)$ is nonzero on the stated parameter/radial domain, with its analytic branch fixed at $r_*$. Set
$$
 q(z)=E(z)-B(z)+{a_r(z)\over a(z)},\qquad
 \mathfrak t(z)=E(z)+B(z)+{a_r(z)\over a(z)},
$$
$$
 \Gamma(z,r)=
   \left({a(z,r)\over a(z,r_*)}\right)^{1/2}
       \exp\!\left[{1\over2}\int_{r_*}^r(E(z,t)+B(z,t))\,dt\right],
 \qquad
 G(z,r)=\sqrt{\kappa_*\over\kappa(r)}\,\Gamma(z,r).
 \tag{C.7}
$$
Then $\Gamma(r_*)=G(r_*)=1$ and
$\Gamma_r/\Gamma=\mathfrak t/2$.
The scalar $q$ here is a gauge coefficient and is not $\sqrt{-K}$.

At $z=0$ one obtains
$$
 G_\infty(r):=G(0,r)
  =(\bar A/a_*)^{1/6}(k/k_*)^{-1/4}
     \exp\!\left[-2\int_{r_*}^r b(t)\langle S(t)\rangle\,dt\right].
 \tag{C.8}
$$
To verify it, use $a(0)=\eta$, (C.5), and the first line of (C.6).
The constant factor is
$\sqrt{\kappa_*/\eta_*}=a_*^{-1/6}k_*^{1/4}$.

Equation (C.8) is precisely the radial normalization of (L.4)--(L.6) in
[the original closed leading amplitude](R133-supplement-closed-leading-Airy-amplitudes-and-exact-seam-transmission.md),
whose immutable text is Git blob becc6a83aaa4c8813dec941c747f11f49bf4aa33 (11462 bytes).
For its full fold amplitude $G_{\rm old}$ one has, before composition and on a common domain,
$$
 G_{\rm old}(r,\phi)=G_\infty(r)
            \left({A(r,\phi)\over\bar A(r)}\right)^{1/6}.
 \tag{C.9}
$$
Thus no radial mean or original $b$ contribution has been removed.

The finite-frequency gauge ratio is exactly
$$
 {G(z,r)\over G_\infty(r)}
 =
 \left\{
 {a(z,r)/\eta(r)\over a(z,r_*)/\eta_*}
 \right\}^{1/2}
 \exp\!\left[-\int_{r_*}^r
       b(t)\{D_{uu}(z,t)+K(t)D_{vv}(z,t)\}\,dt\right].
 \tag{C.10}
$$
It equals one at the root and is holomorphic in $z$ whenever the displayed gaps are paid. Since both primitive sums and $a(z)-\eta$ have a factor $z$, this ratio is $1+O(z)$ on a fixed common compact domain.
That order statement is not a numerical error bound at $j=97$.

## 4. Common-coordinate potential and exact two-row source

For $z=j^{-2}$ define
$$
 W(z)={q_r(z)\over2}-{q(z)^2\over4},
 \qquad
 \widetilde W(z)=W(z)
          -16K\{2\eta\alpha(z)+z\alpha(z)^2\},
$$
$$
 \mathcal V(z,T(r))
       ={\widetilde W(z,r)\over\kappa(r)^2}
          +{3\kappa_r(r)^2\over4\kappa(r)^4}
          -{\kappa_{rr}(r)\over2\kappa(r)^3}.
 \tag{C.11}
$$
The frequency correction in $\widetilde W$ is exactly
$-n^2K(a(z)^2-\eta^2)$ by (C.3). Every term is regular at the root when the common analytic gaps hold. There is no division by $K$ or $\rho$.

For fixed $j\ne0$, put
$$
 c(z,r)={1\over2}\left({\kappa_r\over\kappa}-q(z,r)\right),
 \quad
 U_j={h_{2,j}\over G(z,r)},\qquad
 P_j={A_jh_{1,j}+c(z,r)h_{2,j}\over\kappa(r)G(z,r)}.
 \tag{C.12}
$$
This invertible two-state transformation has inverse
$$
 h_{2,j}=G U_j,\qquad
 h_{1,j}={G\over A_j}\{\kappa P_j-cU_j\}.
 \tag{C.13}
$$
For the reference equation $h'_j=R_jh_j+g_j$, the exact transformed system is
$$
 \boxed{
 \begin{split}
 (U_j)_T&=P_j+{g_{2,j}\over\kappa G},\\
 (P_j)_T&=(n^2T-\mathcal V(z,T))U_j
             +{A_jg_{1,j}+c\,g_{2,j}\over\kappa^2G}.
 \end{split}}
 \tag{C.14}
$$
No radial derivative of $g_2$ is present. The two physical source rows remain independent.

For completeness, let $h_2=\Gamma y$ and
$p=(A_j/\Gamma)h_1-qy/2$.
The original two rows give
$$
 y_r=p+g_2/\Gamma,\qquad
 p_r=(n^2Ka^2-W)y+(A_jg_1-qg_2/2)/\Gamma.
$$
Now $U=\sqrt{\kappa/\kappa_*}\,y$ and
$P=\kappa_*^{-1/2}\{\kappa^{-1/2}p+
\kappa_rU\sqrt{\kappa_*}/(2\kappa^2)\}$.
Differentiation, (C.5), and (C.3) give (C.11)--(C.14).
The $\kappa_r$ terms in the $P$ coefficient cancel exactly.

For real parameters and increasing real $T$, an ordinary source transforms by
$\widetilde g=\kappa^{-1}\mathcal T_jg$, where $\mathcal T_j$ is the matrix in (C.12).
The exact measure is $dT=\kappa\,dr$, so a valid source estimate is
$$
 \|\widetilde g\|_{L^2_T}
 \le\sup_r\|\kappa^{-1/2}\mathcal T_j(r)\|\,
                       \|g\|_{L^2_r}.
 \tag{C.15}
$$
The displayed matrix contains the factor $A_j\sim n$.
It is not a same-order unweighted angular source bound. Its actual frequency weights must be matched to the chosen Airy frame.
The original independent $j=0$ mean is (R.12), not a singular instance of (C.12).

## 5. Root ports and the two signed branches

At the root $G=1$, and the balanced data satisfy
$$
 \begin{pmatrix}U_j\\n^{-2/3}P_j\end{pmatrix}_{r_*}
 =
 \begin{pmatrix}
 0&1\\
 i\epsilon a(z,r_*)/\kappa_*&
             n^{-2/3}c(z,r_*)/\kappa_*
 \end{pmatrix}
 \begin{pmatrix}n^{1/3}h_{1,j}\\h_{2,j}\end{pmatrix}_{r_*}.
 \tag{C.16}
$$
This identifies the same physical mixed root weights that appear in the actual root Cauchy contract. All coefficient bounds and Bessel versus pure-power conversions still require their actual fees.
No root trace approximation is made by (C.16).

Parity gives the same $a,E,B,q,\mathcal V,G$ for $j$ and $-j$.
Only the physical $A_j=i\epsilon n a$ changes sign.
The canonical equation in (C.14) consequently retains two independent columns for each absolute frequency and the original signed physical input convention.
An Airy $Ai$ column alone is not selected as the actual decaying or reflected solution.

Let $F_{j}^{\mathcal V}(T,S)$ denote the fundamental matrix of the homogeneous two rows in (C.14), with the identity initial matrix.
Then
$$
 Y_j(r,s)=
   \mathcal T_j(r)^{-1}
        F_j^{\mathcal V}(T(r),T(s))\mathcal T_j(s)
 \tag{C.17}
$$
is exactly the reference of (R.17).
Ordinary sources use (C.14); all physical trace jumps use (C.12)--(C.13) at their true one-sided endpoints.
An artificial internal cut in one original analytic piece creates no new field or source, while an original physical seam keeps its full original jump.

## 6. Full nonradial coupling stays in physical order

The common coordinate (C.4) is radial.
For the complete system, at a fixed physical $r$ the remaining coupling becomes
$$
 {d\widetilde h_j\over dr}
 =
 \kappa(r)
 \begin{pmatrix}0&1\\n^2T(r)-\mathcal V(j^{-2},T(r))&0\end{pmatrix}
          \widetilde h_j
 +\sum_m\mathcal T_j(r)
      (\Delta\mathcal G)_{jm}(r)\mathcal T_m(r)^{-1}
           \widetilde h_m+\mathcal T_j(r)g_j.
 \tag{C.18}
$$
This formula uses the actual output and input frequency matrices in the displayed order. It does not commute a frequency-dependent gauge through multiplication.

For $j$ or $m=0$, use the unchanged original mean/odd-zero convention and its exact physical row instead of (C.12).
For finite low labels use the original two-state reference unless their own elimination gap has been paid.
All rank columns and the nonmean-to-mean functional stay in (C.18).
The first-order principal drift in $\Delta\mathcal G$ is still first order; conjugation by the displayed matrices alone does not pay it.

The already certified nonradial fold may be used to build a new *known trial* only after its inverse image lies in the present radial-reference domain. The unknown ordinary source is not pulled onto a tilted radial/angle curve by this statement.
No same-order norm for a nontrivial full composition map is inferred from a small coordinate displacement.

## 7. Exact use of a deformed radial Airy basis

There is a useful purely algebraic interface to the already used two-amplitude notation.
Fix $j$, and let a radial scalar $Y_j(T)$ solve
$$
 (Y_j)_{TT}-n^2TY_j+\mathcal V_j(T)Y_j=0,
              \qquad \mathcal V_j(T)=\mathcal V(j^{-2},T).
 \tag{C.19}
$$
For either column of a complete fundamental matrix define
$$
 \mathcal U_j^{\mathcal V}(a,b)
  =e^{i\epsilon nX}\{a(T,X)Y_j(T)
                      +b(T,X)n^{-1}(Y_j)_T(T)\}.
$$
Let
$$
 K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix},
 \qquad E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$
The exact amplitude derivative rules are
$$
 \partial_T\mathcal U_j^{\mathcal V}(w)
 =\mathcal U_j^{\mathcal V}
       (w_T+nK_Tw-n^{-1}\mathcal V_j E_{12}w),
 \qquad
 \partial_X\mathcal U_j^{\mathcal V}(w)
 =\mathcal U_j^{\mathcal V}(w_X+i\epsilon nw).
 \tag{C.20}
$$
For the free choice $Y_j(T)=Ai(n^{2/3}T)$, one has
$n^{-1}(Y_j)_T=n^{-1/3}Ai'(n^{2/3}T)$, the original normalization.

The common principal operator is $\partial_T^2+T\partial_X^2$.
This sign follows directly from the original physical rows (L.2):
their scalar principal part is
$\partial_r^2+K\eta^2\partial_\phi^2$, and (C.5) gives
$K\eta^2=T\kappa^2$.
It also agrees with the exact free normalization (L.8):
$\partial_T^2 Ai(n^{2/3}T)=n^2T Ai(n^{2/3}T)$ and
$\partial_X^2 e^{i\epsilon nX}=-n^2e^{i\epsilon nX}$.
Thus the two principal terms cancel for a constant amplitude in the
free basis. A minus sign in front of $T\partial_X^2$ would instead
leave $2n^2T$ and would not be this canonical operator.

Because
$K_TE_{12}+E_{12}K_T=I$ and $E_{12}^2=0$,
$$
 \begin{split}
 (\partial_T^2+T\partial_X^2)
       \mathcal U_j^{\mathcal V}(w)
 =\mathcal U_j^{\mathcal V}\big[
 &w_{TT}+Tw_{XX}
 +n\{2K_Tw_T+(K_T)_Tw+2i\epsilon Tw_X\}\\
 &-\mathcal V_jw
 -n^{-1}E_{12}\{2\mathcal V_jw_T+(\mathcal V_j)_Tw\}\big].
 \end{split}
 \tag{C.21}
$$
Thus the radial potential is incorporated exactly, rather than estimated as an omitted constant amplitude term.

More generally, let the actual local differential expression in a specified common canonical chart be
$$
 \mathscr P_{\rm loc}=\partial_T^2+T\partial_X^2
                  +c_T\partial_T+c_X\partial_X+c_0.
$$
Relative to the free-Airy amplitude expression for this same local operator, the complete replacement is
$$
 -\mathcal V_jw
 -n^{-1}E_{12}\{2\mathcal V_jw_T+
                    (\mathcal V_j)_Tw+c_T\mathcal V_jw\}.
 \tag{C.22}
$$
The order of the scalar coefficients and matrix $E_{12}$ is fixed by (C.20). No unknown radial derivative is suppressed.

Equations (C.20)--(C.22) concern the displayed differential part.
They do not replace the original physical $I$, the projected inverse $J$, or the independent mean by local canonical operators.
Their exact full action on the new known trial and its physical seam traces must still be evaluated with the original definitions.
In particular old source *bounds* for the Ai trial cannot be reassigned to the new basis without an explicit transfer bound.

## 8. What can now be consumed without repeating old mathematics

The new potential (C.11) requires the existing physical coefficient jets through the orders displayed: $a$ through two radial derivatives, $E,B$ through one, and $\kappa$ through two.
The finite rational sums (C.1) and their radial derivatives preserve all signed Fourier products. A declared common complex domain and all reciprocal gaps must be supplied from the same original piece, full repaired mean and complete 193-mode direction.
No new high-order intrinsic target is implied by the formulas.

A minimal public consumer can therefore evaluate the genuinely new rational-frequency potential, gauge and source-port bounds from previously completed coefficient data, then enclose the new selected reference propagation.
Such a run must explicitly distinguish the original target/FFT/Taylor work, which is reused, from these new reference calculations.
All previously successful native records and all failed larger-domain gates remain unchanged.

The full nonradial principal flow, old-circle remainder, independent mean, two-sided positive graph, full corrected physical seam operator, and low/high Schur feedback remain necessary.
The reference shares the original principal radial coordinate and physical frequency $4j$; its additional radial potential can change a subprincipal return phase, which must be recomputed or transferred with a true bound before using the return arithmetic.
Nothing here identifies a formal radial correction with a realized nonlinear PDE parameter.
