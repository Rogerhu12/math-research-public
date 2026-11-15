# R150: integral infinity Smith equivalence and the canonical 202-source kernel

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-15.  
Status: theorem from the completed original rational and finite-field spectra and the paid original source decompositions. No new mathematical execution is asserted.

## 1. Original ring and precise conclusion

Put

$$
D=\mathbb Z_{(31)},\qquad \mathcal R=D[[u]],\qquad
\mathfrak m=(31,u).
$$

Let $A=A_\infty(u):\mathcal R^{6188}\to\mathcal R^{4367}$ be the original natural infinity matrix. Its coefficients belong to $D[u]$. This is the natural weighted chart already defined by the original equations, not a claim that powers of $u$ are units. All fixed primitive contents, equation scalings and polynomial coordinate changes used to identify that chart have been checked to be $31$ units.

The [completed rational spectrum](R150-appendix-infinity-complete-tenth-connection-one-and-full-characteristic-zero-spectrum66.md) and the complete original finite-field spectrum agree term by term:

$$
a=(1,1,1,1,3,4,4,4,5,6,7,8,10,11).
\tag{1}
$$

There exist genuine matrices

$$
L\in\operatorname{GL}_{4367}(\mathcal R),\qquad
C\in\operatorname{GL}_{6188}(\mathcal R)
$$

such that, with the zero rectangular blocks understood,

$$
LAC=\operatorname{diag}(I_{4340},u^{a_1},\ldots,u^{a_{14}},0).
\tag{2}
$$

Consequently

$$
\operatorname{coker}_{\mathcal R}A
\cong
\mathcal R^{13}\oplus
\bigoplus_{i=1}^{14}\mathcal R/(u^{a_i}),
\qquad
\ker_{\mathcal R}A\cong\mathcal R^{1834}.
\tag{3}
$$

The reduction of this whole kernel is the complete formal kernel:

$$
(\ker_{\mathcal R}A)\otimes_D\mathbb F_{31}
\ \xrightarrow{\ \sim\ }\
\ker_{\mathbb F_{31}[[u]]}\overline A.
\tag{4}
$$

In particular the original cokernel has no $31$ torsion. These are conclusions about the complete original matrix, not about a chosen maximal minor or a chosen outside projection.

## 2. Unit-Schur proof over the two-dimensional local ring

The ring $\mathcal R$ is not being treated as a discrete valuation ring. Equation (2) is proved for this particular matrix by matching its two already determined spectra.

At the first step, both the rational and the mod-$31$ constant matrices have rank $4340$. Select an actual nonzero $4340$-minor of $\overline A(0)$. The corresponding original determinant is a unit of $D$, so the selected block is invertible over $\mathcal R$. Original row and column unit operations eliminate it.

The remaining block has constant term of rational rank zero: the original rational constant rank was exactly $4340$. Its constant term is therefore the zero matrix over $D$. The entire remaining block is divisible by $u$ in $\mathcal R$.

Apply the same argument to that divided block. At each stage the recorded finite-field constant pivots give an actual $D$-unit minor. The rational constant rank at that stage is the same, because the rational and finite-field positive spectra (1) coincide and the previous operations were units over both rings. After eliminating all those pivots, the remaining constant block has rational rank zero and is exactly zero over $D$. Only then is it divided by $u$.

The numbers of positive pivots at successive orders are

$$
4,0,1,3,1,1,1,1,0,1,1
\quad\text{at orders }1,\ldots,11.
$$

After all $4354$ nonzero directions have been removed, the remaining block is zero over $\mathbb Q((u))$, since the original generic rank is exactly $4354$. The inclusion $\mathcal R\hookrightarrow\mathbb Q((u))$ is injective, so that block is exactly zero over $\mathcal R$.

The block eliminations and the divisions therefore produce (2). Every transformation matrix has determinant with $u$-constant coefficient a $31$ unit. Reducing the transformations modulo $31$ remains invertible and proves (4), including surjectivity onto the complete formal kernel.

Only finitely many algebraic operations are required. Starting from the rational polynomial entries of the original matrix, the resulting transformations may be taken to have rational-function entries regular over $D$ at $u=0$. No explicit large rational transformation array has been computed or retained by this proof.

## 3. The already paid original Koszul split

Retain the same $4340$ original constant-unit source coordinates $P$ and complementary $1848$ coordinates $H$ as in [the original 216-source reduction](R150-appendix-original-koszul-source-direct-sum-and-216-column-reduction.md). On the corresponding original unit output coordinates write

$$
A=\begin{pmatrix}U&V\\W&Z\end{pmatrix},
\qquad S=Z-WU^{-1}V.
$$

The original $U(0)$ determinant is a $31$ unit. Define the exact source graph

$$
j(h)=\binom{-U^{-1}Vh}{h}.
\tag{5}
$$

Thus the correction in $j$ is only on the original $P$ source coordinates; its original tail coordinates are precisely $h$.

The $1632$ original Koszul polynomial curves $\Phi$ were constructed directly from the original seventeen equations and verified. Their tail coordinates satisfy

$$
T=[\Phi_H,E]\in\operatorname{GL}_{1848}(\mathcal R),
$$

where $E$ is the same actual $216$-coordinate embedding. The selected constant minor of $\Phi_H$ has determinant $15$ modulo $31$.

Let

$$
M=SE,\qquad \mathcal K=\ker_{\mathcal R}M.
$$

The original identities, already valid over $\mathcal R$, give

$$
S\Phi_H=0,\qquad j(\Phi_Hx)=\Phi x,
$$

and the exact source decomposition

$$
\ker_{\mathcal R}A
=\Phi\mathcal R^{1632}\oplus j(E\mathcal K).
\tag{6}
$$

The first summand is a split free summand, not merely a collection of independent generic curves.

By (3) and (6), $\mathcal K$ is a finite projective module of rank $202$. The ring $\mathcal R$ is local, hence $\mathcal K$ is free of rank $202$.

Moreover, reduction of (6) agrees with the already paid identical original split over $\mathbb F_{31}[[u]]$. Equation (4), the common original $U,\Phi_H,E$, and uniqueness in the split imply

$$
\mathcal K/31\mathcal K
\ \xrightarrow{\ \sim\ }\
\ker_{\mathbb F_{31}[[u]]}(\overline S E).
\tag{7}
$$

No general assertion that kernels commute with reduction was assumed; here it follows from the complete Smith equivalence and the explicit split.

## 4. Why the old high-source free coordinates are now legitimate

This conclusion uses the **source** mapper from [the two regular 202-mapper construction](R150-appendix-two-regular202-mappers-and-independent-precision-recovery.md), with its subsequent [complete original transport](R150-appendix-complete-original-higher-kernel-eight-positive-indices-and-length26.md). It does not use the outside left mapper to choose source coordinates.

The actual source mapper is in the same ordered $216$ original coordinates $E$. The recorded unit-Schur procedure removes all fourteen positive directions of $\overline M$. The original generic rank is fourteen, so after the last pivot its remaining formal block is identically zero. Consequently its free-column back-substitution defines the **complete formal** field kernel, not only a family of solutions through a finite precision.

The actual free set $F_H$ consists of $202$ of those $216$ coordinates. Its complement, as one-based original source indices, is

$$
E\setminus F_H=
(5520,5521,5522,5523,5524,5525,5537,5538,5539,5540,
6154,6168,6171,6184).
\tag{8}
$$

The retained series through degree $21$ has the free block $I_{202}$, and the formal Schur construction gives that same identity exactly. This mathematical full-rank stopping argument, together with the actual original coordinate dictionary, is essential: a finite-jet identity alone would not justify the following step.

Consider the original coordinate projection

$$
p_{F_H}:\mathcal K\longrightarrow\mathcal R^{202}.
$$

By (7), its reduction modulo $31$ is an isomorphism of complete formal field kernels. In particular its reduction modulo $\mathfrak m=(31,u)$ is an isomorphism. After choosing any free basis of $\mathcal K$, its determinant is therefore outside $\mathfrak m$, hence a unit of $\mathcal R$. Thus

$$
\boxed{p_{F_H}:\mathcal K\xrightarrow{\sim}\mathcal R^{202}.}
\tag{9}
$$

There is a unique canonical matrix

$$
N_H\in\operatorname{Mat}_{216\times202}(\mathcal R),
\qquad
MN_H=0,\qquad N_H[F_H,:]=I_{202}.
\tag{10}
$$

It reduces to the same previously constructed complete formal field mapper. Its original source transport

$$
K_H=j(EN_H)
\tag{11}
$$

is now a genuine $31$-integral, primitive basis for the second summand in (6).

Over $\mathbb Q(u)$, the conditions in (10) are a uniquely solvable rational linear system. Hence the canonical entries are rational functions; equation (9) proves that their expansions are regular and $31$ integral. This proves existence and the exact original normalization. It does not claim that all those characteristic-zero entries were numerically computed in this step.

## 5. The actual dictionaries used in (8)–(10)

The direct-sum construction fixes the following original dictionaries:

| Original object | SHA256 |
|---|---|
| $1848$ complementary source coordinates $H$ | `c4a2b6d005c23a2df7ea71ceef3fea9f1f7dd46ad1e361077e85d571c98c0148` |
| $4340$ original unit source coordinates $P$ | `94c940a7b5ff4768e7e1b0820033eca3cabf19bb8958c7cab52c1e1eefb09837` |
| $4340$ original unit output coordinates | `64fa0d3161556aa057e3003e5d0b7998a5aa03373838805dd15b721666254055` |
| $1632$ selected Koszul tail positions | `db111fbbaa1a67989c0944e58e3e1f3468d1b4c1fedb1d88daefec5764da337c` |

The actual ordered $216$ coordinates and ordered $202$ source free coordinates are in the [published mapper receipt](../notes/r150-source-kernel-session-789f/43740928483-higher-two-regular202-mappers-preparation.json), fields `highComplementOriginalSourceRowsOneBased` and `highFreeOriginalSourceRowsOneBased`. Their difference is exactly (8). The mathematical binding of that mapper construction is

`7d781d083a66e7cb2b66426ea47753b7a50e7de5e10426642eb4246de6c46cca`.

The source unit stages remove original $216$-coordinate positions

$$
(0,208,211,212,1,2,3,4,5,214,6,7,9,8).
$$

The full original source transport later checked all $19406948$ original product coordinates at the retained precision, with the complete $202$ original source free block. This verifies that the regular small mapper is being used in the correct original source coordinates.

No outside free dictionary or old selected-minor source dictionary is substituted into (9).

## 6. Consequences and boundaries

The original cokernel, original full right kernel, and this particular canonical $202$-source summand now have compatible $31$-integral structures. This supplies the previously missing source-side normalization for a genuine characteristic-zero high-source calculation.

It does not by itself give a compatible primitive basis for the left kernel of the **outside Koszul matrix**. Nor does it determine the valuation of the map from the source kernel to the old selected source complement. Thus it does not prove either

$$
\sigma_{O,\mathbb Q}=149
\quad\text{or}\quad
\delta_{\mathrm{high},\mathbb Q}=26.
$$

It also does not make the previously selected order-$243$ maximal minor have a $31$-unit leading coefficient. The source split (6) and the particular projection (9) may instead be used to select and prove properties of a different set of original columns; that must be stated as a different minor with its own original row and column dictionaries.

All assertions here are exact deductions from the paid original identities, the actual complete spectra, and the actual complete field source mapper. No new matrix elimination, new rational array, or unperformed original multiplication is recorded as an execution.
