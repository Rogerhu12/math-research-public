# R796 原 CM 二次局部图的执行界面

日期：2026-11-15。此文件给 [R796 严格证明](../results/R796-original-CM-local-chart-from-quadratic-sections.md)
的实现契约，**不登记尚未执行的实际416列、矩阵秩或高阶系数**。
基础全球二次图也供 R793 的 $qP$、$272P$ 评价使用，
所以可先以 target_length=2 实际准备416列与144条准确关系。
只有新增高阶局部分支等待真实消费者要求；不先计算最坏长度155或290。

## 1. 核心入口与不可变配置

计划核心路径为 scripts/R796_original_CM_quadratic_chart.py。
结果标识为 R796-original-CM-quadratic-chart，
最终证书名为 p41-original-CM-quadratic-chart-certificate.json。

核心接受如下显式参数：

- --config：冻结 job JSON；
- --retained：下述 R786、R790 两组原输入目录；
- --output：此次当前任务的临时输出目录；
- --proof：R796 完整证明；
- --method：本执行界面；
- --rr-proof：R793 完整证明；
- --target-length：实际要求的有限局部环长度 $N\ge2$；
- --budget-minutes：只约束当前执行资源，不改变已成数学阶段。

job 同时写明 requested_jet_length，必须与命令行 $N$ 相等。
不在当前会话自动把 $N$ 设为155、156或290。
初次若只需预备全球局部图，可以取长度2；
后继仅在真实函数或胖点要求时增加长度。

阶段不可变 configuration 绑定以下键：

- result、p、source_sha256、python_flint；
- R796_proof_sha256、R796_method_sha256、R793_proof_sha256；
- retained_artifacts 的两组完整 run/source/artifact/manifest/certificate/file SHA；
- original_M2_recipe_sha256；
- cusp_coefficient_convention、cusp_highest_exponent=27；
- CM_point=original_P1、coarse_coordinate=a-1；
- 原 adapted_basis_policy、monomial_order_policy。

requested_jet_length、预算和当前 run 不进入不可变数学 tag。
因此同一个冻结核心、原图及输入可以增量接到更大 $N$。
它们写入当前 request、run receipt 和最终证书，不得借此跨核心或跨输入续接。

## 2. 最小原输入结构

retained/R786 下保留：

- 原 p41-exact-original-power5-short-basis-certificate.json；
- 原 full-outputs-manifest.json；
- 原 R786-exact-stages-manifest.json.gz；
- 原 power1 的146个 R786-exact-power-1-row-NNNN.json.gz；
- 必要的原 basis-index 若用于检查原行顺序；
- run/core/input receipts 的来源元数据。

只读取146行中 $q_Y^0,\ldots,q_Y^{27}$ 的40个原 $\xi$ 坐标。
这些值属于原已完成129项；不得重新运行原 E1/M2。
每行按实际 schema 核 weight=2、bound_qY=128、integer_scale=6724、
recipe 与完整 source-bound configuration。
旧行没有单独 power 或 index 字段；原 power1 行号由固定 manifest 中
绑定 SHA 的文件身份、同一原 recipe，以及 R790 的 index 三者对齐。
不凭空要求不存在的字段，也不只靠未核 SHA 的文件名猜测。

retained/R790 下保留：

- 原 p41-original-CM-fiber-jets-certificate.json；
- 原 full-outputs-manifest.json；
- 原 R790-stage-manifest.json.gz；
- 原146个 R790-M2-CM-jet-NNNN.json.gz；
- run/core/input receipts 的来源元数据。

核 cm_jet_order=5、original_psi_values_and_first_coarse_jets_verified=true、
原 M2 维数146及尺度6724。
逐行读取 value_K_1_zeta、derivative_z_K_1_zeta，
并把原 M2 recipe 与 R786 同一行逐项接上。
两组必须绑定相同的原 R775 M2 recipe SHA
51113988c90b301cb6117fec5c294b77110e1826bf00229b7993ba82144f5d3d。

输入证书、manifest、每个文件及实际 producer 配置全部验证。
不只用一个名字相似的文件；不因某个数学字段看起来合理而跳过原 SHA。
原一日 artifact 过期前，把本次确实消费的原输入放入同一 source-bound
一日 active input bundle；不入 Git 或 Release。

## 3. 原基适配阶段

阶段名 R796-original-CM-adapted-M2-basis.json.gz。

按固定原行顺序选择第一个值非零的 $\tau=s_{i_0}$，
再选择第一个比值首导非零的原行。
构造一点消失的 $\sigma$ 与144个二点消失的 $u_j$，
必要时清分母为 $\mathbb Z[\zeta]$ 原截面组合。

输出必须包括：

- 原 anchor 行号、所有非 anchor 行号；
- $(\tau,\sigma,u_1,\ldots,u_{144})$ 在原146基中的准确列坐标；
- 逆基变换，或等价的逐原截面 $s_i/\tau$ 的 $1,t,x_j$ 坐标；
- 每个清分母尺度；
- 原 $\lambda=dt/dz(P)\in K^\times$；
- 原值/首导核条件全部准确代回；
- 原尺度和 recipe 对齐信息。

这个阶段只能据真实输入选 anchor，不预填第0行或任何特定行一定非零。
$K$ 数编码一律为 $a+b\zeta$，两个有理数各用分子/分母字符串。
若实际全部所需数据落在 $\mathbb Q$，允许记录并走准确 $\mathbb Q$ 优化；
该事实必须由本次公开运行验证，不能从少数例子推断全部数据。

## 4. 416个单项式与全球关系阶段

候选固定为 $w_aw_b$、$0\le a\le b\le144$，
先按 $a$ 再按 $b$ 排序。
只继续实际会增加模素数秩的候选，直到选够416个。
辅助素数若造成退化，记录实际原因并换一个合法素数；
不把特征零维数416硬写成当前模秩。

可用原40个 $\xi$ 系数直接卷积，无须先求 V2 坐标。
若先按 R786 实相位压为20坐标，必须在所有输入、产品、右端上用同一转换。
每个选定的准确乘积可独立保存为
R796-quadratic-column-NNNN.json.gz，
避免预算续接重算已经完成的产品。

R796-WP2-selected-monomials.json.gz 保存：

- 416个实际有序对；
- 所用辅助素数、$K$ 分支、准确 minor 行及非零行列式；
- 已扫描候选位置和原图 SHA；
- 选出的真实列，而非预期秩标签。

下一阶段 R796-original-global-quadratic-relations.json.gz 保存
144个右端 $\tau u_j$ 的准确关系系数。
允许直接解416阶 $K$ 矩阵，也允许在两个分裂分支做准确重构。
若使用分裂分支，416个单项式必须相同；
行 minor 可不同，但两个分支都在解同一唯一 $K$ 关系。

最终须代回全部 $q_Y^0,\ldots,q_Y^{27}$ 原字段坐标。
其证书写明 all_144_global_relations_verified=true，
verification_highest_qY_exponent=27，
full_xi_coordinate_count=40 或经认证的实相位坐标20。
完整代回与 R796 的零次数界共同给全球恒等式；
不能把 mod-rank 或小数 residual 作为此字段的依据。

二次关系矩阵为144×416，记录所选单项式的稀疏结构。
不需要生成完整10585个候选的稠密核。
候选前几个锚点可能已经足够，但这必须由实际416阶 minor 说明。

## 5. 增量局部系数

已有 $x_j(0)=x_j'(0)=0$，且 $t$ 本身为形式变量。
对每个新增阶 $n\ge2$，只运行 R796 (796.14)，
写 R796-local-coefficient-NNNN.json.gz。

每个阶段包含：

- degree=n；
- 144个准确 $K$ 系数；
- 二次关系阶段 SHA；
- previous_coefficient_sha256，首个新阶绑定原基阶段；
- 全部不可变 configuration；
- complete=true。

不在每个阶数重复保存整个前缀。
续接逐 SHA 核全部已成阶段，然后只补欠缺的阶。
输入、原图、核心或证明变化时，不把旧阶段静默当作同一数学任务。

最终可单独写 R796-original-M2-ratio-jets.json.gz，
给所有146个原 $s_i/\tau$ 到当前 $t^{N-1}$ 的展开及 $\lambda$。
这是当前长度的一份线性大小消费者文件。
它不重复保存整个前缀于每个 checkpoint。

## 6. 最终证书的准确范围

最终证书至少含：

- result、p=41、complete、configuration；
- original_M2_dimension=146；
- selected_WP2_monomials=416、global_quadratic_relations=144；
- all_144_global_relations_verified=true；
- implicit_x_Jacobian_at_original_CM_point=identity_144；
- requested_jet_length 与 completed_jet_length；
- 原 anchor、$\lambda$、各主要阶段 file/bytes/SHA；
- input_CM_values_or_first_derivatives_recomputed=false；
- old_E1_M2_or_Laurent_prefixes_recomputed=false；
- actual_beta_eta_or_heights_computed=false。

若当前只完成原图而没有请求更高阶，completed_jet_length=2 是合法实际结果，
不能把它称为长度155或“全部共同零已算完”。

另行消费者可用 R775/R786 的真实 product recipe 评价 V3、V5或V6。
原 A/B 消费者必须绑定 R787 的实际证书和完整1234个原坐标；
胖点消费者必须输出真实评价矩阵和准确核，不能仅输出理论维数。
这两个消费者不作为当前原图任务的隐含已成输出。

## 7. 公开运行与保存

新数学只在 Rogerhu12/math-research-public 的 Actions 执行。
建议每段预算300分钟、工作流350分钟，按完整阶段续接。
所有可重算列、矩阵、局部系数、证书与输入 bundle
只在一日当前任务 artifact 中流转。
仓库只留脚本、参数、run 编号、输出 SHA 与真实结果摘要；
不上传 Release，不将原大字段矩阵提交到仓库。

