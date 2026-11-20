# R965: exact original-trace calibration of the Igusa height coefficient

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: proved exact identities.** In the original $r=2$ row, the first possible height coefficient of R960 is exactly $-g_p$ times R939's complete polynomial trace, where $g_p$ is the original weak weight-four unit of R961. The proof constructs the actual intermediate Cartier form and identifies it with R956's unique opposite-deck interpolation. It retains the original full-six marking, coefficient Frobenius, and source factors. A separate explicit primitive gives a finite Jacobi-polynomial formula for $g_p$ itself.

This does not prove the height coefficient nonzero. It also does not identify the complete trace with a same-label normal derivative; R945's counterexamples to that further inference remain applicable. No new mathematical computation is executed.

## 1. Original objects and the exact statement

Keep the original row
$$
p\ge41,\qquad p\equiv11\pmod{12},\qquad
p=6N+5,\qquad d=(p-1)/2=3N+2,\qquad m=2N+1.
\tag{965.1}
$$
The original Serre application also keeps $p\equiv2,5\pmod9$. Work over $k=\mathbf F_{p^2}$, containing the original $s^2=-3$ and $\zeta=(-1+s)/2$. All geometric assertions may be checked over an algebraic closure and then descended. Set
$$
v=V_4^\dagger,\qquad F=V_{p-1}^\dagger,\qquad
g=E_4^2/v,\qquad g_p=[Q^p]g(Q).
\tag{965.2}
$$
These are the original marked forms: in particular $F$ retains the $Q^4$ oldform coefficient $-2^{p-1}\zeta^2$. The symbol $F$ is not the Hasse polynomial $H$ used below. Let $\mathcal A$ be the Hasse invariant, $\mathcal B=\partial_{p-1}\mathcal A$, and
$$
\mathcal T_wJ=6(\mathcal A\partial_wJ+w\mathcal BJ).
\tag{965.3}
$$
The unchanged original Tate expansion has
$$
\mathcal A(Q)=1,\qquad 12\mathcal B(Q)=E_2(Q^6),\qquad
\mathcal T J(Q)=\Theta_QJ(Q).
\tag{965.4}
$$

R956's unique original $\delta=\zeta^2$ form $Y_F\in S_{p+3}(H_6)$ satisfies
$$
Y_F|_\Sigma=2\,\frac{F^p}{\mathcal B^{p-3}}\Big|_\Sigma,
\qquad
\mathscr K_2Y_F=\alpha v,\qquad
\alpha=\bigl([Q^p]Y_F\bigr)^{1/p}.
\tag{965.5}
$$
Here $\Sigma$ is the complete reduced supersingular divisor on the fine full-six cover. The operator $\mathscr K_2$ includes inverse coefficient Frobenius and the original marking return. Neither $Y_F$ nor $\alpha$ is chosen by an arbitrary eigenline normalization.

Let $S$ be the complete original fine supersingular trace of R932/R956. In R939's original finite algebra put
$$
L=k[t]/(tH(t)),\qquad D=1-4t,\qquad
e_0=H(t)/H(0),
$$
$$
T=\operatorname{Tr}_{L/k}
\bigl((3-2e_0)D^{2N+2}C^{p+1}\bigr).
\tag{965.6}
$$
Thus $S^p=432T$ by R939. The factor $3-2e_0$ gives multiplicity one to $t=0$ and multiplicity three to each geometric root of $H$; the fine-cover degree and the elliptic-point contributions are already included in that equality. The polynomial $C$ is unchanged from R936/R939.

Write $\kappa_p\in\mathbf F_p$ for R960's actual coefficient of $z^{p^2}$ in multiplication by $p$ on the one-dimensional formal factor, with $z=1/u$ and the original branch. The exact identities proved here are
$$
\boxed{\quad
\alpha\in\mathbf F_p,\qquad
\kappa_p=36\alpha=36\alpha^p
=-\frac{g_p}{432}S^p=-g_pT.
\quad}
\tag{965.7}
$$
In addition, let
$$
a(x)=(1-x/4)^{N+1}\frac{H^{\rm rev}(x)}{H_N}
\in\mathbf F_p[x],\qquad
B_*=[x^{m+1}]a(x)^2.
\tag{965.8}
$$
This is the reduction of R960's normalized polynomial; $a(0)=1$ and $\deg a=m$. Then
$$
\boxed{\quad g_p=48B_*\in\mathbf F_p^\times,\qquad
\kappa_p=-48B_*T.\quad}
\tag{965.9}
$$
In particular the unit in the comparison is explicit in the original Hasse polynomial. It is not an unspecified CM period or a replacement source vector.

## 2. A homogeneous Frobenius identity at every fine supersingular point

We first prove the identity
$$
\boxed{\quad
F^{p^2}=\mathcal B^{(p-1)^2}F
\quad\text{on }\Sigma.
\quad}
\tag{965.10}
$$
This will be used on the full fine divisor, not merely on the scalar roots retained in $L$.

Every geometric supersingular elliptic curve has a model over $\mathbf F_{p^2}$ with $p^2$-power Frobenius equal to $[-p]$. A primary proof is Baker--González-Jiménez--González--Poonen, *Finiteness results for modular curves of genus at least 2*, Lemma 3.21, [author PDF, p. 15](https://math.mit.edu/~poonen/papers/finiteness.pdf). Their construction starts from a supersingular curve with Frobenius square $[-p]$ and takes a separable isogeny to the chosen geometric curve; its kernel is preserved by the scalar $[-p]$, so the quotient and the scalar Frobenius descend to $\mathbf F_{p^2}$. Rezk's *Modular isogeny complexes*, §3.8 and Proposition 3.9, [published p. 1386](https://msp.org/agt/2012/12-3/agt-v12-n3-p06-s.pdf), records the same statement.

Since $p\equiv-1\pmod6$, $[-p]$ acts trivially on the full six-torsion. After choosing that model, the transported original full-six marking is therefore defined over $k$. Choose a nonzero Hodge frame $\rho$ over $k$. The scalar evaluations of every original $k$-form in this frame belong to $k$; in particular $F_\rho^{p^2}=F_\rho$.

The genuine full-$\Gamma(6)$ weight-two form $\eta^4$, already used in R869(869.29), is defined over $\mathbf Z[1/6,\zeta_6]$ and satisfies
$$
(\eta^4)^6=\Delta.
\tag{965.11}
$$
One can check its level directly from the eta transformation law: the weight-two multiplier has values $\chi(T)=\exp(\pi i/3)$ and $\chi(S)=-1$, and factors through the abelianization $C_2\times C_3$ of $\operatorname{SL}_2(\mathbf Z/6\mathbf Z)$. Hence it is trivial on $\Gamma(6)$. Its expansion is $Q\prod_{n\ge1}(1-Q^{6n})^4$, so the integral full-six expansion principle gives the asserted field of definition. At a smooth supersingular elliptic curve its value is nonzero because $\Delta$ is nonzero.

Baker's supersingular congruence, with the exact normalization already checked in R939(939.15), gives
$$
\mathcal B_\rho^{p-1}
=-\left(\frac{-1}{p}\right)
\Delta_\rho^{(p^2-1)/12}.
\tag{965.12}
$$
The factor $12^{p-1}$ is one, so this applies to the present $\mathcal B=E_{p+1}/12$. Squaring (965.12) and using (965.11) in the $k$-rational frame gives
$$
\mathcal B_\rho^{2(p-1)}
=\Delta_\rho^{(p^2-1)/6}
=(\eta^4)_\rho^{p^2-1}=1.
\tag{965.13}
$$
As $p-1$ is even, $\mathcal B_\rho^{(p-1)^2}=1$. Together with $F_\rho^{p^2}=F_\rho$, this proves (965.10) in this frame.

Both sides of (965.10) have the same weight:
$$
p^2(p-1)=(p+1)(p-1)^2+(p-1).
$$
The equality is therefore preserved by every frame change and every geometric isomorphism back to the original marked point. This proves it on all of $\Sigma$, including $j=0$ and $j=1728$.

This argument does not assume that the coordinates or Hodge frame in the scalar $E_u$ presentation are defined over $\mathbf F_{p^2}$ at every chosen point. In particular it does not assume that $L$ is a split algebra over $k$. The rational frame is used only to establish the homogeneous identity, after which it is transported back.

## 3. The actual weight-lowering Cartier root

Use R960's homogeneous form
$$
Z=F(144\mathcal B^2-\mathcal A^2E_4)
\in S_{3p+1}(H_6),\qquad \delta Z=\zeta Z.
\tag{965.14}
$$
There is a unique cuspidal form $\mathscr UZ\in S_{p+3}$ on the same fine curve with
$$
\boxed{\quad
(\mathscr UZ)^p
=\mathcal A^{p+1}Z-\mathcal T^{p-1}Z,
\qquad
\mathscr UZ(Q)=\sum_{n\ge1}z_{pn}^{1/p}Q^n.
\quad}
\tag{965.15}
$$
Here $Z(Q)=\sum z_nQ^n$. The symbol is defined by this displayed root and does not assert a weight-preserving operator at weight $3p+1$.

For completeness, the global root follows directly from the proof of R952. Both terms on the right have weight
$$
(3p+1)+(p+1)(p-1)=p(p+3).
$$
The universal full-expansion identity $\mathcal T^p=\mathcal A^{p+1}\mathcal T$, and commutation of $\mathcal T$ with multiplication by $\mathcal A$, show that their difference is killed by $\mathcal T$. At weight divisible by $p$, the connection contribution in the scalar Serre derivative is zero. In a local Hodge frame its scalar coefficient therefore has zero ordinary differential, hence is a unique $p$th power in the function field of the smooth curve. Its root is regular because the original coefficient is regular. The roots glue with the weight-$p+3$ transition functions. At each cusp their $p$th powers vanish, so the roots are cuspidal. This proves existence and uniqueness globally, including at the Hasse zeros.

In the Tate frame the right side is $Z(Q)-\Theta_Q^{p-1}Z(Q)=\sum z_{pn}Q^{pn}$, proving the Fourier rule in (965.15). Naturality and uniqueness retain the actual tame invariants and transform a deck character by inverse Frobenius. Thus the descended original form has
$$
\delta(\mathscr UZ)=\zeta^2\mathscr UZ.
\tag{965.16}
$$
The inverse Frobenius and original determinant return are the same as in R952/R956. No coefficient-extraction map without roots or substituted tame phase is introduced.

On $\Sigma$, each Katz derivative of a weight-$w$ form is multiplication by $6w\mathcal B$. Starting from weight $3p+1$, the $p-1$ successive weight residues are $1,2,\ldots,p-1$. Wilson's identity consequently gives
$$
\mathcal T^{p-1}Z|_\Sigma
=6^{p-1}(p-1)!\,\mathcal B^{p-1}Z|_\Sigma
=-\mathcal B^{p-1}Z|_\Sigma.
$$
Since $Z|_\Sigma=144\mathcal B^2F$, (965.15) yields
$$
(\mathscr UZ)^p|_\Sigma=144\mathcal B^{p+1}F.
\tag{965.17}
$$

On the other hand, (965.5) and the homogeneous identity (965.10) give
$$
Y_F^p|_\Sigma
=2\frac{F^{p^2}}{\mathcal B^{p(p-3)}}\Big|_\Sigma
=2\mathcal B^{p+1}F|_\Sigma.
\tag{965.18}
$$
Thus $\mathscr UZ$ and $72Y_F$ have identical restrictions to the complete reduced divisor $\Sigma$. Their difference is $\mathcal A$ times a cusp form of weight four. After taking the original tame invariants this kernel is
$$
\mathcal AS_4(H_6)=k\mathcal Av,
$$
which has only the character $\delta=\zeta$, by R918 and R956(956.39). Both forms in the difference have character $\zeta^2$. Therefore
$$
\boxed{\quad \mathscr UZ=72Y_F\quad\text{globally}.\quad}
\tag{965.19}
$$
This uses the entire original weight-four invariant space, rather than a claim that an arbitrary fine-level weight-four space is one-dimensional.

## 4. The coefficient and complete-trace calibration

R960 proves, in precisely the original coordinate and phase,
$$
\kappa_p=\frac12[Q^{p^2}]Z(Q)\in\mathbf F_p.
\tag{965.20}
$$
Apply R956's actual $\mathscr K_2$ to (965.19). Its Fourier rule is again inverse-Frobenius extraction of the indices divisible by $p$. Taking the coefficient of $Q$ therefore gives
$$
z_{p^2}^{1/p^2}=72\alpha.
$$
All coefficients of $Z$ are in $k=\mathbf F_{p^2}$; hence the left side equals $z_{p^2}=2\kappa_p$. It follows that
$$
\boxed{\quad \kappa_p=36\alpha,\qquad \alpha\in\mathbf F_p.\quad}
\tag{965.21}
$$
The prime-field statement follows from R960's already proved descent of $\kappa_p$, and is not assumed from the existence of a CM eigenline.

Put $P=\langle z_v,v\rangle_X$, with the actual low principal-parts class and the complete fine Serre pairing. R956(956.44), R950, and R961(961.23) give
$$
S=\frac\alpha2P,\qquad
P^p=-\frac13\mathcal H_4(v,v),\qquad
g_p\mathcal H_4(v,v)=93312.
\tag{965.22}
$$
Every factor here is calibrated in the named original objects. Taking the $p$th power of the first equality and using the second yields
$$
S^p=-\frac{\alpha^p}{6}\mathcal H_4(v,v).
$$
Since $93312=432\cdot216$, multiplication by $-g_p/432$ gives
$$
-\frac{g_p}{432}S^p=36\alpha^p=\kappa_p.
\tag{965.23}
$$
Finally $S^p=432T$ proves (965.7). The weak coefficient $g_p$ is a unit by R961. Its nonvanishing is the low-weight assertion, whereas $\kappa_p$ and $\alpha$ still measure the particular original high Cartier boundary.

## 5. An explicit high primitive and the polynomial formula for the unit

This section proves (965.9) directly on the actual Kummer curve of R960:
$$
\mathscr I_p:\quad y^d=uD(u)^{N+1}H(u^3),
\qquad D(u)=1-4u^3.
\tag{965.24}
$$
The original branch over infinity is
$$
y=24u^2a(u^{-3})^{1/d},\qquad z=1/u=4sQ+O(Q^2).
\tag{965.25}
$$
The constant $24$ is fixed in R960 §8 by the original normalized Eisenstein lift and the Tate evaluations $E_4\sim24^2u^4$, $E_6\sim24^3u^6$; it is not an independent root choice.

Let $b(x)$ be the unique formal power series with $b(0)=1$ and $b(x)^d=a(x)^{-1}$. Through degree $m+1<p$, its coefficients are those of $a(x)^2$: one can lift $a$ integrally and reduce the binomial expansion, since $-1/d\equiv2\pmod p$ and all factorials through that degree are units. Put $b_{\le m}(x)=\sum_{i=0}^m b_ix^i$ and define the global rational function
$$
R_0=\frac y{24}\,u^{3m}b_{\le m}(u^{-3}).
\tag{965.26}
$$
The factor following $y$ is a polynomial in $u^3$, so $R_0$ has no finite pole on the normalization. At the original cusp, (965.25) and $3m+2=p$ give
$$
R_0=z^{-p}\frac{b_{\le m}(z^3)}{b(z^3)}
=z^{-p}-B_*z+O(z^4).
\tag{965.27}
$$
There are exactly $d$ unramified points above infinity, indexed by $\epsilon\in\mu_d$. At such a point the expansion of $R_0$ is $\epsilon$ times (965.27). Thus its only negative Laurent term at each point has order $p$, and $dR_0$ is regular at every point of the complete curve.

Moreover $dR_0\ne0$. If it were zero, then $R_0=h^p$ in the function field over a perfect splitting field. The function $h$ would have no finite poles and at most a simple pole at every point above infinity. The actual $\mu_d$ character of $R_0$ is $\epsilon$; since $\mu_d\subset\mathbf F_p$, the unique root $h$ has the same character. Every rational function of this character is $y f(u)$. At a finite branch point of exponent $e\in\{1,N+1\}$, regularity requires
$$
d\operatorname{ord}(f)+e\ge0.
$$
Because $0<e<d$, this requires $\operatorname{ord}(f)\ge0$. The same conclusion holds at every other finite point, so $f$ is a polynomial. But a nonzero $yf(u)$ has cusp pole order $2+\deg f\ge2$, a contradiction. This proves the asserted nonzero differential.

The actual deck action is $(u,y)\mapsto(\zeta^2u,\zeta y)$, so $dR_0$ has character $\delta=\zeta$ and $\mu_d$ character $\epsilon$. It is Cartier-exact. R958/R960 prove that the entire Cartier kernel in that character space is the line
$$
k\xi,\qquad \xi=\Phi_{p-1}(F),\qquad
\xi(Q)=F(Q)\,dQ/Q=dQ+O(Q)\,dQ.
$$
Hence $dR_0$ is a nonzero multiple of $\xi$. Comparing at the original cusp using $z=4sQ+O(Q^2)$ gives
$$
dR_0=-4sB_*\xi.
$$
In particular $B_*\ne0$, and the exact primitive
$$
R=-\frac{R_0}{4sB_*},\qquad dR=\xi
\tag{965.28}
$$
has the original expansion
$$
R(Q)=c_QQ^{-p}+O(1),\qquad [Q]R(Q)=1,\qquad
c_Q=-\frac1{(4s)^{p+1}B_*}=-\frac1{48B_*}.
\tag{965.29}
$$
There are no other negative powers in this expansion: the sole pole term in (965.27) is a $p$th power, and a change to a regular parameter preserves this property. The last equality in (965.29) uses $s^p=-s$ and $s^2=-3$.

The unchanged weak form is $g=-48u^2v=-576s u^2D$, so its actual Igusa differential is
$$
\Phi_4(g)=-96s\,u^2\frac{du}{y}.
\tag{965.30}
$$
Since $R=y f(u^3)$ with $f$ a polynomial, $R\Phi_4(g)$ has no finite pole. At the original cusp the exact original Fourier expansions give
$$
\operatorname{res} R\Phi_4(g)
=[Q^0]\,R(Q)g(Q)=c_Qg_p+1.
\tag{965.31}
$$
Indeed $g(Q)=Q^{-1}+O(Q^2)$, while (965.29) has only the negative term at $-p$ and its coefficient at $Q$ is one. Any constant term in the primitive has no effect, since $[Q^0]g=0$. At every other cusp the $\mu_d$ factors on $R$ and $\Phi_4(g)$ cancel, so the residue is again (965.31). There are $d$ such points. The global residue theorem therefore gives
$$
d(c_Qg_p+1)=0.
$$
The integer $d$ is nonzero modulo $p$. It follows that $c_Qg_p=-1$, and (965.29) proves
$$
g_p=48B_*\in\mathbf F_p^\times.
\tag{965.32}
$$
The $d$ cusp count here is the Kummer degree, not the degree twelve of the fine tame cover and not the source degree $d_1$ of R932. Each count is used only in the model to which it belongs.

## 6. The resulting finite identity and the original functional

For any permitted degree-at-most-$m$ integral lift $\widetilde a$ of (965.8), with constant term one, R960 proves that
$$
\kappa_p=\frac1p[x^{(p^2-1)/3}]\widetilde a(x)^{2p+2}\pmod p
$$
is integral after division by $p$ and independent of the chosen arithmetic lift. Combining this with (965.9) gives the fully calibrated finite identity
$$
\boxed{\quad
\frac1p[x^{(p^2-1)/3}]\widetilde a(x)^{2p+2}
=-48[x^{m+1}]a(x)^2\,
\operatorname{Tr}_{L/k}
\bigl((3-2e_0)D^{2N+2}C^{p+1}\bigr)
\quad\text{in }\mathbf F_p.
\quad}
\tag{965.33}
$$
The permission to choose an arbitrary polynomial lift here is only R960's coefficient-lift independence. It does not assert that such an arbitrary polynomial yields a smooth geometric lift of (965.24).

R939 already proves $S\in\mathbf F_p$, and (965.32) proves $g_p\in\mathbf F_p^\times$. Consequently (965.7) also says $S=-432\kappa_p/g_p$. R932's actual $r=2$ functional, with its complete original norm extension, is therefore
$$
\boxed{\quad
\lambda_h\bigl(\Phi_{p-1}(F)_{\mathrm{full}}\bigr)
=-\frac{12m_{\mathrm I}(c_h^{\mathrm F})^{1/p}}
{d_1g_p}\,\kappa_p.
\quad}
\tag{965.34}
$$
This follows by substituting $S$ in the existing equality
$\lambda_h=m_{\mathrm I}(c_h^{\mathrm F})^{1/p}S/(36d_1)$.
The actual source coefficient $c_h^{\mathrm F}$, its inverse-Frobenius root, the norm multiplier $m_{\mathrm I}$, and the fine source degree $d_1$ have not been removed or absorbed into a new normalization.

Equations (965.19), (965.21), and (965.33) identify the particular previously unknown high Cartier edge with the actual secondary height coefficient, including its unit. The unresolved assertion remains $\kappa_p\ne0$ for the required primes, equivalently $T\ne0$, a Cartier chain of length one, or formal height two. The fact that $B_*$ and $g_p$ are units supplies the comparison factor; it does not settle that assertion. Even a proof of it would leave R945's separate complete-trace-to-normal-coefficient obstruction in force.

## Exact dependencies

- [R869](R869-original-maximal-cusp-lattice-and-first-theta-layer.md), (869.29): original full-six $\eta^4$ and marked theta convention.
- [R918](R918-original-central-primitive-Igusa-layer-and-marked-weight-four-vector.md): actual full-six descent and complete one-dimensional $S_4(H_6)$ with its geometric deck character.
- [R939](R939-original-Jacobi-Hasse-and-denominator-free-supersingular-trace.md): original polynomial $H,C$, corrected frame, Baker normalization, full trace multiplicities, and prime-field descent.
- [R952](R952-exact-Cartier-formula-for-the-last-Hasse-obstruction.md): global Cartier-root construction, universal theta identity, and original inverse-Frobenius marking transport.
- [R956](R956-original-trace-as-a-fixed-low-weight-Cartier-edge-pairing.md), §§6--7: actual interpolation $Y_F$, its uniqueness in the opposite deck space, the edge $\mathscr K_2$, and the calibrated pairing with $S$.
- [R958](R958-original-r2-Cartier-matrices-and-one-moment-trace-criterion.md) and [R960](R960-original-r2-Igusa-formal-height-and-Jacobi-coefficient.md): complete actual Cartier kernel, Kummer curve, original cusp branch, height coefficient, and its finite and Fourier formulas.
- [R961](R961-actual-weak-Frobenius-unit-and-Cartier-cokernel-top.md), (961.23): exact weak low-weight unit $g_p\mathcal H_4(v,v)=93312$.
- M. H. Baker, E. González-Jiménez, J. González, B. Poonen, *Finiteness results for modular curves of genus at least 2*, American Journal of Mathematics 127 (2005), 1325--1387, Lemma 3.21; [author PDF](https://math.mit.edu/~poonen/papers/finiteness.pdf), p. 15 in that version. C. Rezk, *Modular isogeny complexes*, Algebraic & Geometric Topology 12 (2012), 1373--1403, §3.8 and Proposition 3.9, [publisher PDF](https://msp.org/agt/2012/12-3/agt-v12-n3-p06-s.pdf), p. 1386.
- A. Baker, *A supersingular congruence for modular forms*, Acta Arithmetica 86 (1998), 91--100, Theorem 1.4; [author PDF](https://www.maths.gla.ac.uk/~ajb/dvi-ps/modforms.pdf). This is the same precise supersingular congruence and normalization used in R939.

The new comparisons are proved above without assuming a height-two quotient of the Igusa Jacobian, without assigning a crystalline Frobenius matrix by analogy, and without any finite nonvanishing computation.
