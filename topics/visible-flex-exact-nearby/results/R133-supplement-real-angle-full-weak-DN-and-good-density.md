# R133 supplement: real angle transport of the complete weak DN pairing

2026-11-15, visible-exact-astra-0df9.

**Exact real-coordinate identities and bounded half-order transport.**
This supplements the
[unknown-angle good tangent](R133-supplement-exact-unknown-outer-angle-good-tangent-and-full-means.md).
It gives no new DN inverse or small-background theorem. It explains how a
proved physical DN difference, its relative form, and its true scalar
charges can be read in the common fixed angle.

The actual physical DN and its independent source columns remain
[N.16--N.28](R119-supplement-actual-long-screening-complete-Sobolev-DN-and-cap-facing-port.md).
All statements here are for real orientation-preserving maps. They do not
assert a bounded raw composition family for a complex angle.

## 1. Scalar and density are different trace objects

Let $\theta=\tau(x)$ be a degree-one circle diffeomorphism, preserving
the fourfold class, and put $j=\tau_x>0$. The normalized measures are
$d\mu_\theta=d\theta/(2\pi)$ and $d\mu_x=dx/(2\pi)$.
For scalar heights write
$$
 T_\tau f=f\circ\tau .
 \tag{D.1}
$$
A conormal output is paired with height. Its correct pullback is the
density map
$$
 D_\tau q=j(q\circ\tau),\qquad
 \langle D_\tau q,g\rangle_x
       =\langle q,T_\tau^{-1}g\rangle_\theta .
 \tag{D.2}
$$
For distributions the second equation defines $D_\tau$. Thus
$D_\tau=(T_\tau^{-1})^*$ in the dual height/conormal pairing. One does
not replace $D_\tau$ by $T_\tau$ or by an unweighted matrix transpose.

The physical scalar mean of $T_\tau f$ is
$M_j(T_\tau f)=\langle jT_\tau f\rangle_x=\langle f\rangle_\theta$.
For a density and for a constant height, respectively,
$$
 \langle D_\tau q,1\rangle_x=\langle q,1\rangle_\theta,
 \qquad T_\tau 1=1 .
 \tag{D.3}
$$
Consequently the true total flux and the constant-height gauge have
exactly the original units.

## 2. A complete quantitative half-order bound

Assume
$$
                    1/2\le j(x)\le2 .
 \tag{D.4}
$$
The inverse has the same derivative bounds. If $d(x,y)\in[0,\pi]$
is circle distance, both images of the two connecting arcs have
length at least half their original length, while the image of the
shorter arc has length at most twice its original length. Hence
$$
 {1\over2}d(x,y)\le d(\tau(x),\tau(y))\le2d(x,y).
$$
The chord distances satisfy the same factors:
$$
 {1\over2}\le
 {|\sin((\tau(x)-\tau(y))/2)|\over|\sin((x-y)/2)|}\le2 .
 \tag{D.5}
$$
For the lower bound use $\sin(d/4)\ge\frac12\sin(d/2)$.
For the upper bound separate $d\le\pi/2$, where
$\sin d\le2\sin(d/2)$, from $d\ge\pi/2$, where
$1\le2\sin(d/2)$. This avoids choosing inconsistent real lifts at
the antipodal point.

For smooth functions the exact Fourier identity is
$$
 \sum_{n\in\mathbb Z}|n||f_n|^2
 =\iint { |f(x)-f(y)|^2\over4\sin^2((x-y)/2)}
                         \,d\mu_x\,d\mu_y .
 \tag{D.6}
$$
It follows first on a single exponential from the full geometric
sum, and then by orthogonality. Positivity and Fourier completion
extend it to $H^{1/2}$. Restricting to $4\mathbb Z$ changes no factor.

After the exact change of variables in both integrals, the physical
kernel relative to the fixed-$x$ kernel has multiplier
$$
 j(x)j(y)\,
 {\sin^2((x-y)/2)\over
             \sin^2((\tau(x)-\tau(y))/2)}\in[1/16,16].
 \tag{D.7}
$$
The ordinary $L^2$ squared norms change by factors in $[1/2,2]$.
Using
$\langle n\rangle\le1+|n|\le\sqrt2\langle n\rangle$ for the
usual inhomogeneous half-order norm, this proves
$$
 \|T_\tau\|_{H^{1/2}\to H^{1/2}},
 \ \|T_\tau^{-1}\|_{H^{1/2}\to H^{1/2}}
 \le4\,2^{1/4}<5 .
 \tag{D.8}
$$
True duality in (D.2) then gives
$$
 \|D_\tau\|_{H^{-1/2}\to H^{-1/2}},
 \ \|D_\tau^{-1}\|_{H^{-1/2}\to H^{-1/2}}<5 .
 \tag{D.9}
$$
This proof does not use the false assertion that an arbitrary
$L^\infty$ Jacobian is a multiplier on $H^{-1/2}$. The density map
is bounded as the dual of the real scalar pullback.

The scalar pullback on a negative Sobolev space is a different
operator. If such a scalar curvature input is required, its
Jacobian multiplier has to be paid separately using the actual
background regularity; (D.9) does not supply that extra assertion.

## 3. DN differences and their correct common reference

Let $\mathcal N:H^{1/2}_\theta\to H^{-1/2}_\theta$ be the complete
physical height-to-conormal operator. In fixed $x$ its exact form is
$$
       \widetilde{\mathcal N}
           =D_\tau\mathcal N T_\tau^{-1}.
 \tag{D.10}
$$
If $\mathcal N_0$ is a physical reference, use the same angle on
both operators:
$$
 \widetilde{\mathcal N}_0
      =D_\tau\mathcal N_0T_\tau^{-1},\qquad
 \|\widetilde{\mathcal N}-\widetilde{\mathcal N}_0\|
       <25\|\mathcal N-\mathcal N_0\| .
 \tag{D.11}
$$
For example the genuine radial reference in N.17 is
$\mathcal N_0=\mu_0|D_\theta|\coth(L|D_\theta|)P_{\perp,\theta}$.
Its pulled version in (D.11) is generally **not**
$\mu_0|D_x|\coth(L|D_x|)P_{\perp,x}$. Replacing the former by the
latter requires a separate real-angle form comparison, including
the finite-length reflection. No such replacement is made here.

For any full bilinear or sesquilinear pairing and
$g=T_\tau f,\ h=T_\tau e$,
$$
 \langle(\widetilde{\mathcal N}-\widetilde{\mathcal N}_0)g,h\rangle_x
     =\langle(\mathcal N-\mathcal N_0)f,e\rangle_\theta .
 \tag{D.12}
$$
Thus a relative form bound measured against the **same pulled
reference energy** has exactly the original relative constant.
This also preserves a nonsymmetric form and its genuine dual
estimate. It does not infer a new adjoint certificate from forward
sample columns.

If the homogeneous physical operator kills constant heights and
has zero total output flux, (D.3) proves the corresponding two
properties in fixed $x$. In N.17 the latter follows only after the
complete holonomy-mean slope has been included in the product with
$\mu$. Neither property permits deleting that slope before forming
the full operator. Affine flux charges need not vanish.

## 4. The actual long formula and the independent ports

At the long left endpoint use the exact notation of N.16--N.24.
Write a flat superscript for scalar pullback to $x$, and let
$\mathcal K'_{j,Z}$ be the derivative of the complete pulled slope
graph at fixed $j$, including the true $C_R\to f_*$ feedback and
the holonomy mean. For an input $g^\flat$,
$$
 \widetilde{\mathcal N}_{B,Z}g^\flat
 =-j\mu^\flat\{
       \mathcal K'_{j,Z}J_jg^\flat-d^\flat D_jg^\flat\}.
 \tag{D.13}
$$
The normalization $\delta f_B=J_jg^\flat/(a_Bw_B)$ is the same as
N.16: the factor $a_Bw_B$ cancels in the homogeneous slope column.
It is retained in the independent N.23 source column.

In particular the independent right height/curvature-source term
is the density pullback of
$$
 -\mu a_Bw_B\,D_{f_*}\mathcal K_B
                  (D_Z\Phi_R\,\delta Z+f_*^{\rm src}).
 \tag{D.14}
$$
The input $\delta Z$ keeps its actual physical curvature norm and
its actual good scalar variation. This note neither enlarges that
source class nor replaces its scalar conversion by (D.9). The
other weak, ordinary, flux, and height charges keep their full
N.24--N.25 order and physical factors.

The same distinction applies to the two curvature means $B_0,C_0$.
They are full independent outputs of the curvature graph; they are
not the homogeneous total conormal mean in (D.3).
Constant physical height remains one independent gauge. The two
end mean heights are related by the original radial integral,
not independently reset by a coordinate change.

## 5. Varying the angle: the good conormal density

For the unknown real angle of U.1--U.5 put
$\eta=\dot\tau$, $b=\eta/j$, $\dot j=\eta_x$. For a pulled scalar
$F$ define $\dot F^g=\dot F-bF_x$. Periodic integration by parts
gives the exact weak product rule
$$
 {d\over da}\langle jFG\rangle_x
     =\langle j(\dot F^gG+F\dot G^g)\rangle_x .
 \tag{D.15}
$$
For real variation and a Hermitian pairing, the second term is
conjugated in the usual manner. The same rule with a coefficient
$a$ has the additional term $\langle j\dot a^g FG\rangle$.

If $n^\flat$ is the physical conormal scalar and
$\lambda=j n^\flat$ its fixed-$x$ density, its good tangent is
$$
 \boxed{\quad
 \dot\lambda^g_{\rm dens}
   :=\dot\lambda-\partial_x(\eta n^\flat)
     =j(\dot n^\flat-bn^\flat_x).
 \quad}
 \tag{D.16}
$$
Using $\dot\lambda-b\lambda_x$ instead would miss a term.
The extra expression in (D.16) is an angular total derivative,
so its full mean is zero. Consequently all genuine mean flux
charges have their actual derivatives.

Suppose, for example, the conormal scalar is
$n^\flat=A^\flat h^\flat_t+B^\flat D_jh^\flat$.
The U commutators give its exact good derivative
$$
 \dot n^g
  =\dot A^g h^\flat_t+A^\flat z_t
       +\dot B^gD_jh^\flat+B^\flat D_jz ,
 \quad z=\dot h^\flat-bh^\flat_x .
 \tag{D.17}
$$
There is no separate $\dot j_x$ term in (D.17).
The complete geometric coefficient derivatives, source terms, and
any nonzero boundary residual still remain.

At an exact matching point the two sides have the same scalar
trace and conormal density, so their transport terms cancel.
Away from exact matching, (D.16) applies to the actual difference:
the derivative of a nonzero boundary residual is not silently
replaced by its good derivative without the displayed transport.

## 6. Scope for a new nearby-background estimate

A proved physical estimate
$\|\mathcal N_{B,Z}-\mathcal N_{B,0}\|
 _{H^{1/2}\to H^{-1/2}}\le\varepsilon$
therefore yields a fixed-$x$ norm estimate smaller than
$25\varepsilon$ under (D.4), and the identical relative form
estimate in the common pulled reference energy. Its true mean,
adjoint, and independent source columns are preserved as above.

This conclusion is conditional on that physical estimate and the
actual background defining both operators. It does not manufacture
a new physical DN difference from a high-order Sobolev inverse or
from positivity alone. It does not replace the actual reference
with a different angle's multiplier, prove a nonlinear long graph
exists, or close the infinite body/head/high system. Its role is
to provide the exact real coordinate and weak boundary interface
for those continuing arguments.
