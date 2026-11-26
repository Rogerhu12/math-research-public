# R714 实施附录：完整 normal frame 的同图重接、零控制解析模板与独立数值缓存

状态：本文给出完整解析公式、同调用缓存的适用条件与可执行小核。准确公式已由下述推导证明；完整源只做静态读核、AST 与编译检查，没有本地科学执行，没有观测到的重复率、运行时间改进或新场结果。它不替代 R714/R715 的分支、求积与完整物理六 jet 责任。

本文的直接来源是 R715 完整 centred normal b2597012ec8ee063fabbb49a758b592d10f607de55ded3becaa8b62b6a50118d，以及其校准核 a8e849068b12ffe2876c07ec2518947890c9f09614da2a9882b53e268e3ba873。其 full base 是 6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865。原 66e81 的旋转、积分、normal frame 与完整 32-stage 实质公式均保留在这些来源中。

## 1. 实际需要保留的两个计算层

原 _get_roots 先对完整 data 作 detach，再由 _run_chain 选择并保存每个共同阶段的控制值和角 jet。该调用内部整体处于 torch.no_grad；_normal_frame_jets 只临时启用对局部控制的自动微分，最后返回完整 detached frame。每步 Newton 的 3×3 矩阵、角 jet 的 6×6/9×9 矩阵只对本步新的 eta 局部叶求偏导，previous 与 frame 本来就是这一步的已选系数。

之后 _implicit_jet_value 才在当前完整自由点 x 的活动图上逐步重接所有上游控制、normal frame 和 zero target。它仍解完整的 6m/9m 下三角链；m=32 时没有把任何内部阶段或外层 core/omega/H 自由量删掉。这里 frame 的同值复用必须保留上游导数，不能使用前一层的 detached 数值替代。

因此本实施分成两个严格不共享缓存的 scope：

- 数值 scope 只服务同一次 _run_chain，保存该调用中已实际求出的 detached frame 数值；
- 活动 scope 只服务同一次 _implicit_jet_value，采用 R714 的完整 C1 重接。

两者都严格绑定当前模型、完整自由点、全部有序 literal phi、原 data 的所有 Tensor 对象和版本、角阶数以及全部 3×6 控制 jet 字。scope 结束即清空缓存。没有 checkpoint 导入或跨调用 graph 恢复。

## 2. 当前来源确为线性左指数控制

记固定角下的当前完整未校正 meridian 为 q(s,phi,x)。它已经包含全部外层旋转与冻结 supported reference。内部六控制为 u，真实矩阵为

$$
B(s,\phi)=
\left[
 S\sum_{\alpha=1}^{2}\beta_\alpha(s)
 R_z(\theta_0)Q_{\alpha0}R_z(\theta_0)^T
 \quad \gamma(s)I_3
\right].
\tag{1}
$$

六列记作 B_i。来源 _corrected_jets 逐字实现

$$
T(u)=\exp([Bu]_\times)q.
\tag{2}
$$

这里是 WORLD 左指数。B 的实际值与两角 jet 使用同一固定 chart、十八个 literal Q 字、gamma、同一 S carrier 与完整原积分节点。当前 B 不由外层自由点重选；即使在一般公式里把 B 看成已绑定的 x 函数，下面的活动模板也保留其原 x 图。

原闭合函数与 R715 的 centred 闭合函数之差只涉及对内部控制独立的参考项。它们的控制偏导因而都来自

$$
f(u,x,\phi)=C(x,\phi)+
\frac{1}{S}\mathcal I\{\exp([Bu]_\times)q\},
\tag{3}
$$

其中准确数学时 $\mathcal I$ 是完整径向积分；本工作实现中它是原 _total 的全部原 Gauss 权、np.diff(mesh) 字和 cell cumsum，端点项 C 对独立 u 无依赖。本实施不把两种积分解释互相冒充。

## 3. 零控制的完整一、二控制偏导

对任意向量 w，

$$
\exp([w]_\times)q
=q+w\times q+\frac12w\times(w\times q)+O(|w|^3).
$$

因此在 u=0，

$$
A_i=f_{u_i}
=\frac1S\mathcal I(B_i\times q),
\tag{4}
$$

$$
H_{ij}=f_{u_i u_j}
=\frac1{2S}\mathcal I
\{B_i\times(B_j\times q)+B_j\times(B_i\times q)\}.
\tag{5}
$$

H 的每个分量都是端点三向量。所有六个控制、两个原 bubble 以及新增 gamma 均在 (4)(5) 中，没有删除原第一组或新增第二组。

这也与当前实际 Rodrigues 小范数分支一致：6a803 的 A(0)=1、B(0)=1/2，安全未选分支在零点没有 NaN；由其完整 Taylor 程序在原点得到的第一、二控制偏导正是 (4)(5)。本实施没有把一个只验证过函数值的数值黑盒当成高阶导数证据。

## 4. 两角 jet 的全部 Leibniz 项

写 $B_i^{(a)}=\partial_\phi^aB_i$、$q^{(c)}=\partial_\phi^cq$。在控制路径连同其角 jet 全为零时，对于 j=0,1,2，

$$
A_i^{(j)}
=\frac1S\mathcal I
\sum_{a+c=j}\frac{j!}{a!c!}\,
 B_i^{(a)}\times q^{(c)}.
\tag{6}
$$

对应 Hessian 角 jet 为

$$
H_{ik}^{(j)}
=\frac1{2S}\mathcal I
\sum_{a+b+c=j}\frac{j!}{a!b!c!}
\left[
B_i^{(a)}\times(B_k^{(b)}\times q^{(c)})
+B_k^{(a)}\times(B_i^{(b)}\times q^{(c)})
\right].
\tag{7}
$$

式 (7) 第二项的 a 阶导作用于第 k 列、b 阶导作用于第 i 列，不能错误地重复第一项的列顺序。完整实现按三重指标逐项列出；j=2 的所有六个有序分拆及其 1、2 系数都保留。

实际 _zero_frame 对每个 j 求完整六列的 (6)；_zero_partial 对每个 j 和固定第 i 列求 (7) 的全部六个 k。每次只把六个独立控制列与角列作可逆 reshape，调用原 _total。没有把径向格点、角点或控制列抽样，没有改变 S、原正权或 cell 的物理 width 字。

这种分列方式把一次临时三向量数组限于完整径向节点×全部本 batch 角×六列，而不要求同时常驻三十六列的所有中间 cross 数组。它仍计算所有 6×6 Hessian 分量；不是低秩替代或删除交叉项。

## 5. 零三 jet 处的完整 frame 控制-Jacobian

令 $U=(u,u_\phi,u_{\phi\phi})\in\mathbb R^{18}$，frame 输出是
$\mathcal F(U)=(A_0,A_1,A_2)$，每个 A_j 为 3×6 矩阵。一般控制路径满足

$$
\begin{aligned}
A_0&=f_u,\\
A_1&=f_{u\phi}+f_{uu}u_\phi,\\
A_2&=f_{u\phi\phi}+2f_{uu\phi}u_\phi
       +f_{uuu}[u_\phi,u_\phi]+f_{uu}u_{\phi\phi}.
\end{aligned}
\tag{8}
$$

在全部十八个控制 jet 真为零处，(8) 的完整一阶变化为

$$
D_U\mathcal F=
\begin{pmatrix}
H^{(0)}&0&0\\
H^{(1)}&H^{(0)}&0\\
H^{(2)}&2H^{(1)}&H^{(0)}
\end{pmatrix}.
\tag{9}
$$

每块把六维控制变化送到完整 3×6 frame 变化；(9) 是 54×18 矩阵，不是只有一个 3×3 根矩阵。式 (8) 中三阶控制导数乘两份 $u_\phi$ 的项在零三 jet 处的一阶变化为零，这才是 (9) 无该项的原因，并非任意非零控制下都可省掉高阶导数。

一角接口输出前两行，实施采用完整 36×18 数组，最后六列准确为零；仍以实际十八字作 key。不把当前未请求的二角控制 jet 擅自设零，也不把另一角阶缓存冒充当前 scope。全部数组形状分别为：

| 量 | 实际 shape |
|---|---|
| previous / Ustar | A×3×6 |
| frame | A×(order+1)×3×6 |
| complete partial K | A×(order+1)×3×6×3×6 |
| H angular jets | A×(order+1)×3×6×6 |

A 是本次全部 literal 角数。完整 partial 每个二角节点有 54×18 个 binary64 字；报告只将其实际分配字节记为 detached-partial 存储，不冒称这是整个 AD 图的内存。

## 6. 保留全部外参数导数的活动重接

同一活动图中，设独立局部叶 Ustar 的字与某阶段的 Ustage 字逐个完全一致。以当前原 data 的活动图计算

$$
F_\star(x)=\mathcal F(x,U_\star),\qquad
K_\star=D_U\mathcal F(x_0,U_\star).
$$

本实施使用

$$
\widetilde{\mathcal F}_{\rm stage}(x)
=F_\star(x)+\operatorname{stopgrad}(K_\star)
\,[U_{\rm stage}(x)-U_\star].
\tag{10}
$$

在当前 x0，括号的值严格为零；由普通乘法链式法则，

$$
D_x\widetilde{\mathcal F}_{\rm stage}
=\mathcal F_x(x_0,U_\star)
 +\mathcal F_U(x_0,U_\star)D_xU_{\rm stage}.
\tag{11}
$$

这就是原完整复合函数的一阶导数。忽略 K_x 只因它乘零值，不意味着可把 Fstar 的原 x 图 detach，也不意味着后续阶段的 U_x 为零。

零模板用 (6) 构造 Fstar，保 q、B 和当前数据的全部外参数图；只把 (9) 的系数作为 stopgrad K。第一阶段的 previous 本来是真正不需梯度的零 Tensor，因此可以先返回完整 Fstar，暂不构造 H。直到后来出现同字且具有活动上游的 previous，才由 (7)(9) 补全 K。后续阶段、其 zero target、所有矩阵和 implicit solve 都仍然执行。

一般非零模板则在独立局部控制叶上调用原完整 _normal_frame_jets，再逐 frame 分量求其对完整 U 的偏导。严格来源中的 cross、逐角矩阵作用和 _total 都没有角混合，故对输出各角求和后作 autograd.grad 返回的是全部各角自身偏导，不是把一个混合角系统的 Jacobian 对角近似化。

一般模板只在当前完整计划里同 batch 十八字至少重复 8 次时启用，以避免无重复时必然增加高阶偏导工作。8 是公开计算策略，不是数学可行阈值或已证性能交叉点。零解析模板没有这个至少 8 次要求，但仍只有完整十八字真全零才进入。

每次调用者仍按原式使用

$$
F_{\rm used}=\widehat F_{\rm stage}
 +\bigl(\widetilde{\mathcal F}_{\rm stage}
       -\operatorname{detach}(\widetilde{\mathcal F}_{\rm stage})\bigr).
\tag{12}
$$

因此 selected stage 的工作 frame_hat 仍是原 primal 锚。随后该阶段的 eta、control 锚、6×6/9×9 矩阵与解、下一阶段所有数据依赖均保持。

逐阶段用 (11) 作归纳，最终外层物理六 jet 与其一次 J/J* 的全部上游链都保留。不能把它扩展为对外参数再求一次 Hessian 的合同。当前 functional.jvp 的 reverse-over-reverse 算法第二次对辅助 covector 求导，是重建一次 Jv；这没有要求真实 K_x。当前 R664 的 J* H_res J 也只使用一次物理 J，不是外参数 Hessian。

## 7. no-grad 初场链可以缓存什么

_run_chain 使用已完整 detach 的 data。每个阶段先根据已选 previous 求 frame，再固定该 frame，求新的三维 eta 与对应角 jet。实际 _stage_jacobian 和 _stage_jet_jacobian 的局部叶仅为 eta；它们没有在这一步重新把 previous 当独立自由点求导。

因此在同一次完整 _run_chain 中，如果全部 previous 三 jet 字、全部角、data 对象/版本、order 与完整当前点相同，重复求同一个 frame 数值并非求根方程的必要新操作。独立 CompleteDetachedFrameScope：

1. 第一次仍调用原 _normal_frame_jets，不采用解析零模板重排它；
2. 只有完整 finite detached 结果才保存 clone；
3. 后续十八字完全相同时返回该实际完整值的 clone；
4. 每个阶段仍执行原 Newton、实际残差、原 3×3 与 6×6/9×9 矩阵、角 jet、域检查和阶段/终态真复读；
5. 同调用结束清空，绝不把这些 detached 值拿去代替活动 C1 图。

这可以复用非零的同字 frame，也不需要预先断言 centred 初点的根为零。零 residual、zero-control tag、接近阈值或同角样本的计数相同都不是 key。

升阶仍是原算法：order=2 重新建立本次独立 scope，原已选低阶 frame/eta/control 字继续由原 old_stage 覆盖与核验。没有把 order=1 缓存静默当成 order=2。

数值缓存保存的是第一次真正求得的字，不声称一次尚未发生的未来重新运算必然逐位相同。完整新数值实现须有新 source/model 身份和真实重读；其 frame 值保真缓存不替代对原浮点/求积误差的连续认证。

## 8. 可执行 API 与调用方必须保持的接点

完整小核文件为 normal_frame_c1_reuse.py，导出：

    definition(minimum_generic_repetitions=8, zero_template=True)
    NormalFrameC1Kernel(q, minimum_generic_repetitions=8, zero_template=True)
    kernel.value_scope(data, literal_angle_hex_keys, order)
    kernel.scope(x, data, phi, order, complete_selected_root_items)
    scope.frame(previous, zero_based_stage_index)
    scope.close()
    kernel.metadata()

新 operator 先将完整 definition 写入自身 model 的 normal_frame_C1_reuse；完整 model identity 完成后构造 kernel。调用方的 FRAME_C1_SOURCE_SHA256 必须是此小核的实际整文件 SHA。kernel 同时独立核 runtime operator 的完整文件 hash/model、原 base/hash、全部阶段维数及九个完整数学方法的 canonical AST。AST 编码保全部语义字段，仅剔除 Python 版本间空的 type_params 字段，不忽略任何非空类型参数或方法内容。

数值接点只替换 _run_chain 中的 frame 求值这一行，并在原 torch.no_grad 同一调用内用 value_scope 管理；活动接点在 _get_roots 全部完成后创建 scope，只替换 _implicit_jet_value 内的 frame_computed 求值一行。所有原 stage 控制流与真读循环均逐体保持。两个接点都必须用 finally 或 context manager 关闭，因此失败也记录实际已请求阶段数并释放缓存。

完整 scope key 比较全部原始 binary64 字节，包括 signed zero，不 round、不容差比较。shape、version、图身份、完整方法身份错误会显式失败。仅可选模板构造自身的 RuntimeError、MemoryError 或非有限结果回到原完整 frame 求值，并记录实际原因；不因此删变量、清 residual 或放宽 root 域。

图只存在于当前 scope 的局部 cache。kernel 保存累计数字与最后一次 scope 记录，不保 tensor、cache 或 activity graph。报告 actual_counts 分别列模板构造、通用额外 reverse products、解析 full integrations/cross pairs、C1 重接、no-grad 命中/原始读取与实际临时数组字节。scope_seconds 包含所属 stage chain 的实际耗时，不包括返回后才发生的外层 backward，不能把它当成完整 J/J* 总成本。

## 9. 工作舍入与尚未支付的责任

准确公式 (4)–(11) 不隐去工作算法差异。解析模板重排了 cross、加法、控制列 packing 与求和调用；其工作偏导不宣称逐字等于原多次 AD 的工作偏导。旧 _total 的完整节点、权、width 字与 cumsum 保留，但仅此不足以声称不同打包形状下的所有浮点运算逐字相同。

调用方通过原 frame_hat 锚保持已选 primal；一次 J/J* 使用明确新模板与完整链。这是新的已声明数值实现，不是偷偷把同一份旧 source 的输出换掉。完整新来源必须重新核验模型、同 target、全部自由量、原 norm/mu、全 192-prefix/幅度行和真实历史，不能复用旧 active 图或旧 derivative cache。

本实施没有 outward 包围模板、旧 AD、求积或 solve 的误差，没有证实全部角 normal 分支的存在/连续性，也没有保证 cache 命中或总时间变短。R713 准确均值、R714 一阶合同、R715 完整六 jet lift 与原几何/幅度真实筛的责任仍各自保留。

## 10. 静态验证与下一完整入口

本地只执行 stdlib AST、compile、py_compile、重复 literal key/keyword 与尾空白检查；九个完整 source method 的 AST 与实际 b259 文件逐项核过。没有 import NumPy/Torch 执行科学模块，没有数值 fixture、根求解、F/J 或性能测试。

最终小核为 34,905 B，SHA256 ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9。独立数学核读覆盖零模板完整Leibniz/三角块/C1图；独立来源与scope核读覆盖全部字、同图、no-grad完整原读取和释放。可选 clone 分配失败只记录并使用已算出的或重新原式读取的完整frame；shape/source/graph违规不吞。

新完整 cached 入口必须独立派生校准 helper 的新 ENDPOINT_SCHEMA，再锁新 operator/geometry/driver/launcher/reader 的整文件身份。原 a8e/b259 与原 plain centred 链保持不动。它可以从合法实际输入直接形成独立完整方向，不要求先执行一个从未准入的 plain centred 场作为前门；继承的永久地址只来自真正存在的完整历史报告。

参考：R714 完整同图 C1 重接证明；R715 完整 reference-centred 六 jet 与误差账；R711/R713 完整 supported smooth-triangle reference 与实际费用接口。
