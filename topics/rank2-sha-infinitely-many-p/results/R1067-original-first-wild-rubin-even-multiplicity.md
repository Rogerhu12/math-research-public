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
