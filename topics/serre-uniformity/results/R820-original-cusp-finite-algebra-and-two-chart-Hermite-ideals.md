# R820：原 cusp 有限代数、双图完整理想与20维准确 Hermite 构造

日期：2026-11-15。状态：**本文为证明与实际输入接口；新秩、关系和Hermite矩阵尚未运行。**
本篇给原 cusp 理想一个直接的有限代数入口，不等待R815的导子矩阵。
它与R814的 $\operatorname{im}[\Gamma,M_g]$ 描述相等；
原一般极理想、$\eta$、主函数刚性化及高度仍须后继实际输入。

## 1. 原基、锚点及不变的准确来源

沿 [R805](R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)
及其[实际结果](R805-certified-original-affine-pencil-free-basis.md)，
在原 $K=\mathbf Q(\zeta)$ 上保留
$$
z=\sigma/\tau,\qquad \tau=e_0,\qquad
\sigma=e_1+e_{73},\qquad
\epsilon=(0,1^{144},2^{127}),
$$
$$
\mathcal R_{\tau,K}=\bigoplus_{a=0}^{271}K[z]\beta_a,\qquad
\beta_a=d_a/\tau^{\epsilon_a},\qquad \beta_0=1 .
\tag{820.1}
$$
本篇只用实际 $n=1$ 的原铅笔，不重选锚点或正规基。
第二图以
$$
v=1/z,\qquad \gamma_a=d_a/\sigma^{\epsilon_a}
=v^{\epsilon_a}\beta_a
\tag{820.2}
$$
为原正规基。此处$v$是第二图底变量；
原 Fourier 的 real-coordinate 参数由源文件定义，不能混为同一符号。

原R786 $\tau$ 行的 $q_Y^0$ 数据已由R813输入carrier保留。
文件 SHA256 为
4a0c8371deaf8e2fb1b94faa626f0eb206d4d1738ddc5e8cfcf461615ffdbdf7，
其40维原$\xi$幂基坐标第0项为 $-9512$，故$\tau$在参考 cusp 非零。
这只是读取已成产物，没有重新计算 Fourier 系数。

原R805的两个S3行又分别是
$$
S_{0,0}=\tau^3,\qquad S_{0,1}=\tau^2\sigma.
$$
源文件与SHA为：

- R805-degree3-S-row-0000.json.gz：
  df7c644e5a6840a9f98981fa3362d6c95432a52aa481225e8e8bceb04282b37a；
- R805-degree3-S-row-0001.json.gz：
  eeaa96fccd028482b09c323b80ace6b0b8affcc3830d4f38e291da56e5ff8084。

第二行的 $q_Y^0$ 原$\xi$坐标第0项是 $-42510635453560$，非零。
所以$\sigma$也在参考 cusp 非零。
[R816](R816-original-all-prime-real-cusp-orbit-and-degree-coprimality.md)
给全部20个原 cusp 的 $K$ 与 $L$ 单轨道，故
$$
(H_\tau\cup H_\sigma)\cap D_{\rm cusp}=\varnothing .
\tag{820.3}
$$
两个原仿射图都包含全部 cusp。

## 2. 先证明所用Q-form，不能把原截面直接称为Q定义

[R806实际原乘法](R806-certified-original-primitive-multiplication.md)
已给
$$
W=M_w\in\operatorname{Mat}_{272}(\mathbf Q[z]),
\qquad w=w_0/\tau,
$$
以及实际非零cyclic行列式：
$e_0,We_0,\ldots,W^{271}e_0$在$K(z)$上成基。
这些列的矩阵在$\mathbf Q(z)$中，故也在$\mathbf Q(z)$上成基。

令
$$
F_0=\mathbf Q(z)[w]\subset K(Y).
\tag{820.4}
$$
原$w$在$K(Y)/K(z)$中次数为272。
其由$W$给出的次数272多项式已在$\mathbf Q(z)[X]$中，
在$K(z)$上不可约，从而在$\mathbf Q(z)$上亦不可约。
因此$F_0$是次数272的域，且
$$
F_0=\bigoplus_{a=0}^{271}\mathbf Q(z)\beta_a .
\tag{820.5}
$$
这里cyclic矩阵在$\mathbf Q(z)$上可逆只用于证明存在；
本篇不形成那个大逆。

定义
$$
\mathcal R_{\tau,0}
=\bigoplus_a\mathbf Q[z]\beta_a .
\tag{820.6}
$$
它是一个环：任意$\beta_a\beta_b$的坐标一方面在$\mathbf Q(z)$，
另一方面由原正规环(820.1)在$K[z]$，
而
$$
\mathbf Q(z)\cap K[z]=\mathbf Q[z].
$$
它含1，且
$$
K\otimes_{\mathbf Q}\mathcal R_{\tau,0}
=\mathcal R_{\tau,K}.
\tag{820.7}
$$
正规性同样由忠实标量扩张或整元素测试下降。
第二图的同一论证给
$\mathcal R_{\sigma,0}=\bigoplus_a\mathbf Q[v]\gamma_a$，
其$K$扩张是原第二图正规环。

这是从原已认证$W$与cyclic基得到的Q-form。
**不声称**原扭曲曲线 $Y/\mathbf Q$ 上每个选中M2截面已Q定义，
也不把原 $u=24s(2t-1)$ 的K识别删掉。
后面所有Q系数理想经(820.7)及原基运输，
才是原扭曲曲线上的理想。

## 3. 从旧273个S3常数项得到原有限代数

置
$$
F=\mathbf Q(\xi_{41}+\xi_{41}^{-1}),\qquad [F:\mathbf Q]=20 .
$$
记$\chi=\xi_{41}+\xi_{41}^{-1}$。
可用原实坐标的固定多项式
$$
C_0(X)=2,\quad C_1(X)=X,\quad
C_{j+1}(X)=XC_j(X)-C_{j-1}(X),
$$
$$
P(X)=1+\sum_{j=1}^{20}C_j(X)
\tag{820.8}
$$
表示$F=\mathbf Q[X]/(P)$。
这正是原R805 real-coordinate接口的20维基，
不是一个新选的共轭或数值根。

原S3行次序为
$$
i(0)=0,\qquad
i(a)=4+3(a-1)\quad(1\le a\le144),
$$
$$
i(a)=436+2(a-145)\quad(145\le a\le271).
\tag{820.9}
$$
第$i(a)$行正是$S_{a,0}=\tau^{3-\epsilon_a}d_a$。
再读取第1行$S_{0,1}$，合计273个已有行。

令$N_a\in F$为第$i(a)$行
integer_v_t_coefficients[0]给出的原20维整数多项式值，
$N_z$为第1行的相同值。
所有这些S3行的原integer_scale都是$82^6$，
且原40维$\xi$与20维real坐标已经逐项认证。
在常数项，原逐阶phase指数为0；
也可直接在同权6的截面比中消去共同局部平凡化。

于是准确有
$$
e_a=\beta_a(c)=N_a/N_0,\qquad
\alpha=z(c)=N_z/N_0 .
\tag{820.10}
$$
原共同$82^6$准确相消。
不重新生成$\tau^3$，不额外乘$82^2$，
不求新的torsion、Fourier尾或局部参数单位。
由(820.3)，$N_0,N_z,\alpha$均非零。

因此每个$e_a$和$\alpha$确实落在$F$中；
这是原real-coordinate与同一$\tau^3$比值给出的证明。
不能仅由原尖点域是$KF$就断言这些选定坐标在$F$。

## 4. 完整评价映射与必须实际检验的20维可达性

由(820.10)得到环同态
$$
\mathrm{ev}_\tau:\mathcal R_{\tau,0}\longrightarrow F,
\qquad
\sum_a f_a(z)\beta_a\longmapsto
\sum_a f_a(\alpha)e_a .
\tag{820.11}
$$
其乘法相容性来自原$K$上的尖点评价及$F\hookrightarrow KF$。

R816给原$Y_K$的全部 cusp 是一个次数20闭点，剩余域恰为$KF$。
它位于$U_\tau$，故原仿射环到这个剩余域的评价满射。
因为$K$为虚二次而$F$全实，
$$
K\otimes_{\mathbf Q}F=KF .
$$
结合(820.7)，(820.11)的像$V\subset F$满足
$K\otimes_{\mathbf Q}V=KF$，故
$$
V=F,\qquad
\dim_{\mathbf Q}\mathcal R_{\tau,0}/\ker\mathrm{ev}_\tau=20.
\tag{820.12}
$$

在固定$1,\chi,\ldots,\chi^{19}$基下，
令$E$为列$e_a$组成的$20\times272$准确Q矩阵，
$Z$为乘$\alpha$的$20\times20$矩阵。
则所需可达空间为
$$
\operatorname{span}_{\mathbf Q}\{Z^j e_a:a=0,\ldots,271,\ j\ge0\}=F .
\tag{820.13}
$$
**不预设常数矩阵$E$的秩等于20**，
也不预设$\alpha$在$F/\mathbf Q$中primitive。
实现必须生成实际独立向量与非零准确20阶minor，
并逐个认证所用关系。
若实际输入不满足rank20，则任务失败或记录真实不足，
不能强写为理论预期值。

扩标量后，(820.11)的核正是原约化cusp理想：
$$
K\otimes\ker\mathrm{ev}_\tau=\mathcal C_\tau.
\tag{820.14}
$$
它不是只有正确支撑但未除重数的理想：
有限剩余域是可分的域，核为约化闭点的最大理想。

## 5. 不需要大的多项式kernel：逆序Krylov链

下面给完整、可断点的准确Q算法。
按原基索引
$$
a=271,270,\ldots,0
$$
依次处理，始终保留一组已认证独立向量
$$
\mathcal B=\{\alpha^k e_b:\ b>a,\ 0\le k<d_b\}
\tag{820.15}
$$
及其准确Q-echelons。
其张成空间$S$由先前步骤保证在$Z$下稳定。

对当前$a$，从$e_a$开始顺次检测
$$
e_a,\ \alpha e_a,\ \alpha^2e_a,\ldots
$$
相对已有独立向量的线性相关。
若$\alpha^k e_a$独立，则加入$\mathcal B$。
第一次相关时令$d_a=k$，并保存准确关系
$$
\alpha^{d_a}e_a=
\sum_{\substack{b>a\\0\le j<d_b}}c_{b,j}\alpha^j e_b
+\sum_{0\le j<d_a}c_{a,j}\alpha^j e_a .
\tag{820.16}
$$
右侧仅有已经入选的向量，系数由实际准确消元确定。

新的张成空间仍在$Z$下稳定：
高索引块已经稳定；当前链的前项乘$Z$到下一项，
最后一项由(820.16)返回新空间。
所以可以继续处理$a-1$。

全程至多20次独立扩维，
每个$a$恰有一次首次相关检测；
因此至多292个候选向量。
每次独立后才计算下一次$Z$乘向量，
故建立这些链最多20次该类乘法。
这是维数给出的最坏次数界，不是本次实际$d_a$统计。

最终(820.13)要求
$$
|\mathcal B|=\sum_a d_a=20 .
\tag{820.17}
$$
实际20个入选向量的独立性必须有准确证书；
原输入和源字段不由任何预期rank代替。

## 6. 这些关系已经是完整canonical列Hermite基

把(820.16)提升为$\mathbf Q[z]^{272}$中的列
$$
H_a=z^{d_a}\mathbf e_a
-\sum_{\substack{b\ge a\\0\le j<d_b}}
c_{b,j}z^j\mathbf e_b,
\tag{820.18}
$$
其中对$b=a$的和只有$j<d_a$。
这里$\mathbf e_a$是原正规坐标单位列；
不要与尖点评价值$e_a$混淆。

令$H=(H_0,\ldots,H_{271})$。
它是下三角矩阵，主对角monic，
行$b>a$的非对角条目次数严格小于$d_b$。
因此它就是固定原基次序的canonical列Hermite形式。
对$d_a=0$，对角是1；不能把该列错误删除。

每一列都由实际关系(820.16)评价为零，所以
$$
H\,\mathbf Q[z]^{272}\subset\ker\mathrm{ev}_\tau .
\tag{820.19}
$$
另一方面，
$$
\deg\det H=\sum_a d_a=20,
$$
故左侧的商Q维数为20。
(820.12)给右侧商维数也为20，
于是
$$
\boxed{H\,\mathbf Q[z]^{272}=\ker\mathrm{ev}_\tau.}
\tag{820.20}
$$
这认证完整kernel，没有只给一个子理想、包含或相同的零集合。

也可由三角关系直接得到标准余项：
$\{z^j\mathbf e_a:0\le j<d_a\}$是一组20维商基，
其评价恰为实际独立$\mathcal B$。
因此约化性、剩余域以及完整原重数一并被认证，
无需分解闭点、数值识别根或大特征零Krylov逆。

固定monic首项以外的系数位置数至多
$$
\sum_{b=0}^{271}(b+1)d_b\le272\cdot20=5440.
\tag{820.21}
$$
保存这些短项足够重建完整272阶理想基。

## 7. 第二图由同一有限代数准确运输

由(820.2)、(820.10)，第二图的评价准确为
$$
v(c)=\alpha^{-1},\qquad
\gamma_a(c)=\alpha^{-\epsilon_a}e_a .
\tag{820.22}
$$
只需原$N_z$非零与一次准确字段求逆。
用乘$\alpha^{-1}$的20阶矩阵和这些272个值，
重复第5节的同一个有限算法，
即给完整$\mathcal C_\sigma$的canonical列Hermite基。
不产生新的Fourier系数，也不独立选择一个cusp共轭。

两图的有限代数识别是同一个$F$中的恒等映射，
并保
$$
\alpha\alpha^{-1}=1,\qquad
\gamma_a(c)=\alpha^{-\epsilon_a}\beta_a(c).
\tag{820.23}
$$
因此两kernel在重叠上相容：
同函数正规基运输仍为
$$
f_\sigma(v)=\operatorname{diag}(v^{-\epsilon_a})f_\tau(1/v).
$$
在$c$处代入$v=\alpha^{-1}$后，
对应同一有限代数值，故一个表达在某图属于kernel
当且仅当其重叠运输在另一图属于kernel。
不必为这个已由同一闭点评价认证的理想再做272阶Laurent解算。

## 8. 需要保存的实际证书与断点

首次实际scope只输出这两个cusp理想。证书至少包括：

1. 原R805/R806 producer身份、free basis、S3 index，
   273行逐bytes/SHA与原常数项字段，原共同$82^6$；
2. 固定实字段定义、$N_0,N_z$非零、
   字段求逆的完整乘回和原比例(820.10)；
3. 两图$20\times272$评价坐标、
   乘$\alpha$／$\alpha^{-1}$的准确20阶矩阵及完整原字段乘回；
4. 每条Krylov链的原索引、当前幂次、
   独立pivot或第一次相关关系，
   以及原选定向量的完整20坐标代回；
5. 两个实际rank20、各20阶非零minor、真实$d_a$，
   完整下三角monic/remainder条件与总度20；
6. 每列关系的准确有限代数评价为零，
   完整kernel的长度证书以及(820.23)的双图字段识别。

原基元索引、相位、原$\tau,\sigma$常数及字段共轭都保持。
大producer前缀不重算；预算续接只恢复同核/同源的完整阶段与当前短echelon状态。
不得把理论界20、实际常数$E$的某个猜测rank或理论满射性写成已运行的证书。

这些新算术仅在本公开仓库Actions。
本文自身未执行它们。原stage引用可通过已成R813的活跃输入bundle传递，
仍以原R805/R806身份逐SHA认证，不把carrier改名为数学producer。

## 9. 接回原R814消费者

R814已经识别
$$
\mathcal C_\tau=\operatorname{im}_{k[z]}[\Gamma,M_g]
$$
及第二图的同一个约化cusp理想。
所以本篇实际完成后可以直接供应该$\mathcal C$，
免去在大$\Gamma,M_g$表上再做一次完整image消元。
它也给该像的独立长度20校验。

对一般原极理想$I$，
$$
N(I)=I+\delta I,\qquad
\operatorname{Peel}(I)=(N(I):_{\mathcal R}\mathcal C)
$$
仍需真实$\Gamma,M_g$与完整$I$。
本篇不替代这些输入，不输出$\sqrt I$、原尾部Bézout、
$\eta$代表、主函数或高度。
它只把一个已证明必需的cusp理想变成可直接、有限且很小的准确任务。

依据（2026）：R805、R806、R813的原已成输入接口；
R814的原导子零理想与整理想商；R816的原cusp域与单轨道；
R817的同一Q正规坐标/原primitive输入。
