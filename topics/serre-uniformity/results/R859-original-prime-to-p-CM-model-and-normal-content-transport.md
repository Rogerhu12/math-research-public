# R859 — A prime-to-$p$ comparison with the explicit original CM model, preserving every normal content

Date: 2026-11-16. Status: **proved for every prime in the original range below**. The stable-lattice and complete-BT results used here are already in R390 §§3–4, with their actual-local scope retained by R575. The new statement is their application to the particular model of R725/R728: a rational isogeny can be calibrated to have degree prime to $p$, and this transports the original, ramification-normalized disk functions without changing their common $p$ factors, even one original CM label at a time. No first normal coefficient is asserted to be a unit.

## 1. The original objects and the old local input

Put
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
n=p+1,\quad m=n/6,\quad e=p^2-1,
\quad K=\mathbf Q(\sqrt{-3}),
\quad E=\mathbf Q(\zeta_n),\quad F=E^+.
\tag{859.1}
$$
Keep the original positive CM factor $A=A_{\theta,1}$, its fixed original quotient $q:J_{X_p}\to A$, the original $c_0:a=0$ rigidification, and $c_1:a=1$. Thus the disk map centered at $c_1$ is exactly
$$
\gamma(P)=q([P-c_1])
=q([P-c_0])-\beta,\qquad \beta=q([c_1-c_0]).
\tag{859.2}
$$
Nothing in this proof rescales $q$ or chooses a new translation.

Use precisely the R725/R728 model
$$
C/L:y^2=x^3+b,\qquad \omega_C=\frac{dx}{2y},
\qquad B=\operatorname{Res}_{L^+/\mathbf Q}C,
\qquad A^{\mathrm{mod}}=E_n(B),
\tag{859.3}
$$
where $b=r_0^6$, $L^+=\mathbf Q(b)$, $L=L^+K$, $E_n=ne_n$, and $e_n$ is the actual Ramanujan projector of R728(728.21). R728(728.24) gives a $\mathbf Q$-isogeny
$$
j:A\longrightarrow A^{\mathrm{mod}}.
\tag{859.4}
$$
At this point its degree is unrestricted. R728(728.19–24,32), or R819(819.13–16), identifies the rational endomorphism fields with $E$ over $K$ and $F$ over $\mathbf Q$. The identification is the one with the same original Hecke characters; an intertwiner cannot permute their distinct character lines.

Write
$$
\mathcal H=\{h:1\le h\le p,\ h\equiv1\pmod6,
\ (h,n)=1\},\qquad g=|\mathcal H|=\varphi(n)/2.
\tag{859.5}
$$
For the fixed $p$-adic embedding the finite character is, with the original orientation,
$$
\theta_h(u)=[u]^{-h(p-1)}.
\tag{859.6}
$$
This is R727's initial convention. It is R390's label $k=-h$. The original positive Hecke character is $\Psi_{\theta_h}\kappa_4$. Its local Tate realization is $\psi_0\eta_h$, where $\psi_0$ is the good CM Tate character of $E_{27}$ in R725(725.3–9). In the arithmetic reciprocity convention of R390.14, the finite twist has the two compatible descriptions
$
\eta_h(\operatorname{rec}_{K_p}(u))=[\bar u]^{h(p-1)},
\qquad
\eta_h(\sigma)=\xi^{-h(p-1)}
\quad\text{when }\sigma(\varpi)=\xi\varpi .
\tag{859.6a}
$
Thus the Hecke finite type is not confused with its inverse on reciprocity units. The cubic character $\kappa_4$ is trivial at $p$: $4$ is a cube in $\mathbf Q_p$ because $p\equiv2\pmod3$. The R575 correction of the global cubic twist consequently does not change this R390 local input. These are the actual $p$-adic Tate characters, not Weil–Deligne types substituted for residual representations.

For clarity, the old input being used is the following. R390(390.17–22) separates the residual pairs
$$
1-h(p-1),\qquad p+h(p-1)\pmod e
\tag{859.7}
$$
for $h\in\mathcal H$. A cross collision would require $h+h'\equiv-1\pmod n$, impossible since both labels are $1\pmod6$. Its integral spectral projectors act on every actual stable Tate lattice. On each two-dimensional $G_{\mathbf Q_p}$ block all stable lattices are homothetic to the reference CM lattice; the corresponding statement for complete BT groups holds over a common good-reduction extension. These are already proved in R390, and are not new results of this paper. In particular no finite-order element is being postulated inside the absolute Galois group.

Since $p\equiv-1\pmod n$, $p$ splits completely in $F$ and every prime of $F$ above $p$ is inert in $E/F$. Therefore
$$
F\otimes\mathbf Q_p=\prod_{h\in\mathcal H}\mathbf Q_p,
\qquad E\otimes\mathbf Q_p=\prod_{h\in\mathcal H}K_p.
\tag{859.8}
$$
The indices refer to the same positive labels, rather than to the whole, possibly imprimitive, Weil restriction.

## 2. Maximal local orders on the original target

The complete reference lattice in every block has the integral $\mathcal O_{K_p}$ action described in R390 §3.1. Homothety and the old integral projectors consequently give
$$
(\mathcal O_E\otimes\mathbf Z_p)T_p(A)=T_p(A).
\tag{859.9}
$$
This does not assume an integral finite-order automorphism on the original $A$; it derives the local order from its actual Galois-stable lattice.

Here is the required passage back to genuine endomorphisms, avoiding an unstated integral Tate theorem. If $u\in\operatorname{End}_K^0(A)$ preserves $T_p(A)$, choose an integer $p^r d$ with $(d,p)=1$ such that $a=p^rdu$ is an actual endomorphism. Then $aT_p(A)\subset p^rT_p(A)$, so $a$ kills $A[p^r]$. In characteristic zero it therefore factors through the actual quotient $[p^r]:A\to A$ over $K$. Write $a=[p^r]v$ with $v\in\operatorname{End}_K(A)$. This gives $u=v/d$ and proves
$$
u\in\operatorname{End}_K(A)\otimes\mathbf Z_{(p)}.
\tag{859.10}
$$
Apply this to $u\in\mathcal O_E$, using (859.9), and complete. The reverse inclusion holds because an endomorphism order consists of algebraic integers. The same argument for $u\in\mathcal O_F$ uses factorization over $\mathbf Q$. Thus
$$
\boxed{\operatorname{End}_K(A)\otimes\mathbf Z_p
 =\mathcal O_E\otimes\mathbf Z_p,\qquad
\operatorname{End}_{\mathbf Q}(A)\otimes\mathbf Z_p
 =\mathcal O_F\otimes\mathbf Z_p.}
\tag{859.11}
$$
The assertion concerns the local orders at $p$. It makes no claim about their conductors at other primes.

## 3. A $\mathbf Q$-isogeny of degree prime to $p$

Regard $jT_p(A)$ and $T_p(A^{\mathrm{mod}})$ as lattices in the same rational Tate space. For each $h$, R390's block-lattice uniqueness gives an integer $a_h$ such that
$$
e_hjT_p(A)=p^{a_h}e_hT_p(A^{\mathrm{mod}}).
\tag{859.12}
$$
Here $e_h$ is the old integral local spectral projector. The scalar is a power of $p$, because these are the two-dimensional $G_{\mathbf Q_p}$ blocks; no choice of a possibly ramified coefficient uniformizer is hidden in (859.12).

By weak approximation in the global field $F$, choose $c\in F^\times$ with
$$
v_{\mathfrak p_h}(c)=-a_h\qquad(h\in\mathcal H).
\tag{859.13}
$$
The rational homomorphism $j_0=cj$ is defined over $\mathbf Q$ and maps the two Tate lattices isomorphically. To make it actual without reintroducing a $p$ factor, choose $p^r d$ clearing its denominators, with $(d,p)=1$. As in (859.10), $p^rdj_0$ kills $A[p^r]$ and factors through $[p^r]$. Hence
$$
j_p=dj_0\in\operatorname{Hom}_{\mathbf Q}(A,A^{\mathrm{mod}})
\tag{859.14}
$$
is actual. Its map on $p$-adic Tate lattices is an isomorphism. It is an isogeny, since $c\ne0$ in the simple endomorphism field, and its kernel has trivial $p$ part. We have proved
$$
\boxed{p\nmid\deg j_p.}
\tag{859.15}
$$
This is an existence theorem for a calibrated isogeny to the specified model. It does not pretend that the coordinate functions of $j_p$, or of $j_pq$, have been computed. Choosing the scalar in $F$, rather than merely in $E$, is what retains definition over $\mathbf Q$.

Let $F_p(T)$ be the actual minimal polynomial of $b$ used in R725/R728. A prime-to-$p$ isogeny induces an isomorphism of Néron cotangent lattices: compose it with its reverse isogeny and use that the resulting multiplication integer is a $p$ unit. R728(728.27–30) now gives, on the original target,
$$
\boxed{\omega_{\mathcal A}
 =j_p^*\omega_{\mathcal A^{\mathrm{mod}}}
 =j_p^*e_n^*\!\left(
 F_p'(b)^{-1}\mathbf Z_p[b]\,\omega_C\right).}
\tag{859.16}
$$
The last expression uses R728's trace identification and its primitive direct summand. The inverse different is retained. The map from the original Jacobian to this lattice is still the actual pullback $(j_pq)^*$; (859.16) does not say that this latter map has saturated image or a unit value at $c_1$.

## 4. Transport of the original normalized disk functions

Use the original complete unramified coefficient ring $R_0=W(\overline{\mathbf F}_p)$ of R378, and
$$
R=R_0[\varpi],\qquad \varpi^e=p,\qquad
\sigma(\varpi)=\xi\varpi,
\tag{859.17}
$$
with $\xi$ a primitive $e$-th root. The original models have good reduction over such a tame extension by R390; the complete-BT comparison is equivariant for this same descent. Use exactly the source parameters of R378:
$$
z=\frac{a-1}{\varpi^{3p(p-1)}},\qquad
w=\frac{a-1}{p^3},\qquad z=\varpi^{3(p-1)}w.
\tag{859.18}
$$
No replacement of the coarse parameter or the original CM center is made.

R390 gives complete one-dimensional formal-group factors, indexed by $\mathcal H$, with good-model coordinates $Y_h$ and $Z_h$ of the same exact semilinear weights
$$
t_h=(p-1)h,\qquad 0<t_h<e,
\qquad \sigma(Y_h)=\xi^{t_h}Y_h,
\quad\sigma(Z_h)=\xi^{t_h}Z_h.
\tag{859.19}
$$
The sign is the coordinate-ring sign of R390(390.5–6), with $k=-h$. It is not the opposite finite Tate twist. Both targets use the positive twist fixed in (859.6).

Define the original functions and their images by
$$
\begin{aligned}
F_h(z)&=Y_h(\gamma(P(z))),&
F_h^{\mathrm{mod}}(z)&=Z_h(j_p\gamma(P(z))),\\
G_h(w)&=\varpi^{-t_h}F_h(\varpi^{3(p-1)}w),&
G_h^{\mathrm{mod}}(w)&=\varpi^{-t_h}F_h^{\mathrm{mod}}(\varpi^{3(p-1)}w).
\end{aligned}
\tag{859.20}
$$
They lie in $wR_0\langle w\rangle$ by R378(378.36–40) and R390(390.23). The maps are centered at the same actual point: $j_p\gamma=j_pq([P-c_0])-j_p\beta$.

Because of (859.15), $j_p$ induces an integral formal-group isomorphism between the two good models. In arbitrary coordinates with the listed weights, write it as
$$
Z_i=H_i(Y)=\sum_{|\nu|\ge1}a_{i\nu}Y^\nu,
\qquad a_{i\nu}\in R.
\tag{859.21}
$$
The inverse has the same properties. Equivariance gives
$$
\sigma(a_{i\nu})=\xi^{t_i-\sum_j\nu_jt_j}a_{i\nu}.
\tag{859.22}
$$
Consequently the normalized coefficients
$$
\widetilde a_{i\nu}
=a_{i\nu}\varpi^{\sum_j\nu_jt_j-t_i}
\tag{859.23}
$$
are in the fraction field of $R_0$. If nonzero, their $\varpi$ valuations are multiples of $e$. Integrality of $a_{i\nu}$, $|\nu|\ge1$, and $0<t_i<e$ make that valuation strictly greater than $-e$, hence nonnegative. Also
$$
v_\varpi(\widetilde a_{i\nu})
\ge |\nu|\min_j t_j-\max_i t_i\longrightarrow+\infty.
\tag{859.24}
$$
Thus normalization produces mutually inverse restricted analytic coordinate transformations over $R_0$, with zero constant terms:
$$
G^{\mathrm{mod}}=\widetilde H(G),\qquad
G=\widetilde H^{-1}(G^{\mathrm{mod}}).
\tag{859.25}
$$
A restricted series with zero constant term is a sum $\sum_jX_jA_j(X)$ with restricted $A_j$. Apply this to both transformations to obtain the actual ideal equality
$$
\boxed{(G_h:h\in\mathcal H)
=(G_h^{\mathrm{mod}}:h\in\mathcal H)
\quad\text{in }R_0\langle w\rangle.}
\tag{859.26}
$$
In particular their joint coefficient-content ideals in the DVR $R_0$ agree. The convergent coefficient sums remain in these ideals because every DVR ideal is closed.

## 5. Keeping each original label separately

There is a stronger conclusion in the actual complete-BT factor coordinates, not just in arbitrary coordinates of §4. The rational isogeny $j$ intertwines the original $E$ actions, and multiplication by $c\in F$ preserves this property. The integral spectral idempotents of (859.9) act on the complete BT groups by R390 and Tate full faithfulness. Thus $j_p$ carries the $h$ factor to the same $h$ factor. In those product coordinates,
$$
Z_h=H_h(Y_h)=\sum_{r\ge1}a_{h,r}Y_h^r,
\qquad a_{h,1}\in R^\times.
\tag{859.27}
$$
There are no other-label terms. For $r=1$, (859.22) shows
$u_h:=a_{h,1}\in R_0^\times$. For $r\ge2$, the normalized coefficient has valuation a positive multiple of $e$, because $a_{h,r}$ is integral and $(r-1)t_h>0$. Equations (859.23–24) therefore sharpen to
$$
\boxed{\widetilde H_h(X)
=u_hX+pX^2V_h(X),\qquad
u_h\in R_0^\times,\quad V_h\in R_0\langle X\rangle.}
\tag{859.28}
$$
Its inverse has the same form. For the actual disk functions this gives
$$
G_h^{\mathrm{mod}}
=G_h\bigl(u_h+pG_hV_h(G_h)\bigr),
\qquad u_h+pG_hV_h(G_h)\in R_0\langle w\rangle^\times.
\tag{859.29}
$$
The displayed unit has its inverse by a convergent geometric series. We obtain, for every original primitive label individually,
$$
\boxed{(G_h^{\mathrm{mod}})=(G_h)
\quad\text{in }R_0\langle w\rangle.}
\tag{859.30}
$$
If $G_h=\sum_{r\ge1}b_{h,r}w^r\ne0$, let
$M_h=\min_r v_p(b_{h,r})$. It is a nonnegative integer, and (859.28) proves both
$$
M_h^{\mathrm{mod}}=M_h,
\qquad
\overline{p^{-M_h}G_h^{\mathrm{mod}}}
=\bar u_h\,\overline{p^{-M_h}G_h}.
\tag{859.31}
$$
Indeed the nonlinear term has coefficient content at least $1+2M_h>M_h$. This includes the whole first normal residue function, not just its first coefficient in $w$.

The same preservation can be stated for the original differential comparison. Let the invariant differential on each good formal factor be normalized to have initial term $dY_h$, respectively $dZ_h$. Pullback by $j_p$ multiplies it by $u_h$. Relative to the **same** original raw flat Hodge vector of R592/R727, if the two pullbacks along the original disk map have scalars $c_h$ and $c_h^{\mathrm{mod}}$, then
$$
c_h^{\mathrm{mod}}=u_hc_h,
\qquad v_p(c_h^{\mathrm{mod}})=v_p(c_h).
\tag{859.32}
$$
The common ramification factor $\varpi^{t_h}$ in (859.20) is present on both sides. It is not replaced by an integer-unit assertion.

## 6. What is now available, and what remains

The explicit inverse-different primitive Néron lattice of R728 may now be used as a model for the original target after a genuine $\mathbf Q$-defined prime-to-$p$ isogeny. Its complete good-model coordinates transport the actual $c_1$ disk functions, and each original label retains its precise normal-content ideal and first normal residue up to a unit.

This proves neither a value for $M_h$ nor a unit for the first normal coefficient. R390's lower bound $M_1\ge1$ for the weight-one factor remains a lower bound. The unknown original pullback/test vector has not been replaced by an arbitrary generator of the model's Néron lattice. In particular this result does not turn R855's higher Abel unit, R857's full open-disk root count, or a nonzero characteristic-zero Hom into a first-block same-$h$ Cartier/Legendre unit or a nonzero height coefficient.

### Original sources used

- [R390](R390-cm-coordinate-inertia-weight-one-channel-and-cartier-unit.md), §§2–4: exact local character orientation, arbitrary stable lattices, complete BT comparison and coordinates.
- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md), §§5–7: original positive cubic twist; explicit retention of the local $p$-type and integral-BT results.
- [R378](R378-actual-cm-disc-parameter-and-uniform-integral-tail.md), §§2–6: the actual $c_1$ disk, source scaling, descent and full integral tails.
- [R725](R725-original-CM-elliptic-model-and-splitting-field.md), §§1–6, and [R728](R728-original-Weil-restriction-primitive-projector-and-Neron-lattice.md), §§1–6: the actual CM characters, $b$, $B$, primitive factor and inverse-different Néron lattice.
- [R819](R819-original-primitive-Hom-field-and-all-cusp-nonramification.md), §§1–3: the same original positive $E$ action and primitive, rather than whole-Weil-restriction, scalar convention.

This is a paper proof. No new arithmetic computation, finite-prime scan or recomputation of an existing source is used.
