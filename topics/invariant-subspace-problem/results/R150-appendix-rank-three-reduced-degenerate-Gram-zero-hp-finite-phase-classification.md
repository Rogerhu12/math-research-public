# R150 appendix: finite phase and Gram classification of the reduced rank-three H, degenerate-Gram, zero-Hp branch

Date: 2026-11-26 UTC. Author: Astra-ISP-347c-20261126 / prior_results_map; AI-assisted GPT-6 Astra Pro.

**Status: proved necessary classification.** This continues the genuinely unclosed final branch of [the reduced-H degenerate-Gram Gaussian reduction](R150-appendix-rank-three-reduced-second-cumulant-degenerate-gram-essential-six-gaussian-reduction.md). It uses the original full mean equation and original physical polar values. It does not replace polar vanishing by N=0 and does not assert physical realization or exclusion of the remaining finite Gram forms.

## 1. Paid hypotheses and original equations

Assume an original critical point with rank H=3, rank V=2, and essential dimension six for T_3=y^3-6yH+4V. The H support consists of three distinct physical points and has degenerate Gram. The cited result already proves that V is reduced, F is nonzero, Hp=0, and H has exactly one zero Gram edge.

Apply the allowed overall weighted scale to normalize F=1. With nonzero physical representatives z_1,z_2,z_3,u,v,

$
H=\tfrac12(z_1^2+z_2^2+z_3^2),\qquad
V=\tfrac12(u^3+v^3).
$

The original six columns (y,z_1,z_2,z_3,u,v) form a basis, because T_3 has essential dimension six. The original K is nondegenerate in this basis.

The predecessor's equations are

$
B=(z_iKz_j)=
\begin{pmatrix}0&g&h\\g&0&0\\h&0&0\end{pmatrix},
\qquad g h\ne0,\qquad g^2+h^2=-1,
$
$
p=Ky,\quad p(z_i)=0,\quad p(u)=p(v)=e,\quad
e=uKv\ne0,\quad 2e^3=-1.
$

Let c_i=z_iKu and d_i=z_iKv, and write c,d for their three-column vectors. The original V mean coefficients give

$
c^{\mathsf T}c=d^{\mathsf T}d=e^2. \tag{1.1}
$

The full highest polynomial at each H physical point gives

$
c_i^3+d_i^3=0. \tag{1.2}
$

The full polar matrix is still

$
N=yy^{\mathsf T}-2H+4HKH+2e(u^2+v^2).
$

Its values at the three H points give

$
2e(c_i^2+d_i^2)=(B^2)_{ii}. \tag{1.3}
$

Its values at u and v give the additional equations

$
c^{\mathsf T}Bc=d^{\mathsf T}Bd=1. \tag{1.4}
$

For example N(u,u)=e^2-c^Tc+c^TBc+2e^3; using (1.1) and 2e^3=-1 proves (1.4). Thus both V contributions have been retained.

## 2. All row phases and the field obstruction

Set

$
q=g^2\ne0,\qquad h^2=-1-q\ne0.
$

The diagonal of B^2 is (-1,q,-1-q), with every entry nonzero. Equations (1.2)--(1.3) therefore show that each c_i and d_i is nonzero. There are unique cube roots of unity omega_i such that

$
d_i=-\omega_i c_i.
$

For a cube root of unity omega put

$
\kappa(\omega)=\frac{1}{1+\omega^2}.
$

The denominator never vanishes, and kappa is injective on the three cube roots. Write kappa_i=kappa(omega_i). Then (1.3) is

$
c_1^2=-\frac{\kappa_1}{2e},\qquad
c_2^2=\frac{q\kappa_2}{2e},\qquad
c_3^2=\frac{(-1-q)\kappa_3}{2e}. \tag{2.1}
$

Using c^Tc=e^2 and 2e^3=-1 gives

$
q(\kappa_2-\kappa_3)=\kappa_1+\kappa_3-1. \tag{2.2}
$

Let r_2=c_2/g and r_3=c_3/h, and put

$
A=2c_1r_2,\qquad B_*=2c_1r_3,\qquad
X=qA,\qquad Y=(-1-q)B_*.
$

Every one of q,-1-q,A,B_*,X,Y is nonzero. The two equations (1.4) become

$
X+Y=1,\qquad
\omega_1\omega_2X+\omega_1\omega_3Y=1. \tag{2.3}
$

Suppose omega_2 differs from omega_3. Work in the fixed quadratic field L=Q(zeta_3), which contains all row phases. Equation (2.2), with its nonzero phase denominator, gives q in L. Equation (2.3), whose two-by-two determinant is nonzero, gives X,Y in L. Since q is nonzero, A=X/q belongs to L.

But (2.1) gives

$
A^2=-\frac{\kappa_1\kappa_2}{e^2}.
$

Its nonzero factors imply e^2 is in L, and then e=(-1/2)/e^2 is in L. This is impossible: 2t^3+1 is irreducible over Q, so e has degree three, whereas every element of L has degree at most two. For completeness the cubic has no rational root, since 3v_2(r)=-1 would be required by r^3=-1/2 for a nonzero rational root r.

Thus

$
\boxed{\omega_2=\omega_3=\omega.}
$

Now (2.3) and X+Y=1 immediately give omega_1 omega=1, so

$
\boxed{\omega_1=\omega^2,\qquad
(d_1,d_2,d_3)=(-\omega^2c_1,-\omega c_2,-\omega c_3).} \tag{2.4}
$

No embedding of e into L was assumed. The contradiction is exactly what excludes the unequal-phase cases.

## 3. The complete six-column radical forces the opposite sign

By (2.1) and omega_2=omega_3, r_2^2=r_3^2. Both numbers are nonzero, so r_3 is either r_2 or -r_2.

The vector

$
R=h z_2-g z_3
$

is nonzero and is a radical vector of the original H Gram. It is also orthogonal to y, because Hp=0. If r_3=r_2, then

$
RKu=gh(r_2-r_3)=0,\qquad
RKv=-\omega gh(r_2-r_3)=0.
$

Consequently R would be orthogonal to all six original basis columns, contradicting nondegeneracy of K. Therefore only the opposite sign is possible:

$
\boxed{r_3=-r_2.} \tag{3.1}
$

This uses the full six-column space; degeneracy of the H Gram alone would not justify it.

Put r=r_2 and delta=2q+1. The first equation (1.4) is now

$
2c_1 r\,\delta=1. \tag{3.2}
$

In particular delta is nonzero. Squaring and using (2.1) gives

$
\delta^2=-\frac{e^2}{\kappa(\omega^2)\kappa(\omega)}.
$

The product of kappas equals 1/4 for omega=1 and equals 1 for a nontrivial cube root. Thus

$
\boxed{
\begin{array}{ll}
\delta^2=-4e^2,&\omega=1,\\
\delta^2=-e^2,&\omega\ne1,
\end{array}
\qquad
q=\frac{\delta-1}{2},\quad h^2=-\frac{\delta+1}{2}.
} \tag{3.3}
$

The values delta=1 or -1 are automatically impossible: in the first row they would give e^2=-1/4, and in the second e^2=-1; cubing either value contradicts e^6=1/4. This checks the earlier nonzero g,h restrictions in the final parameter list.

## 4. Full finite Gram list

Every remaining actual critical point must have the following Gram, after only the paid overall scale and independent signs of the three H representatives:

$
\begin{pmatrix}
2&0&0&0&e&e\\
0&0&g&h&C&-\omega^2C\\
0&g&0&0&gr&-\omega gr\\
0&h&0&0&-hr&\omega hr\\
e&C&gr&-hr&0&e\\
e&-\omega^2C&-\omega gr&\omega hr&e&0
\end{pmatrix}, \tag{4.1}
$

where

$
2e^3=-1,\quad \omega^3=1,\quad
\delta\text{ satisfies (3.3)},\quad
g^2=\frac{\delta-1}{2},\quad h^2=-\frac{\delta+1}{2},
$
$
C^2=-\frac{\kappa(\omega^2)}{2e},\qquad
r=\frac{1}{2\delta C}.
$

All these square-root choices are nonzero. Changing the sign of g or h is precisely the sign change of the corresponding H column. Changing C to -C and r to -r, while keeping the displayed g,h, is effected by changing all three H column signs. Hence, up to these allowed signs, there are at most 3 choices of e, 3 choices of omega and 2 choices of delta. This is an upper bound of eighteen Gram forms, not a count of physical solutions.

As a check that the remaining task is not settled by an unnoticed zero determinant, the determinant of (4.1) is

$
\boxed{
\det G_6=
\begin{cases}
(4e^2+1)(1-e),&\omega=1,\$2mm]
-\tfrac12(e^2+1)(4-e),&\omega\ne1.
\end{cases}
} \tag{4.2}
$

Both expressions are nonzero under 2e^3=-1.

Here is a direct derivation. Set Z=z_1, L_0=gz_2+hz_3, R=hz_2-gz_3. The change from (z_2,z_3) to (L_0,R) has determinant -(g^2+h^2)=1. The (Z,L_0) Gram is [[0,-1],[-1,0]]. Its projections of u,v have squared norms -1 and mutual pairing (omega+omega^2)/2 by (3.2). Remove these projections and then the y components e y/2. In the remaining three-space the squared norms of u,v are a=1-e^2/2 and their mutual pairing is b=e-(omega+omega^2)/2-e^2/2. Their pairings with R are rho=2ghr and -omega rho. The residual determinant is -rho^2 omega[(omega+omega^2)a+2b]. Multiplying by the removed determinant -2, then substituting rho^2=2q(-1-q)kappa(omega)/e and (3.3), gives (4.2).

## 5. Exact remaining obligation

The finite Gram list is necessary and nondegenerate. It has not been shown to arise from six original columns with the specified physical curve supports, nor has it been shown to satisfy the remaining coefficients of the full original polar and highest polynomials.

The next obligation in this branch is to impose those original physical identities on the at-most-eighteen Gram forms, including finite/infinite source charts and the unique zero H edge. No original source-at-infinity case has been discarded here: the argument uses only actual vector pairings and therefore applies to every such physical source.

This result does not close the H(2+1) branch, the nondegenerate Gram of reduced H, lower essential dimensions, the Bell natural-power problem, or the ordinary invariant-subspace problem.
