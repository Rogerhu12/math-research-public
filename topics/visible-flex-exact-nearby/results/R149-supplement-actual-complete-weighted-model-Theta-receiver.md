# R149 WMA：同一全 Θ 的实际有权误差小于6.957962

**已证明（公开 Actions 的全部14个完整新目标）。** 2026-11-28。
run [46122573619/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46122573619)
在 event commit `47436302c6f3a93899ac10d9f3227112c5a2cb37` 唯一触发；
科学 checkout 是 `43a487c4e92ad89cffac108e1eb8c34c3c73d8ea`。
整个科学 actual 和 execution 都为 `complete=true`，actual
`proved=true`，两 failure 均为 null，child returncode0，未 timeout。
全部14个新目标成功，旧 scientific targets 调用数为0。

沿 [WMT.1–18](R149-supplement-complete-weighted-model-Theta-receiver.md)
的同一隐式 selected member、真 $a,b,\Omega,\mu$、原 model low96
reference1、physical frequency4、原 $\widehat\Theta$ 和全部 infinite
error scope，实际得到

$$
 \boxed{\|\Theta-\widehat\Theta:Y_a^0\to\mathbb R^{96}\|
           <6.957962.}                                      \tag{WMA.1}
$$

原完整850.945862…候选保留；本次整候选选择实际选新 WMT bound。
这是整个 $Y_a^0$ 的同一算子误差，未把原 low96 的约.31698误差
升级为全频。原有限坐标逆 $\|T^{-1}\|<12.588$ 的 scope 也未改变。

## 1. 完整输入与实际证据

| 完整对象 | Bytes | SHA-256 |
|---|---:|---|
| [manifest](../notes/2026-11-28-weighted-model-Theta-receiver-inputs.json) | 45728 | `4913fe4ce57cd579741b65090cd5e6dae22392956545196c888c3061b8974ffb` |
| [actual](../notes/weighted_model_Theta_receiver_ci/run-46122573619-1/actual-weighted-model-Theta-receiver.json) | 12593 | `587ec4c28e521c8b04a85d42fad02bd5a53b4468ac9fdf217206ef40f231e3ae` |
| [execution](../notes/weighted_model_Theta_receiver_ci/run-46122573619-1/execution.json) | 8924 | `1b022e585f9fc30968a3aaaa8167229891ba02e15e8ece1ea010fe317c856cdc` |
| 原完整 owner source | 24753 | `4c2fd770110f67972061f2892e0e3d4770c26b36d08cda4171c24ac129f3f2e6` |

完整139个 current 输入和6个 historical 输入均重新作 metadata-only
全字节准入；原 UACT21 的 admission/whole validator 与本次 WMT14
原 public validator 全部通过。该复核不导入数值库、不运行科学目标。
原 UACT actual SHA 仍是
`17c721993bb6488ec48918c50caf70c84785ca54cb004fbc51d11de1c6eb14bc`。
execution 的 scientific-files 项精确指向上表整个12593-byte actual。

实际 Python3.12.14、numpy2.3.5、python-flint0.9.0、320-bit arithmetic；
原 IR proposal 的 Haswell/single-thread schedule 保持。
科学 wall time 为60.002861930999984秒。完整 job log 保有96条
8192-point/2048-head行的自然进度以及 model head1048576终项，
不是只因 workflow 绿灯而认定目标完成。

## 2. 全部14个正式保存球

以下逐字复制 whole actual，均有 `bound="upper"`；使用时取
整球上端点。第4项是全正 primitive 的 vector strip upper，
第5项是整个 signed residual Gram 的 operator upper，不能改成
某一 column 的 maximum。

| 顺序 | 完整新目标 | 原正式球 |
|---:|---|---|
| 1 | 原全 Y 的 L2 Gram upper | `[386.350155944204232142703950051573971340870160356056513042902 +/- 6.57e-59]` |
| 2 | 原全 Y 的 D1 Gram upper | `[150106.249331164189905275960245652844466583749394147352724372 +/- 3.47e-55]` |
| 3 | 原全 Y 的 D2 Gram upper | `[58289179.7301975403716448476156639188911634647456547463659427 +/- 2.58e-53]` |
| 4 | 全 positive primitive vector strip upper | `[174.422216132060419019733867816479721443834232049151066667900 +/- 2.30e-58]` |
| 5 | 全 D1 residual head Gram upper | `[1.04703724962878076430610379264715818811377601700252932446282e-8 +/- 2.35e-68]` |
| 6 | 全 D1 residual infinite tail upper | `[0.00121517134107129228579556100171729914000441694581856663194095 +/- 3.00e-63]` |
| 7 | 全 D1 true-map error upper | `[42.6942962546708145695459919408586710381830878978425591254354 +/- 2.72e-59]` |
| 8 | 全 true D1 residual upper | `[42.6955114364822583581195951449214262637946741959261378620927 +/- 3.87e-59]` |
| 9 | 同一全 inverse error 的 D1 upper | `[72.7573667178300218637527993534542614387072629647867831791096 +/- 1.99e-60]` |
| 10 | 原 alpha 的 D1 infinite tail upper | `[0.0227117576840476966831738201553760095876819575984389333726638 +/- 1.68e-62]` |
| 11 | 同一 VQ joint D2 error upper | `[56452.9306949965679587052829657756157385112470690187895185511 +/- 2.06e-56]` |
| 12 | 全 model head 的 D1 weight upper | `[0.572088907894758066456568868536698190789473684210526315789474 +/- 3.16e-61]` |
| 13 | 全 model infinite tail 的 D2 weight upper | `[0.000122070196084789195261769045096354392667395908931819027119611 +/- 3.28e-64]` |
| 14 | 同一原 Θ 的 weighted-model joint L2 error upper | `[6.95796177721855460432781304275513671530130860138633360496264 +/- 3.93e-60]` |

最后的整球上端点严格小于有理数6.957962，给 (WMA.1)。
第7项实际主导新的 density D1 residual；第11项仍支付原 full
alpha products 和 finite Bernstein 的完整费用，没有把微小的
head residual 当成完整 true residual。两个 model weight 在正交
head/tail 上按 WMT.18 的平方和组合；原 model rounding 另付。

## 3. 原载体与全新私有输入确实完整

必要恢复只重建原 IR grid/trial 和原 scalar model carrier，
其 whole receipts 如下；旧 IR residual/norm、UACT、AS/SN、
BFP 和 CYA gap 没有重算。

| 原必要载体 | Bytes / 完整范围 | SHA-256 |
|---|---|---|
| IR grid | 407627 / 全4096点 | `74ba633b63b22fff209c2a42cc5bebe66c25ed3acc3e7c8bb7a3c9bc6563ea0f` |
| IR exact dyadic trial | 294912 / `[192,96,2]` | `02ee6051166f1f23139b39984dbd309592c415405620f99982a3972d8dd49db1` |
| 原 model multipliers | 440380 / 全2240 modes | `037354a0b051a4a251e0d4be858e49e897c1b924d2e92b8c7e67c4fad05f4ae1` |

新8192 grid 完整879737 B，SHA
`349e4ae452b349aff6c7c7d98b802cb6f25f6e2008f2bd3d57a219f22e403bc9`。
原4096节点复用；4096个 interleaved 节点新求。
所有96条完整8192 samples 的链 SHA 是
`952049785b1e65511d88030014424982f6d877d71809235fbd380ce121cadd33`；
全部96×2048 head 链 SHA 是
`7ea98ca0aa33a74352b7d1fb6de9f2268f5711e970ca8a94ce724bebbc490b59`。
三个 Y Gram 及一个完整 residual Gram 的全部9216 entries 各自
先保存读回，其 whole SHA 和长度全部在 actual 中。

新 model continuation 保存2241–1048576的全部1046336条 signed
denominator/reciprocal/weight records，完整 gzip 为76096772 B，SHA
`950ce3eada70b3ff079847fd9d43150d34d7b863395afedc238a1772afb48f13`。
完整读回才取最大值，并再次核 whole SHA；原2240 modes 同时进入
整个 head maximum。剩余全 infinite tail 仍用原 native CYA scope
的解析 $128/(L+1)$ receiver，$L=1048576$。
大数组保持 private，只公开完整 receipts 和小结论。

## 4. 可直接使用的同对象接口

对同一原 $\widehat\Theta$，后继可以保留两份 whole candidates 后
选第14项作完整 global error。特别是在 **全部 BFP19 成功**以后，
其原 exact96 centers、完整 $\delta_X$、$B_{\widehat\Theta}$、
$E_VB_{\rm model}$、$E_MB_x$、$E_{\rm pair}$ 与双 physical mean
全部保留，仅把 BFP.22 的 $E_\Theta$ 槽换为第14项。
这需要整个 BFP actual/execution，不能从仍在运行的 prefix 宣称
已有真正 Θ/ν column。DCP 若产生新的 particular，也可在其
(DCP.22) 的同一 global slot 直接消费本结论。

本 actual 解除的是完整 Θ 的旧512 one-loss 放大瓶颈的一部分。
它不授予 full physical Schur、真正 homogeneous96/high反馈、
physical mean/phase/height完整匹配、非线性 closed family 或课题完成。
这14个成功目标以后保持原对象，不因换 receiver 而再次执行。
