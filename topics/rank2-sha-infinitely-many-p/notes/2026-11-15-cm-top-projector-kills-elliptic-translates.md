# 原最高 CM 投影与所有椭圆平移曲线的 Chow 消失

日期：2026-11-15。**状态：下列有理等价命题已证明。**
本注给 [R832](../results/R832-original-triple-chow-purity-and-rank-zero-contractions.md)
的实际 CM 几何比较一个明确限制。它不判定原唯一端点类非零，
也不把一个抽象动机同构当作给定曲线的像。

## 1. 模型、对应及结论

在特征零的代数闭域上取原 $j=0$ 曲线 $E_0$，令
$$
A=E_0^3,\qquad
\rho=(1+\sqrt{-3})/2,\qquad
u=[\rho]\times[\rho]\times[\rho].
$$
故 $\rho^2-\rho+1=0$、$\rho^3=-1$。
系数取含 $K=\mathbf Q(\sqrt{-3})$ 的特征零域 $\mathcal E$。

用原点定义椭圆曲线的真正 Chow--Künneth 对应 $\pi_0,\pi_1,\pi_2$。
在 $\pi_1$ 上按 CM 对应 $[\rho]$ 分解出 $\pi_+,\pi_-$；
它们是实际有理等价范畴中的多项式投影。
置
$$
\Pi_{\mathrm{top}}
 =\pi_+^{\otimes3}+\pi_-^{\otimes3}.
\tag{1}
$$
不论以 pullback 或 pushforward 给两个符号命名，在这个和上都准确有
$$
\Pi_{\mathrm{top}}u_*=-\Pi_{\mathrm{top}}.
\tag{2}
$$
这是每个本征值的三次方均为 $-1$，不是仅在某个实现中相等。

**命题。** 对任意椭圆子群 $B\subset A$ 和任意 $a\in A$，
$$
\boxed{\Pi_{\mathrm{top}}[a+B]=0
 \quad\text{于 }\operatorname{CH}^2(A)_{\mathcal E}.}
\tag{3}
$$
更一般，任意从光滑亏格一曲线到 $A$ 的态射，其一维像的推前均被 (1) 杀掉。
因此由这些曲线像的有限 $\mathcal E$ 线性组合形成的 cycle，也全部满足 (3)。

## 2. 平移曲线的 degree-three 分量确实随平移点相加

本节保留 Fourier 的绝对约定，避免把 algebraic equivalence 误作 rational equivalence。
记 $\widehat A$ 为对偶，$\mathcal P_A$ 为原点正规化的 Poincaré 线丛，
$$
\mathcal F_A(x)
 =p_{\widehat A,*}\bigl(p_A^*x\,
       \exp(c_1(\mathcal P_A))\bigr),\qquad
\ell_a=c_1(\mathcal P_A|_{\{a\}\times\widehat A}).
$$
使用有理系数，$\mathcal F_A$ 可逆，交换 Pontryagin 积与交积，
并满足
$$
\mathcal F_A([a])=\exp(\ell_a),\qquad
\mathcal F_A([n]^*x)=[n]_*\mathcal F_A(x).
\tag{4}
$$
这些是在 Chow 群中的恒等式。所用标准 Fourier 定理见
A. Beauville，*Quelques remarques sur la transformation de Fourier dans l'anneau de Chow
d'une variété abélienne*，LNM 1016 (1983), 238--260，
[作者全文](https://math.univ-cotedazur.fr/u/beauvill/pubs/fourier.pdf)，
§2 Proposition 3(i)--(iii)、Corollaire 2；点的等式也直接来自定义。
本文后面的平移及 CM 结论由以下计算证明。

令 $i:B\hookrightarrow A$。对偶态射 $\widehat i:\widehat A\to\widehat B$
为光滑商映射，其原点纤维是一个余维一的阿贝尔子群。
Poincaré 的定义给
$$
(i\times1)^*\mathcal P_A=(1\times\widehat i)^*\mathcal P_B.
$$
代入 Fourier 定义，用投影公式和这个光滑基变换，即得
$$
\mathcal F_A(i_*x)=\widehat i^*\mathcal F_B(x).
$$
椭圆曲线维数为一，$\mathcal F_B([B])=-[0_{\widehat B}]$，
所以
$$
\beta_B:=\mathcal F_A([B])
 =-\widehat i^*[0_{\widehat B}]
 \in\operatorname{CH}^1(\widehat A).
\tag{5}
$$
特别，$\beta_B$ 是对称除子类，$[n]^*\beta_B=n^2\beta_B$。
而 $\ell_a\in\operatorname{Pic}^0(\widehat A)$，满足
$$
[n]^*\ell_a=n\ell_a,\qquad
\ell_{a+a'}=\ell_a+\ell_{a'}.
\tag{6}
$$

我们使用 $[a+B]=[a]*[B]$，这里的平移是 pushforward $t_{a,*}$。
(4)--(5) 因而给准确有限展开
$$
\mathcal F_A([a+B])
 =\exp(\ell_a)\beta_B
 =\beta_B+\ell_a\beta_B+\tfrac12\ell_a^2\beta_B.
\tag{7}
$$
更高项由 $\dim A=3$ 消失。若把平移改记为 pullback，$\ell_a$ 相应换负；
本注始终使用 (7) 的约定。

令
$$
w_j(a)=\mathcal F_A^{-1}
 \left(\frac{\ell_a^j\beta_B}{j!}\right),
 \qquad j=0,1,2.
$$
由 (6)，Fourier 端的第 $j$ 项在 $[n]^*$ 下乘 $n^{j+2}$。
又 $[n]_*[n]^*=n^6$，结合 (4) 得
$$
[n]^*w_j(a)=n^{4-j}w_j(a).
\tag{8}
$$
因此三个项分别属于 Chow--Künneth 的 degree $4,3,2$。
这里也可以只取 $n=2$，用三个互异特征值和 $E_0^3$ 的乘积
Chow--Künneth 投影直接分开，不需要任何未证的 Chow 分次消失猜想。

记 $\pi_3^A$ 为整个 degree-three 投影。由 (7)--(8)，
$$
\boxed{
\varphi_B(a):=\pi_3^A[a+B]
 =\mathcal F_A^{-1}(\ell_a\beta_B).
}
\tag{9}
$$
于是 $\varphi_B:A(\overline{\mathbf Q})\to\operatorname{CH}^2(A)_{\mathcal E}$
在点的群法下是加性映射。这是所需的真正有理等价结论；
不是声称整个 $a\mapsto[a+B]$ 本身加性。

## 3. 每个椭圆子群都被对角 CM 自同构保持

取 $B\to E_0$ 的一个非零坐标投影。它是椭圆曲线间的同源，
所以存在一个同源 $h:E_0\to B$。
复合 $i h:E_0\to E_0^3$ 的三个分量均属于 $\operatorname{End}(E_0)$，
因而与 $[\rho]$ 交换。故
$$
u\circ i h=i h\circ[\rho].
$$
取像即得 $u(B)=B$。这是对任意椭圆子群的证明，
不要求先选出三个坐标图形。

$u$ 与乘整数及其 Chow--Künneth 投影交换；
利用 $u_*[a+B]=[u(a)+B]$，(9) 给
$$
u_*\varphi_B(a)=\varphi_B(u(a)).
\tag{10}
$$
点的群上 $u^2-u+1=0$。由 $\varphi_B$ 加性，
$$
(u_*^2-u_*+1)\varphi_B(a)
 =\varphi_B(u^2a-u a+a)=0.
\tag{11}
$$
另一方面，$\Pi_{\mathrm{top}}=\Pi_{\mathrm{top}}\pi_3^A$，
且由 (2)，
$$
\Pi_{\mathrm{top}}(u_*^2-u_*+1)
 =(1+1+1)\Pi_{\mathrm{top}}=3\Pi_{\mathrm{top}}.
$$
对 (11) 施加 (1)，有理系数下除以三，
就得到 (3)。全文没有把实现的忠实性推广到任意高阶 Chow 群。

## 4. 亏格一像、有限扩域及原课题的实际含义

在代数闭域上给亏格一曲线选原点，任意到阿贝尔簇的态射都是
一个群同态再接平移。其非常数像于是为某个 $a+B$，
推前只另乘该态射到像的有限次数。因此命题适用于所有这样的曲线像，
也适用于这些像的任意有限线性组合。

亏格零曲线到阿贝尔簇的态射为常值，不给非零的一维推前。
故一个在 (1) 下非零的 cycle，不能由几何亏格至多一的曲线像
在有理等价意义下表示。这里没有声称所有高亏格曲线的投影非零。

所有所需数据都定义在有限扩域上。
若原对象带有限 Artin 扭曲，可先到一个固定有限扩域消去该扭曲；
该步骤只适用于已经给出的真正 Chow 对应。
返回原域时，restriction--corestriction 的合成是扩域次数，
所以有理系数下的消失不因返回而失效。

在 R832 的三低权张量中，原最高 $\lambda$ 在这样的固定扩域上由 (1) 实现。
因此：

- 若某个 拟议的 cycle 比较把原最高部分实际送成椭圆图形、椭圆子群
  平移或其有限组合，它送到的最高部分必为零。
- 同一 CM $L$ 因子、同一抽象两维实现，均不能据此把原类改成这些曲线。
- 要把 [R814](../results/R814-common-fixed-good-pair-and-three-original-aj-squares.md)
  的指定类与 R831 唯一端点类比较，仍须给出对实际 cycle 的对应；
  R817 的一个 $p$ 的非零不构造这个对应，也不传递到别的 $p$。
- 本命题不消掉上一笔记的坏位高度补项。那里是两个对偶输入的配对；
  这里是某一明确曲线家族的单个 Chow 投影恒等式。

本注只关闭“用 literal 亏格一图形/平移表达非零最高类”这一具体方式。
原高亏格 cycle 的对应、端点非零、完整指定 $p$-adic AJ 与无穷素数主目标均继续。
