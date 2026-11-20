# R943 — Fixed Cartier interfaces for the original p=11 mod12 central and third-position factors

Date: 2026-11-20. Status: **proved fixed-curve identities; the original same-label sigma condition remains open**. The new conclusions are the correctly signed central second-kind comparison and the explicit Hasse, Gauss–Manin and second-kind Cartier certificates on one fixed three-torsion curve. The admissible third-position label pair and its Legendre non-common-zero theorem were already proved in the [2026-11-16 swapped-label result](../notes/2026-11-16-sigma-two-swapped-primitive-labels-at-thirds.md), commit `543d03f8`; those conclusions are reused, not registered anew. The finite window in Appendix A is separate evidence and is not a uniform theorem.

## 1. Original objects and the previously established actual label pair

Let
$$
p\ge41,\qquad p\equiv11\pmod{12},\qquad
p\equiv2,5\pmod9,
\qquad s^2=-3,\quad x=1/s.
\tag{943.1}
$$
The smallest prime in this range is $47$. Retain the original $s$, determinant extension, full norm character, split vector, two-oldform phase and Tate indices. In particular $x^2=-1/3$ and $x^p=-x$.

Put
$$
m=\frac{p-1}{2},\qquad h_0=\frac{p+3}{2},\qquad
n_3=\frac{p-2}{3},\qquad q=n_3+1=\frac{p+1}{3}.
\tag{943.2}
$$
Both $m$ and $n_3$ are odd. The central label is the original weight-four label of R918/R925. Its reflected factor is
$$
L=P_{h_0-1}(x)=P_{m+1}(x)=P_{m-1}(x)\in\mathbf F_p.
\tag{943.3}
$$

The old swapped-label result proves that the following are two distinct original primitive labels in $7\le h\le p-4$, each congruent to $1$ modulo $6$, and that their displayed original Legendre factors do not both vanish:

| Original prime class | Actual labels in the old ordering | Original factors after the original reflection | Actual ordered sigma products |
|---|---|---|---|
| $p=18k+5$ | $q-1=6k+1$, $2q+3=12k+7$ | $P_{n_3-1}(x)$, $P_{n_3-3}(x)$ | $f_{k-1}g_{2k}$, $f_{2k}g_{k-1}$ |
| $p=18k+11$ | $q+3=6k+7$, $2q-1=12k+7$ | $P_{n_3+3}(x)$, $P_{n_3+1}(x)$ | $f_kg_{2k}$, $f_{2k}g_k$ |

The first row is $p\equiv5\pmod9$ and the second is $p\equiv2\pmod9$. Their full-modulus primitivity and their Legendre non-common-zero statement are exactly the already proved (TS7)–(TS9) of that source. No new primality or gcd window is needed here. These actual pairs already settle the Legendre-only choice for $p\equiv11\pmod{12}$; a separate central-versus-third Legendre common-zero theorem is not needed for that choice.

For every label in this table, the unchanged R898 source is
$$
\mathscr J_h
=\overline{J_{3,2}(\mathcal Z_h(u_{G,F}))}
=\frac{(6B)^5}{12}P_{h-1}(x)
\bigl(\overline{f_i g_j}\bigr)^p,
\tag{943.4}
$$
with its actual ordered $(i,j)$ as displayed, and the original $\Gamma_h$, $\mathcal Z_h$, $u_{G,F}$ and Cartier unit $B$. For the central label, writing $p=12t+11$ gives the actual product $f_tg_t$. Reflection is applied only to the Legendre polynomial, never to the sigma factors. The third-position weights grow with $p$; the bounded-weight normal results R925/R940 are not automatically available for them.

## 2. The central Cartier coefficient, with the odd-m sign retained

Use the fixed rational curve and differential of R929/R933:
$$
E_*:\ v^2=f_*(w)=w^3+6w+7,
\qquad \omega_* =\frac{dw}{2v}.
$$
Define
$$
U=[w^{p-1}]f_*(w)^m,\qquad
V=[w^{p-2}]f_*(w)^m,
\qquad A=P_m(x).
\tag{943.5}
$$
Let $d=3s$. The translation and twist from R929/R933 preserve their two different coefficient scales $d^m$ and $d^{m+1}$. Here $m$ is odd, so the original Legendre Hasse polynomial is $-P_m$, and the resulting formulas are
$$
\boxed{
U=-d^m A,\qquad
V=\frac{d^{m+1}}3(xA-4A').
}
\tag{943.6}
$$
For clarity, R933's polynomial identity
$$
B(\lambda)=\lambda H(\lambda)-2\lambda(1-\lambda)H'(\lambda)
$$
holds for either parity of $m$. At $\lambda=(1-x)/2$, the present signs are $H=-A$ and $H'=2A'$. Translating by $(1+\lambda)/3$ therefore gives the coefficient $(xA-4A')/3$ at degree $p-2$. This explains both signs in (943.6) without applying R933's even-$m$ specialization to the present class.

Set
$$
\epsilon=d^{m+1}=(-27)^{(p+1)/4}\in\mathbf F_p^\times.
\tag{943.7}
$$
Since $(-3/p)=-1$, one has $\epsilon^2=27$. The ordinary Legendre derivative identity gives
$$
(x^2-1)A'=m(xA-L),
\qquad
L=xA-\frac83A'
\quad\text{in characteristic }p.
$$
Also $d^{-1}=x/3$, so (943.6) yields the exact central identity
$$
\boxed{\epsilon L=2V-U.}
\tag{943.8}
$$
It does not divide by $U$. The Cartier operator therefore satisfies
$$
\boxed{
\mathcal C\bigl((2w-1)\omega_*\bigr)
=\epsilon L\,\omega_*.
}
\tag{943.9}
$$
Indeed $(2w-1)f_*(w)^m$ has degree $3m+1<2p-1$, so its only exponent selected by Cartier is $p-1$, with coefficient $2V-U$.

Adjacent Legendre polynomials $P_m$ and $P_{m-1}$ cannot vanish together: the three-term recurrence, with all intervening indices below $p$, would force $P_0=0$. Hence
$$
U=0\ \Longrightarrow\ A=0\ \Longrightarrow\ L\ne0.
\tag{943.10}
$$
Thus every supersingular reduction of $E_*$ in this class has nonzero central factor. A hypothetical central zero lies in the ordinary subset. The argument does not assume that $E_*$ is ordinary at every allowed prime.

## 3. A second exact form of the central differential

The rational degree-two map
$$
w_2=w+\frac9{w+1},\qquad
v_2=v\left(1-\frac9{(w+1)^2}\right)
\tag{943.11}
$$
has target
$$
E_2:\ v_2^2=w_2^3-39w_2+70,
\qquad \phi_2^*\omega_2=\omega_*.
$$
Direct differentiation gives the exact identity
$$
\boxed{
(2w-1)\omega_*
=\phi_2^*((w_2-2)\omega_2)
 +d\left(\frac v{w+1}\right).
}
\tag{943.12}
$$
In fact the exact term is $(w+1-9/(w+1))\omega_*$. After $u=w_2-2$, the target becomes
$$
v_2^2=u(u+9)(u-3).
$$
Cartier commutes with the separable isogeny and kills the displayed exact term. Since pullback of the invariant differential is nonzero,
$$
\boxed{
[u^{p-2}]\bigl(u(u+9)(u-3)\bigr)^m
=\epsilon L
=-3\sum_{i=0}^{m-1}\binom mi\binom m{i+1}(-1/3)^i.
}
\tag{943.13}
$$
For the finite sum, the chosen exponents in $(u+9)^m(u-3)^m$ add to $m-1$, and $9^m=1$ modulo $p$. This is a second-kind coefficient, not the holomorphic Hasse invariant of the curve. Full rational two-torsion does not by itself make this coefficient nonzero.

## 4. One fixed three-torsion curve for the old third-position pair

Use a variable $T$, distinct from the integer $t$ in $p=12t+11$, and define
$$
\begin{aligned}
a(T)&=12T-15,\\
b(T)&=4T^2-28T+22,\\
f(X,T)&=X^3+a(T)X+b(T),\\
E_T&:\ Y^2=f(X,T),\qquad \omega_T=\frac{dX}{2Y}.
\end{aligned}
\tag{943.14}
$$
The discriminant is
$$
\Delta(T)=-6912(T-1)(T+1)^3.
\tag{943.15}
$$
The point $(3,2(T+1))$ has order three. Explicitly, setting
$$
X=u+3,\qquad Y=v+3u+2(T+1)
$$
gives
$$
v^2+6uv+4(T+1)v=u^3.
\tag{943.16}
$$
At $(u,v)=(0,0)$ the tangent $v=0$ has triple intersection. This proves the order-three assertion whenever $T\ne\pm1$. At the original $x=1/s$, $x^2=-1/3$ ensures good reduction in the whole range (943.1).

The specialization $E_x$ is one fixed curve over $\mathbf Q(s)$, equipped with its displayed order-three point and differential. It is not assumed ordinary, CM, or isomorphic to the different rational curve $E_*$.

### 4.1. Exact Hasse polynomial and a total-derivative certificate

For any prime $p>3$ with $p\equiv2\pmod3$, put
$$
H(T)=[X^{p-1}]f(X,T)^m,
\qquad m=(p-1)/2,\qquad n_3=(p-2)/3.
$$
We prove the polynomial identity
$$
\boxed{H(T)=-P_{n_3}(T)\quad\text{in }\mathbf F_p[T].}
\tag{943.17}
$$
Because this is a polynomial identity, it can be specialized at $x\notin\mathbf F_p$ without extending a finite-field character-sum formula beyond its domain.

Define
$$
\mathcal L=(1-T^2)\partial_T^2-2T\partial_T-\frac29
$$
and the explicit polynomial
$$
\begin{aligned}
S(X,T)={}&\frac29X^4+\frac{4T-14}{3}X^2\\
&+\frac{-4T^2-44T+68}{9}X
 +\frac43(T+1)^2.
\end{aligned}
\tag{943.18}
$$
Writing $f_T=12X+8T-28$, the following rational polynomial identity is verified coefficient by coefficient:
$$
\boxed{
(1-T^2)\left(\frac34f_T^2-4f\right)
 +Tf f_T-\frac29f^2
=2fS_X-3Sf_X.
}
\tag{943.19}
$$
This is a finite algebraic certificate, with no arithmetic window in its proof. Since $m=-1/2$ modulo $p$ and $f_{TT}=8$, multiplication of (943.19) by $f^{m-2}$ gives
$$
\mathcal L(f^m)=\partial_X(2Sf^{m-1})
\quad\text{in }\mathbf F_p[X,T].
\tag{943.20}
$$
The coefficient of $X^{p-1}$ on the right is zero, because it is $p$ times the coefficient of $X^p$ before differentiation. Thus $\mathcal L H=0$.

To check its degree, write $p=6N+5$, so $m=3N+2$ and $n_3=2N+1$. A monomial contributing to $[X^{p-1}](X^3+aX+b)^m$ has multiplicities $i,j,\ell$ with
$$
i+j+\ell=m,\qquad 3i+j=2m.
$$
They take the form
$$
i=2N+1-r,\qquad j=3r+1,\qquad\ell=N-2r,
\qquad r\ge0.
$$
Its degree in $T$ is at most $j+2\ell=2N+1-r\le n_3$. Hence $\deg H\le n_3$.

Now $n_3(n_3+1)=-2/9$ modulo $p$, so $P_{n_3}$ satisfies the same equation. Among polynomials of degree at most $n_3$, this equation has one-dimensional solution space: for a possible degree $j<n_3$, the diagonal coefficient $n_3(n_3+1)-j(j+1)$ is nonzero, since the other root $p-1-n_3$ exceeds $n_3$. The coefficient recurrence then determines the polynomial from its leading coefficient.

Finally, at $T=1$,
$$
f(X,1)=(X+1)^2(X-2),
$$
and
$$
\begin{aligned}
H(1)
&=\sum_{j=0}^{m}(-1)^j\binom mj(-2)^{m-j}\\
&=(-3)^m=\left(\frac{-3}{p}\right)=-1.
\end{aligned}
$$
Since $P_{n_3}(1)=1$, the scalar is $-1$, proving (943.17).

The curve family also appears in Zhi-Hong Sun, [*Legendre polynomials and supercongruences*, Acta Arithmetica 159.2 (2013)](https://doi.org/10.4064/aa159-2-6), equation (1.5), in its character-sum formulation. The polynomial proof above supplies the sign, scale and non-rational specialization needed here directly.

## 5. Exact Gauss–Manin reduction and Cartier specialization

Set
$$
v_T=\frac1{6(1-T^2)},\qquad
u_T=\frac{2T-1}{6(1-T^2)},
$$
$$
R(X,T)=-v_TX^2+u_TX-\frac{2a(T)v_T}{3}.
\tag{943.21}
$$
Then the exact rational differential identity is
$$
\boxed{
\partial_T\omega_T
=(u_T+v_TX)\omega_T+d_X\left(\frac{R(X,T)}Y\right).
}
\tag{943.22}
$$
Here $\partial_T\omega_T$ is the parameter derivative of the displayed differential, represented on each fixed fiber by $-f_T\omega_T/(2f)$.

An explicit verification uses
$$
2a u_T-3b v_T=-6,\qquad
3b u_T+\frac{2a^2v_T}{3}=-\frac{b'(T)}2.
$$
These imply
$$
-\frac{f_T}2
=(u_T+v_TX)f+2R_Xf-Rf_X,
$$
which is exactly (943.22), because
$$
d_X(R/Y)=\frac{2R_Xf-Rf_X}{f}\,\omega_T.
$$
At $T=x$, write $\omega=\omega_x$ and
$$
\dot\omega=(\partial_T\omega_T)|_{T=x}.
$$
Since $6(1-x^2)=8$, formula (943.22) gives
$$
\boxed{\dot\omega\equiv\frac{X+2x-1}{8}\,\omega\pmod{d,k(E_x)}.}
\tag{943.23}
$$

The two Cartier coefficients are exactly
$$
\mathcal C(\omega)=H(x)^{1/p}\omega,
\qquad
\mathcal C(\dot\omega)=H'(x)^{1/p}\omega.
\tag{943.24}
$$
For the second formula, use $Y^p=Yf(X,x)^m$ to write
$$
\dot\omega
=\frac{-\tfrac12 f_T(X,x)f(X,x)^{m-1}}{2Y^p}\,dX.
$$
Modulo $p$, the numerator is $(\partial_T f^m)|_{T=x}$. Its degree in $X$ is $3m-2<2p-1$, so Cartier selects exactly the coefficient $H'(x)$ at $X^{p-1}$. Thus (943.24) is a direct coefficient proof, not an unsupported interchange of the Cartier operator with parameter differentiation.

The operator is inverse-Frobenius semilinear. All uses below retain that fact: $H(x)=-P_{n_3}(x)$ is generally outside $\mathbf F_p$, whereas each even-degree neighboring Legendre value lies in $\mathbf F_p$.

## 6. Four fixed second-kind forms, including both old legal endpoints

Write
$$
A_3=P_{n_3}(x),\qquad A'_3=P'_{n_3}(x).
$$
Reducing $n_3=-2/3$ and using $x^2=-1/3$, the derivative identity and recurrence give
$$
\begin{aligned}
P_{n_3-1}(x)&=xA_3-2A'_3,\\
P_{n_3+1}(x)&=xA_3-4A'_3,\\
P_{n_3-2}(x)&=-\frac{13}{15}A_3-\frac{14}{5}xA'_3,\\
P_{n_3+2}(x)&=-\frac23A_3-5xA'_3,\\
P_{n_3-3}(x)&=\frac{-61xA_3+83A'_3}{30},\\
P_{n_3+3}(x)&=\frac{-34xA_3+103A'_3}{21}.
\end{aligned}
\tag{943.25}
$$
Every denominator is a unit in (943.1), and all indices are nonnegative and below $p$.

For example, the lower two steps are
$$
P_{n_3-2}=\frac{7xP_{n_3-1}-2A_3}{5},\qquad
P_{n_3-3}=\frac{13xP_{n_3-2}-5P_{n_3-1}}8,
$$
while the upper two are
$$
P_{n_3+2}=\frac{5xP_{n_3+1}-A_3}{4},\qquad
P_{n_3+3}=\frac{11xP_{n_3+2}-4P_{n_3+1}}7.
$$
Thus the constants in (943.25) come from fixed paper recurrences, not from fitting a prime window.

Combining (943.17), (943.23) and (943.24) proves the following exact table on the one fixed curve $E_x$:

| Fixed second-kind differential $\beta$ | Exact Cartier value $\mathcal C(\beta)$ | Actual old branch using this factor |
|---|---|---|
| $(X-1-2x)\omega$ | $4P_{n_3-1}(x)\omega$ | $p\equiv5\pmod9$, $h=q-1$ |
| $(-83X+83+322x)\omega$ | $240P_{n_3-3}(x)\omega$ | $p\equiv5\pmod9$, $h=2q+3$ |
| $(X-1)\omega$ | $2P_{n_3+1}(x)\omega$ | $p\equiv2\pmod9$, $h=2q-1$ |
| $(-103X+103+66x)\omega$ | $168P_{n_3+3}(x)\omega$ | $p\equiv2\pmod9$, $h=q+3$ |

To check the semilinear constants explicitly, for $c\in\{2,4\}$ define $\beta_c=x\omega-c\dot\omega$. Then
$$
\mathcal C(\beta_c)
=\bigl(xH(x)-cH'(x)\bigr)^{1/p}\omega
=-\bigl(xA_3-cA'_3\bigr)\omega,
\tag{943.26}
$$
because the final Legendre value lies in $\mathbf F_p$. Modulo exact forms,
$$
-4\beta_2=(X-1-2x)\omega,
\qquad -2\beta_4=(X-1)\omega.
$$
For the remaining rows, (943.23) and (943.25) give
$$
\begin{aligned}
(-83X+83+322x)\omega
&\equiv488x\omega-664\dot\omega,\\
(-103X+103+66x)\omega
&\equiv272x\omega-824\dot\omega.
\end{aligned}
$$
Their Cartier coefficients are respectively
$$
(-488xA_3+664A'_3)^{1/p}
=240P_{n_3-3}(x),
$$
$$
(-272xA_3+824A'_3)^{1/p}
=168P_{n_3+3}(x).
$$
This proves all four rows, including their scales and the original choice of $x$.

There is a useful consistency check with the already established old pair. The two forms in its $p\equiv5\pmod9$ row satisfy
$$
(-83X+83+322x)\omega+83(X-1-2x)\omega
=156x\omega,
$$
and the two forms in its $p\equiv2\pmod9$ row satisfy
$$
(-103X+103+66x)\omega+103(X-1)\omega
=66x\omega.
\tag{943.27}
$$
The constants $156$ and $66$ have only the small exceptional prime factors $2,3,13$ and $2,3,11$ respectively, matching the old recurrence proof's exclusions. This describes the old non-common-zero pair by fixed second-kind forms; it does not create a new proof claim for that already registered pair.

## 7. The exact three-isogeny of the fixed family

The rational three-torsion structure has a further explicit description. Put $c=T+1$ and
$$
r_T(X)=X+\frac{24c}{X-3}+\frac{16c^2}{(X-3)^2}.
\tag{943.28}
$$
Then
$$
\phi_3:(X,Y)\longmapsto\bigl(r_T(X),Y r'_T(X)\bigr)
\tag{943.29}
$$
is a normalized degree-three isogeny with kernel generated by $(3,2(T+1))$. Its target is
$$
E'_T:\ {Y'}^2={X'}^3+9a(-T)X'-27b(-T),
\qquad \phi_3^*\omega'_T=\omega_T.
\tag{943.30}
$$
One direct verification is the rational identity
$$
f(X,T)r'_T(X)^2
=r_T(X)^3+9a(-T)r_T(X)-27b(-T).
\tag{943.31}
$$
The formula for $r_T$ also follows by adding the two nonzero kernel points in the elliptic addition law: with $P_3=(3,2c)$,
$$
X+\sum_{Q=\pm P_3}\bigl(X(P+Q)-X(Q)\bigr)
=\frac{2(f(X,T)+4c^2)}{(X-3)^2}-X-12
=r_T(X).
$$
The function $r_T$ has double poles exactly at infinity and at the two nonzero kernel points. Thus the pointed morphism (943.29) has degree three; its displayed derivative proves the differential normalization in (943.30).

Over $\mathbf Q(s)$, division of the target coordinates by $s^2,s^3$ identifies $E'_T$ with $E_{-T}$, since $s^4=9$ and $s^6=-27$. The resulting isogeny $\psi_T:E_T\to E_{-T}$ satisfies
$$
\boxed{\psi_T^*\omega_{-T}=s\omega_T.}
\tag{943.32}
$$
In particular $E_x$ is three-isogenous to its conjugate $E_{-x}$, with the exact differential multiplier $s$. This does not identify it with $E_*$, make the second-kind forms holomorphic, or impose the unknown original sigma-unit condition. No assertion of ordinarity or central-versus-third joint nonvanishing is deduced from this isogeny alone.

## 8. Exact remaining scope

The old two third-position labels already guarantee a nonzero original Legendre factor at one actual primitive label. This result places every factor in that old choice on one fixed three-torsion curve, with fully specified second-kind differentials. The separate central factor is likewise placed on its original rational auxiliary curve, including auxiliary supersingular primes.

These interfaces do not prove that the actual sigma product in (943.4) is nonzero at the label selected by Legendre visibility. They do not supply a bounded weight for the old third-position pair, a new $Q'_h(0)$ theorem at those labels, or the separate original height/rational-point comparison. Rational torsion, a three-isogeny to the conjugate, and a finite empty zero window are not substitutes for any of those statements. Serre uniformity remains open.

## Appendix A. Public finite window, independent of the paper proofs

The public consumer [p11_original_legendre_window.py](../scripts/p11_original_legendre_window.py) tests the central label and the actual single third-position branch
$$
h_{\rm selected}=
\begin{cases}
q-1,&p\equiv5\pmod9,\\
2q-1,&p\equiv2\pmod9.
\end{cases}
$$
It also records the two fixed offsets $h_0\pm6$ with their actual gcds, without assuming those offsets primitive. It computes the original Legendre values by one factorial recurrence, retains the auxiliary supersingular possibility, and provides an independent finite-sum check if a central zero occurs. It does not numerically test the new family identity (943.19) or the three-isogeny identity (943.31); those are the displayed paper certificates above.

The completed public run has:

- Source commit: `cfa323577937abf5f80652bacab6bd81971db2d6`.
- [Run 44718206366](https://github.com/Rogerhu12/math-research-public/actions/runs/44718206366), job `136226900472`, success.
- Arguments: `--bound 10000 --allowed-mod9 --stop-after 0 --output /tmp/p11-original-legendre-window.json`.
- Script SHA256: `b53d466e84fb8f7ffd0062f71455dc6e558fd686cf2f0c31f9325159f6476ceb`.
- Deterministic row-stream SHA256: `612e3dbc612cffd8e1be17345cab0fe23cbca847a0bba11cfaeac4ef554e33d9`.
- Deterministic output SHA256: `f4e7416026c5cf358f6b473185cabf1d105998e8db2e79f2c457cecb7996400a`.

The window contains exactly 203 primes, its last prime is 9923, and it has no central zero and no zero at the selected legal third-position branch. There are eight supersingular reductions of $E_*$ in this finite set. The joint-zero count is zero as a consequence of these finite counts; it is not a separate uniform exclusion.

New arithmetic was executed only in public repository Actions. Local checks were restricted to IO, source review, AST and byte hashes. Reproducible arrays and JSON are not stored in Git or Releases. The paper identities in §§2–7 do not depend on the finite window.

## Appendix B. Public exact symbolic verification

The independent standard-library script [p11_fixed_cartier_symbolic.py](../scripts/p11_fixed_cartier_symbolic.py) expands the displayed certificates in the sparse polynomial ring $\mathbf Q[T,X,Y]$, using exact `Fraction` coefficients. It verifies all coefficients after clearing denominators: (943.19) is multiplied by $36$, (943.22) by $6D$ with $D=6(1-T^2)$, and (943.31) by $(X-3)^6$.

All nine polynomial identities pass, including $f_{TT}=8$, the two separate Gauss–Manin coefficient equations, the discriminant factor, the Tate order-three model and the numerator of $r'_T$. All nine additional checks in $\mathbf Q(s)$ pass as well: they verify the target coordinate scaling and the actual differential multiplier $s$, with $s^2=-3$. This verification does not include a new prime window or assert any unknown nonvanishing.

- Source commit: `1f394d300f92824f3bb1253af1f44ca7c1652501`.
- [Run 44719847377](https://github.com/Rogerhu12/math-research-public/actions/runs/44719847377), job `136232493369`, success.
- Arguments: `--output /tmp/p11-fixed-cartier-symbolic.json`.
- Script SHA256: `01fcc962895c9e56b9e693603e680f80d4d84eba8329ffcc69fe96dc9f5b93b6`.
- Deterministic output SHA256: `dfe48b94654e4e14dafe67e390bda7abfd176d8c80e9bd84ebdbb1335b69f7f9`.

This is a public exact verification of the specific source and sign certificates used in the proof. No mathematical part of this script was executed locally.

## Sources and dependencies

- The [old swapped-third-label result](../notes/2026-11-16-sigma-two-swapped-primitive-labels-at-thirds.md), commit `543d03f8`: the actual full-modulus primitive pair, its Legendre non-common-zero theorem and the precise sigma ordering.
- R898: the actual $\Gamma_h$, $\mathcal Z_h$, split vector, determinant extension and ordinary fifth-jet source.
- R929/R933: the original $E_*$, translation/twist convention and polynomial coefficient comparison, with the odd-$m$ signs proved explicitly here.
- R697/R770/R925: the original sigma factors and the unaltered same-label requirement.
- Sun's cited primary paper, equation (1.5), for the known character-sum occurrence of the family; (943.17) is proved here as a polynomial identity with its complete normalization.
