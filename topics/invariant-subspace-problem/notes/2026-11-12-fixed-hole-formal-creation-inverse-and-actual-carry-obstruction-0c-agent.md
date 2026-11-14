# 固定孔次数的形式 creation 左逆，以及真实 carry 在已控形式类上的障碍

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整引理与反例；不另编号。

本稿先把固定次数的纯 Boolean creation 左逆写成可作用于任意形式系数的有限公式，再说明它怎样处理有限孔次数的实际 $T_N^*$ 输入。最后给一个明确形式数组：它满足此前形式原像已经得到的有限头增长和单高孔块平方可和性，但真实 carry 的第二孔层仍不平方可和。该数组不满足未知缺陷向量的全部方程，不能据此判定实际饱和命题为假。

## 1. 纯 creation 的固定次数完成空间

以有限集合 $S\subset\mathbb N_0$ 标记孔基 $e_S$。记
$$
\mathscr H_q=\ell^2\{S:|S|=q\}.
$$
设 $c=(c_i)\in\ell^2$，且至少有 $2q+1$ 个非零系数。纯 creation 定义为
$$
\mathcal C_c e_S=\sum_{i\notin S}c_i e_{S\cup\{i\}}.
\tag{1.1}
$$
它在固定次数间有界：
$$
\|\mathcal C_c:\mathscr H_q\to\mathscr H_{q+1}\|
\le\sqrt{q+1}\,\|c\|_2.
\tag{1.2}
$$
确实，对每个 $|R|=q+1$，
$$
|(\mathcal C_cu)_R|^2
=\left|\sum_{i\in R}c_i u_{R\setminus\{i\}}\right|^2
\le(q+1)\sum_{i\in R}|c_i|^2|u_{R\setminus\{i\}}|^2,
$$
对 $R$ 求和即得。

对任意形式 $q$ 次数组 $u=(u_S)_{|S|=q}$，即使不假定平方可和，(1.1) 的每个输出坐标仍是有限和。因此纯 creation 也有完全明确的形式意义。

## 2. 一个有限头的加权 Boolean 左界

选定 $r=2q+1$ 个非零系数的位置组成有限集合 $F$，记
$$
\mu=\min_{i\in F}|c_i|>0,\qquad
M_c=\max_{i\in F}|c_i|,\qquad
\beta=\mu^{q+1}/M_c^q.
\tag{2.1}
$$
将 creation 分为
$$
\mathcal C_c=\mathcal C_F+\mathcal C_{F^c}.
$$

先看等权有限头 creation $\mathcal C_{\mathbf1}$ 及其伴随
$\mathcal D_{\mathbf1}$。在头 $k$ 孔空间上，一位矩阵交换子给
$$
\|\mathcal C_{\mathbf1}u\|^2
=\|\mathcal D_{\mathbf1}u\|^2+(r-2k)\|u\|^2.
\tag{2.2}
$$
当 $0\le k\le q$ 时，$r-2k\ge1$。

对角变换
$$
D e_S=\left(\prod_{i\in S}c_i\right)e_S
\quad(S\subset F)
$$
满足 $\mathcal C_F=D\mathcal C_{\mathbf1}D^{-1}$。
在头 $k$ 次空间上，因此有
$$
\|\mathcal C_Fu\|
\ge\frac{\mu^{k+1}}{M_c^k}\|u\|
\ge\beta\|u\|.
\tag{2.3}
$$
这里允许任意复相位；$D$ 只是有限维可逆矩阵，不需要是酉的。

对每个 $k\le q$，取明确的有限维左逆
$$
L_k=(\mathcal C_{F,k}^*\mathcal C_{F,k})^{-1}
\mathcal C_{F,k}^*,
\qquad \|L_k\|\le\beta^{-1}.
$$
把这些块拼成 $L$：头 $k+1$ 次映到头 $k$ 次，头0次映到0，并在外部坐标上张量恒等。
那么在总次数 $q$ 的空间上，
$$
L\mathcal C_F=I.
\tag{2.4}
$$

## 3. 有限 Neumann 公式与形式最大域

置
$$
K=L\mathcal C_{F^c}
\quad\text{作用于总次数 }q.
$$
$\mathcal C_{F^c}$ 增加一个外部孔，而 $L$ 减少一个头孔。
因此 $K$ 保持总次数，每次严格减少头孔数，故
$$
K^{q+1}=0.
\tag{3.1}
$$
又
$$
L\mathcal C_c=I+K.
$$
于是
$$
\boxed{
R_q=\left(\sum_{\nu=0}^q(-K)^\nu\right)L,
\qquad R_q\mathcal C_c=I\ \text{于 }\mathscr H_q.
}
\tag{3.2}
$$
由 (1.2)，
$$
\boxed{
\|R_q\|
\le\beta^{-1}
\sum_{\nu=0}^q
\left(\beta^{-1}\sqrt{q+1}\,\|c_{F^c}\|_2\right)^\nu.
}
\tag{3.3}
$$
所以纯 creation 在每个固定孔次数上有正的统一左界。

这个公式还有一个比单纯 Hilbert 空间下界更直接的用途。
$L$ 只混合有限头的有限个坐标；每个 creation 输出坐标也是有限和。
(3.2) 又只含有限次复合。因此所有恒等式逐坐标成立于任意形式 $q$ 次数组。

**形式域推论。** 若形式 $q$ 次数组 $u$ 满足
$$
\mathcal C_cu\in\mathscr H_{q+1},
$$
则
$$
\boxed{u=R_q(\mathcal C_cu)\in\mathscr H_q.}
\tag{3.4}
$$
这一步没有把“有界左逆”自动延伸到未定义的无限和；真正使用的是 (3.2) 的逐坐标有限公式。

对规范慢列 $c_i=a_i=(i+1)^{-2}$，可选 $F=\{0,\ldots,2q\}$，于是
$$
\beta=(2q+1)^{-2(q+1)}.
$$
常数可能随 $q$ 很快增长；没有声称各次数上有共同下界。

## 4. 实际 $T_N^*$ 对形式有限孔输入的一个完整结论

取真实边界慢模型
$$
T_N=\sum_{i\ge0}a_i\mathsf N_i,\qquad
a_i=(i+1)^{-2}.
$$
每个 $\mathsf N_i^*$ 是加 $2^i$ 的加权前移。
若输入第 $i$ 位没有孔，加法增加一个孔，实际系数恰为1。
若从第 $i$ 位开始有长度 $\ell\ge1$ 的连续孔，则这些孔被清去，并在第 $i+\ell$ 位新增一个孔；孔数净变化为 $1-\ell\le0$。

因此 $T_N^*$ 将孔次数不超过 $q$ 的实际向量送入次数不超过 $q+1$，且对任何形式有限孔数组也有
$$
P_{q+1}T_N^*h=\mathcal C_a h_q
\quad\text{当 }h=h_0+\cdots+h_q.
\tag{4.1}
$$
每个输出行上的真实前移系数只含有限个源，所以 (4.1) 在形式意义下合法。

**命题 4.1。** 若形式序列 $h$ 只含有限个孔次数，且其逐行真实像
$T_N^*h$ 属于 $\mathcal H_-$，则 $h\in\mathcal H_-$。

证明：设最高次数为 $q$。由 (4.1)，
$\mathcal C_a h_q\in\mathscr H_{q+1}$，故 (3.4) 给 $h_q\in\mathscr H_q$。
此时 $T_N^*h_q$ 已是真正有界算子作用得到的 Hilbert 向量。
从给定输出中减去它，剩下的形式输入次数至多 $q-1$，且输出仍在 Hilbert 空间。
有限次下降完成证明。

这个结论暂不自动覆盖 $T_Y^*$：
Cayley 级数中的较高幂可以从一个输入产生许多孔，
所以不存在未经证明的相同“最高 $q+1$ 层”截断。
也不能将命题应用到未知具有无限孔次数的形式原像。

## 5. 已有形式增长和单高孔界不使真实 carry 自动平方可和

下面只构造一个形式数组，用于严格限定当前估计的用途。
令
$$
n_j=2^{8j}+2^j-1\qquad(j\ge2),
$$
并定义
$$
u_{n_j}=\alpha_0/\alpha_j,\qquad
u_n=0\quad(n\ne n_j).
\tag{5.1}
$$
每个 $n_j$ 的孔模式是低 $j$ 位全孔，加上一个极高的第 $8j$ 孔。
其孔数为 $j+1$，所以这个数组具有无限孔次数。

### 5.1. 它符合已得的亚四次有限头增长

实际 $-\log\alpha_j\le100\,16^j$。
若 $n_j<2^m$，则 $8j<m$，从而
$$
\|P_mu\|
\le\sqrt m\,\exp(100\,2^{m/2})
\le A_{m+1}=\exp(8(m+1)2^{m+1})
\tag{5.2}
$$
对全部 $m\ge2$ 成立；$m<17$ 时左侧为0，之后右侧有充分余量。
因此它满足此前形式原像的 $\exp(O(m2^m))$ 型有限头上界。

### 5.2. 它也满足每个固定低头上的单高孔平方可和性

固定 $m$，考察
$$
\sum_{k\ge m+2}\sum_{0\le r<2^m}|u_{2^k+r}|^2.
$$
非零项必须有 $k=8j$ 且 $r=2^j-1<2^m$，所以只能来自 $2\le j\le m$ 的有限集合。
因此该和有限，并且其平方根至多
$$
\sqrt m\,e^{100\,16^m}\le e^{260\,16^m}
\quad(m\ge2).
\tag{5.3}
$$
它甚至满足先前单高孔块估计中可用的那种宽松显式固定头常数。
完整第一孔层则恒为0。

### 5.3. 同一个实际低位 carry 却产生非平方可和第二孔层

令 $\mathcal C_a=\sum_i a_i\mathsf E_i^*$ 为纯 creation，
并把
$$
\mathcal R=T_N^*-\mathcal C_a
$$
先按逐行有限和作用于形式数组。

考虑输出
$$
m_j=2^{8j}+2^j.
$$
所有非零输入 $n_l$ 都是奇数。
因此加 $2^i$ 若 $i\ge1$，不能从这些输入到达偶数 $m_j$。
$i=0$ 时唯一可能输入是 $m_j-1=n_j$。

从 $n_j$ 加1要跨过长度 $j$ 的低孔串，故真实系数精确为
$$
\mathsf N_0^*e_{n_j}
=\frac{\alpha_j}{\alpha_0}e_{m_j}.
$$
纯 creation 的 $\mathsf E_0^*$ 在该输入上为0，因为第0位已有孔。
输出 $m_j$ 只有两个孔，纯 creation 的其余源又都是单孔坐标，(5.1) 在这些源上为0。
所以
$$
\boxed{
(\mathcal R u)_{m_j}
=a_0\frac{\alpha_j}{\alpha_0}\frac{\alpha_0}{\alpha_j}
=1
\qquad(j\ge2).
}
\tag{5.4}
$$
由此
$$
P_{\text{两孔}}\mathcal R u\notin\mathscr H_2.
\tag{5.5}
$$

这说明：有限头的亚四次增长，加上每个固定低头与一高孔的平方可和，
仍不足以把真实 carry 当作从未控高孔层到固定低孔层的全局平滑项。

该数组同时有
$(T_N^*u)_{m_j}=1$，所以 $T_N^*u\notin\mathcal H_-$。
它不满足未知缺陷原像的完整输入条件，尤其没有对应
$f=T^*u\in M\ominus N$。
因此它是对一个推理捷径的实际反例，不是实际饱和 $N=M$ 的反例。

## 6. 继续使用的准确接口

目前可直接使用：

1. 固定次数纯 creation 的有界、逐坐标有限左逆；
2. $T_N^*$ 的形式有限孔输入若有 Hilbert 输出，则输入本身在 Hilbert 空间；
3. 对无限孔原像，必须额外使用真实 $T^*h=f\in H$ 和 $Tf=0$ 两条方程，不能仅凭既有头增长与单高孔界吸收 carry。

尤其，§5 的源保留极高的 $8j$ 孔。
carry 的代价只由较低的 $j$ 决定，
正是把单高孔估计重复套用到所有多孔层时不能忽略的差距。

依赖：R185 的实际二进位权；R93 固定次数 creation 背景；
《残差比例线性延拓、缺陷的形式伴随原像与单高孔通量》及
《形式伴随原像附注：单高孔复制块的真实平方可和性》。
