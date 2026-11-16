# R150: the eighth power of the entire transverse ideal lies in the original normalized rank-one ideal

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Original ideal and conclusion

In the normalized physical rank-one mean chart $y=v(s)$, keep the original seventeen equations
$$
I=(\mathcal F_1,\ldots,\mathcal F_{17})
\subset R=\mathbb Q[s,z_0,\ldots,z_{10}].
$$
The $z$ variables are the original polynomial binomial moment coordinates, not an enlarged equation family. Put
$$
\mathfrak n=(z_2,\ldots,z_{10}),\qquad
q_0=sF_+F_-E_8,\qquad
h_*=s^3F_+^2F_-^2E_8.
$$

Then
$$
\boxed{\mathfrak n^8\subseteq I.}
\tag{1.1}
$$
Every pure degree-eight normal monomial has an original seventeen-source identity with source moment degrees at most eighteen. By ideal multiplication this gives (1.1) for arbitrary elements of $\mathfrak n^8$; the bound eighteen is the bound for those degree-eight generators.

This strengthens the [normalized Bell eighth-power identity](R150-appendix-all-high-normal-source-cost8391-and-rank-one-bell-eighth-powers.md): it applies simultaneously to mixed products of all nine normal directions, not only powers of matched Bell remainders.

The statement concerns the same normalized rank-one ideal. It does not remove the mean-cone equations in the unrestricted original Jacobian problem.

## 2. The two whole-quadratic premises

The [completed relative-module theorem](R150-appendix-zero-projection61-and-complete-relative-nine-target-module25.md) proves
$$
h_*W\subseteq\operatorname{im}A,
\qquad W=\mathfrak n^2_{\le5},
$$
inside the original degree-at-most-three Macaulay source module. In particular, for every one of the 45 quadratic generators $a=z_i z_j$, $2\le i\le j\le10$, there are original source polynomials satisfying
$$
h_*a=\sum_{\nu=1}^{17}A_{a,\nu}\mathcal F_\nu,
\qquad \deg_m A_{a,\nu}\le3.
\tag{2.1}
$$
Multiplication by arbitrary ring elements gives $h_*\mathfrak n^2\subseteq I$.

A separate original statement at four fibers is
$$
\mathfrak n^2\subseteq I+(q_0).
\tag{2.2}
$$
This requires whole quadratic-normal fiber membership. It cannot be inferred merely by assuming that the matched Bell squares span all quadratic forms. Here the necessary stronger fiber statements have already been proved:

| Fiber | Original result used |
|---|---|
| $s=0$ | [Zero full critical theorem](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md), §5: the entire 4212-dimensional normal-square space belongs to the original degree-three source span |
| $F_+=0$ | [Plus full critical theorem](R150-appendix-rank-one-Pplus-means-complete-critical-classification.md), §4: $\ker\pi\subset\mathcal R$, with all 4212 high-normal coordinates |
| $F_-=0$ | [Minus full critical theorem](R150-appendix-rank-one-Pminus-means-complete-critical-classification.md), §4: the same complete original inclusion |
| $E_8=0$ | [Octic full critical theorem](R150-appendix-rank-one-E8-means-complete-critical-classification.md), §5: the same complete original inclusion |

These are linear-span statements in the original 6188-source dictionary. They establish every mixed quadratic $z_i z_j$, not only the nine diagonal squares, as an original fiber member with multiplier degree at most three.

For the algebraic fibers the statements hold over the original residue number fields. Lifting their coefficients to polynomial representatives modulo $F_+$, $F_-$ and $E_8$ preserves moment degree. The four parameter factors $s,F_+,F_-,E_8$ are pairwise coprime. Polynomial CRT therefore supplies, separately for every quadratic generator $a$,
$$
a=\sum_{\nu=1}^{17}D_{a,\nu}\mathcal F_\nu+q_0E_a,
\qquad
\deg_m D_{a,\nu}\le3,\quad \deg_m E_a\le5.
\tag{2.3}
$$
The remainder bound follows because the original equations have moment degree at most two, so the numerator before division by the parameter-only polynomial $q_0$ has moment degree at most five.

This proves (2.2) with actual original-source scope. No assertion that the remainders $E_a$ belong to $\mathfrak n^2$ is needed.

## 3. Ideal proof

In the quotient ring $R/I$, (2.2) says
$$
\mathfrak n^2\subseteq(q_0).
$$
Cubing this inclusion gives
$$
\mathfrak n^6\subseteq(q_0^3).
$$
Multiplying by $\mathfrak n^2$ and using
$$
q_0^3=h_*R_q,\qquad R_q=F_+F_-E_8^2\in\mathbb Q[s],
$$
gives
$$
\mathfrak n^8\subseteq q_0^3\mathfrak n^2
=R_qh_*\mathfrak n^2=0
\qquad\text{in }R/I,
$$
where the last equality is (2.1). This proves (1.1).

All ideal operations occur after the original sources have been supplied. The proof uses neither a parameter inverse nor a radical-membership replacement for a polynomial identity.

## 4. Explicit mixed-product source formula

For clarity, the original sources can be combined without leaving an implicit ideal-power step. Let $a_1,a_2,a_3,a_4$ be any four quadratic generators $z_i z_j$. Choose (2.3) for $a_1,a_2,a_3$, and choose (2.1) for $a_4$. Abbreviate
$$
D_{i,\nu}=D_{a_i,\nu},\quad E_i=E_{a_i},
\qquad A_{4,\nu}=A_{a_4,\nu}.
$$
The telescoping identity is
$$
\begin{aligned}
a_1a_2a_3-q_0^3E_1E_2E_3
={}&(a_1-q_0E_1)a_2a_3\\
&+q_0E_1(a_2-q_0E_2)a_3\\
&+q_0^2E_1E_2(a_3-q_0E_3).
\end{aligned}
$$
Multiplication by $a_4$ yields the exact original identity
$$
\boxed{
a_1a_2a_3a_4
=\sum_{\nu=1}^{17}
\left[
R_qE_1E_2E_3A_{4,\nu}
+a_4\left(
D_{1,\nu}a_2a_3
+q_0E_1D_{2,\nu}a_3
+q_0^2E_1E_2D_{3,\nu}
\right)
\right]\mathcal F_\nu.
}
\tag{4.1}
$$
The first source term has moment degree at most $15+3=18$. The three terms in the second group have moment degrees at most 9, 12 and 15, respectively. Every degree-eight monomial in the nine normal variables is a product of four such quadratics, so (4.1) supplies the stated degree-eighteen bound for all generators.

Setting all $a_i=b_r^2$, using the corresponding source identities by linearity, recovers the previous Bell eighth-power construction. Equation (4.1) also covers mixed products which cannot be presented as a single matched-direction eighth power.

The source coefficients in (4.1) are existence-level polynomial sources obtained from the completed module and fiber theorems. No expanded high-degree coefficient array is newly computed, and the degree-three cost 8391 is not assigned to these degree-eighteen source coefficients.

## 5. Scope and verified fiber references

The four source-scope proofs were reread in full for this deduction. Their exact repository blob identities are:

| Original fiber proof | Blob SHA |
|---|---|
| Zero | 289799f0017d6dd570e2236e9fa40da3d3da558a |
| Plus | a0365e4a3320d5c0dbe614ff635ca0b4d00a0b6f |
| Minus | 48e6d42923a2f81a3fc1462e51e2cee8ccce9f4b |
| Octic | b9126755e2bd029b272fe8ab84f7f7b2274c1201 |

Each fiber proof obtains the whole normal-square span by an exact dimension equality using all original source coordinates. No new numerical experiment is required to extract the 45 quadratic cases or apply CRT.

The coordinate change is a polynomial unit, so all identities transport back to the original moment coordinates. Constant equation normalizations likewise transport their original source coefficients.

This is a uniform nilpotence bound on the normal ideal in the normalized rank-one chart. It is not a statement that $\mathfrak n^6\subseteq I$, that a CRT remainder is normal-square, or that the unrestricted critical system has rank-one mean. Those would be separate conclusions requiring new premises.
