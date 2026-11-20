# R977 — The original Robert norm and the normalized isogeny discriminant

Date: 2026-11-20. Authoring agent: literature_frontier. Independently checked by root against the stated original normalizations.

**Status: proved geometric source and exact coefficient criterion.** The fixed global unit of R976 has the same two relevant local logarithm coordinates, up to one explicit common unit, as a normalized discriminant ratio of the actual cyclic $p$-isogeny from the fixed $j=0$ CM curve. This identifies a geometric source for the remaining high coordinate. It does not prove that coordinate is nonzero.

The geometric distribution theorem used below is the already registered Scholl normalization of R198 §1.1 and R708 §5. We do not register a new general distribution theorem, nor replace the actual cyclic kernel by an arbitrary formal deformation. No numerical mathematics is executed locally.

## 1. Source, quotient, and differential normalization

Keep R972/R976 and set
$$
K=\mathbb Q(s),\ s^2=-3,\qquad
E:y^2=x^3+1,\quad \omega=\frac{dx}{2y},\quad
\Delta_E=-432.
\tag{977.1}
$$
The source is the original CM elliptic curve used to realize the level-nine Hecke characters. Its differential gives Weierstrass invariants $g_2=0,g_3=-4$. This is not the $g_3=4$ choice used for the rational coefficient in R974; that change was separately calibrated there.

Choose the complex period generator defining the Robert value in R976 and put $P=\Omega_E/p$. Let
$$
C=\langle P\rangle\subset E[p],\qquad
\phi_C:E\longrightarrow E_C=E/C.
$$
Over characteristic zero define the unique target invariant differential by
$$
\phi_C^*\omega_C=\omega.
\tag{977.2}
$$
This target differential is generally not a primitive differential of a good integral model at $p$. Define
$$
D_C=\frac{\Delta(E_C,\omega_C)}{\Delta(E,\omega)}.
\tag{977.3}
$$
Rescaling $\omega$ rescales $\omega_C$ by the same factor, so the weight-twelve factors cancel. Thus $D_C$ is a modular function of the coarse cyclic-isogeny datum $(E,C)$, independent of a choice of Weierstrass coordinates or a scalar multiple of the source differential.

The coarse CM datum is defined over the actual ring class field
$$
L=H(\mathbb Z+p\mathcal O_K)
$$
of R972. One can see its field directly from the ray parameter: nonzero CM $p$-division parameters form $\mathbb F_{p^2}^{\times}$; quotienting by the source automorphisms $\mu_6$ gives the ray field $R=H_{(p)}$, and passing from a point to its cyclic $\mathbb F_p$-line further quotients by $\mathbb F_p^{\times}$. The stabilizer is exactly $\mathbb F_p^{\times}\mu_6$, the group defining $L$ in (976.3). The quantity (977.3) is invariant under these source automorphisms because both discriminants acquire the same weight-twelve scalar. Consequently
$$
D_C\in L^\times.
\tag{977.4}
$$
For an analytic check of the differential convention, if the source lattice is $\Omega_E(\mathbb Z+\tau\mathbb Z)$ and $C=\langle\Omega_E/p\rangle$, then the target lattice with pullback differential $dz$ is
$\Omega_E(p^{-1}\mathbb Z+\tau\mathbb Z)$. Hence
$$
D_C=p^{12}\frac{\Delta(p\tau)}{\Delta(\tau)}.
\tag{977.5}
$$
The factor $p^{12}$ belongs to this exact normalization and must not be discarded.

## 2. The fixed degree-forty-nine function

On any short Weierstrass model with invariant differential $dx/(2y)$, let $\psi_7$ be the ordinary odd division polynomial with leading term $7x^{24}$. Set
$$
F_7(E,Q)=\frac{\Delta(E)^4}{\psi_{7,E}(Q)}.
\tag{977.6}
$$
It has divisor $49[O]-[7]^*[O]$. If $t=-x/y$ at the origin, then
$$
F_7(E,t)=\frac{\Delta(E)^4}{7}t^{48}(1+O(t)).
\tag{977.7}
$$
Scholl's Kato--Siegel/Robert normalization gives two global sign choices with this divisor and discriminant normalization. Either choice has the exact norm distribution along odd-degree isogenies prime to seven; the two signs behave identically because the isogeny degree is odd. This is the general integer-$D$ argument already used at $D=11$ in R198 and R708. At $D=7$ it reads
$$
\prod_{Q\in C}F_7(E,Z+Q)
=F_7(E_C,\phi_C Z).
\tag{977.8}
$$
The equality is an identity of rational functions where the evaluations are defined, so it can be compared at the origin by leading terms.

The Robert function in R976, after scaling the lattices by $\Omega_E/p$, is $F_7(E,P)$ up to a twelfth root of unity. This is exactly the discriminant normalization of Scholl §1.2, Remark (v), already used in R189: for the auxiliary finite subgroup $E[7]$, its twelfth-power constant is
$$
\frac{\Delta(E)^{49}}{[7]^*\Delta(E)}
=\frac{\Delta(E)^{48}}{7^{12}}.
\tag{977.9}
$$
The product description of the odd division polynomial then gives (977.6), with leading coefficient (977.7). We retain the possible twelfth root here rather than fixing it by an unstated convention. It disappears from every $p$-adic logarithm in this note, since $p>3$.

## 3. The exact ray-to-ring-class multiplicity

The kernel of the ray-to-ring-class map is
$$
\operatorname{Gal}(R/L)
=(\mathbb F_p^{\times}\mu_6)/\mu_6
\simeq\mathbb F_p^{\times}/\{\pm1\}.
\tag{977.10}
$$
The invariance of $F_7$ under source $\mu_6$ follows either from its Robert origin or from (977.6): $\psi_7$ has weight $48$, divisible by six, and so does $\Delta^4$. Thus the norm of its value traverses the points $[u]P$ once for $u\in\mathbb F_p^{\times}/\{\pm1\}$. Inverting the arithmetic ray action merely permutes this index set and introduces no factor.

The norm $V_7$ of (976.6) consequently satisfies
$$
V_7=\xi\prod_{Q\in(C\setminus\{O\})/\{\pm1\}}F_7(E,Q),
\qquad \xi^{12}=1.
\tag{977.11}
$$
The function is even. Squaring (977.11) gives one copy of every nonzero kernel point, rather than two copies of the whole ray norm:
$$
V_7^2=\xi^2\prod_{Q\in C\setminus\{O\}}F_7(E,Q).
\tag{977.12}
$$
Now let $Z$ tend to the origin in (977.8). By (977.2), the parameter on the target pulls back to the source parameter with leading coefficient one. Comparing (977.7) on the two sides yields
$$
\prod_{Q\in C\setminus\{O\}}F_7(E,Q)=D_C^4.
\tag{977.13}
$$
In particular,
$$
\boxed{\quad V_7^2=\xi^2D_C^4,\quad \xi^{12}=1.\quad}
\tag{977.14}
$$
Keeping the same fixed arithmetic $\sigma=\operatorname{Frob}_{(2+s)}$ as R976 and applying $\sigma-1$ gives the exact logarithmic identity
$$
\boxed{\quad
\log U_7=2\log\left(\frac{D_C^\sigma}{D_C}\right).
\quad}
\tag{977.15}
$$
The arguments of these logarithms are local units. A root-of-unity convention cannot alter (977.15).

## 4. The discriminant has exactly four powers of the original uniformizer

Fix the same local embedding and Kummer root as R972:
$$
\pi^{p+1}=-p,\qquad \rho=\pi^3,\qquad
\rho^m=-p,\qquad m=(p+1)/3.
\tag{977.16}
$$
Normalize $v_p(p)=1$ and $v_\rho(\rho)=1$, so $v_\rho=m v_p$ on $L_{\mathfrak P}$.

The fixed source curve $E$ has good supersingular reduction at every original inert $p$. Its formal group has height two. Therefore every nonzero $p$-division parameter satisfies
$$
v_p(t(Q))=\frac1{p^2-1}.
\tag{977.17}
$$
For clarity, this is a statement only about the fixed CM elliptic curve $E$, not about the high-character factor of an Igusa Jacobian. It follows directly from the Newton polygon of $[p](T)/T$: the constant term is $p$, the first nonzero term modulo $p$ has degree $p^2-1$ and unit coefficient, and all intervening coefficients are divisible by $p$. The connected height-two $p$-torsion has exactly these $p^2-1$ nonzero formal roots.

Because seven and $\Delta_E$ are units and the power series in (977.7) has unit constant term, (977.17) gives
$$
v_p(F_7(E,Q))=\frac{48}{p^2-1}.
$$
There are $(p-1)/2$ factors in (977.11). Thus
$$
v_p(V_7)=\frac{24}{p+1},\qquad
v_\rho(V_7)=8.
\tag{977.18}
$$
Taking valuations in (977.14) now proves
$$
\boxed{\quad v_\rho(D_C)=4,\qquad
\delta_p:=\frac{D_C}{\rho^4}\in\mathcal O_{L_{\mathfrak P}}^\times.\quad}
\tag{977.19}
$$
This exact exponent is not inferred from an arbitrary choice of a primitive differential on the quotient. It uses the prescribed pullback differential (977.2).

## 5. The two actual logarithm coefficients

The ratio $\sigma\rho/\rho$ is an $m$-th root of unity. Its logarithm is zero. After removing Teichmüller residue factors from $\delta_p$, equations (977.15) and (977.19) give
$$
\log U_7=2(\sigma-1)\log\langle\delta_p\rangle.
\tag{977.20}
$$
As in R976, the ramification degree $m<p-1$ makes this ordinary logarithm integral. Define the finite coefficients by
$$
\log\langle\delta_p\rangle
\equiv\sum_{j=1}^{m-1}d_j\rho^j\pmod p,
\qquad d_j\in\mathbb F_{p^2}.
\tag{977.21}
$$
Write $\sigma\rho=\eta\rho$, with $\eta\in\mu_m$. Since $\sigma$ fixes $K_{\mathfrak p}$, it fixes the coefficients in (977.21). Comparing with R976's coefficients $B_j$ gives
$$
B_j=2(\eta^j-1)d_j.
\tag{977.22}
$$
For $b=a/3$ and $\chi=\chi_a$, the original reciprocity convention gives $\chi(\sigma)=\eta^{-b}$. On the two canonical embedding components, $\eta^p=\eta^{-1}$. Hence the actual coordinates of R976 satisfy
$$
\boxed{\quad
\gamma_0=2(\chi(\sigma)-1)d_b^p,
\qquad
\gamma_1=2(\chi(\sigma)-1)d_{m-b}.
\quad}
\tag{977.23}
$$
The common factor is a unit by (976.9)--(976.10). Thus the new concrete interface is
$$
\boxed{\quad
d_b\ne0,\qquad
\text{the original complete trace is nonzero}
\iff d_{m-b}\ne0.
\quad}
\tag{977.24}
$$
The unknown is the coefficient of degree $m-1$ when $r=2$, and degree $m-3$ when $r=8$, in the actual normalized discriminant unit (977.19).

## 6. Boundaries of the result

The cyclic subgroup, quotient, differential, field of definition, and uniformizer exponent are all specified. The formula gives an actual modular source to compare with a quasi-canonical CM deformation or a Gauss--Manin expansion. It does not identify the Kummer uniformizer $\rho$ with a flat or Serre--Tate coordinate, nor assert that the two indicated coefficients are equal or conjugate. The ramification degrees distinguishing the two Fontaine--Laffaille lines in R972 remain in force.

Likewise, no height-two statement about the source elliptic curve in (977.17) proves that the separate Igusa character factor has height two. The latter assertion is the unknown high-coordinate nonvanishing under study.

The generic Robert norm and the general discriminant normalization are old inputs here, already used in R189/R198/R708. The new conclusion is their specialization to the exact $D=7$ global source of R976, the ray-to-ring-class half-kernel multiplicity, the exponent $4$ in the fixed local parameter, and the resulting coefficient formula (977.23).

## 7. Sources

- R189, especially its exact finite-subgroup discriminant normalization following (189.15).
- R198 §1.1, especially (198.4), and R708 §5, for the exact normalized odd-isogeny distribution, including its sign.
- A. J. Scholl, *An introduction to Kato's Euler systems*, LMS Lecture Note Series **254** (1998), 379--460, §1.2, Theorem 1.2.1(iii), Remarks (iv)--(v), and the proof on printed pp. 385--386. [Author PDF](https://www.dpmms.cam.ac.uk/~ajs1005/preprints/euler.pdf).
- R972 and R976 for the actual ring class field, arithmetic/global versus geometric/local reciprocity conventions, fixed Robert unit, and the two canonical local coordinates.
