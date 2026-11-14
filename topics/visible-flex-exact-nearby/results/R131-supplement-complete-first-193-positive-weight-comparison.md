# R131 补篇：前 193 个完整正权闭盒的同一误差传播

**状态：已证明所列精确前缀的真实 Cauchy 继续与误差界。**
本条消费已经真正完成的两份原生记录，不修改任何未完成报告，不授完整 `[0,1/5]`、几何嵌入或闭曲面族。

## 1. 对象与准确连续区间

目标仍是原完整 primitive 对象的径向度量，原准确参数中心
`−7789843107295549/4611686018427387904` 和整个 `|η|≤10^−9`。
原完整 1024 候选、s10 正权和实际腰初值都保持原身份。

| 原 partition 行 | 完整闭区间 | 原生文件 |
|---|---|---|
| 0–95，共 96 盒 | `[0,4531033103068763/144115188075855872]` | `2026-11-13-Codazzi-positive-weight-batched-s10-r02-part-000a-native.json.gz` |
| 96–192，共 97 盒 | `[4531033103068763/144115188075855872,17317649385345/281474976710656]` | `2026-11-13-Codazzi-positive-weight-batched-s10-r02-part-000b-native.json.gz` |

两原生进程都正常结束，报告 `complete=true`、`failure=null`，各自 `covered_interval` 与请求区间完全相同。使用全部 4096 角节点所覆盖的闭角盒、完整 Fourier 多项式及全部 scalar germ 余项；whole-parameter、整个实角圆周、均值、完整非线性管和真目标费用均保留。

## 2. 已证明的比较定理在两份完整数据上的应用

采用 [完整正权比较](R131-supplement-positive-comparison-weights-and-cleared-tube-rows.md) 和
[明确原始 producer 身份的分片消费](R131-supplement-explicit-piece-producer-identity.md)。
消费者为 `fourfold_codazzi_positive_weight_batched_piece_C0_v3.py`。
它逐项核原 producer kind/source、全部输入和依赖 SHA、原目标/完整 BC/完整权/实际初值身份、准确原 partition 行号及每盒所属实际 scalar germ。

两片来自同一个全局正权函数。令 $P=(\widehat B+k)/\widehat C$、$Q=(\widehat B-k)/\widehat C$，
$$
z(r)=\max\{\|(p-P)/W_p\|_\infty,\|(q-Q)/W_q\|_\infty\}.
$$
这里是实际 Riemann 场误差；原程序一直使用此量。
消费者在第 95/96 盒交界继续携带同一个已证明的 $z$ 上界，以及独立真实一阶梯度上界；没有把第二片当作一个零误差新初值。
每个原闭盒执行完整比较率、余项、严格屏障及未加权管门 (W_{max}z<T)，并保真分母间隙和曲率符号门。

五个原已付管 `1/500,1/200,1/100,1/50,1/16` 全部通过准确的 193 盒前缀。
其中 `T=1/500` 给以下向外取整的全前缀界：

| 量 | 有效界 |
|---|---:|
| 最大实际未加权 C0 误差 | `<0.000111237119` |
| 右端同一加权误差 | `<0.00001547201624` |
| 全段真分母间隙 | `>0.24339366397` |
| 全段目标 `−K` | `>0.89373184740` |
| 右端独立真实加权梯度 | `<278.9233061` |
| 全段独立真实一阶角导 | `<1131.0857891` |

这些梯度界来自原 R131 的真解导数比较，不是给候选误差另加一个未经证明的 C1 屏障。表中数值的准确 Arb 包络及全部 193×5 行均在完整 C0 报告中。

## 3. 完整证据与第二次消费核验

本条保存两份原生记录的全部行和全部管，而非只保存最后一行。完整消费者输出为
`notes/2026-11-13-R131-positive-weight-complete-first-193-C0-native.json.gz`。
root 在新路径再次实际执行同一严格消费者；解压后的完整 JSON 完全相同，全部绑定输入和源码 SHA 又逐项核对。核验记录为
`notes/2026-11-13-R131-complete-first-193-root-replay.json`，文件清单绑定所有新证据。

可按以下准确参数重做，输出路径必须不存在：

```bash
python scripts/fourfold_codazzi_positive_weight_batched_piece_C0_v3.py \
  --native-parts \
    notes/2026-11-13-Codazzi-positive-weight-batched-s10-r02-part-000a-native.json.gz \
    notes/2026-11-13-Codazzi-positive-weight-batched-s10-r02-part-000b-native.json.gz \
  --right 17317649385345/281474976710656 \
  --out /tmp/first-193-complete-weight-replay.json.gz
```

剩余原 partition 193–385 与 386–578 正在各自完整计算。本条未消费其未完成前缀。
最终 `[0,1/5]` 必须等四片都真实完成后，从同一腰初值重新消费全部 579 行，并执行所有未加权管/真分母/真一阶门。
原已有 `[0,1/10]` 的其他 C0 证书和本次较小区间上的更紧正权误差证书各按自身数据成立；不互相替换输入或扩大证明范围。
