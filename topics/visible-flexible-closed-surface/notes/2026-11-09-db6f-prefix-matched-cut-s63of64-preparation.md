# s=63/64 相配 cut 的新 UNSOLVED 初猜：实际纯准备记录

作者 /root/coupled_prefix，2026-11-09。**准备进程真实退出 0；原 coupled 尚未启动。** 本次落实已冻结的 matched-cut-hermite-warm-interface（SHA256 9c26c977…），没有修改该稿、原 final-preparer-v3、任何已审数值源、continuation03 或原完成标准。

## 1. 固定输入与输出身份

唯一数值来源是：

- 原 UNSOLVED M15 affine CP：prefix-flat-v17v18-m15-affine-cut-predictor-from14q512，SHA256 4a13e132…，连同其原两块完整系数；
- 已关闭的 continuation03 call001，$s=63/64$，SHA256 3a258afc…，真实 converged=true、原 residual $9.40030806875761\cdot10^{-10}$。该历史请求 jacobian=false、audit=false，只能提供 warm states；
- 原 from-affine coupled command、同 g 的原五 I/O 之外配置，以及实际原 constructor/restart。

新脚本是 scripts/db6f-prefix-prepare-matched-cut-warm.py，SHA256
246e36312e7dc80b7f8c16dc8759423752c6370ad923eeba14a5545e5a3ecf48。
它在所有输入 SHA、原请求 $H_j=(63/64)^jH_{{\rm affine},j}$、typed 配置、shape/raw 镜像和有限 jets 核对后，生成：

| 输出 | 身份 |
| --- | --- |
| prefix-matched-cut-s63of64-warm-01.json.gz 与两个 coeff 块 | 仅新的 UNSOLVED 初猜 |
| prefix-matched-cut-s63of64-warm-01-preparation.json | 本次实际原重启检查与完整 15 模高度差 |
| 原 coupled 新 stem 的 -tail-config.json | 原配置仅换五个 I/O |
| 原 coupled 新 stem 的 -input-bindings.json | 原 argv 仅换三个路径，尚未运行 |

新 warm 明确 solver_success=false、actual_nonlinear_tail=false。没有继承旧 affine 的 message、residual、summary、Newton audit、预测 slope、计时、restart 诊断或旧 tail 成功结论。必要的物理/profile/chart/mesh/gauge/support/p 字段原样保留；旧结论只可通过 source_affine_checkpoint 的来源 SHA 回看。

## 2. 实际实现的补偿与舍入

脚本把保存的 binary64 系数、mesh、gauge 和目标 H 当精确有理数。对旧最后跨度按原物理末点作精确 Horner 求值，得到

$$
d_j=\frac{H_j^*}{\sigma q_g}-Y_{Z,j}(L),\qquad
b(s/L)=10(s/L)^3-15(s/L)^4+6(s/L)^5.
$$

每个跨度左端展开同一个全局 b，把 $d_jb$ 只加到零基 state31–45。每个新系数先在 Fraction 中完成“旧系数加精确补偿”，再只舍入一次为 binary64。R/T 块从原数组复制不作任何浮点运算；中央低三阶为零的补偿项直接跳过，保留包括 signed zero 在内的原字节。

输出仍按原 (6,2632,46) 系数布局分块 gzip。两个 gzip 文件分别为 4,174,602 和 1,467,096 字节，均小于 5MB；所有超过 1MB 的数据已压缩。源码、配置、主 CP、各系数块、检查报告和启动绑定分别记 SHA；没有丢弃原系数或覆盖旧文件。

单个原始幂基系数的最大舍入误差约 $5.2215\cdot10^{-12}$，精确分数在报告里。不同阶幂基系数的量纲不同，这个最大值不是位置、曲率或 metric 误差。实际末端导数变化和重启高度另行测量，不能用这个原始系数数值代替它们。

## 3. 真正执行了哪些初始化

程序随后调用原 flat/trial wrapper、原 BVP constructor 和原 preserve-restart，分别重启旧 CP 与新 CP。它只取原物理 chart、保存 PPoly 和入口初始化；没有创建 tail client。

准备进程内将 solve_bvp、solve_ivp、subprocess.Popen、subprocess.run 设为直接拒绝入口；这些保护没有写回任何源码，且拒绝入口实际尝试次数为零。原 bridge 的标量几何初始化仍按原 constructor 执行。报告中的 “0 solver” 专指没有 BVP/IVP、角向 momentum root、RK、真实 DN 或子进程，不把几何 constructor 冒充纯 JSON 读取。

原重启实际得到 2633 节点。以下全部通过：

| 实际核对 | 结果 |
| --- | --- |
| 保存 PPoly 在中央的 0、1、2 阶，全 46 槽 | 字节逐位相同，最大差均 0 |
| 所有跨度 R/T 系数 | 字节逐位相同 |
| 原/新重启的数值 mesh 与原物理 mesh | 字节逐位相同 |
| 原/新重启全部 15 个自由参数 | 字节逐位相同 |
| 原/新重启 R/T 全节点值、全部入口值 | 字节逐位相同 |
| support 振幅、q_g、warp_reference、桥符号 | 与旧重启相同 |
| 末端非均值一阶导数最大变化 | $1.3877787807814457\cdot10^{-17}$ |
| 末端非均值二阶导数最大变化 | $2.7755575615628914\cdot10^{-17}$ |

中央实际比较的是系数 PPoly 的完整两 jet。没有另算完整 Cartesian 或 mean 两 jet；其中央保持范围来自已绑定方法稿的条件证明，不把本次输入检查当新的几何证书。原 mean 仍须由实际解从中央重新积分；完整 Z 镜像和末端 mean/Cartesian 接缝仍按原流程重做。

## 4. 末端高度：全部实际差留在报告

报告保存了四个不同对象：旧 PPoly 的 cut 高度、修改后保存 PPoly 的 cut 高度、历史真实成功 request H*、原 preserve-restart 返回后实际将被请求的高度。没有拿 metadata 中的 affine predicted_cut_height 代替末端求值。

实际重启与 H* 有 9 个非零浮点差，模号为 1、5、6、7、8、11、12、14、15；最大绝对差仍仅

$$
1.0842021724855044\cdot10^{-19}.
$$

这 9 项包括系数舍入及求值误差；其中第 1、6、8、11 模有更基本的规范化限制：原 binary64 的 $(-.1)Y$ 无法逐位等于该 H*。脚本保存最近商及相邻乘积严格夹住目标的事实；不得把 9 项都说成这四个不可表示槽。

原 worker 将看到的第一模 ratio 为 0.9999999999999999。只用实际高度和原 CP 节点作标量预览，全模 boundary-correction 的归一高度 delta 最大为 $1.3552527156068805\cdot10^{-20}$；未调用 tail.initial，也未评价真正尾方程。因此仍保留原默认 boundary correction，再在实际新高度重新求原真实 DN/J；不能把旧成功 response 改标签为新请求的解。

## 5. 冻结的真实启动入口

新的 coupled stem 是：

prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01。

其 input-bindings.json 有 121 个完整来源/输入/输出绑定。实际 command 与原 from-affine command 逐 token 比较，只有 --restart、--tail-config、--out-prefix 三个路径值不同。tail config 只有 initialCheckpoint、traceFile、iterationCheckpointFile、trialDiagnosticFile、trialStatePrefix 五项变化；所有其它键以 typed canonical JSON 比较相同。

原 M15/N256/p8/s32/depth12、guard .05、36 轮、tail tol $2\cdot10^{-9}$ 与全部物理参数保留。prefix angular512/audit1024、tol $2\cdot10^{-9}$、BC $10^{-8}$、physical BC $2\cdot10^{-11}$、空 warmup、lagged-tail、preserve-restart 和全部自由 p 保留。

启动绑定提供原 db6f-prefix-run-bound-command.py 的精确 argv，**仅供主会话在独立审查后启动**。没有调用、放宽或改写旧 final-preparer-v3；这条新来源是“已有成功中间边值的 matched-cut warm”，不是 continuation03 达到旧固定 s=1 的证明。

第一项真实 DN 请求仍由原 solve_with_actual_tail 在实际重启 H 上发出，jacobian=true、audit=false；fresh client 不会直接返回旧响应。随后 inner affine 解必须通过原候选 H 的真 DN 校正和原 BC，最后 seam_audit 仍要求真实 jacobian=true、audit=true。整体 N512 真校正、实际 XYZ 表示、连续证书及独立重跑都没有由本准备代付。

## 6. 实际退出与复算

实际命令为在仓库根目录运行原新脚本，不带参数；tool session60467，首次 yield receipt217447，最终真实 exit0 receipt a79183。程序自报准备耗时 9.484356820998073 秒。实际 tool 观察另存 prefix-matched-cut-s63of64-observed-preparation.json，不从文件存在推断退出。

默认 stem 现在已经使用，脚本会拒绝覆盖。独立复算可给两个全新、位于本题 notes 的 --warm-prefix 与 --coupled-prefix；仍只准备，不启动 coupled。因为压缩系数不含输出文件名且 gzip mtime=0，独立复算应得到相同系数块字节；主 CP/config/报告中的新路径和耗时可以不同，不能要求这些元数据字节全部相同。

这份 CP 是可审查、可复现的初猜。尚未检查其全段 Frenet 正域，也没有新的成功 BVP、实际 metric 或闭曲面结果。
