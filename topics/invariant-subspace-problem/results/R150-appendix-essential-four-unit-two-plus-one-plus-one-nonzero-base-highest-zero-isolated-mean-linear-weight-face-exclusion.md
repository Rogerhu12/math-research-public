# R150 附录：单位 2+1+1 非零最高基值、零孤立点均值图的线性权重行列式面为空

作者：Astra-ISP-347c-20261126 / unit31_general；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条精确范围已证明。** 保持原单位 $2+1+1$ 加孤立零点的同一 Frobenius 乘法、原物理配对、mean、最高式及第二梯度的全部值和一阶 jet。在非零、不同、非相反的两个基点配对，非零基点 mean，$P_0\ne0$ 且孤立零点均值 $m=0$ 的范围，本条完整排除新的权重面
$$
J=\ell Q(2u-1)-u(2u+Q-2)=0.
$$
它在原 $N_1$ 的两张一次图上均为空。它不宣称两图的剩余高次行列式面已空。

## 1. 原式、坐标和已付边界

沿用[两个奇异 jet 面专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-base-highest-zero-isolated-mean-singular-faces-exclusion.md)的共同齐次坐标。原 Gram 的全部配对与孤立零点配对列共同归一，使
$$
p=1-\kappa,\qquad q=1+\kappa,\qquad Q=pq=1-\kappa^2,
\qquad Q(Q-1)\ne0.
$$
在形式二次代数 $\kappa^2=1-Q$ 中同时保留两个根。没有独立改变一个配对或替换原六维二次型。令
$$
\ell=b+c,\quad u=bp+cq,\quad a=1-\ell,
\quad b=\frac{\ell q-u}{2\kappa},\quad c=\frac{u-\ell p}{2\kappa},
$$
$$
D=\ell^2Q-2\ell u+u^2,\qquad bc=\frac{D}{4(Q-1)}\ne0,
$$
$$
H=2P_0=\ell Q(3u-2)+2u^3-6u^2+(4-Q)u\ne0.                 \tag{1.1}
$$
这里 $u\ne0$ 已由[完整零基点 mean 专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)支付；相等、相反和含零的基点配对各自引用原完整分支证明，不由本条重新计算。

原活跃 Gram 为
$$
K_B=\begin{pmatrix}0&0&p&q\\0&A_1&r&s\\p&r&0&t\\q&s&t&0\end{pmatrix},
\qquad
\tau(X)=aX_0+X_1+bX_B+cX_C.
$$
记 $d=D_K1$，$f=\tau(d)/2$，$g=bc\,t$，$x=d_B$，$y=d_C$，$V=2u-\ell Q$。同一原 $E_0=N_0=0$ 精确给出
$$
W_1=V/2-u^2+2fu,\qquad
W_2=uV-2u^3+f(V+2u^2)-Qg,
$$
$$
x=\frac{qW_1-W_2}{bp(q-p)},\qquad
y=\frac{W_2-pW_1}{cq(q-p)},
$$
$$
t=g/(bc),\quad r=x-ap-ct,\quad s=y-aq-bt,
\quad A_1=2f-2bx-2cy+2g.                                    \tag{1.2}
$$
这些分母全由 $bcQ(Q-1)\ne0$ 支付。$P_0=-u_0^3\ne0$ 与原 $N_0=-mu_0^2$ 使本图的 $N_0=0$ 等价于 $m=0$；原第二梯度还必须满足 $N_1=N_B=N_C=0$。

## 2. 两张原 jet 图及原 mean 行列式

定义
$$
\alpha=Q(\ell-1)-2u(u-1),\qquad
\beta=\ell^2Q^2+2Qu^2(1-\ell)+4u^2(u-1),
$$
$$
C_1=\ell(1-\ell)Q^2+4u^2(u-1)^2+2u(u-1)Q,
$$
$$
C_2=\ell Q^2\bigl(2\ell(u-1)-u\bigr)
 +4\ell u(u-1)(u-2)Q-2u^2(u-1)(4u-4+Q).
$$
原 $N_1$ 的化简分子除非零有理常数外恰为
$$
F_1F_2,
\qquad F_1=2fu\alpha+2gQ(u-1)+C_1,
\qquad F_2=2f\beta-2g\ell Q^2+C_2.                           \tag{2.1}
$$
[奇异面专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-base-highest-zero-isolated-mean-singular-faces-exclusion.md)已完整排除 $F_1=0,u=1$ 和 $F_2=0,\ell=0$。故本条的两图分别为
$$
g_1=-\frac{2fu\alpha+C_1}{2Q(u-1)},\qquad u\ne1,
$$
$$
g_2=\frac{2f\beta+C_2}{2\ell Q^2},\qquad \ell\ne0.          \tag{2.2}
$$
特别地，第一图上的 $\ell=0$ 没有被无故删除，第二图上的 $u=1$ 也没有由另一图的边界结果无故删除。

在每张图中，代入同一原五个必要式
$$
E_1,\quad E_B+E_C,\quad (E_B-E_C)/\kappa,
\quad N_B+N_C,\quad (N_B-N_C)/\kappa.                        \tag{2.3}
$$
它们均在形式二次代数中为偶式，故成为 $\mathbb Q(f,\ell,u,Q)$ 的有理式。取各化简分子，再反复以 gcd 精确移去下列已知非零乘积的因子：
$$
K_1=uQ(Q-1)DH(u-1),\qquad
K_2=uQ(Q-1)DH\ell.                                         \tag{2.4}
$$
得到五个多项式 $M_1,\ldots,M_5$。前三个是 $f$ 的二次式。其关于 $(f^2,f,1)$ 的三行系数矩阵在原共同根处必为奇异。对行列式仅移去 (2.4) 的因子后，精确分解为 $J$ 乘另一个多项式；后者在 $(\ell,u,Q)$ 的次数分别为 $(6,9,6)$ 和 $(8,11,7)$。源码从原三行系数验证这个分解，未保存计算数组。本条只支付这个因子 $J=0$，余因子另行处理。

## 3. $J=0$ 的全图和分母账目

若 $u=1/2$，则
$$
J=-(Q-1)/2\ne0.
$$
因此 $J=0$ 上可以且必须写为
$$
2u-1\ne0,\qquad
\ell=\ell_J:=\frac{u(2u+Q-2)}{Q(2u-1)}.                    \tag{3.1}
$$
将它代入原最高基值，精确得到
$$
H\big|_{\ell_J}
 =\frac{u(u-1)\bigl(Q+4u(u-1)\bigr)}{2u-1}.                \tag{3.2}
$$
特别地，$H\ne0$ 在此又保证 $u-1\ne0$。第二图所需的 $\ell\ne0$ 仍由其已付奇异面保证；第一图没有除去 $\ell$。

在第 $i$ 张图把 (3.1) 代入五个 $M_j$，取化简分子，仅移去
$$
\widehat K_i=\operatorname{num}(K_i|_{\ell_J})\,Q(2u-1)
$$
的因子，记结果为 $B_1,\ldots,B_5\in\mathbb Q[f,u,Q]$。由 (2.4)、(3.1)，$\widehat K_i$ 在原图上非零，因此移去的每个因子均有明确来源。这一步不按多项式次数或猜测选择某个不可约因子。

## 4. 完整 QQ 结式及唯一候选的原式回代

先对 $f$ 计算四个完整结式
$$
R_j=\operatorname{Strip}_{\widehat K_i}
       \operatorname{Res}_f(B_1,B_j),\qquad j=2,3,4,5.
$$
任何原有限共同根都使四者为零。接着计算三个完整的第二轮结式
$$
T_j=\operatorname{Res}_u(R_2,R_j),\qquad j=3,4,5.
$$
这里每张图的 $T_3$ 均恒等为零；源码和本条都保留这个零式，未将它当作非零约束。其余两个结式足以给出下表。次数 $-1$ 表示零多项式，gcd 只略去非零有理常数。

| 原 jet 图 | 三个第二轮结式的 $Q$ 次数 | 完整 QQ gcd |
| --- | --- | --- |
| $F_1=0$ | $-1,69,60$ | $Q^{19}(Q-1)^{12}(Q-2)^5$ |
| $F_2=0$ | $-1,232,220$ | $Q^{89}(Q-1)^{73}$ |

第二图只余 $Q=0,1$，均违反原配对范围，故全空。第一图只余 $Q=2$。将 $Q=2$ 直接代回本图全部五个 $B_j$，在 $\mathbb Q[f,u]$ 中的完整约化 lex Gröbner 基为
$$
\{1\}.
$$
因此第一图也全空。这里没有用结式结果替代原最高式或原第二梯度的充分性；仅用原必要式已得到矛盾。首项降阶可能引入的额外候选被完整保留到 $Q=2$ 并回原式排除。

## 5. 自含核验和后续范围

配套[自含源码](../notes/2026-11-26-unit211-nonzero-base-highest-zero-isolated-mean-linear-weight-face-347c.py)从原 Frobenius 乘法、原 $K_B$、$E,P,N$ 与一阶 jet 重建 (1.2)，核验两因子 (2.1)、五个原对称式、两个三行行列式的 $J$ 因子、(3.1)–(3.2)、所有 QQ 结式和 gcd，以及唯一末纤维的完整 Gröbner 基。它只以已证明非零乘积作反复 gcd 删除；所有多项式和 Gröbner 数组仅在内存内生成。

依赖 Python 3.12.14、SymPy 1.14.0、python-flint 0.9.0。实际执行为 `PYTHONPATH=/tmp/isp-347c05929dd3/deps python 2026-11-26-unit211-nonzero-base-highest-zero-isolated-mean-linear-weight-face-347c.py`，exit 0，程序计时 1.30923 秒，峰值 RSS 64372 KiB。源码 SHA256 为 `a5a848592942b59087c7b276473b9820ba2bde7406055f0f71a62e2c69639495`。

本条完整支付 $J=0$，所以剩余两张原 $m=0,P_0\ne0$ 图都可使用 $J\ne0$。剩余的高次权重面和同一原物理条件继续另证；本条不宣称整个 R150 分支或普通 Hilbert 空间不变子空间问题已解决。
