# R150 appendix: exact original-source presentation of the remaining normal target module

Author: Astra-ISP-789f / normal_annihilator. AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-15 UTC.

Status: an exact module and source-transport theorem. It uses the paid original projection transformations. The complete normal tails described below have not been numerically constructed by this appendix. No new high-rank calculation or original target membership is reported.

## 1. The original modules and the target of the next calculation

Let
$$
S=\mathbb Q[s,\Sigma_0^{-1}],\qquad
\Sigma_0=s(s-2)(s+6)F_+F_-E_8.
$$
Use the same original seventeen equations and source degree bound as in the [original polynomial projection reduction](R150-appendix-original-projection-away-from-critical-support-56-by-22-schur.md). Let
$$
A:S^{6188}\longrightarrow V=S^{4367},\qquad L=\operatorname{im}A.
$$
The source coordinates are the original seventeen equations multiplied by all moment monomials of degree at most three. The target coordinates are all moment monomials of degrees one through five.

Use the paid co-moving binomial coordinates
$$
m_i=\sum_{j=0}^{i}\binom ij s^{\,i-j}z_j,\qquad c=z_0,\quad d=z_1.
$$
This change has determinant one on the moment variables and induces polynomial units on the complete finite source and target monomial modules. It introduces no parameter localization.

Let $W\subset V$ be the span of the outputs containing at least two of $z_2,\ldots,z_{10}$. Then
$$
\operatorname{rank}W=450+990+1485+1287=4212,
\qquad \operatorname{rank}(V/W)=155.
$$
The remaining target obstruction module is
$$
T=W/(L\cap W).
\tag{1.1}
$$
It is the kernel in the exact original cokernel sequence
$$
0\longrightarrow T\longrightarrow V/L
\longrightarrow (V/W)/((L+W)/W)\longrightarrow0.
\tag{1.2}
$$
The [PID divisor theorem](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md) concerns this exact module.

The following dimension table specifies complete original source and target dictionaries, rather than replacement matrices chosen only by their dimensions.

| Normal degree | Source count | Target count |
|---:|---:|---:|
| 0 | $17\cdot10=170$ | $20$ |
| 1 | $17\cdot9\cdot6=918$ | $135$ |
| 2 | $17\cdot45\cdot3=2295$ | $450$ |
| 3 | $17\cdot165=2805$ | $990$ |
| 4 | $0$ | $1485$ |
| 5 | $0$ | $1287$ |
| Total | $6188$ | $4367$ |

The original equations have moment degrees one and two. The six $\Gamma$ equations are quadratic in the moment variables; their moment-linear part is zero. They are not treated as linear equations in this argument.

## 2. A source basis with 6012 genuine zero-projection columns

Write the restriction of the original equations to the pure tangent plane as
$$
F_i|_{z_2=\cdots=z_{10}=0}=g(s)\,\beta_i(s)d^2,
\qquad g(s)=-2s^2(s-2)(s+6).
\tag{2.1}
$$
The original polynomial generator proves these identities for all seventeen equations. It also supplies a constant rational row $\alpha$ with
$$
\sum_i\alpha_i\beta_i=1.
\tag{2.2}
$$
Concretely, its eleven $N$ entries are the first row of $J_2^{-1}/4$, and its six $\Gamma$ entries are zero. Thus
$$
F_g=\sum_i\alpha_iF_i
$$
has pure restriction $g d^2$.

Choose any fixed index $i_0$ with $\alpha_{i_0}\ne0$. The rows $\alpha$ and
$$
e_i-\beta_i\alpha\qquad(i\ne i_0)
\tag{2.3}
$$
form a polynomial unit source transformation: its determinant is the same nonzero rational constant as that of the rows $\alpha,e_i$ for $i\ne i_0$. No polynomial determinant is silently inverted.

### 2.1 All one-normal sources

For each of the 54 monomials
$$
z_jc^ad^b,\qquad 2\le j\le10,\quad a+b\le2,
$$
apply (2.3) to its seventeen original equation sources. Their projection to $V/W$ retains one actual $g$-row,
$$
z_jc^ad^bF_g\ \mapsto\ g\,z_jc^ad^{b+2},
$$
and sixteen actual zero-projection difference sources.

Consequently these 918 sources become
$$
54\text{ true }g\text{-rows}\quad+\quad864\text{ zero-projection sources}.
\tag{2.4}
$$
The complete normal tails of both families remain part of their original source products. Only their projections have the displayed forms.

Since $g$ is a unit in $S$, the 54 distinct projected coordinates can be eliminated by valid source and target transformations over $S$.

### 2.2 Three additional pure groups

Among the ten pure source multipliers, the seven retained by the original core are
$$
1,\ c,\ d,\ c^2,\ cd,\ c^3,\ c^2d.
\tag{2.5}
$$
The remaining three are $d^2,cd^2,d^3$. After the 54 projected one-normal coordinates have been eliminated, the projection of each of these seventeen-source groups has only its corresponding pure output:
$$
g d^4,\qquad g c d^4,\qquad g d^5.
$$
Applying the same polynomial unit transformation (2.3) gives three further genuine unit rows and
$$
3\cdot16=48
$$
additional genuine zero-projection sources.

This leaves the original 119 retained sources in (2.5), with the paid projected 119 by 85 matrix.

### 2.3 The original higher-normal sources

All $2295+2805=5100$ original source multipliers of normal degree at least two have zero projection to $V/W$, by exact monomial support. Their full original products in $W$ are retained.

Thus the three families together give
$$
\boxed{6012=5100+864+48}
\tag{2.6}
$$
source columns with exactly zero projection. This is an actual source-basis decomposition over $S$. It does not say that their products generate $W$, or that any 4212 of those products form a unit block.

## 3. The remaining source and target transformations

The paid thirteen polynomial left kernels of the projected matrix have a distinguished free-coordinate block
$$
D_{\mathrm{lin}}^2I_{13},
$$
where
$$
D_{\mathrm{lin}}
=s^8(s-2)^2(s+6)^2F_+^3F_-^3E_8^2
$$
is a unit in $S$. After division by this unit, their free-coordinate block is exactly $I_{13}$.

Extend these thirteen vectors by zero on $W$. They annihilate every original source: the projected pure sources and the 54 retained one-normal sources were checked; the other one-normal sources are their exact projected combinations; all higher-normal sources project to zero. Therefore the output change that completes these thirteen vectors to a unit basis gives thirteen identically zero rows of the complete original $A$. It is a change on $V/W$ extended by the identity on $W$.

For each of the seven pure multipliers in (2.5), the original core applies the triangular binomial transform to the eleven $N$ equation sources, leaving the six $\Gamma$ sources intact. Its determinant is one. The retained matrix is
$$
R=
\begin{pmatrix}
U&C_{\rm right}\\
C_{\rm lower}&D_{\rm small}
\end{pmatrix},
$$
with block sizes $63+56$ by $63+22$. The 63 by 63 block $U$ is triangular by multiplier degree with seven identical 9 by 9 diagonal blocks $H$. The original adjugate identities prove
$$
\det H=c\,D_{\mathrm{lin}},\qquad c\in\mathbb Q^\times.
$$
Hence $U$ is an actual unit over $S$, not a generic or finite-field placeholder.

Eliminating this block contributes 63 further source and target units. In total,
$$
54+3+63=120
\tag{3.1}
$$
originally transported unit directions have been separated. The remaining projected matrix is the complete 56 by 22 matrix $G$.

The final recorded divisions of the core by the six known factors are units in $S$. A source-row division must also be applied to that row's complete normal tail. A projected target-column division extends by the identity on $W$. This convention fixes exactly which original matrix $G$ is used below.

There is a minor but necessary point about the full tails of the 120 unit sources. A source with product $(e_i,h_i)$ in a projected unit coordinate and $W$ can have its tail cleared by the output automorphism
$$
(v_{\rm unit},w)\longmapsto
(v_{\rm unit},w-H_{\rm unit}v_{\rm unit}).
$$
This automorphism fixes $W$ pointwise. Thus clearing the full unit-source tails does not alter the module (1.1), even though it changes products of other source columns.

## 4. The exact relative presentation

Transport every complete original source product through the preceding changes. There are uniquely determined transported matrices
$$
B\in S^{4212\times6012},
\qquad
H_{\rm tail}\in S^{4212\times56}
$$
such that the complete original source map is equivalent over $S$ to 120 identity directions, thirteen zero output rows, and
$$
\mathcal A=
\begin{pmatrix}
G^T&0\\
H_{\rm tail}&B
\end{pmatrix}
:
S^{56}\oplus S^{6012}\longrightarrow S^{22}\oplus W.
\tag{4.1}
$$
All the output equivalences preserve $W$, with the tail-clearing transformations fixing it pointwise. The 6012 columns of $B$ are the complete products of the source families in §2 after the same transformations. The 56 columns of $H_{\rm tail}$ are the complete products of the retained core sources.

It follows directly from (4.1) that
$$
L\cap W=B S^{6012}+H_{\rm tail}\ker(G^T).
$$
Indeed, a source pair $(v,b)$ has zero projected output if and only if $G^Tv=0$, and its remaining output is $H_{\rm tail}v+Bb$. Hence
$$
\boxed{
T\ \simeq\
\operatorname{coker}_W
\bigl[B,\ H_{\rm tail}\ker(G^T)\bigr].
}
\tag{4.2}
$$

The original core has generic column rank 22. Since $S$ is a localization of the PID $\mathbb Q[s]$,
$$
\ker(G^T)\text{ is free of rank }56-22=34.
$$
These 34 source relations cannot be discarded. In particular, replacing (4.2) by $\operatorname{coker}B$ would omit genuine original sources whose projected terms cancel.

Likewise, the numerical identity $\operatorname{rank}W=4212$ does not prove that $B$ has a unit 4212 by 4212 submatrix. Neither assertion is made here.

## 5. A 56-column replacement when the exact projection divisor is inverted

Let $\Omega$ be the complete maximal-minor gcd of $G$. Over
$$
S'=S[\Omega^{-1}],
$$
the matrix $G^T$ is surjective. Choose an actual right inverse
$$
J:S'^{22}\longrightarrow S'^{56},
\qquad G^TJ=I_{22}.
$$
Then
$$
\operatorname{im}(I_{56}-JG^T)=\ker(G^T).
$$
Therefore (4.2) becomes the completely equivalent presentation
$$
\boxed{
T\otimes_SS'
\simeq
\operatorname{coker}_{W\otimes_SS'}
\bigl[B,\ H_{\rm tail}(I_{56}-JG^T)\bigr].
}
\tag{5.1}
$$
This uses 56 explicit relation generators instead of first selecting a rank-34 relation basis.

There is also a direct source-certified construction from any completed list of genuine maximal minors. If their gcd is $U$, then over $S[U^{-1}]$ an exact Bezout identity for those determinants and their adjugates gives a right inverse. The constant row combinations defining each actual minor must be included in its source embedding. This construction uses the paid minor source records, not an arbitrary square matrix with the same determinant degree.

Inverting $U$ or $\Omega$ here is only an algebraic presentation of a parameter-localized module. It is not an actual bounded operator inverse and does not prove membership at their zeros.

## 6. What is already available and what must still be computed

The original core source is

~~~text
notes/2026-11-15-r150-original-global-projection-polynomial-core-789f.py
blob 178a474ace771c3c934ca85fb500fef3f79425ef
SHA256 727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb
~~~

Its immutable original core has semantic binding

~~~text
ce358eac629541da0c9d35fd29c66424fa0d89ded97cfec93f324cf56e9d16ba
~~~

and logical SHA256

~~~text
752d21d7ca74ee5235c05ade9048ef48f120891c567abfb5132a4b2b33b745c8
~~~

The existing phases retain the exact pure and one-normal coefficient polynomials, the actual $H$ and its normalized adjugate, the triangular solve, the complete uncancelled core, and the final known-unit division list. They suffice to specify all transformations above and to reconstruct their action on any complete original product.

They do not yet contain the full normal-degree-two coefficients of the seventeen original equations or the transported arrays $B,H_{\rm tail}$. A numerical next step must:

1. extract those missing original polynomial coefficients from the same physical generator, checking its complete seventeen equations and the already paid pure/one-normal coefficients;
2. apply the precise source transformations of §§2–3 to their full original products;
3. preserve all 6012 zero-projection sources and all 56 retained tails;
4. check that the complete projected products are respectively zero and the same paid $G$;
5. only then compress or solve the presentation (4.2) or (5.1), keeping full original-source reconstruction.

The source multiplier degrees remain at most three throughout these transformations. The parameter denominators are exactly units of the declared localization. No larger moment source space is inserted by the theorem.

## 7. Scope

This appendix supplies the precise original-source object required to attack the remaining module $T$. It avoids both a repetition of the complete 4367 by 6188 elimination and an unsupported assertion that the high-normal coordinates are already generated by units.

It does not claim that the full normal tails have been numerically materialized, that $T$ is zero, that the nine $h_*$ squares already have global original sources, or that the normalized rank-one Bell identities have become identities in the full gradient ideal. Each of those conclusions requires its corresponding additional original-source certificate.
