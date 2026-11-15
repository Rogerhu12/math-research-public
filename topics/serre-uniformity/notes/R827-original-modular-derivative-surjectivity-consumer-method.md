# R827：原导数层的有限域全局满射消费者

日期：2026-11-15。状态：待实际源全部到位的公开 Actions 工程契约；没有新的模满射或重数结论。

依据 [R827](../results/R827-original-global-modular-surjectivity-and-derivative-termination.md)，
proof SHA256 为 17e9c828e01e652b1a73281bf2249ae2b39133faae3cf22384a5fd6d6a3d4a71。
首实现固定原 prime 1000000753 的 branch 0，并使用原五次关系的1186规范方向。
这与重构原 L 系数不同：这里只需要一个经过完整来源认证的真实地方。
所有新矩阵、模逆、递推与多项式模计算只在本公开仓库 Actions 进行。

## 1. 任务边界与实际输出

RESULT 为 R827-original-global-modular-derivative-termination，
FINAL 为 p41-original-global-modular-derivative-termination-certificate.json。
核心入口参数为 --config、--proof、--method、--retained、--output、--budget-minutes；
有限域多项式 helper 与冻结 R811 模操作 helper 按各自 SHA 导入。

第一次请求的目标层为 q=4；它是待检验的参数，不是预期结果。
目标 q 与时间预算从不可变数学身份中排除，每个已成层及最终 receipt 记录实际 q。
原 prime、原 branch、规范 free 方向、所有源身份及其精确阶段、normal 基、proof/core/helper SHA
属于不可变身份。更换 prime 或规范方向必须成为独立数学实例，不能拿原 checkpoint 伪装。

完成输入适配或有限域矩阵，并不意味着原层已经终止。
首模式固定 certification_mode=tau_polynomial_Hermite_and_sigma_infinity_rank。
依据 R827 推论827.4，先实际认证 sigma 图 t=0 的272阶minor，
再认证 tau 图整个多项式模的单位 Hermite / Bézout；两者齐全后 FINAL 才允许写
original_characteristic_zero_Iq_equals_C=true。
无穷远 rank 不足时可以省去此次 tau HNF，记录真实失败字段；
第一图未满射也只记录本组 source 的失败，不据此断言原 Iq 不等于 C 或 D 非约化。

即使实际证明 Iq=C，也只得到安全重数界 floor(q/3)。
当 q=4 真通过时可登记原 D 约化；D 的正规坐标、R825 的完整理想前像、
主函数常数、η 及原高度仍未因此算出。

## 2. 原输入与禁止重复的边界

六个逻辑 producer 为 R806、R813、R820、R824、R809、R787。
后两个允许消费已经结束的预算 checkpoint，但必须由实际 run receipt、
完整输出 manifest 和逐阶段 complete=true 配置认证；不能读取运行中的假想文件。
R787 的旧预算失败身份与 R824 原载体中的字节完全一致，不改成成功 producer。

| 原输入 | 本次真正读取的部分 | 作用 |
|---|---|---|
| R806 | 原 primitive multiplier index、34 组准确坐标、实际 cyclic witness、原基身份 | 真 W 的逐系数模约化与新的单位节点 |
| R813 | 两列准确 S3 坐标及 normal interface | 原 vg、vh，rational scale 各只施一次 |
| R820 | 两图 C index、544 个原列及小原身份 | 完整 flat cusp 格和两图换基 |
| R824 | 首 scope 真实五次 branch 0、共同 chart / 源引用及成功 profile | 原 28 规范模方向；不把 C 坐标当 B 坐标 |
| R809 | 原 S5 index、1234 条已成 69 项整数行、实际旧短 minor | 新 prime753 的 normal 坐标块；绝不重生成前缀 |
| R787 | 旧 selection、chart、rational blocks、branch0 及1234条原 real power5 行 | 同一 DVR 的前级单位逆、原 V5 全1380行和规范 lift |

R809 的 S5 行在此前运行中产生，若尚未发布为可读完整阶段，就保持这一组 pending。
不同 prime753 的新模 minor / inverse 是本消费者必要的新算术；
若同 prime 的完成逆已存在，必须按原 producer/file SHA 直接复用。
不得使用旧739长前缀 minor 冒充 S5 短矩阵。

实际下载可以从 source-bound 后继临时 bundle 提取未改原文件。
原 producer/run/source/file 身份与载体身份分开记录；
Range 下载只宣称所消费成员逐 SHA 通过，不宣称重验过未下载的整个旧 ZIP。
one-day 输入 bundle 只作活跃接续，不入 Git / Release。

## 3. 单一原 canonical B 与整性

固定原 R787 的 prime1000000753、branch0，保原 integral_B/s 根、lambda 与原 b 模型。
旧 stage 必须实际给：
20 阶常数块单位、1234 阶 A 块单位、1186 阶 Schur 单位、
原分母与 κ 单位，以及共同 pivot/free 列。
结合 R824 / R787 的特征零 rank 上界1186，这些事实定义一个真实 p 整的规范 lift。

规范 free 方向由请求指定；优先保留原1186方向时，直接消费旧 initial_C 与 initial_A。
若消费 R824 首 scope 的另一列，必须记录其真实 kernel_free_columns 位置。
所有分支共享的 free 词来源保持不变；本消费者只取一个真实地方，不重新做14分支 CRT。

原 branch 中 C 的1214行先按原 Z 展开：
pivot 行 Z_pivot_integer_rows*C，自由行 Z_free_diagonal*C。
B 得到原 V5 的1234个系数，A 是同一旧规范关系的1234个系数。
不能把 C 当成原 B。

S5 的整数基和原 V5 的整数基都保原82^10。
因此在模 prime 的全部1380行中，先以原 B 系数合成 rhs，
用实际 S5 单位 minor 解1234未知数，再完整乘回1380行。
S5 row_mapping 把解准确变成272条次数至多5−epsilon_i的多项式 vB。
没有补82的幂，没有把旧 content / rational scale 重复放入。

这些模坐标的来源，是同一单位线性系统中唯一的抽象 p 整特征零 lift。
本任务不把它们写成已重构的有理 / L 坐标。
原 B 可能有额外零，甚至在 cusp 有额外零；这只会使本次充分证书失败。
不为了通过检验随意改规范或删除额外因子。

## 4. 八个原单位节点与三个真实模算子

只用真 W、vg、vh、vB 的约化。W、vg、vh 的每个原有理分母须在同一地方为单位；
必要的共同约分在 Actions 内按原整数分子分母执行，不能跳过非单位。
R813 的两个原 scale6724 仅在恢复 vg、vh 时各施一次。

依次查找不同整数 z0 的实际单位 Krylov 点。
同 prime、同原 W / normal 基的已完成点缓存按原 SHA 导入；
不得改旧 configuration 冒充本任务自产。
每个新点计算 K=[e0,W e0,...,W^271 e0]，
记录真实 determinant、K 的源 fingerprint 与双向 inverse products。
坏点完整记录后换点，不更改 prime / 原根，也不填预期 rank。

八个好点共同承担：

- M_B 的八点插值，weighted shift5，最高次数7；
- M_g 的前六点插值，weighted shift3，最高次数5；
- Γ 的前五点插值，weighted shift2，最高次数4。

Γ 点值直接用
Gamma*K = [0,vh,2W vh,...,271W^270 vh] − Mg*Kprime；
Kprime 由 W/Wprime 的短矩阵递推得到。
不重构 M_h，不构造特征零高次 Krylov 基或逆。

插值数据是既已存在且有原全局次数界的算子在单位节点的真实值，
R827 §7 的单位 Vandermonde 引理遂证明其所有特征零系数 p 整。
这与仅凭点值猜一个矩阵不同。
实际新输出仍全核 weighted 支撑、第一列及原 W e0=e1，
并准确核原第一列及 Gamma e0=0、Gamma e1=vh。
M_B 与 W 的交换子每项次数至多8，在固定9个不同剩余点核整个矩阵为零；
Mg 与 W 的交换子每项次数至多6，在固定7点核零。
H=Gamma W−W Gamma+Mg Wprime 的 weighted shift 为3，
[H,W]的每项次数至多6，固定7点的整矩阵核验遂认证完整多项式恒等式。
这些终验点不要求是cyclic单位点；prime远大于9，故点值核验加次数界是准确的。
H只在这些有限域点短暂形成，不另做char0 CRT或存完整Mh多项式。

σ 图使用准确原式：
MBsigma=t^5 D MBtau(1/t) D^-1；
Gsigma_deriv=−t^3 D Mg(1/t) D^-1；
Gammasigma=t D Gamma(1/t) D^-1−t^2 D Mg(1/t) D^-1 diag(epsilon)。
全部负幂必须真实为零；σ 底导数负号不能遗漏。

## 5. 从原 B 的272列递推并进入完整 C

初始两图 F0 是 MBtau / MBsigma；
第 i 列原齐次权为5+epsilon_i。
按原递推
Fnext=Gamma*F+Gderiv*Fprime。
第一图保存完整有限域系数，次数上界为5+epsilon_column+2k−epsilon_row。
第二图只需初始模t^(q+1)，第k层保留模t^(q+1−k)，
所以每一步需要的前层高一项都确实存在；不能求导之后补丢失系数。
实际初始MB是已知完整低次多项式，其范围外的系数为已证零。
每个 source block 按chart/k/单一系数阶/16行命名，记录上一层与Γ/G源；
增加q时只追加真实缺少的系数，绝不重做已成block。

R820 原两图 C 的唯一20次对角在271列，其余271对角为1。
先把第二图F0(0)..Fq(0)横向拼接作准确有限域消元。
若rank272，保存原列索引、真实272阶square及非零det；
因P_sigma(0)是单位，这也就是C坐标的无穷远纤维满射。
若rank不足，仅记录这一充分检验未通过，保全部已成jet。
读取原 q_j、P20，并逐系数检查：
原有理分母单位、首一20次、P20(0)单位；
原 reciprocal / 同字段来源保留，不取 squarefree。
当无穷远通过后，对第一图每条 Fk 的列换基：
前271行不变，最后一行除以P20之前为
F271+sum(q_j F_j)。
实际多项式余数必须为零，并完整乘回原列。
此处仅是完整 C 格的基变换，不是理想 quotient。

首请求只在目标q=4对第一图做一次全模检验，
不额外重做q=0,1,2,3的完整 Hermite，也不计算第二图的整多项式HNF。
所有实际需要的系数分别保存，以便后继增量。
若更小q已有完整 C-coordinate Hermite，则更大q以该已成基加新增层为输入，
不重算旧列消元或旧导数。

## 6. 有限域全多项式 Hermite 与证据链

底环严格为所选原 branch 的 F_prime[z] 或 F_prime[t]。
不使用有理函数 RREF 代替 polynomial module，不只验若干底点。

复用已经完整审过并实际验证过中断恢复的 R811 模操作主干：
独立的有限域 scalar / polynomial adapter 提供同一个精确 Euclid / Bezout 接口，
R811 的 column-operation 状态机不导入 L 数学模型。
新阶段的语义字段明确是原 residue field；
不能在模证书中留下“已在原L上验证”的假标签。

列操作使用真实右矩阵
[[s,−b/d],[t,a/d]]，其 determinant 为1。
每一步保存输入列 SHA、准确 elementary operator、
完整输出列和已完成 receipt；两列同时原子提交。
模逆只作用非零原有限域常数。
有限域 polynomial gcd、整除、Bezout乘回均完整准确。

为减少文件数量，272个坐标整列作为一个 tile；
旧/新 current work 只留已提交版本，保小操作历史。
完成第一图的给定 q 后，将已核完整 plan/receipt 原字节打包成有限大小 tar，
保每项 SHA 与 archive index，再删松散历史。
最终 Hermite 的272个基列及零余列保留，供增量与独立检查。
断在打包或清理中，按已成 archive hash / 原字节幂等恢复，不重做数学。

成功证书要求所有272个 Hermite 对角都为常数1，
所有非对角及余列都为零，并且整个 source→Hermite 操作链保有逐项生成见证。
它等价于完整多项式 Bézout 右逆。
若未来显式导出右逆，须据同一列操作链恢复并乘回；
首次计算不为无消费者的巨大右逆另作新算术。
只有tau多项式模块或无穷远纤维一项成功时也不得写原Iq=C。

没有假定B非零就使模MB为非零因子：约化代数可以有多个分量。
若generic reducer在某个pivot行的所有剩余列为零，核心只捕捉这一明确路径，
再次检查该行确实全零并保存已经完成的unimodular变换。
first_missing_pivot_row不是总rank；没有给出总rank值。
这次充分检验可诚实结束为false，而不把它当坏源或程序正确性的替代断言。
更高q从这份完整变换的全部列加新层继续；若旧全秩HNF已成，则只需其272基列。
已经认证第一图满射的较小q可以直接供更大q复用，不再做任何tau消元。

## 7. 阶段、身份与续算

主要阶段名前缀为 R827-，分为：

1. original-place-and-unit-source-audit；
2. canonical-B-expansion、S5-fixed-minor / normal-vector；
3. prime-...-z-...-Krylov、unit-node-grid；
4. target-B/g/Gamma-point、interpolated-row-block、two-chart-operator-index；
5. tau完整层及sigma递减精度的单系数行block、tau C-coordinate-column；
6. sigma-infinity-order-q-certificate、tau-order-q-Hermite-*及tau证书；
7. final complete stage manifest、FINAL、run receipt。

全部不可变 completed stages 含同一 mathematical configuration。
运行预算、请求的更高q、载体URL和包装器超时从数学身份中排除；
来源与 prime / free 词不能排除。
新 q 对 FINAL 是追加 scope；旧完成阶段的源 SHA、实际 q 和结果保留。
写新 FINAL 前先核各图完整 inventory，防止旧 FINAL 在新增 scope中被误读成完成。

若预算结束，保已成矩阵/层/列操作 checkpoint 与全部所需旧输入，
只标相应范围未完成；不重新触发原 R787/R809/R815。
wrapper 仅作 IO、身份、完整清单和已成标志检查，
数学核心在独立 Actions subprocess运行；本地不导入 core/flint。

## 8. 元数据与诚实边界

wrapper 的公开提交内容只有脚本、参数、原 run/source、输出 SHA 和结果摘要。
原模矩阵、C 列、derivative layers、Hermite work / transcripts、输入 bundle
只保留一天活跃 artifact，不进入 Git / Release。

最终证书列出 actual_prime / original_branch / canonical_free_column、
实际 q / tau Hermite 对角或明确missing-pivot分支 / infinity rank与minor、
单位节点实际列表、原 lift / S5 / scale / C 身份和所有阶段SHA。
失败字段、预算字段和“尚未导出原D/η/高度”字段始终明确。
source单位条件失败会以明确core receipt退出125；预算退出124，均不假装目标q已完成。
一个已完成的充分检验可以complete=true但original_characteristic_zero_Iq_equals_C=false。
safe_D_multiplicity_bound在false时为null；不填假界。
任何新增证书推论必须以实际成功字段为依据，
不能根据目标 q=4、预期随机性或概率论把 D 约化写成事实。
