# Actual09：完整闭参数面通量矩与 R716 重心补偿入口

2026-11-27，Astra-larger-e4e2a2bf-20261126。

**状态：三件完整新源及完整参数计划；没有新的场、矩积分结果或非全等证书。** 本入口消费 actual09 已固定目标和同一真实点的完整准确 normal/六 jet 输出。当前约定的 ff544 科学报告尚未在本次编写中作为成功字段读到，后继 report、snapshot、根盒、积分值与 SHA 均不预填。

数学依据为 [R716](../results/R716-asymmetric-fixed-caps-and-centred-volume-moment.md)、[R625](../results/R625-second-volume-moment-quotient-bound-and-fixed-caps.md) 与 [R661](../results/R661-complete-nonplanar-activity-and-four-fixed-markers.md)。这里实现既有公式的完整数据消费者，不重报这些定理，不更换 p4 帽或固定度量，不添加优化前门。

## 1. 本次绑定的实际对象

本入口仅接受以下完整源链：

- scientific driver `ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5`；
- full pure reader `aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32`；
- complete normal `3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc`；
- complete base `6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865`；
- actual09 fixed target `7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a`；
- actual reference model `d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75`。

完整准确输入/旋转/径向/上层源分别为 f0808c85、29eed317、0587d88c、f5ecc7fb。全 SHA 及真实文件名写在源和交付清单中。固定当前参考使用实际1995叶的数据责任；2397叶只用于恢复历史 dc5 材料地址，不作为当前参考函数值。

输入路径约定为 `{work}/run09-normal-root-and-sixjet-fees-v1/report.json`。这个路径来自完整准确 normal 计划，不能仅因路径已登记就当作文件存在。若没有实际 report，矩入口写明 `actual_input_available=false`、`complete=false`，全部完整域总矩为 null。若准确 producer 只完成 setup 或若干角胞，它保留实际部分贡献与全部未付域，不填零代替缺域。

没有改动科学源、32个 normal 阶段、所有优化变量、原范数、QP、线搜索、P0、旧/当前材料格、typed 历史或实际筛查。此处同样不移除未返回的 run07/run08 历史责任。

## 2. 完整源的分工和边界

`r716_closed_surface_moment_arithmetic.py` 是独立完整的有理向外算术与矩公式源；`run09_complete_closed_surface_moment_integrals.py` 读取全部准确域流并积累矩；`run09_r716_centred_volume_moment.py` 从前者的全部实际块重建总和、重核来源/选支，再计算一般中心矩以及在条件已付时启用的半转简式。

三个文件均完整，小于100000字节。没有通过裁掉校验函数、只发布差异或将大型原始报告改名为参数来满足限制。新源的科学入口均要求本仓库公开 Actions。编写期间只做完整文字/接口/来源审查和字节身份保护；当前执行环境不可用，没有声称已做新源 AST、compile、科学导入、Fraction 算例或数值 fixture。完整源码可由根在环境恢复后做纯源码检查；这不是要求另跑缩小物理问题。

原准确 normal producer 在末次检查全部输入、输出、顶层 immutable binding 后才将
`all_bound_input_and_output_bytes_rechecked_at_final_report` 置 true。本入口保留这个责任：只要它仍 false，即使某些流已经存在，也不把完整矩标成 complete。矩入口自身又对所有已消费文件重核全 SHA/字节，并在输出前执行末次全量重核。

## 3. 从真实点到整个闭参数域的准确绑定

顶层同时核准确请求 binding、准确执行 binding、actual input 的 canonical identity、原 scientific report 的全模型、58个实际 runtime source records、六个真实参考输入、完整当前点 packet 与对应 snapshot。每个文件都按真实路径、完整字节数、whole SHA 读回；不是只比较自报模型字符串。

当前点按原 M160/J923 布局完整读出：157个自由 core 字、2766个自由径向 jet 行各482个旋转槽和一个 H，总计1,333,370个自由变量。完整数组 dtype、shape、所有字节及旧数组摘要格式逐项核对；H 从同一实际点的末字取得，与准确几何的 exact H 相等。没有只读取若干控制块，更没有重置到 reference 初点。

source 的精确行掩码使 core 旋转 value 行以及 cap value/first 两行准确为零；core first/second 与 cap second 保持自由。两完整 Q 支撑和 gamma 支撑严格位于 $(0,S)$，原 supported seed 的两个支撑也全部位于内部。core/cap 的准确端点律仍取原完整源，未用工作 mesh 差冒准确 S。

每个 angular job 的完整 header、hash-linked journal、全部32个成功 stage 或真实失败尝试均读回。成功 stage 的 tau、真实 eta 中心词、局部收缩半径、q<1、严格自映余量、三层角 jet 与全部六控制都保留。原 packet 与实际数组文件、完整准确 mean/domain 证明文件也逐字绑定。后者必须是同 actual input、同准确几何、同 exact angular request、同 anchor 和同全径向分区，不能将另一角或另一参考的完整均值盒移用。

未初始化的角 job 可以没有 journal；它只保留诚实 pending 状态。不能因为首场或准确 setup 失败而让一个缺字段的后续 pure reader 再次掩盖原原因。反过来，任何自称成功的 job 都必须拥有完整32 stage、完整径向物理流及其结束事件。

## 4. 全径向、全角覆盖怎样进入积分

准确径向 leaf 的端点采用原约定：

$$
s=\alpha S+\beta,\qquad (\alpha,\beta)\in\mathbb Q^2.
$$

本入口从准确几何的完整原 plan 独立恢复每个 leaf 的有序地址、原 cell、kind、support index、depth 和准确端点。分区从 $(0,0)$ 到 $(1,0)$，相邻端点严格同词，包含全部922个原径向 cell，包括完整前缀、所有拼接段和无限尾的准确包围。额外 dyadic refinement 只按已声明 depth 完整细分；不会丢弃宽或困难的 leaf。

每个准确宽度是

$$
\Delta s=(\alpha_1-\alpha_0)S+(\beta_1-\beta_0).
$$

必须由真实 S 包围证明其严格为正，不能用 float mesh 相邻差、工作 Gauss mass 或单个节点权重代替。

全角计划完整保留 $\phi/\pi\in[0,2]$ 的全部1024闭胞，以及所有实际 cached/required literal 角。第 i 个全角胞准确为

$$
[2i/N,\,2(i+1)/N]\,\pi,\qquad N=1024.
$$

角度盒用原准确 pi 包围生成；测度为真正 $(2/N)\pi$。没有四分之一对称缩减，没有由几个角的正值猜全圈，没有套 R625 仅适用于有限 Fourier–quintic 表示的固定精确 Gauss 节点数。SO3 指数和隐式 normal 的非有限多项式依赖始终保留。

积分读取每个 leaf×whole-angle cell 的完整六 jet 盒：

$$
F,\ F_s,\ F_\phi,\ F_{ss},\ F_{s\phi},\ F_{\phi\phi}.
$$

用于通量的 $F,F_s,F_\phi$ 已包含原始 hDelta 修正及全部 hp/hpp 责任。即使中心化根残差很小，也不删除这些项或把单位 meridian T 冒作物理 Fs。每个 gzip stream 的 header、每条实际有序 leaf 记录、footer、全记录数及全文件 SHA 都核回；footer 后不允许额外内容。

对每个准确闭胞 B，先用区间运算得到完整被积函数范围 $[f]_B$，再乘真实正测度 $|B|$。由于这是整个胞上的范围包围，

$$
\int_B f\in |B|\,[f]_B.
$$

这一步已经支付胞内变化，不是把采样值当积分，也不需要另假设某阶导数或遗漏 Peano/舍入费用。范围可能较宽，那是实际费用尚不够紧，不是允许省域的理由。

所有成功角块先原子写为 immutable 块并登记 whole source、point、model、原 journal/stream 和准确域身份。完整新总矩只有在所有全角块、完整选支以及上层末次字节重核都成立后才非 null。600秒只是 between-complete-blocks 的调度预算；不会把中间未完成 block 记成成功，也不会以预算耗尽给负科学结论。恢复时每个已完成块全读、全核；已完成和未完成域都留在报告中。

## 5. 一次完整流式读取的12个通道

上半 meridian 采用与源约定一致的参数取向

$$
N=F_\phi\times F_s.
$$

无需单位化 N，也不假设 s 是物理弧长。完整通量通道是

$$
V=\frac13\int F\cdot N,\qquad
m_i=\frac14\int F_i(F\cdot N),\qquad
Q_{ij}=\frac15\int F_iF_j(F\cdot N).
$$

另独立保留

$$
\operatorname{Re}A_2=\frac15\int(F_x^2-F_y^2)(F\cdot N),
\qquad
\operatorname{Im}A_2=\frac25\int F_xF_y(F\cdot N).
$$

因此始终输出 V、mx、my、mz、Qxx、Qxy、Qxz、Qyy、Qyz、Qzz、A2real、A2imag 全12通道。Qxy 的对称两位置在 Frobenius 范数中付2因子，未删混合矩，也没有把 Q 的原始二阶矩误当平移不变量。

这些通道在当前阶段首先是准确参数通量。只有同一个完整闭像、向外取向和有界侧责任已付，才可按 R716 式(19)称为实际体积矩。报告明确区分这两层；源不会通过写一个 `embedded=true` 标签绕过它。

## 6. 下反射、core 接缝及平帽贡献

定义下半为

$$
D_z=\operatorname{diag}(1,1,-1),\qquad F^-=D_zF^+.
$$

其与完整源一致的取向是 $F_s^-\times F_\phi^-=D_z(F_\phi^+\times F_s^+)$。所以 F·N 在反射下不变，关于 z 为奇的 mz、Qxz、Qyz 两半贡献准确相消，其他通道准确加倍。这是明写的整个下半定义及积分恒等式，不是从某几个节点反射相近推论。仍不据此声称整像嵌入、无自交或全局外向。

完整原 source 的端点关系保留为：

- core：$F=\Gamma,\ F_s=e_z,\ F_{ss}$ 水平，$F_{s\phi}=0$；
- cap：$F=R e_r(\theta_0)+He_z,\ F_s=-e_r(\theta_0),\ F_{ss}=0$；
- cap：$F_\phi=R\rho_0 e_t,\ F_{s\phi}=-\rho_0e_t$；
- 两端 hp、hpp 准确为零，内部完整 raw closure lift 不删。

这些是与原完整布局、law 和准确支撑兼容的 gluing 公式。把它们用于一个实际闭嵌入 C2 边界，还需要完整同支上半场以及整体像/定向证明，报告不把 source 公式单独提升为已通过的几何证书。

两轴心平圆帽在 z=±H，半径使用同一真实 R。完整解析角积分给 A2=0；同时完整平帽体积通量与对角二阶矩为

$$
V_{\rm caps}=\frac{2\pi R^2H}{3},\quad
Q_{xx,\rm caps}=Q_{yy,\rm caps}=\frac{\pi HR^4}{10},\quad
Q_{zz,\rm caps}=\frac{2\pi H^3R^2}{5}.
$$

其余一阶/混合通道为零。两个帽都实际加入，没有把未积分活动尾与平帽 A2 为零混为一谈。H 允许保留原真实符号；如果正总 V 尚未由完整包围与零分开，中心化除法明确不可用，不强行归一化或取绝对值。

## 7. 真正的同支周期与半转检验

原准确 producer 对相邻全角胞、0/2pi 接口及每个原 literal 角的同支关联，采用“真根内盒完整包含于另一局部唯一性盒”的有向包含。这里只重新读这些完整 journal 并逐32阶段复核；两个盒相交不算通过，也不声称整个控制球唯一。

半转另付，不能仅凭偶/奇 Fourier 槽的形式就声称所选隐式根半转协变。对本完整 source，

$$
P=\operatorname{diag}(-1,-1,1),\qquad D=P\oplus P.
$$

准确参考、Omega、core/cap 依 P 协变；六控制系数满足

$$
B_6(\phi+\pi)D=P B_6(\phi),\qquad
f(\phi+\pi,Du)=P f(\phi,u).
$$

于是完整控制 frame 变为 $A'=PAD$，normal 更新 $u+B^T\eta$ 在 $\eta'=P\eta$ 下协变。这个 proper 旋转不引入角导数负号。一二角 jet 同 P/D 规则变换；三维无穷范数根盒与六维 Euclidean 控制球都由 signed map 保持。

在已经通过全圈周期关联后，按准确 $\phi/\pi$ 区间配对 i 与 i+N/2。每一对的每个原32 stage 都检查 P 作用后的准确 eta0 内盒是否包含于另一方局部唯一性 cube，或反方向包含；按相同前一 stage 的支逐层归纳。整个配对实际通过才将 `half_turn_signed_root_branch_covariance_proved` 置 true。没有额外调用根算法或改工作候选。

偶数 N 是此明确配对实现的结构条件；若另一完整计划使用奇数 N，只将这一特定半转验证标成未付，仍保所有胞和一般12矩公式，不删域、不擅改科学分辨率。半转失败亦不等于场不可行。此前函数恒等式由独立符号审阅确认；真正包含不预计算，必须来自未来真实准确根盒。

## 8. 不对称 p4 帽与一般三相重心矩

当前固定 p4 配方完全沿用 R661/R716：a=3/20、h=1/1000、四个半径1/25、9/200、1/20、11/200；三个上帽中心 a、ia、−a，一个下帽中心0，符号+,+,+,−。没有为套用对称公式重选帽。

实现原 R716 式(10)–(18)的全部质量、一阶矩、水平迹、xz/yz 混合矩与 zz 矩。各帽的面积支撑和高度检查不替代其外部法向管证明；仍须同一未标记完整闭族的 tube>h 或独立完整的不交证据。不能因凸起位于 z=±H 外侧就忽略远处回折活动面。

一般消费者始终先按 R716 式(2)计算

$$
m_\alpha=R_\alpha m_\Omega+m_B,\qquad
J_\alpha=R_\alpha Q_\Omega R_\alpha^T+Q_B-\frac{m_\alpha m_\alpha^T}{V_\Omega+V_B}.
$$

它准确保留三相 $\alpha=0,\pi/4,\pi/2$，即原物理 t=0、1/2、1；$\pi/4$ 的旋转系数用有理向外 sqrt2/2 包围。全部一阶和混合矩参与，未假设原不对称固定 B 半转对称。此一般代数本来不需要 Omega 半转，所以半转未付仍可保留它，待闭实体/装配条件齐后使用。

只有实际全32stage 半转关联通过，才进一步启用 R716 简式

$$
B_{\rm eff}=B_2-\frac{b_1^2}{V},\qquad
z=A_2\overline{B_{\rm eff}},
$$

及两个相位差。固定 p4 的准确系数是

$$
b_1=a\mu_0(-36+81i),\quad B_2=83a^2\mu_0,\quad
\mu_0=\frac{\pi}{200000000},
$$

$$
B_{\rm eff}=a^2\mu_0\left[83+\frac{\mu_0}{V}(5265+5832i)\right].
$$

一般复乘法与这个解析表达式的包围取交，结构性正实下界保留。若半转未付，相关相位简式的“已应用”字段写 null，数值代数表达式单独标为未应用；不让一个非零候选数被误读为实际相位差。

若完整总 V 仍包含零，消费者保留已完成积分但 `complete=false`、中心化代数 unavailable。若 A2 的真实包围包含零，则仅是这个充分见证未支付，不能改用某截面矩、旧6077系数、非圆 core 或假设值，也不能从见证未分离推全等或不存在。

## 9. 面积、直径与 R625 可选条件界

同一 whole-cell N 盒也积累完整上半参数面积上界；加下半和平帽得到未标记整面参数面积上界。标记 p4 图的 slope 可用 $2h/b_i$ 上界，因此在扣除原底盘后，额外面积不超过

$$
\sum_i\pi b_i^2\left(\sqrt{1+(2h/b_i)^2}-1\right).
$$

这个 slope 界来自完整 p4 径向导数的最大值，保守且不需要局部采样。所有平方根向外求值。

同场全域位置范数上界和真实 R,H 的平帽范数给出旋转不变的全相位位置球；再付标记高度 h 得 D* 上界。这个“全相位”用语明确以原 R248 完整物理相位装配成立为条件，不仅靠把一张参数面形式旋转就宣告题目族已成立。

可选 `--conditional-reach-lower` 只接受明确正有理假设。它不冒作一个实际 reach 文件或证书。给出后，源按 R625 原公式和 R716 原式(21)计算条件性商距离下界；默认参数根本不填写这个假设。报告的 unconditional_noncongruence_certificate、embedded/outward/tube/physical-phase 责任始终 false，直到另有完整真实证据，而不是由这一选项改 true。

这个区分同时允许已经完成的完整矩作为后续证书的实质输入保存，不因几何责任尚未齐而丢掉数据；也避免由一块表面或一个有限点读数越级成为闭面非全等结论。

## 10. 舍入、恢复与实际费用责任

所有数值盒端点用 canonical Fraction 字串。加、乘、除、平方与 sqrt 每一步向外舍入到声明的 dyadic precision；分母跨零即拒除法。sqrt 用整数平方根及准确有理比较决定上端进位，不假设 binary64 sqrt 自动向外。二次幂对跨零盒显式使用非负最小值，避免普通区间乘法虚出负平方。

原真实 point/根中心的 binary64 词仅作为准确输入字；从 hex 读回后核 canonical hex、finite 和全数组身份。不会对数学 S/phi/原尾取工作 float 替代。

恢复读取完整 immutable block；不是重跑科学 solver，也不是在节点 cache 中猜未保存的物理字。所有 lower/cap、marker、重心代数从同一完整绑定的区间重新算回。最终消费者再读所有 block/journal/source，对同一完整总和、domain coverage、branch 和半转字段逐一比对。没有新增 F、J、J*、工作 root 或准确 field oracle 调用。

完整原始流、逐角32stage包含、全12矩盒、中心矩矩阵、参考证明和当前 point 数组只在 runner。公开 summary 只选完整来源 SHA、计数、complete/pending状态及所需的标量上下界，不将矩阵或大坐标数组编码成字符串转存。

## 11. 完整参数计划与尚未完成项

约定依赖顺序：原 v2 full science → 原 v2 full pure → 完整 recorded-reference fees → 完整 accurate normal32/fullcircle fees → 本次完整矩 producer → 本次完整中心矩 consumer。既有 science 和 fees 参数不改；这不是把准确费用当作优化前门。

本次 producer 保留整个原上游角计划，默认 maximum-angle-blocks=0（全部），time budget=600秒，仅在完整角块之间结束。consumer 不传 conditional tau，输出到与所有输入严格分离的新目录。完整 argv、全输出路径和全部 scalar summary 叶在配套 ready 中逐项给出；不存在尚未取得的 report/snapshot SHA 占位假值。

本次完整参数包可公开和接在原正常费用之后。是否在同 job 准入和返回，以实际控制器及真实 child 为准；排队不等于已经执行，partial不等于证书，终态没有返回不等于零值。

当前仍未支付或未实际返回的项目包括：首完整真实物理场、完整准确 normal/六jet域流、实际矩值、同一闭像向外嵌入/有界侧、p4外管不交、原全时物理相位装配、reach/全域相对度量、实际同问题频率和mesh精化以及其它 README 完成标准。这里的接口不删除任何一项。

## 12. 本次完整交付身份

下表记录本次准确采用的三件完整源和完整参数，不把早期未采用候选冒作本版。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `r716_closed_surface_moment_arithmetic.py` | 17397 | `f79c69edc4686148ca0a1418a498ce0154492a842561542c6bbdb8d810563e9a` |
| `run09_complete_closed_surface_moment_integrals.py` | 57152 | `19e4ab31976615b12d002a6ef26c15973859fc4268134b5fd61676206e9c11b4` |
| `run09_r716_centred_volume_moment.py` | 20526 | `357613469917691810a4e76f79c4534867baf188ccd47e1b83ede0acffff1b0a` |
| `run09-complete-R716-closed-flux-centred-moments-ready.json` | 11553 | `03c273e754aca447d2f9612fcaee98b121b68ebc2754217ec5136ef2cfc7220b` |

完整参数的两个对象共7602字节（紧凑JSON），argv分别10和6字，标量选择器分别33和47项。未提供条件 reach 值；完整积分与完整中心化结果的未来 SHA 均为实际运行后才记录。原约定准确 normal 终版源为 `f5ecc7fb67d4c34d5c52cba16ba0cee94b8fb5872f14c67123a190b32c6450c1`，径向终版为 `0587d88cd46ea8379b7e250872ed1b34deb0452ab7d61ae230c284bac126d42b`。

## 13. root 全文接入及独立符号复核

Astra-larger-e4e2a2bf-20261126于2026-11-27 08:47 UTC逐段读完三件完整运行源、完整ready和本说明，五件整字节数/SHA与交付一致。四个完整normal外源均与已刊852bfb85的完整源码逐SHA一致；两step全部10/6个argv均在真实CLI声明内，33/47个scalar selectors与原ready逐值保留。原队列四步逐值不变，完整两个新对象直接排在normal费之后。没有未来输入SHA、根盒或矩结果被补写。

construction已独立对照正式R716全文复核f79c完整算术：12通量的1/3、1/4、1/5系数、上下反射奇项、两平盘、四p4全部一二阶混合矩、5h/18等高度系数、一般三相旋转与总重心扣项，以及Beff和两phase差符号均无所读阻断。该审查为符号/源码审查，没有Fraction算例、AST、科学导入或运行；不替完整准确输入、闭嵌入/外向/标记外管证明。

原始交付note为19731B / `51e421a71ae0cc8bce4e3e6e665ace9df622d804caf664a78e27f15732885768` / Git blob `e9fb3403c2d274f31d2fea2c60fbb06685471e12`。本次只增完整接入记录，运行体与ready字节不改。云核规则commit `91e6cc8826b8d6b091f054674c8b9980541da24e`，双README整SHA581402/3c1c无变；API不冒真实pull。08终态与09未返场/全部历史责任保留。
