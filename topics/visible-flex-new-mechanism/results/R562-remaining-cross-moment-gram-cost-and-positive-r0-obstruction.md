# R562：剩余交叉矩的闭振子成本与同规范六零族的严格正 R0

日期：2026-11-16。**原式纸证；没有执行数值、符号、求积、profile、秩或开发检查。**

本稿承接 R555 的完整原矩、R557 的真实五零词，以及 R559 已写出的同一规范长形状六零族。新增结论是：

1. 任一闭线性法向振子的交叉 Gram 不是可任意选号、任意定价的方向；负交叉有一个严格的线性负 S0 成本。
2. R559 六零词的完整中心 R0 并非只“未知”：在该实际参数族中，它有严格正净首项。
3. 在同类实际低尾公式下，准确清 P0 会锁定低尾 R0 的正领先系数。即使第三个正低尾支付了 0/2/4 矩，也不能靠这些参数或原正交叉长回路将 R0 清零。

上述是当前真实族的障碍，不是一般同规范路径不可达。非闭法向能量、改变真实有效 Gram、不同静态区间或其它尺度仍可能离开本稿的假设。它们必须保原 incoming、第三 history、桥和真实端 germ，不能从形式配权获得。

## 1. 固定坐标和完整原式

始终用 R521/R552 的同一固定中心 y=x+ωc，原第二规范为0。记

\[
\eta=\omega-\omega_c,\quad d=h\eta-k,\quad
u=d/h,\quad b_h=h^{-1},\quad
v=h_s/h,\quad w=d_s/h,\quad \rho=u^2+b_h^2.
\tag{1}
\]

s 是原实际时间，w 在本稿只表示 d_s/h。原水平关系为

\[
\eta_s=k_s/(2h),\qquad w=u_s+uv,\qquad (b_h)_s=-b_hv.
\tag{2}
\]

用 R555 的两个 scalar

\[
\mathcal A=h^2(\eta^2-u^2)-1
=k^2+2kd-1,\qquad
\mathcal B=u\mathcal A+2p_0,
\tag{3}
\]

直接代入 d=hη−k，还得到一个有用的准确式

\[
\boxed{\mathcal B=\eta(kd-1).}
\tag{4}
\]

完整原 p 和余槽是

\[
p_2=-kh/2,\quad p_1=2up_2,\quad p_0=\rho p_2,
\tag{5}
\]

\[
\begin{array}{c|c}
8t_1&\mathcal A-v^2\\
4s_1&u\mathcal A-vw\\
4s_0&u\mathcal B-w^2\\
8r_1&\rho\mathcal A+\rho v^2-2uvw\\
8r_0&\rho\mathcal B+\rho vw-2uw^2 .
\end{array}
\tag{6}
\]

原 trace 关系 t0=p0/4+s1/2 保留。上标 [0]、[2] 分别表示(6)的静态部分和速度二次部分；不是把原实际路径分成可自由相加的两个控制。

由(4)立刻有

\[
\boxed{r_0^{[0]}=\frac{\rho}{8}\eta(kd-1).}
\tag{7}
\]

这给一个真正的点态号门：在 h>0、η<0、kd<1 的实际区间，静态 r0 严格正；在 η>0、kd<1 时静态 r0 严格负。当前构造已有负 r0 的高尾，但其真实时间和高度尺度不足以抵消低尾。这一点将在第5节定量支付，不能只据点态负号配权。

## 2. 任意真实速度的完整 Gram 与顶行交叉

在任意实际区间 J 上定义

\[
F=\int_Jv^2ds,\quad C=\int_Jvw\,ds,\quad
G=\int_Jw^2ds.
\]

于是

\[
\begin{pmatrix}F&C\\C&G\end{pmatrix}\succeq0,\qquad C^2\le FG,
\tag{8}
\]

而原三个速度矩为

\[
N_{T_1}=-F/8,\qquad N_{S_1}=-C/4,\qquad
N_{S_0}=-G/4.
\tag{9}
\]

顶行不能自由改号：

\[
r_1^{[2]}=-\rho\,t_1^{[2]}+u\,s_1^{[2]},\qquad
r_0^{[2]}=-\frac{\rho}{2}s_1^{[2]}+u\,s_0^{[2]}.
\tag{10}
\]

这些是任意真实 incoming 下的准确点态式，不要求历史零或近静态。若 u、ρ 接近常数 u0、ρ0，则由 Cauchy 得明确误差界

\[
\left|N_{R_1}+\rho_0N_{T_1}-u_0N_{S_1}\right|
\le \frac{\|\rho-\rho_0\|_\infty F}{8}
+\frac{\|u-u_0\|_\infty\sqrt{FG}}4,
\tag{11}
\]

\[
\left|N_{R_0}+\frac{\rho_0}{2}N_{S_1}-u_0N_{S_0}\right|
\le \frac{\|\rho-\rho_0\|_\infty\sqrt{FG}}8
+\frac{\|u-u_0\|_\infty G}4.
\tag{12}
\]

因此“接近同一低状态”有一个可直接记账的含义；不能只把低状态值代入后不保系数变化。

在 Sc=(H,0,η=0) 的闭回路领先尺度上，取原快时钟 τ=(s−sin)/δ，并令

\[
h=H+\epsilon f(\tau),\qquad d=\epsilon D(\tau).
\]

记

\[
F_f=\int f'^2,\quad C_f=\int f'D',\quad G_f=\int D'^2.
\]

完整原表(6)给同一个回路的领先速度成本

\[
\begin{aligned}
\delta\,\Delta R_1&=\epsilon^2F_f/(8H^4),&
\delta\,\Delta T_1&=-\epsilon^2F_f/(8H^2),\\
\delta\,\Delta S_1&=-\epsilon^2C_f/(4H^2),&
\delta\,\Delta S_0&=-\epsilon^2G_f/(4H^2),\\
\delta\,\Delta R_0&=\epsilon^2C_f/(8H^4).
\end{aligned}
\tag{13}
\]

实际路径的静态、系数变动、端控、incoming 与桥误差必须另保；R557/R559 正是对其各自真实回路支付这些误差。尤其

\[
\Delta S_1+2H^2\Delta R_0=0
\tag{14}
\]

只是该低状态速度领先项的关系，不是任意全词的准确恒等。

## 3. 闭法向振子给负交叉的严格成本

先给一个完整的线性积分命题。设 β>0、ω²>0 为固定常数，

\[
D''+\omega^2D=-\beta f''
\tag{15}
\]

在有限快区间成立。乘以 D 并作一次分部积分，得到

\[
\boxed{
\int D'^2+\beta\int f'D'
=\omega^2\int D^2+
[D(D'+\beta f')]_-^+.}
\tag{16}
\]

没有删入端的振子能量或自由状态。若 D 两端为0，边项为0。非平凡紧支撑闭回路于是满足

\[
\boxed{G_f+\beta C_f=\omega^2\int D^2>0.}
\tag{17}
\]

所以若 C_f<0，

\[
G_f>\beta|C_f|.
\tag{18}
\]

结合(13)，对这一闭回路的领先增量，负 R0 必支付

\[
\boxed{
-\Delta S_0>2H^2\beta\,(-\Delta R_0)>0.
}
\tag{19}
\]

这比单独的 C_f²≤F_fG_f 给出了不同的必要信息：反交叉不能靠把高度速度幅度与法向速度幅度自由配比而变得廉价。它还给正 S1，且与负 R0 的比例由(14)固定。

(16)同时指出适用边界：若真实入口、出口未准备成闭法向领先条件，必须保方括号；不能把(19)推广到带入端振子能量的任意轨道。若 β 换号、ω²失去正性，或新路径不在此常系数领先类，也不属于(19)的假设。

### 3.1 形状伸缩不会保存原交叉零

R557/R559 的紧支撑形状取

\[
D=\psi'',\qquad f=-(\psi''+\omega^2\psi)/\beta.
\]

反过来，任意紧支撑光滑闭解(15)都可这样表示：积分(15)及其乘 τ 的式子，得到 D 的零阶、一阶矩为0；令 ψ''=D 且在左侧取 ψ=ψ'=0，右侧也为0，再由(15)及紧支撑删去唯一可能的仿射差。

置

\[
I_j=\int(\psi^{(j)})^2,\quad j=1,2,3.
\]

对非零紧 ψ，三个 Ij>0，而且

\[
I_2^2<I_1I_3.
\tag{20}
\]

Cauchy 的等号会迫 ψ''' 为 ψ' 的常数倍；紧支撑的对应常系数 ODE 只有零解，所以这里严格。

对 ψL(τ)=√L ψ(τ/L)，准确有

\[
\begin{aligned}
F_L&=(\omega^4I_1-2\omega^2I_2/L^2+I_3/L^4)/\beta^2,\\
G_L&=I_3/L^4,\\
C_L&=(\omega^2I_2/L^2-I_3/L^4)/\beta,
\end{aligned}
\tag{21}
\]

以及

\[
\boxed{
F_LG_L-C_L^2
=\frac{\omega^4}{\beta^2L^4}(I_1I_3-I_2^2)>0.}
\tag{22}
\]

在原 R559 的 ω²=1、β>0 下，充分长 L 的 C_L 严格正，因此 S1 负、R0 正；只有 L²<I3/I2 才得到负交叉。把 f、D 同时变号，或反转快时间方向，不改变 C_L 的号。只反转 D 却保 f 不变不满足同一(15)。

原二阶第三速度面积 ∫D'f'' 在这些紧形状上准确为0，但这个面积零并不等于 C_L=0；R559 的两个剩余交叉首项必须照付。

## 4. 当前实际 core 的共同尺度与来源

以下严格使用 R556/R557/R559 的原完整实际族：

\[
R=L_h/\sqrt\lambda,\quad M=(1+\log R)^6,\quad
\delta=\lambda^2\zeta,\quad \epsilon=R^{-3/4}.
\tag{23}
\]

母库、右锚、ωc、H、H0、c 与原固定规范

\[
\nu=\delta^{-2}(-H_0^2\lambda,\,2c,\,\lambda)
\tag{24}
\]

在每条实际词内部不变。所有控制参数都不进入 ν。

记 A=A_Y>0、Z=Z*>0、g0>0、\(\mathfrak b>0\)。原两低尾的节点是 z1=Z、z2=Z/2，实际时长为

\[
T_i=\frac{M\ell_i}{\delta R^{3/2}},\qquad
h_i^2=M\xi\{1+o^1(1)\}.
\tag{25}
\]

其原完整历史给

\[
u_i=-Az_i^2/R+o^1(R^{-1}),\quad
\eta_i-u_i=O((MR)^{-1})+o_\delta,\quad
p_{2,i}=O(R^{-1}).
\tag{26}
\]

所有界在同一个固定正参数盒上一阶统一。这里真低尾并非强制 h 恒定的假解；速度、germ 与第三状态按原反馈恢复。

“core”包括最早真零 history 快准备、饱和等待、两低尾、两高尾与全部有限过渡。后面另有真实下降、长快回路及末端四内控。任何原费用都不能在移到这一记号时被重锚。

## 5. 完整 core 的严格正 R0 领先项

从(26)与(3)，

\[
\mathcal A+1=h^2(\eta-u)(\eta+u)=O(R^{-2})+o_\delta.
\]

又由 p0=ρp2、ρ=1/(Mξ)+O(R^{-2})，

\[
2p_0=O((MR)^{-1})+O(R^{-3}).
\]

故低尾上

\[
\mathcal B=u\mathcal A+2p_0
=Az_i^2/R+o^1(R^{-1}),
\]

\[
\boxed{
r_0^{[0]}=
\frac{Az_i^2}{8M\xi R}
+o^1((MR)^{-1}).}
\tag{27}
\]

积分实际时长(25)得到

\[
\boxed{
\delta R^{5/2}R_0^{[0]}\big|_{\rm low}
\longrightarrow
\frac{AZ^2}{8\xi}(\ell_1+\ell_2/4).}
\tag{28}
\]

必须核清其它全部原段在这个尺度的大小，而不是只报低尾正号。

### 5.1 高尾和饱和段

在两个原高尾，

\[
h\asymp\sqrt M R,\quad u=O(R^{-1}),\quad
\eta=O(M/R),
\]

实际总时长为 O((δM²R^{3/2})^{-1})。于是

\[
\rho=O(R^{-2}),\quad
\mathcal A=O(M^3),\quad
p_0=O(M^2/R),\quad
\mathcal B=O(M^3/R).
\]

由完整静态式 r0=ρB/8，

\[
R_0^{[0]}\big|_{\rm high}
=O\!\left(\frac{M}{\delta R^{9/2}}\right),
\qquad
\delta R^{5/2}R_0^{[0]}\big|_{\rm high}
=O(M/R^2)\to0.
\tag{29}
\]

这些高尾可以有负静态 r0；(29)才是其不能抵消(28)的原因。

共同饱和段 h∼R、k=O(1)、u,η=O(R^{-1})，故 A=O(1)、B=O(R^{-1})、r0[0]=O(R^{-3})。其原时长 O((1+logR)/(δR^{3/2})) 给

\[
\delta R^{5/2}|R_0^{[0]}|_{\rm saturation}
=O((1+\log R)/R^2)\to0.
\tag{30}
\]

### 5.2 真快准备、全部速度和有限桥

最早原 R544 快准备的完整速度二次矩是 O(λ²/δ)，因此

\[
\delta R^{5/2}|R_0|_{\rm first\ fast}
\le C R^{5/2}\lambda^2=O(R^{-3/2})\to0.
\tag{31}
\]

没有把这个原 1/δ 费用混入“最后小 δ 即免费”的桥常数。原早期恒参考长段使用其真实时长及小状态盒，静态费用更低阶，速度费用同样按原构造保留。

低尾、高尾的真实慢反馈速度 h_s,k_s=O(C_Rδ)，代入(6)的全部 M2 后，在各自原时长上积分；每个固定有限 R 上，再取同一个 δ，使这些归一费用趋零。所有其它有限桥、开放段与最终下降的完整原矩都进入 C_R，并保参数一阶导数，最后统一小 δ 支付。

这些估计不要求它们的第三状态为零。原矩的几何值由实际解给出；大 incoming A/T 始终经同一 ruling 决定该解。R559 已支付的完整历史盒与真实反馈使上述实际标量/速度界成立。

于是，完整 core 的结论为

\[
\boxed{
\delta R^{5/2}R_0^y\big|_{\rm core}
=\frac{AZ^2}{8\xi}(\ell_1+\ell_2/4)+o^1(1).}
\tag{32}
\]

原三参数共同零满足

\[
\ell_1+\ell_2/4=2\mathfrak bZ/3,\qquad
\xi=g_0\mathfrak b/(9c).
\]

因此在真实根的极限，

\[
\boxed{
\delta R^{5/2}R_0^y\big|_{\rm core}
\longrightarrow
C_0:=\frac{3cAZ^3}{4g_0}>0.}
\tag{33}
\]

## 6. R559 六零词仍有严格正净 R0

R559 的长形状使用

\[
L=\ell_f\sqrt R\,M^{-1/4},
\]

其中 ℓf 与正幅值 a 都在固定正紧盒。它的实际完整回路已经支付

\[
\delta\,\Delta R_0^y
=
\frac{\epsilon^2a^2I_2}{8H^4\beta L^2}\{1+o^1(1)\}.
\tag{34}
\]

该相对精度包含真实 incoming、长区间历史反馈、四个末端内控及真正开放反馈 germ，不由本稿重新假设或省略。

由(23)(34)，

\[
\frac{\delta R^{5/2}}{\sqrt M}\Delta R_0^y
\longrightarrow
\frac{a_*^2I_2}{8H^4\beta\ell_{f,*}^2}>0.
\]

完整 core 的(32)、全部有限桥与原停止值校正，在这个更粗的 √M 归一后趋零。故得到新结论

\[
\boxed{
\frac{\delta R^{5/2}}{\sqrt M}R_0^{y,\rm total}
\longrightarrow
\frac{a_*^2I_2}{8H^4\beta\ell_{f,*}^2}>0.}
\tag{35}
\]

**所以 R559 的实际六零词，在足够大有限 R、随后同一次足够小正 δ 下，完整 R0^y 严格正。** 不是只给新增回路一个正号，也不是忽略 core 后推断总号。

在其六个准确零处，剩余矩阵为

\[
\begin{pmatrix}
0&0&-4R_0^y\\
0&2S_1^y&0\\
0&0&-2S_1^y
\end{pmatrix},
\]

其中(35)已经说明它尚非零。是否再清 S1 不改变这一结论。

本节只消费 R559 指定的正盒和伸缩族。不能把它扩写为所有六零实际词都必须 R0>0；换真实历史或不同控制族可能改变(32)和(34)。

## 7. 第三个正低尾的 0/2/4 矩为何不能清这项正余量

本节是一个明确的条件性推广，不预授尚待完成的第三低尾。假设已在同 χ、完整 incoming 下构造有限 n 个真实低尾，节点 zi=Zri>0、正时长参数 ℓi>0，并支付(25)(26)、高尾盒、全部桥及其 C1 余量。记

\[
\mu_j=\sum_i\ell_i r_i^j.
\]

如果真实端图的同阶公式仍是

\[
F_0^\infty=Z-\frac{g_0\mu_2}{6c\xi},
\tag{36}
\]

那么同一原式证明给

\[
\delta R^{5/2}R_0^y\big|_{\rm core}
=\frac{AZ^2\mu_2}{8\xi}+o^1(1)
=\frac{3cAZ^2}{4g_0}(Z-F_0^\infty)+o^1(1).
\tag{37}
\]

**在清 P0 的分支上，领先值仍被锁为 C0=3cAZ³/(4g0)。** 这个结论甚至不需要先固定 μ0、μ4。改变正节点、权重或共同低高度参数 ξ，只要仍按(36)保 P0，就不能改变这个正基值。

拟用第三低尾付出的前三个矩为

\[
\mu_0=2\mathfrak bZ,\quad
\mu_2=2\mathfrak bZ/3,\quad
\mu_4=2\mathfrak bZ/5.
\tag{38}
\]

例如节点 (1,1/2,1/4) 的归一正权 (107,440,128)/675 在形式上满足 0/2/4 矩，且对应 Vandermonde 非退化。这个代数事实不构造第三次真实 W/history 或 bridge；(37)还说明即使这些真实义务全部付完，领先 R0 也没有被这三个矩清掉。

若其后追加 R559 同类真回路，但取 L=ℓf√R，则

\[
\boxed{
\delta R^{5/2}R_0^{y,\rm total}
\longrightarrow
C_0+\frac{a_*^2I_2}{8H^4\beta\ell_f^2}>0.}
\tag{39}
\]

正盒内 ℓf 的导数可以非零，却不能据此在没有共同零的地点使用 IFT 宣告 R0 可清。仅有局部秩或一个有向调节量不足以越过(39)的正基值。

若允许不同实际低高度、不同有效 Gram、负 u/正 u 的真实转换或更多强段，(36)可能改变；这些是新的实际问题，本节没有排除。

## 8. “再添一条反交叉短回路”的尺度障碍

当前 core 的正 S0 供给只有

\[
S_0^{\rm core,+}
=O\!\left(\frac{M}{\delta R^{7/2}}\right).
\tag{40}
\]

这是原完整 core 的正首项尺度，包含最早负速度费用；不能从负速度 Gram 本身制造另一份正 S0。

而(33)或(39)要求补偿至少

\[
-R_0^{\rm correction}\asymp
\frac1{\delta R^{5/2}}.
\tag{41}
\]

考虑有限条确实实现了闭线性领先(15)的低状态回路，H、β 保固定正下界，静态/历史/端控误差在(40)(41)所需尺度上已真实控制。对其中所有给负交叉的回路相加，(19)要求负 S0 成本至少为常数倍

\[
\frac1{\delta R^{5/2}}.
\tag{42}
\]

即使另一些回路给正交叉，其速度 S0 仍非正，不能支付(42)。两个量级之比为

\[
\frac{R}{M}\longrightarrow+\infty.
\tag{43}
\]

所以，**在这些明确假设下，不能只加反交叉闭回路来修 R0，同时用当前同阶 core 的正 S0 保持 S0=0。**

这不是一般 no-go。它不排除非闭端项(16)、不同 H/β 尺度、额外真实静态正 S0、大有效 Gram 改变或离开当前小态盒。它也不把尚未有精细余项估计的任意 δ 依赖回路塞入(42)；未付误差的路径不在本定理覆盖内。

## 9. 同一完整 incoming 的真实后继接口

所有真实后继必须继续原状态 (S,γ,υ,m,Tthird)，只通过原高度加速度输入，保原水平式与全 ruling。第三增量始终包含

\[
-\int \mathcal N\circ\bar A_{\rm in},\qquad
-\int\mathcal N\circ(\bar A-\bar A_{\rm in}),
\]

以及原 Pacc 两端、速度面积、三次速度与全部 YC 项。即使领先 ∫D'f''=0，也不使完整 third 返回或第一项消失。

在原 P2 已由真实停止事件校正后，设 C 为五个已清目标 (P1,P0,T1,R1y,S0y)，θ 为已付内参数，ξext 为真正的新几何控制。剩余 Q=(S1y,R0y) 的实际导数仍是

\[
D_{\xi_{\rm ext}}Q_{\rm reduced}
=Q_{\xi_{\rm ext}}-Q_\theta(C_\theta)^{-1}C_{\xi_{\rm ext}}.
\tag{44}
\]

其中必须包括停止时间、全部桥、四末控和 incoming 变分。单独取(13)或(34)的回路导数不能代替(44)。

尤其 δR^{5/2}S1 的下一阶仍需要新的完整账：原饱和等待在这个尺度可出现 O(log R)，保 P/T1 的隐式低尾参数位移也可给同阶贡献。现有首项的相消不授其剩余常数或号。本稿没有把这个未支付的余项写成0。

R0 的(35)(39)则不依赖这个未知 S1 次阶，它们已经构成独立完成的新结论。真正下一步需要形成可抵消 C0 的实际负 R0，或改变锁定关系(36)，同时继续保五/六个已清端方程及完整历史。

## 10. 已闭范围和来源

本稿完成：

- 任意真实路径的完整速度 Gram 与顶行系数误差界(8)–(12)；
- 带真实端项的闭振子身份(16)、严格负交叉成本(19)、伸缩 Gram determinant(22)；
- 当前完整 core 的正 R0 净首项(32)(33)，逐项保原准备、饱和、高尾、慢速度及有限桥；
- R559 实际六零词的严格正总 R0(35)；
- 第三同类正低尾在清 P0 分支上的锁定门(37)，及反交叉补救的限定尺度障碍。

原/中心坐标仍按 R555 转换。这里只断言固定 y 的 R0；未清 S1 时不能随意搬成原 x 的同名槽号。完整 M 是否为0当然与坐标无关，本稿证明这些指定词尚未达到它，不宣一般路径不可达。

直接来源：

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：原完整 M0/M2 和水平式；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：同母、原控制、全相位 ruling；
- [R544](R544-one-fixed-gram-and-a-real-path-with-negative-p1-and-positive-t1.md)：唯一规范、原快准备与完整反馈；
- [R555](R555-five-remaining-moments-gram-energy-and-real-history-area-interfaces.md)：完整八矩、速度 Gram、真实端项与中心变换；
- [R556](R556-four-exact-matrix-moments-by-two-real-low-coasts-with-one-gauge.md)：两低尾、原三参数端图和全部同词成本；
- [R557](R557-five-centered-matrix-moments-with-a-real-fast-height-loop-and-one-gauge.md)：真实 incoming 的快回路、四末控和第五零；
- [R559](R559-six-exact-matrix-moments-by-a-slow-fast-height-loop-with-one-gauge.md)：完整 core 的细 S0 尺度、长快统一估计、非零交叉首项和真实第六零。

R555 全文 blob：6b503b544c6f26c0afe59fddf831ab4e671a690e。
R557 全文 blob：cc14b41d4b1ab6d1ad8f0e4959e6108460768a19。
R559 本稿读取的完整稿 blob：288d16c188f64aa208fc4fee6cc7ed8703cc7e51。
本稿不独立重审这些旧构造，不调用其科学程序；以上新结论由已指明实际输入范围和原式直接推导。
