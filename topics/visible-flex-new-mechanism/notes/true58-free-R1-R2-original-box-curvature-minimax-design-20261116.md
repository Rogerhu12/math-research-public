# 真正58自由R1/R2与曲率minimax：一次新公开Actions范围

2026-11-16。状态：新科学问题的源码和参数合同；尚未执行，尚无59。完整数学/生成列/解码公式见[模型合同](true58-free-R1-R2-125-generator-model-contract-20261116.md)。本页不以纸审或源码写完冒数值验证。

## 1. 当前对象与问题改变

唯一实际起点是[58](true57-nonlinear168-original-two-grid-accepted58-20261116.md)：physical SHA94950b2bd5d7b5241e14333a4315b073f64840f74849a7909d6de8cb3cc29f54，ind168 SHAe2d52f849596a5e7bbf596b66d7805587acc944c1549c5648ee4e115548ed2bf，粗细metric辅助量分别.26600541430262403/.26600541463999305，细网κ57.9997782607127。η不是无标签整像位移。

[原盒ring17](true58-ring17-original-box-LP-infeasible-return-no-candidate-20261116.md)、[反射射线首3/8纤维](true58-reflected-R1-ray-selected-fiber-infeasible-no-candidate-20261116.md)及[共同α/R2](true58-joint-alpha-R2-status8-no-candidate-20261116.md)均已真实结束，没有新候选。最新联合19返回SLSQP8/false；新增19.9540876秒/0值，相关累计**2902.366570826科学秒、147个完整值**。其未用余额关闭，失败和原始返回保留；本任务不重启任何旧实例。

这里在[R514](../results/R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md)同一个原51控制中，固定R0，释放全部17个R1方向并共同选择17个R2方向。未知量还包括共同曲率上界K和完整物理范数h；这是一个不同的36变量问题，不能描述成给旧α问题换起点、换求解器或加次数。

原168场、172物理盒、永久参考、固定g/b0、全部height及新九坐标背景保留。原51个物理坐标可能变化，另外121个保实际58值。原三样条完整支持参与后续body预测，不在环外截断。当前metric峰位于这些样条的支持内；这只说明不存在该峰被源码强制固定的障碍，不预先宣下降。

## 2. 五份原stdout和已付输入

每份完成的原research stdout只读一次，按原run/job/commit/总字节及每条JSON+LF身份认证：

| 来源 | research job | 读取范围与用途 |
|---|---|---|
| actual58/run43859882465 | 133273598120 | 原COMPLETE、CACHE2、FINAL_CLOCK；当前168、原14门和pool、已付U/T/e/f、selected metric数组 |
| permanent55/run43832870561 | 133182173190 | 只读COMPLETE的永久reference/height-map constructor，55状态不充当58 |
| closed ring17/run43865295208 | 133292183126 | MODEL、COMPLETE、FINAL_CLOCK；完整原圈二jets、G、精确径向三jet来源及旧闭账 |
| reflected R1/run43873254906 | 133319615177 | MODEL、COMPLETE、FINAL_CLOCK；真正保存的scalar_fields/frame、u9/v8、Z17、PiZ17、V17，旧射线求解不重放 |
| closed joint19/run43880150928 | 133343574077 | 仅COMPLETE、FINAL_CLOCK；最后闭账及同一58身份，不调用其模型或优化器 |

第五源固定commit25c98ff4198cfc10552ddcd0dc9307110a6be8de，原log6343887B/SHA06dbe91e2fd93053904e27784be35e4856a137bf4d800f8713fbad3f2334541d。COMPLETE182315B/SHA293424d38ad60946773491574af45e6bfdc6f4b17d49344fb1442eb231811203，FINAL4998B/SHA76b7397f0ae2f845dce969c75f1e32f511257b3a895dd299e273b35a0afa3dac。原request71258B/SHA383d0d45ecd6c617385eae3a4979856db997beb2b1c76029b7e98b7702c037d3仍逐字绑定。

a及a_s只从actual58 CACHE2保存的metric_a/metric_a_s与metric_radial_ids读取原径向id141，并核两个已有来源的一致性。缺字段诚实输入失败；不由旧ray或Xt反解，不临时调用metric补数。已付a=.3399084551031785；a_s的数值在新输入实际读取之前不编写。

## 3. 真正新增的完整模型

每网新增一个完整142列periodic_operator批次：17个缺失线性列加125个二次生成列（uu45、uv44、vv36）。原V17和PiZ17直接读。完整模型为U=U0+Vx，Z12=C0+Zx，Z11=B0+Lx+H(x,x)+Vy；T和Z22固定，G保原实际数组。125是生成列数，不是rank声明；一条旧Hxstar,xstar不能恢复这张量。

新二阶偏导、输入列、两批真实Pi输出、L17/H125、映射及每次模型收缩全部计入新科学钟。完整数组仅存原stdout与runner临时内存，不入Git、artifact、Release或跨run cache。新浮点线性重组具有自己的身份，不冒旧ray逐位相等。

原R0行选最大绝对值pivot，另两物理增量为z/4，pivot由原准确R0平面消元。这给34个尺度稳定的物理变量；其解码为x17/y17。后端raw36=(z34,K,h)与decoded36=(x17,y17,K,h)分别完整保存。候选从raw z的准确binary64有理数按同一准确映射与原58共同合成，最后只作一次binary64舍入；callback浮点解码与准确解码的差异明存。

## 4. 唯一有界优化会话

目标min K+10^−6 h。K∈[1000/61,58]，h≥4||完整172物理增量||∞，h上界由原172盒来源给出，不暗加旧1/128。原172盒全部344行及零宽行保留；原51变化列的102条norm门保留。

K的准确有理下界保1000/61；后端bounds和同一线性行用向区间内包住该值的最小binary64，binding另记准确binary64值，避免恰到后端边界却在准确目标外。

唯一初点是原58零增量、K58、h0。其新模型第一次评价仍收费；原actual58通过不被预写成新浮点模型零残差。固定metric预算为.26600541463999305，原两metric门、正面积下界、实际G及完整三个谱门（包括中间R≥0）全部使用。K可在目标下界以上返回有限候选，此事不支付主reach。

一次scipy.optimize.minimize(method='SLSQP')，maxiter200、ftol1e−9、disp false；solver至多180秒、至多600次不同字面输入的完整值+解析Jac评价。重复输入用当前会话实际cache，所有callback和真实started/complete/failed次数分开保存。行尺度由唯一初次已付评价固定，不逐迭代改尺度。不作旧LP内循环、重启、另种子、开发调用、冻结差分或旧优化复跑。

原后端OptimizeResult全部字段在筛选前输出，包括实际raw36、fun、Jac、乘子、status/message及计数；不存在的字段如实不存在。局部状态不是准确全局不可行/最优证书。QP乘子不升格非线性严格证书。[官方SLSQP1.17说明](https://docs.scipy.org/doc/scipy-1.17.0/reference/optimize.minimize-slsqp.html)明确其乘子范围；ftol不是原门的替代。

## 5. 独立候选门与唯一原actualpair

只有真实后端success/status0且该返回点通过原单位、未平方四PSD、metric、完整物理norm/盒，才产生候选。完整谱平方门并不替代最终未平方检查。候选舍入后还核准确172盒；未舍入R0恒等不冒舍入后的字面环中性。线性norm按原LP_ROW_TOLERANCE筛选，准确ideal_h≤raw_h的独立布尔值如实保存，不将容差通过称为该准确不等式；候选准确hmax门仍另核。

只有一个合格候选才新算固定g径向metric一次、绑定已付first jets两次，然后做一次完整body非线性metric和curvature预测。这里保原cfg曲率门及原η下降至少1e−7；不改为仅环曲率下降即通过。预测合格才调用一次原actualpair，共至多两个原完整grid值；原14门、准确盒、原pools学习/次序和接受逻辑原样保留。预测不能授actual通过或59。

若接受，完整current first jets及selected二jets在原actual学习后保存，不复跑生成；若没有合格候选，0预测/0actual。失败partial预测数组仅保存实际元数据，不声称未来可以免费恢复未输出数组。

## 6. 不可重置的新费用与发布

新范围总600科学秒从process启动、imports及五份来源输入前开始，包含二阶偏导/Pi、解析值/Jac、优化、失败、候选预测/actual和大输出。两批Pi启动前charge；模型记录每批真正结束/异常及真实elapsed，不把整段build时间假写成每批时间。嵌套phase不再加到总末钟。

计数上限：model1、new_complete_primitive_batches2、solver1、fixedmetric1、paidfirstjetbindings2、prediction1、actualpair1、actualgridvalues2。当前任务没有另立“开发免费调用”。原祖账2902.366570826/147继续保在FINAL；不以新counter代换它。

MODEL保存新系数与原输入身份，NONLINEAR_RESULT保存原后端返回，SOLVE_TRACE保存首/末及真实partial值和Jac、固定行尺度、全部真实评价/迭代标量，COMPLETE后再采权威FINAL_CLOCK。其余未输出的中间数组不得称为可恢复免费输入。若输出本身失败，不伪造或重试一个终账。

research和report各先真实pull public/private，逐份比较已读README blob；变化只输出diff并停科学入口待执行新规，读SHA记回H。MR_TOKEN在科学/报告子进程前移除。workflow只由本新request路径触发，read-only report仅在research完成后读一次stdout，无NumPy或几何导入。

本题主门仍是同一g的全时C²闭嵌入、固定材料H、无对齐δhold≥.3D、全域全时reach≥.03D及metric精化到要求；有限环与两个网都不能替代它们。本会话的结束只关闭这个有限计算范围，随后按open继续。

