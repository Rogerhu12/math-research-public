# R752. A closed-cap shortcut, its quantitative obstruction, and a new full-body metric that pays every central chord

Let \(r=.15,\ H=.17,\ r_y=.108,\ \epsilon_y=.0005\), with the planar unit-speed profile \(q(s)=\Gamma(s)\), signed curvature \(k\), exterior normal \(n\), and period \(P\) of R744. The spatial axial rotation and true circular grip are those of R746. A common ambient rotation drops out of all chord estimates. The physical phase is \(0\le\phi\le\pi/2\). The old R746 central material goes from \(q(s)\) to \(q(s+h)\), \(h=r\phi\). No assumption on the shape of either deformed end is needed for the first theorem.

**Theorem.** On the original R746 phase-zero metric, a pair of prescribed central points alone forces the maximum finite relative Gram error above \(1.01\) at the last phase. Every exact end continuation would require at least one of those two central points to change by more than \(.194\). A different, explicitly generated initial metric below has the opposite global property: for each phase, the assigned map of its entire central cylinder into space is 1-Lipschitz for the path distance of the **whole closed** initial body. This includes arbitrary paths through one or both filled caps. The new reference gives a continuous \(C^2\) family, an extended pointwise grip, held \(>1.521\), positive rigid-quotient distance, and all-phase reach \(>.105>.03D\). Its legacy phase fixes the complete central and both cap tensors. The two rolled annuli still have an actual finite metric defect. The global chord result is a necessary compatibility property, not existence of an isometric filling.

[Complete delayed-turn two-jet generator](../scripts/resume_20261126/r752_delayed_turn_closed_two_jets.py), based on [R744](R744-closed-extruded-bent-disk-global-reach-and-curvature-gap.md), R746–R748. All scalar constants below define continuum curves. The generator implements arclength inversion and the two turn integrals.

## 1. An intrinsic rectangle crosses a whole original cap

The two central profile sheets over \(-1<x<.30\) are \(z=\pm H\). At their positive transverse seam \(y=1\), use the same physical abscissa \(x\) to label each sheet. The arclength orientation on the upper one is \(+e_x\), and on the lower one is \(-e_x\). The inwardly rounded planar offset at distance \(d\) has upper/lower heights \(\pm(H-d)\) on these two straight intervals. On \(x\in[-.75,.05]\) the complete vertical segment between these heights on the terminal cap lies inside its planar domain. Indeed the section at \(x=0\) between them belongs to the enclosed cross-section, and throughout this rectangle there are no other boundary segments: the left wall/turn lie at \(x\le-1\) before offset and \(x\le-1+.1085<-.75\) after offset. The right main bend starts at \(x=.30\), and right turn/wall have \(x>.4\) before offset. Offsetting by at most .1085 keeps them to the right of .05. The two flat horizontal pieces are regular, transverse intersections with each vertical line. Jordan separation gives the asserted closed segment including both endpoints.

Unwrap the upper roll there, then the planar cap strip, then the lower roll. At each end the roll has unit \(v\)-speed, orthogonal to \(e_x\); cap \(z\)-distance is ordinary Euclidean distance. This is a single isometric material rectangle with coordinates \(x\) and transverse length coordinate \(w\), from \(w=0\) at the upper seam to
\[
 \ell=2L_0+2(H-d_b),\qquad L_0=r_y\pi/2+\epsilon_y
\]
at the lower seam. Here \(d_b\ge r_y\): the old turning arclength measure equals \(r_y\,d\alpha\) plus a nonnegative measure, and \(d_b=\int\sin\alpha\,dv\). Consequently \(\ell<.465\). In particular a diagonal is a genuine admissible closed-surface path even if a still shorter one exists elsewhere.

Take the two material points on \(y=1\) with \(x_+=.05,\ x_-=-.75\). The diagonal length is \(l=\sqrt{.8^2+\ell^2}<.926\). At the last phase their unrotated endpoints still lie in the flat parts, since \(.05+.15\pi/2<.30\) and \(-.75-.15\pi/2>-1\). Their Euclidean chord has length
\[
 L_*=\sqrt{(.8+.15\pi)^2+.34^2}>1.315 .
\]
If \(F^*e\le(1+\delta)g_0\) on this path, \(L_*\le\sqrt{1+\delta}\,l\). Hence \(\delta>(1.315/.926)^2-1>1.01\). This also applies to any full relative spectral Gram norm which bounds all directions. If both specified spatial endpoints are changed by at most \(b\), the necessary exact inequality is \(L_*-2b\le l\), giving \(b>(1.315-.926)/2>.194\). Common rigid postcomposition has no effect. This excludes every possible end shape with those central endpoint values; it places no such restriction on unconstrained new central curves that actually move the required distance. A single-cap computation is sufficient and uses no regularity beyond the path length comparison.

## 2. A new closed initial body with a longer low-angle shoulder

Keep the same \(\Gamma\), set the transverse half-width to \(Y=.37\), and change both end curves. Let \(v_0\in[0,L_0]\) be the true R744 turn coordinate and \(\alpha=\alpha_0(v_0)\) its angle. With \(b=1/1024,\ e=.81\) set
\[
 C(\alpha)=1-(1-\min(\alpha/b,1))^4,\qquad
 v=v_0+e C(\alpha),\qquad L=L_0+e.
\]
The increasing coordinate has \(dv/dv_0\ge1\); its third derivatives match where the density becomes zero. Its inverse defines \(\alpha(v)\), still nondecreasing from 0 to \(\pi/2\), with \(\alpha'(0)=\alpha'(L)=0\) and \(|\alpha'|\le1/.108\). The arclength offsets are \(p(v)=\int_0^v\cos\alpha,\ d(v)=\int_0^v\sin\alpha\). On either roll use
\[
 (q(s)-d(v)n(s),\quad y=\pm(Y+p(v))).
\]
The added density is nonnegative and supported at \(0\le\alpha\le b\); in particular
\[
 p_b\le .1085+.81=.9185,\qquad
 d(v)\le .108(1-\cos\alpha)+.0005+.81/1024,\quad d_b<.10930.
\]
For the cap leaves of R747, the *additional* inward offset has maximum \({\rm JOIN}+{\rm RAMP}/2=.0005\), so even this extended collar has total offset \(<.10980<.110\). Its exact maximum follows from the symmetric cutoff and parameters in the R747 source. R744 gives \((q-c_2)\cdot n\ge.110,\ c_2=(.595,0)\). Every required offset is regular and strictly star-shaped by its positive support and degree one; nesting follows by differentiating its radius on a fixed ray, \(\partial_d \rho=-1/(n\cdot e_{\rm ray})<0\). The two filled planar end disks and normal collars are genuine, and the opposite transverse signs give disjoint ends. The new \(\alpha'\) vanishes at both joins and its next derivatives there allow the original \(C^3\) extension (the original curvature ramp vanishes to third order). The initial body is a closed embedded \(C^3\) sphere.

The roll support about \((c_2,0)\) is bounded below by \(.110\cos\alpha+Y\sin\alpha\ge.110\), since
\[
 p(v)\sin\alpha(v)-d(v)\cos\alpha(v)
 =\int_0^v\sin(\alpha(v)-\alpha(w))\,dw\ge0.
\]
The two absolute principal curvatures are \(|\alpha'|\) and \(|k\cos\alpha/(1-dk)|\). If \(k<0\), the latter is \(\le6.91\). If \(k>0\), \(k\le1/.15\), and the bound for \(d\) gives
\[
 {k\cos\alpha\over1-dk}\le
 {\cos\alpha\over .15-.108(1-\cos\alpha)-.0005-.81/1024}
 \le {1\over .15-.0005-.81/1024} <6.75 .
\]
The central and cap bounds are inherited from their actual planar or extruded geometry. R723-A therefore yields whole two-sided reach at least .108 for the initial reference. Every planar projection, including the caps, lies inside the original cross-section by the nesting just proved. Its boundary has planar norm \(<1.17\) by R744, hence so does the entire bounded section. All \(|y|\le1.2885\) and
\[
 D=\operatorname{diam}F_0(M)<2\sqrt{1.17^2+1.2885^2}<3.49 .
\]

## 3. Every central chord is compatible with the closed distance

Write \(d_0=|q(a)-q(a')|\le2.34\) and \(d_h=|q(a+h)-q(a'+h)|\). The shifted central map is locally exactly isometric on the entire cylinder. Consider an arbitrary rectifiable excursion starting and ending on the same transverse bounding circle, with those two arclength coordinates. A connected excursion into one end has both endpoints on that end's bounding circle. Ignore any common final spatial rotation.

Let \(v_*\) denote the unique location of \(\alpha=3b/5\). Since \(v_0\le .108\alpha+.0005\) on the original turn, one has \(v_*<.82\). If an excursion stays in \(v\le v_*\), throughout that region
\[
 {d\alpha\over dv}
 ={\alpha'_0\over1+e C'(\alpha)\alpha'_0}
 \le {b\over 4e(2/5)^3}<.0048,\qquad
 d(v)\le .0024 v^2 .
\]
The initial end metric is \(dv^2+(1-d(v)k(s))^2ds^2\). R744 gives \(4<P<8\) directly from its two length-2 main arcs, its two quarter-turns, two half-turns and wall lengths (each half has a left wall \(<.021\) and a right wall \(<.795\)). Put \(\omega=2\pi/P\). We have \(\omega v_*<\pi/2\) and
\[
 1-dk\ge1-.016v^2\ge\cos(\omega v),
\]
using \(1-\cos t\ge2t^2/\pi^2\) and \(\omega>\pi/4\). Mapping \((s,v)\) to latitude \(\omega v\), longitude \(\omega s\) on the sphere of radius \(1/\omega\) is a globally defined length-decreasing comparison. Its boundary equatorial distance is the shorter periodic arclength between \(a\) and \(a'\), which bounds \(d_h\) from above for every shift \(h\). Thus the true shallow excursion has length at least \(d_h\).

Any deeper excursion, including every one reaching the filled cap, must reach transverse displacement
\[
 p(v_*)\ge .81[1-(2/5)^4]\cos b>.789 .
\]
The total variation of its physical \(y\) on the initial surface is at least \(2p(v_*)\), while total planar variation is at least \(d_0\). The integral triangle inequality applied to \((|(xz)'|,|y'|)\) gives length at least \(\sqrt{d_0^2+4(.789)^2}\). For \(0\le h\le .15\pi/2\) and \(d_0\le2.34\), \(h d_0+h^2<.789^2\). Thus this lower bound exceeds \(d_0+2h\), and the latter bounds \(d_h\) by unit profile speed. This argument does not presume that the material path stays on a selected meridian or on a preferred side of the cap.

Consequently *every* end excursion pays its two shifted central endpoints. Concatenate these Euclidean chords with the images of the portions already in the central cylinder. For infinitely many excursions one may either approximate a rectifiable path by a piecewise smooth path transverse to the seam circles, with length and endpoints converging, or replace excursions on their disjoint open parameter intervals by straight segments at constant arclength-controlled speed. In the latter construction parametrize the original path by arclength; the central map is smooth and locally isometric, the replacements are continuous and have speed at most one. Absolute continuity follows also by first replacing the end map along the path using any smooth global extension of the central values and then modifying on those disjoint intervals: for intervals of length \(d_i\) both old and new variations are bounded by a fixed constant times \(d_i\), and \(\sum d_i\) is finite. The claimed whole path bound follows. Taking an infimum over all initial-surface curves proves
\[
 |F_\phi(P)-F_\phi(Q)|\le d_{g_{\rm new}}(P,Q)
 \quad \text{for every pair of central points and every }\phi.
\]
The conclusion concerns all ambient Euclidean chords with both endpoints prescribed in the central cylinder. It does not provide a global short extension to the caps or an isometric embedding theorem.

## 4. All phases of the named new reference

Use the R746 axial phase on the central cylinder and the true new ends, with the cutoff \(1-S_7(v/L)\). The new cap diagrams have angular label \(s\) in the legacy design, with density, radius and extra collar from the new \(d_b\). This gives a diffeomorphism of every section and an unrotated whole image equal to the new initial body. The optional R747 angular chart has the same zero-phase tensor but carries the usual separate cap-relabeling cost. Its inverse denominator \(1-dk>1-.10980/.15>.26\) pays the full new collar.

Apply the actual ambient bending (R748 (1)) with identical \(a=\sin\phi/4096\) and width .38, but fade from \(|y|=.37\) to .75. Rotate around the original right-circle axis only afterward. The bounds \(t=(.595-x)_+<1.8,\ \|DE\|<.004,\ \|D^2E\|<.10\) from R748 use only the planar projection and the width, so apply on this new convex hull. By its all-ordered-pair tangent-ball estimate the whole family has
\[
 \operatorname{reach}\ge .996^2/(1.004/.108+.10)>.105>.03D .
\]
The maps remain embedded and \(C^2\)-continuous. The transverse interval \(|y|\le .36\) on the R746 true circular sector supplies a pointwise fixed grip of diameter at least \(.72>.2D\). The upper original bound \(z<.945\) on the entire profile holds by R746 and nesting. The left-wall point at \(y=0\), \(x_L\le-1.149\), and the last whole image with \(x>.373\) give the same strict held \(>1.521\): the added bending leaves \(z\) unchanged before the quarter-turn. Both complete legacy cap tensors are exact by their unit-speed developed \(x\)-curve. At the initial phase the surface is \(C^3\); at the final phase the positive cap has the same non-\(C^3\) interior germ across \(x=.595\) as R748, giving positive optimized Euclidean distance by compactness of the relevant rigid maps. Undoing the quarter-turn gives \(\delta_E\le.000475\).

The two joining rolls retain free physical directions. For example take a material point in the middle of the straight right wall, at \(v=L/2,\ \phi=\pi/2\). The point and its advanced label both remain on this wall (length at least .74 and advance less than .12 here). Its unrotated abscissa is \(x_R-d\ge.729-.10930>.595\), so the ambient bending is identically zero there. The actual legacy parametrization has \(g_{sv}=-r\phi\,S_7'(1/2)/L\), whereas the new fixed tensor has \(g_{sv}=0\). A material short-path test alone could not have eliminated this shear. The complete row must be solved and refined on the same new tensor for all times. All-phase immersion, the improved complete material distance comparison and exact central/cap rows are distinct from the missing whole-roll equations and completion meshes.
