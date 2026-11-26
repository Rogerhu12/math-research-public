# R696 — Angular unit tangents with exact closed sections and the original core/cap ports

## Scope and fixed mathematical input

**Proved:** under the stated exact input and positivity assumptions, the representation, closed angular sections, angular Gram identity, and endpoint $C^2$ identities below. The remaining $E/B$ equations and existence are unresolved.

This is a new representation for the same fixed R690 scalar metric. It proves closure of every angular section, its angular metric identity, and the full core/reflection/cap port conditions. It does not assert existence of a solution of the remaining two metric equations, embedding, a reach bound, the required held displacement, or successful refinement. R692–R695 and the already implemented radial-unit representations are not relabeled as instances of this new finite space.

Let the exact scalar domain be $0\le s\le S$, with the same exact symbolic $S$ and scalar $a(s)>0$ as the current independent R690 reference. Write

$$b=a_s,\qquad c=+\sqrt{1-b^2},\qquad b^2+c^2=1.$$

The complete scalar law includes the original quintics, analytic segment, all Hold segments, and the entire new infinitely flat tail. Its endpoint jets are

$$a(0)=1,\quad b(0)=0,\quad c(0)=1,\quad c_s(0)=0,$$

$$a(S)=R,\quad b(S)=-1,\quad c(S)=0,\quad b_s(S)=c_s(S)=0.$$

All formulas below refer to these exact functions. Binary64 mesh, scalar, trigonometric, inverse-chart, and quadrature carriers are evaluation devices, not replacement definitions of the metric.

Fix the initial support coefficients $c_m^0$, the same material chart used to define this metric, and set $\nu_m=2m$,

$$\theta_0(\phi)=\phi+\sum_{m=1}^M\frac{1-\nu_m^2}{\nu_m}c_m^0\sin(\nu_m\phi),\qquad
\rho_0=\theta_0'>0.$$

The fixed target is

$$g=ds^2+a(s)^2d\theta_0^2
  =ds^2+a(s)^2\rho_0(\phi)^2d\phi^2.$$

The current core coefficients $c_m$ remain free except for the same originally fixed first three. Define

$$p_c(\psi)=1+\sum_{m=1}^M c_m\cos(\nu_m\psi),\qquad
\rho_c=p_c+p_c''>0,$$

$$\Theta_c(\psi)=\psi+\sum_{m=1}^M\frac{1-\nu_m^2}{\nu_m}c_m\sin(\nu_m\psi),\qquad
\Gamma_c(\psi)=p_c e_r(\psi)+p_c'e_t(\psi).$$

The real lift $\psi=\psi_c(\phi)$ is defined by $\Theta_c(\psi)=\theta_0(\phi)$. Strict positivity of both full angular densities is an assumption of this exact representation. Sample positivity in a numerical driver is not a proof of that assumption.

Use $e_r(\alpha)=(\cos\alpha,\sin\alpha,0)$, $e_t(\alpha)=(-\sin\alpha,\cos\alpha,0)$, and $e_z=(0,0,1)$ throughout. In particular, the current support curve uses the current normal angle $\psi$, whereas the fixed material coordinate is $\theta_0$.

## The complete angular field and its symmetries

Put

$$\eta(s)=10(s/S)^3-15(s/S)^4+6(s/S)^5,\qquad \lambda=1-\eta,$$

$$\delta(\phi)=\psi_c(\phi)-\theta_0(\phi),\qquad
\beta(s,\phi)=\theta_0(\phi)+\lambda(s)\delta(\phi).$$

Both first and second derivatives of $\eta$ and $\lambda$ vanish at both endpoints. The base unit vector is $E=e_t(\beta)$. Choose a full rotation field with the original axial parity pattern,

$$\begin{aligned}
\Omega_x(s,\phi)&=\sum_{m=0}^{M}x_m(s)\sin((2m+1)\phi),\\
\Omega_y(s,\phi)&=\sum_{m=0}^{M}y_m(s)\cos((2m+1)\phi),\\
\Omega_z(s,\phi)&=\sum_{m=1}^{M}z_m(s)\sin(2m\phi).
\end{aligned}$$

Define

$$V=\exp([\Omega]_\times)E,\qquad W=\rho_0V.$$

Thus $|V|=1$ exactly. This is the angular unit tangent; it is not the radial unit tangent from R692. The coefficient names $z_m$ in $\Omega_z$ do not denote the separate vertical translation profile used below.

Let $P=\operatorname{diag}(-1,-1,1)$ be a half turn about the vertical axis and $S_y=\operatorname{diag}(1,-1,1)$. The even support frequencies and the unique real inverse lift imply

$$\psi(-\phi)=-\psi(\phi),\qquad \psi(\phi+\pi)=\psi(\phi)+\pi,$$

and the identical identities hold for $\theta_0$. The rotation coefficients give

$$\Omega(\phi+\pi)=P\Omega(\phi),\qquad
\Omega(-\phi)=-S_y\Omega(\phi).$$

Under an orthogonal transformation $Q$, the axial vector transforms by $\det(Q)Q$. Consequently the exponential rotation transforms by conjugation. Since

$$E(\phi+\pi)=PE(\phi),\qquad E(-\phi)=-S_yE(\phi),$$

we obtain

$$W(\phi+\pi)=PW(\phi),\qquad W(-\phi)=-S_yW(\phi),$$

$$W(\pi-\phi)=-PS_yW(\phi)=\operatorname{diag}(1,-1,-1)W(\phi).$$

The horizontal components of the full-circle integral cancel under the half turn; the vertical component cancels under reflection. Hence

$$\int_0^{2\pi}W(s,\phi)\,d\phi=0$$

for every $s$ and every allowed coefficient field, without a root solve. The second reflection also gives

$$\int_0^\pi W_y\,d\phi=\int_0^\pi W_z\,d\phi=0,\qquad
\int_0^\pi W_x\,d\phi=2\int_0^{\pi/2}W_x\,d\phi.$$

## Centered primitive and all of its radial derivatives

For any vector field with these parities, use the linear primitive

$$\mathcal C[W](\phi)=\int_0^\phi W(v)\,dv
       -e_x\int_0^{\pi/2}W_x(v)\,dv.$$

Set $C=\mathcal C[\rho_0V]$. The integration constant is part of the definition. Its dependence on $s$ must not be omitted when differentiating. Since the fixed chart does not vary with $s$,

$$\begin{aligned}
C_s&=\int_0^\phi\rho_0 V_s\,dv-e_x\int_0^{\pi/2}\rho_0(V_s)_x\,dv,\\
C_{ss}&=\int_0^\phi\rho_0 V_{ss}\,dv-e_x\int_0^{\pi/2}\rho_0(V_{ss})_x\,dv.
\end{aligned}$$

In particular $C_\phi=\rho_0V$, $C_{s\phi}=\rho_0V_s$, and

$$C_{\phi\phi}=\rho_0'V+\rho_0V_\phi.$$

The integral identities above imply

$$C(\phi+2\pi)=C(\phi),\qquad C(\phi+\pi)=PC(\phi),\qquad C(-\phi)=S_yC(\phi).$$

Also $C(\pi-\phi)=\operatorname{diag}(-1,1,1)C(\phi)$. These formulas, including their $s$ derivatives, are exact. The chosen primitive has $C_z(s,0)=0$; its vertical additive constant has not been left as an untracked function of $s$.

## Independent vertical freedom and free cap height

Define the exact scalar primitive

$$I(s)=\int_0^s c(t)\,dt,\qquad I_*=I(S).$$

Choose a fixed exact $0<\varepsilon<S$; the concrete first choice is $\varepsilon=1/20$. Let $w(s)=10(s/\varepsilon)^3-15(s/\varepsilon)^4+6(s/\varepsilon)^5$ for $0\le s\le\varepsilon$ and $w(s)=1$ thereafter. Define a second fixed scalar primitive and the height basis

$$J(s)=\int_0^s c(t)w(t)\,dt,\qquad J_*=J(S)>0,\qquad h(s)=J(s)/J_*.$$

The symbol $J$ here denotes a scalar integral; it is not a residual Jacobian. The functions $h$ and $\eta$ are different: $\eta$ enters the angular interpolation through $\lambda$, whereas $h$ controls the free height. Their endpoint values and first two endpoint derivatives agree. Indeed

$$h_s=\frac{cw}{J_*},\qquad h_{ss}=\frac{c_sw+cw_s}{J_*},$$

so $h(0)=0$, $h(S)=1$, and $h_s=h_{ss}=0$ at both endpoints. Positivity of $J_*$ follows if $c$ has positive integral on some interval after $\varepsilon$; the intended strictly positive open-interval scalar branch satisfies this.

Retain an independent free height $H$ and an independent **purely radial** scalar profile $r(s)$ whose value, first derivative, and second derivative are zero at both endpoints. Set

$$z(s)=I(s)+h(s)(H-I_*)+r(s),\qquad F(s,\phi)=a(s)C(s,\phi)+z(s)e_z.$$

Then

$$\begin{aligned}
z_s&=c+h_s(H-I_*)+r_s,\\
z_{ss}&=c_s+h_{ss}(H-I_*)+r_{ss},\\
\partial_HF&=h e_z,\qquad
\partial_HF_s=h_s e_z,\qquad
\partial_HF_{ss}=h_{ss}e_z.
\end{aligned}$$

Thus $z(0)=0$, $z_s(0)=1$, $z_{ss}(0)=0$, $z(S)=H$, and $z_s(S)=z_{ss}(S)=0$. All original free core coefficients and the original free height remain optimization variables. The full scalar profile $r$ is additional freedom. Replacing the exact primitive $I$ by an exact finite quintic in the mathematical definition would discard the infinitely flat scalar tail and is not the construction stated here. A working quadrature for $I$ must be recorded with its own error; its first and second exact jets are still $c$ and $c_s$.

For the phase family obtained after a candidate has been fixed, the same $H$ and the same caps are used at every phase. Freedom of $H$ during the search does not mean $H$ changes along that family.

## Full six jets and the three metric entries

The true six jets are

$$\begin{aligned}
F&=aC+ze_z,\\
F_s&=bC+aC_s+z_se_z,\\
F_\phi&=a\rho_0V,\\
F_{ss}&=b_sC+2bC_s+aC_{ss}+z_{ss}e_z,\\
F_{s\phi}&=\rho_0(bV+aV_s),\\
F_{\phi\phi}&=a(\rho_0'V+\rho_0V_\phi).
\end{aligned}$$

In the orthonormal target basis $(\partial_s,(a\rho_0)^{-1}\partial_\phi)$, the complete relative Gram error is therefore

$$\begin{pmatrix}
 |bC+aC_s+z_se_z|^2-1 &(bC+aC_s+z_se_z)\cdot V\\
 (bC+aC_s+z_se_z)\cdot V&0
\end{pmatrix}.$$

The angular equation is an exact identity of the continuous definition. Both remaining entries must be solved. A numerical implementation must still compute all three actual Gram entries of its working six jets; it cannot silently replace a nonzero working angular defect by zero or assign its evaluation error a zero bound.

The base and rotation jets needed for these formulas are explicit. At fixed $\phi$,

$$\beta_s=\lambda_s\delta,\quad \beta_{ss}=\lambda_{ss}\delta,\quad
\beta_\phi=\rho_0\left(1-\lambda+\frac{\lambda}{\rho_c(\psi)}\right).$$

Moreover

$$\psi_\phi=\frac{\rho_0}{\rho_c(\psi)},\qquad
\psi_{\phi\phi}=\frac{\rho_0'}{\rho_c(\psi)}
             -\frac{\rho_0^2\rho_c'(\psi)}{\rho_c(\psi)^3},$$

$$\beta_{\phi\phi}=(1-\lambda)\rho_0'+\lambda\psi_{\phi\phi},\qquad
\beta_{s\phi}=\lambda_s(\psi_\phi-\rho_0).$$

For $R_\Omega=\exp([\Omega]_\times)$,

$$\begin{aligned}
E_s&=-\beta_s e_r(\beta),&
E_{ss}&=-\beta_{ss}e_r(\beta)-\beta_s^2 e_t(\beta),&
E_\phi&=-\beta_\phi e_r(\beta),\\
(R_\Omega)_s&=D\exp_{[\Omega]_\times}[[\Omega_s]_\times],&&&\\
(R_\Omega)_{ss}&=D\exp_{[\Omega]_\times}[[\Omega_{ss}]_\times]
  +D^2\exp_{[\Omega]_\times}[[\Omega_s]_\times,[\Omega_s]_\times],&&&
\end{aligned}$$

and $(R_\Omega)_\phi=D\exp_{[\Omega]_\times}[[\Omega_\phi]_\times]$. Hence

$$\begin{aligned}
V_s&=(R_\Omega)_sE+R_\Omega E_s,\\
V_{ss}&=(R_\Omega)_{ss}E+2(R_\Omega)_sE_s+R_\Omega E_{ss},\\
V_\phi&=(R_\Omega)_\phi E+R_\Omega E_\phi.
\end{aligned}$$

No third radial derivative of a shared quintic is required for these six jets. Complete first variations of the field and its six jets include the centered primitive, all free rotation and scalar coefficients, $H$, and the current inverse chart. In particular

$$D\psi[dc]=-
 \frac{\sum_m(1-\nu_m^2)\,dc_m\sin(\nu_m\psi)/\nu_m}{\rho_c(\psi)}.$$

The inverse-chart residual of a finite numerical root iteration must be reported and paid separately. Differentiating a truncated root iteration is not, by itself, a proof of the exact implicit derivative above.

## Core, reflected half, and cap: all endpoint jets

Impose on the rotation coefficient field

$$\Omega(0,\phi)=\Omega_s(0,\phi)=0,\qquad
\Omega_{ss,x}(0,\phi)=\Omega_{ss,y}(0,\phi)=0,$$

with the full $z$-component of $\Omega_{ss}(0,\phi)$ free, and impose

$$\Omega(S,\phi)=\Omega_s(S,\phi)=\Omega_{ss}(S,\phi)=0.$$

At the core, $\beta=\psi$, $V=e_t(\psi)$, and $\rho_0V=\partial_\phi\Gamma_c(\psi)$. The endpoint values $\Gamma_c(0)=(1+\sum c_m,0,0)$ and $\Gamma_c(\pi/2)_x=0$ show that the centered primitive is exactly $C(0,\phi)=\Gamma_c(\psi)$, with no missing translation. Since $\lambda_s=\lambda_{ss}=0$ there, $V_s=0$ and $V_{ss}=\Omega_{ss}\times e_t(\psi)$ is horizontal. Thus $C_s=0$ and $(C_{ss})_z=0$ at the core, including the differentiated centering constant. The six jets at $s=0$ are

$$\begin{aligned}
F&=\Gamma_c(\psi),& F_s&=e_z,&F_\phi&=\rho_0e_t(\psi),\\
F_{ss}&=b_s(0)\Gamma_c(\psi)+C_{ss}(0,\phi),&
F_{s\phi}&=0,&
F_{\phi\phi}&=\rho_0'e_t(\psi)-\frac{\rho_0^2}{\rho_c(\psi)}e_r(\psi).
\end{aligned}$$

In particular $F_z=0$, $(F_s)_{x,y}=0$, and $(F_{ss})_z=0$. Therefore extending by $F(-s,\phi)=S_zF(s,\phi)$, $S_z=\operatorname{diag}(1,1,-1)$, gives the required $C^2$ reflected join. The mixed jet agrees because $F_s(0,\phi)=e_z$ is independent of $\phi$.

At the cap, $\beta=\theta_0$ and all first and second radial jets of $V$ vanish. The primitive of $\rho_0e_t(\theta_0)$ is exactly $e_r(\theta_0)$ under the same centering convention. Thus $C=e_r(\theta_0)$, $C_s=C_{ss}=0$. The six jets at $s=S$ are

$$\begin{aligned}
F&=Re_r(\theta_0)+He_z,& F_s&=-e_r(\theta_0),&
F_\phi&=R\rho_0e_t(\theta_0),\\
F_{ss}&=0,&F_{s\phi}&=-\rho_0e_t(\theta_0),&
F_{\phi\phi}&=R\bigl(\rho_0'e_t(\theta_0)-\rho_0^2e_r(\theta_0)\bigr).
\end{aligned}$$

These are the same flat inward collar jets to which the fixed R661 graph cap attaches in $C^2$. The lower cap follows by the same reflection. The graph recipe, true radius, and chosen height must remain bound to this same field; no old cap/embedding certificate is inherited merely from this calculation.

## The finite space, its norm, and its precise coverage

Use shared $C^2$ quintics on the same exact affine radial mesh. For each of the $2(M+1)$ odd horizontal channels the two endpoint triples are zero, leaving $3J-6$ free scalar slots. Each of the $M$ even vertical rotation channels retains the core second derivative and has $3J-5$ free slots. The scalar $r$ has $3J-6$ free slots. The original $M-3$ core coefficients and one $H$ are also free. The total is

$$2(M+1)(3J-6)+M(3J-5)+(3J-6)+(M-3)+1.$$

For $J=923,M=160$, this is $1,334,847$ variables: $1,331,926$ rotation variables, $2,763$ scalar-profile variables, $157$ core variables, and one height. All of these must be included in the declared residual Jacobian, transpose, constraints, and norm. This packing is not the old radial-unit packing and is not a bijection with the old $q$ space.

A concrete new positive norm can use the declared node masses $v_j>0$, radial scale $\ell>0$, actual channel frequencies $k$, and $\sigma(k)^2=1+(k/24)^2$:

$$\begin{aligned}
\|d\|_{\mathcal H}^2={}&
\sum_{j,\mathrm{channels}}v_j\sigma(k)^2
 (d\Omega_j^2+\ell^2d\Omega_{s,j}^2+\ell^4d\Omega_{ss,j}^2)\\
&+\sum_jv_j(dr_j^2+\ell^2dr_{s,j}^2+\ell^4dr_{ss,j}^2)
 +\sum_{m>3}(1-\nu_m^2)^2dc_m^2+dH^2.
\end{aligned}$$

The sums include every free slot and no constrained endpoint slot. Positive Voronoi node masses on the chosen numerical carrier define an explicit positive node-jet norm; that choice is not asserted to equal an exact Sobolev integral. A different exact-integral norm would need its own explicit identity and coordinate/transpose maps. The original physical $q$ norm and its damping units are not claimed unchanged. Any chosen $\ell$, angular transition, norm identity, damping, and quadratic-solver budget must be reported as parameters of this new problem.

Interior rotations retain the usual stabilizer redundancy. At a general rotation chart value, its infinitesimal description uses the right Jacobian of the exponential: $J_r(\Omega)d\Omega$ parallel to $E$ gives the stabilizer direction. It is not globally correct to identify the gauge with literal $d\Omega\parallel E$. A positive damping term in all the new norm coordinates can control the retained redundancy; no gauge variable is silently removed.

There is a conditional continuous local-chart statement. Consider a sufficiently regular exact isometric embedding with these core/cap/reflection and dihedral ports; assume the angular and mixed derivatives used above exist classically, and its angular unit tangent is nowhere antiparallel to the chosen $E$. The shortest rotation taking $E$ to that tangent gives a continuous local rotation field with the stated axial symmetries. At the core, $F_s=e_z$ implies $V_s=0$, and $(F_{ss})_z=0$ implies $(V_{ss})_z=0$; the shortest chart then has the stated core endpoint jets. At the cap, the flat collar jets imply $V_s=V_{ss}=0$, hence the cap rotation triple is zero. The centered primitive reconstructs the horizontal part uniquely under the two vertical-plane symmetries; its vertical integration constant is $F_z(s,0)$. Taking $H=F_z(S,0)$ and $r=z-I-h(H-I_*)$ supplies the stated scalar profile and endpoint jets.

This local statement concerns the continuous rotation/profile space with these classical derivatives, for example the needed jets of a $C^4$ embedding. It is not a theorem that every $C^2$ isometry admits these classical mixed derivatives, nor that one finite Fourier/shared-quintic space contains every such embedding. Approximation, a common fixed target, and successful refinement remain separate tasks.

## A concrete initial branch and remaining obligations

At $\Omega=0$ the sections are planar and

$$\beta_\phi=\rho_0\left(1-\lambda+\frac{\lambda}{\rho_c}\right)>0.$$

Their tangent turns exactly once, since both endpoint charts have winding one. For a fixed unit normal $e_r(\alpha)$, the derivative of the projection of $C$ is $-\rho_0\sin(\beta-\alpha)$. The strictly increasing angle $\beta$ makes exactly one full turn. Therefore this projection has one maximum and one minimum on the circle. At the unique maximum the supporting line is perpendicular to $e_r(\alpha)$. Two distinct parameters cannot represent the same point: the supporting line at either parameter would then have two maximizing parameters. Thus the curve is a strictly convex Jordan curve, with perimeter $2\pi$ before multiplication by $a(s)$.

The modified height basis permits a low, monotone seed without adding a necessary lower bound $H\ge I_*$. With $r=0$,

$$z_s=c\left(1+\frac{H-I_*}{J_*}w\right),\qquad
D_*:=I_*-J_*=\int_0^\varepsilon c(t)(1-w(t))\,dt\le\varepsilon.$$

If $H\ge I_*$ the factor is at least one. If $\varepsilon<H<I_*$, its minimum over $0\le w\le1$ is $(H-D_*)/J_*>0$. Hence every $H>\varepsilon$ gives $z_s\ge0$, and gives $z_s>0$ wherever $c>0$. More generally, strict increase follows if $c$ has positive integral on every nonempty open subinterval. The intended R690 branch has $c>0$ at every interior point. The original declared numerical height floor greater than one is already stronger than $H>1/20$; no new algorithmic height gate is needed.

Distinct sections therefore occupy distinct horizontal planes, giving an explicit injective body seed at $\Omega=0,r=0$ for such a height. Its core reflection and fixed cap still have to be checked together with the marked geometry and quantitative budgets. In particular $H$ may be chosen below $I_*$ using an independently established necessary chord bound for the same core and metric. This is a seed construction, not a restriction imposed on all exact isometries. A finite quadrature for $I,J$ still needs its declared evaluation error. No small-metric-error claim follows from the seed embedding.

This representation is intended to trade the difficult radial closure correction for exact angular closure and an exact angular metric. The two remaining nonlinear equations can still be hard. All same-field global geometry, the held displacement, and Euclidean-quotient nontriviality remain necessary. Nonzero fixed core coefficients alone are not a substitute for those checks.

Once a candidate actually solves the fixed rotational metric and all required geometry has been established, the earlier material-phase mechanism applies: shift the material angle and apply the compensating ambient vertical rotation. The rotational caps remain fixed pointwise with the same $H$. This note supplies neither that candidate nor a new certificate for the quantitative amplitude/reach requirements.

## Implementation contract

An executable successor must have a new complete representation schema and source binding. It may consume the actual independent reference input, fixed chart, complete observation measure, and supplied historical addresses, but cannot present an old radial-unit report as its own parent. The literal old angle addresses can be reread as the same frozen-chart parameter addresses with their previously declared interpretation; no old physical values or certificates transfer.

The working angular primitive must include the centered integral and both of its radial derivatives. Its quadrature error, finite inverse-chart residual, exact-domain/carrier differences, and all rounding are actual costs. Complete original curvature rows, both amplitude-distance branches, height/cap rows, all permanent locations, and true nonlinear screening remain in force. Phase I can minimize common physical constraint violation; its slack is not feasibility of the true field. All scientific computation is restricted to the authorized public Actions environment. No scientific run is asserted by this derivation.
