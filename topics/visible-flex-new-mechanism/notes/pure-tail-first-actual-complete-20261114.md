# R56 真幂尾第一次实际编译：全历史完成，后阶仍是密度资料

2026-11-14。公开 [run43635287277](https://github.com/Rogerhu12/math-research-public/actions/runs/43635287277)，source `f3102464c049e13cbf306b29cb31cd3d38eb5607`，lane `pure_tail_period`。实际1.960690441秒完成，RSS125.92578125 MiB；不是资源退出或截断。

本次直接调用未改的R56 `forcing_range`，$q=(c-\xi)^8$，保全部有限$t=c-\xi$多项式与14条真实$s$ histories（第二5、第三9）。没有选择某条几何路径、没有把histories置零、没有积分闭桥period。完整DAG4681 nodes。

[R85](../results/R85-pure-fourth-leading-tail-is-an-exact-derivative.md)的第二/第三leading ODE、第四leading密度及其总导数四条原式余项全准确为零；预计最低幂以下也无漏项。这个实际结果与纸证一致，不把自动消掉的第23阶误当第四正成本。

## 输出与可读范围

- [主报告](actions-43635287277-1-pure_tail_period/pure-tail-period.json)：2569 bytes，SHA256 `33e309952f03f46a513102831f9a385e8d7b66dcdf5298e50faa39c8c01ecd77`。
- [可读表达摘要](actions-43635287277-1-pure_tail_period/pure-tail-period-expressions.json)：61569 bytes，SHA256 `edbf48e406952b5b48d01a04046cc14450a5ea9f10c3e6fd164f3227826fe634`。
- [完整未截断DAG](actions-43635287277-1-pure_tail_period/pure-tail-period-structure.json.gz)：压25632 bytes，SHA256 `90b715e9dc146e4170529c28a33178939b3400094c712b86e3fb8e8517408e7f`；解压158711 bytes，SHA256 `c39fc23a88105dbb13efd992b9971b72fb379ff2db543805b5ec0c8278c55ab5`。

可读文件因95KB上限，明确省略第23–27阶的展开文本，不是这些系数为零。五个完整系数均保存在DAG中：

|t幂|DAG root|规范展开项数|
|---|---:|---:|
|23|4649|1612|
|24|4638|1740|
|25|4639|2462|
|26|4640|2225|
|27|4641|2027|

第23阶虽在原history坐标中有1612项，R85已证明其完整period端差为零。因此其他阶的非零展开项数同样不直接证明period非零，更不证明符号。后续须带真实history微分方程和正确端条件分析第24阶起的完整端差与剩余项。

完整结构已经由publisher保存到公开仓库，预压缩字节保持不变；没有仅留临时artifact。新研究代数若需再处理这些DAG仍用公开Actions，本地仅读结构元数据和纸面推导。该结果不构造零第四成本环、不支付P0、ruling或任何主课题几何完成门。
