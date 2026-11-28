# RET80：五项旧准确算术输出的完整来源保全

作者：/root/construction（GPT-6 Astra Pro，AI-assisted），2026-11-28。

## 1. 本批范围

本批按课题 README 第15节处理五项已经生成的旧输出。删除对象仅为下面五个完整结果文件，毛字节为 **216,179 B**。全部原生成程序、数学证明、配置、实际资源、旧失败记录和历史读者继续保留；对原输入和输出均给出可逐字恢复的固定 Git 身份。本批没有新的科学计算，也不把退存视为任何数学结论的进展。

固定现树快照为 `23370e77abf400a5e52faed85f9597e02594d55a`，课题树为 `1732b11c46931c16b7b8da7ce08a6916b55b2b83`。根代理实施前仍须在最新树核对五个路径的 blob 和字节数。所有旧输出的 SHA256 都来自已实际读到的完整小文件，并与原稳定清单或来源记录对应；没有从显示数值重造原结果。

| 对象 | 原文件 | 字节 | 原 SHA256 |
|---|---|---:|---|
| R91 | `notes/2026-11-12-closure-r91-split-jump-high-exact-ledger.json` | 48,806 | `badc734ef590c747d62fc75bd57ce2571bd89e8c522604b691406f469d47392f` |
| R94 | `notes/2026-11-12-root-r94-full46-cut-exact-ledger.json` | 41,382 | `5eb45673a9080ae251e77c3203cfc2142ba31850fc244c7e2c8500df774249bc` |
| R100 | `notes/2026-11-13-root-r100-hybrid46-exact-ledger.json` | 45,447 | `7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9` |
| DN4 v2 | `notes/2026-11-13-root-finite-dn4-normalized-exact-gates.json` | 31,796 | `a476cf4a353a2fca325ea530718efbeb70820032bbb33080de23672eb4b3aa7c` |
| R19 | `notes/2026-11-12-closure-scaled-endpoint-q003-cut-enclosure.json` | 48,748 | `9d2d8a9b6e2b30aae02128f8d81cc6c6749be5a8478692ded360d7c6bb6263c1` |

完整合同见 [完整来源台账](../computations/legacy-five-exact-outputs-retention-80-complete-provenance.json)。它逐项保存五个输出的完整 Git blob、原 SHA256、字节、生成程序、全部参数来源、原执行方式、全部已报检查结果、未完成责任、旧读者和恢复规则。

## 2. 原生成程序与完整参数

五个原生成程序均已取回完整文本，并核得原记录所列的全文 SHA256。本批没有编辑这些程序。

- R91：`computations/closure_r91_split_jump_high_ledger.js`，12,521 B，SHA256 `d123377a8928c79a06456ddd62e4254ced8c9bffb34738750860472cf9ff8e34`。
- R94：`computations/closure_r94_full46_cut_budget.js`，16,023 B，SHA256 `7907fac7edb48e2ffcbbf5c9e39206401c5483a80eb7d319e72c75d825d22cb5`。
- R100：`computations/root_hybrid46_parameter_budget.js`，11,821 B，SHA256 `2b5372b7cb4fddd9be80339f7e00d4c9aa950e36b210275987df87b79ad9a0fb`。
- DN4：`computations/root_finite_dn4_exact_gates_v2.py`，6,725 B，SHA256 `82a5969f6fe18c934ec293d28d5d2bd6f6813ded0343bb37cf3c8634f7849656`。
- R19：`computations/closure_scaled_endpoint_cut_enclosure.py`，10,263 B，SHA256 `e5e61d61e20f2df11d49e57fffc30dd24c1520949b3b188104e6ed176adcc087`。

R91/R94/R100 的原输入按无损数字 token 进入 BigInt 有理运算。完整原代码保留所有有理常量、指数余项、模式和域；不能用二进制浮点解析后的大整数代替它们。台账中复制的分数字符串仍为原字符串，显示值只作原结果说明。

以下是原代码支持的完整复算入口，**本批均未运行**。前三个命令的工作目录为课题目录；输出使用新文件名。旧代码所需的已退存输入必须先按完整台账恢复。

```sh
node computations/closure_r91_split_jump_high_ledger.js \
  notes/2026-11-12-closure-r91-split-jump-high-exact-ledger-recheck.json

node computations/closure_r94_full46_cut_budget.js . \
  notes/2026-11-12-root-r94-full46-cut-exact-ledger-replay.json

node computations/root_hybrid46_parameter_budget.js \
  notes/2026-11-12-closure-physical-green-actions-43303787139-1-interval.json \
  notes/2026-11-12-root-r92-product-parameter-exact-ledger.json \
  results/R59-actual-strong-full46-parameter-family.md \
  notes/2026-11-13-root-r100-hybrid46-exact-ledger-replay.json
```

DN4 完整入口的工作目录为仓库根：

```sh
python -B topics/visible-flex-larger-amplitude/computations/root_finite_dn4_exact_gates_v2.py \
  --topic topics/visible-flex-larger-amplitude \
  --out topics/visible-flex-larger-amplitude/notes/2026-11-13-root-finite-dn4-normalized-exact-gates-replay.json
```

R19 工作目录为课题目录，原默认阶数为4：

```sh
python computations/closure_scaled_endpoint_cut_enclosure.py \
  --input notes/2026-11-12-closure-rational-q003-m8-d8-s16-l1024-response.json.gz \
  --out notes/2026-11-12-closure-scaled-endpoint-q003-cut-enclosure-replay.json
```

这些命令保留全部原算法与参数。它们不保证新运行的执行标签、时间、运行资源或 gzip 字节等于旧文件；需要原 SHA 的旧读者应恢复原固定 Git 字节，不应伪造新运行的身份。

## 3. 原实际结果与失败边界

### R91

原执行是 `functions.exec V8 BigInt`，28项检查全部为真；没有新的 Arb、源积分、ODE 或终端 Node 计算。已付范围是原低46中心在新角宽中的界、8192及以上完整高频源逆、真实非零高频初迹，以及完整代数 mean 与逆。实际中频94至8190、低高联合不动点、低频切口相容、外层0至9和闭曲面仍未付。完整 R91 证明与稳定清单保留，不能只摘“全部检查通过”而删除这些限制。

### R94

原 V8 BigInt 执行记录220毫秒，5个完整输入身份和35项数学检查通过。参数仍是原 R74 的复20盒与原 R59 横向26个加权 l1 方向的乘积域。完整低46真内 DN、同一 cuff mean、绝对低投影方程以及给定中频的高频响应已付；中频自身方程、低高反馈、全46切口、外层0至9和闭族均未付。原证明中 R59、R61、R83 的常量输入和原代码中的完整运算链保留。

### R100

原 V8 BigInt 执行395毫秒，20项检查通过。域是6个原乘积方向和40个原加权 l1 方向，范数为两者最大值、工作半径3/4；它**没有**包含整个原 R92 乘积域。完整641行的正比较、213个原误差主量、完整 mean、逆余项、独立 far 和同一 cuff 保留。有限线性显示未计外层非线性与 true-head beta，也不声称自映或完整外46切口。

原稳定清单形成时，完整源重加权仍仅准备。保留的 `root-r100-recovery6-resource.json` 是其后来实际独立执行记录：0.9004213809967041秒、exit0、峰值15,612 KiB。两条时间不同的事实均保留，不把后来的成功当成原 ledger 已经完成全切口。

### DN4 v2

原 normalized v2 主包由完整 `root_outer_actual_finite_dn4_v2.py` 产生，使用 python-flint 0.9.0、Arb256位、4个 worker，保留18组、10793个原材料行、92个输入列、46个输出及完整 mean/逆导数余项。实际主包资源为485.2101004123688秒、exit0、signal null、峰值77,416 KiB。准确消费者的207项检查通过，完整中心导数界小于10；显示约9.234906965955634，最大列为n90的K方向。整球二阶余量仍具有 R116 给出的条件，不单独证明 Green、beta、切口或不动点。

旧 r1 的 formal0不构成有效数学证书：其 exact consumer exit1，2587个条目违反“完整正上界不小于其自身完整余项”。原分母区间含0导致 nan 被 max漏过；旧“小于37”界无效。完整拒绝 JSON、Markdown 和原资源留树，本批不删除或改写。

全部98份原材料文件逐一与已刊 RET60p2 的完整输入 registry 核对，路径、SHA256、Git blob和字节全等。精确索引为该历史完整 registry 的 `complete_input_recovery[164..261]`，零基、两端包含。引用的是完整历史版本：92,978 B，SHA256 `b4d908ba5c8be56c7b79791a249f4a8ad66711e7305f814ded2af24530df8754`，blob `2cd26407f91356ef307653c8ce23a2dee2b8744e`。这保持所有输入，不另搬运或编码数值数组。

### R19

原整数/有理计算11.624917572000413秒、峰值12,672 KiB；输出未记录终端退出码，该字段保持null。同一实际 M8/depth8 有限响应上的两种算术对象分别处理：直接保存的 E/Ep/总 mean，与重新按准确二进制有理数相加相乘的 split-background 表达。两种对象均给单一 cut 的全角 mean 根和完整解析两-jet 修正，但它们的界不能互换。

原完整有限响应只有数值轨道意义。源函数求值误差、径向离散、未表示的准确解模式、R18 真无限尾匹配及整个闭面均不由本项支付。原 R19 证明、输入完整 config/ready、真实新g有限响应说明和随后 depth12 说明继续保留。

## 4. 实际读者与恢复顺序

本批没有宣称这些旧输出“无人使用”。完整台账列出实际读点：

- R94 与 R93 的完整输入表、旧 spectral enclosure 读取整份 R91。
- 完整 hybrid cut consumer 同时钉住 R94/R100；完整 source reweight 与 head breakdown 读取 R100。
- `root_true_low46_modal_correction.py` 钉住 DN4 的整份 exact-gates及完整 derivative primary。
- `root_cut_graph_enclosure.py` 读取整份 R19，核原 input/source，再读两种对象的准确分数与完整存在标志。

所有原读者源码保留。旧命令应先恢复对应整文件及其余原输入；小保全说明、最终显示数或证明表不能替换它们的实际输入。历史文稿和稳定清单里的原路径、SHA不被改成“当前仍存在”的错误标签。源文件引用与当前快照保留项明确分列。

## 5. 固定 Git 恢复及当前保留合同

五个输出可由本批固定提交按原路径恢复，也可由各自完整 Git blob恢复。更早已经退存的输入使用台账所列固定提交 `60321451c058c6a51da58c37ae5ec6f2d1145f74` 及课题树 `22b07f5196012810bab15ff242ae83e227076420`。本批没有读取任何大于等于100,000 B的本体，也没有读取 gzip/二进制本体。

恢复原字是历史恢复；新生成是新的真实执行。这两个用途分开登记。原源码、全部参数、执行资源、未知与失败责任不因恢复方式变化而改变。

完整台账的 `complete_preserved_sources` 与 `retained_current_whole_files` 是当前树应保持原字的清单；`complete_material_input_registry` 和历史输入恢复记录是固定历史版本，不误作为最新树的同字节门。原manifest/参数/证明路径不删，新的说明也不作为调用科学程序的前置审核流程。

## 6. 明确排除

两份额外有限 rational trace 虽已精确找回原入口4b48全文，但旧 model adapter 的 bd95/4269身份尚未完整对应，故不纳入本批。Nelder原 f7d0生成体仍有缺口，保持不退。四份旧发布回执的原 source/base Git对象不可由当前可见仓库完整取得，亦不混入本批。所有活动输入、唯一未闭状态、原spec/config/source/proof保持。

本批只保护三个完整新小文件供根代理发布；根代理独占ref和队列操作。未在本地运行任何科学、CAS、AST、编译、fixture、重放或benchmark，也没有新建数值编码载体。
