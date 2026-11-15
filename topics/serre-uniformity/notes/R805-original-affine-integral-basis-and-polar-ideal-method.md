# R805 原仿射整基及极理想执行契约

日期：2026-11-15。依据 R805 完整证明。本文件规定将要实现的准确阶段，
**不是已存在或已成功的核心/运行回执**。函数、极理想、Jacobian、刚性化与高度分别验收。

## 1. 最小输入与既成阶段复用

初次铅笔/分次整基只需：

- R786 的原146条 M2 和418条 V2 行，前41项及全部原 recipe/尺度；
- R775/R799 对三锚0、1、73的实际源绑定和无基点证明；
- R799 原 power7 basis-index/selection 的旧两锚模739秩1758记录。

前两个层已能形成 S 模 V3 的690条真实列，不要求先恢复它们在旧 V3 基中的系数。
若消费者需要旧 V3 系数，再只恢复真实所需右端并全820行核；
不能把新的 S 模基系数直接传进 R798 的旧 V3 系数入口。

清极阶段另读 R786 原962条 V4 行和所用 M2 前55项，
以及原 R775/R803 694基最后四行的 recipe 身份。
只使用 E4/E6 常数项与 eta 的 qY41项，不重算旧 E1 或原 M2。

后继函数阶段才消费：

- 原成功 A/B producer 的1234原 V5坐标、全部关系认证及目标 b；
- R803 成功的 U0..U5 原694坐标和完整1680行认证；
- R794 原5个整数循环字、原 Hom/次数、原 C 与逆；
- R754/R791 的原 sigma/rho；
- R796 原局部二次图及 R798 原 V6选行坐标，供真正的 KM 消费者。

全部 producer 以 run/source/core/manifest/certificate/每个消费文件 SHA 绑定。
已有明确阶段不重跑；预算续接保留同一数学身份及活跃输入包。
不为初次仿射环任务提前启动297阶局部 jets。

## 2. 铅笔与分次自由基

固定整数尺度 τ=e0。旧 n=0 的 V7模739结果直接登记为既有记录，
不把该模缺秩当作特征零失败，也不重算。
优先从 n=1 开始，σ=e1+n e73：

1. 原 V2 各行与 τ、σ相乘，只算本阶段需要的完整41项。
2. 保原 qY/xi，再作原 v 相位并核实坐标，形成820×836整数矩阵。
3. 模素数取实际690阶非零minor。若缺秩，保存实际rank并换n/素数。
4. 每个已成候选可断点读取，所选n、prime、row/column indices、det必须真实。

其后取144个一次补基为原M2去掉0、1行，
对 τV1+σV1 在完整28项中选实际127个 V2补列。
记录418维实际minor、原基索引、尺度、每个新积的完整源。
形成690列 S-module V3 basis，次序严格依证明(805.6)；
真实选行minor与完整820项绑定，不能复用名字相似的旧长minor。

建议输出身份：
R805-pencil-nNNN-prime-PP.json.gz、
R805-graded-free-basis.json.gz、
R805-degree3-S-basis-index.json.gz。
这些名称只是接口约定；实际core未编写前不得标为已有文件。

## 3. primitive 元及真实函数域成本

每个候选 w0 必须在 V1 中，记录原146个准确坐标。
初次可试少量简单原M2元；失败后用证明中的整数一参数族，
但每次是否primitive由真实cyclic minor决定，不以“generic”替代计算。

272列 τ^(2−epsilon_a) w0 d_a 共用一个690阶Q块。
可以复用该块的实际模素数逆；Dixon每组只保最新整数向量/准确残差、
前项SHA和小阶段历史。完整820行认证后才接受。
消去已知τ幂时检查所有不应有的S单项式系数准确为零。
输出原整基中 polynomial M_w，逐项检查 degree≤1+epsilon_a−epsilon_b。

在指定 prime/z0 下求 K_w=[1,M_w1,…,M_w^271 1] 的真实272阶非零minor。
一次坏specialization不能单独宣布w非primitive；
实际搜索/准确K(z)秩的结论分别记录。
正规整基始终是1、144个b/τ、127个c/τ²，不换成幂基冒称整闭。

Krylov矩阵、K(z)上的实际求解和可能的大公共分母是新增成本。
它们按实际消费者分批进行，不先要求完整稠密逆。
每个解全272坐标代回；每次函数除法准确验乘回。
若生成χ(z,W)，核χ(M_w)=0，保原整基和两图过渡；
χ只是函数域的辅助方程，不替代正规环。

导数使用χ_z/χ_W或与之等价的准确connection，明确同一∂z。
原dy/dY比中的共同标度可消；原高度局部参数不能因而改写。

## 4. M6 的8个有理右端清极阶段

从旧V4前55项取962行真实minor，完整列为1100行。
若已有完全相同短列、尺度和行集的已认证逆/解则直接消费。

先对5个目标列 (82^6E6)e_i，i=0..4：

- 仅解所选962行的有理投影坐标；
- **不宣称这五列各自在V4**；
- 保存剩余138行的完整准确残余；
- 对138×5残余求真实核，按固定第一非零坐标规范选非零λ；
- θ=Σλ_i e_i 非零，且完整1100行给 θ(82^6E6)∈V4。

残余秩理论至多4，实际可更低；若算到5必须报告源/尺度错误。
不预填rank4或某个θ行。

再同块恢复 θF690、θF691、θF693；F692的积已由上述5列组合得到。
原尺度为82^8，eta移位q41的原v相位为1。
所有实际成员完整1100行代回，全球差属于4H+2E，不能用42项缩短认证。
输出θ的完整146坐标、四个真正V4坐标、源M6行次序和每个标量。
以R803原坐标组合这些四项及普通690项，得到θUj，
比值时只约同一个θ，保原Uj/U0。

## 5. 原R804 DAG 的环内执行

所有M2/普通幂recipe都在原K定义整基中执行；
原A/B、θUj、原b与rho为源绑定输入。
Gal(L/K)固定这份K环的z和整基，作用于函数全部L坐标，
包括A/B内部及目标b，不能只变最外层scalar。
原T仍是Galois+目标同构，不是Y上的点自同构。

保持R804原Hom字和八节点分支判定。
每个非零节点保存 relative_x、y 的准确函数域坐标/运算DAG，
所有除法验乘回；孤立点零分母不改变全局函数合法性。
有理函数坐标须在原整基中约去实际多项式公因子，不能只约表达式表面的因子。
初次只求原f4及5个最终输出的极理想；
不为每个中间节点无消费需求地作全除子运算。

## 6. 两图理想、quotient 和 saturation

每个非零最终y在两图分别输出：
I_pole=R∩M_y^(-1)R、I_zero=R∩M_y R。
使用原整基的L[z]多项式格，不在可能非正规L[z,w]里取理想。
HNF/Smith算法须保精确变换见证和理想包含等式。
交叠按函数过渡 diag(z'^(-epsilon_a)) 认证；
截面membership用 z'^(r−epsilon_a)，二者不得混用。

ideal sum/intersection/product/colon分别对应min/max/add/subtract。
support saturation使用环内colon并迭代到实际稳定，保每次关系；
单次colon不自动等于saturation。
全球degree使用第一图全部加第二图z'=0部分，避免重复交叠。

R804反对角两图可作为替代/交叉构造，符号与三次幂依原证明；
不要求在直接极理想已经完整成功时重复生成同一除子。
闭点不分裂也照常运算，不引入未认证的分支或小次数假设。

## 7. 三重数提取与固定分歧理想

trace pairing在每个有限代数R/I上准确计算，其核提升给radical。
逐层J_k=radical(I_current)，I_current=(I_current:J_k)，
每逢k为3的倍数把J_k乘入I_D；直到单位理想。

必须记录原E= B+3D的完整乘回，而非仅比较degree。
第一次f4输出的B为原20cusp+P0，global degree21且约化。
另外五次的B理想须逐图等于它。
P1不在B；P1的pole如果存在只能以3的倍数留在D。
这里是除子系数逐项整除，不是选择Jacobian三除点。

完成stage记录真实Edegree与Ddegree，目标分别由原Hom度给定。
原f4以及五输出Ddegree应为395/488/500/527/551/569；
这些是理论校验值，实际ideal尚未返回前不填写computed=true。

## 8. 固定V3/KM接口及原函数标量

用两图ideal对V3进行真正membership，求非零u_g。
对degree569只要求h0≥121，实际维数须记录；不能assert121。
第一次flip通过完整ideal quotient形成F，保u_g/τ³与u_g/σ³。
Fdegree421/328/316/289/265/247。

R796只为实际消费者增量续接到对应qP：
123/216/228/255/279/297；旧完整jets不重算。
R798乘法消费时必须明确当前V3基：

- 或只把实际所需u/v向量恢复到原690基，并完整820行认证；
- 或按R798的生成证明/完整前82项，建立新S模基的按需乘法接口，
  将新前缀仅延长尚缺区间，不把新坐标当作旧基坐标。

同一个原V6选行I仍可直接使用；所有产品都保持原82^12尺度和全部1640项。
后续W_(F+qP)和第二flip回到degree272的标准表示，
输出G_g=u_g/v_g的准确函数、原截面坐标与归一常数。
固定B+251P及272P也在297界内。

整数化原η的完整principal transport是 mathcal_G_g^3；
再接原三同源必须为 mathcal_G_g^9 * mathcal_R_g。
保真正norm、原b、3s、原C逆、c0刚性化与可能Picard二挠比较的未完成字段。
HNF首一基变换不能被当作主函数常数1。

## 9. 分阶段证书与续接

可分别验收 pencil、graded_free_basis、primitive_multiplication、
field_coordinate_transport、M6_clearing、function_DAG、
polar_ideals、small_divisors、KM_representatives、
principal_functions、symmetric_representative_comparison、
rigidification、height。未执行项保持false。

每一阶段绑定原proof/method/core/source输入与参数；
requested_stage和实际消费长度作为运行记录，不通过改变原阶段身份重复计算。
第一版可仅到graded_free_basis或primitive_multiplication，
但不能把这样的初次certificate写作full_eta_adapter_complete。
核心实现和真实运行编号仍待另行创建。

所有新数学只在本公开仓库Actions。每次预算保完整已成阶段与最新活动checkpoint，
续算只追加缺口。原始可重算表和证书不进Git/Release，
只以一日临时bundle传递；仓库保脚本、参数、run、输出SHA与结论。
