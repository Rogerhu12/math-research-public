# 用已成功尾边值初始化原自由 cut 联解：Z-only Hermite 接口

状态：**静态接口及条件证明；未构造新 CP，未调用 profile、root、RK、BVP、优化或几何后端。** 作者 /root/coupled_prefix，2026-11-09。本稿不修改正在运行的 continuation03，也不声称 M15 已联解。

结论是：**原驱动器允许这条初猜路线，原自由 cut 问题不要求先解旧 affine 预测的固定 $s=1$ 高度。** 只补初猜的非均值 Z 系数即可将其数学 cut 高度移到一份真实成功 DN 的高度附近，再由原真实 DN/J 和原 BVP 校正。它没有保证新初猜处于全段 Frenet 正域或联解一定收敛。还有一个必须保留的有限精度限制：当前 $s=63/64$ 的成功高度有四个槽不能通过原 binary64 乘法 $(-.1)Y_Z$ 逐位复现，最大差仅 $1.0842021724855044\cdot10^{-19}$；不能把“数学精确匹配”写成当前计算管线的字节相同。

## 1. 为什么固定 affine 目标不是原 BVP 的额外边界

实际源码是 scripts/db6f-prefix-coupled.py 的 TailMixin、solve_with_actual_tail，以及原 flat/trial wrapper。M15 有 $n=3M+1=46$ 个状态和 15 个原自由参数 $p$。原 BC 是

$$
Y(0)=Y_{\rm core}(p),\qquad
q_g f_Z(L,Y(L),p)
-\frac{S_{\rm DN}(\sigma q_gY_Z(L))}{\sqrt{E_{\rm cut}}}=0.
\tag{1}
$$

首组 46 条、末组 15 条，没有另加 $H=H_{\rm affine}$ 的 Dirichlet 条件。这里

$$
H=\sigma q_gY_Z(L),\qquad q_g=.1,\quad \sigma=-1
\tag{2}
$$

是 cut 状态的函数，不是被固定的材料参数。q_g 是数值规范化；实际中央 support 振幅是原 $p_0$ 所控制的约 .0999997666，二者不能混用。

原 --fixed 冻结整个 profile、bridge、angular chart 和 tail metric；它仍允许全部 $p$ 在原 BVP 中变化。旧 affine 目标只是先前选择的一条初猜接续路径。故从另一份相同 g、相同 M/N/径向离散的真实尾边值起步，不改变 (1)。

## 2. 一个确切的初猜补偿

设旧 UNSOLVED affine CP 的物理域为 $[0,L]$，其 PPoly 状态为 $Y(s)$。M15 的槽是：0 为径向均值，1–15 为 R 模，16–30 为 T 模，31–45 为非均值 Z 模；没有可直接修改的 Z 均值槽。

取一份已关闭、真实 converged 且原 residual 小于 $2\cdot10^{-9}$ 的同 g 尾响应，物理 request 高度为 $H^*$。令

$$
b(u)=10u^3-15u^4+6u^5,\qquad
d_j=\frac{H_j^*}{\sigma q_g}-Y_{Z,j}(L),
$$
$$
\widetilde Y_{Z,j}(s)=Y_{Z,j}(s)+d_jb(s/L),\qquad
\widetilde Y_R=Y_R,\quad \widetilde Y_T=Y_T.
\tag{3}
$$

保持 p、actual_primary_amplitude、central_correction_scales、q_g、warp_reference、物理 mesh 和全部材料字段不变。$b(0)=b'(0)=b''(0)=0$，$b(1)=1$、$b'(1)=b''(1)=0$，所以作为实数多项式恒等式，

$$
\widetilde Y^{(k)}(0)=Y^{(k)}(0)\ (k=0,1,2),\qquad
\sigma q_g\widetilde Y_Z(L)=H^*.
\tag{4}
$$

末端原非均值一、二阶 s 导数也保持。**这不表示末端原 BC、mean jet 或全 Cartesian 两 jet 仍满足**：末端 angular 曲线的 Z 已改变，原 Frenet 速度和 mean 仍随其状态改变。

构造 d 时应使用保存 PPoly 在真实末端的值，不使用 metadata 中的 predicted_cut_height 代替它。已审原 restart 检查明确显示后两者存在 $1.7\cdot10^{-21}$ 级差别；新文件不得把旧 surrogate 输出当新几何值。

### 保全中央完整两 jet的范围

完整高度是

$$
Z(s,\psi)=\bar z(s)+q_g\sum_{j=1}^{M}Y_{Z,j}(s)\cos(3j\psi),
\qquad
\bar z(0)=0,\quad
\bar z'(s)=\langle V_Z(s,Y(s))\rangle_\psi .
\tag{5}
$$

原均值由 height_integral 从中央重新积分，不应复制旧末端 mean 或在 CP 里加一个伪 Z 常数。若原局部 frame 在中央邻域有定义且对状态可微，则 (3) 给 $\widetilde Y-Y=O(s^3)$。故均值速度及其在 0 的一阶导数保持，完整 $F,F_s,F_{ss},F_\psi,F_{s\psi},F_{\psi\psi}$ 在 0 均保持。相同的可逆 angular chart 不改变此结论。

这是**相对于旧两 jet 的保持**，不是把旧有限精度 CP 自动升级为精确闭图。若旧上半图已有中央镜像条件，则下半图应反射完整高度：

$$
F_-(s,\psi)=\bigl(X_+(-s,\psi),Y_+(-s,\psi),-Z_+(-s,\psi)\bigr).
\tag{6}
$$

均值和非均值都在 (6) 内反射；不能只反射 Z Fourier 块。新 warm 仍不是已认证镜像图，最终公共 C²表示和全部接缝必须按原流程重做。

## 3. 保存的五次 PPoly 与原 restart

旧 CP 为 2633 个物理节点，$L=2.021775895105454$，系数以两个 gzip NumPy 块保存。系数轴是 (6, interval, state)，按五次至常数的降序排列。在跨度左端 $s_i$，应只给 Z 块增加

$$
\delta C_{5-m,i,Z_j}
=d_j\,\frac{1}{m!}\left.\frac{d^m}{ds^m}b(s/L)\right|_{s=s_i},
\qquad 0\le m\le5.
\tag{7}
$$

这是同一全局五次多项式的逐跨度展开，不需要新增节点。内部跨度按原 PPoly 半开 convention 使用右侧多项式，最后端点使用末跨度；因为 (7) 两侧是同一多项式，其全部两 jet 在实数层面一致，0 和 L 的条件也成立。实际浮点系数加法、展开和末端求值仍有舍入，须显式记录，不把小浮点差宣称为精确接缝证明。

原 db6f-prefix-preserve-restart.py：

- 检查 chart、frozen_profile、物理 tail 参数/cut、warp_reference 完全相同；
- 由旧 support/参数恢复同一 p，按保存的物理 mesh 反解/正解 chart；
- 用 PPoly 求初始节点值，按 q0/q_g rescale；本路线 q0=q_g，M 不变；
- 最后只加原入口局部修正，支撑止于前半 ramp，cut 处为零。

因为中央值、物理 mesh 和 p 输入未变，原入口修正与旧重启相同，且不能把已修改的末端又复原成旧 affine H。旧已审 restart 中实际 mesh 逐位不变；本路线保持所有决定 mesh 的输入，但仍应由未来纯初始化核查记录新文件的实际 roundtrip。

驱动器最终传给 solve_bvp 的是节点值和 p，**不把 CP 的导数当作独立 BVP 边界条件**。solve_bvp 的初始插值和最终解都不受 (3) 的末端导数约束；方程仍为原 (1)。最后保存的 C² PPoly 又由原物理 RHS 的 dy/ddy 重建。因此“初猜 CP 两 jet 保持”不能误述成“整个 Newton 过程固定了这些导数”。

## 4. 当前可用真尾与不能隐去的舍入

一个现在已经关闭的合法来源是
notes/2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-03_tail_0001.json.gz，
SHA256 为 3a258afc492f4204f85c0ef4535c00d041983c27d8ebd8c9b907df0961a32a0b。
它是真实 $s=63/64$，converged=true，原 residual 为 $9.40030806875761\cdot10^{-10}$；请求 jacobian=false、audit=false。它可提供 warm states，不能冒充首个所需 DN/J 或最终审计。

只读标量比较保存的原 affine 高度与该 request 得
$\|H^*-H_{\rm affine}\|_\infty=1.2709895713833145\cdot10^{-5}$、
$\|H^*-H_{\rm affine}\|_1=1.2985622216825237\cdot10^{-5}$。
这些只是选择初猜时的尺度；没有评价新的 frame 或 metric。

使用原双精度规范化时，即使暂不计 PPoly 求值误差，将 $H^*/(-.1)$ 存成 binary64 再乘 $-.1$，仍有第 1、6、8、11 模不逐位等于原 H*。最大差为 $1.0842021724855044\cdot10^{-19}$。逐项检查最近商及其相邻两个 binary64 值，目标严格位于两个相邻乘积之间，且没有一个乘积等于目标；乘法单调性排除了借更远的 binary64 Y 修复这些槽。**所以当前既定 gauge/原 dtype 下，全部原请求字节精确相等并不是可实现承诺。**

合法处理是保留原真实 request H* 与实际重启请求 $\widetilde H$ 的差，使用原 worker 的全部模线性 boundary warm 修正，再重新按原方程解 $\widetilde H$。不能改 H* 标签、伪造它是 $\widetilde H$ 的成功解，也不能改 gauge 或跳过真 DN 来消掉这项差别。

## 5. 第一项实际 DN 请求确实随新初猜走

原 argv 保留空 --warmup-scales、--lagged-tail、--preserve-restart-mesh。因此不会先强迫回到一串旧 affine 边值。solve_with_actual_tail 的第一项是

$$
\widetilde H=\sigma q_g\,y_Z[-1],\qquad
{\rm tail.solve}(\widetilde H,\ {\rm jacobian=True},\ {\rm audit=False}).
\tag{8}
$$

新 config 的 initialCheckpoint 指向上述真实成功 response。fresh trial client 缓存为空；worker 仅从其 checkpoint 取原 states/parameters/cutHeight，同 M/depth/p8 复制网格，并使用接近 1 的第一模 ratio 和原全模 boundary correction。这里所有高模非零，不走仅纯第一模的 harmonic predictor。旧 response 的 flags 不覆盖新 config，也不会被直接返回为 (8) 的响应。

如果 (8) 成功，原 inner BVP 暂用该点实际 slope/J 的 affine 近似；inner 成功后又在新 candidate H 调真实 DN，再以原 o.bc 检查。H 仍可自由变化。最后 seam_audit 必须真调 jacobian=true、audit=true，检查 mean/nonmean 两 jet。它们均不是旧成功 CP 免费提供的字段。

## 6. 最小文件/参数差别与真实验收

不应改已有 final-preparer-v3：它明确绑定旧 affine restart 与 continuation03 的目标终止身份。这条路线若实施，要单列“匹配已成功中间边值的 UNSOLVED prefix 初猜”来源，不能冒充 continuation03 已完成 $s=1$。

将来新 warm CP 应只继承必要物理字段、mesh、参数、gauge 和重新保存的系数块，并明确 solver_success=false、actual_nonlinear_tail=false、状态 UNSOLVED。原 affine 的 success、collocation residual、summary、预测 slope、审计和计时只能留在独立 source provenance，不能被当成已修改 CP 的结果。原 loader 不要求伪造一个 success=true 才能接收这个初猜。

原命令来源为 notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from-affine-input-bindings.json。其完整 argv 只需换三个路径值：

| 参数 | 新值的身份 |
| --- | --- |
| --restart | 本节明确 UNSOLVED 的新 Hermite warm CP |
| --tail-config | 原 config 仅更新五个 I/O 路径的新副本 |
| --out-prefix | 独立未使用的联解输出 stem |

五个 I/O 为 initialCheckpoint、traceFile、iterationCheckpointFile、trialDiagnosticFile、trialStatePrefix；第一项是真实成功尾包，其余四项指向新 stem。已只读 canonical 比较：旧 from-affine config 与 continuation03 config 在排除此五项后完全相同。因此无需变更 M15/N256/p8/s32/depth12、36 轮、tail tol $2\cdot10^{-9}$、guard .05 或任何物理参数。

原 prefix 参数也全部保留：angular512/audit1024，nodes1601/max4500，tol $2\cdot10^{-9}$、bc_tol $10^{-8}$、physical_bc_tol $2\cdot10^{-11}$，固定 profile/chart/linear port，q_g/warp_reference 都 .1，全部自由 p 不锁定。节点数参数不覆盖 saved-mesh 路径实际的 2633 点初猜。

新 Z 可能改变全段曲率和 $1-\alpha^2$，中央不变不代付全段 Frenet 正域。它一般不再满足旧 affine 或真实 ODE，需保存所有原 failure。数学上原正域是开条件；本稿没有给本次补偿的全域余量，因此没有据小幅度推断必过 guard。

如果将来运行，必须原 solver_success、真实 outer BC、最终真实 DN/audit、自然退出与输入绑定共同通过；原 main 会捕获异常，工具退出 0 本身不够。随后 N512 真校正、实际 XYZ/公共 C²表示、连续 metric/曲率/reach/矩和未参与优化者重跑都要对新图另证。此接口只避开一个可能并非最终 BVP 必需的固定目标入口，不代付任何完成标准。

## 7. 当前范围

当前只读上述源码、关闭元数据及原 scalar 高度。没有创建 Hermite 系数、候选 CP、配置或启动文件，没有执行 flow、root、RK、BVP 或 continuation。对应来源账本绑定本文、原实际命令、旧 affine CP/两系数块、真成功尾与实现源，所有未来事项继续明确为条件式。
