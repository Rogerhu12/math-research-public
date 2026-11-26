# R144 supplement: real H2 exterior DN and the actual positive H1 high inverse

Date: 2026-11-27.
Session: visible-exact-astra-fb31ed6-20261127 / geometric_closure.

This proves the next angular source/state window at every full-tail
background in [QN](R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md):

$$
 L^2_rH^{4/3}_\phi\longrightarrow L^2_rH^1_\phi
 \tag{QH.1}
$$

for the entire positive high block, with its complete finite head
supplied, the true physical exterior graph, both ends, and every original
affine jump. The exterior graph used here is the derivative of the
actual nonlinear DN map. Its two scalar mean columns and its independent
height column remain. The whole body/exterior feedback is below .803;
the collar/body loop is below .016371.

The new boundary step is an actual $H^{\pm2}$ realization of all four
exterior DN rows, obtained with only a real $A^3$ perturbation of the
endpoint. A fourth derivative is used only on the already known analytic
centre. The unknown background is not assumed to have any positive
spatial analytic width. This gives a genuine first increment beyond
QN's order0 and order $-1$ inverses. It does not yet give all angular
orders, the inverse of the coupled finite block, or the complete nonlinear
iteration.

## QH1. Background, exact object and already completed inputs

Use exactly QN.2--QN.4. Thus $Q=Q_*+q$ on the whole positive interval,
with the original reflection parity and

$$
 \sup_r(\|q_1(r)\|_{A^3}+\|q_2(r)\|_{A^3})\le10^{-6},
 \qquad
 \|q_1(R)\|_{A^3}+\|q_2(R)\|_{A^3}\le e:=10^{-9}.
 \tag{QH.2}
$$

The second hypothesis is an independent true endpoint condition. It
does not follow from a radial $L^2$ norm. The actual metric is unchanged
from QN, including every $|\delta|\le10^{-10}$ in the compact-centre
construction; the positive state $Q_*$ itself is independent of $\delta$.
The independent exterior height background obeys the original condition

$$
 \|f_B\|_{\dot A^2_\sigma}\le b:=2^{-60},\qquad \sigma\ge1/16.
 \tag{QH.3}
$$

A height direction is not bounded by (QH.3). It has its own source norm.
The unrelated overall height translation remains an independent scalar.

The actual compact endpoint is the original raw endpoint, exactly, by
[PH.2 and PH5](R144-supplement-actual-positive-high-graph-for-compact-centres.md).
Hence the completed
[original second-translation conclusion](R133-supplement-final-regular-negative-window-and-height-ports.md),
N.8, applies to its physical nonmean curvature $Z_*$:

$$
 \|(Z_*)_{\theta\theta}\|_{A^0}
 <1.856722151\,10^{-9}.
 \tag{QH.4}
$$

Only this already completed scalar conclusion is used; its old
64 choices of Fourier-tail split are not evaluated again. The saved
conclusion is
[2026-11-14-R133-final-regular-negative-window-rational.json](../notes/2026-11-14-R133-final-regular-negative-window-rational.json),
SHA256
2c2c9c9f1973207061a03f892256350670dc486b893906ce773a8b4e0616edb7.

The other numerical inputs are QN's complete body, collar, real
composition, Hilbert and zero-width module conclusions. The exact
rational reader below uses the same completed body and negative-window
small summaries as PH/QN. No original native coefficient enclosure,
Riccati trajectory, kernel sweep, or target is recomputed.

## QH2. Two physical translations require only three unknown derivatives

All functions in this section are at the real endpoint $R$. Write
$v=m+w$, $\theta_\phi=v/m$, and $\Phi=\theta^{-1}$, with the original
mean-zero primitive fixing the phase. The true physical curvature is
$C=(1/v)\circ\Phi$. Its exact third derivative is

$$
 C_{\theta\theta\theta}\circ\theta
 =B_3(v,m):=
 -{m^3v_{\phi\phi\phi}\over v^5}
 +{10m^3v_\phi v_{\phi\phi}\over v^6}
 -{15m^3v_\phi^3\over v^7}.
 \tag{QH.5}
$$

This follows by applying $(m/v)\partial_\phi$ three times to $1/v$.
The radial constant $m$ is retained and is allowed to change with $q$.

Let

$$
 \begin{gathered}
 P=1.480385\,10^{-11},\quad V_\sigma=9.603792\,10^{-9},\\
 m_0=5.84461145233,\quad m_l=m_0-e,\quad M=7+e,\quad t=1/5.84,\\
 a_1=8V_\sigma,\quad a_2=128V_\sigma,\quad
 a_3=3072V_\sigma,\quad a_4=98304V_\sigma,\qquad
 v_j=a_j+e\quad(1\le j\le3).
 \end{gathered}
 \tag{QH.6}
$$

The $a_j$ follow from the known strip $1/8$ by
$(8x)^j\le j!\,8^j e^x$ in the usual Fourier coefficient bound.
Equivalently $|k|^j\le j!\,8^j e^{|k|/8}$.
Thus they bound the known centre's first through fourth raw derivatives.
The unknown contributes at most $e$ to each of the first three
derivatives, because its norm in (QH.2) is $A^3$. The fourth unknown
derivative is neither used nor required.

Throughout the real segment from $Q_*$ to $Q$, QN proves
$|m|\le M$, $\|1/v\|_{A^0}<t$. Product differentiation in the
Wiener algebra gives

$$
 \begin{aligned}
 L_3={}&3M^2v_3t^5+M^3t^5+5M^3v_3t^6\\
 &+10[3M^2v_1v_2t^6+M^3(v_1+v_2)t^6
                       +6M^3v_1v_2t^7]\\
 &+15[3M^2v_1^3t^7+3M^3v_1^2t^7+7M^3v_1^3t^8],\\
 \|B_3(v,m)-B_3(v_*,m_*)\|_{A^0}&\le L_3 e .
 \end{aligned}
 \tag{QH.7}
$$

Here $\|\delta v^{(j)}\|_{A^0}\le e$ for $0\le j\le3$ and
$|\delta m|\le e$. In particular a small centre value has not been
used as a bound for its variation.

Let $j_l,j_u$ be QN's positive lower/upper bounds for $v/m$.
Since both phases have zero mean,

$$
 \|\theta-\theta_*\|_\infty
 \le {e(1+V_\sigma/m_0)\over4m_l},
 \qquad
 \|\Phi-\Phi_*\|_\infty
 \le {e(1+V_\sigma/m_0)\over4m_lj_l}.
 \tag{QH.8}
$$

The numerator follows by subtracting $w/m$ exactly; the constant part
of $\delta v$ is retained through $\delta m$. The factor $1/4$ is the
fourfold mean-zero primitive. The inverse inequality is the real
mean-value theorem for the two orientation-preserving lifted maps.

Only the known function $B_3(v_*,m_*)$ is differentiated to pay this
small shift. Its derivative has the valid bound

$$
 G_3=7^3\{a_4t^5+(15a_1a_3+10a_2^2)t^6
                     +105a_1^2a_2t^7+105a_1^4t^8\}.
 \tag{QH.9}
$$

Indeed differentiating (QH.5) gives the coefficients
$-1,15,10,-105,105$ in front of
$v^{(4)}/v^5,v'v'''/v^6,(v'')^2/v^6,(v')^2v''/v^7,(v')^4/v^8$.
Consequently, splitting the two compositions before estimating,

$$
 \begin{aligned}
 \|C_{\theta\theta\theta}-(C_*)_{\theta\theta\theta}\|_2
 &\le e\left[j_uL_3+
       {1+V_\sigma/m_0\over4m_lj_l}G_3\right]\\
 &<.051e.
 \end{aligned}
 \tag{QH.10}
$$

The first measure factor is at most $\sqrt{j_u}\le j_u$. The second
term is estimated pointwise from (QH.8), so it has no hidden
composition derivative of the unknown.

For a fourfold mean-zero function $f$,

$$
 \|f\|_{A^0}
 \le\left(\sum_{k\in4\mathbb Z\setminus\{0\}}k^{-2}\right)^{1/2}
          \|f_\theta\|_2
 ={\,\pi\over4\sqrt3}\|f_\theta\|_2
 <.46\|f_\theta\|_2 .
 \tag{QH.11}
$$

Apply this to $f=C_{\theta\theta}-(C_*)_{\theta\theta}$, whose physical
mean is zero. Combining (QH.4) and (QH.10) gives the complete physical
bound

$$
 \boxed{\ \|Z_{\theta\theta}\|_{A^0}<1.9\,10^{-9}.\ }
 \tag{QH.12}
$$

The rational expression using the saved whole bound is below
$1.879950733\,10^{-9}$. This proves regularity and a bound for the
actual $Z$ on the real circle, not an assumed analytic strip for $q$.

## QH3. The full nonlinear DN derivative on H2 and H7/6

The zero-width nonlinear value/module construction and its true
holonomy root are already proved in QN5. Keep its actual small
background ball $(z,b)=(4\,10^{-11},2^{-60})$, wider complex
function-parameter ball $(10^{-10},10^{-11})$, and legitimate radii

$$
 r_Z=5\,10^{-11},\qquad r_B=9\,10^{-12}.
 \tag{QH.13}
$$

The wider ball is a ball in the unweighted angular Wiener algebra,
complexified in its function parameters. It is not a spatial strip.
Its complete L2 module is the one used in QN.29; denote its four
operators by $T,C,U,V$, meaning respectively

$$
 D_Zd,\quad D_Zc_0,\quad
 D_{f_B}d\,|D_\theta|^{-2},\quad
 D_{f_B}c_0\,|D_\theta|^{-2}.
 \tag{QH.14}
$$

The scalar outputs are interpreted as constant functions with their
ordinary absolute value. In particular $C,V$ retain the derivative of
the actual holonomy root.

Set

$$
 \Xi_1={7\,10^{-11}\over r_Z}+{16b\over r_B},\qquad
 \Xi_2={1.9\,10^{-9}\over r_Z}+{512b\over r_B}.
 \tag{QH.15}
$$

The two translation derivatives of the independent height background
use only its original strip hypothesis (QH.3). Equation (QH.12) and
QN.25 provide the two real translations of $Z$.

For each one of the four complete operators $A$ in (QH.14),
translation covariance and function-parameter Cauchy give the
actual commutators

$$
 \begin{gathered}
 [\partial_\theta,A]=DA[Y'],\\
 [\partial_\theta,[\partial_\theta,A]]
       =D^2A[Y',Y']+DA[Y''],\qquad Y=(Z,f_B),\\
 \|[\partial_\theta,A]\|_2\le A_{\rm wide}\Xi_1,\quad
 \|[\partial_\theta,[\partial_\theta,A]]\|_2
       \le A_{\rm wide}(2\Xi_1^2+\Xi_2).
 \end{gathered}
 \tag{QH.16}
$$

For a scalar output, translation on the left is the identity. This is
the same formula and does not discard a scalar row. The factor
$|D|^{-2}$ of the height direction commutes with translation.

Using the derivative-vector norm for $H^2$, and then the adjoint,

$$
 \|A\|_{H^{\pm2}\to H^{\pm2}}
 \le A_{\rm small}
       +A_{\rm wide}(2\Xi_1+2\Xi_1^2+\Xi_2).
 \tag{QH.17}
$$

The adjoint identity follows on dense trigonometric polynomials and
extends by the completed module bound. It proves the scalar rows are
functionals on $H^{-2}$ as well. QN's finite-Fourier approximation of
the zero-width value problem, with these uniform commutator estimates,
shows these are derivatives of the same actual nonlinear graph.
No different formal DN operator has been introduced.

Substitution of QN.29 gives the strict complete bounds

| Actual derivative | Every $-2\le s\le2$ | At $s=7/6$ |
|---|---:|---:|
| $D_Zd$ | .030 | .0021 |
| $D_Zc_0$ | .00375 | .0002625 |
| $D_{f_B}d\,|D|^{-2}$ | .003334 | .000234 |
| $D_{f_B}c_0\,|D|^{-2}$ | .00041675 | .00002925 |

The last column uses QN's already paid $H^1$ bounds and

$$
 \|A\|_{H^{7/6}}^6\le\|A\|_{H^1}^5\|A\|_{H^2}.
 \tag{QH.18}
$$

All comparisons are exact sixth-power rational comparisons.
The actual upper expressions for the four $H^2$ norms are below
$.029519168,.003689896,.003279908,.000409989$, respectively.
The mean columns follow from $C=(T-\epsilon)/8$ and
$V=(U-\epsilon)/8$, with $\epsilon=2^{-512}$ retained.

## QH4. The actual physical boundary graph and all independent columns

All real composition, inverse composition and multiplier bounds
QN.19--QN.24 already hold for every $|s|\le2$, as does the exact
Hilbert-conjugation bound $K_H<6\,10^{-7}$. Thus they cover $s=7/6$.
They use only the known centre and the actual endpoint $A^3$ norm.

Use the last column of the preceding table in the exact QN.34--QN.37
calculation, including the onto nonmean chart and its attached mean.
Specifically let $c=1.000001$, $g_0=5.8$, and retain QN's quantities
$m_l,m_u,U_a,W_a,U_1,V_1,b_j,V_a,B_2$. Define

$$
 \begin{gathered}
 L_*={c(1+b_j)\over g_0^2},\qquad
 E_2=[W_a(2m_u+W_a)+V_1V_a/4]c(1+C),\\
 I_*={L_*\over1-L_*E_2}<.03,\\
 E=I_*\{m_u[c(T+\epsilon+C)+K_Hc(1+T+\epsilon)]
           +W_ac(1+T+\epsilon)\\
 \hspace{33mm}
 +[V_a(U_a+U_1/4)
      +(W_a(2m_u+W_a)+V_1V_a/4)/g_0]c(1+C)\},\\
 B_a=V_ac,\qquad
 C_a=V_a(U_a+U_1/4)+B_2/g_0+EB_2.
 \end{gathered}
 \tag{QH.19}
$$

Then the exact physical row is $\mathcal Rh=\mathcal Ey+\zeta$,
with $y=P_{\ne0}h_2$, $\|\mathcal E\|_{H^{7/6}\to H^{7/6}}\le E$,
and

$$
 \|\zeta\|_{H^{7/6}}
 \le B_a(UF_B+\|r_B\|_{H^{7/6}})
                 +C_a(VF_B+|r_C|),\qquad
 F_B=\||D_\theta|^2\dot f_B\|_{H^{7/6}} .
 \tag{QH.20}
$$

The independent nonmean physical Robin residual $r_B$, physical
curvature-mean residual $r_C$, and height direction $\dot f_B$ have
not been exchanged for background radii.

In the actual Riccati frame of QN put $X_k=|k|Z_k$ on $|k|\ge388$.
The exact endpoint identities are

$$
 \begin{gathered}
 X_{u,H}=-P_H|D|^{7/6}W^{-1/2}(\mathcal Ey+\zeta),\\
 y_H=|D|^{-7/6}W^{-1/2}(X_{s,H}+X_{u,H}).
 \end{gathered}
 \tag{QH.21}
$$

Here $W>1/8$. The high homogeneous/Bessel comparison at $7/6$
is less than $17/16$; for example the exact test
$(1+388^{-2})^7<(17/16)^{12}$ suffices.
Thus the full high boundary feedback is at most
$A_o=(17/2)E$ and

$$
 {A_o\over1-A_o}<.004203794<.0043 .
 \tag{QH.22}
$$

This is a bound for the entire physical boundary operator, without a
finite angular support assumption. All its affine columns are

$$
 \begin{aligned}
 \|X_{u,H}(R)\|
 <{}&.0043\|X_{s,H}(R)\|
       +.002\|y_L(R)\|_{H^{7/6}}\\
    &+.0061F_B+23\|r_B\|_{H^{7/6}}+28|r_C|.
 \end{aligned}
 \tag{QH.23}
$$

The four source bounds are obtained from
$(51/16)(1-A_o)^{-1}(E,B_aU+C_aV,B_a,C_a)$.
The true low/head endpoint $y_L(R)$ is an independent prescribed
boundary input. It is not an arbitrary trace of a radial $L^2$ input.

The attached moving mean remains

$$
 |\langle h_2(R)\rangle|
 <.000383\|y(R)\|_{H^{7/6}}
             +.001435F_B+49.020|r_C|.
 \tag{QH.24}
$$

Its exact coefficients are $m_u^2CI_*$,
$m_u^2(1+CI_*B_2)V$, and $m_u^2(1+CI_*B_2)$.
This is a compatibility row for the complete head, not an automatic
extra equation imposed by solving the high block. The original two
physical-density means and the independent world-height data retain
their previous roles.

## QH5. The complete body and collar energy in order +1

The scalar angular conjugation $X_k=|k|Z_k$ has raw frame
$F^+_N=N^{-1}F_N$. Its radius-independent factor does not introduce a
radial derivative. Its logarithmic frequency derivative has norm at
most $8/3$, just as for QN's frame $NF_N$ in order $-1$.

For either pair of signs the rank-one formula QN.9 therefore gives

$$
 \|(F^+_M)^{-1}S_\alpha S_\beta^{-1}F^+_N\|
 <3R_{MN}^{5/3},\qquad
 R_{MN}={\max(M,N)\over\min(M,N)} .
 \tag{QH.25}
$$

For equal signs with $R_{MN}\le2$, the matrix ODE proof gives
$N\|(F^+_M)^{-1}F^+_N-I\|<17|M-N|$.
For larger ratios or opposite signs the same QN.9--QN.11 argument
gives the bounds $8|M-N|R_{MN}^{5/3}$ or
$4|k-n|R_{MN}^{5/3}$. Hence the entire all-frequency drift,
reaction and ordered primitive increments in QN.14--QN.15 hold
unchanged for order $+1$.

In particular the unknown background is charged only through
$A_w$ and its first angular derivative, where
$w(\ell)=(1+|\ell|/388)^{5/3}$. Both are bounded by its $A^3$ norm.
All signed intermediate primitive modes remain, with the true inverse
divisor at least4; no intermediate high projection is inserted.
The high-to-high mean rank vanishes because its input has zero mean.
Its full-tail mean-input high column remains in the supplied head
forcing.

The known degree32 centre uses the originally completed order $+1$
row, with constants $(18,9,8)$. This positive order was already paid
in [B.4--B.9](R133-supplement-full-delta-positive-M32-base-and-M96-difference.md);
its previously missing physical $H^{7/6}$ exterior has now been paid
by QH3--QH4. No inference from a negative order alone is used here.

Use QN's completed bound $D(4,181)<18000\rho$, $\rho=10^{-6}$,
and write

$$
 \begin{gathered}
 \tau=1.894\,10^{-7}+\rho+(1.894\,10^{-7})\rho,\qquad
 \sigma=3.788\,10^{-7}+2\rho,\\
 T_{+1}^{\,Q}
 \le{1.003/(1-\rho)+9000\rho\over1-2\sigma}\,T_{+1}^{\,o}
 <.797741791 .
 \end{gathered}
 \tag{QH.26}
$$

This is exactly the scalar same-reference comparison QN.41, with a
conservative already paid scalar enlargement. The complete
original body value $T_{+1}^{\,o}$ is read from its saved order1
conclusion. Therefore

$$
 \chi:=T_{+1}^{\,Q}+{A_o\over1-A_o}<.803,\qquad
 q_b={1000\over197},\qquad r_b={803\over197}.
 \tag{QH.27}
$$

The ordinary source and jump norms are $H^{4/3}$, rather than the
negative-window $H^{-2/3}$. Positive powers obey
$|k|^{4/3}\le\langle k\rangle^{4/3}$, so the original homogeneous
source factors need no negative Bessel enlargement. The already saved
negative source/jump constants include a larger harmless factor and
give the valid convenient bounds

$$
 B_f=.126142,\qquad C_b=2.518,\qquad
 \text{raw body-jump factor }4.953 .
 \tag{QH.28}
$$

For reconstruction, the saved original order1 body constant already
has the positive Bessel output convention. Both actual metric signs
and the complete positive body are included.

In the collar the known-centre complete kernel has bound144 and
shared drift derivative bound $9/100$. The extra positive conjugation
has ratio at most3 there. Its exact skew commutator satisfies

$$
 {|k+l|\over2}|d_{k-l}|
       \left|{|k|\over|l|}-1\right|
 \le2|k-l|\,|d_{k-l}|,
 \tag{QH.29}
$$

since connected high signs agree and their ratio is at most3.
Thus the same valid complete bound is $432.18$. The full-tail
increment is still below $92\rho$. With $h=9\,10^{-6}$ this gives

$$
 q_c={250\over249},\quad r_c={1\over249},\quad
 B_c=.009000020,\qquad h(432.18+92\rho)<1/250 .
 \tag{QH.30}
$$

The source constant again conservatively includes the old negative
Bessel fee. Raw positive $H^1$ collar reconstruction is below
$3.00001$; the exact test is
$9(1+388^{-2})<(3.00001)^2$.
The common reference remains the actual mean reference with
$g_N(a)=N^{-1/3}$ and the actual terminal scalar $p_Q(R)$.

## QH6. The whole inverse, its true traces and seven source columns

Use exactly the original seven ports
$(s,F_c,F_b,B,J_c,J_s,J_u)$, now with the following angular units.
$s$ is the stable incoming $X$ norm at the true root. $F_c,F_b$
are the full ordinary $L^2_rH^{4/3}_\phi$ sources on collar/body,
including the complete prescribed finite-head forcing. $B$ contains
the entire affine exterior row (QH.23) and all weighted body jumps.
$J_c$ contains all collar jumps; $J_s,J_u$ are the two signed
interface jumps. Raw ordinary jumps have their actual $H^{4/3}$
norms and are mapped by the actual frames with the preceding factors;
they receive no radial length multiplier.

The prescribed finite head and its moving mean are not projected
away. In particular the full-tail coefficients in (QH.2) can produce
arbitrarily high output from a low input. Their forcing is
$P_H\mathcal A_QP_Lh$ in the displayed ordinary norm, with every
primitive and mean-rank term retained. This belongs to $L^2_rH^{4/3}$
for an $L^2_r$ finite head: the coefficient products use at most
$Q_\phi\in A^{4/3}$, which follows from the stated low $A^3$ domain
and the fixed smooth centre. The endpoint low norm in (QH.23) is
separate input.

Let $\Lambda=r_cr_b$, $\Sigma=(1-\Lambda)^{-1}$. The exact
same-reference matching formulas remain

$$
 \begin{aligned}
 X_b&=\Sigma\{q_cs+q_c(B_cF_c+J_c)+J_s
                    +r_c[q_b(B_fF_b+B)+J_u]\},\\
 Y_b&=r_bX_b+q_b(B_fF_b+B)+J_u,\\
 U_a&=r_cs+q_cY_b+q_c(B_cF_c+J_c),\\
 S_b&=q_b(X_b+B_fF_b+B),\\
 S_c&=q_c(s+Y_b+B_cF_c+J_c).
 \end{aligned}
 \tag{QH.31}
$$

The true loop satisfies $\Lambda<.016371$. The raw whole positive
state and the two actual endpoint readouts obey

$$
 \begin{gathered}
 \|h_H\|_{L^2_rH^1}
 \le[\,h(3.00001)^2S_c^2+(2.518)^2S_b^2\,]^{1/2},\\
 \|h_{2,H}(R)\|_{H^{1/6}}\le(5/388)S_b,\qquad
 \|h_{2,H}(R)\|_{H^{7/6}}\le5S_b .
 \end{gathered}
 \tag{QH.32}
$$

These boundary readouts come from the actual frame solution and
(QH.21); they are not trace assertions about arbitrary radial
$L^2$ functions.

Every number in the following table is a strict rational upper bound.
The ordinary radial measure and all original jumps are unchanged.

| Output | $s$ | $F_c$ | $F_b$ | $B$ | $J_c$ | $J_s$ | $J_u$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Body frame sup | 5.181348 | .046633 | .653586 | 5.181348 | 5.181348 | 5.160622 | .020726 |
| Root outgoing | 4.181348 | .046633 | .653586 | 5.181348 | 5.181348 | 4.160622 | 1.020726 |
| Raw $L^2_rH^1$ | 13.046717 | .117422 | 1.645740 | 13.046717 | 13.046717 | 12.994501 | .052990 |
| Outer even $H^{1/6}$ | .066770 | .000601 | .008423 | .066770 | .066770 | .066503 | .000268 |
| Outer even $H^{7/6}$ | 25.906736 | .233162 | 3.267928 | 25.906736 | 25.906736 | 25.803109 | .103627 |

Existence and uniqueness are the same complete Hilbert energy/Green
construction as QN7, now with the positive scalar angular conjugation.
The exact skew transport is retained in every approximating equation.
The all-frequency estimates are uniform for finite Fourier
approximations of the background; the two strict feedback gates give
the actual infinite-dimensional inverse in the limit.

At the root, $X$ is equivalent to
$(|D|^{4/3}h_1,|D|h_2)$ with the original factor9.
A Bessel mixed input in $H^{4/3}\oplus H^1$ pays at most9.
The reverse Bessel output costs at most9.00005; the exact comparison
is $9^3(1+388^{-2})^2<(9.00005)^3$.
Thus the next root source/state unit is specified without exchanging
the weak root window for the strong one.

Finally the same triangular root change of QN.44 holds for $F_N^+$:
its scalar angular factor cancels. The original-coordinate root
reflection is below

$$
 {\tau+\|\mathcal R_Q\|\over1-\tau}
 <4.181353313<4.182 .
 \tag{QH.33}
$$

Multiplication of the whole response table by1.00001 covers all
old-frame input/output changes, including the additive first
reflection term. The original finite193 reference, original $S_i$,
root97 and outer96 observations are not replaced by this high graph.
The high inverse is available for the supplied complete head;
its low/high Schur feedback and the negative return still have to be
consumed in that original coupled problem.

## QH7. Reproducible finite arithmetic and the next higher-order scope

The reader
[fourfold_codazzi_compact_positive_H1_saved_bounds.py](../scripts/fourfold_codazzi_compact_positive_H1_saved_bounds.py)
performs 34 exact rational comparisons. It reads only completed
small scalar conclusions and combines them with the proved formulas
above. In particular it reads the final original second-translation
bound, not the old tail choices. It performs zero native coefficient,
Fourier-tail, reference-ODE or kernel-sweep evaluations.

The actual newly paid result is (QH.1), including the full exterior
$H^{7/6}$ graph and its mean/height columns. The companion
[strict tame flow](R144-supplement-strict-angular-tame-Cauchy-flow-with-one-high-background-factor.md)
already gives every integer angular order on the strict negative
piece with a single high background factor.
Higher positive/root increments must still retain the differentiated
principal transport, original mean terms, complete physical
boundary commutators and their own actual source/trace units.
This first positive increment does not claim those later estimates.
