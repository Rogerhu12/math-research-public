# R150 appendix: labelled physical sources and the original N and highest first derivatives

作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

## Status and purpose

**Status: proved necessary reduction on the entire remaining finite-central chart; the exact unit gate finished unresolved after its 900-second child limit; no unit certificate was obtained.** This replaces the large expanded trace input by individually labelled physical source points and the finite constant Gram field. It also retains the original highest first derivative at each V source. No new physical open set is introduced.

The prior N-first input actually reached its 4 GiB bound without a unit certificate. That failure remains unresolved; it does not affect the exact original identities. The present source changes coordinates and equations instead of rerunning that input.

## 1. Original setting and normalization

Use $u(t)=(1,t,\ldots,t^5)^T$, $u(\infty)=e_5$, with

$$
K=\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix}.
$$

The original definitions are $p=Ky$, $F=\tfrac12y^TKy$,
$T_3=y^3-6yH+4V$, and

$$
N=Fyy^T-2FH-2\{y(Hp)^T+(Hp)y^T\}+4HKH+4V_p.
\tag{1.1}
$$

Criticality includes the complete identities

$$
u(t)^TKNKu(t)=0,\qquad
P(t)^3-6P(t)\mathcal H(t)+4V(Ku(t),Ku(t),Ku(t))=0.
\tag{1.2}
$$

Continue the already proved reduced-H, degenerate-Gram, $Hp=0$, essential-six primitive-phase classification. Under its legitimate weighted normalization,

$$
F=1,\quad H=\tfrac12(z_1^2+z_2^2+z_3^2),\quad
V=\tfrac12(U^3+W^3),
$$
$$
B_H=\begin{pmatrix}0&g&h\\g&0&0\\h&0&0\end{pmatrix},\quad
gh\ne0,\quad g^2+h^2=-1,
$$
$$
e=UKW,\quad p(U)=p(W)=e,\quad 2e^3=-1,
$$
$$
(z_iKU)=(C_1,gr,-hr),\quad
(z_iKW)=(-\omega^2C_1,-\omega gr,\omega hr),
$$
$$
\omega^2+\omega+1=0,\quad
\delta=2g^2+1,\quad\delta^2=-e^2,\quad
2\delta C_1r=1,\quad C_1^2=\omega/(2e).
\tag{1.3}
$$

All these scale denominators are nonzero. The six vectors $y,z_1,z_2,z_3,U,W$ form a basis, and all five physical support points are distinct.

The aligned phase and every H source at infinity have already been excluded, as have original central H sources 0 and 2. Let $c\ne0,2$ be an arbitrary remaining finite central H source. In particular $c=-6$ remains in the present chart.

Make the exact basis change
$$
S(c)u(t)=t^5u(c+1/t),\qquad K_c=S(c)^TKS(c).
$$
This is a translation followed by reversal in the fifth symmetric power, hence invertible for every $c$. Both tensors and the bilinear form are transformed; invariance of the old $K$ is not assumed. The original center $c$ becomes infinity, and an original source at infinity becomes 0.

In the new coordinates write

$$
z_1=\lambda_1u(\infty),\quad
z_2=\lambda_2u(a),\quad z_3=\lambda_3u(b),\quad
U=\rho u(\alpha),\quad W=\sigma u(\beta).
\tag{1.4}
$$

All four displayed source parameters are finite and pairwise distinct. The source code calls $\alpha,\beta$ simply $u,v$; they are points, not the vectors $U,W$.

## 2. Entire changed kernel and genuine derivatives

Put

$$
a_3=-c^2(c-2)(c+6),\quad
a_{21}=-2c(c^2+3c-6),\quad
a_{20}=-6c^2-12c+32,
$$
$$
Q(X,Z)=a_3Z^3+(a_{21}X+a_{20})Z^2
+(-5X^2-6(c+1)X-5)Z+(c+1)X^3+X^2.
$$

The exact original kernel in the new basis is

$$
k(s,t)=-(s-t)^2Q(s+t,st).
\tag{2.1}
$$

Write $k_1(s,t)=\partial_sk(s,t)$, with the other source held fixed:

$$
k_1(s,t)=-2(s-t)Q(s+t,st)
-(s-t)^2\{Q_X(s+t,st)+tQ_Z(s+t,st)\}.
\tag{2.2}
$$

The central and adjacent central polars are

$$
L(s)=[t^5]k(s,t)=-a_3s^3-a_{21}s^2+5s-c-1,
$$
$$
M(s)=[t^4]k(s,t)=2a_3s^4+a_{21}s^3-a_{20}s^2+5(c+1)s-1.
\tag{2.3}
$$

The program checks (2.1) against the full original matrix after the basis change, both coefficient formulas (2.3), and the complete derivative (2.2). In particular the term
$-2(s-t)Q(s+t,st)$ in a V cross derivative is retained: $k(\alpha,\beta)\ne0$, so that term cannot be discarded.

Use the shorthand

$$
L_A=L(a),\ L_B=L(b),\ L_U=L(\alpha),\ L_V=L(\beta),
\quad E_V=L_UL_V,\quad k=k(\alpha,\beta),
$$
$$
f=k(a,\alpha),\qquad g_*=k(a,\beta).
\tag{2.4}
$$

The symbol $g_*$ is a kernel value and is different from the H Gram entry $g$ in (1.3).

## 3. Five small original source equations

The zero H edge gives

$$
\boxed{Q(a+b,ab)=0.}
\tag{3.1}
$$

The two endpoint-polar sums are

$$
\boxed{
S_U=L_Bf+L_Ak(b,\alpha)=0,\qquad
S_V=L_Bg_*+L_Ak(b,\beta)=0.
}
\tag{3.2}
$$

The original primitive ratio is exactly

$$
\boxed{R_\omega=L_Ug_*-\omega^2L_Vf=0.}
\tag{3.3}
$$

The signed H Gram value gives the last equation

$$
\boxed{R_\delta=\delta L_Ak+\omega L_Vf=0.}
\tag{3.4}
$$

Here is a derivation preserving all normalizations. At the two V points,

$$
\frac{k(a,\alpha)}{L_AL_U}=T_0,\quad
\frac{k(a,\beta)}{L_AL_V}=\omega^2T_0,\quad
\frac{k(b,\alpha)}{L_BL_U}=-T_0,\quad
\frac{k(b,\beta)}{L_BL_V}=-\omega^2T_0,
$$
$$
T_0=\lambda_1^2r/C_1
=-\frac{\omega^2k}{2e\delta E_V}.
\tag{3.5}
$$

Define the full physical polynomial

$$
V_*(s)=L_Vk(s,\alpha)+L_Uk(s,\beta).
\tag{3.6}
$$

The primitive sum and the original V norm imply

$$
V_*(a)=\delta L_Ak,\qquad V_*(b)=-\delta L_Bk.
\tag{3.7}
$$

For example, if $S=F_a(\alpha)+F_a(\beta)=-\omega T_0$, then the primitive ratio gives $S^2=F_a(\alpha)F_a(\beta)$. The original norm is
$2eE_V^2F_a(\alpha)F_a(\beta)=k^2$.
Together with (3.5) this yields $\delta=E_VS/k=V_*(a)/(L_Ak)$.
Also (3.3) gives $V_*(a)=(1+\omega^2)L_Vf=-\omega L_Vf$, proving (3.4).

For use in exact lowering, set

$$
r_A=V_*(a)-\delta L_Ak,\quad
r_B=V_*(b)+\delta L_Bk.
$$

The full polynomial identities are

$$
r_A=R_\omega-R_\delta+(\omega^2+\omega+1)L_Vf,
$$
$$
L_Ar_B=L_VS_U+L_US_V-L_Br_A.
\tag{3.8}
$$

The source remultiplies both identities.

The original norm also follows directly from these small equations:

$$
N_A:=2eE_Vfg_*-k^2L_A^2=0.
\tag{3.9}
$$

Indeed the exact identity

$$
N_A=2eL_VfR_\omega
+2e(\omega L_Vf-\delta L_Ak)R_\delta
+(2e\delta^2-1)L_A^2k^2
$$

has zero last coefficient because $\delta^2=-e^2$ and $2e^3=-1$.
Thus the original norm has not been lost by replacing expanded traces.

## 4. The three original N first derivatives in labelled form

Since $F=1,Hp=0$, the full expression (1.1) is
$N=yy^T-2H+4HKH+4V_p$.
Let $\lambda=\lambda_1^2$. The legitimate representative scales give

$$
\lambda=-\frac{k}{2e^2E_V},\quad
\lambda_2^2=\frac{\delta-1}{2\lambda L_A^2},\quad
\lambda_3^2=\frac{-\delta-1}{2\lambda L_B^2}.
\tag{4.1}
$$

Differentiate the full polynomial $V_*(s)$ before using any source equation:

$$
V_*'(a)=L_Vk_1(a,\alpha)+L_Uk_1(a,\beta),
\quad
V_*'(b)=L_Vk_1(b,\alpha)+L_Uk_1(b,\beta).
\tag{4.2}
$$

The original finite-H N derivatives reduce to

$$
\boxed{
G_A=-kL_BL'(a)+e^2(\delta+1)E_Vk_1(a,b)
+2e\delta L_BV_*'(a)=0,
}
$$
$$
\boxed{
G_B=-kL_AL'(b)+e^2(1-\delta)E_Vk_1(b,a)
-2e\delta L_AV_*'(b)=0.
}
\tag{4.3}
$$

For a direct comparison with the prior full first-derivative formulas, define

$$
\widetilde G_A=-k^2L_BL_AL'(a)
+e^2E_V\{V_*(a)+kL_A\}k_1(a,b)
+2eL_BV_*(a)V_*'(a),
$$
and the analogous $\widetilde G_B$.
Then the exact identities are

$$
\widetilde G_A-L_AkG_A
=r_A\{e^2E_Vk_1(a,b)+2eL_BV_*'(a)\},
$$
$$
\widetilde G_B-L_BkG_B
=r_B\{e^2E_Vk_1(b,a)+2eL_AV_*'(b)\}.
\tag{4.4}
$$

All multipliers divided in passing to (4.3) are original units. The frozen program verifies both identities before invoking Singular.

For clarity, the complete V contribution in this calculation is
$4(V_p)_{\rm pol}=2e\{(\rho k(\alpha,t))^2+
(\sigma k(\beta,t))^2\}$.
At an H endpoint it contributes
$-2V_*V_*'/(\lambda E_V^2)$; it is not omitted.

At the central source infinity, $P(t)$ has degree at most four by $Hp=0$. The polar of $HKH$ has degree at most eight, since $\deg L\le3$ and only the two central H edges are nonzero. The full coefficient of $t^9$ in $N$ is therefore the labelled equation

$$
\delta\!\left(\frac{M(a)}{L_A}-\frac{M(b)}{L_B}\right)
-\left(\frac{M(a)}{L_A}+\frac{M(b)}{L_B}\right)
-2\left(\omega\frac{M(\alpha)}{L_U}
+\omega^2\frac{M(\beta)}{L_V}\right)=0.
$$

After clearing exactly the displayed original units, this is

$$
\boxed{
D=(\delta-1)M(a)L_BE_V-(\delta+1)M(b)L_AE_V
-2\omega M(\alpha)L_AL_BL_V
-2\omega^2M(\beta)L_AL_BL_U=0.
}
\tag{4.5}
$$

Equations (4.3) and (4.5) are the same original N first derivatives, with no expanded quadratic traces.

## 5. Original highest first derivatives at the V points

Let

$$
\mathcal C(t)=P(t)^3-6P(t)\mathcal H(t)
+2\{(\rho k(\alpha,t))^3+(\sigma k(\beta,t))^3\}.
$$

At $t=\alpha$, the original V mean equation gives

$$
P(\alpha)=e/\rho,\qquad
\mathcal H(\alpha)=e^2/(2\rho^2)=P(\alpha)^2/2.
$$

Thus the coefficient of $P'(\alpha)$ in $\mathcal C'(\alpha)$ is exactly zero. The diagonal kernel contributes zero, and the full remaining cross term gives

$$
-6P(\alpha)\mathcal H'(\alpha)
+6\sigma^3k^2 k_1(\alpha,\beta)=0.
$$

Since $\rho\sigma k=e$, the correct original identity is

$$
\boxed{
\mathcal H'(\alpha)=\sigma^2\,k\,k_1(\alpha,\beta),\qquad
\mathcal H'(\beta)=\rho^2\,k\,k_1(\beta,\alpha).
}
\tag{5.1}
$$

The extra factor $k$ is essential. It comes from
$\rho\sigma^3k^2/e=\sigma^2k$, and is retained throughout.

Using (4.1), (3.5), and
$\sigma^2=\omega^2/(2e\lambda L_V^2)$, the first equation in (5.1), multiplied by $2e\lambda L_V^2$, is

$$
-\frac{k^2L'(\alpha)}{L_U}
+eL_UL_V^2\frac{f}{L_AL_U}
\left\{(\delta-1)\frac{k_1(\alpha,a)}{L_A}
+(\delta+1)\frac{k_1(\alpha,b)}{L_B}\right\}
-\omega^2k\,k_1(\alpha,\beta)=0.
\tag{5.2}
$$

Here the first term uses
$\lambda^2=-k^2/(2eE_V^2)$, a direct consequence of (4.1) and $2e^3=-1$. Every multiplier is nonzero.

The exact lower polynomial equation is

$$
\boxed{
H_U=2\delta L_AL_Bk_1(\alpha,\beta)
+L_V\{(\delta-1)L_Bk_1(\alpha,a)
+(\delta+1)L_Ak_1(\alpha,b)\}
-2L_Bg_*L'(\alpha)=0.
}
\tag{5.3}
$$

Similarly,

$$
\boxed{
H_V=2\delta L_AL_Bk_1(\beta,\alpha)
+L_U\{(\delta-1)L_Bk_1(\beta,a)
+(\delta+1)L_Ak_1(\beta,b)\}
-2L_BfL'(\beta)=0.
}
\tag{5.4}
$$

There is no additional cross $k$ multiplying the last two terms of (5.3)--(5.4); the factor in (5.1) has already been incorporated in the lowering.

For an entirely checkable derivation, multiply (5.2) by $L_A^2L_BL_U$ and define

$$
\begin{aligned}
\mathrm{Direct}_U={}&-k^2L_A^2L_BL'(\alpha)\\
&+eL_UL_V^2f\{(\delta-1)L_Bk_1(\alpha,a)
+(\delta+1)L_Ak_1(\alpha,b)\}\\
&-\omega^2kL_A^2L_BL_Uk_1(\alpha,\beta).
\end{aligned}
$$

The complete polynomial identity is

$$
\begin{aligned}
\mathrm{Direct}_U-eE_VfH_U
={}&N_A L_BL'(\alpha)\\
&-L_AL_BL_U
\{\omega^2kL_A+2e\delta L_Vf\}k_1(\alpha,\beta).
\end{aligned}
\tag{5.5}
$$

The bracket is zero on the exact original source equations: multiply it by $\omega$ to obtain

$$
2e\delta R_\delta+(\omega^3-2e\delta^2)L_Ak=0.
$$

Here $\omega^3=1=2e\delta^2$. Together with $N_A=0$, equation (5.5) gives (5.3), since $eE_Vf\ne0$.

The V-swapped direct expression has the full cross term
$-\omega kL_A^2L_BL_Vk_1(\beta,\alpha)$, and obeys

$$
\begin{aligned}
\mathrm{Direct}_V-eE_Vg_*H_V
={}&N_A L_BL'(\beta)\\
&-L_AL_BL_V
\{\omega kL_A+2e\delta L_Ug_*\}k_1(\beta,\alpha).
\end{aligned}
\tag{5.6}
$$

Its bracket follows from the preceding bracket and $R_\omega=0$.
The source explicitly checks the two full identities (5.5)--(5.6), including the required original cross $k$. Thus (5.3)--(5.4) are exactly the original highest first derivatives on the paid chart, not a replacement condition.

## 6. Entire physical localization

Use just

$$
\boxed{
\Pi=c(c-2)(a-b)L_AL_BL_UL_Vk\ne0.
}
\tag{6.1}
$$

The first two center factors remove only the two already excluded finite center charts. The remaining factors are the distinct H endpoints, the four original nonzero central pairings, and the original nonzero V pairing. They are all physically forced.

The cross kernel values are nonzero as well: (3.4) forces $f\ne0$; (3.3) then forces $g_*\ne0$; (3.2) forces the two other endpoint/V pairings nonzero. Thus all divisions in §5 are paid by the same source equations and (6.1).

There is no factor $c+6$, $a_3$, an unselected-root discriminant, or a source parameter in $\Pi$. Original source infinity remains represented by a finite zero parameter after the coordinate change and is retained.

Adjoin one inverse $n$ with $n\Pi-1=0$. The ten original equations
(3.1)--(3.4), (4.3), (4.5), (5.3)--(5.4), together with this inverse equation, form the precise new necessary ideal. There is no assertion that these few derivatives imply the complete original critical system.

## 7. One exact coefficient field for every Gram choice

The constants in (1.3) satisfy

$$
e^3=-\tfrac12,\qquad \omega^2+\omega+1=0,\qquad \delta^2=-e^2.
$$

Let $i=\delta/e$, so $i^2=-1$, and set $\eta=\omega/i$.
Then

$$
\eta^3=i,\qquad \eta^4=\omega,\qquad
\eta^4-\eta^2+1=0,\qquad \delta=\eta^3e.
$$

Thus every original choice belongs to the compositum
$\mathbb Q(e,\eta)=\mathbb Q(e,\zeta_{12})$.
The pure cubic field has degree three and the cyclotomic field has degree four; these degrees are coprime, so this compositum has degree 12. Its embeddings retain all three choices of $e$, both primitive choices of $\omega$, and both signs of $\delta/e$.

The implementation uses $\theta=e+\eta$. It constructs

$$
f(\theta)=\operatorname{Res}_E
(2E^3+1,(\theta-E)^4-(\theta-E)^2+1),
\tag{7.1}
$$

normalizes it to monic form, and requires an actual exact QQ factorization showing one irreducible degree-twelve factor. It remultiplies that factorization.

In $\mathbb Q[\theta]/(f)$, a small polynomial Euclidean algorithm computes the common linear factor of $E^3+1/2$ and
$(\theta-E)^4-(\theta-E)^2+1$, recovering $e$. Every coefficient inverse is obtained by a QQ extended gcd and checked by both the full Bézout product and the product modulo $f$. It then sets $\eta=\theta-e$, $\omega=\eta^4$, $i=\eta^3$, $\delta=ie$, and checks every displayed relation exactly.

Consequently the actual Singular input has only the five physical source variables and one inverse variable. The constants $e,\omega,\delta$ are declared as exact numbers in the same irreducible field. They are not extra physical polynomial variables. An actually verified unit identity in that field remains an identity after every complex embedding, so no original Gram choice is omitted.

## 8. Frozen source and success criterion

The current corrected self-contained source is Git blob

253173d7855a518466d78c4f96c6d5826067dab7.

It performs the constant-field checks, the entire original kernel and coefficient checks, the true source derivatives, the two source identities (3.8), the original N lowering identities (4.4), and both complete highest lowering identities (5.5)--(5.6). It then builds the eleven generators above, removing only nonzero integer scalar contents with an exact product check.

The new Singular gate is over the exact field from (7.1), with a 900-second child limit and 4 GiB address-space bound. It verifies the field relations and a small exact lift before requesting a transformation vector $C$. A unit conclusion requires the actual multiplication

$$
\operatorname{matrix}(I)\,C=[1]
$$

with correct matrix dimensions, all verification markers as independent output lines, and no Singular error line. A timeout or memory exit remains unresolved.

The earlier N-first source 0c016a3cbd42a0aafc3858c9953e5293742bdf17 actually exceeded 4 GiB in run45827161540/job139934167647; its unresolved receipt is blob8bf5d473fd163191de70cf7acb8870f538576973. The present labelled equations and added original highest derivatives are a different, lower-degree input. No successful computation is rerun and no failed input is relabelled as a proof.

Until the present unit gate actually succeeds, this document proves only the exact original necessary reduction and its complete coverage of the remaining finite-center chart. The ordinary invariant-subspace problem and the broader R150 Bell problem remain unfinished.


The frozen source is [the labelled original source](../notes/2026-11-26-reduced-H3-labelled-original-L12-highest-N-first-347c.py), launched from f3eb4bac533921bfcaa11becb44d7e9e68cccc3e in Actions run 45831444045, job 139948952361. This is an execution identity, not a success receipt.


### Actual bounded execution

The source actually completed the exact degree-twelve field construction, all original kernel/N/highest identities and the lift smoke test. Singular then reached its 900-second limit without a unit certificate: source 901.257929 seconds, driver 901.618147165 seconds, peak child RSS 2256952 KiB, source exit1. The generated input was 1,212,580 bytes (SHA-256 fe8dc44bb28cbcf24282e053efd9f29467f424895790d8240c82d5406b7e7abf). Only field/smoke/begin-lift markers were returned; no I*C=1 marker occurred. The [actual small receipt](../notes/2026-11-26-reduced-H3-labelled-L12-unresolved-execution-347c.json) preserves the original pull/rule check and hashes. The necessary reduction remains proved; this computational gate remains unresolved and is not rerun.
