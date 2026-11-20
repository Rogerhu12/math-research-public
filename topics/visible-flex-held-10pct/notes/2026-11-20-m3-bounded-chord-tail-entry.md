# m3：原真实尾的可选有限次 chord 入口

维护会话：Astra-held10-1b6d88ec-20261120。

本条只登记独立算法入口和已执行的静态安装。原 M24 实际 nonlinear
DN baseline（session 42787）继续使用原源、原配置、原 Newton 路径；
本条没有启动第二次射击，没有改动它的源或原验收门。

## 1. 成本依据与范围

原 baseline 的第 1、3、5、7 次 native 完整 Jacobian 调用分别实际耗时
579.7985、545.4344、511.1218、682.1270 秒；相邻 state-only 调用
第 2、4、6、8 次分别为 155.459、148.6203、147.3783、147.4566 秒。
这些是 `newg-native-m24/runs/actual-lambda0p002/events.jsonl` 的终态
计时。第 8 次在 2026-11-20 13:13:25 UTC 完成，第 9 次完整 Jacobian
随后开始；当时首个 .25 H warm response 尚未返回，不能由耗时或调用数
断言失败、收敛或最终加速比。

新增 `scripts/resume_m3/install_bounded_chord_tail.py` 将完整旧 solve
保留为默认分支，并在全新源副本加入显式可选的有限次 chord 分支。
它是算法改变，不是原路径身份相同的替代。物理方程、每个 trial 的
state flow、域门、射击残差定义与最后 DN 导数合同保持原定义。

## 2. 可选分支的具体规则

仅当源配置中显式设置 `chordMaxCorrections` 为 2 或 3 时使用新分支。
数字包括获得该完整 Jacobian 后的第一步：3 表示一次 fresh 步加至多
两次复用步。未提供该键时逐字保留的原 solve 分支继续使用。

每步仍用原 sparse multiple-shooting 修正系统。复用只替换该系统中
阶段 flow Jacobian；当前 states、非线性 residual、deep-end residual、
入口残差、mean 和域检查来自实际当前 state flow，不能挪用旧 residual。
每次 trial 仍走原 10 级线搜 `alpha=2**(-k)`，只接受原完整非线性残差
严格下降的 trial，原异常域拒绝逻辑保留。一次已接受 trial 的真实
state-only 结果可以直接作为下一 chord 步的当前 residual。

任何 state-only 残差到达原 shooting tolerance，都必须在返回前重算
当前 states 的完整原 Jacobian，并重新按原残差判断 converged。
达到原 iteration ceiling 后同样重算末态完整 Jacobian；返回的
`linearizedFlowJacobians` 因而不是缓存的旧态导数。若复用步的全部
10 个 trial 均不下降，则该步消耗原预算并舍弃缓存，下次迭代 fresh；
fresh 步线搜失败仍按原路径抛错。原 maxIterations=36 与前缀 outer=8
均未增加，原 shooting gate=2e-9 也未更改。

新 response 明示 `shootingAlgorithm=bounded-chord-v1`、
`chordMaxCorrections`、`finalStageJacobian=fresh-original`，history 明示
各步 fresh/chord 类型。有限 M、有限深尾与无限尾的原 scope 区分保留。

## 3. 已实际执行的独立安装

下列 WORK、TOPIC 是本会话的实际目录；安装器要求全新 destination，
不允许覆盖原源或已有目录。

~~~bash
WORK=/workspace/scratch/1b6d88ecddf3/m3-work
TOPIC=/workspace/scratch/1b6d88ecddf3/math-research-public/topics/visible-flex-held-10pct
python "$TOPIC/scripts/resume_m3/install_bounded_chord_tail.py" \
  --copy-from "$WORK/newg-native/shared-source" \
  --source-topic "$WORK/newg-bounded-chord-source" \
  --manifest "$WORK/newg-bounded-chord-install.json"
env -u LD_PRELOAD -u LD_LIBRARY_PATH python \
  "$TOPIC/scripts/resume_n4_tail/native_extended/prepare_recovered_native.py" \
  --source-topic "$WORK/newg-bounded-chord-source" \
  --dest "$WORK/newg-bounded-chord-native" \
  --native-cli /workspace/scratch/1b6d88ecddf3/n4-work/frozen_flow_batch \
  --modes 24 --spacing 3 --quadrature 512 --steps 16 --workers 2
~~~

两条均实际 exit 0；修改后的 JS 已实际 `node --check` 通过。
原 split/native factory 通过 `...options` 把显式配置传到 shooting
factory；没有新增绕过 worker 或原 response 的路径。

| 对象 | SHA256 |
|---|---|
| 新 installer | 8f9bc468e89bc0523d14e45601e131c723931955d4642781fdaeca4b267fd3a9 |
| 原 shared/periodic stage source | 84f944c560dcb65dc3f6fda2e97f3ebc549f1dbcdcc1fe2525324561d754c3be |
| 独立 chord stage source | 0b61c0adb03643fcc62fb5b79111197e34a4a533c741e043eca42be4b2c92c32 |
| 独立 native manifest | 00e9fff1b36e5fa56396eb246012aa87e9fc3e7b1afdf24e4f02265568e17d26 |
| 复用的原 production CLI | 1b47ed47e70e35a08f11173b1f17a5d1c2ee046f59f54f235ee5fa56de07af94 |

native manifest 位于
`WORK/newg-bounded-chord-native/native-manifest.json`，其独立运行 source-topic 就是
`WORK/newg-bounded-chord-native` 本身。此步骤只是安装，没有 native 数学 batch。

## 4. 已授权、尚未执行的 checkpoint 接续计划

先等待原 baseline 的首个 `.25 H` warm 完整返回。原 client 会先写
`WORK/newg-wide-lambda0p002-m24-actual/tail_0001.json.gz`，其中保留完整
1153×48 shooting states、rawNode/rawStates、cutHeight、完整物理参数、
request、response 和源 SHA。只有 response 明确 converged、无 failed、
residual≤原 2e-9，且全部 states/参数实际可读，才执行接续。

此 warm 请求 jacobian=False，末态 full-J 虽已供原收敛判断实际计算，
worker 不把阶段 J 放进 response，heightJetJacobian 也为 null。
新算法不冒称恢复了这个未序列化的导数；新目标第一步照常 fresh-J。
同 M/depth/parts 的 original remesh 会逐节点复制全部已有 states，
不重积分已完成的 warm。

检查点通过后，记录原 baseline 已完成的 `.25 H`、源与文件 hash，
然后明确中断 session 42787。若它已自动进入下一 `.5 H` 调用，则仅
登记该未完成调用因算法切换被取消，不称为数学失败；必须观察进程
终态后才启动新独立 driver，避免并行重算同一步。

新 scratch config 复制原物理 tail-settings，仅增加
`chordMaxCorrections: 3`、`initialCheckpoint` 指向真实 `.25 H` gzip，
及仅供进度记录的独立 `traceFile`。使用独立 native manifest/run 目录，
其余原物理参数、M24、depth8、parts16、quadrature512、shoot36 和
prefix outer8 不变；原 linear raw、profile、完整核心、H 和所有门不变。
新 driver 的 `--tail-warmup` 为 `.5 .75 .9`，明确不重复已完成 `.25`。
不能直接跳到 full H：从 `.25` 跳 full H 的 ratio=4 不满足原 predictor
要求的严格 ratio<4。对高模入口差仍由原完整 linear-response 初猜补齐，
而真实射击残差决定接受。

实际执行的 argv 与只含非秘密必要项的环境将记录于
`WORK/newg-wide-lambda0p002-m24-actual-chord3-command.json`；输入 config
为 `WORK/newg-wide-m24-port/tail-settings-chord3.json`，新输出目录为
`WORK/newg-wide-lambda0p002-m24-actual-chord3`。截至本条写完，尚未中断
原 baseline，也没有启动 chord 数学调用。

后续应报告原残差/射击 gate、实际域与线搜拒绝、full-J/state-only
次数及时间，并确认末态 fresh-J 已完成。不能只因少调用 Jacobian 就
称成功或加速。本条没有新增合格尾或固定 g 收敛结论；实际完整 trueDN
返回后，仍先冻结最终物理 g/q/c/均值定义再做场细化。
