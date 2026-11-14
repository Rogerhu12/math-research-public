# R119：实际 Codazzi 近似场的稳定度量与曲率后验

2026-11-12，Astra-visible-flex-fd2d / root，接 R116。

**结论。** 把实际有限的第二基本形式场代入准确的径向正交标架 ODE，
可定义一张真实位置图。它相对固定旋转度量的完整误差，由 Gauss–Codazzi
残差的两次径向积分控制，**不需要给正曲率 Cauchy 问题假定稳定性**。
下述估计没有随最高 Fourier 模指数增长的因子，也没有要求目标度量 C³。
角导残差另给真实主曲率的上界。所有结论都是明确输入下的后验定理；
当前强目标完整边值解、连续残差界和全局 reach 尚未支付。

## 1. 固定度量、有限场和真实位置的定义

在带状材料域 \([0,L]\times\mathbb R/(2\pi\mathbb Z)\) 取

\[
g=ds^2+a(s)^2du^2,\qquad a>0,\quad a\in C^2,
\quad c=a'/a,\quad K=-a''/a.
\]

给定实函数 \(l,m,n\)。允许 l 只在径向连续，要求 m、n 的一阶径向导数连续；
角方向取足以支持以下导数的连续正则性。有限 Fourier 场和径向共享 jet 的
分段多项式满足这些要求。曲率后验还用到二阶角导及 m_s、n_s 的一阶角导。
**不要求 l_s 或 K_s 存在。**

取周期的准确初始曲线 \(\gamma(u)\) 和定向正交初始标架
\(F_0=(e_{1,0},e_{2,0},N_0)\)。在每个 u 上定义

\[
A=\begin{pmatrix}0&0&-l\\0&0&-m\\l&m&0\end{pmatrix},
\qquad F_s=FA,\quad F(0,u)=F_0(u),
\tag{1}
\]
\[
X(s,u)=\gamma(u)+\int_0^s F(v,u)e_1^{\rm std}\,dv.
\tag{2}
\]

这是给定连续系数的线性 ODE 和积分，定义了实际函数，不是仅列出期望的诱导度量。
A 反对称，故 \(F\in SO(3)\) 准确成立、\(X_s=e_1\) 准确成立。
ODE 唯一性使周期性和适当的 D2 对称准确保留。
在上述角正则性下 X 为 C²，包括径向 C² 的分段接口。
其浮点求值另有数值误差；以下界针对 (1)–(2) 的准确函数。

为避免在 n 接近零的圆领强除以 n，可以把 l、m、n **三者都作为定义数据**。
若实际求解阶段使用 \(l=(m^2+K)/n\)，只是下面 Gauss 残差恰为零的特例。

## 2. 完整残差矩阵

定义材料坐标中的残差

\[
\mathcal G=ln-m^2-K,
\quad \mathcal R_m=m_s-\frac{l_u}{a}+2cm,
\quad \mathcal R_n=n_s-\frac{m_u}{a}-c(l-n).
\tag{3}
\]

令期望的角连接为

\[
B=\begin{pmatrix}
0&-a'&-am\\a'&0&-an\\am&an&0
\end{pmatrix}.
\]

直接乘法及 \(a''=-aK\) 给准确恒等式

\[
H:=BA+A_u-AB-B_s
=a\begin{pmatrix}
0&\mathcal G&\mathcal R_m\\
-\mathcal G&0&\mathcal R_n\\
-\mathcal R_m&-\mathcal R_n&0
\end{pmatrix}.
\tag{4}
\]

因此在欧氏算子范数中

\[
\|H\|_{op}=a\sqrt{\mathcal G^2+\mathcal R_m^2+\mathcal R_n^2}.
\tag{5}
\]

这里不是把 Frobenius 范数误作算子范数：三维反对称矩阵的非零奇异值
均等于其三个独立系数组成向量的长度。

## 3. 角兼容缺陷的无指数控制

令

\[
D=F_u-FB,\qquad C=X_u-ae_2.
\]

对真实 (1)–(2) 求导，逐项消去后得到

\[
D_s=DA+FH,\qquad C_s=D e_1^{\rm std}.
\tag{6}
\]

第二式使用 B 的第一列：\(FB e_1^{\rm std}=a'e_2+amN\)。
它不预先假定 \(X_u=ae_2\)，所以适用于真正的非零离散残差。

假设连续的非负函数 r 满足

\[
\sup_u\sqrt{\mathcal G^2+\mathcal R_m^2+\mathcal R_n^2}\le r(s),
\quad \sup_u\|D(0,u)\|\le d_0,
\quad \sup_u|C(0,u)|\le k_0.
\]

定义

\[
d(s)=d_0+\int_0^s a(v)r(v)\,dv,
\tag{7}
\]
\[
k(s)=k_0+s d_0+\int_0^s(s-v)a(v)r(v)\,dv,
\qquad \eta(s)=k(s)/a(s).
\tag{8}
\]

则整条角圈上

\[
\|D(s,u)\|\le d(s),\qquad |C(s,u)|\le k(s).
\tag{9}
\]

**证明。** 齐次矩阵方程 \(Z_s=ZA\) 的右传播矩阵正交；
右乘它保持算子范数，而 F 也是正交矩阵。
对第一式 (6) 使用变常数公式和 (5)，即得第一界。
对第二式积分再交换二重积分，得到 (8)。
不存在必须用 \(e^{\int\|A\|}\) 放大的步骤。证毕。

这只说明**给定有限场的几何重建及后验**稳定。
它不撤销 R116 的正 K 冻结主符号，不断言用 Cauchy 数据求解 (3)=0 稳定，
也不由一个有限小残差推出存在邻近的准确无限维解。

## 4. 真实诱导度量的完整界

在目标正交坐标 \((\partial_s,a^{-1}\partial_u)\) 中，实际微分的两列为

\[
(e_1,e_2+C/a).
\]

它与正交两列 \((e_1,e_2)\) 的算子距离至多 η，所以

\[
\boxed{\left\|g^{-1/2}(X^*e-g)g^{-1/2}\right\|_{op}
\le 2\eta+\eta^2.}
\tag{10}
\]

若 η<1，最小奇异值至少 \(1-\eta\)，X 因而确为浸入，
其诱导度量相对 g 的最小特征值至少 \((1-\eta)^2\)。
这是由实际 \(X_s,X_u\) 推出的结论，绝非用辅助标架正交替代实际度量。

若初始数据准确兼容，\(d_0=k_0=0\)。例如 R116 的准确闭中央曲线，
取它的准确曲率为 n、m=0、a′=0，即满足此条件。
若使用准确中央曲线但把 n 初值截成有限 Fourier，则必须计入

\[
d_0=a_0\sup_u|n_{\rm curve}(u)-n_{\rm finite}(u)|
\tag{11}
\]

（此式假设中央 m=0、a′=0），而 k0 仍为零。
当前 balanced oval 的 M191 入口诊断并不自动给 (11) 的连续上界；
报告中的采样数只能用于选实际表示阶数。

作为一个透明的**条件预算**，若
\(L\le8/5,\ 2/5\le a\le11/10,\ d_0=k_0=0,\ r\le10^{-10}\)，则

\[
\eta\le \frac{11/10}{2/5}\frac{(8/5)^2}{2}10^{-10}
=3.52\times10^{-10},
\]

由 (10) 得 metric≤7.04000000124e−10<2e−9。
这不是对尚未完成的强目标候选宣布实付预算；须把其真实 L、a 和连续 r 代入。

## 5. 固定计算角不改变后验

实际程序可用任一固定、正向且满足 \(u(\xi+2\pi)=u(\xi)+2\pi\) 的计算角，
记 \(\omega=u_\xi>0\)、\(b=a\omega\)。方程 (3) 中
\(a^{-1}\partial_u\) 换成 \(b^{-1}\partial_\xi\)，
连接矩阵 B、H 和缺陷 D、C 都乘同一个 ω。
径向积分后再除以 b 时，ω 准确消去，故 (8)–(10) 完全不变。

例如 fixed balanced seed 法向角 φ 取
\(u=\operatorname{arc}_{seed}(\phi)/a_0\)、\(\omega=\rho_{seed}/a_0\)。
中央形状参数变化后仍使用**同一个** u(φ)，不能改成每个形状自己的法向角。
尾端口上的材料 Fourier 系数仍是 u 模，应在这个固定 u(φ) 上实际求值。

### 5.1 随径向改变计算角时的两种准确重建

为同时容纳非圆中央与近圆尾，可以取固定指定的平滑映射
\(u=U(s,\xi)\)、\(U_\xi>0\)。它不改变物理 g，但在新坐标中目标为

\[
g=(1+a^2U_s^2)ds^2+2a^2U_sU_\xi\,ds\,d\xi+a^2U_\xi^2d\xi^2.
\tag{15}
\]

对于保存的 \(\widetilde n(s,\xi),\widetilde m(s,\xi)\)，
(3) 中必须使用
\(\partial_s|_u=\partial_s|_\xi-(U_s/U_\xi)\partial_\xi\)、
\(\partial_u=U_\xi^{-1}\partial_\xi\)。
shape 演化因此有明确的 \((U_s/U_\xi)\partial_\xi\) 漂移项。

**第一种定义：物理材料重建。** 反解 \(\xi=\Xi(s,u)\)，
把场作为 \(n(s,u)=\widetilde n(s,\Xi(s,u))\) 等函数，仍准确按 (1)–(2)
沿固定材料 u 重建。§§2–4 原样适用，再把真实图换坐标到 (15) 即可。
这个换坐标的 \(F_s|_\xi\) 含 \(U_sD\)，不能在非零缺陷时把它删去。

**第二种定义：移动连接重建。** 也可直接定义另一张实际近似图：

\[
\widetilde A=A+U_sB,\quad \widetilde B=U_\xi B,\quad
q=(1,aU_s,0)^T,\quad r_\xi=(0,aU_\xi,0)^T,
\]
\[
\widetilde F_s=\widetilde F\widetilde A,\qquad
\widetilde X_s=\widetilde Fq.
\tag{16}
\]

这里 B 始终是材料 u 的矩阵。令
\(D_\xi=\widetilde F_\xi-\widetilde F\widetilde B\)、
\(C_\xi=\widetilde X_\xi-\widetilde F r_\xi\)。
链式法则及 \(U_{s\xi}=U_{\xi s}\) 给

\[
\widetilde B\widetilde A+\widetilde A_\xi-
\widetilde A\widetilde B-\widetilde B_s=U_\xi H,
\quad (D_\xi)_s=D_\xi\widetilde A+\widetilde F U_\xi H,
\quad (C_\xi)_s=D_\xi q.
\tag{17}
\]

最后一式中无额外项，因为
\(\widetilde Bq+q_\xi-\widetilde A r_\xi-(r_\xi)_s=0\)，
这是对称第二基本形式的直接代数恒等式，不要求 (3)=0。
\(\widetilde A\) 仍反对称。若连续全角界为
\(\omega_*(s)\ge\sup U_\xi\)、\(Q_*(s)\ge\sup\sqrt{1+a^2U_s^2}\)，则

\[
d_\xi(s)=d_{\xi,0}+\int_0^s\omega_*a r\,dv,
\qquad k_\xi(s)=k_{\xi,0}+\int_0^s Q_*d_\xi\,dv
\tag{18}
\]

分别包围 \(\|D_\xi\|\) 和 \(|C_\xi|\)。
目标微分在正交标架中的两列由
\(T=\begin{pmatrix}1&0\\aU_s&aU_\xi\end{pmatrix}\) 给出，
实际微分只在第二列加 \(C_\xi\)。因此相对 (15) 的微分误差至多

\[
\eta_\xi(s)=k_\xi(s)\sup_\xi
\frac{\sqrt{1+a^2U_s^2}}{aU_\xi},
\]

完整 metric 再由 \(2\eta_\xi+\eta_\xi^2\) 包围。
有限残差时 (16) 的图一般不同于第一种定义的图；两种方式可各自使用，
但必须保存选择并计算对应误差。不能沿移动 ξ 重建后仍拿正交对角目标检查 E/F/G。
§6 的曲率公式按物理重建给出；若采用 (16)，须使用它自己的实际二阶导数，不能直接移用。

## 6. 从角导残差控制真实曲率

此节只给局部主曲率，不把它冒称为全局 reach。
全在材料 u 坐标中定义，设已有连续上界

\[
\|A_u\|\le\alpha(s),\quad \|B\|\le\beta(s),\quad
\|H_u\|\le h_1(s),\quad h(s)=a(s)r(s),
\]

其中可直接用

\[
\alpha=\sup_u\sqrt{l_u^2+m_u^2},\quad
\beta=a\sup_u\sqrt{c^2+n^2+m^2},
\quad h_1=a\sup_u\sqrt{\mathcal G_u^2+(\mathcal R_m)_u^2+(\mathcal R_n)_u^2}.
\]

令 \(d_{1,0}\ge\sup\|D_u(0)\|\)、\(w_0\ge\sup|C_u(0)|\)，并定义

\[
d_1(s)=d_{1,0}+\int_0^s
\{d\alpha+(\beta+d)h+h_1\}(v)\,dv,
\qquad w(s)=w_0+\int_0^s d_1(v)\,dv.
\tag{12}
\]

对 (6) 求 u 导数，利用 \(F_u=FB+D\)，有

\[
(D_u)_s=D_uA+DA_u+(FB+D)H+FH_u.
\]

再次用正交的右传播矩阵，即得 \(\|D_u\|\le d_1\)；
再积分 \((C_u)_s=D_u e_1^{\rm std}\)，得到 \(|C_u|\le w\)。
仍没有加入 l_s 或 K_s。

设 \(\eta<1\)，实际单位法向为 \(N_X\)。真实二阶导数满足

\[
X_{ss}=lN,
\quad X_{su}-cX_u=amN+D e_1^{\rm std}-cC,
\]
\[
X_{uu}+aa'X_s=a^2nN+aD e_2^{\rm std}+C_u.
\tag{13}
\]

被减去或加入的向量均切向，所以对 N_X 取点积不改第二基本形式。
在目标正交坐标中，它等于
\((N_X\cdot N)\begin{pmatrix}l&m\\m&n\end{pmatrix}+E_{II}\)，
其中

\[
|(E_{II})_{12}|\le P:=\frac{d+|c|k}{a},\qquad
|(E_{II})_{22}|\le Q:=\frac{ad+w}{a^2},\qquad(E_{II})_{11}=0.
\]

因此若 \(S(s)\ge\sup_u\|\begin{pmatrix}l&m\\m&n\end{pmatrix}\|_{op}\)，

\[
\boxed{\max(|\kappa_1|,|\kappa_2|)
\le\frac{S+P+Q}{(1-\eta)^2}.}
\tag{14}
\]

这里使用 \(|N_X\cdot N|\le1\)、\(\|E_{II}\|\le P+Q\)，
以及实际第一基本形式的最小特征值至少 \((1-\eta)^2\)。
式 (14) 包含位置图的不兼容误差，未直接把输入 l、m、n 的特征值当成实际曲率。

## 7. 实际使用范围与仍须完成的接合

对一份固定的共享径向 jet × 完整角模场，(3) 的残差可用原有的
连续多项式/Fourier 区间工具逐盒包围，再准确累积 (7)、(8)、(12)。
不丢真实角模，不把网格最大值直接当连续上界。ODE (1) 使位置定义可复现；
其数值网格需说明位置求值误差，但无需先把整个 ODE 解伪装成有限多项式。

非零 D 意味着即使输入 n、m 在 cut 与某尾端口相等，
**实际**切口位置与两 jet 仍可能有差异；R117 的准确刚体接合只有在它的
准确兼容假设满足时才适用。不得跳过这个接合误差。
若改在一个重叠领内使用实际 C² 几何修正，须另付修正的完整 metric、曲率和跨片条件。

本结果没有提供强目标的全域嵌入、固定帽接合、法球不碰撞、握持保护或刚体商距离。
它给下一份**实际有限解**可直接支付的稳定连续后验，不把条件公式登记为已完成的闭族。
