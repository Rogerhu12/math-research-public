# 本次运行的早期准备与已被后续状态替代的观察

2026-11-10，Astra-visible-flex-78718bd0。以下从 open.md 原样移出，保留历史观察的时间和范围；当前活动任务与真正未解项以 HANDOFF.md 和 open.md 开头为准。这里的“正在运行”“下一步”只描述各条写作当时，不是当前任务状态。

R88直接给固定g的快速Fourier Jacobian：六个原Cartesian JVP取局部3×3系数，再由有限DFT卷积装配原N点投影。保留平流/旋转基/aliasing，改变浮点求和顺序。实际df2eda的32点比较M15/M22加速4.44/6.93倍、相对差约2e−15；后续generic可选择，当前主M15原源不改。完整BVP时间仍有LU、RHS回溯和尾成本，不把局部加速当整图结果。

R90已完整证明前缀长精度FFT synthesis/projection及其舍入扰动传递，实际32点RHS与complex-step比较完成。通用入口现可显式选择 --jacobian fourier --transforms fourier --tail-jacobian fourier，默认仍original；当前活动主源不变。局部计时不预判整体BVP/真DN速度或收敛。

R89完整证明尾部有限Fourier乘积Jacobian与同RK变分流等价，可选worker已接入，实际局部/短stage成本下降；新W22仍须实际求解。root正研究保存全射击线性化的物理H切线预测，使后续真延拓从二阶残差起步，不变原方程或成功标准。

R91证明纯j1支撑基线的入口误差仅为保留round背景的阶乘尾（M15<4.71e−25）；实际约1e−9不能归因于这个基线。一般support的固定弧长Hessian给已知背景尾+二阶参数余项，仍需真实新prefix的全角值。
R92已证明同一完整有限射击系统的全节点物理H切线预测，含有限基线残差/数值Jacobian误差/尺度转换。新worker保留原来已算的全流J，只改善warm；当前原主source不动。新通用求解每inner返回会保存明示outer UNSOLVED的实际物理PPoly，供长尾期间直接诊断。

R93已完整证明一般support参考的同物理g换图、两jet运输及入口anchor；真实warm参考rho>.19227、材料角改变量<.006。改变坐标本身不减真实metric误差；只有在新表示中真实重求/加密才可能改善近似。当前M15/W22实际路线保持原warp。
R94/R95/R96完整证明直接登记：几何缩幅须重解非线性mean；几何回缩保同一Newton一阶方向并由原残差接受；旋转态二次moment自然产生双频，不能把π当线性高度坐标。R95完整raw正域凸不蕴含消mean后正域凸，当前实际floor仍.05。

旧M14峰附近预算（非新图）：同一真实g下背景余项在整个小span18157对metric贡献≤6.09e−11；原全角行和9.04341e−9经256角区间/4径向子段至8.66431e−9。证明证书宽差可按自身系数缩小，不是新图必付固定floor；不能把两span当全尾，也不把旧图界转移W22。

fast05最终十回溯耗尽，3.336601164e−9仍大于原2e−9，0真尾/0inner。已保存385541B的同态iter3恢复输入；stage12两端原root已达9.19e−17/1.65e−16，紧root与原root逐位同，故端点宽阈值不能解释此停滞。正在比较唯一该stage的原/tight及withJac/无Jac状态路径；不扩展全尾重算、不放宽容差。

同stage12原/tight根×Jac/plain四种实际S32流逐位相同，沿段maxRootRelative≤1.65e−16。已实际定位R95 v2的零方向roundtrip偏置：Q不变、高π约1e−18，经Jππ块约1.97e6放大后引起1.08147e−9归一残差扰动；同段norm3.33660e−9→3.99009e−9。JπQ约2.42e13不能与π偏置直接混乘。中心式baseπ+(Cλ−C0)在nodes0/12/13的δ=0、λ=1逐位固定原state，下一同grid/同h恢复避免额外初猜重投影，仍原root/P8/S32与原2e−9；细分P16/S16保原raw RK密度作备选。

fast06于本轮实际3afd01启动/session27279：R95 centered-v3、原root、P8/S32，worker对同M/N/P/S/物理节点及逐值同h恢复直接复制原canonical states，不再零幅重投影；仍从同h/8的实际未解iter3求起，随后真延拓回原h，原tol/floor/g不变。R98完整证明同RK子步的射击细分零点/线性消元等价，并给非零缺陷传播；P16/S16是保持raw RK密度的备选，不能把新旧非零norm说相等，当前未启用。

R97完整登记：当前common-cut生产源只在末端支持加入quintic，前段与自身base全部二jet同，可用新图自己的base低模前段/common高模末段分算并取。旧M14例Fourier项工作量约42%仅为计数，不是实测加速，也不把旧曲率界移给新图。另一个固定正交框架曲率界在六完整span N64/128/256均未改善，留作已证明工具而不接生产。

fast06在13:30:26的第10个试探只接受λ1/512，norm从3.336601164e−9微降到3.332597699e−9，仍在运行且未达tol，不写成自然失败。准备P16/S16实际分段恢复以降低已观测单map高频增益。实际linearSteps为256，P8/P16/P32对应每stage32/16/8且每raw256；物理calibrationSteps仍512，R98已订正此前数值例的混称。

fast07已be42ba实际启动/session67954：从fast06真实iter2（norm2.996289066e−9）闭存385457B输入恢复，P16/S16/audit16、centered/原root，旧865点逐位保留并实际积分864个中点。fast06 719dc2主动exit1是路线切换，不是自然失败或不存在证明。只对旧stage12的P16两半实算：Jππ最大从1.970607e6降至2538.806/4950.734，实际中点和合成终点shape均与原S32逐位同；完整J组合max-scaled差1.9165e−12为浮点乘积差。尚不是新全尾结果，不继续无关P32局部测试。

fast07首完整Newton试探实际13:44:17已把同h/8射击norm从2.996289066139843e−9降至1.5667180114594494e−10；root ad516d仍67954运行，尚待原full-J迭代和真实响应返回。此为P16有限残差的进展，不是whole metric或最终原h成功，仍接真实h延拓。

fast07首h/8真实响应已13:46:27返回converged=true/residual1.5667180114594494e−10，13:46:28实际TRACK tau=1/8并调用自身完整shooting tangent。bootstrap Jac/audit=false，闭存包不含完整逐段J；自有J保在worker内存。仍须到原h和新prefix，不据低h/射击norm预支whole metric。root b69e30实际67954仍运行。

第二真延拓响应13:57:32已收敛：h=15/64原h、norm3.342331757780155e−10；随后call3实际tau1/4，即h=11/32原h，已用自身切线。root54e06f读取实际返回，bbf4f3 poll仍67954运行；仍未原h成功/inner，不把中间高度改作最终目标。

