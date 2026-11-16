# R906 — The original CM Tate image comes entirely from the Raynaud abelian part

Date: 2026-11-16. Status: **proved for the original primes and the fixed original quotient below**. This is an equality of actual integral Tate images. It preserves, rather than removes, the possible $p$ index of the original quotient. It does not assert saturation of its pullback on invariant differentials or a unit first normal coefficient at the original CM point.

## 1. Fixed source, quotient, and convention

Let
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
e=p^2-1,\qquad n=p+1.
\tag{906.1}
$$
Retain the original curve and its original positive primitive CM quotient:
$$
X=X_p=Z_p,\qquad
J=\operatorname{Jac}(X),\qquad
q:J\longrightarrow A=A_{\theta,1}.
\tag{906.2}
$$
Here $X$ is the normalization in R376(376.1),
$$
X=\operatorname{Norm}
\left(X_{\mathrm{ns}}^+(p)\times_{\mathbf P^1_j}\mathbf P^1_a\right),
\qquad j=6912a^3(1-a^3).
\tag{906.3}
$$
The actual homomorphism $q$, the point $c_0:a=0$, and the point $c_1:a=1$ are those of R616(616.4–5) and R859(859.2). In particular the centered curve map is still
$$
P\longmapsto q([P-c_1])
=q([P-c_0])-q([c_1-c_0]).
\tag{906.4}
$$
If a rational isogeny denominator was cleared in fixing $q$, that fixed integer remains part of $q$. Nothing below replaces $q$ by an optimal quotient, divides it by $p$, or changes (906.4).

All Tate modules in this paper are **covariant**:
$$
T_pD=\varprojlim_r D[p^r](\overline{\mathbf Q}_p),
\tag{906.5}
$$
with transition multiplication by $p$. This convention is specified because the external uniformization reference also uses a contravariant Tate convention elsewhere; we will derive the covariant exact sequence directly.

Write $K_0$ for the completed maximal unramified extension used in R376/R378/R859 and use the same tame extension
$$
L=K_0(\varpi),\qquad \varpi^e=p.
\tag{906.6}
$$
Replacing $\varpi$ by the unit multiple of
$(1-\zeta_p)^{1/(p+1)}$ in R376(376.2) does not change its tame fundamental character. Every finite algebraic object used here descends to a sufficiently large finite unramified coefficient extension; statements about Galois modules are made in the original algebraic closure before completion.

Let $\tau$ be an actual inertia element with
$$
\tau(\varpi)=\xi\varpi,\qquad
\xi\in\mu_e\ \text{primitive},\qquad
\sigma=\tau^{e/2}.
\tag{906.7}
$$
Thus $\sigma$ acts on $L/K_0$ by $\varpi\mapsto-\varpi$. We do **not** postulate an element of order two in the absolute Galois group. Only its stated action on the tame extension, the period lattice, and the Tate module will be used.

## 2. The period lattice has trivial $\sigma$ action

We first identify an actual source action, not just an abstract semistable type.

Edixhoven–Parent, §2.2.4, describes the full-level inertia action on a Drinfeld component by
$$
(\alpha,\beta)\longmapsto
(u^{-1}\alpha,u^{-1}\beta).
\tag{906.8}
$$
This is their formula (13). The same section makes $\mu_{p+1}$ trivial on the Igusa parts. In the proof of their Theorem 3.1, the inertia element $u=-1$ and the geometric matrix $-I$ in the non-split Cartan act identically on the Drinfeld coordinates. Consequently $\{\pm1\}$ acts trivially on the entire special fiber of the **fine** Cartan quotient. That proof allows any auxiliary finite étale representable tame moduli problem, so it applies after adding the full level-six structure.

For the actual source, pass to the normalizer and then take the same tame $H_6$ quotient as in R376 §2. The Galois and geometric actions commute. The cubic change of parameter is $p$-locally trivial by R376(376.13), equivalently R859(859.6a), since $4$ is a cube in $\mathbf Q_p$. These operations introduce no new $\sigma$ character.

It follows that $\sigma$ fixes the dual graph $\mathcal G$ of a semistable model of the actual $X_L$:
$$
\sigma|H_1(\mathcal G,\mathbf Z)=1.
\tag{906.9}
$$
Here is why resolving quotient singularities does not conceal a graph action. Before resolution the components and their branches are fixed. The chains inserted at a fixed node have their two endpoints fixed, hence every vertex and edge in the ordered chain is fixed. Contractions and subdivisions give the same $H_1$. Pointwise identity on each exceptional projective line is unnecessary for (906.9).

Use the Raynaud uniformization of $J_L$ and denote it by
$$
0\longrightarrow\Lambda\longrightarrow G^{\mathrm{an}}
\longrightarrow J_L^{\mathrm{an}}\longrightarrow0,
\qquad
0\longrightarrow T\longrightarrow G
\longrightarrow B\longrightarrow0.
\tag{906.10}
$$
The variety $B$ has good reduction; $T$ is a torus. The letter $B$ here denotes this Raynaud abelian part, not the Weil restriction of R859(859.3) and not a Cartier constant.

The uniformization and its descent are functorial. Its period lattice $\Lambda$ identifies with the character lattice of the toric part of the special fiber of the dual Jacobian. The canonical principal polarization of $J$ and the generalized Jacobian description identify that lattice with $H_1(\mathcal G,\mathbf Z)$. These identifications respect the actual descent action. Therefore
$$
\boxed{\sigma|\Lambda=1.}
\tag{906.11}
$$
Only the graph assertion is needed; no assertion that all inertia acts trivially on $\Lambda$ is made.

For the uniformization and the algebraicity of induced maps, see Emerton, *Optimal quotients of modular Jacobians*, §3, pp. 11–12, which gives the functorial construction and explicitly cites SGA 7 IX, Lemma 7.2.1. The characterization of $\Lambda$ by the dual torus is stated in the same section.

## 3. The actual quotient factors through the abelian part

The target $A_L$ has good reduction by the original local CM construction in R390 and its retained positive-twist application in R859. Its Raynaud uniformization has no torus and no period lattice. Functoriality applied to the **fixed** $q$ gives an algebraic homomorphism
$$
q_G:G\longrightarrow A_L
\tag{906.12}
$$
compatible with (906.10), annihilating $\Lambda$, and equivariant for the original descent.

An algebraic homomorphism from a torus to an abelian variety is zero. For example, after splitting the torus, each restriction to $\mathbf G_m$ extends to $\mathbf P^1$ by properness, and every morphism $\mathbf P^1$ to an abelian variety is constant. The homomorphism condition makes that constant zero. Hence (906.12) factors uniquely as
$$
q_G=q_B\circ\pi_B,\qquad q_B:B\longrightarrow A_L.
\tag{906.13}
$$
This factorization retains all integer scalars in $q$. We do not identify $B$ with a different chosen good-reduction quotient of $J$.

For completeness the covariant torsion sequence associated with (906.10) is
$$
0\longrightarrow G[p^r]\longrightarrow J[p^r]
\longrightarrow\Lambda/p^r\Lambda\longrightarrow0.
\tag{906.14}
$$
To define the last map, lift $x\in J[p^r]$ to $g\in G^{\mathrm{an}}$ and send it to the class of $p^rg\in\Lambda$. Changing $g$ by a period changes that class by $p^r\Lambda$. Its kernel is exactly the image of $G[p^r]$. Conversely a period has a $p^r$-division point in the semiabelian variety, giving surjectivity. Such a division point is algebraic, since it belongs to a finite algebraic fiber of $[p^r]$.

Multiplication by $p$ on these torsion sequences induces reduction on $\Lambda/p^r\Lambda$. The maps on $G[p^r]$ are surjective over the algebraic closure. Taking inverse limits therefore gives the exact integral sequence
$$
0\longrightarrow T_pG\longrightarrow T_pJ
\longrightarrow\Lambda\otimes\mathbf Z_p\longrightarrow0.
\tag{906.15}
$$
Similarly,
$$
0\longrightarrow T_pT\longrightarrow T_pG
\longrightarrow T_pB\longrightarrow0.
\tag{906.16}
$$
All these maps have their actual Galois descent action. By (906.11),
$$
(\sigma-1)T_pJ\subset T_pG.
\tag{906.17}
$$

## 4. Inverting $\sigma-1$ on the original image, integrally

The original positive primitive labels are
$$
\mathcal H=\{h:1\le h\le p,\ h\equiv1\pmod6,\ (h,p+1)=1\}.
\tag{906.18}
$$
R859(859.7), using R390(390.17–22) with $k=-h$, gives the two actual residual Tate exponents
$$
a_h=1-h(p-1),\qquad
b_h=p+h(p-1)\pmod e.
\tag{906.19}
$$
These are the residual characters of the actual $p$-adic representation; Weil–Deligne finite types would not suffice here. Both exponents are odd. Evaluation at the specific $\sigma$ in (906.7) consequently gives eigenvalue $-1$ on every residual constituent. In particular,
$$
\det(\sigma-1\mid V_pA)\in\mathbf Z_p^\times.
\tag{906.20}
$$
It is enough to know these eigenvalues; no unstated assertion that a chosen residual matrix is already diagonal is needed.

Set
$$
M=q(T_pJ)\subset T_pA.
\tag{906.21}
$$
Since $q$ is a surjective homomorphism of abelian varieties, $M$ is a full-rank $\mathbf Z_p$ sublattice. It is stable under the entire original Galois action. In particular $U=\sigma-1$ preserves $M$. Its determinant on $M\otimes\mathbf Q_p=V_pA$ is the unit in (906.20).

Here is the integer step. Write the characteristic polynomial of $U|M$ as
$$
P_U(T)=T^d+c_{d-1}T^{d-1}+\cdots+c_1T+c_0
\in\mathbf Z_p[T].
\tag{906.22}
$$
Its constant coefficient is a unit. Cayley–Hamilton then expresses
$$
U^{-1}=
-c_0^{-1}
\left(U^{d-1}+c_{d-1}U^{d-2}+\cdots+c_1\right)
\in\operatorname{End}_{\mathbf Z_p}(M).
\tag{906.23}
$$
Thus
$$
\boxed{(\sigma-1)M=M.}
\tag{906.24}
$$
This conclusion is about the lattice $M$ itself, not merely its rational span.

For any $a\in M$, choose $b\in M$ with $(\sigma-1)b=a$ and choose $j\in T_pJ$ with $q(j)=b$. Galois equivariance and (906.17) give
$$
a=q((\sigma-1)j)\in q(T_pG).
\tag{906.25}
$$
The opposite inclusion is immediate. Using (906.13) and the surjection (906.16) proves the promised identity:
$$
\boxed{
q(T_pJ)=q_G(T_pG)=q_B(T_pB)
\quad\text{inside }T_pA.}
\tag{906.26}
$$

**Theorem 906.1.** Equation (906.26) holds for the fixed original positive primitive quotient (906.2), at every prime (906.1), with its original integer scale.

The proof does not suppose that $\ker q$ is connected. If that condition is established independently for a particular choice of $q$, then $q(T_pJ)=T_pA$ and (906.26) also gives $q_B(T_pB)=T_pA$. That additional saturation must not be silently imposed on the original denominator-cleared map.

## 5. Same-label integral indices are preserved

Let $e_h$ denote the original integral local spectral projectors of R390(390.19–20), transported as in R859. They act on every original Galois-stable target lattice, hence on $M$. Applying them to the equality (906.26) gives
$$
e_hq(T_pJ)=e_hq_B(T_pB)
\subset e_hT_pA
\qquad(h\in\mathcal H).
\tag{906.27}
$$
Thus any elementary divisor or $p$ index of this actual image, either on the full target or at an individual original primitive label, is exactly the same when computed from $B$. There is no passage to all labels of the unprojected Weil restriction and no identification of $h$ with a different half-period label.

Equations (906.26–27) remove the period-lattice direction as a separate source of the actual Tate-image index. They do not compute the remaining index.

## 6. The remaining integral-geometric comparison

There are still two different steps after (906.26).

First, to identify the pullback of the good-model cotangent lattice, one needs the integral finite-flat or abelian-scheme comparison for the actual
$q_B:B\to A_L$. The extension used here has absolute ramification index $p^2-1$; even its half-degree subextension has index $(p^2-1)/2$. The small-ramification exactness theorem of Raynaud in Mazur, Proposition 1.2, requires $e_{\mathrm{abs}}<p-1$. Its cotangent Corollary 1.1 has the same hypothesis, and §1(e) explicitly explains why it cannot be dropped in general. Accordingly this theorem cannot be applied to turn the Tate equality into Hodge saturation in the present model.

Second, even a separately proved saturated global differential pullback would not give its value or first normal order at the selected point of $D_1$. R376 retains the actual contraction of that component, and R859 transports the complete normal-content ideal without proving it is the unit ideal. A comparison with the original ramified source and its marked parameter remains necessary.

In particular this paper proves neither the first-block Cartier product of R770 nor the required same-$h$ primitive/Legendre nonvanishing. It does not alter the R706/R739 counterexamples, the original $c_0$ rigidification, or the actual height and normal-content problems.

## Sources and precise scope

- [R376](R376-actual-cm-drinfeld-point-and-component-contraction.md), (376.1–2), §2, and (376.15–24): actual source, tame auxiliary layer, local twist, and distinction between geometric action and inertia.
- [R616](R616-original-CM-point-difference-and-explicit-height-basis.md), (616.4–5): original points and quotient, including its allowed fixed denominator-clearing scale.
- [R390](R390-cm-coordinate-inertia-weight-one-channel-and-cartier-unit.md), §§2–3: actual Tate characters and integral spectral projectors.
- [R859](R859-original-prime-to-p-CM-model-and-normal-content-transport.md), (859.2), (859.6a–7), and §§4–6: positive orientation, original normalized disk, and the unchanged normal-content boundary.
- Bas Edixhoven and Pierre Parent, [*Semistable reduction of modular curves associated with maximal subgroups in prime level*](https://arxiv.org/pdf/1907.02418), §2.2.4, (13), and the proof of Theorem 3.1, arXiv PDF pp. 10–12; the $\{\pm1\}$ argument is on PDF page 12. Theorem 3.3 gives the subsequent normalizer quotient. No coarse-curve component-group formula is used for the auxiliary six-level source.
- Matthew Emerton, [*Optimal quotients of modular Jacobians*](https://www.math.uchicago.edu/~emerton/pdffiles/optimal.pdf), §3, pp. 11–12: functorial Raynaud uniformization, dual-torus description of the period lattice, and algebraicity of the induced map. The torsion convention (906.14–16) is derived here.
- Barry Mazur, [*Rational isogenies of prime degree*](https://www.math.columbia.edu/~goldfeld/Mazur-Goldfeld1978.pdf), Proposition 1.2, printed pp. 135–136; Corollary 1.1, p. 137; §1(e), p. 138: the precise small-ramification hypothesis and the limitation on inferring an integral cotangent statement.

