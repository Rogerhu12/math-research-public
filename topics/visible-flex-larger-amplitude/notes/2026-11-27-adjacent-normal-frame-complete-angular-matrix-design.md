# 相邻 normal frame 装配完整 J6/J9 的数学与源码合同

日期：2026-11-27。状态：完整解析及实施设计，尚未实现新数值 producer，未执行科学计算。它是 R714/固定 normal 链的一项独立成本后继，不作为已准入材料包络入口的前门。

当前逐字核对来源是完整矩阵复用 revision2：算子 d461f660063bfa2aeecc724050d71c6ef98143b9129f7cfe34f22e4043488a7f，96949B；stage helper 375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59。其 _run_chain、_get_roots、_normal_frame_jets、_stage_jet_jacobian、_stage_constraints、_stage_control_jets、_implicit_jet_value 为下述源码判断依据。这里不声称它们已有本后继优化。

## 1. 具体重复计算与保留范围

原 _run_chain 按共同固定分割逐阶段读取上一控制的完整 normal frame，解3未知量的原阶段根，再完成其一阶/二阶角 jet，完整复读原阶段方程和最后端点方程。每个实际角的 root cache 保存所有阶段 eta、frame、controls、J3、record。

当外层需要参数 J/J* 时，_get_roots 又按同一完整点的实际角键读取这些已选阶段，并对各阶段重新调用完整 _stage_jet_jacobian。这个方法对6或9个输出逐个调用 reverse AD，生成整个 J6 或 J9。现有 detached matrix cache 可在完整同字时复用此前实际原矩阵；对没有这种命中的不同阶段，仍逐阶段执行全部 reverse rows。

相邻阶段中的 frame 存在另一种准确关系：第 i+1 阶段的上一控制，正是第 i 阶段已经选定并保存的最终控制及其全部所需角 jet。因此，第 i+1 阶段已经付出的 frame 可以提供第 i 阶段端点映射对当前控制的完整导数。最后阶段没有后继 frame，需在已经选定的最后控制上补算一次。

这个方案仅候选替换 _get_roots 的 detached 完整 angular-matrix producer。它不改变：

- 共同准确分割及全部 m=32 阶段；
- 原 _solve_stage 的 Newton、J3、控制域、回溯或根选择；
- 原 returned-value J3 以及完成 eta_phi、eta_phiphi 所用的原线性解；
- 每一阶段实际 eta/control 字、最终已选 root 分支；
- active 全阶段残差、zero-target、上游 frame 与控制的完整外参数链；
- 原全部自由变量、固定参考 seed、H、准确 g、范数、正权、全部行和真筛。

因此它不以减少未知量、减少阶段或用最后三方程替代全链获得成本下降。

## 2. 独立角 jet 与完整 frame 的含义

固定完整自由点 x。设无量纲、参考中心化端点映射为

$$
f(u,x,\phi)\in\mathbb R^3,\qquad u\in\mathbb R^6.
$$

固定 seed 与 x 无关；当前全部 omega/core/H 依赖仍在 f 中。任何来自准确/数值参考的费用都没有因本符号分析消失。

对一条所需光滑控制曲线 u(phi)，写

$$
u^{[j]}=D_\phi^j u,\qquad A^{[j]}=D_\phi^j f_u(u,x,\phi),\qquad j=0,1,2.
$$

为读 A 的总角导数，先把 U=(u0,u1,u2) 视为独立 jet 变量，定义

$$
g_0=f(u_0,x,\phi),
$$

$$
g_1=f_\phi+f_u u_1,
$$

$$
g_2=f_{\phi\phi}+2f_{\phi u}u_1+f_{uu}[u_1,u_1]+f_u u_2.
$$

完整 source 的 _closure_jets 正按所选实际积分与六维旋转控制计算这些 jet。对独立的 u0 作偏导，u1/u2 保持独立，就有

$$
\frac{\partial g_j}{\partial u_0}=A^{[j]},\qquad j=0,1,2.
$$

例如 j=2 时，

$$
A^{[2]}=f_{u\phi\phi}+2f_{uu\phi}[u_1,\cdot]
+f_{uuu}[u_1,u_1,\cdot]+f_{uu}[u_2,\cdot].
$$

没有把 A2 简化成仅显式 phi 二阶偏导；当前控制的一角、二角项都在内。原 _normal_frame_jets 对完整 closure[:,j,k] 作 grad(local)，再取 local[:,0]，正实现上述独立 jet 偏导。此接口也保 active x 与 previous 图的全部边。

以下推导只要求这些经典导数存在。现有限实际来源具有其声明的所需混合正则性；它不扩充到任意仅 C² 的无额外混合导数场。

## 3. 每阶段原方程

设阶段 i 的上一控制为 p_i=u_{i-1}，对应 normal frame 为

$$
B_i^{[j]}=D_\phi^j f_u(u_{i-1},x,\phi).
$$

按原 source，阶段未知量 eta_i 是三维，控制是

$$
u_i=p_i+B_i^T\eta_i.
$$

完整角 jet 展开：

$$
u_i^{[0]}=p_i^{[0]}+(B_i^{[0]})^T\eta_i^{[0]},
$$

$$
u_i^{[1]}=p_i^{[1]}+(B_i^{[1]})^T\eta_i^{[0]}
 +(B_i^{[0]})^T\eta_i^{[1]},
$$

$$
u_i^{[2]}=p_i^{[2]}+(B_i^{[2]})^T\eta_i^{[0]}
 +2(B_i^{[1]})^T\eta_i^{[1]}
 +(B_i^{[0]})^T\eta_i^{[2]}.
$$

第 i 阶段残差三 jet 是

$$
G_i^{[j]}=D_\phi^j f(u_i,x,\phi)-(1-\tau_i)z^{[j]}.
$$

在本阶段的局部增量偏导中，完整 p_i、B_i、z 与 tau_i 固定。它们在外层 x 导数中并不固定，这两个偏导层次不能混同。

## 4. 完整 6/9 维 Jacobian 的块公式

设当前控制处

$$
A_i^{[j]}=D_\phi^j f_u(u_i,x,\phi).
$$

将阶段增量作任意变分，并记

$$
M_i^{[j]}=D_\phi^j\bigl(f_u(u_i,x,\phi)B_i^T\bigr).
$$

Leibniz 法则给出

$$
M_i^{[0]}=A_i^{[0]}(B_i^{[0]})^T,
$$

$$
M_i^{[1]}=A_i^{[1]}(B_i^{[0]})^T
+A_i^{[0]}(B_i^{[1]})^T,
$$

$$
M_i^{[2]}=A_i^{[2]}(B_i^{[0]})^T
+2A_i^{[1]}(B_i^{[1]})^T
+A_i^{[0]}(B_i^{[2]})^T.
$$

局部 eta 变分下的 RHS 项严格为零，因此

$$
\delta G_i^{[0]}=M_i^{[0]}\delta\eta_i^{[0]},
$$

$$
\delta G_i^{[1]}=M_i^{[1]}\delta\eta_i^{[0]}
+M_i^{[0]}\delta\eta_i^{[1]},
$$

$$
\delta G_i^{[2]}=M_i^{[2]}\delta\eta_i^{[0]}
+2M_i^{[1]}\delta\eta_i^{[1]}
+M_i^{[0]}\delta\eta_i^{[2]}.
$$

于是完整矩阵是

$$
J_{i,6}=
\begin{pmatrix}
M_i^{[0]}&0\\
M_i^{[1]}&M_i^{[0]}
\end{pmatrix},
\qquad
J_{i,9}=
\begin{pmatrix}
M_i^{[0]}&0&0\\
M_i^{[1]}&M_i^{[0]}&0\\
M_i^{[2]}&2M_i^{[1]}&M_i^{[0]}
\end{pmatrix}.
$$

每个 block 是3×3，所得完整矩阵仍为6×6或9×9。原所有 eta 的一角、二角未知量都保留；零上三角块来自完整方程的因果 jet 结构，而不是丢弃未知量。

在准确算术中，完整 J6/J9 可逆当且仅当 M0 可逆，行列式分别为 det(M0)² 和 det(M0)³。这只是结构关系；本来源尚未对任何实际角给出可逆性、条件数或误差证书，也不能将它当作成功求根的保证。

## 5. 相邻 frame 身份与最后一项

原阶段定义立即给出

$$
A_i^{[j]}=B_{i+1}^{[j]},\qquad 1\le i<m,\quad j\le q,
$$

其中 q 是本次实际请求角阶。因为下一阶段的上一控制曲线就是当前阶段的最终控制曲线，固定 x 与材料角也相同。这个等式不需要 u_i 与 u_{i-1} 相同，不依赖原同字缓存是否命中，也不要求 tau 均匀。

因此所有 i<m 的 A_i 可以由已有的下一阶段 frame 读取。最后一项

$$
A_m^{[j]}=D_\phi^j f_u(u_m,x,\phi)
$$

需在本次已经保存的最终控制 u_m 上读取一次完整 _normal_frame_jets；不再解 eta，不改变 u_m，不改变最后根的原复读结果。

m=1 时同样成立，只是没有任何相邻项可复用。这里没有把“只多算一个末 frame”当成可忽略或已经支付的实际成本，新的 producer 必须记录该次原调用及其全部计数。

## 6. 当前源码的真实字链及其缺少的显式 provenance

当前完整 _run_chain 的次序是：

1. 初始 previous 为同批全零三角 jet。
2. 本阶段 frame_values.frame(previous,index-1) 读取完整 frame。
3. 原 _solve_stage / _finish_stage_jets 产生 eta 和完整 controls。
4. 原阶段方程、域与物理端点容差完整复读。
5. 把 eta、frame、controls、J3 的实际 numpy copy 存入 all_stages。
6. 执行 previous = controls.detach() 后进入下一阶段。

detach 不改变数值字。因此同一新链中，在相同 dtype/shape/角序下，第 i+1 阶段读取 frame 的 previous 三 jet 与第 i 阶段最终 controls 字相同。最后返回的 Z 也来自最后 previous。

源码还处理阶1→阶2的同分支升级：先补新阶，再把旧 frame0/1、eta0/1、controls0/1 的字强制保留，并作完整旧字一致性检查。前两阶没有被高阶升级悄悄重选。相邻关系应以本次完整 root item 的当前 order 为准，不能把另一阶缓存补零后冒充。

但旧 stage record 没有单独序列化“本 frame 输入 previous 三 jet”的逐角字摘要。不能在新来源里声称某个旧 raw cache 早已提供不存在的 provenance。

一个完整新来源应在 frame 实际读出位置增加纯 metadata：

- 当前整个模型、自由点与 ordered angle batch 身份；
- 该实际角的完整 previous 三 jet 摘要和 dtype/shape；
- 实际 frame0/1/2 的摘要和 requested order；
- 是否沿原同分支升级，以及哪些低阶字来自已选原缓存；
- 对应阶段 ordinal 与完整准确/工作 tau 身份。

这不改变原数值方程，只给实际 next-frame 输入增加可机核的来源。后继 producer 必须逐角逐阶段比较这些记录与上一阶段最终 controls 的完整字，并核最后 controls 与 root item 的 Z 完整相等。

新来源不导入旧源 root cache。若从旧 complete final 继续，只沿已经声明的 full-variable seed 接口导入原自由变量字，随后在新来源重新生成全部实际根与 provenance。因此不需要假补旧 raw root 的字段。

## 7. 完整 producer 接口草案

独立 helper 的预期接口为：

    producer.prepare(data, ordered_phi_keys, selected_root_items, order)
        -> actual_matrices_by_stage, provenance

输入仍由当前 _get_roots 的实际 detached subset 给出。数据批包含全部原径向积分节点、当前 T/Tp/Tpp、完整 W/Wp/Wpp、current/reference core/cap、zero目标等；不能因为这些部分在局部矩阵里不显式出现而削弱同场绑定。

返回保留 m 个完整批矩阵，每个形状为 (A,6,6) 或 (A,9,9)。_get_roots 仍逐角逐阶段写回实际 jacobian 与 jacobian_order，不变成一个末阶段矩阵。

完整工作次序应为：

1. 核当前 q/model/source/free-point，全部 selected root item 的 current order、准确分割、完整来源与有限字。
2. 对所有角、所有相邻阶段核第6节的 previous/control/jet 字链。不得仅以近似相等、计数相同或同一角名通过。
3. 读取既存相邻 frame。每个 frame 在其实际来源批次中已经计算；new producer 记录这个来源，而非声称当前子批重新 AD 产生了相同字。
4. 将每个角的最后完整 controls 按本次 ordered batch 组合，在同 detached data 上调用原 _normal_frame_jets 一次，得到全部末 frame。
5. 对每个 i 计算所需 M0/M1/M2，装配完整 J6/J9；每一矩阵独立检查形状和有限性。
6. 保存实际矩阵来源和实际 frame/乘法/存储成本。任一失败保持完整已选 root 状态，并如实报告本次数值线性化未完成。

数学上 A、B 只需所请求的前 q+1 阶；来源核仍应保完整实际三 jet 字，避免拿一个不同状态的高阶字段冒相同 root。order1 与 order2 分开产生矩阵，不能借本方案改变原根升级政策。

旧 _stage_jet_jacobian 可以作为明确标记的实际 fallback；如果采用 fallback，必须真实调用原方法并报告其来源/成本。不能把 fallback 的数值当作该 frame-product 路径已经执行，也不能为将来的故障预填成功字段。

## 8. 最后一项不会重新选择 root

末 frame 的输入严格是已经保存的 Z/最后 controls，且只是局部 f_u 的计算。完整 _normal_frame_jets 在 detached 模式只读同一数据与控制，执行自己的局部偏导，不调用 _solve_stage，不更新原 eta，不改变固定参考、不改变 H 或外变量。

实施前后应核：

- 全部 m 个 eta/control/J3 原数组逐 byte 不变；
- 最终 Z、zero 与原 root record 不变；
- 固定 reference_point 和 base.initial 摘要不变；
- current model/current-point 尚为同一个明确来源。

这里的“保持 root”是固定已选实际字的合同，不是宣称原 root 是准确根或跨所有角属于一个已认证光滑分支。原根残差和 branch/连续费用仍按自己的报告与 R707 责任处理。

若末 frame 不可用，即使先前所有根数值返回，也只能说线性化失败，不能反推没有几何解，不能自动更改 m 或固定分割来制造另一模型。

## 9. 浮点定义与 active 全链

准确算术等式不意味着下面三种矩阵逐字相同：

- 原 _stage_jet_jacobian 的完整 reverse AD；
- 现有 detached cache 复用的先前实际原矩阵；
- 本候选由已存 adjacent frame 和末 frame 作浮点乘加后装配的完整矩阵。

不同角批、归约次序、局部输入布局和乘加次序都可能改变工作字。因此本方案必须声明独立的新数值矩阵来源、model identity 与完整 source pin，报告具体使用哪一种矩阵；不能把它仅写成原 AD 的标签别名。

原 active _implicit_jet_value 继续按全部阶段构造真实本源 residual 图，保原 p_x、B_x、zero_x、当前 x→T/core/H、全部控制链。它使用新 detached 完整矩阵来完成相同维数的隐式一阶 solve。不能把 adjacent frame 的 detached 数值替换成 active frame 图，也不能省去任何上游 Jacobian 边。

这里不要求计算外参数 Hessian；若以后需要对所得 J 再求导，必须另外处理已 detached 的矩阵依赖。当前一次 J/J* 和对应原 Gauss–Newton 运算仍按其既有范围声明。

数值矩阵与准确矩阵的偏差、隐式线性解残差及误差放大均未因块结构自动支付。R707 的完整矩阵/角 jet/参数链费用可以消费新的真实矩阵误差输入，但本说明没有生成这些误差，也不把 stage frame 的工作值当作 outward interval。

## 10. 严格成本比较及不成立的扩大解释

在一个固定 requested order=q 的完整、尚未缓存 full angular matrices 的批上，原 _stage_jet_jacobian 每阶段进行 3(q+1) 个 reverse products。若没有同字矩阵复用，m阶段是 3m(q+1) 次。

这些阶段进入 _get_roots 前，_run_chain 已经取得 B1,...,Bm 的所需完整 jet。本方案只另算 Am，所以需要一套 3(q+1) reverse products，加上每个阶段的完整 frame 乘加/矩阵装配。对m=32，一阶最多可免去186个该分支的 reverse products，二阶最多可免去279个；“免去”只指本分支原需执行、且没有其它cache命中的那些调用。

这些数目不是实际 CPU 时间或整个算法成本。原阶段根/Newton、root angular solves、active 参数图、scalar/mean provider、QP、C rows、真几何和所有其它成本仍在。frame的输入维数6也与原 eta 的3维偏导路径不同，不能仅按 reverse 调用数断言实际同一单位成本。

若当前同字矩阵cache已经把32个请求合为一次实际原 J6/J9，新增末 frame 的成本可能与那次原 AD 相近或更高，且另有矩阵乘加。因而本方案没有普遍优于现cache的结论；对一般非相同的阶段控制，它提供了一个不依赖相同字命中的明确避免重复的机制。实际采用与预算应由完整真实方向的成本返回决定。

这也不是降低完整科学精度的建议：不变 m，不减少角/径向节点，不删原自由量，不削减任何 geometry/幅度/typed 责任，固定参考仍来自原完整初点而不是替换成旧 final。

## 11. 完整来源、缓存和历史责任

未来完整入口必须同时完成新 helper、new normal/model、独立 calibration schema、geometry/source guard、driver/launcher/reader 与全部参数闭包。原九个数学方法可保全文，通过独立的 angular-matrix producer 改变 _get_roots 的调用；其新政策不能冒称自己所有矩阵都由旧原 AD 得到。

新的缓存只收本新来源实际生成的 root/frame provenance。同来源重启须完整校验；跨来源只迁可证明相同布局的全部自由变量以及全部实际地址/typed 责任，不迁旧 roots、旧矩阵、旧数值可行性或证书。

若前驱已有完整 accepted final，不应因新增优化默认重新从原初点做方向；先保全部原自由变量字为新输入，再新读该来源的初 Phi、根、六 jet、全部旧地址与 typed 行。若只有首次场失败终态，则可显式选择原参考初点，同时保失败前实际已有的全部责任。现在没有预选尚未返回的前驱状态。

本说明不修改已经锁定或准入的任何源，不要求一个额外 fixture 或预试。任何实施都必须保存原当前入口的实际返回，不能用新缓存 policy 解释尚未返回的长时运行。

## 12. 当前已完成与剩余

已完成：原 source 完整次序核对，独立 jet 偏导恒等式、全部 M0/M1/M2 和 J6/J9 块公式、相邻与最后 frame 的准确关系、原同分支升级路径核对、实际 provenance 缺口与完整补法、浮点及 active 链责任、严格条件成本计数。

尚未完成：本新 producer 的可执行源、全部新来源闭包、实际完整参数选择、任何运行成本/命中/误差或物理场结论。它不会替代当前已锁矩阵复用入口的科学状态，也不会以少一个旧运行作为历史责任的豁免。

## 13. root 独立源码复核与请求阶边界

root 已完整读本稿，并从锁定 d461 算子全文提取、逐项读取 `_run_chain`、`_get_roots`、`_normal_frame_jets`、`_implicit_jet_value`，确认实际 `previous = controls.detach()`、完整保存/只读数组、同分支低两阶保留和全部 active 阶段链均与上述推导范围一致。这里仅是完整源码和符号审查，没有导入科学模块或执行矩阵/场/fixture。

还须保一个原调用分支：当前请求 order=1 时，缓存的 root item 可能已为 order=2，而其 angular jacobian 尚未生成。新 producer 不能硬要求 `item.order == requested_order`，也不能重选或降级该已选高阶根。应保全部实际三 jet 与其原来源，按请求使用前 q+1 阶，并在 provenance 中分别记录实际缓存阶和本次矩阵阶。旧完整 source 本就允许这一情形。

前后字保护应包含原 eta/control/J3/zero/Z 及根记录，不应误把本次明确新增的 `jacobian` 和 `jacobian_order` 当作禁止更新字段。本次只正式发表完整设计，没有替换在运行的入口，也没有把未来实现、准入或效果提前标成完成。
