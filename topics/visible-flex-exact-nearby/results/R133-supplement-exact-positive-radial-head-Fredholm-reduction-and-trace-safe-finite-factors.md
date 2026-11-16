# R133 supplement: exact positive radial-head Fredholm reduction and trace-safe finite factors

The complete positive radial head can be reduced to a second-kind compact equation, with its actual endpoint and exterior equations retained. This is a new elimination of a function-valued block: it does not identify a radial function with its finite angular fiber. The resulting head kernel and cokernel are finite but are not proved to vanish. A radial output projection gives a separate, explicit tail test which does not contain the whole negative-side waist-error constant.

The proof uses the already completed full-delta positive given-head graph in its original negative-one window. It is applied here at the selected member $\delta_*$. It does not extend the selected waist principal conjugacy to all parameters, extend a positive-interval estimate to the negative interval, or replace a physical boundary chart by a chosen coordinate image. No scientific quantity is evaluated, no old successful target is repeated, and no finite determinant is asserted.

## WHR1. The original head is a Hilbert-space function

Let $I_+=[r_*,R]$, $R=25/8$, be the true positive interval of the fixed intrinsic metric. Use the original physical angle of period $\pi/2$, its normalized $L^2$ norm, and the physical reflection
$$
 Rh_1=-h_1,\qquad Rh_2=h_2.
 \tag{WHR.1}
$$
Let $Q_L$ project the raw two-component state onto $|j|\le96$, and put $P_H=1-Q_L$. The reflected real head fiber is
$$
 E_L=Q_L\{(h_1,h_2):\text{(WHR.1)}\},\qquad
 \dim_{\mathbb R}E_L=96+97=193.
 \tag{WHR.2}
$$
Its complexification has complex dimension 193, not two independent copies of the physical problem. The complete head and high state are
$$
 a=Q_Lh,\qquad v=P_Hh,\qquad
 \mathscr H=L^2(I_+;E_L),\quad
 \mathscr V=L^2(I_+;P_HH^{-1}_\phi).
 \tag{WHR.3}
$$
The measure is ordinary $dr$. The angular norm on $E_L$ is its fixed inherited normalized $L^2$ norm, not an unrecorded sum of coordinate norms or a radius-dependent graph weight. Any later variable-weight chart requires its complete norm conversions before the radial projection estimate is used.

The space $\mathscr H$ is infinite-dimensional. The 193 number describes only its angular fiber. The physical even mean is one component of $a(r)$; the two density mean entries, when used, keep WPM's exact injection and their reflected relation. No mean matching or amplitude equation is removed by (WHR.2).

The completed positive graph of run 43627228225 admits ordinary sources in $L^2_rH^{-2/3}_\phi$, gives the complete raw high state in $\mathscr V$, and retains seven independent source/affine input types and their actual boundary and mean columns. These input types are not seven scalar dimensions. Its full source and output domains, physical root conversion factors, actual regular graph and both jump signs remain those of the original theorem.

The statements below first concern the original stable root port of that graph. A later use of a WGB graph variable must prove its complete ordered map into this port or prove the needed finite-output pairing directly. A rough waist trace theorem alone is not a raw positive-bulk theorem.

## WHR2. The complete low equation and the actual coupling shell

Moving N.3--9, before scalar mean elimination, gives the exact raw operator
$$
 \begin{split}
 h_r={}&\mathcal A(r)h+g,\\
 \mathcal A={}&M_d\partial_\phi\,Id_2
  +\eta\begin{pmatrix}0&-K\\1&0\end{pmatrix}\partial_\phi
  +\begin{pmatrix}M_{L_{11}}&K M_\ell\\M_\ell&M_{L_{22}}\end{pmatrix}\\
 &-2\beta
       \binom{M_{u_\phi}}{M_{v_\phi}}\,
          I\,\begin{pmatrix}M_u&K M_v\end{pmatrix}
  +\gamma\binom{K v_\phi}{-u_\phi}\Pi_2 ,
 \end{split}
 \tag{WHR.4}
$$
where
$$
 \begin{gathered}
 \Pi_2(h_1,h_2)=\Pi h_2,\quad I=\partial_\phi^{-1}(1-\Pi),\\
 d=-\beta I(u^2+Kv^2),\quad
 \eta=-\gamma\Pi v,\quad \ell=-2\beta uv,\\
 L_{11}=-\beta(1+3u^2+Kv^2),\qquad
 L_{22}=\beta(1-u^2-3Kv^2).
 \end{gathered}
 \tag{WHR.5}
$$
All scalar radial coefficients and both mean-rank entries are present. This is linearization at the fixed approximate background; it does not assume that background solves the nonlinear PDE.

Write
$$
 A_L=Q_L\mathcal A Q_L,\qquad
 B_{LH}=Q_L\mathcal A P_H,\qquad
 B_{HL}=P_H\mathcal A Q_L .
 \tag{WHR.6}
$$
The actual background has angular band 96, while $d$ and the local reaction have band at most 192. The primitive in (WHR.4) is the original ordered pair of convolutions with the zero intermediate frequency annihilated by $I$. Its total shift is at most 192. The radial principal matrix times $\partial_\phi$ commutes with $Q_L$ and has no off-diagonal cutoff block. The final rank in (WHR.4) is entirely a head term.

Consequently
$$
 B_{LH}=B_{LH}P_{\{97\le |j|\le288\}},\qquad
 B_{HL}=P_{\{97\le |j|\le288\}}B_{HL}.
 \tag{WHR.7}
$$
These are support identities for the coupling, not a band limit on the unknown state $v$. In particular the already proved negative-one transfer N.7 gives
$$
 \|B_{LH}v\|_{L^2_rE_L}
 \le 1153\,A_{LH}\|v\|_{\mathscr V}
 \tag{WHR.8}
$$
whenever $A_{LH}$ is the complete original unweighted high-to-low bound on the same interval. The factor uses the true input shell, whose largest physical frequency is $4\cdot288=1152$. It is not applied to the infinite high state before the shell restriction.

Likewise $B_{HL}:\mathscr H\to L^2_rH^{-2/3}_\phi$ is bounded, with the original complete low-to-high bound remaining a valid larger bound. All full-density, primitive and physical mean contributions of (WHR.4) stay in these operators; none is replaced by the scalar mean of a selected waist coefficient.

The finite matrix $A_L(r)$ is bounded and measurable on the closed positive interval, with the original one-sided coefficients at genuine seams. For example, a conservative symbolic bound follows from (WHR.4):
$$
 \begin{split}
 \|A_L\|\le{}&
 384\{\|d\|_\infty+|\eta|\max(1,|K|)\}\\
 &+\|L_{11}\|_\infty+\|L_{22}\|_\infty
                +(1+|K|)\|\ell\|_\infty\\
 &+\frac{2|\beta|}{4}
    (\|u_\phi\|_\infty+\|v_\phi\|_\infty)
    (\|u\|_\infty+|K|\|v\|_\infty)\\
 &+|\gamma|(|K|\|v_\phi\|_2+\|u_\phi\|_2).
 \end{split}
 \tag{WHR.9}
$$
Here the single $1/4$ is the actual $L^2$ norm of the meanzero primitive on the period-$\pi/2$ circle. It is not an $L^\infty$ primitive estimate. This finite expression is an analytic bound, not a new evaluated scalar.

## WHR3. Separate the original boundary ports from a raw head trace

The completed given-head high inverse is linear. Keep every original non-head input, including its true source norm, outer function, mean, height and jump port. Splitting only the head-dependent body source gives
$$
 v=\mathcal P_a a+\mathcal P_y y+v_f .
 \tag{WHR.10}
$$
Here $\mathcal P_a:\mathscr H\to\mathscr V$ is the original high inverse applied to the complete $B_{HL}a$ ordinary source, with its stable root and all independent boundary, mean and jump inputs zero. The vector $y$ denotes the remaining unknown coordinates in their actual spaces; prescribed independent functional inputs may instead be kept in $v_f$. An unknown function in $y$ is still an unknown function.

In particular the original outer low chart port, such as the $y_L$ in negative-one N.12, is not renamed as $Q_Lh(R)$. Denote the original finite boundary/chart ports collectively by $b$. They are components of $y$ and act through their already admitted complete high columns. A raw head trace $a_R$ is a separate auxiliary coordinate. The original chart equations connecting $b$, $a_R$, the true high endpoint, outer height and mean are all retained. Only in a realization already proved to use a raw head trace is its matching equation simply $b=a_R$.

Equation (WHR.10) does not take an endpoint trace of an arbitrary $a\in\mathscr H$. Its head input is an ordinary body source. Actual endpoint trace maps of the high solution are the separately qualified original graph outputs; no trace is inferred from $\mathscr V$ alone.

Define
$$
 K=B_{LH}\mathcal P_a:\mathscr H\to\mathscr H,\qquad
 F_y=B_{LH}\mathcal P_y+G_y,\qquad
 f_L=B_{LH}v_f+g_{L,f},
 \tag{WHR.11}
$$
where $G_y$ and $g_{L,f}$ retain the original low ordinary source columns, including the complete metric derivative if it is an unknown scalar direction. Then the low equation is exactly
$$
 a'=A_La+Ka+F_y y+f_L .
 \tag{WHR.12}
$$
Neither $K$ nor $\mathcal P_a$ is asserted to be causal in $r$. The positive high inverse incorporates the true regular endpoint and can depend on head data at later radii.

For example, if $C_c,C_b$ are the already saved whole-positive raw-state columns for collar and body ordinary sources and $A_c,A_b$ bound the corresponding restrictions of $B_{HL}$, then
$$
 \|\mathcal P_a\|\le C_cA_c+C_bA_b,\qquad
 \|K\|\le 1153 A_{LH}(C_cA_c+C_bA_b).
 \tag{WHR.13}
$$
Every factor has its original input/output norm. The boundary columns are not included in $C_cA_c+C_bA_b$ by replacing their independent input $b$ with a non-existent $L^2$ endpoint trace.

## WHR4. The true IVP and its bounded endpoint rows

Let $\ell_+=R-r_*$ and let $E_L(r,t)$ be the finite-dimensional fundamental matrix of
$$
 \partial_r E_L(r,t)=A_L(r)E_L(r,t),\qquad E_L(t,t)=Id .
$$
It exists across the original coefficient seams in the ordinary absolutely continuous sense. This is the actual finite head generator at the present member, not the old centre's two-boundary Green operator.

The zero-initial-value operator is
$$
 (Vq)(r)=\int_{r_*}^r E_L(r,t)q(t)\,dt,\qquad
 (E_*c)(r)=E_L(r,r_*)c.
 \tag{WHR.14}
$$
It is the same operator on both sides of its equation:
$$
 (\partial_r-A_L)V=Id,\qquad
 V(\partial_r-A_L)a=a-E_*a(r_*).
 \tag{WHR.15}
$$
The second formula is asserted on the actual $H^1$ domain. Existence of this IVP uses no boundary determinant.

If $A_\infty=\operatorname*{ess\,sup}\|A_L\|$ and
$A_1=\int_{I_+}\|A_L(r)\|\,dr$, then
$$
 \begin{split}
 \|V\|_{\mathscr H\to\mathscr H}&\le C_V:=\ell_+e^{A_1},\\
 \|\partial_rV\|_{\mathscr H\to\mathscr H}
       &\le C_D:=1+A_\infty C_V,\\
 \|V_R\|_{\mathscr H\to E_L}
       &\le C_R:=\sqrt{\ell_+}\,e^{A_1},\qquad
 V_Rq=\int_{r_*}^R E_L(R,t)q(t)\,dt .
 \end{split}
 \tag{WHR.16}
$$
These follow from the complete fundamental-matrix bound and ordinary Cauchy--Schwarz. In particular $V:\mathscr H\to H^1(I_+;E_L)$ is bounded.

All actual prescribed low state jumps can be retained as
$$
 (J_L\mathbf j)(r)
   =\sum_{r_*<r_\alpha\le r}E_L(r,r_\alpha)j_{L,\alpha},
 \qquad
 J_{L,R}\mathbf j
   =\sum_\alpha E_L(R,r_\alpha)j_{L,\alpha}.
 \tag{WHR.17}
$$
The exact signs are those of the original convention
$[a]_{r_\alpha}=j_{L,\alpha}$. There is no radial-length factor on an impulse. No jump is invented from a mere change of graph coordinates. A source-dependent jump column stays in its original independent port. If an actual transmission relation contains an unknown endpoint coordinate, that coordinate and its matching row must first be exposed, just as $b$ was in WHR3.

Introduce the actual initial head $a_*$ as an auxiliary finite coordinate. Equations (WHR.12) and (WHR.17) are equivalent to
$$
 (Id-T)a=E_*a_*+V(F_y y+f_L)+J_L\mathbf j,
 \qquad T=VK.
 \tag{WHR.18}
$$
The initial coordinate is not newly granted free physical data: all original root and matching equations still act on it.

Crucially, the raw endpoint is represented by the bounded row
$$
 a_R=E_L(R,r_*)a_*+V_R(Ka+F_y y+f_L)
                          +J_{L,R}\mathbf j .
 \tag{WHR.19}
$$
Every operator in (WHR.19) is bounded on the displayed $L^2$ head space. On solutions of (WHR.18), $a-J_L\mathbf j\in H^1$, and (WHR.19) is its actual right trace with the prescribed jumps. It is not the extension of a fictitious trace functional on all of $\mathscr H$.

## WHR5. The positive head self-block is Fredholm of index zero

Because $E_L$ has finite dimension, the embedding
$H^1(I_+;E_L)\hookrightarrow\mathscr H$ is compact. By WHR3--4,
$$
 T:\mathscr H\xrightarrow{K}\mathscr H
             \xrightarrow{V}H^1(I_+;E_L)
             \hookrightarrow\mathscr H
 \quad\hbox{is compact}.
 \tag{WHR.20}
$$
Therefore
$$
 F:=Id-T
 \quad\hbox{is Fredholm of index zero on }\mathscr H .
 \tag{WHR.21}
$$
This index refers to the self-block with the initial and other independent ports fixed. It is not the index of the whole boundary problem when the 193 initial coordinates and their actual matching rows are appended.

Its kernel functions are in $H^1$, since $a=Ta$ for a kernel element. Its cokernel is finite-dimensional. Write
$$
 m_H=\dim\ker F=\dim\ker F^*<\infty .
 \tag{WHR.22}
$$
No claim $m_H=0$ follows. This $m_H$ is unrelated to the already vanishing FC completion of the natural stable root map.

The noncausal feedback is essential here. For a purely illustrative scalar interval $[0,1]$, take $A_L=0$ and $Ka=2\int_0^1a(t)\,dt$. Then
$Ta(r)=2r\int_0^1a(t)\,dt$ has the eigenfunction $a(r)=r$ with eigenvalue one. Thus a zero-initial IVP on the left does not make $Id-VK$ invertible when the feedback itself is nonlocal. This example evaluates no quantity of the present scientific problem.

For completeness, a trace-safe finite completion always exists. Choose orthonormal bases encoded by
$$
 U_0:\mathbb R^{m_H}\to\ker F,\qquad
 W_0:\mathbb R^{m_H}\to\ker F^*.
$$
By density of $H^1$ in $\mathscr H$, choose a column map
$U_+:\mathbb R^{m_H}\to H^1(I_+;E_L)$ satisfying
$W_0^*U_+=Id$. Then
$$
 \mathcal F=
 \begin{pmatrix}F&U_+\\ U_0^*&0\end{pmatrix}
 :\mathscr H\oplus\mathbb R^{m_H}
       \longrightarrow\mathscr H\oplus\mathbb R^{m_H}
 \quad\hbox{is an isomorphism}.
 \tag{WHR.23}
$$
Indeed the first row determines the auxiliary variable as $W_0^*r$; after subtracting $U_+W_0^*r$, the remaining datum lies in $\operatorname{ran}F$, where $F$ is invertible on $(\ker F)^\perp$. The second row fixes the kernel coordinate.

Choosing $U_+$ in $H^1$ makes the auxiliary solution $H^1$ whenever the right side is $H^1$, before imposing zero auxiliary residual. Alternatively one may keep (WHR.19) throughout and never take a naked trace of an auxiliary $L^2$ solution. With prescribed jumps, the same assertion holds after subtracting their complete particular solution.

Formula (WHR.23) is qualitative: neither its dimension, its columns, its norm nor its finite inverse is evaluated. It gives an exact finite obstruction, not permission to set the original compatibility equations to zero.

## WHR6. Eliminate the head while preserving every remaining cross map

Collect all other actual unknowns into a vector $y$ in their declared product space. This may include a WGB high graph variable only on its qualified domain, the true initial head, the original chart ports, independent external functions, actual physical finite columns, retained WCF/WFR variables and the metric scalar. Absorb the initial and jump columns into a bounded map $\mathscr B$ and datum $f$. The system has the form
$$
 Fa=\mathscr B y+f,\qquad
 \mathscr C a+\mathscr D y=g .
 \tag{WHR.24}
$$
Every endpoint row of $\mathscr C$ is first written as (WHR.19), together with its direct terms in $\mathscr D$ and $g$. The symbol $\mathscr C$ is not defined by taking $a(R)$ on $L^2$.

Let $G$ be the inverse of $F:(\ker F)^\perp\to\operatorname{ran}F$, extended by zero on the orthogonal cokernel. The first equation has precisely the solutions
$$
 W_0^*(\mathscr B y+f)=0,\qquad
 a=G(\mathscr B y+f)+U_0 c,\quad c\in\mathbb R^{m_H}.
 \tag{WHR.25}
$$
Substitution gives the exact reduced system
$$
 \boxed{\;
 \begin{pmatrix}
  \mathscr D+\mathscr C G\mathscr B&\mathscr C U_0\\
  W_0^*\mathscr B&0
 \end{pmatrix}
 \binom y c
 =
 \binom{g-\mathscr C Gf}{-W_0^*f}.
 \;}
 \tag{WHR.26}
$$
Both directions follow from (WHR.25), so no inverse of the remaining matrix is presumed. In particular the cokernel right side has its displayed negative sign.

The map $\mathscr C G\mathscr B$ contains all high/head, finite/head, mean/head, external/head and parameter/head feedback. The columns $\mathscr C U_0$ are actual propagated head-kernel columns. They are not reference columns, not the missing 96 physical columns of WGB, and not root impulse columns of WFR.

Unknown functional coordinates inside $y$ stay infinite-dimensional. Their appearance in a displayed block matrix does not turn them into a finite border. If a particular independent source is prescribed, it contributes to the right side with its complete original units; that does not identify it with another prescribed input.

## WHR7. A concrete radial tail test and an exact finite factor

There is a quantitative alternative to discovering the unknown kernel first. Partition $I_+$ into $N$ cells of maximum length $h_{\rm mesh}$. Let $\Pi_N$ be the ordinary radial $L^2$ orthogonal projection onto cellwise-constant $E_L$-valued functions. Its isometric embedding is
$$
 E_N:\mathbb R^{193N}\longrightarrow\mathscr H,\qquad
 E_N(c_{i,k})=\sum_{i,k}|I_i|^{-1/2}c_{i,k}\,
                                     {\bf1}_{I_i}e_k ,
 \quad \Pi_N=E_NE_N^* .
 \tag{WHR.27}
$$
The $e_k$ use the inherited orthonormal reflected angular basis.

On each cell the vector-valued meanzero Poincare inequality gives
$$
 \|(Id-\Pi_N)w\|_{\mathscr H}
       \le {h_{\rm mesh}\over\pi}\|w'\|_{\mathscr H},
 \qquad w\in H^1(I_+;E_L).
$$
Hence, with any complete $C_K\ge\|K\|$,
$$
 \varepsilon_N:=
 {h_{\rm mesh}\over\pi}\,C_D C_K,\qquad
 \|(Id-\Pi_N)T\|\le\varepsilon_N .
 \tag{WHR.28}
$$
This is an output radial tail estimate. It does not truncate the input dependence of $K$ or $T$ and uses neither output orthogonality of different physical waves nor a radial derivative of an ordinary source. Coefficient seams need not be differentiable for (WHR.28), since $Vq$ is globally $H^1$ for $q\in L^2$. Prescribed impulses occur in the right side of (WHR.18), not inside the homogeneous operator $T$.

If the new strict gate
$$
                         \varepsilon_N<1
 \tag{WHR.29}
$$
has actually been certified, put
$$
 R_N=Id-(Id-\Pi_N)T,\qquad
 V_N=E_N^*T .
$$
Then
$$
 \|R_N^{-1}\|\le(1-\varepsilon_N)^{-1},\qquad
 F=R_N-E_NV_N .
 \tag{WHR.30}
$$
The finite rows $V_N$ act on the entire $\mathscr H$. They are not $E_N^*$ and are not supported on a finite input mesh. Their exact expression is
$$
 (V_Na)_{i,k}
 =|I_i|^{-1/2}
   \int_{I_i}\left\langle e_k,
       \int_{r_*}^r E_L(r,t)\,
                  B_{LH}(t)(\mathcal P_a a)(t)\,dt
                     \right\rangle\,dr .
 \tag{WHR.31}
$$
All ordered high/low feedback and the complete positive inverse remain inside this functional.

Introduce $z_N=V_Na$. Then the complete system (WHR.24) is equivalent, under (WHR.29), to
$$
 a=R_N^{-1}(\mathscr B y+f+E_Nz_N)
$$
and
$$
 \boxed{\;
 \begin{pmatrix}
  \mathscr D+\mathscr C R_N^{-1}\mathscr B&
                  \mathscr C R_N^{-1}E_N\\
  -V_N R_N^{-1}\mathscr B&
                  Id-V_N R_N^{-1}E_N
 \end{pmatrix}
 \binom y{z_N}
 =
 \binom{g-\mathscr C R_N^{-1}f}{V_N R_N^{-1}f}.
 \;}
 \tag{WHR.32}
$$
There is no inverse assumption on $Id-V_NR_N^{-1}E_N$ or on the full displayed system. Its second right side is positive because that row is $z_N-V_Na=0$. Redundant auxiliary coordinates are allowed.

Equations (WHR.28)--(WHR.32) give a concrete route to a certified bounded elimination of the infinite head remainder while retaining its entire finite feedback. The tail test depends on the positive head equation and its given-head graph, not on the large complete negative waist source or endpoint bound. It may still be numerically too conservative; existence of some finite mesh does not certify a feasible matrix, any of its entries, or a determinant.

## WHR8. Interaction with the true physical border

The following objects remain distinct in (WHR.24)--(WHR.32).

| Object | Exact status after the head reduction |
|---|---|
| WGB high graph coordinate and $\Theta u=0$ | The same 96 constraints remain; no head-kernel or radial-cell column satisfies or replaces them by definition |
| Missing genuine 96 physical columns | Still require their actual Poisson realization and all output rows; $E_N$ and $U_0$ are not such columns |
| WFR root trace factor | Its actual column and full dual row remain in the retained auxiliary system, including every new head cross term |
| WCF finite $F_J$, primitive ranks, $\rho_i$ and $\ell_2$ | Their exact factors remain; their high outputs are not set to zero or projected away |
| The two stored density means | Keep WPM's actual reflection relation, both entries wherever used, and the independent physical even-mean/outer/amplitude equations |
| True metric scalar $\varkappa$ | Keep the full body source, normalization derivative, endpoint and matching rows; its finite Schur value is not inferred from (WHR.21) |
| Independent outer height, reference or source function | Retains its original infinite domain unless it was prescribed or separately eliminated by a proved bounded identity |
| Negative-side radial head | Not covered by this positive-interval proof; its own full realization, propagation, interfaces and matching remain |
| A rough WGB input | Requires the complete ordered positive-port or finite-pairing qualification; a strong waist error does not supply it |
| Old finite193 two-boundary Green | Retains its original centre and boundary scope; it is not the present $V$ and is not silently extended to $\delta_*$ |

When a remaining observation is defined only on the original smooth compatible core, (WHR.26) is first an exact identity on that core. Its extension to a proposed larger physical square requires boundedness of the complete observation and all cross maps in that square. No rough bulk solution is manufactured from a trace isomorphism.

The original WGB/WCF angular high gate is not changed into (WHR.29). These are different infinite blocks in different spaces. If both are used, each elimination must retain the full response columns entering the other's finite equations. Choosing an elimination order does not discard mixed head/high feedback.

For a fixed admitted $\delta$, the Fredholm conclusion is proved without an inverse test. If uniform $A_\infty,A_1,C_K$ are supplied on a common interval, the same mesh estimate is uniform, giving a uniformly bounded $R_{N,\delta}^{-1}$ after its strict gate. This alone proves neither operator-norm continuity of the head feedback nor a uniform finite determinant. Strong continuity of a stable map, even with a compact operator on its left, is not substituted for those missing statements. In particular $m_H$ is not presumed constant in the parameter.

## WHR9. The next executable target, without repeated old mathematics

A first new consumer for (WHR.29) has the following exact mathematical target. It need not reevaluate any old Airy, ray, collar, body, exterior, root inverse or waist-error quantity.

1. Read the complete original negative-one positive summary and its process identity. Consume its already saved whole-positive raw-state source columns in their original units. Retain all original mean, endpoint and failure-history fields.
2. Read the complete same-member or full-family bounds for $B_{HL}$ and $B_{LH}$. Use the actual shell and the already proved factor 1153. If the needed whole maximum was not previously saved, compute only that missing named contraction from the immutable complete old row records; do not rerun the row producer or replace a partial maximum by a whole bound.
3. Read an existing bound for the same $A_L$ when its exact scope is available; otherwise form only the new complete finite expression (WHR.9) from already accepted coefficient bounds. Retain all five groups, the even mean and every primitive factor.
4. Produce directed complete $C_K,C_V,C_D,C_R$ and a declared mesh. Any exponential in (WHR.16) is a new scalar target unless an already completed same-operator bound is consumed. A saved centre-only two-boundary Green is not used as the current IVP.
5. Save the full outward $\varepsilon_N$ and its retained strict comparison. A failed strict gate is a complete scientific outcome. It does not authorize discarding a row or repeating a successful old target.
6. Only after that gate, a separate finite-pairing target can enclose (WHR.31), the actual columns $R_N^{-1}E_N$, and every cross block of (WHR.32), including original endpoint chart, physical mean, metric, WCF/WFR and $\Theta$ rows. A scalar norm upper does not determine these signed entries.

This specifies new quantities and a genuine sufficient test, not a numerical result. A large or impractical mesh must be reported as such; it cannot count as completion of the physical inverse. A sharper same-operator IVP estimate, a better radial approximation space with a proved remainder, or exact low-operator block structure may improve this head test without changing its complete factorization.

The unconditional new conclusion is (WHR.20)--(WHR.26): the complete positive head self-block is Fredholm of index zero, and its elimination has precisely the finite kernel/cokernel compatibility and cross terms shown there. The quantitative alternative (WHR.27)--(WHR.32) provides a trace-safe finite-factor contract. The complete positive/high/negative/exterior physical inverse, actual finite matrix, true parameter Schur and nonlinear family remain separate tasks.

## WHR10. Immutable primary sources

All paths below are relative to topics/visible-flex-exact-nearby/. Each source was read as complete small text. No native or binary body was fetched.

| Source and use | Path | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| N: full moving operator and independent physical mean | results/R133-supplement-complete-moving-root-scalarization.md | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| Negative-one full-delta positive contract: shell, sources, boundary chart and all ports | results/R133-supplement-full-delta-negative-one-positive-source-and-regular-ports.md | 6765382c0ea8af731b6593b687cbc84401a4f7ec | 15756 | 0f1383da8611aef931829876b49579f41c7a967435c795ef68a85d2a142cac23 |
| Actual complete positive graph in that window | results/R133-supplement-actual-full-delta-negative-one-positive-source-graph.md | 8b28bcd0929df468f44186236dd0cf2e9c037dad | 10464 | e144ad9f8cd7dbc29904f92524e9da9511f4bb8d403e06620d8ad85f3105742c |
| Same true root and global positive reference | results/R133-supplement-full-real-delta-positive-high-root-to-regular-graph.md | 04a8f78ad57671d4914c5fd169d83f2efee89d4d | 10473 | 5c4b3e1ba50b96e1955c24e560627bb7efc01c447b35ed9352373febb9a09e6e |
| WPM: true radial mean, physical endpoint and parameter rows | results/R133-supplement-physical-reflection-mean-rank-and-complete-scalar-row-ledger.md | f6bc0eafe774149bb768bb71c9dfc4ea39e82a15 | 23951 | 65cc1edec37adb5b0a3667c7e37df2a94bb24201697a53f4a1c7f9bc341f68c7 |
| BT: the radial head is not a finite angular trace | results/R133-supplement-concrete-transported-head-factors-and-retained-operator-audit.md | 8b8646be926d77583138c628c811a0a78672f3a3 | 19570 | b5c2f8441ee616ea801bad8a3b18f57108d8c695f781ee21eb1ce39dcad5cbcf |
| WGB: actual graph, physical 96 columns and complete cross equations | results/R133-supplement-exact-graph-parameterization-and-physical-finite-border.md | 30cd8f7858888c35f942094611614c9f74b3e2af | 25135 | e7d23c583205fcb538fd21260e2e9c5b4859ed73ab6129a453b8c5d1fb05bf7c |
| WFR: complete root finite factor | results/R133-supplement-exact-finite-root-factor-and-reduced-graph-high-test.md | 66557b3eb76c002dedbb7189a197a5a066ec0201 | 16083 | cb72cb37e284e8e4b4c834896b1437ee6400d78a9f8fe5321e75e4b4dac0fcde |
| WCF: complete coefficient finite factors and full graph order | results/R133-supplement-exact-finite-coefficient-factors-and-remaining-graph-error.md | 86090c70f18298a204137f21da7715bdcf19ab18 | 23257 | 452ee9e41e27a1a2000ea2746e09decc6c936b37a5759a1ace656b500bbfb9dd |
| Old finite193 Green: its separate centre and boundary scope | results/R133-supplement-actual-complete-finite193-Green-and-true97-Poisson-three-windows.md | 3318881cc6e0aa629037b468a54f200439f0543c | 15118 | 38c385e2e910ea7d4e52d391578f012c198f41ba8a33bd443462236ed4c3d06c |

The head completion here has its own unknown dimension and its own exact rows. It does not reuse the zero-dimensional FC completion as a proof of a different inverse.
