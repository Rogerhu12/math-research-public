# R262：多宽度能量零点分支仍被一个有序 primitive 面积排除

日期：2026-11-15。**完整纸面有限和与积分身份；没有执行新的 profile 求积、扫描、消元或几何计算。**

本稿消费 [R256](R256-sharp-profile-energy-contrast-and-multiwidth-joint-construction.md) 的准确双参数隐函数分支，证明其指定的高低交错与 Thue–Morse 方向排列虽然支付三矩、完整第三、六能量、整个 $A_{-2,-3}$ 面积及全部 odd 面积条件，仍有 [R257](R257-cumulative-primitive-energy-in-the-complete-positive-negative-Gaussian-area.md) 的真实 $\operatorname{Re}\mathscr Q<0$。结论作用于实际有限正宽的能量零点分支，不只作用于 leading 根。

这不是所有多宽度圆的障碍。新的限制来自该具体方向排列的累计 imaginary primitive；它不否定 R256 已证明的建设性结论，也不允许删除 [R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md) 的其余有序面积条件。

## 1. 实际分支与准确剩余量

沿用 R256：先固定一个足够小的母宽 $h>0$ 和三母包的简单根 $s_h$，再取主宽度 $\delta>0$ 的真实联合根
$(\alpha(\delta),s(\delta))\to(\alpha_0,s_h)$。母包记作
$u=u_{s(\delta),h}$。这里始终先固定 $h$，再将 $\delta$ 取得足够小；没有把两种极限未经证明地互换。

记

$$
m=\int(u'')^2>0,\quad C=\int(u'')^4>0,\quad
\nu=\frac{\int y^2(u'')^2+2\int(u')^2}{m},
$$

$$
\Delta=\iint|y-z|u''(y)^2u''(z)^2\,dy\,dz,
$$

$$
\mathcal L=\int\left[
y^2u''^4-\frac83yu'u''^3+\frac43uu''^3+u'^2u''^2
\right].
\tag{1}
$$

对一个完整合法的 $q=f+ig$，三复矩为零。R257 的真实必要量为

$$
\mathscr Q(q)=\frac12\int[J(q''^2)]^2+
\int\left[x^2q''^4-\frac83xq'q''^3+
\frac43qq''^3+q'^2q''^2\right].
\tag{2}
$$

它等于相应原交换子外矩的非零常数倍；沿本稿共振 germ 的 Gaussian $A_{1,-3}$ 系数，原乘子也非零。因此 $\mathscr Q\ne0$ 是完整 ruling 的实际障碍，不只是未付账标记。

对 I0 归一的互不交偶母包
$\eta_{w_i,\zeta_i}=w_i^{3/2}u((x-\zeta_i)/w_i)$，
若 $q=\sum_i z_i\eta_{w_i,\zeta_i}$，准确有

$$
\boxed{
\mathscr Q
=-\frac{m^2}{2}\sum_{i<j}z_i^2z_j^2(\zeta_j-\zeta_i)
+\sum_i z_i^4\left[
\frac{C\zeta_i^2}{w_i}+w_i\left(\mathcal L-\frac\Delta4\right)
\right].
}
\tag{3}
$$

这里的 $i<j$ 是真实支撑次序。第一项不是可以从单包自能量略去的交叉项；它来自完整 $\int[J(q''^2)]^2$。

## 2. 完整复制与主宽度只能乘正因子

R256 的每个基本 circle 已准确满足

$$
\int q''^4=0,\qquad \int xq''^4=0,\qquad \int q'q''^3=0.
\tag{4}
$$

因此 (2) 对共同平移不变：平移新增的项为
$2d\int xq''^4+d^2\int q''^4-\frac83d\int q'q''^3$，全为零。三复矩使每个完整副本的 $J(q''^2)$ 真紧，故不同完整副本的 primitive 交叉为零。

R256 的八复制于是使 $\mathscr Q$ 同乘
$\sum_{j=0}^7\gamma_j^4>0$。十二复制中 $g$ 的翻转将 $q$ 变为 $\overline q$；偶数、奇数 binomial 权各和为 $2^{10}$。所以最终量为

$$
\boxed{
\mathscr Q_{\rm final}
=2^{11}\left(\sum_{j=0}^7\gamma_j^4\right)
\operatorname{Re}\mathscr Q_{\rm base}.
}
\tag{5}
$$

将基本包云写为 $x=\zeta_0+\delta y$，全部外宽为
$w_i=\delta r_i$，profile 幅度归一为 $\delta^{3/2}$。由 (2)、(4)，准确有

$$
\mathscr Q_{\rm base}=\delta\,\mathscr Q_{\rm shape}.
\tag{6}
$$

这不是渐近式。共同平移、完整复制以及正 $\delta$ 不提供改变符号的参数。以下在 shape 坐标中证明实部严格为负。

## 3. 固定真实次序的一格分解

记

$$
n=2^{11},\quad
q_0=\frac1{16(1-\alpha)^2},\quad
\beta=\frac{5-\alpha}{1-\alpha},\quad
\frac13\le\alpha\le\frac12.
$$

此处用 $q_0$ 表示宽度比，避免与复 profile $q$ 混淆。沿用 R256 的两间距 $A,B$，有 $B>64A$。令

$$
a=q_0(1-\alpha),\qquad
\ell=2q_0\sqrt\alpha,\qquad
H=2\sqrt\beta.
\tag{7}
$$

低包的 $z_i^2$ 为 $-a+i\ell\epsilon_i$，高包为 $64a+iH\epsilon_k$；恒等 $64a=\beta-1$ 来自真实三矩质量平衡。

每个 $k=0,\ldots,n-1$ 的 cell 包含64个低包和一个高包。令 $c=(n-1)/2$，其 shape 中心为

$$
t^L_{k,l}=64A(k-c)+A(l-31.5),\quad 0\le l\le63,
$$

$$
t^H_k=B(k-c).
\tag{8}
$$

Thue–Morse 符号准确分解为
$\epsilon_{64k+l}=\epsilon_k\epsilon_l$。
R256 的统一间隙估计保证高包始终位于本 cell 的低包 $l=31$ 与 $l=32$ 之间；偏移
$d_k=(B-64A)(k-c)$ 小于 $A/100$。所以以下全部绝对距离按真实同一个次序展开，不是将高包强放到理想中心。

对长度 $N=2^p$ 的 Thue–Morse 序列，记前缀和 $P_j$。其
$P_{2j}=0$、$P_{2j+1}=\pm1$，因而

$$
\sum_{i<j}\epsilon_i\epsilon_j(j-i)
=-\sum_{j=1}^{N-1}P_j^2=-N/2.
\tag{9}
$$

这里的第一个等式把每条间隔计作一次“左总质量乘右总质量”；总质量为零后得到负平方和。另有普通等差和
$\sum_{0\le i<j<N}(j-i)=N(N^2-1)/6$。

## 4. 有序交叉项严格为正

先在一个 cell 内求和。低低 pair 给

$$
A\{43680a^2+32\ell^2\},
\tag{10}
$$

因为 $64(64^2-1)/6=43680$，而 (9) 在 $N=64$ 为 $-32$。

高低 pair 的实质量乘积为 $-64a^2$。64个低中心到高中心的距离和准确为 $1024A$：左右各32项使 $d_k$ 抵消。因此实质量贡献为 $-65536Aa^2$。虚质量的高低交叉为零；两个32项半段的符号零次和一次矩各为零，所以它们同时消掉 $A(l-31.5)$ 与真实偏移 $d_k$。于是同 cell 总实部为

$$
A\{-21856a^2+32\ell^2\}.
\tag{11}
$$

再看不同 cell。第 $k$ 个 cell 的总复质量和一阶中心矩分别为

$$
M_k=iH\epsilon_k,\qquad
J_k=64a(B-64A)(k-c)+iH\epsilon_k B(k-c).
\tag{12}
$$

对 $k<j$，全部跨 cell 的有序距离贡献是
$M_kJ_j-J_kM_j$，实部准确为
$-H^2B\epsilon_k\epsilon_j(j-k)$。
由 (9)，所有 cell 之间贡献 $H^2Bn/2$。结合 (11)，

$$
\boxed{
\operatorname{Re}\sum_{i<j}z_i^2z_j^2(t_j-t_i)
=n\left[A(-21856a^2+32\ell^2)+\frac{H^2B}{2}\right].
}
\tag{13}
$$

这个值在整个参数区间严格为正。事实上
$a\le1/8$、$H^2=4\beta\ge28$、$B>64A$ 给每 cell 括号

$$
>A\left(-\frac{21856}{64}+32\cdot28\right)
=\frac{1109}{2}A>0.
\tag{14}
$$

所以 (3) 第一项的实部严格为负。证明保留了 cell 间真实 imaginary primitive 的长平台，没有将每个 cell 冒称合法完整 block。

## 5. 局部余项的准确归约与正母包因子

记 $U_\alpha=\alpha^2-6\alpha+1<0$。低包
$\operatorname{Re}z_i^4=q_0^2U_\alpha$，高包为
$U_\beta=\beta^2-6\beta+1$，并且

$$
64q_0U_\alpha+U_\beta=0.
\tag{15}
$$

两组中心的平均都为零，方差差为
$V_L-V_H=\nu(1-q_0^2)$。因此 (3) 全部局部项的实部恰为

$$
\boxed{
64nq_0U_\alpha(1-q_0^2)
\left(C\nu-\mathcal L+\frac\Delta4\right).
}
\tag{16}
$$

这一步使用实际三矩已经规定的方差差，不自由重选 $B$。共同中心的常数和一次项由 (4) 消失。

现在使用 R256 的真实母三包。令其固定 even 基本母包为 $v$，外侧中心为 $\pm L$，母宽为 $h$，中央宽为 $sh$；记
$m_v=\int(v'')^2$、$C_v=\int(v'')^4$，并用
$\nu_v,\mathcal L_v,\Delta_v$ 表示同一组原定义。严格不交与偶性给

$$
C=C_vh^{-1}(s^{-1}+2),
$$

$$
\mathcal L=2L^2C_vh^{-1}+h(s+2)\mathcal L_v,
$$

$$
\Delta=8Lm_v^2+h(s+2)\Delta_v.
\tag{17}
$$

最后一式的跨包距离总和是
$2m_v^2(L+L+2L)=8Lm_v^2$；各单包自项才是宽度乘 $\Delta_v$。没有删去母包内部的历史。

与 R256 的
$\nu=\{2L^2+\nu_vh^2(s^2+2)\}/3$ 合并，得到

$$
\begin{aligned}
C\nu-\mathcal L
={}&\frac{2C_vL^2}{3h}(s^{-1}-1)\\
&+h\left[
\frac{C_v\nu_v}{3}(s^{-1}+2)(s^2+2)
-(s+2)\mathcal L_v
\right].
\end{aligned}
\tag{18}
$$

R256 第一层隐函数定理给 $s_h=1+O(h^2)$。因此在该真实简单根上，

$$
C\nu-\mathcal L+\Delta/4
=2Lm_v^2+O(h)>0
\tag{19}
$$

对足够小正 $h$ 成立。现在固定这样的一个 $h$；主隐函数分支
$s(\delta)\to s_h$ 的连续性使 (19) 对充分小正 $\delta$ 继续成立。这里不要求 $s(\delta)-s_h=O(h^2)$ 的双参数一致性；正确顺序是先定 $h$，再定 $\delta$。

(16) 的前因子严格为负，所以第二部分也严格为负。

## 6. 对准确六能量零点分支的结论

(13)—(19) 在 $\alpha$ 的整个紧区间及 $s_h$ 的实际小邻域内成立，未将 $\alpha$ 偷换为仅有的 leading 根。故沿 R256 完整能量方程已经解出的分支，

$$
\boxed{
\operatorname{Re}\mathscr Q_{\rm shape}
=-\frac{m^2n}{2}
\left[A(-21856a^2+32\ell^2)+\frac{H^2B}{2}\right]
+64nq_0U_\alpha(1-q_0^2)
\left(C\nu-\mathcal L+\frac\Delta4\right)<0.
}
\tag{20}
$$

由 (5)、(6)，最终八/十二复制并归一化的实际 circle 仍有
$\mathscr Q_{\rm final}<0$。共振时
$B_1=-k_eh_e\Phi_{p_2}$ 与
$B_{-3}=-k_e(41k_e^4+27)\Phi_{r_0}/(216h_e^3)$
的系数都非零，因此这是真正剩余 Gaussian 面积的非零贡献。

完整第四 ruling 所要求的同一必要面积已经失败。不能将已付六能量与一个全角面积的零升级成 full-ruling 成功，也不能通过共同缩小 $\delta$ 将严格非零当作零：$\delta$ 只给 (6) 的正比例，改变的是大小而不是准确成员资格。

## 7. 下一自由度的位置

本结果只排 R256 指定的微包方向排列及其足够窄的真实联合分支。它不排所有正宽、多形状、多方向圆，也不授这些 profile 之外的一般曲面下界。

共同平移和完整复制已经由 (5) 排除为该符号的修复参数。保原 cell 方向、只改变宽度/共同间距的所述参数族也不能修复 (20)：两项在其合法区间分别为负。后继必须改变真实 ordered quadratic density 或包内方向，而不能继续把 $C_i,S_i$ 视作足够的数据。

一个可审查的建设性接口是分开
$\rho_R=f''^2-g''^2$ 与 $\rho_I=2f''g''$，保留

$$
\operatorname{Re}\int[J(q''^2)]^2
=\int(J\rho_R)^2-\int(J\rho_I)^2.
\tag{21}
$$

其中 $\rho_I$ 的累计平台正是 (12)—(14) 中的额外成本。改变它必须同时保持三复矩、完整第三及原全角条件；本稿不凭 (21) 宣称存在这种变更或已解剩余面积。下一构造应逐条支付这些条件后，再用完整 R259 接口核剩余项。

本稿只消耗已证明公式与有限手算恒等，没有运行、要求重放或增加任何科学预算。

