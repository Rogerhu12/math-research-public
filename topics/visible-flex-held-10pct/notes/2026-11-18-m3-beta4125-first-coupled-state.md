# beta0=4.125 的实际联合锚点：q=.02

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
UTC 2026-11-17 19:43 后完成。承接 beta0=3.625 的已 accepted
q=.02 prefix–tail 状态，只把第一个 valley control 改为 4.125，
其余控制参数固定。全局重标定系数随之改变整个 r(x) 的分配；
这是新物理 g 的设计，不能称后部物理函数未变或同 g refinement。

## 完整实际联立结果

原 M8、spacing3、depth8、parts8、RK16、quadrature128、
linearFar48/linearSteps512 保留；实际 worker 的 DN 首斜率为
21.575474149073226。采用显式新 g 线性差初值，随后求解全非线性
尾部和 prefix。delta 重解为 `.06105607210171944`，936 个径向节点。

| 检查量 | 最终数值 |
|---|---:|
| prefix solver_success | true |
| prefix sampled metric FFT l1 | 2.8846498322013053e-9 |
| prefix sampled Cartesian Darboux tensor FFT l1 | 5.6473114874431e-5 |
| prefix sampled κmax | 8.050355751166677 |
| 最终 actual tail residual | 6.178663592424988e-10 |
| tail flow min A | .8008088162702014 |
| tail audit sampled min A | .8008209998678861 |
| tail sampled full Darboux defect | 1.7815218336811155e-8 |
| tail sampled actual metric | 2.521760578180417e-12 |
| tail sampled formal curvature | 8.063569752249412 |
| actual physical BC | 1.1778923960227645e-10 |

首次 tail warmup residual 为 6.222175075524379e-10。实际 Jacobian
驱动 prefix 内解之后，第 3 次 tail 对新 H 通过，第 4 次完整
audit 再次得到表中的最终 residual。它满足原 `2e-9` 门槛，不是
只记录较小的线性 DN 或启动尾响应。

最终 mean 一阶和二阶 jet 差为 -8.507083926190262e-14、
-7.999378937029178e-12；非 mean 一阶、二阶差为
1.1778923960471333e-10、2.7682240206702846e-9。
cut metric 与 C1 metric FFT l1 为 1.8728165039965274e-13、
1.841585397790197e-12。所有 cut 谐波都在实际联立中保留。

## 与前一物理设计比较

beta0=3.625/q=.02 的 accepted tail full Darboux defect 为
2.821838319302809e-6，actual metric 为 3.2508129521602634e-10。
新设计的这两个有限诊断分别降低约 158 倍和 129 倍，实际 min A
也从 .67674 提升到 .80081。两边各自重新求过 prefix 和 H，因此
这不是固定 H 的对照，也不是同 g 的网格收敛证明。

这份单一有限状态仍未建立精确连续闭曲面族、全角 C² 误差界、
全局嵌入或 reach 证书；完整 README 完成标准尚未满足。
下一次已启动同 beta0 的 q=.025 实际继续，delta 再次求解。

## 复现

入口 `scripts/resume_m3/continue_valley_design.py --beta0 4.125
--amplitude .020`，旧输入是 beta0=3.625/q=.02 accepted prefix、
最终 tail 与实际 port；source 副本使用
`install_valley_design_initializer.py` 和
`install_valley_linear_difference.py`。实际 cut 数值 r 的旧/新差
为 5.551115123125783e-17，在已记录解析 cut 舍入检查内；未改写
输入 cut 数值以伪造同 g。

完整命令、source/input/output SHA-256 和终态标量位于
`scripts/resume_m3/beta4125_q020_coupled_record.json`。
主要可再生输出散列：

- prefix：`ff93da79896012b894b1b9226f70677c6737455ddf1a201ee231dc9b7d8c443a`；
- 最终 tail：`4f13212bf2620b40f09484981838e8954ceab11fc69735a43144f9dd5c668130`。

场、网格和 checkpoint 只留在 scratch，没有提交可再生数据。
