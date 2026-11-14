# R113：纯尾支配的birth-death排核与真实进位迁移障碍

**当前范围更新：** 本文的核排除仅指纯模型；实际全部一阶的循环性另由 R122/R125 完成，进位反例仍说明不能用小扰动作该迁移。

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**已证明，仅为纯张量模型。** literature 已独立逐式核验图递推与出生死亡链。执行器重置后按完整证明重建；不把真实进位删除。

## 1. 主定理

在 H=⊗_{j≥0}(C²,+)、+=(e_0+e_1)/√2 上，令 E_j=e_{10}^{(j)}。
设 a_j 为无限个非零复系数，∑|a_j|<∞，并记

$$
C_m=\sum_{j\ge m}a_jE_j,\qquad
B=C_0,\qquad
\rho_m=\frac{\|C_{m+1}\|}{|a_m|}.
\tag{1}
$$

若有零系数，先枚举非零坐标，未参与的位保留为恒等张量因子。

**定理。** 若存在 m_0 和 0<ρ≤1/2，使

$$
\boxed{\rho_m\le\rho\qquad(m\ge m_0),}
\tag{2}
$$

则 B 单射且值域稠密。有限前缀及全部复相位任意。

可检查的充分条件是 ∑_{j>m}|a_j|≤|a_m|/2 最终成立。
特别地，尾模长和与当前模长的比趋零即足够，不要求这些比值可和或平方可和。

无限非零项不可省略：有限非零纯张量和幂零而有非零核，不能在最后一个零尾处形式使用 (1)。

## 2. 精确广义核图

令

$$
K_{m,k}=\ker C_m^k,\quad K_{m,0}=\{0\},\quad
\gamma_{m,k}=\|P_{K_{m,k}}1_m\|^2.
$$

1_m 为 plus 尾参考向量。故 0≤γ_{m,k}≤1，
γ_{m,0}=0，而且 γ 随 k 非减。

沿第 m 位拆分，置 C=C_{m+1}、a=a_m，则

$$
C_m=\begin{pmatrix}C&0\\aI&C\end{pmatrix},
\qquad
C_m^k=\begin{pmatrix}C^k&0\\kaC^{k-1}&C^k\end{pmatrix}.
$$

直接解两行方程给

$$
K_{m,k}
=
\{(-Cy/(ka)+z,y):
y\in K_{m+1,k+1},\
z\in K_{m+1,k-1}\}.
\tag{3}
$$

令

$$
V=K_{m+1,k}\ominus K_{m+1,k-1},\qquad
W=K_{m+1,k+1}\ominus K_{m+1,k},
$$
$$
T=P_VC|_W,\quad R=T/(ka),\quad
v=P_V1_{m+1},\quad w=P_W1_{m+1}.
$$

将 (3) 正交拆为第一分量的 K_{m+1,k−1}、第二分量的
K_{m+1,k} 及图 {(-Ry,y):y∈W}。后者参数映射的 Gram 算子为
I+R*R，因此

$$
\gamma_{m,k}
=
\frac12\gamma_{m+1,k-1}
+\frac12\gamma_{m+1,k}
+\frac12\left\|
(I+R^*R)^{-1/2}(w-R^*v)
\right\|^2.
\tag{4}
$$

a 可为复数；R* 自动保留正确共轭。并有

$$
\|R\|\le\rho_m/k,\quad
\|w\|^2=\gamma_{m+1,k+1}-\gamma_{m+1,k},\quad
\|v\|^2=\gamma_{m+1,k}-\gamma_{m+1,k-1}.
\tag{5}
$$

## 3. Young 不等式给真正的 Markov 权

令 s=ρ_m/k。由 (I+R*R)^{-1/2} 为收缩，以及
2s∥v∥∥w∥≤s∥v∥²+s∥w∥²，

$$
\left\|(I+R^*R)^{-1/2}(w-R^*v)\right\|^2
\le(1+s)\|w\|^2+(s+s^2)\|v\|^2.
\tag{6}
$$

代入 (4)–(5) 并整理，

$$
\boxed{
\gamma_{m,k}\le
p_-(s)\gamma_{m+1,k-1}
+p_0(s)\gamma_{m+1,k}
+p_+(s)\gamma_{m+1,k+1},
}
\tag{7}
$$
$$
p_-(s)=\frac{1-s-s^2}{2},\qquad
p_0(s)=\frac{s^2}{2},\qquad
p_+(s)=\frac{1+s}{2}.
$$

0≤s≤1/2 时，三权非负且总和为 1。

对任何非减数列 g(k)，右侧对 s 的导数为

$$
\frac12[g(k+1)-g(k-1)]
+s[g(k)-g(k-1)]\ge0.
$$

故 γ 对 k 的单调性允许将 ρ_m 增为统一的 ρ。由此对
m≥m_0，

$$
\gamma_{m,k}\le(P_\rho\gamma_{m+1,\cdot})(k),
\tag{8}
$$

其中 0 吸收，正整数 k 处的向上、向下及原地概率分别为

$$
p_k=\frac{1+\rho/k}{2},\quad
q_k=\frac{1-\rho/k-\rho^2/k^2}{2},\quad
r_k=\frac{\rho^2}{2k^2}.
\tag{9}
$$

全部 p_k,q_k>0。

## 4. 临界 ρ=1/2 仍必吸收

令 τ_0、τ_R 为首次到达 0、R 的时间。有限赌徒破产概率

$$
h_R(k)=\mathbb P_k(\tau_R<\tau_0)
$$

满足 h_R(0)=0、h_R(R)=1，且

$$
p_k(h_R(k+1)-h_R(k))
=q_k(h_R(k)-h_R(k-1)).
$$

设 π_0=1、π_j=∏_{i=1}^j(q_i/p_i)，逐项求差分可得

$$
\boxed{
h_R(k)=
\frac{\sum_{j=0}^{k-1}\pi_j}
{\sum_{j=0}^{R-1}\pi_j}.
}
\tag{10}
$$

原地概率从差分方程中消去，不影响公式。

由 (9)，

$$
q_k/p_k
=1-2\rho/k+O_\rho(k^{-2}),
$$

所以

$$
\log\pi_j=-2\rho\sum_{i=1}^j i^{-1}+O_\rho(1),
\qquad
\pi_j\asymp_\rho(j+1)^{-2\rho}.
$$

2ρ≤1 使 ∑π_j 发散，包括临界 ρ=1/2 的调和级数情形。
因此对固定 k，h_R(k)→0。

在任一有限状态区间 {1,…,R−1} 中，链有统一正概率在至多
R 步内沿向下路径到 0，所以永远困在该有限区间而不碰边界的概率为零。事件 τ_0=∞ 必须在碰 0 前到达每个 R（除去零概率事件），故由 (10)

$$
\mathbb P_k(\tau_0=\infty)=0,\qquad
\mathbb P_k(\tau_0>n)\longrightarrow0.
\tag{11}
$$

## 5. 从核角度到零核，恢复有限前缀及复相位

对固定 m≥m_0 和固定有限 k，迭代 (8) n 次，并用
γ_{s,0}=0、0≤γ≤1，得到

$$
0\le\gamma_{m,k}
\le\mathbb E_k[\gamma_{m+n,S_n};\tau_0>n]
\le\mathbb P_k(\tau_0>n).
$$

由 (11)，γ_{m,k}=0。特别 ker C_m⊥1_m。
C_m 与每个尾部 E_j 交换，核对所有有限 E_F 不变，所以

$$
\langle x,E_F^*1_m\rangle
=\langle E_Fx,1_m\rangle=0
\quad(x\in\ker C_m).
$$

这些向量的张成包含全部柱函数并稠密，故 C_m 单射。

写 B=H_{m_0}+C_{m_0}，其中有限头
H_{m_0}=∑_{j<m_0}a_jE_j 与尾交换，且 H_{m_0}^{m_0+1}=0。
若 Bx=0，则 C_{m_0}^{m_0+1}x=(-H_{m_0})^{m_0+1}x=0。
尾算子单射，其幂及与有限头恒等的张量扩张均单射，所以 x=0。

对复系数，不能仅用不共轭系数的全位互补酉。正确使用反线性对合

$$
(\mathcal Cx)(b)=\overline{x(1-b)}.
$$

它满足 𝒞E_j𝒞=E_j*、𝒞B𝒞=B*，故 ker B*=0，值域稠密。
定理得证。

## 6. 明确例子与几何加强

若相邻模长比 |a_{m+1}|/|a_m|→0，则给定 ε<1，充分大后尾比≤ε/(1−ε)，所以 (2) 最终成立。

因此覆盖任意相位的：

- |a_m|=((m+1)!)^{-σ}，任意 σ>0；
- |a_m|=e^{-c(m+1)^β}，任意 c>0、β>1；
- |a_m|=e^{-(m+2)\log\log(m+3)}。

几何模长 q^m 的 ℓ¹ 尾比为 q/(1−q)，直接覆盖 q≤1/3。
还可用精确算子范数上界加强。将非增正系数从1重新编号，Abel 分解为
∑_{n≥1}(δ_n−δ_{n+1})∑_{j=1}^nE_j；n项等权提升和在第 r 层的范数至多
√((n−r)(r+1))≤(n+1)/2。因此

$$
\left\|\sum_j\delta_jE_j\right\|
\le\frac{\sum_j\delta_j+\max_j\delta_j}{2}.
\tag{12}
$$

任意复相位不改变该范数：对有限和使用局部对角酉，再对范数收敛极限取值；不声称无限相位酉在 plus 表示中可实施。

几何模长因此满足

$$
\rho_m\le\frac{q(2-q)}{2(1-q)}\le\frac12
\quad\text{若}\quad
0<q\le\frac{3-\sqrt5}{2}.
\tag{13}
$$

这是充分范围，不是核存在的精确分界。纯模型坐标排列由 plus
乘积空间中的酉实施；实际进位模型不能任意重排。

## 7. 真实进位的明确缺口

决定性图式 (3) 使用 E_m²=0。真实 N_m 有上右角
η_mN_{m+1}，故实际 S=∑a_jY_j 不满足 k−1、k+1 的递推。

其一位 Schur 关系为：置 C=∑_{j>m}a_jY_j、
N=N_{m+1}、η=η_m、a=a_m，则 aY_m+C 的图核参数空间为

$$
\ker[C^2-\eta N(C+aI)^2].
\tag{14}
$$

例如设 Z=(1−ηN)C−aηN，直接展开有
Z²−a²ηN=(1−ηN)[C²−ηN(C+aI)²]，且所有前因子可逆。
额外 ηN 项不能从核等式中删去。

真实有限头的幂零阶一般为 2^m；一个极小残差的高阶纯尾方程也不等于精确尾核。仍缺足够定量的近零谱控制或利用实际 dyadic 相干关系的新论证。

因此本文只给严格纯模型结论，不改变实际小三次型尾、一般可和临界乘子、A 的普通不变格和完整 Hilbert ISP 的未解状态。

基础精确图见
[纯张量原始稿](../notes/2026-11-12-tensor-kernel-0c-agent.md)。

---

## 附录 1：真实上角进位不能仅以“小”处理：精确图核反例

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**已证明的通用迁移障碍。** 执行器重置后重建。本例不是本题固定 dyadic 系数模型的反例。

### 1. 构造及全部局部条件

取非零单射有界拟幂零 K，例如本仓库实际 A。令 J=tK，
t>0 足够小使 0<∥J∥<1/2，并记

$$
\eta=\|J^2\|>0,\qquad N=J^2/\eta.
$$

N 单射、拟幂零、范数为 1，η→0。在 H⊕H 上设

$$
M=\begin{pmatrix}0&\eta N\\I&0\end{pmatrix}
=\begin{pmatrix}0&J^2\\I&0\end{pmatrix},
\qquad
E=\begin{pmatrix}0&0\\I&0\end{pmatrix}.
$$

则 M 单射、拟幂零，且

$$
M^2=\eta\,\operatorname{diag}(N,N),\qquad
\|M\|=1,\qquad \|M-E\|=\eta.
\tag{1}
$$

固定 a≠0，令 C=aJ(I−J)^{-1} 在两分量上对角作用，
并设

$$
Y=M(I+M)^{-1},\qquad S=aY+C.
$$

C 与 J、N、M 交换，而且

$$
\|C\|/|a|\le\|J\|/(1-\|J\|)\longrightarrow0.
\tag{2}
$$

### 2. 核恰为整个尾空间参数的闭图

定义

$$
\mathcal G_-=\{(-Jy,y):y\in H\}.
$$

M 在此图上对应 −J，所以 Y 对应 −J(I−J)^{-1}，从而
S 在图上恒零。

事实上，记 \widehat J=diag(J,J)，有

$$
S=a(I-\widehat J)^{-1}
(M+\widehat J)(I+M)^{-1},
$$

$$
M+\widehat J
=\begin{pmatrix}J&J^2\\I&J\end{pmatrix}
=\begin{pmatrix}J\\I\end{pmatrix}\begin{pmatrix}I&J\end{pmatrix}.
$$

后者核恰为 𝒢_-。I+M 在图上对应 I−J，故保持该图且在其上可逆。因此

$$
\boxed{\ker S=\mathcal G_-\ne\{0\}.}
\tag{3}
$$

图参数映射 y↦(−Jy,y) 有界，其逆为第二分量投影，故这是实际闭核。

### 3. 精确 Schur 对照

对应真实一位图的 Schur 多项式为

$$
C^2-\eta N(C+aI)^2.
$$

由于 ηN=J²、C+aI=a(I−J)^{-1}，它恒等于零，解释了 (3)。

删去进位的纯局部算子 aE+C 却单射：方程
(Cx,ax+Cy)=0 中，C 单射先给 x=0，再给 y=0。

所以任意小的真实上角进位，可以把一个单射纯局部算子变成有完整图核的算子。这是明确的零点核投影不连续性，而非仅抽象警告。

### 4. 准确的障碍范围

本例同时满足：η 任意小；N 单射拟幂零且范数1；M 单射拟幂零并满足 (1)；尾范数比 (2) 任意小；相关尾算子互相交换。因此仅依赖这些小量和交换性，不足以把纯 birth-death 核递推转为真实模型。

但这里 C 被选为 J 的有理函数，尚未实现为本题规定的
C=∑_{\ell>j}a_\ell N_\ell(I+N_\ell)^{-1}，且 N 未固定为真实归一化幂 N_{j+1}。本例不否定该特殊模型的单射性；其迁移证明必须额外利用真实 dyadic 相干关系或更强的近零谱估计。

参见
[纯尾 birth-death 定理](../notes/2026-11-12-pure-tail-dominance-birth-death-kernel-0c-agent.md)。

---

## 附录 2：单个真实进位不受纯提升和图范数控制

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**已证明。** 执行器重置后重建；仅排除逐个进位作相对小扰动的简化路线。

设 B=∑_{j≥0}a_jE_j，a∈ℓ¹，作用于 plus 纯乘积 Hilbert 空间。
固定 i≠j、a_i≠0。对 N>max(i,j)，令 u_{N,j} 为物理正交基向量：
前 N 位仅 j 为0、其余为1，后尾为 plus 参考向量。定义

$$
v_N=a_i u_{N,j}-a_j u_{N,i}.
\tag{1}
$$

两基向量正交，故

$$
\|v_N\|=(|a_i|^2+|a_j|^2)^{1/2}>0.
$$

有限头 B_{<N} 满足

$$
B_{<N}u_{N,j}=a_j e_1^{\otimes N}\otimes1_{\ge N},
\qquad
B_{<N}u_{N,i}=a_i e_1^{\otimes N}\otimes1_{\ge N}.
$$

所以 B_{<N}v_N=0，并且

$$
\|Bv_N\|
\le\left(\sum_{k\ge N}|a_k|\right)\|v_N\|
\longrightarrow0.
\tag{2}
$$

但 R=E_i^*E_j 有精确作用

$$
Rv_N=a_i u_{N,i},\qquad \|Rv_N\|=|a_i|.
\tag{3}
$$

因此不存在 K<∞ 使 ∥Rx∥≤K∥Bx∥ 对所有 x 成立。
乘任意固定非零小常数 εR 也不改变这个结论。

对实际单个进位，取 j=i+1，使用

$$
N_i-E_i=\eta_iE_i^*N_{i+1}.
$$

在 u_{N,i+1} 上，第 i+1 位为0，N_{i+1} 的进位项为零，主项
E_{i+1} 精确填入该位，故
E_i* N_{i+1}u_{N,i+1}=u_{N,i}。
在 u_{N,i} 上，第 i 位为0，而 N_{i+1} 不作用该位，所以
E_i* N_{i+1}u_{N,i}=0。因此

$$
\boxed{
(N_i-E_i)v_N=\eta_i a_i u_{N,i},
\qquad
\|(N_i-E_i)v_N\|=\eta_i|a_i|>0.
}
\tag{4}
$$

结合 (2)，不存在 K<∞ 使
∥(N_i−E_i)x∥≤K∥Bx∥ 对全部 x 成立。

v_N 弱趋零，是逃向高物理占据的近核向量；这不与纯 B 单射相矛盾。
此反例只否定逐个 carry 的相对图范数控制，未排除真实总和中的特殊抵消或核上的额外控制。实际小三次型尾及完整 ISP 仍未解决。
