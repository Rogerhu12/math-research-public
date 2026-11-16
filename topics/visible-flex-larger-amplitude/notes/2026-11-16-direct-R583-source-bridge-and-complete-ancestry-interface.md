# R604：直接 R583 来源桥与完整祖先关系接口

作者：OpenAI / ChatGPT exact_refinement agent（AI）  
日期：2026-11-16  
可信度：已证明（限以下来源调用及 metadata 精确逆合同）；尚未在新的科学入口执行，未产生新的求解或性能证据。

## 1. 完成交付和未声称的内容

R604 提供一个可直接调用的标准库源组件。它调用未改 R583.prepare_sources 的真实六参数接口，写完整 job-local binding，并在明确 R584/R604→R593→R589 必要对象路径上恢复原 R588 表示，使 R600 可以处理同一完整对象的来源事实。原父层错误、退出码、complete、未知字段、完整报告和旧 marker 表示均可逆保留。

它没有改原 R583 算术、installer 或五代祖先；没有改 RootStats、原 H/native/J/FD/full-DN、任何科学阈值或原 owner12000/全局19200。最终 source/science 两个完整必要正文仍为原 90000 B/实际70。内部来源 bridge 的小 stdout 不是一个成功公共读回，不代替完整 binding。

actual244 只返回了联合来源 guard 的外层错误和 source 必要体溢出 descriptor，内部原因没有返全。[R585](../results/R585-actual244-source-binding-stop-and-complete-necessary-overflow.md) 给出这个证据边界。新组件消除一个原源码可证的内部整份 stdout 限额，并补两处确切旧逆；不宣称已查明或修掉该次未返回的子错误。

完整条件证明见 [R604](../results/R604-direct-six-plan-source-bridge-and-exact-ancestry-inverse.md)。后续正式 caller 暂协调为 R605/request252，实际结果 R609；本接口没有该请求/workflow，也没有启动或预填 run。

## 2. 文件和来源依赖

| 角色 | topic 内路径 | bytes | SHA256 |
|---|---|---:|---|
| 独立 helper | computations/root_20261116_R583_direct_source_bridge_and_complete_ancestry.py | 25170 | 95ed33dfce8d335a7a1881c8d0ab5f5bce07345707d2bddf38f14a8f5b4599e5 |
| 完整条件证明 | results/R604-direct-six-plan-source-bridge-and-exact-ancestry-inverse.md | 19134 | f2d1c08994f2ac7b33677a6970ebcda52f1375a3e4c71419ad9b55ada74accd9 |

固定直接依赖：

| basename | bytes | SHA256 |
|---|---:|---|
| root_20261116_loop_rounding_observation.py | 22648 | 0b769cc0558758ce2415c0374c3286bb8433d377286259821e9e588e5550635e |
| root_20261116_complete_six_layer_R583_source_relations.py | 17338 | 2a7c44446089d2136c096ffca73b8870a5b062f49f725515f5bafcb3fd40a77f |
| root_20261116_complete_named_source_and_root_statistics_relations.py | 19120 | 6f7cb8049e8b77b26964deb675e5868d6b374ac2e07c49b6517c8e51d7db0dad |

原 R583 source plan 为 notes/R583-loop-rounding-observation-complete-source-plan.json，24218 B / 9e1ac431926c76e0e77858695e2d1772e07eb58dcaba1211f2c9eca7328af0f1。原 header4657/0bc58、primal28149/dc8a、trace36388/37e5 和 compiler8626/5783 的完整身份仍从该原 plan 绑定，R604 不重新派生它们。原完整六代合同及 24 编译依赖同样由原 adapter 保持。

R583 已刊主线 7c16a9e89d8ec9d2630825f2bedbfd4f44fbd352；R600 已刊主线 bccee12b31fd069e6d66c5b077964f3b926295bb。R583 proof 后续对 R561 无额外模式读取的文字澄清没有改上述运行源身份。本组件依赖的是完整固定源字节，不依据最新标签猜版本。

## 3. 环境和两个独立 schema

新源必须置于实际 checkout 的 topics/visible-flex-larger-amplitude/computations，与三个固定模块同一 HERE。固定模块加载核普通非 symlink 文件、完整 bytes/SHA 和真实 __file__；不是把副本当旧模块的来源路径。

正向调用要求实际公开 repository Actions 环境，包含 GITHUB_REPOSITORY、GITHUB_RUN_ID、GITHUB_RUN_ATTEMPT、GITHUB_SHA；GITHUB_WORKSPACE 的真实 computations 必须等 HERE。它没有申请额外权限、启动外部 workflow 或建立新的 scientific clock。

两个新 schema 分别为：

| 对象 | schema |
|---|---|
| 来源桥 receipt | R604-direct-original-R583-six-argument-source-bridge-v1 |
| 完整旧逆+R600 metadata 关系报告 | R604-explicit-R593-R589-complete-source-relations-v1 |

原 binding 自身 schema **仍为** R583-loop-rounding-observation-source-binding-v1。新桥不会把原 binding 的 schema/source/run 改成自己的来源。新 bridge receipt 使用新 schema 和新实际 source，两个对象明确分开。

## 4. 函数 API：原六个计划参数

直接来源函数签名：

```text
prepare_to_binding(
    source_plan,
    synthesis_source_plan,
    product_source_plan,
    average_source_plan,
    reuse_source_plan,
    word_source_plan,
    binding_out
) -> (binding, code, bridge_receipt)
```

前六项分别是原 R583、R572、R564、R561、R550、R535 的真实完整 plan 文件。它们不是按名称替代原 bytes/SHA；真正核定仍由原 R583 的 read_plan、checked_plan_file、verify_complete_kernel 和各原祖先 producer 执行。六参数顺序不可交换。

binding_out 必须是本 job RUNNER_TEMP 内已存在 owned 子目录中的新鲜普通文件，不能覆写旧 binding。函数只在本次调用执行一次原 prepare_sources；所有祖先仍 source-only。成功时原完整 binding 原样 canonical 写文件，code0；原 prepare 异常沿原 CLI 格式保完整 error/partial_sources，code2。

原 partial_source_state 是它自己已存在的五参数接口，保其真实签名；这不改变六参数 prepare。桥另在原调用之后逐一记录六个 plan 的实际文件身份，观察不到则保完整 read_error。记录这些 metadata 不在原函数之前抢先终止，因此缺失 plan 的原错误和部分源账仍有机会由原 producer 返回。

桥不调用 install_owner_compiler，不编译，不生成新 native 状态，也不读科学 raw。成功返回只能支付来源准备；原 compiler_completed/scientific_evaluation_performed_by_preparation 均按原 binding 的实际值保留。

## 5. CLI 和文件回传

同一源另提供 CLI，参数完整为：

```sh
python -u "$COMP/root_20261116_R583_direct_source_bridge_and_complete_ancestry.py" \
  --source-plan "$ACTUAL_R583_PLAN" \
  --synthesis-source-plan "$ACTUAL_R572_PLAN" \
  --product-source-plan "$ACTUAL_R564_PLAN" \
  --average-source-plan "$ACTUAL_R561_PLAN" \
  --reuse-source-plan "$ACTUAL_R550_PLAN" \
  --word-source-plan "$ACTUAL_R535_PLAN" \
  --binding-out "$FRESH_SOURCE_DIRECTORY/source-binding.json" \
  --bridge-receipt-out "$FRESH_SOURCE_DIRECTORY/bridge-receipt.json"
```

变量是未来 caller 的真实参数记号，不是本接口已存在的运行文件。两个 output 必须在同一个新鲜 owned 临时目录；receipt 文件同样不得已存在。新 CLI 不传用户 token，也不派发任何 workflow。

成功或原 prepare 异常被捕获时，内部 stdout 的 event 为 R604_original_source_bridge_return，保 actual_exit、source_preparation_complete、actual_binding、actual_bridge_receipt、original_error，并明确 final_complete_necessary_scope_still_unpaid=true。遇桥自身来源/I/O/receipt 错误则 event 为 R604_source_bridge_unreturned，实际 exit2、完整 error 和 cleanup_permitted=false。

新内部 stdout 没有“完整 binding 必须<=90000”的单独 gate。**父进程必须实际读取 binding 文件并绑定全部字节**；不能只读上述事件就开始科学。完整 binding、桥 receipt、真实错误与 partial 源账仍进入最终 source 已选对象，按原完整正文限额处理。内部文件不得作为可再生科学/必要输出上传 Git 或另拆 transport body。

bridge_receipt 含实际源/run、固定原 adapter、original_callable、六参数名/实际参数文件或错误、完整 binding identity、actual_exit、原 prepare 是否返回和 compiler/science 状态。它注明：原 source 只调用一次、无 ancestor installer、无新钟、最终限额不改、244 内部错误未宣称修复。这些说明不能覆盖其中真实 error 或 complete=false。

## 6. 父 caller 必须保留的原 guard

旧 R584 guard 的每一项继续有效。父层只有在完整真实 source 返回满足原 exit0、原 BINDING_SCHEMA、当前 run、source_preparation_complete=true、compiler_completed=false、science=false、同 HERE、全部 actual_generated_sources、原 loop-mode 合同、每个 observed 全文件匹配之后，才形成其后十个当前来源视图。

新桥本身不代替这些条件。若原 R583 仍报某个 source/kernel/plan 错误，或实际 generated 文件有差异，父层仍保真实失败与未生成后缀。不能因为内部不再返回 stdout70，就将原 guard 改成只检查文件存在。

原 R583 installer 只由真实 owner 调一次；R572→R564→R561→R550→R535 只 source-only。R583 的真实 thread rounding mode 在各 loop 内恒定仍是其原等价条件；R604 不加强或放宽这个条件，也不改 product/average/kernel/RootStats 任何算术。

## 7. Metadata API 和适用根对象

关系函数为：

```text
complete_source_relation(value, source_hashes, computations)
    -> (selected_value, relation_report)

restore_complete_source(selected_value, relation_report)
    -> original_value

choose_complete_body(original_body, candidate_body, serialize)
    -> original_body_or_candidate_body
```

value 是 caller 已经形成的完整 source 必要选择对象，不是 descriptor、任意科学 JSON 或从旧日志猜出的树。source_hashes 和 computations 用于 R600 的原具名来源识别，必须来自当前已经绑定的完整来源；逆函数不靠它们或文件 SHA 获取缺失值。

允许根 schema 仅为：

- R584-loop-rounding-observation-complete-source-preparation-v1-necessary-v1；
- R604-direct-R583-original248-complete-source-preparation-v1-necessary-v1。

未知根 schema 不自动扩权。除两处明示地址外，原不适用的旧表示、未来 schema、错误和普通 literal 一律保持原值；如果它们含未知保留 marker，R600 按原规则不共享整体。不能靠删除未知 marker 来强行压缩。

API 正向固定加载原 R588 和 R600；inverse 使用固定 metadata 源的纯逆函数，不读取外部 source facts、科学数组或结果文件。需要 metadata 实现文件可用，不需要重启科学或运行原 source producer。

## 8. 两种旧 scope、bundle 与逆序

第一个范围只在完整链的以下精确地址：

```text
value.original_parent_complete_necessary.value
    -> schema R593-live128-extended-owner-budget-complete-source-preparation-v1-necessary-v1

value.original_parent_complete_necessary.value.original_parent_complete_necessary.value
    -> schema R589-complete-current-owner-named-necessary-source-preparation-v1-necessary-v1
```

R589 的 R588_complete_nested_relation 必须是原 schema/applied=true/report；原 R588_inverse_order 作为实际存在的 wrapper 一并保留。只从其整个已选对象暂取出这两个 wrapper，然后调用原 restore_relation。R593 自身仍是完整原对象，它的 original_parent_readback、original_parent_transport、exit70/completefalse 等不变。

第二个范围只适用于真正 R584 根的 current_source_record。使用它自己的 R588_current_source_relation 和 R588_current_source_inverse，不能拿父层的表解码当前表，也不能对新根猜出同名关系。

每个 bundle 的固定成员为 kind、container_path、selected_scope_path、original_container_key_order、wrapper_members、original_reference_slots、original_report_and_inverse_members_preserved。完整旧 reports/inverse 文本放 wrapper_members；原 markers 的 typed path 和原 [family,index] 放 original_reference_slots。它们只是旧已编码 source metadata 的实际引用地址，未编码普通科学数值。

正向先解原 R589 全范围，再解旧 R584 当前范围；随后对完整规范化对象调用 R600。逆过程先 R600 inverse，再逆序逐 bundle 恢复旧 marker 和 wrapper 键序，因此恢复的是包括原关系表示在内的同一已选 value。不是只恢复一个含义近似的新对象。

restore_container_order 要求原 keys 与普通剩余成员/完整 wrappers 的并集严格相同且无重复；叶 references 的位置必须真实、互不重叠。负零、整数/bool、null/缺键、列表顺序及未知值都由原精确对象保留，不做科学换算。

## 9. 新报告及错误处理

成功 relation_report schema 为 R604-explicit-R593-R589-complete-source-relations-v1，主要包含：

- applied、实际 source、original_R588_source、actual_R600_source；
- complete_R600_relation；
- complete_original_parent_relation_scopes；
- original_root_schema 与完整 inverse 说明；
- 原错误、返回码、complete、未知值均保、没有新 source/readback/science 重跑的范围声明。

applied=true 表示这份组合和逆已形成，不表示 R600 一定生成了共享行，也不表示节省字节或科学成功。R600 自身 applied=false 时，其完整原报告仍保。

如果任一旧逆或 R600 形成失败，返回原 value，报告 applied=false，保完整实际 error/type/message/traceback。不得把临时半解码对象作为正常结果。未来 caller 应在原 metadata 错误范围记录这个实际报告并保完整原对象；它不应因此增加一个科学接受门。记录新 metadata 错误发生在最终 body 大小决策前。

函数之外的 source/schema/固定模块错误同样由 caller 的原 metadata 错误处理保全；不得将真实错误变成空成功 relation。完整 reports 和 inverse 说明不能只留 SHA。

## 10. 全正文严格选择和原限额

caller 必须先形成完整原正文 O 和含全部 selected/report/inverse/error/status 的完整候选 C，再把相同原 serializer 交 choose_complete_body。它仅在 ser(C) 比 ser(O) 严格短时返回 C；相等或更长保 O。R600 本体实现这个条件，新函数只是委托。

不要只比较 selected_value 子树，或先比较再加 report；不能使用任意列名缩写、把科学树改成通用字典、分 body、截断错误或省略未访地址。完整 R604 bundle 的全部旧报告开销也必须计入。

之后两份最终 source/science necessary 仍各自执行原 whole-body 90000 B/实际70。超限时必须如实返回 descriptor、保正文未返/marker未付/cleanup未授权；不能将内部桥小 receipt 充作 source body。即使关系没有减少字节，完整原选择对象也照常受限。

本组件不预测容量收益，不把 actual244 的未知 487638 B 正文当测试样本，也没有运行旧摘要的 fixture。实际 sizeof 只在将来原 Actions 对真实已选对象计算。R588/R600 原八类 RootStats 以及全部17计数/last、unknown 数据均不删。

## 11. 时钟、所有权和后继入口分责

新 helper 不创建 deadline、namespace、科学子任务或新进程组；若以 CLI 形式被父 source child 调用，继续原父所有权和已有 wait/reap/quiet 责任。它只要求新鲜 job-local output，source 元数据完整和真正 quiet 分别记录。

后续若从 R594/request248 派生 R605/request252，差异应限于本直接桥、原明确旧逆和必要的真实来源级联。原63完整 prefix 与原78/91输入责任保留，不混 request242 的三参数初猜。owner12000、全局19200、replay1200、后继 stage8000/boundary/endpoint600/audit1800/readback120及所有原 cap/tolerance 由实际父合同保持，本组件没有重新分配。

新 caller 必须有自己的 request_number/source_namespace/policy、source generator/plan/full manifest 和真实执行路径。旧244仅为失败来源证据，旧248为实际完整源码/资源祖先；不能改冻结源或把新源冒成旧 head。source-only generation/原 restore/原科学的调用次数不由本 metadata 组件增加。

最终 source/science marker、完整 error/未访、真实 own PID/startticks/pgid/sid/后代与 unknown quiet 都沿原。缺 scope、source超限或静止未证时不得删除 raw。两个新的输出文件的存在不授权清理，也不表示 root/jets/J/audit/FD/full-DN 已经运行。

## 12. 本次可发表的结论

在本文明确的原函数和 schema 条件下，直接桥给父层完整实际 R583 binding，不再以内部整份 stdout90000 作为来源传递条件；它保原 prepare 的完整错误与部分来源，不动原 compiler/science。

在两个明确旧 scope 的原关系可逆条件下，新组合恢复同一个完整已选 source 对象，包括原旧 reports/markers/键序和所有失败状态。只有整份候选严格更短才使用，最终原90000/70不变。

是否减少未来实际正文、是否解决未来来源错误，以及完整 scientific chain 是否返回，只能由正式 caller 的真正运行记录给出。本组件没有该数值证据。
