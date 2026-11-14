# R45：正组件的内部 2/3 正则与完整 source/contact 增益

2026-11-12，visible-exact-astra-f6a2。

**状态：下面各命题为完整局部算子结论，当前闭面尚未供应全部输入。**
R35、R36 的自然能量不仅给根端的 $H^{1/3}$ trace；在整个内部还控制
$L^2_xH^{2/3}_\theta$。本篇直接证明这个增益，并用同一个实际
Poisson/Dirichlet realization 得到完整普通源到 conormal 的增强估计。
根端增益为 $1/3$，regular 端增益为 $1/6$；两端 cross 和完整
source-contact 项同时保留。

最后给 R43 的实际 Ai residual 一个可核对的接口，以及同一 Airy
frame 中准确的 Cayley 公式。没有将尚未证明的物理换元或 Ai 强余项
写成当前候选已经通过的门，也没有把有限 positive 组件的结果转授
给尚未接合的无限平尾。

## 1. 固定域、完整实际 form 和角范数

角变量先取周期 $2\pi$，积分用 $d\theta/(2\pi)$；
$\langle D\rangle e_j=\langle j\rangle e_j$。
在 $I=[0,L]$ 上考虑以下两种**已经由真实坐标得到的**自然能量：
$$
\|u\|_{V_\chi}^2=\int_0^L\int_{S^1}
 (|u|^2+|u_x|^2+\chi(x)|u_\theta|^2),
\qquad \chi=x\quad\hbox{或}\quad\chi=x(L-x).
\tag{1.1}
$$
分别使用 R36 与 R35 的真实 trace、零 trace 子空间 $V_{00}$，以及
与角导数和 Fourier 权交换的延拓 $E$。每个端点记
$$
\sigma_i=\begin{cases}1/3,&\text{simple-root 端},\\
1/2,&\text{regular 端},\end{cases}\qquad
X_t=\bigoplus_i H^{t+\sigma_i},\quad
Y_t=\bigoplus_i H^{t-\sigma_i}.
\tag{1.2}
$$
所以 $X_t^*=Y_{-t}$，配对按第一变量线性。
记 $\|E:X_0\to V_\chi\|\le E_0$；R35 可取 $E_0=\sqrt{C_E}$，
R36 可取 $E_0=\sqrt{C_E^{(1)}}$，常数均已有显式式子。

使用同一个实际 Hermitian form $\mathfrak e$。允许真实零阶项，
但它及全部 cross 必须包括在 form 内，而以下 Dirichlet 可逆性
必须确实成立：
$$
|\mathfrak e(u,v)|\le B_0\|u\|_V\|v\|_V,\qquad
G:(V_{00})^*\longrightarrow V_{00},\quad\|G\|\le g.
\tag{1.3}
$$
这里 $PGf=f$ 在 $V_{00}$ 上准确成立；$G$ 是该实际 form 的逆。
R35/R36 纯散度情形可取 $B_0=M$、$g=(1+L^2/\pi^2)/m$。
若已经作 height 变换而出现势，不能照抄纯散度的 $g$，须另供实际值。

对所需有限个整数 $r$，设实际系数的角导数 form
$\mathfrak e_r$ 满足
$$
|\mathfrak e_r(u,v)|\le B_r\|u\|_V\|v\|_V.
\tag{1.4}
$$
例如散度项的 $B_r$ 可由归一矩阵 $\partial_\theta^rC$ 的一致 norm
支付；零阶项也一起计入。径向模型权 $\chi$ 不依赖角变量。

完整 Poisson 与 source contact 仍是
$$
\mathcal H=E-GPE,\qquad
\langle\mathcal K f,h\rangle
=\mathfrak e(Gf,Eh)-\langle f,Eh\rangle.
\tag{1.5}
$$
普通源属于完整 $V^*$；只给 $V_{00}^*$ 上的限制不足以定义第二项。
本篇所有源空间均确实嵌入完整 $V^*$。

## 2. 不带边界条件的内部能量增益

**命题 2.1。** 对整个 $V_\chi$，而非仅 $V_{00}$，有
$$
\boxed{\quad
\|u\|_{L^2_xH^{2/3}_\theta}\le C_I\|u\|_{V_\chi}.\quad}
\tag{2.1}
$$
可以取
$$
C_I^2=1+\max\{3,4/L^2\}\quad(\chi=x),
\tag{2.2}
$$
$$
C_I^2=1+(2/L)^{2/3}\max\{3,16/L^2\}
\quad(\chi=x(L-x)).
\tag{2.3}
$$
这些不是最佳常数，但不要求任何端值为零。

**证明。** 先固定一个角频率 $\lambda=|j|$，写其径向系数为 $v$。
对 $0<h\le L/2$，基本定理和 Cauchy--Schwarz 给
$$
\int_0^h|v(x)|^2dx
\le2\int_h^{2h}|v(x)|^2dx
  +2h^2\int_0^{2h}|v'(x)|^2dx.
\tag{2.4}
$$
这里将 $v(x)$ 与 $v(x+h)$ 比较，径向双重积分中每个点的覆盖长度
至多 $h$，所以最后的系数准确为 $2h^2$。

在单根情形，若 $\lambda^{-2/3}\le L/2$，取
$h=\lambda^{-2/3}$。把 (2.4) 加上 $[h,L]$ 的质量，再乘
$\lambda^{4/3}=h^{-2}$，得
$$
\lambda^{4/3}\int_0^L|v|^2
\le3\int_0^L x\lambda^2|v|^2+2\int_0^L|v'|^2.
\tag{2.5}
$$
否则 $\lambda^{4/3}<4/L^2$，直接以质量项支付。
$j=0$ 也属于后一情形。利用
$(1+\lambda^2)^{2/3}\le1+\lambda^{4/3}$，对所有模求和给 (2.2)。

双根情形令 $d(x)=\min(x,L-x)$，则
$\chi(x)\ge(L/2)d(x)$。记 $\mu=(L/2)^{1/2}\lambda$。
若 $h=\mu^{-2/3}\le L/4$，在左右两端分别应用 (2.4)。两个端部
及用于比较的相邻区间内部不重叠，所以
$$
\mu^{4/3}\int_0^L|v|^2
\le3\int_0^L\mu^2d(x)|v|^2+2\int_0^L|v'|^2
\le3\int_0^L\chi\lambda^2|v|^2+2\int_0^L|v'|^2.
\tag{2.6}
$$
若不满足这个 $h$ 门，则 $\mu^{4/3}<16/L^2$，再次用质量项。
最后 $\lambda^{4/3}=(2/L)^{2/3}\mu^{4/3}$，给 (2.3)。
由光滑函数的能量完备化，结论延伸到整个 $V_\chi$。$\square$

其直接对偶结论是准确的完整源嵌入
$$
\|f\|_{V^*}\le C_I\|f\|_{L^2_xH^{-2/3}_\theta}.
\tag{2.7}
$$
这也是下面 source/contact 增强的关键，不能只使用边界 trace
然后把内部源错误地当作更高阶空间。

## 3. 完整 source contact 是 Poisson 的负伴随

**命题 3.1。** 在上述同一个实际 realization 上，
$$
\boxed{\quad\mathcal K=-\mathcal H^*.\quad}
\tag{3.1}
$$
因此
$$
\|\mathcal K:L^2H^{-2/3}\to Y_0\|
\le C_I E_0(1+B_0g).
\tag{3.2}
$$
这给 root 输出 $H^{-1/3}$，regular 输出 $H^{-1/2}$，即分别相对源
增益 $1/3$ 与 $1/6$。

**证明。** $Eh-\mathcal Hh\in V_{00}$，且实际调和性与 Hermitian
性质给 $\mathfrak e(Gf,\mathcal Hh)=0$。故
$$
\mathfrak e(Gf,Eh)=\mathfrak e(Gf,Eh-\mathcal Hh)
=\langle f,Eh-\mathcal Hh\rangle.
$$
代入完整的 (1.5)，正好剩下 $-\langle f,\mathcal Hh\rangle$。
又有 $\|\mathcal H\|_{X_0\to V}\le E_0(1+B_0g)$，再用 (2.1)
和对偶便得 (3.2)。两个端口从未分离，因此 cross 已包含。$\square$

在纯散度情形，取共同常数端值还原 R35 的精确 charge
$\langle\mathcal Kf,(1,1)\rangle=-\langle f,1\rangle$。
若实际 form 含非零势，仍有 (3.1)，但不能无条件继续使用该常数 charge。

## 4. 有限角正则：正、负全部窗口与明确递推

定义三个非负常数列：
$$
\begin{aligned}
P_0&=E_0(1+B_0g),\\
P_k&=P_0+g\sum_{r=1}^k\binom kr B_rP_{k-r}\quad(k\ge1),\\
D_0&=gC_I,\\
D_k&=g\left(C_I+\sum_{r=1}^k\binom kr B_rD_{k-r}\right)\quad(k\ge1),\\
Z_k&=E_0\left(C_I+\sum_{r=0}^k\binom kr B_rD_{k-r}\right)\quad(k\ge0).
\end{aligned}
\tag{4.1}
$$
再记
$$
A_k=C_I\left(\sum_{r=0}^k\binom krP_r^2\right)^{1/2},\qquad
T_k=\left(\sum_{r=0}^k\binom krZ_r^2\right)^{1/2}.
\tag{4.2}
$$
所有量仅依赖同一实际 form 的已付有限角导数及 $g,E_0,C_I$。

**定理 4.1。** 对每个有相应系数导数预算的整数 $k\ge0$，
$$
\|\mathcal H:X_k\to L^2H^{k+2/3}\|\le A_k,
\tag{4.3}
$$
$$
\boxed{\quad
\|\mathcal K:L^2H^{-k-2/3}\to Y_{-k}\|\le A_k,\qquad
\|\mathcal K:L^2H^{k-2/3}\to Y_k\|\le T_k.\quad}
\tag{4.4}
$$
在任意相邻两个已付整数层之间可用 Hilbert 尺度插值。
于是对所付有限实窗口中的任意 $t$，
$$
\boxed{\quad
\mathcal K_i:L^2H^t\longrightarrow H^{t+2/3-\sigma_i}.\quad}
\tag{4.5}
$$
常数是相邻 (4.4) 常数的相应几何平均。

**Poisson 证明。** 设 $u=\mathcal Hh$。实际角微分给
$$
P\partial_\theta^k u
=-\sum_{r=1}^k\binom kr P_r\partial_\theta^{k-r}u,
\qquad \operatorname{Tr}\partial_\theta^k u=\partial_\theta^k h.
\tag{4.6}
$$
利用同一 $G$ 与 $\mathcal H$，归纳得到
$\|\partial_\theta^r u\|_V\le P_r\|h\|_{X_k}$，$0\le r\le k$。
Fourier 恒等式
$$
\|u\|_{L^2H^{k+2/3}}^2
=\sum_{r=0}^k\binom kr
 \|\partial_\theta^r u\|_{L^2H^{2/3}}^2
\tag{4.7}
$$
与 (2.1) 给 (4.3)；(3.1) 的准确对偶给 (4.4) 第一式。

**正 source 层证明。** 令 $u=Gf$，其全部边界 trace 为零。
对 $f\in L^2H^{k-2/3}$，(2.7) 和真实微分方程给
$$
\|\partial_\theta^r u\|_V\le D_r\|f\|_{L^2H^{k-2/3}},
\qquad 0\le r\le k.
\tag{4.8}
$$
角积分分部及 $E\partial_\theta=\partial_\theta E$ 给完整恒等式
$$
\left\langle\partial_\theta^r\mathcal Kf,h\right\rangle
=\sum_{a=0}^r\binom ra
 \mathfrak e_a(\partial_\theta^{r-a}u,Eh)
 -\langle\partial_\theta^rf,Eh\rangle.
\tag{4.9}
$$
所以 $\|\partial_\theta^r\mathcal Kf\|_{Y_0}\le
Z_r\|f\|_{L^2H^{k-2/3}}$。逐端使用与 (4.7) 相同的恒等式，
即得 (4.4) 第二式。

这些微分等式可先对光滑角数据以差商证明，依靠固定域、实际
Dirichlet 逆和 (4.1) 一致界逐阶取极限；角平滑逼近后延伸到声明的
Hilbert 空间。没有假定退化椭圆问题具有一个未经验证的更大最大域。
负源层的延拓由 (3.1) 唯一确定，并与光滑源的真实通量一致。
两条整数序列 $t=k-2/3$、$t=-k-2/3$ 覆盖所有整数平移层；
相邻层插值便给 (4.5)。$\square$

这里对 regular 端只得到 $t+1/6$，未将其写成 root 的 $t+1/3$。
但各端再乘自己的归一因子 $\langle D\rangle^{-\sigma_i}$ 后，
**所有输出端的总增益都是 $2/3$**：
$$
Q_i^{-1}\mathcal K_i:L^2H^t\to H^{t+2/3},
\qquad Q_i=\langle D\rangle^{\sigma_i}.
\tag{4.10}
$$
这正是保全不同端点 cross 时需要的统一尺度。

## 5. 已支付角权时的同一增强

若实际系数在直接 log 或解析 Fourier 权 $W_\rho$ 上已通过
R35 的完整共轭 form/Dirichlet 门，则上述证明在该权下继续成立。
具体使用实际 $P_\rho=W_\rho PW_\rho^{-1}$ 的有限 form 界
$B_r(\rho)$、真实 $G_\rho$ 界 $g(\rho)$，以及相同的
$E_0,C_I$。模型权、trace、延拓和内部能量 Fourier 分解与 $W_\rho$
均交换，故正层递推直接沿用 (4.1)。

负层不能以 $P_\rho$ 的自伴性作论证；一般它并不自伴。准确关系是
$$
\mathcal K_\rho^*=-\mathcal H_{-\rho}.
\tag{5.1}
$$
所以负层使用**反号权**的 Poisson 常数；正负两个权必须实际同时支付。
这是 R35 的已付权输入的推论，不从只有有限光滑的混合坐标自动产生
一个正 log 宽度。

## 6. 同一个 full 正组件的准确 Ai defect 恒等式

现固定一个 simple-root 端 $i$。在它的实际局部 collar 上给出试解算子
$\mathcal Q_i$，延伸为整个**同一正组件**上的能量函数，其本端 trace
为 $A_i$，其余端 trace 为零。记全部端的真实 outward conormal 为
$C_i$，真实 residual 为 $f_i=P\mathcal Q_i$。则 Dirichlet 唯一性给
$$
\mathcal H(\iota_i A_i h)=\mathcal Q_i h-Gf_i h,
\qquad
\boxed{\quad C_i-\Lambda\iota_i A_i=\mathcal Kf_i.\quad}
\tag{6.1}
$$
$\iota_i$ 是该端的注入；$\Lambda$ 是 full DN，而非本端近似。
即使试解只支撑在本端，右边其他端的 contact 一般仍非零，不能删除。

假设在同一已经准确扣除 normal shear 的 canonical root frame 中，
对非零频率 $\Gamma e_j=q|j|e_j$，$q>0$，试解的两个迹**精确**为
$$
A_i=a_A\Gamma^{-1/3},\qquad
(C_i)_i=c_Aa_A\Gamma^{1/3},\qquad (C_i)_{r\ne i}=0,
\tag{6.2}
$$
其中 $a_A=c\operatorname{Ai}(0)\ne0$、
$c_A=-\operatorname{Ai}'(0)/\operatorname{Ai}(0)>0$。
若有根迹误差，也可使用，但必须显式增加下面相应的归一余项 norm。

为保留 mean，给 $\Gamma e_0=1$；必须真正构造和预算它的实际试解列，
或者把其实际 defect 作为有限输入列另付。含 mean 的一个列虽只有一个
输入频率，其输出仍可能有无穷角频率，不能因此免去输出的光滑范数。

设实际 residual 已有**全矩阵强界**
$$
\|f_i:H^s\to L^2H^{s+2/3}\|\le F_{i,s}
\tag{6.3}
$$
于需要的有限窗口；同样可带已付权。这个输入包含实际 Jacobian、
height、径向 cutoff 和物理角变换，不是单列渐近或若干频率的样本。

令各端 $Q_r$ 为其实际 $\sigma_r$ 阶正 Fourier 归一因子；root 端
在 (6.2) 的坐标中取 $Q_i=\Gamma^{1/3}$。记 full
$B=Q^{-1}\Lambda Q^{-1}$。结合 (4.5)、(6.1) 可得
$$
\boxed{\quad B\iota_i=c_A\iota_i+R_i,
\qquad R_i:H^s\to\bigoplus_r H^{s+4/3}.\quad}
\tag{6.4}
$$
其 $r$ 端 norm 不超过实际归一因子比较常数乘
$|a_A|^{-1}F_{i,s}\|\mathcal K_r:L^2H^{s+2/3}\to
H^{s+4/3-\sigma_r}\|$。Fourier 乘子间的比较由
$\sup_j\langle j\rangle^{\sigma_r}/Q_r(j)$ 等明确 sup 给出。
这也证明 regular 输出的 cross 有相同的归一 $4/3$ 增益。

若整个组件的所有端都是 simple root，逐列并合得到
$$
B=c_AI+R_{4/3}.
\tag{6.5}
$$
若有 regular 端，(6.4) 只给 root 输入列，不能把 regular 自身的主
DN 也改成 $c_A I$。后续消去 regular/tail 网络时，其完整 inverse、
cross 与源仍须保留。

## 7. 同一 Airy frame 的真实 Cayley 与 4/3 余项

本节适用于 (6.5) 的 all-root full realization。记
$$
a=\sqrt3+i,\qquad b=\sqrt3-i.
$$
R39 的准确 Airy 根值恒等式给
$$
u=c\operatorname{Ai}(0)\Gamma^{-1/3}(az_++bz_-),
$$
$$
p=-c c_A\operatorname{Ai}(0)\Gamma^{1/3}(bz_++az_-).
\tag{7.1}
$$
这里的 $p$ 已包括该端的 outward 定向及已扣除的真实 normal shear。
把实际 $p=\Lambda u$ 代入，而不是只比较理想 Ai 图，得到准确关系
$$
\boxed{\quad
z_-=Rz_+,\qquad
R=-(bB+c_Aa)^{-1}(aB+c_Ab).
\quad}
\tag{7.2}
$$

**满射和通量。** $B$ 是同一个 full DN realization 的有界自伴算子。
对实 $t$，
$$
|bt+c_Aa|^2=4(t^2+c_At+c_A^2)\ge3c_A^2.
\tag{7.3}
$$
因此分母满射、逆 norm 至多 $1/(\sqrt3c_A)$；也可直接用 R35 的
非实 Robin 门，因为 $bB+c_Aa=b(B-\tau)$，
$\tau=-c_A(1+i\sqrt3)/2$。分子与分母是互为共轭的同一个实谱函数，
所以 (7.2) 是准确 onto unitary，未用 isotropy 冒充最大性。

在当前实际有限 Sobolev 或权窗口，用 R35/R39 的同一 Robin
bootstrap 支付
$$
J_r=\|(bB+c_Aa)^{-1}:H^r\to H^r\|.
\tag{7.4}
$$
基层 (7.3) 不自动成为所有高阶的相同常数。准确代数给
$$
\boxed{\quad R+I=-2i(bB+c_Aa)^{-1}(B-c_AI).\quad}
\tag{7.5}
$$
故 (6.5) 的强余项真正推出
$$
\|R+I:H^s\to H^{s+4/3}\|
\le2J_{s+4/3}\|R_{4/3}:H^s\to H^{s+4/3}\|.
\tag{7.6}
$$
这在 R43 的同一 Airy frame 中固定了实际正侧的首项为 $-I$，
并说明在满足 (6.3) 的条件下，它不额外贡献一个未列出的 $1/j$ 主相位。
若换 frame，必须同时转换 (7.1)、source 和余项，不能只沿用这个负号。

## 8. 本题仍须供应的具体输入

本篇已经证明内部增益、完整 source/contact 和上面的准确接线。
用于当前候选还须针对同一实际对象供应：

1. 真正的正组件系数比较、whole Dirichlet/Robin realization 及所需
   $B_r,g,E_0$，包括实际 collar 到 regular cut/尾的接线。
2. 真正的 finite-jet Ai 试解、准确根迹和其 residual 的 (6.3) 强界。
   单列 $L^2_x$ 界不能直接推出全矩阵 norm；混合径向角坐标的物理源
   变换也不能仅凭 boundary circle composition 代付。
3. 相应参数 jets、有限低块和真实全域残差因子 Newton 所需的导数预算。

若角周期为 $\ell$，先准确缩放到本篇的 $2\pi$ 圆。物理频率
$qj$ 与 $j$ 的 $H^s$ norm 比较费至多
$\max(1,q,q^{-1})^{|s|}$，而系数、source/Jacobian 和 conormal 必须
按同一坐标变换；不能只修改傅里叶分母。

当前候选的 ordinary metric 样本小并不支付这些门。R45 因而是继续
完成真实全传递的一项实质输入，不是 README 所需精确闭族的完成证书。
