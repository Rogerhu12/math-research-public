# 同一固定 Fejér 度量下 b/S=5/8 与 3/4 的输入选择：原六族有限筛、mean 域和已存观测

2026-11-27，UTC。本稿只读现有完整数学与程序正文，分析下一次独立初值选择；没有科学执行、场/导数/root 复算、AST/fixture、数值 benchmark，没有生成新参数文件，没有修改正在运行的 19/20 源、队列或预算。

**建议：若现在从 b/S=1/2 选一个下一次独立 width-only 输入，优先考虑 b/S=5/8，profile δ 仍为 1/32。** 这是根据中央长度代价较温和作出的选择判断，不是两个未知实际场的曲率排序。b/S=3/4 仍是源码合法、有端层转向动机的更强尝试，但其中央段只有原来的三分之一；现有两次有限最大值不足以支持把它称为必然改进或新的默认。新增两种 b 的准确 mean、全 32-stage normal、工作场数值与连续费用目前均未知。

本稿引用既刊 [R721](../results/R721-supported-seed-width-and-profile-sensitivity.md) 的参数结论，不重新证明 R721/R722，不把本分析加到求解入口之前。所有原自由变量、全角/全径向域、原 32 段、迭代和回溯预算、接受不等式保持其原合同。若后续选择新 b，仍是同 g 下另一个完整 seed/field model；不能把旧初点的控制词摘要相同解释为同一个实际场，也不能将旧 final 的 model 直接重标。

## 1. 采用的真实观察及其边界

[原 19 公开记录](https://github.com/Rogerhu12/math-research-public/blob/b93221b5009a12dfc7973c58f95c70b6a7a07fe9/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md) 在固定提交 17561514e3a4b718bc1a0dd7ad084c82e5a0406f 保留完整小索引身份：34,784 B，SHA256 b652b0221ca9ea1c620f5cee63d6d9a90500f6a68081e8f76b77b3f54de88e3b。该记录的初始几何完整点为 7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47，实际 model 为 0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add。下表引用已公开真实有限筛，不是本稿新算场。

| 有符号有限家族/统计 | 18 原 b/S=1/4 初值 | 19 原 b/S=1/2 初值 |
|---|---:|---:|
| reach | 2.0480426708394406 | 0.9684249942095058 |
| body_diameter | -0.04304843011978521 | -0.038135527545650194 |
| distance_plus | 0.11871374548166669 | 0.005863061771032241 |
| distance_minus | -3.0936337267043594 | -3.0936337267043594 |
| cap_diameter | -0.06715131487906445 | -0.06715131487906445 |
| height_floor | -1.0411715967426867 | -1.0411715967426867 |
| 原 Phi | 4954.71485872585 | 3825.0583894874153 |
| 原有限最大 Gram 残差 | 0.6374168330977955 | 0.6460503011117507 |

reach 与 distance_plus 仍正；另外四族负。Phi 下降和最大 Gram 残差上升同时出现，已经足以排除“所有指标随 b 同步改善”的叙述。这些是两种 seed model 的真实初值观察，没有给出 b=5/8 或 3/4 的结果、极值位置或连续证书。

本分析期间根另已读到 19 第一个 trial d761b5f4d54d681b81d3ad56297f2858b65022dd8416a783efda6a8afc7f10ec 的统计 Phi=3825.0583176123996、Gram=0.6460503022350718。这里仅记录根提供的已返统计，尚无该 trial 的几何或接受决定；不能把原初 g 赋给这个点。它也不改变下文的参数尺度分析。

## 2. 5730 的 reach 与 distance_plus 究竟测什么

完整 geometry 的 scan 先读原当前网格、历史额外网格和永久位置并集，取两支 principal curvature 的绝对值最大值 K，以及其实际查询集的最大点范数 Rmax。源码计算

$$
D_{\rm point}=\max(2,\ 2|H|,\ 2R_{\max}),\qquad
p_{\rm reach}=0.03D_{\rm point}K,\qquad
g_{\rm reach}=p_{\rm reach}-0.992.
$$

K 的长度量纲为倒数长度，D 为长度；乘积及 g 无量纲。0.992 是原数值 safety 值。g 既不是 K 的相对误差，也不是对实际 reach 本身的测量。19 的原乘积为 1.9604249942095058，仍须降至不超过 0.992 才能通过这一项有限必要筛。因 D 也会随整个场改变，不能把这个缺口全部归为 K 的变化，更不能从 g 推出极值属于哪一个 seed 区域。

完整结果中的 complete=True 表示这次声明的有限查询已经完成；passed 则要求六族最大 g 不大于零。两者均不支付连续覆盖、准确 root/求积误差或整闭面 reach。

令原幅度预算为 B、见证距离预算为 Lw，r0=1+sum(core)，源码的点家族是

$$
g_{\rm body}(F)=4|F|^2/B^2-1,\qquad
g_+(F)=1-|F-(0,r_0,0)|^2/L_w^2,\qquad
g_-(F)=1-|F+(0,r_0,0)|^2/L_w^2.
$$

distance_plus 取全部已读点中 g_+ 的最大值。因此它为正表示最近的被筛点仍过近；其下降不等于全场直径下降。19 的 g_+=0.005863061771032241 接近零，但没有位置资料时不能把它归因于端层、中央段、两个支持之间的补集或帽附近。改 b 会改变整个支持的累计积分，补集中的位置也可移动，不能借 profile-only 的局部化结论预测 distance_plus。

## 3. 三个 b 的准确定义与两种相反的尺度

ad52 的两个固定支持为 [1/32,15/32]S 和 [17/32,31/32]S，总长 L=7S/8。四个端层总长为 b，每端长 b/4；每个中央段长

$$
\ell=(L-b)/2.
$$

profile 参数 δ 与端层宽度 b/4 是两个不同参数。本节 δ 恒为 1/32，cδ=1/4−δ=7/32。

| 精确定义 | b/S=1/2 | b/S=5/8 | b/S=3/4 |
|---|---:|---:|---:|
| 每端长度 | S/8 | 5S/32 | 3S/16 |
| 每中央长度 ell | 3S/16 | S/8 | S/16 |
| 中央总长 Lc=L−b | 3S/8 | S/4 | S/8 |
| 第一中央区间（除以 S） | [5/32,11/32] | [3/16,5/16] | [7/32,9/32] |
| 第二中央区间（除以 S） | [21/32,27/32] | [11/16,13/16] | [23/32,25/32] |
| 冻结其他量时，显式端层 1/b 项相对系数 | 1 | 4/5 | 2/3 |
| 固定 δ 下，准确中央 max|Fss| 相对式 | 1 | (3/2) lambda_5/8/lambda_1/2 | 3 lambda_3/4/lambda_1/2 |

最后一行对每个对应角度比较准确 seed 的径向二阶量。R721 给

$$
U_c=\max_{\rm central}|F_{ss}|=\frac{\lambda}{c_\delta\ell}.
$$

因此，5/8 若要使这个中央项不增加，需要新 λ 不超过旧 λ 的 2/3；3/4 则需要不超过旧 λ 的 1/3。λ 是完整新 mean 半径经严格递减 Aδ 反解得到的量，不能当作不变常数。更大的新 r 才可能使 λ 足够下降；原两个 g 最大值没有提供这个信息。

端层收益亦带条件。R721 的完整归一化转向项包含 cutoff 导数与真实 blend 分母；只有在共同方向夹角、非零分母和参考导数界下，显式 1/b 成分才能按 4/5 或 2/3 缩小。新增 b 改变 d、d 的角 jets、整个 B 和分母，因此这两个系数不是实际 K 的预测。

Uc 也不是一般 principal curvature：完整 Gram、法向、混合项、Fphiphi 和切面积都参与 K。即使知道中央 Uc 升降，也不能替代 5730 的原完整两支曲率计算。

## 4. b=3/4 不触发一个预先可判的非法定义，但 mean 域变紧

源码的准确定义只要求 0<b/S<7/8、0<δ<1/8。5/8 与 3/4 都严格在内，所有中央区间非空。本次读取的定义与工作算法没有给出一个仅由这两个 b 值就触发的非法或非存在判据；这不是已经证明任意角 root 存在。

真正的方程为

$$
L_c v+B_b(Nv)=K,\qquad d=Nv,\qquad r=|v|,\qquad A_\delta(\lambda)=r.
$$

改变 b 时固定支持补集不变，准确 K 由原 core、cap 与 U 外积分决定；B_b 的完整积分及 Lc 改变。成功准确解需 0<r<1，以及非零 boundary blend 和非零 projected frame。等价地，K−B_b(d) 必须与 d 同向且其长度 a*=Lc r 严格处于 (0,Lc)。三种 b 的上限依次为 3S/8、S/4、S/8。旧解处于原区间并不保证新解处于缩小后的区间，因为 B_b 和 d 也在变化。

完整 f848 工作算法保持所有三分量 mean Newton、真实 Armijo、全部边层点和两角 jets。初值 v=K/Lc 随缩短 Lc 放大，但没有把 v 裁剪到单位球来伪造合法解。实际 profile 步检查工作正权重完整十二片规则的

$$
A_{\rm work}(\pi)<r<A_{\rm work}(0),
$$

再执行原 64 步上限内的完整二分，并同时检查 scalar 残差和 B+Lc A(lambda)d−K 的物理闭合残差。实际端点数值不能未经读取替写为准确的 0 和 1。

已有 R709 粗充分条件 k_++2b<L 在 b/S=1/2 时就不可能成立，因为 2b=S>7S/8；它在另两候选同样不能成立。这只表示该粗充分估计不适用，并不证明 mean 不存在，也不是程序新增的拒绝门。当前后验存在、角 jets、normal 全 32 段与全域误差仍各按其已刊完整合同支付。本稿不把某次 working Newton 成功冒成全角准确证明，也不复写 R722。

## 5. 联合改变 profile δ 的有限作用

若仅为减轻中央径向项而考虑同时减 δ，R721 已给固定准确 r 和 ell 下 pδ=lambdaδ/(1/4−δ) 随 δ 严格上升。因此减 δ 会降低 Uc，但会升高该定理中的 max|alpha_ss|，窄 ramp 的原完整求积与误差责任仍在。

另有一个直接边界可防止把这个旋钮当作任意补偿：固定新 b 及其准确 r，将 1/32 降为任意 0<δnew<1/32。由 R721，lambda_new>lambda_1/32，且 c_new<1/4，故

$$
\frac{U_c(\delta_{\rm new})}{U_c(1/32)}
=\frac{\lambda_{\rm new}}{\lambda_{1/32}}\frac{7/32}{c_{\rm new}}
>\frac78,
$$

而其小于 1 另由 R721 的完整 pδ 单调性得出，不能由两个因子分别单调草率相乘推出。也就是说在这个固定 r 的比较中，单靠减 δ 的中央项收益小于 12.5%。

若再作“两个 b 的 r 恰相同”的条件比较，5/8 的长度压缩即使叠加这种 δ 调节，仍有大于 21/16 的中央尺度下界；3/4 则大于 21/8。这是条件代数，实际 r 随 b 未知，不能拿来断言实际场一定恶化。它足以说明：不应在没有新 mean 资料时宣称“把 δ 调小即可抵消中央压缩”。当前建议保持 1/32，以便下一独立 width 比较解释清楚；本稿没有选联合参数。

## 6. 原 321be 已经保存了什么，可以不多算场就读出什么

10fa 将小观察文件写在 outdir/actual-mathematical-progress.json。321be 的 _geometry 只投影原 scan 返回对象，没有任何新 F/J/root 调用。

以下对象拥有同一组几何字段：

- initial_geometry；
- current_geometry；
- latest_trial_geometry；
- last_completed_trial.geometry（已返 decision 后保留，下一 trial-start 不清空）。

| 对象内精确 JSON 键 | 含义 |
|---|---|
| point_sha256 | 这次返回对应的完整控制向量摘要，不是空间位置 |
| recorded_geometry_point_sha256 | 原 scan 自己记录的完整点摘要 |
| recorded_at_utc、state、complete、passed | 真实观察时刻/事件与有限返回状态 |
| physical_g_by_family.reach / body_diameter / distance_plus / distance_minus / cap_diameter / height_floor | 原六族有符号 g |
| maximum_physical_families | 六族最大值的所有精确并列者，按原族顺序以竖线连接；不猜 ties |
| necessary_reach_product | 原 0.03 Dpoint K |
| maximum_absolute_principal_curvature | 原有限两支绝对曲率最大值 K |
| diameter_point_lower | 原 Dpoint |
| current_height | 该实际点的 H |

这些字段在程序中已经存在。当前 48 live 选择表未全部选出 K/D/乘积/alpha，不能据“未显示”说原程序没算或没存，也不能据 source 字段存在倒填实际值。

每个真实 trial-decision-returned 后，_preserve_completed_trial 另写一个严格小于 16,384 B 的 runner 标量文件：

`outdir/completed-mathematical-trial-scalars/trial-%06d.json`。

其根键包括 point_sha256、phase、serial、index、alpha、accepted、actual_seconds、statistics、geometry。上表几何值在 geometry.*。最新真实文件的路径、字节和 whole SHA 在活文件 last_completed_trial_record.{path,bytes,sha256}。文件编号是已观察 decision 序号；只有源码写入成功且该 record 真存在时才能称有此文件。它不是完整科学 checkpoint，也不是跨 runner 可复用的 immutable 全场。

这两类小文件都没有保存 worst 的 cell/u/s/phi、空间 F 坐标或两支 signed K。不能从 full-point SHA 或 family 名补出它们。

完整 report 原本保留以下路径：

| 完整对象 | 可读位置 |
|---|---|
| 初始 | initial_geometry.worst；initial_geometry.amplitude.worst_by_family.distance_plus |
| 每方向父场 | restoration_directions[i].starting_geometry；metric_directions[i].starting_geometry |
| 每 trial 完整几何 | restoration_directions[i].trials[j].full_geometry；metric 同结构 |
| 已接受方向 | 相应方向 accepted_geometry |
| 最终 | final_geometry |

在任一个完整 geometry 对象 G 中：

- G.worst 含 cell、u、phi、branch；当前网格极值还带 stage、angle、s。历史额外网格或显式位置并不保证带 s，不能假填。
- G.amplitude.worst_by_family.distance_plus.location 含实际 cell/u/phi，其 physical_g 是对应最大值；body_diameter、distance_minus 同结构。
- G.permanent_point_records 含每个实际并集位置的 location、signed_principal_curvatures（两支）、radius、area、三项 amplitude。按真实同一地址匹配可恢复已记录两支 K，不需新场读取。
- G.farthest 对应实际有限 Rmax 位置，不能与曲率 worst 混成同一点。

10fa 在初始完整读回之后 save_report，也在整个方向结束之后 save_report；每次 trial-statistics 或 geometry 返回不会立即保存完整大报告。初始完整 report 因而可含初始 witness；尚在当前方向中而未保存的 trial 完整对象，不能仅凭未来报告结构说已公开落盘。当前 d761b5 只有统计已知，几何/decision仍未知。读取已经有的这些对象只需原有只读路径，不能为了字段存在而额外调用 F 或在运行中换源。

## 7. 已有 mean 报告同样给出可区分风险的真实字段

若原完整报告自然保存，已完成 mean 批次在

`latest_operator_metadata.base_complete_metadata.fixed_supported_unit_seed.mean_batch_records[i].metadata`。

已有以下准确键名对应工作读数：

- actual_minimum_mean_radius、actual_maximum_mean_radius；
- actual_boundary_minimum_normalization_norm；
- actual_minimum_projected_radial_norm；
- actual_minimum_negative_amplitude_derivative；
- minimum_actual_d_z；
- maximum_actual_amplitude_residual；
- maximum_actual_combined_physical_closure 以及 phi/phiphi 两个闭合残差。

批次另保 literal_angle_hex 的完整顺序、seed_model_identity_sha256 和原 runner_raw_arrays/runner_raw_report 文件记录。λ 及其两角 jets 的实际数组在对应原 NPZ，不能把若干角或一个 batch 的 extrema 冒成完整连续角域结论。本稿没有读取这些 raw 数组或假填其当前值。

这些资料若已由原计算产生，可区分“端层 blend 接近零”“mean 半径接近 profile 域边界”“profile 反解导数小”等真实机制；即使还未有自然返回，也不妨碍作出下一输入的有条件选择。它们不是新增准入条件。

## 8. 实际推进建议与 same-source 续跑的不同含义

下一次若要仅改变 width，5/8 比 3/4 保留更宽中央段：它以显式端层系数 4/5 和中央系数 3/2 作权衡，后者则是 2/3 与 3。结合已知 bquarter→bhalf 的真实 reach/distance_plus 改善，这使 5/8 成为有充分源码理由的较温和下一独立尝试。现有证据没有给出二者的实际排序，也没有保证 5/8 会过零或 3/4 一定更差。若真实初始 worst 后续明确在端层且 mean/ramp 余量充足，3/4 的更强转向收益才有更直接的归因依据。

此建议不改变 19 的 .01 或 20 的 .001 恢复阻尼，不同时选择新 δ，不生成新 ready，不丢全预算。新的 b 会改变完整 seed model，所以不能在原 same-source restart 检查里把 b 偷换，再称继承原同 model final。

另据根请求核了现有 f600/10fa 的原续跑边界：它们支持真实 complete=True report 加同 SHA 的 final.npz；强核同 driver/schema/model、fixed profile、carrier，完整 b8af 再核整 representation 与 inherited typed/地址/未知 peer 责任。独立 branch flag 与五组 pending CLI 不能同 restart 混用，旧 pending 责任则从真实父报告保留。

必须区分续跑参数与执行状态：10fa 在新初始重读后仍明确执行

`damping, restoration_damping = args.damping, args.restoration_damping`，

并从零开始本次方向计数。它不会自动把父 final_damping/final_restoration_damping 载入这两个局部变量。若采用原 .01/.001 的完整 CLI，这是同场接续的新完整预算；若参数方案要继承父末 μ，须在真实父返回之后读取真实末值并显式传入。完整父值未知时不填，程序也不把 accepted-only 文件或活 packet 当成 complete final。

## 9. 全文读取来源身份

以下为本稿实际使用的完整源/证明身份。运行体未修改；所有 source 引用在当前完整族的原职责内，证明不作为另一个执行步骤。

| 完整来源 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| [so3_fixed_fejer_batched_missing_angle_geometry.py](../scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py) | 88163 | `5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135` | `c5325d3da8329547ad81e74a5da479323bfccd21` |
| [fixed_fejer_supported_meridian_reference.py](../scripts/resume_20261126/fixed_fejer_supported_meridian_reference.py) | 39771 | `ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a` | `ad7f2d9ea2e63df16d900cf12885d611fef5d823` |
| [supported_smooth_triangle_seed_mean_jets.py](../scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py) | 34725 | `f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917` | `ee318b8971ce3c3d10715fbcd648c3a3bcfd6712` |
| [fixed_fejer_complete_geometry_trial_progress.py](../scripts/resume_20261126/fixed_fejer_complete_geometry_trial_progress.py) | 39500 | `321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5` | `8173d3576958dc5c476466dd4c5012c5ed81b0c1` |
| [fullclosed_fixed_fejer_meridian_batched_so3_qp.py](../scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py) | 99313 | `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f` | `8bba3e30bb8e843fd725a2d19f8966b984acc4ae` |
| [fixed_fejer_supported_so3_meridian_operator.py](../scripts/resume_20261126/fixed_fejer_supported_so3_meridian_operator.py) | 40840 | `552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3` | `1d9e435bb68374b71c3d7361771c28f47838d59e` |
| [fixed_fejer_detached_meridian_normal_lift.py](../scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py) | 96276 | `76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d` | `fc51c16b6dbd53abf04fe9175e5421f77e25c49c` |
| [launch_fixed_fejer_meridian_batched_actions.py](../scripts/resume_20261126/launch_fixed_fejer_meridian_batched_actions.py) | 22136 | `f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506` | `168b1a1d7bc58793985138eb8a02a6e3911d74cc` |
| [fixed_fejer_meridian_memory_transfer.py](../scripts/resume_20261126/fixed_fejer_meridian_memory_transfer.py) | 78920 | `b8af97a4772e5d641c5daea3f2232c65fe52055154d94e45b4c88f661e9778dc` | `2e112909d6937363ad0a643a2acbc1e54f7d8bcd` |
| [R721-supported-seed-width-and-profile-sensitivity.md](../results/R721-supported-seed-width-and-profile-sensitivity.md) | 24655 | `14a0b6205f89fa68e5ec04de5960ca19859fccfebac015e01fadb02f75c7363a` | `ccbe166c7ee811135ead5c4ce782f99278a8197e` |
| [R709-global-convex-mean-closure-without-contraction.md](../results/R709-global-convex-mean-closure-without-contraction.md) | 15645 | `0899ae28564b64468c81746d2543f1ab4d4ed455b2752af0d3e46be8fceba830` | `afd3a16e98bb7c1b3c8b911bc50b656263f51bd5` |

本稿只新增这份来源分析。准确 g、根、全场、连续几何与接续执行的实际返回仍由各自原完整入口记录，未以本稿补成完成。
