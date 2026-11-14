# R111：同一真实尾条件下的端帽参数比较

2026-11-12，visible-exact-astra-f6a2。

**状态：以下比较定理及计算合同已有完整证明。** 它把旧帽能量证书推广到参数盒所需的新费用，严格归结为有限 body/graft 上的相对 form 变化。§8记录11-13实际执行的完整 body 覆盖和参数误差；完整新原始报告在执行环境断线前未推送，须按保存的源码/参数重建。本文仍不宣布 whole-η 六块装配、全 PDE 逆或非线性收敛已通过。

本篇使用 R88 的同一 grounded 物理角 form、同一切口 $c=1/4$、同一 graft 终点 $R=25/8$、完整根迹和 regular mean。保留所有角频率、均值及同一个真实尾部。代码不会把复参数的虚部删除。

## 1. 保留实际 regular mean 的统一变分空间

记 $B_p(r,\theta)$ 为参数 $p$ 的实际正帽矩阵，定义
$$
 b_{p,\Gamma}(U,V)=
 \int_c^R\!\int_{\mathbb S^1}
   \nabla\overline U^{\,t}B_p\nabla V\,d\theta\,dr
 +\langle U(R),\Gamma V(R)\rangle .
\tag{111.1}
$$
角内积可以采用 R88 的平均约定或统一正交约定，但所有输入和输出须一起转换。
$\Gamma=\Gamma_p\ge0$ 是该参数实际无限尾的算子；$\Gamma1=0$。
regular mean 仍通过实际约束
$$
 U(c)=g,\qquad \langle U(R),e_0\rangle=\xi
\tag{111.2}
$$
保留。不能把 $\Gamma1=0$ 解释成删除 $\xi$ 或其共轭输出 $\lambda$。

令 $\mathcal A(g,\xi)$ 为满足 (111.2) 的完整能量空间。其差空间的内端迹及外端均值均为零；在有限正帽上的椭圆性给 Poincaré/coercivity，故能量极小值存在且唯一。记
$$
 q_{p,\Gamma}(g,\xi)=\min_{U\in\mathcal A(g,\xi)}b_{p,\Gamma}(U,U).
\tag{111.3}
$$
这是包括 regular mean 的完整增广 DN 二次型。共同常数输入可以属于其核；下文不将帽 DN 当作正定矩阵求逆。对有限输入等距注入 $J$，记其压缩为 $C_{p,\Gamma}=J^*S_{p,\Gamma}J$。所有内部及外端非均值仍在完整无限空间中取极小，不作内部 Fourier 截断。

## 2. 固定同一个真实尾

假设有限区域上，对于每个真实 $p$ 都有
$$
 (1-\varepsilon)B_0\le B_p\le(1+\varepsilon)B_0,
 \qquad 0\le\varepsilon<1.
\tag{111.4}
$$
这里 $B_0$ 是准确中心 $\delta_5$ 的 body/graft；$B_p$ 及 $B_0$ 都使用相同材料坐标和 grounded 未知量 $U$。

**定理111.1。** 对每个固定的真实 $\Gamma_p\ge0$，
$$
 (1-\varepsilon)S_{0,\Gamma_p}
 \le S_{p,\Gamma_p}
 \le(1+\varepsilon)S_{0,\Gamma_p}.
\tag{111.5}
$$

**证明。** 在同一 $U$ 上，体积分由 (111.4) 比较；尾项非负，故
$$
 (1-\varepsilon)b_{0,\Gamma_p}(U,U)
 \le b_{p,\Gamma_p}(U,U)
 \le(1+\varepsilon)b_{0,\Gamma_p}(U,U).
$$
在完全相同的 $\mathcal A(g,\xi)$ 中取极小即得 (111.5)。极小者不必相同。regular mean 约束保持不变，因而不漏一个边界自由度。$\square$

旧完整 primal/dual 证书给出了保存的 Hermitian 中心 $C_*$ 和误差 $e_C$。
若它的尾部计算已对每个留在有限试探中的非零频率使用包含真实 $\Gamma_p$ 的区间及其倒数，而 trial/dual 在其余频率的尾迹为零，那么其原证明直接给
$$
 \|C_{0,\Gamma_p}-C_*\|\le e_C
\tag{111.6}
$$
对每个这些区间内的真实尾同时成立。有限试探外的尾仍是非负算子，不能换成负尾或抹掉真实无限自由度。

这是当前 true_tail_energy 的实际合同：原 primal 使用整个真 Robin 球，dual 使用整个真倒数球，mean 单列。虽然 body/graft 在中心计算，该尾误差本来就覆盖 R74 的宽参数盒。因此这里可以比较 $B_p$ 和 $B_0$，同时保持该参数的同一个 $\Gamma_p$。不必选择两个不同尾 realization 再估计其差，也不要求任意两个选择随参数连续。后续非线性邻域或最终等距族仍须分别支付其自己的构造要求；本定理不从这种逐参数线性比较推出连续的非线性选择。

由 (111.5)、正性及 (111.6)，
$$
 \boxed{\quad
 \|C_{p,\Gamma_p}-C_*\|
 \le e_C+\varepsilon(\|C_*\|+e_C).
 \quad}
\tag{111.7}
$$
证明是对自伴差应用 (111.5) 的二次型界，再用
$\|C_{0,\Gamma_p}\|\le\|C_*\|+e_C$。
若已有六块装配费用已经计入 $e_C$，本轮只新增
$\varepsilon(\|C_*\|+e_C)$，不重复计旧费，也不额外乘 $1/(1-\varepsilon)$。
帽到装配变量的实际接线若为 $L$，新装配费再乘 $\|L\|^2$。当前 R105 六块选择的帽未知量正是 $U=w/Y_z$，余弦及两帽配对的 $L$ 为准确等距，故这一接线中 $\|L\|=1$；whole-η 的 $Y,Y_rY$ 只在核心项及剪切项中另行计费。若改用未 grounded 的 $w$ 变量，必须重新付实际 $L$，不能沿用这个因子。

## 3. 复参数 Cauchy 给小区间差

设在一个真实 $(r,\theta)$ 小盒上，$B_z$ 对偏移参数 $z=p-\delta_5$ 在
$|z|\le\rho$ 内全纯。真实分母在覆盖该圆盘的复参数矩形中均须无零点。
选择一个与 $z$ 无关的实可逆矩阵 $T$，并证明
$$
 T^tB_0T\ge mI,\qquad
 \sup_{|z|\le\rho}\|T^tB_zT\|\le M,\qquad m>0 .
\tag{111.8}
$$

**定理111.2。** 对 $|z|\le\eta<\rho$，
$$
 |v^t(B_z-B_0)v|
 \le \frac{M}{m}\frac{\eta}{\rho-\eta}\,v^tB_0v
\tag{111.9}
$$
在实 $z$、实 $v$ 时成立；因此该盒可取
$$
 \varepsilon_{\rm box}
 =\frac{M}{m}\frac{\eta}{\rho-\eta}.
\tag{111.10}
$$

**证明。** $F(z)=T^tB_zT$ 的矩阵 Taylor 系数由 Cauchy 积分满足
$\|F_n\|\le M\rho^{-n}$。于是
$$
 \|F(z)-F(0)\|
 \le M\sum_{n\ge1}(|z|/\rho)^n
 \le M\eta/(\rho-\eta).
$$
写 $v=Tw$，用 $w^tF(0)w\ge m\|w\|^2$ 即得结论。所有函数都来自同一真实无限 primitive；不允许仅对有限角模型证明全纯后，把其圆盘估计授予真实系数。$\square$

$T$ 可随径向盒和角盒改变；它只是该盒内的证明工具。全域取所有完整 cover 上界的最大值。径向公共 spline span 两侧分别使用自己的实际多项式 germ，并凭共同真实低 jet 接合，不跨 knot 假设任意高阶光滑。

## 4. 与真实 grounded 系数匹配的稳定归一化

R88/半径准确消项给
$$
 B=\begin{pmatrix}\alpha&\alpha b\\
                   \alpha b&\alpha b^2+\kappa\end{pmatrix},
 \qquad \alpha,\kappa>0\text{ 在实中心}.
$$
任选准确正数 $A,K$ 及实数 $b_*$，令
$$
 T=\begin{pmatrix}
 A^{-1/2}&-b_*K^{-1/2}\\0&K^{-1/2}
 \end{pmatrix}.
$$
于是
$$
 T^tBT=
 \begin{pmatrix}
 \alpha/A&\alpha(b-b_*)/\sqrt{AK}\\
 \alpha(b-b_*)/\sqrt{AK}&
 \kappa/K+\alpha(b-b_*)^2/K
 \end{pmatrix}.
\tag{111.11}
$$
对真实中心，若 $\alpha/A\ge a_*>0$、$\kappa/K\ge k_*>0$，
$|b-b_*|\sqrt{A/K}\le t_*$，则
$$
 m=\frac{\min(a_*,k_*)}{(1+t_*)^2}
\tag{111.12}
$$
有效。这由
$T^tBT=L^t\operatorname{diag}(\alpha/A,\kappa/K)L$、
$L=\begin{pmatrix}1&(b-b_*)\sqrt{A/K}\\0&1\end{pmatrix}$ 和
$\|L^{-1}\|\le1+t_*$ 得到。对复矩阵 (111.11)，两绝对行和的最大值给 $M$：矩阵对称使1范数和无穷范数相同，因此2范数不超过它们。

$A,K,b_*$ 可由有向盒选取二进制中点；一旦选出就是准确常数。平方根、所有归一化运算和误差仍以有向球处理，不能把浮点开方当作准确平方根。

## 5. 外侧自然 graft 的整个实盒比较

接近 $r=3$ 的自然 graft 角扰动很小，可直接用已证明的完整 Wiener 盒。
设一个真实径向小盒对所有 $p$ 和全部角都有
$$
 \|\overline B^{-1/2}(B_p-\overline B)\overline B^{-1/2}\|
 \le t<1
\tag{111.13}
$$
（等价地可用任意 $T^t\overline BT=I$ 的准确三角归一化）。
则中心也在该盒内，从三角不等式及 $B_0\ge(1-t)\overline B$ 得
$$
 \boxed{\quad
 -\frac{2t}{1-t}B_0\le B_p-B_0\le\frac{2t}{1-t}B_0 .
 \quad}
\tag{111.14}
$$
这里的 $1/(1-t)$ 来自选取参考矩阵；它不是 (111.7) 中额外的帽 DN 放大。
该方法保留所有角频率；它不在角节点之外插值。若盒太宽则真实细分径向区间，不能直接缩小误差。

## 6. 新入口的真实执行合同

scripts/fourfold_phase_cap_parameter_comparison.py 独立实现：

1. 同准确仿射中心加复参数偏移；先分离原始 origin/direction 的真实 scalar germs，再形成参数盒；
2. 所有 scalar Taylor 系数同时保留实部和虚部；旧 fast 内核的实参数序列化不能用于复参数；
3. 真无限单位切向 primitive 的全部误差、真实实角小盒以及参数圆盘一起保留；
4. $a,E/a^2,D/a^2,H/a$ 的真实无零点门，整个实中心 $\alpha,\kappa>0$；
5. 逐完整 body span 使用 (111.10)，自然 graft 使用 (111.14)，逐段检查精确有理连续 cover；
6. 保存准确参数区间、源/输入哈希、全部失败及细分，任何未覆盖段都令 complete=false。

复参数下即便 $r$ 为实数，$K$、能量和几何场仍可能非实；代码显式覆盖旧
real = radial.imag == 0 及实系数序列化分支。角盒内的复参数 Fourier 样本保留自身虚部，再添加完整变动半径，不能将虚部中心强置零。

当前已观察的六块计算允许的充分相对 form 额度约为 $.0114123$；这只用于安排计算预算，不是本篇对 $\varepsilon$ 的实际结论。完整六块报告在断线时未远存，须先按已存五入口重放；随后将本程序真实完成的 $\varepsilon$ 按 (111.7) 接回同一准确装配。本篇没有付完整无限高低 Schur、强角源或非线性收敛。


## 7. 实际已完成的完整 graft 参数证书

**本节已有真实执行结果，不再只是执行合同。** 唯一数值输入为
notes/2026-11-12-positive-family-exterior-entry-jets.json，88457 bytes，
SHA256 6748eb485a77031a3f50caccea5111d913e58aa32ac428e30a7689354cfd8f26。
读取后再次逐 UTF8 SHA256 核对，与 R66 的原始已证入口一致。
它给出全部24个物理 phase mode 的0至4阶 Taylor 系数、
log radius、slope ratio 及真实高度，所有误差均为实际整参数盒的球。

原 R66 区间的中心是
$-7789866024620307/4611686018427387904$，半宽 $1/2000000$。
其与当前 $\delta_5$ 不相同。新程序准确检查
$\delta_5\pm10^{-9}$ 完全包含在这个原盒内；并非将旧中心偷换成新中心。
实际上本节的有限 graft 系数比较覆盖整个原 R66 盒。

### 7.1 同一个自然 graft，不是一个新拟合

把入口的真实 Taylor 系列记为 $l=\log a$、$c=Z'/a^2$、
$\beta_j,\gamma_j$，系数已经除以阶乘。先在截断次数4的形式幂级数环中算
$$
 b_j=\beta_j\exp(-3l),\qquad d_j=\gamma_j\exp(-2l).
$$
这些就是原 NaturalGraft 使用的真实归一化入口 jets 的有向包络。
这里对已认证球作完整加乘和级数指数，不对四舍五入导出值求导。

对 $s\in[0,1/8]$，$\ell=1/8$、$u=s/\ell$、以及
$$
 \chi=(1-u)^5(1+5u+15u^2+35u^3+70u^4),
$$
使用原自然 graft 的准确式
$$
 l(s)=l_0+l_1s+\chi\sum_{j=2}^4l_js^j,\quad
 c(s)=c_0+\chi\sum_{j=1}^3c_js^j,\quad
 \beta_k(s)=e^{3l(s)}\chi b_k(s),\quad
 \gamma_k(s)=e^{2l(s)}\chi d_k(s).
$$
$\chi'(u)=-630u^4(1-u)^4$，故 $0\le\chi\le1$；这严格给出程序使用的
完整高度积分外界 $Z_3\pm\ell a_{\max}^2c_{\max}$。
所有实径向小盒同时传播到真实0、1、2阶 jet。

完整角误差沿用已证明的 real_wiener_form。若 $B,G$ 是 phase 的非负
Wiener jet majorant，则水平 primitive、径向零模和垂直 primitive 分别由
$$
 \cosh(G)e^B-1,\qquad \cosh(G)\cosh(B)-1,\qquad \sinh(G)/4
$$
的0、1、2阶 jet 控制。径向零模使用二次量，未误换成线性 phase norm。
在实际 $E/a^2$ 和曲率中保留这三个完整 primitive 误差及所有交叉项；
缩放的 $D,M,W,H$ 和正 grounded form 随后按原恒等式构成。
实角的 $\sin t$ 用 $[-|t|,|t|]$，$\cos t$ 用 $[1-t^2/2,1]$ 包络。
因此每一个接受的小盒都包含整个无限角函数，并非24模 Fourier 截断的替代品。

### 7.2 有向整数算术及完整连续 cover

所有区间端点都是整数除以 $10^{60}$。加减准确，乘除按端点的整数
floor/ceiling 向外舍入；平方根用整数平方根夹取。
指数先将参数除以128，使其绝对值不超过1。48阶 Taylor 后的完整尾取
$3|x|^{49}/49!$，有效性来自 $e^{|x|}<3$；随后七次完整区间平方。
所有只用于阅读的近似小数不参与任何判定。

每个小盒先证明真实正因子，再按 (111.13)–(111.14) 比较。
相对费太宽的父盒准确二分，直至过门或达到声明的深度12。
最后按精确有理端点排序检查无缺口、无重叠且正好覆盖 $[3,25/8]$。
本次实际执行共643个盒，接受322个盒，全部10个身份/域/覆盖门通过，得到
$$
 \boxed{\quad
 \varepsilon_{\rm graft}
 \le
 \frac{1973600858279055891280594507289254407036793211329911177421}
      {10^{60}}
 <0.001973601<\frac1{500}.
 \quad}
\tag{111.15}
$$
故这个真正的完整 graft 已满足 (111.4)，包括当前 whole-η 盒和全部角频率。

实际在 V8 执行的是保存的同一 certifyGraft 纯 BigInt 核；
Node 文件读取 CLI 尚未运行，不将这两种执行身份混写。
源码为 scripts/fourfold_phase_graft_parameter_exact.mjs，
完整紧凑证书为 notes/2026-11-12-R111-actual-whole-family-graft.json。
紧凑证书逐个保留全部322个准确区间及其有向上界、输入/源码SHA和完整域。
较大的中间归一化盒由同一源可再生；没有经连接器拆块或编码传送它们。

本节最初完成时尚欠 body；以下§8记录后续真实 body 执行。六块装配仍须消费完整恢复后的报告。


## 8. 11-13 实际 body 覆盖及断线恢复合同

在真实 Python/flint 执行器上，以同一源码
SHA256 0879acf59242862833b675c2790d62300c0ed2764146b635d4415ac6eef9b65b，
$\eta=10^{-9}$、$\rho=10^{-4}$、512个 primitive 节点、1024个连续角盒、
192 bit Arb 算术，执行了整个 body 的参数比较。

原两区域任务保留了372个已接受径向盒，无 unresolved/pending box，
准确覆盖
$$
 [1/4,b_0],\qquad b_0=1030198414761001/1125899906842624 .
$$
任务本身未结束，故其 complete=false 保持原样。后续四个独立 body 任务均真实返回
complete=true，其相接端点为
$$
 b_1=6327557476455547/4503599627370496,\quad
 b_2=8680688281756631/4503599627370496,\quad
 b_3=5522539043063071/2251799813685248,\quad b_4=3.
$$
它们逐一覆盖 $[b_{j-1},b_j]$；对应完整报告内的最大相对费分别小于
$1.195029\cdot10^{-5}$、$1.030716\cdot10^{-5}$、
$1.009388\cdot10^{-5}$、$1.003426\cdot10^{-5}$。
四个完整子区域的 complete 判定使用准确有理端点的 cover_complete。
前缀的每个接受盒也须经过同一 $\varepsilon\le1/500$ 门；
三个过宽父盒已细分，不能把失败父盒计入最终覆盖。

因此前缀及四个完整任务的并集准确等于 $[1/4,3]$，且全部角、
全部 $\delta_5\pm10^{-9}$ 上均得到
$$
 (1-1/500)B_0\le B_p\le(1+1/500)B_0.
\tag{111.16}
$$
与已远存的完整 graft 证书 (111.15) 拼接，整个有限正帽均满足 (111.16)。
在同一实际非负无限尾条件下，定理111.1及公式 (111.7) 随即适用。

### 8.1 实际观察与文件保存状态分别记账

notes/2026-11-13-R111-native-body-execution-receipt.json 保存了上述五份输出的
原 SHA256、字节数、准确域、已读最大值、原任务状态和完整重放命令。
它是执行收据，**不是缺失的逐盒原报告**。环境在新 collector 返回以及
这些新 gzip 推送之前再次 unavailable；不得把收据展开成未读取的逐盒数据，
也不宣称 collector 或本次 native graft consumer 已完成。

生成程序、原始仿射输入及§7完整 graft 已在仓库。
恢复时按收据重建并推送原完整 body 数据，随后实际消费到六块与强通量报告。
这个恢复步骤为补齐丢失的科学数据，不额外设置独立审查或重复核验门。
本节已经完成的数学比较只支付参数迁移；全高低 Schur、普通强源、
邻域右逆和非线性收敛仍须继续证明。
