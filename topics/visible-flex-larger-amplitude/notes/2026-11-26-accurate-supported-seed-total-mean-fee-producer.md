# R713 同实际 batch 的准确总均值费用生产器

状态：完整源码已形成，当前仅进行了 stdlib AST、compile、py_compile、重复字面 key/keyword、尾空白与三项完整来源 SHA 检查。没有本地积分、区间函数、NumPy/PyTorch 模块导入、root、F/J 或科学 fixture。首次科学执行只允许公开 Rogerhu12/math-research-public Actions。此组件不作为新 solver 的先行门。

## 1. 本组件真正支付的对象

R713 已从完整十二片 profile 的准确 Fraction 矩，支付实际 lambda 字对应 A、A'、A'' 的费用。其余条件输入中，最关键的是同一个准确均值方程在真实工作 v、v_phi、v_phiphi 处的零、一、二 total-angle residual 上界。

本生产器直接对该准确方程积分。它不把实际 mean solver 输出的 working residual 叫作准确误差，也不根据“均值求解成功”将误差设零。全部原参考、固定 scalar、core/H、支持端点、四个边层、补集与无限振荡尾均保留。

源码 basename：supported_smooth_triangle_accurate_mean_residuals.py。

该源分别绑定：

- R713 完整实际 batch 消费者 82e6f1a714c241b1e445304017613cc0fab8874520ef7d6904acf3ae62904f76。
- 原完整准确 reference 4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3。
- 已刊 whole-cell scalar 包围 a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6。

第三项只复用纯 ScalarWholeInterval 的完整径向公式。生产器有自己明确的新 actual-seed binder；不会调用或冒用 a846 的旧 hDelta ActualInput 身份，且没有把新的 seed 场伪装为 606/7f 的实际输出。

## 2. 准确方程与三个真实候选 jet

同一个实际完成 batch 给出每个 literal phi 的三组完整 binary64 字

$$
 \widehat v_0,\quad \widehat v_1,\quad\widehat v_2.
$$

把这些字分别当作准确有理向量。用完整 N(v)=v/|v| 的一、二导数，向外得到

$$
 d_0=N(\widehat v_0),\quad
 d_1=DN(\widehat v_0)[\widehat v_1],\quad
 d_2=DN(\widehat v_0)[\widehat v_2]
            +D^2N(\widehat v_0)[\widehat v_1,\widehat v_1].
 \tag{1}
$$

这些是准确方程在候选 v jet 上的方向，不是把 mean 核输出的已舍入 d/d_phi/d_phiphi 当作准确归一化；R713 后续会分别比较实际保存的工作量。

设支持 U 有两个准确相对区间，边层合长 b，中央合长 Lc。原准确单位 meridian 为

$$
 T_0(s,\phi)=b_0(s)e(\phi)+c_0(s)e_z,\qquad
 e=e_r(\Theta_0(\phi)).
$$

其中 b0、c0 与已有 R690 scalar 的准确定义完全相同。这里将径向系数写 b0，避免与边层总长度混淆。固定 chart 的 phi jets 只作用于 e：

$$
 T_{0,\phi}=b_0e_\phi,\qquad
 T_{0,\phi\phi}=b_0e_{\phi\phi}.
$$

在一个边层定义 Y_j=(1-chi)T0_j+chi d_j。因 chi 只依径向，

$$
 V_0=N(Y_0),\quad
 V_1=DN(Y_0)[Y_1],\quad
 V_2=DN(Y_0)[Y_2]+D^2N(Y_0)[Y_1,Y_1].
 \tag{2}
$$

生产器对 (2) 的全部三 jet 作准确积分，不删除交叉项。记边层积分为 B_j，补集标量积分为

$$
 I_b=\int_{[0,S]\setminus U}b_0(s)\,ds,\qquad
 I_c=\int_{[0,S]\setminus U}c_0(s)\,ds.
$$

于是

$$
\begin{aligned}
 K_0&=(R-I_b)e+(H-I_c)e_z-\Gamma,\\
 K_1&=(R-I_b)e_\phi-\Gamma_\phi,\\
 K_2&=(R-I_b)e_{\phi\phi}-\Gamma_{\phi\phi},\\
 {\cal R}_j&=L_c\widehat v_j+B_j-K_j,\qquad j=0,1,2.
\end{aligned}
 \tag{3}
$$

式 (3) 是 R710/R713 所需的三个准确 total-equation residual。中央 Lc*v 是均值方程的准确定义；它不是声称用实际 lambda_hat、d_hat、w_hat 和 working profile 节点拼出的实际整场积分已等于 Lc*v。lambda 的实际 scalar moment 残差与其准确根位置变化，仍由 R713 独立完整支付。

积分域及其端点不依 phi，故 (3) 的两次角导没有遗漏移动边界项。全部外层 omega/core/H 在求解中仍自由；本生产器只认证已经冻结的参考 seed 同一 batch，既不覆盖其当前 outer normal 修正，也不重做该修正。

## 3. 完整准确固定 chart、Gamma 与 cap

固定 chart 读取实际 reference 全部160个 core 字，不截频。使用已绑定 e091 整数区间 sine/cosine：

$$
 \Theta_0=\phi+\sum_m\frac{1-\nu_m^2}{\nu_m}c_m\sin(\nu_m\phi),
$$

以及完整 rho、rho_phi，得到

$$
 e_\phi=\rho e_\theta,\qquad
 e_{\phi\phi}=\rho_\phi e_\theta-\rho^2e.
$$

core 支持函数仍在原 normal angle phi，而不是 Theta0：

$$
 \Gamma=p e_r(\phi)+p_\phi e_\theta(\phi),\quad
 \Gamma_\phi=\rho e_\theta(\phi),\quad
 \Gamma_{\phi\phi}=\rho_\phi e_\theta(\phi)-\rho e_r(\phi).
 \tag{4}
$$

式 (4) 末项是 rho 而非 rho²；source 与原 provider 相同。真实 R 使用本次完整 reference 的 radius_complete_enclosure，H 使用本次 seed 的 literal initial_height_hex。S 使用同一个 FullHold 准确 affine-time 盒。没有把工作 mesh[-1]、radius carrier 或旧 run 的 H 字替换进准确定义。

每个 batch literal phi 保原顺序及全部字，不按十进制重新取点。每点 rho 的严格正下界由完整整数公式实际包围；这是所请求角点的事实，不冒全角正性证书。

## 4. 正归一化分母的来源

完整原 prefix 的 FullHold 构造器以逐胞 Bernstein 导数界验证 |a_s|<1，选择正平方根。原解析段和 Hold 的角位于规定区间，c=cos(alpha) 非负；R669 第2节已给完整证明。R690 第2、2.1、2.3节给新尾 b0=-cos(beta)、c0=sin(beta)，0≤beta<pi/2。当前完整 4e canonical/source 实现这四支，故全原参考准确满足

$$
 |T_0|=1,\qquad 0\le c_0\le1,\qquad |b_0|\le1.
$$

source 核同一完整 scalar/core/model，以及 FullHold.old_ap_bound<1、原 out<1/40、kappa=3/2；a846 返回的向外 b/c 盒与这些已证结构界取交。若交集为空即报错，不能用结构声明掩盖错误输入。

候选 v0 的准确范数有严格正下界且 v0_z>0时，其方向 dz≥zeta_hat>0。R710 已证完整边层

$$
 |(1-\chi)T_0+\chi d_0|
 \ge \sqrt{\frac{\zeta_{\rm hat}^2}
 {2(1+\sqrt{1-\zeta_{\rm hat}^2})}}>0.
 \tag{5}
$$

生产器用有理化公式计算 (5) 的严格向下界，再完整应用 DN/D²N。chi∈[0,1] 且两端单位，还给 |Y0|≤1；这也是准确结构界，未将工作归一化的误差裁去。

## 5. 没有抽样遗漏的全域积分包围

初始分割包含全部923个准确 affine-in-S 原节点，并加入两个支持、四个边层和两个中央区间的全部准确端点。排序用同准确 S 的区间判定；无法严格分离不同 affine 点时诚实返回，不能靠工作 mesh 顺序强置准确顺序。

每个非中央初始片严格归为补集或某一个边层。中央项由 (3) 的准确 Lc*v 支付。a846 ScalarWholeInterval 对每个完整子片给 b0、c0 的向外包围，其中保留原 prefix、原解析、全部五个 Hold 段以及到 t=0 的无限新尾，不把端点盒冒 whole-cell 盒。

若完整片 I=[l,r] 上每个准确 integrand 分量属于 [L,U]，且准确物理宽度属于正盒 W，则

$$
 \int_I f(s)\,ds\ \in\ W[L,U].
 \tag{6}
$$

证明：准确宽度 w>0 下积分平均位于 [L,U]，乘 w 后再外扩到 W。分量和角 jet 分别应用即可。没有任何浮点 Gaussian 节点、库 trig 或求和被当作准确数。

边层 chi 是 S5 从原 T0 到 d 的准确 cutoff。源先以准确 s/S 计算完整 local-u 盒，再利用 S5 在 [0,1] 单调，以两个端点有理值包围 chi；右端层的方向明确反转。chi 与 T0 区间的相关性只使界变宽，不会漏掉准确值。

每片的三 jet 积分盒加和给完整 B_j；补集只累计完整 b0/c0 两个标量积分，再在 (3) 中组合，保留 R−I_b 的准确抵消。范数上界从完整三维残差盒以向外平方根计算，给出 E0、R1、R2。原 working Gauss、normalization、NumPy/Torch reduction 的所有差异不需要逐项假设精度，因为这里直接包围的是准确方程在真实候选字处的值。

此实现使用一阶 range 积分包围，未声称高阶收敛速度或指定600秒必达到宽度目标。若证明输入盒或模型带来误差底限，tolerance_reached 可以一直为 false；已有完整包围仍诚实保留。

## 6. 可恢复的完整叶与有向误差和

journal 记录两种完整事件：

1. 初始完整片的一次实际向外积分结果。
2. 一个仍活跃的完整父片被两个准确 affine 中点子片共同替换；两个子片全部完成后才提交事件。

不删除未处理补集或尾片。深度任意，叶ID用层次分隔符，避免 r1/0 与原根 r10 混名。

绑定含完整 source、实际 report/batch 原字、reference/scalar/core/H、准确全部分割、精度和宽度目标。每条事件含序号、前条摘要与完整 payload 摘要。恢复严格核全部链、初始片顺序、每次准确父子覆盖与两种 integral shape。它重用已经付款的区间结果，不重做旧数值场。改变源、batch、phi、分割或精度不能混续旧 journal。

活跃叶的下端点与上端点分别用准确 Fraction 累计。替换父片时从这两个精确端点和中分别减去原贡献、加两子贡献；这不是用 Minkowski 区间减法伪装移除父误差，也不因多次更新增加无谓区间膨胀。

自然预算只在完整事件之间检查。未完成全部初始非中央片时，complete=false，既不输出全 residual，也不写可消费的 fee-request。完整覆盖之后，即使精度目标未到，complete=true 仅指全域包围已付；tolerance_reached 独立记录。每个实际角的 R709 充分不等式亦单独记录，不能把“积分覆盖完整”当作“mean 存在条件已过”。

## 7. 实际输入绑定闭包

先调用已刊 R713 bind_actual_batch，它完整调用真实 pure reader，读取同一个捕获的 report 快照以及真实 batch NPZ，核全部15个保存数组、全部 phi 字顺序、来源/seed/target/chart，并在前后核 report/NPZ 字节未变。

随后显式传入并验证本次五个 raw 输入：

- reference_bundle；
- carrier；
- node_report；
- scalar_input；
- preparation_report。

它们必须逐 SHA 等于同一实际 outer report 的绑定。原4e.from_files 再核完整 reference model、原source、全部 positive observation、full scalar definition、true symbolic nodes 和固定 chart。新producer再次比较其完整 canonical 与 seed 内嵌的 complete_axisymmetric_reference_model、profile、H及core身份。跨 job 路径可显式变化，但相同源/原始字节身份不能猜测或替换。

本组件从来没有构造 outer SO3 operator，因此没有暗做 F/J、normal 根或科学预试。准确 scalar/reference interval 的重新构造是本组件自身实际费用，写入此次 wall time 和调用计数。

## 8. 输出与下游接口

主报告 schema：

complete-supported-smooth-triangle-accurate-total-mean-residuals-v1

全覆盖时生成 fee-request.json，schema 精确采用已刊 R713 的：

actual-supported-smooth-triangle-seed-accurate-fee-request-v1

其 binding 保实际 report/seed/batch/scalar/chart 摘要，每个完整实际 phi 行含：

- accurate_S_enclosure；
- K_norm_lower、K_norm_upper、K_vertical_lower；
- accurate_centered_total_equation_residual_norms 的三项真实上界；
- boundary_reference_phi_norm_upper、boundary_reference_phiphi_norm_upper；
- accurate_fixed_chart_radial_jets 的 e、ep、epp；
- 完整参考准确单位/非负支路与固定水平 e 的真实来源声明；
- 用于复核的完整 residual/K 三 jet 盒。

当前 nodes=[]：本次负责准确总均值费用，不捏造 arbitrary node 的准确地址/working六jet。R713 可先消费所有均值/幅度/角根费用；节点责任须由其另一个真实地址生产者接入。

request 的外部费用来源完整记录本source、same-seed binding、全journal文件及链摘要、全参考身份和全部尾覆盖。这里“外部”是相对已刊 R713 消费核；其三均值 residual 在本组件中确实计算，未由用户填一个未经证实的0。

报告明确写 profile_moments_computed_here=false 和 profile_moments_require_independent_R713_consumer=true；这只说明职责分界，不宣称尚未运行的 R713 下游已经计算或支付任何 profile 费用。

每个有限 batch 点的R709充分条件可以由K与长度盒实际验证。它们不是连续全角覆盖；full_angle_R709_hypotheses_certified、continuous_phi_cover_certified、全outer-normal、metric、reach与embedding证书标志均为false。

## 9. 完整可执行 CLI 合同

本组件的命令形态如下。所有路径指本次公开 runner 已存在的真实报告和原始输入，不把旧run SHA 写成新的必然输出。

    python supported_smooth_triangle_accurate_mean_residuals.py
      --repo CURRENT_SOURCE_CHECKOUT
      --report ACTUAL_TRIANGLE_REPORT
      --batch-index ACTUAL_COMPLETED_BATCH_INDEX
      --reference-bundle CURRENT_REFERENCE_NPZ
      --carrier CURRENT_OBSERVATIONS_NPZ
      --node-report CURRENT_NODES_JSON
      --scalar-input CURRENT_ORIGINAL_SCALAR_GZIP
      --preparation-report CURRENT_PREPARATION_REPORT
      --outdir RUNNER_ONLY_MEAN_FEES_DIRECTORY
      --panels 128 --precision-bits 160
      --width-goal 1/100000000 --seconds 600

同目录再次执行按严格 journal 继续；报告可重写，但源与全部 actual binding 必须相同。--batch-arrays 仅用于显式搬移相同 NPZ 字节。--maximum-transitions 是可选的自然完整事件预算，不改变准确积分定义。

--seconds 限积分循环的新完整事件准入；初始化实际 raw/ref 绑定、最后完整事件、输出和恢复的时间单独包含在 total_invocation_seconds，不冒为严格进程硬限。该接口尚未科学执行，首次运行真实成本未知。

可安全公开的紧凑摘要是 complete、tolerance_reached、completed_initial_pieces、required_initial_pieces、active_complete_leaves、total_complete_transitions、literal_angle_count、maximum_total_equation_component_L1_width、all_literal_angle_R709_hypotheses_proved 与 report/journal 摘要。不要把完整 interval 数组、所有 journal 内容或对象型 binding 塞进 scalar-only 控制器metadata。raw仅留runner，不进Git/artifact。

## 10. 与 centred normal 方案的边界

完整准确 mean residual 和 R713 profile费用，是把准确闭合seed与实际工作seed联系起来的一部分。当前生产器没有直接读取 normal 的原胞 Gauss/cumsum，也没有把其 zero-control residual 改成0。

若后续采用基线差分积分，固定closure校准项必须进入完整物理六jet；还须付实际同Gauss/cumsum与真实reference节点的费用。当前输出可以供这一完整下游组合，但不能单凭本文的准确 F(v) 界就宣称其实际 outer field 已闭合、径向等距或达到reach标准。

参考：R669、R690、R708、R709、R710、R713、R714；当前四段准确标量及 a846 whole-cell 连续包围的已刊完整源。

## 11. 冻结身份与本轮静态核范围

完整源码冻结为39,493 B，SHA256为 581fbcc397d379b64ee4a1d36b864b9a9e3b537f7b1be962ae03e22920c72202；不再修改此字节。完整数学/chart/leaf/组合段由geometry独立读核，初末实际字节绑定、完整journal和API由solver独立读核，均未发现所读范围的阻断。来源三pin在当前完整仓库逐SHA核过；本地仅stdlib AST/compile/py_compile及文本结构检查，没有科学运行。

配套 smooth-triangle-accurate-mean-batch0-600s-ready.json 是单个下游600秒完整步。它只预定真实报告路径和batch索引，不预造该batch已存在；目前没有准入。首次实际 R711 报告包含完整batch0及其raw数组之后才能使用。若producer完整覆盖尚未返回，不能以一个不存在的fee-request启动R713消费者。所有源/参数/小说明可入Git，所有raw区间、journal与batch数组只留runner。
