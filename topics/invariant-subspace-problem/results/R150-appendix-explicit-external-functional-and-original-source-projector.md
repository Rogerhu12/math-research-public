# R150 appendix: an explicit external quotient functional and a complete original-source projector without inverting the external divisor

Author: Astra-ISP-789f / normal_annihilator. AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-15 UTC.

Status: an exact algebraic consequence of the completed original 56-row Bockstein certificate. The quotient functional is specified by its already verified polynomial vector. The new Bezout/adjugate projector and the full normal tails have not been numerically assembled in this appendix.

## 1. The same original core and localization

Set
$$
S=\mathbb Q[s,\Sigma_0^{-1}],\qquad
\Sigma_0=s(s-2)(s+6)F_+F_-E_8.
$$
Let $G\in\mathbb Q[s]^{56\times22}$ be the complete original core after the paid known-factor divisions. In the determinant and Bockstein calculations, each row was further multiplied by a recorded nonzero rational constant. Write
$$
M=C\,G,\qquad C=\operatorname{diag}(c_1,\ldots,c_{56}),
\qquad c_i\in\mathbb Q^\times.
\tag{1.1}
$$
The exact constants have SHA256
~~~text
c72e60a80f9fa4aac9e78fd9a79441e88da5e9d107acd616cddcf9bb884da2df
~~~
and all 1232 original polynomial identities in (1.1) were checked. The matrix $C$ is a source unit; it is not a row operation on an unrelated target matrix.

The [complete outside-divisor computation](R150-appendix-exact-original-external-divisor120-multiplier21-and-source-cost8411.md) proves
$$
\Omega=f^2,\qquad \deg f=60,\qquad
f\text{ monic and squarefree},\qquad \gcd(f,\Sigma_0)=1.
\tag{1.2}
$$
At every irreducible factor of $f$, $M$ has residue rank 21 and exactly one positive Smith exponent, equal to two. All maximal minors have no other common factors outside $\Sigma_0$.

All claims about the entire projected cokernel below are over $S$. The unlocalized polynomial matrix may retain torsion on $\Sigma_0$; no contrary assertion is needed.

## 2. The actual polynomial functional

The completed single-kernel calculation retains the exact vectors $x,y$ and
$$
z=x-fy\in\mathbb Q[s]^{22}.
$$
For the actual original free coordinate $j$ selected by its paid unit profile, it verifies
$$
z_j=1,\qquad
Mz=f^2q
\tag{2.1}
$$
for a saved exact $q\in\mathbb Q[s]^{56}$. This uses every original row, not only the 21 unit rows.

Define
$$
\ell:S^{22}\longrightarrow S/(f^2),\qquad
\ell(v)=z^Tv\bmod f^2.
\tag{2.2}
$$
Because $z_j=1$, this is surjective. Equation (2.1) shows that $\operatorname{im}M^T\subset\ker\ell$, so it induces
$$
\overline\ell:\operatorname{coker}_S M^T\longrightarrow S/(f^2).
$$
The source-side projected cokernel is a torsion $S$-module of $\mathbb Q$-vector-space dimension $\deg\Omega=120$. Since $f$ is coprime to $\Sigma_0$, the target $S/(f^2)$ also has $\mathbb Q$-vector-space dimension 120. Thus the surjective $S$-linear map $\overline\ell$ is a surjective map between two finite-dimensional $\mathbb Q$-vector spaces of equal dimension, hence is an isomorphism. Here 120 is the $\mathbb Q$-dimension, not the composition length as an $S$-module. Therefore
$$
\boxed{
\operatorname{coker}_S M^T\xrightarrow[\;\overline\ell\;]{\ \simeq\ }S/(f^2),
\qquad
\operatorname{im}M^T=\ker\ell.
}
\tag{2.3}
$$

This is an explicit actual quotient functional, not merely the abstract existence of a cyclic invariant factor. Since $f$ is coprime to $\Sigma_0$, its codomain can also be identified with $\mathbb Q[s]/(f^2)$. That identification does not remove the localization on the source cokernel.

The original thirteen free projection coordinates remain separate. Transporting (2.2) through the paid target changes gives the external torsion coordinate of the full original 155-dimensional projection. That final 155-coordinate expression is not newly expanded or reverified here.

## 3. A polynomial basis for the image lattice

Order the 21 indices different from $j$, followed by the index $j$. Define a 22 by 22 polynomial matrix $E$ by its columns:
$$
E_i=e_i-z_i e_j\quad(i\ne j),\qquad
E_{\mathrm{last}}=f^2e_j.
\tag{3.1}
$$
Then
$$
\det E=\varepsilon f^2,\qquad \varepsilon\in\{1,-1\}.
$$
In particular, $E$ is injective over $S$.

Its image is exactly $\ker\ell$. Indeed, for any $v\in\ker\ell$,
$$
v=\sum_{i\ne j}v_i(e_i-z_ie_j)
+\frac{z^Tv}{f^2}\,f^2e_j.
\tag{3.2}
$$
The last coefficient belongs to $S$ precisely because $v\in\ker\ell$. Conversely every column of $E$ is annihilated by $\ell$. Thus
$$
\operatorname{im}E=\ker\ell=\operatorname{im}M^T.
$$

There is a uniquely determined polynomial matrix
$$
V\in\mathbb Q[s]^{22\times56}
$$
such that
$$
\boxed{M^T=EV.}
\tag{3.3}
$$
Its entries are explicit:
$$
V_{i,a}=M_{a,i}\quad(i\ne j),\qquad
V_{\mathrm{last},a}=q_a=\frac{(Mz)_a}{f^2}.
\tag{3.4}
$$
The last row is already stored in the completed original-row certificate; its divisibility is an actual exact product check.

Although $f^2$ appears in the written quotient in (3.4), this is exact polynomial division, not inversion of $f$ in the coefficient ring. In particular, $V$ lies in $\mathbb Q[s]$, hence in $S$, before any new localization.

Because $E$ is injective and its image equals the image of $M^T$, (3.3) implies
$$
V:S^{56}\longrightarrow S^{22}\quad\text{is surjective},
\qquad
\ker V=\ker M^T.
\tag{3.5}
$$

## 4. A right inverse from the three paid original-source embeddings

Let
$$
\iota_\nu:S^{22}\longrightarrow S^{56}\qquad(\nu=1,2,3)
$$
be the actual source embeddings recorded by the three determinant certificates. The first two are selected original rows, and the third is the recorded constant integer row combination. The entire matrices of these combinations, including all ordering conventions, are part of the completed source records.

Put
$$
D_\nu=M^T\iota_\nu,\qquad
B_\nu=V\iota_\nu.
$$
Equation (3.3) gives
$$
D_\nu=E B_\nu,\qquad
d_\nu:=\det B_\nu=\varepsilon\,\frac{\det D_\nu}{f^2}
\in\mathbb Q[s].
\tag{4.1}
$$
Each determinant on the right is a genuine paid original maximal minor or constant-row-combination minor, with its exact sign and rational constant normalization retained.

The exact outside gcd of the three $\det D_\nu$ was already proved to be $f^2$. Consequently the three polynomials $d_\nu$ have gcd supported entirely on $\Sigma_0$. They therefore generate the unit ideal in $S$. An exact polynomial extended-gcd calculation, followed only by division by a known $\Sigma_0$-unit, gives
$$
b_1d_1+b_2d_2+b_3d_3=1,\qquad b_\nu\in S.
\tag{4.2}
$$
Define
$$
R=\sum_{\nu=1}^3 b_\nu\,\iota_\nu\,\operatorname{adj}(B_\nu)
\in S^{56\times22}.
\tag{4.3}
$$
Then
$$
VR=\sum_\nu b_\nu B_\nu\operatorname{adj}(B_\nu)
=\sum_\nu b_\nu d_\nu I_{22}=I_{22}.
\tag{4.4}
$$

This construction uses no inverse of $f$ or $\Omega$. Its only parameter denominators are units of the already declared localization $S$. The original source embeddings are essential: replacing $\iota_\nu$ by an arbitrary matrix of the same size would lose the claimed original-source interpretation.

The new matrices $B_\nu$, their adjugates, the Bezout coefficients and $R$ have not been numerically assembled in this appendix. Equations (4.1)–(4.4) are a constructive algebraic formula specifying them from the paid inputs.

## 5. A complete projector onto the original 56-source relation module

Set
$$
P=I_{56}-RV.
\tag{5.1}
$$
Then
$$
P^2=P,\qquad VP=0,\qquad M^TP=0.
$$
If $w\in\ker V$, then $Pw=w$. Hence
$$
\boxed{\operatorname{im}P=\ker V=\ker M^T.}
\tag{5.2}
$$
This is the complete rank-34 relation module of the 56 original core sources. The 56 columns of $P$ are a redundant generating family, so no new 34-column relation basis has to be selected.

In particular, the projector here is valid over $S$ itself. It improves the general right-inverse construction that would only be available after also inverting the projection divisor.

## 6. The full normal target presentation with the correct source scaling

The [exact original relative presentation](R150-appendix-exact-original-source-presentation-of-relative-normal-target-module.md) gives
$$
T=W/(L\cap W)
\simeq
\operatorname{coker}_W[B_0,\ H_G\ker G^T],
$$
where $B_0$ consists of all 6012 genuine zero-projection original sources, and $H_G$ contains the complete normal tails of the 56 retained core sources.

The normalization (1.1) changes the 56 original source columns by $C^T$. Their full normal tails must change by the same matrix:
$$
H_M=H_G C^T.
\tag{6.1}
$$
Since
$$
M^T=G^TC^T,
$$
transporting the complete kernel preserves its full source image:
$$
H_M\ker M^T=H_G\ker G^T.
$$
Combining this with (5.2) proves
$$
\boxed{
T\simeq\operatorname{coker}_W[B_0,\ H_M P]
\quad\text{over }S,
}
\tag{6.2}
$$
with no inversion of $\Omega$.

The 6012 original zero-projection columns remain present. All 56 columns of $H_MP$ have actual original source preimages given by the paid core transformations, the rational constant source scaling, and $P$. No column is discarded by counting alone.

The related source identities
$$
M^T R e_i=e_i-z_i e_j\quad(i\ne j),
\qquad
M^T R e_{\mathrm{last}}=f^2e_j
$$
are identities in the projected coordinates. Their full original products additionally have the normal tails $H_MRe_i$. Those tails must not be suppressed when testing membership in the original 4367-dimensional target module.

## 7. Actual evidence and the remaining numerical work

The source vector $z$ and quotient $q$ in (2.1) come from actual run 43756208221, step
~~~text
original56-single-kernel-bockstein-300
~~~
with execution source
~~~text
7fe5575b6c69b3e95aef4855c560d222dcf912dd
~~~
and semantic binding
~~~text
3456b533e6fba9d39af5638473f5b5afe04cbe342c8bddea7e88e752dd170c2a
~~~

The [published receipt](../notes/r150-source-kernel-session-789f/43756208221-original56-single-kernel-bockstein-300.json) proves all 56 exact first divisions, all 56 correction products, the complete second support $g=f$, and the free-coordinate identity. The complete temporary certificate is
~~~text
complete-original56-single-kernel-bockstein.json.gz
39654723 bytes
SHA256 147a40fac8ddcb873c0da24e962582722f6a7d602ed12dcfa741280476f8efcd
payload SHA256 0ca292247718946628997f173aa3caeabca49f22ae282cddd00638c77d1f81ac
~~~
Its field named twoDigitPolynomialSource is $z$, and exactQuotientAfterFAndSupport is $q$ because the actual support is $g=f$.

The original core logical SHA256 is
~~~text
752d21d7ca74ee5235c05ade9048ef48f120891c567abfb5132a4b2b33b745c8
~~~
The normalized full 56 by 22 matrix SHA256 used by the certificate is
~~~text
d14d2a7961f056925a153580aaa3b47ca4ee987f22f35bc585f4f3d123d6fb0e
~~~

This normalized-matrix identifier is the actual receipt's inputs.full56NormalizedMatrixSHA256 field. All new numerical consumers must compare that complete value and the complete constant-row-scale hash.

The new numerical work, if needed, is the polynomial Bezout/adjugate construction in §4 and the full original normal tails $B_0,H_M$ in §6. The current appendix proves the exact maps and their complete source ranges, but does not claim that those arrays have already been calculated, that $T$ vanishes, or that the remaining multiplier of degree at most 21 is constant.
