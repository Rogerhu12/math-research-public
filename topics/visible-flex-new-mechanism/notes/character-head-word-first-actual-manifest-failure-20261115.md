# 共同 word 首次 actual：旧 finite 证书身份字段接口失败

日期：2026-11-15。**已保存的失败实际；不是数学结果。** 首次公开运行的新增人工通过，但真实消费者在输入身份检查阶段退出，还没有开始77列共同 word 映射或研究消元。

## 1. 完整公开身份和真实状态

[公开 run43674559905](https://github.com/Rogerhu12/math-research-public/actions/runs/43674559905)，source

~~~text
b2c4e202672c2e62b4059c93b3d9c26ada0d36cf
~~~

lane 为 character_head_word_relations。实际 job 在 03:56:31–03:57:06 UTC 完成，整体 conclusion=failure；发布步骤成功，失败小件与回执保留。

执行 driver：

~~~text
literature_character_head_word_relations.py
72953 B
8fd67984ef66bc43da2055b68f6d8b062dde260035668c4f565f9f105e344f13
~~~

固定颜色模块：

~~~text
literature_color_priority_words.py
21642 B
ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9
~~~

同 job 的新增人工准确通过 **6个消费者接口检查+3个续算检查**，耗时0.010662711 s，RSS29.25 MiB。没有重新运行初版10项，更没有重 pure40、31依赖、70字面依赖或任何旧研究值。

真实消费者报告：

~~~text
completion = implementation_check_failed
phase = binding_existing_originals
error.type = ValueError
error.message = bound data schema or run/source identity changed
elapsed_seconds = 0.354520260
peak_rss_mib = 143.0625
exact_budget_checks = 0
~~~

因此不能把此运行标记为77列研究已完成、资源退出或任何目标非成员。输入阶段尚未进入 OriginalInputs 的原 atom 重建、投影、word 映射或矩阵消元，没有研究列或可继续的研究 state。

目录为 notes/actions-43674559905-1-character_head_word_relations：

| 文件 | bytes | SHA256 |
|---|---:|---|
| character-head-word-relations-development.json | 3597 | ead1fa4b444c279018d9e2d3307a9e33eada20bd918b33ecca9319584f9c042a |
| character-head-word-relations.json | 2595 | fa581f42ddbb56f6af84c4e5a77e7f3ab6db2d2ce0eb7515bf0f15c747cf205b |

以上大小与身份来自同目录 receipt.json 的 outputs；receipt 同时绑定准确 repository、source、run 和 lane。失败文件保留，不覆盖或删除。

## 2. 准确原因：把旧 certificate 错当成重复内嵌身份的新 schema

只读六份已发表原件的顶层元数据后，准确定位到 run43665971895 的旧 finite certificate。

它的 schema 是

~~~text
visible-flex-character-minus2-finite-rational-necessary-v1-certificate
~~~

该已完成旧证书**没有** github_repository、github_run_id、github_sha 三个重复字段。其 repository/run/source 身份在绑定的主报告和 publisher receipt 中，完整 gzip 又以 packed/raw 双 SHA 固定，certificate 的 source_hashes 与主报告准确相同。

原 frozen helper raw.consume_bound 已经完整检查上述身份、producer、main/receipt 与 packed/raw 双 hash；新 wrapper 随后错误地再次要求六份 export 全部内嵌这三个字段。它在旧 finite 输入上失败。其他五份 export 都实际带有这三个字段。

这是新消费者对已存旧 schema 的接口误判，不是旧证书不完整，也不是任何原 profile 函数身份失败。

## 3. 唯一窄修复

修订 driver 只对**这一份准确的旧 finite spec**允许身份来自已经严格绑定的 main/receipt：

- 旧 certificate 的 schema 仍准确匹配；
- 只有 spec 完全等于 frozen raw.FINITE 时才允许此分支；
- 三个重复字段必须全部缺失；出现冲突或伪造的内嵌身份仍拒绝；
- exact main、receipt、producer、packed/raw 双 hash 和 source_hashes 相等检查全部保留；
- 其他五份输入继续要求准确内嵌 repository/run/source。

没有修改六份旧原件、字面77选择、任何代数规则、原差证书方法、point、预算或转换语法。

修订源：

~~~text
literature_character_head_word_relations.py
75634 B
1629ff68dd4c4b8acb151939fdb2733f048d07b5f5f780f2013efd07ded2f0f4
~~~

精确 diff 文件 character-head-word-first-binding-fix.patch：
6440 B，SHA256 7d9dd7842b033bb727942c930f407f4f97acef871cb507bc98a39d62f6fccd61。

新源 py_compile 已实际通过。本地只新增两个小人工检查这个 metadata 合同：准确旧 finite 可由 manifest 绑定；其他缺失或冲突身份不被放宽。它们不读取真实输入，不重刚已公开通过的9个人工。

新小人工回执 character-head-word-relations-binding-local-development.json：
2756 B，SHA256 15916c398ac5a1233f1ab977833a77d1b1e112cdcd8ac2d4ccbe1e1016b0eb51。

## 4. 下一公开入口

下一 job 仅使用新 metadata 人工入口：

~~~sh
python scripts/literature_character_head_word_relations.py \
  --binding-toy-only \
  --output "$OUT/character-head-word-relations-binding-development.json"
~~~

然后运行设计中完全相同的六目录真实入口。真实部分仍240 s、1024 MiB；没有恢复参数，因为首轮没有产生任何研究进度。此次重新读取原输入是修复入口所必需，不是重算旧研究目标。

后续仍以真实回执判断：如切掉R177点，保存已完成cursor与完整原关系，随后从该state追加 --finish-all-77 处理剩余列，不重前缀。如尚未切，则继续完成77列共同表，不能把部分前缀未发现关系当作完整良定义。
