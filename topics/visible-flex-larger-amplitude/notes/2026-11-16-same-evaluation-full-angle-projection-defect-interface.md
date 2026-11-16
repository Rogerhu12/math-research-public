# R575：同次完整角投影缺陷库接口

作者：geometry agent（AI）  
日期：2026-11-16  
可信度：已证明（限 R575 的完整条件命题和本接口所列源码调用合同）

## 1　完成范围与实际入口边界

本次交付一份可执行 Python 库、完整纸证和本接口。没有 request、workflow、owner、reader、cleanup 或实际 run。库只供同次已加载的 R553 prefix-tube observer 使用，不复制 R521 数值内核，不直接执行 FFT/BVP/native/FD/fullDN，不改变原 metric 或 DFS 的决定。

R575 支付的是完整物理角上的准确参考非线性投影缺陷：
准确 finite DFT 合成速度与准确 Frenet 速度的差。
它不支付浮点 FFT、profile、trigonometric table、sqrt、RHS 形成差，不把原 solver RMS 变成连续误差，也不把 prefix 界扩大到 tail/collar/patch/caps。
R569 的 Q 与同次 literal cubic 比较仍须其真实 capture caller；本库不虚构已有该记录。

未来完整来源接线仅预留 R576/request241/R577。当前235/238、所有已运行件和原R553/R521保持字节不变。本接口中的调用示例是后继调用位置合同，不表示已在任何现有工作流调用。

## 2　正式文件与固定依赖

| 角色 | repo-relative path（均在 topic 内） | bytes | SHA256 |
|---|---|---:|---|
| 新库 | computations/geometry_20261116_same_evaluation_full_angle_projection_defect.py | 24673 | d2cfc1e35509486dd77f5f2ae4aecba3c0527b2e16b910be69540a73f3c2d6b7 |
| 完整证明 | results/R575-complete-cylindrical-projection-tail-and-alias-defect.md | 19690 | d5d6a045fb72fe00e90864e957942219aed30877d65459f0e8d27b1c1a077aba |
| 本接口 | notes/2026-11-16-same-evaluation-full-angle-projection-defect-interface.md | 以最终 manifest 为准 | 以最终 manifest 为准 |

现有实际运行依赖：

| 固定文件 | bytes | SHA256 | 使用方式 |
|---|---:|---|---|
| geometry_20261116_actual_prefix_coefficient_tube_majorants.py | 24412 | 81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b | 当前实际 R553 活对象；不另创建一份场 |
| geometry_20261116_finite_frenet_tube_residual_majorants.py | 18782 | 4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad | 通过该活对象实际加载的原 R521 API |
| geometry_20261115_shared_active_interval_balls.py | 33310 | 675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b | R553 原 binding 已核实际 prefix_coefficients 的定义模块 |
| alternative-outward-probe.py | 7708 | cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb | 准确网格/布局/reference 的原源码身份 |
| geometry_20261114_r225_outward_probe.py | 7542 | 64a3fd482f6ee01f4d149971dff1212b2c2ca3bdb00f1b733c7b119b458bab5f | 实际继承和 N 范围 |
| geometry_20261114_r225_high_core_bvp.py | 18350 | e12916dcf30dd2088ad59d2059647c8a03bed446aeee693b88f423730fa5a530 | 原完整 BatchedFlow reference |
| geometry_20261114_r225_free_core_bvp.py | 23914 | a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08 | BatchedFFTFlow 实际 synthesis/projection normalization |
| geometry_20261114_fft_frenet.py | 2143 | 973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401 | 原 even-grid 与 retained-below-Nyquist 合同 |

这些 reference 文件的存在与 SHA 绑定只是准确参考定义的来源责任；它不是 FFT 舍入误差证书。
新库读取当前 computations 同目录中的这些固定原文件。
不能通过只复制文件标签或伪造原 module 名称绕过真实模块/路径/SHA 绑定。

## 3　当前场和类身份绑定

实际入口：

~~~python
projection = R575.bind_loaded_projection_defect(prefix_tubes)
~~~

prefix_tubes 必须是当前流程真正创建的原 R553.BoundPrefixTubes 对象，已经绑定当前 current.field、Active、checkpoint、expression 和原 budget_check。

构造函数按实际 type(prefix_tubes).__module__ 查到它所属的模块，然后要求：

- 模块真实文件就是同目录固定 R553 文件，bytes 的 SHA 正确；
- SCHEMA 是原 R553 schema；
- module.BoundPrefixTubes is type(prefix_tubes)；
- 实际 api.frenet_directional_majorants 的定义模块文件/SHA 是原 R521；
- current.field.M 与该对象 M 相等，当前 field.saved.N 是同一个真实整数 N；
- N 是偶数且 N≥4M+4。

不是在 sys.modules 中随便选第一个同路径模块。675 的继承方法归属沿原 R553 actual_module 绑定，未把某个派生 class 名称当作675的身份。

后继 source view 必须按真实生成顺序登记新库及其实际 caller，不能把 R553 的既有四场族/source标签自动冒成当前235/238或未来联合 tuple 的完整注册。这里能接的是传入的真实已绑定对象，尚未生成新的 outer caller。

describe() 返回 SCHEMA+"-binding"，保：

- 新库完整 source_identity；
- 实际 R553/R521 source identities；
- 原 R553 完整 binding，含实际 checkpoint/expression/维数；
- 五个 reference 原件的完整源身份；
- 原预算回调、准确参考范围、当前缺失的 FFT 形成差；
- 新诊断不改变原接受/遍历的明确范围。

## 4　实际输入单位和模式

完整物理排列只有原始

~~~text
r0..rM, t1..tM, z0..zM
~~~

共3M+2个系数。所有频率2,4,...,2M保留，两个均值也保。
原上层若另有常数 augmented rows，它们仍由原 solver/BC 负责；本库没有以此删行或把 augmented 数组冒物理曲线。

角地址是原闭区间 q∈[0,1]，物理角 phi=2*pi*q。
B1/B2 的微分变量是 phi，不是 q 或材料角。
本库没有从 q 二阶界直接漏掉(2*pi)^2单位换算；它直接由原有限频率 n=2j 形成物理角导数。

准确参考固定径向标量 A、nu、mu 对 phi 的一、二阶导数为零。
当前准确 numeric-s 图中 nu=a_s*mu，而不是不经尺度变换直接取 a_s。
这些值来自同次 R553 实际 target return，未选择 C 盒中心。

物理角目标仍为 diag(mu^2,A^2*rho^2)。R575 输出的是 Euclidean 速度缺陷，尚未进行这个 target Gram 的归一化；它不会遗漏一个归一化 rho 后冒 metric bound，也不会把 rho 错乘进 Frenet P。

## 5　同次局部调用：只读已经返回的盒

在原同一个 metric evaluation 已得到原 R553 记录后：

~~~python
local_projection = projection.inspect(
    cell, local_result["actual_prefix_joint_tube"])
~~~

cell 使用原完整 dict；本库深拷原完整地址，不只选 piece index。
非prefix实际片返回None。prefix上要求同次记录的schema、original_cell、radial、prefix_span、angular、全部频率计数和物理维数一致。

消费的真实原字段为：

| 原R553路径 | R575用途 |
|---|---|
| coefficient_tube.complete_coefficient_box | 全3M+2列的实际准确区间；完整角一、二阶方向界 |
| coefficient_tube.radial/prefix_span/field_modes/physical_size | 当前闭径向片/实际维数绑定 |
| angular_box.angular/d/e/frequencies | 同一个完整闭角单元、d/e零阶包围 |
| scalar_box.A/mu/nu | 同一次准确scalar范围 |
| scalar_box.actual_same_target_return | 来源身份，不另查target |
| joint_invariants.P/W | 同一完整独立盒的正域下界 |
| available/reasons/error | 原未付原样分责，不转成功 |

R575 不重做 coefficient Bernstein 或 interval trig，不调用 evaluate/target/refine，不重扫域。
它对完整系数绝对上界作有限和，通过原 R521.norm_upper 转成完整三向量范数。
d/e 的角导数按实际旋转基分量三角多项式求，不使用错误关系 e=d_phi。

接着对同一个原domain调用两次原 R521.frenet_directional_majorants：

1. 方向(d_phi_upper,e_phi_upper,0,0,0)，取得first_upper和second_upper；
2. 方向(d_phiphi_upper,e_phiphi_upper,0,0,0)，取得first_upper。

输出 B2 是第一条second加第二条first，完整保非仿射链式项。没有复制或修改原R521公式。

局部返回 schema 是：

~~~text
R575-same-evaluation-complete-angle-projection-defect-v1-cell
~~~

其中保原cell、R553完整原记录identity、实际domain/同target identity、全方向范数、两次完整原R521结果、B1/B2、错误与reasons。
available=true只指本局部成分可用；局部记录明确不构成整圈Fourier证书。
原R553不完整或P未付时，返回available=false及原原因，不调用原metric拒收。

## 6　原split/retirement仍唯一

在原 traversal 已经决定 refine/split 后，与原 R553 的退休调用并列附记录：

~~~python
record["actual_prefix_projection_retirement"] = (
    projection.commit_original_retirement(
        cell, local_projection, split=refine))
~~~

refine直接来自原数学决定，本库不计算替代值。
split=True只把责任传给原全部children；既不支付父叶，也不删子叶。
终叶只有与同cell对应的完整local record才计paid。
失败终叶记录完整地址、原因、evaluation error和retirement error。

完整 local_projection 与退休记录必须写进原同一临时cell ledger。每条完整原记录的文件身份和行序由原账本负责。
本次库没有写文件或清理权，也没有把“成功摘要只保identity”解释成完整科学记录可以丢弃。

## 7　整体结束与必要摘要

原DFS结束后，复用它实际的五个参数：

~~~python
projection_summary = projection.summary(
    original_coverage=coverage,
    complete_cell_ledger=cell_ledger_identity,
    original_error=error,
    original_stop=stop,
    close_errors=close_errors)
~~~

本函数在同一个R553活对象上调用summary，读取其已发生的原计数。
这是metadata回读，不重新求场或运行DFS。
只有原R553完整prefix cover为真，且R575 observed/committed/split/terminal与该活对象逐项相等、每个终叶paid、未付为零，才给全域投影界。

整体schema：

~~~text
R575-same-evaluation-complete-angle-projection-defect-v1-necessary
~~~

主要字段：

| 字段 | 准确含义 |
|---|---|
| complete_prefix_physical_angle_projection_bound | 全原prefix/全物理角条件是否完成 |
| global_prefix_exact_reference_projection_bound | 完成时的完整准确参考尾+alias界；未完成为null |
| global_prefix_V_rot_phi_upper | 完成时原全域一阶角界 |
| global_prefix_positive_P_lower | 完成时同域最小正P |
| observed_paid_leaf_extrema | 无论完成与否的真实已观察局部极值；明确partial时非global |
| observed/committed/split/terminal/paid/unpaid计数 | 和实际原退休关系，不用统计代替覆盖 |
| first_unpaid_terminal/last_unpaid_terminal | 原具体错误和地址 |
| complete_original_cell_ledger | 同一个完整临时账本identity |
| original_coverage_object_in_same_result | 指向原结果中的coverage，当前frontier及未访根不改 |
| phase_scope/unpaid | 相位有效范围和仍未支付的原科学责任 |

不得把global字段null解释为零，不得把observed max当作complete upper。
完整ledger行没有在这份必要摘要中全部返回；接口明确保原件身份和原必要选择责任。

后继reader须在正常与recovery路径都保这份完整必要对象、原错误和未访引用。
本次没有改任何必要reader或cleanup marker；原90000字节上限、超限70、quiet和保raw规则都仍在。
不能预称新增摘要必然适配90KB，也不能把原大ledger编码/分包上传以绕过限制。

## 8　完整有理上界的纯函数

实际条件函数为：

~~~python
R575.conditional_uniform_projection_bound(B2, M, N)
~~~

它只接准确Fraction/int/rational字符串，拒float/bool。
这是显式条件函数；调用者必须已证明B2为同一个完整圆周上的
rotating-component二阶Euclidean界及原奇偶/π周期/固定sigma。
它不会从传入数字自己创造这个证书。实际observer只在第7节完整条件成立后调用它。

输出保两项完整tail/alias方案：

$$
T=\frac{B_2}{2M},\quad
A_1=\frac{4(2M+1)B_2}{(N-2M)^2},\quad
A_2=T,\quad
\|\Pi v-v\|_\infty\le T+\min(A_1,A_2).
$$

并保retained signed frequencies、N行原grid的首末index、Nyquist、两个均值、向量norm约定、全无限尾与别名已计入。
原正频率系数2/N、零频1/N、T的负imag和inverse1/N都在R575正文推导，未用另一套DFT约定替换实际来源。

## 9　全phase的合法使用

本界是在原完整物理角上证明，因而已构造基场缺陷的相位平移上确界不变。
已付的径向独立准确材料拉回和世界正交变换保持此向量缺陷的覆盖/范数。
实际rho正性、映射方向、帽图粘接及当前准确同场关系仍沿原来源负责。

不允许把“上确界在平移后相同”误写成原固定grid/parity projection与任意平移交换。
平移后的R/Z分量一般不再关于零点偶、T不再关于零点奇。
合法对象是原缺陷的准确拉回，或显式共轭后的projection/grid/basis。
本次没有新增全t FFT试验，也没有把端点t代全t。

反射可能变Frenet binormal符号；两个固定sigma的同界可用，逐角任意换号不可用。
材料角坐标转换不能不带导数因素地重解释B2；本实现始终在物理phi上构造它。

## 10　当前仍未付的责任

本次实际库和R575纸证没有声称完成以下事项：

- 原rounded FFT/trig/profile/sqrt/normal/binormal/RHS形成差；
- 原nominal scalar对同一准确C target scalar的差与比较路径；
- 原literal solver cubic残差及其完整采样/闭域传播；
- 除当前Q-only R553盒外其他曲线的membership；
- 原worker具体root/sigma的识别或改变；
- tail/collar/cut patch/cap的另一套Frenet系数模型；
- anchor、角度量及全闭面relative-metric floor；
- 实际误差下降、有限资源成功、M/N提高后的B2一致控制。

R575的作用是给上述分解中一个已有明确位置的真实可算项。
即使它已经很小，也不替代原四Loewner/全DFS；未付也不作为拒绝原场的新门。

## 11　运行与来源限制

全部数值只在 Rogerhu12/math-research-public 的公开Actions中执行。
库构造和公开算术函数检查GITHUB_ACTIONS/GITHUB_REPOSITORY；
作者只编写源码、按实际原源做文本推导和身份哈希，没有本地import/AST/compile/fixture/test/科学计算。

预算回调与sqrt_bits由实际R553对象继承，无新钟。
每个全模态循环和原majorant调用前使用原callback。
数学异常只记录diagnostic未付；当前原RuntimeError类资源中止不被数学catch吞掉，MemoryError也不被吞掉。
后继若换资源异常类型必须保持同一穿透语义，不能用诊断catch延长原科学预算。

本库无CLI，不启动child、不改变owner、不设置cleanup许可。
完整的后继R576来源接线须显式保存原binding、实际同一次field/target/cell、完整ledger/必要摘要、原clock/quiet。
当前所有科学raw只留同job临时，完整源码/证明可发布；不得上传可再生科学raw或原necessary正文为Git blob。
