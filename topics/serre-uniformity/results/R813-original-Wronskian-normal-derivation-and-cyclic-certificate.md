# R813：两个原 S3 Wronskian 与正规整基上的唯一有界导子

日期：2026-11-15。状态：**本篇证明两个准确低权输入及其完整导子恢复接口；尚未运行新的 Wronskian 坐标、乘法矩阵或导子矩阵。** 首次工程只计算下文两个690维有理右端，全部820行准确回代；后续矩阵的存在及认证算法不写成已经算出的结果。

本篇接 [R803](R803-original-single-map-reuse-and-mixed-Hodge-ratios.md) 的原微分规范、
[R805](R805-original-two-affine-charts-and-small-polar-divisor-adapter.md) 的真实正规整基、
R806 的实际 primitive 乘法接口、[R809](R809-original-normal-vectors-for-function-and-Hodge-inputs.md) 的有界交换子引理，
以及 [R811](R811-original-normal-polar-ideal-preimages-and-two-chart-certificates.md) 的原两图与函数规范。
保持同一 $Y/K$、$K=\mathbb Q(\zeta)$、$L=K(b)$、原 $C:y^2=x^3+b$、$c_0,c_1,\rho,\kappa$。

## 1. 原线丛与准确微分尺度

令 $\mathcal D$ 为二十个 cusp，原
$$
\mathcal H=K_Y+\mathcal D,\qquad \deg\mathcal H=272,\qquad
V_r=H^0(Y,r\mathcal H),\qquad \dim V_3=690.
\tag{813.1}
$$
原整数 M2 基为 $e_i=82^2T_{1,i}$。
读取成功 R805 的实际无基点铅笔
$$
\tau=e_0,\quad \sigma=e_1+n e_{73},\quad
z=\sigma/\tau,\quad H=\operatorname{div}\tau.
\tag{813.2}
$$
$n$ 来自真实 producer。读取成功 R806 的实际
$$
w=w_0/\tau,\qquad w_0=\sum_{i=0}^{145}c_i e_i,\quad c_i\in\mathbb Z,
\tag{813.3}
$$
以及原正规基 $\beta_a=d_a/\tau^{\epsilon_a}$ 和准确 $M_w$：
$$
\epsilon=(0,1^{144},2^{127}),\qquad \beta_0=1.
\tag{813.4}
$$
R806 尚未返回时，不预填 $w_0$、候选号或实际非零 minor。

沿 R803(803.20) 固定
$$
D_0=(2\pi i)^{-1}\frac d{d\tau_{\rm an}}
=\frac{q_Y}{82}\frac d{dq_Y}.
\tag{813.5}
$$
这里 $\tau_{\rm an}$ 是上半平面变量，不是(813.2)的截面。
R205 §1–2 的 Tate 规范给
$$
\nabla_{2r}=D_0-\frac r6 E_2.
\tag{813.6}
$$
以下同权组合中的 $E_2$ 完全相消；不需要新增它的长展开。

将 $\tau$ 视为原对数微分截面，定义其对偶有理导子
$$
\boxed{\ \delta=\tau^{-1}D_0.\ }
\tag{813.7}
$$
它在 $U_\tau=Y\setminus H$ 正则，并在 $K$ 上线性。
它是一个固定的非零有理向量场；不宣称它在整个 $Y$ 上无极点。

## 2. 广义 Wronskian 自动属于普通截面空间

对 $s\in V_1$ 置
$$
W(\tau,s)=\tau D_0s-sD_0\tau
=\tau\nabla_2s-s\nabla_2\tau.
\tag{813.8}
$$

**定理813.1。** 有
$$
W(\tau,s)\in H^0(3\mathcal H-\mathcal D)\subset V_3.
\tag{813.9}
$$
更一般地，对 $d\in V_r$，
$$
W_r(\tau,d):=\tau D_0d-rdD_0\tau
=\tau\nabla_{2r}d-rd\nabla_2\tau
\in H^0((r+2)\mathcal H-\mathcal D).
\tag{813.10}
$$

**证明。** 在粗曲线的线丛局部框架中，$d/\tau^r$ 是有理函数。
乘以 $\tau^{r+1}$ 后的微分
$\tau^{r+1}d(d/\tau^r)$ 是
$\mathcal H^{r+1}\otimes K_Y$ 的全局截面：
局部框架求导的额外项在
$\tau\,d(d)-r\,d\,d(\tau)$ 中相消。
由 $K_Y=\mathcal H-\mathcal D$，这就是(813.10)的线丛。
用原 Tate 框架校准，该截面的模形式系数正是(813.10)，尺度为(813.5)。

也可逐原特殊点检查。$Y$ 的两个内部椭圆点只有阶三有效稳定子。
取 stack 参数 $a$、粗参数 $u=a^3$，写
$$
\tau=a^2T(u),\qquad d=a^{2r}F(u).
$$
对 $a$ 求导后的加权差为
$$
\tau\,\frac{dd}{da}-r\,d\,\frac{d\tau}{da}
=3a^{2r+4}\bigl(TF'-rFT'\bigr).
\tag{813.11}
$$
原 KS/Tate 规范的局部单位不改变消失阶；
$a^{2r+4}$ 恰是普通 $(r+2)\mathcal H$ 的粗模框架。
所以没有遗留椭圆点极点。在 cusp，$D_0$ 含 $q_Y$ 因子，
两个全纯 Fourier 展开的加权差常数项为零，额外至少消失一次。
这给(813.10)中的 $-\mathcal D$。$r=1$ 即(813.9)。
$r=0,d=1$ 时分子恒零。$\square$

因此本篇只需两个普通 $V_3$ 截面
$$
G=W(\tau,\sigma),\qquad J=W(\tau,w_0).
\tag{813.12}
$$
这里 $J$ 是第二个 Wronskian 的名称，不是 Jacobian。
无需改变原普通 S3 基或引入高阶模形式补行。

## 3. 两个有理右端、41阶与真实原尺度

原 R805/R806 的同一 S3 基是
$$
\mathcal S_3=
\{\tau^{3-\epsilon_a-j}\sigma^j d_a:
0\le a<272,\ 0\le j\le3-\epsilon_a\},
\tag{813.13}
$$
按 $a$ 外层、$j$ 内层排列，维数
$4+144\cdot3+127\cdot2=690$。
它与 R786 的普通 V3 行基属于同一空间，但不是同一坐标基；
本篇准确复用(813.13)的实际矩阵、选行与有限域逆。

完整原 $q_Y^0,\ldots,q_Y^{40}$ 给820个有理实圆分坐标。
若一个 $V_3$ 截面这些坐标全零，原二十 cusp 单轨道给至少820个零，
而 $\deg(3\mathcal H)=816$，故该截面为零。
因此同一 $820\times690$ 块的完整回代认证(813.12)的全球身份。

若
$\tau=\sum_i t_iq_Y^i$、$s=\sum_j s_jq_Y^j$，则对 $0\le m\le40$，
$$
[ q_Y^m ]W(\tau,s)
=\frac1{82}\sum_{i+j=m}(j-i)t_i s_j.
\tag{813.14}
$$
只读取旧 M2 的这41项。原 $q_Y,\xi$ 相位及
$v=\xi^{-10}q_Y$ 的实圆分表示保持不变；乘以有理整数 $j-i$、
原有理数 $1/82$ 与原系数域乘法都保持这批固定的实坐标。
因此两个右端和 S3 矩阵均在 $\mathbb Q$，唯一 S3 坐标也在 $\mathbb Q$。

实际执行进一步复用
$$
W(\tau,s)=D_0(\tau s)-2sD_0\tau.
\tag{813.15}
$$
原 R805 alias/原 R786 recipe 已逐项给出
$\tau e_i=$ 原 V2 第 $i$ 行，$0\le i<146$；
消费时仍须核这些原 recipe 与 SHA。
所以 $\tau\sigma$ 和 $\tau w_0$ 都只需合成已成 V2 行，
每个新右端只新增一个加权 formal product $s\cdot(q_Y\,d\tau/dq_Y)$。
这个加权乘积单独不被宣称为模形式；
只有(813.15)的完整差由定理813.1属于 $V_3$。

尺度始终为：
$\tau,\sigma,w_0$ 各自带原 $82^2$，
旧 $\tau e_i$ 带 $82^4$，
S3 基带 $82^6$。
在整系数形式中先形成
$m(\tau s)_m-2\sum_{i+j=m}i\,t_i s_j$，
再恢复准确比例 $1/82$。
不能再乘一个 $82^2$ 使右端看似与基同尺度。
若写 $\tau=82^2\tau_0,s=82^2s_0$，
Wronskian 本身是 $82^4W(\tau_0,s_0)$；
相对于 $82^6$ 的 S3 原基，真实相对比例 $82^{-2}$ 仍在坐标中。
清分母或去整数 content 仅作为计算步骤，最终原有理比例完整恢复。

## 4. 两个 normal 向量给原导子在 z、w 上的值

置
$$
g=G/\tau^3,\qquad h=J/\tau^3.
\tag{813.16}
$$
由(813.7)、商法则，
$$
\boxed{\delta z=g,\qquad\delta w=h.}
\tag{813.17}
$$
二者均在 $H^0(3H)/\tau^3$；其 normal 向量 $v_g,v_h$ 的分量满足
$$
\deg(v_g)_a,\deg(v_h)_a\le3-\epsilon_a.
\tag{813.18}
$$
读(813.13)的 S3 坐标，按原 $(a,j)$ 直接写成 $z^j$ 即得，
没有新的域逆、模型或标量选择。

原 $z$ 非恒定且特征零，故非零导子 $\delta$ 满足 $g\ne0$。
后继实际输出仍须检查准确向量而非抄录这个预期。
$g$ 在某些点为零完全允许；下面矩阵算法只要求原 Krylov 特化可逆，
不要求每个计算点的 $g$ 为单位。

## 5. 原整基导数矩阵的次数与唯一性

定义 $\Gamma$ 的第 $a$ 列为 $\delta\beta_a$ 的原 normal 坐标。
由(813.10)，
$$
\delta\beta_a
=\frac{\tau D_0d_a-\epsilon_a d_aD_0\tau}
       {\tau^{\epsilon_a+2}}
\in H^0((\epsilon_a+2)H)/\tau^{\epsilon_a+2}.
\tag{813.19}
$$
故
$$
\boxed{\Gamma_{ba}\in K[z],\qquad
\deg\Gamma_{ba}\le2+\epsilon_a-\epsilon_b,\qquad\Gamma e_0=0.}
\tag{813.20}
$$
最高次数为4。负上界仍表示该项必须为零。

令 $M_g,M_h$ 为(813.16)的真实 normal 乘法矩阵；
撇号只对矩阵条目的 $z$ 多项式求导。
对任意 normal 向量 $v_f$，
$$
v_{\delta f}=\Gamma v_f+M_gv_f'.
\tag{813.21}
$$
将 $\delta(wf)=hf+w\delta f$ 逐项展开，得到
$$
\boxed{\Gamma M_w-M_w\Gamma=M_h-M_gM_w'.}
\tag{813.22}
$$
$M_g$ 在 $M_w'$ 左侧，不能交换成未经证明的次序。

**定理813.2（唯一有界导子认证）。**
在原 $e_0$ 对 $M_w$ cyclic 的条件下，
任何满足(813.20)及完整准确(813.22)的候选矩阵，
都等于原 $\delta$ 的真实矩阵 $\Gamma$。

**证明。** 真实几何导子已由(813.7)、定理813.1构造，故有一个解。
两个解的差 $C$ 满足 $Ce_0=0$、$CM_w=M_wC$，
于是消掉全部 $M_w^je_0$；这些向量是 $K(z)^{272}$ 的基，
故 $C=0$。$\square$

$M_w$ 及两个准确右端坐标都在 $\mathbb Q$。
由 R809 的同一 cyclic 唯一性，$M_g,M_h$ 的全部系数在 $\mathbb Q$；
(813.20)–(813.22)是一个有限的有理系数线性系统，
其唯一解也在 $\mathbb Q$。
这里说的是固定原整基下的矩阵系数；
不把原 $K$ 曲线或每个原截面另宣称为 $\mathbb Q$ 定义。

## 6. 只有有限域数值 Krylov 逆的恢复公式

在一个实际好素数与好特化 $z=t$，
写 $W=M_w(t)$、$W'=M_w'(t)$，
令
$$
k_0=e_0,\quad \ell_0=0,\qquad
k_{j+1}=Wk_j,\quad
\ell_{j+1}=W'k_j+W\ell_j.
\tag{813.23}
$$
则 $k_j=M_w^je_0$、$\ell_j=(M_w^je_0)'$ 的特化值。
记 $\mathcal K=[k_0,\ldots,k_{271}]$，只在实际非零 determinant 时求其有限域逆。
由 $\delta(w^j)=j w^{j-1}h$，
$$
\Gamma(t)\mathcal K=
\left[
0,\ 
v_h-M_g(t)\ell_1,\ 
2Wv_h-M_g(t)\ell_2,\ \ldots,\
271W^{270}v_h-M_g(t)\ell_{271}
\right].
\tag{813.24}
$$
所以右侧乘 $\mathcal K^{-1}$ 就给 $\Gamma(t)$。
$j=0$ 一栏直接取零；公式没有求 $W^{-1}$。

完整原矩阵次数与终验点数分别为：

| 对象 | 逐项次数界 | 最高次数 | 插值所需好点 | 终验恒等式最高次数 | 准确终验点数 |
|---|---|---:|---:|---:|---:|
| $M_g,M_h$ | $3+\epsilon_a-\epsilon_b$ | 5 | 6 | 各自与 $M_w$ 的交换子至多6 | 7 |
| $\Gamma$ | $2+\epsilon_a-\epsilon_b$ | 4 | 5 | (813.22)的残差至多5 | 6 |

第一行的7点用于准确证明两个乘法矩阵本身；
不能把6个插值点当作它们全部交换子终验点。
第二行则因
$$
\deg(\Gamma M_w-M_w\Gamma-M_h+M_gM_w')_{ba}
\le3+\epsilon_a-\epsilon_b\le5
\tag{813.25}
$$
而使用全部6个互异有理点即可。
两行的第一列条件均逐系数检查。
准确终验点只评多项式矩阵，无需满足 Krylov 好点条件。

插值逐实际好素数进行，CRT和有理重构使用统一严格矩形界 $2AB<M$。
最终通过这些完整准确身份以后，唯一性才给真实矩阵。
全过程不形成特征零 $\mathcal K(z)$ 或其逆。
若旧消费者已有同一 $M_w$、同一 prime/$t$ 的原有限域逆，
按源SHA直接复用，不重算已成小块。

## 7. 所有14个 L 分量及原 Galois 运输共用一个导子

将 $\delta$ 以对 $L$ 常数为零的方式扩张。
对原 $b^i,sb^i$ 基（$s=1+2\zeta$），(813.21)逐14个有理分量同时适用，
不是另构造14个导子。$\delta$ 在原 $K$ 上定义，故与
$\operatorname{Gal}(L/K)$ 的系数运输相容；
原 $\rho_j$ 也是常数，导数不额外产生 $\delta\rho_j$ 项。

若原 R809 已给 $a=A/\tau^5,b_0=B/\tau^5$ 的真实 normal 向量，
且 R811 已给 $M_a,M_{b_0}$，则先准确形成
$$
v_{\delta a}=\Gamma v_a+M_gv_a',\qquad
v_{\delta b_0}=\Gamma v_{b_0}+M_gv_{b_0}'.
$$
原 $y_f=a/b_0$ 的导数作为完整 pair 为
$$
\boxed{
\delta y_f=
\frac{\,b_0\delta a-a\delta b_0\,}{b_0^2},\quad
v_{\rm numerator}=M_{b_0}v_{\delta a}-M_av_{\delta b_0},\quad
v_{\rm denominator}=M_{b_0}v_{b_0}.}
\tag{813.26}
$$
此处 $b_0$ 仍是函数分母，不是椭圆参数 $b$。
原同靶 $Y_j=\rho_j^{-3}\sigma^j(y_f)$ 的导数准确为
$\rho_j^{-3}\sigma^j(\delta y_f)$；
要运输完整 $L$ 系数与原模型数据，不能只改函数名称。

在 R803(803.19)的比值中，
$dy_f/dY_j=\delta y_f/\delta Y_j$。
同一个非零导子公因子相消；
它在孤立点的零或极不允许改用未约分分母的零点集合替代原函数。
因此原 R804 八节点全局 DAG 的微分比有了一个有限、低度且保原规范的输入算法。
得到该算法仍不等于五个原函数或极理想已经执行完成。

## 8. 第二张图的导子是函数运输，并可在 H 上有极点

令 $t=1/z$，
$\beta'_a=d_a/\sigma^{\epsilon_a}$，
$D(t)=\operatorname{diag}(t^{-\epsilon_a})$，
$E_\epsilon=\operatorname{diag}(\epsilon_a)$。
先运输相同函数 $g$ 的矩阵：
$$
M_g^\sigma(t)=D(t)M_g(1/t)D(t)^{-1}.
\tag{813.27}
$$
这是同一个 $g$，不附加截面正规化的公共 $t^3$。
如果读取的是 $G/\sigma^3$ 的正规矩阵，应先除以 $t^3$。

由于 $\delta t=-t^2g$ 与 $\beta'_a=t^{\epsilon_a}\beta_a$，
同一个 $\delta$ 的第二图公式是
$$
\boxed{
M_{\delta t}^{\sigma}=-t^2M_g^\sigma,\qquad
\Gamma^\sigma=D\Gamma(1/t)D^{-1}-tM_g^\sigma E_\epsilon.}
\tag{813.28}
$$
于是
$$
v_{\delta f}^{\sigma}
=\Gamma^\sigma v_f^\sigma
+M_{\delta t}^{\sigma}\frac{dv_f^\sigma}{dt}.
\tag{813.29}
$$
修正项是矩阵乘积 $-tM_g^\sigma E_\epsilon$。
一般的 $g\in K(Y)$ 不属于 $K(z)$，故不能写成一个标量对角阵。

(813.28)可含 $t=0$ 的 Laurent 极，
这正记录原对偶 $\tau$ 的导子在 $H$ 处可能有极点。
若改用第二张图自身的对偶导子 $D_0/\sigma=t\delta$，
必须显式保留这个公因子 $t$；不能在两个图中把不同导子无标记混用。
同一导数比在共同更换导子后保持原值。

## 9. 首次实际计算的边界

首次只输出实际 $G,J$ 的两份 S3 坐标及 $v_g,v_h$，
完整来源、原 $1/82$ 与 $82$ 尺度、同一690块和全部820行回代。
它只依赖真实 R805、R806、R786；不要求尚未完成的原 A/B。

$M_g,M_h,\Gamma$ 的插值、准确身份、(813.26)、原八节点函数、
两图极理想、三重数提取、Jacobian flip、原 $c_0$ 刚性化、$\eta$ 与高度，
均按其各自实际阶段继续。
本篇不从存在性或静态代码审阅预填任一数值矩阵。

所有新算术只在本公开仓库 Actions。
可重算大数据仅供一日活跃产物续传；Git/Release只保存证明、脚本、
参数、run与SHA，不保存完整坐标、矩阵或原证书。

来源：R803(803.20)的准确 $D_0$、同权 Wronskian 与原模型；
R205 §§1–2的 Tate Serre 规范及 stack/粗模检查；
R805/R806的原 S3、分次自由整基与真实 cyclic 证书；
R809的有界乘法认证；R811的原两图、尺度及完整函数pair边界。
