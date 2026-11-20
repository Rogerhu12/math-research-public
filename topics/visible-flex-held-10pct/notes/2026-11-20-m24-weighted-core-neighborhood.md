# 新 g M24：覆盖全部高模的严格核心邻域与整条同伦曲率界

维护会话：Astra-held10-1b6d88ec-20261120。

本条对[实际M24前缀](2026-11-20-m3-newg-wide-m16-spectrum-and-m24-prefix.md)
的全部23个物理support控制建立新邻域。旧M8参数盒不被搬用。
精确有理程序已实际 exit0，并核对当前实际参数在邻域内。
结论只涉及以这些参数定义的R53真积分平面核心；
GL位置/材料反函数有限实现的误差、完整Frenet域、BVP和闭面仍须另付。

## 1. 邻域由真实二进制参数定义

以实际run
c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a
中的c6,...,c72为中心向量 $(\bar c_2,\ldots,\bar c_{24})$。
[小参数文件](../scripts/resume_m3/multistage_m24_core_neighborhood.json)
保存全部binary64 hex，按其精确有理值解释，不把短十进制显示当另一个中心。

设任意有限M≥24，将中心在j>24补零，取

$$
q\in[599/10000,601/10000],\qquad
\sum_{j=2}^{M}(9j^2-1)|c_j-\bar c_j|\le1/100.
$$

它是对物理support系数的加权邻域，不是raw参数的无权球，也不是允许
Newton无条件越出的许可。已有M24中心当然在其中；以后真实尾或升M返回，
须再对完整实际c向量核验一次同一个加权距离。

## 2. 全角正性严格通过

原support函数与曲率半径为

$$
h(\phi)=1+q\cos3\phi+\sum_{j=2}^{M}c_j\cos3j\phi,
\qquad\rho=h+h''.
$$

当前中心的精确加权和为

$$
C=\sum_{j=2}^{24}(9j^2-1)|\bar c_j|
=\frac{14451985358671943599097}{604462909807314587353088}.
$$

三角不等式在整个法向角圆周给出

$$
|\rho-1|\le 8\frac{601}{10000}+C+\frac1{100}
=:B<\frac{103}{200}.
$$

所以统一有

$$
\boxed{\frac{97}{200}<\rho<\frac{303}{200}}.
$$

实际更紧的下界1−B约.48529119579681274；显示值不参与严格比较。
因此原核心完整材料曲率位于
$[1/(1+B),1/(1-B)]$，尤其下界大于200/303>1/5。
所有高阶项都在求和中；没有只核前七个控制。

## 3. 二进制窗参数也进入严格计算

当前设置S=.5、b=.2、k=.2、τ=1，其中b、k按实际binary64值解释。
故没有把binary .2悄悄替换为精确1/5。它们满足S+b<1<π/3，
且1/5≤k<原核心曲率下界。

R53窗口的精确九次对称step满足
$J=\int_0^T\chi=2S+b$，$T=2\pi/3>2$。
令 $a=1/(1+B),\ b_0=1/(1-B)$；
沿当前固定τ=1的整条λ∈[0,1]同伦，[R53式(4)](../results/R53-material-flattening-homotopy-and-positive-domain.md)
直接给

$$
0\le\beta\le(b_0-k)\frac{J}{T-J}
<(b_0-k)\frac{J}{2-J},
$$

$$
\boxed{\frac15\le\kappa_\lambda
\le b_0+(b_0-k)\frac{J}{2-J}<\frac{243}{50}=4.86}.
$$

全部末端比较均为Fraction；π只使用解析不等式π>3，
没有浮点三角取样。所得更紧显示上界约4.851546167853267。
R53的真积分定义同时保持周长2π、旋转闭合与严格凸性；
这里仅把它应用到新的实际高模邻域，不重复证明结构定理。

这给当前宽窗核心留下充分曲率余量，但没有证明首cycle中非核心
曲面仍有同一K上界。准确k圆弧也只在λ=1出现，当前λ=.002不能提前
使用最终握持片或10%位移结论。

## 4. 已执行命令和用途

~~~bash
python topics/visible-flex-held-10pct/scripts/resume_m3/certify_weighted_support_neighborhood.py \
  --center topics/visible-flex-held-10pct/scripts/resume_m3/multistage_m24_core_neighborhood.json \
  --candidate-run /workspace/scratch/1b6d88ecddf3/m3-work/newg-wide-lambda0p002-m24-linear/run.json \
  --out topics/visible-flex-held-10pct/notes/2026-11-20-m24-core-neighborhood-execution.json
~~~

[短执行记录](2026-11-20-m24-core-neighborhood-execution.json)
保存所有界的精确分子/分母、源与中心文件SHA256和实际membership=True。
不提供candidate-run时，可仅用发布的小参数文件重算同一个数学证书；
未来检查新真实返回时替换candidate-run，不能修改中心后还称沿用原邻域。
当前新增高M允许范围来自加权定义，而不是放大旧M8每坐标上界。
