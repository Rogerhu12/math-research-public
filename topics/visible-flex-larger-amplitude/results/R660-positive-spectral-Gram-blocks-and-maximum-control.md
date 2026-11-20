# R660：正谱 Lp 的完整 Gram 块权、原全空间正规算子及最大误差界

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

**状态：完整数学证明。** 给当前全部相对 Gram 行一个严格正的谱 $L^p$ 目标，证明其与有限最大算子范数的上下界、准确 $3\times3$ 块权、全变量 $J^\top KJ$ 与目标梯度，以及可供原 LSMR／粗 QP 消费的正向、转置。该目标改变优化侧重点，不改变 g、不删行、不截模。它不把冻结二次模型误当 $p>2$ 时的上界，也不把有限 $L^p$ 数值当作连续 metric 证书。

普通数值的小模型检查及一次22列同像诊断另记于 [实际谱目标接口与试验](../notes/2026-11-20-positive-spectral-Gram-interface-and-trial.md)；此条不宣布新的主线父。

## 1. 准确有限目标和归一化

对每个保留的径向／角观察块 i，记同 g 的相对 Gram 矩阵为

$$
E_i(x)=
\begin{pmatrix}e_i&f_i\\f_i&g_i\end{pmatrix},\qquad
r_i=(e_i,f_i,g_i)^\top.
$$

x 可取原完整仿射自由坐标，也可代入任何已有粗空间。每个 i 都保留，取准确正权 $\nu_i>0$、$\sum_i\nu_i=1$。固定偶数 $p=2k\ge2$、$\epsilon>0$ 和尺度 $c>0$，定义

$$
\Phi_{p,\epsilon,c}(x)=
\sum_i\nu_i\operatorname{tr}
\left({E_i(x)^2+\epsilon^2I\over c^2}\right)^k. \tag{1}
$$

若 $\lambda_{i,1},\lambda_{i,2}$ 是 E 的两个真实特征值，

$$
\Phi_{p,\epsilon,c}
=\sum_i\nu_i\sum_{a=1}^2
\left({\lambda_{i,a}^2+\epsilon^2\over c^2}\right)^k. \tag{2}
$$

定义未缩放幂目标及平滑谱范数

$$
\Psi_{p,\epsilon}=c^p\Phi_{p,\epsilon,c},\qquad
L_{p,\epsilon}=c\,\Phi_{p,\epsilon,c}^{1/p}. \tag{3}
$$

**本文所有带 $\Phi$ 的数值公式都保留 c；不能把 c=.05 的归一化目标直接代入未缩放 $\Psi$ 的公式。**

对所有允许的x，目标共有准确下界

$$\Phi_0=2(\epsilon/c)^p.$$

每项均至少 $(\epsilon/c)^p$；全部权严格正，故等号当且仅当所有 $E_i=0$。在自由残差矩阵空间中，该下界可以达到；当前受约束场模型是否存在达到它的x仍未证明。上述等号条件只说明平滑不会改动全部原观察行的零集。原 g、a、材料角及原仿射自由空间均未改变。

epsilon、p、c 和基础 $\nu_i$ 必须在一次方向的真实回溯中固定。若后续迭代另选参数，须另记其目标，不能将不同参数的 $\Phi$ 数值直接比较。原加权平方和与直接 maxGram 可同时保留，便于比较相同物理目标误差。

## 2. 与有限最大算子范数的严格关系

令

$$M=\max_i\|E_i\|_{\mathrm{op}},\qquad \nu_{\min}=\min_i\nu_i>0.$$

每个特征值绝对值不超过 M，所以

$$\Phi\le2\left({M^2+\epsilon^2\over c^2}\right)^k.$$

在取得 M 的某个 i／特征值上，其单项已有权至少 $\nu_{\min}$，故

$$\Phi\ge\nu_{\min}\left({M^2+\epsilon^2\over c^2}\right)^k.$$

解得

$$
\boxed{
\sqrt{\max\left\{0,\ c^2(\Phi/2)^{1/k}-\epsilon^2\right\}}
\ \le M\le\
\sqrt{c^2(\Phi/\nu_{\min})^{1/k}-\epsilon^2}.
} \tag{4}
$$

右端根内非负：由 $\Phi\ge2(\epsilon/c)^p$ 及 $\nu_{\min}\le1$ 即得。用未缩放 $\Psi=c^p\Phi$，等价为

$$
\sqrt{\max\{0,(\Psi/2)^{1/k}-\epsilon^2\}}
\le M\le
\sqrt{(\Psi/\nu_{\min})^{1/k}-\epsilon^2}. \tag{5}
$$

这是有限观察集合的准确关系；权很小时上界可以很松。它不能用来跳过真实 maxGram 读取，也不支付径向／角样点之间的误差。连续范围仍由 [R657](R657-complete-closed-relative-Gram-and-same-scalar-enclosure.md) 等完整连续核支付。

固定正权与 epsilon 时，有限求和的 $p$ 次方根随 $p\to\infty$ 收敛到 $\sqrt{M^2+\epsilon^2}$，因为最大项下界的权因子 $\nu_{\min}^{1/p}\to1$，双特征值上界因子 $2^{1/p}\to1$。这给谱目标强调大特征值的准确含义，不要求实际计算把 p 无限增大。

## 3. 严格正的冻结权与准确三分量矩阵

固定基点 $x_0$，令

$$
W_i=\left({E_i(x_0)^2+\epsilon^2I\over c^2}\right)^{k-1}. \tag{6}
$$

W 是对称正定矩阵，并与 $E_i(x_0)$ 交换。其两个特征值为

$$
\left({\lambda_{i,a}(x_0)^2+\epsilon^2\over c^2}\right)^{k-1}
\ge(\epsilon/c)^{p-2}>0.
$$

写 $W=\begin{pmatrix}u&v\\v&w\end{pmatrix}$。对任意真实对称 $R=\begin{pmatrix}e&f\\f&g\end{pmatrix}$，

$$
\begin{aligned}
\operatorname{tr}(WR^2)
&=u e^2+(u+w)f^2+w g^2+2vef+2vfg\\
&=r^\top K r,\qquad
K=
\begin{pmatrix}
u&v&0\\
v&u+w&v\\
0&v&w
\end{pmatrix}. \tag{7}
\end{aligned}
$$

因此不是简单地对三个分量各乘一个经验权，也不能在 K 外再乘一次混合项的 $\sqrt2$。p=2 时 W=I，准确回到 K=diag(1,2,1)，即原 Frobenius 目标。

若 $\mu I\preceq W\preceq LI$，则 $R^2$ 半正定，故

$$
\mu(e^2+2f^2+g^2)
\le r^\top Kr\le
L(e^2+2f^2+g^2). \tag{8}
$$

特别地 K 正定，全部原三分量方向都保留。也可直接由 Sylvester 判据验证：

$$u>0,\quad u(u+w)-v^2=u^2+\det W>0,\quad
\det K=(u+w)\det W>0.$$

这支付正权，而非仅在一个样本上观察到正特征值。实现若因参数过小而在浮点 Cholesky 中丢失正性，应如实返回算术失效，不能默默截掉原行或把小权改成0；提供的源码没有这种截行分支。

## 4. 真实梯度与完整正规模型

令 H=$E^2+\epsilon^2I$。利用迹的循环性质，

$$
d\,\operatorname{tr}(H^k)
=k\operatorname{tr}\{H^{k-1}(E\,dE+dE\,E)\}
=2k\operatorname{tr}(EH^{k-1}dE), \tag{9}
$$

最后一步使用 H 与 E 交换。故在基点

$$
d\Phi={2k\over c^2}
\sum_i\nu_i\,\operatorname{tr}(W_iE_i\,dE_i)
={2k\over c^2}\sum_i\nu_i(K_ir_i)^\top dr_i. \tag{10}
$$

第二个等号直接展开 (7)；矩阵 $W_iE_i$ 在基点对称，混合分量的两次出现已由 K 包含。

令 $J_i=dr_i/dx$ 为原全部仿射变量的完整 Jacobian。冻结权的准确正规量为

$$
H_K=\sum_i\nu_i J_i^\top K_iJ_i,\qquad
g_K=\sum_i\nu_i J_i^\top K_ir_i,\qquad
\nabla\Phi={2k\over c^2}g_K. \tag{11}
$$

这里 $H_K$ 是冻结二次模型的正规矩阵；未把它冒称 $\Phi$ 的完整 Hessian。它是半正定，任一非零原观测方向都得到严格正的残差范数。

若 R 是已有的正定步范数矩阵、$\mu>0$，方向

$$d=-(H_K+\mu R)^{-1}g_K$$

在 $g_K\ne0$ 时满足

$$
\nabla\Phi^\top d
=-{2k\over c^2}g_K^\top(H_K+\mu R)^{-1}g_K<0. \tag{12}
$$

因此只要在同一光滑分片模型中足够缩步，真实 $\Phi$ 会下降。若粗 QP 另带几何不等式，既有约束仍应保留；当0是该线性可行集内的点，最小化同一凸二次模型也给非正的一阶方向。处于必须恢复可行性的负右端约束时，不从 (12) 推断目标必降，仍真实读取。

原完整 H² 预条件和粗列同范数白化可以继续使用。若 x=Bz 是已有任意列映射，正规量准确变为 $B^\top H_KB$、$B^\top g_K$。这没有增加或删除模型自由度。固定旧阻尼数值的尺度不自动与新 K 可比；若只作统一正常数重标，应同时重标二次模型和对应的正则系数，以保持指定步问题。

### 为什么必须读真实目标

p>2 时，冻结 Q=$\sum\nu_i r_i^\top K_ir_i$ 仅在基点给出与 $\Phi$ 同方向的梯度，不是全局上界。取一个块 $E=\operatorname{diag}(x,0)$、p=4、$\epsilon=c=1$、基点 x=1，则 $\Phi=(x^2+1)^2+1$、Q=$2x^2$。与真实目标在基点同值同梯度的缩放二次模型是 $1+4x^2$；x=2 时真实值26，大于模型17。因此即使 epsilon 严格正、补齐正常数和基点常数，仍不是 MM 上界。p=2 时补齐已知缩放与加法常数后，二次模型才与真实目标相同。

因此任何接受都必须重新读取实际固定 epsilon/p/c 的 $\Phi$，并同步直接 maxGram 与原 $J_w$。谱 $\Phi$ 下降也不严格保证每一步 M 下降，式 (4) 只是全局上下界关系；若当前任务要求 max 实降，须读取它。实际试验确实记录了冻结模型预测下降、全步真实 $\Phi$ 却上升而被回溯的情况。

## 5. 正向与转置：原 quarter/orbit 约定保持

当前每个保留角 orbit 的重数为 $m_\ell>0$，径向正权为 $\omega_s>0$。设

$$
C_0=\sum_{s,\ell}\omega_sm_\ell,\qquad
\nu_{s\ell}={\omega_sm_\ell\over C_0}.
$$

原 operator 的 native 残差及 Jacobian 已带 $\sqrt{m_\ell}$：

$$q_{s\ell}=\sqrt{m_\ell}r_{s\ell},\qquad
J_{\mathrm{nat},s\ell}=\sqrt{m_\ell}J_{s\ell}.$$

于是未除全局正常数的准确正规量为

$$
\widehat H=J_{\mathrm{nat}}^\top\operatorname{diag}(\omega_s)KJ_{\mathrm{nat}},\qquad
\widehat g=J_{\mathrm{nat}}^\top\operatorname{diag}(\omega_s)Kq,
$$

且

$$\nabla\Phi={2k\over c^2C_0}\widehat g. \tag{13}$$

不能把 native residual 再乘一次 orbit，也不能漏掉转置侧的原 operator 约定。

令 $K=LL^\top$ 为 Cholesky 分解，设置

$$
A=\operatorname{diag}(\sqrt{\omega_s})L^\top J_{\mathrm{nat}},\qquad
b=\operatorname{diag}(\sqrt{\omega_s})L^\top q. \tag{14}
$$

则 $A^\top A=\widehat H$、$A^\top b=\widehat g$。正向应用 $L^\top$，转置应用 L；这就是供 LSMR／LSQR 使用的准确加权 operator。

对 (7)，五个非零 Cholesky 参数可写为

$$
a=\sqrt u,\quad b_1=v/a,\quad
c_1=\sqrt{u+w-b_1^2},\quad d_1=v/c_1,\quad
h=\sqrt{w-d_1^2}.
$$

其正向与转置准确为

$$
L^\top r=(ae+b_1f,\ c_1f+d_1g,\ hg),\qquad
Lr=(ae,\ b_1e+c_1f,\ d_1f+hg). \tag{15}
$$

这给原始三项上的完整白化，不假定三个分量可独立加权。

角反射下 $E(-\phi)=D E(\phi)D$，D=diag(1,−1)；因此 W 同样共轭，三分量 K 在 diag(1,−1,1) 下共轭。(1)、(7)、双线性正规式保持同一 orbit 对称性。故 [R653](R653-exact-quarter-angle-closed-Gram-reduction.md) 的 quarter 重数合并继续准确成立，即使 K 的非对角元为非零。

## 6. 完整消费接口

[positive_spectral_gram_weights.py](../scripts/resume_20261120/positive_spectral_gram_weights.py) 的完整 SHA-256：

e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91。

它提供以下接口，全部保原行／列：

| 接口 | 数学含义 |
|---|---|
| Parameters(p,epsilon,scale) | 固定 (1) 的三个参数 |
| Blocks(raw_residual,params) | 从原三项 E 基点形成准确式 (6)–(7) 的数值载体 |
| apply(r)／apply_columns(J) | K r／K J，无径向权或重复 Frobenius 因子 |
| normal_and_gradient(J,r,weights) | 流式精确代数 $J^\top\operatorname{diag}(\mathrm{weights})KJ$、$J^\top\operatorname{diag}(\mathrm{weights})Kr$ |
| whiten(r)／whiten(r,transpose=True) | (15) 的 $L^\top r$／$Lr$ |
| NativeLinearization(o,x,stage_weights,params) | 原完整 operator 的 (14)，供现有完整空间预条件／粗列映射包裹 |
| actual_trial(candidate) | 真实 $\Phi$、p/epsilon/c、$\nu_{\min}$、旧 $J_w$ 和直接 maxGram |

NativeLinearization.operator 的 shape 为
$(o.P\,o.N\,3,\ o.free\_size)$；本 Gauss 模型为 $7377\times513\times3=11\,353\,203$ 个 native 行。residual 为相同长度；gradient 为原完整自由变量长度。true_gradient_factor 精确对应 (13)。模型、原仿射端口及同 g 输入均由原 operator 保持。

粗 QP 可逐 stage 使用现有角向分离 Jacobian 核与完整 K 收缩；无需形成“全部行×全部粗列”的巨型矩阵。全空间可直接用已有 Jv/Jᵀ 与 (14)，无需逐原变量差分。已与两求解线程交接：geometry 在其真实物理 H² 方向自然完成后，从新的同空间父接同一正谱目标；full solver 保当前方向源不动，后继按 root 分工接桥，避免重复方向。

实现中的实际数值统计采用普通 binary 运算，明确标为非向外数值证书。数学式 (1)–(15) 是完整精确结论；其使用范围和真实连续证书不混同。本条没有新增必须先通过的 fixture 或科学验收门。
