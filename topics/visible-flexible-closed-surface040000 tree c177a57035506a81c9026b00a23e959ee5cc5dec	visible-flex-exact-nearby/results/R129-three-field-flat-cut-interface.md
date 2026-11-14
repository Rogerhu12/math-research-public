# R129：平展切口的原生三场接口、全残差和实际二阶接合

2026-11-12，Astra-visible-flex-fd2d / metric_closure，接 R117、R119、R124、R126、R128。

**状态：下述接口恒等式、退化点接合命题和有限维计数已证明。**
已提供可直接消费独立 \(l,m,n\) 及其真实插值导数的程序，并用 R128 的实际
Cartesian 二阶导、含开放平片的零曲率点和移动计算角作了浮点实现核验。
这不是尚未求出的非圆前缀，也不把有限投影残差当作连续全域证书。

R128 给出大幅度准确平展尾部，但其 \(n\) 在开放角弧上为零。
因此以前消去 \(l=(m^2+K)/n\) 的表示不适用于这一边界。
这里直接保存三场，无需限制 \(l\) 或 \(n\) 的符号。
R119 **已经包含**完整 Gauss 缺陷；本结果补齐三场数据、边界和程序接口，
没有把原有后验重复登记为新结论。

## 1. 定义数据与最少正则性

固定物理材料坐标及旋转度量

\[
g=ds^2+a(s)^2du^2,\qquad a>0,\quad a\in C^2,
\quad c=a_s/a,\quad K_g=-a_{ss}/a.
\tag{1}
\]

以下 \(l,m,n\) 是相对于期望正交材料基的三个**独立定义场**。
对准确兼容图，它们是定向第二基本形式的三个条目。
对有非零残差的有限场，它们是重建 ODE 的输入，不能先称为实际图的曲率。

径向只需 \(l\) 连续，\(m,n\) 连续且分片 \(C^1\)，共享接口值；
所需一阶径向导在各片可积。角向要求下文出现的导数连续或分片可积。
有限 Fourier 场、共享值的分片多项式，以及本文的准确边界提升满足相应角向条件。
曲率后验另用 \(l_{uu},m_{uu},m_{su},n_{su}\)。
**不要求 \(l_s\)、\(K_{g,s}\) 或度量 \(C^3\)。**

如保存的场为原生计算坐标 \((x,\xi)\) 中的插值多项式，必须保存其真实导数。
在节点用方程右端覆盖插值导数，会改变被检验的有限函数。
本接口不作这种覆盖。

## 2. 不除以形状场的完整残差

定义

\[
\begin{aligned}
\mathcal G&=ln-m^2-K_g,\\
\mathcal R_m&=m_s-l_u/a+2cm,\\
\mathcal R_n&=n_s-m_u/a-c(l-n).
\end{aligned}
\tag{2}
\]

唯一分母是正半径 \(a\)。即使 \(l=m=n=0\)，全部表达式仍有定义。
取

\[
A=\begin{pmatrix}0&0&-l\\0&0&-m\\l&m&0\end{pmatrix},\qquad
B=\begin{pmatrix}0&-a_s&-am\\a_s&0&-an\\am&an&0\end{pmatrix}.
\]

直接乘法给

\[
H=BA+A_u-AB-B_s
=a\begin{pmatrix}
0&\mathcal G&\mathcal R_m\\
-\mathcal G&0&\mathcal R_n\\
-\mathcal R_m&-\mathcal R_n&0
\end{pmatrix}.
\tag{3}
\]

若约定 \([v]_\times w=v\times w\)，则

\[
\operatorname{vee}H=(-a\mathcal R_n,a\mathcal R_m,-a\mathcal G),\qquad
\|H\|_{op}=a\sqrt{\mathcal G^2+\mathcal R_m^2+\mathcal R_n^2}.
\tag{4}
\]

这也固定了程序输出 connection_vector 的符号。

按 R119 定义实际图

\[
F_s=FA,\qquad X_s=Fe_1^{\rm std},\qquad F(0,u)\in SO(3),
\tag{5}
\]

并使用准确初始曲线。令 \(D=F_u-FB\)、\(C=X_u-aFe_2^{\rm std}\)。
式 (3) 逐项消去给

\[
D_s=DA+FH,\qquad C_s=De_1^{\rm std}.
\tag{6}
\]

因此，如果 \(r(s)\) 包住式 (2) 三条残差的全角欧氏范数，且初始误差为
\(\|D_0\|\le d_0, |C_0|\le k_0\)，则

\[
\begin{aligned}
d(s)&=d_0+\int_0^s a(v)r(v)\,dv,\\
k(s)&=k_0+s d_0+\int_0^s(s-v)a(v)r(v)\,dv,\\
\left\|g^{-1/2}(X^*e-g)g^{-1/2}\right\|_{op}
&\le 2k(s)/a(s)+(k(s)/a(s))^2.
\end{aligned}
\tag{7}
\]

**证明。** \(A\) 反对称，故 \(F\) 及齐次右传播矩阵都正交。
对 (6) 使用变常数公式和 (4)，再对第二式积分，即得前两界。
实际归一化微分为 \((Fe_1^{\rm std},Fe_2^{\rm std}+C/a)\)，展开 Gram 矩阵即得最后一界。
这里没有把 \(|A|\) 放入 Gronwall 指数，也没有消去 \(\mathcal G\)。
对共享值的分片场，\(B\) 连续且径向绝对连续，(6) 几乎处处成立，
接口无分布跳跃项；同一积分证明原样成立。
由 \(X_{ss}=lFe_3^{\rm std}\) 及角向参数依赖，
在相应角导连续、共享连续 \(l,m\) 的接口，实际图为 \(C^2\)。证毕。

上式的连续 \(r\) 是完成实际 metric 预算时需消费的量；有限网格最大值不是此界。
R124 的角变分法和 R125 的 primitive 法仍可作为同一实际图的替代或组合后验。

## 3. 原生移动坐标和参数导数

允许计算坐标满足

\[
s=S(x),\quad J=S_x>0,\qquad
u=U(x,\xi),\quad \omega=U_\xi>0,\qquad v=U_x/\omega.
\]

这里 \(S\) 不依赖角。物理导数准确为

\[
\partial_s|_u=J^{-1}(\partial_x-v\partial_\xi),\qquad
\partial_u=\omega^{-1}\partial_\xi.
\tag{8}
\]

因此最少输入为

| 数据 | 用途 |
|---|---|
| \(a,a_s,a_{ss}\) | 固定物理目标，不能换成原生 \(x\) 导数 |
| \(J,U_x,U_\xi\) | 计算坐标到物理材料的准确链式法则 |
| \(l,m,n\) | 三个实际有限定义场 |
| \(l_\xi,m_\xi,n_\xi,m_x,n_x\) | 真实插值一阶导；无需 \(l_x\) |

具体为

\[
l_u=l_\xi/\omega,\quad m_u=m_\xi/\omega,\quad n_u=n_\xi/\omega,
\quad m_s=(m_x-vm_\xi)/J,\quad n_s=(n_x-vn_\xi)/J.
\tag{9}
\]

代入 (2) 就是程序 native_residuals。有限残差时实际图按 (5) 沿固定物理 \(u\)
重建；不能沿固定 \(\xi\) 积分后又冒称用了这一图。两种准确重建的区别见 R119 §5.1。

### 3.1 参数 JVP

用 \(\delta\) 表示指定方向导数，允许设计阶段改变物理 profile，但认证前必须冻结所得 \(g\)。

\[
\delta c=\delta a_s/a-a_s\delta a/a^2,\qquad
\delta K_g=-\delta a_{ss}/a+a_{ss}\delta a/a^2.
\]
\[
\begin{aligned}
\delta\mathcal G&=n\delta l+l\delta n-2m\delta m-\delta K_g,\\
\delta\mathcal R_m&=\delta m_s-\delta l_u/a+l_u\delta a/a^2
                  +2m\delta c+2c\delta m,\\
\delta\mathcal R_n&=\delta n_s-\delta m_u/a+m_u\delta a/a^2
                  -(l-n)\delta c-c(\delta l-\delta n).
\end{aligned}
\tag{10}
\]

原生坐标本身也变时，还须使用

\[
\begin{aligned}
\delta v&=(\delta U_x-v\delta\omega)/\omega,\\
\delta l_u&=(\delta l_\xi-l_u\delta\omega)/\omega,\\
\delta m_u&=(\delta m_\xi-m_u\delta\omega)/\omega,\\
\delta m_s&=(\delta m_x-v\delta m_\xi-m_\xi\delta v-m_s\delta J)/J,\\
\delta n_s&=(\delta n_x-v\delta n_\xi-n_\xi\delta v-n_s\delta J)/J.
\end{aligned}
\tag{11}
\]

native_jvp 就是 (11) 后接 (10)，不求逆于 \(n\)，也不把相邻参数的不同物理坐标混用。
所有式子均由商法则和 (8) 直接得到，因而没有未说明的 PDE 线性化假设。

### 3.2 曲率后验所需的角导残差

置

\[
v_\xi=(U_{x\xi}-vU_{\xi\xi})/\omega,
\]
\[
\begin{aligned}
l_{uu}&=(l_{\xi\xi}-l_uU_{\xi\xi})/\omega^2,\\
m_{uu}&=(m_{\xi\xi}-m_uU_{\xi\xi})/\omega^2,\\
m_{su}&=(m_{x\xi}-v_\xi m_\xi-vm_{\xi\xi})/(J\omega),\\
n_{su}&=(n_{x\xi}-v_\xi n_\xi-vn_{\xi\xi})/(J\omega).
\end{aligned}
\tag{12}
\]

因为 \(a,c,K_g\) 不依赖材料角，

\[
\begin{aligned}
\mathcal G_u&=l_un+ln_u-2mm_u,\\
(\mathcal R_m)_u&=m_{su}-l_{uu}/a+2cm_u,\\
(\mathcal R_n)_u&=n_{su}-m_{uu}/a-c(l_u-n_u).
\end{aligned}
\tag{13}
\]

这给 R119 §6 的完整 \(H_u\)，同样无 \(K_{g,s}\) 或径向三阶几何。
native_angular_residuals 直接实现 (12)–(13)。

## 4. 零曲率边界仍可准确作 Cartesian 二阶接合

**命题。** 两张已经准确兼容的 \(C^2\) 图使用相同物理方向、同 \(a,a_s\)，
若切口上位置 \(X\)、定向正交标架 \(F=(e_1,e_2,N)\) 和三场 \(l,m,n\) 都一致，
则它们的完整 Cartesian 二阶 jet 一致，无论 \(n\) 或 \(l\) 是否为零。

**证明。** 兼容的 Gauss–Weingarten 方程直接给

\[
\begin{aligned}
X_s&=e_1,& X_u&=ae_2,\\
X_{ss}&=lN,& X_{su}&=a_se_2+amN,\\
X_{uu}&=-aa_se_1+a^2nN.
\end{aligned}
\tag{14}
\]

右端只有共享数据，无任何形状场分母。证毕。

若两图准确兼容且切口上 \(n,m\) 为**全角准确相同函数**，则一个点的位置和
完整定向框架对齐，就沿整圈对齐：\(F_u=FB\) 是相同连续系数的线性 ODE，
\(X_u=ae_2\) 再给位置。初始旋转 \(Q=F_2F_1^T\) 为 proper rotation，
无需假定切口曲线非平面。若两图另具有 R117 的同一个半周 D2 对称，
框架及位置唯一性同样给 \(QS=SQ,c=Sc\)，其中 \(S=\operatorname{diag}(-1,-1,1)\)。
可在原有定向条件下选择正确轴向符号。

只匹配 \(n,m\) 不能在 \(n=0\) 时从 Gauss 式推出 \(l\)。
因此平展尾部切口保留独立 \(l\) 边界条件正是支付 \(X_{ss}\) 所需的数据，
并非新增一项光滑性门。

### 4.1 有残差前缀必须用实际 jet

有限场按 (5) 定义实际图后，若残差非零，(14) 不是其真实 jet 公式。
用 R124 的准确角变分

\[
r=\operatorname{vee}(F^TF_u),\quad b=F^TX_u,\quad q=b_u
\]

可准确得到

\[
X_s=Fe_1^{\rm std},\quad X_u=Fb,\quad
X_{ss}=F(0,0,l)^T,\quad
X_{su}=F(r\times e_1^{\rm std}),\quad X_{uu}=F(r\times b+q).
\tag{15}
\]

实际 prefix/tail seam 由这些量与尾部实际二jet比较，必要时消费 R126 的有限修正。
不能仅令形式 \(l,m,n\) 相等就称非零残差的两张实际图已经 \(C^2\) 接好。
程序 compatible_cartesian_twojet 明确保留准确兼容前提，不作上述替换。

### 4.2 R128 的原生符号

在 R128 的上半尾取 \(s=a_{\rm cut}-r\)、
\(y=r\sin u\)、\(\kappa(y)=\alpha'(y)\)。其实际切向标架给

\[
N=(0,-\sin\alpha,-\cos\alpha),\quad
l=\kappa\sin^2u,\quad
m=-\kappa\sin u\cos u,\quad n=\kappa\cos^2u.
\tag{16}
\]

代入 (14) 与 R128 直接微分的 \(X_{ss},X_{su},X_{uu}\) 一致。
这些公式在整个固定平领、未弯角弧以及孤立 \(n=0\) 点都成立。
旧 gc_values=[n,m,X,e1,e2,N] 的 14 列布局没有保存 \(l\)；
新的三场记录须独立保存 \(l\)，例如 15 列
[l,m,n,X[3],e1[3],e2[3],N[3]]，不可由旧 14 列强除恢复。

## 5. 有限 DAE 计数、边界提升和真正的退化

这节说明一种实际离散接口的代数计数，不把方程数相等当作可解性或 Newton 可逆性证明。
令角阶为 \(M\)，\(l,n\) 各用均值及 \(M\) 个 \(\cos(2ju)\)，
\(m\) 用 \(M\) 个 \(\sin(2ju)\)。置

\[
d=2M+1,\qquad a_* =M+1,\qquad q=d+a_*=3M+2.
\]

在 \(N\) 个共享径向节点保存 \(qN\) 个系数，有如下方程安排：

| 方程 | 数量 |
|---|---:|
| 每个径向 cell 的两条 Codazzi 积分行 | \(d(N-1)\) |
| 中央及内部节点的低阶 Gauss 行，切口不再另列 | \(a_*(N-1)\) |
| 中央 \(n,m\) 边界 | \(d\) |
| 切口完整 \(l,n,m\) 边界 | \(q\) |
| 实际中央 gap 标量 | \(1\) |

合计为 \(qN+d+1\)。因此加入 \(p=d+1=2M+2\) 个设计参数时为方阵。
当前具体分配是中央 \(M\) 个参数、尾部 \(M+1\) 个弯曲参数和一个 coast 长度 \(T\)。
尾部可用独立 \(A S_9\) 加 \(M\) 个端点 clamped 泡基；
必须保留切口 \(n\) 的均值，不能为凑计数删除它。
例如 \(M=7,N=113\) 给 \(q=23,p=16\)，未知及方程均为 2615。
若省掉 gap，则相应参数数为 \(d\)。

### 5.1 准确边界提升和投影边界不是同一对象

对 R128 准确尾部采用明确的 lifting \((l_*,m_*,n_*)\)，令有限 Fourier
修正 \((\ell,\mu,\nu)\) 在切口全部为零，并定义实际场

\[
(l,m,n)=(l_*,m_*,n_*)+(\ell,\mu,\nu).
\tag{17}
\]

如果提升在切口就是准确尾部的完整函数，那么切口三场满足 \(ln-m^2=0=K_g\)，
故该切口的准确 Gauss 行确为冗余；保留切口修正未知并用 \(q\) 个零边界行，
或消去这 \(q\) 个未知及行，方阵计数相同。
实际全部残差须消费 (17)，包括准确 lifting 的高模和径向导数。

如果只把尾部三场分别截成有限 Fourier 多项式，秩一恒等式一般丢失。
例如准确

\[
l=\sin^2u,\quad m=-\sin u\cos u,\quad n=\cos^2u
\]

满足 \(ln-m^2=0\)，而分别投影到均值后得到 \(l=n=1/2,m=0\)，
其 Gauss 缺陷为 \(1/4\)。这种离散方案也可定义并求解，但省去切口 Gauss
只是边界行替换，不能称为准确冗余；实际 \(\mathcal G\) 和 seam 必须支付。

中央边界也应绑定实际初始曲线。如果只匹配其曲率的有限投影，
仍须按 R119 式 (11) 付真实初始框架角导缺陷 \(d_0\)。

### 5.2 不除以 \(n\) 并不证明 DAE 自动正则

点态 Gauss 代数行的形状微分是

\[
d\mathcal G=n\,dl+l\,dn-2m\,dm
\tag{18}
\]

（度量变化另加 \(-dK_g\)）。在 \(n=0,l\ne0\) 时可局部以该行解 \(n\)，
所以 \(n=0\) 本身不是代数秩退化。只有三场同时为零时，该行对三场的一阶微分为零。
这说明零曲率初始化可能使 Newton 系统困难，不说明准确曲面不存在。
切口采用全三场边界行正好避免在准确平片上保留无信息的 Gauss 行。
在内部如何处理实际奇异 Jacobian，仍属所给离散问题的求解问题。

有限角空间还允许一个明确但非一致的正性结论：若 \(n\ge0\)，且在一个开放角弧上
\(n>0\)，则任一非零有限三角多项式 \(p\) 满足 \(\int n p^2>0\)。
证明是把有限三角多项式乘一个指数变成普通多项式；若在开放弧上为零则有无限多个根，
故只能恒零。因此 Gauss 行关于 \(l\) 的 Galerkin 质量矩阵为正定。
它的最小特征值仍可能很小；在整个平片 \(n\equiv0\) 上此结论不适用。
该观察不能替代实际完整 DAE 的秩分析。

整个处理保持 Gauss 为代数行。没有通过对它作径向微分引入 \(K_{g,s}\)，
也没有制造额外的 \(C^3\) 目标。

## 6. 完整角残差与无混叠乘积

即使三场都是 \(M\) 阶三角多项式，乘积 \(ln-m^2\) 具有至 \(2M\) 阶的模式。
例如取准确 dyadic \(\epsilon=1/8\)，

\[
l=1+\epsilon\cos2u,\quad n=1-\epsilon\cos2u,\quad m=0,
\quad K_g=1-\epsilon^2/2,
\]

则

\[
\mathcal G=-\frac{\epsilon^2}{2}\cos4u=-\frac1{128}\cos4u.
\tag{19}
\]

均值和第一谐波方程准确为零，但完整 Gauss 缺陷不为零。
径向 collocation 收敛、低模 Gauss 收敛均不能删去这个余项。

程序 gauss_fourier 把实 cosine/sine 系数转成有限 Laurent 系数，作完整卷积，
然后返回所有 \(0,\ldots,2M\) cosine 模。
gauss_fourier_jvp 使用

\[
\delta(L*N-M*M)=\delta L*N+L*\delta N-2M*\delta M,
\]

同样不删高模。此程序只直接消费**全部为有限 Fourier 的三场**。
准确 lifting 若含无限角谱，必须再由其解析表示或有界截断余项消费，
不能仅把修正多项式输入该函数就称已覆盖整个 (17)。

后续连续认证可逐径向 cell 先合并准确系数，再用 Bernstein/区间 Fourier 界包住
(2) 和需要的 (13)。从实际共享值/jet恢复的函数才是被认证对象；
不为通过残差而换成方程 RHS。

## 7. 已闭实现和真实核验

实现：

- scripts/fd2d_gc_three_field_residual.py：物理/原生残差、JVP、角导残差、完整 Gauss 卷积、准确兼容二jet接口。
- scripts/fd2d-metric-three-field-interface-check.py：固定随机方向和 R128 实际几何的可重复实现核验。
- notes/2026-11-12-fd2d-metric-three-field-interface-check-01.json：完整参数、输入源 SHA 和结果。

实际运行 session 64888 自然 exit 0，2.923 秒。冻结 R128 provider SHA 为
361df53c8ff6bc5f293098f6642f10a0866e8f12b159987b765783ec28b94cd3。
五个半径、1024 角中有 3408 个三场全零点；所有接口仍正常：

| 实际检查 | 最大误差 |
|---|---:|
| 原材料坐标 \(\mathcal G,\mathcal R_m,\mathcal R_n\) | \(7.11\times10^{-15}\) |
| (14) 与直接 Cartesian 二jet，含三种 phase | \(1.78\times10^{-15}\) |
| 非常数 \(S(x)\)、径向漂移角 \(U(x,\xi)\) 的三条残差 | \(8.00\times10^{-15}\) |
| 同一移动坐标的三条材料角导残差 | \(8.35\times10^{-14}\) |
| 完整 \(M=7\to14\) Gauss 卷积与直接乘积 | \(1.95\times10^{-13}\) |
| 完整 Gauss JVP 与直接乘积导数 | \(2.39\times10^{-13}\) |

同时变化场、物理 profile 和计算 chart 的 JVP 中心差分，在步长
0.02、0.01、0.005、0.0025 下逐次约降四倍，符合明确公式的二阶差分余项。
准确 dyadic 反例 (19) 返回 [0,0,-0.0078125]，投影秩一反例返回 0.25。
这些结果核验实现的符号、链式法则和模式保留；不是连续残差界。

## 8. 当前可直接消费的范围

新的 raw 三场 BVP 可以保存其准确 lifting 定义、全部有限系数及真实径向/角向导数，
由本接口转为物理 \((s,u)\) 的完整残差，再接 R119/R124/R125。
R128 的全幅尾部不需要恢复旧正 \(n\) chart。
强目标仍须实际非圆前缀、实际 seam 和同一闭面的全域几何预算；
本结果没有提前支付这些尚未得到的对象。
