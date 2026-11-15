# R133 supplement: complete principal Sobolev bootstrap and exact coefficient perturbations

2026-11-15. Analytic statement; no new numerical evaluation.

The same full-circle principal inverse, once bounded on L2, extends to every fixed Sobolev window for which the actual coefficient has the required derivatives. A finite triangular polynomial gives explicit complete constants, without a smallness condition on that derivative matrix. A separate signed-energy argument supplies a real coefficient neighborhood, and exact inverse identities give coefficient derivatives.

This concerns the individual factors in IC/SEI. It does not supply the complete physical incoming inverse, its independent errors, finite equations, positive-side head functions, or a nonlinear core family.

## PSB1. Fixed scalar spaces and immutable evidence

Use the physical period $\pi/2$, normalized measure and physical frequency $4j$:
$$
 \Lambda_j=(1+16j^2)^{1/2},\quad
 \|f\|_{H^s}^2=\sum_j\Lambda_j^{2s}|\widehat f_j|^2,\quad
 I=\partial_\phi^{-1}(1-\Pi).
 \tag{PSB.1}
$$
On the full scalar circle, including its constant coordinate,
$$
 \|I:H^s\to H^s\|\le\frac14,\qquad
 \|I:H^s\to H^{s+1}\|\le C_I=\frac{\sqrt{17}}4,\qquad I^*=-I.
 \tag{PSB.2}
$$
Although $I1=0$, $M_cI$ can have a nonzero output mean.

Use the actual coefficients of IC.23 and SEI.2:
$$
 c_i=-\mu/2+v_i,\quad c_o=\mu/2+v_o,\quad
 \Pi v_i=\Pi v_o=0,\quad T_\sigma=1+M_{c_\sigma}I.
 \tag{PSB.3}
$$
These are full coefficients on the same selected true circle. Neither $c_o-c_i$ nor a scalar mean replaces either factor. The outgoing rotation and global sign remain in the order proved by MS/ZD.

| Input | Immutable Git blob | SHA256 |
|---|---|---|
| Current IC.23,26--29 | eeedd786977f2e324852e430bc1a3a82c175e78f | a5717f1d2be8ba7e11b43b53a052f419c8bb25ef198a9c2bf1acda16ea5f7cea |
| Complete principal adjoint bootstrap PIB | b1cb6bfa236729b8002f30097b55969cbfbab9e8 | 2d74b71c0584cb5ec1af849b6fb5756e48da58bf313d72be62d582d557d23acb |
| Terminal-only individual energy contract SEI | 0f83547b95a0912e03600a28fb9e7c34c6968046 | 268be1a8766bad61335e1b47e15dad6686a2de1116caa880e1d007081a57d44c |
| Complete SN execution, run43751213826/1 | 4dbde1fc9fef378f9f99f0e13da738e107a93ec7 | eccb4ce4e7f8c783079e4400cd7a978214817d8092f50cd2bb8f1acbcf3d6ea6 |
| Actual individual energy execution, run43773319871/1 | e1532b816ea344ee65e52a503279376a0c449299 | b0088f831471f29d41624e487586fbb9f4801ef7837f9b4dd3c29a57e51b3d29 |

The last execution has child return zero, twenty structural gates and both strict energy tests. Its complete scientific object has 35198 UTF-8 bytes and SHA256 e830e10be50804e80054dee7983fe8004a64d24ab5ff567298a490d8f737c93b. Those bytes were reconstructed exactly; no old scalar was reevaluated.

Its shared complete norm records are
$$
\begin{split}
 K_0 &:\
 [1.03380348704792601592204652917414797973152430630000265397246
       \mathbin{+/-}4.19\,10^{-60}],\\
 K_- &:\
 [7.82225994927640878890612421432461144778754752891852946234844
       \mathbin{+/-}3.59\,10^{-60}].
\end{split}
 \tag{PSB.4}
$$
In numerical use these names mean the directed upper endpoints of their original records. They are norm budgets, distinct from the old logarithmic certificates. Their actual scope is the original selected object and chart.

## PSB2. Signed coercivity with the full scalar mean

Let $c\in L^\infty$ be real. Suppose one sign $\varepsilon\in\{-1,1\}$ and a positive $\kappa$ satisfy
$$
                \varepsilon c(\phi)\ge\kappa
                    \quad\hbox{almost everywhere}.
 \tag{PSB.5}
$$
Write $a=\Pi c$, $v=c-a$ and $V\ge\|v\|_\infty$. Then
$$
 T_c=1+M_cI:L^2\longrightarrow L^2
 \quad\hbox{is a bounded isomorphism},\qquad
 \|T_c^{-1}\|\le1+\frac V\kappa .
 \tag{PSB.6}
$$

Indeed $I$ is compact on L2, so $T_c$ has Fredholm index zero. If $T_cf=0$, put $u=If\in H^1$ and $f_0=\Pi f$. The exact equation is
$$
                    u'+cu+f_0=0,\qquad \Pi u=0 .
 \tag{PSB.7}
$$
The real part of its L2 pairing with $\varepsilon u$ cancels the derivative by periodicity and cancels the constant by $\Pi u=0$. Thus $\kappa\|u\|_2^2\le0$ and $u=f=0$. Index zero gives surjectivity and the bounded inverse.

For $T_cf=g$, the same identity gives
$$
                         \|If\|_2\le\kappa^{-1}\|g\|_2.
 \tag{PSB.8}
$$
The exact constant factor $T_a=1+aI$ has constant-mode inverse one and nonzero multipliers $i4j/(i4j+a)$, of modulus at most one. Hence
$$
 f=T_a^{-1}(g-vIf),\qquad
 \|f\|_2\le\|g\|_2+V\|If\|_2.
 \tag{PSB.9}
$$
This proves (PSB.6), including its nonmean numerator and scalar mean. It assumes no physical boundary inverse.

SEI's two actual strict gaps supply (PSB.5) with the positive incoming and negative outgoing signs. This argument justifies the already saved energy bounds analytically; it does not request their reevaluation.

## PSB3. Exact derivative equations

Fix an integer $m\ge0$. Suppose $c\in W^{m,\infty}$ and $K\ge1$ bounds the existing L2 inverse of $T_c$. This section needs no additional sign assumption. A complex coefficient is also allowed, with conjugation in the adjoint.

For $g\in H^m$ and $f=T_c^{-1}g$, the identity
$$
                              f=g-cIf
 \tag{PSB.10}
$$
and the gain of $I$ improve regularity successively from L2 to $H^m$. For each $0\le q\le m$,
$$
 T_c\partial^q f
 =\partial^qg-\sum_{r=0}^{q-1}{q\choose r}
             M_{\partial^{q-r}c}\,I\partial^rf .
 \tag{PSB.11}
$$
Only the exact commutation $I\partial=\partial I$ is used. No physical projection or coordinate map is commuted.

The adjoint and its inverse equation are
$$
               T_c^*=1-I M_{\overline c},\qquad
               z=(T_c^*)^{-1}g=g+I(\overline c z).
 \tag{PSB.12}
$$
Its L2 inverse has the same bound $K$. The same regularity bootstrap and product rule give
$$
 T_c^*\partial^qz
 =\partial^qg+I\sum_{r=0}^{q-1}{q\choose r}
                   M_{\partial^{q-r}\overline c}\partial^rz .
 \tag{PSB.13}
$$
All identities first hold on smooth data and then on the declared spaces by the proved regularity and density.

## PSB4. Complete finite triangular polynomial

Supply actual complete derivative bounds
$$
             b_\ell\ge\|\partial^\ell c\|_\infty,
                            \qquad 1\le\ell\le m.
 \tag{PSB.14}
$$
Define nonnegative matrices, indexed by $0,\ldots,m$,
$$
 A_{qr}=
 \begin{cases}
 (K/4){q\choose r}b_{q-r},&r<q,\\
 0,&r\ge q,
 \end{cases}
 \qquad W_{qq}={m\choose q}^{1/2},\qquad
 B=\sum_{p=0}^{m}A^p .
 \tag{PSB.15}
$$
The matrix $A$ is strictly lower triangular, so $A^{m+1}=0$ exactly. In particular $B$ is a finite polynomial, without a condition $\|A\|<1$.

Let $F_q=\|\partial^qf\|_2$ and $G_q=\|\partial^qg\|_2$. Equations (PSB.2),(PSB.11) give
$$
                         F\le K G+AF\le K BG
 \tag{PSB.16}
$$
componentwise, after $m+1$ substitutions. The exact physical Bessel identity is
$$
 \|f\|_{H^m}^2
   =\sum_{q=0}^m{m\choose q}\|\partial^qf\|_2^2
   =\|WF\|_{\ell^2}^2 .
 \tag{PSB.17}
$$
The adjoint solution satisfies the identical nonnegative comparison by (PSB.13), with $I$ on the output side. Thus
$$
 {\cal K}_m:=K\|WBW^{-1}\|_{\ell^2\to\ell^2}
 \quad\Longrightarrow\quad
 \|T_c^{-1}\|_{H^m\to H^m},\
 \|(T_c^*)^{-1}\|_{H^m\to H^m}\le{\cal K}_m .
 \tag{PSB.18}
$$
A complete finite upper alternative is
$$
 {\cal K}_m\le
 K\bigl(\|WBW^{-1}\|_{\ell^1\to\ell^1}
        \|WBW^{-1}\|_{\ell^\infty\to\ell^\infty}\bigr)^{1/2}.
 \tag{PSB.19}
$$
Every entry and every full row or column must be included. A later evaluation belongs in public Actions. No such matrix is evaluated here.

If $c$ is constant, $A=0$, $B=1$ and $\mathcal K_m=K$. The construction introduces no artificial factor from summing equal constant-coefficient bounds.

The finite matrix in (PSB.15) only organizes derivative estimates. It is not the physical finite Schur matrix. A finite Fourier section, a source estimate on a different chart or the total H3 coefficient bound does not supply (PSB.14) for arbitrary $m$.

## PSB5. One inverse on negative and fractional windows

Duality from the adjoint estimate gives
$$
              T_c^{-1}:H^{-m}\longrightarrow H^{-m},
                      \qquad \|T_c^{-1}\|\le{\cal K}_m.
 \tag{PSB.20}
$$
Both inverse identities hold on the smooth core and extend by density because $M_c$ and $I$ are bounded in the declared windows. Alternatively, a distributional kernel obeys $f=-cIf$ and gains regularity until it reaches the known L2 kernel. The extensions agree on every overlap.

For $|s|=m+\theta$, $0\le\theta\le1$, use the coefficient regularity needed by the two endpoint estimates. Hilbert-scale interpolation then gives
$$
 \begin{split}
 \|T_c^{-1}:H^s\to H^s\|
       &\le{\cal K}_m^{1-\theta}{\cal K}_{m+1}^{\theta},\\
 \|IT_c^{-1}:H^s\to H^{s+1}\|
       &\le C_I{\cal K}_m^{1-\theta}{\cal K}_{m+1}^{\theta}.
 \end{split}
 \tag{PSB.21}
$$
An endpoint uses only its own estimate. The saved SEI negative-$4/3$ bound remains a distinct complete candidate for that window and is not recalculated through this formula.

Smooth coefficients therefore give this same principal inverse on every fixed real Sobolev space. This does not assert uniform numerical constants for every $s$, tame estimates in an unknown PDE background, or the actual higher-derivative data needed by a Nash iteration.

## PSB6. Explicit real coefficient neighborhood

Suppose the base satisfies (PSB.5) and $\|c-\Pi c\|_\infty\le V$. For a real perturbation $h$ with
$$
                         \|h\|_\infty\le r<\kappa,
 \tag{PSB.22}
$$
one has
$$
 \varepsilon(c+h)\ge\kappa-r,\qquad
 \|(c+h)-\Pi(c+h)\|_\infty\le V+2r.
 \tag{PSB.23}
$$
PSB2 gives the full-circle inverse with
$$
 K_0(h):=1+\frac{V+2r}{\kappa-r}
        \ge\|T_{c+h}^{-1}:L^2\to L^2\|.
 \tag{PSB.24}
$$
The scalar mean may change and remains in the exact constant factor $T_{\Pi(c+h)}$.

If $h\in H^1$ and the base nonmean multiplier has the complete PIB bound $B_0$, the already proved physical-frequency estimate gives
$$
 B_h=B_0+\frac{39}{32}\|h'\|_2
       \ge W_{1/3}\bigl((c+h)-\Pi(c+h)\bigr).
 \tag{PSB.25}
$$
The complete adjoint bootstrap of PIB yields
$$
 \|T_{c+h}^{-1}:H^{-4/3}\to H^{-4/3}\|
 \le1+C_I B_h+C_I^2B_h(V+2r)K_0(h).
 \tag{PSB.26}
$$
These are two bounds for one inverse. The physical mean ports remain independent. Higher windows require their actual derivative bounds in PSB3--5.

This is a neighborhood in coefficient functions on the fixed selected circle. No unknown nonlinear geometric family is asserted to lie in it. A different-background bound, a parameter volume column or an unrelated coordinate error does not establish that inclusion.

## PSB7. Exact perturbation and coefficient derivatives

On a fixed $H^s$, write $A_c=T_c^{-1}$ and choose a complete bound $K_s$. If multiplication by $h$ has a complete same-window bound $M_s(h)$ and
$$
                          \rho_s=K_sM_s(h)/4<1,
 \tag{PSB.27}
$$
the exact ordered identities
$$
 T_{c+h}=T_c(1+A_cM_hI),\qquad
 A_{c+h}=(1+A_cM_hI)^{-1}A_c
 \tag{PSB.28}
$$
give
$$
                  \|A_{c+h}\|_{H^s\to H^s}
                         \le K_s/(1-\rho_s).
 \tag{PSB.29}
$$
Here $h$ may be complex. A sufficient multiplication bound is the complete two-sided sum
$$
             M_s(h)=\sum_{k\in\mathbb Z}
                        (1+4|k|)^{|s|}|\widehat h_k|.
 \tag{PSB.30}
$$
It includes the constant term. At $s=0$ the sharper $\|h\|_\infty$ is sufficient.

Whenever both full inverses exist,
$$
 A_{c+h}-A_c=-A_{c+h}M_hI A_c
           =-A_cM_hI A_{c+h}.
 \tag{PSB.31}
$$
The two orders come from the inverse identities, not from commuting multipliers with $I$.

In the Banach coefficient space with norm (PSB.30), inversion is analytic on the open invertible set. Its derivatives are
$$
 \begin{split}
 D A_c[h]&=-A_cM_hIA_c,\\
 D^k A_c[h_1,\ldots,h_k]
 &=(-1)^k\sum_{\pi\in{\mathfrak S}_k}
       A_cM_{h_{\pi(1)}}I A_c\cdots M_{h_{\pi(k)}}I A_c,
 \end{split}
 \tag{PSB.32}
$$
and
$$
 \|D^k A_c[h_1,\ldots,h_k]\|_{H^s\to H^s}
       \le k!K_s^{k+1}4^{-k}\prod_{\ell=1}^k M_s(h_\ell).
 \tag{PSB.33}
$$
For finitely many windows require their respective complete neighborhood gates; the inverses and derivatives agree on the common smooth core. These are derivatives of the exact coefficient and exact operator. No numerical upper bound is differentiated.

## PSB8. Scope and remaining inputs

The new results are signed full-circle coercivity including the scalar mean, a complete finite triangular polynomial for both positive and negative Sobolev windows, and exact coefficient neighborhoods and inverse derivatives.

The actual saved SEI base bounds are inputs, not new arithmetic. Higher derivative bounds, matrix evaluations and coefficient-neighborhood membership needed in an application remain to be supplied separately in public Actions.

The complete incoming errors, transported sign, actual finite and mean equations, positive given-head graph, independent radial head functions, global return and true nonlinear-background transfer remain independent obligations. A principal inverse on every fixed scalar Sobolev window does not invert those complete coupled operators.
