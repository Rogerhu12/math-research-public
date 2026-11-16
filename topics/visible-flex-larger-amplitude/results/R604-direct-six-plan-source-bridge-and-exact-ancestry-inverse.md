# R604：原六实参直接来源桥与明确祖先关系的精确逆

作者：OpenAI / ChatGPT exact_refinement agent（AI）  
日期：2026-11-16  
可信度：已证明（限本文给出的来源函数、明确 metadata schema、原关系逆与完整正文选择条件）；没有执行新科学计算、编译、性能实验或数值对拍。

## 604.1 实际问题、已知证据与本结论不填补的部分

[R585](R585-actual244-source-binding-stop-and-complete-necessary-overflow.md) 记录了 actual244 在来源准备阶段的真实联合 guard 失败。该 guard 同时要求子进程 exit0、完整 R583 schema/run、source_preparation_complete=true、compiler_completed=false、未执行科学、同一 HERE、两个生成源完整身份、真实 loop-mode 合同和所有 observed source 匹配。其外层错误不能确定这些条件中的哪一项实际失败。

同次 source 必要对象实际尝试了 487638 B，超过原 90000 B 上限，因而只返回完整 overflow descriptor；内部 child 的具体错误/返回码和完整绑定正文没有返回。原源码证明 R583 CLI 在完整 binding 文件写出后，还有一个 90000 B stdout 分支，超限时返回 70；这证明一种真实来源传递阻碍存在，**不证明 actual244 就是这个分支**。本结论不把未返字段补成 exit70、exit2 或任一内部异常。

另一个可直接从实际 producer 证明的结构是：R584 必要对象嵌入完整 R593 必要对象；R593 再嵌入完整 R589 必要对象。R589 已可能用 R588 对整个选择对象作具名表示，R584 仅对自己的 current_source_record 作 R588 表示。R600 遇到已经存在的同名 marker 会保原对象不再共享，因此简单再包一层 R600 不能跨这两层旧关系共享当前完整来源事实。

R604 独立支付两个有限责任：

1. 以相同六个实际 plan 实参和同一 HERE 直接调用未改的 R583.prepare_sources，把其完整实际返回写入 job-local 文件；内部来源返回不再次要求整份 binding 能打印进 90000 B。
2. 只在明确 R584/R604 当前必要 schema 和已知 R593→R589 路径上解开两种原 R588 表示，保全部旧报告、旧 reference 地址及原键序，交 R600 共享同一个完整已选对象中的具名来源，再给出精确逆。

最终 source/science 两份必要正文的原 90000/70、原字段选择和所有科学门不变。第二项不保证一次结果能装入 90000 B，第一项不保证修掉 actual244 未返回的内部错误。完整实际 caller 另行登记；本组件没有构造新的 run 或接受结果。

## 604.2 独立源与固定依赖

新源为 computations/root_20261116_R583_direct_source_bridge_and_complete_ancestry.py，25170 B，SHA256 95ed33dfce8d335a7a1881c8d0ab5f5bce07345707d2bddf38f14a8f5b4599e5。

它只依赖三份已冻结 metadata/source 实现：

| 实现 | bytes | SHA256 | 本次作用 |
|---|---:|---|---|
| root_20261116_loop_rounding_observation.py | 22648 | 0b769cc0558758ce2415c0374c3286bb8433d377286259821e9e588e5550635e | 原 R583 source-only prepare_sources |
| root_20261116_complete_six_layer_R583_source_relations.py | 17338 | 2a7c44446089d2136c096ffca73b8870a5b062f49f725515f5bafcb3fd40a77f | R600 全六代具名来源关系和精确逆 |
| root_20261116_complete_named_source_and_root_statistics_relations.py | 19120 | 6f7cb8049e8b77b26964deb675e5868d6b374ac2e07c49b6517c8e51d7db0dad | 只调用旧 R588 restore_relation 解开其真实旧 scope |

原 R583 header、两个 C++ views、compiler function、六层 kernel/plan 和全部 24 编译依赖没有重新编辑。R600 和 R588 两个原文件也不改。新源用完整 bytes/SHA 加真实 __file__ 绑定固定模块，不把动态任意路径当实现。正式计算仍只在原公开 Actions 环境；作者本次只进行了源文本和纸面构造。

源组合依据见 [R583](R583-complete-inner-loop-rounding-observation-and-original-product-words.md)、[R600](R600-complete-six-layer-R583-source-relations-and-exact-inverse.md)；R588 的原具名表示只在这里声明的旧 scope 使用。R604 没有把旧统计和未知 JSON 变成新的任意词典编码。

## 604.3 原 prepare 的真实控制流

原函数的实参顺序是：

$P=(p_{583},p_{572},p_{564},p_{561},p_{550},p_{535}).$

实际参数名依次为 source_plan、synthesis_source_plan、product_source_plan、average_source_plan、reuse_source_plan、word_source_plan。R583 先读自身完整 plan，再按该 plan 内 ancestor_R572 的真实完整身份核五份祖先 plans、完整 kernel 和原固定 adapter。它调用 R572.prepare_sources，后者沿 R564→R561→R550→R535 只形成来源。这个阶段不调用任何祖先 compiler installer。

R583 随后用自己的两个原 literal views 形成或核对 primal/trace，记完整 original/generated source、patch count、kernel 原/派生身份、actual_loop_mode_source_contract 和 actual_R572_source_binding。原函数只有在完整来源条件付清时才返回 source_preparation_complete=true；compiler_completed=false 和 scientific_evaluation_performed_by_preparation=false 明确保留。

owner installer 是原另一个函数 install_owner_compiler。它要求实际 owner globals、完整六代 binding、同 run/HERE、全 plans/dependencies 和未安装其它代，再一次安装真正 compiler。prepare 的完成不是 installer 完成，更不是编译或数值求解。R604 没有调用 installer，因此不能据新桥回执抬高任何阶段完成状态。

原 CLI 的额外行为为：捕获原 prepare 异常，形成完整 error/partial_sources 对象；写 binding_out 后按其 bytes 是否超过 90000 决定打印完整行还是返回 overflow70。后一个条件只约束内部 stdout 传输，不能改变已经写出的完整 source binding 的数学含义。

## 604.4 直接桥的等价命题

**命题 1（同一实际 source-only 调用）。** 假设当前 Actions 的实际 GITHUB_WORKSPACE/topic/computations 等于新源及原 adapter 的 HERE，三固定依赖与六个实际参数均按真实来源绑定。新桥在新鲜 owned 临时目录中调用 prepare_to_binding(P,binding_out)。若原 R583.prepare_sources(P) 正常返回 $B$，则新桥完整文件中写入的对象正是 $B$，采用与原 R583 CLI 相同的 canonical JSON 序列化；它没有挑选、补值、重标或删除 $B$ 的成员。

**证明。** 新桥固定加载原完整 adapter，核其实际 HERE 和 BINDING_SCHEMA。把六个参数转成 Path 后，以原顺序执行唯一一条 original.prepare_sources(*arguments)。它没有执行其它 source producer、compiler installer 或科学函数。正常返回后直接 canonical(binding) 写入新鲜文件。canonical 使用原同一 sort_keys、ensure_ascii、separator、allow_nan=False 和末换行，因此同一个 $B$ 得到同样文件字节。桥的来源/参数 receipt 是另一个对象，未插入原 $B$。证毕。

这里的“唯一一次”指本桥代替原 R584 那一次 R583 来源子调用；不宣称整份原父链从未先前形成过祖先源。原父准备和原祖先函数本身的调用次数由未来完整 caller 保持，不能用此措辞省略它们。

若原 prepare 抛出 Exception，新桥沿原 CLI 相同构造保其实际 type、完整 message、当前真实 traceback，schema/run/HERE/adapter 与 compiler/science=false，调用原 partial_source_state 五参数接口保存原可读部分。该 partial 接口本来只有自身及四份上游 plan 参数；不能擅自把六参数 prepare 的 word 参数塞入另一个不存在的签名。新 traceback 是本次新调用的真实堆栈，不声称与旧 CLI 或旧 run 的 traceback 字符串逐字相同。

六个参数的额外 identity 观察安排在原函数返回或异常捕获之后。某个 plan 此时缺失/不可读，其完整 read_error 写入桥 receipt，不能在原函数之前抢先抛错而丢掉原 prepare 的 error/partial binding。写文件、创建 receipt 或最外层绑定失败时，新桥输出真实 bridge_unreturned 错误，明确未完整返回、不能授权 cleanup；不以空文件或预制成功对象代替。

## 604.5 内部传递和最终必要范围

完整 binding 文件只留当前 job 的临时 owned source 目录。另一个新鲜文件保存桥 receipt，含当前 run、实际桥源、原 adapter、原 callable、六实参/其实际 identity 或错误、binding 身份及真实 code。正常 code0 表示原 prepare 返回；原 prepare 异常为 code2。普通文件/来源错误仍是实际错误，不改为成功。

内部 stdout 只发送这次返回的真实 receipt 身份、binding 身份、实际 exit、原 error 和“最终完整必要范围仍未付”标记。它不是公共必要正文，不用这个小对象替代完整 binding。源交接可以使用 prepare_to_binding 的函数返回，或新 CLI 文件；无论哪种，真正的父 caller 必须读完整 binding，并继续原联合 guard。

本组件删除的是内部整份 source stdout 的 90000 门；没有提高最终 source/science 的 90000 上限。原完整绑定仍要进入最终已选 source 必要对象，由明确关系完整表示或实际溢出70。文件身份本身不能作为“完整正文已经返回”的证据。它也不能转存到 Git、detached 科学对象、分包或从 SHA 恢复旧 raw。

新桥没有建立 science deadline、没有 sleep/retry、没有新 budget、没有调整 owner12000 或全局19200。后续 caller 若以 R594/248 为父，仍使用其原63输入、原 owner12000、原19200全局钟和所有后继 cap/门。R604 的两个作用点属于来源和必要 metadata，不是一次新的 native 算术变体。

## 604.6 两个真实旧 scope 的精确定义

令 $D$ 为 caller 已完整选出的当前 source 必要对象；允许的根 schema 只有：

- R584-loop-rounding-observation-complete-source-preparation-v1-necessary-v1；
- R604-direct-R583-original248-complete-source-preparation-v1-necessary-v1。

它们不是任意 future schema 的通配符。当前公开组件尚未声明另一个 caller schema；后续入口须显式采用本合同或独立登记新的精确映射。

定义地址

$p=(\text{original_parent_complete_necessary},\text{value}),$

$q=p\,\Vert\,p.$

只有 $D[p]$ 的 schema 等于原 R593 necessary、$D[q]$ 等于原 R589 necessary，且 $D[q]$ 内 R588_complete_nested_relation 是真正 applied=true 的原 R588 报告时，才对该整个 R589 已选对象解码。原 R593 schema 为 R593-live128-extended-owner-budget-complete-source-preparation-v1-necessary-v1；原 R589 schema 为 R589-complete-current-owner-named-necessary-source-preparation-v1-necessary-v1。

该报告及 R588_inverse_order 两个实际存在的 wrapper 成员暂移到 bundle；对象其余成员全部交原 R588.restore_relation。若 wrapper 缺键，就按缺键保存，不把缺键变成 null。

另一条仅适用于真正旧 R584 根：它在 current_source_record 上有 applied=true 的 R588_current_source_relation。只解开该 current_source_record，保 R588_current_source_relation 与 R588_current_source_inverse 全文、原根键序。新 R604 根不冒用旧 R584 当前范围。

每个 eligible 报告还必须具有原关系 schema R588-complete-named-source-and-root-statistics-relations-v1、原 marker R588_named_metadata_row、原合法 family tables。未匹配路径/schema/report 的值保持原样。它可能导致 R600 按原规则保整个对象 literal；这是一种诚实的不适用，不是丢字段的理由。

## 604.7 保存原表示的 bundle

旧关系解码会恢复数值对象，但精确还原要求恢复的是**原选择对象，包括它原先使用的关系表示和所有报告**。因此每个旧 scope 保存：

1. 唯一具名 kind、固定 container_path 和 selected_scope_path。
2. 原 container 的完整键顺序。
3. 两个实际存在的完整 wrapper 成员及其全部值；旧 complete、exit、errors、unknown、计数和 inverse 说明都在其中。
4. 旧 selected scope 里已经存在的每个原 marker 的完整 typed 路径及原 [family,index]。

第 4 项不收集普通科学值，不把相同字符串做通用字典。它只记录原 R588 已经创建的叶 reference：字典必须恰好只有 R588_named_metadata_row，family 属原已声明集合，index 为非负整数；路径元素分别保持字符串成员名或整数列表下标。bool 不当整数下标使用。

原 marker 是叶，它们地址互不为严格前缀；记录按原列表/字典遍历顺序生成。所有普通非 marker 成员留在解码后的完整对象中，未进入额外编码表。两种 bundle 的 scope 地址固定，不能据任意 schema 递归寻找可压缩的树。

bundle 保留旧完整报告是实质要求：不能只保存旧报告 SHA，不能把旧 exit70 改成新的 source complete，也不能用解码后的成功来源事实遮住原运输失败。新关系只重组表示，不改这些事实。

## 604.8 正向表示与精确逆定理

记 $N$ 为依上述两个固定 scope 解码的过程，输出规范化完整对象 $\widetilde D$ 和有序 bundles $B$。顺序为先原 R589 全 scope，再旧 R584 当前 scope。若某 scope 不适用，就不产生其 bundle。

对 $\widetilde D$ 调用未改的 R600.source_necessary_relation，得到 $(S,T)$。这里 $T$ 的所有具名表只共享当前完整对象内确切相等的已声明来源事实；原 R583 loop-mode 合同、kernel 原/派生身份、五祖先、24 编译依赖和未知/错误仍完整保留。R604 不扩展 R600 的 families，也不改八类 RootStats 算法。

新报告 $Q$ 完整携带 $T$、$B$、原根 schema、实际新源和两个原 metadata helper 身份、限定 scope 与 inverse 说明。正向 API 返回 $(S,Q)$，完整 caller 必须把 $Q$ 纳入同一个必要正文比较。

**定理 2（完整原已选对象可逆）。** 对上述实际输入 $D$，若旧关系及 R600 的原 inverse 成功，并且新关系生成没有异常，则

$\operatorname{restore\_complete\_source}(S,Q)=D$

在全部 JSON 类型、数值及字符串、列表次序、字典键存在/键序、null、负零、旧报告与旧 reference 表示意义下精确成立。

**证明。** 原 R600 已证明其具名关系逆，故先 restore_relation(S,T) 得到 $\widetilde D$。随后按 bundles 的逆序恢复。对旧 R584 current scope，用记录的每个叶路径把解码值替换为原 [family,index] marker；所有非 marker 位置未动。再把完整 wrapper 成员按原根键序插回。对旧 R589 全 scope 同理，先恢复原叶 markers，再把原报告/inverse 成员按原 container 键序插回原固定地址 $q$。

每个叶原先是一个 reference；旧 R588 inverse 所展开的整段只在该叶下，所以在同一地址放回原 reference 完全逆转该展开。叶地址不重叠，恢复不会抹掉另一个叶；非叶列表位置与所有普通成员保持。原键列表与剩余成员/完整 wrapper 的并集恰好等于原 keys，restore_container_order 拒绝重复或缺项。因此每个 bundle 精确逆转其一次正向操作。逆序同时消除两 scope 的嵌套顺序影响，最后仍为原根 schema。证毕。

若 R600 因剩余未知旧 marker 返回 applied=false，原 R600 inverse 是恒等；定理仍成立，但未产生新的共享。R604 外层 applied=true 仅表示所声明的组合与逆已形成，不表示 R600 省下字节，更不表示数值成功。

原 R588/R600 精确相等的类型敏感比较继续区分整数和 bool、不同浮点字值/负零、缺键和 null；遇不能适用的值保 literal。R604 的 bundle 使用 deepcopy 保存原值，不重新求数或做浮点换算。最终 JSON 序列化遵守原 caller 的既有非有限显示策略；本组件没有创造科学 nonfinite 替代物。

## 604.9 失败、未知 scope 与完整正文选择

若旧解码或 R600 调用发生实际异常，函数丢弃整个临时规范化副本，返回原完整 $D$ 和 applied=false 的完整 metadata 错误报告。它不把半解码对象作为正常结果。caller 若实际尝试该关系，必须记录真实失败报告并保原完整对象，不得以表示失败为新科学拒绝门。

成功时 caller 构成含全部 $S,Q$ 的完整候选正文 $C$，与同一已选 scope 的完整原正文 $O$ 用原 serializer 比较。选择规则唯一为

$O_{\mathrm{selected}}=\begin{cases}C,&|\operatorname{ser}(C)|<|\operatorname{ser}(O)|,\\O,&\text{其余情形}.\end{cases}$

比较计入新报告、完整旧 wrapper、所有 marker 地址和 inverse 说明；不能只比较某个子树或扣除报告开销。新 helper 的 choose_complete_body 直接委托未改的 R600 规则，不在比较后再添未计入的字段。实际 caller 的错误/status 等完整字段应在比较前已形成。

选定后仍应用原 whole-body 90000 限额；超限仍实际70，完整 scope 未返回，不写成功 marker，不授权 cleanup。相等大小不选新表示。没有任何输入无关的“必小于90000”结论，更不能据 actual244 487638 的未知正文推算压缩比例。

本定理只保证表示语义，未保证最优容量；完整旧报告和未知字段有多少字节必须由将来真实对象决定。源生成次数、旧父 readback 返回码、旧 complete=false、已返回/未返回后缀和全部真实错误都留在同一对象中。没有按 source SHA 重建缺失内容，也没有重新读取旧科学 raw。

## 604.10 后续完整 caller 的必要接点

R604 源可被实际调用，但尚无新 request/workflow 在本结论中运行。后续 R605/request252 若采用它，最小真实接线是：

1. 仍先执行原 R594/248 完整祖先来源，保持原63输入、owner12000/全局19200、原全部数学组件及所有门。
2. 把原那一次 R583 CLI 来源子调用替换为本桥，传完全相同六实参、同 HERE 和新鲜 job-local binding/receipt 路径。父读取完整 binding，保原联合 guard 全项，新增桥 receipt 全量进入已选 source 对象。
3. 原 R583 compiler 只在实际 owner 处一次安装；五祖先仍 source-only。不得为新桥重复编译或调用科学。
4. 最终 source reader 先形成完整原选择对象，实际调用本组件的两处明确旧逆+R600；science reader 仍保持其完整范围、RootStats 和 90000/70，若注册 R600 新六代来源关系须明确真实来源。
5. 所有新源的 source_namespace/request/policy/生成 basename 与实际 SHA 独立；旧244/248仅作真实祖先，不在其冻结文件上打补丁。
6. 必要错误、unknown own、quiet、清理门和原钟完整保留。内部 source 输出变短不准被解释成最终公共必要 scope 已经支付。

这是一条具体的来源传递和可逆 metadata 责任，不是为修复未见异常而改原数学。R583 的常量模式条件、全部原有限乘积/求和次序、原 root/jets/J/审计、原 FD/full-DN 和阈值都由原实际组件承担；R604 没有为它们添加替代证明或通过条件。
