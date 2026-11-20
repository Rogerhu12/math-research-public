# R972 — The two actual Artin–Hasse lines and the original ring-class regulator

Date: 2026-11-20. Maintenance session: serre-public-astra-20261120-de0a3e3b. Authoring agent: handoff_audit; independently audited by root. **Status: proved criterion for both original rows.** No new mathematical computation is executed in this note.

The original low-weight unit determines one coordinate of an actual global unit. The high-weight congruence ideal, and hence R970's original whole supersingular trace, is a unit exactly when the other coordinate of that same unit is nonzero. The coordinates below are explicit coefficients in the completion of the conductor-\(p\) ring class field. No nonvanishing of the second coordinate is claimed.

This note supplies the local Hodge–Tate, reciprocity, Artin–Hasse, integral deformation, global dimension, and class-group arguments. A choice of a particular Robert elliptic unit as a generator is a separate source calculation; it is not needed for the theorem here.

## 1. Original rows, characters, and statement

Retain precisely R970's two rows:
\[
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
(r,w)=
\begin{cases}
(2,p-1),&p\equiv11\pmod{12},\\
(8,p-7),&p\equiv5\pmod{12}.
\end{cases}
\tag{972.1}
\]
Put
\[
a=r+1\in\{3,9\},\qquad n=w-1=p+1-a,\qquad
m=(p+1)/3,\qquad b=a/3\in\{1,3\}.
\tag{972.2}
\]
In particular \(p=3m-1\), \(a=3b\), \(n=3(m-b)\), and \(p>2a\). The original label remains \(h=(p+1+r)/2\); no half-period or tame marking is changed.

Let \(K=\mathbf Q(\sqrt{-3})\), \(k=\mathbf F_{p^2}\), and \(\mathcal O=W(k)\). For \(j=a,n\), let \(\Psi_j\) be the \(p\)-adic Galois character attached to the original primitive level-nine Hecke character
\[
\Xi_{j+1}((\alpha))=\alpha^j\epsilon_3(\alpha),
\qquad
f_{j+1}=F_{j+1}\in S_{j+1}(\Gamma_0(9)).
\tag{972.3}
\]
Thus \(\Psi_j\) takes the value in (972.3) at arithmetic Frobenius, for ideals prime to \(3p\). Both forms have trivial nebentypus and rational integral coefficients. We use the positive Hodge–Tate convention in which the cyclotomic character \(\epsilon\) has weight one. The two embeddings of \(K_p=\mathbf Q_{p^2}\) are ordered so that \(\Psi_a\) has labelled weights \((a,0)\).

Define
\[
\chi=\overline{\Psi_a/\Psi_a^c},\qquad
\overline W=\operatorname{Ind}_{G_K}^{G_{\mathbf Q}}k(\chi).
\tag{972.4}
\]
Here \(c\) is complex conjugation. The actual residual adjoint representation splits as
\[
\operatorname{ad}^0\overline\rho_{f_{a+1}}
=k(\chi_K)\oplus\overline W.
\tag{972.5}
\]
The integral CM splitting over the unramified coefficient ring gives this same residual lattice. There is no period comparison in (972.5).

Let \(L/K\) be the conductor-\(p\) ring class field of the order \(\mathbf Z+p\mathcal O_K\). Write \(\Delta=\operatorname{Gal}(L/K)\). Section 2 proves that \(\chi\) is faithful on this group and \(|\Delta|=m\), in both original rows. Let \(\mathfrak P\) be its unique prime above \(p\). Fix
\[
\pi^{p+1}=-p,\qquad \varpi=\pi^3,\qquad
L_{\mathfrak P}=K_p(\varpi),\qquad \varpi^m=-p.
\tag{972.6}
\]
The residue field is \(k_0=\mathbf F_{p^2}\); we distinguish this residue copy from the coefficient copy \(k\). Let \(\tau_0:k_0\to k\) be the chosen embedding and \(\tau_1=\tau_0\circ\operatorname{Frob}_p\). Let \(\lambda_i\in k_0\otimes_{\mathbf F_p}k\) be the canonical idempotent whose \(\tau_i\)-coordinate is one and whose other coordinate is zero.

All isotypic components in this note have the following fixed meaning:
\[
X^\chi=e_\chi(X\otimes_{\mathbf Z_p}\mathcal O),\qquad
e_\chi=\frac1m\sum_{\delta\in\Delta}
\widetilde\chi(\delta)^{-1}\delta,
\tag{972.7}
\]
where \(\widetilde\chi\) is the Teichmüller lift. Thus \(\delta\) acts on \(X^\chi\) by \(\widetilde\chi(\delta)\), not its inverse.

**Theorem.** For every original prime in (972.1), the following statements hold.

1. The two actual residual short-crystalline conditions on
   \(H^1(K_p,k(\chi))\) are different complementary lines \(L_0,L_1\), with an explicit dual Artin–Hasse basis \(u_0,u_1\):
   \[
   L_{\rm low}=L_0=k c_0=\{z:z(u_1)=0\},\qquad
   L_{\rm high}=L_1=k c_1=\{z:z(u_0)=0\}.
   \tag{972.8}
   \]
   The original low and high Hodge–Tate conditions, including the swap of CM characters, are checked in Sections 3–4.
2. Put \(S=\{p,\infty\}\) on \(K\), and
   \(\mathcal H=H^1(G_{K,S},k(\chi))\). Then
   \[
   \dim_k\mathcal H=1,\qquad H^2(G_{K,S},k(\chi))=0,
   \qquad \operatorname{loc}_p:\mathcal H\hookrightarrow H^1(K_p,k(\chi)).
   \tag{972.9}
   \]
   The low local condition meets this image in zero. In particular there is a unique \(z\in\mathcal H\) normalized by
   \[
   z(u_1)=1.
   \tag{972.10}
   \]
3. The \(\chi\)-part of the \(p\)-class group of \(L\) is zero. The global unit module
   \(\mathcal E^\chi=(\mathcal O_L^\times\otimes_{\mathbf Z}\mathcal O)^\chi\)
   is free of rank one and has a primitive nonzero image in the local unit module. For any generator \(e\) of this global unit module, write its residual local class as
   \[
   \overline e=\gamma_0u_0+\gamma_1u_1.
   \tag{972.11}
   \]
   Then
   \[
   \gamma_0\ne0,\qquad z(u_0)=-\gamma_1/\gamma_0.
   \tag{972.12}
   \]
4. With the complete classical high-weight congruence ideal \(\eta_{F_w}\) and the unchanged original whole trace \(S_{\rm orig}\) of R970,
   \[
   \boxed{\quad
   S_{\rm orig}\ne0
   \iff\eta_{F_w}=\mathcal O
   \iff z(u_0)\ne0
   \iff\gamma_1\ne0.
   \quad}
   \tag{972.13}
   \]
   For \(r=2\), R965 also makes these equivalent to the nonvanishing of the actual formal-height coefficient \(\kappa\). No equality of \(\kappa\) or \(S_{\rm orig}\) with \(\gamma_1\) up to a specified scalar is claimed.
5. Both coordinates in (972.11) are explicit finite coefficients. The ordinary local logarithm is integral on principal units of \(L_{\mathfrak P}\), and modulo \(p\) one has exactly
   \[
   e_\chi\log\langle e\rangle
   =\gamma_0\lambda_1\varpi^b+
     \gamma_1\lambda_0\varpi^{m-b}
   \quad\text{in}\quad
   (k_0[\varpi]/(\varpi^m))\otimes_{\mathbf F_p}k.
   \tag{972.14}
   \]
   The angle brackets mean removal of the local Teichmüller residue, extended linearly and continuously to the completed unit module. Thus the remaining assertion is the nonvanishing of the \(\tau_0\)-coefficient at degree \(m-b\) of the logarithm of an actual global unit; the known low unit controls degree \(b\) in the other residue embedding.

## 2. The precise common ring class field

For a principal ideal prime to \(3p\), the ratio of the two finite conductor characters in (972.3) is one. Hence
\[
\chi(\operatorname{Frob}_{(\alpha)}^{\rm arith})
=(\alpha/\bar\alpha)^a\pmod p.
\tag{972.15}
\]
This formula is independent of the generator: \(a\) is a multiple of three and \(\alpha/\bar\alpha\) changes by a sixth-root quotient whose \(a\)-th power is one. The ratio character is unramified at three, so (972.15) defines a character of conductor dividing \((p)\), not of conductor \(3p\). Its local value at a uniformizer of \(K_3\) is determined in Section 5.

Because \(p\) is inert and \(K\) has class number one, the ring class group of the order \(\mathbf Z+p\mathcal O_K\) is
\[
\operatorname{Pic}(\mathbf Z+p\mathcal O_K)
\simeq
\mathbf F_{p^2}^{\times}/(\mathbf F_p^{\times}\mu_6),
\qquad
\left|\operatorname{Pic}(\mathbf Z+p\mathcal O_K)\right|
=\frac{p+1}{3}=m.
\tag{972.16}
\]
The map \(x\mapsto(x/x^p)^a\) kills \(\mathbf F_p^\times\mu_6\). Its image has order
\[
\frac{p+1}{\gcd(a,p+1)}=\frac{p+1}{3}=m,
\tag{972.17}
\]
since \(p\equiv2,5\pmod9\) implies \(v_3(p+1)=1\). Thus it is faithful on (972.16). This proves that the field cut out by \(\chi\) is exactly \(L\), and that the two values \(a=3,9\) give the same field, with different faithful characters.

The inertia character at \(p\) already has this full order. Therefore \(p\) has a unique prime in \(L\), with ramification index \(m\) and residue degree one over \(K_p\). The group \(\Delta\) has order prime to \(p\), and all its character values belong to \(\mathcal O\).

For local reciprocity we use DDR's geometric convention: \(\operatorname{Art}_{K_p}(p)\) is geometric Frobenius and the fundamental character on a unit is its residue. This is compatible with (972.15), which used arithmetic Frobenius on ideals. In these conventions
\[
\chi|_{I_p}=\omega_0^{a(1-p)},\qquad
\chi(\operatorname{Art}_{K_p}(p))=1.
\tag{972.18}
\]
Indeed the norm-one ratio is one on the scalar uniformizer \(p\). If \(\pi^{p+1}=-p\), then \(\omega_\pi(g)=g\pi/\pi\) satisfies
\[
\chi=\omega_\pi^{-a}.
\tag{972.19}
\]
Its kernel in \(\operatorname{Gal}(K_p(\pi)/K_p)\) is \(\mu_3\), proving (972.6). One may also check the unramified normalization directly: the norm of \(\pi\) from this even-degree extension is \(p\), so \(\operatorname{Art}_{K_p}(p)\) acts trivially on it.

## 3. The actual high-to-low residual identification

The original forms satisfy the following identification of Galois representations, not merely an equality of projective inertia types:
\[
\overline\rho_{f_{n+1}}\otimes\bar\epsilon^{a-1}
\simeq\overline\rho_{f_{a+1}}.
\tag{972.20}
\]
On \(G_K\) the two CM lines are exchanged:
\[
\overline\Psi_n\bar\epsilon^{a-1}=\overline\Psi_a^c,
\qquad
\overline\Psi_n^c\bar\epsilon^{a-1}=\overline\Psi_a.
\tag{972.21}
\]
To verify this on an ideal \((\alpha)\) prime to \(3p\), use \(n+a-1=p\) and the inert congruence \(\alpha^p=\bar\alpha\pmod p\):
\[
\alpha^n\epsilon_3(\alpha)(\alpha\bar\alpha)^{a-1}
\equiv\bar\alpha^a\epsilon_3(\bar\alpha)\pmod p.
\tag{972.22}
\]
Equality of the unramified characters follows at all such ideals and hence globally. Conjugating proves the other identity. In particular the high off-diagonal ratio in the order transported to \(\chi\) is \(\Psi_n^c/\Psi_n\), not \(\Psi_n/\Psi_n^c\).

The relevant labelled Hodge–Tate weights are therefore

| Actual source | First CM line | Second CM line | Their quotient |
| --- | --- | --- | --- |
| Low \(f_{a+1}\) | \((a,0)\) | \((0,a)\) | \((a,-a)\) |
| High \(f_{n+1}\), twisted and swapped as in (972.21) | \((a-1,p)\) | \((p,a-1)\) | \((-n,n)\) |

The high twist does not change the adjoint deformation problem. Its original untwisted weights are \((0,n)\) with \(n\le p-2\), so this is still the actual short-crystalline deformation condition. It is not a condition obtained by asking a weight-\(p\) character to lie in an unrelated Fontaine–Laffaille interval.

## 4. Explicit Artin–Hasse basis and both ramification conventions

The tame signature of (972.18), in DDR's notation, is
\[
(a_0,a_1)=(a-1,p-a),
\qquad
a(1-p)\equiv(a-1)+p(p-a)\pmod{p^2-1}.
\tag{972.23}
\]
It is primitive and generic: \(1<a_0<a_1<p-1\). Thus DDR §8.2, Case I applies without an exceptional trivial, cyclotomic, or non-generic extension.

Put
\[
E_{\rm AH}(T)=\exp\left(\sum_{j\ge0}\frac{T^{p^j}}{p^j}\right).
\tag{972.24}
\]
For a positive valuation element \(t\), write
\(\varepsilon_t(x\otimes c)=E_{\rm AH}([x]t)\otimes c\), extended linearly to residue-field tensors and then to the multiplicative group modulo \(p\)-th powers. Here \([x]\) is the Teichmüller lift. Define
\[
u_0=\varepsilon_{\pi^a}(\lambda_1)
=\varepsilon_{\varpi^b}(\lambda_1),\qquad
u_1=\varepsilon_{\pi^n}(\lambda_0)
=\varepsilon_{\varpi^{m-b}}(\lambda_0).
\tag{972.25}
\]
They are elements of the \(\chi\)-isotypic local units, equivalently of
\[
\mathcal U_\chi=
\left(L_{\mathfrak P}^{\times}/(L_{\mathfrak P}^{\times})^p
\otimes_{\mathbf F_p}k(\chi^{-1})\right)^\Delta.
\tag{972.26}
\]
The same space computed in \(K_p(\pi)\) is identified with it by restriction and the norm divided by three. The displayed representatives already lie in \(L_{\mathfrak P}\), since \(a,n\) are divisible by three; no uncertain norm scalar is needed for (972.25).

For clarity, the two different residue embeddings are forced. If \(\delta\varpi=\xi\varpi\), then \(\chi(\delta)=\xi^{-b}\). The \(\tau_1\)-component of degree \(b\) has eigenvalue \(\xi^{pb}=\xi^{-b}\), while the \(\tau_0\)-component of degree \(m-b\) has eigenvalue \(\xi^{m-b}=\xi^{-b}\). Thus both vectors have character \(\chi\).

DDR Theorem 5.1 and §8.2 give that \(u_0,u_1\) form a basis. Local class field theory gives the perfect pairing
\[
H^1(K_p,k(\chi))\times\mathcal U_\chi\longrightarrow k.
\tag{972.27}
\]
It is the equivariant homomorphism pairing: a class is a homomorphism satisfying
\(z(\delta x)=\chi(\delta)z(x)\). Let \(c_0,c_1\) be the exact dual basis, so \(c_i(u_j)=\delta_{ij}\).

To verify the crystalline identification, substitute (972.23) in DDR's Case I table. For \(J=\{0\}\), its \(d\)- and \(b\)-labels are
\[
d=(p-1,p-a-1),\qquad (b_0,b_1)=(a,a).
\tag{972.28}
\]
For \(J=\{1\}\), they are
\[
d=(a-2,p-1),\qquad (b_0,b_1)=(n,n).
\tag{972.29}
\]
These are the actual two rows of the preceding table. For example, adding the common labelled twist \((p-1,p-a-1)\) to the low pair makes the second character's residual character one and gives (972.28). Adding the common twist \((-1,p-a)\) to the transported high pair does the same and gives (972.29). The first quotient has positive labelled difference only at embedding zero; the second has positive labelled difference only at embedding one. No residual common twist or interchange is omitted.

Calegari–Emerton–Gee–Mavrides, Theorem 3.5.3, proves that these crystalline extension spaces equal DDR's Artin–Hasse spaces. We use its proved local theorem, not DDR's then-conjectural formulation. It follows that
\[
L_{\rm low}=kc_0,\qquad L_{\rm high}=kc_1,
\tag{972.30}
\]
as asserted in (972.8). Passing between the split characters over \(K_p\) and the induced representation over \(\mathbf Q_p\) preserves this statement: restriction splits the actual CM filtered module, its two off-diagonal extensions are conjugate, and induction/descent identifies their fixed-determinant extension condition with (972.27).

Here are the precise ramification shifts. DDR §3.1 defines
\[
\operatorname{Fil}^sH^1(K_p,k(\chi))
=\bigcap_{u>s-1}\ker\bigl(H^1(K_p,k(\chi))\to H^1(G_{K_p}^u,k(\chi))\bigr).
\tag{972.31}
\]
The two signature integers are
\[
N_0=(p-1)n,\qquad N_1=(p-1)a,\qquad N_1<N_0.
\tag{972.32}
\]
DDR §8.2(11) gives
\[
L_0=\operatorname{Fil}^{1+a/(p+1)}H^1
=\operatorname{Fil}^{<1+n/(p+1)}H^1,
\tag{972.33}
\]
and the whole two-dimensional space first occurs at
\(\operatorname{Fil}^{1+n/(p+1)}\). Therefore the upper ramification break of a nonzero class in \(L_0\) is
\[
\frac{a}{p+1}=\frac bm,
\tag{972.34}
\]
whereas that of a nonzero class in \(L_1\) is
\[
\frac{n}{p+1}=1-\frac bm.
\tag{972.35}
\]
The filtration index has the extra one; the upper break does not. Equivalently \(L_0\) consists of classes killed on \(G_{K_p}^{n/(p+1)}\). Although \(L_1\) is a specified different line, the ramification filtration alone does not distinguish it from every other line outside \(L_0\).

## 5. Low integral Hecke block and every DFG hypothesis

The following is a consequence of existing complete-space results, not a new finite eigenvalue experiment:
\[
\mathbb T_{a+1,\mathfrak m_{f_{a+1}}}=\mathcal O,
\qquad a=3,9.
\tag{972.36}
\]
For weight four, R918 proves that the full original integral tame cusp module is free of rank one and reduces onto its whole residual space. For weight ten, R942 proves that the complete double-\(T_5\) zero-primary space is a single line at every \(p\ge41\): its other eigenvalues are \(147456=2^{14}3^2\) and \(666^2\), whose prime factors are at most 37. The full CM maximal-ideal block is contained in that one-dimensional primary space and contains the original CM vector, so it also has dimension one.

To pass to the classical level-nine algebra in (972.36), reuse R970 §§3.2–5's actual full-component graph comparison. Its argument applies unchanged at either low weight: the full-six line bundle has degree \(6(a+1)-12>0\), hence has base change; the same unit averaging projector acts on both pairing components; the original CM system is fixed by the quadratic self-twist; and the local types at two and three are the same. Every congruent primitive level-nine representation contributes one full graph-invariant line. In particular the conjugate component is not counted twice, and the single-step inert correspondence is not replaced by an endomorphism of one marking. Thus the classical low block has rank one, proving (972.36).

We now apply the minimal short-crystalline deformation theorem of Diamond–Flach–Guo (DFG), with fixed determinant. The relevant source is DFG §3.1, especially the precise deformation functor on printed p. 717, its cotangent/Selmer identification (70), and the proved isomorphism \(R^\varnothing\simeq T^\varnothing\) on p. 720; §3.2 constructs these objects from modular forms. Its assumptions hold here as follows.

**Weight and coefficient primes.** Both low weights are in \([2,p-1]\), both high weights are in the same interval, and \(p\nmid9k!\) for each weight \(k\) under consideration. Their original crystalline intervals have width at most \(p-2\). DFG uses the geometric dual normalization; dualizing or Tate twisting does not alter the fixed-determinant adjoint extension problem.

**Minimality among twists.** At three the local tame inertia eigencharacters of the original two-dimensional representation have order four, the two exponents two and six on \(\mathbf F_9^\times\) used in R970. A tame character of \(\mathbf Q_3^\times\) has inertia order at most two and cannot make either of these characters trivial. A ramified character of higher conductor cannot lower this tame conductor. Thus conductor exponent two is minimal among twists; it survives reduction at \(p>3\). There is no ramification at other finite primes away from \(p\). Consequently the minimal deformations in DFG have primitive level exactly nine, and the original forms are minimal lifts. This checks the minimality condition on the residual representation itself.

**Quadratic-cyclotomic irreducibility.** Let \(F=\mathbf Q(\sqrt{(-1)^{(p-1)/2}p})\). Its completion at \(p\) is ramified quadratic. The inertia ratio in the induced local CM representation has order \(m=(p+1)/3\). After restricting to \(G_{F_p}\), the inertia ratio still has order \(m/2\ge7\), while the unramified quadratic Frobenius still exchanges the two lines. Hence the local restriction is absolutely irreducible, and so is the global restriction to \(G_F\). This is DFG's actual Taylor–Wiles hypothesis. The theorem used here has no additional non-CM or large-image assumption.

**Integral representation and local condition.** The CM representation is induced from its actual integral character, and its two lines over \(K_p\) split over \(\mathcal O\). Absolute irreducibility makes the stable lattice unique up to homothety; taking its adjoint removes that homothety. DFG Proposition 2.2 identifies the torsion short-crystalline extension condition with the reduction of the characteristic-zero crystalline condition. Thus its residual tangent condition is precisely (972.30), with the integral characters and their labelled weights already checked. No Betti, de Rham, or Manin-period lattice is substituted for this Galois lattice.

It follows from DFG and (972.36) that the actual low fixed-determinant minimal residual Selmer group is zero. Its off-diagonal summand therefore satisfies
\[
\operatorname{Sel}_{\rm low}(\overline W)=0.
\tag{972.37}
\]
This is an all-original-prime assertion here, rather than Weston's unspecified almost-all-prime exceptional set.

We also record the exact local calculation at three, needed in the global argument. The character \(\chi\) is unramified on \(K_3\). At its uniformizer \(\sqrt{-3}\), the ratio is
\((\sqrt{-3}/(-\sqrt{-3}))^a=-1\). Equivalently this follows from global reciprocity applied to the same principal element; the sign is independent of the arithmetic/geometric convention. Hence
\[
\overline W|_{G_{\mathbf Q_3}}
=\operatorname{ur}(-1)\otimes(1\oplus\chi_K).
\tag{972.38}
\]
There are no invariants. The Tate-dual twist has no invariants either: its unramified factor has Frobenius \(-3\) or \(-3^{-1}\), neither one at \(p\ge41\), and the other factor is ramified quadratic. Local Tate duality and the local Euler characteristic formula give
\[
H^1(\mathbf Q_3,\overline W)=0.
\tag{972.39}
\]
Thus the three-adic minimal condition contributes no hidden off-diagonal constraint. Shapiro identifies the remaining global problem with cohomology of \(k(\chi)\) over \(K\), unramified outside \(p\).

## 6. The global relaxed line is really one-dimensional

Let \(\mathcal H\) be as in (972.9). Its localization kernel is contained in the low Selmer group: a class whose localization is zero satisfies \(L_0\), and every other local condition is the one already imposed in \(G_{K,S}\), with (972.39) at three. By (972.37),
\[
\ker(\operatorname{loc}_p|_{\mathcal H})=0.
\tag{972.40}
\]
Moreover \(\chi\ne1,\bar\epsilon\) locally. Thus local Tate duality gives \(H^0=H^2=0\), and the local Euler characteristic gives
\[
\dim_k H^1(K_p,k(\chi))=2.
\tag{972.41}
\]

The global Euler characteristic for the imaginary quadratic field \(K\) gives
\[
\dim_k H^1(G_{K,S},k(\chi))
-\dim_k H^2(G_{K,S},k(\chi))=1,
\tag{972.42}
\]
since the global invariants vanish. This is Milne, *Arithmetic Duality Theorems*, I.5.1, applied to this one-dimensional \(k\)-representation; its single complex place contributes \(-1\) to the additive characteristic. In particular \(\dim\mathcal H\ge1\).

If \(\dim\mathcal H=2\), its injective localization in (972.41) would be surjective and would meet \(L_0\) nontrivially, contradicting (972.37). Thus its dimension is one and (972.42) gives \(H^2=0\). This proves (972.9) without assuming Leopoldt, a unit generator, or any prior global dimension formula for the CM packet.

Its nonzero localized class is not in \(L_0\), so its value at \(u_1\) is nonzero. This proves the unique normalization (972.10).

## 7. The actual class-group direction and the global unit line

Write \(A_L=\operatorname{Cl}(L)[p^\infty]\). Since \(|\Delta|\) is prime to \(p\), inflation–restriction identifies global classes with \(\Delta\)-equivariant homomorphisms over \(L\). In particular a nonzero \(\chi\)-part of the class group gives a nonzero map
\[
\phi:A_L/pA_L\longrightarrow k,
\qquad \phi(\delta x)=\chi(\delta)\phi(x),
\tag{972.43}
\]
and hence a class in \(\mathcal H\) unramified everywhere over \(L\).

Its localization at \(p\) is zero. Indeed \(\Delta\) is entirely inertia at the unique prime \(\mathfrak P\), and acts trivially on its unramified pro-\(p\) Frobenius quotient. That quotient has no nontrivial \(\chi\)-isotypic direction. Equivalently \(H^1_{\rm ur}(K_p,k(\chi))=0\). The class (972.43) would therefore contradict (972.40). Consequently
\[
A_L^\chi=0.
\tag{972.44}
\]
This is the same \(\chi\) as on the units in (972.7), not \(\chi^{-1}\). Formula (972.43) fixes the direction explicitly. If one instead rewrites the problem by Kummer cohomology with \(\mu_p\), a cyclotomic dual twist appears; no such unannounced replacement is made here.

Let \(X_L\) be the maximal abelian pro-\(p\) Galois group over \(L\) unramified outside \(\mathfrak P\). Global class field theory gives the \(\chi\)-part of the exact sequence
\[
\mathcal E^\chi\longrightarrow
\mathcal U_{\mathfrak P}^\chi\longrightarrow
X_L^\chi\longrightarrow A_L^\chi\longrightarrow0,
\tag{972.45}
\]
where \(\mathcal U_{\mathfrak P}\) is the principal local unit group with its \(p\)-adic completion. The valuation term disappears in this nontrivial character: the unique prime is fixed by \(\Delta\). The same observation shows that using \(p\)-units rather than ordinary global units has no effect on this isotypic component.

The global unit representation has character the regular representation of \(\Delta\) minus its trivial representation. This follows from the logarithmic embedding on the \(m\) complex-place pairs of \(L\), on which \(\Delta\) acts regularly. Thus \(\mathcal E^\chi\) has rank one over \(\mathcal O\). There is no \(p\)-power root-of-unity torsion: the absolute degree \(2m<p-1\) precludes \(\mu_p\subset L\). The local module \(\mathcal U_{\mathfrak P}^\chi\) has rank two, as is also seen directly from Section 8.

By (972.44), reducing (972.45) modulo \(p\) gives a right-exact sequence. Its last quotient is dual, by the equivariant homomorphism pairing, to the one-dimensional space \(\mathcal H\). Hence the image of \(\mathcal E^\chi/p\) in the two-dimensional local unit space has dimension one. In particular it is nonzero and primitive. This establishes the local saturation rather than assuming it. It also implies that the rank-one integral unit map is injective and its image is a direct summand of the local rank-two lattice.

Every global class annihilates this global unit image by the reciprocity exact sequence. Thus for a generator \(e\) as in (972.11),
\[
0=z(\overline e)=\gamma_0z(u_0)+\gamma_1z(u_1)
=\gamma_0z(u_0)+\gamma_1.
\tag{972.46}
\]
If \(\gamma_0=0\), then \(\gamma_1\ne0\) by primitivity and (972.46) is impossible. This proves (972.12). Notice the direction: the low Selmer vanishing controls \(\gamma_0\), although its normalized global dual class is specified by the value on \(u_1\).

## 8. Exact finite logarithm formula

The true local ramification index is \(m=(p+1)/3<p-1\). Therefore the ordinary logarithm and exponential give mutually inverse integral isomorphisms
\[
\log:1+\varpi\mathcal O_{L_{\mathfrak P}}
\xrightarrow{\sim}\varpi\mathcal O_{L_{\mathfrak P}}.
\tag{972.47}
\]
This assertion concerns \(L_{\mathfrak P}\). It would not be a valid blanket assertion for all principal units of the auxiliary degree-\(p+1\) extension \(K_p(\pi)\).

Modulo \(p\), one has
\[
\mathcal O_{L_{\mathfrak P}}/(p)
\simeq k_0[\varpi]/(\varpi^m).
\tag{972.48}
\]
For a normalized principal unit \(v\), its logarithm in this ring is exactly the finite polynomial
\[
\log(v)\bmod p
=\sum_{j=1}^{m-1}\frac{(-1)^{j+1}}j(v-1)^j.
\tag{972.49}
\]
All denominators displayed are units. To check that omitted terms of the true logarithm cannot return at smaller order, normalize \(v_\varpi(\varpi)=1\), so \(v_\varpi(p)=m\). For \(j\ge m\),
\[
v_\varpi\left((v-1)^j/j\right)\ge j-mv_p(j)\ge m.
\tag{972.50}
\]
If \(p\nmid j\), this is immediate. If \(v_p(j)=t\ge1\), then \(j-mt\ge p^t-mt\ge p-m=2m-1\ge m\); the function on the right increases with \(t\). This proves (972.49) directly.

For the basis elements in (972.25),
\[
\log E_{\rm AH}([x]\varpi^b)
=\sum_{j\ge0}\frac{[x]^{p^j}\varpi^{bp^j}}{p^j}
\equiv[x]\varpi^b\pmod p.
\tag{972.51}
\]
Every term with \(j\ge1\) has \(\varpi\)-valuation at least
\(bp^j-mj\ge p-m\ge m\). The identical argument applies with \(b\) replaced by \(m-b\). Hence the normalization of the logarithm on the exact AH basis is
\[
\log(u_0)=\lambda_1\varpi^b,\qquad
\log(u_1)=\lambda_0\varpi^{m-b}\pmod p.
\tag{972.52}
\]

The principal-unit quotient modulo \(p\)-th powers maps by the logarithm to
\(\varpi\mathcal O_{L_{\mathfrak P}}/p\varpi\mathcal O_{L_{\mathfrak P}}\).
Passing further to (972.48) discards only the one graded term of degree \(m\); that term has trivial \(\Delta\)-character, so no information is lost in the nontrivial \(\chi\)-part. The valuation and Teichmüller factors also contribute no \(\chi\)-part modulo \(p\)-th powers.

One can independently see the two surviving monomials without invoking a dimension count. If \(\delta\varpi=\xi\varpi\), then \(\chi(\delta)=\xi^{-b}\). In the \(\tau_0\)-factor the unique index \(1\le j<m\) with this character is \(j=m-b\). In the \(\tau_1\)-factor the eigenvalue is \(\xi^{-j}\), so the unique such index is \(j=b\). This proves (972.14) and its exact coordinate normalization.

A different choice of \(\varpi\) or of basis in either one-dimensional coefficient line multiplies the corresponding coordinate by an explicitly nonzero field element. The zero criterion in (972.13) is unaffected. With (972.6) and the canonical idempotents fixed, (972.14) itself has no unspecified scalar.

## 9. High Selmer, the diagonal summand, and the original trace

The diagonal summand in (972.5) contributes no minimal short-crystalline Selmer class, for either weight. At \(p\) it is the nontrivial unramified quadratic character \(\chi_K\), and its weight-zero crystalline extension subspace is the unramified subspace
\[
H^1_{\rm ur}(\mathbf Q_p,k(\chi_K))
=k/(\chi_K(\operatorname{Frob}_p)-1)=0.
\tag{972.53}
\]
At the other finite primes minimality imposes the unramified condition; at three the corresponding local cohomology is already zero. Restricting to \(K\), a putative global diagonal class with localization zero at \(p\) is everywhere unramified. The class number of \(K\) is one, so it is zero. Thus the high residual minimal tangent Selmer group is precisely
\[
\operatorname{Sel}_{\rm high}
\simeq\{z'\in\mathcal H:\operatorname{loc}_p(z')\in L_1\}.
\tag{972.54}
\]

All DFG hypotheses for the actual high weight were checked in Section 5. Consequently its minimal fixed-determinant deformation ring is the complete classical primitive level-nine Hecke algebra localized at \(F_w\). A complete local \(\mathcal O\)-algebra with the \(\mathcal O\)-valued point given by \(F_w\) is \(\mathcal O\) if and only if this residual relative tangent space is zero: in the zero-tangent direction this follows from Nakayama applied to its augmentation ideal, and the converse is immediate. Equivalently, using R970's finite flat classical algebra and its rank-one CM generic factor,
\[
\eta_{F_w}=\mathcal O\iff\operatorname{Sel}_{\rm high}=0.
\tag{972.55}
\]

The space \(\mathcal H\) is a line. It lies in \(L_1\) exactly when its normalized generator \(z\) kills \(u_0\). Thus
\[
\operatorname{Sel}_{\rm high}=0
\iff z(u_0)\ne0
\iff\gamma_1\ne0,
\tag{972.56}
\]
by (972.12). R970 identifies \(\eta_{F_w}\) being a unit with the nonvanishing of the named original whole trace, including its full norm extension, original \(\zeta^2\) oldform phase, and determinant return. This proves (972.13). No eigenline-only multiplicity argument is used in this passage.

## 10. Why actual conjugation and Frobenius do not supply the missing unit

Complex conjugation carries the \(\chi\)-cohomology to the \(\chi^{-1}\)-cohomology. Coefficient Frobenius also carries \(\chi\) to \(\chi^{-1}\), since its values have order dividing \(p+1\). The resulting semilinear descent on the \(\chi\)-cohomology is the composite of these two operations, not complex conjugation alone.

It preserves each of the two actual lines. This can be checked on the local units: conjugation acts by residue Frobenius and sends \(\varpi\) to an \(m\)-th root of unity times \(\varpi\). Coefficient Frobenius exchanges the residue tensor idempotents a second time. Their composite therefore preserves each of
\[
k\lambda_1\varpi^b,\qquad
k\lambda_0\varpi^{m-b},
\tag{972.57}
\]
with its own possible nonzero semilinear scalar, and hence preserves the two dual lines. Independently, the two different upper breaks in (972.34–35) exclude an interchange by any symmetry preserving the actual ramification filtration.

Thus the genuine dihedral/Frobenius symmetry does not identify the missing coefficient \(\gamma_1\) with the already nonzero coefficient \(\gamma_0\). The conclusion is stronger than a statement about arbitrary deformation nodes: the exact original characters, their two different crystalline subspaces, their common ring class field, their global unit line, and the unexplained coefficient have all been specified.

## 11. What remains and what this does not claim

The remaining all-prime assertion on this route is now the concrete statement
\[
\left[\lambda_0\varpi^{m-b}\right]
e_\chi\log\langle e\rangle\ne0
\qquad\text{for every original prime,}
\tag{972.58}
\]
where \(e\) is any generator of the actual global unit \(\chi\)-lattice in the conductor-\(p\) ring class field. The coefficient at \(\lambda_1\varpi^b\) is already proved nonzero. A finite Gras theorem and a correctly normalized Robert generator can make \(e\) a named elliptic unit; they do not by themselves prove (972.58).

No unnormalized CM special value, ordinary local theorem, or comparison between arbitrary CM periods and Manin periods is inserted into the argument. No scalar equality between (972.58) and the original trace is asserted. In the \(r=2\) row the separately proved exact scalar calibration remains R965's \(\kappa=-g_pS_{\rm orig}^p/432\).

Even a proof of (972.58) for every prime would settle only this original whole-trace nonvanishing route. The same-label \(Q'\) failures of R945 and the integral height contents and source comparison of the main problem remain separate. They are not removed by this local-global criterion.

## Primary references checked

1. L. Dembélé, F. Diamond, and D. P. Roberts, *Serre weights and wild ramification in two-dimensional Galois representations*, arXiv:1603.07708v2. [Primary preprint](https://arxiv.org/pdf/1603.07708). §§2.1–2.2 fix reciprocity and Hodge–Tate conventions; §3.1 defines the shifted filtration; Theorem 5.1 gives the AH basis; §8.2, pp. 24–26, gives both Case I lines and formula (11). Local source copy: `/tmp/handoff-ddr-serre-weights.txt`.
2. F. Calegari, M. Emerton, T. Gee, and L. Mavrides, *Explicit Serre weights for two-dimensional Galois representations*, Theorem 3.5.3. [Author preprint](https://math.uchicago.edu/~emerton/pdffiles/explicitBDJ.pdf). This proves the equality of crystalline and AH extension spaces used here. Its indexing is opposite to DDR's; for degree two negating indices fixes 0 and 1, and the notation in the present note is consistently DDR's. Local source copy: `/tmp/handoff-cegm-explicit.txt`.
3. F. Diamond, M. Flach, and L. Guo, *The Tamagawa number conjecture of adjoint motives of modular forms*, Ann. Sci. École Norm. Sup. 37 (2004), 663–727. [Primary journal PDF](https://www.numdam.org/article/ASENS_2004_4_37_5_663_0.pdf). Proposition 2.2; §3.1, pp. 715–720, particularly the deformation functor and equation (70), and the proved minimal \(R=T\); §3.2 for the modular construction. Local source copy: `/tmp/handoff-dfg-adjoint.txt`.
4. J. S. Milne, *Arithmetic Duality Theorems*, second edition, I.2.8 and I.5.1. [Author PDF](https://jmilne.org/math/Books/ADTnot.pdf). These are the local and global Euler characteristic statements used in Sections 5–6.
5. J. S. Milne, *Class Field Theory*, version 4.03, Chapters III and V, especially the local Artin map and the global idelic reciprocity sequence. [Author notes](https://www.jmilne.org/math/CourseNotes/CFT.pdf). The particular ring class quotient (972.16) and the nontrivial-isotypic exact sequence (972.45) are derived here from those reciprocity statements and the class number one of \(K\).

Internal dependencies: R913, R918, R942, R955, R965, and R970. The already registered low-space and complete-packet results are used without recomputation.
