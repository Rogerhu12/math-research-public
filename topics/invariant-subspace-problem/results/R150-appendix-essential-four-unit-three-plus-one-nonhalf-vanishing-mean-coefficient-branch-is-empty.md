# R150 附录：单位 3+1 非半权支路的一阶 mean 系数零情形为空

作者：Astra-ISP-b2a9acde-20261120（root 与 r150_structure）；AI-assisted GPT-6 Astra Pro。日期：2026-11-20 UTC。状态：本条明确范围已证明。

## 1. 本结论的精确位置

沿用[外均值 essential-four 原长度五支撑约化](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md)及单位 $3+1$ 记号。
[完整 $p=0$ 支](R150-appendix-essential-four-unit-three-plus-one-isolated-zero-zero-base-pairing-branch-is-empty.md)已全排，[完整半权 $a=b=1/2$ 支](R150-appendix-essential-four-unit-three-plus-one-half-isolated-zero-branch-is-empty.md)也已全排。
本附录在真正剩余范围
$$
 p\ne0,\qquad a+b=1,\qquad b\ne0,1/2
$$
内，排除一个完整的系数零支路。

把全部 Gram 配对同时除以 $p$，令 $p=1$，仍使用原物理 jets：
$$
 \tau(x)=a x_0+x_2+b x_3,\qquad
 K_B=\begin{pmatrix}
 0&0&A&1\\
 0&-2A&B&q\\
 A&B&C&r\\
 1&q&r&0
 \end{pmatrix}.
$$
原源始终是
$$
 P(x)=\tfrac12\tau(x-\tau(x)1)^3,\quad T_3=P+R^3,\quad
 d=D_K1,\quad \phi=\tau d/2,
$$
$$
 e-2D_Kd-2d^2+4\phi d=0,\qquad
 N=N_B+mR^2,
$$
$$
 N_B(x)=\tfrac12\tau((d-\phi)x^2)
 -(\tau x)\tau(dx)+\phi(\tau x)^2+\tfrac14\tau(xD_Kx).
                                                               \tag{1.1}
$$
三重点各阶的 $e,D_K$ 定义与前两个单位 $3+1$ 附录完全相同。

置
$$
 x=A+b,\quad \delta=1-2b,\quad
 \kappa=2(\phi-x)/b.
$$
因 $b\ne0$，此定义合法，且原 mean 的常数项等价于
$$
 A=x-b,\quad r=x(1+\kappa)-\delta/2,\quad
 C=b\{\delta+\kappa(1-2x)\}.                               \tag{1.2}
$$
即使 $x=0$ 也没有除法。定义
$$
 \alpha=x+b(\kappa-2)=2\phi-A-3b,\qquad
 \beta_0=1/2-\kappa x.
$$
原一次 mean 为
$$
                  2\{\alpha(B+bq)+b\beta_0q\}=0.          \tag{1.3}
$$
本附录证明
$$
                            \alpha=0                     \tag{1.4}
$$
不可能。恢复未归一的 $p$ 后，这是 $2\phi-A-3bp=0$。

在三重点写原 $P,N_B$ 的前三个局部系数为
$p_0,p_1,p_2,n_0,n_1,n_2$。
前一附录已直接从原 highest、$N$ 证明两个不含除法的相容式
$$
 c_0=3p_0n_1-2n_0p_1=0,\qquad
 c_1=6p_0n_2+p_1n_1-4n_0p_2=0.                             \tag{1.5}
$$
此处继续保留所有 $p_0,n_0,m$ 为零的候选。

## 2. $\alpha=0,\ q\ne0$

由 (1.3)、$bq\ne0$，有 $\beta_0=0$。于是
$$
 x\ne0,\qquad
 \kappa=\frac1{2x},\qquad b=\frac{2x^2}{4x-1}.               \tag{2.1}
$$
$4x-1=0$ 不可能满足原 $\alpha=0$；
而 $x=1/2$ 恰给 $b=1/2$，已不在本附录的剩余范围。
故 $x(2x-1)(4x-1)\ne0$。

从同一原 jets 得到 $c_0$ 对 $B,q$ 的线性式
$$
 c_0=\ell_B B+\ell_qq,
$$
$$
 \ell_B=\frac{6x^4(2x-1)^3(4x+1)}{(4x-1)^3},\qquad
 \ell_q=\frac{6x^5(2x-1)^4(4x-3)}{(4x-1)^4}.                 \tag{2.2}
$$
若 $4x+1=0$，则 $\ell_B=0,\ell_q\ne0$，与 $q\ne0,c_0=0$ 矛盾。
所以也有 $4x+1\ne0$，并且
$$
 z:=B/q=-\frac{x(2x-1)(4x-3)}{(4x-1)(4x+1)}.              \tag{2.3}
$$

剩余两个原 mean 写成
$$
 E_2=R_2+L_2q^2=0,\qquad E_P=R_P+L_Pq^2=0,
$$
其中直接从原源
$$
 R_2=\frac{6x^2(1-2x)}{(4x-1)^2},\quad
 R_P=\frac{1-2x}{4x-1},\quad
 L_P=\frac{1-2x}{4x+1},
$$
$$
 L_2=-4z^2-6bz+b(1-2b).
$$
无需除以任何 $L_P,L_2$ 或 $q^2$，消去得到
$$
 R_2L_P-R_PL_2
   =\frac{32x^2(2x-1)^3}{(16x^2-1)^2}\ne0.                \tag{2.4}
$$
与两个 mean 同时为零矛盾。至此 $q\ne0$ 支已完整关闭。

## 3. $\alpha=0,\ q=0$ 的完整一参数二次关系

因 $b\ne0$，令
$$
 v=x/b,\qquad \kappa=2-v.
$$
原单点 mean 变成
$$
  -\tfrac12-2b^2v(v-2)^3=0.
$$
因此
$$
 v(v-2)\ne0,\qquad b^2=H(v):=-\frac1{4v(v-2)^3}.            \tag{3.1}
$$
原另一 mean 是 $R_2-4B^2=0$，在 (3.1) 上恰为
$$
 R_2=\frac{2bv-1}{v(v-2)},\qquad B^2=R_2/4.                 \tag{3.2}
$$

在 $q=0$ 上 $c_0=\ell_B B$。把 (3.1) 代入同一原源，
$$
 \ell_B=\frac{3\{F_2(v)+2bG_3(v)\}}{16v(v-2)^6},             \tag{3.3}
$$
其中
$$
 F_2=v^2-8v+8,\qquad G_3=5v^3-18v^2+28v-16.
$$
将 $c_0=0$ 乘以 $B$，再用 (3.2)，必有
$$
                         R_2\ell_B=0.                        \tag{3.4}
$$
没有为了这一步排除 $B=0$。

将 $q=0$、(3.1)、(3.2) 代入原第二相容式，精确整理为
$$
 c_1=\frac{3\{F_6(v)+2bv(v-2)G_6(v)\}}
              {64v^2(v-2)^9},                             \tag{3.5}
$$
$$
 F_6=4v^6-61v^5+293v^4-638v^3+796v^2-656v+288,
$$
$$
 G_6=-10v^6+73v^5-127v^4-218v^3+1012v^2-1280v+576.
$$
所有分母只含 (3.1) 已排除的 $v=0,2$。

## 4. 两个明确范数障碍只剩半权

只使用恒等式
$$
 (A+bC)(A-bC)=A^2-H(v)C^2
$$
即可从 (3.4)、(3.5) 得到两个必要一元方程。
不要求二次关系在任何函数域中不可约，也不从范数为零反推原式为零。

清除已经非零的分母，必要条件是
$$
 N_1(v)=\{(v-2)^3+v\}
        \{v(v-2)^3F_2(v)^2+G_3(v)^2\}=0,                  \tag{4.1}
$$
$$
 N_2(v)=(v-2)F_6(v)^2+vG_6(v)^2=0.                        \tag{4.2}
$$
这两个明确的 QQ 一元多项式的 monic gcd 为
$$
                           (v-1)^2.                       \tag{4.3}
$$
因此 $v=1$。此时回到原源，而不只停在范数条件：
$$
 R_2=1-2b,\qquad \ell_B=3(1-2b)/16.
$$
由 (3.4)，$3(1-2b)^2/16=0$，迫 $b=1/2$。
这与本附录已经限定的 $b\ne1/2$ 矛盾，故 $q=0$ 支也全部关闭。

## 5. 复核、结论与真实剩余

配套[短 QQ 原源](../notes/2026-11-20-essential-four-unit-three-plus-one-alpha-zero-verify.py)从 (1.1) 重建 mean、三阶以内的原 jets 和两个相容式，
再核 (2.1)–(3.5)，最后在 $\mathbb Q[v]$ 直接求 (4.1)、(4.2) 的 gcd。
它不使用一般多元 Gröbner、有限域提升或未给原出处的消元表。

实际run44733413376/job136278648778、冻结提交f0650d3aaeea0e353ace9ac547d21f80bc87a765，全部检查通过，程序计时1.480秒；源码SHA256为d723067071adab3df7e3871185e6654840ec8a60880d4af90139cea36de46254。[运行身份](../notes/2026-11-20-exact-source-run44733413376-b2a9.json)保完整日志/输出SHA和12:09:30 UTC实际pull回执；不保存可重算数组。

所以在单位 $3+1$ 加孤立零点的真正剩余支路
$p\ne0,\ b\ne1/2$ 中，必须
$$
                         2\phi-A-3bp\ne0.
$$
这是一个完整系数零支路的排除；未声称关闭该系数非零的全部一般权情形，
也不影响其他未闭支路或普通 Hilbert ISP 主问题的状态。
