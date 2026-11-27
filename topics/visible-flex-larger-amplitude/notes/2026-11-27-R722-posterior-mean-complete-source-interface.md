# R722：完整后验均值存在域与原角 jet／十二片 profile 的独立源码分支

日期：2026-11-27。课题：visible-flex-larger-amplitude。

本交付完成两个独立完整运行源及其全文再生器。新分支用已刊 R722 的后验凸势条件支付准确均值根存在域，然后继续原 0471 的全部 R710 角 jet、R711 十二片 profile 和 R713 费用正文。原 ae67 完整径向积分、原 0471 文件及其 literal-batch CLI 均不修改。它不是一个已运行的数值结果，也不是科学求解器的新增准入步骤。

当前终版明确绑定实际修复后的 meridian-batched 家族：driver 5b0dc3573b4baa86728b0c0628a1338d339a6c4cf5cf0afcead1f4e6febcc58f、reader 79375ead2b0a93a54200d079b691e0fb8e0f74da480e3867ea7c91542f4ab222、normal 33c269f3cd04c9435ccb5144984124c8a0b6ae348f95c8bd71ac92a334c51cf4、packet 45dd618adaa5262002bfb9d1979b6f555fe5233a57ec0f75abcec2ab7633a5be，以及准确输入 fd299d23fcf754021dd1a3048b5f6b4008bf8542ba8e04ec2298830348ef417f。原 41b4/d3f1/388c/910f 科学入口已由真实日志确定在 analytic-frame 的完整方法来源校验处失败；失败来源、日志和未执行费用候选均保留，不能把旧标签贴到新修复族上。终版数学正文没有因此改变；当前仍无可消费的完整场／均值残差／immutable snapshot 成功返回，所有未来点、报告和费用 SHA 为空。

## 1. 完整交付和原来源

| 角色 | 完整文件 | 字节 | SHA256 | 远端 Git blob |
|---|---|---:|---|---|
| 新 R722 数学和实际归属核 | fixed_fejer_meridian_batched_R722_posterior_mean_jets.py | 45225 | e10a0bb386d4c44d9d8dc5ed16c75a37de1ff830754e04d57967780241feacf9 | 64df5fd379ae83ee5282728fc8cd3d72b3ee9c10 |
| 新完整全角径向生产器 | fixed_fejer_meridian_batched_R722_accurate_reference_control_radial_boxes.py | 46486 | 9da25953aeb95b88d5a878935832dac05546b778818e00e588c79581ae664953 | 43408b0f0bc15ad3e2f25805f315023701c354fe |
| 完整源码再生器 | reproduce_fixed_fejer_meridian_batched_R722_mean_sources.py | 56178 | 5325b26da5ffca7ad375bdad6a15c9be945cf08c2782ceac7fc94aa6e2cf2392 | e75dde39d25f151293ad1a2fdb400cae7aabc10c |

三者均位于 scripts/resume_20261126/。本说明及配套 manifest 将完整路径和身份保存为可直接读取的记录。

必要原始来源保持全文：

- fixed_fejer_reference_seed_angular_profile_error_bounds.py：72,182 B，0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b，blob c0d09245e9e156cb93516945b3eec84e93807bf7。
- fixed_fejer_reference_accurate_mean_residuals.py：41,476 B，ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0，blob fdddb363e724ab45204854a2b3084fcb95cae4bc。
- 原完整径向父：45,334 B，a978609f6ec973c5c495e7cdb2a2da36eb2e786f48bd948e5ed1ce488934a1fb，blob f22c1c35b07e771b5ba426729d52e5b6438870dc。
- 原完整准确输入：32,969 B，d9cbf733957e3577cfc6175a1d69024a2874468e1cde7141f5d81b984676430b，blob e420aa38eafafb23054c2b8da10b6c0b48545244。
- 当前实际修复后的完整准确输入：32,969 B，fd299d23fcf754021dd1a3048b5f6b4008bf8542ba8e04ec2298830348ef417f，blob a7ac2ad3892decdb285bbbba60ea9b3e383172a4。仅原 PINS 中 driver、reader、normal、packet、field_binding 五行换成真实修后完整身份，其余全文与 d9cb 一致。完整 137 科学来源仍逐文件读取。
- 完整 R722：results/R722-posterior-convex-mean-root-existence.md，25,682 B，b74d5caf7a0e8185e4f82b76e9db6bfc9f736262c16ed62c1d688ef8e7f78721，blob e43c7082ff04ec2088ae5f22dc40819fba68440f；已刊提交 1a236bf682bd5a7ba5f8b55a8331993e6bd750b0。
- 原十八族完整六费用、137 实际科学角色、38/8 argv、36/48 selectors 的来源：computations/fixed-fejer-meridian-batched-complete-accurate-fees-delivery.json，60,812 B，25d8288c8a812a8b87dec89df9e59ef120982ccc7e6a166c04712311c6630fdd，blob 8129866071548651514aa5a09461ec8314a89725。

来源引用不是缺省字段，也不是把完整科学角色压成任意白名单。运行时仍由对应 accurate input 对全部 137 个实际 source files、原 driver/pure、完整模型、六个输入、点和 snapshot 逐一读取校验。后继修复族应保持这一完整职责。

## 2. saved candidate 的真实接口

原 provider 的完成批次保存九个三维向量：

v、v_phi、v_phiphi、d、d_phi、d_phiphi、w、w_phi、w_phiphi。

另保存六个标量：

lambda、lambda_phi、lambda_phiphi、profile_moment、profile_moment_first_derivative、profile_moment_second_derivative。

原批次没有单独保存 r。新核从全部三个 v 的 canonical binary64 hex 字精确构造有理向量 $\widehat v$，用完整 outward sqrt 界包围 $\widehat r=|\widehat v|$，并在数学上定义 $\widehat d=\widehat v/|\widehat v|$。保存的 d 字不是准确单位方向；它们与全部 w/角导数/profile 字仍原样保留，仅作为原费用输出的误差比较对象。没有以归一化后的近似 float 冒精确单位向量。

实际 row 必须包含且仅包含上述十五个值以及 literal_phi_hex、actual_completed_batch_index、actual_raw_batch_sha256。索引必须对应实际完成的完整批次，literal 角必须在原顺序表中唯一出现；不折角，不取任意未记录候选。

下游 validate_root_domain_attribution 不只信 row 自报身份。它从原 runner_raw_arrays 完整记录重新读取整个 NPZ 的 seed identity、全 literal phi 顺序、所有九向量和六标量；核每个数组完整 shape、binary64 dtype 和有限性，再逐字比较选定 row。NPZ 的完整字节数和 SHA 在前后均核，原路径进入统一 files 集合。没有调用原工作场、Newton、Jacobian 或任何根升级。

## 3. 全角 E0 和完整积分覆盖

新径向模块仍使用 ae67.ActualMeanBatch 的完整数学方法。WholeMean 是明确的全角适配对象：完整准确 fixed chart、scalar/S/R、原 support/central、全部参考 v/一阶/二阶候选，及准确 whole-angle phi interval 都来自当前严格输入。原 literal CLI 的 constructor 未被调用，也未放宽其来源限制。

对于每个 whole-angle cell，原实现计算：

$$
E_j\ \ge\ \left|\partial_\phi^j\{L_c v+B-K\}_{\text{candidate jets}}\right|,
\qquad j=0,1,2.
$$

这里 E0 的积分是准确边界 B、准确补集标量、准确 K 与准确 Lc 的完整外包。候选方向参与边层归一化；不能拿简单 $K-B$ 工作字或有限 quadrature 缺陷代替此积分。

所有原 plan 片和全叶被保存。新完整归属核还会复核：

1. 两个原 supports、四个 boundary layers、两个 central intervals、完整 complement 的准确端点与顺序；从准确 0 到 S 无缺段。
2. 每个非 central 根片只可通过原准确 midpoint 的两个完整孩子替换；全部 active leaves 的 id、深度、左右 affine 系数、kind 与 support index 必须逐字段一致。
3. 不丢弃额外叶，不以 cell count 代替覆盖；central 区只按完整原数学使用 exact Lc*v。
4. 原 complement 的两个 scalar endpoint sums 和全部 boundary 的三 angular jets、三个空间坐标，均由所有 active leaves 的完整 endpoints 重新求和。
5. 所有三个准确残差向量都重新核为 Lc*v_jet + boundary_jet - K_jet，完整范数上界必须向外包含该向量盒。
6. 原完整结构证明与实际 reference model 的 source/T0 描述、完整 reference identity 对应；不是对新候选做 sampled unit 检查。

这项复核没有重新做积分，也不产生新的数值候选。准确积分本身来自保留全文且严格绑定的原方法。若全 plan 的正宽或后验不等式尚未在声明的 outward 精度中分开，只留下未付结果，不减少域或用部分叶冒完整结果。

## 4. R722 后验域的有向算术

下列符号与已刊 R722 的区间实例一致。令 $\ell_-\le L_c\le\ell_+$，$b_+$ 是所有边层完整测度的上界；$\widehat r_-\le|\widehat v|\le\widehat r_+$，$\widehat v_z>0$。记 U/D 为声明 bits 上的 dyadic 向上／向下取整：

$$
z_- =D(\widehat v_z/\widehat r_+),\qquad
a_-=D(\ell_-\widehat r_-),\quad a_+=U(\ell_+\widehat r_+).
$$

$$
\eta_0=U(2E_0/a_-),\qquad
\zeta=D(z_- -\eta_0)>0,\qquad L_B=U(b_+/\zeta).
$$

$$
\Delta=U(E_0+L_B\eta_0),\quad
\alpha_-=D(a_- -\Delta)>0,\quad
\alpha_+=U(a_++\Delta)<\ell_-.
$$

$$
r_-=D(\alpha_-/\ell_+),\qquad
r_+=U(\alpha_+/\ell_-),\qquad 0<r_-\le r_+<1.
$$

另外保留 R722 的方向／向量后验误差和完整非对称 J 逆界：

$$
\eta_1=U\!\left(\frac{2E_0}{a_-+\alpha_-}\right),\qquad
E_v=U\!\left(\frac{E_0+L_B\eta_1}{\ell_-}\right),\qquad
\|J^{-1}\|\le U\!\left(\frac{1+L_B/(\ell_- r_-)}{\ell_-}\right).
$$

每一步使用 Fraction 与原完整 outward arithmetic。源码不创建虚构根，不以工作 d 的近单位长度作为假设。全闭单位球上的凸势、帽定位、正 KKT 乘子及唯一性由 R722 支付；本文件负责把真实完整输入变为可复读的条件实例，不重证明 R722。

旧 K 范数和 K_z 的粗余量仍在原 result 中保持真实值。新存在分支不要求它们先通过，也绝不把 all_pointwise_R709_sufficient_inequalities_proved 改为 true。新的 posterior_R722_existence_verified_on_this_whole_interval 只有新条件全部严格成立后才产生。它仅表示该准确 whole-angle cell 的均值域，不表示完整圆周、normal 根链或闭面已经完成。

## 5. 保留的角 jet 与 profile 正文

原 0471.mean_jet_bounds 的完整函数为 8,149 B，SHA e0e233134abb87feb740652810e89d8472588ef162206021a3f04461ea05791f。新函数只替换其 root-domain 前段并绑定原数学函数；从 profile_delta = length["profile_delta"] 到原完整 return 的 **7,133 B** 后缀逐字保留，SHA 4fc958af144bbd27f5c1745fe7d9bd2db86b2ff9aad4ef245b462847aac38db2。

因此原两阶 mean/vector/direction/frame、完整非对称 J 及差界、v/d/w 所有角导数、完整三 profile moments 和 lambda 的两阶费用都继续同一原公式。新域提供的 $r_-,r_+,\zeta$ 替代旧 coarse K 推出的域；后续误差界、十二片积分和严格幅度分支并未裁减。

原后缀实际使用其原保守误差 Ev；R722 的额外较紧 vector bound 被保存在归属中，不偷偷替换旧公式。若实际 lambda 候选尚不能在 (0,pi) 内证明，或完整 profile 导数正下界未分开，仍沿原 unavailable 处理，不借后验根存在掩盖 profile 的未付义务。

bind_parent_math 核原完整文件 SHA、原 provider 与完整九/六字段表，并要求实际函数 code filename 指向该原全文；pi_bounds 的原 lru_cache wrapper 使用原 __wrapped__，Interval 使用真实 __post_init__，不误把 dataclass 生成的 init 当源码函数。这里只读来源，不导入工作场。

## 6. 精确运行 API

新核不提供 literal-batch CLI。完整径向模块创建：

    module = load(full_new_helper_path, exact_helper_SHA)
    kernel = module.PosteriorMeanKernel(actual, original_0471_module, original_ae67_module)

actual 是原严格 ActualNormalPacketPoint 实例；初始绑定时还将新 helper 本文件和完整已刊 R722 theorem 文件加入 actual.used，保留真实 whole file records。

其全角调用为：

    result = kernel.mean_jet_bounds(
        geometry, actual_working_row, complete_total_equation,
        complete_exact_mean_plan, all_active_integral_leaves,
        encoded_accurate_phi_interval,
        bits=geometry.bits,
        taylor_order=original_taylor_order,
        profile_series_order=original_profile_series_order)

成功结果完整保留原 mean 输出，并增加：

- root_domain_attribution：schema/body/canonical identity 完整对象；
- root_domain_source 与 root_domain_source_sha256：明确新 R722 来源；
- original_R709_coarse_inequalities_proved：原结果的真实 boolean；
- original_R709_coarse_inequalities_assumed_for_existence=False。

新 mean evidence schema 为 same-actual-reference-whole-angle-R722-posterior-mean-enclosure-v1。除原全部 integral/evidence 外增加 complete_posterior_mean_root_domain、complete_shared_R710_R711_math_source_sha256 和 complete_R722_theorem_sha256。旧 sufficient_R709_inequalities_verified_on_this_whole_interval 仍等于原 row 的实际 boolean，不强制 true。

## 7. 下游必须显式接入的接口

这是下游完整源实现职责，不是额外科学预门。

### 7.1 第四个费用源码角色

原 normal.PINS 与 leaf._verify_source_roles 严格列三个费用角色。新独立族应增加 posterior_mean 这个第四个费用角色，完整 pin 新 helper。科学 runtime 的 137 全角色不能因此替换或减少；它们与费用角色是不同集合。

g.identity 的完整 canonical 定义新增三项：

- posterior_mean_source_sha256；
- posterior_mean_theorem_sha256；
- posterior_mean_definition_identity_sha256。

g.metadata().posterior_mean 保存 helper/theorem 原始路径、完整 SHA/bytes、definition 和 definition identity。leaf.verify_geometry_identity 应按相同完整对象重算，不能剥去新字段。

### 7.2 真实 whole-angle 叶读者

原 leaf.load_job 内 bind_reference 的 R709 true 检查必须在新独立源中改为 R722 完整验证。其余 actual_input、geometry、phi、anchor、全 plan、complete flags、文件身份、all32 stage journals 等检查全部保留。

精确 API：

    posterior.validate_root_domain_attribution(
        mean["complete_posterior_mean_root_domain"],
        parent_math=original_0471_module,
        actual_binding=context["actual"],
        geometry_identity=context["geometry"]["identity"],
        phi_interval=request["accurate_phi_interval"],
        total_equation=mean["complete_accurate_total_equation"],
        exact_partition=mean["exact_partition"],
        active_leaves=mean["complete_active_leaves"],
        structural_reference=mean["structural_boundary_unit_proof"],
        files=files, bits=context["bits"])

parent_math 是完整 0471 模块，不能用 rotation29eed 的同名函数代替。该 API 真正重读原批次，并完整重算 source_scope、所有有理条件和 canonical identity，要求完整对象相等。它不会因为 evidence 自报 posterior_R722=True 而接受。

原 helper/theorem files 按生产时的 record path 实读；当前 detached checkout 的加载模块可以在另一绝对路径，必须以完整 SHA 和 bytes 与那个原记录相等关联。actual point、report、snapshot、原 batch 与对应 job/domain 文件关系仍严格；缺原件不能由改名副本掩盖。

### 7.3 全周期语义

normal 的 full_R709_unique_reference_mean_and_projected_frame_are_two_pi_periodic 与 leaf 的 periodic_keys 是第二处强语义依赖。新独立源应明确改为 full_R722_unique_reference_mean_and_projected_frame_are_two_pi_periodic，并保持完整固定／当前整数频率、准确 inverse lift、相同原方程、全角覆盖及全部定向 normal-root glue 责任。

R722 给每个 phi 的全闭球唯一均值，因原完整方程两 pi 周期，才能在完整圆周成功覆盖后得到同一均值／projected frame 的周期性。单 cell 后验成功不能取代全部 1024 闭角胞，也不能替 normal roots 自动选择分支。

### 7.4 其余下游

geometry/bridge/closed/R716 的新版本须按新的 normal/leaf/radial 完整 SHA 递归闭合。不得只把旧 source label 改名而仍信旧 R709 boolean。原原始物理 sixjet、同叶全三维 D、全 support/Gram/curvature、闭面上下片／帽／全部相位／mixed pair、八类 beta 证据及晚失败规则均独立保留。

## 8. 全参数与实际范围不变

原 complete-normal ready 的完整参数是：

    --repo {repo}
    --report {work}/fixed-fejer-meridian-batched-first/report.json
    --outdir {work}/fixed-fejer-meridian-batched-normal-root-and-sixjet-fees-v1
    --seconds 900
    --maximum-leaf-evaluations 1000000
    --precision-bits 192
    --panels 128
    --rho-leaf-budget 8192
    --inverse-steps 64
    --inverse-width 1/1000000000000000000000000
    --full-angle-cells 1024
    --radial-depth 0
    --mean-maximum-splits 8192
    --mean-width-goal 1/1000000000
    --first-exp-degree 24
    --maximum-exp-degree 128
    --root-radius 1/100000000
    --root-radius 1/1000000
    --root-radius 1/10000

完整后继要使用新文件和独立 fresh 输出目录；这里引用的是原参数，不排队复用旧输出。全部原 budget、root proposals、1024 closed cells、全 radial plan、所有 actual literal candidates 和 normal32 保持。两新增 library 本身无新 CLI 参数；source reader 与 field candidate 仍必须是真实完成的完整 report/immutable required-angle snapshot，不能用 live progress、prepared input、failed constructor 或未来 final 代替。

原 normal ready 的全 36 selectors 和 geometry ready 的全 48 selectors 均由下游完整源/ready 派生原样保存。输出目录和来源 label 必须与新完整版本对应；不能为队列容量删除参数、读数或未付历史责任。

## 9. 未付和失败语义

PosteriorDomainUnavailable 表示声明精度或准确积分宽度尚不能支付后验充分条件；其参数／误差不会被置零。径向模块将它转换为既有 EnclosureUnavailable，自然返回保留真实完整前缀。source/path/model/字节不一致仍是 ValueError，不被当成数学未付吞掉。

报告不声称非存在、不声称原工作 Newton 失败，更不把旧粗 R709 未证解释为准确根不存在。反过来，R722 成功也只补准确定义的均值域：R710 jet/profile 的完整费用、normal32 每段的 contraction/invariance、全角同支、物理 sixjet、closed surface/phase/reach 都须各自继续由实际全域输入支付。

当前无 actual residual E0 数值、无后验 r/zeta/alpha 成功范围、无 field point 或 fee 完成值。所有预期未来身份均为空。原 18 constructor 来源失败是独立真实实现事件，本交付不改其原日志或已排源。

## 10. 全文再生与已做工作范围

再生器只读两个完整父文件，以完整 SHA 硬核，核原完整 mean function 及 7,133 B 后缀，然后写出完整新 kernel 和径向体。径向修改恰为十一个明确文本替换，其中一个是实际 input 的 d9cb→fd299 来源更新；逆向十一个替换逐字恢复 a978 全文。完整新 source SHA 是输出检查，不是缺失来源的替代品。

本次实际完成的检查仅为 V8 中的全文字符串构造、全文 SHA/bytes、完整逆向文本一致性、原后缀逐字包含，以及远端完整 blob 保护。没有 import scientific module、没有 AST/compile、没有本机数值、没有任何 fixture 或额外科学试跑。再生器可用于原始来源恢复，不被插入求解前置门。

原 source 文件、旧六费用、失败路径和未知历史均保留。refs、queue 和真实运行由根代理处理；本交付不做这些修改。

## 11. 指定独立文字核的范围

solver 独立读取了候选 75f0e8c2 的 posterior_root_domain 与 _mean_jet_bounds 前段，并取回完整 0471 核对 lower/upper_dyadic、point_norm、cap_floor 和 exact_relative_lengths。其所读范围确认 ahat/r/zeta/Delta/alpha 的舍入方向、严格 alpha_hi<lc、以及新域接原 R710/R711 后缀一致。这两个数学段在终版逐字保持。该核验不扩充为完整 active-leaf cover、来源、残差复读或最终修复 pin 的独立审计，也没有 AST、数值或科学执行；不作为额外准入门。
