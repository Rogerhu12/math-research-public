# 六控制、三 active、非零幅完整112场：独立源码接口

类型：可执行源码与参数合同；本地仅源码/AST操作，未调用任何科学函数。作者：OpenAI ChatGPT（amplitude 子任务）。日期：2026-11-15。

## 1. 可以直接做的实验及尚未给定的内容

原低三方程未全部达标，不阻止以实际六系数和一个显式有限正 λ 作为初猜，调用原完整耦合方程。低三近根、当前高109可逆或横截证明都没有被写成开算门。它们关系到种子质量/条件理论，不能替代本次完整方程的实际接受。

新增 `computations/geometry_20261115_six_control_full112.py`，42683 B，SHA-256 `807f6a35e0d66aee7a2f324e4573bd2b9e9be8feab1972e4b073aa8ee91ed7a2`。源目前未执行；本通用源不内置请求号、实际 λ 选择、native 成功锚或未来结果。本接口给出完整运行参数，独立的实验 recipe 与工作流另行声明所选 λ 和真实参数来源。

新 schema 为 `six-control-three-active-nonzero112-complete-physical-DN-v1`。它独立承担新标量/目标/初猜/响应身份，不冒原 v3 scalar schema，不把原 accepted96 或 circle 改成新接受场。

## 2. 精确未知量与目标

完整系数顺序为 `[p1,p2,p3,theta1,theta2,theta3]`。本入口固定三个实际 odd 值，即索引 `[3,4,5]`；active 设计坐标固定为 `[0,1,2]`。暂不选择其它 3×3 minor，也不把六 active 坐标塞入旧平方边界。

物理场338、core112、active参数3，共453；左行341、右行112。全部109个高core仍是自由未知。前三core目标取真实 accepted96 原文件中的三个数 A，再形成当前有限浮点目标 `lambda_target*A`；λ=1回到原三目标。源文件与 accepted 标志均不修改。三 p 继续变化，所以这仍是设计族求解，不是 same-g 细化；只有最终六个值全部冻结后才有 same-g 的意义。

实际标量沿冻结117 family定义。三odd先按原 theta2/theta1/theta3顺序进入 base，随后加三个 active even 控制；该平方视图和原搜索具有同一明确实公式，但不同 binary64 求和路径不被声称逐位相同。原有限Gauss半径与独立返回的 ap/app 保留，不能冒成已证明的连续导数恒等式。

## 3. 可执行参数与 recipe

调用必须在本仓公开 Actions，并将 `out`、`work` 放在互不包含的实际 `RUNNER_TEMP` 子目录。未来真实临时原输入路径由工作流恢复；本源码不做网络传输。

```sh
python computations/geometry_20261115_six_control_full112.py \
  --recipe "$VISIBLE_SIX_RECIPE" \
  --expected-recipe-sha256 "$VISIBLE_SIX_RECIPE_SHA" \
  --accepted "$VISIBLE_ACCEPTED96" \
  --prepared "$VISIBLE_ORIGINAL_PREPARED112" \
  --tail-anchor "$VISIBLE_ACTUAL_ZERO_J112" \
  --tail-config "$VISIBLE_ACTUAL_TAIL112_CONFIG" \
  --tail-client "$VISIBLE_ACTUAL_LIVE_CLIENT_SOURCE" \
  --expected-tail-client-sha256 "$VISIBLE_ACTUAL_LIVE_CLIENT_SHA" \
  --tail-source-root "$VISIBLE_NATIVE_SOURCE_ROOT" \
  --out "$RUNNER_TEMP/six-control-full112-output" \
  --work "$RUNNER_TEMP/six-control-full112-factors" \
  --jac-workers 2 --max-nodes 1200 \
  --material-angles 4096 --physical-angles 4096 \
  --node-heap 1536 --outer-iterations 8
```

`--prepare-only` 明确只付原有限域初猜预检，不调用 native/FD/BVP，返回0也保持success=false。完整调用没有 prepare-only 时，真实 live client/source SHA/source-root 是必需输入，不会退回伪零锚或旧失败结果。

Recipe 的必需字段如下；λ没有默认值：

| 字段 | 明确合同 |
|---|---|
| `schema` | `explicit-six-control-three-active-nonzero112-recipe-v1` |
| `parameter_order` | `[p1,p2,p3,theta1,theta2,theta3]` 字符串列表 |
| `active_parameter_indices` / `frozen_parameter_indices` | `[0,1,2]` / `[3,4,5]` |
| `initial_six_parameters` | 六个实际有限数，作为新求解的初猜 |
| `lambda_target` | 显式数值，当前直线目标路径范围 `0 < λ <= 1` |
| `field_modes` / `field_angular_quadrature` | `112` / `2048`；与边界4096角区分 |
| `initial_guess_kind` | `fresh-circle-low-three-linear` 或 `same-family-complete-field` |
| `source_input_sha256` | 下列原四件实际输入SHA映射 |
| `continuation_sha256` | 仅后一种初猜必需，绑定 `--continuation` 的实际原字节 |

四数学原件按原 `constrained_trust_warm.EXPECTED` 保留：

```json
{"accepted":"b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff","prepared":"0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714","tail_anchor":"e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51","tail_config":"01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5"}
```

例如实际117末六参数的原读数为 `[0.42123313016645575,0.2168136988206389,0.5629172159488391,-0.1326982215718915,0.00881492232668194,0.08635618490039039]`。这可以作为上述 `initial_six_parameters` 的真实字面来源，无须声称其低三或完整场已接受。来源为 run43691986785，88323 B原摘要SHA `14b3c8afe2a4fb03537a6d16dd4c55d44a37d750750ee25aef3bf157a026ac6b`。这里没有选择 λ，也没有生成请求或把117变为非零112父场。

## 4. 两种真实初猜

第一种在当前六系数重新调用冻结117 `CircleReference.evaluate`。圆的 R/Z 和低三 U/H 都重新形成；原实际112×112零尾J的所有项被读取，其完整112右行与对角读数保留。低三系数取 λA，raw-phi切向保持 `T_j=((1-k_j^2)*R-U_j)/k_j` 再乘对应core幅度。高109初猜设零，只是明确的种子选择；没有新增高109零边界，没有消去其未知量，也没有声称非对角泄漏或高块已经解决。

第二种只读本新schema的完整453行原场，要求实际文件SHA、原四输入、M/N、当前标量family/source及完整六系数一致。它保留原物理/core/active数组；λ改变时旧入口目标不伪写为新目标，原Newton处理实际新左边界残差。旧 RHS 不被当成本轮实算结果，当前 RHS 重算后才作 Hermite 插值/完整预检。父件success标志只作已存事实，不继承为新λ接受。

两种初猜都用原 node/midpoint 与两Lobatto RMS域预检和原节点预算。自适应新增节点沿原 Hermite 机制，不用一个小核circle通过替代完整非零场的实际域检查。原预检若失败，结果就是当前初猜失败，没有隐藏投影、放宽阈值或宣布小幅存在。

## 5. 当前实际 H、FD与同一个client

新入口从当前完整endpoint/core经原 `true_height` 得到H，先调用显式提供的真实client `solve(H,jacobian=True,audit=False)`。必须是该实际H的真正完成响应，保全部338×112 height-J字段；原零H响应仅是初猜中的线性来源，不会改SHA成为此响应。

随后直接调用原 `make_directions` 和 `refined_directional_check`：三条原非零height扰动、全部core/物理/control方向、三中心步、两Richardson级、收缩条件与5e−5完全保留。FD中的扰动状态仍使用刚得到的完整J所定义的显式 affine map；没有声称每个FD扰动重新跑native。

FD通过后，同一 live owner 交给原full-DN。原outer当前H调用、每个新H的真实tail重算以及最后 `jacobian=True,audit=True` 全部由原主函数执行；只关闭同一owner一次。关闭错误单独记录，不冒已成功关闭。原core的第一次H调用即使命中本client的合法同H缓存，也只对应刚才真实完成的同一点，不是跨进程旧J改名。

实际bootstrap目前仍未支付。源码不提供或预填一个accepted73/95/103，也不把113诊断当成已经实现的一致128 J/audit。未来可用的client必须真实完成自身原初始化/非线性求解、完整J与审计责任；若它当前没有可用bootstrap，这个调用如实失败。该事实不是要求先完成小核阈值才准尝试非零实验。

## 6. 原求解内核保持及新身份设置

本源码不复制或改写 Newton/QR 内核。它直接调用原完整 `banded.main`，仅将其中旧v3准备入口替换为这个已经实付的新设置/FD层；再直接调用原 `full_dn_solve.main`。原函数体保持原文件字节，设置层只替换profile/显式λ目标/真实初猜/完整RMS预检/新scalar serializer/同client工厂及输出身份。

核心直接pin如下，完整20项在新源 `PINS`；原core `FROZEN_SOURCES` 与family原检查仍执行：

| 直接核心源码 | SHA-256 |
|---|---|
| `geometry_20261115_small_core_six_control_family.py` | `79464f9c6af8863d3c65254701a858f067881b22ca80dba24bacf2bfea484acf` |
| `geometry_20261114_full_dn_solve.py` | `c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162` |
| `geometry_20261114_lifted_modes_banded_full_dn.py` | `390387db4700f64302b76ee684f9a810a611c57c6617eb67d4597a9fa18905c4` |
| `geometry_20261114_projected_core_bvp.py` | `2326720f124d2edc40e63089f8e07d6671e053ff108281efb59091d919f15c5b` |
| `geometry_20261114_full_dn_augmented.py` | `f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e` |
| `geometry_20261114_physical_test_boundary.py` | `3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681` |
| `geometry_20261114_physical_test_response.py` | `83ce387778fb90209e841fc841a81ed3d99e15181d6e86210ec1244fde017e79` |
| `geometry_20261114_full_dn_response.py` | `38d21971b3b0d462f8cf1b8f0a1cd174a28db3dcba450e89d0d0baecc5e26e74` |

保留完整338物理方程、112常数core、三active常数方程；原完整band LU、原17次Newton回溯、固定1e−6 collocation/frozen-physical RMS、1e−11 BC、原外轮、新H真实BC重算与最终fresh native J/audit均不改。原rho/material逆图域guard仍在原core；全部112 native右行与core/active导数完整保留。

原material seam与独立全角cut审计仍读真实最终response，不把physical-phi通过冒成旧material等价或完整闭面证明。最终sample统计显式绑定实际最终三个p与固定三odd。新metric描述独立保存六系数，原accepted96 metric移到source ancestry，不把新的g说成same-g。

原原件写在临时 `initial-guess/`、`actual-H-response/`、`full-DN/`。顶层 `adapter-status.json`及紧凑stdout分别记录准备、FD、原BVP返回和真实错误。source不上传或长期保存raw；未来workflow负责读原小结果/SHA后释放该请求自有临时树。它不调用storage supervisor，也不要求新的SDK存储门。

## 7. 明确的结论范围

这是有限离散完整场的可执行设置层，不是R259分支、R277新参数高块、连续metric误差、全局reach或闭面证书。原三odd保持为设计常数；若后来选择另三个active minor，必须另有明确坐标映射，不能直接改数组标签。

本源没有新增对最终六系数的Arb全区间扫描；原full-DN也没有把该扫描写成数值接受门。当前各完整物理查询域与所有原门保持，最终新的六系数descriptor可供既有family.scalar_domain真实消费；不能把小核阶段旧参数的区间结果跨到此BVP改变后的p。任何真正same-g/闭场阶段均需当前完整实际场及最终全部六个值。

这里只完成源码AST和直接调用/数据合同检查，没有导入或执行科学模块，没有数值fixture，没有实际profile/λ选择，也没有新增独立审核门。本地 `source-interface-static.json` 是可重算源码回执，不要求发布数据。


## 8. 可直接选择的原客户端与真实输入恢复

原 `exact_20261114_true_tail_client.py` 为19526 B，SHA-256 `1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09`。其 `TailClient` 直接读取所给配置；本次原 `T112-config.json` 为2161 B、SHA `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`，实际没有 `initialCheckpoint` 字段，也没有旧trace或iteration-checkpoint输出路径。因而直接传这份原配置不需要恢复一个隐含旧初始checkpoint，也不需要调用会改写配置的 `prepare_config`。客户端只为当前临时输出增设trace/iteration/trial路径，其runtime-config另记新SHA，原input-config保持原SHA。

当前公开HEAD已删除可重算ready数据，必须沿已实际支付的113恢复方法，从历史提交 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复两份原字节到 `RUNNER_TEMP`，再使用客户端已经存在的环境槽：

| 环境槽 | 原 notes 文件 | 字节数 | SHA-256 |
|---|---|---:|---|
| `VISIBLE_FLEX_FROZEN_LEDGER_READY` | `2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json` | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| `VISIBLE_FLEX_FROZEN_STORED_READY` | `2026-11-13-strong-m28-recovered-full-audit-r1-ready.json` | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |

另外必须通过原 `exact_20261114_public_resume.prepare_public_source` 恢复完整78份公开原source及其原manifest。两ready仅供原冻结几何/参数工厂使用，不是本次非零112 native接受锚。没有从actual91、95或103的失败checkpoint导入一个accepted标志，也没有借用它们的J或残差。

这个客户端的首次 `solve(current_H, jacobian=True, audit=False)` 会向真实原worker发送当前完整112维H；原solveTolerance、32次Newton、10档原trial与其域检查都仍由原worker执行。真实未收敛会抛出异常并保留其临时原响应，当前适配器据此停止，而不会把零锚J或线性predictor改写为实际H响应。最终audit请求永远重新发送到worker，不命中无审计缓存。

## 9. 最终源冻结时的补读位置

相对最初42218 B阅读稿，最后源码核对涉及三处接口/来源说明：`PINS` 显式补入原FFT、原物理BVP及原separated-QR源码；`read_recipe` 用 `field_angular_quadrature` 指明2048物理场格点，避免与独立4096边界 `--physical-angles` 混淆；`ThreeActiveView.description` 明确 `scalar_parameters=3` 与 `complete_scalar_coefficient_count=6`。最终以42683 B、`807f6a35…` 的完整源为准；没有为这些说明改写原Newton、完整band求解、FD或native函数体。

有限正λ实验不要求当前unit残差先到1e−8。若独立请求选择λ=0.001，它仅表示三个原目标均按该明确比例缩小：入口非圆扰动和该线性初猜的一阶模态同乘λ，而标量六系数本身不缩放。小比例并不证明整个Hermite域、native或full-DN可接受；当前全部预检和真实求解正是该实验需要支付的结果。这里不以局部λ大小推出存在性，也没有在本地计算初猜的域余量。
