# R126：真实两场 Codazzi、周期重建与连续延拓的误差不等式

2026-11-13，visible-exact-astra-ac0d。

**已证明的内容：**固定旋转对称目标上的两场准确方程、完整周期框架及位置
重建、严格负曲率区的无角导数损失线性能量，以及可直接消费真实径向候选的
$C^0/C^1$ 后验比较式。所有方程保留完整角空间和 mean。

**尚未完成的数值门：**本篇没有把浮点 Codazzi 轨迹认作连续解，没有给
某个指定区间的残差/初误差有向上界，也没有通过 turning root、正帽和尾部
匹配。因此它是 R125 局部真实分支的验证工具，不是精确闭面完成定理。

## 1. 同一固定目标和准确两场

目标保持为 R125 的
$$
 g_0=E(r)\,dr^2+a(r)^2d\theta^2,\qquad a>0,\quad E>0.
 \tag{126.1}
$$
局部改用子午弧长 $ds=\sqrt E\,dr$，下标 $s$ 指对此变量求导。
令 $h=a_s/a$，目标曲率是 $K=-a_{ss}/a$。
取正交切向标架 $e_1=F_s,e_2=F_\theta/a$，法向约定为
$n=e_2\times e_1$。正交第二基本形式写成
$$
 \mathrm{II}=\begin{pmatrix}A&B\\B&C\end{pmatrix}.
$$
在 $C\ne0$ 的图中，完整 Gauss–Codazzi 系统准确等价于
$$
 \boxed{
 A=\frac{K+B^2}{C},\qquad
 B_s=\frac{A_\theta}{a}-2hB,\qquad
 C_s=\frac{B_\theta}{a}+h(A-C).
 }
 \tag{126.2}
$$
例如第一条 Codazzi 来自
$\nabla_{e_1}\mathrm{II}(e_2,e_1)
=\nabla_{e_2}\mathrm{II}(e_1,e_1)$；
连接为 $\nabla_{e_1}e_i=0$、
$\nabla_{e_2}e_1=h e_2$、$\nabla_{e_2}e_2=-h e_1$，
所以两个 $hB$ 都必须保留。

物理 $r$ 变量的入口为
$$
 B_r=\frac{\sqrt E}{a}A_\theta-\frac{2a'}aB,\qquad
 C_r=\frac{\sqrt E}{a}B_\theta+\frac{a'}a(A-C).
 \tag{126.3}
$$
它没有位置演化所需的离散乘法恒等式。完整角平均满足
$$
 \overline B_s=-2h\overline B,\qquad
 \overline C_s=h(\overline A-\overline C).
 \tag{126.4}
$$
腰数据 $\overline B=0$ 可以传播，但 $\overline C$ 不能删除；
非线性商 $(K+B^2)/C$ 的平均也不能以有限非零频率代替。

## 2. 周期框架和真实位置：没有额外未付的闭角条件

给定 (126.2) 的真实周期解，令 $\mathcal E$ 是列为 $(e_1,e_2,n)$ 的
$3\times3$ 矩阵。定义两个反对称矩阵
$$
 M=\begin{pmatrix}0&0&-A\\0&0&-B\\A&B&0\end{pmatrix},\qquad
 N=\begin{pmatrix}0&-a_s&-aB\\a_s&0&-aC\\aB&aC&0\end{pmatrix}.
 \tag{126.5}
$$
首先只沿径向解准确 ODE
$$
 \mathcal E_s=\mathcal E M,\qquad F_s=e_1.
 \tag{126.6}
$$
初始采用 R125 的实际闭腰曲线 $F_0$，及
$$
 e_1(0)=e_z,\quad e_2(0)=F_{0,\theta}/a(0),\quad
 n(0)=e_2(0)\times e_z,
 \quad B(0)=0,\quad C(0)=\frac{n(0)\cdot F_{0,\theta\theta}}{a(0)^2}.
 \tag{126.7}
$$
R124 的非零曲率保证 $C(0)\ne0$，并有 $A(0)=K(0)/C(0)$。
因 $a_s(0)=0$，初始数据准确满足
$\mathcal E_\theta=\mathcal E N$ 和 $F_\theta=a e_2$。

直接矩阵乘法给
$$
 M_\theta-N_s+NM-MN=
 \begin{pmatrix}
 0&a(AC-B^2)+a_{ss}&-A_\theta+2a_sB+aB_s\\
 -a(AC-B^2)-a_{ss}&0&-a_sA-B_\theta+a_sC+aC_s\\
 A_\theta-2a_sB-aB_s&a_sA+B_\theta-a_sC-aC_s&0
 \end{pmatrix}=0.
 \tag{126.8}
$$
因此 $Z=\mathcal E_\theta-\mathcal E N$ 满足 $Z_s=ZM$、$Z(0)=0$，
即 $Z=0$。再令 $Y=F_\theta-ae_2$，由 (126.5)–(126.6)
有 $Y_s=0$、$Y(0)=0$。所以准确得到
$$
 F_\theta=ae_2,\qquad
 \mathcal E_\theta=\mathcal E N,\qquad
 dF\cdot dF=ds^2+a^2d\theta^2=g_0.
 \tag{126.9}
$$
因为 $M$ 反对称，$\mathcal E^T\mathcal E=I$ 准确保持。
因为径向 ODE 的系数和初值都周期，唯一性给整个 $F,\mathcal E$ 周期。
这里没有绕角积分后再忽略的 monodromy、平移缺口或 mean 行。

这构造一个真实等距浸入。在 R125 的充分小腰环带上，它是嵌入；
延拓到较宽区域后，单射、支撑和 reach 仍需另付，不由 (126.9) 自动得到。
当 $A,B,C$ 连续且 (126.2) 具有所需的一阶正则性时，
上述一阶系统给 $C^2$ 的 $F$；分片径向 germ 可在相同连续初迹上接续。

## 3. 严格负曲率区的完整线性能量

设 $K<0$，令 $U=(B,C)^T$。系统为
$$
 U_s=L(U,s)U_\theta+f(U,s),\qquad
 L=\frac1a
 \begin{pmatrix}
 2B/C&-(K+B^2)/C^2\\1&0
 \end{pmatrix},
 \quad
 f=\binom{-2hB}{h((K+B^2)/C-C)}.
 \tag{126.10}
$$
准确特征值是 $(B\pm\sqrt{-K})/(aC)$。取
$$
 H=\begin{pmatrix}
 1&-B/C\\-B/C&(B^2-K)/C^2
 \end{pmatrix}.
 \tag{126.11}
$$
则
$$
 z^*Hz=\left|z_B-\frac BCz_C\right|^2
       +\frac{-K}{C^2}|z_C|^2,\qquad
 \det H=\frac{-K}{C^2}>0,
 \quad HL=(HL)^T.
 \tag{126.12}
$$
这是实际系数的正定对称化，不是圆背景或有限 Fourier 矩阵。
可直接用
$\lambda_{\min}(H)\ge\det H/\operatorname{tr}H$、
$\lambda_{\max}(H)\le\operatorname{tr}H$ 做有向范数转换。

关于一个真实解线性化，$z_s=Lz_\theta+Jz+g$，其中
$$
 J=\begin{pmatrix}
 \frac{2B_\theta}{aC}-\frac{2BC_\theta}{aC^2}-2h&
 -\frac{2BB_\theta}{aC^2}+\frac{2(K+B^2)C_\theta}{aC^3}\\
 2hB/C&-h((K+B^2)/C^2+1)
 \end{pmatrix}.
 \tag{126.13}
$$
完整周期能量 $\mathscr E=\int z^*Hz\,d\theta/(2\pi)$ 准确满足
$$
 \mathscr E'=
 \int z^*\big[H_s-\partial_\theta(HL)+HJ+J^TH\big]z\,
                  \frac{d\theta}{2\pi}
 +2\operatorname{Re}\int z^*Hg\,\frac{d\theta}{2\pi}.
 \tag{126.14}
$$
若实际连续系数给方阵不等式
$H_s-\partial_\theta(HL)+HJ+J^TH\le2\Gamma H$，则
$$
 \sqrt{\mathscr E(s)}
 \le e^{\int_{s_0}^s\Gamma}
 \sqrt{\mathscr E(s_0)}
 +\int_{s_0}^s e^{\int_t^s\Gamma}
        \|H^{1/2}g(t)\|_{L^2_\theta}\,dt.
 \tag{126.15}
$$
没有高频截止或遗漏 mean。该式是线性估计；非线性延拓不能只凭它的
$L^2$ 界宣告闭合，因为 $H_s,J$ 含实际一阶导数。下面给可直接闭合
这些导数的另一套比较。

## 4. 实际 Riemann 变量及其全部低阶项

仍限 $K<0$。令
$$
 k=\sqrt{-K}>0,\quad p=\frac{B+k}{C},\quad q=\frac{B-k}{C},
 \quad \gamma=\frac{\sqrt E}{a},\quad
 \beta=\frac{a'}a,\quad \kappa=\frac{k'}{2k}.
 \tag{126.16}
$$
这里 $\beta=a'/a$ 是物理 $r$ 系数；上文 $h=a_s/a$ 使用弧长。
由准确商法则和 (126.3) 得
$$
 \boxed{\begin{aligned}
 p_r&=\gamma q\,p_\theta-\beta q(1+p^2)+\kappa(p-q),\\
 q_r&=\gamma p\,q_\theta-\beta p(1+q^2)-\kappa(p-q).
 \end{aligned}}
 \tag{126.17}
$$
第一条的输运速度是 $q$，第二条是 $p$，不能写成各自同名速度。
反变换为
$$
 C=\frac{2k}{p-q},\qquad B=k\frac{p+q}{p-q},\qquad A=Cpq.
 \tag{126.18}
$$
这些恒等式保留 $K$ 的真实径向变化；漏掉 $\kappa$ 会求解另一条曲率方程。
在 $K=0$ 附近 $\kappa$ 可能很大，反映此坐标的退化。
它不是曲面不存在或 (126.3) 必然奇异的证据。

## 5. 真正连续 $C^0/C^1$ 后验比较

在一个严格负曲率的闭区间 $I=[r_0,r_1]$ 上，取实际可求值的周期
候选 $P(r,\theta),Q(r,\theta)$。候选可以是分片时间多项式和有限 Fourier
多项式；下面定义的残差总是针对**完整真实系数**，而不是其投影。
为便于书写，定义
$$
 f(p,q)=-\beta q(1+p^2)+\kappa(p-q),\qquad
 g(p,q)=-\beta p(1+q^2)-\kappa(p-q),
$$
$$
 R_P=P_r-\gamma QP_\theta-f(P,Q),\qquad
 R_Q=Q_r-\gamma PQ_\theta-g(P,Q).
 \tag{126.19}
$$
选连续非负的有向上界
$$
 \begin{aligned}
 D_1(r)&\ge\max_\theta(|P_\theta|,|Q_\theta|),&
 D_2(r)&\ge\max_\theta(|P_{\theta\theta}|,|Q_{\theta\theta}|),\\
 \rho_0(r)&\ge\max_\theta(|R_P|,|R_Q|),&
 \rho_1(r)&\ge\max_\theta(|\partial_\theta R_P|,
                               |\partial_\theta R_Q|).
 \end{aligned}
 \tag{126.20}
$$
分片连续上界也可用积分形式处理，端点跳跃必须按真实候选差加入初误差。
设实际解和候选在待验证管中均满足 $|p|,|q|,|P|,|Q|\le M(r)$。
以下系数可全部由候选、系数区间和预设误差屏障直接算出：
$$
 J_0=|\beta|(1+3M^2)+2|\kappa|,\qquad
 A_0=\gamma D_1+J_0,\quad
 A_1=2\gamma D_1+J_0,\quad
 A_{10}=\gamma D_2+6|\beta|M D_1.
 \tag{126.21}
$$
真实误差记为
$$
 e_0=\max(\|p-P\|_\infty,\|q-Q\|_\infty),\qquad
 e_1=\max(\|p_\theta-P_\theta\|_\infty,
                       \|q_\theta-Q_\theta\|_\infty).
$$
在上右 Dini 导数或等价积分比较意义下，
$$
 \boxed{
 D^+e_0\le A_0e_0+\rho_0,\qquad
 D^+e_1\le A_1e_1+\gamma e_1^2+A_{10}e_0+\rho_1.
 }
 \tag{126.22}
$$

**完整推导。** 第一条误差沿 $\partial_r-\gamma q\partial_\theta$ 的实际特征满足
$$
 (\partial_r-\gamma q\partial_\theta)(p-P)
 =\gamma(q-Q)P_\theta+f(p,q)-f(P,Q)-R_P.
$$
$f,g$ 的 Jacobian 行绝对和不超过 $J_0$，故给第一式。
对该式求角导数，令 $w_p=p_\theta-P_\theta,w_q=q_\theta-Q_\theta$。
右端除残差外准确为
$$
 \gamma q_\theta w_p+\gamma w_q P_\theta
 +\gamma(q-Q)P_{\theta\theta}
 +Df(p,q)\cdot(w_p,w_q)
 +[Df(p,q)-Df(P,Q)]\cdot(P_\theta,Q_\theta).
$$
前两项至多 $2\gamma D_1e_1+\gamma e_1^2$，第三项至多
$\gamma D_2e_0$。而 $f$ 的二阶导为
$f_{pp}=-2\beta q,f_{pq}=-2\beta p,f_{qq}=0$；
$g$ 对称。因此 Jacobian 行差至多 $6|\beta|M e_0$，
给 (126.22) 的全部其余项。取两个实际特征族的最大值即可；
无需假设它们等于候选特征线，也没有高频导数损失。

### 可执行的延拓判据

给定初始有向误差 $\epsilon_0,\epsilon_1$，若找到有限非负屏障 $y_0,y_1$
使 $y_j(r_0)>\epsilon_j$（$j=0,1$），并在整个 $I$ 上满足
$$
 y_0'\ge A_0y_0+\rho_0,\qquad
 y_1'\ge A_1y_1+\gamma y_1^2+A_{10}y_0+\rho_1,
 \tag{126.23}
$$
且
$$
 \max_\theta(|P|,|Q|)+y_0<M,\qquad
 \inf_\theta|P-Q|>2y_0,\qquad \inf_I k>0,
 \tag{126.24}
$$
则从同一真实初始数据出发的局部分支可在这个图中连续延拓至 $r_1$，
且 $e_j\le y_j$。

这里的存在接续不是把比较式当成存在性假设：R125 已在腰给真实局部分支。
在任一远离 $K=0$、$p=q$ 的端点，(126.17) 是系数光滑的两条标量输运
方程。把上一步迭代的速度和零阶项冻结，沿其真实特征解线性方程，
在足够短时间上以统一一、二阶角导数界作 Picard 迭代：
特征线之差由速度的 $C^0$ 差和统一一阶导数控制，迭代在 $C^0$ 中收缩；
对方程求一、二阶角导数给相应短时一致界，极限至少为 $C^1$。
若初值光滑，则逐次求角导数延拓正则性。对二阶及更高角导数，
最高阶只线性出现，系数由已控制的一阶导数给出；
故 $e_0,e_1$ 有界排除了有限时一阶爆破。有限区间内 (126.24) 保持
反变换分母非零，标准短时构造可以反复接续。
对实际分片 germ 逐片应用同一过程并匹配连续初迹。

该判据也支持整个辅助参数盒：对每个参数使用各自真实系数，所有
(126.20)–(126.24) 取统一有向界即可。即便候选只取参数中心，
参数变化也应进入 (126.19) 的真实残差，不能删去。

### 从有限两场候选准确生成 Riemann 残差

实际计算可保存有限径向/Fourier 多项式 $\widehat B,\widehat C$，然后用
**真实** $k(r)=\sqrt{-K(r)}$ 定义
$P=(\widehat B+k)/\widehat C$、
$Q=(\widehat B-k)/\widehat C$。该候选通常不是有限 Fourier 多项式，
但分母有严格下界时，它是明确的真实解析函数。
设 $\widehat A=(K+\widehat B^2)/\widehat C$，定义完整未投影残差
$$
 R_B=\widehat B_r-\gamma\widehat A_\theta+2\beta\widehat B,\qquad
 R_C=\widehat C_r-\gamma\widehat B_\theta-\beta(\widehat A-\widehat C).
$$
商法则和 (126.17) 给准确转换
$$
 R_P=\frac{R_B-P R_C}{\widehat C},\qquad
 R_Q=\frac{R_B-Q R_C}{\widehat C}.
 \tag{126.24a}
$$
$k'$ 在残差中准确消掉；仍须在比较系数 $J_0$ 中保留 $\kappa$。
例如
$$
 \partial_\theta R_P=
 \frac{\partial_\theta R_B-P_\theta R_C-P\partial_\theta R_C}{\widehat C}
 -\frac{\widehat C_\theta}{\widehat C^2}(R_B-P R_C).
 \tag{126.24b}
$$
因此 $R,R_\theta$ 的验证只需真实 $K,E,a,a'$ 和候选的两阶角导数、
径向导数及其一阶角导数。候选的真实无限商和所有角格都须包住；
有限 Fourier 投影的 residual 不能直接代入本式。

同样，腰初始曲率可以直接使用 R33 的有限相位
$B_{\rm phase}(\theta)=\sum_j b_j\sin(4j\theta)$：
$$
 B(0,\theta)=0,\qquad
 C(0,\theta)=-\frac{1+\sum_j4j b_j\cos(4j\theta)}{a(0)}.
 \tag{126.24c}
$$
这是准确有限 Fourier 数据，不必先从浮点位置作两次角微分再称其准确。
参数盒内的 $b_j,a(0)$ 仍按真实定义取有向区间；
目标 $E,K$ 的完整 primitive 误差也仍然保留。

## 6. 曲率误差到框架、位置及真实二阶 jet

框架传播本身不需要大的 Gronwall 因子。设候选框架
$\widehat{\mathcal E}$ 和候选位置 $\widehat F$ 具有可计算的真实残差
$$
 R_{\mathcal E}=\widehat{\mathcal E}_r
                 -\widehat{\mathcal E}\,\widehat{\mathcal M},\qquad
 R_F=\widehat F_r-\sqrt E\,\widehat e_1,
$$
其中 $\mathcal M=\sqrt E\,M$，$\widehat{\mathcal M}$ 使用 (126.18) 从候选构造的
$\widehat A,\widehat B$ 及同一个真实 $E,K$。
令 $D=\mathcal E-\widehat{\mathcal E}$。则
$$
 D_r=D \mathcal M+\widehat{\mathcal E}(\mathcal M-\widehat{\mathcal M})-R_{\mathcal E}.
$$
$\mathcal M$ 反对称，故右乘项对 Frobenius norm 的增长贡献准确为零。于是
$$
 \|D(r)\|_F\le\|D(r_0)\|_F+
 \int_{r_0}^r\left[
 \|\widehat{\mathcal E}\|_{\rm op}
 \sqrt{2E\big((A-\widehat A)^2+(B-\widehat B)^2\big)}
 +\|R_{\mathcal E}\|_F\right]\,dt,
 \tag{126.25}
$$
$$
 |F(r)-\widehat F(r)|
 \le |F(r_0)-\widehat F(r_0)|
 +\int_{r_0}^r\big[\sqrt E\,\|D\|_F+|R_F|\big]\,dt.
 \tag{126.26}
$$
完整角/参数 sup 可以直接放进这些式子的右端。

真实二阶 jet 可不微分数值位置地准确表示为
$$
 \begin{aligned}
 F_r&=\sqrt E\,e_1,& F_\theta&=ae_2,\\
 F_{rr}&=\frac{E'}{2\sqrt E}e_1+EA n,&
 F_{r\theta}&=a'e_2+a\sqrt E\,B n,\\
 F_{\theta\theta}&=-\frac{aa'}{\sqrt E}e_1+a^2C n.
 \end{aligned}
 \tag{126.27}
$$
因此真实曲率直接由对称矩阵 $(A,B;B,C)$ 的特征值控制。
若候选位置或框架未准确满足角兼容式，比较其**真实导数**时必须再加
$\widehat F_\theta-a\widehat e_2$、
$\widehat{\mathcal E}_\theta-\widehat{\mathcal E}N$ 及相应导数的残差；
不能把候选的代数 jet 当成其实际导数。
这些真实误差可进入 R123 的支撑、主曲率、握持和 reach 几何门。
R123 的 $(.001,.01,.7)$ 是一组充分档；实际曲率若更小，可以按其原公式
直接支付，不能仅因参考 Hessian 差超过 .7 就判定几何目标失败。

## 7. 本篇没有自动支付的内容

要使用 (126.23)，必须保存整个径向区间上的明确候选，并有向控制
初始无限角尾、全部真实残差及其角导数。两角网格相符、ODE 容差小、
有限谱顶端小、或单端点的值都不足以替代这些量。
只有在所有连续门真实通过之后，才可把指定宽度写为已证。

$K=0$ 处 (126.11)、(126.16) 退化；$C=0$ 处当前 Cauchy 图退化。
这两种情况需更换准确图或另证接续，不能把本定理越过它们。
即使一个较宽的精确腰环带已验证，正帽、尾端匹配、闭曲面单射及同一
度量的可见弯曲族仍是独立且尚未完成的要求。

准确代数的独立复核入口为 `scripts/fourfold_codazzi_exact_identities.py`；已实际运行15/15项符号恒等式检查，完整报告 `notes/2026-11-13-R126-exact-Codazzi-identities.json`。这些检查只核代数，不替代§5尚待实际计算的连续残差和屏障门。
