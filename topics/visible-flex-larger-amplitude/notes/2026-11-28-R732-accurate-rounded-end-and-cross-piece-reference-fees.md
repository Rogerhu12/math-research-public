# R732 accurate reference kernel on the complete material half

2026-11-28. This source realizes the explicit reference in R732 §§1–4 for the fixed R690 metric. It accepts outward enclosures of the actual original \(S,R\), exact dyadic \(H_0,k_0\), all 160 original fixed Fejér coefficients, and the actual binary tail width and curvature. It also binds the complete R690 and R732 proof files. All arithmetic evaluation belongs to public repository Actions. No actual point, run, normal root or numerical fee is reported by this source delivery.

## The terminal scalar calculation

Put \(b=1/1000,d=7/50,h_T=13/50\), \(u=S-s\), and let \(w\) be the original FullHold out width. Its binary rational is \(5764607523034235/288230376151711744\), and \(k_p=3/2\). For \(0<u\le 2b<w/8\), the kernel uses the complete R690 equation
\[
 \beta=k_pw\exp[-y^2-y^4(1+\sin y^4)],\qquad y=w/u .
\]
For any requested upper endpoint \(q>0\) in this tail, choose \(Y=\min(32,w/q)\). Each \(y^j e^{-y^2}\) with \(j\le9\) decreases for \(y\ge Y\). Since \(e>8/3\), write \(B=(3/8)^{\lfloor Y^2\rfloor}\). R690 (3),(6) give
\[
 0\le\beta\le M(q)=k_pw B,\qquad
 |\beta'|\le k_p B(2Y^3+8Y^5+4Y^9).
\]
At the single point \(u=0\), both are exactly zero. The cap on \(Y\) only enlarges the bounding interval. Every turn to \(u=0\) occurs in the enclosed expression. The coordinates on the pure interval \(0\le u\le b\) use
\[
 u(1-M(q)^2/2)\le x(u)\le u,\quad 0\le h(u)\le uM(q).
\]
These inequalities also handle a cell containing \(u=0\).

On \(b\le u\le2b\) let \(v=(u-b)/b\), \(\chi=S_5(v)\), \(J(v)=5v^4/2-3v^5+v^6\), and \(\alpha_0=bJ(v)/d\). Integration by parts in R732 (4) gives
\[
 \alpha-\alpha_0=(1-\chi)\beta+\int_b^u \chi'\beta .
\]
The two nonnegative weights sum to one. Thus the difference lies in \([0,M(q)]\), with \(q\) any valid upper bound for \(u\). The complete signed curvature enclosure is \((1-\chi)[-\sup|\beta'|,\sup|\beta'|]+\chi/d\). Both coordinate primitives differ from their ideal integrals by at most \(bvM(2b)\), because sine and cosine are 1-Lipschitz. The exit angle satisfies \(A\in b/(2d)+[0,M(2b)]\).

On the constant-curvature portion \(\alpha=A+(u-2b)/d\), and the increments in \(x,h\) from \(2b\) are \(d(\sin\alpha-\sin A),d(\cos A-\cos\alpha)\). Its endpoint \(u_c=2b+d(\pi/2-A)-b/2\) has angle \(\pi/2-b/(2d)\). For the following eased turn let \(v=(u-u_c)/b\) and \(\delta=\pi/2-\alpha=(b/d)(1/2-v+J(v))\). Its exact curvature is \((1-S_5(v))/d\). The integral pair in \(v\) is \((\sin\delta,\cos\delta)\). The kernel builds the complete rational polynomial of each sine/cosine Taylor approximation through order 16 for this piece and the ideal blend. It integrates each coefficient exactly. At a variable upper endpoint \(v\), the integrated remainder has absolute value at most
\[
 v \,(b/(2d))^{17}/17!.
\]
The actual integrands are nonnegative on both intervals, so endpoint primitive bounds enclose all intermediate limits. The same outward interval trigonometric kernel encloses all other sine/cosine factors and Machin's formula encloses \(\pi\).

At \(u_f=u_c+b\), \(x_f,h_f\) are intersected with R732 (5)'s independent \([d,d+5b/2]\). The vertical portion has \(x=x_f,\ h=h_f+u-u_f,\ \alpha=\pi/2,\ \alpha'=0\). The complete scalar data for the central curve are
\[
 L=u_f+h_T-h_f,\quad R_v=R+x_f,\quad Z=H_0-h_T,\quad C=S-L.
\]
The generated evidence records both proofs, exact width and curvature, \(A,u_c,u_f,L,R_v,Z,x_f,h_f,C\) and all transition addresses. It preserves the original \(S\) separately for every physical address.

## Central polynomial, integral and root

The degree-five Bernstein controls are R732 (8). With \(\eta=1/512,\ \lambda=(5/4)k_0\eta^2\), define controls \(A=(1,1,1,0,0,0), B=(0,0,0,1,1,1), D=(0,0,1,0,0,0)\). The uncontracted horizontal vector is \(A\Gamma+B R_v e+D\lambda\rho n\). The vertical polynomial is \(ZB+\eta\,\mathrm{Bernstein}(0,1,2,-2,-1,0)\). The horizontal multiplier is \(1-\xi[1-(2t-1)^{12}]^7\). The degree is at most 89. The \(\rho n\) angular rows are
\[
 \rho n,\quad \rho'n+\rho t_{\rm ang},\quad
 (\rho''-\rho)n+2\rho't_{\rm ang}.
\]
All \(\rho,\rho',\rho''\) use the original 160 coefficient slots. Power coefficients are exact. Centered rational polynomial bounds give all derivatives on the complete parameter intervals.

For \(V=|G_t|\), the full integrals of \(V,V_\xi,V_{\xi\xi},V_\varphi,V_{\xi\varphi},V_{\varphi\varphi}\) come from interval Taylor integration. The original partition, even Taylor degree, width target, split budget, complete positive-speed tests and evidence are retained. Each cell accumulates its full interval remainder and intersects it with the whole-cell integrand range. The interval for the fixed-\(\varphi\) candidate residual includes subtraction of the complete \(C\). For \(L_c(\xi,\varphi)=\int V\), R732 gives \(L_c(0)<99/50<C<L_c(3/4)\) with \(L_c(3/4)>41/20\). Convexity gives a true-root slope of at least \(\sigma=(\underline C-99/50)/(3/4)>0\) and the global estimate \(|\xi-\xi_*|\le |L_c(\xi)-C|/\sigma\). The saved binary root only centers this estimate. An optional mean-value step uses \(L_{c,\xi}>0\) on its entire segment. Implicit differentiation uses
\[
 \xi'=-L_\varphi/L_\xi,\qquad
 \xi''=-(L_{\varphi\varphi}+2L_{\xi\varphi}\xi'+L_{\xi\xi}(\xi')^2)/L_\xi .
\]
The original root-record attribution retains each integral, cell, saved word, model, point and fixed-target identity.

For \(\ell(t,\varphi)=\int_0^t V\) along the accurate root, suffix integration subtracts from \(C\). The inverse for a central material query satisfies \(\ell=s\). The denominator for every interval Newton step is the complete segment speed. At fixed \(s\),
\[
 t_\varphi=-\ell_\varphi/V,\qquad
 t_{\varphi\varphi}=-(\ell_{\varphi\varphi}
     +2V_\varphi t_\varphi+V_t t_\varphi^2)/V .
\]
The normalized tangent uses the derivatives of \(G_t\) along this inverse, including the implicit \(\xi\) and both \(t\) angular jets. \(F_s=T\), and \(F_{ss}=G_{tt}/V^2-G_t(G_t\cdot G_{tt})/V^4\). The output also records \(F,F_\varphi,F_{s\varphi},F_{\varphi\varphi},T_{\varphi\varphi}\). This yields \(F_{ss}=k_0\rho n\) at the exact core and a vertical tangent with zero second meridional and mixed derivatives at \(Q\), as proved in R732.

## Cross-piece boxes and same-point use

For every closed input with original affine endpoints \(s_i=a_i S+b_i\), the kernel forms the backward addresses \((1-a_i)S-b_i\) before enclosure. Thus a cap endpoint stays exactly \(u=0\), even when \(S\) has nonzero enclosure width. All possible intersections with the central branch and each of the five terminal pieces are retained. On an uncertain central crossover, the inverse is evaluated on the range of \(\min(s,C)\). Every actual central point belongs to this range. The constant endpoint extension supplies a valid central boundary value for possible overlaps of the enclosing scalar boxes.

In every terminal piece, let \(c=\cos\alpha,\ s_\alpha=\sin\alpha,\ k=\alpha', r=R+x\). The returned formulas are
\[
 F=re+(H_0-h)e_z,\quad T=-ce+s_\alpha e_z,\quad
 T_s=-k s_\alpha e-kc e_z,\quad
 T_\varphi=-ce',\quad T_{\varphi\varphi}=-ce'',\quad
 F_\varphi=re',\quad F_{\varphi\varphi}=re'' .
\]
Together with \(F_s=T,F_{ss}=T_s,F_{s\varphi}=T_\varphi\) these cover every requested role. The final result includes every touching branch and the hull of each individual component. The pure attribution checks the branch list, actual closed material domain, full mathematical-input identity, six positional rows and four tangent rows. It checks that each hull encloses all contributing rows.

The numerical caller must supply the complete original fixed scalar/chart data, including the actual width and curvature from its source-bound tail, and one selected immutable point/model/target/snapshot chain. Its three saved binary root/angle words are candidates with their own provenance. The numerical length residual, the normalized working inverse and the working tangent primitive do not establish exact unit speed for the stored words. All comparisons to those words require actual records and outward errors. Exact metric on \(0\le u\le b\) is a property of the reference. Every original outer radial control, normal stage, angular interval and geometry obligation retains its independent role. This delivery has no empirical results for the corrected field, its metric, reach, a CK width, or a new admissible point.
