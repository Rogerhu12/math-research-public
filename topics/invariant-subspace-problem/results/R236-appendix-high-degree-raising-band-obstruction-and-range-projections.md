# R236 附录：高次提升带的弱极限障碍与像投影的强极限

日期：2026-11-13（UTC）。作者：central_next；AI-assisted，GPT-6 Astra Pro。
状态：已证明。本文只刻画一种明确的高位提升机制，
不宣称普通 ISP 或全部可能的反射方法受到不可能性定理限制。

本文针对 [R264](../results/R264-square-window-weak-averages-and-rearranged-geometric-bell-kernels.md)、[R266](../results/R266-all-multiplicities-for-rearranged-exponential-rows-and-logarithmic-resolvents.md) 及 R236 全重数附录的尾部平均机制；不重新定义这些定理的范围。

## 1. 原实际有限位、占据数与参考向量

在原 Haar 空间 $H=L^2(\mathbb Z_2)$ 中，
取任意有限实际位集 $I$，$|I|=Q$。
在已知的物理位矩阵表示中，
$E_j=e_{10}$ 将第 $j$ 位由 0 提升到 1；
这只是计算已知有限局部算子，不移动任何未知子空间。

令 $P_k$ 为选中位恰有 $k$ 个 1 的正交投影；
其余物理坐标不受投影限制。
常数函数在这些位上的因子是
$$
\Omega_I=2^{-Q/2}(e_0+e_1)^{\otimes Q}.
$$
所以
$$
\|P_k\Omega_I\|^2=2^{-Q}\binom Qk.
\tag{1.1}
$$
对不依赖所选位的有限柱向量 $v$，同样有
$\|P_kv\|^2=2^{-Q}\binom Qk\|v\|^2$。

称有界算子 $B$ 至少提升 $r$ 层，是指
$$
\boxed{
P_iBP_j=0\quad\text{当 }i<j+r,
\qquad 1\le r\le Q.
}
\tag{1.2}
$$
$B$ 可以有作用于未选坐标的系数；
只要求这个准确的占据数块条件。
所有只含总次数至少 $r$ 的平方自由 $E_j$ 单项式的多项式
都满足 (1.2)，即使其系数依赖 $Q$ 或幅度。
如果存在非零降阶项或对角项，则不得自动使用本结论。

## 2. 定量提升带定理

**定理。** 若 (1.2) 成立，而 $v,z$ 都不依赖选中的 $Q$ 位，则
$$
\boxed{
|\langle Bv,z\rangle|
\le2\|B\|\exp\left(-\frac{r^2}{4Q}\right)\|v\|\|z\|.
}
\tag{2.1}
$$

**证明。**
置
$$
m=\left\lceil\frac{Q-r}{2}\right\rceil,\qquad
P_{<m}=\sum_{k<m}P_k,\qquad
P_{\ge m+r}=\sum_{k\ge m+r}P_k.
$$
由 (1.2)，$B(I-P_{<m})$ 的像在 $P_{\ge m+r}H$ 中。
因此
$$
\begin{aligned}
|\langle Bv,z\rangle|
&\le\|B\|\big(
 \|P_{<m}v\|\,\|z\|
 +\|v\|\,\|P_{\ge m+r}z\|\big).
\end{aligned}
\tag{2.2}
$$

令 $K$ 服从 $\operatorname{Bin}(Q,1/2)$。
由 $\cosh x\le e^{x^2/2}$，
$$
\mathbb E e^{t(K-Q/2)}
=(\cosh(t/2))^Q\le e^{Qt^2/8}.
$$
对 $s\ge0$，Markov 不等式后取 $t=4s/Q$ 给
$$
\mathbb P(K-Q/2\ge s)\le e^{-2s^2/Q};
$$
对称性给相同的下尾界。
$m$ 的取整方向确保
$$
K<m\ \Longrightarrow\ K-Q/2\le-r/2,\qquad
K\ge m+r\ \Longrightarrow\ K-Q/2\ge r/2.
$$
故 (1.1) 给
$$
\|P_{<m}v\|\le e^{-r^2/(4Q)}\|v\|,\qquad
\|P_{\ge m+r}z\|\le e^{-r^2/(4Q)}\|z\|.
$$
代入 (2.2) 即得。
$r=Q$ 时 $m=0$，第一项直接为零，也包含在证明内。

## 3. 任意有孔物理高位上的弱极限后果

设 $I_N$ 是实际有限位集，
$Q_N=|I_N|\to\infty$、$\min I_N\to\infty$。
若 $B_N$ 相对 $I_N$ 至少提升 $r_N$ 层，并且
$$
\sup_N\|B_N\|<\infty,\qquad
r_N^2/Q_N\longrightarrow\infty,
$$
则
$$
\boxed{B_N\rightharpoonup0\quad\text{于 }B(H).}
\tag{3.1}
$$
理由是任意固定两个有限柱最终都不依赖所选位，
故 (2.1) 使其配对趋零；
一致范数界和柱向量稠密性再扩展到全 $H$。
同样结论适用于 $B_N+R_N$，若 $\|R_N\|\to0$。

因此，一个统一有界的高位提升主项若要弱趋于
$\lambda I$、$\lambda\ne0$，
其提升阶数不能满足 $r_N/\sqrt{Q_N}\to\infty$。
这不是对任意算子族、任意未知核上的特殊限制
或任意非提升主项的结论。

## 4. 不能免费归一化的具体平均

令
$$
C_I=\frac2Q\sum_{j\in I}E_j,\qquad
a_{Q,r}=\frac{(Q)_r}{Q^r}.
$$
对 $1\le r\le Q$，
$$
\langle C_I^r\Omega_I,\Omega_I\rangle=a_{Q,r}>0.
\tag{4.1}
$$
所以形式归一化
$$
\widetilde C_{Q,r}=a_{Q,r}^{-1}C_I^r
$$
的参考配对恰好为 1。
但它仍满足至少提升 $r$ 层的准确条件。
(2.1) 立即迫
$$
\boxed{
\|\widetilde C_{Q,r}\|
\ge\frac12\exp\left(\frac{r^2}{4Q}\right).
}
\tag{4.2}
$$
因此在 $r/\sqrt Q\to\infty$ 时，
不能通过只检查有限柱配对就声称这个归一化平均弱趋于恒等；
全空间范数已经无界。
弱算子收敛本身会由一致有界原理要求一致范数界。

还能核出其常见中间尺度的准确主增长。
若 $r\to\infty$ 且 $r=o(Q)$，则
$$
\boxed{
\log\|\widetilde C_{Q,r}\|
=\left(\frac12+o(1)\right)\frac{r^2}{Q}.
}
\tag{4.3}
$$
证明如下。令 $S_I=\sum_{j\in I}E_j$，
$u_k$ 是第 $k$ 层的归一化全一向量。
有
$$
S_I^ru_k=
\left(\frac{(k+r)!}{k!}
      \frac{(Q-k)!}{(Q-k-r)!}\right)^{1/2}u_{k+r}.
\tag{4.4}
$$
该层矩阵是规则的有限包含矩阵；
行列和给相同的范数上界，$u_k$ 达到等号。
不同输入层映到不同输出层，故
$$
\|C_I^r\|=
\left(\frac2Q\right)^r
\max_{0\le k\le Q-r}
\left(\frac{(k+r)!}{k!}
      \frac{(Q-k)!}{(Q-k-r)!}\right)^{1/2}.
\tag{4.5}
$$
相邻 $k$ 的平方比为
$$
\frac{(k+r+1)(Q-k-r)}{(k+1)(Q-k)},
$$
所以最大值在距 $(Q-r)/2$ 不超过 $1/2$ 的整数处取得。
逐因子与中心比较，得到
$$
r\log(1+1/Q)-O(r^3/Q^2)
\le\log\|C_I^r\|
\le r\log(1+1/Q).
\tag{4.6}
$$
这里 $r=o(Q)$ 使所有中心比较的相对误差最终小于固定常数。
于是 $\log\|C_I^r\|=o(r^2/Q)$。
另一方面，
$$
\log a_{Q,r}
=\sum_{\ell=0}^{r-1}\log(1-\ell/Q)
=-\frac{r(r-1)}{2Q}+O(r^3/Q^2).
$$
两式相减即得 (4.3)。
(4.2) 对全部 $1\le r\le Q$ 有效，
(4.3) 仅用于明确写出的 $r=o(Q)$ 尺度。

## 5. 一个真正越出提升带的有界强极限

上述定理不排除包含降阶的预处理。
这点可在同一个实际有限位模型中直接展示。

令
$$
P^{\rm ran}_{Q,r}
=\text{到 }\operatorname{Ran}C_I^r\text{ 的正交投影}.
$$
它是已知有限局部矩阵，范数为 1。
由 (4.4)，参考向量的第 $k$ 层分量
在 $k\ge r$ 时属于 $\operatorname{Ran}C_I^r$；
$k<r$ 时与该像正交。
因此
$$
\boxed{
\|(I-P^{\rm ran}_{Q,r})\Omega_I\|^2
=\mathbb P\{\operatorname{Bin}(Q,1/2)<r\}.
}
\tag{5.1}
$$
若固定 $0<\eta<1/2$，并且 $r\le\eta Q$，右侧趋零。
当 $\min I_N\to\infty$ 时，有限柱的张量分解和一致范数界给
$$
\boxed{
P^{\rm ran}_{Q_N,r_N}\longrightarrow I
\quad\text{强算子收敛，甚至允许 }r_N\asymp Q_N.
}
\tag{5.2}
$$
这些投影含有零阶占据数块，不满足 (1.2)，
所以并不与 §3 矛盾。

在有限位空间上，
$$
P^{\rm ran}_{Q,r}=C_I^r(C_I^r)^\dagger
$$
可用真正的 Moore--Penrose 逆写出。
这个逆引入降阶，正是它越出定理假设的原因；
不能把“含降阶”隐去后继续套用纯提升计算。

## 6. 对当前 Bell 排核方法的准确含义

已证明的反射输运等式只对 $f\in M=\ker T$ 给
$$
T^r\mathcal V_N f=C_{I_N}^r f+o(1).
$$
因而下列两种操作仍须另外证明：

- 把 $(C_{I_N}^r)^\dagger f$ 插入右侧输入，
  要求这个实际降阶逆保持未知 $M$，并支付输入误差的增长；
  现有 $M$ 对 $\mathcal A$ 的不变性不蕴含这一点。
- 把降阶逆乘到输出左侧并移入局部测试矩阵，
  会让测试矩阵随 $N$ 增长、涉及所有选中物理位；
  现有“固定局部 $D$”的 $A^r$ 交换子常数不能直接用于它。

§5 展示了一个确实可改变弱平均尺度的有限矩阵机制，
但它进入 Bell 核配对的两个接口尚未关闭。
§§2--4 只证明免费标量归一化以及统一有界的纯高次提升平均
不能替代这些接口，并不证明所有降阶、双边或新实际结构都无效。

普通 ISP 的完成状态不受本笔记改变。
