# 由整个尾的一阶包围控制水平三阶体积矩

2026-11-09，Astra-visible-flex-db6f0b0e。完整条件证明，待未参与者独审。本文不假设有限尾已经与前缀精确接上，也不把一阶尾证书当作等距证书。

## 1. 设定与嵌套平面区域

上尾写成
$$
X(r,\theta)=(\gamma(r,\theta),H(r)+v(r,\theta)),\qquad a\le r\le c,
$$
其中将平面与复数等同，$\gamma=r e^{i\theta}+u$。假定整段为 C²，且
$$
|u|\le\varepsilon_h<a,\quad |v|\le\varepsilon_z,
\quad J=\det(\gamma_r,\gamma_\theta)>0.
$$
每条角截面须严格星形、绕数为一；尾内端为精确圆，即 $u(a,\theta)=v(a,\theta)=0$。令 $D_r$ 为该平面角曲线所围的区域。

记 $\beta=\arg\gamma$，$R=|\gamma|$。星形性给 $\beta_\theta>0$。固定 $\beta$ 求导，利用极坐标雅可比，得到
$$
\left.\partial_r R\right|_\beta=\frac{J}{R\beta_\theta}>0.
$$
因此 $D_r$ 随 $r$ 嵌套；整尾的水平投影是圆盘之间的嵌入环域。又由 $|u|\le\varepsilon_h$，
$$
B_{r-\varepsilon_h}\subset D_r\subset B_{r+\varepsilon_h}.
$$
这是逐截面及全尾的结论，不涉及尾与别的曲面块是否相交。

## 2. 截面的三阶矩

令
$$
P(r)=\int_{D_r}z^3\,dA(z).
$$
圆盘的此矩为零。$D_r$ 与 $B_r$ 的对称差包含在半径 $r\pm\varepsilon_h$ 的圆环内，故
$$
|P(r)|\le 4\pi r\varepsilon_h(r+\varepsilon_h)^3
\le Q:=4\pi c\varepsilon_h(c+\varepsilon_h)^3.
$$
Reynolds 移动边界公式，或对平面 Green 公式求导，给出
$$
P'(r)=\int_0^{2\pi}\gamma(r,\theta)^3J(r,\theta)\,d\theta.
$$
精确圆内端意味着 $P(a)=0$。这些等式允许复杂的参数角速度；没有假设 $\theta$ 就是几何极角。

## 3. 上尾的边界通量

对向量场 $W=(0,0,z_{\rm height}(x+iy)^3)$ 有
$\operatorname{div}W=(x+iy)^3$。上尾外向参数化 $X_r\times X_\theta$ 的竖直分量为 $J$，因此其边界通量为
$$
T=\int_a^c\int_0^{2\pi}(H(r)+v)\gamma^3J\,d\theta\,dr.
$$
分部积分得到
$$
\int_a^c H(r)P'(r)\,dr=H(c)P(c)-\int_a^c H'(r)P(r)\,dr.
$$
设 $B_H\ge\int_a^c|H'(r)|dr$，$R_*=c+\varepsilon_h$。嵌套性和 $J>0$ 给
$$
\int_a^c\int_0^{2\pi}J\,d\theta\,dr
=|D_c|-|D_a|\le\pi R_*^2.
$$
所以完整上尾（包括精确圆领）的通量满足
$$
\boxed{\quad |T|\le (|H(c)|+B_H)\,4\pi c\varepsilon_h R_*^3
          +\pi\varepsilon_z R_*^5.\quad}
$$
它只需整体一阶证书及背景高度界；不需要在极薄尾层对体积三阶矩进行高阶数值求积。

## 4. 与镜像前缀及固定标记帽的组合

若上下尾互为 $z\mapsto-z$ 镜像，其通量相同，合计绝对值至多上式的两倍。两块未标记水平圆盘帽的通量为零。于是当这些块确实组成一个完整 C² 嵌入球面时，设镜像前缀的实部通量下界为 $A_{p,-}$，便有
$$
\operatorname{Re}\int_{\Omega_0}(x+iy)^3dV
\ge A_{p,-}-2|T|.
$$
若右端为正，便支付 R16 所需的完整未标记实体 $A_3\ne0$；反射对称时 $A_3$ 本身为实数。固定的三帽凸起可随后应用 R16。无完整嵌入、正确外向取向和精确公共接缝时，本段只能作为条件论证。

## 5. 当前文件与尚未支付的输入

真实宏观有限前缀报告 `2026-11-09-db6f-root-flat17-coupled-moment.json` 给出镜像通量区间
$$
[0.43484892373304096,\ 0.48095522199304885].
$$
该数由 `db6f-root-volume-moment.py` 对有限 Fourier 图用精确角向求和规则、径向 Bernstein 包围及向外舍入计算，脚本本身仍待独审。它不是完整实体的矩。

尾的一阶证书 `2026-11-09-db6f-tail-first-flat17-m8-q10-n8-s32.json` 给出
$\varepsilon_h<0.00014$、$\varepsilon_z<0.00084$ 以及本证明要求的 $J>0$、逐截面星形性。独审及独立复跑另存。

例如，一旦另证 $|H(c)|\le2$、$B_H\le1$ 且 $c<0.601$，使用 $R_*<0.602$ 和 $\pi<22/7$，两尾总通量的粗上界即小于 $0.003$。这是有严格余量的**条件代入**；背景高度界、公共接缝和完整嵌入仍需明确认证。不能据此提前宣布完整 $A_3$ 或 README 已完成。
