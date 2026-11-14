# R133 supplement: finite-order parametrices for the actual moving root relation

2026-11-14, phase_inverse.

**Proved analytic construction, with the exact residual-to-solution
contract stated below.** The operator is the moving Jacobi operator at
the continuous repaired M32 centre, at intrinsic $\eta_0$ and affine
offset $\delta=0$. The original angular primitive, its mean, both
curvature rows, the supplied low head and the actual regular endpoint
are retained.

The result identifies the scalar finite root coefficient of the
given-head high relation: it is zero in the directed strict-density
convention. This does not set its nonmean first coefficient to zero.
It also proves a strong $4/3$ remainder after a sufficiently large
finite high cutoff, with an explicit norm formula in the residual
and amplitude constants. Those latter constants have not yet been
numerically evaluated here. Consequently no cutoff-97 return inverse,
no numerical strong-remainder budget, no nonzero-$\delta$ positive
graph and no nonlinear PDE branch are claimed.

## 1. The actual three interfaces

The fixed centre definition is
$\mathtt{440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47}$.
Use the exact notation of
[ordered root scalarization](R133-supplement-ordered-scalar-root-operator-and-one-gain-radial-remainder.md),
[the actual principal fold](R133-supplement-actual-moving-analytic-principal-fold.md)
and [the old primitive on Airy amplitudes](R133-supplement-original-primitive-on-actual-Airy-amplitudes-and-exact-mean.md).
In particular
$$
 \rho=r_*-r,\quad \partial=\partial_\phi,\quad
 I=\partial^{-1}(1-\Pi),\quad \eta=-\gamma m,\quad
 A=\eta\partial+L,\quad J=A^{-1}.                       \tag{P.1}
$$
Here $\Pi$ is always the old normalized mean at fixed $r$.
The fourfold physical frequencies are $4j$.

The fold native
$\mathtt{9300be45949cba94115511bf77d025a82e39c78d491ba77de916d7a96902fffd}$
is the actual 16-gate output of public run 43602612900.
The subsequent primitive run 43605453793 has native
$\mathtt{4ebc5865a8427e67e003e0aa25d8f629353ed87efd67d1705e1cdac7d2fc5b39}$.
The latter certifies, on their stated actual domains,
$$
 \|H_\epsilon^{-1}\|<1.000098,\quad
 c_\Pi>0.002921264998045,\quad
 \|[D_0,J]\|<253957.400944014 .                        \tag{P.2}
$$
The original full inverse $J$, not a finite section, is used.

The [same-reference positive graph](R133-supplement-repaired-positive-high-root-to-regular-graph.md)
has actually passed public run 43605513540, native
$\mathtt{2425a0338b958be5d7fb48c955b5a5ce59348f05f1832ab50a81d6cf7dbbc501}$.
It is the complete high block $|j|\ge97$ with the entire 193-coordinate
head supplied. The root state is the genuine global Riccati state
$$
 Z_j=n^{1/6}T_n^{-1}\operatorname{diag}(-i\epsilon,1)h_j,
 \qquad n=4|j|,\quad \epsilon=\operatorname{sgn}j .
$$
In its notation let
$$
 q_c=3000/2999,\quad r_c=1/2999,\quad B_c=9/1000,\quad
 q_b=(1-\chi)^{-1},\quad r_b^{\rm op}=\chi q_b,\quad
 \sigma=(1-r_c r_b^{\rm op})^{-1}.                    \tag{P.3}
$$
Its saved body source factor is $B_f$.
For zero stable root input, zero exterior input and zero affine jumps,
the exact seven-input contract implies
$$
 \|Z_u(r_*)\|
 \le q_cq_b\sigma(B_c F_c+B_f F_b)
 \le C_+\|(F_c,F_b)\|_2,\quad
 C_+=q_cq_b\sigma\sqrt{B_c^2+B_f^2}.                  \tag{P.4}
$$
Both $F_c$ and $F_b$ are ordinary $L^2_rH^{1/3}_\phi$ source norms.
For the collar coefficient, use
$1+q_c r_b^{\rm op}\sigma=q_b\sigma$; replacing $q_b$ by $q_c$
in (P.4) would be incorrect. With nonzero head, mean, exterior or
jump inputs use the entire original seven-column map, not (P.4)
with those inputs silently set to zero.
The actual two source columns are respectively below
$0.012924069462859$ and $0.181137705127099$.

At the root the two-row global $Z$ norm and
$(n^{1/3}h_1,h_2)$ bound each other by the proved factor 9.
Replacing $n^{1/3}$ by the Bessel weight
$\Lambda^{1/3}=(1+n^2)^{1/6}$ costs less than 2 on the high block.

Finally
[the complete root-to-negative Cauchy estimate](R133-supplement-full-family-root-to-negative-Cauchy-energy.md)
has actually passed run 43604498718, native
$\mathtt{8f165ccf9dee6e622060b4fc269908ef322f0b0fea15b82dc4b223a2fb4c122d}$.
On $0\le\rho\le9/10^6$ it gives
$$
 \sup_\rho\|h(\rho)\|_{L^2\times L^2}
 \le {41\over10}
 \left[\|(\Lambda^{1/3}h_1,h_2)(0)\|+
                 {3\over1000}\|g\|_{L^2_\rho H^{1/3}}\right].
                                                               \tag{P.5}
$$
This is the original complete moving system, including its even mean.
Only this proved $s=0$ output window is used below.

## 2. Exact finite amplitude calculus

Write
$$
 U_n(v)=e^{i\epsilon nX}
   \{v_1(T,X)\operatorname{Ai}(n^{2/3}T)
       +v_2(T,X)n^{-1/3}\operatorname{Ai}'(n^{2/3}T)\}.
                                                               \tag{P.6}
$$
All amplitudes in this section are analytic on a strictly smaller
product inside the genuine fold domain. Both signs are kept.
The even/odd reflection columns are the corresponding reflected
linear combinations; this costs at most the sum of the two column
norms. If complex columns are handled before that restriction, both
mean residuals are retained explicitly.

The following finite calculus is constructive.

1. Multiplication by any actual analytic coefficient preserves the
   two amplitudes exactly.
2. Each old angular or radial derivative is a sum of a degree-one
   polynomial in $n$, with analytic $2$ by $2$ coefficients, and
   actual derivatives of the two amplitudes.
3. Every occurrence of the old primitive has the exact finite
   identity (I.8). Its final term is bounded with the genuine
   $I$, and its old mean is retained.
4. For $J$, first solve its amplitude equation recursively by the
   invertible point matrix $\eta H_\epsilon$. If $g_N$ is the finite
   approximation and $E_N=APg_N-Pf$, use the exact identities
   $JPf=Pg_N-JE_N$ and
   $D_0(JPf-Pg_N)=-[D_0,J]E_N-JD_0E_N$.

There is no inversion of a formal infinite series in these rules.
To work to order $n^{-N}$ one uses a finite number of terms and
retains every final remainder. For any fixed number of derivatives,
taking the primitive and inverse expansions a correspondingly
larger finite number of terms gives an error of any prescribed
negative integer order in $n$.

Here is a direct norm justification of the last statement.
For real $T$ in a fixed compact interval, the two real Airy profiles
in (P.6) are uniformly bounded for $n\ge1$. Their derivatives are
controlled by the exact first-order identities
$f_0'=nf_1$, $f_1'=nTf_0$; each prescribed derivative therefore costs
at most one power of $n$ and a finite coefficient constant.
The old primitive has norm $1/4$, and $J$ has its proved full
$L^2$ and one-derivative bounds. A finite expansion through
$N+q+2$ terms consequently pays $q$ derivatives and leaves at least
the prescribed $n^{-N}$ power. The coefficient constants are supplied
by repeated Cauchy inequalities on finitely many nested products.
No pointwise derivative of an interval error is taken.

For reference the Airy real-axis bounds and the first two oscillatory
terms used here are the classical complete formulas with real
remainder bounds in
[DLMF 9.7(ii)--(iii)](https://dlmf.nist.gov/9.7).
On the positive axis they also follow by shifting the contour in
[DLMF 9.5.4](https://dlmf.nist.gov/9.5#E4) through its positive saddle.
The root initial values are
[DLMF 9.2.3--4](https://dlmf.nist.gov/9.2#E3).
These scalar facts are used only for the genuine Airy profiles;
they do not replace any moving-operator residual.

Divide the exact scalar operator (O.11), including its $R_{-1}D_0$
term, by the nonzero actual fold coefficient $\mu$, and denote the
result by $\mathcal P$. It has the finite amplitude expansion
$$
 \mathcal P U_n(v)
 =U_n\left[n\mathcal T_\epsilon v+
                 \sum_{k=0}^{N}n^{-k}\mathcal L_k v\right]
             +\mathcal E_{N,n}(v).                   \tag{P.7}
$$
Each $\mathcal L_k$ is a finite matrix differential operator with
analytic coefficients, regular at $T=0$. Its definition is obtained
by the four exact rules above with the original ordered factors.
The remainder contains all old means, projections and final
primitive/inverse terms. In particular $R_{-1}D_0$ starts at
degree zero in $n$; it is not deleted.

The degree-one operator $\mathcal T_\epsilon$ is exactly (I.19).
For analytic forcing its inverse with a prescribed common root
trace is the convergent characteristic integral (I.21).
Thus define $v_0=(a_0,b_0)$ by
$\mathcal T_\epsilon v_0=0$, $a_0(0,X)=1$, and recursively
$$
 \mathcal T_\epsilon v_{k+1}
    =-\sum_{q=0}^{k}\mathcal L_q v_{k-q},\qquad
 a_{k+1}(0,X)=0 .                                    \tag{P.8}
$$
All these are actual analytic functions. The freely assigned
$a_k(0)$ is a common amplitude normalization, not an omitted
boundary condition on the original problem.
The equations imply
$$
 b_0=O(T^2),\qquad a_k,b_k\text{ analytic at }T=0.       \tag{P.9}
$$
At each finite order a positive analytic domain remains: the
characteristic angular displacement is at most
$2|T|^{3/2}/3$, and the original domain has a strictly larger
angular margin. The finite Cauchy losses are allocated before
constructing the amplitudes. In iterated characteristic integrals
the radial integrations are time ordered: the sum of all angular
shifts along the nested path is at most the integral of
$2|t|^2$ from $0$ to the final $|t|$, not the number of
iterations times that displacement. Thus every finite order
can be constructed on a common strictly smaller product;
its derivative constants may grow with that order.

## 3. A trial for both original curvature rows, with its true mean source

Let $F_N=U_n(\sum_{k=0}^{N}n^{-k}v_k)$, set $f_N=PF_N$,
and take the exact, rather than symbolically reconstructed, pair
$$
 h_{2,N}=f_N,\qquad
 h_{1,N}=J(D_0-B)f_N .                                \tag{P.10}
$$
In the reflection class $h_{1,N}$ is odd and $h_{2,N}$ even.
The projected second equation is exact by $AJ=1$.
The projected first residual is exactly
$$
                 g_{1,N}=J\mu\mathcal P f_N .         \tag{P.11}
$$
The genuine remaining even equation has the source
$$
 g_{2,N}=
 2bm\langle u h_{1,N}+K(v-m)f_N\rangle .               \tag{P.12}
$$
This is an actual scalar source, constant in the old angle.
It is not replaced by a mean in $X$ or declared absent.
Before taking the reflection combination any extra first mean
residual is kept in the same fashion.

The inverse estimate
$$
 \|Jg\|_{H^{1/3}}
 \le\|Jg\|_{H^1}
 \le(J_0^2+J_1^2)^{1/2}\|g\|_{L^2}                  \tag{P.13}
$$
uses the two actual bounds $\|J\|\le J_0$,
$\|\partial J\|\le J_1$. Thus the scalar residual produces
an ordinary source in precisely the window needed by (P.4)--(P.5);
no radial source derivative is requested.

The old means in (P.12) are bounded as follows. Replace $h_{1,N}$
by its finite amplitude reconstruction and retain the exact
$J$ error. For each retained amplitude the old contour estimate
(I.13) applies, also after multiplication by the fixed coefficients
$u$ and $v$. The exact $J$ error is controlled by (P.13).
A fixed finite low Fourier projection is bounded by the same
contour argument, with the extra fixed factor $e^{4\cdot96h_\phi}$.
Consequently, for every integer $L$ one may choose a sufficiently
long finite construction so that, on $|\rho|\le4/10^6$,
$$
 \|g_N\|_{L^2_rH^{1/3}}
 +\|P_Lh_N\|_{L^2_rH^{4/3}}
 +\|(\Lambda^{1/3}P_Lh_{1,N},P_Lh_{2,N})(r_*)\|
 \le C_L n^{-L},\qquad P_L={\bf1}_{|j|\le96}.          \tag{P.14}
$$
The finite head norm in this formula includes each original low
coordinate, rather than just its mean. A factor $n^q e^{-c_\Pi n}$
is converted into a bound of this type using
$$
 \sup_{x>0}x^{L+q}e^{-c_\Pi x}
       =[(L+q)/(ec_\Pi)]^{L+q}.
$$
Hence $C_L$ is a finite, explicitly defined coefficient-and-remainder
constant. It is not a fitted decay estimate from finitely many columns.

The low projection in (P.14) is an error to be paid when constructing
the high Poisson block. For a supplied nonzero head it remains an
independent forcing port. No inverse for the low Schur system is used.

## 4. Correcting the parametrix with the genuine positive graph

Put $t=(r-r_*-2/10^6)/(1/10^6)$ and choose the radial cutoff
$$
 \chi=1\quad(t\le0),\qquad
 \chi=1-10t^3+15t^4-6t^5\quad(0<t<1),\qquad
 \chi=0\quad(t\ge1).                                  \tag{P.15}
$$
It is $C^2$, with $\|\chi'\|\le15\cdot10^6/8$.
Only one radial derivative is used in the original first-order
equation. Its transition is strictly inside the actual analytic
root piece and the actual fold image. It is also strictly before
the body cut $r_b$.

On the transition the real $T$ is positive and bounded below by
$$
             T_{\min}=(2/10^6)A_-^{2/3}>0,             \tag{P.16}
$$
where $A_-$ is the actual positive fold amplitude gap.
The positive Airy estimate supplies $e^{-c_+ n}$ with
$c_+=2T_{\min}^{3/2}/3$. It applies also to the exact reconstruction
(P.10): its forcing consists of exponentially decaying real Airy
profiles and their derivatives, and the genuine $J$ has a uniform
bound on that same real $r$ circle. Therefore the cutoff residual
$\chi'h_N$ is superalgebraically small in $n$ in the required
ordinary source norm.

Take the full trial $\widetilde h_N=\chi h_N$, and then its high
part $P_H\widetilde h_N$, where $P_H=1-P_L$.
The original operator commutes with multiplication by the radial
scalar $\chi$, except for the explicitly displayed $\chi'$ term.
No old angular primitive changes its integration curve in this step.
Projection to $P_H$ adds the complete high forcing of
$P_L\widetilde h_N$. That forcing is bounded by the actual finite
head-to-high coefficient, and (P.14) pays it.

The trial is zero beyond the cutoff, so its entire regular-end
boundary datum and all later affine jumps are exactly zero.
Let $s_N$ be its actual stable root trace in $Z$ coordinates.
Use the complete positive high inverse to solve for the error
with zero stable root trace and the opposite full high residual.
The corrected positive state $\Psi_N$ satisfies the exact
homogeneous high equation, the true exterior condition, and
the exact stable trace $s_N$, with the whole supplied head fixed
to zero for this Poisson column. All its low-equation residuals
remain available as independent finite-head source rows.

For arbitrary source norms $F_{c,N},F_{b,N}$, (P.4) bounds the
root correction by
$$
 \|Z(\Psi_N-P_Hh_N)(r_*)\|
 \le q_cq_b\sigma(B_cF_{c,N}+B_fF_{b,N}).              \tag{P.17}
$$
Here the constructed residual is entirely inside the collar,
so $F_{b,N}=0$. The body and its regular endpoint still select
the actual graph: they have not been replaced by a local Ai
boundary condition. Its influence occurs through the already
proved factor $q_b\sigma$ in (P.17).

Continue $\Psi_N(r_*)$ into the negative germ by the full original
Cauchy evolution, setting its low root trace to zero as required
by this high Poisson column. The exact difference from $h_N$
has the nonzero low root trace $-P_Lh_N(r_*)$, the true negative
residual $-g_N$, and the high correction (P.17).
By (P.5), for $0\le\rho\le4/10^6$,
$$
\begin{split}
 \|\Psi_N-h_N\|_{L^\infty_\rho L^2}
 \le {41\over10}\bigg[
 &18q_cq_b\sigma(B_cF_{c,N}+B_fF_{b,N})\\
 &+\|(\Lambda^{1/3}P_Lh_{1,N},P_Lh_{2,N})(r_*)\|\\
 &+{3\over1000}\|g_N\|_{L^2_\rho H^{1/3}}\bigg].
\end{split}                                                   \tag{P.18}
$$
The conservative factor 18 is the actual root factor 9 and
the Bessel conversion below 2. This is a true error estimate
between an exact selected solution and an actual finite trial.
It preserves both original curvature rows and the complete mean.

Combining the finite remainders, (P.14)--(P.16) and (P.18) proves:
for each prescribed $L$ there is a finite analytic construction
whose true correction is bounded by a specified finite
$\widetilde C_L n^{-L}$. Arbitrary large orders are obtained by
lengthening that finite construction, not by assuming convergence
of an infinite asymptotic series.

For clarity, the choice of zero supplied head identifies one high
Poisson block. The full solution has the sum of this block and
all original head, mean, ordinary-source and exterior columns.
Nothing in this construction closes or removes those equations.

## 5. The selected columns span a genuine high root relation

Let
$$
 \lambda_*=[\eta(r_*)\sqrt{k(0)}]^{2/3},\quad
 \widetilde p_n=n^{1/3}p_n(r_*),\quad 0<\widetilde p_n<66 .
$$
At $T=0$, $X=\phi$, $T_r=\lambda_*$, and the leading amplitude
is $(1,0)$. Directly from (P.10) and the leading inverse of $A$,
$$
 h_{2,N}(r_*)=\operatorname{Ai}(0)e^{i\epsilon n\phi}
                       +O(n^{-4/3}),
$$
$$
 h_{1,N}(r_*)=
 {\lambda_*\over i\epsilon\eta(r_*)}\,
 n^{-1/3}\operatorname{Ai}'(0)e^{i\epsilon n\phi}
                       +O(n^{-1}).                    \tag{P.19}
$$
These errors are full $L^2$ column estimates, with the finite
analytic remainders just described; they are not only diagonal
Fourier coefficients.

The stable global root trace therefore has leading diagonal entry
$$
 c_n=
 {\operatorname{Ai}(0)
       -[\lambda_*/\eta(r_*)]\operatorname{Ai}'(0)
       \over\sqrt{1+\widetilde p_n}}>0,\qquad
 s_N=c_ne^{i\epsilon n\phi}+O(n^{-2/3}).               \tag{P.20}
$$
The initial values $\operatorname{Ai}(0)>1/3$ and
$\operatorname{Ai}'(0)<0$, together with $1+\widetilde p_n<67$,
give $c_n>1/25$. Thus this is a true elliptic root port.
No value of the global Riccati function $p_n$ is approximated
by the local Airy impedance.

To justify a complete high range, let $E_s$ be the column error
in (P.20). Its norm on a high input tail is at most its
Hilbert--Schmidt norm:
$$
 \|E_s P_{\ge J}\|
 \le C_s\left(\sum_{|j|\ge J}(4|j|)^{-4/3}\right)^{1/2}
                 \longrightarrow0.                  \tag{P.21}
$$
For a sufficiently large finite $J$, the high compression of
the actual root port map is invertible by a genuine Neumann
series around the diagonal $c_n$. The finite complementary
coordinates and all cross maps remain as finite head ports.
This proves that the selected exact columns determine the
high-frequency symbol of the actual regular graph, rather
than merely one formal solution with an unrelated boundary
normalization.

If the tail construction creates a finite complementary stable
trace, subtract the actual positive Poisson columns for that trace.
For any fixed finite complementary set its coefficients are
superalgebraically small by the same contour and finite-inverse
argument as (P.14); the true finite-input Poisson and negative
Cauchy maps have finite norms. This subtraction therefore changes
no high symbol. It does not invert an unproved finite Schur block.

No numerical value of the sufficient $J$ is inferred here.
In particular (P.21) does not certify the entire frequency
window beginning at 97. The already certified positive graph
on $|j|\ge97$ and this asymptotic incoming-coordinate inverse
are distinct assertions.

## 6. Full branch remainders and a strong operator norm formula

Choose the original finite-part cut
$$
 r_c={76285779072683\over320000000000000}.
                                                               \tag{P.22}
$$
Its distance from every root in the certified root interval
is positive and below $4/10^6$. Thus at this cut $T<0$ has a
strict negative gap. The two exact fold identities are
$$
            \Phi_\pm=X\pm{2\over3}(-T)^{3/2}.            \tag{P.23}
$$
The sign of the oscillatory Airy exponential is paired with
$\epsilon$ accordingly. These are the true root-based characteristic
footpoint maps. Their root initial condition distinguishes them from
the waist-based maps called $S_\pm$ in the directed return ledger.
Their genuine composition with those waist maps is retained; the
two initial conditions are not identified.

The real Airy expansions through their first inverse-frequency
coefficient, with their actual remainder estimates, give two
separate branch expansions at this cut. Both original curvature
rows follow by (P.10), using a sufficiently long finite $J$
expansion. Apply the exact radial scalar gauge, the wave matrix,
the old primitive and the strict high normalizers in their
specified order. They are bounded on every fixed Sobolev
window at this strict cut. Retain their exact mean rows.

The removal of the other branch at first order must also be checked.
Let $\Theta_\sigma$ denote the one of the two maps in (P.23) satisfying
$\partial_r\Theta_\sigma=c_\sigma\partial_\phi\Theta_\sigma$; this
choice may exchange the displayed plus/minus labels of (P.23).
For that phase, write its leading density amplitude as
$a_\sigma e_\sigma$ and its other-row coefficient as
$(i\epsilon n)^{-1}t_{\tau\leftarrow\sigma}e_\tau$,
where $\tau\ne\sigma$. At order zero, the actual strict equation
(S.7) gives
$$
 (c_\sigma-c_\tau)\Theta_{\sigma,\phi}
          t_{\tau\leftarrow\sigma}=B_{\tau\sigma}a_\sigma,
 \qquad
 t_{\tau\leftarrow\sigma}
       ={S_{\tau\sigma}a_\sigma\over\Theta_{\sigma,\phi}} .
                                                               \tag{P.23a}
$$
The genuine old primitive on this leading branch is
$(i\epsilon n)^{-1}a_\sigma
e^{i\epsilon n\Theta_\sigma}/\Theta_{\sigma,\phi}$
to first order. Therefore the inverse strict frame $1-SI$
cancels the other-row term in (P.23a) exactly through order
minus one. The remaining off-diagonal order-minus-one generator
is removed by the order-minus-two normalizer already specified
after (S.12); it changes no first coefficient.
Every resulting remainder and every mean or finite-head term
is retained in the same finite calculus.

This cancellation is essential. Before it, a row generally contains
a second canonical graph at order minus one, which cannot be put
into an order-minus-two remainder. After it, each normalized branch
map has only its own phase through first order, as used in (P.24).
The true correction (P.18) is of sufficiently high order that it
does not change (P.23a).

A scalar-height column is of size $n^{-1/6}$ there; its density
column after one old primitive is of size $n^{-7/6}$.
Consequently the density input normalization is $n^{7/6}$.
This factor must be applied also to the true errors in (P.18).
Choosing $L\ge4$ in that estimate gives a normalized error
$O(n^{-17/6})$, which is smaller than $O(n^{-2})$.
No claim of a $1/6$ normalization alone is made for the
primitive density state.

After this normalization, each of the two true branch maps has
$$
 B_\pm=M_{a_\pm}C_{\Phi_\pm}
                 (1+M_{c_\pm}I)+E_\pm,\qquad
 \|E_\pm e_j\|_{L^2}\le C_E(4|j|)^{-2}.               \tag{P.24}
$$
All coefficients are the actual finite transport amplitudes
and endpoint transformations at (P.22).
The nonzero leading amplitudes $a_\pm$ follow from the
exponential characteristic solution of the homogeneous
transport (I.21), together with the nonzero Airy constants.
They and their inverses are smooth on this fixed circle.
The first coefficients $c_\pm$ contain every local,
primitive, cross-wave and endpoint term.

One completely explicit meaning of $C_E$ in (P.24) is the sum of:

* the actual Airy first-neglected-term bound at
  $\min_\phi(-T(r_c,\phi))$;
* the finite amplitude and endpoint-reconstruction remainder
  bounds from the exact rules of Section 2, after multiplication
  by $n^{7/6}$;
* the bound (P.18), multiplied by the actual density trace norm
  at (P.22) and by $n^{7/6}$, then maximized using $L\ge4$.

All those quantities are norms of explicitly defined finite
analytic expressions or the already proved genuine Green maps.
They are finite and can be bounded by the supplied Cauchy
recursions. A useful numerical evaluation of this formula is
a further computation, not a consequence of the word
“analytic.”

The column estimate (P.24) is sufficient to prove the actual
strong remainder, without a falsely diagonal Fourier argument.
With $\Lambda_j=\sqrt{1+16j^2}$,
$$
 \|E_\pm\|_{H^{-4/3}\to L^2}
 \le C_E\left(
     \sum_{|j|\ge J}\Lambda_j^{8/3}(4|j|)^{-4}\right)^{1/2}
 \le {2C_E\over4^{2/3}}
       (J^{-4/3}+3J^{-1/3})^{1/2}.                   \tag{P.25}
$$
The first estimate is exactly the Hilbert--Schmidt estimate
on the weighted input orthonormal basis. For the second,
$\Lambda_j^{8/3}<2(4|j|)^{8/3}$ and the integral comparison
for $\sum_{j\ge J}j^{-4/3}$ suffice.
Every output Fourier coordinate is included.

For sufficiently large $J$, conjugating by the leading
invertible multiplier and circle diffeomorphism makes the
incoming map $1+\mathcal K$, where $\mathcal K$ has one-order
gain plus (P.25). Its high compression is small on both
$L^2$ and $H^{-4/3}$ after increasing this finite $J$.
For the latter norm the high output embedding
$L^2\hookrightarrow H^{-4/3}$ contributes a further
$\Lambda_J^{-4/3}$; smooth multiplication and composition
are bounded on that fixed window.
The inverse is then bounded on both spaces. Retaining all
finite complement maps gives the actual high relation
$$
 B_{\rm out}B_{\rm in}^{-1}
      =R_{\rm principal}(1+M_{b_c}I)+R_{4/3},
 \qquad R_{4/3}:H^{-4/3}\longrightarrow L^2
                    \text{ bounded}.                \tag{P.26}
$$
Products of two one-gain terms have two gains, hence also
belong to the displayed strong class. Formula (P.25), the
actual incoming inverse norms and the actual multiplier/
composition norms give its norm bound. No low inverse,
cutoff-97 threshold or numerical smallness follows without
evaluating those additional constants.

## 7. Finite root coefficient in the strict density convention

Fix the strict normalizer orientation exactly as in (S.9):
$$
 y=(1+SI)y_{\rm new},\qquad
 S=\begin{pmatrix}
 0&-B_+/(2\eta q)\\ B_-/(2\eta q)&0
 \end{pmatrix}.                                      \tag{P.27}
$$
Here $y$ is the old primitive of the radially gauged characteristic
state. The new graph is computed in $y_{\rm new}$, so its first
inverse frame is $1-SI$. All coefficients below use
$(i\epsilon n)^{-1}$ as expansion unit. It must not be replaced
by $n^{-1}$ without its factor $i\epsilon$.

The following calculation identifies the constant term of the actual
first coefficient. It concerns first the exact selected graph whose
parametrix error has been paid by (P.18), rather than a graph assumed
to coincide with a scalar Airy model.

Put $\omega=2(-T)^{3/2}/3$. For a fixed negative $T$, the two
Airy oscillatory coefficients contain the universal first corrections
of degrees $(-T)^{-3/2}$. In the height combination
$a_0f_0+b_0f_1$, the leading two amplitudes are proportional to
$$
             a_0\mp i\sqrt{-T}\,b_0 .                \tag{P.28}
$$
They have a common root value. Since $b_0=O(T^2)$, their difference
is $O((-T)^{5/2})$. The Airy derivative's first correction,
after multiplication by $b_0$, is of size $b_0/T=O(T)$.
It contributes no constant at $T=0$.

At the next finite transport order, $a_1(0,X)$ is common to both
branches and cancels from their ratio. The term
$b_1(0,X)$ is multiplied by $\sqrt{-T}$ and tends to zero.
Thus the height ratio's first coefficient has only half-odd
singular powers and terms tending to zero, with no constant.
The fixed normalization $a_1(0)=0$ in (P.8) is convenient but
not necessary for this cancellation.

One must still reconstruct both original curvature rows.
For either actual phase $\Phi_\sigma$, the leading relation is
$h_1=\sigma q f$, with the branch label chosen consistently.
Let $\ell=-2buv$ be the local order-zero coefficient of $A$.
Solving $Ah_1=(D_0-B)f$ to its next order gives the explicit
$\ell$ contribution
$$
 h_1=\sigma q f\left[
   1-\frac{\ell}{i\epsilon n\,\eta\,\Phi_{\sigma,\phi}}
                \right]
       +\text{the remaining first-amplitude terms}.  \tag{P.29}
$$
Projecting onto its own branch by
$(h_2+\sigma h_1/q)/2$ therefore gives the relative term
$$
        -{\ell\over2\eta\Phi_{\sigma,\phi}}\,
                       (i\epsilon n)^{-1}.          \tag{P.30}
$$
Both branches have the same limit
$-\ell(r_*,\phi)/(2\eta(r_*))$. They cancel in the ratio.
The remaining reconstruction contributions consist of analytic
radial derivatives divided by $q$, and the derivative of the
common $q^{-1/2}$ Airy amplitude. They give respectively
$\rho^{-1/2}$ and $\rho^{-3/2}$ times analytic functions.
The branch differences in (P.28) contribute only $O(\rho)$
after that operation. No hidden finite local term is dropped.
The nonlocal order-minus-one coefficient of $A$, or that of $B$,
enters this reconstruction only at the next inverse-frequency
order; its influence on $a_1,b_1$ has already been retained.

The genuine old primitive has, on a single nonstationary phase,
$$
 I(e^{i\epsilon n\Phi}a)
 ={e^{i\epsilon n\Phi}\over i\epsilon n}
 \left\{{a\over\Phi_\phi}
  -{1\over i\epsilon n\,\Phi_\phi}
                \partial_\phi\left({a\over\Phi_\phi}\right)\right\}
 +\text{exact second-order and mean remainders}.     \tag{P.31}
$$
This is a specialization of (I.8), not an integration at fixed $T$.
Its relative first correction is a logarithmic angular derivative.
At the root the two principal amplitudes have the same angular
normalization and $\Phi_{\sigma,\phi}=1$, so their finite
contributions agree and cancel. The radial wave gauge is common
and also cancels. Exact means remain separate smooth finite-rank
rows.

There is one finite off-diagonal term still to pay. Writing
$B_\sigma=B_{\rm e}-2\sigma bquv$ in (P.27) gives
$$
 S=S_{\rm half}
     +s\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 s=(buv/\eta)|_{r_*}+O(\rho).                         \tag{P.32}
$$
The matrix $S_{\rm half}$ has only half-odd powers of $\rho$.
It cannot be treated as a bounded root frame. It is used first
at each strict cut, where its actual high inverse is defined.

In the root angle $X(0,\phi)=\phi$, the principal selected
reflection is the scalar Airy Maslov constant $r_\epsilon$
with $r_\epsilon^2=-1$, after the already fixed direction
of the wave ratio is chosen. A reversal changes that constant's
sign but not the following conclusion. From the exact graph
formula (W.14), the finite matrix in (P.32) contributes
$$
       (r_\epsilon^2-1)M_s I                         \tag{P.33}
$$
to the graph itself, or $(r_\epsilon-r_\epsilon^{-1})s$
to its relative first coefficient. The actual reflection parity
is $u$ odd and $v$ even, while $b,\eta$ are radial. Hence
$$
               \langle s\rangle=0 .                 \tag{P.34}
$$
Equation (P.33) is the inverse-frame contribution in the
uncombined graph formula, not the complete nonmean first symbol.
It must be combined with the original two-row cross reconstruction.
In particular the uncombined terms with the identity and squared
reflection canonical graphs cancel against that reconstruction
through (P.23a). Until this exact cancellation both contributions
remain in the ledger; neither is put into the strong remainder or
deleted merely because (P.34) holds. The corresponding finite
cross-reconstruction contribution has the opposite zero scalar
mean. The full remaining nonmean coefficient $b_c$ still contains
the actual diagonal branch amplitudes, transported strict symbol
and every endpoint term; it is not identified with the single
summand (P.33).

Finally the two genuine root-based ray maps must be included when
taking this mean. Their difference is $O(\rho^{3/2})$. Because
the leading difference is radial, their angular Jacobian
difference is $O(\rho^{5/2})$. This follows by subtracting their
two scalar flow equations and then differentiating that difference
in the angle; all coefficients have the actual analytic bounds.
The coefficient of the most singular $\rho^{-3/2}$ endpoint
term is radial. Its two Jacobian changes differ by $O(\rho)$.
The next $\rho^{-1/2}$ coefficient, which may depend on the angle,
changes under the two pullbacks by $O(\rho)$ as well. Therefore
neither produces an extra finite mean from the different rays.

Equivalently, the exact density transformation of a first
coefficient is $(a/\Phi')\circ\Phi^{-1}$ and its mean is exactly
$\langle a\rangle$, with the full old mean terms retained.
In the root limit this also applies to (P.33).
A half-density conversion contributes an angular derivative
with zero scalar mean and its separate order-minus-two remainder.

The result of these ordered calculations is
$$
 \langle b_{r_*-\rho}\rangle
      =c_{-3/2}\rho^{-3/2}+c_{-1/2}\rho^{-1/2}
                                     +O(\sqrt\rho),             \tag{P.35}
$$
with zero constant. The coefficients of its two singular powers
are fixed without guessing an Airy-height prefactor: differentiate
the actual strict graph along the two strict density equations.
The directed relative first coefficient accumulates
$\langle\Xi\rangle$ as in the already fixed return word.
Its expansion (S.17) then forces
$$
                  c_{-3/2}=-2g_0/3,\qquad
                  c_{-1/2}=-2g_1 .                  \tag{P.36}
$$
This also explains why the scalar-height $5/48$ coefficient
cannot be equated directly with the strict $\Xi$ subtraction.

Consequently, for this actual repaired-centre given-head high
root relation and this orientation,
$$
 \boxed{\displaystyle
 b_{\rm root}^{\rm fin}
 =\lim_{\rho\downarrow0}
  \left[\langle b_{r_*-\rho}\rangle+
        {2g_0\over3\rho^{3/2}}+{2g_1\over\sqrt\rho}\right]=0 .}
                                                               \tag{P.37}
$$
The large-$n$ first coefficient is extracted at each fixed strict
cut before taking $\rho\downarrow0$. No uniform interchange of
these two limits, and no uniform bound on the singular strict
normalizer as $\rho\to0$, is used. The true parametrix correction
at every such cut is of arbitrarily high inverse-frequency
order by (P.18), so it cannot alter the extracted first coefficient.

## 8. Exact scope left for the complete return

This is an actual local-to-regular high-symbol identification at
$\delta=0$, with all head/mean/ordinary sources retained as ports.
Its first coefficient is that of the original moving Jacobi
operator, not a residual-free physical substitute.
The complete combined nonmean endpoint coefficient, including the
ordered cancellation recorded in (P.23a)--(P.34), the transported
nonmean strict symbol and the full source maps still belong to
the return operator.

The analytic part of the construction applies throughout the
already paid root/fold disk $|\delta|\le10^{-8}$, but (P.17)
uses the actual positive regular graph for $\delta=0$.
Extending (P.37) to the selected nonzero $\delta_*$ requires the
same whole-positive graph and source contract on that family.
A root-only parameter budget does not supply it.

The strong class in (P.26) has been proved with the concrete
bound formula (P.25). The constants $C_E,C_s$, the sufficient
incoming-coordinate cutoff and the relevant multiplier and
composition norms still need actual complete numerical bounds
before this result can pay the high-frequency inverse.
It does not enlarge the certified finite head by declaration,
and it does not solve any newly exposed finite frequency window.
No statement about a true nonlinear branch, the true
$\nu$-response or the final parameter Schur follows yet.

