# R618：从当前真实模型产生完整帽口积分输入

日期：2026-11-27；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

本条将 `2026-11-27-r618-true-tail-mean-anchor-bounds.md` 的界落实成
`scripts/r618_current_model_tail_anchor_20261127.py`。
它是给已交付 growing-post 固定E模型的真正消费路径，未生成新科学输入或启动运行。
固定参考明确选原run45899589237/job140181814100的实际397；
后来原normal continuation的新H/q不进入这份E。

## 1. 身份在计算开始前绑定

`CurrentModelTailAnchor` 的输入是实际 `model,response,data,parameter_indices`，
以及一份附hash的完整源区间/误差合同。构造时先核模型文件SHA、实际response、
模型本身的完整radial身份和全部参数下标，再从这些真实对象生成
target/model/response/cap/mouth/indices身份。
外部不能提交一份已组装响应范数再在返回端贴上当前Gaussian政策的hash。

源合同同时绑定同一target/model、原reconstruction和
`accurate_inner_tail_definition`的完整JSON身份，要求同一R600准确无限germ和原phase0。
它从模型读取全部旧归一、实际q/paidq、force、knots和新tail政策；
开始与结束分别计算完整源快照，源或响应变化会拒绝返回。
返回值可以直接供模型 `integrate_mean_height` 消费，输入端已有的
`response_model_sha256` 核对也继续有效。

## 2. 原参考不是只保留几项主系数

生产者从绑定原weak源读取 **literal paid265q和原完整knots**，逐项核同实际对象。
从实际397的原q JSON取完整参考参数；系数的JSON十进制数先包成区间，
不在进入区间之前做浮点乘积。

原pre-tanh每个角模的65列由61个五次B样条加4个原局部enrichment组成。
生产者从原完整knots按准确B样条导数公式界前61列。
后4列仍连同原系数进入完整表；因其真实支撑从`.53`开始，而当前原口小于`.222`，
本内尾上P/Q准确为0。这里没有把非零原germ删掉，也没有把浮点underflow当真支撑。

参考的实际包络、4个mode-height归一、envelope归一、原canonical512 tanh、
全部j4…22的原post修正，以及固定forced-j4的
`amp² × paidq[original_nq] × tail_multiplier / scale` 均单独计入。
forced使用未除核心A的原raw j4 germ；不会误用已归一的j4再少乘一个A。
canonical512减均值的径向导数由两倍原Vr范数覆盖，角导数仍用真实F′、F″链，
未改回随输出N变化的均值。

每个原j2…22都有自己的display-log和核心A绝对值区间。
合同须给出这些区间且必须包含当前原对象实际重建值。
这项相容核对本身不是准确ODE证书：其数学来源和数值误差必须继续按第4节登记。

## 3. 真实响应与所有所选方向

当前响应的前10个原齐次列仍是j4…22，并由实际参数值乘原amp计入。
新增部分遍历当前模型的**全部**j2…J及全部次数0…K，按实际索引
`tail_start + mode_index × degree_count + degree_index` 取系数。
每一列都用其当前a、两个cutoff和真实口计算Gaussian比例及积分界；
未因系数为0、float underflow或某个角谱目前很小而删列。

参数方向按同一索引构造：原10个germ列使用amp乘其原germ界；
每个新增tail列使用amp乘对应完整Gaussian界。
其他原body/compact、新compact、core自由项和tau方向在这个内尾准确为零，
生产者先核当前口确在所有这些真实支撑左侧，再登记这些零方向。
固定E的均值是逐r的同一局部隐式函数，因此这些高度方向为零时
该内尾的均值方向也为零；没有抹掉身体或core上的作用。

把参考和当前全部响应合并后，用同一政策中的lambda括号和合同中的
E上下界验证整个盒的b/u/N正性、均值负导数κ、两个参考E根端符号及响应余量。
不合格会明确拒绝；不会在原口上依靠渐近全平自动放行。
输出的均值及参数积分中心为0，半径是纸证(12)逐项累计的完整界。
这表示真帽积分的包围区间，物理函数仍为从真实rc积分的均值高度。

## 4. 不能默认成0的原误差

源合同必须为下列七类各给一条明确status和evidence，缺任何一项即拒绝：

1. 原finite-M到准确无限germ。
2. 原已付有限Cauchy浮点误差。
3. dense ODE和connector/core归一。
4. 原正包络归一。
5. 原forced tail multiplier和scale。
6. literal系数的数值实现误差。
7. 同一参考E和均值分支的数值求值误差。

状态只能为明确未解决，或有证据说明被提供的准确源区间覆盖。
`require_source_errors_enclosed` 必须显式给bool；严格消费时有一条未解决就拒绝。
数值条件消费可以保留这些未解决项，但返回完整 `unresolved_errors`、
`conditional_exact_source_interval_consequence=true`，
以及 `unknown_old_M_or_ODE_errors_assigned_zero=false`。
没有把“区间算式执行成功”当成它输入的ODE常数已经认证。

后者给的是**假定合同中的准确源区间成立时**的真帽积分界，
不能拿其有限数字宣称数值body与准确germ之间的接口误差消失。
即使本帽口输入的所有源界后来严格包围，body均值求积、根误差、实际两次
primitive、直接位置和整个时空reach仍由各自后继范围支付；本生产者不认证这些条件。

## 5. 当前可复核状态

本地只做源码、原定义对照、AST与hash，不导入或执行科学。
现在没有填造一份“全误差已解决”的合同，没有为了获得合同重跑任何旧内口。
后继实际公开范围必须将原归一的确切来源、严格或条件状态和当前固定参考完整绑定。
该生产者与同一模型的直接位置读出是完整fixedE路线的组成部分，
不是静态小幅数据达到README宏观完成标准的替代品。
