# R933: Same-label Legendre zero as Cartier vanishing of a fixed second-kind differential

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: proved algebraic equivalence; nonvanishing remains open.** This note continues the exact four-step shift in R929. It does not redo R929's ordinarity theorem, and it does not assert that the shifted value is nonzero. No arithmetic was executed locally.

## 1. Statement in the original rational auxiliary model

Let $p\ge41$ be prime with $p\equiv5\pmod{12}$, and retain precisely
$$
s^2=-3,\qquad x_0=s^{-1},\qquad
\lambda_0=(1-x_0)/2,\qquad m=(p-1)/2,
$$
$$
A=P_m(x_0),\qquad L_h=P_{h-1}(x_0),\qquad h=(p+9)/2.
$$
The original Serre residual source further restricts to $p\equiv2,5\pmod9$; every identity below holds before imposing that restriction, so it also holds on the original subset.

Use the actual rational model and differential of R929:
$$
E_*:v^2=f(w)=w^3+6w+7,\qquad \omega=\frac{dw}{2v}.
$$
Define two coefficients in $\mathbf F_p$:
$$
U_p=[w^{p-1}]f(w)^m,\qquad V_p=[w^{p-2}]f(w)^m.
\tag{LS1}
$$
Keep the nontrivial phase
$$
\delta_p=(-27)^{(p-1)/4},\qquad \delta_p^2=-1.
$$
R929 proves $U_p=\delta_pA\ne0$. The new identity is
$$
\boxed{315\delta_p L_h=283U_p-224V_p.}
\tag{LS2}
$$
Thus the remaining same-label condition has an equivalent formulation entirely on one fixed rational elliptic curve:
$$
\boxed{L_h=0\iff \frac{V_p}{U_p}=\frac{283}{224}.}
\tag{LS3}
$$
All displayed denominators are units in the stated range. In particular $p=283$ does not occur since $283\equiv7\pmod{12}$.

## 2. A coefficient identity in the Legendre family

Temporarily work with a variable $\lambda$. Set
$$
F_\lambda(Z)=Z(Z-1)(Z-\lambda),\qquad
H(\lambda)=[Z^{p-1}]F_\lambda(Z)^m,
$$
$$
B(\lambda)=[Z^{p-2}]F_\lambda(Z)^m.
$$
The known finite expansion, also proved in R929, is
$$
H(\lambda)=(-1)^m\sum_{j=0}^{m}\binom mj^2\lambda^j.
$$
The analogous expansion one coefficient below it is
$$
B(\lambda)=(-1)^{m+1}
\sum_{j=1}^{m}\binom m{j-1}\binom mj\lambda^j.
\tag{LS4}
$$
We claim the polynomial identity
$$
\boxed{B=\lambda H-2\lambda(1-\lambda)H'.}
\tag{LS5}
$$
Write $c_j=\binom mj^2$ and use $m=-1/2$ in $\mathbf F_p$. For $1\le j\le m$,
$$
\frac{c_{j-1}}{c_j}=\frac{4j^2}{(2j-1)^2},\qquad
-\frac{\binom m{j-1}\binom mj}{c_j}
=\frac{2j}{2j-1}.
$$
The coefficient of $(-1)^m\lambda^j$ on the right of (LS5) is
$$
-2jc_j+(2j-1)c_{j-1}
=\frac{2j}{2j-1}c_j,
$$
which is the coefficient in (LS4). The constant term is zero on both sides. The potential top coefficient at degree $m+1$ is $(1+2m)c_m=0$. This proves (LS5) as an identity of polynomials, not just after specialization.

At $\lambda_0$, one has $\lambda_0(1-\lambda_0)=1/3$, $m$ even, $H(\lambda_0)=A$, and $H'(\lambda_0)=-2P_m'(x_0)$. Consequently
$$
B(\lambda_0)=\lambda_0A+\frac43P_m'(x_0).
\tag{LS6}
$$

## 3. Translation and the original twist, with both coefficient scales

Put $c=(1+\lambda_0)/3$ and translate $Z=u+c$ as in R929. Its short cubic is
$$
F_0(u)=u^3-\frac29u-\frac7{81s}.
$$
Translation does not change the coefficient of degree $p-1$. It changes the coefficient of degree $p-2$ by precisely minus $c$ times that coefficient:
$$
[u^{p-1}]F_0(u)^m=A,
$$
$$
[u^{p-2}]F_0(u)^m=B(\lambda_0)-cA.
\tag{LS7}
$$
Here is a direct check covering every higher coefficient. For $p\le k\le3m<2p-2$, the binomial coefficients $\binom{k}{p-1}$ and $\binom{k}{p-2}$ vanish modulo $p$ by their base-$p$ digits. The only extra contribution to the coefficient of degree $p-2$ therefore comes from degree $p-1$, with coefficient $\binom{p-1}{p-2}c=-c$. No higher term has been dropped.

Since $2\lambda_0-1=-x_0$, (LS6) and (LS7) yield
$$
[u^{p-2}]F_0(u)^m
=\frac{-x_0A+4P_m'(x_0)}3.
\tag{LS8}
$$
Now use the original $d=3s$ and $f(w)=d^3F_0(w/d)$. For an arbitrary index $k$, the corresponding coefficient of the $m$th power is multiplied by $d^{3m-k}$. Thus the two scales here are respectively $d^m$ and $d^{m+1}$:
$$
U_p=d^mA=\delta_pA,
$$
$$
V_p=d^{m+1}\frac{-x_0A+4P_m'(x_0)}3.
\tag{LS9}
$$
Since $sx_0=1$, division by the proved nonzero $U_p$ gives
$$
\boxed{\frac{V_p}{U_p}=-1+4s\frac{P_m'(x_0)}A.}
\tag{LS10}
$$
The identity $s^2=-3$ now implies
$$
\frac{x_0P_m'(x_0)}A=-\frac1{12}\left(\frac{V_p}{U_p}+1\right).
$$
Insert this into the exact same-label four-step formula R929(929.5):
$$
\frac{L_h}{A}
=\frac{169+896x_0P_m'(x_0)/A}{105}
=\frac{283-224V_p/U_p}{315}.
$$
Together with $U_p=\delta_pA$, this proves (LS2) and (LS3).

## 4. The fixed differential and an exact rational primitive criterion

Define over $\mathbf Q$, on the fixed curve $E_*$, the second-kind differential
$$
\beta=(224w-283)\omega.
\tag{LS11}
$$
It has no finite pole and has a double pole at infinity with zero residue. After good reduction at the primes in question, its Cartier operator is given exactly by
$$
\boxed{\mathcal C(\beta)
=(224V_p-283U_p)\omega
=-315\delta_pL_h\,\omega.}
\tag{LS12}
$$
Indeed, because $v^p=vf(w)^m$,
$$
\beta=\frac{(224w-283)f(w)^m}{2v^p}\,dw.
$$
Cartier selects the terms whose exponent in $w$ is $p-1$ modulo $p$. The numerator has degree $3m+1<2p-1$, so the only selected exponent is $p-1$. Its coefficient is $224V_p-283U_p$. Every coefficient lies in $\mathbf F_p$, so taking its $p$th root does not change it; the factor $1/(2v^p)$ becomes $1/(2v)$. This proves (LS12) directly.

There is also an explicit rational-exactness description. Write
$$
(224w-283)f(w)^m=\sum_{k=0}^{3m+1}b_kw^k.
$$
If $L_h=0$, then $b_{p-1}=0$, and
$$
T_p(w)=\sum_{\substack{0\le k\le3m+1\\k\ne p-1}}
\frac{b_k}{k+1}w^{k+1}
$$
is defined in $\mathbf F_p[w]$, since $p$ is the only possible nonunit among the denominators $k+1$ in this range. In the function field of $E_*/\mathbf F_p$,
$$
\boxed{\beta=d\left(\frac{T_p(w)}{2v^p}\right).}
\tag{LS13}
$$
Conversely the Cartier operator kills every exact rational differential; this is immediate by applying the formal derivative to a rational function in a separating variable and retaining exponents congruent to $p-1$. Hence rational exactness of $\beta$ implies $L_h=0$ by (LS12).

This formulation concerns reduction modulo $p$. It does not assert exactness in characteristic zero, an identity of $p$-adic unit-root lines, or an equality of $p$-adic periods. A characteristic-zero nonexactness statement alone does not rule out (LS13) at individual primes.

## 5. Scope and the new finite-window consumer

R929 proves $U_p\ne0$ but supplies no relation excluding $V_p/U_p=283/224$. Thus (LS2) is a source-preserving restatement of the actual remaining condition, not a proof of its nonvanishing. Neither the first original normal coefficient $Q_h'(0)$ nor the separate global height comparison is addressed here.

The new consumer `scripts/same_label_legendre_window.py` tests this still-open shifted factor, using the factorial-normalized recurrence
$$
q_n=n!P_n(x_0),\qquad
q_n=(2n-1)x_0q_{n-1}-(n-1)^2q_{n-2}.
$$
Parity puts $q_{2a}\in\mathbf F_p$ and $q_{2a+1}\in x_0\mathbf F_p$, so one scalar is stored per index. The tested original factor is $P_{m-4}(x_0)=L_h$. As an exact consistency relation, with $C=P_{m-1}(x_0)/x_0$, one has
$$
x_0P_m'(x_0)=\frac{C-A}{8},\qquad
L_h=\frac{57A+112C}{105}.
$$
Each zero is checked by the finite coefficient formula for $P_{m-4}$. The default window includes all $p\equiv5\pmod{12}$, and `--allowed-mod9` restricts to the original $p\equiv2,5\pmod9$ classes. Output distinguishes these ranges. A finite empty window would be only finite evidence, not a proof of uniform nonvanishing.

The public workflow is `serre-same-label-legendre.yml`. Run metadata and exact output hashes are recorded separately; this proof asserts no finite-window result.

## Dependency

- [R929](R929-original-Legendre-auxiliary-ordinary-curve-and-central-shift.md), *The original Legendre auxiliary curve is ordinary in the split Gaussian class* (2026-11-16), §§1, 2, 4, 5: original argument, exact rational model, differential/twist phase, proved unit $A$, and the four-step shift. The new coefficient and Cartier comparisons are proved fully above.
