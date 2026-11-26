# R150 附录：单位 2+1+1 非零最高基值、零孤立点均值支路的两个奇异 jet 面为空

作者：Astra-ISP-347c-20261126 / unit31_general；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条精确范围已证明。** 本条仍在同一原单位 $2+1+1$ 加孤立零点分支内，研究两个不同、非相反、非零的基点配对，且原最高基值 $P_0\ne0$、孤立零点均值 $m=0$ 的情形。原二阶梯度 jet 分成两张一次图后，本条完整支付各自新的分母零面：$F_1=0,u=1$ 与 $F_2=0,\ell=0$。两张图的非零分母一般部分仍须继续，未在这里宣称整个 $m=0$ 分支为空。

## 1. 共同齐次坐标保留同一原方程

保留原长度五除子 $2A+B+C+Z$、同一原物理曲线和非退化六维配对、单位代数
$$
\mathcal B=\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,
\quad \tau(X)=aX_0+X_1+bX_B+cX_C,\quad a=1-b-c,
$$
以及全部原 mean、最高式、第二梯度的值与一阶 jet。原活跃 Gram 为
$$
K_B=\begin{pmatrix}
0&0&p&q\\0&A_1&r&s\\p&r&0&t\\q&s&t&0
\end{pmatrix}.
$$

在本条的 $p+q\ne0$ 范围，所有 Gram 配对与零点配对列共同作非零齐次变元，使 $p+q=2$。原 mean 为二次，原 $P,N$ 值和 jet 以及相应零点三次式均为三次，故每个原解导出这个归一的必要系统。共同缩放保持完整物理 Gram 的秩；这里没有独立改变一个配对或改换物理二次型。[$p+q=0$ 原分支](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-exclusion.md)已由独立完整证明支付。

写
$$
p=1-\kappa,\quad q=1+\kappa,\quad Q=pq=1-\kappa^2,
\quad Q\ne0,1.
$$
$Q\ne0$ 表示两个配对均非零，$Q\ne1$ 表示它们不同。形式关系 $\kappa^2=1-Q$ 同时保留两个 $\kappa$ 根；不选定实根或某个符号。令
$$
\ell=b+c,\quad u=bp+cq,\quad
b=\frac{\ell q-u}{2\kappa},\qquad
c=\frac{u-\ell p}{2\kappa}.
$$
于是
$$
D=\ell^2Q-2\ell u+u^2,\qquad
bc=\frac{D}{4(Q-1)}\ne0.                                    \tag{1.1}
$$
原零基点 mean $u=0$ 已由[完整零基点 mean 专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)排除，本条故有 $u\ne0$。

原最高基值精确为
$$
2P_0=\ell Q(3u-2)+2u^3-6u^2+(4-Q)u\ne0.                     \tag{1.2}
$$
记原孤立零点配对列为 $U=(u_0,u_1,u_B,u_C)$，$m=\tau(U)$。最高式给 $P_0=-u_0^3$，第二梯度给
$$
(N_0,N_1,N_B,N_C)=(-mu_0^2,-2mu_0u_1,-mu_B^2,-mu_C^2).
$$
因此 $P_0\ne0$ 时，$m=0$ 等价于 $N_0=0$；原完整临界性还要求
$$
N_1=N_B=N_C=0.                                               \tag{1.3}
$$
后文只从这些原必要条件推导矛盾，不把它们当作存在性的充分条件。

## 2. $E_0=N_0=0$ 的全局图没有新的未付分母

令 $d=D_K1$、$f=\tau(d)/2$、$x=d_B$、$y=d_C$，并用加权交叉配对
$$
g=bc\,t.
$$
由于 $bc\ne0$，这是可逆变元。设
$$
V=bp^2+cq^2=2u-\ell Q,\quad
W_1=bp x+cq y,\quad W_2=bp^2x+cq^2y.
$$
直接从原 $E,P,N$ 的 Frobenius 定义得到
$$
E_0=V-2W_1-2u^2+4fu,
$$
$$
N_0=\frac{W_2-fV}{2}-uW_1+fu^2+\frac{Qg}{2}.
$$
因此原 $E_0=N_0=0$ 全局等价于
$$
W_1=V/2-u^2+2fu,
\qquad W_2=uV-2u^3+f(V+2u^2)-Qg,                             \tag{2.1}
$$
$$
x=\frac{qW_1-W_2}{bp(q-p)},\qquad
y=\frac{W_2-pW_1}{cq(q-p)}.                                  \tag{2.2}
$$
每个分母由 $bcQ(Q-1)\ne0$ 已知非零。原剩余参数恢复为
$$
r=x-ap-ct,\qquad s=y-aq-bt,\qquad
A_1=2f-2bx-2cy+2bct,
\qquad t=g/(bc).                                              \tag{2.3}
$$
源码从同一原乘法核验 (2.1)–(2.3) 后的 $E_0=N_0=0$ 与 $\tau(d)/2=f$，没有改写梯度或任意指定 Gram 行。

## 3. 原一阶 jet 的两因子及精确范围

定义
$$
\alpha=Q(\ell-1)-2u(u-1),
\qquad \beta=\ell^2Q^2+2Qu^2(1-\ell)+4u^2(u-1),
$$
$$
C_1=\ell(1-\ell)Q^2+4u^2(u-1)^2+2u(u-1)Q,
$$
$$
C_2=\ell Q^2\bigl(2\ell(u-1)-u\bigr)
 +4\ell u(u-1)(u-2)Q-2u^2(u-1)(4u-4+Q).
$$
在完整原图 (2.1)–(2.3) 上，原 $N_1$ 的化简分子除非零有理常数外恰为
$$
F_1F_2,
$$
$$
F_1=2fu\alpha+2gQ(u-1)+C_1,
\qquad F_2=2f\beta-2g\ell Q^2+C_2.                           \tag{3.1}
$$
分母只来自 (1.1)、(2.2) 的非零量。这个身份由原值和一阶 jet 直接展开验证，不是根据实验猜出的因子。

于是每个原解在 $F_1=0$ 或 $F_2=0$。第一因子对 $g$ 的系数是 $2Q(u-1)$；第二因子的是 $-2\ell Q^2$。本条精确支付的是
$$
\{F_1=0,u=1\}\quad\text{和}\quad\{F_2=0,\ell=0\}.           \tag{3.2}
$$
并不把 $F_2=0,u=1,\ell\ne0$ 或 $F_1=0,\ell=0,u\ne1$ 擅自列为已排除；它们属于相应可解的一般图。

## 4. 两面的交点及解 $f$ 的新分母

在 $u=1$，(1.2) 给 $2P_0=Q(\ell-1)$，故 $\ell\ne1$；而
$$
F_1=Q(\ell-1)(2f-Q\ell).
$$
第一奇异面因此必须
$$
f=Q\ell/2.                                                   \tag{4.1}
$$

在 $\ell=0$，原第二因子为
$$
F_2=2u^2\bigl(2f(2u+Q-2)-(u-1)(4u-4+Q)\bigr).
$$
若 $2u+Q-2=0$，原括号等于 $-2(u-1)^2$，所以 $u=1,Q=0$，与 $Q\ne0$ 矛盾。因此这一面的全部情形都可且必须写成
$$
2u+Q-2\ne0,\qquad
f=\frac{(u-1)(4u-4+Q)}{2(2u+Q-2)}.                           \tag{4.2}
$$

两面的交点 $u=1,\ell=0$ 均迫 $f=0$。将这些值代回原 mean，除去已知非零的 $Q,Q-1$ 因子后，两个剩余 mean 精确为
$$
g^2-g-\frac12=0,\qquad g^2=0.
$$
二者矛盾。因此交点完整排除；在第一面还可使用 $\ell\ne0$，在第二面还可使用 $u-1\ne0$。

## 5. 第一奇异面 $u=1$ 的唯一末纤维违反 Frobenius 条件

将 (4.1) 代回同一原五个必要式
$$
E_1,\quad E_B+E_C,\quad (E_B-E_C)/\kappa,
\quad N_B+N_C,\quad (N_B-N_C)/\kappa.                          \tag{5.1}
$$
$\kappa\ne0$ 已付；对称组合在形式代数 $\kappa^2=1-Q$ 中均为偶式，所以给出 $\mathbb Q[g,\ell,Q]$ 上的有理式，保留两种点标号与全部原 mean/N。

取各化简分子，仅以反复 gcd 精确除去已知非零乘积
$$
Q(Q-1)(\ell-1)(\ell^2Q-2\ell+1)
$$
的因子，得到 $M_1,\ldots,M_5$。对 $g$ 计算四个完整结式 $\operatorname{Res}_g(M_1,M_j)$，$j=2,\ldots,5$，仍仅移去上述非零因子，并移去已由交点排除支付的 $\ell$ 因子，记为 $R_2,R_3,R_4,R_5$。

接着计算 $\operatorname{Res}_{\ell}(R_2,R_j)$，$j=3,4,5$。三个真正有理数多项式的次数为 $22,58,44$，精确 gcd 除非零常数外为
$$
Q^8(16Q-15)^4.                                               \tag{5.2}
$$
所以只剩 $Q=15/16$。将该值回代原五个 $M_i$，其在 $\mathbb Q[g,\ell]$ 中的约化 lex Gröbner 基恰为
$$
g^2,\quad g\ell^2-\frac{32}{15}g\ell+\frac{16}{15}g,
\quad
\ell^3-\frac{52}{15}\ell^2+\frac{176}{45}\ell-\frac{64}{45}.
$$
最后一式是 $(\ell-4/3)^2(\ell-4/5)$。而原 Frobenius 分子
$$
D=\frac{15}{16}\ell^2-2\ell+1
 =\frac{15}{16}(\ell-4/3)(\ell-4/5).
$$
因此所有候选都给 $D=0$，违背 $bc\ne0$。源码还无除法核验 $D^2$ 对上述完整基的余式为零。第一奇异面全空。

## 6. 第二奇异面 $\ell=0$ 的唯一末纤维违反 $u\ne0$

将 (4.2) 代回同一原五式 (5.1)。取化简分子，仅以 gcd 移去已知非零乘积
$$
uQ(Q-1)(2u+Q-2)(2u^2-6u+4-Q)
$$
的因子。最后一因子来自 $2P_0=u(2u^2-6u+4-Q)\ne0$。仍先对 $g$ 作四个完整结式，再移去已付的 $u-1$ 交点因子。对 $u$ 作三个第二轮结式，其次数为 $59,92,88$，精确 gcd 除非零常数外为
$$
Q^{45}(Q-4)^8.                                               \tag{6.1}
$$
只剩 $Q=4$。直接将该值回代本面的五个原多项式，其在 $\mathbb Q[g,u]$ 中的完整约化基为
$$
\{g+u/2,\ u^2\}.                                             \tag{6.2}
$$
它迫 $u=0$，与已知非零基点 mean 矛盾。因此第二奇异面亦全空。

以上两轮结式只使用有限共同根必使结式为零的必要方向。由首项下降产生的额外根也完整保留到 (5.2)、(6.1) 和末纤维原式回代，没有遗漏被除数的零支路。

## 7. 自含原式核验及后续范围

配套[自含 QQ 源](../notes/2026-11-26-unit211-nonzero-base-highest-zero-isolated-mean-singular-faces-347c.py)直接实现原 Frobenius 乘法、原 Gram、$E,P,N$ 及一阶 jet，在形式二次代数 $\kappa^2=1-Q$ 内重建 (2.1)–(2.3)。它精确核验 $bc$ 与 $P_0$、原 $N_1$ 两因子、两个新除数的边界、交点矛盾、全部 QQ 结式与 gcd，以及两个末纤维的完整 Gröbner 基。计算数组只在内存中，不保存表格或证书数组。

依赖 Python 3.12.14、SymPy 1.14.0、python-flint 0.9.0。实际执行为 `PYTHONPATH=/tmp/isp-347c05929dd3/deps python 2026-11-26-unit211-nonzero-base-highest-zero-isolated-mean-singular-faces-347c.py`，exit 0，程序计时 1.138905 秒，峰值 RSS 63756 KiB；源码 SHA256 为 `1b0d38f1cf761cd704e3df9cfe50b58992e1ff73a517c34ef5e5b9771961503b`。首次仅一个 SymPy 展开式与因子式的结构比较失败，改为差式精确展开后按最终字节完整重核通过，数学定义未变。

本条支付了 (3.2) 的全部边界，故原 $m=0,P_0\ne0$ 支路余下两面可分别合法解 $g$：$F_1=0,u\ne1$，或 $F_2=0,\ell\ne0$。它没有排除这两面的一般部分，也没有将抽象必要方程解称作原物理临界点；整个课题仍需继续。
