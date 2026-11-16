# R441：固定准确目标下的角求积、尾步数与完整 450 重求

作者：geometry agent（AI）。日期：2026-11-16。状态：独立来源代码与条件证明；没有执行本项科学程序，没有实际父 450、加密结果、误差常数或收敛证书。

## 441.1 本项支付什么

本项补的是一个真实的有限程序入口。给定当前任务中已经通过原全部门的连续 C 十控制全冻结 450 场，显式增加场与 native 的角求积数、原 native 的 `steps` 参数以及物理边界的材料角和物理角求积数，重新生成实际尾数据，并完整重求新的 450 问题。旧检查点中的状态只成为初猜。

场维数仍为 $M=112$，物理状态仍为 $3M+2=338$，全冻结状态仍为 $4M+2=450$。原 native 保留 $576$ 个 stage、全部 $112$ 个入口方向、完整 $338\times112$ 端点响应及两个 mean 通道。`steps` 是原程序的参数；实际采样、RK 回放与审计必须跟随原程序在该参数下真正形成的 schedule，不能仅按“$576\times\text{steps}$”猜测所有内部调用数。

本项保留原求解方法和门：native 的 $32$ 次外迭代、$10$ 档试步、严格下降和 $2\cdot10^{-9}$ 容差；全 $\eta=0$ 敏感度；物理问题的 $8$ 次外迭代、$17$ 档试步、RMS $10^{-6}$、边界 $10^{-11}$、原完整 FD 阈值 $5\cdot10^{-5}$，以及真正最终 current-H、全 J、full-DN 和 fresh audit。

这不是加密误差定理。更多求积点或更多 RK 步，并不单独推出任一误差单调减小、同一有限根存在、算法成功、连续 C 的某一全局根选择已经实现，或数值场收敛。本项不改变原 field、target、curve、metric、reach、held 与 $\delta E$ 的独立证明责任。

## 441.2 三种对象必须分开

第一种对象是准确目标。保持同一完整 f12f 模型 C 输入、原 $160\times9$ 有限头与深根族、物理 cut、准确十控制 DAG、所有十个冻结参数以及原 core 的几何定义。准确目标不是用新数值场反定义的 $F_0^*e$，也不是把原尾目标换成 $1+B'^2$。

第二种对象是数值标量编译器。其 factory、definition、所有实际输入、十词和编译来源保持与父检查点相同。这里的“保持”由整个 `current_target_identity` 和十个 binary64 原词核对，不能仅比较一个 schema。它不把有限编译器的 `ap/app` 标签改称已证的准确导数，也不免除 R294、R298、R400、R409、R416 已分别说明的准确对象、Hermite 定义与 atlas 责任。

第三种对象是有限求解程序及其结果。角求积与 `steps` 是这个程序的分辨率参数。重求后，core112、全状态、mesh、current-H、Phi、原全局 SE2 配准、R249 入口归一化及实际离散几何都可以变化；本项不会用“同一目标”把这些新值宣称为旧值。

必须保留以下区别：同一个准确 C 根族不意味着不同点的区间中点来自同一个全局 C 成员；同一个标量 DAG 不意味着有限编译器是其准确求值；有限 native 余量小不意味着它已给出无限尾 DN；真实 450 接受不意味着全闭面已经通过几何门。

## 441.3 实际分辨率合同

每个真实父和新检查点都记录

$$
\mathcal R=(112,N,N,s,A_m,A_p,576),
$$

分别对应 `field_modes`、`field_angular_quadrature`、`native_quadrature`、`native_steps_per_stage`、`material_angles`、`physical_angles`、`native_stage_count`。其中 $N$ 为偶整数且 $N>896$，$A_m,A_p$ 为偶整数且均大于 $448$，$s$ 为正整数。这些是原接口对完整所需模态的已存在可解析范围，不是新收敛阈值。

新 recipe 声明四个正整数因子

$$
f_N,f_s,f_m,f_p\ge1,
\qquad
\max(f_N,f_s,f_m,f_p)>1,
$$

并要求

$$
\mathcal R'=(112,f_NN,f_NN,f_ss,f_mA_m,f_pA_p,576).
$$

同一新 $N$ 实际进入场的 FullCoreProbe 和原 native 配置；材料角、物理角分别进入原 PhysicalTestBoundary。每个字段还和实际 full-DN 输出、live native owner 的 `parameter_record`、实际 boundary 描述核对。它们不能只存在于 recipe 的声明中。

如果整数超出原 JavaScript 安全整数接口，入口以资源范围不足结束，保留原父和全部未启动责任。它不截断数值，不把因子暗改回 $1$，也不把容量不足称为数学反例。

即使新均匀角网格的点数是旧网格的整数倍，也不宣称所有角节点的浮点原词逐字嵌套。原运算顺序形成的新角度词、FFT、root 调用和离散积分都必须实际重新执行。

## 441.4 实际父来源与原始时钟

完整初始来源只接受两套明确的已发表组合：原 193 的 driver/launcher 与 joint203 的 driver/launcher。两者必须在当前 run 中真实完成 design453，再将其实际末十词冻结后完整求解 frozen450；不能从 453 删除三行制造 450。

允许的直接父为该真实原 frozen450、原 193 下已经真实接受的 R431 mesh450，或本独立 R441 入口此前真实接受的 resolution450。每种分支都有各自完整 source/schema/检查点 writer 身份，不能只依靠尺寸碰巧等于 450。

新入口读取实际原 launcher 已经消费的 deadline 文件，并要求 bytes/SHA 与其回执相同，schema 分别为原 193 或 joint203 的 deadline schema。实际 namespace 起时、science $18900$ 秒和 readback reserve $2700$ 秒保持。后继不创建新的 namespace 起时，也不重新给予整块 science 时间。

原时钟在两个 owned child 启动之前都计算实际余量，并在运行时按原绝对截止时间轮询停止。读取与绑定也发生在该原始墙钟之内，但 Python 的元数据读取本身不是另一个可抢占的硬杀钟。因此不承诺整个后继必能用完预算，或始终留下完整 $2700$ 秒。未来实际 workflow 的 job/step 硬限仍须真实设置；本项没有虚构一个已派发的 workflow。

SIGTERM/SIGINT 只传播到实际建立的新 session 及经 PID/starttime 观察的自有子进程，不要求共享 runner 进程组为空。sampling 与 refinement 两个 child 都必须被回收和确认静止，之后才读其可变结果。中断、资源截止、绑定错误和原数学拒绝分别保留。

## 441.5 同一 C 的真实新尾采样

新 native 几何不能通过修改旧 `steps_per_stage` 字段得到。入口保留父实际使用的 sampler 家族：positive 或 joint-nominal。新采样仍使用该家族原源码；如果父使用 joint，后继不能暗换回 positive，反之亦然。

新调用逐字绑定父实际完整 C result、完整深端 112 行 result、原 R380 与 R357 proof、同一实际 cut 和根族。它从原源真实重算新 `steps` 下全部 stage 字段、节点、mean、所有远端候选及 112 条 Robin 行。新 geometry 的实际 cut 与 finite far radius 的 binary64 原词必须等于父 geometry；本项不暗改有限远端。

采样精度、积分/传播工作深度、缺陷目标、存储及时间资源必须由新输入完整显式声明。父 result 没有保存所有历史 argv，故入口不会捏造“与父所有工作参数逐字相同”的证据。保持准确数学对象和原 sampler 算法，不等于假称所有工作资源或精度已经从旧 result 恢复。任何改变都可从本次实际完整 argv 看见。

原采样器保留完整不确定 C 族的区间包围。joint-nominal 数值行只是有限程序使用的共同参数盒代表，其完整 family-to-word 差界仍在原回执中；它不是已选准确全局 C 解。新分辨率入口不会弱化这一区别。

只有原 sampler 自己实际返回完整 geometry 后，才从真实父配置复制新配置。允许改变的内容限于新角求积、新 `steps`、新实际 geometry 路径/回执及透明的来源记录。原完整 native 数学方法、32/10、容差、敏感度、factor 资源、全部 source pins 和旧 runtime 仍逐项保留。

采样未完成时，新 450 child 不启动。该含义是实际所需输入尚未产生，不是增加一个独立数学验收条件。必要读回保留所有原尝试 mode、当前未完状态、完整未启动后缀和错误；不把 sampler 部分结果填成 native trial 拒绝。

## 441.6 全 450 初猜与真正重求

父 mesh 的每个原词都进入新初猜，再并入同一有限标量 profile 的全部 literal knots。R441 这条角/步数入口不自动加径向中点；R427/R431 的径向 mesh 实验仍是另一个明确入口。重复值合并时保留父节点的原 signed-zero 词。

设父初值数据为 $X_j,Y_j,DY_j$。新节点上采用原 Hermite 插值器给初猜；父 $DY$ 只决定这个初猜，不被当作新问题的 RHS。对所有新节点、全部 450 行重新调用新分辨率的原 RHS，然后执行原 complete preflight。父节点上的完整 338+112 状态词在 seed/preflight 阶段保持；真正 full-DN 求解随后允许更新状态和 mesh。

完整 seed 并集超过显式 `max_nodes` 时是资源 partial。入口不丢 literal knot、不删父节点、不更改 profile，也不声称一个无新径向节点的初猜说明已经收敛。

新问题的 current-H 从新实际末状态经原 MaterialTrace 计算；它不是父 H、旧零响应或旧 affine。新 native owner 给出完整 112 方向和 338×112 响应；原完整 FD、原 450 full-DN、原全部试步、真实 final-H/J 及 fresh audit 依次执行。只有原 solver 接受后，独立 writer 才能复制原结果并写新检查点。

因此，若该入口报告一个 accepted resolution450，它报告的是实际新有限程序自己的原验收结果。这个结论不依赖父状态被误称为新解，也不依赖删除方程、缩小端点矩阵或借旧敏感度。

## 441.7 准确 target 为什么仍然相同

固定上述准确 C 输入/根族、原准确十控制 DAG 和十个冻结有理词后，公共物理角目标是同一个对象。对于 prefix，公共径向参数取

$$
u=s_{\rm numeric}/L_{\rm numeric}.
$$

若准确长度为 $L_*$，其准确目标在数值 $s$ 图中的径向系数仍为 $(L_*/L_{\rm numeric})^2$；角系数仍由同一准确 $a(L_*u;p)$ 给出。改变 $N$ 或离散 RK 步数不改变这些定义。

但是，真实新 core112 一般改变材料角映射。令

$$
\Theta_j(q)=\Phi_j(2\pi q).
$$

对已满足原 R237 严格正密度条件的两个实际场，R443 给出从第一材料图到当前材料图的正确映射

$$
\psi_j=\Theta_j^{-1}\circ\Theta_0.
$$

它独立于径向变量与相位 $t$。tail/collar 使用相同物理 $r$，帽保留 Cartesian 恒等图，并在抽象粘接处作相应角重标。不能把非线性角重标直接延伸穿过帽中心。

对任意切向量，两张图的 Gram 与目标矩阵通过同一个可逆 Jacobian 作合同变换。因此原四个 Loewner 不等式在同一 $\eta$ 下保持，正是 R443 已给的结论；这里不另证明或新设它的数值门。新 R441 metric 消费者在当前图中计算真实 Gram 与当前图目标，只有其实际严格 bound 返回后，才可沿该已证明的共轭解释为共同目标的 bound。

本项没有实际求值 $\psi_j$ 的区间算法，也没有从两个离散场推出统一强 $C^2$ 收敛。旧和新的 Phi、SE2、R249 与几何定义回执都保留，不能因理论上存在图变换而将不同浮点词宣称相同。

## 441.8 固定全闭构造与真实新几何

输入指定一个已经真实定义的同目标 shared field。入口读取其完整 result 与实际 plan，核同一准确 target 和全十词，并冻结 $W$、帽高度 $H$、完整 `fixed_cap`、所有 marker 的顺序/side/center/radius/height以及原 cuff。浮点量按 IEEE64 原词保持，包括负零；JSON 整数按其准确整数保持，不先舍入到浮点再比较，因此不能把大整数碰巧舍入到同一词冒成同一构造。

这里不调用旧 e70d 背景构造器，不从新 radial 再选择 $H$，也不默认 marker 为空。R437 的首次构造/材料收据可作为该首个实际 shared field 的来源；本入口消费真正已存在的输出，不预填 R437 的未来数值。

R413 已说明帽的常数高度 $H$ 不进入帽 target 的 Gram。因此冻结 $H$ 是本次几何构造与可比性的责任，不应误说它本身产生一个不同 metric。真实需要处理的材料系数变化来自 core→Phi；其方向由 R443 而非高度固定自动支付。

后继重新执行全部 radial replay、原 cuff atlas、shared-B、准确 cut patch 与两帽来源。新 $N$ 下完整 DC、均值、Nyquist 及全部 Fourier 系数均保留；不以原 2048 标记冒充新数据。R249 投影和节点 012/二阶定义仍是新的准确 Hermite 几何定义；实际 RK 轨迹误差尚需独立证明，原 prefix metric 不转移。

准确 cut 的实系数表达仍由同一 C/DAG 和完整 cut 条件产生，不用盒中点代替准确系数，不把非 dyadic 系数塞进旧 Fraction 节点冒准确。tail target 仍是原 $E_C(r)$。帽由全部原 marker 的 Cartesian 图给出，target 恒等比较仍要绑定同一 side/cuff/完整 marker；没有新增数值扫帽前门。

## 441.9 全域消费者和未付范围

新入口保留原 R426 的完整同 C 实时查询责任：实际四份 C 文件、原 source/index 流及根族身份不得由 cut 三盒或旧 fingerprint 替代。空间细分不会自动收紧旧固定 E 盒；只有原 live-query provider 真正调用并绑定同一对象的新包围时才得到新的信息。

reach 保留原 R422 全 pair universe、两反射片、所有 patch/collar/seam、两帽及全相位；R435 只组织其完整块覆盖，不删 rank。块未获证就完整分裂，singleton 回原门。中止时保全部 frontier、当前 pair/phase 栈、原 unpaid ledger 身份及地址范围。metric 不通过、partial 或出错，都不作为 reach 的新的前置门。

held 和 reflection-inclusive $\delta E$ 使用新实际同场的全像覆盖、完整闭 $F_0$ 的 $D$ 责任、实际 witness plan 与原所有 marker。它们不能只用材料点位移、core 直径或旧 tail 见证。该角色只依赖真实 radial/cuff/shared 三前置及同一截止时间，不依赖 metric/reach 是否通过。

R443 的像集不变量说明合法公共图共轭不改变这些几何量；它不会让一个旧场的数值证书自动成为新场的证书。新源全都重新消费新实际场和新的原始输出。

## 441.10 读回、资源与最终边界

每个科学来源保原完整临时输出。独立 metadata reader 在 owner 实际静止后读取新 sampler 的全部 mode/unpaid 流、原完整 FD 层、物理原门、每个 native call 的必要标量、所有失败 scope、最后 call 的实际细项和新检查点成员身份。

大型成功矩阵、全部 earlier trial 细表、成功候选管和原 stdout 只保完整身份和声明范围，不经分块/编码运输。每份必要输出仍为一个不超过 $90000$ bytes 的 JSON；如果本次失败地址或必要输出过多，保原临时输出并诚实返回 70，不提高限额，也不把读回失败改成数学失败。

读回角色不删除 raw。外层未来调用者仍须等待原父、新采样、新 450、所有实际几何角色的必要读回和进程静止后，才能作其获授权的临时清理。本项没有创建该未来请求或 workflow，也不替它预付规则同步、job 硬限和完整收尾。

尚未支付：任何实际 resolution450；有限程序到准确解的误差；$M$ 的维数派生；native 576-stage 深度变更；物理 finite far 变更或无限 DN；uniform $C^2$ 精化收敛；任何实际 $\eta$、reach、held、$\delta E$ 或 README 总完成条件。旧 `exact_20261114_common_grid_refinement.py` 只重采样同一已接受 H 的 readout，不能替代本项新的完整求解。

## 441.11 真实源码依据

- R400 的实际 profile、43f writer、1c7 SavedPrefix 与 011ca 准确 target 接口；本项只独立扩展真实分辨率来源。
- R409 的 5cc radial、6a5 shared 与其完整原采样/FFT/mean/Hermite 责任。
- R413、R416、R417 的原 cuff、准确实 cut patch 和固定帽来源接口。
- R426、R422、R435、R425 的完整 metric、pair cover、块组织及全像 held/rigidity 消费者。
- R427/R431 的真实父450→新 full-DN、源级 writer 和 owned lifecycle；本项不把旧 mesh 子程序重标成已支持 joint203。
- 已发表 R444 的真实 joint203 driver5400/launchercb057，与原193完整来源并列注册。
- [R443](R443-common-material-angle-pullback-and-fixed-closed-target.md) 给公共材料角共轭与同一闭 target 的条件证明。本项不复制其定理，也不以一个未执行的共轭 evaluator 冒新数值证书。

所有新增源码和完整逐字 diff 随本项接口登记。这里只进行了源码文本阅读、编辑、身份散列和纸面论证；没有本地导入、AST、编译、数值计算或测试。
