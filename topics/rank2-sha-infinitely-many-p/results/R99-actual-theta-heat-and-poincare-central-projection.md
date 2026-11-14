# R99. 原完整 theta 的热兼容式与实际 Poincaré 中央投影

## 热算子与公共参考均已明确

在保持原挠点有理周期标签的方向
\[
\mathscr W=-A^{-1}
 \left(\bar\omega_1\partial_{\omega_1}
       +\bar\omega_2\partial_{\omega_2}\right),
\]
原 reduced/translated Kronecker theta 满足
\[
\mathscr W\Theta_P=\partial_z\partial_w\Theta_P.
\]
因此 \(W_P=w\Theta_P\) 的准确热算子是
\[
\mathcal L=\partial_z\partial_w-w^{-1}\partial_z,\qquad
\mathscr WW_P=\mathcal LW_P,\qquad
\mathscr Wd_m=(m+1)^2d_{m+1}.
\]
两个阶乘来自原 Eisenstein–Kronecker 展开，未换成裸 Jacobi theta。

对真实 \(a=-p,q=p^2\) 同源修正 \(T_aW=W^qE\)，
\(\mathcal LT_a=qT_a\mathcal L\)。
完整乘积公式给
\[
\mathscr WE=-(q-1)E\mathcal L\log W
 +(\partial_z\log W)\partial_wE
 +(\partial_w\log W)\partial_zE
 +q^{-1}\mathcal LE.
\]
交叉项不能删去。

参考归一的原标签和
\(\mathcal A=\sum_P W_P/W_T\) 满足
\[
\mathscr W\mathcal A
=\mathcal L\mathcal A+B_z\partial_w\mathcal A+B_w\partial_z\mathcal A,
\quad B_z=\partial_z\log W_T,\quad B_w=\partial_w\log W_T.
\]
这两个漂移的周期增量均为 \(\bar\gamma/A\)，故不能通过有限
椭圆覆盖变成有理函数。原参考实际有
\[
[\mathcal LW_T]_2=17zw+\frac{34}{3}w^2\ne0.
\]
这是自然全 theta 连接的范围；不否定 R47 中央 Borel 的有限 GM 实现，
也不排除增添通用向量扩张坐标或新的中央消去。

## 原对象的实际 Poincaré 实现与两个不同 CM 投影

Sprang 的几何 Eisenstein–Kronecker 对象自然位于
\(\operatorname{Sym}^{k+r+1}H^1_{\rm dR}(E)\)。
其定义先要求两个标签非零。取固定 \(N=68,D=69\)，准确分配式给
\[
\sum_{0\ne Q\in E[69]}\widetilde e_{j,j+1}(P,68Q)
=68\,\widetilde e_{j,j+1}(P,0).
\]
因此以固定 \(1/68\) 平均得到真正承载原零标签数据的
\(\mathcal E_m\in\operatorname{Sym}^{2m+1}H\)，没有中央零除零。

其极端 CM 投影准确为
\[
\operatorname{pr}_{H_+^{2m+1}}\mathcal E_m
=(m!)^2d_m\,\omega^{2m+1}.
\]
作行列式规范
\(V_m=\operatorname{Sym}^{2m+1}H\otimes(\det H)^{-m}\) 后，
中间两条线本来给固定 \(H_+\oplus H_-\)；
但实际原迹在这两条线的投影均为零：
一条来自已经证明的 \(d_0=0\)，另一条在自然 Hodge 支撑之外。

原目标位于极端型
\[
x^{m+1}y^{-m},
\qquad\text{即 }\psi^{m+1}\bar\psi^{-m}.
\]
一个固定有限维 CM torus 表示只有有限多个权，
所以不能以固定中间 \(H^1\) 或固定有限 Artin 标签因子
代替所有这些变化的目标极端权。
此结论只限制这里构造的 CM 等变比较，不排除别的 prime-diagonal 实现。

公共参考仍有非平凡 Poincaré 线丛类：
其对角限制次数为 \(2\)，经 \([68]\times[68]\) 拉回后为 \(2\cdot68^2\)。
已发表的完整 de Rham polylogarithm 实现使用对数层塔，
不能仅凭预期斜率把它压成尚未构造的固定张量类。

## 证明与后续范围

[热算子、漂移与实际同源交换式](../notes/2026-11-12-actual-theta-heat-and-relative-frobenius.md)
及[原 Poincaré 实现与 CM 投影](../notes/2026-11-12-original-theta-poincare-cm-projection.md)
均已根端全文审计；热稿另经第二位研究者独审。
Bannai–Kobayashi 的原规范、Sprang 的构造/投影及零标签分配原文均已核对。
未借用有疑问的低 Hodge 组合因子数值；所用支持和两项投影不依赖它们。

R98 的具体跨权源没有被这些比较消去。
接下来继续 O4 导出类、O6 全局中心核及 O8 实际整数流的未解决条件，
不把已关闭的自然固定张量候选重列为非零输入。
