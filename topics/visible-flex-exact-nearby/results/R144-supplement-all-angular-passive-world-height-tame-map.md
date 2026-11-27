# R144 WT: the complete real all-angular passive world-height map

2026-11-27, visible-exact-astra-fb31ed6-20261127.

This supplies the higher-order height estimates left open by
[WH](R144-supplement-complete-passive-world-height-Hessian-with-independent-ports.md).
The map is the very same off-constraint world reconstruction, with its
actual independent terminal frame, position and waist trace. Its value,
first derivative and Hessian are tame at every integer angular order.
The fixed-physical-angle Hessian loses at most three angular derivatives
in the displayed direction scale. Only one higher background norm occurs.
There is no spatial strip assumption, complex composition of a rough
direction, reset of the world anchor, or use of the equations to erase an
angular compatibility defect.

These are estimates of the complete nonlinear map. They do not supply a
signed height carrier, an inverse for its bordered rows, or a closed
embedding. WH's sharper low-norm $H^{-3}$ bound remains available and is
not replaced by the deliberately large constants below.

## WT1. Exact domain and real function spaces

Use exactly WH.1--WH.5, including the entire admitted parameter interval,
the full-tail $A^3$ background, $R=25/8$, and $A=2^{20}$. In particular

$$
 \|Q\|_{A^0,\oplus_1}<10,\quad |m|>1,\quad
 \|O_R\|_{L^\infty,op}\le1,\quad \|F_R\|_\infty\le A.
 \tag{WT.1}
$$

The first inequality follows from WH's Euclidean pair bound7 and
$7\sqrt2<10$. The affine extension in $O_R$ is the same one as in WH.
At the waist $J=v_w/m_w$ satisfies $1/100<J<7$. Keep its actual mean
and the original constant convention in $\Theta=\phi+Iv_w/m_w$.
All world fields have their full $2\pi$ dependence. Their norms use
normalized measure; fourfold scalar fields thereby keep their old norms.

For integers $s\ge0$ put

$$
 B_s=1+\sup_{0\le r\le R}\|Q(r)\|_{A^s,\oplus_1},\qquad
 P_s=\|O_R\|_{H^{s+1},{\rm Frob}}+A^{-1}\|F_R\|_{H^{s+1}}.
 \tag{WT.2}
$$

Here $A^s$ uses $(1+k^2)^{s/2}$ on the genuine angular frequency $k$.
Using the larger original $(1+|k|)^s$ Wiener norm is also sufficient.
The background trace is the actual $Q(0)$ and is covered by $B_s$.
$B_0<11$; no smallness is required of $B_s$ or $P_s$ at high order.
$P_0$ is an explicit independent low terminal norm, not a hidden constant
claimed from the radial state norm.

For a direction $x=(h,\kappa,U,Y,h_w)$ and an integer $s\ge1$, set

$$
 E_s(x)=\|h\|_{L^2_r(H^s\oplus_1H^s)}+100\sqrt R|\kappa|
       +\|U\|_{H^s,{\rm Frob}}+\|Y\|_{H^s}
       +\|h_w\|_{H^s,\oplus_1}.
 \tag{WT.3}
$$

The harmless component-sum radial norm may be replaced throughout by
the sum of the two $L^2_rH^s$ norms. On smooth inputs $h_w=h(0)$, but
its displayed norm must still be supplied. No trace from radial $L^2$
is asserted. The terminal increments are in their actual moving angle;
an upstream physical-angle graph must pay its own coordinate derivatives.

Define the explicit order constant

$$
                 C_n=2^{200(n+12)}((n+12)!)^8,
                 \qquad n=0,1,2,\ldots .
 \tag{WT.4}
$$

It depends only on the displayed order and the already fixed low domain.
In particular no unknown high norm occurs in an exponent or denominator.

## WT2. Elementary single-high-factor bookkeeping

For any nonnegative moment sequence formed from a fixed positive measure,
Hölder gives $b_j\le b_0^{1-j/N}b_N^{j/N}$ for $0\le j\le N$.
The same assertion holds for $H^{j+1}$ norms, for $L^2_rH^{j+1}$ norms,
for their sums, and for the supremum in (WT.2). Thus, whenever
$j_1+\cdots+j_l=N$,

$$
                 B_{j_1}\cdots B_{j_l}\le11^{l-1}B_N.
 \tag{WT.5}
$$

There is a useful version with differently coloured direction factors.
Each occurrence of a direction has exactly one colour and appears only
once. If its indices, the background indices and an optional terminal
index have sum at most $N$, divide each factor by its order-zero norm,
apply interpolation and then weighted arithmetic-geometric mean.
The result is a sum in which exactly one factor is evaluated at order
$N$; every other factor remains at order zero. Zero order-zero norms
are handled by continuity. At most one terminal factor occurs because
the reconstruction is affine in $(O_R,F_R)$.

For example the terminal/background reduction is

$$
 P_jB_{N-j}\le P_0B_N+11P_N,
 \tag{WT.6}
$$

and the two-direction reduction, with $j+k+l=N$, is

$$
 B_j E_{k+1}(x)E_{l+1}(y)
 \le B_NE_1(x)E_1(y)
       +11E_{N+1}(x)E_1(y)+11E_1(x)E_{N+1}(y).
 \tag{WT.7}
$$

The same proof works when any factors have smaller total order.
This reduction is applied to complete expanded jet terms, before
multiplying separate high-norm upper bounds. It is therefore not an
argument that accidentally produces $B_N^2$ or $P_NB_N$.

The only embedding needed for full-circle directions is

$$
                 \|f\|_{A^j}\le2\|f\|_{H^{j+1}}.
 \tag{WT.8}
$$

It follows directly from Cauchy--Schwarz and the full-circle reciprocal
weight sum $\sum_k(1+k^2)^{-1}<4$ already proved in WH. Derivatives,
the actual zero-mode projection and $I$ commute with angular translation;
$I$ has multiplier zero at0 and modulus at most $1/4$ elsewhere on the
original fourfold fields. Nothing here deletes their original mean.

## WT3. Complete coefficient jets, with the true metric parameter

Put ${\cal A}=\begin{pmatrix}M&c\\0&0\end{pmatrix}$ with the exact
$M,c$ of WH.5 and set $K_*=2^{30}A=2^{50}$. Expanding $d$ in those
formulas leaves twelve scalar terms: three in $p$, three in $k$, two
in $t$, one in $c_1$ and three in $c_2$. Each has at most three angular
$u,v$ factors, one actual ordered primitive, a scalar factor $1/m$
when present, and an intrinsic radial coefficient. The duplicated skew
entries cost at most2 in Frobenius norm.

All intrinsic coefficients and their first two true parameter derivatives
are bounded by $32A$. For the only product requiring a check,

$$
 |(b\beta K)_{\nu\nu}|
 \le(1/2)6+2(1)4+2(8)=27<32;
 \tag{WT.9}
$$

the other cases follow directly from WH.4. This retains $K_\nu$,
$K_{\nu\nu}$, $\gamma_\nu$, $\gamma_{\nu\nu}$ and both mixed terms.
The reciprocal mean has first derivative $-\mu/m^2$ and mixed
derivative $2\mu\lambda/m^3$, where $\mu=\Pi h_2$ and
$\lambda=\Pi k_2$. These are actual scalar mean slots.

Two variations can hit at most five factors in each term. The ordered
choices, including the reciprocal's factor2, cost at most50. After the
two direction embeddings in (WT.8), a convenient whole count is

$$
 12\cdot50\cdot2\cdot32\cdot10^3\cdot4
                  =153600000<2^{30}.                 \tag{WT.10}
$$

It also dominates the orders0 and1. Splitting an angular moment among
the at most three nonconstant factors costs at most $3^{j+1}$.
Consequently every complete $j$th angular coefficient jet with at most
two distinct state/parameter colours is bounded by $K_*3^{j+1}$ times
the coloured single-high expressions from WT2, locally in $r$.
With no direction the assertion holds in $A^j$ as well.
All primitive divisors, every Fourier sign and the mean derivatives
are included. There is no finite support assigned to $h$ or $q$.

For radial integration a single direction uses
$\|h\|_{L^1_rH^s}\le2\|h\|_{L^2_rH^s}$, because $R<4$.
Two directions in the same coefficient jet use Cauchy--Schwarz and
give $L^1_r$ directly. If they occur in separate time-ordered factors,
apply the one-direction inequality to each. Background factors cost
at most4 in radial $L^1$. These are the only radial conversions used.

## WT4. Ordered real rigid-motion jets have no high-norm exponential

The exact augmented reconstruction is

$$
 G=\begin{pmatrix}O&F\\0&1\end{pmatrix},\qquad
 G_r=G{\cal A},\qquad G(R)=\begin{pmatrix}O_R&F_R\\0&1\end{pmatrix}.
 \tag{WT.11}
$$

Let $V(s,r)$ be its relative propagator, with identity initial value.
This relative identity is a change of variables inside the proof;
the actual output is always $G(R)V(R,r)$. Its upper-left block is
orthogonal, and its translation block is the integral of an orthogonal
matrix times $c$. WH's complete $\|c\|_\infty\le630A$ gives, for every
subinterval and every real background,

$$
 \|V(s,r)\|_{op}\le2+630RA<\Lambda,
                    \qquad\Lambda=2^{32}.             \tag{WT.12}
$$

This uses the affine rigid-motion structure, rather than the general
bound $\exp\int\|{\cal A}\|$. It is valid off the PDE constraints.

For $l$ distinct coefficient increments $A_1,\ldots,A_l$, the exact
$l$th variation is the sum of the $l!$ ordered integrals

$$
 \int_{r<t_1<\cdots<t_l<R}
 V(R,t_l)A_{\sigma(l)}(t_l)V(t_l,t_{l-1})\cdots
 A_{\sigma(1)}(t_1)V(t_1,r)\,dt,
 \tag{WT.13}
$$

with the appropriate common orientation sign. Norms ignore that sign.
The permutation simplices partition the whole cube after taking norms,
so their sum is bounded by
$\Lambda^{l+1}\prod_i\|A_i\|_{L^1_r}$. It is not necessary to insert
an additional $l!$ in this product bound.

Apply $n$ angular derivatives and $p\le2$ distinct input variations.
The full chain rule is indexed by partitions of the $n+p$ labelled
derivative slots. Each block is precisely one coefficient jet from WT3.
There are at most $(n+p)!2^{n+p}$ partitions: an ordered listing of
blocks and a cut pattern already overcounts them. Angular orders over
all blocks sum to $n$; each direction colour occurs exactly once.
Use the radial conversions from WT3, (WT.5--7), and (WT.12--13).
The factors4 (radial),3 (moment),11 (low background),3 (colour choice)
and2 (partition count) are dominated, including another factor3 per
angular derivative, by $2^{16}$ per slot. Thus a convenient common
relative-jet majorant is

$$
 D_n=\Lambda(n+2)!L^{n+3},\qquad
                 L=2^{16}K_*\Lambda=2^{98}.            \tag{WT.14}
$$

For $p=0$ it multiplies $B_n$. For $p=1$ it multiplies
$E_{n+1}(x)+B_nE_1(x)$. For $p=2$ it multiplies

$$
 E_{n+1}(x)E_1(y)+E_1(x)E_{n+1}(y)+B_nE_1(x)E_1(y).
 \tag{WT.15}
$$

These assertions initially bound the entire $n$th angular derivative
in $L^\infty_\phi$, and are uniform in the output radius. Directions
in (WT.3) include more inputs than the relative propagator uses, which
only enlarges its right side. No angular derivative of an unobserved
tail was assigned a finite Fourier cutoff.

Multiply by the actual $G(R)$ in (WT.11). Its value uses one terminal
factor, its first variation uses one $U,Y$ factor, and its second
variation is exactly zero. Apply the complete Leibniz rule and then
(WT.6--7), before estimating the result. The elementary conversion
from integer derivatives to the Bessel $H^n$ norm costs at most
$2^{n/2}$ times the largest of their norms. The following explicit
constant dominates all these factors, including $A$ and the terminal
embedding in (WT.8):

$$
                    R_n=2^{128(n+8)}((n+8)!)^4.
 \tag{WT.16}
$$

For $X=(O,F)$ the resulting actual moving-angle estimates are

$$
\begin{aligned}
 \|X\|_{L^\infty_rH^n}
 &\le R_n\{(1+P_0)B_n+P_n\},\\
 \|DX[x]\|_{L^\infty_rH^n}
 &\le R_n\{(1+P_0)E_{n+1}(x)
               +[P_n+(1+P_0)B_n]E_1(x)\},\\
 \|D^2X[x,y]\|_{L^\infty_rH^n}
 &\le R_n\{(1+P_0)[E_{n+1}(x)E_1(y)+E_1(x)E_{n+1}(y)]\\
 &\hspace{34mm}+[P_n+(1+P_0)B_n]E_1(x)E_1(y)\}.
 \tag{WT.17}
\end{aligned}
$$

The norm of a pair can be its component sum. The proof above may absorb
that factor in (WT.16). The only higher background factors on each
right side are $B_n$ and $P_n$, each linear. $1+P_0$ is an explicit
low terminal norm. In particular there is no growth exponential in
any high angular norm, nor a claim that an independently prescribed
terminal curve is constant in the moving angle.

## WT5. The complete inverse-angle Hessian

Write $f(\phi)=e_z\cdot F(0,\phi)$, $\psi=\Theta^{-1}$ and
$Z=f\circ\psi$. For each direction put $a_x=\Theta_x$ and keep
$a_{xy}=\Theta_{xy}$ exactly as in WH.20. Then

$$
\begin{aligned}
 DZ[x]&=[f_x-f' a_x/J]\circ\psi,\\
 D^2Z[x,y]&=\left[f_{xy}-\frac{f_x'a_y+f_y'a_x}{J}
             +\frac{f''a_xa_y}{J^2}-\frac{f'a_{xy}}{J}\right.\\
 &\hspace{13mm}\left.
       +\frac{f'(a_x'a_y+a_y'a_x)}{J^2}
       -\frac{f'J'a_xa_y}{J^3}\right]\circ\psi .
 \tag{WT.18}
\end{aligned}
$$

To verify the formula, use
$\psi_x=-(a_x/J)\circ\psi$ and differentiate
$\Theta(\psi)=\theta$ a second time. The three terms in $\psi_{xy}$
are $-a_{xy}/J$, $(a_x'a_y+a_y'a_x)/J^2$ and
$-J'a_xa_y/J^3$, all composed with $\psi$.
This accounts for every term in (WT.18), including both moving-mean
contributions in $a_{xy}$. No equation relating $F_\phi$ to an angular
frame column is used; $f'$ and $f''$ are derivatives of the actual
off-constraint passive position.

For clarity an elementary real composition estimate suffices. Put
$b=J^{-1}$ and ${\cal L}=b\partial_\phi$. Exactly

$$
 \partial_\theta^j(q\circ\psi)=({\cal L}^j q)\circ\psi,
 \qquad
 \|q\circ\psi\|_2^2=\int |q|^2J\,d\phi\le7\|q\|_2^2.
 \tag{WT.19}
$$

Expanding ${\cal L}^j$ gives at most $j!$ weighted words, each with
$j$ copies of $b$ and one differentiated $q$. Derivatives on the
$b$ copies have total order at most $j-1$. Differentiating $1/J$
expands into reciprocal words; their coefficient sum is bounded by
$2^l l!$ at derivative order $l$, their denominator power is at most
$l+1$, and their total numerator derivative order is $l$.
These claims follow directly by differentiating once and induction.
Consequently a whole composition word at order $j$ has reciprocal
cost at most $100^{2j}$, a coefficient count bounded by
$2^j(j!)^3$, and numerator derivatives of the exact total order
left after differentiating $q$.

Use the same expansion on (WT.18), with its displayed extra powers
of $J^{-1}$. In the value, first derivative and Hessian, the total
angular order to allocate is respectively at most $n$, $n+1$ and
$n+2$. The complete $a_x,a_{xy}$ formulas have at most the original
two nonconstant factors, and at most two direction colours. Their
mean factors have angular order zero. Their primitive norm is at
most1, so discarding this gain is harmless. The small denominators
are only the already fixed $|m|>1$ and $J>1/100$.

Including the finite terms of (WT.18), reciprocal words, the true
Jacobian in (WT.19), and the Bessel conversion, a convenient whole
composition count is

$$
                    T_n=2^{40(n+6)}((n+6)!)^4.         \tag{WT.20}
$$

For example the worst denominator power is at most $2n+5$, the
low numerator moment costs at most $11^{n+5}$, the coefficient
words cost at most $2^{n+6}((n+6)!)^3$, and the Jacobian/Bessel/
finite-formula factors fit the remaining powers in (WT.20).
This estimates an actual real diffeomorphism on arbitrary full
Sobolev inputs; no Fourier-band or complex-angle substitution is used.

## WT6. All-order height value, derivative and Hessian

Insert the expanded ordered jets of WT4 into the complete expression
in WT5, and only then apply the one-high-factor reduction WT2.
Every resulting term has at most one terminal background factor.
The maximal allocated order is $n+2$, so no higher background than
$B_{n+2}$ or $P_{n+2}$ is needed. A direction at allocated order $j$
is paid by $E_{j+1}$, as specified in (WT.8). All constants are
dominated by (WT.4): in particular $R_{n+2}T_n$ and the finite
coloured-product factors fit $C_n$ for every $n\ge0$.

The exact whole height therefore satisfies

$$
\begin{aligned}
 \|Z\|_{H^n}
 &\le C_n\{(1+P_0)B_n+P_n\},\\
 \|DZ[x]\|_{H^n}
 &\le C_n\{(1+P_0)E_{n+2}(x)
              +[P_{n+1}+(1+P_0)B_{n+1}]E_2(x)\},\\
 \|D^2Z[x,y]\|_{H^n}
 &\le C_n\{(1+P_0)
       [E_{n+3}(x)E_3(y)+E_3(x)E_{n+3}(y)]\\
 &\hspace{26mm}+[P_{n+2}+(1+P_0)B_{n+2}]E_3(x)E_3(y)\}.
 \tag{WT.21}
\end{aligned}
$$

Every physical Fourier mode and the height mean are covered by these
Sobolev norms. This is the complete same-world height, not its finite
observation or its high projection. The sharper WH.26 remains the
separate low-order estimate when only its weaker input norms are given.

The constants were made generous to keep the proof uniform. Their
growth is explicit and elementary; it is factorial in the order and
geometric in the fixed low bounds, never exponential in $B_s$ or $P_s$.
The parameter interval, full tails, two means and real angle convention
are exactly those already used by WH. The actual variation $h$ includes
any centre derivative if a consumer later composes $Q$ with its compact
parameter family; that derivative is not silently discarded here.

## WT7. Remainders, density and the actual remaining interfaces

On an admitted real line segment, replace $B_s,P_s$ on the right side
of (WT.21) by their suprema over that segment. Taylor's integral formula
then gives the complete $H^n$ quadratic remainder bounded by

$$
 C_n\{(1+P_0^*)E_{n+3}(z)E_3(z)
       +[P_{n+2}^*+(1+P_0^*)B_{n+2}^*]E_3(z)^2\}.
 \tag{WT.22}
$$

The derivative-difference estimate is the full bilinear right side of
(WT.21) with directions $z,h$ and the same segment suprema. These
statements include the physical height mean and all higher modes.

Smooth angular approximations establish the identities first. Apply
positive Fejer convolution to the perturbation $q$ and the terminal
inputs, retaining the original smooth compact centre. The low $q$
radius, actual means, convex matrix/position bounds and full tails
are preserved. The complete $Q$ moments have limsup no larger than
their original values, since the centre's omitted smooth tail tends
to zero; the strict waist gap holds for all sufficiently fine
approximations. Radial approximation is performed on each original
continuous segment and keeps all actual terminal data.
The exact real ODE, its displayed first two variational equations and
the positive real inverse-angle map converge in the stated norms.
The uniform estimates above then extend the derivatives by density.
Any independently prescribed frame or position impulse must be inserted
as an additional actual affine port; none is manufactured from a
radial $L^2$ source. The present uninterrupted passive reconstruction
retains all original joins of WH.

For genuine orthogonal anchors the result is the actual world map.
The affine extension was used only for differentiation and estimates.
If a cap or outer graph supplies the terminal inputs, its actual first
and second derivatives and any change from physical to moving angle
must be composed with (WT.21), with their own low and high norms.
Neither those equations nor the full bordered inverse follow from WT.

The same PDE, holonomy, position periods, regular caps, waist reflection,
two curvature means and same-metric family requirements remain.
No signed world carrier was reconstructed or assumed. This result
closes the previously unpaid all-angular tame estimate of the passive
height map; it does not claim the entire nonlinear iteration or final
geometric completion.

The companion saved-bound reader checks only the new rational majorants
and the symbolic order domination used here. It never evaluates an old
frame, coefficient array, Fourier target, Riccati equation or norm.

