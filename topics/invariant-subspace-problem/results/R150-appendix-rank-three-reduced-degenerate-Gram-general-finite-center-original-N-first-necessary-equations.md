# R150 appendix: original first derivatives of N for every remaining finite central H source

AI-assisted GPT-6 Astra Pro; Astra-ISP-347c-20261126; 2026-11-26 UTC.

Sources: [original Gaussian reduction](R150-appendix-rank-three-reduced-second-cumulant-degenerate-gram-essential-six-gaussian-reduction.md), [full phase classification](R150-appendix-rank-three-reduced-degenerate-Gram-zero-hp-finite-phase-classification.md), [central-zero exclusion](R150-appendix-rank-three-reduced-degenerate-Gram-central-zero-exclusion.md), [central-two exclusion](R150-appendix-rank-three-reduced-degenerate-Gram-central-two-exclusion.md), and the [self-contained original N-first source](../notes/2026-11-26-reduced-H3-general-finite-center-original-N-first-Ke3-347c.py).

## Status and scope

**Status: proved original necessary reduction. Its new characteristic-zero unit gate has been launched; no completed unit identity is claimed here.** The equations below retain the original central source \(c=-6\) and every zero of a transformed leading coefficient. They use the original primitive phase before squaring it. No finite-field conclusion or earlier bounded timeout is used as an exclusion.

This continues the reduced rank-three H, degenerate-Gram, \(Hp=0\), essential-six branch. The previous Gaussian and finite-phase classifications give

$
F=1,\quad H=\tfrac12(z_1^2+z_2^2+z_3^2),\quad
V=\tfrac12(u^3+v^3),
$
$
B_H=\begin{pmatrix}0&g&h\\g&0&0\\h&0&0\end{pmatrix},
\quad gh\ne0,\quad g^2+h^2=-1,\quad 2e^3=-1,
$
$
(z_iKu)=(C_1,gr,-hr),\quad
(z_iKv)=(-\omega^2C_1,-\omega gr,\omega hr),
$
$
\omega^2+\omega+1=0,\quad
\delta=2g^2+1,\quad\delta^2=-e^2,\quad
2\delta C_1r=1,\quad C_1^2=\omega/(2e).
\tag{0.1}
$

The aligned phase and every H source at infinity have already been excluded. The original finite central sources 0 and 2 have also been excluded by their separate complete rational gates. We retain an arbitrary remaining finite original central source \(c\ne0,2\), including \(c=-6\).

The original Gaussian normalization also gives \(p(u)=p(v)=e\) and \(V_p=e(u^2+v^2)/2\), as proved in §2.2 of the cited Gaussian reduction. These are the original values used in §5 below.

The support vectors \(y,z_1,z_2,z_3,u,v\) form a basis. Hence all five H and V source points are distinct and every displayed representative scale is nonzero.

## 1. Original gradients and the exact changed kernel

For \(p=Ky\), \(F=\tfrac12y^TKy\), the original expressions are

$
\begin{aligned}
\Gamma={}&
(F^2-2p^THp+2\operatorname{tr}((KH)^2))y
-4FHp+8HKHp\\
&+4V(p,p,\cdot)-8V:(KHK),
\end{aligned}
$
$
N=Fyy^T-2FH-2\{y(Hp)^T+(Hp)y^T\}+4HKH+4V_p,
\tag{1.1}
$
$
T_3=y^3-6yH+4V.
$

Original criticality requires \(\Gamma=0\), the entire polar identity
\(k_t^TNk_t=0\), and the highest polar identity
\(P(t)^3-6P(t)\mathcal H(t)+4V(k_t,k_t,k_t)=0\).
In the present branch \(F=1\), \(Hp=0\), so the full quadratic expression becomes

$
N=yy^T-2H+4HKH+4V_p.
\tag{1.2}
$

All \(V_p\) terms are retained below. We use necessary consequences of (1.2), without asserting that they alone imply the full critical system.

Write \(u(t)=(1,t,\ldots,t^5)^T\), \(u(\infty)=e_5\), with original

$
K=\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix}.
$

Use the exact homogeneous change of basis

$
S(c)u(t)=t^5u(c+1/t),\qquad
S(c)_{ij}=
\begin{cases}
\binom{i}{5-j}c^{i-5+j},&i\ge5-j,\\
0,&i<5-j.
\end{cases}
$

It is invertible for every \(c\). Express the original tensors in this basis, with changed bilinear form \(K_c=S(c)^TKS(c)\). Pairings, gradients, \(F\), \(Hp=0\) and essential dimension are preserved under this simultaneous change. There is no assertion that the old \(K\) itself is invariant.

The central source \(c\) becomes infinity. Every other source becomes finite; an original source at infinity becomes 0 and remains allowed. Set

$
z_1=\lambda_1u(\infty),\quad
z_2=\lambda_2u(a),\quad z_3=\lambda_3u(b),\quad
u=\rho u(\alpha),\quad v=\sigma u(\beta)
\tag{1.3}
$

in the new coordinates.

For this section only, use \(a,b\) as the two H roots; later their product is denoted \(b_{\rm s}\). Define

$
a_3=-c^2(c-2)(c+6),\quad
a_{21}=-2c(c^2+3c-6),\quad
a_{20}=-6c^2-12c+32,
$
$
Q_c(X,Z)=
a_3Z^3+(a_{21}X+a_{20})Z^2
+(-5X^2-6(c+1)X-5)Z+(c+1)X^3+X^2.
\tag{1.4}
$

The entire changed physical kernel is

$
k(s,t)=u(s)^TK_cu(t)=-(s-t)^2Q_c(s+t,st).
\tag{1.5}
$

Its two highest coefficients in \(t\) are

$
L(s)=[t^5]k(s,t)=-a_3s^3-a_{21}s^2+5s-c-1,
$
$
M(s)=[t^4]k(s,t)=2a_3s^4+a_{21}s^3-a_{20}s^2+5(c+1)s-1.
\tag{1.6}
$

The frozen source checks (1.5) against the full original matrix expression
\(\sum K_{ij}s^{5-i}(cs+1)^it^{5-j}(ct+1)^j\), and checks both coefficients (1.6). No coefficient of \(Q_c\) is divided out. In particular \(a_3=0\) at \(c=-6\) is retained.

## 2. Root-free quadratic trace notation

Put

$
A=a+b,\quad b_{\rm s}=ab,\qquad
x=\alpha+\beta,\quad z=\alpha\beta.
$

The source code calls \(b_{\rm s}\) simply \(b\). Work with the two monic source algebras

$
H_q(s)=s^2-As+b_{\rm s},\qquad
V_q(t)=t^2-xt+z.
\tag{2.1}
$

For a linear remainder \(f_0+f_1s\) modulo \(H_q\), define

$
\operatorname{Tr}_H(f)=2f_0+Af_1,\quad
\overline f=f_0+f_1(A-s),\quad
\operatorname{Nm}_H(f)=f_0^2+Af_0f_1+b_{\rm s}f_1^2.
$

Similarly, in the V algebra replace \(A,b_{\rm s},s\) by \(x,z,t\).
These operations are polynomial identities before selecting any roots. At a physical point the traces are sums over the two distinct roots and the norms are products.

Define

$
E_0=\operatorname{Nm}_H L=L(a)L(b),\quad
E_V=\operatorname{Nm}_V L=L(\alpha)L(\beta),
$
$
D_H=A^2-4b_{\rm s},\quad D_V=x^2-4z,\quad
k_V=-(x^2-4z)Q_c(x,z)=k(\alpha,\beta).
\tag{2.2}
$

The original Gaussian pairings imply

$
D_HE_0E_Vk_V\ne0.
\tag{2.3}
$

Indeed the H roots are distinct; \(g,h,C_1,-\omega^2C_1\) give all four nonzero central pairings, and \(e=\rho\sigma k_V\ne0\).
Every endpoint/V pairing is also nonzero by (0.1).

## 3. The complete original source cubic with no leading chart restriction

The zero H edge is exactly

$
Q_c(A,b_{\rm s})=0
\tag{3.1}
$

because \(a\ne b\). No monic normalization in \(b_{\rm s}\) is made.

Define the negative endpoint-polar sum

$
N_H(t)=-\{L(b)k(a,t)+L(a)k(b,t)\}
       =-\operatorname{Tr}_H(\overline L\,k(s,t)).
\tag{3.2}
$

Its leading coefficient is \(-2E_0\), a paid nonzero quantity. Its remainder modulo the monic \(t^2-At+b_{\rm s}\) is the exact universal identity

$
\operatorname{Rem}_{H_q(t)}N_H(t)
=D_HQ_c(A,b_{\rm s})\,\operatorname{Rem}_{H_q(t)}L(t).
\tag{3.3}
$

To check (3.3), evaluate at \(a,b\): both diagonal kernel values vanish, and
\(k(a,b)=-D_HQ_c(A,b_{\rm s})\). The source also checks the complete polynomial identity by exact monic division.

Let \(C(t)\) be the quotient in this division. It is a cubic with leading coefficient \(-2E_0\). The original endpoint pairings give \(N_H(\alpha)=N_H(\beta)=0\). The V roots are distinct from the H roots. Hence the complete V quadratic divides \(C(t)\). The two coefficients of

$
\operatorname{Rem}_{V_q(t)}C(t)=0
\tag{3.4}
$

are the first two source equations. This retains all coincidences of the unselected third cubic root with either V root. No cubic discriminant and no leading coefficient of \(Q_c\) is inverted.

## 4. The original primitive phase before squaring it

At the V roots put

$
F_a(t)=k(a,t)/(L(a)L(t)),\qquad
F_b(t)=k(b,t)/(L(b)L(t)).
$

All denominators are original physical units. From (0.1),

$
F_a(\alpha)=T_0,\quad F_a(\beta)=\omega^2T_0,\quad
F_b(\alpha)=-T_0,\quad F_b(\beta)=-\omega^2T_0,
\quad T_0=\lambda_1^2r/C_1\ne0.
\tag{4.1}
$

Since \((1+\omega^2)^2=\omega^2\),

$
\{F_a(\alpha)+F_a(\beta)\}^2
=F_a(\alpha)F_a(\beta).
\tag{4.2}
$

This uses the original primitive ratio, not only the ratio of its squares.

Define the full degree-at-most-five polynomial

$
V_*(s)=L(\beta)k(s,\alpha)+L(\alpha)k(s,\beta)
      =\operatorname{Tr}_V(\overline L\,k(s,t)),
$
$
B_*(s)=\operatorname{Nm}_V k(s,t)
      =k(s,\alpha)k(s,\beta).
\tag{4.3}
$

At \(s=a\), \(V_*(a)=L(a)E_V\{F_a(\alpha)+F_a(\beta)\}\), and
\(B_*(a)=L(a)^2E_VF_a(\alpha)F_a(\beta)\). Thus (4.2), and likewise its H-swapped version, give

$
\boxed{
\operatorname{Rem}_{H_q(s)}
\{V_*(s)^2-E_VB_*(s)\}=0.
}
\tag{4.4}
$

The original V pairing gives

$
2eE_V^2F_a(\alpha)F_a(\beta)=k_V^2.
$

For example, it follows from
$
\lambda_1^2=-k_V/(2e^2E_V),\quad
T_0=-\omega^2k_V/(2e\delta E_V),\quad
\delta^2=-e^2,\quad 2e^3=-1.
$
Combining it with (4.2) gives the stronger low-degree norm equations

$
\boxed{
\operatorname{Rem}_{H_q(s)}
\{2eV_*(s)^2-k_V^2L(s)^2\}=0.
}
\tag{4.5}
$

Each box denotes both coefficients of a linear H remainder. They have coefficients in the fixed cubic field

$
K_e=\mathbb Q[e]/(2e^3+1).
\tag{4.6}
$

This is a field: setting \(w=1/e\) gives \(w^3+2=0\), Eisenstein at 2. Every embedding of this field into \(\mathbb C\) is retained; no root of \(e\) or \(\omega\) is selected.

There is also a useful exact formula for the signed H Gram parameter:

$
\boxed{
\delta_a:=\frac{V_*(a)}{L(a)k_V}=\delta,\qquad
\delta_b:=\frac{V_*(b)}{L(b)k_V}=-\delta.
}
\tag{4.7}
$

To prove it, write \(S_a=F_a(\alpha)+F_a(\beta)=-\omega T_0\).
The displayed formula for \(T_0\) yields
\(\delta=k_V/(2eE_VS_a)\). Equation (4.2) and the original norm give
\(2eE_V^2S_a^2=k_V^2\), so \(\delta=E_VS_a/k_V\), proving the first formula. The second follows from \(F_b=-F_a\) at both V roots.

Equations (4.4)--(4.5) also force the endpoint/V norms nonzero under (2.3). Their use does not silently remove a new source fiber.

## 5. Original N first derivatives at the two finite H endpoints

Set \(\lambda=\lambda_1^2\ne0\). The squared H representative scales are

$
\lambda_2^2=\frac{\delta-1}{2\lambda L(a)^2},\qquad
\lambda_3^2=\frac{-\delta-1}{2\lambda L(b)^2},
\quad \lambda=-\frac{k_V}{2e^2E_V}.
\tag{5.1}
$

Let \(\mathcal N(t)=u(t)^TK_cNK_cu(t)\) be the original quadratic polar.
At either H root \(s\), \(P(s)=0\) by \(Hp=0\), so the derivative of \(P(t)^2\) at \(s\) vanishes.

First take \(s=a\), with the other root \(j=b\). The diagonal kernel has a double zero, so the contributions from \(k(a,t)\) to the first derivative at \(a\) vanish. Also \(k(b,a)=0\). Directly from the full expression (1.2),

$
(-2\mathcal H)'(a)=-2\lambda L(a)L'(a),
$
$
(4HKH)_{\rm pol}'(a)
=-(\delta+1)L(a)\frac{\partial_a k(a,b)}{L(b)}.
\tag{5.2}
$

The entire third-cumulant term is

$
4(V_p)_{\rm pol}=2e\{(\rho k(\alpha,t))^2+
(\sigma k(\beta,t))^2\}.
$

Here
$
\rho^2=\frac{\omega}{2e\lambda L(\alpha)^2},\quad
\sigma^2=\frac{\omega^2}{2e\lambda L(\beta)^2},
$
and (4.1) gives
$
\omega=-\frac{V_*(a)}{L(\beta)k(a,\alpha)},\quad
\omega^2=-\frac{V_*(a)}{L(\alpha)k(a,\beta)}.
$
Therefore its full derivative is

$
\{4(V_p)_{\rm pol}\}'(a)
=-\frac{2V_*(a)V_*'(a)}{\lambda E_V^2}.
\tag{5.3}
$

No V term has been discarded. In (5.3), \(V_*'\) is the derivative of the full polynomial (4.3) before reducing by the H quadratic.

Combining (5.2)--(5.3), and using (4.7), gives for either \(s=a,b\), with the other root \(j\),

$
2\lambda L(s)L'(s)+
\left(\frac{V_*(s)}{k_V}+L(s)\right)
 \frac{\partial_s k(s,j)}{L(j)}
+\frac{2V_*(s)V_*'(s)}{\lambda E_V^2}=0.
\tag{5.4}
$

Multiply by the paid factor \(e^2k_VE_VL(j)\), insert (5.1), and use
\(-4e^4=2e\). The result is

$
\boxed{
G(s):=
-k_V^2L(j)L(s)L'(s)
+e^2E_V\{V_*(s)+k_VL(s)\}\partial_s k(s,j)
+2eL(j)V_*(s)V_*'(s)=0.
}
\tag{5.5}
$

On the original zero edge (3.1),

$
\partial_s k(s,j)
=-D_H\{Q_X(A,b_{\rm s})+jQ_Z(A,b_{\rm s})\},
\quad j=A-s.
\tag{5.6}
$

This follows by differentiating (1.5) with the other endpoint held fixed; the additional term proportional to \(Q_c(A,b_{\rm s})\) vanishes on (3.1).

Substitute \(j=A-s\), use (5.6), differentiate \(V_*\) before reduction, and take both coefficients of

$
\boxed{\operatorname{Rem}_{H_q(s)}G(s)=0.}
\tag{5.7}
$

These are the two finite-H first-derivative equations in the frozen input.
The source also checks the universal identity replacing the pre-field term
\(-4e^4L(j)V_*V_*'\) by \(2eL(j)V_*V_*'\); the difference is exactly
\(-2e(2e^3+1)L(j)V_*V_*'\).

## 6. Original N first derivative at the central source infinity

Since \(P(\infty)=0\), the affine polynomial \(P(t)\) has degree at most four, and its square has degree at most eight. The degree of \(L\) is at most three, even when its leading coefficients vanish. Because only the two central H edges are nonzero, the polar of \(HKH\) has degree at most eight as well.

Thus the coefficient of \(t^9\) in the full original \(\mathcal N(t)\) comes exactly from \(-2H+4V_p\). Put \(\phi(s)=M(s)/L(s)\). A direct coefficient calculation using (0.1) gives

$
\boxed{
\delta\{\phi(a)-\phi(b)\}
-\{\phi(a)+\phi(b)\}
-2\{\omega\phi(\alpha)+\omega^2\phi(\beta)\}=0.
}
\tag{6.1}
$

For example the endpoint H contribution is
\(-2(g^2\phi(a)+h^2\phi(b))/\lambda\), and the complete V contribution is
\(2(\omega\phi(\alpha)+\omega^2\phi(\beta))/\lambda\), giving (6.1).

We now remove all roots and \(\omega\). Define the polynomial in the H variable

$
R_*(s)=\operatorname{Tr}_V
\{M(t)\,\overline{k(s,t)}\}.
\tag{6.2}
$

The conjugate and trace are in the V quadratic algebra. Consequently

$
\operatorname{Tr}_V\frac{M(t)}{k(s,t)}
=\frac{R_*(s)}{B_*(s)}
$

at either H endpoint; its denominator is nonzero by the original pairings.

At \(s=a\), the primitive ratio formulas give

$
\omega\phi(\alpha)+\omega^2\phi(\beta)
=-\frac{V_*(a)}{E_V}\frac{R_*(a)}{B_*(a)}
=-\frac{2eV_*(a)R_*(a)}{k_V^2L(a)^2}.
\tag{6.3}
$

The last equality uses both (4.4) and (4.5). The same formula holds at \(b\). Averaging the two expressions in (6.3) gives

$
\omega\phi(\alpha)+\omega^2\phi(\beta)
=-\frac e{k_V^2}
\operatorname{Tr}_H\frac{V_*R_*}{L^2}.
$

Also (4.7) gives

$
\delta\{\phi(a)-\phi(b)\}
=\frac1{k_V}\operatorname{Tr}_H\frac{V_*M}{L^2}.
$

Let \(\overline L\) denote the H conjugate of the H-linear remainder of \(L\). Its norm is \(E_0\), so \(1/L=\overline L/E_0\). Multiplication of (6.1) by the paid \(k_V^2E_0^2\) yields the polynomial equation

$
\boxed{
D_c=
k_V\operatorname{Tr}_H(V_*M\overline L^{\,2})
-k_V^2E_0\operatorname{Tr}_H(M\overline L)
+2e\operatorname{Tr}_H(V_*R_*\overline L^{\,2})=0.
}
\tag{6.4}
$

Every reduction, trace, conjugation and multiplication in this formula is performed in a monic quadratic algebra. No endpoint or V square root is chosen. The source verifies the full quadratic norm identities used to clear the inverses.

## 7. The precise original necessary ideal and paid localization

All coefficients now lie in \(K_e[c,A,b_{\rm s},x,z]\). The necessary ideal is generated by

1. the original zero H edge (3.1);
2. both V source remainder coefficients (3.4);
3. both primitive phase remainder coefficients (4.4);
4. both original norm remainder coefficients (4.5);
5. both finite-H derivative remainder coefficients (5.7);
6. the original central derivative (6.4).

Zero polynomials are redundant and may be omitted. The source cancels only nonzero integer contents, checking each scalar division exactly.

The sole saturation factor is

$
\boxed{
\Pi=c(c-2)D_HE_0E_Vk_V\ne0.
}
\tag{7.1}
$

Here \(c=0,2\) are already excluded by their separately executed complete theorems. Every other factor is an original physical unit proved in (2.3). In particular \((c+6)\), \(a_3\), transformed source parameters, and all unselected-root discriminants are absent. The unresolved old \(c=-6\) norm chart and its leading-zero boundary are both retained by the new global input.

Adjoin one inverse variable \(n\) and the equation \(n\Pi-1=0\).
This is a necessary ideal, not a claimed converse characterization of the entire critical system. A unit identity for this larger necessary system is sufficient for physical exclusion; no unproved converse is needed.

## 8. New exact gate and pending unit result

The self-contained frozen source is Git blob

0c016a3cbd42a0aafc3858c9953e5293742bdf17.

It builds the original changed kernel, the two monic source algebras, every phase/norm/derivative equation above, and all exact quotient identities from scratch in integer FLINT polynomials. It does not run or rely on a finite-field Gröbner basis.

It then constructs Singular's coefficient field \(K_e\) with
\(\mathrm{minpoly}=(2e^3+1)/2\), verifies the field relation, verifies a small exact lift identity, and requests a transformation vector \(C\) for the actual displayed ideal \(I\). Success is accepted only after explicitly multiplying

$
\operatorname{matrix}(I)\,C=[1]
$

in that same characteristic-zero field, checking the matrix dimensions and equality, receiving all three verification markers as complete output lines, and detecting no Singular error line.

The new gate has a 900-second child limit and a 4 GiB address-space bound. A timeout or failure would be recorded as unresolved. The three earlier H21 timeouts and the different \(c=-6\) rational-norm timeout are not rerun here; this is a different original equation set with the three N first derivatives and the original, unsquared primitive phase.

At present the mathematical result of this document is the proved original necessary reduction (3.1), (3.4), (4.4), (4.5), (5.7), (6.4), with the fully paid localization (7.1). An exclusion may be stated only after the new exact unit identity has actually been obtained. The broader R150 Bell task and ordinary invariant-subspace problem remain unfinished.

The frozen source was launched from commit 7850ab6bf674840c056b5f4c739429f35c0fdc4f in Actions run 45827161540, job 139934167647. This launch identifies the pending computation; it is not a success receipt or a physical exclusion.
