# R133 supplement: true full-delta outer rows in the fixed-base cap inverse

2026-11-15, visible-exact-astra-0df9.

**Proved from the existing complete outer certificates.**
For the same explicit family Qdelta=Q0+delta Z, real |delta|<=1e-8,
the genuinely changed nonlinear exterior derivative contributes a
bounded fixed-base cap feedback of norm less than 1/8. This includes
its independent moving mean row. It does not compare a changing
composition operator with the identity.

The inner cap port stays the original nonmean C port at r=9/10 in
the fixed reference differential DPsi0. The true outer rows are the
ones at Qdelta(R), R=25/8. Thus this note pays the changed-outer part
left explicit in P.19 of the
[fixed-base conservative-source theorem](R133-supplement-fixed-base-conservative-source-transport-and-nearby-cap-linearization.md).
Its body coefficient criterion still has to be instantiated on the
actual cap.

The centre and direction definitions remain
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
and 6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
The original physical eta0 is fixed. The compact nu bump is zero on
this entire cap.

## 1. Previously executed complete inputs

The [full-real-delta theorem](R133-supplement-actual-full-real-delta-outer-and-positive-high.md)
comes from public run 43615531666/1. Its complete outer child passed
25 gates and retains the actual nonlinear long solution, its
holonomy small root, all frequencies, both independent affine mean
and height sources and the same physical angle normalization.

The exact small summary is
notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/evidence/full-delta-complete-regular-Hs-outer-summary.json,
23649 bytes, SHA256
769204e822787216c5aebd2cde30e73759fcf66d3bb1d6d1d76d2381bad6cae6.
Its native SHA256 is
5ab1d1b85cb71556b051fd53f5579cb30260ebdda6a844df9a4b377508e057fc.

The complete boundary formulas and their norms are S.20--S.38 of
[the true regular Hs graph](R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md).
The actual full-delta consumer transfers those same ordered formulas;
it does not reconstruct a nonlinear graph by finite Fourier fitting.
The independent background height retains the stated analytic
restriction ||fB||_{dot A_sigma^2}<=2^-60, sigma>=1/16.

The [continuous cap](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md)
and [complete gauge](R133-supplement-complete-normalized-angle-gauge-and-residual-Hessian.md)
supply the fixed reference inverse and its exact residual correction.
The [reflection theorem](R133-supplement-exact-reflection-sector-and-original-moving-cap-tail-bridge.md)
identifies it with the original moving equation in the actual
odd/even sector. The actual B curvature mean is zero in this sector;
the C mean is not discarded.

## 2. Put both true boundary operators in one original moving coordinate

Let Jphi be the original Hilbert multiplier i sgn(k) on nonzero
k in 4Z, so Jphi^2=-I there. For a full moving variation h at R put
$$
 y=P_{\ne0,\phi}h_2,\qquad z=\langle h_2\rangle_\phi .
$$
Here h1 is odd and h2 is even. The exact complete moving chart is onto
in y. The actual homogeneous outer equations are
$$
 P_{\ne0,\phi}(-J_\phi h_1-p_\delta h_2)=\mathcal E_\delta y,
 \qquad z=\mathcal M_\delta y,\qquad
 p_\delta={q_*\over -m_\delta(R)} .
 \tag{O.1}
$$
The full nonzero-mode row E_delta and independent mean functional
M_delta are the true transformed nonlinear exterior derivatives.
They include the nonlocal primitive and the changed physical angle.
Their definition is not the Hilbert principal part alone.

The actual uniform complete estimates imply
$$
 \|\mathcal E_\delta\|_{L^2\to L^2}<{53\over10^6},\qquad
 \|\mathcal M_\delta\|_{L^2\to\mathbb C}
                          <{1084\over10^9}.               \tag{O.2}
$$
Here the first bound is justified at order zero by the same positive
majorant as S.30--S.32. Specifically, the coefficient multiplication,
angle map, chart inverse and full DN bounds hold for every 0<=s<=1.
Replacing the DN norm T_s by the already paid H1 majorant in those
formulas only enlarges their order-zero right sides. The actual
full-delta complete_Robin_H1 is less than 5.269195e-5, below 53e-6.
This argument uses the formula's order-zero realization, not an
invalid inference that an H1 operator norm automatically bounds its
L2 realization. The full_mean_rank is less than 1.083805e-6,
below 1084e-9. Delta=0 is included in the same estimates.

All changes of the rotational principal scalar are retained. Since
the physical curvature mean is exactly 1/m_delta,
$$
 p_\delta-p_0=-q_*
       \left(\langle C_\delta\rangle_\theta
                           -\langle C_0\rangle_\theta\right).
 \tag{O.3}
$$
The two means in this formula are taken in their own actual physical
angles. Their exact scalar values make the comparison unambiguous.
The executed full-delta bound and 0<q*<=1 give
$$
 |p_\delta-p_0|<3.890229\,10^{-28}.
 \tag{O.4}
$$
The original strictly positive regular multiplier comparison fee is
still part of E_delta; it has not been set to zero.

Define the two-row moving boundary operator
$$
 \mathfrak b_\delta h=
 \begin{pmatrix}
 P_{\ne0}(-J_\phi h_1-p_\delta h_2)-\mathcal E_\delta y\\
 z-\mathcal M_\delta y
 \end{pmatrix}.
$$
Then, exactly,
$$
 \mathfrak b_0h=\mathfrak b_\delta h+\mathcal D_\delta y,
 \quad
 \mathcal D_\delta y=
 \begin{pmatrix}
 (p_\delta-p_0)y+(\mathcal E_\delta-\mathcal E_0)y\\
 (\mathcal M_\delta-\mathcal M_0)y
 \end{pmatrix}.
 \tag{O.5}
$$
Use the output norm ||r||_2+|s|. The triangle inequality on two
complete operators, together with (O.2)--(O.4), gives
$$
 \boxed{\quad
 \|\mathcal D_\delta\|
   <2{53\over10^6}+2{1084\over10^9}
                    +3.890229\,10^{-28}
   <{11\over100000}.
 \quad}                                                   \tag{O.6}
$$
This is a difference bound relative to the common principal row.
It neither subtracts two scalar upper bounds nor declares two
different nonlinear derivatives equal.

## 3. An exact right inverse for the reference raw boundary rows

For arbitrary even nonmean r and scalar s set
$$
                  \mathcal S(r,s)=(J_\phi r,s).
 \tag{O.7}
$$
Its second entry is the constant function s. Therefore y=0, and
Jphi^2=-I gives
$$
                    \mathfrak b_0\mathcal S(r,s)=(r,s).
 \tag{O.8}
$$
In particular its norm is one for the pair sum. It retains the
independent true mean; that row is not solved by assigning a
nonmean primitive.

Let bphys0 be the complete reference physical outer operator,
$$
 \mathfrak b_{\rm phys,0}x=
 \begin{pmatrix}
 J_\theta x_B+Q_{\rm true}P_{\ne0}x_C
                                  -D_Zd_0P_{\ne0}x_C\\
 \langle x_C\rangle_\theta-D_Zc_{0,0}P_{\ne0}x_C
 \end{pmatrix}.
 \tag{O.9}
$$
The exact original graph and its onto moving parameterization prove
$$
 \ker\mathfrak b_0
       =\ker(\mathfrak b_{\rm phys,0}D\Psi_0).
$$
Thus the full affine coordinate conversion is
$$
 \mathfrak b_{\rm phys,0}D\Psi_0h
       =\mathcal T_0\mathfrak b_0h,\qquad
 \mathcal T_0=\mathfrak b_{\rm phys,0}D\Psi_0\mathcal S .
 \tag{O.10}
$$
Indeed h-S b0h lies in the displayed kernel. Also T0 is injective:
T0(r,s)=0 implies S(r,s) lies in ker b0, and (O.8) gives (r,s)=0.
Consequently solving the physical rows with data T0(r,s) imposes
exactly the desired raw rows (r,s), not just necessary conditions.

## 4. Pay the complete reference lift of these raw rows

At the fixed reference endpoint, the uniform multiplier proof of
C.18 gives the pointwise angular estimate
$$
 \|D\Psi_0 f\|_{L^2_\theta,\mathrm{pair}}
       <.324309160\,\|f\|_{L^2_\phi,\mathrm{pair}}
       <\tfrac13\|f\|_{L^2_\phi,\mathrm{pair}} .
 \tag{O.11}
$$
This is the same pointwise coefficient estimate used before radial
integration in C.18. It is not an endpoint trace deduced from a
radial L2 norm.

The true reference outer multiplier satisfies
||Qtrue||<=q*+positive_fee<1+2^-500, and the complete DN norm is
less than 5.898255e-6. The independent mean functional is less than
7.372818e-7. Thus both rows of bphys0, separately, have pair norm
less than 33/32. The positive fee stays in this inequality.

The original physical cap gains for its independent Robin and C0
sources are less than 54 and 6. The product of its additional long
B0 closure and complete residual-Hessian resolvent factors is less
than 33/32: use
(1-2^-46)^-1(1-1/64)^-1<33/32.
Let Gboundary0 denote the full original moving cap solution with
zero body source, zero prescribed inner nonmean C and raw outer
data (r,s). Equations (O.7)--(O.11) give
$$
 \|G_{\rm boundary,0}(r,s)\|_{\mathfrak M}
       <20(33/32)^2(\|r\|_2+|s|)
       <24(\|r\|_2+|s|).
 \tag{O.12}
$$
Every quantity on the left is expressed in the fixed physical
variable x=D Psi0 h. The independent outer source rows are added
with their original signs before taking the displayed positive
upper bound.

The reference inverse differential C.17 further gives
$$
 \|y(R)\|_{L^2_\phi}
 \le\|h(R)\|_{L^2_\phi,\mathrm{pair}}
       <40.814490\,\|x\|_{\mathfrak M}
       <41\|x\|_{\mathfrak M}.
 \tag{O.13}
$$
The module retains actual endpoint evaluations. Once more this is
not an L2_r-to-trace inference.

## 5. The actual changed-outer feedback and its combination with the body

From (O.5), the exact operator that changes the true outer rows
while retaining the reference body is
$$
 \mathcal K_{{\rm out},\delta}x
      =G_{\rm boundary,0}\mathcal D_\delta
                              P_{\ne0}h_2(R),\qquad
                         \widehat h=\mathcal Hx .
$$
Its complete module norm satisfies
$$
 \boxed{\quad
 \|\mathcal K_{{\rm out},\delta}\|
 <{24\cdot41\cdot11\over100000}
 ={10824\over100000}<\frac18 .
 \quad}                                                   \tag{O.14}
$$
For example 8 times 10824 is 86592, strictly less than 100000.
All constants are positive enlargements of already executed bounds;
no new array, target, nonlinear long solve or numerical experiment
was evaluated for this deduction.

The reference body with the genuinely changed outer graph has
inverse factor less than 8/7. More generally, whenever the actual
cap field Y satisfies the joint coefficient criterion P.19,
the exact simultaneous equation is
$$
 x=x_{\rm data}+\mathcal K_Yx+\mathcal K_{{\rm out},\delta}x .
$$
The two fees add to less than 1/4+1/8=3/8, so
$$
 \|(I-\mathcal K_Y-\mathcal K_{{\rm out},\delta})^{-1}\|
                                                   <8/5 .
 \tag{O.15}
$$
This is an all-frequency cap statement in the specified physical
module. The original inner nonmean C row is fixed as stated at the
start. Its genuine mean is an output, not an additional fifth
boundary condition.

For an affine new boundary condition bdelta h=adata, the data term
uses Gboundary0 adata. The independent height, Robin residual and
mean charge in S.36--S.38 are still part of that complete adata;
their exact new chart conversion is retained. This does not set an
outer height or a physical mean source to zero.

## 6. Exact scope of the completed step

O.14 pays the actual changed exterior derivative on the whole
stated real explicit family. It uses both complete nonlinear
boundary operators relative to their common true principal row;
it does not require differentiating the boundary with respect to
delta or claiming smallness of a bare angle composition difference.

The numerical instance of the body criterion P.19 still requires
joint per-mode cap bounds for delta Z in the fixed physical angle.
A rowwise Wiener envelope is not that bound. An arbitrary further
nonlinear state correction also requires its own actual endpoint
graph and coefficient-domain verification. The full negative body,
parameter Schur, nonlinear global matching and the README
geometric completion are not supplied by this cap result.
