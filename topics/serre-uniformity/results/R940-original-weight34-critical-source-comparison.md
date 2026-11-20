# R940 — Original weight-34 normal coefficients and the same-label critical source

Date: 2026-11-20. Status: **proved outside the explicit fixed bad integer of R937**. This extends R925 to the actual primitive weight-34 label, using R938's original normal function and the publicly computed fixed coefficient $f_5$. It retains the exact original theta source, fifth jet, full norm, phases and Tate index. It does not prove that the low normal coefficient or the same-label critical source is nonzero.

## 1. Range, fixed constants and conclusion

Let
$$
p=12t+5\ge41,\qquad p\equiv2,5\pmod9,
\qquad p\nmid B_{34},
\tag{940.1}
$$
where R937 defines
$$
\begin{aligned}
D_{34}&=6257370208079794820150643464381912640000000000000,\\
C_{34}^{\rm mark}&=1350702136960,\qquad
B_{34}=D_{34}C_{34}^{\rm mark}.
\end{aligned}
\tag{940.2}
$$
The superscript distinguishes the marked modular-form constant from R697's indexed Cartier constants below. Retain the original quotient, center $c_1$, $c_0$ subtraction, positive CM coordinate, full norm character, determinant extension, two-oldform phase and Tate index $a_h$.

Put
$$
h=\frac{p+33}{2}=6t+19,\qquad
J=\frac{p-35}{6}=2t-5,\qquad
D=3J-1=\frac{p-37}{2}.
\tag{940.3}
$$
Its actual upper companion has weight $34$ and the other actual companion has weight $p-31$. The label $h$ is odd, $h\equiv1\pmod6$, and any common divisor of $h$ and $p+1$ divides $2h-(p+1)=32$. Hence
$$
\gcd(h,p+1)=1,\qquad 7\le h\le p-4.
\tag{940.4}
$$
Thus this is a genuine label in R898's original admissible range.

On exactly the original elliptic curve and differential
$$
E_0:y^2=x^3-1,\qquad dz=\frac{dx}{2y},\qquad x'=2y,
$$
write the original $c=0$ sigma series
$$
F=x\sigma^6=z^4\sum_{i\ge0}f_i z^{6i},\qquad
G=-xy\sigma^6=z\sum_{i\ge0}g_i z^{6i}.
\tag{940.5}
$$
The exact fixed coefficient is
$$
\boxed{
f_5=-\frac{270862728}{5123589312701234375}
=-\frac{2^3\cdot3\cdot41\cdot71\cdot3877}
 {5^6 7^4 11^2 13^2\cdot17\cdot19\cdot23\cdot29\cdot31}.
}
\tag{940.6}
$$
For primes $p\ge41$ its denominator is a unit, and its only possible zero residues are at $41,71,3877$. In the present class $p\equiv5\pmod{12}$, only $41$ occurs. Each of these three numerator primes already divides $C_{34}^{\rm mark}$, so (940.1) ensures that $f_5$ is a unit without introducing a further bad integer.

R938 gives the actual calibrated polynomial
$$
Q_h(w)=\overline{p^{-a_h}G_h(w)}
=\sum_{j=1}^{J}q_{h,j}w^j,\qquad q_{h,J}\ne0.
\tag{940.7}
$$
For the original Cartier unit $B\in\mathbf F_p^\times$ of R705/R727, set
$$
u_h=\frac{6\overline f_5}{(3J)!}(81B^6)^{J-1}
\in\mathbf F_p^\times.
\tag{940.8}
$$
We prove that the original critical source at this same $h$ satisfies
$$
\boxed{
\mathscr J_h^2
=\left[
\frac{(6B)^5}{12}P_{h-1}(1/s)\,u_h
\frac{Q_h'(0)}{q_{h,J}}
\right]^2,
\qquad s^2=-3.
}
\tag{940.9}
$$
Here $\mathscr J_h$ is exactly the original $J_{3,2}$ of the actual $\mathcal Z_h(u_{G,F})$, specified in §2. In particular
$$
\mathscr J_h\ne0
\quad\Longleftrightarrow\quad
P_{h-1}(1/s)\ne0\ \text{and}\ Q_h'(0)\ne0.
\tag{940.10}
$$
No one of the factors in this conjunction is replaced by a factor at another label.

## 2. The exact original source and the actual critical pair

The maps of R898 apply at every $h$ in (940.4):
$$
\Gamma_h(u)=-p\,u\otimes\Phi_{0,h},
\qquad
\mathcal Z_h
=\varpi^{-p(p-1)}\rho_h(\mathsf B^{-1})\mathcal A_h\Gamma_h
=\beta_h(t_*)\mathcal J_h.
\tag{940.11}
$$
Keep the full determinant extension and the nontrivial transport of the split vector from R898. Its primary index pair is exactly
$$
|p-h,h-1\rangle
=\left|\frac{p-33}{2},\frac{p+31}{2}\right\rangle.
\tag{940.12}
$$
The quotient section remains $u_{G,F}$, associated with
$$
m_{G,F}=((-xy)^ps_{6p})\otimes(x^ps_{6p}).
$$
The functional remains the ordinary fifth jet $J_{3,2}$. In R898(898.36), the actual indices are
$$
N=\frac{p-5}{6}=2t,\qquad
i=\frac{h-7}{6}=t+2,\qquad
\ell=N-1-i=t-3.
$$
Consequently
$$
\boxed{
\mathscr J_h
:=\overline{J_{3,2}(\mathcal Z_h(u_{G,F}))}
=\frac{(6B)^5}{12}\,P_{h-1}(1/s)
\bigl(\overline{f_{t+2}g_{t-3}}\bigr)^p.
}
\tag{940.13}
$$
The rational sigma coefficients reduce in $\mathbf F_p$, so the displayed Frobenius power may be removed. The residue $s$, Cartier unit $B$, original Tate index and phase are unchanged. No half-period replacement of $h$, independent phase choice or altered $\Gamma$ character is made.

For comparison with the whole normal polynomial, define
$$
m_j=3j-1,\qquad
k_{1,j}=h-m_j,\qquad
k_{2,j}=p-h-m_j\qquad(1\le j\le J).
\tag{940.14}
$$
The reference pair at the highest normal coefficient is
$$
(k_{1,J},k_{2,J})=(35,2),
\tag{940.15}
$$
whereas the actual critical pair, at $j=1$ and $m=2$, is
$$
(k_{1,1},k_{2,1})
=\left(\frac{p+29}{2},\frac{p-37}{2}\right).
\tag{940.16}
$$
Thus the top product is $f_5g_0=f_5$, and the critical product is $f_{t+2}g_{t-3}$. The former supplies a unit reference; it does not change the latter into a high jet.

## 3. All ranges for the higher-block comparison

For every $1\le j\le J$,
$$
2\le m_j\le D=\frac{p-37}{2}\le p-3,
\qquad m_j\equiv2\pmod3,
$$
$$
k_{1,j}\ge35,\qquad k_{2,j}\ge2,
\qquad D+1=3J=\frac{p-35}{2}<p.
\tag{940.17}
$$
These are the hypotheses needed for R855's full higher-block identity. Exactly one of $k_{1,j},k_{2,j}$ is $5$ modulo $6$ and the other is $2$ modulo $6$. Define the product with its actual ordering:
$$
\Sigma_j=
\begin{cases}
f_{(k_{1,j}-5)/6}g_{(k_{2,j}-2)/6},&k_{1,j}\equiv5\pmod6,\\
g_{(k_{1,j}-2)/6}f_{(k_{2,j}-5)/6},&k_{1,j}\equiv2\pmod6.
\end{cases}
\tag{940.18}
$$
All indices are nonnegative. Their ordinary Taylor orders $k_{i,j}-1$ are below $p$, so R697 proves their $p$-integrality. In particular
$$
\Sigma_J=f_5,
\qquad \Sigma_1=f_{t+2}g_{t-3}.
\tag{940.19}
$$
The geometric lower endpoint $p=41$ has $J=1$, $D=2$ and $h=37$. The inequalities and index identities remain valid there; none requires the $J\ge5$ bound particular to R925's older two labels. But $41\mid B_{34}$ and $\overline f_5=0$ at that prime. The unit comparison of this result therefore excludes that previously registered case, without reopening or asserting a new conclusion about it.

## 4. Whole calibrated logarithm and exact norm cancellation

R938 supplies the original integral completed-Hom map and the polynomial (940.7). Because $h/(p+1)>1/2$, the calibrated logarithm argument of R925 §2 applies without alteration:
$$
L_h^{\rm cal}(W)=W+pW^2V_h(W),
\qquad V_h\in R_0\langle W\rangle.
$$
It preserves the entire integral reduction after division by $p^{a_h}$, including the infinite tail. The original flat/coarse change
$$
\Psi(w)\equiv\frac38w\pmod p
$$
is independent of $h$. The actual Hodge comparison has one common scalar $c_h^{\rm cal}$. Thus R925(925.28) holds for the new $J,D$:
$$
\frac{q_{h,j}}{q_{h,J}}
=\left(\frac38\right)^{j-J}
\overline{\frac{E_{j,h}}{E_{J,h}}},
\qquad
E_{j,h}=\frac{p^{3j}M_{3j-1,h}}{(3j)!}.
\tag{940.20}
$$
The quotients are integral because their common normalized denominator is a unit. The exact original Hodge jets, center, absolute period and $c_0$ subtraction are retained.

Let $N_h$ be the exact finite norm of R727/R855. It is nonzero in characteristic zero; its residue is permitted to vanish. R855's full-tail formula, valid by (940.17), makes
$$
U_{m,h}=\frac{(p^mM_{m,h})^2}{N_h}
\tag{940.21}
$$
integral with precisely R925(925.34)'s residue formula. The quotient is formed before reduction and never divides by $\overline N_h$.

At the reference pair $(35,2)$, R697 gives
$$
C_{35}=3\,2^{-34}\,34!\,f_5^2
=\frac{789548077693836634073616}{5479774665990625},
\qquad C_2=-\frac12.
\tag{940.22}
$$
All the other rising-factorial, factorial and Cartier scalars in this range are units. Equation (940.6) therefore makes $U_{D,h}$ a unit and proves $M_{D,h}\ne0$. This is independent of whether the original Legendre factor has zero residue. It justifies the same characteristic-zero norm cancellation used in R925 §4.

## 5. Exact squared comparison for every coefficient

For each $m=m_j$, the two sigma identities give
$$
C_{k_1}C_{k_2}
=-3\,2^{2-p+2m}(k_1-1)!(k_2-1)!\,\Sigma_j^2,
$$
whereas the two rising factorials contribute
$$
\frac{(h-1)!(p-h)!}{(k_1-1)!(k_2-1)!}.
$$
After their cancellation, the $m$-dependent ratio is $(6B^2)^{2(m-D)}$. The actual coarse-coordinate change contributes $3/8$, and
$$
\frac38(6B^2)^3=81B^6.
$$
Consequently
$$
\boxed{
\left(\frac{q_{h,j}}{q_{h,J}}\right)^2
=\left[
\frac{(3J)!}{(3j)!}(81B^6)^{j-J}
\frac{\overline{\Sigma_j}}{\overline f_5}
\right]^2
\qquad(1\le j\le J).
}
\tag{940.23}
$$
The comparison is deliberately squared. Independent square-root signs are not asserted to be compatible with one global signed identity. Since every other scalar is a unit,
$$
q_{h,j}\ne0\quad\Longleftrightarrow\quad
\overline{\Sigma_j}\ne0.
\tag{940.24}
$$
In particular (940.23) at $j=1$ gives
$$
\bigl(\overline{f_{t+2}g_{t-3}}\bigr)^2
=u_h^2\left(\frac{Q_h'(0)}{q_{h,J}}\right)^2.
\tag{940.25}
$$
Together with the actual source (940.13), this proves (940.9)–(940.10).

The original comparison scalar has the same valuation formula as in R925:
$$
v_p(c_h^{\rm cal})
=a_h-1-\frac12v_p(N_h).
\tag{940.26}
$$
Neither $c_h^{\rm cal}$ nor $N_h$ is called a unit, and the original $a_h$ has not been discarded.

## 6. Exact fixed arithmetic and its public source

The new calculation computes only the single rational coefficient $f_5$ and its fixed R697 constants. It is not a prime scan. The script uses
$$
x''=6x^2,\quad x=z^{-2}+z^4/7+\cdots,
\qquad(\log\sigma)''=-x,\quad\sigma=z+O(z^7).
$$
Writing $t=z^6$, $x=z^{-2}X(t)$ and $\sigma^6=z^6E(t)$, the recurrences are
$$
a_0=1,\quad a_1=\frac17,\qquad
a_n=\frac{\sum_{j=1}^{n-1}a_ja_{n-j}}{(n-1)(6n+1)},
$$
$$
\log E(t)=-\sum_{n\ge1}\frac{a_n}{n(6n-1)}t^n,
\qquad f_5=[t^5]X(t)E(t).
\tag{940.27}
$$
All arithmetic is rational and truncated at the fixed degree $5$. The independent energy equation $(x'/2)^2=x^3-1$ through that degree, the previously registered $f_0,f_1,f_2$, and R697's square identity all pass. In the original integral-root convention the result is
$$
A_{35}=\frac{34!}{2^{17}}f_5
=-119077474393745219911680,
\qquad
\frac{34!}{3}C_{35}=A_{35}^2.
\tag{940.28}
$$
Both the numerator and denominator factorizations in (940.6) are complete. Their purpose here is to specify the fixed unit exceptions, not to infer a low coefficient from a finite sample.

The new arithmetic was executed only in this repository's public GitHub Actions:

- Source commit: `7843407c2633ffd5f9041a137bd9fe7174021b65`.
- [Run 44716895805](https://github.com/Rogerhu12/math-research-public/actions/runs/44716895805), job `136222480093`, success.
- Script: [weight34_sigma_top.py](../scripts/weight34_sigma_top.py).
- Arguments: `--output /tmp/weight34-sigma-top.json`.
- Deterministic output SHA256: `1fe703b1d888d361161aba47492091e45b9442357d31c1e430dda04614165a65`.

The script guards execution to the public repository Actions. Local work comprised paper derivation, IO and an AST check; no local mathematical execution was used. Reproducible JSON and coefficient arrays are not stored in Git or Releases.

## 7. What this result settles and what remains open

The original weight-34 source is identified by R937, its exact normal layer and reduction degree by R938, and its full same-label coefficient comparison by this result. The highest reference coefficient is now an explicit unit outside the already stated fixed integer $B_{34}$.

R935 proves that the two original Legendre factors at weights $10$ and $34$ are not both zero outside its own fixed bad integer. It does not prove that the corresponding sigma product or $Q'_h(0)$ is nonzero at a label where the Legendre factor is nonzero. Equation (940.9) preserves this precise common-label requirement. The remaining simultaneous-zero problem, all stated fixed exceptions, and the separate original height/rational-point comparison remain open. The main Serre-uniformity goal is not completed.

## Dependencies

R697 for the original sigma normalization, integrality and exact square roots; R705/R727 for the fixed Cartier unit and actual Hodge comparison; R855 for the complete higher-block identity; R898 for the actual $\Gamma_h$, $\mathcal Z_h$, split vector and $J_{3,2}$ formula; R925 for the whole calibrated-logarithm and norm-cancellation argument; R935/R937/R938 for this actual primitive label, its complete source and its original normal polynomial.
