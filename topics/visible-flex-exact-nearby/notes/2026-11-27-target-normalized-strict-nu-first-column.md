# BNC 首次真正归一参数列：完整执行合同

2026-11-27，visible-exact-astra-fb31ed6-20261127 / trial_restore。

本文是 [BNC proof](../results/R147-supplement-target-normalized-strict-parameter-column.md)
的首次公开 Actions 实现合同。发布这些源码时尚不据正在运行的 DWTB
进度制造成功；只有原 DWTB 全九目标的 actual 与 execution 均完整，
metadata generator 才能生成唯一 first-entry manifest/workflow。

## BNC-I1. 原对象及真正新目标

目标保持
\(E_{96}^{a*}\mathcal B^{-1}\mathcal L_\partial\mathfrak D_0v_\nu\)，
其中 \(a=2\mathcal H(0)=b-\Omega\)、\(\mathcal B=Id+\mathcal T_w I\)，
\(\mathcal T_w\) 是原 same-sign Toeplitz。\(v_\nu\) 是原 NP strict
particular，不冒称已满足完整 homogeneous waist matching。

全部192个新 complex observations 使用完整8192点、NP 的全部96个
physical half-sum source modes，以及完整未平移的
\(G=K_{48}\circ H_{24}\)。它们并非旧 physical96 observations 的重跑。
完整96行 contraction 同时保留 conjugate negative modes；新 signed
centers 直接按原 exact rational row carrier 作有理求和。

七个完整自然结果依次为：

1. 原 true B row joint error 作用于原 NP 完整 physical trial 的 fee；
2. 原完整 true receiver 作用于 ASB short waist PDE error 的 fee；
3. 完整 G/H homotopy 的 joint composition fee；
4. 全部无限 trapezoid aliases 的 joint fee；
5. 全192个 observation disks 的 joint rounding/input-radius fee；
6. 五个正式读回完整 fee 的总 joint column error；
7. 完整96个 exact signed centers、true signed balls、joint \(l^2\)
   资格，以及原两独立 mean balls 的一个完整 signed column object。

这不是逐行增加 \(\sqrt{96}\) 的做法。该因子只出现在已证 true
receiver norm；BR 行误差和 composition/disk 联合项不再付行数损失。
\(J\) 是 DWTB 已成的完整 \(IY\) Hilbert--Schmidt bound，
\(N_0\) 是 PO 已成的完整 physical polynomial norm，均不重新归约。

## BNC-I2. 所有原前驱与完整输入绑定

以下 actual/execution/manifest 整对象必须被读取并准入：

| 前驱 | 原 run | 必须保留的完整结果 |
|---|---|---|
| NP | 45893562391/1 | 两完整目标，194 true balls、192 raw trial pairings、四完整数组定义 |
| PO | 45903437912/1 | 十二完整目标，原 even nonmean polynomial norm 和原完整观测逆资格 |
| ASB | 45908403884/1 | 十一完整目标，尤其完整 short waist density error |
| JC | 45887337009/1 | 通过 PO/NH 既有准入链读整个七目标及原 W/H/K |
| DWTB | 生成 manifest 时指定的完整原 run | 原九目标、2048 signed w、96完整192-mode行及全部2240 residual 支集资格 |

新输入仍保全部 NP 原51个历史原件：40 whole native radial parts、
完整 centre index/五片、原 repair、四个 W/R31/H/K definitions。
DWTB 原 source/SN/ASR closure 完整继承。源码没有添加对旧 native
科学 producer 的调用，也不删除原两 mean、原 reflection 或原 implicit
selected-member 身份。

共享文件按完整 path 去重，每份原 parent manifest 保持原字节。
新表中的 descriptor 与每份原 descriptor 除 role 名外必须一致；
唯一允许加强的是四个 PO shared native 的
`restore_only:true`。新表保这个 true，所有原 byte/SHA/Git blob/
commit/indices/encoding 约束保持。因此可以完整恢复每份 parent
输入表，不能通过去重删除旧约束。

generator 只读全部 current texts、完整 parent actual/execution 及
全部 native descriptors，核 UTF-8/AST/bytes/SHA/whole target schema。
真正的51个原 native 字节及既有 NP/PO/ASB/DWTB metadata admission
在公开 worker 的 target reservation 之前完整执行。随后才允许唯一
新的 numerical child。manifest 未满足 whole DWTB9 时不生成。

## BNC-I3. 必要 carrier 恢复与旧目标禁重

SN 原 endpoint/raw192/grid8192 用 DWTB 同一严格原 prefix 恢复，
停止于旧 alpha quadrature 之前。该子进程保原 `CORETYPE` unset；
所有 Python/container/library/thread 版本与原成功 recipe 相同。

新的
[fourfold_codazzi_target_B_row_carrier_restore.py](../scripts/fourfold_codazzi_target_B_row_carrier_restore.py)
只恢复原 DWTB signed **input**：

- 全8192个原 unit-disk input 的原 whole SHA；
- 全2048个原 exact signed w coefficients 的原 whole SHA；
- 原 \([192,96,2]\) binary64 trial 和其完整选择记录的原 whole SHA；
- 原96个完整192-mode rational row polynomials 的原 whole SHA。

它只调用必要的 point/disk reference 及原 deterministic proposal。
不调用 DWT mode-error reducer、DWT 两 whole scalar、BR finite
residual 或 BR 七 norm/error targets；不恢复旧 alpha carrier。
任一原 whole hash 不合即真实失败，不能改成另一个 trial。

NP 恢复直接复用已经公开的
[fourfold_codazzi_strict_nu_trial_carrier_restore.py](../scripts/fourfold_codazzi_strict_nu_trial_carrier_restore.py)：
四个 \([740,193]\) 完整数组、原 node/plan/offset 身份及其原 SHA
全部匹配；不执行旧 residual、pairing、norm、QR 或 direction。
两类 proposal 恢复都保持 Haswell 和六线程变量各1。

physical half-sum 使用 BNC.4。\(K(0)\) 复用原 TC/NP point polynomial
algebra 在真实 waist 的值和完整 error，而不以更宽 whole-cell K
interval 代替；selected mean 使用原 NP 完整 signed ball。这里
没有重新产生任何 intrinsic scalar enclosure，也没有选取 numerical
selected state。

## BNC-I4. 新 quadrature 的完整持久前缀

原 private carriers 完整接受后才形成新的 physical source/G grid。
所有8192个 directed values 写入 private 文件并完整读回，然后保存
全部 exact dyadic raw/phase centers 和 whole disk radii。

192个 observations 按自然 mode 顺序各自保存完整 point/radius/input
身份。输入具有精确 unit-circle phase；BNC.13 为其全部幂误差支付
半径，避免旧 rectangular power 包裹。每16个完整 modes 更新可见
prefix；prefix 不冒充整个 signed column。全部192个完整行记录读回
后，才形成96个 exact rational signed values，再分别保存完整五项 fee、
总 fee 和最终 signed object。

true physical column 仍有无限 Fourier tail。全解析 alias fee、
完整 G/H difference、非等距 \(B_H\) 与 homotopy Jacobian m 都保留。
原 finite row 的真正 phase error 已在 DWTB 的 \(e_R\) 中。
两 independent mean balls 作为既成独立记录原样保留，不称其已完成
非局部 physical-height 或 phase matching。

## BNC-I5. 公开小结论与可恢复的执行绑定

原大 carrier、grid、四 arrays、192×96 row coefficients、
mode disks 等可重建输入全留 private。公共实际文件只含新七个完整
结果、必要 whole SHA/bytes、原完整 scalar records 和状态。

执行 receipt 的 current inputs 用下面的**无损引用**保存，避免在
执行文件里重复约180个已经完整写在 manifest 的 descriptors：

`{"reconstruct_from":"whole manifest.files","manifest_sha256":...,
"complete_count":...,"complete_descriptors_sha256":...}`。

最后一个 SHA 是 canonical whole `manifest.files` 的 SHA，而非
选取的子列表；每个 current input 的原 bytes/SHA/Git blob/path 都在
同一 immutable manifest 中可恢复。51个 historical bytes restoration
receipts 仍逐件保留。不能用这项编码把未校验的输入计为已消费。

当前源码、proof、notes 各自小于100KB；generator 会拒绝达到100KB的完整 manifest，
topic继续受200MB和reserve约束。worker 每次 pull 后核两README，
非快进立即实际 pull/rebase 后重推，current source snapshots 从 Git
objects 取出且统一使用 `input_role.ext`，防止 sparse pull 及
`math.py` 遮蔽标准库造成旧故障。

本条不声称 homogeneous96 inverse、high incoming elimination、
非局部 phase、physical mean-height matching 或 full Schur 已成。
它补的是原 bordered system 中一条真正经过 \(\mathcal B^{-1}\) 的
完整有限 \(\nu\) 列；实际结论必须等唯一公开首次执行的 whole 输出。
