# R230 后继：权零 H 的 universal 平端一次层消费器

日期：2026-11-15。**设计与源码已经完成；当前执行环境不可用，12 项新人工尚未执行。真正研究只在本公开仓库 Actions。**

## 1. 唯一目标与命名

消费已发 R201 的完整算子

$$
H=C_2+\frac1{48}R^{(0_{\rm old})}
+\frac{11}{64}R^{(2_{\rm old})}
-\frac{13}{96}R^{(3_{\rm old})},
\qquad \pi H=0,\quad \lambda_+(H)=1.
$$

只新增 H 与16个权零响应基的模式 −2 **局部次数一次层**。不求完整四次 NF、不再求 H0、不评价任何真实 profile 或几何。

明确写 $R^{(0)}=\Pi_0R$、$R^{(0)}_{\rm p0}=R^{(0)}\cap\ker\pi$。它们均只在真权零；不能把后者与 R225 的全权 $R\cap\ker\pi$ 混名。

两项准确新判定：

1. $T(H_{-2})\in T(R^{(0)}_{-2})$；
2. $T(H_{-2})\in T((R^{(0)}_{\rm p0})_{-2})$。

第二项用 R116 **已保存**三行与 R201 的 pure 像维数三标识该块 pure 核。未新增或重评幂尾。

## 2. 新源码与稳定身份

| 文件 | 字节 | SHA256 | 未挂 Git blob |
|---|---:|---|---|
| literature_endpoint_first_layer.py | 11829 | cf14e26c215bd93feb43dc4b56b8ecdcf9f9013084236e772229404eb9401b69 | e58f2dc2d76c7ea65781fd21dc9a3f54a34ce61d |
| literature_character_zero_endpoint_layer.py | 29604 | bb7be8fc3fa6b98f3f69aca96e5145c6df1f3d581ea85d14aa7fb6ccfefe6a94 | 90bdb0138d92e5e14c1e49642c7fd1b8ebd64408 |

安装到本课题 scripts 目录。所有旧代码保持冻结。driver 继承已发 zero-pure consumer 的完整来源核验，并另核新模块的完整字节和 SHA；不要为了通过门修改已发旧源。

主要旧直接依赖：

- literature_character_zero_pure_readout.py：29283 B / 8d99414bda0a9bf61925f74e5378bfe80532fc8d9b9d35d6cc73625f8f15f7d1；
- literature_character_head_zero.py：42361 B / 337966b4fb9a417ed62d650cac87ffc4c41bedc9938e11c1520fe1136b53dee4；
- literature_color_priority_words.py：21642 B / ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9；
- 其余 exact/colored/原输入 decoder、同 Gamma 与读取 helper 由已发 source_identity 完整递归绑定。

两个新文件只为此新层提供实现。映射模块不含研究入口；actual driver 必须同时满足 GITHUB_ACTIONS=true 与准确的本公开仓库名。

## 3. 五个旧输入目录

### 3.1 原静态 L0 与 W

目录 notes/actions-43645177423-1-local_fourth_quotient。

- run43645177423；
- source2f1b809c0b0abb7a26303d36940edc203815f872；
- main3982 B / 19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a；
- receipt SHA c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba；
- local-fourth-quotient-original-expressions.json.gz：
  packed657195 B / ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace；
  raw3518194 B / d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1。

使用旧 complete export，不重编任何 W 或静态 forcing。只解码 C2 同 Gamma 原组合所需的模式 −2 根，以及旧16响应用到的 W 子集。

C2 为 F0 状态键 (0,2,0,0)，先作完整八参考 Gamma 线性扣除，再只投影真权零。实际 R196 stdout 已记录其原模式 −2 SHA：

b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f。

本次必须逐字一致；不改用未归一的 static 系数。

### 3.2 R126 旧16响应的原定义

目录 notes/actions-43649525432-1-g_first_translation。

- run43649525432；
- source5852d7d4400859e53dde789b4d63f200d0e0acce；
- main23923 B / 9926a1f7026064c95c297b34da60ed5f1b345bc37753a23e75295cf44792fe82；
- receipt33085 B / 06e5d82a7e7db8922d42347920609c83a3ad0114050cdbbdafc72084c3e25bec；
- G-first-translation-complete-report.json.gz：
  packed17734 B / 511431508d58a1b6fe3fb783efe6d9c0b9be9005c86c08796d992ad19441a30b；
  raw74559 B / 4f88bc5fa5af321c57953c1eb7316efbd53d7f4d2da21d2b9c933bcaf617ab45。

沿用已付旧原下标
0,1,2,3,4,5,7,8,9,10,11,12,13,15,17,19。

旧数据没有 portable 响应原 DAG，后来的 H0 也不保存 payload。
因此必须恢复这16个模式 −2 原根，逐根核原 SHA。恢复严格只用冻结 R78 的 −2 公式；不生成 −4 输出，不运行 pure NF、旧四依赖或旧原值评价。这16项是必要输入恢复，新增科学目标是它们的一次层。

### 3.3 R196 真实头部来源

目录 notes/actions-43681388902-1-character_head_zero。

run43681388902/source7872857e7750e1b5091560b6362e52dd952bc6fa。
receipt45501 B / 7919e2406650d394b1128d7014585dbdb830a87adb7979e74f6b2e752e484abf。

只读允许保存的 metadata-only receipt。它绑定原 driver、run、source 及 stdout result 身份；数学身份使用已发表 R196，而不是从 hash 猜数学。

### 3.4 R201 的已付 H pure 身份

目录 notes/actions-43683171512-1-character_zero_pure_readout。

run43683171512/source8c1ab4bab5763273e1004734a9582e3e9d697f9a。
receipt45729 B / 0d926d181f6e607af71a59f62cb83cb187e7a9b705508308ffb56adf16472d4f。
旧 result 身份24340 B / 1fd475ffeaf62258132ac7d938b4f563f7401f2db0c38e78403f4c9de39b239b。

只核发布来源，不索取不存在的 payload，不重540项 pure 原差。H 的准确系数由 R201 已证明结论提供。

### 3.5 R116 的三条已存 pure 坐标

目录 notes/actions-43646543691-1-full_m8_tail_response_projection。

- run43646543691；
- sourcef0652a013fe546778300f0213e659f63ab96ed07；
- main9591 B / 7237cadaac3c4581862d8aee86b94692f0e2436ab7fdb7e393c7b721125d61a7；
- receipt31399 B / 640bf2e0f17bfa635dc688581a192855f372bc7aa840c0ad97614d8696e59de1；
- full-m8-tail-response-certificate.json.gz：
  packed44576 B / b0859868f2db2a08ca1b2831e5ab010840eed8e7ebda01fca49d598822d147a4；
  raw274274 B / a8b5577903e419d2eabe2c327c2c721401acea2d0845017f86c260b2ddb8c36c。

旧 main 没有 github_repository 字段；本新消费者明确使用其固定原字节 SHA，加真实 publisher receipt 的 repo/run/source/lane/output/source 绑定。不会伪造缺字段或放宽到无来源数据。

仅按相同二阶方向、第三原 hash 和真实旧下标匹配16列，读取 (c_power,r_power)=(0,32),(1,31),(2,30)。R116 全局编号为 8*third_index+quadratic_index，不能误用相反顺序。已存三个 pivot 与 rank3 原记录同时核对，但不重算旧消元。

R201 已证完整 pure 像维数恰三，所以这三行在 R^(0) 上有准确的 pure 核判别作用；不能提升到其他真权。

## 4. 一次层的实现与原积分方向

原 DAG atom 的 int_right 实际是 I=∫r^x，导数为正。映射直接用

$$
I(E)(X)=I(E)(a)+\int_a^X E(s)\,ds.
$$

其初值仍是同一个原 Expr，在端点 a 求值；未引入独立 tail symbols。

每个子表达式保零次多项式 P0(X) 与一次线性局部算子。乘法只保 P0*L1+L1*P0。有限左积分按 R230(31)/(32) 准确支付所有下端项。

最后只有一次层的三次系数进入新 R178 映射。外 jets 置0发生在完整三次映射之后；积分内部保 q/qbar，所有嵌套右尾与 shuffle 关系保留。max_weight=3 明确禁止以此入口重新归约完整 quartic 根。

每个新行保：

- “局部微分”或“左矩积分”种类；
- query X 幂、f jet 阶或左矩次数；
- 端点 a 幂；
- 完整三次负尾 word（原存储方向）。

从真正的尾函数与局部算子构成 universal 表。没有某个冻结圆的尾值输入。

## 5. 两门证书及解释

两次新有理消元分别消费：

1. 全16个响应的一次层；
2. 相同16列的一次层加三条旧 pure 坐标；H 的三条 pure 坐标由 R201 为0。

比较列可依赖，不假设本新投影保旧16维。所有秩仅称 universal 新层秩；不改写 U/R 的完整维数。

成员结论保存准确旧响应系数，并另外组成 H−ΣcR 的完整 raw 模式 −2 差。使用独立新截断器及三次边界映射，必须得到同一新层准确零。两门若给同一组合，复用这一条已成新原差证明，不重复它。

窄门成员另核三条已存 pure 行的同系数和准确为0。因此得到真正的 pure 零、lambda+1、一次层零代表；不表示完整 Lf 成员。

非成员给至多17行的准确有理对偶，对全部17个原列重乘后必须是 (0,...,0,1)。对偶行包含完整算子/真实尾word标签，不是形式上给每个右尾一个独立自由数值。

非成员只适用于真权零 universal 比较；不授其他权在固定圆不抵消，不授 lambda+ 在全 U 或全部 U0 的因子化。H 之外的两个零权商方向也未在本轮追加。

## 6. 新人工与执行状态

共12项，当前只是源码定义，**没有运行或通过回执**：

1. 原三次右尾真实保留；
2. raw I 的左增量加号；
3. 外多项式×线性高jet 的全部有限 IBP 项；
4. 嵌套左矩积分的准确化简；
5. 三次 exact derivative 的真实端点外jet为零；
6. 三次 shuffle 耦合，不把初值当自由符号；
7. 嵌套右初值的外多项式边界关系；
8. 纯局部四次项无一次层；
9. L=D+lambda 的小型有限有理消元；
10. 加入旧 pure 约束可改变新层成员结果；
11. mixed-only 恢复式对人工乘法算子的独立 R78 核对；
12. 旧 pure 行只加到响应列，已证 pure 零 H 加0。

环境 unavailable；交由同一新公开 job 先 py_compile 与 --toy-only，成功后运行唯一实际目标。不得把以前任何开发回执写成这两个新源已通过。

## 7. CLI、预算和输出

推荐 lane：character_zero_endpoint_layer。

开发：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_character_zero_endpoint_layer.py \
  --toy-only \
  --output @OUT@/character-zero-endpoint-layer-development.json
~~~

实际28个参数 token：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_character_zero_endpoint_layer.py \
  --static-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient \
  --R0-directory topics/visible-flex-new-mechanism/notes/actions-43649525432-1-g_first_translation \
  --head-directory topics/visible-flex-new-mechanism/notes/actions-43681388902-1-character_head_zero \
  --pure-identity-directory topics/visible-flex-new-mechanism/notes/actions-43683171512-1-character_zero_pure_readout \
  --stored-pure-directory topics/visible-flex-new-mechanism/notes/actions-43646543691-1-full_m8_tail_response_projection \
  --max-seconds 240 \
  --memory-mib 1024 \
  --integer-bits 8192 \
  --max-terms 100000 \
  --max-IBP-calls 300000 \
  --max-cache-entries 250000 \
  --max-summary-bytes 95000 \
  --max-certificate-bytes 8000000 \
  --output @OUT@/character-zero-endpoint-layer.json
~~~

时间/RSS/整数位数均轮询限制；三个原映射缓存、三次 word 缓存和新行数有界。所有新 cubic 调用含 fresh 差在总预算内。资源退出明确标 partial，不宣称成员/非成员或保存了可恢复 cursor。

MATHEMATICAL_RESULT 在 stdout 直接打印 H 一次层是否零、两门完整结论、全部新有理组合或有理对偶行、fresh 差身份。随后打印完整有界 JSON 摘要及其 SHA/字节，避免结果只在临时文件而不可读。

完整新机器证明仅保内存并记录大小/SHA。@OUT@ 只 runner 临时，不将 payload、证书、Actions artifacts 或 Release 数据写回仓库。若摘要超过声明 cap，明确 summary_output_limit，不悄悄裁剪成成功。

## 8. 不发生的工作与下一判断

本轮不恢复 N0/N2/v2/v4，不重3974 forcing、完整 H0、旧16评价或旧 pure NF，不选择一个不存在的 P，不计算任何固定 circle 的 tau，不求路径或 ruling。

若层为零或窄门成员，立即把这一条 lambda 读出路线按准确范围关掉，转剩余 p²层/完整其他观测。若窄门非成员，先交新 universal 原式及对偶，再决定如何给真实解析圆与全权分离输入；不从一个投影秩宣布主课题完成。
