# R683 — The even-weight Cartier channel and the actual $r_3$

**Status: proved, with the precise scope below.** The complete six-torsion
normalization and the rational Cartier comparison extend from the previously
stated weights $k\equiv5\pmod6$ to every $k\equiv2\pmod3$. The even member
$k=p-3$ therefore computes the second coefficient in the actual R605 criterion.
No nonvanishing assertion for all primes is made.

## 1. Statement in the original normalization

Let $p\ge41$ be prime with $p\equiv5\pmod6$. Retain exactly the curve,
differential, tame labels, and original kernel of R615/R658:

$$
 E_0:y^2=x^3-1,\qquad\omega=\frac{dx}{2y}=dz,\qquad\alpha^3=4,
 \qquad\beta^2=3,
$$
$$
 Q_{\delta ij}=(\alpha\zeta^i,\delta\beta)+(\zeta^j,0),
 \qquad\chi(Q_{\delta ij})=\delta\zeta^{j-i},
$$
$$
 R_-=\frac{x^2(x^6+34x^3-8)}{x^9-228x^6+48x^3-64},
 \qquad C_+=\frac{144\beta}{\alpha^2}.
 \tag{683.1}
$$

The chosen $p$-adic reduction of $\alpha$ is the unique cube root of $4$
in $\mathbf F_p$. Put

$$
 B=(-1)^{(p-1)/2-(p-2)/3}
       \binom{(p-1)/2}{(p-2)/3},
 \qquad c=\frac{(3/p)\alpha^2}{2}\in\mathbf F_p^\times.
 \tag{683.2}
$$

Write $\Lambda=\Omega\mathcal O_{\mathbf Q(\zeta)}$ for the same complex
period lattice as R615, with $\Omega>0$, and
$\mathcal A=\operatorname{covol}(\Lambda)/\pi$. Define the completed
Kronecker sum

$$
 H^+(z,w)=\sum_Q\chi(Q)
 \frac{\sigma(z+Q+w)}{\sigma(z+Q)\sigma(w)}
                 \exp(-\overline Qw/\mathcal A).
 \tag{683.3}
$$

For **every** integer $k\ge2$ with $k\equiv2\pmod3$, set $m=k-1$ and

$$
 C_k=(-3)^m m!\,[z^mw^m]H^+(z,w)/C_+.
 \tag{683.4}
$$

For the old odd weights this is literally R615's definition. For even
weights $k\equiv2\pmod6$, it extends the same sum and the same scalars;
there is no change of tame character or global quotient.

The conclusions are:

1. $C_k\in\mathbf Q$, and the finite rational recurrence of R615,
   including its full inverse-sigma factor, computes it for all these
   weights.
2. The fixed-conductor Hecke character
   $$
   \xi_k((\nu))=\chi(\nu)^{-1}\nu^{2k-1},\qquad(\nu,6)=1,
   $$
   is well-defined, and its normalization remains
   $$
   L(\xi_k,k)=
       \frac{\alpha\beta\Omega\mathcal A^{k-1}}{(-3)^{k-1}}C_k.
   \tag{683.5}
   $$
3. If $2\le k\le p$ and $k\equiv2\pmod3$, then $C_k$ is $p$-integral
   and
   $$
   [z^{(p-1)k}]R_-
       \equiv c(-3B)^{-(k-1)}C_k\pmod p.
   \tag{683.6}
   $$
4. In particular, the original coefficient
   $$
   r_3=[z^{(p-1)(p-3)}]R_-
   $$
   satisfies
   $$
   \boxed{r_3\equiv-27cB^3 C_{p-3}\pmod p.}
   \tag{683.7}
   $$
   Combining with R658's $r_2=cC_p$ gives
   $$
   \boxed{v_p(M_2)=-1
       \quad\Longleftrightarrow\quad C_p C_{p-3}\not\equiv0\pmod p.}
   \tag{683.8}
   $$

The field of $M_2$, its actual CM norm pairing, and the residue-field
meaning of its squared congruence remain exactly those of R588/R595.

## 2. Why even weights give the same rational trace

We spell out the parity point, because the earlier statement imposed
$k\equiv5\pmod6$. Set $r=\alpha\zeta^{i-j}$ and use $\xi=\beta z$.
For $\delta=1,j=0$, the rational initial conditions are

$$
 x(0)=r^2+r+2,\quad
 Y(0)=-r^2-2r-3,\quad
 e(0)=\frac{r^2+2r+2}{6},\quad s(0)=1,
$$
$$
 x'=2Y,\qquad Y'=x^2,\qquad e'=-x/3,\qquad s'=es,
 \qquad r^3=4.
 \tag{683.9}
$$

Primes denote $d/d\xi$. Thus every Taylor coefficient belongs to
$\mathbf Q[r]/(r^3-4)$, for odd and even $m$ alike. Let
$\widetilde\sigma(\eta)=\beta\sigma(\eta/\beta)$ and write

$$
 c_m(r)=[\xi^m\eta^m]
          \frac{s(\xi+\eta)}{s(\xi)\widetilde\sigma(\eta)}.
 \tag{683.10}
$$

Negating the tame point changes a diagonal coefficient of total
homogeneity $2m+1$ by $(-1)^{2m+1}=-1$. Its character also changes
sign, so the two $\delta$ terms add for **every** $m$. Rotating the point
by $\zeta^j$ changes the coefficient by $\zeta^{-j(2m+1)}$.
Since $k\equiv2\pmod3$,

$$
 2m+1=2k-1\equiv0\pmod3,
$$

so this factor is one. The character is unchanged under simultaneous
rotation of the two tame coordinates. The three $j$ terms therefore add.
For $j=0,\delta=1$, the character is $\alpha/r$. Keeping the physical
coefficient conversion $\beta^{2m+1}=\beta3^m$ gives

$$
 [z^mw^m]H^+
   =6\alpha\beta3^m\operatorname{Tr}_{\mathbf Q[r]/\mathbf Q}(c_m/r).
$$

Since $\alpha^3=4$ and $C_+=144\beta/\alpha^2$, this is

$$
 \frac{[z^mw^m]H^+}{C_+}
   =\frac{3^m}{6}\operatorname{Tr}(c_m/r).
 \tag{683.11}
$$

If $c_m=c_{m,0}+c_{m,1}r+c_{m,2}r^2$, then
$\operatorname{Tr}(c_m/r)=3c_{m,1}$. Therefore

$$
 \boxed{C_k=\frac{(-1)^m3^{2m}m!}{2}\,c_{m,1}.}
 \tag{683.12}
$$

This proves rationality and the unchanged exact recurrence. Unlike some
odd-weight examples, the **individual** $c_m$ at even weights need not
be proportional to $r$: at $k=2$, $c_1=(1+r)/9$. Formula (683.11), not
an assertion that its constant part vanishes, removes that part.

For completeness, the finite recurrence is the coefficient form of
(683.9), followed by inversion of $s$. If
$\eta/\widetilde\sigma(\eta)=\sum_{h\ge0}u_h\eta^{6h}$ and
$b_j=[\xi^j]s(\xi)^{-1}$, then

$$
 c_m=\sum_{j=0}^m b_j
       \sum_{\substack{h\ge0\\2m+1-j-6h\ge m-j}}
        u_hs_{2m+1-j-6h}
                \binom{2m+1-j-6h}{m-j}.
 \tag{683.13}
$$

Here $u_h$ is computed from the same unshifted sigma series as R615:
$a_1=1/189$,

$$
 a_n=\frac{\sum_{i=1}^{n-1}a_i a_{n-i}}{(n-1)(6n+1)},\qquad
 \sum_{h\ge0}u_h\eta^{6h}
   =\exp\!\left(\sum_{n\ge1}
           \frac{a_n\eta^{6n}}{6n(6n-1)}\right).
$$

Thus every inverse-sigma block in the required degree is retained.

## 3. The exact fixed-conductor $L$-value

On a unit $u\in\mu_6$, $\chi(u)=u^3$. The equality
$2k-1\equiv3\pmod6$ holds for every $k\equiv2\pmod3$, not only the
odd weights. It proves that the formula for $\xi_k$ is independent of
a generator of the principal ideal. Since $\mathcal O_{\mathbf Q(\zeta)}$
has class number one, the same ideal sum as in R615 gives

$$
 L(\xi_k,k)=\frac16\sum_{(\nu,6)=1}
                    \chi(\nu)\frac{\overline\nu^{k-1}}{\nu^k}.
 \tag{683.14}
$$

As usual at this point, insert $|\nu|^{-2t}$ where the sum converges
absolutely, group the terms there, and then continue to $t=0$.
Grouping the eighteen invertible classes modulo $6$, with
$Q_a=\Omega a/6$, gives

$$
 L(\xi_k,k)=\frac{\Omega}{36}
           \sum_a\chi(a)e^*_{m,m+1}(Q_a,0).
 \tag{683.15}
$$

Bannai–Kobayashi, *Algebraic theta functions and the p-adic interpolation
of Eisenstein–Kronecker numbers*, Theorem 1.17 (2007 preprint), gives

$$
 [z^mw^m]\Theta_{Q_a}(z,w)
             =\frac{e^*_{m,m+1}(Q_a,0)}{m!\mathcal A^m}.
 \tag{683.16}
$$

The general sign is $(-1)^{a+b-1}$, here $(-1)^{2m}=1$ for both
parities of $m$. This is precisely where no new negative sign may be
inserted for even $k$. Equations (683.15)–(683.16), (683.4), and
$C_+/36=\alpha\beta$ prove (683.5).

Primary source checked in this continuation:
https://arxiv.org/pdf/math/0610163, Theorem 1.17; its introduction also
states the same formula on printed page 4. We use only the complex
Kronecker identity, not an ordinary-prime interpolation result at these
supersingular primes.

## 4. The Cartier proof already covers every needed parity

Here we check all uses of the weight in R658; the claimed extension does
not infer equality of rational functions from finite residues alone.
In R658, the rational connection functions are

$$
 \sum_{a\ge0}L_aw^a=C_+^{-1}e^{-\mathcal E(z)w}H^+(z,w),
 \qquad\mathcal E=\zeta_\Lambda.
$$

Let $q=-B^{-1}D^{p-2}x$. The proved rational identity R658(658.37) is

$$
 \mathcal C(q^aR_-\omega)=cB^{-a}a!L_a\omega
                  \qquad(0\le a\le p-1).
 \tag{683.17}
$$

Crucially, its range includes **all** $a$, odd as well as even.
The proof uses the genuine completed-zeta multiplication correction and
$N=4p-1$, not a parity assumption on the final weight. If $h_a\omega$
is the difference after matching finite residues, it has no pole away
from $O$ and

$$
 h_a(-P)=(-1)^ah_a(P),\qquad
 \operatorname{Tr}_{[N]}(h_a\omega)=N^{-a}h_a\omega.
$$

A pole of order $d$ would have $d\equiv a\pmod2$, but its trace leading
coefficient is multiplied by $N^{d-1}=(-1)^{a-1}$ instead of the
required $N^{-a}=(-1)^a$. This is impossible. If $h_a$ is constant,
odd $a$ kills it by parity and even $a$ kills it by the trace of $\omega$.
Thus the possible full holomorphic or polar correction at $O$ has
already been removed for the odd index $a=p-4$ needed here as well.

The rational $L_a$ are integral for all $a\le p-1$ by R658 Section 2.
At $a=p-1$ the sole $p!$ denominator is canceled before reduction; for
the new even endpoint $a=p-4$ that complication does not arise.

The exact integral parameter comparison in R594/R658 is

$$
 z_*=q+B^{-1}\overline E_{\mathrm{low}}^{,p},\qquad dz_*=\omega,
 \qquad z_*\equiv z\pmod{(p,u^{p^2})}.
 \tag{683.18}
$$

For $m=k-1\le p-1$, Cartier coefficient extraction and (683.17) give

$$
\begin{aligned}
 [z^{(p-1)k}]R_-{}^{1/p}
  &= [z_*^m]\frac{\mathcal C(z_*^mR_-\omega)}{\omega}\\
  &=cB^{-m}m![z_*^m]
      \sum_{a=0}^m\frac{\overline E_{\mathrm{low}}^{,m-a}}{(m-a)!}L_a.
\end{aligned}
 \tag{683.19}
$$

All factorials displayed here are units. The combined regular expression
in the last line is the $w^m$ coefficient of

$$
 C_+^{-1}e^{(E_{\mathrm{low}}-\mathcal E)w}H^+.
$$

Since $H^+$ is regular at $z=0$ and
$E_{\mathrm{low}}-\mathcal E=O(z^p)$, its $z^mw^m$ coefficient equals
$[z^mw^m]H^+/C_+$ for $m<p$. One discards this tail only after forming
the combined regular expression; individual $L_a$ can have poles.
This also proves integrality of the required diagonal. The degree
$(p-1)k\le p(p-1)<p^2$ stays inside (683.18)'s integral range.
No part of this argument uses $m$ even or $k\equiv5\pmod6$.

Both the kernel coefficient and $C_k$ are rational, so their reductions
are fixed by Frobenius. Substitution of (683.4) into (683.19) gives
(683.6) and proves its stated integrality.

## 5. Substitution into the actual $c_1$ norm formula

Take $k=p-3$ and $m=p-4$. Since $(-3B)^{p-1}=1$ in $\mathbf F_p^\times$,

$$
 (-3B)^{-(p-4)}=(-3B)^3=-27B^3,
$$

which proves (683.7) with its negative sign. The original R605 identities
then become

$$
\boxed{
\begin{aligned}
 r_2r_3&\equiv-27c^2B^3 C_pC_{p-3},\\
 p^2S_2S_3&\equiv-4374\alpha^2B^8C_pC_{p-3},\\
 (pM_2)^2&\equiv-34992\zeta^2\alpha^2B^8C_pC_{p-3}
 \pmod p.
\end{aligned}}
 \tag{683.20}
$$

Here $c^2=\alpha^4/4$ and $\alpha^3=4$ have been retained in the
normalization. The constants $4374=2\cdot3^7$ and
$34992=16\cdot3^7$ are units for every $p\ge41$. Thus the valuation
criterion is exactly (683.8). If either factor vanishes, the currently
proved safe bound remains $v_p(M_2)\ge-1/2$; the calculation does not
establish a stronger valuation or a rational-point obstruction by itself.

## 6. Small exact normalization checks

The unchanged finite recurrence, with its admissible weight guard
extended to $k\ge2$, $k\equiv2\pmod3$, gives

$$
 C_2=-\frac12,\qquad C_8=-\frac{81}{70},
$$
$$
 C_{38}=-\frac{80610429419568430846701796986264}
                  {248150801182058884484375},
$$
$$
 C_{44}=-\frac{95254824577121524958029374842277356564172}
                  {3782099861173919036375764765625}.
$$

The two targeted comparisons with the already published R595 $r_3$
values are:

| $p$ | $C_{p-3}\bmod p$ | $-27cB^3\bmod p$ | product | original $r_3$ |
|---:|---:|---:|---:|---:|
| 41 | 35 | 23 | 26 | 26 |
| 47 | 26 | 8 | 20 | 20 |

The new calculations retain exact rational coefficients and every
inverse-sigma block. They did not repeat a wild-torsion orbit, compute a
prime grid, or substitute an empirical equality for (683.17)–(683.19).
The parity argument proves the extension for every prime in scope.

## 7. What this leaves open

The two previously differently presented local quantities now lie in
one fixed tame-character Hecke family at the adjacent admissible
weights $p$ and $p-3$. The actual remaining local question is

$$
 C_pC_{p-3}\not\equiv0\pmod p
       \quad\text{for the remaining primes }p\equiv2,5\pmod9,
$$

or a precise description and treatment of exceptions. Neither the
nonzero complex value in (683.5) nor $p$-integrality proves this. The
$c_0$ coefficient $r'_p$ is separate, and the actual global rank or
quadratic-height conditions are also separate. This result gives no
absolute Serre constant and no unbounded counterexample family.
