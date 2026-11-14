# R201. Half-period mean-phase closure without reflection

Status: proved. This text was reconstructed from the complete proof and execution summary after the fifth executor outage on 2026-11-13. It does not claim byte identity with the original unpublished 10,925-byte proof (SHA256 ee7d5f59a40b29413895e33d4afe1fd17f0373a074f8554faa54b80dc3fe5f34). The mathematical construction below is complete. Original finite checks and their precise identities are recorded separately; they are not continuous certificates.

## 1. Data and exact definition

Keep the physical material angle $u$ and the chosen metric $ds^2+a(s)^2du^2$ fixed. Let
$$
\Theta(s,u,p)=u+\vartheta(s,u,p),\qquad \psi(s,u,p)
$$
where $\vartheta,\psi$ are $\pi$-periodic in $u$. They may have both sine and cosine modes; $\vartheta$ may also have an angularly constant term. Assume the derivatives actually used below exist and are continuous. For the Cartesian twojet, $C^2$ in $(s,u)$ suffices. Parameter derivatives require the corresponding mixed derivatives, including $\partial_p\partial_s^2$, rather than a third radial derivative.

Define the complete angular integrals
$$
C=\int_0^\pi\cos\psi\,du,\qquad S=\int_0^\pi\sin\psi\,du,\qquad
Z=C+iS,\qquad R=|Z|.
$$
Work on the open domain $R>0$. Set
$$
c_\Phi=\frac{C\cos\psi+S\sin\psi}{R},\qquad
s_\Phi=\frac{C\sin\psi-S\cos\psi}{R},
$$
and
$$
T=(-\sin\Theta\,c_\Phi,\ \cos\Theta\,c_\Phi,\ s_\Phi).
\tag{1}
$$
These equations, which use the complete functions rather than a discrete Fourier derivative, define the object. No global choice of $\arg Z$ is part of the definition.

### Theorem 1: unit tangent and closure

For every admissible $(s,p)$, $|T|=1$, $T_h(u+\pi)=-T_h(u)$ and $T_z(u+\pi)=T_z(u)$, and
$$
\int_0^{2\pi}T\,du=0.
\tag{2}
$$

Proof. The pair $(c_\Phi,s_\Phi)$ is a rotation of $(\cos\psi,\sin\psi)$, so its squared norm is one. Since $\Theta(u+\pi)=\Theta(u)+\pi$ and $\psi$ is $\pi$-periodic, the asserted transformation laws follow. The horizontal integral over $2\pi$ vanishes by antiperiodicity. The vertical half-period integral is
$$
\int_0^\pi T_z\,du=(CS-SC)/R=0.
$$
This proves (2). No reflection identity was used. $\square$

The remaining half-turn is a proper ambient rotation $Q=\operatorname{diag}(-1,-1,1)$. A construction with only this symmetry has more degrees of freedom than the old two-reflection class.

## 2. Exact inclusion of the old odd family

Suppose the old raw $\psi$ is odd in $u$ and $\pi$-periodic. Then its sine has zero integral on $[0,\pi]$: substitution $u\mapsto\pi-u$ changes its sign. Thus $S=0$. If $C>0$, equations (1) give $c_\Phi=\cos\psi$ and $s_\Phi=\sin\psi$ exactly.

Consequently adjoining zero cosine coefficients and zero constant $\vartheta$ coefficients embeds the complete old field, with all radial and angular derivatives, exactly as mathematical functions. If the old parameter family remains in this odd class and $C>0$, the old parameter columns also agree. A finite quadrature may exhibit a small nonzero computed $S$; that is a numerical evaluation difference, not a change in this exact inclusion statement.

An angularly constant addition $b(s,p)$ to $\psi$ is a genuine redundancy:
$Z\mapsto e^{ib}Z$ and $\psi\mapsto\psi+b$ cancel in (1). Omit this column in a solve. An angularly constant addition to $\vartheta$ generally rotates the horizontal tangent by a radial-dependent angle and is not this redundancy.

## 3. The admissible mean domain

For two raw phases $\psi,\psi_0$,
$$
|Z-Z_0|\le\int_0^\pi|e^{i\psi}-e^{i\psi_0}|\,du
\le\pi\|\psi-\psi_0\|_\infty.
\tag{3}
$$
Hence $R_0\ge r_0>0$ and $\pi\|\psi-\psi_0\|_\infty<r_0$ provide an explicit sufficient neighborhood on which the normalization is defined. More generally any certified positive lower bound for $C^2+S^2$ suffices.

Failure of this chart condition at a proposed phase does not prove that the surface problem has no solution. This result introduces a calculable representation, not a global existence or nonexistence assertion. It also introduces no requirement that the final $c_\Phi$ remain positive.

## 4. Complete mean-phase derivatives

Locally choose $\beta=\arg Z$ only to calculate derivatives, so $\Phi=\psi-\beta$. For any parameter or radial differentiation labels $a,b,c$,
$$
\beta_a=\Im(Z_a/Z),
\tag{4}
$$
$$
\beta_{ab}=\Im\left(Z_{ab}/Z-Z_aZ_b/Z^2\right),
\tag{5}
$$
$$
\beta_{abc}=\Im\left[
Z_{abc}/Z
-\frac{Z_{ab}Z_c+Z_{ac}Z_b+Z_{bc}Z_a}{Z^2}
+\frac{2Z_aZ_bZ_c}{Z^3}\right].
\tag{6}
$$
These follow by differentiating a local logarithm; the expressions are independent of its branch. In particular,
$$
\beta_s=\frac{CS_s-SC_s}{R^2},
$$
$$
\beta_{ss}=\frac{CS_{ss}-SC_{ss}}{R^2}
-\frac{2(CC_s+SS_s)(CS_s-SC_s)}{R^4}.
\tag{7}
$$
For a parameter $p_j$, formula (6) with $(a,b,c)=(s,s,p_j)$ gives the required parameter column of $\beta_{ss}$. It does not request $\partial_s^3$.

All the integral columns are full-function derivatives:
$$
Z_a=\int_0^\pi e^{i\psi}i\psi_a\,du,
$$
$$
Z_{ab}=\int_0^\pi e^{i\psi}(i\psi_{ab}-\psi_a\psi_b)\,du,
$$
$$
Z_{abc}=\int_0^\pi e^{i\psi}
(i\psi_{abc}-\psi_{ab}\psi_c-\psi_{ac}\psi_b-\psi_{bc}\psi_a
-i\psi_a\psi_b\psi_c)\,du.
\tag{8}
$$
Compactness of the integration interval and continuity of the stated derivatives justify differentiation under the integral. Since $\beta$ is independent of $u$,
$$
\Phi_u=\psi_u,\quad \Phi_{uu}=\psi_{uu},\quad
\Phi_{su}=\psi_{su},\quad
\Phi_s=\psi_s-\beta_s,\quad \Phi_{ss}=\psi_{ss}-\beta_{ss}.
\tag{9}
$$
The same equations apply to every parameter column.

## 5. Physical tangent twojet and all parameter columns

Write $F(\theta,\phi)=(-\sin\theta\cos\phi,\cos\theta\cos\phi,\sin\phi)$. Its derivatives are
$$
F_\theta=(-\cos\theta\cos\phi,-\sin\theta\cos\phi,0),
$$
$$
F_\phi=(\sin\theta\sin\phi,-\cos\theta\sin\phi,\cos\phi),
$$
$$
F_{\theta\theta}=(\sin\theta\cos\phi,-\cos\theta\cos\phi,0),
\quad
F_{\theta\phi}=(\cos\theta\sin\phi,\sin\theta\sin\phi,0),
\quad F_{\phi\phi}=-F.
$$
For $a,b\in\{s,u\}$,
$$
T_a=F_\theta\Theta_a+F_\phi\Phi_a,
$$
$$
T_{ab}=F_\theta\Theta_{ab}+F_\phi\Phi_{ab}
+F_{\theta\theta}\Theta_a\Theta_b
+F_{\theta\phi}(\Theta_a\Phi_b+\Phi_a\Theta_b)
-T\Phi_a\Phi_b.
\tag{10}
$$
Differentiate these finite expressions using (4)--(9) to obtain every parameter column. In particular one must include the parameter dependence of $C,S,\beta_s,\beta_{ss}$. Treating the computed phase as frozen would give incorrect columns.

An equivalent implementation uses a bivariate degree-two Taylor algebra with ordinary physical derivatives converted to Taylor coefficients by factors $1,1,1,2,1,2$, together with first-order parameter dual numbers. Algebraic operations on $C,S,R^{-1}$ avoid the branch of $\beta$ entirely. Both versions represent (10).

## 6. The complete half-period primitive

There is a unique $2\pi$-periodic primitive of $T$ whose full-period mean is zero. On $0\le u\le\pi$ it is
$$
Y_h(u)=\int_0^u T_h(v)\,dv-\frac12\int_0^\pi T_h(v)\,dv,
$$
$$
Y_z(u)=\int_0^u T_z(v)\,dv
-\frac1\pi\int_0^\pi(\pi-v)T_z(v)\,dv.
\tag{11}
$$
Extend $Y_h(u+\pi)=-Y_h(u)$ and $Y_z(u+\pi)=Y_z(u)$.

Proof. The horizontal endpoint values are opposite, so antiperiodic extension matches; their full-period mean cancels. The zero half-period integral of $T_z$ makes the vertical endpoint values equal. Fubini gives
$$
\int_0^\pi\int_0^u T_z(v)\,dv\,du
=\int_0^\pi(\pi-v)T_z(v)\,dv,
$$
which proves zero vertical mean. Differentiation gives $Y_u=T$. Any two periodic primitives differ by a constant; their zero means make that constant zero. $\square$

The same linear operator applies to $T_s,T_{ss}$ and every parameter derivative, since differentiation of the exact mean and transformation identities gives the corresponding zero-mean identities. Thus it gives $Y_s,Y_{ss}$ and all their parameter columns without omitting a mean derivative.

For normalized $t=v/\pi$, the horizontal primitive kernel is $+1/2$ to the left of the query and $-1/2$ to its right. The vertical kernel is $t$ to the left and $t-1$ to the right. These kernels are useful for rigorous cell-integral accumulation. No quarter-reflection reduction is justified for a general new field.

## 7. Cartesian twojet, metric, and symmetry of the scalar objective

Let $a>0$ and $z$ be the chosen radial functions and put
$$
X(s,u)=a(s)Y(s,u)+z(s)e_z.
$$
Then
$$
X_u=aT,\quad X_s=a_sY+aY_s+z_se_z,
$$
$$
X_{ss}=a_{ss}Y+2a_sY_s+aY_{ss}+z_{ss}e_z,
$$
$$
X_{su}=a_sT+aT_s,\qquad X_{uu}=aT_u.
\tag{12}
$$
The angular metric is exactly $G=a^2$. The remaining normalized residuals are
$$
r_E=|X_s|^2-1,\qquad r_F=X_s\cdot T.
\tag{13}
$$
Every derivative of a designed radius coefficient and of a height coefficient must also be differentiated in (12). The mean-phase construction does not justify freezing $a$ or $z$ in a Jacobian.

Equation (11) gives $X(u+\pi)=QX(u)$ with $Q=\operatorname{diag}(-1,-1,1)$. The same proper rotation applies to every Cartesian derivative and parameter column. Gram entries, principal curvatures and scalar metric/curvature objective rows are therefore $\pi$-periodic. A half-period scalar objective is legitimate; a quarter-period objective needs additional reflection identities and is not used for the new class.

## 8. Central and cut twojet matching

Suppose the new raw corrections and their first two radial derivatives vanish as complete angular functions at a central or cut interface, and the old raw fields satisfy the corresponding interface conditions. Then $Z,Z_s,Z_{ss}$ agree with their old values there. Equations (1), (7), (9), (10) show that $T,T_s,T_{ss}$ and the needed angular/mixed jets agree. Formula (11), including its full means, gives the same statement for $Y,Y_s,Y_{ss}$. With the same $a,a_s,a_{ss},z,z_s,z_{ss}$, (12) gives all six Cartesian quantities $X,X_s,X_u,X_{ss},X_{su},X_{uu}$ unchanged.

This is a preservation theorem. It does not prove an old unresolved cut seam, assign unproved radial second-fundamental-form derivatives at a degenerate cut, or turn a sampled agreement into a continuous one. Parameter twojet preservation requires the same vanishing conditions for those parameter columns.

Compactly supported $C^2$ radial spline corrections with zero endpoint twojets provide one concrete way to meet these hypotheses. The mean phase couples angular modes only at the same radial location. If a parameter's raw value and first two radial jets vanish there, all its mean-phase, tangent, primitive and Cartesian columns vanish there as well. Thus the radial band locality used in R195 is retained, although the local block is wider.

## 9. Rigorous quadrature contract

The exact definition is (1) and (11), with exact integrals. Composite Gauss evaluation is an implementation of them, not a replacement proof.

If $|\widehat Z-Z|\le\varepsilon<|\widehat Z|=\widehat R$, then
$$
R\ge\widehat R-\varepsilon,\qquad
\left|\frac ZR-\frac{\widehat Z}{\widehat R}\right|
\le\frac{2\varepsilon}{2\widehat R-\varepsilon}.
\tag{14}
$$
The second bound follows from the normalization inequality
$|x/|x|-y/|y||\le2|x-y|/(|x|+|y|)$.
For fixed raw angles it bounds the tangent error caused by the mean phase. Each radial/parameter jet requires its corresponding integral enclosure in (8), followed by the rational expressions with a positive lower bound for $R$.

The approximate phase applied to the complete raw function leaves the exact vertical half-mean
$$
\frac{\widehat C S-\widehat S C}{\widehat R},
$$
whose absolute value is at most $\varepsilon$. A cancellation in the quadrature sum alone is therefore not a closure certificate.

For a certified primitive, sum certified complete-cell integrals and a certified partial-cell integral with the kernels in §6. Preserve the weighted vertical moment and all parameter columns. A rigorous Taylor or another justified integral remainder for each complete function is sufficient. A finite DFT derivative, a sampled unit norm, or a finite Gauss sum does not supply that remainder.

## 10. Actual finite implementation evidence and scope

Before the fifth executor outage the independent seven-parameter prototype and checker completed naturally with exit 0 (session 2054, chunk e87705). The test included nonzero cosine columns, the constant-$\vartheta$ column, the redundant constant-$\psi$ diagnostic column, full half-period primitive means, physical twojets and every parameter column. The largest parameter twojet difference against centered finite differences was $1.0389522530480554\times10^{-10}$; a nonzero reflection violation $0.2053146441947865$ confirmed that the exercised family was outside the old reflection class. The exact-cut fixture difference was zero.

Those are implementation observations, with source/report identities preserved in the outage recovery record. They do not certify the quadrature remainders in §9, construct the complete strong closed surface, or assert that a genuine new-freedom LM step has already been performed. That actual R196 adapter and optimization are separate continuing work.
