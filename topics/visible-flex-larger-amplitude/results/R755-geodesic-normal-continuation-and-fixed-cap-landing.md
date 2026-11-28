# R755. Geodesic-normal continuation through both complete rolled shoulders

Use R752's entire new material sphere. The required metric on either roll is
$$
 g_0=A_0(s,r)^2 ds^2+dr^2,\quad A_0=1-k(s)d(r)>0,\quad s\sim s+P,\quad 0\le r\le L .
$$
Its neighbors are the actual R753 central cylinder and full specified developed cap, with material labels fixed on both boundaries. The theorem below gives an exact test on the physical image of a candidate joined roll. The test pays two metric rows identically and isolates the remaining angular row and the cost of reaching the prescribed cap.

## 1. Actual normal rays and their domain

Write the trial roll in its own full periodic coordinates as $H(a,b)$, $0\le b\le L$. Require a regular embedded whole $C^2$ surface with actual two-jet matches to the prescribed central and cap shapes; the interiors of its rolls can have arbitrary induced metric. Its inner rim has speed one and is intrinsically geodesic by the central flat metric and the join. From each $a=s$ launch the surface geodesic in the outgoing unit co-normal. Write $X(s,\tau)$ for its position at arclength $\tau$, $V=X_\tau$, $T(s)$ for first time at the cap rim and $\sigma(s)$ for the raw cap label it hits. Assume unique existence through that first transverse hit, $C^1$ dependence of $(X,V)$ on arclength and starting label, and the standard Jacobi first variation on smooth interiors with continuous variational field and covariant velocity through regular joins. Require an orientation-preserving, nonfocal, one-sheeted covering of the roll by these rays. One sufficient covering check is $db/d\tau>0$ before and at landing, and a strictly positive angular derivative of $s\mapsto a(s,b)$ at each fixed $b$; its lift has degree one, so every latitude is covered exactly once. In a family require these data and first variations continuously in phase, with uniform positive transversality and regularity margins on compact domains.

A $C^4$ regular trial immersion has the needed ordinary geodesic regularity; absence of crossing and correct landing still require proof. At lower regularity the transverse $b$-clock system in §3 provides a sufficient first-variation check: locally uniform integrable bounds in $b$ on its first angular/state derivatives, a.e. continuity of those derivatives at each ray for dominated convergence of the integral variational equations, and uniform control of the neighboring ray states. Integral Grönwall gives uniqueness and differentiation of the integral equation gives $C^1$ variation. A bound $C(1+b^{-1/2}+(L-b)^{-1/2})$ is integrable when a transverse fractional mode generates it. Piecewise-smooth rays crossing finitely many derivative jumps transversely admit the usual Jacobi continuation if the field and covariant velocity transmit continuously there. That transmission can instead be imposed explicitly as a hypothesis. No assertion of smooth normal flow is made for every $C^2$ immersion merely from its name, or for unresolved tangent crossings.

## 2. The exact criterion

The identity $\langle X_s,V\rangle=0$ is preserved: its covariant $\tau$ derivative is $\langle\nabla_s V,V\rangle=\partial_s|V|^2/2=0$, and it holds at launch. Thus $g_{\tau\tau}=1,\ g_{s\tau}=0$. With $E$ the positively oriented unit parallel translate of the initial $s$-tangent perpendicular to the ray, the first variation $X_s=J E$ satisfies
$$
 J_{\tau\tau}+K(X)J=0,\qquad J(s,0)=1,\quad J_\tau(s,0)=0 .
$$
The initial derivative is the signed initial rim geodesic curvature, hence zero. $K$ is the curvature of the *physical trial*, not the target curvature. The angular row is $J^2$. Subtract $A_0''=-k(s)d''$ to obtain the Volterra relation $J-A_0=\int_0^\tau(\tau-w)[-KJ+k(s)d''(w)]\,dw$. No normal-curvature component is used as a denominator.

**Theorem.** Subject to §1, there is an isometric, correctly labeled normal reparametrization of this same trial image on the whole material roll, gluing to the given cylinder and cap, exactly when
$$
 T(s)=L\ \text{for every }s,\qquad
 J(s,\tau)=A_0(s,\tau)\ \text{throughout},\qquad
 \sigma(s_*)=s_*\pmod P\ \text{at one fixed material label}.
$$
Any correctly glued isometric parametrization has these data because the outgoing $g_0$-unit meridians are precisely these geodesics. Conversely their common hitting length makes $X_s(s,L)$ tangent to the rim and perpendicular to $V$. The target cap rim has arclength element $A_b(s)=1-d_b k(s)$, unchanged by its actual developable isometry. Its true lifted arclength is $\Omega_b(s)=s-d_b\Theta(s)$, $\Theta'=k$, with increment $P_b=P-2\pi d_b$. Hence
$$
 (\Omega_b\circ\sigma)'=|X_s(s,L)|=A_b(s)=\Omega_b'(s).
$$
The prescribed anchor kills the additive constant modulo $P_b$, so every rim label agrees. A free rotation in arclength could change the attachment of this noncircular cap. It is a real endpoint condition.

Set the material map on the roll to $X(s,r)$. It has exactly $g_0$ and the correct boundary positions. The unit launch and landing velocities are the correct directed normal-to-rim tangents. Across the inner seam the central transverse coordinate curves are geodesics by $ds^2+dy^2$. Across the cap seam the material inward normal-coordinate tracks are straight planar normals before the cap's actual isometric development; the R752 collar has $d'=1,\ p'=d''=p''=0$ there. Those cap tracks are also intrinsic geodesics. Their ambient accelerations on the two sides equal the common surface second form evaluated on the same unit tangent. The shared boundary curve supplies the pure angular second derivative and differentiating the matched co-normal gives the mixed derivative. Thus all four seams of the two rolls match in two-jets. The resulting map is $C^2$ inside: $E$ is the oriented cross product of $V$ and the surface normal, hence $C^1$ under §1; now $X_s=A_0E$ and $X_\tau=V$ are both $C^1$. This argument avoids assuming second differentiability of every raw solution map of the geodesic ODE. The same formulas and family hypotheses give phase continuity of the two-jets. Diffeomorphic reparametrization preserves the physical image, its reach and image distances. The prescribed grip is unchanged.

## 3. Six-jet shooting with the actual material radius as clock

With $p=da/db,\ q=(p,1)$ put $G_{ij}=H_i\cdot H_j,\ \Gamma^h_{ij}=G^{hk}(H_k\cdot H_{ij})$. Compute $K=(l_{aa}l_{bb}-l_{ab}^2)/\det G$ from $l_{ij}=n\cdot H_{ij}$. The geodesic equations after eliminating the affine parameter and the scalar Jacobi equation become
$$
 a_b=p,\quad p_b=p\,\Gamma^b(q,q)-\Gamma^a(q,q),\quad
 \ell_b=\sqrt{G(q,q)},\quad J_b=\ell_b Q,\quad Q_b=-\ell_b KJ .
$$
Initial data are $(s,-G_{ab}/G_{aa},0,1,0)$; the named seam charts have zero initial slope. The terminal $\ell(s,L)$ is $T(s)$ and the lift $a(s,L)$ gives the landing label. Differentiating $X(s,T(s))$ also gives $T'=\langle H_a(\sigma,L)\sigma',V(s,T)\rangle$. This restricts terminal tangent errors; it does not replace the prescribed value $T=L$.

For a finite solve one can compare $J$ to $A_0(s,L\ell/T)$ and independently charge the entire $T-L$ function. This keeps evaluation on the fixed interval and has exactly the theorem's zeros. Including every angular landing discrepancy in an objective is consistent with the anchored criterion. Check nonfocusing, angular folds, transverse velocity, physical immersion, support and the full actual cap landing. Any guarded or chart-exiting trajectory is unverified physically.

A reconstructed approximate closed field needs its own common material map. For example fit the displacement from $(s,L\ell/T)$ to $(a,b)$ by two periodic functions whose first two transverse jets and values vanish at $0,L$; compose the actual raw physical six-jet with that actual coordinate map. A positive coordinate determinant with boundary identity and degree one is sufficient for diffeomorphism. Read all three induced Gram rows on this reconstructed field, since finite $J,T,\sigma$ discrepancies alone do not prove those rows small. The actual shapes, fit, spatial grid, shooting and time can all be refined on the same complete target.

## 4. An exact analytic comparison

For the unbent, unrotated R752 physical body, prescribe the shifted central circle $q(s+h)$, $h=.15\phi$. Any regular cutoff gauge that arrives at unshifted cap labels represents the same geometric roll. Its normal rays are the original meridians at $s+h$. Consequently
$$
 T=L,\qquad \sigma(s)=s+h,\qquad J=1-d(\tau)k(s+h).
$$
The raw shear disappears everywhere in normal coordinates, but the angular row generally differs in curvature-changing sectors and the terminal cap anchor fails for $h\ne0$. This separates the geometric equations that a genuine end-shape change must solve from the two identically paid gauge rows. The criterion supplies no evidence that an unmeasured candidate or any sampled approximation already meets all three conditions.
