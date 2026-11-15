# R150: a new original maximal minor of degree 8769 with unit leading coefficient

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-15.  
Status: exact theorem using the completed full spectrum and original coordinate dictionaries. The dictionary arithmetic is reproducible by the accompanying small program; no new large determinant has been evaluated.

## 1. A different, explicitly specified original minor

Let $A(s)$ be the original $4367\times6188$ polynomial matrix and let $A_\infty(u)$ be its natural weighted infinity chart. Retain the actual $4340$ original constant-unit source coordinates $P$ from the full infinity computation.

Define the following fourteen additional **original source indices**, using the repository's one-based convention:

$$
J_{14}=
(5520,5521,5522,5523,5524,5525,5537,5538,5539,5540,
6154,6168,6171,6184),
$$

and put $J_*=P\cup J_{14}$. Define the omitted **original output indices**, using the zero-based convention, by

$$
F_{13}=
(3001,3002,4002,4003,4288,4289,4353,4354,4355,
4363,4364,4365,4366),
$$

and let $I_*=\{0,\ldots,4366\}\setminus F_{13}$.

The new original square matrix is

$$
B_*(s)=A(s)[I_*,J_*],\qquad D_*(s)=\det B_*(s).
$$

Then

$$
\boxed{
H_*=8835,\qquad
\operatorname{ord}_u\det B_*^\infty(u)=66,\qquad
\deg D_*=8769,\qquad
\operatorname{lc}(D_*)\in\mathbb Z_{(31)}^\times.
}
\tag{1}
$$

The sets $I_*,J_*$ are not the former sets $I,J$ used for the order-$243$ minor. Nothing in this theorem changes the recorded identities, bounds or open leading-coefficient question for that former minor.

## 2. Original source complement and its unit projection

Write $\mathcal R=\mathbb Z_{(31)}[[u]]$. The [integral full Smith and canonical source theorem](R150-appendix-full-infinity-integral-smith-and-canonical202-source-kernel.md) proves

$$
\ker_{\mathcal R} A_\infty
=\Phi\mathcal R^{1632}\oplus K_H\mathcal R^{202}.
\tag{2}
$$

All coordinates in (2) are the original coordinates. In particular, with $H=P^c$, the paid actual tail decomposition is

$$
[\Phi_H,E_{216}]\in\operatorname{GL}_{1848}(\mathcal R).
$$

Let $R_\Phi=H\setminus E_{216}$ be the actual $1632$ selected tail coordinates, and let $F_H\subset E_{216}$ be the canonical $202$ source free coordinates. The source theorem proves

$$
K_H=j(E_{216}N_H),\qquad
j(h)=(-U^{-1}Vh,h),\qquad N_H[F_H,:]=I_{202}.
$$

The graph correction in $j$ changes only the original $P$ coordinates. Its tail is exactly $E_{216}N_H$. Thus $K_H$ is zero on $R_\Phi$, rather than merely equivalent to zero after an unrecorded Koszul adjustment.

For the original complementary source set

$$
C_*=R_\Phi\ \dot\cup\ F_H
$$

the complete kernel frame has the block form

$$
[\Phi,K_H][C_*,:]
=
\begin{pmatrix}
\Phi_{R_\Phi}&0\\
\Phi_{F_H}&I_{202}
\end{pmatrix}.
\tag{3}
$$

The determinant of $\Phi_{R_\Phi}(0)$ is $15$ modulo $31$, so (3) is invertible over $\mathcal R$.

The remaining original source coordinates are precisely

$$
C_*^c=P\cup(E_{216}\setminus F_H)=J_*.
$$

It follows that

$$
\mathcal R^{6188}
=\ker A_\infty\oplus\mathcal R^{J_*},
\qquad
A_\infty(\mathcal R^{J_*})=\operatorname{im}A_\infty.
\tag{4}
$$

Indeed, subtracting the unique kernel vector with the same $C_*$ coordinates leaves a vector supported on $J_*$. A kernel vector supported on $J_*$ is zero by (3). This pays both generation and injectivity; the new column set is not just generically independent.

The canonical $F_H$ projection used here is justified by the full integral kernel base change and by the earlier complete formal field mapper: all fourteen positive directions actually exited in the same $E_{216}$ coordinates, and the generic rank fourteen makes the remaining formal block zero. No length-$26$ assertion is used to establish (3) or (4).

## 3. Original output complement

The [actual rational thirteen-kernel construction](R150-appendix-original-characteristic-zero-primitive-thirteen-kernels-and-projection-length2.md) supplies a complete original left kernel frame $\Lambda$ with

$$
\Lambda\in\operatorname{Mat}_{4367\times13}(\mathcal R),
\qquad
\Lambda[F_{13},:]=I_{13}.
$$

The complete coefficientwise $31$ regularity and the original free identity were verified there. Let

$$
Y=\ker\Lambda^{\mathsf T}\subset\mathcal R^{4367}.
$$

For any prescribed original $I_*$ coordinates $v_{I_*}$, there is exactly one vector of $Y$ with those coordinates:

$$
v_{F_{13}}=-\Lambda[I_*,:]^{\mathsf T}v_{I_*}.
$$

Thus the original coordinate projection gives

$$
Y\xrightarrow{\ \sim\ }\mathcal R^{I_*}.
\tag{5}
$$

The full integral Smith decomposition shows that $Y$ is the $u$-saturation of $\operatorname{im}A_\infty$, and that $Y/\operatorname{im}A_\infty$ is exactly the torsion summand of the full cokernel. Combining (4) and (5) gives

$$
\operatorname{coker}_{\mathcal R} B_*^\infty
\cong
\bigoplus_{a\in(1,1,1,1,3,4,4,4,5,6,7,8,10,11)}
\mathcal R/(u^a).
\tag{6}
$$

Its zeroth Fitting ideal is $(u^{66})$, while that of the square presentation $B_*^\infty$ is generated by its determinant. Hence

$$
\det B_*^\infty=u^{66}\varepsilon(u),
\qquad
\varepsilon(u)\in\mathcal R^\times.
\tag{7}
$$

This proves the exact order and the $31$-unit coefficient, without computing the enormous determinant polynomial.

## 4. Actual original weights

For a source $m^\alpha N_i$ or $m^\alpha\Gamma_i$, retain the original weights

$$
a_{m^\alpha N_i}=20+10|\alpha|,
\qquad
a_{m^\alpha\Gamma_i}=25+10|\alpha|.
$$

An output monomial $m^\beta$ has weight $b_\beta=10|\beta|$. The source cost is $\deg x_\ell+a_\ell-10$.

The actual original $4340$-column dictionary has the following counts:

| Equation family | Multiplier degree | Count |
|---|---:|---:|
| $N$ | 0 | 11 |
| $\Gamma$ | 0 | 6 |
| $N$ | 1 | 121 |
| $\Gamma$ | 1 | 66 |
| $N$ | 2 | 671 |
| $\Gamma$ | 2 | 315 |
| $N$ | 3 | 2530 |
| $\Gamma$ | 3 | 620 |

Its weight sum is $207925$. All fourteen additional original columns are cubic $\Gamma$ source coordinates, of weight $55$, so

$$
\sum_{\ell\in J_*}a_\ell=207925+14\cdot55=208695.
$$

The total weight of all $4367$ original outputs is $200200$. The thirteen omitted actual outputs have weight sum $340$, giving

$$
\sum_{i\in I_*}b_i=199860,\qquad
H_*=208695-199860=8835.
\tag{8}
$$

The weight arithmetic was decoded from the actual original dictionaries in V8, without a new matrix elimination. The accompanying Python program independently reconstructs the same dictionaries, checks their full paid hashes, enumerates all original monomials, and reproduces (8). It does not turn any transformed source column into an original column.

The natural weighted relation is

$$
B_*^\infty(u)
=\operatorname{diag}(u^{-b_i})\,B_*(1/u)\,
\operatorname{diag}(u^{a_\ell}).
$$

Therefore

$$
u^{8835}D_*(1/u)=u^{66}\varepsilon(u),
$$

which proves $\deg D_*=8835-66=8769$ and identifies its leading coefficient with the $31$-unit $\varepsilon(0)$. This completes (1).

## 5. Cofactors and original column replacements

Equation (6) gives the submaximal Fitting ideal $(u^{55})$. In particular, every $4353$-cofactor of the new natural matrix has order at least $55$.

There is a stronger bound for replacement by an original source column. Equation (4) gives, for every original column, a unique regular source vector $z_\ell\in\mathcal R^{J_*}$ with

$$
(A_\infty)_\ell=(A_\infty)_{J_*}z_\ell.
$$

Cramer's identity therefore shows that every new natural original-column replacement determinant belongs to $u^{66}\mathcal R$. Its natural order is at least $66$, including the zero determinant case. Thus

$$
\deg\bigl(\operatorname{adj}(B_*)A_{\ell,I_*}\bigr)_j
\le 8835-a_j+a_\ell-66.
\tag{9}
$$

The corresponding cofactor degree bound is

$$
\deg(\operatorname{adj}B_*)_{ji}
\le8835-a_j+b_i-55.
\tag{10}
$$

The orders $66$ and $55$ apply to this new minor for distinct reasons. They are not substituted into the former order-$243$ minor.

## 6. Reproducible dictionaries and scope

The sorted original new column list has SHA256

`5d9d416096e2c6d0a8cf10a7a95ad83453d0a8c8e98758b3d7ab19f93720124e`.

The paid $4340$ source list has SHA256

`94c940a7b5ff4768e7e1b0820033eca3cabf19bb8958c7cab52c1e1eefb09837`.

The actual $216$ and $202$ source dictionaries respectively have SHA256

`89adaa79918eeb4e9c114f0009f995b6eb72161fba54078f583a47acbffa0fea`,

`57bc2f0bdbf50d82920d286bd9ab2fdb0e03fd5a68a3d72bf534a297ab4da683`.

The [small original-dictionary verifier](../notes/2026-11-15-r150-new-original-unit-leading-minor-dictionaries-789f.py) is blob `67f18ecd6c1a26373fb55c19ea18edff5a788e64`, $10513$ bytes, SHA256

`653808b60f2c4a2d307e1546642892a3d4881d10033b00624e0296e452834dc7`.

Its input contract pins the historical native model and original full constant receipt, the actual complete field source mapper, the actual primitive rational thirteen-kernel receipt, and the actual complete rational spectrum receipt. Its output records only exact original dictionary checks, weight sums and small hashes.

The new determinant and all source relations used here are original-column objects. No full characteristic-zero $202$-mapper array, no old outside determinant of length $149$, and no old higher quotient of length $26$ is evaluated or inferred. The new local source complement avoids those old-coordinate torsion factors; it does not decide their characteristic-zero lengths.

The uniform finite-precision source reduction for this new minor is proved separately in [the bound 8655 corollary](R150-appendix-uniform-source-bound8655-over-all-powers-of31.md). It has a different purpose from the already proved rational cost 8531; no improvement of that earlier rational bound is asserted here.

## 7. Actual complete dictionary verification

The small reader was actually executed in run `43756208221`, step `new-original-unit-leading-minor-dictionaries`, from execution commit `d8a5f6d3232e1a580a0e309c8f443120b4c54d76`. Its mathematical time was $0.4074878119999994$ seconds and wall time $0.46469509700000344$ seconds; exit code was zero.

The [actual published receipt](../notes/r150-source-kernel-session-789f/43756208221-new-original-unit-leading-minor-dictionaries.json) is blob `0f543b9b02141fcdbca547b91045e4e5dd92e597`, $9056$ bytes, SHA256 `b178415228fa060f529d1aa335a3a7d01078adb4b824042eb7da79d73b66443e`. The full temporary receipt was $6038$ bytes with SHA256 `e09e6aaeef8de337548e447ccf0c4b348dcf24347dffc6daa43cd2ea9cf8abb4`. Its semantic binding is `28c53c39e757924c28a2c0b669641249a80e322cc8c9e4548960fc4dca9cc714`.

All five complete input byte identities, all $3333$ original prebasis records, all $1007$ subsequent constant-pivot coordinates, and the complete original $P,R,H,E_{216},F_H$ dictionaries passed. The actual histograms reproduce every count in section 4. The new row-set hash is `c9c64296a63ec83c67c97fbcbdc150152b6fbd823ab2ecd9de515797ed6fb141`, and the new complementary source hash is `36d196a8ad72f10bd50c84d6a1e6cedd8baf42798173774a7413f9d56e33c15e`.

The two historical text inputs were first restored to temporary storage and checked at full length in the [successful recovery-v2 receipt](../notes/r150-source-kernel-session-789f/43756208221-new-original-minor-historical-dictionary-recovery-v2.json). The initial recovery attempt invoked git from the temporary computation directory and failed before reading either input; the corrected attempt explicitly uses the repository checkout. No historical mathematical array was assumed to exist or newly persisted.

This execution verifies original dictionaries and integer weight arithmetic. The determinant valuation and leading-unit conclusion still come from sections 2--3; `leadingCoefficientComputedNumerically=false` and `newMatrixEliminationPerformed=false` remain accurate.
