# R232：完整 mean 消元后的双秩项与解析能量

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-14。

**已证明的条件工具，尚无新增数值实例化。** 本文明确 R228 中非局部零阶项的一个实际入口：使用原非均值变量并消去完整 mean 后，原角投影与 mean 反馈分别产生一个秩一算子。非恒定剪切后不能删掉前者。两项可以用准确 Hermitian 谱上界计费；在真实非均值约束上还可作准确的正交压缩。

本条使用 [R75](R75-complete-mean-transport-and-shear-constraint.md)(75.5)、(75.8) 已有的完整 mean 微分，以及 [R69](R69-complete-mean-principal-symbol-and-analytic-frame.md) 的原四 jet 偏导与真实剪切。这里引用 R69 的内容身份为 Git blob `42f85bbb092cdda2172237d2e4ee2c3e43d35c0f`，在已读提交 `e3b7f8f48244870fd7b902fc28168cfc7dcf937c` 下定位。R228 的 $A,C$ Fourier Hermitian 界、真实 $T_x,T_\theta$、frame 跳变和余宽费用全部保留。

## 1. 必须先明确采用哪一个系统

保持真实背景 $s,\ell,z,E$ 与完整非线性
$$
\mathcal N(P,K,T,V)
=\frac{Es(V-P)^2+\ell(K^2+2EKT+ET^2-zP^2)}{L},
\qquad L=1+K+ET,
$$
$$
T=P_\theta,\qquad V=K_\theta,\qquad
K=c+\bar K,\qquad \langle\bar K\rangle=0.
\tag{232.1}
$$
$c=c(P,\bar K;x)$ 是同一完整 mean 根。所有 $S,D,y,N,L$ 与原 scalar 根域均保持。

本条线性化的是**已经消去 mean 的非均值系统**
$$
P_x=s\bar K_\theta-(s+\ell)P,
\qquad
\bar K_x=-\ell(2\bar K+P_\theta)+\Pi_\perp\mathcal N(P,c+\bar K,T,V).
\tag{232.2}
$$
令中心为实、具有原奇偶对称性的足够光滑场：
$P$ 为奇函数，$\bar K$ 为偶函数。变化 $X=(p,k)^t$ 满足
$\langle p\rangle=\langle k\rangle=0$，并具有相同奇偶性。变化可以是复数；这不自动允许中心参数变成未付的复域。

若直接采用 R69 中包含完整 $K$ 零模的较大系统，则这些变量没有消元，不能再把本条两项重复加入该系统。两种表述之间的 mean/候选残差桥仍按 R75 支付。

在 (232.2) 的中心上，$\mathcal N_P,\mathcal N_K,\mathcal N_T,\mathcal N_V$ 表示四个 jet 暂时独立时的偏导。局部未投影部分为
$$
A=\begin{pmatrix}0&s\\-\ell+\mathcal N_T&\mathcal N_V\end{pmatrix},
\qquad
C=\begin{pmatrix}-(s+\ell)&0\\
\mathcal N_P&-2\ell+\mathcal N_K
\end{pmatrix}.
\tag{232.3}
$$
所有偏导均包含完整 $c$ 和 $L^{-1}$，不截断它们的 Fourier 频率。

## 2. 准确分离角投影与 mean 两项

置
$$
q=\frac{E(V-P)}{L},\qquad
\mathsf w=\frac{L}{D^{3/2}},\qquad
\mu=\langle\mathsf w\rangle>0,
\qquad D=1-z(2K+K^2+EP^2).
\tag{232.4}
$$
R75 的完整微分准确给
$$
\delta c=-\frac{\langle\mathsf w(k-qp)\rangle}{\mu}.
\tag{232.5}
$$

对局部第二分量取平均并作完整周期分部积分，定义
$$
\beta_P=\mathcal N_P-\partial_\theta\mathcal N_T,\qquad
\beta_K=\mathcal N_K-\partial_\theta\mathcal N_V,
$$
$$
\widetilde\beta_P=\beta_P-\langle\beta_P\rangle,\qquad
\widetilde\beta_K=\beta_K-\langle\beta_K\rangle,\qquad
h=\Pi_\perp\mathcal N_K .
\tag{232.6}
$$
因为 $p,k$ 都是非均值量，减去这两个已知常数不改变任何平均。背景项 $-\ell p_\theta,-2\ell k$ 的平均准确为零。因此线性化的完整非均值算子是
$$
X_x=A X_\theta+C X
-e_2\langle\widetilde\beta_Pp+\widetilde\beta_Kk\rangle
+e_2h\,\delta c+f,\qquad e_2=(0,1)^t.
\tag{232.7}
$$
$f$ 保留原已付的候选缺陷及其它源；本条没有令其第一分量免费为零。

证明 (232.7) 只用对 (232.2) 直接求导。$\delta c$ 没有角导数，故其局部贡献为 $\mathcal N_K\delta c$；输出投影给 $h\delta c$。其余局部输出的平均恰为 (232.6) 的泛函。这里无需假设中心已经满足 PDE；中心的真实径向导数仍须用于下一节的变换。

## 3. 在原真实剪切/frame 下的两列

令 $b=b(x)>0$ 且与角度无关，沿 R69 取
$$
Z=\mathsf T X,\qquad
\mathsf T=B S
=\begin{pmatrix}b&0\\-q&1\end{pmatrix},
\quad
Z_1=bp,\quad Z_2=k-qp .
\tag{232.8}
$$
注意 $\mathsf T e_2=e_2$，所以纯第二源列没有新 $b$ 因子。真实变换后的局部系数仍为
$$
\widehat A=\mathsf T A\mathsf T^{-1},\qquad
\widehat C=\mathsf T C\mathsf T^{-1}
+\mathsf T_x\mathsf T^{-1}
-\widehat A\mathsf T_\theta\mathsf T^{-1}.
\tag{232.9}
$$
其中 $q_x$ 必须用实际候选导数，包括完整 $c_x$；不能以候选未满足的 PDE 代换。

真实约束变成
$$
\left\langle Z_2+\frac qb Z_1\right\rangle=0.
\tag{232.10}
$$
结合 (232.5)，在这个约束上准确有
$$
\delta c=
\left\langle \frac qb Z_1+
 \left(1-\frac{\mathsf w}{\mu}\right)Z_2\right\rangle .
\tag{232.11}
$$
这是完整 mean 的消元，不是删除其导数。两个系数的零模均为零：$q$ 奇，且 $\langle\mathsf w/\mu\rangle=1$。

因此非局部项准确为
$$
\mathcal RZ=u_c\langle g_c,Z\rangle_{\rm av}
+u_\Pi\langle g_\Pi,Z\rangle_{\rm av},
\tag{232.12}
$$
其中平均泛函采用无共轭的实际乘积，并定义
$$
u_c=e_2h,\qquad
g_c=\left(\frac qb,\,1-\frac{\mathsf w}{\mu}\right),
$$
$$
u_\Pi=-e_2,\qquad
g_\Pi=\left(
 \frac{\widetilde\beta_P+q\widetilde\beta_K}{b},
 \widetilde\beta_K\right).
\tag{232.13}
$$
这里 $\langle g,Z\rangle_{\rm av}$ 表示
$\langle g_1Z_1+g_2Z_2\rangle$，不是 Hilbert 内积。

特别地，非恒定 $q$ 使 $Z_2$ 通常不再零均值。故在变换后的能量里，$u_\Pi$ 这一原 $\Pi_\perp$ 项不能因其输出为常数而直接删除。若选择把投影保留在“局部”算子内，也必须重新支付那个被投影算子的能量；不能同时引用 R228 未投影局部块的界并省去 $u_\Pi$。

## 4. 真实加权 Hilbert 对偶与秩一谱

固定一个真实 $x$ 及能量角宽 $\tau\ge0$。置
$\zeta_m=e^{\tau|m|}Z_m$，Hilbert 内积约定为
$$
\langle v,\zeta\rangle_H
=\sum_m\overline{v_m}^{\,t}\zeta_m .
$$
对一个物理输出列 $u(\theta)$ 和无共轭平均系数行 $g(\theta)$，令
$$
U_m=e^{\tau|m|}u_m,\qquad
V_m=e^{-\tau|m|}\overline{g_{-m}}^{\,t}.
\tag{232.14}
$$
则角平均准确满足
$\langle g,Z\rangle_{\rm av}=\langle V,\zeta\rangle_H$。
全部频率保留；必须真实支付 $U,V\in\ell^2$。对实角系数，$\overline{g_{-m}}=g_m$，但不能对一般复中心免费作此替换。

**引理 232.1。** 对任意复 Hilbert 空间中的 $R=U V^*$，记
$c=\langle V,U\rangle_H$。其 Hermitian 部在 $\operatorname{span}\{U,V\}$ 上的两个可能非零特征值为
$$
\lambda_\pm
=\frac{\operatorname{Re}c
 \pm\sqrt{\|U\|^2\|V\|^2-(\operatorname{Im}c)^2}}2 .
\tag{232.15}
$$
因而安全的能量增长系数为
$$
\omega(R)=
\max\!\left\{0,\,
\frac{\operatorname{Re}c+
 \sqrt{\|U\|^2\|V\|^2-(\operatorname{Im}c)^2}}2\right\}.
\tag{232.16}
$$
若实 Fourier 共轭配对给 $c\in\mathbb R$，则为
$\max\{0,(c+\|U\|\|V\|)/2\}$。

**证明。** Hermitian 部是 $(UV^*+VU^*)/2$，秩至多2，迹为 $\operatorname{Re}c$，两个特征值的乘积为
$(|c|^2-\|U\|^2\|V\|^2)/4$。求根得 (232.15)，Cauchy–Schwarz 保证根号非负。其余正交补的特征值为0，得 (232.16)。退化/零列情形由连续性涵盖。这里保留了真实内积 $c$ 的符号，没有用正乘积替代它。证毕。

不利用约束压缩时，可以对 (232.12) 两项分别用 (232.16) 并相加，得到合法 $\omega_{\mathcal R}$。这项费用再加入 R228 的完整 $\Lambda=\chi_H+\zeta_H+\omega_{\mathcal R}$，不重复另加同一两项的算子范数。

对 mean 项，真实内积具有特别简单的身份：
$$
c_c=\langle V_c,U_c\rangle_H
=\left\langle \left(1-\frac{\mathsf w}{\mu}\right)h\right\rangle
=-\frac{\langle\mathsf w h\rangle}{\mu}.
\tag{232.17}
$$
全部角权在这个内积中准确消去，但其范数没有消去。这个等式不是说 $c_c$ 必然有利；实际符号仍须由同完整系数支付。

## 5. 在真实非均值约束上的准确压缩

在原奇偶 Fourier 子空间内，第一分量已无零模。记
$$
e_m=\begin{cases}e_2,&m=0,\\0,&m\ne0,\end{cases}\qquad
v_q=\mathfrak d_\tau(q/b,0),\qquad
v_d=\mathfrak d_\tau(0,1-\mathsf w/\mu),
$$
其中 $\mathfrak d_\tau$ 就是 (232.14) 的平均对偶。令
$$
a^2=\|v_q\|^2,\qquad w_c=e+v_q,\qquad
P_\tau=I-\frac{w_cw_c^*}{1+a^2}.
\tag{232.18}
$$
因 $e\perp v_q$，(232.10) 恰为 $\zeta\perp w_c$，所以 $P_\tau$ 是这个约束子空间的准确正交投影。

对满足该约束的 $\zeta$，
$$
\operatorname{Re}\langle\zeta,\mathcal R\zeta\rangle_H
=\operatorname{Re}\left\langle
\zeta,\sum_{j=c,\Pi}(P_\tau U_j)(P_\tau V_j)^*\zeta
\right\rangle_H .
\tag{232.19}
$$
因此可以用压缩后的两对列支付同一个实际能量。这里仅在每个 $x$ 对二次型作恒等变形，没有把 $P_\tau\zeta$ 定义为新演化变量，故不凭空引入 $P_{\tau,x}$；若另行改变演化变量或约束 Galerkin 方程，则必须支付其真实导数/交换项。

具体有
$$
P_\tau U_c=U_c,\qquad
V_c=v_q+v_d,\qquad
\|P_\tau V_c\|^2=\frac{a^2}{1+a^2}+\|v_d\|^2,
\tag{232.20}
$$
并保持 $c_c$ 不变。原因是 $h$ 的零模为0，而 $v_d$ 的第二分量零模也为0，故 $U_c\perp w_c$、$v_d\perp(e,v_q)$。

对原角投影列，
$$
P_\tau U_\Pi=-e+\frac{e+v_q}{1+a^2},\qquad
\|P_\tau U_\Pi\|^2=\frac{a^2}{1+a^2}.
\tag{232.21}
$$
记 $d_\Pi=\langle w_c,V_\Pi\rangle_H$。因
$\langle\widetilde\beta_K\rangle=0$，$V_\Pi$ 的第二分量零模为0，故
$$
\|P_\tau V_\Pi\|^2
=\|V_\Pi\|^2-\frac{|d_\Pi|^2}{1+a^2},\qquad
c_\Pi^{\rm cmp}
=\langle P_\tau V_\Pi,P_\tau U_\Pi\rangle_H
=\frac{\overline{d_\Pi}}{1+a^2}.
\tag{232.22}
$$
这些是准确恒等式，不是从两个独立向上帽相减获得更小上界的许可。实际区间实现必须共同包围所需 Gram 数据；必要时使用不作减法的更粗范数帽。

当 $q=0$ 时，$P_\tau U_\Pi=0$，原平均投影在真实非均值能量中不收费。这由真实约束推出；对一般非零 $q$，费用由 (232.21) 保留，不能仍按零处理。

## 6. 两项联合的四维 Hermitian 读出

设已经选定不压缩或按第5节压缩的四列
$(\widetilde U_c,\widetilde U_\Pi,\widetilde V_c,\widetilde V_\Pi)$，
组成算子 $F:\mathbb C^4\to H$，令
$$
G=F^*F,\qquad
J=\frac12\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix}.
\tag{232.23}
$$
完整非局部 Hermitian 部是 $FJF^*$。其非零谱等于
$G^{1/2}JG^{1/2}$ 的非零谱，因此
$$
\omega_{\mathcal R}
=\max\{0,\lambda_{\max}(G^{1/2}JG^{1/2})\}
\tag{232.24}
$$
是一个准确的完整两项能量界；在无限维空间中右侧就是其全空间最大谱。也可保守使用两项 (232.16) 的和。

**证明。** 在 $F$ 的极分解中写 $F=U G^{1/2}$；$U$ 是支撑子空间上的等距映射。因此 $FJF^*=U(G^{1/2}JG^{1/2})U^*$，非零谱相同，正交补只有零谱。$G$ 奇异时同样成立。证毕。

$G$ 的每一项必须来自同一个完整 Fourier 对象、同一 $\tau$ 和同一 mean 分支。有限部分可保符号求和，正尾用 Cauchy–Schwarz 逐 Gram 项支付。不能把两个分别取过 supremum 的向量当成实现了同一个有利内积。

## 7. 接入 R228 时的量词与未付项

本条只给非局部零阶项的准确结构与条件能量账。实际接入至少保留以下事实：

- 第5节只作用于真实约束 (232.10) 的解或严格保持该约束的近似。原非均值 Galerkin 后再剪切，与在剪切变量中自由截频不交换；若采用后者，不能借第5节免费满足约束。
- 中心必须是同一候选或同一管内实场。所有 $q,\mathsf w,\mathcal N_K,\beta_P,\beta_K$ 都含完整 mean/逆；$\mu>0$ 和 Fourier 范数门另付。
- $\partial_\theta\mathcal N_T,\partial_\theta\mathcal N_V$ 是已知系数的真实角导数。它们所需的候选二阶角 jet、完整 inverse 导数及尾不能由未付的采样推断。
- 原真实 $q_x$、$b_x$、全部 frame jumps、源的两分量及 R228 的严格余宽/径向先 supremum 转换继续收费。本条不会改变它们的单位或省掉其中任何一项。
- 复变化适用复 Hilbert 公式；若中心本身是复参数场，R228 的实 Fourier 共轭结构、原 mean 分支和本条实简化必须另证。
- 还没有对原3976叶的 $G$、$\omega_{\mathcal R}$ 或其积分作新数值运行；没有由秩小就宣称原非线性管自映、外延拓或闭面已完成。

一个可执行的小消费者可逐原叶保存：中心/source/mean SHA、$\tau,b,\mu$，完整 $U_j,V_j$ 的有限系数与尾、(232.17) 的 signed 内积、$a^2,d_\Pi$、不压缩与压缩两个 Gram 包、最终严格谱上界及全部 finite/branch 门。无需重算任何原线性 ODE。只有实际满足这些门后，才把所得 $\omega_{\mathcal R}(x)$ 加入 R228 的有序能量积分。
