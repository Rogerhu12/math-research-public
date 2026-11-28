# 固定设计 3 目标的真实径向材料重参数化

在[完整 64×80 保 W 的显式物理位置](2026-11-28-2ecf-strong-accurate-hermite-fourier-position-with-literal-W.md)上仍取原物理 $s$、原 $b,S$ 和原冻结目标 $a_*(s)$。新映射为
$$
\widehat X(s,u)=X(s+h(s,u),u),\qquad
h(s,u)=\sum_{j,k}d_{jk}B_j(s)\cos(2ku),\quad 0\le k\le4 .
$$
$B_j$ 是在 $[b,S]$ 真物理 knot 上的 clamped 五次 B-spline，省去两侧各三列，其他片令 $h=0$。在完整源上用训练网各点实际 $E_s,F_s,G_s$ 和相对算子范数的切平面选择 $d_{jk}$。随后用新位置函数 $X(s+h(s,u),u)$，对两个完整 G10 组和独立移位 G11 的所有六个 Cartesian jets 从头求值。目标仍按材料 $s$ 求，未把它随 $s+h$ 拉回。十二轮线性切平面迭代选择一个时钟，最终观察来自完整非线性位置。它是单一材料位置更新，未计入原 6615 LM 链，也未变更度量。

| 有限组 | 父场最大误差 | 新场最大误差 | 新场最大自身曲率 | 新场最小面积比 |
|---|---:|---:|---:|---:|
| G10，958×128 | .140241818 | .113959391 | 28.871846 | .920444847 |
| G10，958×192 | .140241818 | .119206113 | 28.871846 | .919241032 |
| G11，668×256 | .143431819 | .120512744 | 28.824820 | .916493963 |

新场的连续图像与父场相同。对每一个存储二进系数按有理数读取。把首尾三个零控制补回，各角谐波的一阶径向导数控制为 $5(d_{j+1,k}-d_{jk})/(t_{j+6}-t_{j+1})$。对每个控制行取所有角谐波绝对值之和，最后取最大得到
$$
|h_s|\le\frac{9578513281229562065}{70835497243044610048}
<.135222 .
$$
故 $1+h_s>.864778$，每个固定 $u$ 有真正的严格保向重参数化，两端二阶 jets 都是恒等。$(s,u)\mapsto(s+h,u)$ 是整个闭环带到自身的 $C^2$ 微分同胚。父场的任何连续嵌入、图像曲率或 reach 证书将直接转移；本条数值最大曲率的细小差异来自不同材料采点，重参数化未改善连续图像曲率。后继已接该新位置和原冻结目标，释放全 6615 XYZ 的真正物理位移，以同时修改径向形状和曲率。

`S`、`W`、`OUT` 的设置沿用前引物理场记录，`F` 为该记录所得 `strong-physical-hf64m80-W.json.field.npz` 的路径。

```bash
set -eu
mkdir -p "$OUT"
python "$S/2ecf-strong-hf-material-radial-clock.py" \
  --scripts "$S" --field "$F" --ramp "$W/gap105-prefix-ramp-master.npz" \
  --coast "$W/gap105-prefix-coast-master.npz" --prepared "$W/polar-physical-H65-prepared.json" \
  --independent "$W/polar-physical-H65-independent.json" \
  --output "$OUT/strong-hf-physical-radial-clock01.json"
python "$S/2ecf-strong-hf-radial-clock-orientation.py" \
  --state "$OUT/strong-hf-physical-radial-clock01.json" \
  --output "$OUT/strong-hf-radial-clock-orientation.json"
```

两个实际进程均自然退出 0。优化结果的原场、物理端口、冻结目标 SHA 与 64×80 场相同；给定时钟状态后，`Field(args,u)`、`Clock(b,S)` 与 `compose(field,clock,s,u,coefficients)` 提供原切向顺序下的全部六 jets。

| 对象 | 本次 SHA-256 |
|---|---|
| 2ecf-strong-hf-material-radial-clock.py | `e751b853e559541528297d62adc28c5fc2139ab4173484b8d429a70177c1d44a` |
| 2ecf-strong-hf-radial-clock-orientation.py | `b4958a2516f1a1f8b3b571c44df518d7f249a472c1d581f69e0c298e5163069b` |
| strong-hf-physical-radial-clock01.json | `3f3ca37fe9ee55a9e20f13cd744c35bb2b6b1f169026bd1ad7897caffe3d25a0` |
| strong-hf-radial-clock-orientation.json | `784ca7467a4262be5d58a988a22f72dfc0b2f639cbb9eef698b7c802431908dd` |
