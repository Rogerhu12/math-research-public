# R185/R188 附注：真实边界核中的弱复制序列与全部幂非紧性

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整证明；仅补充两个具体边界核的结构，不另编号。

本稿使用 R185、R188 已经逐项建立的有限块纠错算子，证明其中实际构造的核向量可以沿新空坐标弱复制。对每个固定 UHF 算子，复制序列保留该向量的作用范数。由此，两种具体边界核及其稳定闭像部分上的加权后移全部正次幂都非紧。证明不把整个核中的任意向量都视为可复制，也不由非紧性判断尚未解决的内部饱和问题。

## 1. 两个实际模型与所用构造类

在负整数边界 $\mathcal H_-=\ell^2(\mathbb N_0)$ 上，令
$$
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1},\qquad
\mathsf N_j=B^{2^j}/d_j,\qquad
\mathsf Y_j=\mathsf N_j(I+\mathsf N_j)^{-1}.
$$
取
$$
a_j=(j+1)^{-2},\qquad A_0=\sum_j a_j\le2,
$$
以及两个算子中的任意一个：
$$
T_N=\sum_j a_j\mathsf N_j,\qquad
T_Y=\sum_j a_j\mathsf Y_j.
\tag{1.1}
$$
本稿以 $T$ 统一表示所选算子，置 $M=\ker T$。
纯孔消灭算子记为 $\mathsf E_j$，其伴随是纯孔创建算子。
这些孔坐标属于负整数边界，不是原 Haar 空间的 Walsh 次数。

沿用实际权界
$$
\eta_j=\alpha_{j+1}/\alpha_j
\le \exp(-770\,16^j),\qquad
\|\mathsf N_j\|\le1,\qquad
\|\mathsf N_j-\mathsf E_j\|\le\eta_j,
$$
$$
\|(I+\mathsf N_j)^{-1}\|\le3,\qquad
\|\mathsf Y_j-\mathsf E_j\|\le4\eta_j.
\tag{1.2}
$$
最后一个估计由
$\mathsf Y_j-\mathsf N_j=-\mathsf N_j^2(I+\mathsf N_j)^{-1}$
及 $\mathsf N_j^2=\eta_j\mathsf N_{j+1}$ 得到。

R185/R188 的具体归一化构造给出 $g\in M$ 及有限向量 $g_n$：
$$
g_n\in\mathcal F_{m_n},\qquad
g_n\longrightarrow g,\qquad
\sup_n\|g_n\|<\frac32,\qquad
\|Tg_n\|\le \epsilon_{m_n}:=\exp(-40\,4^{m_n}).
\tag{1.3}
$$
它的递归指标满足
$$
L_n=64\,2^{m_n},\qquad m_{n+1}=2L_n,
\tag{1.4}
$$
而 $g_{n+1}$ 的所有非真空坐标只出现在
$$
[0,m_n)\ \cup\ [L_n,2L_n).
\tag{1.5}
$$
特别是间隔 $[m_n,L_n)$ 真正全真空。
原构造从单位向量出发，修正总范数小于 $1/4$，所以 (1.3) 的范数界成立，且 $g\ne0$。

以下证明也适用于任何具有 (1.3)—(1.5) 的同类实际构造。
不预先断言每个 $M$ 向量都具有这样的近似。

## 2. 一个允许较弱首步残差的实际修复引理

先把 R185/R188 的第一步预算单独写出。
给定 $m\ge2$，置
$$
L=64\,2^m,\qquad m^+=2L,\qquad
\mathcal A_m=\exp(8m2^m).
$$
对任意 $v\in\mathcal F_m$，两篇已证明的同一有限块构造产生
$\mathcal R_m v\in\mathcal F_{m^+}$，满足
$$
\|\mathcal R_mv-v\|\le\mathcal A_m\|Tv\|,
\tag{2.1}
$$
$$
\|T\mathcal R_mv\|
\le26\eta_{L-1}\|\mathcal R_mv\|.
\tag{2.2}
$$
对 $T_N$ 原常数为 4；统一使用 26 同样合法。
每一个修正项在新块 $[L,2L)$ 中有孔，所以
$$
\mathcal R_mv-v\ \perp\ \mathcal F_L.
\tag{2.3}
$$
(2.1) 是任意有限输入的估计，不需要先满足 $\epsilon_m$ 预算；
(2.2) 来自精确模型核与实际空间隔误差。

设
$$
\|v\|\le\frac32,\qquad
\mathcal A_m\|Tv\|\le\frac18.
\tag{2.4}
$$
则 $\|\mathcal R_mv\|\le13/8$，且
$$
\|T\mathcal R_mv\|
\le43\eta_{L-1}
\le43\exp\!\left(-\frac{770}{16}\,16^L\right)
\le\exp(-40\,4^{m^+}).
\tag{2.5}
$$
最后使用 $m^+=2L$、$4^{m^+}=16^L$ 及 $770/16=48.125$；
$L\ge256$ 已使常数 43 被剩余指数余量吸收。

于是第一次修正之后，才进入 R185/R188 原有的标准 40 预算。
后续每一步的修正至多 $\exp(-20\,4^{m_\nu})$。
因指标严格增加且增长更快，后续总修正至多
$2\exp(-20\,4^{m^+})$。
这些修正的总量小于 $1/8$，全程范数小于 2，故标准归纳合法。

因此存在真实 $w\in M$，使
$$
\boxed{
\|w-v\|
\le\mathcal A_m\|Tv\|+2\exp(-20\,4^{m^+}).
}
\tag{2.6}
$$
所有后续修正仍只发生在更高新块中，故 $w-v\perp\mathcal F_L$。
特别，若 $v\perp\mathcal F_j$ 且 $j\le m$，则 $w\perp\mathcal F_j$。

本引理特意没有把任意 $\exp(-c4^m)$ 残差直接写成原有
$\exp(-40\,4^m)$ 残差。首先付 (2.1)，然后用新的实际间隔得到 (2.5)。

## 3. 两个空坐标中的归一化纯核

对相邻坐标 $k=j+1$，定义
$$
\mathcal C_j=
\frac{a_k\mathsf E_j^*-a_j\mathsf E_k^*}
{\sqrt{a_j^2+a_k^2}}.
\tag{3.1}
$$
它只作用这两个坐标，并且
$$
\|\mathcal C_j\|=1.
\tag{3.2}
$$
可直接按两位孔数检查：真空被送到归一化的一孔向量；
一孔空间被一个范数为 1 的行送到双孔空间；
双孔被送到零。两部分初始空间与值域分别正交。

令 $P_{00}^{j,k}$ 投影到这两位都为真空的空间，则
$$
\|\mathcal C_jx\|=\|x\|\quad
(x=P_{00}^{j,k}x).
\tag{3.3}
$$
同时，对这样的 $x$，
$$
(a_j\mathsf E_j+a_k\mathsf E_k)\mathcal C_jx=0,\qquad
(a_j\mathsf E_j+a_k\mathsf E_k)x=0.
\tag{3.4}
$$
第一式的真空系数是
$(a_ja_k-a_ka_j)/\sqrt{a_j^2+a_k^2}=0$。

对每个固定 $x\in\mathcal H_-$，有
$P_{00}^{j,j+1}x\to x$：
先对有限头向量检查，再用投影范数为 1 与有限头稠密延拓。
结合 (3.2)—(3.3) 得
$$
\boxed{\|\mathcal C_jx\|\longrightarrow\|x\|.}
\tag{3.5}
$$
这里没有声称 $\mathcal C_jx$ 强收敛。

## 4. 真进位与 Cayley 逆的全部交换子误差

若 $i<j$，实际有限链分解为
$$
\mathsf N_i=\mathsf N_i^{[j]}
+\frac{\alpha_j}{\alpha_i}
(\mathsf E_i^*\cdots\mathsf E_{j-1}^*)\mathsf N_j.
\tag{4.1}
$$
其中有限链与乘积前缀都只作用第 $j$ 位以下，因而与 $\mathcal C_j$ 交换。
所以
$$
\|[\mathsf N_i,\mathcal C_j]\|
\le2\frac{\alpha_j}{\alpha_i}.
\tag{4.2}
$$
对 $i>j+1$，$\mathsf N_i$ 只作用第 $i$ 位及更高位，故交换子严格为零。

对 Cayley 因子，真实逆差给
$$
[\mathsf Y_i,\mathcal C_j]
=(I+\mathsf N_i)^{-1}
[\mathsf N_i,\mathcal C_j]
(I+\mathsf N_i)^{-1}.
\tag{4.3}
$$
所以 $i<j$ 时范数至多 $18\alpha_j/\alpha_i$；
$i>j+1$ 时仍严格为零。

现在取 $x=P_{00}^{j,j+1}x$。
第 $j,j+1$ 两项的纯交换子之和由 (3.4) 恰为零。
用 (1.2)，实际两项相对纯项的交换子误差对 $T_N$ 至多
$2(a_j\eta_j+a_{j+1}\eta_{j+1})\|x\|$，
对 $T_Y$ 至多
$8(a_j\eta_j+a_{j+1}\eta_{j+1})\|x\|$。

由于 $\alpha_j/\alpha_i\le\eta_{j-1}$ 对 $i<j$ 成立，合并得到
$$
\|[T_N,\mathcal C_j]x\|
\le4A_0\eta_{j-1}\|x\|,
$$
$$
\|[T_Y,\mathcal C_j]x\|
\le26A_0\eta_{j-1}\|x\|.
$$
统一放宽为
$$
\boxed{
\|[T,\mathcal C_j]x\|
\le64\eta_{j-1}\|x\|
\qquad(x=P_{00}^{j,j+1}x).
}
\tag{4.4}
$$
低位项始终用真正的 $\alpha_j/\alpha_i$，而非固定低位的全空间 $\eta_i$。
两种模型都已经支付完所有索引；没有未计入的高尾项。

## 5. 在每一最新空间隔中复制并修复

对 (1.3)—(1.5) 的第 $n+1$ 个有限近似，简记
$$
m=m_{n+1}=2L_n,\qquad
j_n=L_n-2,\qquad k_n=L_n-1.
\tag{5.1}
$$
因 $L_n=64\,2^{m_n}$，这两个位都属于
$[m_n,L_n)$，所以 $g_{n+1}$ 在它们上确为真空。
令
$$
v_n=\mathcal C_{j_n}g_{n+1}.
\tag{5.2}
$$
则 $v_n\in\mathcal F_m$、$\|v_n\|=\|g_{n+1}\|<3/2$，
并且 $v_n\perp\mathcal F_{j_n}$。

由 (1.3)、(4.4)，
$$
\|Tv_n\|
\le\epsilon_m+96\eta_{L_n-3}.
$$
置
$$
c_0=\frac{770}{4096}>0.
$$
因为 $4^m=16^{L_n}$，
$$
\eta_{L_n-3}\le
\exp(-770\,16^{L_n-3})
=\exp(-c_0\,4^m).
$$
所以
$$
\boxed{\|Tv_n\|\le100\exp(-c_0\,4^m).}
\tag{5.3}
$$

这个常数 $c_0$ 小于 40，因此不能直接套原标准预算。
但
$$
\mathcal A_m\|Tv_n\|
\le100\exp(8m2^m-c_0\,4^m)
\longrightarrow0.
\tag{5.4}
$$
这是因为 $m2^m=o(4^m)$。
故对充分大的 $n$，(2.4) 成立，实际修复引理给
$$
w_n\in M,\qquad
\|w_n-v_n\|\longrightarrow0,\qquad
w_n\perp\mathcal F_{j_n}.
\tag{5.5}
$$
最后一式使用修正保头，不能仅由范数误差替代。
由于 $j_n\to\infty$、$\{w_n\}$ 有界，有限头稠密性给
$$
\boxed{w_n\rightharpoonup0,\qquad
\|w_n\|\longrightarrow\|g\|>0.}
\tag{5.6}
$$
每个 $w_n$ 都是真实算子 $T$ 的精确核向量，而不是仅有小残差的向量。

## 6. 同一序列保留每个固定 UHF 算子的作用范数

令 $\mathfrak U_-$ 为此边界表示中的 UHF 代数，即有限位矩阵
$E_{\rm fin}\otimes I$ 的算子范数闭包。
对固定 $E\in\mathfrak U_-$，
$$
\|[E,\mathcal C_{j_n}]\|\longrightarrow0.
\tag{6.1}
$$
证明：给定任意 $\varepsilon>0$，先用有限位算子 $E_{\rm fin}$ 满足
$\|E-E_{\rm fin}\|<\varepsilon$；当 $j_n$ 超过它的全部坐标，
$[E_{\rm fin},\mathcal C_{j_n}]=0$，从而交换子范数至多 $2\varepsilon$。

结合 (5.5)、$g_{n+1}\to g$，得到
$$
\begin{aligned}
\|Ew_n-\mathcal C_{j_n}Eg\|
&\le\|E\|\,\|w_n-\mathcal C_{j_n}g_{n+1}\|\\
&\quad+\|[E,\mathcal C_{j_n}]\|\,\|g_{n+1}\|\\
&\quad+\|E\|\,\|g_{n+1}-g\|\longrightarrow0.
\end{aligned}
$$
最后使用 (3.5)：
$$
\boxed{
\|Ew_n\|\longrightarrow\|Eg\|
\quad\text{对每个固定 }E\in\mathfrak U_-.
}
\tag{6.2}
$$
序列 $w_n$ 本身不依赖 $E$。
这里是对每个固定算子的结论，不声称在整个 UHF 单位球上一致。

对任意紧算子 $K:M\to\mathcal H_-$，由 (5.6) 有 $Kw_n\to0$。
所以
$$
\boxed{
\|E|_M\|_{\rm ess}\ge
\frac{\|Eg\|}{\|g\|}.
}
\tag{6.3}
$$
无需假设 $E$ 保持 $M$；如果它保持 $M$，也可在 $B(M)$ 中解释此本质范数下界。
不把 (6.3) 提升为整个 $M$ 上的本质范数等式，因为本稿没有证明任意
$M$ 向量都属于本节的构造类。

## 7. 核、稳定闭像部分和稳定子商的全部幂非紧

取 R185 或 R188 的明确非真空核向量 $g$。
这些结果已经证明 $g$ 的物理整数支持无限：
否则 $g$ 落入有限头，而有限头中 $\ker T=\mathbb Ce_0$，
与构造保留的两个非真空系数矛盾。
因此
$$
B^rg\ne0\qquad(r\ge1).
$$
实际 $B\in\mathfrak U_-$，所以对 $E=B^r$ 应用 (6.2)—(6.3)：
$$
\boxed{
(B|_M)^r\text{ 对每个 }r\ge1\text{ 都非紧}.
}
\tag{7.1}
$$

同样，令 $N=\overline{BM}$，取 $x_n=Bw_n\in N$。
它弱趋零，且
$$
\|x_n\|\to\|Bg\|>0,\qquad
\|B^rx_n\|\to\|B^{r+1}g\|>0.
$$
故 $(B|_N)^r$ 对每个 $r\ge1$ 也非紧。

R187 已证明 $\mathbb Ce_0\subseteq N$，
以及 $C=B_{N/\mathbb Ce_0}$ 单射、值域稠密、拟幂零。
在这个商中，$x_n+\mathbb Ce_0$ 弱趋零。
因为固定一维投影把弱零序列送到强零，
$$
\|x_n+\mathbb Ce_0\|\to\|Bg\|,\qquad
\|C^r(x_n+\mathbb Ce_0)\|\to\|B^{r+1}g\|>0.
$$
所以这个具体稳定子商上的 $C^r$ 也全部非紧。

这些结论只排除了以本模型的紧性作为额外输入的途径。
它们没有证明或否定 $N=M$，没有排除 $B|_M$ 的一般紧交换子，
也没有构造通往原 Haar 表示的有界或可闭交织。


## 8. 高位生成元在整个核上的范数和数值半径

两种具体核还保留每个充分高的单个位生成元的完整极限大小：
$$
\boxed{
\|\mathsf N_j|_M\|\longrightarrow1,\qquad
w(\mathsf N_j|_M)\longrightarrow\frac12.
}
\tag{8.1}
$$
这里 $w$ 是通常 Hilbert 空间数值半径。
$\mathsf N_j$ 为 $B$ 的多项式，因而保持 $M$；
(8.1) 的数值半径指其在 $M$ 上的真正限制。

### 8.1. 纯一孔核中第 $j$ 个坐标趋于 1

对 $j\ge1$，置
$$
\sigma_j^2=\sum_{k=j+1}^{2j}a_k^2,\qquad
u_j=
\frac{\displaystyle
\sigma_j e_{2^j}-\frac{a_j}{\sigma_j}
\sum_{k=j+1}^{2j}a_k e_{2^k}}
{\sqrt{\sigma_j^2+a_j^2}}.
\tag{8.2}
$$
直接计算得
$$
\|u_j\|=1,\qquad
\sum_i a_i\mathsf E_i u_j=0,\qquad
u_j\in\mathcal F_{2j+1},\qquad
u_j\perp\mathcal F_j.
\tag{8.3}
$$
因为
$$
\sigma_j^2\ge\frac{j}{(2j+1)^4},\qquad
a_j^2=(j+1)^{-4},
$$
有
$$
\frac{a_j^2}{\sigma_j^2}
\le\frac{(2j+1)^4}{j(j+1)^4}\longrightarrow0.
$$
所以第 $j$ 位系数
$$
c_j:=\frac{\sigma_j}{\sqrt{\sigma_j^2+a_j^2}}
\longrightarrow1,\qquad
\mathsf E_j u_j=c_je_0.
\tag{8.4}
$$

### 8.2. 真残差和首次修复

$u_j$ 的第 $0,\ldots,j-1$ 位全真空。
对 $i<j$，实际链展开到第 $j$ 位时，有限链的各项都严格杀掉输入；
故
$$
\|\mathsf N_i u_j\|\le\alpha_j/\alpha_i.
$$
Cayley 项把逆置于左边，得到
$\|\mathsf Y_i u_j\|\le3\alpha_j/\alpha_i$。
对 $i\ge j$，使用 (1.2) 与纯核恒等式 (8.3)，得
$$
\|T_Nu_j\|\le2A_0\eta_{j-1},\qquad
\|T_Yu_j\|\le7A_0\eta_{j-1}.
$$
统一放宽为
$$
\|Tu_j\|\le14\eta_{j-1}.
\tag{8.5}
$$
高于 $2j$ 的实际和纯项都严格杀掉 $u_j$，亦可逐项略去；使用上面的总和界同样合法。

令 $m=2j+1$。修复前的首步代价满足
$$
\mathcal A_m\|Tu_j\|
\le14\exp\bigl(8(2j+1)2^{2j+1}-770\,16^{j-1}\bigr)
\longrightarrow0.
\tag{8.6}
$$
因为正项是 $O(j4^j)$，负项的量级是 $16^j$。
因此对充分大的 $j$，§2 的较弱首步修复适用。
它给出精确核向量
$$
z_j\in M,\qquad
\|z_j-u_j\|\longrightarrow0,\qquad
z_j\perp\mathcal F_j.
\tag{8.7}
$$
特别 $z_j\perp e_0$、$\|z_j\|\to1$。
该保头性质来自整个实际修正的高位支持，不能仅从范数趋近推得精确正交。

由 (1.2)、(8.4)、(8.7)，
$$
\|\mathsf N_jz_j-e_0\|
\le\|z_j-u_j\|+\eta_j+|c_j-1|
\longrightarrow0.
\tag{8.8}
$$
因为全空间 $\|\mathsf N_j\|\le1$，(8.8) 已证明 (8.1) 的范数结论。

### 8.3. 由真空与一孔向量的相干叠加取得数值半径

只用 $z_j$ 本身并不能给所需数值半径下界。
应取
$$
x_j=\frac{e_0+z_j}{\sqrt{1+\|z_j\|^2}}\in M,\qquad
\|x_j\|=1.
\tag{8.9}
$$
这里 $e_0\in M$、$z_j\perp e_0$，且 $\mathsf N_je_0=0$。
因此
$$
\langle\mathsf N_jx_j,x_j\rangle
=
\frac{\langle\mathsf N_jz_j,e_0\rangle
+\langle\mathsf N_jz_j,z_j\rangle}
{1+\|z_j\|^2}
\longrightarrow\frac12.
\tag{8.10}
$$
第一项由 (8.8) 趋于 1；
第二项因 $\mathsf N_jz_j=e_0+o(1)$、$z_j\perp e_0$ 及 $z_j$ 有界而趋于 0。
这给限制数值半径的下界。

上界必须作用于整个 $M$，而非仅上述两维向量族。
由全空间比较与数值半径的 Lipschitz 性，
$$
w(\mathsf N_j|_M)
\le w(\mathsf N_j)
\le w(\mathsf E_j)+\|\mathsf N_j-\mathsf E_j\|
\le\frac12+\eta_j.
\tag{8.11}
$$
纯一位消灭矩阵的数值半径为 $1/2$。
(8.10)—(8.11) 证明 (8.1) 的第二式。

### 8.4. 范数商中高位生成元不会变小

分别令原范数代数中的慢符号为 $S_N$、$S_Y$，
并置 $J=\overline{S\mathcal A}$。
边界表示在 $M=\ker\pi_-(S)$ 上的限制为一个收缩含幺表示，
且把 $J$ 送到零。因此
$$
1\ge\operatorname{dist}_{\mathcal A}(N_j,J)
\ge\|\mathsf N_j|_M\|\longrightarrow1.
$$
故
$$
\boxed{\operatorname{dist}_{\mathcal A}(N_j,J)\longrightarrow1.}
\tag{8.12}
$$
每个 $x_j$ 还给边界的正正常向量态
$\varphi_j(T)=\langle\pi_-(T)x_j,x_j\rangle$，
它准确湮灭 $J$，并满足 $\varphi_j(N_j)\to1/2$。

这不构成 $N_j+J$ 在 Banach 商中不弱趋零的证明：
这里的状态 $\varphi_j$ 随 $j$ 改变，不能代替一个固定的连续线性泛函。
(8.12) 排除的是范数趋零，而非弱趋零。
本节也没有将 (8.1) 自动转移到稳定子商 $N/\mathbb Ce_0$；
其中核修复向量是否属于 $N$，仍涉及未完成的内部饱和。
