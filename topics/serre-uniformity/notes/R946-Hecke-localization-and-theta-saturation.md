# The precise Hecke-localization condition left after the low-weight calculation

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: proved algebraic criterion and obstruction to an inference, not a proof of the criterion for the actual high-weight packet.** R913 §8 and R932 §7 already state the possibility of congruent eigenforms and a longer Cartier chain. The additions here are: a perfect-pairing countermodel which retains a rank-one free Gorenstein Hecke module; an explicit theta-saturation condition which would suffice for the actual trace; and a proof that the theta map in that condition is injective. No generic reducedness or saturation is assumed.

## 1. Perfectness and multiplicity one do not imply a nonzero eigenline value

Let $T$ be a finite commutative local $k$-algebra, with maximal ideal $\mathfrak m$ and residue field $k$, and let $M$ be a $T$-module. A nonzero eigenfunctional of the residue character satisfies
$$
\lambda(\mathfrak mM)=0.
\tag{HS1}
$$
Consequently its value on an eigenvector $f$ depends on the image of $f$ in the cosocle $M/\mathfrak mM$. An eigenvector lies in $M[\mathfrak m]$, the socle, and the natural map
$$
M[\mathfrak m]\longrightarrow M/\mathfrak mM
\tag{HS2}
$$
need not be nonzero.

This failure remains possible under much stronger conditions than abstract Serre perfectness. Set
$$
T=k[\epsilon]/(\epsilon^2),\qquad M=T,
\qquad B(x,y)=[\epsilon](xy).
\tag{HS3}
$$
The Gram matrix in the basis $1,\epsilon$ is
$\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$, so $B$ is perfect. Every multiplication operator from $T$ is self-adjoint for $B$. The algebra is a local complete intersection and Gorenstein, and $M$ is free of rank one over it. Its common residue-character eigenspace is the single line $k\epsilon$.

Nevertheless, for
$$
f=\epsilon,\qquad\lambda(x)=[1]x=B(\epsilon,x),
$$
both the eigenvector and eigenfunctional are nonzero and unique up to scalars, while
$$
\lambda(f)=0.
\tag{HS4}
$$
Even a normalized coefficient does not prevent this: the linear functional $a_1(x)=[\epsilon]x$ has $a_1(f)=1$. If desired, multiplication by $\epsilon$ gives a nilpotent operator with image equal to kernel $k\epsilon$, and $\lambda$ annihilates its image. This is an algebraic countermodel to the proposed inference, not a claim that it is the actual modular packet or a second original quotient.

More generally, if $M$ is free of rank one over a nontrivial local algebra $T\ne k$, then every socle vector belongs to $\mathfrak mM$. Indeed, a socle element outside $\mathfrak m$ would be a unit, and $\mathfrak m$ annihilating a unit would imply $\mathfrak m=0$. Thus even a rank-one theorem over the localized Hecke algebra does not by itself establish the desired value. One must control the local algebra or the actual map (HS2).

## 2. What the cited multiplicity-one and theta-cycle results actually say

The original author manuscript of Edixhoven, *The weight in Serre's conjectures on modular forms*, Invent. Math. 109 (1992), §9, Theorem 9.2, gives dimension two for $J[\mathfrak m]$ under its hypotheses, including irreducibility and $2\le k<p$. Its Lemma 9.3 bounds the simultaneous eigenvector space of differentials by one. These are statements about $\mathfrak m$-torsion/common eigenspaces. They do not say that the complete localized Hecke algebra is a field or that there are no generalized eigendirections.

Its Proposition 3.3 describes theta cycles of eigenforms. Applying that statement to the one named CM eigenform does not establish divisibility for every vector in a generalized Hecke packet. A quotient of a generalized packet can contain an eigenclass which does not lift to an eigenvector in the original module.

The author source was read directly from
https://websites.math.leidenuniv.nl/edixhoven/public_html_rennes/publications/weight.ps.gz
(§§3 and 9, manuscript pp. 7–9 and 28–30). Downloading and converting that source for reading did not perform a mathematical experiment. No claim of actual localized reducedness is extracted from it.

## 3. Injectivity of the actual theta map below weight $p$

Use R932's normalized operator
$$
\mathcal T_k(H)=6(\mathcal A\partial_kH+k\mathcal B H),
$$
whose original full-six Fourier effect is $\Theta_Q=Q\,d/dQ$. Let $0<w<p$ and let $H$ be a cusp form of weight $w$ in the full original tame space. Then, for every positive integer $r$,
$$
\mathcal T^rH=0\quad\Longrightarrow\quad H=0.
\tag{HS5}
$$

Here is a proof using the actual fine Igusa cover. If $\mathcal T^rH=0$, its Fourier coefficients give $n^ra_n=0$, hence $na_n=0$ for every $n$. The rational function
$$
f=H/\mathfrak a^w
$$
has derivative zero, since $\mathfrak a(Q)=1$ and $df$ has Fourier expansion $\Theta_QH\,dQ/Q$. A rational differential with zero expansion is zero. Over the perfect residue field, $df=0$ makes $f$ a $p$th power in the function field. Every pole order of $f$ is therefore divisible by $p$.

Its only possible poles are supersingular. The numerator is regular, and $\mathfrak a$ has a simple zero at each fine Igusa supersingular point, so each pole has order at most $w<p$. Hence there are no poles. On the compact connected fine curve $f$ is constant; at a cusp it vanishes because $H$ is cuspidal and $\mathfrak a$ is a unit. Thus $f=0$ and $H=0$. The original tame quotient and full norm extension are recovered by the existing injective pullback/restriction, so this proves (HS5) in the actual spaces.

## 4. An explicit sufficient saturation statement

For the original two labels put
$$
w=k_-=p+1-r,\qquad k_+=r+2,\qquad r\in\{2,8\}.
$$
Let $M_{\rm CM}$ denote the full generalized packet of the actual CM Hecke character containing the named $F=V_w^\dagger$, with the actual full norm and tame transports retained. R913's eigenfunctional is supported on this packet and is nonzero on it: for the finite Hecke algebra, the other primary idempotents have residue-character value zero, so the eigenfunctional annihilates their images. This does not require $M_{\rm CM}$ to be one-dimensional.

The following statement would suffice:
$$
\boxed{\quad
\mathcal T^r(M_{\rm CM})
\subseteq\mathcal A^{r+1}S_{r+2}(H_6,k)
\quad}
\tag{HS6}
$$
with the exact transported marking on the right. The weights match, since
$$
w+r(p+1)=(r+1)p+1,
$$
$$
(r+1)p+1-(r+1)(p-1)=r+2.
$$
Equivalently, every vector in that entire generalized packet must have its $r$th theta image vanish to order at least $r+1$ at every fine tame Hasse zero. The Hasse divisor is reduced, and there are no cusp zeros of $\mathcal A$, so this pointwise condition is exactly the asserted divisibility by $\mathcal A^{r+1}$, including regularity and cuspidality of the quotient.

Assuming (HS6), divide by that Hasse power to obtain an injective map from $M_{\rm CM}$ to the low-weight cusp space; injectivity is (HS5). The Fourier Hecke relation is
$T_\ell\mathcal T^r=\ell^r\mathcal T^rT_\ell$ for the Gross modular normalization. Multiplication by a Hasse power commutes with these operators modulo $p$, since the weight difference is a multiple of $p-1$. In the actual raw Hecke normalization R913 supplies the compensating factors:
$$
\ell^{p-h}\ell^r=\ell^{h-1},
$$
because $r=2h-p-1$. Thus the original Hecke source is transported, rather than replaced by an unrelated packet. In particular the image is in the generalized zero-primary part of the original low-weight $T_5^2$.

For $r=2$ the entire low-weight character space is the original line of R918. For $r=8$ the complete double-marking calculation in [R942](../results/R942-original-complete-weight10-double-Hecke-zero-primary-line.md) shows that the full weight-ten zero-primary part is precisely the original line $kV_{10}^\dagger$ for every $p\ge41$. Therefore (HS6) would imply
$$
\dim M_{\rm CM}=1.
$$
The nonzero named $F$ spans it; the nonzero original eigenfunctional is supported on it; hence its value on $F$ would be nonzero. By R932/R936, the full supersingular trace would then be nonzero.

## 5. The still-unproved step is exactly (HS6)

R932 proves
$$
\mathcal T^rF=\mathcal A^{r+1}V
$$
for the one original CM companion. The newly controlled low-weight generalized packet does not promote that identity to (HS6). The linear-algebra model (HS3) illustrates why: a unique eigenvector can lie in a distinguished subspace even when an additional generalized vector does not.

A useful exact way to state the outstanding task is that the composite
$$
M_{\rm CM}\xrightarrow{\ \mathcal T^r\ }
S_{(r+1)p+1}(H_6,k)\longrightarrow
S_{(r+1)p+1}(H_6,k)/\mathcal A^{r+1}S_{r+2}(H_6,k)
\tag{HS7}
$$
must be proved zero. The known CM theta identity says only that it kills $F$. The eigenform-level theta-cycle theorem controls genuine eigenvectors, not every eigenclass in the quotient of a generalized packet. Perfect Serre duality, the one-dimensional common eigenline, Gorensteinness, or a rank-one freeness theorem alone do not eliminate this distinction.

This note does not assert that (HS6) is false for the original objects. It identifies a concrete sufficient condition and explains precisely why the currently proved low-weight results do not supply it. No new prime computations were executed.
