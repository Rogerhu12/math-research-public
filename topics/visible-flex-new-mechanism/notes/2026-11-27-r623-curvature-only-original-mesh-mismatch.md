# R623 原自然终态：端点场身份不符，新 K 尚未执行

日期：2026-11-26 UTC；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

**结论类型：原公开 Actions 终态与源码的事实记录。**
本次 job 正常结束，科学 FINAL 明确报材料哈希不符；没有授予新的曲率、reach、
固定 g 或 README 完成结论。旧同 a237 完整几何结果保持它原来的适用对象。

## 1. 唯一原运行及完整终态

- workflow：`visible-r623-a237-curvature-only-20261127.yml`。
- run `45902483327`，job `140191333308`；source
  `18d66d1a3cb1b884c71703ff2cca123de4588e1c`。
- job 自然开始 `2026-11-26T22:05:28Z`、完成 `22:08:16Z`，API `success`。
- 原子进程开始 `22:05:57.785172Z`、完成 `22:08:12.345774Z`；返回码0。
  其134.560602秒包含导入与终态输出；科学计时另见第3节，二者不相加。
- request 37687 B/SHA-256
  `a0568ce02685af4347353df8b70704c57ad10dee4406546c865a9062ffbea431`。
- 完整原 stdout 173829 B/SHA-256
  `c97aa487271a6ee654e4362ed7dfb16febe1ee6a861f49980cd85d12b479017d`。
- 完整原 FINAL JSON 6716 B/SHA-256
  `bd3feaf995ca0d4fb3a6eed276a93f1f4f5b3cc5793cd52bef00417dc0d8ac69`。

源码19323 B/SHA-256
`7c3bb3c03af6911fe0481627f449c437c7469ea53601605680978486ae670c91`；
R623 helper11780 B/SHA-256
`43762578fd236233ccb44e8cd38bbfef44863b05b3fce26844bcd2f0febde80d`。
原日志仅在自然终态后下载一次，本地只做文本/JSON/hash解析；
没有执行任何新的科学观察。可重算日志和端点数组不入库。

## 2. 实际失败边界，不把声明身份当作实现身份

原 FINAL 的 failure 为
`ValueError: field realization differs from the exact requested mesh`，
`new_curvature_certificate=null`、`same_material_receipt=null`、`mean_receipt=null`。
这发生在 `SameFieldRadialDesign` 构造中的 `ExactEndpointHermite` 哈希检查，
即必要端点场已经重建，但新曲率的任何径向区间还没有取得资格。

固定97q仍为
`a2377220dacda9eefe63f25a2000441f0169a0db5de9bc23840f90e5037a895e`，p=.181。
要求的同场网格含完整 knots 及全部 endpoint 0/1/2 jets：

`0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`。

此次实际重建却得到

`f60be03b0af36d5d182f21860fe69cef80439c12bb23562d63dc2b57648bf52c`。

原 FINAL 顶层 `material_mesh_binary64_sha256` 是程序固定的**请求身份**；
它不能覆盖嵌套 `field_reconstruction_receipt.material_mesh_binary64_sha256`
给出的实际 f60 身份。半径修复回执明确报告
`new_material_mesh_matches_prior_completed_mesh=false`，同场检查真实拒绝。
端点个数同为62878并不能补足全部端点值及导数身份。

对[原 a237 同场完整几何终态](2026-11-27-r582-a237-normal-curvature-original-terminal.md)
的同一字段作纯文本比较：

| 项 | 原完整 a237 | 本次实际再生 |
|---|---:|---:|
| dense outward 段数 | 160 | 160 |
| dense tail RHS | 960944 | 960932 |
| 材料端点数 | 62878 | 62878 |
| core forward 与新 dense mouth 的 A 差 | `1.5297986673008107e-12` | `1.5295555078585765e-12` |
| 同一处 C 差 | `1.055763809709731e-11` | `1.0809700357050644e-11` |

原 dense mouth 相对原 paid normalization 的六jets差为

```
[-8.646512325571898e-18, 8.031769693772617e-16,
 -8.171241461241152e-14, -5.259681579161679e-15,
  6.328271240363392e-14, -5.879741138414829e-13]
```

此次为

```
[-4.2560356280918477e-16, 4.0207420726190435e-14,
 -4.125366714902157e-12, -2.6181834478222754e-13,
  3.142153204294118e-12, -2.900080176004849e-11]
```

这些只定位了差异已经出现在新 dense ODE 阶段；
它们不是两完整曲面 C0/C1/C2 距离的证书，不能据其看起来很小就转移旧范数。

已逐字核对两范围：paid seed、rtol=`2e-11`、atol=`2e-13`、
max_step=`.15`、factor8、initial_epsilon=`.001`均相同。
两原日志还都记录 Python3.12.14、numpy2.3.5、scipy1.17.0，
Ubuntu24.04.5 / image20261122.23.1。
现有日志没有足够信息证明硬件/BLAS路径或进程初始化是差异原因；
本条不把未证的根因写成结论，也不修改既已发布的源或输入去掩盖差异。

## 3. 全部新费用与未发生的工作

本次新科学计时为 **133.48344923899998秒**。
新增主要计数如下；不同层重叠计数不是互不相交的工作，不能直接求和。

| 新工作 | 原 FINAL 计数 |
|---|---:|
| 必要 dense outward transfer | 1 |
| dense tail RHS / 段数 | 960932 / 160 |
| actual weight 查询 | 1023374 |
| 新 core forward RHS / 调用 | 2510 / 1 |
| 新 short backward RHS / 调用 | 206 / 1 |
| 材料中原 ContinuousMean 数值高度 QUADPACK RHS | 235893 |
| 同一数值高度查询 / cache hit | 3166 / 375 |
| dense tail 径向查询 | 62443 |
| 原材料候选结个数 | 63045 |
| 完成材料端点 | 62878 |
| stable endpoint residual 准备单元 | 62877 |
| 新 inner DtN / 旧三seed比较 | 0 / 0 |
| 被计出的非零jet浮点underflow组件 | 274689 |

`interval_counts={}`，`height_integral_receipt=null`。
R611共享区间 H 对象虽已创建，其按需区间前缀尚未消费；
上表的235893次是材料重建所需原数值高度积分，不能与未开始的区间前缀混淆。
新的完整 K、R604/R622 标量后处理、参考重认证、C0/C1重扫描、
优化、Jacobian、fine以及旧七点诊断都未执行。

原 a237 几何665.7533184509999秒、原 f1 几何527.88478224秒、
原场与优化的所有已知费用及未知旧时段继续在原收据中保留。
本次失败不是撤销费用，也不作为另一条已接受实际优化 q。

## 4. 已有资格与后续输入的准确边界

原0d材料的完整 δ/α/K/reach结论仍只属于原0d材料。
本次没有证明f60材料与它相同，也没有支付两者的全域差。
因此不能把f60的任何后续 K 与旧0d的 δ/α混配。
原圆参考只由同一 mean 控制和圆core定义，独立于这个角材料再生差异；
它的ρ/D证书可在严格保持该参考定义时复用。

后续必须取得真正同一0d材料，或将新实际材料明确作为新输入，
完整支付它所需的所有新全域范数/物理资格；不能改一个mesh标签继续使用旧证书。
R623的纸证明与有限 primitive helper没有因为这次入口失败而得到数值验证，
也没有在这次入口失败中被发现数学反例。

运行入口实际pull公开至 `18d66d1a3cb1b884c71703ff2cca123de4588e1c`，
私库至 `72bafad43ae50754b0f0f0a2102ff3c78f3aaf97`；
README blobs一致，private QUEUE仍为本会话进行中，认证在科学子进程前移除。
