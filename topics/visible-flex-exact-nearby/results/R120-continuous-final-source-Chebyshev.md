# R120 补篇：对最终源插值的真实连续径向证书

2026-11-13，newton_source。**已证明，限定域如下。**

对原来的 R33 候选、同一固定目标及整个 $\eta=10^{-9}$ 参数盒，
在完整连续域

$$
0\le r\le10^{-4},\qquad \theta\in\mathbb R/(2\pi\mathbb Z)
$$

上，真实球面 Newton 标量源满足

$$
\boxed{\quad
\left\| -\tfrac12\mathcal C_s(\rho^2(g_0-g_F))\right\|_{C^0}
<0.703693.\quad}
$$

这是真正连续的径向和角向界，包含完整无穷 primitive 尾。
它只覆盖所列小区间，不是全体1477个正半 scalar germs，更不是闭面全域或收敛。
改进的关键是对**最终小源本身**作径向插值，避免把整个径向盒的 primitive
系数分别取区间后才形成小差。

## 1. 同一源的全纯延拓及真实分母

本区间属于原来已安装的 scalar germ
$[0,2609037194989121/1152921504606846976]$。
把这个准确的 scalar 多项式分支复解析延拓；不把延拓后的域声明成新的物理区域。
令

$$
c=\frac1{20000},\qquad h=\frac1{20000},\qquad R=\frac1{5000}=4h.
$$

`scripts/fourfold_phase_newton_source_complex.py` 在复矩形
$|\Re r-c|\le R,\ |\Im r|\le R$ 上实际计算；此矩形包含闭复盘
$|r-c|\le R$。所有 dot products 使用复双线性延拓，
没有把 Hermitian 范数的非全纯共轭误塞进 source 公式。
原 R117 (117.23) 在代入 $\rho^2=T^{-1}$ 后是有理式；
本入口在最终源中消去了不必出现的 $\sqrt T$，不需要另选复平方根分支。

精确目标径向均值通过真正零 Fourier 卷积计算：

$$
E=\sum_k \widehat F_{r,k}\cdot\widehat F_{r,-k},\qquad
E'=2\sum_k\widehat F_{r,k}\cdot\widehat F_{rr,-k},
$$

另加完整 primitive 余项的乘积误差。这里的均值是原目标
$\langle |F_r|^2\rangle$ 的唯一复双线性延拓，不是重新选择目标。
这个单独的零卷积避免把全部非零模的区间误差当作独立常数项误差。

程序对每个角格检查 $a,E,G,T,S$ 都不含零，并检查
$\det s=S^2/T^3$ 的非零性。实际报告给整个复矩形的下界

$$
|E|>1.228974,\quad |G|>1.370453,\quad |T|>1.005866,
\quad |S|>1.180634,\quad |\det s|>0.816249.
$$

因此这些同一分母在所用复盘内处处非零。scalar 分支与三角函数解析，
primitive 的完整 Fourier 估计在该域一致收敛，故真实源对 $r$ 全纯。
参数仍在同一个完整实 $\eta$ 盒；所有断言对每个参数同时成立。

用 R120 同一 Banach 代数误差法（这里非零系数允许为一般复数，不做 Hermitian
投影），实际全角计算得到

$$
|q(r,\theta)|<M=69807.875274\quad (|r-c|\le R).
$$

粗复盘界虽然很大，但下面把它只用于指数小的插值余项。

## 2. 最终源的径向插值及无限余项

取 $m=16$ 个准确 Chebyshev 根

$$
r_j=c+h\cos\frac{(2j+1)\pi}{2m},\qquad 0\le j<m.
$$

每个 $r_j$ 由 Arb 包在一个确切 dyadic 小区间内；程序在该整个区间、
全部16384个连续角格及整个参数盒上重新计算完整源。
因此节点输入不是未付误差的浮点值。

设 $P_{m-1}$ 为这些准确节点值的 Chebyshev 插值多项式。
其系数由完整区间 DCT 计算：常数系数使用 $1/m$，其余使用 $2/m$。
本次 $m=16$ 时这两个比例本身是确切 dyadic；一般非二次幂情形
代码用 Arb 对准确比例向外包围。所有 cosine 系数也用 Arb 包围。

节点 source 的每个角格区间给该格上插值系数的区间，且
$|T_k(x)|\le1$ 对 $|x|\le1$，所以逐格系数绝对值和给整个实径向区间的
真实插值多项式上界。本次得到

$$
\|P_{15}\|_\infty<0.702999.
$$

还需付完整径向余项，而不是只检插值节点。令 $T_{m-1}^{\rm Tay}$ 是源在
$c$ 处的真实 Taylor 截断。Cauchy 估计及 $\kappa=h/R=1/4$ 给

$$
\|q-T_{m-1}^{\rm Tay}\|_{[-h,h]}
\le\frac{M\kappa^m}{1-\kappa}.
$$

Chebyshev 插值重现所有次数小于 $m$ 的多项式。由 DCT 表达式即可直接得
其 Lebesgue 范数不超过 $2m-1$：常数系数至多输入sup，其余每个系数至多两倍输入sup，
而每个 $T_k$ 的sup至多1。因此

$$
\|q-P_{m-1}\|\le
(1+(2m-1))\frac{M\kappa^m}{1-\kappa}
=\frac{2mM\kappa^m}{1-\kappa}
<0.000693479.
$$

这付的是所有径向 Taylor 阶，不是只多算若干阶。
与完整插值多项式包络相加，实际准确输出为

$$
\|q\|_\infty<0.703692387836080<0.703693.
$$

## 3. 实际运行、保存与适用边界

复盘入口及结果：

- `scripts/fourfold_phase_newton_source_complex.py`；
- `notes/2026-11-13-newton-source-near-waist-complex-native.json`。

完整径向插值入口及结果：

- `scripts/fourfold_phase_newton_source_radial_interpolation.py`；
- `notes/2026-11-13-newton-source-near-waist-continuous-native.json`。

后者逐节点保存真实区间、source 包络、完整 primitive 误差，
再保存全部16个 Chebyshev 系数界、Cauchy比例、无限径向余项、
依赖源码 SHA 与复盘报告 SHA。原生复盘运行13.63秒，插值运行168.50秒。
复盘使用512个primitive节点、4096连续角格；真实节点source使用512/16384。
不同有限网格均包围同一个无限几何，未改变真实对象。

```sh
python scripts/fourfold_phase_newton_source_complex.py \
  --left 0 --right 1/10000 --radius-factor 4 \
  --out notes/2026-11-13-newton-source-near-waist-complex-native.json

python scripts/fourfold_phase_newton_source_radial_interpolation.py \
  --complex-report notes/2026-11-13-newton-source-near-waist-complex-native.json \
  --out notes/2026-11-13-newton-source-near-waist-continuous-native.json
```

此前整个首自然germ的复盘试算在分母非零门失败；它不是已通过证书，
失败原因不能借本小区间结果删除。
同germ中点单独真计算 source 上界0.626341，表明普通宽盒的966319主要是
相关性损失；中点本身当然不覆盖整germ。

本篇已经闭合一个真实连续源子域。后续扩大到全体自然germs需更有效的
复盘分母/最终源包络，且必须支付强角档、完整右逆和非线性收敛，
不能把这个限定域上界宣布为整个闭面的 Newton 门。
