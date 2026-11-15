# 共同 word 第二次 actual：共享 producer atom 表的选根接口失败

日期：2026-11-15。**保存真实失败，不是研究结论。** 首次 manifest 接口修复已公开通过；第二次真实消费者又在原输入结构解码前退出，没有得到共同 word 列、研究消元或指定点判断。

## 1. 公开身份与真实输出

[run43675170178](https://github.com/Rogerhu12/math-research-public/actions/runs/43675170178)，source

~~~text
dd7b89f2835636c874378af160a760398afa36d9
~~~

lane character_head_word_relations，整体 completed/failure，发布步骤成功。

执行 driver 为 literature_character_head_word_relations.py：
75634 B，SHA256

~~~text
1629ff68dd4c4b8acb151939fdb2733f048d07b5f5f780f2013efd07ded2f0f4
~~~

公开新增的2项 manifest metadata 人工全部通过，耗时0.000399631 s，RSS29.6015625 MiB。没有重首轮公开toy9。

真实 main：

~~~text
completion = implementation_check_failed
phase = binding_existing_originals
error.type = ValueError
error.message = the canonical head contains an undeclared input color
elapsed_seconds = 0.350351173
peak_rss_mib = 143.453125
exact_budget_checks = 0
~~~

原目录 notes/actions-43675170178-1-character_head_word_relations：

| 文件 | bytes | SHA256 |
|---|---:|---|
| character-head-word-relations-binding-development.json | 2834 | 4fa06e75a6521972d6a3a7cc669913c208a8989d7d2941324100eef9532662f7 |
| character-head-word-relations.json | 2602 | c98f1b74f61ace20eabe7d6727d89d514ef428cd8f0af52c1f5479c3edc500c7 |

两项身份来自同目录 publisher receipt 的 outputs。失败小件继续保留。

## 2. 准确原因

已发表完整 head 使用一张共享 profile atom 表。它不只保存本次77个完整 canonical 根的祖先，还保存 producer 中间计算用过的其他 atoms。

只读这份原表的元数据可见：

| 颜色 | 原表中的 jet 记录数 |
|---|---:|
| q | 5 |
| qbar | 5 |
| a | 3 |
| b | 4 |
| c | 4 |

全表2332个 atoms。a/b/c 是原生产者的中间颜色名称；不能把它们冒作实际 q/qbar，也不能据它们在共享表中存在就判77个选根含有不允许的颜色。

新 decoder 错误地要求**整张共享表**都只含 q/qbar，而本次真正需要的是77个完整 $-4/-2$ 选根的传递祖先闭包。它在建立该输入对象时拒绝了共享表中的中间颜色，尚未进入任何新 word 映射。

## 3. 只修选根的传递依赖边界

修订步骤：

1. 从 R174 已绑定的77个原列提取其完整 $-4$ 与完整 $-2$ 根；不是先裁为 balanced 再漏掉其他依赖。
2. 只读取原 atom 依赖图，得到这些根全部实际祖先。没有原式评价、forcing 重编或新增响应。
3. 仅对这个完整闭包建立新的 ring atom 映射。没有被这些根引用的 producer-only atoms 保留在完整原表中，但不送入 canonical 解码器。
4. 每个可达 jet 仍严格要求 q 或 qbar。选根若实际触达 a/b/c 等颜色，仍失败；不改名、不丢项。
5. 每个可达 integral 的所有原祖先必须存在；遗漏祖先明确拒绝。原 monomial 若引用闭包外 atom，同样拒绝。

原完整2332表、各选根完整原 hash、head packed/raw 双身份仍保留并核验。新报告记录总原表大小、实际可达 atom 数和未解码的 producer-only 数。具体实际闭包大小须等下一公开运行，不以全表统计冒已经取得的研究结果。

没有修改固定颜色 IBP、shuffle、逐列转换身份求和、77基、指定点、旧 pure40/J/D0 代表或任何数学假设。

## 4. 新源、精确差异和唯一新增人工

修订 driver：

~~~text
literature_character_head_word_relations.py
79108 B
1ec5fab96ec173c3e1583b40a124c5c98b3249cec9a87be39db3b3066e31b300
~~~

模块 literature_color_priority_words.py 仍为21642 B/ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9。

精确 diff：character-head-word-selected-ancestor-fix.patch，
9167 B，SHA256 b5afa7d93c110daaffe5e649e4d8a71c78c0309b33152216775eb2fb8e8142a7。

新源 py_compile 已实际通过。本地仅新增2个人工：

- 人工共享表中的不可达 producer color 不污染所选 canonical 根，而所选 integral 的真实祖先保留；
- 人工可达 foreign color 及不完整祖先闭包都被拒绝。

未重复首轮toy9或上一轮metadata2，也未在本地运行真实选根/word/研究消元。

新回执 character-head-word-relations-atom-selection-local-development.json：
2752 B，SHA256 aead77ab1e734949f87beebf776d4aaafe9a18e1e8750a7a42014ff48f0d89a4。

## 5. 下一公开入口

下一 job 只跑新的选根人工：

~~~sh
python scripts/literature_character_head_word_relations.py \
  --atom-selection-toy-only \
  --output "$OUT/character-head-word-relations-atom-selection-development.json"
~~~

真实入口仍使用同六个已发目录和240 s/1024 MiB预算。前两次都没有研究 word 状态，所以不添加伪 resume 参数。

下一结论仍必须来自真实共同表和完整原关系。R178/R179 的纸面定理不会把这次输入失败变成数学结果；R177 是否良定义、是否被某条新原函数身份切掉仍未决。
