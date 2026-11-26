# 固定 moment-Q 零闭合完整求解器：显式选择一个新的初始自由高度

## 1. 本次范围与实际证据边界

本次提供一个独立、完整、可执行的初值入口。它从实际已刊 ff500 完整 driver、082b launcher 和 c942 纯 reader 派生，只允许在新的原参考初点上显式选择一个有限 binary64 高度 H。它不选择 H 的数值，也没有提交新的运行参数；支持外弦长入口 55ad 的真实高度区间返回后，再据该证据决定是否、以及用哪个单一全局 H 试验。

本次没有重新计算场、端点根、Gram、导数、几何或任何科学参数。全部数学场源码和 source registry 保持原样，完整求解循环也保持原样。新的 driver、launcher、reader 有各自独立的 source SHA 和报告 schema；旧报告不会被改成新报告。

已经返回的普通全弦长读取通过了原初点的完整角覆盖。因此不能把原 H 解释为已证实的通用弦长障碍。显式改变 H 的可能用途，是在同一固定目标和同一有限控制族内改变初始端点方程的右端，研究可达性和数值初值。它不是放宽根残差、球半径、几何筛选或完成标准。

本次依赖的已有数学责任见 [R695 完整局部闭合机制](../results/R695-so3-zero-closure-bubble-uniform-IFT.md)。本说明不重新证明 R695，也不声称当前候选满足其连续条件。

## 2. 完整源码与父来源

| 文件 | SHA256 | 字节数 |
| --- | --- | ---: |
| fullclosed_zero_moment_height_so3_qp.py | 34c9273aad6ccc3299c8b64ac250a37b3ae758eec34945ef00a4b14a3acaf1b3 | 65801 |
| launch_zero_moment_height_so3_actions.py | c1d3e0e5da47d3edef42124a8020cba705e99ac4b522c758ee195e8d575a58bd | 14459 |
| read_zero_moment_height_so3_report.py | 2e5b340d622993af55060f22d1dc26bd1cc451218feb27f8b8ce7b1366de1fe9 | 40458 |
| derive_zero_moment_height_entry.py | e996c9bf3dc0e8607a87a8289bac2bbaf4abef50771aa944675a24a6d6901f5e | 28638 |

这些文件的预定目录都是 scripts/resume_20261126。完整原始父文件保留：

| 父文件 | SHA256 |
| --- | --- |
| fullclosed_zero_moment_so3_qp.py | ff500abfa24de27c22f8a8993b9104cc265c5c96289a927c18755d318fbf0766 |
| launch_zero_moment_so3_actions.py | 082bb92e0e9f01067cf1bd8ecaae65cb559e38bba90dd79b97bf492c11d758f4 |
| read_zero_moment_so3_report.py | c942aa60db84698215e53dd2427a19c693ca73e6c3c8553ef0b73fa75edf295a |

这里 reader 的父版本是实际刊出的 c942 全体，不是早先的 94f 初稿。派生器只读这三个严格 SHA 匹配的完整文件，执行明确的纯文本替换，再验证输出的完整 SHA、AST、原函数范围和完整求解后缀。它不导入任何科学模块。

新 driver 从嵌套的 save_report 定义开始直至 EOF，与 ff500 **逐字节相同**。该后缀的 SHA256 为：

~~~text
9b05f8e00c483491ffd9259b2d675af940c6f0b8a8104d6bfcd70ffb0e31b4ee
~~~

父 driver 的全部 11 个其余顶层函数体保持同一 AST，仅 parse_args 和 main 的初始化部分改变。新的 finite_initial_height、explicit_height_seed、initial_point_record 是初值读取和来源记录函数，不构造科学场。原完整 SOURCE_PINS 对象完全相同。

特别是下列真实数学源码没有修改：

- 44ac53f1fcecceae55ed3b3230e1925292ce76ced85dc75f08e15ff0b70f5e4e：冻结 18 个字面 Q 参数的零闭合算子；
- e4a3271d829a1fc52080b0ac1bdb719f5a13065f23223e64288c77ea6bbc514c：该新表示的完整几何和所有原行适配；
- 4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611：纯 frozen-Q 输入绑定；
- 7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf：完整独立轴对称参考 base；
- 4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3：实际完整参考输入。

其他原观察、H² 坐标范数、谱目标、完整 J/J*、原全 C、永久位置、幅度、Phase I、真实筛选和历史入口的 source guards 也全部保留。

## 3. 参数与初始化次序

新增可选参数是 --initial-height。它接受通常的有限十进制 binary64 输入，或显式十六进制浮点字。真正赋给 H 的是该输入转换得到的一个 binary64 字；报告同时保留原 CLI 字符串、规范 hex 和这个字的准确有理数表示。十进制字符串不会被冒称为另一个未舍入的准确实数。

没有指定此参数时，完整原有三条路径继续存在：

1. 从原参考构造完整初点；
2. 从同一新 source/schema 的完整已返回 checkpoint/report 继续；
3. 按原 ff500 的完整守卫，用真正 606 全体的 checkpoint/report 作为所有原自由变量的种子。

指定 --initial-height 时，只允许第一条。它与 --restart-checkpoint/--restart-report、--seed-so3-checkpoint/--seed-so3-report 互斥，缺失一半的 checkpoint/report 配对也仍由原参数守卫拒绝。不会在一个已优化 checkpoint 上静默覆盖 H。

解析只要求 H 有限。原数学定义的完整 free vector 允许有限 H；真正的高度下界和幅度责任仍由原完整几何筛及 Phase I 处理。本入口没有添加一个与原全场检查重复或替代的正值、弦长或 IFT 准入门。

实际顺序如下：

1. 验证完整 reference、preparation、node、carrier、scalar 的真实输入与源码，重建原 base。
2. 读取并核对原完整 18 字 frozen-Q 定义与来源，完整构造 44ac 的 ZeroClosureOperator。
3. 在这次构造里仍照原规则验证 base.initial() 的整点摘要等于实际 trace 的原参考点 cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3；这里没有改参考、代理旧字段或跳过守卫。
4. 只有构造成功后，取得 q.initial() 的完整副本，记录原点身份，把最后一个原自由分量设为用户明确的 H 字。
5. 对非 H 前缀做逐 byte 比较；记录原/新完整数组摘要和前缀摘要，再核完整 q.model、base.model 的身份未变。
6. 保存 initial_free_point 和 initial_height_input 后，进入原 ff500 的全量初场读取、根判断、初始 Gram 和完整几何读取。该真实 baseline 只来自新的实际点。

SOURCE_PINS 与 q.model 不因 H 的取值改名。新 driver 的 source/schema 与输入点 digest 如实区分本次入口；场的数学定义本来就包含自由 H。固定 g、固定图、固定 scalar、参考文件以及 Q 定义的数学身份仍是原来的身份。

## 4. 精确的数学含义

在固定材料图 $\theta_0(\phi)$、当前完整 core 和当前全部 $\omega$ 自由量下，记

$$
P_H(\phi)=R e_r(\theta_0(\phi))+H e_z,\qquad
T_\omega(s,\phi)=\exp(\omega(s,\phi)^\times)T_0(s,\phi).
$$

冻结的控制矩阵 $W(s,\phi)$ 保持原来的完整 18 个字面 Q 参数及两段支持。端点方程仍为

$$
C(H,c,\omega,z;\phi)
=\Gamma_c(\phi)-P_H(\phi)
+\int_0^S\exp((W(s,\phi)z)^\times)T_\omega(s,\phi)\,ds=0.
$$

对于只改变 H 的初值操作，$T_0$、$T_\omega$、$W$、$\Gamma_c$、$R$、$S$ 和固定目标都保持不变。因此对任意两个高度，准确方程满足

$$
C(H_2,c,\omega,z;\phi)-C(H_1,c,\omega,z;\phi)
=-(H_2-H_1)e_z.
$$

这只说明一条明确的自由参数如何进入同一端点方程。它不保证新的 H 有根，也不保证同一数值球内的可解性或 Newton 回溯成功。

若在某个真实简单根处 $A=C_z$ 可逆，则由完整隐式微分有

$$
\partial_H z=A^{-1}e_z.
$$

该式中的逆和根仍须由实际场承担；源码没有因这一形式公式预填逆矩阵或删除隐式链。相应的场仍是

$$
F_H(s,\phi)=P_H(\phi)
+\int_S^s\exp((W(t,\phi)z(H,c,\omega,\phi))^\times)
T_\omega(t,\phi)\,dt,
$$

故在同一简单根分支上

$$
\partial_H F_H
=e_z+\int_S^s
D\exp((Wz)^\times)[(W\partial_Hz)^\times]T_\omega\,dt.
$$

H 的导数本来就在 44ac 的完整 implicit J/J* 中。此次改变初始值既不固定 H，也不添加新的角度相关高度；所有角度共用原来唯一的全局 H 自由分量，后续优化仍可改变它。全 core、所有旋转系数和 H² 坐标空间都保留。

目标依旧为

$$
g=ds^2+a_{\mathrm{deep}}(s)^2\,d\theta_0^2.
$$

改变 H 初值不会重新定义这个 g，也不会把新场的 Phi 与旧失败点或旧 h-Delta 场的 Phi 作未经同场读取的比较。首个新 baseline、所有接受步、最后的实际场与几何都由原完整循环重读。

原理上，支持外必要条件可以对特定原 core/零 omega/同一支持给出全角度共用的高度范围。这些范围是特定输入的必要性或充分通过该必要检查的范围；它们并不证明本有限 Q 族具有根。普通全弦长通过也不是根存在证明。本次未选择任何范围中的 H。

## 5. 新报告的完整初点记录

报告在首次 q.residual 调用之前包含以下两项。

### 5.1 initial_free_point

这项在所有种子路径上都存在，记录实际完整初始自由向量的：

- source_mode；
- full_point_sha256；
- float64 dtype、完整 shape、free_variables 和最后 H 的索引；
- height_binary64_hex 与 height_exact；
- nonheight_coordinates_sha256；
- 同一 model、fixed scalar 和 frozen-Q definition 身份。

它明确说这是首次场读取之前的字节身份记录，不把记录本身称为科学场求值。

### 5.2 initial_height_input

未使用参数时明确为 null。使用时记录：

- 原 CLI 字符串及其准确 binary64 字；
- 原完整点与新完整点摘要；
- 原 H 与新 H 的 hex 及准确 Fraction 字；
- 非 H 前缀的原/新摘要及逐字节相同断言；
- 原/新完整 dtype/shape 和唯一修改的坐标索引；
- 修改前后同一完整 model 身份，以及同一 base/scalar/Q/reference 身份；
- 原参考点已在改值之前完整核验；
- 参考输入、模型、目标、Q 均未改，H 仍是完整原自由变量；
- 没有继承旧 Phi、根或几何证书，H 输入本身不构成场接受。

如果用户恰好指定原 H 的同一个字，入口不会伪造一个不同候选：height_word_changed 为 false，原/新整点 digest 相同。这不触发额外科学准入条件。

首次根或场读取失败时，原 try/except 保存 actual_initial_read_error、initial_endpoint_roots 和失败未接受标记；上面的初点记录已经在报告里，所以不会被失败丢掉。若还没有真实 initial-new-field.npz 或 final.npz，纯 reader 仍可以读取失败报告。不能以不存在的 final 文件作为控制器的必需父输入来挡住这一读取。

## 6. 纯 reader 的身份核验与范围

reader 先保留 c942 的全部实际 source/model/reference/Q/目标守卫，然后检查新初点记录：

- schema、完整维数、dtype/shape、H 索引、全点与非 H 前缀的摘要格式；
- hex 与准确 Fraction 表示对应同一个有限字；
- 种子路径与 restart/direct-base-seed/height-input 的互斥关系；
- 使用 H 输入时，原点仍是 frozen-Q definition 指明的真实 trace 初点；
- 新点 digest 与 height_word_changed 相符，原/新非 H 前缀身份相同；
- 模型和目标来源全等，全部“不继承”和“未重算 Q”声明保留；
- 若初场成功，真实 initial.endpoint_roots 的整点摘要和 initial.domain.H 对应新的初点；
- 若初场失败，真实 initial_endpoint_roots 的当前整点摘要对应同一新的初点；
- 若后续优化改变了点或 H，不把最终点错误地要求成初点。

reader 只审来源和已返回 JSON。它不从数组重算 full_point_sha256，也不验证连续根、积分误差、连续 Gram 或连续几何。这一限制在新纯输出中写成 initial_point_digest_recomputed_from_arrays_by_reader=false。

以下新输出叶子均为标量，可用于控制器紧凑 summary；它们不需要把整个字典或方向数组塞进 scalar-only summary：

~~~text
explicit_initial_height_used
actual_initial_full_point_sha256
actual_initial_height_binary64_hex
actual_initial_height_exact
actual_initial_point_source_mode
initial_height_changes_target_or_model
initial_point_digest_recomputed_from_arrays_by_reader
~~~

原 c942 的 actual_metric_direction_count、actual_restoration_direction_count、接受方向计数、Phi、最大误差、失败原因和各几何标量保留。完整方向和根元数据仍在完整报告/纯 readout 中，summary 不能把这些数组误称为标量。

新的报告 schema 是：

~~~text
complete-independent-axisymmetric-fixed-deep-frozen-moment-Q-zero-SO3-explicit-height-QP-v1
~~~

纯 readout schema 是：

~~~text
actual-complete-independent-frozen-moment-Q-zero-SO3-explicit-height-readout-v1
~~~

命令记录 schema 是：

~~~text
public-actions-complete-independent-frozen-moment-Q-zero-SO3-explicit-height-command-v1
~~~

## 7. 静态验证与尚未执行的部分

已实际完成以下纯源码验证：

- 三个完整新体及派生器的 AST 与 compile；
- 无重复字面 dict key、无尾随空白；
- 三个完整输出由派生器重新生成后，逐字节等于交付体；
- driver 的 SOURCE_PINS 全等，save_report 至 EOF 完整后缀全等；
- reader 的原 9 个其余顶层函数 AST 全等，仅 read_report 增加初点来源读取和输出；
- launcher 与 reader 的纯 stdlib --help 可用；
- solver 代理独立静态核对了构造/赋值次序、非 H 字节保持、原 sourcepins、H exact 字和失败点关联，未见该范围的接口阻断。

这些检查没有运行 q.initial()、场、端点方程、数值根、J/J*、几何、参数界或科学 fixture。派生器只处理源码文本。它不是一次科学方向的实际返回。

本次没有设置一个 H 数值，没有填写未来 point/checkpoint/model 返回 SHA，也没有生成待执行科学步骤。未来若据 55ad 的真实同输入完整高度区间选择 H，应另写明确的完整新命令与 fresh 输出目录。可从真实 moment-Q 首次参数逐字保留支持、半径、容差、所有变量、所有观察、完整行、幅度、预算与永久位置；唯一科学输入变动是显式 initial-height。若要另外改变求根算法、种子来源或任何预算，必须在各自来源与说明中单独记录，不能归因为本次仅改变 H。

## 8. 本次完整发布

2026-11-26 16:25:05 UTC，root已通读上述完整说明和driver/launcher/reader全部差异，实际stdlib AST/compile及原SOURCE_PINS全等、save_report至EOF逐字相等均通过。完整四源码公开，未做本地科学、未选H、未生成新科学参数。03b中R696首完整计算仍运行，55ad已排其后；据该真实诊断返回后继续新输入，本文的完整代码准备不代表任何场或根已经通过。
