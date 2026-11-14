# R535 — 原三 sigma 的完整 Hesse 五项与真实混合域积分核

日期：2026-11-14。**状态：已证明。** R529–R532 的实际隐藏三输入并不需要留下一个任意 theta 系数。它们在原范数三 Fourier 框架中有一个完整五项 Hesse 张量，保全部输入、canonical 相位和普通测度。由此可以把真实 $E$ 深条件下的 $K$ 单位整逆压成一个显示的四项积分核，仍保 $R_3=J+K$ 的原近相消条件。

本篇支付的是整个来源和全部移权的有限表达。原 $S$ 的权可以使用该五输出核；旧 $W$ 含有被忘去的 $E$，必须继续使用完整三输入张量，不能只用有限个 $E$ 矩代替其 log 权。

## 1. 完整范数三 Fourier 框架

沿用 R529、R532：
$$
a=2+\omega=-\omega\delta,\quad
\delta=1+2\omega,\quad\omega^2+\omega+1=0,\quad
b=17,
$$
$$
\rho_0=-\nu_\sigma^{\otimes6}/84,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1.
\tag{1}
$$
原输入次序仍为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$。

在原 $(\xi_1,\xi_3,c)$ 三输入中取
$$
\boxed{
\begin{aligned}
R&=R_3=\xi_1+\omega^2\xi_3-c,\\
Q&=Q_3=\xi_1+\xi_3-\omega^2c,\\
Z&=Z_3=\xi_1+\omega\xi_3-\omega c.
\end{aligned}}
\tag{2}
$$
完整矩阵及其范数是
$$
M=
\begin{pmatrix}
1&\omega^2&-1\\
1&1&-\omega^2\\
1&\omega&-\omega
\end{pmatrix},\qquad
\boxed{M\bar M^{\,t}=3I,\quad
\det M=(9-3\delta)/2,\quad N(\det M)=27.}
\tag{3}
$$
它在当前处为整自同构；另外三个原输入 $(x,\xi_2,d_0)$ 全保留。
R529 的实际 $E$ 与此前的 $K_3$ 准确关系为
$$
\boxed{
E=\frac a3 Z=\frac{\omega-1}{3}K_3,\qquad
K_3=\omega^2\xi_1+\xi_3-c.
}
\tag{4}
$$
故本篇直接使用三个标准 odd degree3 空间；R529 的 degree9
清分母证明仍然有效，但这里不需要把它当作一个新的独立来源格。

原 $J,K,H_0$ 的真实式是
$$
\boxed{
J=\frac{R-ax}{2},\quad K=\frac{R+ax}{2},\quad
H_0=x+\frac Ra+E,\quad
\eta K=x+\frac Ra,\quad\eta=\frac2a.
}
\tag{5}
$$
特别 $K-J=ax$。本篇始终用完整 $a=2+\omega$，与 R529 中
$(2+\omega)/2$ 的记号区分。

所有 $R,Q,Z$ 均是标准 odd degree3，当前完整
$g_\pi\equiv1\bmod6$，原 $\sigma(\delta z)$ 真实锚给整个空间的
核心为 $\beta$。因此下文每个 degree3 因子逐轴都有该实际核心，
不只是原五项总和的某条边际有核心。

## 2. 三个原 sigma 的完整相位

以 $(r,q,z)$ 为 (2) 的生成变量，原三个 sigma 的生成函数是
$$
\begin{aligned}
&\sigma(r+q+z)
 \sigma(\omega^2r+q+\omega z)
 \sigma(-r-\omega^2q-\omega z)\\
&\hspace{12mm}=
\boxed{-\omega^2\,G(r,q,z),}
\end{aligned}
\tag{6}
$$
其中
$$
\boxed{
G(r,q,z)=
\sigma(r+q+z)
\sigma(r+\omega q+\omega^2z)
\sigma(r+\omega^2q+\omega z).
}
\tag{7}
$$
第二个原因子用 $\sigma(\omega^2u)=\omega^2\sigma(u)$，
第三个原因子用奇负号，故 (6) 的绝对系数为 $-\omega^2$。

定义同一个标准 degree3 基
$$
\boxed{
\mathsf P(u)=\sigma(u)^3,\quad
\mathsf Q(u)=x_\wp(u)\sigma(u)^3,\quad
\mathsf B(u)=-y_\wp(u)\sigma(u)^3=B_3(u).
}
\tag{8}
$$
其首项和 $\mu_6$ 型分别为
$$
\mathsf P=u^3+\cdots\ (3),\quad
\mathsf Q=u+\cdots\ (1),\quad
\mathsf B=1+\frac{3b}{10}u^6+\cdots\ (0).
\tag{9}
$$
它们都属于原同一个整来源格。$\mathsf B$ 是 R522 已付的整卷积单位；
$\mathsf P$ 是三 sigma 卷积，$\mathsf Q=\sigma(\delta u)/\delta$
由完整范数三 sigma 公式可直接看出整性。

## 3. 完整五项 Hesse 身份

准确有
$$
\boxed{
\begin{aligned}
G(r,q,z)={}&
\mathsf B(r)\mathsf B(q)\mathsf P(z)
+\mathsf B(q)\mathsf B(z)\mathsf P(r)
+\mathsf B(z)\mathsf B(r)\mathsf P(q)\\
&-3\mathsf Q(r)\mathsf Q(q)\mathsf Q(z)
-3b\,\mathsf P(r)\mathsf P(q)\mathsf P(z).
\end{aligned}}
\tag{10}
$$

这是一个全函数证明。三个生成方向的完整 Gram 是 $3I$，
各有三个 odd 系数，故 (7) 确在同一个
$\mathcal S_3^{\rm odd}\otimes\mathcal S_3^{\rm odd}
\otimes\mathcal S_3^{\rm odd}$ 中，没有隐藏 cross twist。
同时 $\mu_6$ 作用的总型为 $3$。在 (8) 的 $27$ 个基张量中，
型为 $3$ 的恰好只有五个：
$$
(0,0,3),\ (0,3,0),\ (3,0,0),\ (1,1,1),\ (3,3,3).
\tag{11}
$$
因而 (10) 已列出全部可能项，不是从有限 jet 外推任意函数。

(7) 的完整最低齐次式
$$
(r+q+z)(r+\omega q+\omega^2z)(r+\omega^2q+\omega z)
=r^3+q^3+z^3-3rqz
$$
固定前四个系数。最后沿 $r=q=z=u$，(7) 恒零。
由 $y_\wp^2=x_\wp^3+b$，
$$
3\mathsf B(u)^2\mathsf P(u)-3\mathsf Q(u)^3
=3b\,\mathsf P(u)^3.
$$
故第五系数必须为 $-3b$。这同时支付其符号与绝对大小。

由 (6) 和原 $-1/84$，整个六输入来源在
$(R,Q,Z,x,\xi_2,d_0)$ 框架内就是
$$
\boxed{
\rho_0=\frac{\omega^2}{84}
 \left[\text{式 (10) 的五个真实乘积测度}\right]
 \otimes\nu_\sigma(x)\otimes\nu_\sigma(\xi_2)\otimes\nu_\sigma(d_0).
}
\tag{12}
$$
(12) 是完整联合身份，允许保原任意混合紧开条件。它没有把两个
边际拼成联合，也没有新增一个未经识别的辅助输入。

## 4. 只忘 E 时保全部其余五输出

把 (10) 的第三变量改为 $z=(a/3)e$，就得到物理 $E$ 的生成函数。
令以下三条两输入来源固定于 $(R,Q)$：
$$
\boxed{
\begin{aligned}
\mathcal L&=\nu_{\mathsf P}\otimes\nu_{\mathsf B}
            +\nu_{\mathsf B}\otimes\nu_{\mathsf P},\\
\mathcal M&=\nu_{\mathsf B}\otimes\nu_{\mathsf B}
            -3b\,\nu_{\mathsf P}\otimes\nu_{\mathsf P},\\
\mathcal N&=\nu_{\mathsf Q}\otimes\nu_{\mathsf Q}.
\end{aligned}}
\tag{13}
$$
它们的质量分别是 $0,1,0$。这不为任何未知中央作判断。

记未乘原 $-1/84$ 的三 sigma 块为 $\nu_{\rm block}$。
其第 $j$ 个 $E$ 矩、保完整 $(R,Q)$ 的推前为
$$
\boxed{
\begin{array}{c|c}
j&(R,Q)_*(E^j\,d\nu_{\rm block})\\ \hline
0&-\omega^2\mathcal L\\
1&-\delta\Omega\,\mathcal N\\
2&0\\
3&-\dfrac{2\delta\omega^2}{3}\Omega^3\,\mathcal M\\
4,5&0\\
6&8b\omega^2\Omega^6\,\mathcal L .
\end{array}}
\tag{14}
$$
这里用的是完整 (10)，不是有限采样。具体数值来自
$$
(a/3)^3=\delta/9,\qquad (a/3)^6=-1/27,
$$
和 (9) 的 $1!$、$3!$、$6!$ 规范。

特别，$E$ 的整个偶部分为
$$
\nu_{\mathsf B((a/3)z)}
 \otimes \bigl(\text{忘 }E\text{ 的原来源}\bigr),
\tag{15}
$$
故完整第六 $E$ 矩等于 $-8b\Omega^6$ 倍第零矩。
这是同一个小 degree3 身份在 (4) 的尺度下的推论，不另作为新结果
编号。

对每个 (14) 的行，真实 $E$ 深度 $n$ 准确再乘
$\beta^n\kappa^{jn}$。另外五个原输出及依赖它们的条件全不动。

## 5. E 深条件下的完整 K 单位整逆核

记
$$
D_j=1+\lambda\kappa^j,\qquad
T_0=x+\frac Ra=\eta K.
\tag{16}
$$
所有 $D_j$ 是 R529 已付的单位。仍用 R529 的同一个整测试
$$
\widehat P_K=
\frac1{216b\Omega^6}
\sum_{j=0}^6\binom6j
 \frac{E^{6-j}T_0^j}{D_j}.
\tag{17}
$$
令 $\Pi=(R,Q,x,\xi_2,d_0)$。把 (14) 逐项代入，并保原
$-1/84$，得到对每个 $n\ge0$ 的整个五输出身份
$$
\boxed{
\begin{aligned}
\Pi_*\{{\bf1}_{E\in p^n}\widehat P_K\,d\rho_0\}
=\frac{\omega^2\beta^n}{18144b\Omega^6}
\Bigg[
&\left(\frac{T_0^6}{D_6}
       -\frac{8b\Omega^6\kappa^{6n}}{D_0}\right)\mathcal L\\
&+\frac{40\delta\Omega^3\kappa^{3n}}{3D_3}T_0^3\,\mathcal M
-\frac{6a\Omega\kappa^n}{D_5}T_0^5\,\mathcal N
\Bigg]\\
&\hspace{7mm}\otimes\nu_\sigma(x)\otimes
 \nu_\sigma(\xi_2)\otimes\nu_\sigma(d_0).
\end{aligned}}
\tag{18}
$$
在右侧，显示的 $T_0$ 多项式乘的是同一个完整联合测度，
因为它同时使用 $R,x$。没有把这个乘法当成只作用一条边际。

四项分别来自 $E$ 次数 $0,6,3,1$；其余三行全函数为零。
例如最后系数用 $\delta\omega=-a$，这解释了 $-6a$ 的准确号。

式 (18) 可附任意依赖 $\Pi$ 的原紧开条件，尤其
$$
\boxed{
K\ {\rm unit}\iff T_0\ {\rm unit},\qquad
R=J+K\in p^m,
}
\tag{19}
$$
以及所有 $Q,\xi_2,d_0,x$ 的独立深度条件。
这些是原同一物理变量中的事件，未由有限矩或两个边际代替。

在 $R\in p^m$、$m\ge1$ 上，
$T_0$ 单位又严格等价于原 $x$ 单位。这是 (19) 的真实单位近相消，
不是对所有 $R$ 免费取消 $K$ 条件。

## 6. 原五深网格的完整解析表达

由 (3)–(4)，原五深一单位事件准确为
$$
\boxed{
\mathcal D_n=
\{R,Q,E,\xi_2,d_0\in p^n,\ x\ {\rm unit}\},
\qquad n\ge1.
}
\tag{20}
$$
$\mathcal L,\mathcal M,\mathcal N$ 的每个 $R,Q$ 因子都在同一个
whole odd3 空间，核心都是 $\beta$；另外两条 sigma 的核心也为
$\beta$。因此 (18) 上的另外四个真实深条件可以逐个完整运输。

令 $\tau=\kappa^n$，保新取值仍名为 $(R,Q,x,\xi_2,d_0)$，置
$$
\boxed{
T_\tau=x+\frac{\tau R}{a},\qquad
Y_\tau=\bar\gamma x+
 \tau\left(\frac{-1+4\omega}{3}R+\frac{2a}{3}Q
                   +2\delta\xi_2+2d_0\right).
}
\tag{21}
$$
对 $x$ 单位和 $\tau\in p\mathcal O$，这两个量均为单位。
定义作用于任一 $(R,Q)$ 来源 $\mathcal A$ 的完整函数
$$
\mathscr I_{\mathcal A}[F](\tau)=
\int_{x\ {\rm unit}}
 d\log\langle Y_\tau\rangle\,F(R,x)\,
 d\mathcal A(R,Q)\,d\nu_\sigma(x)\,
 d\nu_\sigma(\xi_2)\,d\nu_\sigma(d_0).
$$
于是原实际局部中央准确为
$$
\boxed{
\begin{aligned}
C_{Y,n}
=\frac{\omega^2\beta^{5n}}{18144b\Omega^6}
\Bigg\{&
\mathscr I_{\mathcal L}
 \left[\frac{T_\tau^6}{D_6}
       -\frac{8b\Omega^6\tau^6}{D_0}\right](\tau)\\
&+\frac{40\delta\Omega^3\tau^3}{3D_3}
     \mathscr I_{\mathcal M}[T_\tau^3](\tau)
-\frac{6a\Omega\tau}{D_5}
     \mathscr I_{\mathcal N}[T_\tau^5](\tau)
\Bigg\}.
\end{aligned}}
\tag{22}
$$
这是 (20) 的整个积分，不只是首个非零系数。
五个真实核心因子合为 $\beta^{5n}$；所有原深度与原单位条件已经
在 (18)–(22) 中明确运输。

三条核只使用 $(R,Q,x)$，所以剩余独立 $\xi_2,d_0$ 的零质量
再次证明完整局部质量为零。全部固定尺度的 log 及
$\log\langle x\rangle$ 项由此准确消失。

作为独立归一核查，(22) 的第五阶只使用
$$
\mu_0(\mathsf B)=1,\quad
\mu_1(\mathsf Q)=\Omega,\quad
\mu_3(\mathsf P)=6\Omega^3,
$$
以及两条原 sigma 的第一矩和 $I_1(\sigma)$。
三条贡献分别给
$$
\boxed{
q_3=\frac{5-20\delta}{27783},\quad
q_5=-\frac{80}{64827}-\frac{8\delta}{7203},\quad
q_6=\frac{-7118+24944\delta}{9529569}.
}
\tag{23}
$$
它们严格返回 R529 的整个首五系数。$D_0$ 那一项先有外部
$\tau^6$，而 $\mathcal L$ 与两条 sigma 的最低总正矩为五，
故该项从第十一阶才开始。这里可看见先前首五阶的零项来自哪条
真正来源，而不是把该来源丢掉。

本篇不另登记 R529 已证明的 $v_p(C_{Y,n})=5n$；
(22) 的新增内容是其所有高阶、全部 $D_0$ 项及真实混合域的
固定来源表达。

## 7. 原 W 必须使用完整三输入

在同一完整 Fourier 框架中，原 $Y,W$ 精确为
$$
\boxed{
\begin{aligned}
Y={}&\frac{-1+4\omega}{3}R+\frac{2a}{3}Q
       +\bar\gamma x+2\delta\xi_2+2d_0,\\
W={}&-\frac{2+\delta}{3}R
 +\left(\frac73+\delta\right)Q
 +\frac{-5+\delta}{3}Z
 +\bar\gamma x+2\delta\xi_2+4d_0.
\end{aligned}}
\tag{24}
$$
$Y$ 不含 $E$，故 (18)–(22) 可合法直接使用其完整 Mellin 权。
$W$ 的第三系数非零；换成 $E=(a/3)Z$ 后该系数就是
R529、R532 的 $-2+4\delta/3$。

因此原 $W$ 的 log 或单位条件不能在 (18) 中先忘 $E$。
但它们可以直接代入未忘任何输入的完整五项 (12)。
这时 $E$ 方向也只涉及三个明确的真实因子
$\mathsf B,\mathsf Q,\mathsf P$，而不是一个任意未知 theta 系数；
必须保各因子的完整测度，不能截成表 (14) 的七个低矩。

在 (12) 上的每个原实际正交深条件、反射与已付核心，均按其
物理矩阵作用。这里没有额外断言第一 CM 投影与混合 $W$ 管
交换，也没有把五个乘积源各自赋为已知的算术零行。

## 8. 保留的中央补域

R529 的完整 $S$ carry 仍是同一个
$\Gamma_r^J=\{J\in p^r,K\ {\rm unit}\}$，
并使用整个 $Y_r=Y\circ P_{J,r}^{-1}$。
(18) 可在该 carry 内继续保 $R=J+K$ 的深条件，也可保 (20)
及其真实 $J$ 深像。

完整算术零行包含这些非零小管之外的实际补域。
式 (22) 没有证明该补域为零；原 $W$ 行还必须保 (24) 的全部
隐藏项与 R529 的两个补偿积分。
本篇的新接口是把这些比较放在同一个完整三 sigma 来源及其
显示的有限积分核中，主目标仍需新的实际关系。

## 精确证书与依赖

- [完整 Fourier 框架、五维 theta 型与整个积分核证书](../scripts/check-r535-original-hesse-tensor-and-mixed-carry-kernel.mjs)；
  [全部精确矩阵、七个来源值与独立第五系数](../scripts/check-r535-original-hesse-tensor-and-mixed-carry-kernel.json)。
  同一 BigInt/CM 主体已经在 V8 执行。检查含完整 Gram 与逆、
  $E/K_3$ 识别、五个且仅五个 theta 型、绝对相位、
  表 (14)、旧 $W$ 的完整转置，以及不依赖原六 sigma 混合展开的
  (23) 第二次推导。
- [R532：原 J/A5 完整六轴与真实二维来源](R532-original-j-a5-full-frame-and-rank-two-source.md)。
- [R529：同一 K 单位逆、原近相消域与 S/W 补偿](R529-original-low-j-k-core-and-complete-st-carry.md)。
- [R522：标准 degree3 基、B3 整性与正矩规范](R522-common-degree3-even-factor-and-same-st-positive-test.md)。
