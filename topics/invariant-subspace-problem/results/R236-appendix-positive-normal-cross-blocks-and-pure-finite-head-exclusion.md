# R236 附录：真实尾交的正交叉块、条件锚与纯有限头排除

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的辅助结论。** 本文只在实际一次尾交的单位奇块条件内工作。全部正态、尾交和源均为原 Haar 表示中的对象；不把递推后商 $G_j$ 换成原始慢行的简单尾比。一般正常见证及普通 ISP 仍开。

## 1. 实际一次消元与同一个正态

在当前实际尾写
$$
N=\begin{pmatrix}0&t\\I&0\end{pmatrix},\qquad
t=\eta\widehat N_{\rm next},\quad
\|t\|\le\eta<1,
$$
$$
S=C+ND=D(N+G),\qquad G=D^{-1}C,
\qquad D\in\mathcal B_{\rm next}^{\times}.
\tag{1.1}
$$
$C,D,G,t$ 属于真实范数尾代数，故彼此交换，且与所有完整尾右因子
$R\in\mathcal C_{\rm next}$ 交换。
设 $0\ne\rho\ge0$ 为当前空间的迹类密度，
$$
\tau=\operatorname{Tr}\rho,
\qquad \operatorname{Tr}(\rho S Q)=0
\quad(Q\in\mathcal C_{\rm cur}).
\tag{1.2}
$$
令 $\sigma=\operatorname{Tr}_{\mathbb C^2}\rho$。
取实际右因子 $D^{-1}R$ 及 $D^{-1}(N-G)R$，得
$$
\operatorname{Tr}(\rho(N+G)R)=0,
\qquad
\boxed{\operatorname{Tr}(\sigma(G^2-t)R)=0.}
\tag{1.3}
$$
第二式正是 R236 完整一次尾交的第一生成元。
每个实际逆都保留在 (1.1) 与测试内；不要求这些逆沿递推一致有界。

## 2. 正交叉块给出不乘 $\|G\|$ 的全右泛函界

把 $\rho$ 写成物理块
$$
\rho=\begin{pmatrix}\rho_{00}&B\\B^*&\rho_{11}\end{pmatrix},
\qquad \sigma=\rho_{00}+\rho_{11}.
$$
取 Hilbert--Schmidt 平方分解 $\rho=WW^*$，把 $W$ 的两行记为 $a,b$。
于是 $B=ab^*$、$\sigma=aa^*+bb^*$。
令
$$
\Omega_+=(e_0+e_1)/\sqrt2,\quad
\chi=(e_0-e_1)/\sqrt2,\quad
r=\operatorname{Tr}\bigl(\rho(|\chi\rangle\langle\chi|\otimes I)\bigr).
$$
则 $\|a-b\|_2^2=2r$、$\|a\|_2^2+\|b\|_2^2=\tau$，且
$$
B-\frac\sigma2
=\frac12\big[(a-b)b^*-a(a-b)^*\big].
$$
Hilbert--Schmidt 乘积的迹范数不等式和二项 Cauchy 给
$$
\boxed{\left\|B-\frac\sigma2\right\|_1\le\sqrt{\tau r}.}
\tag{2.1}
$$
这一界不要求 $\rho$ 的秩有限，也不要求其各块交换。

置
$$
L=\frac{I+t}{2},\qquad
\psi(R)=\operatorname{Tr}\bigl(\sigma(G+L)R\bigr).
$$
直接按块计算 (1.3) 第一式，得
$$
\operatorname{Tr}(\sigma GR)
=-\operatorname{Tr}\bigl((B+B^*t)R\bigr).
$$
因此准确有
$$
\psi(R)=-\operatorname{Tr}
\left(\left[B-\frac\sigma2+\left(B^*-\frac\sigma2\right)t\right]R\right).
\tag{2.2}
$$
对完整尾交换子的单位球取上确界，(2.1) 给
$$
\boxed{
\|\psi\|_{(\mathcal C_{\rm next})_*}
\le(1+\eta)\sqrt{\tau r}.
}
\tag{2.3}
$$
这里没有因 $G$ 的范数而放大正常尾误差。该消去来自同一正密度的实际交叉块，
而非把 $G$ 代入一般迹范数近似后漏掉 $\|G\|$。

## 3. 精确零式迫使真实商的成本增长

因为
$$
(G+L)(G-L)=G^2-t-\frac{(I-t)^2}{4},
$$
对 (1.3) 使用合法尾右因子 $(I-t)^{-2}$，得到
$$
\psi\bigl((G-L)(I-t)^{-2}\bigr)=-\frac\tau4.
\tag{3.1}
$$
真实逆由 $\|t\|<1$ 保证，并有 $\|(I-t)^{-2}\|\le(1-\eta)^{-2}$。
结合 (2.3)，
$$
\boxed{
\frac r\tau
\ge
\frac{(1-\eta)^4}
{16(1+\eta)^2\|G-L\|^2}.
}
\tag{3.2}
$$
若 $r=0$，(2.3) 与 (3.1) 直接矛盾；分母零的情形也不能发生在非零见证上。
等价地，
$$
\|G-L\|\ge
\frac{(1-\eta)^2}{4(1+\eta)}\sqrt{\frac\tau r}.
\tag{3.3}
$$

现在从原首形式阶一的 $S_0$ 沿 R236 的**真实**递推
$$
S_j=C_j+N_jD_j,
\quad G_j=D_j^{-1}C_j,
\quad S_{j+1}=G_j^2-\eta_jN_{j+1}
\tag{3.4}
$$
继续。每个 $D_j$ 都是实际单位，$S_j$ 首形式阶仍一。
若原正常 $\rho_0$ 湮灭 $S_0\mathcal A'$，同一正部分迹
$\rho_j=\operatorname{Tr}_{K_j}\rho_0$ 湮灭 $S_j\mathcal C_j$。
令 $r_j=\operatorname{Tr}(\rho_0P_{\chi_j})$。
实际单个位 Walsh 投影 $P_{\chi_j}$ 强趋零，因为对任意固定有限 Walsh 柱最终作用为零，
故 $r_j\to0$。因此 (3.3) 迫使
$$
\boxed{\|G_j\|\longrightarrow\infty.}
\tag{3.5}
$$
这是一条必要条件，尚未估计真实递推商的上界。
$G_j$ 不能换成未经消元的原始慢行 $\sum_{k>j}a_kN_k/a_j$。
也没有从 $\sum_jr_j$ 的发散推出非正常性：正常态可以具有无穷平均 Walsh 孔数。

## 4. 一个不需要新增商逆的实际条件锚

令 $e:\mathscr H_{\rm next}\to\mathscr H_{\rm cur}$ 为 $eh=\Omega_+\otimes h$。
由于 $N^2=t$，
$$
(I+N)^{-2}=(I+t-2N)(I-t)^{-2}.
$$
实际整尾算子压缩满足 $e^*Ne=L$，故
$$
\boxed{
e^*(I+N)^{-2}e=0,
\qquad e^*N(I+N)^{-2}e=\frac I2.
}
\tag{4.1}
$$
取真实源与目标
$$
R_S=2D^{-1}(I+N)^{-2},
\qquad
\Theta=SR_S=2(N+G)(I+N)^{-2}.
\tag{4.2}
$$
则
$$
\boxed{\Theta\in S\mathcal C_{\rm cur},\qquad e^*\Theta e=I.}
\tag{4.3}
$$
它不要求求 $(G+L)^{-1}$，也不引入一个新的未知分母。
原有 $D^{-1}$ 的费用没有省略：
$\|N\|=1$ 且 $(I+N)^{-1}=(I-N)(I-t)^{-1}$，所以
$$
\boxed{
\|R_S\|\le\frac{8\|D^{-1}\|}{(1-\eta)^2},
\qquad
\|\Theta\|\le\frac{8(1+\|G\|)}{(1-\eta)^2}.
}
\tag{4.4}
$$
源范数与目标范数是两笔不同的费用。
在精确正常湮灭问题中，(4.3) 给每个有限层的准确零配对；
若将其用于近似理想或其他残量估计，则所有 (4.4) 及前级递推源费用仍须一起支付。

设原完整闭尾交为
$$
\mathcal J_j'=
\{b\in\mathcal C_j:I_{K_j}\otimes b\in
\overline{S_0\mathcal A'+Z_0\mathcal A'}^{\|\cdot\|}\},
$$
并按原定义令
$$
q_j^{\rm joint}
=\sup_{b\in\mathcal J_j',\,\|b\|\le1}|\omega_j(b)|.
$$
真实递推的精确尾交身份保证 $S_j\mathcal C_j\subset\mathcal J_j'$。
由 (4.2)–(4.3)，$\Theta_j\in\mathcal J_j'$ 且 $\omega_j(\Theta_j)=1$。
因此
$$
\boxed{
q_j^{\rm joint}\ge\frac1{\|\Theta_j\|}
\ge\frac{(1-\eta_j)^2}{8(1+\|G_j\|)}.
}
\tag{4.5}
$$
单行尾交也成立同一界。
若真实 $\|G_j\|$ 在某个趋向无穷的子列上有界，则对应 $\Theta_j$ 统一有界、
作用于越来越远的实际尾且期望准确为一，故 WOT 趋 $I$。
同一正常态不可能将这些元素全部湮灭。
于是这给出一个明确的充分排除条件：真实消元商存在有界子列。
本文没有证明该条件对原慢行成立。

## 5. 有限连续头的纯约化态不能是见证

以下结论允许该头以后的正密度完全任意，不要求它在任何乘积基中对角。

**定理 5.1。** 设当前实际 $S$ 属于范数尾代数、常数字符零且首形式阶为一。
若 $\rho\ge0$、$\rho\ne0$、迹类，且湮灭 $S\mathcal C_{\rm cur}$，
则对每个有限正长度的连续初始头，其约化密度不能为秩一。

证明：假设头维数为 $H=2^M$、约化态秩一。
正性给 $\rho=|u\rangle\langle u|\otimes\sigma$，其中 $\|u\|=1$、
$0\ne\sigma\ge0$ 迹类。确实，若头约化态支撑于 $\mathbb Cu$，
则 $\operatorname{Tr}\rho(I-|u\rangle\langle u|)=0$，
从而 $(I-|u\rangle\langle u|)\rho^{1/2}=0$，给出该张量因式。

令 $A_c$ 为当前真实归一化尾生成元。R124 的有限余数分解给
$$
S=\sum_{r=0}^{H-1}A_c^r b_r,
\qquad b_r\in\mathcal B_{\rm far},\qquad
A_c^H=zI_H,
\tag{5.1}
$$
其中 $z=d\widehat N_{\rm far}$、$d>0$，$\chi(b_0)=0$、$\chi(b_1)\ne0$。
因此 $b_1$ 是实际尾单位。
记 $J$ 为把远尾字符代入 $A_c$ 后得到的有限加权 nilpotent Jordan 串；
所有非零次对角权均严格正。令 $s(J)=\sum_r\chi(b_r)J^r$。

对 $0\le k<H$，取实际尾算子
$$
c_k=(\langle u|\otimes I)S A_c^k(|u\rangle\otimes I).
$$
它属于 $\mathcal B_{\rm far}$，且
$$
\operatorname{Tr}(\sigma c_kR)=0
\quad(R\in\mathcal C_{\rm far}),\qquad
\chi(c_k)=\langle s(J)J^ku,u\rangle.
\tag{5.2}
$$
如果任何 $\chi(c_k)\ne0$，则 $c_k$ 是实际单位；测试 $R=c_k^{-1}$ 与
$\operatorname{Tr}\sigma>0$ 矛盾。
所以所有这些字符必须为零。

因 $s(J)=Jv(J)$、$v(0)\ne0$，
$s(J),s(J)J,\ldots,s(J)J^{H-2}$ 张成
$J,J^2,\ldots,J^{H-1}$。于是
$$
\langle J^ru,u\rangle=0\quad(1\le r<H).
\tag{5.3}
$$
若 $u$ 至少有两个非零物理坐标，取其最小和最大指标 $i<j$。
在 $\langle J^{j-i}u,u\rangle$ 中，唯一可能的非零项是
从 $i$ 到 $j$ 的正权乘积乘 $u_i\overline{u_j}$，因而非零。
故 (5.3) 迫使 $u$ 为某个物理基向量 $e_i$ 乘一相位。

对于这个剩余情形，在 (5.1) 中计算 $S A_c^{H-1}$ 的第 $i$ 个对角块。
指数区间 $H-1,\ldots,2H-2$ 中只有 $H$ 可给对角块，故准确有
$$
c_{H-1}=z b_1.
$$
由 (5.2) 并右乘 $b_1^{-1}$ 得
$\operatorname{Tr}(\sigma zR)=0$ 对全部远尾右因子成立。
远方真实归一化幂 $N_l$ 都是 $z$ 的一个真实有界右倍数，且
$N_l\to I/2$ 于 WOT、范数统一有界。
正常性遂给 $0=\lim_l\operatorname{Tr}(\sigma N_l)=\operatorname{Tr}\sigma/2$，矛盾。证毕。

对原见证先取到第 $j$ 位的正部分迹，再用真实 (3.4)，可将定理应用于
从任意 $j$ 开始的有限连续块。故同一见证的每个这样的有限块约化态都至少秩二。
这仍允许各块任意接近纯态，也允许一般无限纠缠见证；没有将所有有限秩正态排除。

## 6. 下一实际缺口

本文付出了完整交叉块约束、一个精确条件锚及其原源费用、
和任意尾正密度下的纯有限头排除。
还须估计真实递推 $G_j=D_j^{-1}C_j$，或用联合第二生成元得到更强的来源限制。
目前既没有其有界子列，也没有把同一正常态的 $r_j\to0$ 变成足以抵消实际逆增长的速率。

已证输入均在仓库内：R124 的真实余数分解及首阶一性质；
R253 的正部分迹和远尾弱单位；R236《算子系数 Walsh 首列提升、联合最大子式与精确一次尾交》§§5–7 的完整尾交与两生成元递推。


后续实际界已分开支付：[原正慢行的真实递推增长](R236-appendix-positive-slow-row-true-recursive-quotient-growth.md)证明指定未修正商和目标均至少有四次dyadic指数成本；[完整尾理想的商距离](R236-appendix-full-tail-ideal-quotient-cost-and-normal-anchors.md)则允许全部理想修正，不能由未修正范数推断其结论。
