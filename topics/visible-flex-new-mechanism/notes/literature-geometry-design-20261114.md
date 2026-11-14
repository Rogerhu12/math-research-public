# 在同一个闭合机制内扩大可用带宽

状态：独立几何设计方案，待公开 Actions 实算。它没有给出等距连续族。

来源是公开 [Ghomi–Qiu–Raffaelli–Zhang 预印本](https://arxiv.org/html/2611.17269v1) 的闭渐近带结构，和本题 `literature_band_seed.py` 已实现的反射对称闭合分支。旧单 bump 的实际曲率问题见 `literature-kernel-actions-43585440463.md`。这次先寻找更温和的基带，避免在极窄物理支撑上归一大位移。

## 1. 有严格正速度的显式闭合参数

写 $x=q\theta$、$q\ge2$，取

\[
r=1+a\cos x,\quad 0<a<1,\qquad
\varphi=\theta+\frac bq\sin2x,
\]

\[
B=\frac{(r\cos\varphi,r\sin\varphi,1)}{\sqrt{1+r^2}},\qquad
v=(1+r^{-2})\lambda,
\]

\[
\lambda=\frac{(1-c\cos2x)^2+\eta}{2bc},\qquad
\eta=2bc-1-c^2/2.
\]

本轮令 $c=1/b$，因此 $\eta=1-1/(2b^2)>0$，只需 $b>1/\sqrt2$。同时保留既有分支的 $b<\pi/2$ 条件。速度严格为正。

中心线按 $d\alpha=vT\,ds=-v B\times dB$ 定义。其竖向导数为 $-\lambda\varphi_\theta$；展开并利用三角正交性可得整周期平均为零。水平两分量因 $q$ 重旋转对称而积分为零。因此中心线闭合。反射 $\theta\mapsto-\theta$ 使球面曲率和 $v$ 为偶函数、$\kappa_\theta$ 为奇函数，故 $\oint\kappa_\theta/\sqrt v\,d\theta=0$，特征坐标的周期条件也满足。

$b=1.5,c=2/3$ 时，单独的 $\lambda$ 最大/最小值之比为4；总速度还乘 $1+r^{-2}$，所以不能把4误报为整个 $v$ 的比。这仅是缓和速度对比的入口，实际曲率、特征带宽和点对间隙仍须计算。

## 2. 有限设计扫描具体检查什么

`scripts/literature_band_geometry_scan.py` 枚举27个 $(q,a,b)$ 和三个物理半宽比例，另保留原 curvature-speed 种子作对照。每个设计先固定参考中心线直径样本和物理半宽，再计算：

- 两个闭合积分的实际求积缺陷；周期原函数去掉的零模不会隐藏。
- 解析带一、二基本形式给出的主曲率样本和基带直径样本。
- 同一闭特征条带在所有 $s$ 处的最小实际 $u$ 宽度；这是归一可见扰动时二阶导数成本的重要几何尺度。
- 排名前四个设计保持参数不变，加密角点，并以分块矩阵检查有限带点对的法球弦比。

法球弦比使用真实位置和法向：

\[
\frac{|X(q)-X(p)|^2}{2|\langle X(q)-X(p),\nu(p)\rangle|}.
\]

有限样本最小值只能作必要尺度筛查；它不能给连续 reach 下界，也不证明带嵌入，更不能替代最终闭面及全部时间的法球检查。所有 $(q,a,b,\text{width})$ 都是不同设计，不能将它们混称为同一固定度量的加密。

## 3. 与二阶校正工作的接口

`literature_band_kernel.py` 和 `literature_band_second_order.py` 已有 `--kind symmetric --a ... --b ... --c ...` 入口。该分支的 $\omega$ 从固定32768角节点参考计算并固定 Fourier 系数，随后任意评估网格复用同一表示；报告原周期残差与弃项系数的L1界。旧 curvature 输入和默认值不变。

扫描若给出较好的基带，下一步仍要检验完整二阶周期障碍、有限非线性路径和真实曲率。较宽或较平缓的基带本身不是连续可弯面的证据。
