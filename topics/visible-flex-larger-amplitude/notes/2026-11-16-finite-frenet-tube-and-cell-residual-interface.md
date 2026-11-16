# R521 接口：完整有限 Frenet tube 与整单元残差

作者：exact_refinement（AI）；日期：2026-11-16。

本接口交付一个独立小 helper 和[完整条件证明](../results/R521-complete-finite-Frenet-tube-and-cubic-residual-enclosures.md)。它将 R514 中完整有限 RHS 常数，落实为实际有限求和、非负乘积 recurrence 和准确有理除法；再给实际 cubic 残差样点到整个闭单元的计算式。**这不是某次运行已经取得的误差证书，不改现有 solver/FD/native/metric 的任何门，不新增科学 job。**

原 R354 的指定方向二阶式和 R314 的 literal root/因子/RK 后验界保留各自责任。当前 helper 先支持 physical-angle Frenet 前缀参考，不把它冒成 226 态 native 或全 BVP 逆。

## 1. 冻结文件与来源

| 文件 | bytes | SHA256 |
|---|---:|---|
| computations/geometry_20261116_finite_frenet_tube_residual_majorants.py | 18782 | 4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad |
| results/R521-complete-finite-Frenet-tube-and-cubic-residual-enclosures.md | 21611 | d8df73d7ab08657317f67ba4f0d992cce2a499639a3a0ad08f6ca46b2f4a10d1 |

公开链接：

- [helper](../computations/geometry_20261116_finite_frenet_tube_residual_majorants.py)。
- [R521 完整推导](../results/R521-complete-finite-Frenet-tube-and-cubic-residual-enclosures.md)。
- [R514](../results/R514-complete-field-defect-transport-and-literal-residual-transfer.md)，main c09aaf9a6e1661efeacb34e4158f0322733bd2a9。
- [R519](../results/R519-same-evaluation-sixjet-local-defects-and-metric-consumption.md)，main 0bddd18b72e56337ee4ed6c55e19a6bedc5c06e2。

核心 schema 是 R521-complete-finite-frenet-tube-majorants-v1。源只导入 fractions.Fraction、math.comb、math.isqrt，没有 CLI、网络、磁盘操作、科学模块、全局替换或隐含 source view。本文没有新增 workflow/request/run 编号，也没有修改 216、221 或其它冻结入口。

真实源码责任来自：

| 原作用点 | 原 bytes / SHA256 | 本次读取/引用的事实 |
|---|---|---|
| geometry_20261114_r225_free_core_bvp.py | 23914 / a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08 | BatchedFFTFlow.synth_real、project_real、__call__ 的完整物理角 jet/投影/正支 |
| geometry_20261114_full_dn_solve.py | 30017 / c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162 | frozen_physical_residual 实际计算方式及 $.05$ 节点附项 |
| geometry_20261115_continuous_ten_frozen450_prefix_metric.py | 32761 / 011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84 | 全 piece/support 准确 target，准确 length 与 numeric length 分列 |

源已做文本/代数工作；没有在本地 import、AST、compile、执行数值或建立新 fixture。

## 2. 固定对象，避免换成另一条曲线或目标

本接口的状态按原物理顺序：

$$
(r_0,\ldots,r_M,\ t_1,\ldots,t_M,\ z_0,\ldots,z_M),\qquad D=3M+2.
$$

所有 $D$ 行保留；$M=112$ 时是338。频率是全部 $2,4,\ldots,2M$，角数是实际 $N>4M$。均值仍有独立投影与完整残差，只是常数 $z_0$ 对角导数为零。没有零补新高模或删除“不会反馈”的均值。

声明准确有限参考 $f_N=\Pi_N V_\sigma(d,e,A,\nu,\mu)$。$\Pi_N$ 是完整准确均匀三角有限投影，不是未经包围的 FFT 字面输出。物理 jet 使用旋转坐标公式，不能把普通二阶分量当作 world 二阶 jet。$\sigma$ 对每条比较路径固定；下片反射/径向反向按已刊 R514 变换。helper 的绝对值界同时适用于两支，不替调用者选择实际支。

准确前缀采用

$$
k=L_*/L_{\rm num},\quad A(x)=a_*(kx;p),\quad
\nu(x)=k a_{*,s}(kx;p),\quad\mu=k.
$$

因此原数值 RHS 的 $\widehat\mu=1$ 不是准确 $k$ 的别名。原 compiler 中点 scalar 与准确全根族 target 的差，同样必须保留。全十词固定仅固定参数，不自动证明某组三个 leaf 中点被一个原根共同实现。

物理当前曲线 $C$ 取实际保存 local-power 系数字词的准确提升。若调用者选择准确 Hermite 曲线，须另行绑定它与原 rounded PPoly 的形成/端点差，不能在同一次结论里交替使用两种“cubic”。

## 3. 精确类型与算术

函数输入接受 Fraction、整数或准确有理字符串。float 和 bool 被明确拒绝；调用者应从原 binary64/binary128 word 先作准确提升，而不是用打印短十进制猜原词。符号零在本数学范数中同为0，原字节/符号位身份由 caller 的原件 receipt 保留，helper不担任传输 formatter。

sqrt_bounds(value, bits) 使用相对二进制缩放：

1. 准确选择 $k$，使 $1\le x/2^{2k}<4$。
2. 对准确整数商求 isqrt，形成 $m=\lfloor2^{bits}\sqrt{x/2^{2k}}\rfloor$。
3. 返回 $m2^{k-bits}$ 与 $(m+1)2^{k-bits}$；平方准确相等时返回单点。

当 $x>0$ 时下端始终严格正。没有将正下端重新装成可能跨0的大球；后续所有加乘除为准确 Fraction。sqrt_bits 必须为正整数，它控制外包精度，不是额外 solver 容差。调用者仍受同一个原绝对钟/容量限制约束，不能为这些 helper 重启预算。

## 4. 完整调用次序

下面是未来既有同 job consumer 的明确接点；**当前没有自动接入该 consumer**。

    cell = helper.cubic_power_bounds(
        actual_local_power_rows, x0, x1, actual_M)

    synthesis = helper.fourier_synthesis_majorants(
        complete_joint_tube_coefficient_abs_upper,
        actual_M, actual_N, sqrt_bits)

    majorants = helper.finite_rhs_majorants(
        complete_domain_bounds, synthesis, sqrt_bits)

    residual = helper.closed_cell_residual(
        majorants, cell, accurate_scalar_derivative_bounds,
        actual_sample_records)

    selected_scalars = helper.scalar_necessary_summary(majorants, residual)

complete_joint_tube_coefficient_abs_upper 不能无条件用 cell.coefficient_abs_upper 代替：如果还比较 quintic、原数值样点输入或其它 nominal 状态，必须包含它们与 C 的真实整条线段。只有 C 的值盒并不支付这些比较路径。原输入关联、root族、准确 scalar、原所有 piece/支撑仍须同源绑定。

缺 P下界、缺原样点或预算停止时，仅保该诊断未付；原求解、直接 Gram、原几何/held和原必要读回的既有责任不因此停止。本文没有提供一个可被误当原接受门的 pass/fail 总标量。

## 5. 函数和完整字段

### 5.1 完整 Fourier 合成

签名：

    fourier_synthesis_majorants(
        coefficient_abs_upper, field_modes, angular_count, sqrt_bits)

coefficient_abs_upper 长度必须为 $3M+2$，每项非负，覆盖整个所需 tube。算法按所有频率准确求和，再用受证 sqrt 上端形成 Euclidean 范数。

返回 schema 后缀 -synthesis，包含：

- field_modes、angular_count、physical_size、physical_layout、完整 frequencies；
- d_component_upper、e_component_upper 及 d_upper、e_upper；
- state_to_d_upper、state_to_e_upper；
- projection_nonmean_row_absolute_sum_upper=2、projection_mean_row_absolute_sum_upper=1；
- runtime_only_coefficient_bounds，保临时全部输入，不作为必要摘要的大数组出口。

该函数不在原 $N$ 点重新求 field。它证明所给完整 Fourier 范数对所有角成立，所以覆盖声明的全部有限 N行；P的合法性仍必须由实际完整 tube 的受证外包提供。原 literal table参考若不是准确三角表，需其实际算子权，不冒本函数已支持另一套矩阵。

### 5.2 速度方向 majorant

签名：

    frenet_directional_majorants(domain, direction, sqrt_bits)

domain 必需字段：

| key | 含义 |
|---|---|
| A_lower, A_upper | 同准确半径/路径的正下端及上端 |
| mu_lower, mu_upper | 同径向速度的正下端及上端 |
| nu_abs_upper | 同 $\nu$ 的绝对上界 |
| d_upper, e_upper | 同角 jet 的 Euclidean 上界 |
| P_lower | 原 $A^2\mu^2W-\nu^2Q^3$ 在完整所需 tube 上的严格正下界 |

W_lower 可选，默认0仅表示准确恒有 $W\ge0$；它不替代 P_lower。direction 的 d、e、A、nu、mu 全部必需，都是非负方向上界，不能缺列当零。

返回 -affine-direction 记录：value_upper、first_upper、second_upper、P_first_upper、P_second_upper、sqrt_P_lower_used、AW_lower_used、AW_first_upper、AW_second_upper、原 direction。first/second 是通常导数界，第二项不是 Taylor系数；余项仍乘 $1/2$。

P_lower<=0、scalar下端不正或格式不符会抛明确异常。这说明提交的诊断输入不足，不能据此断言真实场退化或修改原 solver判断。原 producer若只取得未决盒，应保该原地址未付，不伪造一个正数调用。

### 5.3 四块完整有限 RHS 常数

签名：

    finite_rhs_majorants(domain, synthesis, sqrt_bits)

沿用上述 scalar/P/W字段；d_upper/e_upper 由所给完整 synthesis确定，不能混入另一场的角jet盒。返回 -finite-RHS：

- block_lipschitz 的 y、A、nu、mu 四个准确有理上界；
- state_second_direction_upper，控制完整 $D_y^2f_N[v,v]$ 的方向范数；
- coefficient_value_upper 与 mean_value_upper；
- 实际 M/N/physical_size 和四个完整局部 recurrence记录。

同一联合 tube/实际线段合法时，有

$$
\|\Delta f_N\|_\infty\le K_y\|\Delta y\|_\infty+
K_A|\Delta A|+K_\nu|\Delta\nu|+K_\mu|\Delta\mu|.
$$

second_direction 不是完整 Hessian数组，不冒已经求过全部混合列。它足以给同一状态线段的 Taylor余项。四块分责使 numeric scalar与准确目标的变化不被藏入一个未定义“容差”。

### 5.4 实际 cubic

签名：

    cubic_power_bounds(local_power_rows, x0, x1, field_modes)

local_power_rows 有4行，每行全部 $3M+2$ 分量，约定升幂 $(x-x_0)^j$。原 SciPy降幂数据须按真实定义转换，不重新拟合、不截高模、不假共享准确 Hermite端点。

返回 -literal-cubic：准确 x0/x1/M/size、coefficient_abs_upper、C_prime_upper、C_second_upper、runtime_only_bernstein_rows。所有差分/转换为准确有理，不由若干样点推整个多项式范围。

只剩已删文件的 SHA 时，本函数没有恢复能力。未来调用应在原 cleanup前保其真实四行，或由明确新运行按原方法重求；不得从 receipt填造科学输入。

### 5.5 整闭单元残差

签名：

    closed_cell_residual(majorants, cell, scalar_derivatives, samples)

scalar_derivatives 的准确 key 为 A、nu、mu，分别包围对实际 x的导数绝对值。准确前缀可从完整 target三jet给

$$
|A'|\le k_+|a_s|_+,\quad
|\nu'|\le k_+^2|a_{ss}|_+,\quad|\mu'|=0.
$$

每个 sample 必须显式给：

| key | 真实含义 |
|---|---|
| original_address | 原 piece/cell/sample等实际位置 |
| x | 同原闭单元内的准确样点 |
| literal_residual_norm_upper | 所声明原字面残差最大范数的有效上界 |
| formation_error_upper | C′、RHS、相减和必要 norm形成的完整差额 |
| state_gap_upper | 当前准确 C(x)与 nominal输入状态的差 |
| A_gap_upper | 当前准确 A与 nominal半径的差 |
| nu_gap_upper | 当前准确 $A_x$与 nominal ap的差 |
| mu_gap_upper | 当前准确径向速度与 nominal速度的差 |

所有字段必需；代码不为 formation/gap提供零默认。某项若准确同一，应由 caller按真实关系显式传0。

函数保持原样点顺序/原地址；仅为 fill_distance把不同位置排序。重复坐标不伪造新的覆盖长度。至少一个受证样点加完整闭域 Lipschitz界已足以给合法但可能粗的上界，不要求新增求解样点作为接受前门。哪些实际样点参与公式由 caller明说，原未使用/未返的其它记录仍按原必要协议保留。

输出 -closed-cell-residual：

- residual_lipschitz_upper、sample_count；
- runtime_only_sample_records，保每点形成/目标差和 accurate_sample_residual_upper；
- fill_distance、sample_max_upper、eta_C_upper；
- available、unpaid_reason。

无样点时 available=false、相关值null，不返回0。有样点不自动证明输入受证，因此 available只表示公式可形成，不是 science或全域 metric已接受。输入域和形成误差的证据归实际 caller保留。

### 5.6 Quintic 和必要标量

    quintic_residual_transfer(eta_C_upper, E0_upper, E1_upper, state_lipschitz)

准确返回 $\eta_C+E_1+K_yE_0$。caller必须绑定同一目标/tube，以及当前 quintic和声明 cubic的完整差。R514共享端点公式只在前提成立时使用，否则对真实差多项式保完整 Bernstein。

    scalar_necessary_summary(majorants, residual)

返回单个小对象：M/N/维度、四个K、状态二阶界、单元端点、样点数、填充距离、样点最大界、$L_r,\eta_C$、available/未付原因。准确有理数是数值文本，不对大科学树编码压缩。

它只供已有 reader选取，不自建读回帧、成功marker、quiet或raw清理。未来 caller仍须加实际 source/input/field/target/clock身份及完整未付/未访范围，保原单body90KB。整表/样点/系数账留临时现场，不能把这个对象冒成大账已逐值读回。

## 6. 最小真实输入与当前尚缺

已有来源可以提供当前 prefix checkpoint、准确 finite field/完整 target、同C/DAG所有准确 scalar三jet、真实L/L_numeric、实际M/N及原 residual计算位置。现有必要标量不能自动提供：

1. 每个真实 PPoly单元的四行完整系数字词；
2. 所选残差样点的 nominal输入、C′/RHS/相减原字与严格形成误差；
3. 它们与准确目标之间整个联合 tube的P严格下界；
4. 当前 quintic与这条 literal cubic的完整E0/E1；
5. 有限角参考到连续全角速度的投影/aliasing差，或 native尾适用导数证据。

这是具体数据/包围责任，不是让 solver先过更强定理。未来最薄接法是在原 frozen_physical_residual或保存曲线仍存在的同job现场，保实际四行和已有样点/来源，按原预算形成外包；不另开重复全域审计。未付时原R459直接Gram仍可独立完成。

R519同次六jet诊断未收集这些cubic/残差对象，不因本文发表就标成已具备 $K_y,\eta_C$。R504、R464union、动态M等来源也不会因名字相似自动注册；真正 caller须显式绑定其field/target/reference。公式对完整匹配M适用，发布代码本身不修改这些运行入口。

## 7. 原尺度、全闭面与下一消费者边界

原 RMS≤$10^{-6}$、BC≤$10^{-11}$、native≤$2\times10^{-9}$仍是其原范数门。本文不把它们当相对Gram floor，也不宣称mesh变小必达机器精度。

全闭场传递仍需R514列出的有限N到连续角、材料/首共同图、cut与patch、native重构、B/collar、反射/两帽、径向锚和积分。只有所有实际参与的完整片已付，才可写全闭上界。可用四块常数进一步包围合法tube内速度变化，但不据此跳过那些片。

尾部 $\mu=\sqrt{E_C(r)}$还要求真实同C的 $E_C'$；本文没有把E查询盒的宽度或native数值残差替成该导数。本helper不包含R314实际root/因子/两回代/226态RK误差，不用前缀证明删掉它们。

现交付的是明确源码、准确可调用算术核、完整条件推导和真实输入接口。尚无实际值，尚未接新运行。所有新文件小于100KB，只有源/证明/接口入库；可再生展开、原数组或ledger不入Git。未来调用仍只在公开Actions、同原绝对钟与实际owner/quiet/lifecycle下进行。
