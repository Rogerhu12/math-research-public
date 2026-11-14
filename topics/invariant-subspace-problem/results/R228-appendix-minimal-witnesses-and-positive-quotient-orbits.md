# R228A：最小见证的保正商轨道与低秩张量限制

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：以下最小秩等价与子商几何约束完整。它们提供保持正性和原主理想湮灭的正确轨道操作，但尚未证明这些约束在本题不可能同时成立。

## 1. 一般分离泛函和正分离泛函的最小秩相同

记 $\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$，固定 $S\in\mathcal A$，并令
$$\mathcal J=S\mathcal A.$$
本题全部有限放大均让同一个 $A,S,F$ 对角作用。

假设存在有限秩泛函 $\phi$，满足
$$\phi(\mathcal J)=0,\qquad\phi(I)\ne0.$$
把该泛函的最小向量分解写为
$$\phi(T)=\sum_{i=1}^r\langle Tf_i,g_i\rangle.$$
令 $x=(f_i)$、$y=(g_i)\in H^{(r)}$，定义
$$
M=\overline{\{F^{(r)}x:F\in\mathcal A\}},
\qquad N=\overline{S^{(r)}M},\qquad Q=M\ominus N.
\tag{1.1}
$$
由于 $S\in\mathcal A$，$M$ 被 $S^{(r)}$ 保持，故 $N\subseteq M$。这一假设也可以放宽为 $S$ 属于 $A$ 的强多项式闭包；本稿从始至终采用足够覆盖目标慢符号的 $S\in\mathcal A$。

$y\perp N$，而 $\langle x,y\rangle\ne0$，故 $Q\ne0$。取 $0\ne q\in Q$。因为 $F^{(r)}q\in M$、$S^{(r)}M\subseteq N$，
$$
\langle (SF)^{(r)}q,q\rangle=0\quad(F\in\mathcal A).
$$
因此
$$
\rho_q=\|q\|^{-2}\sum_{i=1}^r q_i\otimes q_i
\tag{1.2}
$$
是迹为1的正见证，且 $\operatorname{rank}\rho_q\le r$。

正见证本身当然也是一般有限秩见证，所以
$$
\boxed{
\min\operatorname{rank}(\text{一般有限秩分离泛函})
=\min\operatorname{rank}(\text{正有限秩分离泛函}).
}
\tag{1.3}
$$
这里秩是代表有限秩算子的秩；等价于最少向量配对项数。

## 2. 从最小正见证构造一个规范零子商

取最小秩为 $d$ 的正见证
$$
\rho=\sum_{i=1}^d f_i\otimes f_i,\qquad
\sum_i\|f_i\|^2=1,
$$
并令 $x=(f_i)$、$M,N,Q$ 如 (1.1)。原湮灭条件直接给
$$x\perp N,$$
因此这次有 $x\in Q$，无需再次投影它。$Q$ 是 $M/N$ 的正交实现，$S_Q=0$。

对每个 $F\in\mathcal A$，置
$$q_F=P_QF^{(d)}x.$$
若 $q_F\ne0$，则 (1.2) 定义的 $\rho_{q_F}$ 仍是正见证。这就是正确的保正轨道操作。

其保持湮灭的理由是 $q_F\in Q$，而非未经证明的
$F\rho F^*$ 保持原泛函条件。投影 $P_Q$ 一般不能删除；也没有假设 $C^{(d)}Q=Q$。

$P_Q\{F^{(d)}x:F\in\mathcal A\}$ 在 $Q$ 稠密，所以 $x$ 对压缩商代数循环。

## 3. 零子商中的每个非零向量都必须满 Schmidt 秩

对 $z=(z_1,\ldots,z_d)\in H^{(d)}$，定义
$$\operatorname{srank}z=\dim\operatorname{span}\{z_1,\ldots,z_d\}.$$
这也等于正密度 $\sum_i z_i\otimes z_i$ 的秩。

由 (1.2)—(1.3) 的最小性，立刻有
$$
\boxed{
0\ne q\in Q\ \Longrightarrow\ \operatorname{srank}q=d.
}
\tag{3.1}
$$
结合另一篇 C 实化短注，若 $W_q=\operatorname{span}\{q_1,\ldots,q_d\}$，则还必须
$$\dim(W_q\cap CW_q)\le1.$$
这是各个 $q$ 的有限支撑条件，不是 $Q$ 本身的共轭不变性。

更强地，
$$
\boxed{
 m\in M,\quad\operatorname{srank}m<d\ \Longrightarrow\ m\in N.
}
\tag{3.2}
$$
证明：若 $q=P_Qm\ne0$，则
$$\psi(T)=\langle T^{(d)}m,q\rangle$$
湮灭 $S\mathcal A$，且 $\psi(I)=\|q\|^2>0$。若 $m$ 的分量只张成 $r<d$ 维空间，按该空间的一组基重写上式，就得到至多 $r$ 个向量配对项，故 $\psi$ 的秩至多 $r$。这与 (1.3) 矛盾。因此 $P_Qm=0$，即 $m\in N$。

## 4. 一维交换子行不能在 H 中看到这个商

若 $d>1$，取任意有限行
$$
R=(C_1,\ldots,C_d):H^{(d)}\to H,
\qquad C_i\in\{A\}',
$$
并要求每个 $C_i$ 与 $S$ 交换。本题 $S\in\mathcal A$ 时这一点自动成立；本题全交换子交换性也保证它。

定义
$$
M_R=\overline{RM},\qquad N_R=\overline{RN}.
$$
$M_R$ 对 $A$ 不变，且有
$$N_R=\overline{S M_R}.$$
若 $N_R\ne M_R$，取 $0\ne q\in M_R\ominus N_R$，则
$$T\longmapsto\langle Tq,q\rangle$$
是秩一正分离见证，和 $d>1$ 的最小性矛盾。因此
$$
\boxed{\overline{RN}=\overline{RM}\quad\text{对全部上述 }R.}
\tag{4.1}
$$
特别每个常系数坐标行都如此。

(4.1) 是取各坐标像的 Hilbert 闭包后的陈述。它不说明 $RN=RM$，也不提供商的有界逆；因此不能从中直接取消 $R$ 并推出 $N=M$。

## 5. 为什么这些几何限制尚不足够

### 5.1 闭子空间可以全部由满秩向量组成

一般 Hilbert 空间中，(3.1) 并非矛盾。取 $H_0=L^2([0,1])$，令 $T$ 为乘以变量 $t$ 的有界算子，置
$$
\mathcal Q_d=\{(f,Tf,\ldots,T^{d-1}f):f\in H_0\}.
$$
其第一坐标给有界逆，故 $\mathcal Q_d$ 是无限维闭子空间。若其某个非零向量分量线性相关，就有非零多项式 $p$ 满足 $p(t)f(t)=0$ 几乎处处；非零多项式的零点有限，迫 $f=0$，矛盾。因此其每个非零向量都具有满 Schmidt 秩 $d$。

这个例子不满足本题全部慢符号和 C 条件，只说明不能单凭“闭且无限维”排除 (3.1)。

### 5.2 实际 A 的有界图也可以没有低秩向量

本题 $A$ 单射、拟幂零，因而没有特征向量。实际闭不变图
$$\mathcal G(A)=\{(h,Ah):h\in H\}\subset H^{(2)}$$
的每个非零向量均为 Schmidt 秩2。因此不能企图证明“每个实际有限放大循环不变子空间中的低秩向量稠密”。

但此图并不产生当前零子商：若 $S$ 在全 $H$ 中稠密像且与 $A$ 交换，则
$$S^{(2)}(h,Ah)=(Sh,ASh),$$
而 $h\mapsto(h,Ah)$ 是从 $H$ 到该图的有界同构，所以 $S^{(2)}\mathcal G(A)$ 在图中稠密。

### 5.3 真正需要的新机制

若某个 $M$ 是一个闭交换算子的图，$S^{(d)}M$ 是否在 $M$ 稠密是一个图范数问题。环境中 $SH$ 稠密不自动给图范数稠密；有界图的论证不能直接移到无界图。

因此目前正确的任务是：利用实际慢符号和商压缩轨道，排除同时满足 (3.1)、(3.2)、(4.1) 以及 C 支撑限制的非零零子商，或证明相应无界图中的 $S$ 像为图核心。没有哪个步骤可仅凭普通正共轭变形或环境稠密性略过。
