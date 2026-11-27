# R144 PSC: complete physical phase secant and its tame Hessian

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved.** The actual physical phase residual is the whole moving
waist-chart secant. It has a complete low-norm derivative bound23
and mixed Hessian bound3000, including the actual waist trace and
its mean. At every integer angular order it also has an explicit
tame Hessian with only one high background factor.

This attaches the physical secant left explicit in
[RP.28](R144-supplement-full-off-constraint-principal-return-Hessian.md)
and
[PCT](R144-supplement-all-angular-moving-phase-and-current-normalized-row.md).
It retains all coordinate derivatives at a nonzero phase residual.
A waist trace is a separate normed port; it is not obtained for free
from a radial L2 direction.

## PSC1. Same map, same true waist and domain

Use PCT's actual compact full-tail state and parameter domain, its
fixed target rotation R, and the same degree-one gauge g. In particular
$1/2\le g'\le2$, $G_2=1+\|g-\operatorname{Id}\|_{A^2}\le L$,
$L\ge2$ and $B_3<S=2^{25}$. All RPT constants remain exactly
as defined there.

At the actual waist keep the true second state component v and its
full mean m. Write
$$
 \Theta(x)=x+\theta(x),\qquad
 \theta=Iv/m,\qquad m=\Pi v,\qquad J_w=v/m.                \tag{PSC.1}
$$
This is the original constant convention, not a fitted new angle.
The complete waist domain in
[WH.16--21](R144-supplement-complete-passive-world-height-Hessian-with-independent-ports.md)
gives
$$
 |m|>1,\quad \|v\|_{A^0}<7,\quad
 1/100<J_w<7,\quad \|v'\|_{A^0}<10.                       \tag{PSC.2}
$$
The last bound is the actual compact-background first-angular bound
in RPT.2. Put $W_s=1+\|v\|_{A^s}$, so the genuine same-state waist
satisfies $W_3\le B_3<S$.

For the enlarged port map one can keep this trace as an independent
input, provided it stays in (PSC.2) and $W_3<S$. The actual map is
its restriction to the consistent state trace. In either case a
direction $x=(a,\xi,h_w)$ explicitly pays the full actual waist
increment $h_w$. Define
$$
 \begin{split}
 \widehat X_s(x)&=N_s(a)+\|\xi\|_{H^s}+\|h_w\|_{H^s,\oplus_1},\\
 \widehat E(x)&=N_0(a)+\|\xi\|_2+\|h_w\|_{2,\oplus_1},\\
 \widehat H(x)&=N_0(a)+\|\xi\|_{H^1}+\|h_w\|_{2,\oplus_1},\\
 \widehat Z_n&=B_{n+2}+G_{n+1}+W_{n+1}.
 \end{split}                                                \tag{PSC.3}
$$
Only the second component of $h_w$ enters this chart, but the
displayed component sum is a safe complete port norm.
The mean $\mu_x=\Pi h_{w,2}$ is not zeroed.

Let
$$
 A=P\circ g,\qquad B=g\circ R,\qquad E=A-B.
$$
Their degree-one lifts have the true derivative bounds
$$
 \frac{25}{54}<A'<\frac{54}{25},\qquad
 \frac12\le B'\le2.                                       \tag{PSC.4}
$$
They follow from RPT's $25/27<P'<27/25$ and the original g domain.
In particular every convex lift $B+tE$ is a real diffeomorphism
with derivative above $25/54>2/5$. No intermediate complex
composition or analytic unknown is involved.

The physical gauge is exactly $g_\theta=\Theta\circ g$.
The actual physical residual, expressed in the declared raw state
and raw g coordinates, is
$$
 \begin{split}
 {\cal E}_{\rm phys}
 &=P_\theta\circ g_\theta-g_\theta\circ R\\
 &=\Theta(A)-\Theta(B)
 =E\int_0^1 J_w(B+tE)\,dt .
 \end{split}                                                \tag{PSC.5}
$$
The last integral is a full secant, even when E is not zero.

Consequently, for every $1\le p\le\infty$,
$$
 \frac1{100}\|E\|_{L^p}
 \le\|{\cal E}_{\rm phys}\|_{L^p}
 \le7\|E\|_{L^p}.                                         \tag{PSC.6}
$$
This is a whole pointwise signed residual comparison before taking
norms. Its phase average is not discarded.

## PSC2. Exact full first and second differentials

The waist-coordinate jets are exactly WH.20:
$$
 \begin{split}
 \Theta_x&=Ih_{w,2}/m-Iv\mu_x/m^2,\\
 \Theta_{xy}&=-(Ih_{w,2}\mu_y+Ik_{w,2}\mu_x)/m^2
                       +2Iv\mu_x\mu_y/m^3,\\
 (\Theta_x)'&=h_{w,2}/m-v\mu_x/m^2 .
 \end{split}                                                \tag{PSC.7}
$$
All quantities here are functions of the original angular variable.
The exact total derivatives of A and B are
$$
 A_x=DP[a]\circ g+(P'\circ g)\xi,\qquad B_x=\xi\circ R,
 \qquad A_{xy}=D^2E[x,y],\quad B_{xy}=0,                   \tag{PSC.8}
$$
where the return uses a and b and is independent of the separately
declared waist port. On the actual consistent trace restriction,
these are the same state directions, with the trace norm explicitly
included.

Differentiating the two full compositions in (PSC.5) gives
$$
 D{\cal E}_{\rm phys}[x]
 =\Theta_x(A)-\Theta_x(B)
             +\Theta'(A)A_x-\Theta'(B)B_x,                \tag{PSC.9}
$$
and the full symmetric Hessian is
$$
 \begin{split}
 D^2{\cal E}_{\rm phys}[x,y]={}&
 \Theta_{xy}(A)-\Theta_{xy}(B)\\
 &+\Theta_x'(A)A_y+\Theta_y'(A)A_x\\
 &-\Theta_x'(B)B_y-\Theta_y'(B)B_x\\
 &+\Theta''(A)A_xA_y-\Theta''(B)B_xB_y
                         +\Theta'(A)A_{xy}.
 \end{split}                                                \tag{PSC.10}
$$
There are nine actual terms. No nonzero residual has been replaced
by a zero, and neither evaluation point has been reset. These are
derivatives in the state coordinates of PSC1. Holding $g_\theta$
independently fixed would be a different coordinate calculation,
requiring the full derivative of $\Theta\circ g$; it is not silently
substituted here.

## PSC3. Complete low-norm derivative and Hessian bounds

Use the completed WH inequalities
$$
 \|\Theta_x\|_\infty\le\frac94 e_x,\qquad
 \|\Theta_{xy}\|_\infty\le\frac92 e_xe_y,\qquad
 \|\Theta_x'\|_2\le8e_x,\qquad
 e_x=\|h_w\|_{2,\oplus_1}.                                \tag{PSC.11}
$$
They include the mean variations in (PSC.7).
Also $|\Theta'|<7$ and $|\Theta''|<10$ by (PSC.2).

For the state and gauge parts alone put
$E_x=N_0(a)+\|\xi\|_2$ and
$H_x=N_0(a)+\|\xi\|_{H^1}$.
RP's full return estimate and the true fourfold embedding
$\|\xi\|_\infty\le(11/10)\|\xi\|_{H^1}$ give
$$
 \begin{split}
 \|A_x\|_2&\le(54/25)E_x,&
 \|A_x\|_\infty&\le(54/25)H_x,\\
 \|B_x\|_2&\le E_x,&
 \|B_x\|_\infty&\le(11/10)H_x,\\
 \|A_{xy}\|_2&\le400(H_xE_y+H_yE_x).
 \end{split}                                                \tag{PSC.12}
$$
The last line is precisely RP's complete raw-phase Hessian, not
an inferred same-order bound on a derivative of an arbitrary
L2 function.

Equations (PSC.9),(PSC.11)--12 immediately imply
$$
 \|D{\cal E}_{\rm phys}[x]\|_2
 \le7(54/25+1)E_x+(9/2)e_x
 <23\,\widehat E(x).                                     \tag{PSC.13}
$$

Here is the complete low-Hessian ledger. The first line of
(PSC.10) costs at most $9e_xe_y$.
Change of variables in either A or B costs less than3/2 on L2,
because $54/25<(3/2)^2$. Thus its four mixed chart terms cost
at most
$$
 12(54/25+11/10)(e_xH_y+e_yH_x)
       =39.12(e_xH_y+e_yH_x).                            \tag{PSC.14}
$$
The two spatial second-derivative products cost at most
$$
 5\{(54/25)^2+11/10\}(H_xE_y+H_yE_x)
       =28.828(H_xE_y+H_yE_x).                           \tag{PSC.15}
$$
This averages the two complete L-infinity times L2 product
bounds, so both directions remain symmetric.
The last term costs at most $2800(H_xE_y+H_yE_x)$.

Using $\widehat H=H+e$ and $\widehat E=E+e$, all terms are
therefore paid by
$$
 \boxed{\quad
 \|D^2{\cal E}_{\rm phys}[x,y]\|_2
 \le3000\{\widehat H(x)\widehat E(y)
                   +\widehat H(y)\widehat E(x)\}.
 \quad}                                                  \tag{PSC.16}
$$
Indeed $2800+28.828+39.12+9/2=2872.448<3000$.
There is no angular derivative charge on the waist directions
in this particular low-norm result. Their actual L2 traces
still have to be provided; a radial L2 state norm alone
does not supply them.

## PSC4. All-angular real composition at the two actual lifts

We spell out the higher-order constant so that the passage
from (PSC.16) to a tame estimate has no missing composition
assumption. Let cn and Tn be the explicit PCT constants.
Choose the fixed low derivative budget
$$
 L_A=2+2c_1 L(1+L)R_2S.                                  \tag{PSC.17}
$$
The complete Wiener norm of A' is at most $L_A$:
$$
 \|A'\|_{A^0}
 \le \|g'\|_{A^0}\,2\|P'\circ g\|_{H^1}
 \le2L c_1(1+L)R_2S.
$$
For B', the corresponding bound is just L. Hence $L_A$ pays
both actual composition maps without a high gauge norm.
Notice that it uses the H1 norm of P', not an unproved
H3 budget for g.

The proof of PCT.5--7 applies to either lift C=A or C=B,
with change-of-variables factor below2, and gives
$$
 \|f\circ C\|_{H^n}
 \le\bar c_n\{\|f\|_{H^n}
       +(1+\|C-\operatorname{Id}\|_{A^{\max(n,1)}})
                                     \|f\|_{H^1}\},
 \quad
 \bar c_n=2^{n+5}(n+1)!\,L_A^{n+1}.                       \tag{PSC.18}
$$
At n=0 or1 the actual derivative A' budget already gives
the sharper direct low-order composition estimate; the
displayed enlargement is harmless.

For higher orders the complete Fourier embedding and PCT.7
applied to $P-\operatorname{Id}$ show
$$
 1+\|A-\operatorname{Id}\|_{A^n}
   +\|B-\operatorname{Id}\|_{A^n}
 \le T_{n+1}^3(B_{n+1}+G_{n+1}),\quad n\ge1.              \tag{PSC.19}
$$
For clarity, $A-\operatorname{Id}
=u+(P-\operatorname{Id})\circ g$,
$B-\operatorname{Id}=\Omega_\star+u\circ R$, and
$A^n\le2^{n+1}H^{n+1}$.
The actual high H(n+1) composition requires only
$B_{n+1},G_{n+1}$ and the fixed low $R_1S$.
All fixed multipliers are smaller than the stated T power.
This is why two unknown high background factors do not appear.

The waist jets (PSC.7), and their first spatial derivatives,
are elementary products with scalar m reciprocals. For example
$$
 \|\Theta_x'\|_{H^n}
 \le \|h_{w,2}\|_{H^n}+W_n\|h_{w,2}\|_2,
$$
while the second state jet is bounded by a fixed factor times
$$
 \|h_w\|_{H^n}\|k_w\|_2+\|h_w\|_2\|k_w\|_{H^n}
                        +W_n\|h_w\|_2\|k_w\|_2.         \tag{PSC.20}
$$
The primitive has norm at most1 and the actual mean has norm1.
The background $\Theta''$ uses at most $W_{n+1}$.
Their low H1 norms use at most $W_2<S$ and low H1 waist
directions. Thus (PSC.18)--20 have a single unknown high
factor $B_{n+2}+G_{n+1}+W_{n+1}$.

## PSC5. Explicit all-angular tame map and Hessian

Define
$$
 \begin{split}
 \bar T_n&=2^{8(n+10)}((n+10)!)^2
       (1+L_A)^{2n+20}(1+S)(1+T_{n+1})^4,\\
 \bar C_n&=\bar T_n^{16}.
 \end{split}                                                \tag{PSC.21}
$$
These constants depend only on the fixed low domains, the
explicit completed RPT constants and the declared gauge L.
No unknown higher Bs, Gs or Ws enters them.

Each full composed waist packet in (PSC.10) has high and
low coefficient at most $\bar T_n^3$, by PSC4.
The actual A/B direction packets follow from the literal
PCT.13 formulas: the high return-Hessian direction uses
at most n+3, its low H1 version at most4. For A_x and B_x,
only the displayed direction's own order is needed.
Their coefficients are also below $\bar T_n^3$.
Apply the complete Fourier product inequality PCT.9 with
at most three factors, assigning its high norm to exactly
one factor at a time.

There are at most nine products, with at most three such
packets each. The coefficient ledger is bounded by
$\bar T_n^{9+1+1}=\bar T_n^{11}<\bar C_n$:
three packets, one Fourier product factor, and one complete
term-sum factor. This also covers the value and first
derivative, whose expressions are shorter. For the value use the
periodic expression $E+\theta(A)-\theta(B)$, never the Hn norm
of a nonperiodic degree-one lift.
In a low product slot use the low bound before multiplying;
do not multiply independent high bounds.

The actual all-angular conclusions, for every integer $n\ge0$,
are therefore
$$
 \|{\cal E}_{\rm phys}\|_{H^n}\le\bar C_n\widehat Z_n,
                                                               \tag{PSC.22}
$$
$$
 \|D{\cal E}_{\rm phys}[x]\|_{H^n}
 \le\bar C_n\{\widehat X_{n+4}(x)
                       +\widehat Z_n\widehat X_4(x)\},
                                                               \tag{PSC.23}
$$
$$
 \boxed{\begin{split}
 \|D^2{\cal E}_{\rm phys}[x,y]\|_{H^n}\le\bar C_n\{&
  \widehat X_{n+4}(x)\widehat X_4(y)
 +\widehat X_4(x)\widehat X_{n+4}(y)\\
 &+\widehat Z_n\widehat X_4(x)\widehat X_4(y)\}.
 \end{split}}                                             \tag{PSC.24}
$$
These include all original means and both independent true
state and waist directions. On the actual consistent trace
restriction, $W_s\le B_s$, but the direction's waist norm
must still be paid by a genuine trace theorem or port.

For an admitted real line segment, the low remainder is
$$
 \|{\cal E}_{\rm phys}(q+z)-{\cal E}_{\rm phys}(q)
                -D{\cal E}_{\rm phys}(q)z\|_2
 \le3000\,\widehat H(z)\widehat E(z).                     \tag{PSC.25}
$$
The all-angular remainder and derivative difference follow
by integrating (PSC.24) with one common L and the whole
segment supremum of $\widehat Z_n$.
Real positive angular smoothing and the RPT strong-state
approximation give density exactly as in PCT. Means,
degree-one lifts, original interfaces and the independent
waist port are retained.

The complete physical secant and its first two derivatives
are now paid on this stated domain. This does not supply
the full regular inverse, the true finite or parameter
Schur matrix, the independent geometric matching, a
summable augmented iteration, or the final fixed-metric
embedded family. Those remain the topic's actual
completion obligations.

The companion calculation only combines completed low
bounds and the new exact coefficient ledger. It restores
no old carrier and evaluates no old phase or norm target.

