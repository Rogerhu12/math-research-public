# R144 supplement: raw moving holonomy sources and their complete weak pairing

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

**Proved.** The bulk scalar in the
[R144 boundary-row identity](R144-fourfold-holonomy-transfers-outer-mean-to-waist.md)
can be evaluated directly on the complete raw moving residual, including
its even mean. Its dual weight has an explicit $H^1_\phi$ bound using
only the moving state's angular $L^2$ norms and its true mean gap.
No angular derivative of the background, no division by pointwise
$v^2$, and no division by $K$ is needed for this scalar functional.

The formula also includes the derivative of the weights at an off-shell
selected centre. It therefore does not identify a saved proposal with a
true response. This is a scalar source contract in the named angle and
measure, not a complete BVP inverse or a free conversion of other source
ports.

## 1. The same complete moving residual and frame

Keep $e=\sqrt E$, $\gamma=e/a$, $\beta=a'/a$, $b=a'/e=\beta/\gamma$,
and the actual metric identity
$$
             \beta'=\beta\gamma'/\gamma-a^2\gamma^2K.
 \tag{MH.1}
$$
All angular functions have period $L=\pi/2$. The means below are
$\langle f\rangle=L^{-1}\int_0^L f\,d\phi$. Retain
$$
 m=\langle v\rangle<0,\quad j=v/m,\quad\langle j\rangle=1,\quad
 S=u^2+Kv^2,\quad d=-\beta I_\phi S.
$$
Use the complete residual convention
$$
 \begin{split}
 u_r&=d u_\phi+\gamma mK v_\phi-\beta u(1+S)+R_u,\\
 v_r&=d v_\phi-\gamma m u_\phi+\beta v(1-S)+R_v,\qquad
 R_0=\langle R_v\rangle.
 \end{split}
 \tag{MH.2}
$$
The first row is odd and the second even, as in the original problem.
Taking the second mean gives, without approximation,
$$
                         m'=\beta m(1-\langle S\rangle)+R_0.
 \tag{MH.3}
$$
The complete source and sign conventions are those of the
[moving-frame residual theorem](R133-supplement-moving-frame-with-complete-residual-and-mean.md),
equations (2)--(8).

For clarity define
$$
 \Omega(x,y,z)=\begin{pmatrix}0&-x&-y\\x&0&-z\\y&z&0\end{pmatrix}.
$$
The complete moving angular connection is
$$
 \Omega_\phi=\Omega(bj,au/m,a/m)=[n]_\times,\qquad
                       n=(a/m,-au/m,bj).
 \tag{MH.4}
$$
Write $\tau=dj-\gamma u$. The corresponding algebraic radial connection is
$$
 \Omega_r=\Omega(p,q,t),\qquad
 p=b\tau,\quad q=a(\gamma Kv+du/m),\quad t=ad/m.
 \tag{MH.5}
$$
For exact solutions this is the actual transformed frame connection.
For off-shell states it is the explicit algebraic connection in the
cited theorem. We do not replace the actual off-shell chart derivative
by its zero-residual value.

Using (MH.1)--(MH.3) and
$d_\phi=-\beta(S-\langle S\rangle)$, the already proved complete
curvature identity reads
$$
 \partial_r\Omega_\phi-\partial_\phi\Omega_r+
              [\Omega_r,\Omega_\phi]=[f]_\times,
$$
$$
 \boxed{\quad
 f=\left(
 -\frac{a}{m^2}R_0,\
 -\frac a m\left(R_u-\frac u mR_0\right),\
 \frac b m(R_v-jR_0)
 \right).
 \quad}
 \tag{MH.6}
$$
In particular the mean source has three contributions, not zero.

Let $U_r(s,t)$ be right angular transport for (MH.4), and
$Q(r)=U_r(0,L)$. The true material lift satisfies
$\Theta_\phi=j$, $\Theta(0)=0$, $\Theta(L)=L$ whenever the original
$v<0$ chart is valid. Since (MH.4) is exactly the angular pullback of
the physical connection, its $Q$ is the physical quarter transport.
This statement needs no radial equation and holds off shell.

The same transport differentiation as in R144 gives
$$
 \frac d{dr}\operatorname{tr}Q(r)
 =\int_0^L\operatorname{tr}
          \bigl(U_r(0,\phi)[f(r,\phi)]_\times U_r(\phi,L)\bigr)\,d\phi.
 \tag{MH.7}
$$
The algebraic radial connection (MH.5) contributes only a commutator
after taking trace. Thus (MH.7) computes precisely R144's scalar
$\mathcal I$, with its one-sided jumps retained. It does not assert that
the off-shell radial frame or position is an exact immersion.

## 2. The exact dual weight, including the raw even mean

At fixed $r$ set
$$
 W(\phi)=U_r(\phi,L)U_r(0,\phi),\qquad
 k(\phi)=-2\,\operatorname{axl}(\operatorname{skew}W(\phi)),
 \tag{MH.8}
$$
where $[\operatorname{axl}H]_\times=H$ for a skew $3$-matrix.
For every $z\in\mathbb R^3$,
$$
 \operatorname{tr}([z]_\times W)=k\cdot z,\qquad |k|\le2.
 \tag{MH.9}
$$
The latter follows because $W\in SO(3)$.
Moreover
$$
 W=U_r(0,\phi)^{-1}Q(r)U_r(0,\phi),\qquad
                         k_\phi=k\times n.
 \tag{MH.10}
$$
Indeed $W_\phi=WN-NW$ for $N=[n]_\times$; taking its skew part proves
the second identity. The values of $W$, and therefore $k$, at $0,L$
coincide.

Put
$$
 A=a/m,\qquad D=b/m,\qquad E=a/m^2>0,\qquad \widehat u=u/m.
$$
Do not confuse these scalar coefficients with physical second
fundamental-form entries. In this supplement they occur only in the
following formulas. Define
$$
 \begin{split}
 \lambda&=\langle-Ek_1+A\widehat u k_2-Djk_3\rangle,\\
 w_u&=-Ak_2,\qquad w_v=Dk_3+\lambda.
 \end{split}
 \tag{MH.11}
$$
Substituting (MH.6) and $R_0=\langle R_v\rangle$ into (MH.7) gives the
complete exact functional
$$
 \boxed{\quad
 \frac d{dr}\operatorname{tr}Q(r)
             =L\langle w_uR_u+w_vR_v\rangle.
 \quad}
 \tag{MH.12}
$$
The constant $\lambda$ is the retained mean functional. Omitting it
would change the scalar equation.

If the state is continuous across all original radial interfaces,
there are no jump terms. In general
$$
 \mathcal I=L\int_0^R\langle w_uR_u+w_vR_v\rangle\,dr
                         +\sum_i[\operatorname{tr}Q]_{r_i}.
 \tag{MH.13}
$$
For continuous metric germs, a complete ordinary jump bound is
$$
 |[\operatorname{tr}Q]_i|
 \le2L\left(
 a_i^2|\Delta(1/m)|^2+
 a_i^2\|\Delta(u/m)\|_2^2+
 b_i^2\|\Delta j\|_2^2
 \right)^{1/2}.
 \tag{MH.14}
$$
This is Duhamel applied to the exact difference of (MH.4). Each ratio
uses its own one-sided mean. Neither the mean jump nor a chart jump is
replaced by zero.

At the waist, $b(0)=0$. The R144 waist error can also be bounded directly:
$$
            |\mathcal E_w|\le\frac{2La_0}{|m_0|}\|u(0)\|_2.
 \tag{MH.15}
$$
Here setting $u(0)=0$ in (MH.4) leaves the constant connection
$[(a_0/m_0,0,0)]_\times$. Thus (MH.15) is the same geometric error as in
R144, expressed in moving coordinates. Pointwise negativity of $v$
is still needed for the physical chart and later curvature/reach claims;
it is not needed as a denominator in this estimate.

## 3. An explicit full $H^{-1}$ source contract

Use the normalized periodic norms
$$
 \|q\|_{H^1_\phi}^2=\langle|q|^2+|q_\phi|^2\rangle
       =\sum_{\ell\in4\mathbb Z}(1+\ell^2)|\widehat q_\ell|^2,
$$
and let $H^{-1}_\phi$ be the dual with respect to normalized mean.
For pairs use the Hilbert direct-sum norm. These norms retain the mean.

Set
$$
 U_*=\|\widehat u\|_2,\qquad J_*=\|j-1\|_2,\qquad
 \mu=\|n\|_2
     =\left(A^2(1+\|u\|_2^2)+b^2\|j\|_2^2\right)^{1/2},
$$
$$
 S_*=E+|A|U_*+|D|J_*,
$$
$$
 M_{-1}=2\left(
 A^2+D^2+S_*^2+\max(A^2,D^2)\mu^2
 \right)^{1/2}.
 \tag{MH.16}
$$

**Lemma MH.1.** The complete weight satisfies
$$
                 \|(w_u,w_v)\|_{H^1_\phi,\mathrm{pair}}\le M_{-1}.
 \tag{MH.17}
$$
Consequently, for the same moving coordinate and ordinary radial measure,
$$
 \left|\mathcal I_{\rm bulk}\right|
 \le L\int_0^R M_{-1}(r)\|(R_u,R_v)\|_{H^{-1}_\phi,\mathrm{pair}}\,dr,
 \tag{MH.18}
$$
and, if $M_{-1}\in L^2_r$,
$$
 \left|\mathcal I_{\rm bulk}\right|
 \le L\|M_{-1}\|_{L^2(dr)}
           \|(R_u,R_v)\|_{L^2(dr;H^{-1}_\phi),\mathrm{pair}}.
 \tag{MH.19}
$$

**Proof.** Write
$$
 w_v=D(k_3-\langle k_3\rangle)+\eta,\qquad
 \eta=\langle-Ek_1+A\widehat u k_2-D(j-1)k_3\rangle.
$$
Since $|k|\le2$, one has $|\eta|\le2S_*$,
$\|w_u\|_2\le2|A|$, and
$$
 \|w_v\|_2^2
 =D^2\|k_3-\langle k_3\rangle\|_2^2+|\eta|^2
 \le4D^2+4S_*^2.
$$
The mean term is angularly constant. By (MH.10),
$$
 \|(w_u,w_v)_\phi\|_2^2
 \le\max(A^2,D^2)\|k_\phi\|_2^2
 \le4\max(A^2,D^2)\mu^2.
$$
These prove (MH.17), and duality gives (MH.18)--(MH.19).
The proof extends to $u,j\in L^2_\phi$ as a statement about the fixed
transport weight: the angular connection is integrable, its transport
is absolutely continuous and orthogonal, and $k_\phi\in L^2$.
No derivative of $u$ or $j$ has been taken. The original nonlinear
curvature identity is first used for the sufficiently regular state
for which it is defined. Its linear source functional then has the
displayed weak extension. $\square$

The constants have no $1/K$ singularity at the turning circle. They
also have no pointwise $1/v$ singularity. They still contain the genuine
mean denominators and all mean-rank terms.

This proves the scalar pairing in (MH.18) for its stated spaces only.
A different radial density, a different angular coordinate, an
anisotropic source norm, or a negative-side natural port must first
be converted with its actual bounded map. The estimate is not the
missing inverse for the entire differential system.

## 4. The off-shell derivative keeps the changing weights

The weight itself depends on the state and metric. For a differentiable
family, let dots denote its derivative at any base, including an
approximate one. Duhamel and orthogonality give
$$
 \|\dot k\|_\infty\le2L\|\dot n\|_2,\qquad
 \|\dot k\|_{H^1}\le
 2\bigl(L^2+(1+L\mu)^2\bigr)^{1/2}\|\dot n\|_2.
 \tag{MH.20}
$$
Indeed the two transport factors in $W$ cover disjoint subintervals,
whose total length is $L$. Hence
$\|\dot W\|_{\rm op}\le\int_0^L|\dot n|\,d\phi$.
Taking skew part and axial vector gives the first bound.
Differentiating $k_\phi=k\times n$ then gives
$\|\dot k_\phi\|_2\le2(1+L\mu)\|\dot n\|_2$.

The required complete axial variation is
$$
 \dot n=(\dot A,-\dot A\,u-A\dot u,\dot b\,j+b\dot j).
 \tag{MH.21}
$$
For fixed $a$, $z=\dot m$ gives
$\dot A=-Az/m$, $\dot j=\dot v/m-jz/m$.
Metric contributions to $\dot b$ remain. No fixed-centre coordinate
derivative is identified with the physical one without its true chart.

For an explicit quantitative bound put
$$
 T_*=|\dot E|+|\dot A|U_*+|A|\|\dot{\widehat u}\|_2
                   +|\dot D|J_*+|D|\|\dot j\|_2.
$$
The exact derivative of $\eta$ gives
$$
 |\dot\eta|\le2T_*+2LS_*\|\dot n\|_2.
$$
Since the nonmean projection is an $H^1$ contraction,
$$
 \begin{split}
 \|\dot w\|_{H^1,\mathrm{pair}}
 \le{}&2(\dot A^2+\dot D^2)^{1/2}(1+\mu^2)^{1/2}\\
 &+2(A^2+D^2)^{1/2}
          \bigl(L^2+(1+L\mu)^2\bigr)^{1/2}\|\dot n\|_2\\
 &+2T_*+2LS_*\|\dot n\|_2.
 \end{split}
 \tag{MH.22}
$$
Every term comes from differentiating the full weight, including its
mean component. This estimate again uses no angular state derivative.

On the original exactly continuous selected family
$Q_\delta=Q_0+\delta Z$, $\nu_\delta=\nu_0+\delta$, use the complete
ordinary residuals of the
[selected-centre source theorem](R133-supplement-selected-centre-complete-residual-and-collar-source-bounds.md):
$$
 f_\delta=(Q_\delta)_r-\mathcal F(Q_\delta,\nu_\delta),\qquad
 \partial_\delta f_\delta=-s_\delta.
$$
There are no value-jump terms for these exactly continuous fields.
Thus (MH.13) differentiates to
$$
 \boxed{\quad
 \partial_\delta\mathcal I
   =L\int_0^R\left\{
       \langle\partial_\delta w_\delta,f_\delta\rangle
                         -\langle w_\delta,s_\delta\rangle
               \right\}\,dr.
 \quad}
 \tag{MH.23}
$$
Both ordinary or weak pairings can use the corresponding bounds above
in the same units. The first term is present because the selected
centre is off shell. Compact support of the explicit metric bump does
not remove it, and a small saved exterior residual does not remove it.

At a genuine solution $f=0$, (MH.23) reduces to the usual true-solution
row derivative. This is exactly the distinction required in R144:
zero-set differentiation is valid at the zero set, while a forced
proposal pays its full sources and weight variations.

## 5. Scope

Equations (MH.12)--(MH.23) supply an exact raw-source form of the
holonomy scalar and an explicit weak extension, including its mean,
interfaces and off-shell parameter differentiation. They can be
combined with R144's separately proved waist and outer identities.
They do not waive the physical outer-neighbourhood gate, its
$\mathcal B^{-1}$ fee, or the correct conversion of independent
boundary/height ports. No full nonlinear core or visible closed
isometric family is claimed.
