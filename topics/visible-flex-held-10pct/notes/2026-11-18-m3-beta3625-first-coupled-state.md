# 首谷 beta0=3.625 的第一个真实前缀–尾部联合锚点

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
UTC 2026-11-17 19:18:40 后终态。承接
`2026-11-18-m3-new-first-valley-actual-start.md`，新 beta0=3.625 下
q=.02 已完成前缀校正及校正后实际尾部复核；不是只通过启动 warmup。

## 参数与实际接受结果

只有第一项 valley control 从旧设计 3.125 改为 3.625，其余尾部控制
参数、双脉冲控制和后续 valley controls 不变。全局重标定系数会随之
改变，整个 r(x) 的分配也会改变，不能称后部物理函数不变。同源 M8、spacing3、depth8、parts8、RK16、
quadrature128、linearFar48、linearSteps512，原全局门槛 `2e-9`。
prefix 的 delta 在新物理 port 下重解，结果
`delta=.06105607495644815`，q=.02，936 个径向节点。

| 检查量 | 最终值 |
|---|---:|
| prefix `solver_success` | true |
| prefix sampled metric FFT l1 | 2.8847607452601175e-9 |
| prefix sampled Cartesian Darboux tensor FFT l1 | 5.602582255436866e-5 |
| prefix sampled最大曲率 | 8.050355296763517 |
| 最终实际 tail shooting residual | 1.4651335661047553e-9 |
| 实际 tail min A | .6767415337239006 |
| tail sampled actual metric | 3.2508129521602634e-10 |
| tail sampled full Darboux defect | 2.821838319302809e-6 |
| tail sampled formal curvature | 8.05005147010563 |
| 校正后的 actual physical BC | 6.790112896943099e-10 |

第一次真实 tail 响应只使用旧 prefix 的 q 缩放初值，残差
1.7953077024630326e-9。第二次求出其实际 DN Jacobian，随后重新求解
prefix。第三次针对校正后的 H 得到上述最终 residual；第四次再对
同一个实际 H 做完整尾部 audit，仍通过门槛。只以后两次作为联合
状态证据。

实际 outer check 的缩放边界残差为
3.3950564484715495e-8，按原 bcweights 对应表中的物理 BC。
prefix 与 tail 的两阶 cut jet 差为：mean 一阶
1.7932044737989372e-12，mean 二阶 -3.903974921115605e-10，
非 mean 一阶 6.790113512688406e-10，非 mean 二阶
1.586808023000541e-8。cut metric 与 C1 metric FFT l1 分别为
1.7755053079337236e-13 和 2.0303676742876854e-12。
它们仍是有限数值接缝检查，不是精确 C² 接缝证明。

最终 cut H 的第一项为 -5.46705358562239e-5，第二项为
6.710720870336884e-7。其余全部谐波都参与 actual DN 和 prefix
边界条件；没有以线性 DN 或单主模替换完整向量。

## 与上一批失败的关系

在旧 q=.025 的 H 上直接改变 beta0 的运行已经登记为失败。
本次首先把目标改为 q=.02，再在新 g 下重新求 prefix，因而获得
了实际 accepted 的新设计锚点。两者不同，不能把旧 q=.025 的失败
改写成通过，也不能宣称新设计的幅值上限已经超过旧 q=.025。

此处只建立一个新设计的有限联合状态。没有建立同一 g 的连续
形变族、全角/全空间严格界、无限尾闭合、整体嵌入或 reach，也没有
满足 README 的完整 10% 完成标准。正向继续已启动同 beta0 的
q=.0225，下一次仍要求完整实际联立和原门槛。

## 复现

精确命令、输入及输出 SHA-256、source SHA-256 和全部终态标量在
`scripts/resume_m3/beta3625_q020_coupled_record.json`。
入口为 `continue_valley_design.py --beta0 3.625 --amplitude .020`；
输入是已登记旧 q=.025 accepted prefix/tail 及其字节匹配的 port。
独立 source 副本依次安装 `install_valley_design_initializer.py` 与
`install_valley_linear_difference.py`。所有新 g 构造、prefix restart
和 actual DN 的区别按前一笔记录显式保留。

关键可再生输出散列：

- prefix `seed.json.gz`：
  `bd905caeeff4d8cae23154df279edcd891aa2709cd04429a82812e03c2723a9c`；
- 最后真实 tail `seed_tail_0004.json.gz`：
  `192cf7bfae384f9f7417782e28e020eccdba8ee9e6d778cc0422e4bd53ae6dc8`；
- 标量终态 `seed-summary.json`：
  `9781a3bfa0ceec07170db48b0a523cc4317abd727c30b0653dbc693fff31df6a`。

这些场输出只在 scratch 保留，未提交数据、网格或 checkpoint。
