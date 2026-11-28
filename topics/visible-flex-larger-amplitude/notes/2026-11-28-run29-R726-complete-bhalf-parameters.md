# Run29：R726 完整球面端层 bhalf 参数与历史边界

本包为独立run29准备完整参数，namespace `fixed-fejer-r726-bhalf-first`。准备不是实际运行。全部新run/input/model/point/root/report/final/typed/连续证书字段均为null。源码已完整普通刊于 `7acb89983fe616fbba85cef74811625b357942e4`；本任务没有改refs、queue、workflow或在跑作业。

## 1. 精确完整父与当前来源

直接参数父是run26的完整b/S=1/2 R725族，而不是run27的5/8变体：

- science：72,545B / `fb33c7620b05193b54e38a39e97f7efc0fa7149bcbc720d04db1c041aeda0d63` / blob `ebde4051043cfbf7524244dee27f2e85589a562c`。
- pure：58,721B / `29254c1a4a08cbb508266d9ac4c88178a6a7e2b5413428d31461056fe8939ccf` / blob `b3d57832327fccecf3afb4f211006125f331e271`。
- 完整参数binding：47,684B / `5abc72b77a2eb51064239e49a5e90fcc9fd230fc4883a925e19461ae701ef7eb` / blob `b81215714615e663d537f7d0d8c7341aadb453c9`。
- 完整参数总表：19,108B / `a02d1140c3cc83b9e70cde8a264e68707db5ef9da49710826a14a099b6eeb8f5` / blob `c5edf0dd581dcba4af3d6c8b8c97483d1d089de6`。

上述四件固定publication是 `f44e6c09210e7b616775a966ce89b03ccda25b9d`。各自原顶层metadata、完整参数、所有更早来源与失败/取消/未知记录，以原whole文件和准确JSON pointer保持；不是拿本说明摘要替代。

当前R726来源表是55,517B / `6e5480838f54ecb50ce8baa085ebabed37504a3ba759d1ed958ec28c6d9df059` / blob `159d8c56b1b966cf5de5d19bceec68db3630144b`。全部137科学角色、23 current runtime明确保存；19当前pair变，118原pair保。完整科学source总表24,238B / `f3e2e6b31fa9b59af013c4a8fc048e55858eb32279638a4f11368cf2dd2917f9` / blob `5200b7728c55e192821f0f4f29578bc5d22f4524`。二者都已随7acb899完整刊载，不把新R726冒旧R725相同来源。

## 2. 实际科学变化和不变的参数

真正改变的是已刊独立源码中的R726球面边界和其完整均值Jacobian/角2图。seed1764、mean2513、normal335e、driver58630、launcher36a7、reader1aae是该真实家族。R725 epsilon=1/8的三片cutoff、8个内部boundary cut、R724正负半波和辅助12片profile保持。

原157 science词、7 pure词、458/445正式summary和64 live字段全部保留。全部数值词逐字相同，只有当前script、输出namespace及说明scope改变。下表是原完整参数中的部分关键值，执行仍使用整step：

| 原参数/范围 | run29保留值 |
| --- | --- |
| M / J / N | 160 / 923 / 2048 |
| normal stages / angle block / stage block | 32 / 8 / 64 |
| integration order | 8 |
| metric directions / maxiter / damping | 1 / 16 / .01 |
| restoration directions / maxiter / damping | 4 / 64 / .01 |
| line trials / active rows / envelope near-active rows | 15 / 192 / 32 |
| boundary total length / profile delta | 1/2 / 1/32 |
| cutoff epsilon | 1/8，实际完整seed源码固定 |
| mean maxiter / backtracks / tolerance | 128 / 24 / 2e-12 |
| scalar iterations / profile quadrature order | 64 / 16 |

原所有剩余容差、norm、Q输入、两bubble、gamma、全观察域、全source文件、free core/omega/H和输入文件参数都在完整157词中，没有因表格未列就省略。

`--moment-input-binding supported-smooth-triangle-reference`保原实际parser取值；新的Q/model/seed/mean完整来源已经把实际边界定义切到R726。不能凭这个保留的接口标签推断仍在计算旧chord，也不能随意更名破坏原完整CLI。

完整driver保存到EOF原字不变，原stats/geometry顺序、QP/LM、restoration、line search、接受不等式与预算不变。没有加入23 adaptive damping、demanded frame2/rotation或其他新机制。没有新急角数值门。R709欧氏势、R722专用posterior和R727将来的准确存在结论均没有作为已付证明继承。

## 3. 三完整参数文件

| 文件 | Bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| `fixed-fejer-r726-bhalf-complete-parameter-binding.json` | 60792 | `3790d0411f81f755048be6e4ccf047001ca140bcc7700bf24ecd010d49432a9a` | `faebae8df7750c83d572fdbf9328ea9f2c28de1d` |
| `fixed-fejer-r726-bhalf-science-complete-ready.json` | 72547 | `0092bace732ba29a36335f21a59597fe42b109687c35f5ff42d8424f4c252544` | `370dc3064a8b0040a5e352ae5236ee10cd0c9715` |
| `fixed-fejer-r726-bhalf-pure-complete-ready.json` | 58714 | `0998cec08e7196c1e42f3ac32fb711cf5a74ad29a80c245d45d89ec64c9393d4` | `5b547cea6640c87bc7d2b2008bc5f15ca01c3ceb` |

路径均为 `topics/visible-flex-larger-amplitude/computations/`。所有完整旧metadata保留在精确父文件，不做遍历历史SHA的广域替换。新binding的 `/complete_display_correspondence` 完整保存64 live对应及原全部来源；没有必要另复制一份相同大历史对象。

完整新science step仍保 `script/scope/parent_bundle/args/outputs/summary/cleanup_generated_patterns/retain_fixed_reference_cache_for_same_field_diagnostics/progress_summary` 全部键。pure整step原全部键亦保留。当前 `parent_bundle` 仍是本runner应实际重建的 `fixed-fejer-reference/reference.npz`，不是旧26实际文件SHA。

新报告路径为 `{work}/fixed-fejer-r726-bhalf-first/report.json`；pure输出为 `{work}/postprocess/fixed-fejer-r726-bhalf-first-readout.json`。原输入maker和reference的数学合同不因边界机制改变；根节点按原全参数在新runner实际执行两步输入，实际返回身份才可填入本run。

仅用 `{steps:[science]}` 的紧凑JSON是58267B；两步合并的同格式是105082B，尚未包括controller顶层和原两输入。根节点须按真正完整queue计算95,000B限额；若整pure不能同排，应保完整纯读步骤等实际自然科学返回后接，不删除字段、把selector缩为摘要或以progress替complete report。

## 4. 完整peer和新外部证据

原五组CLI peer/run/source词原字未改，所有literal material-address保护、typed first-discovery和未返责任仍在原完整链内。原13个external pair按原顺序保持，追加两份真实R725外部证据后为15个：

- actual26 `46103106086/1`，原declared driver `e1d3b06875496ba2555d20e2e1e96bfa92c420c15dc7276788160b44fca337cd`。完整原note `topics/visible-flex-larger-amplitude/notes/2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md`，59,709B / `9308c531a5208aada7876c8549fb2e2c6f15b28b12ff8be0b3ecabf778c5cc6d` / blob `db2e8bfe7b8071577f0193dd3862e1e53ebd6f72`。
- actual27 `46105138690/1`，声明源仍原R725 e1d3，宽度5/8也保其原义。完整原note `topics/visible-flex-larger-amplitude/notes/2026-11-28-run27-complete-r725-five-eighths-launch-and-continuation.md`，31,932B / `0aba4962e2c3712d407678da4e64a8f7d38053664e7278bd55a4d68750336bb7` / blob `ed1a598ba18f06cd4f663265f52fef60510388ea`。

这两whole原件没有重写。它们保所有原官方run/job、输入记录、时间、实际来源、进度、缺项和错误。新binding仅指出各自完整文件及其JSON块的位置，不把旧observations裁成新的结论。它们不加入PARENT_FAMILIES，不新增CLI peer，不迁移model/point/root/final或把未知typed设空。旧metadata是其当时完整历史，不以本次准备冒它们的最新终态。

run29本身所有actual字段都为null；旧26/27原实际值只属于上述外部证据。相同数学target、相同float点字或相近初始化不构成新场来源或旧证书继承。

## 5. 可完整复现的参数构造

再生器 `topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_R726_run29_parameters.mjs`，23889B / `cdf9b1834ba2194e4df55de739065ccf0d66f542fe57b613613a56cd21ae4d03` / blob `13c2c42dcf9ca190417727f1f3042a77996e55cc`。它保存完整构造函数、八个完整输入文件身份、全部三输出身份，CLI：

```text
--source-root <repository>
--output-directory <independent-output>
```

八输入为完整26 science/pure/binding/delivery、完整R726 source binding/delivery和上述两个whole外部note。读当前文件前先stat；当原metadata已追加变化时，只从准确旧Git blob取回已声明的小文件，并核全bytes/SHA。它不以新main文件覆盖旧证据的完整历史。

构造只对完整step中的当前namespace作递归路径映射，再精确设置新script和scope；所有其他键和值保留。把这三类变更逆回后，整个step必须与原父对象逐值相等。全部157/7、458/445、64计数与完整原五CLI核对均在该完整JSON构造中实现。本次已做的是V8文本/JSON构造与正逆相等，不是另运行Python、AST、fixture、科学或性能测试，也不是新执行前门。

所有输出文件均<100,000B。原完整参数、scope、budget、source、失败/unknown历史没有因容量而裁剪。原science/pure和所有后续准确费用仍须从runner真实全field/immutable point/final生成；这个参数包不能代付连续证明。
