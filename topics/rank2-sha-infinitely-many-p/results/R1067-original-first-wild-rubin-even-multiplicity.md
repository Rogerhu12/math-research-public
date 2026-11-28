# R1067 — 原第一 wild Rubin 零点的偶重数

日期：2026-11-28。会话：Astra-rank2-Sha-0b097461-20261127。

**状态：本篇证明同一个原整 Rubin 系数在第一 wild 角色处的零点重数必为偶数，并将该重数精确写成原完整 Miller–Hall 权 germ 的零阶。特别，若原第一 wild Hall 值确实等于零，则原 cyclotomic 因子至少出现两次。没有由原中央坏条件、高赋值、Katz 整性或单字非零推出 Hall 等于零或不等于零；尚未证明主目标的无穷素数非消失。**

所有对象沿用 [R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)、
[R716](R716-original-wild-global-theta-period-and-exact-central-l-value.md) 的原曲线、原整基和原第一 wild 角色。新的输入是把
[R1062](R1062-original-translated-miller-jets-and-critical-weight-germs.md)、
[R1066](R1066-original-katz-negative-weight-and-full-gaussian-return.md)
的完整 translated-jet 权 germ 用于同一有限野角色的混合权比较。这里不使用已降级的 literal-usual / flat cross，也不把旧中央 Newton 变量平移到一个未识别的函数。

## 1. 固定对象与结论

固定
\[
 E_{17}:y^2=x^3+17,\qquad E_1:y^2=x^3+1,\qquad
 K=\mathbf Q(\omega),\quad \delta=1+2\omega,
\]
以及
\[
 p>211,\quad p\equiv5\pmod6,\quad
 d=p+1,\quad \Delta=p^2-1,\quad
 L=K_p=\mathbf Q_{p^2},\quad\mathcal O=\mathbf Z_{p^2},
 \qquad v_p(p)=1.                                      \tag{1}
\]
原整类身份是
\[
 F_\vartheta^*\xi_{17}
   =\mathcal A_p(T)\xi_1,\qquad
 \vartheta=17^{1/6}\in\mathcal O^\times,\qquad
 \mathcal A_p\in\mathcal O[[T]]\setminus\{0\}.
                                                               \tag{2}
\]
其中 \(\xi_1\) 是原完整 signed 整模的基。按原生成元 \(\gamma\)，
\(T=\gamma-1\)，令
\[
 q_{\rm ac}=\kappa_{\rm ac}(\gamma)\in1+p\mathcal O,\qquad
 v_p(\log q_{\rm ac})=1.
                                                               \tag{3}
\]
R303 与原第一 wild 注已付
\[
 \mu(\mathcal A_p)=0,\qquad
 \operatorname{ord}_{T=0}\mathcal A_p
       =2e,\qquad e=\operatorname{ord}_{u=0}J_p\ge1.       \tag{4}
\]
式(4)使用原 \(J_p\)，没有先除去其 forced \(u\)。

对 \(r\in\mathbf F_p^\times\)，固定 R716 的
\[
 \chi_r(v)=e_p\!\left(
 \operatorname{Tr}_{\mathbf F_{p^2}/\mathbf F_p}
 \frac{34r}{2\delta}\frac{v^p/\bar v-1}{p}\right),
 \qquad
 \nu_r=\widetilde\eta_{p,r},\quad \nu_{r,p}=\chi_r^2.
                                                               \tag{5}
\]
\(\chi_r\) 在 Teichmüller 单位、\(\mathbf Z_p^\times\) 和 \(\mu_6\)
上平凡。它和 \(\nu_r\) 均有阶 \(p\)、导子 \(p^2\)。
记
\[
 t_r=\nu_r(\gamma)-1.
                                                               \tag{6}
\]
若采用逆 Artin 规范，同时将 \(\nu_r,q_{\rm ac}\) 取逆；
下面结论在此同一整参数自同构下不变。

**定理。** 下文从两条完整原来源构造有限扩域 \(F/L\) 上的解析 germ
\(\mathcal H_{34,r}(t)\)、\(\mathcal H_{2,17r}(t)\)，满足
\[
 \mathcal H_{2,17r}(0)\in\mathcal O_F^\times,\qquad
 \mathcal H_{34,r}\not\equiv0,
 \qquad
 \boxed{\operatorname{ord}_{T=t_r}\mathcal A_p(T)
       =2\operatorname{ord}_{t=0}\mathcal H_{34,r}(t).}
                                                               \tag{7}
\]
其常数项是原实际 Hall 和乘 \(d^{-1/2}\)，没有换源或删除中心相位。

因此，若原 Hall 值 \(\mathcal T_{34,T_r}\) **精确为零**，则
\[
 \boxed{
 \Phi_p(1+T)^2\mid\mathcal A_p(T),\qquad
 \lambda_p\ge 2e+2(p-1),
 }\quad
 \lambda_p=\min\{i:[T^i]\mathcal A_p\in\mathcal O^\times\}. \tag{8}
\]
更精确，若右端 Hall germ 的零阶为 \(f_r\)，则
\[
 T^{2e}\Phi_p(1+T)^{\,2f_r}\mid\mathcal A_p(T),\qquad
 \lambda_p\ge 2e+2f_r(p-1).                              \tag{9}
\]
特别
\[
 J_p'(0)=0,\quad \mathcal T_{34,T_r}=0
 \quad\Longrightarrow\quad \lambda_p\ge2p+2.             \tag{10}
\]
这加强的是两个真实条件的共同后果。第一个条件本身只给
\(T^4\mid\mathcal A_p\)，不提供第二个条件。

## 2. 同一个野角色的两个完整 theta 来源

以 \(N\) 标记线丛次数而非曲线参数。取
\[
 (N,E_N,F_N,r_N)=
 \begin{cases}
 (34,E_{17},S_{17},r),\\
 (2,E_1,\Theta_2,17r),
 \end{cases}
 \qquad \Theta_2=x\sigma^2,\quad \Theta_2(0)=1.           \tag{11}
\]
\(S_{17}\) 是 R297/R298 的完整原多项式来源，首项 \(z^6\)；
\(\Theta_2\) 是 R302 的实际 rank-zero 来源。两者均在各自
Néron 微分 \(dz=dx/(2y)\) 下读取，不把两条实周期设为相同。

写 \(v=x+y\omega\)，令
\[
 h_N(v)=\left(\frac{x+y}{3},\frac{3N}{2}(x-y)\right),
 \qquad
 e^{(N)}_v=\rho_p(-h_N(v/p))\,\mathbf1_{\mathbf Z_p}.      \tag{12}
\]
其矩阵行列式为 \(-N\)，是当前 \(p\) 处单位。
原 Heisenberg 规范仍是
\[
 (\rho(t,\xi)f)(x)
   =\psi_{\rm add}\bigl(\xi(x+t/2)\bigr)f(x+t).
\]
故 \(v\bmod p\) 的 \(p^2\) 个 \(e^{(N)}_v\) 是范数一正交基，且
\[
 e^{(N)}_{v+p\ell}
   =e_p\!\left(\frac N2[\ell,v]\right)e^{(N)}_v,\qquad
 [\ell,v]=\frac{\bar\ell v-\bar v\ell}{\delta}.            \tag{13}
\]
在 \(N(v)=r_N\) 上，原代表变更字符相位恰为(13)的逆。
这里
\[
 2r_2=2(17r)=34r
\]
使 degree 2 的字符与(5)完全相同；没有另选 wild 字符。

于是两条实际 \(p\)-向量为
\[
 \varphi_{N,r_N}
  =\frac1{\sqrt d}\sum_{\substack{v\bmod p\\N(v)=r_N}}
            \chi_r(v)e^{(N)}_v,
 \qquad
 \|\varphi_{N,r_N}\|=1,\qquad
 \rho_{N,\chi_m}(g)\varphi_{N,r_N}
             =\chi_r(g)^{-1}\varphi_{N,r_N}.             \tag{14}
\]
正根 \(\sqrt d\) 只规范 Hermitian 范数；它在当前 \(p\) 处是单位。
真实 Hecke twist 仍是 \(\nu_r=\chi_r^2\)，不将(14)的本征字符误当
Hecke twist。

在 \(p\) 外，degree 34 保持 R290/R716 的全部 \(2,3,17\)
Schwartz 向量；degree 2 保持 R302 的 \(2,3\) 向量、原 Hermitian
类 \(\alpha=1\) 和其余地点的标准球。对(12)的有理位移：

- \(3\) 处平移在 \(3^{-1}\mathbf Z_3\)、调制在 \(3\mathbf Z_3\)；
- \(2\) 处平移和调制同奇偶，原四陪集向量逐项恢复；
- degree 34 的 \(17\) 处调制在 \(17\mathbf Z_{17}\)；
- degree 2 的 \(17\) 处为完整原标准球，平移和调制均整。

半中心在这些检查中一并保留。因而有理 Heisenberg 位移从
无穷处移到 \(p\) 处时，没有新增非 \(p\) 测试向量。

对每个 \(m\ge0,\ 6\mid m\)，以原第 \(m\) Hermite 向量替换无穷
Gaussian。原 \(2,3,17\) splitting 的公共周期正是 \(6\)，而
\(p\) 处未分歧 splitting 的均匀元值仍为 \(-1\)。
所以(14)适用于
\(\psi_{17}^{2m+1}\nu_r\) 及 \(\psi_1^{2m+1}\nu_r\)。
全局环面字符在非 \(p\) 紧子群和无穷处平凡，在好分裂处仍可能
有未分歧值；与 R716 一样保留这些值。类数一及 \(\mu_6\)
兼容给出的紧商体积仍为原来的 \(6\)。

## 3. 完整 Miller 导数、实性和两条全权平方

令 \(\varpi_N=(1-\omega)^{-1}\Omega_N\)，其中 \(\Omega_N>0\)
是相应曲线的 primitive 实周期。对
\(Q_v=\varpi_Nv/p\)，在原 sigma frame 置
\[
 {\mathscr F}_{N,Q_v}(z)
  =\exp[-N\eta_{Q_v}(z+Q_v/2)]\,F_N(z+Q_v),
\]
\[
 {\mathscr D}_{N,r_N,m}
  =\sum_{N(v)=r_N}
         \chi_r(v)\,D_z^m{\mathscr F}_{N,Q_v}(0),\qquad
 s_{N,r_N,m}=\frac{{\mathscr D}_{N,r_N,m}}{m!}.           \tag{15}
\]
这里 \(\eta_Q\) 是原 quasi-period 的实线性延拓。
\({\mathscr F}_{N,Q}(0)\) 正是原 Klein–Miller 值，不只保留其
有理函数部分。更换 \(v\) 的整数代表时，
\({\mathscr F}_{N,Q}\) 乘一个与 \(z\) 无关的真实 Heisenberg
相位；(13)和 \(\chi_r\) 的逆相位逐项抵消。
因此(15)连同全部导数与代表选择无关。

两曲线为原实模型，故
\[
 \overline{{\mathscr F}_{N,Q}^{(m)}(0)}
    ={\mathscr F}_{N,\bar Q}^{(m)}(0),\qquad
 \bar Q_v=Q_{-\omega\bar v},\qquad
 \chi_r(-\omega\bar v)=\overline{\chi_r(v)}.              \tag{16}
\]
范数纤维在 \(v\mapsto-\omega\bar v\) 下保持。
故完整的 \({\mathscr D}_{N,r_N,m}\) 为实数。
若另以 CM 周期归一，\(\bar\varpi_N/\varpi_N=-\omega\)；
在本篇 \(6\mid m\) 的实际权上其 \(m\) 次幂仍为1。
这里的实性针对(15)的完整 word，不针对剥去中心后的任意版本。

为显示两个阶乘的准确位置，原 Hermite 参数为
\[
 h_N^2=-\frac{\sqrt3}{24N\pi^2},\qquad
 h_{34}=\frac{\sqrt{51\sqrt3}}{204\pi i},\quad
 h_2=\frac{\sqrt{3\sqrt3}}{12\pi i}.
\]
把 R290/R302 的完整 coherent generating identity 代入有理
Heisenberg 位移，得到第 \(m\) Hermite theta-null
\[
 b_{N,r_N,m}
   =\frac{C_N}{\sqrt d}(\Omega_Nh_N)^m
                   {\mathscr D}_{N,r_N,m}.             \tag{17}
\]
这是对同一个生成函数取 \(m\) 次导数；不是删除 \(m!\) 的
Taylor 系数。\(C_N\) 是原未扭转来源的固定实常数。
当 \(m=0,N=34\) 时，(17)正是 R716(31)。

新增的坏非分裂地点 \(p\) 将 Yang 的 \(c(0)\) 乘
\((1+p^{-1})^{-1}\)。原 \(p\)-向量范数为1，完整 Hermite 范数
仍含 \(m!/(4\pi)^m\)。因此
\[
 L(\psi_j^{2m+1}\nu_r,m+1)
   =C_j^{(0)}(1+p^{-1})
       \frac{(4\pi)^m}{m!}\,b_{N,r_N,m}^{\,2},
                                                               \tag{18}
\]
其中 \(j=17,1\) 分别对应 \(N=34,2\)。
这使用 Yang 的真实良好向量公式；非零向量不被替换为非零
theta-null，右边允许为零。

定义
\[
 {\mathscr E}_{j,\nu_r,m}
 =\frac{(2\pi/\sqrt3)^m L(\psi_j^{2m+1}\nu_r,m+1)}
        {m!\varpi_j^{2m+1}}.
\]
由原常数
\(C_{17}^{(0)}C_{34}^2/\Omega_{17}=\kappa_0=48940416\)、
\(C_1^{(0)}C_2^2/\Omega_1=1/6\)，以及
\[
 (1+p^{-1})/d=p^{-1},\qquad
 (1-\omega)^2=-3\omega,\qquad\omega^m=1,
\]
(17)–(18)化为
\[
 \boxed{\begin{aligned}
 {\mathscr E}_{17,\nu_r,m}
   &=\frac{\kappa_0(1-\omega)}p\,34^{-m}
                               s_{34,r,m}^{\,2},\\
 {\mathscr E}_{1,\nu_r,m}
   &=\frac{1-\omega}{6p}\,2^{-m}
                               s_{2,17r,m}^{\,2}.
 \end{aligned}}                                             \tag{19}
\]
所以两个 \(m!\) 及新增的 \(p^{-1}\) 都已明确出现。后文只在
两式取比时取消它们，不分别称其为单位。

## 4. 同一有限 \(\nu_r\) 的混合权整类比较

下面的比较对 \(m>0,\ d\mid m\) 进行；这些权自动满足 \(6\mid m\)。
设参考值非零。我们证明
\[
 \boxed{
 v_p\mathcal A_p(\nu_r(\gamma)q_{\rm ac}^m-1)
   =v_p{\mathscr E}_{17,\nu_r,m}
        -v_p{\mathscr E}_{1,\nu_r,m}.}
                                                               \tag{20}
\]
这是原 R303(18)的同一类构造在**固定有限 Artin 线**
\(\nu_r^{-1}\) 上的比较，以下支付这条新增线，而非直接将旧式
加一个字符后援引。

### 4.1 实际的两条 tensor 路径

从各自的完整 ray-class 椭圆单位系统 \(\mathbf u_j\) 出发，
固定 \(\nu_r^{-1}\) 的同一个 Betti/étale 基 \(e_{\nu^{-1}}\)。
先在(2)的反圆分变量作 \(\nu_r\chi_m\) 特化，或先取
\(2m+1\) 次 CM tensor、同时 tensor \(e_{\nu^{-1}}\)，再作中央
cyclotomic 特化，所得表示和向量分别为
\[
 T_j^{-(2m+1)}(m+1)\otimes\nu_r^{-1},
\quad
 \mathbf u_j\otimes b_j^{\otimes(2m+1)}
       \otimes e_{\nu^{-1}}\otimes\zeta^{\otimes m}.
                                                               \tag{21}
\]
相等的原因仍是
\(\chi_m^{-1}=\psi_j^{-2m}\chi_{\rm cyc}^{m}\)，现在两边同时多出
同一有限 tensor。norm、特化、tensor、局部化与 dual exponential
对这一等式自然相容。辅助惰性素数仍可取
\(\ell\equiv1\bmod p\)、\(\ell\nmid6\cdot17p\)。
因有限反圆分 \(\nu_r((\ell))=1\)，原辅助因子仍是共同单位
\(\ell^2+\ell^{-1}\equiv2\bmod p\)。

在 Kato 的负型约定中，(21)使用
\(\psi_j^{-(2m+1)}\nu_r^{-1}\)，型为 \((-(2m+1),0)\)。
Kato §15.8 的构造适用于任意这样的 Hecke 角色和每个有限
\(p\)-adic place；其 §15.9 允许模数含 \(p\)，并对任意有限
ray-class 扩张及有限字符给 period/dual-exponential 公式。
这里用 \(D_{\rm dR}\)，不声称分歧 Artin tensor 是 crystalline。

Lemma 15.11 的两张定义性图及已证 (15.16.1) 把(21)送到具有
相应 Betti 标签的 Kato 类。Theorem 12.5(1)取
\(k=2m+2,\ r_{\rm crit}=m+1\)，再拉回同一 CM–Artin 线。
中间任意 \(S(\psi)\simeq S(f)\) 缩放在两图和标签中同时出现而
抵消。没有使用 Kato §15.11 末未证明的高权 motivic 相容性。

### 4.2 分歧公共因子与真正不同的整费用

取共同 CM-pair 模数 \(\mathfrak f=(34\delta p^2)\)，它作为理想
同时包含于两条角色各自的导子理想。在 Kato §15.9 的原
\(\mathbf C/\mathfrak f\) 模型中，若 \(\beta\) 是由 \(1\in K\)
给出的有理 Betti 向量，则 \(p^2\beta\) 是当前局部 CM Tate 格的
基（固定非 \(p\) 单位因子可随基同保）。因此 \(2m+1\) 次 tensor
在这两种基间有共同因子 \(p^{-2(2m+1)}\)，不能称为单位；它在
两条来源中先保留再抵消。两条原模型间仍是 R303(9)的整同构
\(F_\vartheta\)。若用 finite-character projector，保留
\[
 e_{\nu^{-1}}
   =\frac1p\sum_{\sigma\in\Gamma/\Gamma^p}
                        \nu_r(\sigma)\sigma .
                                                               \tag{22}
\]
本篇不把(22)叫作整投影。亦保留同一 Artin de Rham period：
若所选有限线的 period 为 \(g_{\nu}\ne0\)，两条 tensor period
都是 \(\varpi_j^{2m+1}g_\nu\)。用 Gauss 和表达该 period 时，
Gauss、导子 \(p^2\) 的归一和任何 \(p\) 幂均保持原样。
它们在两条路线中逐项相同，先取比再消去。

完整费用如下：

| 项目 | 两条来源的实际比较 |
|---|---|
| CM tensor 与微分 | \(F_\vartheta^*\omega_{17}^{\otimes(2m+1)}
 =\vartheta^{-(2m+1)}\omega_1^{\otimes(2m+1)}\)，为单位 |
| 新有限 Artin tensor | 同一个 \(e_{\nu^{-1}}\)、\(g_\nu\) 及(22)，保留后相消 |
| 含 \(p^2\) 的共同 CM-pair 运输 | 同一 \(p\)-部分同源和同一秩一 tensor，不丢非单位度数 |
| 临界 Tate/Gamma | 同一个 \(\delta^m m!\)，可非单位，取比后相消 |
| \(p\) Euler | \(\nu_r\) 分歧，两个本地 \(L\)-因子均为1，不沿用旧 \(1+1/p\) |
| 辅助 smoothing | 原共同 \(\ell^2+\ell^{-1}\)，为单位 |
| 固定非 \(p\) 下降 | 原 \(2,3,17\) 有限字及下降度，均为当前位单位 |

两条局部 CM 角色在 \(p\) 本来相同：
\(\psi_1((p))=\psi_{17}((p))=-p\)。
所以含 \(\nu_r\) 的局部 Gauss/period 比较也没有隐藏的不同
未分歧参数。参考在 \(17\) 处保留 primitive Euler 因子。
若为书写共同模数而暂时删掉该因子，它在当前中央权准确为
\(1+1/17=18/17\)，因为 \(\nu_r\) 的整个 \(17\) 分量平凡；
该实际单位必须乘回。

对(2)施(21)与同一个 dual exponential，上述两张图给出两侧
临界 \(L\) 值。所有非公共比较都是列明的整单位；所有可能
非单位的新增 Artin、导子和 Gamma 因子已在比值中共同消去。
这证明(20)。这个证明只给逐权准确赋值，**不需要**剩余单位
随 \(m\) 解析。参考非零时的取比才被使用。

将(19)代入(20)，得
\[
 \boxed{
 v_p\mathcal A_p(\nu_r(\gamma)q_{\rm ac}^m-1)
  =2v_p{\mathscr D}_{34,r,m}
       -2v_p{\mathscr D}_{2,17r,m}.
 }                                                          \tag{23}
\]
其中 \(17^m,6\kappa_0\) 是单位，而两份 \(m!\) 和两份
\(p^{-1}\) 已准确相消。

## 5. 真正的 Hall 权 germ 与参考单位

在每条模型的原不变微分下，R1062 的 complete translated-jet
恒等式写成
\[
 D_z^m{\mathscr F}_{N,Q}(0)
   = B_{N,Q}(NZ_Q)^m\mathcal F_{N,Q}(m),
 \quad
 \mathcal F_{N,Q}\in1+\mathfrak m_F\langle t\rangle,
 \quad \mathcal F_{N,Q}(0)=1.                            \tag{24}
\]
所有中心和实际 \(Z_Q\) 留在 \(B_{N,Q},Z_Q\) 中。
N=2 时同一证明直接适用：\(x\) 在 \(O\) 的极阶为2，\(p\nmid2\)，
去掉 \(e^{2Z_Qz}\) 后的 logarithmic derivative/Bell 估计仍给
第 \(k\) 个正规化项至少
\(k(1-1/(p-1))\) 的估值。没有在此使用 mass-zero 条件。
固定有限全部除点后，可取同一个有限域 \(F\) 包含这些系数。

式(24)是 **physical \(z\)** 的导数。如果先在实际 \([p]\)-cover
使用 R1066(N11)，右边多 \(p^m\)，必须乘回 physical \(p^{-m}\)。
本篇在(15)、(17)、(24)始终已经作了这个返回。

对每个 \(N\) 取一个实际非零点 \(Q_{N,*}\)，设
\(A_{N,*}=NZ_{Q_{N,*}}\)。
R1063(L3) 对同一实际 zeta 连接给
\[
 v_p(NZ_Q)=\frac p{\Delta}-1
\]
与 \(Q,N\) 无关。因此 \((NZ_Q)/A_{N,*}\) 都是单位。
选一个正整数
\[
 M=\Delta e_1p^a,\qquad p\nmid e_1,
\]
使所有这些有限单位的 \(M\) 次幂落在指数收敛盘；
也同时固定已列有限相位。\(M\) 是一个固定的合法权步长，
不随下面趋近序列另行改变。定义
\[
 \mathcal H_{N,r_N}(t)
 =\frac1{\sqrt d}\sum_{N(v)=r_N}
 \chi_r(v)B_{N,Q_v}
 \exp\!\left(t\log
       \left[\left(\frac{NZ_{Q_v}}{A_{N,*}}\right)^M\right]\right)
       \mathcal F_{N,Q_v}(Mt).                          \tag{25}
\]
这是 \(F\) 上同一个解析 germ。对每个非负整数 \(k\)，
\[
 {\mathscr D}_{N,r_N,Mk}
       =\sqrt d\, A_{N,*}^{Mk}\mathcal H_{N,r_N}(k).
                                                               \tag{26}
\]
整个有限 Hall 和保留，未以一个单字的逆矩非零替换(25)。

参考常数项可以严格识别。按 R639/R663 的实际严格 LT frame，
\[
 f_2(v)=v^2T_{\rm g}(w(v))^{-2}x(w(v))
                 \in1+v^6\mathcal O[[v]].
\]
R696(15)的唯一 Hall lift及(13)给出一个原固定中心
\(\mathscr C_{2,T}\in\mathcal O_F^\times\)，使
\[
 \frac1d{\mathscr D}_{2,17r,0}
  =\mathscr C_{2,T}\,
        \frac1d\sum_{\zeta\in\mu_d}f_2([\zeta]Q).
                                                               \tag{27}
\]
它是同一个 norm \(17r\) 的完整 Hall 轨道。
\(\mathscr C_{2,T}\) 一般有 wild 角色，不能设为1。
因为 \(v_p(v_Q)>0,\ p\nmid d\)，右侧的平均等于
\(1+\mathfrak m_F\) 乘原单位中心。故
\[
 \boxed{\mathcal H_{2,17r}(0)\in\mathcal O_F^\times.}      \tag{28}
\]
对充分大的 \(h\)，\(\mathcal H_{2,17r}(p^h)\) 仍为单位。
这也保证(23)可用于下面全部充分靠近的正权。

## 6. 不通过未知解析单位的精确零阶比较

令
\[
 x_r(t)=\nu_r(\gamma)q_{\rm ac}^{Mt}-1.
\]
这是 \(t=0\) 附近的解析坐标，且
\[
 x_r(0)=t_r,\qquad
 x_r'(0)=\nu_r(\gamma)M\log q_{\rm ac}\ne0,\qquad
 v_p(x_r(p^h)-t_r)=h+a+1.                               \tag{29}
\]
导数并非单位；其固定估值 \(a+1\) 必须保留。

在(23)取 \(m=Mp^h\)，再用(26)及
\(v_p(A_{34,*}/A_{2,*})=0\)、(28)，得到对充分大的 \(h\)
\[
 \boxed{
 v_p\mathcal A_p(x_r(p^h))
       =2v_p\mathcal H_{34,r}(p^h).
 }                                                          \tag{30}
\]
这不是一个假设了未知 period 解析性的等式。也没有将
literal usual 全权值本身认成连续族：(25)明确除去实际非单位
\(A_{N,*}^{m}\)，两条来源只在(23)的比值中取消同估值的因子；
所有阶乘先前也已在同一个比值中准确取消。

若 \(\mathcal H_{34,r}\equiv0\)，(30)使
\(\mathcal A_p\) 在趋于盘内点 \(t_r\) 的互异点 \(x_r(p^h)\)
全部为零，故 \(\mathcal A_p\equiv0\)，与(2)/(4)冲突。
所以令
\[
 f_r=\operatorname{ord}_0\mathcal H_{34,r}<\infty,\qquad
 n_r=\operatorname{ord}_{T=t_r}\mathcal A_p<\infty.
\]
在各自首非零项支配的范围，
\[
 \begin{aligned}
 v_p\mathcal H_{34,r}(p^h)&=f_rh+O(1),\\
 v_p\mathcal A_p(x_r(p^h))&=n_rh+O(1).
 \end{aligned}
\]
其中第二个常数项含 \(n_r(a+1)\)。
由(30)比较 \(h\) 的系数，严格得到 \(n_r=2f_r\)，即(7)。
若 \(f_r=0\)，同样得到 \(\mathcal A_p(t_r)\ne0\)；
本证明没有预设 \(f_r>0\)。

## 7. 精确 cyclotomic 重数与原坏条件

\(\Phi_p(1+T)\) 在 \(\mathcal O[T]\) 上为 Eisenstein，
而 \(t_r\) 是其单根。由(7)和原系数域 \(\mathcal O\)，
所有 Galois 共轭第一 wild 点具有同一偶重数 \(2f_r\)。
逐次用 monic Weierstrass 除法可得
\[
 \Phi_p(1+T)^{2f_r}\mid\mathcal A_p(T)
                   \quad\text{在 }\mathcal O[[T]].
                                                               \tag{31}
\]
例如先除一次 \(\Phi_p\)，剩余次数小于 \(p-1\) 的多项式在
\(t_r\) 为零，故余式为零；商在 \(t_r\) 的重数少一，再重复。
这没有把 \(\Phi_p\) 的整投影因子当单位。

为合并中央零，先写 \(\mathcal A_p=T^{2e}B\)。
由于 \(t_r\ne0\)，\(B\) 在 \(t_r\) 仍有重数 \(2f_r\)；
对 \(B\) 进行上述 monic 除法，得到(9)的整除。
不要求 \(T\) 与 \(\Phi_p(1+T)\) 在 \(\mathcal O[[T]]\) 中
生成单位理想。

最后，\(\mu(\mathcal A_p)=0\)，而
\(\Phi_p(1+T)\equiv T^{p-1}\bmod p\)。
(9)给出 \(\lambda_p\ge2e+2f_r(p-1)\)。
原 Hall 精确零与 \(f_r\ge1\) 等价，所以得(8)；
原中央坏条件给 \(e\ge2\)，遂得(10)。

原第一 wild 注的(14)是**精确零与精确整除**
\[
 \mathcal T_{34,T_r}=0
   \iff \Phi_p(1+T)\mid\mathcal A_p.
\]
它不是模 \(p\) 的陈述。与本篇合并后，单次真实
\(\Phi_p\) 因子事实上已迫至少二次；一般高赋值没有这种推论。
特别，R716 的 strict Hall 门依靠
\(v_p(\mathcal T_{34,T_r})<2/(p-1)\)，不能替换成“原中央坏时
Hall 必等于零”。本篇没有证明 \(\lambda_p<2p+2\)、没有证明
任何所需跨 \(p\) 的上界。

## 8. 原始文献和本次实际核验位置

1. K. Kato, *p-adic Hodge theory and values of zeta functions of modular
   forms*, Astérisque 295 (2004), 117–290：
   [Numdam 原文](https://numdam.org/item/AST_2004__295__117_0.pdf)。
   本次直接取得的原文位置为印刷 p.221 Theorem 12.5(1)、
   p.256 §15.8、pp.258–259 Proposition 15.9、
   p.265 式(15.16.1)。前两条 CM 段落分别明确任意有限
   \(\lambda\)、任意含 \(p\) 模数/有限 ray-class 字符的范围。
   完整 PDF 的直接浏览有文件大小限制；本次逐段读取的是
   Numdam 同一 PDF 的可检索原文页，不声称重新取得整本 PDF。
   原两图和中间缩放的核查另见
   [混合权 period 注](../notes/2026-11-27-mixed-weight-period-audit-and-height-difference-scope.md)。
2. A. Lei, D. Loeffler, S. L. Zerbes, *Critical slope p-adic
   L-functions of CM modular forms*，
   [作者全文](https://antoniolei.com/wp-content/uploads/2014/09/critical.pdf)，
   Lemma 2.26、Theorem 2.28 对照两张不同图及(15.16.1)。
   本篇没有用该文后续 ordinary/Dcris 应用段来替代含 \(p\)
   导子时的 Kato \(D_{\rm dR}\) 范围。
3. T. Yang, *Theta liftings and Hecke L-functions*, J. Reine Angew.
   Math. 485 (1997), 25–53，
   [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)，
   Lemma 1.2、Theorem 1.11、Corollary 2.14、Theorems 2.6/2.15。
   (12)–(19)保留原 R290/R302/R716 的所有局部向量、中心、
   Hermite 范数及新增 \(p\) 因子。
4. [原第一 wild Rubin 注](../notes/2026-11-15-original-first-wild-rubin-factor-and-central-order.md)
   §§1–3：同一个整 \(\mathcal A_p\)、BHKO \(\mu=0\)、
   exact Hall 零与单次 \(\Phi_p\) 因子。旧 \(\lambda_p\ge p+3\)
   的条件范围不被删除；本篇在同一条件下将其提高到
   \(\lambda_p\ge2p+2\)。
5. [R696](R696-original-absolute-roots-p2-field-and-linear-height-trace.md)、
   [R703](R703-original-hall-phase-and-finite-fourier-return.md)、
   [R705](R705-original-wild-character-and-absolute-weil-projection.md)、
   R1062/R1066：原全部 \(p^2\) 提升、代数 Miller 常数、actual
   normalized translated jets 与共同合法权子列。

本篇没有新增数值运行、素数扫描或输出数据文件。


## 9. 首非零 physical-weight 系数的准确赋值

继续(25)的原步长 $M=\Delta e_1p^a$，不重新缩小有限角色的
合法权支。令
$$
 \mathcal H_{34,r}(t)=h_f t^f+O(t^{f+1}),\qquad h_f\ne0,
 \qquad
 \mathcal A_p(T)=c_{2f,r}(T-t_r)^{2f}
                         +O((T-t_r)^{2f+1}).
$$
这里 $f$ 可以为0。由(29)、(30)，在充分大的 $h$ 上，
两边的首项分别严格支配；比较除了 $h$ 的系数以外的常数，
准确得到
$$
 \boxed{v_p(c_{2f,r})
             =2v_p(h_f)-2f(a+1).}                       \tag{32}
$$
这个等式只使用已证的逐点赋值身份，不假设两边的比值已经
延拓成解析单位。

按(9)写
$$
 \mathcal A_p(T)=T^{2e}\Phi_p(1+T)^{2f}B(T),
 \qquad B\in\mathcal O[[T]],\quad B(t_r)\ne0 .
$$
因 $t_r$ 的重数恰为 $2f$，严格有
$$
 \begin{aligned}
 c_{2f,r}
  &=t_r^{2e}\bigl(\Phi_p(1+T)'|_{T=t_r}\bigr)^{2f}B(t_r),\\
 v_p(t_r)&=\frac1{p-1},\qquad
 v_p\bigl(\Phi_p(1+T)'|_{t_r}\bigr)
                  =1-\frac1{p-1}.
 \end{aligned}                                           \tag{33}
$$
最后一式来自
$\Phi_p(1+T)=((1+T)^p-1)/T$，在 $t_r\ne0$ 处直接微分；
没有以 cyclotomic 投影代替这个实际因子。

将(33)代入(32)，得
$$
 \boxed{
 \begin{aligned}
 v_p(h_f)
   &=f(a+2)+\frac{e-f}{p-1}+\frac12v_pB(t_r),\\
 v_p(h_f/M^f)
   &=2f+\frac{e-f}{p-1}+\frac12v_pB(t_r)
     \ \ge\ 2f+\frac{e-f}{p-1}.
 \end{aligned}}                                           \tag{34}
$$
第二行是原 physical weight $m=Mt$ 下的首非零系数。
它没有多赚 $v_p(M)$。由于 $B$ 整且 $t_r$ 在极大理想中，
这里使用的 $v_pB(t_r)\ge0$ 由同一整除式保证。

改变(25)的 $A_{34,*}$ 只会把 $\mathcal H$ 乘一个常数项为1
的单位指数；零阶和首非零系数不变。式(34)因而不是任选参考点
造成的估值。$f=0$ 时，它复现原中央阶对第一 wild 值的下界；
以下的新低行只在原 Hall **精确为零**、即 $f\ge1$ 时使用。

## 10. 同一个原 Hall 来源的整 Katz 对偶

### 10.1 模型与所有实际 lift

后面的严格 LT 坐标在 $E_1$ 上。先按已付的实际模型同构作
$$
 S_{17}(z)=\vartheta^{-6}S_1(\vartheta z),\qquad
 Q^{(1)}=\vartheta Q^{(17)},\qquad
 Z_{Q^{(17)}}^{(17)}=\vartheta Z_{Q^{(1)}}^{(1)} .
$$
整个 Miller 指数、half-character 和 $p^2$ lift 随同构运输，
所以 physical $m$ 阶导数乘 $\vartheta^{m-6}$。
取相应的 $A_*$ 后，定义
$$
 H_r(t):=\vartheta^6\mathcal H_{34,r}(t).
                                                               \tag{35}
$$
这是同一个 Hall germ 在 $E_1$ 上的表示；$\vartheta$ 为单位，
所以(32)–(34)的估值不改变。这里不把两个模型的 strict LT
参数直接认成线性缩放；先运输几何 section，再使用 $E_1$
已经固定的严格坐标。

对(14)的每个实际 $v\bmod p$、$N(v)=r$，取其原完整 lift
$T(v)$。令 $\widehat A_v$ 是完整字
$\chi_r(v)e_v^{(34)}$ 在 R1065(W5)的
$[p]^*e_{34}$ 框架中的系数，令
$\widehat{\boldsymbol\mu}_v$ 为对应的 R1065(W13) 对偶。
如果采用 W16 中已经吸收该 wild 相位的 Hall lifts，
$\widehat A_v=A_{34,T(v)}$，不得再乘一次 $\chi_r(v)$。
若采用未加权的(12) lifts，就同时把函数和测度乘
$\chi_r(v)$。两种记法给相同的完整字。

实际点 $Q(v)=pT(v)\ne O$。W4、W7、W10逐字保留
$B_{34,p}$、原中心 $\mathscr C_{34,T(v)}$ 和完整核 character；
由 W8、W11、W13，
$$
 \begin{gathered}
 \widehat A_v\in\mathcal O_F[[v]],\qquad
 \psi\widehat A_v=0,\qquad
 \|\widehat{\boldsymbol\mu}_v\|\le1,\\
 \boldsymbol\mu_H
       :=\frac1{\sqrt d}\sum_{N(v)=r}
                         \widehat{\boldsymbol\mu}_v,\qquad
 P_H(v):=\mathcal K^*\boldsymbol\mu_H
       =\frac1{\sqrt d}\sum_{N(v)=r}\widehat A_v(v)
       =\sum_{n\ge0}a_n v^n .
 \end{gathered}                                             \tag{36}
$$
左端有限指标 $v\bmod p$ 与右端形式参数 $v$ 分别按其原用途
读取。所有中心根、字符、$\vartheta$ 及 $\sqrt d$ 放在同一个
有限 $F/L$ 中。它们为单位，$p\nmid d$，故有限和(36)仍整、
范数至多1，并支撑在 $\mathbb T^\times$。
特别
$$
 P_H\in\mathcal O_F[[v]],\qquad
 \psi P_H=0,\qquad
 \boldsymbol\mu_H(1)=P_H(0)=H_r(0),\qquad
 \boldsymbol\mu_H(c_n)=a_n .                                \tag{37}
$$
这是原单 Hall 的 $d^{-1/2}$ 归一；没有插入双来源 coevaluation
的 $p^{-2}$ Haar，也没有将旧 $\mu_+$ 政名为(36)。

### 10.2 整格与取值精度

准确的测试空间仍是
$$
 \mathscr C^\times
   =C^0_{\mathrm{Gal}}(\mathbb T^\times,\mathcal O_{\mathbf C_p}),
 \qquad X=c_1,\qquad \tau=\frac p{q-1},\quad q=p^2.
$$
$\boldsymbol\mu_H$ 是
$\operatorname{Hom}_{\mathcal O}(\mathscr C^\times,\mathcal O_F)$
中的整泛函。它的完成标量扩张定义在
$\mathcal O_F\widehat\otimes_{\mathcal O}\mathscr C^\times$，
再有理化；取值由 $a\otimes c\mapsto a\boldsymbol\mu_H(c)$
和连续性给出。进一步扩到 $\mathcal O_{\mathbf C_p}$ 也使用
这个完成 tensor，不改成任意连续标量函数上的普通测度。

下文只使用可逐项检查的整数格蕴含
$$
 b\in p^k
       (\mathcal O_F\widehat\otimes_{\mathcal O}\mathscr C^\times)
 \quad\Longrightarrow\quad
 (\boldsymbol\mu_H)_F(b)\in p^k\mathcal O_F,\qquad k\in\mathbf Z .
                                                               \tag{38}
$$
Cp 扩张后的同一式取值在 $p^k\mathcal O_{\mathbf C_p}$。
实际计算中使用的测试系数在 $F$，其收敛和仍在完备的 $F$
中，所以最终各个 $a_n$、矩与 germ 系数具有同一个实际赋值。

特别，不从 pointwise $v_p(b(\xi))\ge\epsilon$、$0<\epsilon<1$
推断 $v_p\boldsymbol\mu_H(b)\ge\epsilon$。
原整格的 gauge 只给 $\lfloor\epsilon\rfloor=0$。
完整 primitive coset character 并不自动改善这个范数。
(38)正是后面截断使用的全部连续性，而非一个无损的
fractional pointwise 积分定理。

## 11. 所有 cover 与连接费用之后的同源 germ

令
$$
 u=\frac{X^\Delta}{p^p},\qquad
 U_q=\frac{q!}{p^{p+1}}\equiv1\pmod p,\qquad
 b_M=M/\Delta=e_1p^a .
$$
R1066(N3)–(N5)是实际 universal character 的系数身份：
$$
 \begin{gathered}
 u=\frac{U_q}{1-p^\Delta}+pU_q\frac{c_q}{X},\qquad
 u,u^{-1}\in\mathscr C^\times,\\
 (u-1)^k\in p^{\lfloor k(1-\tau)\rfloor}\mathscr C^\times,\qquad
 u^t\in\mathscr C^\times\langle t\rangle .
 \end{gathered}                                             \tag{39}
$$
没有遗漏一个可自由选择的 dual-period Teichmüller 常数。
由于 $1-\tau<1$，(39)在 $k=1$ 时只给整性，不给一个 $p$。

写 $A_Q=34Z_Q$，$A_*=A_{Q_*}$，并定义实际 point 尺度
$$
 u_*=\frac{(pA_*)^\Delta}{p^p}.
$$
R1063(L3)给
$Z_Q=(\kappa_*/p)v_Q^p(1+\epsilon_Q)$，
$v_p(\epsilon_Q)\ge\eta=1-1/(p-1)$，
$\kappa_*\in\mathcal O_L^\times$，$v_Q^\Delta=p$。
因此
$$
 \frac{(pA_Q)^\Delta}{p^p}
       =(34\kappa_*)^\Delta(1+\epsilon_Q)^\Delta
              \in1+\mathfrak m_F^{\ge\eta}.                \tag{40}
$$
这里 $(34\kappa_*)^\Delta\in1+p\mathcal O_L$，由非分歧域的
剩余群阶恰为 $\Delta$ 得出。由于 $\eta>1/(p-1)$，
$u_*^{b_Mt}$ 及各实际 ratio 的幂都在整个闭 $t$ 单位盘解析。
无需为此改动已选 $M$。

保持 R1066(N7)–(N10)的全部连接：
$$
 \mathscr A_{34}(j;X)
   =\sum_{s\ge0}(j)_s b_{34,s}(p/X)^s
   \in1+p^{p-2}\mathscr C^\times\langle j\rangle .
$$
任意固定阶 $j$ 导数有相同的 $p^{p-2}$ 界。
在每个非负整数 $m$，N11准确说
$$
 \widehat{\boldsymbol\mu}_v
       (X^m\mathscr A_{34}(m;X))
 =p^m\,\chi_r(v)B_{34,Q(v)}
                       A_{Q(v)}^m\mathcal F_{34,Q(v)}(m),
$$
其中相位已吸收时不再单写右边的 $\chi_r(v)$。
这里 $p^m$ 是实际 cover 导数的费用。
原 physical Hall 导数是整个右边乘 $p^{-m}$。

现在取 $m=Mk=\Delta b_Mk$，先乘确切的
$p^{-p b_Mk}$，然后作(36)的完整有限和。得到
$$
 \boxed{
 H_r(t)=u_*^{-b_Mt}\,
   \boldsymbol\mu_H
       \bigl(u^{b_Mt}\mathscr A_{34}(Mt;X)\bigr).
 }                                                          \tag{41}
$$
先在所有非负整数 $t=k$ 得到本式，因为
$$
 (pA_*)^{Mk}p^{-p b_Mk}
       =u_*^{b_Mk}
$$
且(26)已经除去 $A_*^{Mk}$。
两边均为闭单位盘 Tate germ，故由这些整数点的稠密性得到(41)。
这保留了全部 cover $p^m$、physical $p^{-m}$ 和
$p^{-p b_Mk}$，没有插值一个未经归一的非单位幂。

在(41)中先精确求导，再除实际 $b_M$，得
$$
 \boxed{
 \dot H_r:=\frac{H_r'(0)}{b_M}
   =\boldsymbol\mu_H(\log u)
     +\Delta\boldsymbol\mu_H(\partial_j\mathscr A_{34}(0;X))
     -(\log u_*)H_r(0).
 }                                                          \tag{42}
$$
当 $p\mid b_M$ 时，这仍是等式：先在全式中提出共同的
$b_M$，然后才作下面的精度截断。没有把一个模 $p^k$
近似式直接除 $b_M$。最后一个尺度项只在
$H_r(0)=0$ 时消失。完整连接没有被设为1。

式(34)与 $\Delta\in\mathcal O^\times$ 给
$$
 \begin{array}{ll}
 H_r(0)=0
   &\Longrightarrow\quad v_p(\dot H_r)\ge2,\\[2mm]
 H_r(0)=0,\quad J_p'(0)=0
   &\Longrightarrow\quad
          v_p(\dot H_r)\ge2+\dfrac1{p-1}.
 \end{array}                                                \tag{43}
$$
若 $f=1$，这就是(34)的 physical-weight 首系数；
若 $f\ge2$，左边导数严格为0。没有从常数项的高赋值
代替这里的精确零条件。

## 12. 三个完整 Hurwitz 矩与有限低行

定义同一实际整对偶的正规化 Lie 矩
$$
 M_k:=\boldsymbol\mu_H(u^k)
       =p^{-pk}D^{k\Delta}P_H(0)\in\mathcal O_F,
       \qquad k\ge0,\qquad D=d/dz .
                                                               \tag{44}
$$
后一个等式来自原 character
$\mathbf t_\xi(v)=\exp(X(\xi)z(v))$ 的
$D^m\mathbf t_\xi(0)=X(\xi)^m$，不是 ordinary $v$ 导数。
对每个有限阶，双方都是原 Katz 系数的有限恒等式；
不存在在未知半径上无穷次微分的交换。
(44)本身包含真实的 $p^{pk}$ 可除性。
$M_0=H_r(0)$。

### 12.1 对数尾的全范围界

第 $k$ 个对数项由(39)属于
$$
 \frac{(u-1)^k}{k}
       \in p^{E_k}\mathscr C^\times,\qquad
 E_k=\lfloor k(1-\tau)\rfloor-v_p(k).
$$
对 $1\le k<p$，有 $0<k\tau<1$，所以 $E_k=k-1$。
对 $k\ge p$，函数
$x(1-\tau)-1-\log_p x$ 在 $x\ge p$ 严格递增；
在 $x=p$ 的值为 $p-3-1/\Delta$。
因此整数 $E_k\ge p-3$。这同时证明全部无穷尾趋于无穷。
特别
$$
 \boxed{
 \begin{aligned}
 \log u&\equiv(u-1)-\frac{(u-1)^2}{2}
                                  \pmod{p^2\mathscr C^\times},\\
 \log u&\equiv(u-1)-\frac{(u-1)^2}{2}
                    +\frac{(u-1)^3}{3}
                                  \pmod{p^3\mathscr C^\times}.
 \end{aligned}}                                             \tag{45}
$$
这证明了所有 $k\ge3$、分别 $k\ge4$ 的尾，而不仅检查有限
几个项。p 可整除的 $k$ 已由 $v_p(k)$ 明确计入。

### 12.2 原 Hall 精确零下的真实有限行

现在只假设 $H_r(0)=0$。由(42)，point 尺度项准确为0，
连接导数在 $p^{p-2}\mathcal O_F\subset p^3\mathcal O_F$。
以(38)对(45)取值，得到
$$
 \boxed{
 \begin{aligned}
 \dot H_r&\equiv2M_1-\frac12M_2\pmod{p^2\mathcal O_F},\\
 \dot H_r&\equiv3M_1-\frac32M_2+\frac13M_3
                                           \pmod{p^3\mathcal O_F}.
 \end{aligned}}                                             \tag{46}
$$
所有 $M_k$ 都来自(36)的同一份完整 Hall 来源，不能分别选择。
特别 $M_2,M_3$ 仍读取 $D^{2\Delta}$、$D^{3\Delta}$；
超过 $q-1$ 后，不把它们换成 $ (2\Delta)!a_{2\Delta}$、
$(3\Delta)!a_{3\Delta}$。

结合(43)，得到可直接检查的原低行
$$
 \boxed{
 \begin{aligned}
 H_r(0)=0
   &\Longrightarrow\quad
        2M_1-\frac12M_2\in p^2\mathcal O_F,\\
 H_r(0)=0,\quad J_p'(0)=0
   &\Longrightarrow\quad
 v_p\!\left(3M_1-\frac32M_2+\frac13M_3\right)
                         \ge2+\frac1{p-1}.
 \end{aligned}}                                             \tag{47}
$$
第二行的截断误差在 $p^3$，而显示的门严格小于3；
所以这个分数估值来自已证 Rubin 首 jet，不来自
fractional pointwise 范数的无证保持。

此外，(39)在 $k=2$ 给
$$
 M_2-2M_1=\boldsymbol\mu_H((u-1)^2)\in p\mathcal O_F.
$$
把它代入(47)第一行，严格得
$$
 \boxed{H_r(0)=0\quad\Longrightarrow\quad M_1\in p\mathcal O_F.}
                                                               \tag{48}
$$
这是原 forced 中央阶 $e\ge1$ 已经足够推出的条件；
不需要另假 $J_p'(0)=0$。

## 13. 原 p²-new Hall 的第 q−1 系数

此处终于可以改成一个 ordinary 系数，因为
$z(v)=v+O(v^q)$，且 $\Delta=q-1<q$。逆式也在同一窗为
$v=z+O(z^q)$。因此
$$
 D^\Delta P_H(0)=\Delta!\,a_\Delta,\qquad
 v_p(\Delta!)=p-1,\qquad
 U_q=\frac{\Delta!}{p^{p-1}},
$$
并由(44)得到
$$
 M_1=\frac{U_q}{p}a_{q-1},\qquad U_q\in\mathbf Z_p^\times.
$$
于是(48)准确成为
$$
 \boxed{
 \mathcal T_{34,T_r}=0
 \quad\Longrightarrow\quad
 [v^{p^2-1}]P_H(v)\in p^2\mathcal O_F .
 }                                                          \tag{49}
$$
一般整 $\psi=0$ 来源由 $u\in\mathscr C^\times$ 只给
$a_{q-1}\in p\mathcal O_F$；(49)多出一个 $p$。

$P_H$ 的定义必须保留(36)：
它是原 norm-$r$ Hall 的全部 $p^2$ Weyl 字在实际
$[p]^*e_{34}$ 框架中的整和，先完成原 $\vartheta$ 同构。
它不是裸 $f_{34}=h^{34}R_S$，不是单个 $Q$ 的函数，
也不是 K8 的人工 depletion。特别不能把(49)直接写成
原 $s_{p^2-1}\in p^2$。
这一行是有限的：每个 $[v^{q-1}]\widehat A_v$ 只取其完整
$q-1$ 阶实际 Miller/框架 jet，再按同一 Hall 权求和。
若实际证明 $a_{q-1}/p$ 是单位，就能排除这一原 Hall 的精确零；
本篇尚未给出该单位证明。



若需要在原 $E_{17}$ 的 native pullback frame 直接读取同一系数，
其全部模型费用也可显示。记两个严格参数为 $v_1,v_{17}$。
因为 $z_1=\vartheta z_{17}$ 且各自
$z_b(v_b)=v_b+O(v_b^q)$，原整同构给
$$
 v_1(v_{17})=\vartheta v_{17}+O(v_{17}^q).
$$
[R660](R660-original-torus-coordinate-and-boundary-resonance-ideal.md)
(3)定义 $F_{\rm c}=\Pi_0\log(\sigma/z)$。
$\Pi_0$ 与标量 $\vartheta$ 逐项交换，所以
$E_{{\rm c},17}(z)=E_{{\rm c},1}(\vartheta z)$ 是完整恒等式。
由 $h=\sigma(v/z)E_{\rm c}^{-1}$ 及
$e_{34}=h^{-34}\sigma^{34}$，得到真正的整框架比
$$
 \frac{j^*e_{34,1}}{e_{34,17}}
   =\left(\frac{\vartheta v_{17}}{v_1(v_{17})}\right)^{34}
   =1+r_\vartheta v_{17}^{\Delta}+O(v_{17}^q),
 \qquad r_\vartheta\in\mathcal O_F .
$$
在 $[p]$ 拉回框架中必须先代入
$P(v_{17})=pv_{17}-v_{17}^q$；其第 $\Delta$ 项因此多
$p^\Delta$。原 section 本身还有(35)的
$\vartheta^{-6}$。于是
$$
 \boxed{
 a_{\Delta,17}
   =\vartheta^{\Delta-6}a_{\Delta,1}
       +\vartheta^{-6}r_\vartheta p^\Delta P_{H,1}(0).
 }                                                          \tag{50}
$$
$r_\vartheta$ 是显示的实际框架系数，不宣称它必为单位。
原 Hall 精确为零时第二项严格为0；即便只读模 $p^2$，
它也深于当前精度。因此(49)在两个原模型中完全相容。
norm-$r$ 轨道不因这次模型同构变成 norm-$17r$；
后者仅属于(11)的 degree 2 参考。

## 14. 这条低行的独立性和主目标范围

(49)不是一般 Katz 整性、$\psi=0$ 和质量零的形式推论。
在同一个严格群 $P(v)=pv-v^q$ 上取
$$
 F(v)=v^{2\Delta}-pv^\Delta .
$$
令 $v_1,\ldots,v_q$ 为
$v^q-pv+Y=0$ 的根。完整 Newton sums 给
$$
 \sum_i v_i^\Delta=(q-1)p,\qquad
 \sum_i v_i^{q-2}=0,\qquad
 \sum_i v_i^{2\Delta}=(q-1)p^2.
$$
归一 $\psi$ 是该全迹除以 $q=p^2$，故
$$
 \boxed{
 \psi(v^\Delta)=\frac{q-1}{p},\qquad
 \psi(v^{2\Delta})=q-1,\qquad
 F\in\mathcal O[[v]],\quad \psi F=0,\quad F(0)=0,\quad
 [v^\Delta]F=-p\notin p^2\mathcal O .
 }                                                          \tag{51}
$$
这也给一个实际整 Katz 单位对偶。其
$M_0=0,\ M_1=-U_q$ 为单位，与(39)完全相容：
$u-1$ 的 pointwise 估值至少 $1-\tau$，但其整格 gauge
只有0，泛函不必保持这个分数下界。
因此不能用“单位支撑”或“测度整”偷证(48)。

另一方面，本篇没有证明(49)与原完整 Rubin 因子在逻辑上
独立。(49)正是(31)–(34)经过同一个实际 reader 的后果。
例(51)只排除通用 Katz 性质自动给出(49)，不声称它具有原
$2,3,17$ Schwartz、Hall character、canonical $S$ 或
Rubin 比较。原 exact Hall 零仍可以同时满足(47)、(49)；
迄今没有它们与 actual 完整有限系数的矛盾。

这些结果给下一次实质使用留下明确门：

- 原精确 Hall 零必须同时满足(47)的同源低矩行和(49)的
  完整 $q-1$ 阶系数可除性；
- 核这些行时必须使用同一个 $P_H$，保全部 lift、中心、
  $B_{34,p}$ 和连接，不能把其中的系数当自由变量；
- 若要由此排除原 canonical 坏条件，还须另证该坏条件真的
  落入精确 Hall 零的情形，或回到原
  $v_p\mathcal T_{34,T_r}<2/(p-1)$ 的 strict Hall 门。
  单凭排除精确零并不足以排除一个非零但高赋值的 Hall 值。

以上全部是原对象上的手证；没有数学运行、扫描或新增自由坏行。


### 14.1 实际 Hall 的域下降收紧了 (49) 的独立性

式(49)正确，但对本篇实际来源，它还可由旧整 jet 和域下降直接
得到，因此不能单独当作新增 forcing。

先吸收 R696(15) 的原 Hall 相位。R1065(W7)、(W16)准确给
$$
 \widehat B_Q
   =\mathscr C_{34,T}h(v_Q)^{34}R_S(Q)
   =\mathscr C_{34,T}f_{34}(v_Q),
 \qquad v_p(\widehat B_Q)=6/\Delta ,
$$
其中 $\mathscr C_{34,T}$ 是整个 norm-$r$ 轨道的同一个
实际单位，未重新选择中心。令 $F_1$ 为首挠点域；固定非 $p$
系数及 $\sqrt d$ 只需作非分歧基扩 $L_0/L$。
严格 LT 描述给
$$
 \operatorname{Gal}(L_0F_1/L_0)=\mu_\Delta,\qquad
 F_H=(L_0F_1)^{\mu_d},\qquad
 v_p(F_H^\times)=\frac1{p-1}\mathbf Z .
$$

逐个 physical jet 除中心后只涉及
$h(v_Q),Z_Q=\Xi(v_Q),x(Q),y(Q)$ 及其真实不变导数。
其系数都在 $L_0$；$\sigma_\zeta$ 将完整 jet 送到
$Q\mapsto[\zeta]Q$。W22 的全部
$\alpha_{34,p}$ 系数也在 $L_0$，故返回到 Katz jet 仍交换。
作原 $\mu_d$ 平均后，严格有
$$
 M_0/\mathscr C_{34,T},\quad M_1/\mathscr C_{34,T}\in F_H .
$$
这由完整中心和有限 jet 证明，不由一般 Katz 性质猜测。

置 $u_Q=(p\,34Z_Q)^\Delta/p^p$。N11 取 $m=\Delta$，
保 cover $p^\Delta$ 及正规化 $p^{-p}$，得到
$$
 \begin{aligned}
 M_1-M_0
 &=\frac1{\sqrt d}\sum_{N(v)=r}\widehat B_Q
             \{u_Q\mathcal F_Q(\Delta)-1\}\\
 &\quad-\boldsymbol\mu_H
          \{u(\mathscr A_{34}(\Delta;X)-1)\}.
 \end{aligned}
$$
L3、(40)给 $u_Q-1$ 的估值至少 $\eta$；
R1062 的全 binomial 尾给
$\mathcal F_Q(\Delta)-1\in\mathfrak m^{\ge\eta}$。
最后一项由 N10、(38)在 $p^{p-2}\mathcal O_F$。
所以
$$
 v_p(M_1-M_0)\ge6/\Delta+\eta
     =1-\frac{p-5}{\Delta}
     >1-\frac1{p-1}.
$$
除以实际单位中心后再用 $F_H$ 的离散值群，准确得到
$$
 \boxed{
 M_1-M_0\in p\mathcal O_F,\qquad
 U_q a_{\Delta,1}-p a_{0,1}\in p^2\mathcal O_F .
 }                                                        \tag{52}
$$
它不要求 Hall 为零。结合(50)及 $\vartheta^\Delta\equiv1\pmod p$，
同式无损运到原 $E_{17}$ frame。

因此 Hall 精确零时的(48)、(49)，已由这个 actual 域下降和旧完整
translated jet 强制。例(51)只说明一般整 $\psi=0$ 对偶没有此结论，
不证明它相对于本题完整来源独立。真正额外的精度仍须检查
(47)的 $p^2$ 组合或其含 $H_r(0)$ 的完整版本；
不能把(52)再计为一条独立 canonical 坏条件。

## 15. 完整 Bell 系数给出的高阶差分与含质量的二矩行

本节仍用(36)的同一份完整 Hall 对偶。置
$s=1/(p-1)$、$\eta=1-s$，并定义
$$
 \delta_k:=\boldsymbol\mu_H((u-1)^k)
      =\sum_{j=0}^k(-1)^{k-j}\binom kj M_j,\qquad k\ge1.
 \tag{53}
$$
这里 $M_0=H_r(0)$ 保留。以下估值来自实际有限 Miller 来源，
不是把 fractional pointwise 下界无损地穿过一般 Katz 对偶。

### 15.1 原全 Bell 界和有限差分的整数性

[R1062](R1062-original-translated-miller-jets-and-critical-weight-germs.md)
(G2)--(G5)对同一 physical $z$ 导数证明
$$
 \mathcal F_Q(m)=\sum_{\rho\ge0}\binom m\rho a_{Q,\rho},
 \qquad v_p(a_{Q,\rho})\ge\rho\eta .
$$
其证明使用完整未除幂 Bell 多项式的整数系数及极阶帽；
因此这个界对全部 $\rho$ 成立，未截成
$\mathcal F_Q\in1+\mathfrak m^{\ge\eta}$ 后再臆推高阶差分。
N11取 $m=\Delta j$，保实际 cover 和 $p^{-pj}$ 后给
$$
 M_j=\frac1{\sqrt d}\sum_Q\widehat B_Q
                   u_Q^j\mathcal F_Q(\Delta j)-E_j,\qquad
 E_j=\boldsymbol\mu_H\!\left(
           u^j\{\mathscr A_{34}(\Delta j;X)-1\}\right)
       \in p^{p-2}\mathcal O_F .
 \tag{54}
$$
$E_0=0$。N10的整连接界与(38)正是最后一项的依据。

固定 $k$，只在整数 $0\le j\le k$ 计算。写
$$
 u_Q^j\mathcal F_Q(\Delta j)
  =\sum_{\ell,\rho}
    \binom j\ell\binom{\Delta j}{\rho}
        (u_Q-1)^\ell a_{Q,\rho}.
$$
这个和在这些整数点是有限的：
$\ell\le k$、$\rho\le\Delta k$ 足够。
关于 $j$ 的多项式
$\binom j\ell\binom{\Delta j}{\rho}$ 次数为 $\ell+\rho$。
其第 $k$ 阶差在 $\ell+\rho<k$ 时严格为零；在其它情形中，
差是整数，因为每个被相减的整数点值都是整数。
所以不能因 ordinary polynomial 系数含阶乘分母，再虚增一个
$v_p(\ell!\rho!)$ 的损失。

由(40)，$v_p(u_Q-1)\ge\eta$。每个剩余项的赋值至少
$k\eta$。再乘完整 $\widehat B_Q$ 的 $6/\Delta$，并保(54)
的连接误差，得
$$
 v_p(\delta_k)\ge
       \min\{6/\Delta+k\eta,\ p-2\}.
$$
对 $1\le k\le p-2$，第一项严格小于 $p-2$。
此外，§14.1的下降对每个有限 $j\Delta$ 阶 jet 完全相同：
该阶在 $\mu_d$ 上的角角色平凡，W22的全连接系数仍在 $L_0$。
故所有 $M_j/\mathscr C_{34,T}$，从而
$\delta_k/\mathscr C_{34,T}$，都在同一个 $F_H$。
原中心是单位，而 $F_H$ 的值群为 $s\mathbf Z$。
于是准确提升为
$$
 \boxed{
 v_p(\delta_k)\ge
   \frac{\left\lceil(p-1)(6/\Delta+k\eta)\right\rceil}{p-1}
   =k-\frac{k-1}{p-1},
       \qquad 1\le k\le p-2 .
 }
 \tag{55}
$$
最后等号用 $0<6/(p+1)<1$。特别
$v_p\delta_1\ge1$、
$v_p\delta_2\ge2-s$、
$v_p\delta_3\ge3-2s$。

不能把(55)无代价延到 $k=p-1$：
此时实际连接误差 $p^{p-2}$ 已不足以给所显示的较强界。
所有更高项仍使用(39)、(38)的原整 gauge，不作该外推。

### 15.2 保留质量的真实斜率及全部对数尾

定义未除 point 单位的同源 germ
$$
 G_r(t):=u_*^{b_Mt}H_r(t)
       =\boldsymbol\mu_H
          \!\left(u^{b_Mt}\mathscr A_{34}(Mt;X)\right),
 \qquad
 \dot G_r:=G_r'(0)/b_M .
$$
这是(41)的实际重写；不是新的 canonical 坏条件。精确求导给
$\dot G_r=\boldsymbol\mu_H(\log u)
+\Delta\boldsymbol\mu_H(\partial_j\mathscr A_{34}(0;X))$。

对 $3\le k\le p-2$，(55)给
$v_p(\delta_k/k)\ge k-(k-1)s\ge3-2s$。
$k=p-1$ 时原整 gauge 给至少 $p-2$；
所有 $k\ge p$ 由§12.1给至少 $p-3$，且趋于无穷。
连接导数在 $p^{p-2}$。因此完整无穷尾已经支付，且
$$
 \boxed{
 \begin{aligned}
 v_p\!\left(\dot G_r-
       \left(2M_1-\frac12M_2-\frac32M_0\right)\right)
       &\ge3-2s,\\
 \dot G_r&=\dot H_r+(\log u_*)M_0 .
 \end{aligned}}
 \tag{56}
$$
这里的提升用的是(54)的真正 finite jets及同一个 $F_H$；
并没有声称一般 $\psi=0$ 整对偶也保持(55)。

作为精确零分支的一个后果，(43)、(55)--(56)给
$$
 \begin{gathered}
 H_r(0)=0\ \Longrightarrow\
    v_pM_1\ge2-s,\qquad v_pa_\Delta\ge3-s,\\
 H_r(0)=0,\ J_p'(0)=0\ \Longrightarrow\
    v_p\!\left(2M_1-\frac12M_2\right)\ge2+s .
 \end{gathered}
 \tag{57}
$$
第二行使用 $3-2s>2+s$。这些结论仍要求真正的 Hall 零；
原 $J_p'(0)=0$ 单独并不提供这个条件。
含 $M_0$ 的主分支应使用完整(56)，不能套(57)。

### 15.3 二矩行的原严格参数返回

这一步只换回同一 $P_H$ 的有限系数，不改变来源。
由 $z(pv-v^q)=pz(v)$，
$$
 z(v)=v+\ell_qv^q+O(v^{2q-1}),\qquad
 \ell_q=\frac1{p^q-p},\qquad
 v(z)=z-\ell_qz^q+O(z^{2q-1}).
$$
因为 $2\Delta=2q-2<2q-1$，在 $P_H(v(z))$ 的
$z^{2\Delta}$ 槽，唯一新的交叉项来自 $a_\Delta$。所以
$$
 \begin{aligned}
 U_1&=\Delta!/p^{p-1}=U_q,\qquad
 U_2=(2\Delta)!/p^{2p},\\
 M_1&=\frac{U_1}{p}a_\Delta,\qquad
 M_2=U_2(a_{2\Delta}-\Delta\ell_q a_\Delta),\\
 U_1&\equiv1\pmod p,\qquad U_2\equiv-1\pmod p .
 \end{aligned}
$$
两个 $U_i$ 的估值与剩余类分别由 Legendre 和 Wilson
公式直接得到。没有 $a_0$ 项，因为常数在复合下仍为常数。
尤其 $v_p(\ell_q)=-1$，不能删除其费用。将此代入(56)得
$$
 \boxed{
 v_p\!\left[
  2\dot G_r-
  \left\{\left(\frac{4U_1}{p}+U_2\Delta\ell_q\right)a_\Delta
          -U_2a_{2\Delta}-3a_0\right\}
          \right]\ge3-\frac2{p-1}.
 }
 \tag{58}
$$
此式精确保同一个完整 Hall、所有 $p^2$ lift、原中心、
physical $p^{-m}$ 和 $[p]$ 框架。
它为含质量的更深比较提供明确的有限行，但本节没有将
$\dot G_r$ 直接认作原 $J'_S$，也没有证明(58)与原坏条件冲突。

## 16. 原混合权比值的解析单位：先固定 CM-pair 图，再作相消

本节加强§4的逐权赋值式。所插值的是两条原来源完成全部公共
非单位因子相消后的比值，保持原 $\mathcal A_p$ 的整基；
并不插值单条未正规化的 usual 临界值序列。

### 16.1 比较标量由原图定义，不由非零 Hall 值求商

继续固定同一 $\nu_r^{-1}$。在§4.1的两条路径中，使用
Kato §15.8 的同一个 CM tensor 构造、§15.9 的共同
$(34\delta p^2)$ CM-pair，以及两模型原始 Néron/Betti 基。
从已固定的 $F_\vartheta^*\xi_{17}=\mathcal A_p\xi_1$ 出发，
tensor、特化、dual exponential 与两张比较图给
$$
 \mathcal A_p(x_m)\,\mathscr E_{1,\nu_r,m}
      =\epsilon_r(m)\,\mathscr E_{17,\nu_r,m},
 \qquad m>0,\quad d\mid m .
 \tag{59}
$$
这里 $\epsilon_r(m)$ 的定义是两条实际一维 tensor 路径中
基向量的比较标量，方向由(59)固定。它在对椭圆单位类取值以前
已经定义；即使某条 Hall 值为零，也不以该值作除数。
§4.2的整格证明给 $\epsilon_r(m)\in\mathcal O_F^\times$。

为追踪随权的费用，先在两图中共同提出并取消：
$p^2$-CM-pair 的 Betti/Tate 因子
$p^{-2(2m+1)}$、(22)的整个 $1/p$ 投影、同一个分歧 Artin
基及其 de Rham/Gauss period、共同临界 Tate/Gamma 因子，
以及同一个 auxiliary smoothing。
这些取消在原秩一 tensor 图中进行，未将任何一项单独称作单位。
$p$ 处两个未分歧参数相同；$\nu_r$ 分歧后本地 $L$-因子均为1。
参考的 $17$ primitive Euler 因子仍准确乘回 $18/17$。

下面按实际箭头列出剩余的有限对象。置
$\mathfrak f_0=(34\delta)$，取原 ray-class CM-pair 的共同
定义域 $K(\mathfrak f_0)$；必要时一并含原 $\vartheta$ 模型同构。
由于 $h_K=1$，
$$
 G_0=\operatorname{Gal}(K(\mathfrak f_0)/K)
      \simeq(\mathcal O_K/\mathfrak f_0)^\times/\mu_6,
 \qquad |G_0|=(6\cdot288)/6=288 .
$$
实际使用的局部下降群是它的分解子群；完整 $G_0$ 可在全部
$p$-adic embedding 的直积上作用，二者给同一条 CM 线。
这些固定非 $p$ 域及原模型扩张在 $p>211$ 非分歧。
$p^2$ 层和 $\nu_r^{-1}$ 线并未放入这个群：它们正是上一段
已经同保、同消的公共因子。

对原 CM-pair 的 $g$ 字，令 $\phi_g$ 为定义其 Galois 作用的
相容 CM 同源，并记
$\phi_g^*\omega^g=c_g\omega$、$n_g=\deg\phi_g$。
理想代表可取与 $p$ 互素；于是该同源在原 good 模型的微分
格上是同构，$c_g,n_g$ 均为当前位单位。
改变代表必须同时改 principal CM 标量、微分与 Hecke 角色；
它仍是同一个原箭头。下面的 $R_g$ 记录这一有限标记
在所选 embedding 基中的实际置换，未添加任意矩阵。

| 原箭头 | 固定基中的全部权依赖 |
|---|---|
| 原 ray-class CM 线 | Kato §15.8 的 $\operatorname{coLie}(E)^{\otimes(2m+1)}$，连同原 Hecke descent；每个 $g$ 的系数由 $c_g^{2m+1}$ 和 $\psi_j(\mathfrak b_g)^{\pm(2m+1)}$ 给出，有限角色在 $6\mid m$ 支上固定 |
| Betti/Tate 基 | 原 $\beta_j^{\otimes(2m+1)}\otimes\zeta^m$；$p^2\beta_j$ 的公共非单位费用已先消，余基变换为固定单位的 $2m+1$ 次幂 |
| 原 Néron 微分与模型 | $F_\vartheta^*\omega_{17}=\vartheta^{-1}\omega_1$，以及共同非 $p$ CM-pair 到各原模型的真实同源微分倍率；均只取同一单位的 $2m+1$ 次幂 |
| Tate/Norm 与非 $p$ 下降 | $m$ 次 twist 给固定 Norm 单位的 $m$ 次幂；原下降是 $|G_0|^{-1}\sum_g\rho_{j,m}(g)$，没有 $p$ 分母 |
| 原 signed 类与整基 | $\xi_j$、$F_\vartheta^*$ 及 $\xi_1$ 的 $\Lambda$-基一次固定；本篇不逐权换基。若作一次固定 signed 整基变换，只产生该同一 $\Lambda^\times$ 的评价 |
| 临界值与 theta 平方 | 两图共同的 $\delta^m m!$ 已先消；全权平方中的 $6\kappa_0 17^{-m}$ 和模型 $\vartheta^{2m-12}$ 在§16.3明列；参考 $18/17$ 保回原 primitive 值 |

因此，所有非 $p$ primitive 比较是在固定有限标记空间上，
由以下系数及其相容矩阵的乘积、限制和逆构成：
$$
 \alpha^{\,2m+1},\qquad \beta^m,\qquad
 P_j(m)=\frac1{|G_0|}\sum_{g\in G_0}
       D_{j,g}(m)R_g,\qquad
 [D_{j,g}(m)]_{\iota\iota}
       =\zeta_{j,g,r,\iota}\,
        \alpha_{j,g,\iota}^{\,2m+1}\beta_{j,g,\iota}^{\,m} .
 \tag{60}
$$
这里 $\iota$ 指所用全部 $p$-adic embedding 的矩阵位置。
每个 $\alpha_{j,g,\iota}$ 具体由表中同源微分与
$\psi_j(\mathfrak b_g)$ 在该位置的单位倍率按原箭头取商得到；
$\beta_{j,g,\iota}$ 具体是该位置的 Norm/Tate 倍率。
$\zeta_{j,g,r,\iota}$ 保固定有限角色。
这些系数可以随位置改变；(60)未将不同共轭错认成共同标量。原箭头反向时取其逆。
不需要数值求这些倍率，就能从各自定义确认：它们是固定在
同一个非分歧域 $L_0$ 中的单位；没有随 $m$ 重新选择的 period。
若有限 $\nu_r$ 的相位仍写在(60)，它只是固定系数，导数为0。

$P_j(m)$ 是原秩一 CM descent 的真正幂等元。
由于 $|G_0|$ 是单位，取不变部分是整格的直和因子；
原 good CM-pair 的 primitive 线因有限 étale 下降而自由秩一。
因此在任一合法正权，原矩阵均有一个单位的秩一 minor。
选取该实际 minor 只为在固定标记坐标中读取原 primitive 基，
并不更换该基。§16.2用模 $p$ 恒定性把同一个 minor 运到
整个权盘和 $t=0$；所以锚点不依赖一个非零 Hall 值，也不
依赖未给出的 $m=0$ 临界值。

还需排除一个特别重要的遗漏：modular 比较是否留下
Betti/étale 的相对 CM period。这里可以逐式消去，不需
Kato §15.11 末未证明的相容性。
令 $a_m$、$b_m$ 分别为
[Lei--Loeffler--Zerbes, pp.9--10, Lemma 2.26(a)、(b)](https://antoniolei.com/wp-content/uploads/2014/09/critical.pdf)
的两个映射，$s_m$ 为给定的 de Rham 映射。
作者没有断言 $a_m=b_m$，本篇也不用这个等式。
令 $e_\psi(\gamma_m)$ 表示(21)的同一完整 CM--Artin 类，
已带上同一个临界 Tate twist。Theorem 2.28及Kato(15.16.1)给
$$
 a_m e_\psi(\gamma_m)=z^{\mathrm{Kato}}_{\,b_m\gamma_m}.
$$
对左边施 dual exponential，用(a)的定义性图，得到
$s_m(\exp^*e_\psi(\gamma_m))$。
这里以及下一式，只比较 Kato 临界值定理给出的代数 CM 向量：
记它为 $y_m$，其所选 $p$-adic 嵌入正是
$\exp^*e_\psi(\gamma_m)$ 的原代数基坐标。
先在原 period 定义的代数线上作图交换，之后分别取既定的
复嵌入和 $p$-adic 嵌入；并未定义一个将一般
$\mathbf C_p$ 系数映入 $\mathbf C$ 的映射。
整个 $\theta_{\chi,f}^{\pm}$ 有限和/符号投影和同一个
CM--Artin 基在两个图中逐项保持。
再用(b)的复 period 图
$\operatorname{per}_f\circ s_m=b_m\circ\operatorname{per}_\psi$，
Kato Theorem 12.5(1)准确给
$$
 b_m\!\left(\operatorname{per}_\psi(y_m)\right)
   =\mathcal E_{\mathrm{common}}(m)\,
       L_{\mathrm{primitive}}(m)\,b_m(\gamma_m).
$$
这里有限角色的和、正负投影及公共 Artin 基都按原图同取。
现在将同一个 $b_m$ 逆施于两边，得到纯 CM tensor 的
period 身份。没有出现 $b_m^{-1}a_m$：
$a_m$ 已由 de Rham 自然性变成 $s_m$，
而 $s_m$ 随后由复图变成同一个 $b_m$。
若 $s_m$ 改乘任意标量，两图及 Kato 标签同时改变，
上述两步仍逐项相消。

余下 $\operatorname{per}_\psi$ 正是 Kato §15.8 的原椭圆
period map 的 $2m+1$ 次 tensor；它的模型、Betti、微分和
有限下降已经逐项列在表中。因此不存在另一个未标记的
$a/b$ 相对 period，可以藏成任意逐权单位。
所用原始身份见
[Kato, 印刷 pp.256--265，§15.8--15.9、Lemma 15.11、
(15.16.1)](https://numdam.org/item/AST_2004__295__117_0.pdf)。
这完成(60)对本篇两条原图的穷尽，不调用该 LLZ 论文后面的
ordinary $D_{\mathrm{cris}}$ 结论。

### 16.2 固定有限矩阵的解析延拓和整导数

共同增大原 $M$ 的 prime-to-$p$ 因子一次，使它还倍于(60)
全部 $\alpha,\beta,\alpha_{j,g,\iota},\beta_{j,g,\iota}$，
以及下方实际出现的 $\vartheta^{-4}$ 在 $L_0$ 剩余域中的阶。
记增大的数仍为 $M=\Delta b_M$。
这不能仅凭 $\Delta$ 完成，因为 $L_0/L$ 可能是非平凡非分歧扩张。
若新增因子为 $e_2$，则
$H_{\rm new}(t)=H_{\rm old}(e_2t)$、
$b_{\rm new}=e_2b_{\rm old}$，所以所有
$H^{(k)}(0)/b_M^k$ 保持原值。仍是同一合法权支。

现在每个(60)的幂准确写作固定 $m=0$ 值乘
$\exp(Mt\log\alpha)$ 或 $\exp(2Mt\log\alpha)$。
这些固定单位在 $L_0$，故其 principal log 属于
$p\mathcal O_{L_0}$。固定 ramified $\nu_r$ 相位对 $t$ 的导数为0，
并未用其 log 来代替这个估值。
所以全部原矩阵在 $\mathcal O_F\langle t\rangle$ 上定义，
模 $p$ 等于其 $t=0$ 的矩阵。

在合法正权 $m=M$，表中的 primitive 线给一个实际单位 minor。
其剩余类和 $t=0$ 相同，故这个同一 minor 在整闭盘可逆。
幂等及原比较等式也先在整数权成立，再由解析唯一性成立于整盘。
以该坐标在同一原秩一线上读取(59)的标量，得到唯一实际族
$$
 \boxed{
 \epsilon_r^{\rm an}(t)\in\mathcal O_F\langle t\rangle^\times,\qquad
 \epsilon_r^{\rm an}(k)=\epsilon_r(Mk),\qquad
 \frac{(\epsilon_r^{\rm an})^{(j)}(t)}{b_M^j}
        \in p^j\mathcal O_F\langle t\rangle\quad(j\ge1).
 }
 \tag{61}
$$
右端 $\epsilon_r(Mk)$ 指(59)的整数权标量；左端是由原固定
矩阵实际构造的解析延拓。

导数界可逐运算检验：每次对单位幂求导并除 $b_M$，
准确产生 $\Delta\log\alpha$ 或 $2\Delta\log\alpha$，
属于 $p\mathcal O_{L_0}$；有限和、乘积保持这个分级。
对单位 minor 的逆，逐次微分
$a(t)a(t)^{-1}=1$，整数 Leibniz 系数给同样的 $p^j$ 下界。
这也支付全部逆矩阵。若改变原 signed 整基，所乘的是一份固定
$\Lambda^\times$，其在 $x_r(t)$ 的取值和各阶归一导数有同样性质，
不是每个整数权重新选择的单位。本篇则始终用(2)的原基。

### 16.3 两份 raw Hall germ 上的精确整平方比较

对 degree 2 参考以完全相同的 W/N 构造记 $G_{2,17r}(t)$；
其 mass 为原 $H_{2,17r}(0)$。该值为单位，(24)--(27)以及
(G5)给
$G_{2,17r}(t)-G_{2,17r}(0)\in\mathfrak m_F\mathcal O_F\langle t\rangle$，
所以它在当前闭盘是解析单位。相位中心仍是原实际中心。

N11在两条 $E_1$ 来源上、对同一个 $m=Mk$ 准确给
$$
 \mathscr D^{(1)}_{N,r_N,m}
       =\sqrt d\,p^{-m+pm/\Delta}G_{N,r_N}(k).
 \tag{62}
$$
两边的整数指数由 $\Delta\mid m$ 保证。
这是 cover 导数和正规化后再返回 physical 导数的恒等式；
两来源取比时这些 $p$ 幂完全相消。
目标回到原 $E_{17}$ 还有
$\mathscr D^{(17)}_{34,r,m}
 =\vartheta^{m-6}\mathscr D^{(1)}_{34,r,m}$。
代入(19)、(59)，把全部已知原尺度并在一起，得
$$
 \boxed{
 \begin{aligned}
 \mathcal A_p(x_r(t))
   &=\mathcal U_r(t)
       \left(\frac{G_{34,r}(t)}{G_{2,17r}(t)}\right)^2,\\
 \mathcal U_r(t)
   &=\frac{6\kappa_0}{17^2}\,
        (\vartheta^{-4})^{Mt}\epsilon_r^{\rm an}(t)
        \in\mathcal O_F\langle t\rangle^\times,\\
 \mathcal U_r^{(j)}(t)/b_M^j
   &\in p^j\mathcal O_F\langle t\rangle
           \qquad(j\ge1).
 \end{aligned}}
 \tag{63}
$$
$\kappa_0=2^7\,3^3\,7^2\,17^2$。
$(\vartheta^{-4})^{Mt}$ 使用刚固定的同一 Teich 分量。
其系数来自
$17^{-m}\vartheta^{2m-12}=17^{-2}\vartheta^{-4m}$，
没有再乘一次模型费用。

先在每个正整数 $t=k$ 由原图和全权平方得到(63)，
再由两侧真实 Tate 解析性和整数点的稠密性延拓。
参考是单位，故这一步从未除目标 Hall 值。
所有 point 单位 $u_*$ 已由 raw $G$ 的定义准确消去；
(63)也没有把复 period 作为任意标量嵌入 $\mathbf C_p$。

## 17. 含非零 Hall 质量的准确导数门

本节只是(63)在原整 $\mathcal A_p$ 上的必要后果，
不将它自动视为与旧有限行独立。
记
$$
 \partial=b_M^{-1}d/dt,\qquad
 F(t)=G_{34,r}(t)/G_{2,17r}(t),\qquad
 s=1/(p-1).
$$
由 $x_r(0)=t_r$、$v_pt_r=s$ 及
$\partial^j x_r(0)
 =\nu_r(\gamma)(\Delta\log q_{\rm ac})^j$，
每个 $j\ge1$ 有准确赋值 $j$。
原 $\mathcal A_p(T)=T^{2e}B(T)$、$B\in\mathcal O[[T]]$ 给
$$
 v_p\partial^j(\mathcal A_p\circ x_r)(0)
       \ge j+(2e-j)s,\qquad 0\le j\le2e .
 \tag{64}
$$
这是同一个整函数的有限链式求导，阶乘只增加估值；
没有把 $x_r'(0)$ 当作单位。

结合(61)、(63)，前两阶严格成为
$$
 \boxed{
 \begin{aligned}
 v_p F(0)&\ge e s,\\
 v_p\{F(0)\partial F(0)\}
      &\ge1+(2e-1)s,\\
 v_p\{(\partial F(0))^2+F(0)\partial^2F(0)\}
      &\ge2+(2e-2)s .
 \end{aligned}}
 \tag{65}
$$
例如第二阶中，
$\partial\mathcal U/\mathcal U\in p\mathcal O_F$、
$\partial^2\mathcal U/\mathcal U\in p^2\mathcal O_F$；
第一阶已得的 $F\partial F$ 界保证这两项均深于
显示的第二阶门。因此不能遗漏 $\mathcal U$ 导数，但也无需
把它错误设为常数。

若写 $g_j=\partial^jG_{34,r}(0)$、
$r_j=\partial^jG_{2,17r}(0)$，则
$$
 \begin{aligned}
 F(0)&=g_0/r_0,\\
 \partial F(0)&=(g_1-g_0r_1/r_0)/r_0,\\
 \partial^2F(0)
 &=\{g_2-2g_1r_1/r_0
          +g_0(2(r_1/r_0)^2-r_2/r_0)\}/r_0 .
 \end{aligned}
 \tag{66}
$$
$r_0$ 是已经支付的实际单位。特别 $g_0=H_r(0)$，
无论是否为零都保留在(66)中。$g_1$ 的同源有限返回是(56)--(58)，
而参考的所有导数仍由其原 $\Theta_2$、norm-$17r$ Hall 和
完整连接计算，不能另选低参数。

(65)是以后测试高精度同源行的准确接口。
只知 $J'_p(0)=0$ 时有 $e\ge2$，从而得到(65)相应下界；
没有因此得到 $g_0=0$。最低阶约束若已由原 Hall 的有限系数
自动满足，必须按其真实范围记录。新的 forcing 仍须在同一个
完整来源中证明某条更深关系与这些必要条件不相容。

## 18. 原共同 Gaussian 的全部 $p-1$ 个权块

本节只处理(63)中的两条实际单 Hall 来源：
在 $E_1$ 的同一不变微分下，目标为 $S_1$、norm-$r$，
参考为 $\Theta_2$、norm-$17r$。
各自的 Hall 中心、原 lift、有限字符和 $d^{-1/2}$ 归一保持不变。
所用首 Gaussian 是原 $c_\sigma$，$v_p(c_\sigma)=-1$；
完整剩余高项和连接 $\Gamma$ 不作删除。

### 18.1 参考的真实点标签与准确变量尺度

在 $\mathbf F_{p^2}^\times$ 中取 $\bar\beta$ 满足
$\bar\beta^{p+1}=17$。Hensel 引理在这个指定剩余类给唯一
$\beta\in\mathcal O_L^\times$ 满足
$$
 \beta^d=17,\qquad d=p+1 .
$$
记 $b$ 为 $\bar\beta$ 的 Teichmüller lift。
第一层 $p$ 挠点上
$[\beta]Q=[b]Q$，且原 strict LT 坐标给
$v_{[b]Q}=b\,v_Q$。所以 $Q\mapsto[b]Q$ 准确重标为原
norm-$17r$ 参考点集。重标时保参考的实际完整 Hall 权，
不将 $\beta$ 的 principal-unit 部分额外乘入该字符。

在参考的 physical Lie 变量作 $z\mapsto\beta z$，便有
$$
 2c_\sigma(\beta z)^d=34c_\sigma z^d .
 \tag{67}
$$
这仅是同一个实际 Taylor germ 的变量缩放。
$\beta$ 不被认作全局 CM 同源，也不宣称
$N_{L/\mathbf Q_p}(\beta)=17$。

记已带全部权的 normalized Hall germs为
$\mathscr S_{34}(z)$、$\mathscr S_2(z)$，
其 $m$ 阶导数是相应 $\mathscr D_m/\sqrt d$。
置
$$
 \begin{gathered}
 \mathscr S_+(z)=\mathscr S_{34}(z),\qquad
 \mathscr S_0(z)=\mathscr S_2(\beta z),\qquad
 \lambda=34c_\sigma,\\
 \mathscr V_\epsilon(z)=e^{-\lambda z^d}
                           \mathscr S_\epsilon(z),
           \qquad \epsilon=+,0 .
 \end{gathered}
$$
这些是原全和的形式恒等式；它们没有把逐点比
$\mathscr S_+/\mathscr S_0$ 当作 Hall 权函数的比。
两个来源现在有完全相同的首 Gaussian，余下的
$\mathscr V_\epsilon$ 仍保原全部高 Gaussian、Miller 和 $\Gamma$ 项。

### 18.2 全部权块及统一整数归一

取一次共同的代数数 $\Pi$，满足
$\Pi^\Delta=p^p$，故 $v_p(\Pi)=\tau=p/\Delta$。
它只用于同时写全部块；下面显示原第0块不依赖这个选择。

对每条来源及每个 $\rho\in\{0,\ldots,p-2\}$，
取 physical 权
$$
 m_\rho(t)=d\rho+\Delta t .
$$
在非负整数 $t=k$ 定义
$$
 \mathcal G_{\epsilon,\rho}(k)
   =(p/\Pi)^{m_\rho(k)}
      D^{m_\rho(k)}\mathscr S_\epsilon(0).
 \tag{68}
$$
这是实际 cover 正规化，不能丢 $(p/\Pi)^m$。
由 R1062(G7)和原 N11，同一函数的解析表达是
$$
 \mathcal G_{\epsilon,\rho}(t)
  =\frac1{\sqrt d}\sum_Q\widehat B_{\epsilon,Q}
       a_{\epsilon,Q}^{\,d\rho}
       u_{\epsilon,Q}^{\,t}
       \mathcal F_{\epsilon,Q}(d\rho+\Delta t),
 \qquad
 a_{\epsilon,Q}=\frac{pA_{\epsilon,Q}}{\Pi},\
 u_{\epsilon,Q}=a_{\epsilon,Q}^{\Delta}.
$$
目标 $A_{+,Q}=34Z_Q$；参考缩放后的
$A_{0,Q'}=2\beta Z_{Q'}$。
两者均有 $v_p(A)=\tau-1$，所以 $a_{\epsilon,Q}$ 是单位。
由(40)，目标的 $u_Q$ 为真正 principal unit；
参考再乘 $\beta^\Delta=17^{p-1}\in1+p\mathcal O_L$，
仍有同一 $v_p(u_Q-1)\ge\eta$ 界。
完整 $\mathcal F$ 的 Gauss 范数由(G5)--(G6)控制。
因此每一 $\mathcal G_{\epsilon,\rho}$ 都是同一个有限域上的
整 Tate 函数，范数至多1。这里使用实际有限 Hall 和，
没有把任意 Katz 对偶当成无损 fractional-norm 测度。

第0块给原 raw germs
$$
 \mathcal G_{+,0}(b_Mt)=G_{34,r}(t),\qquad
 \mathcal G_{0,0}(b_Mt)
      =17^{(p-1)b_Mt}G_{2,17r}(t).
 \tag{69}
$$
右端的幂是 $17^{p-1}\in1+p\mathcal O_L$ 的实际解析幂。
更一般参考第 $\rho$ 块的已知缩放就是
$17^\rho(17^{p-1})^t$。所以 $\beta$ 的不同 Hensel
剩余类或 $d$ 次根选择不会制造一个新的自由相位；
对全部 $m\in d\mathbf Z$，$\beta^m=17^{m/d}$。

### 18.3 首 Gaussian 在权端是完整跨块 shift

置
$$
 \gamma=\lambda(p/\Pi)^d,\qquad
 v_p(\gamma)=p-1-\frac1{p-1}.
$$
对 $h\ge0$，唯一写
$$
 \rho-h=\rho_h-(p-1)\ell_h,\qquad
 0\le\rho_h\le p-2,\quad \ell_h\in\mathbf Z_{\ge0}.
$$
于是
$m_\rho(t)-dh=d\rho_h+\Delta(t-\ell_h)$。
在 $\mathcal O_F\langle t\rangle^{\,p-1}$ 上定义
$$
 \boxed{
 (\mathcal T_\gamma\mathbf H)_\rho(t)
  =\sum_{h\ge0}
     \frac{\gamma^h}{h!}\,
       (d\rho+\Delta t)_{dh}\,
       H_{\rho_h}(t-\ell_h).
 }
 \tag{70}
$$
$(x)_j=x(x-1)\cdots(x-j+1)$ 是原 falling factorial。
平移 $t\mapsto t-\ell_h$ 保持闭单位盘 Gauss 范数；
$(d\rho+\Delta t)_{dh}$ 为整多项式。
第 $h$ 项因此有统一下界
$$
 h\left(p-1-\frac1{p-1}\right)-v_p(h!)
 \ \ge\ h\left(p-1-\frac2{p-1}\right).
$$
它趋于无穷，故(70)在整个有限块向量上真正收敛。
$h=0$ 是恒等项，其余项严格较深。

有限 falling-factorial 身份
$$
 (m)_{dh}(m-dh)_{dk}=(m)_{d(h+k)}
$$
连同全部块的 carry $\ell_h$，对满足同一参数赋值下界的
$\gamma_1,\gamma_2$ 给
$\mathcal T_{\gamma_1}\mathcal T_{\gamma_2}
=\mathcal T_{\gamma_1+\gamma_2}$。
两重和可交换，因为上述下界只随 $h+k$ 趋于无穷。
特别 $\mathcal T_\gamma^{-1}=\mathcal T_{-\gamma}$。

由原 physical 乘积 $e^{\lambda z^d}\mathscr V$ 的有限
Leibniz 公式，准确有
$$
 \boxed{
 \mathbf{\mathcal G}_\epsilon
    =\mathcal T_\gamma\,
            \mathbf{\mathcal G}^{\,c}_\epsilon,\qquad
 \mathbf{\mathcal G}^{\,c}_\epsilon
    =\mathcal T_{-\gamma}\,
            \mathbf{\mathcal G}_\epsilon ,
       \qquad\epsilon=+,0 .
 }
 \tag{71}
$$
其中 $\mathcal G^c$ 在非负整数权是
$(p/\Pi)^mD^m\mathscr V_\epsilon(0)$ 的真实值。
先在这些权上，$h>m/d$ 的 falling factorial 严格为0，
所以式子是有限原 Taylor 身份；再用(70)的全盘收敛与
各块整数点稠密性得到(71)。
这提供了完成来源本身的 Tate 族，没有预先假设其新的
Amice 有界性或较大权半径。

若换 $\Pi'=\xi\Pi$、$\xi^\Delta=1$，则第 $\rho$ 块乘
$\xi^{-d\rho}$，而 $\gamma'=\xi^{-d}\gamma$。
由于 $h+\rho_h=\rho+(p-1)\ell_h$，
(70)逐项给这个对角变基的准确共轭式。
因此(71)在第0块、尤其(69)的原读者上与 $\Pi$ 的选择无关。

### 18.4 此完整相消所支付的范围

(71)把两个原来源的同一个 Gaussian 真正移到同一个
跨 $p-1$ 块算子；原点集、所有角色、中心和已知
$17^\rho(17^{p-1})^t$ 均已支付。
它不是在第0块内的乘法算子：
一般
$$
 \frac{(\mathcal T_\gamma\mathbf H)_0}
      {(\mathcal T_\gamma\mathbf K)_0}
 \ne\frac{H_0}{K_0}.
 \tag{72}
$$
所以不能仅因 physical 两个 Gaussian 相同，就从(63)删除它。
(70)还说明它保持 $m\bmod d$；角6等其它实际来源单位
不能免费进入原 $m\equiv0\bmod d$ 的读者。

本节严格证明了全跨块返回与统一尾。
若后继要提高原比值的权半径，还须使用
$\mathbf{\mathcal G}^{\,c}_+$ 与
$\mathbf{\mathcal G}^{\,c}_0$ 的实际共同关系；
单字非零、单字 second-disc 范数或(71)的形式可逆性均不替代它。

## 19. 同一整 Rubin 函数的 $p$ 阶 Euler 读者及完整首连接

本节沿用(63)的实际 $G_{34,r}$、$G_{2,17r}$、$\mathcal U_r$，
不另添坏条件。记
$$
 \partial=b_M^{-1}\frac d{dt},\qquad
 c=\Delta\log q_{\rm ac},\qquad v_p(c)=1 .
$$
所有模 $p^{p+1}$ 的陈述均指原完成系数域的整格；
不能只取点值的 fractional 下界后声称测度无损保持它。

### 19.1 原整函数确切给出的 Euler 同余

在任意特征 $p$ 系数环上，$D_T=(1+T)\partial_T$ 满足
$D_T^p=D_T$。这不要求系数被 Frobenius 固定。
更明确地，以第二类 Stirling 数记
$$
 D_T^p-D_T
 =\sum_{j=2}^{p-1}S(p,j)(1+T)^j\partial_T^j
       +(1+T)^p\partial_T^p .
$$
中间 $S(p,j)$ 被 $p$ 整除，而 $\partial_T^p/p=(p-1)!\partial_T^{[p]}$
保持 $\mathcal O_L[[T]]$。所以
$$
 \mathscr Q_p(A):=(D_T^p-D_T)A/p\in\mathcal O_L[[T]]
 \qquad(A\in\mathcal O_L[[T]]) .
$$
由 $\partial x_r=c(1+x_r)$，在本篇同一权盘上有准确恒等式
$$
 \boxed{
 \partial^p(\mathcal U_rF^2)
       -c^{p-1}\partial(\mathcal U_rF^2)
   =p c^p\,\mathscr Q_p(\mathcal A_p)(x_r(t))
      \in p^{p+1}\mathcal O_F\langle t\rangle ,
 \qquad F=G_{34,r}/G_{2,17r}.
 }
 \tag{73}
$$
右端一般不为零。尤其不能由 $\operatorname{ord}_0\mathcal A_p\ge4$
把它改成新的精确零等式。

若 $U_i=\partial^i\mathcal U_r(0)$、$F_i=\partial^iF(0)$，(73)的实际
点读者就是
$$
 \sum_{i+j+k=p}\frac{p!}{i!j!k!}\,U_iF_jF_k
   -c^{p-1}(U_1F_0^2+2U_0F_0F_1)
       \in p^{p+1}\mathcal O_F .
 \tag{74}
$$
$U_p$ 和所有混合项均保留；(61)的 $v_pU_i\ge i$ 不允许
在(74)中一律把它们删除。

### 19.2 两条原 Hall 来源的 $p$ 阶连接只剩一个真实块

以下 $N=34$ 取 norm-$r$ 来源，$N=2$ 取 norm-$17r$ 来源。
$\mu_{H,N}$ 始终是原完整、已归一的单 Hall Katz 对偶，
保全部字、角色、中心和 $d^{-1/2}$，并有整算子范数至多1。
degree 2 的连接使用与 N7--N10 完全相同的
$(z/v)^2E_{\rm c}^2$，无需新归一。

记 $X=c_1$、$u=X^\Delta/p^p$、$\ell=\log u$，并定义真实高阶差分
$$
 \delta_{N,k}=\mu_{H,N}((u-1)^k).
$$
这里 $k=p,p+1$ 仍是同一原测度的实际读者；
不把(55)仅证明到 $p-2$ 的估值外推到这两个指标。

由 N7，原连接的首非零系数准确为
$b_{N,d}=+Nc_\sigma$，$d=p+1$。不是反向 gauge 的负号。
N8 的全部其余支撑满足 $r\ge2d$，其整格
$$
 r-\lfloor r\tau\rfloor-\lceil r\tau\rceil
       \ge2p-3\ge p+1 .
$$
对权求导、整数平移和乘上 $\ell^a$ 都不降低这个界。
因此对 $0\le k\le p$，令 $P(m)=(m)_{p+1}$，从原 N9 得
$$
 \partial^kG_N(0)\equiv
 \mu_{H,N}\!\left[
  \ell^k+Nc_\sigma p^dX^{-d}
       \sum_{j=0}^k\binom kj\Delta^jP^{(j)}(0)\ell^{k-j}
             \right]\pmod {p^{p+1}}.
 \tag{75}
$$
这是原完整连接的有控制截断，不是预先把它换成首 Gaussian。

对 $k=p$，$P(m)\equiv m^{p+1}-m^2\pmod p$。
故 $3\le j\le p-1$ 的 $P^{(j)}(0)$ 至少被 $p$ 整除，
并且 $\binom pj$ 再给一个 $p$。
原联合点值界为
$$
 v_p(Nc_\sigma p^dX^{-d})=p-1-s,\qquad
 v_p(\ell)\ge1-\tau .
$$
所以这些混合项至少为
$p+2-s-\tau>p+1$。$j=1,2$ 因保留了至少 $p-2$ 个
$\ell$，有更强的同一下界；$j=0$ 严格为0。
先对整个等变测试取这个联合界，再进入整数 gauge，
故积分以后确实模 $p^{p+1}$ 消失。

唯一尚存项准确为
$$
 P^{(p)}(0)=-p!\sum_{a=0}^p a
          =-\frac{p!\,p(p+1)}2 .
$$
特别这项的联合估值为 $p+1-s$，不能先删。

### 19.3 对数幂与负块的有限返回

在同一个整测试格中，
$$
 \ell^p\equiv(u-1)^p-\frac p2(u-1)^{p+1}
                    \pmod {p^{p+1}\mathscr C^\times}.
 \tag{76}
$$
证明如下。$\log(1+x)^p$ 的前两系数是 $1,-p/2$。
在 $p+2\le n\le2p-2$ 时，产生 $x^n$ 的每个对数因子的次数均小于 $p$；
模 $p$ 的 freshman 恒等式迫其系数被 $p$ 整除，
故代 $x=u-1$ 后估值至少 $1+n(1-\tau)>p+1$。
对 $n\ge2p-1$，系数是 $p!s(n,p)/n!$，这里 $s(n,p)$ 为整数。
全尾估值至少
$$
 n(1-\tau)+1-v_p(n!)
 \ge n(1-\tau-s)+1>p+1 .
$$
最后在 $n=2p-1$ 已比 $p+1$ 大 $p-5-3/\Delta>0$，
以后线性增大。这也支付整尾收敛，而不只有限模计算。
同理
$c^{p-1}\ell\equiv c^{p-1}\{(u-1)-(u-1)^2/2\}\pmod {p^{p+1}\mathscr C^\times}$。

沿§18同一 $\Pi^\Delta=p^p$，记未作 $\beta$ 缩放的原块
$$
 B_N=\mathcal G_{N,p-2}(-1),\qquad
 \gamma_N=Nc_\sigma(p/\Pi)^d .
$$
因为 $d(p-2)-\Delta=-d$，原 N11 的同一合法极限给
$$
 B_N=\Pi^d\,
       \mu_{H,N}\!\left[X^{-d}\mathcal A_N(-d;X)\right].
$$
例如取 $m_h=\Delta e p^h-d$，同时保原全部有限相位，
准确归一为 $p^{-p e p^h}$；两边按 N5/N10 的全盘界取极限。
这不是把某个新负槽值自由定义成 $B_N$。

用 N10，去掉该式中的 $\mathcal A_N(-d)-1$ 所产生的误差，
在乘回 $Nc_\sigma p^d\Delta^p p!p(p+1)/2$ 后至少为 $p^{2p-2}$。
所以(75)--(76)给
$$
 \boxed{
 \partial^pG_N(0)\equiv
 \delta_{N,p}-\frac p2\delta_{N,p+1}
   -\frac{\gamma_N\Delta^p p!p(p+1)}2 B_N
           \pmod {p^{p+1}} .
 }
 \tag{77}
$$
若 $\Pi$ 换成 $\xi\Pi$、$\xi^\Delta=1$，
$\gamma_NB_N$ 由§18的实际对角变基保持不变。
对参考的已付 $\beta$ 缩放，
$\mathcal G^{\beta}_{2,p-2}(-1)=17^{-1}B_2$，
故 $\gamma_2B_2=\gamma_{34}\mathcal G^{\beta}_{2,p-2}(-1)$。
这正是同一共同 Gaussian 的真实跨块费用。

再用(42)的连接尾与对数二项式，得到
$$
 \boxed{
 (\partial^p-c^{p-1}\partial)G_N(0)
 \equiv \delta_{N,p}-\frac p2\delta_{N,p+1}
       -c^{p-1}\left(\delta_{N,1}-\frac12\delta_{N,2}\right)
       -\frac{\gamma_N\Delta^p p!p(p+1)}2B_N
            \pmod {p^{p+1}} .
 }
 \tag{78}
$$

### 19.4 与原坏条件的关系

(74)须使用同一个参考商。若 $g_j=\partial^jG_{34,r}(0)$、
$r_j=\partial^jG_{2,17r}(0)$，则全部 $F_j$ 由准确递推
$$
 r_0F_j=g_j-\sum_{a=0}^{j-1}\binom ja F_a r_{j-a}
 \qquad(1\le j\le p)
 \tag{79}
$$
给出，其中 $r_0$ 是实际已付单位。
(75)、(77)使最高行明确落回同一 Hall 高差分与第 $p-2$ 块；
$\mathcal U_r$ 仍是(60)--(63)那份全矩阵构造的原单位，
其导数不得由任意替代单位计算。

R530和R1051已经有其它原格上的 Fermat/除幂机制；
它们本身不识别(74)这一个 Hall 商读者。
本节支付的是该读者的准确返回及全连接费用。
(73)只使用原 $\mathcal A_p$ 的整性，尚未证明(74)
与已有原来源关系独立，也未得到
$J'_p(0)=0\Rightarrow H_r(0)=0$。
要将这一行用于主结论，必须在同一完整来源中评价(74)，
并保(77)的跨块项及所有参考、$\mathcal U_r$ 导数。

## 20. 在(74)的精度内，首连接的完整平方贡献已自动变深

本节实际评价§19的一项，而不添加新假设。
结论不是 $\gamma_{34}B_{34}=\gamma_2B_2$；
这两个原块一般不同。准确结论是：在整个
$\mathcal U_r(G_{34}/G_2)^2$ 的 Euler 读者中，
首连接的总贡献属于 $p^{p+1}$，故不能由(77)单个尚存项制造矛盾。

先以 $s=b_Mt$ 为共同权坐标，故 $\partial=d/ds$。
原完整 Hall 和及 R1062(G5)给
$$
 v_p \partial^kG_N(s)\ge k\eta\quad(1\le k\le p-2),\qquad
 v_p\partial^{p-1}G_N(s)\ge p-2-s_0,
 \quad s_0=\frac1{p-1},
 \tag{80}
$$
作为闭权盘的 Gauss 下界，其中 $N=34,2$，参考仍取 norm-$17r$。
为避免与权坐标混淆，本节用 $s_0$ 记原赋值步长。

这里可直接核全尾：对
$\mathcal F_Q(m)=\sum a_{Q,r}(m)_r/r!$，
$j$ 阶导数的下界是
$v_p(j!)+\inf_{r\ge j}\{r\eta-v_p(r!)\}$。
若 $j\le p-2$，$r<p$ 的最小值为 $j\eta$，
而 $r\ge p$ 的 Legendre 下界已大于它；
若 $j=p-1$，最小可能值在 $r=p$，为 $p-2-s_0$。
再与 $u_Q^s$ 的全部 Leibniz 项相乘，得到(80)。
这是实际有限点表达上的全导数界，不是从一般 Katz 对偶的
fractional 点界直接推出。

原 R1063(H16)、(H23)的完整中心恒等给
$G_{34}(0)=C_{34,T}d^{-1/2}\sum_{\zeta\in\mu_d}f_{34}(\zeta v_Q)$。
$f_{34}\in v^6\mathcal O_L[[v]]$，因此角平均第一次允许的正次数
为 $d$，准确有
$$
 v_pG_{34}(0)\ge s_0 .
 \tag{81}
$$
本步不使用 bad 条件。参考质量已证明为单位。
原连接从首阶 $d$ 起，所以去连接的原 Katz 族
$M_N(s)=\mu_{H,N}(u^s)$ 有同一质量。
N9的整尾以及(80)还给 $M_N$、参考逆及下列有限乘积同样的
$k\le p-2$、$k=p-1$ 导数界。

记 $P(m)=(m)_{p+1}$。在模 $p^{p+1}$ 的全函数及全部 ordinary
导数意义下，由 N8 可写
$$
 G_N(s)=M_N(s)+\gamma_N P(\Delta s)B_N(s)
                         \pmod {p^{p+1}},
 \qquad
 B_N(s)=\mathcal G_{N,p-2}(s-1).
$$
此处将 $B_N$ 内的连接换回原完整块所生误差至少 $p^{2p-4}$；
所有二次首连接项也深于 $p^{p+1}$。$\gamma_NB_N$ 与 $\Pi$
选择无关。参考可依(69)作已付 $\beta$ 缩放，也可保持未缩放两项。

于是
$$
 \mathcal U_r(G_{34}/G_2)^2
 -\mathcal U_r(M_{34}/M_2)^2
 =P(\Delta s)\{\gamma_{34}H_+(s)+\gamma_2H_0(s)\}
                       \pmod {p^{p+1}},
$$
其中准确的两项是
$$
 H_+=2\mathcal U_r M_{34}M_2^{-2}B_{34},\qquad
 H_0=-2\mathcal U_r M_{34}^2M_2^{-3}B_2 .
$$
它们保原参考和全部 $\mathcal U_r$；均有
$v_pH_\epsilon(0)\ge s_0$，
以及(80)的非零阶下界。

现对右边取 $\partial^p$。
纯 $P^{(p)}$ 项由(77)的
$v_p(\gamma_N\Delta^pP^{(p)}(0))=p+1-s_0$
及(81)准确变为至少 $p+1$。
对 $3\le j\le p-1$，$\binom pjP^{(j)}(0)$ 至少被 $p^2$ 整除，
余 $p-j$ 阶 $H$ 导数至少为 $(p-j)\eta$，故也深于 $p+1$。
$j=1,2$ 用(80)的高阶界更深；$j=0$ 为0。
$c^{p-1}\partial$ 项则由 $P'(0)=-p!$ 立即更深。
所以准确得到
$$
 \boxed{
 (\partial^p-c^{p-1}\partial)
 \left[
 \mathcal U_r(G_{34}/G_2)^2
 -\mathcal U_r(M_{34}/M_2)^2
 \right]_{s=0}\in p^{p+1}\mathcal O_F .
 }
 \tag{82}
$$
因此(74)在当前精度真正剩下的是两份原 bare Katz 族的
对数--Fermat组合及实际 $\mathcal U_r$。
$\psi M_N=0$ 的来源陈述本身不杀这一组合；
本节没有将不同 Galois 对偶的对数测试认作 $\mathbf Z_p$-测度。
后继仍须对同一完整 $\mathcal U_r(M_{34}/M_2)^2$ 判断其
Frobenius 费用，不能把(82)误称为全部(74)已经自动。


## 21. 同一 CM-pair 上的实际相对 period 与 Fermat-$17$ 权因子

本节把§16的原比较标量按其定义性图展开。始终使用 R303 的
$F_\vartheta^*\xi_{17}=\mathcal A_p\xi_1$ 和原 primitive Betti/Tate 基；
不作新的 signed $\Lambda$-基变换。下文的固定常数在椭圆单位取值
以前定义，因此即使目标 Hall 值为零也不以该值作除数。

### 21.1 先在代数 CM 线上 tensor，再施原 period 图

置 $w=2m+1$，$6\mid m$。Kato 的负型角色为
$\Psi_{j,m}=\psi_j^{-w}\nu_r^{-1}$。
取共同 $\mathfrak f=(34\delta p^2)$ 的 canonical CM-pair $E_{\mathfrak f}$，
并在含原模型同构的共同有限域上取与原 CM Betti 基相容的
$q_j:E_{\mathfrak f}\simeq E_j$。记
$e_j=q_j^*\omega_j$。在复一致化中两图分别是
$$
 \mathbf C/\mathfrak f\longrightarrow
 \mathbf C/(\varpi_j\mathcal O_K),\qquad
 z\longmapsto \frac{\varpi_j}{34\delta p^2}\,z .
 \tag{83}
$$
式(83)中的 $1$ 只指定共同的有理 Betti 标记；完整格的生成元是
$34\delta p^2$，它准确映到两模型各自的 primitive 标记 $\varpi_j$。
式(83)只标记实际代数同构和这些 Betti 基；没有把复 period 嵌入
$\mathbf C_p$。由 $q_{17}=F_\vartheta q_1$，
$$
 e_{17}=\vartheta^{-1}e_1.
 \tag{84}
$$

还须核原反圆分特化与 $w$ 次 tensor 的同一基方块。
令 $b_j\in T_j^{-1}$ 是 R303 已固定的相容基，
$F_\vartheta^*b_{17}=b_1$，$\zeta$ 是共同 cyclotomic Tate 基。
在同一个 $\chi_m^{-1}$ 线上固定 $e_m$，用原身份
$\chi_m^{-1}=T_j^{-2m}(m)$ 将它送到 $b_j^{2m}\zeta^m$。
于是实际识别 $I_{j,m}$ 满足
$$
 \begin{aligned}
 I_{j,m}:(T_j^{-1}(1))\otimes\chi_m^{-1}
       &\longrightarrow T_j^{-w}(1+m),\\
 I_{j,m}(b_j\zeta\otimes e_m)&=b_j^w\zeta^{m+1},\\
 (F_\vartheta^*)^{\otimes w}I_{17,m}
       &=I_{1,m}(F_\vartheta^*\otimes\mathrm{id}_{e_m}).
 \end{aligned}
 \tag{84a}
$$
最后一式在显示的完整 Betti/Tate 基上系数为1。
所以 tensor 同一 $\chi_m^{-1}$ 后的原映射确是
$F_\vartheta^*$ 的 $w$ 次 tensor；没有另一个
$\vartheta^{2m}$ 重新识别费用。
在 de Rham 后用原 Néron tensor 读取该图时，才由(84)一次产生
$\vartheta^{-w}$。若改用两模型各自的 Néron tensor 来规范
$\chi_m^{-1}$ 的基，必须同时运输 $e_m$；不能将该改基因子再
乘到(84a)已固定的原方块上。共同 $\nu_r^{-1}$ tensor 对此式不作改变。


这里可以直接核原下降，不需要在每个权另选一个 primitive minor。
Kato 印刷 p.257 的定义是
$\eta_\Psi=\Psi(\mathfrak a)^{-1}(\eta_{\mathfrak a}^*)^{\otimes w}$。
在 $w=1$ 的原模型线上，$e_j$ 与实际 Hecke 角色的下降相容。
将这个等式逐字取 $w$ 次 tensor，并 tensor 同一个
$\nu_r^{-1}$ Artin 基，恰得到 $\Psi_{j,m}$ 的下降：
$$
 \eta_{\Psi_{j,m},g}
   =\eta_{\psi_j^{-1},g}^{\otimes w}
      \otimes\eta_{\nu_r^{-1},g}.
 \tag{85}
$$
因此 $e_j^{\otimes w}$ 连同该同一 Artin 线就是本次使用的
descended CM 基。有限比角色
$\chi_{17}=\psi_{17}/\psi_1$ 的阶整除6，且
$\chi_{17}^{w}=\chi_{17}$；两模型间仍是(84)的同一个
$F_\vartheta$，而非随 $m$ 新换的 twist。
临界 Tate tensor 的 Norm 作用两边相同，也在(85)的完整 tensor
中同取。把固定 $288$ 下降写成有限矩阵时，那些矩阵只是(85)
在所选标记中的表达，不再产生额外的相对归一因子。

Kato 同页的 $\operatorname{per}_\Psi$ 正是原椭圆
$\operatorname{coLie}\to H^1_B$ period map 的 tensor。
以原 primitive Betti 双基 $\gamma_j$ 表示，去掉两边同一个临界
Tate tensor后，它准确给
$$
 \operatorname{per}_{\Psi_{j,m}}
   (\omega_j^{\otimes w}\otimes e_{\nu,\mathrm{dR}})
   =\varpi_j^w g_\nu\,
           \gamma_j^{\otimes w}\otimes e_{\nu,B}.
 \tag{86}
$$
$g_\nu$ 是同一实际分歧 Artin period。
(86)先是原代数 CM 线与其复 period 的比较；只有得到该代数线上的
临界系数后才取既定的 $p$-adic 嵌入。

### 21.2 公共因子的逐项位置

对§4.1的两条实际路径使用同一个 dual exponential。
§16.1已经逐图支付 $a_m\to s_m\to b_m\to b_m^{-1}$，
故没有残留一个未标记的 modular $a_m/b_m$ 比值。
原 Kato Theorem 12.5(1) 在
$k=2m+2,r_{\mathrm{crit}}=m+1$ 给出的复因子是
$(2\pi i)^m L_{\{p\}}$；它不含 level 的额外 $N^m$。
下面列出本次所有可能影响两图相对权的项。

| 项目 | 在原图中的位置与取消 |
|---|---|
| 共同非 $p$ 模数 $34\delta$ | (83)把 canonical Betti 标记 $1$ 送到两条 primitive 标记的同一 $(34\delta p^2)^{-1}$ 倍；coLie 与 Betti 经同一 $q_j$ 运输。Kato p.257末至p.258首的模数独立性按这些实际同源识别，故没有一边另留下 $17^m$ |
| $p^2$ Betti/Tate 费用 | Kato p.258 的 $p^2\beta$ 原始 Tate 基给共同 $p^{-2w}$；保持后在两式取比时取消 |
| 固定 finite $\nu_r^{-1}$ | 同一个 $p^{-1}$ 字符投影、Artin 基、$g_\nu$、Gauss 和及导子归一；均先保再同消 |
| 临界 Tate/Gamma | 将 $(2\pi i)^m L/\varpi_j^w$ 写成本文 $\mathscr E_{j,\nu_r,m}$，共同因子准确为 $\delta^m m!$；不把 $m!$ 当单位 |
| 辅助 smoothing | 原共同惰性辅助理想的 $\ell^2+\ell^{-1}$，与 $m$ 无关，最后同除 |
| $2,3$ primitive 因子及有限投影 | 两边均用各自原角色。比较的公共层保同一 $2,3$ 支持；$\chi_{17}^w=\chi_{17}$ 使相对有限标记不随合法权变化。其实际固定基倍率只进下面的常数 |
| 参考 $17$ 因子 | 共同模数暂删后按原 primitive 值乘回。因 $\psi_1((17))=-17$、$N(17)=17^2$、$\nu_r((17))=1$，因子恒为 $1-(-17)^w/17^{2m+2}=18/17$ |
| $p$ Euler 与 Yang 平方中的 $p^{-1}$ | $\nu_r$ 分歧，局部 $L$ 因子为1；两份完整 Hall 平方另有同一个 $p^{-1}$，它已在(19)中，不另混入 period 比较 |
| 原 signed 整基 | $\xi_j$ 与 $F_\vartheta$ 一次固定；原始基与上述原 CM tensor 标签的固定倍率保留，不作逐权或新的 $\Lambda^\times$ 换基 |

因而在原代数基中，若 $y_{j,m}$ 表示这一实际临界
dual-exponential 向量，有
$$
 y_{j,m}
  =k_{j,r}\,K_{\mathrm{common}}(m)\,
       \mathscr E_{j,\nu_r,m}\,\eta_{j,m},
 \qquad
 F_\vartheta^*\eta_{17,m}
       =\vartheta^{-w}\eta_{1,m}.
 \tag{87}
$$
$K_{\mathrm{common}}(m)$ 依次包含表中公共 $p^2$、Artin、Gamma、
Tate 费用，允许为非单位；$k_{j,r}\in\mathcal O_F^\times$
只含已固定的 primitive/有限标记与基的常数倍率。
(83)--(86)说明这是两条具体原图上的等式，不能用任意
“逐权单位”代替 $k_{j,r}$。
原类的两次特化由R303(19)及本篇(21)给
$F_\vartheta^*y_{17,m}=\mathcal A_p(x_m)y_{1,m}$。
先取消同一个 $K_{\mathrm{common}}(m)$，即得
$$
 \boxed{\epsilon_r(m)=\kappa_r\vartheta^{-(2m+1)},
 \qquad \kappa_r=k_{17,r}/k_{1,r}\in\mathcal O_F^\times.}
 \tag{88}
$$
该恒等式是在原基下的比较；若事后改变 signed 基，必须再显写
那一份固定 $\Lambda^\times$ 的评价，不得仍称其为常数。

### 21.3 原 $\mathcal U_r$ 的真实权与参考 $\beta$ 缩放

代回已发表的(63)，所有物理与 theta 费用仍只计一次：
$$
 \mathcal U_r(t)
   =U_{r,0}\,17^{-Mt},\qquad
 U_{r,0}=\frac{6\kappa_0\kappa_r}{17^2\vartheta}
        \in\mathcal O_F^\times .
 \tag{89}
$$
这里 $\vartheta^{-4Mt}$ 来自原全权平方及模型；
$\vartheta^{-2Mt}$ 来自(88)，所以总和才是 $17^{-Mt}$。
没有另外再乘一个 $17^{-m}$。

现保持§18的实际 $\beta^{p+1}=17$、$N\bar\beta=17$，
并置 $\nu_\beta=N_{L/\mathbf Q_p}\beta$。
参考的 physical 变量换成 $\beta z$ 后，germ乘 $\beta^{Mt}$，
所以同一平方比较的单位变为
$$
 \mathcal U_r^\beta(t)=U_{r,0}(\nu_\beta/17)^{Mt}.
 \tag{90}
$$
$\beta^{2Mt}=\nu_\beta^{Mt}$ 在当前合法权支严格成立：
$\beta/\bar\beta$ 是阶整除 $p+1$ 的 Teich 单位。
(90)不把 $\beta$ 当全局同源，也不将 $\nu_\beta$ 设成17。

最后写 $\beta=bz$，$b$ 为其 Teich 余类提升。实际
$z^{p+1}=17/\widehat{17}$ 且 $z\in1+p\mathbf Z_p$，从而
$\log\nu_\beta=2\log17/(p+1)$。
以原 $\partial=b_M^{-1}d/dt$，(90)的常数 log 连接为
$$
 \lambda_{17}
   =\Delta\log(\nu_\beta/17)
   =-(p-1)^2\log17,\qquad
 \lambda_{17}/p\equiv q_p(17)\pmod p .
 \tag{91}
$$
另一方面 $c=\Delta\log q_{\rm ac}$ 属于 $L$ 的反不变 Lie 线，
$v_pc=1$，故 $(c/p)^{p-1}\equiv-1\pmod p$。
于是原单位本身的 $p$ 阶 Frobenius 缺陷准确为
$$
 \boxed{
 \lambda_{17}^p-c^{p-1}\lambda_{17}
       \equiv2p^p q_p(17)\pmod{p^{p+1}}.}
 \tag{92}
$$
所有混合项仍须保留：将(73)用于 $\beta$-scaled 的实际商，
应作用的是
$(\partial+\lambda_{17})^p-c^{p-1}(\partial+\lambda_{17})$。
(92)只明确其中的原单位费用，未单独将其当作非零矛盾；
同源 Katz 商、原中心与实际 lift 差的贡献必须一并评价。

一手定位：Kato，
[印刷p.257的下降与椭圆period定义](https://www.numdam.org/article/AST_2004__295__117_0.pdf)、
[pp.257--258的模数独立性及canonical CM-pair基](https://www.numdam.org/article/AST_2004__295__117_0.pdf)、
[Theorem12.5(1)，印刷p.221](https://www.numdam.org/article/AST_2004__295__117_0.pdf)；
其无额外level幂的临界公式亦在印刷p.272再次原样显示。
本节只消费这些原图；不调用 ordinary $D_{\mathrm{cris}}$ 结论。


## 续证：完整 native Euler 窗口与 exact-norm 框架

[§§22–23，式（93）–（101）](R1067-original-first-wild-rubin-native-euler-continuation.md)继续同一原来源：全部p阶jet只需实际H_a的首p+2槽；完整carry、Lagrange/阶乘及商导数均保，首Fermat frame在当前Euler精度自动变深。原文已近单文件大小上限，完整续证另存同编号；主无穷非零仍未完成。
