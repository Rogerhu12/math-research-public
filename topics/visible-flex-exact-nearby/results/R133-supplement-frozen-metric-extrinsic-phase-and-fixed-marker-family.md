# R133 supplement — the actual extrinsic phase after freezing every metric parameter

2026-11-15. **Proved conditional geometric construction and exact parameter identification.** This note identifies the genuine family parameter and records the complete fixed-metric mechanism already present in [the fifth-marker theorem](R133-supplement-waist-normal-offset-and-fifth-power-markers.md), Section 5. It does not assert that its single global exact surface or its global geometric hypotheses have been constructed.

The parameters $\eta,\nu,\Gamma _1,\Gamma _2$ belong to the design and solution of that single surface. They are selected once and then held fixed. The extrinsic family parameter below is the independent real angle $\tau$. No new numerical computation is used.

## 1. Which parameters are fixed

The original [waist Cauchy construction](R125-local-exact-waist-Cauchy-branch.md), (125.1), uses the exact affine centre
$$
 \eta_0=-7789843107295549/4611686018427387904
$$
and defines $g_{0,\eta}=E_\eta(r)\,dr^2+a_\eta(r)^2d\theta^2$ from the original object. Its Section 1 explicitly allows different auxiliary parameters to have different target metrics. Consequently the old uniform $\eta$-box is an input enclosure, not a fixed-metric flex parameter.

Similarly [the complete state and $\nu$-response](R133-supplement-complete-C0-state-and-nu-geometry-response.md), (C.6)–(C.7), fixes $a$ but changes
$$
 E_\nu=E e^{\nu w},\qquad
 \gamma_{\nu+\delta}=\gamma_\nu e^{\delta w/2},\qquad
 K_{\nu+\delta}=e^{-\delta w}
   \left(K_\nu+\delta\frac{\beta w'}{2a^2\gamma_\nu^2}\right).
 \tag{P.1}
$$
This is an intrinsic metric design direction. The complete $\nu$ source, its Schur column and its nonzero tests remain useful for selecting the one object. They do not produce the family in this note. The radial first and second metric counterterms are frozen in exactly the same way.

The waist amplitude $\alpha$, the outer choices, the absolute height constants and the marker data are also fixed once. The statement in the [waist amplitude interface](R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md), Section 5, that the phase family uses the final fixed parameters is implemented below.

## 2. Required single-surface input

Let $M$ be the closed material surface with a smooth circle action $S_\tau$. Away from its two polar points it has the original material coordinates
$$
 S_\tau(r,\theta)=(r,\theta+\tau).
$$
This action is required to extend across the two material polar disks. Assume there is one $C^2$ exact immersion $G:M\to\mathbb R^3$ whose induced metric $g=G^*\langle\cdot,\cdot\rangle$ obeys
$$
 S_\tau^*g=g.
 \tag{P.2}
$$
In the original body and tail coordinates this is the already intended radial metric $E(r)\,dr^2+a(r)^2d\theta^2$, with every design parameter fixed. Any original physical seams remain part of $G$; their complete two-sided $C^2$ matching is an input.

Assume that the two genuine flat material disks have compatible polar coordinate $a$, with
$$
 G(a,\theta)=(a\cos(\theta+\alpha_\pm),a\sin(\theta+\alpha_\pm),z_\pm),
 \qquad 0\le a\le a_\pm,\quad a_\pm>0 .
 \tag{P.3}
$$
The same material circle action acts on both disks. Their fixed angular offsets $\alpha_+$ and $\alpha_-$ may differ; the axis, offsets and both heights are chosen once and are not separately realigned at different times. The intrinsic requirement is the actual equivariance $G\circ S_\tau=R_\tau G$ on each disk, not a simultaneous choice of two zero-angle origins. Equality here is an exact two-dimensional disk statement, not a boundary circle or an approximate flatness estimate. The period, global reconstruction, physical $B,C$ matching and height conditions needed for this input are the ones retained in [the full physical trace theorem](R133-supplement-full-physical-trace-matching-and-waist-reflection.md).

### 2.1. A geometric verification of the two disks' common orientation

The equivariance in (P.3) need not be an additional PDE condition. Suppose the
original $S$ is the standard effective material circle action, free away from
its two poles, and the two polar material disks are $S$-invariant. Suppose
their images under $G$ are the two round flat disks centred on the same axis,
and the single-surface hypotheses (P.15) and (G.17) hold.

The positive support condition makes $G$ a star-shaped embedding by the
original theorem's radial-projection argument. On either flat disk,
$G S_\tau G^{-1}$ is an isometry of that Euclidean disk, since (P.2) holds.
It fixes the centre. Its connected circle group is therefore a planar
rotation group $R_{k_\pm\tau}$, where $k_\pm$ is an integer.
The standard action is free off its poles, so $|k_\pm|=1$.

Star-shapedness and the opposite signs of $z_\pm$ show that the image meets
the common axis exactly at the two disk centres. Join an ordinary point
in the upper material disk to one in the lower disk by a path in $M$ avoiding
the two poles. Applying $S_\tau$ along this path and then $G$ gives a homotopy
of their orbit loops in $\mathbb R^3$ minus that axis. Their winding numbers
about the axis are equal. Hence
$$
                         k_+=k_-\in\{1,-1\}. \tag{P.3a}
$$
A single choice of positive angular orientation makes both equal to $1$,
which proves the required common equivariance. Equivalently, without
renaming the original action, use the same $R_{k_+\tau}$ on both disks.
The fixed offsets $\alpha_\pm$ remain arbitrary and need not coincide.

This argument uses the single global geometric hypotheses. It does not infer
equivariance merely from two invariant disk images, nor from approximate
flatness, and it does not assert that the still-required exact $G$ exists.

## 3. Exact unmarked phase and its genuine velocity

Let $R_\tau$ be rotation about the common $z$-axis through angle $\tau$. Define
$$
 G_\tau=R_\tau\circ G\circ S_{-\tau},\qquad
 0\le\tau\le\pi/4.
 \tag{P.4}
$$
Since $R_\tau$ is a Euclidean isometry,
$$
 G_\tau^*\langle\cdot,\cdot\rangle
   =S_{-\tau}^*(G^*\langle\cdot,\cdot\rangle)=g.
 \tag{P.5}
$$
No metric coefficient or parameter is updated in this calculation. On either disk (P.3),
$$
 R_\tau(a\cos(\theta-\tau+\alpha_\pm),a\sin(\theta-\tau+\alpha_\pm),z_\pm)
       =(a\cos(\theta+\alpha_\pm),a\sin(\theta+\alpha_\pm),z_\pm).
 \tag{P.6}
$$
Thus both entire disks are fixed pointwise as maps of the same material points.

Composition by a smooth circle action is continuous on $C^2(M,\mathbb R^3)$; this follows directly from the chain rule through order two and uniform continuity of the second derivatives on the compact domain. Hence $\tau\mapsto G_\tau$ is $C^2$-continuous. For $G\in C^2$ its derivative exists in $C^1$, and at zero is
$$
 h=\Omega G-G_\theta,\qquad
 \Omega(x,y,z)=(-y,x,0).
 \tag{P.7}
$$
It satisfies $Dg_G[h]=0$, and (P.6) gives $h=0$ throughout both disks. A derivative in the $C^2$ topology would require additional regularity; it is unnecessary for the stated continuous $C^2$ family.

Before marking, the image is precisely
$$
 G_\tau(M)=R_\tau G(M).
 \tag{P.8}
$$
These unmarked images are Euclidean congruent, including when they have positive held Hausdorff distance. The unmarked phase alone does not establish the required noncongruence.

## 4. The same material marker replacement at every phase

Choose fixed marked subdisks strictly inside (P.3). On each of them use the same fixed Cartesian coordinates $(x,y)$ supplied by (P.3), and replace its height by $z_++u_i$ on the upper disk or $z_--u_i$ on the lower disk. In particular use the exact profile and fixed centres of the fifth-marker theorem:
$$
 u_i(s)=\frac{k_iR^2}{10}(1-s^2/R^2)_+^5,\qquad
 k_i^2=145,146,147,148.
 \tag{P.9}
$$
Here $R>0$, all centres and all signs are chosen once. Define $F_\tau$ to equal this fixed marked map on those material subdisks and $G_\tau$ elsewhere.

The profile and its derivatives through order four vanish on its support boundary. Since (P.6) holds on an open disk containing every support, the new and old maps have exactly the same two-jets there, for all $\tau$. Therefore $F_\tau$ is $C^2$ and $\tau\mapsto F_\tau$ is continuous in that topology.

On a marker the induced metric is exactly
$$
 dx^2+dy^2+du_i\otimes du_i.
 \tag{P.10}
$$
It is independent of $\tau$. Off the markers it is the fixed metric (P.5). Consequently
$$
 F_\tau^*\langle\cdot,\cdot\rangle=g^\#\quad
       \text{for every }\tau\in[0,\pi/4].
 \tag{P.11}
$$
The final common metric $g^\#$ agrees with the selected radial metric away from the markers. On their supports it is the same new metric (P.10) at every time; it need not itself be rotation invariant there. This distinction prevents applying a material rotation directly to an already marked metric.

The held set is the union of the two fixed closed subdisks specified in the original theorem, containing all marker supports. Every one of its material points is fixed under $F_\tau$, including outside and inside the supports.

## 5. Noncongruence is supplied by the fixed labels and a separate nontriviality witness

Assume the unmarked body's Gauss curvature is at most $144$. For (P.9), putting $t=s^2/R^2$, the complete Gauss curvature is
$$
 K_i(t)=
 \frac{k_i^2(1-t)^7(1-9t)}
      {(1+k_i^2R^2t(1-t)^8)^2}.
 \tag{P.12}
$$
It is strictly decreasing while positive away from the centre, and is nonpositive for $t\ge1/9$. Thus each marker has just one positive local maximum, with its distinct value $145,146,147,148$. A level set on a higher marker is not another local maximum. The whole marked surface therefore has a unique point with each of these four labelled maximum values.

With $A=\min(a_+,a_-)/2$, $d=A/2=4R$ and $b_i=k_iR^2/10$, those four points are
$$
 (d,0,z_++b_1),\ (-d,0,z_++b_2),\
 (0,d,z_--b_3),\ (0,-d,z_--b_4).
$$
Their affine determinant has modulus
$$
 2d^2\left(2(z_+-z_-)+\sum_i b_i\right)
       >A^2(z_+-z_-)>0.
 \tag{P.13}
$$
Any Euclidean isometry between two marked images preserves Gauss curvature and local maxima, and must fix these four points individually. Their noncoplanarity forces that isometry to be the identity. This includes orientation-reversing ambient isometries.

One must still show that the two images differ. The velocity formula (P.7) alone does not prove this. The original theorem supplies the exact endpoint witness through its complete waist support gap $\Delta>0$, the full outward normal tube and the unchanged waist. Under those hypotheses,
$$
 d_H(F_{\pi/4}(M),F_0(M))\ge\Delta>0.
 \tag{P.14}
$$
Thus these endpoints cannot be congruent. Compactness of $O(3)$ and boundedness of translations in any sequence with bounded Hausdorff error show that the rigid-motion optimized Hausdorff infimum is attained. Since no exact congruence exists, its value is strictly positive. This gives strict $\delta_{\rm E}>0$, not a new numerical lower bound for it.

## 6. The existing quantitative gates are unchanged

The sufficient geometric inputs remain exactly the fifth-marker theorem's (G.14), (G.17), (G.24), including the full waist $A^0$ error bound, exact reflection and circle-action identities, two true flat disks, and the global bounds
$$
 |G|\le511/400,\qquad G\cdot N>4/49,\qquad
 |\lambda_i|\le12,\qquad \lambda_i\le196/27.
 \tag{P.15}
$$
When these hold for the one final exact surface, the original proved marker estimates give the entire family's held, reach and noncongruence conclusions. In particular its same-object normal tube yields $\delta_{\rm hold}>0.05\,\operatorname{diam}F_0(M)$; its double-sided tube yields the original $0.03$ reach proportion. The original strict inequalities and their complete unknown-tail fees remain authoritative. No endpoint-only computation establishes (P.15) over the body, both tails and the seams.

Because unmarked members are rotations of $G$, their global geometric bounds agree exactly. The fixed markers have the same paid bounds for every phase. Hence these geometric gates need to be established for one $G$ and the fixed patches, not by solving a new metric family at every $\tau$.

## 7. Relation to the reduced derivative and the old parity class

In the original curvature frame, angular translation produces
$$
 B_\tau(r,\theta)=B(r,\theta-\tau),\qquad
 C_\tau(r,\theta)=C(r,\theta-\tau).
 \tag{P.16}
$$
The complete fixed radial-coefficient Gauss–Codazzi equations commute with this translation. On every original piece where the curvature fields are $C^1$, the infinitesimal curvature direction is therefore
$$
 (\dot B,\dot C)=-(B_\theta,C_\theta)
 \tag{P.17}
$$
with zero intrinsic parameter source. At lower regularity the same identity is the distributional derivative of the translation action; no additional classical derivative is asserted. Means are preserved by the translation; they are not set to zero. All actual radial interfaces translate along their circles, so their matched two-jets and any explicitly retained source identities keep the same status.

At the base member, a fixed-axis reflection class has $B$ odd and $C$ even. The direction (P.17) has the opposite parity. It is not an element of that fixed-axis restricted inverse domain. Thus a design inverse in the original parity class does not rule out the geometrically produced phase orbit. Conversely it cannot be relabelled as a full-space inverse containing this kernel. For nonzero phase the reflection axes are translated along with the exact surface.

The nonlinear design map obtained by choosing $\Gamma_1=\Gamma_1(u)$ has a reduced derivative containing the actual metric column. Freezing that map for arbitrary new boundary data would require its own full Schur argument and the true height/mean ports. No such unproved implication is used in (P.4)–(P.17): first solve one design problem, freeze its coefficients and ports, then use the exact geometric symmetry and the fixed patches. This closes the family-parameter identification without pretending that the single global design problem has already been solved.

## 8. Exact provenance and remaining work

The principal original geometric input is
`R133-supplement-waist-normal-offset-and-fifth-power-markers.md`,
Git blob `d3b9761eee0f420e1041812ece78a8c0850dcbdf`, 13447 bytes.
Its Section 5 already gives (P.4) followed by the static replacement. The auxiliary-parameter warning is in R125 Section 1, blob
`309afa6ff3758b0650a65baf52b79837312d3d66`, 10202 bytes.
The physical matching and reconstruction hypotheses are in
`R133-supplement-full-physical-trace-matching-and-waist-reflection.md`,
blob `89a82cfabf212c0345f185b17632f337c37d5016`, 9970 bytes.

This note proves the exact conditional freeze and family interface. It does not supply the still-required single full closed exact $G$, complete body/cap/tail matching, physical means and heights, or the same-object global geometric inequalities. There is no new numerical run or certificate.
