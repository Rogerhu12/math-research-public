# 完整 Bernstein 参考的实时间 q 门

本文补充 `2026-11-12-complete-reference-real-time-image.md`，对应新源
`scripts/fourfold_complete_reference_real_time_q.py` 和可续跑的
`fourfold_complete_reference_real_time_cover.py`。不改动已冻结的
complete-reference adapter；两者使用同一个准确有限 retarget 函数。

## 1. 物理角关于归一化标签的导数

沿用八个完整原段 Bernstein 控制

\[
Y_j(x)=x/4+C_j(x),\qquad
Y(s,x)=\sum_{j=0}^7B_j^7(s)Y_j(x),\quad0\le s\le1.
\]

所有原始 U、Q 与静态初值修正的 Laurent 乘积都被保留；后腿还保留
完整 \(Q_{f,\mathrm{end}}\) 因子。这里

\[
q(s,x)=Y_x(s,x)=\sum_{j=0}^7B_j^7(s)q_j(x),\qquad
q_j(x)=\tfrac14+C_j'(x).
\tag{1}
\]

这个 \(q\) 是**所选有限参考**的导数，不是辅助多项式 Q，也不是尚未
支付误差的真实 flow Jacobian。归一化标签为 x=4θ，所以常数项为1/4。

若 \(C_j\) 的正频率为 \(c_{jk}\)，其完整实轴实值性给出

\[
\Re q_j(x+iS)=\frac14+
\sum_{k=1}^K\{ikc_{jk}\cosh(kS)e^{ikx}
 +\overline{ikc_{jk}\cosh(kS)}e^{-ikx}\}.
\tag{2}
\]

它是实 Fourier 多项式，正频率为 \(ikc_{jk}\cosh(kS)\)，均值准确
为1/4。上边界和下边界的实部由准确共轭对称完全相同。

## 2. 完整角覆盖和时间凸性

对 (2) 使用与像门相同的闭单元 \(x_\ell\pm\pi/N\)、p阶实角
Taylor 表以及全部有限频率的完整余项。记有向表为 \(T_{r\ell}\)，
完整余项为 \(R_{p+1}\)。每个闭单元分别有

\[
\Re q_j\ge
\underline{\Re T_{0\ell}}
-\sum_{r=1}^{p}|T_{r\ell}|-R_{p+1},
\qquad
\Re q_j\le
\overline{\Re T_{0\ell}}
+\sum_{r=1}^{p}|T_{r\ell}|+R_{p+1}.
\tag{3}
\]

实现先对每个单元结果取准确有向 lower/upper，再在全部单元取 min/max。
不会用重叠 Arb 球的偏序比较来代替最大上端点。整个角周期由这些闭
单元覆盖。对标签带的调和最大／最小值原理和两边界实部的共轭关系，
(3) 控制整个 \(|\Im x|\le S\)。由 (1) 的非负 Bernstein 权重，全部
八个控制函数的最小下界同时控制整个实时间段和所有准确 subspan。

另外保留一个完整但较粗的模上界：

\[
|q_j(x+iS)|\le\frac14+
2\sum_{k=1}^K k|c_{jk}|\cosh(kS).
\tag{4}
\]

全带最大模原理和时间凸性再次给出全部实时间、整个复标签带的 (4)。

若得到 \(m>0\)，则 \(q\) 在这一完整集合上不为零；若充分下界不正，
代码保存失败门及实际下界，不能据此宣称 q 有零点。它不推断任何非实
时间盘的 q 门，复时间预算仍由 `continuous_bidisk` 独立支付。

## 3. 正实部还能给出的准确坐标结论

固定任一实时间。假设 (3) 已证明 \(\Re Y_x\ge m>0\) 于整个闭带。
对任意两点 \(z_1,z_2\) 在该凸带内，

\[
\frac{Y(z_2)-Y(z_1)}{z_2-z_1}
=\int_0^1Y_x(z_1+t(z_2-z_1))\,dt
\]

的实部至少为m，所以

\[
|Y(z_2)-Y(z_1)|\ge m|z_2-z_1|.
\tag{5}
\]

因此该 lift 在全带单叶，而非仅局部无零导数。实轴上它严格递增，且
\(Y(x+2\pi)=Y(x)+\pi/2\)，故它把实轴满射到实轴。

任给实 \(w_0\)，取唯一实 \(x_0\) 使 \(Y(x_0)=w_0\)。在圆周
\(|z-x_0|=S\) 上，(5) 给 \(|Y(z)-w_0|\ge mS\)。对
\(|w-w_0|<mS\)，Rouché 定理与已证单叶性说明 \(Y(z)=w\) 在此盘
恰有一个解。因此 Y 的像包含物理角带 \(|\Im w|<mS\)，其解析逆
在该内带满足 \(|(Y^{-1})'|\le1/m\)。这仍是准确**参考**的坐标结论，
不代付真实 flow 对它的接近程度。

## 4. 当前计算和准确继续入口

新全扫同时支付前腿每段：

- 实时间像，标签带1/512、1/256、1/128；
- Re q门，工作标签带1/256；
- N=512、p=8、256bits、完整八控制和全部乘积频率。

源 `fourfold_complete_reference_real_time_cover.py` 逐段保存小 gzip leaf，
index 对全部完成 leaf 的路径、字节数和SHA逐一核对后才能续跑。最后
还核对全部 leaf 哈希与完整请求集合，才标 `whole_reference_leg=true`。
`all_real_time_q_positive` 和 `all_inside_comparison_strip` 是单独的
实际门，不会因为计算结束就自动设置为真。

此前 image-only runner 仅完成前腿0–2；因工作带和 q 门新增，保留其
源、未完成 index 和三个 leaf 后停止，换用新共同扫描，未把旧未完成
index 改成全覆盖。完整新结果需要以最终冻结 index 或明确的部分检查点
为准；本页不预先宣称前腿550段都通过。
