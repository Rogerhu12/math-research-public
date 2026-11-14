# 闭网格的旋转背景相对高度采样器

状态：**数值网格辅助接口，非严格高度区间证书。** `independent_geometry` 已独立全文静态核读其槽位、方向、来源/参数绑定和 gauge；实际完整网格采样与 PL 检查另由该代理执行。

作者：`/root/tail_theory`，2026-11-09。

## 接口与固定背景

新脚本 `scripts/db6f-tail-sample-background-height.mjs`，SHA256 `106061533820a1639387b33b535408d312ade7a8337d59ed8c2b48ec80bc08a4`。输入为 tail manifest、冻结有限校准表、紧 $\alpha$ 报告以及一个小 JSON 半径数组。数组可以直接保存为 `[...]`，或 `{ "radii": [...] }`；必须包含 manifest 的精确已存 cuff 与 cut 两个 binary64 值。所有半径须位于该闭区间。

脚本先核对所有几何参数与紧 $\alpha$ 证书绑定的原检查点、相关 source 文件 hash，并逐一确认重新生成的 160 个有限校准数与冻结表二进值相同。`calibrationSteps=512` 与保护深度 160 固定。采用原数值 $\alpha=97.64534740777785$，并明确检查它在已审精确 $\alpha$ 包内；它只是数值代表，未宣称等于精确积分定义值。

每个输出行给

$$
\operatorname{heightFromRToCut}(r)\approx\int_r^{r_{cut}}w(s)\,ds.
$$

`entry.integrate` 的 0-based 槽 4、5 分别为 $\int wA$、$\int wB$，相加时使用槽 4 加 $\alpha$ 乘槽 5。profiles 从 cut 向 cuff 枚举，累计值用 Kahan 求和。区间内半径用 44 步单调 source 反解；查询点的部分高度从其 source 坐标积分至该段的外端，再加已累积的外侧高度。

## 闭图的高度 gauge

设 $z_{pre,mean}(c)$ 为 prefix 在 cut 的精确均值，$V_{z,mean}(c)$ 为有限 tail 扰动在 cut 的均值，则上尾数值网格可用

$$
z_{upper}(r,\theta)=z_{pre,mean}(c)+V_{z,mean}(c)-V_z(r,\theta)
 +\operatorname{heightFromRToCut}(r).
$$

这样整个 tail 的高度，包括非均值模式与旋转背景，都作了所需反射；cut 处的背景积分精确设为零，避免无意义的绝对高度偏移。下尾再把整个上尾 $z$ 取负。角相位、prefix 的 $\Theta$ 反解和固定帽仍由闭图网格作者按实际定义处理。

## 误差范围

报告保存局部半径反解残差与一次二分积分的一致性差，但明确二者只是数值诊断，不能当作严格求积或顶点误差条。有限函数的二进舍入、数值求积以及使用 $\alpha$ 代表值的误差均未被这个接口严格认证。现有解析闭图证书不会因为导出可视网格而改变。

单独的深尾遗漏项有已有 R15 给出的严格粗界。对于未修改的 $n\ge160$ 源，$w\le1280\,2^{-7n/4}$，且这部分物理宽度小于 $1/2$，所以

$$
0\le\int_{r_{cuff}}^{r_{160}}w\,dr\le640\,2^{-280}.
$$

这个极小的解析界只支付省略的无限深尾高度，不支付前述有限数值误差。报告将这两类信息分开保存。

## 已完成 pilot

输入 `db6f-tail-background-height-sample-radii.json` 包含 cuff、cut 和五个中间半径。输出 `db6f-tail-background-height-sample-pilot.json` 实际退出 0，约 3.05 秒，160 个有限校准数全部逐项相等。高度非负、随半径递减，cut 值严格按定义置零。

全有限段高度约 $.04928110416972474$，最大数值反解径向残差 $4.706\cdot10^{-16}$，局部拆分积分差 $1.388\cdot10^{-17}$。这些数值遵守上节的诊断范围。

```bash
node scripts/db6f-tail-sample-background-height.mjs \
  --manifest notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json \
  --calibrations notes/2026-11-09-db6f-tail-finite-source-calibrations.json \
  --alpha notes/2026-11-09-db6f-tail-tight-alpha.json \
  --radii notes/2026-11-09-db6f-tail-background-height-sample-radii.json \
  --out notes/2026-11-09-db6f-tail-background-height-sample-pilot.json \
  --source-root repro/source-root
```

复跑应使用新的输出文件名；脚本拒绝静默覆盖已有输出。此 helper 不生成新的证明图，也不代替 README 的固定度量收敛门。
