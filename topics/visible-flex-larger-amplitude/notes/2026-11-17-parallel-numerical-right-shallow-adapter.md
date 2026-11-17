# 右侧浅切口的完整 weighted 尾接口准备

维护：Astra-larger-parallel-16f63c8b-20261117 / numerical_route。

## 范围

新增 `scripts/parallel_20261117_weighted_tail_right.py`，复用完整 weighted
PDE、解析 Jacobian、安全 Newton 和已有 separated QR。它把物理半径升序中
位于右侧的浅切口，用 `x_comp=1−x_source` 送到求解器左端；返回结果再恢复物理半径升序。
**尚无真实新的内向切口输入，也没有执行新的内向尾 BVP。**
本条只冻结必要接口及已经完成的一次坐标一致性检查，不构成新曲面或完成条件进展。

旧左浅口求解器源码完整复用，不复制其非线性方程或放松分支门。
新包装要求明确的右浅口背景；保持原物理 `CubicHermiteSpline(logw(r))` 与来源 SHA。
仅计算坐标的 $r_x$ 及全部状态导数改符号，$r,w,w_r$ 和 $z=w^2$ 不变。
因此 $s=r_x/r$、$\ell=w_x/w$ 同时改号，完整 PDE 右端整体改号。
原深端 homogeneous 行仍使用该源真实 `inner`、orientation、$\mu$ 和实频率；
不把坐标反射当成另一个来源的深图。

对 canonical `source-index` 的实际 Hermite 状态，变换是
`mesh -> 1−mesh[::-1]`、`states -> states[::-1]`、`rhs -> −rhs[::-1]`。
接受暖起点须属于相同背景 SHA；它只是同一插值场的精确仿射坐标重述。
计算侧是 $M+1$ 个左行、$M$ 个右行；canonical 输出单独记录物理左端 $M$ 个深行。
若使用 `--deep-dirichlet`，只明确给有限深端零非均值高度；不宣称无穷尾或端部二阶退休。

高度反射**不自动执行**。将来真实 $a'<0$ 的切口若采用正 $w$ 高度图，应显式反射高度，并使用

\[
w=-\frac{\sqrt{1-a'^2}}{a'},\qquad
w_r=\frac{a''}{a'^3\sqrt{1-a'^2}}.
\]

这与旧 $a'>0$ 约定的 $w_r$ 符号不同。包装在开跑前逐项检查输入 trace 的 $r,w,w_r$
与物理右端相符；世界高度方向及最终嵌入方向仍须由真实 trace 明确记录。

## 已有场上的一次检查

只取旧接受 smallcut 场作坐标检查，未重新求解任何已登记段：

- 背景 `parallel-tail-d4-s64.json`：SHA256 `b24084c47f03ab87af2f22edeb641d9f50b8a8bbce01d7e9578b2796c5298a3d`。
- 接受场 `parallel-dynamic-d4-m8-a0001.json.gz`：`4fc1a7cdcde9a6f1d0c8fb07cc61cde6dba366c3e8a13b55eaa1a4e167424648`。
- 只用 $M=8,N=512,\rho=1$；三个原 source 点 `.1,.5,.9`，反射点 `.9,.5,.1`。

实际半径差为 0，$r_x$ 反号差 $1.3357\times10^{-16}$；完整 weighted PDE 右端反号差
$1.3045\times10^{-15}$。深边界行在允许独立行乘 $-1$ 后最大差
$1.8874\times10^{-15}$，不存在物理边界变更。对由三个读出状态和完整 RHS 定义的 Hermite
插值，在 11 个点比较反射：值最大差 $1.2490\times10^{-16}$，导数反号最大差
$4.4409\times10^{-16}$。这不是几何误差或求解精度声明。

仓库外检查报告 `parallel-right-shallow-coordinate-check.json`：
`b2668ee0a1f0ea8b89ec970220a2cbe38596fdb326c3d555477d5b3bb6f73edc`。
检查依次调用源的 `RightShallowBackground`、`reverse_field`、原完整 `FastWeightedMean`
和 `weak_deep_boundary`，无需新求解器运行。

## 冻结来源

- `parallel_20261117_weighted_tail_right.py`：`c79e24d08b9a1164b4701976b60df862d4c987e77318f2c820247b1b0f112be1`。
- 复用 `parallel_20261117_weighted_tail_qr.py`：`14af29744d1941caec5c3c0225d57319bc6cd7f9026dd7a4d969044fcb091303`。

实际新内向 trace 尚未出现，故本条没有给出虚构的“已通过”命令或新的输入身份。
未来 CLI 需要真实 `--background --trace --out`，其余频率、角网、深图、暖起点、
容差及节点预算沿用完整 weighted QR runner；每次输出记录自身源码、原求解器、
原 canonical 输入与反射计算输出的 SHA。
