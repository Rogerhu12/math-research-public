# R482：完整第三历史的逐点消去与单份实际原型的两输入 ruling 系统

日期：2026-11-16。**完整纸面推导；没有执行符号程序、原根恢复、profile 求积、秩计算、人工检查或新的数值研究。**

本稿使用 [R476](R476-full-third-diagonal-kernel-is-invisible-to-disjoint-rank-one-circles.md)、[R480](R480-finite-full-third-outer-moments-and-zero-matrix-prototype-ruling.md) 从起点选择的同一个增强 profile 库。它不再把第三原型的“重复无漂移”当成内部 ruling 已经为零，而给出单份原型内部的一个更强、准确的缩减：

> 在同一个全局 $w_\theta,\chi_\theta$ 下，原完整第四 ruling 中的全部第三累计历史，可以换成**当前几何的一阶 jet 端点势、真实八维第二累计与其平方**。换过以后，内部方程对 $h_{ss},k_{ss}$ 是仿射的；这两个加速度的完整系数可以直接由原第二局部恢复写出。

这给一个有十三维真实状态、两个真实控制输入的局部约束路径问题。十三是状态数，既不是原十三规范行的秩，也不是新的可控性声明。本文给其精确方程和一个可实际延拓路径的正则反馈引理；没有证明原 R70/R80 的任意桥能在该约束集合中走通。

另有一个具体必要门：若实际实现含一个正长度的常 scalar 状态区间，那么一个准确的、与 $w_\theta,\chi_\theta$ 无关的二次系数必须为零。R480 的全第三 outer 矩并不自动消去这个第二历史平方。

所有原二、三阶入值、非恒端的加速度势、第四成本 $V$、右锚与两个 collars 均保留。本文没有建立全闭词的第四 range，更没有推出主课题的完整几何结论。

## 1. 固定的是同一个圆、路径起点和最终规范

固定 R480 的严格不交 rank-one 圆
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta,
\tag{1}
$$
并保原三矩
$$
\mathbf I(D_\theta)=0.
\tag{2}
$$
所有 profiles、原函数与物理 $x$ 区间 $I=[\ell,r]$ 共用原右锚。$D_\theta$ 是原对称二次输入槽；下面写 $D_{11},D_{22}$ 时，只表示在这个槽上施加所列双线性微分式，不先把它当普通乘积再微分。

R480 已给
$$
\boxed{
I_j\{\phi_\theta,\tau(\phi_\theta;D_\theta)\}=0
\quad(\tau\in W,\ j=0,1,2,\ \theta\in\mathbb R).
}
\tag{3}
$$
$W=W_{71}+V_3+W_1$ 是 R80 的完整三槽第三可达空间，不只是对角核。式(3)在**所选同一个库**中使用；若另换母形或不保初选纤维，不能继续引用它。

实际几何为
$$
S=(h,k,\omega),\quad h>0,\qquad
\omega_s=\frac{k_s}{2h},\qquad
F_s=F\Omega(k),\qquad \alpha_s=h^2T.
\tag{4}
$$
记
$$
z=x+\omega,\quad e=hz-k,\quad Q=1+e^2,\quad
\gamma=h_s,\quad \upsilon=k_s,\quad
e_s=\gamma z-\upsilon/2.
\tag{5}
$$
共同物理支要求 $z>0$，不在内部子桥另换 $x$。

沿最终词同一个起点累计
$$
\mathsf m_s=M_{\rm raw}(S,\gamma,\upsilon),\qquad
A_s=\Phi_{\mathsf m(s)}.
\tag{6}
$$
$M_{\rm raw}$ 是 R73 的原八矩密度；尤其它依赖真实速度，不能用一条任意拟定的八维曲线代替(6)。

原第二、第三规范记为同一组 $w_\theta,\chi_\theta$。它们在两个 collars 为零，随相位光滑、周期且保原种子。它们已经承担哪些完整 period、十三行和保护芽，均沿 R467/R469/R472 的原合同；本文不给每个原型另选一组规范。

对真紧 $a$，以及任何本稿原恢复所产生的光滑 $b$，原 physical 配对为
$$
\mathcal E_s(a,b)=\mathbf w(s)\cdot\mathbf I(a,b),\qquad
\mathbf w(s)=\left(\frac{1+(h\omega-k)^2}{4h},
\frac{h\omega-k}{2},\frac h4\right).
\tag{7}
$$
有真实左尾的 $b$ 不因此被设成紧函数。端项由紧的 outer 槽消失，正是 R221 的适用范围。

## 2. 非恒内部端点的完整第三类

### 2.1 原商势在每一个内部点成立

在固定有限维真实第三 ambient 空间中取商映射
$$
\pi_W:E_3^{\rm ext}\longrightarrow E_3^{\rm ext}/W.
$$
$E_3^{\rm ext}$ 保含原 $E_8\circ E_8$；不把形式列当独立基。

R73 的原式为
$$
T_s=-\int_{s_0}^{s}A_t'\circ A_t\,dt
+\int_{s_0}^{s}C_t\,dt
\tag{8}
$$
（若起点有非零真实入值，下面另保该常量）。R77/R79 给逐点分解
$$
C_s=D_s(P_{\rm acc}+P_h)
+C_{3,\rm rem}+k_sR(h,k,\omega).
\tag{9}
$$
其中：

- $P_{\rm acc}$ 是几何速度的二次式；**内部点一般非零**；
- $C_{3,\rm rem}(s)$ 逐点落在 $V_3\subset W$，不仅其闭路积分落在那里；
- 模 $W_1$，原 $R\,dk$ 有固定势 $\bar F(k,\omega)$，沿真实水平关系满足
  $\pi_W(k_sR)=D_s\bar F(k,\omega)$。

最后一条是 R79 的实际有限维商势身份，不要求当前前缀闭合，也不要求当前点是常数端芽。

又由原复合的乘积法则，
$$
-\int A'\circ A+\frac12A_s^2
=\frac12\int(A\circ A'-A'\circ A)+\frac12A_{s_0}^2.
\tag{10}
$$
积分中的交换子逐点属于 $W_{71}$。所以定义
$$
\bar\Pi(j^1S)=
\pi_W(P_{\rm acc}+P_h)+\bar F(k,\omega),
\tag{11}
$$
得到对每一个真实 $s$ 的准确身份
$$
\boxed{
\pi_W\!\left(T_s+\frac12A_s^2\right)
=\pi_W(\Theta_0)+
\bar\Pi(j^1S_s)-\bar\Pi(j^1S_{s_0}).
}
\tag{12}
$$
这里 $\Theta_0=T_{s_0}+A_{s_0}^2/2$ 是真实起点值。全词原零历史规范下它为零；若在中间切一段来记账，必须继承它，不能又归零。

### 2.2 固定 lift 与其不依赖性

一次选定商空间的线性截面，将(11)提升成实际算子 $\Pi(j^1S)$。写
$$
P_s^{\rm end}
=\Theta_0+\Pi(j^1S_s)-\Pi(j^1S_{s_0}).
\tag{13}
$$
于是
$$
\boxed{
T_s=P_s^{\rm end}-\frac12A_s^2+\tau_s,\qquad
\tau_s\in W.
}
\tag{14}
$$
所有状态用同一截面。改变截面只改变一个 $W$ 值，因此由(3)不改变本稿的 ruling 公式。

(14)不是“内部第三为零”。$\tau_s$ 一般非零，原完整第三端目标和全部第四成本仍会读到它。这里能够删掉的，只是第四 ruling 中确实以
$\mathcal E_s\{\phi_\theta,\tau_s(\phi_\theta;D_\theta)\}$ 形式出现的这一项。

尤其，常态端点的 R80 $T_{\rm end}$ 不能直接替代(13)。那样会漏掉内部 $P_{\rm acc}$，也可能漏掉初端势。本文的所有后继公式保留两者。

## 3. 不再恢复第三历史的完整点态 ruling 公式

以下省略 $\theta$，但每个式子同时对全相位成立。记
$$
q_s=A_sD+w.
\tag{15}
$$
由(2)、原 E8 的三矩左尾表和 $w$ 的 collars，$q_s$ 真紧。

### 3.1 第二局部场及原三线性配对

令 $K_s(D)$ 是 R73 的第二局部恢复：
$$
K_s(D)=\frac FzV_K,\qquad
V_K=\left(\frac{\eta_D}{h},\,zP_D+B_D,\,
\frac{e\eta_D}{h}\right).
\tag{16}
$$
原真第二场为
$$
Z_2=K_s(D)-Y_{q_s}.
\tag{17}
$$
$P_D,B_D,\eta_D$ 均取 R56/R221 的原式；没有把 local normal 或速度项置零。

定义
$$
\mathcal T_s(c;a,b)
=\int(Y_c)_u\cdot(K_s(a,b))_u\,du,
$$
$$
\mathcal L_s(q)=
2\mathcal T_s(q;D)
-4\mathcal T_s(\phi;\phi,q).
\tag{18}
$$
R221(17)是(18)的完整局部表达，包含转置右尾产生的 $F_c$ 项。它对 $q$ 线性，在几何上关于 $\gamma,\upsilon$ 线性。

### 3.2 必须保留的变化-profile chain

由(6)，
$$
(q_s)_s=\Phi_{M_{\rm raw}}D=:v.
\tag{19}
$$
这里 $w$ 不依赖 $s$。把 $q_s$ 当静态 profile 代入第三 forcing 会漏掉(19)。

令
$$
F_\phi=Q\phi''-2he\phi'+2h^2\phi,\qquad
F_\phi'=Q\phi'''.
\tag{20}
$$
从 R56 原分子式，对 $2H(Y_\phi,Y_{q_s})$ 的额外变化-profile 部分，准确得到
$$
P_{\rm ch}=B_{\rm ch}=0,\qquad
\boxed{
\eta_{\rm ch}=\frac1{8h}
J\{\phi'''(Qv'-2he\,v)\}.
}
\tag{21}
$$
式(21)的 $P_s$ 不能由于当前 $P_{\rm ch}=0$ 而删掉。直接核法是：在当前点 $q=0$、$q_s=v$ 的那一份 jet 差上，
$$
\eta_{\rm ch}
=-\frac1{2h}\{V_\phi'\!\cdot V_v+
J(V_\phi'\!\cdot V_v')\}
=\frac1{2h}J(V_\phi''\!\cdot V_v),
$$
而
$V_\phi''\cdot V_v=\phi'''(Qv'-2he\,v)/4$。
这只是对真实表达取其 chain 差，不引入一条 $A_s\equiv0$ 的假实际路径。

### 3.3 纯当前几何项的明确取法

对完整 forcing
$$
H_-=-2H(Y_\phi,K_s(D))
$$
按 R56(2)(6)取其局部 $\eta_-$。计算时对整个 $K_s(D)$ 真正求 $s$ 导数；它依赖当前 $S,j^2S$，不含累计第三历史。定义
$$
\boxed{
\begin{aligned}
\mathcal R_s={}&
-\frac1h\int|\partial_xV_K|^2
-\frac1{h^2}\int Q\phi'''\eta_-\\
&-\frac1{8h^3}\int
F_\phi\phi'''(Qv'-2he\,v).
\end{aligned}}
\tag{22}
$$
最后一项正是(21)的真实 physical 配对。它依赖原 $M_{\rm raw}$，所以即使形式上抽取第二累计的常数项，也没有把第二密度归零。

原第二局部场在两 collar 为零：$D$ 的三矩零同时支付 $P_D$ 和 $\eta_D$ 的左常数。因此(22)第一项可用原分子能量，不漏非紧边项。

### 3.4 完整公式与一般规范

真实第三 scalar history 的原传递为
$$
b_s=-2T_s(\phi;D)+2A_s(\phi,w)-\chi.
\tag{23}
$$
由 R56、(17)–(22)直接展开完整第四 forcing，先得到
$$
\mathscr K_s=
\mathcal R_s+\mathcal L_s(q_s)
-\mathcal E_s(q_s,q_s)+2\mathcal E_s(\phi,b_s).
\tag{24}
$$
再用(3)(14)，得到本稿的主公式
$$
\boxed{
\begin{aligned}
\mathscr K_s={}&
\mathcal R_s+\mathcal L_s(A_sD+w)
-\mathcal E_s(A_sD+w,A_sD+w)\\
&-4\mathcal E_s\{\phi,P_s^{\rm end}(\phi;D)\}\\
&+2\mathcal E_s\{\phi,A_s(\phi,A_sD)\}
+4\mathcal E_s\{\phi,A_s(\phi,w)\}
-2\mathcal E_s(\phi,\chi).
\end{aligned}}
\tag{25}
$$

(25)完整保留第二累计、平方、一般 $w$、第三 Gram、初端势和内部速度势。它没有再积分第三 history，也没有改第四 forcing。

作为号的独立检验，用(25)减去 $w=\chi=0$ 的式子，准确得到
$$
\mathcal L_s(w)
-2\mathcal E_s(A_sD,w)
+4\mathcal E_s\{\phi,A_s(\phi,w)\}
-\mathcal E_s(w,w)-2\mathcal E_s(\phi,\chi),
\tag{26}
$$
这正是 R221(12) 与 R184(11)，不是另造一个规范作用。

对一个单份 $A_B=0$ prototype，可以按该块原零输入定义取 $A_{s_0}=T_{s_0}=w=\chi=0$，得到其 canonical $K_0$；在最终词中实际使用时，则必须使用它的真实全局(13)(15)(23)。两种计算不能互相冒充。

## 4. 加速度恰只有两个输入，完整系数可直接写出

### 4.1 原第二局部 $\eta_D$

记
$$
D_{11}=f'^2-\phi'^2,\quad
D_{22}=f''^2-\phi''^2,\quad
D_{12}=2(f'f''-\phi'\phi'').
$$
R221 的原式是
$$
\eta_D=\frac1{16h^2}\left[
Q(\gamma D_{12}-e_sD_{22})-2h\gamma eD_{11}
+J\{(\gamma Q-2he e_s)D_{22}-2h^2\gamma D_{11}\}
\right].
\tag{27}
$$
因此
$$
\eta_D=\gamma a_h[D]+\upsilon a_k[D],
\tag{28}
$$
其中
$$
\boxed{
a_h[D]=\frac1{16h^2}\left[
Q(D_{12}-zD_{22})-2heD_{11}
+J\{(Q-2he z)D_{22}-2h^2D_{11}\}
\right],
}
\tag{29}
$$
$$
\boxed{
a_k[D]=\frac1{32h^2}
\left[QD_{22}+2hJ(eD_{22})\right].
}
\tag{30}
$$
此处 $(h,k,\omega)$ 固定，偏导只对真实速度 $(h_s,k_s)$ 取；$k_s$ 与 $\omega_s$ 不是两个自由输入。

### 4.2 原单位的加速度系数

$h_{ss},k_{ss}$ 只通过 $H_-$ 中的 $\partial_s\eta_D$ 进入(25)。$M_{\rm raw}$ 至多二次依赖速度，(19)不含加速度；$P_{\rm acc}$ 是速度二次式；(18)只线性依赖速度。故没有隐藏的第三或更高 $s$ 导数。

若 $\partial_s\eta_D$ 的某一加速度分量为 $a$，相应分子为
$$
V_a=(a/h,0,ea/h).
$$
R56 原恢复给
$$
\eta_{-,{\rm acc}}
=\frac1{2h}\{V_\phi'\cdot V_a+
J(V_\phi'\cdot V_a')\}
=\frac1{4h^2}J(Q\phi'''a).
\tag{31}
$$
再用(20)及双 collar，
$$
-2\mathfrak b(Y_\phi,K_{-,{\rm acc}})
=-\frac1{4h^4}\int F_\phi Q\phi'''a.
$$
因此完整 ruling 准确为
$$
\boxed{
\mathscr K_s(\theta)=
\mathcal F(X_s;\theta)
+\mathcal C_h(X_s;\theta)h_{ss}
+\mathcal C_k(X_s;\theta)k_{ss},
}
\tag{32}
$$
其中
$$
\boxed{
\mathcal C_h=-\frac1{4h^4}\int F_\phi Q\phi'''a_h[D],
\qquad
\mathcal C_k=-\frac1{4h^4}\int F_\phi Q\phi'''a_k[D].
}
\tag{33}
$$
$\mathcal F$ 是(25)在按(6)代入后抽出的无加速度项；(22)(25)(27)–(30)完整定义了它，不需要重做第三累计积分。

$\mathcal C_h,\mathcal C_k$ 不含累计 $A_s$，也不含 $w_\theta,\chi_\theta$。这并不意味着它们非零、独立或可任意指定；是否独立必须在同一实际库上判定。

## 5. 真实路径问题的精确降维与一个正向局部延拓引理

定义真实状态
$$
X=(h,k,\omega,\mathsf m,\gamma,\upsilon)
\in\mathbb R^{3+8+2}.
$$
它的动力学固定为
$$
\boxed{
\begin{aligned}
h_s&=\gamma,&k_s&=\upsilon,&
\omega_s&=\upsilon/(2h),\\
\mathsf m_s&=M_{\rm raw}(h,k,\omega,\gamma,\upsilon),&
\gamma_s&=u_h,&\upsilon_s&=u_k.
\end{aligned}}
\tag{34}
$$
实际 frame 与位置继续按(4)积分。二者不出现在旋转不变的 ruling 配对中，但端 frame、闭位置及后续 Klein 合成仍要保。

原内部 ruling 条件现在就是
$$
\mathcal C_h(X;\theta)u_h+
\mathcal C_k(X;\theta)u_k=-\mathcal F(X;\theta)
\quad\text{对全部 }\theta.
\tag{35}
$$
这是同一个 $(u_h,u_k)$ 作用于全部相位，不是逐相位选几何。

对固定 $w_\theta,\chi_\theta$，(25)只使用有限个 profile 矩和它们的有限乘积；原端点势也在固定有限第三空间中。因此三项作为相位函数落在一个固定有限维真实函数空间。选择其实际函数基后，(35)是有限实线性系统
$$
C(X)u=-f(X).
\tag{36}
$$
不预设基的维数或矩阵秩；若保冗余呈示，就必须同时保真实函数关系。有限相位采样只有在该真实空间上已证明单射时才能代替全函数式。

**局部正则反馈引理。** 设一个状态开集 $U$ 上，$C$ 的秩固定，且 $-f(X)$ 对每个 $X\in U$ 都属于 $\operatorname{im}C(X)$。取一个固定非零 minor 所给的光滑右逆与核坐标，则可取光滑控制
$$
u(X)=-C(X)^+f(X)+N(X)\zeta(X).
\tag{37}
$$
这里 $+$ 只指该固定秩有限映射的一种光滑广义逆，不要求新增求解程序。将(37)代入(34)，普通 ODE 局部存在唯一性给一条**真实水平几何路径**，并在其存在区间上逐点满足完整 ruling(35)。从 $h>0,z>0$ 的内点出发，取足够短但固定的区间保持这两个开条件；frame/位置用原 ODE 恢复。

若相容只在一个状态子流形 $\Sigma$ 上成立，则还必须要求(34)(37)的向量场与 $\Sigma$ 相切；不能把代数点态有解当成存在穿过该点的完整允许路径。固定秩下降点也必须另付真实光滑延拓，不能任选不连续的逐点逆。

这个引理给一个能真实产生路径的接口：先证明同一库中的有限函数身份和一个正则状态域，再沿反馈走；它不是把形式 scalar 序列拼成几何。**本文尚未证明所需状态域包含能返回 scalar/frame、使整 $A_B=0$ 并达到指定第三量的闭控制路径。**

特别，R70 的无 ruling 限制矩阵桥不自动满足(35)。把其末矩阵归零以后，内部仍须落在(35)；R80 的第三 prototypes 也不能仅凭末 $T_B\in W$ 跳过此式。

## 6. 常 scalar 区间留下一个不能用第三 history 或规范支付的二次门

本节给一个具体、可从实际原型直接检查的必要条件，不以(35)笼统代替它。

假设某个真实开区间上 $S=(h,k,\omega)$ 常数，令
$$
M_c=M_{\rm raw}(S,0,0),\qquad A_c=\Phi_{M_c}.
$$
按局部实长度 $t$，
$$
A(t)=A_*+tA_c.
\tag{38}
$$
(18)在此为零；端点势为常数；(22)的当前项为常数。因此(25)是 $t$ 的至多二次多项式。其二次系数是
$$
\boxed{
\mathcal Q_{A_c,\theta}
=-\mathcal E_S(A_cD_\theta,A_cD_\theta)
+2\mathcal E_S\{\phi_\theta,A_c(\phi_\theta,A_cD_\theta)\}.
}
\tag{39}
$$
这个系数不含真实 $A_*$、$w_\theta$、$\chi_\theta$ 或第三入值。

若该常态区间的整个 ruling 为零，就必须有
$$
\boxed{\mathcal Q_{A_c,\theta}=0\quad\text{对全部 }\theta.}
\tag{40}
$$
没有正长度常态区间时，不额外施加(40)。尤其把旧常 collar 改成真正非平的有理芽以后，不能仍取一个已经不存在的常段系数来排除它。

为核清一阶项，置 $q_*=A_*D+w$。R480 消掉
$\mathcal E_S\{\phi,[A_*,A_c](\phi;D)\}$，故一阶系数准确为
$$
\boxed{
-2\mathcal E_S(q_*,A_cD)
+4\mathcal E_S\{\phi,A_c(\phi,q_*)\}.
}
\tag{41}
$$
常数项仍由(25)在入口的真实值决定。三项都必须为零，才支付整个常段；只付(40)不足。

(39)正是 R472 的第二历史平方类型，并非 R480 所清的第三交换子 outer 矩。本文没有断言它在当前库上非零，也没有从其形式存在推出 actual 不可能；它把一个原第三原型实现中可能被重复无漂移掩盖的具体门单独列出。

## 7. 加速度行还有有限低阶结构，但不能自动当成已付新观察

这一节只说明(33)的真实数据性质，并明确它与现有初选纤维的关系。

在严格不交的一个包上写 $\phi=c_i u_i$、$D=d_i u_i^2$。右方包对(29)(30)的贡献在这个包上都是常数，因为其全部贡献来自已经积分完的原 $J$。而
$$
\int_{J_i}F_{u_i}Q u_i'''=
\int_{J_i}F_{u_i}F_{u_i}'=0.
\tag{42}
$$
所以全部跨包尾对两个加速度行准确为零，得到
$$
\mathcal C_\alpha(\theta)
=\sum_i c_i(\theta)^2d_i(\theta)\,
\mathfrak c_\alpha(u_i;S),\qquad \alpha=h,k.
\tag{43}
$$
单包 $\mathfrak c_\alpha$ 就是(33)以 $\phi=u,D=u^2$ 取值；没有先把单包的三矩冒设为零。

这些是完整 quartic $C^2$ polynomial 泛函。理由是(29)(30)只含 $u,u',u''$ 与二次 $C^2$ 密度的真实右积分，(33)中最高 $u'''$ 只线性出现。对 $r=u''$ 取从 $0$ 开始的多项式原函数，再作一次真实 IBP，原 $J$ 的导数仍是 $C^2$ 密度；两端的原函数在 $r=0$ 准确为零，未丢左常尾。

共同平移 $u_t(x)=u(x-t)$ 时，
$$
\deg_t\mathfrak c_h(u_t;S)\le7,\qquad
\deg_t\mathfrak c_k(u_t;S)\le6.
\tag{44}
$$
这是直接由 $F_uQ$ 至多四次、(29)的局部系数至多三次／尾权至多二次、(30)至多二次得出。共同右锚保持在全部支撑右方，换元不增加积分常数。

因(29)(30)(33)对几何仅含有限 Laurent–多项式系数，(43)涉及一个明确有限的低阶观察表。**R480 原表列的是完整第三 commutator self；本文没有证明这张新增表已落在那个原表的跨度，也不宣称当前已冻结母包已保它。**

若在一次新的初始库选择中明确将这些有限系数也纳入同一个 $F^\star$，则 R455/R480 的原低阶纤维机制适用：相同纤维使 self 是同一平移多项式，等背景十次矩与十二副本的奇项消去给(43)为零。该条件性后果不需新的 principal rank，但它是一个**明确的新初选要求**，不能在目前同一实际库上免费添加。

即使两加速度行被这样支付，(32)也只变成 $\mathcal F(X;\theta)=0$ 的第一阶约束；不会因此把所有内部 ruling 自动置零。实际路径仍须保持这个约束、真实八矩 ODE 和端点条件。

## 8. 如何接回同一个完整闭词

本稿的缩减同时适用于原单份 $A_B=0$ prototype、它内部 $A\ne0$ 的实现子桥，以及 R472 的复位单元。使用方法始终是同一个：

1. 从最终全词起点保真实 $A_s$，或在切段处带入真实 $\Theta_0,A_{s_0}$；不重新设历史为零。
2. 在每一个内部点用(13)(22)(25)或等价(32)评价整个 ruling。
3. 同一个全局 $w_\theta,\chi_\theta$ 同时进入所有段；若改变它们以支付某段，原十三行、period 和已付保护芽都要保持。
4. 新路径的完整 $T$、$V$ 仍按原式恢复。$\tau_s\in W$ 对此处 outer 配对盲，不对一般 $2T(w;D)-4T(\phi;\phi,w)$ 或完整第四组合盲。
5. 把新的全部 $V$ 基准纳入 R468/R467 的同一个实际成本目标；该步骤不替代新控制块内部的(25)。

对相同 scalar/frame、相同低阶入值的 $A_B=0$ 重复块，(3)使第三 $W$ 增量不再改变其内部 ruling。更强的当前结论是：在同一圆和规范下，ruling 对完整第三路径历史的依赖已经下降到(13)这个一阶 jet 端点类；它仍通过(6)保留真实第二路径历史。两个块仅有相同总 $A_B=0$ 或相同 $J(V)$，不足以使其内部状态曲线相同。

因此下一项可付任务已经具体化：在(34)(35)这一个真实受约束系统中构造所需返回路径，或从(39)等准确系数证明某个现成 prototype 不满足它。不能以末矩阵、末第三或有限成本截面代替这一全段条件；也不能把有剩余第三控制方向误写为能够逐 $s$ 独立选 $\chi$。

本稿完成的是完整第三记忆消去、原两加速度系数、真实有限状态路径合同以及常态实现的明确平方门。尚未给出满足全部端点与控制目标的受约束闭原型。它为继续正向构造提供实际 ODE 接口，同时保留一个可能首先阻断旧原型的、与规范无关的必要行。

### 原式来源与独立窄核范围

- [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)：全部适应坐标分子、$\eta_0$、局部恢复和 physical ruling；
- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：真实八矩、变化-profile chain、完整第三累计；
- [R77](R77-weight-three-local-operator-actual-finite-controllability.md)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)、[R80](R80-complete-third-affine-class-and-P1-endpoint-obstruction.md)：逐点局部余项、商势与完整 $W$；
- [R184](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、[R221](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)：一般 $w,\chi$ 与真实端项；
- [R472](R472-two-level-prefix-reset-and-unavoidable-ruling-in-actual-return-bridges.md)、[R476](R476-full-third-diagonal-kernel-is-invisible-to-disjoint-rank-one-circles.md)、[R480](R480-finite-full-third-outer-moments-and-zero-matrix-prototype-ruling.md)：同一实际词、已付 outer 身份及重复范围。

mechanism 仅独立手核(31)(33)的原号、$1/(4h^4)$ 因子和真实端 IBP；literature 仅核(14)代入 $-4\mathcal E$ 后的两项系数及必须保初端势的范围。本文其余完整推导按上述显示原式给出，未将这两次窄核扩大成新科学执行或整篇外部验证。
