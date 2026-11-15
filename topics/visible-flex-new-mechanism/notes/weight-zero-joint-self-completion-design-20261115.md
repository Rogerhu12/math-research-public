# 权零 C4/C6 的最后两个完整 pure/self 门：最小消费设计

日期：2026-11-15。状态：新源码与八项新接口人工已写成，**均未执行**；首次语法检查、人工与研究只在本公开仓库 Actions。本文是待执行设计，不预报成员或非成员。推导及源码：tail_cost；root 负责独立阅读、唯一 Git 发布与 Actions 调度。

新源码：scripts/literature_weight_zero_joint_self_completion.py。建议 lane：weight_zero_joint_self_completion。本文不改已冻结 R316 driver 或 self helper。

## 1. 已付结果之后的两个准确目标

使用 R196 的真实权零空间及 R126 原 old-column 编号：

\[
U^{(0)}=R^{(0)}\oplus
\operatorname{span}\{C_2,C_4,C_6\},\qquad
\dim R^{(0)}=16.
\]

三个 normal 根的状态键依次为
\((0,2,0,0),(0,4,0,0),(1,1,1,0)\)；它们都是 F0 同一八参考 \(\Gamma\) 规范化后的完整原根。这里 \(R^{(0)}\) 表示真权零，不与全权 pure 核 \(R\cap\ker\pi\) 混用。

R201 已证明
\[
\pi U^{(0)}=\pi R^{(0)},\qquad
\dim\pi R^{(0)}=3,
\]
其真实 pure 基是 R126 old 标签 \(0,2,3\)。R316 已完整计算全部
\[
R^{(0)}\cap\ker\pi
\]
的 13 个原方向之 full-self 像，真实秩为 7；其报告完整保存有序矩阵 \(\mathbf T\) 与整个局部 Euler 多项式。R316 还给
\[
H_*=C_2+\sum_j b_jR_j,\quad
\pi H_*=0,\quad\mathcal Q(H_*)=0,\quad\lambda_+(H_*)=1.
\]
本次不重复 H 或其中任何旧 self 方向。

记
\[
E=(\pi,\mathcal Q),\qquad
\mathscr C=E(U)/E(R).
\]
R323 已证明整个 joint 闭成本锥等于 \(E(U)\)，而其零权商最多只剩
\[
\mathscr C^{(0)}
=\operatorname{span}\{[E(C_4)],[E(C_6)]\}.
\]

因此本次只问两个完整成员问题：
\[
\boxed{E(C_4)\in E(R^{(0)})\ ?\qquad
E(C_6)\in E(R^{(0)})\ ?}
\tag{1}
\]

先由已存 pure 坐标得到唯一三基校正
\[
\pi C_i=\sum_{j\in\{0,2,3\}}\beta_{ij}\pi R_j,\qquad
H_i=C_i-\sum_j\beta_{ij}R_j\in\ker\pi.
\tag{2}
\]
再判
\[
\mathcal Q(H_i)\in\mathcal Q(R^{(0)}\cap\ker\pi),
\quad i=4,6.
\tag{3}
\]

这不是仅比较最高 jet、单个母函数、平移族、端层、某个固定圆或 partial \(\mathbf T\)。R314 的完整 \(\mathbf T\)+Euler 忠实坐标参与。

R122 的 \(R+\operatorname{Orb}(G)\) 真实查询控制不会被误用来直接跳过 C6。该文 §7 明确允许其他商分量同时改变；\([C_6]\) 属于平移像本身不证明 (1)，也不自动消除 R206 的完整基准义务。

## 2. 新运算清单与旧运算复用

本次新增科学范围严格为：

1. 必要恢复 C4、C6 两个完整 mixed 原根，分别核 R196 原 SHA。
2. 必要恢复一次 16 个缺失 R126 mixed 原输入，逐根核旧 SHA。没有 portable 原 DAG；这是候选原复合差所需的输入恢复，不是重做 16 个 self 目标。
3. 只映射两个新 \(H_4,H_6\) 的完整 self。
4. 对读入的 13 个已存 faithful 向量作一次仅服务于两个新 RHS 的精确因式分解；已发表秩 7 用作一致性检查，不另报告旧秩为新结果。
5. 每个阳性目标至多另作一次独立 mapper，对其完整原 mixed 复合差核 \(\mathbf T\)/Euler 零和 whole-word 重构。

不执行旧 13 个 self 映射、旧 Euler 展开、旧 pure 正规化、旧 profile 或幂尾评价、R196 完整头部秩、旧 3974 forcing、任何新 N 收缩、H 的再验证或任何旧开发套件。

新源码只 import 冻结 R316 driver，继承原 reader 与 R314 helper。标准库新增网络输入接口只读取一个已完成 public job 原日志，不能 dispatch/rerun、写 ref 或访问新的科学目标。

## 3. 完整比较空间确实可以复用

### 3.1 R316 原报告包含完整列

唯一完成来源：

- run 43735872441；
- job 132878270740；
- source ca186db057ed753abe565d0c3c2c8305278b5af7；
- lane weight_zero_complete_self；
- receipt 路径 notes/actions-43735872441-1-weight_zero_complete_self/receipt.json；
- receipt：55780 bytes，SHA256
  8d79ddda157153788ae70bb1cc44d6c64d4672541bb2e66f7cfbaf33f9549701；
- 原主报告 weight-zero-complete-self.json：61441 bytes，SHA256
  731ffae43cc8f06346801c444a7de010fe2cf6f9f05ecf4b650d319fa2ee06fd。

已静态核冻结 driver 的 public_column 与原公开报告格式：columns 中每一列保存

- ordered_matrix_T：全部九个有序项；
- complete_local_density：完整局部四次密度；
- complete_Euler_coefficients：整个六 jet 三次 Euler 多项式；
- local_density_sha256、Euler_sha256、faithful_coordinate_sha256；
- 原 mixed、全局同色、whole-word、self-word 身份；
- whole-word 从 T 与局部密度重构为零的准确声明。

complete_response_pure_kernel.new_kernel_coordinate_columns 又保存全部 13 个原 R126 old 组合。它们的非主元标签为
\[
1,4,5,7,8,9,10,11,12,13,15,17,19.
\]
每列在自己的非主元上系数 1，其他项只在原 \(0,2,3\) 基列。因此它们是整个 13 维 pure 核，不是某个方便的 Z 子空间。

完整比较坐标在 61441B 主报告内；**不需要未归档的 95310B 内存 certificate**，也不把旧 rank=7 这个单一数字冒作可求解的基。

### 3.2 原日志只在 runner 内存消费

新 driver 用 GITHUB_TOKEN 对 GitHub API 读取原 run、job 元数据，核源提交、run/job、lane、completed/success。随后只 GET 该 job 原日志。API credential 仅送 api.github.com；所有后续 signed-log redirect 不带 Authorization，最多四跳、日志最大 8 MiB。

解析只剥每行的 Actions 时间戳、ANSI 包装及行首 BOM。找到唯一对应 schema、带 decision 的 COMPLETE_REPORT 后，用**原 JSON 子串加一个 LF**核 61441B 与上述 SHA，而不是用重新格式化的 JSON 代替原字节。

还核主报告全部旧 source leaf 对原 receipt，及其 source_hashes 与冻结 R316 reader 身份一致。读取完成后，日志、原列与数组均只留内存；不复制进仓库、Release、artifact 或新 input 常量文件。

网络/来源错误在 phase=read_completed_comparison… 如实失败。不得因旧日志不可取而重做 13 个旧 self，也不得只用摘要 rank 猜列。如果需要修复，只能另安排原输入读取，不默认重跑旧科学。

## 4. C4/C6 的 pure 校正完全来自已存数据

### 4.1 两个同 Γ 完整 packet

R124 已发布的 normalized_static 完整 packets 使用同一
\[
F_0(S)=L_0(S)-\Gamma m_0(S).
\]
其证书已包含每个完整几何系数的 pure \(m=8\) 多项式。只读取 C4、C6 对应的状态键；未做任何 profile 代入。

来源：

- run 43649160345；
- source c69562728ce9d0f5115ad2710d45bcff15762693；
- lane constrained_static_m8_tail_quotient；
- main constrained-static-m8-tail.json：7892B，
  297c6716a7cf23d1c6006a273f251640bc4c0da878da07d68ef981af43ba65b7；
- receipt 32633B，
  8b8e3aff681ccbb15a879040d4a69aad94900b00eadae0130571c36b9b18679e；
- certificate gzip 57845B，
  022cd4f767d40b5ad21089e4cf88f7f6d4e6e051b7d730c038e87ab0e0961175；
- raw JSON 489034B，
  ced7357546b2c85610cf200e961c4e568a7a8f53407bf8da033eee8b9cb86ed7；
- 原 driver 28580B，
  8b075b222a1c8ea5579645905f9f3c3efc57a1b286a393cdcd597f384db50417。

groups.normalized_static.geometry_coefficients 是已完成的完整列表。原 producer 只删除 empty packets，所以没有某个状态键时，它在该完整列表中的 polynomial 准确为零；新 reader 标明这一情况，不把未完成当零。

### 4.2 为什么三个值足够且不混权

采用原 \(q=(c-x)^8,\ r=c-x\)，只读
\[
[c^0r^{32}],\quad[c^1r^{31}],\quad[c^2r^{30}].
\tag{4}
\]
四次真权 \(\sigma\) 的这些多项式总次数是 \(32+\sigma\)。因此 (4) 自动选择真权零，不混入该 packet 其他权，也不需要对旧 packet 再计算投影。

R116 已发布的权零 pure 响应秩恰 3，(4) 是已付的三个主元查询。R201 又证明整个 \(\pi U^{(0)}\) 等于该三维像。因此在这个**已证明的像**上，(4) 忠实。

旧 16 个响应的这三个值仍沿 R234/R316 的 read-only reader，从 R116 完整 certificate 读取。对两个新目标，只解同一个三乘三已知基坐标转换，给 (2)。这是读入系数的换基，不重新求旧秩、不执行旧 pure 原式评价，也不把三查询当成一般 profile 充分门。

新输入互相使用同一 canonical −4 归一化。R124 的完整静态 packet 与 R116 的响应 packet 已在原 producer 的完整原 polynomial 差式中匹配，不能局部再乘一个 16。

## 5. 两个 mixed 原根与必要输入恢复

C4/C6 的旧原身份来自 R196 job132712596579 的原完整 25121B stdout。已只读提取、核 SHA
838266c7b4b86b137482127e7e874d8d3eb014aa5745b9be6fceb2d9d3dc7fa4。

| 根 | 状态键 | mixed −2 SHA256 |
|---|---|---|
| C4 | (0,4,0,0) | 1d67672bb734f602675f84768b8afd62363d3742ca203ea01b23c9b1f3f0b592 |
| C6 | (1,1,1,0) | 5ca598f50107cf8f059608f27694ad87bb5cbd26be152ff18d8d0f2e2a95bc02 |

相应 pure 原 SHA 已在 R201 source 固定，分别为
5d70abb9d4000f457beb9d5d6d0adbf08f19becb953818f362c62b5c04dbb3e9 与
c074cfef87ff0f7b9435092bfce4615b7de12d2cbe4a0eabcb1a457d17b01044。
本次只把它们作为来源标记，不恢复 pure 根、不再正规化。

真实 mixed 恢复沿冻结 prior.restore_C2_and_W 的同一装配原则，目标改为 C4/C6：

1. 仅读旧完整静态 L0/W 导出的必要 roots；
2. 先按全部八参考态组合同一 \(\Gamma\)，保 reference 减项与 log 规则；
3. 合并后只作这两个必要 true-weight0 原投影；
4. 分别核上述旧 mixed SHA；
5. 所需 W 根与 16 个 R126 mixed 根按原 old 标签恢复一次并核旧 SHA。

没有先模 W 替换第三势，没有重新编 forcing；恢复的原响应只用于组装两个新 H 和阳性时的 fresh 原差。

## 6. 两个新 faithful 向量与一次复用求解

self helper 不变。对每个 H_i：

- 原 qbar 在所有 nested primitives 内全局识别为同一 q；
- 原右锚积分、三角对角项、真实左常数完整保留；
- 完成规范转换后才令外 local jets 为零，并取原 mixed 的 \(-[x^2]\)；
- 得到 \(q=\mathcal N_T+\int L\)；
- 完整 word 重构准确为零；
- 保存整个 Euler(L)，而不是只最高 jet。

对 13 个旧列只执行反序列化与 hash 核对。旧 local/Euler 不重新微分，不调用旧 self mapper。

为了给两个新 RHS 求有理组合，一次 factorization 读入的 13 个 faithful 向量。旧 rank 7 作为一致性前提核对，不把它当作本次新秩成果。两个 RHS 共用同一 basis；非成员时加入的目标列不污染另一个目标的比较空间。

阳性先核全部读入 faithful 向量的准确线性和。随后合并 pure 校正与 13 核列的原 R126 组合，形成
\[
D_i=C_i-\sum_j a_{ij}R_j.
\]
三个已存 pure 值准确为零；R201 的已付忠实性给 \(\pi D_i=0\)。

再从完整原 mixed 根重新组成 D_i，用独立新 mapper 核
\[
\mathbf T(D_i)=0,\qquad
\operatorname{Euler}(L_{D_i})=0,
\]
以及整个原 word 重构。R314 从这两组零授 \(\mathcal Q(D_i)=0\)。**不额外要求 self NF 字面零**；若本次恰为零，作为实际字段记录而非一般成员门。

阴性给一条确切 T/Euler 有理对偶，直接核对全部 13 个旧向量为零、新目标为 1；因此是真实函数非成员，不是某个不完备 NF 的余项非零。

全部组合继续用 R126 old 标签，不把 16 紧缩位置、13 核列位置和原 old 编号混淆。主报告同时输出核列系数与完整 old 响应系数。

## 7. 两种结果对主线的准确意义

若两个目标均 MEMBER，结合 R316 的 C2 成员和完整 U0/R0 基：
\[
\bigl(E(U)/E(R)\bigr)^{(0)}=0.
\]
R323 已有 joint 闭锥满；R206 的真实缩放、零矩/frame 桥、真倒行、两次紧商截面、整数复制和末次响应校正遂适用于 E。这给实际有限同时支付**全 universal pure 与全 universal self**的接口，而非仅固定母或有限中心。

该应用仍须在人类结果稿按原构造说明实际 word、完整基准与选择顺序。程序只标记已满足该已发表充分门，不把有符号响应组合本身直接当作实际字。

若一个目标 NONMEMBER，本文只判 (1) 中对应门失败。它不证明 actual joint 控制不可能、不构造正字符，也不允许把 R323 闭锥满提升为 actual 半群满。下一步须对尚存零权商给别的真实控制来源。

不论结果如何，完整成本 \(U\) 的 signed 控制、某一固定圆的两 mixed 整函数、同一二阶 gauge 的 period/ruling 联立、曲面完工条件均未自动支付。\(\lambda_+\) 在完整成本上的严格长度正性保持有效。

## 8. 首次公开开发范围

只有八项新接口人工，均不读研究输入、不联网、不调用旧 mapper：

1. 原 COMPLETE_REPORT 的 BOM/时间戳剥离、原字节 SHA、重复/篡改拒绝；
2. 旧完整 T/Euler 的反序列化与 hash，不重算 Euler；
3. 既存同 Γ packet 的三个 degree32 系数，其他权隔离及完整零 packet 缺项；
4. 两个新 RHS 在已知三 pure 基上的准确坐标转换；
5. 一次 stored-coordinate factorization 上两个 RHS，含非单调主元、阳性与完整对偶；
6. 13 核位置到 R126 old 标签的准确组合；
7. 假 API redirect 的 token 边界，绝不发送网络；
8. 原 nested source leaf 与 receipt 的逐项来源匹配。

没有声称这些人工已经 passed。首次 syntax compile、八项检查与实际都由新公开 Actions 执行。

## 9. 资源、输出与失败语义

默认数学上限：

| 项目 | 上限 |
|---|---:|
| 总进程研究秒数 | 240 |
| 内存 | 1024 MiB |
| 有理整数位数 | 8192 |
| 表达/word 项 | 100000 |
| 新 primitive 调用总数 | 300000 |
| 缓存项 | 250000 |
| 主摘要 | 95000 bytes |
| 新内存 proof | 4000000 bytes |
| 旧原日志输入 | 8 MiB |

共享两目标 mapper 与最多两个独立 fresh mapper 共用总 primitive 预算。原输入读取也占进程 elapsed；报告另记原日志读取耗时，不能称所有耗时均为新符号运算。

literal monitor 的 operations/maximum_bits 不代表整个 DAG 全部算术，字段明确保此范围。

成功 stdout 输出两个完整决定、每个新 T/Euler 原列、全部准确响应组合、fresh 身份及 COMPLETE_REPORT。主摘要超限时改为明确 summary_output_limit，不在截断内容上宣布完成。数学或输入预算失败只报告实际进度，不伪造零值、成员或可恢复 cursor。

新 proof、旧 log 和所有数组仅在 runner 内存；主 JSON 仅写 @OUT@ 临时目录供 metadata-only publisher 记录字节/SHA。没有 artifact、Release 或 repo payload。

## 10. 复现 CLI 与最小接线

开发：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_weight_zero_joint_self_completion.py \
  --toy-only --max-seconds 30 --memory-mib 256 \
  --output @OUT@/weight-zero-joint-self-completion-development.json
~~~

实际 32 个参数字符串：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_weight_zero_joint_self_completion.py \
  --static-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient \
  --R0-directory topics/visible-flex-new-mechanism/notes/actions-43649525432-1-g_first_translation \
  --head-directory topics/visible-flex-new-mechanism/notes/actions-43681388902-1-character_head_zero \
  --pure-identity-directory topics/visible-flex-new-mechanism/notes/actions-43683171512-1-character_zero_pure_readout \
  --stored-pure-directory topics/visible-flex-new-mechanism/notes/actions-43646543691-1-full_m8_tail_response_projection \
  --static-pure-directory topics/visible-flex-new-mechanism/notes/actions-43649160345-1-constrained_static_m8_tail_quotient \
  --completed-self-directory topics/visible-flex-new-mechanism/notes/actions-43735872441-1-weight_zero_complete_self \
  --max-seconds 240 --memory-mib 1024 --integer-bits 8192 \
  --max-terms 100000 --max-IBP-calls 300000 --max-cache-entries 250000 \
  --max-summary-bytes 95000 --max-certificate-bytes 4000000 \
  --output @OUT@/weight-zero-joint-self-completion.json
~~~

旧五目录保留，R124 目录已经在 continuation sparse list；唯一新增 checkout 目录是 R316 receipt 目录。运行步骤只为本新 lane 暴露 github.token，且 workflow 已有 actions:read；原研究实际 pull、双 README/private QUEUE 规则读取及 metadata-only 发布流程不变。

六处 workflow 小改：allowlist、R316 sparse 目录、该 lane 的 read token、script map、toy flag、复用 self helper 的 syntax list。两处 publisher 小改：允许新 lane、将其标为无候选几何的完整研究编译。没有更改旧 lane 数学、容量、预算或验收。

新 request 为单 lane，不再运行旧 R316 请求；旧请求永久由其 source 保留。34 个直接源码绑定包括旧 30 个科学源、新 driver 和 workflow/publisher/printer 三项。所有哈希随冻结小文本给 root，不在源码硬编码可重算旧 payload。

## 11. 交付身份

冻结新 driver：

- filename：literature_weight_zero_joint_self_completion.py；
- UTF8：50185 bytes；
- SHA256：1f5d671598ca6fc4a804c6f22a65d145b5ced3743506a2144d507717ff4789d3；
- Git blob：6d578bd9f34b03138a17025829c61da7204be6b6。

新源码、参数与接线 blob 尚未挂任何 ref。本设计未执行人工、研究、语法检查或新的 profile 求值；发布和首公共运行由 root 唯一进行。
