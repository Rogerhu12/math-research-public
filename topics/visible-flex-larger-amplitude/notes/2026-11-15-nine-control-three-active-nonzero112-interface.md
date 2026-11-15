# 九设计量、固定六形状的三 active 非零112适配

作者：OpenAI ChatGPT / amplitude。日期：2026-11-15。分类：独立完整场设置层的源码接口，尚未运行。当前没有选择九参数或正幅度，没有请求号、成功 native 锚或未来运行身份。

## 1. 已完成的最小源码适配

新文件为 computations/geometry_20261115_nine_control_full112.py，43641字节，SHA256为 00e4d2c3413cfa6c1df915b9d85050bf375ab88c04e8756149d4ea0533ef3bd8。它从冻结的 geometry_20261115_six_control_full112.py（42683字节，807f6a35e0d66aee7a2f324e4573bd2b9e9be8feab1972e4b073aa8ee91ed7a2）独立形成，原六控制入口不改。

原源读取自公开提交 ace38440324f09471482826136584da38960c417，Git blob 32b8dbb61153a97bb937f2868578373148b2b57d。新源临时 blob 为 ab8a983d21c90d1deaf1c17e80c2fd537a42482c；该对象本身没有更新任何 branch、tree 或 ref。源码交给主控统一发布。

九族来源是 geometry_20261115_small_core_nine_control_family.py，44390字节，SHA256为086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629。该族保留原偶控制与三个 odd 控制，新增同支撑的三个原始 quadratic 控制。参数顺序固定为：

~~~
[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]
~~~

本完整场入口固定最后六项，只把 p1、p2、p3 作为 active 设计坐标。它不要求低三 unit 方程先到1e−8才可尝试真实有限正幅场，也不保证任何初猜、native 或 BVP 收敛。实际123输出尚未在这里消费；六族120的具体参数与λ不转抄成九族输入。

## 2. 与807f的精确接线差异

| 责任 | 原六控制入口 | 新九控制入口 |
|---|---|---|
| 实际 family | frozen six-control family 79464f9c… | frozen nine-control family 086572f9… |
| 完整参数 | 6个实际数 | 9个实际数，前六次序保持 |
| 固定形状索引 | [3,4,5] | [3,4,5,6,7,8] |
| 固定 profile | OddCoefficientsFrozenProfile | ShapeCoefficientsFrozenProfile |
| active 索引 | [0,1,2] | [0,1,2]，未改变 |
| field/core/active维数 | 338+112+3=453 | 338+112+3=453，未改变 |
| 分离边界行 | 左341、右112 | 左341、右112，未改变 |
| recipe/status/source身份 | 六系数独立schema | 九系数独立schema，原v3/v4不重标 |
| prepared/continuation | 原六完整字段 | own九schema、完整九系数及新family SHA |
| 固定系数记录 | 三odd | 六shape整向量，并分别记录三odd和三quadratic |
| 原FD/完整band/core主函数 | 原函数体 | 原函数体；只改新身份与固定向量变量名 |
| 后续same-g | 需全部六系数冻结 | 需全部九系数冻结；当前仍非same-g |

新源直接 PINS 保留旧20项，增加九family一项，共21。runtime仍核原 core.FROZEN_SOURCES、family.checked_sources 和全部实际消费源码；原六family保留为九family明确依赖，不删祖先来源。旧六入口807f是本次源码推导基线，不被冒作实际运行的当前producer。

公开新 schema：

~~~
nine-control-three-active-nonzero112-complete-physical-DN-v1
explicit-nine-control-three-active-nonzero112-recipe-v1
~~~

原FD函数 actual_boundary_fd 与完整求解函数 original_full_solve 在新旧身份字符串和 problem.shapes/problem.odd 名称逆映射后，完整文本相等。此比较不是数学数值检查，也没有把新标量族说成相同g。新 profile 的标量函数确实增加了三项；完整求解内核与原接受责任不变。

## 3. 标量函数与有限求和路径

令原支撑的保存左端点、宽度为 $\ell_i,w_i$，$x_i=(s-\ell_i)/w_i$，$t_i=2x_i-1$，$b_i=w_i^2\,64x_i^3(1-x_i)^3$。新完整标量为

$$
a(s)=a_0(s)+\sum_{i=1}^{3}p_i b_i(s)
+\sum_{i=1}^{3}\theta_i b_i(s)t_i
+\sum_{i=1}^{3}\eta_i b_i(s)t_i^2.
$$

本适配器的 three-active view先把真实固定odd按theta2、theta1、theta3的原顺序加入base，再按eta1、eta2、eta3加入真实固定quadratic，最后加三个active偶控制。其数学标量与九family相同；与搜索阶段“先p后形状”的不同binary64组合顺序不声称逐字相同。原有限Gauss值、独立返回ap/app以及各自保存宽度的责任保留，不冒连续恒等式已经验证。

固定形状包含在 base_jet 中，control_jets 仍是原三个偶控制。因此原AugmentedFlow的全部物理RHS、state/Jp和边界导数是在当前九系数标量上形成，而不是遗漏冻结形状对物理响应的影响。冻结形状没有自己的状态行或Newton列；它们只是不参与当前设计更新。

当前源没有加入新的控制项正交化、旧p平移、导数阈值或rank选择。它固定的是明确的六个实际系数，不以函数独立推断响应补秩。

## 4. 完整453维方形设计问题

M=T=112，全部物理338维（含mean height）、core112维、active参数3维。原三个固定低core目标依然是实际accepted96输入中前三个系数A乘以一个显式lambda_target。高109个core仍为自由未知；没有把它们固定为零或从完整右端边界删去。

lambda_target必须显式提供，有限且0<λ≤1。这个参数只缩放原三个目标，不缩放九标量系数。λ=1还原原三个目标。源码不写默认λ，也不选择九参数。较小幅度不是存在性、全域合法性或native可收敛的保证。

左341行包括原物理入口条件和完整core识别；右112行保留原全部native斜率条件及完整core/active导数。原三active仍在迭代改变，所以即使六shape固定，这个阶段仍是设计族求解，不是same-g网格细化。

## 5. 两种真实初猜

fresh-circle-low-three-linear：
在实际完整九系数重新运行九family.CircleReference.evaluate。读取原完整112×112零H斜率J，保原三传播模式与全部112线性末端残差读数。采用原699节点准备网格，构造完整453状态的一阶低三初猜；高109初core为零只是初猜选择，不改变其自由未知量或右端全部行。当前圆和低三传递结果不是native锚、不是完整非零BVP接受，也不声称九控制位于低三根。

same-family-complete-field：
只读本新九schema的完整field，并用显式continuation_sha256绑定实际文件。要求原四输入、M/N、原场表示、新family/schema/source和九系数身份一致；完整453物理/core/active数组直接作为新初猜。lambda改变时旧入口目标残差不被偷偷清除。父success只记录，不继承为新目标接受。旧RHS不改名为新RHS，必须重新评价原完整RHS，再形成Hermite初猜和完整预检。

这两种路径均用原节点、中点、两Lobatto RMS域与max_nodes预算。预检失败如实返回，不靠小核circle通过代替非零场实际域合法性。

## 6. 当前H、原FD与同一live owner

准备完成后，从真实当前完整endpoint/core经原true_height取得全部112维H，首先要求明确提供的真实client执行solve(H,jacobian=True,audit=False)。必须是该H的实际非线性收敛响应，保完整heightJacobian；不能把旧零H或失败native的结果改成当前H响应。

然后付原physical boundary FD：原三个非零height扰动、原direction集合、中心差分级、两个Richardson级、收缩条件和5e−5阈值完全保持。FD扰动使用刚得到的完整J所定义的显式affine map；不声称每个FD扰动都另跑native。

FD通过后，把同一个live owner交给原完整band/full-DN入口。原每轮真实当前H、所有被采用新H的真实tail重算、最终jacobian:true/audit:true以及一次关闭责任保持。同H合法缓存只对应本owner刚真实完成的响应，不是跨进程旧J重标。任何native未收敛、协议错误或审计失败均保持原失败，不替代成准备成功。

本入口仍允许显式选择实际client源码及其SHA；没有预选未来H(s)客户端，也没有引入新的bootstrap算法。120六族首次native拒绝不是这里的accepted parent；113/122的精度实验也不构成这里已完成的新J/audit。将来若接独立H(s)实现，必须明确其真实source/config与同worker收敛责任，不能只替换标签。

## 7. 四输入与运行CLI

原四输入和旧807f相同：

| 输入 | SHA256 |
|---|---|
| accepted96原输入 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| 原M112 prepared | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| 原T112零H anchor | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| 原T112 config | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

新recipe必需字段：

| 字段 | 值合同 |
|---|---|
| schema | explicit-nine-control-three-active-nonzero112-recipe-v1 |
| parameter_order | [p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3] |
| active_parameter_indices | [0,1,2] |
| frozen_parameter_indices | [3,4,5,6,7,8] |
| initial_nine_parameters | 全部九个实际有限数，无默认值 |
| lambda_target | 显式有限0<λ≤1，无默认值 |
| initial_guess_kind | fresh-circle-low-three-linear或same-family-complete-field |
| field_modes / field_angular_quadrature | 112 / 2048 |
| source_input_sha256 | 上述四原件完整映射 |
| continuation_sha256 | 仅真实own-schema完整场续接需要 |

源码本身不做网络传输，也不创建请求。未来公开Actions先真实恢复原78source、两ready历史输入和四数学输入到本请求临时目录，然后可以执行：

~~~sh
python computations/geometry_20261115_nine_control_full112.py \
  --recipe "$ACTUAL_NINE_RECIPE" \
  --expected-recipe-sha256 "$ACTUAL_NINE_RECIPE_SHA" \
  --accepted "$ORIGINAL_ACCEPTED96" --prepared "$ORIGINAL_PREPARED112" \
  --tail-anchor "$ORIGINAL_ZERO_ANCHOR112" --tail-config "$ORIGINAL_CONFIG112" \
  --tail-client "$REAL_TAIL_CLIENT_SOURCE" \
  --expected-tail-client-sha256 "$REAL_TAIL_CLIENT_SHA" \
  --tail-source-root "$ORIGINAL_NATIVE_SOURCE_ROOT" \
  --out "$RUNNER_TEMP/nine-full112-output" \
  --work "$RUNNER_TEMP/nine-full112-factors" \
  --jac-workers 2 --max-nodes 1200 \
  --material-angles 4096 --physical-angles 4096 \
  --node-heap 1536 --outer-iterations 8
~~~

out/work必须是RUNNER_TEMP内新建互不包含的独立目录。prepare-only只报告准备阶段，返回0仍success=false，不能说已做FD/native/BVP。没有prepare-only的完整调用必须给真实live client及其source SHA；不会退回零H伪响应。

原01930f3b配置已在六族接口按原字节确认没有initialCheckpoint；复用该配置不要求虚构一个旧成功checkpoint。两ready仍按原客户端现有环境槽VISIBLE_FLEX_FROZEN_LEDGER_READY和VISIBLE_FLEX_FROZEN_STORED_READY恢复真实历史字节；它们用于原几何工厂，不是新native锚。

## 8. 核心原门和输出身份

直接调用原geometry_20261114_lifted_modes_banded_full_dn.py的main和原geometry_20261114_full_dn_solve.py的main。原完整band/QR、全部338物理+112core+3constant参数方程、17次inner试探、1e−6 collocation/frozen-physical RMS、1e−11 BC、原外轮及最终fresh native fullJ/audit不改。

仅设置层替换当前profile、新lambda目标、真实初猜、完整RMS预检、新scalar serializer、同client工厂与输出身份。原actual_boundary_fd及original_full_solve的数值函数体在上述名字/身份逆映射后保留。原cut audit、material/physical范围和最终实际active-p统计保持，不把finite physical-phi通过冒成闭面或所有连续几何条件完成。

prepared、pending、actual、driver-status等原输出独立绑定nine_control_full112_implementation。实际新scalar用九family.scalar_spec序列化，完整九系数、odd/quadratic支持及各自source身份全保。最终原accepted96 metric只移入来源祖先，新的metric schema为nine-control-material-metric-v1，并明确same_g_as_original_source_claimed=false。original_metric_identity不能继续冒旧族。

当前原完整门通过也只可能得到新的finite design field，complete Cartesian closed surface仍是独立未完成责任。该适配器没有追加最终全部九系数的Arb全区间扫描；如果p在BVP中改变，不能借用候选搜索旧p的区间证书。当前实际完整物理查询域和所有原门保留，新的完整descriptor可供未来同新family真实消费。

## 9. 旧v3/v4为什么不能直接接，真正450维same-g还缺什么

原geometry_20261114_lifted_modes_profile.py的v3 scalar_spec/reconstruct只认识原三个参数和旧control_scheme/多项式，冻结参数长度严格为3。原geometry_20261114_same_metric_profile.py的v4 _design_specification也只接受真实v3或已有v4，验证v3字段、三参数长度、来源SHA、完整port和canonical identity。新九scalar的schema、嵌套原三参数spec、三个odd和三个quadratic、九值全部必须保留；不能删后六项、改schema或仅替hash让旧消费器通过。

真正same-g阶段应以实际完整接受场的全部九个最终系数冻结成新的独立冻结身份；新重构器必须验证完整九标量spec、支持、有限宽度/组合顺序、原base/port及source闭包。对M=T=112、固定core目标数K=0、active标量数k=0，原维数公式给出：

$$
n=3M+2=338,\qquad n+M+k=450,\qquad
\text{left}=338,\quad\text{right}=112.
$$

这时不再保原三个设计目标，否则不方形；全部112 core是未知。改变网格/field modes不能改变冻结标量，不能把空active向量重新写成空“frozen design parameters”，也不能把新field mode数当成旧source接受身份。原相同g下的残差、真实H/native/fullJ/FD/audit和几何细化必须实际重新支付。

本新源码只供应453维设计适配；未实现或宣称450维新冻结重构/serializer/main。既有AugmentedFlow/SeparatedBoundary/FullDNBoundary的K=k=0维数关系可复用，但旧v3/v4身份层不能偷换。将来450源码需要独立实现这个真实标量重构合同，不能由本次的设计成功标志自动推出。

## 10. 静态范围、交付与没有做的事项

旧807f源码从明确公开commit/blob读取，并独立SHA256核为原字节。新source通过逐项文本替换形成，完整replacement清单绑定原source/newsource SHA与各项出现次数。actual_boundary_fd和original_full_solve作完整文本比较，只允许新身份与固定向量变量名映射，未改变原数值主体。

本次环境在源写入期间变unavailable；后续按根README第8条仅用公开GitHub小文本读取及纯JS文本/hash操作。没有冒称该环境已执行新Python AST、科学import、构建、数值fixture或任何模型/原门。源码和接口各小于100KB，仅创建blob暂存，没有创建tree/commit/ref或派发。原807f及所有旧科学源保持原字节。

当前不提供九参数样例、lambda数值或request文件。未来实际运行应记录真实来源及显式选择，再按完整当前H/FD/full-DN结果决定后继。本接口不为未来实验增加低三根、rank证明、独立预审或额外科学通过门。
