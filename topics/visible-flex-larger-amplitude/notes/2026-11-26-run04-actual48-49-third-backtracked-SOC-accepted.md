# 2026-11-26 run04 实际48/49：第三个完整后退锚 SOC 返回，新的同范数父为 a801

## 1. 真实返回与来源边界

本条只登记公开 run `45857104277/1` 的实际48科学方向与49纯归因，不把下一个请求当作已执行。索引记录时间为 **2026-11-26 21:26:21 UTC**，两项均 `completed / exit 0`。科学入口实际耗时 `2044.3290403350002 s`；纯读取耗时 `5.935303106998617 s`。

完整已限制大小的公开记录是 [第5卷（46–49）](2026-11-26-public-actions-45857104277-1-part-005.md)，此次读取的 Git blob 为 `3b92cd5f5587f1aa5e7a53be5c972551de45e2a0`，原 UTF-8 全文 `36,272 B`、SHA256 `f8cd7d4919f4270f6fe5729e707bf788c314837c1f20b2a371b27296f923dcf4`。第48/49项的 `summary_errors=[]`、`missing_outputs=[]`。所有大科学报告、数组、缓存和日志继续只留 runner；本条没有整读这些大文件，也没有本地重算场、导数、QP、根或数值证书。

第48项实际源码 checkout 是 `ac7547dbaf0ffe05f10cd63950078e36c90d5d6c`；第49项是 `58dc109817b989b97f75e3eab4719cccca8fe89e`。实际队列文件来源提交 `c17aff856d7cea38e50d2996e535c1288fb67e28`，队列完整 SHA256 `86c0bfbf42e0bc0a5deb79f21d55b814f67f04780bd1a1b92a92119b294d18e6`。科学命令的完整 argv、runner 路径、输出大小及 SHA 在该公开原记录内完整保留。

## 2. 同一物理问题、实际父与源码闭合

本次保留原 `892f` 完整科学源与原 `009e` 完整纯读取，没有换成正在准备的八列 PCG；后者的源码准备不属于本次结果。

| 对象 | 实际 SHA256 / 身份 |
|---|---|
| launcher | `6c594f20adba3fa519a10c68669a42e099fd6d1d24f2e5f4fa49ff583b4b038e` |
| 完整 driver | `892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8` |
| 原同父全行 SOC helper | `e716afd05b162baecbdddf29ec119974213745bd5235fc1a23f36b4792ecb021` |
| 原全部半空间投影 | `a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e` |
| 完整纯 reader | `009e1e1d54ccd41e8ac2b4e6efe43541ebc327b7a6f3d4fa743e145517c897e6` |
| 固定 normalized parent bundle | `fcce34129466c5e19df169308c38b76795feff7f7b2384bbcdb10189461d6375` |
| 完整物理 model | `ac2cfc0d46a75a2070dfd9b208e3802c895a7bd35a9df5ab60d1016c81aebf19` |
| 固定 scalar target | `2612418a7f6dd3718ec340a37e7793bbedee0a3423f90a4a15c028cdb80492df` |
| 完整坐标范数 | `c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa` |
| 真正 restart checkpoint | `0c9afcc4971d66b3021bdc11360c6f303c0218d7cf6e14297d85128f3a20bade` |
| 真正 restart report | `606e10f8622ab830c122f38c5530e292bf932e2daf2831fb18c12c832b6445a3` |

第49纯读取实际确认 `whole_body_match=true`，并校验完整 final bundle 和缓存文件。新初始 bundle 的完整 SHA 与 restart 的 `0c9a` **相同**，不是只比较标量。全空间仍为 `1,333,370` 个变量；完整全角逻辑 observation rows 为 `45,324,288`。本次原范数为 `jet-sum`，未改 `radial-norm-length=.05`、`angular-transition=24` 或原范数权。

显式数值输入仍是 `N=2048`、径向 stage block `64`、角 block `8`、径向积分阶数 `8`、CPU threads `4`；谱目标 `p=4, epsilon=.001, scale=.05` 与 `legacy-fraction=.5`。真实 final damping 与 restoration damping 均为 `.01`。完整 `1×64` metric 方向和 `4×64` restoration 可用预算、原 `15` 次 ray、最多 `8` 次 SOC、`tau=0`、observed inward fraction `.125`、数值半空间容差 `2e-11` 都保留。曲率预算 `.03/.992`、marked diameter `4.2`、witness lower `.9`、height floor `1.01` 与原完整真实接受条件未放宽。

## 3. 实际同一 Phi 与最大缺陷变化

| 本次实际读取 | 初点 | 末点 |
|---|---:|---:|
| centered 同一谱目标 Phi | `0.005135593635366869` | `0.005037813931167355` |
| 工作网格最大 relative Gram defect | `0.034109509524516045` | `0.03390456510876344` |
| 最大真实有限 physical g | `-3.72901331765485e-05` | `-2.3377415068748242e-05` |

初点的这些数值与实际46末场、实际47归因相接。末场 `final_geometry_feasible=true`，`all_permanent=true`。这表示本次完整 finite grid、全部永久地址和幅度筛按原代码真实通过。它没有提供连续曲率、reach 或全域 metric 的证书；最大工作缺陷也仍远高于本题的 `1e-6` 完成阈值。

科学完整返回位置：

- 目录：`so3-closed-actual-profile-cached-backtracked-SOC-v2-third`。
- `report.json`：`25,951,879 B`，SHA256 `bf64118bed66e05a24f80741e02b0a5ad45d521d6da25985809a75b1a96450df`。
- `final.npz`：`10,720,258 B`，SHA256 `a801cf94cea863374b4453046c09bfb95a24903a8e6bb0e0a7ccbf6915de4b37`。
- `initial-new-field.npz`：`10,720,258 B`，SHA256 为上述真实 `0c9a` restart。
- 相邻完整 `-command.json`：`16,682 B`，SHA256 `60054891c21ae813446652383857e84f28af5567a22b40ba86af34569c4eafa2`。
- 纯读 `postprocess/so3-cached-backtracked-SOC-v2-third-summary.json`：`198,972 B`，SHA256 `3ea6d425a90ca8ae3de737d6e87955f978267132544220017cd89acec2e7e6e7`。

这些原 runner 文件没有被取回或重包进仓库。

## 4. 真正接受的是后退锚全行 SOC，内层并未驻点

第49实际归因给出：

| 字段 | 实际值 |
|---|---|
| metric / restoration 返回方向数 | `1 / 0` |
| 接受原 ray / 接受 SOC | `0 / 1` |
| SOC 真候选数 / 半空间投影数 | `2 / 2` |
| 最后候选在最新永久点的完整重读数 | `1` |
| 最近符合资格的被拒原 ray 锚 | `0.03125 = 1/32` |
| 已经完整通过的原 ray fallback | `0.015625 = 1/64` |
| 最终 step kind | `complete_separation_SOC` |
| 最终 accepted alpha | `null`，因为完整修正向量不是原 ray 上一个 alpha |
| QP 状态 | `iteration_limit` |
| 实际 advances | `64` |
| 最后面 projected-gradient norm | `1.9739983679000024` |
| 本次 gradient tolerance | `3.923431443941044e-06` |
| QP 实际秒数 | `1189.021793762` |
| 完整方向实际秒数 | `1669.6590694119986` |

本次实际 parent、A、原 QP direction 和选定锚在各 SOC 轮中保持原源码的同父语义；全原 C prefix、增加的分离行、独立修正 A*z 和真实同 Phi/全几何门没有删减。最终仅接受同一个候选。这里引用的正确性来自此次完整源码绑定和既有完整实现，而不是从数值 `g<0` 倒推某个漏读检查必然执行。

公开紧凑摘要没有逐轮导出所有原 ray 与 SOC 的每个失败家族、最坏地址、C 行数、每次新行数或 J/J* 总计数。因此本条不补这些未知值，不将锚变小独自解释成某一种几何障碍。内层 projected gradient 仍明显超过其真实容差，`iteration_limit` 不作驻点/收敛声明。两轮修正后的真接受说明本次全局化产生了合法的有限数值推进；它也不证明下一方向必然有效。

## 5. 永久位置、同 run 缓存与真实成本

本次最终永久曲率地址 `2235`，永久半径地址 `2156`，全部在最后真实筛中读过。这些地址必须随真实 `third/report.json` 进入后继完整 union，不能只继承上一轮 `2155/2070` 或把数量当集合摘要。

原缓存实现实际复用 `1655` 个文件，计划缺失数为 `0`，又有 `5` 个完整新 provider 文件，纯读取最终重哈希 `1660` 个实际缓存文件。完成 manifest SHA256 为 `b58f812c53e6fc685ba9abffd6288cd772096240013411345b9cd4bb0a97ea8f`，`cache_completed=true`。

缓存准备实际 `6.608439200997964 s`；包括完整初态读取的 setup 为 `363.67610191600033 s`；driver 总秒数为 `2039.270462299999 s`；报告 peak RSS 为 `3,166,788 KiB`。原 cleanup 只移除明确已返回 child 的新可再生 row cache，共显式记录 `3,232,088,880 B`；原输入、report、final、manifest/cache donor 均不在其删除范围。完整 cleanup 明细继续在 runner 状态日志，公开小卷只记录真实数量、字节和 canonical metadata SHA。

## 6. 由真实返回决定的后继与仍未解决的责任

新父是完整 `a801`，不再沿用 `0c9a`。目前可继续同 fixed g、同范数、同实际 `.01` 的完整方向；原 `892f` 入口仍可运行，不能因为八列当前预条件器尚在源码闭合就停止实际求解。后继完整参数明确保留原 locations 和实际39/40/44/46/48的全部报告地址，并使用实际48完成 cache 作为同 run donor。它继续真实检查域、曲率、全幅度以及全部新增地址。

另一个独立准备中的入口会用当前完整 A/A* 组装八列 SPD 预条件器；它不是本条48/49的算法或结果，不把新源码归入这次实际计时或收敛结论。其正确接线和实际效果应另行登记。

公开的 `789f` 单准入 wrapper 只把原科学 launcher 与原纯 reader 顺序置于一次 controller admission，二者完整 argv/源码/原预算不改。科学非零返回也仍尝试纯读；真正系统中断如实记缺失。**它不延长 Actions 硬 job 时限，也不保证这一请求会自然返回。** 原 run04 硬预算接近结束时，后续若没有实际返回，不可预填成功；跨 runner 仍需要完整合法输入再生，不能从本条 SHA 合成 raw。

本题仍须产生达到连续相对 metric `1e-6`、固定目标下实际精化，以及 README 的全 t、幅度、reach、嵌入和闭合等完整证据。此次 `complete` 仅表示本次已声明数值方向预算及最后实际读取完成；`continuous_certified=false`、`isometry_accepted=false`。本条不停止研究，不将数值改善或已到运行时限视为完成。
