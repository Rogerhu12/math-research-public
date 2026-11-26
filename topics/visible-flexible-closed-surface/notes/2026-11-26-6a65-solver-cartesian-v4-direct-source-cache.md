# 同一实际源的直接样本缓存：v4 完整 Cartesian 接续

日期：2026-11-26；会话：Astra-visible-flex-6a65。此记录只支付直接源缓存、身份边界和可执行接口；没有新增完整 Cartesian 接受步，没有连续证书，也没有本题完成声明。

## 为什么复用这些数据

独立冷实验 run 45812620369 的实际 v2 子进程用时 1073.140468766 秒，其中完整 LSMR 80 次迭代的实际时长为 29.245083139999906 秒。旧实验已分别记录其实际接受与很差的 metric/曲率；不得把该过程的成功退出理解成达标。

同一独立 Cartesian 模型写成 $X=X_0+W_z$，固定的 $X_0$、完整物理 $g$、材料角原语以及真实端口均来自同一个实际 Cauchy checkpoint。只读缓存保存 $X_0$ 的六个真实 jets 和 $a,a_s,a_{ss}$。每次自己的非零 $z$ 接续仍完整重算 13 行残差、J/JT、LSMR、所有真实 line search 和密观察；复用缓存不复用上一态的目标值、导数或接受决定。

本 revision 不改变任何残差、方程、曲率/几何 guide、LSMR 参数、径角采样、全部 7760 列或 Armijo 条件。原 v2/source003、v3、point、stream、oracle adapter 均保持原文件身份；新 revision 使用新文件名。第一态照旧直接生成两个完整 cache，后继自己的非零态严格读取实际 checkpoint。

## 冻结源与接口

| 文件 | 字节数 | SHA-256 |
| --- | ---: | --- |
| scripts/6a65-cartesian-fixed-source-cache-reuse.py | 15587 | 13a900d751115332608e1cb53de5621952b2a84a9e8f09565068d0884a9b9c99 |
| scripts/6a65-cartesian-independent-experiment-v4.py | 34740 | 33a392a0738e74608b18de2bb05be14e9c01e1c2db7e3ecdfc926cb7b585a21d |
| scripts/6a65-actions-cartesian-same-model-v4-20261126.py | 30948 | 949d4a90d76300a14732eee5210a14a5e9b231695acb9149192e745d9198f456 |
| scripts/6a65-cartesian-cache-reuse-actual-fixture.py | 9519 | 5ac0eb05dfc0ae2cdb383f9a586b91aa3f8704b8752d8ead2991f0a02a5812c5 |

原三个算子源仍为 stream b8cfd595b535cc33d47e2c0bc3e2b8d6a79c8163a235415115ca42c53416e4a9、point cf475476fb2b5e3a91d4438dd9dd67e54652bfd9594cc577b038ee2fd5e6f08f、oracle adapter c57d4d21f85f949f869a2c7d1d7c4e50ede7be948ce541f1b676d589ae4045a5。recipe 仍为 0794c4d61e4307cde3de4a84154d4e27311f96a4f7f7aa48d74d6fa0724841a7。

entry 在原 v3 参数上增加必需的 `--source-cache-directory`。controller 原参数全保留，可选 `--source-cache-directory` 默认为本次 fresh `--out-dir/shared-fixed-source-cache`，必须在本次输出目录内。它不是跨 job raw 恢复器。controller 每次实际 numerical child 都剥离 Git 凭据，真实报告、每条 scalar commit/push、45 分钟规则检查、拒步保留 actual state 与同 job 后继等待沿用已核发布器；新增缓存回执必须逐态通过其检查并进入 scalar 报告。

缓存身份包括实际 run ID、run attempt、job、source epoch、actual source/candidate/原 observer/全参数向量与全 g 的身份、live metadata、所有源 SHA、完整 recipe/grid/basis/pointConfig/operator/entry 身份、物理与材料网格的二进制 SHA、数组字节 SHA、dtype 与 shape。source、g、grid 或任何这些字节不同均拒绝。数组以只读 mmap 打开；没有 Fourier/Hermite 投影和插值。

首个生产 oracle 必须自然退出且 OS exit 0，才写完整自然退出 seal。后继进程重新启动真实 oracle 核 live metadata/hash，但不再次采样已有不可变数组；只有匹配的 seal 可支付复用。部分失败输出、缺失 seal、非本 job 身份、不同数值模型、被改写的 receipt/array/seal 均拒绝。所有原始数组、cache、state 与 observer 只在同一 runner 的 Git 外目录。小 fixture 的显式 local 身份开关不在生产 entry 中使用。

## 实际小检查

输入是几何 agent 独立以公开 recipe.config、无 z 配置，经原 factory.value 真正得到的本地 INITIAL，SHA-256：

`1e3ae25e984fd4ac166022644cb5cbc248976e749ca391859d08ac1d45a7aced`。

这不是 CI checkpoint，不是 interface probe，也不是已结束 job 的 raw。它先前完整 value 的真实退出记录独立存在；本检查没有重复完整 value 或 normal。candidate 字节 SHA 为 `9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d`。

确切命令（原始结果保存在 Git 外）：

```sh
python /tmp/visible-flex-6a65e705/solver-work/recovered-sources/6a65-cartesian-cache-reuse-actual-fixture.py \
  --sources /tmp/visible-flex-6a65e705/solver-work/recovered-sources \
  --scripts /tmp/visible-flex-6a65e705/math-research-public/topics/visible-flexible-closed-surface/scripts \
  --candidate /tmp/visible-flex-6a65e705/math-research-public/topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json \
  --source /tmp/visible-flex-6a65e705/geometry-work/gap105-window-ownzero01-initial.json \
  --output /tmp/visible-flex-6a65e705/solver-work/cartesian-cache-reuse-actual-fixture02
```

实际外部 OS exit 0；fixture 内部秒数 1.2193978099967353。报告 `cartesian-cache-reuse-actual-fixture02/report.json` SHA-256 为 `897342e9619007d93aa54e8f37d66380a1030184f87156487aab830f3159dcea`。

实际第一 oracle 自然退出 0，0.6374515109928325 秒、12 次协议请求；生成 training shape `[4,6,4,3]` 与 observing shape `[3,6,8,3]`。第二 oracle 自然退出 0，0.3549321830068948 秒，恰好 1 次 metadata 请求；其 cache 方法被 fixture 设为一旦调用即抛错，所以这次真实返回支付了没有重复点采样的断言。两组 jets 和 radius 全部逐值相同，mmap 写入实际被拒绝；两次输入文件 SHA 不变。

13 个真实拒绝项：local fixture 冒 production；改 run ID、source epoch、物理 g 身份、完整数值身份、s 网格、u 网格、array 字节、原始 receipt 字节；缺自然退出 seal；改 seal 字节；改实际 array shape；改实际 array dtype。测试中的变坏副本只在 scratch，不修改真实源输入。

首次 fixture01 曾因测试脚本取不存在的 metadata 键 `metricDefinition` 在缓存前真实退出 1；改为 oracle 已定义的 `radialMetricDefinition` 后才运行上述 fixture02。它没有形成数学结果。四个新源的 compile 检查以及 v4 `--help` 的实际导入均 exit 0。

## 已支付与尚未支付的范围

此检查支付真实原源协议、直接样本不变性、自然退出封存、只读复用及具体身份拒绝。它不支付新的 7760 列接受，不支付大网格整步速度，也不支付任何连续 metric/曲率/reach/held 门槛。新 batch 必须在自己的 runner 重新生成实际原源、真实原 observer 和已见首步，再从它自己真正保留的非零态继续；已见首接受重生只作为输入恢复计数。

原 training 与密观察的径向点集合并非嵌套，任何实际最坏值仍须同时保留两份结果。v4 没有通过更换观察网格降低峰值，也不把采样曲率或 `max |a''/a|` 称作连续界。


## 根会话的实际多步接线

新增入口 scripts/6a65-actions-cartesian-batch-bootstrap.py，SHA256为34c36f8084db8373d24c130da32e90d0dd2781c71c71fa9d86714d0b65f2325c。已实际py_compile exit0，并经根与solver agent完整读过；这只验证接线，不计实际数学尝试。

新workflow 6a65-cartesian-cached-continuation.yml 明确生成本job自己的完整Cauchy INITIAL及matching observer；数值前首次真实pull核双README，baseline长于45分钟时也实际pull并写H。两个workflow凭据均从数值children中剥除。原无z配方、完整g和Cartesian配方不改，原件只在RUNNER_TEMP；从冻结目录启动v4同模型controller，初始请求20个完整尝试。

previously observed accepted prefix计数为1仅作输入重生标识，不直接添加接受。真正后继继承自己的非零向量、匹配observer和只读source cache。每个真实尝试普通commit/push；真实拒步仍保存有效当前态，不捏造接受。请求步数到达后仍保留同job源，等待根会话发布严格匹配后继；这不是等待用户确认或本题完成。350分钟为job外部执行上限，不是研究停止标准。

请求/工作流的发布只代表执行已授权并触发；实际run ID、退出与每个全场结果以随后真实回执为准。
