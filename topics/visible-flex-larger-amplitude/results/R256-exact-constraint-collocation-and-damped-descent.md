# R256. 完整有限 collocation 的精确约束坐标、伴随与正阻尼下降

日期：2026-11-14。

**状态。** 本文证明固定有限网格上两种坐标表示的全部方程零点双射，给出完整 Jacobian/伴随链式公式，并证明正阻尼加权线性最小二乘的精确解何时是实际有限残差的下降方向。不证明 LSMR 截停必收敛，不证明当前 warm 已解决原 BVP，也不把显式 affine 尾图等同于真实非线性 DN。

对应独立实现：

- [geometry_20261114_constrained_collocation.py](../computations/geometry_20261114_constrained_collocation.py)
- [geometry_20261114_constrained_trust_warm.py](../computations/geometry_20261114_constrained_trust_warm.py)

实际数值只由公开仓库 Actions 执行。本文的代数等式在实数有限系统中成立；浮点实现仍须记录其舍入差、实际方向乘积和真实试探残差，不将同一代码中符号相消冒充另一个实数函数的机器严格证书。

## 1. 原有限增广系统与共同域

固定严格递增的有限网格
$$
s_0<\cdots<s_{m-1},\qquad m\ge2,\qquad h_i=s_{i+1}-s_i.
$$
物理状态维数为 $n=3M+2$，排列为
$$
y=(r_0,\ldots,r_M,\ t_1,\ldots,t_M,\ z_0,\ldots,z_M).
$$
每个节点的增广状态为
$$
X_i=(y_i,c_i,p_i)\in\mathbb R^{n+M+k}.
$$
这里 $c_i$ 有全部 M 个 core 系数，$p_i$ 有全部 k 个 active scalar controls。原增广 RHS 为
$$
\mathcal F(s,X)=\bigl(f(s,y,p),\,0,\,0\bigr).
\tag{256.1}
$$
当前原 BatchedFFTFlow 的物理 RHS 不显含附加 c；c 通过入口识别和右端材料图参与完整问题。本文以这一实际结构为假设；若将来 RHS 显含 c，必须补上相应导数，不能直接套用下面的稀疏块公式。

对每个 trial，先重新计算 $F_i=\mathcal F(s_i,X_i)$，再使用原三次 Hermite 中点
$$
\widehat X_i=\frac{X_i+X_{i+1}}2+
\frac{h_i}{8}(F_i-F_{i+1})
$$
和原 collocation 残差
$$
\mathcal C_i(X)=X_{i+1}-X_i-
\frac{h_i}{6}\left(F_i+F_{i+1}
+4\mathcal F(s_{i+1/2},\widehat X_i)\right).
\tag{256.2}
$$
这是真正含新 nodal RHS 的中点，不是以旧 RHS 或端点方向均值代替的线性路径。

固定前 K 个 core 目标 $\bar c_1,\ldots,\bar c_K$。原左端物理约束为
$$
r_0(0)=1,\qquad r_j(0)=\bar c_j\quad(1\le j\le K),
$$
$$
t_j(0)=-\omega_jr_j(0)\quad(1\le j\le M),\qquad
z_j(0)=0\quad(0\le j\le M),
\qquad \omega_j=2j.
\tag{256.3}
$$
另有 M 个左端识别条件
$$
c_{0,j}=r_j(0).
\tag{256.4}
$$
右端保留全部 T 个原指定方程
$$
\mathcal B(y_{m-1},c_{m-1},p_{m-1})=0.
\tag{256.5}
$$
本文固定同一个右端算子 $\mathcal B$：它可以是明确定义的真实有限 DN，也可以是原内层在某个实际尾锚上使用、如实标记的 affine 图。两种坐标必须使用同一个算子。本定理不把某个 affine 图的零点提升为真实非线性 DN 的零点。当前新有限测试的含义见 [R252](R252-physical-angle-DN-Galerkin-boundary.md)。

平方系统的计数条件是
$$
T=M-K+k.
\tag{256.6}
$$
当前 M=T=112、K=k=3、n=338 满足它。物理左行数为 $2M+K+2$，加上 M 个 core 识别行后为 $n+K$；再加 T 个右行恰好是增广维数 $n+M+k$。

定义共同合法域 $\Omega$：所有原节点、真实中点和所要求的边界图都可定义，且在所作微分处原有限函数为 $C^1$。例如严格 Frenet 域、原 scalar 条件和材料图条件必须沿用原定义。若还要核原 RMS 的两个 Lobatto 点，可将这些实际查询的合法性也并入 $\Omega$。以下证明从不把无效 trial 当作系统中的零点。

## 2. 精确约束坐标

令自由入口 core 变量为
$$
\xi=(c_{K+1},\ldots,c_M)\in\mathbb R^{M-K}.
$$
写
$$
c(\xi)=(\bar c_1,\ldots,\bar c_K,\xi).
$$
用这个完整 core 唯一定义入口物理状态
$$
y_0(\xi)=
\left(1,\ c(\xi),\
-\omega_1c_1(\xi),\ldots,-\omega_Mc_M(\xi),\
0,\ldots,0\right).
\tag{256.7}
$$
所有非入口物理节点保留为独立完整未知量。新的坐标是
$$
q=(y_1,\ldots,y_{m-1},\xi,p)
\in\mathbb R^N,\qquad
N=n(m-1)+(M-K)+k=n(m-1)+T.
\tag{256.8}
$$
定义仿射、单射的扩张映射
$$
E(q)_i=\bigl(y_i,c(\xi),p\bigr),
\tag{256.9}
$$
其中 $y_0$ 使用 (256.7)。没有删去任何物理模式或完整 z0。入口被约束的分量由原左方程确定；非入口所有 n 个物理分量都保留。

记 $\mathcal A$ 为恰好满足 (256.3)--(256.4) 以及所有节点 c、p 相同的增广状态集合。E 是 $\mathbb R^N$ 到 $\mathcal A$ 的仿射双射。其逆映射读取所有非入口物理节点、自由入口 core 和共同 p，唯一性直接成立。

在此坐标中，定义 reduced 残差
$$
\mathcal R(q)=
\left(
\mathcal C_0(Eq)_{\rm physical},\ldots,
\mathcal C_{m-2}(Eq)_{\rm physical},\
\mathcal B(y_{m-1},c(\xi),p)
\right).
\tag{256.10}
$$
它包含全部 $n(m-1)$ 个物理 collocation 行和全部 T 个右行。合法 reduced 域是 $E^{-1}(\Omega)$。

## 3. 定理 R256-A：原全部方程与 reduced 系统的零点双射

**定理。** 在上述共同域内，E 给出以下两个零点集合的双射：

- 原全部增广 collocation 行 (256.2)、全部左行 (256.3)--(256.4) 及全部右行 (256.5)；
- reduced 系统 $\mathcal R(q)=0$。

**证明。**

先取任意 q。由于 (256.1) 的 c、p 导数恒为零，E(q) 中的这些节点值全部相同，其增广 collocation 残差恰为相邻节点差，故恒为零。入口由 (256.7) 定义，全部左端物理及 core 识别行也恒为零。其余原残差恰是 (256.10)。因此 $\mathcal R(q)=0$ 当且仅当 E(q) 满足原全部方程。

反过来，设一个合法增广状态 X 满足原全部方程。c、p 的 collocation 行分别是
$$
c_{i+1}-c_i=0,\qquad p_{i+1}-p_i=0.
$$
沿有限链相加，所有节点 c、p 相同。左端识别和物理约束随后强制其入口恰为 (256.7)。因此 $X\in\mathcal A$，存在唯一 q 使 $X=E(q)$；它的全部剩余方程就是 $\mathcal R(q)=0$。证毕。

更强地，在 $\mathcal A$ 上，经过固定的原行排序，完整残差就是
$$
\mathcal R_{\rm full}(E(q))=
I_{\rm rows}\,\mathcal R(q),
\tag{256.11}
$$
其中 $I_{\rm rows}$ 只是插入恒零约束行的单射，不含残差近似或惩罚参数。

这说明“消去约束”与“删掉未满足方程”不同。这里被消去的行在整个坐标像上都是恒等式，而不是因为权重小、模式高或残差暂小而省略。若输入状态不在 $\mathcal A$，pack 后再 expand 会改变它，必须记录实际入口投影差或拒绝不合适的输入；不能把这个过程称为源状态逐点未变。

当前 699 节点的 reduced 维数是
$$
338\cdot698+112=236036.
$$
这个有限计数不含任何求解成功声明。

## 4. 完整物理中点与 global-control 链式

在 $\mathcal A$ 上，c、p 都是共同常数。令
$$
f_i=f(s_i,y_i,p),\qquad
\widehat y_i=\frac{y_i+y_{i+1}}2+\frac{h_i}{8}(f_i-f_{i+1}),
$$
$$
f_{i+1/2}=f(s_{i+1/2},\widehat y_i,p).
$$
物理 collocation 行为
$$
\Phi_i=y_{i+1}-y_i-\frac{h_i}{6}(f_i+f_{i+1}+4f_{i+1/2}).
\tag{256.12}
$$
记同一原有限 RHS 的导数
$$
A_i=D_yf_i,\qquad U_i=D_pf_i,\qquad
A_{i+1/2}=D_yf_{i+1/2},\qquad U_{i+1/2}=D_pf_{i+1/2}.
$$
对实际方向 $(v_i,v_{i+1},\pi)$，
$$
\delta\widehat y_i=
\frac{v_i+v_{i+1}}2+
\frac{h_i}{8}
\left(A_iv_i-A_{i+1}v_{i+1}+(U_i-U_{i+1})\pi\right).
\tag{256.13}
$$
代入 $\delta\Phi_i$，得到完整三个块
$$
\delta\Phi_i=\mathsf L_iv_i+\mathsf R_iv_{i+1}+\mathsf P_i\pi,
$$
$$
\boxed{
\mathsf L_i=-I-\frac{h_i}{6}(A_i+2A_{i+1/2})
-\frac{h_i^2}{12}A_{i+1/2}A_i,
}
\tag{256.14}
$$
$$
\boxed{
\mathsf R_i=I-\frac{h_i}{6}(A_{i+1}+2A_{i+1/2})
+\frac{h_i^2}{12}A_{i+1/2}A_{i+1},
}
\tag{256.15}
$$
$$
\boxed{
\mathsf P_i=
-\frac{h_i}{6}(U_i+U_{i+1}+4U_{i+1/2})
-\frac{h_i^2}{12}A_{i+1/2}(U_i-U_{i+1}).
}
\tag{256.16}
$$

最后一式中的 $h_i^2$ 项来自真实中点，不能因为 p 在所有节点相同就省去。p 恒定只意味着它在 midpoint 仍是同一个 p；物理 midpoint 对 p 的依赖仍通过两端 RHS 非线性进入。

对原增广 local_blocks 而言，左右端的 p 块相加恰为 (256.16)，因为同一 global p 同时改变两个端点。这解释了实现中的完整 $\mathsf P=L_{\rm parameter}+R_{\rm parameter}$；它不是只保留直接中点参数导数。

这些链式式子是在固定网格上的状态/参数导数，不包含网格位置变分。当前 warm 的网格固定；若改变网格，须在新固定网格上重新定义和计算模型，而不能遗漏移动节点的链式。

## 5. 入口 map、完整 Jacobian action 与 adjoint

令
$$
T_0=D_\xi y_0\in\mathbb R^{n\times(M-K)},\qquad
C_0=D_\xi c\in\mathbb R^{M\times(M-K)}.
$$
对自由模式 j，$T_0$ 的对应列在 $r_j$ 行为 1，在 $t_j$ 行为 $-\omega_j$，其余为零；$C_0$ 选取该 core 分量。令右端导数为
$$
B_y=D_y\mathcal B,\qquad
B_\xi=(D_c\mathcal B)C_0,\qquad
B_p=D_p\mathcal B.
$$

### 5.1 正向 action

对 reduced 方向
$$
v=(v_1,\ldots,v_{m-1},\eta,\pi),
$$
先置 $v_0=T_0\eta$。完整 $Jv=D\mathcal R(q)v$ 为
$$
(Jv)_i=\mathsf L_iv_i+\mathsf R_iv_{i+1}+\mathsf P_i\pi,
\quad 0\le i\le m-2,
\tag{256.17}
$$
$$
(Jv)_{\rm right}=B_yv_{m-1}+B_\xi\eta+B_p\pi.
\tag{256.18}
$$
自由 core 同时改变入口 r/t 与右端材料图，两条路径都出现。物理 RHS 不显含附加 c，正是这里没有另一项沿各 interval 的显式 core 列的原因。

### 5.2 完整伴随

取 interval 对偶向量 $\lambda_i\in\mathbb R^n$ 和右端对偶向量 $\mu\in\mathbb R^T$。则 $J^T(\lambda,\mu)$ 的各部分为
$$
g_{y_j}=
\mathsf R_{j-1}^T\lambda_{j-1}
+\mathbf1_{j\le m-2}\mathsf L_j^T\lambda_j
+\mathbf1_{j=m-1}B_y^T\mu,
\quad 1\le j\le m-1,
\tag{256.19}
$$
$$
\boxed{g_\xi=T_0^T\mathsf L_0^T\lambda_0+B_\xi^T\mu,}
\tag{256.20}
$$
$$
\boxed{g_p=\sum_{i=0}^{m-2}\mathsf P_i^T\lambda_i+B_p^T\mu.}
\tag{256.21}
$$
**证明。** 将 (256.17)--(256.18) 分别与 $\lambda_i,\mu$ 点乘后按独立变量 $v_j,\eta,\pi$ 收集，即得三个式子。它们对所有方向、所有对偶向量成立，故是完整伴随，而非仅在某组样本上成立。

特别地，$T_0^T$ 自动包含 $g_{r_j}-\omega_jg_{t_j}$；右端 core 梯度还要通过 $B_\xi^T\mu$ 加入一次。若实现已经把右端 core 梯度并入入口 r 行，不能再重复加第二次。

## 6. 固定权重与缩放后的算子

在一个当前模型和全部对应 trial 中，固定正对角行权重 $W_r$ 和正对角坐标尺度 S。它们仅定义优化的局部尺度，不替换原 RMS/BC 验收。

令
$$
b=W_r\mathcal R(q),\qquad
A=W_rJS^{-1}.
\tag{256.22}
$$
缩放变量 z 对应真实 reduced 方向
$$
d=S^{-1}z.
$$
算子与伴随必须配对为
$$
Az=W_rJ(S^{-1}z),\qquad
A^Tw=S^{-1}J^T(W_rw).
\tag{256.23}
$$
因为两个权重均为实对角阵，式中不额外转置；每个尺度出现一次。若 trial 时改用随试探状态变化的行权重，就不再是同一个局部 merit，其方向导数还包含权重的导数。当前算法必须如实保持模型内权重固定。

角频率权重可以帮助抑制高角导的大方向；core 的尺度应包括入口 $t_j=-\omega_jc_j$ 的额外频率成本。但任意声明为“优化惩罚”的正尺度都不自动是连续 $C^2$ 范数证书。本文的零点双射与下降证明只使用其正性和模型内固定性。

### 6.1 精确列范数的结构

对某个非入口物理坐标，其 weighted J 列分别出现在相邻 interval 的 $\mathsf R$、$\mathsf L$ 块以及末端的 $B_y$ 块；这些属于互不相同的残差行，列平方范数为各行贡献平方之和。

自由 core 的第 ell 列必须先计算
$$
(\mathsf L_0T_0)_{:\ell},
$$
再取带权平方范数，并加上右端 $(B_\xi)_{:\ell}$ 的带权平方范数。不能把入口 r 与 t 两个贡献分别平方再相加，否则会漏掉同一行中的交叉项。

global p 的第 ell 列包括每一个 interval 的 $(\mathsf P_i)_{:\ell}$ 和右端 $(B_p)_{:\ell}$，全部保留。最后再除以对应坐标尺度 $S_{\ell\ell}^2$，得到 A 的列平方范数。

这些只给对角预条件数据，不要求形成 $A^TA$。

## 7. 定理 R256-B：正阻尼模型的唯一解与下降条件

固定 $\lambda>0$，考虑完整线性最小二乘模型
$$
\min_z\;
\frac12\|Az+b\|^2+\frac{\lambda^2}{2}\|z\|^2.
\tag{256.24}
$$
**定理。** 该有限模型有唯一解 $z_\lambda$。若 $z_\lambda\ne0$，则 $d_\lambda=S^{-1}z_\lambda$ 是真实局部 merit
$$
\Psi(q')=\frac12\|W_r\mathcal R(q')\|^2
\tag{256.25}
$$
在 q 处的严格下降方向。

**证明。** 增广矩阵 $\binom A{\lambda I}$ 列满秩，因为其作用于非零 z 的范数至少为 $\lambda\|z\|$。故 (256.24) 严格凸、coercive，具有唯一解。

其一阶最优条件是
$$
A^T(Az_\lambda+b)+\lambda^2z_\lambda=0.
$$
这里只把此式用于证明；实现无需、也不应因此组装法方程矩阵。左乘 $z_\lambda^T$ 得
$$
\boxed{
b^TAz_\lambda
=-\|Az_\lambda\|^2-\lambda^2\|z_\lambda\|^2.
}
\tag{256.26}
$$
另一方面，因行权重固定且 $d_\lambda=S^{-1}z_\lambda$，
$$
D\Psi(q)[d_\lambda]
=b^TW_rJd_\lambda=b^TAz_\lambda.
\tag{256.27}
$$
若 $z_\lambda\ne0$，(256.26) 严格为负。证毕。

如果 $z_\lambda=0$，则 $A^Tb=0$：这是该 weighted residual 的驻点条件，不能一般推成 $\mathcal R=0$。只有另有 J 可逆等适用条件，才能进一步推出 b=0。正阻尼使局部模型唯一，并不证明原非线性系统可解、其 Jacobian 可逆或某个驻点就是解。

### 7.1 同一未阻尼模型预测

对正方向 trial $q+\alpha d$，未阻尼残差模型的预测下降为
$$
\mathrm{pred}(\alpha)
=-\alpha\,b^TAz-\frac{\alpha^2}{2}\|Az\|^2.
\tag{256.28}
$$
这里不把阻尼惩罚加进真实非线性 merit。

对精确解 $z_\lambda\ne0$，使用 (256.26)，在 $0<\alpha\le1$ 时
$$
\mathrm{pred}(\alpha)
=\alpha\left[
\left(1-\frac\alpha2\right)\|Az_\lambda\|^2+
\lambda^2\|z_\lambda\|^2\right]>0.
\tag{256.29}
$$
如果 q 位于共同合法域的内部，则由连续性，充分小的 alpha 使全部原查询仍在域内。由 (256.27) 和可微性，
$$
\frac{\Psi(q)-\Psi(q+\alpha d_\lambda)}
{\mathrm{pred}(\alpha)}
\longrightarrow1\qquad(\alpha\downarrow0).
\tag{256.30}
$$
这是精确有限模型的局部存在性结论。它不给一个有用大小的 alpha，不保证预设有限回溯次数足够，也不保证下降超过浮点噪声门槛。

## 8. 显式增广 LSMR 与列预条件不改变该惩罚

定义
$$
D_{\ell\ell}
=\sqrt{\|Ae_\ell\|^2+\lambda^2}>0.
$$
用新求解变量 t 写 $z=D^{-1}t$，则 (256.24) 等价于
$$
\min_t\left\|
\begin{pmatrix}A\\\lambda I\end{pmatrix}D^{-1}t
-
\begin{pmatrix}-b\\0\end{pmatrix}
\right\|^2.
\tag{256.31}
$$
因此可以只给 LSMR 正向与伴随：
$$
t\mapsto
\binom{A(D^{-1}t)}{\lambda D^{-1}t},
$$
$$
\binom uv\mapsto D^{-1}(A^Tu+\lambda v).
\tag{256.32}
$$
全过程不构造法方程。LSMR 在这个显式增广算子上使用额外 damp=0；阻尼已在下方 $\lambda I$ 中完整出现。求解后必须依次恢复
$$
z=D^{-1}t,\qquad d=S^{-1}z.
\tag{256.33}
$$
若把右预条件后的 t 直接作为物理方向，或再次给错误变量加同名阻尼，得到的是另一个模型，不能沿用上节证明。

这里“等价”指精确最小化问题。有限次数 LSMR 只返回其迭代近似；预条件虽不改变精确问题，仍会影响截停误差。不能由模型唯一性推断实际返回方向已达到其最优条件。

## 9. 实际截停方向必须重新测量

对实际返回的任意近似 z，代码应直接计算
$$
g_{\rm dot}=b^TAz,\qquad \|Az\|^2,
$$
以及 (256.28)，而不假定 (256.26) 已数值成立。只有有限、严格负的 $g_{\rm dot}$ 才给当前线性模型的下降方向；真实 trial 还必须重新计算原节点 RHS、真实 Hermite 中点、原右端及需要的 RMS 域。

对每个 trial，使用模型开始时固定的同一个 $W_r$，求
$$
\mathrm{ared}
=\frac12\|b\|^2-\frac12\|W_r\mathcal R(q+\alpha d)\|^2,
\qquad
\mathrm{ratio}=\frac{\mathrm{ared}}{\mathrm{pred}}.
\tag{256.34}
$$
只接受正预测、合法真实域和足够正的实际下降，是一种明确的 warm 全局化规则。例如当前实现的 ratio 门槛、有限 alpha 序列及舍入下降 floor 都应如实记录；它们是优化算法选择，并非新的 full-DN 科学验收。

完整导数实现的独立检查可以直接对原 collocation_fun 做合法 complex 方向微分，包含重新求节点 RHS 和由它构造的非线性 midpoint。若检查自由 core 与 global p，应先通过真实方向 map (256.9) 把它们提升到全部增广节点，不能把 complex 坐标送进会强转 float 的 pack/expand 接口。伴随恒等式检查与同一 L/R action 对照有价值，但不能独自排除所有正向链式错误。

若只在极小 alpha 才有限、或阻尼很大导致实际下降低于可靠分辨率，就应记录停滞。有限迭代预算下没有进展不等于不可解；有少数进展也不等于已满足原方程。

## 10. 本结果在当前主线中付清和未付清的事项

本结果付清：

- 对固定实际有限 RHS、同一右端算子和共同合法域，精确约束坐标没有丢失或增加原全部方程的零点；
- 原非线性 Hermite midpoint 的完整状态及 global-control Jacobian 链式；
- 自由入口 core、所有非入口完整物理节点、global p 的完整 action 与 adjoint；
- 固定正权重、正阻尼模型及其显式列预条件的精确等价性；
- 精确非零阻尼方向的下降结论，以及实际近似方向必须测量的量。

本结果不付清：

- 任何实际 LSMR 截停的最优性或全过程收敛；
- 新 H 已有真实非线性 native 尾解；
- affine 右端零点已经满足真实 DN；
- 原完整 BVP 的 RMS、BC、fresh native 与最终 audit 门；
- 某个 warm 已是 accepted field、同一 g 精化已完成，或闭面幅度、reach、marker 刚性排除已完成。

因此 warm 产物必须保持未接受身份。只有后续原 full-DN 流程按其真实新 H、同一完整状态和全部原容差实际通过，才可以取得该流程自己的接受结论。R256 不代替这一步。

