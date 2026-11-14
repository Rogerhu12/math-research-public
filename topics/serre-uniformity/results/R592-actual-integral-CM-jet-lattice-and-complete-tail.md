# R592 — The actual integral CM jet lattice and its complete primitive tails

> Recovery, 2026-11-14. The old scratch and in-memory stores were lost. This is a reconstructed full proof of the previously reviewed result, with new bytes and a new hash. It does not claim to reproduce the old 16,247-byte document, SHA e8e766d81c1b965919e6df403bba57fb6ca1f890e05d05059d300b7d6c23aca0. The old checker and its exact certificate were not recovered, and no earlier numerical experiment was repeated for this reconstruction. All the statements below are proved algebraically. The scope correction of R575 is in force throughout.

## 1. Statement and absolute normalization

Let $p\ge41$ be prime, $p\equiv5\pmod6$. Fix the specified primitive local character
$\theta=\theta_{-1}$ of the nonsplit torus and the actual six-level markings of R575. The actual global family has the cubic direction $\kappa_4$, not the withdrawn opposite-direction identification. Set

$$
e=p^2-1,\qquad s=p(p-1),\qquad \varpi^e=p,\qquad
\lambda=\varpi^s,\qquad v_p(\lambda)=\frac p{p+1}=:\sigma.
\tag{592.1}
$$

Allow a sufficiently large coefficient extension and use $v_p(p)=1$. No assertion that every CM value lies in an unramified field is needed.

The source is the actual full-level CM branch, with good elliptic family

$$
E_t:y^2=x^3+tx-1,\qquad \omega=\frac{dx}{2y},\qquad \eta=x\omega.
\tag{592.2}
$$

Fix the flat coordinate and flat Hodge frame in Section 5. For either actual tame vector, write its resulting weight-two value as

$$
\mathcal F_{\rm flat}(z)=\sum_{n\ge0}\frac{M_n}{n!}z^n.
\tag{592.3}
$$

The normalization is the raw cusp-normalized Cartan trace, not an unspecified scalar multiple. The main integral statement is

$$
\boxed{\quad
v_p\!\left(\frac{M_n}{n!}\right)\ge-\frac{np}{p+1}
\quad(n\ge0).\quad}
\tag{592.4}
$$

Equivalently, $\lambda^n M_n/n!$ is integral for every $n$. This is a bound on the actual algebraic Hodge section and its flat expansion. It is not obtained by identifying a cusp lattice with a Néron cotangent lattice. If a separately identified quotient differential is a nonzero scalar multiple of this section, that scalar is retained in the comparison; its zero set is unchanged, but its absolute valuation is not silently discarded.

For the original $c_1$ marking, only $n\equiv2\pmod3$ occur. For the $S_6$-translated $c_0$ marking, only $n\equiv0\pmod3$ occur. Sections 6–8 give complete convergent primitive bounds. In particular:

* if the actual $c_1$ value has $v_p(M_2)=-1$, its primitive has no nonzero zero on the branch $v_p(a-1)\ge4$;
* if the actual $c_0$ value $M_0$ is a unit, its primitive has no nonzero zero for $v_p(z)\ge1$;
* a character-free version already suffices on $v_p(z)\ge4/3$.

These are local zero statements. No rank-zero quotient, rational-point zero image, or transport of a candidate between $c_0$ and $c_1$ is supplied by this theorem.

## 2. The specified finite-type lattice is integral at every cusp

We recall the part of R434 that is independent of its corrected global application. Put

$$
\Lambda=\mathcal O^{\mathbb F_p}/\mathcal O\mathbf1,
\qquad \mathsf G=\mathrm{PGL}_2(\mathbb F_p).
\tag{592.5}
$$

Let $e_r$ be the indicator class at $r$, with $\sum_re_r=0$, and use $e_r$ for $r\ne0$ as an integral basis. The Borel acts by affine permutations. For $\theta$ or $\theta^{-1}$ the Weyl action is

$$
w e_r=-\frac1p\sum_{y\in\mathbb F_{p^2}^{\times}}
\theta(y)e_{r\mathrm N(y)+\operatorname{Tr}(y)}.
\tag{592.6}
$$

The exact finite-field identity proved in R434 §§2–3 is

$$
\sum_{\substack{y\ne0\\r\mathrm N(y)+\operatorname{Tr}(y)=a}}
 y^{p-1}=1
\qquad(r,a\in\mathbb F_p),
\tag{592.7}
$$

and the inverse character has the same sum, by Frobenius conjugation. This includes the zero-trace and zero-norm fibers. If $S_{r,a}$ is the characteristic-zero Teichmüller sum, then $S_{r,a}\equiv1\pmod p$ for every fiber. Thus (592.6), written in the actual basis, has coefficients

$$
-\frac{S_{r,a}-S_{r,0}}p\in\mathcal O.
\tag{592.8}
$$

Borel and Weyl generate $\mathsf G$, so the entire group preserves $\Lambda$. In particular this is an integral statement about every translate, not only a numerically observed cancellation in one vector.

The reduction map

$$
\ell([\phi])=\sum_{a\in\mathbb F_p}\phi(a)
\tag{592.9}
$$

is well defined on $\Lambda/p\Lambda$ and $\mathsf G$-invariant. For a nonsplit torus $\mathsf T'$ of order $p+1$, its average

$$
A_{\mathsf T'}=\frac1{p+1}\sum_{g\in\mathsf T'}g
\tag{592.10}
$$

is integral, and $\ell(A_{\mathsf T'}e_r)=1$. Hence the averaged vector is primitive in its rank-one invariant lattice. There is no additional division by $p$ to impose after taking this average.

The actual newform has trivial $p$-Euler factor. If its local cusp vector is $f=\sum a_nQ^n$, the isomorphism of this finite type sends

$$
e_r\longmapsto f_r=\sum_n a_n\zeta_p^{-nr}Q^n.
\tag{592.11}
$$

The relation $\sum_re_r=0$ is respected because $a_{pn}=0$. Therefore any vector of $\Lambda$ has integral cusp coefficients, and every finite-group translate does as well.

It remains necessary to include the actual tame direction. Use

$$
H_0(\tau)=f_\theta(\tau/(6p)),\qquad
H_2(\tau)=f_\theta(2\tau/(3p)).
\tag{592.12}
$$

In coefficient basis $(H_0,H_2)$ the actual right-slash matrices are

$$
S=\begin{pmatrix}0&1/4\\4&0\end{pmatrix},\qquad
T=\zeta\begin{pmatrix}-1&0\\-4&1\end{pmatrix}.
\tag{592.13}
$$

In the integral basis $(H_0,4H_2)$ they are

$$
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
T=\zeta\begin{pmatrix}-1&0\\-1&1\end{pmatrix}.
\tag{592.14}
$$

Both are invertible over $\mathcal O$ for $p>3$. For completeness, the factors $4$ are fixed by the actual degeneracy functions, not a numerical eigenvector normalization. The Fourier support of $f_\theta$ is $n\equiv1\pmod3$, and its inert-$2$ relation is $a_{2n}=0$ for odd $n$ and $a_{4n}=-2a_n$. A CRT lift of the tame translation shifts its argument by $-1/6$; splitting its odd and even terms gives $H_0\mapsto-\zeta H_0-4\zeta H_2$ and $H_2\mapsto\zeta H_2$. The weight-two Fricke substitution at level $9p^2$ gives $H_0\mapsto4H_2$ and $H_2\mapsto H_0/4$ in the fixed actual normalization. Even before fixing the Fricke sign, its scalar is a unit, which is all that the integrality assertion requires. At $p$ the Weyl element fixes $e_0$: the exact trace-zero character sum is $-(p-1)$ and each nonzero-trace sum is $1$, so (592.6) evaluates to $e_0$. This separates the tame substitution from the already integral $p$ factor. The $p$-level and tame actions commute. Tensoring this explicitly stable tame lattice with (592.5) therefore proves all-cusp integrality of both actual vectors

$$
F_1=H_0-4\zeta^2H_2,\qquad
F_0=-\zeta^2H_0+4H_2,
\tag{592.15}
$$

after the same integral Cartan projection. This argument retains the fixed full-level Weil-pairing component. Other components are transported by the actual level-structure/Galois action: at the fixed $p$-adic place the $\mu_p$ action changes the cusp phase in (592.11), and conjugation of $\mu_3$ replaces $\theta$ by its inverse in the same finite type. No claim that arbitrary $\theta^u$ share an unspecified lattice is used.

Finally, the two cubic global directions are locally identical at $p$: since $p\equiv2\pmod3$, the unique cube root of $4$ in $\mathbb F_p$ lifts to $\mathbb Z_p^\times$. The finite lattice argument consequently applies to the actual R575 family, without recovering any of the withdrawn global rank-zero assertions.

## 3. From all cusps to an integral Hodge section

We use the full-level integral $q$-expansion principle, including at primes dividing the level. In Anthony Kling, *Comparison of integral structures on the space of modular forms of full level N*, [arXiv:2310.18869](https://arxiv.org/pdf/2310.18869), Lemma 2.1 and Proposition A.17 identify the sections of $\omega^{\otimes k}$ on the full-level integral modular model by integrality at **all** cusps. This is precisely why Section 2 established every translate. The statement is used after the required coefficient/base extension and then pulled back to the actual formal model.

The algebraic normalization is fixed by the Tate differential

$$
\omega_{\rm Tate}=dX/X=2\pi i\,dz_{\rm an}.
\tag{592.16}
$$

If the elliptic period lattice is $\Omega\mathcal O_K$, the corresponding CM evaluation is

$$
\mathcal F(E_0,dz)=\left(\frac{2\pi i}{\Omega}\right)^2
 F(\tau_{\rm CM}).
\tag{592.17}
$$

The raw expression $H_0=f_\theta(\tau/(6p))$ in (592.12) is already the chosen cusp-integral weight-two vector. No second factor $(6p)$ or $(6p)^{-1}$ is inserted when applying the $q$-expansion principle. A degeneracy pullback of a differential and the raw weight-two vector would have different displayed scalings; (592.12), (592.16), and (592.17) specify which one is used here.

It follows that $F_0$ and $F_1$ define actual integral sections of $\omega^{\otimes2}$ on the full-level modular model. This assertion concerns that Hodge line bundle. It does not identify it with a Néron lattice for a quotient of the Jacobian.

## 4. The full marking extends on the scaled CM disc

The actual full-level branch is indispensable. We use R378 §§2–3, whose local geometry is retained under its R575 correction. At the Drinfeld CM point the full $p$-level structure gives every torsion section

$$
T(S)\in\varpi\mathcal A,
\qquad
\overline{T(aP+bQ)/\varpi}=a\alpha+b\beta,
\tag{592.18}
$$

with $\alpha,\beta$ linearly independent over $\mathbb F_p$. Its Weierstrass polynomial has roots $T(S)$; thus the coefficient $w_j$ of $T^j$ is divisible by $\varpi^{p^2-j}$. In particular the coefficient of $T^p$ in $[p](T)$ is divisible by $\varpi^s$.

For (592.2), that coefficient has the form

$$
c_p(t)=tV(t)+pW(t),\qquad V(0)\in\mathcal O^\times.
\tag{592.19}
$$

One sees $V(0)$ directly from the coefficient of $x^{p-1}$ in $(x^3+tx-1)^{(p-1)/2}$. Since $v_p(p)>v_p(\lambda)$, comparison gives $t\in\lambda\mathcal A$.

This alone would not prove a parameter statement. R378 computes the reduced Dickson invariant

$$
\mathcal D=
\frac{\alpha^{p^2}\beta-\alpha\beta^{p^2}}
 {\alpha^p\beta-\alpha\beta^p}.
\tag{592.20}
$$

In Cartan coordinates $A_0^{p+1}-B_0^{p+1}=c$ and $V=A_0B_0$, its value at a CM lift is

$$
\mathcal D=-c^{p-2}V+O(V^2).
\tag{592.21}
$$

The coefficient is a unit, and the other CM lift has the same property. Therefore

$$
\tau=t/\lambda
\tag{592.22}
$$

is an integral parameter on the actual fine formal disc, which is $\operatorname{Spf}R[[\tau]]$ after the stated tame base extension. The prime-to-$p$ six-level sections extend étale-locally, and all the full $p$-level sections are already present in (592.18). The map to the integral full-level modular model thus extends on this disc; it is not merely a map of its punctured generic fiber. In particular the integral section obtained in Section 3 can genuinely be pulled back here.

Cartan is free at these fine CM lifts and the normalizer exchanges the two lifts; neither introduces a new $p$-denominator. For the $c_1$ branch the remaining effective $\mu_3$ quotient is only taken after this fine calculation. The $S_6$-translated $c_0$ marking changes the tame marking of the same elliptic deformation, so it has the same fine integral scale (592.22).

Since $\omega=dx/(2y)$ is a generator of the Hodge bundle for the smooth family, the actual value in this frame satisfies

$$
\mathcal F_t(\lambda\tau)\in R[[\tau]].
\tag{592.23}
$$

This establishes absolute integrality before any passage to a quotient abelian variety.

## 5. Gauss–Manin and the complete flat-coordinate estimate

For (592.2), the Gauss–Manin connection in $(\omega,\eta)$ is

$$
\frac d{dt}\binom{\omega}{\eta}=
\begin{pmatrix}a&b\\c&-a\end{pmatrix}
\binom{\omega}{\eta},\qquad
\begin{aligned}
a&=-\frac{t^2}{4t^3+27},\\
b&=-\frac9{2(4t^3+27)},\\
c&=-\frac{3t}{2(4t^3+27)}.
\end{aligned}
\tag{592.24}
$$

All three power series are integral for $p>3$. Let the fundamental matrix with value $I_2$ at $t=0$ have columns $(u_1,v_1)^T$ and $(u_2,v_2)^T$. The recurrence for an integral linear differential system gives

$$
v_p([t^n]u_i),\ v_p([t^n]v_i)\ge-v_p(n!).
\tag{592.25}
$$

Indeed, multiplying the degree-$n$ recurrence by $n!$ expresses it as integral combinations of the preceding $k!$-scaled coefficients. This proves (592.25) for every $n$, not just a computed jet. The determinant is one because the connection has trace zero.

In the CM splitting used for the actual jets, the flat coordinate and flat Hodge frame are

$$
z=\frac{u_2}{u_1},\qquad
\frac{dz}{dt}=\frac b{u_1^2},\qquad
z=-\frac t6+O(t^4),\qquad
\omega_{\rm flat}=\frac\omega{u_1}.
\tag{592.26}
$$

Thus the flat value is

$$
\mathcal F_{\rm flat}(z(t))=u_1(t)^2\mathcal F_t(t).
\tag{592.27}
$$

These formulas fix the unit as well as the valuation of the parameter: $z'(0)=-1/6$. In particular $M_0=\mathcal F_t(0)$. The jets are derivatives of this same actual section; no fixed auxiliary elliptic function is substituted for the moving modular form.

Set $t=\lambda\tau$. Since $\sigma=p/(p+1)>1/(p-1)$, (592.25) implies

$$
u_1(\lambda\tau)\in1+\mathfrak m_R[[\tau]],
\qquad
u_i(\lambda\tau),v_i(\lambda\tau)\in R[[\tau]].
\tag{592.28}
$$

In particular $u_1$ is an integral unit. The series

$$
Z=\frac{z(\lambda\tau)}\lambda
\tag{592.29}
$$

has integral coefficients and unit linear term $-1/6$. To verify the possible integration denominators directly, the degree-$k$ coefficient of $b/u_1^2$ has valuation at least $-v_p(k!)$; after integration and division by $\lambda$, its scaled valuation is at least

$$
k\sigma-v_p((k+1)!)\ge
k\left(\sigma-\frac1{p-1}\right)>0\qquad(k\ge1).
\tag{592.30}
$$

We used $v_p((k+1)!)\le k/(p-1)$. Hence $Z(\tau)$ is an invertible integral formal change of parameter, and its inverse is integral as well. Combining (592.23), (592.27), and (592.29) yields

$$
\mathcal F_{\rm flat}(\lambda Z)\in R[[Z]].
\tag{592.31}
$$

Its degree-$n$ coefficient is exactly $\lambda^n M_n/n!$. This proves (592.4), including the whole infinite series and its absolute scale.

## 6. The two tame selection rules

Use the right-slash convention of (592.13). For $v=(1,-4\zeta^2)^T$,

$$
(TS)v=v,\qquad Sv=(-\zeta^2,4)^T,\qquad
(TS)(Sv)=\zeta^2(Sv).
\tag{592.32}
$$

The CM point is fixed by the analytic $ST$ transformation. Its automorphy factor is $\tau_{\rm CM}+1=-\zeta^2$. A weight-$2+2n$ jet consequently matches the first vector exactly when $n\equiv2\pmod3$ and the second exactly when $n\equiv0\pmod3$. Equivalently,

$$
\begin{aligned}
\mathcal F_1(z)&=\sum_{r\ge1}\frac{M_{3r-1}}{(3r-1)!}z^{3r-1},\\
\mathcal F_0(z)&=\sum_{r\ge0}\frac{M_{3r}}{(3r)!}z^{3r}.
\end{aligned}
\tag{592.33}
$$

The Cartan trace commutes with this tame calculation. These are the actual two tame markings. An $S_6$ operation on the full-level marking has not here been identified with an automorphism of the coarse curve carrying every candidate between $a=0$ and $a=1$.

## 7. The full c1 primitive on the deep disc

Choose the primitive vanishing at the CM point. Put

$$
U=\frac{z^3}{p^3},\qquad
L_1(U)=\sum_{r\ge1}C_rU^r,\qquad
C_r=\frac{p^{3r}M_{3r-1}}{(3r)!}.
\tag{592.34}
$$

This equals the integral of $\mathcal F_1(z)\,dz$. By (592.4),

$$
v_p(C_r)\ge1+\frac{3r-1}{p+1}-v_p(r).
\tag{592.35}
$$

The bound tends to $+\infty$ linearly, up to a logarithm. Thus it controls the complete restricted series, not only finitely many Taylor coefficients.

Suppose now that the separately established actual value satisfies $v_p(M_2)=-1$. On $U=pV$ one has

$$
p^{-3}L_1(pV)
=V\left(\frac{pM_2}{6}+V H_1(V)\right),
\qquad H_1(V)\in\mathfrak m_R\langle V\rangle.
\tag{592.36}
$$

For $r\ge2$, the valuation of its $V^r$ coefficient is at least

$$
r-2+\frac{3r-1}{p+1}-v_p(r)>0.
\tag{592.37}
$$

For $r=2$ this is $5/(p+1)>0$; for $r\ge3$ the integer $r-2-v_p(r)$ is nonnegative and the remaining fraction is positive. The leading coefficient $pM_2/6$ is a unit. The bracket in (592.36) is consequently a unit throughout $|V|\le1$, and $U=0$ is the only zero for $v_p(U)\ge1$.

The relation to the actual coarse branch is fixed, not chosen for convenience:

$$
j(E_t)=\frac{6912t^3}{4t^3+27},\qquad
j=6912a^3(1-a^3),\qquad z=-t/6+O(t^4).
\tag{592.38}
$$

Near $a=1$, these imply

$$
z^3=\frac38(a-1)+O((a-1)^2),\qquad
U=\frac38w_1(1+\epsilon(w_1)),\qquad
w_1=\frac{a-1}{p^3}.
\tag{592.39}
$$

Here $\epsilon(0)=0$ and $v_p(\epsilon(w_1))>0$ on the stated deep branch. This last estimate follows directly by substituting $v_p(t)\ge4/3$ in the factorial bounds (592.25)–(592.30), together with the unit factors in the exact $j$ formulas. It does not assume that every unscaled flat-coordinate coefficient is integral. Hence $v_p(U)=v_p(w_1)$ there. The zero statement covers $v_p(a-1)\ge4$ and does not by itself cover shallower discs or supply a global zero-image relation.

## 8. The full c0 primitive and a character-free variant

For the second marking define

$$
L_0(z)=\sum_{r\ge0}\frac{M_{3r}}{(3r+1)!}z^{3r+1}.
\tag{592.40}
$$

At $z=pV$, (592.4) gives

$$
v_p\!\left(\frac{p^{3r+1}M_{3r}}{(3r+1)!}\right)
\ge1+\frac{3r}{p+1}-v_p(3r+1).
\tag{592.41}
$$

For $r\ge1$ the right side is strictly greater than one. To see this without a finite test, let $h=v_p(3r+1)$. If $h=0$ it is immediate. If $h=1$, the integer $(3r+1)/p$ is $2\pmod3$, since $p\equiv2\pmod3$; hence $3r\ge2p-1>p+1$. If $h\ge2$, then $3r\ge p^h-1>h(p+1)$ for $p\ge41$. This proves the assertion in all cases, and the bound tends to infinity.

If $M_0$ is a unit, then

$$
p^{-1}L_0(pV)=V\bigl(M_0+V^3H_0(V)\bigr),
\qquad H_0(V)\in\mathfrak m_R\langle V\rangle.
\tag{592.42}
$$

Thus $z=0$ is its only zero for $v_p(z)\ge1$.

For an application that only uses (592.4), not the character selection rule, write the entire primitive as
$L(z)=\sum_{n\ge0}M_n z^{n+1}/(n+1)!$. If $M_0$ is a unit and $v_p(z)\ge4/3$, the ratio of its $n$th term to $M_0z$, for $n\ge1$, has valuation at least

$$
n\left(\frac13+\frac1{p+1}\right)-v_p(n+1)>0.
\tag{592.43}
$$

Indeed, if $h=v_p(n+1)>0$, then $n\ge p^h-1\ge5^h-1>3h$; if $h=0$ it is immediate. This supplies the same unique-zero conclusion on the smaller disc without using a selection rule.

## 9. Conditional application to a genuinely identified cubic twist

This paragraph states exactly how a later global input can use the theorem. It is not such a global input. Suppose an actual curve $X_{p,d}$ has a separately proved compatible quotient map and a commuting geometric twist identification with the same local Cartan channel. In the notation of that identification, put $a'=\sqrt[3]d\,b$ near $b=0$ and use the actual fine parameter

$$
t=3a'(1-a'^3)^{1/3}(1-2a'^3)^{-2/3}.
\tag{592.44}
$$

On the deep branch this gives $v_p(t)=v_p(a')$, while (592.26) gives $v_p(z)=v_p(t)$. If $v_p(d)=m\in\{1,2\}$ and $v_p(b)=k\ge1$, then

$$
v_p(z)=\frac m3+k\ge\frac43.
\tag{592.45}
$$

Under that separately proved commuting twist square, the pullback of the specified quotient logarithm is a nonzero scalar times the same primitive $L_0(z)$. If the quotient has rank zero and the particular rational-point difference is known to have zero logarithm, a unit $M_0$ forces $b=0$ by (592.43). Each italicized logical input has a distinct role: the actual quotient must occur, the twist must preserve the chosen channel, the image must have zero logarithm, and $M_0$ must be the actual normalized value. The local theorem alone supplies none of the first three. In particular it never reinstates R348's withdrawn rank-zero interpretation of the untwisted $d=1$ family.

## 10. Dependencies and recovery boundary

The proof uses the already available local contents of R378 §§2–3, R434 §§1–4, and the actual direction and tame matrices of R575/R571, restated explicitly here. Its one external geometric input is Kling's full-level integral $q$-expansion principle cited in Section 3. The Hodge/flat comparison, the complete factorial bounds, and both primitive lemmas are proved above.

Neither R588's toric norm identity nor a uniform nonvanishing theorem is used to prove (592.4). Results R588/R589/R595 are needed only when one wants to verify the hypotheses “$M_0$ is a unit” or “$v_p(M_2)=-1$” for a particular actual channel. The local primitive statements are valid with those hypotheses stated explicitly. No fixed-curve coefficient is substituted for an actual modular-curve jet.

The old source and 3,638-byte checker certificate were lost. Their reported earlier execution is not represented here as a new run, and no reconstruction of their exact bytes is claimed. This recovered proof is self-contained for its new bounds and retains the explicit available dependencies; the manifest records the currently read source hashes and the unrecovered historical hashes.
