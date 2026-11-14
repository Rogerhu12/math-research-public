# R43 supplement: the actual nonconstant physical cut has a strong connector

The old operator's negative root collar now connects to the actual physical
cut used by the complete R46 strict certificate. This result includes the
full graph conormal, normal shear, angle change, height normalization,
both amplitude rows, all mean matrices and ordinary sources with their
exact stated norms. It does not replace the cut by a constant canonical
section.

Set \(r_c=268136140016943/1125899906842624\) and \(L=1/4000\).
The preceding true chart gives the actual graph \(\xi=\chi_p(\phi)\),
uniformly for every parameter of the unchanged step5 family:

\[
 .000240160024215254<\chi_p(\phi)
                <.000248188362538822<L.                    \tag{P.1}
\]

Use the complete scaled norm
\(\|u\|_{H_N^s}^2=\sum_n(1+n^2/N^2)^s|u_n|^2\).
At \(N=1048576\), the executed directed consumer proves

\[
\begin{split}
 \|\mathcal T_{\rm root\to cut}\|_{E_N^s\to E_N^s}
     &<2.659478\,10^{34},\\
 \|\mathcal T_{\rm cut\to root}\|_{E_N^s\to E_N^s}
     &<2.960463\,10^{35},\qquad |s|\le10,\\
 \|\mathcal T_{\rm root\to cut}-\mathcal M:
                  E_N^s\to E_N^{s+4/3}\|
     &<2.226262\,10^{43},\qquad |s|\le8.                   \tag{P.2}
\end{split}
\]

The full model \(\mathcal M\) is specified in (P.31). Its first root phase
is the original R43 phase. Its regular-cut phase includes the actual Airy
geometric correction, and its graph phase uses the complete potential and
density. Every frequency remains in the evolution. These finite bounds
close this physical-cut interface; they are not a small-feedback estimate
or a final R104 cutoff.

## 1. The actual graph has a complete complex strip

Use the full seven-field potential report and complete canonical-domain
report already consumed by the full-root Airy operator. Let
\(S_1=3/2000\), \(e<.028750705256\), and \(U_-,M_U\) be its
complete lower real-part and modulus bounds for \(U_0\).
At the fixed true physical radius \(\rho_c=t(p)-r_c\),

\[
 \phi_\theta=U_0(F_++F_-),\qquad
 |\phi_\theta|\ge2U_-(1-e)>0.
\]

A complex \(\phi\) segment of length at most \(1/40000\), lifted at
this fixed \(\rho_c\), stays in the paid half physical angle strip,
because \((1/40000)/[2U_-(1-e)]<S_1/2\).
The exact graph identity gives

\[
 \chi_\phi=\frac{F_+-F_-}{(F_++F_-)\sqrt\chi},\qquad
 |\chi_\phi|\le
 \frac{e}{1-e}[\rho_{c,-}(1-e)^{2/3}]^{-1/2}
 <1.913023687023=:B_\chi.                                 \tag{P.3}
\]

Thus the true graph, with its actual quarter period, is analytic on
\(|\Im\phi|\le1/40000\). This is an inverse lift of the same chart,
not an approximate Fourier graph.

For the graph field calculations take \(\sigma_g=1/400000\).
The graph moves from its corresponding real point by at most

\[
 B_\chi\sigma_g<4.782559218\,10^{-6}<10^{-5}/2.
\]

Consequently the foliation below has
\[
 \Xi_-:=\chi_--B_\chi\sigma_g\le|\xi|
       \le\Xi_+:=L+B_\chi\sigma_g,\qquad \Xi_->0,           \tag{P.4}
\]
strictly inside the earlier canonical potential halo. Complete derivative
bounds at this complex image are
\[
 |V_\xi|\le\frac{M_V}{10^{-5}-B_\chi\sigma_g},\qquad
 |V_\phi|\le\frac{M_V}{1/40000-\sigma_g}.                  \tag{P.5}
\]
These are new interior Cauchy estimates; the earlier real-radial derivative
estimate is not applied at a complex radial point.

## 2. Exact foliation, conormal and shear

Normalize \(x=q\phi\) to period \(2\pi\), and put
\[
 a(x)=L-\chi(x/q),\quad \beta=q a_x,\quad
 \xi=L-ta(x),\quad D=1-\xi t^2\beta^2,\qquad 0\le t\le1.    \tag{P.6}
\]
The real gap satisfies \(a\ge1.81163746117889\,10^{-6}>0\).
The exact pullback of the positive divergence density has
\[
 \boxed{
 A=D/(qa),\quad B=\xi t\beta,\quad C=-q\xi a,\quad
 d=aV/q,\quad \mu=\sqrt{B^2-AC}=\sqrt\xi .
 }                                                       \tag{P.7}
\]
The absolute coordinate determinant is used when time reverses.
The complete conormal and source are
\[
 \boxed{
 p_t=-[U_\xi+\xi t\chi_\phi U_\phi]/q,\qquad
 f_t(t,x)=a(x)f_c(L-ta(x),x/q)/q .
 }                                                       \tag{P.8}
\]
At \(t=1\), this is the full canonical graph conormal. It is not just
\(U_\xi\).

The complete normal shear is
\[
 T=\tfrac12[A(\log\mu)_t+B(\log\mu)_x]=-1/(4q\xi).          \tag{P.9}
\]
Indeed \((\log\mu)_t=-a/(2\xi)\) and
\((\log\mu)_x=-t a_x/(2\xi)\); their quadratic angular terms cancel.
Both this shear and the conormal sign are kept.

The complete complex tilt is
\(\sqrt{\Xi_+}B_\chi<.030535511224<1/8\). Hence \(D\) never
vanishes, and on the real foliation \(A>0\).
We do not require \(a\) to be nonzero on the larger complex strip.
The original second-order time coefficient may have a complex pole;
the canceled composites actually used in the proof remain analytic.

## 3. Exact characteristics and the canceled full residual

For \(\tau(\xi)=2\xi^{3/2}/3\), the actual labels are
\[
 S_\sigma(t,x)=x+\sigma q[\tau(L)-\tau(\xi)],\qquad
 S_{\sigma,x}=1+\sigma t\sqrt\xi\,\beta.                  \tag{P.10}
\]
They satisfy \(D_\sigma S_\sigma=0\), with
\[
 D_\sigma=\partial_t+a w_\sigma\partial_x,\qquad
 w_\sigma=-\sigma q\sqrt\xi/(1+\sigma t\sqrt\xi\,\beta).
\]
Set
\[
 \kappa=\sqrt{\Xi_+}B_\chi,\quad
 C_J=(1+\kappa)/(1-\kappa),\quad X=q_-\sigma_g,\quad
 \delta_f=X/(4C_J^2).                                    \tag{P.11}
\]
The exact map/inverse lifts preserve the field strip: relative-flow
imaginary displacement is at most \(C_J\) times the input displacement.
The smaller \(\delta_f>2.15073638420584\,10^{-5}\) also pays the
inverse-label composition in the transported phase. On this strip the
labels and inverses have derivative modulus at most \(C_J\) and
\[
 \Re H'\ge c_J:=(1-\kappa)/(1+\kappa)^2>0.                 \tag{P.12}
\]
For the inverse this follows directly by taking the real part of
\(1/z\) with \(|z-1|\le\kappa\).

The complete reduced potential and first transport equation are
\[
 F_0=V+5/(16\xi^2),\qquad
 \mathcal F=\mu^{1/2}P(\mu^{-1/2})=aF_0/q,                 \tag{P.13}
\]
\[
 m=\xi^{-1/4},\quad D_\sigma h_\sigma=g_\sigma,\quad
 h_\sigma(0)=0,\quad
 g_\sigma=a g_{0,\sigma},\quad
 g_{0,\sigma}=F_0/(2q\sqrt\xi\,S_{\sigma,x}).               \tag{P.14}
\]
Equation (P.13) is covariance of the same full operator, including the
zero-order part.

The complete R46 residual is
\(P(mh)=m[\mathcal Fh+A D_\sigma g+2\sigma\mu g_x+B_rg]\),
where \(B_r=A_t+B_x-A(\log\mu)_t-B(\log\mu)_x\).
Its apparent inverse gap cancels exactly:
\[
\begin{split}
 A D_\sigma g&=(D/q)[D_\sigma g_0+w_\sigma a_xg_0],\\
 2\sigma\mu g_x&=2\sigma\sqrt\xi(a_xg_0+a(g_0)_x),\\
 aB_r&=-2\xi t\beta^2/q+a\xi t\beta_x+a/(2q\xi).           \tag{P.15}
\end{split}
\]
In the last line the \(t^2\beta^2/q\) pieces from \(A_t\) and \(B_x\)
first cancel. The logarithmic pieces then give \(1/(2q\xi)\).
Thus all of (P.13)–(P.15) are analytic on the wider graph strip even at
a complex zero of \(a\). Real \(a>0\) is still used to define the
actual time foliation.

Here are the complete scalar majorants used by the executable. Put
\[
\begin{gathered}
 A_+=a_++B_\chi\sigma_g,\quad \mu_\pm=\sqrt{\Xi_\pm},\\
 B_x^\chi=B_\chi/[q_-(1/40000-\sigma_g)],\quad A_x=B_\chi/q_-,\\
 M_0=M_V+5/(16\Xi_-^2),\quad
 M_1=M_{V_\xi}+5/(8\Xi_-^3),\quad s_-=1-\kappa .
\end{gathered}
\]
Then
\[
\begin{split}
 G_0&=M_0/(2q_-\mu_-s_-),\\
 J_t&=\mu_+B_\chi[1+A_+/(2\Xi_-)],\\
 J_x&=\mu_+[B_x^\chi+A_xB_\chi/(2\Xi_-)],\\
 G_t&=[A_+M_1+M_0(A_+/(2\Xi_-)+J_t/s_-)]/(2q_-\mu_-s_-),\\
 G_x&=[M_{V_\phi}/q_-+A_xM_1+
            M_0(A_x/(2\Xi_-)+J_x/s_-)]/(2q_-\mu_-s_-).
                                                               \tag{P.16}
\end{split}
\]
These bound \(g_0,(g_0)_t,(g_0)_x\), respectively.
Let \(W=q_+\mu_+/s_-\), \(D_+=1+\Xi_+B_\chi^2\),
\(H=A_+G_0\), and
\[
 B_a=2\Xi_+B_\chi^2/q_-+A_+\Xi_+B_x^\chi+A_+/(2q_-\Xi_-).
\]
The complete residual is bounded by
\[
 \Xi_-^{-1/4}\left[
 (A_+M_0/q_-)H+
 (D_+/q_-)(G_t+A_+WG_x+WA_xG_0)
 +2\mu_+(A_xG_0+A_+G_x)+B_aG_0\right].                  \tag{P.17}
\]
The directed result is
\[
 |h_\sigma|<80.823452368,\qquad |P(mh_\sigma)|<779486.161628.
                                                               \tag{P.18}
\]
Both remaining momentum fields also have exact canceled bounds:
\[
 \left|\frac{m\mathcal F}{2\nu}\right|
 \le\frac{m_+D_+M_0}{2q_-^2\mu_-},\qquad
 \left|\frac{\mathcal F}{2\mu\nu S_{\sigma,x}}\right|
 \le\frac{D_+M_0}{2q_-^2\Xi_-s_-}.                       \tag{P.19}
\]

## 4. Complete Cauchy energy and scaled derivative hierarchy

The true first-order coefficients are
\[
 \alpha=qa/D,\quad \gamma=q\xi a/D,\quad
 v=q\xi t\beta a/D,\quad d=aV/q.
\]
All four are analytic on width \(X\), without a complex inverse gap.
Their recorded complete moduli give real derivatives \(j!M_f/X^j\)
through order eleven.

Use the real positive energy
\[
 e_j^2=\int(|\partial_x^ju|^2+
              \gamma|\partial_x^{j+1}u|^2+
              \alpha|\partial_x^jp|^2).
\]
After exact integration by parts the base matrix has diagonal
\[
 v_x,\quad (\partial_t+v\partial_x)\log\gamma-v_x,\quad
 (\partial_t+v\partial_x)\log\alpha-v_x
\]
and only the \(u,p\) off-diagonal \(\sqrt\alpha(1-d)\).
The \(u_x,p\) terms cancel. Direct differentiation of the rational
coefficients, with the positive real gap, proves
\[
 g_0<.069892076775,\qquad
 \sup(|v_x|+|\nu_x|)<.138122035930=:\chi_1.
\]
The executable uses the seven-term lower-triangular Leibniz majorants
already proved in the R46 triangular supplement. The diagonal is
\(g_0/2+j\chi_1\). Replacing \(e_j\) by \(N^{-j}e_j\) changes
each lower entry \(C_{j\ell}\) to \(N^{-(j-\ell)}C_{j\ell}\);
it leaves the diagonal unchanged. The full comparison is \(\exp C_N\).

For \(0\le k\le10\), define
\[
 E_{k+1/2,N}=\sqrt{h_+(N)/h_-(N)}
       \|W_k(\exp C_N)^{[k]}W_k^{-1}\|_2,\quad
 W_k=\operatorname{diag}\sqrt{\binom kj},                 \tag{P.20}
\]
\[
 h_-=\min(1,N^2\gamma_-,\alpha_-),\qquad
 h_+=\max(1,N^2\gamma_+,\alpha_+).
\]
These factors compare \(1+\gamma n^2\) to \(1+n^2/N^2\).
The necessary \(N^2\) is included. There is only one final norm
conversion; the same absolute matrix covers reverse time and subintervals.
The exact Green flux gives negative half-integer bounds, and interpolation
gives the full real window.

The base diagonal exponential is \(<1.035563827\), while the tenth-order
diagonal exponential is \(<4.121290728\), independently of \(N\).
All scaled higher commutators, eleven half-integer bounds and the actual
energy equivalence are stored separately. At \(N=1048576\),
\(\max_kE_{k+1/2,N}<167843.486\).

Duhamel retains the ordinary input \(L^1(dt;H_N^{s-1/2})\) for the
actual source (P.8), with both Cauchy components. No weak source is
renamed to this input.

## 5. Multipliers, full compositions, cross signs and the normal frame

For an entire coefficient of modulus \(M\) on width \(\delta\), form
\[
 T^{f,N}_{j\ell}=\binom j\ell(j-\ell)!M/(N\delta)^{j-\ell}.
\]
The weighted matrix \(W_kT^{f,N}W_k^{-1}\) bounds its full multiplier.
Negative orders use its true adjoint, and fractional orders interpolate.
The executable takes the maximum over the required integer levels. This
retains the zeroth-order bound \(M\), rather than introducing an unnecessary
\(1/\delta\) fee at order zero.

For a label or inverse, the full Bell coefficients \(b_{j\ell}\) obey
the majorants \((j-1)!C_J/(\delta_f/2)^{j-1}\) for its derivatives.
Use \(N^{-(j-\ell)}b_{j\ell}\) and the true \(L^2\) Jacobian factor
\(\sqrt{C_J}\). The negative-order composition additionally pays the
inverse-Jacobian multiplier. All positive and negative integer bounds
through eleven, and both complete matrices, are saved.

The cross-sign and mean-output bound is a complete contour estimate.
If \(\Re H'\ge c>0\) on its complex strip and \(|a_0|\le M\),
then for opposite signs or output zero,
\[
 |(M_{a_0}C_H)_{kj}|\le M e^{-d(|k|+|j|)},\qquad
 d=c\delta_f/2.                                          \tag{P.21}
\]
Shift the periodic contour by \(\pm\delta_f/2\) with the input sign.
The imaginary part of \(H\) has that sign and magnitude at least
\(c\delta_f/2\), and the output exponential also decays.
All squared matrix weights are summed with positive exact geometric
formulas, including every finite and infinite frequency.
The consumer also takes the lesser of that estimate and
\[
 \|K:H_N^r\to H_N^{r+g}\|
 \le\|K:H_N^r\to H_N^r\|
       +N^{-g}\||D|^gK:H_N^r\to H_N^r\|,\quad g=1,2,    \tag{P.22}
\]
where the second term uses (P.21). This follows from
\(\langle D/N\rangle\le1+|D|/N\) or its exact squared identity.
The first term is the actual same-order multiplier/composition norm.
No intermediate head path is removed.

The complete R46 normal frame remains
\[
 \mathscr Fz=2^{-1/2}
 \binom{m\Lambda^{-1/2}(z_++z_-)}
 {-Tm\Lambda^{-1/2}(z_++z_-)+i\sqrt\mu\Lambda^{1/2}(z_+-z_-)} .
\]
Here \(\Lambda_n=\max(1,|n|)\), including zero.
In scaled spaces the negative half power gains \(1/2\) with norm
\(\le2^{1/4}\), and the positive half power loses \(1/2\) with norm
\(\le\sqrt N\).
If \(M_m,M_\mu,M_T\) bound \(m,\sqrt\mu,T\), the paid frame constants are
\[
\begin{split}
 u_*&=2^{1/4}M_m,\\
 F_*&=[u_*^2+(M_Tu_*+\sqrt N M_\mu)^2]^{1/2},\\
 I_*&=[NM_\mu^2+\sqrt2M_m^2(1+M_T^2)]^{1/2}.             \tag{P.23}
\end{split}
\]
The same positive \(\sqrt N\) fee is kept for \(Q_H\) and cross-cone
operators.

Use the exact R46 model \(\mathcal W_g\) with (P.10), the actual
\(\widehat h=h\circ S^{-1}\), all four branch/cone combinations and
the mean \(\Pi_0 I\). The true source correction, (P.17), initial
defect (P.19), frame (P.23), and all ordering terms prove
\[
 \mathcal C_g=\mathcal W_g+R_g,\qquad
 R_g:E_N^s\to E_N^{s+2}.                                 \tag{P.24}
\]
The ordering fee is
\(2\sum_l(1+|l|/N)^{10}|l||\widehat h_l|\), with its full tail.
At \(N=1048576\),
\[
 \|\mathcal C_g\|,\|\mathcal C_g^{-1}\|<2.376752\,10^{10},
 \quad \|\mathcal W_g\|<2056519,\quad
 \|R_g\|_{s\to s+2}<1.498856\,10^{17}.                    \tag{P.25}
\]
The actual mean difference \(\mathcal C_g\Pi_0-\Pi_0\), including
its infinite output, is paid by the same Cauchy and frame bounds.

More explicitly, the executable uses the R46 formula
\[
 R_g\le C_{\rm err}+4(2X+L_{\rm mom}+Q_*K_{\rm ord}),
\]
where
\(C_{\rm err}=I_*E[d_{\rm init}+\mathcal R+F_*]+1\),
\(\mathcal R=4\,2^{1/4}N_{\rm comp}M_{19/2,N}(Pmh)\),
\(d_{\rm init}=2^{3/4}M_{19/2,N}(m\mathcal F/(2\nu))\),
\(L_{\rm mom}=2M_{19/2,N}(\mathcal F/(2\mu\nu S_x))N_{\rm comp}\),
\(Q_*=2^{1/4}\sqrt N N_{\rm comp}\), and
\(X=\sqrt N[2^{1/4}X_{s+1/2,2}+2^{3/4}X_{s+3/2,1}]\).
Every multiplier, full composition and cross bound in this expression
was defined above. This also states all scaled modifications to the
original R46 consumer.

## 6. Actual physical angle and its exact mean normalization

At the physical cut put \(z=4\theta\) and
\(H(z)=q\phi(\rho_c,z/4)\). The actual degree-one map satisfies
\[
 \Re H'\ge(q_-/4)(2U_--2M_Ue)>.426936236220,\qquad
 |H'|<2.987701243
\]
on \(|\Im z|\le4S_1\). Its inverse exists on the corresponding
positive-real-part image strip. The common map/inverse strip exceeds
\(.00128080870866\); all Bell and contour bounds are paid there.

The exact amplitude map is
\[
 \mathscr G_H=\tfrac12
 \begin{pmatrix}Q_H+P_H&Q_H-P_H\\Q_H-P_H&Q_H+P_H\end{pmatrix},
 \quad Q_H=\Lambda^{1/2}C_H\Lambda^{-1/2},\quad
 P_H=(Q_H^{-1})^*.                                      \tag{P.26}
\]
The full positive height normalization cancels exactly in this frame.
A boundary-preserving radial change also has
\(p_{\rm new}=H'p_{\rm old}\) and \(T_{\rm new}=H'T_{\rm old}\):
its radial scale cancels in the normal density. Thus no additional
unpaid height or tilted-normal multiplier is hidden in (P.26).

For nonzero same-sign indices \(P_{kj}=Q_{kj}\) exactly.
All remaining cross signs and mean rows are covered by (P.21).
The distinct mean input \(P_He_0=\Lambda^{-1/2}H'\) is also paid.
At \(N=1048576\),
\[
 \|\mathscr G_H\|,\|\mathscr G_H^{-1}\|<1.074023\,10^9,\qquad
 \|\mathscr G_H-\operatorname{diag}(Q_H,Q_H)\|_{s\to s+2}
       <1.144669\,10^8.                                  \tag{P.27}
\]

Return from normalized \(z\) to the native physical \(\theta\)-frame.
Its exact amplitude map \(D_4\) equals \(2I\) for nonzero modes, while
\[
 \boxed{D_{4,0}=\tfrac12
             \begin{pmatrix}5&-3\\-3&5\end{pmatrix}}       \tag{P.28}
\]
on the mean. The mean height combination \(r\) stays fixed and its
momentum combination \(t\) multiplies by four. For nonzero modes the
square-root physical frequencies \(4|n|\) instead multiply both
combinations by two. Hence \(\|D_4\|\le4\),
\(\|D_4^{-1}\|\le1\).
Using physical derivative scale \(4N\) in the strict region gives the
same scalar weights \(1+n^2/N^2\); the physical \(\Lambda\) itself
has not been changed.

## 7. The full fixed-\(L\) Airy interface, including its finite head

Let \(F_0(L)\) be the original R39 free-Airy matrix. First take the
inward normal frame with conormal \(U_\xi/q\) and \(T=1/(4qL)\):
\[
 \Phi=F_{\rm normal}(L)^{-1}\operatorname{diag}(1,1/q)F_0(L).
                                                               \tag{P.29}
\]
Its determinant at every frequency is
\(\gamma_0^2=2c^2/(\pi q)\), with
\(\gamma_0=\sqrt{2/\pi}\,c\,q^{-1/2}\).
The exact mean comes from
\(D_\pm=c(1\pm iL/\pi)\), \(D'_\pm=\pm ic/\pi\).
It is retained as \(\Phi_0\), not replaced by a nonzero-frequency limit.

For nonzero modes set
\[
 (\Phi_{\rm app})_\tau
 =\gamma_0e^{i\tau(q|n|\tau(L)+\pi/4)}
       [1-5i\tau/(48q|n|L^{3/2})],                       \tag{P.30}
\]
and set its mean exactly to \(\Phi_0\).
This is the unchanged R46 geometric correction after the complete shear.

R46 §8 proves
\(\sqrt\pi|Z-Z_{\rm app}|,\sqrt\pi|Z'-Z'_{\rm app}|
 \le1/(4\eta^2)\) for
\(\eta=2q|n|L^{3/2}/3\) and \(L(q|n|)^{2/3}\ge1\).
The exact normal-frame combinations are
\(r=cZ/\sqrt q\), \(t=-icZ'/\sqrt q\).
The derivative of the first correction adds \(A_*/\eta^2\),
\(A_*=5/72\). The full two-by-two matrix error is therefore at most
\(\gamma_0(A_*+1/2)/\eta^2\).

The common transition threshold is \(n_A=6507\).
Above it, the full scaled order-two bound is
\[
 \frac{9\gamma_{0,+}(A_*+1/2)}{4q_-^2L^3}
                       (n_A^{-2}+N^{-2}).
\]
For every \(1\le|n|<n_A\), the entire R39 negative-axis function and
derivative bounds in (P.29) give
\(\|\Phi\|<1011.420586\),
\(\|\Phi^{-1}\|<45035.511905\).
The inverse bound also follows from the exact two-by-two determinant.
The finite-head error is bounded by
\((\|\Phi\|+\|\Phi_{\rm app}\|)[1+(n_A/N)^2]\).
No finite column is omitted or treated as an asymptotic column.
At \(N=1048576\), the maximum gives
\(\|\Phi-\Phi_{\rm app}\|_{s\to s+2}<1350.341662\).

The graph time reverses the inward \(\xi\) direction. Conormal and
shear both reverse, so its true initial conversion is \(J_b\Phi\),
where \(J_b\) is the exact branch swap, including the mean.

## 8. Full operator, full model, source and strong composition

Let \(C_0(L,0)=I+B_{\rm original}+R_r\) be the completed full-root
R43 operator. Then
\[
\begin{split}
 \mathcal T_{\rm root\to cut}
   &=D_4\mathscr G_H\mathcal C_gJ_b\Phi C_0(L,0),\\
 \mathcal M
   &=D_4\operatorname{diag}(Q_H,Q_H)\mathcal W_gJ_b
                             \Phi_{\rm app}(I+B_{\rm original}).
\end{split}                                               \tag{P.31}
\]
All actual labels, inverse phase compositions, four branch/cone
combinations, \(\pi/4\) factors and mean matrices are specified above.
The first root phase \(B_{\rm original}\) is unchanged.

Writing the corresponding full order-zero bounds as
\(G,W_g,\Phi_*,\Phi_{\rm app,*},C_r\), a complete strong bound is
\[
 4[G R_g\Phi_*C_r+G W_gR_\Phi C_r+
          R_GW_g\Phi_{\rm app,*}C_r+
          G W_g\Phi_{\rm app,*}R_r].                     \tag{P.32}
\]
The first three remainders gain two derivatives and embed to \(4/3\).
The last has the actual full \(4/3\) root gain.
All intermediate orders are within the paid amplitude window
\([-10,10]\), with frame/composition orders through eleven.
This proves (P.2). The reverse Cauchy bound reverses the exact onto
factors; it does not invert the approximate model.

For an ordinary source defined on the paid canonical collar the exact
output is
\[
 D_4\mathscr G_H[
       \mathcal C_gJ_b\Phi\,\mathcal S_r f_c+\mathcal S_g f_t].
                                                               \tag{P.33}
\]
At \(N=1048576\) the two complete gains are
\[
 2.515028\,10^{31}\quad\hbox{for }
       \|f_c\|_{L^1(d\xi;H_N^{s-1/3})},\qquad
 2.354745\,10^{17}\quad\hbox{for }
       \|f_t\|_{L^1(dt;H_N^{s-1/2})}.
\]
These are two explicit norms for the same source after its exact
coordinate changes. A tilted change mixes radial and angular variables;
these Bochner norms are not identified with an untransformed physical
radial-angular norm.

For original-height data the exact conversion remains
\(f_c=\alpha_c^{-1/2}(f_{\rm gr}/J_\Psi)\circ\Psi^{-1}\),
where \(f_{\rm gr}=u_zf_{\rm original}\) when that ground state is used.
No weak divergence load is renamed to either ordinary source.
A source specified only on the root-to-cut region requires an actual
extension to the paid overlapping collar and its displayed norms.
Flux integrals and both mean source charges follow (P.8), (P.26),
and (P.28). The other root is obtained by the actual R77 radial
reflection of this entire operator, including conormal and source;
the same constants apply.

## 9. Executed artifacts and exact remaining scope

The new consumer is

    scripts/fourfold_negative_root_physical_graph_operator.py

The frozen full-root producer was run at one additional norm scale:

    notes/2026-11-13-negative-root-full-Airy-operator-additional-scale.json
    SHA256 e8bea2d84985897aa0930c3efd3f0669502ba086883bc9d3ec1fad3b855059bc

The completed graph report is

    notes/2026-11-13-negative-root-physical-graph-operator.json
    SHA256 e4b3faf5ae998607207246367a430d80a1fdac7e404d1b013e66b9c373124cb5

It stores all input identities and hashes, complete domain gates,
energy/composition matrices, all half-integer levels, source and frame
constants, the whole Airy transition head and exact mean formulas.
The last directed calculation took about 2.39 seconds.

| Norm scale | Full graph \(R_2\) | Full root-to-physical-cut \(R_{4/3}\) |
|---:|---:|---:|
| \(1\) | \(<5.088340\,10^{333}\) | \(<2.157130\,10^{507}\) |
| \(4096\) | \(<2.745771\,10^{104}\) | \(<1.559176\,10^{131}\) |
| \(16384\) | \(<2.387553\,10^{67}\) | \(<9.046449\,10^{90}\) |
| \(65536\) | \(<3.890437\,10^{35}\) | \(<7.828289\,10^{60}\) |
| \(1048576\) | \(<1.498856\,10^{17}\) | \(<2.226262\,10^{43}\) |

This is a change of complete norms, retaining all finite-head paths.
It is not an assertion that the last row closes the feedback.

From the topic directory, using python-flint 0.9.0 and fresh output paths:

    python3 scripts/fourfold_negative_root_full_Airy_operator.py \
      --scales 1 4096 16384 65536 1048576 \
      --out /tmp/root-additional-scale-recheck.json
    python3 scripts/fourfold_negative_root_physical_graph_operator.py \
      --out /tmp/root-physical-graph-recheck.json

The second command uses the installed exact additional-scale report unless
its input is explicitly changed. Source, dependency and actual input
hashes are checked. The arithmetic is 320-bit directed and all analytic
tails are complete.

The actual nonconstant negative root-to-strict-cut interface is now paid
in the stated complete spaces and source norms. This does not pay positive
Ai/contact, identify the final full returned \(b-\beta\), combine the
entire returned \(R_*\), invert its actual finite head Schur block, or
select a final effective feedback cutoff.

