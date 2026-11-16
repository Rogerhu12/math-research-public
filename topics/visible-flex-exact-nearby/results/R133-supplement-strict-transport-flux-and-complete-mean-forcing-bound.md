# R133 supplement: strict transport flux and a complete angular L1 mean-forcing recipe

2026-11-16, phase_inverse.

**Proved here:** on the original strict negative interval, the same complete genuine height has an exact radial-to-angular flux identity. After pairing with the full physical-mean test, this removes the explicit positive power of frequency and the radial derivative of the first amplitude. Five exact mean recursions then retain the original decay $n^{-23/6}$. The complete positive recipe below uses normalized angular $L^1$ bounds for the common weight of WMF and reads the already successful geometric, amplitude and profile records.

This is a new analytic bound for the same forcing. No scientific value has been evaluated, no previous mean/source target has been rerun, and no numerical improvement or smallness gate is asserted. The local root patch retains its old complete forcing bound. The strict reciprocal of $T$ is not extended to the root.

## WMT1. Same trial, interval and complete genuine derivative rules

Use exactly the WUA/WEJ trial and the original input cutoff:
$$
 n=4|j|\ge N_0=388,\qquad \epsilon=\operatorname{sgn}j,\qquad
 z_n=n^{-1},\qquad
 f=P n^{7/6}{\cal U}_{n,\epsilon}^{\rm ext}(w),\qquad
 w=w_0+z_nw_1^{\rm ext}.
 \tag{WMT.1}
$$
The symbol $z_n$ in this note is the inverse frequency, not the physical mean $z_{\rm ph}$. Write
$$
 \begin{gathered}
 x=X_\phi,\qquad y=T_\phi,\qquad
 K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix},\\
 H=i\epsilon x\,Id+yK_T,\qquad
 M_r=i\epsilon X_r\,Id+T_rK_T,\qquad
 D=\partial_r-d\partial_\phi .
 \end{gathered}
 \tag{WMT.2}
$$
The matrix $K_T$ is not the physical curvature $K$.

The numerical predecessors retain their original selected real member and frozen actual realization. These identities do not extend a selected coordinate or a saved scalar bound to an unqualified parameter family.

All strict identities are on the same interval
$0\le r\le r_c$ with
$r_c=76285779072683/320000000000000$.
The saved strictly positive lower for $-T$ applies throughout this interval. All original one-sided pieces and actual seams are retained. No new rectangle or complex extension of the physical background is assumed.

The genuine profile, with the original full root matrix $C_n$ and its $\beta_n$, has the exact rules
$$
 \begin{split}
 \partial_\phi{\cal U}^{\rm ext}(a)
   &=n{\cal U}^{\rm ext}(Ha)
       +{\cal U}^{\rm ext}
           (\partial_\phi a-z_nV_{\rm ext}yE_{12}a),\\
 \partial_r{\cal U}^{\rm ext}(a)
   &=n{\cal U}^{\rm ext}(M_ra)
       +{\cal U}^{\rm ext}
           (\partial_ra-z_nV_{\rm ext}T_rE_{12}a).
 \end{split}
 \tag{WMT.3}
$$
These are WUA.30 and WEJ.23 for the same reference columns. The root matrix depends on the input index, not on $r$ or $\phi$, so it is not differentiated in (WMT.3). Both reference columns remain present in their original realization.

The complete WUA forcing is denoted $(F_b,F_a)^t=-{\cal L}_0w_0$; it includes the original $\vartheta$ term and all the differential coefficients. For the extended first amplitude,
$$
 \begin{split}
 {\cal T}_\epsilon w_0&=0,\\
 {\cal T}_\epsilon w_1^{\rm ext}
   &=\binom{F_b^{\rm ext}}{F_a^{\rm ext}}
     =\binom{F_b}{F_a}+V_{\rm ext}w_0 .
 \end{split}
 \tag{WMT.4}
$$
In particular $F_b^{\rm ext}=F_b+V_{\rm ext}a_0$ and
$F_a^{\rm ext}=F_a+V_{\rm ext}b_0^{\rm amp}$, where
$w_0=(a_0,b_0^{\rm amp})^t$. This amplitude component is distinct from the radial scalar $b_0=\beta(1-\Pi S)$ in WMF.

Equation (WMT.4) uses the full WUA.22--23 addition
$w_1^{\rm ext}=w_1+\mathcal B_{\rm ext}K_Tw_0$.
The nonzero tail of $\mathcal B_{\rm ext}$ is not cut away.

## WMT2. Exact ordinary radial transport of the amplitude

Let $l,m_{\rm can}$ be the canonical transport coefficients of WUA.14--15. The canonical first equation can be solved, on the strict domain $T<0$, as
$$
 w_T=-i\epsilon K_Tw_X+{\cal N}w+
                     \binom{F_a/2}{F_b/(2T)},\qquad
 {\cal N}=
 \begin{pmatrix}
 -l/2&-i\epsilon T^2m_{\rm can}/2\\
 -i\epsilon Tm_{\rm can}/2&-(l+1/T)/2
 \end{pmatrix}.
 \tag{WMT.5}
$$
For $w_0$ the forcing is zero; for $w_1^{\rm ext}$ it is the complete extended pair from (WMT.4).

The genuine fold identities are
$$
 \begin{gathered}
 DT=Q_f x,\qquad DX=-Q_fTy,\qquad
 \mu=Q_f^2(x^2+Ty^2),\\
 H^{-1}H_D=-i\epsilon Q_fK_T,\qquad
 H_D=M_r-dH .
 \end{gathered}
 \tag{WMT.6}
$$
Here $Q_f$ is the positive fold coefficient, not a Fourier projection. Matrices that are linear combinations of $Id$ and $K_T$ commute pointwise. Eliminating $w_X$ between the physical $r$ and $\phi$ derivatives in (WMT.5) gives
$$
 w_r={\cal C}w_\phi
       +Q_f(xId+i\epsilon yK_T)
                      \left({\cal N}w+
                          \binom{F_a/2}{F_b/(2T)}\right),
 \qquad {\cal C}=dId-i\epsilon Q_fK_T .
 \tag{WMT.7}
$$
In particular $H{\cal C}=M_r$. No derivative of an interval upper or reconstructed phase value has been used.

For a completely explicit zero-order matrix put
$$
 {\mathfrak h}=\frac{q_r}{q}+4\beta\Pi S-4d_\phi,\qquad
 {\cal L}=-\frac{\mathfrak h}{2}Id+
 \frac{Q_f}{4}
 \begin{pmatrix}
 x/T&-i\epsilon y\\
 i\epsilon y/T&-x/T
 \end{pmatrix}.
 \tag{WMT.8}
$$
Indeed WUA.15 gives
$l=\mathfrak h x/(Q_f(x^2+Ty^2))-1/(2T)$ and
$T^2m_{\rm can}=-\mathfrak h Ty/(Q_f(x^2+Ty^2))$.
Substitution in $Q_f(xId+i\epsilon yK_T){\cal N}$ yields exactly (WMT.8); the apparent inverse determinant cancels in this whole matrix identity.

Define the complete physical forcing vector
$$
 q_{\rm ext}=\frac{Q_f}{2}
 \binom{xF_a^{\rm ext}+i\epsilon yF_b^{\rm ext}}
       {i\epsilon yF_a^{\rm ext}+(x/T)F_b^{\rm ext}}.
 \tag{WMT.9}
$$
Then the full amplitude in (WMT.1) obeys
$$
                 w_r={\cal C}w_\phi+{\cal L}w+z_n q_{\rm ext}.
 \tag{WMT.10}
$$
This equation contains no $w_{1,r}^{\rm ext}$ on its right side, no ratio of the first amplitude by $v_{0,\sigma}$, and no omitted forcing component. The reciprocal $T^{-1}$ is justified only on the stated strict interval. The original local/germ forcing is used separately near the root.

## WMT3. An exact angular flux for the complete genuine height

Set
$$
                  {\cal M}=xE_{12}+i\epsilon yE_{11}.
 \tag{WMT.11}
$$
The elementary ordered identities
$$
 E_{12}K_T=E_{11},\qquad T_r=Q_fx+dy
$$
give
$$
           yE_{12}{\cal C}-T_rE_{12}=-Q_f{\cal M}.
 \tag{WMT.12}
$$
The order of $E_{12}$ and $\mathcal C$ is essential here.

Expand $\partial_\phi{\cal U}^{\rm ext}({\cal C}w)$ using (WMT.3), use $H{\cal C}=M_r$, and then substitute (WMT.10). The exact result is
$$
 \boxed{
 \partial_r{\cal U}^{\rm ext}(w)
   =\partial_\phi{\cal U}^{\rm ext}({\cal C}w)
       +{\cal U}^{\rm ext}
         \left[
          ({\cal L}-{\cal C}_\phi
                  -z_nV_{\rm ext}Q_f{\cal M})w
                  +z_nq_{\rm ext}\right].
 }
 \tag{WMT.13}
$$
The term $-z_nV_{\rm ext}Q_f{\cal M}$ is the difference of the two actual genuine derivative corrections. It is not a free-profile replacement. The $V_{\rm ext}w_0$ part of $q_{\rm ext}$ is also retained, and these two terms are not individually set to zero.

Use the complete WMF kernels
$$
 e=-\frac{2\beta m}{\eta}I(p_Ju),\qquad
 e_\kappa=-b_0e+
       2\beta mP\!\left[p_J\left(Kv-\frac{du}{\eta}\right)\right].
 \tag{WMT.14}
$$
Both are mean zero. Consequently the outer height projection in (WMT.1) can be removed in their two pairings, without removing any physical mean. Integrating the angular flux in (WMT.13) by parts proves
$$
 \boxed{
 F_{\rm mean}
   =n^{7/6}\Pi{\cal U}^{\rm ext}
      \left[
       \left\{e_\kappa Id-\partial_\phi(e{\cal C})
                 +e{\cal L}
                 -z_neV_{\rm ext}Q_f{\cal M}\right\}w
                +z_ne q_{\rm ext}\right].
 }
 \tag{WMT.15}
$$
The derivative acts on the entire product $e{\cal C}$. It includes $e_\phi$, the drift derivative, the fold coefficient derivative and the derivative of $K_T$. No radial integration by parts has occurred, so there is no new $e_r$ term or radial endpoint contribution.

For clarity define
$$
 \begin{gathered}
 {\cal B}=e_\kappa Id-\partial_\phi(e{\cal C})+e{\cal L},
 \qquad {\cal D}=eV_{\rm ext}Q_f{\cal M},\\
 A_0={\cal B}w_0,\qquad
 A_1={\cal B}w_1^{\rm ext}-{\cal D}w_0+e q_{\rm ext},
 \qquad A_2=-{\cal D}w_1^{\rm ext}.
 \end{gathered}
 \tag{WMT.16}
$$
Then (WMT.15) is the complete identity
$$
               F_{\rm mean}
              =n^{7/6}\Pi{\cal U}^{\rm ext}
                       (A_0+z_nA_1+z_n^2A_2).
 \tag{WMT.17}
$$
Every displayed $A_k$ is a full vector amplitude. In particular, the projection in $e_\kappa$ remains in it. If that projection is expanded, its actual constant output must be kept; it cannot be dropped just because the original height was projected.

## WMT4. Normalized angular L1 jets for the common weight

All $L^1$ norms below use normalized angular measure. For scalar functions define
$$
 [a]_{j,\infty}=\frac{\|\partial_\phi^ja\|_\infty}{j!},
 \qquad
 [a]_{j,1}=\frac{\|\partial_\phi^ja\|_1}{j!}.
 \tag{WMT.18}
$$
For vector amplitudes use the sum of the component norms. For matrices use the sum of the entry norms. These norms are submultiplicative; in this convention the entry-sum norm of $Id$ is two.

For arrays write $(a*b)_j=\sum_{i=0}^ja_i b_{j-i}$. Products of normalized derivative bounds use this convolution without an extra binomial factor. Differentiation sends an array $a_j$ to $(j+1)a_{j+1}$.

Let $U_j,V_j,d_j$ be complete upper bounds for the actual background derivatives in (WMT.18), and let nonnegative $\alpha^+,M,\beta^+,K^+,b^+$ bound
$|\alpha|,|m|,|\beta|,|K|,|b_0|$, with a strictly positive lower $\eta_-$ for $\eta$, on the same strict patch. They may be supplied by the already saved complete records with their actual norm/domain qualification. The exact strict JI/WMR qualification permits $\alpha^+=1/2$ and $\delta=79/128$ below. The bounds $M,b^+$ may be read from WMR's unchanged strict_V and strict_base records; these are bounds for $|m|$ and the complete $|b_0|$, not signed assertions about $v$.

The exact WMF identities are
$$
 \Pi[p_J(1-\alpha uIv)]=1,\qquad
 p_J>0,\qquad
 (p_J)_\phi=-\alpha uvp_J,\qquad
 \Pi p_J\le\delta^{-1}.
 \tag{WMT.19}
$$
Define complete positive $L^1$ bounds by the finite recurrence
$$
 \begin{split}
 {\mathsf p}_0&=\delta^{-1},\\
 h_j&=\alpha^+(U*V)_j,\\
 {\mathsf p}_{j+1}
  &=\frac1{j+1}\sum_{i=0}^j h_i{\mathsf p}_{j-i}.
 \end{split}
 \tag{WMT.20}
$$
Then $[p_J]_{j,1}\le\mathsf p_j$. This follows by differentiating the exact first-order equation in (WMT.19). It takes no separate norm of $a_J$, no inverse-denominator derivative and no new exponential.

The normalized convolution kernel of the complete primitive on a circle of length $L=\pi/2$ is $K_I(t)=L/2-t$ for $0<t<L$. Its distributional derivative gives $P$, and
$$
 \|I\|_{L^1\to L^1}\le\frac{\pi}{8},\qquad
 \|I\|_{L^1\to L^\infty}\le\frac{\pi}{4}.
 \tag{WMT.21}
$$
These are not the Fourier-Wiener or $L^2$ constant $1/4$.

Since $p_Ju$ is odd, $e_\phi=-\alpha m p_Ju$ without a further mean. Therefore complete bounds for $[e]_{j,1}$ are
$$
 \begin{split}
 {\mathsf e}_0&=\alpha^+M\,\frac{\pi}{8}{\mathsf p}_0U_0,\\
 {\mathsf e}_j&=\frac{\alpha^+M}{j}
                      ({\mathsf p}*U)_{j-1},\qquad j\ge1 .
 \end{split}
 \tag{WMT.22}
$$
Put
$$
 \zeta_j=K^+V_j+\eta_-^{-1}(d*U)_j,\qquad
 \rho_j=({\mathsf p}*\zeta)_j .
$$
The full projected kernel (WMT.14) then has the complete bounds
$$
 \begin{split}
 {\mathsf k}_0&=b^+{\mathsf e}_0+4\beta^+M\rho_0,\\
 {\mathsf k}_j&=b^+{\mathsf e}_j+2\beta^+M\rho_j,\qquad j\ge1 .
 \end{split}
 \tag{WMT.23}
$$
Here $\|P\|_{L^1\to L^1}\le2$ is paid at degree zero; positive angular derivatives annihilate its constant output. This is a bound for the whole exact $e_\kappa$, not for one selected part of it. The real positivity in (WMT.19) is not asserted on a complex disk.

## WMT5. A fully specified positive amplitude recipe

The following finite recipes make the new target explicit. All arrays are normalized as in (WMT.18), all products mean convolution, and all sums retain every term. A coefficient that is radial has zero pure angular derivatives above degree zero; it is not decoded as an arbitrary mixed jet.

Let $t_j,Q_j,x_j,y_j$ be complete strict bounds for $T,Q_f,x,y$; retain the old positive lower $t_->0$ for $-T$. A complete reciprocal array is
$$
 R_0=t_-^{-1},\qquad
 R_j=t_-^{-1}\sum_{i=1}^j t_iR_{j-i}\quad(j\ge1).
 \tag{WMT.24}
$$
It bounds derivatives of the signed function $1/T$. No negative power is applied to a signed interval or to a ball crossing zero.

Let $q_1^+$ and $q_->0$ be the old complete strict radial $q$ derivative upper and positive $q$ lower, and use the same complete $b^+$ as above. Since $\beta\Pi S=\beta-b_0$ exactly, the scalar $\mathfrak h$ of (WMT.8) has bounds
$$
 \mathfrak h_0=q_1^+/q_-+4\beta^++4b^++4d_1,\qquad
 \mathfrak h_j=4(j+1)d_{j+1}\quad(j\ge1).
 \tag{WMT.25}
$$
The terms $q_r/q$ and $\beta\Pi S$ are radial. Their higher angular derivatives are exactly zero; their degree-zero values have not been omitted.

Define $k_j^T=t_j+\mathbf1_{j=0}$. The complete matrix arrays
$$
 \begin{split}
 C_j&=2d_j+(Q*k^T)_j,\\
 L_j&=\mathfrak h_j+
       \tfrac14\{Q*(2x*R+y+y*R)\}_j,\\
 M_j&=x_j+y_j
 \end{split}
 \tag{WMT.26}
$$
bound the entry-sum derivatives of $\mathcal C,\mathcal L,\mathcal M$. The factor two in $C_j$ is the full scalar identity matrix.

Let $a_{0,j},b_{0,j}^{\rm amp}$ and $a_{1,j}^{\rm ext},b_{1,j}^{\rm ext}$ be the original complete component-sup derivative arrays, and put
$$
 W_{0,j}=a_{0,j}+b_{0,j}^{\rm amp},\qquad
 W_{1,j}=a_{1,j}^{\rm ext}+b_{1,j}^{\rm ext}.
$$
Let $V_j^{\rm pot}$ bound $V_{\rm ext}$ and let $F_{a,j},F_{b,j}$ be the saved complete free-forcing arrays. Set
$$
 F_a^{e}=F_a+V^{\rm pot}*b_0^{\rm amp},\qquad
 F_b^{e}=F_b+V^{\rm pot}*a_0 .
$$
A complete vector bound for (WMT.9) is
$$
 q_j^{e}=\tfrac12
    \{Q*[(x+y)*F_a^{e}+(y+x*R)*F_b^{e}]\}_j .
 \tag{WMT.27}
$$
Thus the potential addition is paid in both complete forcing components in its actual order.

Use
$$
 \begin{split}
 B_j&=2{\mathsf k}_j
          +(j+1)({\mathsf e}*C)_{j+1}
          +({\mathsf e}*L)_j,\\
 D_j^{e}&=({\mathsf e}*V^{\rm pot}*Q*M)_j,\qquad
 Q_j^{e}=({\mathsf e}*q^e)_j .
 \end{split}
 \tag{WMT.28}
$$
The first factor two is the entry-sum bound for $e_\kappa Id$; $(j+1)({\mathsf e}*C)_{j+1}$ is the whole derivative of $e\mathcal C$, including every derivative of both factors.

Complete normalized $L^1$ bounds for the three amplitudes in (WMT.16) are
$$
 \begin{split}
 A_{j,0}^{+}&=(B*W_0)_j,\\
 A_{j,1}^{+}&=(B*W_1)_j+(D^e*W_0)_j+Q_j^e,\\
 A_{j,2}^{+}&=(D^e*W_1)_j ,
 \qquad 0\le j\le5 .
 \end{split}
 \tag{WMT.29}
$$
These are three whole positive formulas. There is no subtraction of previously saved upper bounds and no mixing of different candidate decompositions.

The required finite orders are explicit:

| Object | Pure angular normalized orders required |
|---|---:|
| $p_J$ | $0$ through $5$ |
| $e$ | $0$ through $6$ |
| $e_\kappa$ | $0$ through $5$ |
| Background $u,v$ in (WMT.20)--23 | $0$ through $5$ |
| Drift $d$ | $0$ through $6$ |
| $T,Q_f,X$ | The derivatives sufficient for $C$ through $6$ and $L,M$ through $5$; in particular $X,T$ through $6$ |
| $w_0,w_1^{\rm ext},F_a,F_b,V_{\rm ext}$ | $0$ through $5$ |
| $H^{-1}$ | $0$ through $5$ |

The geometry row uses $x_j$ and $y_j$ as derivatives of actual $X_\phi,T_\phi$. It never requests or fills an unqualified zero-order phase lift. No $w_{1,r}^{\rm ext}$, $a_{J,r}$, $D_{J,r}$ or $e_r$ is a predecessor of this strict forcing recipe. Other source terms that genuinely contain $J_r$ or a radial background derivative are unchanged.

## WMT6. Five complete genuine mean recursions

Let
$$
 A(z_n)=A_0+z_nA_1+z_n^2A_2,\qquad
 {\cal A}_n=\partial_\phi-z_nV_{\rm ext}yE_{12}.
$$
Use the exact finite sequence
$$
 v_0=H^{-1}A,\qquad
 v_{\ell+1}=-H^{-1}{\cal A}_nv_\ell
                    \quad(0\le\ell\le3).
 \tag{WMT.30}
$$
Five applications of the full angular derivative rule (WMT.3) give
$$
       \Pi{\cal U}^{\rm ext}(A)
           =-n^{-5}\Pi{\cal U}^{\rm ext}({\cal A}_nv_4).
 \tag{WMT.31}
$$
All of these are periodic angular identities. The final $\mathcal A_nv_4$ is retained as a whole terminal. Since $A$ has degree two in $z_n$, the complete terminal has degrees zero through seven. There is no discarded high-degree coefficient.

For an explicit positive recurrence let $H_j^+$ be the already saved complete entry-sum upper for normalized derivatives of $H^{-1}$ and let
$c_j=(V^{\rm pot}*y)_j$.
Pad only polynomial coefficients outside their actual degree range by exact zero. Define
$$
 {\mathsf V}^{[0]}_{j,k}
      =\sum_{a=0}^jH_a^+ A_{j-a,k}^+,
       \qquad 0\le j\le5,\quad 0\le k\le2 .
 \tag{WMT.32}
$$
For $\ell=0,1,2,3$ set
$$
 \begin{split}
 {\mathsf D}^{[\ell]}_{j,k}
   &=(j+1){\mathsf V}^{[\ell]}_{j+1,k}
           +\sum_{a=0}^j c_a{\mathsf V}^{[\ell]}_{j-a,k-1},\\
 {\mathsf V}^{[\ell+1]}_{j,k}
   &=\sum_{a=0}^j H_a^+
                       {\mathsf D}^{[\ell]}_{j-a,k}.
 \end{split}
 \tag{WMT.33}
$$
At step $\ell$ retain $0\le j\le4-\ell$ in both lines of (WMT.33), and retain all polynomial degrees $0\le k\le3+\ell$. The level $v_4$ has angular orders zero and one and degrees zero through six. The complete terminal bounds are
$$
       {\mathsf T}_k={\mathsf V}^{[4]}_{1,k}
                           +c_0{\mathsf V}^{[4]}_{0,k-1},
                    \qquad 0\le k\le7 .
 \tag{WMT.34}
$$
These recurrences use $L^\infty$ matrix bounds times $L^1$ vector bounds. They do not reclassify the WGS sup/component-sum jets as Fourier-Wiener norms.

Let $P_\star$ be the original complete pointwise bound for one signed genuine reference column, read from the successful profile node. Then
$$
 \boxed{
 C_{F,s}^{\rm flux}
       =2P_\star\sum_{k=0}^{7}N_0^{-k}{\mathsf T}_k,\qquad
 |F_{{\rm mean},n}(r)|
       \le C_{F,s}^{\rm flux}n^{-23/6}
       \quad(0\le r\le r_c).
 }
 \tag{WMT.35}
$$
The factor two is the same complete reflected-column assembly as in the original mean_N6_strict node. It is not an assertion that a second reference/source port has vanished. The frequency is the physical $n=4|j|$, so the cutoff in this formula is $388$, not $97$.

The exponent is exactly $7/6-5=-23/6$. This proves a new complete same-power bound once all finite positive predecessors above have been supplied. It does not prove that the numerical value is smaller than the old one.

## WMT7. Read-only input contract and norm types

The calculation of (WMT.35) can use already successful small JSON conclusions. It does not require a restored native archive, original ray integration, old flow exponential or old scientific producer.

The complete WGS pair is:

| Complete original file | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WGS main science | 32ff92c516fcc5c43f3619930d4845d294289270 | 72251 | 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e |
| WGS original-input copies | d6d13860e322d82ce354c8c0d0eb0f279ca63b3c | 31632 | 3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66 |

Both are in
notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/.
The filenames are actual-scientific-conclusion.json and complete-original-inputs.json. Their complete same-run/source/manifest/math identity and the main file's exact reference to the copies remain required.

The two additional successful posterior nodes used directly here are:

| Complete node | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| extended_amplitude_strict | 81bd01b84d8ebf5613ec0821e7c4ae770c39dfc9 | 9627 | fc2077f4fc24d6105e9e483c1b584e53bfd60987ad1a1a9718e9459c6830a0c2 |
| profile_block_strict | f2a2687ae736d291c5d5b85e0309e625d729e5d8 | 9131 | 6e781157c43f7ba7f7e4ac454308545444164138920cbab027a7af56dd1d89a6 |

Their paths are
notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/extended_amplitude_strict.json
and the same directory's profile_block_strict.json.
They are complete preserved nodes of the original first attempt. That attempt's later failure is not changed into a successful whole run by using these already completed nodes.

The exact field families for the finite recipe are:

| Needed input | Complete source path inside the original JSON |
|---|---|
| $T,Q_f,x,y,H^{-1}$ and their complete strict jets | WGS main: complete_strict_geometry_conclusion.complete_jets.t, Q, x, y, H_inverse_entry_sum |
| $w_0$ components | WGS main: complete_strict_leading_conclusion.complete_jets.a0 and b0 |
| Complete free forcing $F_a,F_b$ | WGS main: complete_strict_forcing_conclusion.complete_forcing_jets.Fa and Fb |
| $V_{\rm ext},w_1^{\rm ext}$ | extended_amplitude_strict: conclusion.complete_jets.Vext, a1_ext and b1_ext |
| Strict drift and radial $\eta$ | WGS main: complete_strict_coefficient_conclusion.new_jets.d and eta |
| Strict reciprocal and radial prerequisites | WGS copies: copied_original_scalar_records.t_cut_lower, q_1, q_lower, eta_lower |
| Background angular pair inputs | WGS copies: copied_original_scalar_records.Q_0_0 through Q_0_3 |
| Original radial metric bounds | WGS copies: copied_original_scalar_records.beta_0 and K_0 |
| $P_\star$ | profile_block_strict: conclusion.new_complete_records.single_signed_point_profile_upper |
| Existing $|m|,|b_0|,\beta,K,\eta$ bounds, if used | WMR science: copied_original_scalar_records.strict_V, strict_base, strict_beta, strict_Kabs and strict_eta_lower |

WGS normalized degree-group upper bounds dominate each actual derivative coefficient in their group. A reader may select the existing upper for the requested pure angular index, respecting its original factorial normalization. It must not reconstruct an old producer to recover an unretained sharper row, and it must not fill a missing phase value with zero.

For new pure angular background bounds, the unchanged original pair inputs and the original physical bandwidth may be used as a new, explicitly named envelope:
$B_{0,j}\le384^{j-3}B_{0,3}$ for $j>3$, as qualified in WGS.9. The $Q_0_j$ inputs are ordinary complete Fourier $\mathcal A_0$ bounds; divide by $j!$ when placing them in (WMT.18). They are not point samples. This new pure-angular envelope is distinct from the old mixed/grouped target and does not rerun it. In the held WGS/support sources the higher ordinary values were unsaved predecessors of grouped sums; the new consumer must not reconstruct any of those old grouped sums. No assertion of a repository-wide absence is made.

Any already saved identical derivative or scalar bound used by the recipe must be read, not reevaluated. The complete actual scope, field paths, input bytes/hashes, original node bindings and retained first-attempt failure status must be checked before a new consumer imports numerical arithmetic. The later full consumer interface and exact publication budget are separate artifacts; no workflow is authorized by this analytic note.

## WMT8. Reassembly in the same physical mean and complete error

The local root forcing is unchanged. Read its already completed whole bound
$C_{F,\ell}$ with the original power $n^{-23/6}$, the original physical initial condition $z_{\rm ph}(r_*)=0$, and every original patch/interface qualification. Here $r_*$ is the true root; its upper enclosure $r_+$ enters only the already qualified local length bound and does not move that initial condition. The new strict bound (WMT.35) has exactly that power and applies to exactly the same strict forcing.

If a numerical consumer is later authorized, it may retain both the old complete strict $C_{F,s}$ and the new complete $C_{F,s}^{\rm flux}$ and choose between these two whole bounds. It must preserve both final records, select using their saved upper endpoints, and prefer the old record on a tie. This comparison cannot select individual positive terms from different recipes. This comparison also does not authorize recomputing the old WMR branch. If the old forcing is selected, the already completed corresponding WMR mean and reception targets are copied. An equivalent fixed-shape implementation may evaluate a separate complete flux branch using $C_{F,s}^{\rm flux}$ throughout and compare only the completed whole candidates at the end. In either case every previously completed target remains read-only.

In the following formulas $C_{F,s}^{\rm chosen}$ denotes that whole choice. Read, without reevaluation, the saved WMR strict backward factor $G_s$, local physical-mean bound $Z_\ell$, and complete absolute strict mean coefficient $A_s$. The same backward scalar equation and ordinary radial length give the new complete candidates
$$
 \begin{split}
 Z_s^{\rm new}
    &=G_s\bigl(r_cC_{F,s}^{\rm chosen}+Z_\ell\bigr),\\
 (Z_s')^{\rm new}
    &=A_sZ_s^{\rm new}+C_{F,s}^{\rm chosen}.
 \end{split}
 \tag{WMT.36}
$$
The exponential defining $G_s$ has already been paid and saved in WMR. It is not recomputed here. The derivative bound uses the complete absolute coefficient $A_s$, not the one-sided backward coefficient.

Read the same complete strict bounds $k_{0,s}$, $I k_s$ and $T k_s$ from the existing WMR input/target records. WMR.27--31 then gives
$$
 \begin{split}
 M_s^{\rm new}
   &=k_{0,s}(Z_s')^{\rm new}
                      +(T k_s)Z_s^{\rm new},\\
 \widetilde M_s^{\rm new}
   &=(I k_s)(Z_s')^{\rm new}
                      +\tfrac14(T k_s)Z_s^{\rm new}.
 \end{split}
 \tag{WMT.37}
$$
Here the notation $I k_s$ and $T k_s$ names the already bounded actual primitive and complete residual action on the mean-completion vector; it is not a product of unrelated scalar inputs. The factor $1/4$ is used only for the declared odd $L^2$ primitive in WMR. It is not substituted for either $L^1$ constant in (WMT.21).

The remaining complete reassembly is exactly the WMR one with the following replacements and retentions:

| Part of the same physical error | New candidate or unchanged complete input |
|---|---|
| Strict physical mean and its radial derivative | The two complete candidates in (WMT.36) |
| Strict raw and primitive mean-source terms | The two complete candidates in (WMT.37) |
| Local physical mean, derivative and both mean-source terms | Their original completed WMR records |
| Union mean-source upper on the original mixed collar receiver | The whole maximum of the unchanged local term and the new strict term |
| Nonmean ordinary source terms | All original complete block and terminal records, unchanged |
| Actual interface jumps | All original complete jump records and the original sum over every true seam |
| Collar and strict reception | The same $C_O,C_R,C_1$, original cuts, ordinary radial lengths, physical frequency powers and dyadic sums |
| Waist mean endpoint | The original full $v_z$ norm and original $\Xi_{23/6}$ multiplied by $Z_s^{\rm new}$ |
| Other three waist endpoint terms | Their original completed nonmean records |
| Positive correction and root finite factor | Their original complete records, in their original order |
| Coefficient error and its independent finite factor | Their original whole/reduced realizations and complete retained finite terms |

In particular, the original $v_z$ norm includes the two stored physical mean entries. Neither the $q$ contribution to that norm nor the actual physical mean $z_{\rm ph}$ is discarded. The independent external mean, waist amplitude, parameter $\nu$, head functions, finite matching rows and actual 96 physical columns with their still uncomputed signed normalization remain separate.

A new full-error candidate must include every term in the full realization and use its original left readout once. A new reduced-error candidate must include every term in that reduced realization while retaining its explicitly separated root and coefficient finite factors. Each may be compared only with the prior complete bound for the same operator and coordinates. The whole and reduced operators are not compared with each other, and no bound is formed by subtracting a mean subtotal from a saved whole upper.

There is no change of trial in (WMT.13)--17 and no radial integration by parts. The old true jumps therefore remain the same mathematical objects. The strict angular argument does not erase a jump, produce a new free radial source window or replace the local germ.

This note supplies neither a signed finite matrix inverse nor an inverse of the positive head equation, a physical Poisson onto theorem, a completed 96-column border or a new Newton smallness gate. It supplies a complete new forcing recipe and the exact route by which its eventual value may replace one complete input to the already established error accounting.

## WMT9. Evidence, independent checks and unevaluated targets

The mathematical identities use the complete original sources below. The successful WGS pair and the two complete posterior nodes are identified in WMT7. The successful WMR science is
notes/positive_weight_physical_mean_refinement_ci/run-43840219992-1/actual-scientific-conclusion.json,
Git blob 5fdb01ed62008489bca34a4b6231519af4f60793, 51030 bytes,
SHA256 39a2d96accdbe1b4a8073674cabeda97878876f11fc24a055b910ed61567b432.

| Source | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WMF: exact normalized-weight forcing | 2c4a1789195a1ea400ef7c547b319ea3f4f7329f | 15111 | 14900631ba2d793977336fd5f7e8870e4313cbda50a8a8c3e02fa11b53054356 |
| WUA: global real genuine trial | 7b89251dcd51e8cb78fd3e8e42905114ef982ebf | 40111 | 9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad |
| WGS: complete strict finite jets | 4980f1a2c119b6470afc24a2fc662c75fa210479 | 28978 | 4d3638fe6ae8793b937d4c7f57a4c092d59d41df94991722d8b622ed958e576e |
| WEJ: complete posterior source/endpoint contract | da9d8461ca406a1c6f4b829a91147a860133567f | 59644 | 6b7644a978915550b5835b3492eda3bffde872b8e92f16c2db6c4538e405be8f |
| WMR: complete physical-mean reassembly | a7b23dea9a96dfab74475d382ca2d1df8edd5b8e | 31643 | 550866c05d9a07d3e4b037e5840a4f75b66a7f3a9304c5cd0d52e4f2b7e729a6 |

Before this draft, Newton independently checked the physical matrix transport, the ordered $E_{12}$ identity, the complete genuine potential correction and the three polynomial amplitudes. Tail independently returned to the complete WUA.14--15 and WUA.23 text and checked the same physical transport and flux, including the complete extended forcing. Tail also checked the normalized-circle primitive constants and the common-weight $L^1$ recurrence. These were pure formula checks, not evaluations of the proposed positive recipe.

The author has read the complete listed mathematical sources, the complete WGS actual pair, the complete two posterior nodes and the successful WMR result. Their saved scalar records and scope fields remain immutable. This draft does not represent the old failed posterior attempt as a successful attempt; it uses only its already completed named nodes through their exact identities.

The new numerical targets, if subsequently evaluated, are the complete normalized-weight angular envelopes, the full three forcing amplitudes, the full five-step terminal and $C_{F,s}^{\rm flux}$, followed by the complete reassembly of WMT8. Every terminal degree is retained. No value, improvement factor, passed numerical gate, feasible finite border or new scientific execution is claimed here.
