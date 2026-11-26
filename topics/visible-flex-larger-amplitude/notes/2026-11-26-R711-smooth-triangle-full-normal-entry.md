# R711 平滑三角中央相位的完整固定参考场与 normal 求解入口

2026-11-26。本文登记一套独立、完整、可直接交公开 Actions 的新来源；当前尚未执行其科学入口。数学依据是 [R711](../results/R711-smooth-triangle-central-profile-and-geometric-comparison.md)，准确均值与端层仍使用 [R708](../results/R708-supported-unit-meridian-seed-contraction.md) 和 [R709](../results/R709-global-convex-mean-closure-without-contraction.md)。本文没有新增完成标准、预试验门或求解成功结论。

新输入保留实际 4e 参考的准确固定标量度量、符号域、固定材料角、原核心和原高度，只把中央相位换成 R711 的十二段平滑三角形状。原全部自由核心、全部共享 quintic/Fourier 旋转系数、自由 H、完整正权 Gram 行、同 H² 坐标、192 个原几何选择行与附加幅度行、真实 Phase I、全已知位置筛选全部保留。它没有把当前自由旋转覆盖成某个 seed，也没有把旧根或旧场改标签。

## 1. 完整来源与字节身份

九个执行/读取来源及一个纯源码再生器完整列在下表。文件均保存完整正文，不以差异片段冒完整来源。所有 blob 只是这些小源码的不可变保护副本；没有上传科学数组或原始大报告。

| 完整文件 | 字节 | SHA256 | 未引用源码 blob |
|---|---:|---|---|
| supported_smooth_triangle_seed_mean_jets.py | 34725 | `f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917` | `ee318b8971ce3c3d10715fbcd648c3a3bcfd6712` |
| supported_smooth_triangle_meridian_reference.py | 39728 | `0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b` | `84eca8e0c3db5867ac3f04bcbf25a53433b4d2e5` |
| so3_supported_smooth_triangle_meridian_operator.py | 40771 | `6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865` | `f7a8cfe316f166613b784781b4277cd924c5f968` |
| supported_smooth_triangle_literal_zero_moment_input.py | 30950 | `307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7` | `77d9e2291cd8ddaa21e33126f4dc97b2029ad251` |
| so3_supported_smooth_triangle_normal_lift_operator.py | 92000 | `66e81e439a2545134549b4527e68a2480a9d8010679dcf9cfa23ca5e48c15d68` | `d6ff6aaee8f295d7f985a5693505887aa9196d0e` |
| so3_supported_smooth_triangle_normal_lift_geometry.py | 55829 | `ef46386e2313cd1e53c971ea8d6ee63a7c6d630074a8feb45ebb9103ec0e52f3` | `1d9da3bd5e7733c54745effb0b682a09584c6827` |
| fullclosed_supported_smooth_triangle_normal_lift_so3_qp.py | 67838 | `fd95d91abe9525cbfa34d55bd576be7dfba1fe25fcafb73bdaaea40e003ad65f` | `deaeb822c36001c780c988bfb3bc99bba9806b3b` |
| launch_supported_smooth_triangle_normal_lift_so3_actions.py | 17246 | `8dc81890440e744bd846e71b4d33848566dfdf76bcf9d30c47c59664a5823339` | `647549c8e7d77c7269e01c98c23b700ed43a9fcf` |
| read_supported_smooth_triangle_normal_lift_so3_report.py | 56712 | `3914004ac39b838c33411bd11660bb8fbec1372630c3569f3ea4ad5ae16c0f97` | `8de7f7530804c357a2a5ad5a51d7140c5e2c7bf2` |
| derive_smooth_triangle_supported_seed.py | 19176 | `dd59a539655dfe6f9754ada77f8e96f215d8bbe2accde1299518a491cba941b7` | `36f4274333b554c786239a868fa40e1038987ad0` |

来源的前驱分别是已刊 bd9c 均值核、30ea provider、e1bb base、9fec binder、5297 normal、d84 geometry、e482 driver、fa468 launcher 和 d788 pure reader。它们的字节保持不变。

纯再生器 `derive_smooth_triangle_supported_seed.py` 只读九份前驱的完整源码并逐一核其 SHA，生成独立新文件、逐树 AST 比较以及完整变更索引。命令为：

```sh
python3 topics/visible-flex-larger-amplitude/scripts/resume_20261126/derive_smooth_triangle_supported_seed.py --repo /path/to/actual/source-checkout --outdir /path/outside/repository/derived-sources
```

它只用 stdlib，不导入任何科学模块，不做 quadrature/root/F/J/矩阵分解。输出必须在仓库外。科学执行不依赖先运行这个再生器；公开的九份完整新源就是实际入口。

## 2. 同一准确对象与明确改变

实际新 provider 从已经逐字绑定的 4e reference 构造，保存同一准确 scalar definition、reference 完整模型、原 core/chart/H、支撑、端层以及完整工作求积定义。准确三均值方程仍是

$$L_c v+B(Nv)=P_{\rm original}-\Gamma_{\rm original}-\int_{U^c}T_0.$$

其所有外补集包括无限尾，四个端层全部保留。这里的 $v,d=Nv,w$ 冻结于原初 core/H，既不接受当前外层 $x$，也不在每次优化时重新覆盖当前 $\omega$。

新中央参数是规范有理数 `profile_delta='1/128'`，对应模型键 `exact_profile_delta`；它与端层总宽 `relative_boundary_total_length='1/16'` 是两个不同参数。外部两支持仍为 $(1/32,15/32)$ 与 $(17/32,31/32)$，每个端层准确宽为 $S/64$。

新模型增加明确字段：

- `mathematical_profile_piece_count=12`；
- `mathematical_amplitude_interval='(0,pi)'`；
- `old_five_piece_working_cache_or_geometry_inherited=False`。

新的 seed、base、normal、geometry、控制输入和报告均有独立 schema 与完整源码身份。通用字段名 `fixed_supported_unit_seed_model` 仍指单位 seed，但其完整值必须是此次新 schema/源码；它不允许旧五段对象冒充。

## 3. 同一个完整 point evaluator 与十二段正权规则

新均值模块定义 `smooth_triangle_value_and_derivative(t, profile_delta)`。这是 R711 的整个 $[0,1]$ 函数，返回工作 $h_\delta,h_\delta'$，没有丢掉任何 ramp，也没有裁剪 profile 值。四个 quarter 的反射符号与参数方向分别为 $(+,+),(+,-),(-,+),(-,-)$。每个 quarter 包含完整的 S5 ramp、正长度中段和反向 ramp，合计十二个多项式 piece。

新 provider 的 `_profile` 直接调用这个同一来源的函数，并核其 code filename 的完整 SHA。因此均值求积与实际任意径向点的 profile 不存在两份未关联的公式。实际二进制 width、节点、normalization 和求和误差仍未包围；共享工作表达式不等于这些误差为零。

默认每个完整 piece 使用 16 点 Gauss，合计 192 个全部正权节点。完整记录准确 Fraction 边界、实际边界/宽度/节点/权/两种 profile 数组的摘要。没有把四 quarter 约化为一个 quarter，也没有重新归一化权。与原五段的 80 个节点相比，profile moment 的工作节点数增加；不宣称这项本身提速。

实际幅度二分区间改为工作 $(0,\mathrm{float}(\pi))$。两端 moment 都由完整规则实际计算；即使准确 $A_\delta(\pi)=0$，源码也**不把工作端值强制置零**。实际括号失败、导数非负、非有限值或原容差未满足，都产生自己的完整失败记录。

准入/求解仍同时读取 `a(lambda)-|v|` 和完整物理组合闭合

$$B+L_c a(\lambda)d-K.$$

其物理三分量范数必须保持原 $2\times10^{-12}$ 工作容差。三个 mean 分量、完整 Newton 真残差 Armijo、全部角位置、$v,d,w,\lambda$ 的一二角导及相应实际残差读数没有删除。R709 的 $q<1$ 不作为数值门，R711 的全部正半径覆盖也不冒成此次工作求根已经成功。

## 4. 两角链与真正物理场

新 profile 只依赖径向归一化坐标；其参数固定。中央段仍用

$$T=\cos(\lambda h_\delta)d+\sin(\lambda h_\delta)w,$$

完整保留 $d_\phi,d_{\phi\phi},w_\phi,w_{\phi\phi},\lambda_\phi,\lambda_{\phi\phi}$。径向导数是

$$T_s={\lambda h_\delta'\over\ell_i}(-\sin(\lambda h_\delta)d+\cos(\lambda h_\delta)w).$$

四个 world 参考 jet 接口仍为 `T0,T0_s,T0_phi,T0_phiphi`，形状均为 `(P,A,3)`。准确符号域/物理长度与工作 carrier 分开记录；它们没有变成另一个固定 $g$。

外层 base 的完整旋转、积分、核心隐式逆图、六 jet、所有 J/J* 和 H² 坐标方法沿原体。完整 normal 层仍对所有外层自由变量求同一个有限共同分段系统的隐式导数。seed 的三维均值 Jacobian 可逆不等于这个六控制 normal 闭合 Jacobian 可逆；新 source 没有转移这样的证书。

中央幅度允许超过 $\pi/2$ 是明确的新输入范围。该范围保持单位、闭合和端口恒等式，但不保原强正高度条件；旧嵌入、单调性、曲率、reach、握持或 Euclidean 商数值均不能继承。所有实际几何仍由完整新场读取。

## 5. 唯一额外 normal 成本改动

在原 `_normal_frame_jets` 入口，`enabled=torch.is_grad_enabled()` 已经在临时 `torch.enable_grad()` 之前捕获。此次只把该方法中一处

```python
create_graph=True
```

改为

```python
create_graph=enabled
```

临时 `enable_grad` 仍使完整 $f_u$ 及其两角 jet 被实际计算。外层 active J/J* 情况的 `enabled=True`，所有上一 stage 的 $u/A$、原零控制目标和参数边完整保留。外层 `no_grad` 只求工作值时，不再创建随后由既有 `detach` 丢弃的导数图。

没有改 `_closure_jets`、stage root、任何 3/6/9 阶局部矩阵或递推、surrogate、完整 J/J*，没有改 32 个共同 Fraction stage、每角根选择、数值域或容差。没有引入 A0/A1 的其他重写、跨源 cache、ridge、删变量或改阻尼。新模型和 metadata 明报 `normal_frame_create_graph_matches_outer_grad_enabled=True` 与 active 全图保留。实际内存/耗时和成功性尚未返回，不能把源码省工当实际加速结果。

## 6. 完整来源闭包、控制输入与历史

新十二字段 literal-Q binder 保持完整原 18 个字的历史来源和全当前 reference/profile/chart/base.initial 绑定；同时绑定完整新 seed model/id、provider/mean/base 源码及完整 working definition。旧 literal 参数只作为明确定义的常量采用，不称它们是新场真实 moment 的逆。

此前九个 history 文件全部保留，另加旧五段 supported seed 的真实返回报告作为第十个完整 manifest。ready 不允许该文件缺失，也不把目前尚无返回当空集合。每个现有/新发现地址仍以原 binary 地点完整保留，profile 改变不是删除历史的理由。

第十报告只提供历史地址；新输入仍从实际原 reference 的原完整初点开始，既不读取其旧末点作为同场继承，也不沿用其 Phi/根/几何。源字节/模型/working identity 不同，原 checkpoint 不能作为同源 restart。将来只有实际同新模型/source/工作定义的完整 checkpoint 与自身报告可继续。

## 7. 原完整求解循环与读取器

`fullclosed_supported_smooth_triangle_normal_lift_so3_qp.py` 从 `def save_report()` 至文件末尾与 e482 **逐 byte 相同**，后缀 SHA 为

`9b05f8e00c483491ffd9259b2d675af940c6f0b8a8104d6bfcd70ffb0e31b4ee`。

`so3_supported_smooth_triangle_normal_lift_geometry.py` 从 `_set_x` 至文件末尾与 d84 **逐 byte 相同**，后缀 SHA 为

`50d6f1414807ea91710ecf3a0e3e52d9530a04f299763d2a05f30c372f27bf7e`。

这保留完整实际 C 前缀、两支幅度、H/cap 行、全网格及两永久地点集合、每候选真筛、拒绝后新地址、父重读、Phase I 的物理 g 与共松弛分离、同 Phi 原射线和全部失败归因。它未包含另一个尚未接入的 SOC 或预条件器。

新 pure reader 严核新的整个 source registry、当前 reference/model、十二字段控制 input、profile_delta、十二 piece 成功标志和新 seed 批次身份。原 34 个 normal snapshot 键及实际 currentpoint 归因保持；失败尚未得到场时保留 null/缺读语义，不填旧场数值。失败报告的 pure 读取依赖真实初 reference，因此无需 final.npz 已存在。

## 8. 已做的验证与没有做的执行

本次实际做了以下纯源码验证：

- 九个完整前驱 SHA 检查，九个新源的 AST、compile、py_compile、重复 literal dict key/keyword 和尾空白检查；
- 新 driver 26 个 source role 全部核实际完整文件 SHA，13 种 literal `paths[...]` 消费全部落入已声明 role；
- launcher 与 driver 的完整 parser AST 在只去掉 launcher 专有 print/install 两 flag 后相同；
- launcher/reader 的完整 driver SHA 一致；完整 physical loop 和 geometry 后缀字节相同；
- 完整 ready 的实际 stdlib `--print-command` 成功：150 个 argv 项、10 个 manifest、正确新 delta 和原 spectral epsilon；
- 所有 source 身份与批次/模型名称均为独立新来源，没有修改已锁或在跑的五段源。

没有 import 科学模块、没有本地 root/F/J/积分/因子、没有科学 fixture，没有声称任何新连续或工作数值通过。源码检查不是科学成功。

## 9. 完整 ready 与参数

完整参数文件：`computations/smooth-triangle-fixed-reference-normal-full-history-run05-ready.json`。两步分别调用新 launcher 和独立 pure reader，输出目录为 `smooth-triangle-fixed-normal-lift-first`，原五段输出不覆盖。

参数保当前完整首入口：全 $M=160,J=923,N=2048$ 与原完整正权观测；`jet-sum`、径向长度 .05、角转折24、mu .01；p4/epsilon .001/scale .05；一次完整 metric 方向，最多16个 QP advances；Phase I 最多4方向、每方向64；共同 normal 32段；原 all-row/geometry/amplitude 策略与全部原自由量。预算只定义这次完整尝试，不是问题能力上界或完成标准。

新 profile delta=1/128，12×16点全部正权。完整 mean Newton最多128、每步最多24回溯、原物理容差2e−12；lambda二分64；outer全径向积分仍Q8。原高度不改变。新的 source/model/root/cache 身份使此次初始 Phi 必须自己完整读取，不可与前一个 profile 的 Phi 直接相减。

当前 ready 仅准备，未准入或执行。是否实际排入由真实前驱/历史报告返回决定；必须加入届时所有实际必要的新增地址报告。

## 10. 连续费用和完成标准的责任

R711 给出了此新 profile 的准确全部正半径存在、两角链、近最优转角斜率、限定中央段 $|F_{ss}|$ 比较及完整 Gram/曲率/位置/握持预算。它没有将 $|F_{ss}|$ 的改进冒 principal curvature 的实际改进。

已刊 R710 执行核严格绑定旧五段 source/profile，它不能接受这些新源。新输入若后续需要连续费用，将以独立新来源采用 R711 的新 scalar 导数下界及 $(0,\pi)$ 幅度范围，保 R710 其余真实 mean/向量误差链和 R707 normal 链全部费用；不能把旧 `(1-4epsilon)` 平台下界或旧 lambda<pi/2 条件搬来。完整外部求积/trig/carrier/root/normal 费用尚未支付。

最终固定问题的 $10^{-6}$、真正全相位闭曲面/握持/反射 Euclidean 商/reach 与有意义的同问题加密收敛，仍完全按本课题 README；此入口没有以新 profile、阶段预算或条件证明替代它们。
