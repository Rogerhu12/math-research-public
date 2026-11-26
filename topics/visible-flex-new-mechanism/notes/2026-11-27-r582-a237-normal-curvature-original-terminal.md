# a237 全闭连续几何：R621 原终态与实际剩余曲率瓶颈

日期：2026-11-26 UTC；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

**这是唯一原 Actions 运行的完整终态收据。** 同一真实 a237 参数与原
common-endpoint Hermite 材料已取得全闭嵌入及正 reach 的连续充分证书，
但认证的 `reach/D` 仅为 **`0.007183367225307948`**，未过 `.03`。
全部 radial / angular / core / cap 覆盖完成，不能把未过目标归因于漏查
区间，也不能把较宽的曲率上界 `86.9811818809665` 宣称成实际曲率峰或下界。
本记录不支付固定 g 精化、宏观振幅或主 README 完成门。

## 唯一运行与原字节身份

- run [45895935112](https://github.com/Rogerhu12/math-research-public/actions/runs/45895935112)，job `140169696746`。
- 触发提交及 public 实际 pull 都是
  `ac528e756d9e8f601f9a2c2a8623e2f77c212d94`。
  两份公开 README 与已读 blob 匹配且差异为空。
- private 实际 pull 为 `a5e143524f7f9c09865e9e276a1d90eeefc529c4`，根 README
  匹配，QUEUE 唯一且认领为本会话进行中。
- 实际 driver `scripts/r582_a237_normal_curvature_reach_20261127.py`，
  23,122 B，SHA-256
  `577211e39b11d3102cee6154bd209ada0a41a6138bedb7c69a56a67ca6f911ae`。
- request 18,337 B，SHA-256
  `a156c7f369a0a64aa2ba60221ea4255c7c583c1f04ccb6122667ac4091110fe2`；
  lane `actual-a237-normal-curvature`。
- job `21:07:41–21:19:21 UTC`，Actions conclusion `success`；科学子进程
  `21:08:10.412259–21:19:17.194644 UTC`，returncode 0。
- 新科学 **`665.7533184509999` 秒**；FINAL `failure=null`。
- 完整原 stdout **182,044 B**，SHA-256
  `efc8b74fa6db80a635ac36e969c1e4d0c1edb3ead7700bd06c8b2c622a2659f7`。
- 逐字原 FINAL JSON **18,157 B**，SHA-256
  `fe8bf5e7b9051907a80bfa76799d680fb19128bb45df15e7976cd292a9f4b431`。

已完成 job 的日志只下载一次。后续本地工作只有原日志 / JSON / hash
解析和纸面解释，没有重新执行原 interval、ODE、mean、FFT 或 optimizer。

## 同一个真实 q、材料与比较圆面

唯一实际 97q binary64 SHA-256：
`a2377220dacda9eefe63f25a2000441f0169a0db5de9bc23840f90e5037a895e`。
固定 `p=.181`，原四个完整 Fourier 模式及全部 16 个尾部坐标保留。
62,878 个共同端点及其所有 stored two-jets 的材料 mesh SHA-256 为
`0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`。
它与原实际保留 q 所用 seed 材料身份严格相同。

这里的有限 C² 材料是“全部 stored binary64 端点 jets 作为准确实数所定
共同端点 quintic”，使用同一多项式及它的真实一二阶导数。它不被冒充为
无穷 DtN 核或 dense ODE 的准确解；zero seed suffix 的准确起点为
`0.8901718420886569`，但非圆完整角场不因此被置零。
解析高度 H 保持完整无限振荡尾，不能用数值 seed 的零 suffix 替换。

比较参考圆面使用 **本次 a237 的全部 16 个 mean 控制与 cap height**
`0.6942718843124706`，圆核心半径仍 `.38`。材料 seed 的原冻结半径商
`design.reference_alpha` 没有改用这个新参考。R611 对象在此只供应准确
共享解析 H；旧 R611 / f1 圆参考的曲率、叶子、rho 或 D 没有转移到本次。

## 新 mean 圆参考已全闭认证

在 compact `[.036, .8840000000000002]` 共检验 **1452** 个区间、接受
**761** 个叶子，0 pending / 0 unresolved；准确 R608 tail-start 的包围是
`[.8839999999999999, .8840000000000001]`，compact 与全尾真实重叠。
原 R608 的所有 mean 系数盒由实际 a237 检查，开核心、上下反射和两帽
按 R599 组合，全部闭面前提成立。

| 全 compact 连续量 | 原向外界 |
|---|---:|
| 最低半径 | `0.2359999999999995` |
| 最高半径 | `0.39394094059237733` |
| 最低实际速度 | `0.6669703017552703` |
| 最低正高度导数 | `5.177120984913564e-18` |
| 最高子午 / 周向曲率 | `16.468393555796123` |
| 完整参考 reach 下界 | `0.06071999999999999` |
| 完整参考直径上界 | `1.5964998139950985` |

曲率最大包围叶为 `[.7129730769230771, .7131769230769232]`。
参考接受叶流 SHA-256 为
`c8379c401ec4452de6c643bd3dc519e7f1cff61706e6a0e69aa6360fe2ff0324`。
高度用 65,536 个 outward Riemann cells；完整 H 积分宽度
`1.817236120027488e-6`，未达宽度目标的容量状态照实保留，仍是有效包围。
无限余尾的 dimensionless 积分上界 `1.001471338609514e-16`，完整 prefactor
在 interval 内相乘；没有以 QUADPACK 误差估计充当证明。

## 非圆全域同次盒读取

初始 **17,805** 个 proof intervals，检验 **44,467** 个区间、接受
**31,136** 个叶子，0 pending / 0 unresolved。完整上下 body、共同材料 z 的
开核心柱、全部 theta、两 Cartesian cap 与轴均覆盖。两帽相同高度 / 半径，
贡献位置差 0、一阶差 0、曲率 0；没有把正宽 annulus 替换成帽盘。

有 **12,878** 个叶子超过精化预算但仍给有效较宽上界；depth / 容量策略
只控制细分，不截掉覆盖、不裁剪结果。此次总容量没有触顶。
接受叶流 SHA-256 为
`bf838cc20311d17f771f2c52dbb70d5533779e24be2eb6503c2a362e534c172d`。

| 已支付全域连续界 | 原上界 | attaining cell |
|---|---:|---|
| C0 位置差 delta | `.0019834139688272357` | `[.42799999999999994,.43106249999999996]` |
| C1 差 alpha | `.020761486451790993` | `[.8692209796197373,.8692215187106758]` |
| 全协变 C2 差 beta | `85.10241767992281` | `[.8695418166556349,.8695421040062525]` |
| R621 实际主曲率上界 K | `86.9811818809665` | `[.8695400925519293,.869540379902547]` |

每 cell 同一遍 radial / angular jets 与 current / reference mean 盒组装供应
全部四界。beta 原样报告但不触发细化，细化由 K 预算 18 及原 C0/C1 预算
控制；没有用 budget 18 作为实际 K。exact rational Hermite construction
共 **17,800** 个实际 material cells，**44,466** 次 Hermite interval queries；
全部 current/reference mean boxes **44,467** 次，其中 compact exact height
query **31,413** 次、解析全尾盒 **13,053** 次。

## 原 R604 的完整结果

原实际 derived constants 是

- `lambda = 1.0207614864517913`，向外包围 `1+alpha`；
- `nu = .020761486451790993`；
- `K = 86.9811818809665`，来自同次 R621 全域实际主曲率上界；
- `d* = .01678620621370151`，以 64 正项 artanh 及其余项和 `3<pi` 保守门支付。

原完整 R604 输出：

| 结论 | 严格原界 |
|---|---:|
| 全闭材料映射单射 / 嵌入 | 已由全近远点对证书成立 |
| reach 下界 | `.011496739620858416` |
| D 上界 | `1.6004666419327533` |
| reach / D 下界 | `.007183367225307948` |
| `.03` 比例门 | 未通过 |

这里近项 `1/K` 已限制最终下界。R622 改长近弦门对应的近项是 `.9/K`；
在完全相同 K 下它不会改善这个受 `1/K` 限制的完整结果，因此没有为
本次旧输入另开新的标量运行。不能混用新 d* 与旧 `1/K`。

## 同一个最坏 cell 揭示的具体剩余项

K-attainer 的已输出同-cell diagnostics 为：

| 诊断 | 原已支付上界 |
|---|---:|
| reference normal 投影 H11 | `85.0907890560436` |
| 完整 H11 | `85.09078905897589` |
| current normal H11 | `85.71324906822436` |
| 同-cell alpha | `.007315196572414145` |
| oriented normal difference | `.007315245505001876` |
| reference 主曲率（两项） | `1.4392275412129125e-5`, `7.988319498031568e-9` |
| reference-normal primitive value / s / ss 分块界 | `1.0537258833485346e-5`, `.029164972111230487`, `339.5052719762898` |
| rotating T difference value / s / ss | `6.705540559308812e-6`, `.018559527708682383`, `216.0488094468951` |

reference-normal H11 与完整 H11 几乎同样宽；本次 R621 投影没有消除它。
这些是 interval / primitive 充分界，不是该 cell 的真实主曲率值。
实际垂直切向分量是 `v/sqrt(1+v^2)`，并非 v。可把它准确分为有限
Fourier 线性项 v 与完整归一化余项 `v*((1+v^2)^(-1/2)-1)`；只对前者
按原模式逐系数除频率，后者及其全部径向 jets 仍须完整支付。不能丢掉
余项而改变实际材料。这个分解可改进对整个垂直分量统一套通用 `pi/2` 的界。
这是本终态确定的后继输入方向，必须先追溯同 q 的全部原系数，并单独
证明和付新的全域 K。原已付同 a237 的参考 rho/D 与全域 delta/alpha
可保持；无需重跑这些已通过门。原材料端点和高度前缀没有保存可直接
消费数组时，必要再生仍作为新费用，不能冒充免费缓存。

## 新费用原样保留

本段科学总数 `665.7533184509999` 秒覆盖全部新 reference、材料、H 与
非圆盒。必要材料再生含 160 个 dense segments、960,944 个 dense RHS、
2,510 个 core-forward RHS、206 个 short-backward RHS、62,878 个共同
端点、62,877 个 residual preparation cells，以及 3,166 次高度 query /
235,893 个 QUADPACK RHS。它们用于定义/重建同一个有限 material，
不是把 ODE 数值误差宣称成已认证零。

原 analytic H interval 积分共 `interval_integrand_cells=131063`。
旧 paid seed / primitive 理论、原旧 7 点失败诊断、旧方向检查、全 fine
扫描和优化 Jacobian 均未重跑。源记录的计数层级有重合，不能把 RHS、
weight calls 和总 elapsed 再相加造成重复费用。既有优化与几何科学账
仍留在完整 source receipt 中。
