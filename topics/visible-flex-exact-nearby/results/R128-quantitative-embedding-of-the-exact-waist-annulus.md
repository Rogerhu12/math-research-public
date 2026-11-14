# R128：已证精确腰环带的定量嵌入

2026-11-13。

**状态：已证明，并已执行全部新数值门。** R127 对真实完整方程的
连续验证构造了同一原腰圈初值的精确等距浸入。本篇证明它在

$$
[-10^{-3},10^{-3}]\times\mathbb S^1
$$

上实际是 $C^2$ 嵌入，统一覆盖原辅助参数盒
$|\delta-\delta_5|\le10^{-9}$。证明消费 R127 的全角、全参数和全部
primitive 尾证书；没有把浮点框架、角采样或一个有限 Fourier 解
当成真实曲面，也不使用原参考面的小二阶校正预算。

这是**带边环带**的结论。不同辅助参数仍可能对应不同目标度量，
没有由此得到 README 要求的共同度量闭面可见弯曲族、端帽接合或
全闭面的 reach。

## 1. 同一已经存在的真实分支

R127 已给整个 $0\le r\le T=1/1000$ 上的真实完整 Riemann 解，
其 $C^0/C^1$ 误差由严格仿射屏障控制。R126 的重建给正交标架
$X,Y,\nu$，其中 $\nu=Y\times X$，满足

$$
F_r=\sqrt E\,X,\qquad F_\theta=aY,
$$

$$
X_r=\sqrt E A\nu,\qquad
Y_r=\sqrt E B\nu,\qquad
\nu_r=-\sqrt E(AX+BY),
\qquad A=\frac{K_0+B^2}{C}.
\tag{128.1}
$$

相同初值为 $F(0,\theta)=F_0(\theta)$、$X(0,\theta)=e_z$；
$Y_0$ 是原腰圈的正向平面单位切向，$\nu_0=Y_0\times e_z$。
真实度量准确等于固定的 $g_0=Edr^2+a^2d\theta^2$。
R125/R126 的平面反射构造给负半带并支付腰接缝的 $C^2$。
以下估计用 $|r|$ 表示，因而同时适用于两侧。

### 1.1 实际消费的粗有理门

设 $k=\sqrt{-K_0}$、$p=(B+k)/C$、$q=(B-k)/C$。
R127 的实际报告严格推出

$$
|p|,|q|<M=\frac{2737}{1000},\quad
|p-q|>d=\frac{41}{250},\quad
0<k<\frac{463}{500},
$$

$$
1<\sqrt E<e=\frac{111}{100},\qquad a>1.
\tag{128.2}
$$

这里的 $|p-q|$ 是**实际解**的间隔：报告的候选下界减去两倍真实
$C^0$ 屏障后再向外取粗有理数。具体地，候选间隔大于 $.2436020565$，
真实误差小于 $.0394557828$，因此实际间隔大于 $.16469049$，严格大于
$41/250$。对振幅使用候选上界加真实误差；并未把候选直接当成解。

由 R126 的准确反变换

$$
C=\frac{2k}{p-q},\qquad
B=k\frac{p+q}{p-q},\qquad A=Cpq,
$$

精确有理运算给

$$
|A|<\frac{2k_*M^2}{d}<85,\quad
|B|<\frac{2k_*M}{d}<31,\quad
|C|<\frac{2k_*}{d}<12,
\qquad k_*=\frac{463}{500}.
\tag{128.3}
$$

这些数只是一个很宽的充分档；本证明不要求当前二阶校正很小。

R79/R123 已对原真实背景、包含本参数盒的完整族证明
$F\cdot n>1/2$、$D<2553/1000$。原背景关于原点中心对称，故
$\sup |F|=D/2$。特别同一个原腰圈满足

$$
F_0\cdot\nu_0> s=\frac12,\qquad
|F_0|<R=\frac{13}{10}.
\tag{128.4}
$$

它是原已嵌入面的平面腰圈，因此本身嵌入；正支撑使它绕原点一次。

## 2. 不付旧参考 Hessian 的真实标架控制

从 (128.1)、正交性及 (128.2)–(128.3)，

$$
|X_r|<e\,85<95,\qquad
|Y_r|<e\,31<35,
$$

$$
|\nu_r|=\sqrt E\sqrt{A^2+B^2}
<e\sqrt{85^2+31^2}<101.
\tag{128.5}
$$

最后一门通过比较两个正数的平方精确验证。积分得

$$
|F(r,\theta)-F_0(\theta)|<e|r|\le\frac{111}{100000},
$$

$$
|Y-Y_0|<35|r|,\qquad
|\nu-\nu_0|<101|r|,
\qquad |X-e_z|<95|r|.
\tag{128.6}
$$

对负半带，$F(-r)=Q_zF(r)$、$Y(-r)=Q_zY(r)$、
$\nu(-r)=Q_z\nu(r)$、$X(-r)=-Q_zX(r)$；初始平面向量和 $e_z$
的变换使同样的界成立。

记下标 $h$ 为水平二维投影，$\det_h$ 为平面有向行列式。
因为 $\det_h(F_0,Y_0)=F_0\cdot\nu_0$，有

$$
\begin{aligned}
\det_h(F_h,Y_h)
&\ge \det_h(F_0,Y_0)
 -|F_h-F_0|\,|Y_h|-|F_0|\,|Y_h-Y_0|\\
&>s-eT-R\cdot35T
=\frac{45339}{100000}>0.
\end{aligned}
\tag{128.7}
$$

同理，由 $|\nu_h|\le1$，

$$
F_h\cdot\nu_h
>s-eT-R\cdot101T
=\frac{36759}{100000}>0.
\tag{128.8}
$$

水平半径没有零点，且有准确粗界

$$
\frac{49889}{100000}<|F_h|<\frac{130111}{100000}.
\tag{128.9}
$$

下界使用 $|F_0|\ge F_0\cdot\nu_0>s$。这些都是完整连续曲面上的
界，不是在一个数值框架的节点上检查。

## 3. 柱坐标映射的全局单射

考虑曲面的柱坐标投影

$$
\Psi(r,\theta)=(\phi(r,\theta),z(r,\theta)),\qquad
\phi=\arg F_h\pmod{2\pi},\quad z=F_z.
$$

由 (128.9)，$\phi$ 在整个环带上定义为圆值函数。对每个固定 $r$，

$$
\phi_\theta
=\frac{a\det_h(F_h,Y_h)}{|F_h|^2}
>\frac14.
\tag{128.10}
$$

最后一门只使用 $a>1$ 和
$45339/100000>(130111/100000)^2/4$。
初始腰圈的角映射次数为1；无零点的径向同伦保持这个次数。
因此每个 $\theta\mapsto\phi(r,\theta)$ 是圆周的一次定向微分同胚，
可以全局用 $(r,\phi)$ 代替 $(r,\theta)$。

其完整二维 Jacobian 有准确恒等式

$$
\begin{aligned}
J&:=z_r\phi_\theta-z_\theta\phi_r\\
&=\frac{\sqrt E\,a}{|F_h|^2}
\big[X_z\det_h(F_h,Y_h)-Y_z\det_h(F_h,X_h)\big]\\
&=\frac{\sqrt E\,a}{|F_h|^2}\,F_h\cdot\nu_h
>\frac15.
\end{aligned}
\tag{128.11}
$$

中间的向量恒等式来自 $\nu=Y\times X$。最后一门使用
$\sqrt E>1,a>1$ 及
$36759/100000>(130111/100000)^2/5$。
令 $\theta=\theta(r,\phi)$ 是刚得到的圆周逆，
$\widetilde z(r,\phi)=z(r,\theta(r,\phi))$。链式法则给

$$
\partial_r\widetilde z\big|_\phi
=\frac{z_r\phi_\theta-z_\theta\phi_r}{\phi_\theta}
=\frac J{\phi_\theta}>0.
\tag{128.12}
$$

所以，固定同一个柱角 $\phi$ 后，高度沿 $r$ 严格增加。
若两点的三维像相同，它们的柱角和高度相同；(128.12) 迫使
$r_1=r_2$，再由固定 $r$ 的圆周单射迫使 $\theta_1=\theta_2$。
因此 $F$ 在整个闭环带上单射。

R127 的精确度量给 $F$ 已是 $C^2$ 浸入；紧环带到 Hausdorff 空间的
连续单射是到其像的同胚。因此 $F$ 是 $C^2$ 嵌入，包括两条边界和
反射腰接缝。所有常数在辅助参数盒上统一。

另由 $|X|=1$、$X(0)=e_z$，

$$
X_z=1-\frac{|X-e_z|^2}{2}
>1-\frac{95^2T^2}{2}
=\frac{79639}{80000}>\frac{199}{200}.
$$

结合 $\sqrt E>1$，还得到 $F_{z,r}>199/200$。
这条直观的高度方向门不是用来替代 (128.11) 的完整 Jacobian；
单靠一个正的高度偏导不能自动排除不同角标签之间的自交。

## 4. 原始输入、执行和可复核性

唯一新计算入口为

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
python scripts/fourfold_phase_codazzi_waist_embedding_budget.py \
  --out notes/2026-11-13-R128-waist-annulus-embedding-native.json
```

它已执行成功，17个门全部通过。读取 R127 数字端点使用192位 Arb
有向比较；之后的新预算全部用 `Fraction` 精确有理运算，法向速率门
比较平方而不舍入开方。

消费的冻结报告是
`notes/2026-11-13-Codazzi-continuation-r001-v3-native.json`，SHA256
`0f7aa2f4e9a1df567b209cd873f2af5f6428feafc01a9613fc75a46259fb75eb`。
脚本先核对整个报告 SHA，再核对原 validator、真实系数 provider、
准确有限候选和原对象的 SHA。还明确核对全角、全参数、完整径向 cover
及全部严格屏障成功门。本篇没有把后来改变的文件路径授予旧报告。

原腰圈的正支撑与半径调用同一 R79/R123 已证背景定理；新报告记录
R123 与 R126 证明文本的 SHA。它不是重新采样这些几何输入。
源代码、所有粗有理数、每项门、输入身份和结论范围都在新小报告中。

R128 只把 R127 的**实际存在浸入**升级为明确宽度的嵌入环带，
仍须另行解决远处负区、转折、完整正帽和全局共同度量可见弯曲问题。
