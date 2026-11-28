# R750 — A quantitative nonlinear Darboux strip over every displaced straight entrance

2026-11-28. For the original fixed R746/R747 end metric we extend the fractional Darboux construction over a full finite lift of its **actual piecewise-polynomial section**, crossing every original knot. Its use as a physical seam continuation is restricted to the material intervals that are carried into straight parts of the physical cylinder. On every such entire arc we obtain a common, explicit, strictly positive transverse width. The estimate is extremely small. The auxiliary height need not be periodic after one circuit and does not give an end over a curved trace.

## 1. The finite section and rescaling

In [R749](R749-fractional-Darboux-exact-local-continuation-at-the-displaced-straight-wall.md) the target was \(g=A^2ds^2+dv^2,\ A=1-\kappa(s)d(v)\), with \(d\) the actual initial R744 rolled offset, \(\epsilon_y=1/2000,\ r_y=27/250\). Keep these data. On a lift \(s\in[0,P]\) the original \(\kappa\) is continuous with continuous first derivative and consists of 26 successive polynomials of degree at most 5. Each half contains one left wall, three portions of the left turn, five portions of the original bent disk arc, three portions of the right turn, and one right wall. Reflection reverses their order on the other half. Every piece has length less than 2. Subdividing a piece causes no change of metric or geometry. To follow an interval across the periodic cut one may instead use the same 26 pieces from a cyclically permuted knot, or concatenate two lifts with the corresponding number of estimates below.

At a new piece entrance \(s_j\), introduce a real positive parameter \(q\) and use
\[
 X=q(s-s_j),\qquad v=q^8 Y,\qquad z=v^{5/2}u,\qquad u=q^{-4}U(X,Y).
\]
For the analytic argument also use complex \(q,X,Y\) near zero. Let
\[
 k_5(X,q)=q^5\kappa(s_j+X/q).
\]
This is a polynomial in \(X,q\) for each piece, including \(q=0\). Define \(A=1-q^{-5}k_5 d(q^8Y)\), \(C_1=q k_5 A[d''(v)/v^3]\), \(C_2=q^{-2}AA_v/v\), with analytic values at zero. Indeed \(d=v^5 d_*(v),\ d'=v^4 e_*(v),\ d''=v^3 f_*(v)\) for analytic \(d_*,e_*,f_*\). In particular
\[
 A=1-q^{35}k_5Y^5d_*,\qquad C_2=-q^{17} A k_5 Y^3 e_*,\qquad C_1=q k_5 A f_*.
\]
The scaled R749 equation, including the nonconstant angular metric, is
\[
 \begin{split}
 T&=\tfrac52 U+Y U_Y,\qquad B=\tfrac{15}{4}U+5Y U_Y+Y^2 U_{YY},\\
 D&=\tfrac52 U_X+YU_{XY}-(YA_Y/A)U_X,\\
 W^2&=1-q^{34}Y^5U_X^2/A^2-q^{16}Y^3T^2,\\
 U_{XX}&=(A_X/A)U_X-C_2T+(D^2+C_1 W^2)/B .                          \tag{1}
 \end{split}
\]
The Cauchy data at the entrance of the first piece are \(U=1,U_X=0\). At \(q=0\) the constant solution \(U=1\) satisfies these data and (1) on each piece. The longitudinal Cauchy data on all subsequent pieces are supplied by the actual previous solution, not reset at knots.

## 2. Explicit analytic bounds for one continuation

Put \(R_0=2^{-200}\). For \(|q|,|X|,|Y|\le R_0\), all coefficients of (1) obey
\[
 |A-1|,\quad |A_X|,\quad |Y A_Y|,\quad |C_1|,\quad |C_2| <1/8 .
 \tag{2}
\]
Here are crude sufficient estimates with the original constants. On a true curvature ramp the argument of \(S_5\) measured from the start of its polynomial piece is either \(t/L\) or \(1-t/L\), with \(L\ge .001\) and amplitude \(<7\). Constants and straight portions obey the same majorization. Expanding those degree-five polynomials gives coefficient sum \(<7[10(1+1000)^3+15(1+1000)^4+6(1+1000)^5]<10^{18}\). Hence \(|k_5|<10^{18}\), \(|\partial_X k_5|<5\cdot10^{18}\) on the unit bidisk. For \(|v|\le2^{-200}\), the exact polynomial \(\eta\) of R749 §1 satisfies \(|\eta/v^4|<10^{12}\), \(|\eta'/v^3|<10^{12}\). This follows by inserting \(\epsilon_y=1/2000,\ r_y=27/250\) into its three coefficients and multiplying the last two terms by \(|v|\) and \(|v|^2\). The elementary bounded complex sine and cosine series then give \(|d_*|,|e_*|,|f_*|<10^{13}\). The \(Y\) derivative of \(d(q^8Y)\) uses \(q^8d'(q^8Y)\). These estimates in the displayed formulas imply (2), including \(C_1\), whose smallest parameter power is one.

Use the three first-order variables \(Z=(U-1,U_X,U_Y)\) with longitudinal derivative equal to \(U_X\), (1), and \(\partial_Y U_X\), respectively. If at the current entrance we have an analytic initial triple \(Z^0(Y,q)\) with \(Z^0,Z^0_Y\) bounded in component norm by \(1/64\), subtract it as a function independent of \(X\). The new unknown \(H=Z-Z^0\) has zero Cauchy data and satisfies
\[
 H_X=F(X,Y,q,H,H_Y).
\]
On \(|X|,|Y|,|q|<a\le R_0\), \(|H_i|,|(H_Y)_i|<1/8\), every component of \(F\) is bounded by 16. Indeed \(|U-1|,|U_X|,|U_Y|,|U_{XY}|,|U_{YY}|<1/8+1/64\), while \(|B|>3,\ |A|>7/8\). The two short first-order rows and (1) directly give the asserted bound. Equality of the third integrated variable with \(U_Y\) follows from its first-order evolution and the initial compatibility.

For clarity an explicit common CK radius follows from positive Taylor majorants. Cauchy's coefficient estimates on these polydisks majorize all three right-hand sides coefficientwise by
\[
 \frac {16}{1-(X+Y+q)/a-8\sum H_i-8\sum (H_Y)_i}.
\]
Let \(\beta=65536,\ \xi=\beta X+Y+q\), and take \(f(0)=0\), with the small positive root in
\[
 f'=\frac{16/\beta}{1-\xi/a-24f-24f'} .
 \tag{3}
\]
The root as a function of \(\xi,f\) has nonnegative Taylor coefficients by the usual geometric/quadratic power series. On \(|\xi|,|f|\le a/4\), write \(L=1-\xi/a-24f\), so \(|L|>.74\). The expansion of the small root in \(24(16/\beta)/L^2\) gives \(|f'|<.001\), and implicit differentiation gives \(|\partial_f f'|<.05\) there. Integration from zero is a contraction of the bounded holomorphic disk functions \(|f|\le a/4\) on \(|\xi|<a/4\). Thus (3) has an analytic nonnegative-coefficient solution there. Its composite \(f(\beta X+Y+q)\) coefficientwise dominates the solution for each unknown: at \(X=0\) the zero unknowns are majorized, and recursion by the \(X\) derivative preserves domination, including the \(Y\) derivative. Both sides converge where \(\beta|X|+|Y|+|q|<a/4\). Its bound there is \(<a/4\). This supplies an explicit analytic existence estimate without inferring convergence from finite Taylor data.

## 3. Crossing the actual knots

Suppose the preceding field \(Z\) is analytic on the polydisk of common radius \(R\le R_0\), bounded componentwise by 1 and identically zero on \(q=0\). With previous physical longitudinal length \(\ell<2\), form the two Cauchy data and their spatial derivative by reading the previous solution at \(X=q\ell\). This is analytic in \(q,Y\) for \(|q|<R/3,\ |Y|<R\). Schwarz's lemma at \(q=0\), followed by the one-variable Cauchy estimate in \(Y\), gives bounds \(3|q|/R\) for the initial triple and \(12|q|/R^2\) for its \(Y\) derivative on \(|Y|<R/2\). The first piece instead has identically zero data for \(Z\). Use
\[
     a=R^3/4096,\qquad R_{\rm next}=2^{-34}R^3 .
\]
On the polydisk used in §2 these data satisfy both \(1/64\) bounds. Since \((65536+2)R_{\rm next}<a/4\), the new solution exists on the full \(R_{\rm next}\) polydisk with \(|Z|<1\). At \(q=0\) it is again identically zero by (1) and uniqueness. This closes the induction. The polynomial for the next actual piece is its own polynomial centered at its exact entrance. The old and new analytic continuations into complex \(X\) can differ off their respective physical intervals.

After 26 pieces put
\[
 R_{j+1}=2^{-34}R_j^3,\qquad q=R_{26}/8,\qquad
                     v_* = q^8 R_{26}/8 >0.                               \tag{4}
\]
For this **single fixed** \(q\), every required \(X=q(s-s_j)\) has magnitude \(<R_{26}/4\); throughout \(0\le v\le v_*\) one has \(0\le Y\le R_{26}/8\). This produces one actual solution over all \(0\le s\le P\). The two Cauchy data agree at the knots, as do their transverse derivatives. The successive right sides of (1) there agree because \(\kappa,\kappa'\) are continuous. Thus \(U_{XX}\) and the entire two-jet match. Higher regularity where needed for the development follows as well on the two sides: the true ramp joins have \(\kappa\) at least \(C^2\), so differentiating (1) once gives agreement of the third derivatives. The data at \(s=P\) may differ from those at zero, and no periodic identification of \(U\) is made. In exact powers of two, \(R_j=2^{-(217\cdot 3^j-17)}\). This is a rigorous lower width with an extremely conservative exponent and no claim of practical sharpness.

## 4. Development, curvature and physical scope of this width

The positive definiteness and the planar development of \(g-dz^2\) follow as in R749. For example on the smaller final boxes the bounds of §2 give \(|U-1|,|U_X|,|U_Y|<1/8,\ |Y^2 U_{YY}|,|YU_{XY}|<1/8\), using the one-variable Cauchy estimate on the larger \(Y\) disk for the last two quantities. Hence \(3<|B|<5,\ |D|<1,\ W^2>1/2\). For the physical covariant Hessian entries one obtains
\[
 |H_{vv}|=\sqrt Y\,|B|,\quad |H_{sv}|=q^9Y^{3/2}|D|,\quad
 |H_{ss}|=q^{18}Y^{5/2}|(D^2+C_1W^2)/B|.
\]
Together with (2), \(Y\le R_{26}/8\) these bound the absolute principal curvatures on the whole positive strip by \(10\sqrt{R_{26}}\): use \({\rm II}=\operatorname{Hess}_g z/W\) and the two metric speeds \(A,1\). In particular they are less than 1. The planar development may be made successively along the rectangles, aligning its common coframe at each boundary. The developed coordinates and their first derivatives coincide along each whole seam by the flat connection and the matched metric jets. Normalize them so the entire lower edge has the planar trace \((s,0)\) and transverse derivative \((0,1)\).

There is also global injectivity when this thin strip is used on a *single straight physical trace*. Its developed-plus-height map is a small \(C^1\) perturbation of the planar rectangle, quantitatively as follows. In physical coordinates \(|A-1|, |A_s|,|A_v|<10^{-3}\) there, by the real actual section bounds (or the scaled ones with their higher powers of \(q\)). The covariant Gauss formula and the above curvature bound give \(|F_{sv}|,|F_{vv}|<.01\) after aligning the flat trace, since \(F_{sv}=(A_v/A)F_s+{\rm II}_{sv}n\), \(F_{vv}={\rm II}_{vv}n\). Integration in \(v\) keeps its planar differential within operator norm .01 of identity. The planar projection is therefore injective on every such convex rectangular material domain by integrating along straight parameter segments. The positional and normal errors tend uniformly to zero with the displayed width; on the R744 straight portions the original support is at least .110 and the support error here is below .001. For instance the normal changes by at most twice the .01 derivative estimate sharpened to \(.02v_*\), while \(|F-c|<2.30\).

For each physical phase the formula is applied to the entire material inverse of any one genuinely straight section of \(\Gamma(s+r\theta)\). The origin of the physical frame is chosen so that its longitudinal coordinate \(s\) maps to that line; its other axes are the transverse side and the true outward normal. This includes positive and negative \(y\) ends and every phase for which the selected straight trace is present. Zero-target-curvature and ramp knots *inside* such a true straight trace are included. If material coordinates cross the cut, cyclically shift the starting knot or use a double lift and \(R_{52}\) in (4). Supports slightly inside straight portions can be spliced in the closed reference by R749 §4, with all-phase reach at least .106. The full-width exact piece is itself an open seam continuation; the closed global splices pay transition errors. The numerator bound on local curvature does not certify a complete end, any physical curved boundary continuation, compatibility around the full circumference, or attachment to the two filling caps.
