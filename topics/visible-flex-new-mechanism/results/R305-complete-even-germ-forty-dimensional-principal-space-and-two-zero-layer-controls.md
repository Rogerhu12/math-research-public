# R305：完整偶 germ 的实际主秩40与两个新增零层观察

日期：2026-11-15。**完整纸面推导；没有执行新的符号程序、profile 求积、秩计算、人工检查或研究运行。**

[R300](R300-one-history-tail-compensation-and-thirty-eight-dimensional-principal-space.md) 已把全部一层的实际 even principal 定为38维。本稿将 [R296](R296-complete-zero-one-Gaussian-layers-and-the-full-principal-square.md) 的完整主平方用于零层，证明零层只增加两个真正的新方向。连同原二层和六能量，完整中心偶 germ 在原三矩商中的实际主秩准确为40。

两个新增方向都可取为原零层的明确 Laurent 系数，并且准确杀原 $\mathcal W_e$。因此它们可与旧全部主控制坐标在同一个实际有限频率圆上联付。这个结论仍不支付 principal 关系留下的完整低阶基线；不把40维主秩称为整个偶 germ 已解。

## 1. 原对象与准确零层

固定 R241/R293 的实际初始共振安装
$$
h=h_e e^{\varepsilon\sigma^2},\quad
\varepsilon=\kappa^2/4,\quad 0<\kappa^2<1/100,\quad
j=2\varepsilon\kappa\sigma^2=\alpha\sigma^2,\quad
\alpha=\kappa^3/2\ne0.
\tag{1}
$$
所有 profile、右锚、中心表示和实际前缀比较沿 R296/R299。记
$$
\phi_\theta=f\cos\theta+g\sin\theta,\quad D_\theta=f^2-\phi_\theta^2,
\quad
\mathcal W_e=\operatorname{span}\{h,j,(1+j^2)/h\}.
\tag{2}
$$
(2)与原三矩空间仅差第二列的非零常数。

在全部二层及面积已付后，原剩余是
$$
\widehat{\mathscr K}_\theta
=\mathscr R_{0,\theta}
+\sum_{\rho\in\{1,-1,-2,-3\}}E_\rho\mathscr R_{\rho,\theta}.
\tag{3}
$$
R299 从起点加入真实有限 $C^2$ 映射 $\mathcal F^{\rm ang}$ 后，整个中心角项已归约到 $\theta=\pi/2$；实际偶部仅在同一 $\mathcal W_e$ 商中作此比较。

R296 的原 $W_0$ integrand 是奇 $\sigma$ 多项式乘有限 $h$ Laurent 幂。令 $j=\alpha\sigma^2$，对非零指数积分是指数乘多项式，对零指数是普通多项式；真实中心常数另保。故
$$
\mathscr R_{0,\pi/2}\in\mathbb R[j,h,h^{-1}]
\tag{4}
$$
作为有限实际函数表达成立。系数是保所有局部恢复、chain、真实 Volterra 尾的原 quartic profile 泛函。

因为 $h=h_e\exp(j/(2\kappa))$，有限个不同整数指数的指数多项式在任何开放 j 区间上独立。因此在(4)的真实有限表达中，$[h^n j^m]$ 系数有唯一含义；本稿不依赖任意冗余的 Gaussian-word 坐标，也不需要执行数值采样。

## 2. 零层的全部 principal 来自同一个平方

沿 R300 的原 jet 变量，
$$
A=-2u'',\quad B=2u'-2xu'',\quad C=u-xu',
\quad V=x^2C-\frac{x^4A}{4}.
\tag{5}
$$
给 $x,A,B,C,V$ 分别赋权 $1,0,1,2,4$。R300(37)给真实 elementary 系数
$$
\alpha_{\mathsf Q}+2\beta
=\sigma\sum_{r=-3}^{1}h^r V_r(j).
\tag{6}
$$
$V_r$ 的完整多项式表沿该文(38)，其权为 $r+3$。在本稿需要的高权计算中，特别记
$$
V_1=\kappa V/2,\qquad
V_0=p(j)\frac Vx+q(j)x^2B,
\tag{7}
$$
其中 $V/x=xC-x^3A/4$ 本身是多项式，未引入 profile 零点处的除法，并且
$$
p(j)=-\kappa j/3+j^2/5,\qquad
q(j)=\frac{3\kappa^2-2}{16}-\frac{\kappa j}{48}-\frac{j^2}{40}.
\tag{8}
$$
另写
$$
V_{-1}=\ell(j)C+m(j)xB+n(j)x^2A.
$$
R300 的准确表直接给
$$
n+\ell/4=\frac{\kappa^2(j+4\kappa)}8,
\tag{9}
$$
而 $m+jq$ 的最高项为 $-j^3/40$。这些都是原系数身份，不是任意扩大的符号空间。

在一个实际不交微包上，置
$\lambda_i=-a_i^2R_i$、$R_i=a_i^2-b_i^2$。
R296 的整个主平方给零层
$$
\boxed{
\mathscr R_{0,\pi/2}\equiv_2
\sum_i\lambda_i\int
\frac{\sigma^2}{4h}
(1+(hx+j)^2)
\left(\sum_{r=-3}^{1}h^rV_r(j)\right)^2
(u_i''')^2.
}
\tag{10}
$$
$\equiv_2$ 的差是保全部真实尾的 $C^2$ 数据。它不是删去 zero/one/two 间未知余项；(10)只抽原完整平方的零 Gaussian-letter 部分。

定义有限多项式
$$
\boxed{
Z_n(j)=\frac14\left[
(1+j^2)\sum_{r+s=n+1}V_rV_s
+2jx\sum_{r+s=n}V_rV_s
+x^2\sum_{r+s=n-1}V_rV_s
\right],
}
\tag{11}
$$
其中 $-3\le r,s\le1$，两指标按有序和计数；不存在的项为零。于是(10)为
$$
\sum_i\lambda_i\int
\sigma^2\sum_{n=-7}^{3}h^nZ_n(j)(u_i''')^2.
\tag{12}
$$
每个 $Z_n$ 的权恰为 $n+7$。因此零层不会产生超过10权的新符号。

## 3. 与已付38维主空间的比较

R300 的自由符号空间在权0至6已经是全部二次 jet 多项式空间，其各维数为
$$
1,\ 2,\ 4,\ 5,\ 6,\ 6,\ 6.
$$
所以这些权上零层不能增加维数。只需完整检查权7至10；这一步不把最高次数当作实际 rank。

旧高权空间是
$$
\begin{array}{c|c|c}
\text{权}&\text{空间}&\text{维数}\\ \hline
7&V\mathscr L_3+\operatorname{span}\{x^4BZ\}&4\\
8&V\mathscr L_4&3\\
9&\operatorname{span}\{xV^2,x^4VB\}&2\\
10&\operatorname{span}\{x^2V^2\}&1
\end{array}
\tag{13}
$$
其中
$$
Z=dC+e_-\left(xB+\frac{x^2A}{2}\right),\quad
d=\frac{6\kappa^3}{h_e},\quad
e_-=-\frac{\kappa(15\kappa^2+1)}{4h_e}.
\tag{14}
$$
$\mathscr L_3,\mathscr L_4$ 为 R300 的三个线性 jet 基空间。注意 $e_-\ne0$。

### 3.1 权7的全部零层至多增加一维

权7是 $Z_0$。由(11)，含 $V_1$ 的每项均属于 $V\mathscr L_3$。将其余项在模 V 中整理，准确得到
$$
\boxed{
Z_0\equiv
\frac{q}{2}x^4B
\left[(m+jq)xB+(n+\ell/4)x^2A\right]\pmod{V\mathscr L_3}.
}
\tag{15}
$$
因此新旧合空间都在
$$
V\mathscr L_3+\operatorname{span}\{x^5B^2,x^6AB\}.
\tag{16}
$$
(16)维数为5：模 V 可置 $C=x^2A/4$，后两个剩余单项独立。旧额外方向 $x^4BZ$ 也在该空间，因为
$$
Z\equiv e_-xB+\frac{d+2e_-}{4}x^2A\pmod V.
\tag{17}
$$
故权7至多增加一维，而非把整个六维 $\mathscr H_7$ 全授给零层。

### 3.2 权8至多增加一维，权9、10没有增加

权8是 $Z_1$。所有含 $V_1$ 的项都被 V 整除；只有 $x^2V_0^2/4$ 能给新部分。因此
$$
\boxed{Z_1\equiv\frac{q(j)^2}{4}x^6B^2\pmod{V\mathscr L_4}.}
\tag{18}
$$
所以新旧合空间至多是四维
$V\mathscr L_4+\operatorname{span}\{x^6B^2\}$。

权9的 $Z_2$ 只含 $xV_1^2$ 与 $x^2V_1V_0$；由(7)全在(13)的原二维空间中。权10的 $Z_3=x^2V_1^2/4$ 也在原一维空间中。

综上，完整零/一/二层加旧能量的自由主空间维数至多
$$
40+1+1=42.
\tag{19}
$$
下一节用两条真正原系数证明该上界达到，同时确认它们是 $\mathcal W_e$ 商上的必要观察。

## 4. 两条明确的零层原系数达到这个上界

令 $t=\kappa^2$，并记
$$
r_*^{\,Z}=\frac{d+2e_-}{4e_-}
=\frac{3t+1}{2(15t+1)}\ne0.
\tag{20}
$$
这里的上标 Z 常数与共同右锚 $r_*$ 无关。以下均为有限多项式系数的纸面比较。

### 4.1 权7：$j^5$ 行确实不在旧空间

由(8)，$q$ 最高项 $-j^2/40$；$m+jq$ 最高项 $-j^3/40$，而(9)至多一次。因此由(15)
$$
[j^5]Z_0\equiv\frac1{3200}x^5B^2
\pmod{V\mathscr L_3}.
\tag{21}
$$
模原额外方向 $x^4BZ$，用(17)、(20)又得到
$$
\boxed{
[j^5]Z_0\equiv
-\frac{r_*^{\,Z}}{3200}x^6AB
\pmod{V\mathscr L_3+\operatorname{span}\{x^4BZ\}}.
}
\tag{22}
$$
这个类非零：在模 V 的两维 $(x^5B^2,x^6AB)$ 空间中，旧方向的第一系数是 $e_-\ne0$；单独 $x^6AB$ 不可能是它的倍数。故权7确实增加一维。

### 4.2 权8：$j^0$ 行确实不在旧空间

由(8)、(18)
$$
\boxed{
[j^0]Z_1\equiv
\frac{(3t-2)^2}{1024}x^6B^2
\pmod{V\mathscr L_4}.
}
\tag{23}
$$
在 $0<t<1/100$ 内系数严格非零。$x^6B^2$ 不被 V 整除，故该类非零。它与权7的新方向属不同齐次权，不能相互抵消。

### 4.3 这两行准确杀原 We，而不强迫零层全部系数为零

利用 $\sigma^2=j/\alpha$，定义两个实际 quartic 观察
$$
\boxed{
\mathcal J_7=\alpha[h^0j^6]\mathscr R_{0,\pi/2},
\qquad
\mathcal J_8=\alpha[h^1j^1]\mathscr R_{0,\pi/2}.
}
\tag{24}
$$
其 principal 分别是(21)与(23)对应的
$\sum_i\lambda_i\int (\cdot)(u_i''')^2$。乘 $\alpha$ 只是准确消掉(12)的共同 $1/\alpha$，未改变真实低阶基线。

原 $\mathcal W_e$ 的支持只有
$(n,m)=(1,0),(0,1),(-1,0),(-1,2)$，后两项在同一固定比例中出现。因此(24)两条都对 $\mathcal W_e$ 为零。若完整零层属于原三矩空间，必有
$$
\mathcal J_7=\mathcal J_8=0.
\tag{25}
$$
本稿没有要求 $(1,0)$ 或原三矩空间中的其他合法系数为零，也没有把有限 Taylor 匹配替代整个商。

## 5. 完整偶 germ 的实际 even principal 秩准确为40

(19)、(22)、(23)给自由主空间准确维数42，其逐权维数是
$$
\boxed{1,\ 2,\ 4,\ 5,\ 6,\ 6,\ 6,\ 5,\ 4,\ 2,\ 1.}
\tag{26}
$$
R289/R300 对真实 even 母包、偶 cutoff 和真实平移的普遍核，在这些二次 jet 多项式中恰为无 x 因子的 $uu'$ 与 $u'u''$；二者分别为权3、1，已在旧空间内。新增权7、8不进入这个核，也不增加新的普遍恒等关系。

故
$$
\boxed{
\operatorname{rank}_{\rm actual\ even\ principal}=42-2=40.
}
\tag{27}
$$
该结论可以表述为完整偶 germ 在 $\mathcal W_e$ 商中的主秩：旧一层与二层观察不被 elementary 三矩商改变；新增两行(24)也明确杀该商。因此商后仍达到40，上界仍由整个原平方(10)给出。

这里的实际性采用 R289 的同一个正解析母包见证与有限 Hermite 条件，再用 R293 的 polynomial-path 方法兼取初选有限 $C^2$ 映射的最大秩点。没有用多个不可兼容母形的形式秩拼凑一条实际路径，也没有执行数值秩。

## 6. 两条新观察与旧全部主控制坐标的真实有限联付

沿 R300 从120个一层原行中选定八个 $\mathcal O_1,\ldots,\mathcal O_8$。联合
$$
\left(\mathcal V,\mathcal O_1,\ldots,\mathcal O_8,\mathcal J_7,\mathcal J_8\right)
\tag{28}
$$
共有42个实际条目，其中 $\mathcal V$ 的原两条完整关系保留。它始终取值于
$\mathscr S_{30}\times\mathbb R^{10}$，真实主秩由(27)是40。

从起点采用包含 R299 $\mathcal F^{\rm ang}$ 的有限 $C^2$ polynomial 观察。全部新 symbol 的位置次数仍至多十；R289 每组十二个真实交替包的严格正 Vandermonde 核不变。有限个真实偶 cutoff 的正锥遂覆盖(28)的40维值空间，可加正核使选定幅度全严格正。

对任意预先固定的有限十维新目标，保留整个原低阶基线，先在极限平方幅模型中准确表示目标之差，再选40个独立幅列。R293 原 $N^{-3}$ 振荡与同纤维有限纠正给固定正幅盒上的真实 $C^1$ 收敛；足够大的有限 N 有准确根。五个最后完整 block 按原实际位置分别进行，随后只使用已固定的正四次权。

特别可以同时取得
$$
\boxed{
\mathcal V=0,\quad
\mathcal O_1=\cdots=\mathcal O_8=0,\quad
\mathcal J_7=\mathcal J_8=0.
}
\tag{29}
$$
并保全部二层全角、72面积、三矩、完整第三、六识别能量、正解析 prefactor 和 R299 的全角归约。它没有付(28)以外全部原函数行。

## 7. principal 结清后，剩下的仍是真实低阶相容

对完整零层的任一杀 $\mathcal W_e$ 的准确系数观察，以及一层原120行，可用(28)的40维 principal 基消掉其主平方。余下符号最多是两个无 x 的普遍 even 核；在每个关于自身中心为偶的实际微包上，其积分准确为零。其余线性三阶项按原真实 primitive 分部积分得到 $C^2$ 表达。

于是整个中心偶 germ 的剩余可以准确表为有限组、可能冗余的真实低阶相容量。但本稿不列一个未经编译的总行数或秩，不声称这些值已经为零，也不把“加入有限观察映射”误解为可以任意改变其初始值。

这些余量含真实 self、跨包 Green 和有序 history。下一步须从原式判明其中的完整恒等关系，或在同一实际母包、排列及几何中找到改变真实基线的机制。仅有(27)与(29)不足以得出完整零/一层消去。

R303 一类单包 period self 的几何控制与本稿的 profile principal 控制仍有自己的联合选择问题；本稿不把改变几何期间的路径当作同一固定度量的等距族。整条路径的其他 s 段、奇部、canonical period、同一个二阶 gauge、高阶收敛、嵌入和全时 reach 仍须继续。
