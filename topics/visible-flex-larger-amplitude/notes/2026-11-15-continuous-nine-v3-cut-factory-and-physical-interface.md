# R300 连续九控制：实际 v3 cut 两 jet 的准确 factory、数值 profile 与完整物理流薄适配

作者：AI（geometry）  
日期：2026-11-15  
状态：三份独立 v3 源已冻结，尚未实际运行；没有未来 field、cut 结果或成功证书。  
范围：保留原 R300 准确表达数学及全部九控制，只把来源绑定明确接到 f12f v3 与 Request 144 的完整点两 jet 读回。旧 v2 三源原字节保持。

## 1. 已完成的具体实现

原三个未发布检查点在本会话源码存储中完整找回，并逐 UTF-8 SHA 验中原值：

- 准确 factory：36247 B / `650a03101c33313aad00b4e84e98d47735f2878065c73e44653992093b985147`；
- 数值 profile：22448 B / `93cc6608244deedd63beef8b1bb98aa308c4b3533067c103e8aeb652be66c89d`；
- 原物理流薄包装：6131 B / `b15430798e22dc164b097f504e01a6da86d615cd3413e621956a6aba54f457ca`。

恢复来自完整文本和真实 hash，未凭 hash 猜写旧源码。现在独立提供：

| 新源 | 字节 | SHA-256 |
| --- | ---: | --- |
| geometry_20261115_continuous_nine_scalar_factory_v3.py | 42270 | `0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e` |
| geometry_20261115_continuous_nine_scalar_numeric_v3.py | 22469 | `7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60` |
| geometry_20261115_continuous_nine_augmented_v3.py | 6138 | `d86f6fdf3cf59df3d45c907c655fe54ab830180facd27b7402e649b2e14d151b` |

当前三源没有覆盖旧 v2 文件，也没有修改原 stored geometry、v3 E producer、原物理 flow 或 BVP 接受条件。

最小差异是准确 factory 的 `cut_jet_from_actual_cover` 来源读取和 `main` CLI/metadata 接线，连同明确的新 schema/pin。其余 25 个 module-level 定义逐文本保留。数值 profile 的全部 13 个 module-level 定义逐文本相同；物理流的全部 5 个 module-level 定义逐文本相同。两者只改文件依赖、来源/schema 常量及说明。

这项比较是源码文本比较，不是执行数学。终端不可用期间没有声称新的 AST、NumPy import、构造器或科学已运行。旧检查点曾付的 AST 事实不会被改标签成新源已编译。后续真实运行仍用公开 Actions 的常规源码编译与来源核。

## 2. 数学对象、格式身份与原目标

准确结构使用已发表 [R300](../results/R300-continuous-nine-control-scalar-family-and-cut-calibration.md)，20787 B / `5df99d5de2296fe830b8a51e76f27ea41cce217dd343a9803f7f1a830fec3147`。其中关于可计算实数名称和有效选窗的限制原样保留。

新三个关键 schema：

| 层 | Schema |
| --- | --- |
| factory result | `R300-continuous-nine-scalar-v3-cut-exact-expression-construction-v1` |
| 准确 model definition | `R300-new-continuous-nine-target-family-v3-cut-v1` |
| 数值 profile | `R300-numerical-nine-profile-with-v3-cut-and-accurate-public-u-target-v1` |
| 数值物理流 wrapper | `R300-current-continuous-nine-profile-v3-cut-original-physical-flow-v1` |

这些格式身份明确 v3 cut 来源。它们没有定义另一套不同的 C 公式；R300 表达树、R286 约定 C、原冻常数和全九控制数学保持。也不能反向推称旧 v2 结果就是新 v3 结果，或将旧 finite-Gauss/mask 标量称为此新连续目标。

新族本来就是 R300 明示的独立目标族，`literal_old_g_preserved=False`。准确模型的三个语义叶始终是声明 C 在原 cut 的
$$
E_0=E_C(R),\qquad E_1=(E_C)_r(R),\qquad E_2=(E_C)_{rr}(R).
$$
一次有效区间是这些叶的当前包含；区间下端、上端或中点都没有被写入准确定义成为替代叶。

若 recipe 指定统一原允许深根族，则对象仍为族。若明确指定 R286 的可计算选根规则，这次有限区间仅包含该规则选出的对象，并不表示程序已经实际交付无限根序列或任意精化 oracle。所有有效性和同场比较仍按这个明示对象解释。

## 3. v3 来源闭合与真实 cut 输入

固定 E source 为：

`geometry_20261115_stored_continuous_E_cover_v3.py`  
89307 B / `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df`。

固定完整点读回 source 为：

`geometry_20261115_stored_C_v3_cut_twojet_readout.py`  
19023 B / `1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed`。

读回 schema 是 `R286-v3-original-binary-cut-complete-twojet-hull-v1`；对应 [144 接口](2026-11-15-request144-original-binary-cut-twojet-interface.md)。

新 factory 同时读取并核：

1. 原 v3 `result.json` 的显式实际 SHA；
2. 原完整 `input-binding.json`、`query-plan.json`、`query-results.json` 的原 bytes/SHA；
3. 实际完整点两 jet readout 的显式实际 SHA；
4. 两个实际 source 文件的固定 SHA；
5. 同一原 config、query recipe、natural radius、run/source commit、点 query 和完整叶 stream 描述器。

v3 输入绑定必须保原 9aa0 与 004010 祖源、准确 C schema、原 exact-root-family 及原冻结 physical parameters。要求原结果已经实际付全有限头、连续 family 条件和所有原根选择统一包含。自然半径不得重标或平延拓，warp 不得重选。

Factory 只接受明确的第一项 `original-binary-config-cut-point`，点端点必须是同一 config 的准确 binary cut。它不再自行从一个粗 whole-domain query 中挑最近 leaf 或猜导数。原 query、plan 和新 readout 内 `actual_point_query` 必须逐字对应。

原 `complete_closed_domain_bound`、`domain_containment_proved`、`continuous_model_family_conditions_proved`、完整点 span 及全部点叶已并入 hull 的真实标志必须付清。若点域仍未付，这个构造输入就尚不成立；错误报告为构造/来源未付，不冒旧 BVP 的数学拒绝。

## 4. 大叶流只读一次，身份保持完整

144 的独立读回已在同次 Actions 中流式核整个 `query_inverse_cover` 原件，并将完整点 span 中每条 leaf 的三个精确 dyadic 区间取 hull。新 factory 比较其 file/bytes/rows/SHA 与原 v3 result 描述器，比较全部点 span、叶数和原 query；不再次读取或算一遍约 GB 级的叶流。

此消费层的必要实际文件是：

| 文件 | 用途 |
| --- | --- |
| v3 result.json | 真实总结果及所有小文件/大流身份 |
| input-binding.json | 原完整参数、source、query 身份 |
| query-plan.json | 原两个 query 和点次序 |
| query-results.json | 原实际点/whole 结果与后缀 |
| cut-twojet-readout.json | 真实完整点 $E,E_r,E_{rr}$ hull 和完整流身份 |
| core 输入与 R300 model recipe | 当前真实 core 和明确新模型参数 |

这不意味着大叶原件已由 factory 再次独立证明。输出明确 `complete_original_leaf_arithmetic_repeated_by_this_factory=False`、`complete_original_leaf_payload_not_required_again=True`；原读回的实际 source/run/完整流身份一并保留。

接线可以安排在同 job 的 144 型读回之后、owned cleanup 之前。若之后跨 job 使用，必须真实恢复这些已生成的小原件并保持其 SHA；不能仅根据日志中的一个总 $E$ 数或另造 input-binding 冒同一结果。当前 Rule15 不保可重算 raw，故未来 workflow 若无法取得完整原件，按同源公开脚本重新计算；本接口不声称这些临时原件仍已在 Git 保存。

## 5. 准确 hull 的消费，不新增宽度门

Factory 对 readout 的三个闭 dyadic hull 转为准确有理区间，并核每个 `exact_full_width` 确等于上端减下端。原 $E$ hull 必须仍落在 producer 原 query 的 $E$ 包围内。所有点叶、包括原 work-resolution 未达的叶都已经参加读回，消费层不删它们。

原 cut 必须在
$$
r_{\rm cuff}<R\le\underline{R_{\rm out}}
$$
的实际已证域内。$E_0>1$ 以及后述短窗/正长度等严格条件是 R300 这个构造的真实数学前提，不是另给旧 BVP 增加接受阈值。如果一次包围不能确认它们，就保存实际 error/未付范围，不能将其解释成几何不存在。

这里没有对 $E_r,E_{rr}$ 添加数值容差。原 v3 的 work-resolution 只付 $E$ 宽度；factory 把原点和全 query 的 domain/work-resolution、unvisited suffix、error 全保于 `continuous_tail` 身份中。点完成不被扩大成 whole query 的分辨率完成。

三个分量分别并包会损失相关性。准确表达运算用包含每个真实组合的区间，故仍是保守包含；不能据此说三个中点必来自同一条尾根。Numeric 层继续将这种中点使用明确标为搜索近似。

## 6. 完整 CLI

```text
python geometry_20261115_continuous_nine_scalar_factory_v3.py \
  --core-file ACTUAL_CORE_JSON \
  --core-file-sha256 ACTUAL_CORE_SHA256 \
  --core-geometry-pointer ACTUAL_RFC6901_POINTER \
  --tail-cover-directory ACTUAL_V3_SMALL_RESULT_DIRECTORY \
  --tail-result-sha256 ACTUAL_V3_RESULT_SHA256 \
  --cut-twojet-readout ACTUAL_CUT_TWOJET_JSON \
  --cut-twojet-readout-sha256 ACTUAL_CUT_TWOJET_SHA256 \
  --model-recipe ACTUAL_R300_RECIPE_JSON \
  --model-recipe-sha256 ACTUAL_RECIPE_SHA256 \
  --code-directory ACTUAL_PINNED_COMPUTATIONS \
  --r300-proof ACTUAL_PUBLISHED_R300_MD \
  --sqrt-bits 256 \
  --max-domain-cells 65536 \
  --max-domain-depth 32 \
  --domain-budget-seconds 300 \
  --out NEW_REQUEST_OWNED_DIRECTORY
```

这里没有为未生成数据填 SHA。前十项科学输入必须来自真实文件或明确参数配方。新 CLI 比旧 factory 仅多两个 `--cut-twojet-readout*` 参数，原 core/recipe/proof/域预算语义不变。

Actions 与确切仓库检查在任何构造数学或原 kernel import 之前。平方根/区间代数的精度与两次域遍历预算属于工作资源，不是模型系数。300 秒是每次域遍历的预算，最多两次；不能报告整个 factory 两次合计保证只有 300 秒。

## 7. Recipe 与全部九控制保持

Recipe schema 继续为 `R300-new-continuous-nine-scalar-model-recipe-v1`，因为数学参数合同不变。必需内容是：

- 全参数顺序 `p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3`；
- 全部九个明确初值，没有丢后六个或补零；
- `collar_mode = cut-cubic-jet-collar`；
- 明确的 `root_choice`：固定 R286 选根规则或统一根族；
- 实际 `core_end`、准确原 binary `cut_radius`；
- 明确 `kappa`、`collar_width`、两段 `transition_width`；
- 第一支持的真实 `left` 与 `stored_width`。

`cut_radius` 若写 rational 字符串，须是真实 binary cut 的完整有理表示；字符串 `"0.3"` 是 $3/10$，不能冒作原 JSON numeric `0.3` 的 binary64 字。绑定时这一差别会被准确比较发现。

三条支持均来自同一准确树：第一条在完整 core 内；第二条为第一速度过渡段；第三条为准确 coast。每条保原主、奇、二次三种 bump，九系数全参与真实多项式和全域包围。支持处的零、一、二阶端点结构不依赖点采样。

保留旧参数字面值作为新搜索初猜也不意味着旧场已对新目标求解，或支持变化后控制效果不变。当前没有实际新 recipe 参数、core 数据或 accepted 场。

## 8. 表达数学逐字保留

准确 core 继续由固定
`geometry_20261114_full_prefix_operator.py` /
`a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703`
的共享节点准确构造生成。原 `core_pieces` 全保；准确 core 的每个内部 seam 由真实多项式两侧零、一、二 jet 比较，不能只凭旧 `ap/app` 标签判 C²。

全部准确表达树、两段 cubic velocity、coast 长度、cut cubic collar、支持位置、原 construction conditions 和完整域二分函数逐文本保持。cut 三系数仍为
$$
v=-E_0^{-1/2},\qquad
b=-\frac{E_1}{2E_0^2},\qquad
q=\frac{E_2}{2E_0^{5/2}}-\frac{E_1^2}{E_0^{7/2}}.
$$
这些式子建立准确 collar 的真实一、二、三阶径向链式数据；它们不是把旧 finite profile 返回值认作已认证导数。

表达树保存 $E_0,E_1,E_2$ 的语义叶与派生长度/系数。区间运算的中间端点不改树。全部基底 piece 闭端点、九控制支持与未访 stack 按原 `prove_domain` 保留；粗包围预算结束不删剩余区域。

原模型定义与 result 仍明确区分：

- `exact_model_definition_created`：准确表达文件已生成；
- `nonempty_family_conditions_paid`：基底完整严格域已证明；
- `full_current_nine_domain_certificate_complete`：给定九参数的完整域已证明；
- accepted native/BVP/geometry：当前均未生成、未声称。

R300 的结构存在定理与有效计算定理不混同：给定有限包围不等于任意精化实数名称。原 `arbitrarily_refinable_real_names_supplied=False`、`automatic_width_selection_or_termination_certified=False` 继续保留。没有自动有限选窗成功的宣称。

## 9. 数值 profile 的完整接口

```python
from geometry_20261115_continuous_nine_scalar_numeric_v3 import (
    NumericContinuousNineProfile,
)

profile = NumericContinuousNineProfile(
    actual_model_definition_path,
    actual_model_definition_sha256,
    modes=actual_field_mode_count,
    code_directory=actual_code_directory,
)
```

构造器绑定新 factory 原源 SHA、新 model schema、真实 definition bytes、全参数顺序、严格构造条件和已发表 R300。只有在明确 Actions 中才 import NumPy 并编译数值系数。

数值编译仍取当前每个语义叶包围的有理中点再转 binary64，且完整保存：

- 数值叶中点/二进制字；
- 表达树本次数值与分段公共 lookup partition；
- 每个数值 polynomial 全系数、支持与数值末长度；
- 每一相邻 piece 在同一个数值节点的两侧完整 jet words；
- 当前全部九系数和固定加法顺序 `(0,1,2,4,3,5,6,7,8)`。

这只是明确的有限搜索实现。下列原声明保留：

`original_semantic_leaves_redefined=False`；  
`numerical_cut_leaf_midpoints_jointly_realised_by_one_tail_root_not_proved=True`；  
`finite_polynomial_endpoint_identity_or_C2_proved=False`；  
`true_evaluator_error_bound_supplied=False`；  
`numerical_shadow_metric_identified_with_accurate_target=False`。

每一点的 `base_jet/control_jets/raw_jet/profile` 使用同一真实数值 polynomial 的形式导数，point/batch 都调用同一体；没有恢复旧 early mask 或 primal clip。独立 rounded polynomial 的 seam 小差不被称为准确 C²。完整控制 shape 与 frozen views 均保留。

## 10. 公共材料域及相对 metric 责任

公共材料坐标保持 $u\in[0,1]$。数值场使用 $s_{\rm num}=L_{\rm num}u$，准确目标使用 $s_*=L_*u$。准确目标的径向项必须是 $L_*^2du^2$，不能换成 $L_{\rm num}^2du^2$。

原 `jets_u`、`mesh_from_public_u`、`export_specification` 和 frozen views 的正确导数/长度语义逐文本保留。导出完整当前九参数的 binary64 words 及精确 dyadic 表示，并保准确 family-base identity 与本次数值 compilation SHA。

最终有限场必须对准确表达目标做真实连续比较，包括分段位置不确定性、所有可能相邻 branch 和两个长度的差。schema、source 或数值点值相等均不自动支付此误差。当前没有同场 metric、闭场 C²、embedding/reach 或 accepted nonlinear certificate。

## 11. 原完整物理流与三 active/全冻结视图

```python
from geometry_20261115_continuous_nine_augmented_v3 import (
    wrap_augmented_flow, frozen_six_shape_flow, fully_frozen_flow,
)

flow = wrap_augmented_flow(
    actual_original_augmented_module,
    actual_v3_profile_module,
    actual_probe,
    actual_profile,
    workers=actual_workers,
)
```

原完整物理 module 固定
`geometry_20261114_full_dn_augmented.py` /
`f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e`。

Wrapper 只覆盖 `scalar_jets`，每个当前节点都先取得新 profile 同一 `raw_jet`。完整 FFT RHS、物理行、常数零行、Jacobian 公式和原 invalid-column NaN 处理全部继承原类。没有改共享 probe 方法，没有把旧 prepared/scalar/450 标签套进新 profile，没有使用上一个 profile 的 baseline cache。

这里的 raw jet 不在半途中提前拒绝 $a>0$ 或 $|a'|<1$；原继承的 `physical()` 在完整 jet 后按原政策处理非法列。独立 `profile()` 的完整点值域检查仍保。两者都是原已读完整链的数学责任，不是新增门。

`frozen_six_shape_flow` 固定实际全九向量的后六 shape，保 actual 当前前三 $p$ 作为初猜；显式 state 行仍拥有当前参数。`fully_frozen_flow` 固定全部九系数，构造新的零 active-parameter flow。两者都创建独立对象，不改输入 flow、profile 或 state。

传入的 probe/original-module 仍须具备真实 source closure。这个 wrapper 不提供尾 Robin/J，不伪造新的 TailClient，不把任何旧零响应缓存当成声明 C 的导数。

## 12. 仍然未付的实际搜索输入与执行范围

即使未来 144 得到完整且较窄的点两 jet，仍须真实提供准确 core、全部 recipe 控制和当前 C 的尾边界/线性响应。R318 已付的是完整 112 深端线性图；有限头到 cut 的传播、所有高度分母非零和真正非线性 DN 仍分别有责任。它们不由本 profile 的构造正常返回自动成立。

允许数值近似用于明确标示的搜索，但不能把任意旧零 J 或旧 readylineargraph 贴成新 C 尾。原 BVP/fullDN/最终几何验收必须在真正的新目标和真实状态上执行，预算/门不能由这里私自修改。

此次没有创建新科学 workflow 或选择新参数，没有派发 job，也没有未来 run/result SHA。下一个实际调度可将 v3 原 E 计算、点读回、此 factory 与新数值搜索安排在同一个受控任务内；必须在 source/provenance/原验收都明确后实际运行，不能把本接口登记当搜索成功。

所有新原始 model/domain/compilation 数据仅写调用方自有临时目录，之后先完整必要读回，再依 Rule15 清理。库内保源码、参数、run、哈希与紧凑结论；原来源小文本 blob 只用于当前受控交接，不移动分支。全文源差异和本地纯文本比较回执只是可重算审读资料，不作为新的科学门。
