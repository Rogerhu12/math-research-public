# J1845 当前场的完整准确 normal 六 jet 与连续几何费用

日期：2026-11-27。状态：完整独立源码及参数交付，尚无本包的科学执行结果。本文不登记新定理，不修改活跃 J1845 求解源或队列。

## 1. 完成的工作及准确对象

这组七个完整 Python 运行体把已刊全圆、全 32 阶段 normal 根与物理六 jet 费用算法接到真实 J1845 径向精化族。它保留冻结参考的 J923 节点、固定 RN-even Fejér 图、完整标量度量、参考 seed、18 个 Q 字、gamma 支撑和原共同 normal 分割。当前 omega 的 Hermite 域则使用全部 J1845 准确节点与全部当前自由量。两种径向域在输入、积分计划、每个叶片及下游读数器中独立记录和复核。

这一改动不能只替换 J 常量。先前 N/M 费用族的 AccurateFieldGeometry.make_plan 和 ExactOmegaBounds.prepare_cell 都以冻结的 context.nodes 为 omega 单元边界；那适用于参考 J923 与当前 J923 相同的族。J1845 当前场有 1844 个径向单元。继续用 922 个参考单元插值当前 omega，会遗漏当前中点 jet，并给出错误的准确单元宽度。因此本包真正改了当前 Hermite 域的生产和消费接口，同时保留原参考上下文。

全交付包括七个完整独立运行体（共 271,498 字节）、一份 78,166 字节的可逆文本再生器、两份完整 Actions 参数（共 25,103 字节）、本说明和完整交付总表。两份参数保留原数值预算及全部 36/48 个 summary selectors。

数学运算只在公开 Actions 中进行。这里实际做的是完整来源阅读、纯文本生成及正反向全字节比对，没有本机科学、Python 导入、AST、编译、数值例子或新 fixture。源码再生器是交付的复现途径，不是活跃求解或费用执行的新增前门。

## 2. 真实父来源与分开的身份

当前科学族与文本父体分别来自以下完整记录。

| 来源 | 字节 | SHA-256 | Git blob |
|---|---:|---|---|
| [J1845 完整源码及三种计划](../computations/fixed-fejer-J1845-complete-source-and-parameter-delivery.json) | 81920 | 9f121393761a2c5b93fc7124ed093caf6116283b512f5ce1379f5dfbe089a096 | 06ffe89220e5cbd3a26f0278f464c98002bde6c6 |
| [J1845 五个基础源](../computations/fixed-fejer-J1845-complete-base-source-delivery.json) | 10411 | 9a49dd2f26dc83b5ff70cc440cc30cf4b5d1cff92bcbd1a2270a204148677f97 | d1d98dbaed9e3fb74dcc02f492c0e1ae57ab9989 |
| [原 Fejér 完整准确费用](../computations/fixed-fejer-complete-normal-sixjet-geometry-fees-delivery.json) | 31084 | 6a8dc00ee02ce5399ae69859c7442c414c5dcd3553af68e3c8959eb21ac2f910 | fb27baa4b8c3e2fab489425990e94c65691a8c57 |
| [N13 完整费用后继](../computations/N13-base-bound-complete-accurate-fee-successor-delivery.json) | 31425 | 9319bf31d9d4dc209a1908d6bb37732ce55f4c4c7841b07e8f9b06488054ace7 | 5ea1af4f86b9881dfebccad6952dcb22598c12b9 |

J1845 整族正式发布是 f9d79e20c153170acab210858ce9564472b2cc1c；五基础发布是 729cf7b0e1fdef4b3d6ca8e4bff1ca7764124d5b。本包七源码的逐字文本父体取自 N13 后继；N13 的实际场、观察布局、旧失败和 source 身份均不迁为 J1845。原准确旋转、均值、角导、normal、六 jet、Gram/K/support 与 R717 同叶范数公式沿原完整费用链。

本包只接受 driver 97ae6ab8a2a19a07b134efc611b442d9e9113ca0b68c0cd322a45ec175d0f8fd 与完整 pure reader 4ea3b45ecce7e02c7e911a3bfd6f33110b422173cc4a377ae63845398b6a80a5。当前 normal 是 543ef57246c45f923133d121e414ca90cbba44e1ed9e4056b410f80ab5f2064f，base 是 78ded2682f5a42bc44a1939e9d814eec17254d1385dfe08a545d6aee109892ef，immutable packet 是 8a6b68a63c25a48a1bae2718161b0346b197012cedec4f43e7cc92b0c4cf5b77。

完整 whole-source registry 有 131 个角色，规范化映射 SHA-256 是 86c0f23b144cc9567f8809dd517f929b290da2a4f032f140e8ee94b2d44797e4。执行时既核整个映射，也逐一读取实际文件；原 Fejér 110 个完整路径/SHA 对继续作为子集核对。角色数本身不是验证依据。

固定 recipe identity 是 957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9，参考 model 是 ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac，完整 fixed target 是 50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319。三者分别代表 recipe、参考模型和完整目标，不替代真正当前点或真正 report 的身份。运行体从完整实际 binding 再读取并交叉核对这些对象；未来 report、point、snapshot 和费用输出 SHA 在参数中均为 null。

## 3. 冻结参考域与当前 Hermite 域

设冻结原准确径向节点为

$$
X_j(S)=a_j S+b_j,\qquad 0\le j\le922.
$$

每个 $(a_j,b_j)$ 来自完整 symbolic-node 定义，按有理数读取；$S$ 是同一固定标量模型的准确长度。当前细分定义为

$$
Y_{2j}=X_j,\qquad
Y_{2j+1}=\frac{X_j+X_{j+1}}2,\qquad 0\le j<922,
$$

并有 $Y_{1844}=X_{922}=S$。当前 layout 的完整 bisect_nodes 是精化来源；本包重读其完整定义并验证全部 1845 个 affine 对，不从工作浮点中点反推它们。

| 对象 | 冻结参考 | 当前精化场 |
|---|---:|---:|
| M | 160 | 160 |
| 完整角向 N | 2048 | 2048 |
| 径向节点 J | 923 | 1845 |
| 径向单元 | 922 | 1844 |
| 三个 SO(3) 通道数 | 161/161/160 | 161/161/160 |
| 合计角通道 | 482 | 482 |
| 完整自由量 | 原族 1,333,370 | 2,666,582 |
| 准确 scalar/chart/seed | 固定 | 同一个固定对象 |
| 当前 omega 三套径向 jet | 原族自己的数据 | 真正当前完整数据 |

当前 point 的核心自由系数、三通道全部 omega 值/一导/二导和 H 均保留。原三个固定 core 系数和原 omega 固定零槽遵守 source 定义；没有删变量、压成一个通道、减少 normal 阶段或只取低角阶。

工作 mesh 仍是实际 checkpoint/carrier 的全部 binary64 字。输入核整个 mesh 的 dtype、shape、finite、严格递增和摘要，并核全部 even 字精确等于原完整参考 mesh。工作中点和准确 $Y_{2j+1}$ 属不同层；前者是已绑定 producer 的真实输出，不等于后者没有舍入费。全部准确运算使用完整 affine 定义，不把 rounded old-u 当作准确查询。

准确固定度量保持

$$
g=ds^2+\bigl(a_{\rm deep}(s)\rho_0(\phi)\bigr)^2\,d\phi^2.
$$

J 的变化没有重新选择 chart、scalar、seed、参考 H0 或参考积分定义。当前 H 自由量如实读取；参考 seed 的 H0 仍由原冻结定义给出。

## 4. 真实报告与不可变 packet 的完整点绑定

family source 只声明 J1845 这一族，先识别整个 report schema 和实际 driver，再调用原完整 pure reader 与当前 radial source-and-report binder，不用旧 N/M reader 的返回值改名为 J 场。

ActualNormalPacketPoint 选择真正已记录、required angles 完整的 immutable snapshot，保其自己的 point 摘要及 source/model/target。每个实际 cached/required literal angle 的完整 packet 都读取，保持原顺序、实际阶数、全部32阶段和保存的矩阵字。它不由进度计数、运行时长、bare initial vector 或 report 顶层 current 值猜出完整场，也不宣称该 snapshot 必为 accepted final。

完整固定输入仍由 whole pinned fixed_fejer_reference_input_binding.py 读取，SHA-256 为 3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f。六个真实输入、maker/preparation/source records、完整 RN-even recipe 字、准确 scalar 定义和真正参考 model 一并重读。e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb 参考源及当前2218叶完整 metadata 保留；accuracy_reached=false 不升级为已付。旧2397历史载体不是当前准确 scalar。

径向额外 wrapper 的准确结构是：

~~~text
complete_radial_input_files
  schema
  definition_identity_sha256
  files
    current-symbolic-nodes.json
    complete-a-boxes.json
    complete-parent-address-transfer.json
    observation-definition.json
    complete-dyadic-observations.npz
  raw_stays_on_runner
  scientific_input_precision_status_not_upgraded
~~~

运行体核 files 中每份完整 record，同时保整个 wrapper；不能遍历 wrapper 的 schema 字串/布尔值来冒文件。原 reference positive rule、当前 native rule、旧历史与新细分地址的责任在完整 refinement/history 绑定内继续存在。工作 integration carrier 从同 snapshot 完整读取，核所有 current cells、Gauss u、权重、batch 排列及全 source。

新 _bind_current_radial_domain 形成以下持久合同：

~~~text
schema = complete-fixed-fejer-J1845-accurate-current-and-reference-radial-domain-v1
reference_J = 923
current_J = 1845
reference_cell_count = 922
current_cell_count = 1844
complete_reference_nodes
complete_current_nodes
complete_radial_layout_identity_sha256
reference_node_definition_identity_sha256
current_node_definition_identity_sha256
original_reference_mesh_sha256
actual_current_mesh_sha256
complete_actual_working_carrier
complete_actual_radial_input_files
~~~

对象明确 reference/mean 域未改、全部 current Hermite 胞、准确查询不用 rounded old-u，以及未提供 working 中点/求积字误差证。完整 canonical identity 进入 actual.binding、准确 geometry identity、normal request/binding、physical leaf reader 及连续 geometry binding。923/1845 数字是在完整定义与实际数组验证后的结论，不是缺失输入的补值。

## 5. 当前 omega 的准确插值

current_omega_bounds(actual, scalar) 加载整个 pinned a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6 连续核，继承其 ExactOmegaBounds。独立子类只覆盖 prepare_cell；原 polynomial、restricted Bernstein 及全部算术/角通道组合保完整原体。

对当前单元 $[Y_i,Y_{i+1}]$ 令 $h_i=Y_{i+1}-Y_i>0$。每模式原顺序的六个端点 jet 为

$$
\omega_i,\ \omega_{s,i},\ \omega_{ss,i},\
\omega_{i+1},\ \omega_{s,i+1},\ \omega_{ss,i+1}.
$$

在 $v=(s-Y_i)/h_i$ 上，原 quintic Hermite 使用 $h_i\omega_s$、$h_i^2\omega_{ss}$ 进入标准化系数，导数再除准确 $h_i$。这是六个给定物理径向 jet 的唯一五次插值。仅换编号或保旧宽度会变函数；本实现真正把当前准确宽度送入原完整 polynomial 算法。

原 self.omega[cell:cell+2].reshape(6,self.n) 顺序与482通道全部保留。仅六个实际端点字确均零时沿原算法保零 polynomial shortcut；未知数据不作零。omega_piece 用 leaf.current_cell 和当前准确节点，将 $s$ 叶通过 affine 差/准确宽变局部区间，再用原 restricted Bernstein 值/导包围。它不用 original_cell 当当前插值胞。

准确场把实际 current point 的 literal binary64 系数作为准确 dyadic 数据，按已刊 J 模型的准确 affine 域定义函数。该包围不是工作 Torch/NumPy 输出的逐字误差界。父末点注入、working midpoint、求积或校准的舍入不会因本包存在自动变已付。

## 6. 全切点并集与逐叶双重归属

准确计划取完整集合

$$
\mathcal C=\{X_j\}_{0}^{922}\cup\{Y_i\}_{0}^{1844}
\cup\mathcal C_{\rm seed}\cup\mathcal C_{\rm profile}
\cup\mathcal C_Q\cup\mathcal C_\gamma.
$$

它含两个 support 的全部端点、两个 central 的端点、每个 central 四 quarter/十二 polynomial pieces 的端点、所有 bubble/Q/gamma 支撑端点与峰。不是 Gauss 样本集合，也不是按浮点 midpoint 选分支。

每个 cut 是准确 affine 对。compare 对完全相同的对直接判等；不同对用准确 S 盒验证差的严格符号。若无法确定顺序，原 EnclosureUnavailable 诚实保未付，不借 double 排序充准确顺序。

相邻 cuts 形成初始叶，保存 id、left、right、current_cell、original_cell、kind、support_index、depth。其宽必须正，而且同时满足

$$
[Y_i,Y_{i+1}]\supseteq[\ell,r]
\subseteq[X_{\lfloor i/2\rfloor},X_{\lfloor i/2\rfloor+1}].
$$

完整准确二分关系先已核，original_cell=current_cell//2 才有依据；整数对应不能替代 affine 包含。children 用准确 affine 中点分裂，原 current/reference cell、region、所有 source 身份保留，仅更新端点/id/depth。

leaf reader 独立重读 whole layout、全部 nodes、mesh 和 carrier，并核：

- 当前1845/参考923完整定义与所有 even working 字；
- 每叶两个 cell 的范围、准确包含、正宽、邻接及完整0/S域；
- current cell 集恰为0..1843，reference cell 集恰为0..921；
- plan 边界集恰等完整 cuts 并集；
- 整个 point/model/target/source/request/domain canonical 与实际 records 一致。

叶数通常超过1844，因为 profile/control 的全部 cuts 必须保留。仅 count=1844 或部分叶成功不构成完整覆盖；真实叶数由实际准确 plan 给出。原尾部、所有细分中点及所有角模式均不省略。

## 7. 冻结 mean、normal32、全圆与全部物理 jet

WholeMean.context 仍是原冻结 context923，整个 reference_mean_adapter 沿已刊父体。它对真正全角区间重新算准确参考均值及两角导，含完整 scalar/T0、边层、profile、central、固定 Q。有限 literal mean batch 的费用不能冒全角；current J 翻倍也不能悄悄改变 seed mean 定义。

accurate_normal_rotation_and_stage_boxes.py whole SHA-256 是 29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b。它用准确指数级数与完整导数余项，不把 working Horner 标签当准确微分。本包不改该核。

每个原阶段继续用完整方程、当前与上一阶段全部控制/角 jet、centered endpoint/reference 差及完整积分。实际 stage_XXX_J 仅是有来源的有理预调候选，保其完整字与实际阶；不是准确逆矩阵的无误差证。根盒/逆矩阵收缩以及一、二角方程仍须由准确核实际付清，全上游误差逐阶段传递。32段没有压成最后一段，working residual 不替准确总方程 residual。

计划保留每个真正 recorded/required literal angle，并另外覆盖 $\phi/\pi\in[0,2]$ 的1024个闭胞。缺高阶 packet 或完整 snapshot 不能凭计数补出。原 uniqueness-domain 有向包含仍负责全角 branch glue、周期接合和原 literal 关联；半转/quarter 对称与 N 的整除关系不自动证明同 selected branch。

每完整角 job 的六个物理量为

$$
F,\quad F_s,\quad F_\phi,\quad F_{ss},\quad F_{s\phi},\quad F_{\phi\phi}.
$$

R715 的 raw-defect lift 与 $h,h',h''$ 全保，centered residual 某值为零不等于其导数可删。每叶还有同目标 $a_{\rm deep},b,c,b_s,c_s,S,R,\rho_0$ 的准确盒。组成这些盒所需 scalar/mean/profile/rotation/积分/算术责任保留于原准确算法。

complete_original_working_physical_sixjet_word_errors_paid 继续 false。准确场向外盒可供连续几何使用，但没有因此得到 working 场字到准确场的全六 jet 差、外参数 J/J* 费或父子 working roots 逐字等价。

## 8. 连续 Gram、K、support 与 R717 D

连续 geometry 数学正文沿原完整体：以全部六 jet 计算相对同一 $g$ 的对称 Gram 算子界，保完整一/二基本形式与度量逆，包围两主曲率。candidate normal 为 $F_\phi\times F_s$，水平与竖直 support 分子分别记。没有把 entry max 当算子范数，也没有只用 $F_{ss}$ 代替完整曲率。

[R717](../results/R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) 同叶三维位置范数从同一完整 $F$ 盒计算。与分坐标 cylinder D 一起保留，取有效较小的 formal union bound，覆盖完整形式上的旋转/反射/固定帽联合。不能把不同叶或不同角的未付近似极值拼成全像证书。

只有全部 whole-angle jobs、全部 radial leaves、完整 source/point/request/journal/branch 条件和最终字节复核齐，才升 complete upper cover。正 Gram、normal 非退化、K、support 缺口保 null/未付或真实 partial statistics；局部成功不能补全域。

形式联合 D 不是实际下反射、端口 C2、两帽、外向、全 physical phase 或 mixed-pair reach 的证明。optional beta bridge 仍需原八个完整同场证据角色及 lower/activity-seam 责任，并重读比较所有真实 support 行。它不生成缺失证明，不拿 complete upper flag 代外向，未预先排入这两步 ready。

## 9. 持久接口与 partial 边界

| 运行体 | 主 schema |
|---|---|
| family | complete-fixed-fejer-J1845-accurate-field-family-binding-v1 |
| input | actual-fixed-fejer-J1845-complete-normal-packet-accurate-field-input-v1 |
| radial | actual-fixed-fejer-J1845-complete-accurate-reference-control-radial-boxes-v1 |
| normal | actual-fixed-fejer-J1845-complete-normal-root-and-physical-sixjet-fees-v1 |
| leaf | actual-fixed-fejer-J1845-complete-physical-sixjet-leaf-reader-v1 |
| geometry | actual-fixed-fejer-J1845-complete-continuous-gram-curvature-support-v1 |
| bridge | actual-fixed-fejer-J1845-complete-geometry-to-conditional-R650-beta-bridge-v1 |

normal report 保原 actual report/source、own point、snapshot、完整 input/request、各角 journal、实际预算、complete 状态、最终 bytes recheck 和全旧数学字段。新增 current/reference J 和 declared cells 是来源声明，不能替代 complete flags。

accurate_geometry.complete_exact_radial_plan 的每叶新增 current_cell。geometry metadata 的 accurate_current_and_reference_radial_domain_identity_sha256 必须等于完整 input domain canonical。连续 geometry binding 又保存这个身份、整个 exact plan、原32共同分割及 full-circle requests；主 report 保存 current_J=1845、fixed_reference_J=923 和两种完整胞数。还没有 upstream complete binding 的早期返回保 complete=false，不造已付域。

所有中间 proof、当前点、carrier、job journals、完整 physical streams 和 geometry blocks 只留 runner，每条 record 含真 path/bytes/SHA。最终主报告再次核全部 bound input/output。目录中有一个中途副件、某个 true flag 或一个成功角文件，不足以被后继当完整证书。

正常 time/leaf-budget 用尽保完整已付 prefix 与未付 jobs，不证明无解、曲面不可行或科学 solver 失败。source/shape/bytes/current point/domain 失配是明确错误，不吞成0或空覆盖。

## 10. 实际15来源与全部执行参数

既有报告位置是：

~~~text
{work}/fixed-fejer-radial-J1845-independent-first/report.json
~~~

该位置来自真实 resume-20261127-followups-15.json 中完整 scientific/readout pair。读取版本90478字节、Git blob 6f23e1a2518617d5540a79e748b4be450c134202，parent_request_id 为 visible-larger-resume-20261127-15。这只定位已排来源，不表示完整场/final/packet已经返回；费用源不修改该 pair，也不要求未发生的父 final。

完整 normal 命令：

~~~text
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_J1845_complete_normal_root_and_sixjet_fees.py
  --repo {repo}
  --report {work}/fixed-fejer-radial-J1845-independent-first/report.json
  --outdir {work}/fixed-fejer-J1845-normal-root-and-sixjet-fees-v1
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
  --field-family J1845
~~~

完整 geometry 命令：

~~~text
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_J1845_continuous_gram_curvature_support.py
  --repo {repo}
  --normal-report {work}/fixed-fejer-J1845-normal-root-and-sixjet-fees-v1/report.json
  --outdir {work}/fixed-fejer-J1845-continuous-gram-curvature-support-v1
  --seconds 900
~~~

两步 parent bundle 都保 fixed-fejer-reference/reference.npz。原 normal38个 argv 字仅替实际 report/output 路径并加显式 family 两字，成为40；geometry原8字只替两路径。原36/48个 summary selectors 全字保留，不删不利结果，不把 missing 当 success。完整 JSON 含全 pins、未来值 null、准确范围与未完成义务。

按2空格缩进和末换行，两个完整 step 分别5243/5571字节，合并 steps 数组11143字节。现90478字节队列若原样追加会越过95KB，由唯一队列写者按真正返回调度；不能为限额裁 argv、selector、域、阶段或预算。

## 11. 完整运行源与可逆全文再生

| 角色 | 完整源 | 字节 | SHA-256 | Git blob |
|---|---|---:|---|---|
| family | [fixed_fejer_J1845_fee_source_binding.py](../scripts/resume_20261126/fixed_fejer_J1845_fee_source_binding.py) | 20785 | 02551f8f6b7e74bdb161332215c3d07aaf8063d2de4f08ce8a63868365428faf | 2f0a34c8a4be00f9ebbfc02423bc6796eb6140d0 |
| input | [fixed_fejer_J1845_normal_packet_accurate_field_input.py](../scripts/resume_20261126/fixed_fejer_J1845_normal_packet_accurate_field_input.py) | 38319 | 839f8cd4e0357fd0f0dc61241b4eb2d04527e04db4046dbda868837866e800c7 | bf8d75b8d969581cfae3ed4ee35314675f5fa5fd |
| radial | [fixed_fejer_J1845_accurate_reference_control_radial_boxes.py](../scripts/resume_20261126/fixed_fejer_J1845_accurate_reference_control_radial_boxes.py) | 48761 | af75e60b73e5935476a8a60239d3380751c1ec07e4f6deb503ee31436c55ade8 | 8d6987b5c6fc3b8c397afb7dc6c114812a42b2d4 |
| normal | [fixed_fejer_J1845_complete_normal_root_and_sixjet_fees.py](../scripts/resume_20261126/fixed_fejer_J1845_complete_normal_root_and_sixjet_fees.py) | 40700 | 0e846404430fad55450c171ae5cb48255cdfc0debe0a1aeada3ff7cba5ca92bc | 18f32d324fcef17a8cec2f588d90106390d068bf |
| leaf | [fixed_fejer_J1845_complete_physical_leaf_binding.py](../scripts/resume_20261126/fixed_fejer_J1845_complete_physical_leaf_binding.py) | 54746 | 78b6ed398da3d815835e51e48201036f4c35947c8f8d72963e956b7639578e1c | 3b8d5d6b8e14fe775d0fd426bc8dfda2248354c6 |
| geometry | [fixed_fejer_J1845_continuous_gram_curvature_support.py](../scripts/resume_20261126/fixed_fejer_J1845_continuous_gram_curvature_support.py) | 47057 | 47c1e1ce08be098b3618c30e4f7ba298a95cd901a18a961116da01b8bbc90a79 | c61a47088ede7f95f86a008637f0ed0d37a61060 |
| bridge | [fixed_fejer_J1845_complete_geometry_support_beta_bridge.py](../scripts/resume_20261126/fixed_fejer_J1845_complete_geometry_support_beta_bridge.py) | 21130 | 706c197c94414817ad0d1478fd20b2359e25dc56a15b818396bdfe2fe82d4508 | beba3dde9ec56509b4ca718bf54106e272a8fcab |

以上都是完整独立可运行源码。旧 N13、旧 Fejér 和当前 J 求解体保原字，没有运行时 monkey patch 或片段替身。

完整参数：

| 文件 | 字节 | SHA-256 | Git blob |
|---|---:|---|---|
| [fixed-fejer-J1845-complete-normal32-full-circle-sixjet-fees-ready.json](../computations/fixed-fejer-J1845-complete-normal32-full-circle-sixjet-fees-ready.json) | 12271 | a8a0178cf3ff1f651cd7de9bff68df31683aa57edb6156cb39c23d0934db3103 | 2cc50ee7228c4b9977d052bcc37eee211f199851 |
| [fixed-fejer-J1845-complete-continuous-gram-curvature-support-ready.json](../computations/fixed-fejer-J1845-complete-continuous-gram-curvature-support-ready.json) | 12832 | adfe199db2c3658a042e05f8a1c9e40e442280223208ec11b537f230dfa2075f | b1fc4c85be0c77a6266de04d2d1648bfdf17b68d |

完整再生器 [reproduce_fixed_fejer_J1845_normal_geometry_fees.mjs](../scripts/resume_20261126/reproduce_fixed_fejer_J1845_normal_geometry_fees.mjs)：78166字节，SHA-256 ea2359d6e2585797590200410fcd8f4dacda3ea5efe60a50ff6ad3b530846fbd，Git blob a056cfc73cc9cb474c671689b02326d5ecf7f976。

~~~text
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_J1845_normal_geometry_fees.mjs
  --repo {complete_repository}
  --outdir {fresh_scratch_reproduction_directory}
~~~

它读取整个 pinned parent 文件，依明确原/新行块重建全输出，核全新 bytes/SHA，再反向恢复整个旧父。在写任何输出前重读全部父源，对既有输出核完整身份。--verify-existing 只比较九个完整既有文本，不重写；输出树保完整 topic 路径。不导入 Python、不调用科学、不改 refs 或 queue。

精确全文父源码如下。它们是文本来源，不能据此把旧 N/M 数值场当新J父场：

| 角色 | 原完整父源码 | 字节 | SHA-256 | Git blob |
|---|---|---:|---|---|
| family | fixed_fejer_base_bound_refinement_fee_source_binding.py | 20456 | 92df9772c5512c49f69b91ba46f799ebad552cad7a76072875e0cd62361ecbdd | 4cdc78510dba4d321703c06b75bdfcfb52aec559 |
| input | fixed_fejer_base_bound_refined_normal_packet_accurate_field_input.py | 33517 | 40924085d5c77e57f5286989e53d64caf733b763d92c74b03ecfe713607d3452 | 70c5457d8a196488f3da10788a1597f3a28a15c0 |
| radial | fixed_fejer_base_bound_refined_accurate_reference_control_radial_boxes.py | 45706 | d5bdec4193a4c62797a6a398e6da3bbf7c2aa5cf7cd9e9136fa2afc866e1add3 | 9faee20a3c226a500a06871fbde7409c436498b2 |
| normal | fixed_fejer_base_bound_refined_complete_normal_root_and_sixjet_fees.py | 40528 | 81081fa9d6c1347a7a8373789c01e9a5d48dcdfcee57558b53e6d909014539d3 | 6b25f8d9a355a536118a7bcf561d679c746d4c46 |
| leaf | fixed_fejer_base_bound_refined_complete_physical_leaf_binding.py | 47933 | fd8f64770614e58cec8f7d30352df2d3161d4ac1a8292419bbde47602e777d2a | 31939c19d60141a7e72ddfb4a6d8a3c654a8ff58 |
| geometry | fixed_fejer_base_bound_refined_continuous_gram_curvature_support.py | 46727 | 13c39eb2e3e13600e518181010813b3246fc6aab4e1a55ed393f5a5746ab9f7e | 4b4b20f145c891263e8aea364c1e51372ac167da |
| bridge | fixed_fejer_base_bound_refined_complete_geometry_support_beta_bridge.py | 20907 | adca737f9358522accf2cfd8f8edec9d7e0d1ec4ad4dda68ee95f89d6ef05210 | ecd386215e382150886d5938f1a4ffa76b169916 |

两份参数来自原 Fejér 完整9380/9901字节 ready，完整 SHA 分别 d38cabbbc9dbc3dd973fe271de7085b9ab5a5f6d5b14df5476c22fba3b91fafa、a2171bdfafd5aa4b3a2c70d53b57bb7c055be4dc17d29138b77fed211323aae4，Git blobs 分别 d00ea8dca3607ddb6e383a003044f4c8005fa331、2beb63b4a5b9fcce3f981a31769a1fbeb67cc043。它们不继承 N13 constructor 失败、N13 currentN 或未返回 N 场；只有新 source/schema、真实J路径、显式family和域说明变化。

## 12. 共享完整核与证明边界

| 原件 | SHA-256 | 保留责任 |
|---|---|---|
| so3_axisymmetric_continuous_integrand.py | a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6 | 准确 scalar/affine/quintic/Bernstein 基类 |
| accurate_normal_rotation_and_stage_boxes.py | 29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b | 准确 Exp、全部 stage/root 与角导 |
| fixed_fejer_reference_accurate_mean_residuals.py | ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0 | 完整准确参考 mean/积分费用 |
| fixed_fejer_reference_seed_angular_profile_error_bounds.py | 0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b | interval/trig/profile/seed jet 费用 |
| same_field_positive_support_parameter.py | e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991 | 原八角色输入下条件 R650 beta 消费 |

这些完整原件原字共享，不复制第二份。已刊 R676 的准确 affine 同g精化，R709/R710/R713 的 mean/profile/两角费用，R715 的完整物理 lift，R717 的同叶全像范数，在各自原完整来源内继续适用。本包不重复登记泛型 IFT/Gram/beta 定理。新实质是当前 fine quintic 与冻结 reference mean 的准确域分离及两端消费者的完整重核。

当前 core 的全连续正 rho 仍由原准确全圆算法实际证明。固定首3或有限采样正性不替该条件；R719/R720 的纸面 core 结论不提前填为当前场的 whole-image/support/reach 结果。

## 13. 已完成的核对与尚无的数值结果

V8中实际完成七完整 Python 文本及两完整 JSON 文本的正反向再生，各新旧 bytes/SHA 全相等。完整再生器中的九项 specification 与这些文本一致。没有 Python AST/编译、数学脚本或科学执行。

Geometry 独立窄读的是新 radial 的 current_omega_bounds/make_plan/omega_piece、原 a846 ExactOmegaBounds 全class，以及新 leaf 的 validate_radial_domain 与 plan归属。所读 current/reference 交界、reshape/准确宽缩放、所有 cuts、双胞包含及 WholeMean仍923未见阻断。该审查不冒全部七体审计，更不冒真实费用已经付清；未把额外审查设为运行前门。

本交付未产生未来 scientific report/current point/snapshot/fee report SHA，未产生全32根、全角 glue 的实际 complete 结果，未产生实际六 jet/Gram/K/support/D 数字，也未给完整闭面、caps/outward、全phase/mixed reach、工作字误差、外参数误差、收敛或原题完成结论。

后继必须按真实主report的 complete/binding/final-recheck 消费整个证据链。partial只保已付 prefix及缺口，不把历史未知 typed、未来父或缺失角填为空集合。全部新件均小于100KB；raw/数组/流/journals只留runner。根是唯一refs/队列写者。
