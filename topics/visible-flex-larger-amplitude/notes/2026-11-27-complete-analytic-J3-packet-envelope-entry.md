# 完整解析 working J3、不可变根记录与同目标全变量迁移入口

日期：2026-11-27。状态：完整独立源码、参数与来源闭包；本说明不报告新的科学执行、根成功、几何证书或加速比。根负责唯一普通提交与发布。本入口不改已排的 95559/f382，也不要求先运行一个未执行的 plain 变体。

## 1. 本次实际交付

本包有十三个完整运行源，分成六个局部求导／normal 下层与七个完整入口／记录／纯归因上层。另有两个完整标准库再生器，精确保留原全文、每一处替换、输出字节数和 SHA-256；两套 ready 各含完整科学 step 与完整纯读 step。

下层来自已刊 d5da 完整 normal、6a803 完整 base，以及 ba3d／375059／955d 三个完整缓存／角矩阵 helper。上层来自已刊提交 35e4d40fd459bef32055684a1048323f96de4a33 的 95559、1bcce、182a、104220、f382 全体。新 helper、normal、geometry、driver、launcher、reader 都有独立文件名与完整身份，没有把旧报告改标签。

两个 ready 都明确绑定 run08 已真实返回的 7c 固定参考输入。它们不是 run09 的输入声明。run09 的完整 warm／参考／chart／模型尚须实际读取后单独闭合；不能仅因参数相同就搬用 105289 的固定身份或声称同一个 g。

## 2. 局部求导的精确范围

原三维 stage 方程及其原真实重读保持。对某个角和某个 stage，只对当前局部增量 eta 求偏导，previous 控制、previous frame、当前外变量、原零控制 target、参考校准、core、cap、积分节点、权重、S 和 tau 在这个偏导里固定。当前六控制为

$$
u=u_-+A_-^{\mathsf T}\eta,\qquad w=\mathcal B u.
$$

对第 j 列，完整方向是

$$
e_j=\mathcal B A_-^{\mathsf T}e_j^{(3)}.
$$

其中 B 的前后三块仍是原全部 W 与 gamma；没有选三个物理控制代替原六个控制。原 endpoint、moment、core、cap 项不依赖局部 eta 的部分偏导为零，并不因此从全局外参数 J 或 J* 删除。

写 q=w·w、c=w×V、d=w×c，原 working 旋转值为

$$
T=V+A(q)c+B(q)d.
$$

其完整局部方向导数为

$$
D T[e]
=A(e\times V)
+B\{e\times c+w\times(e\times V)\}
+2(w\cdot e)\{A_qc+B_qd\}.
$$

每一列都经过原完整 _total，再除以同一个 S；不改变原 cell reshape、Gauss 权重、物理宽度、求和或末次 cumsum 的消费顺序。局部矩阵是全 batch 的 3×3，不裁列、行、角或 stage。

小 q 分支逐字沿原 working degree-12 Horner 的 binary64 系数定义，并在同一次倒序递推中计算导数。没有拿另一个独立舍入的 Az/Bz 系数表代替实际 value 多项式的导数。大 q 分支使用同一原三角函数表达式的导数；原切换位置与无效分支安全值不改。零附近使用多项式极限，不除零。完整公式及其代数证明在同包《complete-analytic-working-normal-stage-J3》全文。

这里证明的是所声明 working 分支表达式的精确代数导数身份。新乘法／叉乘／归约的浮点排列不承诺与原 AD 逐字相同，也没有向外包围真实导数或逆矩阵误差。原真实 stage 方程、域、控制球、残差、Armijo、回溯次数和最终 endpoint 重读都保留。

可选数值准备失败时，完整原三反向产品 AD 公式对相同当前输入整批重做；部分解析列不充完整解析矩阵。来源、模型或 shape 不一致仍直接拒绝。解析尝试、成功、失败、AD 回退、真实 stage 方程读数与时间分别记录。矩阵产生成功不代表根成功。

## 3. 全局链与物理六个 jet

新 normal 的 __init__、_stage_jacobian、metadata 三个方法改变；其余四十八个类方法与原 d5da 的 AST 相同。完整 _solve_stage、_run_chain、_finish_stage_jets、_get_roots、_implicit_jet_value、_normal_frame_jets、_corrected_jets 和物理 fields 方法保留。

尤其，外参数导数仍来自原全部 stage 的隐式图。previous frame 对全部上游变量的导数、原零控制 target 的全部外参数链、每角一二 jet、全部 32 段和全局 J/J* 都不从局部 eta 偏导中借用一个不完整替代。没有反传 Newton 迭代，也没有据近零残差删除 stage。

已有 C1 frame 复用、detached 同-call 矩阵复用、相邻 frame J6/J9 都使用新的完整独立 helper 副本；只更换严格来源／实际局部 J3 wrapper 的 AST 身份和诚实的策略说明。原数学正文及完整回退保留。角矩阵 helper 保留的是本次所选局部 J3，不能再写成“原 AD J3 没变”。

参考中心化仍使用固定原 base.initial 的完整同 Torch 路径。raw quadrature defect 与 centered root residual 各有自己的三角 jet 记录。完整 h、h'、h'' lift 都进入 F、Fs、Fss、Fphi、Fsphi、Fphiphi。working 径向 Gram 不宣称恒等于一。R713／均值 producer／连续 normal-chain 费用尚未因这一数值入口自动支付；本入口不继承连续根、几何或全部 phase 的证书。

## 4. 不可变真实根记录

本入口使用 solver 完整修订的 immutable_analytic_normal_root_packets_v2。它显式登记 04f1 normal、6a803 base、8a63 adjacent、4c3 calibration 及 64b 局部求导对象。所有实际方法 codefile、完整 model、SOURCE_PINS 与计数器均绑定。

两处 hook 是原 QP 计数和时间结算之后、以及每次 save_report。它们只复制已经存在的数据：完整当前点、实际积分 query 字、已有角根、32 段各自已经保存的 eta/frame/controls/J3，以及确实已有的 J6/J9、order 与 provenance。order 1 不被改成计算过 order 2，未存的矩阵生产策略不由另一次 last_call 补造。已有 reference calibration 数组也按完整身份保存。

已修正实际接口：witnesses 和 radius_witnesses 是带 cell/u/phi 的字典；记录器精确读取命名字段，保留原字典、protected 和 typed 身份，不把它们当三元位置列表。不重新归一化角，不清空历史。

outer x 的 SHA 与当前 cache point 的 SHA 分列。QP 中最后一次缓存可能不属于被接受的 outer 点，记录器不把二者强行认同。每个 capture 有自己的 ordinal、标签和不可变 snapshot；失败记录不挪用上一成功 snapshot。记录器前后核全部实际 field/root/J/normal/frame/stage/adjacent/analytic 计数，不允许增加科学调用。

原数值解法仍可能失败；文件 I/O 失败有独立未完成记录，来源错误直接失败。完整记录不是精确分支认证，不是连续四／六 jet 误差包围，也不是过去所有未保存 Newton 状态的恢复。

## 5. 新鲜输入、同源续接和严格旧末点迁移

新鲜路径以显式 independent flag 从完整冻结参考点开始，当前 7c scalar／chart／reference／carrier／domain／Q／seed 模型均按现有 105289／4d92 全部真实输入读取。旧 dc5 仅承担已定义的完整历史材料地址来源，不把它改称新 target。

同源 restart 仍要求本新完整 driver、完整模型、当前 norm／输入／checkpoint 相同；不接受 95559 checkpoint 作为这种同源文件。

新的显式前驱注册表另外支持完整 cc0a/104e/c79 家族及完整 95559/f382/4d92 家族。先由各自原纯 reader 完整读取同一份 report 字节，核 terminal 范围、真实 input 与 carrier、全 model 与原内存策略。不同 memory 家族不能混作同一 loader。对于 95559，保留其完整独立 fixed-target origin 与所有尚未读取的 peer 责任。

模型对照没有忽略完整 reference 或 seed。新旧 C1、stage、adjacent、analytic 策略分别通过各自完整源码重新构造；只剥除这些已明确另核的来源／数值策略字段及 calibration 的 source/endpoint source 两字段，再比较剩余完整对象。base、g、完整固定 chart、准确 scalar 定义、原 seed、Q、gamma、bubble、mesh、partition、全部自由变量和工作积分规则必须逐项相等。来源变化后的浮点场逐字相等不声明。

显式 prior-final 路径要求实际完整 final report、真实 final NPZ 与其原 reader 的 final 验证。完整十三个 NPZ member 都要存在且不多别名；omega_jets、core、Hcap、mesh、fixed_parent_core 全数组 shape／dtype／finite／字节及所有模型字段完整检查。重组所有原自由变量，再 unpack 回全部数组逐字复核，且须等于原完整 final 几何和 metadata 的同一点。不会重新选参考、移交旧根缓存、旧 Phi、旧可行性或旧证书。新源首个字段读数在该完整新点重新计算。

所有实际父报告都再由原完整 walker 读取；全 P0、old/current G、已知 protected、uncapped family/location/partner/branch/sign 与原发现来源保留。typed 初始并集成为永久前缀。原未来报告不存在时严格拒绝，而不是补空数组。

## 6. 未返回的 peer 与当前已知终态

新 CLI 有两组精确对应参数：

- --pending-parallel-envelope-run RUN/ATTEMPT；
- --pending-parallel-envelope-source RUN/ATTEMPT=完整 driver SHA。

每个 run 必须且仅能有一个声明来源，来源须在完整支持的 parent family 中。报告保存完整映射。这个 pending 指尚未支付的全报告／地址／typed 责任，不表示 workflow 一定还活着。

在本包准备结束时，根已经实际确认 run07 completed/cancelled，但最后 compact 仅返回 1–3，原 cc0a 的 step4 没有科学结果或 typed 状态返回。两个 ready 明确记录该状态，不把取消等同于空地址、无计算或无历史。run08 95559 的完整末场在本包未读取；其 SHA 不预填。run09 已启动的 bootstrap 同样没有被冒作 run08 7c 输入。

## 7. 全参数与两个 ready

独立初点 ready 的科学 argv 145 词，纯 reader 7 词。它逐项保持原 ready 的所有科学数值；新增的六词只是未知 peer 的明确来源和额外 run 声明，输出与源码地址为新独立文件。

条件 prior-final ready 的科学 argv 144 词，纯 reader 7 词。它移除 independent/pending CLI，加入完整父 report、同一 report manifest 和显式 final 两文件。未来 report/final/model SHA 均为 null。只有实际完整父返回后才能按这个条件使用；新源自行核全部真实字节，不以本说明代替实际文件。

两套 ready 都保原科学 240 个和纯读 224 个 selector，逐键同值，另增加实际解析与记录器 scalar 计数。总计为 281／265 个 selector，没有字典或数组被选成 controller scalar。初失败时 pure step 的 parent 仍是真实 reference，避免没有 final 文件遮蔽失败归因。只清理新 rows-* 缓存，不请求删除固定参考或 immutable packet 数据。

共有原 N2048、J923、M160、原 mesh、integration order8、同一两 bubble 与 gamma、原32段、同控制半径／残差／回溯、原全192前缀／幅度／全E工作规则、完整 Phase I 与原 QP。新参数没有给局部 J3 增加人为测试门或改变题目完成标准。

## 8. 已实际执行的纯源码工作

下层完整六源的再生器与上层完整七源再生器均已经在恢复环境中实际执行，只处理文本、哈希、AST 与 compile。没有导入 NumPy、Torch 或生成的科学模块，没有运行 F、J、积分、根或任何数值 fixture。

完整十三体各自小于 100000B；最大是完整 pure reader 99527B。全部四十八个 runtime role 的实际完整文件 SHA 都已逐一核对。上层原科学 suffix 在移去恰好两处 record-only hook 后与原 95559 的 18958B 后缀逐字相同；其 SHA 为 3a34eeb13a52579aacafb1598c52a94a42f8db2cfab03a3fef0d64c2b88937d5。geometry 只有 constructor 的严格 source/instance guard 改动，其完整 scan、原行前缀及后续所有方法不变。

launcher/driver 的 parse AST 在去除原两个 launcher 专有选项后完全相同。参数文本检查保全部原数字词与原464 selector，新增旗标均有真实源码声明。reader 原二十二个完整函数 AST 保持，六个绑定函数的变动与一个新增小 binder 只处理新来源／policy／metadata，不删原 scientific 读数检查。

完整输出 SHA 与预期 source path 全保两个完整再生器及两套 ready 的完整来源表；交付 manifest 仅保scratch用于逐项复核，不另复制派生清单进Git。原草稿 blob 保留历史，只有 manifest 中列出的终版参加该入口。科学实际执行、效果、根可解性和耗时均等待 Actions 的真实返回。

## 9. 后继接口边界

本包只为当前明确的 M160、N2048、6a803 base／04f1 normal 完成来源闭包。M320 零嵌入、N4096 观察细化以及新参考输入应各自完整派生实际 base/helper/model/source 链；不能只放宽本 helper 的来源 guard。本包数学公式可复用，但来源身份、完整历史和实际子空间／积分语义需要相应真实体。

本包不改变题目 g、幅度、全 t 嵌入／reach 或精化完成标准。全域连续费用、精确根分支、非全等见证与全部 phase 证据仍按已登记 R703/R707/R713/R715 及同场合同支付，不能由一次局部矩阵加速或完整缓存记录替代。

## 10. root实际再生与当前运行

root在完整公开checkout再次实际执行两个标准库再生器：六下层和七上层全部exit0，逐字复现全部13体，并独立核48个实际完整runtime source角色SHA。全patch/guard AST及原3a34科学后缀核对保持；无科学module import或数值fixture。根记录器v2的完整独立四体再生也已实际exit0，所有原物理源SHA逐项相同；该复核不构成新的数值返回。

09已真实启动run45943410994/1、job140322567209，初始公开提交0e84fd89a4248e1bd196248334d4959dd0a98355；API实际确认依赖安装success、研究step5 in_progress。这里只记录真实运行元数据。该run的完整目标仍须由实际warm/reference返回绑定；这两套7c ready没有被写成其当前已准入求解。
