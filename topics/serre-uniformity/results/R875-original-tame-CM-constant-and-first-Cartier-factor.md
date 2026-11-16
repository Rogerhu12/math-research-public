# R875 — The original tame CM constant and the first Cartier factor

Date: 2026-11-16. Status: **proved in the scope stated below**. The undetermined value of the actual rational companion in R871 is identified, with its full six-level phase and scale, with the first Cartier factor $C_p$. This is a comparison of two original objects. It does not assert that either is nonzero, does not remove the second factor $C_{p-3}$, and does not identify the cyclic-$p$ source or a height.

## 1. Statement and fixed objects

Let $p\ge41$ be a prime with $p\equiv5\pmod6$. Retain the fixed coefficient place and the original objects of R683, R871, and R874:
$$
 K=\mathbb Q(\zeta),\qquad \zeta=\frac{-1+\sqrt{-3}}2,\qquad
 E_0:y^2=x^3-1,\qquad \omega=\frac{dx}{2y},
 \qquad \alpha^3=4,\quad \beta=\sqrt3.
 \tag{875.1}
$$
For the complex comparison take $\alpha,\beta>0$ and
$$
 \Lambda=\Omega\mathcal O_K,\qquad \Omega>0,\qquad
 \mathscr A=\frac{\sqrt3\,\Omega^2}{2\pi}.
 \tag{875.2}
$$
The same $\alpha$ is subsequently embedded at the prescribed $p$-adic place; its reduction is the unique cube root of $4$ in $\mathbb F_p$.

The original six-torsion labels and character are
$$
 Q_{\delta ij}=(\alpha\zeta^i,\delta\beta)+(\zeta^j,0)
             =\frac{\Omega a}{6},
 \qquad
 a\bmod3=\delta\zeta^i,\quad a\bmod2=\zeta^j,
 \qquad
 \chi_6(a)=\delta\zeta^{j-i}.
 \tag{875.3}
$$
Thus the numbers $C_n$ used below are exactly R683's numbers, defined with the $\chi_6$-weighted completed Kronecker kernel, not the inverse-weighted original rational kernel. Their exact normalization is
$$
 \xi_n((a))=\chi_6(a)^{-1}a^{2n-1},\qquad
 L(\xi_n,n)=
 \frac{\alpha\beta\Omega\mathscr A^{n-1}}{(-3)^{n-1}}C_n
 \quad(n\ge2,\ n\equiv2\bmod3),
 \qquad C_2=-\frac12.
 \tag{875.4}
$$
See R683(683.1–5), including its even-weight extension.

Let $\mathcal A$ be the level-one Hasse invariant with Tate expansion one, and put
$\mathcal B=\partial_{p-1}\mathcal A$, where $\partial$ is the Serre derivative normalized in R871(871.10). On the same full tame level-six component let
$$
 \begin{aligned}
 \mathsf C_{p-1}&=f_{a^{p-2}\epsilon_3(a)},\\
 W(\tau')&=\overline{\mathsf C}_{p-1}(\tau'/6)
                  -\zeta^2\overline{\mathsf C}_{p-1}(2\tau'/3),\\
 R&=W/\mathcal A.
 \end{aligned}
 \tag{875.5}
$$
A bar on a modular form in (875.5) means reduction. Complex conjugation of an algebraic CM value will always be written explicitly as $\overline{J}$ below. The use of $\mathsf C$ for the modular form avoids confusion with the scalar $C_n$.

The point $P^\dagger$ is the actual conjugate full-six marking in R871: in the analytic period basis it is
$$
 \tau^\dagger=1+\zeta=-\overline\zeta,
 \tag{875.6}
$$
and in the original theta constants it has $A_2=\zeta B_2$. Both the marking and its coefficient phase are transported. R871 proves that $R$ is regular at this point. The first Cartier constant is
$$
 B=(-1)^{(p+1)/6}
       \binom{(p-1)/2}{(p-2)/3}\in\mathbb F_p^\times.
 \tag{875.7}
$$

The new comparison is the equality in the fixed residue field
$$
 \boxed{\quad B^2 R(P^\dagger)^2=\zeta^2\alpha^2 C_p.\quad}
 \tag{875.8}
$$
In particular
$$
 R(P^\dagger)\ne0
 \quad\Longleftrightarrow\quad
 C_p\not\equiv0\pmod p.
 \tag{875.9}
$$
Neither side of (875.9) is assumed. The square in (875.8) is a square in the actual residue field of the marked CM object; it is not a claim that $C_p$ is a nonzero square in $\mathbb F_p$.

We first prove a characteristic-zero identity that fixes every factor.

## 2. The actual high-weight six-level vector

For an integer $k\ge4$ with $k\equiv4\pmod6$, let
$$
 \mathsf C_k=f_{\Psi_k},\qquad
 \Psi_k((a))=a^{k-1}\epsilon_3(a).
 \tag{875.10}
$$
This is the normalized rational CM newform of weight $k$, trivial nebentypus, and level $9$. Its exact finite conductor over $K$ is $(\sqrt{-3})$. The unit condition follows from $k-1\equiv3\bmod6$; the nontrivial sign on the residue units at $\sqrt{-3}$ proves the stated conductor. Its coefficients are rational integers, by conjugating the ideal sum.

Write
$$
 h_0(\tau)=\mathsf C_k(\tau/6),\qquad
 h_2(\tau)=\mathsf C_k(2\tau/3),\qquad
 H_k=h_0-2^k\zeta^2 h_2.
 \tag{875.11}
$$
These are genuine weight-$k$ cusp forms on the full-level-six component, with integral $q$ expansions over the tame coefficient ring. The matrices below also make every cusp transport integral at $p>3$. The coefficient $2^k$ is part of the characteristic-zero vector.

Here are its full slash matrices, on coefficient columns in $(h_0,h_2)$:
$$
 S_k=\begin{pmatrix}0&2^{-k}\\2^k&0\end{pmatrix},
 \qquad
 T_k=\zeta^2\begin{pmatrix}-1&0\\-2^k&1\end{pmatrix}.
 \tag{875.12}
$$
We give the argument instead of importing the weight-two phase from R588.

First put $h_1(\tau)=\mathsf C_k(\tau/3)$. Norms of ideals prime to $3$ are $1\bmod3$, so $h_1|_kT=\zeta h_1$. Since $\mathsf C_k$ is a real normalized newform, $h_1|_kS=\varepsilon_9h_1$ for its normalized Fricke eigenvalue $\varepsilon_9\in\{1,-1\}$. The relation $(ST)^3=S^2$ in even weight gives $(\varepsilon_9\zeta)^3=\varepsilon_9^2$, hence $\varepsilon_9=1$. The Fricke transformation then gives $h_0|_kS=2^kh_2$ and $h_2|_kS=2^{-k}h_0$.

At the inert prime $2$, the ideal $(2)$ has norm $4$ and
$\Psi_k((2))=-2^{k-1}$. Consequently
$a_{4n}=-2^{k-1}a_n$, and coefficients with odd $2$-adic valuation vanish. The even part of $\mathsf C_k(Q)$ is therefore
$-2^{k-1}\mathsf C_k(Q^4)$. All odd nonzero exponents are $1\bmod6$ and all even ones are $4\bmod6$. Translating $\tau$ by one gives
$$
 h_0|_kT=-\zeta^2h_0-2^k\zeta^2h_2,\qquad
 h_2|_kT=\zeta^2h_2,
 \tag{875.13}
$$
which proves (875.12).

In the normalized basis $(h_0,2^kh_2)$, the two matrices are the same fixed matrices as for the weight-four constituent of R390 §6. In particular its quaternion kernel at three is trivial, and its full tame subgroup action is transported without a new sign. Directly,
$$
 T_k^{-1}S_k\binom{1}{-2^k\zeta^2}
       =\binom{1}{-2^k\zeta^2}.
 \tag{875.14}
$$
Thus $H_k$ is invariant under the actual $H_6^\dagger$ and its indicated three-cycle $ST^{-1}$. This is full-group invariance of the given vector, not a claim inferred from a single coefficient.

The matrix
$ST^{-1}=\left(\begin{smallmatrix}0&-1\\1&-1\end{smallmatrix}\right)$ fixes $\tau^\dagger$ and has automorphy factor $\tau^\dagger-1=\zeta$ there. Since $k\equiv1\bmod3$,
$$
 H_k(\tau^\dagger)=0.
 \tag{875.15}
$$

## 3. The original flat jet and its algebraic conjugation

Let
$$
 \delta_k=\frac1{2\pi i}\frac d{d\tau}
             -\frac{k}{4\pi\operatorname{Im}\tau}.
$$
Define the first flat Hodge jet in the original differential frame by
$$
 J_k=\left(\frac{2\pi i}{\Omega}\right)^{k+2}
                   \delta_kH_k(\tau^\dagger).
 \tag{875.16}
$$
This is the general-weight version of R588(588R.30–32), with the same period columns and flat coordinate. More explicitly the flat expression is
$$
 \left(\frac{2\pi i}{\Omega}\right)^k
 (1-z/\mathscr A)^{-k}
 H_k\!\left(
       \frac{\tau^\dagger-\overline{\tau^\dagger}z/\mathscr A}
            {1-z/\mathscr A}
      \right).
 \tag{875.17}
$$
Its derivative at $z=0$ is (875.16). Here
$\tau'(0)=2\pi i/\Omega^2$, so this assertion includes the factor of $2\pi i$, the period power, and the weight term. By (875.15), any connection term proportional to the value of $H_k$ vanishes at this point. In particular $J_k$ is also the algebraic Serre derivative of $H_k$ evaluated in the original frame.

The coefficient identity giving its complex conjugate is
$$
 T_k^{-1}\binom{1}{-2^k\zeta}
       =-\zeta\binom{1}{-2^k\zeta^2}.
 \tag{875.18}
$$
Since $\mathsf C_k$ has real coefficients and
$-\overline{\tau^\dagger}=\tau^\dagger-1$, the Maass derivative respects this Fourier conjugation. Also $(2\pi i/\Omega)^{k+2}$ is real because $k+2$ is even. Therefore the exact algebraic identity is
$$
 \boxed{\overline{J_k}=-\zeta J_k.}
 \tag{875.19}
$$
It is proved before choosing a $p$-adic embedding. It does not assert that complex conjugation preserves that embedding, or that its residue action is Frobenius.

## 4. The toric character, including the inverse finite action

We apply the characteristic-zero Waldspurger formula of Hsieh, Proposition 2.1, and its archimedean evaluation in Proposition 3.3:
[primary text, §§2 and 3.7.2](https://www.math.ntu.edu.tw/~mlhsieh/research/VBDP.pdf).
No ordinary-prime interpolation theorem is used.

Use the same adelic right-translation convention, quotient Haar measures, and Hermitian conversion as R588 §§4–6. The toric character at infinity is
$(z/\bar z)^{(k+2)/2}$. Its finite unit character is
$$
 \chi_6^{-1}\epsilon_3.
 \tag{875.20}
$$
The two base-change factors, in unitary normalization, are the conjugates of the characters $\xi_2$ and $\xi_{k+1}$ from (875.4). One way to check this without a convention shortcut is to write
$\Psi_k^u=\Psi_k/\operatorname N^{(k-1)/2}$,
$\xi_n^u=\xi_n/\operatorname N^{n-1/2}$, and define the global unitary toric character as
$$
 \chi_{\rm tor}=\overline{\xi_2^u}\,(\Psi_k^u)^{-1}.
 \tag{875.21}
$$
Then $\chi_{\rm tor}\Psi_k^u=\overline{\xi_2^u}$ and
$\chi_{\rm tor}(\Psi_k^u)^c=\overline{\xi_{k+1}^u}$. Its restriction to rational ideles is trivial. Its positive infinity type gives exactly (875.20) on the finite units. Conjugating the ideals in each full $L$ sum shows
$L(\overline{\xi_n},n)=L(\xi_n,n)$. Thus the finite global factor used below is
$$
 L_{\rm prod}=L(\xi_2,2)L(\xi_{k+1},k+1).
 \tag{875.22}
$$

The same character can be checked directly against the actual vector. Multiplication by $\zeta$ in the basis $(\tau^\dagger,1)$ is $ST^{-1}$. In the normalized pair $(h_0,2^kh_2)$, its order-three factor at two has eigenvalue $\zeta^2$ on $(1,-\zeta^2)$, and the selected factor at three has eigenvalue $\zeta$. These are classical slash eigenvalues. Finite adelic right translation by a rational matrix corresponds to the inverse classical slash action. Thus the finite eigenvalues are $\zeta$ at two and $\zeta^2$ at three; the toric character is their inverse.

Explicitly (875.20) on a class with the labels (875.3) is
$\zeta^{-j}$ at two and $\zeta^i$ at three. This verifies both local factors and the choice $\chi_6^{-1}$, rather than $\chi_6$. The selected character at three is the CM-visible projection of the original split-fixed source line. It is not an assertion that the unprojected source line already has norm equal to its projection.

## 5. Finite factors and the half factor at three

The representation at two is unramified with unitary Satake parameters $i,-i$, for every weight in (875.10). The original degeneracy functions have the following exact adelic interpretation:
$$
 \frac{y^{k/2}}{6^{k/2}}H_k(\tau)
 \ \longleftrightarrow\
 \pi(d(6))W_{\rm new}
       -\zeta^2\pi(d(3/2))W_{\rm new},
 \qquad d(a)=\operatorname{diag}(a,1).
 \tag{875.23}
$$
Indeed $6^{-k/2}2^k=(2/3)^{k/2}$. This is why $2^k$, rather than $4$ or $1$, is the correct characteristic-zero coefficient.

At two the two components of (875.23) are the neighboring translates
$v_-,v_+$ used in R588(588R.22–23). Their norms and inner product are
$$
 \|v_-\|^2=\|v_+\|^2=\frac43,\qquad
 \langle v_-,v_+\rangle=-\frac23.
 \tag{875.24}
$$
The actual combination $v_--\zeta^2v_+$ has norm $2$, lies in the required cubic toric line, and the local prefactor is $1/3$. Thus
$$
 P_2=\frac23.
 \tag{875.25}
$$

At three both terms in (875.23) have the same $d(3)$ translate of the normalized newvector. The inducing character has conductor one over the ramified quadratic field, is $-1$ on $-1$, and is not conjugation invariant: conjugation sends a uniformizer $\sqrt{-3}$ to its negative. Its compact type is therefore the same two-dimensional depth-zero cuspidal type of $\operatorname{GL}_2(\mathbb F_3)$ used in R588 §5.4. Changing $k$ in its stated congruence class does not change this unit-character calculation.

The translated newvector is the split-torus-fixed line of norm one. The two characters of the ramified-torus unit quotient $C_3$ are exchanged by its split reflection; their orthogonal projections each have squared norm $1/2$. The CM unit and the fixed characters at two and infinity select the required one. Projecting onto it does not change the CM evaluation, but it does change the local norm. This distinction is necessary here just as in R588.

The odd-valuation coset has zero matrix coefficient: the compact-induction vector is supported on $ZK$, where determinant valuations are even, while that coset has odd determinant valuation. The unit coset has measure $1/\sqrt3$, and the local prefactor is $2/3$. Hence
$$
 P_3=\frac23\cdot\frac1{\sqrt3}\cdot\frac12
     =\frac1{3\sqrt3}.
 \tag{875.26}
$$
Both local base-change $L$ factors are one: (875.20) has nontrivial inertia at two and conductor two on the ramified extension at three. At every other finite place the normalized spherical integral cancels the corresponding $L$ factor. In particular there is no depth-zero factor at $p$ in this tame characteristic-zero calculation.

## 6. Exact norm and cancellation of periods

Hsieh Proposition 3.3 at raising order one gives
$$
 P_\infty=\frac{8\,k!}{(4\pi)^{k+3}}.
 \tag{875.27}
$$
With (875.25–26), Proposition 2.1 in the Hermitian normalization of R588(588R.17–19) therefore gives
$$
 |P_{\chi_{\rm tor}}|^2
  =L_{\rm prod}\,
       \frac{16k!}{9\sqrt3(4\pi)^{k+3}}.
 \tag{875.28}
$$

The field $K$ has class number one. The same global torus fundamental domain as in R588 §6 has volume $2/(3\sqrt3)$: the unit component at three is used, and the three global units modulo rational units are divided out. The finite vector is toric at two, the correct three-component is selected without changing evaluation, and all other finite components are spherical. The actual CM period is consequently
$$
 P_{\chi_{\rm tor}}
 =\frac2{3\sqrt3}\,
    \frac{y^{k/2+1}}{6^{k/2}}\,
                  \delta_kH_k(\tau^\dagger),
 \qquad y=\frac{\sqrt3}{2}.
 \tag{875.29}
$$
There is no average by $p+1$ and no hidden $p$-degeneracy factor in this formula.

Using (875.16) and $\mathscr A=\Omega^2y/\pi$, the squared absolute value of (875.29) is
$$
 |P_{\chi_{\rm tor}}|^2
 =\frac{4\mathscr A^{k+2}}
        {27\cdot6^k(4\pi)^{k+2}}\,
                 J_k\overline{J_k}.
 \tag{875.30}
$$
Equations (875.28–30) give
$$
 J_k\overline{J_k}
 =\frac{\sqrt3\,6^k k!}{\pi\mathscr A^{k+2}}\,
                           L_{\rm prod}.
 \tag{875.31}
$$
Now use the original exact normalization (875.4), with both indices $2$ and $k+1$:
$$
 L_{\rm prod}
 =\frac{3\alpha^2\Omega^2\mathscr A^{k+1}}
                {(-3)^{k+1}}\,C_2C_{k+1}.
 \tag{875.32}
$$
Since $\Omega^2/\mathscr A=2\pi/\sqrt3$, $k$ is even, and $C_2=-1/2$, all period factors cancel and leave
$$
 \boxed{
 J_k\overline{J_k}=2^k\alpha^2 k!\,C_{k+1},
 \qquad
 J_k^2=-\zeta^2\,2^k\alpha^2 k!\,C_{k+1}.
 }
 \tag{875.33}
$$
The second identity uses the already proved algebraic conjugation (875.19). No square root or nonvanishing assumption has been inserted.

As a normalization check entirely within the old fixed formula, when $k=4$ the vector is
$\eta^4(B_2-\zeta^2A_2)$ from R871. Its derivative is $288U(P^\dagger)$, where $U=V/E_4$. From
$\eta^{24}=\Delta$, $E_6=-864$, and $A_2=\zeta B_2$, the theta formulas give
$|U|^2=\alpha^2/48$. Thus its norm is $1728\alpha^2$, equal to
$2^4\alpha^2\,4!\,C_5$ with the already registered $C_5=9/2$. This is a paper check of the same scales, not a new numerical computation.

## 7. Reduction in the original Hasse and elliptic frames

Now set $k=p-1$. The level-six vector (875.11) is integral at the fixed place, and $2^{p-1}\equiv1\bmod p$. Hence
$$
 \overline{H_{p-1}}=W
 \tag{875.34}
$$
as full modular sections on the actual tame component, not just as one formal Fourier series. The good full-six CM object and its differential are integral at $p>3$; the Serre derivative has only the unit denominator $12$. Thus $J_{p-1}$ is integral at that place.

Since $H_{p-1}(P^\dagger)=0$ in characteristic zero, its reduction satisfies
$$
 \operatorname{red}_p(J_{p-1})
   =(\partial_{p-1}W)(P^\dagger)
   =\mathcal B(P^\dagger)R(P^\dagger).
 \tag{875.35}
$$
The last equality is the Leibniz rule for $W=\mathcal A R$, using the proved regularity of $R$ and $\mathcal A(P^\dagger)=0$. Here $\operatorname{red}_p$ denotes reduction at the fixed place; the complex conjugate has already been eliminated by the square identity in (875.33).

For completeness $\mathcal B(P^\dagger)$ is exactly the original $B$, not merely an unspecified unit. Write $p=6r+5$ and use the original fixed model
$$
 E_t:y^2=x^3+tx-1,\qquad \omega=\frac{dx}{2y}.
$$
The linear term of its Hasse invariant, obtained from the coefficient of $x^{p-1}$ in $(x^3+tx-1)^{(p-1)/2}$, is
$$
 \mathcal A(E_t,\omega)=\kappa t+O(t^2),\qquad
 \kappa=(-1)^r\frac{(3r+2)!}{(2r+1)!\,r!}
       =-(r+1)B=-\frac B6
       \quad\text{in characteristic }p.
 \tag{875.36}
$$
This is the same calculation as R874(874.15–16). In this frame
$E_4=-48t$, $E_6=-864$ and
$\partial E_4=-E_6/3=288$ at $t=0$. The Serre derivative therefore has parameter velocity $-6$. The connection term is multiplied by the vanishing value of $\mathcal A$, so
$$
 \boxed{\mathcal B(P^\dagger)=-6\kappa=B.}
 \tag{875.37}
$$
It is independent of the tame marking because it is level one in the unchanged elliptic differential frame.

Finally reduce (875.33), using Wilson's identity $(p-1)!\equiv-1$ and $2^{p-1}\equiv1$. Combining with (875.35–37) proves
$$
 B^2R(P^\dagger)^2
   =\zeta^2\alpha^2 C_p,
$$
as claimed.

## 8. The exact remaining source condition

R683 already proves, in this same original normalization,
$$
 v_p(M_{2,1})=-1
 \quad\Longleftrightarrow\quad C_pC_{p-3}\not\equiv0\pmod p.
 \tag{875.38}
$$
Equation (875.8) now rewrites that actual two-factor criterion as
$$
 v_p(M_{2,1})=-1
 \quad\Longleftrightarrow\quad
 R(P^\dagger)\ne0
 \ \text{and}\ C_{p-3}\not\equiv0\pmod p.
 \tag{875.39}
$$
It identifies the previously undetermined constant of the tame companion with one precise original factor. It does not identify its marked cubic coefficient with that factor: R871's cubic unit concerns
$R(T)-R(0)$ and remains compatible with $R(0)=0$.

The registered R706 example has $C_p\ne0$ and $C_{p-3}=0$, so it is fully compatible with (875.39) and continues to exclude an unconditional minimal-valuation claim for $h=1$. R874's one-flag leading cancellation also remains unchanged. The genuine two-flag cyclic-$p$ and ramified phase comparison, the full primitive/Legendre same-$h$ condition, and the height problem remain separate open requirements.

### Sources and execution scope

- [R683](R683-even-weight-Cartier-channel-and-actual-r3.md), §§1, 3 and 5: the original character, exact fixed-conductor $L$ values, and both Cartier factors.
- [R871](R871-original-tame-Abel-companion-and-marked-cubic-unit.md): the actual $W$, conjugate full-six point, regularity of $R$, and its marked cubic term.
- [R874](R874-original-cyclic-p-quotient-scales-and-Kodaira-Spencer-leading-term.md), (874.15–16), (874.23): the unchanged original Hasse and elliptic scales.
- [R588](R588-actual-toric-norm-and-CM-normalization.md), §§4–8: Haar measures, Hermitian conversion, normalized local types, global volume, and original flat Hodge frame. Its weight-two conjugation phase is not substituted for the independent calculation (875.18).
- [R390](R390-cm-coordinate-inertia-weight-one-channel-and-cartier-unit.md), §6: the actual full tame group and theta normalization, within its stated R575 correction.
- Hsieh, [*Special values of anticyclotomic Rankin–Selberg L-functions*](https://www.math.ntu.edu.tw/~mlhsieh/research/VBDP.pdf), Proposition 2.1 and Proposition 3.3, reopened in the original PDF in this continuation. Only the characteristic-zero formulas are used.

This is a paper proof with source inspection. No mathematical program was executed locally or on Actions, and no new prime window was opened.
