# Actual57：R273 方向的原十次试探均完整返回，最大残差未下降

- 作者：`geometry`；日期：2026-11-14 UTC。
- 分类：公开 GitHub Actions 的实际有限数值回执与原件字节审计。
- 本条只报告原十次非线性试探；完整 QR、模型读回与精确有限行账的原摘要见[同次方向原报告](public-actions-43637356027-1-dampedchain/native-damped-chain-qr/summary.json)；完整因子的独立审计另行登记。

## 1. 实际结论

Request57 的 R273 完整阻尼平方根方向以显式 `eta=1` 生成，随后在同一原 actual28 基态上执行原十次非线性 no-J 试探。**十次 evaluate 都返回有限 norm，没有 guard 抛错；十次均因原最大残差未严格下降而被拒。**

每次记录的 trialNorm 与 cached baseNorm 均为

```text
0.04177307820740199
float64 little-endian bits: c61182e94763a53f
```

这不是只在十进制打印精度下相等：原 numberRecord 保存的全部十对浮点位逐一相同。原生失败消息为：

```text
Error: multiple-shooting line search failed at 0.04177307820740199
```

结果是 `replay_completed=true`、`trial_accepted=false`、`selected_state=null`、`native_accepted=false`、`task_completed=false`。进程完成了声明的一轮原试探，入口以 exit2 保留全部拒绝；没有新的 accepted 状态可继续求解。

## 2. 公开运行与输出身份

| 项目 | 实际值 |
|---|---|
| 运行 | [43637356027](https://github.com/Rogerhu12/math-research-public/actions/runs/43637356027) |
| source commit | `adbdf144b14ae7adc71df09948a5c05f8a30e8b8` |
| job | `132576978446` |
| workflow | `visible-larger-public-damped-chain.yml` |
| artifact | `14130547938`，`visible-mainline-dampedchain-43637356027-1` |
| 完整 ZIP | 845612536 B；SHA256 `226227489fb0e4111061ac03c8bfe204a8a53cda16e6bb731d2656569288aec8` |
| trial result | 13454 B；SHA256 `83d5927be4180d5c962c1e27a86935bcff3d64d17c49b1c59e2bfdc43a6a4ba5` |
| trial summary | 7774 B；SHA256 `528f896d75fcb57c5f3258d414d66bdf4ed25dee513a0b8d2edd2aa67a1a5d24` |
| 实际 R273 result | SHA256 `c6feb54847e96778b076076ba17b4ccd666c2548c72f8c36414b2897d176cdc1` |

原 trial step 的 UTC 时间是20:27:06至20:40:55。其前完整 QR step20:25:50至20:27:06成功；这项成功表示方向生产者完成，不是原非线性接受。原件上传20:40:55至20:41:24成功。

入口报告的 elapsed 是820.125492312秒；Node replay context 报告794.413秒。二者计时范围不同，不能相加，也不能据总时间杜撰每次试探的单独耗时。

公开有界原件：

- [trial result](public-actions-43637356027-1-dampedchain/native-damped-chain-original-trial/result.json)
- [trial summary](public-actions-43637356027-1-dampedchain/native-damped-chain-original-trial/trial-replay-summary.json)
- [原逐次记录](public-actions-43637356027-1-dampedchain/native-damped-chain-original-trial/trial-replay-records.jsonl)
- [完整字节审计](2026-11-14-actual57-original-trial-byte-audit.json)

## 3. 十个原 alpha 的真实记录

| trial | alpha | 原 kind | 原 trialNorm |
|---:|---:|---|---:|
| 0 | 1 | `residual-not-decreasing` | 0.04177307820740199 |
| 1 | 1/2 | `residual-not-decreasing` | 0.04177307820740199 |
| 2 | 1/4 | `residual-not-decreasing` | 0.04177307820740199 |
| 3 | 1/8 | `residual-not-decreasing` | 0.04177307820740199 |
| 4 | 1/16 | `residual-not-decreasing` | 0.04177307820740199 |
| 5 | 1/32 | `residual-not-decreasing` | 0.04177307820740199 |
| 6 | 1/64 | `residual-not-decreasing` | 0.04177307820740199 |
| 7 | 1/128 | `residual-not-decreasing` | 0.04177307820740199 |
| 8 | 1/256 | `residual-not-decreasing` | 0.04177307820740199 |
| 9 | 1/512 | `residual-not-decreasing` | 0.04177307820740199 |

这与[actual55的求值内拒绝：九次 guard、一次 root Newton 失败](2026-11-14-actual55-original-ten-trial-rejection.md)不同。actual57的失败记录没有 `stage/rawCell/rawSegment`：此次 evaluate 没有在某个段的 guard 处异常退出，而是完整返回后未通过严格 norm 下降。

这只说明本次有限原生数值 evaluate 的实际行为，不是连续域、全相位几何或无限尾的证明。

## 4. 实际施加的方向与同一原问题

方向来自新的 R273 producer：

```text
exact_20261114_native_damped_chain_qr.py
SHA256 9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33
```

它使用 actual54 的完整有限1372段矩阵：

```text
76f30d775c0255dd127b08fa279e59fcaaa4a79a50b72bc7adc8231e436f6999
```

试探施加的是其完整1373节点方向按原 `old_to_new` 映射得到的577节点限制。没有重新加 sigma、截模、阈值化或清零 cut/far 方向分量。原 H、target、far、graphs/gains 与原 residual scales 仍是父问题。

| 对象 | shape / f64 words | raw SHA256 |
|---|---|---|
| 完整恢复方向 | `[1373,224]` / 307552 | `2c5d9ffdf6caf815e8104c38df8f7e33451db00df0779d5614afab8eabcd6773` |
| 实际原节点方向 | `[577,224]` / 129248 | `5b6e7bb4205ce79c6d0f20b63e491def9747e95a3272e8add1712595ea1c4a85` |

两份 raw 全部是有限 f64。完整方向与原节点方向都各有78个零 word，其中39个是负零。这些是原字节的分类计数：**实际方向不是全零**。但是，非零方向仍不能单独证明某个 `base+alpha*delta` 的最终浮点状态改变；本次审计没有在本地重新计算这些加乘。

完整 checkpoint 的负零侧表恢复后，与对应 raw 文件逐字节相同；全1373方向提取的577行，与实际原节点方向也逐字节相同。

## 5. 缓存与原生调用范围

本次缓存的是 actual28 同基态的原 with-J norm/minA/minD。记录明确保留：一次 cached baseline、一次 saved direction、0新baseline evaluate、0新J、0新correction，以及10次真实原 no-J trial evaluate。

没有把缓存改标签称 fresh with-J。协议请求仍带原 `jacobian=true,audit=true`，但一轮 replay 在原十次全拒后结束；本次没有成功 endpoint J，也没有 fresh endpoint audit。完整 native response 不因这些请求标志而视为成功。

本次调用保留原十trial正文、原 guard、原尺度 norm 及严格下降判据；没有把 R273 的 L2/model/exact 诊断变成新接受门。

## 6. 完整字节与源码身份审计

对唯一下载并核过 ZIP/CRC 的原包，另以纯标准库审计了 trial 目录的25个实际文件，以及 result 列出的22个完整小输出描述器。全部文件大小与 SHA吻合。

审计还核了：完整 gzip spec及其未压缩原文；完整 actual28/41/54 目标来源；实际 eta=1 的原 bits；完整1373/577方向raw/checkpoint/负零/映射；十条 observer记录与原 `native_trials.jsonl` 的逐项一致；原 full H bits；原 failure消息和一次请求、正常 worker退出事实。

源码身份方面，保存的 instrumented internal solve 经三处显式逆操作恢复成原 solve 原文；原十次试探正文 SHA 仍为：

```text
603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99
```

实际 public solve 的源字符串也独立核 SHA，没有用 `Function.toString` 伪装内部插入。原内部 solve SHA `d7d063fe2fca25c1742c68ec8056902a583952b61cdda98e1d9eaab7c09f3615`；实际 instrumented internal solve SHA `d9d712de7afbbf45f2c6cc2f11ddc507a634da24efe5cce0a58cd1016c9b50a5`，两个对象明确区分。

审计报告 SHA 为 `cce41e43cb66df637315197513a38cdb5ea43fdd17b0a637f59b77569a8fe21a`。审计源 `geometry_20261114_actual57_trial_byte_audit.py` 为19846 B，SHA `6591aa47ff88c9590e683588ad175c2a93dc3264e8378d2f4a4b7f6d72dd6024`。

这里没有导入科学求解器，没有重算 RHS、J、RK、QR、精确点积或任何 norm。QR因子、模型和原精确行账由同次独立报告处理，本条不重复声称审过这些大 payload。

## 7. 本次证据能说明什么

已确认的科学事实是：这条实际非零 R273 方向的原577节点限制，在十个既定 alpha 下均可让原 evaluate完整返回，但没有降低该原最大残差。

相同 norm bits 本身不能说明所有候选状态未变、所有 residual分量未变，或某个唯一原因已经成立。现有 `residual-not-decreasing` observer保存原标量 norm，没有保存这些完整返回的 trial state/residual向量；因此也没有本次真实 argmax 的逐trial位置记录。

后继若比较原576保存矩阵与1372目标，必须明确这是另一个有限求方向模型，并仍交回同一原试探；若增加只读状态/残差记录，须在原 evaluate的一次实际调用中保全，不能把旧数据重新标成新试探。当前没有 selected 状态，完整 native 求解和课题完成门仍未通过。
