# 当前连续十族真450固定帽的独立区间接口

作者：OpenAI / ChatGPT amplitude agent。日期：2026-11-15。

完整证明见 [R417](../results/R417-current-ten450-fixed-cap-six-jets-curvature-and-normal-balls.md)。本接口只说明当前对象、准确字段、API和执行边界，不创建请求、workflow或未来数值结果。

## 1. 冻结交付

运行源：

computations/geometry_20261115_current_C_ten450_fixed_cap_balls.py

长度23622 B，SHA256：

0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae

论文：

results/R417-current-ten450-fixed-cap-six-jets-curvature-and-normal-balls.md

长度13627 B，SHA256：

e5d40dd6d86f17e5706cb545e6b557b52e81f0777dba30ec8d07e0f889008bb6

本接口为第三件。另交相对旧帽17496B全文的完整文本差异，说明旧main/binder未复用、数学纯函数由直接导入引用，而不是伪造旧source identity。旧帽/R409/R413/R400/193源均未改。

## 2. 直接依赖与实际加载

| 源 | SHA256 | 本源实际调用 |
|---|---|---|
| geometry_20261115_current_C_ten450_shared_field.py | 6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3 | 验当前CurrentSharedAssembly类与七元组来源；不再调用runtime/load_shared_bundle |
| geometry_20261115_current_C_original_cuff_target_atlas.py | 02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2 | bind_loaded_shared_bundle与canonical |
| geometry_20261115_fixed_cap_rational_balls.py | a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e | disk_partition、minimum_distance_squared、cap_cell及其内部graph_at |
| root_mixed_phase_normal_balls.py | ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6 | 仅sqrt_upper |

上述四个直接源都按完整字节核SHA。Shared模块严格从实际A的 type(A).__module__ 在sys.modules中取得，再核其真实__file__、冻结SHA和 module.CurrentSharedAssembly is type(A)；不扫描并取第一个同路径模块。R416可能在旧R409已加载后用自己的模块名再载入相同文件，源码相同并不使两份Python类相同。其他无此类对象交接的纯函数模块仍按原同路径复用／独立非main名字加载。R413 binder只比较实际字段、source、word和loader guard，不依赖A的Python类身份。旧帽的 bind_geometry、load_sqrt_kernel、main 完全不执行；它们所需的e70d/ac635旧field和marker.index/kappa不是此输入合同。

此表不是完整科学闭包替代。传入七元组必须已经由R409的真loader产生，原SavedPrefix/Checkpoint/当前target与所有原数组、响应、接受记录仍由其原闭包认证。本源不重算BVP、不访问新的RHS、fullDN或准确C，也不把来源元数据当第二份接受证书。

本源只用Python标准库Fraction及原有理sqrt纯函数。675 Jet2仍属活动片；帽无需导入它或启动旧Arb/runtime。没有库更新、额外native依赖或新的接受前门。

## 3. 所需实际对象

七元组严格为

    paths, plan, assembly, target, saved, A, bindings

这是R409原 load_shared_bundle 返回值，顺序和七个对象保持不变。其原schema为 R409-current-C-ten450-shared-background-complete-field-v1，当前完整target仍为原准确连续十族；真正450来源不能由旧有限十族、453删行或摘要/哈希伪造。

另需实际R413的准确atlas及其attachment。调用者从原文件读取时应核自己的实际完整文件SHA，再交对象；R417会用冻结R413绑定函数重形成attachment，并按完整canonical字节与给定attachment比较。它不替换或重写R413原结果。

相关实际字段：

| 位置 | 含义 |
|---|---|
| plan.cuff | R413从原C rCuff保留的同一半径字词 |
| plan.cap_height | 完整显式准确帽高度的原JSON数值 |
| plan.fixed_cap.markers | 两侧全部四字段marker列表 |
| A.shared_background.radii[0] | 必须是同一准确cuff |
| A.shared_background.nodal[0][0] | 必须是同一准确H |
| target.complete_current_ten_target | 当前完整十词及准确C target identity |
| saved.checkpoint.receipt / target_identity | 原实际真450来源，由原loader负责全部内容认证 |
| assembly.mean_gauge.whole_lower_sheet_reflected | 原整体lower反射 |
| assembly.core_and_hold_gauge.native_cap_rotation_axis_xy | 原Cartesian轴，不重选registration |
| atlas.original_cuff / fixed_caps | R413原cuff和完整帽内平坦环带 |
| attachment.original_shared_binding | 与这一个实际七元组一致的R413附件 |

每个marker恰有 upper（布尔）、center（两个原有限数值）、radius（正）、height（有符号有限值）。当前格式没有index或kappa，R417不会读取或写入这些原字段。其内部列表序号和 $8A/R^2$ 只供旧数学纯函数使用，明确标记为派生。

原plan值保准确dyadic／整数和原little-endian word。准确H与renderer投影的区别只记录，不要求后者额外通过误差／逐词门。负零可能在准确Fraction中化为零，原plan word仍保，未把这视为科学失败。

## 4. 最小可执行API

只有公开Actions环境允许实际绑定及有理求值：

    GITHUB_ACTIONS=true
    GITHUB_REPOSITORY=Rogerhu12/math-research-public

本源无CLI/main，不需要另造输入schema或wrapper。已经加载同场的科学消费者可按以下对象调用；这些是API说明，非本轮执行：

    bundle = shared_module.load_shared_bundle(actual_shared_args)
    atlas = actual_SHA_checked_R413_atlas
    attachment = cuff_module.bind_loaded_shared_bundle(bundle, atlas)
    caps = cap_module.bind_loaded_shared_bundle(
        bundle, atlas, attachment, actual_computations_directory)

    binding = caps.describe()
    one_cell = caps.cell(actual_path, actual_upper, actual_sqrt_bits)
    all_caps = caps.cover(
        depth=declared_depth,
        sqrt_bits=declared_base_bits,
        max_cells=declared_max_cells,
        budget_check=actual_resource_callback)

R417不会再次运行R409 loader；上例第一行是调用者原本取得七元组的步骤，不是帽API内部重复操作。也不会改变给定tuple或其guard、target未付标记、旧scope或任何参数。

### 4.1 describe

返回独立same-field binding副本，schema：

R417-current-ten450-fixed-cap-rational-six-jets-and-balls-v1-same-field-binding

保当前source、四直接source、完整原shared binding、实际shared文件receipt、R413 atlas canonical SHA及attachment、原cuff/H/全部marker字词、当前完整十target、已继承的帽内平坦环带及未付责任。每cell用该原binding的canonical SHA，避免重复携带整张来源表。

这里的文件receipt只标识传入原loader的对象。源码不凭文件名认field，也不将单个source SHA当数学接受。

### 4.2 cell

输入path是原四叉字符串，字符0/1/2/3分别左下／右下／左上／右上。它从原 $[-c,c]^2$ 准确重建闭box，不能给一份不相干的box再贴路径。upper必须为布尔。sqrt_bits是实际有效bits，范围16至4126；完整cover按原base+depth使用。

严格盘外box不属于cell；相切box保留。实际参数域为闭box与原闭cuff盘的交。矩形中心可在交集外，不影响位置／法向球，因为graph准确延拓到整个平面。

返回schema：

R417-current-ten450-fixed-cap-rational-six-jets-and-balls-v1-cell

关键字段：

| 字段 | 完整语义 |
|---|---|
| same_field_binding_sha256 | 上述独立完整binding的canonical SHA |
| original_ball_record | 原cap_cell完整输出，含路径、闭box、盘交域、原中心／半径与全部界的推导数据 |
| Cartesian_six_jets.value/x/y/xx/xy/yy | 各三个坐标，每分量均为准确有理lower/upper |
| graph_six_jets.value/x/y/xx/xy/yy | 原 $b_\sigma$ 完整和的六个准确闭区间 |
| curvature.induced_metric | 完整2×2帽目标Gram $I+Db\otimes Db$ |
| curvature.squared_area_density | $1+b_x^2+b_y^2$，准确下界至少1 |
| curvature.unit_normal | $(-b_x,-b_y,\sigma)/\sqrt{1+|Db|^2}$ 的完整分量区间 |
| curvature.oriented_second_fundamental_form | 按 $N\cdot F_{ij}$ 的完整2×2区间 |
| curvature.shape_operator | $g^{-1}\mathrm{II}$ 完整2×2区间 |
| curvature.mean_curvature / Gaussian_curvature | 原取向约定下的signed interval |
| curvature.both_principal_curvature_absolute_upper | 同cell全部marker的 $8|A|/R^2$ 和 |
| exact_cap_target_relative_metric_error_zero_by_definition | 只该固定帽和R413既定局部目标，不能用于改活动目标 |

每个区间是两个准确有理字符串lower/upper，不是样本最大最小值。几何六jet高度分量全乘side；准确位置为 $F_\sigma=(x,y,\sigma(H+b_\sigma))$，不是 $\sigma H+b_\sigma$。

original_ball_record保原字段固定位置、固定法向中心和两个半径。球中心法向可非单位，归一化误差已由原sqrt上界显式支付。curvature.unit_normal的分量区间是另一份有效包含表示，二者同源同帽，不互相替代。

### 4.3 cover

输入depth范围0至30，base sqrt bits为16至4096，实际cell精度base+depth。要求显式max_cells≥2且最坏 $2\cdot4^{depth}\le max_cells$，避免在未声明资源内无界展开；不涉及残差、曲率或metric是否够小。

原disk_partition一次形成全部闭path和严格盘外省略box。顺序先全部upper，再全部lower，每侧保原path顺序。边界重叠是完整覆盖的一部分，不删相切或支持圆边界。

budget_check可省略；若提供，它是原调用者的资源／外部中断回调，不接收科学残差，不产生新的接受阈值。源码在partition前与每cell前调用；原disk_partition本身仍是原纯函数，显式最坏cell预算限制其大小，没有承诺它每个内部节点都可细粒度中断。

正常返回schema：

R417-current-ten450-fixed-cap-rational-six-jets-and-balls-v1

含完整临时cap_cells、完整exact_closed_disk_partition、真实已完成数以及两侧全cover完成标志。只在原两侧全部地址完成后 completed 和 complete_two_cap_six_jets_balls_curvature 才为true。

若partition前／中失败，则pending记录两个原盘全未付；若已有完整partition，则保原全部path表与真实未付半开索引 [cursor,total)，并给next_cap/next_path。已完成cell不丢弃；未访、失败和外部中断不被改写为完整cover。

## 5. 该API不产生的结果

即使未来all_caps.completed=true，也只表示该实际固定帽的完整区间覆盖及相关局部量已付，不是whole field成功。以下字段始终保明确边界：

- complete_active_sheet_or_pair_cover=false；
- whole_surface_metric_proved=false；
- full_surface_curvature_or_reach_or_held_proved=false；
- finite_renderer_rounding_error_enclosed=false；
- new_BVP_or_native_acceptance=false；
- task_completed=false。

单帽作为Cartesian图的局部正则性由准确Gram下界1给出，但两帽可能相交、也可能与活动场相交。本源不新增H>0或分离条件来遮蔽这些未付责任；完整拓扑、embedding、reach、held和规定尺度仍由原题整体处理。

帽metric误差恒零只针对R413已定的帽目标。整个active目标、准确C根选择、cut公共图、完整prefix/tail/patch与四Loewner原责任不被该局部恒等式覆盖。

## 6. 与R418后续组合的准确接点

后续组合器可直接消费上述cell中的：

- 原closed Cartesian box和原盘交域；
- 完整六jet；
- curvature.induced_metric作为该帽已有目标；
- original_ball_record及其完整来源；
- 全部显式path和真实pending状态。

不得把disk box当成整圆盘内部，亦不得用只取中心点的样本替代六jet区间。帽区间无需把Cartesian角转换为原物理角，不能对固定帽施加活动相位旋转。所有重叠marker和负振幅必须保留；本源已在准确graph和target形成前完整相加。

R413帽内平坦环带和原cuff同目标两jet在binding里作为已付的独立子责任引用。本源没有改变原R409几何cut补丁，R416准确cut组件若另行接入，必须通过其实际独立接口与此同场绑定，不能仅合并两个success标签。

## 7. 生命周期、输出和当前状态

本源返回内存对象，不写raw、不上传artifact、不分块编码、不删除任意输入或其他项目目录。完整cell表属于可重算输出，只供同job受管临时对象使用；未来调用者沿原必要摘要硬界、读回完整和owner静止后清理，不能把整表经小文本API搬运入Git。

若原193成功后按原规则清理450 raw，不能凭其摘要/SHA恢复这个live七元组；要在新的真实两阶段同job再生并接R409/R413，或在那次真实owner清理前明确接入。本文没有执行R409、没有预选plan参数，也没有修改193。

本轮只有原源码全文读取、纯纸面推导、独立源码／文档写入、文本差异及bytes/hash。没有本地科学、科学import、AST、编译、fixture、benchmark或新的独立审核门。没有实际run；所有区间数值、原场结果与全几何条件保持未执行状态。
