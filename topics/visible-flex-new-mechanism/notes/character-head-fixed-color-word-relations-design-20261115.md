# R178 后继：77 个已存原式基的共同颜色 word 关系与 R177 指定点

日期：2026-11-15。**新消费者设计，真实目标仅公开 Actions。** 本设计只补完整原函数良定义关系。它不重建十四族、forcing、响应或旧 pure 基，不重复 R174 的 70 条字面依赖，也不重复旧 RREF、LP、86 行或任何几何/profile 评价。

独立新文件：

- literature_color_priority_words.py：R178 固定颜色原函数映射及完成缓存的保存/读取。
- literature_character_head_word_relations.py：消费 R174 的 77 个原式基、旧 pure 转换证书和 R177 的已发表指定点，给新的完整原式关系。

已冻结旧文件均不修改。根代理负责 Git、公开请求与 Actions；本设计没有绕过真实研究执行门。

## 1. 本次只回答一个明确问题

R174 的 147 个字面原多项式列由 40 个完整响应和 107 个 normal 记录组成。已发表实际给字面秩 77、70 条完整原始两模式零差，并给九条新的必要等式。满足这些关系的外部线性赋值，还必须尊重 profile 原函数之间的全部普适恒等式。

R177 已纸面给完整标量 action 严格正的明确点；公开 run43672582314 又验证其全部 86 行、九原式等式、十四族及同一乘子。该点的 old-free 向量为

$$
\left(
\frac14,0,-1,1,0,\frac14,0,-1,1,1,0,1,-\frac14,
1,\frac14,-\frac14,\frac1{16},\frac1{12},-\frac18,0,
-\frac1{12},1,\frac14
\right).
$$

其标量静态部分是 $(1+k^2)^2/4$，其余层由 R177 的完整平方恒等式支付。本次不再寻找反例路径，而是检查：

$$
\sum_{j=0}^{76}a_jC_j=0
\quad\Longrightarrow\quad
\sum_{j=0}^{76}a_j\ell_{\mathrm{R177}}(C_j)=0
$$

是否被某条新原函数关系违反。这里 $C_j$ 为 R174 已保存的 77 个字面基，响应列的候选值为零，normal 列值直接读取 run43672582314 的 107 项准确值。

默认在第一条完整原式身份准确切掉该指定点时完成本门，保存剩余 cursor；若没有这种关系，则继续处理全部 77 列。没有候选点扫描、LP 重求或追加新原列。已有状态可用于后续完整关系收集，不能用已完成目标重新跑一次。

## 2. 真正新增与明确复用

| 对象 | 来源 | 本次处理 |
|---|---|---|
| 完整两模式十四族与 R40 原根、2332 个共享原 atom | 43665345551 | 只读原式；选 77 列，不编译原 forcing/响应 |
| 字面 77 基及 70 条已付原依赖 | 43670254711 | 消费已证选列与来源，不重算 70 条差式 |
| 107→23 的旧准确变换 $B$ | 43665971895 | 直接读取，供新等式投影 |
| pure R40 的全部 word rows | 43657785023 / R151 | 核来源、原 hash、存储摘要和余 letter 语法，零次重新正规化 |
| J 的 pure word rows | 同一 R151 证书 | head normal90 原 hash 匹配后直接使用 |
| D0 的 pure word rows | 43659795254 / R157 | head normal103 原 hash 匹配后直接使用 |
| R177 唯一指定点 | 43672582314 | 读取 23/107 全值；不重验 86 行和完整 action |
| 新 balanced 共同表 | 当前 R178 模块 | 从已存原根只取 $(q^2,\bar q^2)$ 分量并新展开 |
| 其余未存 normal pure 代表 | 当前 R178 模块 | 只对尚无匹配原 hash 的根作新展开 |

还允许原 hash 完全相同的其他 pure 列直接复用已绑定代表。这里复用的是原多项式身份，不是根据 m8 尾零或若干采样猜测成员。

R131 导出保存了 mixed 原根、摘要和 word hash，没有保存全部 mixed word rows。不能把一个摘要当成已经可读的共同 mixed 矩阵；所以这些原根到新共同 balanced 字典的展开是准确的新工作范围。

77 个原 147 下标为

~~~text
0..39,
40,41,42,44,45,47,48,50,60,63,65,68,70,71,78,80,83,85,86,88,93,
98,103,109,111,112,113,115,117,130,131,132,137,138,140,141,143
~~~

原下标 $40+i$ 对应 normal $i$。所有源字段都同时保留新基位置、原 147 下标和 normal 下标，避免把 R131 的 50 原响应下标、保留 40 位置、R116 全局号混用。

## 3. 两根 faithful 投影与 phase 归一化

每个完整 canonical 列使用两根：

$$
\pi C=C_{-4},
\qquad
\Xi C=\Pi_{(2,2)}C_{-2}.
$$

第一根必须是四次 pure $q$；第二根是在完整 $-2$ 原根中按真实颜色次数直接选出的 $(q^2,\bar q^2)$ 项。保存原 phase 因子，不再外乘或删掉 $1/16$、$1/128$ 等归一化。

R159 说明：完整 canonical 差式的这两根都为零，便是完整函数身份。原 $-2$ 多项式的其他颜色分量不被假定字面为零；新关系证书仍保存**完整两模式原多项式差**，另列上述 faithful 投影。

原 atom 的颜色次数与真实仿射权从已经发表的 DAG 结构读取：jet $q_j$、$\bar q_j$ 权为 $-j$，$\xi$ 权为 $1$，同右锚 $I$ 增权 $1$。本次选列要求真实权全部为 $-2$、总 profile 次数为 4。颜色原函数始终是共同 profile 的实际 primitive，不把累计值当独立可赋数值。

## 4. R178 新字典的规则和语法门

固定颜色次序 $q<\bar q$。对于正多次数的局部 monomial，先取实际存在的最高颜色，再看该颜色的最高 jet 阶。只有这个 jet 阶至少为 1 且只出现一次才作局部 IBP。

若

$$
DB_0=f_0+r_0,
$$

则对非空或空剩余 word $w$，按共同右锚准确使用

$$
I(f_0I_w)=B_0I_w-I(r_0I_w)-I(B_0DI_w).
$$

保持剩余 word 长度的分支严格降低最高存在颜色的 jet 阶；另一分支严格缩短 word。每次递归都显式检查这个下降尺度；活动递归 key 再出现是实现错误，不能通过 cycle fallback 假装得到一个已完成代表。

全部深度 shuffle 保留重字重数。零 profile 的多项式 letter 只在非空 word 上积分，边界由该 word 在右端为零支付；空 word 的纯多项式原函数明确拒绝，不丢右端常数。

每个最终 word letter 都必须符合 R178 余类型：

1. 最高存在颜色的最高 jet 为零阶；或
2. 该颜色的最高正阶 jet 至少重复两次。

新列输出和旧 pure 行解码都逐 letter 检查，并保存
every_word_letter_is_an_R178_fixed_color_remainder=true。
这只是已存/新得表示的语法检查，不重新评价旧 pure 原式。

R178 本身只授 soundness 和有限终止，不把非零 word 代表自动提升成非零函数或真实独立性。若独立的完整普适字典单射定理已经发表，可在相同已核语法和转换身份上另行应用，不需要因此重跑 40 个 pure 根。

## 5. 新映射 Phi 与复用映射 Psi 必须分开

固定规则直接作用原 DAG 得到 $\Phi$。它是确定的有理线性 sound 映射。

R151 的旧 pure 代表实际先经过 RightIBP，再经过单颜色 word；仅靠局部规则相同，不能暗称它们等于新 $\Phi$ 直接作用原根的字面输出。本消费者因此明确使用另一映射：

$$
\Psi\left(\sum_jt_jC_j\right)=\sum_jt_jv_j,
$$

其中每个 $v_j$ 都有源身份绑定的 $C_j=\operatorname{Eval}(v_j)$ 转换证书。旧 pure 使用旧成功转换，新列使用当前 R178 新转换。按 R174 的字面基作线性延拓，不需要混用两个正规化算法的缓存。

准确结论始终是

$$
\operatorname{Eval}\Psi=E,\qquad \ker\Psi\subseteq\ker E.
$$

本程序选取 R178 明确允许的“逐列转换身份完整求和”证书。不要求 $\ker\Psi$ 的原差必须被 fresh $\Phi$ 再次识别，也不把 fresh $\Phi$ 的非零视为原身份反证。

## 6. 每条新关系怎样从完整原差证明

共同矩阵只提出一个有理系数向量。提出后独立执行：

1. 从 bound head 的**原始存储行**重新逐列求和，得到完整 $-4$ 与完整 $-2$ 多项式差。保存全部原项、原 hash、输入项计数；不只保存消元后的空向量。
2. 从每列的转换记录重新加载该列代表。原 root hash、投影 hash、输出 rows hash、颜色余类型和来源必须再次匹配。旧 pure 代表还直接同其绑定旧存储行比较；新代表来源必须是确切 R178 文件、固定颜色次序和零 cycle fallback。
3. 不使用消元行 ID，从这些原转换记录按同一系数重新准确求和 pure 与 balanced 两根。两者都必须为零。
4. 将每个逐列转换身份乘系数相加，再用 R159 的两根忠实性，得到完整 canonical 原式身份。

每条证书包含完整 77 和 147 系数、两模式原差、faithful 投影原差、两份准确零 word 和、每个转换的 hash/来源及同锚声明。它不是“两个标签相等所以证明”，也不是用非零 NF 推非成员。

如果上述独立和不为零，报告实现/证书检查失败，不能把它提交为关系。共同矩阵的非依赖列只标记代表基列，不自动授真实函数独立。

## 7. 新消元只在 77 个共同代表上做一次

40 个已证真实完整响应先进入基，然后是 37 个 normal 字面基。pure 与 balanced 行有独立标签，绝不能互相抵消。

每个新列先清本列分母。整数向量与原列系数一起更新，始终保持

$$
w=\sum_jc_j\Psi(C_j).
$$

每个 pivot 使用准确整数消元，再除共同 gcd，控制位数；保存原列组合的三角非零对角。不会重新求旧 147 原行的 70 个 kernel，也不重跑 pure R40 的 31 条已付依赖。

每条新完整身份给

$$
\sum_i a_i\nu_i=0.
$$

只通过已经保存的 $\nu=By$ 投到旧 23 坐标，再模去 R168 的已发表 parity、R174 九等式和本次先前的新等式，输出真正新增的行。这个小增量不重建旧 124 等式或 rank84 的 RREF。

指定点值同时从已发 107 值和已发 23 值计算并要求一致，只评价**这条新关系**。不重新评价 86 旧半空间、十四族 action 或任何 profile。

## 8. 输入绑定：六个已完成公开目录

每个目录读取主报告、receipt 和一个完整 gzip。要求 repository/run/source/lane、producer 源、main bytes/SHA、packed/raw 双身份、receipt 输出列表全一致。

| 参数 | 目录 basename | 公开 run / source |
|---|---|---|
| head-dir | actions-43665345551-1-character_head_minus2 | 43665345551 / 0aae9a6a85583a9f87415e586d8db2c9c7fea6a7 |
| literal-dir | actions-43670254711-1-character_head_literal_relations | 43670254711 / 952cf7927d809150ac2579f1a390225c2cf23f52 |
| finite-dir | actions-43665971895-1-character_minus2_finite_necessary | 43665971895 / 05bb659b59997906316ddd2873aedbf4840f62a5 |
| pure-dir | actions-43657785023-1-general_pure_J_membership | 43657785023 / c606688a842bd811106ff2844e1161a4f34c159e |
| d0-dir | actions-43659795254-1-general_pure_D0_membership | 43659795254 / ce6c80bfbde6158e38c0e74e26fba3f352201658 |
| point-dir | actions-43672582314-1-character_minus2_raw_positive_candidate | 43672582314 / 14f33da3731f543bdafeee98f5f83ec5390f0b5e |

完整 artifact：

| 对象 | gzip bytes / SHA256 | raw bytes / SHA256 |
|---|---|---|
| head | 1247411 / 2c1242e13d253ba352c7ff1b025a91cf564ab2a7cfd93c6bcedc19baa5fac45c | 6560138 / 7a93a53aa7fafa1cff76608aceaeac294911ca4f828746913c1b125ae2fd33af |
| R174 | 41109 / 5d929f4f45265ee4eec949eace228bf4b639753cd0a4b24a8a3d32d0857dc62e | 269605 / ed3bedb70a0f49a058daf578ff9403a7ff89407c55f0954f876bfedaeaeac775 |
| old B | 31976 / 5658e056313fff939356f91c97578a8dfc3e1158661b209c84ba7d2b86aa3634 | 143028 / dd539b088c354d99c04af46d8d7c63822679f13ebc02b14a673c76767fd745f7 |
| pure R40/J | 84283 / af46437f676716a20051bf3bad5a96235398dcf8a45c179d1395bc1f9d84712e | 456216 / 9859368ec20e0923cc168199a7ecb82eff0beac5fa191f1b6388e67cfd1aa550 |
| D0 pure | 15463 / f5355a03cbdb076c9d33900930f0cad5e5c86abf4713f6b59b3acbd9b875037e | 88545 / 117a4bf88cedd3a85ccfc26e6c80324bd67f3ce07aaf19b1837e434b0c7173cc |
| R177 point | 12864 / b7b7cf0fc4bf476c918f9302462e3dc2071b5bff799bdf6131e8b6d7c22e2778 | 60197 / e37ce83e392bdc743614451126cbb64c7444788fd6ae253ead154d3d1a8f7d26 |

所有 main/receipt 的准确尺寸、SHA 和 producer 身份也固定在源码，不依靠完成标签或文件名猜测。原输入只以公开仓库 sparse checkout 供 Actions 消费；不经 API 取大 gzip 或拆分编码它们。

## 9. 资源上限和可续状态

默认真实预算：

| 项 | 上限 |
|---|---:|
| 本次 elapsed | 240 s |
| RSS 轮询 | 1024 MiB |
| 准确整数/有理数 bit | 8192 |
| 原存储 nodes / atoms | 500000 / 60000 |
| 单 word、当前列、fresh 和及共享行字典 | 80000 |
| 本次新增 primitive calls | 250000 |
| 共享缓存总条目 | 250000 |
| shuffle 缓存 | 100000 |
| 小 main | 95000 B |
| state / certificate 各自 packed | 3200000 B |
| 全部发布文件合计 | 4800000 B |
| 单份完整 raw JSON / snapshot expression pool | 40000000 B |

两份 gzip 不同时使用各自上限：先计算 certificate 大小，再从 4.8 MB 中扣 main 保留额，为 state 给出实际剩余上限。snapshot 在构造 expression pool 时即累计字节，不只在最后压缩后检查。

自设 main 上限须在 12000 B 至不足 100000 B 之间；最终小化后仍再次检查实际字节，不能静默写过声明上限。紧凑缓存也保存本轮已启动调用的真实统计，恢复时才按新一轮重置。

每次 source monomial 成功累加后保存内存 cursor；预算中断会卸下活动递归，留下真正完成的共享缓存。每四个完成列以及每条已付关系写 checkpoint。

状态包含：

- 完成列的两根代表、所有转换身份和原行索引；
- 尚未完成的列、当前投影、原 monomial cursor 与准确部分和；
- 完成的整数 pivot 向量及原列组合、正在消元的准确状态；
- 原差/转换和检查中已经完成的原列 cursor 与准确部分和；
- 已付全部新关系和新小等式基；
- 共享 atom/monomial/primitive/shuffle 的完成值。

默认保存完整缓存。若 packed/raw 输出超限，紧凑形式仍保存全部完成原 atom 值、全部完成列和准确部分和，省去可导出的 monomial/primitive/shuffle 缓存；pivot 可由已经保存的列组合准确物化，不重复消元步骤。被中断的原子调用可能重入，不能标为已完成转换。

每轮 primitive 调用计数与累计统计分开。恢复把**本轮**计数重置为零，保留累计记录，使用明确同一新增预算，不抬一个累计上限伪装续算。缓存、terms、bit 和 bytes 仍是全局硬门；若这些全局门使下一步无容量，需要明确更改预算或已有安全紧凑化，不能把它们说成每轮自动清空。

缓存超限会撤回本次新插入，使已保存状态能按同全局门读回。主报告用准确进度 hash 明确最后真实进度是否已保存；若最终存储失败，必须显示最新进度没有完整 checkpoint，不能声称全部可恢复。

续算必须同时给旧公开 main 和 receipt 的准确 SHA；它们绑定相同源码、同颜色顺序、相同六份原输入和同一指定点。不能把别的程序输出当本次 state。

## 10. 新输出

lane：character_head_word_relations。

1. character-head-word-relations.json：小主报告，包括完成前缀、pending 阶段、新真关系数、新等式数、指定点是否被真身份切掉、资源和全部输入。
2. character-head-word-relations-certificate.json.gz：完成转换、原 atom 表、完整两模式原差、两根准确零和、77/147 系数、old-free 新等式及点值。
3. character-head-word-relations-state.json.gz：相同来源绑定的准确续算状态。
4. character-head-word-relations-development.json：同 job 的新增人工。

若切点，complete 表示**这一指定点已被完整原函数身份排除**，不暗称 77 列都处理完；主报告另列 all_77_columns_processed。

若全 77 完成而未切点，本版报告完整共同代表核没有切掉点。不得仅凭这个保守标签宣称或否认完整函数核的后续纸面升级；任何升级要明确引用独立的完整字典定理，而不能省掉这里的全部来源/语法/转换证据。

无论哪种结果，都不从本门本身宣称所有正字符排除、实际 signed control、完整 period/ruling 或本课题完成。

## 11. 新人工与已完成的本地开发

没有本地研究输入运行。已有开发分开记录：

- 映射初版 10 项小人工检查固定颜色、local/word IBP、shuffle、边界、缓存顺序和旧人工 pure rows 只读接口。
- 随实际续算实现新增的 3 项，只核同本轮预算停止→恢复未成原语、缓存撤回后按同全局门读回、expression-pool 字节门；没有再跑旧 10 项。
- 77 消费器新增 6 项人工，核非字面但真函数相同的两列、完整原差/两根转换和、单点新关系值、伪转换拒绝、完整/紧凑中途续算、来源/语法边界。
- 最后仅为新增输出逻辑跑 1 项人工：合计 publication bytes 与最新 checkpoint 进度标记；没有再跑前述 6/10/3。

本地报告准确记录各自执行时的源码 SHA。最终公开 job 的 toy 入口只跑 6 个新消费者检查和 3 个新续算检查；不读真实 head、旧40/31/70 或指定点。最终源仍须由这个公开 job 实际执行，不能把早期局部开发回执冒作最终 Actions 已过。

## 12. 准确公开 CLI

在 topic 根目录下，先公开 py_compile/新增人工，再同 job 跑真实消费者。实际入口：

~~~sh
python scripts/literature_character_head_word_relations.py \
  --head-dir notes/actions-43665345551-1-character_head_minus2 \
  --literal-dir notes/actions-43670254711-1-character_head_literal_relations \
  --finite-dir notes/actions-43665971895-1-character_minus2_finite_necessary \
  --pure-dir notes/actions-43657785023-1-general_pure_J_membership \
  --d0-dir notes/actions-43659795254-1-general_pure_D0_membership \
  --point-dir notes/actions-43672582314-1-character_minus2_raw_positive_candidate \
  --max-seconds 240 \
  --memory-mib 1024 \
  --integer-bits 8192 \
  --max-terms 80000 \
  --max-IBP-calls 250000 \
  --max-cache-entries 250000 \
  --max-shuffle-entries 100000 \
  --checkpoint-every 4 \
  --output "$OUT/character-head-word-relations.json"
~~~

新人工：

~~~sh
python scripts/literature_character_head_word_relations.py \
  --toy-only \
  --output "$OUT/character-head-word-relations-development.json"
~~~

真实入口自身要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY 准确为 Rogerhu12/math-research-public。没有在本地设置这些变量运行研究目标。$OUT 只由该公开 workflow 指定。

若从已发布 partial 继续，再追加 --resume-dir、--resume-main-sha256 和 --resume-publication-sha256。若在已切指定点后为了下一完整关系任务继续，必须明确 --finish-all-77；该开关沿已存 cursor 继续，不重做前缀。

六个 notes 输入目录需加入这条 lane 的 sparse 依赖；scripts 中仅新增两个文件。旧 consumer、输入证书和旧 workflow 计算不重新运行。
