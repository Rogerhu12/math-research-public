# R818 — Original primitive cusp coefficients and an actual all-cusp unramified Hom direction

Date: 2026-11-15. Status: **proved in the precise scope below**. This is a characteristic-zero statement about the original cusp and the original positive CM factor. It does not assert that the cusp coefficient is a $p$-adic unit, nor that the original $c_1$ critical coefficient is nonzero.

## 1. Objects and the original Fourier realization

First let $p\ge41$, $p\equiv5\pmod6$, and put
$$
n=p+1,\qquad K=\mathbf Q(\zeta_3),\qquad
E=\mathbf Q(\zeta_n),\qquad \xi=e^{2\pi i/p}.
$$
Use the original primitive character $\theta=\theta_{-1}$, its coefficient conjugates $\theta_h$ with $h\equiv1\pmod6$, and the original positive cubic twist of [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md). The curve is the smooth normalization
$$
X_p=\operatorname{Norm}\bigl(X_{\rm ns}^+(p)\times_j\mathbf P^1_a\bigr),
\qquad j=6912a^3(1-a^3).
\tag{818.1}
$$
All statements about a cusp below refer to this curve, not to a different cyclic-$p^2$ model.

The finite cuspidal realization and the actual Cartan average are
$$
V_h=E^{\mathbf F_p}/E\mathbf1,\qquad
u_h=\frac1{p+1}\operatorname{Tr}_{\mathsf T_\zeta}e_0
     =\sum_{r\in\mathbf F_p}c_{h,r}e_r,\qquad c_{h,r}\in E.
\tag{818.2}
$$
The Weyl matrix has entries in $E$: its explicit entries are finite sums of $\theta_h(y)$, divided by $p$, as in R592(592.6) and R745(745.8). Thus (818.2) is an $E$-vector; it does not require adjoining $\xi$. The choice of representatives $c_{h,r}$ is immaterial modulo a common constant.

The vector $u_h$ is nonzero. For $h=1$, R588(588R.10) proves that its norm scalar is congruent to $-1\pmod p$. Every $u_h$ here is a coefficient conjugate of this same characteristic-zero vector, because $h$ is primitive and fixes the displayed $\mu_6$ labels. Equivalently, R727(727.2–3) retains its nonzero characteristic-zero norm $N_h$, even when its mod-$p$ Legendre residue vanishes.

Choose the reference full-$6p$ cusp and
$$
Q=e^{2\pi i\tau/(6p)},\qquad
H_{0,h}=f_h(\tau/(6p)),\qquad
H_{2,h}=f_h(4\tau/(6p)).
$$
The normalized original theta newform has $a_1(f_h)=1$. The actual tame line is
$$
H_{0,h}-4\zeta_3^2H_{2,h}.
\tag{818.3}
$$
For each $r$, let $k_r$ be the CRT class modulo $6p$ with $k_r\equiv0\pmod6$ and $k_r\equiv r\pmod p$. The corresponding finite-model translate is $\tau\mapsto\tau-k_r$. Consequently its $Q^m$ coefficient is multiplied by
$$
e^{-2\pi i m k_r/(6p)}=\xi^{-m r/6},
\tag{818.4}
$$
where $6^{-1}$ is taken in $\mathbf F_p$.

This is precisely the general finite-model Fourier map R592(592.11), expressed with the original CRT convention. R745(745.16–18) records its $p=41$ instance; no coefficient from that finite computation is used here. Formula (818.4) follows directly from the two CRT congruences for arbitrary $p>3$.

Since $H_{2,h}$ starts with $Q^4$, the coefficient of $Q$ in the actual Cartan-averaged function is
$$
b_{1,h}=\sum_{r\in\mathbf F_p}c_{h,r}\xi^{-r/6}.
\tag{818.5}
$$
In particular the two tame summands do not cancel this coefficient. Multiplication by the original arithmetic/twist scale $\alpha\sqrt{-3}$, $\alpha^3=4$, and passage from the raw function to a differential multiply (818.5) by nonzero constants. In the convention $2\pi i\,d\tau=(6p)\,dQ/Q$, the resulting leading differential coefficient is $(6p)\alpha\sqrt{-3}\,b_{1,h}$. Any different nonzero normalization of the same actual Hodge line leaves its vanishing unchanged. The displayed coefficient is for the explicitly written $\alpha\sqrt{-3}$ times the averaged raw vector. Passage to a fixed arithmetic Hom differential retains its own nonzero comparison scalar; no period equality or new Manin comparison constant is computed here.

## 2. Exact injectivity of the first-coefficient functional

**Lemma 818.1.** The $E$-linear map
$$
\mathcal W:E^{\mathbf F_p}/E\mathbf1\longrightarrow E(\xi),
\qquad
[c_r]\longmapsto\sum_r c_r\xi^{-r/6},
\tag{818.6}
$$
is an isomorphism.

**Proof.** It is well defined because $\sum_r\xi^{-r/6}=0$. The integers $p$ and $p+1$ are relatively prime, and
$$
[E(\xi):E]
=\frac{\varphi(p(p+1))}{\varphi(p+1)}
=p-1.
\tag{818.7}
$$
Here $E(\xi)=\mathbf Q(\zeta_{p(p+1)})$; the degree computation is the cyclotomic degree formula with coprime conductors. Hence the minimal polynomial of $\xi$ over $E$ is exactly
$$
\Phi_p(T)=1+T+\cdots+T^{p-1}.
$$
After permuting the indices by $r\mapsto-r/6$, a relation in the kernel of (818.6) is a polynomial of degree at most $p-1$ vanishing at $\xi$. It is therefore a scalar multiple of $\Phi_p$. All its coefficients are equal, so its class in the quotient is zero. The source and target both have $E$-dimension $p-1$, proving the assertion. $\square$

Applying the lemma to $u_h\ne0$ proves
$$
\boxed{b_{1,h}\ne0\quad\text{for every original primitive }h.}
\tag{818.8}
$$
No reduction modulo $p$ is made: $\Phi_p(T)$ becomes $(T-1)^{p-1}$ modulo $p$, so (818.6) cannot be used as a mod-$p$ unit argument.

The original cusp has width $6p$. This is proved in [R816](R816-original-all-prime-real-cusp-orbit-and-degree-coprimality.md): the intermediate $Y_p$ cusp has width $2p$, and $a^3=t$, with $\operatorname{ord}(t)=-p$, is totally ramified of degree three. Thus $Q$ is a genuine analytic uniformizer on $X_p$, and a weight-two function beginning with $b_{1,h}Q$ gives a differential with nonzero constant term relative to $dQ$. Equation (818.8) is exactly nonvanishing of the original Hodge line at the original reference cusp.

This proof uses the original split vector and the original Cartan average in characteristic zero. The coefficient-field disjointness in (818.7) is independent of the different cusp-field disjointness with $L$ in R816.

## 3. An actual Hom direction unramified at every cusp

Now impose the original arithmetic range
$$
p\ge41,\qquad p\equiv2,5\pmod9
\tag{818.9}
$$
of [R725](R725-original-CM-elliptic-model-and-splitting-field.md). Keep its actual fields and positive target:
$$
H_0=K(E_{27}[p])^{\mathbf F_p^\times},\qquad
L=H_0^{G_6},\qquad [L:K]=(p+1)/6,\qquad
C/L:y^2=x^3+b.
$$
Let $A=A_{\theta,1}$ and $q:J_{X_p}\to A$ be the original primitive quotient of R575/R616. R725(725.30) proves
$$
A_L\sim_L C^g,\qquad g=\dim A.
\tag{818.10}
$$
Use actual homomorphisms, not arbitrary $L$-linear combinations of differentials:
$$
V=\operatorname{Hom}_L(A_L,C)\otimes_{\mathbf Z}\mathbf Q.
$$

**Theorem 818.2.** There exists $0\ne v\in V$ such that the original curve map
$$
f_v=vq[x-c_0]:X_{p,L}\longrightarrow C
$$
after clearing an integer denominator is unramified at every geometric cusp of $X_{p,L}$.

**Proof.** Choose an actual $L$-isogeny $\iota:A_L\to C^g$, whose existence is (818.10), and let $v_j=\operatorname{pr}_j\circ\iota$. Each $v_j$ is an actual $L$-homomorphism. Since a characteristic-zero isogeny induces an isomorphism on invariant differentials, the $g$ forms
$$
v_j^*\omega_C=\iota^*\operatorname{pr}_j^*\omega_C,\qquad 1\le j\le g,
\tag{818.11}
$$
are an $L$-basis of $H^0(A_L,\Omega^1)$. Thus the asserted spanning statement follows from actual isogeny pullbacks, not from a dimension count. Equivalently, with the fixed positive embedding $K\hookrightarrow L$,
$$
V\otimes_KL\xrightarrow{\;\sim\;}H^0(A_L,\Omega^1),
\qquad v\otimes c\longmapsto c\,v^*\omega_C.
\tag{818.12}
$$
Indeed, the same isogeny identifies $V$ with $K^g$, since $\operatorname{End}^0_L(C)=K$. We use (818.12) to test whether every actual Hom value vanishes; an arbitrary $L$-linear differential combination is not thereby declared to be an actual homomorphism.

The original quotient $q$ has injective pullback on differentials. By its construction in R575 and R616, its complex Hodge image is the span of the coefficient embeddings of the original newform, with the actual tame line (818.3) and actual Cartan average (818.2). The finite local invariant spaces are one-dimensional, and the retained original vectors are nonzero. The positive cubic descent multiplies these analytic representatives by the fixed nonzero twist scale. Therefore each original primitive line just used in (818.8) is indeed a line in this same $q^*H^0(A,\Omega^1)$; it is not a line from a different modular quotient.

If every $v_j$ in (818.11) had zero pullback differential at the reference cusp, their $L$-span and then their complex span would vanish there. This would force all the preceding actual primitive Hodge lines to vanish, contradicting (818.8). Consequently at least one of these actual $L$-homomorphisms has nonzero cusp differential.

[R816](R816-original-all-prime-real-cusp-orbit-and-degree-coprimality.md) proves that all geometric cusps of the original $X_{p,L}$ form one $G_L$-orbit, with residue field $L\mathbf Q(\xi_p)^+$ of degree $(p-1)/2$ over $L$. The zero divisor of the $L$-defined differential $q^*v^*\omega_C$ is $G_L$-stable. Hence nonvanishing at one cusp implies nonvanishing at every cusp. Clearing the denominator of $v$ multiplies its differential by a nonzero integer, so it preserves the assertion. A characteristic-zero map to the elliptic curve is unramified exactly when the pullback of its nonvanishing invariant differential is nonzero. $\square$

The proposition does not require choosing an explicit isogeny or assuming that every nonzero $v\in V$ is unramified. To prove the latter stronger statement by R816's evaluation-kernel argument, one must still identify the actual general-prime semilinear operator and its irreducible rank-one $K[T]$-module. The $p=41$ matrix calculation in R791 is not by itself such a general-prime proof.

## 4. Scope for the continuing problem

This result supplies a genuine characteristic-zero first-cusp coefficient and an actual all-cusp unramified Hom direction for the original primitive factor. It preserves the original positive twist, tame vector, cusp width and Cartan average.

It does not give a $p$-unit, a first nonzero $c_1$ coefficient, the valuation of a Néron/Manin comparison scalar, or a same-$h$ product
$P_{h-1}(1/\sqrt{-3})f_{(h-7)/6}g_{(p-h-4)/6}$ modulo $p$.
It does not identify the original map's poles or prove a height nonvanishing statement. The main completion criterion remains open.

No mathematical computation was run for this proof.

## Original dependencies

- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md), especially (575.4), (575.10–13): the same original curve, tame vector and positive twist.
- [R588](R588-actual-toric-norm-and-CM-normalization.md), (588R.7–10), and [R592](R592-actual-integral-CM-jet-lattice-and-complete-tail.md), (592.5–15): the finite quotient, original average, nonzero $u_1$, and exact Fourier realization.
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md), §§1–2: original primitive coefficient conjugates and retained characteristic-zero toric norms.
- [R745](R745-certified-original-p41-Hodge-and-adelic-input.md), (745.12–18): recorded original CRT and tame phase conventions, used only as a normalization check; its numerical data are not generalized.
- [R616](R616-original-CM-point-difference-and-explicit-height-basis.md), §§1–4, and [R725](R725-original-CM-elliptic-model-and-splitting-field.md), (725.30): the original primitive quotient and its actual $L$-splitting.
- [R816](R816-original-all-prime-real-cusp-orbit-and-degree-coprimality.md), original all-prime real cusp orbit and degree-coprimality theorem: cusp widths, total ramification and the single cusp orbit over $L$.
