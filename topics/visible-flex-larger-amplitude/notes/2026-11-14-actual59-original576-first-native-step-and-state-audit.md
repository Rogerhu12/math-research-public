# actual59：原 576 段方向通过首次原生试探，完整状态与残差字节已核

- 作者：geometry agent
- 日期：2026-11-14
- 分类：公开 Actions 实际数值结果；纯字节/源码身份审计
- 理论：[R273 完整阻尼平方根链](../results/R273-complete-native-damped-square-root-chain.md)
- 接口：[原576方向、原十试探及只读记录](2026-11-14-original576-damped-native-trial-and-readonly-residual-interface.md)
- 完整审计：[actual59 原生试探字节审计](2026-11-14-actual59-original576-native-trial-byte-audit.json)
- 配套线性报告：[actual59 原576 QR及两方向exact读回](2026-11-14-actual59-original576-QR-and-two-exact-readbacks.md)

## 1. 实际结论

本次完整原576系统的 R273、eta=1 方向，在**第一个原步长 alpha=1** 即被原始非线性线搜索接受。原范数从保存的基态值

```text
0.04177307820740199     f64le c61182e94763a53f
```

降到本次原 `evaluate(...,false,scales)` 返回的

```text
0.0001289424025918576   f64le 491eedcd96e6203f
```

只发生一次原 no-J 求值和一次原 trial callback；该次完整求值返回，没有触发原 stage guard 失败。原十步循环因首次接受而正常提前退出，未计算其余9个试探。

**这是一轮真实原生接受，不是完整 native 求解完成。** 原 native 容差仍是 `2e-9`。本入口按设计保存 selected 后停止，下一轮 with-J、最终端点 J 和 fresh audit 均未运行；不能把 job success 或 selected state 改称完整响应。

## 2. 公开运行身份

| 项目 | 实际值 |
|---|---|
| run | [43640772654](https://github.com/Rogerhu12/math-research-public/actions/runs/43640772654) |
| source commit | `c61725631d20191bd5e02054cefa41cc1af5f245` |
| job | `132587632535` |
| artifact | `14132106883` |
| ZIP bytes | `368592441` |
| ZIP SHA256 | `e8f4862114772a627ddea61b24be3bd50cc6f9c306e71e90010e324511e36a74` |
| 原接受 callback 时间 | `2026-11-14T21:07:20.599Z` |
| trial launcher elapsed | `104.20004066099997 s` |
| trial context elapsed | `78.395 s` |

两个 elapsed 来自不同计时范围，不相加，也不据此拆分本次原 flow 的耗时。

本次原576方向的 `result.json.gz` SHA 为 `d22e21a926318f15cb2d38f1f657404c0684d8bc81fe54c32499b35713a83b97`；其完整矩阵身份为 `3c4583c83c5b91a6aab5e64ef74ba8ef0196047c50857f32f9e2cf1dd1bcc57d`。它绑定 actual28 原576全部保存 J/r/cut/far/sigma/H，不是 previous1372方向的限制。

试探入口/ hook 仍分别是 `c337d880c29aaa865b6516fd679ffffe9410d30c893ff2f8e0cc4092f6adbec7` 和 `c104ff11b356cb3993ffd5ae97988259b2f27c91e492c7736d7a96a9ad450e36`。

## 3. 完整 selected 状态

实际试探输入、selected binary 解压结果及 selected checkpoint 逐行恢复后的全部字节一致：

| 项目 | 事实 |
|---|---|
| shape | `[577,224]` |
| raw bytes | `1033984` |
| raw SHA256 | `384de298d6274ef7a6f5bdbc4e6cf6ef9dee5fb9bffd020b7b60001463940e03` |
| 有限 words | `129248 / 129248` |
| zero words | `31` |
| 其中负零 | `8` |
| 相对 actual28 基态改变的 words | `118878` |
| 有改变的原节点 | `577 / 577` |

变化数由已保存字节对照核验，没有在本地重新算 `base+alpha*delta`。本次不是全零方向或候选数组逐位不变的情形；这项实际证据不倒推 actual57 范数不变的唯一原因。

selected 文件身份：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `selected-state.f64le.gz` | `954571` | `8ade070f746caed9a45c582c7485a060e55ee589858f5f88255d8ffd0d9112cb` |
| `selected-state-checkpoint.json.gz` | `1255992` | `7659016c0218b8c2e9ba220ca81a0b410b7e38005ea609e417b9b534d76c3556` |

checkpoint 的 raw JSON SHA 是 `b38dcd3bbdc8645ebfe3eabdcfa096c540357130cf0f712e45604f0715ec09ef`，raw JSON 大小 `3005552`。其中完整 rows 和 `negative_zero_columns` 恢复后与 raw 状态逐字相同。

本次实际方向本身也完整保留：shape `[577,224]`，raw SHA `22d79a989a13cc99a239735d184d63064751c141f05ded2f5131b198be3d80c0`，129248个有限 word、80个零、其中43个负零。原 cut/far 方向分量未投影或改零。

## 4. 原返回残差和最大位置

原 `evaluate` 返回的完整 stage residuals 和 far residual 直接复制原字节。cut 数组是同一原减法的事后只读拷贝，范围在接口与 metadata 中明确，不冒称原函数原先已返回该数组。

| 实际数组 | shape | raw SHA256 |
|---|---:|---|
| 全 stage residuals | `[576,224]` | `41d327736bb0f462b2dd920933a2af25933a9e4ef395dc5c0e9f564141158592` |
| far residual | `[1,112]` | `61fcea40cbd9eb1ae4220143937a1d8a6d43e6a7b97c1674b9c60125d1dae3ff` |
| cut residual 只读拷贝 | `[1,112]` | `6937668b754c82597e8a40024d14a77ea11fdf82797c812821e5c2f809c0d595` |

三数组中的全部129248个 word均有限。producer 的只读 argmax 扫描记录只有一个最大位置，其扫描 norm bits 与原返回 norm 完全相同：

| 位置/数 | 原记录 |
|---|---|
| stage | `11` |
| raw cell / segment | `0 / 7` |
| component / mode / frequency | `Pi / 76 / 152` |
| stage column / complete global row | `187 / 2763` |
| residual | `6.674619624363887e-19` |
| residual f64le | `0000000000a0283c` |
| 原 sigma | `5.176434974219545e-15` |
| sigma f64le | `3d3e5ef00550f73c` |
| 原尺度绝对 residual | `0.0001289424025918576` |

本地审计逐字核该 witness 的 residual 和 sigma 确实来自本次保存的原数组；**没有在本地重算除法、norm 或 argmax**。最大位置及其数值结论来自公开 Actions 的完整原求值及只读记录。

no-J 返回的 `minA/minD` 都是原代码的 `+Infinity` 占位值，bits `000000000000f07f`；不能把这两个值说成新计算的正性裕量。原所有 stage 实际返回才是本次 no-J 没有 guard 失败的证据。

## 5. 来源、负零及记录范围核验

纯stdlib audit 对 trial 目录的34件文件和 result 中26件 small-file 清单逐SHA核对；完整方向 raw/checkpoint、原 operand receipts、实际 input/r/cut/end、argmax witness、selected rows/负零、原 callback 与 observer 的别名都通过。

实际 observed evaluate 源 SHA 是 `cff3bf72887e95ead5623a60c4d04875ed7787cb5ec200dad6cf542fe5371606`。去掉声明的两个只读插入后，精确恢复原 evaluate `9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9`。实际 public `Function.toString` 与恢复参考视图分别保留，没有伪装。

原十 trial 正文 SHA 仍为 `603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99`。原 internal solve 从声明的两个调用替换和 finish observer精确还原为 `d7d063fe2fca25c1742c68ec8056902a583952b61cdda98e1d9eaab7c09f3615`。

actual trial `result.json` SHA 是 `c0a9b191e843e9036e84707ffa1855d5881dce13e4b71bf94812e9526b59d00e`；`trial-replay-summary.json` SHA 是 `770b97e62eda7cbcc10b045c42298b95ef2c55a0f2dd5ac1930690175a156709`。

审计器为 `geometry_20261114_original576_trial_byte_audit.py`，SHA `69c840ddf2f155e3baa560d07653fb544ef40780b2222ff0713632196faf1620`；实际审计 JSON SHA 为 `ffa7e1884d4277fc8a8a5101db4cd62e36d393c05a6e95cec1661d1b59a91000`。审计仅解析原件、hash和bits/source，不运行 native/RHS/J/ODE、QR、候选算术或任何科学范数。

QR 因子、完整常数行、R273 formed model及两方向在原576矩阵的全exact读回由独立线性结果报告说明；本note不把trial字节审扩称重审因子。

## 6. 原计划停止与下一真正求解状态

原 worker 返回的本次消息是：

```text
Error: VISIBLE_NATIVE_ORIGINAL576_DAMPED_TRIAL_REPLAY_ACCEPTED_STOP_V1
```

这是在原alpha1接受、完整selected保存后抛出的计划停止。`success=False`、`converged=False`、`native_tail_response=False`、`endpoint_J_computed=False`、`fresh_endpoint_audit_computed=False`、`task_completed=False` 都保持真实范围。

后继可从上述实际selected的完整原字节继续。它的 H 仍是原全部112个非零高度系数，不能阈值化；原图、far、sigma和g保持。softcut可能有残差，不能把selected node0强制改回target。继续求解时每轮必须对当前状态执行真正原with-J，再构造本轮完整576方向；actual28缓存不得冒充新基态。R273只替换非线性校正调用，最终端点 sensitivity/J和fresh audit仍须原真实流程支付。
