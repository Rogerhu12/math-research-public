# ψ-warp 核的填充投影见证：不预设径向图（2026-11-14）

## 结论与文件接口

`scripts/warped_ruled_projection.py` 提供

```python
projection_audit(certificate, half_width_text, witness_count=12)
```

输入为 `scripts/warped_ruled_core.py` 的 `certified_centerline(u_text,v_text,scale_text,nodes)` 返回值。新模块不修改该精确核心、材料角或任何参数；它读取已经认证的中央位置盒子、导数界和有限多边形，检验旋转见证点到**填充投影集合**的距离。

关键区别是：到闭曲线的正距离本身不能证明点在填充域外。模块先证明见证点所在的补集分支无界，然后才使用曲线距离。主证明不要求曲线简单、径向单值或具有正定向。

本文件及脚本只完成连续几何证书的准备。真实候选 `u=.6,.8,1,1.2; v=0` 的计算在本公开仓库 Actions 执行；本地只运行合成射线、精确 winding 与单位圆接口检查。

## 1. 填充集合与必要的外部判定

令 \(C=c_{xy}(\mathbb S^1)\subset\mathbb R^2\) 为精确中央投影的紧致像集。令 \(U_\infty\) 为 \(\mathbb R^2\setminus C\) 的唯一无界连通分支，并定义

\[
 \operatorname{Fill}(C)=\mathbb R^2\setminus U_\infty.
\]

这是包含曲线及其所有有界补分支的紧集，即使投影自交也定义良好。这里只把它当作后续过渡曲面必须满足的**条件投影容器**，没有证明真实封口已在其中。

**命题 1。** 若 \(q\in U_\infty\)，则

\[
 \operatorname{dist}(q,\operatorname{Fill}(C))
 =\operatorname{dist}(q,C).
\]

证明：因为 \(C\subset\operatorname{Fill}(C)\)，左端不大于右端。设右端为 \(d\)。开球 \(B(q,d)\) 连通且与 \(C\) 不交，因此整个球都在含 \(q\) 的补集分支 \(U_\infty\) 内。故该球也与填充集合不交，得到反向不等式。此证明不依赖 Jordan 性。

若存在一条从 \(q\) 出发、一直通向无穷且不交 \(C\) 的连续路径，则 \(q\in U_\infty\)。本实现选择整条射线，不以有限几个射线样本冒充无交证明。

## 2. 曲线、顶点和多边形误差

输入的有序顶点中点 \(v_i\in\mathbb R^2\) 是准确的 binary64 数；每个真顶点 \(c(2\pi i/N)\) 到 \(v_i\) 的 Euclidean 误差不超过 \(\epsilon_v\)。已有核心证书还给出

\[
 \sup_\phi|c_{\phi\phi}|\le M_2.
\]

设 \(P\) 为相邻 \(v_i\) 的闭折线、\(h=2\pi/N\)。参数一致的线性插值误差给出

\[
 \epsilon_c=\epsilon_v+\frac{M_2h^2}{8},\qquad
 \sup_\phi|c(\phi)-P(\phi)|\le\epsilon_c.
\]

这是向量值二阶导数的弦插值界；不是由网格中点“看上去平滑”推断。输入的三维误差和三维二阶导数界也可用于二维投影，因正交投影不增距离。

选取一个有限顶点参数 \(i\)，将其真位置的 xy 盒子准确旋转 \(\pi/3\)：只使用有理数和 \(\sqrt3\) 的定向区间，不使用未经认证的浮点三角函数。得到 \(q\) 的盒子及 binary64 中点 \(q_0\)，令 \(|q-q_0|\le\epsilon_q\)。若计算出的多边形距离包围为 \([d_P^-,d_P^+]\)，则

\[
 \operatorname{dist}(q,C)\in
 [\max(0,d_P^- -\epsilon_c-\epsilon_q),
  d_P^+ +\epsilon_c+\epsilon_q].
\]

只有下一节的外部判定成功后，这个区间才标为到 \(\operatorname{Fill}(C)\) 的距离。

## 3. 整条射线的外部证书

取非零 binary64 向量 \(d_0\)，作为准确实向量定义射线

\[
 R_0=\{q_0+t d_0:t\ge0\}.
\]

默认取 \(d_0=q_0\)，仅是尝试寻找逃逸方向，不假设 \(q_0\) 是全曲线最大半径点，也不假设实际中央曲线相对于原点为径向图。

### 3.1 与每条边的交点排除

对多边形边 \([A,B]\)，令

\[
 c_A=\det(d_0,A-q_0),\quad c_B=\det(d_0,B-q_0),
\]

\[
 p_A=d_0\cdot(A-q_0),\quad p_B=d_0\cdot(B-q_0).
\]

下列任一证书可排除该边与射线相交：

1. \(c_A,c_B\) 严格同号，整条边位于射线所在直线的一侧；
2. \(p_A,p_B<0\)，整条边在射线起点后方；
3. \(c_A-c_B\ne0\)，直线交点的边参数 \(t_e=c_A/(c_A-c_B)\) 已证不在 \([0,1]\)，或该交点的纵向坐标 \(p_A+t_e(p_B-p_A)\) 严格为负。

全部运算使用逐初等操作向外扩张的 IEEE-754 区间。若某条边既未证相交也未证不交，模块给它零间隙下界，不作有利的猜测。共线边在起点前方和后方分别处理。

### 3.2 射线到整条边的距离

已证边与射线不交后，二者的最近点对至少有一个有限端点；非平行且两参数都在内部时，距离函数的两个驻点条件会强迫距离为零，和不交矛盾。平行情形沿共同方向移动一个最近点对，可到达有限端点而保持同一距离。因此

\[
 \operatorname{dist}(R_0,[A,B])=
 \min\{\operatorname{dist}(q_0,[A,B]),
       \operatorname{dist}(A,R_0),
       \operatorname{dist}(B,R_0)\}.
\]

这些点到线段/射线距离均由准确的投影、截断和范数公式作定向包围。取所有边的最小下界 \(r_P^-\)，则真实起点的平行射线

\[
 R=\{q+t d_0:t\ge0\}
\]

满足

\[
 \operatorname{dist}(R,C)\ge r_P^- -\epsilon_c-\epsilon_q.
\]

若该数严格为正，**整条无限射线**避开真曲线，故 \(q\in U_\infty\)。这里不需要先给射线截断长度，也没有只检查离散射线点。

## 4. 可选径向图证书与 winding 备选

模块还利用 `position_cells` 和 `derivative_cells` 求整个参数圈的

\[
 \det(c,c_\phi)>0
\]

下界，并用到原点的多边形距离减 \(\epsilon_c\) 证明原点不在曲线上。还须验证**绕原点的 winding 恰为 1**；只证角速度正，不能排除多绕。

多边形 winding 直接对 binary64 坐标转成准确有理数计算。曲线到多边形的参数一致直线同伦若避开原点，二者 winding 相同。于是正角速度加 degree 1 证明中央投影为单值径向 Jordan 曲线。

若某条默认逃逸射线未成功，但上述 Jordan 证书成立，可另用 \(q\) 的多边形 winding 为 0、加距离同伦的正间隙，证明 \(q\) 位于外部。这个备选在代码中明确记录；不会从一般自交曲线的 winding 为 0 直接推出属于无界补分支。

## 5. 直径及未来闭面的条件预算

全多边形直径使用全部顶点对的定向距离，不假设某三个外尖就是最远点。真曲线的直径满足

\[
 D_C\ge D_{P,\mathrm{lower}}-2\epsilon_v,
 \qquad D_C\le D_{P,\mathrm{upper}}+2\epsilon_c.
\]

另外 \(\operatorname{Fill}(C)\subset\operatorname{conv}(C)\)：凸包外任一点有一条由分离直线给出的逃逸射线。凸包与原集合直径相同，所以填充集合的直径也等于 \(D_C\)。因此这里的全曲线直径上界同样可用于填充集合。

准确 ruled 核 \(X=c+s d\) 满足 \(|d|=1\)。在 \(|s|\le w\) 上，核心投影属于 \(\operatorname{Fill}(C)_w\)，高度绝对值不超过 \(H+w\)，其中 \(H\) 是已有连续中央高度上界。若认证见证距离下界为 \(\delta_0\)，则有条件预算

\[
 \delta\ge\delta_0-w,
 \qquad
 D\le\sqrt{(D_C+2w)^2+4(H+w)^2}.
\]

将其用于整个闭面的固定握持幅度，仍须实际构造所有连接带/帽、证明其共同投影与高度范围、并完成固定材料握持。这些字段全部保持 `false`。本模块没有认证 reach 下界；已有核心主曲率**下界**只可和直径下界合成必要 reach/D 上界。

## 6. 廉价验证与 Actions 使用

`notes/warped-projection-check-20261114.json` 是本地实现检查，包含外点向外/向内射线、内点射线、直线交点在射线后方、共线边在前/后方、准确 winding 内外/边界判定。另用准确单位圆经过完整 API：证明其为径向 Jordan 图，同时正确拒绝把同圆旋转误当正填充距离。没有使用这些合成例选择真实研究参数。

主脚本已经按以下形式调用本模块：

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/warped_ruled_core.py \
  --warp-u .6,.8,1,1.2 --warp-v 0 --scale 1 --half-width .05 \
  --nodes 1536 --sample-angles 384 --out "$VISIBLE_OUT/warped-ruled-core.json"
```

上述命令仅在本公开仓库 Actions 执行。需要 `warped_ruled_core.py`、本模块及其已有区间依赖；本模块读取 API 的内部顶点数组，但只将小型证书摘要和有限见证点输出到 JSON。
