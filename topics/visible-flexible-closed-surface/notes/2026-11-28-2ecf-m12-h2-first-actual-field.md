# 首个原 M12 保 H2 增量的完整直接步：真实下降，连续旧界尚未通过

日期：2026-11-28。身份：原有限尾 source、原 g、h487/M32/N384/G6，47,628 个 Cartesian 全列。此分支从实际零系数初始化，**不是**既有 h487 暖场续解；原 LSMR 重生分支仍独立运行。新场不是 README 完成结论。

## 实际非线性步

入口为 `2ecf-m12-h2-cached-direct-lm.py`，H2 核为 `2ecf-m12-h2-direct-lm.py`。本步解 `(JᵀJ + 10^-12 S2)d = -Jᵀr`，完整三 Gram 行、所有角向交叉通道均保留。S2 只作用于本次增量，非线性 g 和目标函数不变。真实接受 alpha=1；并非只返回一条提议方向。

| 观察 | 初始 | 实际更新后 |
|---|---:|---:|
| 训练全部 G6/N384 点最大度量误差 | 1.9672357520761352e-8 | 8.260458611849639e-10 |
| 训练加权能量 | 4.516974804254324e-19 | 4.566061443149597e-21 |
| 独立全部 G8/N768 点最大度量误差 | 1.96715752576182e-8 | 8.260458152801774e-10 |
| 独立加权能量 | 4.518839905395179e-19 | 5.4506414287167756e-21 |
| 独立曲率峰 | 6.416878776645082 | 6.416881801138602 |

正则化法方程的真实物理 J/Jᵀ 后验相对残差为 2.185940703255659e-13；**未正则化**原法方程相对残差为 1.0065033435199284e-4。因此不能把此步称为原方程已收敛。方向 H2 范数平方为 5.83089330097796e-10。增量二阶浮点筛选为 .016002173945844213，小于 .05，但该筛选本身不是连续证书。单线程实际运行 394.401262079 秒，resident high-water 744020 KiB。

## 相同实际场的连续消费

真实 R226 报告按全部结点与角度控制六 jets，中心/真 cuff 的三重端点零条件全部成立。旧全 source 几何转移可证 homotopy 嵌入，但 reach/D 下界仅 .024650538180548135，未过 .03；旧粗度量三角界 .0002913189945051292。

较细 R236 消费了同一 field：487 原片、864 接受子片、377 次径向细分，128 个 D3 角区间、96-bit 整数包围；连续 dW Frobenius 上界 4.898136088164749e-6，度量三角界 9.822017620038512e-6，**未过 1e-6**。这里 `source_cross_Gram_cancellation_used=false`。这与实际 Gram 残差采样下降同时成立，不能混同。

全源连续几何是否可由新的 R249 局部二 jet 预算改善，由该 checker 的真实返回另行记录；本条不预告成功。独立 driver 的六个实际阶段现均 exit 0。两原源微区的 546 点/N768 实际峰为 8.260458648889868e-10，位于第二窗口 r=.5133824696921363685、原源 span17477；第一窗口峰为 3.433153761278807e-10。保留全部既有祖先点的实际 union 峰为 8.260458152801774e-10。

## 可复现调用与身份

以既有 h487 grid/query/source-bounds，调用：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
python scripts/2ecf-m12-h2-cached-direct-lm.py \
  --scripts scripts --data PREFIX --grid H487_GRID \
  --query-report QUERY --query-cache QUERY_NPZ \
  --initial-field ZERO_FIELD --initial-result ZERO_BINDING \
  --out RESULT --lambda-step 1e-12 --steps 1 --hessian-step-cap .05
```

ZERO_BINDING 为真实全零 field 与 grid 的哈希绑定，不能拿旧 h487 场或旧结果代替。原源数据 SHA256 `359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0`；grid `b01dd07d72c5e6fd29ac2aefd4029717bb41754494335a85bbf34e29aa72387b`。

- `result.json`：`416d1a541b5ee6ab261b12a097e127e0fb772953060008c844189c450b7ea209`。
- `result.json.field.npz`：`b6425243454a6a019d06a729405b0ebdaa0dbbc68b73b7f62745b1587174be1c`。
- `correction-bounds.json`：`3684cc00854d38a0a429f7288527b908ba43893b620837c5963a01edfe1772a6`。
- `geometry.json`：`d9e657e97c08fbea1142517bf450afa5c8db24b3f702b57a651f04735c8222ab`。
- `metric-budget.json`：`3c15466dd4975579cf824db05a539c65eed13f62f666d9011d7b020c20e95c80`。

原始 field、逐点数组与完整 JSON 仅在 scratch，不进 Git。所有数值是实际本次返回；原 LSMR 再生的最后位差异不被复述为逐字重复旧 CI。

- 完整阶段回执 `microspan-observer.json`：`933398abf3012dc1960479c1418599cc6cb5d23fcd7268c724ccbc4fe9509188`。

- 完整阶段回执 `ancestor-observer-union.json`：`aac222d7a31318cba7fa8f62430741175010da736873ae22441ebf897f6a7512`。

- 完整阶段回执 `execution.json`：`369dafe69e5d89ac5b37cedc06fcbb7bb4e99aee99f162e720b800619721ef9b`。
