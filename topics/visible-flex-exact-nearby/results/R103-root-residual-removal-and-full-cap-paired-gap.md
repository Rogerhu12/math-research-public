# R103：根残差可去修正与完整正帽的成对 primal/dual gap

2026-11-12，independent-audit。

**状态：完整数学桥接已证明；从既有真实报告导出的根修正及 contact 数值已用准确有理数执行。**
本篇把同一个真实帽中的试函数和散度零通量直接配对。新增二阶项准确消去根残差，
同时保持原来的两槽 Cauchy 数据。所有角模、regular 均值及其通量、真实 Robin
形式都保留。可选的零总通量构造只增加一个明确的有限秩接线项；其根列并非有限
Fourier 多项式，全部高尾仍需携带。

本篇没有取得新的整宽领口积分值，也没有宣称已经验证完整反馈逆。
此前宽领口 pilot 未分配到 CI runner；没有将该次未运行记为数学结果。

## 1. 同一个 grounded form 和边界变量

实际对象为准确仿射族
$$
 \delta_5=-7789843107295549/4611686018427387904,\qquad
 |\delta-\delta_5|\le10^{-9}.
 \tag{103.1}
$$
它包含 R101 的最终参数，且包含于 R66/R69/R74/R96 已付外域参数集合。
每个参数使用自己的真实根 $t=t(\delta)$。置 $s=r-t$，
$0\le s\le L=25/8-t$。物理角仍为 $\theta\in\mathbb R/(2\pi\mathbb Z)$；
四重子空间的非零频率是 $4k$。

完整正帽形式是
$$
 \mathfrak b(v,v)=
 \int_0^L\int_0^{2\pi}(\nabla v)^*B\nabla v\,d\theta\,ds
 +\langle\Gamma v_L^\perp,v_L^\perp\rangle.
 \tag{103.2}
$$
$B=Y^2\widehat A$ 是原有真实 grounded 密度；外部包含同一个 body、
自然 graft 与 R74 的真正无限尾。$\Gamma$ 正自伴、在非零模上严格正，
$\Gamma e_0=0$，其中
$$
 e_0=(2\pi)^{-1/2},\quad P_0 f=\langle f,e_0\rangle e_0,\quad \Pi=I-P_0.
$$
本篇内积取第一变量线性。$\Gamma^{-1}$ 只用于非零模。

边界数据为 $g=(a,\xi)$，即 $v_0=a$、$\langle v_L,e_0\rangle=\xi$。
完整调和延拓记为 $u_g$，其 DN/regular 输出为
$$
 Sg=(-p_u(0),\,\langle p_u(L),e_0\rangle),\qquad
 p_u=(B\nabla u_g)_s.
 \tag{103.3}
$$
其余 regular 模服从真实 Robin 条件 $p_u^\perp+\Gamma u_L^\perp=0$。
这里没有在根或体内压缩方程。共同常数输入 $(e_0,1)$ 准确对应
$u=e_0$、通量零；在有限增广中应直接保留这个准确核方向。

在某个已付根领口 $0<s\le h$，写
$$
 B=\alpha
 \begin{pmatrix}1&b\\ b&b^2+s\kappa\end{pmatrix},
 \quad \alpha=B_{11}>0,\quad b=B_{12}/B_{11},\quad
 \kappa=\det B/(sB_{11}^2)>0.
 \tag{103.4}
$$
这只是同一个矩阵的准确分解。根处 $\alpha,b,\kappa$ 有相应的光滑极限。
下文的数值代入需要实际
$\alpha\ge a_*>0,\kappa\ge k_*>0,|b|\le Q$；局部存在性不能替代这些费用。

## 2. 消去根残差而保持两条真实 Cauchy 迹

先在同一有限 canonical 图中写
$$
 A=J^{-1}D\Psi B D\Psi^T,\quad
 C_*=\tau_*^2A,\quad
 P_*=-\operatorname{div}(C_*\nabla)+V_*,
 \quad
 V_*=-\frac{\tau_*}{J}\operatorname{div}(B\nabla\tau_*).
 \tag{103.5}
$$
$\tau_*>0$ 可以是 R96 的准确归一化 height，也可以是另行支付正性的
根匹配四次多项式 height。后者的 $E_{11}$ 不设为零。
准确换元为
$$
 -\operatorname{div}\!\left(B\nabla(\tau_*U\circ\Psi)\right)
       =\frac J{\tau_*}(P_*U)\circ\Psi.
 \tag{103.6}
$$

给定一个足阶试解 $U$，令 $R_0=(P_*U)|_{y=0}$。
取固定 $\eta(y)$，在根邻域等于1，且支撑于已付领口。
定义
$$
 \boxed{\quad
 \widetilde U
   =U+\eta(y)y^2\,\frac{R_0(\phi)}{2C_{*,11}(0,\phi)} .
 \quad}
 \tag{103.7}
$$
因为新增项及其全部一阶导数在根为零，
$$
 \widetilde U(0)=U(0),\quad
 (C_*\nabla\widetilde U)_y(0)=(C_*\nabla U)_y(0).
 \tag{103.8}
$$
而 $P_*(y^2a)|_0=-2C_{*,11}(0)a$，故
$$
 (P_*\widetilde U)(0)=0.
 \tag{103.9}
$$
(103.7) 的正号由所用的 $-\operatorname{div}$ 约定决定。
新增项经过同一 height、角图、Piola 密度后，物理值和物理 conormal
也都不变。R98 的共同正化 frame、其有限列、R99 的真实 Cauchy 矩阵及
所有根比较预算因此原样适用于新试解；这不是只保留主符号。

也可完全在物理坐标完成此步。若 $V$ 是 grounded 试函数，
$q=\operatorname{div}(B\nabla V)$，则
$$
 \widetilde V
   =V-\eta(s)s^2\,\frac{q(0,\theta)}{2B_{11}(0,\theta)}
 \tag{103.10}
$$
满足 $\widetilde V|_0=V|_0$、$(B\nabla\widetilde V)_s|_0=(B\nabla V)_s|_0$，
并有 $\operatorname{div}(B\nabla\widetilde V)|_0=0$。
它与(103.7)的符号一致，因为(103.6)带负散度。

对修正后的真实物理残差仍记为 $q$。在根的单个真实 scalar span 内，
$$
 q(s,\theta)=s\,q_1(s,\theta),\qquad
 q_1(s,\theta)=\int_0^1 q_s(us,\theta)\,du.
 \tag{103.11}
$$
这是准确的可去商，不对差分得到的近零数除以一个含零的区间。
若只给有限正则性，(103.11)需要相应的实际一阶残差；
本篇不由根值为零免费取得整个领口的 $q_1$ 上界。

## 3. 当前真实 canonical 试解的根残差预算

本节使用的根匹配 height 使 $C_{*,11}(0)=1$，并且
$E=C_*-\operatorname{diag}(1,y)$ 的根值及全部一阶根 jets 都准确为零。
四次根匹配还保持 $V_*(0)=-v_0$ 和 $(V_*)_y(0)=v_1$。
因此完整 $P_*$ 的根残差与 R53 正侧 canonical 表达准确相同；
没有将主矩阵导数项遗漏在(103.13)之外。

本节明确选取 R53 的 **canonical** 多项式
$$
 B_+(y,\phi)=-v_0(\phi)+y\,v_1(\phi)/3,\qquad
 C_+(y,\phi)=y^2(v_0)_\phi(\phi)/2.
$$
正侧势满足 $V_+(0)=-v_0$、$(V_+)_y(0)=v_1$。
对 $k\ne0$，$\lambda_k=4q|k|$、$\epsilon_k=\operatorname{sgn}k$，
$$
 U_k=c\lambda_k^{-1/3}e^{4iqk\phi}
 \left[(1+i\epsilon_k\lambda_k^{-1}C_+)
                   \operatorname{Ai}(y\lambda_k^{2/3})
      +\lambda_k^{-4/3}B_+\operatorname{Ai}'(y\lambda_k^{2/3})\right],
 \quad c=\sqrt{\frac{\operatorname{Ai}(0)}{-\operatorname{Ai}'(0)}}.
 \tag{103.12}
$$
用 R53 的准确残差式，或者直接微分并用
$\operatorname{Ai}''(0)=0,\operatorname{Ai}'''(0)=\operatorname{Ai}(0)$，
得到完整根行
$$
 \boxed{\quad
 R_0=-ic\operatorname{Ai}(0)\,
          M_{(v_0)_\phi}\operatorname{sgn}(D)\Gamma^{-4/3}
       +c\operatorname{Ai}'(0)\,M_{v_0^2}\Gamma^{-5/3}.
 \quad}
 \tag{103.13}
$$
所有乘法在左，输入频率乘子在右；没有把二者交换。
(103.13)包括其全部低输出、跨号和均值输出。

R87 为易算而选的物理 $s,\theta$ 多项式虽然有同一 value/first-normal，
一般有非零 $B_{yy}(0)$。用于那个旧试解时，(103.13)的第二乘法必须改为
$M_{v_0^2-B_{yy}(0)}$；或者直接使用(103.7)的完整 $R_0$。
本节数值不转授给遗漏该项的旧物理多项式。
输入均值、regular 输入和其它有限列均用其实际完整残差，不套用
非零频率的 Ai 消去式。

完整真实 v0 报告（含无限 Fourier 尾）已给
$$
 \sum_n|\widehat v_{0,n}|<5176,\qquad
 \sum_n|n|\,|\widehat v_{0,n}|<1186,\qquad q<10.
$$
所以 $\|(v_0)_\phi\|_\infty<47440$、$\|v_0^2\|_\infty<26790976$。
R96 已给 $\operatorname{Ai}(0)<9/25$、$-\operatorname{Ai}'(0)<13/50$。
另由
$$
 \Gamma(1/3)=\int_0^\infty t^{-2/3}e^{-t}dt<3+e^{-1}<4,\qquad
 3^{1/3}<3/2
$$
有 $-\operatorname{Ai}'(0)>1/6$，从而 $c<3/2$。因此
$$
 \|R_0P_{>K}\|_{L^2\to L^2}
 \le\frac{25617.6}{\Lambda_K^{4/3}}
       +\frac{10448480.64}{\Lambda_K^{5/3}},
 \quad \Lambda_K=4q_-(K+1).
 \tag{103.14}
$$
这是完整输出范数，不仅是某一列或高高块。

当前两种根匹配 height 都准确满足 $C_{*,11}(0)=1$。
程序从原始三份小型真实报告读取准确内容并核 SHA，执行12项准确有理
输入检查。取实际已付 $H=49/102400$，结果向外放宽如下：

| canonical 输入 $|k|>K$ | $\|R_0P_{>K}\|$ | $\sup_{0\le y\le H}\|\eta y^2R_0P_{>K}/2\|$ | 原 R98 正根算子 $A$ 下界 |
|---:|---:|---:|---:|
| 64 | 23.066786000 | $2.640884076\,10^{-6}$ | $118/125$ |
| 128 | 7.415308086 | $8.48968255\,10^{-7}$ | $123/125$ |
| 256 | 2.374943535 | $2.71903966\,10^{-7}$ | $249/250$ |

表中 $A$ 是 R98 的共同正化算子，和本篇坐标密度 $A$ 不同。
表的最后一列不是新近似正性判断：根两迹准确不变，所以既有严格正性直接保留。
这些数值只控制根修正及其指定幅度，不包含未付的整个 $q_1$ 或完整 gap。

## 4. 从一个完整试函数构造准确散度零通量

以下一律在整个物理圆柱 $(s,\theta)$ 上实施，避免把 canonical Fourier
投影误认成物理投影。设 $V$ 是完整 admissible 试函数，已经完成(103.10)。
写
$$
 B\nabla V=(p,z),\qquad q=p_s+z_\theta,\qquad
 p_0(s)=\langle p(s),e_0\rangle,\quad z_0(s)=\langle z(s),e_0\rangle.
$$
$\partial_\theta^{-1}\Pi$ 是物理角的准确零均值原函数；在四重子空间，其
乘子为 $(4ik)^{-1}$。置
$$
 m=p_0(0),\qquad
 j_s=\Pi p+m e_0,\qquad
 j_\theta=z_0(s)e_0-\partial_\theta^{-1}\Pi p_s.
 \tag{103.15}
$$
逐项微分给 $\operatorname{div}j=0$，且 $\langle j_s,e_0\rangle=m$ 沿全域为常数。
其与真实试函数通量的差准确为
$$
 d_s=(p_0(s)-m)e_0,\qquad
 d_\theta=\partial_\theta^{-1}\Pi q,\qquad d=B\nabla V-j.
 \tag{103.16}
$$
由(103.11)和平均散度恒等式，
$$
 p_0(s)-m=\int_0^s t\,\langle q_1(t),e_0\rangle\,dt=O(s^2),
 \qquad d_\theta=s\,\partial_\theta^{-1}\Pi q_1(s)=O(s).
 \tag{103.17}
$$
故 $j(0)=B\nabla V(0)$；完整根 conormal 也准确匹配。
这比仅在两个通量中取相同主项更强。

对(103.4)，精确有
$$
 d^*B^{-1}d
   =\alpha^{-1}\left(|d_s|^2+
                   \frac{|d_\theta-bd_s|^2}{s\kappa}\right).
 \tag{103.18}
$$
(103.17)使它在根可积。
如果没有先消根残差，通常 $d_\theta(0)\ne0$，
则第二项会出现不可积的 $1/s$；这就是(103.7)所修复的实际问题。

给出可直接计算的完整局部上界。若
$$
 |\langle q_1(s),e_0\rangle|\le A_1,\qquad
 \|\partial_\theta^{-1}\Pi q_1(s)\|_{L^2}\le B_1
 \quad(0\le s\le h),
$$
则由(103.17)、(103.18)积分得到
$$
 \boxed{
 \int_0^h\|B^{-1/2}d\|_2^2\,ds
 \le\frac1{a_*}\left[
 \frac{A_1^2h^5}{20}
 +\frac1{k_*}\left(
       \frac{B_1^2h^2}{2}
      +\frac{QA_1B_1h^3}{3}
      +\frac{Q^2A_1^2h^4}{16}
                  \right)\right].}
 \tag{103.19}
$$
对线性输入族，上述 $A_1,B_1$ 可直接取相应的算子范数。
完整无限 Fourier 系数必须一起估计，不能从逐列上界省略 lag 求和。

确切的原函数分频界是
$$
 \|\partial_\theta^{-1}\Pi q_1\|_2^2
   =\sum_{k\ne0}\frac{|(q_1)_k|^2}{16k^2}.
 \tag{103.20}
$$
只有实际输出 $|k|>N$ 的那部分才得到 $1/[4(N+1)]$；
低输入/高输入均可能产生低输出。径向上的低体模不是有限维边界槽，
没有在本篇被删掉。

在其它 true scalar spans 上按原分段取真实系数和试函数。
若试函数与通量的径向分量连续，通量的切向分量可有径向跳跃，
$\operatorname{div}j=0$ 仍在分布意义下成立。
所有端点与真无限尾须保留在下面的同一全域能量中。

## 5. 完整 primal/dual 平方恒等式与全部输出

定义
$$
 E(V)=\mathfrak b(V,V),\quad
 D(j)=\int_0^L\|B^{-1/2}j\|_2^2ds
       +\|\Gamma^{-1/2}j_s(L)^\perp\|_2^2,
$$
$$
 d_j=(-j_s(0),m),\qquad
 L(j,g)=\langle d_j,g\rangle .
$$
与 R88 同一分部积分给
$$
 \boxed{
 \mathcal R^2:=E(V)-2\operatorname{Re}L(j,g)+D(j)
 =\int_0^L\|B^{-1/2}(B\nabla V-j)\|_2^2ds
  +\|\Gamma^{1/2}V_L^\perp+
                         \Gamma^{-1/2}j_s(L)^\perp\|_2^2.}
 \tag{103.21}
$$
regular mean $m$ 与输入 $\xi$ 在 $L(j,g)$ 中，不能从平方范数里看不到
它们就把它们删去。所有非均值 Robin 误差也仍在最后一项。

令
$$
 \mathcal U_g=(B^{1/2}\nabla u_g,\Gamma^{1/2}u_{g,L}^\perp),\quad
 \mathcal J=(B^{-1/2}j,-\Gamma^{-1/2}j_s(L)^\perp).
$$
$e=V-u_g$ 的根迹与 regular 均值都为零。
调和最小化和 $\operatorname{div}j=0$ 分别给
$\langle\mathcal E,\mathcal U_g\rangle=0$、
$\langle\mathcal E,\mathcal J\rangle=0$，其中
$\mathcal E=(B^{1/2}\nabla e,\Gamma^{1/2}e_L^\perp)$。
所以还有准确正交分解
$$
 \boxed{\quad
 \mathcal R^2=\mathfrak b(e,e)+\|\mathcal U_g-\mathcal J\|^2.
 \quad}
 \tag{103.22}
$$
对任意完整调和测试 $u_h$，
$$
 \langle Sg-d_j,h\rangle
      =\langle\mathcal U_g-\mathcal J,\mathcal U_h\rangle.
 \tag{103.23}
$$
若已有完整 competitor 给
$\mathfrak b(u_h,u_h)\le E_{\mathcal X}\|h\|_{\mathcal X}^2$，
则
$$
 \boxed{\quad\|Sg-d_j\|_{\mathcal X^*}
       \le\sqrt{E_{\mathcal X}}\,\mathcal R.\quad}
 \tag{103.24}
$$
这里乘的是整个已付 gap 的平方根，不是一个未经配对的 PDE 残差。
它也不乘普通源的一般逆大常数。

对线性试函数族 $V_g$，记其能量形式为 $S_V$。同一个恒等式进一步给
$$
 0\le S_V-S\le G_{\rm gap},
 \quad
 \langle G_{\rm gap}g,g\rangle=\mathcal R_g^2.
 \tag{103.25}
$$
因而真实高高块与准确 trial 能量形式之间可以使用完整平方 gap，
不必先开平方。这需要实际计算该 trial 能量及其与目标模型的差；
(103.25)本身不会把 trial 根通量替换为某个尚未证明的自伴正常形。

## 6. 可选的零外通量构造及一个完整有限秩项

若只考虑 regular 输入为零的根试函数，并使 $V=0$ 于 $s\ge h$，
(103.15)在外区等于 $(me_0,0)$。直接使用它时，外部常通量能量
$\int_h^L m^2 e_0^2(B^{-1})_{11}$ 必须支付。
下面给出一个可消去此外区费用、但不删除 mean 接线的准确替代。

令 $b_0(\theta)=b(0,\theta)$。取 $\chi_0=1$ 于根邻域、$\chi_0=0$ 于 $s\ge h$。
定义真实散度零单位通量
$$
 J^0_s=e_0\,[1-s\chi_0 b_0'],\qquad
 J^0_\theta=e_0 b_0(\chi_0+s\chi_0').
 \tag{103.26}
$$
确有 $\partial_sJ_s^0+\partial_\theta J_\theta^0=0$，
$\langle J_s^0,e_0\rangle=1$，根处
$J^0=(e_0,b_0e_0)$ 位于真实退化矩阵的非退化方向，
外区则为 $(e_0,0)$。因此其根附近的逆能量有限。

例如设 $|b_0|\le Q_0$、$|b_0'|\le Q_1$、
$|(b-b_0)/s|\le Q_s$、$|\chi_0'|\le L_\chi$、$0\le\chi_0\le1$。
从(103.18)直接得到
$$
 E_{J^0,h}\le\frac1{a_*}\left[
       h(1+hQ_1)^2+
       \frac{h^2}{2k_*}
           (2Q_0L_\chi+Q_s+QQ_1)^2\right].
 \tag{103.27}
$$
这里使用 $|\chi_0-1|\le sL_\chi$；没有在根积分一个裸 $1/s$。

置
$$
 j^{\,c}=j-mJ^0.
 \tag{103.28}
$$
它准确散度零、在 $s\ge h$ 为零，且与 $V$ 一起使真实 regular Robin
平方项准确为零。全 gap 因而只在同一领口积分。
根 DN 候选与原候选的差是
$$
 \boxed{\quad d_{j^c}-d_j=m(e_0,-1).\quad}
 \tag{103.29}
$$
这是一个秩至多一的真实边界项，包含 regular 行；它对共同常数输入的
测试为零。$m$ 是实际试函数根通量的完整线性泛函，不能强行设置为零。

在 canonical 根空间中，该输出列是
$(T_0^*e_0,-1)$，其中
$$
 T_0^*e_0=
 \left[\frac{\tau_0}{Y_0'}e_0\right]\circ Y_0^{-1}.
 \tag{103.30}
$$
它一般含全部 canonical Fourier 模。R92/R97/R99 的真实角图、height
及全尾接口应完整作用到它，而不是把它当成一个纯 canonical 零模。
同样，$m$ 的所有高输入系数都须保留。

局部 gap 可用
$$
 \mathcal R_c\le
 \left(\int_0^h\|B^{-1/2}(B\nabla V-j)\|_2^2ds\right)^{1/2}
       +|m|\sqrt{E_{J^0,h}}
 \tag{103.31}
$$
控制，也可直接计算其准确交叉项以收紧。
这没有把 mean 的能量删除，而是把它改成可实际支付的局部能量与有限秩接线。
regular 输入、原始根有限列可另选完整 admissible primal/dual 对并相加。
共同常数方向直接选 $V=e_0,j=0$，其 gap 准确为零。

## 7. 由既有实际报告立即得到的 gap/contact 常数

使用 R96 的根变换 $a_{\rm ph}=T_0a$，
$\mathcal X=H^{1/3}_\phi\oplus\mathbb C_\xi$。
已有完整帽 competitor 能量为
$$
 E_{\rm all}<2128.565112,\qquad E_{\rm reg}<50.912957.
$$
对于只含 canonical $|k|>N$ 的根测试，R96 给 $E_N$。
这些只是入口测试的限制，帽内解仍未压缩。
由能量的 Cauchy--Schwarz，
(103.24)在全部根及 regular 上取 $\sqrt{E_{\rm all}+E_{\rm reg}}$；
只取高根与 regular 上取 $\sqrt{E_N+E_{\rm reg}}$；
只取高根上取 $\sqrt{E_N}$。

### 测度与 Fourier 基的逐项归一

R96 §1 使用物理 $d\theta$ 与 $e_0=(2\pi)^{-1/2}$，§2 使用
canonical $d\phi$ 与正交归一基 $\ell^{-1/2}e^{iqj\phi}$，
$\ell=2\pi/q$；四重指标为 $j=4k$。
其 $E_{\rm all},E_N$ 是在真实 $dy\,d\phi$ 中对完整 ramp 按 Parseval
积分得到的，$q$ 已进入 $\lambda=4q|k|$。
其中 $dy\,d\phi=J\,ds\,d\theta$，height 的变换也同时携带；
所以这些能量不需要再乘一个圆长或 $q$。

$E_{\rm reg}$ 来自 R94 (94.9) 的 $M_g/L_-$。
具体竞争函数为 $v(s,\theta)=\xi(s/L)e_0(\theta)$；
在同一已付 shear 密度中它仍与角无关，其能量上界为
$|\xi|^2(M_g/L)\int_0^{2\pi}|e_0|^2d\theta
=|\xi|^2M_g/L$。真实 tail 的常数 form 槽为零。
原完整报告的 $M_g<146.965498$、$L_->2.886603124879$ 与
$E_{\rm reg}<50.912957$ 相容。

若使用平均角 Fourier 系数作计算坐标，准确转换分别是
$
 a_k^{\rm ph}=\sqrt{2\pi}\,\widehat a_k^{\rm ph},\qquad
 a_k^{\rm can}=\sqrt{\ell}\,\widehat a_k^{\rm can},\qquad
 \xi=\sqrt{2\pi}\,\widehat\xi.
$
因此 $T_0$ 在两个正交归一基中的矩阵，等于
$\sqrt{2\pi/\ell}=\sqrt q$ 乘以其在平均角基中的矩阵；
dual 按相应共轭转置变换。
不能一边把 $\xi$ 留作未归一化常数值、一边引用本表。
本篇直接使用真实函数 $T_0$ 和上述两个正交基，故已包含该因子。
R98/R99 的 Wiener 乘法界与指数的 Fourier 系数不随这一共同基归一改变。

准确有理数加法和整数平方根给以下向外界：

| 输出测试范围 | 根输出 contact | 同时保 regular 通量 |
|---|---:|---:|
| 全部 canonical 根频率 | 46.136375145 | 46.684880503 |
| $|k|>64$ | 3.660640937 | 8.019554107 |
| $|k|>128$ | 2.899616214 | 7.701995209 |
| $|k|>256$ | 2.299322829 | 7.496655353 |
| $|k|>65536$ | 1.041980286 | 7.211010950 |

regular 单行费用小于 $7.135331528$。
表中所有值乘的是 **完整** $\mathcal R$。
不能把(103.19)一个局部小块单独填进(103.24)，除非其余 body、外尾和
Robin 项已经实际为零或已另行包围。方案(103.28)的支撑及有限秩修正
同时保留时，外区为零是精确构造事实；仍须支付整个局部 gap。

## 8. 与真实 paired 源、height 和强窗口的接线

对任意 $C_*=C_0+E$，包括 $E_{11}\ne0$，准确有
$$
 P_*(\chi U)=
   \underbrace{\chi P_0U-\chi'U_y}_{f}
  -\operatorname{div}
       \underbrace{\left(\chi E\nabla U+\chi'UC_*e_y\right)}_{F},
 \quad P_0=-\partial_y^2-y\partial_\phi^2+V_*.
 \tag{103.32}
$$
新增 normal flux $E_{11}U_y$ 包含在 $F$ 中；
$\|C_*^{-1/2}\chi'UC_*e_y\|=|\chi'U|\sqrt{C_{*,11}}$。
R96 的物理换元
$$
 F_{\rm ph}=\frac J{\tau_*}D\Psi^{-1}F,\qquad
 f_{\rm ph}=\frac J{\tau_*}(f-\nabla\log\tau_*\cdot F)
 \tag{103.33}
$$
使两部分对同一个 test 的 height 项准确相消。
本篇实际 stream 构造使用 **整个**
$\operatorname{div}(B\nabla V)$，不单独忽略(103.32)中的某个大项。

选 compact primal/dual 后，$\chi',\chi''$ 的真实费用仍进入 $q_1$ 和完整
平方 gap；本篇没有证明这些费用已经数值变小。
若改用不截断的试解，则外端 Cauchy 匹配、R96 的外端 Wronskian、
regular cross 与 affine source 必须付入(103.21)或相应的真实接合，
不能因 Ai 衰减而免费去掉。

若给定非齐次 grounded 方程 $\operatorname{div}(B\nabla u)=f_{\rm src}$，
可选真实 particular flux $\operatorname{div}j=f_{\rm src}$。
把 $E(V)$ 换成 $E(V)+2\operatorname{Re}\int f_{\rm src}\overline V$ 后，
(103.21)的平方右端不变。
具体地，令
$$
 m(s)=m(0)+\int_0^s\langle f_{\rm src}(t),e_0\rangle dt,\qquad
 j_s=\Pi p+m(s)e_0,\quad
 j_\theta=z_0e_0-\partial_\theta^{-1}\Pi(p_s-f_{\rm src}).
$$
则差量公式使用 $q-f_{\rm src}$，两端均值满足正确的源守恒。
源没有足够根迹时不能直接套(103.7)；所需 particular flux 的完整
能量和源空间必须另付。这一仿射恒等式不替代尚未完成的全普通源右逆。

对强角窗口可接
[core-strong-weak-residual-contract §7](../notes/2026-11-12-core-strong-weak-residual-contract.md)
的完整 equilibrated 投影公式。但在根的物理坐标中，
$\|B^{-1/2}B_\theta B^{-1/2}\|$ 可因变化的退化方向而无界。
因此该文在普通切口的实际常数不能免费转授到根。
应在已拉直、已付实际角导数的 canonical grounded form 中建立相应窗口，
或明确支付协变角导数及其交换项。
本篇的 $L^2$ energy-gap/contact 不依赖该未付强窗口。

## 9. 原始真实输入、准确执行与下一计算量

源：

    scripts/fourfold_phase_root_completion_gap_budget.mjs

实际准确有理数结果：

    notes/2026-11-12-R103-root-completion-gap-budget.json

输入原件及 SHA256：

| 原始小报告 | SHA256 |
|---|---|
| ci-canonical-v0-scaled-Wiener-summary.json | 66112956b245389aa38c3d07244685ad31c29f7aae0575b8986bf80b54459ce8 |
| actual-common-root-high-remainder.json | e727251cd6c187ded5782aff3a03401301d21b83fd03d419f31f716862be6253 |
| ci-direct-canonical-source-summary.json | 826bda30e5d42bf47efc4fb5daa3bf6da1361bb2f4ee737486f89be9c597ca09 |

三件均位于本课题 notes/。原完整大报告由对应既有 manifest 绑定。
本次实际读取了这些小原件，逐字节 SHA 检查后，在 functions.exec 的
JavaScript BigInt 环境执行与源码相同的纯准确算术核心；
完整 Node 文件入口尚未运行。该区别保存在结果 execution 字段中。

重放：

~~~sh
node scripts/fourfold_phase_root_completion_gap_budget.mjs
~~~

下一实际计算需支付同一个修正 trial 的完整 $q_1$、可选 $J^0$ 局部能量、
截断区全部交叉项，以及真实 frame 到完整反馈的接线。
已保存宽领口 correlated-germ/polynomial-height 源可用于这些系数，但
尚未运行的新 source 不构成当前数值输入。
本篇先关闭根处不可积缺陷和 mean/外端接线中的数学缺口，
保留真正剩余的整域 gap、有效高切、全低高 Schur 及非线性零解任务。
