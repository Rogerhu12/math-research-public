# R801：原六至八次幂的准确长尾及真实低幂依赖闭包

日期：2026-11-15。状态：**公开 Actions 的实际计算和完整输出 IO 核验均已完成；没有计算新函数关系、极除子、η、β或高度。**

本篇消费 [R801 原证明](R801-original-minimal-long-tails-and-exact-relation-interface.md)、
[原方法](../notes/R801-original-long-tail-extension-and-relations-method.md)，
原 R775/R786/R795/R799/R800 输入与各准确配方均不改变。
原短基和旧系数没有重算，原基没有重选。

## 1. 实际成功任务

- [公开 run43701282817](https://github.com/Rogerhu12/math-research-public/actions/runs/43701282817)，attempt1；
  source commit 92961ce5b5a526109c3ba6c101961dc3c3100a85。
- job132772758246，公开 core 步骤和最后完整 verify 步骤均 success；
  run 在2026-11-15 10:06:58 UTC完成。
- 数学核心实际耗时796.738574836秒。
- 只新增以下原准确系数；表中终点均为包含端点。

| 原普通空间 | 原维数 | 本次新增 qY 指数 | 连同原前缀的完整范围 | 原整数尺度 |
|---|---:|---|---|---|
| V6 | 1506 | 109–141 | 0–141 | 82^12 |
| V7 | 1778 | 96–175 | 0–175 | 82^14 |
| V8 | 2050 | 109–195 | 0–195 | 82^16 |

七次幂另分别保留至169、171的真实完整 index；八次幂另保留至192。
它们准确对应原五个 N170/172/176/193/196 的消费者。
没有生成 V6 的142以后、V7的176以后或V8的196以后系数。

所有新尾保留原40个ξ坐标、20个t坐标、全局指数相位及逐项反演检查；
原power2至6的新增尾还通过同一R775的mod739比较。
七、八次基沿用R799实际所选行及其原minor，不把此次延长包装成重新选基。

## 2. 实际依赖闭包比纸面最低需求更全

本次严格沿原recipe和准确消失阶闭包执行。
读真实产物得到：

| 原幂 | 行数 | 本次是否新增 | 本次新增范围 | 现有完整范围 |
|---|---:|---|---|---|
| power1 | 146 | 否，读取R800 | 无 | 0–195 |
| power2 | 418 | 是 | 129–195 | 0–195 |
| power3 | 690 | 是 | 129–195 | 0–195 |
| power4 | 962 | 是 | 129–195 | 0–195 |
| power5 | 1234 | 是 | 129–195 | 0–195 |

这是实际closure和全段ledger的结果，不是把预定上界当成完成状态。
所有12种实际二/三锚点乘子均能别名原R786的完整行，因此没有为它们
重新生成从指数0开始的一套乘积。原6仍只延至141。

**直接后果。** R801原方法提醒七、八次铅笔另需全部原690条V3
分别至136/149；本次真实依赖闭包已经全部覆盖至195。
因此这个具体的基尾缺口现在已关闭，后继直接消费已有V3段，
不再追加或重复生成136/149的尾。第二关系本身、其实际rank690+e以及极除子仍未计算。

原 R803 的符号备用路线最高N202仍没有被本次V8覆盖；
只有实际选择该消费者时才考虑196–201的缺口。
原 R804 已选择的五个实际低次数映射仍是N≤196，不要求该备用延长。

## 3. 完整输出与来源审核

实际artifact14156204348，名称
serre-global-R801-original-power6-to8-long-tails-43701282817-1；
API标记未过期，当前到期时间2026-11-16 10:06:07 UTC。
实际 ZIP 大小1,049,535,812字节，完整字节SHA256：
dad8f653dd672099a873618992f32425902298250b1f62a46d8436983a6ef792。

全部30,781项full manifest文件逐字节数/SHA核过；
共30,773个已成stage，其中30,764个新增tail段。
所有source/request/core/wrapper/workflow/两README/helper
均以原source commit的git对象逐hash核对。

原冻结wrapper的全部结构、依赖、节点、前缀、frontier与来源断言也已通过。
本地两次全量缓存读入因资源不足以137结束，未出现数据断言失败；
之后仅把verify中的tail_headers字典替换为按相同文件惰性读取七字段的MutableMapping。
原各检查语句及执行顺序不变；文件名保插入顺序，
每次读取返回node_key、node_fingerprint、node_identity、
first_exponent、last_exponent_exclusive、previous_segments、source_dependencies。
原函数经这唯一替换再反替换后与冻结源码逐字符相同，回值0。
公开workflow自身也已执行冻结verify并成功。

本地只做IO/schema/hash，不导入或执行数学core。
审核脚本SHA c440984a543abaa6d1996a5c4e5cb7934da0e920c7a2b56bfc0477adb2e5058f；
原verify函数SHA cc2e775c8cf6bca986abff8a2413bd1d7ba6960ad751039934cfebd9498e5230，
惰性缓存版本函数SHA 747b9b241744b4f372c230bddf9b7957a4f298d5ab34d4195403b6c50a69155b。
小IO摘要17,860字节、SHA
50f07681a3592ed70ead8dc20547d62b52438a13214492b4e70b3f2be057edba；
摘要与所有可重算证书/系数都不入Git。

## 4. 固定源码与输出绑定

| 源对象 | SHA256 |
|---|---|
| README.md | c6db597c32b022d46d861463e32ad7160545e088610916339bd47e1acae74970 |
| topics/serre-uniformity/README.md | 35f82f3d96f1e07d1b7c3f0320398fdc0cd68d0c0e55ac17881c9f976299646d |
| topics/serre-uniformity/scripts/R801_original_long_tail_extension.py | ba9c52a31b17439de3f945d4cd3e2575b3f6a812f7685f8ac5f07af0e656ce4d |
| topics/serre-uniformity/scripts/R801_public_original_long_tail_extension.py | 11bdf0843cb2fa9e0dbe75c73b7b2300f58fec6d247a7597e0787bff986193b1 |
| topics/serre-uniformity/notes/R801-public-original-long-tail-extension-request.json | f37dc4d0eba76b86ff8fdadb52d730e82952a52e870cb7d11de4f5271cd9a8d1 |
| topics/serre-uniformity/results/R801-original-minimal-long-tails-and-exact-relation-interface.md | b283280e94a9b429d57a20e8bc1c3e40ce552a8eb06ca8ddb19a6d43d18fb6fd |
| topics/serre-uniformity/notes/R801-original-long-tail-extension-and-relations-method.md | a96d7c3b3e4665b1ca2cdd7383e08406fe3d4cc0b8a1bea0aa4a43d110a74126 |
| .github/workflows/serre-p41-original-long-tail-extension.yml | c6540b0b42bf630509b75ce75b017cf62aa1376b697a61d3fe5e2fb14b1c71fc |
| topics/serre-uniformity/scripts/R786_public_exact_power5_short_basis.py | 7fbfe97b21ff9f58de4f1d2891b9f4a8cec4712e1b1c6d26d6d1ab9c336b81ec |
| topics/serre-uniformity/scripts/p41_public_actions_recovery.py | 39de279d30ad1493f1727c2e3c650b47b2bb0191765770b32a17ae2adb97c49e |

| 实际输出 | 字节数 | SHA256 |
|---|---:|---|
| p41-original-power6-to8-long-tails-certificate.json | 8597 | 1fbcd66fb639ac94942d6f82df5ca0c291fdf3cb7af3a13c7971a6b42992c64b |
| full-outputs-manifest.json | 8877946 | 4f636429e38767b7cc57c010f0480391ecf301d7edffe98ba09249a14990371f |
| R801-stage-manifest.json.gz | 1518627 | be5caff277fedb7b857b1c9ccf0c2b5e9a98c70711dfbf0b5d268af150bd1923 |
| R801-original-recipe-dependency-plan.json.gz | 1104557 | b9d98f46026da8049878d780ac6b597920d61f260224e307f04a5757ef0078ce |
| R801-actual-auxiliary-coverage-index.json.gz | 1406763 | b027d701ca5737ad98a55f72b0ea553aa9696f698f65f6728109dd69be705f3b |
| R801-required-original-prefix-retention-index.json.gz | 520220 | d377e834ff58bae45de01f56eb1a602ad203bdb938c2b76d04947ac95e2abfc8 |
| R801-retained-producer-inputs.tar.gz | 523795908 | 9036398ec3075261295848037712f137c661cf2be8393c5e7fc859a0f01b259c |
| run-receipt.json | 663 | c0e92fa638f87d321b90ea00c30c1456b2dbf702a8f0b96918ed7e1fa113fdcb |
| core-receipt.json | 467 | 7eff858e221f102606a6a03bbef978d673711823c85c14a687c9cc53af29ad11 |
| public-actions-input.json | 8373 | abdfb8dfc8f2caa019ae21dff995b1b3f1fd2f9d893479320f886935e75dc2c3 |
| retained-inputs-receipt.json | 9273 | 630c8bdd9a353472046d8ad4cad04cd7cf9667bf9ded8f943b79bd19aee097fd |

### 各真实 frontier index

| 原幂/排除终点 | 文件 | 字节数 | SHA256 |
|---|---|---:|---|
| 6 / 142 | R801-original-power6-frontier-0142.json.gz | 332052 | b168a7943483ffa725520882387947209adf18ba77844f87560796e3efa0f707 |
| 7 / 170 | R801-original-power7-frontier-0170.json.gz | 289841 | cae531739752c0decfdf220f3715a055f4e9fddddd9b26723aa71c933e8b6e63 |
| 7 / 172 | R801-original-power7-frontier-0172.json.gz | 382644 | 29ac6a4ab0a4b36a16c3690510ace43c6c3841fe5c8ab3114ef78a6a7e1392bf |
| 7 / 176 | R801-original-power7-frontier-0176.json.gz | 476998 | e4014d88cfb69419c53d650b807614df8158c3ec6692f128588f588ad50c1380 |
| 8 / 193 | R801-original-power8-frontier-0193.json.gz | 335382 | a71961611cc951408aa10bb68bdb48fc62c6c2499f81af56e7197b880a7fe75a |
| 8 / 196 | R801-original-power8-frontier-0196.json.gz | 443224 | c79ce4f80769a2f9e343b470ac59dc986f5749a2474b9f07b29af4784b64c245 |

## 5. 当前可直接续传的原输入

当前输入bundle为523,795,908字节，SHA
9036398ec3075261295848037712f137c661cf2be8393c5e7fc859a0f01b259c。
其中10,477个成员全部逐bytes/SHA核过，与原五组成功producer及其父链一致；
保10,436份真实原前缀文件，含全部所选R799短基和原R795/R799六次前缀。

| 原producer | 原成功run | 原source commit |
|---|---|---|
| R775 | 43679160495 | 032899cc3bcd937497a857df0c271261fc709ae5 |
| R786 | 43682100611 | dd262672a8b1e2af82277b15e0fa766038609670 |
| R795 | 43692029484 | ac6d8fff1e1905539339bf1bec39365fd62312ba |
| R799 | 43695571499 | 2ebb10bc2cca7000374f83fa855030723deca2f4 |
| R800 | 43696070150 | b53ef624e98b6cdbc9e59ad1bd7d33509dfdfc8c |

完整源文件SHA与manifest链由已冻结实际请求及上述证书绑定。
后继按真正所需文件选择最小输入包，不把1GB整份输出无条件再次展开或永久存档。
完整raw仍仅在一日当前Actions artifact/bundle传递，不进Git/Release。

## 6. 接续的精确边界

- 原R787函数仍按自己的source/core及真实断点继续；本次没有求任何新A/B或kernel。
- 原R797每个映射只已生成κ^(N−1)；若消费相应原关系最后一行，κ^N仍各只补一次域乘法。
- R804从原f4的八步加法函数复用，与本次基尾保持同一五个原低次数对象。
  函数表达式、完整极除子/全局约分、η及高度是独立实际阶段。
- 本次已经完成全部较低幂长尾，任何后继不得再以旧纸面缺口为由重算。
  但没有把基尾完成等同于第二真实关系、Jacobian类、刚性化或主定理。

依据：上述真实公开run、冻结R801核心/方法、全部原producer和完整输出审核。
