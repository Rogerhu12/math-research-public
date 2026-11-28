# 两条非椭圆中央曲线的真实原生 H65 与 Γ95

[R281](../results/R281-positive-support-central-cylinder-at-full-gap.md)给出两例闭解析曲线及完整中央柱的严格数据。对每例均以法向角 $\theta$ 为 native，$s=0$ 的初值真正取 $P=h n+h't$、$e_s=e_z$、$e_u=(-\sin\theta,\cos\theta)$、向内法向、$n_{II}=1/\rho,m_{II}=0$；初始 native 密度改为各自准确的 $\rho(\theta)$。中央半高 $13/128$。沿用物理 Cauchy 候选的逐点标架 ODE 及小负高斯曲率轮廓，$a_0=1$、ramp 长 .06、末斜率 .045、coast 长 .02。用 191 个 shape Fourier 模和 768 个实际 native 角，DOP853 从新初值积分并在 65 个物理径点取真实 ODE 节点。每节点保留整张位置、径向切向、法向加速度 Fourier。最后的实际空间曲线用全部 M95 重建新的 Γ95，原周长和规定的端口角半径各自写入新文件。

| 非椭圆中央 | 初始截断的 $n$ 最大残差 | 65 个物理节点 metric 峰 | 这些点实际曲率峰 | 节点最小 $n$ |
|---|---:|---:|---:|---:|
| $p=8,A=1.45,A-B>1.05$ | $4.65\cdot10^{-16}$ | $2.60\cdot10^{-12}$ | 8.33734848 | .22001198 |
| $p=6,r=.2$ | $3.57\cdot10^{-16}$ | $2.13\cdot10^{-12}$ | 6.92612098 | .26537449 |

两次均自然返回 0，分别 1637 次 ODE 函数调用。上表是实际 IVP 节点值。两个中央柱的连续结论见 R281；各自 ramp 的节点观测还没有给出整片区间 reach 与 Gram 证书。

```bash
python "$SCRIPTS/2ecf-strong-stadium-support-physical-H65.py" --scripts "$SCRIPTS" --prefix stadium-p8A145-H65 --offset 212017711/1479139996 --power 8 --modes 191 --nodes 65
python "$SCRIPTS/2ecf-strong-stadium-support-physical-H65.py" --scripts "$SCRIPTS" --prefix stadium-p6r20-H65 --offset 1/5 --power 6 --modes 191 --nodes 65
```

主例 ramp/coast SHA-256 分别为 `2dbf6c3ff86b3fe3e39a49d9351a37e80b8e5d18c14ed71813853ebccdd4e167`、`8672f468f460293976d2474c1bd52bd092d8f5c0f006709335c1a18fc055f244`。对照例为 `962457f6ea5930f0339a00001664f8cadd812d614115d0ab31ec1573d5cb0305`、`cf22720fa7e0bd5aff0550781a6f09bfc960e37571c56738945198363f027090`。可重算数组不入库。
