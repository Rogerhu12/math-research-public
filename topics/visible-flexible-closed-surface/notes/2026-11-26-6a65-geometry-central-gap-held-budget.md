# 中央 gap 条件预算的实际输入与执行

完整证明已登记为 [R222](../results/R222-central-gap-conditional-held-and-ramp-budget.md)。本记录的旧全场数值属于启发式/有限数值证据，明确不把重构记录冒充旧文件。

## 身份与实际输入

本条不产生新 gap 的完整位置场，也不把改变中央间隙称为同一 \(g\) 的改进。
原输入是已经实际 exit 0 的完整 1788 列 pure-clock 拟合场，原报告名为
`geometry-work/cauchy-clock-fit02-value-monitored-baseline.json`，
当时报告的 SHA256 为
`01725d3b221e5d0f8d0580ac332f957e8183edc6bcacd3b664743197a4ee46e2`。
该报告的有限观察给出 held 最小距 `0.6263963331525163`、
`maxAbsoluteY=0.8283679419627915`、
自身最大主曲率 `18.630497499487163`。
现有场尚不满足完整目标。

原报告字节随临时环境失联而丢失。本次明确保存
`central-gap-recorded-observations.json` 作为已经报告过的少量观察值的重构记录，
其 `recordedNotOriginalBaseline=true`，不是原始 baseline 或新场评价。
预算程序必须用 `--recorded-input` 消费这份记录；
输出的 `sourceBaselineSHA256=null`，
旧报告哈希仅列在 `recordedOriginalBaselineSHA256`，
新的记录和源码各有自己的实际哈希。

本条精确证明两件事：固定周长的中央椭圆族中哪些 gap 仍满足中央曲率预算；
以及**假定既有位置集合不动且具有指定距离、宽度界**时，
移动 held 参照点能增加多少距离。旧位置界来自有限观察，未成为连续域证书。
新 gap 的真正全场必须重建和重新评价。

## 6. 执行、哈希与关联

本条消费 R116 的 GC 方程、R219 的完整帽输入及已经发表的 pure-clock 场，
不重证既有封帽结论。
程序只用 Python 标准库。

```sh
python scripts/6a65-geometry-central-gap-held-budget.py \
  --recorded-input notes/2026-11-26-6a65-central-gap-recorded-observations.json \
  /tmp/fresh-central-gap-held-budget.json
```

重构完整版已实际自然 exit 0，内部用时 `0.30744218826293945` 秒。
11 个 gap 的精确端点盒、连续 gap 区间所需端点断言、
.65 guide 的 witness 排除式和两个 ramp 门槛全部通过。
实际文件 SHA256：

| 文件 | SHA256 |
|---|---|
| `6a65-geometry-central-gap-held-budget.py` | `001f8f4907a9ed165b9ac99ec35e0144999b3f73e3a5a32ede3f6916fb67aed9` |
| `central-gap-recorded-observations.json` | `b3dc47bb68288cd2dde48449b0e042169aac44e916f6264c2bb9144bebfa7ca1` |
| `central-gap-held-budget-recovered.json` | `e2eed168337fbe8db8ae8115175254e1734868e20f6fb134136048168a074f0a` |

较早的初版在临时环境失联前也实际自然 exit 0，记录用时约 `.278` 秒，
但其源码或报告 SHA 未读回，不补造。
恢复后的内存有理核心另曾实际 exit 0，内部用时 `.2702600955963135` 秒；
那次没有写文件，不与上表的重构完整版文件身份混同。
三个执行记录都没有新 gap 全场求解或连续域 reach 证书。
