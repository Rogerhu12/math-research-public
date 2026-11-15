# R347：同权完整矩的准确半平面与低成本单向 P–Y 第一矩纠正

日期：2026-11-15。**完整纸面证明与实际正幅构造。** 未执行求积、符号程序、人工检查、profile 扫描或新的研究计算。

[R348](R348-true-translation-and-Green-self-terms-pay-the-first-positive-minus-one-Gaussian-moment.md) 已在同一弱圆上联合支付负三个 Gaussian pair 的全部九矩及 Y–Z 的第零、第一矩。本稿处理尚未支付的 P–Y 第一外矩。它的两个 even 系数本来相同，不能按两个独立目标计数。

这里不能直接套用新增较高权矩的三角分离：P–Y 第一矩与已有 Z–W 第二矩具有**同一个完整伸缩权 −4**。从 R271/R275/R343 的原完整式可得一个准确的有限宽恒等式。在目前真实两坡、两宽度强原型上，它给一个严格半平面；现有正锥不能无条件扩大成包含新标量的全空间。

同一恒等式又给实际建设：选定真实母包与足够大的有限间距后，R348 八目标矩阵的一个严格正核，自动成为保持全部已付矩、但使 P–Y 第一矩严格为负的真实模块。以同权伸缩可将这一负纠正的正 Ψ 成本任意缩小。因此若当前弱基线的待付标量为正，就能在同一最终构造中准确清除它。**本文尚未证明该基线具有所需正号，也未构造相反方向。**

来源：[R271](R271-six-complete-blocks-pay-the-first-two-positive-negative-Gaussian-moments.md)、[R275](R275-first-moment-obstruction-for-the-small-width-two-slope-family.md)、[R343](R343-two-real-orders-and-positive-center-clusters-pay-the-third-Gaussian-second-moment.md)、[R346](R346-positive-six-target-cone-pays-a-further-complete-Gaussian-zero-moment.md)、R348。所有有序 primitive、单包 self 与真实 Green 尾使用这些原式，未以点质量极限代替实际 profiles。

## 1. 原几何、规范与共同标量

固定同一实际共振参数 $0<t=\kappa^2<1/100$、$h_e>0$，并沿用
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},\quad
L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2},
$$
$
W_*=aR+bS,\qquad Z_*=dL+eU.
$$
几何系数与 R343 相同。定义两个固定非零系数
$$
k_*=\frac{db}{2}-ea
=-\frac{\kappa(1173\kappa^6+177\kappa^4+122\kappa^2+8)}
{256h_e^3}\ne0,
$$
$
\chi_\kappa=\frac{\kappa(28t^2-35t-4)}{64h_e^3}\ne0.
\tag{1}
$$
$k_*$ 的符号不预设为正。

对合法三矩圆
$$
u_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-u_\theta\odot u_\theta
$$
记
$$
\mathcal B_j=I_j\{u_\theta,[Z_*,W_*](u_\theta;D_\theta)\},\qquad
\mathcal C_j=I_j\{u_\theta,[Z_*,Y](u_\theta;D_\theta)\},
$$
$
\mathcal D_1=I_1\{u_\theta,[P,Y](u_\theta;D_\theta)\}.
\tag{2}
$$
所有 $I_j$ 保留原定义，尤其 $I_2$ 中的 $2u'w'$。

R271 对任意实或复紧单包的完整 self 身份是
$$
2I_1\{v,[P,Y](v;v^2)\}=-\frac12 I_0(v,v)I_2(v,v).
\tag{3}
$$
它包含真实 Green 项 $+\mu_0\mu_2/2$。合法复输入 $q=f+ig$ 的右边为零，因此完整圆的两个 even 系数相同；原十二完整副本消去 odd 后，有
$$
\boxed{\mathcal D_1(\theta)=d_1\sin^2\theta,\qquad
d_1=\mathcal D_1(\pi/2).}
\tag{4}
$$
这只减少目标维数，不把 $d_1$ 置零。

原算子完整权给
$$
\mathcal B_2(f_H,g_H)=H^{-4}\mathcal B_2(f,g),\qquad
\mathcal D_1(f_H,g_H)=H^{-4}\mathcal D_1(f,g),
\quad f_H(x)=f(x/H).
\tag{5}
$$
所以不能用两者不同阶的假设来获得新的三角块。

## 2. 同一个实际母包与有限两坡族

取 R343/R346 的一个实际 even 实紧母包 $v$，满足原
$\mathcal F_\kappa(v)=0$。母包此后固定；其普通/真实伴随两个版本沿原最细子包定义。写
$$
m=\int(v'')^2>0,\quad
\nu=\frac{I_2(v,v)}m,\quad
C=\int(v'')^4,\quad X_2=\int y^2(v'')^4,
$$
$
N=\int yv'(v'')^3,\quad
U_3=\int v(v'')^3,\quad V_2=\int(v')^2(v'')^2,
$$
$
\Delta=\iint|y-z|v''(y)^2v''(z)^2\,dy\,dz,
\quad
\mathcal L=X_2-\frac83N+\frac43U_3+V_2.
\tag{6}
$$
这些全是同一个母包的真实有限数，不能独立指定。

用 R275 的原完整 local 组合
$$
\mathfrak d=2d(a+b)+e(11a+5b),\qquad
p=\frac{d(a+b)+2e(4a+b)}3,
$$
$
B_{\rm loc}=C\nu-\mathcal L+\Delta/4,
$$
$
H_1=\frac{\mathfrak d}{12}(X_2-C\nu)-pN
+\frac{d(a+b)}3U_3+\frac{a(4e-d)}2V_2,\qquad
\mathcal R=H_1+k_*(C\nu-\mathcal L),
\tag{7}
$$
以及 R343 的真实完整 R–S 第二 self 组合
$$
K_{RS}=-\frac53(X_2-C\nu)+\frac{16}3N-4V_2-\frac43U_3.
\tag{8}
$$

取
$$
\frac13<\alpha<\frac12,\quad
\beta=\frac{5-\alpha}{1-\alpha},\quad
q=\frac1{16(1-\alpha)^2},\quad
a_c=q(1-\alpha)>0,\quad n=2048.
\tag{9}
$$
低、高的真实平方幅度为 $(\alpha q,q)$、$(\beta,1)$；宽度为 $q,1$。原方差式为
$$
(B-64A)(B+64A)(n^2-1)
=(4095-12\rho^2)A^2-12\nu(1-q^2).
\tag{10}
$$
本文只需已经付过合法次序的 $\rho=0,20$。选择 $A>10+\sqrt\nu$ 并再取足够大有限值，原严格不交与所有三矩关系保持。令
$$
D_B=B-64A,\qquad
U_\rho=na_c(64q+1)
\left\{\frac{16}3D_B(n^2-1)+A\left(\frac32\rho^2-512\right)\right\}.
\tag{11}
$$
这是原有限 cell 的完整有序和，不是局部矩。

原型的主宽为 $\delta>0$，完整八／十二复制的正四次权和为 $\mathcal W>0$。相对 copy 中心按原构造四次加权居中；最终实际共同中心为 $X>0$。普通/伴随版本在 $\theta=\pi/2$ 的同源 quadratic 与 local quartic 数据相同，故下列该角度公式同时适用；并未声称二者的全部 pure 或 odd 数据相同。

## 3. 三个原完整式与半因子

在未包装 base 的 $\theta=\pi/2$，R275 定义
$$
S_0=2I_0\{g,[P,Y](g;f^2-g^2)\},\qquad
Z_1=2I_1\{g,[Z_*,W_*](g;f^2-g^2)\}.
$$
原准确式为
$$
S_0=\delta na_c
\{m^2A[10928q-(32q+1)\rho^2]+64(1-q^2)B_{\rm loc}\},
\tag{12}
$$
$
Z_1=-k_*S_0-k_*m^2\delta U_\rho
+64na_c\delta(1-q^2)\mathcal R.
\tag{13}
$$
其中单包的 $\int r_i^2J(xr_i^2)$ 与完整有序项已经共同保留。

R271 的完整第一矩在实际中心 $X$ 给
$$
\boxed{d_1=-\frac{\mathcal Wm^2X\delta U_\rho}{2}.}
\tag{14}
$$
这里的 $1/2$ 来自 R271 的 $E_{04}$ 属于加倍面积，而本文 $\mathcal D_1$ 未加倍。原有限宽项及三矩匹配负责消去常数和二次中心项；不是把 $I_1$ 当作普通平均中心。

R343 则给
$$
\mathcal B_1(\pi/2)=\frac{\mathcal WZ_1}{2},\qquad
r_{04}:=\mathcal R_2(\pi/2)
=\frac{\mathcal W}{2}n(\beta-1)\delta(1-q^2)K_{RS},
\tag{15}
$$
$
\boxed{\mathcal B_2(\pi/2)=X(\mathcal WZ_1+\chi_\kappa r_{04}).}
\tag{16}
$$
这里 $\mathcal R_2=I_2\{u,[R,S](u;D)\}$。其非零值和真实左尾均不能省略。完整 $\mathcal B_2$ 在辅助共同中心零处为零，由反射与原正交端项证明；(16) 是原全部平移公式在这些**实际强原型**上的特化，不是任意弱圆的普通矩平移。

所有 copy 的中心矩已经包含在 (14)—(16) 中。跨完整 blocks 的 inner 三矩为零，故后续正幅相加使用完整可加性。

## 4. 一个有限宽准确恒等式

定义新读出
$$
\boxed{\mathfrak F=\frac{\mathcal B_2(\pi/2)}{k_*}-d_1.}
\tag{17}
$$
$k_*\ne0$ 是固定几何系数，不把负幅度藏在此定义中。

由 (12)—(16)，
$$
\begin{aligned}
\frac{\mathfrak F}{X\mathcal W\delta na_cm^2}
={}&-A[10928q-(32q+1)\rho^2]-\frac{U_\rho}{2na_c}\\
&+64(1-q^2)\frac{\mathcal R/k_*-B_{\rm loc}}{m^2}
+32\chi_\kappa(1-q^2)\frac{K_{RS}}{k_*m^2}.
\end{aligned}
\tag{18}
$$
最后系数 32 使用
$$
\frac{\beta-1}{2a_c}
=\frac{2}{q(1-\alpha)^2}=32.
$$
没有将 $r_{04}$ 设零。

将 (10) 准确重写为
$$
D_B(n^2-1)
=\frac{(4095-12\rho^2)A}{128}
-\frac{12\nu(1-q^2)+D_B^2(n^2-1)}{128A},
\tag{19}
$$
代回 (11)、(18)，得到
$$
\boxed{
\begin{aligned}
\frac{\mathfrak F}{X\mathcal W\delta na_cm^2}
={}&A\left(\frac{2731}{16}+\frac{\rho^2}{2}-4q\right)\\
&+(64q+1)\left\{\frac{\nu(1-q^2)}{4A}
+\frac{D_B^2(n^2-1)}{48A}\right\}\\
&+64(1-q^2)\frac{\mathcal R/k_*-B_{\rm loc}}{m^2}
+32\chi_\kappa(1-q^2)\frac{K_{RS}}{k_*m^2}.
\end{aligned}}
\tag{20}
$$
这是有限 $A,\delta,n$ 的准确式，未取 $n=\infty$、$\delta=0$ 或删除原 self 余项。

前行系数严格为正，因为 $9/64<q<1/4$，所以
$$
\frac{2731}{16}+\frac{\rho^2}{2}-4q>\frac{2715}{16}>0.
\tag{21}
$$
第二行非负；后两行是固定母包与固定 $\alpha,\kappa$ 的有限常数，完全不随 $A$ 增长。因此可选一个足够大的**有限** $A$，使
$$
\boxed{\mathfrak F>0}
\tag{22}
$$
对 $\rho=0,20$、普通/伴随两个版本及所有实际正中心 $X$ 同时成立。有限多个不同母包与不同 $\alpha$ 也可分别取有限阈值，随后取共同更大的 $A$；没有要求未知积分具有某个预定符号。

之后可再取足够小的有限正 $\delta$，以满足 R346/R348 的支撑、有限余项符号及实际矩控制入口。(20) 的符号不受这一选择破坏。原 R343 正锥所需的大 $A$ 与这里的大 $A$ 可以共同满足。

## 5. 严格半平面排除无条件升维

对任意有限个上述最终实际正中心原型，以真实正四次幅度 $\lambda_i>0$ 相加。完整可加性及 (22) 给
$$
\sum_i\lambda_i\frac{\mathcal B_{2,i}(\pi/2)}{k_*}
-\sum_i\lambda_id_{1,i}>0.
\tag{23}
$$
所以若新增模块保持整个 $\mathcal B_2=0$，必有
$$
\boxed{\Delta d_1<0.}
\tag{24}
$$
在该族内，既保持 $\mathcal B_2=0$ 又产生正的 $\Delta d_1$ 不可能。甚至无需再使用 $\mathcal B_1=0$ 或其他旧门，这个限制就已经成立。

(5) 表明共同正伸缩将 $\mathfrak F$ 乘 $H^{-4}$；正第四幅仍保符号。因此增加同类正幅列、取更远正中心、重复正伸缩，均不能把这些列变成新三坐标的全正锥。这不是单纯线性秩不足：列的线性 span 可以更大，实际正可达集合仍受 (23) 限制。

范围必须保留：这是上述真实强两坡母族、有限大间距分支的限制，**不是所有合法圆的普遍符号恒等式**，也不是原弱 rank-two 核的障碍。改变母族的机制、使用其他真实质量布局、或分析弱基线本身，均仍是合法下一入口。

## 6. R348 的正核给一个实际负方向

R348 的八目标矩阵来自：

- R343 的八个真实强列，控制 $(\mathcal B_1,\mathcal B_2)$；
- R346 的四个实际母纤维列，新增 $\mathcal C_0$；
- R348 的四个实际母纤维列，新增 $\mathcal C_1$。

它们都使用本稿的两坡、两宽度、even 母包及合法排序。R346/R348 的 $\mathcal F_\kappa=0$、$J/h=\pm\tau$ 在选定实际母宽后给有限多个真实母包；可先要求这些原型的 $A$ 全部超过 (22) 的阈值，再选择有限正 $\delta$。新矩双号仍由其原完整公式和有限余项控制取得。R343 所需原 minor、两种严格号与有限中心群照原顺序固定。

于是整个实际八目标库仍满秩并有严格正核。选一个 $c>0$，使
$$
M_8c=0.
\tag{25}
$$
用 $c_i^{1/4}$ 作实际 profile 幅度，得到一个完整强模块 $(f_-,g_-)$。它准确保持
$$
\mathcal M_j=\mathcal A_j=\mathcal B_j=0\quad(j=0,1,2),
\qquad \mathcal C_0=\mathcal C_1=0,
\tag{26}
$$
并保原完整第三、quartic hook 数据及十二复制的全部 odd 零。所有列已有正 $\Psi$ 系数，故
$$
\Psi(f_-,g_-)=\psi_-\sin^2\theta,\qquad \psi_->0.
\tag{27}
$$
同时，(23) 和 $\mathcal B_2=0$ 准确给
$$
\boxed{\mathcal D_1(f_-,g_-)=-d_-\sin^2\theta,\qquad d_->0.}
\tag{28}
$$
$d_-$ 是这个真实有限模块的完整原函数值；不把它当作未实现的自由数。

这一步没有假设 $d_1$ 行在旧八行之外独立，也不需要新的求秩。所用的是已付的实际严格正核以及新的严格符号身份。

## 7. 任意固定负纠正的 Ψ 成本可小

给定任意 $r>0$。将 (28) 的整个模块共同伸缩 $H$，再乘真实共同幅度
$$
\lambda_H=\left(\frac r{d_-}H^4\right)^{1/4}>0.
\tag{29}
$$
由完整权 (5) 及 $\Psi$ 的权 $-7$，
$$
\boxed{
\Delta\mathcal D_1=-r\sin^2\theta,\qquad
\Delta\Psi=\frac{r\psi_-}{d_-}H^{-3}\sin^2\theta.
}
\tag{30}
$$
(26) 全部保持，因为每个零函数有各自准确齐次权。有限大的 $H$ 已使正成本小于任何指定正余量；新正支撑也可放到固定旧 profiles 的右侧。先选这些有限量，再从全部有限几何包络选择共同合法区间和右 collar，沿原 R105/R114/R271 的实际范围，不对任意已冻结窄区间作扩大承诺。

原三条 directed 行取新模块加入后的完整真实有限值；并未声称模块自己将它们置零。若接入 R348 最后控制器前的负 $\Psi$ 基线，选 $H$ 保留严格负余量，再用同一个初选 $F^\star$、固定真 minor、有限频率正核根，付这三行并将 $\Psi$ 归零。该控制器自身完整72面积均零，故也保 (30) 与全部旧矩。

因此已有一个**实际、有限、可低成本使用的负向 P–Y 第一矩纠正器**。它不是有符号 span 或形式负元。

## 8. 对当前弱圆仍需解决的具体门

设 R348 最后控制器前的实际基线有
$$
\mathcal D_1=r_{\rm old}\sin^2\theta,\qquad
\Psi=-\Delta_0\sin^2\theta,\quad\Delta_0>0.
$$
若进一步证明 $r_{\rm old}>0$，取 (30) 的 $r=r_{\rm old}$，选有限 $H$ 使新增成本小于 $\Delta_0/2$，就能在同一构造中把整个 P–Y 第一矩准确归零，同时保持已付十一外矩、完整第三与最后三行。

若 $r_{\rm old}=0$，无需增加该纠正器。若 $r_{\rm old}<0$，本稿的负方向不能清除它；(24) 解释了为什么不能通过简单增加现有同类正幅模块得到所需正方向。

**当前没有证据将 $r_{\rm old}$ 的符号写成正号。** 下一子问题是：从原 weak mixed/Green 式计算该标量及其对已付三个最终中心的真实依赖，或构造一个突破 (23) 的新实际正方向。不能只变旧中心而破坏 B0/B1/B2，不能把 primitive 差当作自由旋钮，也不能将 R271 旧六块的单独可达性直接移植到当前同时九矩分支。

本稿没有把整个 P–Y 第一矩标为已付，没有减少当前剩余 Gaussian 门的正式记账，更未支付完整第四、period、同一个 gauge 的 joint 条件或 README 的最终曲面标准。新增的完成结果是 (20) 的准确有限恒等式、(24) 的真实族内限制，以及 (28)—(30) 的低成本实际负方向。
