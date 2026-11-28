# R730：完整 base / Q / calibration 接线与 pure 合同

## 交付状态

三份完整运行体与完整可逆文本再生器均已保护。它们在同一固定 Fejér 标量/图上采用新的 R730 length/inverse-arclength seed，尚未执行科学，不具有未来 point、model、normal roots 或费用。原 source、原完整失败与历史责任保留。没有新增 AST、fixture、预演或准入步骤。

| 角色 | basename | 字节 | SHA256 | Git blob |
| --- | --- | ---: | --- | --- |
| base | fixed_fejer_r730_meridian_operator.py | 40854 | b9c787340021b5736f2796f2b84a1c25cb4b0ce96333eb98f543b1e8923ce267 | 9dc7e423afe81a5f115f2dd60ad97fdff86d79a0 |
| Q | fixed_fejer_r730_literal_zero_moment_input.py | 37575 | 4e72d300388372ae9fa43ba1795be9ad3ed17805a45fd0c407c4f16ed4aa4d1b | 4d71d70d17976721e76d65045acd88e80bd9e284 |
| calibration | fixed_fejer_r730_reference_calibration.py | 11895 | 7650bbd18c856d70164a8b76eab22d63231d401cff91bf63f8b0bd5019b010fd | dd289d0f24c50cf3afddb7279305d66f697b3c43 |
| reproducer | reproduce_R730_complete_base_Q_calibration_sources.mjs | 46442 | d084f6f33a37be239f6c58eb86b74ac188eacdd7d98e5fd2d036005ae736fe69 | b104c19172ab4187f6236f3cb7b4ec420b6360ef |

四文件均在 `topics/visible-flex-larger-amplitude/scripts/resume_20261126/`。两数学核与完整接口父包是 `computations/R730-safe-cone-minimal-reference-complete-source-delivery.json`，9,725 B / `8f59f54e5cffe473c88ae91b2847c763e3a58512ca195bdecf322419ea7e432d` / blob `1dc015fc0e7039be74be60810cd1036bf3184d4c`。该完整文件保全部 kernel/provider/证明/输入来源，不在本包重复复制运行正文。

R730 完整证明是 `results/R730-whole-image-safe-cone-and-unit-speed-contracted-reference.md`，40,604 B / `362062d7b90d67e050130266d1c355f267fd97a4e604c5d657178efcdd35c7b8` / blob `41407fa22c569fad73a848ab603b885601066228`，已发表于 `3a38882e887dae0688835ccd9b1b41c7eb6d24c6`。

## 1. 真实物理父与计算父分开

三体的完整源码父来自 31 R728 demanded 族：

- base：40,877 B / `427227b006741b809fc728d4c4d23fe7fa59f2ccbf5e020e15fc8ed0b730168c` / blob `46c5227c3a839aa14695c75f4699b98478bf3cb1`；
- Q：44,554 B / `872dca4cf1e15c419aad68d31c053fc4f3465357a3e162413a19002f5b70e43d` / blob `d5d088cc53d7450fd90c8944de731e21a4e30917`；
- calibration：11,850 B / `00d50d208a19e7f75b431e3a8010bca068022539c82dbbb598c1f615b865ae8a` / blob `840613d36e1ff24fa19f9d0b086034e4faa622ca`。

完整父总绑定为 `computations/fixed-fejer-r728-demanded-current-runtime-binding.json`，74,756 B / `4af8d6d8ca43a8bc62005e091e0b3baddb6e0e382f0ba6c6ac62247678f3c4ea` / blob `d79fd8c5e889f826585cd4ddaf64aeadbc0ef369`。它包含全部 137 source pairs 和 23 current sources；这里只改变明确的新 seed 机制，不把旧 seed 仍称为当前物理模型。

root 已指定 R730 完整上层算法父为已刊 32 的 R729 common-slack 源族，提交 `6c07ca019af58f0102a40a00c63027948ee0332a`，driver SHA256 `501313cc50c2a877f98318193a8878242ec13c2f8a0664740a4ea8c47eb4baa7`；全算法来源由 solver 的新 family 总表完整记录。本文三体不实现、替换或删减该恢复 QP/fallback，不把两个父来源混成同一个物理场。先原 QP、原 dependent failure 时的全行 fallback、完整原预算仍由最终真实 upper 负责。

## 2. base：新 ctor 和完整模型，原 outer 数学不动

新 schema：
`complete-fixed-fejer-r730-so3-meridian-with-core-lift-v1`。

`ClosedMeridianOperator` 的实际新增/替换关键字为：

```python
length_parameters=length_kernel.LengthParameters(...),
length_kernel_module=length_kernel,
```

其余 parent/problem/prepared/cache/integration/angle-block/core-root 参数保持原接口。ctor 实际调用 `SafeConeUnitMeridianJet`，全字核新 provider，provider 再全字核 length kernel 和原完整 context。旧 `seed_parameters` / `seed_mean_kernel_module` 不作为可接受别名。

完整 base model 改为以下真实五键：

```text
fixed_safe_cone_unit_seed_model
fixed_safe_cone_unit_seed_identity_sha256
fixed_safe_cone_unit_seed_source_sha256
fixed_safe_cone_unit_seed_length_kernel_sha256
fixed_safe_cone_unit_seed_working_definition
```

整份原 axisymmetric reference model、固定 scalar model、初始 reference bundle、全 chart/core/mesh、全 M/J/free layout、固定 metric、current H 自由性仍保。model 的 `T0` 描述现在是六控制点 + 固定 eta + 单宽 pulse + 长度根 + inverse-arclength。没有旧 supported complement、Slerp 或半波身份被留作当前数学定义。

从 `initial` 至 `metadata` 之前全部原方法正文逐字相同；完整 `RotationH2Coordinates` 正文也保持原字。因此：

- 全 current core（除原固定前三）、三个完整 omega 通道与自由 H 保；
- 原 raw-defect lift、core inverse chart、全 Gauss/partial Lagrange 积分和全部六字段表达式保；
- residual、完整 J/J*、point covectors、domain 与保存/同模型 checkpoint 守卫保；
- 原 norm、径向 mass、angular scales、原冻结的 norm 选择与完整数组布局保。

metadata 的 seed 键相应改为 `fixed_safe_cone_unit_seed` / identity，反继承字段改为 `seed_length_inverse_not_a_certificate_for_current_closure_control_Jacobian=True`。其他科学方法没有为新 seed 缩域或改预算。

## 3. Q：原十八词与两泡保持，真正替换完整 seed 类型

新 schema：
`fixed-fejer-r730-reference-literal-zero-endpoint-Q-input-v1`。

新 definition schema：
`fixed-fejer-r730-reference-literal-two-bubble-endpoint-Q-v1`。

原十八个 binary64 Q 词、两个完整 (1/32,1/4,15/32)、(17/32,3/4,31/32) bubble triples、原反射 parity、05dc 参数来源/真实 trace/3618 B 参数文件都逐字保。当前 Q 仍是新 field 的固定控制参数，不自动声称原 working inverse 仍是新场的准确右逆。complete model/point/scalar/chart/source 等号仍完整检查。

旧 `_supported_seed` 与专用 R725 cutoff/R726 Slerp/R728 paired-halfwave 定义验证整块被新 `_length_definition` 和 `_safe_cone_seed` 替换；原完整旧 Q 文件作为明确完整父保留。这是数学类型改变，不是把旧 validator 守卫删除后接受任意来源。

`_length_definition` 纯 stdlib 重建 kernel 87be 的完整定义，并对整个 dict 严格等号比较。它核：

- eta=1/32、xi_max=3/4、k=6、全局 84 次 pulse、全部端口阶数和完整 domain；
- 原两项正 Gauss 阶数与完整最大阶，全部三个整数 scalar-root budget；
- canonical root-tolerance/Armijo binary64 words；
- exact length/inverse 方程、两角链范围、原 outer/normal 分离和所有未付 flags。

`_safe_cone_seed` 对整个实际 frozen seed 和 working dict 全对象严格等号，核新 provider/kernel、整个原参考和 scalar model、全部 160 chart identity、同 R690 radius、固定 H word、原 exact kappa0、完整 S enclosure、全部 923 个 canonical affine node 对、两个端点、922 胞和真实预算。完整模型来源由实际 caller/source binding 重读；这个 pure binder 不读取科学数组或自行证明积分、S 比较、单调性或 root。它仍明确 `current_base_array_and_source_validation_remains_callers_responsibility=True`。

原十二个 definition 字段中，两 seed 字段精确改为：

```text
fixed_safe_cone_unit_seed_model
fixed_safe_cone_unit_seed_identity_sha256
```

其他十个完整参数、scalar、reference、point 和 base 身份字段保留。provenance 的冻结键相应为 `safe_cone_unit_seed_is_frozen_before_current_free_point`。原 API `from_parameter_file`、`bind_new_input`、`bind_to_base`、`parse_literal_Q` 参数形状不变；旧输入类型自然被新 schema 拒绝。

## 4. calibration：实际新 reference 缺陷重新计算

新 helper schema：
`complete-R730-frozen-reference-working-calibration-v1`。

完整 endpoint schema 合同：
`complete-fixed-fejer-r730-detached-meridian-normal-layer-v1`。

新 reference-centering definition：
`R730-fixed-length-reference-centred-working-normal-definition-v1`。

ctor 现在核新 base/seed/length source 与 `fixed_safe_cone_unit_seed_model`。definition 的 identity 键为 `fixed_safe_cone_reference_identity_sha256`。原方法来源守卫、实际 core/cap owner、full base source、reference point 原 core/H/zero omega 等号完整保留。

从 `bind_field` 至文件结尾的全部科学正文逐字同父。特别是 `reference_data` 仍实际调用新 base 的完整 `_parent_tensor`，对同角的 T0/T0_phi/T0_phiphi 真积分，计算并保存全部实际 reference closure 三 jet；不会把 R730 的准确闭合定理当工作缺陷零。原 nodewise difference、完整 reference-centred equation、实际 raw lift、全角 derivatives 和每 point 的 raw/centered readout 全部保。

长度工作残差、partial Gauss 的离散导数差、工作 primitive 与积分 unit T0 的差仍明确未付。原 `accurate_reference_or_quadrature_or_geometry_certified=False`、`raw_reference_defect_forced_to_zero=False`、`numerical_radial_Gram_identity_claimed=False` 均保留。新 kernel 可逆性不能替代当前 closure-control Jacobian 的可逆性。

## 5. pure reader 抽取的完整依赖

Q 可直接作为纯 stdlib 模块导入，它不 import NumPy/Torch、不读取科学数组、不求 F/J/root。若 upper 沿既有 AST 纯函数提取机制，必须完整提供以下实际声明；这份名单不意味着在本工作中执行过 AST。

常量：

```text
SCHEMA DEFINITION_SCHEMA ORIGIN_SCHEMA ORIGIN_DEFINITION_SCHEMA
ORIGIN_DEFINITION_SHA ORIGIN_PARAMETER_FILE_SHA ORIGIN_PARAMETER_FILE_BYTES
ORIGIN_PARAMETER_PATH ORIGIN_TRACE_REPORT_SHA ORIGIN_TRACE_SOURCE_SHA
BASE_SCHEMA BASE_SOURCE_SHA SEED_SCHEMA SEED_PROVIDER_SOURCE_SHA
LENGTH_KERNEL_SOURCE_SHA PULSE_FLATNESS LENGTH_DEFINITION_SCHEMA
PARENT_COMPLETE_BINDER_SOURCE_SHA REFERENCE_SCHEMA REFERENCE_SOURCE_SHA
SCALAR_SCHEMA SCALAR_SOURCE_SHA EXACT_BUBBLE_NODES LITERAL_Q_WORDS
DEFINITION_KEYS OUTER_KEYS
```

函数：

```text
sha canonical json_copy is_digest require_digest _nodes _words _validate_origin
_canonical_positive_word _length_definition _safe_cone_seed _current_binding
validate_definition _validate_outer bind_new_input bind_to_base parse_literal_Q
from_parameter_file
```

namespace 为 `Fraction, hashlib, json, math, Path`。完整 CLI 的 `main` 仅供该 Q 源原独立 pure 入口，不需在 normal reader 中执行。不要继续抽不存在的旧 paired/cutoff/spherical helpers 或旧 polarity 常量。

其余 lower/upper 真正必要改动：所有 current source pin；base model 新五键；calibration schema/definition/identity；normal constructor 的新 seed/schema/length 来源；所有 root packet/metadata 的新长度根记录；source registry 明确 length 角色。旧 mean role 可以保完整历史 source pair，但不能用旧 mean 名将新 length root 伪装为旧 12 数组。当前 literal-angle root state、完整 prefix、xi 两角 jet 与旧 v/d/w/lambda 的字段不同，必须按实际源码消费。

## 6. 完整再生与来源验证范围

再生器读取三份完整父文件，核每一份 bytes/SHA；应用所有精确文本替换，产出三份完整新 source；从完整新 source 逆向恢复全部父正文并核同。base 13 组替换、calibration 14 组替换；Q 的完整新类型块及所有实际字段/源引用为 44 次精确文本替换。完整块文本全部在再生器内，不靠摘要、截断或未知外部 patch。

```text
node scripts/resume_20261126/reproduce_R730_complete_base_Q_calibration_sources.mjs \
  --source-repository COMPLETE_REPOSITORY \
  --generated-directory INDEPENDENT_OUTPUT_DIRECTORY
```

构造时的 V8 字符串正逆复演只证明所声明文本关系，没有执行该 MJS 的文件系统路径、Python AST、import、science、fixture 或 numerical test。不存在一个新增的 scientific preflight gate。全部 files <100000 B；原完整源与数学证明继续保留。

实际新 field、normal32、全角 jet 误差、完整 reference safe cone/grip/closed reach、R716、mesh 和来源完整 report 尚未产出。所有 future identities 为 null。root 管 refs/queue/launch，solver 管 R730 剩余完整 lower/upper，geometry 管这五个新物理源及准确 length/inverse 后继。原 31/32/33 运行或 source 文件均未改变。
