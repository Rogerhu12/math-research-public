# 商坐标弱零条件的纯平方零障碍及真实正常泛函边界

日期：2026-11-12（UTC）。作者：literature。

状态：完整相邻模型反例与实际必要条件。这里只说明“全部 Banach 商对偶上的弱零”比原 Haar 正常泛函接口强得多；不声称已给实际 $\mathcal A/J$ 的反例，也不声称解决慢符号的普遍限制范围。

## 1. 两个问题须分开

对真实慢符号
$$
S=\sum_{j\ge0}b_jN_j,\qquad b_j=(j+1)^{-2},
\qquad J=\overline{S\mathcal A}^{\|\cdot\|},
$$
已有笔记给充分条件
$$
q(N_j)\rightharpoonup0\quad\text{在 Banach 商 }\mathcal A/J
\quad\Longrightarrow\quad
I\in\overline{J}^{\mathrm{SOT}}.
\tag{1.1}
$$
这里左边测试全部商对偶泛函。
右边实际只需要控制从 Haar 有限秩泛函下降的那些元素。
本稿构造相邻纯平方零代数中的严格差别，然后给真实序列所满足的额外条件。

## 2. 纯平方零代数的一次齐次部分

仍在公平乘积空间的物理 UHF 中工作，令 $E_j=e_{10}^{(j)}$。
这些算子两两交换，$E_j^2=0$，$\|E_j\|=1$。
记
$$
\mathcal Z=\overline{\operatorname{alg}(I,E_0,E_1,\ldots)}^{\|\cdot\|}.
$$

有限张量中的同相旋转
$$
E_j\longmapsto zE_j\qquad(z\in\mathbb T)
$$
与局部代数嵌入相容，给 $\mathcal Z$ 上的点范数连续等距圆群作用 $\gamma_z$。
它不是原加一位移的二进制 gauge。
定义 Fourier 投影
$$
P_k(T)=\int_{\mathbb T}z^{-k}\gamma_z(T)\,dm(z).
\tag{2.1}
$$
所有 $P_k$ 范数至多1。
在 $\mathcal Z$ 上没有负次数，$P_0(T)=\chi_0(T)I$；
$P_1$ 的像是一次齐次部分的范数闭包。

对有限复系数行 $a$，
$$
\frac12\sum_j|a_j|
\le\left\|\sum_j a_jE_j\right\|
\le\sum_j|a_j|.
\tag{2.2}
$$
上界来自三角不等式。
下界中，逐位选择一个单位物理向量 $v_j$，
使
$$
\langle E_jv_j,v_j\rangle
=\frac{\overline{a_j}}{2|a_j|}
$$
（$a_j=0$ 时任选），然后在有限乘积单位向量上取数值域即可。
因此一次齐次部分与 $\ell^1$ 线性同构，其系数唯一。
对任意 $c\in\ell^\infty$，
$$
\lambda_c\left(\sum_j a_jE_j\right)=\sum_j c_ja_j
$$
延伸为有界泛函，且
$$
\|\lambda_c\|\le2\|c\|_\infty.
\tag{2.3}
$$
所以
$$
\varphi_c=\lambda_cP_1\in\mathcal Z^*,
\qquad
\varphi_c(I)=0,\qquad
\varphi_c(E_j)=c_j.
\tag{2.4}
$$

## 3. 一个慢主理想的商坐标并不弱趋零

取任意 $b\in\ell^1$，$b_0\ne0$，且至少有无穷多个非零位；
特别可用 $b_j=(j+1)^{-2}$。
令
$$
B=\sum_jb_jE_j,\qquad
J_0=\overline{B\mathcal Z}^{\|\cdot\|}.
$$
由于 $B$ 恰为一次齐次，非负次数的卷积精确给
$$
P_1(BT)=B P_0(T)=\chi_0(T)B
\qquad(T\in\mathcal Z).
\tag{3.1}
$$
若 $\sum_jb_jc_j=0$，则
$$
\varphi_c(BT)=0\quad(T\in\mathcal Z),
$$
故 $\varphi_c$ 下降为 $(\mathcal Z/J_0)^*$ 的有界泛函。

具体取
$$
c_j=1\quad(j\ge1),\qquad
c_0=-b_0^{-1}\sum_{j\ge1}b_j.
\tag{3.2}
$$
这是有界行，满足上述消去条件，却有 $c_j\to1$。
因此若 $q_0$ 为纯商映射，
$$
\boxed{
q_0(E_j)\text{ 不在 Banach 商 }\mathcal Z/J_0\text{ 中弱趋零}.
}
\tag{3.3}
$$
这不是单凭形式关系构造的代数泛函：
(2.2)—(2.3) 已经付清其原算子范数连续性。

## 4. 此泛函恰不属于 Haar 正常部分

在公平乘积 Haar 表示中，
$$
E_j\longrightarrow\tfrac12I\quad\text{于 WOT}.
\tag{4.1}
$$
先对有限柱向量逐位计算，再用 $\sup_j\|E_j\|=1$ 延伸即可。
因序列统一有界，(4.1) 对所有迹类正常泛函也成立。

若上节 $\varphi_c$ 是某个 Haar 正常泛函在 $\mathcal Z$ 上的限制，则
$$
\varphi_c(E_j)\longrightarrow\tfrac12\varphi_c(I)=0,
$$
与 (3.2) 矛盾。
故
$$
\boxed{
\varphi_c\text{ 不能表示为 Haar 正常泛函的限制}.
}
\tag{4.2}
$$
特别不能用有限秩向量泛函表示它。

这没有判定纯模型 $B$ 的普遍限制范围。
它只严格展示：即使原目标只涉及正常下降泛函，
更强的全部 Banach 商弱零接口也可能被纯奇异泛函破坏。

### 4.1 纯模型中甚至有正的商消去状态

对具体正系数 $b_j=(j+1)^{-2}$，取足够小的 $q>0$，使
$$
q\le\tfrac12,\qquad
q b_0^{-1}\sum_{j\ge1}b_j\le\tfrac12.
$$
定义实数
$$
r_j=q\quad(j\ge1),\qquad
r_0=-q b_0^{-1}\sum_{j\ge1}b_j.
\tag{4.3}
$$
则 $|r_j|\le1/2$ 且 $\sum_jb_jr_j=0$。

先在第 $j$ 位选择单位向量 $v_{j,0}$，
使 $\langle E_jv_{j,0},v_{j,0}\rangle=r_j$；
这总能做到，因为一位 $e_{10}$ 的数值域是半径 $1/2$ 的闭圆盘。
对每个 $t\in[0,2\pi)$，明确令
$$
v_{j,t}=\operatorname{diag}(e^{it},1)v_{j,0},
$$
并取其向量状态 $\omega_{j,t}$。采用第一变量线性的内积，
直接计算给
$$
\omega_{j,t}(E_j)=r_je^{it}.
$$
各有限张量积状态相容，故定义整个物理 UHF 的乘积状态 $\omega_t$。
每个有限局部矩阵元关于 $t$ 连续；
状态范数统一为1，再用局部算子的范数逼近，
得到 $t\mapsto\omega_t(T)$ 对每个 UHF 元素都连续。
对任意有限孔集 $F$，
$$
\omega_t(E_F)=e^{i|F|t}\prod_{j\in F}r_j.
\tag{4.4}
$$
无需假设这个无限乘积状态由原 Haar 空间中的向量实现。

取 $0<\varepsilon\le1/2$，定义状态
$$
\omega(T)=\frac1{2\pi}\int_0^{2\pi}
(1+2\varepsilon\cos t)\,\omega_t(T)\,dt.
\tag{4.5}
$$
被积密度非负且积分为1；先在有限局部算子上定义，再按范数延拓，
所以 $\omega$ 确为正、范数为1的 UHF 状态。
Fourier 正交性给
$$
\omega(I)=1,\qquad
\omega(E_j)=\varepsilon r_j,\qquad
\omega(E_F)=0\quad(|F|\ge2).
\tag{4.6}
$$
因此在 $\mathcal Z$ 上，
$$
\omega=\chi_0+\varepsilon\varphi_r.
$$
由 (3.1) 及 $\sum b_jr_j=0$，
$$
\omega(J_0)=0,\qquad
\omega(E_j)\longrightarrow\varepsilon q>0.
\tag{4.7}
$$
所以纯商的弱零障碍甚至可由一个正状态见证。

这个状态仍不是 Haar 正常状态：
若它正常，(4.1) 会迫
$\omega(E_j)\to\omega(I)/2=1/2$，
而 $\varepsilon q\le1/4$。
这进一步强调，限制为正泛函仍不能省去指定 Haar 正常表示的要求。

## 5. 为什么不能把构造搬到真实代数

真实算子满足
$$
N_j^2=\eta_jN_{j+1},\qquad \eta_j>0.
\tag{5.1}
$$
假如存在一个代数 gauge 同时使 $N_j\mapsto zN_j$，
则对 (5.1) 两端应用它会要求
$$
z^2\eta_jN_{j+1}=z\eta_jN_{j+1}.
$$
因为 $N_{j+1}\ne0$，非零 $z$ 只能取1。
所以 §2 的同相齐次代数作用在真实代数中不存在。

原真实二进制 gauge 是
$N_j\mapsto z^{2^j}N_j$，
其次数也与 §2 的“每个字母次数1”不同。
因此 (3.1) 不能在真实 $S$ 上照抄。
无论 $\eta_j$ 多小，它们都是精确非零的代数关系；
本稿不以范数小扰动来保持理想消去条件。

## 6. 真实正常下降泛函的精确矩条件

设 $\varphi$ 为 Haar 正常泛函，且 $\varphi(J)=0$。
记
$$
W_n=\|A^n\|,\qquad
t_n=\frac{\varphi(A^n)}{W_n},\qquad W_0=1.
$$
则 $|t_n|\le\|\varphi\|$。
因 $N_j=A^{2^j}/W_{2^j}$ 及 $b\in\ell^1$，
对每个固定 $k\ge0$ 有绝对收敛的真实对偶方程
$$
0=\frac{\varphi(SA^k)}{W_k}
=\sum_{j\ge0}
b_j\frac{W_{k+2^j}}{W_kW_{2^j}}\,t_{k+2^j}.
\tag{6.1}
$$
权比不超过1。若 $2^j>k$，二进制权积没有相互进位，故权比恰为1。

还有正常性特有的高位兼容条件：
固定 $k$ 时，$N_jA^k/W_k$ 的 Haar-WOT 极限为 $A^k/(2W_k)$，
故
$$
\boxed{
t_{k+2^j}\longrightarrow\tfrac12t_k
\qquad(j\to\infty,\ 2^j>k).
}
\tag{6.2}
$$
同样，固定有限个不同高位、逐一令其趋于无穷，得到迭代的
$2^{-r}t_k$ 极限。这里保持先固定其余位的极限顺序；
没有把固定阶极限误作随阶数增长的一致估计。

(6.1) 来自真实主理想，(6.2) 来自指定 Haar 正常表示。
仅仅构造一个满足 (6.1) 的有界标量序列，
既不证明其给出 $\mathcal A$ 上的连续泛函，
更不证明它满足 (6.2) 或来自 Haar 正常泛函。

目前仍缺：从真实方程及正常性得到 $t_0=0$，
或以别的方法证明所有正常消去泛函均消去 $I$。
本稿没有将这一缺口改写成已完成结论。

## 7. 实际强主理想失败可由正的有限秩状态见证

下面的缩减适用于真实代数，和纯模型反例无关。

**命题7.1。** 对真实范数闭主理想 $J=\overline{S\mathcal A}$，
以下两项等价：

1. $I\notin\overline J^{\rm SOT}$；
2. 存在有限个向量 $x_1,\ldots,x_d\in H$，至少一个非零，使
   $$
   \varphi(T)=\sum_{i=1}^d\langle Tx_i,x_i\rangle
   $$
   满足 $\varphi(J)=0$。

可将该泛函除以 $\sum_i\|x_i\|^2$，得到正的有限秩正常状态。
没有把“有限秩”进一步降低为秩一。

**证明。** 第2项显然排除 $I$ 的强逼近，因为有限个固定向量上的矩阵元
在 SOT 下连续，且 $\varphi(I)>0$。

反过来，若第1项成立，由 SOT 邻域的定义，可取有限向量
$$
F=(f_1,\ldots,f_d)\in H^{(d)}
$$
使
$$
F\notin
N:=\overline{\{T^{(d)}F:T\in J\}}.
\tag{7.1}
$$
括号中每次使用的是同一个 $T$ 的对角放大；
没有让各个坐标独立选择不同的理想元素。
该集合为线性空间，闭包也为线性子空间。

令
$$
M=\overline{\{p(A)^{(d)}F:p\in\mathbb C[z]\}}
=\operatorname{cyc}_{A^{(d)}}(F).
\tag{7.2}
$$
由于 $J\subseteq\mathcal A$，有 $N\subseteq M$。
而且
$$
T^{(d)}M\subseteq N\qquad(T\in J).
\tag{7.3}
$$
确实，若 $p_n(A)^{(d)}F\to y\in M$，则
$T p_n(A)\in J$，故
$T^{(d)}y=\lim_n(Tp_n(A))^{(d)}F\in N$。
这里先固定有界算子 $T$ 再取极限，没有使用不同 $T$ 的统一范数界。

设
$$
x=P_{M\ominus N}F.
$$
由 (7.1) 得 $x\ne0$，并且 $x\in M$、$x\perp N$。
对每个 $T\in J$，(7.3) 给
$$
\langle T^{(d)}x,x\rangle=0.
$$
把 $x$ 写成 $(x_1,\ldots,x_d)$，便得到第2项的正有限秩泛函。证毕。

归一化后的这种见证若存在，其 §6 矩满足
$$
|t_n|\le1,\qquad t_0=1,\qquad
t_{k+2^j}\longrightarrow\tfrac12t_k,
$$
以及完整的正状态 Gram 不等式，而不只是一个任意有界形式序列。
因此实际目标可以缩小为排除这样的正、有限秩、Haar 正常消去状态。
第4.1节说明，即使保留正性，若丢掉 Haar 正常性，纯模型中仍会出现反例。
本稿没有从这些额外条件直接推得矛盾。

内部依据：R12 的归一化幂与高位极限、真实二进制权积公式，以及
[正常/商接口审查](../notes/2026-11-12-factorization-fock-defect-subdiagonal-and-normal-boundary-audit-0c-agent.md)。
