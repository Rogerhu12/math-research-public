# R737 — Two-cap matching and an exact finite isometric pair of closed marked embedded surfaces

2026-11-28. **Proved, for a new designed metric.** Retain the exact existing deep-valley tail from each cap up to a selected positive material cut. A controlled round turn after each cut and reflection at the equator produce a compact $C^2$ embedded sphere with two fixed marked caps and a genuine nonrigid infinitesimal bending which fixes both caps. For each sufficiently small fixed nonzero amplitude, its two opposite displacements give two distinct, Euclidean-noncongruent **exactly isometric** closed embeddings, with the same fixed marked caps, reach $>.03D$ and fixed grip diameter $\ge .2D$. The material cut is selected by a proved winding argument, without reversing the prescribed singular tail or assuming a numerical eigenvalue. This changes the *interior* metric and circular base core; it does not solve the original full Fejér/R690 two-end boundary conditions. It gives a pair of finite endpoints, not a continuous isometric flex of strong displacement $.2D$.

## 1. A continuously designed round turn

Choose once a mode $m\ge2$; $m=2$ suffices. A scalar $0<\delta<.0005$ is, for now, a variable physical cut in the backward arclength $u$ starting at a cap. Let $R$ be the actual R690 terminal radius in $(9/16,.57)$. Start the meridian as the exact original deep profile for $0\le u\le\delta$, with backward radial/descending tangent $(\cos\beta,\sin\beta)$ as in [R690](R690-quasimonotone-tail-and-deep-valley-input.md), and (below) measure ordinate downward from the cap. Its angular radius and vertical drop are obtained by integrating these two components, starting at radius $R$. Since $\delta<d_0/8$ for the original out width $d_0$, the pure oscillatory law holds. It gives $0<\beta(u)<u$ on this interval by $\beta(0)=0$, $|\beta'|<1$.

At the cut put $b_0=\beta(\delta)$, $k_0=\beta'(\delta)$, and
$$
 \ell=\frac{b_0}{100(1+|k_0|)}>0 .
$$
This $k_0$ denotes only the present cut derivative. Over the next arclength $\ell$, at normalized coordinate $t\in[0,1]$, use angle $b_0+k_0\ell(t-t^2/2)$. Its derivative starts at $k_0$, ends at zero and has absolute value at most one. Its angle stays between $.995 b_0$ and $1.005 b_0$. Call the end angle $b_1$.

Put $d=.14$, $b=.001$, and let $S_5(t)=10t^3-15t^4+6t^5$. From $b_1$ prescribe curvature in succession:
$$
 S_5(t)/d\text{ over length }b,\qquad
 1/d\text{ over length }d(\pi/2-b_1)-b>0,\qquad
 (1-S_5(t))/d\text{ over length }b .
$$
Both variable pieces use their own increasing affine $t$. The integral is exactly $\pi/2-b_1$ since $\int S_5=1/2$. The end tangent is vertical and the end curvature zero. The meridian is $C^2$, its angle $\alpha$ lies in $[0,\pi/2]$, strictly positive except at the cap, and $|\alpha'|\le1/d$. During the last three pieces the angle is nondecreasing. The choices depend continuously on $\delta>0$.

Revolve the meridian about the common vertical axis. Place its final vertical-tangent ring at height zero, the first cap at height $H_\delta>0$, reflect across height zero, and put the original three upper and one lower p4 markers on the two flat disks (R716 §4). The meridian radius $a(u)$ is at least $R$. On the last turn the radial/descending increments are respectively $d(1-\sin b_1)+e_x$ and $d\cos b_1+e_h$, where $0\le e_x,e_h\le b$. Indeed integrate $f(\alpha)=\cos\alpha$ or $\sin\alpha$ against $du=d\,d\alpha+(1-d\alpha')du$, whose nonnegative remainder has total mass $b$. The first two piece lengths total $\delta+\ell<.00051$. Therefore the entire radius is $<.713$, and $.139<H_\delta<.143$. The sphere $M$ with this surface of revolution and its actual marked caps is closed, connected, embedded and $C^2$: strictly positive drop separates parallel sections, the end turns vertical, and the true deep tail has zero curvature and horizontal tangent at the flat rim. The paired halves have matching second jets at the equator. The marked reference diameter is at most $2\sqrt{.713^2+.144^2}<1.46$.

## 2. The closed reference has a full quantitative reach margin

We prove all ordered pairs, including the two-sided normal inequalities across the equator. Recall R732 §3's planar chord lemma: if the tangent angles of a unit meridian on a particular connecting arc are in an interval of length $\pi/2$ and $|\alpha'|\le1/d$, its chord from either base satisfies $2d|\text{normal component}|\le|\text{chord}|^2$. The proof integrates $|(d/du)\sin(\alpha-\alpha_{\rm base})|\le d^{-1}\cos(\alpha-\alpha_{\rm base})$ in base tangent coordinates, so it allows the actual oscillatory nonmonotonicity. Each entire half including the straight disk radius satisfies this lemma. Rotation adds $2rr'(1-\cos\omega)$ to the squared planar chord, and at most $2d|n_r|r'(1-\cos\omega)$ to $2d$ times the absolute normal projection. At every nonflat base $r\ge R>d$ and at a disk base $n_r=0$. This covers arbitrary azimuths including disk centers.

Take $\tau=.047$. An opposite-half unmarked pair of distance at least $2\tau$ passes at either base. Otherwise both heights have magnitude $<.094$. Each such point lies in the nondecreasing last turn, at angle $>\pi/4$ in its upper-half representation. Indeed before that turn the remaining drop exceeds $d\cos b_1>.139$, and on the turn at angle $\alpha\le\pi/4$ the remaining drop is at least $d\cos\alpha\ge .14/\sqrt2>.094$ by the same nonnegative-remainder calculation. Between the two points along the meridian through the equator, the continuous tangent angles are therefore in $[\pi/4,3\pi/4]$ in downward traversal. The same planar and azimuthal chord bounds apply across the join. This proves both radius-$\tau$ inequalities for every unmarked pair. The separation argument based on heights applies just as well when the endpoints have different azimuths.

Within an actual marked cap the full graph Hessian bound $5$ from [R732, §3](R732-rounded-cap-exact-terminal-metric-and-full-reference.md) pays both radius-$.2$ tests. Every marker point is at radius at most $.2$ and is separated horizontally from any active point by at least $R-.2>.36>2\tau$. A marked point and one on the other cap are separated by at least $2H_\delta>.278$. All other same-cap or mixed pairs were covered above. Thus every actual complete closed surface in this construction before bending has reach $\ge.047$ by Federer's tangent-plane characterization (1959, Theorem 4.18, p.449). Its absolute principal curvatures are at most $\max(1/d,1/R,5)<8$ from the meridian, azimuthal and marked graph formulas, so even the diagonal part has a strict reserve.

## 3. The genuine deep-tail matching phase winds without bound

On the common original pure deep tail choose any nonzero real cap-flat R735 line in mode $m$, with tangential coefficient $iV$ and height coefficient $W$. For propagation from a cap *toward the equator*, use the state
$$
 y=a^{m^2-1}V,\qquad z=a^{-m^2}W .
$$
This $z$ has opposite sign to R735's canonical state in its variable increasing toward the cap. Directly from R735 (2), for the meridian in the present backward physical arclength $u$, it solves
$$
 y'=\mathcal A z,\qquad z'=-\mathcal B y,\qquad
 \mathcal A=m a^{2m^2-2}c,\quad
 \mathcal B=m(m^2-1) a_u^2a^{-2m^2}/c,\qquad c=\sin\alpha .
 \tag{1}
$$
This remains regular at the vertical equator $a_u=0$, since $c=1$ there. The chosen tail solution is never zero as a two-dimensional state at any positive $u$. Its ordinary lifted argument has derivative
$$
 (\arg(y+iz))'=-(\mathcal B y^2+\mathcal A z^2)/(y^2+z^2).
 \tag{2}
$$
On the genuine deep tail both coefficients are positive. R735 (8)–(10) gives alternating nonzero signs of $y$ at all sufficiently late valley phases $v_n$ accumulating at $u=0$. There are infinitely many intervening zeros. Monotonicity of (2) implies the initial argument at the cut tends to $+\infty$ on its continuous lift as $\delta\downarrow0$.

The continuation on the added pieces changes that argument by a uniformly bounded amount independent of $\delta$ for this fixed $m$. On the short interval of length $\ell$, $c$ lies between fixed positive multiples of $b_0$ and all radii are bounded above and below. Thus $\int(\mathcal A+\mathcal B)\le C_m\ell(b_0+b_0^{-1})\le C'_m$; this bounds the argument change by (2). On the remaining turn $c$ is nondecreasing and $0\le c\le1$, so
$$
 \mathcal B(y)\mathcal A(x)\le C_m \qquad(x\le y)
$$
throughout it. This uses the actual ratio $c(x)/c(y)\le1$, the uniform radius bounds, and $|a_u|\le1$. Even as $b_1$ tends to zero it does not require a uniform bound on $\mathcal B$ by itself. Cut this turn into a number of subintervals bounded independently of $\delta$, so that $C_m$ times the square of each length is less than $1/4$; the total length is at most $d\pi/2+b$. For each subinterval and every initial portion, the Volterra estimate for the solution with initial $(0,1)$ from R735 §2 gives $|z-1|\le(1/4)/(1-1/4)=1/3$. In particular its lifted argument stays within one open half-circle. The linear transfer has determinant one. For any other initial direction the continuous angle under this transfer stays, up to an integer multiple of $\pi$ fixed initially, within $\pi$ of that reference direction's lifted angle: two noncollinear directions keep nonzero determinant and cannot cross projectively. The collinear case is immediate. Consequently the argument change for any initial state is bounded by $3\pi$ per subinterval, uniformly. This avoids relying on the badly conditioned unscaled maximum of $1/c$.

For $\delta>0$ the endpoint phase is continuous: the cut data are continuous and nonzero and each regular connector ODE depends continuously on its coefficients and segment lengths. Equivalently its continuous lift is the initial lift plus the integral of (2) on the added pieces. Its difference from the initial lift is uniformly bounded, so the equatorial phase tends to $+\infty$ as $\delta\downarrow0$. The intermediate value theorem gives infinitely many positive cut choices accumulating at zero with equatorial phase an integer multiple of $\pi$. Fix one of them. This is the actual equation $W=0$ at the equator, and $V\ne0$ there since the full state is nonzero. The metric and cut are henceforth fixed. No phase condition was imposed using a renamed old core, a formal series, or a numerical zero.

## 4. Mirror the matched bending and obtain exactly isometric finite endpoints

The upper activity field is the real part of
$$
 Y=(mV e_r+iV e_\theta+W e_z)e^{im\theta}.
$$
It is zero, with all jets, on the upper marked cap. The two missing Gram equations of its linear isometry are exactly (1) in physical coordinates, and the angular equation follows from the coefficient $mV$. On the lower half take the same horizontal field and the negative vertical field reflected about the equator. At the seam $a_u=0,\ c=1,\ W=0$, the original regular equations give $V_u=0$ and $W_u=m(a_u/c)V_u=0$. Differentiating the latter once gives $W_{uu}=0$ there. Therefore the value, first and second jets of the mirrored $Y$ agree, including angular and mixed derivatives. It vanishes on both complete caps and gives a nonzero global $C^2$ infinitesimal bending of this particular closed reference $F_*$. The connector angles are $C^1$, which suffices for (1) to give $C^2$ material fields across its joins. The fixed p4 cap graphs have their original regularity. A rigid infinitesimal motion cannot vanish on an entire open flat disk without vanishing everywhere.

For real $\epsilon$ define
$$
 F_+=F_*+\epsilon Y,\qquad F_-=F_*-\epsilon Y.
$$
On the entire closed material sphere, including its fixed caps, the exact bilinear identity is
$$
 F_+^*g_{\rm Eucl}=F_-^*g_{\rm Eucl}
        =F_*^*g_{\rm Eucl}+\epsilon^2(dY)^T dY=:g_\epsilon .
 \tag{3}
$$
Indeed the term linear in $\epsilon$ vanishes identically by the just-proved global infinitesimal isometry. For each fixed nonzero $\epsilon$ the two displayed maps therefore have a **single fixed exact metric**, generally different from that of $F_*$. This is a finite-amplitude algebraic equality, with zero induced-metric discrepancy between the two endpoints independently of a grid.

For sufficiently small $|\epsilon|$ both are embeddings by compact $C^1$ stability. For the two full endpoint surfaces their reaches are at least $.046$ for all sufficiently small $|\epsilon|$. To verify the strict lower margin, suppose otherwise along an endpoint sequence tending to $F_*$ in $C^2$. A violating tangent-plane chord has a convergent subsequence of ordered base/test parameters. If they have distinct limits the reference $.047$ inequality is strict for $.046$, and $C^1$ convergence contradicts the violation. At coincident limits use a regular local chart on the closed sphere. By joint $C^2$ convergence, the limiting upper bound on twice the normal projection divided by squared chord length is at most the reference maximum absolute principal curvature $<8$, whereas $1/.046>21$. The local estimate follows by second-order Taylor expansion in that chart and normalization by the limiting positive first fundamental form. This covers seams as well. Diameters tend to the reference diameter $<1.46$; hence $D=\operatorname{diam} F_+(M)<1.5$ for small amplitude and both endpoints have reach $\ge.046>.03D$. The fixed cap disk of radius $.45$ in material planar coordinates (including any fixed p4 graph it contains) has interior and diameter at least $.9>.2D$, since its rim is genuinely flat. Both caps are fixed pointwise.

## 5. The images really differ and have positive Euclidean quotient distance

The bending has a nonzero normal component somewhere on the open activity. Otherwise it is tangent throughout the upper cap-tail component and a tangential Killing field of that metric. Here this can be checked without global rigidity: write the tangential field as $fE+gT$ in the orthonormal meridional/angular frame, with inward-to-outward $s$ coordinate. Vanishing of the $ss$ variation gives $f_s=0$; $f=0$ at the cap, so $f=0$. The mixed variation then gives $g_s-(a_s/a)g=0$, so $g=0$ as well because it vanishes at the cap. This contradicts the chosen nonzero mode. Nonvanishing of the normal component also persists at some fixed interior point of the full doubled surface.

At such a point $p$, the two images have positive separation for all sufficiently small $\epsilon\ne0$. More precisely the distance of $F_+(p)$ from $F_-(M)$ is at least a positive constant times $|\epsilon|$. If this were false along a vanishing sequence, take nearest material points $q$. Embeddedness and compactness of the limit give $q\to p$. In a regular chart $|q-p|=O(|\epsilon|)$ by comparing to $F_-(p)$ and using a local lower Lipschitz bound for $F_*$. Project the equality up to $o(|\epsilon|)$ on the fixed $N_p$; the linear term in $F_*(q)-F_*(p)$ is tangent, and continuity gives $2\epsilon N_p\cdot Y(p)=o(|\epsilon|)$, a contradiction.

Finally the phase endpoints $F_\pm$ have no planar germ on the activity. Every horizontal projection of a fixed-material circle remains noncollinear for small $|\epsilon|$ uniformly because reference circles have radius $\ge R$ and the perturbation is bounded. If an open patch lay in a plane, angular analyticity would extend that plane equation along complete circles for nearby material radii. Each circle is invariant as a set under the horizontal rotation by $2\pi/m$. The plane uniquely determined by a noncollinear circle must be invariant under that rotation. For $m\ge3$ it must be horizontal; for $m=2$ the other possibility is a vertical plane and is excluded by noncollinearity of the horizontal projection. A horizontal planar patch on complete circles at nearby radii would have constant mean height, but the mean height is exactly that of $F_*$ and strictly changes there. One may select the subpatch away from the finite joining circles; the genuine deep tail is strictly increasing in height away from the rim. Thus [R238](R238-planar-germ-marker-rigidity.md) and [R661, §4](R661-complete-nonplanar-activity-and-four-fixed-markers.md) apply with the actual four distinct-radius, affinely independent fixed circles. Every Euclidean congruence of the two marked images, including reflection, would be the identity. Their images differ, hence their quotient Hausdorff distance is positive by compactness of $O(3)$ and bounded translations on any hypothetical vanishing-distance sequence.

Equation (3) gives two exactly isometric complete endpoints. Linear interpolation between them generally changes the metric, since its quadratic term depends on the square of the interpolation parameter. No continuous isometric path or $.2D$ displacement is inferred, nor is the selected cut numerically enclosed. This new two-cap metric uses the original R690 law only on the two terminal pieces; the complete earlier Fejér target and its active computations remain separate. No scientific computation or numerical selection was executed for this proof.
