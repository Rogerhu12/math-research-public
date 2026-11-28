# H96：原完整 96 列 trial 的高度与消高 phase 公共入口

2026-11-28，visible-exact-astra-b0d5a16-20261128 / alternative_route。

这是七个**新完整目标**的执行契约，不是已完成的 actual 数值结论。
同一原 selected member、固定 metric/eta、原 true-root TC 试验及其 96 个
输入坐标保持不变。所有结果仍属于该固定有限 trial；不能把它们记成已
完成 true PDE correction、完整 regular/Theta inverse 或最终 Schur。

## 完整目标顺序

| 次序 | 完整目标 | 条目数 | 保存约定 |
| --- | --- | ---: | --- |
| 1 | `complete_same_selected_TC_canonical_height_row96` | 96 | 全 signed balls |
| 2 | `complete_same_selected_TC_waist_Jacobian_L2_upper96` | 96 | 全 upper balls |
| 3 | `complete_same_selected_TC_reference_height_row96` | 96 | 全 signed balls |
| 4 | `complete_same_selected_TC_actual_cap_height_row96` | 96 | 全 signed balls 与 96 个 exact dyadic centres |
| 5 | `complete_same_selected_TC_actual_cap_height_joint_radius` | 1 | 对上一整向量相同 centres 的 joint upper |
| 6 | `complete_same_selected_TC_height_reduced_phase_row96` | 96 | 全 signed balls 与 96 个 exact dyadic centres |
| 7 | `complete_same_selected_TC_height_reduced_phase_joint_radius` | 1 | 对上一整向量相同 centres 的 joint upper |

每个新向量是一个自然完整目标。单个 entry、单个原 cell 或一个偶然成功
的积分片段不能另算完成目标。每 8 个完整 RHI cell 保存全部 96 个积分
累积量、已接受区间及全误差；每个目标先完整写入并读回，再允许后继消费。
真实失败保其完整 accepted prefix，不自动重试。

## 同一输入球和完整载体

原 P96 run `45926971089/1` 的 actual/execution 与完整 manifest 一起准入。
直接消费其整个 `complete_same_selected_TC_phase_row96` 和
`complete_original_TC_negative_trial_L1_L2_upper96`；旧 phase169 germs、
原 phase transport、旧 L1、残差或 pairing 科学目标均不调用。

原 RHI run `45933988440/1` 的 actual/execution、完整四目标与所有 profile
误差一起准入。RHI/NP/SB 原准入和 P96 原准入均完整执行，保留共同的 51
件历史 native 输入、40 个原 row parts、7721 行及全部原 source SHA。
历史 index 保原 basename/相邻目录；不展开未使用的 phase169 载体闭包。

必要载体恢复遵守原配方：

1. 原 P96 restore 恢复四个完整 `7671×193×96` TC 数组，共
   `4548105216` bytes；逐一核原 whole SHA。全 6144 段 base offset 链及
   7724 个 TC certificate cells 的原身份一起核验。
2. 原 NP restore 恢复四个完整 `740×193` 数组并核每个 whole SHA。
   TC 全 offset 中的原 NP/RHI 前缀再核原 signed offset sequence SHA。
3. 原 RHI restore 的全 18 状态、2847 个原 ordered cells、终态及整条 SHA
   链都不变。唯一 AST 修改是在原 `proposal` 返回后插入只读 observer；
   没有替换任何旧系数或浮点递推。
4. observer 将每一格原七个 chosen degree6 coefficients 的 A9/x3 部分
   写入作业私有 `2847×7×2048×12` memmap，`3918200832` bytes，按原
   `rhi.full_plan` 正向索引。多项式变量始终是
   `u=(right-r)/(right-left)`，不能把它当成正向变量。
5. 原 `2048×18` 全终态 SHA 和 2847 格全 ordered chain 必须与 RHI actual
   一致。新 cache 只公布 whole SHA、shape、bytes 和 receipt chain；不向
   git、artifact 或 Release 发布任何数组。

此恢复只重建已指定科学输入，不运行任何旧 RHI residual/strip/mean 目标。
TC 与 cache 共约 8.47 GB；私有磁盘上限 12 GiB、RSS 上限 16 GiB，完成
映射写入后 flush 并释放不需要驻留的页面，不改变任何文件字节。

## 全频误差与新的有限配对

新的数学证明和 kernel 是
[H96 proof](../results/R149-supplement-complete-height-row-on-original-finite-trials.md)
及 [H96 math](../scripts/fourfold_codazzi_finite_trial_height_math.py)。
原 1024 context 不变；新 kernel 独立使用 8192 context，完整有限支持上界
3584，且 `2×3584<8192`。原 2048 Nyquist real coefficient 各半置于
`+1024/-1024`，与原 real cosine Nyquist convention 完全相同。

RHI 末完整 grid error 单调支配每一原 cell 的 whole-cell error；原累积
strip bounds 同样支配全区间。原 profile alias 的 Fourier tail/aliases
绝对和也给 C0 界。实插值 Parseval 范数不大于 normalized grid l2 范数，
再由 2049 个完整复指数及 `sqrt(2049)<46`，得到统一 `EA<1.3e-7`、
`EX<6.6e-8`。这两项是无限角支持的 C0 error；新 primitive 付 `2/5`，
没有把 unknown error 塞进有限 trial 的次数或借用 Wiener 的 `1/4`。

完整 adjoint 先形成再和原 trial 配对。两个 moving means、physical
coordinate term、完整 waist Jacobian 变分及原 reference/actual-cap 费用
保留。完整 `Y_b/K_b`、其他几何 impulses、mean 和剩余 Schur 方程独立。

## 文件与执行状态

新增 owner、carrier observer、public worker、manifest generator 分别为：

- [owner](../scripts/fourfold_codazzi_finite_trial_height_owner.py)
- [carriers](../scripts/fourfold_codazzi_finite_trial_height_carriers.py)
- [public worker](../scripts/fourfold_codazzi_finite_trial_height_public_worker.py)
- [manifest generator](../scripts/make_finite_trial_height_manifest.py)

四条旧 whole-input admission 已静态通过；worker 的完整 RHI AST 继承和
唯一 passive tap 已编译检查，`numpy/flint/scipy` 本地导入数为 0。
新 math 所需全部 bundle keys 均由 owner 完整供应；公开 worker 不含
`phase_input_plan` 展开分支，native 历史路径保持原名。九项新 Fraction
比较由根代理首算一次全过，入口生成未重算它们。

完整 [manifest](2026-11-28-finite-trial-height-complete-inputs.json) 为
`61916` bytes，whole SHA256
`0bf3e4abe612c744cba56cfb2161528cb34171351414885d2761349e61a70073`，
`114` current inputs + `51` historical inputs；`--check-only` 已通过。
工作流是 `.github/workflows/visible-exact-finite-trial-height-complete.yml`，
沿用原不可变 Python container、Python 3.12.14、NumPy 2.3.5、flint 0.9.0、
Haswell 和单线程配方。科学预算 18000 秒，child timeout 18600 秒；真实
partial prefix 保存为不完整结果，不改记完整目标。公开 scientific 和
execution 各至多 99000 bytes，整次 publication reserve 为 210000 bytes。

实际新目标只在公开 Actions 运行。根代理在本条对应提交统一发布新workflow，首次push触发唯一运行；
实际run及后继状态见HANDOFF，此文不宣称 actual 数值成功。
