# Gap 1.05 整支的独立冷复生运行契约

## 当前身份

这是一个新 Actions 编排入口和运行配方。写作时，本地执行环境不可用，新的 Controller、request 和 workflow 尚未执行，未产生新 run、基线或接受步。既有数值实现与既有实际结果已分别登记；这里没有把“代码已准备”记为“计算已通过”。

专用入口是 `scripts/6a65-actions-gap105-whole-branch-cold.py`，SHA-256
`3ee599cecb1038d1b6c031b3aab857a5df479972212452ecc028370fb25d8877`。

配方是 `ci-requests/6a65-gap105-whole-branch-cold-20261126.json`，SHA-256
`6630723f4f8723f5c9630f0f67fc1a4c967efa814c4a1adbc16bf17d36844ebf`。

工作流是 `.github/workflows/6a65-gap105-whole-branch-cold.yml`，SHA-256
`7bf0fe97d0896df7a3001cb45807e676826f98cc7f58f4c237b752a34256e209`。

工作流仅由 `main` 上这一个新 request 路径的 push 触发，拥有独立 concurrency group，不修改活动 M12、旧 Cauchy 或原 Cartesian 任务。先执行 `py_compile` 和工厂的 `node --check`，再进入真实数值步骤。Python 3.12、Node 22.23.5、NumPy 2.3.5、SciPy 1.17.0、部分克隆和 unshallow 方式沿用现有公共 Cartesian job；总 job 时限为 350 分钟。这不是停止整个课题的理由，剩余研究仍由主会话推进。

## 一条真实的依赖链

令 S 为本次冻结到 Git 目录之外的 scripts 路径，W 为本次 RUNNER_TEMP 新目录。S 只复制一次，此后每次 live pull 都不会改变当前数值过程所消费的源码。完整 inventory、公开源提交、所有关键源码 SHA 和运行库版本写入实际回执。

1. 直接运行 `6a65-geometry-coupled-gap-prefix.py --scripts-dir S --output-prefix W/coupled-prefix`，生成本次真实 Cauchy ramp、Γ95 coast 和完整端口。固定参数仍为 gap $21/20$、ramp $.06$、slope $.045$、coast $.02$；没有读取历史 NPZ。
2. 从公开 Cauchy recipe 的 `config` 构造明确无 z 的新配置，再运行原工厂的完整 `value`。命令为 `node --expose-gc --max-old-space-size=128 --max-semi-space-size=4 S/6a65-cauchy-global-position.cjs value CANDIDATE W/own-zero-config.json W/own-zero-initial.json`。最后一个参数是完整输出文件名。该新源必须实际给出 INITIAL、`accepted=false`、`cauchyAcceptedSteps=0` 和 `actualValueBaseline=true`。
3. 用新 INITIAL、新 ramp/coast 调用 base driver 的 `prepare`。128 角训练缓存和 192 角观察缓存直接由实际六 jets oracle 生成；必须等原 oracle 自然退出 0 后才封存并复用。prepared 绑定本次 run ID、execution UUID、实际源、自然周长度量、全部物理分段、两套节点与权重、raw 文件 SHA。
4. base driver 的 `solve --steps 1` 给 6 次尝试预算。
5. two-grid driver 给 9 次尝试预算，保留两套网格上各自全部 13 行并采用共同列预条件坐标。
6. refined driver 给 3 次尝试预算，实际把 J32/M12 全 2400 列通过四个物理 knot 插入和 Fourier 包含扩成 J36/M24 全 5292 列。
7. 已实际执行过的原 14 行 area driver 给 12 次后续尝试预算，仍保全部 5292 列、全部旧 13 行，并加入自己的倒面积残差及真实 J/JT。没有改用尚未验证的 compact 缓存草稿。

第 4–7 步每个进程只运行一次真实 Cartesian 尝试，输出 `-initial.json`、`-step01-state.json`、`-report.json`。下一进程只消费本 job 刚保存的实际状态。某个 phase 出现真实拒绝，就结束该 phase，不对同一初值和相同阻尼重复相同尝试；然后进入已明定的下一数值模型。最后一个 phase 的拒绝也如实登记。

6、9、3、12 都是尝试预算。旧会话曾有的 20 次实际接受没有写入新状态；新接受总数只能由本次各步的实际 Boolean acceptance 和保存态计数逐步增长。每次交接校验父 SHA、prepared SHA、sourceIdentity 和实际累计计数。每个新目标都重新计算完整自身 baseline，并分别公开旧 13 行成本、新面积成本及两套实际网格的指标。

每个新进程从原配方阻尼 $10^{-4}$ 开始，因此如果旧多步 batch 曾提高阻尼，这种单进程拆分不保证逐字复现旧数值轨迹。它是同一固定场模型上的明确新执行序列，所有实际数值以新回执为准。

## 前缀证书和新身份的界限

公开 R233 的原件 SHA 分别是：

- ramp：`0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7`；
- coast：`f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d`。

入口会对本次真实生成的文件计算 SHA。只有两项都相同，才记录 R233 原件匹配；匹配也只继承准确形式定义的既有证书，不继承字面浮点评价器尚未支付的舍入界。若不匹配，记录新的前缀身份，不宣称 R233 的 metric、曲率或 C2 结论适用于新原件。旧 raw state 中带 certified 字样的历史字段名不能替代这项实际检查。

源仍使用独立 kind `gap105-short-window-natural-metric-v1`。没有放宽原 Cauchy fixed-source binder，也没有把新 gap 源伪装为旧 CI checkpoint。新自然周长度量在 prepare 后冻结，各个 phase 共享该同一 g。固定前缀的误差仍是小非零数；本编排不宣称已经满足全域趋机器精度的完成标准。

每次子进程真实退出码、耗时、stdout SHA、输入与输出 SHA 都单独记录。若子进程失败前已保存完整状态，入口只在实际文件存在且父、源、prepared、计数都相符时登记该保存态和其实际接受标志，同时保留非零退出事实；没有保存态就不推断接受。

## 每次拉取和 45 分钟规则检查

仅复用已测 v5 publisher 的 `git`、`publish`、`execute_child` 方法。原 Cartesian Controller 的 constructor、schema、binder、one、run 和计数没有被实例化或继承为数据定义。新 wrapper 有自己的源码身份、save 方法和标量报告。

独立 HANDOFF marker 是：

`<!-- 6a65-gap105-whole-branch-cold-ci-rules -->`

首次数值步骤之前先真实 pull 与双 README 差异检查。每条有意义的实际回执立刻普通 commit/push；非快进按原 publisher 立即 pull --rebase 后重推循环。长子进程期间最多 2700 秒触发一次同样的实际 pull、差异检查、HANDOFF 读过提交号记录与小回执发布。数值源始终来自此前冻结的 S。

若 README 有新差异，publisher 先公开实际 pull 提交、差异 SHA 和 HANDOFF 记录，再停止当前数值子进程，交主会话阅读差异并按新规矩继续；不会让旧规则下的数值任务继续运行。只去重逐字相同的本 marker 行，保留别人的 HANDOFF 内容与 marker。HANDOFF 10 KB guard 保留，主会话应在触发前留足空间。

认证沿用 workflow 的 `github.token`，通过 `CART_CONTINUATION_TOKEN` 只给 git 环境；数值子进程移除这些凭据变量。日志、源码、request、标量报告中均不写令牌。


## 同一 runner 保留和薄接收口

初始 6/9/3/12 预算结束后，或 area 出现真实拒绝后，Controller 不退出。它保留本次实际源、缓存和完整末态，每 30 秒 fetch 一次，只读取独立的小文件：

`topics/visible-flexible-closed-surface/ci-requests/6a65-gap105-whole-branch-cold-followup-20261126.json`。

这个 followup 路径不触发新 workflow。等待期间仍每 45 分钟执行真实 pull、双 README 检查与 HANDOFF 提交号登记；每次准备执行续算包时，也先实际 pull 和规则检查。

包的 schema 固定为 `6a65-gap105-area-same-job-followup-v1`。它必须逐项等于当前 runner 的 `run_id`、`run_attempt`、`source_epoch`、`requestSHA256`、`parentStateSHA256`、`preparedSHA256`。run 和 attempt 使用实际回执中的字符串；父状态和 prepared 使用当前实际文件 SHA，不接受历史状态数字或其他 run 的文件。

只允许两种操作：

- `operation="additional_area_attempts"`，并给出整数 `additional_area_attempts`，范围 1–100；它只运行相同已冻结完整 14 行模型的额外真实单步进程。
- `operation="release"`；它发布明确释放回执后退出，不把 runner 释放写成课题完成。

同一文件 SHA 只消费一次。错误或不匹配的小包只登记忽略原因，不运行数值步骤。area 一旦真实拒绝，同配置额外尝试不再被接受，只允许 release；新的实质数学模型需要另立明确身份后继续，不能借此薄接口偷换目标或自动重复已拒绝输入。未收到 release 时，实际文件保持到当前 job 的平台时限，主会话应利用这个同 job 接口继续研究。

## 文件和数学结果边界

原始 coefficients、NPZ、六 jets cache、prepared 数组和完整 checkpoint 仅留在本 runner 的临时目录，不上传 artifact、Release 或 Git。公共报告只含小标量、源码/输入/输出 SHA、实际 run 与状态链。源文件、配方和工作流均为小文本，可以从公开提交重新生成本次输入。

面积列中的 `minImmersion` 始终是
$$
\eta=\frac{|X_s\times X_u|^2}{a^2},
$$
而 $\sigma=\sqrt\eta$ 才是目标面积比。离散正值和有限离散 barrier 成本不证明连续浸入性；R240 的连续积分结论需要自己的连续积分前提。完整闭面、全时 reach、同 g 的连续非平凡等距族及本题强目标仍未完成。
