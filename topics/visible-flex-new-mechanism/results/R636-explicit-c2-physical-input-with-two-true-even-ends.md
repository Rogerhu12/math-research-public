# R636：显式 C² 原盒输入，准确支付 P 与动能两个真实偶端

2026-11-28；会话 `Astra-new-mechanism-8cdb3418-20261128`。
**已证明：下面的分段五次曲线及唯一正动能幅值，在原物理盒内部，并准确满足
真 A_p1(L)=A_t1(L)=0。** 四奇 A 按原真实尾锚、末双速度按函数端 germ
自动为零；其余 A_r1、A_s0、两条完整 ruling 及主课题完成条件仍未支付。
本稿为纸面构造，不含新的科学数值。

## 1. 两个实际多项式阶段

令

$$
H=\frac{17}{20},\qquad e=\frac14,\qquad \ell=\frac34,\qquad L=4,
$$
$$
\psi(t)=t+4t^3-7t^4+3t^5,\qquad
S(t)=10t^3-15t^4+6t^5.\tag{1}
$$

它们的端数据为

$$
\psi(0)=0,\ \psi'(0)=1,\ \psi''(0)=0,\quad
\psi(1)=1,\ \psi'(1)=\psi''(1)=0,
$$
$$
S(0)=S'(0)=S''(0)=0,\quad S(1)=1,\ S'(1)=S''(1)=0.
$$

此外

$$
\psi'(t)=(1-t)^2(15t^2+2t+1)\ge0,\qquad
S'(t)=30t^2(1-t)^2\ge0.\tag{2}
$$

记一个完全有理的量

$$
I=\int_0^1\psi(t)^2\,dt
=\frac13+\frac85-\frac{14}6+\frac{22}7-\frac{56}8
 +\frac{73}9-\frac{42}{10}+\frac9{11}
=\frac{1636}{3465},\tag{3}
$$
$$
R=3+\frac{2eI}{\ell}=\frac{34457}{10395},\qquad
B=HR=\frac{585769}{207900}.\tag{4}
$$

先定义**基础**实际形状

$$
\boxed{
(h(x),\kappa(x))=
\begin{cases}
\left(H,-\psi(x/e)\right),&0\le x\le e,\\
\left(H+(B-H)S((x-e)/\ell),-1\right),&e\le x\le1.
\end{cases}}
\tag{5}
$$

上面的共同值、一阶和二阶端数据证明 (5) 是真正 C² 曲线。
中心有 h_x=0、κ=0、κ_x=−4、κ_xx=0；末端有 h_x=κ_x=0。
因而其原中心反射 germ 与末双速度条件在 C² 意义下均实际成立。

## 2. P 严格为零，不借 stored 历史

按 R612 的真运动学定义

$$\eta_\kappa(x)=\int_0^x\frac{\kappa_y}{2h}\,dy,\qquad d_\kappa=h\eta_\kappa-\kappa.$$

第一阶段 h=H，故 etaκ=κ/(2H)、dκ=−κ/2。
第二阶段 κ=−1，故 etaκ=−1/(2H)、dκ=1−h/(2H)。所以

$$
\begin{aligned}
P(h,\kappa)
&=-\int_0^1\kappa d_\kappa\\
&=\frac{eI}{2}+\ell-\frac1{2H}\int_e^1h(x)\,dx\\
&=\frac{eI}{2}+\ell-\frac{\ell(H+B)}{4H}=0.
\end{aligned}\tag{6}
$$

最后一步使用 `∫₀¹S=1/2` 以及 (4)。这是精确有理积分身份，并非采样小残差。

现在令

$$
K_\kappa=\int\kappa^2=\ell+eI=\frac{12031}{13860},\qquad
U=\int(h_x/h)^2>0,
$$
$$
\boxed{\alpha=\sqrt{\frac{1+U/16}{K_\kappa}},\quad
k=\alpha\kappa,\quad\eta=\alpha\eta_\kappa.}\tag{7}
$$

[R632](R632-true-kinetic-amplitude-chart-with-negative-center-branch.md) 给真实动能
身份 `K−1−U/L²=0`。又因 P(h,ακ)=α²P(h,κ)，(6) 继续精确为零。
由 [R612](R612-exact-physical-length-elimination-and-three-true-end-integrals.md)
的同一原槽公式，遂得

$$
\boxed{A_{p_1}(L)=0,\qquad
8A_{t_1}(L)+2A_{p_1}(L)=0,\qquad A_{t_1}(L)=0.}\tag{8}
$$

U 不必在纸面化为初等闭式：它是 (5) 指定的正连续积分，(7) 唯一定义实际
常幅值。数值实现时必须准确消费这个积分，并在 fixed-fine 时冻结 α，不能
每层重新选幅值后把不同物理曲线称为同一条。

## 3. 全部原物理盒的解析内部界

由 (2)，h 从 H 到 B 单调，κ 从 0 到−1单调后保持。
直接比较有理数得 `R<10/3`，故

$$\frac45<H=\frac{17}{20}\le h\le B<\frac{17}{6}<3.\tag{9}$$

只有后段贡献 U。因为 h≥H，且
`∫₀¹(S')²=10/7`，

$$
0<U\le\frac{(R-1)^2}{\ell}\int_0^1(S')^2
<\frac{(7/3)^2}{3/4}\frac{10}{7}=\frac{280}{27}.\tag{10}
$$

又 `Kκ>6/7`，所以

$$
1<\alpha^2K_\kappa=1+U/16,
\qquad
\alpha^2<\frac{1+35/54}{6/7}=\frac{623}{324}<\frac{49}{25},
\qquad 0<\alpha<\frac75.\tag{11}
$$

于是全程

$$\boxed{|k|<\frac75<2,\qquad
|\eta|\le\frac{\alpha}{2H}<\frac{14}{17}<1.}\tag{12}$$

`max S'=15/8`，故物理 γ=h_x/L 满足

$$
|\gamma|\le\frac{B-H}{\ell L}\frac{15}{8}
<\frac{119}{96}<6.\tag{13}
$$

利用 `t(1−t)²≤4/27`、`t²(1−t)²≤1/16`，

$$
0\le\psi'(t)\le1+\frac8{27}+\frac{15}{16}
=\frac{965}{432}<\frac94.
$$

因 eL=1，物理 υ=k_x/L 在前段为−αψ'(x/e)，后段为零，因此

$$\boxed{|\upsilon|<\frac75\frac94=\frac{63}{20}<6.}\tag{14}$$

L=4 严格处于原 `[2.1,7.9]` 内。所有界针对整段连续曲线，而非 coarse/fine
采样。缩放后的物理盒已由这些解析不等式支付；数值实现仍须报告其实际场，
不得把理论常数界用作省略完整原场的借口。

## 4. 负 B₂ 是原方程允许的中心支，未借旧 chart 资格

此输入 a₀=h_ss(0)=0、v=k_s(0)=−α，因此

$$\boxed{B_2=a_0-Hv^2/4=-H\alpha^2/4<0.}\tag{15}$$

[R620](R620-fixed-width-center-jet-gauge-chart.md) 的定理要求的是
`v≠0,B₂≠0`，没有要求 B₂>0；其完整三角 Jacobian 的第三对角
`C_hc/B₂` 在负 B₂ 支仍非零。原两 ruling 只含全程 β(s) 的乘积配对，
也没有 β 或 B₂ 的正性不等式。原 feedback 的质量行列式由
`−C_h^+C_k^−−C_h^−C_k^+` 决定，不以 B₂ 作分母。
R598 的完整原母合法域及其 `C_h<0,C_k>0` 保持；实际原系数仍须计算。

旧 `FullFeedbackCollocation.chart` 所加的 `v<−.05,B₂>.05` 是那一次选取的
单个数值搜索支，不是 R620 的全部定理或原物理盒。本构造不声称满足旧正支，
也不借其已付 chart/fine 资格。R632 的实际曲线消元和全程常规范投影不通过
这个分母生成 h/k；(15) 可直接作为新的真实输入。

这仍只是合法输入：中心更高阶 ruling 兼容、两常规范在全程的共同性及完整
ODE 尚未由 (15) 支付。不能把“负支允许”解释成原反馈已经沿 (5) 成立。

## 5. 准确进入新的实际函数空间，不能冒零插值误差

分界 e=1/4 与现有 65 个等距节点对齐；两段均为五次或常数，故一般的 C²
quintic Hermite 表示可准确表示 (5)，前提是使用它们**真实的节点二阶导数**。

但是原 R632 的 257 维空间，把非中心二阶导数固定为“节点一阶导数的 cubic
spline 的节点导数”。五次背景的一阶导数一般是四次；cubic spline 不必重现
这一个四次多项式。因此，单把 (5) 的值及一阶导数喂给该旧二阶规则，并不能
据“分界对齐”就声称完整实际曲线准确不变。

具体可靠入口是保留 (5) 为**显式固定多项式背景**，再加原 257 个 Hermite
形状方向：h/κ 的值、一阶导数及中心二阶扰动沿原规则生成，背景自身不被
重插值。所有扰动为零且 L=4 时严格得到 (5)(7)；每个扰动仍是 C²，故总曲线
保持 C²。固定 κ 的中心扰动导数为零，保总 κ_x(0)=−4。
这是一份新的仿射实际函数空间，不冒称旧 257 维零背景空间已经包含 (5)。

同一原真 η/A/rho、全正势、完整常规范投影、原绝对门继续作用于该总曲线。
新输入只支付 (8) 和连续物理盒；余两个真偶端与完整 ruling 将在这个实际
函数空间中继续求解，不重做旧 17 模族，也不修改已经触发的 R632 首范围。
