# 真完整闭图的多个 t 网格导出入口

独立入口 `scripts/resume_20261128/geometry/export_actual_closed_mesh.py` 已完成语法／CLI 实际检查及另一代理逐式只读审查；SHA `38fcc275e1462a5d145dbd7391af36e7febeabfe8a536936e87f7072e78ed412`。**目前没有真实完整 full-H bundle，因此没有执行正向网格导出，没有新闭图或完成结论。**

## 真实输入与握持坐标

入口保留已冻结 `actual_closed_map_coupled_v3.py` 的完整图定义。原来源仍过 `load_actual_prefix`；真正联合来源另给 `--coupling-summary`，通过原 `accepted_coupled` 门并绑定最终 physical H 与同一个实际 packet，不能拿 raw candidate 冒用。

读 bundle 后还重新执行原 `load_packet` 的真实 converged/residual/tolerance/background/cut 门、`validate_packet_states` 的完整谱及实际维数门、`bind_height` 的 reference/factor/arithmetic 身份；要求 factor-one/unscaled。初始化后再按实际原／coupled 来源，以完整二进制 H 核 request/checkpoint。没有新增 native 或 BVP 求解。

默认 `--frame held` 要求真实 λ=1、curvature_blend=1、S=.5、b=.2、实际圆弧 k=.2 及正短柱。它对未校正相位图 Gα 施加 R54 的

\[
F_\alpha=R_{-(1-k)\alpha}G_\alpha+O-R_{k\alpha}O,
\qquad O=\Gamma(\pi/3)-k^{-1}e_{\pi/3},\qquad\alpha(t)=9t/20.
\]

k 使用源的实际字面数，O 是真核心圆弧中心的数学定义；导出坐标和所报 center 仅是这些表达式的浮点评价。不是把浮点 center 当新的严格定义常数。真实 λ<1 不获准进入 held 分支；显式 `--frame phase` 仅可生成低 λ 真完整闭图的诊断相位图，所有 completion/held/reach/metric/noncongruence flags 仍为 false。

R67 固定帽用已审核有理函数直接评价，保无限三重谐波，不截断成 Fourier 有限帽；帽在原相位坐标中固定，最后全图统一作握持刚体变换。柱半长只允许 .0025 或 .005；这里不替代后续选定哪一个长度实际支付活动矩非零的责任。

## 有限网格与完整数学场的区别

每个环的点都评价完整 prefix、真实 R53 lift、最终均值、所有已保存 tail pm/hm 和圆盘帽。prefix/tail/disk 位置公式向量化；正向执行时每环另取三点与原 reader 对照。该有限对照只是适配检查，不是连续误差证书。可视化网格不裁掉数学场的高频系数，也不保证有限采样已解析所有高频。

拓扑按下极点、下半反序环链、唯一中央环、上半正序环链、上极点组成。所有 cut／圆柱／圆盘接缝只用一个公共环，不制造重复边。执行时核每条边恰有两个反向面、Euler 数 2、显式连通环链及极点扇；这只支付组合拓扑，不能替代几何嵌入性。还拒绝非有限坐标和零面积采样三角形。

采用 binary-little-endian PLY，坐标 float64、三角形 int32，避免主动把固定小帽压到单精度。每个完整文件在写前以实际顶点／面数和头字节数计算，必须严格小于 **5,000,000 bytes**；写后再核实际大小。默认 t=0,1/4,1/2,3/4,1，全部文件保持同一顶点／面拓扑。源仓库内的输出路径被拒绝；网格、环参数和完整执行记录留在 scratch，Git 只保脚本和小来源记录。

## 等真实输入后的调用

```text
python scripts/resume_20261128/geometry/export_actual_closed_mesh.py 
  --source-run ACTUAL_ACCEPTED_RUN --geometry-bundle ACTUAL_COMPLETE_FULL_H_BUNDLE 
  --coupling-summary ACTUAL_COUPLING_SUMMARY --outdir SCRATCH_OUTPUT 
  --frame held --cylinder-half-length .0025 --times 0 1/4 1/2 3/4 1
```

原设计来源省略 `--coupling-summary`。输出成功仍只说明真实有限图的可复现网格已导出；完整 g 的连续误差、全时嵌入/reach、握持比例、全 E(3) 非全等和固定问题精化继续由各自实际证书支付。
