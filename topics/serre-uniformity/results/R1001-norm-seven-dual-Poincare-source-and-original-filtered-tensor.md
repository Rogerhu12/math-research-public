# R1001 — A norm-seven dual Poincare product for the original filtered sigma tensor

Date: 2026-11-21 (Asia/Taipei). Session: serre-public-astra-20261120-de0a3e3b.
Authoring agent: handoff_audit. The dual-line calculation, the scalar in
Section 4, and the finite boundary were independently checked on paper by
root and literature_frontier.

**Status: proved exact source, complete finite convolution, and its first
projected pole boundary.** A specified product of two bare canonical
Kronecker kernels has cancelling Poincare classes. After a specified unit
projection and subtraction of its complete named polar summand, a specified
first-order operator gives the original two-variable tensor $F\otimes G$
with a unit factor for every $p\ge41$. Its original primitive and Legendre
filters are retained in an explicit finite convolution.

The balanced coefficient of a single bare kernel is not identified with a
coefficient of this product. The low critical extraction below uses only
kernel coefficients of total degree at most $p-6$. It does not transport
the varying balanced coefficient of total degree $2p-5$ into that band,
prove any filtered coefficient nonzero, or complete Serre uniformity.
No mathematical computation or coefficient window is executed.

## 1. The unchanged CM curve and its norm-seven sections

All functions in this note use the original model and sigma coordinate
$$
 E_-:y^2=x^3-1,\qquad dz=\omega=\frac{dx}{2y},\qquad
 x=\wp(z),\quad y=\frac{\wp'(z)}2,\quad S=\sigma(z)^6,
$$
$$
 \sigma(z)=z+O(z^7),\qquad \zeta=\frac{\sigma'}{\sigma},
 \qquad x'=2y,\quad y'=3x^2.
 \tag{1001.1}
$$
Thus $F=xS,\ G=-xyS$ are exactly the sections of
R697/R788/R966; there is no $E_+$ phase change. Put
$$
 s^2=-3,\qquad \alpha=2+s,\qquad \bar\alpha=2-s,\qquad
 \alpha\bar\alpha=7.
 \tag{1001.2}
$$
The embedding of $s$ is the original one. At this CM lattice,
$\eta_{\alpha\lambda}=\bar\alpha\eta_\lambda$.
Since $\alpha\equiv1\pmod2$, the two sigma semicharacters in
$$
 W_\alpha(z):=\frac{\sigma(\alpha z)}{\alpha\sigma(z)}
 \tag{1001.3}
$$
cancel. Its exact multiplier is the multiplier of $S$, not that multiplier
times an unspecified Gaussian.

The six nonzero points of $\ker[\alpha]$ are simple zeros of (1001.3).
The quotient $W_\alpha/S$ is an elliptic function with its only pole,
of order at most six, at $O$. It is fixed by $\mu_6$: the exact
identity $\sigma(uz)=u\sigma(z)$ holds for $u\in\mu_6$ in the fixed
zero-quadratic-parameter normalization. The class-zero part of
$H^0(E,O(6O))$ is spanned by $1,x^3$, and the constant term of
$W_\alpha$ fixes the leading $x^3$ coefficient. Consequently
$$
 \boxed{\quad
 W_\alpha=(x^3-c_\alpha)S,\qquad
 c_\alpha=-\frac{2+6s}{7},\qquad
 W_{\bar\alpha}=(x^3-c_{\bar\alpha})S,\quad
 c_{\bar\alpha}=-\frac{2-6s}{7}.
 \quad}
 \tag{1001.4}
$$
For completeness, the constant is fixed without a value fit. The original
Weierstrass equation gives
$$
 x=z^{-2}+\frac{z^4}{7}+O(z^{10}),\qquad
 \sigma=z-\frac{z^7}{210}+O(z^{13}),
$$
so $x^3S=1+\frac25z^6+O(z^{12})$. On the other hand,
$$
 W_\alpha
 =1+\frac{1-\alpha^6}{210}z^6+O(z^{12}),\qquad
 \alpha^6=-143-180s.
 \tag{1001.5}
$$
These expressions give
$c_\alpha=(\alpha^6+83)/210=-(2+6s)/7$, including its phase.
In particular
$$
 c_\alpha+c_{\bar\alpha}=-\frac47,\qquad
 c_\alpha c_{\bar\alpha}=\frac{16}{7}.
 \tag{1001.6}
$$

## 2. The genuine dual Poincare product

Use the bare canonical kernel, with no Frobenius correction inserted,
$$
 K(z,t)=\frac{\sigma(z+t)}{\sigma(z)\sigma(t)}.
 \tag{1001.7}
$$
Define the particular source
$$
 \boxed{\quad
 \mathscr P_\alpha(z,t)
 =\alpha W_\alpha(z)W_{\bar\alpha}(t)
       K(\alpha z,t)K(z,-\bar\alpha t).
 \quad}
 \tag{1001.8}
$$
The two Kronecker factors have opposite actual Poincare classes:
translation $z\mapsto z+\lambda$ multiplies them by
$e^{\bar\alpha\eta_\lambda t}$ and
$e^{-\bar\alpha\eta_\lambda t}$, respectively; translation in $t$
likewise gives the two reciprocal factors
$e^{\alpha\eta_\lambda z}$ and $e^{-\alpha\eta_\lambda z}$.
This cancellation precedes any coefficient extraction.

Cancel the actual sigma factors in (1001.8). Oddness of sigma gives the
equivalent complete expression
$$
 \boxed{\quad
 \mathscr P_\alpha(z,t)=
 -\frac{\sigma(\alpha z+t)\sigma(z-\bar\alpha t)}
          {\bar\alpha\,\sigma(z)^2\sigma(t)^2}.
 \quad}
 \tag{1001.9}
$$
No multiplication constant has been left free. For example, the
normalizing factor is $\alpha/(\alpha\bar\alpha)$, and
$\sigma(-\bar\alpha t)=-\sigma(\bar\alpha t)$ supplies exactly
the displayed minus sign.

This is a meromorphic section of the genuine
$L_6\boxtimes L_6$, $L_6=O(6O)$, with poles of order at most two
on each origin axis and no other poles. Here is a direct multiplier check.
For translation in $z$, the two numerator multipliers have exponent
$$
 \bar\alpha\eta_\lambda
    \left(\alpha z+t+\frac{\alpha\lambda}{2}\right)
 +\eta_\lambda\left(z-\bar\alpha t+\frac{\lambda}{2}\right)
 =8\eta_\lambda(z+\lambda/2).
 \tag{1001.10}
$$
Their signs cancel because $\alpha\equiv1\pmod2$.
The denominator removes $2\eta_\lambda(z+\lambda/2)$.
The resulting exponent is exactly $6\eta_\lambda(z+\lambda/2)$.
The same calculation in $t$ uses $-\bar\alpha\equiv1\pmod2$
and gives the other $L_6$ multiplier.
Equivalently, the numerator's CM matrix
$$
 M=\begin{pmatrix}\alpha&1\\1&-\bar\alpha\end{pmatrix},
 \qquad M^\dagger M=8I
 \tag{1001.11}
$$
has its two diagonal degrees lowered by two by the specified denominator.
The exact calculation (1001.10) also checks the theta signs that the
Hermitian degree calculation alone would not determine.

In particular, this construction is not the product of two arbitrary
sections of the same weight. It is a named multiplication of mutually
dual bare Poincare sections, with its axes and normalizations fixed.

## 3. Complete projection and its named polar summand

Let
$$
 \Pi_a^z U(z,t)=\frac16\sum_{u\in\mu_6}u^{-a}U(uz,t),
 \qquad
 \Pi_b^t U(z,t)=\frac16\sum_{u\in\mu_6}u^{-b}U(z,ut).
 \tag{1001.12}
$$
For a meromorphic $L_6$ section with an origin pole of order at most
two, divide by $S$. The resulting function belongs to
$H^0(E,O(8O))$, whose actual basis is
$$
 1,\ x,\ y,\ x^2,\ xy,\ x^3,\ x^2y,\ x^4.
 \tag{1001.13}
$$
Its class-four subspace is $\langle x,x^4\rangle$, and its
class-zero subspace is $\langle1,x^3\rangle$. Thus the entire
$\Pi_4^z\Pi_0^t$ projection lies in
$$
 \langle x^4S,F\rangle_z\otimes\langle x^3S,S\rangle_t.
 \tag{1001.14}
$$
This lists the complete space, including the origin pole.

Put $V=x^4S$. In the original $z$-coordinate the coefficient of
$z^{-2}$ in (1001.8) is exactly $W_{\bar\alpha}(t)$:
the factors $\alpha$, $(\alpha z)^{-1}$, and $z^{-1}$ cancel
their scalars, and $W_\alpha(0)=1$.
Since $V=z^{-2}+O(z^4)$, there exist uniquely specified constants
$A_\alpha,C_\alpha\in\mathbf Q(s)$ such that
$$
 \boxed{\quad
 \Pi_4^z\Pi_0^t\mathscr P_\alpha
 =V(z)W_{\bar\alpha}(t)
   +F(z)(A_\alpha x(t)^3+C_\alpha)S(t).
 \quad}
 \tag{1001.15}
$$
The first summand is the full polar summand, not only its Laurent
principal term $z^{-2}W_{\bar\alpha}(t)$.

The otherwise unused constant can, for example, be defined completely by
$$
 C_\alpha=[z^4t^6]\mathscr P_\alpha
 -\frac{19}{35}\left(\frac25-c_{\bar\alpha}\right)
 -\frac25 A_\alpha.
 \tag{1001.16}
$$
Indeed $V=z^{-2}+\frac{19}{35}z^4+\cdots$ and
$[t^6]x^3S=2/5$. Thus (1001.15) has no choice of an unnamed source;
its specified first-order image below simply kills this fixed constant.

## 4. Exact scalar and the original two-variable tensor

The coefficient of $t^0$ in the unprojected source determines
$A_\alpha$ directly. Set $r=x^3-c_\alpha$ and
$$
 \Phi(z)=\zeta(\alpha z)-\bar\alpha\zeta(z)
        =\frac{r'(z)}{\alpha r(z)}.
 \tag{1001.17}
$$
The last identity follows by differentiating
$W_\alpha=rS=\sigma(\alpha z)/(\alpha\sigma(z))$;
the two $6\zeta$ terms cancel because $\alpha\bar\alpha-1=6$.
Differentiating it also gives the exact isogeny formula
$$
 x(\alpha z)=\frac{\bar\alpha}{\alpha}x(z)
             -\frac{\Phi'(z)}{\alpha}.
 \tag{1001.18}
$$

The local expansion
$$
 K(v,t)=t^{-1}+\zeta(v)
       +\frac{\zeta(v)^2-x(v)}2\,t+O(t^2)
 \tag{1001.19}
$$
and $W_{\bar\alpha}(t)=1+O(t^6)$ show
$$
 [t^0]\mathscr P_\alpha
 =-\frac{\alpha W_\alpha}{2\bar\alpha}
       \{\Phi^2-x(\alpha z)-\bar\alpha^2x\}
 =S\left(4xr-\frac{r''}{14}\right).
 \tag{1001.20}
$$
The Weierstrass equations in (1001.1) give
$$
 r''=(x^3)''=42x^4-24x.
 \tag{1001.21}
$$
Consequently
$$
 [t^0]\mathscr P_\alpha
 =\{x^4+(12/7-4c_\alpha)x\}S.
 \tag{1001.22}
$$
This already has class four in $z$; its $t^0$ coefficient is fixed
by $\Pi_0^t$. Comparing (1001.15) gives
$$
 \boxed{\quad
 A_\alpha=\frac{12}{7}-4c_\alpha
          =\frac{4(5+6s)}7,\qquad
 N_{\mathbf Q(s)/\mathbf Q}(A_\alpha)=\frac{16\cdot19}{7}.
 \quad}
 \tag{1001.23}
$$
In particular $A_\alpha$ is a unit at every $p\ge41$.
This conclusion uses its explicit original scalar, not a rescaling of
the source.

Subtract the full summand fixed in Section 3:
$$
 \mathscr Q_\alpha
 :=\Pi_4^z\Pi_0^t\mathscr P_\alpha-V(z)W_{\bar\alpha}(t).
 \tag{1001.24}
$$
Use the named meromorphic operator
$$
 \mathcal L_t=\frac1{x(t)}\bigl(\partial_t-6\zeta(t)\bigr).
 \tag{1001.25}
$$
On the complete class-zero space its action is
$$
 \mathcal L_t S=0,\qquad
 \mathcal L_t(x^3S)=6xyS=-6G.
 \tag{1001.26}
$$
The apparent divisor $x(t)=0$ cancels in these displayed images;
there is no additional pole or deleted point. Thus (1001.15) proves
the actual two-variable identity
$$
 \boxed{\quad
 \mathcal L_t\mathscr Q_\alpha(z,t)
       =-6A_\alpha F(z)G(t).
 \quad}
 \tag{1001.27}
$$
In particular the output is holomorphic on both axes and globally.
Comparison with the actual conductor-$(2s)$ source of R966 is also
fully specified:
$$
 \mathcal L_t\mathscr Q_\alpha
 =\frac{A_\alpha}{12}\,
   \Pi_4^z(\partial_t-6\zeta(t))^2\mathscr K_0(z,t).
 \tag{1001.28}
$$
This equality concerns the two indicated complete images. It does not
identify the unprojected bare product with R966's entire epsilon vector.

## 5. The complete finite convolution in the original critical band

Fix $p=6N+5\ge41$. Work over the localization of
$\mathbf Z[s,1/7]$ at $p$, and subsequently reduce into
$\mathbf F_{p^2}$. Keep
$$
 F=z^4\sum_{i\ge0}f_i z^{6i},\qquad
 G=t\sum_{j\ge0}g_j t^{6j}.
 \tag{1001.29}
$$
Write the following original one-variable coefficients, without changing
the coordinate:
$$
 \frac1{x(t)}=t^2\sum_{\nu\ge0}a_\nu t^{6\nu},
 \qquad
 \frac{\zeta(t)}{x(t)}=t\sum_{\nu\ge0}b_\nu t^{6\nu},
 \qquad a_0=b_0=1,
 \tag{1001.30}
$$
$$
 w_r=[z^{6r}]W_\alpha,\quad
 \bar w_r=[t^{6r}]W_{\bar\alpha},\quad
 v_i=[z^{6i+4}]V,\quad
 P_{a,b}=[z^at^b]\mathscr P_\alpha.
 \tag{1001.31}
$$
For every $i,j\ge0$ with $i+j=N-1$, coefficient extraction in
(1001.27) gives the complete, triangular formula
$$
 \boxed{\quad
 -6A_\alpha f_i g_j
 =\sum_{m=0}^{j}
    \bigl(6m\,a_{j-m}-6b_{j-m}\bigr)
       \left(P_{6i+4,\,6m}-v_i\bar w_m\right).
 \quad}
 \tag{1001.32}
$$
Both terms in the parentheses are part of the original source. In
particular the polar summand has not been silently discarded.
The term $m=0$ is present, with coefficient $-6b_j$.

Here is a full expression for each $P_{a,6m}$ as a convolution of
the bare kernel. Define its Laurent index set and coefficients by
$$
 \mathcal I=\{(-1,0),(0,-1)\}\cup\mathbf Z_{\ge0}^2,\qquad
 k_{u,v}=[z^ut^v]K(z,t),\qquad
 k_{-1,0}=k_{0,-1}=1.
 \tag{1001.33}
$$
Zero coefficients remain zero in this definition. For $a=6i+4$,
(1001.8) gives
$$
 \boxed{\quad
 P_{a,6m}
 =\alpha\sum_{r=0}^{i+1}\sum_{d=0}^{m}w_r\bar w_d
   \sum_{\substack{(u,v),(u',v')\in\mathcal I\\
                   u+u'=a-6r\\v+v'=6m-6d}}
       \alpha^u(-\bar\alpha)^{v'}k_{u,v}k_{u',v'}.
 \quad}
 \tag{1001.34}
$$
All sums are finite. The outer endpoint $r=i+1$ permits the two
$z^{-1}$ poles and is necessary: it is not omitted on the grounds
that the final output is holomorphic. The sign
$(-\bar\alpha)^{v'}$, including its value at $v'=-1$, is the
one in the actual second kernel.

### 5.1 Integrality and exact required range

The output exponent in $t$ is $6j+1$. Each term of
$\mathcal L_t$ raises an input exponent by $1+6e$, with $e\ge0$.
It therefore uses exactly the input exponents $6m$, $0\le m\le j$,
listed in (1001.32). In particular
$$
 (6i+4)+6m\le p-7,\qquad
 6i+4\le p-7,\qquad 6m\le p-11.
 \tag{1001.35}
$$
In (1001.34) the other kernel has total degree at least $-1$.
Thus every single kernel coefficient that occurs has total degree at
most $p-6$. Computing it from the sigma quotient uses sigma
coefficients of degree at most $p-4$, strictly before the first
$p$-denominator. The coefficients $w_r,\bar w_d$ use
$r\le i+1\le N$ and $d\le N-1$, also within the original
first-$p$ integral range. The coefficients of $1/x$ and
$\zeta/x$ in (1001.32) are below their first possible nonintegral
degrees as well. These assertions also follow directly from the
finite original $u=x^{-1/2}$ expressions of R702/R760.

Hence every displayed summand in (1001.32)–(1001.34) is individually
$p$-integral in the stated critical range. This is a legitimate
finite reduction, not a reduction of an infinite rational sigma
series or an exchange of reduction with a pole.

### 5.2 Both original filters remain on their original labels

For the application impose $p\equiv2,5\pmod9$ and write
$$
 h_i=6i+7,\qquad
 \omega_i=\mathbf 1_{\gcd(h_i,p+1)=1}
             P_{h_i-1}(1/s),\qquad j=N-1-i,
 \tag{1001.36}
$$
where the $P_d$ in this formula are the original Legendre polynomials,
not the source coefficient $P_{a,b}$.
The original filtered critical polynomial is therefore exactly
$$
 \boxed{\begin{aligned}
 \sum_{i=0}^{N-1}\omega_i f_i g_{N-1-i}X^{6i+4}
 =-\frac1{6A_\alpha}
  \sum_{i=0}^{N-1}\omega_i X^{6i+4}
   \sum_{m=0}^{N-1-i}
    \bigl(6m\,a_{N-1-i-m}-6b_{N-1-i-m}\bigr)
    \left(P_{6i+4,6m}-v_i\bar w_m\right).
 \end{aligned}}
 \tag{1001.37}
$$
This is the unchanged nonendpoint critical range of R788/R966/R968.
Every primitive and Legendre weight remains attached to its original
column. No total contraction is substituted for simultaneous labelled
nonvanishing, and the separate endpoint $h=1$ is not inserted here.

## 6. The exact first projected pole boundary

There is a genuine boundary if one asks for the entire first-$p$
rectangle of $\Pi_4^z\Pi_0^t\mathscr P_\alpha$ before subtracting
the summand in (1001.24). Keep the original R702/R788 unit
$$
 B=(-1)^{N+1}\binom{3N+2}{2N+1},\qquad \kappa=6B.
 \tag{1001.38}
$$
R702 proves, in an explicitly integral finite truncation,
$$
 pF\equiv-\kappa z^{p+1}F_0\pmod{p,z^{2p}},
 \tag{1001.39}
$$
where $F_0=z^4+\cdots$ is integral. Its inverse coordinate $u(z)$
is integral throughout the required range. Since $x^3=u^{-6}$,
one may multiply (1001.39) by this integral Laurent series and obtain
$$
 pV\equiv-\kappa z^{p+1}x^3F_0
          \pmod{p,z^{2p-6}},\qquad
 x^3F_0=z^{-2}+O(z^4).
 \tag{1001.40}
$$
The original one-pole argument bounds all retained denominators by a
single factor of $p$. Therefore among the coefficients
$-2\le a<p$ of $V$ the sole nonintegral coefficient is the
one at $a=p-1$, with exact residue
$$
 \boxed{\quad p[z^{p-1}]V\equiv-\kappa=-6B\pmod p.\quad}
 \tag{1001.41}
$$

The first-$p$ coefficients of $W_{\bar\alpha}$, $F$, $S$,
and $x^3S$ are integral by the original six-section results.
The fixed constant $C_\alpha$ is integral at every $p\ge41$:
its definition (1001.16) only needs the fixed expansions
$$
 \sigma=z-\frac{z^7}{210}-\frac{z^{13}}{1801800}
          +O(z^{19})
 \tag{1001.42}
$$
and their reciprocal products. Their denominators have prime factors
at most $13$; the additional CM denominators are powers of $7$.
No uncomputed high coefficient or unknown period is used to infer
this integrality.

It follows from the complete decomposition (1001.15) that in the
finite Laurent rectangle $-2\le a<p,\ 0\le b<p$,
$$
 \boxed{\quad
 p\,\Pi_4^z\Pi_0^t\mathscr P_\alpha
 \equiv-\kappa z^{p-1}W_{\bar\alpha,<p}(t)\pmod p.
 \quad}
 \tag{1001.43}
$$
This statement means the coefficientwise congruence after multiplying
by $p$, when every coefficient is integral. It does not reduce the
unsubtracted source itself. Subtracting the entire $V\otimes
W_{\bar\alpha}$ cancels this boundary exactly and gives the
integral rectangle of $\mathscr Q_\alpha$.

The critical extraction in Section 5 has $a\le p-7$, and its
operator acts only in $t$. Thus this $z^{p-1}$ boundary cannot
enter that extraction. It is distinct from the degree-$p+1$
cross correction in R788 and does not remove that correction from
any high-band comparison.

## 7. The related single trace and the precise remaining gap

To distinguish the new product from a single balanced coefficient,
one can retain the actual first-variable norm-seven trace difference
$$
 \mathscr A_\alpha(z,w)
 =\alpha K(\alpha z,w/\bar\alpha)
  -\bar\alpha K(\bar\alpha z,w/\alpha).
 \tag{1001.44}
$$
It is regular at the origin axes: the $1/z$ terms and the $7/w$
terms cancel separately. Its zero column is exactly
$$
 \mathscr A_\alpha(z,0)
 =\alpha\zeta(\alpha z)-\bar\alpha\zeta(\bar\alpha z)
 =D\log(W_\alpha/W_{\bar\alpha}).
 \tag{1001.45}
$$
With $\delta=c_\alpha-c_{\bar\alpha}=-12s/7$, the actual
Wronskian is
$$
 W_{\bar\alpha}W_\alpha'-W_\alpha W_{\bar\alpha}'
 =-6\delta FG.
 \tag{1001.46}
$$
Consequently $W_\alpha W_{\bar\alpha}\mathscr A_\alpha(z,0)
=-6\delta FG$. This is a diagonal identity and is not (1001.27).

For $c_n^-=[z^nw^{n-1}]K(z,w)$, the *unmultiplied* trace has
the exact balanced coefficient
$$
 [z^nw^{n-1}]\mathscr A_\alpha
 =7\left\{(\alpha/\bar\alpha)^n
          -(\bar\alpha/\alpha)^n\right\}c_n^-.
 \tag{1001.47}
$$
For the original $n=p-r,\ r=2,8$, this prefactor is a unit at
every original $p\ge41$. Indeed $\alpha^p=\bar\alpha$, so it reduces
using $a=r+1=3,9$ to a unit times
$\alpha^{2a}-\bar\alpha^{2a}$. The exact fixed values are
$$
 \alpha^3-\bar\alpha^3=18s,\quad
 \alpha^3+\bar\alpha^3=-20,
$$
$$
 \alpha^9-\bar\alpha^9=1026s,\quad
 \alpha^9+\bar\alpha^9=12580.
 \tag{1001.48}
$$
Their numerator prime divisors are among $2,3,5,7,17,19,37$.
The only denominators here are powers of $7$.

Multiplying (1001.44) by $W_\alpha W_{\bar\alpha}$, however,
introduces every appropriate $z$-convolution. Its balanced
coefficient is generally not (1001.47). Likewise (1001.8) is a
product of two bare kernels with the complete convolution
(1001.34); the unit in (1001.23) does not identify that convolution
with the single coefficient $c_n^-$.

The line-bundle distinction is concrete. After $w=7t$,
(1001.44) has Poincare class $7$. Clearing its actual nonzero
kernel poles in both variables with
$W_\alpha W_{\bar\alpha}$ gives Hermitian degree matrix
$\left(\begin{smallmatrix}12&7\\7&12\end{smallmatrix}\right)$,
not the external degree-six product used in Section 2.
The opposite factors in (1001.8), not a Gaussian silently chosen
afterwards, are what cancel the cross class.

Thus the new conclusions are the genuine external-product source,
its exact original tensor image, its complete mask-preserving low
convolution, and its displayed projected first pole boundary. In the
$r=2$ row the desired bare balanced total degree $2p-5$ is still
$p+1$ above the original critical output $p-6$. The corresponding
high-band comparison must retain the first-pole carry and all endpoint
terms; it is not proved here. The $r=8$ gap is different and is not
silently replaced by the $r=2$ argument.

## Dependencies

- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md)
  and [R702](R702-first-pole-block-and-uniform-shifted-units.md):
  the original sigma sections, finite coordinate, and exact first pole.
- [R760](R760-original-critical-sigma-jets-from-four-digit-division-data.md):
  first-$p$ integrality and the original labelled coefficients.
- [R784](R784-original-full-sigma-kernel-and-primitive-preserving-left-inverse.md)
  and [R788](R788-original-cross-p-Cartier-correction-and-rank-six-coupling.md):
  the already established six-rank addition kernel and its cross-$p$
  correction, which are not re-proved or removed here.
- [R966](R966-single-conductor-two-s-CM-kernel-and-original-critical-jet.md)
  and [R968](R968-full-level-mixed-CM-jet-and-critical-factor.md):
  the actual conductor-$(2s)$ source and the original filtered critical
  tensor.
- [R975](R975-original-balanced-Kronecker-integral-heat-recurrence.md),
  [R984](R984-frobenius-regularized-finite-Kronecker-kernel-and-rational-Cartier-descent.md),
  and [R988](R988-original-pure-balanced-Cartier-contraction-and-high-trace.md):
  the unchanged bare Kronecker normalization and the distinction between
  its balanced coefficient and a full product of kernels.

## Full review

The entire frozen proof, including both semicharacters, the complete projected section space, both pole endpoints in the convolution, every finite precision bound, and the exact first boundary, was independently reviewed on paper by root and literature_frontier. The constants in the named operator were derived from the actual sigma source. No new numerical arithmetic, coefficient window, or mathematical execution was used.
