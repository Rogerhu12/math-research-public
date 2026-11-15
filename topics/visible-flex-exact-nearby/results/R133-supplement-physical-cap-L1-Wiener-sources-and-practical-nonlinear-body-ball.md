# R133 续篇：物理帽的 L1 Wiener 普通源与实际非线性主体球

2026-11-15，visible-exact / root。

**已证明下述完整源门、二阶代数界与实际仿射负荷。** 同一 ac1 连续修补中心的逐模双端核可直接消费径向 $L^1\mathcal A_0$ 源，不要求先取每个 Fourier 系数的全径向 supremum。原已成7296行的残差因此给实际未闭 Green 负荷小于 $1.2\,10^{-6}$，落入半径 $2^{-15}$ 的明确主体收缩预算。

这不证明真实外端 $C_R$ 保持在已付输入球。该端点保持条件在第7节单独列出；它未完成前，不宣称完整非线性帽 BVP、全体/尾匹配或精确族存在。本文只作解析消费，没有重算原 target、残差包络或参考核。

## 1. 同一物理对象与不同范数

固定 $\eta=\eta_0$、$\delta=0$ 及原精确 $\alpha,\nu$。候选 SHA 为 ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413；准确连续修补定义 SHA 为440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47。帽区间 $I=[L,R]=[9/10,25/8]$。

记修补中心的真实物理曲率为 $\widehat W=(\widehat B,\widehat C)$，全部mean、inverse angle及修补路径使用[连续物理帽](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md) C.1--C.18。旧M64/.65中心的精确解不能移到此对象。

未知 $x=(b,c)$ 使用完整 joint Wiener 空间
$$
 \|x\|_{\mathscr X}=\sum_{k\in4\mathbb Z}\sup_I|b_k|
                         +\sum_{k\in4\mathbb Z}\sup_I|c_k|.
 \tag{A.1}
$$
对普通物理源使用
$$
 \|F\|_{\mathscr L}=\int_L^R\sum_{k\in4\mathbb Z}|F_k(r)|\,dr.
 \tag{A.2}
$$
两个mean都包含。$\mathscr L=L^1_r\mathcal A_0$ 不是 joint norm，也不是 $L^2_rL^2_\theta$；不将sup移过求和。

$f_B$ 是原long另一端的归一非mean高度，物理高度为 $s_Bf_B$、$s_B=a_Bw_B>0$；独立mean高度/通量另保。实际入口取原反射背景及 $\|f_B\|_{\dot{\mathcal A}^2}\le2^{-60}$。算子门仍保一般 $4\mathbb Z$ 方向和两曲率mean。

## 2. 原逐模核直接给完整 L1 源门

使用[实际全模物理帽](R133-supplement-actual-final-all-mode-physical-cap-Green.md) C.12--C.25。对 $M=|k|\ge4$，置
$b_k^{\rm ref}=i\operatorname{sgn}(k)b_k$、$d_k=b_k^{\rm ref}+q_Mc_k$。准确两行是
$$
 \begin{aligned}
 d_k'&=A_Dd_k+(-M\gamma+q_M\beta)Q_k+F_{b,k}+q_MF_{c,k},\\
 c_k'&=-A_Cc_k+M\gamma d_k+\beta Q_k+F_{c,k},
 \end{aligned}
 \tag{A.3}
$$
$A_D\ge Ms_D>0,\ A_C\ge Ms_C>0$；$d$从右、$c$从左积分。原实际比较给
$$
 q_M<1.389936764<1.39,\quad T<3.625263015,\quad
 H_D=1+(1+q_+)T<10,\quad H_C=1+q_+<3.
 \tag{A.4}
$$
$T$ 是真正变系数 $d\to c$ 核的总质量界。

暂令 $Q$ 和端值为零，只估独立普通源。标量指数核点值不超过1，故
$$
 \sup_I|d_k|\le\|F_{b,k}\|_1+q_+\|F_{c,k}\|_1,\qquad
 \sup_I|c_k|\le T\|F_{b,k}\|_1+(Tq_++1)\|F_{c,k}\|_1.
$$
再由 $b_k^{\rm ref}=d_k-q_Mc_k$，pair增益为 $H_D$、
$H_Dq_++H_C<17$。mean另解原C.19；$\beta<0$使其从右积分的指数核点值也不超过1，因此各ordinary源增益不超过1。全部频率同时得到
$$
 \boxed{\ \|\mathcal G_{\rm ord}(F_B,F_C)\|_{\mathscr X}
          <10\|F_B\|_{\mathscr L}+17\|F_C\|_{\mathscr L}.\ }
 \tag{A.5}
$$
这是先对完整径向积分用正核，再用Tonelli的
$\sum_k\int|F_k|=\int\sum_k|F_k|$；没有以 $L^\infty_r\mathcal A_0$ 冒joint范数。

角散度/非线性 $Q$ 列仍消费已成质量门
$$
                            \|\mathcal G_Q\|<16.
 \tag{A.6}
$$
(A.5)不把裸角导当同范数ordinary源。独立jump/BV原子按原次序付
$10\sum\|j_B\|_{\mathcal A_0}+17\sum\|j_C\|_{\mathcal A_0}$。
原端值付 $3\|\gamma_{\ne0}\|+10\|e_D\|+|e_{B0}|+|e_{C0}|$；
两mean及内端输出不删。

## 3. 真非线性残差与固定r的完整换角

在修补moving中心记真实残差为 $R=(R_u,R_v)$。准确非线性协变是
$$
 F^{\rm phys}=D\Psi R=PR-\widehat W_\theta I_\theta(\widehat C R_v),
 \qquad
 P=\begin{pmatrix}\widehat C&-\widehat B\widehat C\\0&-\widehat C^2\end{pmatrix}.
 \tag{A.7}
$$
$R$在同一$r$拉回物理角。$D^2\Psi[R,h]$只在线性化共轭出现，不能再加到(A.7)。

这里的$R$是实际反射残差：$R_u$奇、$R_v$偶，$\widehat C R_v$为偶函数、$I_\theta(\widehat C R_v)$为奇函数。因此一般全$4\mathbb Z$第一微分中的独立weighted primitive相位常数在本式准确为零。(A.5)的普通源门仍是全$4\mathbb Z$门；(A.7)的简写不另行授予任意非反射源同一相位约定。

原完整moving残差有96标签支撑，即物理频率不超过384；连续修补仍是同有限状态及完整三次项。对固定$r$，实际inverse-angle位移满足
$\|h_r\|_{\mathcal A_0}<1/256$。完整指数卷积给
$$
 \|R_i(r)\circ(\mathrm{id}+h_r)\|_{\mathcal A_0}
 \le e^{384/256}\|R_i(r)\|_{\mathcal A_0}
 <5\|R_i(r)\|_{\mathcal A_0}.
 \tag{A.8}
$$
该不等式在积分前逐个固定$r$使用，故没有额外96倍费用，也不涉及未知物理系数的sup/sum交换。

原修补路径的完整joint系数可向外宽取
$\|\widehat C\|<1/3,\ \|\widehat B\|<1/128$，
$\|\widehat B_\theta\|,\|\widehat C_\theta\|<1/32$；
$\|I_\theta\|_{\mathcal A_0\to\mathcal A_0}=1/4$，mean准确排零。
由(A.7)--(A.8)，
$$
 \begin{aligned}
 \|F_B^{\rm phys}\|_{\mathscr L}
 &\le\tfrac53\|R_u\|_{L^1\mathcal A_0}
                         +\tfrac5{192}\|R_v\|_{L^1\mathcal A_0},\\
 \|F_C^{\rm phys}\|_{\mathscr L}
 &\le\tfrac{655}{1152}\|R_v\|_{L^1\mathcal A_0}.
 \end{aligned}
 \tag{A.9}
$$
直接项 $-\widehat C^2R_v$ 的mean保留；primitive的mean零不删它。因此未闭reference Green负荷满足
$$
 \eta_{\rm body}
 <\tfrac{50}{3}\|R_u\|_{L^1\mathcal A_0}
                     +\tfrac{11435}{1152}\|R_v\|_{L^1\mathcal A_0}.
 \tag{A.10}
$$

## 4. 消费已成whole残差，准确另付repair

[全部7296闭行的实际残差](../notes/2026-11-14-R133-final-complete-moving-residual.md)给原标准化量
$$
 \|R_U\|_{L^1\mathcal A_0}<3.042614\,10^{-8},\qquad
 \|R_V\|_{L^1\mathcal A_0}<5.237515\,10^{-8}.
 \tag{A.11}
$$
该证书覆盖全$[0,25/8]$、所有mean和真实graft，共同参数仅$\eta_0$。
完整原merged4592623B，SHA6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1。
这里仅引用已成两个数，不重新合并或重算旧行。

限制到帽只减小积分；物理moving残差乘 $0<\alpha<1$。原连续帽C.35另给每点pair修补残差差 $<4.285\,10^{-15}$，乘帽长 $89/40<3$ 后可宽取
$$
 \|R_u\|_{L^1(I)\mathcal A_0}<3.1\,10^{-8},\qquad
 \|R_v\|_{L^1(I)\mathcal A_0}<5.3\,10^{-8}.
 \tag{A.12}
$$
将这两个有理上界代入(A.10)，严格得到
$\eta_{\rm body}<1.1\,10^{-6}$。

修补值及所有角导在原接口准确相等，物理角也相同，故本中心无额外value-jump源。原中心6143接口预算没有改名为repair接口；独立方向跳仍保真实jump列。

## 5. 原真外端非线性残差的repair转授

[实际regular端口](R133-supplement-final-moving-centre-actual-regular-boundary.md)F.17--20在同ac1给
$$
 \|Z_0\|_{\mathcal A_0}<2.532986\,10^{-13},\qquad
 \|J\widehat B+q_{\rm true}Z_0-d(Z_0,f_B)\|<1.258388\,10^{-15},
$$
$$
 |\widehat C_0-C_{\rm ref}-c_0(Z_0,f_B)|<2.048004\,10^{-19},
 \qquad \widehat B_0-b_0(Z_0,f_B)=0.
 \tag{A.13}
$$
最后一式用实际反射背景，不删除一般方向的$Db_0$。

原连续帽C.9在全repair路径付
$\|\Delta C(R)\|<4.970\,10^{-19}$、
$|\Delta C_0(R)|<7.898\,10^{-23}$。
同路径pair修补在物理角 $<5\,10^{-18}$。
$D\Psi$第一行给
$$
 \|\Delta B(R)\|
 \le\tfrac13\|e_u\|+\tfrac1{192}\|e_v\|<2\,10^{-18}.
 \tag{A.14}
$$
[完整物理帽尾Schur](R119-supplement-complete-physical-cap-tail-Sobolev-Schur-with-all-mean-charges.md)L.6的真Wiener列为
$Dd<1/1024,\ Dc_0<1/8192$；原完整$\|q_{\rm true}\|<1$。
沿repair路径积分，得同440866中心
$$
 \boxed{\ \|r_D\|<1.3\,10^{-15},\quad
                |r_{C0}|<2.05\,10^{-19},\quad r_{B0}=0.\ }
 \tag{A.15}
$$
$C_0$修补、$Dc_0\Delta Z$及正的regular尾费均在内。

若内侧非mean曲率规定为中心自身，则$\gamma=0$。加(A.15)的原endpoint gains后，完整仿射负荷为
$$
                              \eta<1.2\,10^{-6}.
 \tag{A.16}
$$
一般$\gamma$加$3\|\gamma\|_{\mathcal A_0}$，独立mean荷、jump亦另加；
$f_B$及其mean高度不被改成innerheight Dirichlet数据。

## 6. 精确Gauss余项及完整二阶界

令 $c_{\rm bg}=\widehat C-C_{\rm ref}$，
$$
 Q(B,c_{\rm bg})=(B^2+\ell c_{\rm bg}^2)/(C_{\rm ref}+c_{\rm bg}),
 \quad \ell=K/C_{\rm ref}^2,\quad
 u=\widehat B/\widehat C,\quad v=1/\widehat C.
$$
同physical角已成joint门给$\|v\|<6,\ \|u\|<1/50$。

还可从原reference核严格读出$\sup\ell<1.39^2$。原producer
fourfold_codazzi_final_physical_cap_linear_module.py（SHA ef93be07b64bc6bf83be62b26f2a2e75e0f597dca3205401a6162826c3dcaf02）
逐行构造
$$
 q_{\rm hi}\ge(b_u+\sqrt{b_u^2+4\ell_{\rm hi}})/2
                    \ge\sqrt{\ell_{\rm hi}},\qquad b_u\ge0.
$$
原已成$q_+<1.39$因而支配每行$\ell_{\rm hi}$。$\ell$是径向scalar，其joint norm就是sup。完整
$Q_C=\ell-Kv^2-u^2$的joint norm小于.051432066，故
$$
                              \|Kv^2+u^2\|<2.
 \tag{A.17}
$$
这是原逐行构造的推论，非从任意Riccati解大小倒推$\ell$。

通分准确得
$$
 \boxed{\
 \mathcal R_Q(b,c)
 =Q(\widehat B+b,c_{\rm bg}+c)-Q(\widehat B,c_{\rm bg})-Q_Bb-Q_Cc
 =\frac{b^2-2ubc+(Kv^2+u^2)c^2}{\widehat C+c}.\ }
 \tag{A.18}
$$
mean保留完整卷积。若$\|x\|,\|y\|\le\rho\le1/1000$，则$\|vc\|\le6\rho<1$，
完整Neumann分母给
$$
 \boxed{\
 \|\mathcal R_Q(x)\|<13\|x\|_{\mathscr X}^2,\quad
 \|\mathcal R_Q(x)-\mathcal R_Q(y)\|
 <13(\|x\|_{\mathscr X}+\|y\|_{\mathscr X})\|x-y\|_{\mathscr X}.\ }
 \tag{A.19}
$$
分子是norm不超过2的对称双线性型。首系数
$12/(1-6\rho)<13$；差的完整系数可取
$12/(1-6\rho)^2<13$，包含分母改变。
无未知Fourier截断或高角小范数。

## 7. 实际主体球与独立的真外端保持

在原已付long输入球内，外端保完整nonlinear差
$d(Z_0+c_{\ne0}(R),f_B)-d(Z_0,f_B)$、$c_0$差和$b_0$差。
L.6和原真$b_0$门给Lipschitz系数$1/1024,1/8192,2^{-48}$；
原rotational/true regular差$\epsilon_q<2^{-500}$仍保。
于是同一未闭reference Green映射的线性及外边界总Lipschitz小于
$$
 16(.052)+10(1/1024+\epsilon_q)+1/8192+2^{-48}<17/20.
 \tag{A.20}
$$
各列只计一次，没有再次乘已闭帽resolvent。
完整帽映射$\mathcal T$在其真实定义域内满足
$$
 \|\mathcal T(x)\|\le\eta+(17/20)\rho+208\rho^2,\qquad
 \operatorname{Lip}_{\mathscr X}\mathcal T<(17/20)+416\rho.
 \tag{A.21}
$$
实际取$\rho=2^{-15}$。由(A.16)，$\eta<\rho/16$，故
$$
 \|\mathcal T(x)\|_{\mathscr X}<15\rho/16,\qquad
                         \operatorname{Lip}\mathcal T<7/8.
 \tag{A.22}
$$

但是$\rho$大于原$Z$输入球，不能在整个$\mathscr X$球上宣称$\mathcal T$有定义。
正确后验域还须带真端点门，例如
$$
 \mathcal B_{\rho,\zeta}
 =\{x:\|x\|_{\mathscr X}\le\rho,\
            \|c_{\ne0}(R)\|_{\mathcal A_0}\le\zeta\},
 \qquad \|Z_0\|+\zeta\le\bar Z,
 \tag{A.23}
$$
连同原long图的mean、height和参数门。该集合在$\mathscr X$中闭；
(A.22)只证明其主体norm不越界。还须证明
$$
 \|(\mathcal T(x))_{C,\ne0}(R)\|\le\zeta
                     \quad\hbox{对所有 }x\in\mathcal B_{\rho,\zeta}.
 \tag{A.24}
$$
它必须消费ordinary端点核、线性$Q$反馈、二次源及真实outer响应；
仅未闭ordinary源的端点界不足以证明(A.24)。
扩大$\bar Z$时重付原long image/Lip/mean与完整域门。
(A.24)及所有其余域门通过后，才可对同一闭集合使用(A.22)的contraction。

内侧给的是同physical角的非mean$C(L)$，$B(L),C_0(L)$为输出；
$B_0(L)$保完整通量行。它不是innerheight Dirichlet条件。
moving端口须由
$m_L=1/\langle C(L)\rangle_\theta$、
$\phi_L=\theta+m_LI_\theta(C-\langle C\rangle)+a_L$、
$v_L=1/C,\ u_L=B/C$及真实逆角读出；相位$a_L$独立匹配，
仅原反射奇相位可取零。普通$\mathcal A_0$小量不免费授未知逆角的同阶Wiener组合界。

该同身份实际负荷和主体球可继续用于端点保持与低范数存在性。
角正则bootstrap、全负体/尾height/flux/mean/Γ/ν匹配、C²连续精确族及几何验收仍须继续。
