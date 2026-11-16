# R898 — A full integral Cartan projector and the original primitive period source

Date: 2026-11-16. Status: proved an integral realization of the full auxiliary nonsplit Cartan, including its determinant-nonsquare elements and exact phase; transported the original CM torus and split vector together; and identified the original same-label primitive/Legendre/sigma product as a specified jet of an actual integral period source. The nonvanishing of that specified jet is not proved.

## 1. The original generic representation and integral theta operators

Retain R881/R886/R897. Put
$$
k=\mathbf F_{p^2},\quad T=\{q\in k^\times:q^{p+1}=1\},
\quad n=p+1,\quad \widetilde\chi(q)=[q],
$$
$$
7\le h\le p-4,\quad h\equiv1\pmod6,\quad (h,n)=1,\qquad
\theta_h(y)=[y]^{-h(p-1)},\quad \mu_h=\widetilde\chi^{\,2h}.
\tag{898.1}
$$
The original pairing parameter is $\gamma\in k^\times$ with
$\overline\gamma=-\gamma$, and the original symplectic coordinates are
$$
u=a+\overline b,\qquad
v=-\frac{\gamma}{2}(a-\overline b).
\tag{898.2}
$$
The positive product theta line bundle, its actual quotient module $\mathcal U_L$, and the original maps $\Gamma_h,\mathcal C_h$ have the meanings of R886.

Let $M_q$ denote R881's actual integral single-factor norm-one theta action. It commutes with the six-primary theta action. On the special fiber,
$$
M_q Q^r m=\widetilde\chi(q)^{-r}Q^r m
\qquad(0\le r<p,\ m\in\mathcal H_0).
\tag{898.3}
$$
The omitted index is $p$. The actual opposite-character projector
$\mathcal P_{2h}$ on the product therefore selects $s-r\equiv2h\pmod n$.

On the generic fiber the original cuspidal representation is the norm model
$$
W_{\mu_h}=
\{\varphi:k\to K':\varphi(q\xi)=\mu_h(q)^{-1}\varphi(\xi)\}.
$$
The fixed split vectors are
$$
\Phi_{t,h}(\xi)=\theta_h(\xi)^{-1}\psi(t\operatorname N\xi)
\quad(\xi\ne0),\qquad \Phi_{t,h}(0)=0.
\tag{898.4}
$$
R881 identifies the original $e_t$ with this exact vector. In particular
$$
\Gamma_h(u)=-p\,u\otimes\Phi_{0,h}
\tag{898.5}
$$
in R886's generic identification normalized by actual quotient pullback. The generic group acts as the identity on $\mathcal U_L$.

The single-factor canonical Weil phase is the proved R881 formula
$$
M_q=\widetilde\chi(q)^{\,1-n/2}\rho_{\rm W}(q)
\tag{898.6}
$$
on its primary factor. The two phases cancel for opposite factors, but do not cancel for two factors with the same $q$. The argument below uses a single factor and keeps the full determinant extension.

## 2. The full auxiliary Cartan from one actual theta factor

Apply $(a,b)\mapsto(a,qb)$. In (898.2) its symplectic matrix over $k$ is
$$
\mathsf M(q)=
\begin{pmatrix}
(1+q^{-1})/2&(q^{-1}-1)/\gamma\\
-\gamma(1-q^{-1})/4&(1+q^{-1})/2
\end{pmatrix}.
\tag{898.7}
$$
Choose $\delta_q\in k^\times$ with $\delta_q^{p-1}=q$ and set
$$
g_q=\delta_q^{-1}\mathsf M(q).
\tag{898.8}
$$
Every entry of $\mathsf M(q)$ has Frobenius equal to $q$ times itself. Thus
$g_q\in\mathrm{GL}_2(\mathbf F_p)$, and
$$
\det g_q=(\operatorname N\delta_q)^{-1}.
\tag{898.9}
$$
Replacing $\delta_q$ by $c\delta_q$, $c\in\mathbf F_p^\times$, changes $g_q$ by the scalar $c^{-1}$, so its projective class is independent of that choice. Because $\mathsf M(q_1)\mathsf M(q_2)=\mathsf M(q_1q_2)$, these classes form a group. The class is the identity only for $q=1$.

Consequently
$$
T_0=\{[g_q]:q\in T\}\subset\mathrm{PGL}_2(\mathbf F_p)
\tag{898.10}
$$
is a full nonsplit Cartan of order $n$, not merely its index-two subgroup. Its fixed points on the projective coordinate $u/v$ are
$$
\pm2/\gamma.
\tag{898.11}
$$
Indeed its matrices have equal diagonal entries and lower-left/upper-right ratio $\gamma^2/4$.

The determinant-nonsquare elements are visible:
$$
\varepsilon(\det g_q)
=(\operatorname N\delta_q)^{-(p-1)/2}
=q^{-n/2}=q^{n/2}.
\tag{898.12}
$$
Thus the nonsquare coset corresponds to the nonsquare coset of the cyclic group $T$ and has not been discarded.

## 3. The exact three-phase calculation

We first record explicitly the determinant convention of the original representation. For $g\in\mathrm{GL}_2(\mathbf F_p)$, put $d=\det g$, and choose $b\in k^\times$ with $\operatorname N b=d$. Then, on $W_{\mu_h}$,
$$
\boxed{
\rho_h([g])=
\theta_h(b)\varepsilon(d)\,
\rho_{\rm W}(b^{-1}g).
}
\tag{898.13}
$$
Here $b^{-1}g$ is regarded as a four-dimensional symplectic transformation of the two $k$ positions. The factor $b^{-1}$ compensates the determinant $d$.

To check (898.13), it suffices to use $\mathrm{SL}_2$ and
$\operatorname{diag}(d,1)$. On $\mathrm{SL}_2$, choose $b=1$ and use R881's canonical norm model. For the latter diagonal matrix the symplectic transformation is
$$
(u,v)\longmapsto(\overline b\,u,b^{-1}v).
$$
The canonical Weil operator is
$$
\rho_{\rm W}\!\left(\operatorname{diag}(\overline b,b^{-1})\right)
 \varphi(\xi)=\varepsilon(\operatorname N b)\,\varphi(b\xi).
$$
The configuration-change scalar is the quadratic character of its $\mathbf F_p$ determinant. It follows either by tensoring the one-dimensional formula
$\rho(\operatorname{diag}(a,a^{-1}))f(x)=\varepsilon(a)f(ax)$, or as follows: the ratio to plain substitution is a character of $\mathrm{GL}_2(\mathbf F_p)$; the one-coordinate diagonal determines that character to be $\varepsilon\circ\det$. The one-dimensional formula is displayed in Liu--Zhang (2.1), and tensor compatibility/uniqueness is the same canonical Weil input used in R881.

Multiplication by the two factors in (898.13) therefore gives exactly
$$
\mathcal D_d\varphi(\xi)=\theta_h(b)\varphi(b\xi),
$$
the original determinant extension in R881 (881.31). Changing $b$ to $bq$ multiplies the displayed scalar by $\theta_h(q)$ and its orthogonal scalar action on $W_{\mu_h}$ by the inverse; hence the formula is choice-independent. Choosing $b$ multiplicatively also verifies products, and projective scalar matrices act trivially. Thus this is the same full extension, not a newly chosen quadratic twist.

For $g_q$ take $b=\delta_q^{-1}$. Then $b^{-1}g_q=\mathsf M(q)$ and
$$
\theta_h(b)=\widetilde\chi(q)^h,\qquad
\varepsilon(\det g_q)=\widetilde\chi(q)^{n/2}.
$$
The remaining canonical Weil factor is, by (898.6),
$$
\rho_{\rm W}(\mathsf M(q))
=\widetilde\chi(q)^{-1+n/2}(1\otimes M_q).
$$
Combining all three factors gives
$$
\boxed{
\rho_h([g_q])
=\widetilde\chi(q)^{\,h-1}(1\otimes M_q)
\quad\text{on }\mathcal P_{2h}\mathcal B_{K'}.
}
\tag{898.14}
$$
This identity includes $q$ in the determinant-nonsquare coset. It uses neither a square-root choice in $T$ nor an identification of $h$ with $h+n/2$.

Define
$$
\boxed{
\Pi_{0,h}=
\mathcal P_{2h}\frac1n
 \sum_{q\in T}\widetilde\chi(q)^{h-1}(1\otimes M_q).
}
\tag{898.15}
$$
It is a genuine integral projector. All its factors are integral commuting torus projectors, and $n$ is a unit. On the selected cuspidal generic fiber it is exactly the full $T_0$ average.

The second index selected in (898.3) is $s=h-1$, and the opposite-character condition then gives $r=p-h$. Hence
$$
\mathcal V_h:=\Pi_{0,h}\mathcal B_{R'}
\quad\text{is a saturated rank-}36\text{ direct summand},
$$
$$
\boxed{\overline{\mathcal V_h}=|p-h,h-1\rangle\mathcal M.}
\tag{898.16}
$$
In particular its generic primary invariant line is one-dimensional. The two lines fixed by the projective square subgroup have not been confused with this one line.

## 4. A unit isomorphism supplied by the original Gauss source

Use the trace-normalized quotient basis $\{u_m\}$ of R897. Formula (897.16) there, followed by the actual integral projector (898.15), kills every displayed layer except the last one. It gives
$$
\Pi_{0,h}\Gamma_h(u_m)
\equiv
\varpi^{p(p-1)}
 P_{h-1}(0)|p-h,h-1\rangle m
\pmod{\varpi^{p(p-1)+1}}.
\tag{898.17}
$$
The unramified coefficient corrections to $\Pi_{0,h}$ are multiples of $p$ and cannot affect this precision. R897 already includes the trace-normalization error and all other integer coefficient corrections.

Because $P_{h-1}(0)$ is a unit and the $36$ vectors in (898.16) are independent, the actual map
$$
\boxed{
\mathcal J_h=
\varpi^{-p(p-1)}\Pi_{0,h}\Gamma_h:
\mathcal U_L\xrightarrow{\ \sim\ }\mathcal V_h
}
\tag{898.18}
$$
is an integral isomorphism. Divisibility follows first in $\mathcal B_{R'}$ from (898.17), then in $\mathcal V_h$ because it is a direct summand. Its reduction is
$$
\overline{\mathcal J_h(u_m)}
=P_{h-1}(0)|p-h,h-1\rangle m.
\tag{898.19}
$$
This is an isomorphism of the actual tame theta modules. It is not a statement about evaluation of their sections at $(O,O)$.

## 5. Moving the original CM torus and the split vector together

Let $s=\sqrt{-3}$ be the original residue, so $\overline s=-s$. Put
$$
\nu=\gamma/2,\qquad c=s\gamma/4\in\mathbf F_p^\times,
\qquad
\mathsf B=
\begin{pmatrix}c&-1/2\\0&1\end{pmatrix},
\qquad
t_*=\frac1{2c}=\frac2{s\gamma}.
\tag{898.20}
$$
No constant here is the unrelated cube root used in the original CM periods.

The affine transformation of $u/v$ defined by $\mathsf B$ carries
$\pm2/\gamma$ to $(-1\pm s)/2$. These are precisely the two fixed points of
$$
\mathsf T_\zeta=
\left\{\begin{pmatrix}a&-b\\b&a+b\end{pmatrix}\right\}
/\mathbf F_p^\times.
$$
Both groups are the full order-$n$ stabilizer of that conjugate pair, so
$$
\boxed{\mathsf T_\zeta=\mathsf B T_0\mathsf B^{-1},\qquad
\mathcal A_h=\rho_h(\mathsf B)\Pi_{0,h}\rho_h(\mathsf B^{-1}).}
\tag{898.21}
$$
The conjugation is in the original full projective group.

The actual Borel action of R881 satisfies
$\rho(\operatorname{diag}(c,1))\Phi_{0,h}=\Phi_{0,h}$ and
$\rho(n(t))\Phi_{0,h}=\Phi_{t,h}$. Since
$$
\mathsf B^{-1}=n(t_*)\operatorname{diag}(c^{-1},1),
$$
it follows that
$$
\boxed{\rho_h(\mathsf B^{-1})\Phi_{0,h}=\Phi_{t_*,h}.}
\tag{898.22}
$$
The split vector is therefore moved by the nontrivial quadratic phase
$\psi(t_*\operatorname N\xi)$. It has not been left fixed while the torus is centered.

For clarity, the generic unipotent operator
$U_t\varphi(\xi)=\psi(t\operatorname N\xi)\varphi(\xi)$ has the exact actual-theta expression, for $t\ne0$,
$$
\boxed{
U_t=-\frac1p\sum_{u\in k}
 \psi(-\operatorname N u/t)\,\rho(\tau(u,0)).
}
\tag{898.23}
$$
Here $(u,0)$ still means the original marked pair
$(u/2,\overline u/2)$. To check (898.23), use the actual modulation
$\rho(\tau(u,0))\varphi(\xi)=
\psi(-\operatorname{Tr}(u\overline\xi))\varphi(\xi)$ and complete the norm square. For any nonzero $a\in\mathbf F_p$,
$$
\sum_{u\in k}\psi(a\operatorname N u)
=1+(p+1)\sum_{b\in\mathbf F_p^\times}\psi(ab)=-p.
$$
Taking $a=-1/t$ gives exactly (898.23), including the minus sign and the denominator.

The numerator in (898.23) is an integral theta operator. No assertion is made that division by $p$ preserves the entire theta lattice.

## 6. The projected phase is an integral scalar, with the original Legendre residue

Let $\mathcal O$ be the unramified coefficient ring for the original finite cuspidal representation and its character values, as in R808. Use its original Hermitian form $G$, linear in the first variable, and put
$$
v_0=\Pi_{0,h}\Phi_{0,h},\qquad
d_h=G(\Phi_{0,h},v_0)=G(v_0,v_0),
$$
$$
\beta_h(t)=\frac{G(\Phi_{t,h},v_0)}{d_h}.
\tag{898.24}
$$
We will prove $d_h\in\mathcal O^\times$. Since the full $T_0$ invariant primary line is one-dimensional, this will also give
$$
\boxed{\Pi_{0,h}\Phi_{t,h}=\beta_h(t)v_0.}
\tag{898.25}
$$

Here is the exact reduction calculation in the original orbit Gram quotient of R808. Put
$$
r=\min(h-1,p-h).
$$
Then $r$ is even, $2r\le p-3$, and the quotient is
$$
W_r=\operatorname{Sym}^{2r}(k^2)\otimes\det^{-r},\qquad
v_{\rm sp}=X^rY^r,\qquad
\langle v_{\rm sp},v_{\rm sp}\rangle=-1.
\tag{898.26}
$$
It retains every original group element and the Frobenius-Hermitian convention. Define
$$
\mathsf H=\begin{pmatrix}1&1\\\nu&-\nu\end{pmatrix},
\qquad
v_T=\mathsf H v_{\rm sp}
=(-2\nu)^{-r}(X^2-\nu^2Y^2)^r.
\tag{898.27}
$$
This vector is defined over $\mathbf F_p$: $r$ is even and
$\overline\nu=-\nu$. The full $T_0$ invariant line in $W_r$ is precisely $kv_T$, since $2r<n$.

Here $\mathsf H\in\mathrm{GL}_2(k)$ need not belong to the original finite group $\mathrm{GL}_2(\mathbf F_p)$. We therefore use the algebraic $\mathrm{GL}_2(k)$-invariant bilinear form on $W_r$, not the all-$g$ finite-group identity with an unsupported extra argument. With the normalization in (898.26), its polynomial matrix-coefficient identity is
$$
\begin{aligned}
\langle v_{\rm sp},g v_{\rm sp}\rangle
&=-(ad-bc)^{-r}\sum_{j=0}^r\binom rj^2(ad)^j(bc)^{r-j}\\
&=-P_r\!\left(\frac{ad+bc}{ad-bc}\right),
\qquad g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{GL}_2(k).
\end{aligned}
\tag{898.27a}
$$
The first equality extracts the coefficient of $X^rY^r$ from
$(ad-bc)^{-r}(aX+cY)^r(bX+dY)^r$; the second is the binomial identity for the Legendre polynomial. Thus (898.27a) holds over $k$ directly. In R808 the reduced original Hermitian form is this bilinear form with Frobenius on the second vector. Both $v_{\rm sp}$ and $v_T$ are $\mathbf F_p$-rational, so that Frobenius is trivial on the vectors used here. Algebraic invariance and (898.27a), applied to $\mathsf H$, consequently give
$$
\langle v_T,v_T\rangle=-1,\qquad
\langle v_{\rm sp},v_T\rangle=-P_r(0).
\tag{898.28}
$$
The cross ratio of $\mathsf H$ is zero. Thus
$$
\overline v_0=P_r(0)v_T,\qquad
\overline d_h=-P_r(0)^2\ne0.
\tag{898.29}
$$
The last nonvanishing also follows immediately from the even-index binomial expression for $P_r(0)$ and $r<p$.

All numerators in (898.24) are integral: $\Phi_{t,h}$ is the original orbit vector $e_t$, $v_0$ is an average of orbit vectors with denominator $n$, and R727/R808 prove integrality for every pair of orbit vectors. Consequently
$$
\boxed{d_h\in\mathcal O^\times,\qquad\beta_h(t)\in\mathcal O.}
\tag{898.30}
$$
This integrality uses the original Gram lattice and a unit denominator; it is not deduced from the generic expression (898.23).

Finally
$$
n(-t)\mathsf H=
\begin{pmatrix}1-t\nu&1+t\nu\\\nu&-\nu\end{pmatrix}
$$
has cross ratio $-t\nu$. Apply the polynomial identity (898.27a) to this matrix. Since $t\in\mathbf F_p$, both $n(t)v_{\rm sp}$ and $v_T$ are $\mathbf F_p$-rational, so the same calculation is also the required reduced Frobenius-Hermitian pairing. It gives
$$
\boxed{
\overline{\beta_h(t)}=\frac{P_r(-t\nu)}{P_r(0)}.
}
\tag{898.31}
$$
For $t=t_*$, one has $t_*\nu=1/s$. Since $r$ is even, and the original reflection identity gives $P_r=P_{h-1}\pmod p$,
$$
\boxed{
\overline{\beta_h(t_*)}
=\frac{P_{h-1}(1/s)}{P_{h-1}(0)}.
}
\tag{898.32}
$$
The denominator is a unit. This proves the residue with the original Legendre argument, not the argument zero of the centered auxiliary torus.

All these scalars act identically on the $36$ tame channels. In R886's fixed Heisenberg identification the group acts as $1_{\mathcal U_L}\otimes\rho_h$, so (898.25) is a scalar primary-line equality tensored with the identity. Equivalently all maps commute with the full six-primary theta algebra, whose actual irreducible multiplicity module is $\mathcal U_L$. There is no separate unspecified scalar or matrix for each channel.

## 7. An actual integral source for the original period and the precise jet

Define initially on the generic fiber
$$
\mathcal Z_h=
\varpi^{-p(p-1)}
 \rho_h(\mathsf B^{-1})\mathcal A_h\Gamma_h:
\mathcal U_{L,K'}\longrightarrow\mathcal B_{K'}.
\tag{898.33}
$$
Equations (898.21)--(898.22) and the rank-one identity (898.25) give the exact equality
$$
\boxed{
\mathcal Z_h
=\varpi^{-p(p-1)}\Pi_{0,h}U_{t_*}\Gamma_h
=\beta_h(t_*)\mathcal J_h.
}
\tag{898.34}
$$
The right side is integral by (898.18) and (898.30). Thus (898.33) is an actual integral map into the direct summand $\mathcal V_h$, even though no integrality of its individual generic factors $\rho_h(\mathsf B^{-1})$, $\mathcal A_h$, or $U_{t_*}$ on the entire theta lattice has been asserted.

For the trace-normalized original tame basis of R897,
$$
\boxed{
\overline{\mathcal Z_h(u_m)}
=P_{h-1}(1/s)|p-h,h-1\rangle m.
}
\tag{898.35}
$$
In particular $\mathcal Z_h$ is an integral isomorphism onto $\mathcal V_h$ exactly when the original Legendre factor is a unit. This refers to a vector-valued map; it does not assert that a specified jet of its value is a unit.

Take the actual fixed quotient section $u_{G,F}$ of R897, associated with
$$
m_{G,F}=((-xy)^ps_{6p})\otimes(x^ps_{6p}).
$$
For the original indices
$$
p=6N+5,\qquad h=6i+7,\qquad j=N-1-i,
$$
and
$$
F=x\sigma^6=z^4f(z^6),\qquad
G=-xy\sigma^6=zg(z^6),
$$
R889's original local functional gives
$$
\boxed{
\overline{J_{3,2}\bigl(\mathcal Z_h(u_{G,F})\bigr)}
=
\frac{(6B)^5}{12}\,
P_{h-1}(1/s)(f_i g_j)^p.
}
\tag{898.36}
$$
The local frames and the ordinary Taylor coefficient are exactly those of R889/R897. Since $h-1$ is even, $P_{h-1}(1/s)\in\mathbf F_p$, so the right side is also
$$
\frac{(6B)^5}{12}
 \bigl(P_{h-1}(1/s)f_i g_j\bigr)^p.
$$
All scalar factors outside the original three factors are units.

Thus the original same-label primitive/Legendre/sigma condition is exactly the nonzero reduction of one specified jet of a transported original period source which has now been proved integral. The full torus average, determinant extension, and nontrivial shift are all part of that source. This is stronger than identifying only a diagonal matrix coefficient or an ambient weight space.

It still does not prove that the jet in (898.36) is nonzero. Even when the Legendre factor is a unit and $\mathcal Z_h(u_{G,F})$ has unit content, the particular functional $J_{3,2}$ can vanish on its reduction. The known individual-label counterexamples remain compatible with (898.36). Nor does this theorem identify this theta-section lattice with the unresolved original modular normal or height lattice.

Replacing $h$ by $h+n/2$ changes (898.14)--(898.15) by the norm-quadratic character, changes the full determinant extension and the split vector, and selects the corresponding different primary index. That change has nowhere been collapsed to equality of the restricted characters.

## Sources

- [R881](R881-original-integral-theta-lift-and-cuspidal-test-vector.md), §§4--7: actual single-factor phase, original symplectic marking, original full determinant extension, and split vectors.
- [R886](R886-original-two-flag-theta-descent-and-split-contraction.md), §§3--7: fixed tame multiplicity identification, actual $\Gamma_h$, and the original generic CM average.
- [R897](R897-original-quotient-theta-basis-and-same-label-Gauss-source.md): actual quotient basis, full controlled Gauss expansion, original precision and fifth jet.
- [R808](R808-original-cuspidal-Gram-quotient-and-Howe-chain.md), §§1--3, and its original R727 inputs: complete all-$g$ integral Gram quotient and the fixed covariant/Frobenius convention.
- [B. Liu and Q. Zhang, *Uniqueness of certain Fourier-Jacobi models over finite fields*](https://arxiv.org/pdf/1810.11901), §2.2, (2.1), and §2.3, (2.2): the canonical one-dimensional quadratic scaling factor and the original anisotropic norm realization. These displayed formulas were read directly.
- [S. Gurevich and R. Hadani, *Notes on the Self-Reducibility of the Weil Representation and Higher-Dimensional Quantum Chaos*](https://arxiv.org/pdf/0708.0755), §2.3, Theorem 6, and §2.5, Theorem 7: canonical finite Weil linearization and character normalization used in R881. Tensor compatibility follows from the uniqueness in Theorem 6; Theorem 7 is the character formula $\operatorname{ch}\rho(g)=\sigma((-1)^N\det(g-I))$ on its stated domain. The phase for the present full Cartan is calculated explicitly in §3 above.

This is a symbolic proof. It executes no new mathematical computation or prime scan.
