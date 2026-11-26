# 同一真实冻结父的 T0 缓存复用：完整续接入口

状态：完整源码实现；已进行纯文本、AST、compile 和接口检查，尚未执行本版本的科学方向。这里没有新的等距存在结论，也没有新的度量、reach、幅度或精化证书。

## 1. 已核实的重复准备来源

已刊 [`so3_closed_meridian_operator.py`](../scripts/resume_20261126/so3_closed_meridian_operator.py) 的完整身份为 `234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42`。构造函数每次以 `exist_ok=False` 创建新的 `cache_directory`，并初始化一个空的普通 `dict`：`self._cache = {}`。`_parent` 只在这个当前实例字典已有 `(label, tuple(phi.hex()))` 时读缓存；否则调用完整冻结父的 `ParentMeridianJet.evaluate`，随后把四个数组保存成 NPZ。它没有扫描旧目录，也没有读取以前运行的缓存清单。

已刊 [`fullclosed_so3_actual_profile_interior_restore_qp.py`](../scripts/resume_20261126/fullclosed_so3_actual_profile_interior_restore_qp.py)，完整 SHA `0f542de9ab1f91f5ca27a0efe315b0ee96beddd3e3972ba12fbc5140221623a6`，总是把本次 `outdir/frozen-parent-meridian-cache` 传给该构造函数。读 restart 报告和 checkpoint 的代码位于构造之后。故新输出目录会丢掉旧字典的索引，即使旧 NPZ 仍保留，也会再次准备相同冻结父的 T0。这个实现事实解释了为何仅保留旧目录并不能节省重启时的完整父场准备。

真实冻结父的完整提供器是 [`so3_parent_meridian_jet.py`](../scripts/resume_20261126/so3_parent_meridian_jet.py)，SHA `d3f25bb74e179865b20f7759bc1ee8dcdf2c2771f062ac096ee4d5398a8be4b9`。它已经独立核验真实父 bundle、全部 q/core/H、完整 canonical model、标量、节点、观察载体以及真实物理函数来源，并保存冻结副本。本次只复用这个提供器已经返回的四组数值字：`T0`、`T0_s`、`T0_phi`、`T0_phiphi`。

旧 NPZ 文件名只是 `canonical({label, phi}) + '.npz'`；旧报告没有逐文件 cache SHA，也没有保存 cache 查询的径向数组 SHA。不能把它们描述成已经受到旧报告逐字承诺的文件。这一缺项在新输入记录中明确保留。

## 2. 新入口的准确范围

新增 [`so3_frozen_parent_cache.py`](../scripts/resume_20261126/so3_frozen_parent_cache.py) 只向原有的普通 `q._cache` 填入原协议的 `dict(cache_path=...)`。**234ac 的所有方法保持原完整字节，d3f25 的所有方法也保持原完整字节。** 它不替换 `_parent`、`_parent_tensor`、`fields_torch`、J、J* 或任一几何入口。构造时还逐项核验这些方法的实际 `__code__.co_filename` 对应的完整源码 SHA。

四个数值数组是对固定父的查询结果，不依赖当前待求的 omega、自由 core 或 H。复用它们不会删掉当前 free core 的隐式逆图链，也不会缓存当前新场 F、当前残差、当前方向或线性算子。原表示中的 `h' Delta`、全部六 jet、全正权 Gram、原 H² 母范数、完整原 192 行、幅度行、永久位置及所有真实非线性试步筛保持原实现。

新的完整 driver 是 [`fullclosed_so3_cached_interior_restore_qp.py`](../scripts/resume_20261126/fullclosed_so3_cached_interior_restore_qp.py)。它以 0f542 完整体为基，增加缓存来源、清单和续接绑定。显式正 `restoration_interior_margin` 仍只收紧 Phase I 的搜索目标；原物理 g 和非线性接受条件未放宽。首版没有额外接入 SOC，不能把别的已刊 SOC 代码计入本入口。

新入口仍要求公共仓库 Actions；本地没有调用 F、J、T0、数组提供器或科学 fixture。准备命令和纯读数入口分别是：

- [`launch_so3_cached_interior_restore_actions.py`](../scripts/resume_20261126/launch_so3_cached_interior_restore_actions.py)；
- [`read_so3_cached_interior_restore_report.py`](../scripts/resume_20261126/read_so3_cached_interior_restore_report.py)。

## 3. 首次采用旧缓存时的绑定

复用是显式参数：

```text
--reference-cache <实际旧 outdir>/frozen-parent-meridian-cache
--reference-cache-report <同一个实际旧 outdir>/report.json
```

两参数必须同时提供。它们与 restart 可以来自不同的已完成预算，只要真实冻结父及完整查询一致。cache donor 的报告自动加入永久位置来源列表，因而它提供的失败试步及最终记录位置也继续保留。当前 restart 则继续携带自己的全部位置；两者不以文件大小或十进制近似合并地址。

旧报告只允许完整来源 7e9095 或 0f542；新版本的自续接则绑定本版本完整 driver 字节。来源检查读取每个来源文件真正的 `SOURCE_PINS`，逐项验证完整真实依赖，使用已刊 9ca39 实际父绑定器复核固定标量目标。新版本没有把旧报告改成自己的 schema，也没有借一个宽松 source 白名单跳过完整来源核验。

每个 cache donor 必须满足下列实际条件：

1. 它是已经完成的真实数值预算，报告和实际 `final.npz` 的 SHA 一致。完成不等于几何可行，缓存复用不要求、也不冒认该场已经可行。
2. 它来自当前同一 `GITHUB_RUN_ID`，目录必须正好是该实际报告旁由原源码写出的 `frozen-parent-meridian-cache`。本首版不采用从其他运行搬来的无来源原始目录。
3. 当前 q 的完整 model、固定标量、真实父 q/core/H 绑定、原始父报告、bundle、观察载体、节点、标量输入、M/J/N/P 都与旧报告一致。路径之外的每个完整 provider 绑定字段继续保留。
4. 当前完整 `integration` 和 `grid` 查询分别记录所有 cell/u 数组的 dtype、shape 和逐字 SHA；同时记录 mesh、完整 quarter phi、Gauss u/w 和完整父 model。它们构成新缓存查询身份，不把 shape 当成父身份。
5. 首次旧缓存采用还要求原 NumPy 版本、Torch 版本、线程数、Q 和角块宽与当前相同。旧径向查询哈希未记录这一事实仍标为 false；它们的来源是同一实际运行中未改源码和未改输入的查询规则，本次才保存当前 literal 数组哈希。它不是向旧报告倒填一个从未记录过的承诺。

首先列出当前完整角网格的每个原角块，分别寻找 `integration` 和 `grid` 文件；再为全部已知永久位置的每个确切 phi 寻找 singleton `integration` 文件。文件名由完整原协议重新计算。未知文件没有足够的 label/phi 身份，不导入。已知但缺失的文件也不假造；实际请求它时，原 234ac 调用原 d3f25 完整计算。

对每个实际找到的文件，核验四个数组齐全、精确 shape、float64 类型和有限性，记录文件及每个数组的 SHA。用 `allow_pickle=False` 读取，不接受 symlink。然后把同一文件硬链接到本次新目录；若文件系统不支持硬链接，则完整复制并重新验证两端 SHA。原旧目录的数值内容和报告不修改。

该第一次采用是一个**当前明确记录的数值输入绑定**。它不能倒推成历史文件早已被报告 hash，也不支付数值归一化、libm、积分或其他舍入误差。这些费用仍按原连续证书责任处理。

## 4. 本次及后继的完整清单

清单位于本次运行目录的 `reference-meridian-cache-manifest.json`。其中包含完整查询绑定、每个实际采用或新产生文件的 label、literal phi、四个数组的 shape/dtype/SHA、文件 SHA、来源和完整点数。它属于 runner 原始记录，不进入 Git，不上传 artifact。公开报告仅记录清单路径、bytes、SHA、身份和标量计数。

每次原 driver 保存报告时，管理器读取原 `q._cache` 的实际索引。新产生的条目来自未经替换的实际提供器，逐项加入清单；已绑定条目不允许修改。完成预算时再对全部当前文件重算完整文件 SHA，随后将最终清单 SHA 写入真实完成报告。清单的写入是临时文件加原子替换，报告不会宣称未写完的清单已完成。

后继若采用本新版本已经完成的缓存，先核报告真正承诺的最终清单 SHA，再核同一完整查询身份和每个实际文件。此时可以复用清单中所有有明确 literal phi 的条目，包括旧版文件名本身无法反解出的角点。缺失条目仍回原提供器；已有但 checksum 或数组错误的条目会明确拒绝，不静默把错误数据当成缓存命中。

此处“不可变”指一个已经绑定条目的数值字及其查询身份不变。后续实际遇到新的角地址可以增加新的条目，完整清单随实际报告保存而增加，不意味着旧条目被改写。当前待求 x 不进入 T0 的身份。

## 5. 可读的成本和责任字段

报告的 `reference_meridian_cache` 给出：采用文件/点数/bytes、hardlink/copy 数量、缺失计划条目、未识别旧文件数、新产生的文件/点数、完整清单条目数、真实缓存 setup 时间、新文件验证时间和最终字节审计时间。

234ac 的原 `parent_jet_evaluations` 和 `parent_jet_points` 继续只计算本次真正调用 provider 的次数及点数。它们没有为了显示节省量而人为增加。缓存命中次数没有另加 hook，因此明确标为未插桩，不把采用文件数写成实际命中次数。实际完整初读时间和当前原始 counters 可以回答本预算到底省下了多少父场准备。

原 `maximum_requested_parent_norm_deviation` 只包含本次 fresh provider 调用；以前缓存采用的父归一化诊断单独记录在 donor 字段，明确是来源报告的旧诊断而不是本次重算。它不被塞回 q 的新计数器，也不被当作向外上界。

最终 `total_actual_seconds_including_cache_manifest` 包含末次清单审计；原 driver 的 `total_actual_seconds` 字段仍保留原计算位置。两者的含义没有混合。

纯读数入口核完整新 driver、所有实际角色、相同固定标量、原 Phase I 含义、全 C 计数及真实试步筛，再核完整清单。`--verify-cache-files` 只做原始 NPZ 文件 SHA 归因，不重算任何科学数组；它与 `--verify-final-bundle` 可一同启用。无论是否复用缓存，最终闭等距、连续 reach/幅度、全相位非平凡性和固定问题精化责任仍未因此得到解决。

## 6. 本轮静态核验与 ready

四个完整源均已在实际可用环境进行 stdlib AST parse、compile、重复字面 key 及尾空白检查。新 driver 的全部原顶层物理/线性函数与 0f542 AST 相同；除 `save_report` 的清单记录外，内部科学函数 AST 相同；从 `def statistics(point, native)` 至文件结束逐字相同。launcher 去掉 `--print-command` 和 `--install-torch` 两个专用选项后，其完整 parser 与 driver AST 相同。完整 ready 参数已通过 launcher 的纯 `--print-command`，返回 0，并实际生成 111 个 argv 项；没有导入科学模块。solver 另独立静态核对完整 helper、原缓存协议、adoption/restart/save 接线，未发现阻断。

这轮只有源码静态检查，不冒充科学通过或缓存加速的实际时间。完整 ready 保留原固定父来源及同参数，使用新的输出目录，并以已经完成的旧缓存作为显式输入。实际排队时，根代理依据原 0f542 真实返回选取 restart；本实现没有为了生成一个阶段报告而预造下一父的结果。

## 7. 实际48支持的完整64步继续与公开排程

root亲读 [真实46–48](2026-11-26-public-actions-45800076687-1-part-005.md)。新restart准确锁 `793bde458be303034d3f3a0b1b7f9fd17d7cf84ec99fc1b3bb5313ce10008044` / `bb5c52e02af18b02cd2aed9a9d64fe6bb687f8f1f1510fe0792684ff241f9241`；原冻结父d021、profile0a223、modelad017、normc4b2和全部四源输入不变。首次缓存donor采用已完成7e first目录及其3b73报告。实际43、46的cleanup只列自身rows-*；44、45、47纯读数cleanup空，未记录删除任一frozen-parent-meridian-cache。这里不把未删除日志冒作独立目录存在检查；新launcher/helper仍在runner完整检查实际目录、report、final、来源和字节。

实际48已证旧metric QP是16步iteration_limit，Pg 4.769888394947521远高于原5.208014191841168e−6容差；满步Phi下降但真g=0.002834877771912603，回溯到1/16才过。完整QP385.735416386秒，全方向819.6019953670002秒。故下一次把完整内层预算显式增加为64，且另行继续全约束二阶修正的实现，不能把全部截步只归因于QP未驻点。

[完整两步参数](../computations/resume-20261126-so3-cache-reuse-1x64-ready.json) 为13116字节，SHA256 `746e30daf4c892e0847faec5f15631429e2f12122b18b7d9dc333b613987a8e9`，已排02。从真实793b末场开始，本预算一条完整metric方向、至多64次推进，原4×64恢复、两种mu .01、内点搜索margin1e−8、全部原full C、固定正权目标、真g≤0与所有历史地点保持。单次方向预算只为让当前公开作业完整返回此方向，不是研究停止或数学收敛门；实际返回后继续。此前仅供选择的1×16及2×64草稿不作为本次已执行参数。

| 本次完整小源 | 字节 | SHA256 |
|---|---:|---|
| so3_frozen_parent_cache.py | 26048 | 4e9ed6949bf42f8ef103b06d0e15dbfa1a8f7d21317a9492f71dca33195824cd |
| fullclosed_so3_cached_interior_restore_qp.py | 50736 | 174b79f4b2393a719e7ddee70f59fe5c500e89d41e8d181497f1b4329f8b015f |
| launch_so3_cached_interior_restore_actions.py | 11047 | 9b87e0e42c310464a369e8a1e09225c939910cab3a7bcd7c053ac3e6ace12159 |
| read_so3_cached_interior_restore_report.py | 22527 | 6982823418fb60c82ee8e774919b460a19451703bfc78cdd6eaba3f7f5d634ff |

root完整读本说明、完整cache helper、driver/launcher/reader相对原实现的全部差异与本次完整ready；source身份核对通过。没有本地科学试跑，没有预填缓存命中、节省时间或新方向接受结果。
