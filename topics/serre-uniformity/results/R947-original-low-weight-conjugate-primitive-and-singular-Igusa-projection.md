# R947 — The original fixed-low-weight conjugate-Frobenius primitive and its singular Igusa projection

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / literature_frontier. **Status: proved paper identities for both original rows.** This continues R944. It constructs a nonzero class in the fixed-low-weight Serre-dual space, with every supersingular principal part explicit. Its resulting low-weight sum is kept distinct from R936's high-weight trace. In particular it supplies no unit-source comparison to the original normal coefficient $Q'_h(0)$.

## 1. Original objects and the complete theta cycle

Use precisely R944's fine tame base $X$, bundle $\mathscr H$, frame $\rho$, horizontal conjugate frame $\sigma_\rho$, scalar Hasse invariant $A$, and positive $K_\rho=\operatorname{KS}(\rho^2)$. Keep
$$
r\in\{2,8\},\qquad k=p+1-r,\qquad
F=V_k^\dagger,\quad V=V_{r+2}^\dagger,
$$
$$
\Omega_V=(V/\rho^{r+2})\rho^rK_\rho,\qquad
\Psi_F=\frac{(F/\rho^k)\sigma_\rho^r}{A^{r+1}}K_\rho,
$$
$$
\Omega_V=6\nabla Z+6^r r!\Psi_F.
\tag{947.1}
$$
All original prime restrictions and phases remain those of R932/R944.

The original CM Fourier series has zero coefficient modulo $p$ at every exponent divisible by $p$. Indeed $p$ is inert in $\mathbf Q(\sqrt{-3})$: an ideal whose norm is divisible by $p$ is divisible by $(p)$ and its character value contains the positive power $p^{k-1}$. The same conclusion holds after the original oldform substitution $Q\mapsto Q^4$, since $p\ne2$. Consequently
$$
\Theta_Q^{p-1}F=F.
$$
Comparing the exact modular weights by the full-six expansion principle gives
$$
\boxed{\mathcal T^{p-1}F=\mathcal A^{p+1}F.}
\tag{947.2}
$$
This identity is for the original $F$, including its coefficients, not a replacement by an unchanged-coefficient series in $Q^p$.

For any form $H$ and nonnegative integer $b$, the characteristic-$p$ Katz rule gives
$$
\mathcal T(\mathcal A^bH)=\mathcal A^b\mathcal T(H).
\tag{947.3}
$$
Indeed the derivative of $\mathcal A^b$ contributes $b\mathcal B$, while its weight contributes $(p-1)b\mathcal B$, and their sum is zero modulo $p$. In (947.3) each application uses the actual weight of its argument.

Define the named iterate of the fixed low-weight form
$$
\widetilde G=\mathcal T^{p-r-2}V,
\qquad \operatorname{wt}(\widetilde G)=p(p-r-1).
\tag{947.4}
$$
Using $\mathcal T^rF=\mathcal A^{r+1}V$, (947.2–3) yields
$$
\mathcal T^{p-2}F=\mathcal A^{r+1}\widetilde G,
\qquad
\mathcal T\widetilde G=\mathcal A^{p-r}F.
\tag{947.5}
$$
The weight in (947.4) is divisible by $p$. Therefore
$$
\boxed{\partial\widetilde G=\mathcal A^{p-r-1}F/6.}
\tag{947.6}
$$

## 2. An actual global rational primitive

Put $\widetilde g=\widetilde G/\rho^{p(p-r-1)}$, a local scalar. Because its weight is divisible by $p$, its scalar derivative in the frame $\rho$ has no connection term in characteristic $p$. Equation (947.6) reads
$$
d\widetilde g=A^{p-r-1}(F/\rho^k)K_\rho/6.
\tag{947.7}
$$
Define
$$
\boxed{
W=6Z+6^{r+1}r!\frac{\widetilde g\,\sigma_\rho^r}{A^p}.
}
\tag{947.8}
$$
The second term is frame independent: its exponent under $\rho\mapsto z\rho$ is
$-p(p-r-1)-pr+p(p-1)=0$. It is therefore a global rational section of $\operatorname{Sym}^r\mathscr H$ on the original fine tame base. As $d(A^{-p})=0$ and $\nabla\sigma_\rho=0$, equations (947.1) and (947.7) give
$$
\boxed{\nabla W=\Omega_V.}
\tag{947.9}
$$
There are no cusp poles: $A$ is a unit there and every Katz iterate in (947.8) is cuspidal. Thus the only possible poles of $W$ lie at the full supersingular divisor.

## 3. Its complete polar part at every supersingular point

At any supersingular point $P$, retain the R932 local frame and write
$$
b_P=(\mathcal B/\rho^{p+1})(P),\qquad
v_P=(V/\rho^{r+2})(P).
$$
The $p-r-2$ Katz steps in (947.4) have nonzero successive weights
$r+2,r+3,\ldots,p-1$ modulo $p$. Hence
$$
\widetilde g(P)
=6^{p-r-2}\frac{(p-1)!}{(r+1)!}\,b_P^{p-r-2}v_P
=-\frac{6^{-r-1}}{(r+1)!}\,b_P^{p-r-2}v_P.
\tag{947.10}
$$
Here Wilson's theorem and $6^{p-1}=1$ are exact symbolic identities, not finite-prime experiments.

Use the scalar Hasse invariant $A$ as local parameter, as in R932. Equation (947.7) shows that
$$
\widetilde g=\widetilde g(P)+O(A^{p-r}),
\tag{947.11}
$$
since the coefficients of degrees $1,\ldots,p-r-1$ have nonzero derivative multipliers. R944 already proves that $Z$ has pole order at most $r$. It follows that after subtracting
$$
\frac{6^{r+1}r!\widetilde g(P)}{A^p}\sigma_\rho^r
$$
from $W$, the remaining pole order is at most $r<p$. Its connection derivative is regular by (947.9), and the subtracted term is horizontal. A vector-valued meromorphic section with pole order $d$ strictly between $0$ and $p$ cannot have a regular derivative for a regular connection: in any regular local basis the derivative of its leading term has nonzero coefficient $-d$ and pole order $d+1$, which cannot be canceled by the regular connection matrix. Thus the remainder is regular.

Consequently the **entire** polar part of $W$, not just its leading scalar value, is
$$
\boxed{
\operatorname{pp}_P(W)
=-\frac{v_Pb_P^{p-r-2}}{r+1}\frac{\sigma_\rho^r}{A^p}
\quad\bmod\text{regular sections}.
}
\tag{947.12}
$$
The full local section $\sigma_\rho^r$, not only its value at $P$, occurs here. This matters because replacing it by its value can change lower polar coefficients. At any of the already proved elliptic zeros of $V$, (947.12) is zero and $W$ is regular there; the point is still included in the construction.

## 4. The resulting fixed-low-weight class and its nonzero image

Let
$$
\mu_P=\left(-\frac{v_Pb_P^{p-r-2}}{r+1}\right)^{1/p}.
\tag{947.13}
$$
The root is the unique one in the perfect original residue field. The principal parts
$$
u_P=\frac{\mu_P}{A}\rho^{-r}
\tag{947.14}
$$
are independent of the chosen local frame modulo regular sections. Here is the full compatibility check. If $\rho'=z\rho$ with $z$ a regular unit, then
$$
A'=z^{1-p}A,\qquad
b'_P=z_P^{-p-1}b_P,\qquad v'_P=z_P^{-r-2}v_P.
$$
Writing $L_P=-v_Pb_P^{p-r-2}/(r+1)$, the exponent in its change of frame is
$-(r+2)-(p+1)(p-r-2)=p(-p+r+1)$. Hence
$$
L'_P=z_P^{p(-p+r+1)}L_P,\qquad
\mu'_P=z_P^{-p+r+1}\mu_P,
$$
and therefore
$$
u'_P-u_P
=\frac{\mu_P}{A}
\left(\left(\frac z{z_P}\right)^{p-1-r}-1\right)\rho^{-r}.
$$
The expression in parentheses vanishes at $P$, so it is divisible by the local parameter $A$ and this difference is regular. The construction also commutes with residue-field extension and Galois action, because the inverse $p$th-power map on the perfect residue fields is unique. Thus these compatible principal parts define a global class $z_V\in H^1(X,\omega^{-r})$ by the usual connecting map. The relative-Frobenius inclusion of R944 induces the $p$-semilinear map
$$
\mathsf F_r:H^1(X,\omega^{-r})
\longrightarrow H^1_{\mathrm{dR}}(X,\operatorname{Sym}^r\mathscr H),
$$
$$
(u_{ij}\rho^{-r})\longmapsto(u_{ij}^p\sigma_\rho^r,0).
\tag{947.15}
$$
This map uses the same relative conjugate line as R944, and is not a divided crystalline Frobenius. Its semilinearity sends $c$ to $c^p$, including constants in the original coefficient field.

Equation (947.12) and the rational primitive (947.9) identify the image exactly:
$$
\boxed{\mathsf F_r(z_V)=[\Omega_V].}
\tag{947.16}
$$
To verify the sign, use $W$ as primitive away from $\mathrm{SS}$ and $W-(\mu_P/A)^p\sigma_\rho^r$ near $P$, where (947.12) proves regularity. Their difference is $(\mu_P/A)^p\sigma_\rho^r$, the image of the section $u_P$ under the relative conjugate map. With R932's Čech convention $b_i-b_j$, this is precisely the inverse-Frobenius construction in (947.15), with derivative $\Omega_V$.

### 4.1 A self-contained proof that no global primitive exists

Use the logarithmic complex
$$
\operatorname{Sym}^r\mathscr H
\xrightarrow{\nabla}
\operatorname{Sym}^r\mathscr H\otimes\Omega_X^1(\log C)
$$
on the compactified fine tame curve. The level is six, prime to $p$, so the canonical Hodge extension and the logarithmic Kodaira–Spencer isomorphism are valid at the cusps as well. R936 gives $\deg\omega=6$ on each geometric connected fine component; only its strict positivity is needed here. The proof requires $r<p$ so $1,\ldots,r$ are units, which is satisfied by $r=2,8$ and $p\ge41$. No stronger bound, Hodge-to-de Rham degeneration, or injectivity of (947.15) is assumed.

On $\operatorname{Sym}^r\mathscr H$ use the Hodge filtration $\mathrm{Fil}^i$, with
$$
\operatorname{gr}^i\simeq\omega^{2i-r}.
$$
For $i\ge1$, the component of $\nabla s$ in $\operatorname{gr}^{i-1}\otimes\Omega^1_X(\log C)$ for $s\in\mathrm{Fil}^i$ depends only on $\operatorname{gr}^i(s)$ and is $i$ times Kodaira–Spencer. To see the coefficient directly, use a local Hodge frame $\rho$ and any complementary frame $\nu$. The lowest monomial in $\mathrm{Fil}^i$ is $\rho^i\nu^{r-i}$; the only contribution lowering its Hodge index is replacing one of its $i$ copies of $\rho$ by the quotient component of $\nabla\rho$. Derivatives of its scalar coefficient do not lower the Hodge index. Thus this graded map is the isomorphism
$$
i\operatorname{KS}:\omega^{2i-r}
\longrightarrow\omega^{2i-2-r}\otimes\Omega_X^1(\log C).
$$

Suppose $\Omega_V=\nabla s$ for a global regular section $s$. Its image in $\operatorname{gr}^0=\omega^{-r}$ is zero because this line bundle has negative degree. Hence $s\in\mathrm{Fil}^1$. If inductively $s\in\mathrm{Fil}^i$ for $1\le i\le r$, the equation $\nabla s=\Omega_V\in\mathrm{Fil}^r$ makes its $\operatorname{gr}^{i-1}$ component zero. The displayed isomorphism forces $\operatorname{gr}^i(s)=0$, so $s\in\mathrm{Fil}^{i+1}$. At the last step $s=0$, contradicting the nonzero original $V$.

This also proves that $\Omega_V$ is nonzero in logarithmic de Rham hypercohomology. Indeed a degree-zero Čech cochain which is a coboundary of the global cocycle $(0,\Omega_V)$ must have zero differences on every overlap, so its local sections glue to precisely such a global $s$. This argument does not use degeneration of a spectral sequence. Since $V$ is cuspidal, $\Omega_V$ actually lies in $\operatorname{Sym}^r\mathscr H\otimes\Omega_X^1$. It therefore is a degree-one cocycle in the compact-support logarithmic complex
$$
\operatorname{Sym}^r\mathscr H(-C)
\xrightarrow{\nabla}
\operatorname{Sym}^r\mathscr H\otimes\Omega_X^1,
$$
so its nonzero logarithmic class belongs to the parabolic image as claimed. Equation (947.16) now proves
$$
z_V\ne0.
\tag{947.17}
$$
No claim that (947.15) is injective on all coefficient cohomology is required for this implication.

## 5. Exact projection back to the original Igusa objects

Use R944's ordinary Igusa basis $e=a\rho$, $f=a^{-p}\sigma_\rho$, and its normalized symmetric-power pairing. On the ordinary locus define the horizontal projection
$$
P_r(s)=\langle s,f^r\rangle_r.
\tag{947.18a}
$$
For the original scalar Igusa differentials one has
$$
\Phi_{r+2}(V)=h_r\eta/6,\qquad \Phi_k(F)=h_0\eta/6.
$$
Since $\langle e^r,f^r\rangle_r=1$ and every monomial containing $f$ pairs to zero with $f^r$, the exact identities are
$$
\boxed{
P_r(\Omega_V)=6\Phi_{r+2}(V),\quad
P_r(Z)=G/\mathfrak a^{rp},\quad
P_r(\Psi_F)=0.
}
\tag{947.18b}
$$
Here $G/\mathfrak a^{rp}$ means the original scalar quotient, as in R932. The adjoint horizontal inclusion $j_r(h)=hf^r$ satisfies
$$
\boxed{j_r(\Phi_k(F))=\Psi_F/6.}
\tag{947.18c}
$$
Thus projecting the exact R944 homotopy recovers precisely
$$
\Phi_{r+2}(V)=d(G/\mathfrak a^{rp}),
\tag{947.18d}
$$
the rational-primitive identity of R932. The outside factor $1/6$ in R932(932.7) is included in each displayed $\Phi$; $\Omega_V$ remains in the explicitly stated KS normalization of R944. This is an explicit comparison of the original sources, not just a matching of Hecke eigenvalues.

The projection is not regular at supersingular points. In the original Igusa uniformizer $a$, its horizontal factor is $f^r=a^{-rp}\sigma_\rho^r$. It can therefore have pole order $rp$, even on a regular vector-valued section. In particular it annihilates the entire horizontal $p$th-power principal part (947.12), because $\langle\sigma_\rho^r,\sigma_\rho^r\rangle_r=0$, while $P_r(W)=6G/\mathfrak a^{rp}$ still has the original R932 poles. Those poles come from applying the singular projection to the regular remainder after (947.12) is subtracted. Consequently (947.18b–c) cannot be promoted to an uncorrected global cohomological adjunction across $\mathrm{SS}$. This is a specific local boundary term which any proposed crystalline-pairing comparison must compute.

## 6. Its actual Serre pairing and the distinction from the original high-weight trace

For any fixed-low-weight cusp form $U$ of weight $r+2$, its vector-free Serre-dual differential is $(U/\rho^{r+2})\rho^rK_\rho$. The principal parts (947.14) give the exact pairing
$$
\langle z_V,U\rangle
=\sum_{P\in\mathrm{SS}(X)}
\frac{\mu_P\,(U/\rho^{r+2})(P)}{b_P},
\tag{947.18}
$$
because $K_\rho=dA/b_P$ to leading order. In particular
$$
\boxed{
\langle z_V,V\rangle^p
=-\frac1{r+1}\sum_{P\in\mathrm{SS}(X)}
\frac{v_P^{p+1}}{b_P^{r+2}}.
}
\tag{947.19}
$$
Every supersingular point on the same fine tame curve is included, and the formula is Hodge-frame independent. This is a fixed-low-weight CM pairing with an explicitly proved source. Its nonzero class $z_V$ alone does not imply that its value on $V$ is nonzero; a correctly transported perfect pairing on the precise one-dimensional Hecke component would still have to be supplied for that assertion.

The sum in (947.19) uses $V$ and denominator exponent $r+2$. R936's original functional instead uses
$$
\sum_P\frac{F_P^{p+1}}{b_P^{p+1-r}}.
$$
These are different sums. The present proof does not identify them, multiply one into the other by an unnamed unit, or identify either one with the original same-label normal coefficient $Q'_h(0)$. The newly observed same-label failures of that latter proposed comparison are therefore not contradicted by this construction. All actual fine degrees, Igusa part counts, determinant corrections, and the original unknown functional scale remain outside the present statement as in R932.

Dependencies: R913's original inert-prime CM source; R932's original Katz operator, full companion identity, and Čech convention; R944's complete Gauss–Manin homotopy, frame transformation laws, and pole bounds. No numerical arithmetic was executed in this proof.
