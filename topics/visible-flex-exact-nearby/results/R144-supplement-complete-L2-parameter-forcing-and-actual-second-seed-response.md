# R144 HL: complete L2 parameter forcing and the actual second-seed response

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved.** The actual full parameter column of the S/T tail has the
same complete source bound as GA with the direction norm replaced
by $L^2$:
$$
 \|D_\gamma{\cal F}_\gamma(w)[\eta]\|_{Z_s^{[3]}}
 \le\{2^{8388608}\epsilon_L(1+W_{s+1})
          +2^{6291456-110000000}W_s\}\|\eta/r_\gamma\|_{L^2},
 \quad20\le s\le2898 .
 \tag{HL.1}
$$
Here $W_j=\|w\|_{E_j^+}$ in the same common physical reference.
In particular, if $W_{s+1}\le1$, the already paid GA combination gives
$$
 \|D_\gamma{\cal F}_\gamma(w)[\eta]\|_{Z_s^{[3]}}
             <2^{-48000000}\|\eta/r_\gamma\|_{L^2}.
 \tag{HL.2}
$$
The operator is jointly continuous
$L^2\to Z_s^{[3]}$ when gamma varies in its relative $A^0$ topology
within the original value domain and $w$ varies in $E_{2960}^+$.

This is a genuine Hilbert-direction estimate. Its proof starts from
M's complete lag kernel, proves the square-zero $L^2$ long module,
differentiates the actual incoming fixed point and each of the 94
seed updates, and then retains the actual second parameter and
complete first-principal feedback. No small value bound is
differentiated without these actual derivative equations.

The independent metric reference-height, with its reference $1$,
retains its separate column. It is not put into an ordinary source
bound proportional to the nonmean state. No nonlinear $L^2$ open
value domain, rough-source onto inverse, or new cap/body solution
is asserted.

## 1. Same objects, units and direction convention

Use the original completed proofs:

- [M: two-input zero-width cap and complete inner ports](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md), especially M.6--M.7 and M.13--M.19;
- [RG: true rough-input separated-end seed](R119-supplement-rough-inner-curvature-data-and-true-smoothed-B-seed.md), especially RG.6--RG.26;
- [T: actual selected family and seed reference](R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md), especially C.3--C.14;
- [GA: the complete mixed parameter forcing](R144-supplement-separated-end-A0-parameter-forcing-with-complete-mixed-height.md);
- [GF: the full actual parameter source](R144-supplement-complete-parameter-forcing-for-the-selected-exact-tail-family.md);
- [GHR](R144-supplement-actual-seed-metric-reference-height-and-complete-endpoint-column.md), for the separate metric-reference height;
- [S](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md), with its actual endpoint lift, reference units and complete ordinary mean recovery.

The real value domain and reference are exactly GA's:
$$
 \|\gamma/r_\gamma\|_{A^0}\le1/128,\qquad
 \|\gamma/r_\gamma\|_{H^{8193}}\le2^{1048576},\qquad
 \|w\|_{E_{1856}^+}\le2^{-49000000},
 \qquad r_\gamma=10^{-9}.
 \tag{HL.3}
$$
The far height and cap-end height use the different original units
$r_B=2^{-60}$ and $r_f=10^{-8}$. Put
$$
 G=\gamma/r_\gamma,\qquad
 U=|D_\theta|^2f/r_B,\qquad e=\eta/r_\gamma,\qquad f=F_Bw .
 \tag{HL.4}
$$
Use normalized Fourier $L^2=H^0$ on the complete signed set
$4\mathbb Z$. The original even nonmean subspace is kept.
Scalar means are output frequency zero; no input or output mean
is removed merely by changing the direction norm.

Initially take $e$ to be a finite even Fourier polynomial. The
original holomorphic $A^0$ maps have their actual derivatives in
these directions. The uniform Hilbert bounds below extend those
same linear derivatives uniquely to all $L^2$ directions. They
do not extend the nonlinear input set.

## 2. M's complete kernel gives the genuine cap L2 direction

M.16 is a bound for each complete input tuple, not an assertion
that an arbitrary column-bounded matrix is bounded on $L^2$.
Its pointwise consequence, including the full radial supremum
for an output coefficient, is
$$
 |T_k(m;n_1,\ldots,n_k)|
           \le2\,4^k e^{-h|m-\sum n_i|},\qquad h=2^{-15}.
 \tag{HL.5}
$$
The two species are already included in the direct-sum input
norm of M.6. Let
$$
                        K_h(\ell)=e^{-h|\ell|}.
$$
Using all integer frequencies as an upper bound for $4\mathbb Z$,
$$
 \|K_h\|_{\ell^1}
   =1+\frac{2}{e^h-1}
   \le1+\frac2h<2^{17}.
 \tag{HL.6}
$$
Thus both lag signs and the entire convolution factor are paid.

Differentiate one gamma slot of the full Taylor series at
$Z=(G,U)$. If $b=\|G\|_{A^0}+\|U\|_{A^0}\le1/16$, the
absolute majorant for degree $k$ is a convolution of $K_h$,
one $\ell^2$ sequence $|e_n|$, and $k-1$ actual $\ell^1$
background sequences. Young's
$\ell^1*\ell^2\to\ell^2$ inequality, after taking the radial
supremum in each coefficient, gives
$$
 \|D_G V(G,U)e\|_{\mathcal O_0^H}
 \le2\|K_h\|_1\sum_{k\ge1}k4^k b^{k-1}\|e\|_2
 \le\frac{128}{9}\|K_h\|_1\|e\|_2<2^{21}\|e\|_2.
 \tag{HL.7}
$$
The Hilbert output uses M's normalized complete outputs, with
the joint radial $\ell^2(C_r)$ module in place of the angular
Wiener norm. In particular,
$$
 \|D_\gamma\Phi_\gamma(f)[\eta]\|_{\dot H^2}
                         <2^{21}r_f\|\eta/r_\gamma\|_2 .
 \tag{HL.8}
$$
The actual $f_*$ output is the one in M.7. Its cap construction
still contains the B and C means, true holonomy root and the
unscreened mean-height span. Each scalar mean row is controlled
as the $m=0$ output of the same complete convolution.

The same argument with one $L^2$ gamma direction and one
$A^0$ background difference uses
$$
 2\sum_{k\ge2}k(k-1)4^k b^{k-2}
       \le4096/27<2^8 .
$$
Together with (HL.6), this bounds that mixed derivative by
$2^{25}$ in the normalized output. Hence (HL.8) is a genuine
operator-valued holomorphic family on this low Wiener domain,
jointly continuous in $G,U$ with their $A^0$ topology. No row
bound has been inferred from a column sum: the full lag
convolution (HL.5)--(HL.6) is what proves the Hilbert statement.

All auxiliary cap evaluations below use
$\|G\|_{A^0}\le1/64$ and $\|U\|_{A^0}<1/32$, whose sum is
less than $1/16$. The smaller far probe ball is necessary
for this particular kernel argument.

## 3. The actual long module with one Hilbert direction

Retain RG's same two-ended Green functions, both reflected
terms, full small-root mean and true endpoint lifts.
The background is still in its original Wiener ball.
For a distinguished direction use the block sum of the
$\ell^2$ norms of the modewise radial suprema of
$$
 e^{\sigma(t)|m|}e^{\lambda(L-t)}
                  |m|^2|\dot h_m|,\quad
 e^{\sigma(t)|m|}e^{\lambda(L-t)}
                  |m||\dot h_m'|,\quad
 e^{\sigma(t)|m|}e^{\lambda(L-t)}|\dot h_m''|.
 \tag{HL.9}
$$
Its scalar mean has the original radial supremum norm.
Multiplication is now the actual Wiener-background/Hilbert-
direction module, with norm one. Mean extraction is bounded
by the same complete convolution or the $\ell^2$ pairing.
The Green and lift estimates are modewise before taking
the sequence norm, so their original constants remain.

Consequently the full differentiated contraction, with
zero left direction and right direction $\dot g$, gives
for $\sigma(t)=\sigma(1-t/L)$ and $\lambda=7/4$,
$$
 \|\dot h\|_{\mathfrak Y^H_{\sigma,7/4}}
 \le16\|\dot g\|_{\dot H^2}
                +\frac58\|\dot h\|_{\mathfrak Y^H_{\sigma,7/4}} .
 \tag{HL.10}
$$
The original complete mean derivative is controlled in the
same module. Reading its actual left mean and nonmean slope,
the already paid coefficient $128/3+1/24<44$ yields
$$
 \|D_g{\cal K}(f,g)[\dot g]\|_{\dot H^1_\sigma\oplus\mathbb C}
                         <44\epsilon_L\|\dot g\|_{\dot H^2}.
 \tag{HL.11}
$$
This holds for the original $\sigma=s_\beta$, and for every
$0\le\sigma\le1$ used below. In every case
$\sigma/L<1/32$ and the actual right width is zero.
The background does not receive the radial difference weight.

For the incoming map with $f=0$, use RG's genuine
$\sigma(t)=7(L-t)/16$ and $S'=7L/16$. Its contraction
is $5/16$, so the same differentiated equation gives
$$
                 \|Dg_*(g)[\dot g]\|_{\dot H^1_{S'}}
                                  <24\|\dot g\|_{\dot H^2}.
 \tag{HL.12}
$$
All these are derivative proofs in the original complete
integral equations. The mean-height span remains its original
directed integral with its physical scale; it is not assigned
the nonmean screening factor in (HL.11).

## 4. Differentiate the true incoming seed and all 94 ordered updates

The true seed is the one in RG, not a new small label chosen for
this estimate. Put
$$
 R_a=2^{-55000000},\qquad
 \beta_H=262144,\qquad \beta_n=262144-2080n .
$$
Every actual label used below lies in the original
$\|a\|_{\beta_n}\le1/256$ domain. RG.13 implies
$$
 \||D|^2f(a)/r_B\|_{A^0}
        \le2^{-443+60}\|a\|_{\beta_n}
        \le2^{-391}<1/32 .
 \tag{HL.13}
$$
Thus (HL.8) applies to every cap evaluation in the seed.

The incoming fixed point is exactly
$$
       a_0={\cal I}_\gamma(a_0),\qquad
       {\cal I}_\gamma(a)=D_0^{-1}g_*(\Phi_\gamma(f(a))).
 \tag{HL.14}
$$
Let $d=S'-\beta_H-1850>1$ and $E'=4d$, as in RG.14.
For any complete nonmean Fourier sequence, Cauchy--Schwarz gives
$$
 \|v\|_{\dot A^1_{\beta_H+1850}}
 \le\left(\sum_{m\in4\mathbb Z\setminus\{0\}}
                              e^{-2d|m|}\right)^{1/2}
                      \|v\|_{\dot H^1_{S'}}
 <2e^{-E'}\|v\|_{\dot H^1_{S'}} .
 \tag{HL.15}
$$
Both signs are included. Indeed the exact square sum is
$2e^{-8d}/(1-e^{-8d})$, and $d>1$ makes its square root
smaller than $2e^{-4d}$. No incoming width is silently restored.

Differentiate (HL.14) at fixed label. The actual $D_0^{-1}$
norm $1/16$, (HL.8), and (HL.12)--(HL.15) give
$$
 \|D_\gamma{\cal I}_\gamma(a)[\eta]\|_{\beta_H}
  <3e^{-E'}2^{21}r_f\|e\|_2
  <2^{23}R_a\|e\|_2.
 \tag{HL.16}
$$
The last step is the completed RG.15 inequality
$(3/2)e^{-E'}<2R_a$, and $r_f<1$.
The original full label contraction is
$\|D_a{\cal I}_\gamma\|<2^{-55000406}<1/2$. Differentiating
its exact fixed-point equation, with that entire inverse,
therefore proves
$$
 D_\gamma a_0=(I-D_a{\cal I}_\gamma)^{-1}
                               D_\gamma{\cal I}_\gamma,\qquad
          \|D_\gamma a_0[\eta]\|_{\beta_H}<2^{24}R_a\|e\|_2.
 \tag{HL.17}
$$
This is an actual derivative estimate, not Cauchy applied to
a small real label value.

For the subsequent exact steps retain RG.23--RG.25:
$$
 \begin{gathered}
 {\cal F}_\gamma(a)
    =k(a)-K_{B,\perp}(f(a),\Phi_\gamma(f(a))),\\
 a_{n+1}=a_n-D_0^{-1}{\cal F}_\gamma(a_n),\qquad 0\le n<94.
 \end{gathered}
 \tag{HL.18}
$$
For a parameter direction $v_n=D_\gamma a_n[\eta]$, its exact
differentiated equation is
$$
 v_{n+1}
 =-D_0^{-1}\{[D_a{\cal F}_\gamma(a_n)-D_0]v_n
                               +D_\gamma{\cal F}_\gamma(a_n)[\eta]\}.
 \tag{HL.19}
$$
The first term includes the complete actual label/phase/metric
response. RG.24 in its genuine norms gives
$$
 \|D_0^{-1}[D_a{\cal F}_\gamma(a_n)-D_0]:
                         \ell^1_{\beta_n}\to\ell^1_{\beta_{n+1}}\|
 \le2^{-404}(\|a_n\|_{\beta_n}+\epsilon_L)<1/2 .
 \tag{HL.20}
$$
The source-width difference is precisely
$$
 s_{\beta_n}-(\beta_{n+1}+1850)=3177/400>1.
 \tag{HL.21}
$$
At fixed $a_n$ the second term of (HL.19) is exactly the
negative of the full cap-end direction in (HL.11), after
the original nonmean projection:
$$
 D_\gamma{\cal F}_\gamma(a_n)[\eta]
 =-P_\perp D_g{\cal K}(f(a_n),\Phi_\gamma(f(a_n)))
                                      D_\gamma\Phi_\gamma(f(a_n))[\eta].
$$
Apply (HL.8), (HL.11), and Cauchy--Schwarz at the actual gap
(HL.21), then the same $D_0^{-1}$. A conservative full bound is
$$
 \|D_0^{-1}D_\gamma{\cal F}_\gamma(a_n)[\eta]\|_{\beta_{n+1}}
                          <2^{24}\epsilon_L\|e\|_2.
 \tag{HL.22}
$$
For example $2\cdot44\cdot2^{21}/16<2^{24}$ already includes
both lag signs, and the omitted positive gap exponential
and $r_f<1$ can only decrease that bound.

Use $B_a=2^{32}R_a$. The initial bound (HL.17) is smaller
than $B_a$. Since
$$
                  2^{24}\epsilon_L<\tfrac12 B_a,
 \tag{HL.23}
$$
(HL.19)--(HL.22) prove by induction through each of the 94
actual updates that
$$
          \|D_\gamma a_{94}[\eta]\|_{\ell^1_{66624}}
                                    <2^{32}R_a\|e\|_2.
 \tag{HL.24}
$$
The induction uses the actual norms on successive widths.
It is not a derivative of the final value estimate.

The maps in this argument are the original holomorphic
incoming fixed point and finite ordered operations. The
module estimates show their actual derivatives to be bounded
$L^2\to\ell^1_{66624}$. The mixed coefficient argument of
section 2 and the actual long resolvent imply continuity
in that operator norm when the admitted gamma varies in
$A^0$. The 94-step recursion is finite, so its complete
operator continuity follows without an infinite-step
differentiation or an unproved high-width trace.

## 5. The seed's true second parameter retains the old small bound

Use the same
$\mathfrak q(\gamma)=\Gamma_2^*(a_{94}(\gamma))-\bar\Gamma_2$
and the exact weighted space $\mathcal P_2$ of T.C.5.
Its norm still has the original two-neighbor internal weight
and separate shallow exterior row. No six-neighbor source
weight is substituted into that definition.

T.C.4, T.C.8 and the actual label value give
$$
 \begin{gathered}
 \|a_{94}\|_{224}<2^{-55332002},\\
 \|D_\gamma a_{94}[\eta]\|_{224}
                       <2^{-55331968}\|e\|_2,\\
 \|D_a\mathfrak q^*(a)\|_{\ell^1_{224}\to\mathcal P_2}
                              \le2^{266256}\|a\|_{224}.
 \end{gathered}
 \tag{HL.25}
$$
Therefore the full actual chain rule proves
$$
 \begin{aligned}
 \|D_\gamma\mathfrak q(\gamma)[\eta]\|_{\mathcal P_2}
 &<2^{266256-55332002-55331968}\|e\|_2\\
 &=2^{-110397714}\|e\|_2
  <2^{-110000000}\|e\|_2 .
 \end{aligned}
 \tag{HL.26}
$$
Both the small label value and its separately proved Hilbert
direction enter this product. The radial first compensation
and all cross-parameter responses are the same true joint map
used in T.C.7--C.8. They are not replaced by diagonal bump
derivatives.

This operator is continuous $L^2\to\mathcal P_2$ on the
relative $A^0$ gamma domain, by (HL.24) and the holomorphic
weighted joint map of T.C.7--C.8. The old value bound on
$\mathfrak q$ is unchanged. Thus its reference comparisons,
root germs, fixed stop and B scale remain precisely those
of T.C.10--C.14.

## 6. Complete mixed far-height smoothing with an L2 gamma direction

For the endpoint column set
$$
 {\cal A}_G(U)e
   =D_g{\cal K}(f,\Phi_\gamma(f))
                                  D_\gamma\Phi_\gamma(f)[r_\gamma e].
 \tag{HL.27}
$$
Use $0\le\sigma\le1$ with the true long width
$\sigma(t)=\sigma(1-t/L)$, cap-end width zero, and the same
radial difference weight. On the auxiliary far ball
$\|U\|_{A_\sigma^0}<1/32$ and $\|G\|_{A^0}\le1/64$,
(HL.8), (HL.11) prove
$$
          \|{\cal A}_G(U)e\|_{H^1_\sigma,\mathrm{complete}}
                          \le M_H\|e\|_2,\qquad
                          M_H=2^{32}\epsilon_L .
 \tag{HL.28}
$$
The complete norm uses $a_m=\max(1,|m|)$, including $m=0$.
For the bound before widening,
$44\,2^{21}r_f<2^{27}<2^{32}$.
The far analytic width is only a Taylor probe, not an
analyticity requirement on the actual far field or gamma.

Expand in the far input. Cauchy on radius $1/32$ and
polarization give degree-$d$ coefficient norm at most
$M_H128^d$, not the $M_H4^d$ appropriate to a unit ball.
For normalized even cosine probes retain their two signed
Fourier coefficients, and absorb $a_m$ into the kernel.
The width-zero and width-one estimates give, for one entire
direction $e$ and $B=\sum_{\ell=1}^d|n_\ell|$,
$$
 \begin{split}
 \|K_{d,G}(m;\mathbf n)[e]\|_{\ell_m^2}
                              &\le M_H128^d\|e\|_2,\\
 \|e^{|m|-B}K_{d,G}(m;\mathbf n)[e]\|_{\ell_m^2}
                              &\le M_H128^d\|e\|_2 .
 \end{split}
 \tag{HL.29}
$$
They are coefficients of the same actual map, identified
on finite Fourier probes by the unique cap and long
solutions. Split the output axis at $|m|=B$ to obtain
$$
 \|e^{(|m|-B)_+}K_{d,G}(m;\mathbf n)[e]\|_{\ell_m^2}
                                \le2M_H128^d\|e\|_2 .
 \tag{HL.30}
$$
No sum of separate operator norms over output frequencies
is asserted. The full direction is tested before the
output Hilbert norm is taken. Both the mean row and both
frequency signs remain.

For the actual far field put
$b_j=\sum_{n\ne0}|n|^j|U_n|$. The original added B trace,
with its actual $2^{440}$ coefficient and $r_B=2^{-60}$,
gives
$$
          b_0\le2^{-10},\qquad
          b_{s+1}\le2^{-380}W_{s+1}.
 \tag{HL.31}
$$
The stronger low inequality follows directly from the same
trace and $W_{1856}\le2^{-49000000}$; it is not a new input
restriction. Thus $x=128b_0\le1/8$.

Use $n=s+1$, $\lambda=(|m|-B)_+$, and the complete inequalities
$$
 \begin{gathered}
 (1+|m|)^n\le3^{n-1}(1+B^n+\lambda^n),\qquad
 B^n\le d^{n-1}\sum_{\ell=1}^d|n_\ell|^n,\qquad
 \lambda^ne^{-\lambda}\le n!,\\
 \sum_{d\ge0}x^d<2,\qquad
 \sum_{d\ge1}128^d d^n b_0^{d-1}
       \le128n!(1-x)^{-n-1}\le2^{n+8}n!.
 \end{gathered}
 \tag{HL.32}
$$
Apply these to (HL.29)--(HL.30) in $\ell^2$ and use
Minkowski to sum the absolute far-input coefficients.
Every high far factor is paid once by $b_n$; all others
are paid by $b_0$. The constant and excess terms include
$d=0$ and $m=0$.

The original inequality
$\langle m\rangle^{s+2}/a_m
 \le2^{s+2}(1+|m|)^{s+1}$ then gives the safe complete bound
$$
 \|{\cal A}_G(U)e\|_{H^{s+2}}
 \le2^{4s+60}(s+1)!\epsilon_L(1+b_{s+1})\|e\|_2
 \le2^{65536}\epsilon_L(1+b_{s+1})\|e\|_2 ,
 \quad20\le s\le2898.
 \tag{HL.33}
$$
The new exponent check is $16s+72\le46440<65536$.
This retains all mixed far-height terms; the gamma
direction has no angular derivative on the right.

The actual S.12 endpoint lift and (HL.31) therefore give
$$
 \|D_\gamma{\cal U}_\gamma(w)[\eta]\|_{E_s^+}
       \le2^{131072}\epsilon_L(1+W_{s+1})\|e\|_2,
                    \qquad20\le s\le2898.
 \tag{HL.34}
$$
This is the same numerical budget as GA.10, now proved
for an actual Hilbert parameter direction.

## 7. Joint Hilbert-operator continuity with every high far factor

The family in (HL.28) is holomorphic as an operator from
$L^2$ to the complete left Hilbert space. This follows from
the convergent module kernels in section 2 and the actual
differentiated long resolvent. It is not a Banach-space
Cauchy estimate on an unproved $L^2$ nonlinear input ball.

For a gamma background difference, keep the actual inputs
on $\|G\|_{A^0}\le1/128$. The complex gamma circle of radius
$1/256$ remains within the auxiliary $\|G\|\le1/64$ domain.
Its operator Cauchy bound costs at most $2^8$.

For a far-height difference, telescope each complete
multilinear coefficient, keeping one differing far slot.
The high frequency can belong to that slot or to one
unchanged background slot. The degree sums in (HL.32)
then have at most two extra degree moments. Through
$s+1\le2899$, these cost at most 24 additional factorial
bits; a further factor128 costs 7 bits. Together with
the gamma factor8 bits and the fixed scalar sum charges,
all additions fit 64 bits. The new complete exponent
check is
$$
                       16\cdot2898+136=46504<65536.
 \tag{HL.35}
$$
Thus the widened joint estimate is
$$
 \begin{split}
 &\|{\cal A}_G(U)-{\cal A}_{G'}(U'):
                             L^2\to H^{s+2}\|\\
 &\ \le2^{131072}\epsilon_L
  \{\|U-U'\|_{\dot A^{s+1}}
       +(1+b_{s+1}+b'_{s+1})
                    [\|U-U'\|_{A^0}+\|G-G'\|_{A^0}]\},
 \quad20\le s\le2898 .
 \end{split}
 \tag{HL.36}
$$
All actual low far norms stay below $2^{-10}$, so every
telescoped series converges with $128b_0\le1/8$.
The term involving a high unchanged background is retained.
A bound without it would not prove the required mixed
operator continuity.

After the original endpoint lift, this proves continuity
of $D_\gamma{\cal U}_\gamma(w)$ as
$L^2\to E_s^+$ for gamma in relative $A^0$ and $w$ in
$E_{s+1}^+$. It is the same actual endpoint column, with
its real five-jet support and all radial source units.

## 8. Full metric feedback, complete ordinary source and its units

The exact separation identity GA.13 remains
$$
 {\cal F}_\gamma(w)=
   \mathfrak f_{\mathfrak q(\gamma)}(w)
       +\{\mathfrak f_0(w+v_\gamma)-\mathfrak f_0(w)\},
 \qquad v_\gamma={\cal L}_\partial q_\gamma(F_Bw).
 \tag{HL.37}
$$
Its support proof holds for every candidate first parameter,
not just the selected one. All design bumps and every
negative principal input are outside the fixed positive
B collar. The same local mean root occurs on both sides,
so (HL.37) is the complete ordinary-source identity.

Differentiate at one fixed physical $w$:
$$
 D_\gamma{\cal F}_\gamma(w)[\eta]
  =D_{\mathfrak q}\mathfrak f_{\mathfrak q(\gamma)}(w)
                                 [D_\gamma\mathfrak q(\gamma)[\eta]]
    +D_u\mathfrak f_0(w+v_\gamma)[D_\gamma v_\gamma[\eta]] .
 \tag{HL.38}
$$
The first term is GF's whole actual metric column: both
radial bumps, first compensation, the full inverse
$(I-D_pT)^{-1}$ in the first-principal response, and the
true reference source are retained. Its directional
estimate is already stated in the actual $\mathcal P_2$
norm. The new bound (HL.26) therefore gives the same
$2^{-110000000}\|e\|_2$ input budget as GF/GA required.

The second term is the genuine endpoint ordinary source.
Its actual $E_s^+$ bound (HL.34) is exactly the complete
numerical budget previously used in GA.10. Substituting
these two newly proved Hilbert-direction bounds into
the unchanged full ordinary source inequality
$$
 \|D_u\mathfrak F(u)[v]\|_{Z_s^{[3]},\rm full}
 \le2^{4194304}
  \{\|v\|_{E_s^+}+(1+\|u\|_{E_s^+})\|v\|_{E_{20}^+}\}
$$
and the original metric source estimate proves (HL.1).
The original GF.11 comparison is applied before multiplying
high factors, so only one highest $W_{s+1}$ occurs.
The already completed GA.14--GA.15 arithmetic then gives
(HL.2), without a new scientific or profile calculation.

The internal unit is still $\zeta_j\delta_j^{16}$. The
finite connector has its own original ordinary source
unit and $2^{440}$ weight. All three scaled broken radial
source derivatives and their true one-sided representatives
remain. There is no substitution of an internal density
factor into a finite source, and no new raw radial trace.

The complete ordinary holonomy-mean source and off-shell
charge identity are retained exactly as in GF:
$$
             \langle A\,D\mathfrak F\rangle
                           =-\langle DA\,\mathfrak F\rangle .
 \tag{HL.39}
$$
Only on an exact background may its right side vanish.
Independently prescribed flux or compatibility loads
remain separate ports.

The metric reference-height has its genuine formula
$$
 (H_{\rm met})_t
       =aW\{\psi(1+\kappa)+\dot\kappa\},\qquad
 H_{\rm met}(t_f)=0 .
 \tag{HL.40}
$$
Its reference $1$ is not removed. GHR's already proved
$\mathcal P_2$ bound, applied to (HL.26), also yields
$$
 \|H_{\rm met}[D_\gamma\mathfrak q(\gamma)\eta]\|_{C_r^2}
   <\rho\varepsilon_s2^{1024-110000000}\|e\|_2 .
 \tag{HL.41}
$$
It keeps the same physical Cartesian conversion, two
endpoint heights and full conormal column. It is separate
from (HL.1), which is an ordinary source estimate.

The metric-source operator continuity follows from
(HL.26) and the full principal/reference construction
already used in GF and GA section 6. On finite groups of
cells its real ODE, mean coefficients and compact bumps
are continuous in the displayed operator norm. On the
infinite remainder the original physical source profiles
tend uniformly to zero. Those are the true profiles
after the full source is formed, with the shallow
exception and both original profile junctions retained.

For the endpoint source, (HL.36) gives operator continuity;
on its fixed collar the original rational coefficients,
small-root mean and three source jets are continuous
in the background. Hence, for every $20\le s\le2898$,
$$
 (\gamma,w)\longmapsto D_\gamma{\cal F}_\gamma(w)
   \quad\hbox{is continuous in }\mathcal L(L^2_{\perp,\mathrm{ev}},
                                            Z_s^{[3]}),
 \tag{HL.42}
$$
when gamma has its original relative $A^0$ topology and
$w$ the common $E_{2960}^+$ topology. The same topology
controls the independent metric-height column in its
own stated output space.

## 9. Actual parameter differences and the precise new permission

For two original admitted parameters use their convex
segment and one fixed physical graph input. The actual
fundamental theorem of calculus, first for their genuine
high-regularity difference, and then the Hilbert operator
bound give
$$
 \|{\cal F}_{\gamma'}(w)-{\cal F}_\gamma(w)\|_{Z_s^{[3]}}
 \le\{2^{8388608}\epsilon_L(1+W_{s+1})
       +2^{6291456-110000000}W_s\}
                       \|(\gamma'-\gamma)/r_\gamma\|_2 .
 \tag{HL.43}
$$
In particular at $s=1794$ the coefficient is
$2^{-48000000}$ on the original low ball. At the actual
selected limit the already proved $E_{2960}^+$ bound
supplies $W_{s+1}\le1$ for the entire window.

For the selected high-response window $64\le j\le1164$,
the required source index is $s=j+1734\le2898$, and the
highest far background is $j+1735\le2899<2960$.
Thus (HL.1), (HL.2) and (HL.42) supply precisely the full
mismatch, derivative and operator-continuity interface
needed by the existing low inverse and actual selected
difference quotients.

This proof does not redo that selection argument. It
does not claim continuity in any new selected
$\mathcal L(L^2,E_j)$ operator topology, does not create
a nonlinear $L^2$ cap value ball, and does not assume
onto solvability for arbitrary rough forcing.
It supplies the genuine $L^2$ parameter column with all
actual seed, principal, mean and source terms included.

## 10. New exact combinations

The companion
[fourfold_codazzi_l2_gamma_forcing_saved_bounds.py](../scripts/fourfold_codazzi_l2_gamma_forcing_saved_bounds.py)
records the 15 new exact rational and integer combinations
for the Hilbert module, true seed recursion and complete
mixed high-frequency budgets. Their first evaluation in
code mode passed; the Python reader preserves those
same operations and was not run in the unavailable local
environment.

The earlier GA/GF source combinations are consumed in
their unchanged stated bounds, not rerun. No old native
array, seed iteration, principal map, profile integral,
Green kernel or scientific target was recomputed.
