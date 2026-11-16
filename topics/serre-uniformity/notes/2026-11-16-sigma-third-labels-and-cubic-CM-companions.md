# 三分位置原标签的四条三次 CM companion 同余

日期：2026-11-16。会话：serre-public-astra-20261115 / sigma_uniform。

**状态：本文的原角色识别、四条模 $p$ theta 级数同余、完整导子和 Gauss 因子已证明。尚未得到原 central 值、Cartier 系数或同标签三单位的整比较。**

本篇接 [两个交换标签](2026-11-16-sigma-two-swapped-primitive-labels-at-thirds.md)，保留 [R717](../results/R717-exact-original-CM-norm-from-certified-complex-traces.md) 的全部六层相位与所选 $p$ 进嵌入。这里出现的三次扭仍有真实 $p$ 导子；不是 R830 已排除的固定 tame 替代。

## 1. 同一两个本原标签与原角色

设
$$
p\ge41,\quad p\equiv2,5\pmod9,\quad n=p+1,
\qquad
e=\begin{cases}1,&p\equiv2\pmod9,\\2,&p\equiv5\pmod9.\end{cases}
$$
仍取 $K=\mathbf Q(\zeta)$、$s=\sqrt{-3}=1+2\zeta$、原
$$
\theta(\gamma)=\operatorname{Teich}(\gamma/\bar\gamma),
\qquad \chi=\theta^{n/3}.
\tag{TC1}
$$
所以 $\chi$ 的精确阶为三，并且 $en/3\equiv1\pmod3$。定义
$$
h_+=en/3+3,\qquad h_-=(3-e)n/3-1.
\tag{TC2}
$$
它们恰是前篇的两个标签：

| $p$ | $h_-$ | $h_+$ |
|---|---|---|
| $18k+5$ | $6k+1$ | $12k+7$ |
| $18k+11$ | $12k+7$ | $6k+7$ |

两者均与完整的 $n$ 互素，且 $h_-+h_+=p+3$。前篇已证明其两个原 Legendre 值不同时为零。

R717(717.7)--(717.9) 的六层字符与原 Hecke 角色是
$$
\chi_6(\delta\zeta^i\bmod3,\zeta^j\bmod2)
 =\delta\zeta^{j-i},
$$
$$
\xi_{5,h}((\gamma))=\gamma^5\chi_6(\gamma)\theta(\gamma)^{-h},
\qquad
\xi_{7,h}((\gamma))=\gamma^7\chi_6(\gamma)\theta(\gamma)^h.
\tag{TC3}
$$
In particular, $\chi_6(u)=u^3$ for $u\in\mu_6$, while
$\chi(\zeta)^e=\zeta^{-1}$ and $\chi(-1)=1$.
Thus the following two characters really descend to ideals:
$$
\psi_+((\gamma))=\gamma\chi_6(\gamma)^{-1}\chi(\gamma)^e,
\qquad
\psi_-((\gamma))=\gamma\chi_6(\gamma)\chi(\gamma)^e.
\tag{TC4}
$$
For example both expressions are unchanged by replacing $\gamma$ by $-\gamma$ or $\zeta\gamma$; these generate all units. The finite characters in (TC4) are primitive modulo $6p$: the factors at $2,3$ are the original primitive $\chi_6^{\pm1}$, and the factor at $p$ has exact order three. For the local factor at $3$, choose by CRT a residue equal to $\zeta\bmod3$ and to $1\bmod2p$. Then $\chi_6=\zeta^{-1}$ and $\chi^e=1$, so both finite characters remain nontrivial on the kernel of reduction from $(\mathcal O_K/(3))^\times$ to $(\mathcal O_K/(s))^\times$. Thus the exponent at $s$ is exactly two. At $2$ the cubic factor is nontrivial on $\mathbf F_4^\times$, and at $p$ it has order three; CRT prevents cancellation between these three factors. Their Hecke conductors are therefore $(6p)$, and their induced weight-two theta forms have level
$$
|D_K|\operatorname N(6p)=108p^2.
\tag{TC5}
$$
The powers $\psi_+^5,\psi_-^7,\psi_-^{13}$ retain the same conductor: the exponents are prime to three, and their odd powers retain the nontrivial sign and cubic tame characters. No factor at $p$ has been removed.

## 2. Which actual cubic twists occur

For an ideal prime to $6p$, choose its unique generator $\gamma\equiv1\pmod3$. Then
$$
\chi_6(\gamma)=\left(\frac{\gamma}{2}\right)_3
 =\left(\frac2\gamma\right)_3,
\qquad
\chi(\gamma)=\left(\frac{\gamma}{p}\right)_3^{-1}
 =\left(\frac p\gamma\right)_3^{-1}.
\tag{TC6}
$$
The first equality uses the exact original $\chi_6$ at the primary generator: its value is $\zeta^j$ when $\gamma\equiv\zeta^j\pmod2$. The second line follows from
$$
\theta(\gamma)^{n/3}\bmod p
 =\gamma^{-(p^2-1)/3}.
$$
Both sides are third roots of unity, whose reductions at $p\ne3$ are distinct, so the equality of roots of unity is exact. Cubic reciprocity gives the remaining equalities in (TC6); multiplying a primary generator by $-1$ does not change a cubic residue symbol.

Let $C_D$ denote the elliptic curve $u^3+v^3=D$. In the standard positive CM embedding its Hecke character is
$$
\psi_{C_D}((\gamma))
 =\gamma\,\overline{\left(\frac D\gamma\right)_3}
\quad(\gamma\equiv1\pmod3).
\tag{TC7}
$$
This is Kezuka--Li (2.1), and also Rosu §2.1--2.2. The conjugation on the cubic symbol in (TC7) is essential; it is visible in the original PDFs, though plain-text extraction can omit the bar.

Substitution of (TC6) now gives the exact original identification
$$
\boxed{\psi_+=\psi_{C_{2p^e}},\qquad
       \psi_-=\psi_{C_{4p^e}}.}
\tag{TC8}
$$
For the second formula, $(4/\gamma)_3^{-1}=(2/\gamma)_3$, which fixes the direction at $2$.

The direction agrees with the actual positive/inverse tame distinction retained after R575. More specifically, the established results of Kezuka--Li, Theorem 1.1 and Corollary 1.2, give
$$
\begin{array}{c|cc}
 &\psi_+&\psi_-\\\hline
p\equiv2\pmod9&C_{2p}\text{ has analytic rank }1
 &L(C_{4p},1)\ne0\\
p\equiv5\pmod9&C_{2p^2}\text{ has analytic rank }1
 &L(C_{4p^2},1)\ne0.
\end{array}
\tag{TC9}
$$
This does not identify these small cubic factors with the original primitive Jacobian quotient. In particular $\chi^e(s)=1$, whereas the original primitive $\theta^{h_\pm}(s)=-1$. The replacement is a residual companion comparison, not an equality of those original characteristic-zero representations. The rank statements in (TC9) also say nothing by themselves about the central values of the fifth, seventh or thirteenth powers.

## 3. Four exact residual ideal-character identities

Use the chosen prime above $p$ and reduce integral character values there. If $\mathfrak a=(\gamma)$ is prime to $6p$, put $q_{\mathfrak a}=\operatorname N\mathfrak a=\gamma\bar\gamma$. It is a $p$ unit. Equations (TC1)--(TC3) give
$$
\theta^{h_-}=\chi^{-e}\theta^{-1},\qquad
\theta^{h_+}=\chi^e\theta^3.
\tag{TC10}
$$
Since $\theta(\gamma)\equiv\gamma/\bar\gamma\pmod p$, the four comparisons are
$$
\boxed{\begin{aligned}
\xi_{5,h_-}(\mathfrak a)&\equiv
 q_{\mathfrak a}^{-1}\psi_-^7(\mathfrak a),\\
\xi_{7,h_-}(\mathfrak a)&\equiv
 q_{\mathfrak a}\psi_+^5(\mathfrak a),\\
\xi_{5,h_+}(\mathfrak a)&\equiv
 q_{\mathfrak a}^{2}\overline{\psi_+(\mathfrak a)},\\
\xi_{7,h_+}(\mathfrak a)&\equiv
 q_{\mathfrak a}^{-3}\psi_-^{13}(\mathfrak a)
\pmod p.
\end{aligned}}
\tag{TC11}
$$
Here the bar on $\psi_+$ is complex conjugation of the character value, before reduction. It is not notation for reduction. To verify every exponent, the respective algebraic parts after replacing $\theta$ are
$$
\gamma^6\bar\gamma^{-1}
 =q_{\mathfrak a}^{-1}\gamma^7,\quad
\gamma^6\bar\gamma=q_{\mathfrak a}\gamma^5,\quad
\gamma^2\bar\gamma^3=q_{\mathfrak a}^2\bar\gamma,\quad
\gamma^{10}\bar\gamma^{-3}=q_{\mathfrak a}^{-3}\gamma^{13}.
$$
Their finite factors are respectively
$\chi_6\chi^e,\chi_6\chi^{-e},\chi_6\chi^{-e},\chi_6\chi^e$.
Using $\chi_6^6=1$ and $\chi^3=1$ verifies all four powers in (TC11), including the inverse on $\chi_6$ in $\psi_+$.

## 4. The actual theta-series companions

For an ideal character $\eta$ above, write
$$
\mathcal T_\eta(q)
 =\sum_{(\mathfrak a,6p)=1}\eta(\mathfrak a)q^{\operatorname N\mathfrak a},
\qquad \Theta_q=q\frac{d}{dq}.
$$
Let $\mathcal F_{5,h}=\mathcal T_{\xi_{5,h}}$ and $\mathcal F_{7,h}=\mathcal T_{\xi_{7,h}}$. Their weights are six and eight. The other four theta series have weights eight, six, two and fourteen, in the order in (TC11). The antiholomorphic infinity type $(0,1)$ in $\overline{\psi_+}$ still defines a holomorphic theta series: conjugating the ideal index identifies its series with $\mathcal T_{\psi_+}$.

All coefficients are algebraic integers. Because $p$ is inert, an ideal whose norm is divisible by $p$ is itself divisible by $(p)$ and has been excluded. Thus these series already have zero coefficients at all indices divisible by $p$, and no unrecorded Euler term enters when applying $\Theta_q$.

Summing (TC11) coefficient by coefficient proves
$$
\boxed{\begin{aligned}
\Theta_q\mathcal F_{5,h_-}&\equiv\mathcal T_{\psi_-^7},\\
\mathcal F_{7,h_-}&\equiv\Theta_q\mathcal T_{\psi_+^5},\\
\mathcal F_{5,h_+}&\equiv\Theta_q^2\mathcal T_{\overline{\psi_+}},\\
\Theta_q^3\mathcal F_{7,h_+}&\equiv\mathcal T_{\psi_-^{13}}
\pmod p.
\end{aligned}}
\tag{TC12}
$$
These are four identities of the actual integral $q$ expansions, all at full level $108p^2$. The companion series have rational integer coefficients: conjugate ideals pair their $K$-valued algebraic integers into rational integers. No sum over different original $h$ has been taken.

The equations are stated as $q$-expansion identities. They do not assert a supersingular evaluation after division by a Hasse invariant on a model with bad $p$ level. Such a comparison needs an actual integral model and the corresponding period map. In particular one cannot replace the original first-$p$ sigma coefficient simply by the complex central value of the weight-two companion, which vanishes by (TC9).

## 5. The Gauss factor in the original additive convention

Retain R717(717.20), namely if $\gamma=A+B\zeta$ then
$$
\mathbf e_M(\gamma)=\exp(2\pi iB/M).
$$
For every nontrivial character $\nu$ of $\mathbf F_{p^2}^\times$ trivial on $\mathbf F_p^\times$, the original local Gauss sum is
$$
\sum_{x\in\mathbf F_{p^2}^\times}\nu(x)\mathbf e_p(x)=p.
\tag{TC13}
$$
Indeed $B(x)=\operatorname{Tr}(x/s)$. In the trace convention, the trace-zero line contributes $p\nu(s)$ after summing the other lines. Changing to $\operatorname{Tr}(x/s)$ multiplies by $\nu(s)$, and $\nu(s)^2=\nu(-3)=1$. This proves (TC13) without dropping a phase. It applies both to the original $\theta^{\pm h_\pm}$ and to the new $\chi^{\pm e}$.

The original tame sum is $\tau_6(\chi_6)=-6$. Also $\chi_6(p)=-1$ and $\chi^{\pm e}(6)=1$, so CRT gives
$$
\tau_{6p}(\chi_6\chi^{\pm e})
 =-\tau_6(\chi_6)\tau_p(\chi^{\pm e})=6p.
\tag{TC14}
$$
All four comparison characters in (TC11) have precisely these finite factors. Thus their full Gauss factor remains $6p$, as in R717. It has valuation one and must not be replaced by a unit. For comparison, the weight-two $\psi_+$ itself has tame $\chi_6^{-1}$, with $\tau_6(\chi_6^{-1})=6$ and full Gauss sum $-6p$; taking its conjugate value in (TC11) restores the displayed $\chi_6$ direction.

## 6. The period scale that remains in the comparison

Write $\alpha^3=4$, $\beta^2=3$, with the original positive complex choices, and let $\Omega$ be the real period of
$E_0:y^2=x^3-1$ for $dz=dx/(2y)$. Kezuka--Li (1.2) use the period of $Y^2=4X^3-1$ for $dX/Y$, which is $2\Omega/\alpha$. Hence their actual Néron period of $C_D$ is
$$
\boxed{\Omega_D=\frac{2\Omega}{\alpha\beta D^{1/3}}.}
\tag{TC15}
$$
This also follows by first scaling the classical model $Y^2=X^3-432D^2$ by $u=\alpha\beta D^{1/3}$, and then retaining the factor two between its displayed differential and the Néron normalization in (1.2).

For $D=2p^e$ or $4p^e$, the algebraic differential-comparison factor $2/(\alpha\beta D^{1/3})$ has $p$ valuation $-e/3$ after choosing a cube root of $p$. This is a statement about that algebraic factor, not a valuation assigned to the complex number $\Omega$. Its odd tensor powers, the norm shifts in (TC11), and the nonunit factor $p$ in (TC14) must all remain in any comparison with R727's normalized Fourier tails.

Consequently (TC12) is a concrete same-label companion bridge, but it does not yet identify the integral functional that extracts
$$
P_{h-1}(1/s)f_i g_{N-1-i}.
$$
No primitive indicator or Legendre value has disappeared. A proof that the relevant integral central-value or Cartier functional respects (TC12), with the factors (TC14)--(TC15), is still needed before any unit assertion. The two-label theorem remains a sufficient window, not a replacement for the full original target.

## Primary sources checked

- R717 (717.7)--(717.9), §4: exact original six-level character, Teichmüller direction, additive character and $6p$ Gauss sum.
- [E. Rosu, *Central values of L-functions of cubic twists*](https://arxiv.org/abs/1711.03200), v2 PDF pp. 4--5, §2.1--2.2 and Theorem 2.1: primary generators, the conjugated cubic symbol, and cubic reciprocity. The displayed conjugation was checked in the PDF image.
- [Y. Kezuka and Y. Li, *A Classical Family of Elliptic Curves having Rank One and the 2-Primary Part of their Tate--Shafarevich Group Non-Trivial*](https://archive.ymsc.tsinghua.edu.cn/pacm_download/615/12104-liyx3.pdf), Documenta Math. 25 (2020), 2115--2147: Theorem 1.1, Corollary 1.2, (1.2), and (2.1). Its local valuation statements used there are at $3$; this note does not misread them as a $p$-unit theorem.

No new numerical computation or prime window is used in this proof.
