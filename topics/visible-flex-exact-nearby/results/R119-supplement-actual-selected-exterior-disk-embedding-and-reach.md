# R119 GHX: the actual selected exterior disk is embedded with a uniform reach bound

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved.** For every original admitted S/T parameter, the actual exact
selected tail, its same finite connector and its filled flat disk form
a $C^2$ isometric embedded material disk. With its one fixed placement
and height convention, it differs from the radial reference having
that same actual metric by less than $2^{-46000000}$ in physical $C^2$.

As a compact subset of physical space, including its actual boundary,
this entire exterior disk has
$$
                          \operatorname{reach}>1/3 .
 \tag{GHX.1}
$$
These are the original physical units. The statement is about this
piece with its boundary. It does not bound the reach of its union
with the core or another piece, prove the remaining attachment
equations, or replace the whole closed-surface geometry gate.
The reference metric is the actual one selected at the given gamma;
different gamma values are not thereby assigned a common metric.

## 1. Actual references and the completed physical input

Use:

- [GHW](R144-supplement-complete-physical-height-derivative-in-the-original-low-graph.md), especially its fixed-metric bound GHW.18 and whole-domain two-jet qualifications;
- [GHV](R144-supplement-actual-horizontal-coframe-and-low-graph-vector-two-jets.md), especially GHV.3--GHV.7, GHV.14--GHV.25 and its exact matched reconstruction;
- [the single-frame reconstruction](R119-supplement-positive-collar-principal-invariance-and-single-frame-reconstruction.md), including its actual flat-disk extension;
- [the fixed-stop installation Sobj](../notes/2026-11-14-R119-simple-root-fixed-stop-new-object-and-transfer-gates.md), with its actual $W/a,W_a$ bounds;
- [S/T](R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md), with the complete selected zero residual and original trace matching.

Fix one admitted gamma and its actual selected design parameters.
Let $W(a)$ be that actual metric slope, not an old radial proxy:
$$
              g_\gamma=(1+W^2)\,da^2+a^2d\theta^2 .
 \tag{GHX.2}
$$
The material domain is the same disk $D=\{|y|\le a_B\}$ of GHV,
in physical Cartesian material coordinates
$y=(a\cos\theta,a\sin\theta)$. Its flat part has the same
fixed radius $a_f>0$. Extend $W=0$ there as in the original
proved construction. All original interfaces and their jets remain.

Let $z_{\rm ref}$ be the radial positive height satisfying
$$
 (z_{\rm ref})_a=W,\qquad z_{\rm ref}(a_f)=0 .
$$
Choose the same global height $\lambda_0$ and the same planar
initial rotation and position as for the actual selected
reconstruction. With outer material point $y_0$, its reference is
$$
 F_0(y)=
 \big(X_0+R_{\alpha_0}(y-y_0),\,z_{\rm ref}(|y|)+\lambda_0\big).
 \tag{GHX.3}
$$
Use the actual northern sign instead in the vertical component
when that is the stated physical convention. Apply the same fixed
orthogonal placement and translation to both surfaces if working
in world coordinates. Such a common placement leaves all the
Euclidean bounds below unchanged.

This comparison does not reset height or frame at an internal
interface or at the flat end. In particular it does not subtract
an independently chosen mean-height span.

GHV.4, from the complete fixed-metric part of GHW.18 and the
actual selected state bound, gives for the full height
$$
             e=z-z_{\rm ref}-\lambda_0,\qquad
             \|e\|_{C^2(D)}<E_z:=2^{708}R,\quad
                            R=2^{-47000000}.
 \tag{GHX.4}
$$
It contains both the nonmean field and the true mean correction.
The bound is in actual physical Cartesian derivatives and holds
on the entire finite connector and every infinite-tail layer.
The genuine zero residual and matching make it a global $C^2$
bound, not just a norm of broken representatives.

Sobj's actual installed inequalities, already consumed in GHV,
are
$$
                     |W_a|<2,\qquad W/a<1/3,\qquad W<1/8.
 \tag{GHX.5}
$$
Hence $\|DF_0\|<2$ and $\|D^2F_0\|<2$ in Euclidean operator norms.
The latter follows directly because the planar part is affine
and the radial height Hessian has eigenvalues $W_a,W/a$.
The fixed reference is a $C^2$ graph across the flat-disk boundary.

## 2. Actual uniform C2 distance to that same radial graph

For $0\le s\le1$ put
$$
 z_s=z_{\rm ref}+\lambda_0+s e,\qquad
 G_s=I+W^2 e_r e_r^{\mathsf T}-Dz_sDz_s^{\mathsf T}.
 \tag{GHX.6}
$$
These are algebraic intermediate metrics; no intermediate
Darboux equation is assumed. From (GHX.4)--(GHX.5), all of
them satisfy the matrix domain in GHV.7. The complete metric
variation has $\dot W=0$, and GHV.14 gives
$$
                    \|\partial_sG_s\|_{C^1}\le2^8 E_z.
 \tag{GHX.7}
$$
The direction includes its actual Hessian; no derivative of a
small value has been inferred.

Use GHV's full coframe and one-path formal vector readout
throughout this path, with the same initial phase, position
and height. Its estimate GHV.25 is a bound on the actual
algebraic matrix/height domain, so it applies to (GHX.6)
even though the intermediate formal jets need not be compatible:
$$
                \|\partial_s{\cal V}(G_s,z_s)\|_{\mathcal V^2}
                                                       \le2^{64}E_z.
 \tag{GHX.8}
$$
At $s=0$, $G_0=I$ and this readout is exactly the reference
(GHX.3). At $s=1$, it is exactly the actual matched selected
surface $F$, by GHV section 7. Integrating the formal readout
and then using the compatible endpoint identities proves
$$
 \|F-F_0\|_{C^2(D)}
       <2^{708+64-47000000}
       =2^{-46999228}<\varepsilon,\qquad
                         \varepsilon=2^{-46000000}.
 \tag{GHX.9}
$$
The vector norm is Euclidean in each Cartesian derivative,
as in GVC.4; it is dominated by GHV's component-sum readout.
This controls the value, both first derivatives and every
second derivative, including the flat-end and all original
matching jets. The proof does not transfer the old analytic
label bound to a new finite-Sobolev field.

## 3. Global injectivity on the whole material disk

Let $X$ denote the two horizontal components in the common
canonical frame. Equation (GHX.9) gives
$$
                   \|DX-R_{\alpha_0}\|_\infty<\varepsilon.
 \tag{GHX.10}
$$
The material disk is convex. For any $x,y\in D$, integrate
along its actual straight segment. Because $X$ is genuinely
globally $C^1$ there, including at the accumulation circle,
$$
 \begin{split}
 |X(y)-X(x)|
 &\ge|R_{\alpha_0}(y-x)|
     -|X(y)-X(x)-R_{\alpha_0}(y-x)|\\
 &\ge(1-\varepsilon)|y-x|.
 \end{split}
 \tag{GHX.11}
$$
Thus $F$ is globally injective on this disk. Its already
proved exact first fundamental form (GHX.2) is positive,
so it is an immersion. Continuity and compactness make
the injection a homeomorphism onto its image. Hence
$F:D\to\mathbb R^3$ is a genuine $C^2$ isometric embedding
of the material disk, with its boundary retained.

No separate annular path factor is needed after the actual
flat-disk filling: the segment used in (GHX.11) stays in the
same material disk. Neither a complex-angle chart nor an
unmatched off-shell extension is used for this argument.

## 4. A complete reach lemma including the boundary

Here is the elementary estimate needed for the entire
compact piece, rather than just a local curvature bound.

**Lemma.** Let $K\subset\mathbb R^d$ be compact and convex.
Suppose a $C^2$ map $F$ on $K$, with its actual one-sided
boundary jets, satisfies
$$
 |F(y)-F(x)|\ge c|y-x|,\qquad
                        \|D^2F\|\le L,\qquad c,L>0 .
 \tag{GHX.12}
$$
Then the reach of the closed set $F(K)$ is at least $c^2/L$.

**Proof.** Every ambient point has a nearest point in $F(K)$.
Suppose an ambient point $p$ has two distinct nearest points
$F(x),F(y)$ at the same distance $r$. Injectivity from the
first inequality ensures $x\ne y$.

Convexity makes $x+s(y-x)$ feasible for $0\le s\le1$.
The actual one-sided derivative of the squared distance
at the minimum $s=0$ gives
$$
                  \langle p-F(x),DF(x)(y-x)\rangle\le0 .
 \tag{GHX.13}
$$
Taylor's integral formula along that same segment gives
$$
 F(y)-F(x)=DF(x)(y-x)+R_{xy},\qquad
                           |R_{xy}|\le\tfrac L2|y-x|^2 .
$$
Equality of the two nearest distances gives
$$
 \tfrac12|F(y)-F(x)|^2
       =\langle p-F(x),F(y)-F(x)\rangle
       \le r\,\tfrac L2|y-x|^2 .
$$
Using (GHX.12) and $x\ne y$ implies $r\ge c^2/L$.
Therefore every point at distance less than $c^2/L$ has
a unique nearest point in $F(K)$, proving the lemma.
No assumption that a nearest point lies in the interior
has been used. This is why the actual boundary is included.

Apply the lemma with the same material disk,
$$
                         c=1-\varepsilon,\qquad L=2+\varepsilon.
$$
Equations (GHX.5), (GHX.9) and (GHX.11) supply its two
hypotheses. Since $\varepsilon<1/8$,
$$
 \operatorname{reach}F(D)
 \ge\frac{(1-\varepsilon)^2}{2+\varepsilon}
 >\frac{(7/8)^2}{17/8}
 =\frac{49}{136}>\frac13 .
 \tag{GHX.14}
$$
This proves (GHX.1) in the original physical coordinates.
It is a nearest-point uniqueness estimate for the whole
piece, not a conclusion drawn solely from its principal
curvatures.

## 5. Actual normal and curvature comparison

Choose the consistent material orientation for both
surfaces. Let $n,n_0$ be their unit normals. Their tangent
cross products differ by at most
$$
        4\varepsilon+\varepsilon^2<5\varepsilon .
$$
Indeed each reference tangent column has norm below2,
and each column difference is bounded by (GHX.9).
Both exact surfaces induce the same metric (GHX.2), so
both cross-product norms are $\sqrt{\det g_\gamma}\ge1$.
Normalization therefore gives
$$
                           |n-n_0|<16\varepsilon .
 \tag{GHX.15}
$$
A common reflected world placement changes both orientation
conventions consistently and leaves this difference norm
unchanged.

Let $\mathrm{II},\mathrm{II}_0$ be their second forms, identified
on the same material tangent space. The exact difference is
$$
 (\mathrm{II}-\mathrm{II}_0)(v,w)
   =\langle(D^2F-D^2F_0)(v,w),n\rangle
                   +\langle D^2F_0(v,w),n-n_0\rangle .
$$
For Euclidean unit material directions it is bounded by
$(1+2\cdot16)\varepsilon<64\varepsilon$.
Since the common metric has $g_\gamma\ge I$, the same bound
holds on its unit tangent directions:
$$
                    \|\mathrm{II}-\mathrm{II}_0\|_{g_\gamma}
                                                    <64\varepsilon .
 \tag{GHX.16}
$$
Thus the value, normals and curvatures in this comparison
are all controlled on the actual entire selected piece.

## 6. Geometry scope and new exact combinations

The radial reference in this theorem uses the actual selected
$W$ at the current gamma, including both true design parameters.
It has the same global height and placement as the actual
comparison. The theorem does not compare arbitrary different
world anchors or replace a nonzero mean-height span by zero.

Reach does not pass from two pieces separately to their union
without the true attachment and cross-piece separation bounds.
The rest of the core, the other cap, waist reflection and
the final connected closed surface retain those obligations.
In particular (GHX.14) is not the final ratio
$\operatorname{reach}/D$ for that unconstructed union.

The companion
[fourfold_codazzi_selected_exterior_geometry_saved_bounds.py](../scripts/fourfold_codazzi_selected_exterior_geometry_saved_bounds.py)
records four new exact integer/rational combinations.
Their first code-mode evaluation passed. Its Python text
preserves the operations without claiming a local execution.
No previous geometry carrier, label construction, profile,
numerical array, integral or scientific target was rerun.
