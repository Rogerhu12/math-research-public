# R133 supplement: explicit-family transfer of the complete finite part

2026-11-14, visible-exact-astra-0df / phase_inverse.

**已证明（条件导数与有限部转移定理）：** the following complete derivative contract transfers the
finite part $\mathfrak X(0)$ to the selected R31 parameter in the
same explicit family $Q_\delta=\bar Q+\delta Z$,
$\nu_\delta=\nu_0+\delta$, at $\eta_0$. It uses the existing
3146 strict integration intervals, 169 scalar germs, complete compact
control cache, and the [actual full-frequency complex root norms](R133-supplement-actual-full-frequency-moving-root-budget.md). No scalar
germ, phase transport, or full response is regenerated. The named
public consumer supplies the numerical instantiation; this proof
does not invent its execution.

The complete numerical instantiation is still to be executed in the public
repository; this theorem asserts the stated bounds once their named input
inequalities are supplied. The previously completed inputs are linked below.

The object remains the finite part of $\Xi$. The actual root
connection coefficient, strong return remainder, and genuine PDE
background transfer are separate obligations, as specified in
[the directed return-word contract](R133-supplement-directed-return-word-and-root-first-coefficient-contract.md).

## 1. Exact parameter identities on the strict interval

Write $w$ for the fixed compact metric bump, supported on
$[1/20,9/50]$, and $R=10^{-8}$ for the complex parameter radius.
The original controlled metric is $E_0$; $b=a'/a$ is independent of
$\delta$. Put

$$
 Q=-K_0=q_0^2,\qquad T=\frac{b}{2E_0},\qquad
 \kappa=T w',\qquad W_\delta=Q-\delta\kappa.
                                                               \tag{D.1}
$$

The already proved complete compact-$T$ cache has SHA
ab5e8156fbaf50c80e944a15d68858d29419229e7ae10665b432cd1af593587d.
Its definition and use in the optical identities are retained in
[the original all-parameter source](../scripts/fourfold_codazzi_phase_all_delta_speed.py).
Direct differentiation of $E_\delta=E_0e^{\delta w}$ gives

$$
 K_\delta=e^{-\delta w}(K_0+\delta\kappa),\qquad
 \gamma_\delta=\gamma_0e^{\delta w/2},\qquad
 q_\delta=e^{-\delta w/2}\sqrt{W_\delta}.              \tag{D.2}
$$

The square root is the branch continuous from positive $q_0$. For
$m_\delta=m_0+\delta Z_m$ and $\eta_\delta=-\gamma_\delta m_\delta$,
the exact cancellation is

$$
 \eta_\delta q_\delta=-\gamma_0m_\delta\sqrt{W_\delta},\qquad
 \frac{q_\delta}{\eta_\delta}
      =-\frac{e^{-\delta w}\sqrt{W_\delta}}{\gamma_0m_\delta}.
                                                               \tag{D.3}
$$

The logarithmic radial derivative used in the strict symbol is

$$
 \lambda_\delta:=\frac{(q_\delta)_r}{2q_\delta}
      =-\frac{\delta w'}4+\frac{Q'-\delta\kappa'}{4W_\delta},
 \qquad
 \partial_\delta\lambda_\delta
      =-\frac{w'}4+\frac{\kappa Q'-\kappa'Q}{4W_\delta^2}.
                                                               \tag{D.4}
$$

In particular the numerator in the second quotient has no remaining
$\delta$ term. Off the actual compact support, $w,\kappa$ and all
their derivatives here are exactly zero. The formulas do not charge
a false metric-parameter singularity near the root.

For the complete physical states, define

$$
 L_\delta=\lambda_\delta+
          b(1+u_\delta^2+q_\delta^2v_\delta^2),\qquad
 C_\delta^{uv}=u_\delta(v_\delta)_\phi
                              -v_\delta(u_\delta)_\phi.
$$

The exact same density as in the actual finite-part computation is

$$
 \Xi_\delta=\frac{L_\delta^2}{\eta_\delta q_\delta}
       -4b^2\frac{q_\delta}{\eta_\delta}u_\delta^2v_\delta^2
       -2bq_\delta C_\delta^{uv}.                    \tag{D.5}
$$

All three terms are required. In particular the last term has no
factor $\eta_\delta^{-1}$.

## 2. A complete cellwise parameter derivative bound

On one real radial interval use complete ordinary Wiener bounds
$U,U_1,V,V_1$ for $u_\delta,(u_\delta)_\phi,v_\delta,(v_\delta)_\phi$
on the whole parameter disk. Use $Z_u,Z_{u1},Z_v,Z_{v1},Z_m$ for
the complete direction and its mean. Let

$$
 Q_-\leq Q\leq Q_+,\quad |Q'|\leq Q_1,\quad
 |\kappa|\leq\kappa_0,\quad |\kappa'|\leq\kappa_1,\quad
 |w^{(j)}|\leq H_j,\quad |b|\leq b_*,\quad
 \gamma_0\geq\gamma_->0,\quad |m_\delta|\geq M>0.
                                                               \tag{D.6}
$$

The [complete direction native](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md) provides these state norms on
the whole negative interval. Its positive-strip Wiener bounds also
bound the ordinary Wiener norm used here. Set

$$
\begin{split}
 W_-&=Q_- -R\kappa_0>0,& W_+&=Q_++R\kappa_0,\\
 q_+&=e^{RH_0/2}\sqrt{W_+},& Q_\delta^+&=e^{RH_0}W_+,\\
 \dot Q_\delta^+&=e^{RH_0}(\kappa_0+H_0W_+),\\
 \Lambda&=RH_1/4+(Q_1+R\kappa_1)/(4W_-),\\
 \dot\Lambda&=H_1/4+(\kappa_0Q_1+\kappa_1Q_+)/(4W_-^2),\\
 L_*&=\Lambda+b_*(1+U^2+Q_\delta^+V^2),\\
 \dot L_*&=\dot\Lambda+b_*(2UZ_u+\dot Q_\delta^+V^2
                                           +2Q_\delta^+VZ_v).
                                                               \tag{D.7}
\end{split}
$$

Dots in these bounds denote a parameter derivative, not a radial
derivative. Define further

$$
\begin{split}
 J_*&=(\gamma_-M\sqrt{W_-})^{-1},&
 j_*&=Z_m/M+\kappa_0/(2W_-),\\
 R_*&=e^{RH_0}\sqrt{W_+}/(\gamma_-M),&
 r_*^{\rm log}&=H_0+\kappa_0/(2W_-)+Z_m/M,\\
 q_*^{\rm log}&=(H_0+\kappa_0/W_-)/2,\\
 C_*&=UV_1+VU_1,\\
 \dot C_*&=Z_uV_1+UZ_{v1}+Z_vU_1+VZ_{u1}.
                                                               \tag{D.8}
\end{split}
$$

Here $r_*^{\rm log}$ is only the indicated logarithmic bound and is
not the physical turning radius. Equations (D.2)--(D.4), the product
rule and the complete Wiener algebra give

$$
\boxed{
\begin{split}
 \|\partial_\delta\Xi_\delta\|_{\mathcal A_0}\leq\mathcal D={}&
 J_*(2L_*\dot L_*+L_*^2j_*)\\
 &+4b_*^2R_*\{U^2V^2r_*^{\rm log}
                       +2UZ_uV^2+2U^2VZ_v\}\\
 &+2b_*q_+(\dot C_*+q_*^{\rm log}C_*).
\end{split}}                                                     \tag{D.9}
$$

This estimates the entire angular function before taking its mean.
The full even mean affects $M$ and $Z_m$ and has not been removed.

The existing 3146 accepted strict intervals partition exactly
$[0,r_c]$. On each, the existing scalar Taylor identity supplies
$b,K_0,K_0',\gamma_0$. On the compact support the existing $T,T'$
models supply $\kappa,\kappa'$. The bump is an exact polynomial on
its support; its first two derivatives are evaluated before absolute
values are taken. Restriction uses the saved point jets and complete
seventh derivative, not a derivative of a uniform error ball. Hence

$$
 \left|\partial_\delta\int_0^{r_c}
                         \langle\Xi_\delta\rangle\,dr\right|
       \leq L_{\rm strict}:=\sum_J |J|\,\mathcal D_J. \tag{D.10}
$$

The final bound includes every accepted interval. The source hashes
and scalar-germ membership are checked anew, while their mathematical
contents are reused.

## 3. Root derivative without differentiating a divergent integral

The compact bump vanishes on the entire root germ. The intrinsic
root $r_*$ and $K,b,\gamma$ are therefore exactly independent of
$\delta$ there. Put $\rho=r_*-r$ and $K=-\rho k(\rho)$.
The full root decomposition is

$$
 \langle\Xi_\delta\rangle
   =A_\delta\rho^{-5/2}+B_\delta\rho^{-3/2}
                      +C_\delta\rho^{-1/2}-D_\delta\rho^{1/2},
                                                               \tag{D.11}
$$

where, with $a_0=k_\rho/(4k)-b(1+u_\delta^2+\rho k v_\delta^2)$,

$$
\begin{split}
 A_\delta&=(16\eta_\delta\sqrt k)^{-1},&
 B_\delta&=\langle a_0\rangle/(2\eta_\delta\sqrt k),\\
 C_\delta&=\langle a_0^2\rangle/(\eta_\delta\sqrt k),\\
 D_\delta&=4b^2\sqrt k\,\langle u_\delta^2v_\delta^2\rangle/\eta_\delta
          +2b\sqrt k\,\langle C_\delta^{uv}\rangle.
                                                               \tag{D.12}
\end{split}
$$

These four coefficients are holomorphic in the product of the actual
root disk $|\rho|\leq R_r=10^{-5}$ and $|\delta|\leq R$.
Nonzero $k,\gamma,m_\delta$ follow from the complete complex native
and the actual full moving root inverse budget. The latter includes
the exact background repair and all 193 repaired direction states.

On the outer root disk, $k(\rho)=\int_0^1K_0'(r_*-t\rho)\,dt$.
Thus the original complex $K_0'$ native gives
$\operatorname{Re}k\geq k_->0$ and $|k|\leq k_+$. It also gives
the smaller centered bound $|k-60|\leq M_k$, by integrating the
complete complex enclosure of $K_0'-60$. For any $H<R_0<R_r$,
where $H=r_*-r_c$, Cauchy implies

$$
            |k_\rho|\leq M_k/(R_r-R_0)
                    \quad (|\rho|\leq R_0).           \tag{D.13}
$$

No unprovided $K_0''$ interval is inferred from the real $K_0'$ bound.
The estimate uses the full complex disk and its declared radius.

Use the full complex root norms $U,V,U_1,V_1,Z_u,Z_v,Z_{u1},Z_{v1}$,
$M\leq|m_\delta|$, $Z_m$, and $e_*\geq|\eta_\delta^{-1}|$. Put

$$
 a_*={M_k\over4k_-(R_r-R_0)}
             +b_*(1+U^2+R_0k_+V^2),\qquad
 \dot a_*=2b_*(UZ_u+R_0k_+VZ_v),\qquad z_*=Z_m/M.
                                                               \tag{D.14}
$$

Since $k,b,\gamma$ do not vary with $\delta$ on this germ,
the following are complete product-disk bounds:

$$
\begin{split}
 M_A&={e_*z_*\over16\sqrt{k_-}},\\
 M_B&={e_*\over2\sqrt{k_-}}(\dot a_*+a_*z_*),\\
 M_C&={e_*\over\sqrt{k_-}}(2a_*\dot a_*+a_*^2z_*),\\
 M_D&=4b_*^2\sqrt{k_+}e_*
       (U^2V^2z_*+2UZ_uV^2+2U^2VZ_v)
           +2b_*\sqrt{k_+}\dot C_*.
                                                               \tag{D.15}
\end{split}
$$

They bound respectively $|\partial_\delta A|$,
$|\partial_\delta B|$, $|\partial_\delta C|$ and
$|\partial_\delta D|$. The second summand of $M_D$ has no $e_*$
factor, consistently with the second summand of $D$ in (D.12).

For a holomorphic $F$ with $|F|\leq M_F$ on $|\rho|\leq R_0$,
the coefficient Cauchy bounds give

$$
 |F(\rho)-F(0)-\rho F'(0)|
       \leq {M_F\rho^2\over R_0^2(1-\rho/R_0)},\quad
 |F(\rho)-F(0)|
       \leq {M_F\rho\over R_0(1-\rho/R_0)}.           \tag{D.16}
$$

Apply these to $\partial_\delta A$ and $\partial_\delta B$.
The exact finite-part antiderivatives, with both nonintegrable
coefficients subtracted, give the uniform bound

$$
\boxed{
\begin{split}
 L_{\rm root}(R_0)={}&M_A\left\{
       {2\over3H^{3/2}}+{2\over R_0\sqrt H}
       +{2\sqrt H\over R_0^2(1-H/R_0)}\right\}\\
 &+M_B\left\{{2\over\sqrt H}
       +{2\sqrt H\over R_0(1-H/R_0)}\right\}
       +2M_C\sqrt H+{2\over3}M_DH^{3/2}.
\end{split}}                                                     \tag{D.17}
$$

With an interval for $H$, the negative powers use its lower endpoint
and positive powers and $H/R_0$ use its upper endpoint. In particular
the root-refinement interval is not silently replaced by its midpoint.
Taking the smallest of several separately valid choices of $R_0$
preserves the proof.

The subtracted remainders in (D.16) are integrable uniformly in the
parameter disk. Differentiation under their ordinary integrals is
therefore justified. This proves the bound for the derivative of the
finite part itself, without differentiating an unrenormalized
divergent integral.

## 4. Selected-parameter and arithmetic contracts

For every $|\delta|\leq R$, (D.10) and (D.17) imply

$$
 \boxed{\quad
 |\mathfrak X(\delta)-\mathfrak X(0)|
       \leq |\delta|\bigl(L_{\rm strict}
                         +\min_{R_0}L_{\rm root}(R_0)\bigr).
 \quad}                                                        \tag{D.18}
$$

Use the actual selected R31 parameter bound from its successful
strip-refinement native, not a proposed floating parameter step.
Adding the right side of (D.18), outwardly, to the [actual complete
v2 finite-part interval](R133-supplement-actual-complete-moving-first-symbol-finite-part.md) gives a true enclosure for this same
explicit-family $\mathfrak X(\delta_*)$. Dividing by $-4$ gives the
corresponding directed-word arithmetic multiple.

The genuine returned coefficient may additionally contain
$-b_{\rm root}^{\rm fin}/4$ and other retained declared interfaces.
Neither the finite-part transfer nor an arithmetic check of its
multiple pays those terms. A subsequent genuine PDE background
transfer is also required. The numerical consumer records all these
scope restrictions explicitly.
