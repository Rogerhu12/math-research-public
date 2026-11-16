# R562 — request236：准确二进制角向平均、完整复用祖先与原全门的实际来源组合

作者：ChatGPT（AI）  
日期：2026-11-16

**可信度：已证明（限本文列明的来源组合、准确字运算及控制流条件命题）；request236 的编译、owner、replay、投影模型、FD、fullDN 与最终 audit 尚未执行。** 本文不把来源准备、安装或计数当作数值接受。实际终态另记 R563。已有 request232 仍是独立运行；本文不修改它、不读取或继承其求解结果。

## 1. 本次交付和准确边界

本次把 R561 的三个角向归一化接点放进正式 R551/request232 的完整原执行链。保留 R535 的本次 root 有限字共享和 R550 的同一 root 内完整已接受 RootEval 复用；实际 owner 改为只安装一次 R561。R550、R535 的安装函数不先行调用，二者仅在源码准备阶段真实重建并成为新编译输入的祖先。

实际修改的数值位置仅为原 primal 的 root residual、root Gram 与 primal flux 中第二次乘法。原第一乘积照算，原逆数表达式照算，原角与分量累加顺序照旧。合格字可通过修改指数得到准确相同的缩放字；其余全部执行原第二乘法。R561 的 trace view 保持全部方向算术，只把原 root_matrix 调用接到带原统计对象的新 primal 函数。

完整576阶段、每阶段226状态和224方向、两个均值、原112边界、混合338×112末端响应、原FD/fullDN及最终独立audit均保。原128 owner 最终值与 fresh replay 仍是当前状态的来源；由其一次 RN64 投影构造的完整同 DN 模型仍是明确的 binary64 线性模型。本文不把它改称 owner128 的准确导数，不把投影点改称已接受 native 状态，也不添加全解析338行或新模型误差阈值。

本交付五件：一个源码生成器、一个完整逐字来源计划、一个完整请求、一个工作流和本文。十个调用者及两个 R561 include 只在本次公开 Actions 的实际 computations 目录生成，不以展开全文、压缩包或分片重复入 Git。

## 2. 冻结来源、完整计数与字节身份

### 2.1 直接祖先

直接祖先是正式 R551/request232 主线：

- commit：`42492b0c728e260b3b1de8be79b4ab962259ad3e`；
- 原请求：`public-live128-root-reused-projected-model-original-full112-FD-fullDN-request.json`，91119 B，SHA256 `1e1b37ac0184eea4111989cb080214fa734cabd7f8f16b1cf859bd9cec494fd5`；
- 原生成器：`root_20261116_live128_reused_projected_source_views.py`，37196 B，SHA256 `c501c85b7ec9fe44b7d5642c49025dea57862b9bb482e656425a282c8eb86f10`；
- 原计划：`notes/r551-live128-root-reused-projected-model-complete-source-plan.json`，77676 B，SHA256 `06acd58ff29dd4dee359341711174ae10897843984347833511be8faac82d124`。

上述完整请求、原生成器及其实际祖先计划由新生成器读取并核对。本次不是以旧计算结果为输入：实际新 run/source、同次 receipt、重新编译及所有科学量仍须在新 job 产生。祖先请求中历史源码说明可由其已绑定全文和明确 JSON pointer 恢复；原输入、算法、资源及全部源码 map 并未用历史说明的缩写替代。

R550 的正式来源为 `bb4a03981babcf956e408930538941d54b2c547a`。准确复用责任见 [R550](R550-same-root-accepted-complete-evaluation-reuse.md)。R551 的完整链和必要选择见 [R551](R551-request232-accepted-root-reuse-and-honest-projected-model-complete-entry.md)。R561 的准确缩放与原首乘积责任见 [R561](R561-exact-normal-dyadic-average-and-original-first-products.md)。

### 2.2 新 R561 三件

| 角色 | 完整相对路径 | B | SHA256 |
|---|---|---:|---|
| header | computations/root_20261116_exact_dyadic_average.hpp | 6760 | e94b31dc091a8a727ab6f4808fb61e951cb892fc496120fe8312c82b7d71c0ac |
| adapter | computations/root_20261116_exact_dyadic_average.py | 18526 | 9d954a23b1a8991c4aff38c1ffb6879229552cc9894ba70e7c3fb485fa928082 |
| 数值源码计划 | notes/R561-normal-dyadic-average-complete-source-plan.json | 13708 | 5667d987ea5b7387bb0c4f6c61d86cd9ea94035299da91d3c7889fb1cde5f5a7 |

R561 的实际生成 include 为：

| 角色 | basename | B | SHA256 |
|---|---|---:|---|
| primal | root_20261116_exact_dyadic_average_primal128.cpp | 26420 | 0e01b54b3b456711efd23ba94961eb669aef5394ab848e720fcf4a4ac64c854f |
| trace | root_20261116_exact_dyadic_average_trace128.cpp | 35787 | 07b8fd4dd7d31b2728e0f74a3ed9c9e6653593376529c12d26cdb57d617b8dc5 |

这两件不是预存公共 Git 文件。R561 adapter 按实际 R550 include 全文、每处 before/after/count 和完整输出 SHA 构造它们；逆替换恢复完整原文的检查仅为已声明源码身份责任，不是数值对拍或新增科学门。

### 2.3 并集

| 集合 | 公开源码 | 本 job 生成源码 | 总数 |
|---|---:|---:|---:|
| 正式232完整祖先 | 351 | 51 | 402 |
| R561 新 header/adapter 与两个 include | 2 | 2 | 4 |
| 本次新生成器与十个 caller | 1 | 10 | 11 |
| 实际236并集 | **354** | **63** | **417** |

原402项的每个 basename/SHA 均原样留在新请求 `source_sha256`；原51项也原样留在 `generated_source_sha256`。祖先生成源码不被误列为可从 Git 直接读取的公开源码。计划61个逐字补丁覆盖十个新 caller，各有完整原文身份、明确次数和完整结果身份。

这是实际声明并逐字检查的有限来源集合，不是对任意未执行动态 import 名字的无限闭包断言。原 Actions 的 Python compile 和 Node --check 仍在真实工作流中执行；本文没有在本地执行它们。

### 2.4 本次四执行/入口件

| 角色 | 路径 | B | SHA256 |
|---|---|---:|---|
| generator | root_20261116_live128_dyadic_projected_source_views.py | 37603 | 0f984347d801b3b8132b7814494b3f883f72ef1bd73d00aa15d01b767c2de85c |
| plan | notes/r562-live128-dyadic-projected-model-complete-source-plan.json | 64999 | a72e2d5a225a977c6eec7d3f7d65066b102a405b1362af5b855d38495b8c4780 |
| request | public-live128-root-dyadic-projected-model-original-full112-FD-fullDN-request.json | 97937 | 299cf5532e510c3629354347d1ba03aa57135077a1530b605867b0f71e08cb45 |
| workflow | .github/workflows/visible-larger-public-live128-root-dyadic-projected-model-original-fullDN.yml | 23459 | b683e42765e1ca758ddf8d189fbb501057f733e5dcc920594a9e9878ea082b66 |

本文不把自己的 SHA 写入自身；其最终完整身份在发布提交及交接 manifest 中给出。manifest 仅用于交接，不新增为题内科学文件。

## 3. 三个缩放接点的条件命题

设原实际第一乘积字为 $z$，原实际逆数字为 $v$。R561 仍先按原表达式计算二者。新函数先检查原整数 $N$ 是否正且为 $2^k$，并逐位确认实际 $v$ 恰为正的 $2^{-k}$。此外只在已声明的16字节、113有效位、小端 IEEE binary128 与16字节 unsigned integer 布局上使用位式；不支持的布局执行原乘法。

对于非零正规字，设其符号为 $s$、偏置指数为 $e$、112位显式尾数为 $f$。它表示

$$
z=(-1)^s(2^{112}+f)2^{e-16383-112}.
$$

当 $e>k$ 且 $e<32767$，缩放后的偏置指数 $e-k$ 仍在正规范围，完整尾数与符号不变，因此

$$
z\,2^{-k}=(-1)^s(2^{112}+f)2^{e-k-16383-112}
$$

本身是准确可表示的 binary128 字。仅从指数字段减去 $k$，不丢低位、不做两次舍入。对这个分支，原第二乘法的准确结果已经可表示，按原浮点合同得到相同结果字。$+0$、$-0$ 分支保留原符号；逆数是正数，故这也保留原乘法的零号。

若输入是非零次正规、非有限，或正规缩放后可能进入次正规范围，则新函数执行原 `product*inverse`。即使某个边界次正规结果本身准确可表示，也不为它扩大快捷分支。任何 count、实际 inverse 字或布局不合资格，同样走原表达式。资格判断不是拒收，不构造新数学阈值；资源异常也没有被捕获后重开计算。

三个接点分别是：

| 原路径 | 原第一乘积 | 原被替换第二乘法 | 保留的次序 |
|---|---|---|---|
| root_evaluate residual | `quad*cs[i]` | 与原 `invN` 相乘 | 原角 n、分量 i、原加法顺序 |
| root_matrix Gram | `value*gc[k]` | 与原 `invN` 相乘 | 完整0…2M频率和原累加顺序 |
| primal rhs flux | `f*sn[j]` | 与原 `invN` 相乘 | 原角 n、分量 j、原加法顺序 |

这里的 cs、gc、sn 是实际原表字，不使用理想三角恒等式；没有把 pref、ell 或任何首乘积提前约分，也没有移动 invN 穿过加法。new root_matrix 多传原 RootStats 引用，只负责记录本次调用。

**命题1。** 在 R561 的字布局、原算术语义和相同实际输入词条件下，每次完整返回的快捷分支给出原第二乘法的相同有限字；回退分支直接执行原第二乘法。全部原首乘积、项数、加法顺序及方向表达式保持。因此，该替换没有改变这三个既定数值表达式的值责任。

这不声称所有运行前缀、异常 payload、硬件浮点状态副作用、内存布局、墙钟或资源截止位置完全相同。新计数只反映实际执行过的工作。原程序仍可能在任何原试步、owner、replay、模型或末门处停止；不能从源级字等价推导本次必完成或有某个加速倍数。

## 4. 实际源码准备：一条祖先链、同一代码目录

新生成器的 `context` 要求真实公开仓库 Actions 四个身份键，并要求：

```text
HERE = GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations
args.computations = HERE
out = RUNNER_TEMP/request236-source-preparation
```

不得把新源码放进另一目录却让 caller、config 或 receipt 仍指旧目录；不得覆写原 Git 科学源码或把新来源冒成旧 SHA。

`prepare` 的顺序是：

1. 真读完整232请求、生成器、来源计划及其 R534 core plan，并核402/51两个原集合。
2. 实际调用原 R551 generator 的 prepare，固定输出 `RUNNER_TEMP/request232-source-preparation`。该调用内部继续其原 R547/R534/R527/R518 来源恢复。完整402件均在这个新 job 中重新获得，旧实验的临时目录或输出不会被复用。
3. 原 R551 来源 receipt 必须实际返回且 complete、run、HERE 均一致；随后逐个读取原402文件的完整 SHA。原失败、stderr、partial、not_generated 后缀由原 receipt 保留。
4. 依据本次61个 literal 补丁在内存中形成十个新 caller，核每个输出的完整 bytes/SHA。未到写出阶段的 caller 仍明确列为 not_generated。
5. 实际调用 R561 source-only CLI。它内部真实调用 R550 source-only，后者真实调用 R535 source-only。R551 已生成的同字祖先 include 可被逐字重新核对；不覆写科学原件，也不因已有文件略过来源责任。
6. 核 R561 binding 的实际 run、HERE、adapter、完整两 include 以及 source_preparation_complete=true、compiler_completed=false、scientific_evaluation_performed_by_preparation=false。两条 include 的 observed/present/actual 字段来自真实文件。
7. 独占创建十个新 caller，写完整417 map、63 generated map及实际角色映射。最后才置本层 complete=true。

新 source record 中的 `R551_child` 保完整 command、started/returned/exit、stdout/stderr身份和实际原 source receipt，但不重复内嵌原385KB级源大对象。该原对象仍在同次目录，原 necessary reader 会实际读它。相反，当前 `R561_child.source_result` 是实际完整 binding，owner 随后逐字核它，不用摘要代替。

**命题2。** 若本层 prepare 成功，则十个新 caller 与两个 R561 include 的身份由完整原文件和明确的逐字变换唯一确定；417 map逐项等于真实同目录文件，原402词保留。此命题的前件仅支付源码准备，既不支付 g++，也不支付任何科学结果。

## 5. 真 owner 的单次 R561 安装

新 owner 的 `install_exact_dyadic_average` 在真实 `owner_scope = scope["source_scope"]("owner")` 得到之后、原 main 开始之前调用。它读取本次236 source receipt，核 schema、request_number、四个 run 键、actual_computations，以及 owner 在 generated 列中的真实完整文件身份。

接着读取固定实际路径：

```text
RUNNER_TEMP/request236-source-preparation/R561/source-binding.json
```

要求其整对象等于实际 `R561_child.source_result`，保留 descriptor 与完整正文。实际安装模块是18526 B 的 R561 adapter，不是旧 R550 installer。

R561 的 install_owner_compiler 要求原 scope 中 `_R561_SOURCE_BINDING`、`_R550_SOURCE_BINDING`、`_R535_SOURCE_BINDING` 均尚未存在，保证一次直接安装。它仍核原 persistent owner、原 persistent CPP、原 compile_owner 的完整函数字节及显式源码变换。原 owner 的 main、solve/replay及实际全局命名空间关系不变；被替换的是已声明的 compiler 接点。

完整新 compiler 函数为6256 B，SHA256：

```text
97e534367318ae3f16e3d24b0628cc603ca99c0cbb7e6b830db6d59e6a5afc03
```

原完整 compiler 函数为3860 B，SHA256：

```text
be019045058f4616f98b07e19c0d8d3901e979ce2b1ba7d4259c65fcae4ae46d
```

原 persistent CPP 为22364 B / `7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd`。R561 计划保它原样。原 g++ 仍由随后实际 main 调用；prepare 或 install 成功不能填 compiler_completed。

实际安装保三个既有 receipt 槽位，其名称不改作虚构旧实现：

- `root_finite_word_cache_source_preparation`：当前 source-views.json 的真实 descriptor；
- `root_finite_word_cache_source_binding`：当前 R561 文件 descriptor 与完整 actual_binding，包含 R550/R535 所有实际 ancestry；
- `root_finite_word_cache_compiler_installation`：实际 R561 installer 的完整返回。

真正 compile 返回只来自原 summary 的 `compilation.root_finite_word_cache_compilation_source_binding`。它含实际 compiler command、全部依赖、stdout/stderr、可执行文件、returncode等；不能由前述安装正文补填。

原 R534 deferred handoff 仍在该 scope 中按原序连接。只有原最终值/原 tolerance/fresh replay/真实完整 final-state 均就绪后，当前 Node 才可构造其完整模型；defer 本身不冒四组件已完成，更不冒 native/fullDN 接受。

## 6. 十个新 caller 和不变的三个数学消费者

| 角色 | 路径 | B | SHA256 |
|---|---|---:|---|
| owner | geometry_20261116_live128_dyadic_projected_same_call_owner.py | 25904 | 2b2070afb87813910f6422600a63c80d16c0f551897b2e23ab4b2b3497a80dbd |
| system | exact_20261116_live128_dyadic_projected_current576_system.py | 29055 | fc56dd3988c4ea7f95a080383f5e110ce7d64e6610ad8872975f1cdc068e3c36 |
| qr | exact_20261116_live128_dyadic_projected_current576_chain_qr.py | 21847 | 1137208df50318002518d569ce5de8f9477af44edd3013db496a4167f2edc674 |
| pipeline | geometry_20261116_live128_dyadic_projected_call_pipeline.py | 43209 | 8b4b4e93aa37f3e60844f1a8b74950c86c96818438d7f66b37c7c9910187548e |
| call | geometry_20261116_live128_dyadic_projected_current_call.mjs | 45399 | ce6b5c88bdc1af47da048c03fcf70457aeb05ec832094bc956f3ff633a088f89 |
| worker | geometry_20261116_live128_dyadic_projected_worker.mjs | 8305 | 362ca026dcd26f491f4c584456f2aae58ed484c43b55b7ebec73d00c3d9b31c1 |
| client | geometry_20261116_live128_dyadic_projected_tail_client.py | 37549 | 725d73de59d916f1131f31f6ce547145e93b5418e280824d767598bbe41195e9 |
| fulldn | geometry_20261116_live128_dyadic_projected_original_full_dn.py | 43270 | 5bc2524395aac3fdc49113313b30453cc93f90cf4d6493d342792668fba84a6c |
| runner | geometry_20261116_live128_dyadic_projected_owned_run.py | 39356 | 97e639c3f98f212fb78e3b8f3420063b17412bc3df39035b6b4e63f161e22764 |
| reader | root_20261116_live128_dyadic_projected_necessary.py | 61330 | 3bda6213246c10163519c9067b85c570fe947f96411b97a459c406fabb95cee1 |

计划为每件保存原R551完整basename、bytes、SHA，61处 before/after/count 及上述完整输出身份。新增文件中的旧完整 LIVE_SOURCE_PINS 仍留作祖先；新当前 tuple 明确追加。fullDN 的 CLIENT_NAME 指向新 client，旧 client 另以实际旧名/SHA保留。其余 loader、worker、pipeline、QR、system、runner、reader逐层绑定真新文件，不靠来源标签推定。

三个未复制、未修改的 R534 数学消费者为：

| 角色 | basename | B | SHA256 |
|---|---|---:|---|
| boundary | geometry_20261116_live128_projected_model_boundary128.cpp | 12844 | 0364ea5cc8173f40dbe7a375fbca798987dcd75b4f67b90470c638352ae8ecb9 |
| components | geometry_20261116_live128_projected_model_final_components.py | 38561 | c4b3a5eb05fc4d4ae6767c2c08f75ea38a5a5538366fcd3264ff59cec17bb04e |
| assembly | geometry_20261116_live128_projected_model_response_assembly.py | 33269 | 863790de6c0c2020d79150ac99134b2a8ee74592cc42669127ca7df296a0f21a |

同一 Node 的实际 full state 一次 RN64 投影、同一 loaded DN 引擎中的576全阶段、完整列/双mean、准确64→128存储 lift、原边界/末端/独立audit、原响应组装次序全部沿正式232。历史 paired stage 来源仍保在417集合中；不据其存在声称本链调用了另一条旧数值路线。

诚实 system guard 原样为：

```python
B.same(current['same_call_complete128_value_components_and_explicit64_linear_model_required'], True,
       'Current128 values/replay and the explicit complete projected64 linear model are required')
```

本文没有重新填旧的 `same_call_complete128_final_components_required=true`，也没有恢复原229/231缺字段导致的旧契约误称。该修复已属正式R551祖先，本次保持。

## 7. 原输入、规模和全部接受责任

本次请求从正式232保留以下八组完整 JSON 对象：original_inputs、actual63、actual91_artifact、runtime、live_call_resources、resources、original_scientific_contract、reviewed_README_blobs。它们在本次文本构造中逐值相同。

实际63只给原prefix初猜及完整 port对象来源；实际91只给原failed73完整tail初猜。不得继承接受状态、旧响应、旧J、旧因子或旧fullDN结论。原六个输入含已接受prefix历史原件、actual63 warm及status、原112config和两原ready对象，仍以请求给出的完整历史commit/blob/bytes/SHA恢复；原78来源也仍按原恢复流程。

| 原合同项目 | 本次保持值/责任 |
|---|---|
| 场/尾模式与 spacing | 112 / 112 / 2 |
| tail阶段与节点 | 576 / 577 |
| 每节点状态 | 224 |
| 局部 RK 状态与方向 | 226 / 224，两个mean均保 |
| 当前末端响应 | slope112、second112、meanSlopeCorrection1、meanSecondCorrection1、height112，共338行 |
| physical J | 完整混合338×112，未宣称全部解析 |
| 原 owner 外圈/试步 | 32 / 10 |
| 原 solve tolerance | 2e−9 |
| FD | direct_boundary和separated_boundary各10方向，原3层step/2层Richardson |
| 原 FD 相对阈值 | 5e−5，全部原适用 contraction |
| 原 prefix inner试步/RMS/边界 | 17 / 1e−6 / 1e−11 |
| 最终消费者 | 同当前H fresh audit，原全部physical RMS/domain/fullDN门 |
| 原使用范围 | 有限prefix问题；不从本链推完整闭面/全域几何完成 |

noJ 请求原本可能仍需要完整组件以返回规定physical量；本文不从“外部未索J”省略内部J、均值或predictor责任。原 same-H cache 只有实际本次完整 current call 之后才可使用。可选 predictor 失败仍沿原规则，不成为新增验收门。

**命题3。** 若沿原当前H控制流完成，那么新调用关系确实通达原全部模型、FD/fullDN和最终audit消费者；本文没有新增或削弱这些数学接受条件。任何实际接受结论仍须由对应真实返回量和原判定函数支付，不由来源数、完整map或程序complete自动提升。

## 8. 原钟、上限、内存与磁盘

| 项目 | 原值 |
|---|---:|
| job timeout | 350 min |
| science step | 320 min |
| 一次科学总钟 | 19200 s |
| 读回/清理预留 | 120 s |
| owner cap / replay reserve | 6000 s / 1200 s |
| stage cap | 8000 s |
| boundary / endpoint cap | 600 s / 600 s |
| audit cap | 1800 s |
| 原threads | 4 |
| Node heap | 6144 MiB |
| 原jac/native workers | 2 / 2 |
| 最大factor bytes | 2147483648 |
| 原startup free storage | 68719476736 B |
| 原free resource stop | 2147483648 B |
| 原uncached protocol call最多声明数 | 18 |

原runtime还保 max_nodes=1200、material_angles=physical_angles=4096、outer_iterations=8、extension_step=0.005、taper_fraction=0.4、native_eta字面“1”。本次数值来源没有缩角、缩模式、缩阶段或缩列。

来源和原输入恢复仍在原 science clock 前；原钟在规则同步和首次native factory前建立，schema仍 `R493-original-full112-live128-job-deadline-v1`。新H不会重启它。每call/per-component cap仍按实际剩余钟裁剪，不能把cap之和当新增总预算，也不能用本次源优化预称将在期限内完成。

来源准备保原10分钟step cap；science保持320分钟；source necessary保持5分钟、科学necessary20分钟、cleanup5分钟、report5分钟。这些是实际工作流资源上限，不是新增数学前门。

## 9. 必要统计：三条R561路径完整保留

实际 RootStats 新成员为 `exact_dyadic_angular_average`，schema：

```text
R561-exact-normal-dyadic-angular-average-v1
```

它的 root_residual、root_gram、primal_flux 各保十个原字段：

```text
terms
exact_normal
exact_signed_zero
original_multiply
fallback_layout
fallback_count
fallback_inverse
fallback_nonfinite
fallback_subnormal
fallback_normal_to_subnormal
```

每条路径另保 last_present 和整个 last：phase、angle_zero_based、index_zero_based、positive_dyadic_shift、original_product_biased_exponent。未产生last时的null与字段缺失分别保留，不能由其他路径的计数填值。

科学reader并不按这十个名字截取对象：它仍选完整 RootStats 字典，含原R53518计数、R550 primal/trace_variation各13计数、全部last、原旧计数及未知新成员。此十字段表只是说明本源实际写出的内容。原counter只计实际执行的工作，不补“如果没优化本来会执行”的次数。

R561三path的join沿原stage index合并；last表示原聚合次序中的最后已返回记录，不冒连续时间profiling。计数能说明实际分支覆盖，不能给出速度、误差大小或科学接受。

原八张具名完整表保留：root_statistics、root_finite_word_cache、owner_compilation、root_cache_compile_binding、三个source/installation receipt对象及physical_source_input_binding。只在完整类型/值相同且负零一致时共享原对象；NaN不被当可相等字节对象。字段缺失、显式null、原数组顺序以及实际unknown成员均保。每个引用context和逆映射明确在返回正文，既有source preparation/installation与actual compilation的区别不变。

## 10. 来源必要读回和原70的完整处理

新 R562 source reader 真实调用原 R551 reader，不把原读回当作已付假设。原R551本身真实调用R547 reader，因此原R549发现的实际旧层102413B超限/70及false传输事实仍可在新job的原来源链中按原规则出现；本交付没有读取旧run已删除的文件，也没有把已发表数值当本次fixture。

新层按这条顺序处理原R551：

1. 核实际 `request232-source-preparation/source-views.json` descriptor，保当前 source record 中实际原child状态。
2. 真运行原R551readback，保完整command、started/returned、原exit和实际stdout/stderr身份。
3. 真读 `RUNNER_TEMP/request232-source-preparation-necessary.json`，核其原schema、request232、原source/plan、同run键。
4. 若该原transport为70，保原child70和原 necessary_readback_complete=false。只允许读取它descriptor指向的同次固定 `request232-source-preparation/necessary-source-overflow.json`，并核完整文件bytes/SHA及attempted bytes/SHA。
5. 由该实际完整文件读取原完整必要对象；若原正常返回0/2，则直接使用原transport完整正文。所有原错误、未生成后缀、缺字段和unknown内容保留。
6. 新层独立判断自己是否读取完整范围；即使新层 complete=true，也不更改原child70、原false或原错误。新层 complete仅表示选择/传输责任，不是来源生成、编译或求解成功。

原R551正文内部已有的R547两表、完整逆定义、原source catalogue与实际原overflow身份全部留在它自己的namespace中。新R562 catalogue以完整232请求402map和本次15新增项为basis，不能拿新的索引去解释旧表。

新层仍只有两种固定metadata行表示：

- 原 source inventory 行只有 file/bytes/sha256且完整path/SHA等于实际bound map时，才用该具名catalogue索引。实际观测bytes、原行顺序、原key顺序均留；未知形状整个字面保留。
- 原literal_changes/replacements使用固定六列：id、count、before_bytes、before_sha256、after_bytes、after_sha256。完整SHA字符串仅按准确相等共享一次，原列值、原键顺序、缺失/null和原数组次序均可逐项恢复。

整对象引用只用于与另一个独立已读取record完全有序JSON相等的明确source字段，引用附原file身份、角色和完整逆。它不是任意数值对象编码，不遍历或压缩科学大数组以绕90KB。

每个实际stderr（包括实际零字节文件）保真实path/bytes/SHA及完整读取范围；缺失日志不能写成空文件。重复stdout正文仅保完整身份，实际选择的source对象由原固定文件读取。

新source正文和新science正文分别遵守原单份90000B及超限70。新层若再次超限，保完整本地对象与实际overflow descriptor，necessary=false、cleanup=false；不拆分、不截原字段、不保证将来体积必过。原source body尚未返回时，不以其descriptor宣称已读完整。

## 11. Schema、路径与真实CLI

主要当前schema为：

| 用途 | schema |
|---|---|
| request | public-live128-root-dyadic-projected-model-original-full112-FD-fullDN-request-v1 |
| source preparation | R562-root-dyadic-current-owner-projected-model-source-preparation-v1 |
| source plan | R562-root-dyadic-current-owner-projected-model-complete-source-plan-v1 |
| owner | R562-current-H-root-dyadic-owner128-before-projected-model-v1 |
| client policy | R562-current-H-root-dyadic-live128-projected-model-client-policy-v1 |
| current pipeline | R562-current-H-root-dyadic-live128-projected-model-call-pipeline-v1 |
| original fullDN | R562-live128-root-dyadic-projected-model-actual63-H-original-FD-and-complete-fullDN-v1 |
| owned run | R562-live128-root-dyadic-projected-model-original-full112-owned-procedure-v1 |
| scientific necessary | R562-live128-root-dyadic-projected-model-original-full112-necessary-v1 |

当前变量为：

```text
VISIBLE_COMPUTATIONS=GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations
VISIBLE_BASE=RUNNER_TEMP/visible-live128-root-dyadic-projected-model236
VISIBLE_NECESSARY=RUNNER_TEMP/visible-live128-root-dyadic-projected-model236-necessary.json
VISIBLE_SOURCE_PREPARATION=RUNNER_TEMP/request236-source-preparation
```

完整实际source CLI：

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_live128_dyadic_projected_source_views.py" prepare \
  --plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/r562-live128-dyadic-projected-model-complete-source-plan.json" \
  --plan-sha256 a72e2d5a225a977c6eec7d3f7d65066b102a405b1362af5b855d38495b8c4780 \
  --computations "$VISIBLE_COMPUTATIONS" --out "$VISIBLE_SOURCE_PREPARATION"
```

source生成器内部的实际R561命令：

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_exact_dyadic_average.py" \
  --source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R561-normal-dyadic-average-complete-source-plan.json" \
  --reuse-source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R550-accepted-root-evaluation-complete-source-plan.json" \
  --word-source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R535-native-root-finite-words-complete-source-plan.json" \
  --binding-out "$VISIBLE_SOURCE_PREPARATION/R561/source-binding.json"
```

该命令由prepare持有其独占目录时执行，不是要求操作者重复启动。真正原输入恢复与科学运行依次调用：

```bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_dyadic_projected_owned_run.py" prepare \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-dyadic-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 299cf5532e510c3629354347d1ba03aa57135077a1530b605867b0f71e08cb45 \
  --namespace "$VISIBLE_BASE"

PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_dyadic_projected_owned_run.py" run \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-dyadic-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 299cf5532e510c3629354347d1ba03aa57135077a1530b605867b0f71e08cb45 \
  --namespace "$VISIBLE_BASE"
```

source必要读回使用同source CLI的 `readback` mode和完全相同plan/out；它在独立always步骤。science必要读回是：

```bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/root_20261116_live128_dyadic_projected_necessary.py" \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-dyadic-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 299cf5532e510c3629354347d1ba03aa57135077a1530b605867b0f71e08cb45 \
  --namespace "$VISIBLE_BASE" --out "$VISIBLE_NECESSARY"
```

两份frame准确为：

```text
BEGIN_R562_DYADIC_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY
END_R562_DYADIC_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY

BEGIN_REQUEST236_DYADIC_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
END_REQUEST236_DYADIC_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
```

prepare模式、readback模式、request/plan的全部完整SHA固定在实际workflow中，未用零占位符。R561 binding源和R562源正文只在本job的实际路径出现，不伪称已刊旧源或旧run产物。

## 12. Owned quiet、清理、report和发布

原PID、PGID、SID、/proc startticks、registered/suspected descendants及无法证明quiet时保raw的算法均原字继承。新名字只让独立namespace与实际request/source绑定一致。science必要reader首先实际调用原quiet；它不凭job结束或process returncode推“所有子进程已静止”。

cleanup保持两项实际必要条件：source_readback_complete=true且science necessary_readback_complete=true；再由原runtime读取真实summary、ownership/run/request并重新核quiet。失败或未完成科学可以在其完整范围已读且原quiet成立后清理；必要范围缺失、超限或quiet未证则skip。本文不删旧运行，不清理其他题或无关目录。

源码准备产生的行政临时目录与实际checkout生成源码仍按原runner生命周期消失；本文的science cleanup只对它拥有的科学namespace行动，不冒整个RUNNER_TEMP都被清空。原raw不入Git、不上传大artifact，不拿输出SHA恢复已删除科学内容。

工作流保 `workflow_dispatch`，无push自动重复触发；root发布者唯一实际dispatch。prepare/source binding/readback/report使用实际 GITHUB_RUN_ID、GITHUB_RUN_ATTEMPT、GITHUB_SHA。来源完整与science必要分别在report中原字重印，同字正文核bytes/SHA，report标签不改科学判定。transport错误会覆盖先前step输出的true，不保旧true冒本次成功。

## 13. 完整条件结论与未付范围

**命题4（实际组合）。** 在本次已列原文件/计划身份与真实Actions环境下，如果source prepare、实际compiler和原科学消费者分别完成，则：

1. 执行的当前owner确实使用R561两个include，保R550/R535完整祖先；不是仅把metadata来源名换成R561。
2. 任一快捷缩放只作用于已经计算出的原第一乘积；不合资格直接原第二乘法。原首乘积、根选择、全部试步及方向算术不被shortcut替代。
3. 当前128状态/replay、once-RN64同DN全模型、原末消费者及全部原接受函数仍按原次序真实支付。
4. actual统计、完整源/安装/compile区分、错误和未访范围从本次原件读取；每份必要正文仍有原90KB上限。
5. 所有新行政字节和科学scope具有自己的实际来源，旧232与其运行结果没有被追改或再解释为236成功。

本文的文字构造只处理源码/JSON字节及完整身份、逐字补丁、有限来源并集和条件证明。没有导入数值模块、执行AST、编译、科学运算、fixture或本地测试。实际Actions中保留的原syntax/compile/solve步骤属于既有完整入口。

仍未付：本次编译/程序执行的真实成功与资源范围、每条缩放路径的实际调用数、owner接受及fresh replay、当前model全576阶段、边界/混合末端/audit、完整FD/fullDN与最终接受、必要正文实际体积、真实quiet/cleanup。没有预称三路径会全合格、shortcut占比、速度倍数或连续几何结论。后续R563必须以唯一官方终态和真实完整必要值归责。

## 14. 题容量及保存责任

本次新题内generator、literal plan、request三件共 **200539 B**；workflow在题目录外，为 **23459 B**。本文是第四个题内新文件，其最终实际字节数在交接manifest中单列，并与前三件相加得到准确题增量。R561自己的四件由其独立发布计数，不重复算在R562增量内。

十个展开caller共 **355224 B**，两条R561 include共 **62207 B**，以及本次完整caller差异 **32046 B**均不新增到Git；实际生成内容以完整来源计划、公开原文件和输出SHA可确定重生。这里没有丢掉任何科学输出字段来节省容量，也不移除科学输入或真实consumer依赖。容量整理由root独立按固定历史与实际引用执行，与本源的数学接受门分开。
