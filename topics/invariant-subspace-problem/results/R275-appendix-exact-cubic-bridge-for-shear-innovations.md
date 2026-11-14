# R275 附录：相邻剪切创新的准确三次权桥公式

日期：2026-11-14。会话：Astra-ISP-789f / literature_audit。作者：ChatGPT，GPT-6 Astra Pro。

**状态：以下身份已证明；创新正性仍未证明。** 本稿续[一位完整 Schur 递推](R275-one-bit-full-primitive-schur-recursion-and-innovation.md)，不修改已交付稿，也不把同一目标仅改写为新的完成声明。新增点是消去其中所有 $T_j$：每个相邻剪切创新准确由两个旧出生的真实 Gram 和同一个原 Boolean 三次权桥给出，包括最高硬端。

## 1. 定义与规范

沿用旧 $M$ 位正权行 $d=\sum b_iE_i$，新出生 $s\ge1$，新满长 $h=M+1-2s\ge2$。
$$K=\ker d\cap\mathcal H_s,\qquad L=\ker d\cap\mathcal H_{s-1},\qquad R=d_s^\dagger|_L.$$
旧两个出生的归一最小逆 Gram 分别是 $G_j$（$K$ 上，$0\le j\le h-1$）与 $L_j$（$L$ 上，$0\le j\le h+1$）。两者用 $d^j/j!$，不是用真 $d^j$。

定义同一个实际算子
$$C=\sum_{i=1}^M b_i^3E_i,\qquad B=C|_K:K\to L.\tag{1.1}$$
因 $[d,C]=0$，其像确实在 $L$。$B^*:L\to K$ 是原 Hilbert 伴随，含真实 primitive 投影；不是把 $C^*$ 原样限制而丢掉投影。

在整个 Boolean 空间上直接有
$$[d,[d,d^*]]=-2C,\qquad[d,C]=0.\tag{1.2}$$
既有[三次权 MP 桥](R239-appendix-boolean-cubic-mp-bridge-top-layer-anchor-and-polynomial-top-cost.md) §§2–3 在原无限尾证明了相应身份。这里逐项给出有限满秩范围，以接到一位递推的硬端。

## 2. 真幂两个下降及其桥系数

令 $J_{t,b}=(d^t)^\dagger|_{K_b}$、$H_{t,b}=J_{t,b}^*J_{t,b}$ 为**真幂**最小逆；所以
$$H_{t,s}=G_t/(t!)^2,\qquad H_{t,s-1}=L_t/(t!)^2.$$
在孔层中用实际正交核层 $W_{r,p}=\ker d^r\ominus\ker d^{r-1}$。

由 (1.2) 的交换展开，$d^*$ 把 $\ker d^r$ 映入 $\ker d^{r+2}$。取伴随并用 $d(\ker d^{r+1})\subset\ker d^r$，得 $d$ 在这些真实核层上只有第一、第二下降 $d_1,d_2$。

同一真 MP 唯一性给
$$d_1J_{t,b}=J_{t-1,b}.$$
对 $t\ge2$、$v\in K$，令 $z=J_{t-2,s}v$，则 $d^{t-1}z=0$，完整交换式给
$$d^td^*z=-t(t-1)Cv.$$
投到最高实际核层，得到
$$d_2^*J_{t-2,s}=-t(t-1)J_{t,s-1}B.\tag{2.1}$$

写第二下降为
$$d_2J_{t,s-1}=J_{t-2,s}\,K_t.$$
将 (2.1) 按实际 Hilbert 内积取伴随，严格保留次序，得到
$$\begin{aligned}
K_t&=-t(t-1)H_{t-2,s}^{-1}B^*H_{t,s-1}\\
&=\boxed{-\frac1{t(t-1)}G_{t-2}^{-1}B^*L_t.}
\end{aligned}\tag{2.2}$$
全部 $2\le t\le h+1$ 都合法：下出生的最高真幂为 $h+1$，上出生只用到 $t-2\le h-1$。特别没有需要不存在的 $G_h$。

## 3. 旧最小右逆的准确差分

置
$$U_j=d^jJ_{j+1,s-1}:L\to\mathcal H_s,\qquad0\le j\le h.$$
它始终满足 $d_sU_j=I_L$。
当 $j\le h-1$，由完整约束最小化
$$U_j=F_jd_s^*(d_sF_jd_s^*)^{-1}=R-T_j,$$
其中 $F_j=d^j(d^*)^j/(j!)^2$ 是旧整层 Gram。最顶 $j=h$ 时右式的 $F_h$ 虽可奇异，$d_sF_hd_s^*$ 仍可逆，且
$$U_h=(I-U)R,$$
$U$ 是前稿沿 $\operatorname{Ran}(d^h)$ 投到 $K$ 的真实斜投影。所以可统一记 $T_h=UR$，全范围都有 $U_j=R-T_j$。

将真 MP 两下降式
$$dJ_{j+1,s-1}=J_{j,s-1}+J_{j-1,s}K_{j+1}$$
再作用 $d^{j-1}$，得
$$\boxed{U_j-U_{j-1}=K_{j+1},\qquad1\le j\le h.}\tag{3.1}$$
此处 $d^{j-1}J_{j-1,s}=I_K$，并没有把真幂 MP 换为逐次 MP。

前稿的剪切为
$$Q_j=(j+1)T_j-jT_{j-1}
=R-(j+1)U_j+jU_{j-1}.$$
使用 (3.1)，准确得到
$$Q_j-Q_{j-1}=(j-1)K_j-(j+1)K_{j+1}.\tag{3.2}$$
当 $j=1$，第一项按零处理，等于 $-2K_2$。

代入 (2.2)，就是所需全高度公式：
$$\boxed{
Q_j-Q_{j-1}
=\frac1j\left(G_{j-1}^{-1}B^*L_{j+1}
-G_{j-2}^{-1}B^*L_j\right),\quad1\le j\le h.
}\tag{3.3}$$
只为这条精度公式约定 $G_{-1}^{-1}=0$。它既不增加一个旧出生，也不定义一个虚假的可逆 Gram。

最高 $j=h$ 的式子是通过真实顶端原像和两下降给出的，不是将内点解析式强行延伸到旧奇异层。

## 4. 与已隔离的创新 Schur 条件接合

令 $C_j=G_j^{-1}$。对前稿的相邻高度 $n$，两条真实创新准确为
$$\Delta_- =\frac1n(C_{n-1}B^*L_{n+1}-C_{n-2}B^*L_n),$$
$$\Delta_+ =\frac1{n+1}(C_nB^*L_{n+2}-C_{n-1}B^*L_{n+1}).\tag{4.1}$$
其中全部 $G,L$ 在旧合法域内。把它们代入前稿 (5.2)，就把一位归纳的未知块完全写成旧真实 Gram、实际同一个 $B$ 和添加位权 $a$，不再有未定义的跨出生漂移。

但 $G,L$ 各自相邻正性**不单独约束任意放大的 $B$**。因此不能删去它的 Boolean 来源，将 (4.1) 当作任意矩阵参数然后宣布完整块正。真正还需用 (1.1)–(1.2) 或相应的联合 Gram，支付实际 $B$ 与旧两种精度缺陷之间的交叉 Cauchy–Schwarz 控制。

特别前稿必要条件仍是
$$a^2P_n\Delta_+V_{n+1}^{-1}\Delta_+^*P_n
\preceq P_{n-1}-P_nP_{n+1}^{-1}P_n,$$
且还须保留完整交叉 Schur。三次桥身份给了实际创新，并没有自动给这个正序。

## 5. 核验范围

配套[精确校准脚本](../notes/2026-11-14-one-bit-cubic-innovation-789f-next.py) 独立从完整物理逆构造 $T_j$ 和顶端斜投影，再与 (3.3) 比较。它使用真实三次权删除的 primitive 限制，不从 (3.3) 反向定义 $B$。一般出生及最高硬端均纳入。

本稿是一般有限正权 Boolean 的精确结构结果，不是任意正权相邻序的证明；原连续尾推广、首头 graph 逆传播和普通 ISP 均不随之自动闭合。
