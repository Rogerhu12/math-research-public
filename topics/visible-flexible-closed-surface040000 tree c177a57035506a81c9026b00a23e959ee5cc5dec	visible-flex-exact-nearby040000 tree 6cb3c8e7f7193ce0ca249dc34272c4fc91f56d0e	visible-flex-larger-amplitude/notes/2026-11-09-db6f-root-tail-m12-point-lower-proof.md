# R21 指定 M12 实际闭图的正误差点下界

状态：完整点证书已实际 exit 0；下述论证复用已独审 R21/背景/point 公式，本次小 wrapper 与新算例待独立审查。没有得到新解或支付 G5。作者 Astra-visible-flex-db6f0b0e，2026-11-09。

## 1. 唯一指定的图和固定度量

本稿只指 R21 的 critical 第一档闭图：`db6f-root-flat17-common-cut-m12-critical-r01.json`，以及该图的尾 manifest `db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json`。脚本对二者、完整 whole-v2 汇总、精确背景 transfer packet 和已审旧 M8 point 证书分别检查冻结 SHA256，不接受另一个未审候选。

R21 §1–2、§4 已证这里的实际有限尾与该闭图一致；上尾的整个高度反射与竖直平移不改变诱导度量。背景 transfer packet 的 `background_definition_hashes` 与旧 point 证书逐项相同，脚本同时重核六个实际背景文件和 point 公式依赖文件的 hash，并核 packet 的新旧 manifest 连接与其余物理参数相同声明。因此复用的是同一个固定 $g$ 的背景 $w$，不是把旧 M8 checkpoint 与新 M12 的求解状态视为同一件数据。

旧 `db6f-root-tail-metric-point.py` 的 CLI 仍保留原输入 checkpoint guard，字节未改。本稿 wrapper 显式绑定 R21 已审的这一个异 checkpoint/同 $g$ 算例，直接复用其已审 `point_metric` 及 background point enclosure。此连接不能推广到任意新 manifest。

## 2. 取点与误差下界

选择有限尾 span **17148**，局部参数 $u=3/4$；实际半径为精确有理数

$$
r=542597661727932063391508010872115368615351/1247347073977141182794646048914448905666560.
$$

材料角 $\theta=2\pi/6$。旋转标架的 Fourier 频率全为三的整数倍，因此这里每个三角因子都是精确 $0,\pm1$。径向系数来自由该 manifest 保存的二进数据及精确径向增量定义的五次多项式，使用有理 $u$ 和向外区间 Horner 求值；背景 $w(r)$ 用已独审 point-Lipschitz 真背景包。

在 $g$ 的正交归一标架，令

$$
B=g^{-1/2}(F^*e-g)g^{-1/2}.
$$

已审公式分别计算 $B_{rr},B_{r\theta},B_{\theta\theta}$。对任意实对称矩阵，$\|B\|_{\rm op}\ge |B_{ij}|$，因为 $|e_i^TBe_j|\le\|B\|_{\rm op}$。该点的 `$B_{rr}$` 区间给出

$$
\|B\|_{\rm op}\ge
L=\frac{370012576184137}{18889465931478580854784}
>1.95883\cdot10^{-8}.
$$

$L$ 是报告中向外二进端点的**精确**有理值；比较十进下界用 Fraction 完成，未把小数打印当作向外端点。故 R21 闭图的全域实际相对误差 $E_{12}$ 满足 $E_{12}\ge L>1.95883\cdot10^{-8}$。全相位由 R21 的解析相位作用保持该误差最大值。

计算共考察同 span 的 $u=1/4,1/2,3/4$ 和四个特殊角，共12点；取其中最大下界仍然是合法单点存在见证，不用于任何全域上界推断。

## 3. 后续可使用的比较及范围

R21 已有 $E_{12}<2.57212\cdot10^{-8}$。本稿给它补上正下界；如果未来**同 $g$ 的实际完整新闭图**被严格认证 $E_{\rm new}\le2\cdot10^{-9}$，则可由 $E_{12}>9.79415 E_{\rm new}$ 证明又一次实际误差下降（这个写法也涵盖 $E_{\rm new}=0$）。这个条件当前尚未得到满足，UNSOLVED M15 affine prefix 的采样数值不能代入。

本稿没有认证任何精确等距解、无限尾极限、完整联解或 README 完成。它只是为后续固定 $g$ 加密比较提供已指定旧图的严格正下界。

## 4. 复跑与记录

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-root-tail-m12-point.py --out <新的JSON路径>
```

脚本拒绝覆盖已有输出；默认参数就是上面的 span/12点，默认要求正下界超过 $2\cdot10^{-9}$。真实执行 exit 0，报告的 `requested_lower_proved=true`。独立复跑应换输出路径，并比较全部数学字段及输入 hash，忽略耗时。

- 脚本：`scripts/db6f-root-tail-m12-point.py`，SHA256 `5d950fa6caa3aff062ba5a62e743abac5b00d7ef0721930f299135d1dbdc1bb1`。
- 记录：`notes/2026-11-09-db6f-root-tail-m12-point-metric-witness.json`，SHA256 `13311ea4ecb781d0607ff6b58880c5f70bd79db2df2527aa9de3b6d9ad2e1b5e`。
- 新脚本只完成固定输入连接和搜索调度；point 公式/背景供应器没有改动。
