# R751 — The second dyadic line: its full finite character, original negative-one square, and inertia extraction

Date: 2026-11-15. **Status: proved.**

This result identifies the second dyadic direction in each of the two original $17$-local sectors $\tau_2,\tau_4$. It is a type-$3$ source, whereas the sources $D_{2,17},D_{4,17}$ in R735 are type $5$. The two directions do not have the same allowed finite-character branch.

The new source has a complete fixed Schwartz description and an algebraic normalization. Every one of its surviving finite-character negative-one values belongs, with the original common period, to a specified space of algebraic point logarithms. Its point field is ramified at $2$ and $17$; it is not the only-$p$-ramified field of R748. Those ramification characters are computed below.

The finite point-factor inertia projector at the chosen ordinary $p$ kills this entire second branch. Together with R748 and the actual finite-source decomposition paid in R752, this gives an exact finite extraction of the original two untwisted negative-one values. No projection of an arbitrary infinite $p$-adic sum is used.

## 1. Fixed conventions and the new algebraic section

Keep the conventions of R735 and R746:
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad
\theta=17^{1/6},\quad
\Omega_{p,0}=\theta\Omega_p.
\tag{1}
$$
The symbol $E_j$ in this paper means
$$
E_j:y^2=x^3+17^j,\qquad j=2,4.
$$
The common curve with constant term $1$ is denoted $E_{\mathrm{base}}$.

For $k\in\{2,4\}$ put
$$
j=6-k.
\tag{2}
$$
Let $f_k$ and $n_k$ be the complete, nonzero, real odd $17$-adic vectors and their positive norms in R735 (14)--(16). Thus the actual $17$-torus character is
$$
\tau_k(g)=g^{9-3k},\qquad
\tau_2(g_0)=-\omega^2,\quad
\tau_4(g_0)=-\omega,
\tag{3}
$$
including the quadratic splitting in the exponent $9$.

In the same four-coset dyadic model set
$$
f_A=e_0-e_2,\qquad f_B=e_1+e_3,\qquad
t_+=\frac{1+\sqrt3}{\sqrt2},\qquad
\phi_{2,+}=f_A+t_+f_B.
\tag{4}
$$
The vector in R735 was $\phi_{2,-}=f_A+t_-f_B$ with
$t_-=(1-\sqrt3)/\sqrt2$.

Take
$$
\phi_{3,+}=\mathbf1_{3^{-1}\mathbf Z_3},\qquad
\phi_{17,+,k}=\sum_a f_k(a)\mathbf1_{a/17+\mathbf Z_{17}},
\tag{5}
$$
and the original spherical vectors at all other finite places.

The corresponding sequence and theta function are
$$
\begin{aligned}
a_{+,k,n}&=v_+(n\bmod4)\,f_k(3n\bmod17),
&v_+&=(1,t_+,-1,t_+),\\
F_{+,k}(Z)&=\sum_{n\in\mathbf Z}a_{+,k,n}
 \exp\!\left(\frac{\pi i(\delta/3)n^2}{68}+2\pi inZ\right),\\
S_{+,k,\Lambda}(Z)&=e^{34\sqrt3\pi Z^2}F_{+,k}(Z),
&\Lambda&=\mathbf Z+s_0\mathbf Z,\quad s_0=(1-\omega)^{-1}.
\end{aligned}
\tag{6}
$$
The sequence is nonzero: $f_k$ is nonzero and every entry of $v_+$ is nonzero. It is real and odd. It satisfies exactly the old half-period relation
$$
(-1)^n a_{+,k,n+34}=-a_{+,k,n}.
\tag{7}
$$
Consequently (6) is a nonzero section of the **same standard** degree-$34$ line bundle, without an unspecified two-torsion twist.

Let $\Omega_0>0$ be the original period with
$E_{\mathrm{base}}(\mathbf C)=\mathbf C/(\Omega_0\Lambda)$.
Normalize the algebraic section $P_{+,k,1}$ by
$$
S_{+,k,\Lambda}(Z)=s_{+,k}P_{+,k,1}(\Omega_0Z),\qquad
[z^{r_k}]P_{+,k,1}=1,
\tag{8}
$$
where $r_k$ is its first nonzero Taylor order. In particular
$s_{+,k}\ne0$; it is purely imaginary in the chosen real-period normalization.

This algebraic normalization can be specified without guessing $r_k$. Use the algebraic theta-group model of
$H^0(E_{\mathrm{base}},\mathcal O(34[0]))$, with the standard sigma trivialization, apply the two fixed finite projectors selecting (3) and (4), and divide by the first nonzero Taylor coefficient. All matrices and torsion theta-group data are algebraic; the CM theta algebraization used in R745 identifies this line with (6). Equivalently it is the normalized algebraic line selected by the complete finite Schwartz tensor (4)--(5). No arbitrary $\mathbf C_p$ scalar is used.

The angular calculation below implies
$$
P_{+,k,1}(z)=
 \sigma_1(z)^{34}\,y(z)x(z)^2\,Q_k(x(z)^3),
\qquad \deg Q_k\le4,
\tag{9}
$$
up to the harmless sign already fixed by (8). Thus
$$
r_k\in\{3,9,15,21,27\}.
\tag{10}
$$
This definition does not claim that the first order is $3$.

On the original $b=17$ curve use the exact scale
$$
P_{+,k,17}(z)=\theta^{-r_k}P_{+,k,1}(\theta z).
\tag{11}
$$
Its first coefficient is again $1$. The measure is the original physical one with Amice transform
$P_{+,k,17}(\Omega_p\log(1+T))$. In particular the equality of measures is
$$
\nu_{P_{+,k,1}}=\theta^{r_k}\nu_{P_{+,k,17}}
\tag{12}
$$
on the same $\mathbf Z_p$ variable; no scaling of that variable is implicit.

## 2. Full $2,3,17$ character identification

Let $\psi_j$ be the original Hecke character of $E_j$.
The complete sextic formula is the one already used in R735:
$$
\psi_j(\mathfrak q)
=-\left(\frac{4\cdot17^j}{\mathfrak q}\right)_6^{-1}\pi,
\qquad \pi\equiv2\bmod3.
\tag{13}
$$
Thus this step does not infer a Hecke character from its value at one good prime.

For positive weights
$$
m\equiv3\bmod6
\tag{14}
$$
take the unitary character associated to
$\psi_j^{\,2m+1}$.
The full local table is
$$
\begin{array}{c|c|c}
v&\text{value on local units}&\text{uniformizer value}\\ \hline
2&\operatorname{Teich}_{\mu_3}(u\bmod2)&-1\text{ at }2\\
3&u\bmod\delta\in\{\pm1\}&-i\text{ at }\delta\\
17&(u\bmod17)^{-48k}&-1\text{ at }17 .
\end{array}
\tag{15}
$$
Indeed $2m+1\equiv7\bmod12$, so the dyadic cubic character is unchanged, the cubic-prime uniformizer is $i^7=-i$, and
$48j(2m+1)\equiv48j\equiv-48k\bmod288$.

At $17$, the character in (15) is identical to the one in R735 (9), hence its actual invariant vector is exactly $f_k$, with the same Hilbert-90 and quadratic splitting. At $3$ the entire local character and vector are identical to R735.

At $2$, this is the original splitting, before the $\omega^2$ correction used for the minus vector in R735. Its full matrix on $(f_A,f_B)$ is
$$
M_\omega^{\mathrm{old}}
=\frac{\omega^2}{\sqrt2}
 \begin{pmatrix}-\zeta_8&i\\ i&i\zeta_8\end{pmatrix},
\qquad
M_\omega^{\mathrm{old}}(1,t_+)^{\mathsf t}
 =(1,t_+)^{\mathsf t}.
\tag{16}
$$
The old $g_*=(-11+4\delta)/13$ matrix fixes both $f_A$ and $f_B$, and so does $-1$. The topological generation result in R290 therefore fixes (4) under the full local norm-one torus. This is a full local verification, not just a $\mu_3$ test.

The two inverse cubic characters of $\mathbf F_4^\times$ have the same original Gauss sum $2$. With the unchanged uniformizer and additive-character normalization, the dyadic dichotomy is therefore the same as for R735. All other local dichotomies are unchanged. The Hermitian parameter and Gaussian are consequently
$$
\alpha=17,\qquad \mathcal G=51\sqrt3.
\tag{17}
$$
The exact finite norms are
$$
\|\phi_{2,+}\|^2=3+\sqrt3,\qquad
\|\phi_{3,+}\|^2=3,\qquad
\|\phi_{17,+,k}\|^2=n_k.
\tag{18}
$$

The original geometric $\mu_3$ operator has local label $\omega^2$.
Its dyadic eigenvalue on (4) is $1$, and
$\tau_k(g_0^{12})=1$.
Together with oddness this gives
$$
P_{+,k,b}(\omega z)=P_{+,k,b}(z),\qquad
P_{+,k,b}(-z)=-P_{+,k,b}(z),
\tag{19}
$$
which is type $3$. Riemann--Roch in the sigma trivialization proves (9)--(10).
In particular this is not a type-$1$ direction.

For comparison with the whole CM trace normalization, the absolute scalar of R735 is still $-\omega^2$ and the dyadic $g_{13}$ eigenvalue is now $1$. Hence
$$
N_{13}P_{+,2,b}=-P_{+,2,b},\qquad
N_{13}P_{+,4,b}=-\omega P_{+,4,b}.
\tag{20}
$$
These values are consequences of (13)--(17) and the existing absolute anchor. They are not used to identify an otherwise unspecified global character.

## 3. Every positive weight and the fixed algebraic scalar

Use the same Hermite normalization as R735:
$$
\exp(xT-T^2/(8\pi))=\sum_{m\ge0}H_m(x)T^m/m!.
$$
Put
$$
\begin{aligned}
b_{+,k,m}
 &=\sum_{n\in\mathbf Z}a_{+,k,n}
 H_m(\sqrt{51\sqrt3}\,n/102)
 e^{-\pi\sqrt3 n^2/204},\\
h_\infty&=\frac{\sqrt{51\sqrt3}}{204\pi i},\qquad
d_{+,k,m}=[z^m]P_{+,k,1}(z).
\end{aligned}
\tag{21}
$$
Then
$$
b_{+,k,m}=m!s_{+,k}(\Omega_0h_\infty)^m d_{+,k,m},
\qquad b_{+,k,m}=0\quad(m\not\equiv3\bmod6).
\tag{22}
$$
The complete finite norm, the class-number-one torus volume, and Yang's original constant give
$$
\begin{aligned}
\mathcal N_{+,k,m}
 &=\frac{3(3+\sqrt3)n_k}{\sqrt{102\sqrt3}}
      \frac{m!}{(4\pi)^m},\\
L(\psi_j^{\,2m+1},m+1)
 &=C_{+,k}\frac{(4\pi)^m}{m!}b_{+,k,m}^2,\\
C_{+,k}
 &=\frac{\pi\sqrt{102\sqrt3}}
          {17\sqrt3(3+\sqrt3)n_k}.
\end{aligned}
\tag{23}
$$
The finite factors in this formula have not been normalized away.

Set $\varpi_0=s_0\Omega_0$ and
$\varkappa_{+,k}=-C_{+,k}s_{+,k}^2/\Omega_0>0$.
For (14),
$s_0^{-2m}=-3^m$.
Consequently
$$
c_{+,k}:=-\frac{\varkappa_{+,k}}{s_0}
 =34^{r_k}
   \frac{(2\pi/\sqrt3)^{r_k}
           L(\psi_j^{\,2r_k+1},r_k+1)}
        {r_k!\,\varpi_0^{\,2r_k+1}}
 \in\overline{\mathbf Q}^{\times},
\tag{24}
$$
and the complete weight formula is
$$
\boxed{
\frac{(2\pi/\sqrt3)^mL(\psi_j^{\,2m+1},m+1)}
     {m!\,\varpi_0^{\,2m+1}}
 =c_{+,k}\,34^{-m}d_{+,k,m}^2 .
}
\tag{25}
$$
Algebraicity in (24) is the standard CM critical-value algebraicity in the same period normalization as R735. Nonzero (24) follows from the actual first nonzero coefficient in (8) and (23); it is not an unproved claim about a guessed order-$3$ coefficient.

## 4. The original finite-character negative-one value

Define
$$
I_{+,k,\chi}
 =\int_{\mathbf Z_p^\times}x^{-1}\chi(x)
             \,d\nu_{P_{+,k,17}}(x).
\tag{26}
$$
The prime is the original good ordinary prime, with the original embedding and period.
From (19), the exact angular condition is
$$
I_{+,k,\chi}=0
\quad\text{unless}\quad
\chi(\zeta)=\zeta^4
\quad(\zeta\in\mu_6).
\tag{27}
$$
In particular $\chi=1$ never survives in this branch.

For a surviving character put
$$
\Gamma_j=\widehat\psi_j/\widehat{\bar\psi}_j,\qquad
\rho_\chi=\chi\circ\Gamma_j,\qquad
\nu_\chi=\psi_j\rho_\chi^{-1},\qquad
H_\chi=K^{\ker\rho_\chi}.
\tag{28}
$$
This definition keeps the complete finite character, not just its value on inertia at $p$.

The primitive positive-weight Katz formula from (25) is
$$
\mathcal K_{34\delta}
  (\widehat\psi_j^{\,m+1}\widehat{\bar\psi}_j^{-m})
 =c_{+,k}\Omega_{p,0}\,34^{-m}
 \left(1-\frac{\alpha_j^m}{\bar\alpha_j^{m+1}}\right)^2
 M_{+,k,m}^{\,2},
\tag{29}
$$
where
$M_{+,k,m}=\Omega_{p,0}^m m!d_{+,k,m}$,
$v_p(\alpha_j)=1$, and $v_p(\bar\alpha_j)=0$.
Both ordinary Euler factors in (29) are retained.

Apply the same bounded-measure and rigid-analytic argument as in R746, now on the angular component (14). High positive integral weights give the actual unit moments when the nonunit moments and the displayed Euler corrections tend to zero. They have an interior accumulation point on the relevant rigid weight component, so the resulting equality extends throughout that component, including its finite wild-character points. This is analytic continuation of the two full functions, not approximation of a nontrivial wild root by integer exponents.

At $x^{-1}\chi(x)$ the factor $34^{-m}$ becomes $34\chi(34)^{-1}$.
Using (12) gives the exact original-source equality
$$
\boxed{
\mathcal K_{34\delta}
       (\widehat{\bar\psi}_j\rho_\chi)
 =34c_{+,k}\theta^{\,2r_k+1}\Omega_p
       \chi(34)^{-1} I_{+,k,\chi}^{\,2}.
}
\tag{30}
$$
The formula covers every surviving finite tame and wild character. A zero value is included. The modulus $34\delta$ denotes the fixed primitive tame normalization; positive conductor at $p$ is handled by the actual ramified local interpolation factor, not by inserting an unramified Euler factor.

## 5. Actual ramification, central sign, and the point formula

For local units, all assertions use the reciprocity convention of R735/R746. The complete ramification table of $\rho_\chi$ is
$$
\begin{array}{c|c}
\text{inertia subgroup}&\rho_\chi\text{ on its local units}\\ \hline
2&\operatorname{Teich}_{\mu_3}(u\bmod2)^2\\
3&1\\
17&(u\bmod17)^{96j}\\
\mathfrak p&\chi(u)^{-1}\\
\bar{\mathfrak p}&\chi(u)\\
v\nmid 2\cdot3\cdot17\cdot p&1 .
\end{array}
\tag{31}
$$
At the uniformizers $2,17,\delta$ the additional character is $1$.
To verify this, at the first two places the ratio $\Gamma_j$ on the indicated uniformizer is $1$. At $\delta$ it is $-1$, and $\chi(-1)=1$ by (27).
On the dyadic and $17$ units, $\Gamma_j=\psi_j^2$ in the unitary notation, and (27) acts as the identity on $\mu_3$.
This gives exactly the first and third rows of (31).

Thus $\rho_\chi$ has nontrivial cubic tame inertia at both $2$ and $17$. Its conductor is
$$
\mathfrak f_{\rho_\chi}
 =(34)\,\mathfrak p^{\,n}\bar{\mathfrak p}^{\,n},
\tag{32}
$$
where $p^n$ is the exact conductor of $\chi$; $n\ge1$.
The coordinate field $H_\chi$ is unramified outside $2,17,p$ and unramified at $3$.
It is not claimed to be unramified at $2$ or $17$.

The character $\nu_\chi$ in (28) has type $(1,0)$ and
$$
\nu_\chi\nu_\chi^*=\mathbf N_K.
\tag{33}
$$
Its finite unit characters at $2$ and $17$ are the inverse cubic characters to those of $\psi_j$; its $3$-part is unchanged and the discriminant prime occurs exactly once.
These inverse cubic characters have the same original local Gauss sums as their partners: $2$ at the dyadic place and $17$ at $17$.
Their uniformizer values are unchanged.
At the split pair over $p$, the product of the normalized Tate epsilon factors changes by $\chi(-1)=1$.
It follows from the full root calculation in R735 that
$$
w(\nu_\chi)=-1.
\tag{34}
$$

The good-pair proof of R748 applies to this actual $\nu_\chi$.
Its use there was not limited to the only-$p$-ramified twist: it required a self-dual type-$(1,0)$ character with sign $-1$, discriminant prime exactly once, and an auxiliary cyclic conductor away from the finite forbidden set.
All those hypotheses have just been checked for (28).
Choose the auxiliary Hecke character unramified at our $p$, put its whole $p$-ramification into the finite toric character, and use the exact LZZ local period, including its finite Gauss factor.

For clarity, the same component calculation is retained. If
$\psi_{\rm aux}\xi^{-1}=\nu_\chi$, the plus period has CM character
$\psi_{\rm aux}$ and point-factor character $\xi$.
The minus period has CM character $\mathbf N/\psi_{\rm aux}^*$ and point-factor character $(\xi^*)^{-1}$.
Both therefore descend to $\nu_\chi$, in the same coefficient embedding.
If the target Katz value is nonzero, their non-torsion Heegner point gives $L'(\nu_\chi,1)\ne0$ by Gross--Zagier; Kolyvagin's rank-one consequence then turns their actual product into a square in that same component.
If the value is zero, take the zero point.
No rank-one or Sha assumption on these varying twists is made.

We obtain
$$
P_{+,k,\chi}\in
 (E_j(H_\chi)\otimes_{\mathbf Z}\mathbf Q)
               \otimes_K\overline{\mathbf Q},
\qquad
g_{\rm pt}P_{+,k,\chi}
 =\rho_\chi(g)P_{+,k,\chi},
\tag{35}
$$
and a nonzero algebraic $\epsilon_{+,k,\chi}$ satisfying
$$
\mathcal K_{34\delta}(\widehat{\bar\psi}_j\rho_\chi)
 =\epsilon_{+,k,\chi}\,
    \Omega_{p,E_j}^{-1}
    \log_{\omega_j}(P_{+,k,\chi})^2 .
\tag{36}
$$
The scalar uses the algebraic differential, exact BDP phase, full LZZ local factors and finite-twist Gauss sum; no anonymous Iwasawa unit is declared algebraic.

Map to $E_{\mathrm{base}}$ by
$$
\phi_j(x,y)=(\theta^{-2j}x,\theta^{-3j}y),\qquad
\phi_j^*\omega_{\mathrm{base}}=\theta^j\omega_j,\qquad
\Omega_{p,E_j}=\theta^{1-j}\Omega_p.
$$
Equations (30) and (36) give
$$
\boxed{
\Omega_p I_{+,k,\chi}
 =A_{+,k,\chi}\,
   \log_{\omega_{\mathrm{base}}}(\phi_jP_{+,k,\chi}),
\qquad
A_{+,k,\chi}^{\,2}
 =\frac{\epsilon_{+,k,\chi}\chi(34)}{34c_{+,k}}
       \theta^{-j-2r_k-2}
 \in\overline{\mathbf Q}^{\times}.
}
\tag{37}
$$
A square root in the fixed embedding is algebraic, and its sign is chosen to give the actual equality. Compatible signs for different characters are not asserted or needed for the point-space membership statement.

## 6. The combined point characters after returning to the common curve

The isomorphism $\phi_j$ is defined over $K(\sqrt[3]{17})$ because $j$ is even.
This field is unramified at $2$ and at our $p$.
Its point-factor cocycle is
$$
a_j=\psi_0/\psi_j.
\tag{38}
$$
This can either be checked on the coordinates of $\phi_j$, or on its action on the two CM Tate modules. In particular its $17$-unit character is $u^{-48j}$.

After applying $\phi_j$, the total point character is $a_j\rho_\chi$.
Consequently the actual inertial characters on the common curve are
$$
\begin{array}{c|c|c}
\text{family}&I_2&I_{17}\\ \hline
D_{k,17}\text{ with }\chi|_{\mu_6}=1
 &1&u^{-48k}\\
P_{+,k,17}\text{ with }\chi(\zeta)=\zeta^4
 &\operatorname{Teich}_{\mu_3}(u)^2
 &u^{-48j}u^{96j}=u^{48j}=u^{-48k}.
\end{array}
\tag{39}
$$
The last equality uses $j=6-k$ in the residue group of order $288$.
Thus the two dyadic directions have the same actual $17$-sector after the full point return, and distinct dyadic inertia.
Deleting the cocycle (38) would give the wrong $17$ label.

At the chosen $p$, both families have point-inertia character
$$
\chi^{-1}.
\tag{40}
$$
The algebraic scalar in (37), or in the formula of R748, is fixed for this action.
It is not conjugated together with the point.

## 7. Exact extraction for a finite original source

This section uses only a **finite** source decomposition.
For $k=2,4$, suppose the actual source has been written as
$$
\Phi_{-,k}(x)\,\nu_{D_{k,17}}
  +\Phi_{+,k}(x)\,\nu_{P_{+,k,17}},
\tag{41}
$$
where the four $\Phi_{\pm,k}$ are algebraic-valued functions modulo a fixed $p^M$.
The half-character and full-torsion transport needed to obtain (41) belong to R752; they are not inferred from the dimension of a theta space here.
The coefficients include all finite companion jets, Gauss factors and original scalar multipliers.

On units write the actual finite multiplicative Fourier expansions
$$
\Phi_{\pm,k}(x)
 =\sum_{\chi\bmod p^M}
      \widehat\Phi_{\pm,k}(\chi)\chi(x),\qquad
\widehat\Phi_{\pm,k}(\chi)
 =\frac1{\varphi(p^M)}
   \sum_{a\in(\mathbf Z/p^M)^\times}
        \Phi_{\pm,k}(a)\chi(a)^{-1}.
\tag{42}
$$
All these coefficients are algebraic.
The type-$5$ family keeps $\chi|_{\mu_6}=1$; the type-$3$ family keeps (27).
No finite Fourier coefficient is discarded on another criterion.

Let $\mathcal J$ be the sum of the negative-one values of (41), multiplied by the original common $\Omega_p$.
R748 and (37) put $\mathcal J$ in the algebraic point-logarithm space on $E_{\mathrm{base}}$.
Take a common finite Galois coordinate field for all the finitely many point tensors and $\phi_j$.
Write $I_{\mathfrak p}$ for the image in this finite Galois group of inertia at the fixed ordinary embedding.
Define its point-factor projector by
$$
e_{I_{\mathfrak p}}
 =\frac1{|I_{\mathfrak p}|}\sum_{g\in I_{\mathfrak p}}g_{\rm pt}.
\tag{43}
$$
It keeps all algebraic scalar coefficients fixed.
R749 provides the injective logarithm map and hence the well-defined transported projector on this finite point-logarithm space.

By (40), a summand survives (43) if and only if $\chi=1$.
The plus branch has no such summand.
We therefore have the exact formula
$$
\boxed{
(e_{I_{\mathfrak p}})^{\log}\mathcal J
 =\widehat\Phi_{-,2}(1)\,\Omega_p I_{2,1}
   +\widehat\Phi_{-,4}(1)\,\Omega_p I_{4,1}.
}
\tag{44}
$$
This uses the actual local inertia subgroup. It does not split a mixed ramification field into fictitious independent only-$p$ and tame fields.

The two values on the right are nonzero and algebraically linearly independent by R733/R735. Thus
$$
\bigl(\widehat\Phi_{-,2}(1),\widehat\Phi_{-,4}(1)\bigr)\ne(0,0)
\quad\Longrightarrow\quad
\mathcal J\ne0 .
\tag{45}
$$
If both coefficients vanish, (44) gives no claim that the whole original value is zero.

There is also a dyadic version: the trivial point-inertia projector at $2$ kills the entire plus branch and preserves the entire minus branch, by (39). After that projector one may use the only-$p$ point-factor extraction of R749. Both procedures give (44).

More generally the nonzero finite-character values in all four families are algebraically linearly independent. Their joint inertia labels at $2$, $17$, and the chosen $p$ distinguish the family, $k$, and the finite character, respectively; R749 then applies to the common point tensor space. This statement is linear independence, not algebraic independence, and does not assert nonzero values for every character.

## 8. What this does and does not close

This result pays the second dyadic line in the original two $17$-sectors, including:

- its full fixed local characters and Schwartz vector;
- its standard degree-$34$ half-character and type $3$;
- its complete positive-weight formula and fixed nonzero algebraic constant;
- every surviving tame and wild finite-character negative-one square;
- the actual point field, including the nontrivial inertia at $2$ and $17$;
- the combined character after mapping to the common curve;
- the finite point-inertia extraction (44).

The conclusion does not rely on a new numerical run. The undecided label $r_k$ is part of an exact finite definition, and all formulas retain it. No data file or sample of prime values is used to identify the source.

R752 is responsible for proving that a particular full original finite gate belongs to (41). Once it does, (44) applies to that complete finite source, with its actual coefficients. This proof does not replace those coefficients by a convenient test vector.

Finally (43) is not an operation on arbitrary $\mathbf C_p$ numbers, and it is not continuous on the full space of all algebraic point logarithms with its induced $p$-adic topology. The finite-carrier and coefficient-limit conditions in R753 must still be checked before passing to a limit or an infinite log expansion. No original $J'_S$, $J'_T$ or $J'_U$ is assigned a new zero by this result.

## References and dependencies

- [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md): the complete sextic character, original local splitting, $17$ vectors and norms, period conventions, exact positive-weight and ordinary formulas.
- [R746](R746-original-type-five-all-finite-p-character-squares.md): the full-weight-space finite-character continuation with the original physical measure variable.
- [R748](R748-original-type-five-ramified-good-pair-and-point-eigenspaces.md): the exact good-pair/LZZ point formula, both reciprocity directions, same-component product-to-square, finite-twist descent and algebraic normalization.
- [R749](R749-point-factor-projectors-and-finite-character-extraction.md): injective algebraic point-logarithm map and point-only finite Galois projectors.
- R745 and R752: algebraic theta-group transport and the actual finite first-source decomposition; R753: the separate issue of limits of point-factor projections.
- T. Yang, [Theta liftings and Hecke L-functions](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf), J. reine angew. Math. 485 (1997), especially Theorem 1.11, Corollary 2.14 and Theorem 2.15.
- T. Yang, [Nonvanishing of central Hecke L-values and rank of certain elliptic curves](https://people.math.wisc.edu/~tonghaiyang/rank.pdf), Compositio Math. 117 (1999), Section 1 and Appendix.
- M. Bertolini, H. Darmon, K. Prasanna, [p-adic Rankin L-series and rational points on CM elliptic curves](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP2.pdf), Pacific J. Math. 260 (2012), exact period/twist formulas and the good-pair argument, with the arbitrary $p$-conductor point step supplied as in R748 by:
- Y. Liu, S. Zhang, W. Zhang, [A p-adic Waldspurger formula](https://web.math.princeton.edu/~shouwu/publications/pWalds.pdf), Duke Math. J. 167 (2018), Definition 3.3.1, Theorem 3.3.2 and Proposition 4.3.6.
