# 固定 dyadic 型的正参数十七处四次扭曲族：实际 primitive 分块

日期：2026-11-12。状态：§1–3 的角色与有限表示比较已证明；
§4 的秩使用 Cremona 数据体系中的准确 Mordell–Weil 秩，
其中 E17 的秩二另有本仓库 R4 的完整下降证明。
本篇只核具体固定四条曲线；其中只有 E17 的秩为二。
它不排除改变 dyadic 型后的 E34，亦不排除其他固定有限候选族。

## 1. 固定族与全局角色

取
$$
E^{(k)}:\ y^2=x^3-17^k x,\qquad0\le k\le3,\qquad K=\mathbb Q(i).
\tag{1}
$$
选实数 $\alpha>0$、$\alpha^4=17$。在 $K(\alpha)$ 上使用
$$
\iota_k:E^{(k)}\longrightarrow E^{(0)},\qquad
(x,y)\longmapsto(x/\alpha^{2k},y/\alpha^{3k}).
$$
和[Dirichlet 中心比较](2026-11-12-dirichlet-lambda-and-actual-quartic-center.md)
中的直接 Galois 计算相同，在所选 CM 直线上有
$$
\rho_k=\epsilon^k\rho_0,\qquad
\epsilon(\sigma)=\frac{\alpha}{\sigma\alpha}.
\tag{2}
$$
因此这里确实是同一个四次 Hecke 角色的四个幂，不是事后
把三个局部特征任意命名成三条曲线。

在 $\mathbb Q_2$ 中，$17$ 是四次方。可直接对 $X^4-17$ 在
$X=3$ 使用 Hensel：$v_2(3^4-17)=6>2v_2(4\cdot3^3)=4$。
故 $\iota_k$ 可在 $\mathbb Q_2$ 定义，而且与 CM 作用交换。
所有 $E^{(k)}$ 的二处 CM 表示、单位化 Hecke 特征和 Weil
splitting 相同。其实际向量是已证的 $\mathbf1_{\mathbb Z_2}$，见
[二处向量](2026-11-12-dyadic-vector-and-reference-theta.md) §§2–4。

无穷处的有限角色 $\epsilon^k$ 平凡，四条曲线的单位化无穷型相同。
在 $2,17$ 以外，有限角色未分歧，Yang 的未分歧向量仍可取
$\mathbf1_{\mathbb Z_\ell}$。因此比较可在同一极化、同一无穷
Hermite 规范及同一二处向量上进行。

## 2. 十七处的准确指数是 $k$，不是 $2k$

固定 $i\mapsto4\pmod {17}$ 的 split 分量，令
$$
K\otimes\mathbb Q_{17}=\mathbb Q_{17}\oplus\mathbb Q_{17},
\qquad K_{17}^1=\{(a,a^{-1})\}\simeq\mathbb Q_{17}^\times.
$$
以 E17 已固定的方向记 $\lambda(3)=-i$。
由 (2)，split 第一分量上
$$
\chi_{k,17}(a,1)=\chi_{0,17}(a,1)\lambda(a)^k
\qquad(a\in\mathbb Z_{17}^\times).
\tag{3}
$$

Yang（1997）Corollary 2.10(i) 的自然极化作用准确为
$$
\omega_\chi(a)v(y)=\chi(a,1)|a|^{1/2}v(ay).
\tag{4}
$$
原文紧接式 (2.24) 已区分 $\chi(a,1)$ 与
$\chi(a,a^{-1})=\chi(a,1)^2$。所以不能把 norm-one 限制的
平方再代入 (4)，那会把 primitive 四次块错误地压成二次块。

在单位群上 $|a|=1$，且参考 $\chi_{0,17}(a,1)=1$。于是
$$
\omega_k(a)v(y)=\lambda(a)^k v(ay).
\tag{5}
$$
从 $17^{1/2}\mathbf1_{1+17\mathbb Z_{17}}$ 作归一紧平均，得到
$$
v_k(y)=\frac{\sqrt {17}}{16}\lambda(y)^{-k}
                 \mathbf1_{\mathbb Z_{17}^\times}(y),
\qquad k=1,2,3.
\tag{6}
$$
直接证明：若 $y$ 非单位，平均为零；若 $y$ 为单位，恰有
$a\equiv y^{-1}\pmod {17}$ 的一个陪集贡献，测度 $1/16$，
乘子为 $\lambda(y)^{-k}$。由 (5) 可再核 $\omega_k(a)v_k=v_k$。

比较时须把三条线放在同一个参考作用
$\omega_0(a)v(y)=v(ay)$ 下，此时
$$
\omega_0(a)v_k=\lambda(a)^{-k}v_k.
\tag{7}
$$
极化转换 $\rho$ 是 Yang 式 (2.28) 中的固定算子，与 $k$ 无关，
所以 (7) 是同一有限 Schrödinger 表示中的实际三条 primitive 线。
这里没有从一个特征的形式幂跳过其 dyadic 或 archimedean 数据。

对本课题的 $4\mid m$ 中央权族，有限四次部分仍为原角色：
$2m+1\equiv1\pmod4$。故这些线也保持在各自完整权族中；
不存在随 $m$ 把 $\lambda$ 与 $\lambda^3$ 任意交换的规范自由。

## 3. 五维空间的直接分解

在 $\operatorname{Fun}(\mathbb F_{17},\mathbb C)$ 中用
$(a\cdot v)(y)=v(ay)$。平凡角色重数二，基可取
$\delta_0$、$\mathbf1_{\mathbb F_{17}^\times}$；
每个非平凡乘法特征的重数一。

全局 $i$ 对应 $a=4$，而 $4$ 在 $\mathbb F_{17}^\times$ 中
阶为四。故 $i$-不变部分准确为
$$
\operatorname{Fun}(\mathbb F_{17})^{\langle4\rangle}
=
\langle\delta_0,\mathbf1_{\mathbb F_{17}^\times}\rangle
\ \oplus\ \mathbb C v_1\ \oplus\ \mathbb C v_2\ \oplus\ \mathbb C v_3.
\tag{8}
$$
这是 $2+1+1+1$ 的分解，不是四条 rank-two 曲线的分解。
前三节的全局角色计算把后三条线分别识别为
$E_{17},E_{289},E_{4913}$ 的实际有限向量。

参考未分歧向量 $\mathbf1_{\mathbb Z_{17}}$ 落在前面的平凡类型；
两个同范数整数 CM 缩放也在该类型中，完整证明见
[有理 CM 缩放类型](2026-11-12-theta-rational-cm-scaling-type.md)。
原全局 theta 映射在这些固定有限 Schwartz 向量上的单射性也已在
该笔记 §4 证明。因此不能借一个 theta 核把 (8) 的不同类型混合。

## 4. 哪些曲线真的满足秩门槛

Cremona 的 Table One 明确把第五列定义为 Mordell–Weil 秩；
Table Two 给经作者核定的完整 Mordell–Weil 生成元。
本次直接核读原数据，得到：

| $k$ | 曲线 | Cremona 标号 | 准确秩 | 有理挠子 |
|---|---|---|---:|---|
| 0 | $y^2=x^3-x$ | 32a2 | 0 | $C_2\times C_2$ |
| 1 | $y^2=x^3-17x$ | 9248g1 | 2 | $C_2$ |
| 2 | $y^2=x^3-289x$ | 9248e1 | 0 | $C_2\times C_2$ |
| 3 | $y^2=x^3-4913x$ | 9248f1 | 0 | $C_2$ |

源为 John Cremona，
[Elliptic Curve Data](https://johncremona.github.io/ecdata/)，
表说明更新于 2020；
[原 allcurves 文件](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999)、
[原 allgens 文件](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allgens/allgens.00000-09999)，
本次核读日期 2026-11-12。
此处引用秩和生成元表，不引用 BSD 预测的 Sha 阶。
E17 的独立下降证明为 R4；本篇未重新运行另外三条曲线的完整下降。

因此，在这个已经识别角色的固定族中，满足主问题秩门槛的
集合准确只有 $\{E_{17}\}$。把同族的有理同源曲线也加入没有改变：
有理同源保持秩，并保持每个 $p$ 的 Sha 初级部分是否有限。
后一事实由同源与其对偶的复合是非零整数乘法，作用在
$T_p\Sha\otimes\mathbb Q_p$ 上互为标量逆立即推出。

## 5. 有限覆盖路线在此具体族上的剩余条件

若要用有限并/抽屉原理，须证明无穷多个 $p$ 中至少一条
秩已达门槛的成员通过完整有限性判据。对 (1)，这个条件
仍然要求 E17 自己对无穷多个 $p$ 通过判据。

在五维 theta 空间中找到一个中心导数非零的向量，或证明三个
primitive 块不同时消失，都不足以代替这个条件：另外两个
primitive 块来自秩零曲线，前两个维数又是参考的平凡类型。
这不是抽象的维数警告，而是 (2)–(8) 和上述准确秩给出的实际
分块对照。其他固定有限扭曲族仍可研究，但它们需要新的合格成员
及其真正非同时消失恒等式。

一手 theta 来源：T. Yang，*Theta liftings and Hecke L-functions*，
J. reine angew. Math. **485** (1997)，25–53，
§2.2、Corollary 2.10、Corollaries 2.12–2.14、式 (2.24)、(2.28)，
[作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
