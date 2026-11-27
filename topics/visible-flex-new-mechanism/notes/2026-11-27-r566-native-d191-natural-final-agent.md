# B030：原 d191 / partial238 的 native 曲率运行真实自然终态

**状态：启发式/数值证据，未完成课题。** 本文只登记已结束的公开运行，不重做科学计算。原生 SLSQP 曲率初始化产生了四次 metric 接受和一次 geometry-restoration 接受；最后还有同一个真实候选的 2,561 个角向区间未完成。保留点的物理几何违反为零，不等于它通过原工作余量门，更不等于全域等距或 reach 证书。

## 1. 唯一原运行与输出身份

- Run [45914886940](https://github.com/Rogerhu12/math-research-public/actions/runs/45914886940)，job `140231615166`；自动 push，原自然结束，无取消、重跑或重复 dispatch。
- Source commit / Actions 实际 public pull 均为 `797efdf06d2418f8bdf1f6303872855d75c0082f`。实际 private pull `d8383050f7823c5eb8a72e781f976eb784b77d78`，根 blob `5ba164843b1f5802184178a82d786264404873a3`；规则检查通过，私库内容没有输出。
- Workflow：`.github/workflows/visible-r566-native-d191-partial238-20261127.yml`。
- 科学源：`scripts/r566_native_d191_partial238_20261127.py`，60,295 B，SHA-256 `23a5e6df8de9ec8bafa60e8e7527038b2961fe03fe8e2b293f07232a9b7c9fbf`。
- Request：`computations/request-r566-native-d191-partial238-20261127.json`，868,286 B，SHA-256 `3030d05ad50554b023b49b16b96e1bb665eab09e2c5e7cf84da3b038c05c6e4e`。
- 原科学子进程 `2026-11-27 00:08:02.294029–00:47:34.341879 UTC`，returncode `0`；合作时钟在原角向区间内触发，保留最终状态后正常退出。不能把 runner 的 success 解释为科学完成。

原 stdout 由 finite_geometry 在自然终态后取一次，后继只读取这份已付材料：

| 对象 | 原字节数 | SHA-256 |
|---|---:|---|
| 原 job stdout | 17,839,432 | `e52e204affd28c493626b4008ef996a2a0742890e8ed16bb68a7252aa0cb5d8c` |
| 唯一 `WORKING_ROWS_FINAL` 行的原 JSON | 909,317 | `6ac4e786d92ee4109f739c99b3871a09897583aeddce26d2ffcdc439e743d9b8` |
| 唯一 `THETA_PEAK_LOCALIZER_PARTIAL` 行的原 JSON | 2,083,457 | `f11fc1a43f24909df7b111ba280e13ae2cfbbc47d90022aafdf7849edaadce4d` |
| partial 中 9,452 个已完成峰，规范 JSON | 1,501,121 | `923861b92559e949aa30ac4cf3903caddcf930c5f15779822d97a60859d3d78d` |
| 2,561 个未完成区间描述，规范 JSON | 554,151 | `f2eec7aaf2c52f23b3f0aca3a5ff2571aac9f873f3f758c7626ed5f736ee3ec2` |

规范 JSON 指 `sort_keys=True,separators=(',',':')`；原 FINAL / PARTIAL 行则保留其逐字字节。原 stdout、可再生事件表和科学数组不入库。后继真正需要的已付峰输入若超过 1 MB，按根规矩 8 压缩为 `.gz`，不能为省输入而重播这 9,452 个峰。

## 2. 实际接受轨迹与最后保留点

原起点来自上一真实终态 d191，`eta=0.21585219167801023`。本次先复用其已完成 1,678 个区间，只补原剩 238 个；原粗、细、nested 报告复用一次，该原候选没有被接受。随后发生以下五次完整原门接受：

| outer | 阶段 | 实际 q 的 SHA-256 | 原实际 eta | 后处理步分数 |
|---:|---|---|---:|---:|
| 0 | metric | `199f19efa077fd80c10b2bab21d626bcf72a906e2f9610774181f19b1aa2977f` | 0.2155127290392059 | 1 |
| 1 | metric | `7e39c1282b40bd90f1ccd8cc5b70ae7c84204fbdd68ae9efd2860a559ce4581a` | 0.21405306389725903 | 1 |
| 3 | metric | `adbe6c2abc95a107482b66ba9a6d3079a93f75fd7a39a5ef72d209e52bbd10cc` | 0.21002499488767573 | 1 |
| 5 | metric | `c956a1f9b0d27555a770613ccf3008673d84ea5e7736c477d8fd977bc5a08b59` | 0.20869433542684312 | 0.5 |
| 8 | geometry_restoration | `56594ecb1d8d94cd8463359dc2e40b4a681be6a4588296d63ae3eda3a240c7f3` | 0.20868474226441153 | 0.5 |

最后保留 q 有 81 个原参数；`actual_q_binary64_sha256` 与上表最后一行相同。原 callback 对缩步的接受只更新独立物理 best，不能伪称 raw SLSQP 迭代也等于该点。实际有一次缩步接受后继续同一个正在运行的 backend；真实换行、换阶段仍按原规则重新启动。

最终完整库和资格如下：

| 项目 | 真实末值 |
|---|---|
| 原 coarse 半径 | 804 个；binary64 SHA `6b5a794a7f207d24e05fce68f72634cdeaea04d6091ebf28447fd852bbb56067` |
| 当前 fine 半径 | 1,610 个；SHA `6c81065190712fac73136514a7caf7f7c7b41e59a74712602aa7f08bf1fe776b` |
| 保留点已经完成资格的 fine 半径 | 同一组 1,610 个、同一 SHA，无新库冒用旧资格 |
| coarse / fine FFT 角数 | 1,536 / 3,072 |
| 原物理峰轨道 / working 行 | 1,793 / 277 |
| 未应用 physical / working 提案 | 0 / 0 |
| 完整 coarse 原标量行 | 2,224,960 |
| 实际阶段 | `geometry_restoration` |
| 实际 / 提议 trust | 均 `0.45050811767578125` |
| trust 决定 | 未完成；没有把一个未采用提议冒作原末步 |
| 当前库的保留 q 完整值已知 | `true` |
| 当前实际独立辅助量 e | `0.010474815185526721` |

保留点 fine 实际 `eta_grid=0.20868436084486303`，完成的 9,330 个角向峰给 `eta=0.20868474226441153`；物理几何最大违反为 `0`。原细网还有 `|y|max=0.3925820470796853`、球半径最大 `1.0114825458727434`、`det_min=0.8876354741154494`、mean E 范围 `[0.9958904272238597,3.646165864107548]`、`z_min=0.02`。这些是原有限网与已观察角峰的读数，`all_pair_reach_certified=false`，连续角向覆盖也未证明。

### 原工作余量不可被物理 V=0 代替

outer 8 的已付接受记录直接输出

`actual_complete_geometry_margin_violation = 0.0004748151855263885`，

attainer 为 `curvature_plus`，`s=0.7617187499999999`、`theta=1.5707963267948966`。接受时 `e=0.005474908170231097`。它是在原允许的恢复阶段改善余量，并没有把原工作余量全部恢复到零。

outer 9 换库后原 coarse 重新选行，源码先执行 `best_geo=max(best_geo,-geometry_min)`，再置 `e=best_geo+.01`；真正输出的 e 为 `0.010474815185526721`。这一轮**没有单独输出未加 e 的 minimum 或更新后的 best_geo**。因此已接受 fine 的准确值与末 e 必须各自保存；不能把浮点 `e-.01` 宣称为逐位恢复了原未输出的 best_geo。此差别只涉及一个未保存标量的舍入记录，不削弱已付 fine 或原物理门。后继应保原 exact e，保已付 fine margin，并明确处置这个标量缺口；若原待候选最终满足 `geometry_peak<=tol` 且物理门通过，原 `restored` 接受分支根本不依赖这个缺口。

## 3. 同一未完成候选：只剩 2,561 个原区间

最终 raw / last_trial 的 q SHA 为
`53ed9bb6db3208246487553d2061ab4e61baaf1ba4b2159332a5686249f0dbba`，不是保留点。该候选属于原 `geometry_restoration`，实际 e 为 `0`、缩步分数 `1`、原物理盒违反 `0`。原 coarse 全 2,224,960 行、同一 1,610×3,072 fine、nested 比较均已支付。原工作行 / coarse 最坏为 strip `-5.514922517789456e-9`，在声明的原容差内；不是以放宽余量获得的。

fine 已给 `eta_grid=0.20921002233215497`、物理几何违反 `0`；原 nested 三读数依次为：

- metric components：`1.9984014443252818e-15`；
- relative mean E：`6.83153289749207e-16`；
- tau curvature：`1.1001759503415087e-14`。

这不是 metric 改善候选：其 eta 比保留点略大。但原恢复阶段以工作几何余量为目标，若全部原门最终通过，不能因 eta 没降低就错用 metric 阶段判据拒绝它。

同一 oracle 身份为 `18745e500f027eaffa8178b66aafc3c9b01579e2d424b9e52367abc403ec6505`。原发现 12,013 个区间，完成 9,452 个，剩 2,561 个；已付 83,830 个点目标调用、`440.78279974299994 s`，18 个整批完成、19 批开始、批大小 512。时钟消息是 `clock reached inside retained angular bracket`，不是数值失败、证明失败或自然求解完成。

已付峰中 strip 最大 `5.542782454369399e-9`，metric_plus 最大 `0.20921004461892675`；其余已付几何峰尚未显示新的超容差违反。这些是已完成前缀的观察，**剩余 2,561 个未闭，不能据此前缀接受、拒绝或声称角向覆盖完成**。后继必须保同 q、同 oracle、同 fine、原区间描述与全部 9,452 个已付峰，补剩余区间；不重做原 coarse/fine/nested 作为前门，也不重新搜一遍候选区间。

## 4. 真正已保存的 native H / secant 状态

冻结 helper `scripts/r566_true_secant_curvature_20261127.py` 的 SHA 为 `76c38d9ebdb51698d115d667adb7ab33cc2d1b18af99697f1a0e1058e6b27a0f`。本次初始 H 是 I；之后的更新来自同目标、同行函数定义的真实已付 J 和 QP 的固定乘子梯度差。

最终 `actual_curvature_checkpoint`：

- schema `r566-real-frozen-multiplier-native-initial-H-v1`，维度 82；
- model identity SHA `8a1abe70f785c8c1d8e80b884aa58299598846c716c1be63b0d7b3e9421414a7`；
- row function signature `20757ab502170f224b227cd78a00edd5af0bf47ddde0b04ebaa293e40a90d09f`；
- 完整规范 JSON 74,980 B，SHA `f499980ad5de37b29a7b80263978e07df31d012c41e5d01a1ac06f90119dfd4e`；
- 不含自己的 receipt 的 payload 74,857 B，SHA `5163edd217185c43913639ed9f557089a4be89023272ed82a90736a7b9b57645`；
- 实际 packed LDL 为 3,403 个 binary64，27,224 B，SHA `ba6108794907e6f72be0c683d0752e6f657ac60ec394ad07b99acee6babc49d7`；
- pending 包括 82 维原 QP anchor、82 维固定乘子梯度、两条实际非零乘子行，零乘子按准确等于零省略，没有阈值截断。

pending 原 QP 是 backend 10 / major 1 / MODE 1 / reset 1；原 J anchor SHA `d9d3d7dccae0b398200e4a678dc672e6578238084ebe2c4b57a065f55e5b4453`，行顺序 SHA `1c80702fd614935dfa0c5281d6880ecb784afa7413c0ea697f08a87dec3d0161`。

最后一次准备的 H 来自上一真实 QP 9 / major 2。Powell theta `0.8000000000346704`，原观察特征值范围 `[0.04020909279441955,1.0000001657211286]`，此次没有 eigenvalue clipping；这仍只是下一原 QP 的启发式正定初值，不能当 Hessian 证书。真实内部 MODE -1 消费 pending 后 helper 会清除，不能在后继又补一次同 secant。

后继可准确向同 helper 传 `checkpoint=terminal['actual_curvature_checkpoint']`。这恢复的是已输出的 H/pending；完整旧 native workspace、完整 J 矩阵仍没有保存。新进程的必要 native 构建、真实新 working J、同一原模型内的新梯度差均须计费。若补完队列后真正转回 metric，原 helper 的语义签名会使恢复阶段 H 重置 I；不能把不同阶段的梯度差作为同一模型 secant。

原 FINAL 的 `source_internal_BFGS_arrays_not_recovered=true` 指最初 normal56e8 来源没有输出旧 workspace，不能读成“当前 native packed LDL 未保存”。本文明确区分这两层身份。

## 5. 全部实际费用与未闭项

本次科学 elapsed 为 `2370.546518149 s`，包含合作时钟触发前的部分工作、native 构建和线性代数。原 prior ledger 已完整保留，累计已记录科学时间下界此前为 `17099.551640495 s`；再加本次 elapsed。更早被截断工作的未知部分仍未知，不据下界宣称精确总费用。

| 原计数 | 本次真实值 |
|---|---:|
| outer started / completed | 10 / 9 |
| metric / restoration 接受 | 4 / 1 |
| callback proposals / backtrack value trials | 11 / 16 |
| working recoveries / exhausted | 5 / 0 |
| 完全合格的缩步接受 | 2 |
| 缩步接受后原 backend 继续 | 1 |
| backend natural returns | 0 |
| coarse scans / fine scans / complete localizations | 28 / 9 / 9 |
| coarse / fine 行拒绝 | 2 / 3 |
| nested 拒绝 | 0 |
| localizer candidates / completed / unresolved | 41,588 / 39,027 / 2,561 |
| localizer point objectives | 330,498 |
| 原 source 完成峰复用 / 原剩区间新完成 | 1,678 / 238 |
| 原 source coarse/fine/nested 复用 | 1 |
| source 原待候选的完整接受 | 0 |
| physical / working exchanges | 8 / 10 |
| 新完整 working J / direction blocks | 11 / 876 |
| working J seconds | 388.1190170099998 |
| working value keys | 43 |
| working / coarse / fine epigraph lifts | 7 / 5 / 4 |
| epigraph 后原 working 重查 | 16 |
| 已付当前完整 selection replay 避免 | 2 |
| 新 restriction observation | 0 |

所有活跃/退休 oracle 各计一次的总账：构造器 158 次 / `41.03551152599795 s`；FFT states 1,515；diagnostic uniform FFT 0；exact core arclength points 1,510,552；nonuniform summed points 1,575,709；point evaluations 333,581；point parameter directions 2,367,792；point values 1,835,568；point sets 330,667；subsets 3,134；uniform gathered points 259,859；primitive Fourier fields 13,635。prepare、point-set、point 时间依次为 `401.7433294690039`、`125.76976000689831`、`1658.273980647886 s`。这些子项属于 elapsed，不能相加再收费。

native 共 backend 10、calls 12 / `0.05963662500010969 s`；seed preparations 10 / `0.023427469000239398 s`；实际 QP 观察 11；frozen-multiplier 更新 5，全部发生 Powell damping；skipped 3，phase semantic reset 1，MODE -1 已消费 pending 1；clipped seeds 0、invalid H reset 0；额外模型 value/J 均 0。

必要 native build `1.2602176089999944 s`，四份官方源抓取 `0.33052138000005016 s`，一次编译 `0.8849108229999842 s`；52080 B binary SHA `83652093638515310571078e19b5934d1d3ec4b107373bae71c8ed15dd5664c4`。使用同 SciPy LP64 OpenBLAS，SHA `8fb864c29cac4b25f6e2c139491ea96f2724dde42d51394f84e9c4a622e34790`；没有数值探针。运行 Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0，原 helper 对工作状态、非零乘子和 MODE 的实现不变。

## 6. 这条终态具体支付了什么

原 native 曲率机制实际发生了五次来自已付 J 的固定乘子更新，并产生了新的真实原门接受；不能继续称它只有源码、没有运行。同时当前残差仍约 0.209，metric 是静态设计过程中的变量，并没有固定同一个 g 或支付任意 t 的全族门。下一必要科学工作是补同一候选的原 2,561 个区间，随后按真实阶段接同模型优化；完整 H/pending、全部原行、保留 fine 身份、原 margin 与既有费用都保留。
