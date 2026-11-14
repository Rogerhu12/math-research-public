# R275：一位添加的完整 primitive MP 递推、对角继承与真实剪切创新

日期：2026-11-14。会话：Astra-ISP-789f / literature_audit。作者：ChatGPT，GPT-6 Astra Pro。

**状态：§§1–6 的身份、对角继承和真实 Boolean 障碍已证明；§5 的创新矩阵正性未证明。** 这里处理任意有限正权 Boolean 行的一位添加，不增加一个特殊权组模型作为替代目标。所有 $\Gamma$ 都是 $D^j/j!$ 的完整层最小逆 Gram；真 $D^j$ 的最小逆 Gram 是 $\Gamma_j/(j!)^2$。本稿的 $\Gamma$ 不是首物理头接合图的 $T^*T$。

一般目标仍是
$$\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\preceq C\Gamma_{n-1}.$$
下文没有证明通用 $C=1$，也没有给出它的反例或一个有限统一 $C$。

## 1. 完整物理空间及同一个新源

旧行有 $M$ 个位，
$$d=\sum_{i=1}^M b_iE_i,\qquad b_i>0.$$
在正交子集基上记旧孔层为 $\mathcal H_r$。添加一个权 $a>0$ 的位，得新行
$$D=d\otimes I+aI\otimes E.$$
按新位未占据、已占据分解新 $s$ 孔层，删除是
$$D_s=\begin{pmatrix}d_s&aI\\0&d_{s-1}\end{pmatrix}:
\mathcal H_s\oplus\mathcal H_{s-1}\longrightarrow
\mathcal H_{s-1}\oplus\mathcal H_{s-2}.$$

取 $s\ge1$，并令新行满长
$$h=M+1-2s\ge2.$$
置
$$K=\ker d_s,\qquad L=\ker d_{s-1},\qquad R=d_s^\dagger|_L:L\to\mathcal H_s.$$
特别 $d_sR=I_L$、$R(L)\perp K$。$s=1$ 时 $L=\mathbb C$，下一个删除为零。

新 primitive 空间的同一个源映射为
$$\boxed{\mathcal E(x,y)=(x-aRy,y),\qquad (x,y)\in K\oplus L.}\tag{1.1}$$
它是到 $\ker D_s$ 的线性双射：第二行迫 $y\in L$，第一行迫 $x-aRy$，且全部自由量恰是 $x\in K$。各高度均使用 (1.1)，不更换源。

记旧完整层幂
$$A_j=\frac{d^j}{j!}:\mathcal H_{s+j}\to\mathcal H_s,
\qquad F_j=A_jA_j^*.$$
对于 $0\le j\le h-1=M-2s$，$A_j$ 满射，$F_j>0$。这由正对角去权后的 Boolean 包含矩阵满秩给出；其准确满射范围也见 [R271 有限模型归约](R271-appendix-universal-adjacent-height-constants-finite-models-and-continuous-tail.md) §1。

旧两个出生的真实形式记为
$$G_j=P_KF_j^{-1}|_K\quad(0\le j\le h-1),$$
$$L_j=P_L\left[\frac{d^j(d^*)^j}{(j!)^2}\bigg|_{\mathcal H_{s-1}}\right]^{-1}\bigg|_L
\quad(0\le j\le h+1).\tag{1.2}$$
因此 $G_0=I_K,L_0=I_L$。定义真实跨出生系数
$$\boxed{T_j=G_j^{-1}P_KF_j^{-1}R:L\to K,\qquad0\le j\le h-1.}\tag{1.3}$$
有 $T_0=0$。只取完整逆后压缩，没有交换这两个操作。

## 2. 两步核的准确完成平方

在旧层的 $K\oplus R(L)=\ker d_s^2$ 上，完整形式准确为
$$\boxed{
\langle F_j^{-1}(x+Ry),x+Ry\rangle
=\|x+T_jy\|_{G_j}^2+\frac1{(j+1)^2}\|y\|_{L_{j+1}}^2.
}\tag{2.1}$$

证明：按 $x\in K$ 完成平方得到第一项。剩余最小值是约束 $d_su=y$ 下的 $F_j^{-1}$ 最小能量，因而为
$$\langle(d_sF_jd_s^*)^{-1}y,y\rangle.$$
而
$$d_sA_j=(j+1)\frac{d^{j+1}}{(j+1)!},$$
故 $d_sF_jd_s^*=(j+1)^2F_{j+1}^{(s-1)}$。这是完整层等式，给出 (2.1)，包括全部较低出生的自由补全。

对于 $1\le j\le h-1$，新归一幂的两行是
$$\frac{D^j}{j!}=\begin{pmatrix}A_j&aA_{j-1}\\0&A_j^{(s-1)}\end{pmatrix}.$$
若新输入为 $(z,w)$，令 $t=A_{j-1}w$，则其第二行等于 $d_st/j$。因此同源 (1.1) 的准确最小能量是
$$\min_{t:\ d_st=jy}
\left\{\|x-aRy-at\|_{F_j^{-1}}^2+\|t\|_{F_{j-1}^{-1}}^2\right\}.
\tag{2.2}$$
两项都是其整个原像纤维的最小值；所用幂满射，故没有漏掉相容条件。写 $t=jRy+v$，$v\in K$，并对两项使用 (2.1)，得
$$\min_{v\in K}\left\{
\|x-av-a(j+1)T_jy\|_{G_j}^2+
\|v+jT_{j-1}y\|_{G_{j-1}}^2
\right\}+\|y\|_{L_j+a^2L_{j+1}}^2.$$

设置
$$Q_j=(j+1)T_j-jT_{j-1},\qquad
P_j=(G_j^{-1}+a^2G_{j-1}^{-1})^{-1},\qquad
V_j=L_j+a^2L_{j+1}.\tag{2.3}$$
平行和的真实最小化给
$$\boxed{\widetilde\Gamma_j[(x,y)]=
\|x-aQ_jy\|_{P_j}^2+\|y\|_{V_j}^2,\qquad1\le j\le h-1.}\tag{2.4}$$
这里 $\widetilde\Gamma_j=\mathcal E^*\Gamma_j(D;s)\mathcal E$。由于 $\mathcal E$ 对所有高度相同且为双射，目标相邻序在 $\widetilde\Gamma$ 与原 $\Gamma$ 间完全等价。

高度零同式成立，只需定义
$$P_0=I_K,\qquad Q_0=0,\qquad V_0=I_L+a^2L_1.\tag{2.5}$$
确实 $R^*R=L_1$，而 (1.1) 的原物理范数正是 (2.4)。

## 3. 最顶高度的硬约束完整保留

在 $j=h$，旧 $A_h$ 不满射，不能使用不存在的 $F_h^{-1}$。此时其输入层是 $\mathcal H_{M-s+1}$。映射
$$d_sA_h=(h+1)A_{h+1}^{(s-1)}:
\mathcal H_{M-s+1}\longrightarrow\mathcal H_{s-1}$$
是可逆的互补层映射。因此 $A_h$ 单射，且
$$\mathcal H_s=K\mathbin{\dotplus}\operatorname{Ran}A_h.$$
直和的交为零：若 $A_hz\in K$，则 $d_sA_hz=0$ 迫 $z=0$；维数相加为整层维数。

令 $U$ 为沿 $\operatorname{Ran}A_h$ 投到 $K$ 的真实斜投影，准确为
$$U=I-A_h(d_sA_h)^{-1}d_s.\tag{3.1}$$
顶端的 (2.2) 应改为使用 $F_h^\dagger$，并同时要求
$$x-aRy-at\in\operatorname{Ran}A_h.$$
写 $t=hRy+v$ 后，此硬约束唯一决定
$$v=a^{-1}x-(h+1)URy.\tag{3.2}$$
第一项的源变为 $-a(h+1)(I-U)Ry$。因 $d_s(I-U)Ry=y$，其唯一原像正好是 $-a(A_{h+1}^{(s-1)})^{-1}y$，故第一项能量为 $a^2L_{h+1}[y]$。第二项用 (2.1) 的 $j=h-1$ 完成平方，得到与 (2.4) 相同的表达式，其中
$$\boxed{P_h=a^{-2}G_{h-1},\qquad
Q_h=(h+1)UR-hT_{h-1},\qquad V_h=L_h+a^2L_{h+1}.}\tag{3.3}$$
这实际解完了顶端硬约束，不是内点极限，也没有把旧 $\Gamma_h$ 当成有限正矩阵。

于是全部 $0\le j\le h$ 都有明确三角 Gram
$$\boxed{\widetilde\Gamma_j=
\begin{pmatrix}
P_j&-aP_jQ_j\\
-aQ_j^*P_j&V_j+a^2Q_j^*P_jQ_j
\end{pmatrix}.}\tag{3.4}$$

## 4. 若旧相邻序成立，两条对角序已完整继承

本节是条件性继承引理，不假称旧任意权的目标已经证明。假设旧 $G_j$ 及 $L_j$ 在各自全部合法高度满足常数一的相邻序。那么 (3.4) 的 $P_j,V_j$ 也分别满足常数一的相邻序，包含两端。

对 $V_j=L_j+a^2L_{j+1}$，这直接由相邻 $2\times2$ 正块矩阵相加得到。

对 $P$ 需要一个非交换卷积引理。称精度序列 $C_j>0$ 相邻矩阵 log 凹，若
$$C_{j+1}\preceq C_jC_{j-1}^{-1}C_j.$$
若 $C_0,C_1,C_2,C_3$ 满足连续两条这种序，则对任意 $t>0$，
$$\boxed{C_3+tC_2\preceq
(C_2+tC_1)(C_1+tC_0)^{-1}(C_2+tC_1).}\tag{4.1}$$

证明：用同一同余归一 $C_0=I$，写 $A=C_1,B=C_2$。则 $0<B\preceq A^2$、$C_3\preceq BA^{-1}B$。置 $Z=A^2-B\succeq0$。直接按正确非交换次序展开得
$$\begin{aligned}
&(B+tA)(A+tI)^{-1}(B+tA)-(BA^{-1}B+tB)\\
&\qquad=t\{Z-ZA^{-1}(A+tI)^{-1}Z\}\succeq0.\tag{4.2}
\end{aligned}$$
最后一步用 $Z\preceq A^2$ 及
$A^{-1}(A+tI)^{-1}\preceq A^{-2}$：
$Z^{1/2}A^{-2}Z^{1/2}\preceq I$，所以花括号正。加回 $BA^{-1}B-C_3$ 即证。

现在令 $C_j=G_j^{-1}$，并只在**精度递推**中置两个边界值
$$C_{-1}=0,\qquad C_h=0.$$
这不定义不存在的 $G_h$。由 (2.3)、(2.5)、(3.3)，准确有
$$P_j^{-1}=C_j+a^2C_{j-1}\quad(0\le j\le h).$$
内部直接使用 (4.1)。首边另由
$$\begin{aligned}
&(C_1+tC_0)C_0^{-1}(C_1+tC_0)-(C_2+tC_1)\\
&=(C_1C_0^{-1}C_1-C_2)+tC_1+t^2C_0\succeq0
\end{aligned}$$
支付。末边允许 (4.1) 的 $C_3=0$，同一证明仍适用；$h=2$ 时直接用上述首边即可。反转后恰得 $P$ 的目标相邻序。

因此一位归纳的困难不在于平行和或这两条对角序是否保正；这些部分已经证明。

## 5. 剩余是明确的真实剪切创新矩阵

固定 $1\le n<h$，简写下标 $-,0,+$ 为 $n-1,n,n+1$，定义
$$\Delta_-=Q_n-Q_{n-1},\qquad \Delta_+=Q_{n+1}-Q_n,$$
$$A_0=P_--P_0P_+^{-1}P_0,\qquad
B_0=V_--V_0V_+^{-1}V_0.\tag{5.1}$$
在 §4 的旧归纳假设下，$A_0,B_0\succeq0$。

对三个高度同时作同一源变换 $x'=x-aQ_ny$。中间 Gram 变成 $\operatorname{diag}(P_0,V_0)$；其余两项保留真实创新。直接求 $\widetilde\Gamma_+^{-1}$，得到目标差的准确同余：
$$\boxed{\mathcal D_n=
\begin{pmatrix}
A_0-a^2P_0\Delta_+V_+^{-1}\Delta_+^*P_0&
a(P_-\Delta_--P_0\Delta_+V_+^{-1}V_0)\\
a(\Delta_-^*P_--V_0V_+^{-1}\Delta_+^*P_0)&
B_0+a^2\Delta_-^*P_-\Delta_-
\end{pmatrix}.}\tag{5.2}$$
即
$$\widetilde\Gamma_n\widetilde\Gamma_{n+1}^{-1}
\widetilde\Gamma_n\preceq\widetilde\Gamma_{n-1}
\quad\Longleftrightarrow\quad \mathcal D_n\succeq0.$$
每个逆和交叉次序都保留，未用逐向量标量比较替换矩阵乘积。

即使 $A_0,B_0$ 已正，仍必须支付例如必要条件
$$a^2P_0\Delta_+V_+^{-1}\Delta_+^*P_0\preceq A_0,\tag{5.3}$$
以及 (5.2) 的交叉项。若右下块 $B$ 严格正，则完整所需条件准确是
$$A_0-a^2P_0\Delta_+V_+^{-1}\Delta_+^*P_0
\succeq a^2W B^{-1}W^*,$$
$$W=P_-\Delta_--P_0\Delta_+V_+^{-1}V_0,
\qquad B=B_0+a^2\Delta_-^*P_-\Delta_-.$$
退化情形应保 (5.2) 的完整正块及其值域条件，不擅用逆。

这些创新与旧右逆坐标的选择无关。若将 $R$ 换成 $R+Z$，$Z:L\to K$，则每个 $T_j$ 及顶端 $UR$ 都增加 $Z$，因而所有 $Q_j$ 同加 $Z$，而 $\Delta_\pm$ 不变。选 MP 右逆只让 $Q_0=0$；它没有消除 (5.2) 中的真实信息。

## 6. 真实四位例排除单阶剪切的统一粗界

不能用“每个 $Q_j$ 在其自身两对角度量间统一有界”代替 (5.2)。取旧三位正权
$$b=(r,1,1),\quad s=1,\quad r>0,$$
再添加 $a=1$。新满长 $h=2$。置 $z=r^2$、$S=z+2$、$e_2=2z+1$。旧出生零有
$$L_2=e_2^{-1},\qquad L_3=z^{-1}.$$
以物理向量表示 $T_j,Q_j$，由 (1.3) 及 (3.1) 得
$$R=\frac{(r,1,1)^T}{S},\qquad
T_1=R-\frac{(2r,z+1,z+1)^T}{2e_2},$$
$$UR=R-\frac{(1,r,r)^T}{3r}.$$
所以
$$Q_2=3UR-2T_1
=\frac{1-z^2}{S e_2}\,(-2/r,1,1)^T.\tag{6.1}$$
在重位与另两位对称方向组成的正交二维坐标中，
$$F_1=\begin{pmatrix}2&\sqrt2r\\\sqrt2r&z+2\end{pmatrix},
\qquad\det F_1=4.$$
顶端 $P_2=G_1$。直接取完整逆得
$$Q_2^*P_2Q_2=\frac{2(z^2-1)^2}{z(z+2)^2(2z+1)}.$$
因此实际两对角尺度之间的剪切平方恰为
$$\boxed{
\frac{a^2Q_2^*P_2Q_2}{V_2}
=\frac{2(z^2-1)^2}{(z+2)^2(3z+1)}
\sim\frac23z\longrightarrow\infty.
}\tag{6.2}$$
这已经是真实四位正权 Boolean 模型，不是抽象 Lefschetz 模块。它**不是目标相邻序的反例**：该出生一首边属于已经证明的通用范围，见 [R271 出生一首边](R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md)。它准确排除的是当前 MP 源分解下逐高度粗压 $Q_j$ 的统一常数捷径。跨高度相消不能删除。

## 7. 校准及仍未完成的任务

配套 [精确校准脚本](../notes/2026-11-14-one-bit-schur-789f-next.py)从原子集包含矩阵完整求逆，与 (2.4)、(3.3) 独立比较；包括一般出生、两端和多个完全不同正权。脚本只验证已证明身份的实现，不把有限样本作为一般相邻正性的证据。

一般 $C=1$ 或统一 $C<\infty$ 仍未得。当前一位归纳的准确新需求是：利用真实乘积权的 $F_j$ 与 $T_j$，控制 (5.2) 的**两个创新及其非交换交叉项**。纯 $G,L$ 相邻序只支付 §4，单阶剪切范数由 §6 排除；抽象 HL/HR 与完整 Hankel 正矩均不能补上这个信息。

本稿不把 primitive 相邻序当作首物理头 graph Gram 的逆传播界；二者之间仍须保同一个来源、全部跨出生返回与实际费用。边界 $N=M$、正常见证和普通 Hilbert ISP 均未关闭。

## 8. 同一三次权桥给出的全高度创新

[附录完整证明](R275-appendix-exact-cubic-bridge-for-shear-innovations.md)进一步消去全部跨出生 $T_j$。令 $B=(\sum b_i^3E_i)|_K:K\to L$、$C_j=G_j^{-1}$，仅记 $C_{-1}=0$，则全部 $1≤j≤h$ 有
$$Q_j-Q_{j-1}=\frac1j(C_{j-1}B^*L_{j+1}-C_{j-2}B^*L_j).$$
最高端由真MP塔和两下降证明，不需要不存在的 $G_h$。这把 (5.2) 的两个创新都化为同一个实际三次权桥及旧完整Gram；对这些真实数据的完整块正性仍须另证。

精确校准：主稿14个完整层递推、6个同源创新缺陷同余及真实四位剪切发散符号式全部通过；附录另10条全高度三次桥创新通过。有限校准只核身份实现，不替代上述全参数证明或未付相邻正性。
