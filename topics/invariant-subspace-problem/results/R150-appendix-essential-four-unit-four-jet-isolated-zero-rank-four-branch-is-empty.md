# R150: a unit length-four local block and an isolated zero point cannot be rank-four critical

Author: Astra-ISP-b2a9acde-20261120 / r150_structure, with root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved.** In the original essential-four outer-mean length-five reduction, the rank-four case with divisor $4s_0+s_1$, $L$ a unit on $4s_0$ and $L=0$ at $s_1$, is empty. This is the opposite placement of the defect from the previously excluded simple zero on the quadruple block. The proof supplies all exceptional branches and an explicit rational univariate remainder certificate for the regular branch.

## 1. The exact local-unit normal form

Use [the original length-five reduction](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md), under its rank-three mean-catalecticant, essential-four and outer-mean hypotheses. The present algebra is a unit block $\mathbb C[t]/(t^4)$ and an isolated point where $L=0$.

Divide the physical representative on the unit block by the same $L$. Its Frobenius functional $\tau$ then has $\tau(1)=1$. An invertible parameter change makes
$$
\tau(t)=\tau(t^2)=0,\qquad \tau(t^3)=1.
\tag{1.1}
$$
Indeed, if the original top value is $q\ne0$, choose a new parameter $z=c_1t+c_2t^2+c_3t^3$. First choose $c_1^3q=1$, then kill $\tau(z^2)$ using $c_2$, and finally kill $\tau(z)$ using $c_3$. This changes only the original physical jet basis. The same $L$ remains the constant one on the block, and the original $K$ and moments remain fixed.

Let $u_0,u_1,u_2,u_3$ be the resulting divided jets. Normalize the nonzero cubic coefficient at the isolated zero point by rescaling its physical representative $w$. For a covector $r$ write
$$
T=r(u_0),\quad X=r(u_1),\quad Y=r(u_2),\quad Z=r(u_3),\quad R=r(w).
$$
The original moments are
$$
y=u_0+u_3,\qquad H(r,r)=\tfrac14(T^2+2TZ+2XY),
$$
$$
V_{\rm act}(r,r,r)=\tfrac18\tau((T+Xt+Yt^2+Zt^3)^3),\qquad
V_{\rm zero}(r,r,r)=\tfrac14R^3.
$$
The exact complete cubic is
$$
T_3=P(X,Y,Z)+R^3,\qquad
P(X,Y,Z)=Z^3-3XYZ+\tfrac12X^3.
\tag{1.2}
$$

Write the active Gram matrix as
$$
K_a=
\begin{pmatrix}
0&0&A&B\\
0&-2A&-B&C\\
A&-B&D&E\\
B&C&E&G
\end{pmatrix},
\tag{1.3}
$$
and the cross column against $w$ as
$$
U=(x,y,z,w_3)^{\mathsf T}.
$$
The letter $w_3$ is a pairing, distinct from the physical vector $w$. The relations in the first two rows of (1.3) come from the original physical isotropy $K(u(s),u(s))=0$ through order three. Also $K(w,w)=0$.

The five original support vectors are independent. Since the original $K$ is nondegenerate in dimension six,
$$
\operatorname{rank}(K|_{E_D})\ge4.
\tag{1.4}
$$
No two independent support vectors can both lie in its radical.

## 2. Exact necessary sources from the original gradients

The full highest identity is the global binary polynomial identity
$$
P(X(s),Y(s),Z(s))+R(s)^3=0,
\tag{2.1}
$$
where each variable now denotes the physical quintic polar of its corresponding support vector. In a compatible local parameter at the quadruple point its first terms are
$$
\begin{aligned}
X(s)&=-2As-Bs^2+Cs^3+O(s^4),\\
Y(s)&=A-Bs+Ds^2+Es^3+O(s^4),\\
Z(s)&=B+Cs+Es^2+Gs^3+O(s^4),\\
R(s)&=x+ys+zs^2+w_3s^3+O(s^4).
\end{aligned}
\tag{2.2}
$$
These are the same physical pairings as in (1.3).

The unchanged complete mean equation, after contraction with the outer-mean covector gives $\mathcal Q_{F_0^2}=0$, has active form
$e-2Dd-2d^2+4Fd=0$ in the unit Frobenius algebra. In the current normal form its four coefficients are exactly
$$
BG=AC,\qquad CG=-2AE,
$$
$$
AB+EG=C(D+C),\qquad
G^2-BG-AC-4CE-2AD=0.
\tag{2.3}
$$
Here and below the scalar $F$ in the original gradient is $B+G/2$, not a new Gram entry.

For a direct check, the Frobenius matrix and active polar mean are
$$
J=\begin{pmatrix}1&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},
\quad
d=K_a(1,0,0,1)^{\mathsf T}=(B,C,A+E,B+G),
$$
$$
K_aJ=
\begin{pmatrix}
B&A&0&0\\
C&-B&-2A&0\\
A+E&D&-B&A\\
B+G&E&C&B
\end{pmatrix},
$$
$$
e=(0,-4A^2,4AB,4AC-4AD+4B^2).
$$
Substitution gives (2.3). This is the original mean equation, without a restriction of the allowed moment variations.

The isolated-point mean coefficient is
$$
\tau(U^2)=2\tau(U)^2,
\quad\text{that is}\quad
x^2+2xw_3+2yz=2(x+w_3)^2.
\tag{2.4}
$$
It follows from $4V_{\rm zero}(Ky,Ky,\cdot)-8V_{\rm zero}:(KHK)=0$. The highest identity at that point is
$$
P(y,z,w_3)=w_3^3-3yzw_3+\tfrac12y^3=0.
\tag{2.5}
$$

We also need one coefficient of the original second-gradient tensor
$$
N=T_{3,Ky}-F(yy^{\mathsf T}-2H)+4HKH,\qquad F=B+G/2.
$$
Its isolated contribution is $(x+w_3)R^2$. The complete active form is
$$
\begin{aligned}
4N_a={}&2GZ^2-2(B+G)(TZ+XY)-(2A+4E)XZ-4CYZ\\
&+(2C+D)X^2-2AY^2+2(A+E)TX+2CTY.
\end{aligned}
\tag{2.6}
$$
For example, the three separate sources are
$$
T_{3,Ky}
=C(X^2/2-YZ)-(A+E)XZ+(B+G)(Z^2-XY),
$$
$$
yy^{\mathsf T}-2H=T^2/2+TZ+Z^2-XY,
\qquad 4HKH=\tfrac14 K_a(Jr,Jr).
$$
They give (2.6) by direct expansion. At the quadruple base $(T,X,Y,Z)=(0,0,A,B)$, use $BG=AC$ from (2.3). The full second-gradient identity becomes
$$
2(x+w_3)x^2=GB^2+A^3.
\tag{2.7}
$$
Every source used below is now explicit.

## 3. The branch $B=0$

The constant coefficient of (2.1) gives $x=0$. Equation (2.7) then gives $A=0$. The mean equations (2.3) reduce to
$$
CG=0,\qquad EG=C(D+C),\qquad G^2=4CE.
$$
If $C\ne0$, they give
$$
G=E=0,\qquad D=-C.
\tag{3.1}
$$
The leading physical terms in (2.2) are then
$$
X=Cs^3+O(s^4),\quad Y=-Cs^2+O(s^4),\quad
Z=Cs+O(s^4),\quad R=ys+zs^2+w_3s^3+O(s^4).
$$
The order-three highest coefficient is $C^3+y^3=0$. Rescale the isolated point by a cube root of unity so that $y=-C$. The order-four coefficient is then $3C^2z=0$, so $z=0$. Equation (2.4), with $x=z=0$, gives $w_3=0$. But (2.5) is now $y^3/2=0$, contradicting $C\ne0$.

If $C=0$, the last mean equation gives $G=0$. In (2.2), $X$ starts at order at least four and $Z$ at order at least two. Thus the order-three coefficient of the highest identity is solely $y^3$, so $y=0$. The first two rows of the full five-dimensional Gram matrix are now zero: $A=B=C=x=y=0$. Hence both $u_0,u_1$ lie in its radical, contradicting (1.4). The entire $B=0$ branch is excluded.

## 4. The branch $B\ne0$, $A=0$

The highest constant coefficient gives $x^3=-B^3$. A cube-root rescaling of the isolated point makes
$$
x=-B.
\tag{4.1}
$$
The mean equations (2.3) give $G=0$ and $CE=0$.

At the quadruple point, $X=-Bs^2+O(s^3)$, $Y=-Bs+O(s^2)$, and $Z=B+Cs+Es^2+O(s^4)$. The identity
$$
R^3+Z^3=3XYZ-X^3/2
$$
first forces $R+Z$ to have zero coefficients of orders one and two, so
$$
y=-C,\qquad z=-E.
$$
At order three the right side is $3B^3s^3$, while the left side is $3B^2(R+Z)+O(s^4)$. Hence $w_3+G=B$, or $w_3=B$. Therefore $x+w_3=0$. Equation (2.4) becomes
$$
-B^2+2CE=0,
$$
contradicting $CE=0$ and $B\ne0$. This branch is excluded.

## 5. The regular branch and its normalized parameters

It remains that $AB\ne0$, and keep (4.1). If $C=0$, the second mean equation forces $E=0$, and the third forces $AB=0$, impossible. Thus $ABC\ne0$.

Define the nonzero ratios
$$
a=A/B,\qquad c=C/B.
$$
The first three equations in (2.3) give
$$
G/B=ac,\qquad E/B=-c^2/2,\qquad
D/B=a/c-ac^2/2-c.
\tag{5.1}
$$
Substitution into the fourth gives exactly
$$
a^2(1-c^3)=c^4.
\tag{5.2}
$$

Normalize the three cross pairings as
$$
\widehat y=y/B,\quad \widehat z=z/B,\quad \widehat w=w_3/B.
$$
Equation (2.7), using $x=-B$, gives
$$
\widehat w=1+\tfrac12ac+\tfrac12a^3.
\tag{5.3}
$$

For clarity we derive the required highest coefficients rather than citing an elimination. Write
$$
H(s)=\frac{R(s)+Z(s)}B=h_1s+h_2s^2+h_3s^3+O(s^4).
$$
Dividing the identity by $B^3$ and using
$$
R=-Z+BH
$$
gives the exact formal relation
$$
(Z/B)^2H-(Z/B)H^2+H^3/3=(X/B)(Y/B)(Z/B)-(X/B)^3/6.
\tag{5.4}
$$
Its first two coefficients are
$$
h_1=-2a^2,\qquad
h_2=a+2a^2c+4a^4.
\tag{5.5}
$$
Therefore
$$
\widehat y=-c-2a^2,\qquad
\widehat z=c^2/2+a+2a^2c+4a^4.
\tag{5.6}
$$
For the third coefficient, use (5.1) in (5.4). Since $c^2+2E/B=0$, the result simplifies to
$$
h_3=
1+2ac-\frac{2a^2}{c}-2a^2c^2-\frac83a^3
-12a^4c-\frac{40}{3}a^6.
\tag{5.7}
$$
On the other hand, $h_3=\widehat w+G/B$, so (5.3) makes it
$$
h_3=1+\tfrac32ac+\tfrac12a^3.
$$
Equating these two forms, multiplying by $6c/a$, yields
$$
3c^2-12a-12ac^3-19a^2c-72a^3c^2-80a^5c=0.
\tag{5.8}
$$
All divisions here are by the already nonzero $a,c$.

Next insert (5.3) and (5.6) into the isolated-point mean equation (2.4), divided by $B^2$. It gives exactly
$$
2+2c^3+6ac+13a^2c^2+10a^3+34a^4c+33a^6=0.
\tag{5.9}
$$
For a direct check, its left side is the negative of twice
$$
1-2\widehat w+2\widehat y\widehat z-2(\widehat w-1)^2.
$$
This is the original mean equation with $x/B=-1$.

## 6. Two univariate equations with no common root

Put
$$
r=a/c^2\ne0.
$$
Equation (5.2) becomes
$$
c^3=1-r^{-2}.
\tag{6.1}
$$
Divide (5.8) by $c^2$ and use (6.1); after multiplication by $r$ it is
$$
H(r)=-80r^6+168r^4-19r^3-120r^2+22r+20=0.
\tag{6.2}
$$
Similarly substitute $a=rc^2$ in (5.9), use (6.1), and multiply by $r^2$. It becomes
$$
M(r)=33r^8-98r^6+10r^5+109r^4-14r^3-52r^2+4r+10=0.
\tag{6.3}
$$
For example, the six nonconstant combinations in (5.9) reduce using
$ac=r-r^{-1}$,
$a^2c^2=r^2-2+r^{-2}$,
$a^3=r^3-2r+r^{-1}$,
$a^4c=r^4-3r^2+3-r^{-2}$,
and
$a^6=r^6-4r^4+6r^2-4+r^{-2}$.
These give (6.3) directly.

The following exact rational computation proves that (6.2)–(6.3) have no common root. Start with $M$ and $-H$, both with positive leading coefficient. For integer polynomials $A,B$, while $\deg A\ge\deg B$, replace
$$
A\ \longleftarrow\
\operatorname{lc}(B)A-\operatorname{lc}(A)\,
r^{\deg A-\deg B}B.
$$
After the degree becomes smaller, divide the coefficients by their nonzero integer gcd and choose positive leading coefficient. Apply this primitive pseudo-remainder operation successively to the preceding two polynomials. It terminates at the constant polynomial $1$ after six nonzero remainder steps.

The complete source, containing the literal input polynomials (6.2)–(6.3) and only integer arithmetic, is
[the exact rational-gcd script](../notes/2026-11-20-r150-unit-four-isolated-zero-gcd-b2a9.py).
It was actually executed in this public repository by GitHub Actions run
[44722024572](https://github.com/Rogerhu12/math-research-public/actions/runs/44722024572),
job 136239897518, at 2026-11-20 10:46:24 UTC. The original job log was retrieved by root and reports:
six steps, all intermediate degrees strictly decreasing, final degree zero, and exact final primitive gcd equal to one.
The source SHA-256 is
002d10bfdc6837cde7befb32f8a64eae5a708f48b267d89407071846766ae094;
the literal-input SHA-256 is
579b72d74be190d52a1128f1c58646e9952d47d03ae42eea163458b1323c1524.
The computed remainder stream has SHA-256
ba5154856f4c0ed1ee08d91cc9e08ff6126aba29269d9e58abe5d812001d6cff.
Only source, inputs, execution identity and hashes are retained; the reproducible remainder array is not saved.
The small [execution receipt](../notes/2026-11-20-r150-unit-four-gcd-run44722024572-b2a9.json) contains the same identities.

Every pseudo-remainder step preserves a common complex root, since its polynomial multipliers and removed integer contents are nonzero constants. The final polynomial $1$ therefore rules out any common complex root of (6.2) and (6.3).

This is an exact characteristic-zero exclusion. It does not promote a finite-field ideal computation or a numerical rank to a complex conclusion. Consequently the regular branch is empty.

## 7. Exhaustion and accurate consequence

Sections 3–6 exhaust $B=0$, $B\ne0,A=0$, and $ABC\ne0$, with the remaining $C=0$ subcase explicitly excluded before division. All sources are coefficients of the original complete highest, mean and second-moment gradients. The point at infinity is included because the construction uses invertible local parameters and physical divided jets.

Therefore the rank-four placement with a unit length-four local block and an isolated zero point is empty. Together with the separate simple-zero-on-the-quadruple-block exclusion, the divisor type $4+1$ contributes no rank-four complete critical points in either possible placement of the defect.

Other isolated-zero-point cases have a unit length-four factor split among several physical points, and those are not treated here. The simple-zero-on-a-double-point case and rank five also remain separate. No global Bell radical membership or Hilbert invariant-subspace theorem follows from this branch exclusion alone.
