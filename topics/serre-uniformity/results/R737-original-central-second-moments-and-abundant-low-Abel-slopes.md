# R737 — Original central second moments and many bounded Abel valuations

Date: 2026-11-14. **Status: proved.** We keep the full original
weight-five and weight-seven central-value formulas and prove a
logarithmic second-moment bound over the complete odd family. The
primitive geometric mean consequently costs only powers of logarithms
in addition to the original period factor $p^2$.

Together with the original toric-norm average, this gives
$2v_p(M_{2,h})\le3$ for at least one actual primitive label at every
sufficiently large allowed prime. For still larger primes, more than
one eighteenth of the primitive labels satisfy that inequality.
These are labelled coefficient embeddings; no independence or distinctness
beyond the original family is inferred from the count.

The whole-series consequence is the already justified depth-eight
Abel isometry. A half-integral valuation is not silently rounded as an
integer, so this argument alone does not give depth seven or the
original depth-four candidate disc.

## 1. Original objects and statements

Use R717/R729/R730/R733 with
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
n=p+1,\quad m=n/6,\quad g=\varphi(n)/2,
$$
$$
\mathcal H=\{h\bmod n:h\equiv1\pmod6\},\qquad
\mathcal H^*=\{h\in\mathcal H:(h,n)=1\},\qquad
F_0=\mathbb Q(\zeta_n)^+.
\tag{737.1}
$$
The original central values, including the conductor-six character, are
$$
L_{2,h}=L(\xi_{5,h},3),\qquad
L_{3,h}=L(\xi_{7,h},4),
$$
$$
\xi_{5,h}((a))=a^5\chi_6(a)\theta(a)^{-h},\qquad
\xi_{7,h}((a))=a^7\chi_6(a)\theta(a)^h.
\tag{737.2}
$$
All logarithms below are natural unless marked $\log_2$.

**Theorem 737.1.** The complete original families satisfy
$$
\boxed{
\frac1m\sum_{h\in\mathcal H}|L_{2,h}|^2
 <2^{25}(1+\log p),\qquad
\frac1m\sum_{h\in\mathcal H}|L_{3,h}|^2
 <2^{27}(1+\log p).
}
\tag{737.3}
$$
In particular
$$
\boxed{
\left(\prod_{h\in\mathcal H^*}|L_{2,h}L_{3,h}|\right)^{1/g}
 <2^{26}\frac mg(1+\log p).
}
\tag{737.4}
$$
This remains a valid upper bound if a central value vanishes.

**Theorem 737.2.** Suppose the specified original $M_{2,1}\ne0$.
All primitive $M_{2,h}$ are then nonzero and
$$
\boxed{
\frac1g\sum_{h\in\mathcal H^*}2v_p(M_{2,h})
 <
3+
\frac{134\log2+\log(1+\log p)+2\log(2+\log_2p)}
     {\log p}.
}
\tag{737.5}
$$
Write the fraction on the right as $\delta_p$.
For $p\ge2^{160}$ one has $\delta_p<1$, and hence some actual
primitive label satisfies
$$
\boxed{v_p(M_{2,h})\le3/2.}
\tag{737.6}
$$
More quantitatively, with
$$
a_p=\#\{h\in\mathcal H^*:2v_p(M_{2,h})\le3\},
$$
one has
$$
\boxed{\frac{a_p}{g}>\frac{1-\delta_p}{9}\quad
       \text{whenever }\delta_p<1.}
\tag{737.7}
$$
For $p\ge2^{512}$ this gives $a_p>g/18$.

R729 makes the nonvanishing premise unconditional for all sufficiently
large allowed $p$. No explicit replacement for its nonvanishing threshold
is asserted here.

## 2. First sum all rational multiples with their actual signs

Let $\mathcal O=\mathbb Z[\zeta]$, with the original complex absolute
value and norm, and let $\mathcal V$ be the visible primary elements
whose norms are prime to $6p$, as in R726/R729. Every primary generator
in the original ideal sum has the unique expression
$$
a=\chi_{-3}(q)\,q\beta,\qquad
q\ge1,\quad(q,6p)=1,\quad\beta\in\mathcal V.
\tag{737.8}
$$
The factor $\chi_{-3}(q)q$ is $1\bmod3$, is odd, and has trivial
$\chi_6$ and $\theta$ value. Its remaining normalized contribution
is $\chi_{-3}(q)/q$, since the infinity type is odd.

Put
$$
c=\frac{\pi}{3\sqrt3},\qquad
K_r(u)=e^{-u}\sum_{j=0}^r\frac{u^j}{j!},
$$
$$
F_{r,2p}(u)=
\sum_{\substack{q\ge1\\(q,2p)=1}}
 \frac{\chi_{-3}(q)}qK_r(uq^2).
\tag{737.9}
$$
R729 proves, by the alternating scalar series and exact removal of
multiples of $2$ and $p$, that
$$
0\le F_{r,2p}(u)\le S K_r(u),\qquad
S=\tfrac32(1+1/p)<2.
\tag{737.10}
$$
The original complete AFE is therefore the exact identity
$$
L_{r,h}=\sum_{\beta\in\mathcal V}
 c_{r,\beta}\theta(\beta)^{\epsilon_rh},
\qquad \epsilon_2=-1,\quad\epsilon_3=1,
$$
$$
c_{r,\beta}
 =2\chi_6(\beta)
   \frac{\beta^{2r+1}}{|\beta|^{2r+2}}
   F_{r,2p}(c|\beta|^2/p).
\tag{737.11}
$$
The coefficient $c_{r,\beta}$ is independent of $h$.
There has been no removal of the original fixed cubic phase:
all character dependence is still the actual $\theta^{\epsilon_rh}$
with $h\in\mathcal H$.

The inequality
$$
K_r(u)\le(2^{r+1}-1)e^{-u/2}
$$
now gives, on putting
$$
a=c/2=\frac{\pi}{6\sqrt3},\qquad
f(T)=\frac{e^{-aT^2/p}}T,
$$
$$
|c_{2,\beta}|<28f(|\beta|)<2^5f(|\beta|),\qquad
|c_{3,\beta}|<60f(|\beta|)<2^6f(|\beta|).
\tag{737.12}
$$
All sums are absolutely convergent. Summing the rational multiples
before taking absolute values is essential: an unsigned harmonic
estimate would discard the exact cancellation in (737.10).

## 3. Square-sum bound for the actual projective directions

The character
$$
\theta:\mathbb F_{p^2}^{\times}\longrightarrow\mu_n
$$
has kernel $\mathbb F_p^\times$. Its $n=p+1$ values thus label exactly
the nonzero projective lines over $\mathbb F_p$.

For each line $\ell$, let
$$
W_\ell=\sum_{\substack{\beta\in\mathcal V\\\beta\bmod p\in\ell}}
 f(|\beta|).
\tag{737.13}
$$
If this set is nonempty, let $r_\ell$ be the least occurring
$|\beta|\ge1$; otherwise put $r_\ell=\infty$ and $W_\ell=0$.
The least value exists because the Eisenstein lattice is discrete.

We use the exact visible-point bound on an index-$p$ lattice from
R614 (614.15), with the same proof and normalization recalled in
R726 §2:
$$
N_\ell(T):=
\#\{\beta\in\mathcal V:\beta\bmod p\in\ell,\ |\beta|\le T\}
\le4+\frac{6T^2}{p}.
\tag{737.14}
$$
Visibility is part of this statement. Without visibility, multiples
of a short lattice vector would violate a bound of this form.
The global packing estimate is
$$
\#\{\beta\in\mathcal V:|\beta|\le T\}\le9T^2
\qquad(T\ge1).
\tag{737.15}
$$

Since $N_\ell(T)=0$ below $r_\ell$, Stieltjes summation gives
$$
\begin{aligned}
W_\ell
&=\int_{r_\ell}^{\infty}N_\ell(T)(-f'(T))\,dT\\
&\le4f(r_\ell)+\frac6p
          \int_{r_\ell}^{\infty}T^2(-f'(T))\,dT\\
&\le\frac4{r_\ell}+\frac{6\sqrt{\pi/a}}{\sqrt p}
 <\frac4{r_\ell}+\frac{21}{\sqrt p}.
\end{aligned}
\tag{737.16}
$$
Here the equality at the first line includes the initial jump of
$N_\ell$; it is the usual partial-summation integral with no boundary
term at infinity. Direct integration on $[0,\infty)$ gives
$$
\int_0^\infty T^2(-f'(T))\,dT
 =\sqrt{\pi p/a},
\qquad
6\sqrt{\pi/a}=6\sqrt{6\sqrt3}<21.
$$
Thus the full infinite tail is present in (737.16).

Choose one shortest representative for each nonempty line.
These representatives are distinct lattice points. If
$$
R(T)=\#\{\ell:r_\ell\le T\},
$$
then $R(T)\le9T^2$. A second partial summation at $T=\sqrt p$
therefore gives
$$
\sum_{r_\ell\le\sqrt p}\frac1{r_\ell^2}
 \le9+18\log(\sqrt p)=9+9\log p.
\tag{737.17}
$$
The other lines contribute at most $(p+1)/p<2$.
Consequently
$$
\sum_\ell r_\ell^{-2}<11+9\log p.
$$
Using $(u+v)^2\le2u^2+2v^2$ in (737.16), and summing over the
$p+1$ lines, proves
$$
\begin{aligned}
\sum_\ell W_\ell^2
&<32(11+9\log p)+882\frac{p+1}{p}\\
&<2116+288\log p\\
&<2^{12}(1+\log p).
\end{aligned}
\tag{737.18}
$$
This bound allows a line with a shortest vector of length one.
No uniform lower bound of order $\sqrt p$ for shortest vectors
has been assumed.

## 4. Exact full-family orthogonality leaves blocks of six lines

Let $q_\ell\in\mu_n$ be the character value of line $\ell$, and put
$$
C_{r,\ell}
 =\sum_{\substack{\beta\in\mathcal V\\\beta\bmod p\in\ell}}
       c_{r,\beta}.
$$
Then (737.11) is
$$
L_{r,h}=\sum_\ell C_{r,\ell}q_\ell^{\epsilon_rh}.
\tag{737.19}
$$
The elements of $\mathcal H$ are $h=1+6j$, $0\le j<m$.
Averaging the square in (737.19) uses the exact orthogonality
$$
\frac1m\sum_{j=0}^{m-1}
    (q_\ell/q_{\ell'})^{6\epsilon_rj}
 =1_{\{(q_\ell/q_{\ell'})^6=1\}}.
\tag{737.20}
$$
Partition $\mu_n$ into its cosets modulo $\mu_6$.
Each block has exactly six lines, and the remaining exponent-one
phase must be retained. We get the equality
$$
\frac1m\sum_{h\in\mathcal H}|L_{r,h}|^2
 =\sum_{\mathcal B\in\mu_n/\mu_6}
     \left|\sum_{\ell\in\mathcal B}
              C_{r,\ell}q_\ell^{\epsilon_r}\right|^2.
\tag{737.21}
$$
Cauchy--Schwarz in a block of six, followed by (737.12), yields
$$
\frac1m\sum_{h\in\mathcal H}|L_{r,h}|^2
 \le6\sum_\ell|C_{r,\ell}|^2
 <6B_r^2\sum_\ell W_\ell^2,
\quad B_2=2^5,\ B_3=2^6.
\tag{737.22}
$$
Together with (737.18) and $6<8$, this is precisely (737.3).

The passage to the primitive family uses nonnegativity of squared
absolute values, not primitive-character orthogonality:
$$
\frac1g\sum_{h\in\mathcal H^*}|L_{r,h}|^2
 \le\frac mg\cdot
        \frac1m\sum_{h\in\mathcal H}|L_{r,h}|^2.
\tag{737.23}
$$
Apply arithmetic--geometric mean separately to $|L_{2,h}|^2$ and
$|L_{3,h}|^2$ and multiply their square roots. This gives (737.4),
including the factor $m/g$ rather than its square.

## 5. The same original algebraic norm now has exponent eight

Recall the unchanged original data from R717/R730:
$$
\mathcal P=\frac{S_2S_3}{C_0^2}\in F_0,\qquad
D=2^{37}3^{26}p^5,\qquad D\mathcal P\in\mathcal O_{F_0},
$$
$$
N=N_1\in\mathcal O_{F_0},\qquad
\sigma_h(N)=N_h>0,
$$
$$
M_{2,h}^2
 =-\frac{8\zeta^2N_h}{(p+1)^2}C_0^2\sigma_h(\mathcal P).
\tag{737.24}
$$
The exact original period formula is
$$
\sigma_h(\mathcal P)
 =C_{\rm per}\,p^2L_{2,h}L_{3,h},\qquad
0<C_{\rm per}
 =\frac{\alpha^2}{144\Omega^2\mathcal A^5}<2^{16}.
\tag{737.25}
$$
All these are identities for the original positive quotient and
its actual toric vector.

Set $T_p=2+\log_2p$. R733 proves
$$
\frac mg=\frac n{3\varphi(n)}<T_p,\qquad
\left(\prod_{h\in\mathcal H^*}N_h\right)^{1/g}<5pT_p.
\tag{737.26}
$$
Equations (737.4)--(737.26) give
$$
\left(\prod_{h\in\mathcal H^*}
          |\sigma_h(\mathcal P)|\right)^{1/g}
 <2^{42}p^2(1+\log p)T_p.
\tag{737.27}
$$
Since $2^{37}3^{26}<2^{89}$ and $5<8$,
$$
\boxed{
\left|N_{F_0/\mathbb Q}(DN\mathcal P)\right|^{1/g}
 <2^{134}p^8(1+\log p)T_p^2.
}
\tag{737.28}
$$

Under $M_{2,1}\ne0$, the integer on the left before taking the
$g$th root is nonzero. Every $M_{2,h}$ is nonzero by the same original
Galois argument in R730. Since $p$ splits completely in $F_0$,
$$
v_p\!\left(N_{F_0/\mathbb Q}(DN\mathcal P)\right)
 =5g+2\sum_{h\in\mathcal H^*}v_p(M_{2,h}).
\tag{737.29}
$$
Taking logarithms in the nonzero-integer inequality
$p^{v_p(N(DN\mathcal P))}\le|N(DN\mathcal P)|$, then using
(737.28), proves (737.5).

Each $2v_p(M_{2,h})$ is an integer, because the right side of
(737.24) apart from its displayed fixed units lies in the selected
copy of $\mathbb Q_p$. This proves integrality of the doubled
valuation only.

For the explicit thresholds, put $L=\log_2p$.
Since $\log2<1$,
$$
\delta_p
 \le\frac{134+3\log_2(L+2)}L.
\tag{737.30}
$$
At $L=160$, $\log_2(162)<8$, so the numerator is less than $158$.
The difference
$L-134-3\log_2(L+2)$ is increasing for $L\ge160$.
Thus $\delta_p<1$ throughout that range. If every doubled
valuation were at least four, it would contradict (737.5).
This proves (737.6).

Similarly, at $L=512$, $\log_2(514)<10$, so
$134+3\log_2(514)<164<256$.
The difference
$L/2-134-3\log_2(L+2)$ is increasing for $L\ge512$.
Hence $\delta_p<1/2$ for $p\ge2^{512}$.

## 6. A positive proportion, with no unsupported integer rounding

The integrality in (737.24) also gives at each prime above $p$
$$
v_p(N_h)\ge0,\qquad v_p(\sigma_h(\mathcal P))\ge-5,
\qquad 2v_p(M_{2,h})\ge-5.
\tag{737.31}
$$
If exactly $a_p$ labels have doubled valuation at most three,
all the remaining integral doubled valuations are at least four.
Therefore
$$
\sum_{h\in\mathcal H^*}2v_p(M_{2,h})
 \ge-5a_p+4(g-a_p)=4g-9a_p.
\tag{737.32}
$$
Combining this with (737.5) yields (737.7), and then $a_p>g/18$
at the second explicit threshold.

For each such label, retain the original complete flat jets and put
$$
E_{j,h}=\frac{p^{3j}M_{3j-1,h}}{(3j)!},\qquad
G_h(V)=\frac{\mathcal I_h(V)}{E_{1,h}}
       =V+\sum_{j\ge2}b_{j,h}V^j.
$$
R730 proves, without residue-unit assumptions,
$$
b_{j,h}\in\mathbb Q_p,\qquad
v_p(E_{j,h})\ge
\frac{3j-1}{p+1}-v_p(3j)>0,
\qquad v_p(E_{j,h})\longrightarrow\infty.
\tag{737.33}
$$
If $\eta_h=v_p(M_{2,h})\le3/2$, then
$$
v_p(b_{j,h})>-\eta_h-3\ge-9/2.
$$
The ratios are rational $p$-adic numbers, so the valid rounding is
$$
b_{j,h}\in p^{-4}\mathbb Z_p,\qquad
v_p(b_{j,h})\longrightarrow\infty.
\tag{737.34}
$$
It follows that $G_h(p^5u)/p^5=u+pH(u)$ in the restricted power-series
ring. Compose with the full original change of variable
$$
V=\Psi(s/p^3),\qquad
\Psi(v)=\tfrac38v+p\,v^2\mathbb Z_p\langle v\rangle,
\qquad s=a-1.
$$
The exact normalized conclusion is
$$
\boxed{
\frac{16\mathcal I_h(p^8u)}{p^8M_{2,h}}
 =u+pH_h(u),\qquad H_h\in u^2\mathbb Z_p\langle u\rangle.
}
\tag{737.35}
$$
This is an isometric automorphism of the full closed unit disc, with
the same exact difference valuations as R733. The actual component
$c_h\mathcal I_h$ retains its original nonzero KS scalar $c_h$.

Without another argument, $\eta_h=3/2$ is allowed; it does not imply
$\eta_h\le1$. Thus the gain in the norm estimate and the number of
available labels does not by itself improve (737.35) to depth seven.
Neither (737.35) nor the second moment is a canonical-height equation.
The original depth-four candidates and the true height exterior
remain to be excluded.

## Sources and dependencies

- [R717](R717-exact-original-CM-norm-from-certified-complex-traces.md):
  original character directions, full AFE, exact period factor and
  integral denominator.
- [R726](R726-uniform-original-primitive-nonvanishing.md), §2:
  the uniform visible-point bound on each index-$p$ lattice, with its
  R614 normalization, and the global packing bound.
- [R729](R729-uniform-full-Abel-nonvanishing-and-valuation-bound.md),
  §§2--3: the full odd family and the exact signed scalar kernel;
  its uniform theorem supplies the original nonvanishing premise.
- [R730](R730-fixed-depth-original-Abel-isometry-by-all-embedding-norm.md):
  original toric-norm integrality, norm over all primes above $p$,
  rational jet ratios and the complete one-$p$ Hodge bound.
- [R733](R733-averaged-original-toric-norms-and-depth-eight-Abel-isometry.md):
  average of the original toric norms and the fixed original coarse
  change of parameter.
