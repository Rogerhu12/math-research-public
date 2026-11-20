# R980 — Original level-one Hurwitz reflection and its distinct mirror pairs

Date: 2026-11-20. Authoring agent: literature_frontier. Independently checked by root against the primary sources.

**Status: proved application of a published theorem.** Robert's 1980 level-one reflection applies to both pure Hurwitz indices in R978, with no omitted exceptional original prime and with an explicit scalar. The already proved low coefficient gives a new, explicitly identified coefficient of size linear in $p$ that is a unit. The unknown high coefficient is equivalent to a different reflected coefficient. These are two distinct reflection pairs; this note does not prove high nonvanishing.

The general reflection theorem is due to Gilles Robert, not a new theorem of this repository. The new work here is its exact specialization to the original differential, its factorial-free identification with R978, and the separation of its two reflection pairs from the Frobenius pair used in the inert Kummer criterion. All calculations below are symbolic. No numerical mathematics has been executed locally.

## 1. Original objects and the four indices

Retain the two rows of R972/R978:
$$
\begin{array}{c|c|c|c}
p\bmod12&r&a=r+1&n=p+1-a\\ \hline
11&2&3&p-2\\
5&8&9&p-8
\end{array}
\qquad p\ge41,\quad p\equiv2,5\pmod9.
\tag{980.1}
$$
In particular $p\equiv5\pmod6$, $a,n\equiv3\pmod6$, and $3\le a,n<p$. Keep the actual CM source and differential:
$$
E_+:\ y^2=x^3+1,\qquad
\omega=\frac{dx}{2y},\qquad
g_2=0,\quad g_3=-4,\quad \Delta=-432.
\tag{980.2}
$$
The pure coefficients have exactly the R978 definition
$$
\log\frac{\sigma_{E_+}(z)}z
=-\sum_{k\ge4}\frac{\mathcal G_k}{k}z^k,
\qquad \sigma_{E_+}'(0)=1,\quad \omega=dz.
\tag{980.3}
$$
For even $k\ge4$ they are the lattice sums $\sum_{\lambda\ne0}\lambda^{-k}$. They are rational numbers, and vanish unless $6\mid k$.

Put
$$
k_{\rm lo}=a(p-1),\qquad k_{\rm hi}=n(p-1)
=p^2-1-a(p-1).
\tag{980.4}
$$
Define their Robert reflections
$$
k_{\rm lo}^{*}=(a+1)p-a+1,\qquad
k_{\rm hi}^{*}=np+a=p^2-rp+r+1.
\tag{980.5}
$$
Their explicit values are:

| Original row | $k_{\rm lo}$ | $k_{\rm lo}^{*}$ | $k_{\rm hi}$ | $k_{\rm hi}^{*}$ |
|---|---:|---:|---:|---:|
| $r=2,\ a=3$ | $3p-3$ | $4p-2$ | $p^2-3p+2$ | $p^2-2p+3$ |
| $r=8,\ a=9$ | $9p-9$ | $10p-8$ | $p^2-9p+8$ | $p^2-8p+9$ |

All four numbers lie between $4$ and $p^2+1$ and are divisible by six. The distinction between the two starred indices will be maintained throughout.

## 2. Robert's normalization is precisely the original pure coefficient

Robert, *Congruences entre séries d'Eisenstein, dans le cas supersingulier*, Inventiones Mathematicae **61** (1980), 103–158, defines on printed p. 105
$$
G_k^{\rm Rob}=-\frac{B_k}{2k}E_k,\qquad
S_k=\frac{2G_k^{\rm Rob}}{(k-1)!}
=-\frac{B_k}{k!}E_k.
\tag{980.6}
$$
Here $E_k$ has the usual normalized Fourier expansion with constant coefficient one. The symbol $G_k^{\rm Rob}$ in this equation is a modular form with Fourier coefficients, and must not be identified with the pure $\mathcal G_k$ of (980.3).

The exact identification instead follows from Robert's §1.4(2), printed p. 114:
$$
X_{E,\omega}(z)
=z^{-2}+\sum_{\substack{k\ge4\\k\ {\rm even}}}
(k-1)S_k(E,\omega)z^{k-2},\qquad \omega=dz.
\tag{980.7}
$$
Twice differentiating (980.3), with the sign in the identity
$X_{E_+,\omega}=-\partial_z^2\log\sigma_{E_+}$, gives the same expansion with $\mathcal G_k$ in place of $S_k(E_+,\omega)$. Therefore
$$
\boxed{\quad S_k(E_+,\omega)=\mathcal G_k.\quad}
\tag{980.8}
$$
There is no remaining factorial, transcendental period, or power of $p$ in (980.8).

For the algebraic sign convention, Robert's §1.2, Proposition 1, printed p. 112, writes the Weierstrass equation as
$$
Y^2=4X^3-\frac{E_4}{12}X+\frac{E_6}{216},
\qquad \omega=\frac{dX}{Y}.
\tag{980.9}
$$
With $Y=2y$, the original pair (980.2) therefore has
$$
E_4(E_+,\omega)=0,\qquad E_6(E_+,\omega)=+864.
\tag{980.10}
$$
As a direct normalization check, (980.6) gives
$S_4=E_4/720$ and $S_6=-E_6/30240$; these equal
$g_2/60$ and $g_3/140$, respectively, in the Laurent expansion of the actual Weierstrass function. In particular the source is $g_3=-4$. The $g_3=+4$ curve used for the balanced coefficient in R974/R975 is not substituted here.

## 3. The published level-one theorem and the supersingular unit

Let
$$
M=\mathbb Z_p[E_4,E_6],\qquad
\Lambda=\frac{E_{p-1}}p,\qquad L=M[\Lambda].
\tag{980.11}
$$
For a $p$-adically separated torsion-free $\mathbb Z_p$-algebra $A$, Robert considers pairs $(E,\omega)$ over $A$ with everywhere nonvanishing differential and
$E_{p-1}(E,\omega)\in pA$. Every element of $L$ can be evaluated integrally on such a pair.

For an even integer $4\le k\le p^2+1$, define $k^*$ as the unique even integer in the same range satisfying
$$
k^*+pk\equiv p+1\pmod{p^2-1}.
\tag{980.12}
$$
Robert defines $\mathscr S_k=p^{e(k)}S_k$ by the integral lattice $L$. His results in §5.3 give $e(k)=0$ outside the three possible exceptional weights
$$
p+1,\qquad p^2-1,\qquad p^2+1.
\tag{980.13}
$$
The functional equation is stated in the introduction, printed pp. 105–106, and proved as §5.4, Theorem 8, printed p. 152. For a unit $b_k\in\mathbb Z_p^\times$ it gives
$$
\mathscr S_{k^*}(E,\omega)\equiv
b_k\left(\frac{E_{p+1}(E,\omega)}{12}\right)^{(k^*-k)/(p+1)}
\mathscr S_k(E,\omega)\pmod p.
\tag{980.14}
$$
One can state this with $k^*>k$ as a congruence in the graded lattice itself; the reverse direction follows by inversion of its unit coefficient at the supersingular pair.

All hypotheses hold for the fixed source (980.2). Indeed $E_+$ is smooth over $\mathbb Z_p$, $\omega$ is an integral generator, and its $\mu_6$ automorphisms force
$$
E_{p-1}(E_+,\omega)=0
\tag{980.15}
$$
already in characteristic zero: the weight $p-1\equiv4\pmod6$ is not divisible by six. Thus evaluation of $\Lambda$ is exactly zero, not an unspecified quotient of two vanishing quantities.

Set, without rescaling the differential,
$$
B_p=E_{p+1}(E_+,\omega).
\tag{980.16}
$$
This is a $p$-integral number. Its nonzero reduction is also independently fixed by the universal supersingular congruence of Baker, Theorem 1.4, already used in R939:
$$
B_p^{p-1}\equiv
-\left(\frac{-1}{p}\right)(-432)^{(p^2-1)/12}\pmod p.
\tag{980.17}
$$
The right side is nonzero for $p\ge41$, so $B_p\in\mathbb Z_p^\times$. This supplies the needed unit on the original differential, including the elliptic point $j=0$. It does not choose a new supersingular frame or normalize $B_p$ to one.

## 4. Exact specialization to both original indices

Take $k=t(p-1)$ with $t=a$ or $t=n$. Since $1<t<p$,
$$
k^*=k+p+1.
\tag{980.18}
$$
Indeed $k+p+1+pk=(p+1)+t(p^2-1)$, and $k+p+1$ lies in the prescribed range. Neither $k$ nor $k^*$ is any weight in (980.13). Thus both modified series in (980.14) are the unmodified $S$ series.

Robert's explicit constant in §5.4, case (i), printed p. 150, is
$$
b_{k^*}=k/(p-1)=t,\qquad b_k=t^{-1}
\tag{980.19}
$$
for this case. The separate case $t=p$ in the source is not used. The exponent in (980.14) is exactly one. Combining (980.8), (980.16), (980.18), and (980.19) proves
$$
\boxed{\quad
\mathcal G_{t(p-1)+p+1}
\equiv\frac{B_p}{12t}\mathcal G_{t(p-1)}\pmod p,
\qquad t\in\{a,n\}.
\quad}
\tag{980.20}
$$
The same theorem gives $p$-integrality of the starred coefficients. The unstarred coefficients are already integral by R978. All factors $12,t,B_p$ in (980.20) are units.

Consequently R978's established low unit gives
$$
\boxed{\quad
\mathcal G_{(a+1)p-a+1}\in\mathbb Z_p^\times.
\quad}
\tag{980.21}
$$
For the high coefficient one obtains only the exact equivalence
$$
\boxed{\quad
S_{\rm orig}\ne0
\quad\Longleftrightarrow\quad
\mathcal G_{np+a}\in\mathbb Z_p^\times.
\quad}
\tag{980.22}
$$
In (980.21) the indices are $4p-2$ and $10p-8$ in the two rows. In (980.22) they are $p^2-2p+3$ and $p^2-8p+9$. They are not the same modular coefficient.

## 5. The exact original Artin–Hasse coordinate after reflection

Keep R978's original roots and character:
$$
m=(p+1)/3,\quad b=a/3,\quad
\varpi=\eta X,\quad \eta^m=-1,\quad
\sigma\varpi=\zeta\varpi,\quad
\chi(\sigma)=\zeta^{-b}.
\tag{980.23}
$$
No change to $\eta$, $\zeta$, the arithmetic Artin symbol, or the two residue embeddings is made.

Dividing (980.20) by $t(p-1)$ yields the useful uniform scalar identity
$$
\overline{\frac{\mathcal G_{t(p-1)}}{t(p-1)}}
=-\frac{12}{\overline B_p}\,
\overline{\mathcal G_{t(p-1)+p+1}}.
\tag{980.24}
$$
Here $p-1\equiv-1\pmod p$ produces the minus sign. In particular, the $t$ factor cancels; no factorial is reintroduced.

Substitution into R978, equations (978.13)–(978.14), now gives
$$
\boxed{\quad
\gamma_1=
-288\,\overline\eta^{-(m-b)}
\bigl(\chi(\sigma)-1\bigr)\overline B_p^{-1}
\overline{\mathcal G_{np+a}}.
\quad}
\tag{980.25}
$$
The already nonzero low coordinate becomes
$$
\boxed{\quad
\gamma_0=
\left(
-288\,\overline\eta^{-b}
(\overline\zeta^b-1)\overline B_p^{-1}
\overline{\mathcal G_{(a+1)p-a+1}}
\right)^p.
\quad}
\tag{980.26}
$$
These equalities retain R976/R978's actual local basis. The $p$th power in (980.26) is the prescribed residue-embedding operation; it is not the Robert reflection (980.12). Every displayed multiplier outside a pure coefficient is nonzero in the original range.

## 6. What the original inert Kummer and reflection results do not imply

There are two different index operations in the primary literature. They must not be interchanged:
$$
\begin{array}{rcl}
\text{Frobenius mate:}&k\longmapsto pk&\pmod{p^2-1},\\
\text{Robert reflection:}&k\longmapsto p+1-pk&\pmod{p^2-1}.
\end{array}
\tag{980.27}
$$
For $k_{\rm lo}=a(p-1)$, its Frobenius mate is $k_{\rm hi}=p^2-1-k_{\rm lo}$. Its Robert reflection is instead $k_{\rm lo}^*=k_{\rm lo}+p+1$.

Robert's 1978 paper, introduction Theorem 1, printed pp. 300–301, formulates the inert condition using the pair of coefficients with indices $k$ and $pk\bmod(p^2-1)$ in a two-dimensional residue space. For class number one, Appendix B, Proposition B.1, printed p. 353, makes the relevant condition the nonvanishing of at least one of these two coefficients. The known nonzero low coefficient already satisfies that condition; it supplies no proof that the high member is separately nonzero.

Robert's 1979 Grenoble exposition uses the reflection $k\mapsto p+1-pk$ and announces results relying on texts then in preparation. The published 1980 Theorem 8 above supplies the level-one theorem actually used here. We do not treat the 1979 exposition as a stronger Frobenius-mate equality.

Gillard's 1982 Grenoble Theorem 1.1.2 is a higher-level generalization with explicit exclusions modulo $p-1$, including the class $k\equiv0\pmod{p-1}$. Those exclusions prevent use of that particular generalization for our unstarred indices; they do not remove the same indices from Robert's published level-one theorem. In particular it would be incorrect to discard (980.20) because of Gillard's larger-level hypotheses.

There is also a separate stronger equivalence of two conjugate Bernoulli-type quantities in Charkani El Hassani–Gillard (1986), §4.1.3, printed p. 38, under the hypothesis that the ambient field is abelian over $\mathbb Q$. Our conductor-$p$ ring class field has generalized dihedral Galois group over $\mathbb Q$, with cyclic subgroup of order $m=(p+1)/3>2$. It is not abelian over $\mathbb Q$. That stronger result therefore cannot exchange the two original Artin–Hasse coordinates.

The surviving next question is whether a genuine integral comparison identifies a separately controlled mixed Eisenstein–Kronecker coefficient with the high quantity in (980.22), or proves that quantity nonzero by another method. Replacing $\bar\lambda$ by $\lambda^p$ termwise in an infinite complex lattice sum is not such a comparison.

## 7. Sources and reproducibility of this source check

1. Gilles Robert, *Congruences entre séries d'Eisenstein, dans le cas supersingulier*, Inventiones Mathematicae **61** (1980), 103–158, DOI [10.1007/BF01390118](https://doi.org/10.1007/BF01390118). Definitions and theorem: printed pp. 105–106; Weierstrass convention: §1.2, Proposition 1, p. 112; coefficient identification: §1.4(2), p. 114; explicit constant: §5.4 case (i), p. 150; formal functional equation: Theorem 8, p. 152. [Public Göttingen scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0061/LOG_0012.pdf). The scan includes one library cover; printed page 103 is PDF page 2.
2. Andrew Baker, *A supersingular congruence for modular forms*, Acta Arithmetica **86** (1998), 91–100, Theorem 1.4. [Author PDF](https://www.maths.gla.ac.uk/~ajb/dvi-ps/modforms.pdf). The congruence and its normalization are already registered in R939.
3. Gilles Robert, *Nombres de Hurwitz et unités elliptiques. Un critère de régularité pour les extensions abéliennes d'un corps quadratique imaginaire*, Annales scientifiques de l'École Normale Supérieure, 4e série **11** (1978), 297–389, introduction Theorem 1, pp. 300–301, and Appendix B, Proposition B.1, p. 353. [Primary scan](https://www.numdam.org/article/ASENS_1978_4_11_3_297_0.pdf).
4. Gilles Robert, *Une curieuse symétrie des unités elliptiques*, Séminaire de théorie des nombres de Grenoble **7** (1978–1979), exposé 4, 1–20; §§4 and 6. [Primary scan](https://www.numdam.org/article/STNG_1978-1979__7__A4_0.pdf).
5. Roland Gillard, *Séries d'Eisenstein et critère de Kummer*, Séminaire de théorie des nombres de Grenoble **10** (1981–1982), exposé 2, 1–15; Theorem 1.1.2, printed p. 4, and §2.3.2.2. [Primary scan](https://www.numdam.org/article/STNG_1981-1982__10__A2_0.pdf).
6. Mohamed Charkani El Hassani and Roland Gillard, *Unités elliptiques et groupes de classes*, Annales de l'Institut Fourier **36** (1986), no. 3, 29–41; §§4.1.3–4.1.4, printed p. 38. [Primary scan](https://www.numdam.org/item/10.5802/aif.1057.pdf).
7. R972, R976, and R978 for the already proved low coordinate and the exact relation between the original high trace and the high pure Hurwitz coefficient. No old finite trace, coefficient, or same-label calculation has been rerun.
