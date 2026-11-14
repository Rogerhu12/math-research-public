# R133 supplement: passive physical Jacobi, positive Dirac splitting, and complete Schur source

2026-11-13, visible-exact / phase_inverse. **Exact structural theorem
proved.** The coordinate identities below apply to the current complete
moving candidate, including at an approximate centre with nonzero PDE
residual. The positive high-block inverse is a quantitative theorem
under its displayed coefficient and interface gates. Those gates must
be evaluated on the intended positive interval and current centre; no
uncomputed final-centre cutoff or full body inverse is asserted.

The result retains the complete finite angular head, both means, all
head/high couplings, ordinary source, and exact PPoly interface maps.
In particular it never divides a small positive-barrier transmission.

## 1. Passive pullback is distinct from varying the moving coordinate

Let the exact moving centre fields be $u(r,\phi),v(r,\phi)$, with
$m(r)=\langle v\rangle_\phi<0$, $v<0$. Its exact physical angle is

$$
 \theta(r,\phi)=\phi+\frac1m I_\phi(v-m),\qquad
 j=\theta_\phi=v/m>0.                                      \tag{D.1}
$$

Here $I_\phi$ is the complete mean-zero primitive on the fourfold
circle of length $L=\pi/2$. All statements are on intervals where this
genuine circle map is defined. At the current root the jointly complex
version was separately proved; here a real circle diffeomorphism is
enough.

Let $h$ be the variation in the **original physical-angle equation**.
We take only the passive pullback
$\widetilde h(r,\phi)=h(r,\theta(r,\phi))$. This is not the variation of
the moving unknown, and there is no variation of the coordinate in
this definition. Thus its equation follows by the ordinary chain rule
even when the centre does not solve the PDE.

After $y=R\widetilde h$, $R=\operatorname{diag}(-1,1)$, the complete
equation is

$$
 y_r=(\delta I+\eta J(K))y_\phi+\widetilde L y+R\widetilde f,\quad
 \eta=-\gamma m>0,\quad
 \delta=\frac{m}{v}(\gamma u+\theta_r),\quad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.                \tag{D.2}
$$

The original physical coefficient matrix, evaluated after pullback,
is

$$
\begin{gathered}
 g=\gamma v_\theta-2\beta uv,\\
 L_{11}=\gamma u_\theta-\beta(1+3u^2+Kv^2),\qquad
 L_{22}=-\gamma u_\theta+\beta(1-u^2-3Kv^2),\\
 \widetilde L=\begin{pmatrix}L_{11}&-Kg\\-g&L_{22}\end{pmatrix},
 \qquad \partial_\theta=(m/v)\partial_\phi .
\end{gathered}                                                        \tag{D.3}
$$

Both off-diagonal signs in $\widetilde L$ arise from the reflection
$R$. In particular $\widetilde L_{12}=K\widetilde L_{21}$ exactly.

Most importantly, $\eta J(K)$ in (D.2) is radial. The true common
drift $\delta$ is retained. Removing $\delta$ by a separate angular
flow would generally restore angular dependence in the other
principal coefficient, and is not done here.

## 2. The exact approximate-centre drift includes the full residual mean

Let
$d=-\beta I_\phi(u^2+Kv^2)$ be the drift in the exact moving nonlinear
system, and let $R_v$ be its complete **physical, unnormalized** second
residual. Write $z_R=\langle R_v\rangle_\phi$. Exact differentiation of
(D.1), using the full moving equation plus its residual, gives

$$
 \theta_r=-\gamma u+\frac{d}{m}v+
     \frac1m I_\phi\left(R_v-\frac{z_Rv}{m}\right),\qquad
 \delta=d+\chi_R,\quad
 \chi_R=\frac1v I_\phi\left(R_v-\frac{z_Rv}{m}\right).       \tag{D.4}
$$

The argument of $I_\phi$ has mean exactly zero. Also

$$
 (\chi_R)_\phi=\frac{R_v}{v}-\frac{z_R}{m}
                         -\frac{v_\phi}{v}\chi_R .        \tag{D.5}
$$

Thus actual complete $A^0/A^1$ residual bounds may be used to pay the
true drift and its derivative. It is not permissible to set
$\delta=d$ at an approximate centre. If a solver records normalized
$V$ residuals, its full physical $v=s+\alpha V$ residual must first be
formed, including the $s'$ term and the correct factor $\alpha$.
The exact source column $z_R$ is not projected away.

Equations (D.2)–(D.5) are passive-coordinate identities. They do not
delete the nonlocal term that appears when the **moving unknown
itself** is varied. The separate residual-sensitive moving-variation
bridge remains necessary when that different variable is supplied as
an input.

## 3. Positive half-density Dirac equation and physical norm

Now restrict to a genuine strictly positive interval $K(r)>0$ and put
$q=\sqrt K$, $Q=\operatorname{diag}(1,q)$,
$J_0=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
Use the complete half-density state

$$w=\sqrt j\,Qy,\qquad \alpha_r:=\eta q>0.                \tag{D.6}$$

The subscript on $\alpha_r$ labels the radial coefficient, not a
derivative or the deformation amplitude. In particular
$\alpha_r=-\gamma m\sqrt K$.

At each physical constant-$r$ circle,

$$
 \|w(r)\|_{L^2_\phi}=\|Q(r)h(r)\|_{L^2_\theta},\qquad
 F=\sqrt j\,QR\,f(r,\theta(r,\phi)),\quad
 \|F(r)\|_2=\|Q(r)f(r)\|_{L^2_\theta}.                    \tag{D.7}
$$

These are exact measure identities. When an ordinary physical norm is
required, the factors $\max(1,q)$ or $\max(1,q^{-1})$ are written
explicitly. This strict-positive theorem does not extend them
unpaid through $q=0$; the separately proved actual Airy ports are the
turning interface.

Direct differentiation gives

$$
 w_r=\alpha_r J_0\partial_\phi w+S w+Vw+F,                \tag{D.8}
$$

where

$$
\begin{aligned}
 S&=\delta\partial_\phi+\frac12\delta_\phi I
                     +\frac{\gamma qv_\theta}{2}J_0,\\
 V&=Q\widetilde LQ^{-1}
       +\operatorname{diag}(0,q'/q)-\frac{\gamma u_\theta}{2}I .
\end{aligned}                                                        \tag{D.9}
$$

$S$ is exactly skew-adjoint on the full real circle and $V$ is a
real symmetric multiplication matrix. To verify the cancellation in
(D.9), before splitting $S$ the additional half-density matrix is

$$
 \tfrac12(j_r/j-\delta j_\phi/j)I
                         -\tfrac12\alpha_rJ_0j_\phi/j .
$$

The exact identity $\theta_r=\delta j-\gamma u$ gives
$j_r/j-\delta j_\phi/j-\delta_\phi=-\gamma u_\theta$.
Also $\alpha_rj_\phi/j=-\gamma qv_\theta$. Substituting gives
(D.9), without using the PDE or setting its residual to zero.
This removes an unnecessary separate bound for $j_r$ from the
Hermitian energy cost.

Let $D_\phi=-i\partial_\phi$, and $\mathcal C=iJ_0$.
$\mathcal C$ is a constant Hermitian involution. The principal term is
$\alpha_r\mathcal C D_\phi$. Its two nonzero-frequency spectral
branches are real and have absolute size $\alpha_r|n|$ for the full
physical frequencies $n\in4\mathbb Z$.

## 4. Every frequency, both means, and bounded cross-cone coupling

Choose a physical cutoff $N\in4\mathbb N$. Set
$P_H={\bf1}_{|D_\phi|\ge N}$ and $P_L=I-P_H$.
Both mean states are in $P_L$.
Inside $P_H$, define the constant orthogonal projectors
$\Pi_s={\bf1}_{\mathcal C D_\phi\le-N}$ and
$\Pi_u={\bf1}_{\mathcal C D_\phi\ge N}$.
Stable data are imposed at the left endpoint and unstable data at the
right endpoint. The full finite angular head is retained separately.

Write

$$
 b(r)=\|V(r)\|_{L^\infty\to L^\infty},\quad
 a_1(r)=\sum_{k\in4\mathbb Z}|k|\,|\widehat\delta(k,r)|,\quad
 c_0(r)=\tfrac12|\gamma q|\,\|v_\theta\|_\infty.            \tag{D.10}
$$

A complete proved upper bound for $a_1$ is required; samples or a
finite retained part are insufficient.

There is a useful full cross-cone estimate. The Fourier matrix of
$\delta\partial_\phi+\delta_\phi/2$ is

$$
 \frac i2(n+\ell)\widehat\delta(n-\ell).                  \tag{D.11}
$$

Since this scalar operator commutes with $\mathcal C$, a stable to
unstable matrix entry has opposite signs of $n$ and $\ell$. Therefore
$|n+\ell|\le|n-\ell|$. Complete convolution and Young's inequality give

$$
 \|\Pi_s(\delta\partial_\phi+\delta_\phi/2)\Pi_u\|,
 \ \|\Pi_u(\delta\partial_\phi+\delta_\phi/2)\Pi_s\|
                         \le a_1/2 .                    \tag{D.12}
$$

The last skew multiplication in $S$ contributes at most $c_0$.
Hence the complete off-diagonal high coupling has norm at most

$$k(r)=b(r)+a_1(r)/2+c_0(r).                              \tag{D.13}$$

No factor $N\|\delta\|$ has been charged to this cross-cone operator,
and no modes crossing the finite angular head have been discarded.
The latter are the exact head/high operators below.

The two unprojected means are also explicit. Let
$C_0=S-\delta\partial_\phi+V$ denote the ordinary zero-order matrix in
(D.8), and write $w=w_0+w_{\ne0}$. Then

$$
 w_0'=\langle C_0\rangle w_0+
       \langle(C_0-\delta_\phi I)w_{\ne0}\rangle+F_0.       \tag{D.14}
$$

The nonzero equation has mean-driven column
$P_{\ne0}C_0w_0$. Both rows of (D.14) are retained.
The original physical mean is, in addition, the exact weighted
functional
$\langle h\rangle_\theta=\langle\sqrt j\,R Q^{-1}w\rangle_\phi$.
It is not identified with $w_0$.

## 5. Complete high two-port Green on a smooth positive interval

Let $I=[a,b]$ lie inside a smooth actual piece. Suppose that fully
proved bounds give

$$
 \lambda_*=\inf_I[N\alpha_r-b(r)]>0,\qquad
 k_*=\sup_Ik(r)<\lambda_* .                              \tag{D.15}
$$

The diagonal stable generator is
$-\alpha_r|D_\phi|+\Pi_sS\Pi_s+\Pi_sV\Pi_s$; the unstable generator is
the corresponding positive branch. Each compression of $S$ remains
exactly skew-adjoint. Direct full Hilbert energy therefore gives

$$
 \|U_s(t,s)\|\le e^{-\lambda_*(t-s)}\quad(t\ge s),\qquad
 \|U_u(t,s)\|\le e^{-\lambda_*(s-t)}\quad(t\le s).           \tag{D.16}
$$

These propagators can be constructed by Fourier Galerkin within each
complete cone. The projected skew terms retain their exact energy
identity. The resulting uniform estimates and the differentiated
equation for smooth dense data give a weak limit and uniqueness;
density gives the bounded propagators on $L^2$. No finite Galerkin
inverse is used as the final infinite-dimensional inverse.

The diagonal two-port Green $G_0$ has full $L^2(I)$ norm at most
$1/\lambda_*$ by the two one-sided exponential kernels. Its two
independent Poisson columns, measured in the Euclidean direct sum of
the endpoint Hilbert spaces, have combined $L^2(I)$ norm at most
$(2\lambda_*)^{-1/2}$. The columns take values in orthogonal stable
and unstable spaces.

The off-diagonal coupling is bounded multiplication in $r$ of norm
at most $k_*$. Neumann inversion on the single full space
$L^2(I;P_HL^2)$ gives

$$
 \|G_H\|\le\frac1{\lambda_*-k_*},\qquad
 \|P_H^\partial\|\le
 \frac{1}{1-k_*/\lambda_*}\frac1{\sqrt{2\lambda_*}}.        \tag{D.17}
$$

All high Fourier modes remain. This also gives the full complementary
endpoint output:

$$
 \|w_s(b)\oplus w_u(a)\|
 \le e^{-\lambda_*|I|}\|g_s(a)\oplus g_u(b)\|
   +\frac{\|F_H\|_{L^2}+k_*\|w_H\|_{L^2}}
          {\sqrt{2\lambda_*}}.                           \tag{D.18}
$$

Thus both incoming and outgoing ports and both full source columns
are present. No inverse of a tiny transmission appears.

A sufficient explicit cutoff is any physical multiple of four for
which
$N\inf_I\alpha_r>2\sup_Ib+\sup_Ia_1/2+\sup_Ic_0$.
This is a checkable coefficient gate, not a claim that such a
particular cutoff has been numerically paid on the current centre.
The singular radial $q'/q$ term in (D.9) is kept in $b$ unless an
explicit radial Airy reference absorbs it. It must not be ignored
when approaching the turning point.

## 6. Exact finite-head and ordinary-source Schur reduction

Let $\mathcal A=\alpha_r\mathcal C D_\phi+\delta\partial_\phi+C_0$.
Keep the full operators

$$
 K_{HL}=P_H(\delta\partial_\phi+C_0)P_L,\qquad
 K_{LH}=P_L(\delta\partial_\phi+C_0)P_H.                   \tag{D.19}
$$

The radial principal coefficient commutes with both projections, so
it has no hidden head/high term. The two operators in (D.19) are
bounded:

$$
\begin{aligned}
 \|K_{HL}\|&\le N\|\delta\|_\infty+\|C_0\|_\infty,\\
 \|K_{LH}\|&\le N\|\delta\|_\infty+\|\delta_\phi\|_\infty
                                     +\|C_0\|_\infty .
\end{aligned}                                                        \tag{D.20}
$$

For the second estimate, take the adjoint and move the derivative onto
the finite head before applying the multiplier bound. The complete
operators, rather than only these sufficient norm bounds, are used
in the Schur equation. In particular the derivative vanishes on a
constant head input; the exact high mean-driven column is
$P_HC_0P_0$, not a fictitious $N\delta$ mean column.

With $\mathcal L_{LL}=\partial_r-P_L\mathcal A P_L$ the exact solution
formula is

$$
\begin{aligned}
 w_H&=P_H^\partial g_H+
               G_H(F_H+K_{HL}w_L),\\
 [\mathcal L_{LL}-K_{LH}G_HK_{HL}]w_L
 &=F_L+K_{LH}G_HF_H+K_{LH}P_H^\partial g_H .
\end{aligned}                                                        \tag{D.21}
$$

Every ordering in (D.21) matters. This is the complete finite angular
head, including both means; it is still a radial boundary-value
operator until its own validation is performed. The right side
retains the ordinary high source and both high endpoint columns.
Independent parameter-source columns are included in $F$ without
change. No derivative loss or mean convention is silently altered
in this elimination.

## 7. Exact PPoly interfaces and why bare pullback smallness is unnecessary

At a candidate join, the physical variation has its specified actual
jump (zero for the homogeneous continuous physical problem).
Let the two real angle maps be $\theta_\pm$, and set
$\chi=\theta_-^{-1}\circ\theta_+$. Since the intrinsic $K$ is the same
on both sides, $q$ is unchanged. The exact homogeneous half-density
interface is

$$
 w_+(\phi)=U_\chi w_-(\phi),\qquad
 U_\chi f=\sqrt{\chi'}\,f\circ\chi .                       \tag{D.22}
$$

$U_\chi$ is exactly unitary on the whole angular Hilbert space.
An ordinary physical jump $a(\theta)$ adds
$\sqrt{j_+}QR\,a\circ\theta_+$, with exactly its physical $Q$-weighted
norm. Means and source jumps are not removed.

Unitarity alone does not justify a dichotomy connection: a general
unitary could exchange stable and unstable spaces. Here the actual
circle map permits a quantitative **cross-cone** bound, without
claiming that $U_\chi-I$ is small on the full space.

Assume
$\epsilon=\|\chi'-1\|_\infty\le1/2$ and
$M_2=\|\chi''\|_\infty$. For the periodic Hilbert transform $\mathcal H$,
the kernel of $U_\chi\mathcal H U_\chi^*-\mathcal H$ is

$$
 \frac1L\left[
 \sqrt{\chi'(x)\chi'(y)}
       \cot\frac{\pi(\chi(x)-\chi(y))}{L}
       -\cot\frac{\pi(x-y)}L\right].                      \tag{D.23}
$$

Its singular part cancels exactly. Here is an explicit full bound.
Choose $d=x-y$ on the circle with $|d|\le L/2$, and
$A=(\chi(x)-\chi(y))/d$. Then
$A\in[1-\epsilon,1+\epsilon]$ and
$|\sqrt{\chi'(x)\chi'(y)}-A|\le M_2|d|/2$.
On $|s|\le3\pi/4$, concavity gives $\sin|s|\ge0.3|s|$.
For $R(s)=\cot s-1/s$,
$|R'(s)|\le4$ follows from
$|s-\sin s|\le|s|^3/6$ and that lower bound.
Separating the $1/s$ singularity in (D.23) therefore yields a bounded
kernel and, by the full Schur integral estimate,

$$
 \|U_\chi\mathcal H U_\chi^*-\mathcal H\|
      \le LM_2/\pi+5\pi\epsilon
      <M_2/2+16\epsilon\quad(L=\pi/2).                    \tag{D.24}
$$

Consequently the opposite-cone blocks satisfy

$$
 \|\Pi_sU_\chi\Pi_u\|,\ \|\Pi_uU_\chi\Pi_s\|
                      \le M_2/4+8\epsilon .              \tag{D.25}
$$

The constant matrix $\mathcal C$ commutes with the scalar pullback.
Both means are retained separately. For example the mean-to-nonmean
block of $U_\chi$ has norm at most $\epsilon$, since
$U_\chi1=\sqrt{\chi'}$ and
$|\sqrt{\chi'}-1|\le\epsilon/(1+\sqrt{1-\epsilon})$.
The adjoint block has the same norm by the full unitarity identity.

For a finite head, its additional coupling can be bounded using its
finite derivative, without extending bare pullback smallness to high
frequencies. If $h_*=\|\chi-\mathrm{id}\|_\infty$ for a consistent
lift, interpolation along
$\chi_t=(1-t)\mathrm{id}+t\chi$ gives

$$
 \|(U_\chi-I)P_L\|\le 2\epsilon+2Nh_* .                    \tag{D.26}
$$

All finite head and mean coupling operators remain exactly in the
interface version of (D.21); (D.26) is only a sufficient norm budget.

The actual small differences in (D.24)–(D.26) must be computed from
the complete saved candidate interfaces. They are not inferred from
a floating continuity tolerance. The exact angle lift gives, for
instance,
$\|\chi-\mathrm{id}\|_\infty
 \le\|\theta_+-\theta_-\|_\infty/\inf j_-$.
Then $\chi'=j_+/(j_-\circ\chi)$ and its exact derivative give the
first and second derivative budgets from complete one-sided
coefficient differences. These preserve the changing mean $m$.

## 8. Piecewise high two-port assembly with explicit interface fees

For clarity, a sufficient full piecewise contract can be stated in
the $L^\infty_rL^2_\phi$ solution norm. For the Neumann step use the
explicit two-branch maximum norm
$\max(\|w_s\|_{L^\infty_rL^2},\|w_u\|_{L^\infty_rL^2})$;
the final Euclidean two-row Hilbert norm is at most $\sqrt2$ times
this norm. At each interface split the
exact high blocks of $U_\chi$ into stable and unstable rows. Suppose
that both diagonal blocks are onto and their inverse norms are paid,
and that their corresponding two-port scattering representation has
diagonal propagation factors at most $\Gamma_i\ge1$ and cross
reflection norm at most $\rho_i$. These are concrete blocks of
(D.22), with the complete head columns retained as sources.

The required onto property is not granted merely by injectivity.
For example, unitarity plus complete upper bounds on both the
off-cone and head leakage rows gives both
$U_{\sigma\sigma}^*U_{\sigma\sigma}\ge(1-\varepsilon_i^2)I$
and
$U_{\sigma\sigma}U_{\sigma\sigma}^*\ge(1-\varepsilon_i^2)I$.
If $\varepsilon_i<1$, both-sided inverse bounds follow.
These estimates use the full head leakage, not only (D.25).

Let $\Gamma=\prod_i\Gamma_i$, assume the smooth diagonal decay gate
$\lambda_*>0$ on every piece, and let $k_*$ be the full distributed
cross bound. If

$$
 \rho:=\Gamma\left(k_*/\lambda_*+\sum_i\rho_i\right)<1,      \tag{D.27}
$$

the exact piecewise high two-port problem is inverted by Neumann on
the stated two-branch maximum norm. The diagonal Green kernels
are bounded by
$\Gamma e^{-\lambda_*|r-s|}$ in their allowed direction.
An interface reflection enters as the actual point source in that
kernel. Thus

$$
 \|w_H\|_{L^\infty_rL^2}
 \le \frac{\sqrt2\Gamma}{1-\rho}
 \left(\|g_H\|_{\ell^1\text{ of the two ports}}
       +\|F_H+K_{HL}w_L\|_{L^1_rL^2}
       +\sum_i\|\text{actual head/jump source}_i\|_2\right).            \tag{D.28}
$$

For the distributed coupling, each output branch uses only the
opposite input branch, so its exponential integral is at most
$k_*/\lambda_*$ in the maximum norm. Each interface cross block
similarly contributes at most $\rho_i$. The displayed $\sqrt2$ is
the explicit conversion back to the Euclidean two-row output norm;
it is not suppressed inside a Hilbert supremum estimate.

This retains every interface, low source and ordinary source column.
If an $L^2_r$ norm is desired, the explicit factors
$|I|^{1/2}$ and
$\|F\|_{L^1}\le|I|^{1/2}\|F\|_{L^2}$ convert this sufficient contract;
no free change of source space is asserted.
The same exact finite-head Schur equation (D.21), with all low
interface conditions, then applies.

Condition (D.27) is sufficient, not necessary. It is not declared
verified for the present entire positive body. Its merit is that
every actual fee is identified and no inverse exponentially small
transmission, hidden mean projection, or bare same-space pullback
difference appears.

## 9. Current application status

For the current final moving centre, the exact physical complex germ
and full local Airy collar already supply the genuine turning
operator and true source/mean conventions. Equations (D.1)–(D.9)
now give a local physical positive-interval operator whose radial
principal part and true residual-sensitive drift can be computed
directly from the same complete candidate. Equations (D.10)–(D.28)
specify the actual coefficient, interface, high-frequency, head,
and source obligations needed to attach its positive regular graph.

No numerical high cutoff, finite-head inverse, actual regular graph
over the whole positive interval, or nonlinear full BVP is granted
until those same-centre gates and the exterior boundary conditions
are paid. This is an exact reduction and a complete quantitative
conditional inverse theorem, preserving the actual outstanding
spectral task.
