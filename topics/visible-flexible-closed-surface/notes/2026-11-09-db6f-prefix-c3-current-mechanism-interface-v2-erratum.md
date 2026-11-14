# 有限核实际机制接口 v2：两项精确修订

/root 与未参与实现的 tail_theory 在全文审查中独立指出：v1 第 8.1 节定义 $R_K=\max_K|x|$，仅证明 $R_K\le57/40$。因此第 8.2 节以实际 $R_K$ 定义的 $Q_{CD}$ 只能写成 $Q_{CD}\le4.419076<26/5$。v2 将原等号改成这个不等号；后续凸包直径及 held 条件结论完全不变。

原 Fraction 脚本本来就把 `radius` 定义为已证明的上界 $(3-r)/2$，输出字段也是 `centered_radius_upper` 和 `pair_distance_squared_upper`，所以它计算的是有效上界。其源码及数值输出维持原 SHA，没有重跑或更改数字。

依 tail_theory 的范围提示，v2 另将第 6 节 $w=w_r=0$ 明确限定为**当前平帽接口**：一般固定轴对称非平帽不要求这两个值为零，但仍需要完整 Cartesian 二 jet 匹配。这不改变原稿所讨论的实际平帽构造。

唯一其它变化是来源 ledger 文件名转到 v2。v1 原稿、原 ledger、标量脚本、账本和真实退出记录全部保留。高阶 Taylor 段仍明确需要额外光滑分支；没有将四阶展开称为任意 C² 分支结论。没有新增参数、候选、求解或测试。

## 冻结身份

- v1 原稿：`2026-11-09-db6f-prefix-c3-current-mechanism-interface.md`，SHA256 `eec8eab0e2a4979436c0a21f27bccfdc8abdc1281587f8cdda6b1ae6281eb8da`。
- v2 正文：`2026-11-09-db6f-prefix-c3-current-mechanism-interface-v2.md`，SHA256 `7497d615d4fb46eeed1b6cc710851d9bca4aa46a040567f1879cf77acd30a356`。
- v2 来源 ledger：`2026-11-09-db6f-prefix-c3-current-mechanism-interface-v2-sources.json`，SHA256 `d7c6f11a0150e292c4da692e9935ec12d2647ba4725d7175348b8af9fe3c849b`。
- 未改标量源码：`db6f-prefix-c3-mechanism-conditional-budget.py`，SHA256 `b98272c2d92406dd3611ae680ebd754b3558268281c47500aea1e6a70b23f527`。
- 未改标量账本：`2026-11-09-db6f-prefix-c3-mechanism-conditional-budget.json`，SHA256 `47fda2e36bf60860f94c0f151542cbff465a3ebb28845db617bf80d45f5ef1a1`。

## 完整文本差分

```diff
--- 2026-11-09-db6f-prefix-c3-current-mechanism-interface.md
+++ 2026-11-09-db6f-prefix-c3-current-mechanism-interface-v2.md
@@ -223,7 +223,7 @@
 $$
 材料角平移与空间旋转共同给原活动 metric；中央像包含 $R_\alpha\Gamma$。这不要求中央曲线本身轴对称。
 
-但是要让另加的帽保持逐点固定，cuff 处必须是轴对称圆领的**全部 Cartesian 两 jet**，而非只有圆形位置。现有尾 collar 把扰动及其前两阶径向导数精确降为零，背景也需 $w=w_r=0$；这些性质才使 (22) 与固定帽 C² 拼接，并使相位在 C² 拓扑连续。未来新数据仍须支付全圆领与完整闭图的 metric、嵌入及曲率。
+但是要让另加的帽保持逐点固定，cuff 处必须是轴对称圆领的**全部 Cartesian 两 jet**，而非只有圆形位置。对当前平帽接口，现有尾 collar 把扰动及其前两阶径向导数精确降为零，背景还需 $w=w_r=0$；一般固定轴对称非平帽不必满足这两个零条件。这些性质才使 (22) 与固定帽 C² 拼接，并使相位在 C² 拓扑连续。未来新数据仍须支付全圆领与完整闭图的 metric、嵌入及曲率。
 
 本例中央的实际二 jet 局部主曲率为 $1/\rho$ 与 0，支撑 $F\cdot n=h\ge(1+r)/2$；这只给中央的好余量。全闭面仍要按 R10 的完整假设控制全域支撑及实际主曲率，例如当 $D<2.3$ 时 $\sigma_0\ge.069$、$K_0\le1/.069$ 足以给该工具所需的全 reach 下界。平面或带边柱核的 reach 不能代替这个全域结论。
 
@@ -305,7 +305,7 @@
 $$
 同一端盘内的点对也被 $Q_{DD}$ 覆盖。所有常数以有理数计算，严格得到
 $$
-Q_{CC}<\frac{26}{5},\qquad Q_{CD}=4.419076<\frac{26}{5},
+Q_{CC}<\frac{26}{5},\qquad Q_{CD}\le4.419076<\frac{26}{5},
 \qquad \frac{26}{5}<\left(\frac{23}{10}\right)^2.
 \tag{30}
 $$
@@ -348,7 +348,7 @@
   --out notes/2026-11-09-db6f-prefix-c3-mechanism-conditional-budget-NEW.json
 ```
 
-固定输入身份、本文所读源码及已有证明见同 stem 的 `sources.json`；完整路径是 `notes/2026-11-09-db6f-prefix-c3-current-mechanism-interface-sources.json`。旧图的高度、正支撑及 metric 数值只用于识别旧对象，不作为新候选证书。
+固定输入身份、本文所读源码及已有证明见同 stem 的 `sources.json`；完整路径是 `notes/2026-11-09-db6f-prefix-c3-current-mechanism-interface-v2-sources.json`。旧图的高度、正支撑及 metric 数值只用于识别旧对象，不作为新候选证书。
 
 实际尚未支付的条件具有明确接口：中央多模数据的合法新入口与足够精确投影；(6) 的全段正性及 (17) 的真实全局边值解；(19)–(21) 的完整端迹与逐次趋零的修正；cuff 全二 jet 与固定帽；真实闭图位于 (25) 的连续位置界；全时浸入、嵌入、reach、固定握持区及非全等；以及原 README 的同 $g$ 加密与独立完整重跑。这个清单不是新任务门槛，只定位现有完成标准中不能由平面核心证明替代的部分。
 
```
