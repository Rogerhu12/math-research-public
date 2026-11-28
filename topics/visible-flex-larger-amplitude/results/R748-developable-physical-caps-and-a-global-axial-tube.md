# R748. An exactly developable physical bend of each flat cap with noncongruent endpoints

The unmarked axial-translation body of R746 admits a different end design. Both entire physical caps are developable for every phase. In the R746 material action pulled back to the common R747 atlas they induce **exactly their single initial metric at every phase**, even though they physically bend. The connected closed \(C^2\) embeddings have reach \(>.105\), initial diameter \(D<3.40\), grip diameter \(\ge1.40\), and held displacement \(>1.521\). The unmarked endpoint images are not congruent. The inverse endpoint rotation gives \(\delta_{\rm E}<.000475\) for the named field. The remaining fixed-metric costs on the moving cylinder strips and the two rolled ends are not removed by this theorem.

[The complete six-jet source](../scripts/resume_20261126/r748_developable_axial_caps.py) evaluates both the original cutoff material phase and the offset-arclength phase of R747 on the same closed charts. It returns either world-space jets or jets before the known rigid rotation.

## 1. Actual ambient deformation and cap metric

Use the exact R744 unmarked reference with no curvature-changing normal correction. The R746 circle axis, periodic profile and full cylinder, rolled heads and planar end disks are used unchanged at the initial phase. At a phase \(\phi\in[0,\pi/2]\), first take the R746 zero-end-modes material action. Its unrotated image is the whole same closed reference. On the optional R747 offset-arclength charts its alternative material action also keeps that same unrotated image, by the degree-one leaf diffeomorphisms and filled-cap construction there. Denote the ultimate R746 ambient rotation around the physical \(y\)-axis through \(O\) by \(B_\phi\).

For \(x_* = .595,\ a=\sin\phi/4096,\ t=(x_*-x)_+\), define
\[
 d(x)=\int_0^t [1-\cos(a r^2)]\,dr,\qquad
 h(x)=\int_0^t\sin(a r^2)\,dr .
\]
With \(\lambda(y)=S_7((|y|-.71)/.38)\), using the clamped smooth step, apply the **actual spatial map**
\[
 T_\phi(x,y,z)=\big(x+\lambda(y)d(x),\,y+\operatorname{sgn}(y)\lambda(y)h(x),\,z\big) . \tag{1}
\]
It equals the identity on an open neighborhood of \(y=0\), and it is \(C^2\) on all space. Apply \(B_\phi\) only after (1). On both cap planes \(|y|=1+p_b\ge1.108\), where \(p_b\ge.108\) follows from the nonnegative turn remainder in R744, we have \(\lambda=1\). For \(x<x_*\), the developed arclength tangent in the \((x,y)\) plane of the positive cap is \((\cos(a t^2),-\sin(a t^2))\); on the negative cap the second sign reverses. At and beyond \(x_*\) the tangent is \((1,0)\). It is unit everywhere and orthogonal to the \(z\)-tangent. Thus the entire developed cap metric in its original planar coordinates is exactly \(dx^2+dz^2\). In the legacy material action those planar cap coordinates are the same functions of the material at every phase. Its complete cap tensor is therefore fixed, including the regular Cartesian cap center and all actual seams. For the R747 offset-arclength material phase the same cap bending preserves the metric of its unbent transported planar cap; any angle-dependent relabeling cost remains to be paid separately. All designs at \(\phi=0\) give the same material tensor on the R747 atlas.

The upper and lower rolls, caps and middle cylinder are acted upon by one common \(T_\phi\); their actual first and second jets agree in the same overlap charts. The original unmarked image is \(C^3\) by R744. Its material phase maps are at least \(C^2\), and (1) and both derivatives are continuous in phase, including at zero. This gives the required \(C^2\) continuity of the named geometrical family.

## 2. A uniform complete tube

For a compact \(C^2\) embedded surface \(S\) of reach at least \(\rho\), suppose on its convex hull \(T=I+E\) has \(\|DE\|\le L<1,\ \|D^2E\|\le H\). Integrating the first derivative along straight chords gives
\[
 (1-L)|p-q|\le |T(p)-T(q)|\le(1+L)|p-q|.
\]
In particular \(T|_S\) is an injective immersion. At \(p\), projection on the transformed normal kills \(DT_p(T_pS)\). The initial two-sided tangent-ball inequality gives \(\operatorname{dist}(q-p,T_pS)\le |q-p|^2/(2\rho)\). Taylor's theorem along the chord bounds the transformed normal component by \(\big((1+L)/\rho+H\big)|q-p|^2/2\). The tangent-chord characterization of reach (Federer 4.18, as in R731) on the transformed compact surface yields
\[
 \operatorname{reach}(T(S))\ \ge\
 \frac{(1-L)^2}{(1+L)/\rho+H}. \tag{2}
\]
This is one global estimate for all ordered pairs.

R744 bounds the planar projection of the original boundary curve by norm \(<1.17\). Its inward offsets and filled cap projections lie inside the original section, by R744 §§2–3 and the strict nesting proved in R746 §3. Thus \(t<1.8\) on the convex hull. Write \(D=(d,\operatorname{sgn}(y)h,0)\) separately in the two nonzero cutoff slabs. The elementary chord bound \(2\sin(\beta/2)\le\beta\) for \(\beta=ar^2\) gives
\[
 |D|\le a\,1.8^3/3<.000475,\qquad
 |D_x|\le a\,1.8^2<.000792,\qquad |D_{xx}|\le2a\,1.8<.000879 .
\]
Here the first derivative is continuous through \(x=x_*\), and its derivative there is zero. The clamped step gives \(|\lambda'|\le (140/64)/.38<5.76,\ |\lambda''|\le(420/16)/.38^2<182\). Its first two derivatives vanish around the sign discontinuity. By the product rule, the displacement in (1) has differential norm \(<.000792+5.76(.000475)<.004\) and second differential norm \(<.000879+2(5.76)(.000792)+182(.000475)<.10\). Put \(\rho=.108\) from R744 into (2). At every phase, the full closed image is embedded and has reach at least
\[
 .996^2/(1.004/.108+.10)>.105>.03D.
\]
The initial diameter is \(D<3.40\) and every phase diameter is at most \(1.004D\).

## 3. Fixed extended grip, strong held and a quotient witness without markers

The material grip on the constant-curvature right cylinder sector of R746 has \(|y|\le.70\). The compensating axial translation and ambient rotation fix it, and (1) is exactly the identity on its entire swept physical sector because of this transverse bound. It has nonempty interior and diameter at least \(1.40>.2D\). The initial left-wall witness at \(y=0\) has \(x\le-1.149\). At \(\phi=\pi/2\) the spatial abscissa of any point after (1) and rotation is \(O_x+O_z-z>.373\) by R746 §4; (1) leaves \(z\) unchanged. Its distance to this entire endpoint therefore exceeds \(1.521\).

The original positive cap is planar on a neighborhood of its material center \((x_*,0)\) in the \(xz\)-plane. The center is interior because the final offset has strictly positive support and unit polar winding about this point. On this regular open chart at \(\phi=\pi/2\), \(h'= -\sin(a t^2)\), \(h''=2at\cos(a t^2)\) for \(x<x_*\); both vanish at \(x=x_*\), but the two one-sided derivatives of \(h''\) are \(-2a\) and \(0\). The horizontal developed coordinate \(x+d(x)\) has derivative one at the line and third derivative continuous there. Thus the actual cap image is a \(C^2\) graph with a nonzero normal third-derivative jump. It is not \(C^3\) in any neighborhood of that point. The initial closed image is \(C^3\). Euclidean congruence preserves this distinction. Compactness of the endpoint sets and boundedness of translations in any Hausdorff-aligning sequence now give \(\delta_{\rm E}>0\). Undoing just the endpoint rotation aligns the two unmarked reference images to within \(\|T_{\pi/2}-I\|_\infty<.000475\), proving the stated upper bound. This construction establishes positivity, not a large quotient-displacement lower bound.

There is a useful preservation condition for actual physical searches. Suppose a subsequent additive physical correction is \(C^3\) in the regular material coordinates near that one positive cap-center point and its first derivatives vanish there, with the initial shape unchanged. Then the jump in the third derivative of the terminal parameter curve across the material \(x_*\)-line is the same nonzero \(y\)-vector (transported by the rigid rotation). At the point it is normal to the corrected surface because the first jets agree. For clarity, if a \(C^3\) graph over this common tangent plane contained the corrected curve, compose the \(C^3\) graph with the planar projection of the curve. That projection is \(C^3\) across the line: before correction the horizontal jump is zero, and the correction is \(C^3\). The normal height would then be \(C^3\), a contradiction. Under this pointwise trace condition the terminal image stays noncongruent to the initial \(C^3\) surface whenever the complete candidates remain embedded. No assumption of zero curvature or no physical freedom on whole neighborhoods of either cap is required. Global thickness, held and a common metric of corrected fields require their own estimates.

For the named field, (1) starts moving physical cylinder strips already at \(|y|>.71\), and shears the rolled ends. Their first fundamental forms, any additional free physical corrections there, and refinement against the one frozen complete target remain outstanding. The favorable two caps and whole-image bounds alone do not complete the problem.
