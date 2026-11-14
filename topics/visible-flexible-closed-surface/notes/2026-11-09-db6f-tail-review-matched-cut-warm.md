# Matched-cut Hermite 初猜：完整独立审查与纯准备重放

审查人：/root/tail_theory，2026-11-09。作者 /root/coupled_prefix。

**结论：PASS，范围为条件数学、实际准备器、保存的初猜、原 restart 与未来原联解入口。** 本人未参与该准备器实现；独立重新运行了作者的纯准备进程，并另写不导入作者实现的 exact Fraction / 保存数据检查器。两次工具进程均实际退出 0。没有启动 BVP、IVP、角向 momentum root、RK、真实尾 DN 或任何未来联解。

这份新 CP 明确是 **UNSOLVED 初猜**。本审查没有证明其全段 Frenet 正域、真实边界残差、等距误差、闭合、曲率或 reach；也没有把 continuation03 的中间成功响应写成原固定目标 $s=1$ 已完成。

## 1. 冻结对象及来源

全文审查的对象为：

| 文件 | SHA256 |
| --- | --- |
| prefix-matched-cut-hermite-warm-interface.md | 9c26c977f6bc173b8e8710672c4258dfcaa55ea1a4abbedabb5215204c77ef2f |
| 同 stem 的 sources.json | bcdbb73657f477e7db770640ead238ed1365436122817a662933d26a520a7f18 |
| scripts/db6f-prefix-prepare-matched-cut-warm.py | 246e36312e7dc80b7f8c16dc8759423752c6370ad923eeba14a5545e5a3ecf48 |
| prefix-matched-cut-s63of64-preparation.md | 16f04072372a1e9924b993633baf8b028d3cb8e95f2087a16bfea9dc7db53118 |
| prefix-matched-cut-s63of64-warm-01.json.gz | cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc |
| 同 warm stem 的 preparation.json | 31bc073433407e02edb11ec7ea41478195b46d95de1bb73d04b864e56c40a358 |
| 原 coupled 新 stem 的 input-bindings.json | 5b184918f4c5a86f10189c5433cd447af4a822856a2fe569df4439e03efdeb21 |

上表省略的笔记前缀均为 `notes/2026-11-09-db6f-`。coupled 新 stem 是 `prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01`。

独立检查器重哈希了原静态账本的 34 项、作者启动账本的 121 项、独立重放账本的 121 项及作者发布清单的 9 项；去重后共 129 个实际文件，哈希和已记录长度全部一致。没有通过旧摘要代替当前文件校验。作者与重放输出路径相异，所有已冻结作者文件保持原字节。

原 63/64 尾来源确是 continuation03 call001，文件 SHA256 为 3a258afc492f4204f85c0ef4535c00d041983c27d8ebd8c9b907df0961a32a0b，converged=true、残差 $9.40030806875761\cdot10^{-10}$。该请求 jacobian=false、audit=false，只能提供 warm states。请求的 15 个高度、865×30 states、13 个 rawNode / rawStates、17 个 jet 字段及同 g 配置均由准备器的冻结输入门核验；本独立审查再核其实际文件身份和使用方式。

## 2. 原自由 cut 问题没有新增高度边界

直接读原 `db6f-prefix-coupled.py` 的 TailMixin、solve_with_actual_tail、main，及 flat / trial 两个薄 wrapper。原问题仍是 46 个状态加 15 个自由参数：入口条件为 $Y(0)=Y_{\rm core}(p)$，终端为

$$
q_g f_Z(L,Y(L),p)-\frac{S_{\rm DN}(\sigma q_gY_Z(L))}{\sqrt{E_{\rm cut}}}=0.
$$

没有额外的 $H=H^*$ 条件，也没有锁定 $p$。$H=\sigma q_gY_Z(L)$ 始终是当前边界状态的函数。`--fixed` 保持物理 profile、桥、角坐标图和尾背景固定；实际中央 support 振幅仍由 $p_0$ 决定。数值规范 $q_g=.1$、桥符号 $\sigma=-1$ 与实际 support 振幅不混用。

当前来源只是选取一个已成功的中间尾边值，使新 prefix 的首个实际请求接近它。原求解目标与最终边界判据不变。原保存的 affine 目标不是必须先满足的独立边界。

## 3. 全局五次补偿及中央完整两 jet

对保存的 binary64 数字按精确实数解释，记

$$
b(u)=10u^3-15u^4+6u^5,\qquad
d_j=\frac{H_j^*}{\sigma q_g}-Y_{Z,j}(L).
$$

只令 $\widetilde Y_{Z,j}=Y_{Z,j}+d_jb(s/L)$，其余 R/T、物理 mesh、全部 $p$ 和材料数据保持。直接求导得到

$$
(b,b',b'')(0)=(0,0,0),\qquad
(b,b',b'')(1)=(1,0,0).
$$

因此实数多项式层面中央全状态两 jet 保持，末端非均值 Z 高度达到 $H^*$、其一二阶径向导数保持。$d$ 中的旧末值来自最后实际 PPoly 跨度，不能以旧 metadata 的 predicted_cut_height 代替；实现使用 exact Horner，独立检查器用 exact power sum 重算，15 项完全相同。

完整高度的均值没有可直接编辑的状态槽。原 `height_integral` 从中央零值重新积分实际角曲线的平均速度；adaptive frame 中该速度是包含角坐标输运项的 W。若原局部 frame 在中央邻域定义并对变量可微，则 $\widetilde Y-Y=O(s^3)$，而两条状态曲线在 0 的值和一阶导数相同，所以平均速度的值和一阶导数相同。两边均值初值均为零，故均值自身的两 jet 相同。非均值状态的两 jet 已相同，有限 Fourier / 相同可逆角坐标链式法则于是给中央完整 Cartesian 两 jet 相同。

这是相对于旧数据的条件保持引理。它既不证明旧数据本身是精确几何解，也不保证修改后的全段 frame 留在正域。下半的镜像必须反射完整 Z，包括新重新积分的均值；只反射 Z Fourier 块不足。

同一个全局多项式在各跨度的展开在实数层面一致。实际保存时每个系数单独舍入，可能产生微小的内部导数差；此 warm 不是由该论证认证的精确公共 C²图。最后原 solver 将从所得节点和原 RHS 重新构造 C²表示，仍须按原完整认证流程检查。

## 4. 实现与全数组独立算术

完整阅读准备器的输入门、gzip/NumPy 读取、系数展开、输出白名单、原初始化、防求解入口、报告及 argv 构造。它固定三件关键来源 SHA，逐项重核其余绑定；系数只允许形状 (6,2632,46) 的有限 float64 数组、按 state 连续分块，且拒绝覆盖。

作者实现用二项式公式把 $b(s/L)$ 平移到各跨度左端，再在 Fraction 中完成“旧系数加补偿”，最后只舍入一次。我的检查器不导入该实现，改用另一条精确计算路径：

1. 旧末值用六项 exact power sum 求和；
2. 对 $b(s/L)$ 从最高项递推 $p(u)\mapsto(u+s_i)p(u)+c$，得到局部升幂系数；
3. 独立重算每个 Z 系数的精确加法及 binary64 舍入，逐值比较存储字节。

实际检查了全部 **236,880 个 Z 系数**。全部 **489,552 个 R/T 系数**与旧数组逐字节相同。完整数组共 726,432 个数字；作者与独立纯准备重放的完整数组及两个 gzip 文件字节均相同。没有只检查少量采样点。

独立重算也得到与作者完全相同的最大原始幂基系数舍入误差，约 $5.2215249770097094\cdot10^{-12}$，精确分数在机器报告中。它不是位置、曲率或 metric 误差上界，不同阶系数的量纲不能混算成一个几何容差。

中央 46 槽各自 0/1/2 阶系数 jet 全部字节相同，共 138 个中央项。这里没有数值求过完整 Cartesian 或均值两 jet；其保持仅由上节条件论证支付，报告明确标识这一范围。

## 5. 实际原 constructor / restart 重放

独立以新 `tail-review-matched-cut-warm-replay` 与 `tail-review-matched-cut-run-replay` stems 运行同一冻结准备器。原默认 stems 已占用，未再次使用，也没有覆盖作者数据。

准备器实际导入原 flat/trial wrapper 和原 preserve-restart，分别对旧 CP、新 CP 执行原几何 constructor / restart；没有创建 tail client。该准备进程在导入数值源码前将 solve_bvp、solve_ivp、subprocess.Popen、subprocess.run 设为直接拒绝，并另外覆盖 runner 的 solve_bvp。实际拒绝入口尝试数为零。原桥的几何初始化仍执行，不能把本重放称作纯 JSON 读取；“零求解”专指未调用 BVP/IVP、moment root/RK、真实 DN 或子进程。

原 preserve-restart 实现核查同一 chart、物理 profile、尾参数/cut、warp_reference；以保存的 support/参数恢复原自由 $p$，对保存物理节点反解/正解坐标，评估保存 PPoly，最后加原入口局部修正。此修正止于前半 ramp，不能把新末端高度改回旧 affine 高度。完整源码中没有要求 CP success=true 的入口门。

本次实际原/新 restart 数值与独立重放全部一致：

| 项目 | 结果 |
| --- | --- |
| 实际节点数 | 2633 |
| 数值 mesh、物理 mesh | 逐字节不变 |
| 全部自由参数 | 逐字节不变 |
| R/T 全节点值及全部入口值 | 逐字节不变 |
| support 振幅、规范、warp_reference、桥符号 | 相同 |
| 末端非均值一阶导数最大变化 | $1.3877787807814457\cdot10^{-17}$ |
| 末端非均值二阶导数最大变化 | $2.7755575615628914\cdot10^{-17}$ |

作者与独立重放报告中所有确定的数学字段逐值相同。仅明确输出路径、由路径变化引起的 CP 哈希/长度、来源记录及耗时不要求相同；其余 restart 诊断也完全相同。

传给未来 solve_bvp 的是重启节点值及 $p$。初猜 CP 的末端导数不是额外的独立边界条件，因此没有偷换成同时固定高度和 slope 的问题。

## 6. 四个不可表示槽、九个实际高度差

我用 exact Fraction 商先求最近 binary64，再检查相邻两个浮点数的实际 $(-.1)Y$ 乘积。第 **1、6、8、11** 模的目标严格落在相邻乘积之间，三个乘积均不等于目标。浮点乘法的单调性排除任何更远浮点输入给该目标，故既定 gauge / dtype 下不能承诺全部目标字节一致。

实际 PPoly 舍入和重启求值还贡献其他差别。实际新 H 与 H* 共 **9** 个非零差：第 1、5、6、7、8、11、12、14、15 模；最大绝对差

$$
1.0842021724855044\cdot10^{-19}.
$$

九项差不等同四个不可表示槽。旧真实 request 保留不变，新实际 request 单列；没有把旧 response 改标签为新解。

原 worker 将据第一模比值约 0.9999999999999999 作 uniform warm rescale；高模均非零，不走只有纯第一模目标才触发的 harmonic 分支。原默认 correctInitialBoundary 仍开启，对全部模式调用原线性边界修正作为初猜，再解新实际请求。准备报告中 $1.3552527156068805\cdot10^{-20}$ 只是归一高度修正的预览最大值，作者与本重放都没有调用 tail.initial 或真正尾方程来评价它。

## 7. 旧结果作废、真实首请求及未来验收

新 CP 从白名单复制必要物理/profile/chart/mesh/gauge/support/p 字段，显式声明 solver_success=false、actual_nonlinear_tail=false 和 UNSOLVED。旧 residual、summary、预测 slope、Newton audit、计时及成功状态没有作为新结果继承；独立检查器核各失效字段缺席。来源指针只证明数据从何而来。

typed canonical JSON 比较证实新 tail config **只有五个 I/O 字段变化**，其它物理和数值字段完全相同。initialCheckpoint 指向已关闭的真实63/64响应；四个输出路径指向新 coupled stem。原 argv **只有 --restart、--tail-config、--out-prefix 三个值变化**。原 M15 / tail N256 / p8 / s32 / depth12、36 轮、guard .05、tail tol $2\cdot10^{-9}$ 全保留；prefix angular512 / audit1024、原容差、4500 节点上限、空 warmup、lagged-tail、preserve-restart 和全部自由 $p$ 全保留。

直接读取 trial client / worker 确认：fresh client 的 cache 初始为空；旧 CP 只载入 states、参数与 height 标签，不载入旧成功 response 作为缓存。原 solve_with_actual_tail 首先从新 restart 的实际 H 发出 jacobian=true、audit=false 的真正请求。内层 affine BVP 之后仍在 candidate H 重新请求真 DN 并检查原 o.bc；最终 seam_audit 要求 jacobian=true、audit=true。历史未审计的63/64成功不能替代上述任何一步。

旧 final-preparer-v3 原字节未动，本路线有自己的来源与输出身份；它没有冒称 continuation03 已达旧固定 $s=1$。原 main 可捕获异常后写 summary，未来验收必须同时核 solver_success、真 outer BC、最后 true DN/audit、实际退出和绑定，不能只看工具退出码。

## 8. 实际工具证据、复算及限制

本人的独立纯准备命令是冻结作者脚本加两个全新输出 stem。实际 exec_command 初始 receipt **f55272**、session **75959**，write_stdin 完成 receipt **09b7ee**、实际 exit_code=0；报告自计 4.58408178499667 秒。

本人的独立检查器为 `scripts/db6f-tail-review-matched-cut-warm.py`，SHA256 **02dd8e6ad710f55d682b8509b66daf6d11ee36eb455d3729ba254e0117d6be47**。其实际初始 receipt **633a60**、session **65342**、完成 receipt **b8ca25**、exit_code=0。结果文件 `tail-review-matched-cut-warm-check.json` 的 SHA256 为 **11403ef8c0bef61541744ab1b172ad154333ff55e18e58cd7bb42579b2a78805**。

本审查不证明原联解将收敛，不检查修改后的全段正域，也不支付 N512 真校正、实际 XYZ、公共 C²接缝、连续 metric/曲率/reach、非全等矩或独立完整求解。它确认的是：当前已保存、可复现的新初猜如实实现已证明的条件补偿，接入的仍是原自由 cut 问题，且所有旧成功声明正确作废。
