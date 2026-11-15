# R133 supplement: exact selected-source frequency bands and complete known high forcing

2026-11-15, tail_connector.

**Proved analytic consequence of the same RF/R objects and completed source receipts.** The continuously repaired centre has quarter-index degree32, and the complete physical response direction has degree96. The selected residual has degree at most288 in the original moving angle. Its known high forcing can be bounded without the background residual term. Above index160 there is an additional exact quadratic cancellation; above index224 only a cubic state term remains. No new numerical evaluation or true-solution assertion is made here, and the frozen CR restriction consumer is unchanged.

## RH1. Same objects, original moving angle and all means

Use [RF](R133-supplement-complete-core-residual-reuse-for-the-selected-centre.md) and [R.1--R.5](R133-supplement-selected-centre-complete-residual-and-collar-source-bounds.md):
$$
 Q_\delta=Q_0+\delta Z,\qquad
 \nu_\delta=\nu_0+\delta,\qquad
 \eta_{\mathrm{physical}}=\eta_0,\qquad
 |\delta|\le d=10^{-10},\qquad I_-=[0,L],\quad L=9/10 .
 \tag{RH.1}
$$
The exact centre and direction definitions are
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
and
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
The direction is in its original physical moving units: it is not multiplied by the centre amplitude again.

All Fourier projections below act in the fixed original moving coordinate $\phi$, with frequencies $4j$. Let
$$
 \Pi_{\le J}f=\sum_{|j|\le J}\widehat f_j e^{4ij\phi},
 \qquad H_J=1-\Pi_{\le J}.
 \tag{RH.2}
$$
They act on both components and respect the original odd/even reflection class. Thus $\Pi_{\le96}$ has96 real odd coordinates and97 real even coordinates, including the genuine even mean. It is the original193-dimensional low space. It is not a projection in the physical curvature angle $\theta$ or the true phase angle.

Write $\deg_\phi f\le J$ when $H_Jf=0$. A radial scalar or an angular mean has degree zero. Angular or piecewise radial differentiation does not increase the degree. The complete primitive $I=\partial_\phi^{-1}P_{\ne0}$ also preserves the support bound. Its zero mean convention is retained throughout.

The original exact centre repair [V.1--V.5](R133-supplement-exact-continuous-repair-of-final-centre.md) uses the same65 real coordinates, hence
$$
 \deg_\phi Q_0\le32.
$$
The original direction formula [Q.1--Q.3](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md) uses all193 coordinates:
$$
 Z=\left(\sum_{j=1}^{96}\xi_j(r)\sin4j\phi,\ 
                 \zeta_0(r)+\sum_{j=1}^{96}\zeta_j(r)\cos4j\phi\right),
 \qquad \deg_\phi Z\le96 .
 \tag{RH.3}
$$
Its exact interface repair adds only a constant-in-$r$ vector in these same193 slots. The mean $\zeta_0$ is retained. Consequently $Q_0,Z,Q_\delta$ are exactly continuous across their original radial interfaces. Their distributional first radial derivatives have no value-jump masses, although their ordinary one-sided radial derivatives can differ.

The true radial reference in $Q_0$ is $s_{\eta_0,\nu_0}$, with its full mean. It remains part of the fixed $Q_0$ in (RH.1). This note does not reset the state to $s_{\eta_0,\nu_\delta}$ while holding its finite normalized vector unchanged.

## RH2. Exact support in the complete moving equation

The full field is R.2:
$$
 \mathcal F(Q,\nu)
 =-\beta I(S)Q_\phi+GmJ(K)Q_\phi
                   +\beta(-u,v)-\beta SQ,\qquad
 S=u^2+Kv^2,\quad m=\langle v\rangle,
 \quad J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.
 \tag{RH.4}
$$
Every intrinsic coefficient is radial. Its dependence on $\nu$ does not introduce angular frequencies. If $\deg_\phi Q\le M$, then $S$ and $I(S)$ have degree at most $2M$, while the drift and local cubic products have degree at most $3M$. The mean term $GmJ(K)Q_\phi$ has degree at most $M$, not$2M$.

For
$$
 f_\delta=(Q_\delta)_r-\mathcal F(Q_\delta,\nu_\delta),
 \qquad
 s_0=\mathcal F_\nu(Q_0,\nu_0)
                   -(\partial_r-A_0)Z,\quad A_0=D_Q\mathcal F(Q_0,\nu_0),
$$
we obtain the exact identities
$$
 H_{96}f_0=0,\qquad H_{160}s_0=0,\qquad H_{288}f_\delta=0 .
 \tag{RH.5}
$$
For the middle assertion, $\mathcal F_\nu(Q_0,\nu_0)$ has degree at most96 because the derivative affects only radial coefficients. Every cubic term of $A_0Z$ contains at most two factors of degree32 and one of degree96, giving degree160. The complete primitive-rank and mean-rank terms have the same or smaller support; $Z_r$ has degree96.

These are statements about the given explicit family. They do not assert that an unknown correction, unknown nonlinear residual, actual cap chart, or composition into another angle is finitely supported. Physical frequencies corresponding to the last endpoint are $|4j|\le1152$.

## RH3. The already completed high97--160 source

The successful original [complete mixed-$Z$ source](R133-supplement-actual-complete7721-continuous-Z-source-cover.md) gives a complete bound for the same source $-s_0$. Its summary field
$$
 \texttt{complete\_source\_bounds.inner\_body.high97\_through160.L2\_L2\_radial}
$$
is a directed ordinary norm bound for $H_{96}s_0$ on $[0,9/10]$. Denote its directed upper endpoint by $S_H$. The old actual report already gives the outward display
$$
                         S_H<1.155273\,10^{-6}.
 \tag{RH.6}
$$
This is a copy of an old successful conclusion, not a new evaluation.

The original proof and producer first combine the full raw nonmean residual with its signed even mean, then pay the complete centre and direction repairs. For the high projection the raw mean is exactly annihilated, while every nonmean repair contribution remains. The high norm is its own complete saved upper bound. It is not obtained by subtracting the squares of the independent full and low upper bounds.

The summary also has distinct whole-$[0,25/8]$ and fixed-negative-window records. They are not substituted for the inner record here. In particular, the fixed negative endpoint
$2383968743003/10^{13}$ retains its original explicit-background interpretation; it is not automatically the genuine negative-phase endpoint for a changed background. No restriction of old rows or source integral is repeated.

Let $\mathcal D_{\mathrm{core}}$ be the already completed whole-core D budget in RF.14. Applying $H_{96}$ to the exact R.5 identity, and using R.7--R.8, gives
$$
 H_{96}f_\delta
   =-\delta H_{96}s_0
      -H_{96}\int_0^\delta
          \{\Delta\mathcal F_\nu(t)+\Delta A(t)Z\}\,dt,
$$
$$
 \boxed{\quad
 \|H_{96}f_\delta\|_{L^2(I_-;L^2_\phi)}
 \le |\delta|S_H
       +\frac{|\delta|^2}{2d}\mathcal D_{\mathrm{core}} .
 \quad}\tag{RH.7}
$$
There is no background $F_0$ term in (RH.7). The known linear source, all its means before projection, and the selected-parameter remainder are still the same complete objects. No second raw-mean fee, $384E_Z$, amplitude factor or Green multiplier is charged.

## RH4. A fixed-coefficient expansion gives two sharper high bands

For each fixed $\delta$, abbreviate the radial coefficients at $\nu_\delta$ by $\beta_\delta,G_\delta,K_\delta$ and hold them fixed while expanding in the state. Put $Q_0=(u,v)$, $Z=(\xi,\zeta)$ and
$$
 B_\delta=u\xi+K_\delta v\zeta,\qquad
 S_{Z,\delta}=\xi^2+K_\delta\zeta^2,\qquad m_Z=\langle\zeta\rangle .
$$
The exact cubic state expansion is
$$
 \mathcal F(Q_0+\delta Z,\nu_\delta)
  =\mathcal F(Q_0,\nu_\delta)
    +\delta D_Q\mathcal F(Q_0,\nu_\delta)Z
    +\delta^2T_{2,\delta}+\delta^3T_{3,\delta},
 \tag{RH.8}
$$
where
$$
 \begin{split}
 T_{2,\delta}={}&-\beta_\delta\{
       I(S_{Z,\delta})Q_{0,\phi}
       +2I(B_\delta)Z_\phi
       +S_{Z,\delta}Q_0+2B_\delta Z\}\\
   &+G_\delta m_ZJ(K_\delta)Z_\phi,\\
 T_{3,\delta}={}&-\beta_\delta\{
                  I(S_{Z,\delta})Z_\phi+S_{Z,\delta}Z\}.
 \end{split}\tag{RH.9}
$$
This is an exact algebraic identity at each fixed $\delta$. Because the radial coefficients can themselves depend on $\delta$ inside the compact intrinsic bump, it does not assert that the entire core family is a polynomial of degree three in$\delta$. The positive-collar polynomial of R.15--R.16 has the additional fixed-intrinsic-coefficient hypothesis; it is not extended here.

The four state terms in (RH.8) have support bounds96,160,224,288, respectively. The last term in $T_{2,\delta}$ has support at most96. Since $(Q_\delta)_r$ also has support at most96,
$$
 \boxed{\quad
 H_{160}f_\delta
  =-\delta^2H_{160}T_{2,\delta}
                 -\delta^3H_{160}T_{3,\delta},
 \qquad
 H_{224}f_\delta=-\delta^3H_{224}T_{3,\delta}.
 \quad}\tag{RH.10}
$$
Thus the first left side contains only indices161--288, and the second only225--288. The holonomy mean term in (RH.9) vanishes under these two declared projections because of its exact support. It is not removed from the original source or any mean boundary row.

## RH5. Complete symbolic bounds from already paid global products

The same original D checks give on the entire core
$$
 \|Q_0\|_{A^0,\mathrm{pair}}\le7,\quad
 \|Q_{0,\phi}\|_{A^0,\mathrm{pair}}\le6,\quad
 \|Z\|_{A^0,\mathrm{pair}}\le19,\quad
 \|Z_\phi\|_{A^0,\mathrm{pair}}\le83.
$$
The complete WL positive product, uniformly on the selected interval, is
$$
 \mathsf B\ge
 \sup_{r\in I_-,\,|\delta|\le d}
       |\beta_\delta(r)|\max\{1,|K_\delta(r)|\}.
 \tag{RH.11}
$$
Use the genuine Wiener primitive norm $1/4$ for these known finite functions. Define the unevaluated exact expressions
$$
 \begin{split}
 \mathcal T_2&=\mathsf B
    \left(\frac{19^2\cdot6}{4}
              +\frac{7\cdot19\cdot83}{2}
              +3\cdot7\cdot19^2\right),\\
 \mathcal T_3&=\mathsf B
    \left(\frac{19^2\cdot83}{4}+19^3\right).
 \end{split}\tag{RH.12}
$$
The first three terms bound the two primitive products and the local cubic derivative in (RH.9), after the exact high projection has eliminated its support96 holonomy term. The second line bounds both complete terms of $T_{3,\delta}$. The pair $A^0$ bound controls the Euclidean normalized-circle $L^2$ norm. Therefore
$$
 \boxed{\quad
 \|H_{160}f_\delta\|_{L^2(I_-;L^2_\phi)}
   \le\sqrt L\bigl(|\delta|^2\mathcal T_2
                         +|\delta|^3\mathcal T_3\bigr),\qquad
 \|H_{224}f_\delta\|_{L^2(I_-;L^2_\phi)}
   \le\sqrt L\,|\delta|^3\mathcal T_3 .
 \quad}\tag{RH.13}
$$
The factor $\sqrt L$ uses ordinary radial measure once. The complete original mean participates in all product estimates before projection. No physical-angle Jacobian, radial $P$, or extra orthonormal-coordinate factor enters (RH.12)--(RH.13).

For $H_{160}f_\delta$ one may also use the contraction bound
$|\delta|^2\mathcal D_{\mathrm{core}}/(2d)$ from R.5 and $H_{160}s_0=0$.
If a future public scalar consumer evaluates these complete bounds, it may select a smaller complete upper bound for that same norm. No new scalar value or numerical improvement is asserted here.

## RH6. Typed use, exact evidence and remaining obligations

The known forcing decomposes into
$$
 f_\delta=\Pi_{\le96}f_\delta
       +\Pi_{97\ldots160}f_\delta
       +\Pi_{161\ldots224}f_\delta
       +\Pi_{225\ldots288}f_\delta .
 \tag{RH.14}
$$
RF supplies the symbolic complete ordinary low load; a successful CR receipt evaluates its new restricted bound. Equations (RH.7) and (RH.13) give legitimate known high loads in the same moving angle; the individual shells may use the corresponding complete high bound by orthogonal contraction. They do not give unknown high-body or high-cut norms, a strong-return remainder, an incoming inverse, or a physical-curvature-domain entry. The complete finite193 low receiver still retains its independent cap affine source, original96 waist source, nonlinear source and unknown high feedback.

For an arbitrary approximate state $Q$, the source of the error equation also contains its actual residual $Q_r-\mathcal F(Q,\nu_\delta)$ and its actual value jumps. Neither is deleted by the finite support of the known $f_\delta$. For a true solution the residual is zero by its equation, but its correction need not be finite Fourier.

Primary identities used here are already immutable small texts:

| Primary | Git blob | Bytes / SHA256 |
|---|---|---|
| Exact continuous direction Q.1--Q.3 | 2bc958ab42db0c4936a717e54ff3b43f5001bdf5 | 8753 / 2b7d6080dc7fdac0bd5c557b71f3e7ec1eb5436a14d45a5a762e1b548a9e20f1 |
| Exact centre repair V.1--V.5 | 7338254acdfdab61bd22124d964a4231791b9f7f | 11484 / a39fcfa2b7ca6f83cd9fadcc1987afe86f3364830848de78d2401469d7ce9f44 |
| Complete residual R.1--R.16 | 4cd540b5da2e5f2de3aff44a52fc003ab26d5ae5 | 14153 / 575bd371c09d0b82a975b0c80082f652b82468c90d56d0e730da5e98602d6861 |
| Complete mixed-Z finish summary | 79fb51921478ac1e8682601980b35dc1cb3cb904 | 21085 / e1ae6bd3ae8b9f04297fb2c9664d249c15ffe9366d15a4504444f06f08b727ac |
| Complete mixed-Z source contract | 2e78310c5f10c2344989675b29b32142cce2e654 | 8736 / 3567bcd86a2ae190117c9e9acb22f588085ad4d144b5da5417fccb0d666a03c4 |

The same RF D/WL execution identities supply (RH.11). Their complete source fields, raw means and repair fees remain as recorded. The CR consumer is neither modified nor rerun for this analytic consequence; no original native is restored and no new numerical arithmetic is executed.
