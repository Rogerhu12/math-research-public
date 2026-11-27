# 原 S3150 完整有限来源与 K/Y 读者的点域投影

2026-11-27 UTC。接原 [unitary 全字](2026-11-27-original-y-k-rational-unitary-and-precise-p-level-words.md) §§10–15 与 [全 p-character 返回](2026-11-27-original-connected-words-and-full-p-character-return.md) §4。

本注支付实际有限读者的全部点载体，包括完整三处模块、五处全部24个新角色和目标 p 的所有有限字符。原正交伙伴的一阶 jet 只成为代数系数，不能以其相反角色消掉点因子的惯性。最终得到原完整 K/Y 值的一个非零 point-only 投影。这里没有给任意中央 logarithm 的无限尾定义点投影，也没有从这个非零读者跳到原 canonical 坏条件的矛盾。

## 1. 固定原来源，保两支及所有伙伴

沿原文记六输出为 Y,H,K,J,A,N，令
$$
 \mathscr P_3=\Pi_{H,0}\Pi_{J,0}\Pi_{N,0},\qquad
 \nu=\mathscr P_3\rho .
\tag{1}
$$
下标3表示三个实际 CM 型投影，不是三次 Taylor 多项式。
原行 Y、K 的范数为126、6。对于 $\epsilon=\pm1$，固定
$$
 U_\epsilon=2Y+21\epsilon K,\quad V_\epsilon=-\epsilon Y+2K,
 \quad \|U_\epsilon\|^2=3150,\quad\|V_\epsilon\|^2=150.
\tag{2}
$$
两行及 H,J,A,N 的全正交关系沿原 Gram 身份。原固定乘积为
$$
 \mathcal G_\epsilon(z,w,\mathbf t)
 =-\frac1{84}\prod_{j=1}^6
 \sigma_{17}(U_{\epsilon,j}z+V_{\epsilon,j}w
      +H_jt_H+J_jt_J+A_jt_A+N_jt_N),
 \qquad
 \mathcal F_\epsilon(z,w,\mathbf t)
 =\mathcal G_\epsilon(z/5,w/5,\mathbf t).
\tag{3}
$$
反变符号仍是：$\phi_n^+$ 的其它有限来源为 $\mathcal F_-$，
$\phi_n^-$ 的其它有限来源为 $\mathcal F_+$。
(3)保每个伙伴，不以单变量边际替代。

Y 方向是原偶次数、标准 theta characteristic 的完整
$S_M=H^0(E_0,\mathcal O(MO))$（其中包括奇函数，standard even
并非把整个空间限制为偶函数），
$M=3150$。完整代数基可取
$$
 \sigma^M x^a\quad(0\le a\le M/2),\qquad
 \sigma^M yx^a\quad(0\le a\le(M-4)/2).
\tag{4}
$$
在第二类中使用
$$
 \sigma^M yx^a=(y\sigma^4)\Theta^a\sigma^{M-4-2a},
 \quad \Theta=x\sigma^2,\quad y\sigma^4=-\sigma(2z)/2.
\tag{5}
$$
所以整个空间在原好普通位有界；这里不假设 $y\sigma^3$ 有界。
所有 p-有限 Fourier 门保全，(4)只是指定实际有限维系数空间。

## 2. 与原 Gaussian 对齐的完整局部模型

Yang 的极化保持 $X=\mathbf Q\delta$，有限加性角色保持
$\psi_{{\rm add},v}(x)=e^{-2\pi i\{x\}_v}$。
原输出对偶系数给
$$
 \alpha=\frac2{3150}=\frac1{1575},\quad
 \alpha=\frac{1/7}{15^2},\quad
 \kappa_\infty=|\delta^3\alpha|=\frac{\sqrt3}{525}.
\tag{6}
$$
因此到 R1038 的 $\alpha=1/7$ 模型是整个有理平方缩放
$\phi_{\rm new}(x)=\phi_{\rm old}(x/15)$，包括支撑、Haar、
Gaussian 和整个 Weil 核。不是只改一个 Hermitian 类。

固定基 splitting $\nu_0=\psi_0N^{-1/2}$，以下 $W_v$ 均是该
**完整 Hecke splitting** 的 torus 表示。它与裸有限 Weil 矩阵
的差在七处明确保留。

### 2.1 二处：两个真实 even 方向

令 $e_a=\mathbf1_{a/2+2\mathbf Z_2}$，
$f_A=e_0-e_2,\ f_B=e_1+e_3$。
因 $15^{-1}\equiv-1\bmod4$，原两偶向量在(6)的变换下不变。
$\alpha\equiv7\bmod8$，故 R1038(36)–(38) 的整个矩阵仍适用：
$$
 v_0=f_A-\frac{\sqrt3-1}{\sqrt2}f_B,\quad
 v_1=f_A+\frac{\sqrt3+1}{\sqrt2}f_B,\quad
 W_2(\omega)v_e=\omega^e v_e .
\tag{7}
$$
两个其它拓扑生成元 $-1,g_*$ 都固定它们；
范数为 $n_{2,0}=3-\sqrt3,\ n_{2,1}=3+\sqrt3$。
这里第二线用 R1040(115) 的同一相位，不能换成另一平方类的向量。

### 2.2 三处：整个九维，而非三个 principal 列

取 $s_3^2=1/7,\ s_3\equiv7\bmod9$。实际九个小球为
$$
 e_a^{(3)}(x)=\mathbf1_{a/9+\mathbf Z_3}(s_3x/15),
 \qquad a\bmod9 .
\tag{8}
$$
每个小球的 Haar 体积为 $1/3$，完整支撑是
$3^{-1}\mathbf Z_3$，周期为 $3\mathbf Z_3$。
R391/R1038 的原 Rao 核按(6)整体共轭。
在 $\alpha=1$ 的旧坐标，基 splitting 的
$g_*=(1+3\delta)/(1-3\delta)$ 作用为
$\omega^{-a^2}e_a$，$-1$ 为反射；
$\omega$ 的完整九列使用同一个 Rao 核。
三个生成元给有限群像，阶整除18。原 old 三列及六个单位列
都包括在(8)，不先限定偶性或 principal 角型。

对这个全群像的每个实际非零角色 $\tau_3$，定义
$$
 \Pi_{\tau_3}=\int_{K_3^1}\tau_3(t)^{-1}W_3(t)\,dt,\qquad
 f_{\tau_3}=\Pi_{\tau_3}e_{a(\tau_3)},\quad
 a(\tau_3)=\min\{a:\Pi_{\tau_3}e_a\ne0\}.
\tag{9}
$$
紧 Haar 的体积为一，所以这是一个完整有限和。
Yang(2.8)对 nonsplit $K_3/\mathbf Q_3$ 的整个
$\mathcal S(\mathbf Q_3)$ 给重数至多一；不是从一个三列压缩猜
重数。因此所有非零(9)准确分解整个九维(8)。
$\overline{W_3(t)}=W_3(t^{-1})$ 和原对称核使投影矩阵实，
故向量实、代数，其范数
$$
 n_{3,\tau_3}=\frac13\sum_{a\bmod9}f_{\tau_3}(a)^2>0
\tag{10}
$$
原样保留。这一定义不声称执行过新的九维数值分解。

### 2.3 五处：完整 old 加24个 wild 方向

本处 $\alpha=2/(126\cdot25)$。取
$s_5^2=1/126,\ s_5\equiv1\bmod125$，则同一局部平方变换将
模型准确化为 R1047(9)–(14)。在当前位置 $u=5y$ 上，小球为
$\mathbf1_{u+25\mathbf Z_5}$，每列范数平方为 $1/25$。
令
$$
 \mathcal T_5=(\mathcal O_K/25)^1,\quad
 g_5=-\omega(1+5\delta),\quad
 \tau_r(g_5)=\zeta_{30}^r .
$$
整个基 splitting 是
$$
 W_5(a+b\delta)_{uv}
 =\frac15\zeta_{25}^{\,3\{a(u^2+v^2)-2uv\}/b}
 \quad(5\nmid b),
\tag{11}
$$
其它群元沿同一个 Schrödinger 表示。
全 trace 和投影已在 R1047 逐类支付：
$$
 V_5=\mathbf C v_{\rm old}\oplus
       \bigoplus_{5\nmid r}\mathbf C f_r,\qquad
 v_{\rm old}=\mathbf1_{5\mathbf Z/25}.
\tag{12}
$$
$f_r$ 保原最小非零投影列，不规范成单位范数。
真实 Haar 范数为
$$
 n_{5,{\rm old}}=1/5,\qquad
 n_{5,r}=\frac1{25}\sum_{u\bmod25}f_r(u)^2>0 .
\tag{13}
$$
所有24个新角色在 $1+5\mathcal O_K$ 非平凡，不能只留
unitary 两支差中的十二个 odd 字。

### 2.4 七处：同一固定向量及 split 非紧参数

原 N 主型在整个六变量来源中与 Y 的七处 Heisenberg 配对
收缩，R1040(112)–(113)已支付其唯一结果为 R1038 的 $f_7$。
这里还须核(3)的有理角没有改该向量。

记原自然 Y/K Schrödinger 坐标为 $y,k$，R1038 的最小
Y 坐标为 $x_{\rm old}=y/3$；新的整坐标为 $u=5y,v=5k$。
在 $g_0^\epsilon$ 拉回后准确有
$$
 x_{\rm old}=\frac{2u+21\epsilon v}{75},\qquad
 k_{\rm old}=\frac{-\epsilon u+2v}{25}.
\tag{14}
$$
七处第二个伙伴是整球。这个变换 determinant 为七处单位，
在整支撑上第一式模7为 $x_{\rm old}\equiv-u$。
$f_7$以 $7\mathbf Z_7$ 为周期、且为偶函数，所以
整个七处张量仍是 $f_7(u)\mathbf1_{\mathbf Z_7}(v)$，
保其余伙伴；两支都相同。这里使用了实际坐标倍率，
不是以“原行正交”代替局部核验。

具体保
$$
 f_7(a)=\sqrt7\mathbf1_{a=0}
   +i(\omega^2\zeta_7^{2a^2}-\omega\zeta_7^{-2a^2}),\qquad
 n_7=3(7+\sqrt{21})/7 .
\tag{15}
$$
在裸有限 Weil 模型中其特征是 $t\mapsto t$；
相对本注固定的 $\nu_0$ Hecke splitting，其特征是
$$
 \tau_7(t)=t^{-2},\qquad t=x+2y\in\mathbf F_7^\times .
\tag{16}
$$
这是 natural quadratic splitting 的 $t^3$ 比值，
不能把裸特征直接当有限 Hecke 角色。
Yang(2.28)的完整 isometry将(15)送到
$\vartheta^{-1}\mathbf1_{\mathbf Z_7^\times}$，
$\vartheta(u)=\operatorname{Teich}(u)^2$，连同原非零比例。
非紧 uniformizer 移到不交环带，未声称逐向量固定。
原 Corollary2.13 的紧投影及 Haar 费用仍为
$$
 c_7(0)=7/6 .
\tag{17}
$$
所以后面的范数公式适用于这一个实际向量，包括非紧参数。

## 3. 满空间识别与完整角色，不据好位谱命名

允许七处全七维时，上述有限模型的维数为
$2\cdot9\cdot25\cdot7=3150$。
其有理支撑为 $x=n/6$，完整系数序列满足
$$
 a_{n+6300}=a_n,\qquad (-1)^n a_{n+3150}=-a_n .
\tag{18}
$$
对于(15)的实际子空间，局部标签
$\ell=(e,\tau_3,r_5)$给
$$
 a_{\ell,n}
 =v_e(n\bmod4)\,
 f_{\tau_3}(7n\bmod9)\,
 f_{r_5}(21n\bmod25)\,
 f_7(6n\bmod7).
\tag{19}
$$
三处的7来自 $s_3/10\equiv7\bmod9$，其余也由 $x=n/6$
直接读取。所有列实且代数；CRT给每个非零 tensor 一个非零序列。
整个 theta 为
$$
 S_{\ell,\Lambda}(Z)=e^{3150\sqrt3\pi Z^2}
 \sum_{n\in\mathbf Z}a_{\ell,n}
 e^{\,\pi i(\delta/3)n^2/6300+2\pi inZ}.
\tag{20}
$$
由(18)换指标验证它恰在原 standard even $S_{3150}$；
Fourier 频率唯一性给单射，完整维数给满射。
故原(3)在 N 投影后属于(19)的
$2\cdot9\cdot25=450$维完整子空间。
有限 p 门及 K/A/H/J 的 jets 不会引入另一个七处向量。

令 $r_\ell\bmod6$为(20)实际 $\mu_6$ 角型。
所有 local torus projectors 与原 theta-group 作用相容，
所以每个(19)有唯一角型；不预设它为5。
对于有限坏位的单位，定义
$$
 \eta_{\ell,v}(u)
  =\nu_{0,v}(u)^{-2r_\ell}
       \tau_{\ell,v}(u/\bar u)^{-1},
 \quad v=2,3,5,7 .
\tag{21}
$$
这里二处用(7)、三处用(9)、五处用(12)，七处用(16)；
在其它有限处不分歧。二处明确为
$\operatorname{Teich}^{r_\ell+e}$，五处为
$\tau_{r_5}(u/\bar u)^{-1}$。
七处在固定 split 识别 $(u_1,u_2)$ 下是
$\vartheta(u_1/u_2)$；在各自 residue embedding 中对应
R1038(27)的两个 $u^2$，两个根单位嵌入不可混同。

原全局 $\mu_6$ 协变与(20)的角型恰给
$\prod_v\eta_{\ell,v}(\zeta)=1$。
类数一遂将(21)唯一延伸为固定有限 Hecke 角色：
$$
 \eta_\ell((z))
   =\prod_{v\mid2\cdot3\cdot5\cdot7}
                     \eta_{\ell,v}(z)^{-1}
 \quad((z),2\cdot3\cdot5\cdot7)=1 .
\tag{22}
$$
所有 uniformizer 用主 idèle 条件定义，不自行设为1。
特别 $\eta_{\ell,2}(2)=\eta_{\ell,5}(5)=1$。
明确写 $\sigma_3=\tau_3(-1),\sigma_5=\tau_5(-1)$（old 时 $\sigma_5=1$），
完整 theta parity 给 $(-1)^{r_\ell}=\sigma_3\sigma_5$。
$\delta$ 在二处为1模2，七处两支之比为 $-1$ 且 $\vartheta(-1)=1$，
所以原主 idèle 条件准确给
$
\eta_{\ell,3}(\delta)=\sigma_5=(-1)^{r_\ell}\sigma_3,
\quad \Phi_{\ell,m,3}^{\rm un}(\delta)=i\sigma_3,
\quad \nu_{\ell,\chi,3}^{\rm un}(\delta)=-i\sigma_3.
\tag{22a}
$
最后一式在下文(33)的存活分支读取；它正是完整逆角色值。
此处 $\sigma_3$ 不与(8)的平方根 $s_3$ 混同。
(21)在有理单位上平凡，因而
$$
 \eta_\ell^c=\eta_\ell^{-1},\qquad
 \eta_\ell|_{\mathbf A_{\mathbf Q}^{\times}}=1.
\tag{23}
$$
全部导子固定有界于 $(350\delta^4)$。
五处 old 时无五处分歧，new 时恰为25；
七处两个导子都恰一次；正权二处始终分歧；
三处保全 conductor 从 $\delta$ 到 $\delta^4$ 的可能性。

实际正权族为
$$
 \Phi_{\ell,m}=\eta_\ell\psi_0^{\,2m+1},
       \qquad m\ge0,\quad m\equiv r_\ell\bmod6 .
\tag{24}
$$
在 nonsplit 二、三、五处，(21)与完整 uniformizer将原
$W_v$特征 $\tau_{\ell,v}$逐个取消；
这是 Yang 原(2.18)的真实 test-vector 条件。
三处的全 $-1,\omega,g_*$ 和 $\delta$ 都已包括。
七处则用(15)–(17)的实际 compact projection。
因此完整 positive root sign 为+，其局部平方条件都满足。
没有由首几个 Hecke 特征猜一个角色，也没有将 split
$\mathcal S(\mathbf Q_7)$错误套 nonsplit 重数一。

## 4. 全权平方及固定代数规范

按原第一个非零 Taylor 系数规范
$$
 S_{\ell,\Lambda}(Z)=s_\ell F_{\ell,1}(\Omega_0Z),\qquad
 [z^{o_\ell}]F_{\ell,1}=1,\quad0\le o_\ell\le3150,\quad
 o_\ell\equiv r_\ell\bmod6 .
\tag{25}
$$
代数 theta-group和完整有限投影给
$F_{\ell,1}\in S_{3150}(\overline{\mathbf Q})$；
首系数规范不加入任意 $\mathbf C_p$ 系数。
$s_\ell$为实数或纯虚数，依 $o_\ell$ 奇偶。

令 $h_\infty=\sqrt{\kappa_\infty}/(12\pi i)$；
原 Hermite 生成式给
$$
 b_{\ell,m}=\sum_n a_{\ell,n}
  H_m(\sqrt{\kappa_\infty}\,n/6)
       e^{-\pi\kappa_\infty n^2/36}
   =m!s_\ell(\Omega_0h_\infty)^m d_{\ell,m},
 \quad d_{\ell,m}=[z^m]F_{\ell,1}.
\tag{26}
$$
它是同一来源的实数。完整平方范数为
$$
 \mathcal N_{\ell,m}
  =\frac{n_{2,e}n_{3,\tau_3}n_{5,r_5}n_7}
          {\sqrt{2\kappa_\infty}}\frac{m!}{(4\pi)^m}.
\tag{27}
$$
三处 ramified quadratic extension 不列入 Yang 的 unramified
坏集合；五处 old/new 分别保
$$
 c_\ell^{\rm loc}(0)=\frac79
       \begin{cases}1,&r_5={\rm old},\\5/6,&r_5\ne{\rm old}.
       \end{cases}
\tag{28}
$$
二处 $2/3$、七处(17)和全体积比6全已在(28)及下式中。
Yang Theorems2.6、2.15给
$$
 \begin{split}
 L(\Phi_{\ell,m},m+1)
 &= C_\ell\frac{(4\pi)^m}{m!}\,b_{\ell,m}^2,\\
 C_\ell
 &=\frac{2}{6c_\ell^{\rm loc}(0)}
       \frac{\pi}{3\sqrt3}
       \frac{\sqrt{2\kappa_\infty}}
            {n_{2,e}n_{3,\tau_3}n_{5,r_5}n_7}>0 .
 \end{split}
\tag{29}
$$
这包括每条实际局部范数，不以“非零常数”抹去新五处费用。

写 $s_0=(1-\omega)^{-1},\ \varpi_0=s_0\Omega_0$。
$$
 h_\infty^2=-\frac{\sqrt3}{24\cdot3150\pi^2},\qquad
 s_0^{-2}=-3\omega
$$
使(26)–(29)严格化为
$$
 \mathscr E_{\ell,m}:=
 \frac{(2\pi/\sqrt3)^mL(\eta_\ell\psi_0^{2m+1},m+1)}
 {m!\varpi_0^{2m+1}}
 =c_\ell3150^{-m}d_{\ell,m}^2,
\quad
 c_\ell=3150^{o_\ell}\mathscr E_{\ell,o_\ell}
       \in\overline{\mathbf Q}^{\times}.
\tag{30}
$$
首系数1与(29)支付非零，原 CM 临界值代数性支付代数性；
$c_\ell$在取 p、n、有限字符以前固定。
没有逐权选平方根或未定 Iwasawa 单位。

取原 $t=17^{1/6}>0$，在物理 $b=17$ 模型上严格有
$$
 F_{\ell,17}(z)=t^{-o_\ell}F_{\ell,1}(tz),\quad
 \Omega_{p,0}=t\Omega_p,\quad
 \nu_{F_{\ell,1}}=t^{o_\ell}\nu_{F_{\ell,17}} .
\tag{31}
$$
物理积分变量没有被 t 缩放。(3)的 $z/5$ 另保真实
$D_{1/5}$推前；负一 $\chi$ 矩因而乘
$5\chi(5)^{-1}$，是明确代数因子。

## 5. 所有 physical finite-p 字与真实 root sign

固定原合格普通 $p>1296$，且 p 不在原固定有限坏集。
对任意有限 $\chi:\mathbf Z_p^\times\to\overline{\mathbf Q}^{\times}$
定义
$$
 I_{\ell,\chi}
  =\int_{\mathbf Z_p^\times}x^{-1}\chi(x)
                             \,d\nu_{F_{\ell,17}}(x).
\tag{32}
$$
它除非
$$
 \chi(\zeta)=\zeta^{r_\ell+1}\quad(\zeta\in\mu_6)
\tag{33}
$$
否则为零。对存活字符令
$$
 \Gamma_0=\widehat\psi_0/\widehat{\bar\psi}_0,\quad
 \rho_{\ell,\chi}=\eta_\ell(\chi\circ\Gamma_0),\quad
 \nu_{\ell,\chi}=\psi_0\rho_{\ell,\chi}^{-1}.
\tag{34}
$$
保(22)所有 uniformizer；这不是只给 p 惯性的定义。

R778§7的解析证明逐项用于(30)，其前提(5)的整个有界测度已付。
正权原两个 ordinary Euler 因子都是
$$
 1-\eta_\ell(\mathfrak p)
             \frac{\alpha_p^m}{\bar\alpha_p^{m+1}},
 \quad\alpha_p=\psi_0(\mathfrak p).
$$
在同一 tame 分支沿正整数
$m_h=m_0+(p-1)p^h$取极限，再用解析唯一性；
不把 wild 字写作整数幂的收敛列。
得到完整 primitive Katz 身份
$$
 \boxed{\mathcal K_{\mathfrak f_\ell}
       (\widehat{\bar\psi}_0\rho_{\ell,\chi})
 =3150c_\ell t^{2o_\ell+1}\Omega_p
             \chi(3150)^{-1} I_{\ell,\chi}^{\,2}.}
\tag{35}
$$
正 p 导子时使用实际 ramified Gauss 因子；
五处是惰性位，old 只有一个完整局部因子
$(1+1/5)^{-1}=5/6$，new 保真正25导子而局部因子为1。
这里 $\mathfrak f_\ell$ 采用各来源的最小 primitive 模数，所以 old
的 $5/6$ 已在完整 $L$ 值中，不另乘；若改用统一含5的模数，必须
另显示 $6/5$ 的去 Euler 费用。目标 p 的两个分裂 Euler 因子
不应搬到五处。
其它所有固定坏因子按(24)原样保留。

根数还需处理七处，不能只说“有限角色取共轭”。
正权(24)的无穷 epsilon 是 $i(-1)^{r_\ell}$，
全部有限乘积遂为 $-i(-1)^{r_\ell}$。
在二、三、五处，(33)使目标(34)的单位与 uniformizer
准确成为正权 unitary 角色之逆。
在七处，单位确实取逆，但 uniformizer 可另含随 p、$\chi$
变化的 unramified 倍率。两个分裂支的该倍率互逆，
且两个 conductor 均为1；Tate epsilon 的 unramified-twist
公式使这两个倍率完全相消。
等价地，其完整 paired epsilon 只等于
$\nu_{\mathfrak q}(-1)$，不取决于非紧参数。
这是本注保 R1038(27)而不能把两个 uniformizer 设成1的原因。

用 $\epsilon(\lambda)\epsilon(\lambda^{-1})=\lambda(-1)$，
以及全部旧有限 $\prod_v\Phi_{\ell,m,v}(-1)=-1$，
目标旧有限乘积仍为 $-i(-1)^{r_\ell}$。
新增 p 的两个 Gauss 因子乘积为 $\chi(-1)$，
无穷处为 i，故
$$
 \boxed{w(\nu_{\ell,\chi})
   =(-1)^{r_\ell}\chi(-1)=-1.}
\tag{36}
$$
这包括完整 wild 三处及任意 finite-p 字，未忽略 split 七处。

## 6. 全部有限负一值的实际代数点载体

R774已证明的全 wild 三处/p 版本、原 BDP2 特殊值比较及
LZZ局部非零因子现逐项适用：中心角色是
$\epsilon_KN$，(36)为负根数，(34)有固定 type $(1,0)$。
于是存在原点因子
$$
 P_{\ell,\chi}\in
 E_0(H_{\rho_{\ell,\chi}})_{\mathbf Q}
                     \otimes_K\overline{\mathbf Q},
 \qquad g_{\rm pt}P_{\ell,\chi}
       =\rho_{\ell,\chi}(g)P_{\ell,\chi},
$$
以及明确非零代数系数 $A_{\ell,\chi,p}$，使
$$
 \boxed{\Omega_p I_{\ell,\chi}
       =A_{\ell,\chi,p}\log_{\omega_0}P_{\ell,\chi},\qquad
 A_{\ell,\chi,p}^{\,2}
 =\frac{\epsilon_{\ell,\chi,p}\chi(3150)}
 {3150c_\ell t^{2o_\ell+2}}\in\overline{\mathbf Q}^{\times}.}
\tag{37}
$$
$\epsilon_{\ell,\chi,p}$为 R774 的完整 primitive Gauss、
Euler与局部 pairing 比值；其非零与全部原假设已由同一定理支付。
(37)包括零点和零值；没有据来源非零宣布各个点非挠。

在 p 的两个惯性群，点角色分别是
$\chi^{-1},\chi$，沿 R778 的同一 reciprocity。
在五处，它是 $\tau_{r_5}(u/\bar u)^{-1}$；
$\Gamma_0$在五处未分歧。因此只有 $r_5={\rm old}$
能通过五处的点惯性平均，只有 $\chi=1$ 能通过 p 的点惯性平均。
这里固定所有代数标量，即使它们所在的系数域在5或p处分歧。

R749 的 Fuchs–Pham 对数单射已使这个 point-only 动作在任意
**有限**完整代数点和的对数上有定义。
各点域是有限 abelian ray 域；对其复合域的两个惯性群作有限平均，
得到可交换投影 $\Pi^{\rm pt}_5,\Pi^{\rm pt}_p$。
没有把普通 Galois 对 $\mathbf C_p$ 系数的动作冒称 point-only。

## 7. 原 K/Y 读者确实是上述有限点和

取原允许 $h_{\rm bad}\mid n$，保
$d_n=(p-1)p^{n-1}$及 $\kappa=p\lambda^2,\beta=-\lambda$。
原全 p-character 返回逐字是
$$
 \nu_{E_\theta\phi_n^\epsilon}|_{Y^\times}
 =\frac{\beta^{-n}}{d_n}\theta(\epsilon/2)\,
 (D_{K,\kappa^{-n}})_*
  \bigl[\mathbf1_{Y^\times,K^\times}
           \theta(Y/K)\,\mu_{-\epsilon}\bigr].
\tag{38}
$$
测度式尚未读取 K/Y；该读取的 $\kappa^{-n}$ 因子在下文保留。
$\mu_{-\epsilon}=(g_0^{-\epsilon})_*\nu$就是(3)的实际来源。

对 K/Y 读取，(38)先给有限个 Y 负一
$\theta(Y)$矩与 K 正一 $\theta(K)^{-1}$矩。
同一个 p-有限门展开为有限 Fourier 和。
R745 的原 Mumford/Bannai外积公式给 K 的这些正一 jets
除共同 $\Omega_p$ 后均为代数数；
其它伙伴的零 jets和全 $\mathscr P_3$也保代数系数。
正交外积使 p-挠平移留在 K 因子，不向 Y 暗添另一个 p-flat twist。
Y 因子仍是(3)、(19)的整个空间，物理字符恰是所显示的
$\chi=\theta$。包括 $D_{1/5}$ 在内的坐标倍率都代数且已显示。

因此
$$
 L_n^\epsilon:=
 \int_{Y^\times}\frac K Y\,d\nu_{\phi_n^\epsilon}
\tag{39}
$$
是(37)中点对数的**有限**代数线性和。
相反的 K 字可以在对角自然 Galois 作用中抵消 Y 字，
却不能在此 point-only 投影中抵消，因为它是被固定的代数系数。
这精确支付原 unitary§14.6 不能删 p-new 的障碍。

(12)的 full Bell 配对使 Y 的5-old当且仅当 K 的5-old，
不因其它坏位不同而改成只保十二个 odd 字。
故在同一个(39)上，
$$
 \boxed{\Pi^{\rm pt}_5\Pi^{\rm pt}_p L_n^\epsilon
     =\int_{Y^\times}\frac K Y\,
                  d\nu_{E_{5,{\rm old}}E_0\phi_n^\epsilon}.}
\tag{40}
$$
两个投影均只在本段已付的有限点和上使用，不推广到中央 log 的无限尾。

## 8. 消费原已证 old 返回，得到全读者非零

原 unitary(58)与§15的完整 old 比较保全部两支、K/A 类型：
$$
 \boxed{\begin{aligned}
 \Pi^{\rm pt}_5\Pi^{\rm pt}_p L_n^+
  &=\frac{\beta^{-n}\kappa^{-n}(1-\beta\kappa)}
               {5d_n}\,\frac{10\delta}{7}\,
                         \Omega_p I_{D,p}\ne0,\\
 \Pi^{\rm pt}_5\Pi^{\rm pt}_p L_n^-&=0 .
 \end{aligned}}
\tag{41}
$$
原 $I_{D,p}$由固定 E21609 的真实非挠点及完整点因子定理支付，
不重算其非消失；$1-\beta\kappa\ne0$，其余显示因子也非零。
因此
$$
 \boxed{L_n^+\ne0,\qquad L_n^+-L_n^-\ne0.}
\tag{42}
$$
全部5-new和p-new已成为真实分歧点载体后才被(40)投影消去；
没有从 natural diagonal inertia 直接删项。

全 p 字的另一已付表达仍是原有理核
$$
 L_n^\epsilon
 =\int_{Y^\times}
   \frac{\epsilon\kappa^{-n}Y+2K}
        {2Y-21\epsilon\kappa^nK}\,d\nu ,
\tag{43}
$$
保原变量与整 unit 域。所以(42)是同一真实来源的有限读者结论。

原 canonical 坏条件尚未在这个**相同**读者上给零。
下一消费必须用原完整测度身份、全部 companion与补域建立该条件；
不能把(42)、另一角导数、某个非零点或首系数直接宣称为
rank2 的 $J'(0)\ne0$。原无限 p-adic logarithm 尾也仍不在
本注有限 point-only 投影的定义域内。

## 来源与验证范围

- 原 unitary 全字 §§10–15、全 p-character 返回 §4：同一3150/150来源、
  逆 Gram、所有 p 字、5-old两支和实际 K/Y 读数。
- R391、R1038 §§9–11、R1040 §14、R1047 §2：原二/三/五/七
  全有限模型、Haar、splitting及全局 Gaussian；本注按(6)、(14)
  支付新来源的真实坐标，而未重跑旧producer。
- R745：原完整有限 p 门的代数外积/正交伙伴 jets。
- R774、R749、R778 §§7–8：primitive Katz/点因子、有限点和
  对数单射与 point-only 动作。
- T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math.485
  (1997), (2.8)、Theorem2.6、Corollary2.13、Theorem2.15及(2.28)：
  <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
  split 七处只使用本注(15)–(17)的真正测试向量，不套任意Schwartz。
- T. Yang, *Eigenfunctions of the Weil representation of unitary group of one
  variable*, 作者全文：<https://people.math.wisc.edu/~tonghaiyang/lattice.pdf>。

本注只有原来源上的手工有限恒等式、角色和全权解析证明；
没有新增数学执行、未声称新矩阵run，也没有删除任何原日志中的失败或开放门。
