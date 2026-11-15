# 同一准确 R323 基底上的固定 power4 十控制组件

作者：AI（amplitude）；2026-11-15。独立源码交付，无新请求号、workflow、科学运行或接受场。既有178/183有限字面模型、184完整九族入口、185十维非线性校正均保持原字节。本组件实现已发表的 [连续十控制设计](2026-11-15-continuous-C-fixed-power-ten-source-design.md)，没有用旧 LiteralTenModel 更换一个profile便声称新目标已付。

## 1. 三件具体实现

| 独立源 | bytes | SHA256 |
|---|---:|---|
| `geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py` | 46691 | `72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682` |
| `geometry_20261115_continuous_ten_fixed_power_scalar_numeric_v3.py` | 24933 | `7dedb7134cd2efc43f136c4a87795f06c6f3824c12a25261b6886c624f6e4ddd` |
| `geometry_20261115_continuous_ten_fixed_power_augmented_v3.py` | 6474 | `a248e9577bf6f522b86c7c9b32d3fd51cc49dc9468760ef1d3e78e33062f9e0f` |

准确factory以原0d89370d的完整core/C两jet消费者、表达树、累计长度、construction条件和闭域遍历为基线；数值层以原7cfab12e的同一有限多项式/point/batch路径为基线；物理层以原d86f6fdf为基线，只调整实际独立profile身份与允许视图。旧三源没有修改。完整三个差异及逐项replacement表随交付给出。

新准确factory schema为 `R300-continuous-ten-fixed-support1-power4-v3-cut-exact-expression-construction-v1`，recipe schema为 `R300-new-continuous-ten-fixed-support1-power4-model-recipe-v1`，definition schema为 `R300-new-continuous-ten-fixed-support1-power4-target-family-v3-cut-v1`。数值schema为 `R300-numerical-ten-fixed-support1-power4-v3-cut-accurate-public-u-target-v1`，物理层schema为 `R300-current-continuous-ten-fixed-support1-power4-v3-cut-original-physical-flow-v1`。不能把这些新对象改标签送进原九族硬锁消费者。

## 2. 同一个准确函数与十个真实坐标

参数顺序明确为
$(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3,\xi)$。
完整控制表恰有十条：

| parameter_index | support_index | power |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 1 | 0 |
| 2 | 2 | 0 |
| 3 | 0 | 1 |
| 4 | 1 | 1 |
| 5 | 2 | 1 |
| 6 | 0 | 2 |
| 7 | 1 | 2 |
| 8 | 2 | 2 |
| 9 | 1 | 4 |

没有把所有三支撑粗暴增加至五个powers。旧九项的准确参数与控制项全部保留，只增加零基support1的power4项。

沿原准确表达树，support1是第一速度过渡
$[L_0,L_0+\delta_A]$。令 $w=\delta_A>0$、$x=(s-L_0)/w$、$P(x)=64x^3(1-x)^3$，新增函数为
$$
h(s)=
\begin{cases}
w^2P(x)(2x-1)^4,&0<x<1,\\
0,&\text{其他}.
\end{cases}
$$
它是degree10。准确一、二阶导数仍是同一半径多项式的物理 $s$ 导数：
$$
h'=w[P'(2x-1)^4+8P(2x-1)^3],
$$
$$
h''=P''(2x-1)^4+16P'(2x-1)^3+48P(2x-1)^2.
$$
端点三重零给出 $h=h'=h''=0$ 的左右极限，因此准确零延拓 $C^2$。新factory直接复用准确多项式卷积和微分，不把一个独立返回的ap/app标签冒成导数。

自然长度、三个支持、同一cut、core、$E_0,E_1,E_2$语义叶以及累计coast公式完全不依赖这十个控制系数。第十项不进入coast支撑内部，不经长度间接修coast；180修域是调整原$p_3,\theta_3,\eta_3$的独立已完成责任。$\xi=0$精确限制为新连续九族，不是178/183的旧finite-Gauss九族。

新增函数独立不推出完整残差响应补秩。任意非零ξ也没有预付正半径、亚单位速度、current C尾响应或非零BVP。

## 3. 与真实180点的最小来源连接

[R384](../results/R384-actual180-complete-accurate-coast-domain-and-selected-nine-parameters.md) 已给真实selected recipe：

- 2136 B，SHA256 `cc87d9327c33a208ac36e7dadaa5608cc3597e8d9f9bc0bd615631a6681fc6fb`；
- 真实来源run `43753422569`、source `636bbc30601cb577266219ed66bb2759d285badc`；
- 原单份必要summary 64284 B，SHA `503d2e7d86359c687842e5ce2d5161cac951c7a0b80c5d2b08f5bec3231dcafd`；
- 九个准确有理系数均有实际逐字binary64表示记录；这只是这些系数的结论，不给C中点或整个数值profile误差外包。

新factory提供真实函数：

~~~python
recipe_from_actual_nine(
    nine_recipe_raw,
    expected_sha256,
    *,
    xi,
    parameter_origin,
)
~~~

它首先核原九recipe完整bytes/SHA、准确九schema、原顺序和九输入；按原 `rational` 规则解释数值输入：float按准确binary64 dyadic，字符串按准确有理词。它保原core/cut/窗口/根规则等字段，移除旧 `nine_parameters`，写独立十schema、`ten_parameters`、完整十项 `control_terms`、原九recipe receipt和调用者提供的实际来源。

ξ没有默认值，调用方必须明确给出。选择ξ=0可精确嵌入实际180准确点；此处只是允许的同函数限制，尚未运行新factory、更没有预定未来非零系数。函数明确记录 `old_nine_domain_result_not_relabelled_ten=True`，不伪造旧factory `result.json`、新domain成功或native输出。

对真实180以ξ=0嵌入、且同一准确core/C族/cut/参数/宽度语义时，已付准确域结论的数学传递可以依据同函数责任办理；不能为换source标签额外制造数值精度门，也不能不核上述准确身份就沿用任何旧证书。对新的非零ξ或活动系数改变，旧参数点域结论不能代付当前点。

未来调用可以沿原完整CLI构造当前C下的新definition：
`--core-file --core-file-sha256 --core-geometry-pointer --tail-cover-directory --tail-result-sha256 --cut-twojet-readout --cut-twojet-readout-sha256 --model-recipe --model-recipe-sha256 --code-directory --r300-proof --sqrt-bits --max-domain-cells --max-domain-depth --domain-budget-seconds --out`。
本组件没有恢复旧大数据、生成新输入、运行C或选择λ/mesh/H。

## 4. 准确factory的实际差异

`build_expression`强制十项表和十参数，构造的原base表达树、全部pieces、支持和roots仍为原公式。模型保存 `control_terms`。准确C叶仍为同一$E_0,E_1,E_2$语义节点；`cut_boxes`不会被安装为表达常数，midpoint不进入准确目标。

`piece_range`改为逐明确十项表，按各支持实际闭区间交集和跨界并零形成三个jet的包围。原九项顺序不变，第十项在最后。所有piece与原完整未访stack照保，未加入掩盖非法域的clip、容差mask、独立速度标签或少算一段的例外。

`definition`完整导出 `ten_parameters`、十项表、新source、原九source文本基线以及第十项的支持表达root、degree10、公式与准确零jet责任。原 `continuous_tail/core_input/model_recipe_input` 原来源保持。原R300 proof仍支付原cut/累计构造职责；本新增项的明确零jet推导和源责任在本接口/已发表设计中列明，不假称原九producer产生了十对象。

`main`仍真实读取原core和当前C结果/完整cut读回；原construction条件不松。两个原诊断域pass仍是base及“所有当前参数”两个pass，后者文件改为 `requested-ten-parameter-domain.json`。未决或预算未完仍仅表示充分证书未付，不被改写成非线性拒绝。所有默认资源沿原source，未替未来实验选新预算。

## 5. 数值层的同体三jet与准确参数分责

`NumericContinuousTenProfile`只消费新definition schema/source/十项表。当前C叶盒的中点仍仅用于明确的binary64数值编译，不把它们称为准确目标叶值。原core/全部piece系数的形成、查段、公共partition和接缝word记录均保原程序。

`control_jets(s)`返回完整3×10，按同一控制多项式及其两阶微分形成。四个实际powers为0、1、2、4；第十列只用support1。准确端点零延拓的支持界不加早期容差，数值层仍在原 `x<=0 or x>=1` 分支返回0。它不声称独立圆整支持词与准确支持逐位相同。

`raw_jet`加项顺序为原九的
`(0,1,2,4,3,5,6,7,8)`，然后9。点、batch、公共u与冻结视图都回到同一个新raw体。复数参数forward仍走完整十个系数，实参数域由原profile/继承physical处理，不新设J精度门。

数值编译新增两层必要元数据：

1. definition中的十个准确有理词；
2. 初始binary64参数词及逐项精确 `Q(binary64)-accurate` 差异。

`all_initial_coefficients_exactly_represented_by_numeric_words`按实际相等记录；不以这些字段将不相等的参数重标为同点。实际180九项已可准确表示，不预填未来ξ也可表示。系数投影误差与C叶中点误差分列。

`export_specification(current_p10)`给当前十个真实数值词、其准确dyadics、原定义初始准确词、当前是否逐项等于定义初点、十项表和准确family base身份。若求解改变了参数，导出的当前dyadics定义当前准确family参数点，不冒它仍是最初definition中的点；数值函数与准确family在同参数处的误差仍未包围。

公共材料域保持 $u\in[0,1]$，数值侧 $s_{\rm num}=L_{\rm num}u$，准确侧 $s_*=L_*u$。同样的u名称不代表两者在相同s处；新长度/支持表达root和数值编译原词均导出。原实际有限多项式接缝word不相同不能因新增shape零jet而称全数值C²已证。

## 6. 七冻结453与全冻450的可调用视图

| 类或函数 | 活动系数 | 当前112模维度 | 来源责任 |
|---|---|---:|---|
| `NumericContinuousTenProfile` | 全10 | 460设计对象 | 十项全部参加当前值/响应；不能直接当原453方阵 |
| `profile.frozen_seven_shapes(p10[3:10])` | $p_1,p_2,p_3$ | 453 | 原六shape与ξ七项固定，原前三控制真实活动 |
| `profile.frozen_ten(p10)` | 0 | 450 | 完整十系数冻结为同一个当前数值g |
| `frozen_seven_shape_flow(flow,p10)` | 3 | 453 | 新建独立flow，并把默认active初猜设为实际p10前3词 |
| `fully_frozen_flow(flow,p10)` | 0 | 450 | 新建独立全冻flow，不改原flow或已有state |

两冻结视图的 `raw_jet/profile/scalar_jets/jets_u` 都委托完整十族当前参数；没有把7个或10个系数漏掉。固定七view的 `base_jet`是固定形状加项的原有限顺序，不声称其“先组成base再加active”与完整raw体在有限算术下必逐字同；物理薄层实际逐节点调用 `profile.raw_jet`，因此采用明确同raw路径。

完整物理适配仍继承原 `geometry_20261114_full_dn_augmented.py` 的
`f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e`。
只覆写 `scalar_jets`，保原FFT RHS、physical域、零常量行、Jacobian与invalid-column NaN政策。新类/source硬锁十族及k∈{0,3,10}；旧九class不被接受后再改标签。

例如未来在Actions中的实际构造顺序为：

~~~python
profile = numeric.NumericContinuousTenProfile(
    actual_ten_definition_path,
    actual_ten_definition_sha256,
    modes=112,
    code_directory=code,
)
view453 = profile.frozen_seven_shapes(actual_ten_numeric_words[3:10])
view453.initial_parameters = actual_ten_numeric_words[:3].copy()
flow453 = physical.wrap_augmented_flow(
    actual_original_augmented_module, numeric, actual_probe, view453, workers,
)
flow450 = physical.fully_frozen_flow(flow453, actual_ten_numeric_words)
~~~

这里的definition、numeric_words、probe均必须真实生成并完整绑定，示例不提供伪数据。三原active目标的boundary/未知量合同仍由具体新入口承担。450同g只表示本次十系数和数值求值体被冻结，不自行产生精确连续metric证书、SavedPrefix或accepted状态。

### 6.1 第十项的实际采样盲点

新增power4项在准确局部坐标 $x=0,1/2,1$ 的零、一、二阶jet都为0。端点由三重零给出；中心由 $(2x-1)^4$ 及其前两阶微分仍含零因子给出。因此，**若一个实际离散体仅在整个support1的两端与精确中点取这三个jet**，则该项对这些采样输入完全不可见。这个局部条件不足以断言完整J的第十列为0：实际probe、积分、RK内部采样或边界评价可能包含其他内部位置；舍入后的站坐标、系数形成以及完整响应仍须按真实入口读取。本结论只覆盖明确列出的三个准确局部jet输入，不把它扩成整条求解链的不可见性。

未来十控制入口必须明确保留支持内部可见站或继承已含这些站的真实更细网格。例如 $x=1/4,3/4$ 处准确 $h$ 非零，可以作为明确的内部站选择；必须把站映射到当前准确/数值长度并记录实际可表示坐标、严格顺序以及probe/积分/RK/边界使用的全部真实采样责任，不能只改一个“mesh已覆盖”标签。本组件的 `knots` 仍是原pieces/支持端点，`mesh_from_public_u` 只验证调用方实际给出的网格，没有偷偷选择或添加这两个站。

这项网格责任只保证所声明的离散输入有机会看到新增形状，不证明完整第十响应列非零、补秩或可下降。新入口仍形成完整真实十列；不得把“第十列必须非零/大于某阈值”设成新的科学接受门。若实际列为零或很弱，保原记录与原求解责任即可。该问题不重解释178/183不同旧支持上的原输出，也不改变184当前九族网格。

## 7. 仍须真实支付的求解接口

当前179/184的九参数 CurrentProfile 与source closure仍是独立合同；它们没有被修改，也不能直接吞本十schema。以后实际入口须明确消费新factory结果、definition、十参数recipe、当前C numeric编译和新物理薄层，并保持：

- 当前同C、当前H的完整112 Robin/响应及cut分母；
- 相同明确profile/参数/mesh下真实bootstrap或初猜；
- 原native/fullDN残差、strict slope/Armijo、RMS/BC、fresh当前H FD、finalJ/audit与accepted状态身份；
- 明确投影与准确模型的差别，不借旧零尾anchor、旧J或178/183有限字面值付款。

本次只完成profile和flow源码组件。它没有为一般非对角C重建旧低三模型，也没有把原ExactlyDiagonal条件跨目标搬用。完整十dim方向的线性代数在另有完整新响应时可复用条件结论；本接口不宣称新十响应满秩或当前残差下降。

原九域通过且ξ=0的同函数限制，与将来非零ξ/活动p变化后能否继续原域是不同范围。参数变更不能通过源名保持来掩盖准确目标已变。

## 8. 交付、差异与未执行范围

本地独立目录 `/tmp/visible-continuous-ten-components/`，三运行文件对应本节首表。完整差异分别相对已发表0d89370d、7cfab12e、d86f6fdf；每个newsource小于100KB。源和接口以小文本对象保全，主控唯一Git发布，不创建新request/workflow，不动184/185源或运行。

所有构造代码带原public Actions运行职责。此处仅文本变更、原源码/JSON/字节读取与纸面推导；没有导入、编译或执行科学模块，没有本地数值fixture，也未声称语法或科学结果已运行通过。真正语法与运行范围由未来明确Actions入口按原合同承担。

作为源码条件结论，第十形状的准确三jet/零延拓/固定自然长度已明示；作为实际计算结论，本交付没有新的domain/J/FD/field或成功。实际183若终态先到，R390原读回优先，不能因等待本组件加入其数学接受门。
