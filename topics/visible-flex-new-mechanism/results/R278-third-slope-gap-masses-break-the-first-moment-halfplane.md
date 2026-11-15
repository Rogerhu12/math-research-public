# R278：第三斜率的真实 gap 质量打破第一外矩的共同半平面

日期：2026-11-15。**完整纸面构造与准确响应公式；未执行 profile 求积、参数扫描、符号计算程序、人工检查或研究计算。**

[R275](R275-first-moment-obstruction-for-the-small-width-two-slope-family.md) 已证明，原双斜率、小母宽、两种排序及正幅混合不能同时支付指定的两个面积矩。本稿改变的是实际圆的平方质量：增加第三种平方斜率 $a_i^2/b_i^2=1$，把有限个真实正宽微包放入原 cell 间的空隙。它们在 $\theta=\pi/2$ 不改变 $f''{}^2-g''{}^2$，却改变外槽 $g''{}^2$。原有序积分因此产生 R275 族内没有的严格负响应。

新增微包也会改变局部四次矩，不能只写一个负方向。本稿以五个 gap 簇的严格正权匹配中心的零、二、四次矩，把这笔代价同时纳入。所得有限正宽圆保留三矩、完整第三、六能量、整个 $A_{-2,-3}$、整个 $A_{-1,-3}$、整个 $A_{1,-1}$ 第零外矩、整个 $A_{-1,-2}$ 第零外矩及全部 Gaussian odd 条件；还能保留 pure $\mathscr Q$ 的正、负分支。

本稿不宣称全部面积通过。尤其新负响应还与 $A_{1,-3}$ 第一外矩联动，$A_{-1,-2}$ 第一外矩的另一个 even 系数仍保留真实母形余项。最后两节给出这些准确账目。

来源：[R250 全角局部矩](R250-complete-circle-Gaussian-area-and-nonuniform-profile-cancellation.md)、[R256 联合能量与一般微包归约](R256-sharp-profile-energy-contrast-and-multiwidth-joint-construction.md)、[R257 原累计量](R257-cumulative-primitive-energy-in-the-complete-positive-negative-Gaussian-area.md)、[R259 完整 self/cross 表](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R267 母形条件](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、[R269 真实 cell 次序](R269-reordered-real-masses-pay-a-complete-Gaussian-zero-moment.md)、[R270 四变量 IFT](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)及 [R273 第零外矩](R273-reflection-densities-pay-the-minus-one-minus-two-zero-moment.md)。

## 1. 保留的原量及结论的精确方向

保持同一右锚
$JF(x)=\int_x^{r_*}F(t)\,dt$。记

$$
P=\Phi_{r_0},\quad Y=\Phi_{p_2},\quad
B_{-1}=d\Phi_{p_0}+e\Phi_{s_1},\quad
B_{-2}=a_G\Phi_{r_1}+b_G\Phi_{s_0}.
$$

用 $a_G,b_G$ 区分 Gaussian 系数与微包幅度。原共振参数是
$\varepsilon=\kappa^2/4$，实际 $\kappa\ne0$ 足够小。令

$$
k=\frac{db_G}{2}-ea_G
=-\frac{\kappa(1173\kappa^6+177\kappa^4+122\kappa^2+8)}
 {256h_e^3}\ne0.
\tag{1}
$$

对真实圆 $\phi_\theta=f\cos\theta+g\sin\theta$、
$D_\theta=f\odot f-\phi_\theta\odot\phi_\theta$，本稿特别跟踪

$$
S=2I_0\{g,[P,Y](g;f\odot f-g\odot g)\},
$$

$$
Z=2I_1\{g,[B_{-1},B_{-2}](g;f\odot f-g\odot g)\}.
\tag{2}
$$

它们是各完整角函数的 $\sin^4\theta$ 系数。原 Gaussian 方向只再乘已经明确的非零系数。这里不把 $S,Z$ 两个 scalar 当成两个完整面积。

取 R270 的同源 even 母包 $u$，包括真实中央幅/宽及左右镜像的奇扰动；固定小正母宽 $h$ 后，它有严格正有限宽度。用

$$
\eta_{w,\xi}(x)=w^{3/2}u((x-\xi)/w),\qquad
m=\int(u'')^2,\quad C=\int(u'')^4,
$$

$$
\nu=\frac{\int(y^2(u'')^2+2(u')^2)}m,\qquad
N_0(u)=\int u'(u'')^3=0.
\tag{3}
$$

先缩小母宽的统一邻域，使 $\operatorname{supp}u\subset(-1,1)$。所有未标物理位置的 $t,w$ 都是 shape 坐标；实际坐标是

$$
x=\xi_0+\delta t,\qquad w_{\rm physical}=\delta w,\qquad \delta>0.
\tag{4}
$$

最后各 block 在其最终正位置 $\xi_0$ 先完成真实 IFT，不在解完后任意搬动一个能量根。

本稿将构造普通和伴随两类完整 block，满足

$$
S>0,\qquad Z/k<0,\qquad
\operatorname{Re}\mathscr Q_-<0<\operatorname{Re}\mathscr Q_+ .
\tag{5}
$$

在全部 odd 包装后 $\mathscr Q$ 为实。正四次幅度混合两类可另付 $\mathscr Q=0$，同时保 $S>0>Z/k$。这与 R275 的共同半平面相反，但仍没有令 $S=0$。

## 2. 新的三斜率及准确四次预算

原
$\beta(\alpha)=(5-\alpha)/(1-\alpha)$。
引入固定的小正参数 $r$，定义

$$
H=\beta(\alpha)+r,\qquad
q=\frac{H-1}{64(1-\alpha)},\qquad
a_{\rm c}=q(1-\alpha)=\frac{H-1}{64}.
\tag{6}
$$

附近始终可取
$1/3<\alpha<1/2$、$1/8<q<1/3$、
$a_{\rm c}<1/7$、$H>13/2$。高、低两类仍用 $n$ 与 $64n$ 个包：

$$
\begin{array}{c|c|c|c}
 & (a_i/b_i)^2 & b_i^2 & w_i\\ \hline
\text{low}&\alpha&q&q\\
\text{high}&H&1&1\\
\text{mid}&1&b_i^2&q .
\end{array}
\tag{7}
$$

各平方斜率内部允许原符号及同源伴随方向。最后一行的真实幅度在 §4 给出；没有把其形状常数独立指定。

前两类的 real 二次质量仍准确配平：

$$
64q(\alpha-1)+(H-1)=0.
\tag{8}
$$

同时
$C_4-E_4=\sum b_i^4((a_i/b_i)^2-1)C/w_i=0$，
而另一个全角四次条件需要付出的新增量为

$$
64\alpha q(\alpha-5)+H(H-5)
=(H-\alpha)\{H-\beta(\alpha)\}=4T_r,
$$

$$
T_r=\frac{(H-\alpha)r}{4}>0.
\tag{9}
$$

因此给 mid 指定总四次质量

$$
\boxed{\ \sum_{\rm mid}\frac{b_i^4}{q}=nT_r\ }
\tag{10}
$$

便准确支付 $A_4=5C_4$；每个 mid 的贡献是 $-4b_i^4/q$。

后面还需要保留逐包恒等式。对 $x=\alpha,H$，

$$
x(x-5)=(\alpha+H-5)(x-1)+r_0,\qquad
r_0=(1-\alpha)\{H-\beta(\alpha)\},
$$

$$
r_0(64q+1)=4T_r.
\tag{11}
$$

这说明新斜率会产生一个 unsigned local 背景，不能继续使用旧的
$E_{22}=\alpha\beta E_{04}$。§5 用真实正权匹配这个背景。

## 3. 居中 cell、真实空隙及未近似的累计一阶矩

取一个足够大的、但最终固定的 $n=2^M$，$M\ge11$。
本稿允许增大这个有限包数；不把它冒作原 $n=2048$ 的同一个 profile。

令 $c=(n-1)/2$，低中心为

$$
t^L_{k,l}=64A(k-c)+A(l-31.5),
\qquad 0\le k<n,\ 0\le l<64.
\tag{12}
$$

高中心为居中排序

$$
t^H_k=B(k-c),\qquad
B^2=\frac{A^2((64n)^2-1)-12\nu(1-q^2)}{n^2-1}.
\tag{13}
$$

取 $A=\Lambda+\sqrt\nu$，$\Lambda\ge10$ 最后一次固定。于是

$$
V_L-V_H=\nu(1-q^2),\qquad
B>64A,\qquad
B-64A=\frac{4095A^2-12\nu(1-q^2)}
 {(B+64A)(n^2-1)}.
\tag{14}
$$

对 $n\ge2048$，原高点偏移
$|(B-64A)(k-c)|<A/100$；高包仍严格位于自己 cell 中央的两个低包之间。所有原包的支撑严格不交。

在第 $k$ 个 cell 与第 $k+1$ 个之间有一个真实 gap，中心是

$$
g_j=64Aj,\qquad j=k-\frac{n-2}{2},
\qquad -\frac{n-2}{2}\le j\le\frac{n-2}{2}.
\tag{15}
$$

gap 的左右低中心分别是 $g_j-A/2$、$g_j+A/2$。
后面所有 mid 支撑都放在其中央 $A/8$ 子区间内。

这里“旧部分”只指同一组新参数下尚未加入 mid 的低高部分，绝不指保持某个已发表固定 profile 不变。记它的 real 差密度为
$D_{\rm r}=f_{\rm old}''{}^2-g_{\rm old}''{}^2$。
每个 cell 的总质量为零，shape 一阶矩准确为

$$
64a_{\rm c}m(B-64A)(k-c).
$$

所以在整个第 $j$ 个 gap 内，

$$
\boxed{
J(D_{\rm r})=0,\qquad
J(xD_{\rm r})=
\delta\,64a_{\rm c}m(B-64A)
\,\frac{n^2/4-j^2}{2}>0.
}
\tag{16}
$$

共同物理中心 $\xi_0$ 的项因各 cell 的零质量消失。第二式来自所有未来 cell 的准确和
$\sum_{\ell=k+1}^{n-1}(\ell-c)
=(n-k-1)(k+1)/2$。
它包含全部远侧 history，不只是相邻两包的点模型。

低、高 imaginary 三矩用各自足够长的 Thue–Morse 符号支付。
式 (14) 是 real 第三矩所需的准确方差差，包含 $2(u')^2$ 的原 $I_2$ 项。

## 4. 五个 gap 簇：严格正的零、二、四矩匹配

### 4.1 同宽正权匹配

低中心其实是长度 $64n$ 的完整等距序列，其均值为零。记其无权平均二、四矩为

$$
V_L=\frac{A^2((64n)^2-1)}{12},\qquad
W_L=\frac{A^4((64n)^2-1)(3(64n)^2-7)}{240}.
\tag{17}
$$

在允许的整数 $j$ 中，选最接近下列归一位置的五个 gap：

$$
\frac{2j}{n}\longrightarrow
0,\quad \pm\frac1{\sqrt2},\quad\pm\frac{\sqrt3}{2}.
\tag{18}
$$

对充分大有限 $n$，它们严格不同，均远离两端；可统一取
$|2j/n|<9/10$。

每个 gap 簇含一个固定 $N=2^s\ge8$，位置为

$$
t_{j,\ell}=64Aj+4q\left(\ell-\frac{N-1}{2}\right),
\qquad 0\le\ell<N.
\tag{19}
$$

选 $Nq\le A/32$。每个簇包括各真实包支撑在内的半径小于
$2Nq\le A/16$，故完全处于原 gap；簇内间距 $4q$ 也严格大于两支撑半径和。

把中央簇及两对对称簇的总四次概率分别记 $p_0,p_1,p_2$；
一对中的两个簇各分 $p_j/2$。对每个簇取其 $N$ 个中心的平均。要求

$$
\boxed{
p_0+p_1+p_2=1,\quad
\langle t^2\rangle_{\rm mid}=V_L,\quad
\langle t^4\rangle_{\rm mid}=W_L .
}
\tag{20}
$$

奇的一、三次矩由真实镜像位置和相同权重准确为零。

这三式是实际有限中心的线性系统，不是连续测度近似。用 $32nA$ 归一化，low 的二、四矩趋于 $(1/3,1/5)$；
簇内部宽度在此尺度下是 $O(1/n)$，且在
$Nq/A\le1/32$ 全范围一致。三个不同的归一中心平方趋于
$0,1/2,3/4$，相应矩阵是非退化 Vandermonde 矩阵。
极限严格正解为

$$
\boxed{(p_0,p_1,p_2)=\left(\frac{19}{45},\frac25,\frac8{45}\right).}
\tag{21}
$$

因而先选择一个足够大的有限二幂 $n$，(20) 就有唯一严格正解，并在所需小参数邻域连续、解析。没有设置负幅权或把无效端点当作正包。

也可直接消去共同簇内二、四矩：若簇内偏移的二、四矩是 $v_N,w_N$，三个矩阵列为
$(1,\ g_j^2+v_N,\ g_j^4+6g_j^2v_N+w_N)$。
行初等变换立即化为中心平方的 Vandermonde 矩阵。故论证使用的正性在有限 $n,N$ 上明确可检验，不需求积。

### 4.2 真实幅度与三复矩

令单个簇的概率为
$\pi_j\in\{p_0,p_1/2,p_2/2\}$。
在它的所有 $N$ 个包中取同一正幅

$$
b_j^4=\frac{nT_r\,\pi_j q}{N},\qquad
a_{j,\ell}=b_j,\quad b_{j,\ell}=\epsilon_\ell b_j,\quad
\epsilon_\ell=(-1)^{\operatorname{popcount}(\ell)}.
\tag{22}
$$

因此确有 $a_{j,\ell}^2=b_{j,\ell}^2$，(10) 准确成立。
此处 $b_j$ 是正实四次根；符号只进入第二方向。

在每个簇内，real 差密度逐点为零，cross 三矩则由
$\sum\epsilon_\ell t_{j,\ell}^r=0$，$r=0,1,2$，准确支付。
所以每个 mid 簇自己就是三矩闭的圆：不是只在最后把若干不闭簇勉强相加。
低高加 mid 后的整个圆仍有原三个复矩。

(20) 还给出全部四次中心平均

$$
\boxed{
\frac1{nT_r}\sum_{\rm mid}\frac{b_i^4}{q}\,t_i^r
=\frac1{64n}\sum_{\rm low}t_i^r,\qquad r=0,1,2,3,4.
}
\tag{23}
$$

由于 mid 和 low 的宽度同为 $q$，共同平移及主宽 $\delta$ 后，这些恒等仍逐项准确。这是下面两个新 local even 门共用的一份真实支付。

## 5. 第三斜率没有漏掉原完整 local 面积

对任意只含同包 self 的一个外矩，把 even 母包的真实 self 写为
$w^{-1}P(\xi,w)$。在实际主宽下，先定义
$\widehat P_\delta(t,w)=\delta^{-1}P(\xi_0+\delta t,\delta w)$；
实际 self 就是 $w^{-1}\widehat P_\delta(t,w)$。
以下 $\langle P\rangle_L,\langle P\rangle_H$ 简记这个
$\widehat P_\delta$ 的 low/high 无权平均，故共同的 $1/\delta$ 没有丢失。
所有现用多项式对中心的次数至多4。
mid 的宽度等于 low，(23) 给其四次权平均准确为 $\langle P\rangle_L$。

R259 的 $E_{04}$ 是

$$
E_{04}=n(H-1)\{\langle P\rangle_H-\langle P\rangle_L\}.
\tag{24}
$$

mid 的 $x-1$ 为零，不改变它。另一方面由 (11)、(23)，

$$
\begin{aligned}
E_{22}
={}&(\alpha+H-5)E_{04}\\
&+nr_0\{64q\langle P\rangle_L+\langle P\rangle_H\}
-4nT_r\langle P\rangle_L .
\end{aligned}
$$

用 $r_0(64q+1)=4T_r$ 得到新的准确关系

$$
\boxed{
E_{22}
=\left(\alpha+H-5+\frac{r_0}{H-1}\right)E_{04}.
}
\tag{25}
$$

这不是旧两斜率恒等的沿用，而是新增真实测度匹配后的结论。
它对每份共同平移后的 self 仍成立，故对原八/十二完整副本的四次加权和也成立。

逐项应用如下。

- **整个 $A_{-2,-3}$。** R250 的真实三外矩在 rank-one 微包类中准确局域。第零矩恒零；第一矩使用四次质量，第二矩使用一次中心和及母 $N_0=0$。式 (9)、(10)、(23) 给 $A_4=5C_4$、$C_4=E_4$ 及相应一次中心条件。普通或同源伴随的 even 数据一致，odd 部分交给完整十二复制。
- **整个 $A_{-1,-3}$。** R267 的原跨包核为零，前两 self 使用上述零、一次矩；第三个原 self 在真实 $\mathcal F_\kappa(u)=0$ 后正比于
  $Cw^{-1}(\xi^2+\nu w^2)$。式 (14)、(23)、(25) 准确保全其两个 even 系数。
- **整个 $A_{1,-1}$ 第零外矩。** 其原跨包核也为零，真实 self 为
  $w^{-1}P_4(\xi,w)$，其中
  $P_4=a_4C\xi^4+\mathcal B_\kappa w^2\xi^2+\mathcal D_\kappa w^4$
  是 R270 的原式。式 (23) 匹配它的全部有限宽项，绝非只配 $\xi^4$。因此只需保原真实 $E_{04}=0$，(25) 就付 $E_{22}=0$。
- **整个 $A_{-1,-2}$ 第零外矩。** mid 对整体 $f''{}^2,g''{}^2$ 的增加均关于同一中心对称。R273 的 even history
  $\int f''{}^2J(f''{}^2-g''{}^2)$ 仍准确为零；其 local 零、一次四次矩也由上式保持。所有 odd 项仍由原完整复制支付。

这里每个 $(f',g')$ 在最小真支撑上仍成比例，故完整 hook 张量继续为零。原八个完整副本的第七差分支付全部四个第三槽；随后原十二个完整副本的第十一差分支付全部36个 Gaussian odd 条件及 odd 能量。副本在求能量根以前一并纳入，四次正权中心仍取零。跨完整副本只在 inner 三矩已为零后才消掉；base 内部的 mid/old history 从未被删去。

## 6. 六能量与四变量实际 IFT 仍有非退化解

mid 在 real 二次差 $gg-ff$ 中逐点为零。R256 的一般微包完整 bulk 归约于是给：它对 $L_c,M_c$ 的贡献准确为零；在共振 germ 上
$N_c=6M_c$、$N_s=6M_s$ 仍成立。没有从这个能量局域事实推出 Gaussian history 局域化。

新 low/high 的 leading 能量方程是

$$
P(\alpha,r)=
\frac{64\alpha(1-\alpha)}q-H(H-1)=0,
$$

即

$$
4096\alpha(1-\alpha)^2=H(H-1)^2.
\tag{26}
$$

在 $r=0$，它正是 R256 的
$256\alpha(1-\alpha)^5-(5-\alpha)=0$，
有唯一简单 $\alpha_0\in(1/3,1/2)$。
故存在小正 $r$ 的简单根 $\alpha(r)$，且可统一保 §2 的严格范围。

母包继续使用 R270 的真实 $(\gamma,s,z)$，不是新增独立 self 常数。其三归一母条件

$$
\mathcal H=27\nu-K_2/A_0,\qquad
\mathcal F_\kappa,\qquad \mathcal J/h
$$

在原小正 $h$ 的真实母根上有可逆形状 Jacobian。式 (14) 保留完整方差差，所以在新简单 $\alpha(r)$ 根上，归一 $M_c$ 行仍是非零因子乘 $\mathcal H$；新低高宽度仍满足 $q\ne1$。

在最后位置 $\xi_0>0$，实际主方程仍是

$$
\delta^3L_c=0,\qquad
\delta(M_c+3L_c/\xi_0)=0,\qquad
\mathcal F_\kappa=0,\qquad E_{04}^{\,A_{1,-1},I_0}=0.
\tag{27}
$$

最后一行使用 R270 的整个有限 $\delta$ self 多项式。mid 的 $E_{04}$ 恒为零，不进入这四行；(23) 只是在解后准确补付相应 $E_{22}$。
归一第二行可能出现的 $\delta^{-1}$ 项仍因各类及两层副本的四次中心零消失；mid 甚至没有该行的 real 能量贡献。
第四行减去原 $\mathcal F_\kappa$ 倍数后，在 $\delta=0$ 恰给
$\mathcal J/h$。所以原四变量 Jacobian 的三角非退化证明完整保留。

对每个固定的有限 $n,N,\Lambda$、最后位置和复制间距，真实 IFT 给充分小正 $\delta$ 的
$\alpha,\gamma,s,z$，使 (27) 全部准确成立。所有正宽、正权及严格 gap 都在其统一邻域保留。这里没有先把一个 leading 解当作实际解，也没有在解完后更改 mid 幅度而忘记 local 门：幅度始终由该实际参数下的 (20)、(22) 定义。

## 7. 原单位的有限宽负响应

对任一 mid 簇，记其真实二次质量

$$
\mu_j=N b_j^2m=m\sqrt{nT_r\pi_jNq}>0.
\tag{28}
$$

在 $\theta=\pi/2$，mid 的 inner 差为零。因此新项只来自其 outer
$g''{}^2$ 对未来旧 inner 差的作用。由 R259 的原跨核及 (16)，准确有

$$
\boxed{
\Delta S=0,\qquad
\Delta(Z/k)
=-\sum_j\mu_j\,J(xD_{\rm r})|_{\text{gap }j}<0.
}
\tag{29}
$$

整个真实包支撑上 primitive 都是同一常数，所以(29)不含点质量近似或窄包误差。mid 自项在此角度也为零，因为 $a_i^2-b_i^2=0$。

总 mid 二次质量为

$$
\mu_{\rm mid}
=m\sqrt{nT_rNq}
\{\sqrt{p_0}+\sqrt{2p_1}+\sqrt{2p_2}\}.
\tag{30}
$$

这是固定总四次质量 (10) 与二次质量之间的真实差别。

为明确有限容量，先固定上述充分大 $n$，固定小正 $r,h$ 的母根邻域。选固定上界 $q_{\max}<1/3$，取 $N$ 为不超过
$\Lambda/(32q_{\max})$ 的最大二幂。对任意足够大有限 $\Lambda$，

$$
N\ge8,\qquad
Nq\le A/32,\qquad Nq\ge c_0A>0
\tag{31}
$$

在整个所需参数邻域成立，其中 $c_0$ 与 $\Lambda$ 无关。所有 gap 簇仍严格装得下；不是把无限多个包塞进固定正宽区域。

五个 gap 有 $|2j/n|<9/10$。由 (14)、(16) 得一个与 $\Lambda$ 无关的正常数 $c_1$，使

$$
J(xD_{\rm r})|_{\text{gap }j}
\ge c_1\delta a_{\rm c}mA .
\tag{32}
$$

结合 (30)、(31)，有

$$
\Delta(Z/k)\le-c_2\delta A^{3/2}.
\tag{33}
$$

常数 $c_2>0$ 可以依赖已经固定的 $r,n,h,\kappa$ 邻域；不声称在 $r\downarrow0$ 时一致。

旧低高部分的准确 R275 公式只含 $A$、$(B-64A)(n^2-1)$ 及有限母常数，故
$Z_{\rm old}/k=O(\delta A)$。
原居中 $S$ 则准确为

$$
S=\delta n a_{\rm c}
\{10928m^2qA+64(1-q^2)B_{\rm loc}\},
\quad
B_{\rm loc}=C\nu-\mathcal L+\Delta/4 .
\tag{34}
$$

所以先取一个足够大但有限的 $\Lambda$，再取实际充分小正 $\delta$，
就得到 $S>0$、$Z/k<0$。R275 任何共同 $0<c_*<1$ 的左式现在满足

$$
(1-c_*)S-c_*Z/k>0.
\tag{35}
$$

这是真实离开其排除族的机制，不是放宽原门或改一个不影响 profile 的标签。

共同正幅归一化使 $I_0(f,f)=I_0(g,g)=1$、$I_0(f,g)=0$，只同乘所有四次量一个正因子。它不影响(29)、(35)的符号。未归一化的 $A^{3/2}$ 容量估计不被误称为归一化后量值也无界。

## 8. Pure 累计量：先支付大中心项，再保正负号

定义原合法复 profile $q_{\rm c}=f+ig$，以及

$$
\mathscr Q=
\frac12\int[J(q_{\rm c}''{}^2)]^2
+\int x^2q_{\rm c}''{}^4
-\frac83\int xq_{\rm c}'q_{\rm c}''{}^3
+\frac43\int q_{\rm c}q_{\rm c}''{}^3
+\int q_{\rm c}'{}^2q_{\rm c}''{}^2 .
\tag{36}
$$

mid 单包的 local $\xi^2$ 项可能很大；不能先把它估成与中心无关的 $O(1)$。
§5 已付整个 $A_{-1,-3}$、母 $\mathcal F_\kappa=0$，所以对同一个实际母包，有准确恒等

$$
\boxed{
\sum_i\operatorname{Re}(a_i+ib_i)^4
 \frac{C\xi_i^2}{w_i}
=-C\nu\sum_i\operatorname{Re}(a_i+ib_i)^4w_i .
}
\tag{37}
$$

这里使用实际物理中心与宽度；若统一在 shape 坐标写，则双方共同按 (4) 换元。
R267 原组合的非零系数已经除去；没有把 $C,\nu$ 独立调节。

因此 (36) 的整个 real local 部分准确为

$$
(\mathcal L-C\nu)
\sum_i\operatorname{Re}(a_i+ib_i)^4w_i,
\quad
\mathcal L=X_2-\frac83N+\frac43U_3+V_2.
\tag{38}
$$

对新增 mid，shape 中
$\sum \operatorname{Re}(a_i+ib_i)^4w_i=-4nT_rq^2$。
大中心项已经由全局原条件抵消后，才得到其 local 代价与 $A$ 无关。

以下 (39)、(40) 统一在 shape 坐标 $t$ 评价；实际 primitive 平方积分另乘共同正因子 $\delta$。这不影响符号或相对 $A$ 的阶。原完整 $M_4,M_1,N_1$ 的零（见本节末）还保证整个 $\mathscr Q$ 没有共同中心附加项。

再看 primitive。每个 mid 簇内

$$
q_{\rm c}''{}^2
=2i\,b_j^2\sum_{\ell=0}^{N-1}\epsilon_\ell
 \big(\eta_{q,t_{j,\ell}}''\big)^2 .
$$

其零、一次矩都为零，所以该簇 primitive 真紧，且其积分为零。
旧 primitive 在整个 gap 上为常数，故

$$
\int A_{\rm old}A_{{\rm mid},j}=0
$$

准确成立；不同 mid 簇的 primitives 支撑不交，交叉项也零。
TM 符号的前缀部分和绝对值至多1，在包内也给统一幅界
$|A_{{\rm mid},j}|\le2b_j^2m$。
簇长度小于 $4Nq$，于是

$$
\int|A_{{\rm mid},j}|^2
\le16m^2Nq\,b_j^4
=16m^2nT_r\pi_jq^2.
\tag{39}
$$

这是实际有限宽证明，不是把单个非紧 primitive 删掉。

原低高部分的 ordinary quadratic history 仍可用 R269 的同一真实求和。
令 $\ell=2q\sqrt\alpha$、$H_{\rm im}=2\sqrt H$；其 shape 有序项为

$$
n\left[
A\{-21856a_{\rm c}^2+32\ell^2\}
+\frac{H_{\rm im}^2B}{2}
\right].
\tag{40}
$$

在 §2 的邻域，$a_{\rm c}<1/7$、$H>13/2$、$B>64A$，
故 (40) 严格大于
$nA(832-21856/49)>0$。R257 中它乘 $-m^2/2$。
原 self/finite-width 项与 (38)、(39) 均不随 $A$ 线性增长；
所以 ordinary 版仍有 $\operatorname{Re}\mathscr Q_-<0$。

同源伴随版的 imaginary primitive 在每个旧外包内就紧，
real primitive 不变；其正领先项为
$10928nm^2a_{\rm c}^2A$。
全部其余项及 mid 代价由同一个实际母包的有限常数控制。
再扩大一次有限 $\Lambda$ 即得
$\operatorname{Re}\mathscr Q_+>0$。
这与 §7 的 $Z/k<0$ 所需大 $\Lambda$ 可以同时满足。

原及新增的完整 $M_4,M_1,N_1$ 都为零：real 部分由 (9)、(23) 与中心反演支付；ordinary 的 imaginary 部分由 TM 的零/一次矩支付；mid 的四次复权为纯实负值；伴随的奇因子由原内部 TM3 支付。故整个 $\mathscr Q$ 的共同平移规则无新增项。
八/十二完整副本只给正四次权和，十二复制再清其虚部。
两个最后位置的 ordinary/companion 完整 block 各自先完成真实 IFT，然后以正四次幅混合，可得

$$
\boxed{\mathscr Q=0,\qquad S>0,\qquad Z/k<0.}
\tag{41}
$$

所有在 §5、§6 已为零的完整条件都保持。这里不要求两个 block 的实际母参数或最后宽度相等。

## 9. 同一负方向还改变第一正负矩，不能当成独立坐标

定义

$$
Y_1=2I_1\{g,[P,Y](g;f\odot f-g\odot g)\}.
$$

R271 的原跨核为
$-(m_0n_2+m_2n_0)/2$。
在 mid 所在 gap 中，未来旧 real 总质量为零，故只有 outer 的 $m_0$ 项留下。
两对镜像 gap 的未来二阶矩相加，准确等于
$4\xi_0J(xD_{\rm r})$；central gap 则等于
$2\xi_0J(xD_{\rm r})$。
这使用原 $I_2$ 中的 $2u'v'$，不是只用点中心平方。
于是完整五簇有

$$
\boxed{\Delta Y_1=\xi_0\,\Delta(Z/k).}
\tag{42}
$$

两层完整复制的四次中心零使同一关系继续成立。
所以本稿的负方向同时更改 R271 已付的带最后中心矩。
不能将 R271 的旧六块混合原封不动搬来，再宣称这个改动不影响它。
后续需要按真实向量 $(S,Y_1,Z/k,\ldots)$ 配平，或增加新的独立作用。

## 10. $Z$ 的另一 even 系数仍有真实母形余项

保留 R275 原定义

$$
\begin{aligned}
H_1={}&\frac{\mathfrak d}{12}(X_2-C\nu)-p_GN
+\frac{d(a_G+b_G)}3U_3
+\frac{a_G(4e-d)}2V_2,\\
\mathcal R={}&H_1+k(C\nu-\mathcal L),\\
p_G={}&\frac{d(a_G+b_G)+2e(4a_G+b_G)}3,\qquad
\mathfrak d=2d(a_G+b_G)+e(11a_G+5b_G).
\end{aligned}
\tag{43}
$$

它来自原四条真实 self 的 Green/primitive 合并，非新增自由坐标。
R259 的上三角全槽恒等给

$$
E_{22}^{Z}-E_{04}^{Z}
=\operatorname{Re}\{2I_1(q_{\rm c},
 [B_{-1},B_{-2}](q_{\rm c};q_{\rm c}\odot q_{\rm c}))\}.
$$

用 (37) 消去已付的二阶中心项，再用 (36) 保留完整 quadratic primitive，准确得到单一母包 block 的身份

$$
\boxed{
E_{22}^{Z}-E_{04}^{Z}
=k\operatorname{Re}\mathscr Q
+\mathcal R\sum_i\operatorname{Re}(a_i+ib_i)^4w_i .
}
\tag{44}
$$

对于不同实际母根的最后 block，右边应逐 block 乘正四次幅度相加，不能强行抽出同一个 $\mathcal R$。
特别即使以后同时支付 $\mathscr Q=0$、$E_{04}^{Z}=Z=0$，
另一个 even 系数仍需

$$
\sum_{\rm blocks}\lambda_j\mathcal R_j
 \sum_{i\in j}\operatorname{Re}(a_i+ib_i)^4w_i=0 .
\tag{45}
$$

本稿没有证明 (45)，也没有把 $\mathcal R/k=O(h)$ 冒成准确零。
mid 的 full-angle inner 差仅在 $\theta=\pi/2$ 为零；
一般角度为一个含 $\cos\theta\sin\theta$ 的真实项，(44)正保留了它最终带来的 even 代价。

## 11. 参数次序、保持范围及下一问题

选择顺序可以明确固定如下。

1. 在原联合安装的小 $\kappa^2$ 邻域，先取 R270 的一个足够小正母宽 $h$ 及非退化母根邻域；所有归一系数对该邻域光滑。
2. 选择固定小正 $r$，使 (26) 有简单根，保 $q,a_{\rm c},H$ 的严格范围。随后选一个足够大的有限二幂 $n$，保证五簇的正权矩匹配在允许簇宽范围一致成立。
3. 取足够大但有限的 $\Lambda$，并一次固定满足 (31) 的二幂 $N$。这同时保真 gap、负响应主导、pure 正负号。完整八/十二复制及最后位置、间距也在此时固定。
4. 最后用 (27) 的四变量 IFT 选小正 $\delta$，并在这些实际参数上使用 (20)、(22) 的准确正权。若最后有多个 block，各自先在最终位置解完，再只用共同正实幅相加。

归一系数在小 $\kappa^2$ 区间的光滑性与 R270 相同；每个最终有限 profile 及其有限范数再进入原 R227/R241 的联合安装范围。不用零宽 profile，不授所有收缩宽度统一的高阶范数界，也不把新圆说成旧 fixed-seed 的一次变形。

这条新机制准确完成的是：

- 用真实第三斜率和有限正宽包增加 outer 平方质量；
- 用同一份正权零、二、四矩匹配支付新增的 local 全角代价；
- 在完整 history 中准确保持 $S$ 并降低 $Z/k$，有限参数下打破 R275 半平面；
- 保留六能量、指定完整面积与 odd 条件，并保留可付 pure $\mathscr Q$ 的双号；
- 明确记录与 $Y_1$ 的耦合和另一个 $Z$ even 的母形余差。

它不是主课题的完成，也不减少一个未经同时支付的 formal-even 计数。后继已经有不同于原两斜率族的真实向量方向，但必须同时处理 (42)、(45) 及其余完整有序面积；不能继续只调原 cell 位置或把一个负响应当作全解。

