# continuation03：从真实 call15 恢复的冻结来源接口

作者 coupled_prefix；2026-11-09。**只准备原控制器启动文件，不启动求解。**

## 1. 实际恢复点和中断身份

恢复输入为 continuation02 的完整闭响应：

    notes/2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02_tail_0015.json.gz

SHA256 为 e6ef3389c839be9f793a11d875d99c616c207acc58b680efc0bda2c005e55c1f。它是 $s=31/32$ 的实际有限 DN 真成功，原 residual 为 6.367950627222893e−10，小于原 tol 2e−9；history 有 7 个基点评估，state 为 865×30，rawNode 为 0、72、…、864，对应 13×30 的 rawStates。请求 jacobian=false、audit=false，返回没有 Jacobian/source audit；本准备器没有把它重标成完整目标或前缀。

根实际观察记录 root-amplitude-resume02-observed-execution.json（SHA 5cda4dd0fd47dd002b4c57fc648152a6307de27b9a67d5ae00090c9eab8e496e）及其九个绑定文件为必需输入。其内容是 root/session17869/receipt cf4fa6 实际工具 exit1，原因 ENOSPC；child 和 worker 的直接退出值没有记录，仍为 null。call16 的完整响应和最终 reproduction 均不存在，旧 progress 是陈旧的 RUNNING 状态。本准备器不使用 call16 中间 iteration，不把磁盘故障视为数值失败，也不要求旧 02 被伪造为 clean exit。

## 2. 准备器的有限核验

scripts/db6f-prefix-prepare-amplitude-resume03.py 全部只做本地元数据/哈希/数组有限性检查：

- 旧 02 launch 固定 SHA，原 66 个绑定逐字节核验；原 controller/client 固定 SHA 不变。
- call15 已发布闭审的 8 件文件及闭审程序源码逐项核验，额外核真实响应的精确 8 源集合。
- 根 ENOSPC 记录、原因 Markdown 及九件闭文件全部绑定；不从文件存在推断进程退出。
- 原 config 与 call15 record.config 去掉五个 I/O 键后，以 canonical JSON 作逐类型比较；bool 不与 0/1 混同。M15/N256/depth12/shootingParts8/steps32、max36、tol2e−9、原 .05 guard、默认开启的 initial-boundary correction 保持不变。
- 原目标仍是明确 UNSOLVED 的 affine prefix。用原控制器相同的 NumPy 表达式
  $H_j(s)=H_{{\rm goal},j}\,s^{j+1}$，逐值比较 request.height 与 checkpoint.cutHeight，$s=31/32$。
- 形状节点及 raw 镜像全部是非 bool 的有限数，rawNode 必须是原精确整数布局。call15 的历史序号仍为原 0,…,6。

准备器拒绝已用的 03 输出 stem，并拒绝覆盖任何准备元数据。它不会预建 03-config.json：这个文件仍由原控制器在运行时创建，否则原控制器的 output-prefix 拒覆盖门会正确拒绝。准备元数据名字放在独立的 prefix-amplitude-resume03 前缀下。

## 3. 原 argv 的唯一四项变更

以旧 02 launch.command 为基准，只替换：

| 选项 | 新值 |
|---|---|
| --out-prefix | notes/2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-03 的绝对路径 |
| --initial-step | .015625，即 1/64 |
| --resume-checkpoint | 上述真实 02_tail_0015.json.gz 的绝对路径 |
| --resume-scale | .96875，即 31/32 |

其余 token 逐项不变：原 Python/控制器/source-root/config01/affine target，initial-scale .25、maximum-step .2、minimum-step 1/4096、max-attempts64、node-heap1536。有 resume 时 initial-scale 不用于首个新请求；实际首个新请求为
$$
\min(1,31/32+1/64)=63/64.
$$
随后仍按原控制器自适应：只有真实成功才更新 last；失败退回 last 并减半步长，成功 history 超过 7 时也会减步。因此不能预先宣称只需两次新请求或下一次必为 1。

原控制器拷贝原 config，先去掉旧 initialCheckpoint，再设置 call15 作为新 initialCheckpoint；另外四条 I/O 路径全部指向新 03 stem。fresh client 没有旧 cache。原 worker 只将旧 CP 当 warm，保留默认全模边界修正，重新求原方程。

完整可执行 argv、cwd 和 stdout_log 均在 prefix-amplitude-resume03-launch.json；根持有长工具会话。记录实际退出的根 wrapper 必须使用独立 observed-execution 文件，不能覆盖原控制器自己生成的 03-reproduction.json。

## 4. 最终门仍待实际运行

当原控制器真的达到 $s=1$，它会再把原 goal.copy() 作为唯一目标向量，发出 jacobian=true、audit=true 的原实际请求。03 真结束后仍必须核：

1. 03 自身的真实工具退出和 worker 退出；
2. target_reached、target_audited 以及对应最终成功 status；
3. 新最终 response 的原目标、原 residual、17 个 cut-jet 字段、705 个原 Jacobian 条目、实际 source audit 和全部来源；
4. controller 自身 reproduction/progress/config/最终响应的闭合绑定。

原控制器会捕获部分异常并写 UNCONVERGED 状态，所以工具 exit0 单独不支付这些门。即使最终目标 DN 真成功，原 M15 prefix 仍须外层原 BC 校正，随后才是 N512 校正和实际图认证。

旧 prepare-final-m15-coupling-v2 的 continuation02 身份门保持原字节。将来使用 03 时，新的 v3 必须明确绑定 03 的 launch、progress、reproduction、实际观察和最终响应；不能把 03 的结果伪装成 02 完成。

## 5. 作者执行事实

正式准备运行实际 exit0，receipt 77b2b6；生成 source-check 和含 83 件绑定的 launch，零求解器调用。首次未冻结自检把 CP 实际字段 rawNode 误写成 rawNodeIndices，receipt 77a2fd 实际 exit1；当时尚未写任何输出。仅将这一键名改成实际 schema 后重跑通过。这是元数据准备笔误，不是 call15 数据拒绝或数学失败。正式源码、报告和 launch 随后冻结，未修改任何原控制器、client、旧运行文件或当前物理参数。
