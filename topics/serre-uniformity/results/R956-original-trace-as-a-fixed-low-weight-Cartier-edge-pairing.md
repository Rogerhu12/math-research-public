# R956 — The original high-weight trace as a fixed-low-weight Cartier edge pairing

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / literature_frontier.

**Status: proved.** This result gives an exact comparison between the complete original R932 supersingular trace and a Serre pairing on the fixed-low-weight space. The second vector of that low-weight pairing is obtained by a specific Cartier edge and a specific supersingular interpolation problem. It is not replaced by the named low-weight CM form. The nonvanishing of that particular edge value remains to be proved.

The comparison preserves R932's original full-six marking, its inverse coefficient Frobenius, the factor $1/6$ in its scalar differential, and the actual descent factors $d_1,m_{\mathrm I},c_h^{\mathrm F}$. It does not identify the trace with a same-label normal derivative; R945's counterexamples to that further inference remain in force.

## 1. Original objects and the comparison to be proved

Work first on the same connected fine tame full-six curve $X$ as R944–R953. Let $C$ be the complete cusp divisor, $\omega$ its Hodge line, and $\Sigma$ the full reduced Hasse divisor. The perfect coefficient field $\kappa$ contains the original full-six marking; for residue calculations it may be extended so that the finitely many points of $\Sigma$ are rational. All formulas descend from that extension.

The original two rows are
$$
(r,k,F,V)=
\begin{cases}
(2,p-1,V_{p-1}^{\dagger},V_4^\dagger),&p\equiv11\pmod{12},\\
(8,p-7,V_{p-7}^{\dagger},V_{10}^\dagger),&p\equiv5\pmod{12},
\end{cases}
\qquad p\ge41.
\tag{956.1}
$$
Thus $k=p+1-r$ and $r<p-1$. The Serre application additionally retains $p\equiv2,5\pmod9$. The dagger and all tame, determinant, and norm transports mean the original ones. Put
$$
M_a=H^0(X,\omega^a),\qquad S_a=H^0(X,\omega^a(-C)).
$$

Write $\mathcal A$ for the Hasse invariant and
$$
\mathcal B=\partial_{p-1}\mathcal A,\qquad
\mathcal T_aH=6(\mathcal A\partial_aH+a\mathcal BH).
$$
The original Fourier coordinate is $Q$, with
$$
\mathcal A(Q)=1,\qquad
\mathcal T(H)(Q)=\Theta_QH(Q),\qquad
K_\rho=\operatorname{KS}(\rho^2)=6\,dQ/Q
\quad\text{in the original Tate frame}.
\tag{956.2}
$$
Here the last equality is at that Tate cusp, not an identification of an arbitrary frame with the Tate frame.

For a local Hodge frame $\rho$ put
$$
A=\mathcal A/\rho^{p-1},\quad
Y_\rho=Y/\rho^{\operatorname{wt}Y},\quad
b_P=(\mathcal B/\rho^{p+1})(P).
$$
At $P\in\Sigma$,
$$
dA(P)=b_PK_\rho(P),\qquad b_P\ne0.
\tag{956.3}
$$
R946's actual Bol operator is
$$
\mathscr D_r:S_k\longrightarrow S_{p+r+1},\qquad
\mathcal T^rH=6^r\mathcal A^r\mathscr D_rH.
\tag{956.4}
$$
For the named source,
$$
\mathscr D_rF=6^{-r}\mathcal A V.
\tag{956.5}
$$

Let $G=\mathcal T^{r-1}F$ and $g_P=(G/\rho^{pr})(P)$. R932 gives
$$
g_P=c_rb_P^{r-1}F_P,\qquad
c_r=-6^{r-1}(r-1)!.
\tag{956.6}
$$
The complete fine supersingular trace and the high-weight finite pairing are
$$
S=\sum_{P\in\Sigma}\frac{g_P^{\,1+1/p}}{b_P^r},
\qquad
\mathcal H_k(F,F)=
\sum_{P\in\Sigma}\frac{F_P^{p+1}}{b_P^k},
\qquad
S^p=c_r^2\mathcal H_k(F,F).
\tag{956.7}
$$
Every fine supersingular point occurs. Zero values at elliptic points are retained, and no special point is given a new weight.

We shall define an additive $p^{-1}$-semilinear map
$$
\mathscr K_r:S_{p+r+1}\longrightarrow S_{r+2}
\tag{956.8}
$$
and choose $Y_F\in S_{p+r+1}$ by the full supersingular interpolation condition
$$
\boxed{\quad
Y_F|_\Sigma=
r!\,\frac{F^p}{\mathcal B^{\,p-r-1}}\Big|_\Sigma.
\quad}
\tag{956.9}
$$
The result is the exact equality
$$
\boxed{\quad
S=\frac{6^{r-2}}r
\left\langle z_V,\mathscr K_rY_F\right\rangle_X,
\quad}
\tag{956.10}
$$
where $z_V\in H^1(X,\omega^{-r})$ is precisely R947's original low-weight principal-parts class. The right side is independent of the choice of the interpolating lift $Y_F$.

## 2. The explicit Cartier edge, including its frame and root

Let $\operatorname{Car}$ denote the Cartier operator on scalar one-forms. It is additive and $p^{-1}$-semilinear, with
$$
\operatorname{Car}(f^p\alpha)=f\operatorname{Car}(\alpha),
\qquad
\operatorname{Car}\left(\sum_n a_nQ^n\,\frac{dQ}{Q}\right)
=\sum_n a_{pn}^{1/p}Q^n\,\frac{dQ}{Q}.
\tag{956.11}
$$
The coefficient roots, rather than an operator which merely drops the other indices, are essential here.

Define $\mathscr K_rY$ locally by
$$
\boxed{\quad
\frac{\mathscr K_rY}{\rho^{r+2}}\,K_\rho
=
\operatorname{Car}\!\left(A^{r-1}Y_\rho K_\rho\right).
\quad}
\tag{956.12}
$$
This is a global definition. Under $\rho'=z\rho$, the scalar one-form inside Cartier changes by
$$
z^{(r-1)(1-p)-(p+r+1)+2}=z^{-pr}.
$$
Consequently its Cartier image changes by $z^{-r}$. This is exactly the change of $(\mathscr K_rY/\rho^{r+2})K_\rho$, since $K_{\rho'}=z^2K_\rho$.

The input to Cartier is regular at every noncusp point. At a cusp, $A$ is a unit, $K_\rho$ has a logarithmic pole, and the cuspidal $Y$ vanishes; hence the input is an ordinary regular one-form. Cartier preserves regular one-forms. Using $\Omega_X^1=\omega^2(-C)$ proves that the output in (956.12) is a cusp form of weight $r+2$. This also proves regularity at every supersingular point without dividing by $A$.

In the original Tate frame, (956.2) and $6^{1/p}=6$ give the exact Fourier rule
$$
\mathscr K_rY(Q)=\sum_{n\ge1}y_{pn}^{1/p}Q^n
\quad\text{if}\quad
Y(Q)=\sum_{n\ge1}y_nQ^n.
\tag{956.13}
$$
The whole Fourier expansion principle therefore gives
$$
\mathscr K_r\mathscr D_r=0,
\tag{956.14}
$$
because $\mathscr D_rH(Q)=6^{-r}\Theta_Q^rH(Q)$ and every coefficient at an index divisible by $p$ vanishes.

For $U\in S_{r+2}$ set
$$
\mathscr U_{\mathrm{low}}U:=\mathscr K_r(\mathcal AU).
\tag{956.15}
$$
It is the actual semilinear mod-$p$ Fourier operator on that low-weight space, with coefficient roots as in (956.13). No choice of a Frobenius-conjugate tame marking is suppressed by this notation. Naturality of (956.12) gives the original tame transports. On each actual prime-to-$p$ Hecke arrow, the coefficient formula also shows that $\mathscr K_r$ commutes with the normalized arrow: the two weights differ by $p-1$, so their Fourier factors $\ell^{p+r}$ and $\ell^{r+1}$ coincide in $\mathbf F_p$. If the arrow changes the marking, its target marking is retained on both sides.

## 3. A fixed-rank connection complex whose edge is exactly $\mathscr K_r$

This section identifies the map (956.12) with an actual connection-complex edge and determines both end spaces of its cokernel sequence. It includes the cusps and supersingular points.

Let $\mathscr H$ be R944's canonical rank-two logarithmic Gauss–Manin bundle. Put
$$
\mathscr E_{\mathrm{Bol}}
=\operatorname{Sym}^{r-1}\mathscr H\otimes F_X^*\omega,
\tag{956.16}
$$
where $F_X^*\omega$ has its canonical Cartier connection. Consider the compact-support logarithmic extension
$$
\mathscr D_c(\mathscr E_{\mathrm{Bol}})
=
\left[
\mathscr E_{\mathrm{Bol}}(-C)
\xrightarrow{\nabla}
\mathscr E_{\mathrm{Bol}}\otimes\Omega_X^1
\right].
\tag{956.17}
$$
The target is equivalently $\mathscr E_{\mathrm{Bol}}(-C)\otimes\Omega_X^1(\log C)$. Thus the displayed differential is well-defined at the cusps.

### 3.1 Elimination of the intermediate Hodge pieces

The Hodge graded lines of (956.16) are $\omega^{k+2i}$ for $0\le i\le r-1$. The component of the connection lowering the Hodge index $i$ to $i-1$ is $i$ times Kodaira–Spencer. Each $i=1,\ldots,r-1$ is a unit. Eliminating these intermediate pairs identifies (956.17), as a complex of additive sheaves (or after Frobenius pushforward as an $\mathcal O_X$-linear complex), with
$$
\left[
\omega^k(-C)
\xrightarrow{\ (-1)^{r-1}\mathscr D_r/(r-1)!\ }
\omega^{p+r+1}(-C)
\right].
\tag{956.18}
$$
Here elimination means solving successively for the next Hodge coefficient so that every component of the derivative except the top one vanishes. It is a differential-operator construction on the chosen bottom section, not a claim of an $\mathcal O_X$-linear splitting of the Hodge filtration.

For both its normalization and its existence globally, verify this construction explicitly on the ordinary Igusa cover in R944's unchanged frames:
$$
e=\mathfrak a,\qquad
f=a^{-p}\sigma_\rho,\qquad
\eta=\operatorname{KS}(e^2),\qquad
\nabla e=f\eta,\quad\nabla f=0,
\quad a=\mathfrak a/\rho.
$$
The symbol $e^p$ in the next formula denotes the horizontal frame of $F_X^*\omega$. Let $D$ be dual to $\eta$ and set $h=H/\mathfrak a^k$. The lift with bottom Hodge coefficient $H$ is
$$
s_H=
\sum_{i=0}^{r-1}\frac{(-1)^i}{i!}D^ih\,
e^if^{r-1-i}\otimes e^p.
\tag{956.19}
$$
The coefficient of each non-top component of $\nabla s_H$ is the derivative of its coefficient plus $(i+1)$ times the next coefficient; they cancel. The remaining component is
$$
\nabla s_H=
\frac{(-1)^{r-1}}{(r-1)!}
D^rh\,e^{r-1}\otimes e^p\,\eta.
\tag{956.20}
$$
R944's scalar derivative rule gives
$$
D^rh=\frac{\mathcal T^rH}
{6^r\mathfrak a^{\,k+r(p+1)}}.
$$
Converting the top term in (956.20) to the Hodge frame yields $\mathcal T^rH/(6^r\mathcal A^r)=\mathscr D_rH$, precisely (956.18).

For extension across $\Sigma$, perform the same successive solving in any regular Hodge frame: the only inverses required are the units $1,\ldots,r-1$ and the Kodaira–Spencer line-bundle isomorphism. The regularity of the connection and that isomorphism proves that the lift is regular. Its uniqueness with prescribed bottom coefficient and vanishing lower derivative components makes the lifts glue. At a cusp use logarithmic Kodaira–Spencer and sections vanishing at that cusp; logarithmic differentiation preserves this vanishing. This proves (956.18) on the entire compact curve.

### 3.2 Cohomology sheaves: no extra contribution supported at $\Sigma$

Let $F_X$ now denote absolute Frobenius, so the pushed-forward differential is $\mathcal O_X$-linear for $a\cdot s=a^ps$.

R953's $p$-curvature calculation implies that the horizontal line of (956.16) is generated locally by
$$
\sigma_\rho^{r-1}\otimes\rho^p.
$$
Its transition factor under $\rho'=z\rho$ is $z^{p(2-r)}$. Regular horizontal coefficients are $p$th powers of regular functions. The domain of (956.17) requires cusp vanishing; the unique root of a horizontal coefficient must likewise vanish. Consequently
$$
\mathcal H^0\!\left(F_{X,*}\mathscr D_c(\mathscr E_{\mathrm{Bol}})\right)
=\omega^{2-r}(-C).
\tag{956.21}
$$

We determine $\mathcal H^1$ explicitly, including its local freeness. At an interior point choose a formal coordinate $t$, keep the horizontal nonvanishing $\sigma_\rho$, and choose a regular complementary vector $\nu$ with $\langle\nu,\sigma_\rho\rangle=1$. Horizontality of the pairing gives
$$
\nabla\nu=\sigma_\rho\xi.
$$
If $K_\rho=\kappa(t)\,dt$, R953(953.29) gives
$$
\psi(\partial_t)=-\kappa(t)^p N,\qquad N\nu=\sigma_\rho,\quad N\sigma_\rho=0.
$$
For this two-dimensional unipotent connection, direct differentiation gives
$$
\psi(\partial_t)
=-\left(\operatorname{Car}(\xi)/dt\right)^pN.
$$
Indeed, the $(p-1)$st derivative of $\sum a_nt^n$ is $-\sum a_{pn+p-1}t^{pn}$. It follows that
$$
\operatorname{Car}(\xi)=K_\rho.
\tag{956.22}
$$
In particular this Cartier image is a unit one-form even at a supersingular point.

Subtracting an exact form from $\xi$ by replacing $\nu$ with $\nu-g\sigma_\rho$ puts it in the form
$$
\xi=a(t^p)t^{p-1}\,dt,\qquad a(t^p)\ \text{a unit}.
$$
Over $\kappa[[t^p]]$, decompose source and target using $1,t,\ldots,t^{p-1}$ and the monomials $\nu^i\sigma_\rho^{r-1-i}\otimes\rho^p$. For $1\le m<p$, the source summand $t^m$ maps to the target summand $t^{m-1}dt$ by
$$
mI+a(t^p)t^pN.
$$
This is invertible, since $N$ is nilpotent. The remaining summand maps by $a(t^p)N$ to the summand $t^{p-1}dt$. On $\operatorname{Sym}^{r-1}$ the nonzero lowering coefficients are $1,\ldots,r-1$, all units. Its kernel and cokernel are free of rank one. The cokernel is represented by $\nu^{r-1}\otimes\rho^p\,t^{p-1}dt$; no torsion is supported at a supersingular point.

The global cokernel coordinate is obtained by pairing a one-form in (956.17) with the horizontal dual vector $\sigma_\rho^{r-1}\otimes\rho^{-p}$, applying scalar Cartier, and multiplying the resulting coordinate by $\rho^r$. This is a unit isomorphism on the computed local cokernel. Its target is
$$
\omega^r\otimes\Omega_X^1=\omega^{r+2}(-C).
$$

At a cusp check this in the original Tate frame without changing its coordinate. The domain is $Q\kappa[[Q]]$ times the monomial module, and the target is the same scalar module times $dQ/Q$. The connection matrix is $\Theta_Q+6N$. Decompose into exponents $1,\ldots,p$ over $\kappa[[Q^p]]$. For $1\le m<p$ the block $mI+6N$ is invertible; for $m=p$ it is $6N$. Its cokernel generator has differential $Q^p\,dQ/Q$, whose Cartier image is $Q\,dQ/Q=dQ$. Thus the cokernel is the regular, cuspidal target just asserted, with no extra skyscraper quotient at a cusp. We have proved
$$
\mathcal H^1\!\left(F_{X,*}\mathscr D_c(\mathscr E_{\mathrm{Bol}})\right)
=\omega^{r+2}(-C).
\tag{956.23}
$$
On a Hodge-top one-form corresponding to $Y\in S_{p+r+1}$, the pairing in this construction is exactly $A^{r-1}Y_\rho K_\rho$. The induced edge is therefore (956.12), including its sign and coefficient roots.

### 3.3 The complete cokernel sequence

Both global line bundles in (956.18) have $H^1=0$: their Serre dual spaces are $M_{2-k}$ and $M_{1-p-r}$, which vanish because their weights are negative and $\deg\omega>0$. Degree-one hypercohomology is therefore the actual global cokernel of $\mathscr D_r$.

Let $(\operatorname{coker}\mathscr D_r)_{\mathrm{Fr}}$ denote that additive cokernel with scalar action $c\cdot[Y]=[c^pY]$. The cohomology-sheaf exact sequence on a curve, applied to (956.21–23), is
$$
\boxed{\quad
0\longrightarrow H^1(X,\omega^{2-r}(-C))
\longrightarrow(\operatorname{coker}\mathscr D_r)_{\mathrm{Fr}}
\xrightarrow{\ \mathscr K_r\ }S_{r+2}
\longrightarrow0.
\quad}
\tag{956.24}
$$
The last map is $\kappa$-linear under the displayed scalar action, and is $p^{-1}$-semilinear on the original cokernel. The left term is Serre-dual to $M_r$; it includes the Eisenstein contribution. Its dimension and the right dimension depend only on the fixed tame level and $r$, not on $p$.

This is not an assertion that the left Hecke module can be discarded. Its action is the one supplied by this actual connection and its Serre duality. The sequence is natural for the original prime-to-$p$ correspondences and tame transport; exact tame idempotents may be applied since their orders are units. With relative Frobenius, the same statement has its line bundles and scalar fields on $X^{(p)}$. The absolute convention above makes each semilinearity explicit.

## 4. The same Bol complex is obtained by contracting the original primitive

There is a direct source check between (956.16) and the actual R947/R953 primitive. The normalized contraction with $\sigma_\rho$, followed by tensoring with $\rho^p$, is
$$
c_\sigma(v_1\cdots v_r)
=
\frac1r\sum_{i=1}^r
\langle v_i,\sigma_\rho\rangle
v_1\cdots\widehat v_i\cdots v_r\otimes\rho^p.
\tag{956.25}
$$
It is a regular horizontal map $\operatorname{Sym}^r\mathscr H\to\mathscr E_{\mathrm{Bol}}$: the frame factors cancel, and the two factors used to define it are horizontal. It kills $\sigma_\rho^r$, hence the entire horizontal polar part of $W$. Thus $c_\sigma W$ is globally regular.

Substitute R944's exact expression for $Z$ in $W=6Z+6^{r+1}r!\widetilde g\,\sigma_\rho^r/A^p$. In the original Igusa frames, contraction sends $e^{r-j}f^j$ to $(r-j)e^{r-j-1}f^j\otimes e^p/r$. Reindexing with $i=r-1-j$ and using $D^ih=h_i/6^i$ in (956.19) gives
$$
\boxed{\quad
c_\sigma W=(-1)^{r-1}6^r(r-1)!\,s_F
=-6^r(r-1)!\,s_F.
\quad}
\tag{956.26}
$$
The second equality uses the original even $r$. Both sides are regular, and equality on the ordinary locus gives equality globally.

Likewise $c_\sigma\Omega_V$ is the Hodge-top one-form corresponding to $\mathcal AV$. Applying $\nabla$ to (956.26) recovers exactly $6^r\mathscr D_rF=\mathcal AV$. Thus this fixed-rank Bol complex is tied to the same original source and its actual Gauss–Manin primitive, beyond agreement of weights or Hecke eigenvalues.

## 5. A global residue comparison using the regular remainder

R947 supplies the global rational primitive
$$
\nabla W=\Omega_V,\qquad
\operatorname{pp}_P(W)
=L_P\frac{\sigma_\rho^r}{A^p},
\qquad
L_P=-\frac{V_Pb_P^{p-r-2}}{r+1}.
\tag{956.27}
$$
Write $\mu_P=L_P^{1/p}$. The principal parts $\mu_P\rho^{-r}/A$ define exactly $z_V$. Set
$$
W_{0,P}=W-L_P\sigma_\rho^r/A^p.
$$
This is regular. R953(953.26) computes its bottom Hodge quotient, in the frame $\rho^{-r}$, as
$$
q_P=-6^r(r-1)!\,\frac{F_P}{b_P}.
\tag{956.28}
$$
Use the normalized symmetric-power pairing of R944; since $r$ is even, $\langle\nu^r,\rho^r\rangle_r=1$ when $\langle\rho,\nu\rangle=1$.

For arbitrary $Y\in S_{p+r+1}$ form the global meromorphic $\operatorname{Sym}^r\mathscr H$-valued differential
$$
\Omega_Y=\frac{Y_\rho}{A}\rho^rK_\rho.
\tag{956.29}
$$
It is intrinsic: $Y/\mathcal A$ has weight $r+2$. It has only simple poles at $\Sigma$ and is regular at the cusps. The scalar differential $\langle W,\Omega_Y\rangle_r$ has poles only at $\Sigma$; $W$ is regular at the cusps and $Y$ is cuspidal.

At $P$, its contribution from the polar part in (956.27) is
$$
L_PY_\rho A^{r-p-1}K_\rho.
\tag{956.30}
$$
Here $\langle\sigma_\rho^r,\rho^r\rangle_r=A^r$ because $r$ is even. The regular remainder contributes the residue
$$
\operatorname{Res}_P
\left(\frac{Y_\rho}{A}
\langle W_{0,P},\rho^r\rangle_rK_\rho\right)
=\frac{q_PY_P}{b_P}.
\tag{956.31}
$$

The residue-Cartier identity $\operatorname{Res}(\operatorname{Car}\alpha)=(\operatorname{Res}\alpha)^{1/p}$, together with (956.11), gives
$$
\left[
\operatorname{Res}_P\!\left(
\frac{\mu_P}{A}
\operatorname{Car}(A^{r-1}Y_\rho K_\rho)\right)
\right]^p
=
\operatorname{Res}_P\left(
L_PY_\rho A^{r-p-1}K_\rho\right).
\tag{956.32}
$$
The residue on the left, before the $p$th power, is exactly the local Serre pairing of the principal part defining $z_V$ with $\mathscr K_rY$.

Sum over the complete $\Sigma$ and apply the global residue theorem to $\langle W,\Omega_Y\rangle_r$. Equations (956.28–32) prove
$$
\boxed{\quad
\left\langle z_V,\mathscr K_rY\right\rangle_X^p
=6^r(r-1)!
\sum_{P\in\Sigma}\frac{F_PY_P}{b_P^2}
\qquad(Y\in S_{p+r+1}).
\quad}
\tag{956.33}
$$
Over a coefficient field not splitting $\Sigma$, use the residue traces; extension to a splitting perfect field proves the same equality.

The sign in (956.33) is positive: the residue theorem negates the regular-remainder residue, while that remainder has the negative sign in (956.28). There is no additional $r!$ from the normalized symmetric-power pairing. This compares the actual regular remainder of $W$, rather than inferring anything from a nonzero low diagonal.

Taking $Y=\mathcal AU$ gives
$$
\boxed{\quad
\langle z_V,\mathscr U_{\mathrm{low}}U\rangle_X=0
\qquad(U\in S_{r+2}).
\quad}
\tag{956.34}
$$
This whole-space annihilation accounts for independence of the interpolation lift.

## 6. The precise original interpolation and all trace constants

The weight of the right side of (956.9) is
$$
pk-(p-r-1)(p+1)=p+r+1.
$$
It is a section on $\Sigma$ because $\mathcal B$ is nonzero there. R946(946.13) is the exact sequence
$$
0\longrightarrow S_{r+2}
\xrightarrow{\ \mathcal A\ }S_{p+r+1}
\longrightarrow H^0(\Sigma,\omega^{p+r+1})
\longrightarrow0.
\tag{956.35}
$$
A cuspidal $Y_F$ satisfying (956.9) therefore exists. Original tame and geometric-deck isotypic conditions are retained by their unit averaging idempotents. Any two such lifts differ by $\mathcal AU$.

This particular interpolation is required by the actual Cartier preimage equation; it is not a new candidate source. R952 gives for every $H\in S_k$
$$
(\mathscr UH)^p
=\mathcal A^kH-6^r\mathcal T^{p-1-r}(\mathscr D_rH),
$$
and on the full Hasse divisor
$$
\mathscr O_r(H)
=r!\frac{(\mathscr UH)^p}{\mathcal B^{p-r}},
\qquad
\mathscr O_r(H)=\frac{\mathscr D_rH}{\mathcal B}\Big|_\Sigma.
\tag{956.36}
$$
Thus $\mathscr UH=F$ requires precisely $\mathscr D_rH|_\Sigma=Y_F|_\Sigma$.

Insert (956.9) in (956.33):
$$
\boxed{\quad
\left\langle z_V,\mathscr K_rY_F\right\rangle_X^p
=6^r r!(r-1)!\,\mathcal H_k(F,F).
\quad}
\tag{956.37}
$$
Equation (956.34) proves directly that this pairing is unchanged by any other permitted interpolation lift.

Comparison with (956.7) gives
$$
\frac{c_r^2}{6^r r!(r-1)!}
=\frac{6^{r-2}}r.
$$
This is in $\mathbf F_p^\times$, so its unique $p$th root is itself. This proves (956.10), with no change of phase or scalar source.

Finally, R932's actual scalar functional on its full original norm extension is
$$
\lambda_h(\Phi_k(F)_{\mathrm{full}})
=
\frac{m_{\mathrm I}(c_h^{\mathrm F})^{1/p}}
{d_1\,6^r(r-1)!}\,S.
$$
Hence the complete original comparison is
$$
\boxed{\quad
\lambda_h(\Phi_k(F)_{\mathrm{full}})
=
\frac{m_{\mathrm I}(c_h^{\mathrm F})^{1/p}}
{36\,d_1\,r!}
\left\langle z_V,\mathscr K_rY_F\right\rangle_X.
\quad}
\tag{956.38}
$$
The degree $d_1$ is the actual fine-cover degree and $m_{\mathrm I}$ the actual norm multiplier. The original nonzero source coefficient $c_h^{\mathrm F}$ has not been normalized away. The factor $36$ comes from the two explicit six normalizations, not a substitution of a numerical orbit count for $d_1$.

## 7. The weight-four row: one unique lift and one exact scalar

For $r=2$ descend by the original tame invariants to $H_6$. R918 proves that its compact coarse curve has genus zero and one cusp, and
$$
S_4(H_6)=\kappa V_4^\dagger,\qquad
\delta V_4^\dagger=\zeta V_4^\dagger.
\tag{956.39}
$$
Moreover
$$
M_2(H_6)=0.
\tag{956.40}
$$
Indeed, by tame Kodaira–Spencer invariant weight-two forms are differentials on the coarse genus-zero curve with at most a logarithmic pole at its one cusp. At a tame elliptic point, an invariant regular differential descends to a regular differential, with no extra pole. The space is therefore $H^0(\mathbf P^1,\Omega^1(\text{one point}))=0$. This proof works over the residue field since every stabilizer order is prime to $p$.

Here $F$ has the original $\delta=\zeta$ character; the right side of (956.9) has $\delta=\zeta^2$, since $p\equiv-1\pmod3$ and $\mathcal B$ is fixed. The kernel $\mathcal AS_4$ of (956.35) has only $\delta=\zeta$. Thus there is a **unique** original $\delta=\zeta^2$ interpolation lift $Y_F$.

Exact tame invariants in (956.24), with (956.40), give
$$
(\operatorname{coker}\mathscr D_2)_{\mathrm{Fr}}
\xrightarrow{\ \sim\ }S_4(H_6).
\tag{956.41}
$$
The coefficient roots interchange the nontrivial deck characters. Therefore
$$
\boxed{\quad
\mathscr K_2Y_F=\alpha V_4^\dagger,\qquad
\alpha=\bigl([Q^p]Y_F\bigr)^{1/p}.
\quad}
\tag{956.42}
$$
This uses the original normalization $[Q]V_4^\dagger=1$. It does not assert $\alpha\in\mathbf F_p$.

There is an exact relation with the actual bad Cartier chain. If $\alpha=0$, (956.41) gives $Y_F=\mathscr D_2H$ for $H$ in the actual $\delta=\zeta^2$ high-weight space. By (956.36), $\mathscr UH$ and $F$ have identical evaluations on $\Sigma$. Evaluation on $S_{p-1}$ is injective: its kernel is $\mathcal AS_0=0$. Hence $\mathscr UH=F$. Conversely, if such an actual $H$ exists, (956.36) and uniqueness of the negative-character interpolation give $\mathscr D_2H=Y_F$, and $\alpha=0$ by (956.14). Thus
$$
\alpha=0
\quad\Longleftrightarrow\quad
\text{there is actual }H^-\text{ with }\mathscr UH^-=F.
\tag{956.43}
$$
This is R955's bad-chain condition, whose shortest possible nilpotent chain has length three.

R950 proves $\langle z_V,V_4^\dagger\rangle_X\ne0$. Equation (956.10) becomes
$$
S=\frac{\alpha}{2}\,\langle z_V,V_4^\dagger\rangle_X.
\tag{956.44}
$$
Thus $\alpha$ is a concrete single remaining scalar, defined by a unique original interpolation and an exact original Fourier coefficient. Its nonvanishing has not been proved here.

## 8. The weight-ten row and the remaining scope

For $r=8$, (956.24) has the fixed low-weight left term dual to the complete $M_8$ and the right term $S_{10}$. One cannot discard the left term merely because R942 proves that the actual double-$T_5$ zero-primary line in $S_{10}(H_6)$ is simple. Any localization of (956.24) must retain the action on both ends and the actual transpose transport.

The exact trace formula (956.10) needs none of that additional vanishing. Its value depends only on the class of $\mathscr K_8Y_F$ modulo the actual $\mathscr U_{\mathrm{low}}S_{10}$, by (956.34). R950's functional $\langle z_V,-\rangle_X$ is supported on the specified simple CM line after the original double-Hecke projection. Determining the actual component of this particular $\mathscr K_8Y_F$ on that line, rather than substituting an arbitrary nonzero vector of the same Hecke type, remains necessary.

In both rows, (956.38) is a genuine source-preserving reduction of the original complete high trace to a fixed-low-weight Serre operation. A subsequent crystalline interpretation must identify this specific Cartier/interpolation operation with an explicitly normalized divided Frobenius entry on the actual CM realization. Neither a general perfect pairing nor an abstract height-two source establishes that identification. The original ramified Hodge-content obstruction of R916 remains in force.

No new finite-prime arithmetic computation was performed. The proof uses R932, R944, R946–R947, R950, R952–R953 and R955 with their original conventions, together with the explicit local connection and residue calculations given above.

