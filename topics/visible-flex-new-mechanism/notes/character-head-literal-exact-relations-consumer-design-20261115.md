# 完整权 −2 呈示的原始字面有理关系消费器

状态：**新源码与人工开发检查；真实 147 列尚未运行。** 本文不登记新的函数空间维数、真实成员关系或正字符存在结论。真实消元只在本公开仓库的 GitHub Actions 运行。

实现文件：scripts/literature_character_head_literal_relations.py。输入是已公开的完整 head 原始表达式和已公开的外部必要系统坐标；新增工作只有同一原始 DAG 上的一般有理列关系、每条关系的原式核零，以及这些关系在已有坐标中的表达。

## 1. 原函数关系是这次的具体目标

R163 已给出十四族的完整单权呈示。首次实际输出保存 107 个 normal 系数记录、66 个平移关系记录和已有 40 个真实响应原列；107 是生成记录数，不是维数。旧 finite consumer 只加入字面零、两列比例、平移与协变等已经取得的必要关系，得到 23 个外部坐标，尚未计算这 147 个原列之间的一般字面有理依赖。

R168 的全部错误二次奇偶已经公开加入。R172 又给出当前外点最高层的精确 Gram 平方证书和完整二阶层的正定平方证书。保持这些层而使静态层全非负的外部点可能通过所有路径不等式；还必须检验它是否尊重真实原函数关系。

本次先付清最便宜而完全 sound 的一层：**共同右锚、共同 profile atom DAG 的完整原系数逐项抵消。** 不做新 IBP，不把非零字面余式当作非成员，不假设右 Volterra primitive 可独立赋值。

## 2. 精确输入和来源绑定

### 2.1 完整 head 原式

公开 run **43665345551**，source commit **0aae9a6a85583a9f87415e586d8db2c9c7fea6a7**，lane character_head_minus2。目录：

notes/actions-43665345551-1-character_head_minus2/。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| character-head-minus2.json | 15967 | 55320985df05f928caf007016777ecb2413f16c969dca4741b0c2e936f00b940 |
| receipt.json | 39451 | 88bdcf2dadbba25d816e886705b70e7844f698f07917b696698e86ea2770f675 |
| character-head-minus2-original-expressions.json.gz | 1247411 | 2c1242e13d253ba352c7ff1b025a91cf564ab2a7cfd93c6bcedc19baa5fac45c |

raw 为 6560138 字节，SHA256 为 7a93a53aa7fafa1cff76608aceaeac294911ca4f828746913c1b125ae2fd33af。原 producer 为 literature_character_head_minus2.py，58856 字节，SHA256 fcc41b4d5a640a1ac411e7f6f29622db81c39cb2be37aed7811136418a045f11。

只接受这份完成所有十四族、所有计划收缩的完整原式。main、receipt、source producer 和 gzip 的 packed/raw 身份全部交叉核对。完整 head 的旧源码不改。

### 2.2 已有外部坐标

run **43665971895**，source **05bb659b59997906316ddd2873aedbf4840f62a5**，lane character_minus2_finite_necessary。目录：

notes/actions-43665971895-1-character_minus2_finite_necessary/。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| character-minus2-finite-necessary.json | 10143 | 1e8d751fca7fb6d8b2c33d1152e8651399824be22ffad5496c8bdb48de7fef6c |
| receipt.json | 40026 | 6fbdf4f3c98bfa14fe6344d988a5df9acad10b4c7e598711aa3f5b57c8515764 |
| character-minus2-finite-necessary-certificate.json.gz | 31976 | 5658e056313fff939356f91c97578a8dfc3e1158661b209c84ba7d2b86aa3634 |

raw 为 143028 字节，SHA256 dd539b088c354d99c04af46d8d7c63822679f13ebc02b14a673c76767fd745f7。producer 为 45116 字节、SHA256 d4c3751cf58f1ef08c534e61a16d7a40cd368980c0cca0ef48a0bce505ce3545。

只读已保存的 normal_coordinates_as_free_linear_forms，即 $\nu=By$，以及 normal107 的语义元数据；后者必须逐条等于 head 的 normal_family_records。旧 124 个等式、84 行 RREF、63 个半空间及六条路径积分均不重做，只保留原内容哈希。

### 2.3 已发全部奇偶和原外点

run **43668125602**，source **c8a89721ee361074096b202af6aa0841ac1bc445**，lane character_minus2_static_parity。目录：

notes/actions-43668125602-1-character_minus2_static_parity/。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| character-minus2-static-parity.json | 6971 | bb2e66e4ddd6e0e826c8aa78cef96462e23290852f512b84ab0d3fceb800f968 |
| receipt.json | 40112 | 947bbcd35c08476233568a67c8f6b4c322bf8991284b8c9382fc65fea2ccd6d2 |
| character-minus2-static-parity-certificate.json.gz | 9222 | 2431172cb890ad9d6bc7fa227793fabd9a33e5f254531ff2411b6fbc6870e3af |

raw 为 34807 字节，SHA256 f15004c94a2400bf9fed2e9705227ba2cd1ca2dacc38080a25bf703e9f27ef23。producer 为 18508 字节、SHA256 9e7f7d2b9b70b78a3eec17f8c4c2e4cd64caf8d6304247355aaff55c962f41e1。

只消费 complete_quadratic_parity 的四个已发等式和 decision.outer_candidate。新消费器不重新评价 68 个半空间，不运行 LP，不做静态多项式分离。

## 3. 147 列和两模式的准确含义

证书列号先列 R40，再列 normal107：

$$
(C_0,\ldots,C_{146})=(R_0,\ldots,R_{39},V_0,\ldots,V_{106}).
$$

R40 使用 archived_R_basis_records 的已有顺序，其原下标为 0,…,23,25,27,28,29,31,32,33,35,36,39,40,41,46,47,48,49。不重选或重证旧响应基，也不生成其原式。新增的是把这些已保存列放入**同一完整原始系数矩阵**，作为 normal 关系的分母。

每列是 $(C_{j,-4},C_{j,-2})$。一行的完整标签是

$$
(\mathrm{mode},\ \xi\text{ 的幂},\ \text{原 atom 编号多重集}).
$$

两 mode 绝不合并。q、qbar 和所有右 Volterra 原子保持原定义、完整相位与共同右锚；没有 pure 代入、幂尾、profile 数值或几何路径。

只读已发 metadata 得到选中列共有 294 个根和 204687 条 term rows，其中 normal 为 171564 条，R 为 33123 条。每个选中根按原 portable DAG 协议重算原 hash：jet 直接哈希，右积分 atom 按拓扑子原子哈希，根按排序 rational rows 哈希。这只检查已保存内容，不编译新表达式，也不调用旧研究模块。

## 4. 精确列消元和独立原式核验

取所选系数分母的正最小公倍数 $L$，同时把所有原列乘以 $L$，得整数列 $A_j=LC_j$。共同 $L$ 不改变有理关系。

处理顺序为 R40、normal107。每个活动列同时保存整数向量 $v$ 和原列整数系数 $a$，保持

$$
v=\sum_j a_jA_j.
$$

若当前最低非零行和已有基列的 pivot 相同，分别记 pivot 值为 $v_p,b_p$，取 $g=\gcd(|v_p|,|b_p|)$，同时更新

$$
(v,a)\longmapsto
\left(\frac{b_p}{g}v-\frac{v_p}{g}b,\
\frac{b_p}{g}a-\frac{v_p}{g}a_b\right).
$$

之后只可同时除以向量和证书全部整数的共同 gcd，并统一符号。没有浮点 rank 或模素数候选。

非零余列只成为这个字面矩阵的基列；由于积分原子可能有真实恒等式，不据此宣布真实函数独立或目标非成员。

余列为零时也不立刻登记。先把证书规范为 primitive 整数向量，再从原 gzip 的有理 rows 独立相加，分别计算

$$
\sum_j a_jC_{j,-4},\qquad \sum_j a_jC_{j,-2}.
$$

原核验使用原 monomial 键，不使用消元的整数 row-id 向量。只有两 mode 的每一个原系数都精确为零才接受；共同 $L$ 只用于整数累加。若 R40 内竟出现这样一条关系，报告实现检查失败并保留状态，不悄悄与已发表的真实独立性并列。

通过核验的关系是完整原算子的恒等式，不依赖 primitive 自由、不完备 normal form 或采样。每条证书明确保存 147 个系数及两 mode 零证。

若 147 列全部处理完成，每个非基列关系具有自身系数非零、只涉及自身和先前列的三角形式，因而构成**该字面系数矩阵**的完整核基。其核维数等于 147 减字面基列数，但不是完整真实函数关系核维数。

## 5. 新外部等式的准确接口

将一条已核验关系写为

$$
\sum_{i=0}^{106}a_iV_i+\sum_{j=0}^{39}b_jR_j=0.
$$

真权 −2 字符杀 R，故必须满足 $a\cdot\nu=0$。用原来 $\nu=By$ 得

$$
(aB)y=0.
$$

保存三个层次：

1. $aB=0$：旧坐标映射已经包含，不新增行。
2. $aB$ 由已发 R168 和先前新原式关系推出：完整原证书保留，后继必要系统不重复加行。
3. 对上述行仍有余式：给出一条新精确等式，可加为正负两条半空间。

这里至多 23 维的小有理消元只给新行去重，初始只插入已发 parity，没有重做旧 124 个等式或 84 行 RREF。输出每条关系的全部原列系数、normal 行、old-free 行、约化过程。后继 solver 应加入 old_free_coordinate_equality 原行，不猜一个新的自由坐标解释。

原 66 个 N 像关系从原坐标映射继承；本次不生成任何新的 $NV$ 原目标。实际新关系可能只减小外部空间，也可能支付一个具体商类，须按实际结果分别说明。

## 6. 明确指定点及其结论边界

默认诊断已发 static/parity 外点。加 --diagnose-half-static 后，再诊断同一个明确向量：复制已发点，只将 free[12]=normal73 对应的 $y_{12}$ 改为 $-1/2$。

纸面读取旧线性行得到只改 normal0、1、9、10、73；corrected 十四族中只改静态常数和二次项，新静态多项式为

$$
a(k)=\frac12-\frac32k^2+k^4+k^6
=(k^2+2)(k^2-\tfrac12)^2+\frac14k^2>0.
$$

R172 的 Q2 和最高层平方证书保持。独立指定点 actual **43669803169**，source **7d29631406407408e7fed52fdbc014e036d5a6ab**，已检查其全部 68 行、完整十四族和同一 $\mu,c,d$：68 行全满足，只有 64–67 为零，其余 64 行严格正。目录为 notes/actions-43669803169-1-character_minus2_static_positive_candidate；完整证书 9305 字节，SHA256 b5b3dacf8d8078c069f73567e82fc8bcbe2bb411bf1bbe057ac0c360a9f49122。

这已是一个准确验证的**外部系统可行点**，但还不是已实现的真实泛函。新消费器不额外读取这第四份数据、不重验 68 行；它从旧已发 y 的明示单项修改定义完全同一个向量。源码中的 not_asserted_realizable 标签仍准确指真实泛函未证。

每条新原关系保存该点的精确值；非零值足以排除该点来自尊重此原式关系的泛函。全部为零，只说明本次已取得的字面关系没有排除它，不能证明真实正字符存在、成本锥 proper 或 period 不可支付。

诊断配置进入续算身份。若未来诊断其他点，直接消费已发新等式即可，不为换点重做 147 列。

## 7. 有限预算与真实续算

默认 240 秒、1024 MiB、8192 位精确系数；每 8 个完成列和每条新依赖后保存状态。每个 gzip 不超过 4400000 字节，main 不超过 95000 字节；main、关系证书、状态合计不超过 4800000 字节。单份 raw 上限 40000000 字节。

状态保存已成基列的原组合和精确向量、已成关系、当前活动列及其原组合、原核验的已加列前缀和累加器。每个消元步骤或原列相加先在临时对象完成，预算通过后才替换有效状态，不把半步当完成。

通常保存显式向量；必要时保存各状态向量的**原列精确整数线性组合及对应向量 SHA256**。续算只按固定组合重新物化状态并核 hash，不重新做已成 pivot 消元，也不生成或评价旧响应。原核验累加器仍明确保存，未完成核验不能标成已证明。

续算要求同一脚本 hash、原输入、inherited view、诊断配置，以及公开前次 main/receipt/state 的真实 packed/raw 身份；只从 complete 或 resource_limit 的有效状态续算。实现检查失败不能自动恢复成研究成功。

若最新状态因输出上限不能保存，必须准确报告最后有效状态的列数、阶段与操作计数，并令 latest_new_progress_has_a_saved_exact_state=false。绝不假装完整计算或完整保存。已完成原式关系仍独立给出准确证明状态。

## 8. 输出与后继接口

主 schema：visible-flex-character-head-literal-relations-v1。

- character-head-literal-relations.json：小报告，输入身份、完成前缀、原核验关系数、新等式数、指定点首批违反值及 packed/raw hash。
- character-head-literal-relations-certificate.json.gz：完整 147 列语义、所有依赖的 dense_147_original_coefficients 和稀疏同值行、每条两 mode 原零证、normal/old-free 行、新行索引和诊断值。
- character-head-literal-relations-state.json.gz：可以从具体新状态继续的精确消元状态，不冒作函数空间研究结论。

后继 solver 用 new_equalities_for_the_inherited_23_coordinates 指向 original_dependencies 的记录，读取其中 old_free_coordinate_equality。它始终使用原 23 个 $y$，没有重定义自由坐标；仍须核新 main、receipt 和证书的来源身份。

## 9. 人工检查和公开实际命令

本地九项新增人工的原回执对应58210字节源码ae72b9fa738f2b4620ac89fa623e0fb3b1a276d1ba9f574e71dd600af8cdaf48，保存在character-head-literal-relations-pre-final-artificial-20261115.json。随后仅把诊断配置加入续算身份并补最新保存进度元数据，形成最终58885字节源码80ab553a2dbb35fd4547beaf1b7ad094e831a2cb7f02e4968b867c4654cd9995；不把旧回执称作最终源码实跑。公开lane先在最终源码执行同一小人工入口，通过后才运行本次新147列。

新人工只用自造的一条 R 和三个 normal 小列，检查有理分母、两 mode 分离、三角关系、伪造余零拒绝、旧 B 投影、显式和紧凑的列内/原核验续算、来源变更拒绝、portable 原 hash 与位数预算。不打开真实目标文件，不运行旧研究测试。

~~~bash
python -m py_compile topics/visible-flex-new-mechanism/scripts/literature_character_head_literal_relations.py
python topics/visible-flex-new-mechanism/scripts/literature_character_head_literal_relations.py --toy-only --output literal-relations-development.json
~~~

真实命令仅用于本公开仓库 Actions：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_character_head_literal_relations.py \
  --head-dir topics/visible-flex-new-mechanism/notes/actions-43665345551-1-character_head_minus2 \
  --finite-dir topics/visible-flex-new-mechanism/notes/actions-43665971895-1-character_minus2_finite_necessary \
  --parity-dir topics/visible-flex-new-mechanism/notes/actions-43668125602-1-character_minus2_static_parity \
  --diagnose-half-static \
  --max-seconds 240 --memory-mib 1024 --integer-bits 8192 \
  --checkpoint-every 8 \
  --output character-head-literal-relations.json
~~~

若需要续算，在完全相同输入命令后加：

~~~bash
--resume-dir topics/visible-flex-new-mechanism/notes/actions-<run>-<attempt>-character_head_literal_relations \
--resume-main-sha256 <published-main-sha256> \
--resume-publication-sha256 <published-receipt-sha256>
~~~

新 sparse 依赖仅以上三份已发实际目录和脚本目录。不读取其他大数据，不复编 W、forcing、N2、原响应、纯尾或 mixed evaluation。

真实结果如切掉指定点，马上把对应原证书交给必要系统合并；如未切掉，就依完整依赖数据定位下一条真正缺失的原函数关系。原呈示关系表本身不是本课题完成。
