# M12：同真实父态的 M64/G12 独立角空间支已返回

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。

## 原输入与明确父态

本分支实际父态是原 M48/G6 场 `6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61`。它与 M48/G12 的04r1支共享父态，不是04r1的后继。原 g、source、参数和时间范围都不变；物理网格仍487个unique元素、736个径向自由系数及相同C2 knot multiset。M48→M64把角通道146→194、未知数107456→142784；训练角N768→1536、独立角N1536→3072，径向采用已准确重生的G12/G14与13185查询。

准确嵌入由原 exact Boehm/Fourier transfer 真跑，6.695471951秒，自然exit0；只有高模式零补，没有径向插结点。实际暖场 SHA `06871d00d7c7c893b3e432da14ba358d2f1893a55ca021b428b533badf8ab4e5`，记录真实旧M48/G6 result/grid/R226身份。新 grid 的准备链经过 G12 准备器，不等于伪造已求完的G12父场。

## 真正直接步与独立观察

lambda=1e−13、alpha=1 接受，保原全部三Gram残差行和交叉项。当前新点集上，实际输入和实际新场对比如下：

| 同点量 | 实际暖输入 | 实际新场 |
|---|---:|---:|
| 训练 G12/N1536 metric peak | 6.072532458837339e−10 | 5.424137901119057e−10 |
| 训练 weighted energy | 2.910730669120075e−21 | 2.1387224286851556e−21 |
| 独立 G14/N3072 metric peak | 6.08959701377465e−10 | 5.424140506515565e−10 |
| 独立 weighted energy | 2.9150799370423875e−21 | 2.1422786436418283e−21 |

加密后的独立输入峰6.089597e−10确实高于旧N1536的约6.07253e−10，表中没有借用较粗观察峰。两个独立分支使用不同最终N，不能把有限峰数值差直接当作两张新场的连续全域误差排序。

旧Jacobian线性步的未正则 physical normal 相对量3.881529671999157e−5，正则normal1.867593533187306e−12；只作原有诊断，不添加README完成门。新场的实际 nonlinear JT r 会由已核的新被动入口在后继场记录；这里不把线性步normal改名为它。

## 真实资源和完整场

完整LM自然exit0，2306.88849652秒；峰RSS1,782,956KiB（约1.70GiB），单Gram band1,329,604,608bytes。所有五个全域物理J数组落盘逐行SHA核且逐块恢复；完整Gram装配1149.68317228秒，原位factor5.625382431秒，返回指针核同址。独立观察前已删临时physical数组，RSS269028KiB；最终场保存后3,183,769,542bytes的私有source packet组也已按入口清除。

新场 SHA `3ca49d46da9c13392f93cd3a6f1dcc6a1cdc906731c4571adae7800405c93b54`；同场R226自然exit0，23.732451432秒，公共两端完整correction二jet仍为零。旧全局geometry消费者自然0。随后旧R236也自然exit0（801.173565156秒），487个原元素被严格分成911片，其原target-Frobenius p=2.4569737966281845e−5、旧三角metric界4.916580206851371e−5；该未用source-cross抵消的旧界如实未过，不覆盖较尖锐的后继相关Gram证明。两个旧micro窗口的546点/N3072观察自然exit0（70.403706312秒），峰5.424144791414333e−10，在原source17479、r≈0.5134652116092632635、原元素187。此条冻结时全祖先union仍活动，未先称完成；完整新相关Gram和全时reach后验由同场独立消费者支付，不能借前场证书。

## 真实物理h的选点依据

被动observer未改原统计，共记录487个实际元素，每元素G14有14点。prefix峰为4.794736289336967e−10，在元素153、q≈1.964230751522352；tail峰5.424140506515565e−10在元素187、r≈0.51346557985170107336。实际prefix前8热点是149..156，tail前8是184..191，因而下一真实物理h对这16个元素插中点三重结点。它不改g或角空间，也不把G12积分加密冒作h；真实新场与全域证界仍另行登记。

## 可重生配方

先按已有G12准备/原源扩充记录生成G12 grid和准确原查询；随后：

```bash
python scripts/6a65-m12-frequency-only-grid-prepare.py --old-grid <actual-G12-grid.json> --order 64 --angular 1536 --out <M64-output>/grid.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-refinement-execute.py --scripts scripts --data <M12-prefix-data> --old-grid <actual-M48-G6-grid> --old-field <actual-M48-G6-field> --old-result <actual-M48-G6-result> --old-correction-bounds <actual-M48-G6-R226> --new-grid <M64-output>/grid.json --query-report <actual-G12-query-report> --query-cache <actual-G12-query-cache> --source-bounds <actual-G12-source-bounds> --out-dir <M64-output> --solver-entry scripts/2ecf-m12-h2-disk-normal-cached-lm.py --lambda-step 1e-13 --steps 1 --hessian-step-cap .05
```

默认block24、normal assembly block8；入口是完整原角收缩版，此实际M64运行未中途换成后来的稀疏角核。全部大数组仅临时本地，公开配方可重生。

- `grid.json` SHA256 `39bd8a5acbee30f0e441794623341553097536cf356564a761370d96e099b79a`。
- `warm-transfer.json` SHA256 `7b70f8243ab0658814a80a2fd9eab78ed43ced38c54b08e195d7bf689725d034`。
- `result.json` SHA256 `07046908ccfa92aa3c3325f8fa255ad3f8e53530ec6adf1658931fea75534147`。
- `result.json.field.npz` SHA256 `3ca49d46da9c13392f93cd3a6f1dcc6a1cdc906731c4571adae7800405c93b54`。
- `correction-bounds.json` SHA256 `c4687a94d44ca489da84c5d9abcdb794d22c27104f005873f1fde8078288b426`。

- `metric-budget.json` SHA256 `2574a47312dd1d887118ba12818d7c9ec25c3bebd076d3ef493a9a668da59f5a`。
- `microspan-observer.json` SHA256 `db23c6b7d6fa097dcdcd89675fbb42647ec89069b2db3035a4346037de5e98b0`。
