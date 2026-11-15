# R133 supplement: two-input zero-width cap graph, mixed Fourier kernels and complete inner curvature ports

2026-11-15, visible-exact / newton_source.

**Analytic extension of the completed cap construction.** Both the inner nonmean curvature input and the normalized far height are now unknown zero-width functions. The auxiliary complex translation acts only on the known centre, residual and coefficients. It never evaluates either unknown input at a complex angle. The complete right B mean, C mean, holonomy mean and mean-height span remain in the graph.

The only numerical inputs are the completed weighted-Q gate and the already proved complete cap/long maps. No target, convolution, reference kernel, original integral or numerical derivative table is recomputed.

## 1. Fixed object and original complete maps

Keep exactly the fixed intrinsic parameter, original continuous 440866 repair of the ac1 M32 centre, true cap I=[9/10,25/8], and true finite long segment used in:

- [X: actual all-mode cap existence](R133-supplement-actual-all-mode-positive-cap-existence-at-repaired-M32-centre.md).
- [E: weighted-Q endpoint invariant set](R133-supplement-weighted-Q-endpoint-invariance-and-small-analytic-cap-ball.md).
- [F: full-periodic zero-width cap Phi and finite-Sobolev tame map](R133-supplement-actual-zero-width-full-periodic-cap-Phi-and-finite-Sobolev-tame.md).
- [Y: normalized moving readout and both means](R133-supplement-actual-cap-moving-readout-with-normalized-angle-and-both-means.md).

The published F input has SHA256
`3959bb3674bcbd119568299a28c7f6f96d9fb27c3f8348cfa65cbd0ae49a834a`.
Its F.4--F.7 already add the true B-mean right output on this actual unweighted cap. In particular its current mean lift is 1, not the inverse of an unrelated weighted-cap endpoint factor.

All angular labels below are the complete signed set 4Z. Set
$$
 \sigma_0=2^{-13},\quad h=\sigma_0/4=2^{-15},\quad
 r_\gamma=10^{-9},\quad r_B=2^{-60},\quad r_f=10^{-8},
$$
$$
 \rho=3\,10^{-6},\qquad \zeta=9.9\,10^{-10},\qquad
 r_Z=10^{-9},\qquad \kappa_*=2^{-36}.
 \tag{M.1}
$$
The inner parameter gamma is a physical nonmean C-curvature change at L. The far parameter f_B is the original normalized nonmean height. Their units are different. Physical far height is s_B f_B; physical height at the adjacent long end is s_R f_*, with the original positive scales retained.

## 2. Existence on the full zero-width product domain

Define the complete two-component space
$$
 \|x\|_{X_0}=\sum_{m\in4\mathbb Z}\sup_I|b_m|
               +\sum_{m\in4\mathbb Z}\sup_I|c_m|,
 \qquad x=(b,c).
$$
Let
$$
 \mathcal B_0=\{x:\|x\|_{X_0}\le\rho,\
                  \|c_{\ne0}(R)\|_{A^0}\le\zeta\}.
 \tag{M.2}
$$
Its coefficient functions are continuous on each actual common radial domain and matched continuously at the original artificial interfaces. Endpoint evaluation is bounded in this norm.

For arbitrary complex, nonmean, fourfold-periodic inputs require
$$
 \|\gamma\|_{A^0}<r_\gamma,\qquad
 \|f_B\|_{\dot A^2_0}<r_B.
 \tag{M.3}
$$
Neither input is assumed analytic. In the zero-width contraction proof the inner input appears only through the actual linear nonmean C-value lift, with the original bound H_C<3 and endpoint attenuation a_L. Its analyticity was needed in F only because that paper placed gamma among the known translated data. It is not needed to define the zero-width reference integral or to prove its norm bound.

Thus E/F give, uniformly on (M.3),
$$
 \|\mathcal T x\|
 <3.23\,10^{-7}+.879\rho+208\rho^2+2^{-80}<.99\rho,
$$
$$
 \operatorname{Lip}_{X_0}\mathcal T
 <.879+416\rho+2^{-49}<.881,\qquad
 \|(\mathcal T x)_{C,\ne0}(R)\|<.9\zeta.
 \tag{M.4}
$$
The actual coefficient gate is still the same completed
q_w<3.561348304031e-6; dropping its angular weight does not enlarge it.
The true outer input remains Z_0+c_ne(R), whose norm is below r_Z throughout the set. The full C_R inverse, not a reference substitute, is evaluated there.

The B mean is precisely
$$
 B_0(R)=\chi_R\left\langle(V-P)(D^{-1/2}-1)\right\rangle,
 \qquad
 B_0(r)=\frac{a(R)^2}{a(r)^2}B_0(R).
 \tag{M.5}
$$
Its value and Z derivative have the already paid bounds 2^-80 and 2^-49. The pure mean lift has zero direct C-ne endpoint component; its subsequent linear and quadratic Q couplings are already counted in (M.4).

Banach's theorem therefore gives a unique full fourfold-periodic value solution of the original integral equations in (M.2), together with its true long solution, on the whole product domain (M.3). The Codazzi equations hold in their corresponding weak sense; the finite-regularity statements below recover strong equations at the required orders. Both maps depend holomorphically on the two zero-width inputs. On reflection-symmetric analytic data uniqueness identifies this solution with X/F. It does not redefine the original scientific centre.

## 3. Mixed normalized input and complete output

Let D_theta=partial_theta and use |D_theta|^2 only on nonzero modes. Put
$$
 G=\gamma/r_\gamma,\qquad U=|D_\theta|^2f_B/r_B,\qquad
 \mathcal E=A^0_{\ne0}\oplus_1 A^0_{\ne0},
 \quad \|(G,U)\|_{\mathcal E}=\|G\|_{A^0}+\|U\|_{A^0}.
 \tag{M.6}
$$
The unit ball of this direct sum lies inside (M.3). The nonlinear value graph exists on the larger product domain; the direct sum is chosen to control all mixed Taylor coefficients without an artificial factor for the number of species.

Write the actual physical curvature W=hat W+x=(B,C). The following core outputs are kept:
$$
 \left(
 x/\rho,\quad |D_\theta|^2 f_*/r_f,\quad Z/r_Z,\quad
 \kappa(\cdot)/\kappa_*,\quad
 [v_0(\cdot)-v_0(0)]/[a_Rw_R\kappa_*]
 \right).
 \tag{M.7}
$$
The long mean and its height span are continuous functions of the long radial variable, read in their supremum norm. They are angular frequency-zero outputs. The original mean estimate gives
sup|kappa|<kappa_* and
sup|v_0(t)-v_0(0)|<a_Rw_R kappa_*/2.
No screening factor is attached to this height span.

All fixed physical cap traces are bounded linear reads of x:
$$
 C_{\ne0}(L)-\widehat C_{\ne0}(L)=\gamma,\quad
 B(L),\quad C_0(L),\quad B_0(L),
 \quad (B,C)(r)\text{ at each fixed true cut}.
 \tag{M.8}
$$
The last three inner quantities are outputs. There is no independently prescribed inner C mean, and B_0(L) is the nonzero value (M.5) for general data.

For completeness, further algebraic readouts can be put in the same normalized output without changing the contraction. Set
$$
 c_0(r)=\langle C(r)\rangle,\quad j=C/c_0,\quad
 p=I_\theta(j-1),\quad
 m=1/c_0,\quad \bar u=B_0/c_0,\quad
 A=(K+B^2)/C .
 \tag{M.9}
$$
The primitive has its actual zero physical mean. The known centre satisfies
|hat c_0|>1/6, ||1/hat C||<6, ||hat j||<2,
||hat u||<1/50 and the original complete H_*<2.
On the entire value ball,
$$
 |c_0|>1/7,\quad
 \|j-\widehat j\|_{A^0,\rm joint}<21\rho,\quad
 |m-\widehat m|<42\rho,
$$
$$
 |\bar u-\widehat{\bar u}|<7\rho,\quad
 \|A-\widehat A\|_{\mathscr A_0}<3\rho,\quad
 \|(B/C,1/C)-(\widehat B/\widehat C,1/\widehat C)\|_{X_0}<44\rho.
 \tag{M.10}
$$
Here hat B_0=0 for the fixed centre; the current B_0 is not set to zero.
For the Gauss readout one may use its exact linear terms
2 hat u b-H_*c and the complete remainder bounded by 13||x||^2.
The reciprocal estimates use the full denominator
1+(1/hat C)c, not the subtraction of two norm upper bounds.

Append to (M.7) the outputs
$$
 \frac{D_\theta(p-\widehat p)}{32\rho},\quad
 \frac{m-\widehat m}{64\rho},\quad
 \frac{\bar u-\widehat{\bar u}}{64\rho},\quad
 \frac{A-\widehat A}{4\rho},\quad
 \frac{(B/C,1/C)-(\widehat B/\widehat C,1/\widehat C)}{64\rho}.
 \tag{M.11}
$$
Use the maximum of the displayed output norms, with the two curvature components always in block-sum norm. Equations (M.4), (M.7), (M.10) make the resulting normalized output V have norm less than 1. These additional outputs use physical theta; they do not compose an unknown zero-width function with a complex inverse angle.

For real data C<0, the real map Phi(theta)=theta+p(theta) has derivative C/c_0>0 and degree one. Its real inverse gives the original moving readout. Exact change of measure gives
$$
 \langle v\rangle_\varphi=1/c_0,\qquad
 \langle u\rangle_\varphi=B_0/c_0,\qquad
 \langle\Theta-\mathrm{id}\rangle_\varphi
   =-\langle p(1+p_\theta)\rangle_\theta=0 .
 \tag{M.12}
$$
This retains both means and the original coordinate phase. It does not reset the separate Euclidean frame angle at every radius. For complex nonanalytic inputs (M.9)--(M.11) are algebraic physical outputs; no complex-angle evaluation of them is asserted.

## 4. Auxiliary complex parameter without translating either unknown input

For |Im z|<2h, translate only the known centre, its exact known residual and every known nonradial coefficient by theta->theta+z. Keep the radial reference, intrinsic functions and endpoints unchanged. In particular gamma is no longer part of this known family: it is the first independent unknown in (M.6).

The known joint A_sigma0 bounds control all these translated coefficients in A_sigma0/2. Thus (M.4) and all normalized output bounds remain uniform. The two unknown inputs stay in their original zero-width spaces. This constructs a holomorphic family V_z on the unit ball of E.

For real t, translation covariance of the full equations, the true C_R small root, both mean equations and uniqueness gives
$$
 V_t(T_tG,T_tU)=T_tV_0(G,U).
 \tag{M.13}
$$
The angular translation on scalar mean outputs is the identity. Fixed radial traces commute with it. All known subtractions in (M.11) translate with the centre. This is a covariance of the complete graph; it is not a claim that the unknown zero-width inputs admit complex translates.

## 5. Full mixed Taylor kernel

Expand at the zero pair:
$$
 V_z(Z)=\sum_{k\ge0}T_{k,z}[Z,\ldots,Z],
 \qquad Z=(G,U)\in\mathcal E .
 \tag{M.14}
$$
The coefficient T_k includes 1/k!. Banach-space Cauchy and complex polarization give
||T_k,z||<=k^k/k!<4^k for k>=1, with ||T_0,z||<1.

Let e_(s,n) be the Fourier basis vector in species s=gamma or f, with n in 4Z nonzero. For every output component the complete kernel satisfies
$$
 T_{k,t}(m;s_1,n_1,\ldots,s_k,n_k)
 =e^{it(m-\sum n_i)}T_{k,0}(m;s_1,n_1,\ldots,s_k,n_k).
 \tag{M.15}
$$
In radial outputs the absolute coefficient norm means its full radial supremum. Both sides are holomorphic in z, so real covariance identifies them on the whole auxiliary strip. Evaluate separately at z=ih and z=-ih and sum the two signed lag half axes:
$$
 \sum_m e^{h|m-\sum n_i|}
 |T_k(m;s_1,n_1,\ldots,s_k,n_k)|
 \le2\,4^k .
 \tag{M.16}
$$
All mean output rows are included with m=0. This is an actual complete kernel estimate, not an upgrade of an arbitrary bounded operator to an absolute matrix sum.

For each species-labelled input coefficient its absolute value is dominated by
a_i(n)=|G_i(n)|+|U_i(n)|. Summing over all species therefore gives exactly the convolution of these a_i. No factor 2^k is needed: it is already the expansion of the direct-sum norm.

## 6. One-high finite Sobolev bounds

Put
$$
 \|Z\|_{\mathcal E_q}=\|G\|_{H^q}+\|U\|_{H^q}.
$$
For curvature-type radial outputs use the genuine joint norm
$$
 \|v\|_{\mathfrak M_q}
 =\left(\sum_m\langle m\rangle^{2q}\sup_I|v_m|^2\right)^{1/2},
 \tag{M.17}
$$
with a block sum for a pair. It controls the corresponding L-infinity-r H^q norm. Scalar radial outputs use their supremum norm as frequency zero.

The pointwise consequence of (M.16) is a full convolution majorant with
K_h(l)=exp(-h|l|). For q>=0,
$$
 \begin{split}
 \|T_k[Z_1,\ldots,Z_k]\|_{\mathcal O_q}
 \le2\,4^k(k+1)^q\{&
 \|\langle\cdot\rangle^qK_h\|_{\ell^1}
             \prod_i\|Z_i\|_{\mathcal E}\\
 &+\|K_h\|_{\ell^1}\sum_i
       \|Z_i\|_{\mathcal E_q}
                  \prod_{j\ne i}\|Z_j\|_{\mathcal E}\}.
 \end{split}
 \tag{M.18}
$$
The normalized phase output in O_q is D_theta(p-hat p), and the normalized height output is |D_theta|^2 f_*.

Use the full signed estimates
$$
 \|\langle\cdot\rangle^qK_h\|_{\ell^1}
 \le2^{q+3}q!h^{-q-1},\qquad
 \sum_{k\ge0}(k+1)^p4^{-k}
 \le p!(4/3)^{p+1}.
 \tag{M.19}
$$
For noninteger q use ceil(q) only in these scalar moment and factorial bounds; the one high input in (M.18) remains H^q.

On the low ball ||Z||_E<=1/16, the entire mixed series, its first derivative and its second difference converge. A uniform convenient constant for 0<=q<=8160 is
$$
                    C_q=2^{112(q+32)+18432}.
 \tag{M.20}
$$
Indeed the exponents in F.19--F.22, with ceil(q)+4<=8164, are already below
64(ceil(q)+8)+8192. The fixed additional output count, direct-sum/Hilbert conversions and first two difference factors fit within (M.20). The constant is not multiplied once per Taylor factor.

The actual graph therefore obeys
$$
 \|V(Z)\|_{\mathcal O_q}\le C_q(1+\|Z\|_{\mathcal E_q}),
$$
$$
 \|DV(Z)H\|_{\mathcal O_q}
 \le C_q\{\|H\|_{\mathcal E_q}
                  +(1+\|Z\|_{\mathcal E_q})\|H\|_{\mathcal E}\},
 \tag{M.21}
$$
and, when the whole segment stays in the low ball,
$$
 \|V(Z+H)-V(Z)-DV(Z)H\|_{\mathcal O_q}
 \le C_q\{\|H\|_{\mathcal E}\|H\|_{\mathcal E_q}
          +(1+\|Z\|_{\mathcal E_q})\|H\|_{\mathcal E}^2\}.
 \tag{M.22}
$$
The corresponding derivative difference has the same one-high form. High norms are finite, not small. Fourier truncations converge by these difference estimates, and zero-width uniqueness identifies the limiting solution with the complete value graph. No density assertion for arbitrary pre-existing joint radial spaces is needed.

In original units, for example,
$$
 \|x\|_{\mathfrak M_q}
 \le\rho C_q\left(1+r_\gamma^{-1}\|\gamma\|_{H^q}
                       +r_B^{-1}\|f_B\|_{H^{q+2}}\right),
$$
$$
 \|f_*\|_{H^{q+2}}
 \le2r_f C_q\left(1+r_\gamma^{-1}\|\gamma\|_{H^q}
                       +r_B^{-1}\|f_B\|_{H^{q+2}}\right).
 \tag{M.23}
$$
The actual derivative inputs are r_gamma^-1 delta-gamma and
r_B^-1 |D_theta|^2 delta-f_B. All quantities in (M.11) are read with their displayed normalizations. In particular p-hat p has one extra angular derivative, while f_* has two. These are physical-angle statements.

## 7. Complete weak-direction windows at finite-jet backgrounds

The value map is not defined on arbitrary distributional input. A derivative at an actual finite-jet background does extend to the following weak spaces. This part may use the larger normalized background ball ||Z||_E<=1/2; it uses the complete value map on the unit ball, rather than summing the small-ball Taylor majorant.

Let
$$
 J_4=\sum_{j=1}^4
       \{\|\partial_\theta^jG\|_{A^0}
                       +\|\partial_\theta^jU\|_{A^0}\}<\infty,
 \qquad a=\frac{h}{1+J_4}.
 \tag{M.24}
$$
No smallness of J_4 is required. It is a fixed low-order quantity; for example H^5 of G and U controls it. Form the genuine finite parameter polynomial
Z^[4](z)=sum_(j=0)^4 z^j partial_theta^j Z/j!.
For |z|<a its norm is below 1/2+2h<3/4. Hence
A(z)=DV_z(Z^[4](z)) is a holomorphic A^0-direct-sum to O_0 operator with norm below 4.

The real covariance (M.13) and the finite chain rule identify its first four jets with ad_(partial_theta)^j DV_0(Z). They do not require a complex-angle value of either unknown input. Cauchy then gives, for either input species,
$$
 |(DV)_{m;s,n}|
 \le2^{70}(1+J_4)^4\langle m-n\rangle^{-4}.
 \tag{M.25}
$$
Both defined nonmean input species and every mean output are retained; the independent height constant lambda remains a separate scalar coordinate. This does not introduce an input mean into either species. For scalar outputs m=0 this is an actual decaying row bound.

After restoring the two f_B input derivatives, the two f_* output inverse derivatives, or the single p output inverse derivative as appropriate, all needed weight ratios are bounded by
$2\langle m-n\rangle^{3/2}$. For example the curvature row uses
$n^2\langle m\rangle^{-3/2}\langle n\rangle^{-1/2}$ for f_B, and
$\langle m\rangle^{-3/2}\langle n\rangle^{3/2}$ for gamma. The height row uses the analogous nonzero-output $m^{-2}$ factor. Thus the complete two-sided Schur sum
$\sum_{\ell\in4\mathbb Z}\langle\ell\rangle^{-5/2}<4$ is finite.

A single explicit physical-unit constant valid for the normalized-height convention is
$$
                         C_{\rm weak}=2^{144}(1+J_4)^4 .
 \tag{M.26}
$$
It covers
$$
 \begin{split}
 \|D f_*[\dot\gamma,\dot f_B]\|_{H^{1/2}}
 +\|D x[\dot\gamma,\dot f_B]\|_{\mathfrak M_{-3/2}}
 \le C_{\rm weak}\big(
          \|\dot\gamma\|_{H^{-3/2}}
                           +\|\dot f_B\|_{H^{1/2}}\big).
 \end{split}
 \tag{M.27}
$$
The same bound covers each normalized readout of the complete long kappa and mean-height span, and the algebraic quantities in (M.11) after their actual scales are restored. For p-hat p the output is H^-1/2; for A and the physical ratios it is M_-3/2; for m and bar u it is the full radial scalar norm.

To see the size of (M.26), the largest normalization needed for these appended outputs is
64rho/r_B<2^48; the gamma counterparts are smaller.
The kernel factor, two weight ratios, both Schur sums and the fixed output count remain far below 2^144. Standard Hilbert pair norms are read only at this final stage; no square-root-of-two factor is inserted into the contraction (M.4).

In particular all fixed inner traces B(L), C_0(L), B_0(L), the full nonmean B/C rows and their Hilbert adjoints have these genuine derivative extensions. The exact row
D C_ne(L)[dot gamma,dot f_B]=dot gamma is retained. The adjoint is that of this full operator; it is not a transpose of a finite 97-input sample.

For physical height variables y_B=s_B f_B and y_R=s_R f_*, the f_B-to-f_* column has the factor s_R/s_B, and the gamma-to-f_* column has s_R. These scales cannot be set to one when attaching the graph to another physical segment.

## 8. Both means, coordinate phase and geometric matching

For an actual direction, the algebraic output differentials are exactly
$$
 \dot j=(\dot C-j\dot c_0)/c_0,\quad
 \dot p=I_\theta\dot j,\quad
 \dot m=-\dot c_0/c_0^2,\quad
 \dot{\bar u}=\dot B_0/c_0-B_0\dot c_0/c_0^2 .
 \tag{M.28}
$$
The primitive input has zero actual mean. Neither dot c_0 nor dot B_0 is discarded. The true B-mean endpoint and its radial conservation law are (M.5); the C mean obeys its original equation with the full Q mean and true outer mean output.

Long mean height is
v_0(t)=lambda+integral_0^t a(s)w(s)kappa(s) ds.
There is one independent lambda. Its derivative is an extra scalar datum, not part of a nonmean Fourier input. The physical mean slopes are w kappa. The height span uses a_Rw_R and is not assigned an epsilon_L screening factor.

The coordinate primitive p in (M.9) fixes the original moving-coordinate phase on real data. The Euclidean coframe angle and position follow the original complete ordered reconstruction and its radial angular-mean connection. They are not reset at each radius. This theorem supplies the full physical curvature and true long mean outputs needed by that reconstruction; it does not invent a new numerical bound for an unlisted position/frame lift.

At positive regularity, the Codazzi equations recover the permitted radial derivatives on every actual smooth target piece. The artificial candidate residual cancels against the correction equation. Original target/graft regularity and all actual matching charges remain as given. Weak derivatives in (M.27) are extensions of these actual derivatives at a finite-jet background, not nonlinear value solutions for arbitrary H^-3/2 gamma.

The cap intrinsic nu column vanishes only because its true compact support is absent here. The independent nu effects through gamma, f_B and the full exterior charges remain. Whole negative-body return, the waist, nonlinear tail residual, the complete source Schur and the final geometric conditions are separate interfaces.

This extension removes the requirement that the unknown inner curvature input itself be analytic. It gives a single true two-input zero-width graph, complete mixed Taylor kernels, finite-Sobolev one-high estimates and actual weak inner curvature columns, while retaining both means and all stated physical units.
