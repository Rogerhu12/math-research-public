# R819 — Every nonzero original primitive Hom direction is unramified at every cusp

Date: 2026-11-15. Status: **proved in the original arithmetic range below**. This is a new application of R728's already established primitive Weil-restriction factor and finite-order operator. It does not reprove that construction or generalize the $p=41$ matrices of R791.

## 1. Original fields, target, primitive factor and scalar convention

Let
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
n=p+1,\quad m=n/6,\quad
K=\mathbf Q(\zeta_3),\quad E=\mathbf Q(\zeta_n).
\tag{819.1}
$$
Keep the original positive CM embedding of $K$, the actual finite character
$\varepsilon$, the cyclic fields $H/K$ and $L/K$, and
$$
r=r_0/\sqrt[3]4,\qquad r^6=b/16,\qquad
C/L:y^2=x^3+b,\qquad \omega_C=dx/(2y)
\tag{819.2}
$$
from R725. In particular
$$
[H:K]=n,\quad [H:L]=6,\quad [L:K]=m,
\qquad
h(r)=\varepsilon(h)^{-1}r\quad(h\in\operatorname{Gal}(H/L)).
\tag{819.3}
$$
Let $A=A_{\theta,1}$ be the original primitive factor and
$q:J_{X_p}\to A$ its original quotient. The original curve and base point remain
$$
j=6912a^3(1-a^3),\qquad c_0:a=0.
$$
No opposite cubic twist or imprimitive summand is included.

Set
$$
V=\operatorname{Hom}_L(A_L,C)\otimes_{\mathbf Z}\mathbf Q.
\tag{819.4}
$$
Its $K$-scalar action is postcomposition by the actual positive CM endomorphisms of $C$. In particular $V$ is a $K$-vector space, not an $L$-vector space. The scalar extension of its differential image to $L$ is the Hodge space, as proved using actual isogeny coordinate projections in R818.

## 2. The actual semilinear operator, transported by Weil adjunction

Choose a generator $g$ of the **actual** cyclic group $\operatorname{Gal}(H/K)$ and define
$$
\sigma=g|_L,\qquad
\rho=g(r)/r,\qquad
\eta=g^m(r)/r=\varepsilon(g^m)^{-1}.
\tag{819.5}
$$
R728(728.11–14) proves
$$
\rho\in L^\times,\qquad
\rho^6=\sigma(b)/b,\qquad
N_{L/K}\rho=\eta,\qquad \operatorname{ord}(\eta)=6.
\tag{819.6}
$$
For $D_u(x,y)=(u^2x,u^3y)$, the map $D_{\rho^{-1}}$ has the actual direction $C^\sigma\to C$. Define
$$
\mathcal T(v)=D_{\rho^{-1}}\circ{}^\sigma v.
\tag{819.7}
$$
The source $A$ is defined over $K$, so this is again a member of $V$.
Because $\sigma$ fixes $K$ and the coordinate scaling commutes with the actual CM action, $\mathcal T$ is $K$-linear. Its semilinearity concerns the $L$-coefficients of the differential, not the scalar field of $V$.

Here is an exact comparison with the already established operator of R728. Put
$$
B_K=\operatorname{Res}_{L/K}C.
$$
Weil adjunction gives a $K$-linear isomorphism of rational Hom spaces
$$
V\xrightarrow{\ \sim\ }
\operatorname{Hom}_K(A_K,B_K)\otimes_{\mathbf Z}\mathbf Q,
\qquad
v\longmapsto Q_v.
\tag{819.8}
$$
Over $L$, its $\tau$-component is $\tau(v)$ for
$\tau\in\operatorname{Gal}(L/K)$. R728's actual automorphism $T$ of $B_K$ is
$$
(TP)_\tau=D_{\tau(\rho)^{-1}}P_{\tau\sigma}.
$$
Consequently, component by component,
$$
(TQ_v)_\tau
 =D_{\tau(\rho)^{-1}}\,{}^{\tau\sigma}v
 ={}^\tau(D_{\rho^{-1}}\,{}^\sigma v)
 =(Q_{\mathcal T v})_\tau.
\tag{819.9}
$$
Thus $\mathcal T$ is precisely postcomposition by the original $T$ under (819.8). It is not an arbitrarily chosen cyclic action.

In particular R728 gives
$$
\mathcal T^m=[\eta],\qquad \mathcal T^n=1.
\tag{819.10}
$$
The same sign follows directly from (819.7): the product of the scaling factors is $\eta^{-1}$, and in the positive CM convention $D_{\eta^{-1}}=[\eta]$.
The choice of a generator $g$ is substantive. The specific finite-field element used in R791 gives a different $p=41$ normalization of order $21$; that finite calculation is not used to set the order in (819.10).

For later use, define the original pulled-back differential
$$
\omega_v=q^*(v^*\omega_C)\in H^0(X_{p,L},\Omega^1).
$$
The coordinate scaling in (819.7) satisfies
$D_{\rho^{-1}}^*\omega_C=\rho\,{}^\sigma\omega_C$. Hence the exact identity of global differentials is
$$
\boxed{\omega_{\mathcal T v}=\rho\,{}^\sigma\omega_v.}
\tag{819.11}
$$
The nonzero scalar $\rho$ is retained.

## 3. Why this Hom space is a rank-one module over the primitive field

This step uses the primitive summand, not the whole $m$-dimensional Weil restriction.

R728(728.8–10) decomposes the positive CM characters of $B_K$ as
$$
\psi_0\varepsilon^a,\qquad a\bmod n,\quad a\equiv1\pmod6.
\tag{819.12}
$$
They are distinct. Its actual Ramanujan idempotent
$$
e_n=\frac1n\sum_{j=0}^{n-1}c_n(j)T^j
$$
cuts out $A^{\rm mod}=e_nB$ in the rational isogeny category. Precisely the primitive labels $(a,n)=1$ occur on this factor, and
$$
A^{\rm mod}\sim_{\mathbf Q}A,\qquad
\dim A^{\rm mod}=g_A=\varphi(n)/2.
\tag{819.13}
$$
The complementary factor contains only the different, imprimitive characters in (819.12). Thus
$$
\operatorname{Hom}_K(A_K,(1-e_n)B_K)\otimes\mathbf Q=0.
\tag{819.14}
$$
This follows directly from the actual distinct Tate characters of R728; it is not inferred from dimensions.

R728(728.19–24) identifies the original primitive algebra as
$$
e_n\operatorname{End}_K^0(B_K)
 =\operatorname{End}_K^0(A^{\rm mod}_K)
 \simeq \mathbf Q[U]/\Phi_n(U)
 =E.
\tag{819.15}
$$
The embedded $K$ here is the actual positive CM subfield: $T^m=[\eta]$ with $\eta$ a primitive sixth root. Equivalently, on the positive part the $T$-roots are exactly
$\varepsilon(g)^{-a}$ for primitive $a\equiv1\pmod6$, as R728 proves by its original scaled cyclic basis. These form one orbit under $\operatorname{Gal}(E/K)$. The minimal polynomial over $K$ is therefore the one irreducible factor of $\Phi_n$ selected by the displayed $\mu_6$ label, of degree $g_A$.

Choose any actual $K$-isogeny $j:A_K\to A^{\rm mod}_K$ from (819.13). It respects the positive $K$ action: both actions are the same scalar on the corresponding holomorphic differentials, and homomorphisms of characteristic-zero abelian varieties are detected by their differential. By (819.14), the map $u\mapsto i\circ u\circ j$, where $i:A^{\rm mod}\hookrightarrow B$ is the inclusion in the isogeny category, identifies
$$
\operatorname{Hom}_K(A_K,B_K)\otimes\mathbf Q
 \simeq \operatorname{End}_K^0(A^{\rm mod}_K)
 =E
\tag{819.16}
$$
as a left $E$-module. The inverse uses the rational inverse isogeny of $j$ and the primitive projection. Under this identification, postcomposition by $T$ is multiplication by its primitive cyclotomic class.

Combining (819.8), (819.9) and (819.16) proves
$$
\boxed{
K[\mathcal T]\simeq E,\qquad
\dim_K V=\varphi(n)/2,\qquad
\operatorname{rank}_{K[\mathcal T]}V=1.
}
\tag{819.17}
$$
In particular $\mathcal T$ has order exactly $n$ on $V$ for the generator chosen in (819.5). No explicit general-prime matrix or chosen integral Hom basis is needed for this rational-module assertion. It concerns the original primitive factor, with the same positive $K$ action; it makes no assertion that the complete Weil restriction is a rank-one module over a field.

## 4. The cusp evaluation kernel is stable under this actual field

Fix a geometric cusp $P$ of $X_{p,L}$ and write
$$
\lambda_P:V\longrightarrow\Omega^1_{X_{p,\overline L}}|_P,
\qquad v\longmapsto\omega_v(P).
\tag{819.18}
$$
This is $K$-linear. It is not being treated as an $L$-linear map on a space of homomorphisms.

By R816, all geometric cusps of the original $X_{p,L}$ form one $G_L$-orbit. Indeed their common residue field is
$L\mathbf Q(\xi_p)^+$, of degree $(p-1)/2$ over $L$; the exact coprimality is
$$
\gcd\bigl((p+1)/6,(p-1)/2\bigr)=1.
$$
If $v\in\ker\lambda_P$, then the zero divisor of the $L$-defined $\omega_v$ is $G_L$-stable, so $\omega_v$ vanishes at every geometric cusp.

The automorphism $\sigma$ of $L/K$ also permutes the geometric cusps, since the original curve is defined over $K$. Thus $\sigma(\omega_v)$ vanishes at every cusp, and (819.11), with $\rho\ne0$, shows that $\omega_{\mathcal T v}$ does too. Hence
$$
\mathcal T(\ker\lambda_P)\subseteq\ker\lambda_P.
\tag{819.19}
$$
This is the required kernel-stability argument. It does not require $P$ itself to be $L$-rational, nor an unproved action formula for a chosen nonrational local parameter.

By (819.17), a $K$-linear $\mathcal T$-stable subspace of $V$ is a submodule of a one-dimensional vector space over the field $E$. It is therefore either $0$ or $V$. R818 supplies an actual $L$-Hom direction whose differential is nonzero at the reference cusp and, by the same single-orbit argument, at every cusp. Thus $\lambda_P$ is not identically zero. The second possibility is excluded, and
$$
\boxed{\ker\lambda_P=0.}
\tag{819.20}
$$

## 5. Result and its exact boundary

**Theorem 819.1.** For every $p$ in (819.1), every nonzero member of
$\operatorname{Hom}_L(A_L,C)\otimes\mathbf Q$ has nonzero pulled-back differential at every geometric cusp of the original $X_p$. Consequently every nonzero actual integral Hom direction in this original primitive space defines a curve map unramified at all cusps.

For a rational Hom direction one may clear its integer denominator; this multiplies the differential by a nonzero integer and does not change characteristic-zero ramification. The map is the original $vq[x-c_0]$, with the original quotient, base point and target. Its differential cannot vanish identically because $q$ is surjective and a nonzero homomorphism to an elliptic curve is surjective.

This theorem strengthens R818's existence conclusion by identifying the actual field action on the full original primitive Hom space. It does not compute the image of a cusp, any pole divisor or a function defining the map. It does not supply a $p$-adic unit, the original $c_1$ critical coefficient, the same primitive-label Cartier/Legendre product, a Néron comparison factor, or a height coefficient. In particular a nonzero characteristic-zero cusp coefficient is not a substitute for the main mod-$p$ nonvanishing target.

No new mathematical computation was performed.

## Sources in the original normalization

- [R725](R725-original-CM-elliptic-model-and-splitting-field.md), §§2, 5: $H$, $L$, the original $\varepsilon$, the positive target $C$ and its $L$-splitting.
- [R728](R728-original-Weil-restriction-primitive-projector-and-Neron-lattice.md), §§2–5: the actual distinct characters, coordinate operator $T$, positive CM unit, primitive idempotent and cyclotomic endomorphism field. These are reused, not newly asserted from the finite $p=41$ calculation.
- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md) and [R616](R616-original-CM-point-difference-and-explicit-height-basis.md): the original curve, quotient, positive $K$ action and base point.
- [R816](R816-original-all-prime-real-cusp-orbit-and-degree-coprimality.md): exact cusp field and single orbit after the original $L$ base change.
- [R818](R818-original-primitive-cusp-coefficients-and-unramified-Hom-existence.md): the original first-cusp coefficient and an actual nonzero Hom evaluation.
