# R205. Complete bent-annulus cut lifting with a fixed inner collar

**Status: proved representation and gluing identities; the finite prefix candidates remain unsolved.** This result supplies a new complete reference. It does not infer an isometry, embedding, or global reach from local or sampled residuals.

## 1. Exact tail and true cuff height

Use the R128 tail with
$$
a_c=4/5,\quad r_c=8/25,\quad c_f=17/50,\quad L=a_c-c_f=23/50.
$$
Let $S_9(t)=126t^5-420t^6+540t^7-315t^8+70t^9$ on $[0,1]$, extended by zero and one. For a frozen design amplitude $0\le A\le6/5$, put
$$
\alpha_A(y)=\operatorname{sgn}(y)A S_9((|y|-c_f)/L),\quad
C_A(y)=\int_0^y\cos\alpha_A(v)\,dv,\quad
H_A(y)=\int_0^y\sin\alpha_A(v)\,dv .
\tag{1}
$$
The actual upper annulus is
$$
F_A(r,u)=(r\cos u,C_A(r\sin u),Z_c-H_A(r\sin u)),
\qquad r_c\le r\le a_c.
\tag{2}
$$
Here $Z_c$ is the **inner flat cuff plane height**, not the outer cut mean.

For $r<c_f$, (2) is exactly $(r\cos u,r\sin u,Z_c)$. In Cartesian material coordinates, $F_x=(1,0,0)$ and $F_y=(0,\cos\alpha_A,-\sin\alpha_A)$ are orthonormal. Thus the metric is exactly $dr^2+r^2du^2$ for every $A$. Since $\cos\alpha_A>0$, the map is embedded. The clipped polynomial is $C^4$, which gives more than the required surface regularity.

With $k=\alpha_A'$ and inward coordinate $s_{\rm tail}=a_c-r$, the orthonormal second form is
$$
(l,m,n)=(k\sin^2u,-k\sin u\cos u,k\cos^2u).
\tag{3}
$$
The principal curvatures are $0,k$, with $0\le k\le315A/(128L)$. R128 gives the complete Cartesian two-jets, including axes where a component of (3) vanishes; no division by such a component is used.

## 2. Frozen scalar background and complete reference angles

Let $s\in[0,S]$, with an exact central cylinder $0\le s\le c$. Write the frozen B32 scalar radius as $a_0(s)$ and its background center height as $Z_0(s)$. Here $a_0$ denotes a function, not only the central constant. Its accurate terminal jets are
$$
a_0(S)=a_c,\quad a_0'(S)=-1,\quad a_0''(S)=0,\quad
Z_0'(S)=Z_0''(S)=0.
\tag{4}
$$
The R187 complete reference angles $(\Theta_0,\Phi_0)$ give the normalized central ellipse and agree through two radial derivatives with the circular flat reference $(u,0)$ at the cut.

Use the explicit R196 cubic basis $B_j(s)$, extended by zero with value, first derivative and second derivative zero at $c,S$. Put
$$
\chi(s)=S_5((s-c)/(S-c)),\qquad S_5(t)=10t^3-15t^4+6t^5
\tag{5}
$$
with constant extensions. Then $\chi',\chi''$ vanish at the endpoints. The radius design is
$$
a(s)=a_0(s)+\sum_j\rho_jB_j(s).
\tag{6}
$$
Changing $\rho$ changes the target metric. All new reference terms below use the **frozen** $a_0(s)$, not (6); this explicit choice is part of the definition.

The normalized angular tangent of (2) is
$$
T_A(r,u)=(-\sin u,\cos\alpha_A(r\sin u)\cos u,
-\sin\alpha_A(r\sin u)\cos u).
\tag{7}
$$
Use spherical angles
$$
T(\Theta,\Phi)=(-\sin\Theta\cos\Phi,\cos\Theta\cos\Phi,\sin\Phi).
$$
The horizontal norm in (7) is at least $\cos A>0$. Moreover its horizontal dot product with $(-\sin u,\cos u)$ is
$$
\sin^2u+\cos\alpha_A(r\sin u)\cos^2u>0.
$$
Consequently the relative angle $\Theta_A(r,u)-u$ is an explicit single-valued periodic atan2 with positive denominator; there is no unwrapping choice. The latitude $\Phi_A$ is regular. This defines full-circle angles, not merely quarter samples.

Define
$$
\begin{aligned}
\Theta_{\rm ref}&=\Theta_0+\chi\bigl(\Theta_A(a_0(s),u)-u\bigr),\\
\Phi_{\rm ref}&=\Phi_0+\chi\Phi_A(a_0(s),u),\\
\Theta&=\Theta_{\rm ref}+\sum_{j,k}\theta_{jk}B_j\sin(2ku),\\
\Phi&=\Phi_{\rm ref}+\sum_{j,k}\phi_{jk}B_j\sin(2ku).
\end{aligned}
\tag{8}
$$
All angular functions are evaluated completely. The additional functions of an explicitly reflection-relaxed representation can be added under the same endpoint-zero-jet convention.

For use without angular inverse differentiation, with $r=r(s)$ put
$$
\alpha_s=kr_s\sin u,\quad
\alpha_{ss}=\alpha_A''(r\sin u)r_s^2\sin^2u+kr_{ss}\sin u,\quad
\alpha_u=kr\cos u.
$$
Then
$$
\begin{aligned}
T_s&=(0,-\sin\alpha\,\alpha_s\cos u,-\cos\alpha\,\alpha_s\cos u),\\
T_{ss}&=(0,-(\cos\alpha\,\alpha_s^2+\sin\alpha\,\alpha_{ss})\cos u,
(\sin\alpha\,\alpha_s^2-\cos\alpha\,\alpha_{ss})\cos u),\\
T_u&=(-\cos u,-\cos\alpha\sin u-\sin\alpha\,\alpha_u\cos u,
\sin\alpha\sin u-\cos\alpha\,\alpha_u\cos u).
\end{aligned}
\tag{9}
$$
These explicit tail-reference formulas impose no $C^3$ requirement on an arbitrary solved prefix.

## 3. The necessary mean-height subtraction

Let $Q=\pi/2$. The linear R188 quarter primitive is
$$
\begin{aligned}
(\Pi T)_x(u)&=\int_0^uT_x-\int_0^QT_x,\\
(\Pi T)_y(u)&=\int_0^uT_y,\\
(\Pi T)_z(u)&=\int_0^uT_z-Q^{-1}\int_0^Q(Q-v)T_z(v)\,dv .
\end{aligned}
\tag{10}
$$
Its vertical quarter mean is zero; the D2 extension gives the full periodic position.

Define
$$
M(r,A)=Q^{-1}\int_0^Q H_A(r\sin u)\,du
=-\frac rQ\int_0^Q(Q-u)(T_A(r,u))_z\,du .
\tag{11}
$$
The second equality is integration by parts, using $H_A(0)=0$. It avoids nested position integrals. Set $M_0(s)=M(a_0(s),A)$ and define
$$
Y=\Pi T,\qquad
Z(s)=Z_0(s)+\sum_j z_jB_j(s)+z_c\chi(s)-\chi(s)M_0(s),
\qquad X=aY+Ze_z.
\tag{12}
$$
The true fixed-cuff plane height is
$$
\boxed{Z_c=Z_0(S)+z_c.}
\tag{13}
$$
The last term of (12), including its full first and second radial derivatives, is indispensable. Omitting it changes the cut position and radial jets.

Since $Y_u=T$,
$$
X_u=aT,\qquad |X_u|^2=a^2.
\tag{14}
$$
The remaining equations $|X_s|^2=1$ and $X_s\cdot T=0$ remain to be solved.

## 4. Complete endpoint two-jet proof

At the central cylinder, $\chi$ and all finite basis corrections vanish with the stated jets, so the normalized ellipse cylinder is unchanged.

At $S$, (4), (5), and the vanishing basis jets make $T,T_s,T_{ss}$ agree with (7) along $r(s)=a_c-(s-S)$ through the required order. Exact integration commutes with these derivatives. Directly from (7) and (10),
$$
Y(S,u)=\left(\cos u,\frac{C_A(a_c\sin u)}{a_c},
\frac{M(a_c,A)-H_A(a_c\sin u)}{a_c}\right).
\tag{15}
$$
Equations (12) and (15) give precisely (2). Differentiating the same identities gives $X_s$ and $X_{ss}$; (14) and (9) give $X_u,X_{su},X_{uu}$. Thus the entire Cartesian two-jet
$$
(X,X_s,X_u,X_{ss},X_{su},X_{uu})
\tag{16}
$$
matches the real annulus. No missing entry is inferred from only $n,m$.

The outer section mean and its inward derivatives are
$$
\left(Z_c-M(a_c,A),\
-\partial_sM(a_0(s),A)|_S,\
-\partial_s^2M(a_0(s),A)|_S\right),
\tag{17}
$$
and their derivatives with respect to $z_c$ are $(1,0,0)$. This mean is not the plane height (13).

The exact quarter symmetry of the reference and of the sine corrections gives matching angular jets under the D2 reflections. At a quarter endpoint the tail angle differences have the corresponding odd parity; the reference is flat near $u=0$ and regular at $u=\pi/2$. Hence the full periodic map has the claimed $C^2$ regularity, including the axes and the two radial seams.

## 5. All original finite columns and the external amplitude direction

For any original finite parameter direction, the new reference is fixed. Write $q^1=\Theta,q^2=\Phi$ and $T_a,T_{ab},T_{abc}$ for angular derivatives of $T$. Ordinary chain differentiation gives
$$
\begin{aligned}
\delta T&=T_a\delta q^a,\\
\delta T_s&=T_a\delta q_s^a+T_{ab}q_s^a\delta q^b,\\
\delta T_{ss}&=T_a\delta q_{ss}^a+2T_{ab}q_s^a\delta q_s^b
 +T_{ab}q_{ss}^a\delta q^b+T_{abc}q_s^aq_s^b\delta q^c,\\
\delta T_u&=T_a\delta q_u^a+T_{ab}q_u^a\delta q^b.
\end{aligned}
\tag{18}
$$
Repeated indices range over the two angles. The third angular tensors are parameter derivatives, not radial $C^3$ assumptions.

Put $\delta Y=\Pi\delta T$ and commute derivatives with the exact primitive. Then
$$
\begin{aligned}
\delta X&=\delta aY+a\delta Y+\delta Z e_z,\\
\delta X_s&=\delta a_sY+\delta aY_s+a_s\delta Y+a\delta Y_s+\delta Z_s e_z,\\
\delta X_{ss}&=\delta a_{ss}Y+2\delta a_sY_s+\delta aY_{ss}
+a_{ss}\delta Y+2a_s\delta Y_s+a\delta Y_{ss}+\delta Z_{ss}e_z,\\
\delta X_u&=\delta aT+a\delta T,\\
\delta X_{su}&=\delta a_sT+\delta aT_s+a_s\delta T+a\delta T_s,\\
\delta X_{uu}&=\delta aT_u+a\delta T_u.
\end{aligned}
\tag{19}
$$
Every original theta, phi, height, cut-height, and radius column is present. The metric residuals use these actual variations. For curvature, if $W=X_s\times X_u\ne0$, use
$$
\delta W=\delta X_s\times X_u+X_s\times\delta X_u,\qquad
\delta N=(I-NN^\top)\delta W/|W|.
$$
Differentiation of the actual Gram matrix and $N\cdot X_{ij}$, followed by the R191 symmetric shape-operator hinge, gives the complete curvature derivative. No formal second-form surrogate is substituted.

For an external amplitude variation,
$$
q_A=\chi(\partial_A\Theta_A,\partial_A\Phi_A),\qquad
Z_A=-\chi\,\partial_A M_0,\qquad a_A=0.
\tag{20}
$$
Its radial and angular jets are supplied, so (18)–(19) apply without new formulas. The current finite factory freezes $A$; it does not silently append a global column or pretend the old one-border solver already handles it.

## 6. Common-metric phase orbit and fixed caps

Fix one solved prefix and amplitude $A$, then apply the same space/material phase to both pieces:
$$
X_\tau(s,u)=R_\tau X(s,u-\tau),\qquad
F_{A,\tau}(r,u)=R_\tau F_A(r,u-\tau).
\tag{21}
$$
The outer seam remains matched through (16). On $r<c_f$, the tail is a round planar annulus, so (21) fixes every material point. The fixed caps attach at $r_c=.32$, not to the moving noncircular outer cut at $.8$.

The target metric is invariant under the material shift. A solved prefix therefore gives a common-metric orbit; a proved relative metric-error bound transports unchanged. The maps depend continuously in $C^2$ on phase. This does not make arbitrary changes of $A$ into solved isometric prefix families.

Fill the two inner cuffs by their flat disks to form the original closed kernel. Under the existing R113 hypotheses—global reach of that entire kernel at least $R$, actual $|z|\le Z_c$, and the stated cap dimensions—the complete collar/cap normal-ball proof applies. It needs the flat disk and an open collar, not a flat region extending to $.8$. Thus $.34>.32$ is enough. The detailed consumer is notes/2026-11-13-fd2d-R205-bent-annulus-thin-cuff-grafting.md.

The global reach premise includes prefix–tail and other cross-piece pairs; it is not replaced by the tail curvature bound. Existing exact generalized-cylinder results already handle the indicated same-tail and disk pairs. The still unknown complete-prefix geometry remains explicit.

## 7. A strict held bound for amplitude one

The exact polynomial moments are
$$
\int_0^1S_9^2=\frac{38251}{92378},\qquad
\int_0^1S_9^4=\frac{376009639}{1094020070}.
$$
Using $\cos x\le1-x^2/2+x^4/24$ for $0\le x\le1$ gives
$$
C_1(a_c)\le a_c-\frac L2\int S_9^2+\frac L{24}\int S_9^4
=\frac{13114910942657}{18436616484000}<.711352 .
\tag{22}
$$
The generating coordinate is increasing and odd, so every point of the phase-zero annulus has $|y|\le C_1(a_c)$. For the accurately normalized current central major axis $A_q\ge136203/100000$ and witness $p=(0,A_q,0)$, every such point is at distance at least
$$
A_q-C_1(a_c)\ge
\frac{149953922588069}{230457706050000}
=.6506787087\ldots>\frac{16}{25}.
\tag{23}
$$
The exact positive margin above $.64$ is $2460990716069/230457706050000$. This pays the complete annulus at the held-witness phase without substituting a background height. It does not pay the unknown prefix or assert the same fixed-plane bound for every rotated annulus.

For general $A\le1$ the same argument gives
$$
C_A(a_c)\le a_c-\frac{LA^2}{2}\int S_9^2+\frac{LA^4}{24}\int S_9^4,
\qquad 0\le H_A\le23A/100.
$$
A separate uniform-amplitude cap consumer may combine these with actual $A_q,Z_c$; a small-amplitude field does not inherit (23) solely from using the same code.

## 8. Actual source, checks, and unsolved baselines

The independent modules are:

- scripts/fd2d-bent-annulus-reference-R205.cjs;
- scripts/fd2d-direct-position-bent-annulus-metric-R205.cjs;
- scripts/fd2d-direct-position-bent-annulus-curvature-R205.cjs;
- scripts/fd2d-check-bent-annulus-R205.cjs.

The helper exposes complete full-circle reference angles, tail Cartesian two-jets, $T,T_s,T_{ss},T_u$, mean-height jets and external amplitude jets. The old finite layout remains transparent; its mandatory bentAnnulusReference definition distinguishes this mathematical reference from the original flat-cut field.

Numerical primitives use Gauss8 on declared cells, split additionally at $a_0(s)\sin u=\pm c_f,\pm a_c$. Those boundaries depend on neither finite coefficients nor $A$, so every parameter derivative uses the same finite sums. The supplied $s$ jets approximate derivatives of the exact primitive; they are not described as derivatives of a floating moving-quadrature algorithm. R188/R193 error consumers are still needed for continuous certification.

An initial unsplit cut test had an $X_{ss}$ discrepancy about $9.58\times10^{-10}$. Explicit clipping splits reduced the nine-angle amplitude-one discrepancy to $1.46\times10^{-14}$. The final executable amplitude-$1/4$ test gives maximum cut two-jet discrepancy $4.39\times10^{-15}$. At an active-curvature point, a nonzero direction through all finite columns has scaled two-jet difference at most $1.65\times10^{-9}$ and scaled curvature-hinge difference at most $1.03\times10^{-9}$. These are implementation diagnostics, not interval certificates.

The actual R203 eight-accepted parent was consumed with all $961$ parameters unchanged and $N=128$. The new metric-plus-curvature objective, excluding the parent's additional R203 geometry rows, gives:

| Frozen amplitude | Squared objective | Sample maximum curvature | Sample minimum immersion determinant |
| --- | --- | --- | --- |
| 0 | .01243088658 | 14.37587557 | .8521765319 |
| .25 | .03797777527 | 17.13140872 | .7007926330 |
| 1 | 1.20130401504 | 87.79176689 | .1308504556 |

The inner cuff height stays $.524551678714407$; the outer means change. These are new baselines with **zero accepted R205 steps**. Abrupt replacement by amplitude one is a bad warm field. A valid additional representation is not an already improved or solved surface.

Final work must still establish full-domain isometry convergence for a fixed physical metric, complete all-phase embedding/reach, the required held and rigid-motion quotient changes, and actual closed meshes. Radius-design steps are not silently relabelled as refinement of one fixed metric.
