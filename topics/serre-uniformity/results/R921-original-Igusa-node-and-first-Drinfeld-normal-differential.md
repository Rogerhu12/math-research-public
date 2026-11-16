# R921 — The original Igusa layer fixes the first Drinfeld normal differential

Date: 2026-11-16. Status: **proved for every original allowed prime**. The actual Igusa vectors identified in R918 and R920 determine the first nonzero normal layer of the same original pullback differential on the component through $c_1$. The integral comparison and the node unit are retained. The holomorphic coefficient within this layer, the original Tate index, and the specified critical source coefficient are not identified with units.

## 1. Original maps, indices, and statement

Assume
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
n=p+1,\qquad e=p^2-1.
\tag{921.1}
$$
Use the same original curve, positive CM quotient $q$, tame level-six marking, $c_0$ rigidification, and $c_1$ centering as in R906–R920. Work over
$$
R=R_0[\varpi],\qquad \varpi^e=p,\qquad
\tau(\varpi)=\xi\varpi,
\tag{921.2}
$$
after an unramified extension containing the marked constants. Its residue field may be enlarged to $k=\overline{\mathbf F}_p$. Valuations below are $v_\varpi$ unless specified.

The actual good Raynaud abelian part is $B/R$. For each original primitive label the complete-BT map of R908 is
$$
e_hq_B=[p^{a_h}]\circ f_h,\qquad a_h\ge0.
\tag{921.3}
$$
No division of the original quotient by its actual index is implicit. Select the following label, separately in the two cases:
$$
\begin{array}{c|c|c|c|c|c}
p\bmod12&h&r=2h-n&k_+=r+2&
g=g(D_1)&M=n/6\\ \hline
11&(p+3)/2&2&4&(p+1)/12&2g\\
5 &(p+9)/2&8&10&(p-5)/12&2g+1 .
\end{array}
\tag{921.4}
$$
The labels are those of R918 and R920. They satisfy $h\equiv1\pmod6$, $(h,n)=1$, and $h>n/2$. For the second assertion of primitivity, $\gcd(h,n)$ divides eight and $h$ is odd; in the first case it divides two and $h$ is odd.

Let $\omega_h$ be the same unit good-model positive-CM differential as in R916. Its coordinate-ring inertia character is
$$
\tau^*\omega_h=\xi^{t_h}\omega_h,\qquad t_h=(p-1)h.
\tag{921.5}
$$
The integral comparisons in §2 send $f_h^*\omega_h$ to a global relative dualizing differential on the actual semistable source; denote it by $\Omega_h$. Thus the differential of the original map is exactly
$$
\Theta_h:=(e_hq)^*\omega_h=p^{a_h}\Omega_h.
\tag{921.6}
$$
This is an equality of differentials, not an assertion that $f_h$ is an algebraic quotient of the entire original Jacobian.

The original component and point are
$$
D_1:\quad y^2=x(x^M+A),\qquad A\in k^\times,
\qquad \overline{c_1}=(0,0).
\tag{921.7}
$$
These are R376(376.3–4), in its retained local scope under R575. If $b_D(\Omega_h)$ denotes the order of divisibility by $\varpi$ at the generic point of $D_1$, then
$$
\boxed{
b_D(\Omega_h)=k_+(p-1),\qquad
b_D(\Theta_h)=ea_h+k_+(p-1).
}
\tag{921.8}
$$
In particular, the exact first normal differential
$$
\nu_h:=\overline{\varpi^{-k_+(p-1)}\Omega_h}\bigm|_{D_1}
\tag{921.9}
$$
has the form
$$
\boxed{
\nu_h=x^{g-1}\bigl(\alpha_hx^M+\beta_h\bigr)\frac{dx}{y},
\qquad \alpha_h\in k^\times,\quad \beta_h\in k.
}
\tag{921.10}
$$
The reduction in (921.9) is taken along $D_1$: the divided differential need not be integral along the adjacent Igusa component. The poles in (921.10) are exactly the node poles described below.

## 2. Integral Hodge transport from the same good part

Let $\mathcal J$ be the Néron model of the original source Jacobian. Its Raynaud extension over $R$ is
$$
0\longrightarrow\mathcal T\longrightarrow\mathcal G
\longrightarrow B\longrightarrow0.
\tag{921.11}
$$
The formal completion of $\mathcal G$ along its special fiber is the formal completion of $\mathcal J^0$. This is the integral construction of the Raynaud extension, not merely an isomorphism between generic tangent spaces. Emerton, §3, pp. 11–12, recalls the algebraization of this very formal completion and its functoriality. Taking cotangents at the identity gives
$$
\omega_{\mathcal G}\xrightarrow{\sim}\omega_{\mathcal J}.
\tag{921.12}
$$
Because the projection in (921.11) is smooth and its kernel is a torus, its cotangent sequence is an exact sequence of free $R$-modules:
$$
0\longrightarrow\omega_B\longrightarrow\omega_{\mathcal G}
\longrightarrow\omega_{\mathcal T}\longrightarrow0.
\tag{921.13}
$$
In particular the first arrow is saturated. These assertions concern the Raynaud extension and do not assert that the pullback of $q$ is saturated.

Take a proper regular semistable model $\widetilde{\mathcal X}$ of the original curve. Cais, Theorem 1.2 and diagram (1.3), identify integrally
$$
\omega_{\mathcal J}
\xrightarrow{\sim}
H^0(\widetilde{\mathcal X},
      \omega_{\widetilde{\mathcal X}/R}).
\tag{921.14}
$$
The hypotheses hold: the model is regular and its special fiber is geometrically reduced. This is the actual Abel–Jacobi pullback. Changing an auxiliary Abel base point changes that map by translation, which acts trivially on invariant differentials. The identification therefore preserves the given descent and the original $c_0$ rigidification; centering the map at $c_1$ changes no differential.

One can contract the rational chains to use the original nodal local models
$UV=\epsilon\varpi^d$ below. This does not change the module in (921.14). Indeed resolving such a node inserts the usual chain of projective lines; the relative dualizing generator is $dU/U=-dV/V$, and its pullback is the same generator on successive node charts. There is no additional canonical divisor on that chain. Equivalently these $A_{d-1}$ singularities are rational and Gorenstein, and Cais's same theorem applies directly to the contracted model. Thus (921.14) also gives the dualizing section on the original contracted nodal model $\mathcal X$.

Combining (921.12–14) gives the actual integral injection
$$
\omega_B\hookrightarrow
H^0(\mathcal X,\omega_{\mathcal X/R}).
\tag{921.15}
$$
Its reduction on the abelian part is the usual collection of holomorphic differentials on the normalized components. This follows as well from the Picard construction: the special fiber of $B$ is the product of their Jacobians, and invariant differential pullback is the componentwise Abel–Jacobi identification. The torus accounts for the residue part and is the quotient in (921.13).

The original $q$ is functorial for Raynaud uniformization and kills the torus when mapped to its good target. Consequently its differential through (921.15) is precisely (921.6). The BT differential $f_h^*\omega_h$ is a genuine vector of $\omega_B$, even though no unnecessary algebraization of $f_h$ is asserted.

R916 now gives an integral primitive vector
$$
L_h=\varpi^{-pr}\Omega_h
   \in H^0(\mathcal X,\omega_{\mathcal X/R}).
\tag{921.16}
$$
By R918 and R920, its restriction to the marked Igusa part is nonzero and is a nonzero scalar times the specified $V_{k_+}^\dagger$ under the actual Igusa map. Thus the exact fine Igusa order is
$$
\operatorname{ord}_{I_{\rm fine},P_0}(\overline L_h)
=2p-k_+-1.
\tag{921.17}
$$
All phases and the determinant correction are those in those results. No unmarked $j=0$ point or arbitrary vector with the same Hecke eigenvalues replaces this vector.

## 3. The joint stabilizer and the actual node thickness

The elliptic automorphism group at the marked $j=0$ curve is $\mu_6$. R376 §2 proves that the original $a=1$ branch retains its whole effective $\mu_3$: the map
$j=6912a^3(1-a^3)$ is unramified at $a=1$, whereas the fine elliptic deformation has a cubic quotient parameter. The actual cubic twist is locally trivial as recorded there. It supplies no further inertia character.

Before this tame quotient the normalizer Igusa component is the quotient by a scalar group
$$
C_a,\qquad
a=\begin{cases}2,&p\equiv11\pmod{12},\\4,&p\equiv5\pmod{12}.
\end{cases}
\tag{921.18}
$$
These are the two cases of Edixhoven–Parent, Theorem 3.3. In the second case there are two such Igusa components, with the full norm extension retained as in R920.

The two stabilizer groups on the fine Igusa curve share exactly their order-two subgroup. In moduli terms the tame action of $[-1]$ on the full-six basis is identified, by the same elliptic isomorphism, with the sign change of the Igusa generator. Thus these two signs are the same action. An element in their intersection acts trivially on the tame base. The kernel of $\mu_6$ on that base is exactly $\{\pm1\}$, because the remaining order-three action is faithful on the elliptic deformation. There is no larger intersection.

The actions commute, being the tame-level action and the scalar action on the Igusa structure. Their product is therefore cyclic of order
$$
d=\frac{6a}{2}
=\begin{cases}6,&p\equiv11\pmod{12},\\12,&p\equiv5\pmod{12}.
\end{cases}
\tag{921.19}
$$
It acts faithfully on the local fine Igusa parameter. The scalar group acts faithfully there, and a nontrivial order-three element cannot have trivial tangent action: it already acts nontrivially on the tame base. For a tame action on a smooth formal curve, averaging a parameter gives a linearizing parameter. Hence the ramification index of the fine-to-original Igusa map at this point is exactly $d$, not $6a$.

If $m_I$ is the order of the actual coarse Igusa differential, pullback of a differential under a tame map of ramification index $d$ gives
$$
2p-k_+-1=d\,m_I+(d-1).
$$
Thus put
$$
R_*:=m_I+1=\frac{2p-k_+}{d};
\qquad
m_I=
\begin{cases}
(p-5)/3,&p\equiv11\pmod{12},\\
(p-11)/6,&p\equiv5\pmod{12}.
\end{cases}
\tag{921.20}
$$
These are exact orders, so their leading coefficients are nonzero.

We next retain the integral thickness, rather than deducing it only from this special-fiber action. Edixhoven–Parent's base $W$ has ramification index $e/2$. Their Theorem 3.3 gives thickness one for the single-Igusa case and thickness two for the two-Igusa case. At $j=0$ the remaining effective order-three quotient acts with opposite characters on the two node branches. Its invariant coordinates are the cubes of the branch coordinates. Theorem 3.5 records exactly the resulting exponents three and six over $W$.

Passing to our original $R$, of ramification index $e$, doubles these exponents. The local equation at each node adjacent to the actual $D_1$ is consequently
$$
\boxed{UV=\epsilon\,\varpi^d,\qquad \epsilon\in R^\times,}
\tag{921.21}
$$
with $d$ as in (921.19). Here $D_1$ is $U=0$ and the Igusa component is $V=0$. The unit $\epsilon$ retains the original parameters and the unit relating the $W$ uniformizer to $\varpi^2$. It is not replaced by one. The original tame branch has the same local quotient as this marked $j=0$ calculation by R376(376.14); no global identification with a different modular curve is being assumed.

There is one adjacent node, at the unique point at infinity of (921.7), when $p\equiv11\pmod{12}$. There are two, at its two points at infinity, when $p\equiv5\pmod{12}$. The original full-norm character transports the nonzero Igusa differential between the latter two components. Thus (921.20) holds at each relevant branch.

## 4. Inertia excludes every lower possible normal layer

Let
$$
b=b_D(\Omega_h).
$$
The differential is nonzero, so this is a finite integer. Equation (921.16) gives $b\ge pr$. Its first nonzero reduction along $D_1$ has character
$$
u^{t_h-b},\qquad
u\in\mathbf F_{p^2}^{\times},
\tag{921.22}
$$
because division by $\varpi^b$ subtracts that exponent in the original semilinear coordinate-ring convention.

The full inertia action on the actual component, from R910–R911 followed by R376's quotient, is
$$
x\longmapsto q_u^6x,\qquad
y\longmapsto q_u^3y,\qquad
q_u=u^{p-1}\in\mu_n.
\tag{921.23}
$$
Its pointwise kernel has order $3(p-1)$: it is exactly the preimage of $\mu_3$ under $u\mapsto u^{p-1}$. Tame inertia fixes the residue-field constants. Every nonzero rational differential on $D_1$ therefore has trivial action of this kernel. Applied to (921.22), this forces
$$
b\equiv t_h\pmod{3(p-1)}.
\tag{921.24}
$$
This uses the entire pointwise kernel on the actual component; the subgroup $\mu_{p-1}$ alone would give a weaker bound.

Since $h\equiv1\pmod3$, the allowed multiples of $p-1$ have multiplier congruent to one modulo three. Since $r=2$ or $8$,
$$
r\equiv2\pmod3,\qquad
pr=r(p-1)+r,\qquad 0<r<p-1.
$$
The smallest integer not less than $pr$ that satisfies (921.24) is
$$
b_0=(r+2)(p-1)=k_+(p-1).
\tag{921.25}
$$
In particular no coefficient arising from a higher integral lift term at a node can create a nonzero component layer between $pr$ and $b_0$. Such a layer would still satisfy the same original descent and would violate (921.24).

We have proved the genuine lower bound $b\ge b_0$. It remains to prove equality, which requires the actual node coefficient.

## 5. The Igusa unit forces equality at the node

In the completed local ring (921.21), write the integral dualizing section (921.16) as
$$
L_h=f(U,V)\frac{dU}{U}
   =-f(U,V)\frac{dV}{V}.
\tag{921.26}
$$
The exact Igusa order (921.20) says that
$$
f(U,0)\bmod\varpi
=c_*U^{R_*}+\text{higher powers of }U,
\qquad c_*\in k^\times.
\tag{921.27}
$$
Choose the unique power-series normal form for the nodal ring:
$$
f(U,V)=\sum_{i\ge0}a_iU^i+\sum_{j\ge1}b_jV^j,
\qquad a_i,b_j\in R.
\tag{921.28}
$$
It is obtained by replacing each mixed monomial by a power of
$\epsilon\varpi^d$ times a monomial on one axis. Completeness makes the resulting sums converge. Uniqueness also follows by substituting $U=\epsilon\varpi^d/V$ in the formal Laurent expansion. In particular $a_{R_*}$ is a unit by (921.27).

At the generic point of $D_1$, substitute that same equation into (921.26). The term with index $i=R_*$ is
$$
-a_{R_*}\epsilon^{R_*}\varpi^{dR_*}
  V^{-R_*}\frac{dV}{V}.
\tag{921.29}
$$
It has a Laurent exponent distinct from every other $U^i$ term and from every nonnegative-axis term. It cannot be cancelled. Its coefficient is a unit times $\varpi^{dR_*}$.

More explicitly, after reduction at any fixed $\varpi$ precision, only finitely many negative Laurent powers in (921.28) can occur. Distinct negative powers and nonnegative powers are linearly independent in $k((V))$. Thus the generic $D_1$ valuation of $f$ is at most $dR_*$, with no implicit assumption that all other coefficients are units. Since
$$
pr+dR_*
=pr+2p-k_+
=(r+2)(p-1)=b_0,
\tag{921.30}
$$
this proves $b_D(\Omega_h)\le b_0$. Combined with §4, it proves (921.8).

At this exact layer the leading node pole is
$$
-\overline{a_{R_*}}\,
 \overline{\epsilon}^{\,R_*}
 V^{-R_*-1}\,dV.
\tag{921.31}
$$
Its coefficient is nonzero. Terms $i>R_*$ cannot contribute, because $di>dR_*$ and their coefficients are integral. Terms $i<R_*$ may contribute at this layer if their coefficients have the requisite positive valuation; they give smaller poles. The $V$-axis terms are regular apart from the displayed logarithmic generator. Therefore $\nu_h$ has pole order at most $R_*+1$ at this node, and exactly that order by (921.31). This proves the lower layer and its nonzero leading coefficient while retaining every integral lift correction and the node unit.

Away from the nodes, the first normal reduction is regular on $D_1$. Locally the surface is smooth over $R$ and its completed ring is $R[[w]]$. Generic divisibility along the reduced component implies coefficientwise divisibility by that power of $\varpi$: the ideal $(\varpi^b)$ is primary there, and localization at $(\varpi)$ introduces no further divisibility. Thus no finite pole is introduced in (921.9).

## 6. Determining the complete normal differential

By (921.22), (921.25), and (921.23), $\nu_h$ has character
$$
q_u^{h-k_+}.
\tag{921.32}
$$
The element $q_u=-1$ is the hyperelliptic involution of (921.7). Since $h-k_+$ is odd, the differential is anti-invariant. Every anti-invariant rational differential regular on the affine curve has the form
$$
P(x)\,\frac{dx}{y},\qquad P(x)\in k[x].
\tag{921.33}
$$
To see polynomiality, its rational coefficient belongs to $k(x)$; a finite pole of that coefficient would be a pole of the differential, including at a branch point, where $dx/y$ is a unit times the local differential. Such poles have just been excluded.

The character of $x^jdx/y$ is $q_u^{6j+3}$. In both cases of (921.4),
$$
h-k_+=6g-3,
$$
so the only possible exponents satisfy
$$
j\equiv g-1\pmod M.
\tag{921.34}
$$

If $p\equiv11\pmod{12}$, then $M=2g$, the curve has one point at infinity, and
$$
\operatorname{ord}_{\infty}x=-2,\qquad
\operatorname{ord}_{\infty}(dx/y)=2g-2,\qquad
R_*=4g-1.
\tag{921.35}
$$
The pole bound $R_*+1=4g$ therefore gives
$\deg P\le3g-1=g-1+M$.

If $p\equiv5\pmod{12}$, then $M=2g+1$, and at either point at infinity
$$
\operatorname{ord}_{\infty}x=-1,\qquad
\operatorname{ord}_{\infty}(dx/y)=g-1,\qquad
R_*=2g.
\tag{921.36}
$$
The pole bound $2g+1$ gives $\deg P\le3g=g-1+M$.

Combining these bounds with (921.34) leaves exactly the two monomials in (921.10). The highest permitted monomial is necessary because (921.31) has the full pole order. Consequently $\alpha_h\ne0$. The remaining coefficient $\beta_h$ is the possible holomorphic ambiguity. Neither the pole argument nor the inertia character sets it equal to zero or makes it a unit.

## 7. The original point is the branch point, and both cases remain

R376(376.4) places the original $c_1$ at $(0,0)$, not at an unspecified affine point. The local parameter there is $y$; from (921.7),
$$
x=A^{-1}y^2+\text{higher terms},\qquad
\frac{dx}{y}=\left(\frac2A+\text{higher terms}\right)dy.
\tag{921.37}
$$
Thus (921.10) gives the exact two alternatives
$$
\operatorname{ord}_{c_1}\nu_h=
\begin{cases}
2g-2,&\beta_h\ne0,\\
2(g-1+M),&\beta_h=0.
\end{cases}
\tag{921.38}
$$
The corresponding first unit coefficient in a local primitive has degree
$$
d_h:=1+\operatorname{ord}_{c_1}\nu_h
=
\begin{array}{c|cc}
&\beta_h\ne0&\beta_h=0\\ \hline
p\equiv11\pmod{12}&(p-5)/6&(p-1)/2\\
p\equiv5\pmod{12}&(p-11)/6&(p-3)/2 .
\end{array}
\tag{921.39}
$$
All four integers lie strictly between zero and $p$, so this integration step divides by a unit. This is a statement about the reduction of the first normal differential and its primitive at that same layer. It does not assert that the entire characteristic-zero Abel series has no lower-degree terms with larger valuation, or that this is the first normal layer of the formal map itself. Pure $p$-power terms can disappear on differentiating.

The observation that $\alpha x^M+\beta$ has only simple roots when $x\ne0$ does not yield a simple-zero assertion here: the actual point has $x=0$, and $x$ has order two in $y$. Formula (921.38) is the applicable statement.

## 8. A bounded zero count on a genuinely deep smooth disc

There is a direct consequence for zeros of the actual centered Abel component, independent of the unknown alternative in (921.38). Choose an integral formal parameter $w$ at $c_1$ reducing to a unit parameter on $D_1$, and write the local pullback as
$$
\Theta_h
=\varpi^{ea_h+b_0}H_h(w)\,dw,\qquad H_h(w)\in R[[w]].
\tag{921.40}
$$
The coefficient of $w^{d_h-1}$ in $H_h$ is a unit and its earlier coefficients reduce to zero, by (921.38). Let
$$
F_h(w)=\int_0^w H_h(t)\,dt.
\tag{921.41}
$$
This is the centered scalar Abel logarithm of the same original map, multiplied by the nonzero constant $\varpi^{-ea_h-b_0}$. If
$H_h=\sum_{m\ge0}c_mw^m$, then
$$
F_h(pZ)=\sum_{m\ge1}\frac{c_{m-1}p^m}{m}Z^m,
\qquad
v_p\left(\frac{c_{m-1}p^m}{m}\right)\ge m-v_p(m).
\tag{921.42}
$$
The coefficient at $m=d_h<p$ has valuation exactly $d_h$. Every $m>d_h$ has
$m-v_p(m)>d_h$. For $m<p$ this is immediate. For $m\ge p$, one has
$v_p(m)\le(m-1)/(p-1)$, so $m-v_p(m)\ge p-1>d_h$.
The coefficients in (921.42) tend to zero.

The largest index at which the minimal coefficient valuation occurs is consequently at most $d_h$. Strassmann's theorem, or restricted Weierstrass preparation, gives at most $d_h$ zeros, counted with multiplicity, in $v_p(w)\ge1$. This includes the center. On this disc the actual formal-group image is in the convergence and injectivity domain of the good formal logarithm, since the original centered formal map is integral and $1>1/(p-1)$. Hence the same bound applies to zeros of this actual projected Abel increment, and in particular to simultaneous zeros of the full original Abel increment.

The actual source coordinate of R378(378.2,28–30) and R859(859.18) is
$$
z=\frac{a-1}{\varpi^{3p(p-1)}}.
\tag{921.43}
$$
It is an integral formal parameter at $c_1$, up to an integral change with unit linear term. Such changes preserve valuations on the open unit disc. If $v_p(a-1)\ge4$, then
$$
v_p(z)\ge4-\frac{3p}{p+1}=1+\frac3{p+1}>1.
\tag{921.44}
$$
Thus (921.42) supplies, uniformly for the labels (921.4), the bounds
$$
\#\{\text{noncentral zeros in this original deep disc}\}
\le
\begin{cases}
(p-3)/2,&p\equiv11\pmod{12},\\
(p-5)/2,&p\equiv5\pmod{12}.
\end{cases}
\tag{921.45}
$$
If $\beta_h\ne0$, the smaller bounds $d_h-1$ from (921.39) apply. This is a finite zero-count assertion; it asserts neither that the center is the only zero nor that a positive-rank rational-point candidate has zero Abel image.

## 9. What has and has not crossed the original source boundary

The new conclusion is the exact original componentwise differential exponent (921.8), the complete two-term first normal shape (921.10), and its actual node and $c_1$ vanishing orders. It uses the actual nonzero marked Igusa vector, not only the existence of an abstract Hodge eigenspace.

The original index $a_h$ remains unchanged. The holomorphic coefficient $\beta_h$ remains to be determined by the actual global gluing or an additional compatible correspondence. The local integral comparison has not proved that the entire original quotient is $p$-optimal.

Most importantly, no expression above identifies $\alpha_h$, $\beta_h$, or the node coefficient (921.31) with R898's specified coefficient of the original $u_{GF}$. The primitive label in (921.4) is fixed throughout, but the target
$$
P_{h-1}(1/s)\,f_i g_{N-1-i}\ne0,
\qquad p=6N+5,\quad h=6i+7,
\tag{921.46}
$$
still needs its same-label source comparison. R706 and R739's counterexamples to individual universal first-block assertions remain valid. The height linear term and second-kind periods are also untouched. Neither the bounded zero count nor nonzero node propagation completes the README's uniformity criterion.

## Sources and exact scope

- [R376](R376-actual-cm-drinfeld-point-and-component-contraction.md), (376.3–4), §2 and §§3–4: original $a=1$ stabilizer, component, actual $c_1$, and local action; only its retained local scope under [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md) is used.
- [R378](R378-actual-cm-disc-parameter-and-uniform-integral-tail.md), (378.2,28–30), and [R859](R859-original-prime-to-p-CM-model-and-normal-content-transport.md), §4: actual integral source coordinate and positive coordinate-ring inertia weight.
- [R906](R906-original-period-lattice-and-integral-CM-Tate-image.md), [R911](R911-original-Picard-descent-and-exact-CM-gluing-dichotomy.md), and [R916](R916-original-finite-flat-quotient-and-exact-Hodge-content.md): same quotient, integral good part, original index, descent convention, and exact good-model content.
- [R918](R918-original-central-primitive-Igusa-layer-and-marked-weight-four-vector.md), (918.9), (918.23), and [R920](R920-original-upper-primitive-Igusa-layer-and-inert-Hecke-row.md), (920.11), (920.35–36): the two actual named Igusa vectors and their specified marked units and fine orders.
- Matthew Emerton, [*Optimal quotients of modular Jacobians*](https://www.math.uchicago.edu/~emerton/pdffiles/optimal.pdf), §3, pp. 11–12: algebraization of the Néron formal completion and functorial Raynaud uniformization.
- Bryden Cais, [*Canonical extensions of Néron models of Jacobians*](https://arxiv.org/pdf/0909.1849), Theorem 1.2, diagram (1.3), and §4: integral dualizing-differential comparison and actual Abel–Jacobi pullback.
- Bas Edixhoven and Pierre Parent, [*Semistable reduction of modular curves associated with maximal subgroups in prime level*](https://arxiv.org/pdf/1907.02418), Theorems 3.3 and 3.5, especially (26) and the node equations immediately following it: normalizer Igusa quotients, the exceptional $j=0$ stabilizer, and integral node thickness. Their base has ramification index $(p^2-1)/2$; (921.21) explicitly makes the additional quadratic base change.

The proof contains no new arithmetic execution or finite prime scan.

