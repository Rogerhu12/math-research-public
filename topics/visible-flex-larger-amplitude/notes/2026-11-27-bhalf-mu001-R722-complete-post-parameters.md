# 第20次独立初场：bhalf、恢复阻尼 `.001` 的完整 R722 后处理参数

## 1. 本次交付的范围

本包为第20次完整独立科学运行准备三个后续步骤：准确法向根与物理六jet费用、连续 Gram／曲率／支持费用，以及完整闭面、全物理相位、握持、R718 与 R716 外管证据装配。三个运行源均沿用已经公开的 producer_R722 完整版本。本包只创建参数文件和可逆参数构造器，不修改任何科学运行源，不执行科学计算，也不创建、修改或启动队列。

第20次科学入口的唯一数值参数变化由 root 的两份完整 science／pure 参数文件定义：`--restoration-damping` 的值在零基 argv 索引37由父运行19的字面 `.01` 改为 `.001`。`--damping` 仍是字面 `.01`；两者是不同参数，不能把本次变化写成普通度量阻尼变化。种子仍为 `--seed-boundary-total-length 1/2` 和 `--seed-profile-delta 1/32`。

本包中的三个费用步骤不接收、替换或自行解释恢复阻尼；它们读取第20次真正返回的完整场、模型、输入和不可变法向快照，并按原有完整校验器验证。因此三份后处理 argv 的数值词完全不变。每份 argv 只改变索引3与5的当前输入、输出路径。

第19次与更早运行的完整参数、旧输入和实际失败／未知记录都保留为参数来源；它们不是第20次的实际输入或场。计划就绪也不是准入、收敛、准确误差已付或几何证书。

## 2. 完整科学参数来源及冻结目标

当前完整科学参数文件：

| 文件 | 字节 | SHA-256 | Git blob |
|---|---:|---|---|
| science | 97019 | `89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca` | `598b4cdf62021a66b54c22b71171722027f1c0b5` |
| pure | 86221 | `f627447f7887bdc9d7f257b4d0772173556683501cd5fa9f1e39890ec7ac7f64` | `53655fce8344040770e02295898a1c4ae9a06ebf` |

完整路径分别是 `topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json` 与 `topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-pure-complete-ready.json`。这两个完整文件保有157／7个 argv 词、科学458个正式选择器、原48个实时字段，以及完整137个当前科学来源角色和所有原120对来源身份。本包没有复制省略版科学命令来替代它们。

固定数学配方身份仍为 `957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9`。完整 RN-even dyadic Fejér 材料图、R690 标量定义、冻结参考 M160／J923／N2048、全部当前变量、32法向阶段以及精确物理相位定义均不变。恢复阻尼是外层恢复搜索参数，不进入该固定度量或准确种子配方。全部定义相同的依据是原实际运行源和上述完整参数，不是跨运行报告 SHA 的猜测。

同一预定配方不允许继承实际文件字节、当前自由点、根或费用。新 runner 的完整输入文件、参考报告、场模型和快照仍须实际产生并逐份重读。本包中未来 actual run、完整 report、point、normal model、seed model、packet 和各项费用身份全部为 null。若 root 随后启动20，实际启动记录应另存；不反写已锁计划中的未知结果。

本次参数选择本身不保证有限64步内层解、更好的线搜索接受率、真实非线性约束下降或全域几何改善。科学参数文件已经精确限制了较小恢复参数的理论比较范围：同一完整可行线性约束集下的精确全局 QP 最优解。这里不把这一条件结论升级为当前求解器的实际结果。

## 3. 同一个种子的完整准确定义

预定支持区间仍为
$[S/32,15S/32]$ 与 $[17S/32,31S/32]$。总支持长为 $7S/8$，四个端层总长为 $b=S/2$，每端层长 $S/8$。中央总长为 $3S/8$，两段各为 $3S/16$，中央区间是
$[5S/32,11S/32]$ 与 $[21S/32,27S/32]$。
每段 profile ramp 的准确长度由原定义给出为 $3S/512$，profile 参数为 $1/32$。

这些是完整源中的准确比例定义，不是尚未返回的浮点 carrier。当前代码仍从完整真实模型读取种子定义。原 R709 粗充分条件保留其实际 true／false 值；本族的根存在与导数归属由独立 R722 后验合同实际支付。未付时照原返回 unavailable／partial，不能将 R722 的成功填成旧 R709 条件为 true。R710 的两阶角 jet、R711 的十二片 profile、全部正性和区间舍入责任也完全不变。这里不重复 R721、R722 的证明。

## 4. 三个完整步骤与当前目录

唯一当前科学目录是
`{work}/fixed-fejer-meridian-batched-bhalf-mu001-first`，
其完整输入场为
`{work}/fixed-fejer-meridian-batched-bhalf-mu001-first/report.json`。

| 步骤 | argv 词 | 原 scalar 选择器 | 当前报告 |
|---|---:|---:|---|
| normal | 38 | 36 | `{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-normal-root-and-sixjet-fees-v1/report.json` |
| geometry | 8 | 48 | `{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-continuous-gram-curvature-support-v1/report.json` |
| closed | 8 | 66 | `{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-closed-phase-grip-v1/report.json` |

三个完整 ready 中保留每个 argv 词、全部 outputs，以及每一个 summary 标签与表达式。原 `parent_bundle=fixed-fejer-reference/reference.npz` 和三个 script 路径不变。summary 只改变当前报告对象的外层路径键，内部36／48／66个标签—表达式映射逐字保留，没有新建简略字段清单替代它们。

normal 的原数值预算全部保留：

- `--seconds 900`、`--maximum-leaf-evaluations 1000000`、`--precision-bits 192`。
- `--panels 128`、`--rho-leaf-budget 8192`、`--inverse-steps 64`。
- `--inverse-width 1/1000000000000000000000000`。
- `--full-angle-cells 1024`、`--radial-depth 0`。
- `--mean-maximum-splits 8192`、`--mean-width-goal 1/1000000000`。
- `--first-exp-degree 24`、`--maximum-exp-degree 128`。
- 三个原 `--root-radius` 依次为 `1/100000000`、`1/1000000`、`1/10000`。

geometry 仍有完整 `--seconds 900`；closed 仍有完整 `--support-chunk-rows 4096`。这些只是重述已保全的实际 argv，未新增试验门、AST、fixture、性能测试或科学前置步骤。

normal 保留全部32阶段、所有原 literal 角与1024个全圆闭胞、全部922个径向胞和完整 support／profile／control 精确 cuts、全部标量尾项、全部控制与六个物理 jet、全部上游与 raw lift 项。geometry 原 Gram 算子范数、主曲率、支持、同叶三维位置范数和完整最终字节复读均保留。任何有限预算返回仍有原来的未付边界。

## 5. 闭面、全相位、握持与下游 sidecar

closed 运行体仍是完整 `002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f`。它保留上片、下反射、两 Cartesian 平帽与完整 p4 标记的接合、相位、取向和来源责任；保留所有八个原 beta 证据角色及独立径向／下反射角色。共同支持、闭面／全相位和混合点对 reach 的支付条件没有缩减。

完整目标像距离与 R718 流下界仍在同一完整准确场上按原公式分别计算；强目标 $\delta_{hold}\ge0.2D$ 的未付状态不能被标准 $0.05D$ 掩盖。R719 的条件使用也保持原义。这里不替换为正在独立开发的 R723 consumer，不把新的理论结论偷接进旧运行源。

R716 外管副件路径仍为：
`{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-closed-phase-grip-v1/R716-unmarked-outward-tube.json`。

下游必须先接受最终 complete 主报告，再按其实际 file record 读取 sidecar，复核全部输入／输出来源及同 point／model／target／snapshot 身份；不能孤立消费途中可能留下的副件。原晚失败清空顶层已付结果的行为完全保留。这里没有支付十二矩、$\delta_E$ 或 working-word／参数误差。

## 6. 三个完整父对象的保全

三份直接父文件是已经公开在提交
`6167a8bd8fd01c984095e705874e7516ea3fcb6c`
的完整 run19 参数。其确切身份如下：

| 父 ready | 字节 | SHA-256 | Git blob |
|---|---:|---|---|
| normal | 49322 | `14e6ac6d8e95721a8fc1ddf983c7d3c67258f9daa41d01fefab955491d74d39a` | `bae2aeb057b0d1c58d6520038a3467bb4b2548b9` |
| geometry | 48299 | `d43d408cb4612a8998256e4e0d85085bb4041f0abf7e47dc89e5dd6b3e0874cc` | `bab97b529ea6e68d19fbd92335bd7064ef283202` |
| closed | 74772 | `6ea0e0482697134be32ef6ff080aea7007297116c2ad679a874087e61e3c972f` | `f5392f425a12a8b219f517f235c368e29e66f7ff` |

原文件的全部文字都作为可逆变换的父字节读取；原正文并非一律等于重新 pretty-print 的 JSON。因此构造器采用顶层 JSON token span 的精确文本替换，而非声称普通 stringify 能恢复父的特殊空白。

每份原 `run19_complete_parameter_contract`、`run19_complete_parameter_parent` 和 `run19_current_post_plan` 原值不变，分别移到 `parameter_parent_run19_...` 键。closed 另外将其旧当前 correspondence、两费用 ready records、旧 science 文件状态、旧 source scope 和旧再生器路径完整移为历史字段，再增加当前20对应项。其余每一个原字段都保留，只有当前 schema、当前报告路径和单个完整 step 显式更新。全部历史 run18 初始化失败、旧输入与 unknown peer 义务都没有删除或改成当前输入。

新 run20 合同逐项说明精确科学参数变化，记录两份真正完整科学参数文件，保存当前全部后处理 args，以及两处路径差异。closed 的当前 normal／geometry ready records 是本包实际锁定的新 whole file identities。

## 7. 全文可逆再生及实施界限

完整构造器是：

`topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bhalf_mu001_R722_post_parameters.mjs`

其身份为 20018 字节，
SHA-256 `2ee1f0fa7896b26e00ecebbed962c4d6be905cecb3eae5d3aae0cf4a8f8c185d`，
Git blob `fed59e865192c18048e039afc1fa8e746eb63dac`。

它只使用 Node 的标准文件、路径、hash 和可选只读 `git show` 接口，完整读取三父 ready 和两份当前 science／pure 参数，核对全文件身份，执行同一明确文本变换，逐一反向恢复父的每个原字节，然后写出三份完整 ready。它不 import 任何科学模块，不调用 F／J／root／积分，不改变 Git ref，不启动队列。历史父可用
`--restore-parent`
从上述固定已刊提交完整读取；不假设当前同名路径永远保持旧字。

可选用法：

```sh
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bhalf_mu001_R722_post_parameters.mjs --repo /path/to/repository --out /path/to/parameter-output --restore-parent
```

该构造器是参数恢复工具，绝不加入科学或控制器准入步骤。构造时已经以 V8 对实际完整父文本执行正向变换、逐字反向恢复，核对全部 argv 非路径词、完整选择器映射、旧字段对象和运行源 hash 映射。没有执行 Node CLI、AST／compile、数值例子、本地科学或新 benchmark。

三份最终 ready 的身份为：

| ready | 字节 | SHA-256 | Git blob |
|---|---:|---|---|
| normal | 61812 | `e0b3728a65788157abb245058fccbc477714e181ec34da8e9d1459a555a28d3e` | `d2dfbda375f6dc896d994de865ccd40017066757` |
| geometry | 59207 | `d971eeb39b6c3b40b1531f68b8f10a039161a441ff1f19255b754305a6ab461a` | `6f1da76a472d17f54512855e71ad946016b87061` |
| closed | 92335 | `a6277fb071145363b2533e59e6aafd86f2ca4ba4b9a40579ed461846fb9964f6` | `e60b4bbcf83f7b9457b40ae4ba40d46ea6c3e34f` |

三份 ready 共 213354 字节，每份均小于100000字节。
仅将这三个完整 step 组成 `{"steps":[...]}` 的紧凑 JSON 文本含末尾换行时为 20867 字节；这只是明确对象的字节数，不冒充根实际控制器队列的最终大小。root 保留唯一发布、队列和执行调度职责，实际队列仍须完整保留其原格式与正在等待的步骤。
