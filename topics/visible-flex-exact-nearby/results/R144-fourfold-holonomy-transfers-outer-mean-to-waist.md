# R144: fourfold holonomy transfers the outer curvature mean to the waist

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

**Proved: an exact nonlinear boundary-row replacement, full Euclidean
closure of the reconstructed core, and the complete off-shell source
identity for that replacement.** On the stated physical outer-circle
neighbourhood, the independent outer physical curvature mean can be
replaced by the waist condition
$$
                  \langle v(0)\rangle_\phi=-a(0).
$$
All body equations, the complete waist $B$ row, the outer $B$ row, the
nonmean outer $C$ row and every transmission condition remain. This is an
equivalence of nonlinear zero sets in one specified winding branch.
It does not assert existence, replace a forced equation by its
zero-residual version, or transfer an old inverse certificate to a new
matrix.

The monotone object is the trace of the **quarter-circle SO(3)
transport**. Position closure is proved separately. The off-shell formula
keeps ordinary defects, boundary defects, and all one-sided jumps.
Its derivative at a genuine solution is an explicit triangular row
operation. True metric-parameter/phase compatibility remains independent.
No new scientific computation is used.

## 1. The complete variables and the two boundary problems

Use the material angle $\theta$, of period $2\pi$, and the actual fourfold
symmetry, so curvature coefficients have period $L=\pi/2$. Write
$$
 g=E(r)\,dr^2+a(r)^2d\theta^2,\quad
 e=\sqrt E,\quad b=a'/e,\quad\gamma=e/a,\quad\beta=a'/a.
 \tag{144.1}
$$
On the core $0\le r\le R=25/8$, $a,e>0$. At the waist
$a'(0)=E'(0)=0$. The frame and second fundamental form have the convention
of the [complete physical matching theorem](R133-supplement-full-physical-trace-matching-and-waist-reflection.md):
$$
 X=F_r/e,\quad Y=F_\theta/a,\quad n=Y\times X,\qquad
 \mathrm{II}=\begin{pmatrix}A&B\\B&C\end{pmatrix}.
$$
The physical equations are
$$
 AC-B^2=K,\qquad
 B_r=\gamma A_\theta-2\beta B,\qquad
 C_r=\gamma B_\theta+\beta(A-C).
 \tag{144.2}
$$
In the graph used by the original problem, $C\ne0$ and
$A=(K+B^2)/C$.

Retain the true moving chart, from the
[complete moving-to-physical trace theorem](R133-supplement-physical-inner-curvature-data-from-true-moving-core-trace.md):
$$
 \begin{split}
 m&=\langle v\rangle_\phi,\qquad
 \Theta(\phi)=\phi+I_\phi(v-m)/m,\qquad \Theta_\phi=v/m>0,\\
 B&=(u/v)\circ\Theta^{-1},\qquad
 C=(1/v)\circ\Theta^{-1},\qquad
                  \langle C\rangle_\theta=1/m.
 \end{split}
 \tag{144.3}
$$
The last equality uses $d\theta=(v/m)d\phi$. It is not
$\langle1/v\rangle_\phi$. Means and $L^2$ norms in a named angular
coordinate are normalized on one quarter circle. The odd/even symmetry
fixes the chart origin. Fourfold periodicity gives
$\Theta(\phi+L)=\Theta(\phi)+L$.

Supply a genuine periodic outer cap with the same metric germ at $R$,
complete physical traces $(B_{\rm cap},C_{\rm cap})$, and fourfold
curvature coefficients. Its frame and position are single-valued.
Keep all its independent inputs, height conditions, far labels and metric
design equations. Set
$$
 d_B=B(R)-B_{\rm cap},\quad
 d_C=P_{\ne0,\theta}(C(R)-C_{\rm cap}),\quad
 c=\langle C(R)-C_{\rm cap}\rangle_\theta.
 \tag{144.4}
$$
The systems compared here have identical body, cap, far, symmetry,
any independently specified phase/normalization, and interface equations.
Their differing rows are
$$
 \begin{array}{c|c|c}
 &\text{waist}&\text{outer}\\ \hline
 \text{original}&B(0)=0&d_B=0,\ d_C=0,\ c=0\\
 \text{replacement}&B(0)=0,\ m(0)+a(0)=0&d_B=0,\ d_C=0.
 \end{array}
 \tag{144.5}
$$
The full physical $B$ rows are retained. In the actual odd sector their
mean vanishes by exact symmetry; this does not remove the independent
even $C$ mean. A fixed genuine cap may equivalently be replaced by a
family of genuine caps supplied by the original exterior construction,
provided the same conditions hold for each member.

Put $a_0=a(0)$ and $m_0=m(0)$. The winding branch used throughout is
$$
                  m_0<0,\qquad |a_0/m_0+1|<1/2.
 \tag{144.6}
$$
This is a declared neighbourhood condition. It is not inferred from a
floating winding count.

## 2. Angular transport and the actual outer reference

For $w\in\mathbb R^3$, let $[w]_\times x=w\times x$. The angular and radial
connections are
$$
 N=\begin{pmatrix}0&-b&-aB\\ b&0&-aC\\aB&aC&0\end{pmatrix}
       =[(aC,-aB,b)]_\times,\qquad
 M=\begin{pmatrix}0&0&-eA\\0&0&-eB\\eA&eB&0\end{pmatrix}.
 \tag{144.7}
$$
Let $U(s,t)$ solve the right transport equation
$\partial_tU(s,t)=U(s,t)N(t)$ with $U(s,s)=I$. Every $U$ lies in $SO(3)$,
and $U(0,L)=U(0,s)U(s,L)$. Write $Q=U(0,L)$. Since $N$ has period $L$,
the full-circle transport is $Q^4$. The frame matrix itself may have
determinant $-1$ under $n=Y\times X$; its change-of-frame transport still
has determinant $1$.

The [actual rotational positive-cap reference](R133-actual-rotational-positive-cap-and-Codazzi-Jacobi-graph.md)
at the same $R=25/8$ has
$$
 B_\circ=0,\qquad
 C_\circ=-\frac{\sqrt{E-a'^2}}{a\sqrt E}<0,\qquad
                     b^2+a^2C_\circ^2=1.
 \tag{144.8}
$$
Thus $w_\circ=(aC_\circ,0,b)$ has length one,
$Q_\circ=\exp(L[w_\circ]_\times)$, and $\operatorname{tr}Q_\circ=1$.
The already proved reference bounds give
$$
 |C_\circ|>0.17053380>17/100,\qquad
 6.5637657879557\,10^{-6}<a(R)<6.5637657879724\,10^{-6}.
 \tag{144.9}
$$
These are reused exact reference enclosures, not a new execution.
The original compactly supported $\nu$ bump is zero near both endpoints.

The physical outer neighbourhood required for both body and cap is
$$
 \sup_\theta\sqrt{B(\theta)^2+(C(\theta)-C_\circ)^2}
                          \le\varepsilon\le1/1000.
 \tag{144.10}
$$
No raw moving $C^0$ state ball is automatically relabelled as (144.10).
Its actual moving-to-physical conversion must be justified.

## 3. Strict monotonicity of the quarter trace

Fix $B_*,C_*$ at this outer circle and let $B_t=B_*$, $C_t=C_*+t$.
Suppose the whole interval of $t$ being used lies in (144.10).
Set $\chi(t)=\operatorname{tr}Q_t$.

**Lemma 144.1.** On that entire interval,
$$
 \left|\chi'(t)+2La^2C_\circ\right|
                  \le2L^2a^2\varepsilon,\qquad
 \chi'(t)>\frac{3\pi}{20}a^2>0.
 \tag{144.11}
$$

**Proof.** For any two skew connections the exact right-transport
Duhamel identity is
$$
 U_1(s,t)-U_0(s,t)=
 \int_s^t U_1(s,\xi)(N_1-N_0)(\xi)U_0(\xi,t)\,d\xi.
 \tag{144.12}
$$
The transports are orthogonal and
$\|[w]_\times\|_{\rm op}=|w|$. Therefore
$$
 \|U_t(s,t')-U_\circ(s,t')\|_{\rm op}\le(t'-s)a\varepsilon.
 \tag{144.13}
$$
There is no exponential Gronwall factor.

Put $J=[e_1]_\times$. Parameter variation and cyclicity of trace give
$$
 \chi'(t)=a\int_0^L
       \operatorname{tr}\bigl(JU_t(s,L)U_t(0,s)\bigr)\,ds.
 \tag{144.14}
$$
Each product in (144.14) differs from
$U_\circ(s,L)U_\circ(0,s)=Q_\circ$ by at most $La\varepsilon$ in
operator norm. The nuclear norm of $J$ is $2$. Thus the total error in
replacing the product by $Q_\circ$ is at most $2L^2a^2\varepsilon$.
Rodrigues' formula gives
$$
 \operatorname{tr}(JQ_\circ)
       =-2(e_1\cdot w_\circ)\sin L=-2aC_\circ.
$$
This proves the first inequality. The second follows from
$$
 \chi'(t)\ge2La^2(|C_\circ|-L\varepsilon),\qquad
 17/100-11/7000>3/20,\qquad L<11/7.
$$
The variation formula also proves differentiability for continuous
bounded angular coefficients. $\square$

The trace in this lemma is the quarter trace. The full-circle trace has
zero first derivative at the identity and cannot replace it.

For the genuine cap, $Q_{\rm cap}^4=I$ implies
$\operatorname{tr}Q_{\rm cap}\in\{3,1,-1\}$. Equations (144.9),
(144.12)--(144.13) give
$$
 |\operatorname{tr}Q_{\rm cap}-1|\le3La\varepsilon<1,
 \qquad\hbox{hence}\qquad \operatorname{tr}Q_{\rm cap}=1.
 \tag{144.15}
$$
This does not identify the actual cap frame with the rotational frame.

When $d_B=d_C=0$, body and cap differ only by the constant $c$.
The full segment between them remains in (144.10) by convexity.
Consequently
$$
             \operatorname{tr}Q_{\rm body}(R)=1
                          \quad\Longleftrightarrow\quad c=0.
 \tag{144.16}
$$
The complete equalities $d_B=d_C=0$ are required for this reduction.

## 4. Gauss--Codazzi propagates this trace to the waist

Exact Gauss--Codazzi gives
$$
                         N_r-M_\theta+MN-NM=0.
 \tag{144.17}
$$
Let $V(r)$ be radial transport along $\theta=0$. Since the radial
connection has period $L$, compatibility around the quarter rectangle
gives
$$
                      Q(r)=V(r)^{-1}Q(0)V(r).
 \tag{144.18}
$$
One can prove this by reconstructing the compatible frame on the angular
universal cover and comparing the two orders of transport around the
rectangle. The radial transports at $\theta=0,L$ are the same $V$.

At the waist, $B(0)=0$ and $a'(0)=0$ give
$N(0,\theta)=a_0C(0,\theta)J$. These matrices commute, so (144.3) implies
$$
 Q(0)=\exp((La_0/m_0)J),\qquad
                  \operatorname{tr}Q(R)=1+2\cos(La_0/m_0).
 \tag{144.19}
$$

**Theorem 144.2.** For exact body and cap satisfying all common equations,
(144.6) and (144.10), the two nonlinear boundary systems (144.5) have the
same zero set.

**Proof.** The replacement condition $m_0=-a_0$ makes (144.19) equal to
one. Then (144.16) gives the missing outer mean equation. Conversely,
full original outer matching gives quarter trace one. Thus
$\cos(La_0/m_0)=0$. The branch (144.6) places its argument in
$(-3\pi/4,-\pi/4)$, whose unique cosine zero is $-\pi/2$.
Hence $m_0=-a_0$. $\square$

This is an equivalence theorem, not an existence theorem.

## 5. Zero translational holonomy and one geometric alignment

Assume $C(0,\theta)<0$, as in the actual chart $v<0$. Set
$$
 X_0=e_z,\quad
 \psi(\theta)=-a_0\int_0^\theta C(0,s)\,ds,\quad
 Y_0=(\cos\psi,\sin\psi,0),\quad n_0=Y_0\times X_0.
 \tag{144.20}
$$
The new mean condition and fourfold symmetry imply
$$
 \psi(\theta+L)=\psi(\theta)+L,\qquad
                   Y_0(\theta+L)=R_z(L)Y_0(\theta).
$$
Therefore
$$
 \int_0^{2\pi}a_0Y_0\,d\theta
 =\bigl(I+R_z(L)+R_z(2L)+R_z(3L)\bigr)
                            \int_0^L a_0Y_0\,d\theta=0.
 \tag{144.21}
$$
The last integral is horizontal, so the rotation sum does annihilate it.
Consequently $F_{0,\theta}=a_0Y_0$ has a periodic primitive. Take its
horizontal mean and height to be zero. The complete initial frame is
also periodic and obeys the correct angular connection.

This waist is strictly convex and simple. To verify the global assertion,
fix a point with tangent angle $\psi_*$ and its outward normal
$n_*=(\sin\psi_*,-\cos\psi_*,0)$. Along one full positively oriented
turn, the derivative of $(F_0-F_*)\cdot n_*$ is
$a_0\sin(\psi_*-\psi)$. It is strictly negative for the first half-turn
and strictly positive for the second. The scalar returns to zero only
at the period endpoint by (144.21), and is strictly negative in between.
Every tangent line is therefore a strict supporting line, and no two
distinct points in one period coincide. Here $\psi'>0$ and total turn
$2\pi$ were both used.

Now solve the exact radial frame and position equations
$$
                  \mathcal E_r=\mathcal E M,\qquad F_r=eX.
 \tag{144.22}
$$
Periodic coefficients and periodic initial data imply periodic frame
and periodic position at every radius by ODE uniqueness. Flatness gives
$\mathcal E_\theta=\mathcal E N$ and $F_\theta=aY$, as in
[R126](R126-exact-Codazzi-reconstruction-and-continuation.md).
Thus both rotational and translational holonomy vanish. An SO(3)-only
argument has not replaced the position calculation.

By Theorem 144.2 the complete outer $B,C$ traces match. Gauss gives the
same $A$ since $C\ne0$. Use one Euclidean rigid motion to align position
and full frame at one outer point. The angular ODE then aligns the
whole circle. The first and second jets match by the complete physical
trace theorem, so the attachment is $C^2$. The negative half is attached
by its already proved waist reflection. There is no second independent
world anchor and no deletion of the original height condition.

Fourfold symmetry is essential in (144.21). A periodic planar tangent
frame with turning number one does not alone force zero translation
period.

## 6. Complete off-shell identity and ordinary source norms

For arbitrary sufficiently regular piecewise fields with the same metric,
define
$$
 \begin{split}
 R_G&=AC-B^2-K,\\
 R_B&=B_r-\gamma A_\theta+2\beta B,\\
 R_C&=C_r-\gamma B_\theta-\beta(A-C).
 \end{split}
 \tag{144.23}
$$
Direct substitution into (144.7) yields
$$
 \mathcal F:=N_r-M_\theta+MN-NM
                         =[a(R_C,-R_B,eR_G)]_\times.
 \tag{144.24}
$$
In the two-field graph only $R_G$ vanishes identically by definition.
Neither Codazzi defect nor its mean is deleted.

Let $U_r(s,t)$ denote angular transport at radius $r$. Differentiating its
equation and using $M(r,L)=M(r,0)$ gives
$$
 \partial_rQ-QM(r,0)+M(r,0)Q
   =\int_0^L U_r(0,\theta)\mathcal F(r,\theta)
                                      U_r(\theta,L)\,d\theta.
 \tag{144.25}
$$
Indeed, subtract $UM(r,\theta)-M(r,0)U$ from $\partial_rU$.
The difference has zero angular initial value and angular derivative
equal to itself times $N$ plus $U\mathcal F$. Taking trace at $L$
eliminates the commutator.

Define
$$
 \mathcal I=\int_0^R\int_0^L
  \operatorname{tr}\bigl(U_r(0,\theta)\mathcal F(r,\theta)
                         U_r(\theta,L)\bigr)\,d\theta\,dr
                     +\sum_i[\operatorname{tr}Q]_{r_i}.
 \tag{144.26}
$$
Integrate on the open smooth pieces, and include exactly the actual
one-sided jumps. Telescoping gives
$\mathcal I=\operatorname{tr}Q(R)-\operatorname{tr}Q(0)$.

At the waist compare with the connection having the same $C(0)$ and
$B(0)=0$. At the outer boundary compare with
$(B_{\rm cap},C_{\rm cap}+c)$. Put
$$
 \begin{split}
 \mathcal E_w&=\operatorname{tr}Q(0)-[1+2\cos(La_0/m_0)],\\
 \mathcal E_o&=\operatorname{tr}Q(R)-\operatorname{tr}Q_{{\rm cap}+c},\\
 \mathcal B(c)&=\int_0^1\chi'(tc)\,dt,\qquad e_w=m_0+a_0,
 \end{split}
 \tag{144.27}
$$
where $\chi(t)=\operatorname{tr}Q_{{\rm cap}+t}$.
Each boundary error is an exact Duhamel difference. Since the genuine
cap has quarter trace one, exact subtraction gives
$$
 \boxed{\quad
 \mathcal B(c)c=2\sin(Le_w/m_0)+\mathcal E_w+\mathcal I-\mathcal E_o.
 \quad}
 \tag{144.28}
$$
No common residual has been set to zero. Whenever the constant-mean
interpolation itself remains in (144.10),
$\mathcal B(c)>3\pi a(R)^2/20$. With $d_B=d_C=0$ this follows by
convexity. For a general off-shell state it must be checked separately:
changing its nonmean boundary components back to those of the cap need
not stay within a neighbourhood established only at the original
body and cap endpoints.

Here $\|\cdot\|_2$ is the normalized physical quarter-circle $L^2$ norm,
and radial measure is $dr$. Since
$|\operatorname{tr}([z]_\times U)|\le2|z|$ for orthogonal $U$,
$$
 \begin{split}
 |\mathcal E_w|&\le2La_0\|B(0)\|_2,\\
 |\mathcal E_o|&\le2La(R)
                   (\|d_B\|_2^2+\|d_C\|_2^2)^{1/2},\\
 |\mathcal I_{\rm bulk}|&\le2L\int_0^R a(r)
       (\|R_C\|_2^2+\|R_B\|_2^2+e(r)^2\|R_G\|_2^2)^{1/2}\,dr.
 \end{split}
 \tag{144.29}
$$
For a jump across a continuous metric germ its added term is at most
$$
                 2La(r_i)(\|[C]_i\|_2^2+\|[B]_i\|_2^2)^{1/2}.
 \tag{144.30}
$$
An unaccounted metric jump also has a $[b]$ contribution to $N$; it is
not admissible in the original geometry.

These are ordinary physical $L^2$ contracts and contain all modes and
means. They do not freely extend to any negative-Sobolev source port.
That requires the corresponding exact dual transport-weight bounds.

## 7. Exact linear row operation at a genuine matched solution

At a true solution,
$c=e_w=\mathcal E_w=\mathcal I=\mathcal E_o=0$.
Allow variations of the state, genuine cap and original compactly
supported metric parameter, using the same physical angle. The endpoint
metric germs are unchanged by this $\nu$ direction. Differentiating
(144.28) gives
$$
 \boxed{\quad
 \mathcal B(0)\dot c
 =-\frac{\pi}{a_0}\dot m_0+
              \dot{\mathcal E}_w+\dot{\mathcal I}-\dot{\mathcal E}_o.
 \quad}
 \tag{144.31}
$$
If another permitted design variation changes $a_0$, the waist term
becomes $-\pi(\dot m_0+\dot a_0)/a_0$. That extension still requires the
appropriate endpoint-germ identities and a genuine periodic cap.

All extra terms in (144.31) are explicit linear functionals of the other
common residual rows. At a zero-residual base, differentiated transport
weights multiply zero defects. Thus:

* The bulk integrand in $\dot{\mathcal I}$ uses
  $[a(\dot R_C,-\dot R_B,e\dot R_G)]_\times$.
* $\dot{\mathcal E}_w$ uses $[(0,-a_0\dot B(0),0)]_\times$.
* $\dot{\mathcal E}_o$ uses $[a(R)(\dot d_C,-\dot d_B,0)]_\times$.
* Every interface contributes its complete variation with
  $[a(r_i)([\dot C]_i,-[\dot B]_i,0)]_\times$.

The boundary variation functional at radius $r$ is exactly
$$
       \int_0^L\operatorname{tr}
        \bigl(U_r(0,\theta)\dot N(\theta)U_r(\theta,L)\bigr)\,d\theta.
 \tag{144.32}
$$
Where these functionals are bounded on the chosen common data spaces,
(144.31) is a bounded invertible triangular row transformation:
its coefficients $\mathcal B(0)>0$ and $-\pi/a_0\ne0$ are nonzero.
Keeping every common row, either last row can be replaced by the other.
Kernels, surjectivity and indices then agree in that same realization.
No unpaid dual norm or unrelated source window is included in this claim.

For a true pure metric-$\nu$ response solving the full linearized
Gauss--Codazzi equations with the metric source, the common homogeneous
boundary rows, and all transmission conditions, (144.31) reduces to
$$
                  \dot c=-\frac{\pi}{a_0\mathcal B(0)}\dot m_0.
 \tag{144.33}
$$
For a true response satisfying the original complete outer mean row,
this in particular implies $\dot m_0=0$. For the saved proposal $Z$ or
a general forced field, all defect terms in (144.31) remain.
The zero-set derivative must not replace the derivative at an
approximate off-shell centre. Differentiating (144.28) at that centre
also differentiates its nonzero defects and their weights.

The coefficient $\mathcal B$ is of order $a(R)^2$ near this reference.
Its reciprocal may be large. Hence neither numerical conditioning nor
strong/weak source-port comparability improves automatically.

## 8. The actual candidate and remaining independent compatibility

The [actual waist-amplitude theorem](R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md)
defines the original complete centre by
$$
 v_c(0,\phi)=-a_0+\alpha\sum_{j=0}^{32}V_j\cos(4j\phi).
$$
The [saved exact rational certificate](../notes/2026-11-13-R133-final-waist-amplitude-chart-rational.json)
contains
$$
 \alpha=\frac{6890507429876859}{9007199254740992},\qquad
 V_0=\frac{1270129564654771}
              {158456325028528675187087900672}>0.
 \tag{144.34}
$$
Therefore its waist mean is $-a_0+\alpha V_0$, not exactly $-a_0$.
The [continuous response repair](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md)
has initial offset $e_0=0$ and preserves the saved response waist value.
For the selected centre $Q_\delta=Q_0+\delta Z$, its additional actual
waist response mean must also be retained; this theorem does not set
$\langle Z_2(0)\rangle$ to zero. A mean retraction changes the centre and
must carry its own full body residual and source transformation.

The final design in [the selected-parameter core theorem, Section 6](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md)
keeps the selected metric parameter fixed while solving the complete
regular BVP: every waist odd row and every outer nonmean/mean row,
including the fourth Robin row. The waist amplitude is an output to be
checked against the visible-geometry margin; this result does not add
a fixed-amplitude equation to that final BVP.

The mean replacement preserves the state/row count. Eliminating the
scalar mean from its new initial value removes one scalar state together
with its boundary row, not an independent design condition.
The true phase/waist-phase compatibility and any explicitly chosen
parameter Schur condition are not proved by the mean replacement.
An older fixed-amplitude bordered formulation can also use the row
identity when its other equations are retained, but its extra
normalization is not silently imposed on the final fixed-parameter BVP.

To use the replacement BVP, one must establish its actual outer
neighbourhood, branch, full equations, transmission and genuine cap.
After a solution is constructed, Section 5 gives the same periodic core
and $C^2$ attachment. Global embedding, reach, held motion,
noncongruence, the low/high cap entrance and exact far installation keep
their previous obligations. The final fixed-metric phase family remains
the one in the [frozen-metric and fixed-marker theorem](R133-supplement-frozen-metric-extrinsic-phase-and-fixed-marker-family.md).
This result does not yet construct an exact visible closed family.
