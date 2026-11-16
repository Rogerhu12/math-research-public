# R904 — Original six-channel Wronskians and six-torsion vanishing sequences

Date: 2026-11-16. Session: serre-public-astra-20261115 / sigma_uniform.

**Status: proved.** For every original theta weight $5\le r<p$, the ordinary $D$-Wronskian of its six actual sections is nonzero. Its common ramification weight at the thirty-six marked six-torsion points is at most $p$; at $r=5$ its entire divisor is exactly $pE_0[6]$. For $r\ge6$ the weight has an exact description by the last six independent original sigma coefficient rows. These results constrain the full vanishing sequence, but do not prove intersection of the two required complementary supports or nonvanishing at a primitive, Legendre-visible label.

## 1. The unchanged curve, field, and actual operators

Use exactly R889 and R891:
$$
p=6N+5\ge41,\qquad k=\mathbf F_{p^2},\qquad
E_0:y^2=x^3-1,\qquad \omega=\frac{dx}{2y},\qquad D=\frac d\omega.
\tag{904.1}
$$
Write $K=k(E_0)$, $L_m=O_{E_0}(mO)$, and retain the compatible rational sections $s_as_b=s_{a+b}$. The six-dimensional source has the original ordered rational basis
$$
(f_0,f_1,f_2,f_3,f_4,f_5)=(1,x,y,x^2,-xy,x^3).
\tag{904.2}
$$
The actual theta distribution and its vacuum are
$$
\kappa=-6B\in\mathbf F_p^\times,\qquad
Q=q+\kappa^{-1}d_p,\qquad
q=-B^{-1}D^{p-2}x,\qquad Dq=1,
$$
$$
\mathcal H_0=\{f^p s_{6p}:f\in H^0(E_0,L_6)\},\qquad
V_r=Q^r\mathcal H_0\quad(0\le r<p).
\tag{904.3}
$$
Here $d_p$ is the coefficient of the actual translation in R889's CM parameter $Y$; it is not $D^p/p!$. In particular
$$
d_pq=B^{-1}x^p,\qquad
d_p(q^j f^p)=jB^{-1}x^p q^{j-1}f^p+q^j(Df)^p
\quad(0\le j<p).
\tag{904.4}
$$
This precise restricted product rule, not a global assertion that $d_p$ is a derivation, is used below.

The constant field of $D$ is
$$
C=\ker(D:K\to K)=K^p.
\tag{904.5}
$$
Indeed $[K:K^p]=p$: the degree-two separable presentation over $k(x)$ and its Frobenius image give this directly. Since $Dq=1$, $q\notin K^p$ and
$$
K=C\oplus Cq\oplus\cdots\oplus Cq^{p-1}.
\tag{904.6}
$$
On this basis $D(q^j)=jq^{j-1}$, so its kernel is exactly $C$.

Let $\partial=d_p|_C$ and $\xi=B^{-1}x^p\in C$. The Hasse product rule on $p$th powers gives
$$
\partial(f^p)=(Df)^p,
$$
and $\partial$ is a derivation of the field $C$. Equation (904.4) says, for every polynomial of $q$-degree less than $p$,
$$
d_p\!\left(\sum_j a_jq^j\right)
=\sum_j\bigl((\partial a_j)q^j+j\xi a_jq^{j-1}\bigr).
\tag{904.7}
$$
The restriction is essential: $d_p(q^p)=1$, whereas applying a formal derivation to $q^p$ would give zero.

## 2. The highest six polynomial coefficients

For $c\in C$ and $0\le r<p$, (904.7) gives a unique expansion
$$
Q^rc=\sum_{j=0}^r q^{r-j}A_{r,j}(c),\qquad A_{r,j}(c)\in C.
\tag{904.8}
$$
Its degree is at most $r$, so no reduction of $q^p$ occurs. Extend $A_{r,j}$ by zero outside $0\le j\le r$. The exact recurrence is
$$
A_{r+1,j}
=A_{r,j}+\kappa^{-1}\partial A_{r,j-1}
+\kappa^{-1}(r-j+2)\xi A_{r,j-2}.
\tag{904.9}
$$
It follows by induction that
$$
A_{r,j}(c)
=\binom rj\kappa^{-j}\partial^jc
+\sum_{a=0}^{j-2}u_{r,j,a}\partial^ac,
\qquad u_{r,j,a}\in C.
\tag{904.10}
$$
For $j=0,1$ the sum is empty. For the induction, the first two terms of (904.9) give the leading coefficient through Pascal's identity. The third term has differential order at most $j-2$, and differentiating a lower-order term from $A_{r,j-1}$ still has order at most $j-2$. This also explains why the noncommuting correction involving $\xi$ has not been discarded.

For $5\le r<p$, form the matrix of the highest six coefficients of the six sections:
$$
\mathsf A_r=\bigl(A_{r,j}(f_a^p)\bigr)_{0\le j,a\le5}.
$$
Equation (904.10) expresses it as a lower triangular matrix times
$\bigl((D^jf_a)^p\bigr)_{j,a}$. Therefore, if
$$
W_{\rm orig}=\det(D^jf_a)_{0\le j,a\le5}\in K,
$$
then
$$
\boxed{
\det\mathsf A_r
=\kappa^{-15}\left(\prod_{j=0}^5\binom rj\right)
 W_{\rm orig}^{\,p}.
}
\tag{904.11}
$$
Every binomial coefficient here is nonzero: $5\le r<p$ and $0\le j\le5$. It remains to check the actual original Wronskian, rather than presupposing six independent derivatives.

## 3. The original degree-six Wronskian

For a line bundle $L$ on this elliptic curve, the ordinary six-column Wronskian of six sections is a section of $L^{\otimes6}$. The invariant differential trivializes the additional canonical-bundle factor. In a local frame, replacing every coefficient by its product with a unit changes the derivative matrix by a triangular matrix, whose determinant is the sixth power of that unit. Thus the local Wronskians glue.

The vector field $D$ has no zero or pole anywhere on $E_0$: it is dual to the nowhere-vanishing invariant differential. Consequently its action on a regular local series lowers order by at most one.

For the complete original series $H^0(E_0,L_6)$, the vanishing sequence at $O$ is
$$
0,1,2,3,4,6.
\tag{904.12}
$$
For example, in the local frame $s_6/Y^6$, the rational sections
$x^3,-xy,x^2,y,x,1$ have exactly these orders, with nonzero leading coefficients. The six distinct exponents are distinct modulo $p$. The leading determinant is their Vandermonde determinant times the product of those coefficients. Hence
$$
\operatorname{ord}_O\bigl(W_{\rm orig}s_6^6\bigr)
=(0+1+2+3+4+6)-(0+1+2+3+4+5)=1.
\tag{904.13}
$$
In particular $W_{\rm orig}\ne0$.

The original six-primary theta group preserves the complete series $H^0(E_0,L_6)$. Translation by any $A\in E_0[6]$ transports its Wronskian divisor to itself. This follows either from the local triangular transformation just described and translation invariance of $D$, or directly from functoriality of the jet determinant. Thus every one of the thirty-six points of $E_0[6]$ has the same order one as $O$.

The Wronskian line bundle is $L_6^6=O(36O)$, of degree thirty-six. There are no further zeros:
$$
\boxed{
\operatorname{div}\bigl(W_{\rm orig}s_6^6\bigr)
=\sum_{A\in E_0[6]}[A].
}
\tag{904.14}
$$
This also gives the rational-function identity for its divisor,
$\operatorname{div}(W_{\rm orig})=\sum_{A\in E_0[6]}[A]-36[O]$.
An explicit division-polynomial normalization is not needed.

## 4. Nonzero ordinary Wronskians of all actual weights $r\ge5$

For $5\le r<p$, (904.11) proves that the six polynomials
$Q^r f_a^p$ are linearly independent over the full constant field $C$. Their ordinary $D$-Wronskian is therefore nonzero.

For completeness, the differential-field criterion used here holds over the actual kernel of the derivation, in any characteristic. If a minimal independent family has zero Wronskian, divide its columns by a nonzero first member. The first resulting column is $1$. The determinant of the derivatives of the remaining ratios is zero. Induction supplies a constant linear relation between those derivatives; integrating the relation means that the same linear combination of the ratios is in the constant field, contradicting minimal independence. No factorial division or characteristic-zero assumption is used in this argument.

Define
$$
\mathcal W_r=
 \det\bigl(D^jQ^r(f_a^p)\bigr)_{0\le j,a\le5}s_{6p}^6.
\tag{904.15}
$$
It is the actual Wronskian of $V_r$, not an independent scalar equation imposed on the original sigma functions. Since $L_{6p}=F^*L_6^{(p)}$, its Cartier connection is regular and has
$D(Rs_{6p})=(DR)s_{6p}$ in this rational frame. In the local frame
$\epsilon_{6p}=s_{6p}/Y^{6p}$, the factor $Y^{6p}$ is horizontal. Thus (904.15) agrees with the ordinary local coefficient Wronskian. It is a global section of
$$
L_{6p}^6=O(36pO).
\tag{904.16}
$$
Its zero divisor consequently has total degree $36p$.

R889/R891 show that every $V_r$ is preserved by the actual six-primary theta group. The same jet-determinant argument as in §3 proves that the order of $\mathcal W_r$ is equal at all points of $E_0[6]$. Put
$$
w_r=\operatorname{ord}_O(\mathcal W_r).
$$
Then
$$
\boxed{
\mathcal W_r\ne0,\qquad
\operatorname{div}(\mathcal W_r)\ge
 w_r\sum_{A\in E_0[6]}[A],\qquad
0\le w_r\le p
\quad(5\le r<p).
}
\tag{904.17}
$$
The inequality uses the actual degree $36p$. It is not obtained by applying characteristic-zero ramification formulae outside their range.

## 5. The exact boundary $r=5$

For $r=5$, the six polynomial columns in (904.8) have degree at most five. Taking their ordinary $q$-Wronskian multiplies the determinant of their ascending coefficient matrix by $\prod_{j=0}^5j!$. Reversing the six rows of (904.11) contributes $(-1)^{15}=-1$. Therefore
$$
\boxed{
\mathcal W_5
=c_5\bigl(W_{\rm orig}s_6^6\bigr)^p,\qquad
c_5=-\kappa^{-15}
 \prod_{j=0}^5\left(j!\binom5j\right)\in\mathbf F_p^\times.
}
\tag{904.18}
$$
The line-bundle factors match because $s_{6p}^6=(s_6^6)^p$. Formula (904.14) now gives the complete divisor:
$$
\boxed{
\operatorname{div}(\mathcal W_5)
=p\sum_{A\in E_0[6]}[A],\qquad w_5=p.
}
\tag{904.19}
$$
Both the multiplicity $p$ and the sign of the displayed constant follow from the actual polynomial coefficient matrix. No arbitrary normalization of the theta distribution was made.

The low weights also illustrate why ordinary Wronskians must not be used before $r=5$. For $r<5$, all six polynomials in (904.8) have degree at most four, and their six-column ordinary Wronskian is identically zero.

There is nevertheless an exact ordinary vanishing sequence at $O$ for each of these low spaces:
$$
\begin{array}{c|l}
r&\text{vanishing sequence of }V_r\\ \hline
0&(0,p,2p,3p,4p,6p)\\
1&(0,1,p,2p,3p,5p)\\
2&(0,1,2,p,2p,4p)\\
3&(0,1,2,3,p,3p)\\
4&(0,1,2,3,4,2p)\\
5&(1,2,3,4,5,p).
\end{array}
\tag{904.20}
$$
Here is a direct check that retains the actual frame. In the original ordered-by-order basis from (904.12), write $m\in\{0,1,2,3,4,6\}$ for the initial order of $f\sigma^6$. For $0\le r\le5$ and $m\le r$, R889 (889.35) gives initial order $r-m$; the original $\mu_6$ weights make all the other coefficient rows between zero and five vanish on this chosen basis vector. For $m>r$, use the exact Bell Taylor identity R889 (889.40), before truncation:
$$
Y^{6p}\Phi(\nabla_6^rf)
=\sum_{j=0}^r\binom rj6^j\Delta(Y)^j U_{r-j}(Y)^p,
\qquad \Delta(Y)=-BY+O(Y^p).
$$
The initial term of $U_{r-j}$ has order $m-r+j$, with nonzero coefficient $(m)_{r-j}$ times the original leading coefficient. These exponents are at most six, so the original truncated-zeta comparison does not affect them. The $j=0$ term has order $p(m-r)$, whereas every term with $j>0$ has the larger order $p(m-r)+j(p+1)$. The constant multiplier from R889 (889.22) is a unit. Thus the initial order is $p(m-r)$. These six orders are distinct and give exactly (904.20). In particular its last row also verifies the local order in (904.19).

## 6. Exact coefficient-row formula for $r\ge6$

Retain the original linear functionals
$$
c_n(f)=[z^n](f\sigma^6)\bmod p,\qquad 0\le n<p,
\tag{904.21}
$$
on the original six-dimensional source. These first-$p$ coefficients are integral by R702; no full reduction of the nonintegral high sigma series is being taken.

The six rows
$$
c_0,\ c_1,\ c_2,\ c_3,\ c_4,\ c_6
\tag{904.22}
$$
are independent. Indeed $c_0$ is nonzero on $x^3$, the next four rows isolate $-xy,x^2,y,x$ in their distinct $\mu_6$ weights, and $c_6(1)=1$ while all earlier rows vanish on $1$.

For $6\le r<p$, read the rows $c_r,c_{r-1},\ldots,c_0$ in that order and keep a row precisely when it increases their span. Let
$$
b_1<b_2<\cdots<b_6
\tag{904.23}
$$
be the six retained indices. They exist by (904.22). R889 (889.35), with all its factors units, identifies the rank of each successive local jet map with the rank of these successive row sets. The vanishing sequence of $V_r$ is consequently
$$
a_j=r-b_{7-j}\qquad(1\le j\le6).
\tag{904.24}
$$
In particular all six $a_j$ are distinct integers between zero and $r$, hence strictly less than $p$. The ordinary local Wronskian therefore has its expected initial determinant: the Vandermonde in the $a_j$ is a unit. There is no extra inseparable cancellation. Combining this with (904.17) gives
$$
\boxed{
w_r=\sum_{j=1}^6a_j-15
=6r-\sum_{j=1}^6b_j-15,\qquad
w_r\le p.
}
\tag{904.25}
$$

The exact original $\mu_6$ weights are $0,4,3,2,1,0$ on (904.2). Thus a basis of six coefficient rows necessarily consists of two rows with index zero modulo six and one row in each of classes $1,2,3,4$. Class five is identically zero. It follows that
$$
\sum_jb_j\equiv0+0+1+2+3+4\equiv4\pmod6.
$$
Since $w_r\ge0$, (904.25) sharpens to
$$
\boxed{
w_r\equiv5\pmod6,\qquad
5\le w_r\le p
\quad(6\le r<p).
}
\tag{904.26}
$$
This statement includes the two-dimensional weight-zero channel. It does not replace its two independent rows by a single scalar coefficient.

If $\nu_r=a_1$ is the common base-point order from R891, the distinctness of the $a_j$ yields $w_r\ge6\nu_r$. Consequently (904.25) implies $\nu_r\le\lfloor p/6\rfloor=N$, consistent with R891. The additional content of (904.25) is control of the sum of all six orders, not an improvement to a fixed-width bound for the scalar sequence.

## 7. Exact relation to the original open problem

For the original critical pairs
$$
i+j=N-1,\qquad h=6i+7,
$$
R891 gives
$$
f_i=0\Longleftrightarrow \nu_{6i+4}>0,\qquad
g_j=0\Longleftrightarrow \nu_{6j+1}>0.
\tag{904.27}
$$
The two indices add to $p-6$. Formula (904.25) imposes the proved six-row constraint at each of these indices. It does not assert an inequality coupling $w_r$ to $w_{p-6-r}$ or a total bound over all $r$ strong enough to rule out complementary zeros.

Likewise no primitive indicator or Legendre factor is removed. The required conclusion remains that at some original label with $(h,p+1)=1$,
$$
P_{h-1}(1/s)f_i g_j\ne0.
\tag{904.28}
$$
The common six-torsion orbit of the Wronskian zeros is a consequence of the genuine six-primary theta action. It is not a global action of the full norm-one $p$-torus on the elliptic curve. The actual original counterexamples in R706/R739 therefore remain compatible with all the results here.

## Sources

- [R889](R889-original-theta-distribution-and-same-label-sigma-jet.md), (889.15)--(889.22), (889.30)--(889.40): actual distribution, restricted Hasse product rule, six-dimensional vacuum, and local sigma comparison.
- [R891](R891-original-sigma-zeros-and-six-torsion-base-divisor.md), §§1--4: original coefficient rows, genuine six-primary theta action, full six-torsion base divisor, and complementary-index interpretation.
- [R878](R878-original-finite-theta-action-and-section-projections.md), §§2--4: actual symmetric theta lift, marked six-torsion action, and Cartier descent.
- [R702](R702-first-pole-block-and-uniform-shifted-units.md), §§1--3: integrality of the original coefficient range below $p$.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md), §§1--3: the same-label primitive and Legendre conditions.

This is a paper proof. No new numerical evaluation, prime scan, or mathematical execution is used.
