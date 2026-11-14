# Folded bearing：本轮固定入口

**状态：固定 $g$、$e=0$、锁开放非圆核心的 pilot；尚无新 BVP 优化结果。** 只在本公开仓库 Actions 优化。此轮冻结 `scripts/folded_collar_search.py` 和 `scripts/folded_reference_geometry.py`，不接入仍开发中的 inward-fold 接口。详细推导见 `folded-collar-design-20261114.md`。

## 参数的物理含义

本轮共用圆参考参数为 $b=2.4,L=3,r_0=.8,c=.06,p=.15$，核心为 $s\in[1.05,1.95]$ 的开放挤出段。其周长半径数值为 $a_0\approx.8503196368$，总高度约 $1.80677049$。

**默认椭圆参数 `1.4,.5` 只规定形状比，不是物理半轴。** 代码先把椭圆归一化到周长 $2\pi$，再乘该参考的 $a_0$；该输入椭圆的周长半径为 $1.0040828380$。因此本轮物理半轴约为 $1.18560685,.42343102$；它不匹配机制预算中的物理半轴 $1,.3$，也没有全带 $|y|\le.3$ 或包围球半径 $1.15$ 的保证。这个 pilot 检验能否取得固定度量的非圆同轴 bearing，不能据其标签声称达到最终幅度/reach 门。

中央挤出段的 $a'=a''=0$，避免普通回折母线核心 $\kappa_s=-a''\rho$ 造成的必然曲率放大。两过渡分别使用夹持五次 B 样条，固定端领和核心全部二阶 jet；总自由变量不增加。非圆核心不会通过优化退回圆。

## 最小 Actions 命令

只需要已装的 NumPy/SciPy；区间参考脚本用 Python 标准库，无新增依赖。沿用现有 lane 的输出/发布路径。下面三个文件都小于仓库限制。

```sh
python topics/visible-flex-new-mechanism/scripts/folded_reference_geometry.py \
  --beta-wiggle 2.4 --length 3 --radius .8 --collar .06 --plateau .15 \
  --cells 512 --curvature-limit 12 \
  --out "$VISIBLE_NEW_OUT/folded-reference.json"

python topics/visible-flex-new-mechanism/scripts/folded_collar_search.py \
  --engine signed --core-shape curvature --seed2 .25 --seed3 .2 \
  --beta-wiggle 2.4 --length 3 --radius .8 --collar .06 --plateau .15 \
  --controls 14 --modes 6 --radial-order 8 --angles 64 --max-nfev 180 \
  --reference-audit "$VISIBLE_NEW_OUT/folded-reference.json" \
  --out "$VISIBLE_NEW_OUT/folded-signed-curvature-core.json"

python topics/visible-flex-new-mechanism/scripts/folded_collar_search.py \
  --engine cartesian --core-shape ellipse --ellipse-major 1.4 --ellipse-minor .5 \
  --beta-wiggle 2.4 --length 3 --radius .8 --collar .06 --plateau .15 \
  --controls 14 --modes 6 --radial-order 8 --angles 64 --max-nfev 180 \
  --curvature-limit 13 --curvature-weight 0 \
  --reference-audit "$VISIBLE_NEW_OUT/folded-reference.json" \
  --out "$VISIBLE_NEW_OUT/folded-cartesian-ellipse-core.json"
```

默认 offset 为零且脚本明确拒绝非零值。两个 BVP 都保持同一参考 $g=ds^2+a(s)^2du^2$；各自核心形状固定，二者不是同一场的精化比较。Cartesian 此轮不加曲率软权重，但会独立输出真实主曲率，不能用参考曲率替代它。优化和审计结果明确保留 `task_complete=false`。

区间脚本只证明圆参考的几何；512 格是否通过由实际 Actions 输出决定。即使通过，也不传递给非轴 BVP。signed 的有限 Fourier 原函数与闭合残差仍需角精化；Cartesian 的核心材料弧长一、二阶 jet 使用解析公式。

## 已完成的廉价开发核验

没有本地最小二乘迭代。Cartesian/unit/signed 的随机方向 Jacobian 相对差分别约 $8.81\cdot10^{-10}$、$2.56\cdot10^{-9}$、$3.09\cdot10^{-9}$；开放核心全二阶 jet 对任意小系数扰动保持不变。椭圆单位速误差 $4.4\cdot10^{-16}$、周期闭合误差 $7.6\cdot10^{-16}$。这些是表示检查，不是已取得 BVP 解的证据。
