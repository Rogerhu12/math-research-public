# R133 supplement: actual cap inner Poisson perturbation and the complete 97-row matching interface

2026-11-15, visible-exact / newton_source.

**Analytic consequence of the completed cap bounds.** The actual nonlinear cap has an inner nonmean C-to-(B,C-mean) derivative on all physical Fourier modes. Its complete Poisson operator differs from the old residual-corrected moving reference, expressed in the same fixed physical coordinates, by less than 1/5 in the complete Hilbert module below. The proof keeps the right nonmean trace as a second variable, the two Q source terms, the old residual Hessian, and the actual exterior mean row.

This supplies an explicit perturbation and affine matching load for the original 97-row boundary. It does not prove that the finite boundary Schur, the unknown high return, or the global parameter Schur is invertible. No old matrix, target, residual, source integral or reference kernel is recomputed.

## 1. One centre, one physical circle, and the two inputs

Keep the original ac1 candidate and its continuous repair
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47,
the same intrinsic eta0 and delta=0, and I=[L,R]=[9/10,25/8]. Use:

- [P: full-frequency moving cap interface](R133-supplement-full-frequency-moving-cap-boundary-and-Poisson-interface.md).
- [A: exact physical Q remainder](R133-supplement-physical-cap-L1-Wiener-sources-and-practical-nonlinear-body-ball.md).
- [E: weighted-Q invariant cap ball](R133-supplement-weighted-Q-endpoint-invariance-and-small-analytic-cap-ball.md).
- [X: actual cap existence](R133-supplement-actual-all-mode-positive-cap-existence-at-repaired-M32-centre.md).
- [M: the two-input zero-width map](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md).
- [S: true exterior with the complete square-zero Hilbert module](R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md).

Write the fixed physical centre and the exact cap as
$$
 \widehat W=(\widehat B,\widehat C),\qquad
 W_*=\widehat W+x_*,\qquad
 \|x_*\|_{X_0}\le\rho=3\,10^{-6}.
 \tag{I.1}
$$
Here X0 is the complete joint Wiener pair sum. The nonmean right input obeys
$$
 \|P_\perp(x_*)_C(R)\|_{A^0}\le\zeta=9.9\,10^{-10},\qquad
 \|Z_0\|_{A^0}<3\,10^{-13}.
 \tag{I.2}
$$
Thus the actual long input remains inside the already checked Z-radius
10^-9. The two independent data are
$$
 P_\perp(W_*-\widehat W)_C(L)=\gamma,\qquad
 \| \gamma\|_{A^0}\le10^{-9},\qquad
 \|f_B\|_{\dot A^2}\le2^{-60}.
 \tag{I.3}
$$
The full two-input map is defined in M. For comparison with the original
193-state / 97-row system, restrict here to its original reflection
sector: B odd, C even, and gamma,fB even. This preserves every even mean
and all positive and negative Fourier frequencies. The full-periodic
extension in M is not compressed to 193 states by this restriction.

For the comparison with the already cached K0 and its 97 rows, fix fB
to the identical prescribed value used by that reference. The all-mode
bounds (I.15)--(I.16) are uniform on the stated height ball. A changed
height is a separate column below; it does not silently identify a
new height-dependent reference with the old cached K0.

## 2. Hilbert source units and the already paid constants

For a physical scalar field let
$$
 \|u\|_{\mathfrak M}
   =\left(\sum_{k\in4\mathbb Z}\sup_{r\in I}|u_k(r)|^2\right)^{1/2},
 \qquad
 \|(b,c)\|_{\mathfrak M_\Sigma}=\|b\|_{\mathfrak M}+\|c\|_{\mathfrak M}.
 \tag{I.4}
$$
Every mean has weight one. Evaluation at either endpoint is bounded by
this norm. A joint Wiener coefficient acts on it by complete convolution.

The unclosed rotational Green from E and the original all-mode physical
cap proof has
$$
 K_Q<16,\qquad H_D<10,\qquad H_C<3,\qquad T_*<.824,\qquad a_L<4\,10^{-9}.
 \tag{I.5}
$$
KQ is the complete Q-source column, not a single ordinary or divergence
column. In the physical equations its input q contributes
$$
                    {\cal V}q=(\gamma_{\mathrm{rad}}\partial_\theta q,\ \beta q).
 \tag{I.6}
$$
The radial coefficient gamma_rad is not the inner input gamma or an r derivative. Formula
(I.6) keeps both equations and the ordinary C mean; replacing it by
one derivative source would be incorrect.

The old complete physical inverse G, including its original true
exterior derivative, has resolvent factor less than 5.571744. Therefore
$$
 \|G{\cal V}\|<90,\qquad
 \|G[e_D]\|<54\|e_D\|_2,\qquad
 \|G[e_0]\|<6|e_0|.
 \tag{I.7}
$$
The first inequality is the same complete KQ column multiplied once by
the old physical resolvent: 16 times 5.571744 is less than 90. The
second and third are the original 53.846164 and 5.571744 gains. They are
not new source estimates.

The repaired original coefficients satisfy
$$
 \max(\|Q_B\|_{\mathfrak A_0},\|Q_C\|_{\mathfrak A_0})
       <.051432066,\qquad q_w<10^{-5},\qquad K_e<5 .
 \tag{I.8}
$$
The weighted gate is the completed public run 43695160055/1. It is a
joint coefficient bound, not a maximum of rowwise sums.

## 3. Actual exterior columns on the larger legitimate ball

The completed scalar consumer 43692857656/1, summary
c589a4549b56afe88e4c479e7a56819de65da072, checks the original S.10--S.13
formula at z=10^-9 and b=2^-60. Its exact source is
fourfold_codazzi_cached_cap_L1_endpoint_sources.py,
SHA256 106ec9308882b814ca773da904e561e93aa4475f4f46f84b9632c9716653992f.

S.10--S.11 are estimates in the complete square-zero L2 module.
Their zero-width use is the same complete fixed-point/module
argument retained in M. It does not convert a Wiener operator norm
into an L2 norm by name. They give, throughout the actual ball,
$$
 \|D_Zd_*\|<.006,\quad \|D_Zc_{0,*}\|<.00075,\quad
 \|D_{f_B}d_*|D|^{-2}\|<.000657,\quad
 \|D_{f_B}c_{0,*}|D|^{-2}\|<.000083 .
 \tag{I.9}
$$
The summary's bounds are respectively .0059069501581,
.0007383687698, .0006563277954 and .00008204097442, each below the
displayed rational enclosure. The same complete regular multiplier
comparison remains included. B mean is exactly zero in the stated
reflection sector; C mean is the actual exterior output in (I.9).

At the old centre the original full physical proof gives
$$
 \|D_Zd_0\|<.000006,\qquad \|D_Zc_{0,0}\|<.000001 .
 \tag{I.10}
$$
Both are conservative enlargements of the complete original bounds,
including the retained positive regular comparison fee. Thus, on the
same physical circle and at the same fB,
$$
 \|\Delta T\|:=\|D_Zd_*-D_Zd_0\|<.006006,\qquad
 \|\Delta C_0\|:=\|D_Zc_{0,*}-D_Zc_{0,0}\|<.000751 .
 \tag{I.11}
$$
This is a legitimate triangle bound between two complete operators.
No entrywise subtraction of unrelated enclosures and no small
composition-minus-identity assertion is used.

## 4. Linearization at the actual nonlinear cap

A.17--A.19 and E.15 give the exact Gauss remainder and its derivative:
$$
 {\cal R}_Q(b,c)=
 \frac{b^2-2\widehat u\,bc+
            (K\widehat v^2+\widehat u^2)c^2}{\widehat C+c},
 \qquad
 \|D{\cal R}_Q(x_*)\|_{\mathfrak M_\Sigma\to\mathfrak M}
                           \le26\rho .
 \tag{I.12}
$$
The second statement follows either by the explicit two multiplication
coefficients or by the same full Banach-algebra Lipschitz estimate.
It includes both means and the variable denominator. Denote this
multiplication row by TQ.

For an inner direction g in the full physical even, nonmean L2 space,
let x be the actual Jacobi response at W*, with fB fixed. Set
$$
 X=\|x\|_{\mathfrak M_\Sigma},\qquad
 Z=\|P_\perp x_C(R)\|_2,\qquad G_{\rm in}=\|g\|_2 .
 \tag{I.13}
$$
The same signed modal kernels and then their complete positive
majorants yield
$$
 \begin{aligned}
 X&\le3G_{\rm in}+.825X+.061Z,\\
 Z&\le4\,10^{-9}G_{\rm in}+.00049X+.005Z .
 \end{aligned}
 \tag{I.14}
$$
Here the X coefficient uses
16(.051432066)+16(26rho)<.825. The Z-to-X coefficient is
10(.006)+.00075<.061. For the second line, the original weighted
linear term contributes at most 10^-4 X, and the complete new
remainder derivative contributes 5(26rho)X=.00039X.
The true outer d response contributes T_* .006 Z<.005Z.
Its C mean is already retained in the first line; it is not an
additional nonmean R input. The left port contributes the actual
aL, not a unit endpoint Poisson constant.

The positive matrix in (I.14), applied to (18,.009), is strictly
below that vector after adding (3,4 times 10^-9). Equivalently one
may eliminate Z with its .995 denominator and then solve the first
line. Thus the complete actual inner Poisson operator satisfies
$$
 {\cal K}_*:g\longmapsto x,\qquad
 \|{\cal K}_*g\|_{\mathfrak M_\Sigma}<18\|g\|_2,\qquad
 \|P_\perp({\cal K}_*g)_C(R)\|_2<.009\|g\|_2 .
 \tag{I.15}
$$
The positive matrix is a strict contraction in the associated
weighted two-coordinate norm. This proves the Hilbert-module
linear BVP, first for finite data and then by the bounded complete
kernels. On the common smooth data it is exactly the derivative of
the nonlinear cap map by uniqueness. There is no physical Fourier
cutoff on g.

## 5. The independent far-height column

Put g=0 and let h be a direction of the normalized fB. In (I.14)
the additional first source is at most .006653 times
F=||h||_(dot H2); the second is at most .824(.000657)F.
Using the same two-coordinate comparison gives
$$
 {\cal L}_*h=D_{f_B}x_*[h],\qquad
 \|{\cal L}_*h\|_{\mathfrak M_\Sigma}<\frac1{25}\|h\|_{\dot H^2},
 \qquad
 \|P_\perp({\cal L}_*h)_C(R)\|_2<.0006\|h\|_{\dot H^2}.
 \tag{I.16}
$$
Indeed .825(.04)+.061(.0006)+.006653<.04, and
.00049(.04)+.005(.0006)+.824(.000657)<.0006.

These are normalized height units. For physical height yB=sB fB,
the direction is
$$
                 \dot f_B=(\dot y_B-f_B\dot s_B)/s_B .
 \tag{I.17}
$$
Only when sB is fixed does the source coefficient become simply
1/sB. M supplies the separate H^(1/2)-to-H^(-3/2) weak window and
finite tame windows; (I.16) is not that weak-window statement.

## 6. The old Hessian bridge is part of the comparison

Let D0 be the complete physical Jacobi operator at the repaired
centre, with the original physical exterior derivative. Let
R0 be its moving nonlinear residual and define the complete
residual-sensitive body operator
$$
 {\cal H}_0x=D^2\Psi_0[R_0,D\Psi_0^{-1}x],\qquad
 \|G{\cal H}_0\|<\chi_H=.003840162 .
 \tag{I.18}
$$
P.10--P.13 define
$$
 \widetilde G=(I-G{\cal H}_0)^{-1}G,\qquad
 {\cal K}_0=\widetilde G[\hbox{inner }C_{\ne0}=g].
 \tag{I.19}
$$
In particular K0 is the inverse of D0-H0 in physical coordinates,
with the stated fixed boundary rows. It is not just G.

At the exact nonlinear cap the physical body Jacobi is
D0-V TQ. Consequently, writing the actual response in the old
reference equation gives the exact ordered identity
$$
 {\cal K}_*g={\cal K}_0g+
 \widetilde G\big[
      {\cal V}T_Q{\cal K}_*g-{\cal H}_0{\cal K}_*g;\
      e_D=\Delta T\,P_\perp({\cal K}_*g)_C(R),\
      e_0=\Delta C_0\,P_\perp({\cal K}_*g)_C(R)\big].
 \tag{I.20}
$$
The semicolon separates body source and actual outer loads.
The signs correspond to the physical boundary convention
Jb+Qtrue c_ne=D_Zd c_ne+eD and c0=D_Zc0 c_ne+e0.
All other independent loads are zero for this particular column.

Although the actual background solves its nonlinear equations,
H0 in (I.20) is the old nonzero reference residual term. Setting
it to zero because the new background is a solution would change
the reference operator.

## 7. A complete all-mode perturbation smaller than 1/5

Use (I.7), (I.11), (I.12), and both bounds in (I.15) in (I.20).
Then
$$
 \|{\cal K}_*-{\cal K}_0\|_{L^2_{\mathrm e,\perp}
                               \to\mathfrak M_\Sigma}
 <\frac{(90\cdot26\rho+\chi_H)18+
          [54(.006006)+6(.000751)](.009)}
                {1-\chi_H}
 <\frac15 .
 \tag{I.21}
$$
Every number in the last comparison is rational, and every
underlying source constant is an already completed bound.
The complete ordinary C-mean source in V and the independent
outer C-mean load are different terms and both remain present.

The true inner trace operators are
$$
 K_{B,*}g=({\cal K}_*g)_B(L),\qquad
 K_{0,*}g=\Pi_0({\cal K}_*g)_C(L),
 \tag{I.22}
$$
with analogous old operators. Endpoint evaluation and the pair
sum give, without another factor,
$$
 \|(K_{B,*}-K_{B,0})g\|_2+
       |(K_{0,*}-K_{0,0})g|<\frac15\|g\|_2 .
 \tag{I.23}
$$
An L2 body estimate alone would not give an endpoint trace.
Here the stronger module and the separately controlled R trace
have been retained throughout.

## 8. Exact physical matching and its affine load

The actual nonlinear cap is a graph over its physical inner
nonmean C datum and fB. At a chosen base pair (gamma,fB), all
linearized matching conditions are
$$
 \begin{aligned}
 b_{\rm left}&=K_{B,*}\,P_\perp c_{\rm left}+g_B,\\
 \Pi_0c_{\rm left}&=K_{0,*}\,P_\perp c_{\rm left}+g_0 .
 \end{aligned}
 \tag{I.24}
$$
For the far-height direction,
(gB,g0)=((L_*h)_B(L),Pi0(L_*h)_C(L)); other physical source,
mean, jump, metric and parameter columns must be added in their
original units. Inner Cmean is an output in (I.24), not an extra
independent Dirichlet input.

At gamma=0 the old moving centre has the correct prescribed
nonmean C(L), but generally not the actual cap's B(L) or Cmean(L).
Its exact affine physical mismatch is
$$
 r_B=\widehat B(L)-B_*(L)=-(x_*)_B(L),\qquad
 r_0=\widehat C_0(L)-C_{*,0}(L)=-\Pi_0(x_*)_C(L).
 \tag{I.25}
$$
The pair norm is at most rho. These are actual matching loads,
not zero because the cap itself is exact. A rigid height constant
does not alter either curvature mismatch.

## 9. Fixed-reference moving coordinates and the complete mean

At L use exactly the old P.1--P.9 maps S0, HB0, HC0 and m0.
For a physical direction written as D Psi0(h1,h2), the equations
(I.24) become
$$
 \begin{aligned}
 h_1+E_*^0h_2&=S_0g_B,\\
 M_*^0h_2&=g_0,
 \end{aligned}
 \qquad
 \begin{aligned}
 E_*^0&=S_0(H_{B,0}-K_{B,*}P_\perp H_{C,0}),\\
 M_*^0&=-m_0^{-2}\Pi_0-K_{0,*}P_\perp H_{C,0}.
 \end{aligned}
 \tag{I.26}
$$
The input of the Poisson map is Pperp HC0 h2, not Pperp h2.
In particular a moving constant h2 can produce physical nonmean
input. Its physical mean is nevertheless exactly
Pi0 HC0 h2=-Pi0 h2/m0^2. The whole even isomorphism HC0, including
its constant input, is necessary for the sufficiency argument.

Let E0,M0 be the original P.14 rows. Their exact differences are
$$
 \Delta E^0=-S_0(K_{B,*}-K_{B,0})P_\perp H_{C,0},\qquad
 \Delta M^0=-(K_{0,*}-K_{0,0})P_\perp H_{C,0}.
 \tag{I.27}
$$
Thus, if s*=||S0|| and c*=||HC0|| are the same paid full-function
bounds,
$$
 \|\Delta E^0u\|_2+|\Delta M^0u|
       <\frac{\max(s_*,1)c_*}{5}\|u\|_2 .
 \tag{I.28}
$$
One may retain the exact HC0 input Gram instead of c* where a
future directed matrix consumer has actually certified it.
There is no new numerical covariance in this theorem.

## 10. How the old 97 rows consume this result

In the original reflection basis let PL,e select even labels
0,...,96, and PL,o select odd labels1,...,96. The complete
low boundary has 96 odd rows plus the independent Cmean row.
For u in the 97-dimensional even input, it is
$$
 {\cal B}_{*,L}^0(h_1,u)
  =\big(P_{L,o}(h_1+E_*^0u),\ M_*^0u\big).
 \tag{I.29}
$$
All bases use the original orthonormal sine/cosine convention:
the even zero mode has weight one, and neither its input nor
its output is divided by sqrt2 a second time.

HC0 and the true Poisson map can create infinitely many physical
modes even from those 97 moving inputs. Equations (I.21)--(I.29)
hold for that complete image; they do not replace it by 97
physical modes. The operator P_L,o remains after S0 and is not
commuted through that nonconstant multiplier.

For an unknown high even input uH, the additional low load is
(P_L,o E_*^0 uH,M_*^0uH). The high odd equations also retain
P_H,o E_*^0 PL,e u and P_H,o E_*^0 uH. The cap has no finite
bandwidth that permits deletion of these blocks.

Write epsilon= max(s*,1)c*/5. The complete perturbation of the
97-output map, with the stated common input norm, has norm at
most epsilon. Hence its output covariance is bounded by
epsilon^2 I97. If an old error covariance Wold already bounds
the same full input/output operator, then any t>0 gives the
legitimate upper bound on the new actual error covariance
$$
 A_{\rm err,new}A_{\rm err,new}^*
 \preceq W_{\rm new}:=(1+t)W_{\rm old}
                      +(1+t^{-1})\epsilon^2 I_{97}.
 \tag{I.30}
$$
This is a whole signed-matrix Young estimate; it is not an
entrywise minimum or a transpose transfer from a finite
forward matrix.

If the actual 97 right-Poisson Gram HY satisfies
G_R^*G_R<=HY on exactly these rows, the extra composed
perturbation is at most epsilon sqrt(tr HY). A sharper signed
bound may be substituted only after its actual covariance has
been paid. No present theorem says that this number is less
than1. The ongoing finite matrix Green calculation is not
replaced by this symbolic expression.

## 11. What is fixed, what changes, and the remaining Schur

Equations (I.26)--(I.29) are in fixed D Psi0 coordinates. They
are, when gamma=0, directly the linearization at the old moving
trace Q0 of the nonlinear physical matching map
Psi(Qleft(L)) versus the actual cap graph, with S0 used as a
fixed row normalization. The nonzero value is (I.25).
Thus no derivative of a changing row normalization is silently
discarded.

At a different moving body background Qleft, the exact incoming
physical variation is D Psi_(Qleft) h. One must either retain
that map in (I.24), or apply
(D Psi0)^(-1)D Psi_(Qleft) before (I.26). Nothing here makes a
nontrivial angle-composition operator close to identity in
L2. The complete phase and two-mean formulas of M, or the
separately paid good-direction chart, are the relevant input;
a raw composition-minus-identity estimate is not available
for free.

Changing the lower-body generator or its background is also
independent of the cap perturbation. The complete finite
Schur must consume those body changes, the actual cap affine
load, the height column, and all mean/jump rows together.
For the infinite problem it must additionally retain the
unknown high trace, the true negative high inverse and all
low-high feedback blocks. The positive given-head graph
alone does not provide that missing negative return.

There is one physical height constant lambda. It remains in
the frame/position/height matching and cannot remove the
Cmean equation in (I.24). The cap's direct nu-bump vanishes,
but nu can change gamma, fB, the lower-body response, physical
installation factors and independent mean charges. These
columns remain in the global parameter Schur.

The new result is the actual all-mode physical inner
Poisson column, its quantitative comparison to the old
residual-corrected reference, and the exact 97/mean matching
interface with its remaining obligations.
