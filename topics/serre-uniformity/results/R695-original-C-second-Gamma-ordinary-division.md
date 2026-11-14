# R695: the original C as a second Gamma-division of the same Robert units

**Status: proved reduction; no numerical C, b, m, or J is asserted.**
Use exactly R561/R613/R619/R633/R657's original fields, character,
unaveraged projector, positive Artin convention, and units. In particular
the auxiliary constant $C_t=9$ only normalizes a comparison of two
ordinary capitulation cocycles; it is not substituted for $C$.

This note proves a finite-layer criterion for the original $C$ which
does not require the unknown original norm unit $y$ in its test element.
No hypothesis $m=43$ or even $m\ge2$ is used.

## 1. Input and statement

Write $p=43$, $\mathcal O=\mathbf Z_p[i]$, $k=\mathcal O/p$,
$\Gamma=\langle\gamma\rangle$, $\pi=\gamma-1$,
$P=S\times T=\langle s,t\rangle$, $M'=LB$,
$M_s=LB^T$, $N=LB^S$. All unit groups mean the completed
ordinary $\chi^-$ unit lattices. Put

$$
a=15i/7,\quad
D_\Gamma^{\rm bal}=\sum_{j=-21}^{21}j\gamma^j,
\quad D_S=\sum_{j=0}^{42}js^j,
\quad D_T=\sum_{j=0}^{42}jt^j,
\quad H_{11}(s)=\sum_{j=0}^{10}s^j.
$$

The actual ancestor $c_B$ and its norms are

$$c_s=N_Tc_B,\qquad c_t=N_Sc_B,\qquad
c_q=N_SN_Tc_B.$$

They have the exact relations

$$
N_\Gamma c_B=(1-s^{11})u_B,\quad
N_\Gamma c_s=(1-s^{11})u_s,\quad
N_\Gamma c_t=N_\Gamma c_q=0,
$$
$$
N_Su_s=N_Tu_t=u,\quad
N_\Gamma y=u,\quad
py=u+aD_\Gamma^{\rm bal}c_q,\quad
\pi y=a\gamma^{22}c_q.
\tag{1}
$$

For any $\kappa\in\mathcal O$, define the explicit actual-unit element

$$
Q_\kappa=
\pi D_Sc_s-\kappa\pi D_Tc_t-11a c_q
\quad\in E_{M'}.
\tag{2}
$$

Then the original class $C$ of R561 is characterized by

$$
\boxed{
Q_\kappa\in\pi^2E_{M'}
\quad\Longleftrightarrow\quad
\bar\kappa=C/9\text{ in }k.
}
\tag{3}
$$

Thus exactly one residue class of $\kappa$ modulo $p$ satisfies
the second ordinary-unit division test. Because $C\in i\mathbf F_p$,
the search can be restricted to the $43$ values
$\bar\kappa\in i\mathbf F_p$. Multiplication by $9$ recovers
the original $C$, and R561 then gives
$\mathcal L=31-22iC$. These formulas preserve the original phase.

## 2. The complete P-cohomology comparison

Define the actual units

$$
v_s=u_s-y+aD_\Gamma^{\rm bal}c_s\in E_{M_s},
\qquad
v_t=u_t-y+aD_\Gamma^{\rm bal}c_t\in E_N.
\tag{4}
$$

They have $N_Sv_s=N_Tv_t=0$. On $P=S\times T$ let $f_s$ be
the cocycle whose values at $s,t$ are $(v_s,0)$, and let $f_t$
have values $(0,v_t)$. These are cocycles because $v_s$ is
$T$-fixed and $v_t$ is $S$-fixed.

The ordinary divisor descent identifies

$$
H^1(P,E_{M'})\simeq
\ker(A_L\longrightarrow A_{M'}).
\tag{5}
$$

Here (5) includes all finite divisors. Hilbert 90 for the whole
finite group supplies a multiplicative solution of a unit cocycle;
its divisor is $P$-invariant. The only ramified primes in
$M'/L$ lie above $p$, whose character divisor summand is zero.
All other invariant divisors descend. Conversely a class in the
displayed capitulation kernel supplies such a cocycle by choosing
a generator of its extended ideal. Changing the generator or the
divisor representative has exactly the ordinary coboundary effect.

R619 gives $A_L=ke_q$ and zero transfer $A_L\to A_N$.
Consequently $A_L\to A_{M'}$ is zero. Thus (5) identifies
$H^1(P,E_{M'})$ with the actual one-dimensional $k$-line $A_L$.
The sign convention in R561 is $(s-1)z_s=v_s$, and R619 uses
$(t-1)z_t=v_t$. With these identical signs the two classes are

$$[f_s]=Ce_q,\qquad [f_t]=9e_q.$$

It follows that an ordinary unit $Z\in E_{M'}$ solves

$$
(s-1)Z=v_s,\qquad (t-1)Z=-\kappa v_t
\tag{6}
$$

if and only if $C-9\bar\kappa=0$. This is an equality of
ordinary cohomology classes, not merely a field Hilbert-90
solvability condition.

## 3. A normalized Gamma primitive

Set

$$
V_s=a\gamma^{22}D_Sc_s+aH_{11}(s)u_s,
\qquad V_t=a\gamma^{22}D_Tc_t.
\tag{7}
$$

The balanced derivative identity is
$\pi D_\Gamma^{\rm bal}=p\gamma^{22}-N_\Gamma$.
Together with (1) and
$(s-1)D_S=p-N_S$, $(t-1)D_T=p-N_T$, it gives

$$
\pi v_s=(s-1)V_s,\qquad
\pi v_t=(t-1)V_t.
\tag{8}
$$

The cross actions vanish: $V_s$ is $T$-fixed, $V_t$ is $S$-fixed.
Also

$$
N_\Gamma V_s=11a u,\qquad N_\Gamma V_t=0.
\tag{9}
$$

Indeed
$D_S(1-s^{11})=-H_{11}(s)(p-N_S)$, so the two
$pH_{11}(s)u_s$ terms in $N_\Gamma V_s$ cancel, leaving
$aH_{11}(s)u=11a u$.

If (6) holds, (8) shows
$\pi Z-V_s+\kappa V_t\in E_L$. Its Gamma norm is $-11a u$
by (9). The full lattice $E_L=\mathcal O[\Gamma]y$ from R210
implies

$$\ker(N_\Gamma:E_L\to E_F)=\pi E_L.$$

After changing $Z$ by an element of $E_L$, without changing (6),
we may and do arrange

$$
\pi Z=W_\kappa,
\qquad
W_\kappa=V_s-\kappa V_t-11a y.
\tag{10}
$$

Conversely suppose $W_\kappa=\pi Z$ for an ordinary unit $Z$.
Equation (8) says that

$$
(s-1)Z-v_s,\qquad (t-1)Z+\kappa v_t
$$

are killed by $\pi$, hence lie in $E_B=E_{M'}^\Gamma$.
They form a $P$-cocycle. R657 proves the entire saturated lattice
$E_B=\mathcal O[P]u_B$, so $H^1(P,E_B)=0$. Subtracting an
element of $E_B$ from $Z$ kills both errors and gives (6).
We have proved

$$W_\kappa\in\pi E_{M'}
\Longleftrightarrow C=9\bar\kappa.$$
\tag{11}

This converse uses the proved ordinary lattice and does not
replace it by a subgroup of Robert units or an $S$-unit lattice.

## 4. Elimination of the unknown y

Equation (9) gives $N_\Gamma W_\kappa=0$. Multiplying (10)'s
test element by $\pi$ and using (1) yields exactly

$$
\pi W_\kappa=a\gamma^{22}Q_\kappa.
\tag{12}
$$

The factor $a\gamma^{22}$ is an invertible operator preserving
the ordinary unit lattice. If $W_\kappa\in\pi E_{M'}$, then
(12) makes $Q_\kappa\in\pi^2E_{M'}$.

Conversely, if $Q_\kappa\in\pi^2E_{M'}$, (12) supplies
$Z\in E_{M'}$ with $\pi W_\kappa=\pi^2Z$.
Thus $W_\kappa-\pi Z\in E_B$. Its Gamma norm is zero, whereas
the Gamma norm on $E_B$ is multiplication by $p$. The ordinary
unit lattice is torsion-free over $\mathcal O$, so this difference
is zero. We recover $W_\kappa=\pi Z$ and (11), proving (3).

The test depends only on $\bar\kappa$. To check this directly,
$V_t$ is killed by $N_\Gamma$ and is therefore an $R_\Gamma$
module element. In this DVR $p$ is divisible by $\pi^{42}$;
hence changing $\kappa$ by $p\lambda$ changes $W_\kappa$ by
an element of $\pi E_{M'}$, and changes $Q_\kappa$ by an
element of $\pi^2E_{M'}$.

## 5. Arithmetic boundary

The criterion involves only $c_s,c_t,c_q$ from the same actual
Robert ancestor, the fixed coefficient $a$, and **ordinary**
unit divisibility in the actual field $M'$. It does not insert
$y$, a free local root, an auxiliary ray scalar, or a replacement
phase into the input expression (2).

Ordinary divisibility remains substantive. In fact **every**
$\kappa$ passes the corresponding field-division test. For every
$\kappa$, (9)--(10) define an ordinary $W_\kappa$ with Gamma
norm zero, regardless of whether (6) has an ordinary solution.
Hilbert 90 supplies a multiplicative field element $Z_\kappa$
with $\pi Z_\kappa=W_\kappa$. Equation (12) then gives

$$Q_\kappa\in\pi^2(M'^\times\otimes\mathcal O)_{\chi^-}
\quad\hbox{for all }\kappa.$$

The divisor of this field solution is invariant; its ramified
$q$ coefficients need not descend integrally from $B$. Thus it
need not be removable by a Gamma-invariant multiplicative
element. The condition (3) is the ordinary integral condition,
not field divisibility or division in a rational tensor space.
No value of $\kappa$ has been certified here. In particular this
does not establish the lost bridge $C=-34ib$, whose old summary
also used the unproved endpoint $m=43$.

All non-elementary input in this reduction is already proved in
R210, R561, R613, R619, and R657. The cohomology identification,
the two sign-sensitive derivative identities, and the converse
ordinary-unit adjustment have been proved explicitly above.
