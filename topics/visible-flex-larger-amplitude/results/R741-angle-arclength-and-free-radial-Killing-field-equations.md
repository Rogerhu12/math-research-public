# R741. Exact angle-arclength equations for the finite one-sided disk shoulder

Let \(s\) denote physical radial material distance on the shoulder before any change of angular variable. It need not be arclength on the new surface. Its interval is \([0,L]\). Take an immersion \(F(s,\theta)\) periodic in \(\theta\), with the symmetry \(F(s,-\theta)=JF(s,\theta)\) for the isometric reflection \(J:(x,y,z)\mapsto(x,-y,z)\). This reflection commutes with reflection in each tilted equator used below. At least two continuous derivatives are assumed for the metric equations, with the additional mixed derivatives stated for the chart and its edge below. All angular means in this note use the measure \(d\theta/(2\pi)\).

For each \(s\), define
\[
 w=|F_\theta|,\qquad T=F_\theta/w,\qquad q=F_s\cdot T,\qquad V=F_s-qT,
 \quad E=|V|^2,\quad P=\langle w\rangle,\quad H=P_s/P .
\]
The immersion hypothesis gives \(w>0,E>0\). Both have positive minima on the compact shoulder. The choice of the fixed reflection ray \(\theta=0\) specifies the angular origin. Put
\[
 \eta(s,\theta)=P(s)^{-1}\int_0^\theta w(s,\alpha)\,d\alpha,\quad
 B=q-P\eta_s,\qquad
 \widetilde F(s,\eta)=F(s,\theta(s,\eta)).
 \tag{1}
\]
Here \(\theta(s,\cdot)\) is the inverse degree-one circle diffeomorphism. The denominator \(P\) is circumference divided by \(2\pi\).

**Theorem.** The three coefficients of the induced metric of \(\widetilde F\) are
\[
 \widetilde g_{ss}=E+B^2,\qquad
 \widetilde g_{s\eta}=PB,\qquad
 \widetilde g_{\eta\eta}=P^2 .
 \tag{2}
\]
Functions of \(\theta\) on the right are evaluated at \(\theta(s,\eta)\). This fixed family of physical rings, in its angular arclength chart, has an angle-independent metric exactly when \(E\) depends only on \(s\) and \(B=0\). In particular, there are only two angular equations. Without any division by ring curvature these can equivalently be written
\[
 |V|^2=A(s),\qquad V\cdot\kappa=-P_s/P,\qquad
 \kappa=w^{-1}\partial_\theta T .
 \tag{3}
\]
These are equations for the chosen rings. Other foliations of the same physical image can have different defects.

Indeed, \(\eta_\theta=w/P\), so \(\widetilde F_\eta=PT\) and \(\widetilde F_s=F_s-P\eta_sT=V+BT\). This proves (2). Reflection makes \(w\) even, \(q\) odd and \(\eta\) odd, hence \(B\) odd. An angle-independent cross term must consequently vanish. Now \(q_\theta=w_s+w V\cdot\kappa\) and \(P(\eta_s)_\theta=w_s-wP_s/P\), proving
\[
 B_\theta=w(V\cdot\kappa+H).
 \tag{4}
\]
An odd constant vanishes, including on every regular ring with a straight subarc. The circumference first variation \(\langle w V\cdot\kappa\rangle=-P_s\) follows by integration. For a target \(A(s)ds^2+Q(s)^2d\eta^2\), with \(A,Q>0\), the relative metric defect is the larger absolute deviation from one of the two eigenvalues of
\[
 \begin{pmatrix}(E+B^2)/A & PB/(Q\sqrt A)\\ PB/(Q\sqrt A)& P^2/Q^2\end{pmatrix}.
 \tag{5}
\]
Composition with \(\theta(s,\eta)\) leaves the full-circle supremum unchanged.

**The actual two edges.** At \(s=0\), require equality of the position, first and second radial derivatives, as functions of \(\theta\), with the finite isometric disk
\[
 D(r,\theta)=C(r\cos\theta)+r\sin\theta\,e_y+H_0 e_z,\qquad
 C'(x)=(\cos\beta(x),0,\sin\beta(x)),\quad r=1+s .
\]
Here \(H_0\) is the physical disk height. Since \(C'\) has unit length orthogonal to \(e_y\), the disk metric is \(dr^2+r^2d\theta^2\). Assume the mixed edge traces through \(F_{ss\theta}\) exist and can be computed by differentiating the radial traces, as for the disk and finite Fourier and quintic spline corrections used here. Then \(w(0)=1,\ w_s(0)=1,\ w_{ss}(0)=0\), from the disk identity \(|D_\theta|=r\). Thus \(\eta(0,\theta)=\theta,\ \eta_s(0,\theta)=\eta_{ss}(0,\theta)=0\), including angular derivatives of the matching identities whenever used. The inverse material chart has the same matching radial traces. The tangents and all second derivatives of the actual disk are preserved. One concrete base uses \(r(s)=1+d\tanh(s/d)\), \(d=0.15\), in the true bent curve \(D(r(s),\theta)\), then the left endpoint quintic Hermite cutoff and a terminal linear-jet Hermite interpolant. The identities \(r(0)=1,r_s(0)=1,r_{ss}(0)=0\) give the required matching. This preserves the large disk bend throughout its use in the base. It does not require Taylor extrapolation of rim acceleration across the shoulder.

At \(s=L\), in a fixed orthonormal frame of the tilted mirror plane \(\Pi\), impose
\[
 F(L,\theta)\in\Pi,\qquad F_s(L,\theta)=-n_\Pi,\qquad F_{ss}(L,\theta)\parallel\Pi .
 \tag{6}
\]
The notation \(\parallel\Pi\) for a vector means that its normal component is zero. Such a field has \(w_s(L)=0\), since \(F_{s\theta}=0\), and therefore \(\eta_s(L)=0\). In the inverse coordinates, \(\theta_s(L)=0\), but in general \(\theta_{ss}(L)\) need not vanish. Its contribution \(F_\theta\theta_{ss}\) to \(\widetilde F_{ss}\) lies in \(\Pi\). Consequently (6) holds for \(\widetilde F\) as well. The lower field \(J_\Pi\widetilde F(2L-s,\eta)\), reflected across the equator with the reversed signed radial variable, has the same two-jet there. In detail, the first derivative changes by \(-J_\Pi\), the second by \(J_\Pi\), and the mixed derivative vanishes because the first derivative is a constant vector on the edge. The angular derivatives through order two are planar. At the upper and lower disk rims the same direct trace test applies. For a \(C^2\) canonical chart inside the shoulder, it suffices for \(w\) to have two continuous \(s\)-derivatives and the corresponding first angular and mixed derivatives, and for \(P\) to stay positive. All formulas here concern the underlying analytic or piecewise smooth data. A floating null-space basis satisfies its clamped trace constraints to numerical precision. An exact representation for a degree-five clamped spline correction sets its first three control rows to zero, the last two horizontal rows equal and the last three vertical rows zero.

Suppose (3) holds everywhere. Use the upper and reflected lower unmarked pieces and act by \(\eta\mapsto\eta-t\) in material, followed by the ambient rotation \(R_t\) about the fixed vertical through the straight disk patch. This yields the same metric at every \(t\) by (2), and the image of the entire unmarked body is \(R_t\) of the initial one. On a concentric disk of radius \(h\) where the upper unmarked disk is planar and horizontal the map fixes every point after the two rotations. Smooth stationary marker height functions supported strictly inside this disk can therefore be attached for every \(t\). Their fixed graph metric is common to the family. In particular an image-only witness, chord-ball estimate, or support bound uses the same candidate geometry before and after the material angular change, provided the markers are treated in their stationary frame. The equations above do not imply any particular numerical image separation, embedding, or reach. These require independent estimates. For a target (5) fixed through refinement, a uniform bound on (5)'s eigenvalue defect bounds every rotated phase by the same number, since the target is angle independent on the moving pieces.

**Full-circle forward and transpose variations.** Write \(\mathcal I\) for the periodic primitive with mean zero on zero-mean functions, null on constants. Reflection and differentiation of (1) give
\[
 B=q-\mathcal I(w_s-wH),\qquad w_s=T\cdot F_{s\theta}.
 \tag{7}
\]
The integrand is even with zero mean, so its periodic primitive is odd and vanishes at zero. For variations \(u=\delta F_s,\ v=\delta F_\theta,\ m=\delta F_{s\theta}\) retaining the reflection, write \(U=F_s,\ M=F_{s\theta}\). Then
\[
 dw=T\cdot v,\quad dT=(I-TT^\top)v/w,\quad dq=u\cdot T+U\cdot dT,
 \quad dE=2U\cdot u-2q\,dq,\quad dw_s=dT\cdot M+T\cdot m,
\]
\[
 dB=dq-\mathcal I\left(dw_s-H\,dw-
 w\frac{\langle dw_s\rangle-H\langle dw\rangle}{P}\right),\qquad dP=\langle dw\rangle .
 \tag{8}
\]
Here \(I\) inside the projector denotes the identity on ambient vectors. For incoming adjoints \(e,b\) of \(E,B\), put
\[
 a=b-2qe,\quad h=\mathcal I b,\quad k=h-\langle hw\rangle/P,\quad
 \ell=aU+kM .
\]
The corresponding outgoing adjoints of \(u,v,m\) are, respectively,
\[
 2eU+aT,\qquad -HkT+(I-TT^\top)\ell/w,\qquad kT .
 \tag{9}
\]
An incoming adjoint of \(P\) is handled by \(dP=\langle T\cdot v\rangle\), with matching mean or sum weights. Equations (8) and (9) follow directly by the product rule, self-adjointness of angular averaging and \(\mathcal I^\top=-\mathcal I\). They apply also to uniformly sampled trigonometric integration with the mean and the unpaired even-grid Nyquist multiplier both set to zero. In this finite calculation the integrand need not be a band-limited function. The discrete primitive and its transpose are exact linear-algebra partners for the sampled problem. A continuum certificate must separately bound quadrature, unresolved modes, derivatives and floating error.

The implementation in scripts/resume_20261128/bent_disk_arclength.py uses (5), (7)–(9) with the actual full fields from the run-36 module and an independent R740 ellipse starting geometry. Its designed-stage scalar is \(A=\langle E\rangle\) estimated in the original angle. Any strictly positive angular measure would detect the same zero-scatter locus. For both fixed-target refinements it defines \(A_*(s)\) and \(P_*(s)\) by evaluating the very same selected source field and coefficient vector at the same 640 angles at each requested radial coordinate. There is no interpolation between two different meshes and no refitting of those functions at refinement. Exact positive mathematical target functions may likewise be specified by these fixed equiangular sums of the underlying source formulas, subject to explicit error bounds for the numerical source representation. A 257-radius fingerprint of the two functions is a reproducibility check. It is not their mathematical definition. The physical program also evaluates bending, support relative to a point in the mirror plane, two-sided sampled chords and finite held witnesses. These are distinct from the two angular equations. R638 supplies earlier global arclength estimates for two different stored prefixes. The identities here deliver normal-speed and cross-speed costs, both material edge tests and their full variation for a finite strong-disk shoulder.

**Releasing the radial foliation.** Let \(M_0\) be the connected compact closed unmarked double, \(F:M_0\to\mathbb R^3\) a \(C^2\) immersion with matching edges, \(g_0=F^*e\), and \(X\) a \(C^2\) material vector field. On the entire upper and lower disks prescribe \(X=\partial_\theta\), interpreted at the center as the smooth infinitesimal planar rotation. On the shoulder in the original physical coordinates write
\[
 X=U(s,\theta)\partial_s+W(s,\theta)\partial_\theta .
\]
For the reflection in \(y\), take \(U\) odd and \(W\) even in \(\theta\). For \(C^2\) matching with the disks it suffices that \(U,W-1\) and their first two radial derivatives vanish at the rim, as identities in the angle with the usual differentiated traces. For reflection across the equator extend \(U\) oddly and \(W\) evenly in signed radial distance from the equator. It suffices that \(U=U_{ss}=W_s=0\) there. A free equatorial meridional derivative \(U_s\) is allowed. Both rims and the equator are invariant under the flow by uniqueness for the ODE and \(U=0\) on those circles. The compact boundaryless surface and the \(C^2\) field give a complete \(C^2\) flow \(\varphi_t\), smooth to the stated order in initial point and time. This follows locally by differentiating the integral equation for the flow twice, then using a finite time covering of the compact material surface.

For \(t\in[0,T]\) set \(F_t=R_t F\circ\varphi_{-t}\), with the same ambient vertical-axis rotation as above. On the straight upper disk the two rotations cancel pointwise, so a time-independent marked graph can be attached inside that disk. On the unmarked body \(F_t(M_0)=R_t F(M_0)\) for every \(t\). Consequently a valid continuum held or support calculation for these images is independent of the newly freed radial material labels. An actual fixed marked graph requires its own local and mixed geometry bounds. With no markers the image family is ambient-congruent.

The tensor
\[
 K_{ij}=(\mathcal L_X g_0)_{ij}
 =X^k\partial_k(g_0)_{ij}
 +(g_0)_{kj}\partial_iX^k+(g_0)_{ik}\partial_jX^k
 \tag{10}
\]
is linear in \(X\) at fixed \(F\). Its coefficients use only the first two derivatives of the actual physical field. If \(K=0\), all \(F_t\) induce exactly \(g_0\), by differentiating \(\varphi_{-t}^*g_0\). Conversely, exact constancy of these pullbacks on any time interval starting at zero implies \(K=0\) by the derivative at zero. No assumption about the period or return map of the trial vector field is needed. A linear constrained minimization of (10) is therefore a geometric test for a given shape. It need not have zero minimum. Equations (2)–(3) are the special angle-relabeling case that keeps the input radial foliation.

For a uniform estimate put \(\epsilon=\sup_{M_0}\|g_0^{-1/2}Kg_0^{-1/2}\|_{\rm op}\), interpreted in any tangent bases. At every material point \(p\), for \(v\ne0\), the positive function \(a(t)=(\varphi_{-t}^*g_0)_p(v,v)\) satisfies \(|a'|\le\epsilon a\). Thus
\[
 e^{-|t|\epsilon}g_0\ \preceq\ F_t^*e\ \preceq\ e^{|t|\epsilon}g_0 .
 \tag{11}
\]
The actual marked patch is fixed at every time and has zero relative error against its fixed graph metric. The bounds apply on the unmarked complement and agree on the planar overlap. If one *single* target tensor \(g_*\) is fixed in material coordinates through all subsequent refinements, with \((1-\delta)g_*\preceq g_0\preceq(1+\delta)g_*\), \(0\le\delta<1\), the corresponding bounds in (11) relative to \(g_*\) have factors \((1-\delta)e^{-|t|\epsilon}\) and \((1+\delta)e^{|t|\epsilon}\). In particular the larger absolute deviation from one at \(T\) is at most \((1+\delta)e^{T\epsilon}-1\). Apply these bounds with the marked target on the fixed patch. A sampled least-squares norm of (10) supplies neither a uniform bound nor an exact Killing field. A residual for the actual solved \(X\), a positive reference metric, finite-time errors or their uniform upper bound, and independently computed whole-surface geometry are required to apply this criterion to a candidate.

**An exactly invariant target from an approximate trial field.** Suppose in addition that \(W>0\) on the upper closed shoulder, with the preceding disk and equator traces. This condition is on the annular component \(W\); the smooth polar generator vanishes as a vector at each disk center. Taking the reflected field below and \(\partial_\theta\) on each disk introduces no singular division at a pole. Because the material is compact, \(W\) on the shoulder has a strictly positive minimum. For each initial \(s=b\) at \(\theta=0\), solve
\[
 \partial_\theta \sigma(b,\theta)=U(\sigma,\theta)/W(\sigma,\theta),
 \qquad \sigma(b,0)=b .
 \tag{12}
\]
Both endpoints are invariant. The derivative \(\sigma_b\) is the exponential of the integral of \(\partial_s(U/W)\) along the trajectory, hence remains positive. Reflection yields \(\sigma(b,2\pi-\theta)=\sigma(b,\theta)\): both sides satisfy (12) with the same value at \(\pi\), by oddness of the right side under \(\theta\mapsto2\pi-\theta\). In particular \(\sigma(b,2\pi)=b\) exactly. The map \((b,\theta)\mapsto(\sigma(b,\theta),\theta)\) is thus a degree-one \(C^2\) annular diffeomorphism. Write \(b(p)\) for its first inverse coordinate. It is constant on each orbit, and the positive return time
\[
 T(b)=\int_0^{2\pi} W(\sigma(b,\theta),\theta)^{-1}\,d\theta
\]
is \(C^2\) by the positive denominator and compact integration interval. Now use \(Y=T(b(p))X/(2\pi)\). Its flow \(\psi_t\) goes once around every shoulder orbit in time \(2\pi\). The pointwise fixed disk centers also satisfy \(\psi_{2\pi}=\mathrm{id}\). On a disk \(T=2\pi\) and \(Y=\partial_\theta\). The traces \(U=0,\ W=1,\ U_s=W_s=U_{ss}=W_{ss}=0\) at its rim imply by differentiating the integral that \(T_b=T_{bb}=0\) there. At the equator the two-sided \(C^2\) extension has \(U\) odd, \(W\) even in signed radial distance. Its time \(T\) as a function of signed initial distance is even, by reflection of the solutions in that variable. Thus \(Y\) defines a global \(C^2\) field and \(\psi\) a global \(C^2\) circle action conserving the two halves.

Given one selected unmarked source \(F_*\) with positive \(g_{\rm in}=F_*^*e\), define one material tensor
\[
 g_*=\frac1{2\pi}\int_0^{2\pi}\psi_t^*g_{\rm in}\,dt.
 \tag{13}
\]
It is positive definite by averaging positive quadratic forms over a compact interval, and invariant under every \(\psi_h\) by periodicity and change of integration variable. Its regularity is at least \(C^1\) for the stated \(C^2\) maps, and improves with the inputs. It equals the flat disk metric on each entire unmarked disk, since the material action there is the ordinary polar rotation. To use the fixed marked graph, replace the flat upper center patch tensor by its time-independent marked metric, retaining their common planar collar. The marked tensor need not be invariant under material rotations inside the marked patch: the implemented map there is the constant-in-time graph, so the induced metric is already the chosen one. The invariance used for time transport is that of the unmarked tensor on the moving complement.

For any subsequent unmarked candidate \(G\) on the same material with the same prescribed planar central patch, keep \(\psi\) and (13) fixed. If \((1-\delta)g_*\preceq G^*e\preceq(1+\delta)g_*\) on the unmarked surface, then this inequality with exactly the same \(\delta\) holds for every \(R_tG\circ\psi_{-t}\). Pullback preserves quadratic form order and \(\psi_{-t}^*g_*=g_*\). The marked domain is fixed as above. In particular no time-accumulation factor is needed once the target and action have been frozen. Estimates for individual orbit periods or derivatives of a normalized experimental field must not be inferred merely from the smallness of an unnormalized sampled Killing cost. Formula (13) is a continuum definition and remains positive even when the chosen source is far from Killing. For computation the orbit maps, angular and radial derivatives, period, quadrature and positive denominators have to be bounded or numerically resolved as applicable. A later refit of (13) using each refined surface defines different metrics and cannot serve as fixed-target refinement.
