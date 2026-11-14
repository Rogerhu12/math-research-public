# 新78718存储完整来源适配与实际读取检查

状态：新来源已经生成并完成以下限定执行；**完整未参与者独审未完成，production_ready=false**。
本稿不是缺失旧A/B源的恢复，不改旧求解器、旧原单文件来源或任何曲面参数。

## 1. 第一次真实失败及另名修复

原builder-v1完整保留，SHA4c574c493f53f0e90ba3d6db98b64a61a930d9d34a6c9faa7a7df092425f52e8。
root实际47de38自然exit1：continuous reader原本没有HERE与importlib.util，
初版统一载入插入假设不成立。失败发生在全部文件写出以前，0adapter、0ledger、0solver；
完整记录见storage-builder-first-failure.json（本目录同日期会话前缀）。
另名scripts/78718-build-storage-adapters-v2.py只为该已钉原源补显式stdlib载入/path，
v1不改。v2 SHA17c63f1c0c2066b42c1f5e9e113e679247b30b317ac103d63176a50bc3233500。

## 2. 纯来源生成与冻结身份

root实际4e50df/session86481 → 280654自然exit0，生成14份新适配及2份原样core，
134处逐步唯一文本替换、188个函数AST完全相同；不调用数学backend/solver。
源码账本2026-11-10-78718-storage-adapters-source-ledger-02.json为60660 B，
SHA375e716789ef206deecbb62207d8e1c70d9995bfb303f27f0b1c250c174e8634。
每个剩余变更函数的完整old/new替换片段全部在该账本，不能靠AST计数替代语义审查。
生成地点为/tmp/78718-storage-adapters-scratch-02；root实际d25a08逐字核后把14个
新来源复制到本题scripts，所有最终全文与生成账本SHA相同。原来源没有改。

|新文件|字节|SHA256|须审的变更函数|
|---|---:|---|---|
|78718-prefix-fullxyz-hermite-storage-v1.py|15820|2ab813fba7d3a33ef273799a4f6d27628b9cc2f98285fb3d3371fdacb49b009d|SharedHermite.__init__, build|
|78718-prefix-mirror-hermite-storage-v1.py|5138|f975ab40ca05f5237954398533934eda2365ceda38cb0ba4dfe8d9e3287f6957|build|
|78718-prefix-continuous-hermite-storage-v1.py|15784|09e8c748c7cc49347876d849029e835a8cd0e5f097d36eaf6cf2fd7c0f2ddc18|ExactHermite.__init__, certify|
|78718-prefix-metric-polynomial-storage-v1.py|11134|d290543f75224509fef8287db838265540a74b7caec38d7b9f34cea563d8359e|run|
|78718-prefix-metric-supplier-storage-v1.py|17622|f2d8e79504a2a3895ec8705457eabe46321e80b68b8e7c7de11f13015d160ff3|main|
|78718-prefix-volume-moment-storage-v1.py|4138|16f493774c7176566dda1f08e494b2af74d2f6e04b970b43c802838b08a5f654|integrate|
|78718-prefix-common-cut-storage-v1.py|13714|34b0b92c6f4d92bd497f3d84d28cbd73cb29271e36b240d3a19795987f057d43|install, install.CommonCutPrefix.__init__, main, make|
|78718-prefix-angular-arithmetic-storage-v1.py|23047|3ade215b643345920eafe9a1e3c7ce477ed6e46913e47bf712f309d800636ece|run|
|78718-prefix-metric-budget-storage-v1.py|9635|656e11ca0226ca1647a968c76afb4566b076ba0e9b4c0836bf263cf097ced091|load_uncorrected_region, main|
|78718-prefix-closed-budget-storage-v1.py|24683|375261a22c8465c9ce318624818493590b1ceee4eb28ce9cd3c1c253a9f8f150|main|
|78718-prefix-angular-metric-storage-v1.py|24403|baa57dbb55360f9706c9cd409233be7bef3b31f68f35217e06d1936658193e2f|run, validate_inputs|
|78718-prefix-export-closed-mesh-storage-v1.py|25593|5126cfca789877456463ae640d0f174d45ab50dffbe83233c080b02f21119ea5|prepare|
|78718-prefix-review-closed-mesh-storage-v1.py|11228|9a211f07178ae7653518b59a243dee0046825cec2e7fae287762ebdef5a11611|main|
|78718-prefix-terminal-error-storage-v1.py|48878|fdaddf0466c5a7a1606315a5c741b55882e9a1170b985dfd4b30b86e574437b0|candidate, prefix_metric, prefix_storage|

## 3. 实际reader与终门存储子程序检查

root实际cdc599/session39085 → fce588自然exit0。
脚本scripts/78718-check-storage-readers-v1.py；精确命令为：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python scripts/78718-check-storage-readers-v1.py --scratch-dir /tmp/78718-storage-reader-fixtures-01 --source-ledger notes/2026-11-10-78718-storage-adapters-source-ledger-02.json --report notes/2026-11-10-78718-storage-readers-check-01.json
```

cwd为当前topic。报告12678 B，SHA
480b4761ccfbc5fcf0955fc87793955346b7de9f662fbfffce31836b4cf041c2。
检查脚本在报告绑定自己的完整源码及33项来源/账本（含14原源、16新源）。
两份确定性有限合成输入为M2/5节点与M24/11节点，固定随机种子78718000+M，
二进制有理nodal数据，含负零；小fixture只留scratch，不当曲面候选或上传数据。

实际支付：

1. 重新纯执行v2 builder得到完整文本，逐字匹配全部当前新源与原变换账本；导入全部16新源。
2. 新terminal的原SOURCES（tail/reference家族）完全同旧terminal；BOUND精确1/500000000、
   FACTOR、LOWER、height/positive-alpha来源全同，所有新prefix/角向源hard pins逐字匹配。
3. 两套reader都读取相同原gzip/NPZ逻辑字节P。新codec按257B强制多片，仅用于小fixture；
   P重组逐字相同，不重新np.savez。legacy单容器及新descriptor/parts均为原始P的存储。
4. 原/新SharedHermite的mesh、jets、mean increments、h、quintic系数、0/1/2阶实际点值
   与角向三个basis值相同且负零符号相同；longdouble未定义padding不作浮点差异。
5. 原/新ExactHermite的精确inlet有理量、完整interval power上下端和0/1/2阶
   全段/中半段Bernstein ranges逐个binary64位相同。
6. 新reader实际storage闭包相同；以M64扩充元数据冒充定义base会拒绝，保存base M24语义。
7. 每份输入用fresh primary子进程调用真正新terminal.prefix_storage及prefix_storage_ledger，
   定义base与扩充元数据分开，重组/hash绑定及旧路径迁移账本通过。缺storage文件条目、
   common逻辑SHA改变、common storage引用改变均拒。子进程未导入NumPy/SciPy。

较大高熵字节流及通用NaN payload、字节序/C/F布局、23类坏存储的实际core检查
见numerical-new-storage-core-check-01.json；本次没有重复那些已有充分执行。
它与本次检查的输入和作用域不同，不能混用报告或哈希。

## 4. 数学含义与仍需完成的检查

纯字节层只把原gzip/NPZ输出P分片/重组；P完整字节相等时全部原NPZ头、数组dtype、
shape、Fortran标志与数组位值相等。原reader的数学段保持原文本，故给同一有限图。
改变的producer段只在原np.savez和gzip.compress后获取存储，原mirror parity各执行原语句一次。
common-cut两处直接读NPZ均用defining base载入，其padding、signed modes及精确修正公式不变。
新prefix独立arithmetic副本仅替换prefix导入，原tail backend及M12家族保持原样。
这些是需要完整来源审查的论证，不能把几个fixture当作所有数据的数值证明。

本次没有运行完整producer、common-cut数学构造或terminal.candidate，更没有新曲面认证。
报告明确full_common_cut_or_candidate_gate_executed=false、full_producer_executed=false、
new_candidate_or_geometric_certificate=false、production_ready=false；0 BVP/Newton/DN。
后续须未参与者检查全部134个替换和完整真实消费者闭包，然后才能在实际单容器超限时
采用此新身份。成功候选的完整输入、最终证书、网格及原种子独跑仍须实际执行。
