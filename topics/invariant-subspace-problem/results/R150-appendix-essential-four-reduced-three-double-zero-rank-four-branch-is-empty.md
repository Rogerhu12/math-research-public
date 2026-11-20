# R150: the remaining reduced-three-point complement of a rank-four double zero is empty

Author: Astra-ISP-b2a9acde-20261120 / r150_structure, with root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved, with exact original-source verification.** In the essential-four outer-mean length-five reduction, a complete critical point cannot have a simple zero of the same $L$ on a double-point factor and a unit complement consisting of three distinct points. Every vanishing cross mean and every repeated cross value is included. Combined with the exclusions for unit complements of types $3$ and $2+1$, this removes the entire simple-zero-on-a-double-point rank-four case.

## 1. The original five-dimensional algebra and equations

Use [the original length-five reduction](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md), with rank-three mean catalecticant, essential cubic dimension four, and mean outside that essential space. The active unit algebra is
$$
\mathcal B=\mathbb C^3,\qquad
\tau(X)=\sum_{i=1}^3a_iX_i,\qquad
a_i\ne0,\quad \sum_i a_i=1.
$$
Its three representatives $v_i$ are normalized by the same outer-mean $L$ to have value one. The remaining support is a distinct physical double point $w_0,w_1$, where the same $L$ has a simple zero. Normalize that factor as in [the original double-zero equations](R150-appendix-essential-four-double-zero-rank-four-isotropic-active-branch-is-empty.md), Section 1:
$$
L=\epsilon,\qquad \nu(1)=0,\qquad \nu(\epsilon)=1.
$$
This allowed physical representative change preserves the original $y,H,V$ and $K$.

For active coordinates $X\in\mathcal B$ and $R=r(w_0),S=r(w_1)$, the original moments and cubic are
$$
y(r)=\tau(X),\quad
H(r,r)=\tfrac14(\tau(X^2)+R^2),\quad
V(r,r,r)=\tfrac18\tau(X^3)+\tfrac38R^2S,
$$
$$
T_3=P(X)+\tfrac32R^2(S-\tau(X)),\qquad
P(X)=\tfrac12\tau((X-\tau(X))^3).
\tag{1.1}
$$
Let $K_a$ be the active Gram matrix and let
$$
U_i=K(v_i,w_0),\quad V_i=K(v_i,w_1),\quad
m=\tau(U),\quad n=\tau(V).
$$
The polar active mean is $d=K_a y$, and $F=\tau(d)/2$.

We use the exact original complete mean equations
$$
E_a+U^2-2mU=0,\qquad
\tau(U^2)=2m^2,
$$
$$
\tau(UV)=\tau(Ud)-2Fm+2mn,
\tag{1.2}
$$
where $E_a=e-2Dd-2d^2+4Fd$ is the active unit-factor mean equation, $D$ is integration against the active physical kernel, and $e$ integrates its square. These formulas are coefficients of the unchanged complete mean vector equation, after its contraction by the same outer-mean covector gives $\mathcal Q_{F_0^2}=0$.

The complete second-gradient tensor is
$$
N=N_a+mR(S-\tau(X))+\tfrac12(n-F)R^2
+\tfrac12\tau(UX)R.
\tag{1.3}
$$
It is exactly $T_{3,Ky}-F(yy^{\mathsf T}-2H)+4HKH$, with no moment variation removed. The full highest and second identities hold on the entire physical curve. At the zero double base, $R=S=0$, so in particular
$$
P(U)=0,\qquad N_a(U)=0.
\tag{1.4}
$$
The first equation and the square equation in (1.2) give
$$
\tau(U)=m,\qquad \tau(U^2)=2m^2,\qquad \tau(U^3)=4m^3.
\tag{1.5}
$$

The five support vectors are independent, and $K$ is nondegenerate in dimension six. Hence the Gram form on their span has rank at least four. We repeatedly use the consequence that a star matrix plus one diagonal entry has rank at most three and is impossible here.

## 2. A scalar cross element must be zero, and zero is impossible

If $U$ is scalar, the square equation gives $U=0$. Then $E_a=0$. The active mean classification in [the reduced-five-point exclusion](R150-appendix-essential-four-reduced-five-point-rank-three-branch-is-empty.md), Section 2, applies independently of the zero factor: either $K_a=0$, or one weight is $1/2$ and the pairing between the other two active points is zero.

If $K_a=0$, the two-column cross matrix $(U,V)$ has rank at most one, leaving at least two active radical vectors. This contradicts the Gram rank bound.

For the other case write the weights as $a,b,1/2$, with $a+b=1/2$, $ab\ne0$, and
$$
K_a=\begin{pmatrix}0&0&p\\0&0&q\\p&q&0\end{pmatrix}.
$$
In the three active coordinates,
$$
P(X,Y,Z)=\tfrac{ab}{2}(X-Y)^2
[2(1-a)X+2(1-b)Y-3Z],
$$
$$
N_a(X,Y,Z)=\tfrac{ab}{2}(X-Y)
\{p((1-a)X+aY)-q(bX+(1-b)Y)\}.
\tag{2.1}
$$
Because $U=0$, the full second equation (1.3) is
$$
N_a+\tfrac12(n-F)R^2=0
$$
on the physical curve. If $n=F$, independence of the first two physical polars forces
$(1-a)p-bq=ap-(1-b)q=0$. Their determinant is $-1/2$, so $p=q=0$, already excluded.

If $n\ne F$, this expresses the square of the physical $w_0$ polar as a quadratic in the first two active polars. But $v_1,v_2,w_0$ are three distinct pairwise orthogonal physical points. The complete isotropic-jet classification makes them one of the two triples $W_\pm$. The exact conic lemma in [the complete rank-three exclusion](R150-appendix-essential-four-all-rank-three-second-moment-branches-are-empty.md), Section 9, excludes precisely such a squared-coordinate relation on either triple. Thus $U=0$ is impossible.

## 3. Two cross values with nonzero mean

Suppose $m\ne0$ and $U$ has exactly two distinct values $\alpha,\beta$. Apply $\tau$ to its quadratic minimal polynomial and to that polynomial times $U$. Using (1.5) gives
$$
2m^2-(\alpha+\beta)m+\alpha\beta=0,
$$
$$
4m^3-2(\alpha+\beta)m^2+\alpha\beta m=0.
$$
Subtracting $m$ times the first equation from the second gives $\alpha+\beta=2m$, and then $\alpha\beta=0$. Thus the two values are $0,2m$, and the aggregate weight of either value group is $1/2$.

One of the groups is a singleton. Label its point $v_3$ and its weight $1/2$. The other weights are $a,b$ with $a+b=1/2$ and $ab\ne0$. Since $U^2-2mU=0$, the active mean equation is again $E_a=0$, so its Gram matrix and forms are those in (2.1).

There are just two cross patterns:
$$
U=(0,0,u)\quad\text{or}\quad U=(u,u,0),\qquad u=2m\ne0.
$$

For $U=(0,0,u)$, the mixed mean equation in (1.2) gives
$$
aV_1+bV_2=0.
$$
Indeed $\tau(Ud)=uF$, and the two $F$ terms cancel. At the physical zero double base, $X,Y$ have first terms $V_1s,V_2s$ and $Z$ has constant value $u$. The term $R^2(S-\tau(X))$ has order at least four. The order-two highest coefficient from (2.1) is
$-3abu(V_1-V_2)^2/2$. Thus $V_1=V_2$, and $a+b=1/2$ gives both zero. The full Gram matrix is now a star centered on $v_3$, plus the possible $w_1$ diagonal entry. Its rank is at most three, impossible.

For $U=(u,u,0)$, the highest equations at $v_1,v_2$ give
$$
V_1=p/2,\qquad V_2=q/2.
$$
The second-gradient equation at either point gives $n=F$, and hence $V_3=0$. At the physical zero base, the order-two highest coefficient is now
$$
\frac{3abu}{8}(p-q)^2.
$$
Therefore $p=q$, so both cross columns and the active pairings factor through the same sum of the first two active coordinates. Again the full Gram form is a star plus one diagonal entry, of rank at most three. Both two-value patterns with nonzero mean are excluded.

## 4. Every zero-mean cross element is excluded

Suppose $m=0$. If $U$ generates $\mathcal B$, then $1,U,U^2$ is a basis. Equation (1.5) says that $U$ is Frobenius-orthogonal to this entire basis. Nondegeneracy forces $U=0$, contradicting generation. The scalar case has already been excluded, so $U$ has exactly two values.

The quadratic minimal polynomial and $\tau(U)=\tau(U^2)=0$ imply that the product of those two values is zero. The nonzero value group has aggregate weight zero. Since each individual active weight is nonzero, that group contains two points, with weights $a,-a$, $a\ne0$; the remaining point has weight one. Use homogeneous ratios to normalize the nonzero cross value to one. Thus
$$
(a_1,a_2,a_3)=(a,-a,1),\qquad U=(1,1,0).
$$
Write
$$
k_{12}=x,\qquad k_{13}=p,\qquad k_{23}=q.
$$
The original value $N_a(U)=0$ is
$$
\frac a2(p-q-3ax)=0,
\quad\text{so}\quad p-q=3ax.
\tag{4.1}
$$
For a direct source, $\tau(Ud)=a(p-q-2ax)$ and
$\tau(U D U)=-2a^2x$; at this zero-mean, zero-square point the original $N_a$ value is $\tau(Ud)/2+\tau(U D U)/4$.

The active mean target is $E_a=(-1,-1,0)$. With (4.1), its third component is
$$
(E_a)_3=a^2x[6a^2x-(p+q)].
\tag{4.2}
$$
If $x\ne0$, then
$$
p=\tfrac{3a}{2}(2a+1)x,\qquad
q=\tfrac{3a}{2}(2a-1)x.
$$
The first two active mean components are exactly
$$
(E_a)_1=\frac{a(4-3a)(4a^2-1)}4x^2,\qquad
(E_a)_2=-\frac{a(4+3a)(4a^2-1)}4x^2.
$$
Their equality forces $4a^2-1=0$. Both components would then be zero, contradicting their required value $-1$.

If $x=0$, then $p=q$, and the first two mean equations give $p^2=1$. The highest equations at $v_1,v_2$ give $V_1=V_2=p$. The original second equation there gives $V_3=0$. Consequently the full Gram form again factors as a star through the common first-two-point direction, plus the possible $w_1$ diagonal, and has rank at most three. This excludes every $m=0$ case.

## 5. A faithful orthogonal basis for the remaining generating case

Only $m\ne0$ with three distinct cross values remains. Divide all Gram pairings and both cross columns by $m$; these are homogeneous necessary equations. Rename the normalized quantities, so $\tau(U)=1$, $\tau(U^2)=2$, $\tau(U^3)=4$.

Set
$$
x=U-1,\qquad z=x^2-1.
$$
Because $U$ generates the three-dimensional algebra, $1,x,z$ is a basis. The moment identities imply
$$
\tau(1)=1,\quad \tau(x)=\tau(z)=0,\quad
\tau(x^2)=1,\quad \tau(xz)=0.
$$
Put $\ell=\tau(z^2)$. The Frobenius Gram matrix is
$\operatorname{diag}(1,1,\ell)$, so $\ell\ne0$. Associativity and the pairing give the exact multiplication table
$$
x^2=1+z,\qquad xz=\ell x+cz,
$$
$$
z^2=\ell+c\ell x+(\ell+c^2-1)z
\tag{5.1}
$$
for some scalar $c$. Indeed the constant coefficient of $xz$ is zero; pairing it with $x$ gives coefficient $\ell$, and call its $z$ coefficient $c$. Multiplying once more by $x$ gives the last identity.

This change of algebra basis is faithful. It only rewrites the same active physical kernel. In this basis the active vector-valued cubic is
$$
P(X_0+X_1x+X_2z)=
\frac{\ell}{2}
[3X_1^2X_2+3cX_1X_2^2+(\ell+c^2-1)X_2^3].
\tag{5.2}
$$
The original physical self-pairing is zero at all three active points, hence multiplication of the active kernel's two tensor factors is zero in $\mathcal B$.

Write the symmetric kernel coefficient matrix as $(k_{ij})$ in the basis $1,x,z$. The diagonal-zero condition and the necessary original value $N_a(U)=0$, $U=1+x$, give the following exact two-parameter form:
$$
K=
\begin{pmatrix}
(c+1)h&-\ell h/2&(h+r)/2\\
-\ell h/2&-(c+1)h-\ell r&(h-cr)/2\\
(h+r)/2&(h-cr)/2&r
\end{pmatrix}.
\tag{5.3}
$$
Here is the linear derivation. If initially $p=k_{11},q=k_{12},r=k_{22}$, multiplication using (5.1) gives
$$
k_{00}=-p-\ell r,\quad
k_{01}=-\ell q-c\ell r/2,\quad
k_{02}=-[p+2cq+(\ell+c^2-1)r]/2.
$$
The original $N_a(U)$ equals
$$
-\frac{\ell}{4}[p+2(c+1)q+(\ell+c^2+c)r].
$$
Set $h=2q+cr$ and eliminate $p$; this is (5.3). Thus no independent Gram condition has been inserted.

## 6. The original mean equation has only three candidate families

In the basis (5.1), the active mean equation (1.2) is simply
$$
E_a=-z,
\tag{6.1}
$$
because $U^2-2U=z$. Let
$$
W=4\ell+c^2-1.
$$
Direct substitution of (5.3) into the original unit-factor mean expression gives
$$
(E_a)_0=\frac{\ell}{2}
[-\ell h^2+2(c+1)hr+Wr^2],
$$
$$
(E_a)_x=\frac{\ell}{4}
[2\ell h^2+2(\ell+c(c+1))hr+cWr^2].
\tag{6.2}
$$
If $r=0$, these force $h=0$, which makes $E_a=0$, contradicting (6.1). Hence $r\ne0$; set $t=h/r$.

The first two equations in (6.1) give
$$
-\ell t^2+2(c+1)t+W=0,\qquad
2\ell t^2+2(\ell+c(c+1))t+cW=0.
$$
Eliminating $W$ yields
$$
\ell t[(c+2)t+2]=0.
\tag{6.3}
$$
The remaining coefficient is
$$
(E_a)_z=\frac{r^2}{4}\Phi(t,c,\ell),
$$
$$
\begin{aligned}
\Phi={}&\ell(2c+1-\ell)t^2
+2(c+1)(3\ell+c^2-1)t\\
&+8\ell^2+(6c^2-5)\ell+(c^2-1)^2.
\end{aligned}
\tag{6.4}
$$

If $t=0$, the first equation gives $\ell=(1-c^2)/4$, and $\Phi=\ell$. Thus the first candidate family is
$$
\mathrm{I}:\quad
t=0,\quad \ell=(1-c^2)/4,\quad r^2=-4/\ell.
\tag{6.5}
$$
In particular $c\ne\pm1$.

If $t=-2/(c+2)$, then $c\ne-2$, and the first equation factors as
$$
(c+1)(c+3)(4\ell+c^2-4)=0.
$$
For $4\ell+c^2-4=0$, direct substitution in (6.4) gives $\Phi=0$, impossible in (6.1). At the two remaining values,
$$
\mathrm{II}:\quad c=-1,\quad t=-2,\quad
r^2=-\frac4{\ell(4\ell-3)},
$$
$$
\mathrm{III}:\quad c=-3,\quad t=2,\quad
r^2=-\frac4{\ell(4\ell+5)}.
\tag{6.6}
$$
Their displayed denominators are nonzero, since otherwise $(E_a)_z=0$. Equations (6.3)–(6.6) exhaust the original mean equation in the generating case.

## 7. The same highest equations determine the remaining cross column

For each candidate family write $K=r\overline K$, where (5.3) with $h=rt$ gives
$$
\overline K=
\begin{pmatrix}
(c+1)t&-\ell t/2&(t+1)/2\\
-\ell t/2&-(c+1)t-\ell&(t-c)/2\\
(t+1)/2&(t-c)/2&1
\end{pmatrix}.
$$
Let its three columns, regarded as elements of $\mathcal B$, be
$$
d_{\rm bar},\quad a_{\rm bar},\quad b_{\rm bar}.
$$
Then the active polar mean is $rd_{\rm bar}$, $F=r(d_{\rm bar})_0/2$, and integration of $U=1+x$ against the active kernel is $r(d_{\rm bar}+a_{\rm bar})$.

The element $U$ is a unit. Its explicit inverse, directly checked using (5.1), is
$$
U^{-1}=\frac{\ell-c-1}{\ell}
+\frac{c+1}{\ell}x-\frac1\ell z.
\tag{7.1}
$$
The highest equation restricted to all three active points is
$$
r^3P_{\rm bar}+\tfrac32U^2(V-rd_{\rm bar})=0,
$$
where multiplication is in the same algebra and
$$
P_{\rm bar}=\frac{\ell}{2}b_{\rm bar}
[3a_{\rm bar}^2+3ca_{\rm bar}b_{\rm bar}
+(\ell+c^2-1)b_{\rm bar}^2].
\tag{7.2}
$$
Therefore it uniquely gives $V=rV_{\rm bar}$ with
$$
V_{\rm bar}=d_{\rm bar}-\frac{2r^2}{3}P_{\rm bar}U^{-2}.
\tag{7.3}
$$
This is the original active highest equation, evaluated in the faithful algebra; it retains all three active equations.

For completeness the active original $N_a$, divided by its overall factor $r$, is the following quadratic form in a general element $X_0+X_1x+X_2z$:
$$
\begin{aligned}
\overline N_a=\frac{\ell}{4}\big[&
-tX_0X_1+(t+1)X_0X_2+tX_1^2\\
&+((-2\ell+2c+1)t+c)X_1X_2\\
&+((\ell(1-c)+c(c+1))t+2\ell+c^2-1)X_2^2
\big].
\end{aligned}
\tag{7.4}
$$
It follows from (5.2), the same polar mean, $H=\operatorname{diag}(1,1,\ell)/4$, and the three original terms in (1.8).

Let $N_{\rm bar}$ be (7.4) evaluated at
$(d_{\rm bar},a_{\rm bar},b_{\rm bar})$, with products in $\mathcal B$. Substitute (7.3) into the original full second-gradient equation (1.3), restrict it to the active algebra, and divide by $r\ne0$. The required element is
$$
\boxed{
\mathcal R=
r^2N_{\rm bar}
+U(V_{\rm bar}-d_{\rm bar})
+\tfrac12\left((V_{\rm bar})_0-\tfrac12(d_{\rm bar})_0\right)U^2
+\tfrac12(d_{\rm bar}+a_{\rm bar})U=0.
}
\tag{7.5}
$$
Every factor and operation in (7.5) is now explicit in (5.1), (6.5) or (6.6), and (7.1)–(7.4).

## 8. Each candidate family contradicts the original second gradients

Only the coefficients of $1$ and $z$ in (7.5) are needed.

For family I, exact algebra multiplication gives
$$
\mathcal R_0=
\frac{(c+1)(3c^2+10c+19)}{4(c-1)},
\qquad
\mathcal R_z=
\frac{(c+1)(-3c^2+38c+29)}{16(c-1)}.
$$
Since $c\ne\pm1$, vanishing would require the two quadratic numerators after removal of $c+1$ to be zero. Their sum is $48(c+1)$, a contradiction.

For family II, the corresponding coefficients are
$$
\mathcal R_0=-\frac{4\ell(4\ell+39)}{3(4\ell-3)},
\qquad
\mathcal R_z=\frac{\ell(69-220\ell)}{12(4\ell-3)}.
$$
The denominators and $\ell$ are nonzero. The equations $4\ell+39=69-220\ell=0$ contradict their linear combination $2214=0$.

For family III, put
$$
Q_0(\ell)=12\ell^4+71\ell^3+260\ell^2+712\ell+640,
$$
$$
Q_z(\ell)=92\ell^4+275\ell^3+464\ell^2+784\ell+1280.
$$
The original coefficients are
$$
\mathcal R_0=-\frac{Q_0(\ell)}{3\ell^2(4\ell+5)},
\qquad
\mathcal R_z=-\frac{Q_z(\ell)}{12\ell^2(4\ell+5)}.
$$
Their integer Sylvester resultant is
$$
\operatorname{Res}_\ell(Q_0,Q_z)
=7325267546603520000\ne0.
\tag{8.1}
$$
Thus they have no common complex root. This excludes the last family.

The companion exact source [reduced-three double-zero verifier](../notes/2026-11-20-essential-four-reduced-three-double-zero-verify.py) reconstructs the multiplication table, the diagonal kernel identity, the original active mean coefficients and the original $N_a$ directly from the original moments. It then constructs the three highest-derived cross columns (7.3), checks all six residual coefficients used above from the unchanged full $N$, and checks the integer resultant (8.1) over $\mathbb Q$. It prints only a bounded scalar result; no recomputable elimination table is stored.


The exact source was executed without arguments in [Actions run 44724947207](https://github.com/Rogerhu12/math-research-public/actions/runs/44724947207), job 136249870826, at frozen commit a945aec4331160c285f6187b0cecb3bc2e92db39. SymPy 1.13.3 and mpmath 1.3.0 reconstructed all stated source identities and the six original residual coefficients; every assertion, including (8.1), passed in 0.687237499 seconds. The root fetched the original job log and matched source SHA-256 e40779b9596d56b3c592a023f28c9c1af395d00d470dfe60d2cb3fc98ae4ade0. The one-line result SHA-256 is 52ed23cd365d3e33c0c8bfc05ed274cc6629822f266f4442b68b15dbffa2b0a5; the complete decoded job-log SHA-256 is 993d4afe61b0f8da2e665d1fa783be4b97e854cb34c94dab7fe0749c3c280aab. No elimination output arrays are retained. This same job completed an actual pull and verified both unchanged README blobs at 2026-11-20 11:07:23 UTC.

## 9. Exhaustion and consequence for rank four

Every element of the reduced three-dimensional algebra has one, two or three distinct values. Section 2 excludes one value. Sections 3 and 4 exclude all two-value and zero-mean cases. A three-value element generates the algebra; with nonzero mean it is precisely Sections 5–8, where all mean branches and all denominators have been handled. This exhausts the unit reduced-three-point complement.

The argument uses the original complete highest and low gradients throughout. The physical zero orders, the complete isotropic-triple classification and its conic lemma include infinity. No positive-measure, spectral or numerical assumption is made.

Combining this result with the unit-triple and unit-two-plus-one exclusions, every rank-four case where $L$ has a proper simple zero on a double-point block is empty. The previously excluded simple zeros on blocks of lengths three, four and five then leave only the rank-four pattern in which $L$ is identically zero on one entire reduced point and is a unit on its length-four complement. The unit length-four local case of that pattern was also excluded separately; split length-four unit supports remain distinct. Rank five and the other essential-space branches remain open, and no global matched Bell power certificate or Hilbert ISP theorem is inferred here.
