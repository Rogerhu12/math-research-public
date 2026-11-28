# R320. A nonplanar compact center with exact flat two-sided strip, strong strip held distance and nonzero mixed Cauchy data

Use unscaled material length, physical scale λ=53/50, strip half-length s₀=13/128, h=9/100, ρ(θ)=1/5+(32/15)sin⁴θ, and v(θ)=θ−(8/15)sin(2θ)+(1/15)sin(4θ). Then v′=ρ>0 and v(θ+2π)=v(θ)+2π. Put ω=h cos(2θ) and prescribe the unit tangent

T(θ)=(-sinθ,cosθ cosω,cosθ sinω).

Let γ(0)=(A,0,0), A=301/225, and γ_θ=ρT. Its x component equals the V52 p2 planar curve exactly. The y and z derivatives are even about 0, odd about π/2, and all three tangent components change sign at θ+π. Thus γ(π)=(-A,0,0), γ is closed with exact length 2π, γ(v+π)=−γ(v), and γ(−v)=Rγ(v) for the proper half-turn R=diag(1,−1,−1). This v denotes arclength; in displays involving θ its analytic inverse is understood. With Frenet N,B, curvature κ and torsion τ, put a=τ/κ. For |s|≤s₀ solve u=v+s a(v) modulo 2π and set

X(s,u)=γ(v)+s[B(v)+a(v)T(v)].

Since B′=−τN, (B+aT)′=a′T. Hence X_u=T and X_s=B after inversion. This is an exact flat cylindrical material metric ds²+du². Its second form in this order is (κ/J)[[a²,−a],[−a,1]] with J=1+s a′. In physical units its single nonzero principal curvature is κ(1+a²)/(λJ). The symmetry is X(−s,−u)=R X(s,u). This permits true single-half reconstruction of the reflected whole. The nonplanarity follows from a(0)=−4h and κ(0)>0. The two long material marks and their laboratory locations remain explicit.

## Uniform rational certificate

Set x=sin²θ, d=1−x, H=1+16h²x d², P=−1+(3+H)x, and B₀=−PH+2dP′H−3dPH′, using derivatives in x. Direct differentiation of T gives |T_θ|=√H,

a=4h cosθ P/H^(3/2),    a′(v)=4h sinθ B₀/(ρH^(5/2)).

Indeed the numerator of a is det(T,T_θ,T_θθ)=4h cosθ P. Write D=H³+16h²dP². The physical nonzero curvature equals D/[λ(ρH^(5/2)+4hs sinθ B₀)]. The source's `strict` mode covers x∈[0,1] by 8192 closed rational intervals, uses outward rounded fixed-point BigInts of denominator 10²² and encloses each square root by integer square root. Over the entire two-sided flat strip it returns

- J≥.5847055721260626955420;
- κ(1+a²)/(λJ)≤7.7170215448490457259259;
- |a|≤.3600000000000000000000.

The strict weaker bounds .584, 7.74, and .361 are asserted by the consumer. They cover all angles, both boundaries and the full strip. A reach of .097 for the new closed surface does not follow from these local bounds.

## Global embedding and physical strip envelope

Let Γ be V52's planar p2 curve. Its support ranges from B₀₀=141/225 to A. Its radius is at most A. By first-quadrant monotonicity and the signed symmetries, |γ_y|≤B₀₀, |γ_z|≤hB₀₀, |γ_xy−Γ|≤h²B₀₀/2, and |γ_xy|≤A. Since T_xy differs from its planar tangent by at most h²/2, the determinant γ_xy×T_xy is at least B₀₀−(A+B₀₀)h²/2. In the local basis (e_x,(0,cosω,sinω),(0,−sinω,cosω)), the binormal components are (cos²θ ω′,sinθ cosθ ω′,1)/√H. Consequently |B_xy|≤3h=.27, and B_z≥[1−h²/2−h²]/√(1+4h²)>.970. For every s, the planar determinant X_xy×T_xy exceeds B₀₀−(A+B₀₀)h²/2−.27s₀>.59. Also |X_xy|≤A+s₀(.27+.361)<1.403.

The ambient horizontal polar angle has positive v derivative and degree one, by homotopy through s to the simple star-shaped center. The center itself has degree one by projection from the planar curve (same determinant bound with h replaced by any number from zero to .09). Along fixed polar angle, the derivative of laboratory z with respect to s is

B_z−T_z (X_xy×B_xy)/(X_xy×T_xy) > .970−.09·1.403·.27/.59 > .91.

Thus polar angle and height distinguish all strip points up to the periodic parameter, proving global embedding including the two boundary curves. The whole physical strip has y half-width at most λ[B₀₀+s₀(.27+.361)]<.733 and radius at most λ[√(A²+(hB₀₀)²)+s₀√(1+.361²)]<1.535. Its distance from both switched material positions (0,±λA,0) is greater than .684 for every strip point. These strip estimates apply to the actual space curve and both complete halves.

## Actual outgoing data and continuation

The two-jet numerical consumer derives the complete initial frame B,T,N, normal curvature n=κ/J, mixed m=−aκ/J and radial curvature l=a²κ/J from this strip at s=s₀, with full unconstrained positive and negative angular modes. For example its upper boundary m at u=0 and π is approximately +1.25163616 and −1.25163616. Both short-axis binormals have Cartesian y component .0898785492. These are genuine new upper Cauchy data for the original V40 target, with no planar-cylinder assumption.

The same source integrates the full material frame outward, encodes Cartesian positions in all periodic Fourier components on 40 quintic radial panels, and attaches the unchanged physical V47/R314 infinite shell and cap through an explicit two-jet blend to V48. The lower half is the displayed R image with reversed u. Its numerical outer connector and global curvature, reach, strong deformation ratios and continuous full metric require their own tests. The frozen original metric and integrated upper Cauchy field differ conceptually from the exact flat strip above.

From the visible-flexible-closed-surface scripts use `node 2ecf-compact-space-center-flat-strip.mjs strict` and `ports`. To reproduce the actual 256/512-angle outgoing fields use `make256/make512 STATE192 STATE540 TWISTFIELD` and `observe STATE192 STATE540 TWISTFIELD` with V40/V48 inputs. No generated arrays are needed in Git.
