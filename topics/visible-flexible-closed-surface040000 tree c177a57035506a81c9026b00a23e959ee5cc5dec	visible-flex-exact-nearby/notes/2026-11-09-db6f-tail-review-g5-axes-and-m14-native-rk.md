# G5 加密轴与条件 M14 原生径向接口：全文独立审查

2026-11-09，`/root/tail_review_continued_2`。审查对象是
`prefix-g5-axes-and-m14-native-rk.md`，SHA256
`2b24b749be6351e6906e268bacc03d3412dccb7d58d192880495e40c976f54c8`。
作者三件封存清单 SHA256 为
`c0c54cf74f0946dae82a75a09080a59b201a14b38a915aacf085051c9e1afbdc`。

**结论：通过，限于术语、已闭历史参数、原程序调用路径和未来条件接口。**
原 G5 充分条件稿与原 N512 接续稿本来已经区分角求积和径向 RK，
不需要就此作勘误；当前稿也没有把一档新的 s64 实验加入 README 的必需完成门。
它没有产生真正 M14/W14 联解、整图证书或最终独立重跑。G5 仍未由本审查支付。

本次全文读完待审稿、原两份条件稿与固定 g 收敛记录，逐项阅读下述源码调用路径；
对旧保存 CP 和它们各自的末响应独立抽取小字段，对当前已冻结输入重核哈希。
没有导入项目模块，没有执行 BVP、DN、moment root、RK、几何 flow、导出或连续后端，
没有读取当前运行的 trace/iteration/reproduction 来推断完成，也没有新造候选 config 或 CP。

## 1. 原 G5 充分条件与本稿作用域

原 `tail-g5-final-m15-sufficiency.md`（`f3b37b270e7f3479…`）§3 的真实序列表已经写明：
M8 原生径向为 $2\times32,2\times64,2\times128$，之后 M12/M14 的基础步数均为256。
§4.2 把 Galerkin 模数、源角求积、prefix 角数和 XYZ 保留阶分别定义。
§6–7 明确说，达到原完整实际 metric 容差后不自动追加最终高模的独立 s64 门。
原 `prefix-final-m15-n512-followup.md`（`c6e97843feeabc25…`）§1 也明确列出
`steps/auditSteps/shootingParts=32/32/8` 保持，只有 `quadrature=256→512`。

因此，作者说旧稿没有这项错误是准确的。应澄清的是即时文字里可能混同两条轴的
“native N256→512”简称；准确说法是“尾角求积 $N_\theta=256\to512$ 的真原方程校正”。
当前稿既未下调 $B=2\times10^{-9}$，也未把源 residual 改名为全域实际 metric。

README 要求同一个物理问题的加密证据，未指定必须恰好以 M15 作最终模数。
因此将来真正 M14/W14 若能付清同等全部源、整图、误差下降、全时及独立重跑门，
可以作为候选。这个条件判断不等于当前 M14 已成功，也不能略过采用 W14 后数值轨迹改变的说明。
作者保留 M14 旧非单调诊断和失败路径，不把每次试验都宣称单调，范围正确。

时间方向继续由原已审相位作用的全时恒等式支付；该族不使用时间积分器，
因而不存在需要人为制造的时间步误差实验。此点只在最终族确实沿原相位作用、
公共两 jet 和固定帽构造时适用，不能由任意时间采样替代。

## 2. 数值轴及源函数身份

### 2.1 $M$、$N_\theta$、$P$、$S$ 的区别

`db6f-prefix-tail-shared-core.mjs` 从 options 分别读取 `modes`、`quadrature`、`steps`；
`subdividePhysical` 单独读取 `shootingParts`。`createCompactTailShooting.cellFlow`
在每个 stage 上使用 `stepsPerSegment=steps`，或在 state-only 分支作 `steps` 次基础调用。
engine factory 则独立接收 `modes` 与 `quadrature`。
因此改变角求积不会由该入口增加径向基础步数，W14 也不会增加 Fourier 未知模数。

`950f-tail-subdivision.mjs` 把一个原 profile 的局部参数区间分成 $P$ 段，
每段以 $x\mapsto a+hx$ 拉回，并把 `drdx`、`dlogwdx` 同乘 $h=1/P$。
每段再用 $S$ 个基础区间，故原 profile 参数中的基础最大步长为

$$
\Delta x_{\rm base}=\frac1{PS}.
$$

这里是原 profile 参数 $x$，不是物理半径 $r$；每个 raw cell 又含多个 profile，
不能把一条 profile 的 $PS$ 当成整 raw cell 的总步数。

### 2.2 cusp 的附加子步

state-only 的 engine 经 `withCuspAwareRK` 包装，后者用
`splitIntegrationInterval` 在原 `integrationBreakpoints` 处再分段。
`f6tail_fast_split_flux_engine.mjs` 的 state/variational 分支用
`integrationGrid(steps,cuts)` 合并均匀网格和同一断点。
所以 $PS$ 只是基础区间数，有 cusp 时不能把它写成全部实际子步数的严格等式。

在 $P$ 固定、$S$ 加倍时，均匀网格精确嵌套，加入同一断点集合后仍嵌套。
独立检查以有理数核了 P8/S32→64 与64→128的均匀节点包含，
没有调用实际 profile/RK，也没有由嵌套网格推断某次求解的误差已经下降。

### 2.3 `auditSteps`、线性图与冻结背景

原 DN 的 nonlinear shooting 方程由 `steps` 决定。
`auditSteps` 仅在已经得到 sol 后选择 `audit(sol,...)` 的诊断遍历；
把它单独增大不会重新求 shooting。因此未来同步改变 `steps` 和 `auditSteps`
应清楚说明前者改离散方程、后者对齐诊断，作者做到了。

`buildStableStageGraphs` 只接收 `linearFar`、`linearSteps` 和已确定 stage 布局，
它没有接收 nonlinear `steps`。固定 P8、linearFar32、linearSteps256，
确实把本次比较的线性远端图保持不变。
这只隔离 nonlinear RK 轴，不证明线性远端图本身的误差已收敛；待审稿明确保留这一限制。

`closing_recalibrated_tail.createRecalibrationFactory` 的物理 source 创建显式使用
`modes:1, depth:protectCell, steps:1, quadrature:16`。
其几何和积分构造读取冻结的 calibration/warp/cap/width 等输入。
`closing_weighted_tail` 的权重 wrapper 继续使用固定的 `warpWeightLevels` 与 `warpSteps`。
外层 $S$ 或 $N_\theta$ 不会在这个调用点重新设计 source。
原六个物理字段的相同仅是身份复核；共同目标的函数解释来自这些来源及既有几何证明，
不能只凭一个字典哈希宣称整个数学目标相同。

## 3. 三个已闭 M8 的独立字段复核

对每一份 CP，本次从其 `tail_seam.tail_record` 找到它自己的真实末响应，
并核 CP/响应 SHA 与旧 `tail-g5-closed-sequence-inputs.json` 的记录相同。
逐项核对 `tail_config`、末 Jac/audit 请求、converged、seam jets 与 residual。
三份均为保存的真实成功闭包；本次没有重新运行这三个历史求解器。

| 字段 | M8/32 | M8/64 | M8/128 |
|---|---:|---:|---:|
| prefix nodes | 778 | 2570 | 2570 |
| prefix tol | $2\times10^{-7}$ | $2\times10^{-9}$ | $2\times10^{-9}$ |
| fixed_metric | false | true | true |
| physicalDepth / stage depth | 10 / 180 | 10 / 180 | 10 / 180 |
| P / S / auditSteps | 2 / 32 / 32 | 2 / 64 / 64 | 2 / 128 / 128 |
| 基础 PS | 64 | 128 | 256 |
| 尾角求积 | 256 | 256 | 256 |
| 最后真实 residual | $1.3505653752886372\times10^{-10}$ | $1.872382418274325\times10^{-10}$ | $8.191673022591901\times10^{-11}$ |

其余宣称的小字段，包括 `linearFar32/linearSteps256/calibrationSteps512`、
原 floor .05、tail tol $2\times10^{-9}$、maxIterations30/36/36，均由独立读取吻合。
三份历史 CP 与当前 M14 seed 的原六个物理字段 canonical SHA 都是
`811e8cdccbad6edd4c487afc8ec07c16d519995cd9c5b182bc79ab327f414071`。

第一项是设计求解结束后选择了最终物理字段，不能说它从开始就固定 g 或已经使用后两项的 prefix 容差。
32→64同时改变前缀容差和节点数；64→128的真实 DN 路线也不同，
旧已读 `prefix-fixed-g-convergence` 明确记录前者每次实际 DN、后者 actual-outer/affine-inner。
末实际方程与单独真 seam 仍然支付，不能据此把 affine 响应列作成功点。

旧 prefix $C^2$ 差表只是采样诊断，tail metric 最大值本来有小幅非单调；
待审稿没有把它们变为连续高模 RK 误差上界。历史径向证据可进入原 G5 账本，
不能单独支付当前 M14 或任意更高模的源误差。

## 4. 条件 M14/W14 径向入口

### 4.1 真 baseline 与旧硬门

未来 baseline 必须是真正关闭、完整审过的 M14/W14 联解：
自己的 CP、所有 PPoly 分片、真实 outer 原 BC、自己最后的 Jac/audit seam，
以及 root 的实际工具退出观察。首 DN、活动 iteration、捕获异常的 exit0、
affine predictor 或另一个旧响应都不能代替。

当前 `db6f-prefix-spectral-true-m14.py.validate_inputs` 明确绑定 P8/S32/audit32，
并把完整 config 对照原 `expected_config`；当前 auditor 又把响应 parameters
在仅除五个 I/O 键之后严格比对旧真实 warm。
因此单改 config 后复用当前入口会被正确拒绝。
未来 S64 必须另建最小新 selector/preparer/auditor，并重新审查新来源身份。

本次独立重哈希了当前冻结 launch 的106件绑定；这里只核已冻结入口，
没有据它推断当前 attempt01 或 attempt02 的运行结果。
作者原稿中的“运行结果尚待 root 观察”是其封存时的状态；本审不把历史现在时当作最新进度。

### 4.2 同 stage 的 warm 复制

固定 M14、physicalDepth12、P8 后，旧/new stage 布局不因 S32→64而改变。
`remeshCheckpoint` 在 `rawLeft*oldParts` 为整数时，复制原保存 Q/Pi，
并 `continue` 跳过潜在插值 RK。
它仍会为潜在分支构造旧 engine；“没有进入插值积分”不等于“完全没有构造 engine”。

独立检查按源码的 profile 逆序和 stage 逆序，使用精确有理端点逐个计算复制来源，
确认全部865个状态节点均为恒等索引，包含13个 raw 节点及其间852个内点。
当前已闭 seed 的自有 warm 确为865×28、rawNode 13、stage depth864；
未读取这些数组进入对话，也未对它们作新数值 flow。

初猜从旧 Q/Pi 复制并不意味着它满足新的 S64 方程。
fresh client 的 cache 为空，新 dn 按新 config 构造；原 ratio warm 和全部模的边值线性修正仍在。
原自由 cut 的 $p_0$ 与其它参数必须继续由真实 BVP 求，不把旧 H 固定成新的辅助问题。

### 4.3 原 outer、谱权与后验验证

原 `solve_with_actual_tail` 最多8轮：每轮临时 affine DN 仅供 inner BVP，
随后恢复真实 tail、取得新真 DN/J、检查原 BC；最终 seam 再发 Jac/audit 请求。
`TailMixin.seam_audit` 的角数是 $\max(512,64M)$，M14为896，与尾 $N_\theta$ 分开。
现 selector 的 W14 由 `runner.solve_bvp=selected` 注入；
未来若直接调用原 flat-coupled，确实不会自动获得同一谱权。

可选接口只改 nonlinear S/auditSteps及独立 I/O，保留原其它数字、类型、容差、floor、
Node heap和物理回调。未来更换选择层也必须保留运行期 Newton/物理回调身份门。
新的实际图仍须自己的全部公共 C²接合、metric、曲率/支撑、reach、握持和网格证书；
旧 XYZ 或 old metric/κ 的数值不因源设置相近而自动转移。

## 5. 实际独立检查与留痕

独立纯检查程序：
`scripts/db6f-tail-review-g5-axes-and-m14-native-rk.py`，17738 bytes，SHA256
`0f9ab65f47f2daeb6cbc029e4083a5d32cdbc9e898f072000e189c68f191c0a3`。

正常执行的实际工具 receipt 为 **`10ff5c`，exit0**；报告
`tail-review-g5-axes-and-m14-native-rk-check.json`，11166 bytes，SHA256
`6ca212ab3885dc8ef2ba048eb41c16a6eb85ccf082513e6ed9adadebd487a341`。
它核30作者来源、106当前冻结入口、3个历史真闭包、865个精确复制索引、两对嵌套基础网格，
并为全文阅读的11个实现文件保留29个静态定位锚点。
静态锚点只帮助定位和复核，不代替本稿的语义审查。

检查程序定稿前的一次实际 `4f9aa6/exit1` 在最后的源码定位断言拒绝：
本审程序把局部变量名误写成 `flat.m.solve_bvp`，真实源为 `runner.solve_bvp`。
修正的只是尚未封存的检查程序定位文字；原作者稿和全部数学源码均未改。
该次没有写出成功报告，后续上述正常 exit0 才是本次结论依据。

本审通过的是条件协议与已有历史的准确归类。没有新求解、没有新完整闭图，
没有自动 G5=true；若将来完整图已达原容差并付清既有 G5 和 README 全部门，
本稿不会再机械追加一档 S64。若仍未达到，则据实际误差来源继续原问题研究。
