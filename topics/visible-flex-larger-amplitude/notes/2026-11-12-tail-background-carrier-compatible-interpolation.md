# 背景斜率 carrier 与真实正权残余插值

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）
日期：2026-11-12

**已证明，条件构造工具。** 本文在一个固定真实背景上构造新的非均值高度候选。它精确保留两个端点的物理高度、径向一阶与二阶 jet，并把背景线性方程中最强的 $1/w$ 斜率形状显式保留。完整 mean、实际径向导数和全部有限 Darboux 分子按 R64/R75/R77 验证。

本文不声称新候选必然比旧候选好，不声称外头方程、Green/Schur 或闭曲面已经完成。当前物理半径首子段的旧试验上界没有改善；本文是需要真实执行的新候选，不能用端点拟合或线性恒等式代替完整缺陷。

## 1. 固定背景与输入

取真实物理区间 $[r_L,r_R]$，$0<r_L<r_R$，记 $W=r_R-r_L$、$u=(r-r_L)/W$。固定背景 $w\in C^1([r_L,r_R])$，$w>0$。度量仍为 $g=(1+w^2)dr^2+r^2d\theta^2$，不改变原校准、warp、cap、真实半径或角变量。

给定实、非均值、有限 Fourier 端点场

$$
(H_L,S_L,Q_L),\qquad(H_R,S_R,Q_R),
\tag{C.1}
$$

其中 $S=H_r$、$Q=H_{rr}$ 都是物理 $r$ 导数。所有相邻段共享这些同一实数/角场，而不是分别选择区间中点。本文的积分盒始终包围已定义的同一个精确积分；重包积分不改变候选。

写 $H_L=\sum_{m\ne0}H_{L,m}e^{im\theta}$，并同样表示其余端点。可使用实 sine/cosine 表示；以下公式逐模作用且与该选择无关。对无限角级数推广时，定义下述 carrier 需要相应两阶角导数正则性；本文实际有限输入没有免费增加未知解的角导数。

## 2. 显式 carrier 及准确线性余量

定义角场

$$
a=-\frac{\partial_{\theta\theta}H_L}{r_L},
\qquad b=w_L(S_L-a),
\qquad A(r)=\int_{r_L}^{r}\frac{dt}{w(t)}.
\tag{C.2}
$$

于是 $a_m=m^2H_{L,m}/r_L$。定义

$$
F(r,\theta)=H_L(\theta)+a(\theta)(r-r_L)+b(\theta)A(r).
\tag{C.3}
$$

$A\in C^2$，且直接求导得到

$$
F_r=a+\frac b w,\qquad
F_{rr}=-\frac{b w_r}{w^2}.
\tag{C.4}
$$

因此 $F(r_L)=H_L$、$F_r(r_L)=S_L$。这在 $w_r=0$、任意 cap 分支以及 $w_R=w_L$ 时均有效；未除以 $w_r$ 或 $w_R-w_L$。

背景线性高度算子定义为

$$
\mathcal L f=f_{rr}+\frac{w_r}{w}f_r+
 \frac{w_r}{rw}f_{\theta\theta}.
\tag{C.5}
$$

这是由兼容高度的完整方程在旋转背景处线性化所得的算子。本文只使用其明确表达式。对每模定义 $\mathcal L_m f=f_{rr}+(w_r/w)f_r-m^2w_rf/(rw)$。式 (C.4) 给

$$
\boxed{\mathcal L F=\frac{w_r}{w}
 \left(a+\frac{F_{\theta\theta}}r\right),\qquad
\mathcal L_m F_m=\frac{w_r}{w}
 \left(a_m-\frac{m^2F_m}{r}\right).}
\tag{C.6}
$$

最强的 $b w_r/w^2$ 两项在此严格相消。由 $a_mr_L=m^2H_{L,m}$，还可写为

$$
a_m-\frac{m^2F_m(r)}r
=\frac{a_m(1-m^2)(r-r_L)-m^2b_mA(r)}r .
\tag{C.7}
$$

故 $\mathcal L_mF_m(r_L)=0$，并有直接可核算的整段界

$$
|\mathcal L_mF_m(r)|
\le\frac{|w_r|}{wr}
 \bigl(|a_m||1-m^2|(r-r_L)+m^2|b_m|A(r)\bigr).
\tag{C.8}
$$

这些是 carrier 的准确恒等式，不表示它满足完整非线性方程。二阶端点尚未强行设成方程右端，必须由下一节的残余保留指定输入。

## 3. 残余端点与五正矩

令 $G=H-F$。为得到 (C.1)，应精确使用残余端点

$$
\begin{aligned}
G_L&=0,&S^G_L&=0,&
Q^G_L&=Q_L+\frac{b w_{r,L}}{w_L^2},\\
G_R&=H_R-H_L-aW-bA_R,&
S^G_R&=S_R-a-\frac b{w_R},&
Q^G_R&=Q_R+\frac{b w_{r,R}}{w_R^2},
\end{aligned}
\tag{C.9}
$$

其中 $A_R=A(r_R)$ 是同一个正积分。不能在计算 $G_R$、$F(r_R)$ 或别的评价点时独立选择 $A_R$ 的中点。

对残余归一斜率 $\kappa=G_r/w$，物理 $r$ 到 $u$ 的准确端点变换为

$$
\kappa_j=\frac{S^G_j}{w_j},\qquad
\dot\kappa_j=\frac{WQ^G_j}{w_j}
 -\frac{Ww_{r,j}}{w_j}\kappa_j,\quad j=L,R,
\tag{C.10}
$$

点号仅表示 $u$ 导数。特别地 $\kappa_L=0$。沿用 R48 的四个 Hermite 基函数与 bubble：

$$
\begin{aligned}
q_{00}&=(1-u)^2(1+2u),&
q_{10}&=u(1-u)^2,\\
q_{01}&=u^2(3-2u),&
q_{11}&=-u^2(1-u),&
B&=u^2(1-u)^2 .
\end{aligned}
\tag{C.11}
$$

五个真实正矩为

$$
(I_{00},I_{10},I_{01},I_{11},I_B)
=\int_{r_L}^{r_R}w(r)(q_{00},q_{10},q_{01},-q_{11},B)(u(r))\,dr.
\tag{C.12}
$$

所有五项严格正。定义

$$
\kappa_3=\kappa_Lq_{00}+\dot\kappa_Lq_{10}
+\kappa_Rq_{01}+\dot\kappa_Rq_{11},
$$

$$
\lambda=
\frac{G_R-G_L-\kappa_LI_{00}-\dot\kappa_LI_{10}
-\kappa_RI_{01}+\dot\kappa_RI_{11}}{I_B},
\qquad \kappa_4=\kappa_3+\lambda B,
\tag{C.13}
$$

以及新的非均值候选

$$
\boxed{\widehat H(r)=F(r)+G_L+
  \int_{r_L}^{r}w(t)\kappa_4((t-r_L)/W)\,dt.}
\tag{C.14}
$$

### 定理 C.1：准确两端兼容与唯一性

(C.14) 是仿射空间 $F+\{G:G_r/w\text{ 是不超过四次的 }u\text{ 多项式}\}$ 中唯一具有 (C.1) 六个物理端点条件的候选。它为 $C^2$，保留实性、非均值、原有有限频率与任何给定的半周对称性。

**证明。** $I_B>0$ 使 (C.13) 唯一有定义。R48 的 Hermite 端点恒等式和 $B=B'=0$ 保留 (C.10) 的四个斜率条件；积分条件给 $G(r_R)=G_R$。准确求导给 $G_r=w\kappa_4$、$G_{rr}=w_r\kappa_4+w\dot\kappa_4/W$，代入 (C.10) 得残余两 jet，再加 (C.4) 得 (C.1)。任何两个这样的四次斜率之差都是一个角场乘 $B$，高度积分条件乘严格正的 $I_B$ 迫使该场为零。所有角运算为有限线性运算，因此频谱、实性和非均值保持。$w\in C^1$ 及 (C.4) 保证 $C^2$。证毕。

这是新的仿射试验空间，一般不同于原来 $H_r/w$ 直接取四次多项式的候选。因此新的残余 $\lambda$ 不能与旧候选的 $\lambda$ 求交，也不能把两候选的缺陷逐点取最小后称同一解。

## 4. 实际导数与完整线性相消的可核算形式

记 $\ell_r=w_r/w$，则总非均值归一斜率和其真实导数是

$$
\begin{aligned}
\bar K&=\frac{\widehat H_r}{w}
=\frac a w+\frac b{w^2}+\kappa_4,\\
\bar K_r&=-\frac{a w_r}{w^2}
-\frac{2b w_r}{w^3}+\frac{\dot\kappa_4}{W},\\
\widehat H_{rr}&=-\frac{b w_r}{w^2}
+w_r\kappa_4+\frac wW\dot\kappa_4 .
\end{aligned}
\tag{C.15}
$$

这些式子来自候选自身；不能用 Darboux 方程右端替代其中任何导数。作为避免区间中不必要相消的等价式，置

$$
P=\frac{\widehat H_\theta}{rw},\qquad T=P_\theta .
$$

则有完整场恒等式

$$
\boxed{\bar K_r+\ell_r(2\bar K+T)
=\frac{\dot\kappa_4}{W}
+\ell_r\left(2\kappa_4+
 \frac{a+\widehat H_{\theta\theta}/r}{w}\right).}
\tag{C.16}
$$

每模的最后分子还可用

$$
a_m-\frac{m^2\widehat H_m}r
=\frac{a_m(1-m^2)(r-r_L)-m^2b_mA(r)-m^2G_m(r)}r
\tag{C.17}
$$

评价，保留 $a_mr_L=m^2H_{L,m}$ 的准确关联。两种有效区间式可以相交；不允许省去其中真实项。式 (C.16) 只重写已知候选的线性部分，全部非线性和 mean 项仍按下一节计算。

## 5. 第一兼容式、完整 mean 与拼接

对 (C.14)，链式法则给

$$
P_r=\frac1r\bar K_\theta-\left(\frac1r+\ell_r\right)P.
\tag{C.18}
$$

因此 R44 的第一行残差恒等为零。设每个连续径向面板实际通过 R64 的完整 mean 根门、实正支和所用 Wiener 逆分母门。用同一完整角平均定义唯一根 $c(r)$，令 $K=c+\bar K$。

**定理 C.2：mean 两 jet 的接合。** 若相邻段共享同一个真实 $r,w,w_r,H,H_r,H_{rr}$，且各自根属于 R64 的同一可容许唯一分支，则公共端点的 $c,c_r$ 相同。选定一个全区间积分常数并定义

$$
h_0(r)=h_0(r_*)+\int_{r_*}^{r} w(t)(1+c(t))\,dt,\qquad
h=h_0+\widehat H,
\tag{C.19}
$$

即可得到整体 $C^2$ 高度候选。

**证明。** 给定共享 jet，$P,\bar K,T$ 及其真实 $r$ 导数在公共端点相同。具体地，$P_r$ 由 (C.18) 决定，$T_r=\partial_\theta P_r$，$\bar K_r=H_{rr}/w-\ell_r\bar K$。$z=w^2$ 和 $z_r=2ww_r$ 也相同。R64 的完整方程 $\mathcal M(c;P,\bar K,z)=0$ 在该点完全相同，严格单调性给相同根。隐函数微分
$c_r=-\partial_r\mathcal M/\mathcal M_c$ 的分子由上述同一真实 jet 和背景组成，分母严格正且相同，故 $c_r$ 相同。若不同面板选不同认证半径，R64 的根区间以零为中心，较小区间包含于较大区间，唯一性仍给同一根。由 (C.19)，$h_{0,r}=w(1+c)$、$h_{0,rr}=w_r(1+c)+wc_r$ 连续；非均值两 jet 已由定理 C.1 保证，混合与角二阶导数由相同有限 Fourier 数据保证。证毕。

这里没有逐节点重置 mean 高度。若在同一固定端点 jet 下替换旧候选，虽然两个外端的完整 $h_r,h_{rr}$ 相同，区间的 mean 高度改变量一般是

$$
\Delta h_0(r_R)-\Delta h_0(r_L)
=\int_{r_L}^{r_R}w(r)(c_{\rm new}(r)-c_{\rm old}(r))\,dr.
\tag{C.20}
$$

不能免费把它置零。只有一个自由竖直平移时，可以匹配一个位置常数并连续积分；若构造确实预先固定双端 mean 高度，(C.20) 必须单独作为边界条件支付。当前题目不应人为增加未指定的绝对 cuff 高度。

若全部端点场随相位作同一角平移，(C.2)–(C.14) 与该平移交换。完整角平均的唯一性使 $c,c_r$ 对这一相位不变；选择同一个高度常数后形成同样连续的相位族。一般有限维参数的 $C^2$ 连续性在固定背景、$I_B>0$ 及统一严格 mean 分支余量内也由上述显式式与隐函数定理得到。这些局部性质不替代全闭面及 reach。

## 6. 完整有限分子与缺陷验证

在物理 $r$ 坐标置 $E=1+w^2$、$U=K_\theta-P$、

$$
D=1-w^2(2K+K^2+EP^2),\qquad
L=1+K+ET .
$$

R64 的完整有限分子可准确写为

$$
\mathcal J=
 L\left[K_r+\ell_r(2K+T)\right]
-\frac Er U^2
-\ell_r\left[(K+T)^2+w^2(2KT+T^2-P^2)\right].
\tag{C.21}
$$

其中 $K_r=c_r+\bar K_r$，$c_r$ 是同一个完整 mean 根的实际隐函数导数。可用 (C.16) 将第一括号评价为
$c_r+2\ell_rc+\dot\kappa_4/W+
\ell_r[2\kappa_4+(a+\widehat H_{\theta\theta}/r)/w]$。
不能把 $K_r$ 设成 ODE 右端，从而人为删除残差。

若最高高度频率为 $m_*$，$\mathcal J$ 的完整频谱至多为 $2m_*$；$c,c_r$ 是完整均值，不是截断角根。对当前最高 $40$ 的输入必须保全 $0,\ldots,80$ 的全部实际非零频率。真实物理缺陷界使用

$$
|\operatorname{Darboux}(h)|
\le\frac{w^2}{rE^2}\|\mathcal J\| .
\tag{C.22}
$$

原 source 坐标 $x$ 仍用于支付背景和积分；此处独立变量是 $r$，所以 $r_r=1$。不得混用 $K_x$ 与 $K_r$ 或漏掉原 $r_x$。

完整连接根与第一兼容式给
$\langle\mathcal J D^{-3/2}\rangle=0$，故 R77 的零模改进可逐完整连续叶使用。所有 $E_{\max},D_{\min}$ 及角范数必须来自同一整叶，不能用中点代 supremum。达到这些门只说明候选缺陷已真实包围，外 Green/Schur 和真边界匹配仍独立。

## 7. 仅一个新增正积分及真实源算法

R48/R85 的五个正矩完全由固定背景和物理子区间决定。对本文新的残余，它们仍是 (C.12) 的同一积分，可以复用已验证的真实物理 $r$ 包；不能复用以 source $x$ 作为 Hermite 参数的不同积分。

唯一新增积分是

$$
A(r(x))=\int_{x_L}^{x}\frac{r_x(t)}{w(t)}\,dt.
\tag{C.23}
$$

其 integrand 严格正。在一个确定 cap 分支及绝对值符号的源叶上，对 $r_x/w$ 使用 R85 的 point Taylor 系数和全叶最高阶导数余项，给出严格局部积分。跨分支或根条带须保留全部可能分支并集；若不能确定解析分支，可直接用正的 $r_x/w$ 全叶范围乘真实源宽。不得调用只对 uncapped 源成立的简式。

完整有序分割上分别保存每叶正积分及总 $A_R$。端点 $A(x_i)$ 同时用前缀和与 $A_R$ 减后缀相交；叶内用正性给连续位置包围。左右高度可分别由 (C.14) 与从右端反积分评价并相交，以保同一 $A_R$、五总矩和候选系数的关联。所有积分除数必须有严格正下界。新增积分不改变背景或原端点数据。

## 8. 一致逼近与不保证改进的界限

若端点确实来自同一准确高度 $H$，先由其左端 jet 定义同一个 $F$，置
$\kappa_{\rm true}=(H_r-F_r)/w$。若在所选光滑子段上
$M_4=\sup_{u\in[0,1]}\|\partial_u^4\kappa_{\rm true}\|<\infty$，
R48 对残余直接给

$$
\|\bar K_{\rm true}-\bar K_{\rm cand}\|\le M_4/192,\qquad
\|H-\widehat H\|\le M_4 I_B/24,
$$

$$
\|H_{rr}-\widehat H_{rr}\|
\le \frac{13w}{32W}M_4+\frac{|w_r|}{192}M_4 .
\tag{C.24}
$$

carrier 在两者之差中严格消去。R48 的端点噪声及 $1/I_B$ 放大依然存在；本文没有证明 $M_4$ 比旧候选的小，也没有把真实保存数据当成准确轨道。必须对新候选实际计算完整域、mean、导数和缺陷，再决定是否采用。

## 9. 重做顺序与保留旧对象

1. 以已发布同一背景、原实际 M20 响应、ready 和 seg7 八子段输入为唯一依赖，核原 9 个共享端点及两外端完整 jet。不得从当前聊天数字重造任何丢失主数据。
2. 对原未推的物理 $r$ 首子段先 fresh 重做真实五矩和完整 R64/J/R77，采用新文件前缀并保存正式工具退出码、wait4 资源、所有输入/输出哈希。原 64415/12337 曾正式成功的历史与本次 fresh 结果分开；不冒认重建源码为原 SHA。
3. 当前选择仍是旧 seg7 source 插值；物理 $r$ 试验的较大上界不构成其真实残差的下界，也不得选入整段最优界。
4. 只对首子段新增 (C.23)，依 (C.9)–(C.14) 构造 carrier 残余候选。保存 $a,b,A_R$、残余两端三 jet、五正矩、$\lambda$、真实左右高度评价及完整 mean。所有量定义为固定实对象，不随评价点另选。
5. 对完整首子段执行实际 $H,H_r,H_{rr}$、有限 Horner、完整 mean/导数、$\mathcal J$ 全谱和 R77；分别保存保留频率与带外贡献、最坏整叶及有符号系数见证。点探针只作点结论。
6. 只有完整结果支持改进且所有端点/mean 身份成立，才把首子段替换进同一候选并重做完整源分割合成；其他七子段不自动展开。无改进则保留失败/界限并依据真实见证选择下一项。
7. 无论此局部结果怎样，完整外头的低/高频 Green、真内头参数一致性、非线性场球、完整闭合及全相位几何门仍按原完成标准继续。

## 10. 使用的已证明接口

- [R48](../results/R48-weighted-compatible-outer-interpolation.md)：五正矩、四次残余斜率和真实物理两 jet。
- [R64](../results/R64-general-outer-mean-and-compatible-defect.md)：一般外头的完整均值根及实际候选导数。
- [R75](../results/R75-complete-mean-transport-and-shear-constraint.md)：完整均值输运、单一高度常数及非精确中心残差项。
- [R77](../results/R77-complete-mean-defect-zero-mode.md)：完整连续叶的零模约束。
- [R85](../results/R85-physical-radius-positive-moments.md)：真实物理半径原函数、完整分支、正前后缀与 Taylor 余项。

本文正文是完整条件证明；数值执行另记，不把执行器中断时未保全的文件或未运行的检查当成证据。
