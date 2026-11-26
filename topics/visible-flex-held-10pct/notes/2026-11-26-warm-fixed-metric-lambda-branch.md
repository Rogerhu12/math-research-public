# 从真实小正 λ 场进入暖支撑核心：固定完整 g 的独立 λ 设计分支

会话：Astra-held10-06bbeb39-20261126 / fixed_metric。**状态：可执行入口已写；只做了下面列出的轻量核心接口实测，尚未运行新的 BVP，没有 accepted 暖场。** 原 M24 冷恢复失败与新低 q 恢复链由 root/actual_tail 单独记录；本文不把恢复重记为数学结论。

## 与原分支的关系

R65 的零控制恒等不要求接近 λ=1。只要已有一个真实 accepted R53 场且源 λ*>0，就可固定它的完整 support 向量 b*，取
$$\Phi(u;\lambda,d)=\phi_{R53}(u;\lambda,b_*)+
\sum_{j\ge1}d_j\frac{W(u)\sin(3ju)}{3jN_j}.$$
在源 λ*、d=0 时，完整 Γ/Γ′/Γ″ 直接取原 live baseline，位置增量用 expm1 积分，恒等不是采样拟合或只保曲率。R48 的 Y 转移系数仍为 1；升 M 使用零扩展及完整 reference lift 差。先通过旧实际 chart 把源 PPoly 解释为物理 s，再进入冻结 actual δ 的新 chart。若源的 mean 规则也是 1168，这一转移保持完整 Cartesian 图；脚本单独记录源 mean 是否一致，不把其它节点数冒称同图。

物理 g 的 actual δ、全部 profile/尾背景参数、角图、数值 gauge=.06、mean1168 和 core 的目标曲率/保护窗固定。新 p0=log(q_aux/gauge)，d_j=phase_scale·p_(j−1)；q_aux 只是新第一相位控制的正坐标，绝不作为支撑幅度或 Y 的 gauge。原固定模式 BVP 的 M 个未知参数全部进入真实核心；第 0 列保持原 analytic Jacobian 的链式因子。旧 [.055,.065] support 幅度门不适用于这个新坐标，也没有用它声称非圆性；最终 λ=1 的 k=.2 准确圆弧及周长 2π 本身排除圆。

λ 在设计过程中变化，所以父链明确为 fixed_metric=True、fixed_metric_refinement=False。这不是一个完整固定边值问题的加密序列。最终 λ1 后，`warm_fixed_m3_step.py` 可用相同 λ、相同冻结定义、不同 modes/angular/refine/tol 继续；此时记录 same_complete_problem_as_source 和 fixed_metric_refinement 为 true，但只有实际完整 C2 比较及误差下降才可讨论收敛。全程保留原 **linear DN**，不会把它改称实际 fullH。

## 三个入口与 provider 改动

- `scripts/resume_20261126/warm_fixed_m3_continue.py`：参数 `--repo --work --source-run --outdir [--port32]`。先在源 λ 做零控制暖交接，再默认 .004/.008/.016/.032/.064/.128/.256/.512/.75/1；目标不大于已接受 λ 的项跳过。失败据真实返回缩步或升谱。收敛但 metric 不过的场仅在同 λ 升谱时作有标签的 Newton seed，绝不记 accepted。summary.json 提供现有 worker 需要的 status/stages/progress/result/error。
- `warm_fixed_m3_step.py`：单次真实原 BVP，参数 `--source-run --outdir [--homotopy --modes --angular --port --refine --tol --bc-tol --physical-bc-tol]`。原 Frenet/曲率/domain guard、DomainNewton、RMS 域门、analytic Jacobian、固定 BC normalization=.02 全保留；有限 acceptance 要求 solver、原 normalized BC、physical BC、全相对 metric 的有限 FFT component 和 sampled operator 均过原门。实际角审计将每个请求节点数提升至至少原 `16*(3M+1)`，去重后记录，M24/M32 分别至少 1168/1552；mean1168 仍独立冻结，不能把升谱后的 512/1024 审计冒称原采样范围。每次先保存 raw return，再导 physical C2 图及完整 metric diagnostics。
- `warm_fixed_m3_model.py`：只读重建，供实际场比较/metric 审计。它自己定义 source signature 和两个 lift-transfer helper，不依赖旧 branch 的 qrange 验收。旧几何构造器把核心 factory 捕获在闭包中，因此此入口在安装暖 factory 后新建原 Flow/Base，再安装原 exact lift 和 analytic Jacobian；旧模型仍保留用于转移，没有只改全局名字的假交接。
- `warm_fixed_m3_compare_c2.py`：`--first-run --second-run --out`。只接两个实际已过门且完整 warm_definition（包括 λ、冻结 b*、相位尺度）相同的场；在同一 mean1168、共同物理 s 和同一材料角图比较完整六个 Cartesian jet。原 physical/raw/port SHA 和参数交叉核对；相位 d 的零扩展加权 l1 差按 literal binary 参数的有理数精确计算，不把 q_aux 当支撑系数。尚无两份 accepted 暖场，未进行虚构数值比较；本入口的 compile 与 --help 已实际通过。
- `warm_supported_core_factory.py` 仅新增可选 `homotopy` override。`anchor_core_settings` 保存源 λ 和完整源定义，不被目标 λ 覆盖；只在建立当前 baseline 时使用 override。

源 run/raw/physical 的真实 SHA、原 numerical sources 的 SHA、完整 source chart 和 frozen profile 都核对；不硬编码旧 dc85 chart。新低 q 恢复链若使用新的已声明 chart，只要整个当前分支保持该 chart，入口如实继承它。实际 nonlinear tail 输入会被此 linear-only 入口拒绝，不能通过换标签丢掉原真实边界。

## 已执行的最小接口检查

`py_compile` 覆盖三个新入口、factory 和 check；两个可执行入口 `--help` 成功。`check_warm_lambda_entry.py` 的实际命令为：

```sh
python scripts/resume_20261126/check_warm_lambda_entry.py \
  --repo /path/to/math-research-public \
  --reference-source /path/to/original/fixed_metric_mode3_core.py \
  --out /scratch/warm-lambda-entry-check.json
```

在 q=.06、M=8、原 support 的七个修正均为 0 的**合成核心**上，分别 λ=.002、.5、1，34 个材料点的 live zero-control Γ/Γ′/Γ″ 全部字面相等；通过可选 override 独立重建的 baseline 对这三个 jet 的差也全部为 0。对新 BVP 列 0 和 7 做中心差分 h=1e−6，与 analytic two-jet 链式导数比较，最大绝对误差为 `1.5614270987285295e-10`。源 anchor 设置仍为 λ=.002，未被后两档修改。

这验证的是新 λ override 和原参数链的接口，不是 accepted BVP 或近 λ1 场，更不是同 g 收敛。没有在本地重跑大型矩阵。

执行来源 SHA-256：

| 输入/输出 | SHA-256 |
|---|---|
| genuine original support reference | `fa8576bb1d592ee0e0152082b9ee722a1f1a86738f21a906bb0f3ac88e38707c` |
| 原 R53 material_flattened_support_core.py | `1d655f2bdad53e1d320c1115a9873abe399a9b7ba930722c415d02dedb9b1f20` |
| 本次 factory | `9192499334d9f8603c812cd95964cc660a065132a82ce240fe2331f64c9b14dc` |
| check_warm_lambda_entry.py | `34ac709e7550b57c478810528f59af2d9be59f8aae8717336328cd73395c3af4` |
| 合成检查输出（可重算，不入库） | `aad6328e72426f84d8bd0322b0861ef84749a7f8d4249976506cda14b7bc4b22` |

当前新恢复场仍在真正的 q checkpoint 链上。此独立入口等待同 runner 的 accepted 正 λ M24 run/raw/physical，然后实际执行；不改原 λ 设计或真尾分支的 source input。

## 同runner执行安排和可观测性

当前旧lowq长命令的repo只在小时pull时更新，且已经选择原真尾/旧fixed-g诊断/旧λ设计；它继续保有自己的实际场。其汇总超过worker原64KiB时，旧worker仅发布omitted，这不是数学失败，不能推断M24或子路终态。

独立warm通道用同一已真实成功的小q链必要再生一份本runner状态（不是重登记旧结论），M24原门后直接进入本新phase控制族，不重复启动原三路。请求为held10-warm-supported-route-20261126-01，bootstrap仍恢复相同源/物理输入；新chart明确按实际setup绑定。完整场不跨runner上传，旧两个runner不取消。

新worker保持原64KiB/1MiB限制、原路径与键白名单。超总量先裁去重复历史/源码列表并保各路status/error；同一活跃id、script、args允许只刷新经原检查的diagnostics，无需重启数学进程。请求默认不投影含完整commands的stages，源和各单run仍全在runner。该改动不影响已经载入旧worker的两个进程，也不修改任何数学门。
