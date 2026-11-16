# R920 — The original upper primitive Igusa layer is fixed by one inert Hecke row

Date: 2026-11-16. Status: **proved for all original allowed primes with $p\equiv5\pmod{12}$**. The actual weight-ten Igusa layer of R916 is the original marked CM vector up to a nonzero scalar. One exact coefficient of the inert operator $T_5$, equal to $8$, removes the extra tame multiplicity in every characteristic under consideration. No residual semisimplicity or finite-prime experiment is used.

## 1. Original label, scales, and variables

Keep the original positive CM quotient, good Raynaud abelian part, target generator, and scales:
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
p\equiv5\pmod{12},\qquad
n=p+1,\quad e=p^2-1,\quad\varpi^e=p.
\tag{920.1}
$$
Choose
$$
h=\frac{p+9}{2},\qquad r=2h-n=8.
\tag{920.2}
$$
Writing $p=12b+5$ gives $h=6b+7$, so $h\equiv1\pmod6$ and $h$ is odd. Since any common divisor of $h$ and $n$ divides $2h-n=8$, one has
$$
(h,n)=1.
\tag{920.3}
$$
The label lies in the original upper-half range: $n/2<h\le p-4$ for $p\ge17$. In particular no extra choice of label or prime is made in (920.1).

Write exactly as in R916
$$
e_hq_B=[p^{a_h}]\circ f_h,\qquad a_h\ge0,\qquad
L_h=\varpi^{-8p}f_h^*\omega_h.
\tag{920.4}
$$
Then $L_h$ is integral and primitive. Its nonzero reduction is on the original Igusa part with full character
$$
\chi_+(u)=\operatorname N(u)^{1-h},
\qquad \delta=\zeta.
\tag{920.5}
$$
Its weight in the actual Igusa correspondence is
$$
k_+=10,\qquad k_-=p-7
\tag{920.6}
$$
for the different Cartier-cokernel functional of R913.

We distinguish the variables as follows. The tame full-six variable is $\tau'$, with width-six parameter
$$
Q=\exp(2\pi i\tau'/6).
$$
For an ordinary Fourier expansion put $\tau'=6\tau$ and
$$
q=\exp(2\pi i\tau),\qquad Q=q.
\tag{920.7}
$$
Thus $E_6(\tau')$ becomes $E_6(6\tau)$, not $E_6(\tau)$, and
$\eta(\tau')^{12}$ becomes $\eta(6\tau)^{12}$. The positive original choice is
$$
s=\sqrt{-3}=\zeta-\zeta^2=1+2\zeta,
\qquad s^2=-3.
\tag{920.8}
$$
All appearances of $s$ and $\zeta^2$ below use this same marked branch.

Let $F_{10}$ be R913's normalized tame CM theta series
$$
F_{10}=f_{\Xi_{10}},\qquad
\Xi_{10}((a))=a^9\epsilon_3(a),
\qquad a_1(F_{10})=1.
\tag{920.9}
$$
It has level nine and trivial nebentypus. Define the original marked vector
$$
V_{10}^\dagger(Q)=F_{10}(Q)-2^{10}\zeta^2F_{10}(Q^4).
\tag{920.10}
$$
The conclusion is that, with the full two-component extension explained in §5,
$$
\boxed{\quad
\overline L_h=c_h\,\Phi_{10}(\overline V_{10}^\dagger),
\qquad c_h\in k^\times,
\quad}
\tag{920.11}
$$
where
$$
\Phi_{10}(F)=\frac16\operatorname{KS}(F/\mathfrak a^8)
\tag{920.12}
$$
has exactly the original tame, exotic/Frobenius, and determinant transports of R913. The scalar $c_h$ is not set equal to one.

## 2. The whole tame space and its actual character

Use the entire original graph subgroup $H_6$, not just an eigenspace selected by its Hecke values. Its modular curve and deck action are
$$
X'(6)=\mathbf P^1_u,\qquad
j=27648u^3(1-4u^3),\qquad
\delta_\zeta:u\longmapsto\zeta u.
\tag{920.13}
$$
As proved in R918 from this model, it has one width-six cusp, three elliptic points of order three, and no elliptic point of order two. Its original positive cubic transport is the fixed unit $a=\sqrt[3]4\,u$.

The weight-four form $V_4^\dagger$ of R869 has precisely the minimum zero divisor forced on a cusp form of weight congruent to four modulo six: one at the cusp and local fine order one at each of the three order-three points. There are no further zeros, by the valence calculation of R918(918.14–15). Consequently division gives an isomorphism
$$
S_{10}(H_6)\ \xrightarrow{\;/V_4^\dagger\;}\ M_6(H_6).
\tag{920.14}
$$
The quotient is regular at the cusp and at the elliptic points, since weights ten and four have the same stabilizer character. Conversely multiplication by $V_4^\dagger$ makes every regular weight-six form cuspidal.

Put
$$
W_6=\frac{E_6}{8u^3-1}.
\tag{920.15}
$$
The three simple zeros of the denominator are exactly the zeros of $E_6$ above $j=1728$. The quotient is therefore regular there. It has no zero or pole at any other finite point and has a zero of order three at the cusp. This gives
$$
M_6(H_6)=W_6\,\langle1,u,u^2,u^3\rangle.
\tag{920.16}
$$
Equivalently the weight-six line on the coarse $\mathbf P^1$ has degree three; its stabilizer characters are trivial.

The deck transformation fixes $E_6$ and $W_6$. Hence the invariant part of (920.16) is spanned by $W_6$ and $u^3W_6$. It can be written without choosing a sign in a square root:
$$
W_6^2=-1728\,\Delta=-1728\,\eta^{24},
\qquad W_6=\pm24s\,\eta^{12}.
\tag{920.17}
$$
To verify the square identity, combine
$E_6^2=E_4^3(1-1728/j)$ with (920.13):
$$
1-\frac{1728}{j}
=-\frac{(8u^3-1)^2}{16u^3(1-4u^3)}.
$$
Since $27648=16\cdot1728$, division gives (920.17). The ratio in its second equality is a constant of square one. Its sign is irrelevant for the span. Also
$E_6=(8u^3-1)W_6$, so
$$
M_6(H_6)^{\delta=1}=\langle E_6,\eta^{12}\rangle.
\tag{920.18}
$$

On the pre-Frobenius marking, $V_4^\dagger$ and $V_{10}^\dagger$ have the same deck character, by the uniform tame matrices in R913(913.32–33). The determinant correction changes both to the original positive $\delta=\zeta$ character. It follows from (920.14–18) that the actual weight-ten character space is exactly two-dimensional, with basis
$$
B_1=V_4^\dagger E_6,\qquad
B_2=V_4^\dagger\eta^{12}.
\tag{920.19}
$$
The whole weight-ten cusp space has dimension four; only the specified character space is asserted to have the basis (920.19).

These statements commute with reduction at every $p>3$. On the fine full-six curve the cusp-form line
$\omega^{10}(-\text{cusps})$ has degree $60-12=48$, so its $H^1$ vanishes on the genus-one fibers. Integral cohomology and base change therefore apply. Taking the actual $H_6$ and deck-character summands uses only unit averaging denominators. In the ordinary variable (920.7), the coefficient matrix of $B_1,B_2$ at $q$ and $q^4$ will be
$$
\begin{pmatrix}1&0\\8s&1\end{pmatrix}.
\tag{920.20}
$$
Its determinant is one. The forms are integral at every full-six cusp, by their original integral theta expressions and tame transports. Thus they form a basis of the full integral rank-two character lattice, not merely a sublattice of finite unspecified index. In particular (920.19) is the whole special-fiber space.

## 3. Two short exact expansions and the named CM vector

All expansions in this section are finite algebraic identities of power series; no numerical execution is used. With $q$ as in (920.7),
$$
F_4(\tau)=\eta(3\tau)^8
=q\prod_{m\ge1}(1-q^{3m})^8.
$$
For $x=q^3$, multiply the first three relevant factors:
$$
\begin{aligned}
(1-x)^8&=1-8x+28x^2-56x^3+O(x^4),\\
(1-x^2)^8&=1-8x^2+O(x^4),\\
(1-x^3)^8&=1-8x^3+O(x^6).
\end{aligned}
$$
The resulting coefficients through $x^3$ are $1,-8,20,0$. Therefore
$$
V_4^\dagger(6\tau)
=q+8s\,q^4+20q^7+0q^{10}+O(q^{13}).
\tag{920.21}
$$
Here the oldform contributes only its first term up to degree ten, and
$-8-16\zeta^2=8s$. Also
$$
E_6(6\tau)=1-504q^6+O(q^{12}),\qquad
\eta(6\tau)^{12}=q^3(1-12q^6+O(q^{12})).
\tag{920.22}
$$
Equations (920.21–22) give (920.20), and specifically
$$
[q^{10}]B_1=-4032s,\qquad
[q^{10}]B_2=20-12=8.
\tag{920.23}
$$

The prime two is inert in $\mathbf Q(s)$, so the CM form in (920.9) has
$a_2=0$ and $a_4=-2^9=-512$. Consequently
$$
[q]V_{10}^\dagger=1,\qquad
[q^4]V_{10}^\dagger=-512-1024\zeta^2=512s.
\tag{920.24}
$$
Its actual membership in the character space (920.19) is already fixed by the full original tame matrices, not inferred from these two coefficients. Comparing (920.20) and (920.24) now proves the exact identity of characteristic-zero modular forms
$$
\boxed{\quad
V_{10}^\dagger=V_4^\dagger(E_6+504s\,\eta^{12})
=B_1+504s B_2.
\quad}
\tag{920.25}
$$
This identity reduces in the full integral lattice at every $p>3$.

## 4. The inert $T_5$ row and why it applies to the actual source

After the fixed change $\tau'=6\tau$, every form in (920.19) is a classical weight-ten cusp form for $\Gamma_0(36)$ with trivial nebentypus. Indeed
$$
\begin{pmatrix}6&0\\0&1\end{pmatrix}
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\begin{pmatrix}6&0\\0&1\end{pmatrix}^{-1}
=
\begin{pmatrix}a&6b\\c/6&d\end{pmatrix}
\equiv\pm I\pmod6
\tag{920.26}
$$
for an element of $\Gamma_0(36)$, and $\pm I$ belongs to the original tame group. The constant slash-operator factor is a power of six, a unit at all primes considered.

We only need preservation of a Hecke **zero**, not an unmarked identification of all the Hecke matrices. Prime-to-six isogenies commute with this fixed six-level pullback. This may be checked before taking quotients on the full paired level: the isogeny transports the complete six-basis, the associated six-isogeny diagram commutes, and the target pairing is multiplied by its degree. Choosing the target pairing component inserts exactly its fixed invertible determinant transport. If necessary the source pairing component is changed by the inverse transport. Therefore a form killed by the original full marked $T_5$ pulls back to a form killed by the ordinary $\Gamma_0(36)$ operator $T_5$. No nonzero value is being compared after discarding that transport. The same statement follows by viewing the fixed six-level translation at the primes two and three: it commutes with the Hecke convolution at five. Any fixed normalization factor is a power of five and is a unit here.

For an ordinary series $G(q)=\sum a_mq^m$ of weight ten and trivial nebentypus,
$$
T_5G=\sum_{m\ge1}
\bigl(a_{5m}+5^9a_{m/5}\bigr)q^m,
\tag{920.27}
$$
with $a_{m/5}=0$ if $5\nmid m$. Thus the coefficient at $q^2$ is exactly $a_{10}$. This formula is used on the pulled-back form; no assertion that its output remains in the same $\delta$ branch is made. In fact the inert correspondence interchanges the two nontrivial deck characters.

Let $A,B\in k$. Equations (920.23) and (920.27) give
$$
T_5(AB_1+BB_2)=0
\quad\Longrightarrow\quad
-4032sA+8B=0
\quad\Longrightarrow\quad
B=504sA.
\tag{920.28}
$$
The last implication uses only that $8$ is a unit. Conversely the CM vector (920.25) is killed by $T_5$: the prime five is inert, so $a_5(F_{10})=0$, and both actual oldform maps commute with this prime-to-six operator. Hence
$$
\boxed{\quad
\ker\!\left(T_5\bigm|
\langle\overline B_1,\overline B_2\rangle\right)
=k\,\overline V_{10}^\dagger .
\quad}
\tag{920.29}
$$
For the forward implication it would suffice to use the single target coefficient row; no rank assertion for an endomorphism of the original two-dimensional space is needed.

The original quotient supplies precisely the required Hecke zero. R913(913.40–42) transports the actual Hecke relation to weight ten, retaining its factor $5^{p-h}$ and all pairing corrections. The CM eigenvalue is zero at five, and $p\ne5$. Thus the weight-ten form corresponding to the actual $\overline L_h$ is killed by this operator. It is consequently on the line (920.29), provided the whole Igusa character space has been included. That last point is addressed next.

## 5. The two Igusa components and the full character space

Here $p\equiv1\pmod4$. The actual normalizer quotient has two Igusa parts, each of type $\operatorname{Ig}(p)/C_4$, before the original tame quotient. A nonsquare norm interchanges them. This differs from the single-part situation in R918.

For scalar $u=a\in\mathbf F_p^\times$, the original ordinary datum sends $P$ to $aP$, while $\operatorname N(u)=a^2$. Equation (920.2) gives
$$
a^{2(1-h)}=a^{-(p+7)}=a^{-8}.
\tag{920.30}
$$
For the multiplicative Igusa structure $\beta$ paired to $P$, this is the inverse scaling $\beta\mapsto a^{-1}\beta$. Thus (920.30) is exactly the character of (920.12). Since $10-2=8$ is divisible by four, the differential descends through the actual $C_4$ quotient.

On one chosen part, Cais Proposition 3.1 with $k=k_0=10$ identifies the whole holomorphic character space with $S_{10}(H_6,k)$. There is no supersingular-pole term, since $10<p+1$. The converse may be verified directly as in R918: multiplying by $\mathfrak a^8$ after dividing by Kodaira–Spencer gives a descended section satisfying
$$
(p-1)\operatorname{ord}_{P_{\rm tame}}F
\ge10-p>-(p-1).
\tag{920.31}
$$
Its order on the tame base is nonnegative. Holomorphicity at the cusps forces it to be a cusp form. Thus higher-weight presentations cannot add an extra holomorphic character space. Taking the actual tame invariants and deck summand is exact because their orders are prime to $p$.

The full original character is (920.5), not just its restriction in (920.30). Starting with the differential on the chosen part, extend to the other part with the factor prescribed by $\chi_+(u)$ for an element of nonsquare norm. This extension is unique. Its compatibility with the stabilizer follows from (920.30) and the $C_4$ descent. The square of an interchange lies in that stabilizer, so the same character verifies the group law. Conversely restriction of a full-$\chi_+$ vector to one part is injective; a vector zero on one part is also zero on the other. Hence a nonzero vector from R916 restricts nontrivially.

Finally retain R913's exotic/Frobenius map and determinant-$-1$ correction at level six. It conjugates the deck character and transports the phase and CM point together. The actual $\delta=\zeta$ subspace on one part is consequently the complete space (920.19), not an arbitrarily chosen CM subspace.

We may therefore apply (920.29) to the nonzero actual restriction of $\overline L_h$. It equals $c_h\Phi_{10}(\overline V_{10}^\dagger)$ with $c_h\in k^\times$. Extending with the fixed full norm character proves (920.11) on both parts. No half-period label or alternative norm extension has been merged.

## 6. The specified CM unit and actual fine Igusa vanishing order

The identity (920.25) retains a simple marked unit. Use the original
$$
A_2=\vartheta_2^4,\qquad B=\vartheta_4^4,
\qquad A_2=\zeta B
\tag{920.32}
$$
at the transported $j=0$ point. The classical theta identities in the same normalization are
$$
E_6=\frac{(A_2+2B)(2A_2+B)(B-A_2)}2,
\qquad
16\eta^{12}=A_2B(A_2+B).
\tag{920.33}
$$
At (920.32), use $2\zeta+1=s$ and
$(\zeta+2)(1-\zeta)=3$ to obtain
$$
E_6=\frac{3s}{2}B^3,\qquad
\eta^{12}=-\frac1{16}B^3,
\qquad E_6=-24s\,\eta^{12}.
\tag{920.34}
$$
This fixes the sign at the actual marking. In particular
$$
\left.\frac{V_{10}^\dagger}{E_4}\right|_{P_0}
=
-20\,E_6(P_0)
\left.\frac{V_4^\dagger}{E_4}\right|_{P_0}.
\tag{920.35}
$$
R869(869.30) proves the final ratio is a unit. The factor $E_6(P_0)$ is nonzero because $\Delta$ is a unit and $E_6^2=-1728\Delta$ at $j=0$. All remaining factors are units for $p\ge41$. Thus $V_{10}^\dagger$ has exactly a simple zero at this fine tame CM marking. A change to the other marked branch without changing the phase would not be this calculation.

On the fine Igusa cover, the tame base parameter has order $p-1$, $\mathfrak a$ has order one, and the pulled-back Kodaira–Spencer differential has order $p-2$. Equations (920.11–12) and (920.35) give the exact order of the actual layer:
$$
\boxed{\quad
\operatorname{ord}_{P_{\rm ss}}\overline L_h
=(p-1)-8+(p-2)=2p-11.
\quad}
\tag{920.36}
$$
This is on the fine cover, before the $C_4$ and tame quotients. It does not silently identify that parameter with the original coarse $c_1$ parameter.

## 7. Scope and remaining comparison

The actual complete differential retains
$$
\operatorname{content}_R((e_hq_B)^*\omega_h)
=\varpi^{ea_h+8p}R.
\tag{920.37}
$$
The integer $a_h$ is unchanged. The theorem identifies the primitive good-model layer with its named CM vector, and gives its actual marked fine Igusa order. It does not divide the original map by its Tate index or replace it by an optimal quotient.

The other weight $p-7$ belongs to the distinct Cartier-cokernel functional of R913. The argument above proves no value of that functional on its proposed companion.

In the original critical notation the same label has
$$
i=\frac{p-5}{12},\qquad
j=i-1,\qquad
h=6i+7,\qquad
p=6N+5,\qquad i+j=N-1.
\tag{920.38}
$$
Its primitive status is proved in (920.3); the remaining original expression is still
$$
P_{h-1}(1/s)\,f_i g_{i-1}.
\tag{920.39}
$$
The nonzero scalar in (920.11) has not been identified with this expression, with the specified coefficient of $u_{GF}$, or with a first normal coefficient at $c_1$. The actual ramified source/normal transport and any holomorphic ambiguity must still be retained. The new uniqueness is a theorem about the actual good Igusa layer, not a substitution for the specified jet.

## Sources

- [R916](R916-original-finite-flat-quotient-and-exact-Hodge-content.md): exact original content and nonzero upper-half layer.
- [R913](R913-original-Igusa-Cartier-functional-and-two-CM-companions.md), §§3–7: full norm extensions, complete same-label CM companions, the fixed two-oldform phase, and the corrected original Hecke operator.
- [R918](R918-original-central-primitive-Igusa-layer-and-marked-weight-four-vector.md), §§2–4: the full tame group, integral base change, and the weight-four divisor.
- [R869](R869-original-maximal-cusp-lattice-and-first-theta-layer.md), (869.27–30), and [R390](R390-cm-coordinate-inertia-weight-one-channel-and-cartier-unit.md), §6: the actual weight-four theta vector and marked normalization.
- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md), §§2–4: the original six-level isogeny transports and determinant correction; the present proof uses Hecke-zero compatibility before taking any marked component.
- Gross, *A tameness criterion for Galois representations associated to modular forms (mod p)*, [original PDF](https://www.math.purdue.edu/~tongliu/seminar/Mlift/Gross.pdf), §3, especially the Hecke $q$-expansion formula (3.5), and Propositions 5.7–5.9: normalized Hecke and Igusa differential conventions.
- Cais, *On the $U_p$ operator in characteristic $p*, [author paper](https://arxiv.org/pdf/1305.4188), Proposition 3.1 and equation (3.2): the full holomorphic Igusa character space and its local orders.

All coefficient identities used above are displayed finite paper expansions. No new mathematical computation or finite-prime scan has been executed.

