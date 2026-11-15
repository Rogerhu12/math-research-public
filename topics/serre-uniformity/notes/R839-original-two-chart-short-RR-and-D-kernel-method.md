# R839 双图短 RR 执行契约

日期：2026-11-15。本文接更正后的 R839 充分秩证明及首次2431秩的真实结束记录；新增算术尚未执行。原 B、导子、两图、单位 chart、固定锚及原尺度不变。

## 1. 只补原无穷远所需20条源

固定原 $\mathfrak p\mid1000000753$，R827原branch0。τ第一轮的完整2866×2886矩阵及2431个独立列直接读 run43773898829，不重做原移位构造或全部列RREF。

保原σ∞272阶子式中层1的20个原列 $c=0,73,\ldots,91$。其全局权为 $7+\epsilon_c$。权11需5+19·4=81个新移位。

原R827实际只算过σ一阶的0..3系数，文件
`R827-sigma-layer-001-precision-0004-index.json.gz`及68个原coefficient blocks。
这些字节直接复用。原σ的 B、g、Γ 三完整算子也已成：各index及17个row blocks直接读取。

对所选20列，只续缺少的4..9系数：
$$
(F_{1,\sigma})_n
=\sum_{a+b=n}(\Gamma_\sigma)_a(F_{0,\sigma})_b
 +\sum_{a+b-1=n}(G_\sigma^{\rm deriv})_a\,b(F_{0,\sigma})_b.
$$
原R827保存的σ g算子已经带底变量导数的负号，不能再次取负。所有三算子的原weighted support、negative-power检查和原运输证书完整保留。新增系数在 $n>7+\epsilon_c-\epsilon_b$ 的位置必须精确为零；第9项对此20列全为结构零，仍明确记录原完整次数界。

完整σ列经
$$
S_{b,c}(z)=z^{7+\epsilon_c-\epsilon_b}(F_{1,\sigma})_{b,c}(1/z)
$$
运输到τ normal坐标。它准确等于 $zF_{1,\tau,c}-(5+\epsilon_c)M_gF_{0,\tau,c}$，但实现从已成σ系数续接，避免重新计算旧0..3。不存在丢掉表面最高项的截断。

## 2. 原独立列上的增量20阶 Schur

旧2431列记为 $T_0$；这是其真实原源矩阵中的列，不是RREF组合。对其转置做新增行选择，保存2431阶原子式及435×2866商 $\Pi_0$。该新增操作并不重复旧2886列的选择。

新增81列记为 $S$，只对435×81的 $\Pi_0S$ 选新列。实际rank20时，保存20阶子式 $U$。最终2451阶子式按原行序的分块Schur乘积为
$\det(T_0[I,:])\det U$。

以这个20阶解组合新的415行商，逐项核完整原2451列被消去和415个补行是单位阵。其特征零kernel为完整 $T_{11}$，因为所有新旧原列均有真包含且维数上界2451。不能从旧2431模秩另称τ族特征零秩2431。

若增量rank不足20，保存真实结果和新增全部完成系数；不称原短空间不存在。补成全球双图源以后高权最终满射才有正确理论保证，本次不预填权11的结果。

## 3. 原短商、锚乘法和 D 核

成功T11后，完全复用冻结核心
`R839_original_short_RR_spaces.py` 的 T5、原 S5、两锚产品和 D 核数学方法。其SHA为
`0a027c2dd83cfab37181e6386cfd8b22baf176421b727d81a7584d7b351d0c36`。
通过正常、哈希绑定的模块导入继承这些方法，不改模块全局变量。

新core自己构造真实新result/tag、阶段I/O、final与receipt。旧producer阶段保持原字节/原tag；不会改成新自产阶段。完整830×1234的415商、原两个锚在本地方的新乘积、同素点已成S5逆及全部1380代回、最终830×690的395单位核与690×295完整代回，都沿原冻结算术。

## 4. 来源与接口

新核心：`scripts/R839_two_chart_short_RR_spaces.py`。
RESULT：`R839-original-two-chart-short-RR-spaces-and-D-kernel`。
FINAL：`p41-original-two-chart-short-RR-and-D-kernel-certificate.json`。
CLI仍为 `--config --out --budget-minutes`。

expanded job保原五组 `sources`：R827、R838、R837、R809、R786。R827除旧选件外加入上述四个σindex和119个原blocks。每组的directory只用于运行，不进入tag。

新增 `previous_tau_source` 给原R839结束run的六项身份(result/run_id/source_commit/core_sha256/manifest_sha256/configuration_sha256)、certificate_name、directory、逐file/bytes/SHA。其完整原矩阵、2431列选择、metadata、源清单及falsefinal必须由真实原manifest绑定。原79MB载体只是原五组来源的传输；不在数学tag假称新增算术。

tag固定真实新core、冻结legacy core、已更正原proof、本次补全proof、执行method、全部源字节和固定20列/81移位/20阶要求。预算与绝对目录不进数学身份。

新旧阶段不得互相伪造tag。新out使用 `R839-*.json.gz`，每个数学阶段都有新result/tag/complete。旧阶段从明确的previous/source resolver读取。stage manifest只列新out实际完成stage，排自己；falsefinal不约束以后新阶段的旧快照，truefinal所有引用则完整核验。

## 5. 可续性和实际边界

σ新系数按次数原子保存；原独立列的行子式/商、新81列矩阵、435×81的实际增量秩、20阶Schur商各自保存。原后半产品仍按17列保存。预算停只重做尚未落盘的未完成原子操作。

完整success仍要求原T11、T5与D核三个真旗标；expanded_characteristic_zero_coordinates_computed和actual_eta_or_height_computed恒false。输出是唯一原特征零unit-solve DAG及其实际约化，并非展开全部原数域系数，更不是原η或高度。

所有新数学仅在公开Actions；可重算数据只作一日活跃产物。Git只保存脚本、参数、run/hash与证明。
