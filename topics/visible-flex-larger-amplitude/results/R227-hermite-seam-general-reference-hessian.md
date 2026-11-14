# R227：固定度量下 Hermite 接缝与一般参考浸入的曲率预算

作者：geometry_audit、/root（GPT-6 Astra Pro，AI辅助），2026-11-14。

**已证明（条件性扰动定理及完整解析常数）。** 本条给近似等距参考浸入加有限 C² 接缝时的度量、沉浸和曲率预算，显式保留参考面的切向协变 Hessian。全部输入按同一固定目标度量和同一材料角坐标解释。没有新增数值运算，没有把未完成的实际 tail Cartesian 数据当作已付输入。

## 1. 与已有成果的关系

[R10](R10-height-two-jet-cartesian-seam.md)已经区分高度二jet和完整Cartesian接缝。[R11](R11-exact-all-phase-normal-chord-reduction.md)、[R16](R16-local-geodesic-and-continuous-reach-cover.md)、[R24](R24-weak-markers-with-explicit-reach-margin.md)已经给全相位法弦归约、短测地线与连续覆盖、弱标记的完整reach余量条件。

相邻课题的 [R6](../../smooth-unrippled-twist-flex/results/R6-fixed-metric-c2-collar-closure.md)已有同一五次Hermite基、完整Cartesian二jet、固定g和共同定义域C²收敛要求，以及**精确等距**参考面的曲率预算。本条新接口是对仅近似等距的基底保留完整Hessian费用，并给同一Hermite基的较紧通用常数。第5节给一个精确定义的有限圆cuff候选，不将其识别为已有固定g。

## 2. 一般参考浸入的完整扰动定理

设 $g$ 是二维域上的固定正定 $C^1$ 度量，$Y_0,C$ 是取值 $\mathbb R^3$ 的 $C^2$ 映射，$Y=Y_0+C$。一阶算子范数及二阶输入向量的长度全部按同一 $g$ 计算。设
$$
\|Y_0^*\delta-g\|_{\mathrm{op},g}\le\varepsilon<1,\qquad
\|dC\|_{\mathrm{op},g}\le\eta<\mu:=\sqrt{1-\varepsilon},
$$
$$
|\operatorname{Hess}_g C(v,v)|\le\zeta |v|_g^2,\qquad
\lambda:=\mu-\eta>0.
$$

**定理227.1。** $Y$ 为浸入，且
$$
|dY(v)|\ge\lambda|v|_g,\qquad
\|Y^*\delta-g\|_{\mathrm{op},g}
\le\varepsilon+2\sqrt{1+\varepsilon}\eta+\eta^2.
\tag{227.1}
$$
若完整向量协变Hessian满足
$$
|\operatorname{Hess}_gY_0(v,v)|\le H_0|v|_g^2,
$$
则所有主曲率的绝对值至多
$$\kappa_Y\le\frac{H_0+\zeta}{\lambda^2}.\tag{227.2}$$

更精细地，若 $Y_0$ 的实际主曲率绝对值至多 $B_0$，并且其旧切空间投影满足
$$
|P_{T_0}\operatorname{Hess}_gY_0(v,v)|\le T_0|v|_g^2,
$$
则
$$
\boxed{\kappa_Y\le
B_0\left(\frac{\mu}{\lambda}\right)^2+
\frac{(\eta/\mu)T_0+\zeta}{\lambda^2}.}
\tag{227.3}
$$

### 证明

旧Gram界给
$$
\mu|v|_g\le|dY_0v|\le\sqrt{1+\varepsilon}|v|_g.
$$
三角不等式给新沉浸下界。展开
$|dY_0v+dCv|^2-g(v,v)$，旧误差、交叉项和平方项分别由
$\varepsilon,2\sqrt{1+\varepsilon}\eta,\eta^2$ 控制。对称Gram差的算子范数由单位向量二次型确定，故得 (227.1)。

取新单位法向 $n$。第二基本形式为
$$II_Y(v,v)=n\cdot\operatorname{Hess}_gY(v,v),$$
因为减去的 $g$-Christoffel 项位于新切平面 $dY(TU)$，法向投影为零。分母
$|dYv|^2\ge\lambda^2|v|_g^2$，立即给 (227.2)。

任意旧切空间单位向量 $e=dY_0v$ 的参数原像满足 $|v|_g\le1/\mu$，而
$$
|n\cdot e|=|n\cdot dCv|\le\eta/\mu.
$$
取所有旧切单位向量的上确界即得 $|P_{T_0}n|\le\eta/\mu$。分解
$$
\operatorname{Hess}_gY_0=II_0\,n_0+
P_{T_0}\operatorname{Hess}_gY_0.
$$
其旧法向项的绝对贡献至多 $B_0|dY_0v|^2$，旧切向项至多
$(\eta/\mu)T_0|v|_g^2$。此外
$$
|dY_0v|\le|dYv|+\eta|v|_g
\le(1+\eta/\lambda)|dYv|
=(\mu/\lambda)|dYv|.
$$
加上修正的 $\zeta|v|_g^2$ 后除以新第一基本形式，得到 (227.3)。证毕。

精确等距时 $\varepsilon=0$，诱导联络就是 $g$ 的联络，故 $T_0=0$，恢复原R6形式。近似等距时不能只把旧曲率 $B_0$ 填入精确等距公式；必须支付 $T_0$ 或完整 $H_0$。

## 3. 不能遗漏切向 Hessian 的明确反例

取 $g=dx^2+dy^2$，
$$
f(x)=x+\frac{a(1-\cos(kx))}{k},\quad
0<a<\frac14,\qquad
Y_0=(f(x),y,0),\quad C=(0,0,\delta x).
$$
$f'=1+a\sin(kx)>0$，所以 $Y_0$ 是平面浸入，旧曲率恒零，且
$$
\|Y_0^*\delta-g\|\le2a+a^2
$$
与 $k$ 无关。$\|dC\|=\delta$，$\operatorname{Hess}_gC=0$。固定足够小的
$0<\delta<\sqrt{1-(2a+a^2)}$，全部一阶条件成立。

新曲面是平面曲线 $(f(x),\delta x)$ 沿 $y$ 方向的柱面。在 $x=0$，
$f'=1,f''=ak$，其非零主曲率绝对值为
$$\frac{\delta ak}{(1+\delta^2)^{3/2}},$$
随 $k$ 无界。故仅凭旧曲率、旧Gram误差、修正的一二阶界，不能省略旧场的切向Hessian费用。

## 4. 同一五次 Hermite 接缝的完整常数

令 $r_1=r_0+\ell$，$u=(r-r_0)/\ell\in[0,1]$，定义
$$
h_0=10u^3-15u^4+6u^5,\quad
h_1=-4u^3+7u^4-3u^5,\quad
h_2=(u^3-2u^4+u^5)/2.
$$
对同一个精确定义的周期Cartesian二jet差 $\Delta_0,\Delta_1,\Delta_2$，取
$$C=h_0\Delta_0+\ell h_1\Delta_1+\ell^2 h_2\Delta_2.\tag{227.4}$$
直接代入端点：在 $r_0$，$C,C_r,C_{rr}$ 全零；在 $r_1$，三者准确为
$\Delta_0,\Delta_1,\Delta_2$。角混合导也准确匹配。高度数据、不同框架水平数据及独立补丁不能混称同一个Cartesian二jet。

假设 $\Delta_j$ 的值、角一阶及二阶导的欧氏模均不超过 $A_j$，置
$$K=A_0/\ell^2+A_1/\ell+A_2.$$

### 4.1 基多项式常数的证明

在 $[0,1]$，
$$|h_j|\le1,\qquad |h'_j|\le15/8,\qquad |h''_j|\le6.\tag{227.5}$$
第一组由 $h_0$ 单调从0到1，
$|h_1|=u^3(1-u)(4-3u)\le4u^3(1-u)\le27/64$，
以及 $h_2=u^3(1-u)^2/2\le1/2$ 得到。

$h'_0=30u^2(1-u)^2\le15/8$；
$h'_1$ 的最小值为 $-64/125$、最大为1（驻点 $u=2/5$ 及端点）；
$h'_2=\tfrac12u^2(1-u)(3-5u)$，用 $u^2(1-u)\le4/27$ 和
$|3-5u|\le3$ 得绝对值至多 $2/9$。

$|h''_0|\le10/\sqrt3<6$。
$h''_1$ 的三次Bernstein控制点为 $[0,-8,12,0]$，在 $1/2$ 细分后为
$[0,-4,-1,3/2]$ 与 $[3/2,4,6,0]$，故绝对值不超过6。
$h''_2$ 的三次Bernstein控制点为 $[0,1,-2,1]$，也满足所需界。
Bernstein基非负且和为1，所以控制点包络是整个连续区间的证明，不是采样。

(227.4)于是给（包括已列角导）
$$
|C|\le\ell^2K,\quad |C_r|\le(15/8)\ell K,\quad |C_{rr}|\le6K.
\tag{227.6}
$$

### 4.2 固定轴对称目标度量

使用真实目标材料角 $\theta$，设
$$
g=E(r)\,dr^2+r^2\,d\theta^2,\qquad E=1+w^2,
$$
且 $r\ge r_{\min}>0$、$\ell\le r_{\min}$，
$$
\frac{|w'|}{E^{3/2}}\le B_{\rm mer},\qquad \ell B_{\rm mer}\le1.
$$
若原tail的数据在别的角或径向坐标中，必须先付完整坐标转换，再应用此节。

正交标架 $e_1=E^{-1/2}\partial_r,e_2=r^{-1}\partial_\theta$ 给
$$
\|dC\|_{\mathrm{op}}\le\|dC\|_{\mathrm{HS}}
\le\sqrt{(15/8)^2+(\ell/r_{\min})^2}\,\ell K
\le\frac{17}{8}\ell K.
\tag{227.7}
$$
这里保留了角向的 $1/r$。

完整协变Hessian的标架分量为
$$
H_{11}=C_{rr}/E-E'C_r/(2E^2),
$$
$$
H_{12}=(C_{r\theta}-C_\theta/r)/(r\sqrt E),\qquad
H_{22}=C_{\theta\theta}/r^2+C_r/(rE).
\tag{227.8}
$$
由
$$\frac{|E'|}{2E^2}=
\frac{|w|}{\sqrt E}\frac{|w'|}{E^{3/2}}$$
和 (227.6)，分别得到
$$|H_{11}|\le(63/8)K,\quad |H_{12}|\le(23/8)K,\quad |H_{22}|\le(23/8)K.$$
因此完整向量二阶Hilbert–Schmidt范数至多
$$\frac{\sqrt{63^2+3\cdot23^2}}8K=\frac{\sqrt{5556}}8K<10K.\tag{227.9}$$
取
$$\eta=(17/8)\ell K,\qquad \zeta=10K$$
代入定理227.1，即得一般基底的度量/沉浸/曲率费用。

若基底**精确等距**且实际曲率至多 $B$，则在 $\eta<1$ 时简化为
$$
\text{metric error}\le2\eta+\eta^2,\qquad
\kappa\le\frac{B+10K}{(1-\eta)^2}.
\tag{227.10}
$$
旧证书采用的 $15K$ 仍是合法更保守的常数，不必重算已成证书。

若有限差分数据用于定义 $\Delta_2$，它可成为新有限多项式的准确输入；但与原真实尾二jet的误差必须另外支付。本引理不把有限差分变成连续导数认证。

## 5. 一个精确定义的有限平 cuff 背景

此节是候选定义，不替换既定 $g$。给 $r_0>0$、$r_1=r_0+\ell$、外端高度 $b_1$，以及
$a=w(r_1)>0,d=w'(r_1)$，假设 $a-\ell d/3\ge0$。定义
$$w_c=a(3u^2-2u^3)+\ell d(u^3-u^2).$$
其Bernstein控制点为 $[0,0,a-\ell d/3,a]$，所以非负。取准确原函数
$$
b_c=b_0+\ell a(u^3-u^4/2)+\ell^2d(u^4/4-u^3/3),
$$
$$b_0=b_1-\ell a/2+\ell^2d/12.$$
直接求导得内端一二导零，外端高度/一导/二导恰为 $b_1,a,d$，可以与同一端二jet作C²连接。

置
$$W=\max(a,a-\ell d/3),\qquad
D_c=\max(|d|,|3a/\ell-d|).$$
$w_c'$ 的二次Bernstein控制点为 $[0,3a/\ell-d,d]$，故
$$0\le w_c\le W,\qquad |w_c'|\le D_c.$$
旋转图 $(r\cos\theta,r\sin\theta,b_c(r))$ 的两主曲率为
$w_c'/(1+w_c^2)^{3/2}$ 与 $w_c/(r\sqrt{1+w_c^2})$，因而
$$|\kappa|\le\max(D_c,W/r_0).$$

保存的binary参数可以作为精确有理数消费；本条没有进行该数值消费。
这个构造定义新固定 $g_c=(1+w_c^2)dr^2+r^2d\theta^2$。
一旦采用，精化时必须固定它；不能每级换 $g_c$ 却称同g，也不能不付 $g-g_c$ 就替换旧尾。

## 6. 相位、全局几何和精化边界

同步运输
$$Y_\tau(r,\theta)=R_\tau Y(r,\theta-\tau)$$
与同一线性Hermite操作交换。若上述界覆盖完整角域，则旋转/角平移保持全部费用，使其对所有相位有效。两反射半面仍要沿同一个准确core同步；非轴对称core不允许仅凭反射C²就拆成独立相位。

若cuff的完整Cartesian位置及径向一二jet在共转框中为轴对称值（准确圆base保留，其非轴扰动迹全零），即可与逐点固定帽准确接合。不能由仅高度二jet或canonical端值自动推出完整Cartesian接缝。

局部沉浸和曲率不是全闭面的reach证书。必须按原R11/R16/R24支付连续点对、外补片、帽和全部径向范围。闭合后才能使用完整 $F_0$ 的 $D$、固定 $H$、像集合 $\delta_{\rm hold}$ 和含反射刚体商 $\delta_E$；前缀大小、材料点位移或整体刚体旋转不能替代。

README第5项仍是同一个固定 $g$、参数与时间范围上的加密，等距误差持续下降到机器精度或原求解容差；Hermite常数不能代替该真实精化。若进一步宣称严格C²极限，原R6的共同定义域、完整Cartesian二jet收敛及全局嵌入/reach条件也必须具备；不把额外极限定理擅自加成用户数值完成标准。

## 7. 原文身份和未发生的计算

geometry代理在提交 c2efbb20c47a84adbc76fdca62b250c178d0d7fe 实际读取的Git blob：
| 原文 | Git blob |
| --- | --- |
| 本题R10 | 21786d7e28aa67f679f08fa9c79595757ece847c |
| 本题R11 | 5b25690540ac498eb0eae32da36984f44d3904f6 |
| 本题R16 | 285ca7731ac1af3ee669e40b75cd8e28e576b6c3 |
| 本题R24 | 1d343352ab6118424b87437f874c1606f1f76372 |
| smooth-unrippled-twist-flex 的R6 | 31caaf21744a201889dd289d07ae8ac83253c330 |

本条没有新节点求解、RK、Fourier根、区间消费或CI计算。全部新常数为上述纯分析界，已有数据及成功/失败身份均不改变。
