# R133 supplement: exact exponential subprincipal normalization and a directly matched strong remainder

2026-11-15, visible-exact / root.

**Proved conditional operator theorem.** This gives a second complete normalization route when the actual return is validated against an exponential first-symbol reference. It keeps the entire scalar phase in that reference. It does not remove any term from the already proved linear-reference budget CN.

The quantitative inputs are the same complete real first coefficient and actual angle as in [CN](R133-supplement-exact-full-circle-subprincipal-normalizer-and-strong-remainder-budget.md), together with a new, independently validated remainder relative to the full exponential. The latter is not supplied by a norm of the old linear-reference remainder. No new numerical computation is asserted here.

## 1. Exact units and the new conditional input

Use the original physical rotation coordinate of period $\pi/2$, normalized angular measure, and
$$
 e_j(x)=e^{4ijx},\qquad
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 I=\partial_x^{-1}(1-\Pi),\qquad \Pi f=\langle f\rangle .
 \tag{EN.1}
$$
Write $U_\Omega f(x)=f(x+\Omega)$ for the actual selected principal rotation. It is unitary on every Sobolev space in these units. Let
$$
 c=\mu+v,\qquad \mu=\langle c\rangle\in\mathbb R,\qquad
 \langle v\rangle=0,\qquad C=\|v\|_{H^3}.
 \tag{EN.2}
$$
This is the complete first coefficient after the prescribed true root, waist and angle changes. It is not a pointwise strict-region scalar or the already accepted mean phase alone.

Use the CN all-mode solution
$$
 w(x-\Omega)-w(x)=v(x),\qquad \langle w\rangle=0,
 \qquad w_-(x)=w(x-\Omega).
 \tag{EN.3}
$$
The actual bounded15 principal gap, physical frequencies and full signed coefficient sums are those of CN. Define $A_a=M_aI$ for any coefficient $a$.

Suppose a complete return on the same chart has the exact decomposition
$$
 \mathscr R=\zeta U_\Omega e^{A_c}+\mathscr E_{\exp},
 \qquad |\zeta|=1,\qquad
 \|\mathscr E_{\exp}\|_{H^{-4/3}\to L^2}\le R_{\exp,0}.
 \tag{EN.4}
$$
The exponential is the full convergent bounded-operator exponential on both spaces, not its finite Taylor polynomial. Every genuine branch, mean, source, cutoff, interface, finite-head and actual-coordinate remainder needed for (EN.4) belongs to $\mathscr E_{\exp}$.

In particular, obtaining the function $c$ from PF/CT does not by itself establish (EN.4). Conjugating a physical-angle exponential by a nonconstant density map changes the true primitive beyond its first symbol. Those complete differences must be included in the actual remainder; they cannot be replaced by the covariance rule for $c$ alone.

## 2. A full-circle exponential with an exact inverse

Set
$$
 \mathcal T_{\exp}=e^{A_w},\qquad
 \mathcal T_{\exp}^{-1}=e^{-A_w}.
 \tag{EN.5}
$$
Both operators are bounded on $H^{-4/3}$ and $L^2$, with no smallness assumption or further finite cutoff. The exact inverse follows from the bounded-operator exponential identity.

CN.7--8 and $\|I\|_{H^s\to H^s}=1/4$ give
$$
 \|\mathcal T_{\exp}^{\pm1}\|_{L^2\to L^2}\le e^{C/2},
 \qquad
 \|\mathcal T_{\exp}^{\pm1}\|_{H^{-4/3}\to H^{-4/3}}
                                      \le e^{51C/4}.
 \tag{EN.6}
$$
The shift $w_-$ has identical weighted Fourier norms.

The zero-mean primitive does not mean that the output mean can be discarded. Although
$\mathcal T_{\exp}^{\pm1}1=1$, general nonmean inputs can contribute to
$\Pi\mathcal T_{\exp}^{\pm1}f$. These full mean functionals remain part of any augmented finite system. Independent physical mean and charge rows are transformed with the actual operators, not set to zero or identified with a single scalar constant mode.

We also need the following complete elementary consequence of $v\in H^3$:
$$
 \|v\|_{\mathcal W_{4/3}}\le\|v\|_{\mathcal W_2}\le C,
 \qquad \|v'\|_{\mathcal W_0}\le C .
 \tag{EN.7}
$$
Indeed, for $n=4|j|\ge4$,
$(1+n)^4/(1+n^2)^3\le(5/4)^4n^{-2}$, and the full signed sum obeys
$$
 \sum_{j\ne0}(4|j|)^{-2}
 \le2\cdot4^{-2}\left(1+\int_1^\infty t^{-2}\,dt\right)=\frac14 .
$$
Cauchy--Schwarz therefore gives the squared multiplier factor at most
$625/1024<1$. The mean of $v$ is exactly zero; no unknown mode is omitted.

For real $\mu$, the scalar operator $\mu I$ is skew-adjoint in every one of these diagonal Sobolev inner products, including its zero action on constants. Thus
$$
 \|e^{t(\mu I+A_b)}\|_{H^s\to H^s}
       \le\exp\!\left(\frac{t}{4}\|b\|_{\mathcal W_{|s|}}\right),
 \qquad t\ge0,\quad s\in\{-4/3,0\}.
 \tag{EN.8}
$$
This follows by the interaction-picture Duhamel formula with the unitary group $e^{t\mu I}$ and Gronwall. The large constant part $\mu$ does not enter the exponential growth bound. The same statement holds with a minus sign on $b$.

## 3. Exact commutators, including every mean term

On smooth periodic inputs, the true primitive satisfies
$$
 [I,M_b]=-I M_{b'} I+M_{Ib}\Pi-\Pi M_b I .
 \tag{EN.9}
$$
For example, differentiating both sides gives
$-b'If+b\langle f\rangle-\langle bf\rangle$, and the means agree. This verifies the full identity, including its finite-rank terms.

Since $\Pi I=0$, (EN.9) gives
$$
 \begin{split}
 [A_a,A_b]={}&-M_a I M_{b'}I^2+M_b I M_{a'}I^2\\
             &-M_a\Pi M_bI^2+M_b\Pi M_aI^2 .
 \end{split}
 \tag{EN.10}
$$
The last two terms are retained. No high-output projection is invoked to delete them.

Put $a_0=\|a\|_{\mathcal W_0}$, $a_1=\|a'\|_{\mathcal W_0}$ and similarly for $b$, and use the already proved CN primitive norm
$$
 \iota=\|I^2\|_{H^{-4/3}\to L^2}
       =\frac{17^{2/3}}{16}<\frac12 .
 \tag{EN.11}
$$
Multiplication on $L^2$, the remaining $\|I\|_{L^2\to L^2}=1/4$, and the full rank terms then give
$$
 \|[A_a,A_b]\|_{H^{-4/3}\to L^2}
 \le K(a,b):=
 \iota\left\{\frac{a_0b_1+b_0a_1}{4}+2a_0b_0\right\}.
 \tag{EN.12}
$$
The estimate first holds on smooth inputs and extends by density to the displayed spaces. The regularity $w\in H^2$ supplied by CN makes $w,w'$ bounded with the required weighted sums.

The CN bounds $\|w\|_{\mathcal W_0}\le2C$,
$\|w\|_{\mathcal W_{4/3}}\le51C$ and
$\|v\|_{\mathcal W_0}\le C/32$, together with (EN.7), imply
$$
 \begin{aligned}
 K(w_-,c)
 &\le \iota\left\{\frac{67}{4}|\mu|C+
                                  \frac{131}{128}C^2\right\},\\
 |\mu|K(1,w)&\le\iota\,\frac{67}{4}|\mu|C .
 \end{aligned}
 \tag{EN.13}
$$
These bounds vanish when $C=0$. The independent physical mean rows have not been removed in obtaining them.

## 4. A two-space product-of-exponentials estimate

For bounded generators $A,B$ on $X=H^{-4/3}$ and $Y=L^2$, with
$[A,B]:X\to Y$ bounded, the exact identity is
$$
 \begin{split}
 e^Ae^B-e^{A+B}
  =\int_0^1\int_0^t&
 e^{(1-t)(A+B)}e^{(t-s)A}\\
 &\cdot[A,B]e^{sA}e^{tB}\,ds\,dt .
 \end{split}
 \tag{EN.14}
$$
Differentiate $e^{(1-t)(A+B)}e^{tA}e^{tB}$ and integrate. The two factors to the left of the commutator use their $Y$ norms; those to its right use their $X$ norms. This is a complete strong estimate, not a formal asymptotic expansion.

Apply this first with
$$
 A=-A_{w_-},\qquad B=A_c,\qquad D=A_w .
 \tag{EN.15}
$$
The homological equation gives exactly
$$
 A+B=\mu I-A_w,\qquad A+B+D=\mu I .
 \tag{EN.16}
$$
Split the full error as
$$
 \begin{split}
 e^Ae^Be^D-e^{\mu I}
 ={}&(e^Ae^B-e^{A+B})e^D\\
    &+(e^{A+B}e^D-e^{\mu I}).
 \end{split}
 \tag{EN.17}
$$

For the first term in (EN.17), the exponent from (EN.14), (EN.6)--8 and the final $e^D$ on $X$ is at most
$$
 \left\{\frac{1-t}{2}+\frac{t-s}{2}
               +\frac{51s}{4}+\frac t4+\frac{51}{4}\right\}C
 \le\frac{103}{4}C .
 \tag{EN.18}
$$
Here $A+B$ has scalar part $\mu I$ and perturbation $-A_w$; $B$ has scalar part $\mu I$ and perturbation $A_v$. Their norms are controlled by (EN.8), without a factor $e^{|\mu|/4}$.

For the second term, use the pair $A+B,D$. Their sum is the unitary generator $\mu I$, and their commutator is exactly
$$
 [A+B,D]=\mu[I,A_w].
$$
The remaining exponent is at most
$$
 \left\{\frac{t-s}{2}+\frac{51s}{4}+\frac{51t}{4}\right\}C
 \le\frac{51}{2}C .
 \tag{EN.19}
$$
The integration triangle has area $1/2$. Since both exponents are below $26C$, (EN.12)--13 prove
$$
 \left\|e^{-A_{w_-}}e^{A_c}e^{A_w}-e^{\mu I}\right\|_{X\to Y}
 \le e^{26C}\left\{
       \frac{67}{8}|\mu|C+\frac{131}{512}C^2\right\}.
 \tag{EN.20}
$$
All terms of the exponentials and all mean functionals are included.

## 5. The resulting exact scalar phase and strong bound

Rotation commutes with $I$, and
$U_\Omega^{-1}A_wU_\Omega=A_{w_-}$. Consequently (EN.4)--5 give
$$
 \mathcal T_{\exp}^{-1}\mathscr R\mathcal T_{\exp}
 =\zeta U_\Omega e^{\mu I}+\widetilde{\mathscr E}_{\exp}.
 \tag{EN.21}
$$
The transported original error is bounded by
$e^{53C/4}R_{\exp,0}$, using the $L^2$ inverse norm and the
$H^{-4/3}$ forward norm in (EN.6). Combining it with (EN.20) proves
$$
 \boxed{\quad
 \|\widetilde{\mathscr E}_{\exp}\|_{H^{-4/3}\to L^2}
 \le e^{26C}\left\{
      R_{\exp,0}+\frac{67}{8}|\mu|C+\frac{131}{512}C^2\right\}.
 \quad}
 \tag{EN.22}
$$
For every nonzero signed physical label,
$$
 e^{\mu I}e_j
       =e^{-i\mu/(4j)}e_j=e^{i\beta/j}e_j,\qquad
                    \beta=-\mu/4 .
 \tag{EN.23}
$$
Its constant-mode action is the identity. This is the actual scalar exponential used by the previously proved phase-divisor theorem, once the same accepted $\mu$ and selected-background scope are supplied.

When $C=0$, the normalizer is exactly the identity and the error in (EN.22) is just the directly supplied $R_{\exp,0}$. There is no independent scalar Taylor-replacement term because the hypothesis (EN.4) already contains the entire scalar exponential.

## 6. Why the existing linear-reference fee remains valid

Suppose instead that only the original linear-reference identity has been paid:
$$
 \mathscr R=\zeta U_\Omega(\operatorname{Id}+A_c)
                      +\mathscr E_{\rm lin}.
 \tag{EN.24}
$$
Then the required exponential-reference error is exactly
$$
 \mathscr E_{\exp}
   =\mathscr E_{\rm lin}
       -\zeta U_\Omega(e^{A_c}-\operatorname{Id}-A_c).
 \tag{EN.25}
$$
An upper bound for $\|\mathscr E_{\rm lin}\|$ does not reveal cancellation in this difference. A triangle bound still pays the complete exponential tail, including the scalar quadratic term when $c$ is constant. Thus (EN.22) does not authorize dropping the $\mu^2/4$ term in CN, or replacing its $R_0$ by a smaller symbolically renamed number.

A new actual calculation may directly validate a trial and complete return against the reference in (EN.4), retaining signed quadratic terms before taking norms. Alternatively, it may bound the full signed difference (EN.25). Either route must retain the complete mean, source, branch, incoming, root, positive cutoff, finite-head, strict-region and actual-density contributions. Previously computed positive budget sums cannot recover a lost signed cancellation by subtraction of their upper endpoints.

The complete function target CT and its old mean references can supply $c$ and a rigorous value of $C$ without repeating the old scalar or ray computation. They do not automatically supply $R_{\exp,0}$.

## 7. Conditional use in the existing high criterion

If the same true phase-divisor and correct graph-domain assumptions of [GH](R133-supplement-quantitative-strong-return-inverse-and-core-high-block-gates.md) are paid, its existing base strong bound may use the right side of (EN.22) as a complete remainder constant. The associated high criterion still requires its actual numerical product to be less than one.

This note proves neither that criterion nor a value of $C$ or $R_{\exp,0}$. Higher Sobolev output bounds require the corresponding complete multiplier and commutator estimates at those orders; they are not granted by this base estimate alone. The actual physical finite border, noncommuting physical and phase projections, two independent body/cut outputs, both full physical means and the true parameter row remain as in GH.

The final nonlinear core, low/shell collar inputs, tail matching, and the README's fixed-metric visible family are unaffected pending obligations. This theorem identifies a rigorous alternative reference and its exact normalization cost; all new numerical validation remains confined to the public repository's own Actions.
