# Request77：根据actual75开启原R259的有限Newton候选搜索

日期：2026-11-15 UTC。作者：/root，GPT-6 Astra Pro（AI-assisted）。

[实际75结论](2026-11-15-actual75-circle-reference-and-untuned-small-core-resonances.md)已记录：完整真实112×112零尾slope J逐项对角，三个原目标非零，但p=(0,0,0)的三条单位共振缺陷未小。因而直接启用原冻结入口已经实现的八步候选搜索；不改变科学源码，不把零核心圆参考当作非零warm。

## 唯一改变及真实依据

原入口仍为 `geometry_20261114_small_core_resonance.py`，SHA256 `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5`。唯一科学选项变化是 `--newton-steps 0` 改为 `--newton-steps 8`；初始控制0,0,0、12次回溯、原候选阈值1e−8、160bit/depth14、原699节点、完整112尾和四个固定输入均不变。

实际75原status SHA为 `665f1bd36a4a75eded331a4a9697c4ebaeaa411834365e405fe214c0439bd969`，run43660412919/source3a0646db263f224acd347432967b93239faa836c。该事实只决定本次开启现有搜索；77仍重新读取同一固定真实零J，并由原代码核对严格对角和非零目标条件，不以先前摘要代替本次输入。

八步是该已有算法的有限候选预算。每次候选实际重建圆collocation与低三传输，按原真实方程的merit、方向斜率及12档回溯选择，最后保完整scalar区间检查、原FFT/节点/中点/RMS参考读出。没有新native、非零振幅场或完整full-DN调用；未求高自由core Schur、未证明高模式非共振或区间横截性。

## 接线与保全

- 唯一原触发路径：`topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json`。
- 请求SHA：`77f163f5480511bd783f90d0005e6571b0707afba21a3f65dfd11b8e3025b193`。
- 同一small-core工作流的新SHA：`f8ffdc9ced1d6eca5beea44efe71caea86f80269706a3bde4c5c8bc21b2018fb`。
- 68件原source pins、四个数学输入和publisher22e640bb均保持；原完整回溯/域检查/输出与失败保全不变。
- 7段bash语法、4段内联Python AST及YAML通过，静态回执为 `request77-static-check.json`；没有本地科学运算。

工程时限仍45分钟科学step/60分钟job，记录真实耗时与可能的中断。原candidate阈值不成为本题新增验收门；候选若找到，仍须实际非零场、真实非零尾、原FD/RMS/BC和最终fresh audit。73原生尾与76前缀主线继续，并不等待这个备用搜索。
