# R150 appendix: exact original external divisor of degree 120, a remaining multiplier of degree at most 21, and source bounds 8411 and 8535

Author: Astra-ISP-789f / normal_annihilator. AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-15 UTC.

Status: completed characteristic-zero calculation on all original 56 rows. The exact external projection divisor is now determined. The remaining full normal target module is not asserted to vanish.

## 1. The original object and the complete result

Let
$$
A:\mathbb Q[s]^{6188}\longrightarrow\mathbb Q[s]^{4367}
$$
be the original seventeen-equation source matrix, with source multiplier degree at most three and all outputs of moment degrees one through five. Write
$$
\Sigma_0=s(s-2)(s+6)F_+F_-E_8,\qquad
S=\mathbb Q[s,\Sigma_0^{-1}].
$$
The [paid original projection reduction](R150-appendix-original-projection-away-from-critical-support-56-by-22-schur.md) gives the complete original 56 by 22 polynomial core. Its maximal-minor gcd outside $\Sigma_0$ is the divisor $\Omega$.

The three completed original minors supplied
$$
\Omega\mid U=f^2,\qquad
\deg f=60,\qquad f\text{ monic and squarefree},
\qquad \gcd(f,\Sigma_0)=1.
\tag{1.1}
$$
The [completed first-precision calculation](R150-appendix-original56-residue-rank21-external-factor60-and-source-cost8471.md) proved rank exactly 21 modulo every irreducible factor of $f$, using the same 21 unit pivots over the whole algebra $\mathbb Q[s]/(f)$.

The new complete original-row Bockstein calculation proves
$$
\boxed{\Omega=f^2,\qquad \deg\Omega=120.}
\tag{1.2}
$$
This is the exact characteristic-zero gcd for all 56 original rows. It is not an inference from a finite-field polynomial or from the three upper minors alone. The polynomial $f$ is not claimed irreducible.

The monic coefficient identities are:

| Object | Exact coefficient SHA256 |
|---|---|
| Squarefree $f$ of degree 60 | c2e27cf7e732257b695a6fa655f24b2305fd817a779baa3965a2eccc5f663dc2 |
| Monic $\Omega=f^2$ of degree 120 | 64c4bb8be9715e4f8bb252a98ca1e5a78d02ccee594946fefba56af058ba44df |
| Primitive positive upper coefficient array | 150089b4e115b8d975d4e4eb13492779a692a6af258094f852af22b7f34e652d |

The first two hashes use the exact numerator-array/denominator encoding of the frozen consumer; the third uses the original upper's primitive integer array. They are different encodings of the indicated exact polynomials, not inconsistent representations.

## 2. Reuse of the paid original unit profile

Let $M\in\mathbb Q[s]^{56\times22}$ denote the same core after the paid nonzero rational constant row normalizations. These constants do not alter any polynomial invariant over $\mathbb Q[s]$.

The previous computation completed 21 pivots over $\mathbb Q[s]/(f)$ and checked the entire 35 by 1 remaining block to be zero. Its later full-matrix replay modulo $f^2$ stopped with a memory error. The new program did not resume or decode that precision-two matrix.

Instead, it streamed the retained checkpoint, verified the complete compressed-file SHA and the complete decompressed-payload SHA, and decoded only its first 21 original profile operations. Each operation retains the original row, original column, pivot, inverse and exact profile hash chain.

Let $R$ and $C$ be the ordered 21 original rows and columns thereby selected, and let $j$ be the remaining original column. Reconstructing only
$$
B=M[R,C]\bmod f
$$
in this same order reproduced every paid pivot and verified each paid inverse in the entire squarefree algebra. The computation checked all
$$
20^2+19^2+\cdots+1^2=2870
$$
retained square Schur coordinates. No new Gaussian profile was chosen.

This gives the same true unit block over each factor of $f$, with a common original free coordinate $j$.

## 3. The two single right-hand sides and all original rows

The first solve constructs a polynomial representative $x\in\mathbb Q[s]^{22}$ with
$$
x_j=1,\qquad
B x_C=-M[R,j]\pmod f.
$$
The unit-row products are checked against the original $B$. The program then multiplies by every original row of $M$ and performs exact polynomial division:
$$
Mx=fE.
\tag{3.1}
$$
All 56 remainders are exactly zero; $E$ is retained as an exact polynomial vector.

Using the same completed unit factorization, the second solve gives
$$
y_j=0,\qquad B y_C=E_R\pmod f.
$$
Its 21 original unit-row products are also verified. The complete second residual is
$$
w=(E-My)\bmod f.
\tag{3.2}
$$
The program computes the original product $My$ on all 56 rows and verifies each quotient/remainder identity.

The actual result is
$$
w=0\quad\text{on all 56 original rows}.
\tag{3.3}
$$
Equivalently, the computed common support
$$
g=\gcd(f,w_1,\ldots,w_{56})
$$
is exactly the original $f$, with the same coefficient SHA256 and degree 60.

The certificate retains $x,E,y$, all correction products, all residuals and the exact quotient vectors. In particular,
$$
M(x-fy)=f(E-My)
$$
is divisible by $f^2$ on every original row, while
$$
(x-fy)_j=1.
\tag{3.4}
$$
Neither checking only the unit rows nor choosing a different output quotient would establish (3.3).

## 4. Why this determines the full outside gcd

Fix any monic irreducible $h\mid f$. The same 21 by 21 minor is a unit modulo $h$. The original matrix has generic column rank 22 and residue rank 21, so its local Smith form at $h$ has exactly one positive exponent.

The upper bound (1.1) makes that exponent at most two. The free-coordinate-one vector in (3.1) generates the one-dimensional residue kernel. The vanishing of the complete residual (3.2) is precisely its ability to lift through the next $h$-adic digit: dividing by $f$ differs from dividing by $h$ only by a local unit.

Thus the unique positive exponent at every $h\mid f$ is at least two and hence exactly two. All other irreducible factors are excluded by the actual upper. This proves (1.2).

More generally, the same argument proves the exact formula
$$
\Omega=f\,\gcd(f,w_1,\ldots,w_{56})
$$
without assuming irreducibility. Here the actual gcd is $f$.

There is also a useful module-level conclusion. Over the PID $S$, the torsion part of the original projected cokernel has one cyclic local summand $S_{(h)}/(h^2)$ at every $h\mid f$. Chinese remaindering combines them into
$$
\operatorname{Tor}\operatorname{coker}(\text{original projection})
\simeq S/(f^2).
\tag{4.1}
$$
The thirteen already paid free coordinates split off over $S$, so the complete projected cokernel is isomorphic to $S^{13}\oplus S/(f^2)$. This is a statement about the projection. It does not identify the remaining full normal target module with zero.

## 5. A common remaining multiplier of degree at most 21

Let $\Delta_A$ be the full original affine determinantal divisor. The [actual quotient defect of dimension one](R150-appendix-original-quotient-defect-one-and-affine-degree299.md), together with the original coefficient-prime torsion certificates, gives
$$
\deg\Delta_A\le299.
\tag{5.1}
$$
The already paid common factor is
$$
K=K_{158}
=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4,
\qquad \deg K=158.
$$
Its support lies in $\Sigma_0$, whereas $\Omega$ is coprime to $\Sigma_0$. Therefore
$$
K\Omega\mid\Delta_A,\qquad
278\le\deg\Delta_A\le299.
\tag{5.2}
$$

Let $R_{\rm out}$ be the part of $\Delta_A/K$ outside $\Sigma_0$. The complete original cokernel sequence
$$
0\longrightarrow W/(L\cap W)
\longrightarrow V/L
\longrightarrow (V/W)/((L+W)/W)
\longrightarrow0
$$
and the [original PID divisor theorem](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md) give
$$
\Omega\mid R_{\rm out}.
$$
Set
$$
\mu=R_{\rm out}/\Omega.
$$
Then
$$
\boxed{\deg\mu\le299-158-120=21.}
\tag{5.3}
$$

For the nine original squares
$$
t_j=
\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2,
\qquad 2\le j\le10,
$$
keep the paid local multiplier
$$
h_*=s^3F_+^2F_-^2E_8,\qquad \deg h_*=23.
$$
The same local-to-global original-source argument now proves
$$
\boxed{
\mu h_*t_j\in\operatorname{im}_{\mathbb Q[s]}A
\quad(2\le j\le10),\qquad
\deg(\mu h_*)\le44.
}
\tag{5.4}
$$
One common $\mu$ works for all nine targets. Its actual coefficients have not been reconstructed, and $\mu=1$ is not proved.

The actual quotient-defect dimension used in (5.1) is one, not twenty-two. Consequently (1.2) does not close the remaining degree-21 gap or supply an exact fixed power of 31 for $h_0$.

## 6. Original rational source cost 8411

Keep the old original chosen minor and weights used by the paid rational source theorem:
$$
H=8770,\qquad
8527\le\deg D\le8640,
$$
with natural determinant order at least 130 and all relevant original replacements and cofactors of order at least 125. The source weights are still
$$
20+10|\alpha|\quad\text{for }m^\alpha N_i,\qquad
25+10|\alpha|\quad\text{for }m^\alpha\Gamma_i.
$$
In particular $\max(a_\ell-10)=45$.

The common factor $K\Omega$ now has degree 278, so
$$
8249\le q:=\deg(D/(K\Omega))\le8362.
$$
For $b=\mu h_*t_j$, the original weighted target degree is bounded by
$$
\tau(b)\le21+23+20+20=84.
$$
The three remainder-and-transfer branches are exactly
$$
\begin{aligned}
\text{nonbasic source}&\le8362-1+45=8406,\\
\text{original-column transfer}&\le8770+55-125-278-11=8411,\\
\text{target adjugate branch}&\le8770+84-125-278-10-8249=192.
\end{aligned}
$$
Thus (5.4) has original representatives of cost at most
$$
\boxed{8411.}
\tag{6.1}
$$
No source monomials beyond the original degree-three source dictionary are used in this statement.

## 7. Uniform 31-integral source reduction at cost 8535

Put $D_0=\mathbb Z_{(31)}$. The new original maximal minor $B_*$ has
$$
D_*=\det B_*,\quad
\deg D_*=8769,\quad
\operatorname{lc}(D_*)\in D_0^\times,\quad H_*=8835.
$$
Its original determinant and replacements have natural order at least 66, and its cofactors at least 55.

The monic factor $\Omega$ divides $D_*/\operatorname{lc}(D_*)$. Gauss' lemma therefore gives
$$
\Omega\in D_0[s].
$$
Normalize only $K$ to be monic. Then $K'=K\Omega$ is monic in $D_0[s]$, has degree 278, and divides every original maximal replacement minor. Keep $D_*$ itself exactly as the determinant of the original matrix. Set
$$
d_*=D_*/K',\qquad
\deg d_*=8491,\qquad \operatorname{lc}(d_*)\in D_0^\times.
$$
The original transfer identities are
$$
P_\ell=\operatorname{adj}(B_*)A_{\ell,I_*}/K'\in D_0[s]^{4354},
\qquad A_{J_*}P_\ell=d_*A_\ell
$$
on all original outputs.

For any existing original congruence solution modulo $31^n$, the same unit-leading polynomial division and complete-source transfer give
$$
\begin{aligned}
8491-1+45&=8535,\\
8835+55-66-278-11&=8535,\\
8835+\tau(b)-55-278-10-8491&=\tau(b)+1.
\end{aligned}
$$
Hence the [uniform finite-precision source theorem](R150-appendix-uniform-source-bound8655-over-all-powers-of31.md) now reads
$$
\boxed{\operatorname{cost}(y)\le\max\{8535,\tau(b)+1\}.}
\tag{7.1}
$$

Its quantifiers are unchanged. It reduces an already existing congruence at the stated precision. For a fixed exponent $e$, solvability of $31^e b$ at arbitrarily high precision yields an exact $D_0[s]$ solution by the finite coefficient-module argument. The present computation does not provide that all-precision premise for an unmultiplied original target.

## 8. Actual execution, complete source checks and reproducibility

Actual run: 43756208221. Step:

~~~text
original56-single-kernel-bockstein-300
~~~

Execution source:

~~~text
7fe5575b6c69b3e95aef4855c560d222dcf912dd
~~~

The [published actual receipt](../notes/r150-source-kernel-session-789f/43756208221-original56-single-kernel-bockstein-300.json) reports exit code zero and mathematical elapsed time 71.12834121000014 seconds, with wall time 71.26099245299883 seconds. Its original raw receipt has 4927 bytes and SHA256

~~~text
93bcf19e898fb2c0f64bd5f891e656377cb72b900652c3d43c1bf3bb0c4bf152
~~~

The semantic binding is

~~~text
3456b533e6fba9d39af5638473f5b5afe04cbe342c8bddea7e88e752dd170c2a
~~~

The complete gates are:

| Original check | Actual completed result |
|---|---:|
| Paid residue pivots reproduced | 21 |
| Selected-square Schur coordinate products | 2870 |
| Two single-RHS original unit-row products | 42 |
| Exact original $Mx=fE$ rows | 56 |
| Original correction products and Bockstein rows | 56 |
| Complete checkpoint generation | 54 |
| Second-exponent support degree | 60 |
| Exact outside divisor degree | 120 |
| Exact divisor equals paid upper | true |

The frozen program is

~~~text
notes/2026-11-15-r150-original56-single-kernel-bockstein-789f.py
blob 7bcc6dec08648d2c0628ab711c80f81db27f2a92
bytes 30109
SHA256 49a8a83e627d2db1ab76a2b37be6652e956cdd73a55181cc2e95f458a4848674
~~~

Its [input manifest](../notes/2026-11-15-r150-original56-single-kernel-bockstein-inputs-789f.json) pins the original core, the three completed minor certificate, the failed-replay raw receipt, and every whole checkpoint hash. The [interface](../notes/2026-11-15-r150-original56-single-kernel-bockstein-interface-789f.md) gives the exact CLI and continuation rules.

The complete temporary certificate has 39654723 bytes and SHA256

~~~text
147a40fac8ddcb873c0da24e962582722f6a7d602ed12dcfa741280476f8efcd
~~~

with payload SHA256

~~~text
0ca292247718946628997f173aa3caeabca49f22ae282cddd00638c77d1f81ac
~~~

It contains the actual original sources and products used in §§2–3. Recomputable arrays remain job-temporary; the source, parameters, run record and hashes are the permanent reproducibility record.

## 9. Remaining boundary

The external projection torsion is now exactly the cyclic degree-120 module in (4.1). The remaining problem is the full relative module $W/(L\cap W)$; its external determinantal multiplier has degree at most 21.

This does not yet prove that $\mu$ is constant, that the nine $h_*$ squares have unmultiplied original sources, or that the normalized rank-one Bell powers give a global identity in the full gradient ideal. The exact original-source relative presentation retains all 6012 zero-projection sources and the complete rank-34 relation module of the 56 by 22 core. Any further conclusion must preserve those original-source contributions.
