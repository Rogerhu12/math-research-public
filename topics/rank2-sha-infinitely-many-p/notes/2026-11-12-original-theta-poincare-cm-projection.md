# 原 theta 的 Poincaré 实现、固定 $H^1$ 投影与中央 CM 权

日期：2026-11-12。状态：本篇的固定除法平均、原中央系数的
对称幂实现、固定 $H^1$ 投影为零及 CM 权比较均已证明。
这里审计的是一个具体候选几何实现；没有排除指定 prime diagonal
另有不同的有限维实现，也没有证明无穷多个素数的中央导数非零。

## 1. 对象和需要区分的两个投影

沿用 R47/R87 的 $E=E_{17}$、原 $256$ 个导子挠点集合
$\mathcal S\subset E[68]\setminus\{O\}$ 与准确平移 theta：
$$
\Theta_P(z,w)=\frac1w+
 \sum_{a,b\ge0}\frac{\widetilde e_{a,b+1}(P,0)}{a!b!}z^bw^a,
\qquad
d_m=[z^mw^m]\sum_{P\in\mathcal S}\Theta_P(z,w).
\tag{1}
$$
因而
$$
\sum_{P\in\mathcal S}\widetilde e_{m,m+1}(P,0)=(m!)^2d_m.
\tag{2}
$$
这里以 (1) 固定 $\widetilde e$ 的符号和阶乘规范。
原中央首值
$$
d_0=\sum_{P\in\mathcal S}U_P=0
\tag{3}
$$
已经由 R18/R47 的原导子迹证明；不是本篇新加的高度或 Sha 假设。

令 $H=H^1_{\rm dR}(E)$。在 CM 域上有代数分解
$$
H=H_+\oplus H_-,
\qquad [\alpha]^*|_{H_+}=\alpha,
\quad[\alpha]^*|_{H_-}=\bar\alpha.
\tag{4}
$$
解析记号 $\omega=dz,\bar\omega=d\bar z$ 分别生成这两条线。
需要区分：

- $\operatorname{Sym}^{2m+1}H\to H_+^{\otimes(2m+1)}$ 的极端
  Hodge/CM 投影；它包含实际 $d_m$。
- 乘 $(\det H)^{-m}$ 后，指向固定 $H_+\oplus H_-$ 的中间
  CM 投影；本篇证明实际原迹在这里为零。

## 2. 用固定 $69$-除法平均付清第二标签为零的接口

Sprang（2019）Definition 4.1、Theorem 4.2 首先要求两个挠点标签
均非零且阶互素。不能直接把其中第二标签设为零。
但同文 Proposition 7.2 的证明，印刷 pp.25–26，给出精确分配式：
对 $(N,D)=1$、$P\in E[N]\setminus\{O\}$，
$$
\sum_{0\ne Q\in E[D]}
 \widetilde e_{k,r+1}(DP,NQ)
=D^{k-r+1}\widetilde e_{k,r+1}(P,0)
 -\widetilde e_{k,r+1}(DP,0).
\tag{5}
$$
它先在绝对收敛的格点和中由有限字符正交性得到，再由同一
Eisenstein–Kronecker 延拓成立；特别包含所需 $k=r$。

现在固定
$$
N=68,\qquad D=69.
$$
于是 $DP=P$。对所有 $j\ge0$，(5) 简化为
$$
\sum_{0\ne Q\in E[69]}
 \widetilde e_{j,j+1}(P,68Q)
=68\,\widetilde e_{j,j+1}(P,0).
\tag{6}
$$
尤其分母是同一个固定非零整数 $68$，没有随 $m$ 变化的
分配因子，也没有在中央权处出现零除零。

设 $\mathcal E^{k,r+1}_{P,Q}$ 是 Sprang Definition 4.1 的
真实代数 Poincaré 连接值。定义
$$
\mathcal E_m
=\frac1{68}\sum_{P\in\mathcal S}
                  \sum_{0\ne Q\in E[69]}
                       \mathcal E^{m,m+1}_{P,Q}
\in\operatorname{Sym}^{2m+1}H.
\tag{7}
$$
先在同时定义全部挠点的有限扩张上构造，再对 $69$-挠点求和，
所得对象下降到原 $68$-标签域。若再对原 $256$ 标签取规定的迹，
这正是 (7)，并没有增添自由的标签选择。
本篇在特征零中使用 (7)；若要求该特定 $69$-模型的整性，
须另排除 $3,23$，本篇并未拿它作所有目标素数的整模型。

## 3. 实际极端分量非零数据与中间分量的严格消去

Sprang Proposition 4.6 把每个 $\mathcal E^{k,r+1}_{P,Q}$
展开为以下 CM 单项式的线性组合：
$$
\bar\omega^i\omega^{k+r+1-i},
\qquad 0\le i\le\min(k,r).
\tag{8}
$$
第 $i$ 项的系数是明确的有理组合因子乘
$A^{-i}\widetilde e_{k-i,r-i+1}(DP,NQ)$；
其中 $i=0$ 的组合因子为 $1$。
这里只需要 (8) 的支持范围及各项所用的 EK 指标，
不需要更改该文的对称张量约定。

在 (7) 中令 $k=r=m$，由 (6) 可以逐项还原原零标签值。
因此得到两个准确结论：
$$
\boxed{\quad
\operatorname{pr}_{H_+^{2m+1}}(\mathcal E_m)
=(m!)^2d_m\,\omega^{2m+1}.
\quad}
\tag{9}
$$
另一方面，(8) 中唯一可能给出
$H_+^{m+1}H_-^m$ 的项是 $i=m$；它的系数是固定非零
组合因子乘 $A^{-m}\sum_P\widetilde e_{0,1}(P,0)$。
由 (3) 这项为零。分量 $H_+^mH_-^{m+1}$ 则根本不在 (8) 中。
所以
$$
\boxed{\quad
\operatorname{pr}_{H_+^{m+1}H_-^m\,\oplus\,
                      H_+^mH_-^{m+1}}(\mathcal E_m)=0.
\quad}
\tag{10}
$$
这个证明保留了实际 Poincaré 参考和实际全部标签。
它不是仅根据对称幂的维数增长而猜测中间分量无用。

## 4. 中央 Tate 规范与目标 Hecke 字符

把对称幂作中央行列式规范：
$$
V_m=\operatorname{Sym}^{2m+1}H\otimes(\det H)^{-m}.
\tag{11}
$$
在抽象 CM torus 坐标 $(x,y)$ 下，第 $i$ 条线的字符为
$$
x^{m+1-i}y^{i-m},\qquad0\le i\le2m+1.
\tag{12}
$$
$i=m,m+1$ 正是固定的 $x,y$，即 $H$ 的两条 CM 线。
由 (10)，真实原迹到这两条线的投影均为零。

实际目标 (9) 是 $i=0$，其字符为
$$
\boxed{\quad x^{m+1}y^{-m}
       =x^{2m+1}(xy)^{-m}.\quad}
\tag{13}
$$
在 R47 使用的 Hecke 规范中，这就是
$$
\psi^{m+1}\bar\psi^{-m}
=\psi^{2m+1}(\psi\bar\psi)^{-m}.
\tag{14}
$$
若改用对偶 étale 约定，各字符同时对偶，不改变
“中间固定、目标极端且随 $m$ 变化”的结论。

这些字符两两不同。严格地说，若一个固定有限维对象 $V$
带有与 CM 相容的 torus 作用，则 $V$ 只有有限多个权。
任何 CM-equivariant 映射 $V_m\to V$ 对 (13) 的限制，除有限多个
$m$ 外都为零。这也适用于固定有限 Artin 标签因子：在有限扩张后，
其在连通 CM torus 上为平凡，不会抵消随 $m$ 变化的字符。

所以不能从 $V_m$ 中选出固定 $H^1$ 的中间型，再用它代替
本题的极端型。也不能只因为 $H^1\otimes H^1(-1)$ 的某个
$p$-斜率看起来合适，就声称已经得到作用于所有实际中央权的
CM-compatible 比较映射。这是指定候选的范围结论；
它不排除不通过 (7) 的其他 prime-diagonal 构造。

## 5. 固定 $[68]$ 有理覆盖为何没有删掉公共参考

R87 证明
$$
\Theta_P(68z,68w)
=\Theta_T(68z,68w)\frac{A_P(z+w)}{A_P(z)},
\tag{15}
$$
其中 $A_P$ 为固定有理函数。公共参考的线丛类仍是平移后的
Poincaré 类。记 $m:E\times E\to E$ 为加法，则其数值类为
$$
m^*\mathcal O_E(O)
\otimes\operatorname{pr}_1^*\mathcal O_E(O)^{-1}
\otimes\operatorname{pr}_2^*\mathcal O_E(O)^{-1}.
\tag{16}
$$
把 (16) 拉到对角线上，其次数是 $4-1-1=2$。
再经 $[68]\times[68]$ 拉回，次数变为 $2\cdot68^2$，仍非零。
因此这个固定覆盖没有把公共参考变成全局平凡线丛。
有理比值 (15) 不改变这件事。

这只排除在整个适当曲面上把它当作平凡的绝对平坦标量。
在去掉除子的开集上，当然可以用一个亚纯截面作框架；
但由此得到的普通标量 jet 并不自动等于原规范的加法 jet。
Sprang §4.1 的两条连接分别沿两个相对方向可积，
同节印刷 p.10 明确指出它们一般不交换。
把二者误拼成没有漂移的绝对平坦线连接，会丢失原中央系数。

Sprang（2020）Theorem 4.7、Theorem 5.8 给出的真正 de Rham
polylogarithm 实现使用整个对数层塔：把 Poincaré 丛限制到
对偶椭圆曲线或其二维 universal vectorial extension 的第 $n$ 阶
无穷小邻域，再沿有限投影推出，得到秩分别为
$n+1$、$\binom{n+2}{2}$ 的层。
这是一套准确的几何实现，但不是一个已经保留所有实际中央
投影的固定 $H^1\otimes H^1(-1)$ 类。

## 6. 本分支的结论与后续接口

(7)–(10) 给出了此前固定张量候选所需的实际对象审计：
原 theta 确有完整代数 Poincaré 实现；其自然固定 $H^1$
中间投影恰为零，实际 $d_m$ 位于 (13) 的移动极端 CM 权。
固定参考的混合线丛类和热连接漂移也仍在。

因此 R98 中跨权 cochain 的实际非齐次源，不能仅由这个
固定 $H^1$ 投影消去。当前没有据此构造出独立非零的中央类。
接下来回到 O4：对实际导出 Kolyvagin/Heegner 类及完整 Selmer
局部条件寻找不预设 Sha 有限的非零输入。

## 来源

- J. Sprang（2019），*Eisenstein–Kronecker series via the Poincaré bundle*，
  Forum of Mathematics, Sigma **7**, e34，
  DOI [10.1017/fms.2019.29](https://doi.org/10.1017/fms.2019.29)。
  [作者预印本](https://arxiv.org/pdf/1801.05677)：
  §4.1、Theorem 4.2、Proposition 4.6；第二零标签的精确分配式见
  Proposition 7.2 的证明，印刷 pp.25–26。
- J. Sprang（2020），*The algebraic de Rham realization of the elliptic
  polylogarithm via the Poincaré bundle*，Algebra & Number Theory **14**,
  545–585，DOI [10.2140/ant.2020.14.545](https://doi.org/10.2140/ant.2020.14.545)。
  [作者预印本](https://arxiv.org/pdf/1802.04996)：§4.1、Theorems 4.7、5.8。
- 原迹、Borel 及覆盖的全部规范：
  [R18](../results/R18-rational-layer-and-fixed-fermat-quotient.md)、
  [R47](../results/R47-central-borel-modular-form-and-exact-growth.md)、
  [R87 工作全文](2026-11-12-translated-kummer-units-and-original-theta-cover.md)。
- 原参考的准确热漂移与同源交换项：
  [实际热方程](2026-11-12-actual-theta-heat-and-relative-frobenius.md)。
