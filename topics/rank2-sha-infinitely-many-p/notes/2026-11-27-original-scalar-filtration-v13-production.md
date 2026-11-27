# v13 原完整 shadow 接入核对

本稿只记录源码接入与实现门。本提交已请求 v13；实际 run 与终态待消费。三个独立软件检查的 PASS 不代替原四交、一般 Norm 或完整 $18\times9$ 终门。

## 1. 三个真实软件 PASS

| 部件 | 源码 SHA-256 | 实际回执 |
|---|---|---|
| captured complete return | 23f862035b668478bfafebdf95cf4d7f600d251243c3e47791fd4fec47c2c5bd | run 46076504365 / job 140765352826 |
| current idempotent square | 4c01f72b41e503be862045c7b9e1b63b3a457c7c63282ee3bf5df9d0d7d2a410 | run 46077929103 / job 140769938354 |
| scalar base support | c84656c73bb062958c233de20fbed4fb889779985d154058548305e02d73e39a | run 46079484704 / job 140774878749 |

第三项最终源码含 Sage 矩阵所需的 `copy(idempotents)`；checker 同样用 `copy(t**2*I)`。最终 payload SHA-256 为 `12109417a54201bac6a700c0795f2bd18b56577d26e458fc38452608cc96a16d`。7 个完整案例比较原通用厚分解的全部 ambient / constant 坐标、完整 maximal HNF、非约化长度和同点身份，并实际通过非 scalar HNF 与重叠 infinity-chart 两个拒绝门。

R1050 已给 scalar 理论。本 helper 不返回或冒充通用 thick local ideal。

## 2. 从真实 v12 得到的导入时序

原 v12 source SHA-256 为 `2e2fbe9cbd3213ac02a78c018ccfe857a3bd3296893230dc276166a5f8943ee9`。

1. `quadratic.prepare_backend()`。
2. 载入原 native producer，调用 `prepare_source_bindings()`：native PREPARED 行函数编译完成，原 projector module 已载入；projector main、linear main、triangular 导入均未发生。
3. 准备 projector main 的最小文本副本，仍以原 projector module 字典为 globals。
4. `quadratic.bind_original_returns()`；随后 `bind_prepared_native_return()` 修第 2 步捕获的旧 return alias。
5. 绑定 current-square；绑定 scalar geometry。
6. native main 复用 PREPARED，然后调用 projector main；projector 此时才载入 linear。
7. 原 emit hook 绑定 native row solver；linear main 此时才载入 triangular，故后者的 geometry from-import 精确取得第 5 步函数。
8. triangular 的原两处 geometry 绑定及全部原 producer / 数学终门依次实际执行。

原 projector decomposer 动态调用 `closed._lift_idempotent(...)`，没有裸函数捕获问题。新入口只核其 `closed` 是 current-square 使用的同一 module，不额外改不存在的捕获点。

## 3. projector 副本恰改实现使用门与对应回执

原文件、通用 API、`complete_original_primary` 的全部 full-local / maximal / return / idempotent / length 检查不改。运行时取完整 main，六处单次替换：副本函数名、records 使用断言、最终输出 tag、最终 status、新增实际使用回执字段，以及绑定回执明确写“原数学门”而非未修改的实现计数断言。

六项逆序恢复后必须逐字等于原函数，原文件 / 原函数 / 生成函数 hash 全输出。新函数以原 module 字典构造，故 global ENTRY、emit 与 native hook 闭包保持同一对象，不复制隔离的 ENTRY 状态。

实际门为：有本次非空 generic projector 返回，或有本次完整 scalar-filtration 返回。当前 v13 固定绑定 scalar geometry，因此八条 scalar 回执必须全部核过，即使另有 generic 使用也不跳过。`complete_original_primary_records` 原列表保留，允许真实为空，绝不添加假项。

最终 tag 为 `RANK2_COMPLETE_PROJECTOR_OR_SCALAR_SUPPORT_COMPLETE`；status 明记 `all_original_gates_completed_with_complete_projector_or_scalar_filtration`。

## 4. 八条回执连到本次实际来源

使用门读取 `linear_entry.ORIGINAL_LINEAR_FIBER_COMPLETE_CONTEXT`，并与原 triangular / original producer 返回 context 核对象 identity。geometry 的 six、四交 geometry、engines、registry 也逐一同一对象。

按原次序读 T 与 v 的 2×4 条 `actual_whole_boundary_divisors`。每组从 `cache[id(function)]` 取原 divisor，断言其 function 就是原 T / v 对象。每条 record 连回对应 finite / infinity chart 的 actual ideal；infinity 使用原先已算的 actual boundary ideal。

逐条检查 input HNF、target HNF、determinant hash 与 actual 对象一致；complete length / degree 等于 target.length；全部 primary 与 component 长度和返回 target。每个非约化 fiber 的 $d_i$ 和为 $306$，$f_i$ 整除 $d_i$，scalar thickness $m$ 对应 norm exponent $306m$；$\mathrm{multiplicity}=md_i/f_i$，乘原点 degree 后等于完整 local $k$-length。原 Frobenius、完整 idempotents、常数嵌入和 maximal-ideal 身份保留。

回执明确 `thick_local_hermite_ideals_materialized=False`、`general_thick_local_ideal_interface_claimed=False`、`local_fraction_values_or_elliptic_trace_claimed=False`。不填原 projector PASS 字段。

## 5. 原数学输入与终门

新入口仍调用同一 native → projector → linear → triangular → original pipeline。原 triangular 与 consumer 文件不改。

参数仍 `p=29`、`q_precision=2453`、`batch_size=64`、`kernel_method=minimal`、`phase=shadow`、`trace_method=artinian`、`run_api_preflight=false`。两真实 char0 PASS 的 host 认证逐项保留：

- first run 43906594646 / job 133436977753 / source 135b50ff04a12c51dd1b9de583a20b2bed19cbed / result 5193c929a0369e957a0495f12c5af244243f2b4ed444ba305bba963dfdc4831f。
- packet run 44714703201 / job 136215000168 / source b688d6ac703fec422a7c864bcdc997cc553185fd / result d3371b55fbdbf8999f2ed6da76cc004a78eba733ff5e7977bce4149e4ecb8915。

原两 chart、完整 normalization/M2/equation/W transport、四个完整 intersection、一般 Artinian Norm、全部 18×9 字与九对、原方程、全部厚长度、真实常数域和嵌入，以及 `all_requested_original_acceptance_gates_completed` 终门全保。

## 6. 源码与 host

旧 60 个 code hash 直接来自 v12 run 46033409751 的实际 host manifest；另固定三 helper 与新 launcher/producer，共 65 个源码。host 逐个核 request 中固定 hash，并核实际 workflow hash。README 仍按当前实际 commit 记入 manifest。

request 除 schema/实现名与新增 source/workflow pins 外，其余旧数学字段逐项相同。launcher 保原 Sage image、read-only mount、offline 数学进程、双 PASS reader、token 隔离、21000 秒上限及失败清理。workflow 只改展示名、增加新路径、换 launcher；权限、concurrency、image、timeout 均保留。

静态逆向核对：producer 外层 17 处可精确反转到 v12；内部 projector main 6 处运行时反转；launcher 10 处；workflow 3 处。两 Python 源仅已做字符串/括号词法核对，不冒称 Python AST 或生产已 PASS。

## 7. 耗时证据及范围

v12 在 21000 秒真实超时，未取得数学终端 PASS。24 个 cusp component 从完整 maximal 返回到 thick projector 完成的区间合计约 10082.829 秒。scalar 支持省去这类 thick local projector 构造，仍保原全非约化 fiber、完整 maximal 与厚长度证明。

current-square 先前约 750.508 秒重复乘法处于这些区间内，不能把二者重复相加成预计收益。后续四交与一般 Norm 实际耗时尚未知，本稿不保证 v13 六小时内完成。

本提交写入已逐项审阅的源码与固定请求，并修改原同一个 workflow 的 launcher。数学输入和4CPU/16GB限制保持，运行不保存或加载矩阵/数学缓存文件。root 统一消费实际 run；所有几何终门未获回执前均保持未完成。

## 8. 本次发布的确切源码

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| scripts/produce-original-scalar-filtration-shadow.py | 17182 | d2e2ba156cee83234d8cc04efc6f3a6d73fe78f260334bfd8c5b6f298f871daa |
| scripts/launch-original-scalar-filtration-shadow.py | 12738 | ac761d0721a7fc0897d812b0f0228f386ab3122b496ec866eb46e0952dd0a66b |
| ci/original-scalar-filtration-shadow-request.json | 8304 | 56cad619305dcde9709667486e870f64a2f29c1f4dde904876ad02f39ee4abe2 |
| .github/workflows/rank2-sha-original-triangular-artinian-shadow.yml | 3736 | a9ff7ae63c0f7a452afc44648b5f4d8e95a195224f34b55b17cc3bc5a946d15b |

root 已逐字读四文件，比较实际 v12 host 的全部60旧pin，确认恰加上述新launcher/producer和三helper；新request的65项与源码一致。软件执行和首次生产的回执按实际读取后追加，发布本身不充作通过。

## 9. 首次实际启动

公开 run [46080875647](https://github.com/Rogerhu12/math-research-public/actions/runs/46080875647) / job140779301767，source277c55dd2c0d36baf665c65700935ac671faa816，创建于2026-11-27 23:09:29UTC。已核实际job完成checkout及固定镜像拉取，并在认证原回执/完整计算步骤执行。首次读取进行中job日志返回BlobNotFound，未据此声称源码绑定或数学终门通过；以后消费实际完整输出。
