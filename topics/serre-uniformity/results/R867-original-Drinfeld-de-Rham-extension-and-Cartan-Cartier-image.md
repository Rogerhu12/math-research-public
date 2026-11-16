# R867 — The original Drinfeld de Rham extension and its Cartan–Cartier image

Date: 2026-11-16. Status: **proved**. The particular residual lattice of R863 is realized on a fine Drinfeld component of the original full-level model. The original Cartan average has an explicit second-kind representative, and its image under the conjugate-filtration Cartier map is a differential that is a unit at both original CM lifts. This is a comparison of the local finite type with the component's de Rham cohomology. It does not identify the pullback of an original Néron differential, or a normal coefficient of the map $q$, with this representative.

## 1. The actual component, its constant, and the action convention

Let $p\ge41$, $p\equiv2\pmod3$, and work over a perfect residue field $k$ containing $\mathbf F_{p^2}$ and the actual fine CM markings. Retain the original blow-up coordinates from R376(376.15–18):
$$
\alpha=\overline{T(P)/\varpi},\qquad
\beta=\overline{T(Q)/\varpi},\qquad
\alpha^p\beta-\alpha\beta^p=c,\qquad c\in k^\times.
\tag{867.1}
$$
The symbol $\varpi$ here denotes the chosen tame blow-up scale. Changing from the $(1-\zeta_p)^{1/(p+1)}$ scale to the original $p^{1/(p^2-1)}$ scale changes $c$ by the corresponding nonzero factor; we do not set that factor to one. Let $\mathcal D_c$ be the smooth projective completion of (867.1). On the chart $\beta\ne0$ put
$$
v=\alpha/\beta,\qquad w=1/\beta,
\qquad v^p-v=cw^{p+1},\qquad dv=-c w^p\,dw.
\tag{867.2}
$$

This is the fine component before the normalizer and auxiliary $\mu_3$ quotients. Edixhoven–Parent, Theorem 2.3 and §§2.2.1–2.2.4, give (867.1), the full-level group action, and the inertia scaling. R376 records those inputs with the original auxiliary level and the actual CM point. In particular fixed-pairing inertia $u\in\mu_{p+1}$ acts by
$$
(\alpha,\beta)\longmapsto(u^{-1}\alpha,u^{-1}\beta).
\tag{867.3}
$$
This is distinct from the geometric auxiliary automorphism that scales the same coordinates while fixing the base.

We make the level convention explicit. In the analytic period basis $(\tau,1)$, the left finite-type action is $g\cdot f=f|g^{-1}$; an upper translation sends $f(\tau-r)$ to $f(\tau-r-t)$, as in R592(592.11). The corresponding relabelling of the ordered torsion basis is $(g^{-1})^t$. In Edixhoven–Parent's right-level notation, the pullback of the column $(\alpha,\beta)^t$ by a relabelling $h$ is $h^t(\alpha,\beta)^t$. Thus our left finite-type convention acts on the coordinate column by $g^{-1}$, before compensating its determinant. This explains the inverse below and fixes the torus and the label $r$ simultaneously.

For $g\in\mathrm{GL}_2(\mathbf F_p)$ choose $u\in\mathbf F_{p^2}^\times$ with
$u^{p+1}=\det g$. The matrix $u^{-1}g$ preserves (867.1), because the left side scales by $\det(g)/u^{p+1}$. Consider the scalar eigenspace
$$
H=H^1_{\mathrm{dR}}(\mathcal D_c/k)_{-2},
\qquad [a]^*\xi=a^{p-1}\xi=a^{-2}\xi
\quad(a\in\mu_{p+1}),
\tag{867.4}
$$
where $[a](\alpha,\beta)=(a\alpha,a\beta)$. Its inertia character in (867.3) is
$u^{-(p-1)}$, precisely the original $\theta_{-1}$ direction on the stabilizer. Define the left $G=\mathrm{PGL}_2(\mathbf F_p)$ action on $H$ by
$$
g\cdot\xi
=u^{-(p-1)}(u g^{-1})^*\xi.
\tag{867.5}
$$
This is the determinant-compensated action obtained from all Weil-pairing components and their inertia identification, with the character in (867.4) retained. It is not an assertion that every $g$ preserves a fixed pairing component without that compensation.

The formula is independent of the choice of $u$. Replacing $u$ by $u a$, with $a^{p+1}=1$, multiplies the pullback on (867.4) by $a^{p-1}$ and its displayed prefactor by $a^{-(p-1)}$. Composition follows by choosing the product of the two norm lifts. A scalar matrix $bI$ acts trivially: choose $u=b$, so its geometric matrix is $I$ and $b^{p-1}=1$. Hence (867.5) really is a $G$ action. All these factors are units, and the actual constant $c$ has remained in the equation.

## 2. The full de Rham extension, including its one-dimensional quotient

There is a single point at infinity on the superelliptic model (867.2), with
$$
\operatorname{ord}_\infty(v)=-(p+1),\qquad
\operatorname{ord}_\infty(w)=-p,\qquad
\operatorname{ord}_\infty(dw)=p^2-p-2.
\tag{867.6}
$$
The last equality follows from $dv=-cw^p dw$ and the nonzero leading derivative of the pole of order $p+1$ of $v$.

The holomorphic part of (867.4) is
$$
H^{1,0}_{-2}
=\left\langle \omega_i=v^i w\,dw:0\le i\le p-3\right\rangle.
\tag{867.7}
$$
Each displayed differential is regular: at finite points this is immediate, and (867.6) proves regularity at infinity. To see completeness directly, write a scalar-weight $-2$ differential as a rational function of $v$ times $w\,dw$. Regularity at the finite branch points and at the other finite points forces that function to be a polynomial; (867.6) bounds its degree by $p-3$.

The remaining de Rham dimension is one. Here is an explicit Čech description, also fixing its normalization. For the map $v:\mathcal D_c\to\mathbf P^1$, the scalar-weight $-2$ summand of $v_*\mathcal O_{\mathcal D_c}$ is the line bundle $\mathcal O_{\mathbf P^1}(-2)$: it has frame $w^2$ over finite $v$ and frame $w^2/v^2$ near infinity. Its first cohomology is generated by the cocycle
$$
f=w^2/v.
\tag{867.8}
$$
The exact differential identity
$$
df=\left(v^{p-2}+v^{-1}\right)w\,dw
\tag{867.9}
$$
follows by substituting (867.2). Thus the triple
$$
e=\left(v^{p-2}w\,dw,\ -w\,dw/v,\ w^2/v\right)
\tag{867.10}
$$
is a de Rham Čech cocycle, using the affine chart away from infinity and a neighborhood of infinity. The second differential is regular near infinity. Its class maps to the generator (867.8) of $H^1(\mathcal O)_{-2}$.

Equivalently, $e$ has the specified second-kind representative
$v^{p-2}w\,dw$, with a pole of order $p$ at infinity. The other regular local representative and the transition function in (867.10) are part of that assertion. It is not a globally holomorphic differential. We obtain the basis
$$
\omega_0,\ldots,\omega_{p-3},e
\quad\text{of }H,
\qquad \dim H=p-1.
\tag{867.11}
$$

For clarity, the Hodge–de Rham exact sequence used here is the one for the smooth proper curve $\mathcal D_c$; for curves its degeneration also follows directly from the residue pairing. In this scalar eigenspace the preceding Čech representatives provide the entire sequence explicitly.

The holomorphic subspace in (867.7) has the finite-group type
$S=\operatorname{Sym}^{p-3}V\otimes\det$. For example, before passing from a right action to the left inverse convention, put
$g=\left(\begin{smallmatrix}a&b\\c_0&d\end{smallmatrix}\right)$ and choose the same norm lift $u$. Under $u^{-1}g$,
$$
v\longmapsto\frac{av+b}{c_0v+d},\qquad
w\longmapsto\frac{u w}{c_0v+d}.
$$
Using (867.2) gives
$$
u^{p-1}(u^{-1}g)^*(v^i w\,dw)
=\det(g)(av+b)^i(c_0v+d)^{p-3-i}w\,dw.
\tag{867.12}
$$
The left inverse representation is the self-dual finite $G$ representation $S$, exactly as in R863.

The one-dimensional quotient is trivial. One can verify this without a character table. Its Serre-dual line is the opposite scalar eigenspace of holomorphic differentials, generated by
$$
\eta=\frac{dv}{w^2}=-c w^{p-2}\,dw.
\tag{867.13}
$$
For this opposite eigenspace the determinant compensation is inverse to that in (867.5). The fractional-linear formula gives
$(u^{-1}g)^*\eta=u^{p-1}\eta$, and the compensation cancels this factor. Thus its finite $G$ action is trivial. The residue of $(w^2/v)\eta=dv/v$ at the relevant branch point is $p+1=1$ in $k$, up to the harmless sign of the Čech pairing. This also proves that (867.8) is a nonzero quotient class.

Normalize $\lambda_{\mathcal D}:H\to k$ by $\lambda_{\mathcal D}(e)=1$ and by zero on (867.7). We have proved the exact sequence
$$
0\longrightarrow S\longrightarrow H
\xrightarrow{\lambda_{\mathcal D}}k\longrightarrow0.
\tag{867.14}
$$

## 3. Identification with the original full Weyl lattice

For $r\in\mathbf F_p$ set
$$
E_r=\left[(v-r)^{p-2}w\,dw\right]\in H.
\tag{867.15}
$$
The brackets mean the class represented as in (867.10), with its holomorphic lower terms. Each has quotient $\lambda_{\mathcal D}(E_r)=1$. Their only relation is $\sum_rE_r=0$, since the coefficients are the evaluations of polynomials of degree at most $p-2$.

Under the left convention (867.5), upper translation gives $v\mapsto v-t$, $w\mapsto w$, and therefore
$$
n(t)E_r=E_{r+t}.
$$
For $g=\operatorname{diag}(a,1)$ the compensated action on $v^i w\,dw$ is multiplication by $a^{-i-1}$. Hence
$$
\operatorname{diag}(a,1)E_r=E_{ar}.
\tag{867.16}
$$
Thus $e_r\mapsto E_r$ is exactly the Borel identification of the original R592/R863 lattice, with no independent change of the torus or the split label.

The extension (867.14) is nonsplit. Indeed its Borel module in (867.15) is the affine permutation quotient, which has no fixed vector: unipotent invariance leaves only the bottom vector, and the diagonal character of that vector is nontrivial. R863 §3 proves both that the nonsplit extension of $k$ by this $S$ is unique up to scalar and that the Borel endomorphism ring of this module is $k$. Applying those already proved statements to (867.14) and to the original lattice gives
$$
\boxed{\overline\Lambda\xrightarrow{\sim}H,
\qquad e_r\longmapsto E_r,}
\tag{867.17}
$$
as a **full $G$ isomorphism**, including the original Weyl matrix. The normalization agrees because both quotient maps send every displayed $e_r$ or $E_r$ to one. This is a new geometric realization of the complete extension; it does not replace it by a semisimplification or only its trivial quotient.

## 4. The original Cartan vector as a second-kind class

Keep the original torus of R727(727.17),
$$
T_\zeta=
\left\{\begin{pmatrix}a&-b\\b&a+b\end{pmatrix}\right\}/\mathbf F_p^\times,
\qquad \zeta^2+\zeta+1=0,\qquad s=\zeta-\zeta^2,\quad s^2=-3.
\tag{867.18}
$$
It fixes the two directions $v=\zeta,\zeta^2$. Let
$v_T=(p+1)^{-1}\operatorname{Tr}_{T_\zeta}e_0$. Its R863 moments are
$$
\mu_k=\frac{\zeta^{k+1}-\zeta^{2k+2}}{(k+1)s},
\qquad 0\le k\le p-2.
\tag{867.19}
$$
Using $\binom{p-2}{k}=(-1)^k(k+1)$ and (867.15), its image in (867.17) has the specified second-kind representative
$$
\Omega_T=H(v)w\,dw,
\qquad
H(v)=\frac{v^p+v+1}{v^2+v+1}\in k[v].
\tag{867.20}
$$
Indeed its polynomial is
$$
\sum_{k=0}^{p-2}(k+1)\mu_kv^{p-2-k}
=\frac{(v-\zeta)^{p-1}-(v-\zeta^2)^{p-1}}s
=\frac{v^p+v+1}{v^2+v+1}.
\tag{867.21}
$$
For the middle equality one may expand the binomial coefficients, or divide $v^p-\zeta^p$ by $v-\zeta$. In particular the leading coefficient is one. The denominator in (867.20) cancels exactly, since $\zeta^p=\zeta^2$.

Under the original CM marking, R376(376.25–27) puts the two fine CM lifts on the two eigen-directions of this same torus. In (867.2) they are
$$
P_\pm:\quad v=\zeta\text{ or }\zeta^2,\qquad
w^{p+1}=\frac{v^p-v}{c},
\tag{867.22}
$$
with $w\ne0$. Both $v$ and $w$ are étale parameters locally, since $dv/dw=-cw^p$ is nonzero. The polynomial value of $H$ is
$$
H(\zeta)=1/s,\qquad H(\zeta^2)=-1/s.
\tag{867.23}
$$
For example, differentiate the numerator and denominator of the exact polynomial division; their derivatives at the simple root are $1$ and $2\zeta+1=s$. Consequently the specified representative $\Omega_T$ is a local differential unit at both points.

This last sentence is deliberately about the representative in (867.20). An arbitrary exact change of a representative of a de Rham class can change its local value. The invariant statement relevant below is the value of its Cartier image.

## 5. The Cartier map, its precise subquotient, and its CM unit

For a smooth proper curve over a perfect field, local Cartier maps on the differential entries of a de Rham Čech cocycle glue, since Cartier kills exact differentials. This is the conjugate-filtration map to the Frobenius-twisted space of holomorphic differentials. We write it in its $p^{-1}$-semilinear form
$$
\mathsf C:H^1_{\mathrm{dR}}(\mathcal D_c/k)
\longrightarrow H^0(\mathcal D_c,\Omega^1),
\qquad \mathsf C(a\xi)=a^{1/p}\mathsf C(\xi).
\tag{867.24}
$$
The target notation incorporates this semilinearity rather than pretending that (867.24) is an ordinary $k$-linear map. It sends scalar weight $-2$ to weight $+2$.

In the separating variable $w$, substitute $v=v^p-cw^{p+1}$ into $v^i w\,dw$. In its binomial expansion the exponent of $w$ has the form
$(p+1)j+1$. To contribute to Cartier it must be $p-1$ modulo $p$, which in the range $0\le j\le i\le p-2$ forces $j=p-2$. Therefore
$$
\mathsf C(\omega_i)=0\quad(0\le i\le p-3),\qquad
\mathsf C(e)=-c^{(p-2)/p}w^{p-2}\,dw
=c^{-2/p}\eta.
\tag{867.25}
$$
Here $c^{1/p}$ denotes the unique $p$th root in $k$. The expression is holomorphic on the complete curve; in the other chart it is the Cartier image of the other entry of (867.10). Thus (867.25) is independent of the choice of a second-kind representative.

On the scalar eigenspace $H$ in (867.4), the kernel of (867.24) is exactly the holomorphic subspace (867.7), and the induced semilinear map on the quotient of (867.14) is an isomorphism onto $k\eta$. Since $\lambda_{\mathcal D}(v_T)=1$, we get the precise original-vector identity
$$
\boxed{\mathsf C([\Omega_T])=c^{-2/p}\eta
=-c^{(p-2)/p}w^{p-2}\,dw.}
\tag{867.26}
$$
This retains the original component constant and the semilinear root. If $c\in\mathbf F_p^\times$, the factor $c^{-2/p}$ is simply $c^{-2}$; it is not silently so simplified for an arbitrary fine residue field.

The divisor of $\eta=dv/w^2$ consists of the $p+1$ points above $v\in\mathbf P^1(\mathbf F_p)$, each with multiplicity $p-2$. At a finite branch point $dv/w^2=-cw^{p-2}dw$ gives that order; (867.6) gives the same order at infinity. The total is $(p+1)(p-2)=2g(\mathcal D_c)-2$, so there are no other zeros. The original CM directions in (867.22) do not belong to $\mathbf P^1(\mathbf F_p)$. Hence
$$
\boxed{\mathsf C([\Omega_T])(P_+)\ne0,
\qquad \mathsf C([\Omega_T])(P_-)\ne0.}
\tag{867.27}
$$
These are unit statements in the actual residue-field differential lines, invariant under unit changes of the blow-up scale. No prime scan, coefficient interpolation, or characteristic-zero period has been substituted for them.

## 6. What this identifies, and the remaining original normal comparison

Equation (867.17) identifies the **local finite-type factor** with a specific de Rham factor of the actual fine Drinfeld component. Equations (867.20) and (867.26) transport the original split/Cartan vector, including its one-dimensional quotient normalization and the full extension. Thus they are stronger than merely recognizing two semisimple constituents with the right dimensions.

They do not identify the global automorphic multiplicity coordinate on a chosen supersingular component. In particular, a global modular quotient can have an additional specialization coefficient at the original $j=0$ component. Determining that coefficient, with the original tame vector, Hodge frame, and the $q$-pullback, is a separate step. The original $q$ contracts the component after its actual auxiliary quotient, as already proved in R376; an ordinary component differential or this fine second-kind class is not its nonzero reduced pullback.

Similarly, R863 gives a cusp expansion modulo $(1-\zeta_p)^{p-1}$, whereas (867.17) is a characteristic-$p$ component realization. An integral nearby-fiber comparison must connect those two statements before the representative or its Cartier image can determine a normal jet. R859/R861 remove prime-to-$p$ target-model ambiguity and give actual Néron parameters, but do not manufacture this source comparison. No first-normal coefficient, same-$h$ pair of sigma coefficients, original height, or all-prime exclusion is asserted here.

### Sources and scope of new work

- [R376](R376-actual-cm-drinfeld-point-and-component-contraction.md), (376.15–27): the original fine component, the separate geometric and inertia actions, and the two original CM lifts. Its corrected positive-twist scope is understood throughout.
- [R592](R592-actual-integral-CM-jet-lattice-and-complete-tail.md), §2, and [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md), §5: the original finite-type action, split-cusp phase, and the period-basis torus.
- [R863](R863-original-cuspidal-extension-and-full-first-ramified-phase.md), §§2–4: the full original residual extension, the extension and Borel uniqueness proofs, and all moments of its original torus average.
- B. Edixhoven and P. Parent, *Semistable reduction of modular curves associated with maximal subgroups in prime level*, Documenta Math. 26 (2021), 231–269, Theorem 2.3 and §§2.2.1–2.2.4, especially equations (4), (5), (10), (12), (13): [original author PDF](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf). Only the model and its actions are used from this source; the de Rham extension, precise lattice match, second-kind vector, and Cartier calculation are proved above.

This is a paper proof. No mathematical computation has been executed locally or introduced as an unperformed numerical claim.
