# 有限尾与 collar 的平面胚判据及执行接口

2026-11-14，geometry，AI 辅助。**条件代数论证已证明；实际数据检查待本公开仓库 Actions 返回。**

## 1. 不需要尾的准确半转对称

考虑一个径向片上的有限场
$$F(r,\theta)=(r\cos\theta,r\sin\theta,H(r))+P(r,\theta),$$
其中 $H$ 是任意函数；$P$ 的三个分量是关于 $r$ 次数至多五的多项式与有限三角多项式的组合。允许 $P$ 没有准确半转对称，这覆盖浮点 FFT 后的完整有限 Fourier 场。

取四个角 $\theta_j=j\pi/2$，令
$$D(r)=\det\big(F(r,\theta_1)-F(r,\theta_0),
F(r,\theta_2)-F(r,\theta_0),F(r,\theta_3)-F(r,\theta_0)\big).$$
均值 $H(r)$ 和 $P$ 的全部零频分量准确抵销。其余坐标都是径向至多五次多项式，所以 $D$ 是至多十五次多项式。四个角的所有三角值都准确为 $0,\pm1$。

**命题。** 若 $D$ 不恒为零，该径向片没有非空平面开片。

**证明。** 假定一个参数矩形开集映入固定平面。对每个处于该径向小区间的 $r$，平面方程作为角变量的有限三角多项式在一个角开区间为零，所以在整个圆周为零。四点共面使 $D(r)=0$ 对该径向小区间恒成立。多项式因此恒零，矛盾。这里没有假设 $H$ 解析，也没有调用精确等距。若非零见证位于径向片端点，同样可由多项式在闭区间上的连续延拓使用。证毕。

给出一个准确非零的有理见证即可证明 $D$ 不恒零。反之，十六个互异的有理点上都为零就能决定它恒零；但这只表示这个**特定四角判据**失败，不能推出曲面有平面开片。

## 2. 覆盖实际有限接缝修正

`RefinedTail.span` 给每个实际原径向片上的五次 Hermite 系数。固定宽外修正也是五次多项式。在它的起点、以及 clip 到1的终点切开径向片后，两者之和在每个开片仍是至多五次多项式。有限内 collar 是另一个同型五次多项式；它在 cuff 处的零二阶 jet 不妨碍在片内部取非零见证。

检查器按原适配器的已保存/已生成浮点系数作**准确有理解释**，将所有 Fourier 频率保留。它准确求和四个 cardinal 角，给每个原片及被外 patch 切出的子片求有理 determinant。`H(r)` 和零频平移只在这项判据中消去，不改变实际闭曲面的均值或度量。

检查器源码：`computations/geometry_20261114_tail_planar_germ.py`。调用形式：

```bash
python computations/geometry_20261114_tail_planar_germ.py \
  --checkpoint ACCEPTED_PREFIX.json.gz --source-topic PINNED_SOURCE_TOPIC \
  --port ORIGINAL_PORT.json --config REFINED_CONFIG.json \
  --complete RADIAL_READOUT_COMPLETE.json --plan CLOSED_PLAN.json \
  --out OUTPUT/tail-planar-germ.json
```

所有输入先与 plan 的 hash 绑定。逐片有理见证位置和 determinant 的符号、整数位数、分子分母 hash 写入压缩文件；完整整数可以由同一输入与脚本重生。程序不使用一个浮点阈值把极小数改为零，也不把它当作一个抗扰动余量。

## 3. 结论边界

本项在实际执行通过后，只证明该**有限多项式场**逐片无平面开片。FFT 的极小高频噪声也可能使这个有限场的 determinant 非零；因此结果不能证明精确等距极限仍无平面开片，不能给 $\delta_{\rm E}$ 的稳定下界，也不能免除新的候选重新检查。

与 R238 前缀判据组合仍需要全局 $C^2$ 装配和闭嵌入，把活动片识别为环带，以及一个真实整面像变动的见证。检查器始终输出 `actual_delta_E_certified=false` 和 `task_completed=false`。全空间 reach 的实际证明也不由此产生。
