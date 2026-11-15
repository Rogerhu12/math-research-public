# 九条真实原式关系后的权 −2 必要系统增量

状态：**源码及新人工检查已完成；这份新必要系统的 LP 尚未实际运行。** 真实计算只由本公开仓库 GitHub Actions 执行。本文件不登记正字符存在、不存在或真实头部维数。

实现：`scripts/literature_character_minus2_literal_relation_cuts.py`。

本次只消费已经发表的原始两模式关系，把其中九条新等式加到原 23 坐标、68 个必要半空间中。完整 head、旧 124 等式及其 RREF、六条路径积分、原 147 列消元和旧 44 列查询均不重算。

## 1. 为什么现在接这九条关系

R173 的指定点已经准确满足全部旧 68 行，且其完整标量 action 有严格正下界。这仍没有证明该坐标赋值尊重真实 profile 函数关系。

公开 raw147 实际 **43670254711** 已给出 70 条原始两模式逐项为零的有理关系。指定点违反其中 18 条。最短的一条不含响应列：

$$
-V_0+V_1-V_2+V_3=0.
$$

因此任何真实泛函必须满足

$$
-\nu_0+\nu_1-\nu_2+\nu_3=0.
$$

在旧自由坐标中，这是 $-2y_0-y_2+2y_{12}=0$；R173 指定点的准确值为 $-2$。排除该点不需要新 profile 评价，也不需要把字面秩当真函数秩。

九条新等式在全部旧坐标与 R168 奇偶关系之外分别独立。其证书编号为

$$
0,4,35,55,62,64,65,66,67.
$$

本消费者逐条使用这些记录的 `old_free_coordinate_equality`，不把消元余行另定义为新的坐标系，不删掉旧 23 个变量。

## 2. 可直接读出的纸面加强及边界

令完整静态函数写为

$$
a(k)=\nu_0+\nu_1k^2+\nu_2k^4+\nu_3k^6.
$$

关系 4 减去关系 0 的九倍，在旧自由坐标中给 $-9y_1=0$，而 $y_1=\nu_3$。结合关系 0，任何真实字符必须有

$$
a(k)=(1+k^2)(\nu_0+\nu_2k^2).
$$

这排除了原指定点中被错误当成独立自由度的六次项。全部静态点态非负等价于 $\nu_0,\nu_2\ge0$；**本轮只添加九条原等式，没有额外添加这个无穷远必要半空间，也不启动新的静态 oracle。**

最高层采用 R165 的记号 $A=A_0+A_2k^2$、$B=B_1k$、$C=C_0$，并令 $a=h_{ss},b=k_{ss}$。关系 62 和 64 给

$$
B_1=-A_2,\qquad C_0=A_2/4.
$$

于是加速度部分化为

$$
A_0h^{-4}a^2+A_2(h^{-2}ka-h^{-1}b/2)^2.
$$

它的逐状态 PSD 门等价于 $A_0,A_2\ge0$。面积项、全部速度四次项、二次层和静态层仍在同一个旧十四族中；这不授整个 action 的正性。

另一个已核的旧接口是 $[N^3G]=6[V_{18}]\bmod R$，但旧 `normal_coordinates_as_free_linear_forms[18]` 已经是空行。故 $\nu_{18}=0$ 不作为本轮新增工作。

## 3. 三条准确输入链

### 3.1 原 68 行与旧 23 个自由坐标

保持 published static/parity run **43668125602**、source **c8a89721ee361074096b202af6aa0841ac1bc445**：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| character-minus2-static-parity.json | 6971 | bb2e66e4ddd6e0e826c8aa78cef96462e23290852f512b84ab0d3fceb800f968 |
| receipt.json | 40112 | 947bbcd35c08476233568a67c8f6b4c322bf8991284b8c9382fc65fea2ccd6d2 |
| character-minus2-static-parity-certificate.json.gz | 9222 | 2431172cb890ad9d6bc7fa227793fabd9a33e5f254531ff2411b6fbc6870e3af |

证书 raw 34807 字节，SHA256 为 `f15004c94a2400bf9fed2e9705227ba2cd1ca2dacc38080a25bf703e9f27ef23`。

该证书已有完整 68 行和同一自由坐标列表。它不含完整十四族的线性形式，所以同时消费它明确引用的最早完整系统证书：run **43665971895**，source **05bb659b59997906316ddd2873aedbf4840f62a5**。

`character-minus2-finite-necessary-certificate.json.gz`：31976 字节，SHA256 `5658e056313fff939356f91c97578a8dfc3e1158661b209c84ba7d2b86aa3634`；raw 143028 字节，SHA256 `dd539b088c354d99c04af46d8d7c63822679f13ebc02b14a673c76767fd745f7`。

这个读入链复用已公开 `literature_character_minus2_static_positive_candidate.py` 的纯输入 `consume`：同时核旧 RREF、变换 $\nu=By$、63 行前缀、全部路径积分及十四族原形式的内容绑定。不调用它的指定点、静态 oracle 或旧人工套件。

### 3.2 九条真实原关系

公开 run **43670254711**，source **952cf7927d809150ac2579f1a390225c2cf23f52**，lane `character_head_literal_relations`：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| character-head-literal-relations.json | 7103 | 0d3351e00b434292b7b8fce62ac74096ea0fbb96cdf78998bb096d29ab336055 |
| receipt.json | 41254 | 043a234f7cf4c8962d50edc69a441794f562041e2fbf334c8ad570335ae42d73 |
| character-head-literal-relations-certificate.json.gz | 41109 | 5d929f4f45265ee4eec949eace228bf4b639753cd0a4b24a8a3d32d0857dc62e |

raw 269605 字节，SHA256 `ed3bedb70a0f49a058daf578ff9403a7ff89407c55f0954f876bfedaeaeac775`。

原 producer `literature_character_head_literal_relations.py` 为 58885 字节，SHA256 `80ab553a2dbb35fd4547beaf1b7ad094e831a2cb7f02e4968b867c4654cd9995`。新消费者只读其发表回执和关系证书，不导入该 producer，不加载 profile DAG。

对每一条新关系，要求：

- 完整原 147 系数向量与稀疏向量一致；响应 40 列和 normal107 的切分无歧义。
- 原 normal 行及旧 free 行来自同一个已绑定证书。
- 两个模式都有已发表的 `remaining_terms=0` 与 fresh 原式核验标记。
- `new_equalities_for_the_inherited_23_coordinates` 的完整列表准确为上述九项。
- `inherited_view` 中的旧 B、RREF、68 行与本次消费的文件逐项 hash 相同。

这些是输入意义与内容绑定，不重做已完成原式求和或九条关系的旧坐标投影。

## 4. 唯一新增的必要系统

设旧 68 行为 $r_i\cdot y\ge0$，九条原关系投影为 $e_j\cdot y=0$。新系统为

$$
r_i\cdot y\ge0\quad(0\le i<68),\qquad
e_j\cdot y\ge0,\quad-e_j\cdot y\ge0\quad(1\le j\le9).
$$

新增行仅作正倍数 primitive 规范化和逐行去重。若某一有号行已存在，只引用旧行号，不增加其理由计数、不改变旧记录字节。实际新增半空间数至多 18，不提前把 86 当实际结果。

原自由坐标仍为

$$
(2,3,14,23,26,28,38,43,58,63,67,69,73,90,91,94,96,97,99,100,101,103,104).
$$

旧自由变量全部是原 normal 坐标，因此它们全为零会使全部 107 个生成记录为零。没有采用仅 $\lambda J=1$ 的不完整归一化。

### 4.1 真排除证书

对每个 $y_j$ 的正负两个单位向量，复用原准确 Farkas 核验：浮点 LP 只提出有理支持；只有准确非负有理组合

$$
\sum_i c_i r_i=\pm e_j,\qquad c_i\ge0
$$

逐系数成立时才登记。全部 46 个方向都取得真证书，才排除所有非零**正**权 −2 字符。它不排其他权，也不把非正字符一并排除。

### 4.2 外部点或未决

若双证未完成，保留已完成双证，并尝试得到盒 $[-1,1]^{23}$ 内的非零有理点。该点必须用 Fractions 精确通过全部更新行及九条等式，才标成新的外部必要系统点。

随后只对这个新点作用已保存的 $B$、十四族线性系数及同一 $\mu,c,d$，给出完整解释。旧 R172/R173 的 SOS 不自动移交给新点。新点全过仍不证明它尊重所有真实原函数关系，更不证明正字符存在。

若有理点恢复也未完成，报告未决。浮点可行、不可行或求解器退出状态均不升为数学结论。

## 5. 输出、来源和失败回执

主 schema 为 `visible-flex-character-minus2-literal-relation-cuts-v1`。

- `character-minus2-literal-relation-cuts.json`：小报告，旧输入与新关系完整绑定、准确新增行数、双证计数或新外部点解释、范围。
- `character-minus2-literal-relation-cuts-certificate.json.gz`：保原 68 行前缀、全部新增有号行、九条原关系及 source-record hash、46 个方向中的已成准确双证；若有新点，保存全 107 值、14 族及 $\mu,c,d$。
- `character-minus2-literal-relation-cuts-development.json`：仅本新消费者的小人工检查。

完整原始十四族和 B 不重复复制到新证书，保其准确 hash 与旧证书输入链。后继消费需要同时保留原有限系统证书。

默认总时限 180 秒、软轮询 512 MiB、16384 位有理系数。主报告上限 95000 字节；完整 gzip 上限 4500000 字节；总输出上限 4800000 字节。预期本次只有小型有理矩阵输出，不含新原 DAG 或研究轨迹。

若资源退出，已经组好的必要行可保存，排除结论保持 false。若完整数学证书未成功写出，不在小 fallback 中保留正性排除的成功标记。

## 6. 新人工检查

人工只构造一条假响应和两个假 normal 的小列证书，不打开任何真实输入，不运行 LP。检查：两模式原零标记、原系数向量一致、两符号加入、旧行去重不变、错误符号 Farkas 拒绝、全部十四个人工字段输出以及外部点范围标记。

旧 `rref`、`construct_system`、`path_integrals` 在人工中替换为报错函数，防止增量函数误调旧研究。该人工不重复旧 cubic oracle、原列开发检查或任何公开 actual。

## 7. 最小公开命令

先只执行新源码语法与新人工：

~~~bash
python -m py_compile topics/visible-flex-new-mechanism/scripts/literature_character_minus2_literal_relation_cuts.py
python topics/visible-flex-new-mechanism/scripts/literature_character_minus2_literal_relation_cuts.py --toy-only --output character-minus2-literal-relation-cuts-development.json
~~~

唯一实际命令，lane 建议 `character_minus2_literal_relation_cuts`：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_character_minus2_literal_relation_cuts.py \
  --source-report topics/visible-flex-new-mechanism/notes/actions-43668125602-1-character_minus2_static_parity/character-minus2-static-parity.json \
  --source-publication topics/visible-flex-new-mechanism/notes/actions-43668125602-1-character_minus2_static_parity/receipt.json \
  --source-certificate topics/visible-flex-new-mechanism/notes/actions-43668125602-1-character_minus2_static_parity/character-minus2-static-parity-certificate.json.gz \
  --original-system-certificate topics/visible-flex-new-mechanism/notes/actions-43665971895-1-character_minus2_finite_necessary/character-minus2-finite-necessary-certificate.json.gz \
  --literal-report topics/visible-flex-new-mechanism/notes/actions-43670254711-1-character_head_literal_relations/character-head-literal-relations.json \
  --literal-publication topics/visible-flex-new-mechanism/notes/actions-43670254711-1-character_head_literal_relations/receipt.json \
  --literal-certificate topics/visible-flex-new-mechanism/notes/actions-43670254711-1-character_head_literal_relations/character-head-literal-relations-certificate.json.gz \
  --max-seconds 180 --memory-mib 512 --rational-bits 16384 \
  --output character-minus2-literal-relation-cuts.json
~~~

实际入口同时要求 `GITHUB_ACTIONS=true` 与 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。新 lane 由 root 统一部署；本地仅作上述新人工。
