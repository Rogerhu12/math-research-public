# R75：固定 flat17 全周期 Sturm 传播与精确两端口

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / geometric_closure。

**状态：已证明；全文未参与者独审通过。** 本稿在当前同一解析 Target 的
整个 outward 第一物理周期上工作，不改物理参数。结论是背景线性化的
精确 Sturm 化、全部 Fourier 模的真实传播，以及两个外区的无指数角损耗
估计；不是非线性闭面、原尾 Robin 逆或当前数值入口的认证。

root 先前冻结稿
notes/2026-11-10-78718-geometry-flat17-linear-analytic-propagator-v1.md
（8466 B，SHA256 8d45cd27a130919073287792421f2d2af153a510f98511b695332a73d2667db2）
给固定正则参数的全周期估计。本稿全文读过该稿后，用精确标量化和
频率相关正则化改进，不改它的冻结来源。全部新论证在下文写出。

## 1. 同一完整线性系统及精确消去零阶项

令 $c=a'$、$Q=aa''$、$\bar p=(1-c^2)^{-1/2}$、
$\alpha=\bar p/a$。线性化变量为
$b=\tau\beta$、$p=\bar p+\tau\pi+O(\tau^2)$，
$U=(\beta,\pi)^T$。给定普通非齐次源 $f=(f_1,f_2)^T$ 时，完整方程为
$$
U_s=\alpha
\begin{pmatrix}0&-Q\\-1&0\end{pmatrix}U_u+
\begin{pmatrix}d_1&0\\0&d_2\end{pmatrix}U+f,
\tag{1}
$$
$$
d_1=-\frac ca(1-Q\bar p^2),\qquad
d_2=\frac{3cQ}{a}\bar p^2.
$$
它直接来自已证明的多项式 Gauss–Codazzi 系统。源 $f$ 是这里的实际
二分量源；没有把原 Darboux metric column 未经换算地塞入此位置。

由于
$$
\frac{\bar p'}{\bar p}=\frac{cQ}{a}\bar p^2,\qquad
d_1=\frac{\alpha'}{\alpha},\qquad
d_2=3\frac{\bar p'}{\bar p},
\tag{2}
$$
取
$$
x=\frac{\beta}{\alpha}=\frac{a\beta}{\bar p},\qquad
y=\frac{\pi}{\bar p^3},\qquad
H=\frac1{a^2\bar p},\qquad
r(s)=\int_0^s H(\tau)\,d\tau.
\tag{3}
$$
因为 $H>0$，$r$ 是全周期真实的递增径向坐标。直接代入得
$$
x_s=-Q\bar p^3y_u+\frac{f_1}{\alpha},\qquad
y_s=-H x_u+\frac{f_2}{\bar p^3}.
$$
故在 $r$ 坐标中精确为
$$
\boxed{\quad
x_r=-V(r)y_u+g_1,\qquad
y_r=-x_u+g_2,\qquad
V=a^2Q\bar p^4=\frac{a^3a''}{(1-c^2)^2},
\quad}
\tag{4}
$$
$$
g_1=a^3f_1,\qquad g_2=a^2\bar p^{-2}f_2.
\tag{5}
$$
这里没有剩余零阶势。齐次情形消去 $x$ 得
$$
y_{rr}=V(r)y_{uu},\qquad
y_{j,rr}+j^2V(r)y_j=0.
\tag{6}
$$
有源情形则在分布意义下
$$
y_{j,rr}+j^2Vy_j=-ijg_{1,j}+\partial_rg_{2,j}.
\tag{7}
$$
(7) 只用于弱形式；不要求原源多一次径向导数。保留 (4) 的一阶系统
即可对任何 $L^1_r$ 源逐模式定义真正解。

记 $Z=(x,y)^T$。第 $j\in\mathbb Z$ 模的齐次基本解是
$$
Z_j'=-ij
\begin{pmatrix}0&V\\1&0\end{pmatrix}Z_j,\qquad
T^Z_j(r_1,r_1)=I.
\tag{8}
$$
它是连续系数有限维 ODE 的实际基本解，不是大频率形式展开。
当 $j=0$ 时恰为恒等传播；均值没有删除。

## 2. 实际周期、符号区间及统一常数

所有输入常数均保原 exact-binary 实值：
$\varepsilon=.4$、$\eta=.05$、$v_u=.17$、$v_d=.18$、
$\delta=.07254443456654512$。原解析 Target 的精确时长是
$$
T_u=\frac{\delta}{v_u(1-\varepsilon)},\qquad
T_d=\frac{\delta}{v_d(1-\varepsilon)},\qquad T=T_u+T_d.
\tag{9}
$$
令
$$
s_-=(1-\varepsilon)T_u,\qquad s_+=T_u+\varepsilon T_d.
\tag{10}
$$
则实际 $a''$ 的符号排列是：

- $[0,s_-]$ 为第一个正加速度 ramp 加其后开放平段，$V\ge0$；
- $[s_-,s_+]$ 为上升减速与下降加速两段，$V\le0$；
- $[s_+,T]$ 为第二个开放平段及末个正加速度 ramp，$V\ge0$。

在 $s=T_u$ 中央两段之间，$V=0$ 但不变号。开平段与所有二次零点
原样保留，没有把这些区间替成简单根模型。令
$R=r(T)$、$r_-=r(s_-)$、$r_+=r(s_+)$。

记 $P=51/50$、$A=43/40$。已在实际参数的有理包含中核明
$$
1\le a<A,\quad 1\le\bar p<P,\quad
|a''|<\frac34,\quad T<\frac32.
\tag{11}
$$
其中 $\bar p<P$ 来自
$P^2(1-(181/1000)^2)>1$；其余界直接由原 ramp 多项式及精确 Tu/Td 得到。
后文使用的严格有理比较为
$$
A^3P^4<\frac{27}{20},\quad
A^3<\frac54,\quad P^4<\frac{11}{10},\quad
A^2P<\frac65,\quad AP^3<\frac{23}{20}.
\tag{12}
$$
所以置 $\omega=a^3\bar p^4$、$v=|a''|$，有
$$
|V|=\omega v<\frac{81}{80}=:V_*,
\qquad \frac56<H\le1,\qquad R<\frac32.
\tag{13}
$$

原 turn_ramp 的加速度形状 $d(t)$ 在每个 ramp 上非负，从0单调上升到
平台，再单调下降到0；在两端小段它是
$(3z^2-2z^3)/(1-\eta)$，$0\le z\le1$，其导数为非负的
$6z(1-z)/(1-\eta)$。因此每个 ramp 的 $v=|a''|$ 都恰有这一升降结构。
在整个周期 $\bar p$ 依次从1升到
$P_u=(1-v_u^2)^{-1/2}$、降到1、升到
$P_d=(1-v_d^2)^{-1/2}$、再降到1。故
$$
\int_0^T(\log a)'_+\,ds=\log(1+\delta),\qquad
\int_0^T(\log\bar p)'_+\,ds=\log P_u+\log P_d.
\tag{14}
$$
负变差总量同正变差总量，因为两个函数周期端值相同。
这里 $h'_+$ 表示 $\max(h',0)$，不是先取 $h_+$ 再求导。

此外，中央物理宽度 $\varepsilon(T_u+T_d)>1/2$，可直接由
$$
\frac{399}{1000}\frac{9/125}{601/1000}
\frac{2000}{181}>\frac12
\tag{15}
$$
推出。结合 (13)，得到后续中央能量估计可用的真实宽度
$$
\frac{5}{12}<r_+-r_-<\frac32.
\tag{16}
$$

## 3. 频率相关正则化和正变差估计

对每个整数模取
$$
n_j=\sqrt{1+j^2},\qquad m_j=n_j^{-1},\qquad
q_j(r)=\sqrt{|V(r)|+m_j^2},\qquad
S_j=\operatorname{diag}(1,q_j).
\tag{17}
$$
$V$ 在实际分段多项式背景下绝对连续；$q_j\ge m_j>0$，所以所有
退化端点和开平段都在同一能量里。对 $W_j=S_jZ_j$，
$$
W_j'=-ij
\begin{pmatrix}0&V/q_j\\q_j&0\end{pmatrix}W_j+
\operatorname{diag}(0,q_j'/q_j)W_j.
\tag{18}
$$
乘 $-i$ 的主矩阵的 Hermitian 部分的最大特征值绝对值是
$$
\chi_j(V)=\frac{|V|+m_j^2-V}{2\sqrt{|V|+m_j^2}}
\le\sqrt{V_-}+\frac{m_j}{2}.
\tag{19}
$$
对 $V\ge0$ 这是 $m_j^2/(2q_j)\le m_j/2$；
对 $V=-z^2\le0$，把右侧乘 $2\sqrt{z^2+m_j^2}$ 并平方，余量为
$4m_jz^3+m_j^2z^2+4m_j^3z\ge0$。因此并未把非负势区按指数损耗计算。

零阶对角项的最大特征值仅需 $(q_j'/q_j)_+$，不用其绝对值。于是
沿向前路径
$$
\frac{d}{dr}|W_j|
\le\left\{|j|\sqrt{V_-}+\frac{|j|m_j}{2}
              +(\log q_j)'_+\right\}|W_j|.
\tag{20}
$$
反向路径把相应的负变差改为正变差，后续总界同样成立。

关键是对正变差积分，不用 $m_j^{-2}\int|V'|$。由 $|V|=\omega v$，
几乎处处
$$
(\log q_j)'_+
\le\frac12(\log\omega)'_+
+\frac12\frac{(v')_+}{v+m_j^2/\omega_{\max}}.
\tag{21}
$$
此处导数可在 $r$ 或在 $s$ 中一致使用；时间变换正向，积分相同。
证明是
$(\omega'v+\omega v')_+\le(\omega')_+v+\omega(v')_+$，
再分别用 $\omega v+m_j^2\ge\omega v$ 和
$m_j^2/\omega\ge m_j^2/\omega_{\max}$。$v=0$ 处由绝对连续性与
原有正分母保证公式仍几乎处处有效。

每个 ramp 的上升部分于是贡献至多
$$
\int\frac{(v')_+}{v+m_j^2/\omega_{\max}}
\le\log\left(1+\frac{V_*}{m_j^2}\right).
\tag{22}
$$
四个 ramp 的此项共四次。由 (14)，
$$
\begin{aligned}
\exp\int_0^R(\log q_j)'_+\,dr
&\le (1+\delta)^{3/2}(P_uP_d)^2
       (1+V_*n_j^2)^2\\
&<\frac{99}{80}(1+V_*n_j^2)^2.
\end{aligned}
\tag{23}
$$
最后用 $A^{3/2}<9/8$ 与 $P^4<11/10$。
反向总正变差满足同一上界；任意子区间的正变差不超过全周期相应总量。

## 4. 整个周期的真正全模 Cauchy 界

定义正势与负势的准确作用量
$$
\Omega(s,t)=
\left|\int_t^s\frac{\bar p}{a}\sqrt{Q_-}\,d\tau\right|
=\left|\int_{r(t)}^{r(s)}\sqrt{V_-}\,dr\right|.
\tag{24}
$$
固定模在任意两点的实际传播由 (20)–(23) 得
$$
\begin{aligned}
\|T^Z_j(r(s),r(t))\|
&\le
\frac32 n_j\,
e^{3/4}\,\frac{99}{80}
  (1+V_*n_j^2)^2 e^{|j|\Omega(s,t)}\\
&<17\,n_j^5 e^{|j|\Omega(s,t)}.
\end{aligned}
\tag{25}
$$
这里用了
$\|S_j\|\le3/2$、$\|S_j^{-1}\|\le n_j$、
$|j|m_jR/2<3/4$，以及
$$
e^{3/4}<\frac{11}{5},\qquad
\frac32\frac{99}{80}
\left(\frac{161}{80}\right)^2\frac{11}{5}<17.
\tag{26}
$$
所有因子独立于 $j$。矩阵 $j=0$ 也在该估计内。
变回 $U$ 时，坐标矩阵为
$\mathcal R(s)=\operatorname{diag}(a/\bar p,\bar p^{-3})$，
且
$\|\mathcal R(s)^{-1}\|\|\mathcal R(t)\|\le AP^3<23/20$。
所以原物理线性化的基本解满足
$$
\boxed{\quad
\|T^U_j(s,t)\|
\le20\,\langle j\rangle^5 e^{|j|\Omega(s,t)}
\quad(0\le s,t\le T).\quad}
\tag{27}
$$
这替代固定小正则参数下的巨大指数常数。它保留五次角导数损失，不把
这个损失隐藏为无损估计。

对当前周期，只有两段 $Q<0$。各 ramp 用
$|a''|=(v_{\rm speed}/(\varepsilon T_v))d(t)$、$ds=\varepsilon T_vdt$、
$\int_0^1d=1$ 及 Cauchy–Schwarz，有
$$
\int_{\rm ramp}\sqrt{|a''|}\,ds
\le\sqrt{\frac{\delta\varepsilon}{1-\varepsilon}}.
$$
因 $a\ge1$，遂得
$$
\Omega(T,0)\le
\sqrt{\frac{\delta\varepsilon}{1-\varepsilon}}(P_u+P_d)
<\frac{459}{1000}.
\tag{28}
$$
最后严格界使用
$(3/40)(401/599)<81/1600$ 与 $P_u,P_d<51/50$。

例如定义共同 Fourier 权
$e^{\sigma|j|}\langle j\rangle^k$，取
$\sigma(s)=\sigma_0-\Omega(s,0)>0$，则逐模式的真正变常数公式给
$$
\|U(s)\|_{\sigma(s),k}
\le20\left\{\|U_0\|_{\sigma_0,k+5}
+\int_0^s\|f(t)\|_{\sigma(t),k+5}\,dt\right\}.
\tag{29}
$$
Minkowski 不等式和 (27) 同时给解的收敛与估计，不先假定完整角解。
系数连续时每模存在；正剩余解析宽度使任意更窄带上的全部角导数一致
收敛。源可积给 mild 解，源连续给经典解。没有作 Fourier 截断。

## 5. 两个实际外区仅有两次角导数损失

在左外区 $[0,s_-]$，$a$ 与 $\bar p$ 都不下降，故 $\omega=a^3\bar p^4$
单调不下降。在右外区 $[s_+,T]$，两者都不增加，故 $\omega$ 单调
不增加。沿外端走向中央时，两区的 $\omega$ 都单调不下降；反方向
没有更大的正变差。各外区的 $v=|a''|$ 只有一个升至平台再降为零的
ramp，其余为开平段。因此对任何位于同一外区的两点，(21) 只需
一次 (22)，并且
$$
\exp\int(\log q_j)'_+\,dr
\le\sqrt{\omega_{\max}}\sqrt{1+V_*n_j^2}
<\frac65\frac32 n_j.
\tag{30}
$$
$V\ge0$ 使 (20) 的 $\sqrt{V_-}$ 项完全为零，故
$$
\boxed{\quad
\|T^Z_j(r_2,r_1)\|\le6\langle j\rangle^2
\quad(r_1,r_2\hbox{ 在同一个实际外区}).\quad}
\tag{31}
$$
常数核算是
$$
\frac32\frac65\frac32\frac{11}{5}
=\frac{297}{50}<6.
$$
它允许两个方向，也包括开放平段。源由同一变常数公式获得
$$
|Z_j(r_2)|
\le6\langle j\rangle^2
\left\{|Z_j(r_1)|+\int_{\text{该路径}}|g_j(r)|\,dr\right\}.
\tag{32}
$$
这是实际外区的完整非齐次传播，不是一次 WKB 主项。
(16)、(31) 和中央的 $V\le0$ 正是后续中央强制问题所需的有效输入；
本稿没有从这些输入跳过该内部问题的证明。

## 6. 精确通量与逐模两端口散射

令
$$
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
P_0=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\tag{33}
$$
(8) 的系数矩阵 $\mathcal A_j$ 满足
$\mathcal A_j^*J+J\mathcal A_j=0$、$\operatorname{tr}\mathcal A_j=0$。
故任意实际齐次传递 $T^Z_j$ 都满足
$$
(T^Z_j)^*JT^Z_j=J,\qquad \det T^Z_j=1.
\tag{34}
$$
取整个周期传递的通量坐标
$$
\widetilde T_j=P_0T^Z_j(R,0)P_0
=\begin{pmatrix}A_j&B_j\\C_j&D_j\end{pmatrix}.
$$
它保持 $\operatorname{diag}(1,-1)$。将其逆的伴随表达与行列式一的
二维逆式比较，得
$$
D_j=\overline{A_j},\quad C_j=\overline{B_j},
\quad |D_j|^2-|B_j|^2=1,\quad |D_j|\ge1.
\tag{35}
$$
所以这项具体端口消元不需要另行排除分母零点。

写 $z=P_0Z$，把左侧 $z_+$、右侧 $z_-$ 记作两个 incoming 量，把
左侧 $z_-$、右侧 $z_+$ 记作两个 outgoing 量。这些名称仅指所选通量
符号下的端口方向。直接消去左侧 $z_-$ 给
$$
\binom{z_-(0)}{z_+(R)}
=
\mathcal S_j\binom{z_+(0)}{z_-(R)},\qquad
\boxed{\quad
\mathcal S_j=
\begin{pmatrix}-C_j/D_j&1/D_j\\1/D_j&B_j/D_j\end{pmatrix}.\quad}
\tag{36}
$$
由 (35) 可逐列核算 $\mathcal S_j^*\mathcal S_j=I$。
因此这个已经实际构造的逐模边界算子，在任意两端口共用的正 Fourier
权中延拓为范数恰一的酉算子，含解析、Sobolev 或 log 权。
$j=0$ 时 $T=I$，$\mathcal S_0$ 是交换矩阵，未漏掉均值。
实系数还给 $\mathcal S_{-j}=\overline{\mathcal S_j}$。

为避免误用范围：端口算子的加权酉延拓本身不保证任意低正则 incoming
在整个内部存在同类解。带宽大于 (28) 的解析输入可由 (27) 真正重构
内部。若要取消解析带损耗，须利用中央单一非正势区作进一步内部估计，
不能只凭 (36) 省略这步。

有普通源时，令
$$
w_j=P_0\int_0^R T^Z_j(R,r)g_j(r)\,dr
=\binom{w_{+,j}}{w_{-,j}}.
$$
则精确仿射散射式为
$$
\mathrm{out}_j=\mathcal S_j\,\mathrm{in}_j+
\binom{-D_j^{-1}w_{-,j}}
{w_{+,j}-B_jD_j^{-1}w_{-,j}}.
\tag{37}
$$
这保留了源的两个分量；没有用齐次 unitary 身份把源列删除。
其原始积分可先在 (29) 的解析类内使用；其它权中的内部和普通源界
要另由真实估计支付。原尾 Robin 反馈也不是这里自动选定的
incoming 条件，不能据 $|D_j|\ge1$ 声称原反馈逆已经存在。

## 7. 单位换算与后续接口的边界

整周期两端 $a=1$、$c=0$、$\bar p=1$，所以 $Z=U$，没有隐藏的端点
缩放。对普通源的物理 $L^2_s$ 与 Sturm $L^2_r$，(5)、$H\le1$ 和
(12) 给
$$
\|g\|_{L^2_r}\le A^3\|f\|_{L^2_s}
<\frac54\|f\|_{L^2_s}.
\tag{38}
$$
反过来，$U=\operatorname{diag}(\alpha,\bar p^3)Z$、
$ds/dr=a^2\bar p$，所以
$$
\|U\|_{L^2_s}
\le AP^{7/2}\|Z\|_{L^2_r}
<\frac65\|Z\|_{L^2_r}.
\tag{39}
$$
最后严格比较可平方后用有理数核算
$A^2P^7<36/25$。这些是原两种坐标的真实变换，不改变源或度量。

本稿只处理固定旋转背景的线性化。当前非径向有限候选的线性化有角依赖
系数，不能直接继承 (8) 的逐模解耦；实际核心还含完整高 support 修正、
固定 chart 及有限投影误差，不能用单频近似替代其入口。

下一步的真正二维任务是利用中央 $V\le0$ 及外区 (31)，支付无解析带
损耗的全内部/普通源估计，再处理非线性扰动、原尾反馈与闭曲面接合。
本稿没有支付后面这些门，没有改变主数值运行或它的完成标准。

## 8. 冻结来源、完整独审和实际回执

本结果数学正文由[冻结原稿](../notes/2026-11-10-78718-geometry-flat17-sturm-frequency-provider-v1.md)转录，只改标题和可信度声明；
原稿 14295 B，SHA256 `68962bac35e0a6969ce159b17e0b7754698cffc816248ddfb596c35a7a93f5db`，冻结文件保持原样。
[全文未参与者独审](../notes/2026-11-10-78718-audit-flat17-sturm-frequency-provider-v1.md)为 17678 B，
SHA256 `2342490bf048e45797d2ff278055228f1a081d6532bcda340f735fbe1b8279e2`；root 已用真实只读回执 4902bb 全文回读，准确范围内通过。

[有限代数/有理检查源码](../scripts/78718-geometry-flat17-sturm-frequency-check.py) 5338 B，
SHA256 `83735a6881a9934b8a0611ddef302bdfa0e3ce6844fbb92a997bc6ac4ec215ee`。
未参与者实际 `2ce6a8` 自然 exit0；
[独立运行报告](../notes/2026-11-10-78718-audit-flat17-sturm-frequency-check-01.json) 1710 B，
SHA256 `e0fce82bc3130307c0a6ff3ea3879ff7583ed798cb22f5bc2019498573ea9fcd`。有限检查不替代上文完整证明，0 PDE/0新曲面候选。

这是中间模块；原文列出的实际入口、原尾边界、非线性全域闭合、全时嵌入/reach及G5义务均保留。
