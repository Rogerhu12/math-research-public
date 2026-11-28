# q090 原响应与六份 warm 诊断：完整来源和精确恢复

本批仅提议退出主树的九份旧生成 JSON，共 **305,008 B**。固定候选快照是 `922382c228b1c8449cf3119a1cd5447185dc512b`；逐路径 Git blob、字节数、已有 SHA256、原命令、完整来源、实际结果边界与消费者记录在随附 `legacy-q090-response-warm-diagnostics-provenance.json`。提议交付本身没有修改 ref 或删除任何文件。

## 1. 九个对象与保留边界

两份响应是 2026-11-12 的 q090 current-control response（151,211 B）和 c6eighth current-triple response（43,037 B）。第三份是 control-tangent-budget（35,059 B）。其余六份是 q0925/q095 与 c6held/freeq4/naturalc6 三种方向组合的完整 warm inspection，合计 75,701 B。逐个完整文件名和对象身份以台账 `candidates` 为准。

本批不删除任何源代码、证明、物理 port、profile/config、成功或失败 checkpoint、方向数组、资源记录、运行计划、完整比较或选择说明；不涉及任何当前 Fejér、R726、R727 输入。Nelder 原驱动仍未闭合，其 519,142 B 原对象继续保留。台账中的旧二进制记录只是精确恢复身份，不是本批新的删除列表。

所有候选都可通过固定 Git commit/path 或完整 blob 恢复原字节。151,211 B 大响应正文未读取；它的 SHA256 来自原 run-state 与真实历史消费者。其余候选均小于 100,000 B。没有读取、解码、复制或重编码任何二进制，没有把旧数值数组改名装成新参数。

## 2. 实际生成器与全参数

第一响应由完整 `strong_control_exchange_diagnostic.py` 生成，原 SHA256 为 `7df44cfc3606e84f5df8a188d2223fee5747045c07b2fffcc9693ed3931a2017`。其 `base_response` 直接插入原完整响应过程，保存 11 个配套数组，保原控制顺序和 QR/Jacobian 公式；预期的 inspection 停止异常由原入口处理。完整实际 argv、72.05432295799255 秒、exit 0、资源和实际 session 38635 都保留。它不是新的非线性解。

第二响应由完整 `strong_triple_control_response.py`（SHA256 `2d6e1a62fe0b1cba7e657da4d2b53fea4ee45d9bd9659ae3bed989657b5d1bc0`）产生。实际 935 节点、M20、N512、radial/collocation batch 16/12，基点 raw x/y/p 逐字一致；实际一次 Jacobian 与 factorization，保存全部七个方向数组。资源记录 wall 89.41965508460999 秒、exit 0。原计划和资源全体保留，不能由它推出新的接受解。

tangent budget 由完整 `strong_control_tangent_budget.py`（3eac35b7…）读取第一响应和原成功基点；其 13 行是 baseline 加 actual_q4、boost_speed、vu 各四个原比例。原顺序、精确步长和每行结果均可由原 whole report 恢复。实际资源 exit 0、wall 2.712291717529297 秒。其背景/平面 core 样本不等于全活动曲面的曲率或直径。

六个 warm report 的真实入口为：

`strong_multicore_checkpointed_bvp.py → strong_small_batch_bvp.py → strong_checkpointed_tangent_bvp.py → strong_multicore_tangent_bvp.py`。

原入口 2abb9345…与小 batch 包装 2b1d3edc…完整源已读取；原 1,634 B radial-batches 记录对 2b1d3edc…的完整 SHA 精确一致。包装只按原显式 16/12 参数设置原函数的可选 batch 默认值。实际六条命令没有 `--batch-check-output`，所以该源中另一个可选数值比较分支不是本次运行。六条命令有 `--tangent-inspect-output`，没有 Newton 续跑；报告全都声明 `inspection_only=true`、`nonlinear_solution=false`。

原 M20/N512、q=.09 表征、all-knots、tol=1e-6、max-nodes=2000、direct-block-qr、flow-cache=8、refresh backend、完整 profile/port/restart/candidate name 与 q-step 均保。台账保存每个完整实际资源 argv；另外以完整父文件身份和精确 JSON pointer 保留原候选计划整对象，不截去历史字段。

## 3. 真实结果与失败范围

六个 warm inspection 均真实 exit 0、有限域检查通过，但都是未求解的全场 C2 cubic 预测。原 6,807 B comparison 与 3,607 B selection 继续在主树保留，其中六行 RMS、sampled D/K/height 与最终选择的完整 solver 命令仍是原文。不能把 sampled warm κD、线性预测或有限域检查当作最终 PDE-jet 场或连续证书。

第二响应的 balanced QR 条件数只针对原 142×142 endpoint/parameter 矩阵。物理单位 condition_2 为 53594968487.86336；这既不是全局 Jacobian 条件数，也不是折叠或不存在性证明。原 accepted RMS 9.717639276473202e-7 与 scaled collocation max 1.1033736951176919e-8 属原成功基点，不属于 warm 新解。

先前 c6-held 尝试耗尽 max_nodes 的失败仍保留：原说明记 891 节点、8 次 Jacobian、约 .00705 RMS。它没有被拿作成功 restart，也没有转述成折叠或非存在证据。第一 inspection 的预期 RuntimeError 与该真实非线性失败是两件不同的事。

## 4. 确实存在的历史消费者

`strong_tangent_warm_bvp.py` 读第一响应、原 inspection summary、成功 physical checkpoint、原 t/warm_p/warm_y 与所选完整方向数组。后续 c6eighth recovered-r1 的完整 summary 中 `/warm_start/conversion/full_tangent_warm` 保有它实际读到的原 SHA 和方向。恢复消费者时必须恢复全部这些原件，不能只给本说明中的摘要。

`strong_multicore_tangent_bvp.py` 读第二响应、原 c6eighth 成功 physical checkpoint、原 raw-collocation manifest/x/y/p，以及全部实际选中的 q1/q4/(c6) 方向。它按完整 candidate name 和 q-step 唯一选取预测。六个 inspection JSON 本身是派生诊断，不是这个 solver 的 physical/raw 状态输入。后续若要分析原诊断，仍须把所需 JSON 恢复到原路径。

因此本批不以“没有消费者”为理由删除，也不声称已穷尽所有历史 reader。所知实际 reader 和原路径恢复责任都进入台账，原比较/选择也保持。

## 5. 完整源链与旧外部来源

台账登记 34 个本 topic 完整源记录与 28 个真实取回的外部 Python 源记录；记录包含 path、whole SHA256、bytes、Git blob 和固定恢复 commit。其中部分外部辅助分支只是保全，不声称实际调用。

原 `source-dependencies.json` 是完整 24,057 B、91 项、866,846 B 的来源目录，whole SHA256 `7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941`。原 source revision 字符串 `869436630c99aa5a68afb55bd8877c826034d117` 在当前公开仓库的 commit API 为 404。不能编造从该 commit 恢复成功，也不能把当前 checkout 冒成旧来源。

本次按实际调用的 finite-port Python 闭包，从公开固定 `922382c228b1c8449cf3119a1cd5447185dc512b` 完整取回源，核对来源目录的 whole SHA 和 bytes。恢复时按台账路径材料化这些完整原源，再让 `--source-topic` 指向相应 topic。旧 `source-origin.json` 的来源标签与实际公开恢复 commit 分别记录；`numerical-m2-prefix.py:source_revision` 读取该标签，但标签不等于新 checkout HEAD。

原 4,752 B `78718-prefix-tail-geometric-client.py` 没有被当前 8,274 B 客户端替代。本组 finite-port 路径不 import/调用该 client 或 Node tail worker，因此它不是本组真实源缺口；这不构成对整个 91 项目录所有无关程序的重跑宣称。`root_profile_scan.py` 的完整公开源亦保留；原直接诊断未单独记录它的 whole hash，台账如实区分原记录与公开恢复身份，且 q090 使用其 port/linear-matrix 函数而没有调用另一个 bridge constructor。

## 6. 精确数据恢复与科学重算的区分

台账另列全部 28 个原 physical/pp/raw/tangent 记录：两个原 physical checkpoint、各完整 pp-coefficient chunk、原 raw-collocation manifest 与全部成员、第一响应 11 数组、第二响应 7 数组。它们以各自固定旧 commit `2cf540ca1c273724596288484394bb9ca49042d1`、path、blob 和 bytes 精确恢复。只在已有小记录给出 SHA256 时填该值；未读二进制的未知 SHA256 明确 null，不从文件名猜。

在仓库根目录恢复一个候选的原字节，例如：

```sh
git show 922382c228b1c8449cf3119a1cd5447185dc512b:topics/visible-flex-larger-amplitude/notes/2026-11-12-strong-q090-current-control-response.json > topics/visible-flex-larger-amplitude/notes/2026-11-12-strong-q090-current-control-response.json
```

其余各项用台账记录自己的 commit/path，或 `git cat-file blob <完整blob> > <原path>`；旧二进制不能误用当前快照。恢复文件前建立原目录，历史消费者依原路径读回。原大数组既未复制进新文档，也未以压缩/分块/差分形式重新提交。

如未来独立要求重新生成科学诊断，应恢复全部原源和输入，使用完整原 argv，并按原入口防覆写规则选择新的输出位置；原参考路径和来源标签的变动须如实另记。当前台账没有执行这种重算。历史 NumPy/SciPy/BLAS 的精确版本没有保存在已读小记录里，不能宣称跨环境浮点逐位重跑；原输出字节的 Git 恢复则不依赖这种宣称。

## 7. 交付范围

完整台账采用紧凑 JSON 保持单文件小于 100,000 B。whole-parent+JSON-pointer 只共享完整已有元数据，不删除任何原字段、科学参数或未知失败责任。九个候选、完整源表、输入恢复表、完整实际命令与短结论同时保留。

没有本机科学、AST/compile/fixture、额外运行门、ref/queue 修改或删除。根发布者可以把这份完整工件与精确九路径删除一次提交；若候选的当前 blob/bytes 不再相符，应保持该候选并由实际差异决定后续，不能据旧名字误退新内容。
