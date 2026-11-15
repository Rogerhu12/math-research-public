# Request149：持久 Decimal50 参数、完整字面三模模型与同程序 forward 响应

作者：ChatGPT（amplitude 子任务）。本文是可执行实验接口，不是实际149结果、精度证书或非零场接受证明。源码准备期间没有导入或运行数学模型；终端不可用，不能声称本地 Python AST/编译已经通过。当前只做了源文本、JSON 身份及文本差异检查；工作流正常源码解析照旧进行，不另设科学验收门。

依据是 [R320 的 actual146 完整读回](../results/R320-actual146-direct-normal-responses-and-finite-parameter-resolution.md)。146 的九个外方向和两个直接P响应均已付，仍有五次normal的20档全拒、多段完全相同的binary64参数/方程记录，以及原real/complex primal实际字差。149提高完整有限字面模型的算术精度并持久保留参数，不把末端高精度相减立即折回64，也不以重复32批微步替代本实验。

## 1. 文件、身份与唯一触发

| 文件 | UTF-8 bytes | SHA256 |
|---|---:|---|
| geometry_20261115_nine_control_decimal_literal_model.py | 23719 | 2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75 |
| geometry_20261115_nine_control_decimal_curved_search.py | 29697 | 433d5ddd2587efa581fb28ea151ddf3cec5b6a63eb5017340375d1f19b6d98d0 |
| geometry_20261115_small_core_nine_control_decimal_recipe.py | 24656 | 66906f121c52f6dc57894efa368299990eea45f2f1d4fc5e6ce4af2fc5b9536e |
| root_20261115_nine_control_decimal_scalar_readout.py | 17169 | 18583ca2f78b19976ce2d68b999556ff1139f07e0d842a575d1c9188bbd8b5dc |
| geometry_20261115_nine_control_decimal_temporary_batch.py | 20767 | 4f5ca501a1253cf3cbfe6fd0b4543e550ad312850bac334b99b2f2503de50943 |
| public-nine-control-decimal-parameter-recipe.json | 2452 | c9f5908efe8254d785ac56a77e664522e3b36ffdedb3e40c3a744745846a0123 |
| public-nine-control-decimal-request.json | 37538 | 9d42de67627f5d51228b653e9e1bf4bc8f190a6295cd832c0cead1b0c9c568ea |
| visible-larger-public-nine-control-decimal.yml | 19650 | dc5a32467afa016fddc2adc669852c7c43ad2d26812ab3d4e2535e1ddd600599 |

前七项位于题目 computations/，工作流位于仓库 .github/workflows/。只有 computations/public-nine-control-decimal-request.json 的main push触发。没有预填未来149 run、artifact或接受结果；只允许一个原8方向child。

146请求的原96源pin完整保留，再增加模型、求解、producer、wrapper四件，共100；原六个workflow support再加新reader，共7。实际producer来源闭包为原146的33件加当前模型、求解和producer，共36。wrapper/reader是单列工程角色，不伪列成数学producer。历史824c及旧wrapper/reader/normal helper的main不运行。146 producer只复用load_baseline、recipe_input等输入与来源函数；原0865 family生成原有限系数表并执行后述原投影消费者。

旧冻结源均不修改。提供完整文本diff：0865 family→新模型、146 normal helper→新求解、146 producer→新producer，以及146 reader/wrapper/recipe/request/workflow→各新件。新求解同时含独立外方向移植；与旧normal helper的diff不能被当成“只改两行数学”。

## 2. 真实初猜与来源

实际父是146末点，绝非非零场：

- run 43716274591，source 69765fcd81ca84819cdeb09c4fe14c55fdb5fb80；
- 原producer c717bafb95854bef7b60048a8194b9949a30fbff29bc5e1eee8a0dbb25cf233b；
- 原status：2741264 B，252a9ceabf63305cdab40312b104e397acb7a8deb52ea513d4ecc038104d80e5；
- 原primary：73169 B，befc5446223c3f45bc96f4d53aeae6e0115f2fe3214051bc4219f2465fefe1e9；
- 完整view：1329928 B，9593cb0a813caba9a1d43fc59fa7ef6ad2859968fb9804e189ef69bedc623233。

只转录原final.parameters与final_relative_trust_radius：

~~~json
{
  "parameters": [
    0.3055213835477326, 0.21645013203050154, 0.34270051957744246,
    -0.06322334619266512, -0.01747451701873286, 0.9376115689625685,
    1.0751306255033548, 0.6886900390922872, 0.9385431607625546
  ],
  "radius": 4.76837158203125e-8
}
~~~

父配方保原R259-explicit-nine-control-parameters-and-radius-recipe-v1，origin仍是146。九值及radius先按原JSON恢复实际binary64 word，再以Decimal.from_float精确提升，不把显示十进制字符串替成另一初值。半径不重置、不设下限、不夹紧。每次evaluate/description重新执行；父residual/J/merit/FD/normal轨迹都不复用。

父status/log SHA是来源声明，本次不要求读取已清理raw，也不伪称重新核过其payload。跨run重新形成的原binary64表不预称逐字相同：149将自身原模型实际生成的同一组表同时用于原64对照和高精度模型，并保存各表原字节SHA。这个内部共享模型的身份与“父点真实来源”是不同责任。

## 3. 四原输入与完整112范围

| 原输入 | bytes | SHA256 |
|---|---:|---|
| accepted | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| tail anchor | 6815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| T112 config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

沿已付路径从公开历史8bd267107cc8710d371f3b62c02986655ac965b0恢复到本请求RUNNER_TEMP，完整size/SHA核对。原78数值源仍由冻结prepare_public_source恢复。Python3.12.14、numpy2.3.5、scipy1.17.0、python-flint0.9.0与单线程配置保留；高精度内核只用标准库Decimal，没有新数学依赖。

LiteralCircleModel精确提升本次原CircleReference的mesh、h、mid、base/base_mid、九列controls/controls_mid、完整112×112原J、三个target、频率与cut/height常数。逐表记录shape/dtype/raw C-order SHA；h和mid按各自原已有word提升，不从高精度mesh另造几何网格。

保699节点、698单元、三个频率2/4/6及全112末端矩阵。原“J恰对角且三个target非零”入口条件保留，不删除非对角高块，也不因只传播三低模便只读J左上3×3。J是原零H anchor输入，不是当前非零H的新native J。

这仍是低三模有限线性候选问题。完整112右残差保留，但未证明高109可逆、未求出非零112场、未运行非线性native/fullDN；总success/nonzero-field完成声明保持false。

## 4. 高精度从参数一直覆盖到完整残差

上下文是**50位十进制有效数字、ROUND_HALF_EVEN**，不是binary128，不是区间算术。初值/原表的精确dyadic lift可以有超过50位十进制展开；后续算术按该上下文舍入。accepted参数、normal坐标、radius和候选保存完整Decimal字符串，不在科学循环中回写float/NumPy。

标量精确实仿射式保留全部九列。显式odd相加顺序为theta2、theta1、theta3，随后eta1、eta2、eta3。原前三列einsum改为Decimal三项和，不能宣称保持旧NumPy浮点求和word。未由九个控制函数独立推出响应补秩。

完整radius recurrence、midpoint radius、正sqrt、height Simpson、三模每个单元均在同一上下文。每次继续原节点/中点 $a>0,\ |a'|<1$、circle $R>0,\ 1-(a'R/a)^2>0$ 以及分母/有限值检查。原矩阵：

$$
L_j=-I-\frac{h_j}{6}(B_j+2B_{m,j})-\frac{h_j^2}{12}B_{m,j}B_j,\qquad
R_j=I-\frac{h_j}{6}(B_{j+1}+2B_{m,j})+\frac{h_j^2}{12}B_{m,j}B_{j+1}.
$$

完整 $R_jv_{j+1}=-L_jv_j$ 用显式2×2 determinant表达式求解，forward沿其所有乘除传播。这是同一准确实线性系统，不是原LAPACK有限程序的相同舍入序列；没有自动获得条件或后验误差界。

每个模式完整trajectory/velocity、终端Robin两项及相减后的真实残差均保留。原112行仍为

$$
n_k=e_ht_kv_{N,k,1}\ (k\le3),\quad n_k=0\ (k>3),\qquad
f_j=-\gamma\sum_{k=1}^{112}J^0_{jk}n_k+
{\bf1}_{j\le3}t_jv'_{N,j,1}.
$$

单位方程保持原对角情形 $r_k=v'_{N,k,1}-\gamma e_hJ^0_{kk}v_{N,k,1}$。目标仍为原未加权完整三项 $W=\frac12r^Tr$，不是只压第三项，也不是暗换成全112范数。

## 5. 同primal的forward9、9、2、1

Jet同时保存该次实际primal和全部种子方向。加减乘除/正sqrt、完整radius/三模链、L/R、2×2 solve、终端Robin及全112行逐算术传播。没有real/complex两条NumPy内核切换，没有只提高最终减法精度。

response接受九行种子矩阵，依次用于：

1. 全九轴，形成当前完整3×9；
2. 全九个物理basis列；
3. 每个已有normal模型处固定P的两列；
4. 最终选定完整方向的一列。

响应同时产生同表达式primal方程；保存seed、完整三行及112×列数响应身份。与工作primal、pilot乘积和basis组合的差仅读回，不设一致性门。

例如 $z=x/y$ 的变分实现为 $(\dot x-z\dot y)/y$。准确实表达式下是链式恒等式，有限50位仍有取舍误差。没有声称它是rounding离散映射的导数，没有外包误差；域/零分支边界不可暗称可微。FD也不证明最小奇值或弱方向准确。

## 6. 完整方向、normal和选择规则

完整换基沿 [R310](../results/R310-complete-nine-directional-response-basis-and-finite-error.md)。由九轴pilot及 $S_j=\max(1,|p_j|)$ 形成完整9×9 pivoted Householder Q，所有列保留。$V=SQ$，实际 $G=V/S$ 重新形成，不能默认有限Q精确正交后把G换成I。直接forward形成完整 $K=DF(p)[V]$，全部12×9 $[K;\mu G]$ 经列pivot QR及完整三角解。没有normal matrix、rcond、SVD截断或新弱奇值阈值。

floor继续使用原binary64 epsilon这个**算法参数**，不是Decimal epsilon。原64次上界扩张与64次几何细分预算保留；正几何均值改用Decimal sqrt，替代原exp/log舍入路径。真实形成的 $d/S$ 范数仍用于原radius条件。QR、permutation、linear residual与stationarity读数都保留，不能把小值冒严格界。

外方向 $d=Vw$ 再做一列forward。原target为 $c(p)+\alpha a_c$，每条曲线P固定。normal处保fresh九轴响应及其投影读回，另按两个P实际列forward，取对应两constraint行解原完整2×2 row-scaled QR。scaled normal merit、12×20预算原义保留。P、pilot、action及真实曲线起点导数的责任分开，不因标签相似便认作有限值相等。

R299只从一个完整返回的normal轨迹中选已有合法有限点的原full3 merit最小者；working return并列优先，否则首次严格shadow minimum。全部失败trial、working return、候选与误差保留，不增加evaluate/J，不从shadow挽救未完成调用。新算术可改变轨迹，不能说与146相同normal轨迹。

外层仍8个总方向（接受和拒绝都计数）、每方向20档，仍按

$$
W(q)\le W(p)+{\tt original0.2}\,\alpha\,r^Ta
$$

接受。没有新增inner-target门；原normal $10^{-8}$ 只是内层停止目标。原半径规则不变：接受回溯/差ratio则halve；准确近边界全步可double至1；其余retain；20档全拒后quarter而保原点/state/J。normal修正后的总步长不冒称自动在predictor球内。

## 7. 两套54 FD与原final的具体点

原CircleReference.description在初末两个**明确binary64投影点**各做九列×三个step，共54项原central-difference列检查。原complex J、原字段与异常都由冻结0865执行。另在初末实际高精度点，以同三个原step字面值执行新增54项高精度central-difference检查，对照forward9；单列失败仍尝试其余列，不能冒全部有效，也不增加验收门。

每个投影保存实际p50字符串、float参数和hex、精确float的Decimal lift、p50减lift的Decimal50舍入读数、原description/FD。这个差值不是区间界。投影从不写回owner。初始精确提升再投影的情况不能替后续不同点作等同声明。

末端原scalar160-bit/14-depth Arb及完整453圆/两RMS/BC消费者在**最终binary64投影点**、六shape固定的原视图上执行。原初始zero-quadratic counterfactual也只在投影对照中保留。Arb仅承担原声明实表达式范围，不外包字面float误差，更不认证不同的高精度点。高精度循环每次有原离散节点/中点circle domain检查，但没有高精度连续scalar或453全域证书。

unit/full112阈值分别明确命名高精度点和投影点；任何一份都不等价于非零BVP/native/fullDN接受。原overall success/nonzero-field仍false。

## 8. 输出与真正可续参数

producer schema为 R259-nine-control-persistent-decimal50-complete-three-curved-search-v1，临时status为 nine-control-decimal50-status.json。正常final.parameters、final_relative_trust_radius均为完整字符串。current_persistent_parameters/current_relative_trust_radius记录已保存owner；资源中断保真实phase、部分normal记录、异常和未访问后缀，不冒完整final。任意信号可中断局部运算，最后已记录owner不承诺包括尚未完成记录的动作。

未来own-schema配方为 R259-explicit-nine-control-decimal50-parameters-and-radius-recipe-v1，九参数/radius必须是字符串，精度身份固定50/ROUND_HALF_EVEN。实际run/source/status/primary来源须真实补齐，不能经过JSON float转抄后冒同一点。status里的restart_recipe只含可续组件并声明还缺实际origin，不伪装成未来可运行父配方。

## 9. 全标量、错误原文与临时生命周期

reader不以数值白名单裁剪status。全部outer/normal/fresh axes/direct columns、每档候选、R299 sample、原working return、错误、两套FD、投影差、最终域/circle及source字段都保留。大字段通过原结构JSON协议分到完整log groups，段/整组/full view均有bytes/SHA；primary为可重组索引。任何index仍超90000则诚实报transport error，不能删科学字段冒complete。

标签为 BEGIN_VISIBLE_NINE_DECIMAL50_*_PART_*、BEGIN_VISIBLE149_PRIMARY、BEGIN_VISIBLE149_CHAIN_SUMMARY。chain保完整八个计划方向和真实未启动后缀。reader只读JSON/bytes，不调用模型；输出错误不等于数学域失败。

child留在原rules-runner进程组，没有隐藏数值child超时或新session。75min科学step、90mincompute job为一次高精度实验的明确墙钟；原2700s真实pull/rebase/README差异停止保持。没有本地benchmark，不保证8方向都在预算内完成。预算/规则中断是resource partial，不能改称数学拒绝。

若producer在status建立前失败，workflow always步骤在清理前完整保stderr；失败时另完整保producer stdout。每文件总bytes/SHA，每12000字节段有范围/bytes/SHA，用UTF-8 surrogateescape文字可逐字恢复，单JSON<90000。正常producer stdout和所有reader segments本已逐byte tee；reader stderr亦全保。不会只留错误SHA后删除唯一import/工程诊断。

原status/raw数组/ledger/四输入/78sourcecache仅在请求RUNNER_TEMP。完整读回或诚实partial步骤之后才按原属主/路径检查清理；无raw新artifact、仓库或Release留存。清理成功不是科学成功。

## 10. 源级差异和实际149的判读

这是整个primal/变分/参数owner和QR的独立算术移植，非旧scipy结果重标。原方程/control/target/native112/门和预算的数学含义保留，有限操作顺序与轨迹明确改变，无精度或全局收敛承诺。

实际应先读同一次literal table绑定、原64初投影与持久初点的三残差/Robin两项；再读axis9、basis9、normal2、actualdirection1的值与差；全部normal20档是否还出现同参数/同方程后缀、实际dw/target/merit；所有真正接受点/radius/stop及内tol=false的接受；两套54 FD的点身份和异常；最后p50与64投影之差及各份unit/full112/453/Arb范围。

高精度若仍拒绝或慢降，必须据新的完整读数区分非线性曲率、radius/阻尼、真实弱响应与原表精度。149没有预设146全部失败都来自舍入，也没有把高精度标签变成接受证书。
