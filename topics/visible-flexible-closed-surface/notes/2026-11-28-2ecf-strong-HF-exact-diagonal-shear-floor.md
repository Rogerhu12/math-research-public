# R274 在两张实际 HF 曲面上的严格对角度量下界

**连续场的严格必要界。** 固定[整圈共同度量问题](../results/R274-all-angle-invariant-metric-centre-and-diagonal-reduction.md)的材料角识别。对[真实双钟母场](2026-11-28-2ecf-strong-hf-two-material-clocks-on-new-metric.md)及[同 $g$ 的 75 次真实位置场](2026-11-28-2ecf-strong-hf-true-XYZ-joint-spectral-solve.md)，各给一个准确有理材料点。它们不是按最近的储存网格坐标定义。若 $E=|X_x|^2,F=X_x\cdot X_u,G=|X_u|^2$，R274 说明一个点在任意正对角基准下的最优相对误差为 $|F|/\sqrt{EG}$。正径向材料钟的导数与任何共用的角半径都会从该比值约去。故下表约束能自由选正材料总长度、角半径、光滑或非光滑径向系数的任意对角目标。

| 实际位置场 | $x$ | $u$（弧度） | 内 HF 第几片（零起） | 严格误差下界 |
|---|---:|---:|---:|---:|
| 已接受的二维材料钟 | $1/4$ | $3031/1000$ | 5 | $9811/100000=.09811$ |
| 其上 75 次真实 XYZ | $281/1000$ | $6197/1000$ | 7 | $8359/100000=.08359$ |

在每个点先以两个真正的完整 B 样条／Fourier 时钟给 $y=x+p,v=u+q$，随后以母径钟给 $\xi=y+h(y,v)$，全取一次偏导。内片判定由有向区间的**严格**不等式确定。两点均远离 Γ95 和 R205 端片，内部 HF64M80 直接采用实际保存的全部复系数、原五次 Hermite 和完整 W；第二张场另外在真正外坐标 $(x,u)$ 加其 6615 个系数定义的完整 Cartesian 修正。全部连续导数组合后才形成 $E,F,G$。程序不使用数值法向或差分，不对采样表插值。

计算采用整数端点、统一网格单位 $2^{-160}$ 的向外区间。保存的 binary64 源系数还原为准确有理数，区间加减乘除均向外。正弦余弦先将角度折半至 $|v|\le1/8$；余弦取 Taylor 至 32 次，正弦至 33 次，Lagrange 余项分别不超过 $(1/8)^{33}/33!$、$(1/8)^{34}/34!$，均小于一个工作网格单位。向外扩张后用倍角和三角递推包含所有实际高频。径向样条在准确单一内片按 Cox–de Boor 与导数公式求取，HF 端点 Hermite 缩放带实际片长。最后以整数叉乘严格比对 $\min|F|^2/(\max E\max G)$ 与所列有理数的平方。两个下界的数值展示分别约 .098110133539、.083593630953。逐点严格界与[逐环浮点理想值](2026-11-28-2ecf-strong-all-angle-HF-free-diagonal-floors.md)的证据形式各自保留。改变实际位置场或允许额外材料角依赖变换仍可绕过所列必要界。

在前述真实场的生成环境运行（不需要重新计算 G10 或 G11）：

```bash
witness=(--field "$HF/strong-physical-hf64m80-W.json.field.npz" --angular-clock "$HF/strong-hf-physical-radial-clock01.json" --warp clock-hf-two-material-spectral.json --diagonal clock-hf-diagonal-d006.json)
python "$SCRIPTS/2ecf-strong-hf-exact-inner-shear-witness.py" "${witness[@]}" --x 1/4 --u 3031/1000 --floor 9811/100000 --output clock-hf-r274-base-witness-tight.json
python "$SCRIPTS/2ecf-strong-hf-exact-inner-shear-witness.py" "${witness[@]}" --position clock-hf-full-joint-spectrum-03.json --x 281/1000 --u 6197/1000 --floor 8359/100000 --output clock-hf-r274-75-witness-tight.json
```

两份准确输出的 SHA-256 为 `4db3ef49edce0cc05ac58ee74e8c3d505c9b61db610f2e919da2e99beffed69c`、`18b7781dbcd631e4f0c2577bdc020e9363f1625c5cde5e440a3ee1c8a1d1409e`。内含有理 $E,F,G$ 两端、完整源身份和实际严格平方下界。
