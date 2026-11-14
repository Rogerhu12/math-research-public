# critical 第一档对应的完整公共接缝与闭图几何账本

状态：**已审数学组件应用于此一新有限图后的完整重算；本图的独立输入绑定及完整轻账本复跑均 PASS。** 不是 README 第 5 项结论。原 uniform M12 与此图是两个不同的精确有限对象。

此图用 M12 原前缀 `db6f-root-flat17-coupled-m12f24.json`，通过已审 common-cut-v2 的精确五次修正，接到第一档 critical 尾 manifest：
`db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json`，SHA256 `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`。

新图元数据为 `db6f-root-flat17-common-cut-m12-critical-r01.json`，SHA256 `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`。它重新从此尾的所有精确增量积分端值，并使用该尾自己的两阶端迹与 R6 collar；未挪用 uniform 尾的端点值。

## 实际重算与范围

完整命令、每步时间和实际退出码保存于 `db6f-root-flat17-common-cut-m12-critical-r01-reproduction.json`。make、前缀 geometry256、metric 与 moment512 四步均真实 exit0。前缀全域连续界为：

- support 下界 0.814440512144689；
- 实际主曲率绝对值上界 5.547265858340158；
- 同一精确目标度量的相对误差上界 2.572118832449239e−8（含桥参数转换）；
- 握持见证距离下界 0.1998911434256142。

闭账本还使用此 critical 尾自身的完整一阶证书 `db6f-tail-first-flat17-m12-critical-r01.json` 及同背景物理分割转移报告 `db6f-audit-transfer-tight-m12-critical-r01.json`。后者重新核旧源、目标源、精确外域锚与物理参数恒等性，故旧背景高度与 alpha 证明可以转用；旧有限图的 metric/曲率不能由该转移获得。

此一闭图的汇总结果为 D≤3.92、全表面 support>0.7370435198982138、δ_hold/D>0.0509926386289832、完整活动实体三阶复矩实部>0.4401644538270965。固定帽与镜像组合沿用 R17 的已审构造及 R16 条件矩论证，新的矩输入正性已重算。因此其几何见证与严格非全等条件保留。

全尾实际 metric/曲率证书仍由同一 critical manifest 的完整后端运行提供；这里不借用 M8 或 uniform M12 的实际尾图数值。精确闭图 C² 接口由 common-cut-v2 定义本身支付，全部相位由同一解析旋转作用支付。

本记录不把一个更小的有限 metric 界等同于精确等距解。固定物理 g 的高模源联解、误差达到求解容差及最终未参与者全流程重跑仍继续。

## 独立复跑补记

`db6f-audit-closed-budget-m12-critical-r01.md/.json` 已核七项输入、同一实际公共接缝/尾/bridge/同背景转移及全部 Fraction 严格比较；独立实际运行 exit0，全部输出 JSON 字段相同。全尾 metric/曲率待完成的字段原样保留。
