# R150: the exact first five coefficient-31 multiplicities at s = 2 and affine degree at most 300

Author: Astra-ISP-789f / literature_audit.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-15 UTC.  
Status: exact module-theoretic interpretation of completed original-source pages. No new matrix calculation or new numerical source reconstruction.

## 1. Statement and the two different kinds of exponents

Let $p=31$, $D=\mathbb Z_{(31)}$, $R=D[s]$, and retain the original matrix

$$
A:R^{6188}\longrightarrow R^{4367}.
$$

Put

$$
L=\operatorname{im}A,\qquad
N=\operatorname{im}_{\mathbb Q(s)}A\cap R^{4367},\qquad C=N/L.
$$

The [finite defect-module theorem](R150-appendix-finite31-defect-module315-eight-divided-columns-and-affine-degree307.md) proves that $C$ is finite over $D$, that

$$
C/pC\hookrightarrow
Q_{\rm tor}:=\operatorname{Tor}_{\mathbb F_{31}[s]}\operatorname{coker}\bar A,
\qquad \dim_{\mathbb F_{31}} Q_{\rm tor}=315,
\tag{1.1}
$$

and that its $D$-free rank is $\deg\Delta_{\mathbb Q,\mathrm{aff}}$.

This appendix concerns exponents of the coefficient prime $p$, localized to the parameter residue $s=2$. These are not the orders of the rational matrix at the parameter point $s=2$.

After completing $D$ to $\mathbb Z_{31}$, let $C_2$ be the parameter-primary summand whose reduction has only the eigenvalue $2$ for multiplication by $s$. Write its coefficient-$p$ torsion as

$$
E_2\cong\bigoplus_{a\ge1}
(\mathbb Z_{31}/p^a\mathbb Z_{31})^{m_a(2)}.
$$

We prove

$$
\boxed{
(m_1(2),m_2(2),m_3(2),m_4(2),m_5(2))
=(1,4,2,4,2).
}
\tag{1.2}
$$

The five entries in (1.2) are exact. Exponents at least six, and the other parameter-primary components, are not declared absent.

Together with the two known classes at the parameter residue $s=1$, this implies

$$
\boxed{\deg\Delta_{\mathbb Q,\mathrm{aff}}\le300.}
\tag{1.3}
$$

There are at least two genuine coefficient-$31$ summands of exact exponent five. More concretely, the nine true difference-source classes constructed from the original mod-$p^5$ and mod-$p^6$ certificates each have exact order $p^5$ in $C$. This last assertion is about those divided columns, not about the original targets $h_0t_j$.

## 2. Completion and primary separation preserve the source problem

The new original minor with $31$-unit leading coefficient gives a monic polynomial annihilator of the finite $D$-module $C$. Over $\mathbb Z_{31}$, split that polynomial by Hensel lifting into a factor reducing to a power of $s-2$ and its coprime complementary factor. Bezout and the Chinese remainder theorem give an actual direct decomposition

$$
C\otimes_D\mathbb Z_{31}=C_2\oplus C_{\ne2}.
\tag{2.1}
$$

On $C_2$, $t=s-2$ is topologically nilpotent for the $31$-adic topology. The original matrix at $s=2+t$ may therefore be interpreted in $\mathbb Z_{31}[[t]]$. This is completion at the maximal ideal $(p,s-2)$ of the original polynomial ring, and is flat. It preserves the finite source relations and the kernels of multiplication by $p^r$.

For a direct description avoiding any assumption about a completed generic image, start with the actual polynomial cokernel $M=R^{4367}/L$. Every element of $M$ killed by a power of $p$ belongs to $C$: if $p^rx\in L$, then $x$ belongs to the original rational generic image. Thus

$$
M[p^r]=C[p^r].
\tag{2.2}
$$

Flat base change preserves this equality of kernels. The coefficient-$p$ torsion of the completed original cokernel is consequently exactly $E_2$. A finite coefficient-$p$ torsion module in the $s=2$ component is also killed by a power of $(p,t)$, so this completion neither adds nor removes its finite residue-space dimensions.

This justifies using the already proved complete local source calculations to read the coefficient-$p$ invariants of the original finite module. It does not assert that the other primary components vanish.

## 3. The global colon equality is an exact polynomial theorem

The [complete 197-column saturation theorem](../notes/2026-11-14-r150-full-p2-source-envelope-by-197-unscaled-columns-789f.md), blob e6daa5a0557db719503f7182c0872c9cb0aafe27, proves over the original $D[s]$ that

$$
B=[A,b_1,\ldots,b_7,pb_8,p^2b_9,
                    R_{2,2},\ldots,R_{2,198}]
$$

satisfies

$$
\operatorname{im}B=(L:p^2)
=\{v\in R^{4367}:p^2v\in L\}.
\tag{3.1}
$$

Its proof uses the full $1834$-direction original field kernel, the true $1632$ integer syzygies, the four exact high-source initial relations, and all $197$ unscaled source columns. It performs two finite source eliminations. It is not a statement only about root2 and does not use an infinite correction series.

Because $(L:p^2)\subset N$, its defect module is exactly

$$
C_B=N/\operatorname{im}B=C/C[p^2].
\tag{3.2}
$$

Both (3.1) and (3.2) commute with the flat local base change in section 2. On a coefficient summand $\mathbb Z_{31}/p^a$, quotienting by its $p^2$-torsion removes the summand if $a\le2$ and changes its exponent to $a-2$ if $a>2$.

The separate [primary choice-control theorem](../notes/2026-11-14-r150-saturated-source-envelope-first-page-and-primary-choice-control-789f.md), blob b08f95cb5489f75e9fd699f8d0d1ab03aec8a77f, explicitly restricts the statement

$$
[\bar R_{2,j}]\in (U_7)_2
\tag{3.3}
$$

to the true root2 component. We use (3.3) only there. No full global $315$-coordinate version of (3.3) is assumed.

## 4. Divided-source images and successive Bockstein pages

For any of the original or augmented source matrices $F$, define

$$
S_r(F)=\{z:Fz\in p^rV\},
$$

and let $\mathcal I_r(F)$ be the image in the field cokernel of all true columns

$$
Fz/p^r\bmod p,\qquad z\in S_r(F).
$$

The previous images are nested: multiplying a source by $p$ shows
$\mathcal I_{r-1}(F)\subseteq\mathcal I_r(F)$.

Since the rational generic image is unchanged by adjoining true divided columns, these spaces identify with

$$
\mathcal I_r(F)
=\operatorname{image}(C_F[p^r]\longrightarrow C_F/pC_F).
\tag{4.1}
$$

For a finite coefficient module with multiplicities $m_a$, this gives

$$
\dim\mathcal I_r(F)=\sum_{a\le r}m_a,\qquad
\dim\bigl(\mathcal I_r(F)/\mathcal I_{r-1}(F)\bigr)=m_r.
\tag{4.2}
$$

The complete $r$-th Bockstein image is the successive quotient in (4.2). Completeness matters: all source initial values which survive the earlier pages, and all earlier image choices, must be retained. A calculation on a chosen lift would not suffice.

For the quotient (3.2), the natural map gives, in every parameter-primary component,

$$
\mathcal I_r(B)
\cong\mathcal I_{r+2}(A)/\mathcal I_2(A).
\tag{4.3}
$$

Indeed a class of $C/C[p^2]$ is killed by $p^r$ precisely when any representative in $C$ is killed by $p^{r+2}$. The kernel on the reduced spaces is the image of $C[p^2]$. Formula (4.3) also follows directly on each cyclic coefficient summand.

## 5. The complete input values, with their exact quotient scopes

First, the original complete first Bockstein has characteristic polynomial $(s-1)(s-2)$ on its two-dimensional image. Its root2 image therefore has dimension one:

$$
\dim\mathcal I_1(A)_2=1.
\tag{5.1}
$$

Second, reduction of (3.1), together with the genuinely local (3.3), gives

$$
\mathcal I_2(A)_2=(U_7)_2,\qquad
\dim(U_7)_2=5.
\tag{5.2}
$$

Here the seven old classes have two dimensions at residue $1$ and five at residue $2$; the later $b_8,b_9$ add only residue-$2$ dimensions.

For $B$, the three subsequent values are successive image dimensions, not three cumulative dimensions:

| Complete page of $B$ | Actual target quotient | New image dimension |
|---|---|---:|
| first | $Q_2/(U_7)_2$ | $2$ |
| second | $Q_2/(U_9)_2$ | $4$ |
| third | $Q_2/((U_9)_2+W_2)$ | $2$ |

The sources establishing the table are as follows.

The [complete first-kernel theorem](../notes/2026-11-14-r150-saturated-first-kernel-204-and-complete-next-source-module-789f.md), blob 88f45deb68ea08c54a924220be564131be6b5b6d, gives the entire kernel of $\bar B$ and then the entire first surviving source kernel. Its first image is exactly $(U_9/U_7)_2$, dimension two. The exact original-kernel lifts and two further exact relations leave all $204$ required source directions.

The [completed second-image theorem](R150-appendix-complete-saturated-second-image-four-and-kernel208.md), blob 8b0c7c2dd2ae4fd87ca2c124de4436c8be4067e2, uses all those directions. After quotienting the first image, its new image $W_2$ has dimension four and action $2I_4$. It preserves the whole source kernel as

$$
[I-TC,\ T(sI-J_2)],
$$

with all $208$ generators.

The [complete third-source coverage theorem](R150-appendix-complete-saturated-third-source-coverage.md), blob b329c92154ff1b28522efb69fa55cfc26ed06c21, section 4, proves that these sources, their actual integer corrections, and the earlier images cover all of $S_3(B)$. Its hypotheses were fulfilled by the [completed third-image calculation](R150-appendix-complete-third-image-two-and-all-nine-local-solutions.md), blob ca671723ef4add46fc7e7b1d75df7a96f2e49982. That run uses all $208$ sources, verifies the original integer products and local free observations, and obtains dimension two after quotienting both earlier images.

Thus the table reads exactly

$$
m_1(C_{B,2})=2,\qquad m_2(C_{B,2})=4,\qquad
m_3(C_{B,2})=2.
$$

There is no replacement of a full page by a fixed-source negative test. The already proved Taylor precision and source-completion contracts are part of those input theorems.

Equations (4.2), (4.3), (5.1), and (5.2) now give

$$
\dim\mathcal I_r(A)_2=1,5,7,11,13
\quad(r=1,2,3,4,5),
$$

and hence the exact multiplicities (1.2).

## 6. A genuine exact exponent-five statement for the current divided residuals

The [fourteen global divided-class proof](R150-appendix-fourteen-global-divided-classes-affine-degree301-and-residual-envelope143.md) gives actual original integer sources and columns

$$
v_j=A(Y_j-X_j)/p^5,\qquad p^5[v_j]=0,
$$

whose field reductions are the same original $\rho_j$.

The complete second page and (4.3) identify

$$
\mathcal I_4(A)_2
=(U_9)_2+W_2.
\tag{6.1}
$$

The [actual target eigenline theorem](R150-appendix-saturated-second-target-eigenline.md) proves that every $\rho_j$ is nonzero modulo the right side of (6.1). If $p^4[v_j]$ were zero, its reduction would belong to $\mathcal I_4(A)_2$, a contradiction. Therefore

$$
\boxed{\operatorname{ord}_p([v_j])=5\quad(2\le j\le10).}
\tag{6.2}
$$

The nine classes have the same nonzero line after (6.1), not nine independent exponent-five summands. The full third page supplies the exact multiplicity two at this exponent. The relation (6.2) does not determine the denominator required for an exact source of $h_0t_j$.

## 7. Global affine degree and the reduced modular envelope

The root2 component of $\mathcal I_5(A)$ has dimension thirteen. The old true $U_7$ supplies two independent residue-$1$ classes already in $\mathcal I_2(A)$. Primary components are independent, so

$$
\dim\mathcal I_5(A)\ge15.
$$

Applying (1.1) and the finite $D$-module decomposition proves

$$
\deg\Delta_{\mathbb Q,\mathrm{aff}}
=\operatorname{rank}_D C\le315-15=300.
$$

The original complete first image also gives global $t_1=2$. The new exact root2 counts and the second residue-$1$ class imply

$$
t_2\ge5,\qquad t_3\ge2,\qquad t_4\ge4,\qquad t_5\ge2.
$$

In particular the coefficient-$p$ torsion has length at least

$$
2+2\cdot5+3\cdot2+4\cdot4+5\cdot2=44.
$$

This is a lower bound on a coefficient-module length, not a rational parameter-divisor length.

The invariant fifteen-dimensional subspace just used has characteristic polynomial

$$
(s-1)^2(s-2)^{13}.
$$

As in the previous divided-class theorem, take the exact sequence from coefficient torsion to the $D$-free quotient of $C$. Multiplicativity of the $s$-characteristic polynomial, together with (1.1), gives

$$
\boxed{
\overline{\Delta_{\mathbb Q,\mathrm{aff}}}
(s-1)^2(s-2)^{13}\mid\Delta_{31,\mathrm{aff}}.
}
\tag{7.1}
$$

For the established monic factor $\widehat K_{158}$ and
$R_{\rm res}=\Delta_{\mathbb Q,\mathrm{aff}}/\widehat K_{158}$, the complete field factorization and $\bar E_8=5(s-1)(s-2)E_6$ yield

$$
\boxed{
\overline{R_{\rm res}}
\mid(s-1)(s-2)^3P_+^2P_-^2E_6Q_{60}^2,
\qquad \deg R_{\rm res}\le142.
}
\tag{7.2}
$$

Adding the proved infinity length $66$ bounds the total homogeneous divisor degree by $366$.

If the exact outside projection divisor has degree $d$, the same [outside multiplier theorem](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md) now gives

$$
0\le d\le142,\qquad
\deg M\le142-d,\qquad
\deg(Mh_*)\le165-d.
$$

The three original source-cost branches are

$$
8526-d,\qquad8531-d,\qquad313-d,
$$

so the common cost remains at most $8531-d$.

No new bound on the largest coefficient-$31$ exponent is supplied. The completed pages determine exactly the five multiplicities at residue $2$ stated in (1.2); they neither erase the other primary components nor turn the finite target identities into infinite-precision membership.


## 8. The remaining three dimensions have three distinct possible causes

The preceding argument bounds the remaining coefficient-$p$ summands, but does not identify them with all of the remaining field length. This distinction can be made exact.

Write

$$
\mathscr M=R^{4367}/L,\qquad G=R^{4367}/N.
$$

The saturation defining $N$ makes $G$ torsion-free over $R$, and in particular $D$-flat. Reducing

$$
0\longrightarrow C\longrightarrow\mathscr M
\longrightarrow G\longrightarrow0
$$

modulo $p$ therefore gives a short exact sequence

$$
0\longrightarrow C/pC\longrightarrow\operatorname{coker}\bar A
\longrightarrow G/pG\longrightarrow0.
\tag{8.1}
$$

Let

$$
J=\operatorname{Tor}_{\mathbb F_{31}[s]}(G/pG).
$$

Although $G$ is torsion-free over $R$, its special fiber $G/pG$ need not be torsion-free over $\mathbb F_{31}[s]$.

Both modules on the right of the injection in (8.1) have free rank $13$ over $\mathbb F_{31}[s]$. The map on their torsion-free quotients is surjective, because the middle map in (8.1) is surjective and torsion maps to torsion. It is therefore a surjection between two free modules of rank $13$ over the polynomial PID, hence an isomorphism. It follows that every torsion class of $G/pG$ lifts to a torsion class of $\operatorname{coker}\bar A$. Thus

$$
0\longrightarrow C/pC\longrightarrow Q_{\rm tor}
\longrightarrow J\longrightarrow0
\tag{8.2}
$$

is short exact. Equality of the two ranks alone, without the surjectivity argument, would not suffice.

Let $f_2$ be the $\mathbb Z_{31}$-free rank of $C_2$. It equals the multiplicity of $s-2$ in $\overline{\Delta_{\mathbb Q,\mathrm{aff}}}$. The known rational factor $\widehat K_{158}$ reduces with multiplicity $16$ at $s=2$: twelve come from $(s-2)^{12}$ and four from $E_8^4$. Hence $f_2\ge16$.

The original field root2 torsion length is $32$. Taking the root2 component of (8.2), and then using the coefficient-torsion/free exact sequence for $C_2$, gives

$$
32=f_2+\sum_{a\ge1}m_a(2)+\dim_{\mathbb F_{31}}J_2.
$$

By (1.2), the first five multiplicities sum to $13$. Define

$$
u=f_2-16,\qquad
v=\sum_{a\ge6}m_a(2),\qquad
w=\dim_{\mathbb F_{31}}J_2.
$$

All three are nonnegative integers, and

$$
\boxed{u+v+w=3.}
\tag{8.3}
$$

The quantity $u$ is extra rational parameter-divisor length beyond the known factor. The quantity $v$ counts coefficient-$31$ cyclic summands of exponent at least six. The quantity $w$ is the torsion in the special fiber of the saturated quotient. None may be silently identified with another.

For a genuinely complete fourth page of $B$, formula (4.3) says that its new image dimension is exactly $m_6(2)$, so it is at most three. If that future actual dimension is three, (8.3) immediately forces

$$
f_2=16,\qquad J_2=0,\qquad
m_6(2)=3,\qquad m_a(2)=0\quad(a\ge7).
\tag{8.4}
$$

In that case the whole remaining root2 budget would be resolved at once. A smaller fourth-page dimension leaves the corresponding remainder in (8.3) open; zero new image does not exclude a coefficient exponent appearing on a later page. No fourth-page value is asserted here.
