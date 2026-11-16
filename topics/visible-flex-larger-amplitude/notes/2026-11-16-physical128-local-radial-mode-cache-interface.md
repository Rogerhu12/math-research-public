# R515：physical128 局部径向模式缓存的源码、编译接线与消费接口

作者：OpenAI ChatGPT。日期：2026-11-16。

**状态：源码与所列条件等价已证明；没有编译、科学运行或速度测量。本接口不修改正在运行的211/215/221/222，不创建请求或workflow。**

## 1. 本轮交付及精确身份

以下五件是拟登记的完整交付。manifest 只是临时交接清单，不计为题内产物。展开的组件源码及CPP仅供本次文本核对和未来Actions实际生成，不另存Git。

| 文件（topic相对） | 字节 | SHA-256 |
|---|---:|---|
| computations/geometry_20261116_native_physical_radial_mode_cache128.hpp | 5253 | 959d43bffc27665f30dffe4e98bb00fc007ee10fc3f3e519589c0c3d854fcd51 |
| computations/geometry_20261116_native128_physical_radial_cache_source.py | 13235 | 22e64c73005918527815269930f94ad4413bbc129120cb9dd5686a78a58873c6 |
| notes/r515-physical128-radial-mode-cache-source-plan.json | 8662 | 5950052fac0d9c23e96f29421c03df79f4748828b2d7a6e9a4ed7f40bd090666 |
| results/R515-physical128-local-radial-mode-word-sharing.md | 16739 | 93d225ae7423a21f2ccc7c51e52ee1531ca0db12df3c7b8891ce10562ccd649f |
| 本接口 | 以登记的完整字节/SHA为准 | 不把自身hash写入自身正文 |

完整数学范围、原词表达式、负零/次正规及非有限边界见[R515正文](../results/R515-physical128-local-radial-mode-word-sharing.md)。这不是对old physical程序增加一个新数值检查。

## 2. 实际被消除的重复

原[physical128头](../computations/geometry_20261115_native_physical128.hpp)为12683 B / `4b0569a245147e346149d462d974a80cac853bcf9d5abf13700b743acd33af35`。其 `physical_jets` 每个角内重复形成

```cpp
-p.frequency[j]*r3/(p.sq2*g.w)
    *(rhs[j]+(3*sigma-k)*state[j])
```

该表达式在同一个 field/state/geometry 调用中与角指标无关。新增函数第一次实际访问每个模式时仍在原位置形成它；只有形成词为finite才缓存。其余角下保留所有原 `dp*sn`、`frequency*dp*cs` 和原顺序累加。没有合并角点、重排求和、移动 $1/N$、使用三角恒等式或把 `pref*ell` 化简。

这与R471的零flux资格及R474/R494的dense零系数省略不同。本实现不依赖当前Q/Pi/L恰为零，对每个真实cut perturbation与audit query分别开新的缓存。跨调用的几何、state、RHS或root即使看起来相同，也不复用缓存。

## 3. C++ API 与原类型

新头文件真实包含原4b0569头；原头继续包含bcca737共享trace头及当前编译目录的完整R283前缀。新函数在原 `physical128` namespace 下，不冒同名替换：

```cpp
static Jets physical_jets_radial_mode_cache(
    const Problem&, const PhysicalPacket&, const V& state,
    const Cell&, const PhysicalGeometry&, const FieldTape&);

static CutReadout cut_readout_radial_mode_cache(
    const Problem&, const PhysicalPacket&, const V& node,
    const Policy&, BatchStats&, std::ostream& trace, int label);
```

原 `Jets` / `CutReadout` 类型、返回字段和所有数值输出完全沿用。没有新增counter字段或一个未经真实执行的命中数。若后续只拿到源码身份，不能将理论 $M(N-1)$ 复用数写成实际观测。

第一函数相对原完整数值正文仅新增两个本次私有容器及dp形成位置的有限词复用。第二函数相对原cut正文只改变名称与physical调用。保留 `right`、`Tdot`、`root_matrix`、`spd_solve`、全部C残差、七个角jet、曲率、height、holonomy、所有338行和两均值。

每个缓存先赋实际Q词再置ready。没有利用初始化零槽，保存-0不转+0，有限subnormal不截尾；非finite词不存且原表达式继续执行。新容器的分配失败、原时间异常均向原调用者传播，不重新运行一份旧科学程序。

## 4. 新 compiler-source adapter

新Python文件是实际可调用的source adapter，不是伪造的旧source label。它只用标准库，并保原Actions/实际仓库限制；数学或编译只在公开Actions发生。

### 4.1 保持的API

| API | 行为 |
|---|---|
| `copy_named_source(name, directory)` | 委托完整原R493 adapter，供原stage fallback来源使用 |
| `forward_lines(path, label)` | 委托原完整错误/日志行选择和原尺寸规则 |
| `prepare_compile(command)` | 对真实原physical编译命令生成R515实际新源；其他调用委托原adapter |
| `wrapped_base_process(original)` | 将实际新命令交同一个原进程/期限管理器一次；不捕获资源异常重试 |

原adapter是[geometry_20261116_native128_live_scalar_source.py](../computations/geometry_20261116_native128_live_scalar_source.py)，15897 B / `06a257765276863a487c1b2db6a13990c0dd6ec7dca4bc5422eda4af63d3bb2b`。它的module缓存按真实 `__file__` 和原schema核对；每次使用前仍核原源完整SHA，不以模块名代替来源。

### 4.2 生成次序和五个真实源对象

1. 原完整a090 CPP，18055 B / `a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415`，保持公开原字节。
2. 原49处JSON调用qualification，18202 B / `ecf14bf4d5cfd7a9f7796d0fa513822a05ca6cdc5a3ecc291859cff58a91b265`。
3. 原R493四处scalar-word导出，真实生成19958 B / `5f6b2d3c641befb6816c3e411ba00b7faf6eb3407b210f8b4c68b1c655746502`，basename `geometry_20261116_native_physical_live_scalar128.cpp`。它是实际生成的祖先，不是可从Git下载的公开文件。
4. 新R515有限词缓存头5253 B /959d43bf，另将原physical4b0569和shared bcca737完整复制到同一个实际compiler目录。
5. 新实际CPP `geometry_20261116_native_physical_live_scalar_mode_cache128.cpp`，20048 B / **c0364bcdb302c0909d31ae4737257891640eeb25c91b56c9f646006bc9f47ea8**。

第3步由原 `upstream.prepare_compile(original_command)` 真生成。第4–5步发生在原process管理器调用g++之前，不再次执行上游科学。完整源plan中的三个替换依次为include一次、原cut调用三次、audit physical调用一次；每项count与最终全文SHA均明确。真实旧source未覆写。

新CPP保留原base、plus、minus三个cut调用及audit全query调用；只把callee换成同类型新函数。forcing模式虽然使用同一编译产物，但没有调用physical缓存函数，其数学体原样。

### 4.3 编译路径和收据

编译目录仍是当前组件创建的独占RUNNER_TEMP子目录。新头及两个旧头以完整字节拷贝到此处，原生成 `native_frozen_trace128_prefix.inc` 已存在。新CPP就在同目录，引用新的实际头；不能在另一目录生成却仍宣称旧HERE。

命令与原请求只在一个translation-unit argv位置不同。原 `-O3 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math`、两个include路径、`-lquadmath`、输出executable和seconds保留。

实际binding文件：

```text
<component>/compile/physical-radial-mode-cache-source-binding.json
```

schema：

```text
R515-physical128-finite-radial-mode-cache-source-composition-v1
```

完整字段包括implementation、upstream_factory、prepared_ancestor_source、实际三份header拷贝、每项替换次数及before/after完整SHA、真正actual_executed_source/path/command、原command、原R283 prefix、缓存范围和未宣称的接受/速度范围。

原R493 factory会写自己的source收据。它嵌入新binding的 `upstream_prepared_but_not_compiled_binding`；字段 `upstream_receipt_execution_labels_are_preparation_ancestry_only=True` 明确旧嵌套收据中的“executed”用语不表示祖先CPP实际被编译。最终唯一g++调用使用新c0364bcd源。

进程结果实际新增key为

```text
live128_physical_radial_mode_cache_source_binding
```

并保真正actual_executed_command及original_requested_compile_command。非physical路径仍用原key。必要source事件前缀为 `LIVE128_RADIAL_MODE_CACHE_SOURCE `，事件只传绑定文件与实际源身份，不传展开源码或科学大表。

## 5. 完整组件 source view

原完整组件入口[geometry_20261116_live128_final_components.py](../computations/geometry_20261116_live128_final_components.py)为32027 B / `2369787d7454c4f3d0e9f91cbf4f82327f73046bc637c6180361bff877d0b866`。

source plan的 `component_layer` 从这份完整文本生成：

```text
geometry_20261116_live128_cached_radial_final_components.py
32429 B
0a7f47213789bc4779a6241b121f636d2356302b9f258fdf7a94b3dec4b02f8b
```

只有五项字面变更：说明、实际组件schema、qualifier basename、完整旧/新来源并集、明确physical源变化的scope字段。新schema为

```text
R515-live128-cached-radial-final-components-launch-v1
```

原OWN_PINS条目全部保留；原qualifier仍以明确旧basename加入，新qualifier与新头另加入。原base.PINS继续完整检查，不将新adapter的名字当成旧06a257身份。组件view必须生成在真实完整computations目录，并与实际HERE一致；完整closure来自已刊原组件，不把本文三个文件误当成全部runtime依赖。

完整四角色 `stages/boundary/endpoint/audit` 都通过该同一view调用；因此其原 `validate_prior` 的同schema/source/实际inputs/完整manifest核对仍成立。不能拿另一wrapper的旧stage摘要改标签塞入新boundary。

本轮提供此明确可生成、可调用的组件view，但不修改旧live owner的VIEW_PLAN、pipeline或已有请求。因此没有“R501当前已经用了cache”的声明。后继entry要接live owner时，需公开更新其实际component源码、schema和原必要consumer对应来源；这一步是尚待实际组合的工作，不是新增科学阈值。

## 6. 原完整CLI参数

新组件view接受原全部参数，名称与数学含义不变：

| 参数 | 原合同 |
|---|---|
| `--component` | stages / boundary / endpoint / audit |
| `--packet`、`--packet-binding`、`--owner-summary`、`--owner-source`、`--state` | 每件都要真实路径及各自 `--expected-…-sha256` |
| `--physical-packet`、`--physical-binding` | 对应物理角色的真实同状态包及各自expected SHA |
| `--original-source-root` | 原实际恢复完整源目录 |
| `--stage-output`、`--expected-stage-summary-sha256` | boundary的真实完整stage前件 |
| `--boundary-output`、`--expected-boundary-summary-sha256` | endpoint的真实完整boundary前件 |
| `--seconds` | 原本组件含绑定/编译的墙钟上限 |
| `--scientific-seconds-cap` | 原可选主C++上限，不改变总钟 |
| `--absolute-deadline-monotonic` | 原父同host绝对deadline，按原min裁剪 |
| `--threads` | 原1–4范围；未来完整入口仍须使用其原确定值 |
| `--first-stage 0 --stages 576` | 完整实际stage范围 |
| `--first-column 0 --columns 224` | 完整实际state列范围 |
| `--reference-columns` | 原明确可选诊断，默认none，不新增门 |
| `--retain-temporary-for-same-job` | 原同job真实消费者保留责任 |
| `--out` | 原fresh owned RUNNER_TEMP目录 |

可接受原 `--operator-components` 前缀。不给未存在的packet、state、秒数或run预填值。本文未触发这些命令。

boundary仍要求完整同状态stage数据，endpoint仍要求完整boundary；audit仍从真实各节点独立重放原query/advance，不能借endpoint完成代替。新source不改变原native/fullDN接受字段，也不将四complete合成为接受。

## 7. 必要读回、局部失败和清理

新adapter不直接删除文件、不建新session、不扩科学预算。编译与科学进程、PID/quiet/原deadline和cleanup全部由原管理器负责；不会在有限缓存不满足时另起一次科学，也不会吞下资源throw。

完整component摘要仍含原scientific_report、process、compile及source_receipts。新增sourcebinding位于实际compile.process的新key；全文留在原临时树，短事件只给完整身份。原局部owner-to-parent reply仍是bounded index，不冒公开完整必要读回。

当前主reader没有被本轮默改。将来实际entry的必要reader须至少明确选出新实际source identity与scope，或者明示只读了完整binding身份；不能保旧key列表后宣称新binding正文已返回。所有原科学必要值、错误、stage/query/advance/column未访地址保持原选择，不删减以给新metadata腾空间。单90KB及超限出口照原规则；本文不保证未来摘要尺寸、不分包、也不把原未返111829B摘要作为fixture。

物理查询中途失败时，新缓存不向读回提供一份虚假的完成统计。原endpoint的symmetric/analytic列进度、audit每query后未完advance、原极值partial标志继续由原程序返回。新增内存分配或运行时资源异常也照原真实错误报告。

临时生成CPP/组件view/源收据只在同job保留至原真实消费者与必要读回完成、owner静止之后清理。Git只保存本接口§1五件，不保存展开源、raw或日志。

## 8. 误差责任与可用性边界

该局部优化没有重新关联原角向求和，没有换__float128精度，没有减少576×224或226双均值，也没有把literal table换成理想三角函数。原C-based physical公式和其限制保留：不从Csolve推出 $C=F_e$，不从混合338×112响应推出全解析Jacobian，不从finite jet/audit推出准确连续几何。

有限缓存词复制保持原符号零/次正规。非finite词原式重算；对于NaN payload、浮点环境flag的外部次数观察和实际wall-clock分支，不作whole-run逐词承诺。原source中的数学判定没有使用被删除的重复形成次数。

源码层若完整访问且所有模式有限，可将同一原表达式的形成次数从MN改为M；这不是测得的hit计数，更不是速度倍数。原编译器可能已消除部分重复；本轮未测量也未假定其行为。

## 9. 后继真实整链的明确剩余接点

现有R501的owner VIEW_PLAN、call pipeline及其readback仍固定旧2369787d组件；本轮不把这部分称已更新。若后继完整入口选择R515，应：

- 保原owner/replay数学与原clock，只登记新的真实组件view及sourceadapter/header；
- 把新组件schema/source和完整四角色的实际prior receipts接入同一次H调用；
- 保原response assembly/最终原门，新增binding必要字段在原单summary范围内真实消费；
- 沿实际新compile/source信息报告partial/错误，而不把本条件证明当成运行成功。

这些是具体源码来源组合，不是fixture、独立审核或更强解析门；不需要重复证明原零j命题。是否得到速度收益、是否完成原native/fullDN、是否达到连续closed-surface目标，仍分别由未来完整运行及原数学责任负责。
