# R588 — Actual toric norms, CM periods, and the two normalized jets

> Recovery, 2026-11-14. The old full proof and its local-factor table were lost with the former environment. This is a new reconstruction from the actual vectors, with the primary Waldspurger formula reopened and the normalizations recomputed. It is not claimed to reproduce lost bytes. In particular the finite norm $N_\theta$ is defined explicitly below; no missing factor is chosen merely to fit an old final formula. All statements concern the actual R575 family and its transported marking.

## 1. The two formulas to be proved

Let $p\ge41$, $p\equiv5\pmod6$, $K=\mathbb Q(\zeta)$, and let $\theta=\theta_{-1}$ be the specified primitive norm-one character. Put

$$
E_0:y^2=x^3-1,\quad \omega=dx/(2y),\quad
\Lambda=\Omega\mathcal O_K,\quad \Omega>0,\quad
A=\frac{\sqrt3\,\Omega^2}{2\pi}.
\tag{588R.1}
$$

Use the two actual markings proved in R586. The higher rational kernel is computed separately in R595; its coefficient evaluation is not an input to the present norm identity. For $m=0$ take $\chi_m=\chi_0$ and the actual vector $F_0$; for $m=2$ take $\chi_m=\chi_6$ and the actual vector $F_1$. Explicitly, for the labeled mixed six-torsion point $Q_{\delta ij}$,

$$
\chi_0(Q_{\delta ij})=\delta\zeta^{-i-j},\qquad
\chi_6(Q_{\delta ij})=\delta\zeta^{j-i}.
\tag{588R.2}
$$

Let $T_r$ be the diagonal coefficient of the completed Kronecker theta function in the same normalization as $T_0=E_1^*$. Thus

$$
T_r(P)=\frac{e^*_{r,r+1}(P,0)}{r!A^r}.
\tag{588R.3}
$$

Write $H_r(P)=\sum_Q\chi_m(Q)^{-1}T_r(P+Q)$ and define the two actual finite sums, for each chosen $m$, by

$$
S_m=-\sum_{b\in(\mathcal O_K/p)^\times}\theta(b)H_m(\Omega b/p),
\quad
S_{m+1}=-\sum_{b\in(\mathcal O_K/p)^\times}\theta(b)^{-1}H_{m+1}(\Omega b/p).
\tag{588R.4}
$$

No change from $\chi_0$ to $\chi_6$ is made inside either pair. Let $M_m$ be the actual flat jet of that marking, with the absolute normalization of R592 and Section 7 below. We prove

$$
\boxed{
M_m\overline{M_m}
=\frac{[m!(m+1)!]^2N_\theta}{18(p+1)^2}
 S_mS_{m+1}\qquad(m=0,2).
}
\tag{588R.5}
$$

Here the bar is the actual algebraic complex-conjugation operation, subsequently transported to the fixed $p$-adic embedding. It is not assumed to preserve that embedding. The actual identities are

$$
\overline{M_0}=-M_0,\qquad
\overline{M_2}=-\zeta M_2,\qquad
N_\theta\equiv-1\pmod p.
\tag{588R.6}
$$

In particular the constants in the two norm formulas are $1/18$ and $8$, respectively. This supplies the precise norm input for R589 and R595. It does not assert that the finite products never vanish or that the relevant quotient has rank zero.

## 2. The finite norm, its precise denominator, and its residue

On the R434 finite type

$$
\Lambda=\mathcal O^{\mathbb F_p}/\mathcal O\mathbf1
$$

fix the positive Hermitian form

$$
G(e_r,e_s)=p\delta_{rs}-1.
\tag{588R.7}
$$

It is well defined on the quotient, positive definite there in each complex realization, and invariant under the finite representation. One can see its normalization without computing a large matrix: invariance under the affine Borel makes the diagonal entries equal and the off-diagonal entries equal, while $\sum_re_r=0$ forces their ratio. The invariant unitary form is unique up to scale, and (588R.7) fixes that scale. In particular $G(e_0,e_0)=p-1$.

Let $\mathsf T$ be the actual CM nonsplit torus, of order $p+1$, and retain the **average** used in R592:

$$
A_{\mathsf T}=\frac{\operatorname{Tr}_{\mathsf T}}{p+1},
\qquad u=A_{\mathsf T}e_0.
\tag{588R.8}
$$

Define the finite scalar in this reconstructed proof by

$$
\boxed{
N_\theta:=G(e_0,\operatorname{Tr}_{\mathsf T}e_0)
=(p+1)G(u,u).
}
\tag{588R.9}
$$

The second equality follows from self-adjointness and idempotence of the average. This specifies whether the norm belongs to the average or to the raw trace. Replacing the average vector by the raw trace would multiply each $M_m$ by $p+1$ and its squared norm by $(p+1)^2$; that replacement is not made here.

R434 proves that the whole finite group preserves $\Lambda$ and that the reduction functional $\ell([c_r])=\sum_rc_r$ is invariant, with $\ell(u)=1$. Modulo $p$, (588R.7) is $-\ell\otimes\overline\ell$. Therefore

$$
N_\theta=(p+1)G(u,u)\equiv-1\pmod p.
\tag{588R.10}
$$

This is an integral unit statement about the actual projected vector. No complex numerical norm is used to infer it. Transporting the full marking also transports the split vector and the torus simultaneously, preserving $G$ and (588R.9).

## 3. Hecke characters and the two exact finite L sums

Let $f_\theta=f_{\Psi_\theta}$ be the untwisted theta newform of level $9p^2$, where

$$
\Psi_\theta((a))=a\epsilon_3(a)\theta(a).
\tag{588R.11}
$$

The six-level marking, not an unverified relabeling of $f_\theta$, carries the actual cubic direction of R575. The two Hecke characters whose center values occur in the toric factorization are

$$
\begin{aligned}
\xi_{2m+1}((a))&=a^{2m+1}\chi_m(a)\theta(a)^{-1},\\
\xi_{2m+3}((a))&=a^{2m+3}\chi_m(a)\theta(a).
\end{aligned}
\tag{588R.12}
$$

The unit conditions can be checked on $-1$ and $\zeta$. For $m=0$, $\chi_0(\zeta)=\zeta$; for $m=2$, $\chi_6(\zeta)=1$; and $\theta(\zeta)=\zeta^{-1}$. Thus both definitions are independent of the chosen generator. On rational integers their finite factor is $\epsilon_3$, as required for the corresponding trivial-nebentypus CM forms.

The normalized Eisenstein–Kronecker sum is

$$
e^*_{r,r+1}(P,0)=\sum_{\lambda\in\Lambda}
 \frac{\overline{P+\lambda}^{r}}{(P+\lambda)^{r+1}},
\tag{588R.13}
$$

initially interpreted in its convergent auxiliary half-plane and then continued. Splitting the Hecke sum into residue classes modulo $6p$, using the six units, and replacing $a$ by $\bar a$ gives the exact general identity

$$
L(\xi_{2r+1},r+1)
=\frac{\Omega}{36p}\sum_{c\in(\mathcal O_K/6p)^\times}
 \eta(\bar c)e^*_{r,r+1}(\Omega c/(6p),0),
\tag{588R.14}
$$

where $\eta$ is the finite factor of $\xi$. This also follows from the completed two-variable theta expansion of Bannai–Kobayashi, [*Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers*](https://arxiv.org/pdf/math/0610163), Theorem 1.17, with $\Theta_{P,0}$ rather than $\Theta_{-P,0}$; the latter would reverse the odd total-degree sign.

For the CRT decomposition $c=6b+pa$, one has $c\bmod p=6b$ and $c\bmod6=pa$. Since $p\equiv-1\pmod6$ and $\chi_m(p)=-1$, the weight in (588R.14) is precisely $-\theta(b)\chi_m(a)^{-1}$ for the first character, and $-\theta(b)^{-1}\chi_m(a)^{-1}$ for the second. This is the minus sign already present in (588R.4). Consequently

$$
\begin{aligned}
L(\xi_{2m+1},m+1)&=\frac{\Omega\,m! A^m}{36p}S_m,\\
L(\xi_{2m+3},m+2)&=\frac{\Omega\,(m+1)! A^{m+1}}{36p}S_{m+1}.
\end{aligned}
\tag{588R.15}
$$

The product is

$$
L_{\rm prod}
=\frac{\Omega^2m!(m+1)!A^{2m+1}}{1296p^2}S_mS_{m+1}.
\tag{588R.16}
$$

This records the characters, CRT sign, both factorials, and the same period $\Omega$. In particular no fixed high-weight $C_p$ from the opposite family is substituted.

For clarity about the idelic convention in the next section, take the unitary toric character $\chi$ with archimedean part $(z/\bar z)^{m+1}$ and finite unit character $\chi_m\epsilon_3$. In Hsieh's convention the base-change factors are the unitary versions of $\overline{\xi_{2m+1}}$ and $\overline{\xi_{2m+3}}$. Conjugating ideals shows $L(\bar\xi,s)=L(\xi,s)$ here, so the central product is exactly (588R.16). At $p$, $\chi_p$ is trivial; at $2$ it is the indicated nontrivial cubic character; at $3$ it has conductor two and value $\chi_3(\zeta)=\zeta^{-1}$. This explicitly accounts for the conjugation rather than ignoring it.

## 4. Waldspurger formula and the Haar measures

The primary input is M.-L. Hsieh, *Special values of anticyclotomic Rankin–Selberg L-functions*, [author manuscript](https://www.math.ntu.edu.tw/~mlhsieh/research/VBDP.pdf), §1.1 and Proposition 2.1. We use that proposition itself, which is a characteristic-zero identity and does not require the ordinary hypotheses used later in that paper.

Use the standard additive character with real component $e^{2\pi i x}$ and its self-dual additive measures. The multiplicative measure is $d^\times x=\zeta_F(1)|x|^{-1}dx$ and $dt$ is the quotient measure on $K_v^\times/\mathbb Q_v^\times$. Thus:

* at an unramified inert finite prime, the torus has volume $1$;
* at $3$, the unit component has volume $1/\sqrt3$ and the entire ramified torus has volume $2/\sqrt3$;
* at infinity, $dt=(2/\pi)d\vartheta$ for $0\le\vartheta<\pi$, of volume $2$.

These are Hsieh's quotient measures. A separately rescaled Tamagawa measure must not be inserted without changing the factors below.

For the embedding $\iota$ from the actual CM basis, let $J^2=1$ and $J\iota(t)=\iota(\bar t)J$. The local Whittaker pairing is

$$
b_v(W_1,W_2)=\int_{\mathbb Q_v^\times}
 W_1(d(a))W_2(d(-a))\,d^\times a,
\tag{588R.17}
$$

and Hsieh's local factor is

$$
P_v(W_1,W_2,\chi)=
\frac{L(1,\eta_{K_v/\mathbb Q_v})}{\zeta_v(1)}
\int_{K_v^\times/\mathbb Q_v^\times}
 b_v(\pi(\iota(t))W_1,\pi(J)W_2)\chi(t)\,dt.
\tag{588R.18}
$$

Here $d(a)=\operatorname{diag}(a,1)$. To make the Hermitian use of the formula explicit, set $\delta=\operatorname{diag}(-1,1)$ and

$$
W_2(g)=\overline{W_1(\delta gJ)}.
\tag{588R.19}
$$

It is again a $\psi$-Whittaker function, and the integrand pairing in (588R.18) is exactly the usual Hermitian matrix coefficient of $W_1$. Globally this comes from $\varphi_2=\overline{\pi(J)\varphi_1}$. Since $J$ is rational and conjugates the torus to its conjugate, its global period is $\overline{P_\chi(\varphi_1)}$. Proposition 2.1 therefore gives the squared norm of the global period with the local Hermitian factors just specified. No unproved assertion about a $p$-adic conjugate place is involved.

At each of $2,3,p$ the base-change local $L$ factor is $1$: the indicated toric character is nontrivial on the inertia that would otherwise contribute. At every other finite place the normalized spherical factor is the local $L$ factor and cancels. The archimedean $L$ factor cancels against the denominator in the proposition. Only the four factors computed next remain.

## 5. The actual finite local vectors

### 5.1. Classical and finite-adelic degeneracy conventions

Use adelic right translation $\pi(g)\varphi(x)=\varphi(xg)$. Then the raw classical function $H_0=f_\theta(\tau/(6p))$ corresponds to the finite vector $\pi(d(6p))W_{\rm new}$, and its automorphic CM value has the factor $1/(6p)$. The inverse matrix $d((6p)^{-1})$ is the corresponding **classical archimedean** degeneracy matrix. Interchanging these descriptions in the finite stabilizer calculation would be wrong.

In particular, at $3$ the finite right-translate is $\pi(d(3))W_{\rm new}$. It conjugates $K_0(9)$ to the subgroup with both off-diagonal entries divisible by $3$, the inverse image of the split torus modulo $3$. It contains $K(3)$. This is the actual shifted newvector used below.

### 5.2. The prime p

The depth-zero newvector has Kirillov function $1_{\mathbb Z_p^\times}$ and norm one. Its finite $d(p)$ translate realizes $e_0$, whose finite-form norm is $p-1$ in (588R.7). Therefore the Whittaker norm of the actual average $u$ is

$$
\|u\|^2=\frac{G(u,u)}{p-1}
=\frac{N_\theta}{(p-1)(p+1)}.
\tag{588R.20}
$$

It is torus invariant and the torus has volume one. The prefactor in (588R.18) is $(p-1)/(p+1)$. Thus the complete local factor is

$$
\boxed{P_p=\frac{N_\theta}{(p+1)^2}.}
\tag{588R.21}
$$

This is the source of both factors $p+1$. One is not silently absorbed into the definition of $M_m$.

### 5.3. The prime 2

The spherical representation has Satake parameters $i,-i$, because $a_2=0$. Its normalized Kirillov norm is

$$
\|W_{\rm sph}\|^2=\sum_{r\ge0}|W(d(2^r))|^2
=\sum_{k\ge0}2^{-2k}=\frac43.
\tag{588R.22}
$$

Let $v_-$ and $v_+$ be the two neighboring $d(2)$ and $d(2^{-1})$ translates. The spherical distance-two coefficient is $-1/2$, so

$$
\langle v_-,v_-\rangle=\langle v_+,v_+\rangle=\frac43,
\qquad \langle v_-,v_+\rangle=-\frac23.
\tag{588R.23}
$$

The factor $4$ in the raw $H_2$ term exactly compensates its degeneracy factor. Hence the actual two tame vectors are $v_- -\zeta^2v_+$ and $-\zeta^2v_-+v_+$. Both have Whittaker norm $2$, and they are the two cubic torus eigenvectors in the standard plane. The toric character in Section 3 picks the appropriate one in each case. Since the torus volume is one and $L(1,\eta_2)/\zeta_2(1)=1/3$,

$$
\boxed{P_2=\frac23.}
\tag{588R.24}
$$

### 5.4. The prime 3, including the odd-valuation coset

The local inducing character has conductor one over the ramified quadratic extension, value $-1$ on $-1$, and is not conjugation invariant. Its induction is the depth-zero supercuspidal of conductor two. Its compact type is the two-dimensional cuspidal representation of $\mathrm{GL}_2(\mathbb F_3)$ with trivial central character. The compact-induction description used here is the depth-zero case of File–Martin–Pitale, *Test vectors and central L-values for GL(2)*, [published text](https://msp.org/ant/2017/11-2/ant-v11-n2-p01-p.pdf), §5B4 (the preprint's §5.2.4).

The actual vector from §5.1 is the split-torus fixed line in this type and has norm one. On the ramified-torus unit quotient $C_3$, the two characters $\zeta,\zeta^2$ are orthogonal. The split reflection exchanges them and fixes the source line, so each projection has squared norm $1/2$.

The compact-induction vector is supported on $ZK$. The matrix of a ramified uniformizer has odd determinant valuation, as does its entire unit coset, whereas every element of $ZK$ has even determinant valuation. Consequently its matrix coefficient is exactly zero on the odd-valuation coset. This is a support argument; that coset is not omitted because its numerical contribution looked small.

The unit coset has volume $1/\sqrt3$. Multiplying its projected norm $1/2$ by the local prefactor $2/3$ gives

$$
\boxed{P_3=\frac1{3\sqrt3}.}
\tag{588R.25}
$$

## 6. The archimedean factor and the global CM period

Let $\delta_k=(2\pi i)^{-1}\partial_\tau-k/(4\pi\operatorname{Im}\tau)$ and use its iterates with the increasing weights. Hsieh's normalized raising operator $\widetilde V_+^m=(-8\pi)^{-m}V_+^m$ has the actual classical value $y^{m+1}\delta_2^mF$. Proposition 3.3 of that paper gives, for weight two,

$$
\boxed{P_\infty=\frac{8\,m!(m+1)!}{(4\pi)^{2m+3}}.}
\tag{588R.26}
$$

This follows as well from the discrete-series norm recurrence and the real torus volume two. The factorials are not removed by interpreting the jet as a coefficient instead of a derivative.

Since $K$ has class number one, a fundamental domain for the global torus may be taken to have finite unit components and the real circle. At $3$ this selects the unit component of volume $1/\sqrt3$; its other valuation class is removed by the global principal element $\sqrt{-3}$. Dividing by $\mathcal O_K^\times/\mathbb Z^\times$, of order three, gives

$$
\operatorname{vol}(K^\times\backslash\mathbb A_K^\times/
\mathbb A_\mathbb Q^\times,dt)=\frac2{3\sqrt3}.
\tag{588R.27}
$$

At $2$ and $p$ the chosen vectors are already toric. At $3$, evaluation at the CM point annihilates the wrong $C_3$ character: the global CM unit, its $2$-component, and the raised infinite weight force the correct eigencharacter. Thus projecting the split-fixed $3$-vector does not change its actual CM evaluation, even though its local squared norm acquires the factor $1/2$ in §5.4. This is the distinction between the CM period and the local matrix-coefficient norm.

With $y=\sqrt3/2$, the complete global period is therefore

$$
P_\chi(\varphi_m)=\frac2{3\sqrt3}
 \frac{y^{m+1}}{6p}\,\delta_2^mF(\tau_{\rm CM}).
\tag{588R.28}
$$

The raw $F$ in this equation includes the average (588R.8) and the actual tame combination. There is no further average by $p+1$ or further degeneracy factor. Combining Proposition 2.1 with (588R.21), (588R.24), (588R.25), and (588R.26) gives

$$
|P_\chi(\varphi_m)|^2
=L_{\rm prod}\,
\frac{16\,m!(m+1)!N_\theta}
 {9\sqrt3\,(p+1)^2(4\pi)^{2m+3}}.
\tag{588R.29}
$$

## 7. The flat Hodge jet and cancellation of every period factor

The relation between the flat jet and the Maass derivative can be checked directly in the same elliptic family used in R592. At the CM point the two period columns of $(\omega,\eta=x\omega)$ are

$$
\binom{\Omega}{-\Omega/A},\qquad
\binom{\Omega\tau_{\rm CM}}{-\Omega\overline{\tau_{\rm CM}}/A}.
\tag{588R.30}
$$

The sign in the second row is the integral of $\wp\,dz$, namely minus the quasi-period. If the Gauss–Manin fundamental matrix has top row $(u_1,u_2)$ and $z=u_2/u_1$, then the period ratio and the flat value are

$$
\tau(z)=\frac{\tau_{\rm CM}-\overline{\tau_{\rm CM}}z/A}{1-z/A},
\qquad
\mathcal F_{\rm flat}(z)=
\left(\frac{2\pi i}{\Omega}\right)^2
(1-z/A)^{-2}F(\tau(z)).
\tag{588R.31}
$$

Here $\tau'(0)=2\pi i/\Omega^2$. Differentiating (588R.31), or inducting with the displayed fractional-linear change of variable, proves

$$
\boxed{M_m=\left(\frac{2\pi i}{\Omega}\right)^{2m+2}
 \delta_2^mF(\tau_{\rm CM}).}
\tag{588R.32}
$$

It is the same absolute Hodge normalization as the Tate differential $dX/X=2\pi i\,dz_{\rm an}$. Thus it also agrees with R592's $z'(0)=-1/6$ normalization of $E_t$, without an unidentified Manin or period scalar.

Taking squared absolute values in (588R.28), using $A=\Omega^2y/\pi$, gives

$$
|P_\chi(\varphi_m)|^2
=\frac{A^{2m+2}}{243p^2(4\pi)^{2m+2}}
 M_m\overline{M_m}.
\tag{588R.33}
$$

Substitute the exact finite $L$ product (588R.16) into (588R.29), then divide by (588R.33). The rational constant is

$$
\frac{243\cdot16}{9\cdot4\cdot1296}
\frac{\Omega^2}{\sqrt3\,\pi A}
=\frac1{12}\cdot\frac23=\frac1{18}.
\tag{588R.34}
$$

All powers of $p$, $\Omega$, $A$, and $\pi$ cancel exactly. The two remaining factorials occur twice. This proves (588R.5) directly from the actual vectors and measures.

## 8. The actual anti-linear identification

The last step cannot be replaced by saying that complex conjugation fixes the chosen $p$-adic place. We instead prove an identity of the algebraic CM values before applying that place.

Choose an integer $L$ divisible by $p$ and congruent to $1$ modulo $12$, and use the period basis

$$
\tau_*=\frac{-L+\sqrt{-3}}2.
\tag{588R.35}
$$

It differs from $\zeta$ by a multiple of six, so the tame marking is unchanged. Transport the split vector, full $p$-level basis, and CM torus together under this change; the norm (588R.9) is unchanged. The reduced CM torus has trace zero. Its reflection is the affine involution, and the plus-type torus invariant line is fixed by that reflection.

The finite matrices are real: in the Weyl sum of R434, complex conjugation replaces $\theta$ by $\theta^{-1}$, and $a\mapsto a^p$ preserves each norm/trace fiber and interchanges these characters. The affine generators are real as well. The transported averaged vector is therefore real and reflection invariant. The underlying theta newform has real Fourier coefficients, by pairing conjugate ideals. It follows that the same projected $H_0,H_2$ satisfy the expected conjugation relation with $\tau\mapsto-\bar\tau$.

At (588R.35), $-\overline{\tau_*}=\tau_*+L$. The $p$-translation is trivial because $p\mid L$, while the tame translation is exactly $T$ in (586R.3). For a tame coefficient vector $v$, the actual antilinear action is therefore

$$
v\longmapsto T\overline v.
\tag{588R.36}
$$

Writing $v_0=(-\zeta^2,4)^T$ and $v_1=(1,-4\zeta^2)^T$, direct multiplication gives

$$
T\overline v_0=-v_0,\qquad
T\overline v_1=-\zeta v_1.
\tag{588R.37}
$$

The normalized Maass operator commutes with this Fourier conjugation, and the even period powers in (588R.32) are real. For the actual allowed jets $m=0,2$, (588R.37) proves the first two identities in (588R.6). This calculation retains the transported full-level marking and the positive CM embedding; a single untransported complex $q$ expansion would not have sufficed.

Now apply the fixed embedding into $\overline{\mathbb Q}_p$ to these algebraic identities. Since $-1$ and $-\zeta$ are units, $v_p(M_m\overline{M_m})=2v_p(M_m)$ follows from (588R.6) itself. It does not require that conjugation stabilize the chosen place.

## 9. Explicit downstream identities and scope

For the actual two markings, (588R.5) becomes

$$
M_0\overline{M_0}=\frac{N_\theta}{18(p+1)^2}S_0S_1,
\qquad
M_2\overline{M_2}=\frac{8N_\theta}{(p+1)^2}S_2S_3.
\tag{588R.38}
$$

Together with (588R.6), these give exactly the norm interfaces used in the restored R589 and R595, including their half-integral safe bounds when a residue vanishes. The proof never substitutes the fixed opposite-family $C_p$, never treats an unproved candidate transport as an automorphism of the coarse curve, and never concludes a global zero image from a local period.

The local norm normalization (588R.9) is newly made explicit in this recovery because the original definition was not recoverable from the published repository. It was derived from the actual average and its Whittaker realization, rather than inferred from the old final denominator. The old statements are compatible with this precise normalization; no claim is made that the old lost symbol had an independently verified identical definition.
