# R861 — The original CM Néron Fourier basis and the actual normal parameters

Date: 2026-11-16. Status: **proved**. This computes the individual original-label factors of R728's inverse-different lattice and identifies R378's ramification normalization with actual Néron formal parameters. R859 transports the result to the original target. It does not compute the original quotient's first normal coefficient.

## 1. Fixed original fields, scales and labels

Use the range and objects of R859:
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
n=p+1=6m,\quad e=p^2-1,
\quad K=\mathbf Q(\sqrt{-3}),
\tag{861.1}
$$
and retain the original positive finite character $\varepsilon$, the cyclic extensions $H/K$ and $L/K$, and the actual elements
$$
\alpha=\sqrt[3]4,\qquad r=r_0/\alpha,\qquad
r^6=b/16,\qquad C/L:y^2=x^3+b,
\quad \omega_C=dx/(2y).
\tag{861.2}
$$
These are R725's elements; in particular the factor $16$ is not replaced by a new elliptic twist. At $p$, $\alpha\in\mathbf Q_p^\times$ and $\kappa_4$ is trivial.

Let $R_0=W(\overline{\mathbf F}_p)$, $K_0=\operatorname{Frac}(R_0)$ and
$$
R=R_0[\varpi],\qquad \varpi^e=p,
\qquad \tau(\varpi)=\xi_e\varpi
\tag{861.3}
$$
as in R378. Base change the chosen local embeddings of $H$ and $L$ to $K_0$, writing $H_0^{\mathrm{loc}}=K_0H$ and $L_0^{\mathrm{loc}}=K_0L$. They are totally tamely ramified of degrees $n$ and $m$. The notation $H_0^{\mathrm{loc}}$ here means this local base change of the actual $H$, not a redefinition of R725's global field $H_0$.

Choose $g\in\operatorname{Gal}(H_0^{\mathrm{loc}}/K_0)$ by restricting the original inertia generator $\tau$. Put
$$
\xi=\varepsilon(g)^{-1}=\xi_e^{p-1},\qquad
\sigma=g|_{L_0^{\mathrm{loc}}},\qquad
\rho=g(r)/r.
\tag{861.4}
$$
The equality of characters in (861.4) uses the original Teichmüller orientation $\theta_h(u)=[u]^{-h(p-1)}$, not its reciprocal. R725(725.17) gives the corresponding leading action on $r_0$, while R390 gives the positive coordinate-ring weight.

Use all positive labels first, and then the actual primitive subset:
$$
\mathcal A=\{h=6a+1:0\le a<m\},\qquad
\mathcal H=\{h\in\mathcal A:(h,n)=1\},
\quad |\mathcal H|=g_A=\varphi(n)/2.
\tag{861.5}
$$
The full Weil restriction has dimension $m$; its primitive factor has dimension $g_A$. These two dimensions are not interchanged below.

## 2. An actual eigen-uniformizer and the complete inverse-different basis

Define the exact finite projection
$$
v=\frac1n\sum_{j=0}^{n-1}\xi^{-j}g^j(r).
\tag{861.6}
$$
R725(725.15–17) gives
$$
v_p(r)=1/n,\qquad g^j(r)/r\equiv\xi^j
\pmod{\mathfrak m_{H_0^{\mathrm{loc}}}}.
\tag{861.7}
$$
Since $n$ is a $p$ unit, the leading terms in (861.6) add to $r$, rather than cancel. Thus
$$
g(v)=\xi v,\qquad v/r\equiv1
\pmod{\mathfrak m_{H_0^{\mathrm{loc}}}},\qquad v_p(v)=1/n.
\tag{861.8}
$$
Both $r$ and $v$ transform by $\xi^m$ under $g^m$, which generates $\operatorname{Gal}(H_0^{\mathrm{loc}}/L_0^{\mathrm{loc}})$. Consequently
$$
u:=r/v\in\mathcal O_{L_0^{\mathrm{loc}}}^{\times},\qquad
\nu:=v^6\in L_0^{\mathrm{loc}},\qquad
v^n=p\delta,\quad\delta\in R_0^\times.
\tag{861.9}
$$
Here $u$ is the target-field unit; it is unrelated to the source disk coordinate $w$ below. The polynomial $T^m-p\delta$ is Eisenstein, so
$$
\mathcal O_{L_0^{\mathrm{loc}}}=R_0[\nu],\qquad
\mathfrak D^{-1}_{L_0^{\mathrm{loc}}/K_0}
=\nu^{1-m}\mathcal O_{L_0^{\mathrm{loc}}}.
\tag{861.10}
$$
The derivative factor $m$ is a unit. This is the same inverse different as $F_p'(b)^{-1}R_0[b]$ in R728: $b=16u^6\nu$ is the original uniformizer, and the different is an ideal of the extension, independent of the chosen Eisenstein generator.

R728(728.17) gives the actual action on the trace realization of cotangents:
$$
T^*(f\omega_C)=\sigma^{-1}(\rho f)\omega_C.
\tag{861.11}
$$
Since $\rho=\xi\sigma(u)/u$, for $h=6a+1$ put
$$
f_h=u\,v^{1-h}=u\nu^{-a}\in L_0^{\mathrm{loc}}.
\tag{861.12}
$$
A direct substitution, retaining the inverse $\sigma$ in (861.11), gives
$$
\sigma^{-1}(\rho f_h)
=\sigma^{-1}(\xi\sigma(u)v^{1-h})
=\xi^h f_h.
\tag{861.13}
$$
The $m$ elements $u\nu^{-a}$, $0\le a<m$, form a complete $R_0$-basis of (861.10): multiplication by the unit $u$ preserves that fractional ideal, and $\nu^{-(m-1)},\ldots,1$ is its displayed power basis. Therefore
$$
\boxed{\omega_{\mathcal B}\otimes_{\mathbf Z_p}R_0
=\bigoplus_{h\in\mathcal A}R_0\,\beta_h,
\qquad \beta_h=f_h\omega_C.}
\tag{861.14}
$$
Here $B=\operatorname{Res}_{L^+/\mathbf Q}C$ and $\mathcal B$ is its actual Néron model; (861.14) is the base change of R728(728.28), not an alternate lattice. It is an equality, not just an inclusion based on eigenvectors.

The $T$-root $\xi^h=\varepsilon(g)^{-h}$ has order $n$ exactly when $(h,n)=1$. Applying the actual, $p$-integral primitive projector gives
$$
\boxed{\omega_{\mathcal A^{\mathrm{mod}}}\otimes R_0
=\bigoplus_{h\in\mathcal H}R_0\,\beta_h.}
\tag{861.15}
$$
The identification is R728(728.25–30), whose addition isogeny has degree prime to $p$.

## 3. Exact comparison with the good CM Fourier basis

Over $H_0^{\mathrm{loc}}$, the actual Weil restriction splits into $m$ conjugate elliptic factors. For $0\le i<m$ write
$$
r_i=g^i(r),\qquad C_i:y^2=x^3+g^i(b),
\qquad E_{27}:Y^2=X^3+16.
\tag{861.16}
$$
The true good-model isomorphism is
$$
D_{r_i}:E_{27}\longrightarrow C_i,
\qquad (X,Y)\longmapsto(r_i^2X,r_i^3Y),
\qquad D_{r_i}^*\omega_{C_i}=r_i^{-1}\omega_{27,i}.
\tag{861.17}
$$
Thus all constants in (861.2) are retained. In R728's trace identification, $f_h\omega_C$ means $\sum_i g^i(f_h)\omega_{C_i}$. Because
$$
\frac{g^i(f_h)}{r_i}
=\frac{g^i(u)\xi^{i(1-h)}v^{1-h}}
       {g^i(u)\xi^iv}
=\xi^{-ih}v^{-h},
\tag{861.18}
$$
we obtain the exact equality of generic-fiber differentials
$$
\boxed{\beta_h=v^{-h}\Omega_h,
\qquad \Omega_h=\sum_{i=0}^{m-1}\xi^{-ih}\omega_{27,i}.}
\tag{861.19}
$$

The matrix in (861.19), with $h=6a+1$, is the Fourier matrix for the primitive $m$-th root $\xi^{-6}$, followed by multiplication of its $i$-th column by $\xi^{-i}$. Its inverse has entries obtained by the inverse Fourier matrix and $1/m$. All these entries are integral, and $m$ is a unit. Hence its determinant is a $p$ unit. It follows that $\Omega_h$, $h\in\mathcal A$, form the full good-model cotangent lattice. Restricting the primitive projector selects exactly $h\in\mathcal H$, still as a full direct summand.

Finally $v$ and $\varpi^{p-1}$ have the same exact inertia character and the same valuation. Their quotient is therefore a unit in the fixed field:
$$
\epsilon:=v/\varpi^{p-1}\in R_0^\times.
\tag{861.20}
$$
Equations (861.15,19) become
$$
\boxed{\omega_{\mathcal A^{\mathrm{mod}}}\otimes R_0
=\bigoplus_{h\in\mathcal H}
 R_0\,\epsilon^{-h}\varpi^{-(p-1)h}\Omega_h.}
\tag{861.21}
$$
This proves the exact coincidence, up to displayed unramified units, with the normalization in R378/R390.

Let $c$ denote the canonical Néron base-change map to the good model over $R$. Pullback of its good cotangent basis satisfies
$$
c^*\Omega_h=v^h\beta_h.
\tag{861.22}
$$
Its elementary-divisor exponents, with $v_\varpi(\varpi)=1$, are exactly
$$
\boxed{t_h=(p-1)h\qquad(h\in\mathcal H).}
\tag{861.23}
$$
Equivalently the normalized exponents are $h/(p+1)$. This statement follows from the complete lattice bases, so it does not mistake an inertia weight alone for a computed Néron base-change index.

All diagonalizations above were made after unramified base change. The original $\mathbf Z_p$ lattice remains the trace lattice from $L^+$ in R728. The formulas were derived from its base change, and equality of lattices is preserved and detected by the faithfully flat extension to $R_0$. No claim is made that the separate $f_h$ belong to $L^+$ or that their Fourier basis descends term by term to $\mathbf Q$. Its descent is the original descent of that actual lattice.

## 4. The normalization defines actual Néron formal parameters

Choose the complete one-dimensional good formal factors from R390, with coordinates $Y_h$ having initial differential $\Omega_h$ and exact semilinear weight
$$
\tau(Y_h)=\xi_e^{t_h}Y_h.
\tag{861.24}
$$
Such a choice is obtained by choosing a parameter with the specified initial differential and applying the same finite, prime-to-$p$ average used in R378(378.35). It preserves the complete-BT factor. The scalar normalizations in (861.19) are units in the good lattice.

The integral primitive local endomorphism idempotents also act on the Néron formal group over $R_0$. One way to check the completion involved here is to use the characteristic-zero formal logarithm: at every fixed total degree, the coefficients of an endomorphism are polynomial expressions in its differential matrix with fixed denominators. A $p$-adically convergent sequence of integral endomorphisms therefore converges coefficientwise to an integral formal-group endomorphism. This extends the integral action to the $p$-completed endomorphism order. Its mutually orthogonal idempotents split the formal group into the corresponding one-dimensional factors. The product map is a formal isomorphism, as its tangent map is an isomorphism and the idempotents sum to one.

Take any formal parameter $X_h$ on the Néron factor over $R_0$ whose initial differential is $\beta_h$. The base-change map respects these factors. Write
$$
c^*Y_h=\sum_{r\ge1}a_{h,r}X_h^r\in R[[X_h]].
\tag{861.25}
$$
Equation (861.22) says $a_{h,1}=v^h$. Since $X_h$ is defined over $R_0$, equivariance gives the same coefficient weight for every degree:
$$
\tau(a_{h,r})=\xi_e^{t_h}a_{h,r}.
\tag{861.26}
$$
Consequently $a_{h,r}/v^h\in K_0$. Integrality of $a_{h,r}$ and $0<h/n<1$ force this quotient to be integral: its integer $p$-valuation is strictly greater than $-1$. Therefore
$$
\boxed{X_h^{\mathrm{can}}:=v^{-h}c^*Y_h
\in R_0[[X_h]],\qquad
X_h^{\mathrm{can}}=X_h+O(X_h^2).}
\tag{861.27}
$$
It is an actual Néron formal parameter, with an integral compositional inverse. This conclusion uses the explicitly computed inverse different and good Fourier basis; it was not assumed in R378.

For additional clarity, the normalized group law in this coordinate is integral. A nonlinear good-group coefficient of total degree $d\ge2$, after the same scaling, is multiplied by $v^{h(d-1)}$. Equivariance makes its valuation an integer, and integrality before scaling makes that integer positive. Thus this one-dimensional Néron formal group has law
$$
X+X'+p\,XX'\,Q_h(X,X'),\qquad Q_h\in R_0[[X,X']].
\tag{861.28}
$$
Terms with one exponent zero are absent by the formal-group identity axiom. In particular its reduction is the additive formal group. This concerns the Néron formal neighborhood, not a good-reduction BT group over $R_0$.

## 5. The actual original disk and its still unknown normal coefficient

Keep exactly
$$
\gamma(P)=q([P-c_1])=q([P-c_0])-\beta,
\qquad
z=\frac{a-1}{\varpi^{3p(p-1)}},\quad
w=\frac{a-1}{p^3},\quad
z=\varpi^{3(p-1)}w.
\tag{861.29}
$$
For the explicit target model, apply these formulas to $j_p\gamma$, with the same original $q$ and the prime-to-$p$ isogeny of R859. If
$$
G_h^{\mathrm{mod}}(w)
=\varpi^{-t_h}Y_h(j_p\gamma(P(z)))
\big|_{z=\varpi^{3(p-1)}w},
\tag{861.30}
$$
then (861.20,27) gives the exact identity
$$
\boxed{(j_p\gamma)^*X_h^{\mathrm{can}}
=\epsilon^{-h}G_h^{\mathrm{mod}}(w).}
\tag{861.31}
$$
It holds as an integral formal expansion in $w$, and as an identity of Néron formal parameters on $w\in pR_0$ (equivalently $v_p(a-1)\ge4$), where all the formal compositions converge. R378 already proves $G_h^{\mathrm{mod}}\in wR_0\langle w\rangle$; no convergence of an arbitrary formal coordinate on the entire closed unit disk is needed.

Transport $\beta_h$, $\Omega_h$ and $X_h^{\mathrm{can}}$ through the genuine prime-to-$p$ isogeny from R859. Its maps on both Néron and good-model lattices are isomorphisms, and its same-label formal maps have unit linear term. Thus (861.21–23) apply to the original $A$, and (861.31) identifies the original R378 functions with actual Néron formal parameters up to the units and same-factor coordinate changes explicitly controlled in R859. The original base point, $\beta$ and the positive cubic twist have all been retained.

In particular the common coefficient factor
$$
M_h=\min_{r\ge1}v_p([w^r]G_h)
\tag{861.32}
$$
has a concrete meaning as the divisibility of this original Néron formal-coordinate pullback. Its first normal residue is the actual pullback after removing that common factor. This does **not** specify $M_h$, nor prove that the first coefficient of that residue is nonzero. The source map $q$ has not been replaced by an arbitrary vector in the target lattice. The original same-$h$ Cartier/Legendre product, the first normal coefficient, and the required height nonzero statement remain separate tasks.

### Sources and scope

- [R725](R725-original-CM-elliptic-model-and-splitting-field.md), (725.13–18): the original $r_0$, its nonzero leading inertia term, $b$, and the exact real/local fields.
- [R728](R728-original-Weil-restriction-primitive-projector-and-Neron-lattice.md), (728.11–17), (728.21–30): the true $T$ direction, primitive projector, trace convention and inverse-different Néron lattice.
- [R378](R378-actual-cm-disc-parameter-and-uniform-integral-tail.md), (378.30), (378.35–40), and [R390](R390-cm-coordinate-inertia-weight-one-channel-and-cartier-unit.md), §§2–4: the actual source scale, coefficient descent, complete BT factors and coordinate-ring weights. Their retained local scope is that specified by R575.
- [R859](R859-original-prime-to-p-CM-model-and-normal-content-transport.md): the actual original target, prime-to-$p$ isogeny and individual-label normal-content transport.

All calculations here are finite paper identities in the original objects. No new numerical arithmetic or finite-prime scan is used.
