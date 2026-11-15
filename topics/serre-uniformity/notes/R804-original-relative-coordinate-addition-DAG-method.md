# R804 原相对坐标加法 DAG 的执行接口

日期：2026-11-15。依据
[R804 完整证明](../results/R804-original-selected-map-reuse-in-integral-cyclic-module.md)。
原 R803 final 已冻结，本方法不改其源码或数学身份。

## 1. 实际输入

固定 R794 成功 stage R794-selected-original-low-degree-eta-basis.json.gz：
SHA256 5b96f623e1f43d834a7db21064ff2cb101284b9a4038e5434eb291b6e73f6e0f，
run43691270124、source7cf160128953901a9e4c1d60cfd7cb5a45a17332。
原候选顺序0/3/1/21/15、六个原微分、12坐标a和两个基变换矩阵直接读取。
十二个a坐标的分母必须逐项等于1，不把有理坐标四舍五入。
原 C 与逆的整性只记录既有输入，不重新计算原 R794 范数、秩或 Gram。

原 f4 函数必须来自已成功且全部原129×20关系核验的 producer，
保持原1234基坐标、82^10尺度、b字段、原c0零平移。
未返回的R787请求不是可消费函数输入。
R803 的 U0..U5 必须由其实际成功 stage 绑定，不把本证明当成计算结果。
原 sigma/rho 与 T/CM标签来自原 R754/R791；不得重新求下降表。

## 2. 节点格式与准确 Hom 字

每个节点记录：
- stable node id 与父节点；
- 类型zero、base、negative、CM-unit、Galois、add或double；
- 原 E=Q[T]/Phi21 的十二个准确整数坐标；
- 非零节点的 relative_x、y 两个源绑定表达式；
- 原target b、原base f4的S=y_f4²−b、适用的源SHA；
- 分支所用的准确Hom相等/相反/零判定。

零映射用O状态，没有伪造的有限x/y坐标。
CM单位[ζ]使relative_x乘ζ、y不变；取负仅使y变号。
任何[整数]或其它非单位CM操作都必须有实际群律节点，
不能把系数除法冒充除法映射。

全局关系R³S=y²−b由各合法椭圆群律节点保持。
验证可以使用已证明的通用恒等式及完整源绑定，
不要求把整棵DAG展开成一个庞大有理分式。

## 3. 初始化仅六个非平凡共轭

基节点(1,y_f4)。
j=1..5直接消费原Uj/U0，j=6使用
U6=−U0−ζU1−ζ²U2−U3−ζU4−ζ²U5。
全部j=1..6按原sigma/rho及同权Wronskian形成(relative_x,y)。
不新增第六个混合收缩，不重做原Hodge三积。

原T^7=[ζ²]，所以j+7只使r_j乘ζ²，y_j保持。
必须特别检查这个CM绕回，不能因为sigma^7=1就把T^7设为1。

Galois运输任意节点P时，
r_(T^jP)=r_j sigma^j(r_P)，y_(T^jP)=rho_j^-3 sigma^j(y_P)。
sigma作用于完整函数叶与所有标量，包括b；
它不是Y自同构，也不是对原解析q参数另作未记录平移。

## 4. 固定八步链

严格输出原五个候选，保留源stage中未约化的十二坐标多项式。
短链依R804§5执行：
candidate0一次、candidate3三次、candidate1两次、candidate21一次、
candidate15复用candidate0再一次。
所有短链多项式用原Phi21或原K六次因子准确归约，
逐项核与原stage坐标完全相同。

每个add先比较Hom字：
零元素处理identity，互为负返回O，相等调用double，否则调用割线。
原genericadd分母r_Q−r_P由该判定保证非零函数。
双倍点使用完整R804(804.10)，r与y都保持原常数。
孤立点的零分母仅影响求值方式，不将一个全局合法节点判为失败。

最终每条记录保candidate index、原整数Hom列、原a(T)、原微分、
原次数及原m/N，同时保存relative_x和y的DAG根。
这些标签必须与既有R794完全相同。
新八步处理只生成原映射的函数表示，不重新登记原Hom、范数或低次数选择任务。

## 5. η、主函数与点值消费者

每个实际输出按原R794的d/1206=p/q形成
Norm(y_g²−b)^q / Norm(y_f4²−b)^p。
Norm必须含sigma^k b；若使用同靶T函数乘积则补Norm(b)/b^7。
原3同源3s及所有域常数逐节点保留。
原C与C逆可运输已记录五方向，但不据整数矩阵声称原具体线丛刚性化已得到。

若真实β=f4(c1)先返回，因c1为原Q点，点值可以直接在
D_(rho_j^-1)sigma^jβ上执行相同CM/Galois/加法链，
使用完整椭圆射影群律，不必等待全局M6坐标。
这一分支的证书明确只是五个原映射在c1的值；
不改变其全局函数、极除子或η完成标志。

## 6. 除子接口单独验收

R804(804.14)–(804.16)给两张图的反对角理想及全局支撑拼接。
实现需接受真正有效除子/理想表示、gcd、quotient、support saturation与
必要的局部正规化，保持原乘法/主函数常数。
不能仅保存原式后把complete_polar_divisors设为true，
也不能直接把表达式分母作为极除子。

函数DAG阶段可完成而除子阶段未完成。
证书须分别记录function_DAG、actual_point_values、
complete_polar_divisors、eta、symmetric_representative_comparison、
rigidification和height；未执行项为false。
所有新算术仍仅在公开仓库Actions，完整可重算文件只作一日活跃传递。

