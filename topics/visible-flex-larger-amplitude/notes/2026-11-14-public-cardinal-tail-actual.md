# 公开 Actions：四角共享 C² 规范形的全部尾部非平面片检查

完整命题、全片证明、精确 Hermite 定义和实际证明实例已整理为
[R243](../results/R243-exact-C2-cardinal-tail-no-planar-germ.md)。本条保存执行回执。

## 实际回执与结论范围

公开仓库 `Rogerhu12/math-research-public` 的 run `43584222071`，源码提交
`a47c0f96b7a5843deb8d8ffea181beab6eb6696e`，`cardinal` lane 已实际成功，
包括 publisher。产物 `visible-mainline-cardinal-43584222071-1`，artifact
`14109383592` 中的 `R238-exact-C2-normal-form.json` 记录实际用时
`9.842972846999999 s`。这次执行消费已有节点字节小包，没有重跑 RK48
非线性解或完整径向读出。

**已付：**从该包定义的精确共享节点 Hermite 四角迹，全部尾部和有限 collar
径向多项式小段都不存在平面开片；径向共享节点 C² 和四角端点 2-jet 配准按
有理运算成立。**未付：**该规范形与旧浮点 renderer 的同一性或误差界、整个
场与 prefix 的精确 C² 接缝、严格等距非线性极限，以及当前全闭面的
`delta_E > 0`。本条不是本课题完成结论。

## 输入与实际检查

| 项目 | 实际结果 |
| --- | --- |
| 已逐文件验证的原径向节点 | `9245` |
| 原 tail 径向区间 | `9244` |
| 加入 patch 分界与 collar 后检查的多项式小段 | `9246` |
| 小段四角非共面多项式均非零 | `true` |
| 未覆盖小段 | `[]` |
| 共享节点 0/1/2 jets 原样用于两侧 Hermite | `true` |
| 径向四角迹为精确 C² | `true` |
| 外端四角 jets 等于提供的 prefix target | `true` |
| cuff 四角差分 jets 到二阶等于平圆 | `true` |

检查器源码 SHA256：
`1d33b952d539ae9fbbff6807f8b61c73fc65c1b85bb9514fe3d29fc0f507af8e`。
小包 manifest SHA256：
`29c7799e77147a763903d66dfbb9848f336058247fb0646207b7f8378e5c9660`。
原 complete SHA256：
`2f27e53cc6880cade99ebd52eb137d1d3fd6e901c4faa2e04c2571f3ad73f118`。
原 plan SHA256：
`f8f508ab1c6de0463663b3124494a3350435e9e844851a09e585e90e40350c2e`。
本次 `R238-exact-C2-normal-form-witnesses.json.gz` SHA256：
`9029fc8dd1961e1b02a781af05a86d2d8c215adf3c013792f97ef1d8ca840433`；
解压后 JSON SHA256：
`47f4c595d7c394b92cd9e1b1d1ea84a015efc7e2cce073af704fd90b9f24a64f`。

原数据出处和小包定义见
`2026-11-14-public-cardinal-tail-normal-form.md`。检查器逐段把四角位置相对
第一个角的位置差组成三重积；精确 Hermite 给出有理系数多项式，并保存
至少一个非零有理取值。因而该多项式不可能在任何径向开子区间恒为零。
任何关于周期角解析、且具有这些四角迹的有限场，若有一个平面开片，角向
解析延拓会令同一径向开区间的四个角全部落在同一平面，产生矛盾。

## 共享规范形与旧表示必须区分

此处先把原始节点的二进制数当作精确有理数，再从两端共享的 0/1/2 jets
重建 Hermite。原 renderer 先做浮点 FFT，再计算并舍入 Hermite 系数；
即使两者来自同一组节点，它们也不是已证明完全相同的函数。因此回执中
`literal_previous_renderer_binary_field_identity` 为 `false`，且没有给出
两种表示之差的上界。

四角差分精确消去同一个角无关高度均值，没有把物理曲面的均值改为零。
外端 target 来自旧 A checkpoint
`917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf`
的直接 Fourier 径向 jets；本次只证明规范形外端等于这些**提供的**二进制
target，不补付 prefix 径向转换的舍入误差及共同高度均值的精确 C² 接缝。
回执 `exact_prefix_to_target_conversion_rounding_paid` 和
`exact_prefix_seam_and_common_mean_C2_paid` 均为 `false`。

此外，非零有理见证可以非常小。本结果没有提供在加密或严格非线性极限
下仍保持非零的统一下界。`exact_nonlinear_limit_nonplanarity_certified`、
`actual_delta_E_certified`、`task_completed` 全为 `false`。R238 的几何刚性
条件定理仍须与实际整面嵌入、图像变化及相同几何表示上的无平面开片输入
一起使用；R242 的严格等距且角解析结构引理则是另一条条件路线。
