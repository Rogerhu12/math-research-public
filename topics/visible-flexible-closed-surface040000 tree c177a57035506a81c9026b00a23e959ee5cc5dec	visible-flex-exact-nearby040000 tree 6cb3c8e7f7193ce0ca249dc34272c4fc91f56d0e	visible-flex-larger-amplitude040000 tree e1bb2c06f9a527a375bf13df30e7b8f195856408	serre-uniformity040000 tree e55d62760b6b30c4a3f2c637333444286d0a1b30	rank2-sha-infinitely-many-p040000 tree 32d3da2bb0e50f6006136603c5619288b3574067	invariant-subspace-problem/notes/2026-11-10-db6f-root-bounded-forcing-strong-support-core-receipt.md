# 有界 forcing 强支撑核：作者实际有理检查回执

状态：实际完成，仅有限有理比较。完整数学作者稿仍待未参与者全文独审。

- 实际V8开始/结束：2026-11-10 00:43:56 UTC / 2026-11-10 00:43:56 UTC；functions.exec正常完成。
- 从固定commit fb9c9d106be35e52fc17bc91ddaf4895c0817dc4 的唯一JavaScript围栏提取后实际执行；
  blob 32a23264bab0138aba1d67dc24d9310aeb3e6d0b，全文SHA256 2052d22f434067cc97875c100fd9183e8213a3357b06f6fa28bc88acc3af6b98。
- 冻结代码 2853 ASCII B，SHA256 b215925f779f522ba32c4d6174b5b5e738fa90d3db13881f679d497abb2c15d1。
- 28 项检查全部通过。没有Python、PDE、曲线/网格数组或主solver运行。
- 来源已先冻结并固定回读，未预填运行结果；独立者的重跑仍须另有自身回执。

| 检查 | 精确左值 | 精确右值 | 结果 |
|---|---:|---:|---|
| plateau left | 2/5 | 7/20 | PASS |
| plateau right | 3/2 | 7/5 | PASS |
| Taylor integral lower | 33523601/56250000 | 59/100 | PASS |
| rho lower | 1/10 | 1/10 | PASS |
| rho upper | 19/10 | 19/10 | PASS |
| material chord | 7/209 | 1/30 | PASS |
| perturbation small | 1/30 | 1/100000 | PASS |
| normal cross column | 3/100000 | 200001/10000000000 | PASS |
| reach exact | 99940009/1045950000 | 99940009/1045950000 | PASS |
| reach absolute | 99940009/1045950000 | 3/32 | PASS |
| L budget | 1/2000000 | 10000001/50000000000000 | PASS |
| ru budget | 1/50 | 1001/100000 | PASS |
| uu budget | 1/50 | 531/50000 | PASS |
| directional Hessian | 1/1 | 7/100 | PASS |
| H chord | 591/1000 | 591/1000 | PASS |
| whole initial diameter budget | 1011/500 | 1011/500 | PASS |
| diameter convenient bound | 51/25 | 1011/500 | PASS |
| H ratio | 197/680 | 1/4 | PASS |
| north increment | 531/1000 | 531/1000 | PASS |
| held gap | 53/100 | 53/100 | PASS |
| held ratio | 53/204 | 53/204 | PASS |
| held strong | 53/204 | 1/4 | PASS |
| diameter witness | 1281961/250000 | 81/16 | PASS |
| rigid quotient gap | 21/200 | 21/200 | PASS |
| rigid quotient ratio | 7/136 | 7/136 | PASS |
| rigid quotient strong | 7/136 | 1/20 | PASS |
| reach normalized | 25/544 | 25/544 | PASS |
| reach normalized target | 25/544 | 3/100 | PASS |

本回执只支付文中有限常数。完整forcing周期、凸体、全法锥、两段PDE应用、真实位置与整像比例须依完整证明及独审；仍未闭合。
