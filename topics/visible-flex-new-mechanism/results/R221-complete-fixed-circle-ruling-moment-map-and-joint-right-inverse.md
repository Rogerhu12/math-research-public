# R221：任意二阶 gauge 的完整 ruling 矩映射、周期核右逆与固定圆联合判据

日期：2026-11-15。**已证明；完整纸面推导，没有新的研究编译、profile 求积、几何评价或消元。**

本稿把 [R184](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md) 的任意二阶齐次 gauge 联合问题化成可直接消费的准确接口。相对于 [R195](R195-single-active-packet-period-kernel-and-nonzero-fourth-ruling-direction.md) 的单活动包，本稿不限制 gauge 的支撑，也不要求 f 在其支撑上常值。完整线性 ruling 响应由 42 个明确的真实几何函数与 126 个固定 profile 线性矩表示；真实第二累计历史全部保留。

在第 6 节明确的导数包条件下，本稿还刻画周期算子的**全部核**，用一个有限正半定矩阵准确给出这整个核的矩像与固定 profile 右逆。于是，先付两个真实 period 目标后，全部剩余 joint 问题等价于一个冗余的 48 行、135 列实三角多项式矩阵方程及其有限降秩点的可去奇点条件。后者负责全相位光滑性，不能用逐相位的像包含替代。

42、126、48 和 135 都是本稿保留的生成元或矩阵尺寸，**不是实际秩**。本稿没有评价一个实际几何的目标，也没有宣称第四联合条件已经成立。R220 的 Morse 几何给适用的真实低阶背景，不自动使本稿矩阵满射。

## 1. 固定资料、真实锚与结论范围

固定一条 [R220](R220-constrained-Morse-geometry-with-exact-universal-pure-control.md) 允许的真实光滑闭 hook 几何。保持同一个目标度量、第一 profile 圆和全局几何参数 s。假设已付

$$
M=0,\qquad T=\kappa\mathfrak H,\qquad
\kappa\ne0,\qquad \pi V=0.
\tag{1}
$$

其中最后一式是 R210 的整个 universal pure 身份。取 R183/R199 的一个合法八完整 packet 圆

$$
\phi_\theta=\cos\theta\,f+\sin\theta\,g,\qquad
F=f^2,\qquad D_\theta=F-\phi_\theta^2.
\tag{2}
$$

平方与乘积在二次算子输入中均指对称槽。f、g 实线性无关，原 canonical 二、三阶场已通过周期和两 collar range。最终几何固定以后，本文所有操作都在这同一几何和同一圆上进行，不再扰动其度量。

固定 $I=[\ell,r]$ 及其中两个共同开放零 collar。写 $\mathcal X$ 为在这些固定 collar 上恒零的实光滑 profiles。可选 $\ell<\ell_0<r_0<r$，把 $\mathcal X$ 等价写成在 $I\setminus[\ell_0,r_0]$ 为零的光滑函数；它们在 $\ell_0,r_0$ 的全部 jets 相应为零。

初始选择 $\ell_0,r_0$ 时，把它们严格放在 f、g 的共同零带内部，并使所有活动闭区间与这两个边界保持正距离。于是第 7 节最外侧的端迹 cutoff 也有一段允许的 f 常值平台可作过渡；不使用首活动端点恰等于 $\ell_0$ 或末活动端点恰等于 $r_0$ 的极端选择。这个固定 collar 的选择在几何和 profiles 确定后一次完成。

共同右积分是

$$
Jv(x)=\int_x^r v(t)\,dt,\qquad (Jv)'=-v.
\tag{3}
$$

不把 J 的左值重置为零。s 累计历史始终从整个实际字的同一个起点 $s_0$ 累计；下文在几何子段上的公式继承其真实入值。

记

$$
d=h\omega-k,\quad e=hx+d,\quad Q=1+e^2,\quad
\gamma=h_s,\quad \delta=d_s=\gamma\omega-h\omega_s,\quad
e_s=\gamma x+\delta.
\tag{4}
$$

仍有 $\omega_s=k_s/(2h)$、$h>0$ 和共同物理区间上 $x+\omega>0$。本稿不用负 h 的形式延拓。

第 2–5 节的任意 gauge 有限分解不需第 6 节的额外包条件。完整核右逆及第 10 节的双向有限判据使用该明确条件；不能无条件推广到任意带退化平台的 f。原 period 的两个函数成员门则始终保留，不假定一组通量必要条件已经充分。

## 2. 从真实第二恢复分离全部 gauge 依赖

[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md) 已给瞬时二阶密度属于同一 E8：

$$
r_s(a,b)=\Phi_{M_{\rm raw}(s)}(a,b),\qquad
\mathsf m(s)=\int_{s_0}^{s}M_{\rm raw}(t)\,dt.
\tag{5}
$$

取其固定八基 $\Phi_j$，写

$$
\Phi_{\mathsf m(s)}=\sum_{j=1}^{8}a_j(s)\Phi_j
=:\mathsf A_s.
\tag{6}
$$

这是完整八维第二历史。全周期 M=0 只给两端的累计值相同，不能令中间的 $a_j(s)$ 为零。任一子段的初值是 (5) 的真实前缀。canonical 全字采用其原零初值；另加的任意二阶齐次 profile 正是本文的 w，而非悄悄改写 (5)。

对静态 profiles a、b，R56/R73 的同锚恢复是

$$
Z_B(a,b)=K_s(a,b)-Y_{\mathsf A_s(a,b)},
\tag{7}
$$

$$
K_s(a,b)=\rho_{ab}N+
\frac{\eta_{ab}}{h^2}\{uT+(h^2-ku)B\},\qquad
u=\frac h{x+\omega}.
\tag{8}
$$

设

$$
\mathbf m(a,b)=
\left(\int a''b'',\ \int xa''b'',\
\int x^2a''b''+2\int a'b'\right),
$$

$$
\mathbf w(s)=
\left(\frac{1+d^2}{4h},\frac d2,\frac h4\right).
\tag{9}
$$

所有未标区间的 profile 积分均在 I。真实 physical ruling 配对是

$$
\mathcal E_s(a,b)
=\int (Y_a)_u\cdot(Y_b)_u\,du
=\mathbf w(s)\cdot\mathbf m(a,b).
\tag{10}
$$

当一槽为 $\mathsf A_s(a,b)$ 这类有真实左尾的 profile 时，若另一槽紧支撑，(10) 仍成立：分部积分端项含那个紧支撑槽的 jets，因而为零；有尾槽本身并未被设为紧支撑。

定义实三线性泛函

$$
\mathcal T_s(c;a,b)
=\int (Y_c)_u\cdot (K_s(a,b))_u\,du,
\tag{11}
$$

后两槽对称。由 R184 的原式，**对任意 $w\in\mathcal X$**，

$$
\boxed{\begin{aligned}
\mathcal B_\theta(w)
={}&2\mathcal T_s(w;D_\theta)
-4\mathcal T_s(\phi_\theta;\phi_\theta,w)\\
&-2\mathcal E_s(\mathsf A_sD_\theta,w)
+4\mathcal E_s(\phi_\theta,\mathsf A_s(\phi_\theta,w)).
\end{aligned}}
\tag{12}
$$

这里 $\mathcal B_\theta$ 是 R184 的完整线性 ruling 响应，不是只在零 gauge 的切向近似。若 w 尚不满足新增第三 range，式 (12) 是同锚形式恢复的准确表达；第 9 节再准确施加该合法性条件。

原 canonical 第三场 W 没有进入 (12) 的线性算子系数。它仍全部存在于待匹配的原目标 $K^0_\theta$ 中；第 8 节不会把这部分删掉。

## 3. 完整局部三线性式：18 个明确几何函数

下面把 (11) 写成只含局部 profile 乘积的式子，保留从真实右尾产生的全部项。这是 R195 对角公式的完整极化，而非由某个常态或幂尾猜测。

### 3.1 极化后的 eta

第一分子及固定 x 的协变导数为

$$
V_a=\left(-\frac{a'}2,0,ha-\frac e2a'\right),\qquad
\nabla_sV_a=
\left(0,h\left(a-\frac{x+\omega}{2}a'\right),
\gamma a-\frac{e_s}{2}a'\right).
$$

由 R56(2)、R73(2)，

$$
b_{ab}=\frac h2ab-\frac e4(ab'+a'b)+\frac Q{8h}a'b',
$$

$$
P_{ab}=\frac e8a'b'+
\frac1{8h}J\{Qa''b''+2h^2a'b'\}.
\tag{13}
$$

其对称混合配对是

$$
T_{sx,ab}=
\frac{\gamma h}{4}(ab'+a'b)
-\frac{\gamma e}{4}(ab''+a''b)
-\frac{he_s}{4}a'b'
+\frac{ee_s}{8}(a'b''+a''b').
$$

将这些量直接代入真实恢复

$$
\eta_{ab}
=-\frac{T_{sx,ab}}{2h}
+\frac{e_s}{2h}(P_{ab})'
+\frac{\gamma}{2h}(b_{ab})'
-\frac12(P_{ab})_s
$$

得到

$$
\boxed{\begin{aligned}
\eta_{ab}=\frac1{16h^2}\Big[
&Q\{\gamma(a'b''+a''b')-e_sa''b''\}
-2h\gamma e\,a'b'\\
&+J\{(\gamma Q-2hee_s)a''b''
-2h^2\gamma a'b'\}\Big].
\end{aligned}}
\tag{14}
$$

求 s 导数时固定真实 x，且先对整个 $P_{ab}$ 求导。式 (14) 保留 $\gamma,\delta$ 及所有右原函数，不要求常状态。

### 3.2 消去配对里的右积分并保端项

(8) 的分子为

$$
V_K=\left(\frac{\eta_{ab}}h,\ (x+\omega)P_{ab}+b_{ab},\
\frac{e\eta_{ab}}h\right).
$$

$(Y_c)_u$ 的 N 分量为零，所以中间分量与它逐点正交。对余下两分量作一次真实分部积分，得

$$
\mathcal T_s(c;a,b)=
\frac1{2h^2}\int Qc'''\eta_{ab}\,dx.
\tag{15}
$$

例如完整 physical 配对先写成
$h^{-1}\int V_c'\cdot V_K'$；被合并掉的端项是
$-[V_c\cdot V_K/(h(x+\omega))]_\ell^r$，由 c 的双 collar 准确为零。随后对 $\eta'$ 的积分中，$c'$、$c''$ 项准确相消，留下 (15)。

右尾转置是左积分，不是另选右锚。具体地，

$$
\int_\ell^x Q(t)c'''(t)\,dt
=Qc''-2hec'+2h^2c=:F_c.
\tag{16}
$$

(16) 用的是 c 在左 collar 的真实零 jets。Fubini 给
$\int Qc'''Jv=\int F_cv$。因此

$$
\boxed{\begin{aligned}
\mathcal T_s(c;a,b)=\frac1{32h^4}\int\Big[
&Q^2c'''\{\gamma(a'b''+a''b')-e_sa''b''\}\\
&-2h\gamma eQ\,c'''a'b'\\
&+F_c\{(\gamma Q-2hee_s)a''b''
-2h^2\gamma a'b'\}\Big]dx .
\end{aligned}}
\tag{17}
$$

没有假定 $Jv(\ell)=0$；该左尾已经全部进入 $F_c$ 项。这个式子对后两槽普通极化，不能把三个槽自行完全对称化。

### 3.3 18 个生成元的定义

把 $e=hx+d$、$e_s=\gamma x+\delta$ 代入 (17)。公共分母为 $h^4$；分子关于 h、d 的总次数只可能为 0、2、4，并且关于 $\gamma,\delta$ 线性。因此存在 18 个固定 profile 三线性泛函 $t_\alpha$，准确满足

$$
\mathcal T_s(c;a,b)=\sum_{\alpha=1}^{18}
g_\alpha^{\rm loc}(s)t_\alpha(c;a,b),
\tag{18}
$$

其中几何生成元按固定顺序取

$$
\boxed{
\gamma h^{i-4}d^j,\quad
\delta h^{i-4}d^j,\qquad
i,j\ge0,\quad i+j\in\{0,2,4\}.}
\tag{19}
$$

共有 $2(1+3+5)=18$ 项。$t_\alpha$ 定义为 (17) 中相应单项式的系数，包含 $1/32$；这是明确有限的系数抽取定义，可直接从显示的被积式实现，不需另编任何第四 forcing。

## 4. 任意 gauge 的 126 个固定 profile 矩

历史两项由 (6)、(9) 精确给 24 个几何函数

$$
\boxed{
g^{\rm hist}_{j,i}(s)=a_j(s)\mathbf w_i(s),
\qquad j=1,\ldots,8,\quad i=0,1,2.}
\tag{20}
$$

把 (19)、(20) 合并成一个固定 42 维列向量 $\mathbf g(s)$。不预设其分量独立。对局部第 $\alpha$ 项定义相位线性泛函

$$
L_{\alpha,\theta}(w)=
2t_\alpha(w;D_\theta)
-4t_\alpha(\phi_\theta;\phi_\theta,w).
\tag{21}
$$

对历史项定义

$$
L_{j,i,\theta}(w)=
-2m_i(\Phi_jD_\theta,w)
+4m_i(\phi_\theta,\Phi_j(\phi_\theta,w)).
\tag{22}
$$

每一项只含 $1,\cos2\theta,\sin2\theta$，故唯一写成

$$
L_{\rho,\theta}
=\ell_{\rho,0}+\cos2\theta\,\ell_{\rho,c}
+\sin2\theta\,\ell_{\rho,s},
\qquad \rho=1,\ldots,42.
\tag{23}
$$

于是任意 $w\in\mathcal X$ 的完整响应是

$$
\boxed{
\mathcal B_\theta(w)(s)=
\sum_{\rho=1}^{42}g_\rho(s)
\{\ell_{\rho,0}(w)+
\cos2\theta\,\ell_{\rho,c}(w)+
\sin2\theta\,\ell_{\rho,s}(w)\}.}
\tag{24}
$$

(17)、(21)、(22)、(23) 就是全部 126 个矩的明确来源。它不依赖把 w 限在一个有限试空间；只是在准确表达全空间上的有限线性映射。

### 4.1 全部矩的光滑密度与精确 adjoint

写

$$
D_0a=a^{(4)},\qquad
D_1a=xa^{(4)}+2a''',\qquad
D_2a=x^2a^{(4)}+4xa'''.
\tag{25}
$$

则 $m_i(a,w)=\int(D_i a)w$。每个固定 E8 算子用 R73 的六项式

$$
\begin{aligned}
\Phi_j(a,w)={}&A_0aw+
\frac{A_1}{2}(aw'+a'w)+A_2a'w'\\
&+B_0J(a''w'')+B_1J(xa''w'')\\
&+B_2J(x^2a''w''+2a'w').
\end{aligned}
\tag{26}
$$

这里 $A_\nu,B_\nu$ 是该单位基的固定 x 多项式，不是新几何未知函数。对任意 v，记
$J^*v(x)=\int_\ell^xv(t)\,dt$。由真正端项为零，

$$
\boxed{\begin{aligned}
\Phi_{j,a}^*v={}&
\left(A_0a+\frac{A_1}2a'\right)v
-D_x\left[\left(\frac{A_1}2a+A_2a'\right)v\right]\\
&+D_x^2\left[
a''\{J^*(B_0v)+xJ^*(B_1v)+x^2J^*(B_2v)\}
\right]\\
&-2D_x\{a'J^*(B_2v)\}.
\end{aligned}}
\tag{27}
$$

因此

$$
m_i(c,\Phi_j(a,w))
=\int\Phi_{j,a}^*(D_i c)\,w.
\tag{28}
$$

另一类历史密度为 $D_i[\Phi_j(a,b)]$。其真实左尾是二次以下多项式，由 (25) 的三、四阶导数准确杀掉；不能先把该尾设零。局部式 (17) 对 w 作有限次分部积分即可给相应密度。

由此所有 126 个矩都有固定光滑密度。连同新增第三 range 所需的六个矩，定义

$$
\mathcal M w=
\bigl(\mathbf m(f,w),\mathbf m(g,w),
(\ell_{\rho,\bullet}(w))_{\rho,\bullet}\bigr)
=\int_I\boldsymbol\rho(x)w(x)\,dx
\in\mathbb R^{132}.
\tag{29}
$$

$\boldsymbol\rho$ 是明确、固定的 132 维光滑函数。它的可能线性关系全部保留，既不先假独立，也不以有限采样替代其真实关系。

## 5. 先支付整个 period，保留两个函数成员门

[R213](R213-two-mixed-sources-and-gauge-invariant-platform-obstructions-after-pure-closure.md) 给真正两个 canonical 源 $V_d,V_e$，含完整第三历史，且在 (1) 下

$$
V^0_\theta=\sin^2\theta\,V_d+
2\sin\theta\cos\theta\,V_e.
$$

所以 period 方程准确为

$$
L_f(w_\theta)=
(1-\cos2\theta)G_c+\sin2\theta\,G_s,
\qquad
G_c=-\frac{V_d}{4\kappa},\quad
G_s=-\frac{V_e}{2\kappa}.
\tag{30}
$$

必要且充分的第一门是

$$
\boxed{G_c,G_s\in L_f(\mathcal X).}
\tag{31}
$$

必要性不需像闭性：从一个全相位解在两个适当相位取固定线性组合就能得到两个原目标的解。充分性是选取两个实际 profiles $u_c,u_s$，分别满足这两个方程。

(31) 是原函数成员门。R181 的退化 ODE、全部端条件与右锚给准确全局解释；R211 的有限 Green 判据只在其已注明的正则/有限简单退化子区间及目标支撑前提下可用。不能把 R181 的若干通量必要条件冒称 (31) 的充分条件。

R185 给固定的六矩右逆 $S_6:\mathbb R^6\to\ker L_f$。因此可取

$$
w_c=u_c-S_6\mathcal M_6u_c,\qquad
w_s=u_s-S_6\mathcal M_6u_s,
$$

$$
w_\theta^{\rm per}
=(1-\cos2\theta)w_c+\sin2\theta\,w_s.
\tag{32}
$$

它准确解 (30)，全部六矩为零，光滑周期且在 $0,\pi$ 为零。此处只选两个实际解，不需要一个未经证明的无限维连续选根定理。

一切其他 period 解恰为

$$
w_\theta=w_\theta^{\rm per}+k_\theta,\qquad
k_\theta\in\ker L_f.
\tag{33}
$$

**不能进一步要求 $k_\theta$ 的六矩分别为零。** R185 的投影一般改变 ruling；完整合法域将在第 9 节只施加 R184 真正必要的三列几何条件。

## 6. 一个可检查的导数包类及全部周期核

设 f 的非恒活动部分由有限个不交开区间

$$
J_j=(a_j,b_j),\qquad j=1,\ldots,m
\tag{34}
$$

组成，彼此之间有正长度的 f 常值间隙；f 在每个 $J_j$ 非恒，并且所有正阶 jets 在 $a_j,b_j$ 为零。允许这些端点的 f 值非零。

在各 $J_j$ 置

$$
p=f',\qquad A_f=6pp''-2(p')^2.
$$

另要求：

1. p 在 $J_j$ 内的零点是有限个有限阶零点；
2. $A_f$ 在 $J_j$ 的任何非空开子区间不恒零。

第二条等价于 $A_f\ne0$ 的集合在各 $J_j$ 稠密；允许任意孤立零点，包括无限阶零点，不要求其全部简单。可取内部解析的 step/补偿 bump 形状满足这些可检查条件，并保留原八包构造。R199 只换最后 g step，不迫 f 失去此性质。

R217 的非对称 $\rho_3$ 若在升降间放入正长度的**非零常平台**，则相应 p 不为零但 $A_f\equiv0$，不在本节类内。可选择该平台长度为零；升降在峰值平端相接，原非零 $J_*$ 仍保留。不能因此声称 R217 允许的所有圆都满足本节假设。条件不满足时，第 2–5 节仍成立，但后续应回到原退化 ODE 的真实核，而不能使用本节的核分类。

**定理 1。** 在 (34) 的条件下，$w\in\mathcal X$ 属于 $\ker L_f$，当且仅当：

- 每个活动区间上 $w=C_jf+B_j$，$C_j,B_j$ 为该区间的实常数；
- 每个 f 常值间隙上 w 是任意光滑函数；
- 这些片段在全部端点光滑匹配，并保共同零 collar。

**证明。** R181 的准确式是

$$
L_f(w)''=(A_fu')'-V_fu,\qquad
u=w',\quad V_f=6(p'p'')',
$$

$$
(A_fp')'=V_fp.
\tag{35}
$$

若 $L_f(w)=0$，则

$$
\{A_f(pu'-p'u)\}'=0.
\tag{36}
$$

在外 collar 上 $p=A_f=0$，故 (36) 的全局常数为零。在 $pA_f\ne0$ 处，

$$
(u/p)'=0.
$$

由 $A_f\ne0$ 的稠密性及连续性，这在 p 非零的每个连通分支上成立。若两个分支之间 p 有阶数 n 的零点，$u=C_\pm p$ 的第 n 阶导数连续，且 $p^{(n)}$ 在该点非零，迫 $C_-=C_+$。因此每个 $J_j$ 上 u 为同一个 $C_jp$，积分得 $w=C_jf+B_j$。

在 f 常值间隙上，$A_f=V_f=0$，微分方程对 w 没有约束。反过来，符合所列片段与光滑匹配的 w，在活动区间由 (35) 满足 $L_f(w)''=0$，在间隙也满足；于是全区间均为零。右 collar 上原 Volterra 式同时给 $L_f(w)=L_f(w)'=0$。这个全局仿射函数因而恒零。最后一步支付的是 **$L_f$ 本身**，没有漏掉由求两次导数丢失的右锚常数。证毕。

本定理允许所有 f 常平台上的自由 w，不把它们换成有限个局部测试函数，也没有把非零 p 常平台混入 f 常平台。

## 7. 整个周期核的准确矩像与固定有限右逆

定理 1 把无限维核分成有限端迹和各常值间隙的自由函数。现在只对有限矩映射 (29) 取其像，得到完整有限化。

### 7.1 有限端迹 profiles

为每个 $J_j$ 选 $\chi_j\in\mathcal X$，在 $\overline J_j$ 上恒 1、在其他活动区间上恒 0，其过渡全部放在邻接 f 常值间隙。定义

$$
\beta_{j,0}=\chi_j,\qquad
\beta_{j,1}=\chi_j f.
\tag{37}
$$

它们均在 $\ker L_f$；在每个活动区间上的限制分别给 1 和 f。由 f 非恒，各区间这两条端迹独立。把这些 profiles 编成 $\beta_1,\ldots,\beta_{2m}$。

任意核函数减去其活动区间上的 $B_j,C_j$ 组合后，在全部活动区间恒零。其余部分是各 f 常值间隙中的光滑函数，在间隙端点全部 jets 为零；最外间隙还须在原固定 collar 为零。反过来，所有这样的余函数都在核内。

把允许的这些开间隙记为 $K_\nu$，最外间隙只取 $[\ell_0,r_0]$ 内的部分。选一个固定 $\zeta_\nu$，在 $K_\nu$ 内严格正、在两端全部 jets 为零，并在该间隙外零延拓。它是共同 collar 内的光滑函数。

### 7.2 完整核 Gram 与 image 身份

记

$$
v_i=\mathcal M\beta_i\in\mathbb R^{132}.
$$

定义固定正半定矩阵

$$
\boxed{
G_{\rm ker}
=\sum_{i=1}^{2m}v_iv_i^T+
\sum_\nu\int_{K_\nu}
\zeta_\nu(x)\boldsymbol\rho(x)
\boldsymbol\rho(x)^T\,dx.}
\tag{38}
$$

**定理 2。**

$$
\boxed{
\operatorname{range}G_{\rm ker}
=\mathcal M(\ker L_f).}
\tag{39}
$$

这不是把任意核函数近似到有限网格。

**证明。** 对一个常值间隙，向量 b 消掉全部可允许函数的矩，当且仅当连续函数
$b^T\boldsymbol\rho$ 在该间隙恒零。因为所有内部紧支撑测试函数都允许，这是测试函数分离的准确结论。又因 $\zeta_\nu>0$，同一条件等价于

$$
\int_{K_\nu}\zeta_\nu(b^T\boldsymbol\rho)^2=0.
$$

因此该间隙的矩像与其 Gram 的像有相同正交补，在有限维空间中相同。加入所有端迹向量后，(38) 的核正是所有这些像的共同正交补。由第 7.1 节的整个核分解得到 (39)。证毕。

更强地，定义一个明确的有限 profile 家族

$$
\boxed{
\mathscr S z
=\sum_i(v_i^Tz)\beta_i+
\sum_\nu \zeta_\nu(x)\boldsymbol\rho(x)^Tz,
\qquad z\in\mathbb R^{132}.}
\tag{40}
$$

每个间隙项均作零延拓。定理 1 保证 $\mathscr S z\in\ker L_f$，直接积分给

$$
\boxed{\mathcal M\mathscr S z=G_{\rm ker}z.}
\tag{41}
$$

若 $b\in\mathcal M(\ker L_f)$，取
$z=G_{\rm ker}^+b$，其中 $+$ 是这个**固定**实对称矩阵的 Moore–Penrose 逆，便得到一个线性光滑-profile 右逆。所有真实线性关系由 $G_{\rm ker}$ 的核保留，不要求其可逆。

因此任意周期核函数在后续联合问题中的全部效果，都能由同一个至多 132 维固定 profile 空间实现。替换时保留的不是仅 ruling：六个合法性矩也在 (29) 中一同保留。

## 8. 第三历史造成的完整几何函数成员门

先取第 5 节的一个 $w_\theta^{\rm per}$。定义

$$
r_\theta(s)=K^0_\theta(s)
+\mathcal B_\theta(w_\theta^{\rm per})(s).
\tag{42}
$$

记

$$
\mathbf g_*(s)=
\begin{pmatrix}\mathbf g(s)\\ \mathbf w(s)\end{pmatrix}
\in\mathbb R^{45},\qquad
G_{\rm geo}=\int_{S^1_s}\mathbf g_*(s)\mathbf g_*(s)^T\,ds,
$$

$$
d_\theta=\int_{S^1_s}\mathbf g_*(s)r_\theta(s)\,ds.
\tag{43}
$$

真实几何的任何依赖都由这个固定 Gram 保留。由 (24)，任何二阶 gauge 改变量都在
$\operatorname{span}\{g_\rho\}$；第三齐次与 gauge 平方都在 $\operatorname{span}\{\mathbf w_i\}$。所以联合可解首先要求

$$
\boxed{
r_\theta\in\operatorname{span}\{g_{*,1},\ldots,g_{*,45}\}
\quad\text{对所有 }\theta.}
\tag{44}
$$

这是准确的全函数成员条件。它可写成

$$
\boxed{
r_\theta-\mathbf g_*^T G_{\rm geo}^+d_\theta=0,}
\tag{45}
$$

或写成一个真实非负残量为零：

$$
\int r_\theta^2\,ds-d_\theta^TG_{\rm geo}^+d_\theta=0.
\tag{46}
$$

canonical $K^0_\theta$ 含完整第三累计历史。其在 (45) 中的正交余项是一个具体的、对所有合法二阶及第三 gauge 不变的函数：因为 (42) 的第二项已经在上述 span，(45) 的余项恰等于 $K^0_\theta$ 的余项。这给出了第三历史不能被二阶/第三 gauge 修改的准确部分，未预设它为零或非零，也未把它与 R196 的字符等同。

$K^0_\theta$ 只有相位 $0,\cos2\theta,\sin2\theta,\cos4\theta,\sin4\theta$；由 (24)、(32)，$r_\theta$ 也只有这五个实系数。故 (44) 只需对五个固定真实 s 函数检验。不能用有限 s 节点的零值代替 (45)。

## 9. 保全部第三合法域的 48×135 联合矩阵

令 $P_6:\mathbb R^{132}\to\mathbb R^6$ 抽取 (29) 前六项，令

$$
C_\theta=(\cos\theta I_3\ \ \sin\theta I_3),
\qquad
G_W=\int_{S^1_s}\mathbf w(s)\mathbf w(s)^T\,ds.
\tag{47}
$$

由于 $w_\theta^{\rm per}$ 的六矩为零，R184 真正的新增第三 range 条件对
$w_\theta=w_\theta^{\rm per}+k_\theta$ 精确等价于

$$
\boxed{G_WC_\theta P_6\mathcal M k_\theta=0.}
\tag{48}
$$

这里使用事实：$\mathbf w(s)\cdot q$ 全函数零，当且仅当 $G_Wq=0$。没有假定几何三列独立；也没有把 (48) 加强为六矩分别零。

定义矩阵 $L_\theta:\mathbb R^{132}\to\mathbb R^{42}$，对每个 $\rho$ 从 (29) 的三矩槽抽取

$$
(L_\theta b)_\rho
=b_{\rho,0}+\cos2\theta\,b_{\rho,c}
+\sin2\theta\,b_{\rho,s}.
\tag{49}
$$

由 (39)–(41)，可以且无损地取
$k_\theta=\mathscr S z_\theta$。设 $v_\theta\in\mathbb R^3$ 表示希望保留给第三 gauge 的 ruling 三列值。则需要

$$
r_\theta+
\mathbf g^T L_\theta G_{\rm ker}z_\theta
-\mathbf w^Tv_\theta=0.
\tag{50}
$$

在 (44) 已成立的前提下，(50) 等价于它与全部 45 个生成函数的内积为零。因此准确的有限方程是

$$
\boxed{
\mathbb A(\theta)
\begin{pmatrix}z_\theta\\v_\theta\end{pmatrix}
=
\mathbb b(\theta),}
\tag{51}
$$

$$
\mathbb A(\theta)=
\begin{pmatrix}
G_{\rm geo}
\begin{pmatrix}
L_\theta G_{\rm ker}&0_{42\times3}\\
0_{3\times132}&-I_3
\end{pmatrix}\$$2mm]
G_WC_\theta P_6G_{\rm ker}\quad 0_{3\times3}
\end{pmatrix},
\qquad
\mathbb b(\theta)=
\begin{pmatrix}-d_\theta\\0_3\end{pmatrix}.
\tag{52}
$$

该矩阵有 48 行、135 列。其 entries 是实三角多项式，常系数均为固定实际资料的真积分。此尺寸保留冗余，不宣称 rank。

### 9.1 为什么这一有限化对全部 gauge 双向成立

若原问题有一个光滑合法全相位 gauge，由 (33) 得 $k_\theta$。其有限矩属于 (39)，故取

$$
z_\theta=G_{\rm ker}^+\mathcal M k_\theta.
$$

这是固定线性映射，保相位光滑、周期与种子；(41) 保全部 132 个矩，因而保 (48) 及 $\mathcal B_\theta$。真实 ruling 若属于 $\mathcal W$，用固定 $G_W$ 的右逆可选一个光滑 $v_\theta$ 表示它。于是得到 (51)。在两个种子，原 $K^0$、w 和 $w^{\rm per}$ 均为零，可同时选 $z=v=0$。

反过来，若 (44) 和 (51) 有同样光滑、周期、种子为零的解，取

$$
w_\theta=w_\theta^{\rm per}+\mathscr S z_\theta.
\tag{53}
$$

则 (30)、(48) 和 (50) 全部准确成立。它就是 R184 所需的**同一个**二阶 gauge。平方项仍在原 forcing 中；它与 (50) 留下的三列值，由 R184 的单 $\phi_\theta$ 三矩 Gram 右逆给出的 $\chi_\theta$ 准确支付。因每个 $\phi_\theta\ne0$，该 Gram 在紧相位圆上光滑正定，$\chi_\theta$ 光滑周期并在种子为零。最后 R56 完整 range 给第四场。

至此只剩 (51) 的全相位光滑解条件，不能停在逐点 rank 比较。

## 10. 有限降秩点条件准确支付全相位光滑性

设 $y_\theta=(z_\theta,v_\theta)$。所有原目标与 $w^{\rm per}$ 在
$\theta=0,\pi$ 为零，故 $\mathbb b(0)=\mathbb b(\pi)=0$。因 $\mathbb b$ 只有偶谐波至 4，

$$
\widetilde{\mathbb b}(\theta)
=\frac{\mathbb b(\theta)}{\sin\theta}
\tag{54}
$$

在两个零点作可去延拓后，仍是实三角多项式。任一光滑周期 y 在这两点为零，当且仅当

$$
y_\theta=\sin\theta\,\widetilde y_\theta
\tag{55}
$$

且 $\widetilde y$ 光滑周期；这是在两个简单零点各自使用 Hadamard 引理。于是种子问题准确化为

$$
\mathbb A(\theta)\widetilde y_\theta
=\widetilde{\mathbb b}(\theta).
\tag{56}
$$

### 10.1 可计算的有限准确条件

记 $n=48$，
$r_*=\max_\theta\operatorname{rank}\mathbb A(\theta)$。
若 $r_*=0$，(56) 可解当且仅当
$\widetilde{\mathbb b}\equiv0$，此时取零解。

若 $r_*>0$，令

$$
H(\theta)=\mathbb A(\theta)\mathbb A(\theta)^T,
$$

$$
\Delta(\theta)=e_{r_*}(H(\theta))
=\sum_{\text{全部 }r_*\times r_*\text{ 子式}}
\det(\mathbb A_{\rm sub}(\theta))^2.
\tag{57}
$$

这是一个非零、非负的实三角多项式，其零点集 $\Sigma$ 在相位圆上有限。定义 135 维三角多项式向量

$$
\boxed{
N(\theta)=
\mathbb A(\theta)^T[t^{\,n-r_*}]
\left\{\operatorname{adj}(tI_n+H(\theta))
\widetilde{\mathbb b}(\theta)\right\}.}
\tag{58}
$$

$t$ 只是一个新的形式标量；方括号为系数抽取。以下两个有限条件必要且充分：

**(i)** 增广矩阵
$[\mathbb A\mid\widetilde{\mathbb b}]$
的全部 $(r_*+1)$ 阶子式作为三角多项式恒零；若 $r_*=n$，这一条件自动成立。

**(ii)** 对每个 $\theta_*\in\Sigma$，N 的每个分量在 $\theta_*$ 的零点阶数都至少为 $\Delta$ 的零点阶数。等价地，对相应有限阶数以前的导数逐一为零。

这些是有限个真实代数/微分身份。它们不是数值小残差，也不是只在若干选点检查增广 rank。

### 10.2 证明与明确相位右逆

在 $\Delta>0$ 的最大秩开集，(i) 保证相容。由于

$$
\det(tI_n+H)
=t^{n-r_*}\{\Delta+O(t)\},
$$

且 $\widetilde{\mathbb b}$ 在 H 的像内，

$$
(tI_n+H)^{-1}\widetilde{\mathbb b}
=H^+\widetilde{\mathbb b}+O(t).
$$

比较相应系数，得到

$$
\boxed{
\frac{N(\theta)}{\Delta(\theta)}
=\mathbb A(\theta)^+\widetilde{\mathbb b}(\theta)}
\quad(\Delta>0).
\tag{59}
$$

右侧是相容方程的最小 Euclidean 范数解。

若已有一个光滑解，(i) 显然成立；最小范数解的范数不超过该光滑解，故 (59) 在每个降秩点邻域有界。一维实解析函数之商只有有限阶可能极点，有界恰迫分子零点阶数不低于分母。于是 (ii) 必要。这里不能把一般不连续的逐点 Moore–Penrose 逆直接当光滑右逆；使用的是准确消极点条件。

反过来，若 (i)、(ii) 成立，$N/\Delta$ 在所有 $\Sigma$ 点作可去延拓后是光滑、事实上实解析且周期的向量函数。在稠密最大秩集解 (56)，由连续性在全部相位也解 (56)。于是

$$
\boxed{
y_\theta=\sin\theta\,
\left(\frac{N}{\Delta}\right)_{\rm removable}(\theta)}
\tag{60}
$$

给所需的光滑周期、双种子零解。接 (53)、R184 的第三右逆及 R56 的第四恢复，便构造全部相位的第四形式场。证毕。

因此本稿没有假定解必须有有限相位谐波。式 (60) 是可去奇点的三角有理函数，通常可有无限 Fourier 展开，但它由有限准确数据决定。

## 11. 完整必要充分定理及实际未付数据

**定理 3。** 固定第 1 节的真实低阶背景、共同 collar 及满足第 6 节包条件的合法圆。允许 R184 的全部二阶、三阶齐次 gauge，保持目标度量、相位光滑周期和两个准确种子。则第四完整 range 可解，当且仅当：

1. 两个原目标通过 (31) 的完整函数成员门；
2. 取 (32) 后，五个原几何函数系数通过 (44)；
3. 对 (52) 的有限矩阵，(54)–(58) 满足第 10 节的相容和有限可去奇点条件。

选择第 1 项不同的特解只把后续目标平移一个完整周期核像，所以三项的联合可解性不依赖该选择。第 9–10 节给一个构造右逆；它没有限制二阶 gauge 只在某个导数包或旧十维核空间内。

本定理准确保留了尚可能失败的两个来源：**period 的原函数像**与**同一 gauge 的真实 ruling 矩像**。R220 的全域 Morse 性只消除了旧四阶 flat-point 障碍的前提，不使任何一项自动成立。

### 11.1 最小后继数据接口

对一个实际选定的几何与 profile，不需重编已完成的 universal 3974 根、W36、pure 权块或旧 word 关系。这里只需新的固定圆资料：

- 从原真实二阶 ODE 读取 8 个完整累计历史 $a_j(s)$，连同 h、d、$\gamma,\delta$ 形成 (19)、(20) 的 42 个几何函数；
- 由原完整三阶场读取 $K^0_\theta$ 的五个实相位系数，并保所有第三入历史；另读 R213 的两个真实 period 源 $V_d,V_e$；
- 用 (17)、(21)、(22)、(25)–(28) 形成 126 个 profile 矩密度，加 6 个第三合法性密度；
- 选第 7 节固定的端迹和 gap 权重，形成 $G_{\rm ker}$；形成 $G_{\rm geo}$、$G_W$ 及真实 target 内积；
- 先按原 degenerate ODE/Green 条件处理两个 period 目标，再检验完整几何残量及有限相位矩阵的真实关系与可去性。

(45) 若非零，就明确定位为 canonical 第三历史的一个全 gauge 不变量；(48) 或 (51) 若失败，则定位为相应真实矩/函数像不足。没有把这些不同失败合并成一个未说明的采样残差。

这些数据目前未对 R220 的存在性构造实际求值；本稿不虚构一个已冻结可计算几何。真正 profile 求积、ODE、原函数编译、rank 或候选判断仍须在本公开仓库 Actions 中按实际输入运行，并按根 README 第 15 条仅保源、参数、run 和 SHA。数值 Gram 的近零特征值本身不付准确函数身份。

### 11.2 结论边界

本稿新增的是任意 gauge 的完整有限矩映射、指定包类上全部 period 核的右逆，以及第四 joint 的必要充分接口。它没有构造一个已通过这套门的第四解，也没有支付更高阶、收敛、有限幅度等距族、闭嵌入、reach 或主课题的握持位移指标。完整 joint 仍是下一实际目标，不能由“有限化”或“有右逆公式”替代其原目标相容性。

