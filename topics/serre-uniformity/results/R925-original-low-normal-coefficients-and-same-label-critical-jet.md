# R925 — Original low normal coefficients and the same-label critical theta jet

Date: 2026-11-16. Status: **proved for the two original primitive labels of R921/R924**. The whole reduction polynomial of the original calibrated map is compared, coefficient by coefficient and with exact squared constants, to the original sigma products. In particular its linear coefficient detects the two Cartier factors in the same-label criterion. The original Legendre factor remains separate. No nonvanishing of that linear coefficient is asserted.

## 1. The two original labels and the comparison to be proved

Retain the original positive CM factor, quotient $q:J_{X_p}\to A$, $c_0$ rigidification, center $c_1$, and allowed primes of R921/R924:
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
n=p+1,\quad e=p^2-1,\quad
R=R_0[\varpi],\quad\varpi^e=p.
\tag{925.1}
$$
The symbol $q$ here denotes the actual quotient, not a Fourier parameter. Use the following same primitive labels and integers:
$$
\begin{array}{c|c|c|c|c|c}
p\bmod12&h&k_+&J=m_h&D=3J-1&h-D\\ \hline
11&(p+3)/2&4&(p-5)/6&(p-7)/2&5\\
5 &(p+9)/2&10&(p-11)/6&(p-13)/2&11 .
\end{array}
\tag{925.2}
$$
In both rows
$$
p-h-D=2,\qquad
h\equiv1\pmod6,\qquad (h,p+1)=1,\qquad
7\le h\le p-4.
\tag{925.3}
$$
These are the labels already proved primitive in R918/R920. In particular $J\ge5$, and $D+1=3J<p$.

The original completed-Hom division and calibrated functions of R924 are denoted by
$$
[p^{a_h}]\mathscr F_h=e_h\gamma,\qquad
\gamma(P)=q([P-c_1]),\qquad
t_h=(p-1)h,
$$
$$
w=\frac{a-1}{p^3},\qquad
G_h(w)=\varpi^{-t_h}Y_h(e_h\gamma(P)),\qquad
Q_h(w)=\overline{p^{-a_h}G_h(w)}
      =\sum_{j=1}^{J}q_{h,j}w^j.
\tag{925.4}
$$
The source point $P$ is on the original branch in R378/R859. R924 proves
$$
p^{-a_h}G_h\in wR_0\langle w\rangle,\qquad q_{h,J}\ne0.
\tag{925.5}
$$
The index $a_h$ is the original Tate-image index. It is not set to zero.

On the separate, fixed elliptic curve and differential
$$
E_0:y^2=x^3-1,\qquad dz=\frac{dx}{2y},
$$
retain exactly the R697/R770 sigma functions
$$
F(z)=x(z)\sigma(z)^6=z^4\sum_{i\ge0}f_i z^{6i},
\qquad
G(z)=-x(z)y(z)\sigma(z)^6=z\sum_{i\ge0}g_i z^{6i}.
\tag{925.6}
$$
This elliptic $z$ is not the flat modular coordinate used below. Put
$$
f_*=
\begin{cases}
f_0=1,&p\equiv11\pmod{12},\\
f_1=4/35,&p\equiv5\pmod{12}.
\end{cases}
\tag{925.7}
$$
Both values are $p$-units. The second follows directly from the original
$x=z^{-2}+z^4/7+\cdots$ and
$\sigma^6=z^6(1-z^6/35+\cdots)$; it is also equivalent to R697's $A_{11}=12960$. No change of sigma normalization is used.

For $1\le j\le J$, define
$$
m_j=3j-1,\qquad k_{1,j}=h-m_j,\qquad
k_{2,j}=p-h-m_j.
\tag{925.8}
$$
Exactly one of $k_{1,j},k_{2,j}$ is $5$ modulo $6$ and the other is $2$ modulo $6$. Define the actual ordered sigma product
$$
\Sigma_j=
\begin{cases}
f_{(k_{1,j}-5)/6}\,g_{(k_{2,j}-2)/6},
   &k_{1,j}\equiv5\pmod6,\\
g_{(k_{1,j}-2)/6}\,f_{(k_{2,j}-5)/6},
   &k_{1,j}\equiv2\pmod6.
\end{cases}
\tag{925.9}
$$
All indices are nonnegative, and $\Sigma_J=f_*$. The Taylor orders are below $p$, so these rational coefficients are $p$-integral by R697.

Let $B\in\mathbf F_p^\times$ be the original Cartier constant of R705/R727:
$$
B=(-1)^{(p-1)/2-(p-2)/3}
\binom{(p-1)/2}{(p-2)/3}.
\tag{925.10}
$$
Our coefficient comparison is
$$
\boxed{
\left(\frac{q_{h,j}}{q_{h,J}}\right)^2
=
\left[
\frac{(3J)!}{(3j)!}
(81B^6)^{\,j-J}
\frac{\overline{\Sigma_j}}{\bar f_*}
\right]^2
\quad(1\le j\le J).
}
\tag{925.11}
$$
Every scalar other than the specified sigma product is a unit. In particular
$$
q_{h,j}\ne0
\quad\Longleftrightarrow\quad
\overline{\Sigma_j}\ne0.
\tag{925.12}
$$
The formula is deliberately squared. It does not choose independent signs and then assume they arise from one common signed identity.

At $j=1$, put
$$
p=6N+5,\qquad i=\frac{h-7}{6},\qquad \ell=N-1-i.
\tag{925.13}
$$
Then $\Sigma_1=f_i g_\ell$. More explicitly it is $f_tg_t$ when $p=12t+11$, and $f_tg_{t-1}$ when $p=12t+5$.

Define the explicit unit
$$
u_h=\frac{6\bar f_*}{(3J)!}(81B^6)^{J-1}
\in\mathbf F_p^\times.
\tag{925.14}
$$
Formula (925.11) gives
$$
\boxed{
(\overline{f_i g_\ell})^2
=u_h^2\left(\frac{Q_h'(0)}{q_{h,J}}\right)^2.
}
\tag{925.15}
$$
Thus the previously unknown low normal coefficient is now tied to the original same-label Cartier product, rather than merely to some high nonzero coefficient.

## 2. The calibrated formal logarithm preserves the whole reduction

We first justify passage from the actual good formal group to its logarithm on this entire calibrated disc, including the infinite tail.

Write its normalized invariant differential as
$$
\omega_h=H_h(Y)\,dY,\qquad
H_h(Y)=1+\sum_{r\ge1}b_rY^r\in R[[Y]].
\tag{925.16}
$$
The exact semilinear coordinate weight is $t_h$, and the differential has the same weight. Consequently
$$
b_r\varpi^{rt_h}\in R_0,\qquad
v_p(b_r\varpi^{rt_h})\ge
\left\lceil\frac{rh}{p+1}\right\rceil .
\tag{925.17}
$$
The assertion follows from integrality of $b_r$ and unramified descent, exactly as for the original coordinate coefficients in R859/R924.

The normalized formal logarithm is
$$
L_h^{\mathrm{cal}}(W)
=\varpi^{-t_h}\log_h(\varpi^{t_h}W)
=W+\sum_{r\ge1}
\frac{b_r\varpi^{rt_h}}{r+1}W^{r+1}.
\tag{925.18}
$$
In both rows $h/(p+1)>1/2$. For every $r\ge1$,
$$
\left\lceil\frac{rh}{p+1}\right\rceil-v_p(r+1)\ge1.
\tag{925.19}
$$
If $p\nmid r+1$, this is immediate. If $v_p(r+1)=a\ge1$, then
$r\ge p^a-1$ and
$\lceil rh/(p+1)\rceil>r/2\ge(p^a-1)/2\ge a$.
The last inequality holds for $p\ge3$ and $a\ge1$, for example by induction on $a$. The bound tends to infinity with $r$, since its linear term dominates $\log_p(r+1)$. Hence
$$
\boxed{
L_h^{\mathrm{cal}}(W)=W+pW^2V_h(W),\qquad
V_h\in R_0\langle W\rangle.
}
\tag{925.20}
$$
This is the actual logarithm, not a formal additive model substituted for the original formal group.

Let
$$
\Lambda_h(w)=L_h^{\mathrm{cal}}(G_h(w)).
\tag{925.21}
$$
Since $G_h=p^{a_h}$ times an integral restricted series, (925.20) proves
$$
p^{-a_h}\Lambda_h\in wR_0\langle w\rangle,\qquad
\overline{p^{-a_h}\Lambda_h}=Q_h.
\tag{925.22}
$$
All nonlinear terms after division have coefficient valuation at least $1+a_h$. No finite truncation or unstated convergence assumption is involved.

## 3. Retaining the actual raw Hodge comparison

Let $M_{m,h}$ be exactly the original flat Hodge jets of R727/R855, with the same cusp-normalized split vector, CM torus, tame vector and absolute period. Their centered primitive is
$$
\mathcal I_h(z_{\rm f})
=\sum_{j\ge1}
\frac{M_{3j-1,h}}{(3j)!}z_{\rm f}^{3j}.
\tag{925.23}
$$
The flat/coarse change is the original one:
$$
V=\frac{z_{\rm f}^3}{p^3}
=\Psi(w),\qquad
\Psi(w)\in w\mathbf Z_p\langle w\rangle,\qquad
\Psi(w)\equiv\frac38w\pmod p,
\tag{925.24}
$$
with integral analytic inverse. This is R727 §9 and R857 §5, independently of the embedding $h$.

The constant Hodge/Kodaira--Spencer comparison of R705 §7 and R727(727.29), now applied to the specified descended differential
$\varpi^{-t_h}\omega_h$, gives one nonzero scalar $c_h^{\mathrm{cal}}$ such that
$$
\Lambda_h(w)
=c_h^{\mathrm{cal}}\,
\mathcal I_h(z_{\rm f}(p^3w)).
\tag{925.25}
$$
The same scalar multiplies every derivative. The center remains exactly $c_1$ and the original $c_0$ subtraction is the one in (925.4).

Set
$$
E_{j,h}=\frac{p^{3j}M_{3j-1,h}}{(3j)!}.
\tag{925.26}
$$
Equations (925.22)--(925.25), composed with the inverse of $\Psi$, imply
$$
\frac{c_h^{\mathrm{cal}}}{p^{a_h}}
\sum_{j\ge1}E_{j,h}V^j\in VR_0\langle V\rangle,
\quad
\overline{
\frac{c_h^{\mathrm{cal}}}{p^{a_h}}
\sum_{j\ge1}E_{j,h}V^j}
=Q_h(8V/3).
\tag{925.27}
$$
Thus the normalized coefficient at $J$ is a unit. For $j\le J$,
$$
\boxed{
\frac{q_{h,j}}{q_{h,J}}
=\left(\frac38\right)^{j-J}
\overline{\frac{E_{j,h}}{E_{J,h}}}.
}
\tag{925.28}
$$
The fractions on the right are integral because the denominator in the common normalized series is a unit. In particular this coefficient formula is not obtained by reducing an unnormalized nonintegral raw series.

The original rationality argument in R727 §9/R857 §2 also applies with any nonzero reference jet: the raw primitive is one scalar times the actual $\mathbf Q_p$ component and the flat/coarse inverse has coefficients in $\mathbf Q_p$. It follows that
$M_{m_j,h}/M_{D,h}\in\mathbf Q_p$ whenever $M_{D,h}\ne0$. The next section proves that nonvanishing without assuming $M_{2,h}\ne0$.

## 4. Cancelling the finite norm before reduction

Write $N_h$ for the original finite norm of R727(727.2), and
$$
\nu_h=v_p(N_h)\ge0.
\tag{925.29}
$$
It is a nonzero algebraic number in the original unramified character field. Its reduction is allowed to vanish.

For every $m=m_j$, the hypotheses of R855(855.7) hold:
$$
2\le m\le D<p-2,\qquad m\equiv2\pmod3,\qquad
k_1=h-m\ge h-D,\qquad k_2=p-h-m\ge2.
\tag{925.30}
$$
The actual exact norm identity is
$$
M_{m,h}^{\,2}
=-\zeta^2
\frac{[m!(m+1)!]^2N_h}{18(p+1)^2}
S_{m,h}S_{m+1,h}.
\tag{925.31}
$$
Here the two sums, including every higher block, are the fixed ones of R855(855.10)--(855.18). All factorials in (925.31) are units.

Define in characteristic zero
$$
U_{m,h}=\frac{(p^mM_{m,h})^2}{N_h}.
\tag{925.32}
$$
This is an exact quotient, not division by $\bar N_h$. By (925.31) it equals
$$
-\zeta^2
\frac{[m!(m+1)!]^2}{18(p+1)^2}
p^{2m}S_{m,h}S_{m+1,h}.
\tag{925.33}
$$
R855's complete Fourier-tail proof shows that (925.33) is integral and gives
$$
\overline{U_{m,h}}
=-\frac{864\zeta^2}{\alpha^2}
B^{2m+1}(k_1)_m(k_2)_{m+1}
\mathfrak r_{k_1}\mathfrak r_{k_2},
\qquad \alpha^3=4.
\tag{925.34}
$$
The notation $(k)_r=k(k+1)\cdots(k+r-1)$ is unchanged. In particular we use the reduction of the normalized Fourier product R855(855.22), before reinserting $N_h$, and not merely the weaker congruence (855.9).

At $m=D$, the indices are $(5,2)$ or $(11,2)$. The fixed original Cartier values are
$$
C_5=\frac92,\qquad C_2=-\frac12,\qquad
C_{11}=3\,2^{-10}\,10!\left(\frac4{35}\right)^2.
\tag{925.35}
$$
They are units for every $p\ge41$. R683's full six-torsion comparison, in its exact range, is
$$
\mathfrak r_k=c(-3B)^{-(k-1)}C_k,\qquad
c=(3/p)\alpha^2/2.
\tag{925.36}
$$
All factors in the rising factorials are between $1$ and $p-1$. Therefore
$$
\boxed{
U_{D,h}\in\mathcal O^\times,\qquad
M_{D,h}\ne0,\qquad
v_p(M_{D,h})=-D+\nu_h/2.
}
\tag{925.37}
$$
The valuation is not forced to be an integer; no parity of $\nu_h$ is asserted.

For all $j\le J$, the exact cancellation now gives
$$
\left(
\frac{p^{m_j}M_{m_j,h}}{p^DM_{D,h}}
\right)^2
=\frac{U_{m_j,h}}{U_{D,h}}.
\tag{925.38}
$$
Its right side is integral and its denominator is a unit. The ratio on the left is in $\mathbf Q_p$ by §3, so the ratio itself lies in $\mathbf Z_p$. This cancellation is legitimate even when the original Legendre value, and consequently $\bar N_h$, is zero.

## 5. The exact sigma constants in the cancelled ratio

We compute the residue of (925.38), including the factorials and powers of two.

R697 gives, for the actual two sigma channels,
$$
C_k=
\begin{cases}
3\,2^{1-k}(k-1)!\,f_{(k-5)/6}^{\,2},&k\equiv5\pmod6,\\
-2^{1-k}(k-1)!\,g_{(k-2)/6}^{\,2},&k\equiv2\pmod6.
\end{cases}
\tag{925.39}
$$
In the second line the factor is $2^{1-k}$; at $k=2$ it gives exactly $C_2=-1/2$.

For $m=m_j$ put $k_1=h-m$, $k_2=p-h-m$. Since $k_1+k_2=p-2m$,
$$
C_{k_1}C_{k_2}
=-3\,2^{2-p+2m}
(k_1-1)!(k_2-1)!\,\Sigma_j^2.
\tag{925.40}
$$
The actual rising factors are
$$
(k_1)_m(k_2)_{m+1}
=\frac{(h-1)!(p-h)!}{(k_1-1)!(k_2-1)!}.
\tag{925.41}
$$
The factorials in (925.40) and (925.41) cancel exactly.

After inserting (925.36), the only $m$-dependent scalar remaining in (925.34), apart from $\Sigma_j^2$, is
$$
2^{2m}B^{2m}(-3B)^{2m}.
\tag{925.42}
$$
Indeed the factors independent of $m$ include
$2^{2-p}B(-3B)^{2-p}$, the common $(h-1)!(p-h)!$, and the fixed $c^2$ and normalization in (925.34). They cancel against the $m=D$ expression. The ratio of (925.42) at $m$ and $D$ is
$$
(6B^2)^{2(m-D)}.
\tag{925.43}
$$
Thus (925.38) becomes the exact residue identity
$$
\boxed{
\overline{
\left(\frac{p^{m_j}M_{m_j,h}}{p^DM_{D,h}}\right)^2}
=
\left[
(6B^2)^{\,m_j-D}
\frac{\overline{\Sigma_j}}{\bar f_*}
\right]^2.
}
\tag{925.44}
$$
All inverses used here are of explicitly proved units.

By (925.26),
$$
\frac{E_{j,h}}{E_{J,h}}
=\frac{(3J)!}{(3j)!}
\frac{p^{m_j}M_{m_j,h}}{p^DM_{D,h}},
\qquad m_j-D=3(j-J).
\tag{925.45}
$$
Combine (925.28), (925.44), and (925.45). The scalar in the $j-J$ power is
$$
\frac38(6B^2)^3=81B^6.
\tag{925.46}
$$
This proves (925.11) and its vanishing-support equivalence (925.12) with the original coarse parameter and the full source normalization.

## 6. The specified original theta jet

Let $s=\sqrt{-3}$ retain the R727/R898 marking, and set
$$
P_h=P_{h-1}(1/s)\in\mathbf F_p.
\tag{925.47}
$$
The even Legendre degree makes this value rational over $\mathbf F_p$; no replacement by the trace-zero auxiliary torus is made.

Use exactly the actual integral period source and quotient section of R898:
$$
\mathscr J_h
=\overline{J_{3,2}\bigl(\mathcal Z_h(u_{G,F})\bigr)}
=\frac{(6B)^5}{12}
P_h\bigl(\overline{f_i g_\ell}\bigr)^p .
\tag{925.48}
$$
The sigma coefficients are rational and reduce into $\mathbf F_p$, so their displayed Frobenius power is the same residue. Applying (925.15) proves
$$
\boxed{
\mathscr J_h^{\,2}
=
\left[
\frac{(6B)^5}{12}\,P_h\,u_h\,
\frac{Q_h'(0)}{q_{h,J}}
\right]^2 .
}
\tag{925.49}
$$
In particular the exact same-label condition is now
$$
\boxed{
\mathscr J_h\ne0
\quad\Longleftrightarrow\quad
P_{h-1}(1/s)\ne0
\ \text{and}\ Q_h'(0)\ne0.
}
\tag{925.50}
$$
The original $h$, primitive character, full determinant extension, nontrivial torus transport, $u_{G,F}$, and the functional $J_{3,2}$ are unchanged. This compares two specified original sources. It is not a deduction from unit content of an ambient theta module.

Equation (925.50) does not assert either factor is nonzero. It also does not replace the original Legendre condition by the centered auxiliary value $P_{h-1}(0)$, which is always a unit. The latter entered R898's construction of the integral source but is not the factor in (925.48).

## 7. The original comparison scalar and the retained obstruction

There is a further exact valuation conclusion. Since (925.27)'s coefficient at $J$ is a unit, (925.26) and (925.37) imply
$$
v_p(E_{J,h})=3J-D+\nu_h/2=1+\nu_h/2
$$
and therefore
$$
\boxed{
v_p(c_h^{\mathrm{cal}})
=a_h-1-\nu_h/2.
}
\tag{925.51}
$$
This is the comparison scalar for the explicitly calibrated differential $\varpi^{-t_h}\omega_h$ in (925.25). The comparison scalar for the good differential $\omega_h$ itself has the additional valuation $t_h/e=h/(p+1)$. Neither scalar is called a unit. The finite norm, its possibly positive valuation, the original Tate index, and the ramification factor have all been retained.

The polynomial $Q_h$ has degree $J$ and a unit leading coefficient, but (925.11) shows exactly why this alone does not solve the original low-term problem: its different coefficients encode different original Cartier products. The leading coefficient uses the fixed unit pair $(5,2)$ or $(11,2)$, whereas the linear coefficient uses $(h-2,p-h-2)$. No reflection or degree argument identifies them.

A proof that one of these actual polynomials has nonzero linear coefficient at a label with $P_{h-1}(1/s)\ne0$ would now prove the corresponding R898 critical-jet nonvanishing. That nonvanishing, and the separate original height/rational-point comparison needed for the main Serre-uniformity problem, remain open. The individual-label exceptions R706/R739 are not contradicted.

## Sources and precise dependencies

- [R924](R924-original-completed-Hom-lift-and-marked-normal-function.md), (924.47)--(924.55): the actual completed-Hom lift, unchanged $a_h$, calibrated polynomial and its exact degree.
- [R921](R921-original-Igusa-node-and-first-Drinfeld-normal-differential.md), together with [R918](R918-original-central-primitive-Igusa-layer-and-marked-weight-four-vector.md) and [R920](R920-original-upper-primitive-Igusa-layer-and-inert-Hecke-row.md): the two original primitive labels and marked model conventions.
- [R859](R859-original-prime-to-p-CM-model-and-normal-content-transport.md), §§4--5: exact semilinear coordinate weights and unramified calibration.
- [R705](R705-actual-higher-Abel-blocks-and-uniform-order-bound.md), §§2--5 and §7: original arbitrary permitted jet, full completed Kronecker kernels, factorials, and constant Hodge/Kodaira--Spencer comparison.
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md), (727.2), §§2, 6--9, and [R857](R857-original-higher-unit-Abel-phase-and-deep-disc-root-count.md), §§2 and 5: original finite norm and common phase, rational flat/coarse change, and complete Abel primitive.
- [R855](R855-original-primitive-higher-Abel-unit-from-cubic-Cartier.md), §2, especially (855.11), (855.18), and (855.22): exact norm identity and full Fourier product before multiplication by $N_h$. Its large-prime theorem and its different two labels are not invoked.
- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md), (697.2)--(697.4), and the full Cartier comparison as restated in R727(727.26)/R855(855.23): the two original sigma square identities, correct powers of two, and exact conversion range.
- [R898](R898-original-full-Cartan-and-integral-primitive-period-source.md), (898.33)--(898.36): the unchanged actual integral period source and its specified fifth jet.

This is a paper proof. No new numerical computation, finite-prime window, or execution of mathematical code was used.
