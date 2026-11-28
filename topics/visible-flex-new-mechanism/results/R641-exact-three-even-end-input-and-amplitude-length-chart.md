# R641：第三真实偶端的准确幅值／长度图与原盒内显式三端输入

2026-11-28；会话 `Astra-new-mechanism-8cdb3418-20261128`。

**已证明：对同一真实 h/κ，动能与 s₀ 两个偶端可由一个明确的 2×2 线性系统同时消去幅值平方和长度倒平方。R636 的具体背景处于这个非退化正分支，所得新 L、α 仍严格在全部原物理盒内，因此给出准确满足 A_p1=A_t1=A_s0=0 的实际 C² 输入。** 配合 R638 的真实 P 图，其小邻域也保持这三个原偶端，余下 A_r1 与完整 ruling 继续作为真实目标。

本稿是连续积分的纸面构造；没有科学数值执行，没有把积分打印值设为零，没有给出余下 r₁、完整 ruling、closed-surface、period/pose、嵌入或 reach 的完成证明。

## 1. 同一真实形状上的五个基础积分

设 h,κ∈C²[0,1]，h>0，κ(0)=0，保留原中心和末端 germ。定义

\[
\eta_0(x)=\int_0^x\frac{\kappa_y}{2h}\,dy,\qquad
d_0=h\eta_0-\kappa,\qquad
v_0=(d_0)_x=h_x\eta_0-\frac{\kappa_x}{2}.
\tag{1}
\]

记

\[
K_0=\int_0^1\kappa^2,\qquad
U=\int_0^1(h_x/h)^2,
\tag{2}
\]
\[
S_2=\int_0^1\frac{\eta_0d_0}{h},\qquad
S_4=\int_0^1\frac{\eta_0\kappa d_0^2}{h},\qquad
W_0=\int_0^1\frac{v_0^2}{h^2}.
\tag{3}
\]

这些量均由同一 h/κ 和真实 η₀ 得出。下标 2、4 表示整体幅值的次数，不表示截断近似。取正幅值 α、正物理长度 L，并令

\[
k=\alpha\kappa,\quad \eta=\alpha\eta_0,\quad d=\alpha d_0,
\qquad s=\alpha^2>0,\quad z=L^{-2}>0.
\tag{4}
\]

[R612](R612-exact-physical-length-elimination-and-three-true-end-integrals.md) 的完整原槽身份给

\[
\frac{8A_{t_1}+2A_{p_1}}L=sK_0-1-Uz,
\tag{5}
\]
\[
\frac{4A_{s_0}}L
=\int\frac{\eta d(kd-1)}h-z\int\frac{d_x^2}{h^2}
=s^2S_4-sS_2-sW_0z.
\tag{6}
\]

式 (6) 保留全部静态四次、静态二次和速度二次项；没有忽略真实 η 的形状依赖。

## 2. 一般非退化正图与准确覆盖范围

令

\[
D=US_4-K_0W_0,\qquad N=K_0S_2-S_4.
\tag{7}
\]

假设 K₀>0、U>0、D≠0 且 N/D>0。则令

\[
\boxed{z=\frac ND,\qquad L=z^{-1/2},\qquad
s=\frac{1+Uz}{K_0},\qquad\alpha=\sqrt{s}.}
\tag{8}
\]

这些量唯一、有限、正，并准确支付 (5)(6)。证明是把两式在 s>0 下写成

\[
\begin{pmatrix}K_0&-U\\ S_4&-W_0\end{pmatrix}
\begin{pmatrix}s\\ z\end{pmatrix}
=\begin{pmatrix}1\\ S_2\end{pmatrix}.
\tag{9}
\]

行列式恰为 D，Cramer 法则给 z=N/D，再由首行给 s；s>0 由 K₀,U,z>0 得出。反向，任何同一基础形状上的正幅值、正长度解，只要 D≠0，就必须等于 (8)。因此这是两端的准确图，不是仅满足某个替代目标的参数化。

本图的覆盖**限于 D≠0 的正分支**。D=0、N≠0 时 (9) 不相容；D=N=0 时两行相容且可能有一条 s/z 解线，仍须检查正性与全部物理条件。后者没有被证明不可能，不能把本图失败升级为原方程无解。

此外还必须实际保留 L∈[2.1,7.9]、h/k/η/γ/υ 的原盒。一般形状上，(8) 的正性本身不支付这些条件。R632 的固定非零负 κ_x(0) 只选择中心导数的一个幅值支，也不应被冒称覆盖另一个符号支。

## 3. 与真实 P 图组成三个独立的原偶端消元

记

\[
P_0(h,\kappa)=-\int\kappa d_0,
\qquad \frac{A_{p_1}}L=sP_0.
\tag{10}
\]

若形状先按 [R638](R638-exact-P-and-kinetic-two-end-shape-chart.md) 的真实末高度控制 b_h（该稿中的 b）解到 P₀=0，则 (8) 立即给

\[
\boxed{A_{p_1}(L)=A_{t_1}(L)=A_{s_0}(L)=0.}
\tag{11}
\]

这不是同一控制重复支付多个方程。在共同根处，选择等价归一化方程

\[
F_1=sP_0,\qquad F_2=sK_0-1-Uz,\qquad
F_3=sS_4-S_2-W_0z,
\]

对控制 (b_h,s,z) 的 Jacobian 具有首行 \((sP_{0,b_h},0,0)\)，其右下 2×2 块就是 (9)，故

\[
\det D_{(b_h,s,z)}(F_1,F_2,F_3)=sP_{0,b_h}D\ne0.
\tag{12}
\]

由原矩改到这些方程只乘除 L、s 和固定正数，均非零。R638 给 P₀,b_h≠0；本稿在 R636 背景上具体证明 D<0，而非假定完整端图满秩。

R638 的增加 σ 再消 b 的空间保留 129 个原 h 方向、127 个原 κ 方向和独立 L，共 257 个自由参数。现在进一步用真实 s₀ 方程确定 L，剩下 **256 个自由形状参数**。两个形状方向集合仍完整保留；消掉的是有明确非零控制行列式的物理 L，不能继续称它为一个独立自由列。唯一未自动支付的偶端是 A_r1；原奇 A 尾锚、末双速度与全部原历史仍照常构造。

## 4. 全部形状导数，不能冻结新 L 或 α

对真实总方向 (ḣ,κ̇)，其中 ḣ 已包含 R638 的隐式 \(\dot b_h\sigma\)，

\[
\dot\eta_0(x)=\int_0^x\left(\frac{\dot\kappa_y}{2h}
-\frac{\kappa_y\dot h}{2h^2}\right)dy,
\quad
\dot d_0=\dot h\eta_0+h\dot\eta_0-\dot\kappa,
\quad
\dot v_0=\dot h_x\eta_0+h_x\dot\eta_0-\frac{\dot\kappa_x}{2}.
\tag{13}
\]

于是

\[
\dot K_0=2\int\kappa\dot\kappa,
\qquad
\dot U=2\int\frac{h_x}{h}
\left(\frac{\dot h_x}{h}-\frac{h_x\dot h}{h^2}\right),
\tag{14}
\]
\[
\dot S_2=\int\left(\frac{\dot\eta_0d_0+\eta_0\dot d_0}{h}
-\frac{\eta_0d_0\dot h}{h^2}\right),
\tag{15}
\]
\[
\dot S_4=\int\left(
\frac{\dot\eta_0\kappa d_0^2+\eta_0\dot\kappa d_0^2
+2\eta_0\kappa d_0\dot d_0}{h}
-\frac{\eta_0\kappa d_0^2\dot h}{h^2}\right),
\tag{16}
\]
\[
\dot W_0=2\int\left(\frac{v_0\dot v_0}{h^2}
-\frac{v_0^2\dot h}{h^3}\right).
\tag{17}
\]

完整链为

\[
\dot N=S_2\dot K_0+K_0\dot S_2-\dot S_4,
\quad
\dot D=S_4\dot U+U\dot S_4-W_0\dot K_0-K_0\dot W_0,
\]
\[
\boxed{\dot z=\frac{D\dot N-N\dot D}{D^2},\quad
\dot L=-\frac{L\dot z}{2z},\quad
\dot s=\frac{z\dot U+U\dot z}{K_0}-\frac{s\dot K_0}{K_0},\quad
\dot\alpha=\frac{\dot s}{2\alpha}.}
\tag{18}
\]

然后 k̇=α̇κ+ακ̇、η̇=α̇η₀+αη̇₀，且

\[
\dot\gamma=\frac{\dot h_x}{L}-\gamma\frac{\dot L}{L},\qquad
\dot\upsilon=\frac{\dot\alpha\kappa_x+\alpha\dot\kappa_x}{L}
-\upsilon\frac{\dot L}{L},
\tag{19}
\]
\[
\dot a=\frac{\dot h_{xx}}{L^2}-2a\frac{\dot L}{L},\qquad
\dot b=\frac{\dot\alpha\kappa_{xx}+\alpha\dot\kappa_{xx}}{L^2}
-2b\frac{\dot L}{L}.
\tag{20}
\]

式 (20) 的 b 是原加速度 k_ss；末高度控制另记 b_h。八 A 的 L 倍密度、六 ρ、全原母系数、正势、中心 ζ₀ 和两全程常 gauge 必须继续消费 (13)–(20)，不能在得出新长度后冻结长度链。

## 5. R636 背景上的准确降维积分

沿用 [R636](R636-explicit-c2-physical-input-with-two-true-even-ends.md) 的同一个连续背景 h/κ，不做旧 spline 的插值替代：

\[
H=17/20,\quad e=1/4,\quad\ell=3/4,\quad
I=1636/3465,\quad R=3+2eI/\ell=34457/10395,
\]
\[
\psi(t)=t+4t^3-7t^4+3t^5,\qquad S(t)=10t^3-15t^4+6t^5.
\]

前段 h=H、κ=−ψ(x/e)，后段 h=H[1+(R−1)S((x−e)/ℓ)]、κ=−1。R636 已证明这条 h/κ 真正 C² 且 P₀=0。这里重新选 L 与 α，不能借用 R636 的 L=4 物理资格。

设

\[
Z(t)=1+(R-1)S(t),\qquad T=\int_0^1\frac{dt}{Z(t)},
\quad I_4=\int_0^1\psi^4,\quad J=\int_0^1(\psi')^2=43/35,
\]
\[
A=eI-\ell+2\ell T,\qquad c=\frac e2(I-I_4).
\tag{21}
\]

J 的值由 `ψ'=1+12t²−28t³+15t⁴` 平方逐项积分得到；没有数值求积。直接分别积分前后两段可得

\[
\boxed{K_0=\ell+eI,\qquad
S_2=-\frac{A}{4H^2},\qquad
S_4=\frac{A-c}{4H^2},\qquad
W_0=\frac{U+J/e}{4H^2}.}
\tag{22}
\]

例如前段 η₀=κ/(2H)、d₀=−κ/2，给 `S₂=-eI/(4H²)`、`S₄=eI₄/(8H²)`、`W₀=J/(4eH²)`；后段 η₀=−1/(2H)、d₀=1−h/(2H)，给出余项。由于 η₀κ≥0 且前段内部 d₀²>0，S₄>0，故 A−c>0。又 0<ψ<1 于内部，Cauchy–Schwarz 给

\[
0<c\le\frac e2I(1-I)\le\frac1{32}.
\tag{23}
\]

代入 (8)，得到具体的新长度与幅值：

\[
\boxed{L_*^2=\frac{U(K_0-A+c)+K_0J/e}{(1+K_0)A-c},
\qquad \alpha_*^2=\frac{1+U/L_*^2}{K_0}.}
\tag{24}
\]

以下证明其分母、L 盒与所有原场盒，不以未求的数值代替。

## 6. T 的显式有理夹界

S(1−t)=1−S(t)，故

\[
T=\int_0^{1/2}G_R(S(t))\,dt,\qquad
G_R(s)=\frac1{1+(R-1)s}+\frac1{R-(R-1)s}
=\frac{R+1}{R+(R-1)^2s(1-s)}.
\tag{25}
\]

R 满足 33/10<R<10/3，且 G_R(s) 对 R 严格递减。对 0≤t≤1/4，单调性给
`0≤S(t)≤S(1/4)=53/512<1/9`，于是

\[
G_R(S(t))>\frac{39}{30+49(8/81)}=\frac{3159}{2822}.
\]

对 1/4≤t≤1/2，s(1−s)≤1/4，故

\[
G_R(S(t))\ge\frac4{R+1}>\frac{12}{13}.
\]

合起来

\[
\boxed{T>\frac14\left(\frac{3159}{2822}+\frac{12}{13}\right)
=\frac{74931}{146744}>\frac{51}{100}.}
\tag{26}
\]

另一方面，(25) 的分母在内部严格大于 R，故

\[
T<\frac{R+1}{2R}.
\tag{27}
\]

使用 `47/100<I<1/2`、(26)(27) 与 R>33/10，得到

\[
\boxed{\frac{53}{400}<A<eI+\frac\ell R
<\frac18+\frac5{22}=\frac{31}{88}.}
\tag{28}
\]

又 R636 已给 `0<U<280/27`，且

\[
\frac67<K_0<\frac78,\qquad J/e=172/35.
\tag{29}
\]

于是 `0<A−c<31/88<K₀`，从 (22) 立即得到

\[
D=-\frac{U(K_0-A+c)+K_0J/e}{4H^2}<0,
\quad
N=-\frac{(1+K_0)A-c}{4H^2}<0.
\tag{30}
\]

这个具体背景确实进入 (8) 的非退化正分支。

## 7. 新长度严格在原盒内

写

\[
Q=(1+K_0)A-c,\qquad V=U(K_0-A+c)+K_0J/e,
\quad L_*^2=V/Q.
\]

由 (23)(28)(29)，

\[
Q>\frac{13}{7}\frac{53}{400}-\frac1{32}
=\frac{1203}{5600},\qquad
Q<\frac{15}{8}\frac{31}{88}=\frac{465}{704},
\tag{31}
\]
\[
V>\frac67\frac{172}{35}=\frac{1032}{245},\qquad
V<K_0(U+J/e)<\frac78\left(\frac{280}{27}+\frac{172}{35}\right)
=\frac{25277}{1890}.
\tag{32}
\]

所以

\[
L_*^2>\frac{726528}{113925}>\frac{25}{4},\qquad
L_*^2<\frac{141551200}{2273670}<\frac{6241}{100}.
\tag{33}
\]

这些最后的比较均为正整数交叉乘法。因此

\[
\boxed{\frac52<L_*<\frac{79}{10},}
\tag{34}
\]

严格位于原 `[2.1,7.9]` 内。

## 8. 新幅值与其余连续物理盒

还需控制 `U/L_*²=UQ/V`，不能独立取 U 上界和 L 下界造成过松估计。由

\[
K_0-A+c>\frac67-\frac{31}{88}=\frac{311}{616},
\]

有 `V>(311/616)U+1032/245`。另一方面 Q<465/704，而

\[
U\left(\frac{465}{704}-\frac{311}{616}\right)
<\frac{280}{27}\frac{767}{4928}
=\frac{3835}{2376}<\frac{1032}{245}.
\]

因此 UQ<V，准确得到

\[
\boxed{0<\frac{U}{L_*^2}<1,\qquad
\alpha_*^2<\frac2{6/7}=\frac73<\frac{64}{25},\qquad
0<\alpha_*<\frac85.}
\tag{35}
\]

高度完全未改，仍有 `.8<H≤h≤HR<17/6<3`。R636 的真实 η₀ 公式给

\[
\boxed{|k|\le\alpha_*<\frac85<2,\qquad
|\eta|\le\frac{\alpha_*}{2H}<\frac{16}{17}<1.}
\tag{36}
\]

又 `max S'=15/8`、`R−1<7/3`，故 `|h_x|<119/24`；由 L*>5/2，

\[
\boxed{|\gamma|<\frac{119}{60}<6.}
\tag{37}
\]

R636 已证明 `0≤ψ'<9/4`，前段 `|κ_x|<9`，后段为 0；所以

\[
\boxed{|\upsilon|<\frac{9(8/5)}{5/2}=\frac{144}{25}<6.}
\tag{38}
\]

这些是整段解析严格界。中心 a₀=0、v=−4α*/L*≠0，因而

\[
\boxed{B_2=a_0-Hv^2/4=-4H\alpha_*^2/L_*^2<0.}
\tag{39}
\]

[R620](R620-fixed-width-center-jet-gauge-chart.md) 的原非零支允许负 B₂；仍不借旧 `B₂>.05` 搜索支的资格。新尺度下的全部物理条件由 (34)–(39) 独立支付。

## 9. 可实际消费的输入与后继真实方程

保留 R636 的显式背景 h/κ，按 (21)(24) 的真实积分定义 L*、α*，就得到原盒内、C²、P/t₁/s₀ 三个偶端准确为零的新输入。其函数空间仍按 R636 的“显式背景加原方向”表示，不能把背景喂给旧二阶 spline 规则后冒称零插值误差。

在该背景附近，R638 的 P₀,b_h=−15/68 非零，(30) 的 D<0，(34)–(39) 全有严格裕量。积分与 C² 形状连续依赖，因此存在保持这些性质的局部三端图；其完整方向由 (13)–(20) 和 R638 的 \(\dot b_h\) 组成。这个图的存在不证明余下 r₁ 与完整 ruling 有共同根，它提供更接近真实端约束、可继续实际求解的输入和空间。

实施中必须真实计算 S₂/S₄/W₀/U/K₀ 与全部历史；若固定求积代替连续积分，先得到的只是该离散图的一致零。fixed-fine 必须冻结已选 b_h、α、L、完整曲线、八中心 A 与三 gauge，直接重读全部原偶端；不能在 fine 重新解 (8) 或 P 后把另一条物理曲线称作同曲线检验。

原十八块母、正势系数 1、全部 r₁ 速度交叉项、两 ruling、全原绝对门和主课题宏观完成条件均继续保留。本结果不重做旧有限 17 模族，也不修改已经运行的 R632/R636 范围。
