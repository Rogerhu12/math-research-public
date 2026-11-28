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
