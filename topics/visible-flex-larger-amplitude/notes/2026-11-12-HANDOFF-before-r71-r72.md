# 交接：闭曲面握持变化量至少0.2D

## 状态、授权与发布

进行中：visible-larger-20261112。**未满足完成标准，继续研究，不在中间报告停止。** 两README最近确认提交`bc4fa669294f1d742852344ed72feee45b040022`。每次pull立刻比较两README，只读变化；至少每小时一次。2026-11-12 16:14:49 UTC的pull发现根README新差异，已实施：**非快进拒绝立即git pull --rebase再推并循环成功；只写本题log，根LOG停写且不归档。** 根README授权直接main、可自行修共享设施；不强推、不改写他人提交、凭据不落盘。完整证明直接登记（第13条），无附加审批门。文件<5MB、>1MB压缩、Markdown<100KB、HANDOFF<10KB；不传PDF/逐页渲染。

目标：闭连通C²嵌入等距族，共同g；固定H有内点且diam(H)≥.2D、held≥.2D、δE>0含反射；全t reach≥.03D。D=diam F0(M)，H允许不连通。固定g/物理参数/t区间真加密至机器或求解容差，给数个完整网格。固定taper、开放片、小幅闭图不算完成；达到后继续增幅。

工作区`/workspace/scratch/c0de65fac774/math-research-recovered`；相邻math-research-publish专用于pull/push，计算树不rebase。**最近已发布main477f34c8b29f30659d6b2f3a2c53e95e5e0f7cfa**，源29ed8692863dfba4d2309e624a5256f4cfac42e4，81783正式0、98件，包括完整outer11/10 Taylor和576cache/seed；准确临时cache ref已删。此前main69ea含R63–66及完整组合暖场等。源537d06e3bd9174d6797e1e600839541df8fea5a7的176件已完整cache到7e3cfdfe177e90c6b30bdd9ca042fb6b82e59692，46904仍循环普通main竞争；不把cache当main发布。R70正文/seg7随后新增待下一批。

16:14仅重建自有干净publisher，旧.git3.067GB回收；active无alternate依赖、科研数据未动、必要main/read/base元数据保全。fresh depth1/partial/sparse；55813退出50是README差异门，已应用新规则。新publish_topic_checkpoint_rebase.py实际pull --rebase后重建本题树，每次pull即时README门；topic上游变化须先合并。旧cached入口只留历史。

## 固定源与资源规范

source869436630c99aa5a68afb55bd8877c826034d117，91件866846B，manifest7de25376ab0ec102…；相邻visible-flex-source由prepare-source-dependencies.py恢复，73900正式0全hash同。bash/login=false，BLAS单线程，Flint为相邻research-venv/bin/python。第二次执行器丢失后重做记录在notes/environment-interruption-20261112-second.md。

大数值只一条；exact/tail共享一条小Arb流。只信self/wait4，不以跨exec /proc空读数或signal9猜OOM。旧未知终态保持未知。61107这次明确ENOSPC，不能反推此前−9；86778已在空间恢复后仍−9，原因未知。新构造异常guard关闭并wait自己的worker，正常数学路径不改。MJS全树参与stage缓存身份，当前冻结；Python/文稿可改，改MJS须另建完整身份/等价证据。

## 强数值分支与下一真实设计

accepted基准`root-q095-design-fixed-actual-m24-tol7-frozen-r1`，主包1d7f6f0ab3b7b51b…，完整raw/物理五次/尾已推。9377正式0，M24/N768/tol7、2004点3轮；RMS9.97630e−8、trueBC3.02005e−14、tail5.6363e−10。actual c2=.09499996014428179与gauge=.09不同。全内部metric8.77614e−8但Darboux3.13335e−4，C²与同g真精化仍欠；该g首解不和旧q085/M20混报收敛。接受设计后执行真正27→24冻结，再同g优先M28；旧身份27791已过但实际冻结未跑。

q105原4388/disk98541均正式137/signal9，原因未知、非解；最后0003 colloc .01392040/BC4.18963e−5，无新H审计。完整失败/六matvec证据已推；不凭巨大raw高模步改Jac，不借旧H0给不同H。

下一真实设计q096从accepted q095全raw/5响应构造：target=(.09599996014428179,−.006718093057120565,−.0004136733380408847)，vu−.0002、descendingK−.0025，原M24/N768/tol7/physical门保持。这是新g设计，不是同g精化。21118准确全24H逐位同root warm loader，H2=−2.386055074591057e−5、Float64LE SHA c486a7cac208969a2c7e4febd7961098a9e075e641ebee2596876c7179d8f4f7。

完整576段缓存92668正式0/worker0，261.086秒/380032KiB：1,384,155数逐位同，第二遍576hit/0miss，原残差/J/mean/minA/D全部保留。初猜norm507.11093是未解状态。577×48 exact seed f1e7d96a…已推；cache identity66e22f1f…包含真实后端、全MJS和Node/V8/架构，4分档共10.835MB/577件逐字恢复核过，执行清单71f73efb…已推。原M24/N512/depth8/steps12/parts8/tol2e−9、fullJac/audit不删。

67663使用同seed/cache首次576全hit、3.15秒完成校正，首非Jac线搜索中worker−9，正式1/98.845秒/383616KiB，无新接受步，完整iterate0保留。61107仅heap128还未发求解request即写adapter ENOSPC，Node终态未知。构造清理guard7门真后86778继续同heap128，正式1/Node−9，76.989秒/241856KiB，ready前结束、无新请求。新失败与guard稳定清单保留。25305现用young-space4（V8总heap320→140MiB，非RSS保证），MJS/key/g/seed不变；151秒ready，576全hit与原norm/chartCondition重现，首校正后进入原线搜索，尚无accepted尾。真尾成功直接接已备fresh资源/fixedS/disk/域观察actual prefix，changed-H真求。

## 严格内头、共同cut与当前外接口

R1–R70见results.md，完整证明直接登记。R58固定R39 q085/M20实g、node12全20Q/余26零，12..224+R18无限尾全部641门真，Lip<.969、总修正<4.477e−15。精确31/32目标false。不是q095/q096新H、q105或外0..11证书。

R61全641×46正列29486门已付：参数依赖l1盒，canonical Q2=2^-193、Q92=2^-291；H=b⁴Q无额外w，不能把逐列最大轴当积盒。R63直接源功能保213cell/完整mean/逆余项，m2 Wσ1≤1.000518e−50、m4≤6.183529e−49。单cut且cuff高度自由时只选一个mean常数，纯相位族同一常数；一般a族固定H另核。无限振荡累积在正cuff rc=.05，非r=0；trueRout=.300000000000007159…，不换binary.3、不重标g。

R65真实四cell局部Taylor18822正式0，36段7533面板/16根括号，m2/m4 slope半宽<1.678e−26/<3.018e−24，真无限尾Wronskian误差<7.178e−52/<5.595e−61。共享符号48737给m2候选真K差−3.4653602e−44±5.51e−51，严格非零，不能继续当区间噪声。

R67实际outer11/10 Taylor34414正式0/110.074秒/30824KiB，18段3478面板+8根括号、11门真；globalµ*=µ11无重复ρ，所有旧真流相交、S0排零。node10 m2/m4 S0约2.13356e11/8.56246e13。单cut m2项约3198参数轴，微小dyadic斜率重心化后<.000299轴，但必须保补偿forcing。整段候选线性forcing合并准确是q−Q_R/S0，m2在node11/10仍约1.21186e11/2.39821e11轴；cell11完整N现由R70加上，非不存在性。内部Q是可校正候选节点，不是额外固定题目边界。R67清单600e2832…，不能冒称全46/全外Schur。

96084原cell11 signed N正式0/55.555秒/34632KiB，5545面板保原candidate/mean/J聚合逐字同、7门真，九gz约5.44MB，清单3365b543…。有限二次N2/N4及完整mean/逆余项未删。R70的94339真实adjoint正式0/235.948秒/31116KiB，5609 Taylor子步和4根括号全保，m2源绝对界<1.242929e−56，完整中心差[9.6530184,9.6530185]e−48。正文清单45cd090d…；39026正做双侧内部node11重心化并单付mean总积分，node10完整线性边界残差不因此消失。

R68完整最优固定frame定理已登记；37378原10793面板正式0/26.090秒/30912KiB，Γ由.1910589182降到.0801047061，真gap=.128810830748过门，保所有跳变和b<1首尾范数。70557完整连续位置有理后处理正式0/49.793秒/12928KiB，cut到任意x D+<189.460745，回cut D−<205.967303；任意对向外/内D<281.281503/288.945155。仅齐次背景，较大前因子明确保留；非有源Green/高频边值逆。

## 外候选改善与全局几何缺口

R60 outer11及cell10完整正moment/mean/J已付；R64一般完整mean根不强求1/32小球，保真实M_c和全部逆分母。R66 cell0末段物理r表示、其余原x表示，J/N不得混单位；Darboux是共同物理量。seg3真实八子段30285正式0/104.732秒/38072KiB，4211面板，段缺陷5032.166→.193210604，旧最坏点新上界<.253倍旧严格下界。34268复现其余7段、5299全覆盖，原最大转到seg5：554.245695。seg5的63344正式0，1124面板使缺陷降至4.023376336；seg7的21985正式0/32.079秒/37256KiB，1686面板使71.023→2.378359。84262完整组装正式0，同g/H/原两jet7378面板，最大仍seg5的4.023376336。93119定位最坏叶r_x跨度148.41，同候选分半完整J/mean界≤.025970868；仅该叶结论。下一按r_x相对跨度重包全段。

R69完整mean主符号判别式−4s ell D/L²，正支D/L上类型取决于ell；点态剪切还须支付其x/θ导数与解析权交换，不能免费套背景strip。完整条件证明不代实际非线性传播门。

root五控制几何已完整保存：共同3178×384保全部raw/knots/已知峰，基准κ8.44332482582、2r3.90094646007；全部11场与全6101760行LP已推。组合23587正式0/106.431秒/133132KiB，κ8.38561523665、2r3.90874685180，乘积改善.4849%，但κ比线性cap高.000211923，非严格LP/actual解/真实D或reach。全24核心真d=2Σodd c2j：.18913039378→.19112857192；暖场d/(有限2r)仅诊断，不是held/D。

R14弱四Gauss标记排除含反射E(3)，R24有严格余量时保reach；R37与R62给连续位置/法向球和全相位Sturm工具。当前仍无整闭面、连续K/全覆盖、held≥.2D或全时reach证书。下一actual q096成功后做完整几何与真实固定问题加密；任何时长不是停下理由。详细历史与完整规范见本次及先前HANDOFF归档，所有primary按各stable manifest保全。
