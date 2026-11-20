# The complete weight-ten double-Hecke zero packet, with both tame markings

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: paper proof; the accompanying small exact-series computation has not been run locally.** The low-weight space in this note is the four-dimensional pullback of the complete $H_6$ weight-ten cusp space. It is not the much larger space $S_{10}(\Gamma_0(36))$. The ordinary $T_5$ does not preserve this four-dimensional marked space: it exchanges it with its conjugate tame marking. We prove that exchange before extracting any coefficient. The resulting $T_5^2$ has a simple zero-primary part for every $p\ge41$.

The previously suggested single-space matrix with $T_5B_2=8W$ is false and is not used. The correct arrow is $T_5B_2=8\bar W$. The two arrows and the exact normalization below give the double-step scalar $147456$, not $-49152$.

## 1. The full space and its integral basis

Retain R913/R918/R920's original $\zeta^2$ oldform phase and $s^2=-3$, $\zeta=(-1+s)/2$. In the ordinary pullback variable $q$ of R920, put
$$
v=V_4^\dagger(6\tau),\qquad e_4=E_4(6\tau),
\quad e_6=E_6(6\tau),\qquad a=\eta(6\tau)^{12}.
$$
Define
$$
B_1=ve_6,\quad B_2=va,\quad W=e_4^2a/v,\quad Z=e_4a.
\tag{WH1}
$$
Let $\mathcal S$ be the pullback of $S_{10}(H_6)$ in this fixed marking. R920 proves that this full space has dimension four. All four displayed sections belong to it. Only regularity of $W$ needs discussion: the only zeros of $v$ are the original cusp and the three order-three points, and at the latter $e_4$ has fine order one. Thus division by $v$ gives no pole. At the cusp $a/v$ has order two. The same divisor argument works integrally at every prime greater than three, by R918's full integral divisor calculation.

Their initial terms are
$$
B_1=q+8sq^4+\cdots,\quad B_2=q^4+\cdots,
\quad W=q^2+\cdots,\quad Z=q^3+\cdots.
\tag{WH2}
$$
The coefficient matrix at $q,q^2,q^3,q^4$ has determinant one. Using the same fine-curve base change and unit averaging as R920, this is the full integral basis, not a sublattice with an uncomputed index.

Let $\overline{\mathcal S}$ denote coefficient conjugation $s\mapsto-s$, with $q$ fixed. Its corresponding basis is $\bar B_1,\bar B_2,\bar W,Z$. We distinguish these spaces throughout.

## 2. The determinant-five tame marking, before coefficient calculations

On the original full-six variable $\tau'$, let $G$ be the image of the geometric group in
$\operatorname{SL}_2(\mathbf F_2)\times\operatorname{SL}_2(\mathbf F_3)$:
$$
G=\{(\vartheta(g),g):g\in\operatorname{SL}_2(\mathbf F_3)\}.
\tag{WH3}
$$
The kernel of $\vartheta$ is the original $Q_8$, and its image on $\operatorname{SL}_2(\mathbf F_3)$ is the order-three subgroup $A_3\subset\operatorname{GL}_2(\mathbf F_2)$. In particular $G$ contains the image of $-I$.

Set $d=\operatorname{diag}(1,-1)$ modulo six. Its mod-two component is the identity, while its mod-three component has determinant minus one. The latter maps under $\vartheta$ to a transposition, which conjugates $A_3$ by inversion. Consequently
$$
dGd^{-1}=G',\qquad
G'=\{(\vartheta(g)^{-1},g):g\in\operatorname{SL}_2(\mathbf F_3)\}.
\tag{WH4}
$$
The equality uses conjugation on the second component followed by a change of variable $g$; inversion is taken only in the abelian group $A_3$. In particular it does define a subgroup. Complex conjugation of Fourier coefficients carries the original modular space to the space for $G'$, by the usual map $f(\tau')\mapsto\overline{f(-\bar\tau')}$. Thus this is precisely the conjugate marking above, not a new CM phase chosen for convenience.

Here is an explicit normalized Hecke formula which keeps that marking. For weight $k$ use the slash convention
$$
(f|_k M)(\tau')=\det(M)^{k/2}(c\tau'+d)^{-k}f(M\tau').
$$
Take the six matrices
$$
M_\infty=\begin{pmatrix}5&0\\0&1\end{pmatrix},
\qquad M_j=\begin{pmatrix}1&6j\\0&5\end{pmatrix},
\quad 0\le j<5,
$$
and define
$$
\mathcal T_5f=5^{k/2-1}\left(f|_kM_\infty+
\sum_{j=0}^4f|_kM_j\right).
\tag{WH5}
$$
All matrices reduce modulo six to $d$ or $-d$. For $\gamma$ in the inverse-image group of $G'$, the usual determinant-five coset permutation writes
$M_i\gamma=\kappa_iM_{j(i)}$ with $\kappa_i\in\operatorname{SL}_2(\mathbf Z)$. Reducing modulo six gives
$\kappa_i\in G$, because $dG'd^{-1}=G$ and $-I\in G$. This proves that (WH5) carries $G$-invariant cusp forms to $G'$-invariant cusp forms. Repeating it carries $G'$ back to $G$, since $d^2=I$ modulo six. This is a full-space stability proof, not an inference from exponent residue classes.

If $Q=e^{2\pi i\tau'/6}$ and $f=\sum a_nQ^n$, the five-term sum in (WH5) selects the indices divisible by five. Thus
$$
\mathcal T_5f=\sum_{m\ge1}(a_{5m}+5^{k-1}a_{m/5})Q^m.
\tag{WH6}
$$
After $\tau'=6\tau$, this is exactly the ordinary $\Gamma_0(36)$ formula used in R920. There is no extra factor of six: the fixed pullback slash factor is constant on both sides. We therefore denote (WH5–6) by $T_5$ below and have proved
$$
T_5:\mathcal S\longrightarrow\overline{\mathcal S},
\qquad T_5:\overline{\mathcal S}\longrightarrow\mathcal S.
\tag{WH7}
$$

The translation $Q\mapsto\zeta Q$ normalizes both tame groups. Formula (WH6) exchanges its two nontrivial characters and preserves its trivial character. With the bases (WH1–2), the target lines and planes are therefore
$$
T_5\langle B_1,B_2\rangle\subset\langle\bar W\rangle,
\quad T_5\langle W\rangle\subset\langle\bar B_1,\bar B_2\rangle,
\quad T_5\langle Z\rangle\subset\langle Z\rangle.
\tag{WH8}
$$
This character argument is used only after (WH7) has been established.

## 3. The new short coefficient identities

R920 already proves the two input rows
$$
[q^{10}]B_1=-4032s,\qquad [q^{10}]B_2=8.
\tag{WH9}
$$
We reuse them without treating their recomputation as a new conclusion. The new coefficients needed are
$$
[q^5]W=-8s,\qquad [q^{20}]W=6144,
\qquad [q^{15}]Z=-666.
\tag{WH10}
$$
For a complete paper derivation, put $x=q^3$. The original CM norm coefficients at $1,4,7,10,13,16,19$ are respectively
$1,-8,20,0,-70,64,56$. They also follow from the finite product $q\prod(1-q^{3n})^8$. Incorporating the original oldform term gives
$$
v/q=1+8sx+20x^2-70x^4-64sx^5+56x^6+O(x^7).
\tag{WH11}
$$
Writing $y=x^2$,
$$
e_4=1+240y+2160y^2+6720y^3+O(y^4),
$$
$$
a/q^3=1-12y+54y^2-88y^3+O(y^4).
$$
Their product gives
$$
e_4^2(a/q^3)=1+468x^2+56214x^4+333032x^6+O(x^8).
$$
Dividing by (WH11), whose constant term is one, yields
$$
W/q^2=1-8sx+256x^2-1888sx^3+5852x^4
-9552sx^5+6144x^6+O(x^7).
\tag{WH12}
$$
The last coefficient can be checked without a large product: its preceding convolution is
$229248+117040-17920-1536+56=326888$, and
$333032-326888=6144$. Also
$$
[q^{15}]Z=54-2880+2160=-666.
$$
As an independent phase check,
$$
[q^{25}]B_2=64s.
\tag{WH13}
$$
Indeed the coefficient of $x^7$ in $(v/q)(a/q^3)$ is
$0+(-64s)(-12)+0\cdot54+(8s)(-88)=64s$; the omitted $x^7$ coefficient of $v/q$ is zero because the norm index is $22$. In particular $[q^5]T_5B_2=64s$, which rules out the false formula $T_5B_2=8W$.

## 4. The two correct arrows and their square

Membership (WH8), the unit initial coefficients, and (WH9–10) give the complete modular identities
$$
\begin{aligned}
T_5B_1&=-4032s\bar W,&T_5B_2&=8\bar W,\\
T_5W&=-8s\bar B_1+6336\bar B_2,&T_5Z&=-666Z.
\end{aligned}
\tag{WH14}
$$
For the coefficient $6336$, use $[q^4]\bar B_1=-8s$:
$$
6336=6144-(-8s)(-8s)=6144+192.
$$
The rational formula (WH6) commutes with coefficient conjugation. Hence
$$
T_5\bar W=8sB_1+6336B_2,
\quad T_5\bar B_1=4032sW,\quad T_5\bar B_2=8W.
\tag{WH15}
$$
Set $U=T_5^2|_{\mathcal S}$. On $\langle B_1,B_2\rangle$ it is the rank-one operator with column and row
$$
\binom{8s}{6336}\begin{pmatrix}-4032s&8\end{pmatrix}.
\tag{WH16}
$$
Their scalar product is
$$
\rho=(-4032s)(8s)+8\cdot6336=147456=2^{14}3^2.
\tag{WH17}
$$
Moreover
$$
UW=\rho W,\qquad UZ=666^2 Z.
\tag{WH18}
$$
For every $p\ge41$, both $\rho$ and $666=2\cdot3^2\cdot37$ are units. The full generalized zero eigenspace is therefore
$$
\boxed{\quad
\bigcup_{n\ge1}\ker(U^n)
=\ker U=k(B_1+504sB_2)=kV_{10}^\dagger.
\quad}
\tag{WH19}
$$
For instance, the polynomial
$(1-U/\rho)(1-U/666^2)$ is the projector onto this line. This remains true if the two nonzero eigenvalues coincide modulo $p$; no separation of those two nonzero packets is needed.

## 5. Returning to the actual original Hecke source

The single-step calculation has deliberately kept both pairing markings. After two degree-five steps the tame determinant is $25\equiv1\pmod6$, so the transported pairing component returns to the original one. In the Hecke composition the scalar-five level correspondence acts at level six by $5I=-I$, which belongs to the original $H_6$ and acts trivially in the even weight ten. Thus the usual double-step Hecke relation and (WH16–18) are on the original tame quotient. This follows from the explicit coset marking above, not from identifying a conjugate CM form with the original form.

R913 (913.40) supplies the remaining original Igusa/norm conversion on the full $\chi_+$ source:
$$
T_5^{\rm orig}=5^{p-h}T_5^{\rm Gross}.
$$
It holds on the full deck-character sum, with the actual nonsquare-norm interchange of parts retained. Consequently the square differs by the unit $5^{2(p-h)}$. The fixed exotic/Frobenius determinant correction conjugates the complete diagram; the full character extension determines the other Igusa part uniquely. Neither operation changes the dimension of the zero-primary part or replaces its transported $V_{10}^\dagger$ line. Thus (WH19) gives the original low-weight generalized Hecke-zero line after those exact transports.

## 6. What this does and does not settle

This is stronger than R920's single $T_5$-kernel row: it rules out a longer generalized zero packet in the complete weight-ten tame space. Its proof preserves the conjugate intermediate marking that the false single-space matrix omitted.

It does not prove that the high-weight companion packet maps entirely into the Hasse multiple of this low-weight line under $\Theta^r$. R932 proves that divisibility for the one named companion. Extending it to all generalized CM eigenvectors is a separate saturation statement. Without that statement, (WH19) does not prove that the R936 supersingular trace is nonzero for every prime, and does not determine $Q'_h(0)$.

## Sources and computation contract

- R913, §§2–3 and 7: original graph, full norm characters, the Hecke normalization and transpose, and the interchange of the two deck characters.
- R918, §§2–3: full tame subgroup and the complete divisor of $V_4^\dagger$.
- R920, §§2–4: complete dimension four, original two-dimensional character basis, unit integral basis argument, the already proved rows (WH9), and the fixed six-level pullback.
- The new group-theoretic determinant-five calculation and short coefficient derivations are fully given above.

The accompanying script is to be executed only in this repository's public GitHub Actions. Its task is the new coefficients (WH10), the conjugate coefficients, the diagnostic (WH13), and the resulting double-step identities, reusing (WH9). It does not rerun the supersingular trace or scan primes.
