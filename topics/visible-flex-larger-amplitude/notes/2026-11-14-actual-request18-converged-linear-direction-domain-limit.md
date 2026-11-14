# request18 实际回执：线性最小化停止后仍受同一 RMS 域限制

2026-11-14。本次公开 Actions 正常结束，得到一个新的、仍未被原完整 BVP 接受的 warm。它没有启动 native tail，不能与 request17 的非零 H 失败合并成一次成功联解。

## 1. 实际执行与可复现身份

- run `43602070499`，job `132468788403`，lane `trustresume`，原执行提交 `fd4f5619dd5ba35cf30c571338b48530448c8cee`。
- 正常出版提交 `1e490cda7f4df3292b53aaaae9c7c9c5193afab8`；完整限额输出为 `notes/public-actions-43602070499-1-trustresume/`，出版 manifest 与取回 artifact 的文件 SHA 一致。
- 完整 artifact `14116817371`，8,960,117 bytes，ZIP SHA256 `a027f3eedfd8ee27e91da1aeec541516b91706110c80479c226ad35e344fec7b`。
- native 前独立 warm artifact `14116702854`，4,729,310 bytes，ZIP SHA256 `0cd3bd1f836c645c8e3c9858f27030dccfb5acb575ad2906b15c429976564c4d`。
- 父输入是 request17 实际保存的 `warm-003.json.gz`，SHA256 `5d1c452291099ad18b1a619ba3794614b04a0c620b8ed0f28887a84731ef7886`。
- 完整九件 producer 源逐 SHA 核同；原三 warm/collocation/response 源未改，原699节点、M112/N2048、全部 physical collocation、112条 Rφ、原 exact chart 与全部域检查不变。

本次按既有规则使用 damping270，一模型，LSMR 上限200；原两 RMS 分数、17层回溯、真实 matched merit、原 Richardson 步长和5e−5接口门都保留。

## 2. 真实线性结果与回溯

LSMR 在第80次迭代以 `istop=2` 停止，实际11.039037173秒。它没有耗尽本次200上限。记录为：

| 量 | 实际值 |
|---|---:|
| damping | 270 |
| normr（含正则项） | 9.371378069626763 |
| normar | 2.6149467597152025e−5 |
| normA | 29.50180759498129 |
| 估计 condA | 4.28184748670011 |
| scaled direction L2 | .00290540343337052 |
| physical coordinate direction max | .0002071568422591971 |
| 完整模型实际一阶导数 | −1.071626910018626 |
| 加权 J 方向平方范数 | .4562510494137782 |

此事实只排除了**本次λ270方向因80次上限而截停**的解释；它没有回溯证明 request17 的λ90方向已收敛，也不将含正则项的非零 normr 当作线性失败。

α从1到1/16时有3至5个无效 midpoint。α≤1/32时，所有节点和midpoint已有效，真实 merit 也下降，但原 RMS 查询拒绝前面的步长。最接近接受的两层如下；全17层回执都保留：

| α | 固定本模型 Wr 的实际 merit | 实际/预测下降比 | 原 RMS 结果 |
|---|---:|---:|---|
| 2^-15 | 44.44714423978154 | 1.0000043544832091 | interval473 内 β²=−6.05166211278263e−5，拒绝 |
| 2^-16 | 44.4471605914814 | 1.0000007444488113 | 两组各698个查询全部有效，warm下降接受 |

本模型自己的初始 merit 为 `44.44717694316943`，实际下降 `1.6351688032045786e−5`。不把不同模型重算的 Wr merit 作直接差分。

仍限制步长的查询完全相同：interval473，左右节点 `[1.1993469629899143,1.2043314144896742]`，fraction `.17267316464601146`，位置 `s=1.2002076440044023`，physical phi=0。查询 scalar 字段为 a=`1.1899847955223861`、ap=`−.14863126227800036`、app=`−2.472231719360121`。

较大步的最坏角可以转移；例如α=1/32在此单元的最坏phi约.09817。后续只保护当前固定角的一阶变化，仍必须保留所有角、所有节点/中点/两RMS的真实检查，不能据一个 covector 保证全域。

## 3. 新 warm 和真实边界导数检查

完整优化耗时 `250.657267318` 秒，只保存一个下降步。新 `constrained-warm/warm-001.json.gz` 为4,702,637 bytes，SHA256：

`1dbdcc8fbb9dd7d4571259679a97dca5ee635fab88dece584d3a44727da477c3`。

- 原 physical collocation max 从 `.007110547307418288` 变为 `.007110547287016681`，仍远非原BVP接受。
- 完整 affine BC max 为 `9.606657590166996e−8`；入口/常值ODE残差为0。
- 原rho最小值 `.16604058243275`，全部节点/midpoint/两RMS查询域有效。
- 新p为 `[-8.111473945558798e−20,2.247104106123805e−20,−7.838061805957672e−20]`。
- status仍明确 `success=false`、`new_coupled_finite_acceptance=false`。

该实际新端点的完整原 Rφ 三步/Richardson 检查重新运行24.012766615秒，最大 Richardson 相对误差 `9.000976460873103e−10`，小于原5e−5门。它仍使用已完成真T112零态J的**显式affine图**，当前H与零锚不同，未调用当前H的native solve，不代表新的完整尾导数。

完整J/JT及原增广/约束坐标动作检查保留。真实方向的三个中心差分 merit 斜率约 −1.0716225、−1.0716237、−1.0716031，与模型负斜率一致；完整方向向量差分误差并未达到机器级，不能扩大解释范围。

## 4. 直接执行的后续选择

不再仅增加同方向的LSMR上限、模型数或damping。本次在允许200次的线性停止后，仍消耗相同 turn 内 RMS 余量；这是改用该查询完整域梯度的实际依据。

后续独立算法保持λ270与原残差，先在此新warm上检验通过**真实两端nodal RHS、完整Hermite查询、全p和exact入口chart**的域covector，然后只做一个投影正阻尼模型。其数学恒等式另记R262；原所有 nonlinear/RMS/merit检查与最终fullDN/BC/audit门全部保留。一个保护行仅限制优化方向，不增加科学方程或宣布存在。

尾侧同时由 request19 的无J实际cold residual探针定位；这两条阻断分开处理，不阈值归零H、不拿失败响应作完成anchor。

## 5. 关键文件 SHA256

| 文件（相对本次公开输出目录） | SHA256 |
|---|---|
| constrained-warm/driver-status.json | `4c37bb395ccefbb42733136dd46bfcaa6381f9f4de582feb675050367c90c7f9` |
| constrained-warm/model-000.json | `a94a351d39680ed1100a442411d320ae775b8e2f6b1d6f624785ef921986f923` |
| constrained-warm/model-000-operator-check.json | `f01df0cd705b1dcf3a8603f044fe3598aa5e13ce6c159ff7eedab14dae0665e4` |
| constrained-warm/optimization-intent.json | `35060c913710dc70ea824922207ed9e46d2f27016dc3a184ad26430b863eca50` |
| physical-response/response-check.json | `4bc9015590b8a375efa268c1e6da04ba9420bb730c2144ee674d84e6bbedf4f2` |
| resume-source-ledger.json | `a0d5f6c561b3e79e6d3c729a3c44839c8029e98129902c886e2a6f831237c9c7` |

所有新增数值均来自上述公开Actions实际输出；本地只读、取回与SHA核对。
