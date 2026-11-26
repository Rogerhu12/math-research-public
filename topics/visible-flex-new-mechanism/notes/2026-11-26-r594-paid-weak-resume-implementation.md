# R594 paid 八模真实续接：实际 496q、damping 与域内位置差分

日期：2026-11-26。会话：Astra-new-mechanism-0105020f-20261126。

## 1. 续接的是哪个实际状态

原 [run 45822196061](https://github.com/Rogerhu12/math-research-public/actions/runs/45822196061)、job 139917033661、提交 `7c80b8bf496d796e5204538b50d2424fd8df0ccc` 自然完成 60 次真实接受，状态为 `declared_iteration_limit`；最后一步仍下降。完整收据见 `2026-11-26-r594-eight-mode-weak-natural-final.md`。本次直接从它的 iteration60 继续最多 60 个迭代标签 60…119，没有把原零增量或更早 q 重跑。

- 实际 496q 紧凑 JSON：10887 B，SHA256 `371f15bc0133badcb4a2fae4a1513c56c2aa156eb558e75ef651cfc9d8e93650`。
- 真实 H=0.5188892674755166，幅度仍为 $10^{-5}$。
- 原 stdout 1132326 B / `598a09eab8eb5de6753c7334a76db5305c4032c3d48a682a97583d219f263fea`。
- 原 FINAL JSON 45724 B / `249d77bf9367ac9cfa62eef12c0afd191bd941217dd9fa231d620199e0d10c8d`。
- 原弱算子 SHA256 `4a4ef267e6b35d9eae59acc96441aa50ded2ead3f57e90f86a9da49c90f005bb`。

整个原 265q 高度场及 67 knots 继续由绑定原源码完整保留，不能只恢复新 496q 然后丢失原 pre-tanh 及 paid forced-j4。原 forced H=.5188895813736972、归一 16533.1541790287 仍由原重建器使用，不换成当前 H。

输入是实际小状态、四个新模原 mouth 参数与原费用，通过既有 stdin runner 传入并核 SHA。原 stdout、完整 checkpoint 和可重算的场表不写入仓库。

## 2. damping 的真实恢复

原 solve_stage 从 $10^{-5}$ 开始；每次实际接受的 trial 指数 k 更新

$$
d_{\rm next}=\max(10^{-14},d\,10^k/3).
$$

原 60 条 ACCEPTANCE 逐条解析后，trial 全为 0，因此实际 iteration60 后的 damping 已达到 $10^{-14}$。最后 backtrack fraction=.5 不进入上述规则，不能把它另乘到 damping 上。请求保存全部 60 个原 trial 指数；新程序只进行这个标量元数据递推，并要求所得值与输入 $10^{-14}$ 一致，不重新优化任何旧步骤。

新迭代保留原列范数尺度、完整 SVD、全部方向、8 个 damping 候选、9 个回溯步、函数 jets 步长限制及实际完整弱 merit 严格下降规则。唯一恢复差异是从真实末 damping 开始，而不是重置为 $10^{-5}$。所有新 ACCEPTANCE 和完整状态立即打印 damping_before、lambda、actual_next_damping 或等价完整状态字段。

原解析 Jacobian 的唯一方向观察已经支付，relative L2=$3.4687281030087757\times10^{-15}$。本次算子及表示没有变，不重跑旧方向门。每一步仍按当前实际 q 计算真正需要的完整 Jacobian 和残差。

## 3. 全部八模的 paid 尾输入与必要重建

原低四模 2/4/6/8 仍走已发布 PaidFlatSeed。新高四模 10/12/14/16 的原 `WEAK_BVP_NEW_TRUE_MODE.finite_inner_data` 全部复用：

- 各自 M=25、terminal peak index26、alpha17；
- 原 balanced z(alpha17) 与 rho18；
- 原 display log scale；
- 原 13 个出口 jets。

这些数据来自原一次正式运行。没有新 `inner_slope` / Riccati 链，没有新 H shooting，没有新增频率或改变尾公式。

原日志没有存 dense 内插场，继续在任意新径向点上求值仍须从已付 alpha17 Cauchy 方向重建 dense 外传，再重建原 connector/core。所有 RHS、几何求值、源项和高度求积都如实计费。本次不把“口已付”解释成“重建免费”。

对于四个高模，connector 的初值明确直接使用原 13 个 jets 中对应的原 A/C 数据；display normalization 与原定义相同。dense 重建自己的 13 个口值与原记录之差逐分量打印，作为实际 ODE 重建误差观察；它不是另一次旧检查 gate，也不被设为零。核心 A 归一仍由原 AdmissibleMode 求解决定，并打印相对原 raw Acore/Ccore 的差。因此相同 496q 的高度表示若受数值重建误差影响，会明确暴露；没有把浮点重建当作严格同场或准确无限尾误差证书。

原支持 [.55,.65] 的准确二jet core trace 修正仍完整进入高度与残差；本包不把 Ccore 的强制零误称为未修正原射击核。

## 4. 保留所有原 r 的实际位置差分

首 run 的最坏 direct metric 观察落在数值窗口首点 r=0.22184543511708774。旧公式使该点 h 约为 $4.44\times10^{-14}$，半步后误差进一步放大。本次不删这个点、不平移观测网、不把准确核心端条件换成 $R-\varepsilon$。

对每个原 r 设

$$
h=\mathrm{factor}\,\min(2\times10^{-5},.002(R-r)),
\qquad \mathrm{factor}\in\{1,1/2\}.
$$

若 $r-2h>r_{\min}$，使用五点中心四阶：

$$
Y_r\approx\frac{Y_{-2}-8Y_{-1}+8Y_1-Y_2}{12h},
\qquad
Y_{rr}\approx\frac{-Y_{-2}+16Y_{-1}-30Y_0+16Y_1-Y_2}{12h^2}.
$$

否则在相同目标点 r 使用域内 $r,r+h,\ldots,r+5h$：

$$
Y_r\approx\frac{-25Y_0+48Y_1-36Y_2+16Y_3-3Y_4}{12h},
$$

$$
Y_{rr}\approx
\frac{45Y_0-154Y_1+214Y_2-156Y_3+61Y_4-10Y_5}{12h^2}.
$$

单侧二阶导系数的 0、1、3、4、5 次矩为零，二次矩为24；除以 $12h^2$ 后得到准确二阶主项且四阶截断阶。单侧一阶导同样消去 0、2、3、4 次矩，一次矩12。这里的阶仅说明光滑点的形式截断阶，不授全域连续误差。

实现先取每个偏移的 $Y_k-Y_0$，再作上述线性组合，取消常量项。中心/前向分支使用五次偏移位置求值。前向偏移可能跨过原网中邻近 r，因此每个偏移向量先稳定排序后传给 prepare，再用原排列恢复到各原目标 r；这样 prepare 的径向权不出现负号，目标点一个也不丢失。

因 $h\le .002(R-r)$，前向最远点满足 $r+5h<R$；中心分支的最左点则由显式分支条件保证。程序还逐点检查这些条件。

实际重构曲率和 metric 仍由实际 Y 的这些径向差分、其角向谱导数和所定义高度 Z 的解析 jets 重新组成 E/F/G、法向与二次基本形式，完全保留 G 的实际缺陷。不是用 R576 恒等式冒充位置导数。

每套观察明确打印：

- h 的全局最小、最大与首末原 r 的 h；
- metric、曲率及最大 Yr 差的真实 attainer 和对应 h；
- 中心/前向点数、原 r 总数与首末 r；
- 实际 metric、outward、曲率、角 G 缺陷和恒等式/位置 Yr 差；
- 同一真实 q 的 h 与 h/2 两套结果。

仍不把这两次浮点差分授为连续、区间或 reach 证书。

## 5. 原完整弱问题及资格门保持

模式仍为 2、4、6、8、10、12、14、16，原496维空间、完整 paid 高度、现有67 knots、128角 active /256角 fine、原完整核心 finite trace 均保留。仍不除可能失号的 a；采样弱主块 rank/singular 信息仍随状态报告。

完整 core D 的0…34模、整个 body D 的0…40模（包括当前未求解的18…32）和细网指标全部保留。本次不因为原 m18 泄漏而临时加新频率；R600只是后续可用的准确尾范围，不是本次免费新输入。

实际新步只按原完整弱 merit 接受；若 fine eta 与两套真实位置 eta 未同时小于 $2\times10^{-9}$、或相应高度/outward门未过，仍显示 qualification false。merit 下降不被包装为完整等距误差下降。本 scope 仅当前幅度的下一60步，结束后交付真实末态继续研究，不声称完成原 README。

## 6. 状态和全部投入

在求下一步前、每次实际接受后均打印完整496q、真实全局 iteration、damping、原弱 merit、完整核心和 mass 观察。保留态先写入 model.actual_checkpoint，再 flush；若新 trial 或 readout 中断，FINAL 回到最后实际接受的 q/amplitude/damping，而不是最后试探值。

原运行 elapsed=452.79767207 s 及全部原计数在输入中保留为原费用，不加入本次计数冒充新进展，也不抹去更早原 forced run 的460.575048554 s。必要 dense/core 重建、本次优化、实际位置偏移求值、H 积分与原完整几何计算均计入本次实际 elapsed 与各原计数器。新增 resume_counts 另列四高模 dense RHS 和 stencil 几何点数；其中与底层总计有包含关系，不能机械重复相加。

## 7. 文件与执行范围

- `scripts/r594_paid_weak_resume_20261126.py`。
- `computations/request-r594-paid-weak-resume-20261126.json`。
- `.github/workflows/visible-r594-paid-weak-resume-20261126.yml`。

复用已付 stdin runner：真实 pull 两仓、检查 README 与 QUEUE、绑定所有源码/工作流、移除凭证后再公开执行。单 job，科学2400秒，job45分钟；原 Python/numpy/scipy 固定版本保留。工作流只由本新请求触发，与旧八模队列共享 concurrency。

本地只解析原已终态日志、恢复小状态/标量 damping、静态读源及 AST/JSON/hash/sparse 核对；未执行模型、求积、优化或新数值核。本包不保存 raw 场表、artifact、Release、Git 科学输出或跨 run cache。度量仍随静态设计参数变化，固定 g 和连续全频/全尾、嵌入/reach 完成标准仍未支付。
