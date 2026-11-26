# 新 gamma 六控制 KKT 场的完整几何与原全部约束适配

日期：2026-11-26。本文说明一个独立新来源适配。它不是新的实际候选或几何证书；科学执行仍只允许公开仓库 GitHub Actions。新的 KKT 数学定义、条件可逆性、反射分支责任和完整 27 维隐式导数见 construction 的新增形状完整稿。本适配不重复那些证明。

## 1. 来源与实际物理场合同

完整父几何源码是 so3_zero_closure_moment_geometry.py，SHA256：

~~~text
e4a3271d829a1fc52080b0ac1bdb719f5a13065f23223e64288c77ea6bbc514c
~~~

新完整文件是 so3_zero_gamma_kkt_geometry.py，schema 为：

~~~text
complete-added-gamma-six-control-KKT-zero-SO3-world-geometry-and-original-192-amplitude-rows-v1
~~~

它只消费独立新 operator schema：

~~~text
complete-direct-R690-SO3-added-gamma-six-control-KKT-zero-layer-v1
~~~

最终 operator 与几何的实际字节 SHA 由同批 source-derivation.json 记录；带 UNLOCKED 标记的草稿不可作为科学入口。派生脚本会直接读取最终 operator 源码，核 SHA、schema 及实际物理/隐式方法属于该完整类。运行时还要逐一核 grid_fields、point_fields、point_vjp、prepare、domain 的代码文件字节与 model 中的新 operator 身份一致。

新算子的完整 core、全部原旋转自由量和末槽 H 都保留。六个内部控制与三个 KKT 乘子，以及它们的角 jet，是隐式内部变量，不追加到外层完整自由点，也不删掉任何原自由量。几何适配核：

~~~text
implicit_control_dimension = 6
KKT_dimension = 9
complete_second_angular_implicit_dimension = 27
implicit_control_cost = (|z/S|^2+|v|^2)/2
~~~

它还核实际 gamma 的三个准确相对节点与 model 一致、原冻结十八字 Q 的完整 canonical 定义一致、完整 base/reference/scalar 定义一致，以及整个 model 的 canonical hash。固定 Q 没有按当前场重算，也没有被称为准确积分的逆。

新字段只能声称选定一个 KKT 驻点分支。SOSC 与全局最小点都没有认证。几何适配不会把代价函数的名称当作已通过二阶充分条件，或把一个分散数值根当作已认证的全角连续分支。

### 两种明确区分的固定 Q 输入

旧 actual-moment 输入仍使用 frozen-zero-endpoint-moment-Q-input-v1 与 literal-two-bubble-endpoint-Q-v1，其原同参考守卫保留。重建参考场只允许另一个完整类型：

~~~text
new-reference-literal-zero-endpoint-Q-input-v1
new-reference-literal-two-bubble-endpoint-Q-v1
~~~

新 definition 精确含十项：schema、全部十八个 Q0_binary64_hex、exact_relative_bubble_nodes、fixed_scalar_metric_identity_sha256、完整 fixed_scalar_profile_definition、initial_reference_bundle_sha256、initial_reference_model_identity_sha256、base_model_identity_sha256、initial_full_point_sha256、fixed_chart_core_sha256。

几何适配逐项核新 definition 与当前完整 base、context、固定图及实际 base.initial() 的字节身份一致。source-pinned operator 还调用独立完整 binder，核其整文件以及实际 parse_literal_Q、bind_to_base 的代码来源，再读取所有十八字。旧模式不走这条新分支。

这些字在新参考场中是明确选定的常量参数。旧 05dc 定义、26b trace、7319 源只作来源记录，不成为新 definition 的当前数学身份，也不证明新场的实际矩逆。新分支的 frozen_moment_Q_trace_report_sha256 记录为 null，另报其真实 input schema 与 binder source；same_mathematical_g、current_working_moment_inverse 均不作继承宣称。新输入的定义 hash 必须由完整当前十项实际产生，本文没有预填未来的值。

## 2. 哪些完整算法逐字保留

从父文件的 GeometryScreen._set_x 开始直到 EOF，全部字节保留。这个完整后缀的 SHA256 是：

~~~text
50d6f1414807ea91710ecf3a0e3e52d9530a04f299763d2a05f30c372f27bf7e
~~~

全部顶层纯辅助函数和 Budgets 的方法也保持 AST 相同。唯一变化的类方法是 GeometryScreen.__init__，用于绑定真实新来源、模型、内部维数及新增 gamma 输入，并如实更改来源说明。完整派生器逐项核这件事，不以部分摘录或运行时替换冒充全体源码。

因此保留的算法包括：

- 对所有实际 grid block 读取完整六个 world jet，拒绝缺项、非有限值、重复角 block 或不完整覆盖。
- 全部永久曲率点与永久半径点的并集，及每个实际 trial 新返回极值的持久保存。
- 完整场上的两主曲率分支、实际当前全身半径、真实幅度与帽/H 标量约束。
- 原 e783 工作集选择器产生的完整前缀，连同新物理场的 point_vjp 和完整 coordinate transpose。
- 原缓存矩阵只扩容并写入追加行，不覆盖原前缀；全部原行身份和每行真实物理量、梯度尺度继续记录。
- 原有限几何筛选、完整全变量梯度和 Phase I 所需行单位。没有用新来源名放松旧筛选、删行或丢永久位置。

两份重用纯源的身份仍是：

~~~text
curvature differential a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854
complete selector      e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8
~~~

这些仅是坐标无关的曲率代数与工作集选择算法。旧 R671 场、旧点 pullback、旧候选值或旧几何证书均未被转用。

## 3. 世界坐标幅度与全部 core 导数

新完整场的参考见证点仍是

$$
p=(0,r_0,0),\qquad r_0=1+\sum_{\text{全部 core}}c_\nu.
$$

全 grid 和两套永久点的并集都实际读取

$$
g_D=4|F|^2/B^2-1,\qquad
g_{L,\sigma}=1-|F-\sigma p|^2/L^2,\quad \sigma=\pm1.
$$

两种符号始终保留。构建距离行时，先通过新完整 point_vjp 付

$$
-2(F-\sigma p)/L^2
$$

的 world 场 covector，再给每个原 free core 槽加入

$$
2\sigma(F-\sigma p)_y/L^2.
$$

这之后才应用完整坐标转置。没有把新内部 root 变量当作独立外层自由量，也没有冻结 p 或只给某个 core 子集导数。新增 KKT 的所有控制与乘子反作用都应由实际 point_vjp 的 27 维隐式链支付。

帽约束仍读取同一固定 R 和当前自由 H；body/marked 预算间的标记高度费用仍按原有理定义定向舍入。预算是所选 whole-image 见证的设计约束，不是对所有可能幅度机制的必要条件。

## 4. 坐标、对称与同分支责任

历史的 literal phi 地址在新表示中仍按固定父材料图的 phi0 读取。它是完整地址保存，不宣称跨表示对应同一物理点。新极值也以新表示的 literal cell/u/phi0 保存；没有传递历史点的场值。

六 jet API 保持：

~~~text
F, Fs, Fphi, Fss, Fsphi, Fphiphi
~~~

grid 可另带原 rho0 或 closure_delta 诊断；其它 KKT 统计应放在 metadata/report 中，不混入物理 jet dict。所有实际物理 jet 仍从同一个新场返回，不能取旧 Ty 充当已闭合修正场。

上半部分的 quarter 扩展依赖新定义的 polar-z/axial-v、原 Q 和 gamma 的完整反射/半转协变，以及所选根在相容轴端上的同分支关联。有限筛选没有证明这些连续分支责任。下半部的 z 反射沿用同端口定义；绝对曲率、半径与两个赤道见证距离按原对称关系读取。

若初始或 trial KKT 失败，算子应明确拒绝该候选；几何适配不以零根、旧根或旧场值补齐。如果产生完整数值场，普通有限 geometry pass 仍不等于全域 metric、embedding、reach 或 root 证书。

## 5. 静态验证与未执行范围

本次只运行纯文本派生、SHA、AST、compile、重复字典键/关键字及尾空白检查。没有 import 科学模块，没有读取候选 NPZ，没有计算新根、F、J、J*、曲率、积分或实际试验。

最终 source-derivation.json 应完整给出父源 SHA、已锁 operator SHA、新源 SHA/字节数、实际变化的 AST 方法与全物理后缀相同检查。若 operator 仍未锁，记录必须明确 draft_unlocked=true、executable_locked_scientific_source=false，不可提前排入公开科学任务。

发布后的第一实际消费者仍须以真实新输入与当前完整点构造新算子，完成其自身初场、全部原 C、幅度和永久点读取。此前的数学稿、source 复核及同场必要弦长检查都不替代这些实际返回。

## 6. 本次已完成的锁源结果

以下是源文件的实际字节身份，不是未来候选的身份：

| 完整文件 | 字节数 | SHA256 |
| --- | ---: | --- |
| so3_zero_gamma_kkt_geometry.py | 51803 | 0c4886237d642382a1ae329d36517d5752ba717f0fa1471993bb98769e828f17 |
| derive_zero_gamma_kkt_geometry.py | 15030 | 6af33f03a013a80639a5f558c762285646c54fbceba7a8ee2acde6b3604d6946 |
| 绑定的新 so3_zero_gamma_kkt_operator.py | 94323 | b712a24a0c0223356b4a53e6aa1fa78ba9cea66e4be39c7ee39931be99cb782a |
| operator 绑定的 new_reference_literal_zero_moment_input.py | 22763 | ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39 |

本次 source-derivation.json 的 draft_unlocked=false。纯派生过程确实读入并核对了 b712 完整源的 SHA/schema/方法，生成 0c488 完整几何源；它没有 import 或执行该科学算子。

除本适配的实际纯源验证外，还完成了对 b712 的独立静态审查：完整 closure 角 jet 对控制求偏导生成 stationarity 各阶，create_graph 保留全部 y 与乘子链；9/18/27 矩阵、角 jet 解算、缓存升阶、零值隐式 surrogate、sixjet 只消费六控制但保留全部乘子反作用均已读。新增输入分支保旧 validator 原字节，另核 ea94、当前完整 reference/profile/chart/初点与十八个实际参数字；没有跨来源重标签。失败阶段只存该阶段已求出的 K，并附矩阵自己的真实 state/iteration，不把它当成后来状态的矩阵，也没有因此新增 F/J/SVD。

这些均是源码和数学接口审查。新的 root、场、原完整约束和几何仍须以真实 Actions 返回登记。
