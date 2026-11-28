# 真实三步 XYZ 形状上的两次双材料坐标更新

采用 [HF64 材料径钟](2026-11-28-2ecf-strong-hf-true-radial-material-clock.md)后的实际 6615 个新 XYZ 系数，固定取 `polar-HF64-clocked-xyz-step03-step01-state.json` 的全部三步形状。其独立 G11 最大主曲率已由约 28.8 降至 17.36385，固定设计 3 目标的峰度量误差为 .15262399。现在仍用同一原 $g$，在该准确形状上连续实施两个新的完整材料变换
$$
(s,u)\mapsto (s+h(s,u),u+k(s,u)).
$$
$h$ 为物理五次 clamped splines 乘 $\cos(2mu)$，$0\le m\le5$；$k$ 为相同径向空间乘 $\sin(2mu)$，$1\le m\le5$。省去首尾两侧各三行，故所有端迹至二阶是恒等。目标仍在原 $(s,u)$ 位置求值。每一步都在实际可变径向和角向位置重新消费中间 Hermite、原物理 $W$、原径钟以及此后新增的三步 XYZ；用完整二变量链式法则生成全部六个物理 jets。G10 的两组、移位独立 G11 均为整张原物理定义的全半面观察。

| 真实场 | G10 训练峰 | G10 观察峰 | G11 移位峰 | G11 主曲率峰 |
|---|---:|---:|---:|---:|
| 真实 XYZ own3 | .152324099 | .152324099 | .152623992 | 17.363851 |
| 第一次双钟 | .129438330 | .131806304 | .129667137 | 17.356263 |
| 第二次双钟 | .112409106 | .117170022 | .116619048 | 17.364583 |

第一步基于实际 Gram 在双坐标上的六项一阶变化与谱范数活动方向，完全非线性重算的步长 1、3/4、1/2 中，1/2 在训练上最佳。第二步在第一步的完整图上重新线性化，加入系数绝对值惩罚和完整谱截平面的实际包络，四个真实候选步长中 1 最佳。第一份原始 JSON 的遗留字段 `trainingParentPeak` 重复本步输出；上表左上两格来自[真实父态 G10](2026-11-28-2ecf-clocked-hf64-actual-new-6615-positions-four-steps.md)及独立全图重求，父态 G11 也用该原态自己的移位观察。第一步、第二步最终状态的真系数 hex 及所有实际三组观察都保留。

把每一个 dyadic 样条系数按有理数取得。对 $h,k$ 各自，在每个径向导数控制的全部谐波绝对值和上取最大，给 $|h_s|,|k_s|$；原控制以角频率的绝对值加权，给 $|h_u|,|k_u|$。每一步实际计算这四个有理数。第一步两行和的最大值小于 $.209$，第二步小于 $.076$。故 lift 上的增量在无穷范数下为严格压缩，恒等加该增量为单射，Jacobian 全处可逆。端外以零延伸后，对每个目标点用压缩映射得到唯一原像；两条边界固定、周期等变，故原闭环带上的映射是 $C^2$ 自微分同胚。真实图像和全域自身曲率的上确界不随这两次材料变换改变，表中曲率差异来自材料取样移动。此处采用三步新 XYZ 形状，与 R272 用于严格整核几何的较早物理形状有别。

令 `S` 为公开课题 scripts 目录，`W` 为 strong 分支原件目录，`F`、`CLOCK` 为原 HF64 物理场和第一次径钟状态文件路径，`OUT` 为新目录。原 G10/G11 源生成见[原径钟记录](2026-11-28-2ecf-strong-hf-true-radial-material-clock.md)。

```bash
set -eu
mkdir -p "$OUT"
p=(--scripts "$S" --field "$F" --clock "$CLOCK" --ramp "$W/gap105-prefix-ramp-master.npz"
   --coast "$W/gap105-prefix-coast-master.npz" --prepared "$W/polar-physical-H65-prepared.json"
   --independent "$W/polar-physical-H65-independent.json"
   --state "$W/polar-HF64-clocked-xyz-step03-step01-state.json")
python "$S/2ecf-strong-hf-physical-xyz3-two-chart-clock.py" "${p[@]}" --output "$OUT/step1.json"
python "$S/2ecf-strong-hf-physical-xyz3-composed-two-charts.py" "${p[@]}" \
  --parent-chart "$OUT/step1.json" --output "$OUT/step2.json"
```

两步回执均由实际进程自然退出 0。第二步首次构造稀疏矩阵时被同名的局部数组遮蔽，未开始新步的拟合；修正后在同一父态完成实际运行。真实源指纹如下。

| 文件 | SHA-256 |
|---|---|
| `2ecf-strong-hf-physical-xyz3-two-chart-clock.py` | `6146733dc7cfcdd0164cefd8454510d25e8af3d273defe719ffabb50a3503fa5` |
| `2ecf-strong-hf-physical-xyz3-composed-two-charts.py` | `1b5df192648188aedd2879eaadb99b0d7c7b8ee02653baa6ed58293666582836` |
| `strong-hf-physical-xyz3-two-clock01.json` | `957834f9c3f593122ab24b02fa63ac1bd851f8c4766a4bc0174121741ebf6d05` |
| `strong-hf-physical-xyz3-two-clock02.json` | `566cbe36ca0bc7c5f203fcf1f7716850c8b4643791b3423ca7da066b8fd1a93f` |
