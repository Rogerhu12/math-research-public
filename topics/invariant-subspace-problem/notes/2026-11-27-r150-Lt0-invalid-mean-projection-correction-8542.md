# R150 Lt0：本轮未登记均值试探的分量纠错记录

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127 / r150_open_geometry。

本轮 scratch 新输入 `universal_means.py` 与 `Lt_scaled_original_means.py` 起初将均值 E_j 中的 `−2(d·d)_j` 一律写成 `−2 d_j²`。这只在简约点分量成立；原双点代数乘法是

```
vm(v,w) = (v0*w0, v0*w1+v1*w0, vB*wB, vC*wC).
```

因此 j=1 的正确项为 `−4 d0 d1`，不能写成 `−2 d1²`。发现后已经修正为 `−2*vm(d,d)[j]`，并停止使用此前全部衍生数据。

**全部无效范围：** 旧 scratch 的 `universal-means.json`、`Lt-ek-means.json`、`universal-Lt-means.json`、原齐次均值及其 theta 约化，三个 t 二次式系数行列式，`Lt-det-graph-reduced.json` 所谓 lambda 374 次 / z 11 次投影，旧 E1/EBodd 结果式、所谓 lambda 580 次投影，以及它们的未完成 lambda 结果式和 primitive PRS。旧 PRS 到 z 次数 5 时峰值约 913 MiB，已主动终止，exit 130。它们没有被登记成结果，不能作为后会话数学输入；旧 E1 t² 的因式分解也不能作为支付单位。没有保存其大系数数据到仓库。

此前已登记的 h=k 两谱、theta 伪余式双零面、M 的 z 首项零面三份源始终使用 `dd=vm(d,d)` / `ddv=vm(d,d)`，不受此试探错误影响。

随后单独完成的 [u=2 全原返回](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-zero-base-weight-exclusion.md) 从原 Lt0 恒等式、原 G/K/M 和 `z²−D=0` 出发；其自含源不读取上述 scratch 输入。在末 36 维代数中，源按正确 `ddv=vm(d,d)` 重新生成全部九式，检查原 U 三矩、P(V)、N(V)、P1，原 Res_t(E1,EB) 真逆实际回乘为 1。其源 SHA256 为 `9342f3a73f1af187c2fa0d5c297f4d26719f02605553e60964bff6aa0fd420a7`，九式输入 SHA256 为 `0ff265959dbfdb0653df0bbeb569307292ac4d358077d7dd3c3848a364707c9d`。

修正后的新一般图输入在重新逐项核对原乘法前仍只属 scratch 试探；本记录不把新的待算投影声明为数学结论。
