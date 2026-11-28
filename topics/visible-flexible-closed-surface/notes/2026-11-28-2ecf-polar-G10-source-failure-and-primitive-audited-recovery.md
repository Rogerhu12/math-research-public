# G10 源生成的实际失败、内层精度恢复与原位 primitive 复核

958径点（每个54个非空span含完整G10，保全部旧205与第三观察径点）的目标没有改变。本条登记原source消费失败和新的恢复入口，不把未完成缓存冒作完整成功；G10新有限基线和接受数仍需两组完整生成以后另付。

## 1. 原位失败及已完成前缀

原 `2ecf-polar-c2-g10-prepare.py cache --group training` 为753个新增径点生成128角源。在外部1294.517242757秒后自然 OS exit=1，peak child RSS207928KiB。真正异常：

```text
Safeguarded literal inverse unresolved: side=0, indices=[84],
maximumResidual=1.5631940186722204e-13,
maximumBracketWidth=8.881784197001252e-16
```

失败点是新增径点索引667（从0开始） `s=0.856679790800223`、128角中的索引84。原日志最后正式完成并flush的进度回执为665行。原memmap有667个非零行，但后两行缺少正式完成日志；新consumer只复用前665行，余88行全部重新实际计算。原失败 exit=1、日志和原数组哈希保留，不改成成功。

对该同一个s重新按全128、2块、4块、8块、128个单角逐步实际求值，均在同一个物理角复现失败。因而没有用重分块偶然跨过原门槛。

## 2. 门槛冲突定位和实际修复

外层polar inverse要求角残差严格小于5e−14，内层R137 material inverse原默认残差是2e−13。失败时外层括宽已到约一个binary64 ulp，继续二分不能消除内层近似值的跳变。

保持全部数学Fourier系数、端口公式、Hermite/height公式、物理(s,u)、原目标g和 **原外层5e−14门不变**，只对失败源行将内层material tolerance从2e−13收紧到2e−15、上限100次。该同一个全128角源行实际成功，最大外层角残差7.105427357601002e−15，调用4.283002865秒。进一步盲收紧到5e−16反而实际失败（10.904942484秒，内层迭代界），同样保留此失败，不宣传“越小越可靠”。

新 `2ecf-polar-tight-source-evaluator.py` 只在实际原source抛出上述外层异常后启动refinement；其它source行仍调用完整原函数。原源码文件不修改，新评估consumer单独有SHA。它改变浮点求值流程，而不改变原数学source或目标g的定义。

## 3. 不依赖原双精度门的返回根原位审计

恢复时逐字重现原compatible fast8+bracketed64算法，并保存实际返回的每个根u和对应theta。随后在这些固定返回根处独立重评估角方程，不再让另一遍Newton替换这些根：

- 原191 Fourier系数作为相同binary64字面输入，改用longdouble complex指数/求和，实际mantissa64bit。
- 保留原arc累计锚、cuts、normalization等字面常数；局部primitive与逆图用longdouble，材料逆图更精确。
- 分别用原Gauss16与独立Gauss32局部primitive，检查相同根和目标theta。
- 这检查有限原位求值误差，不是全角/全域区间证书，也未将原有限quadrature冒作精确积分。

两组primitive均给：

| 实际量 | side0 | side1 |
|---|---:|---:|
| 原位更高精度角方程最大残差 | 5.0879439550e−15 | 8.8991314318e−16 |
| polar logrho 全两jet最大差 | 7.1365136023e−13 | 0 |
| polar rho 全两jet最大差 | 9.3169916227e−13 | 0 |
| polar z 全两jet最大差 | 2.6027791034e−14 | 0 |

longdouble局部arc逆图实际最大残差4.336808689942018e−19。这里profile两jet差是已固定返回根处tight binary64与更高精度primitive的有限差，不是“所有source两jet统一误差上界”。审计进程实际自然exit=0；没有记录可信外部总时长，故不编造秒数。新恢复producer运行时的真实审计成本会包含在各自外部OS回执中。

## 4. 新恢复consumer与完整性

入口 `2ecf-polar-c2-g10-resume-prepare.py`：

- training只接收正式665行回执，复用前逐字比对数组；另实际重采原索引0、332、664，要求完整六jet及radius字节一致。
- 每完成并flush一个新行，单独写 `-completed-rows.jsonl`，后续恢复不再依赖每8行打印。
- observer组实际重算全部753新行，不借training不同角的样本。
- 两组均保全部原205行原六jet/radius字节；958径点、原128/192角、完整12789列及固定g不变。
- 所有fallback单独保存实际异常、全部返回根/目标theta、Gauss16/32原位残差和profile两jet差；任何更高精度原位残差未过原5e−14就拒绝本行。
- 安装已单独实核字节相等的 exact-input memoization，只缓存相同输入的原exp和原theta结果，miss运算序不变；其SHA也绑定，不能把以后优化静默塞回旧身份。
- 原目标oracle仍须实际自然exit=0，两组完整后才assemble新的prepared。此处没有把运行中的组当完整prepared。

实际新prefix `polar-c2-G10r`。固定g求解器显式传 `--prepare-entry .../2ecf-polar-c2-g10-resume-prepare.py`，新prepared全hash身份独立于失败的旧G10入口。所有已有G2状态只转移同一12789系数场，G10新objective/成本/计数重付。

| 文件 | SHA256 |
|---|---|
| `2ecf-polar-c2-g10-prepare.py` | `1476272aae1cddeed747b2d26be4b6730a22fc26957cdf9689561b5e16ef814e` |
| `2ecf-polar-c2-g10-resume-prepare.py` | `d0af059771db8d39b84eba498a73d3154872a5be69a3218dbea340e38f1cd1b6` |
| `2ecf-polar-tight-source-evaluator.py` | `5d91140712ca78df5bf8e62392ad9ddb86915a0b0197d7f3804d4d4a9fe4435a` |
| `2ecf-polar-g10-failure-probe.py` | `29dca0f0a1c7a2edd079cbf75dcdbfdcaddb3c8675b704478f586c297092490c` |
| `2ecf-polar-g10-tight-material-probe.py` | `ab412203fc34b30782bb8b63203641be057ca65c16cd62466496e274a17a1c74` |
| `2ecf-polar-g10-primitive-audit.py` | `fd46ea2c7f0cdbca575b8eb5dc7cb54851cf2ce315b355a09db92c6ca802e80f` |
| `polar-c2-G10-training-source-exit.json` | `8fc4f87264e23c31b53b853df655a27f0bf115e08e4ff9e9c2f3888ff4ddc064` |
| `polar-c2-G10-training-source.log` | `d07bcf645aad63229ca6223e06a301e27f852d378ecc206cb1c462293a8cfbb1` |
| `polar-c2-G10-training-new-jets.npy` | `5d450cb684f713344007ae54379401cb3a446c1fd08a2343f00be5264ea34830` |
| `polar-c2-G10-training-new-radius.npy` | `6a192d22fb964a813126649d5aa7ee4864dbd6fcebdfd12eb1003ce034b413c1` |
| `polar-G10-failure-probe.json` | `30451f764fe0c2cb8bc58b36b65893d8c1d98c61b5c4b7e4c337267c5446236d` |
| `polar-G10-tight-material-probe.json` | `4f0b567d6e4fe44e0aeb897c484f5a4512846c34723e154212b94232d030dcf8` |
| `polar-G10-primitive-audit.json` | `b15e08e03956dcd1778975527b6445a0b07fc9a2a9f956d8131f2c4c40ea92ba` |

以上没有全域source证界、连续metric证书、whole closed reach证书或完成宣称。
