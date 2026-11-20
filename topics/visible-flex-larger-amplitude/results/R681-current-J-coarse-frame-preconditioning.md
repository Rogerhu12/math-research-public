# R681. 当前 J 的 coarse 正交框架、完整正谱角矩与原 QP 的预条件

日期：2026-11-20。会话：Astra-larger-resume-24b2ab87-20261120 / fullclosed_solver。

**状态：完整代数结论与具体源码调查；没有新数值、fixture、预条件运行或预排任务。** 本条不宣称预条件不足已经是当前实际瓶颈。是否采用，仍由已排纯报告诊断中的固定面历史、模型能量和真实拒步原因决定。

相对 [R677](R677-low-damping-fixed-face-CG-and-reliable-updates.md)，新增的是三个可直接实现的结构：完整增广坐标中可用于当前数据 Hessian 的物理 coarse 框架；非理想白化时仍保持零场核正交补的小 Gram 修正；以及只用当前六分量谱张量的有限阶角矩，组装全部 coarse 数据 Hessian。[R654 §5–6](R654-complete-integrated-H2-norm-and-endpoint-spectrum.md)已经证明 DI 最小表示、白化列在母坐标中正交及增广商范数的二分之一至一界，本条直接沿用这些结论，不把它们重新登记为新结果。以下构造不需要扫约 133 万个单位坐标，也不把完整空间换成 coarse 空间。

## 1. 原问题与准确母范数

继续使用相同真实父、全部原变量和有限 metric 行。记完整 QP 为

$$
q(z)=\frac12\|Az+v\|^2+\frac{\mu^2}{2}\|z\|^2,
\qquad Cz\le b,
\qquad H=A^TA+\mu^2I.
\tag{1}
$$

其中 $A$、虚拟右端 $v$ 保留 R664 的真正正谱 residual-Hessian 与真正半梯度关系。预条件器只用于选择同一 QP 的搜索方向，不更改 $A,v,C,b,\mu$ 或最后的原坐标欧氏罚项。所有永久位置仍参加真实非线性筛选。

令 $S$ 为已声明的 DI 正尺度，$\Pi$ 为完整端口矩阵在缩放坐标中的欧氏正交投影。令 $A_H$ 为已刊物理高度三角映射。定义

$$
\mathcal L=A_H\,\mathrm{DI.lift},\qquad
\mathcal I x=S^{-1}\,\mathrm{DI.inverse}(A_H^{-1}x;\mathrm{affine=false}).
\tag{2}
$$

这里 $\mathcal L$ 的输入仍有完整端口冗余槽；$x$ 是原物理自由步。沿用 R654 的准确逆/投影结论，并与已刊可逆高度映射复合，

$$
\mathcal L\mathcal I=I,\qquad
\mathcal I\mathcal L=\Pi,\qquad
\operatorname{range}\mathcal I=\operatorname{range}\Pi.
\tag{3}
$$

因此当前未附加 coarse 的母范数是 $\|x\|_N^2=\|\mathcal I x\|^2$。式(3)只使用全部 A/E/D、准确自由端口和高度三角映射；它没有把 E/D 置零。

设 $B$ 为当前 literal coarse 列，$G_N=B^TN B$。当前 `angular_h2_coordinates.coarse_norm` 的源码准确流程是

$$
D=\operatorname{diag}\sqrt{\operatorname{diag}G_N},\quad
L_NL_N^T=D^{-1}G_ND^{-1},\quad
R=D^{-1}L_N^{-T},\quad U=BR.
\tag{4}
$$

**当前源码没有 ridge、jitter、特征值截断或列删除。** 准确算术中 $R^TG_NR=I$。它另做一个实际 literal inverse/scale 探针对照；该浮点探针不等于机器中逐项严格正交的证明。本条第 3 节覆盖一般非正交的实际小 Gram。

完整 solver 的方向映射是

$$\mathcal T=[\mathcal L,U],\qquad A=\mathcal J\mathcal T,$$

其中 $\mathcal J$ 是在当前父冻结的、已含径向/角轨道/正谱和 `1600/C0` 外尺度的原自由步数据算子。

## 2. 当前准确白化下的物理 coarse 框架

定义 $Q=\mathcal I U$。由(3)–(4)，

$$Q^TQ=I,\qquad \Pi Q=Q,\qquad \mathcal LQ=U.$$

于是

$$
W=\frac1{\sqrt2}\begin{bmatrix}Q\\I\end{bmatrix},
\qquad W^TW=I,
\qquad \mathcal TW=\sqrt2U.
\tag{5}
$$

令 $A_c=\mathcal JU$，$G_c=A_c^TA_c$。则

$$AW=\sqrt2A_c,\qquad W^THW=2G_c+\mu^2I.\tag{6}$$

这个 $W$ 是当前完整冗余坐标中的物理 coarse 子空间。**单独取最后的 coarse 系数槽，不是同一个正交物理框架。** DI 槽已经能表达同一物理方向，附加 coarse 槽使其可被两份坐标共同表示；式(5)保留了这个重复结构的准确因子。

此外，若 $(u,a)\in\ker\mathcal T$，则 $\Pi u=-Qa$，所以

$$W^T(u,a)=(Q^Tu+a)/\sqrt2=0.$$

因此 $\operatorname{range}W\subset(\ker\mathcal T)^\perp$。只在这个框架上作对称 coarse 预条件不会把准确的零场核混入原零起步 Krylov 过程。这个结论比“最后若干坐标做一块 Jacobi”更强。

## 3. 一般非正交 Q 的小 Gram 修正

若把实际给定的白化矩阵视为 literal 矩阵，或未来另用非理想白化，令

$$K=Q^TQ\succ0.$$

仅将 $(Q,I)$ 按 $I+K$ 正规化虽能得到正交列，却一般不再与 $\ker\mathcal T$ 正交。保持两个性质的正确选择是

$$
V=\begin{bmatrix}Q\\K\end{bmatrix},\quad
E_c=K+K^2=L_cL_c^T,\quad
W=V L_c^{-T}.
\tag{7}
$$

直接计算给 $W^TW=I$。对任意零场向量仍有

$$V^T(u,a)=Q^Tu+Ka=-Ka+Ka=0.$$

又有

$$
\mathcal TW=U(I+K)L_c^{-T},\qquad
H_c:=W^THW=
L_c^{-1}(I+K)G_c(I+K)L_c^{-T}+\mu^2I.
\tag{8}
$$

当 $K=I$ 时退化为(5)–(6)。$K$ 不必由巨大 $Q$ 显式形成：

$$K=R^T G_N R.$$

这里 $G_N$ 应按实际 literal coarse 的 inverse/scale 分离式重新取得，不能只从已经算出的 Cholesky 因子反向定义一个必然接近恒等的矩阵再把它称作独立母范数核对。现有 `coarse_norm` 在形成因子之前已有完整 $G_N$；后继可保留该小矩阵，不需要调用场或 J。

式(7)是准确线性代数定理。实际浮点仍须记录小 Gram/Cholesky 与框架误差，不能把理论恒等式写成向外舍入结论。若数值分解失败，可以保留原 solver 和原 QP，记录本方向未使用该预条件；不应以静默 jitter 更改母范数或把分解失败称为物理不可行。

## 4. Q 与转置的线性成本实现

不需要保存尺寸约为 `integrated_variables × coarse_variables` 的 $Q$。正向直接用既有接口：

$$Qa=S^{-1}\,\mathrm{DI.inverse}(A_H^{-1}BRa;\mathrm{affine=false}).$$

反向只缺一个局部差分转置。将 $w=S^{-1}u$ 按 DI 的 core/A/E/D/H 布局分开。对

$$E_i=(U_{i+1}-U_i)/h_i-(A_i+A_{i+1})/2,$$

$$D_i=(Y_{i+1}-Y_i)/h_i-(U_i+U_{i+1})/2,$$

inverse 的转置由以下累加准确给出：

- A：初始 A covector，再向左右节点各减 $E_i^*/2$。
- U：向右加 $E_i^*/h_i$、向左减同项，再向左右各减 $D_i^*/2$。
- Y：向右加 $D_i^*/h_i$、向左减同项。
- core：直接 core covector 加 $g_{Y_0,R,\nu}-\nu g_{Y_0,T,\nu}$，只取原自由 core 模；其余固定端口 covector 丢弃。
- H：保留其单独 covector。

随后作 $A_H^{-T}$，即 H covector 减去 $v_q^Tg$；再用现有 $B^T$ 和 $R^T=L_N^{-1}D^{-1}$。这就是 $Q^Tu$，不是另一个度量下的转置。

因此(7)的正向只需 `Q.apply(c)` 和小矩阵 `K@c`，反向只需 `Q.transpose(u)+K@a`，以及 $L_c$ 的小三角求解。全维存储是若干现有长度向量，附加密集存储只有 coarse 阶小矩阵。它不需要对任何原变量的单位向量作 J/JT 探测。

## 5. 当前完整 coarse 数据 Hessian 的六分量张量

需要的是当前父的 $G_c$，不能使用别的父的矩阵、旧 Jw 权矩或 v7 的旧范数白化来替代它。

先核当前 `physical_subspace_v3.free_direction`：每个 coarse 列的 leading free-core-c 槽都是零。名为 `global_core_second_jet` 的列是允许的初端 A0_xy 变化，**不是** core 位置系数 $c_\nu$ 变化。所有这些 A0 列都进入当前 nodal 三 jet 和观察权。这使 coarse 限制中 $\rho$ 与解析转角不变；完整 DI 部分仍保留所有 core-c 自由变量。

先在固定 Cartesian 坐标中写 $V_{\rm cart}=F_s$、$d_{\rm cart}=F_\phi$、$r=a\rho$。对这类 coarse 方向，三个 raw Gram 分量的导数是

$$
\mathsf D_{\rm cart}
\begin{bmatrix}\delta V_{\rm cart}\\\delta d_{\rm cart}\end{bmatrix},\qquad
\mathsf D_{\rm cart}=
\begin{bmatrix}
2V_{\rm cart}^T&0\\
d_{\rm cart}^T/r&V_{\rm cart}^T/r\\
0&2d_{\rm cart}^T/r^2
\end{bmatrix}.
\tag{9}
$$

令 $L_{s\phi}$ 是 R664 在同一实际 raw Gram 冻结的正谱三乘三块。Cartesian 六乘六张量为

$$\mathsf S_{\rm cart}=\mathsf D_{\rm cart}^TL_{s\phi}\mathsf D_{\rm cart}\succeq0.\tag{10}$$

**有限阶角矩必须先转到随 $\phi$ 旋转的 R/T/Z 分量。** 明确定义

$$
e_R(\phi)=(\cos\phi,\sin\phi,0)^T,\quad
e_T(\phi)=(-\sin\phi,\cos\phi,0)^T,\quad e_z=(0,0,1)^T,
$$

$$
\mathcal R(\phi)=[e_R(\phi),e_T(\phi),e_z],\qquad
O(\phi)=\operatorname{diag}(\mathcal R(\phi),\mathcal R(\phi)),
$$

$$
V_{\rm loc}=\mathcal R^TV_{\rm cart},\quad
d_{\rm loc}=\mathcal R^Td_{\rm cart},\quad
\mathsf D_{\rm loc}=\mathsf D_{\rm cart}O,\quad
\mathsf S_{\rm loc}=O^T\mathsf S_{\rm cart}O
=\mathsf D_{\rm loc}^TL_{s\phi}\mathsf D_{\rm loc}.
\tag{10a}
$$

$\mathsf D_{\rm loc}$ 也就是把(9)中的 $V_{\rm cart},d_{\rm cart}$ 换成 $V_{\rm loc},d_{\rm loc}$。共轭变换只改分量表示，原场的全部 M 模、当前解析 lift 与正谱块完整保留。若直接对 Cartesian $\mathsf S$ 取后文阶数 0 到 $2m_c$ 的矩，会遗漏 $e_R,e_T$ 自身的角依赖；不能省略(10a)。

现有 complete operator 的 `physical_jet` 和缓存本来就按 `rotating-phi orthonormal frame` 提供分量，coarse 的 `h/dh` 也用这一约定。因此实际接线可直接用其 $V_{\rm loc},d_{\rm loc},\rho$ 缓存和 `bridge.blocks` 构造 $\mathsf S_{\rm loc}$，不必先回 Cartesian，更不能再重复旋转一次。不得把 $L$ 换成先前 R660 的 K 梯度权，也不得额外乘一次 cross 的 $\sqrt2$。

当前 v7 的 `spectral_evaluate` 正是用等价的 `(radial velocity channel, radial position channel)` 角矩累加全部 coarse 正规矩阵；其返回矩阵已经乘 $k/\mathrm{scale}^2$，还需除 $C_0$ 才与完整 normalized QP 同单位。若复用它的 raw coarse 矩阵，最后仍必须用当前完整 solver 的 $R$，而不是 v7 的另一个物理范数 `norm_right`。

R671 特别要求当前缓存确实来自其 h/f/k 工厂：固定 $k'$ 已影响当前 $V_{\rm loc}$，不能在(9)–(10a)中漏掉。高度列必须按真实 observation weights 从 **nodal** $b-h$ 三 jet 重建后，再加实际解析 $h,h'$。一般它等于

$$\operatorname{Hermite}_{\rm mesh}(b-h)+h,$$

不能在过渡段直接换成理想 $b$。母范数中采用的 $\int b''{}^2=120/(7S^3)$ 仍只是此前声明的高度尺度，不因此变成真实场的精确 bending energy。

如果未来 coarse 真正加入非零 $\delta c$，则(9)还须加入 $\delta\rho$ 和解析转角链；本条不把当前零 core-c 的专用角矩冒成任意新 coarse 的完整公式。

## 6. 有限角矩替代逐列 J 扫描

令 $E_R,E_T,E_Z$ 为 moving 分量空间的三个**固定坐标单位向量**，不是 Cartesian 中随 $\phi$ 变化的 $e_R,e_T,e_z$。当前 coarse 最大角模为 $m_c$。其 moving 基函数 $h^{\rm loc}=\mathcal R^Th^{\rm cart}$ 与实际 Cartesian 角导数的 moving 分量满足

$$
h_{,\phi}^{\rm loc}:=\mathcal R^T\partial_\phi h^{\rm cart}
=\partial_\phi h^{\rm loc}+\Omega h^{\rm loc},\qquad
\Omega=\mathcal R^T\mathcal R'
=\begin{bmatrix}0&-1&0\\1&0&0\\0&0&0\end{bmatrix}.
$$

这里 $h_{,\phi}^{\rm loc}$ 不是仅对 moving 分量作普通微分。代入得到

$$
h_R^{\rm loc}=E_R\cos(2m\phi),\quad
h_{R,\phi}^{\rm loc}=-2m E_R\sin(2m\phi)+E_T\cos(2m\phi),
$$

$$
h_T^{\rm loc}=E_T\sin(2m\phi),\quad
h_{T,\phi}^{\rm loc}=-E_R\sin(2m\phi)+2m E_T\cos(2m\phi),
$$

$$h_Z^{\rm loc}=E_Z\cos(2m\phi),\quad h_{Z,\phi}^{\rm loc}=-2m E_Z\sin(2m\phi).$$

上述分量系数才只是 $\cos(2m\phi),\sin(2m\phi)$ 的一项或两项组合；基底旋转的单位项已经包含在 $\Omega h^{\rm loc}$ 中。在每个 radial stage，**对(10a)的 $\mathsf S_{\rm loc}$** 的 21 个对称分量形成

$$
C_{ij,k}=\sum_\phi m_\phi\,(\mathsf S_{\rm loc})_{ij}(\phi)\cos(2k\phi),\quad
S_{ij,k}=\sum_\phi m_\phi\,(\mathsf S_{\rm loc})_{ij}(\phi)\sin(2k\phi),
\quad 0\le k\le2m_c.
\tag{11}
$$

这里 $m_\phi$ 是原 quarter 算子的准确轨道倍数，只付一次。所有角点仍进入求和。由逐点乘积化和差，任意 coarse 角矩只用这些数，例如

$$\sum m_\phi\,s(\phi)\cos(2m\phi)\cos(2n\phi)
=\tfrac12(C_{|m-n|}+C_{m+n}),$$

$$\sum m_\phi\,s(\phi)\sin(2m\phi)\sin(2n\phi)
=\tfrac12(C_{|m-n|}-C_{m+n}),$$

$$\sum m_\phi\,s(\phi)\cos(2m\phi)\sin(2n\phi)
=\tfrac12(S_{m+n}+\operatorname{sgn}(n-m)S_{|n-m|}).\tag{12}$$

交换 sin/cos 时交换差频的符号。$m=0$ 也由这些式子准确处理。

因此可以一次批量小矩阵乘积形成(11)，再以(12)恢复全部 $(2n_c)\times(2n_c)$ velocity/position 通道矩；此处 $n_c=2+3m_c$ 是角通道数，并非完整 coarse 的列数。当前 $m_c=12$ 时只需阶数 0 到 24。这个“有限阶”针对 moving 测试列分量的乘积，不是截断当前场：原场的全部 M 模、完整解析 lift、当前正谱权和所有观察点都留在 $\mathsf S_{\rm loc}$ 的实际点值中。直接在给定角点作(11)时，证明只依赖逐点恒等式，不需要假设 $\mathsf S_{\rm loc}$ 是带限函数。

最后按 literal radial 三 jet 的 $u_\ell(s),y_\ell(s)$ 组装

$$
N_{\ell j}=\gamma\sum_s w_s
\{u_\ell u_j K^{uu}+u_\ell y_j K^{uy}
+y_\ell u_j K^{yu}+y_\ell y_j K^{yy}\}_{\ell j},
\quad
\gamma=\frac{k}{\mathrm{scale}^2 C_0},
\tag{13}
$$

并置 $G_c=R^TNR$。只在当前 basis 的实际非零 radial 列上累加可节省算量，但每个原 stage 的正权都保留。式(13)与当前完整正谱 J 的 coarse 限制准确相同；没有使用虚拟右端的平方冒充 Phi。

算法复杂度从逐stage约 $N n_c^2$ 的大角积，变成约 $21N(2m_c+1)$ 的有限矩及小通道代数；系数 21 在显式同时算 cos/sin 时再乘二。径向累加和 coarse 密矩阵分解仍有实际成本，不能写成零成本。

## 7. 一个完整 SPD 预条件器与合法 PCG

用(7)或当前理想特例构造 $W$，用(8)形成 $H_c\succ0$。令 $\beta>0$ 是本次 QP 固定的背景逆尺度，$P_W=I-WW^T$。定义

$$\mathcal B=\beta P_W^2+WH_c^{-1}W^T.\tag{14}$$

对任意非零 $x$，

$$x^T\mathcal Bx=\beta\|P_Wx\|^2+(W^Tx)^TH_c^{-1}(W^Tx)>0.$$

因为若两项同为零，$W^Tx=0$ 且 $P_Wx=x=0$，矛盾。这个 SPD 论证甚至不要求一个浮点实现的 $W$ 逐项严格正交；要求正向/转置是同一声明线性映射的互转置，且小解是 SPD 解。准确正交时 $P_W^2=P_W$，并有 $W^T\mathcal B^{-1}W=H_c$。该框架上的压缩准确白化，而补空间保留完整维数。

当前独立活动面的原欧氏投影为 $P$。在固定面上取

$$p=Pg,\quad y=P\mathcal Bp,\quad d=-y.$$

则 $d$ 切向，且 $g^Td=-p^T\mathcal Bp<0$。仍按 R677 的同一全部不等式可行线步推进。对于未截断、活动面和 $\mathcal B$ 都未变的步，已付 $Hd$ 给

$$\beta_H=\frac{y_+^THd}{d^THd},\qquad d_+=-y_++\beta_Hd,\tag{15}$$

从而 $d_+^THd=0$，$g_+^Td_+=-p_+^T\mathcal Bp_+<0$。在准确算术下这是相应 PCG 递推。仍可保留原欧氏 $\|Pg\|$ 作为停止和报告尺度；不能把旧 Euclidean FR 系数与新的 PCG 残差内积混用。

有限精度下降保护若按新方向度量写，应比较 $p^T\mathcal Bp$，而非把另一尺度的数直接塞入旧阈值。发生真实面改变或重建预条件器时重启。R668 提前释放的第一步继续使用原准确 Euclidean 向内方向并核实际符号；不直接假设预条件后的新面梯度仍朝被释放行内侧。全部原目标、阻尼和线性/非线性几何接受条件保持。

若需要用当前数据固定 $\beta$，一个不用额外 J 乘积的明示候选是：先完成一次原 solver 已付的正长度推进，记录该方向的 Rayleigh 值

$$\sigma=\frac{\|Ad\|^2+\mu^2\|d\|^2}{\|d\|^2}>0,\qquad \beta=1/\sigma,$$

随后只重启一次并在本次 QP 内固定它。它提供当前方向的真实单位，不证明整个补空间的谱都在 $\sigma$ 附近，也不是自动选出的最优预条件参数。现在没有启用这个候选。

## 8. 能保证什么，不能保证什么

本条保证原问题不变、预条件 SPD、当前活动面合法下降、准确 coarse 压缩和可实现的矩阵成本。它**没有**从这些性质推出总条件数必下降。

相对 $W$ 与其正交补，预条件后仍存在 coarse/fine 非对角耦合；未建模补空间的谱也可能与背景尺度相差很大。仅将 coarse 压缩白化不能消除这些量。默认把背景逆尺度一律设为 $\mu^{-2}$，也可能放大并非弱方向的补空间。因此不能在没有实际 Hessian 能量/历史前，把一个未经判断的背景尺度包装成改进结论。

还应避免一个表面“免费”的重复方案：在恒定活动面、准确算术和同一 H 下，只回收当前未重启 CG 已付的 Krylov 方向及其 H 像，若后继所有操作仍局限于已有 Krylov 空间加每次一次新 $PHP$ 扩展，便没有超出同等乘积数普通固定面 CG 的搜索空间。普通 CG 已在该空间最小化 q，不能由这些数据另造一个准确算术下严格更优的解。这类回收可以修复重启丢失或有限精度，也可能在面改变后有用；前一种正是 R677 已处理的方向，不能再作为本条新加速的保证。

式(11)–(13)提供的是**独立的实际 J 结构信息**，由全观察点的局部张量直接组装，不依赖已付 Krylov 方向，也不靠逐变量探测。这是本条相对“再加 CG 预算”的实质差别。

若实际慢方向主要在 coarse 补空间，本条也明确指出下一层可用结构：固定 core-c 时，完整 q 的同频 R/T/Z 三 jet 只耦合相邻 radial 节点；当前六张量可形成每频率的 block-banded 数据近似，母范数 A/E/D 也是相邻节点二次型。H 是 Z0 的全局 border，真正 core-c 还需保留其完整解析链和相应 border。不同频率之间的耦合若在预条件中略去，只能声明近似，原全 H 乘积仍保留。该较大接口现在未实现，也未作为新预算启动条件。

## 9. 实际资源与最小接线

当前 full 的 coarse 维数是 2534；一个 double coarse 密矩阵约 51.4 MB。并不保存约 `1.33M × 2534` 的 Q。每个 Q/QT 使用局部差分、原 B 与其转置，以及长度为当前完整变量数的工作向量。小 Gram、正谱 coarse normal 和因子需要有限个 coarse 密矩阵，必须在实际报告中分别记录峰值，不能从这个单矩阵数推断完整进程峰值。

角矩可按现有 stage block 流式生成：缓存实际 $V_{\rm loc},d_{\rm loc},\rho$ 与 R664 block，形成 $\mathsf S_{\rm loc}$、有限 cos/sin 矩、radial 累加。若输入缓存为 Cartesian，则必须先按(10a)变换。无需新的完整 J/JT 单位列调用；但这仍是一次新的数值组装，科学执行仅在公开 Actions，不由本条纸证冒成已运行。

最小后继接口可以是三个互相分开的对象：

1. `CoarseFrame`：给出 Q/QT、K、W/WT 和实际母范数/白化身份。
2. `current_coarse_data_gram`：消费同一次完整父的原观察缓存、R664 正块和真实 stage 列，按(11)–(13)返回 $G_c$ 与已用源/模型/权身份。
3. `FixedSPDPreconditioner`：冻结 $\mu,\beta,W,H_c$，只提供 `apply(vector)` 和实际准备元数据；PCG 的 H 和所有接受检查仍调用原完整算子。

这三者不应在导入时执行，不应另增 fixture 门。若后继采用，新的真实方向必须记录构造成本、当前父/源、原和新模型目标是否同一、实际迭代/重启/释放、同一 alpha 的真实回溯及全部永久点结果。现在仅完成定理和源码调查，尚无可运行的新 PCG driver。

## 10. 本次实际读过的源码身份

| 源 | SHA256 | 本条用途 |
|---|---|---|
| `notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py` | `d429d68baded58908454e49f4bfdf8e43ce9d3f857ed666eafa95c1c366462db` | 完整端口、inverse 与投影 |
| `scripts/resume_20261120/physical_height_coordinates.py` | `f26738f9ee5a27ec861a9a9cbdc99b301edb6c6b3b271320e567a3892fab5f0e` | 物理高度三角映射 |
| `scripts/resume_20261120/angular_h2_coordinates.py` | `11fd0b8c3bc8139cbce19374cc81ba73b47bddecb007eed3cd296285951c298b` | 当前母范数与无 ridge 白化 |
| `scripts/resume_20261120_physical_subspace_v3.py` | `118e1a89745988c06ecf89c392b84f7e47397f58aad86f90c3efff2c401ffae8` | literal 全 coarse 列及零 core-c 槽 |
| `scripts/resume_20261120_curvature_qp_v3.py` | `3131377740b06ff400b1a74e3efe349c987769c4c4d3c2cbf40ea40ad9c9308e` | 原 nodal 列在所有观察行的真实重建 |
| `scripts/resume_20261120_curvature_qp_v7_spectral_hessian.py` | `702c9e13db661d39771aa673dca7c19120c695da16556919e63918705b038ec8` | 当前正谱 coarse 角矩公式，不复用它的旧范数 |
| `scripts/resume_20261120/positive_spectral_gram_hessian.py` | `29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4` | R664 正块、真正梯度与外尺度 |

源码身份来自文件字节读取；本次没有导入这些科学模块，没有数值试算，没有更改冻结源，也没有创建新运行计划。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
