# R133：准确角节点上的径向 ODE 误差与连续张量消费者

2026-11-14，visible-exact-astra-ac0d。

**已证明：以下径向积分误差递推及其连续张量组合。实际运算目前为明确的完整前缀。** 本篇使用原 ac1 候选和原 model anchor；没有把径向模型提前称作精确 Codazzi 曲面。全角缺陷与全部网格凸包已分别完整，径向区间验证继续按原不可变几何块推进。本篇保存其真实 61 块、3903 个径向单元的原生前缀，以及第一次实际张量消费的全部逐格结果。

## 1. 同一个模型、准确角点和完整连接

原对象及共同模型定义见[完整角向几何定理](R133-supplement-complete-angular-model-geometry-from-moving-residual.md)。固定

$$
\phi_k=\frac{\pi k}{1024},\quad0\le k<512,\qquad
Q_r=Q\Omega_r,\quad F_r=Qf_r,
$$

其中 $\Omega_r$ 是真实三阶反对称连接。保存的 binary64 角值只用于原浮点提案；本消费者通过 directed FFT 的准确单位根计算上述准确角点上的完整字段。

候选 $u,v$ 的 moving Fourier 次数为32，$u^2+Kv^2$ 和其零均值原函数的完整次数为64，连接的完整次数至96。512点 directed FFT 分别完整计算这些有限乘积；这只利用原模型确实有限的 moving 支撑，不将未知物理 Fourier 尾设零。scalar target 的所有 primitive 尾、参数盒及径向导数仍从原完整 target provider 取得。模型真实 mean 的负间隙在每个盒内检查后才取倒数。

model anchor 准确正交。其两系数为 $b=\beta/\gamma$、$z=-aC_{\rm ref}$。由目标 provider 的准确恒等式

$$
\gamma^2=\beta^2+a^2R,\qquad C_{\rm ref}^2=R/\gamma^2
$$

可得 $b^2+z^2=1$；旋转后的三列因此仍为正交框架。此后反对称连接保正交。它与真实外部帽世界锚的差别另付，不在本模型定义中冒充为零。

## 2. 真闭盒、单侧 jets 与局部 Taylor 余项

每个原径向格含在一个准确 candidate cubic 中；网格本来已含全部 candidate 接点。用有理数中点选片，避免两个相邻 binary64 节点间的浮点中点落在错误一侧。格内再按完整 scalar target 的真正 germ 接口拆分。

在一个这样的单侧闭段 $[a,b]$，令 $h=a-b<0$。完整 target provider 给

$$
A_j\ge\sup\|\partial_r^j\Omega_r\|_{\rm op},\qquad
f_j\ge\sup|\partial_r^jf_r|,\qquad0\le j\le3.
\tag{R.1}
$$

对三阶 skew 矩阵，若系数为 $p,q,t$，其 operator norm 准确为 $\sqrt{p^2+q^2+t^2}$。实现对每个准确角点取 directed 欧氏范数，再取512点的最大上界；它不要求用于全圆周的 Wiener norm。每个径向导数阶使用同一个准确结构。

在右端需要该段自身的 jets。消费者取

$$
\epsilon=\min\{(b-a)/2,2^{-100}\},\qquad[b-\epsilon,b],
$$

用这个闭盒包含右端的单侧 target jets；candidate 多项式则准确在 $b$ 计算。跨 scalar seam 时不强求其第三阶 jets 相等，也不把一侧 Taylor 多项式越过 seam 使用。

记保存的起点为 $(\widehat Q,\widehat F)$。每次实际先验证 $\|\widehat Q\|_F<2$。从该准确 dyadic 初值出发的局部精确 ODE 流同样保持 Frobenius norm小于2。令 $Q_j,F_j$ 为该初值的真实右端导数；它们由

$$
Q_1=\widehat Q\Omega,\quad
Q_2=Q_1\Omega+\widehat Q\Omega',\quad
Q_3=Q_2\Omega+2Q_1\Omega'+\widehat Q\Omega'',
$$
$$
F_1=\widehat Qf,\quad
F_2=Q_1f+\widehat Qf',\quad
F_3=Q_2f+2Q_1f'+\widehat Qf''
\tag{R.2}
$$

完整包围。这里保留真实矩阵乘法次序，没有假设不同 $\Omega^{(j)}$ 可交换。

设

$$
B_2=A_0^2+A_1,\qquad B_3=A_0^3+3A_0A_1+A_2,
$$
$$
B_4=A_0^4+6A_0^2A_1+3A_1^2+4A_0A_2+A_3,
\qquad W_4=B_3f_0+3B_2f_1+3A_0f_2+f_3.
\tag{R.3}
$$

反复微分 $Q'=Q\Omega$、$F'=Qf$ 并使用乘法范数不等式，得到局部精确解的第四导数界 $\|Q^{(4)}\|_F\le2B_4$、$|F^{(4)}|\le2W_4$。因而对实际辅助数值终点 $(\widehat Q^+,\widehat F^+)$，准确三次 Taylor 包围给

$$
\begin{aligned}
d_Q&=\left\|\widehat Q^+-\widehat Q-hQ_1-\frac{h^2}{2}Q_2-\frac{h^3}{6}Q_3\right\|_F+\frac{2|h|^4}{24}B_4,\\
d_F&=\left|\widehat F^+-\widehat F-hF_1-\frac{h^2}{2}F_2-\frac{h^3}{6}F_3\right|+\frac{2|h|^4}{24}W_4.
\end{aligned}\tag{R.4}
$$

所有和、乘、范数以及准确有理 $h$ 均向外舍入。Taylor polynomial 的区间误差已经包含在第一项，不能把提案积分器的局部容差当作 (R.4)。

## 3. 不含指数放大的全径向误差递推

设准确模型与保存起点的误差分别由 $e_Q,e_F$ 控制。全局模型和从保存初值出发的局部精确流具有相同 skew 连接；右基本解正交，所以二者框架差的 Frobenius norm 保持不变。位置差的导数为框架差乘同一个 $f_r$。因此本段以后

$$
\boxed{\quad e_Q^+\le e_Q+d_Q,\qquad
 e_F^+\le e_F+|h|f_0e_Q+d_F.\quad}\tag{R.5}
$$

位置行使用本段开始的 $e_Q$；式中已经比较了完整局部精确流，并未漏掉一个传播中的 $d_Q$ 积分。后续段再使用更新后的 $e_Q^+$。

辅助单侧分段浮点轨道可能与原未拆分浮点整步不同。两轨道的实际终点 dyadic 差再完整加入对应的 $e_Q,e_F$。原整步轨道始终保留；每64行原不可变 block 的最后框架、位置与保存状态逐 uint64 相同才接受该块。故本误差控制的正是原网格提案，没有在验证中偷偷换一条更好的轨道。

初始 $e_Q,e_F$ 用准确 model anchor 的 directed 包围与原 dyadic anchor 比较得到，均不置零。两种范数的用途也明确区分：原模型框架的 operator norm为1；辅助 dyadic 初值仅用已经验证的 Frobenius界2。

## 4. 连续张量消费者的全输入合同

[已证明的网格凸包与双线性定理](R133-supplement-complete-mesh-hulls-and-continuous-tensor-geometry.md)给准确公式 (T.7)–(T.14)。本篇消费者在每个实际径向格上核对完整 scalar germ 分割，并取

$$
M_{F,r}=\max_{\rm germs}(A_0f_0+f_1),\qquad
M_{N,r}=\max_{\rm germs}(A_0^2+A_1).
$$

它使用真实两端累计误差的最大值，再加格宽平方项和完整角向 native 给出的全圆周二阶项。保存网格的四次旋转 wrap、完整八个反向见证像、准确世界高度平移均不变。

consumer 核对 candidate、target、准确 $\alpha,\nu$、原 geometry report、完整 block chain、整个径向网格，以及两个完整 native 的字节 SHA。径向 native 必须是原源 `3347e061…` 的成功连续前缀，且全部已成块的原状态比特门为真。旧已消费行还保存 canonical JSON 前缀摘要，resume 时必须完全相同；只追加真正新完成的行，不重做 ODE。

径向参数盒包含 $|\eta-\eta_0|\le10^{-9}$；完整角向 native 的共同范围只有 $\eta=\eta_0$。所以两者张量组合目前只在准确 $\eta_0$ 声明连续模型几何，不能把较窄一方的权限扩大。

## 5. 本次实际执行的范围

准确原径向输入为61块、3903格，区间

$$
\frac{1057564037496759}{2251799813685248}\le r\le\frac{25}{8}.
\tag{R.6}
$$

张量消费者实际正常返回0，耗时5.029730秒。该整个连续区域上有

| 量 | 严格界 |
|---|---:|
| 模型位置半径 | $<1.275713423$ |
| 模型位置与框架列的支撑量 | $>.965296536$ |
| 模型到保存的旋转腰见证的距离 | $>.550095277$ |
| 位置总张量误差 | $<.000165359$ |
| 框架法向列总张量误差 | $<.000127780$ |

第三行的见证目前是保存的网格腰顶点；准确模型腰点自身的误差要等径向消费者真正到达 $r=0$ 才能相减。本篇没有从尚未覆盖的腰部推定最终全模型距离。

本次输入快照 SHA256 为 `36f3185dc2eca493d0f0ad9efd0f31fa7ac99094f3c54aedd33c4fa797eb4a4e`。原径向进程在张量消费后继续追加块；按其未改动的完整行前缀及实际61块进度记录恢复该快照，逐字节 SHA 与消费者当时记录完全一致。恢复没有重算一个数学门，也没有改写原失败记录。后续消费使用独立不可变径向快照。

源码分别为
[径向 jets](../scripts/fourfold_codazzi_moving_geometry_directed_jets.py)、
[真实径向验证](../scripts/fourfold_codazzi_verify_moving_geometry_grid.py)、
[连续张量消费](../scripts/fourfold_codazzi_complete_continuous_tensor_geometry.py)。
本次完整前缀输入、输出与重建参数见
[原生记录说明](../notes/2026-11-14-R133-directed-radial-tensor-prefix0061.md)。

## 6. 尚未自动完成的几何步骤

继续完成原全部141块、8966径向格后，张量消费者才生成全模型半径、支撑和真实旋转腰见证距离。其后仍须分别加入真实外帽世界锚、连续修复中心、最终选定度量参数和完整精确非线性解的比较费用。模型框架列不是未解 Codazzi 位置图的几何单位法向；真正帽、四个固定曲率 marker 和闭合条件也未由这条径向 ODE 证明。
