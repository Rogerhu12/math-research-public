# 第 19 个完整初场的同源 R722 normal、连续几何与闭面参数

2026-11-27 UTC。本包提供三份完整后续参数：normal/physical-sixjet、continuous Gram/K/support、closed-phase/grip/R718。它们复用已经公开的 producer-bound R722 全部运行体，不产生新的科学源码、模型别名或削减后的试验。

当前科学输出约定为 `{work}/fixed-fejer-meridian-batched-bhalf-first/report.json`。新的 seed 仅取端层总长 $b/S=1/2$，profile $\delta=1/32$；固定度量、全部自由变量及科学预算保持原来完整定义。该选择的实际六 g、完整同点身份、单位混合与一般非单位分母、中央段代价和未知条件，均见 [独立选择说明](2026-11-27-actual18-six-constraints-and-bhalf-seed-choice.md)。本文不重复 R721 或 R722 的定理证明。

## 1. 完整参数来源

三份直接参数父文件均在确切历史提交
`42e52a68c95f18ccf945ddf598e313116b835ab1`：

| 完整参数父件 | 字节 | SHA-256 |
|---|---:|---|
| fixed-fejer-meridian-producer-bound-R722-complete-normal32-full-circle-sixjet-fees-ready.json | 37257 | b1058785f0f6ccd0d6a1d2ddd1842fd701e070751593ab8709aff5b2b0ad9a2d |
| fixed-fejer-meridian-producer-bound-R722-complete-continuous-gram-curvature-support-ready.json | 37899 | 0324c6a5ff20b8ea38c51fd9fcde8ce2d813773589787e0ba8de965deaf436ec |
| fixed-fejer-meridian-producer-bound-R722-closed-phase-grip-r718-ready.json | 58295 | 19e251c617e4e0ae70f7684b78648a2c6401140d956bf8191b12caa09c2d5705 |

全部原步骤对象、原 flags 和数值 argv、完整 source 表、原 summary 名称/表达式、输出列表以及所有更早的父参数记录都保留。新参数只更新当前 runner 输入/输出命名空间、步骤 id、明确的新 seed 计划及其归属说明。原 18 的启动、输入返回、三次初始化失败、partial observation、旧 seed 和未知科学责任均完整保存为历史，不复制成第 19 次实际输入。

新的科学/pure 参数由 root 独立完整准备：

| 对象 | 字节 | SHA-256 |
|---|---:|---|
| fixed-fejer-meridian-bhalf-science-complete-ready.json | 90652 | 242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67 |
| fixed-fejer-meridian-bhalf-pure-complete-ready.json | 80254 | 8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7 |
| fixed-fejer-meridian-bhalf-complete-display-correspondence.json | 25057 | cc564e5c273367242aae226913a0dd82ae5b88b3e166fbcbb8da68d6c04edb2d |

总表完整链接这三件。三份 post ready 是在其完整记录到达前准备的整体文本，其中未知 current science 文件身份保持 null，并由最终总表给出精确链接；没有为了回填这项说明再次改写已锁参数。实际新 run、输入、field/normal/seed model、point、完整 report、immutable packet 和费用数值继续未知，不能从固定 recipe 或源码存在推出。

## 2. 同源运行体

以下完整运行体逐字共享，没有为 b=1/2 复制一份新源码或放松某个固定输入验证：

| 角色 | SHA-256 |
|---|---|
| science driver | 10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f |
| pure reader | 8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49 |
| actual packet/field input | d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7 |
| R722 posterior kernel | 4fc252f8977f4f4246d2cc13583efc0bccd4b28742df3a797d1c266cdd1eac7d |
| accurate radial/control boxes | 7c66ed0f31323451156c1cd76ae7401eb497f37377393bb66503523ad2aaac54 |
| normal32/physical-sixjet fees | c6f6c9726b23ceb25533d5a6a6ac41fd31e8a3c14226895d5fc32e74787c0108 |
| complete physical leaf reader | 7892eb497fe9d8ce4ca50a066d7c8189531e05b89b5c06ed1155c2b6a1d45c1f |
| continuous Gram/K/support | 6c57f78a9c8b80805e8e551a8fba50a089687cea164bd192c8bead845dda29b4 |
| complete support/beta bridge | c6b07b17ba9c25985faae62cd5db0991cd27bc4927d22fdd9e56a6c5ac7ae4e1 |
| closed-phase/grip/R718 | 002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f |

完整 137 个当前科学来源及其中 120 个原父来源身份继续逐项绑定；同原 whole reader 重读完整6个固定输入文件、全部实际 seed 定义、当前完整自由点、所有 required/cached-angle packet 和各自来源。目录中中途产生的副件、mutable progress、旧 accepted 观察或旧准备输入都不代替本次完整自然返回的 field。

准确径向源的 `AccurateFieldGeometry` 直接读取实际
`exact_relative_support_intervals`、
`exact_relative_central_intervals`、
`exact_relative_boundary_each_end_length`、
`exact_relative_boundary_total_length` 与
`exact_profile_delta`；
它完整检查两个 supports、四端层及准确中央分区，然后由当前 S 和全部中央区间生成 Lc。代码没有把 b 固定为 1/4。

本轮预定的准确相对分区为：每端 $1/8$、中央总 $3/8$、每中央 $3/16$，中央区间为 $[5/32,11/32]$ 与 $[21/32,27/32]$。这些是公式的有理参数，不是未来 working carrier words。实际 `central_length_carrier_hex`、所有 mean/angle jets、候选幅度和其费用仍须本次完整重读。

## 3. 三个完整步骤与全部预算

| 步骤 | 完整 argv 词数 | 原 scalar selector 数 | 预算和范围 |
|---|---:|---:|---|
| normal32/full-circle/sixjet | 38 | 36 | 900 s，1000000 leaf evaluations，192 bits，128 panels，1024 全圆闭胞，32 normal stages |
| continuous Gram/K/support | 8 | 48 | 900 s，完整原 root/physical streams、全部原径向胞与 cuts |
| closed-phase/grip/R718 | 8 | 66 | 原 support-chunk-rows=4096，完整全部支撑行与八 beta 加径向证据角色 |

normal 的其余原字预算全部保留：rho-leaf-budget=8192、inverse-steps=64、inverse-width=1/1000000000000000000000000、radial-depth=0、mean-maximum-splits=8192、mean-width-goal=1/1000000000、first-exp-degree=24、maximum-exp-degree=128，三个 root-radius 依次为 1/100000000、1/1000000、1/10000。本文没有用这些精度词称实际误差已付。

两个数值费用步骤都保所有 922 个参考/current 径向胞和全部实际支持/profile/control cuts、完整尾、每个原 literal angle、1024 全圆闭胞、32阶段、完整6个物理 jets 与所有 raw-lift 交叉项。R722 后验根存在域及真实 R709 粗条件结果分开：新分支不把旧 bool 伪改为 true，也不从一个全角小胞推断整个圆或闭面通过。

相对三份直接完整父 ready，三个步骤的 argv 只有索引3和5分别更换 input report 与 outdir，其余每个字符串、顺序、数值和数量均相同；运行脚本路径不变。输出/summary 的文件路径键随当前目录变化，而其全部 selector 名称和取值表达式逐对象完全相同。

## 4. 新目录与完整主副件消费

科学 report 为 `{work}/fixed-fejer-meridian-batched-bhalf-first/report.json`。

- normal report：
  `{work}/fixed-fejer-meridian-batched-bhalf-first-R722-normal-root-and-sixjet-fees-v1/report.json`。
- geometry report：
  `{work}/fixed-fejer-meridian-batched-bhalf-first-R722-continuous-gram-curvature-support-v1/report.json`。
- closed report：
  `{work}/fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-v1/report.json`。
- R716 unmarked tube sidecar：
  同 closed 目录的 `R716-unmarked-outward-tube.json`。

闭面源保持原全部上片、Dz 下反射、两完整 Cartesian marked caps、R248 inverse-Theta 相位、同一 A_beta 支撑与 R650 mixed-pair reach、固定 grip、全像距离、R718 与条件 R719 原合同。原精确积分、曲率和证明不由更换目录支付。

下游必须先读取最终 complete/status/recheck 均满足的 closed 主 report，再以主 report 的确切 file record 找到 sidecar，并重读全部 source/proof/input/output、同 point/model/target/snapshot 和完整流。晚失败写出的副件不能脱离主 report 被接受。未标记平帽外管仍按完整独立的 sigma/K/D/tau0 与严格 mark height < tau0 解释，不借已标记 embedding 循环证明。R716 十二矩与 mesh 各有其完整另一步；本三步不假称已支付这些后继。

## 5. 可逆全文参数再生

[完整参数再生器](../scripts/resume_20261126/reproduce_fixed_fejer_bhalf_R722_post_parameters.mjs)
仅用 Node 标准库进行完整文本、JSON 与文件 hash 操作。它从上述确切历史 Git commit 逐件 `git show` 取完整参数父文件，核 whole bytes/SHA-256/Git blob，施加全部有记录的整段文本变换，核输出完整身份，再逆变换至逐字原父件。

它不会 import 科学源码、创建工作场或运行 F/J/root/积分；它不修改 refs、queue 或原文件。输出目录必须位于源码 checkout 外。这只是可选、完整可复现记录，不是新科学入口条件。

本次实际完成的是 V8 文本正向/反向构造、完整 JSON 参数与 selector 对应关系和 whole byte hashes；没有执行该 Node 再生器，没有 AST/compile、科学 fixture、局部 benchmark 或误差数值运行。正文没有用可逆构造冒充科学求解成功。

三份完整 ready 均小于 100 KB，没有删除原科学参数以满足发布限制。原所有旧历史和失败来源仍在完整父文件及当前继承字段内；没有把参数源版本误标为本次实际数据。

## 6. 当前交付与严格未知

本包只是同一完整源家族的新输入选择后的后续参数就绪。预计字段仍为 null：新完整输入 record、normal/seed identity、完整 field point、same-point packet、费用/几何/闭面结果。原 18 初始六 g 是选择依据，不是新 run 的预测，更不是新准确包围。

root 独占发布与 Actions 队列。本包没有写 refs 或安排执行，也没有增加独立 review、重放、测量或数值门。后续实际预算未完成、准确条件不足和真正代码失败仍按原不同状态如实记录；不把“源和参数齐全”写成研究目标已完成。
