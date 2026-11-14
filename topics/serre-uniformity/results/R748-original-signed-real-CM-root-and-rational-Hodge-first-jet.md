# R748 — The original signed real CM root and six rational Hodge first jets at p = 41

Date: 2026-11-14. **Status: proved, with a completed exact public
computation.** The original sign, all six rational first coefficients,
and the complete local consequence below are certified. The old finite
torus fibers and the R717 integer traces were reused.

## 1. Statement in the actual normalization

Put

$$
p=41,\qquad n=42,\qquad \eta=e^{2\pi i/42},\qquad
\zeta=\eta^{14},\qquad
\beta=\eta+\eta^{-1},\qquad F_0=\mathbf Q(\beta).
\tag{748.1}
$$

The original finite label is $\eta\bmod41=(7,30)$ in the basis
$(1,\zeta)$, and $\zeta$ has positive imaginary part.
Let $\alpha=\sqrt[3]4>0$, $s_0=1+2\zeta=\sqrt{-3}$, and retain
the original raw form $F^\circ$ and the average
$u=A_{\mathsf T_\zeta}e_0$ of R588/R745. In particular, no raw
Cartan trace is substituted for this average.

R747 defines the original signed real element

$$
T=\frac{42\alpha M_2}{144(1-\zeta^2)}
  =\frac{42}{432}\,\widehat M_2,
\qquad \widehat M_2=\alpha s_0\zeta^2M_2,
\qquad T^2=2NP.
\tag{748.2}
$$

Here $M_2$ is the unchanged R588 raw flat jet,
$N=42G(u,u)$, and $P=S_2S_3/C_0^2$.
The factor $\zeta^2$ is the single actual $g_*$ transport at
$c_1$; it is not applied a second time to $M_2$.

**Theorem 748.1.** In the specified real embedding,

$$
\boxed{
T=
\frac{
10177+16725\beta-16710\beta^2-8550\beta^3+
4754\beta^4+1425\beta^5
}{5043}.
}
\tag{748.3}
$$

The minimal polynomial of the specified generator is

$$
f_\beta(X)=X^6+X^5-6X^4-6X^3+8X^2+8X+1.
\tag{748.4}
$$

The value in (748.3), with the displayed sign, is the original
CM value. For the six positive primitive labels

$$
(h_1,\ldots,h_6)=(1,13,19,25,31,37),
\tag{748.5}
$$

the original signed conjugates have signs

$$
(+,-,+,-,+,+).
\tag{748.6}
$$

These are the conjugates of one element of $F_0$, rather than
six independently chosen square roots.

Use the actual rational Hodge basis of R745,

$$
\omega_j=2\pi i\,\alpha s_0
 \operatorname{Tr}_{F_0/\mathbf Q}
     \bigl(\beta^jF^\circ\bigr)\,d\tau,
\qquad 0\le j\le5.
\tag{748.7}
$$

At the original marked point $c_1$, write $s=a-1$ and

$$
I_j(s)=\int_{c_1}^{x(s)}\omega_j,\qquad I_j(0)=0.
\tag{748.8}
$$

Then the six exact original first coefficients are

$$
\boxed{
\begin{aligned}
[s]I_0&=\frac{43719}{11767},&
[s]I_1&=\frac{200187}{23534},&
[s]I_2&=\frac{162558}{11767},\\
[s]I_3&=\frac{687471}{23534},&
[s]I_4&=\frac{659397}{11767},&
[s]I_5&=\frac{2521233}{23534}.
\end{aligned}}
\tag{748.9}
$$

**Corollary 748.2.** For the particular actual rational Hodge
component $\omega_0$, the complete primitive $I_0$ has only
the central zero on the open disc

$$
v_{41}(a-1)>3.
\tag{748.10}
$$

On the entire closed candidate disc $s=41^4t$, the normalized
complete function is

$$
\boxed{
\frac{I_0(41^4t)}
     {41^4(43719/11767)}
=t+41H(t),\qquad H\in t^2\mathbf Z_{41}\langle t\rangle.
}
\tag{748.11}
$$

It is an isometry and a bijection of $\mathbf Z_{41}$, with
inverse given by a restricted integral series. This concerns
the specified Hodge component and its Abel integral. It is
not an actual height equation or a rational-point exclusion
for the positive-rank quotient.

## 2. Retained inputs and actual public run

The computation was performed once in the public repository:

- [Run 43617493590](https://github.com/Rogerhu12/math-research-public/actions/runs/43617493590),
  attempt 1, source commit
  b401479892e81ed76c587da52305606100ed88a7.
- Core runtime: $0.396870754$ seconds. The core receipt and
  run receipt both record complete success and no repeated
  old finite fiber, approximate functional equation, or DFT.
- Python-FLINT 0.9.0, 512-bit working precision, original
  Fourier cutoff $4096$, and $E_6$ cutoff $80$.
- Full artifact:
  serre-cartier-R748-original-signed-CM-root-p41-43617493590-1.
- Bounded certificates are in
  [the original public output directory](../computations/R748-original-signed-CM-root-p41/43617493590-1/).

Two completed inputs were used. R745 run 43616027318
provided the original twelve-coefficient norm $N$, all forty
nonzero-gauge coordinates of $u$, and $a_0,\ldots,a_{800}$.
The exact Hodge input gzip has SHA-256
a629d550bd2f3102111bbb58fe707470081e2062da10221ab778fe3ba71b53dd.
Its completed certificate has SHA-256
7fdac934ab8be401afbe793c9dd6d790bba2dc1f39cdbb134fc51748870816be.

R717 run 43597163388 supplied the already certified integer
trace polynomial $\mathcal P$ satisfying

$$
\mathcal P(\eta)=42DP,\qquad
D=2^{37}3^{26}41^5
 =40474523621172381677418486693888.
\tag{748.12}
$$

The integer polynomial gzip SHA-256 is
932899efb77482cb7712e8554376b6c6f65050620bf9a84485d610949ba0dbc7,
and its completed norm receipt SHA-256 is
fb4d9ffadacda241575ab92a49f66819d8ac077ececa8f5151adf4aea3751fa6.
The character generator, its $\zeta$ direction, and the exact
denominator $D$ were checked against those receipts.

Only new Fourier coefficients with index greater than $800$
were formed. The completed extension through $4096$ is a
9,909-byte gzip retained in the full artifact, with SHA-256
0c7d73a2a2c9202c6a25f343c9357a8b59d9cfc4928a29b5d460dbf84828bff0.
The core used $637$ nonzero Fourier terms. The complete
checkpoint remains available in the same artifact.

## 3. Exact real-field identity and integral reconstruction

All field calculations here are rational polynomial
calculations. Inside $A=\mathbf Q(\eta)$, one has

$$
\Phi_{42}(X)=
X^{12}+X^{11}-X^9-X^8+X^6-X^4-X^3+X+1.
\tag{748.13}
$$

The original R745 norm is

$$
\begin{aligned}
N={}&4-12\eta+4\eta^2+28\eta^3+16\eta^4-20\eta^5\\
   &-24\eta^6+12\eta^7+36\eta^8+8\eta^9
      -24\eta^{10}-16\eta^{11}.
\end{aligned}
\tag{748.14}
$$

The retained R717 polynomial and (748.12), followed by the
exact change to the real basis $1,\beta,\ldots,\beta^5$, give

$$
2NP=
\frac{
48903672-50398615\beta-124453534\beta^2
-35500533\beta^3+53498759\beta^4+24966893\beta^5
}{25431849}.
\tag{748.15}
$$

The denominator in (748.15) is $5043^2$. If $U(X)$ denotes
the numerator in (748.3), the accepted candidate satisfies the
exact identity

$$
\begin{aligned}
U(X)^2\equiv{}&
48903672-50398615X-124453534X^2\\
&-35500533X^3+53498759X^4+24966893X^5
\pmod{f_\beta(X)}.
\end{aligned}
\tag{748.16}
$$

The public core checked (748.16) in rational polynomial
arithmetic; its truth does not depend on a floating point
fit. The real field, the retained $P$, and both sides of
(748.16) are recorded in
[R748-exact-real-field.json](../computations/R748-original-signed-CM-root-p41/43617493590-1/R748-exact-real-field.json).

For completeness, the reconstruction did not assume an
unproved integral basis. R747 gives

$$
D_TT\in\mathcal O_{F_0},\qquad
D_T=2^{18}3^{13}41^2=702560852508672.
\tag{748.17}
$$

The exact power traces through order ten are

$$
(6,-1,13,-1,41,-1,139,6,489,62,1763).
\tag{748.18}
$$

Therefore the trace Gram matrix
$G_{ij}=\operatorname{Tr}(\beta^{i+j})$, $0\le i,j\le5$,
has determinant

$$
\Delta=453789.
\tag{748.19}
$$

If $D_TT=\sum z_i\beta^i$, its integral trace pairings with
$\beta^j$ give $G(z_i)\in\mathbf Z^6$. The adjugate identity
implies

$$
W=\Delta D_TT\in\mathbf Z[\beta].
\tag{748.20}
$$

This argument is valid even without identifying
$\mathcal O_{F_0}$ with $\mathbf Z[\beta]$.

The public calculation formed the six positive square roots
of the six real embeddings of $2NP$ and interpolated signed
values using exact-label Lagrange basis balls. The clearing
scale and accepted integer vector were

$$
\Delta D_T=318814386699057758208
\tag{748.21}
$$

and

$$
\begin{aligned}
(W_0,\ldots,W_5)=(&643381719896155226112,\\
 &1057340990985869721600,\\
 &-1056392703101577461760,\\
 &-540524094046588108800,\\
 &300544040128360218624,\\
 &90087349007764684800).
\end{aligned}
\tag{748.22}
$$

All six coefficient balls contained unique integers. Their
largest radius was

$$
981244225\cdot2^{-463}<2^{-433}.
\tag{748.23}
$$

Exact reduction of $W^2-(\Delta D_T)^2(2NP)$ gave zero.
The first twenty sign patterns failed the required integer
test; the successful pattern was $(+,-,+,-,+,+)$ with the
first embedding positive. These failed patterns need not be
interpreted as separate arithmetic information: after one
nonzero root is verified exactly, a field has just the two
roots $T_+$ and $-T_+$.

The full interpolation balls and the exact identity are in
[R748-exact-positive-root.json](../computations/R748-original-signed-CM-root-p41/43617493590-1/R748-exact-positive-root.json).
The original sign still needs the separate argument next.

## 4. Absolute Fourier expression and its complete tails

The original finite vector has the R745 gauge

$$
u=\frac1{1722}\sum_{r=1}^{40}c_r(\eta)e_r,\qquad c_0=0,
\qquad1722=41\cdot42.
\tag{748.24}
$$

Write $\xi=e^{2\pi i/41}$ and $v=6^{-1}\bmod41$. The
actual integral CRT shift is $k_r=6(rv\bmod41)$, so
$k_r\equiv0\bmod6$ and $k_r\equiv r\bmod41$. For

$$
Q=e^{2\pi i\tau/246},\qquad
B_\nu=\frac1{1722}\sum_{r=1}^{40}
 c_r(\eta)\xi^{-\nu rv},
\tag{748.25}
$$

the unchanged raw form is

$$
\begin{aligned}
F^\circ
 &=A_{\mathsf T_\zeta}
   \bigl(f_\theta(\tau/246)
         -4\zeta^2f_\theta(4\tau/246)\bigr)\\
 &=\sum_{\nu\ge1}a_\nu B_\nu t_\nu Q^\nu,
\end{aligned}
\tag{748.26}
$$

where $t_\nu=1$ for odd $\nu$, $t_\nu=-s_0$ for $4\mid\nu$,
and the other terms vanish. Indeed $a_{4m}=-2a_m$, so the
coefficient at $4m$ is multiplied by
$1+2\zeta^2=-s_0$. No additional factor of $246$ is
inserted in the raw weight-two function.

The new coefficients were formed by the same original
primary-generator formula as R745,

$$
a_\nu=
\sum_{\substack{a^2-ab+b^2=\nu\\
a\equiv1,\ b\equiv0\ (3)}}
 (a+b\zeta)\,
 \eta^{-\log_{(7,30)}(\overline y/y)},
\quad y=(a+b\zeta)\bmod41,\quad 41\nmid\nu.
\tag{748.27}
$$

For $41\mid\nu$ the coefficient is zero. The retained first
$801$ arrays were copied and checked unchanged. No finite
torus average was regenerated.

The absolute tail estimate is elementary. In the gauge
$c_0=0$, the finite form has matrix $41I-J$, whose minimum
eigenvalue is one. The original average is an orthogonal
projection of $e_0$, whose norm is $40$. Thus

$$
\sum_{r=1}^{40}|c_r/1722|^2\le40,\qquad
\sum_{r=1}^{40}|c_r/1722|\le40.
\tag{748.28}
$$

The normalized CM coefficient has
$|a_\nu|\le d(\nu)\sqrt\nu\le2\nu$: each ideal summand has
absolute value $\sqrt\nu$, and there are at most $d(\nu)$
summands. Hence

$$
|a_\nu B_\nu t_\nu|\le80\sqrt3\,\nu.
\tag{748.29}
$$

At the original positive CM embedding,

$$
Q=e^{-\pi i/246}r,\qquad
r=e^{-\pi\sqrt3/246}.
\tag{748.30}
$$

For $D=q\,d/dq$, the $k$th derivative multiplier is
$(\nu/246)^k$. The complete tail beyond $B$ therefore has
the rigorous bound

$$
\left|\operatorname{tail}_B D^kF^\circ(\zeta)\right|
\le \frac{80\sqrt3}{246^k}
       \sum_{\nu>B}\nu^{k+1}r^\nu,
\qquad k=0,1,2.
\tag{748.31}
$$

No cancellation is used in (748.31). With $b=B+1$, each
positive tail is evaluated by the exact identity

$$
\sum_{\nu>B}\nu^k r^\nu
=r^b\sum_{j=0}^k\binom kj b^{k-j}
 \sum_{\ell=0}^j
 \left\{\begin{matrix}j\\\ell\end{matrix}\right\}
 \frac{\ell!\,r^\ell}{(1-r)^{\ell+1}},
\tag{748.32}
$$

obtained by expanding $(b+m)^k$ and then $m^j$ in falling
factorials. This includes the $j=\ell=0$ term.

The rational level-one form is evaluated as

$$
E_6(\zeta)=1-504\sum_{\nu\ge1}\sigma_5(\nu)q^\nu,
\qquad q=-e^{-\pi\sqrt3}.
\tag{748.33}
$$

The bound $\sigma_5(\nu)<2\nu^5$ gives the full error

$$
1008\sum_{\nu>B_6}\nu^5|q|^\nu.
\tag{748.34}
$$

All analytic error bounds and all floating point rounding
radii were included in the final balls. Root of unity
phases were computed independently from exact rational
arguments; there was no long rectangular-ball rotation
recurrence. The completed certificate contains the separate
partial and full balls for $F^\circ$, $DF^\circ$ and
$D^2F^\circ$, as well as the partial and full $E_6$ balls.

## 5. The original sign from the CM derivative

The actual R592 deck selection gives the exact identities

$$
F^\circ(\zeta)=DF^\circ(\zeta)=0.
\tag{748.35}
$$

Consequently

$$
\delta_4\delta_2F^\circ(\zeta)
=\partial_4\partial_2F^\circ(\zeta)
=D^2F^\circ(\zeta).
\tag{748.36}
$$

The full zeroth- and first-derivative balls separately
contained zero, as required by this exact transformation
law. The proof of the vanishing is (748.35), not its
numerical enclosure.

R742 supplies the exact absolute period identity

$$
M_2=-864\,\frac{D^2F^\circ(\zeta)}{E_6(\zeta)}.
\tag{748.37}
$$

Inserting it into the fixed definition (748.2) gives

$$
T_{\rm CM}
=-\frac{252\alpha}{1-\zeta^2}
  \frac{D^2F^\circ(\zeta)}{E_6(\zeta)}.
\tag{748.38}
$$

The computed $E_6$ interval excluded zero. In
[R748-original-CM-sign-balls.json](../computations/R748-original-signed-CM-root-p41/43617493590-1/R748-original-CM-sign-balls.json),
the final exact dyadic enclosure of (748.38) is

$$
\begin{aligned}
\operatorname{Re}T_{\rm CM}
&\in
2^{-119}\,[A-237737681,A+237737681],\\
\operatorname{Im}T_{\rm CM}
&\in
2^{-121}\,[-950936211,950936211],
\end{aligned}
\tag{748.39}
$$

where

$$
A=3636921846028588064099403856809080571.
\tag{748.40}
$$

In particular the real interval is strictly positive.
Its rounded display is

$$
T_{\rm CM}\in
[\,5.472231788017626379870965347
   \ \mathbin{\pm}\ 4.46\cdot10^{-28}\,]
\quad\text{on the real line}.
\tag{748.41}
$$

The exact first embedding of the polynomial in (748.3)
overlapped the real interval in (748.39). The negative root
was disjoint. The source also rechecked the exact square
identity after the original sign was selected.

By R747, the actual value belongs to $F_0$ and satisfies
the exact square identity (748.2). Thus the strict positive
sign identifies it with the candidate in (748.3). The six
original signs in (748.6) now follow from the coherent
coefficient conjugation of R747, completing the proof of
Theorem 748.1's first assertion.

## 6. Derivation of the six actual rational first coefficients

The exact traces from (748.3) are

| $j$ | $\operatorname{Tr}_{F_0/\mathbf Q}(\beta^jT)$ | $[s]I_j$ |
|---:|---:|---:|
| $0$ | $29146/5043$ | $43719/11767$ |
| $1$ | $22243/1681$ | $200187/23534$ |
| $2$ | $36124/1681$ | $162558/11767$ |
| $3$ | $229157/5043$ | $687471/23534$ |
| $4$ | $439598/5043$ | $659397/11767$ |
| $5$ | $280137/1681$ | $2521233/23534$ |

Here is the complete differential comparison. At the actual
$c_1$, its single $g_*$ transport multiplies the raw local
form by $\zeta^2$. Equation (748.2) gives

$$
\widehat M_{2,j}
=\frac{432}{42}
  \operatorname{Tr}_{F_0/\mathbf Q}(\beta^jT).
\tag{748.42}
$$

The actual flat Hodge primitive starts with
$\widehat M_{2,j}z_{\rm flat}^3/6$. R592's exact coarse
change is

$$
z_{\rm flat}^3=\frac38s+O(s^2).
\tag{748.43}
$$

Therefore

$$
[s]I_j=
\frac{\widehat M_{2,j}}{16}
=\frac9{14}
 \operatorname{Tr}_{F_0/\mathbf Q}(\beta^jT),
\tag{748.44}
$$

which gives the last column and (748.9).

Equivalently the canonical flat second jets are

$$
\frac1{11767}
(699504,\ 1601496,\ 2600928,\ 5499768,\
10550352,\ 20169864).
\tag{748.45}
$$

These are in the explicitly defined R745 rational Hodge
basis. The comparison does not replace that basis by a
Néron basis, nor absorb a quotient-map scalar.

## 7. Complete local consequence for the actual rational component

We prove Corollary 748.2 using the full tail, without
declaring the first computed coefficient to be the entire
function. Since $11767=7\cdot41^2$ and
$43719\equiv13\bmod41$, (748.9) gives

$$
v_{41}([s]I_0)=-2,\qquad
v_{41}(\widehat M_{2,0})=-2.
\tag{748.46}
$$

For each allowed index $m=3j-1$, let
$\widehat M_{m,0}$ denote the canonical flat derivative of
the same rational Hodge form $\omega_0$ at $c_1$.
It is the trace sum of the six original derivatives,
with the same factor $\alpha s_0\zeta^2$, which is a
$41$-adic unit. R730's complete one-$p$ Hodge bound
therefore remains valid term by term and after this sum:

$$
v_{41}\!\left(\frac{\widehat M_{m,0}}{m!}\right)
\ge -1-\frac{41m}{42}.
\tag{748.47}
$$

The integer valuation and rationality follow either
from R742 and the actual rational Hodge basis, or from
R750's global real descent with the same single tame
normalization. Put

$$
E_j=\frac{41^{3j}\widehat M_{3j-1,0}}{(3j)!}.
\tag{748.48}
$$

The full-tail argument of R730 now gives

$$
v_{41}(E_j)
\ge\frac{3j-1}{42}-v_{41}(3j)>0,
\qquad v_{41}(E_j)\longrightarrow+\infty.
\tag{748.49}
$$

The displayed strict inequality is the same elementary
one used there: if $41\nmid3j$ it is immediate; if
$v_{41}(3j)=a\ge1$, then $3j\ge3\cdot41^a$, which makes
$(3j-1)/42-a$ positive. Since $E_j\in\mathbf Q_{41}$,
it follows that $E_j\in41\mathbf Z_{41}$ for every $j$.
Moreover

$$
v_{41}(E_1)
=v_{41}(41^3\widehat M_{2,0}/6)=1.
\tag{748.50}
$$

Use the same complete coarse change of variables from
R710/R744,

$$
V=\frac{z_{\rm flat}^3}{41^3}
  =\Psi(s/41^3),\qquad
\Psi(v)=\frac38v+41v^2
                  \mathbf Z_{41}\langle v\rangle.
\tag{748.51}
$$

The full primitive is exactly the convergent series

$$
I_0(s)=\sum_{j\ge1}E_jV^j.
\tag{748.52}
$$

For $v_{41}(s)>3$, the coordinate $V$ has positive
valuation, and (748.49)–(748.50) give

$$
I_0(s)=E_1V
 \left(1+\sum_{j\ge2}(E_j/E_1)V^{j-1}\right),
\tag{748.53}
$$

where the parenthesized factor is a unit. This proves
(748.10) over $\mathbf C_{41}$, counting the central
zero with its actual multiplicity one in the coarse
parameter.

For the closed disc put $s=41^4t$ and

$$
U(t)=\frac{\Psi(41t)}{41}
    =\frac38t+41^2t^2\mathbf Z_{41}\langle t\rangle.
\tag{748.54}
$$

The linear term in (748.52) is
$E_1\cdot41\cdot(3/8)t
 =41^4([s]I_0)t$. For $j\ge2$, (748.49) gives

$$
v_{41}\left(
 \frac{41^jE_j}{41^4([s]I_0)}
       \right)
\ge j-1\ge1.
\tag{748.55}
$$

These coefficients tend to zero, and $U(t)^j$ is an
integral restricted series. Equations (748.54)–(748.55)
prove the complete identity (748.11).
For $x,y\in\mathbf Z_{41}$, the difference
$H(x)-H(y)$ is divisible by $x-y$ in $\mathbf Z_{41}$,
so the normalized function preserves the $41$-adic
distance. The equation $t+41H(t)=b$ is solved uniquely
by the contraction $t=b-41H(t)$. This proves the asserted
bijection and its restricted inverse.

This uses the actual rational Hodge form throughout.
It does not assert that a noncentral rational point in
the original positive-rank problem must satisfy
$I_0=0$ or a height-zero equation.

## 8. Evidence and reproducibility

The complete source, request, workflow, fixed inputs and
theory dependencies are recorded in
[R748-source-manifest.json](../computations/R748-original-signed-CM-root-p41/43617493590-1/R748-source-manifest.json).
The core source SHA-256 is
6b34e4946907cb657cb68ce585e43b8ef31295be36e3f700966daa0d4f133d7c.
The parameter SHA-256 is
828df79c965ee5627949fbf0242a68cf1104abba51a50602b7ca68560955a57f.

The principal completed certificates have the following
SHA-256 values.

| Certificate | SHA-256 |
|---|---|
| Exact real-field identities | ee588074d44e151a9dea2d9b602c5fcf26bdd2ee86edad9a155caaac963ac443 |
| Exact positive-root reconstruction | b015e4acc946a637a24fdf8272d08185675ace63cd67abd9e9defa764f20b2ef |
| Original CM sign and complete tails | 227cf38171b8b57679444acc7fc8e8c060ad7257e7cd049d3bb848791e78effa |
| Final signed root and six exact jets | 56418d0cef84554584d8777aed4acb54a2dc57bbf95cc38a1bb42b12140769f3 |
| Core receipt | da20992562cd9b15c8c22f88de35c0b77d639cbddd730e0e60646d4d1305edca |
| Public run receipt | 48f480d4980eb39d5066cd6f7e36939a7f8eed12b6adfde73d47dd33eea9ff6f |
| Published files manifest | 65a1a1c2582c410716d4735542bf16f1d779fb1a5e91a068ced569893db73835 |
| Full-output manifest | d21f97fc8b88ed27f5dc87cd1821692f7540b528cdfc88dfda4969013b301956 |

The twelve published bounded files and all fourteen members
of the source archive were read and checked against their
published sizes and hashes. This was file verification of
the completed public run, without rerunning its mathematics.
The complete new coefficient array and its checkpoint are
kept in the Actions artifact with their original hashes.

The analytic and exact-field algorithm is also described in
[the original method note](../notes/R748-original-signed-real-CM-root-and-p41-Hodge-first-jet-method.md).
Its full error estimates and all arithmetic identities were
applied in the successful public run above.

## Dependencies and scope

- [R588](R588-actual-toric-norm-and-CM-normalization.md):
  unchanged original average, period, and norm.
- [R592](R592-actual-integral-CM-jet-lattice-and-complete-tail.md):
  raw tame vector, flat derivative, and coarse factor $3/8$.
- [R717](R717-exact-original-CM-norm-from-certified-complex-traces.md):
  retained exact original integer traces.
- R745: the actual rational Hodge basis and original Fourier
  coordinates, including the factor $246$ for differentials.
- [R747](R747-global-real-square-root-of-original-toric-period-product.md):
  the signed real root, its integral denominator, and coherent
  coefficient conjugates.
- [R742](R742-unramified-original-first-jets-and-depth-seven-Abel-isometry.md)
  and R730/R710/R744/R750: all-order integrality, full tails,
  rational jet line, and complete change of parameter.

This result computes an original signed first Hodge jet and
proves its complete local Abel consequence at $41$. It does
not compute the original quotient map, the point
$q[c_1-c_0]$, or the required global height expressions.

