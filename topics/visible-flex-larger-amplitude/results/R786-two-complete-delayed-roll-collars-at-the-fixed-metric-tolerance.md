# R786. The two complete cap collars at all phases and all angles on the R781 fixed metric

Use the R781 material sphere and its original initial metric. The two-millimeter-scale collars below are part of the true rounded ends, including the nearly diagonal material lines where two extended cap turns can overlap. The prescribed field has relative spectral Gram error below $10^{-6}$ on both entire disks and on the two complete roll collars of width $.0024$ at every phase. On the disks the error is exactly zero. This is a finite error bound on fixed input. The central error is still large, and this bound on a subdomain supplies neither whole-domain convergence nor exact isometry.

## Actual meridians

Retain the R785 common four-sector shear with the MILD angles $(.020,.022,.024,.025)$ and the R781 balanced central reference with $\xi=.02$. At each end let $v=L-b$ be reverse roll arclength, $a_b=.45-d_b\in[.359,.36]$, with cap plane $Y_\sigma$ and $\sigma=1,-1$ for the two heads. Put $h_r=.09$, $\eta=.001$. The original turn from the plane is $\alpha(u)$, with $\alpha(0)=0$, $\alpha'=S_5(u/\eta)/h_r$ up to $\eta$, and $\alpha(u)=(u-\eta/2)/h_r$ on the subsequent constant-curvature section. Write $p(u)=\int_0^u\cos\alpha$, $d(u)=\int_0^u\sin\alpha$. Reflection symmetry of the original R781 softened quarter turn gives the true old meridian $(a_b+p(v),Y_\sigma-\sigma d(v))$ exactly.

Use the clipped quintic smoothstep $S_5$. Let $H=.0024S_5(t/.006)$, $V=.004$, $W=.08$ and define
$$
 s=\max\{0,v-H[1-S_5((v-V)/W)]\},\qquad
 a_H=a_b+v+p(s)-s,\qquad y_H=Y_\sigma-\sigma d(s).
$$
The new end profile is $(a_H n_\theta,y_H)$ followed by the single R785 world shear $S$ on the whole sphere. The central chart and both full disks are the original R785 charts. At $v=0$ its first two meridian derivatives agree with the genuine planar disk coordinates; at $v\ge V+W$ the old R785 end is exactly recovered including both jets. At $s=0$ the two remainders $p(s)-s=O(s^9)$ and $d(s)=O(s^5)$ preserve joint $C^2$ of the positive-part composition in space and phase. At phase zero $H=0$, and the entire model, including the Cartesian poles and normal overlap, is the old initial R781 surface. The source uses the original phase-zero evaluator to make this true of the working floating-point evaluation as well. The new delay changes actual positions.

## Relative norm on the full collars

The fixed tensor there is $dv^2+a_0(v)^2d\theta^2$, $a_0=a_b+p(v)$. For $v\le v_*:=.0024$ the delay is constant before taking the positive part. Thus before shear the meridian is unit-speed, its mixed metric entry is zero, and
$$
 0\le a_H-a_0\le \int_0^{v_*}(1-\cos\alpha(u))\,du <1.55\cdot10^{-7}.
$$
For the last inequality use $\eta[\eta/(2h_r)]^2/2$ up to $\eta$, and $[(v_*-\eta/2)^3-(\eta/2)^3]/(6h_r^2)$ thereafter. Hence the pre-shear relative angular excess $(a_H/a_0)^2-1$ is $<8.65\cdot10^{-7}$.

At $t\ge.006$, $s=0$ on the whole strip. Each transverse coordinate is transformed by its own unit-speed planar bend. Write $b_X,b_Z$ for the signed angles in those two Cartesian coordinates (only one of each signed pair can act). On a horizontal plane their simultaneous pullback is exactly $dX^2+dZ^2+\sin b_X\sin b_Z(dX\,dZ+dZ\,dX)$, in symmetric-tensor notation. Where two bends act let their signed positive distances beyond $a_b/\sqrt2$ be $u_1,u_2$. Cauchy–Schwarz gives $u_1+u_2\le\sqrt2v_*$, so the smaller is $\le v_*/\sqrt2$. The corresponding clock argument divided by its softened edge width $.08(.06)$ is at most $.354$. The actual clock derivative has the factor $S_5$ there, and $S_5(.354)<.25$. Thus one of the two $|\sin b_i|$ is at most $.25(.025/.0752)u_i$ and the other at most $(.025/.0752)u_i$. Their product is at most
$$
 .25(.025/.0752)^2v_*^2/2 < 8.0\cdot10^{-8}.
$$
Where only one or no flap acts, this product vanishes. Pulling the cross tensor to the original orthonormal frame multiplies its norm by at most $(1+8.65\cdot10^{-7})$. The full sum is $<9.46\cdot10^{-7}$.

At $0\le t<.006$ each $|\sin b_i|\le .025(.006)^2=9\cdot10^{-7}$. Before shear the dual norm of $dY$ is $\le\sin[(v_*-\eta/2)/h_r]<.0212$. In addition to the two-coordinate product, the shear adds the symmetric cross term between $dY$ and $\sin b_X\,dX+\sin b_Z\,dZ$. Its operator norm is at most $2(.0212)\sqrt2(9\cdot10^{-7})\sqrt{1+8.65\cdot10^{-7}}<5.41\cdot10^{-8}$. Together with the angular term the total is $<9.20\cdot10^{-7}$. These bounds include the switch instants $v=H(t)$, the complete angular overlaps and all true cap seam points. On either actual cap the four flap interiors are disjoint and $dY=0$ before the shear, so all cap Gram entries, in each of their three material charts, remain exact.

## Signed reach, macroscopic motion and scope

The original R785 central profiles have curvature at most $22.70$ and signed normal layers out to distance $1/22.70$. The modified ends permit the same radius. To check the actual new meridians, write their oriented planar velocity as $U=e_r+s'(T-e_r)$, where $T=(\cos\alpha,-\sin\alpha)$ in radial and signed axial components. On $V\le v\le V+W$,
$$
 1\le s'\le1.057,\quad |s''|<2.18,\quad
 .0016\le s\le.084,\quad \alpha'=1/.09,\quad 0\le\alpha<.93 .
$$
Hence $|U|^2=1+2s'(s'-1)(1-\cos\alpha)\ge1$. The curvature numerator in the signed turning direction is $s'^2[s'+(1-s')\cos\alpha]\alpha'+s''\sin\alpha>0$ and $|U'|\le s'^2/.09+2|s''|\sin(.93/2)<14.5$. The radial component $1+s'(\cos\alpha-1)$ is positive. Before recovery the flat part and the delayed true segment have curvature between zero and $1/.09$; after recovery the original fillet continues all the way to its vertical tangent. The angular principal curvature is at most $1/a_b<2.8$. Every head profile is a regular monotone turn between its two original end directions; the extreme axial planes and the central joining rim are unchanged.

For clarity, at a fixed signed normal distance $z$, $|z|<1/22.70$, a meridian offset has the same tangent directions as the original and positive speed factor $1\pm z\kappa$. Start at the pole on its flat disk including the extra flat collar, continue along the open turn, and stop at the central joining rim. Transverse radius increases strictly up to that rim; the final radius is $R\pm z$, an affine strictly monotone function of $z$. At a fixed transverse radius the set of eligible $z$ is an interval. Along the resulting graphs the signed axial height has derivative with respect to $z$ of fixed sign and magnitude $1/|n\cdot e_Y|$ wherever the transverse radius derivative is positive. This follows by differentiating the offset at fixed transverse radius and eliminating the meridional parameter. The same statement on the flat part is immediate. Continuity includes the single vertical-tangent rim. Thus all signed head layers are disjoint. They stay strictly on the exterior side of their central rim plane except for the rim itself, by the signed axial monotonicity of the fixed-$z$ meridians. At the central ends these planes are independent of $z$ since the rim normal is radial. The two ends have disjoint exterior intervals, and neither meets any open central normal layer, by the R781/R785 central axial-coordinate argument. The azimuth is preserved and every transverse radius away from the cap poles stays positive. This proves global normal injectivity before shear, including both caps, sides and the true central interfaces.

Apply the same R785 shear and its complete ambient chord estimates. For $b=.025$ they are $m^2\ge1-\sqrt2 b-2b^2$, $M^2\le1+\sqrt2b+b^2$, $\|D^2S\|\le b/.0752$. Thus the true full post-shear reach is at least $m^2/(22.70M+b/.0752)>1/24.36>.03D$, with $D<1.362$ the unchanged initial diameter. At a given label the difference between the new pre-shear end and R785 is bounded by $(v-s)\sup_{[s,v]}|e_r-T|\le.0024\,[2\sin(.93/2)]<.00216$ throughout the modified area. The change after shear is $<.0023$; the initial field has zero change. Consequently the original R785 held separation $>.320$ stays $>.317$, and its Euclidean-quotient separation $>.086$ stays $>.083$. The unchanged cap grip contains the disk of radius $.18$, diameter $.36>.2D$; the larger unchanged square is available as well. 

The all-angle collar estimate is for the named physical field, on one unchanged fixed metric and at finite parameters. The full central metric and the rest of the rounded rolls still need correction. The short length $.0024$ is a material arclength; the rest of each true roll up to $L=.09\pi/2+.001$ remains present. A later numerical field that modifies these charts must evaluate its own metric, reach and displacements.
