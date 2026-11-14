# R520 — 第三共同伴随的 whole 偶深核心与真实三输入联合

日期：2026-11-14。**状态：已证明。** 本篇补上 R516 第三条正交伴随 $E_*$ 的两层返回。先在准确的整 theta 度数 $1090152$ 上支付整个中心，再用固定 degree2 参考的非零 CM 拉回定绝对相位。由此得到原四态的完整三伴随矩形；共同偶深下，可以保留 $Y,W,W'$ 三个实际观察并准确返回同一个三输入联合。

原三阶 $T$ 在这个联合上是真正物理变换。原反射 $U$ 和 $Z/T_c$ 条件仍有显示的隐藏项，不能一并省掉。本篇不赋 $E_*$ 一层 scalar，也不把新的推前当作完整中央非零。

## 1. 同一个第三正交轴及完整整覆盖

保 R516 的原六输入 $\xi=(\xi_1,\xi_2,\xi_3,x,c,d_0)^t$、
四态 $(u,v,z,h)$ 和 raw $\rho=-\nu_\sigma^{\otimes6}/84$。
记
$$
\delta=1+2\omega,\quad\omega^2+\omega+1=0,\quad
\lambda=-\bar\pi_0^{-1},\quad\kappa=p\lambda^2,\quad\chi=\chi_{65}.
$$
R516 的原框架
$$
\mathcal F_*=(Y,W,W',Q_0,Q_b,E_*)
\tag{1}
$$
满足
$$
Q_0,Q_b,E_*\perp Y,W,W',\qquad
\operatorname{Gram}(Q_0,Q_b,E_*)=\operatorname{diag}(5,515,216/103).
\tag{2}
$$
它的完整行列式为 $(43200+38880\delta)/7$，原固定坏集之外是单位；
所有逆矩阵和非对角的观察 Gram 都保留。

清同一个实际分母后，
$$
\boxed{
\begin{aligned}
L=721E_*={}&(-19+423\omega)\xi_1+(504+315\omega)\xi_2\\
 &+(-358-481\omega)\xi_3+(309+824\omega)x\\
 &+(11+13\omega)c+(-17+20\omega)d_0.
\end{aligned}}
\tag{3}
$$
准确有
$$
\boxed{N(L)=1090152=2^3\cdot3^3\cdot7^2\cdot103=:N.}
\tag{4}
$$
六个系数模二都非零，六个 odd sigma 半特征的乘积是标准 even
半特征。沿原整方向 $\bar L^{\,t}z$ 变化时，
$$
L=Nz,\qquad E_*=1512z.
\tag{5}
$$
所以实际 theta 度数是 (4)，物理输出的固定尺度 $1512$ 在当前处
为单位，仍用原 $\kappa$。

为了保全其他五个输入，可对 $j=1,\ldots,5$ 取
$$
R_j=\bar L_6\xi_j-\bar L_jd_0,\qquad L_6=-17+20\omega,\quad NL_6=1029.
$$
第一 $L$ 轴与这些行正交，整个框架行列式为
$-\bar L_6^{\,4}N$，也是当前处的单位。
因此标准 $\mathcal S_N$ 的归属是完整原联合的断言。

R496 的十六个来源 $f_t=\mathsf T^{72}_{t,W}\rho$、$t\in E[4]$
在此轴上的平移参数严格为零，因为 $L\perp W$。
它们都在同一个标准 $\mathcal S_N$ 与完整五伴随空间中；
此处没有未支付的第一轴 quarter flat twist。
四态都是这些实际 $f_t$ 的线性组合。

## 2. 完整中心、两层及绝对相位

R496 的原 ray 给
$$
g=\pi_0/\bar\pi_0\equiv91+72\omega\pmod{576},
\qquad g\equiv11+8\omega\pmod{16}.
\tag{6}
$$
原模数中已有 $\pi_0\equiv1\bmod27$；
R513 和 R509 分别给 $\pi_0\equiv2\bmod49$、$\pi_0\equiv1\bmod103$。
所以
$$
g\equiv1\pmod{27\cdot49\cdot103}.
$$
令 $M_{\rm odd}=27\cdot49\cdot103=136269$，则 $N=8M_{\rm odd}$。
同一个完整 CRT 代表是
$$
\boxed{g\equiv272539+1090152\omega\pmod{2180304}.}
\tag{7}
$$
直接在 $\mathbb Z[\omega]/2N$ 中相乘得到
$$
\boxed{g^2\equiv1090153=1+N\pmod{2N},\qquad g^4\equiv1\pmod{2N}.}
\tag{8}
$$
本篇不新增 ray，也不只核去掉中心后的模 $N$ 关系。

在标准 even $\mathcal S_N$ 的完整 canonical Heisenberg 作用中，
乘 $1+N$ 的两个额外中心相位均为一：
新增乘法指数是 $\exp(\pi i(2+N)ab)=1$。
由完整不可约性，$K_{N,p}^2$ 是 whole scalar。
其绝对值由非零固定参考支付。令
$$
\gamma_{103}=11+2\omega,\qquad
a=42\delta\gamma_{103}=294+840\omega,
\qquad Na=545076=N/2.
$$
原 degree2 参考给
$$
\boxed{\Theta(az)\in\mathcal S_N,\qquad K_{N,p}\Theta(az)=-\Theta(az).}
\tag{9}
$$
这是同一个原 $\Theta$ 的固定 CM 单位拉回，普通核心为
$-\lambda$；归一核为 $-1$。在 (9) 上比较待定平方 scalar，
得到整个空间上的绝对身份
$$
\boxed{K_{1090152,p}^{\,2}=I.}
\tag{10}
$$
(10) 不说一层核为 scalar 或恒等；只支付所使用的两层返回。

## 3. 原四态的完整三伴随矩形

定义实际物理缩放
$$
P_{*,n}=I+\frac{\kappa^n-1}{216/103}\bar E_*^{\,t}E_*.
\tag{11}
$$
它固定五个正交方向并将 $E_*$ 乘 $\kappa^n$。
由 (5)、(10) 及第一轴无 twist，对所有十六个 $f_t$、特别四态
$\mu\in\langle u,v,z,h\rangle$，有
$$
\boxed{
\nu_\mu|_{\{E_*\in p^{2c}\}}
=\lambda^{2c}(P_{*,2c})_*\nu_\mu,\qquad c\ge0.
}
\tag{12}
$$
这里仅在完整偶深使用，未把中间的一层来源擅自压回原四态。

与 R513 的两条真实 $\chi\lambda$ 核联立，因 (2) 完全正交，
对任意 $a,b,c\ge0$ 得
$$
\boxed{
\begin{aligned}
&\nu_\mu|_{\{Q_0\in p^a,\ Q_b\in p^b,\ E_*\in p^{2c}\}}\\
&\quad=\chi^{a+b}\lambda^{a+b+2c}
[D_{Q_0,a}D_{Q_b,b}P_{*,2c}]_*\nu_\mu.
\end{aligned}}
\tag{13}
$$
这是原六输入上的真正三深度矩形，保任意另外三个输出的测试。
共同深度为 $2n$ 时，准确简化为
$$
\boxed{
\nu_\mu|_{\{Q_0,Q_b,E_*\in p^{2n}\}}
=\lambda^{6n}(I_{\mathcal R}\oplus\kappa^{2n}I_{\mathcal H})_*\nu_\mu,
}
\tag{14}
$$
其中 $\mathcal R=\operatorname{span}(Y,W,W')$、
$\mathcal H=\mathcal R^\perp$ 是 R516 的实际整直和。
(14) 与所有保持这个分解的真实操作相容，特别与原三阶 $T$ 交换。

## 4. 保留三个原观察的真实联合

令
$$
\bar\nu_\mu=(Y,W,W')_*\nu_\mu
\tag{15}
$$
为真正的三输入推前。对任何只依赖 $(Y,W,W')$ 的连续测试或
紧开域指示，(13) 准确给
$$
\boxed{
\int_{\substack{Q_0\in p^a,Q_b\in p^b\\E_*\in p^{2c}}}
 f(Y,W,W')\,d\nu_\mu
=\chi^{a+b}\lambda^{a+b+2c}
 \int f\,d\bar\nu_\mu.
}
\tag{16}
$$
这里不从两个边际拼出联合，也不使用零质量来源的卷积逆。
raw 联合的完整生成函数就是原乘积的真实限制：
$$
\boxed{
\Phi_\rho(y,w,w')
=-\frac1{84}\prod_{j=1}^6
 \sigma(Y_jy+W_jw+W'_jw').
}
\tag{17}
$$
其他四态仍使用原 canonical $W$ 四挠平移。
(17) 的极化是 R516(11) 的非对角 $G_{\mathcal R}$；
不能把它误记成三个独立一变量 theta 空间的张量乘积。

原三阶变换在这个联合中确实下降为
$$
\boxed{T_{\mathcal R}(Y,W,W')=(Y,W',-\omega^2W-\omega W').}
\tag{18}
$$
因为 R516 的完整六框架使 $T$ 真正块对角，恒有
$(Y,W,W')\circ T=T_{\mathcal R}\circ(Y,W,W')$。
因此六输入来源身份严格推成
$$
\boxed{
(T_{\mathcal R})_*\bar\nu_\rho=\omega\bar\nu_h,\qquad
(T_{\mathcal R})_*\bar\nu_h=-\omega(\bar\nu_\rho+\bar\nu_h).
}
\tag{19}
$$
这与 R509/R515 中 $T$ 不下降到所选四/二维物理坐标的情形不同：
此处使用的是显示的真正不变三维观察空间。

## 5. 所有第一轴算术操作仍用原方向

因为 $\mathcal H$ 与 $Y,W,W',W_2$ 均正交，原第一轴 canonical
CM 纤维、反射、角平均及原算术投影都与 (15)、(16) 交换。
原 $S/T$、合格新线与参考行的完整伴随因此仍有两个真实输出。

这里的“第一 $Y$ 轴”不能被误读为固定原 $W,W'$ 后只改变 $Y$。
可明确用
$$
Z_1=W-\frac{37+3\delta}{34}Y,\qquad
Z_2=W'-\frac{37+3\delta}{34}Y
\tag{20}
$$
作为两个真正 $Y$ 伴随；它们的内部非对角 Gram 保留。
在 $(Y,W,W')$ 坐标中，第一 $Y$ 的实际缩放矩阵由完整
$G_{\mathcal R}$ 给出：
$$
I_3+\frac{a-1}{34}G_{\mathcal R}e_Y^{\,t}e_Y .
$$
所以所有原 CM/投影操作都有实际三维矩阵，非第一输出的变动没有被删除。
第一 $W$ 同理使用它自己的正交伴随。

四态的来源构造 $K_W,F$ 只作用于这些保留方向，其全部中心相位
在三输入中原样保持。原参考行的未知导数与
Mellin 依赖伴随所产生的质量项同样保留。
(16) 本身仍不将任意未投影混合 $Y/W$ 单位管赋中央零。

## 6. 与 R515 两平面坐标的准确比较

为与 R518 的原 sigma carry 接合，R515 的两个原伴随
$E_{41554}$、$K_{113918}$ 中，准确有
$$
\boxed{
E_*=\frac{3+8\omega}{1106}
\left(E_{41554}+\frac{233+24\omega}{721}K_{113918}\right).
}
\tag{21}
$$
附证书在原六个输入上逐项验证，不只比较两个范数。
(21) 给出 $E_*$ 深条件在原 carry 坐标中的真实线性式；
不能用“$E$ 深”或“$K$ 深”单独替换它。

R510/R515 的 $Y/B_{15}$ 平面在 $\mathcal R$ 中。
故它的任何已付 raw 压深词都与 (11)、(13) 的全部共同伴随
缩放交换。R516 已给完整像格直和及交集公式，现在可以把其中
第三正交伴随的偶深事件也真实加入。
原逆词观察仍保留；R518 的有限多项式测试若含 (21) 中的变量，
须沿同一个矩阵逐次转置。

## 7. Z、Tc 与 U 的隐藏项仍明确保留

原 $T_c=\gamma Y-34x$ 在完整 (1) 中为
$$
\boxed{
\begin{aligned}
T_c={}&\left(-\frac{97}{36}-\frac{283\delta}{216}\right)Y
+\left(-\frac{1751}{1512}+\frac{34\delta}{63}\right)W\\
&+\frac{11713+1343\delta}{3024}W'
+\frac{1751(1+4\delta)}{756}E_* .
\end{aligned}}
\tag{22}
$$
它没有 $Q_0,Q_b$ 项，但最后一项非零。
$Z=(27Y+\bar\gamma T_c)/34$ 也含 $E_*$。
因此原 $B_0$ 的 $Z/T_c$ 单位条件和 R497 的正伴随测试不能在
(16) 中被当成只依赖保留三输入的对象。
有限多项式可按真实 $E_*$ 次数加权推前；单位指示仍保完整线性条件。

原反射法向 $C$ 在同一框架中也保
$$
\frac{-11+5\delta}{70}Q_0+
\frac{-31+23\delta}{3605}Q_b+
\frac{-485-421\delta}{3024}E_*
$$
这三个显示的隐藏项。故 $U=I-2\bar C^{\,t}C$ 仍没有成为三维
物理变换。需要它时继续按 R513/R519 的整个真实积分核处理。

本篇补全了三条共同伴随的已付矩形，给出保旧 $W/W'$ 的准确
三输入联合和真正 $T$ 下降。原完整混管的补偿与跨 $p$ 非零仍待解决。

## 精确证书与依赖

- [原整行、完整中心和三输入框架的 BigInt 证书](../scripts/check-r520-third-common-companion-and-three-input-source.mjs)；
  [全部原矩阵、逆、E/K 与 Tc/C 的运输](../scripts/check-r520-third-common-companion-and-three-input-source.json)。
  同一有理/CM 主体已在 V8 执行；核了完整 CRT、两次中心、
  非零 Theta 锚、六系数比较和整个框架。whole 结论由第2节证明，
  不靠抽样 theta 列或有限素数实验。
- [R516：完整共同三维几何和真实词域](R516-original-rotated-common-companion-cores-and-word-intersections.md)。
- [R513：两条基础 odd 核及所有原四态](R513-original-hidden-odd-cores-and-b0-reflection-kernel.md)。
- [R496：当前模576完整中心和十六来源](R496-original-new-axis-even-core-and-four-source-group.md)。
- [R519：完整 even 中心与原 Theta 绝对定标方法](R519-original-c4-eighth-core-and-complete-b0-transport.md)。
- [R515：原 E/K 两个完整伴随及真实二维来源](R515-original-two-dimensional-st-source-and-same-source-sigma-carry.md)。

主目标尚未完成，继续同一来源的算术测试与真实补域。
