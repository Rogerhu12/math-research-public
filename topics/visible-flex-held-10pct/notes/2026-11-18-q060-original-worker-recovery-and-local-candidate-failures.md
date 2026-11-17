# q060 原 worker 续接接口与三次局部候选失败

## 结论与范围

**数值证据／工程接口，非存在性或非存在性证明。**

`beta4625-q060-local-tail-retry` 的原联立 run 在 call3 的新完整高度向量
处线搜索失败；原记录为
`seed_tail_0003.json.gz`，SHA-256
`6059334fa00c9fe6ce4bca788dff852f4da0988b920c5ad7e7f22b7fad65e35b`。
其原 full-Jacobian 范数为
$3.241344522795531\times10^{-9}$，原门是严格小于 $2\times10^{-9}$。
以下三次新执行只尝试内部初值，均完整复核原方程，没有调用 `dn.solve`。
它们没有得到严格改善，也没有新 DN、前缀或闭曲面接受结果。

另已实现独立的原 worker 恢复客户端和 owned-source 入口。
它保存内层真实三次插值与所用 actual-DN 锚点；只在外部初值经原全残差
严格改善后，才允许原 worker 对相同物理高度重试一次。
当前三次候选均未触发这个重试分支。该接口尚无成功恢复的端到端执行，
不得把源准备完成写成新求解接受。

## 同一真实失败态上的有限搜索

所有版本使用同一输入、同一物理配置和同一原全残差实现：
$M=8$、spacing $3$、depth $8$、quadrature $128$、RK steps $16$、
shooting parts $8$。完整状态为 $577\times16$；完整八维边界高度不改。
已存在的原 locator
`call3-locate.json`（SHA
`7f64fdb1bf18c455318ce507bb9d131fe62a3c10cab6bb69c98da2dc27b73e63`）
只用于绑定同一输入及原范数，没有重跑定位计算。

内部 shooting 方程写成
$R_i=\Phi_i(X_{i+1})-X_i$，其中动量分量保留原 `portRatio` 变换。
改变节点集合 $S$ 时，精确重算的行集合为
$\bigcup_{i\in S}\{i-1,i\}$，并去掉越界行；第二节点变化因此确实
包含 $i-2$ 行。其他行沿用最近一次真正重算的原残差。
完整左端 Dirichlet 和远端 Robin 残差也加入候选总范数。
候选的局部流继续用原 `flowStateWithJacobian`，域失败只丢弃该候选。
每轮只接受总范数严格下降的候选；最多 16 轮。
最终必须再调用一次原全域 `evaluate(..., true, scales)`，且其范数必须
逐位等于局部依赖缓存预测值。这里只是初值筛选，不是原 DN 接受门。

| 版本 | 唯一新增选择 | 每轮理论上限 | 实际候选数 | 选中轮数 | 完整 replay |
|---|---|---:|---:|---:|---:|
| v1 | 原八个 $\alpha$、五个 $\beta$ | 48 | 23 | 0 | $3.241344522795531\times10^{-9}$ |
| v2 | 增加 $\alpha=1/128,1/64,1/32,1/16$ | 72 | 27 | 0 | 同上 |
| v3 | 仅放宽第二节点候选分支资格 | 72 | 72 | 0 | 同上 |

原八个 $\alpha$ 是
$1/8,1/4,5/16,1/3,3/8,1/2,3/4,1$；
五个 $\beta$ 是 $1/8,1/4,1/2,3/4,1$。
没有对产生相同 binary64 数的候选去重，因此实际计数如实包括重复值。
v2 相对 v1 的源只替换上述 $\alpha$ 常量。
v3 相对 v2 只把
`downstream.norm > cfg.solveTolerance`
替换成
`downstream.norm >= currentNorm` 作为跳过第二节点候选的条件；
原 upstream 条件、列表、16 轮限制、全 replay 和原 solver 门均未变化。
该替换改变的是初值搜索分支资格，不是接受阈值。

峰位于零基编号 stage45/component11，即 mode12 动量，原差约 70 ULP。
v1 最小 $\alpha=1/8$ 移动约 9 ULP，把邻 stage44 推至
$4.1940029467591604\times10^{-9}$。
v2 的 $1/128$、$1/64$ 都实际移动 1 ULP：stage45 降至
$3.195039601041309\times10^{-9}$，但 stage44 升至
$5.061727694364504\times10^{-9}$。
因此失败不能只归于最小步过粗。
v3 真正尝试对应第二节点修补后，最佳已试组合
$(\alpha,\beta)=(1/128,1/4)$ 的总范数仍为
$3.760140572956488\times10^{-9}$，高于原值。
三版本都在第一轮停止，没有修改任何原内部状态。
它们的全 replay 都给 minA $0.5220201871565618$、
minD $0.9991195608484377$；完整边界范数为
$2.5533258603093732\times10^{-14}$，左端补正本身严格为零。

三次真实终态分别为 session62324、80768、50321，均 exit0；
运行时间为 18.3522、21.6484、18.6799 秒。
这三个 exit0 只表示候选生成与复核正常结束，输出明确
`solver_success=false`、`candidate_only=true`、
`original_solver_invoked=false`。

## 原 worker 续接的身份与状态

`recovering_tail_client.py` 继承未经修改的原 `WeightedTailPort`。
正常路径直接调用原方法；只有原方法已经写出完整失败记录后，才运行一次
candidate-only 外部器。若未严格改善，则保留原失败并退出该逻辑请求。
若改善，则关闭旧 worker，通过原 worker 已有的 `initialCheckpoint`
协议加载候选，要求其原方法完成同一整个高度向量的 DN/Jacobian/audit。
外部器不能合成 `converged`、不能填入客户端缓存，也不能替代返回响应。
原 worker 接受后自然保留自己的 `last` 状态，供后续新高度续接。

恢复时只能改 initializer/trace 元数据路径；物理、离散化、原求解门和
迭代配置全部逐项不变。完整 ready 数据与原八个 client/worker 源哈希
必须不变；31 个 runtime 源、sparse helper、owned adapter 和候选器源
也绑定并检查。source root 的解析路径必须与候选器使用的原 root 一致。
当前 sparse helper 使用当前 publication 副本，不依赖旧 session 目录。

原客户端构造器禁止复用已有记录前缀。恢复代码用未发过请求的临时
bootstrap 前缀启动原 worker，再恢复原记录前缀和累计 call 数；
event 记录每个 generation 与该 worker 内部 call 的对应关系。
每个失败逻辑请求至多一次外部候选及一次原生重试，调用原方法而不递归
进入恢复函数。重试总要求 `jacobian=true,audit=true`，物理高度与原请求
逐项相同；这不声称 audit 标志与原 `audit=false` 字面请求完全相同。

reload 的比值与边界补正使用独立的同一 JavaScript 算术检查：
`height[0]/checkpoint.cutHeight[0] === 1`，且每个
`height[j]/radius**4 - states[0][j]` 为正零。
还排除会被 `+0` 改写的负零状态。当前 v3 真实输出通过此检查：
radius $.3$、比值 1、全部左端补正零；此检查没有构造 DN 或调用求解器。
原 parts 不变的重启使用原 remesh 的节点复制分支。

## 保留原 inner 三次场，不冒充已接受前缀

`prepare_recovering_tail_source.py` 只新建 owned overlay，不改原源。
原 coupler SHA 是
`37defb33c031fd967ab0e06e086da56f2d67e30dd88bbbcb8e5e13201476511a`。
它原样应用已提交的 `install_inner_prefix_debug_record.py`，然后只在
原 actual-tail 请求之前插入一个独立 DN 锚点 sidecar 调用。
去掉这两处保存操作和原 dump helper 后，代码逐字恢复原 coupler。
原方程、边界、outer 更新及接受顺序不改。

原 dump 保存 `sol.x/y/p`、原独立变量坐标、三次插值 breaks/coefficients、
物理参数、完整 candidate height 及所有输入来源；明确
`solver_success=false`、`actual_tail_accepted=false`。
新增 sidecar 将它与本 inner affine 问题实际使用的已接受 DN 记录、
完整 request、response hash、配置、generation/calls 和原求解选项绑定。
后续失败时可据此精确续接原 cubic，而无需把 physical quintic 重建误称
原 cubic 状态。

旧 call3 run 没有这个 dump，不能凭本接口补造其丢失的 `sol`。
因此没有重跑前缀来重复产生同一失败；后续先测试同物理请求的原
parts8→16 嵌套离散化，只有新的原尾结果有用后才重启有保存能力的联立。
该新实验另行记录，不计入本条三次候选结果。

## 来源、复现与不足

完整来源和输出 SHA 见
`scripts/resume_transfer/q060_internal_candidate_recovery_execution.json`。
原始候选表、状态和全 replay 输出只在 scratch；Git 仅保脚本、参数、
命令、哈希和上述紧凑标量。`record_q060_internal_candidates.py` 仅核对并
抽取这些执行记录，不重跑方程。源准备真实 exit0，owned client 已作
纯导入检查，未启动 worker。

当前 owned 入口是
`/workspace/scratch/7322d0dee069/closed_work/q060-recovery-v3-source`，
准备清单是同层 `q060-recovery-v3-source-manifest.json`。
可复现准备命令：

```bash
python scripts/resume_transfer/prepare_recovering_tail_source.py \
  --source-topic "$CURRENT_ORIGINAL_TOPIC" \
  --owned-topic "$NEW_OWNED_TOPIC" \
  --manifest "$NEW_MANIFEST"
```

这里环境变量只表示调用者提供的明确路径。原 worker 必须使用相同 runtime
source root；实际运行另显式设置当前 sparse helper，并在同配置下使用
新的输出前缀。本条没有通过的局部候选、没有新的 actual prefix，
也没有全闭 metric、握持比例或收敛结论。
