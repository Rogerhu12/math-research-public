# R271 附录：有限异权与原连续尾的相邻高度常数完全归约

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。
状态：已证明；Astra-ISP-1cf8c51d 与 boundary_resume_1cf 全文独立复核。本稿不证明常数4或任何新的统一上界。
新增的是：原连续尾在任意足够高出生区的最坏相邻常数，与所有合法有限正异权 Boolean 模型的普遍最坏常数相同。压缩与逆始终按真实 Schur 补处理。

## 1. 同一个 primitive 上的实际最小逆

对有限正权列 $b=(b_1,\ldots,b_n)$，在正交 Boolean 占据基上令
$$
D_b=\sum_{i=1}^n b_iE_i,\qquad b_i>0.
$$
$\mathcal H_p$ 表示 $p$ 孔层。固定高度 $h\ge2$ 和出生数 $s\ge0$，要求
$$
n\ge2s+h.
\tag{1.1}
$$
记
$$
K_s=\ker D_b\cap\mathcal H_s,\qquad
E_{r,p}=\ker D_b^r\cap\mathcal H_p,\qquad
U_{r,p}=E_{r,p}\ominus E_{r-1,p}.
$$
对 $0\le j\le h$，令
$$
J_{j,s}:K_s\longrightarrow U_{j+1,s+j}
$$
是 $D_b^j$ 的真正最小范数逆，约定 $J_{0,s}=I_{K_s}$。置
$$
H_{j,s}=J_{j,s}^*J_{j,s},\qquad H_{0,s}=I_{K_s}.
\tag{1.2}
$$

这些逆确在整个 $K_s$ 上有定义。令 $S_be_I=(\prod_{i\in I}b_i)e_I$；则
$D_b=S_b^{-1}D_{\bf1}S_b$，所以各层幂的秩不变。等权关系
$[D_{\bf1},D_{\bf1}^*]=nI-2N$ 给标准有限梯：
若 $D_{\bf1}f=0$、$f\in\mathcal H_r$，则
$$
D_{\bf1}(D_{\bf1}^*)^\ell f
=\ell(n-2r-\ell+1)(D_{\bf1}^*)^{\ell-1}f.
$$
按孔数归纳作正交梯分解，(1.1) 保证每条到 $\mathcal H_s$ 的梯都延伸到 $\mathcal H_{s+j}$，$j\le h$。故
$$
D_b^j:\mathcal H_{s+j}\longrightarrow\mathcal H_s
$$
满射。其全空间最小逆作用于 $K_s$ 后又满足 $D_b^{j+1}J_{j,s}=0$，因此恰落在显示的 $U_{j+1,s+j}$。
全部 $H_{j,s}$ 是有限维正定算子。

令
$$
A_{r,p}=P_{U_{r-1,p-1}}D_b|_{U_{r,p}}
$$
为实际第一下降块。它是有界双射，并且
$$
A_{r,p}J_{r-1,p-r+1}=J_{r-2,p-r+1}.
\tag{1.3}
$$
证明只需再作用 $D_b^{r-2}$，其余低高度项被杀掉，然后用最小逆的唯一性；不要求删掉第二下降。

定义真实相邻最优常数
$$
\mathsf C_h(D_b;s)
=\inf\left\{C\ge0:
A_{h+1,s+h}A_{h+1,s+h}^*
\le C A_{h,s+h-1}^*A_{h,s+h-1}\right\}.
\tag{1.4}
$$
由 (1.3) 作实际有界可逆同余，准确等价于
$$
\boxed{
C H_{h,s}\ge
H_{h-1,s}H_{h-2,s}^{-1}H_{h-1,s}.
}
\tag{1.5}
$$
例如 $h=2$ 是 $C H_{2,s}\ge H_{1,s}^2$，等价于
$\|H_{1,s}H_{2,s}^{-1}H_{1,s}\|\le C$。
这里每个 $H_j$ 都先取整个实际幂的最小逆，再限制到同一个 primitive；没有以环境 Gram 的压缩之逆替换它。

令
$$
\boxed{
\mathsf C_h^{\rm fin}
=\sup_{\substack{s\ge0,\ n\ge2s+h\\ b_1,\ldots,b_n>0}}
\mathsf C_h(D_b;s)\in(0,\infty].
}
\tag{1.6}
$$
共同缩放全部 $b_i$ 不改变这个常数：$H_j$ 缩放为同一几何因子 $\lambda^{-2j}H_j$，(1.5) 两边因子相同。

## 2. 原连续尾及主归约

保留原物理尾
$$
D_m=\sum_{j\ge m}b_jE_j,\qquad b_j=(j+1)^{-2},\qquad m\ge5.
\tag{2.1}
$$
其所有固定孔层上的 $D_m^j$ 均满射且有有界右逆；下一节给同时适用于截断的完整证明。
所以 (1.2)—(1.5) 对这个原尾及每个固定 $s,h$ 也有定义。记
$$
\mathsf C_h^{\rm tail}(m,s)=\mathsf C_h(D_m;s).
$$

**定理。** 对每个固定 $h\ge2$，有
$$
\boxed{\mathsf C_h^{\rm tail}(m,s)\le \mathsf C_h^{\rm fin}
\qquad(m\ge5,\ s\ge0),}
\tag{2.2}
$$
以及
$$
\boxed{
\liminf_{m\to\infty}\ 
\inf_{\substack{s\in\mathbb N_0\\s\ge4\cdot2^m}}
\mathsf C_h^{\rm tail}(m,s)
\ge \mathsf C_h^{\rm fin}.
}
\tag{2.3}
$$
如果 $\mathsf C_h^{\rm fin}<\infty$，因此上述下确界实际收敛到
$\mathsf C_h^{\rm fin}$。若右边为无穷，(2.3) 指：给定任何有限阈值 $L$，充分大 $m$ 后，全部 $s\ge4\cdot2^m$ 都有 $\mathsf C_h^{\rm tail}(m,s)>L$。

不声称每个固定 $m,s$ 都等于普遍最坏值。
特别，有限异权模型中的任何新上界都能传给原尾；
任何有限异权反例也会在原尾全部充分高出生层出现。
这不是把原尾替换成一个有限模型，而是证明两方向的真实域、投影和能量传递。

## 3. 固定孔层的共同右逆与截断核投影收敛

固定 $m$ 和一个有限孔数预算 $p_*$。
令
$$
D_{m,N}=\sum_{m\le j<N}b_jE_j
$$
作用在整个原尾 Hilbert 空间；$j\ge N$ 的位仍存在，但该截断不删除它们。
因为 $\sum_{j\ge m}b_j<\infty$，
$$
\|D_{m,N}-D_m\|\le\sum_{j\ge N}b_j\longrightarrow0.
\tag{3.1}
$$

选一个固定有限块 $I=[J,2J)$，$J\ge m$，且 $J$ 充分大于 $p_*$。
置 $D_I=\sum_{j\in I}b_jE_j$、$S_I=\sum_{j\in I}b_j^2$。
在 $I$ 中至多 $p_*$ 个孔的所有层上，
$$
D_ID_I^*=D_I^*D_I+S_I I-2\sum_{j\in I}b_j^2n_j
\ge a_I I,
$$
$$
a_I:=S_I-2p_*\max_{j\in I}b_j^2>0.
\tag{3.2}
$$
存在这样的 $J$，因为
$S_I\ge J(2J+1)^{-4}$，而第二项至多 $2p_*(J+1)^{-4}$。

于是 $R_I=D_I^*(D_ID_I^*)^{-1}$ 是在这些层上同时定义的右逆，
$\|R_I\|\le a_I^{-1/2}$；它只改变 $I$ 位，并保留 $I^c$ 的孔数。
对 $N\ge2J$，写 $D_{m,N}=D_I+D_{I^c,N}$。
$D_{I^c,N}$ 与 $R_I$ 真正交换。对总孔数至多 $p_*$ 的输入，
$R_ID_{I^c,N}$ 每次降低一个 $I^c$ 孔，故其 $(p_*+1)$ 次幂为零。
因此
$$
\boxed{
R_N=R_I\sum_{\ell=0}^{p_*}(-R_ID_{I^c,N})^\ell,\qquad
D_{m,N}R_N=I.
}
\tag{3.3}
$$
所有中间输入仍在 (3.2) 允许的层内。
范数统一满足
$$
\|R_N\|
\le a_I^{-1/2}
\sum_{\ell=0}^{p_*}
\left(a_I^{-1/2}\sum_{j\ge m}b_j\right)^\ell.
\tag{3.4}
$$
右端与 $N$ 无关。将外部截断换成完整 $D_{I^c}$，同一个有限 Neumann 公式也给 $D_m$ 的右逆。

逐层复合 (3.3)，在固定孔数和固定幂数范围内得到 $D_{m,N}^j$ 与 $D_m^j$ 的共同满射常数。
所以对每个固定目标层，正算子
$$
D_{m,N}^j(D_{m,N}^*)^j
$$
都有同一个正下界，且由 (3.1) 按范数收敛。其逆遂按范数收敛。

特别，各固定层中的真实核投影
$$
P_{\ker D_{m,N}^j}
=I-(D_{m,N}^*)^j
[D_{m,N}^j(D_{m,N}^*)^j]^{-1}D_{m,N}^j
\tag{3.5}
$$
按范数趋于原尾的相应投影。
若目标层为负，幂为零、投影为 $I$，另行按此约定处理。
这一步依赖 (3.2)—(3.4) 的共同正 gap，不是一般的“核投影自动连续”。

对固定源层 $\mathcal H_s$，令 $P_N=P_{\ker D_{m,N}\cap\mathcal H_s}$，
$P=P_{\ker D_m\cap\mathcal H_s}$，$s=0$ 时两者都是 $I$。
将最小逆暂延为整个源层上的有界算子：
$$
J_{j,N}=(D_{m,N}^*)^j
[D_{m,N}^j(D_{m,N}^*)^j]^{-1}P_N,\qquad J_{0,N}=P_N.
\tag{3.6}
$$
(3.5)—(3.6) 给
$$
J_{j,N}\to J_j,\qquad H_{j,N}=J_{j,N}^*J_{j,N}\to H_j
\quad\text{按算子范数}.
\tag{3.7}
$$
在 primitive 上这些就是 (1.2) 的实际最小逆 Gram；在其正交补上为零。

## 4. 从所有有限模型传到每个固定原尾

若 $\mathsf C_h^{\rm fin}=\infty$，(2.2) 无需证明。以下假设其有限，并记 $C=\mathsf C_h^{\rm fin}$。

取固定 $m,s$，令截断活跃位数 $N-m\ge2s+h$。
按截断外的孔数 $q$ 分解源层，$0\le q\le s$。每个块的活跃出生数是 $s-q$，所以
$$
N-m\ge2(s-q)+h.
$$
每一块都是合法有限正异权模型，乘上未被截断删除的外部孔层恒等因子。
因而 (1.5) 在每个块成立，并且对整个原源层可写为
$$
\boxed{
\begin{pmatrix}
C H_{h,N}&H_{h-1,N}\\
H_{h-1,N}&H_{h-2,N}
\end{pmatrix}\ge0.
}
\tag{4.1}
$$
每个 $H_{j,N}$ 的共同支撑是 $P_N$；在 $P_N^\perp$ 上此块矩阵为零。
没有漏掉截断之外的占据数。

由 (3.7)，(4.1) 的范数极限仍为正块。
限制到原 $K_s$，$H_{h-2}$ 为真实正定有界单位，Schur 补给
$$
C H_h\ge H_{h-1}H_{h-2}^{-1}H_{h-1}.
$$
这就是 (2.2)。

## 5. 任意固定有限权模型的真实活跃位与同一个暗背景

现在固定任意满足 (1.1) 的有限模型 $b=(b_1,\ldots,b_n)$、出生数 $s_0$。
利用共同缩放及排序，只为记号方便令
$$
1=b_1\ge b_2\ge\cdots\ge b_n>0.
$$
排序只用于指定有限目标权，不改原连续尾的物理次序。

对充分大 $m$，选严格递增的实际活跃位 $j_1(m),\ldots,j_n(m)$，满足
$$
j_1(m)=m,\qquad
j_i(m)\equiv m+i-1\pmod2,\qquad
\frac{j_i(m)+1}{m+1}\longrightarrow b_i^{-1/2}.
\tag{5.1}
$$
不同目标权给相距 $O(m)$ 的位置；重复目标权可用相邻或相隔固定偶数的位置。每个固定目标位置只需 $O(1)$ 的整数与奇偶修正，所以 (5.1) 可同时实现。
各活跃间隙的未选位数都是偶数。

将原尾归一化为
$$
\widehat D_m=b_m^{-1}D_m,\qquad b_m=(m+1)^{-2}.
$$
其活跃权
$$
b_i^{(m)}=\frac{b_{j_i(m)}}{b_m}
=\left(\frac{m+1}{j_i(m)+1}\right)^2\longrightarrow b_i.
\tag{5.2}
$$

给定任意 $s\ge4\cdot2^m$，令
$$
t=s-s_0,\qquad K=m+n+2t.
\tag{5.3}
$$
充分大 $m$ 时 $t\ge0$ 且 $K>j_n(m)$，一致适用于全部这些 $s$。
按 (5.1)，$K-j_n(m)-1$ 也为偶数。
所以 $[m,K)$ 除活跃位外的全部位置可逐段配成相邻对，恰有 $t$ 对。

对每对 $(j,j+1)$，取真实归一化暗向量
$$
\chi_j=
\frac{b_{j+1}e_j-b_je_{j+1}}{\sqrt{b_j^2+b_{j+1}^2}}.
\tag{5.4}
$$
每个暗对只有一个孔，且其尾删除为零。活跃集以外、$j\ge K$ 的位取真空。
所有这些背景因子的张量积记为 $\chi_{m,s}$，它是单位 $t$ 孔向量，并被背景删除 $D_{\rm bg}$ 杀掉。

这里及以下 $D_{\rm a}$、$D_{\rm bg}$ 均指归一化 $\widehat D_m$ 的活跃和背景部分。
同一背景向量供全部 $0\le j\le h$ 的最小逆使用，不分阶更换源。

## 6. 全部固定高阶的背景误差

每个暗对的上升平方范数为
$$
\frac{(b_j^2-b_{j+1}^2)^2}{b_j^2+b_{j+1}^2},
$$
而真空单个位的上升平方范数是 $b_j^2$。
令归一化后这些平方范数的总和为 $\delta_{m,s}^2$。
由
$$
\frac{(b_j^2-b_{j+1}^2)^2}{b_j^2+b_{j+1}^2}
\le16(j+1)^{-6},
$$
得到
$$
\boxed{
\delta_{m,s}^2
\le \frac{C}{m+1}+\frac{(m+1)^4}{3K^3}
\longrightarrow0
}
\tag{6.1}
$$
一致于全部 $s\ge4\cdot2^m$。

每个背景因子的上升最多作用一次；不同被上升因子集产生正交向量。
因此对每个固定 $\ell\ge0$，准确有
$$
\boxed{
\|(D_{\rm bg}^*)^\ell\chi_{m,s}\|^2
=(\ell!)^2e_\ell(d_\nu^2)
\le \ell!\,\delta_{m,s}^{2\ell}.
}
\tag{6.2}
$$
这里 $d_\nu^2$ 是上述各背景因子的平方上升量。无穷真空尾按平方可和及单调有限截断得到同式。
本式保全部高阶背景，不以一阶小量免费推出高阶小量。

## 7. 同一有限 primitive 子空间的全部 Gram 压缩逼近

在固定有限活跃 Hilbert 空间中，令 $P_{\rm a,m}$、$P_{\rm a}$ 是权 $b^{(m)}$、$b$ 的出生 $s_0$ primitive 投影。
有限满秩和 (5.2) 给
$$
P_{\rm a,m}\longrightarrow P_{\rm a}
\quad\text{按范数}.
$$
若 $s_0=0$，投影恒为 $I$。
令 $K_{\rm a}=\operatorname{Ran}P_{\rm a}$。
充分大 $m$ 时，用实际极分解给等距识别
$$
U_m=P_{\rm a,m}|_{K_{\rm a}}\,
(P_{\rm a}P_{\rm a,m}P_{\rm a}|_{K_{\rm a}})^{-1/2}
:K_{\rm a}\longrightarrow\operatorname{Ran}P_{\rm a,m}.
\tag{7.1}
$$
它按范数趋于自然嵌入。

定义
$$
V_{m,s}f=(U_mf)\otimes\chi_{m,s}.
\tag{7.2}
$$
这是同一个固定有限 primitive 空间到原归一化尾 $K_s(\widehat D_m)$ 的等距映射。
本式只用实际活跃坐标的张量因子，不将任意物理重排当作原算子的等式。

记活跃最小逆 Gram 为 $H_j^{\rm a,m}$。
对 $g\in\operatorname{Ran}P_{\rm a,m}$，置
$$
w_j=[D_{\rm a}^j(D_{\rm a}^*)^j]^{-1}g,\qquad
u_j=(D_{\rm a}^*)^jw_j,\qquad
a_j(g)=\|u_j\|^2=\langle H_j^{\rm a,m}g,g\rangle.
$$
固定有限模型和 $j\le h$ 下，这些映射的范数在充分大 $m$ 时一致有界。

显式原像 $u_j\otimes\chi_{m,s}$ 给真正全尾最小能量的上界 $a_j(g)$。
以 $w_j\otimes\chi_{m,s}$ 为原范数对偶测试，活跃与背景孔数使各项正交，且
$$
\begin{aligned}
\|(\widehat D_m^*)^j(w_j\otimes\chi_{m,s})\|^2
&=a_j(g)\\
&\quad+\sum_{\ell=1}^j\binom j\ell^2
\|(D_{\rm a}^*)^{j-\ell}w_j\|^2
\|(D_{\rm bg}^*)^\ell\chi_{m,s}\|^2\\
&\le a_j(g)+C_j\delta_{m,s}^2\|g\|^2.
\end{aligned}
\tag{7.3}
$$
对任何全尾原像 $v$，有
$\langle v,(\widehat D_m^*)^j(w_j\otimes\chi)\rangle=\langle g,w_j\rangle=a_j(g)$。
Cauchy–Schwarz 因而给下界
$$
\frac{a_j(g)^2}{a_j(g)+C_j\delta_{m,s}^2\|g\|^2}
\ge a_j(g)-C_j\delta_{m,s}^2\|g\|^2.
$$
对 $j=0$ 则两边准确相等。
所以在同一 primitive 子空间上，作为二次型，
$$
H_j^{\rm a,m}-C_j\delta_{m,s}^2I
\le (g\mapsto g\otimes\chi)^* H_j(\widehat D_m;s)
(g\mapsto g\otimes\chi)
\le H_j^{\rm a,m}.
\tag{7.4}
$$

有限活跃满秩还给
$U_m^*H_j^{\rm a,m}U_m\to H_j(D_b;s_0)$。
结合 (6.1)、(7.4)，得到同时覆盖全部固定阶的真正范数极限：
$$
\boxed{
\sup_{s\ge4\cdot2^m}
\left\|V_{m,s}^*H_j(\widehat D_m;s)V_{m,s}
-H_j(D_b;s_0)\right\|\longrightarrow0
\quad(0\le j\le h).
}
\tag{7.5}
$$
没有使用一般核投影连续性来比较全尾与活跃模型；
全尾的压缩逼近是由同一源的显式原像与对偶测试共同证明的。

## 8. 压缩逆必须用 Schur–Jensen 的正确方向

若 $A>0$ 是有界可逆正算子，$B=B^*$ 有界，$V$ 为等距嵌入，则
$$
\begin{pmatrix}A&B\\B&BA^{-1}B\end{pmatrix}\ge0.
$$
用 $\operatorname{diag}(V,V)$ 压缩，再取真正 Schur 补，得到
$$
\boxed{
V^*BA^{-1}BV
\ge (V^*BV)(V^*AV)^{-1}(V^*BV).
}
\tag{8.1}
$$
这不声称压缩与逆交换。

取 $C=\mathsf C_h^{\rm tail}(m,s)$。
全尾的 (1.5) 及 (8.1) 给
$$
C\,V_{m,s}^*H_h(\widehat D_m;s)V_{m,s}
\ge
\bigl(V_{m,s}^*H_{h-1}V_{m,s}\bigr)
\bigl(V_{m,s}^*H_{h-2}V_{m,s}\bigr)^{-1}
\bigl(V_{m,s}^*H_{h-1}V_{m,s}\bigr).
\tag{8.2}
$$
共同归一化 $\widehat D_m=b_m^{-1}D_m$ 不改变 $C$。

有限维正定三元组的最优常数是连续函数，例如
$$
\mathcal C(A_-,A_0,A_+)
=\left\|A_+^{-1/2}A_0A_-^{-1/2}\right\|^2.
\tag{8.3}
$$
(7.5) 使 (8.2) 右侧与左侧压缩在全部 $s$ 上一致趋于固定有限模型的三元组。
故
$$
\liminf_{m\to\infty}\inf_{s\ge4\cdot2^m}
\mathsf C_h^{\rm tail}(m,s)
\ge \mathsf C_h(D_b;s_0).
\tag{8.4}
$$
对全部合法有限模型取上确界，就是 (2.3)。
若 (1.6) 为无穷，对每个有限阈值选一个更大的有限模型常数再使用 (8.4)，量词仍然成立。

## 9. 对当前相邻上界任务的准确意义

本稿不提高已知下界，也不把完整 Hankel 正性重新列为可用猜想。
此前两簇及暗对稿已给
$$
\mathsf C_h^{\rm fin}\ge\left(\frac h{h-1}\right)^2,
$$
特别高度2至少需要4。0c 的七位精确例还排除了过强的额外有限维因子；这些已证范围不重新计作新增。

新归约说明：只利用原 $b_j=(j+1)^{-2}$ 的连续正则性，不可能在其高出生区得到一个严格小于所有有限异权最坏值的相邻常数。
反之，任意真正与有限出生数、位数、正权型无关的 $C_h$，一经有限模型证明，就完整适用于原连续尾的每个固定层。
若仅求温和增长而非最优常数，例如 $\log C_h=O(h\log h)$，也是同一个准确归约。

结论不支付原边界 Schur 逆之间的未知源匹配，不扩大有限核提升窗口，也不把整个 $D$ 的环境不等式代替实际第一下降。
无权 $N=M$ 与普通 Hilbert ISP 仍未完成。

## 10. 依赖

- [R271 两簇全高度稿](R271-appendix-two-cluster-minimal-inverses-and-squared-all-height-comparison-lower-bounds.md)：真实最小逆 Gram、固定高阶暗背景及已证平方下界。
- [R271 原连续尾暗对稿](R271-appendix-dark-pair-transfer-and-continuous-tail-adjacent-descent-counterexample.md)：相邻物理暗对的真实源、原尾范围与实际正交层。
- [R271 占据交换子稿](R271-appendix-occupation-commutator-known-source-minimum-energy.md)：原孔层与第一／第二下降的准确区分。
- [R239 七位反例](R239-appendix-seven-site-counterexample-to-refined-primitive-gram-comparison.md)：已排除的过强有限维因子；不反较弱的普遍相邻猜想。

本稿自足支付共同截断正 gap、任意有限活跃权的奇偶嵌入、同一有限 primitive 空间的全阶压缩及逆的正确 Schur 方向。