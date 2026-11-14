# W14 / release-LU / direct CSC：完整新入口的未执行源码

日期：2026-11-10。作者会话：db6f / coupled_prefix；文件沿用本轮 2026-11-09 前缀。

## 1. 当前状态和范围

本批新增元数据门、显式运行选择器、真实 M14 runner、纯准备器及关闭审计器。旧 release-LU/W14、原 Newton、SciPy、尾部源和研究数据保持原字节。环境仍不可用；本批没有 Python 导入、AST 执行、factory、安装、矩阵、SuperLU、线性求解、BVP、DN、RK 或新几何导出。

**本批不是一次实际纯准备的通过记录。** 目前没有这个新入口的 config、launch、候选 CP 或成功数据。准备器必须先读到真实完成的两项检查和 root 实际工具退出证据。静态独审、运行计划、本文和源账本均不能替代这些证据。

改动针对旧全局 COO 索引及 values 拼接的存储开销，不改变有限方程、材料 metric、边界条件、谱权、原非线性尾部、容差、最大节点数或外层算法。它不保证实际峰值、分解成功、收敛或 G5。旧资源失败和失联仍属于各自旧 run；本批不解释失联原因。

## 2. 五个新源和三份原版

下表路径相对本题 scripts/。每件都先核新路径不存在，再创建并固定 commit 完整回读；均小于 100 KB。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| db6f-prefix-direct-csc-entry-gates.py | 20547 | d110a15669612ae75207d98b46b8ee31c41d5f98dc8a9b693a06a4cbc399606b |
| db6f-prefix-select-direct-csc.py | 14009 | e1083f63e26a5a248c9e8911308ba515f3b57c0d914b4bb8aceb6b6dc0660a49 |
| db6f-prefix-spectral-true-m14-direct-csc.py | 24690 | b6fd772b5f44819186fc7e31af370ffa199bfa5c9b14a2722b36345bcf26cd24 |
| db6f-prefix-prepare-spectral-true-m14-direct-csc.py | 13103 | 2e843363c57aee7d96b3359fc0735604f9c0fdbafce8ad4adb2feb421d4f3116 |
| db6f-prefix-audit-spectral-true-m14-direct-csc.py | 31225 | b6222f3394c53eebd8409c922ed2e009de85b4bcdbfa5a6e8c8d57b2294967e0 |

固定 commit 依次为 a804d0121309ac33ed4f1c3ee88c0a7586d7a47b、9af49bff30bae6307ff15167f918e3b40e2406db、4682653bd3f69028709959d5667ffa47f0003204、d01c9ae6e672ca7ad04755ea087a3564177d1bb3、82ddbdffef930266a5aadb52bcbc24a513a01897。

后三件完整复制自以下已审原版后作显式变换，原件未动：

| 原文件 | 原 SHA256 |
|---|---|
| db6f-prefix-spectral-true-m14-release-lu.py | 2db1fe8b9171c3d9a7a4ac0d11311cff8daec1aa36bb8cd91130148903070ed0 |
| db6f-prefix-prepare-spectral-true-m14-release-lu.py | 2018226a193294d7791492ec44d595e19ae004079ae717eb5557db249a21949c |
| db6f-prefix-audit-spectral-true-m14-release-lu.py | ee0d6aeadc4cfbe25ef4788581cebf81d5a50cfdb77b9a47f83d9d6df3071989 |

完整前向替换账本为 notes/2026-11-09-db6f-prefix-spectral-true-m14-direct-csc-source-transforms.json，SHA256 1a3b90585de2cf352641e922b054413267a6906f6e061887a129dae3f7882e23，commit 9b7640066e07bb0935c6a9907332e08f0b9eac41。三组分别 22、12、9 项替换；V8 已从完整旧文本重放并得到新文本逐字相同。这不是 Python 或 AST 验证。

实际选择仅用 foundation v2：db6f-prefix-direct-csc-foundation-v2.py，SHA256 8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf。历史 v1 不参与。

## 3. 必须真实执行的前置检查

### 3.1 源码及整数布局

只能接受冻结 db6f-prefix-check-direct-csc-foundation.py，SHA256 e437630f9718a898b31d16b21a2616034b0984d17a6b05ac5913f6cc7ec509dd 的真实闭报告。它须有 schema=db6f-direct-canonical-csc-source-integer-check-v1、status=PASS_SOURCE_AND_INTEGER_LAYOUT_ONLY；checker、foundation、六个 SciPy 源的字节身份一致；完整 construct/prepare 文本与 AST 对照、三项/两项替换、恰一次中点原地更新通过；36 个尺寸组合完整，8 个非法尺寸和5个损坏布局被拒。

该脚本仍应声明 factory_called=false、matrix_calls=solver_calls=0、actual_sparse_byte_replay=not performed。不能把整数检查改名成数组检查。

### 3.2 原函数/v2 的小矩阵字节和别名副作用

只能接受冻结 db6f-prefix-test-direct-csc-bytes.py，SHA256 197da92ec9ca8768c1b5a876aeed2b5164056fa7e3a3b3d790cd9eb626ee5bbc 的真实报告。必须 stage=completed、status=PASS_SMALL_SYNTHETIC_CSC_BYTES_AND_ALIAS_EFFECTS、无 error、script_return_code=0，且：

- 15 个固定 spec 和原顺序逐项一致；原与新 construct 各尝试/完成15次。
- data/indices/indptr 的实际 dtype、shape、strides、全字节、stored/canonical、显式零及指定符号零均经该固定源检查。
- 两套独立可变输入、全部根与视图的最终副作用和只读 seed 完整；非零别名例确实改变中点与 D/E。
- SuperLU、线性求解、BVP/DN/RK 计数均为0；原函数绑定未变、未读研究数据、未批准完整入口。
- 原 oracle、foundation、六个 runtime 源、NumPy/SciPy 版本和 factory provenance 完整。

新门从已绑定测试源 specs() 的唯一 literal return 读取场景定义，不导入测试模块，不重构矩阵。报告只有小元数据和摘要，没有矩阵数据传输。

factory provenance 在比较前创建，里面的 actual_sparse_byte_replay=pending 必须保留。外层报告的真实成功与内部原 snapshot 分开核，不事后篡改 snapshot。

### 3.3 root 的真实工具退出合同

两个报告分别需一个 root 观察文件：

- status=observed-process-completed、observer=/root；
- actual_exit_code 是非 bool 的整数0，且 tool_receipt 为非空字符串；
- command 是实际 argv，Python 为实际解释器的绝对路径，解析到准备器使用的同一文件；检查脚本和显式 --foundation/--out 对应，整数检查另有 --scipy-source-root；
- files 完整绑定本报告、检查器、foundation 和六个源，逐项 path/bytes/SHA 与当前真实文件相同。

短检查不强求长会话 session_id；计划命令、程序自己的 requested code 或 child 摘要均不能替代实际工具退出。观察文件本身也入新 launch 的来源闭包。四份文档必须互异。额外闭文件允许被观察记录列出，但同样重哈希并绑定。

目前四份实际文档尚不存在，本批不能跳过这项前提。

## 4. 纯准备和原参数

新增 CLI 为：

~~~
--out-prefix NEW_STEM
--pure-check-report ACTUAL_PURE_REPORT
--pure-observed ROOT_PURE_TOOL_OBSERVATION
--byte-check-report ACTUAL_BYTE_REPORT
--byte-observed ROOT_BYTE_TOOL_OBSERVATION
~~~

可加 --check-current-gate：仅核真实前置证据，0文件写入、0 runner 导入、0 factory/安装/求解。缺证据返回 NOT_READY_ACTUAL_CSC_CHECKS_REQUIRED、退出2。该负门本轮也未实际运行。

正常纯准备先经过同一门，再导入 runner 定义/NumPy，读取原 M14/N512 97绑定参考 bundle、原真 CP 和它自己的 final true DN/J。它不构造候选、restart、flow、RHS、Newton 或任何 solver/factory，不假设 affine01 或 M15 已成功。

新闭包包含原来源、三个历史 release-LU 入口、五个新源、foundation/checker/byte-checker、四份实际报告/观察、六个 SciPy 源、方法/变换账本及原 LU/spectral 定义。实际数量由未来准备器计算，本文不预造计数。旧 Python 依赖扫描与 original coupled main 闭包继续保留。

tail config 仍只改变五个 I/O 键，所有非 I/O 字段 canonical typed 相同。保持 M14、角 quadrature512、depth12、p8*s32=256/raw、auditSteps32、floor默认.05、maxIterations36、shooting tol2e−9、默认初猜边界修正。prefix 保持 tol2e−9、bc_tol1e−8、physical_bc_tol2e−11、max_nodes6500、audit angular1024、Node heap1536、fixed/lagged/preserve-restart-mesh 与显式空 warmup。N512 不冒称径向加密。

新 launch schema 是 db6f-spectral-true-m14q512-direct-csc-v1，明确指向新 runner，并保存 csc_prerequisites 和 csc_selection_definitions。新源身份不能借旧 LU-only schema 冒充。

所有验证完成后才独占写新 config/launch/preparation 三个小文件。out-prefix 须为完全未用的本题 notes stem。

## 5. 显式运行选择

原 LU 选择仍先核 f6 install 后的原 Newton，再显式选已审 factor=None 生命周期版本，保留原 STATS、NumPy、SuperLU、merit、排序及步规则。新 CSC selector 不安装或替换 Newton。

原 main 的第一真实 DN/J 可以先按旧流程关闭；第一次真正 BVP 前，新 runner：

1. 核已选 release-LU 的真实运行身份。
2. 重读闭合 CSC 先决证据。
3. 以固定 _bvp.py 编译文本核 exported prepare_sys、construct_global_jac、compute_jac_indices、solve_bvp 的 code/globals/defaults/closure；不执行这些函数。
4. 核 W14 的 scipy_solve_bvp 仍指原 solve_bvp，其 scipy_bvp 是同一 backend。
5. 在新 loader 名字 db6f_direct_csc_selected_foundation_v2 下加载 verified foundation，调用 make_functions 做源/回调/CSC类方法绑定，不构造矩阵。
6. 与真实 byte-test factory snapshot 完整比对；只规范化两个新函数的 loader module label。其余源路径/大小/SHA、版本、qualname、文件、首行、code digest 和原 callbacks 不改。
7. **只赋值 backend.prepare_sys。** 新 prepare 闭包捕获新 construct；backend.construct_global_jac、compute_jac_indices、solve_bvp 继续是原函数。Newton 继续由另一已审选择器负责。

真实 test module 名字是 _db6f_direct_csc_small_byte_test；实际运行用新诚实名字。两个身份都留在报告中。只允许这一文本标签区别，不把运行函数伪称原函数。

prepare 的四个闭包项恰为 collocation_fun、construct_global_jac、estimate_bc_jac、estimate_fun_jac；construct 的四项恰为 csc_matrix、get_index_dtype、np、stacked_matmul。prepare 不保留旧 i_jac/j_jac。dimensions、column_segments、_assemble_csc 的函数对象/code也记录。

选择阶段发生异常时，只在当前 prepare 仍是本次函数时恢复原 prepare，然后重新抛错；不吞错、不改 Newton。新模块加载、factory 接受和来源验证都不表示数值成功。

## 6. 每轮与 finally

原 W14 callable 继续接物理回调，返回物理状态/PPoly，复算原物理 RMS/BC。内层 BC 是当时 affine DN 的物理坐标 BC；原恢复 tail 后的 candidate true DN/J 与 BC 才支付真实非线性门。

每轮保留 before_newton/after_newton、14个原 physical callback 来源和全部谱权记录，追加 before_csc/after_csc：

- selected prepare 确实在用；
- exported construct/indices/solve_bvp 仍原对象；
- Newton 对象与 code 没变；
- W14仍调用原 solve_bvp；
- 新函数 globals/defaults/完整closure不变；
- 原helper/CSC方法、新storage helper对象与code不变；
- 当前源与factory snapshot对应真实小测试。

原 main、8轮 outer、DN/J、BC 与 final seam均未改。原关闭检查成功才暂记 DIRECT_CSC_FINITE_M14_COUPLED_PROGRAM_SUCCESS。

finally恢复原 prepare并记录原→新→原；不撤销或改变已选 release-LU Newton。恢复失败会将程序置失败、请求非零退出，即使先前数值门已过。程序请求退出与root真正tool exit仍分开，缺实际观察最终审计拒绝。

## 7. 关闭审计的有限门

首包只审已闭 _tail_0001，不读活动trace，不要求整轮退出。仍核精确request、八源、真实residual<2e−9、616 Jac、17 jets、865×28及13×28 states与同g/config；只给 PASS_FIRST_ACTUAL_M14_DN_ONLY。

最终保留原门：

- root实际长会话session、tool_receipt、exit0，原reproduction/输出绑定；
- CP/summary真实success及一致性、全部固定材料字段；
- 43物理状态、14参数、13correction scales、完整有限quintic chunks/SHA/shape/端高；
- 物理RMS≤2e−9、每轮inner_success与true tail residual、最后实际BC≤1e−8、1至8轮；
- 最后真实seam的精确物理端高、后续真实Jac/audit请求、616/17/8维数、896 samples和原记录身份；
- 原W14返回物理坐标、物理RMS/BC、Newton/STATS及全部callback来源。

没有新增二jet数值阈值或worker自然退出门；原sourceFullD/samplemetric等不冒充连续整图metric。

新增审计仅负责真实CSC先决文档、显式来源、各轮前后身份、第一selection与首记录、最后恢复与末记录、原prepare确已恢复且Newton未变。runtime code digest按绑定源编译核对，不执行任何callback。新schema/status明示，不放宽旧审计器来接新身份。

## 8. 恢复后的接口次序（未运行）

路径需恢复后重核。PYTHON_ABS 是实际解释器绝对路径，SCIPY_SOURCE_ROOT 为包含 integrate/ 和 sparse/ 的已安装包目录；所有报告选全新路径。

~~~
"$PYTHON_ABS" topics/visible-flexible-closed-surface/scripts/db6f-prefix-check-direct-csc-foundation.py \
  --foundation topics/visible-flexible-closed-surface/scripts/db6f-prefix-direct-csc-foundation-v2.py \
  --scipy-source-root "$SCIPY_SOURCE_ROOT" --out "$ACTUAL_PURE_REPORT"

"$PYTHON_ABS" topics/visible-flexible-closed-surface/scripts/db6f-prefix-test-direct-csc-bytes.py \
  --foundation topics/visible-flexible-closed-surface/scripts/db6f-prefix-direct-csc-foundation-v2.py \
  --out "$ACTUAL_BYTE_REPORT"
~~~

root须真实观察两次自然退出，记录当前6源与报告。观察里的实际command应将脚本/选项路径解析为绝对路径；上述相对展示不自动满足观察合同。

独立全文审和实际两检查通过后：

~~~
"$PYTHON_ABS" topics/visible-flexible-closed-surface/scripts/db6f-prefix-prepare-spectral-true-m14-direct-csc.py \
  --out-prefix "$NEW_UNUSED_STEM" \
  --pure-check-report "$ACTUAL_PURE_REPORT" --pure-observed "$ROOT_PURE_OBSERVATION" \
  --byte-check-report "$ACTUAL_BYTE_REPORT" --byte-observed "$ROOT_BYTE_OBSERVATION" \
  --check-current-gate
~~~

去掉最后flag才纯准备三个新小文件，仍不启动候选。root审实际launch来源及资源/空间条件后持有真实runner会话。本批未改任何既有resource/space guard。

真实运行将是：

~~~
"$PYTHON_ABS" topics/visible-flexible-closed-surface/scripts/db6f-prefix-spectral-true-m14-direct-csc.py \
  --launch "$NEW_LAUNCH"
~~~

NEW_LAUNCH 是纯准备器实际产生的新 stem 加 -launch.json 的完整路径，必须从实际输出读取，不在本稿预造。首/最终审计走新auditor --mode first/final，final另需root实际 --observed-execution，均使用本次新launch。只检查缺文件门时用 --check-current-gate，且不得同时 --out。

## 9. 已核与待核

已核：五源创建/固定回读、完整旧文阅读、三入口全部文字变换的V8重放，及12个函数完整文本不变：equal、without_io、write_json、expected_config、expected_parser_argv、runtime_original_newton、runtime_newton、select_runtime_newton、runtime_callbacks、check_packet、polynomial_endpoint、check_newton_lifetime_record。

已收到小字节测试本身的完整静态独审（tail-review-direct-csc-byte-test.md，SHA256 f8c0f68ad9d5a0fc64a7b9962bad754dc8f5dfa315af81bd00bb6350d216cce4，commit e4a15f7f830690c13d947ae764c648d445327ec8）；它仍明确0实际矩阵，不代付真实两报告。root 后续实际 guard 应另外绑定该审稿和完整新入口独审，不能只据本准备器可写 launch 就视为审核已完。

尚待：本批完整独立源码审；真实Python/AST和负门；两项冻结实际前置检查；新factory/selection/restore协议；实际纯准备；原方程联解与整图连续认证。若未来任一失败，保留原报告并另版修订，不改本批成“已过”，不放宽g/tol/guard或原数学门。

本次仅源码生成还有两次未写文件的V8编写错误：账本for-of拼写、初稿shell花括号被JS模板解释；各自在创建相应文件前修正，不涉及算法或测试执行。

直接CSC的等价依据是已静态审foundation v2；有限小合成测试核具体实现/环境，不证明任意输入的一切逐位行为。没有采用或实现分块QR、改变SuperLU排序、改用近似方向，也没有承诺实际内存收益。
