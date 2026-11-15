# R295：实际末格点迫整个平台矩阵为零，及自历史的准确高 jet 分裂

日期：2026-11-15。**完整纸面证明；没有执行科学计算、符号程序、格点枚举或开发测试。**

[R292](R292-zero-platform-periods-and-ordered-second-history-matrix.md)把零平台 period 写成单包自历史与一个固定几何的有序三矩矩阵。本稿先证明：R280 实际五块构造的最右正布局若通过全部零平台必要门，则这个矩阵必须整体为零。原同 $\mathcal F^\star$ 的 profile 修改保持三矩，不能改变这个结论。

再从原 R56/R73 提取每个自历史 $q_i$ 的完整三阶 jet 主项，余项准确降到有限多项式 $C^2$ 观测。主项的 $u^2$ 系数由 $M=0$ 自动消去；其余项不先宣零。给定真实非零偶配对主符号时，任何有限 $C^2$ 纤维观测都不能把这个自历史冻结，因而不能把它未经证明并入低阶 $\mathcal F^+$。

本稿没有证明几何矩阵非零，没有评价新的原积分，也没有把已经支付的 Gaussian 两层 ruling 误作 canonical period 已付。

## 1. 使用 R292 的真实递推

保同一实际几何
$$
M_B=0,\qquad T_B=\kappa\mathfrak H,\quad\kappa\ne0,
\qquad \pi V_B=0,
\tag{1}
$$
其中最后一项是 R210 及后续安装真正构造的 universal whole-period pure 身份。

在从左至右的不交 compact 微包上写
$$
f=\sum a_i u_i,\quad g=\sum b_i u_i,\quad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,
$$
$$
\mu_i=\left(\int(u_i'')^2,\ \int x(u_i'')^2,\
\int[x^2(u_i'')^2+2(u_i')^2]\right).
\tag{2}
$$
以下所有 $a_i\ne0$，正是当前模板。

令 $q_i$ 为 R292 的实际单包自尾二次系数，令 $\mathbf T_B$ 表示其真实双线性型
$\mathcal T_B(\mu,\nu)=\mu^{\mathsf T}\mathbf T_B\nu$。全部零平台通过 $V_d''=V_e''=0$ 的必要充分递推为
$$
R_iq_i+\sum_{j>i}R_j\mu_i^{\mathsf T}\mathbf T_B\mu_j=0,\qquad
T_iq_i+\sum_{j>i}T_j\mu_i^{\mathsf T}\mathbf T_B\mu_j=0.
\tag{3}
$$
消掉真实自项而不假定它为零，得
$$
\boxed{\mu_i^{\mathsf T}\mathbf T_B
\sum_{j>i}(T_iR_j-R_iT_j)\mu_j=0.}
\tag{4}
$$
这里的后缀是实际位于该平台右方的包；全圆总矩为零不能代替它。

## 2. 当前最右正布局强迫 $\mathbf T_B=0$

采用 [R280 §4、§7](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)已经支付的两个编码与五个最后位置。正布局为
$$
i=kL+j,\quad L=17^{11},\quad K=2^{11},
$$
$$
R_i=r_j,\qquad T_i=\epsilon_k\tau_j,\qquad
\epsilon_k=(-1)^{\operatorname{popcount}(k)}.
\tag{5}
$$
从最初把 high 指定为17进制数位和 $0\bmod17$ 的一类，和 R289 使用同一选择。原两种真实幅值为
$$
R_H=8B,\quad T_H=\epsilon_k3B,\qquad
R_L=-B/2,\quad T_L=\epsilon_k B/\sqrt2,\qquad B>0.
\tag{6}
$$
于是
$$
T_LR_H-R_LT_H
=\epsilon_k B^2(4\sqrt2+3/2)\ne0.
\tag{7}
$$

R280 的最右最终块在 $C+D$，确是正布局：其 $D>\ell+4R$，全部支撑严格分开。再取这个最终块中最右的完整八/十二副本，及该副本中的最后 $k=K-1$ 子块。此后没有另一个完整块、复制或 $k$ 子块。

各副本与最后正幅只给这个子块一个共同非零幅因子；若翻 $g$ 号，只把(6)两个 $T$ 同时反号。因此它们不改变(7)或以下零结论。包络、宽度及最终物理位置均用原实际值。

### 2.1 三个准确末 high 和三组 low

$L-1$ 的11个17进制数位全为16，总和176。直接作末两位的有限减法可知最后三个 high 是
$$
j_1=L-7,\qquad j_2=L-23,\qquad j_3=L-39,
\tag{8}
$$
从右至左排列。它们的数位和均为170；每个固定高位前缀、末位完整遍历0至16的17点段仅有一个 high。因此每个 $j_\ell$ 的左方都有至少三个连续 low，且：

- $j_1$ 前这三个 low 的右方 high 只有 $j_1$；
- $j_2$ 前这三个 low 的右方 high 为 $j_2,j_1$；
- $j_3$ 前这三个 low 的右方 high 为 $j_3,j_2,j_1$。

这只是三组明确索引的纸面数位身份，没有枚举 $17^{11}$ 个格点。

原相同母包、同宽格距及保持三二次矩的 $\mathcal F^\star$ 纠正给
$$
\mu_i=m(1,x_i,x_i^2+\sigma_*^2),\qquad m>0,
\tag{9}
$$
其中同一子块的 $\sigma_*^2>0$ 相同。不同频率或不同纠正后的母函数仍具有原来这些准确矩，因为它们在同一实际观测纤维。共同 affine 缩放只改变这两个共同常数和实际递增 $x_i$。

任意三个不同 $x_i$ 的(9)向量线性无关：从第三列减去 $\sigma_*^2$ 倍第一列即是普通二次 Vandermonde。

### 2.2 逐后缀消元，不使用任何自项假设

对 $j_1$ 前三个 low 应用(4)。右方其他 low 与当前 low 双角方向相同，在和式中准确相消；high 系数是同一个非零常数(7)。故
$$
\mu_i^{\mathsf T}\mathbf T_B\mu_{j_1}=0
\quad\text{对三个独立 }\mu_i.
$$
从而
$$
\mathbf T_B\mu_{j_1}=0.
\tag{10}
$$
在 $j_2$ 前三个 low 上同样得到
$\mathbf T_B(\mu_{j_2}+\mu_{j_1})=0$，结合(10)即
$\mathbf T_B\mu_{j_2}=0$。第三组再给
$\mathbf T_B\mu_{j_3}=0$。

三个 high 的(9)向量也独立，故
$$
\boxed{\mathbf T_B=0.}
\tag{11}
$$

因此，**当前 R280/R281/R293 从起点保原三矩的最右正布局，如果其完整 period 可由允许的全局 gauge 支付，就必须满足(11)。**

这不把矩阵九个条目当作九个独立条件；可以有原几何身份。它也不证明矩阵实际非零。它证明的是：若固定几何的实际矩阵非零，当前模板在所有同 $\mathcal F^\star$ 的高频、低阶纠正和正幅完整复制后仍不能通过零平台。不能把新增有限低阶观测本身当作对这个几何门的支付。

若(11)确已另付，则(3)进一步迫每个原微包
$$
q_i=0.
\tag{12}
$$
下文判清这些自项的真实正则阶数。

## 3. 矩阵的原曲率配对形式

为精确交接这个几何目标，记录一个简化。R292 的单包三矩模式写为
$$
\Pi_\mu=(\mathfrak a_\mu z+t_\mu,\ p_\mu z,\eta_\mu z+q_\mu^{\rm tail}),
\quad v_\mu=t_\mu/h,\quad w_\mu=q_\mu^{\rm tail}/h,
$$
$$
\rho_\mu=(v_\mu)_{ss}+v_\mu-kw_\mu.
\tag{13}
$$
此处 $q_\mu^{\rm tail}$ 是二阶仿射分子的系数，不是(12)的第四自项 $q_i$。

原平台恒等为
$$
(\eta_\mu)_s=p_\mu+h^2(v_\mu)_s,\qquad
\eta_\mu=-h^2v_\mu-k\mathfrak a_\mu-(p_\mu)_s.
\tag{14}
$$
于是对两个模式，先在
$\int h^2(v_\mu)_s(v_\nu)_s
=\int[(\eta_\mu)_s-p_\mu](v_\nu)_s$
中分部积分，再用(13)、(14)，得到
$$
\int\left[t_\mu t_\nu+\tau_\mu\tau_\nu+
\frac{k}{h}(\mathfrak a_\mu t_\nu+\eta_\mu q_\nu^{\rm tail})\right]
=-[p_\mu v_\nu]-\int\eta_\mu\rho_\nu .
$$
真实模式、几何与 frame 周期，使显示的端项为零。故
$$
\boxed{\mathcal T_B(\mu,\nu)=\frac14\int\eta_\mu\rho_\nu\,ds.}
\tag{15}
$$
这是同一原矩阵，不是重新指定一族平台场。这里未证明其对称性、符号或 signed 可达性，也没有把它等同于 R196 的 $\lambda_+$。

## 4. 自项的真实原源与最高三阶 jet

固定一个紧单包 $u$，令 $v=u'$、$r=u''$。用 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md) 的真实二阶 history
$$
W_2=\Phi_{m(s)}(u,u)
=A_{0,m}u^2+A_{1,m}uv+A_{2,m}v^2
+B_{0,m}J_0+B_{1,m}J_1+B_{2,m}J_2^*.
\tag{16}
$$
全部系数是同一个 $m(s)$ 的坐标，$m(s_0)=m(s_1)=0$。
置
$$
C_m=B_{0,m}+xB_{1,m}+x^2B_{2,m},\qquad Q=1+e^2.
$$
这里 $\deg_x A_{1,m}\le2$、$\deg_x A_{2,m}\le3$、$\deg_x C_m\le4$。

先从原 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 计算二阶 $\eta_0$，而不假定它低于 $u''$。第一分子及其导数是
$$
V_Y=(-v/2,0,hu-ev/2),\quad
V_{Y,x}=(-r/2,0,hv/2-er/2),
$$
$$
\nabla_sV_Y=(0,h(u-zv/2),\gamma u-e_s v/2).
$$
采用 R73 的
$P=J_e/(8h)+ev^2/8$ 和 $B=V_Y\cdot V_Y/(2h)$，
在 R56(6)逐项收集，得到完整式
$$
\boxed{
\eta_0=
-\frac{e_sQ}{16h^2}r^2
+\frac{\gamma Q}{8h^2}vr
-\frac{\gamma e}{8h}v^2
-\frac1{16}\partial_s(J_e/h).}
\tag{17}
$$
其中 $J_e=Q_dJ_0+2hdJ_1+h^2J_2^*$ 是原正尾。式(17)保全部时间导数和右原函数。

二阶恢复为
$$
V_Z=(A_Z,zP+B,eA_Z-hW_2),\qquad
A_Z=(W_2)_x/2+\eta_0/h.
$$
只有 $(A_Z)_x$ 能产生 $u'''$。用
$J_0'=-r^2$、$J_1'=-xr^2$、
$(J_2^*)'=-(x^2r^2+2v^2)$，
从(16)、(17)准确得到
$$
\boxed{
V_{Z,x}=(1,0,e)\,\Lambda(s,x;u,v,r)\,u'''
+\mathcal Z_{\le2},}
\tag{18}
$$
$$
\boxed{
\Lambda=\frac{A_{1,m}}2u+
\left(A_{2,m}+\frac{\gamma Q}{8h^3}\right)v
-\left(C_m+\frac{e_sQ}{8h^3}\right)r.}
\tag{19}
$$
$\mathcal Z_{\le2}$ 只含至多二阶局部 jets、原 $J_0,J_1,J_2^*$ 及其有限乘积。这里没有把 $\eta_0$ 的 $r^2$ 项漏掉，也没有把 $m$ 的原端值自由重选。

## 5. 准确的 $C^3$ 主项加有限 $C^2$ 余项

令 $U,V$ 是该单包在共同左 collar 的真实二阶分子 $xU+V$。记
$$
E_Z(s)=\int_\ell^r|V_{Z,x}|^2dx,\qquad
\alpha_Z=\frac{|U|^2}{2h}.
$$
对正 forcing $H(Z,Z)$，原 $P$ 左尾恰为
$$
P_Z=-\alpha_Z x+\frac{E_Z}{2h}+\ell\alpha_Z.
\tag{20}
$$
将它代入 R56，保全部 $B$、$T_s$ 后，
$$
[x^2]\mathscr P H(Z,Z)=
\int\left\{\frac{k}{2h}E_Z+
k\left[(\ell-\omega)\alpha_Z+\frac{U\cdot V}{h}\right]
+\frac{|\nabla_sU|^2}{2h^2}\right\}ds.
\tag{21}
$$
由 actual pure 身份，R292 的自项是此量的 $-1/4$。

用(18)展开 $|V_{Z,x}|^2$。二次最高 jet 项为
$Q\Lambda^2(u''')^2$。
其余含 $u'''$ 的项都只线性出现。对它们的系数关于 $r=u''$ 取一个在 $r=0$ 时为零的多项式原函数，再作一次真实 $x$ 分部积分。原函数中的 $J_j$ 的 $x$ 导数仍是二阶 jets；两 collar 有 $u''=0$，所以这一步没有遗失左尾边项。

因此准确存在一个四次多项式 $C^2$ 泛函 $\mathcal L_B$，使
$$
\boxed{
q_B(u)=-\frac18\int_I
\mathcal K_B(x;u,u',u'')\,(u''')^2\,dx
+\mathcal L_B(u),}
\tag{22}
$$
其中
$$
\boxed{
\mathcal K_B(x;u,v,r)
=\int_B\frac{kQ}{h}\,
\Lambda(s,x;u,v,r)^2\,ds.}
\tag{23}
$$
$\mathcal L_B$ 包含(21)的全部矩尾项以及(18)的全部低阶及线性最高 jet 项，不把任何真实累计项删掉。

这给有限而完整的来源描述：$\mathcal K_B$ 关于 $(u,v,r)$ 二次、关于 $x$ 至多十次；系数由同一实际几何的局部项、线性 $m(s)$、二次 $m(s)$ 积分确定。按六种 jet 单项的次数上界分别为 $6,7,8,8,9,10$，至多54个原标量系数；这只是保守生成上界，不是声称它们独立。

$\mathcal L_B$ 则是有限个至多二阶 jets 与原右积分的多项式积分，连同(21)的三矩二次项，所以在固定紧支撑的 $C^2$ 范数中连续。共同平移也只产生有限多项式系数。若从最初建立一个新的有限 $\mathcal F^\star$，这些**余项**可以准确加入；但(23)尚未消失时不能将整个 $q_B$ 冒称为 $C^2$ 观测。

## 6. 一个已经自动消去的主系数

令
$$
A=A_{1,m},\qquad
B^\flat=A_{2,m}+\frac{\gamma Q}{8h^3},\qquad
C^\flat=C_m+\frac{e_sQ}{8h^3},\qquad
\mathscr R=K_0+\lambda_s.
$$
R73 的点态(4)、(5)、(7)准确给
$$
\boxed{
A_s=-\frac{kQ}{2h},\qquad
(B^\flat)_s=\frac{Q}{8h}\mathscr R_x,\qquad
(C^\flat)_s=\frac{Q}{8h}\mathscr R.}
\tag{24}
$$
后两式中 $\gamma e e_s$ 和 $e e_s^2$ 分别在真实端势的时间导数中抵消；不假定连接段为常态。

特别，(23)的 $u^2$ 系数为
$$
\frac14\int\frac{kQ}{h}A^2ds
=-\frac12\int A_sA^2ds
=-\frac16[A^3]_{s_0}^{s_1}=0,
\tag{25}
$$
最后一步正是 $M_B=0$ 给 $m(s_0)=m(s_1)=0$。

所以 $\mathcal K_B$ 的普遍 $u^2$ 项已经付清。式(24)还把其余五类主系数准确表示成有限真实 history 配对。例如 $uv$、$ur$ 系数分别为
$$
\int A^2(B^\flat)_s\,ds,\qquad
-\int A^2(C^\flat)_s\,ds.
\tag{26}
$$
这些式子不意味着它们为零。本稿不由 $M_B=0$、$T_B=\kappa\mathfrak H$ 或 $\pi V_B=0$ 直接填入未证的消项，也不把新增主系数当作可任意指定的自由变量。

## 7. 何时新增 $C^2$ 纤维确实不足

式(22)不只是一个形式最高阶符号。若在一个实际基点和真实扰动支撑上(23)的主积分非零，就能严格排除“它已由某个有限 $C^2$ 观测固定”的推断。

先对不要求 even 的单包说明。选光滑 $u_0,\chi$ 使
$$
J_*=\int\mathcal K_B(x;u_0,u_0',u_0'')\chi^2dx\ne0.
\tag{27}
$$
取有限整数 $N$ 的真实函数
$$
u_N=u_0+N^{-5/2}\chi(x)\cos Nx.
$$
则 $u_N\to u_0$ 于 $C^2$，而三阶导的振荡幅为 $N^{1/2}$。由(22)、平方平均和 $C^2$ 系数连续性，
$$
\boxed{\frac{q_B(u_N)}N\longrightarrow-\frac{J_*}{16}\ne0.}
\tag{28}
$$
余项 $\mathcal L_B(u_N)$ 有界；最高项系数变化为 $O(N^{-1/2})$，除以 N 后消失。因此(27)下，$q_B$ 不是一个 $C^2$ 连续泛函。

当前母包为 even 时，应先作**真实偶配对**，不能直接用一个未配对的 jet 值。若物理中心为 X，定义
$$
\widehat{\mathcal K}_{B,X}(y;u,v,r)=
\mathcal K_B(X+y;u,v,r)
+\mathcal K_B(X-y;u,-v,r).
\tag{29}
$$
取 even $u_0,\chi$。只要相应的真实积分
$\int\mathcal K_B(X+y;u_0,u_0',u_0'')\chi^2dy$
非零，同一个 even 振荡与(28)仍成立。相反，若(29)对全部相关 jets 恒零，则(22)的主积分对该中心的所有 even 母包准确为零，不能据未配对符号宣称仍有高阶障碍。

这里没有先验声称当前固定几何的(27)或(29)非零。判断它们属于明确的原 history 问题，和 $\mathbf T_B=0$ 分开。

### 7.1 在任意初选有限 $C^2$ 观测纤维内仍成立

设从起点选定一个有限多项式 $C^2$ 观测
$\mathcal F^\star$，包括所有需要保持的旧数据和新低阶余项。假定一个开放母包邻域上有(27)的严格非零性，或其 even 版本。

应先在该开放邻域内选择 $\mathcal F^\star$ 的**真最大秩**基点和固定纠正方向。R277/R281及 R293 的多项式线论证允许这一选择：从邻域内一点连向一个最大 minor 见证，minor 是不恒零的有限多项式，所以任意小参数可避其有限根。解析端芽类别中先用 $\psi P$ 和 $\psi Q$ 稠密逼近，保严格非零性，再沿同类多项式线选定真正 minor。不是假定任意原母函数 regular。

对上述 $N^{-5/2}$ 扰动，固定 finite-minor 纠正满足
$$
a_{\ell,N}=O(N^{-1/2}),\qquad
\widetilde u_N=u_N+\sum_\ell a_{\ell,N}e_\ell,
\qquad
\mathcal F^\star(\widetilde u_N)=\mathcal F^\star(u_0).
\tag{30}
$$
原最大秩邻域的常秩论证保证不只是 minor 坐标，而是完整 $\mathcal F^\star$ 都保持。方向 $e_\ell$ 固定光滑，其三阶导纠正也只有 $O(N^{-1/2})$，不能抵消 $N^{1/2}$ 的真实振荡。因此(28)对 $\widetilde u_N$ 原样成立。

固定任何足够大的有限 N，仍是普通有限光滑、有限频率的包。在 R281 类中，prefactor 的修正一致趋零，故可保持原正 prefactor、两端解析形式和非退化 minor。没有把无限频率本身当作实际 profile。

这说明：**若真实偶主项非零，增加有限 $C^2$ 观测并保持其值，并不能把 $q_B$ 冻结，更不能声称它已被支付。** 同时，本节不宣称在另已固定的全部 $C^3$ 能量根上仍可任意改变 $q_B$；若需要联合支付，应把(22)作为准确新增高阶量，与原完整能量一起证明实际有限维正锥和非退化根。

## 8. 对当前剩余任务的精确含义

现在必须把三类任务分开：

1. **几何矩阵。** 对当前最右正布局，全部平台通过强迫 $\mathbf T_B=0$。同 $\mathcal F^\star$ 的 shape 修改保持原三矩，不能改变此必要条件；需要原几何身份、真实 signed 控制或一个明确的几何反例来处理。
2. **单包自历史。** 即使矩阵为零，每个 $q_i$ 还须为零。其完整来源是(22)，不能在未核主项时塞入 $C^2$ 观测。已经自动消去的是(25)，其余主配对和真正低阶基线逐项保留。
3. **全 period 与 joint。** 平台二次项和零端一次层只是一部分。全局通量、内部退化匹配、平台仿射部分、零/一 Gaussian history，以及同一个二阶 gauge 的 ruling 条件都没有由本稿支付。

本稿给出的障碍不扩大到任意圆：它明确使用当前正布局在最右的实际后缀。若改用重叠 profiles、另一真实排列或改变矩数据，须重新推其完整平台条件，不能沿用(11)而不检查前提。反之，只在当前纤维中追加位置、频率或更多观测，不会消掉已经由三组末格点强迫的原几何矩阵。
