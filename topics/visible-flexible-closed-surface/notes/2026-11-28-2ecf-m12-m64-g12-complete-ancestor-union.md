# M12：M64/G12全部七阶段自然结束与真实祖先观察

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。

这是前条 `2026-11-28-2ecf-m12-m64-g12-actual-field-and-span-peaks.md` 冻结后真实返回的补记。实际场仍为 `3ca49d46da9c13392f93cd3a6f1dcc6a1cdc906731c4571adae7800405c93b54`，实际输入仍是原M48/G6场准确注入所得 `06871d00d7c7c893b3e432da14ba358d2f1893a55ca021b428b533badf8ab4e5`；没有重求、改g或替换父态。

## 最后观察与自然终态

全部原G8祖先集合中当前G14未含的3912个点保留，连同当前6818个G14点，构成10730个径向点的真实union；全部使用N3072。每个点的before都评价上述实际暖输入，每个after都评价上述实际保存场，沿用原source、g与物理s二jet，没有混入source-zero before。

| 同一实际点集 | 暖输入 | 保存的新场 |
|---|---:|---:|
| 完整祖先union metric peak | 6.089598376967154e−10 | 5.424143958602297e−10 |
| union curvature peak | 6.428917975685667 | 6.428917514613397 |
| union support lower | 0.8178848939287313 | 0.8178848938021344 |

union阶段自然exit0，墙时562.647455917秒（其receipt内部计时562.299970445秒）。这只保留真实观察集合，不给并集随意拼装求积权重，也不把有限观察上界当连续全域证书。

此后原参数化driver自然exit0，`finished=true`。其七阶段——准确warm transfer、完整原g H2 LM、R226、旧global geometry消费者、旧R236、两个旧micro窗口、实际祖先union——均有真实exit0；不存在仍等待的旧观察进程。旧R236三角metric界4.916580206851371e−5仍如前条如实未过。新的全域相关Gram/reach证书须另对同场支付，不能借其他field的结论；原B=2e−9门也不由这些样本代替。

## 可重生与结果绑定

全部七阶段可由前条完整 `2ecf-m12-refinement-execute.py` 命令重生。若只重新执行本条观察，在已重生实际暖输入与实际新场后：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-quadrature-observer-union.py --scripts scripts --data <M12-prefix-data> --grid <actual-M64-output>/grid.json --initial-field <actual-M64-output>/warm-transfer.json.field.npz --field <actual-M64-output>/result.json.field.npz --result <actual-M64-output>/result.json --query-report <actual-G12-source>/exact-tail-queries.json --query-cache <actual-G12-source>/exact-tail-queries.json.npz --out /tmp/m12-M64-actual-union.json
```

- `ancestor-observer-union.json` SHA256 `853bf9c450526d7c53833d15f6150f511a7013337eedf5e75a62190d5e9c70fa`。
- 完全结束的 `execution.json` SHA256 `8b76086983bf4ba94d7014d13826d9d1726bd3127ab3ed4da24a68d34e6b744a`。
- union消费者 SHA256 `eb8753969c3871705997f15bc153eaa3b0e1c6632b4f675f5492466cfa65487f`；本条没有新的实现变化。

真正后继物理h503支已按该实际场的热点启动，并继续独立支付新的接受、观察及连续后验；本条管线终态不是本课题完成宣告。
