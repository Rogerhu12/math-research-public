# R62：保留强位移和厚度的共同度量混合曲率短领

**状态：已证明；本轮未参与旧稿构造者全文独审通过。**

2026-11-10 UTC。root 提出 R56强核与R57局部修改的组合、参数和几何预算；tail_review_continued_2 逐项核对来源、重推组合及全部新估计并成稿。上述 root 指旧 db6f 会话参与者；本轮新会话 Astra-visible-flex-78718bd0/root 未参与旧稿构造，现已完成全文独审。

本稿给一个真实联合 C∞、同一精确光滑度量的有边环带族。它同时具有固定开握持片、有效的强握持像变化和全欧氏刚体商像变化、全时正厚度，并在新增领圈内真正含正、负 Gauss曲率开片。

它仍有两条边界，没有帽中心和完整闭合，不是 README 完成解。正宽 T 只由统一存在寿命选择，尚非算出的有效十进制数值。没有运行 PDE、主数值、矩阵或网格；有限标量检查须在正文冻结后另记实际回执。

## 1. 已审来源与新的准确结论

固定来源为：

- **R56强核及全法锥 C²扰动引理。**
  作者 [fb9c9d106be35e52fc17bc91ddaf4895c0817dc4](https://github.com/Rogerhu12/math-research/blob/fb9c9d106be35e52fc17bc91ddaf4895c0817dc4/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-root-bounded-forcing-strong-support-core-v1.md)，
  blob 32a23264bab0138aba1d67dc24d9310aeb3e6d0b，21,223 UTF-8 B，
  SHA256 2052d22f434067cc97875c100fd9183e8213a3357b06f6fa28bc88acc3af6b98。
  全文独审 [8e03f06cb5b68bcdc85a06e8ee9b941345b99bfa](https://github.com/Rogerhu12/math-research/blob/8e03f06cb5b68bcdc85a06e8ee9b941345b99bfa/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-prefix-review-bounded-forcing-core.md) 已通过；正式结果 R56-bounded-forcing-strong-support-core.md。
- **R57退化入口有限传播及实际参考修改。**
  作者 [4c436678284b17a5e14f8629ce706bab5a1425c0](https://github.com/Rogerhu12/math-research/blob/4c436678284b17a5e14f8629ce706bab5a1425c0/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-nonradial-mixed-curvature-collar-v1.md)，
  blob 7714bd76ba9e67e9b4b9d4554d706b43f18eb02b，23,797 UTF-8 B，
  SHA256 d509320eebbab4cf194729d7e128d4bda7ddf779a4f410bfdadc52b8d9c29f3a。
  新证明全文独审 [86904cea8a88bd190027da243a4cf077b9fee206](https://github.com/Rogerhu12/math-research/blob/86904cea8a88bd190027da243a4cf077b9fee206/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-root-review-nonradial-mixed-curvature-collar.md) 已通过；正式结果 R57-nonradial-mixed-curvature-collar.md。
- **R50非减 Q光滑存在。** 作者 a07c2b1357e8e0a11bc0a7d15d28b6a16352b51b，全文未参与者独审 0fbb537133c97af06cf55ca3939f002f5cfb17ad。其独审身份独立保留；本文只逐项支付这次初值和系数输入，不重新声称为该一般定理的独审。

本稿不把上述旧常数程序回执绑定到新正文。

**命题。** 存在一次固定的 T>0、共同材料环带

$$
M=[-1/100,T]\times\mathbb R/(2\pi\mathbb Z),
$$

以及同一光滑度量 g上的联合 C∞ 精确等距嵌入族 F_t，t∈[0,1]。令 D=diam F_0(M)，则

$$
D<1011/500<51/25,\qquad
\operatorname{diam}F_0(H)/D>197/680>1/4,
\tag{1}
$$

$$
\delta_{\rm hold}/D>53/204>1/4,\qquad
\delta_{\rm E}/D>7/136>1/20,
\tag{2}
$$

$$
\operatorname{reach}F_t(M)\ge3/32,\qquad
\operatorname{reach}F_t(M)/D>25/544>3/100
\quad\text{对全部 }t.
\tag{3}
$$

沿用题目定义
\(\delta_{\rm hold}=\max_{t\in[0,1]}d_H(F_t(M),F_0(M))\)，
\(\delta_{\rm E}=\max_{t\in[0,1]}\min_{A\in E(3)}d_H(AF_t(M),F_0(M))\)。
前者不作刚体对齐，后者包括反射。H是固定闭集且有二维内部。新领实际含正 K和负 K开区域。这里不要求 C3；只有一处选定的固定角区，不能把旧三扇区属性移到这个新实例。

## 2. 完全固定的强核心及实际见证

沿用 R56的同一强核，参数 τ∈[0,9/10]，最后置 τ=9t/10。为了使输入可直接核对，重列其定义：

$$
E(x)=\begin{cases}e^{-1/x},&x>0,\\0,&x\le0,\end{cases}
\qquad
\sigma(x)=\frac{E(x)}{E(x)+E(1-x)}.
$$

令

$$
g_*(s)=\sigma(20s-7)\sigma(15-10s),
$$

在 [0,π]上取 f(φ)=g_*(φ)−g_*(π−φ)，再作奇延拓和2π周期延拓。令

$$
\psi(\phi)=\int_0^\phi f(s)\sin(\phi-s)\,ds,\qquad
h_\tau=1+\tau\psi,\qquad
\rho_\tau=h_\tau+h_\tau''=1+\tau f.
\tag{4}
$$

R56已经完整证明这些函数真实 C∞ 周期、ψ平均为0，且

$$
1/10\le\rho_\tau\le19/10.
$$

实际凸曲线及共同材料弧长为

$$
\widehat\gamma_\tau=h_\tau e_r+h_\tau'e_\phi,\qquad
u_\tau(\phi)=\phi+\tau\left(\int_0^\phi\psi(s)\,ds+\psi'(\phi)\right),
\qquad
\gamma_\tau(u)=\widehat\gamma_\tau(\phi_\tau(u)).
\tag{5}
$$

这里 u_τ′=ρ_τ>0，其逆真实光滑周期。于是

$$
|\gamma_\tau'|=1,\qquad
C_0(u):=\kappa_\tau(u)\in[10/19,10].
\tag{6}
$$

各有限角阶范数在整个固定 τ区间统一有限。

R56的构造给 ψ=0于 |φ|≤7/20，且从0起的积分也为0。因此在这整段内 u_τ=φ，实际有

$$
\gamma_\tau(u)=e_r(u)\quad (|u|\le7/20)
\tag{7}
$$

及全部位置/框架/角 jet相同。虽然 R56的握持片只使用 |u|≤3/10，有限传播这里可用更大的(7)，并非另假定固定弧。

保留原负侧柱面

$$
B_\tau(r,u)=\gamma_\tau(u)+r e_z,\qquad -h_0\le r\le0,\quad h_0=1/100.
\tag{8}
$$

两个后面仍使用的精确支持见证是

$$
I_*=\int_{7/20}^{3/2}g_*(s)\cos s\,ds>59/100,
\quad
\psi(\pi/2)=I_*,
\quad
\psi(\pi)=0,\quad\psi'(\pi)=-2I_*.
\tag{9}
$$

R56通过 g_*=1于[2/5,7/5]及交错 Taylor 界证明 I_*>59/100；附录也重核所需有理比较。这里仅承接其已审核心，后面的新图包络、度量和 C²门重新支付。

## 3. 单调上升 Q、统一寿命与最后一次选 T

固定

$$
\varepsilon=1/100000,\qquad q_*=\varepsilon/100=1/10000000,
\qquad S(x)=\sigma(2x-1/2).
\tag{10}
$$

S非减，x≤1/4时为0，x≥3/4时为1。对尚未最后选定的 δ>0，令

$$
Q_\delta(r)=q_*S(r/\delta),\qquad
a''=Q_\delta/a,\quad a(0)=1,\quad a'(0)=0.
\tag{11}
$$

负侧取 a=1。这里**只用上升段**，以后不把出口称作 flat领。对固定 r≤1/2窗口，

$$
a\ge1,\quad 0\le a''\le q_*,
\quad 0\le a'\le q_*r,\quad
0\le w:=a-1\le q_*r^2/2.
\tag{12}
$$

从(8)的真实初值

$$
F(0,u)=\gamma_\tau(u),\quad
e_1=e_z,\ e_2=T_\tau,\ N=\nu_\tau=e_z\times T_\tau,\quad
M(0,u)=0,\ C(0,u)=C_0(u)
$$

应用 R50。其 X=M/C、Y=1/C 初值是 X_0=0、Y_0=ρ_τ∈[1/10,19/10]，背景 P恒为0，全部所需角范数统一有限。系数 a,a′,Q的低阶上界由(12)给出，不使用 δ^{-1}或 Q′的大小决定寿命。

对正则化参数 0<η≤q_*，R50中的 q=Q+η≤2q_*。先取得一个共同 T_0>0并统一缩小，使原物理解与所有正则化解在 [0,T_0]存在，且

$$
|X_\eta|\le1/4,\qquad 0<Y_\eta\le2,
\tag{13}
$$

Y还具有统一正下界。原因是初值距这些界有固定余量，混合角能量控制实际 X,Y的低阶角范数；实际时间方程中的大阻尼精确抵消，故低阶时间导数有不依η或δ高导数的统一界。全部高阶能量共用这个时间。

原物理方程

$$
L=(M^2-Q)/C,\quad
M_r=L_u-(a'/a)M,\quad
C_r=M_u+(a'/a)C+aa'L
\tag{14}
$$

只用 Q和一次角导数。先有共同正性及低阶角界后，可固定 K_*≥1，使所有候选 δ和τ上

$$
|M_r|+|C_r|\le K_* .
\tag{15}
$$

现在固定角截止

$$
B_0(x)=1-\sigma((4x^2-1)/3),\qquad
\chi(u)=1-2B_0(5u)\quad(-\pi\le u\le\pi),
\tag{16}
$$

再周期延拓。它在接缝附近恒1，故真实 C∞；−1≤χ≤1，

$$
\chi=-1\ (|u|\le1/10),\qquad
\chi=1\ (|u|\ge1/5).
\tag{17}
$$

记 K_1=||χ′||∞、K_2=||χ″||∞。这两个常数由(16)一次固定。

**最后才**选择一次 T>0，使

$$
T<\min\{T_0,\ 1/2000,\ \varepsilon/(100K_*)\},
\qquad
T(K_1+2)\le1,\quad
T^2(K_2+2K_1+2)\le1,
\tag{18}
$$

并固定 δ=T/2。以上有限个正门可同时满足。T、δ、a、Q及完整材料域随后对全部τ固定，不以 τ另选，也不把 δ变化当作主 flat17的网格加密。

由(15)、(18)，

$$
|M|\le\varepsilon/100,\quad
|C-C_0|\le\varepsilon/100,\quad
1/2<C<11.
\tag{19}
$$

物理图记为 F_τ^hyp，它真实具有共同 dr²+a²du²、全圈位置周期。位置和框架由与(14)相容的径向反对称 ODE重构，初值已经是实际周期位置。入口 r≤δ/4=T/8上 Q=0、a=1，唯一性给 F_τ^hyp=B_τ，与旧柱面在开区全 jet相同。

## 4. 更强角数据下的有限传播与真实位置开重叠

R57的局部差能量并不要求初始 C接近1；它使用共同角范数、正性及统一特征速度界。这里(13)和 2q_*<1/16给

$$
|X_\eta|+\sqrt{Q+\eta}\,Y_\eta
\le1/4+(1/4)\cdot2=3/4<1.
\tag{20}
$$

因此原 R57证明在新强核上原样适用。具体地，在内缩区间
I_r=(−7/20+r,7/20−r)上，对两个正则化解的差 (z,y) 使用

$$
\mathcal E_s(r)=
\sum_{k=0}^s\int_{I_r}\{(Q+\eta)|\partial_u^kz|^2+
|\partial_u^ky|^2\}\,du
+\sum_{k=0}^{s-1}\int_{I_r}|\partial_u^kz|^2\,du,\qquad s\ge4.
$$

配对主通量矩阵的特征值受(20)控制，区间端点以内缩速度1运动，全部边界通量非正。权导数与阻尼给 −Q′|∂^kz|²≤0；未加权低阶 z与 y的导数耦合直接用 y的 H^s控制，不产生1/(Q+η)。高阶系数由统一角能量控制，故 E_s′≤C_sE_s，其中 C_s不依η和Q′的大小。

初始两组数据在(7)开弧内完全相同，所以局部能量为0。先在每个η下取全局 Galerkin 极限的真实光滑解，再使用局部能量，最后令η→0；不对有限 Fourier 投影宣称局部支撑。这给物理 M,C在整个锥内相同。

取第二个初值为 τ=0的圆柱数据。其实际旋转解是

$$
b=\sqrt{1-a'^2},\qquad z(r)=\int_0^r b(s)\,ds,\qquad
F_{\rm rev}(r,u)=a(r)e_r(u)+z(r)e_z .
\tag{21}
$$

它的 L=−a″/b、M=0、C=ab直接满足同一个物理系统；R50唯一性识别它为圆初值解。正则化 q=Q+η本身不冒称满足这个几何关系。

在 |u|<7/20−r的开锥内，L,M,C相同；通向任意锥内点的整条径向线也在锥内。实际位置和框架的初值相同，径向 ODE唯一性遂给

$$
F_\tau^{\rm hyp}(r,u)=F_{\rm rev}(r,u)
\quad (|u|<7/20-r).
\tag{22}
$$

这包括全部位置和 jet，不只有第二基本形式相同。由于
1/4+T<7/20，χ−1的支撑 |u|≤1/5及一个固定开邻域 |u|<1/4始终位于(22)中。

## 5. 实际新图及唯一共同非径向度量

在 0≤r≤T置

$$
\boxed{\quad
F_\tau(r,u)=F_\tau^{\rm hyp}(r,u)+(\chi(u)-1)w(r)e_r(u).
\quad}
\tag{23}
$$

负侧保持(8)。这个公式全圈真实周期。入口 w=0的开段使两侧位置全 jet匹配。

在 χ−1的全部支撑及其开邻域，(22)使(23)恰好等于实际固定图

$$
F_*(r,u)=R(r,u)e_r(u)+z(r)e_z,\qquad R=1+\chi w.
\tag{24}
$$

支撑外则恰好是已有的实际 F_τ^hyp。因而这里没有对不同时间的两个未知图作未经等距核验的插值。

直接微分(24)，

$$
(F_*)_r=\chi a'e_r+b e_z,\qquad
(F_*)_u=w\chi'e_r+R e_\theta.
$$

整张新图的共同度量为

$$
\boxed{
g=\{1+(\chi^2-1)a'^2\}\,dr^2
+2\chi\chi'wa'\,dr\,du
+\{(1+\chi w)^2+w^2\chi'^2\}\,du^2 .
}
\tag{25}
$$

χ=1处它就是原 dr²+a²du²；其余处由实际固定图(24)求出。故(25)对完整材料域和全部时间精确成立，负侧取w=a′=0即为原柱度量。

行列式是

$$
\det g=R^2(b^2+\chi^2a'^2)+b^2w^2\chi'^2>0.
\tag{26}
$$

因为 a−1≤q_*T²/2很小，R≥1−w>0、b>0。这证明实际图正则。χ非恒定的过渡区一般有非零交叉项，这不是原径向度量的改名；不把径向 mixed-flux守恒误套到它。

在 χ=−1的开区，半径为2−a且r仍是弧长，真实形系数为

$$
L_*=\frac{a''}{b},\quad M_*=0,\quad
C_*=(2-a)b>0,\quad
K_{\rm Gauss,*}=\frac{Q_\delta}{a(2-a)}>0\quad(Q_\delta>0).
\tag{27}
$$

在χ=1的开区则 K=−Q_δ/a²<0。由于δ=T/2，
r∈(3T/8,T)上Q=q_*>0，配合 |u|<1/10或任一支撑外开角区，确有两种曲率符号的真实开片。过渡区曲率由(24)决定，不另假设其符号。

出口 Q(T)=q_*>0，本稿没有末端平坦或已经封帽的声明。

## 6. 新图相对强参考柱的完整 C²预算

把参考柱 B_τ=γ_τ+r e_z延到整个 [-h_0,T]×S¹，写

$$
E_{\rm hyp}=F_\tau^{\rm hyp}-B_\tau,\qquad
\Delta=(\chi-1)w e_r,\qquad E=E_{\rm hyp}+\Delta .
$$

负侧两项都为0。下面使用 T<1/1000这个由(18)推出的稍宽上界，以保留清楚的有理预算。

由(12)、(19)，

$$
a'<\varepsilon/100000,\qquad
a-1<\varepsilon/200000000,
$$

$$
|L|\le2\{(\varepsilon/100)^2+\varepsilon/100\}<\varepsilon/20.
\tag{28}
$$

径向框架方程给 |N_r|<3ε/50，并积分得到

$$
|N-\nu_\tau|<3\varepsilon/50000,\quad
|e_1-e_z|<\varepsilon/20000,\quad
|e_2-T_\tau|<\varepsilon/100000.
$$

因此由 F_u=a e_2，

$$
\|DE_{\rm hyp}\|_{\rm op}
<\varepsilon\left(\frac1{20000}+\frac1{100000}
+\frac1{200000000}\right).
\tag{29}
$$

真实二阶差为

$$
(E_{\rm hyp})_{rr}=LN,\quad
(E_{\rm hyp})_{ru}=a'e_2+MN,
$$

$$
(E_{\rm hyp})_{uu}
=-aa'e_1+(C-C_0)N+C_0(N-\nu_\tau).
$$

用 a<2、C_0≤10，有

$$
|(E_{\rm hyp})_{rr}|<\varepsilon/20,\qquad
|(E_{\rm hyp})_{ru}|<\varepsilon/50,\qquad
|(E_{\rm hyp})_{uu}|<\varepsilon/50,
$$

其中最后一项的系数粗界是
2/100000+1/100+30/50000<1/50。
对任意实参数方向v，用2|v_rv_u|≤v_r²+v_u²，

$$
|D^2E_{\rm hyp}[v,v]|\le(7\varepsilon/100)|v|^2.
\tag{30}
$$

新增项的完整导数为

$$
\Delta_r=(\chi-1)a'e_r,\quad
\Delta_u=w\{\chi'e_r+(\chi-1)e_\theta\},
$$

$$
\Delta_{rr}=(\chi-1)a''e_r,\quad
\Delta_{ru}=a'\{\chi'e_r+(\chi-1)e_\theta\},
$$

$$
\Delta_{uu}=w\{(\chi''-\chi+1)e_r+2\chi'e_\theta\}.
$$

由(18)，

$$
\|D\Delta\|_{\rm op}
\le2q_*T+\frac{q_*T^2}2(K_1+2)
\le\frac52q_*T=\frac{\varepsilon T}{40}
<\frac{\varepsilon}{80000},
\tag{31}
$$

$$
|D^2\Delta[v,v]|
\le q_*\{2+T(K_1+2)+\tfrac12T^2(K_2+2K_1+2)\}|v|^2
\le\frac{7\varepsilon}{200}|v|^2 .
\tag{32}
$$

合并得完整固定材料域上的实际门

$$
\boxed{\quad
\|DE\|_{\rm op}<\varepsilon,\qquad
|D^2E[v,v]|\le\frac{21\varepsilon}{200}|v|^2\le\varepsilon|v|^2.
\quad}
\tag{33}
$$

最后一个不等式在 v≠0 时严格，在 v=0 时取等号。这些是位置的完整方向 Hessian预算，已含切向项；不把主曲率或法向分量上界替代它。开重叠保证接缝处也有同一 C²控制。

## 7. 应用已审全法锥引理：全时嵌入和 reach

R56对同一 γ_τ证明了参考柱在任何闭径向区间上的：

- 单位正交参数微分；
- 全局最短材料 lift弦长 |B(q)−B(p)|≥|q−p|/30；
- 方向 Hessian≤10；
- 半径1/10滚动球给出的全部可行法锥不等式，包含两条边界。

它的已审 C²扰动引理对满足(33)的 F=B+E给

$$
\operatorname{reach}F(M)\ge
R_\varepsilon
=\frac{(1-30\varepsilon)^2}{10+45950\varepsilon}
=\frac{99940009}{1045950000}>\frac3{32}.
\tag{34}
$$

为明示全图适用的理由：沿可行材料线段先得
|ΔF|≥(1−30ε)|ΔB|，排除所有自交。固定p处以线性A把
(e_z,T,N_0)映到(F_r,F_u,F_r×F_u)，则 ||A−I||≤5ε。
F−AB在p的一阶导为0，二阶界≤51ε，故
|ΔF−AΔB|≤22950ε|ΔB|²。新图的任何可行法锥向量经 Aᵀ
拉回成为参考柱的同类法锥向量，给分母10+45950ε。
距离平方比较于是排除半径(34)内的两个最近点。

这不是从原 R56像直接转移 reach；(29)–(33)为新图自身支付了引理输入。
T所改变的区间仍是闭区间×材料圆，最短角 lift线段可行；
单侧边界近点完全在引理范围内。所有常数对τ统一，因此全时间嵌入和(34)成立。

## 8. 新初态全图包络和固定 H

取

$$
H=[-3/400,-1/400]\times[-3/10,3/10].
\tag{35}
$$

它是负侧柱核中的闭片且有二维内部。由(7)，每个τ在这个材料片上与初态逐点相同。其同一r上的角±3/10两点给

$$
\operatorname{diam}F_0(H)\ge2\sin(3/10)>591/1000.
\tag{36}
$$

新图正侧的 F_r不再一般为单位向量，所以不能直接沿用旧环带的单位径向长度包络。改从真实 F_0^hyp出发：它的径向速度为1，且从单位圆起步；新增项满足 |Δ|≤2w≤q_*T²。因此任何正侧初态像点到相应单位圆点的距离至多

$$
T+q_*T^2<1/1000 .
\tag{37}
$$

最后一步只需 T<1/2000和 q_*≤1/100，精确有理门见附录。
负侧到单位圆的距离至多h_0。故整个初态像

$$
D\le2(1+h_0+T+q_*T^2)<1011/500<51/25 .
\tag{38}
$$

并且初态的全部像点满足 y<1+1/1000，负侧实际上y≤1。

由(36)、(38)，

$$
\operatorname{diam}F_0(H)/D>197/680>1/4,
$$

而(34)、(38)给全时 reach/D>25/544>3/100。所有分母都是完整新初态直径，不是旧曲线直径或领宽。

## 9. 强握持像位移及覆盖全部 E(3)的有效商位移

修改只在r≥0发生。终态τ=9/10的负侧 r=−1/200仍保留原强核的全部实际点。

先取法向角φ=π/2。其材料角由(5)确定，真实像点p满足

$$
p_y=1+\tau I_*>1+531/1000.
$$

所有初态像点q满足 q_y<1+1/1000，所以

$$
\inf_{q\in F_0(M)}|p-q|>53/100.
$$

因此完整像的单向距离已经给

$$
\delta_{\rm hold}>53/100,\qquad
\delta_{\rm hold}/D>53/204>1/4.
\tag{39}
$$

这是对整张像的 Hausdorff见证，不是某个材料点的轨迹长度。

再取同一负侧r处、φ=0和φ=π的两个真实终态点。由(9)，其水平位置是

$$
(1,0),\qquad (-1,2\tau I_*).
$$

故整个终态直径D_1满足

$$
D_1\ge\sqrt{4+(2\tau I_*)^2}
>\sqrt{4+(531/500)^2}>9/4.
\tag{40}
$$

任意非空紧集满足 |diam K−diam L|≤2d_H(K,L)。每个欧氏刚体运动都保直径，包括反射，所以对全部 A∈E(3)，

$$
d_H(AF_1(M),F_0(M))
\ge(D_1-D)/2>21/200.
$$

固定数值(D_1−D)/2本身严格大于21/200，与A无关，因而取下确界仍有同一严格门。最佳刚体也可取得：有界代价列的平移有界，O(3)紧，取子列即可。于是按题目含min的定义，

$$
\delta_{\rm E}>21/200,\qquad
\delta_{\rm E}/D>7/136>1/20 .
\tag{41}
$$

无需刚体保持H、坐标轴、某个边界或材料标签。联合光滑与紧材料域给全时间 Hausdorff连续，商距离也连续，t∈[0,1]上的max存在；端点见证已足够支付以上下界。

## 10. 已付范围与仍需完成的研究

本稿在一张真实共同度量图上同时组合了强位移、固定H、全时嵌入/厚度及正负曲率开片。正曲率片来自固定参考图的实际替换和开重叠；没有把整圈非解析角数据送入未证明的椭圆 Cauchy问题。

仍有两条边界；r=T处Q=q_*>0，不能称为有限flat出口或帽中心。当前正K固定片只是一段短领，未证明它能重复延到整个圈收缩，也未给全帽的共同度量/标架/两jet匹配。

T、δ由先统一寿命和K_*后选择，严格存在并一次固定；它们尚非有效计算出的宽度。全文没有生成 PDE 解数组或网格，没有支付实际加密、主 flat17 G5或最终未参与者从种子重跑。它和R56、R57及flat17具有各自不同的g，不相互冒充一次加密。

以下小程序只核有限有理比较；完整存在、有限传播、实际贴接、reach和两种像距离必须由全文证明及独立审查支付。

## 附录 A. 冻结的纯标量检查源

必须先冻结本文并固定回读，再从唯一 JavaScript围栏提取源执行；实际时间、源哈希和结果另存小回执。正文不预填PASS。程序不求解PDE，不生成曲线/网格数组，不证明统一寿命，也不替代全文独审。

```javascript
(() => {
  "use strict";
  const abs=x=>x<0n?-x:x;
  const gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;};
  const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];};
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const sub=(a,b)=>add(a,Q(-b[0],b[1]));
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const pow=(a,k)=>{let r=Q(1);for(let j=0;j<k;j++)r=mul(r,a);return r;};
  const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1],rows=[];
  const eq=(name,a,b)=>{if(cmp(a,b)!==0n)throw Error(name);rows.push({name,status:"PASS"});};
  const lt=(name,a,b)=>{if(!(cmp(a,b)<0n))throw Error(name);rows.push({name,status:"PASS"});};
  const eps=Q(1,100000),q=div(eps,Q(100)),T=Q(1,2000),tau=Q(9,10);
  eq("physical q",q,Q(1,10000000));
  lt("regularized q",mul(Q(2),q),Q(1,16));
  eq("speed upper",add(Q(1,4),mul(Q(1,4),Q(2))),Q(3,4));
  lt("speed below cone",Q(3,4),Q(1));
  lt("support in open buffer",Q(1,5),Q(1,4));
  lt("buffer in finite propagation cone",add(Q(1,4),T),Q(7,20));
  lt("C lower",Q(1,2),sub(Q(10,19),div(eps,Q(100))));
  lt("C upper",add(Q(10),div(eps,Q(100))),Q(11));
  lt("slope coarse",mul(q,T),div(eps,Q(100000)));
  lt("radial radius coarse",div(mul(q,pow(T,2)),Q(2)),div(eps,Q(200000000)));
  lt("radius below two",add(Q(1),div(mul(q,pow(T,2)),Q(2))),Q(2));
  lt("L upper",mul(Q(2),add(pow(div(eps,Q(100)),2),q)),div(eps,Q(20)));
  eq("normal derivative",add(Q(1,20),Q(1,100)),Q(3,50));
  lt("e1 difference",mul(div(eps,Q(20)),T),div(eps,Q(20000)));
  lt("e2 difference",mul(div(eps,Q(100)),T),div(eps,Q(100000)));
  lt("normal difference",mul(mul(Q(3,50),eps),T),mul(Q(3,50000),eps));
  lt("hyp mixed Hessian",add(Q(1,100000),Q(1,100)),Q(1,50));
  lt("hyp angular Hessian",add(add(Q(2,100000),Q(1,100)),Q(30,50000)),Q(1,50));
  eq("hyp direction Hessian",add(Q(1,20),Q(1,50)),Q(7,100));
  eq("added direction Hessian",mul(q,add(add(Q(2),Q(1)),Q(1,2))),mul(Q(7,200),eps));
  eq("total direction Hessian",add(Q(7,100),Q(7,200)),Q(21,200));
  lt("total Hessian budget",Q(21,200),Q(1));
  eq("added derivative envelope",mul(mul(Q(5,2),q),T),div(eps,Q(80000)));
  lt("total derivative budget",add(add(add(Q(1,20000),Q(1,100000)),Q(1,200000000)),Q(1,80000)),Q(1));
  lt("positive chord factor",mul(Q(30),eps),Q(1));
  const reach=div(pow(sub(Q(1),mul(Q(30),eps)),2),add(Q(10),mul(Q(45950),eps)));
  eq("exact reach",reach,Q(99940009,1045950000));
  lt("absolute reach",Q(3,32),reach);
  lt("new initial displacement",add(T,mul(Q(1,100),pow(T,2))),Q(1,1000));
  const D=mul(Q(2),add(add(Q(1),Q(1,100)),Q(1,1000)));
  eq("diameter envelope",D,Q(1011,500));
  lt("diameter convenient bound",D,Q(51,25));
  const grip=mul(Q(2),sub(Q(3,10),div(pow(Q(3,10),3),Q(6))));
  eq("grip chord",grip,Q(591,1000));
  eq("grip ratio",div(grip,Q(51,25)),Q(197,680));
  lt("grip target",Q(1,4),Q(197,680));
  const sx=Q(7,5),sy=Q(2,5);
  const low=sub(add(sub(sx,div(pow(sx,3),Q(6))),div(pow(sx,5),Q(120))),div(pow(sx,7),Q(5040)));
  const high=add(sub(sy,div(pow(sy,3),Q(6))),div(pow(sy,5),Q(120)));
  lt("source support integral",Q(59,100),sub(low,high));
  eq("terminal north increment",mul(tau,Q(59,100)),Q(531,1000));
  eq("whole image held gap",sub(Q(531,1000),Q(1,1000)),Q(53,100));
  eq("held ratio",div(Q(53,100),Q(51,25)),Q(53,204));
  lt("held strong",Q(1,4),Q(53,204));
  lt("terminal diameter witness",pow(Q(9,4),2),add(Q(4),pow(Q(531,500),2)));
  eq("all E3 distance gap",div(sub(Q(9,4),Q(51,25)),Q(2)),Q(21,200));
  eq("all E3 ratio",div(Q(21,200),Q(51,25)),Q(7,136));
  lt("all E3 strong",Q(1,20),Q(7,136));
  eq("reach ratio",div(Q(3,32),Q(51,25)),Q(25,544));
  lt("reach target",Q(3,100),Q(25,544));
  return {kind:"exact-BigInt-scalar-gates",pass:rows.length,fail:0,checks:rows,
    pde_runs:0,solver_runs:0,geometry_arrays:0,terminal_math_runs:0};
})()
```


## 正式采用与本轮真实独审

原作者稿逐字保留于 `notes/2026-11-10-db6f-strong-support-mixed-curvature-collar-v1.md`，
23,363 B，SHA256 `0bb11a1acad3d19f2751cbaa554a0e727aaed192559e5b709281da0e78fb3955`。

新会话未参与者全文审稿为
`notes/2026-11-10-78718-root-review-strong-mixed-collar.md`，
SHA256 `a73962e69f0fe7bbd8ccf66b266322063368e4369c323bbdeec6e5aad7018758`。已实际逐节核对统一寿命、有限传播的真实位置开重叠、
新共同度量、全部位置 Hessian、边界法锥 reach 与完整像的两种位移门。
没有依靠标量程序代替这些论证。

原附录的44个纯 BigInt 有理门由本轮 root 实际 Node 重放，
工具回执 `204847` 自然 exit0，0.102492678 秒；报告
`notes/2026-11-10-78718-strong-mixed-collar-scalar-replay.json`，
SHA256 `74e6e3bf820d5adf028675084f24dbafde6bcb8d8224a3922c994fdb8a26cfcb`。
没有 PDE、主候选、几何数组或网格执行。

本结果仍有两条边界，宽度只由统一寿命存在性选取，出口不平坦；
不是闭曲面、原 flat17 的加密或 README 完成。
