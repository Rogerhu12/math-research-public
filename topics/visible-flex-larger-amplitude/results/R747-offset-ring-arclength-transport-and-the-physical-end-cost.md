# R747 — Exact offset-ring arclength transport on the axial closed sphere

2026-11-28. We give a full second material atlas and phase map for the physically moving images of [R746](R746-circular-grip-periodic-translation-and-physically-free-closed-ends.md). The initial metric is the same in both maps in the same material coordinates. For an undeformed rolled annulus the new map pays the **entire angular metric row** at every angle and time. The other two entries are determined by one explicit turning difference. On the genuine circular meridional panels of both rolled ends all three entries are paid exactly, down to a short open collar inside each filling cap. Independent cap motion still gives positive Euclidean-quotient distance without markers. The complete noncircular ends still need a physical solve.

The [full physical two-jet source](../scripts/resume_20261126/r747_offset_arclength_closed_two_jets.py) includes the original R746 phase map on this same atlas. Its two entries can be used with identical phase samples, material target, and allowed three-dimensional displacements.

## 1. The exact shift at every transverse level

For the original periodic planar R744 section let \(P\) be the period, \(n'=\kappa T,\ T'=-\kappa n\). Lift its clockwise tangent angle to \(\Theta(s)\in\mathbb R\), \(\Theta(0)=0\) at the upper-pointing left-wall equator. The upper profile has \(0\le\Theta\le\pi\); reflection gives \(\Theta(s)=2\pi-\Theta(P-s)\) on the lower profile and \(\Theta(s+P)=\Theta(s)+2\pi\). In particular \(\Theta'=\kappa\). Inward offset distance \(d\) gives \(\Gamma_d(s)=\Gamma(s)-dn(s)\) with derivative \(A(s,d)T(s)\), \(A=1-d\kappa\). Write
\[
 \Omega_d(s)=s-d\Theta(s),\qquad
 \Omega_d(S)=\Omega_d(s)+\theta(r-d),\qquad r=.15,\quad 0\le\theta\le\pi/2 .
 \tag{1}
\]
We use (1) through both entire end annuli, with \(d=d(v)\) the original R744 transverse offset. Since \(0\le d\le.1085,\ \kappa\le1/.15\), \(\Omega_d\) is a strictly increasing diffeomorphism of the real line, with \(\Omega_d(s+P)-\Omega_d(s)=P-2\pi d>0\). Thus (1) gives a smooth periodic relabeling with a well-defined lift. At \(d=0\) it is exactly the R746 cylinder action \(s+r\theta\). The geometry of the named images and the eccentric spatial rotation \(B_\theta\) remain the R746 ones.

Differentiate (1) on the annulus and let \(e=\Theta(S)-\Theta(s)-\theta\). Then
\[
 A(S,d)S_s=A(s,d),\qquad A(S,d)S_v=d'(v)e.
 \tag{2}
\]
For zero physical height perturbation there the pulled-back metric is exactly
\[
 g_{ss}=A(s,d)^2,\qquad g_{sv}=A(s,d)d'e,\qquad
 g_{vv}=1+(d'e)^2.                                                   \tag{3}
\]
Indeed the two derivative vectors before spatial rotation are \(A(s,d)T(S)\) and \(d'eT(S)-d'n(S)+\sigma p'e_y\), where physical \(p'^2+d'^2=1\). These formulas apply on the full continuum, not just along the meridians or at the endpoint phase. Where both \(s\) and \(s+r\theta\) and their intervening arc lie in the true constant-radius right circle, (1) gives \(S=s+r\theta,\ e=0\). The spatial rotation cancels this shift exactly for every inward offset there. Both entire rolled meridional panels over the R746 grip angles are consequently stationary.

For the fully named R746 physical roll at a nonzero amplitude, put
\[
 D=\lambda_\sigma\sin\theta\,[4(p/p_b)(1-p/p_b)]^4G(\Gamma_d(S)),\qquad
 G(x,z)=1+.20x+.10z .
\]
The three entries in (3) then acquire respectively \(D_s^2,\ D_s(p'+D_v),\ 2p'D_v+D_v^2\). The source offers the original nonzero modes on both ends and both caps, and a second choice with only the two cap modes. The latter retains the actual cap volume difference and realizes (3) exactly on both rolled ends. The freely changeable physical field can move both ends, the shared rims, and both caps. For example, on a long flat material arc with \(s,S\) in the same straight segment, \(e=-\theta\). Near the cap rim this can leave a mixed entry close to \(-\theta\). Equation (3) by itself is not an isometry of the whole annulus.

## 2. A single cap atlas for both phase maps

Denote the original terminal offset by \(d_b\), the old star center by \(c_2=(.595,0)\), and put \(w=0\) on the cap rim and \(w=1\) at the cap center. Let \(j(0)=0\). Its derivative is 1 up to \(w=.00025\), then decreases to zero as \(1-S_5((w-.00025)/.0005)\) over length .0005 and stays zero. Thus \(j(1)=.0005=:J_*\). Define
\[
 d=d_b+j(w),\qquad \rho=1-\frac{w-j(w)}{1-J_*},\qquad
 C(s,w)=c_2+\rho(w)(\Gamma_d(s)-c_2).
 \tag{4}
\]
Every unscaled ring is a simple star curve as in R744 §2 because \(d\le.109<.110\). At fixed polar direction its radius \(R(d)\) satisfies \(R'(d)=-1/(n\cdot e_{\rm polar})<0\). The scaled physical radius is \(\rho R\), with derivative \(\rho'R+\rho R'd'\) strictly negative away from the center: \(d'=j'\ge0,\ \rho'=-(1-j')/(1-J_*)\le0\) and these cannot both vanish. Thus (4) covers the complete terminal star disk once, is regular on the punctured disk, and its regular central Cartesian chart is available. This foliation changes material coordinates only.

On each cap solve instead
\[
 \Omega_d(S)=\Omega_d(s)+\theta(r-d)\omega(w),\qquad
 \omega=1-S_7((w-.25)/.50)
 \tag{5}
\]
with the smoothstep clamped to 0 and 1 outside its unit interval. Evaluate the cap at \(C(S,w)\), then add its R746 physical graph and rotate. Up to \(w=.00025\), \(j=w,\ \rho=1,\omega=1\), so (5) is literally the same offset-arclength shift as (1). At the common seam the end arclength has \(d'=1,\ d''=0,\ p'=p''=0\). The two physical jets agree with the cap normal coordinate \(w\) there, including mixed derivatives. The named end height and its two derivatives vanish on that seam, and the actual cap bump vanishes on a neighborhood of the rim. On the true circular panel the cap's inner normal collar is also fixed for the cap-only design.

For \(w>.75\) we have \(S=s\), so (4) just selects the original physical plane point and the angular action is identically absent. The plane Cartesian chart covers this open scaled star disk, including its polar origin. This removes any requirement that a nontrivial angular map be differentiable at a polar center. Away from that disk the two cap charts with \(u=s,\ v=1-w\) cover all points. The legacy entry uses \(S=s\) on the same entire cap foliation and the original R746 cutoff in the rolls. At phase zero the two maps, and all their material derivatives, coincide everywhere. Both maps cover the *same entire physical image at each phase* for the same chosen modes because each leaf map is a bijection. Thus all R746 image estimates apply unchanged, also for cap-only: reach \(\ge.107\), \(D<3.40\) initially, all phase diameters \(<3.403\), held distance \(\ge1.521\), fixed grip diameter \(\ge1.40\), and \(\delta_{\rm E}>0\). The cap volume increase alone is sufficient in both cases.

## 3. What must change in a true end solve

Suppose, in the pre-rotation frame, an exact end with target \(dv^2+A(s,d(v))^2ds^2\) had every material circle in one of the parallel planes \(y=Y(v)\). Write its planar part \(Q(s,v)\). The \(ss\) and \(sv\) rows give \(Q_s=AT\), \(Q_v=b(s,v)n\). The \(vv\) row makes \(|b|=\sqrt{1-Y'^2}\) independent of \(s\). For \(0<v<L\), \(d'>0\); \(b\) cannot vanish identically because \(A_v=-d'\kappa\) does not vanish identically. Hence its sign too is constant on the circle. Writing \(n_s=A k_v T\) for the signed curvature of that planar level gives \(A_v=b A k_v\). Each actual simple level near the original boundary has the same turning number as the original section. Integration in \(s\) therefore gives \(b=-d'\). It follows \(T_v=0\) and \(\kappa(s)=A k_v\), so the limiting entrance curvature must be the original material \(\kappa(s)\). The R746 action instead supplies \(\kappa(s+r\theta)\). A phase moving a curved entrance segment to a straight segment fails this necessary condition. The physical end and material surfaces in a free solve can leave the parallel-plane ansatz.

There is also a one-sided regularity constraint independent of the planar-slice ansatz. At \(\theta=\pi/2\) take \(s\) close to the point on the upper right true circle of turn angle \(\pi-.5\). Here the initial material \(\kappa(s)=1/.15>0\) on an open interval, but \(s+r\theta\) and a neighborhood are in the true straight right wall. Indeed the arclength beyond the completed right turn is \(r(\theta-.5)-.0005\), positive and strictly below the right wall length. In a fixed physical orthonormal frame the full locked cylinder has exactly the flat two-jet of the plane \((s,v,0)\) at this edge, up to origin and orientation. The prescribed target curvature on the incoming roll is
\[
 K=\frac{\kappa(s)d''(v)}{1-d(v)\kappa(s)},\qquad
 d(v)=d_5v^5+O(v^6),\quad d_5=\frac1{2(.108)(.0005)^3}.
 \tag{6}
\]
Indeed its initial curvature ramp is \(S_5(v/.0005)/.108\), the derivative of the end turning angle. Thus \(K/v^3\to20 d_5\kappa(s)>0\).

If the physical end were \(C^4\) one-sided up to this edge and joined the locked flat cylinder \(C^2\), then \(F_{ss}=F_{ssv}=F_{ssvv}=0\) there: differentiate in \(s\) the entire flat entrance first and second transverse jets. Taylor expansion now gives \(F_{ss}=o(v^2),\ F_{vv}=O(v),\ F_{sv}=O(v^2)\). The denominator \(\det g\) tends to 1, so the Gauss equation would give \(K=o(v^3)\), contradicting (6). This does not exclude a \(C^2\) solution. One may also physically free the central cylinder outside the swept grip so its entrance has different second jets.

For a constructive \(C^2\) comparison in those actual flat coordinates use
\[
 (s+U(s)v^5,\quad v+V(s)v^4,\quad h(s)v^{5/2}),\qquad
 V=-25h^2/32,\qquad U=-3hh'/16 .
 \tag{7}
\]
Every second jet at zero joins the flat cylinder. Direct multiplication cancels the order-three term of \(g_{vv}\) and the order-four term of \(g_{sv}\). The order-five term of \(g_{ss}\) is \((5(h')^2-3hh'')/8\), equal to the target \(-2d_5\kappa\) if
\[
                     3hh''-5(h')^2=16d_5\kappa(s).
\]
For a finite closed subinterval of the positive true curvature arc take \(Z=h^{-2/3}\), obtaining \(Z''=-(32/9)d_5\kappa Z^4\). At the interval midpoint choose \(Z=a>0,\ Z'=0\). If the maximum distance to either endpoint is \(b\), choose \(a\) small enough that \((16/9)d_5\max\kappa\,a^4 b^2<a/2\). Up to first exit from \([a/2,a]\), integration gives \(Z\ge a-(16/9)d_5\max\kappa\,a^4b^2>a/2\); concavity prevents exit above \(a\) on either side. This defines finite \(h\) throughout that subinterval. The actual \(d_5\) is large. Neither (7) nor this existence argument supplies a specified reach margin on a specified positive-width end strip. They pay the leading metric terms, and motivate a nonlinear \(C^2\) continuation with the same fixed target.

The source differentiates the unique lifted inverse twice by its implicit equation. Its default returns the world-frame two-jet; passing rotate=False returns the true pre-rotation two-jet on all patches. Both entry points allow a seam-compatible true three-component physical correction. The expenditure in (3), the finite cap metric change, and the matching problem across the whole closed surface all remain explicit.
