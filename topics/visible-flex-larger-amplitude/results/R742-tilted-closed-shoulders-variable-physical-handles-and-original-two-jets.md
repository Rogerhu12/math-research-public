# R742 — Two tilted reflected closures, controllable physical shoulder turns, and complete unprojected spatial derivatives

2026-11-28. We give two finite, horizontally gripped, closed \(C^3\)-off-marks reference spheres for the finite bent disk of [R740](R740-finite-bent-disk-rolled-and-elliptic-closed-shoulders.md). The reflection plane is genuinely tilted. The full images are embedded at every phase, have \(D<2.64\), held displacement at least .557, grip diameter at least .60 and positive Euclidean-quotient separation. The tilt changes both the other disk and the shoulder. The original short interpolation in **each** design nevertheless has a principal curvature of magnitude greater than 20 on its left shoulder. We prove this directly and give actual geometric shape controls that preserve both full joining jets. Neither the base fields nor the softened variants have a demonstrated common whole-surface metric.

The [complete two-jet generator](../scripts/resume_20261126/r742_tilted_disk_two_jets.py) returns \(F,F_u,F_\theta,F_{uu},F_{u\theta},F_{\theta\theta}\) of the actual physical fields, with the original one-dimensional quadratures. There is no Fourier fit of the initial coordinates. [The public cost calculation](../scripts/resume_20261126/measure_r742_tilted_shoulders.py) evaluates actual first and second forms, signed sphere-center support and the two angular-invariance prices through the complete shoulder.

## 1. Complete geometry in the tilted plane frame

Keep \(h=.30,b=.26,e=1/8\), the actual smooth turning law \(\beta\), and its arc \(u_0(x),v_0(x)\) from R740. Keep the same turning segment A with \(R_b\in[1.09,1.091],\,t_b\in[.09,.091]\). Take the following physical parameters, with \(j=1.01,\ z_e=L=.006\) in both rows.

| Design | tilt \(\gamma\) | upper disk height \(H\) | ellipse shift \(c\) |
|---|---:|---:|---:|
| TILT32 | .32 | .32 | .16 |
| TILT44 | .44 | .37 | .19 |

The physical mirror is \(z=x_{\rm phys}\tan\gamma\). Use an orthonormal frame with planar coordinates \(X=x_{\rm phys}\cos\gamma+z\sin\gamma,\ Z=-x_{\rm phys}\sin\gamma+z\cos\gamma\), preserving \(Y=y\). The mirror is \(Z=0\). The arc in this frame is \(C(x)=(U,V)\), the transform of \((u_0(x),H+v_0(x))\). Write \(d=\beta(x)-\gamma\), \(T=(\cos d,\sin d)\), \(N=(\sin d,-\cos d)\). On A take \(x=R(s)\cos\theta,\ y=R(s)\sin\theta\), and planar point \(C(x)+t(s)N(x)\). This is exactly R740 A expressed around a shifted height and in a rotated frame. The physical disk is the actual unchanged cylindrical deformation \((u_0(x),y,H+v_0(x))\).

During B keep \(x=R_b\cos\theta,\ y=R_b\sin\theta\). Its entrance and exit planar points are \(Q_0=(X_0,Z_0)=C(x)+t_bN(x)\), \(Q_e=(jx+c,z_e)\). Use \(S=S_7(p)\) from R740, \(D_0=\int_0^p(1-S), E_0=p-D_0, G=D_0-S/2\). Initially put the physical handle \(\ell=L\), \(p=s_B/L\). The complete interpolation is
\[
 Q=Q_0+\ell D_0 N-\ell E_0 e_Z + S W,\qquad
 W=Q_e-Q_0-\tfrac{\ell}{2}(N-e_Z).                                      \tag{1}
\]
The residual from the straight convex combination of \(Q_0,Q_e\) is
\(\ell[G(p)N+G(1-p)e_Z]\). Indeed \(G(1-p)=S/2-E_0\). Both factors are nonnegative by the R740 polynomial factorization and their sum is \(D_0-E_0\le\min(p,1-p)\le1/2\).

From the endpoint ellipse at height \(z_e\) follow vertical lines in the **tilted frame** down to zero. Over the first half of this terminal wall use the R740 strictly increasing angle transition to normalized ellipse arclength; the remaining positive-width terminal collar has metric \(ds^2+(|\Gamma|/2\pi)^2d\theta^2\). The end geodesic is planar and noncircular. Reflection is \((X,y,Z)\mapsto(X,y,-Z)\) followed by transformation back to the original physical frame. The full reflection and phase rule is spatial vertical-axis rotation after this operation and a material angular shift. For the three R740 marks add their fixed height graph only on the physical upper grip. In particular the tilted lower disk is not a stationary marked grip.

## 2. Separation from the preceding disk and global injectivity of the interpolation

At every \(x\) we shall use the two strict margins
\[
 A_N=(Q_e-Q_0)\cdot N>\ell,\qquad Z_0-z_e>\ell .                         \tag{2}
\]
For the second margin \(Z_0'=(1+t_b\beta')\sin(\beta-\gamma)\). Its minimum is at \(\beta=\gamma\), on the constant-curvature part \(x=h+be/2+\gamma/\kappa_m<.382\), \(\kappa_m=\pi/[2b(1-e)]>6.89\). There \(Z_0\ge H\cos\gamma-.382\sin\gamma-t_b\). The two bounds exceed .08 and .079 respectively, so both exceed \(z_e+L\).

In the physical frame
\[
 A_N+t_b=[(jx+c)\cos\gamma-z_e\sin\gamma-u_0(x)]\sin\beta+
 [H+v_0(x)-(jx+c)\sin\gamma-z_e\cos\gamma]\cos\beta .                    \tag{3}
\]
For \(x\le h\) only the second bracket remains, and it exceeds .15 for both designs. For \(x\ge h+b\) only the first remains, bounded below by \([j(h+b)+c]\cos\gamma-z_e\sin\gamma-(h+b/\sqrt2)>.19\). In the bend use \(u_0\le x,v_0\ge0\), \(\sin .32<.315,\cos .32>.949,\sin .44<.427,\cos .44>.904\). The first bracket exceeds .125 for the first design and .119 for the second. For \(x\le.43\) the second exceeds .126 and .097 respectively, strictly greater than the largest possible \(t_b+L=.097\). For \(x\ge .43\) it exceeds .084 and .040 respectively. Here \(\beta\ge\pi/4\) and the minimum of \(a\sin\beta+b\cos\beta\) for positive \(a,b\) is at least \(\min(a,(a+b)/\sqrt2)\). These inequalities prove (2).

The planar curve \(C(x)\) turns monotonically by \(\pi/2\). Its tangent support implies \((C(x')-C(x))\cdot N(x)\le0\) for every ordered pair. Hence every earlier disk or A point, even with a different material abscissa, has planar displacement from \(Q_0(x)\) with nonpositive \(N(x)\)-component: \(0\le t\le t_b\) and \(N(x')\cdot N(x)\le1\). By (2), \(W\cdot N>0,\ -W\cdot e_Z>0\). Equation (1) moves strictly to the other side in the open portion and strictly decreases height. The terminal vertical path keeps that separating side since \(\cos d>0\). A itself is embedded: the whole planar map \(C(x)+tN(x)\) on \(t\ge0\) is injective as \(C(x)\) is the unique nearest curve point there. This follows by expanding squared distance using the preceding supporting inequality; distinct \(x'\) yield strict inequality. Its two coordinate derivatives are \((1+t\beta')T,N\), independent. The actual disk and A have the indicated regular polar/rim joins.

For constant \(\ell\),
\[
 Q_x=[(1-S)(1+t_b\beta')+\ell G\beta']T+Sj e_X,\qquad
 Q_p=\ell(1-S)N-\ell S e_Z+S'W.
\]
The determinant of the first vector and the second is strictly negative. In fact each of the two first-vector directions has negative determinant with \(N,-e_Z,W\), by (2) and \(\cos d>0\); zero coefficients do not remove all terms. Also \(Z_p<0\). At fixed \(Z\), the actual \(X\) increases strictly with \(x\) by implicit differentiation. If the set \(Z<Z_0(x)\) has a gap, interpolate by \(X_0(x)\) there: it is strictly increasing and agrees at its two ends. This proves injectivity of the entire planar interpolation, hence of the three-dimensional shoulder. The terminal wall has smaller height than all earlier B points. At \(\cos\theta=0\) the planar determinant ensures a regular chart, and otherwise the angular \(y\)-derivative is nonzero. The two reflected halves have opposite signed heights and a product seam. The disk rim and the other joins have the full matching two-jets of the construction. The unmarked field is \(C^3\); the three known mark rims are \(C^2\).

## 3. Physical handles independent of material width

The published SOFT32 and SOFT44 keep the **same** material radial lengths and join data as their respective base designs. Put
\[
 \ell(x)=L+\lambda S_7((-.20-x)/.55),\qquad 0\le\lambda\le .14,
\]
with the saturated step. The named soft designs have \(\lambda=.09\). To use (1) with unit material entrance and exit speeds, put \(t=s_B/L\) and use the increasing lifted angle
\[
 p(t,x)=\frac1\pi\arg\{\cos(\pi t)+i (L/\ell(x))\sin(\pi t)\},\quad 0\le t\le1.  \tag{4}
\]
Its values at the ends are 0 and 1. With \(a=L/\ell\), \(p_t=a/(\cos^2(\pi t)+a^2\sin^2(\pi t))\), and \(p_{tt}=0\) at both ends. Thus \(Q_s=N,-e_Z\) and \(Q_{ss}=0\) at the respective joins for *every* \(\lambda\); differentiation in \(\theta\) gives the full mixed jets. Changing \(\ell\) actually changes (1) as a plane curve. Changing only the material clock would not repair geometric curvature.

For \(x<-.20\) the disk is flat, \(jx+c<0\), and (3) gives \(A_N\ge H-z_e-t_b>.22\); also \(Z_0-z_e=(H-t_b)\cos\gamma-x\sin\gamma-z_e>.25\). Thus (2) still holds even for the largest physical handle .146. On this negative branch \(X\le\max(X_0,jx+c)<0\), since \(\sin d=-\sin\gamma\). At the paired positive abscissa \(x>.20\), \(X>.17\) from (1) in convex-combination form; its handle is unchanged. At each fixed \(y\) these are the only possible two branches. Within each, height strictly decreases; for \(|x|\le.20\) the earlier determinant applies. Their open parts are regular by the nonzero angular \(y\)-derivative, with the previous chart valid at \(x=0\). Separation from the disk and A still follows from (2). The initial geometric and embeddedness conclusions thus persist for this entire **physical** handle interval, without restricting the transverse handle derivative. For regularity of the unmarked *image*, use the smooth local surface chart with radial coordinate \(\ell(x)p\) at the entrance and \(\ell(x)(p-1)\) at the exit. In these charts (1) matches the adjacent straight tangent through third order. The chosen computational clock (4) is only required to join through second order; its third material derivative can differ by a tangential term. An optional independent pair of shape-control columns adds \(\lambda_X,\lambda_Z\) times the left weight and \(256p^4(1-p)^4\) in the two mirror-frame coordinates. These have zero through the second material derivative at both ends; the conclusions just proved concern the zero values of these additional columns.

## 4. Actual meridional defect and global geometry that survives it

For the two original constant \(L=.006\) designs take \(x=-R_b,\theta=\pi\); this lies in the physical symmetry plane \(y=0\). The initial meridional unit tangent has angle \(\gamma\) from downward vertical in the mirror frame, toward negative \(X\). At this left point
\[
 W_X=c-(H-t_b)\sin\gamma-(j-\cos\gamma)R_b+(L/2)\sin\gamma,\quad
 -W_Z=(H-t_b)\cos\gamma+R_b\sin\gamma-z_e-(L/2)(1+\cos\gamma).
\]
The given parameter ranges imply \(|W_X|<.055,\ .52<-W_Z<.74,\ |W|<.75\) in both cases (use also \(.314<\sin .32<.315,\ .425<\sin .44<.427,\cos .32<.950,\cos .44<.905\)). At \(p=1/8\), \(S'>.18\); from (1) the absolute horizontal-to-downward tangent ratio is at most \((L\sin\gamma/S'+.055)/.52<.135\). Its tilt from downward vertical is therefore \(<.135\). The total arc length from 0 to \(1/8\) is at most \(L/8+|W|S(1/8)<.0072\), since \(S(1/8)\le35/8^4\). The actual change of tangent angle is at least \(.32-.135=.185\). Consequently some planar curvature exceeds 20. The surface angular tangent on this symmetry line is parallel to \(e_y\), so this is genuine *normal* curvature of the surface. Since \(D\ge2\) at the two disk \(y\)-extrema, \(\operatorname{reach}\le1/20<.03D\). The original small-handle versions fail the required thickness even before enforcing isometry. This argument does not assert the same obstruction for (4) with \(\lambda>0\).

For completeness the tilted global distance margins are independent of that curvature failure. On the upper disk and A the original physical formulas give \(H+.565\) as a lower witness height at \(x=.995\), \(X_{\rm phys}\ge .43\). The norm on A and the disk is \(<1.28\): in the bend use \(R_b^2+2(.56)t_b+t_b^2+(H+b/\sqrt2)^2<1.62\); on the plateau maximize as in R740 with \(H\le.37,\ H-h-b+q<0\), and on the flat part use \(R_b^2+H^2\). The endpoint ellipse in its own frame has norm \(<1.30\). For the base handle (1) adds at most .003 to the greater endpoint norm. The only softened region has \(x<-.20\), where its A endpoint norm is \(\sqrt{R_b^2+(H-t_b)^2}<1.14\), and its ellipse endpoint norm is \(<1.12\) since \(2jxc<0\). Here the residual is at most \(.146/2\). Rotations and reflection in the plane through the origin preserve these norm bounds, as does the small marker addition within the grip. Thus \(D<2.64\) throughout.

On upper points with \(x\le h\), the physical vertical coordinates at the two B ends are \(H-t_b\) and \((jx+c)\sin\gamma+z_e\cos\gamma\le H-.10\). At \(x<-.20\) the handle residual is at most .073, and elsewhere at most .003. Thus the whole upper inactive sector stays below \(H+.001\) including marks. On \(x>h\) the two physical endpoint abscissas are at least \(h\) and \((jh+c)\cos\gamma-z_e\sin\gamma>h\). Its residual is at most .003 and the terminal line in the mirror frame only increases its physical abscissa as \(Z\) drops. For the comparison lower half-turn first undo that rotation on the upper witness: the signed distance of \((-u_0(.995),0,H+v_0(.995))\) from the original mirror is \(u_0(.995)\sin\gamma+(H+v_0(.995))\cos\gamma>.565\). These three tests give distance at least .557 from the witness to the **whole** half-turn image. The open upper disk \(\rho\le .30\) remains pointwise fixed with diameter at least .60. The three distinct non-\(C^3\) circles identify three fixed noncollinear centers exactly as in R740. Reflection in the upper grip plane is excluded because the lower image contains the mirror of the genuine upper point \((-1,0,H)\), of physical height \(-H\cos(2\gamma)-\sin(2\gamma)\); reflecting it in \(z=H\) would exceed height 1.32. Thus quotient separation is positive.

The upper grip also has radius-.08 balls with every point in either order. True-disk pairs use R740. Every lower point is separated by the signed grip distance \(H\cos\gamma-h\sin\gamma>.16\). The unchanged upper A argument uses actual \(x,y\) and physical height as before. On tilted B/wall \(|y|\ge.5\) suffices; otherwise \(|x|>.96\). The positive A-end has physical abscissa at least .52 and its positive ellipse endpoint exceeds .99; the residual is at most .003. On the negative branch both endpoints have abscissas below \(-.68\); the residual is at most .073. Terminal-wall removal of its .006 vertical coordinate costs at most .006. These are plain Euclidean separations greater than .16. This argument does not provide non-grip reach.

## 5. Complete spatial jets and the quantities still to solve

The generator's normalized shoulder \(u\) runs from 0 to 1 with physical material \(s=(L_A+L+z_e)u\). Setting `normalized=False` gives derivatives in physical \(s\). Formula (4), both azimuthal substitutions, and the low-order frame operations are differentiated twice, including the mixed derivative. For the final ellipse arclength lift \(\psi\), let \(g(\psi)=(j^2\sin^2\psi+\cos^2\psi)^{1/2}\), \(\bar g=(2\pi)^{-1}\int_0^{2\pi}g\). Then \(\psi'=\bar g/g,\ \psi''=-(j^2-1)\sin\psi\cos\psi(\psi'/g)^2\). The disk antiderivatives use \(C'=T,\ C''\) from the true turning law rather than a fitted derivative of quadrature nodes. For the phase rotation, the tilt reflection is performed in its own orthonormal frame before the physical rotation. The stationary upper mark jets are added in their actual fixed material coordinates. These derivatives give complete direct initial-field data for addition of free clamped corrections and for a separate physical-field Killing calculation.

A candidate whole-surface metric still must be frozen and matched. For the present radial foliation the two useful scalar prices are \(E_\perp=|F_s|^2-(F_s\cdot F_\theta)^2/|F_\theta|^2\) and \(V\cdot\kappa_\theta\), where \(V=F_s-(F_s\cdot F_\theta)F_\theta/|F_\theta|^2\) and \(V\cdot\kappa_\theta=V\cdot F_{\theta\theta}/|F_\theta|^2\). Their angular spreads are direct physical observations, invariant under sliding the angular labels; they need not vanish for these initial fields. For R723's independent reach price take the single center \(c_\gamma=(.58,0,.58\tan\gamma)\) in the mirror, rotated with the physical phase. The unmarked upper disk has support \((.58-u_0)\sin\beta+(H+v_0-.58\tan\gamma)\cos\beta>.085\), since \(u_0\le h+b/\sqrt2\) on the bend and tongue and \(\sin\beta+\cos\beta\ge1\). The actual marked graph changes this lower bound in the flat portion by less than .00001; there the flat support itself exceeds .09. Reflection preserves the center and the same support on the unmarked lower counterpart. The rest of the shoulder and its true principal curvatures must still satisfy the R723 global inequalities to obtain the requested reach. Finite multiresolution price tables do not turn an unverified interval into a certificate. No actual nonlinear same-metric or full-thickness solution follows from a completed initial-field evaluation.
