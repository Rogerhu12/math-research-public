# 偶高度核心：独立冻结验证器与材料入口

日期：2026-11-14。实现状态：脚本已准备并经作者静态核查；当前执行环境失联，尚未执行 Python 开发检查。必须先在本公开仓库 Actions 运行 `--check-only`。本文不记录任何未经运行的 passed 数值，也不把开发完成当成实际几何达标。

## 1. 文件职责和冻结身份

- `scripts/space_star_cosine_design.py`：另一代理负责的几何设计器，全部 cos 高度系数及可选 offset 自由。
- `scripts/space_star_cosine_verify.py`：本文的独立连续验证器，只消费选中的准确物理身份；不优化、不重新选择 trial，不改变高度 offset。
- `scripts/cosine_rectifying_core.py`：同一个准确模型的数值材料角与完整二 jet 接口；它的 Gauss 求积和反解结果不能当成区间证书。

设计输出必须是 `space-star-cosine-design-v1`，并有顶层
`frozen_physical_identity`：

```json
{
  "height_basis": "cosine",
  "a": "13/20",
  "b": "3/25",
  "half_width": "1/50",
  "height_coefficients": [
    {"numerator": "...", "denominator": "..."}
  ],
  "height_offset": {"numerator": "...", "denominator": "..."}
}
```

数组第 \(j\) 项的频率固定为 \(3j\)，没有隐含相位变更。优化器的实际 binary64 高度和 offset 由 `Fraction.from_float` 精确冻结；验证器拒绝身份中未注明语义的 float。\(a,b,w\) 按 CLI 指定的准确有理/十进制模型保存。

参数哈希统一使用
`sha256(json.dumps(identity,sort_keys=True,separators=(',',':')).encode())`。
输入的物理哈希不匹配即报错；连续 certificate 本身也携带相同物理哈希，材料入口拒绝把另一模型的 certificate 当作当前模型的全宽保证。原始设计 JSON 的字节 SHA256 也记入输出。独立验证只消费明确选中的顶层 identity，不会把失败 trial、raw final 或新采样自动换成另一个候选。

另须保留 `planar_certificate_source.sha256`，锁住原平面几何证书。固定公开路径是：

`topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json`

对应 SHA256：
`ba03fc43af2c86ee61b7ca1a9fa541f9287222ef8bd4dcb155c35332c9def405`。

## 2. 连续认证的实际公式

新高度导数循环为
\[
(\cos m\phi,-\sin m\phi,-\cos m\phi,\sin m\phi),
\]
并乘 \(m^k\)。offset 只加入位置，不加入任何正阶导数。验证器没有复用旧 sin 的尖谷挠率消元，也没有把旧 sin 的曲率结果转到新模型。

所有位置导数先在同一个 proper 极坐标架中表达，继续使用既有已核的叉积、三重积及 \(q_\ell\) 不变量。每个 cell 分别计算
\[
\kappa>0,\quad
J\ge1-w|q_\ell|,\quad
|\lambda|\le
\frac{(\kappa+\tau^2/\kappa)^+_{\rm cell}}
     {1-w|q_\ell|^+_{\rm cell}}.
\]
没有混乘不同角点的全局最大值。连续高度使用准确固定 offset 的顶点值加
\[
\frac18\left(\sum_j(3j)^2|H_j|\right)(2\pi/N)^2
\]
作为线性插值误差。另保留整 cell 高度区间，取两个已证上界的较小者。

尖、谷的准确有理导数额外通过
\[
\kappa=\sqrt{R^2+Z^2}/r^2,\qquad
q_\ell=(ZU-RV)/(R^2+Z^2)^{3/2}
\]
验证。其中 \(R=r''-r,U=r''''-6r''+r,Z=z'',V=z''''\)。
\(\tau=0\) 不会删掉一般非零的 \(q_\ell\)。

若全圈空间曲率已证正，则按偶高度的反射论证认证零 framing。正径向投影单独证明中央曲线嵌入；有限宽核心嵌入和 reach 仍明确保持 false。条件幅度预算仍要求未来全部过渡及帽共享同一个投影、高度包络。

## 3. 最小 Actions 命令

先开发检查：

```bash
python topics/visible-flex-new-mechanism/scripts/space_star_cosine_verify.py \
  --check-only \
  --out "$VISIBLE_OUT/cosine-verifier-check.json"
```

这个检查只使用合成参数，包含准确圆柱位置、cos 导数的区间不变量交叉检查、尖谷公式、同侧反射，以及数值位置的全部一阶和混合/纯二阶导数差分。它不扫描研究候选。

在同一个 Actions lane 中，设计器已把一个明确选中的候选写到
`$VISIBLE_OUT/cosine-design.json` 后：

```bash
python topics/visible-flex-new-mechanism/scripts/space_star_cosine_verify.py \
  --input "$VISIBLE_OUT/cosine-design.json" \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --nodes 32768 \
  --out "$VISIBLE_OUT/cosine-frozen-N32768.json"
```

设计输入也可来自本题已公开的 notes。验证器只允许本题 notes 或当前 Actions 的 RUNNER_TEMP 输入；真实研究验证要求
`GITHUB_ACTIONS=true` 且仓库为 `Rogerhu12/math-research-public`。

若某轮只需连续验证，可加 `--skip-numerical-interface`。加密时保持同一个输入文件和同一物理哈希，只改变 `--nodes`。不得把新的优化或高度平移叫作固定参数精化。

## 4. 材料角和完整二 jet 接口

```python
from cosine_rectifying_core import CosineRectifyingCore
core = CosineRectifyingCore.from_verified_report(report)
data = core.evaluate(s, theta)
```

`evaluate` 返回 `X, Xs, Xtheta, Xss, Xst, Xtt, normal, phi, q_ell, J`，
并报告材料方程残差。输入只允许 \(|s|\le w\)，不向外推断新 connector。

准确模型由
\[
\ell(\phi)=\int_0^\phi|\gamma'|,\qquad
a_0=\ell(2\pi)/(2\pi),\qquad
\ell(\phi)+s q(\phi)=a_0\theta\pmod{\ell(2\pi)}
\]
定义。实现用固定 Gauss 分块求积及带括区间的 Newton 反解；数值 \(a_0\) 必须落在连续证书的积分包围内。它没有用插值重拟合新的曲线。

完整二 jet 使用
\[
X_s=B,\quad X_\theta=a_0T,\quad
X_{ss}=\frac{\tau^2}{\kappa J}N,\quad
X_{s\theta}=-\frac{a_0\tau}{J}N,\quad
X_{\theta\theta}=\frac{a_0^2\kappa}{J}N.
\]
`jet` 只支持总阶数不超过二的六项；请求更高混合导数会报错，不填零冒充。正负端口 \(\pm w\) 独立评估，保留逐侧的镜面对称而不假定旧的交换两侧半转。

即使数值接口检查失败，原区间输出也会保留，并单独记接口错误；不会把一次浮点反解故障改写成连续几何反例。反过来，数值接口通过也不提高连续结论的等级。

## 5. 当前尚未取得的结果

新脚本准备完成时，还没有任何实际 cosine 候选的连续 \(\kappa/J/\lambda\) 结果。它解除的是旧奇高度的拓扑路线障碍并提供可验证入口；完整闭面、两个圆领、固定握持尺寸和全局 reach 仍未构造。
