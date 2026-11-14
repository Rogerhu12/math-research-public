# R133 supplement: a uniform complete two-port Airy kernel below 32

2026-11-13, visible-exact / phase_inverse. **Status: proved.**

For the complete canonical two-state system

$$
 U_T=J(T)U_X+f,\qquad J(T)=\begin{pmatrix}0&T\\-1&0\end{pmatrix},
 \quad -d_-\le T\le d_+,
 \tag{A.1}
$$

take one incoming port on the negative boundary and one unstable Airy
coefficient on the positive boundary, exactly as defined in
[the actual fold theorem](R133-supplement-actual-physical-fold-and-full-Airy-collar.md),
Section 6. The complete Green kernel and each of the two Poisson columns
have common bound 32 in the full Airy two-state weights, for every
nonzero physical frequency $m\in4\mathbb Z$ and every finite positive
$d_-,d_+$. The two mean equations have kernel and column bounds at most
one and are included separately.

This improves the deliberately coarse $2^{25}$ constant of that theorem.
It changes neither the reference equation, its source unit, its input
ports, nor its two complete state components.

## 1. State, source, and the two different radial orientations

For $m\ne0$, the second state $u=U_{2,m}$ solves
$u_{TT}=m^2Tu$, and $U_{1,m}=iu_T/m$. Put

$$
 \omega_m(T)=(|T|+|m|^{-2/3})^{1/2},\qquad
 D_m(T)=\operatorname{diag}(\omega_m^{-1/2},\omega_m^{1/2}).
 \tag{A.2}
$$

On the positive side use $x=|m|^{2/3}T$ and on the negative side use
$x=-|m|^{2/3}T$. The equations are respectively $u_{xx}=xu$ and
$u_{xx}+xu=0$. **Their root derivatives have opposite signs.** If the
positive-side initial data are $(u(0),u_x(0))$, the negative scalar
equation starts from $(u(0),-u_x(0))$.

In either orientation the full state $D_mU$ is a unitary permutation
and phase change of

$$
 |m|^{-1/6}\operatorname{diag}((1+x)^{1/4},(1+x)^{-1/4})(u,u_x).
 \tag{A.3}
$$

The common factor cancels from two-state kernels and normalized port
columns. The change of variable is used only to prove matrix bounds;
the Green kernel in (A.1) integrates the original ordinary source in
$dT$. No factor $|m|^{2/3}$ is dropped from or added to the source.

## 2. Two exactly normalized real Airy solutions

For $x\ge1$, let $Z=(x^{1/4}u,x^{-1/4}u_x)$ and
$a_1=(Z_1+Z_2)/\sqrt2$, $b_1=(Z_1-Z_2)/\sqrt2$.
On the positive side,

$$
 a_1'=\sqrt x\,a_1+\epsilon b_1,\qquad
 b_1'=\epsilon a_1-\sqrt x\,b_1,\qquad \epsilon=(4x)^{-1}.
 \tag{A.4}
$$

The stable solution $A$ is constructed by imposing $a_1/b_1=0$ at
$x=R$ and passing to $R\to\infty$. Its ratio equation

$$
 r'=2\sqrt x\,r+\epsilon(1-r^2)                         \tag{A.5}
$$

leaves $[-1/4,0]$ invariant backward. Differences contract backward
since their coefficient is $2\sqrt x-\epsilon(r_1+r_2)>0$.
This proves the limit and uniqueness of the stable line. Normalize
$b_1(1)=1$, and denote its actual ratio at 1 by $r_A$. Thus

$$
 r_A\in[-1/4,0],\qquad
 A(1)=\frac1{\sqrt2}(1+r_A,r_A-1).
 \tag{A.6}
$$

The growing solution $B$ is fixed by $(a_1(1),b_1(1))=(1,0)$, so
$B(1)=(1,1)/\sqrt2$. Its ratio $b_1/a_1$ stays in $[0,1/4]$ forward.
The stable $b_1$ decreases and the growing $a_1$ increases on $[1,\infty)$.

For every possible $r_A$ in (A.6), their scalar Wronskian is exactly

$$
 \det(A,B)=1.                                          \tag{A.7}
$$

This follows by evaluation at 1 and is preserved by the scalar ODE.
The negative coordinate reverses its sign, while its modulus remains
one. No bound for the unknown stable ratio replaces this exact identity.

## 3. Complete root data from exact convergent series

For either scalar equation $u''=\varepsilon xu$, $\varepsilon=\pm1$,
the two power-series fundamental columns have initial data $(1,0)$ and
$(0,1)$ and recurrence

$$
 c_n=\frac{\varepsilon c_{n-3}}{n(n-1)},\qquad n\ge3.
 \tag{A.8}
$$

The native calculation sums through degree 48 at $x=1$. For the first
omitted nonzero index $n_0$, successive omitted absolute values have
ratio at most $1/((n_0+3)(n_0+2))$, and their derivative terms have
ratio at most $1/(n_0(n_0+2))$. Therefore the two complete tails are
bounded by

$$
 \frac{|c_{n_0}|}{1-1/((n_0+3)(n_0+2))},\qquad
 \frac{n_0|c_{n_0}|}{1-1/(n_0(n_0+2))}.                 \tag{A.9}
$$

Let $F_+$ and $F_-$ be these complete scalar fundamental matrices at
1, both based at 0. Their determinants are exactly one because the
two-state matrices have trace zero. The inverse of $F_+$ is therefore
its cofactor matrix, with the complete directed entry intervals.
The positive root states are

$$
 A_0=F_+^{-1}A(1),\qquad B_0=F_+^{-1}B(1).             \tag{A.10}
$$

Every evaluation retains the entire interval $r_A\in[-1/4,0]$.
For the negative energy at $x=1$ the exact states are

$$
 A_{-,1}=F_-\operatorname{diag}(1,-1)A_0,
 \qquad B_{-,1}=F_-\operatorname{diag}(1,-1)B_0.          \tag{A.11}
$$

The executed native bounds prove $A_{0,1}>0$, $A_{0,2}<0$ and both
components of $B_0$ positive. In particular

$$
1.81531501<\|A_0\|<2.37801385,\qquad
0.4878941233<\|B_0\|<0.4878941235.                      \tag{A.12}
$$

All of (A.8)--(A.12) use directed Arb arithmetic and explicit infinite
tails. No sampled Airy values or floating asymptotics are used.

## 4. Global negative and positive weighted bounds

On $0\le x\le1$ for the negative equation, the largest logarithmic
norm is $(1-x)/2$. Hence the propagator and its inverse have norm at
most $e^{1/4}$. The $(1+x)$ weights add a factor at most $2^{1/4}$.

For $x\ge1$ define

$$
 S(x)=\begin{pmatrix}1&e(x)\\e(x)&1\end{pmatrix},\quad
 e(x)=(4x^{3/2})^{-1},\quad E_Z=Z^*SZ.
$$

As in the preceding fold theorem, $M^*S+SM=0$ and
$\int_1^\infty |e'|/(1-e)=\log(4/3)$. If $E_1$ is the exact
energy at 1, then

$$
 \frac34E_1\le E_Z(x)\le\frac43E_1.
 \tag{A.13}
$$

Combining the eigenvalue bounds $3/4\le S\le5/4$ and the
$(1+x)/x$ weight comparison gives the sufficient global estimates

$$
 \frac{3}{5\sqrt2}E_1\le
 \|\operatorname{diag}((1+x)^{1/4},(1+x)^{-1/4})(u,u_x)\|^2
 \le\frac{16\sqrt2}{9}E_1\quad(x\ge1).                 \tag{A.14}
$$

The negative-side states (A.11) supply the complete directed $E_1$
bounds. Denote the resulting negative-side upper/lower norms by
$A_-^+,A_-^-,B_-^+$. The native calculation proves

$$
 A_-^->1.18883307,\quad A_-^+<4.72728903,\quad B_-^+<0.82867210.
 \tag{A.15}
$$

On the positive interval $[0,1]$, the two absolute components of $A$
decrease forward: $u>0,u'<0,u''=xu\ge0$, with these signs continued
backward from (A.6). The two components of $B$ increase forward,
starting from the strictly positive values in (A.12).
For $x\ge1$ the cone estimates from (A.4) apply. They give

$$
 A_+^+:=\sup_{x\ge0}\|W(x)A(x)\|<2.82795099,
 \qquad B_+^-:=\inf_{x\ge0}\|W(x)B(x)\|>0.41026841,
 \tag{A.16}
$$

where $W(x)=\operatorname{diag}((1+x)^{1/4},(1+x)^{-1/4})$.

The causal positive products also have a uniform bound. For
$x\ge y\ge1$, the stable forward ratio and the exact Wronskian give
$\|Z_A(x)\|\|Z_B(y)\|\le17/15$; the reversed growing/stable product
has the same bound when $x\le y$. After the $(1+x)$ weight comparison
this is at most $\sqrt2\,17/15$.
On $[0,1]$ the bound is $\sqrt2\|A_0\|$, and when the two points
straddle 1 it is at most $\sqrt2\sqrt{17}/4$.
Their maximum, denoted $P_+$, satisfies

$$
 P_+<3.36301944.                                        \tag{A.17}
$$

## 5. Both boundary conditions in the same exact kernel

At the negative boundary let
$\mathfrak i(U)=((D_mU)_1+(D_mU)_2)/\sqrt2$.
Both real scalar solutions $A,B$ are isotropic for the conserved
Hermitian flux $U^*\Sigma_1U$, since their two physical state components
are respectively purely imaginary and real. Thus
$|\mathfrak i(A)|=\|D_mA\|/\sqrt2$, and likewise for $B$.

Put

$$
 c=\mathfrak i(B)/\mathfrak i(A),\qquad C=B-cA.
 \tag{A.18}
$$

Then $C$ has zero negative incoming port, $A$ has zero positive
unstable port, and $\det(A,C)=\det(A,B)$ still has modulus one
in the scalar weights. The same common frequency factor in (A.3)
cancels from each Green product. Moreover

$$
 |c|\le B_-^+/A_-^-=:c_+<0.69704664,
 \quad\|C\|_{-,\infty}\le B_-^++c_+A_-^+=:C_-^+<4.12381300.
 \tag{A.19}
$$

The zero-port Green kernel is the usual exact two-state fundamental
kernel: for $T\ge S$ it uses the stable column $A(T)$ and the row
dual to $A(S)$ in the $(A,C)$ basis; for $T\le S$ it uses the
negative of the $C(T)$ column and its dual row at $S$.
The dual row norms in dimension two are the norm of the other column
divided by the absolute determinant. Thus all of its cases are bounded
by

$$
 K_G=\max\{A_-^+C_-^+,\ A_+^+C_-^+,\ P_++c_+(A_+^+)^2\}.
 \tag{A.20}
$$

The first term treats both points negative, the second both mixed
orders, and the third both positive orders. The latter uses
$C=B-cA$ before estimating, so it never bounds the growing positive
column at an inappropriate later time.

For negative incoming data, the Poisson column is
$A/\mathfrak i(A)$, with bound

$$
 K_-\le\sqrt2\max(A_-^+,A_+^+)/A_-^-.
 \tag{A.21}
$$

For positive unstable input, normalize $B$ to unit balanced norm at
the positive boundary. The column is $C/\|B(d_+)\|$.
The increasing positive $B$ cone and the weights show that
$\|B(T)\|/\|B(d_+)\|\le2$ for $0\le T\le d_+$.
Therefore

$$
 K_+\le\max\{C_-^+/B_+^-,\ 2+c_+A_+^+/B_+^-\}.
 \tag{A.22}
$$

This input is a growing coefficient normalized at its actual endpoint,
not the inverse of an exponentially small transmission value.

All native comparisons, with their complete series tails and stable
ratio interval, give

$$
 \boxed{\quad K_G<19.494456,\qquad K_-<5.623495,
                 \qquad K_+<10.051500.\quad}             \tag{A.23}
$$

Thus a common complete kernel and column bound is 32. At $m=0$ solve
$U_0'=f_0$, prescribing $U_{1,0}$ at the left and $U_{2,0}$ at the
right. Its kernels and two columns are bounded by one, with both
complementary means retained as outputs. This proves the assertion
on the entire Fourier space.

## 6. Execution and correction of the initial orientation attempt

The proof producer is
`scripts/fourfold_full_two_port_Airy_universal_v2.py`, and the executed
report is `notes/2026-11-13-R133-universal-two-port-Airy-v2-native.json.gz`.
All nine gates passed. The report explicitly records
`negative_root_derivative_exact_reflection=true` and both complete
fundamental matrices and their infinite-tail fees.

Reproduction uses

```sh
python3 scripts/fourfold_full_two_port_Airy_universal_v2.py \
  --out /tmp/universal-two-port-Airy-v2-native.json.gz
```

The report SHA-256 is
`1e5b5436f35c46e1c760c7385754867db6a28e7bd89d1a66700a069908608921`.
The first unpublished orientation attempt omitted the reflection in
(A.11). Its intervals were finite but did not represent the same
negative continuation. It is excluded, together with any intermediate
consumer of it; the correction record is
`notes/2026-11-13-R133-Airy-orientation-attempt-correction.json`.
Only the present v2 report is a certified source for the bound 32.
