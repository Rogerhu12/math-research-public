# R1199：原最高 packet 的全部普通尾交叉项及 CM 核上的完整 MW 首列

**现行范围更正（R1208，2026-11-28）：** 本文 §§1–5 的原 generic normal、全部交叉收缩及 opposite 无关性保持成立。§6 将 centre frame 与全局模 I 平凡化在整个 CM node 上直接识别，漏掉一个非恒定静态单位；因此三个支持 node 的贡献不能按旧论证删除，(1199.30) 的完整值等于 SS 和的身份由 [R1208](R1208-original-CM-node-boundary-and-corrected-highest-kernel-log.md) 替换。完整首值准确为 −8·2^mν/binom(m,n)²，仍是单位。以下旧正文的支持零贡献及完整 V 解释仅作更正前记录，不能继续消费；SS 公式本身继续使用。

## 更正前正文（按上方现行范围读取）


日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；root / global_route。

**已证明。** 原最高 packet 的每个所需 generic-tail normal 层都有显示的完整微分；其系数由 R1193 的首中心 $T_L\,db/(uA_p)$ 与 R1198 的同一周期比给出。全部较低 log 次数与较高 normal 的 Serre 配对化为一个准确有限收缩，所有交叉项都保留。这个完整收缩与 opposite line 的选择无关，尽管 R1198 的单项系数并不具有这种不变性。

对 R1197 完整 CM 轮廓的一维核
$T_*(b)=(b^3-1)^{2g-1}$，三个支持 CM 尾连同其节点过渡在所需首层的贡献严格为零。因此本文的全 supersingular 有限和恰是同一原 $P=(p-1)D_0$ 在这个指定向量上的完整首对数值，不只是一个 raw 节点输入。

本文没有证明该有限和为单位或非零，没有将原节点相位设为常数，也没有把整 packet 替成指定 $C$ 的单尖点型投影。Serre 主目标仍 OPEN。

## 1. 原对象、正常层及显示输入

保持 R1193、R1196–1198 的全部原对象：
$$
p=12g-1>37,\quad m=(p-1)/2=6g-1,\quad
e_0=m(p+1),\quad \pi_0^{e_0}=p,\quad\varepsilon=\pi_0^m,
$$
$$
P=(p-1)D_0,\qquad E_m=(e_{\tau_m}+e_{\mathrm{PS}_{m-1}})e_N.
\tag{1199.1}
$$
令 $\Omega_L$ 为权 $m^2$、负 deck 角色的实际 $E_m$-固定整 Hodge 提升，首中心仍为
$$
\overline{\pi_0^{-1}\Omega_L}|_I
 =\eta_T=\frac{T(b)}{uA_p(b)}\,db,\qquad
u^m=h_p(b)=r(b)^{2g}A_p(b),\quad r(b)=1-b^3,
$$
$$
T=T_L\in k[b^3],\qquad\deg T<m-1.
\tag{1199.2}
$$
在原无支撑尾 $s\in S=\{A_p=0\}$ 保留全部节点单位，记
$$
\tau_s=\lambda_s\rho_s,\qquad
\theta_s=\kappa_s\rho_s^m,\qquad
\tau_s^m=h_p'(s)\theta_s.
\tag{1199.3}
$$
最后两式由同一个
$z_sw_s=\rho_s\pi_0$、
$b-s=\kappa_sw_s^m+\cdots$、
$u=\lambda_sw_s+\cdots$
和 R1018 的实际商参数首项直接比较而来。

R1198 定义同一个 target period ratio
$\xi_s(t)=f_{1,s}(t)/f_{0,s}(t)$，其逆级数记为 $J_s(v)$。一切只读取次数小于 $p$ 的所需有限 jet。定义
$$
K_s(t)=
 \left(\frac{h_p(s+t)}{h_p'(s)\xi_s(t)}\right)^{1/m},
\qquad K_s(0)=1,
$$
$$
\mathcal E_{s,T}(t)
 =\frac{\xi_s(t)T(s+t)}
 {A_p(s+t)\xi_s'(t)K_s(t)},\qquad
e_{N,s}(T)=[v^N]\mathcal E_{s,T}(J_s(v)).
\tag{1199.4}
$$
这些都是合法单位根或有限幂级数：分子、分母在 $t=0$ 的简单零相消，$m$ 可逆。特别
$$
e_{0,s}(T)=T(s)/A_p'(s).
\tag{1199.5}
$$

使用 R1198 的同源有限 log 系数
$$
D_{a,s}
 =\frac1a[t^{a-1}]\lambda(s+t)
                 (t/\xi_s(t))^a,\qquad
\lambda=2G'/G=-6(b+1)/r.
\tag{1199.6}
$$
这里没有将单个 $D_{a,s}$ 的实际 $\alpha_s$ 任设为零。

对 $0\le N\le m-1$，记
$$
a_N=(-1)^N(N+2)!/2,\qquad
\gamma_{N,s}(T)=
 \frac{m\theta_s^N}{2\tau_s}\,e_{N,s}(T).
\tag{1199.7}
$$
在原 generic full 分支用
$$
U^2=V^{p+1}+A_s,\qquad
X=V^2,\quad Y=UV,\quad z_s=V^{-1},
$$
$$
\eta=\frac{dX_{\rm full}}{X_{\rm full}^{p}}
     =\frac{dY_{\rm full}}{Y_{\rm full}^{p}},
\qquad \Theta=X_{\rm full}^p\partial_{X_{\rm full}}
              +Y_{\rm full}^p\partial_{Y_{\rm full}},
$$
并保持 $\Theta V=2U,\ \Theta U=V^p,\ dF=(\Theta F)\eta$。定义
$$
F=V^{m-1},\qquad
\omega_{N,s}=\frac4{a_N}\Theta^NF\,\eta.
\tag{1199.8}
$$
$N=0$ 时正是原 $\omega_s^{\rm hi}=X^{(m-1)/2}dX/Y$。

本文的完整 generic normal 公式是
$$
\boxed{\quad
[\pi_0^{Nm}]\Omega_L|_{D_s}
 =\gamma_{N,s}(T)\,\omega_{N,s}
 \qquad(0\le N\le m-1).
\quad}
\tag{1199.9}
$$
左边使用 R1021 的实际非约化模 $p$ 仿射图读取整个系数微分，不只读最高极部。

## 2. 完整有限角像及实际极阶界

### 2.1 全部所需次数的一维图像

对 $0\le N\le m-1$，置
$$
D_N=(N+1)(p-1)-2,\qquad
M_N=\operatorname{Sym}^{D_N}(k^2)\otimes\det^{1-m}.
\tag{1199.10}
$$
沿 R1197 的同一个 Dickson 多项式 $C=X_{\rm full}^pY_{\rm full}-X_{\rm full}Y_{\rm full}^p$ 过滤。最大 $C$ 次数不超过 $m-1$，因为
$D_{m-1}=(m-1)(p+1)$。

每个非终端 quotient 的两个因子仍为
$$
S_j=W_{m-1-j},\qquad
T_j=W_{j+1}\otimes\det^m,\qquad
W_b=\operatorname{Sym}^{2b}(k^2)\otimes\det^{-b}.
\tag{1199.11}
$$
此时 $j\le m-2$。第一因子的 $N_{\rm ns}$-固定线只有偶 $b$ 时存在，R1195 把它分配到指标 $b+1=m-j$；所以实际 $E_m$ 只在 $j=0$ 的 $W_{m-1}$ 上贡献一维。第二因子要求 Cartan 单项式下标
$j+1\pm(m+1)$ 落入 $0,\ldots,2j+2$，无解。

终端若 $j\le m-2$，次数为 $p-3-2j\ge2$，也是上述第一因子；在 $j>0$ 时不给 $E_m$ 图像。唯一 $j=m-1$ 终端出现在 $N=m-1$，其次数与 twist 都为零，是平凡模，亦被 $E_m$ 杀掉。$N=0$ 时没有正次过滤，整个空间就是 $W_{m-1}$。幂等元取像 exact，故
$$
\boxed{\quad \dim\overline E_m M_N=1
                   \quad(0\le N\le m-1).\quad}
\tag{1199.12}
$$
这里保留真实整 packet，没有使用非整的单 cuspidal 投影。

由 R1193 的原低次 evaluation，$c^{1-m}F$ 被 $E_m$ 固定；$\Theta$ 等变且 $\Theta c=0$，所以
$c^{1-m}\Theta^NF$ 同样被固定。在无穷支，
$U\sim V^{m+1}$，第 $j$ 次微分给最高系数因子
$$
2(m-1+jm)=-(j+3)\quad\text{于 }k.
$$
因此总因子是准确的 $a_N$，且
$$
\omega_{N,s}=-2z_s^{-Nm}dz_s+\text{较低极阶项}.
\tag{1199.13}
$$
所有 $(N+2)!$ 都是 $p$ 单位。

### 2.2 极阶界适用于全部实际层

原 generic affine 图在整个 $R/(p)$ 上常数化，完整 level 换基为常线性；因此整 $E_m$ 逐 normal 层作用。当前 $Nm\le(m-1)m<e_0$，均在该精度内。

在所选实际 ordinary node，原 full 参数记为 $x,y$，$Q=s_{\rm Car}P_{\rm level}$、$s_{\rm Car}^2=-3$。同一个
$V=(y^2-s_{\rm Car}^2x^2)/\varpi^2$ 给
$$
z_s=V^{-1},\qquad W_s=\pi_0/z_s=y^2-s_{\rm Car}^2x^2,
\qquad z_sW_s=\pi_0.
\tag{1199.14}
$$
若采用 R1193 的已有 node 单位，此式的 centre 首系数正由 $\tau_s=\lambda_s\rho_s$ 保留。不能只在特殊纤维另选一个无关系的 plumbing 参数。

中心的首可能层是 $\pi_0^1$。在真实 node 中，中心第 $h\ge1$ 层 regular 项
$cW_s^j\,dW_s$ 转为
$-c\pi_0^{h+j+1}z_s^{-j-2}dz_s$。
所以第 $n=Nm>0$ 尾层的极阶至多 $n$；最高极阶只能来自第 $1$ 中心层。中心既定 polar 部分送回尾上的项正则，不会增加这个界；node residue 为零，按原 compact-type 树保留。中心自身非齐次变形和全部其它尾返回可改变低极部，均未被删除。

full 分支到该 generic 尾的无穷分歧指数为二。利用 R1044 已证
$\operatorname{div}(\eta)=(p-2)\sum_\infty[\infty]$，若写实际当前层为 $f_N\eta$，则 $f_N$ 的 full 极阶至多
$$
2Nm-1+(p-2)=D_N.
$$
$N=0$ 的 holomorphic $\omega_s^{\rm hi}$ 同样给次数 $p-3=D_0$。

光滑平面闭包的超平面正合列给总次数不超过 $D_N$ 的 polynomial representative。原 framing 权将 $c^{m-1}f_N$ 的权锁为 $\upsilon^{-D_N}$；在固定分支的 $\mu_{p+1}$ 下平均并用 $C$ 齐次化，再以完整 framing 运输到全部 Weil 分支，准确得到 (1199.10) 的 determinant twist。这与 R1197 §4 的论证相同，但本节的极阶、分歧指数和次数已重新计算。

施实际 $E_m$ 后，(1199.12) 迫完整当前层为 $\omega_{N,s}$ 的倍数。因而低极部和所有 holomorphic 修正由最高系数一并决定。

## 3. 同一 ordinary node 给准确的 $\gamma_{N,s}$

所选 ordinary centre 上 connected line 的 $x$ 约化为零，所以 (1199.14) 的 $W_s=y^2$。R1021 的 target eigenparameter 的完整 Cohen 次数为
$p-1+j(p^2-1)$。因此在这条实际 centre 上
$$
u'=c_sW_s^m+O(W_s^{m+e_0}).
\tag{1199.15}
$$
这是沿指定 ordinary line 的恒等式，不把 $x=0$ 宣称为整个 full 图上的关系。

由 R1198 的有限 period 比较，足够本篇全部系数的精度内，
$$
\xi_s(b-s)=\theta_sW_s^m,\qquad
b=s+J_s(\theta_sW_s^m).
\tag{1199.16}
$$
遗漏的次数至少 $m(m+1)>m^2$。再由 $u^m=h_p(b)$ 和 (1199.3)，
$$
u=\tau_sW_sK_s(b-s).
$$
将这些代入原 $\eta_T$，准确得到
$$
\boxed{\quad
\eta_T=
 \frac m{\tau_s}W_s^{-2}
 \mathcal E_{s,T}(J_s(\theta_sW_s^m))\,dW_s.
\quad}
\tag{1199.17}
$$

也可用 R1023 的真实同源微分参数取 $ZW_s=\pi_0$，
$\psi_s=Z^{-m}$。在特殊尾上
$Z=z_s(1+A_sz_s^{p+1})^{1/(2m)}$ 到所需有限 jet；
它的首项为 $z_s$，而在 centre reduction 上给同一个 $W_s$。
两个写法的差只进更高 centre 层，降低当前极阶，不改本节最高系数。全部原单位仍是 (1199.3)，没有另一次单位规范化。

(1199.17) 的第 $N$ 项，乘 $\pi_0$ 并过 node，给当前尾层最高项
$$
-\pi_0^{Nm}\frac{m\theta_s^N}{\tau_s}
 e_{N,s}(T)\,z_s^{-Nm}dz_s.
$$
与 (1199.13) 比较，正得 (1199.7)–(1199.9)。$N=0$ 由
$T(s)=2\tau_sA_p'(s)L_s/m$ 恰恢复 $\gamma_{0,s}=L_s$。这核准了同一原 Serre 基中的尺度，而不只证明它是某个非零倍数。

## 4. 全部交叉配对的闭式

令
$$
c_{m,s}=(-1)^{(m-1)/2}
 \binom{m-1}{(m-1)/2}A_s^{(m-1)/2}\in k^\times.
\tag{1199.18}
$$
R1196 的原 gap 计算给
$$
\operatorname{Res}_{\infty_s}(\psi_s^m\omega_{0,s})
 =-2c_{m,s}.
$$

在原 full 坐标中，$\psi_s=\beta_Q^{p-1}$，而
$\Theta\beta_Q=\beta_Q^p$，所以有严格的同源恒等式
$$
\Theta\psi_s=-\psi_s^2.
\tag{1199.19}
$$
对 formal Laurent residue，$\operatorname{Res}(dH)=0$。于是完整分部积分给
$$
\operatorname{Res}(\psi_s^a\Theta^NF\,\eta)
 =(-1)^N\operatorname{Res}(\Theta^N(\psi_s^a)F\eta)
 =(a)_N\operatorname{Res}(\psi_s^{a+N}F\eta).
$$
在 $a+N=m$ 时得到准确式
$$
\boxed{\quad
\operatorname{Res}_{\infty_s}(\psi_s^a\omega_{N,s})
 =-2c_{m,s}\frac{(a)_N}{a_N}.
\quad}
\tag{1199.20}
$$
可先在原 full 支读取再作真实 trace/同一正规化子平均；有限覆盖的 residue 因子在两边同时出现并约去。这里从未把某个节点上的 $\psi_s$ 当作整个 quotient 尾的单一全局正则函数。

所用原负主部精度也足够：R1018 的
$\psi_s=z_s^{-m}(1+A_sz_s^{p+1})^{-1/2}
+O(z_s^{-m+p(m+1)})$
与当前极界相乘后，误差次数至少
$p(m+1)-m^2>0$，不贡献 residue。

R1198 的第 $a$ 个 finite-log 输入是
$\varepsilon^a\theta_s^aD_{a,s}\psi_s^a$。
读取总 $\pi_0^{m^2}$ 时恰有 $N=m-a$。结合 (1199.7)、(1199.20)，该 ordinary node 的完整贡献为
$$
\boxed{\quad
\mathcal B_s(T)=
 -\frac{m\,c_{m,s}\theta_s^m}{\tau_s}\,
 \sum_{a=1}^{m}
 D_{a,s}e_{m-a,s}(T)
 \frac{(a)_{m-a}}{a_{m-a}}.
\quad}
\tag{1199.21}
$$
$1\le a\le m$ 的每一项均保留。所有阶乘和 $(a)_{m-a}$ 都小于 $p$；没有反除 Bernoulli 数或未知首项。

按 R1018 的 $e_D/e_I$ Čech 方向，Serre 配对就是这里的原 residue，故 (1199.21) 的负号与基配对 $-2$ 一致。它给一般 $T$ 的所有无支撑尾之和；一般情况下尚须加三个支持尾的贡献。

## 5. 完整收缩严格消去 opposite line 的选择

记
$$
\mathcal S_s(T)=
 \sum_{a=1}^{m}D_{a,s}e_{m-a,s}(T)
                    \frac{(a)_{m-a}}{a_{m-a}}.
$$
精确的权为
$$
w_a:=\frac{(a)_{m-a}}{a_{m-a}}
 =\frac{2(-1)^{m-a}(m-1)!}{(a-1)!(m-a+2)!}
 =\frac{2(-1)^{m-a}}{m(m+1)}
                  \binom{m+1}{a-1}.
\tag{1199.22}
$$

首先由同一 Hasse 方程及初值得
$f_{1,s}(t)=h_p(s+t)/h_p'(s)$；
Wronskian 为 $r(s)/r(s+t)$。因此在所需次数内
$$
K_s=f_{0,s}^{1/m},\qquad
\mathcal E_{s,T}(t)=
 \frac{r(s+t)^{2g+1}T(s+t)}{h_p'(s)r(s)}
                 f_{0,s}(t)^{\,1-1/m}.
$$
因为 $m=-1/2$ 于 $k$，且所有读取次数小于 $p$，有限二项展开给
$$
\boxed{\quad
\mathcal E_{s,T}(t)=
 \frac{r(s+t)^{2g+1}T(s+t)}{h_p'(s)r(s)}
                 f_{0,s}(t)^3
 \pmod{t^m}.
\quad}
\tag{1199.23}
$$

形式上将 $\alpha_s$ 改为 $\alpha_s+c$，则
$f_0\mapsto f_0+cf_1$、
$\xi\mapsto\xi/(1+c\xi)$。令
$H_s(v)=\log(G(s+J_s(v))^2/G(s)^2)$、
$E_s(v)=\mathcal E_{s,T}(J_s(v))$。有限变换准确为
$$
H_s^{\rm new}(v)=H_s\!\left(\frac v{1-cv}\right),\qquad
E_s^{\rm new}(v)=(1-cv)^{-3}
                 E_s\!\left(\frac v{1-cv}\right).
\tag{1199.24}
$$
所以无穷小变换为
$$
\partial_cD_{a,s}|_{c=0}=(a-1)D_{a-1,s},\qquad
\partial_ce_{N,s}|_{c=0}=(N+2)e_{N-1,s}.
$$
每个 $D_{b,s}e_{m-b-1,s}$ 的系数恰为
$$
b\,w_{b+1}+(m-b+2)w_b=0.
$$
变换是参数 $c$ 的加法群作用，而且整个收缩关于 $c$ 的次数至多 $m-1<p$。其导数处处为零迫它是常数，不存在一个隐藏的 $c^p$ 项。因而
$$
\boxed{\quad \mathcal S_s(T)\text{ 与 }\alpha_s\text{ 无关}.\quad}
\tag{1199.25}
$$
这是对全部低 $a$/高 normal 项一起证明的不变性。计算这个完整收缩时可以使用任意方便的 $f_0$ 初值，例如 $\alpha_s=0$；不能据此改写 R1198 的某一个原单槽或丢掉其它项。

## 6. 旧支持节点论证（已由 R1208 替换）

取
$$
T_*(b)=(b^3-1)^{2g-1}.
\tag{1199.26}
$$
R1197 的完整 normal 旗标给原 $c_1$ 尾上所有小于 $m^2$ 的层为零：最后已处理层为 $m^2-3m$，下一个允许角色层就是 $m^2$。真实 deck 运输将此结论同时送到另外两个 CM 支。于是
$$
\Omega_{L_*}|_{D_\xi}\in
 \pi_0^{m^2}\Omega^1(D_\xi)
\qquad(\xi^3=1).
\tag{1199.27}
$$
只凭 (1199.27) 还不能删除整个支持支；还须处理 centre–node 的 frame，下面逐项补足。

在每个实际 CM node，原同源微分参数满足
$v\,w_{\rm dual}=p$。R1023 的精确 character 形状给
$$
u'=vA(p,v^{p+1})+w_{\rm dual}^pB(p,w_{\rm dual}^{p+1}),
\qquad A(0,0)\in W^\times.
$$
原 node 的单位根正规化给 $v=W_{\rm fine}^m$、
$Z_{\rm fine}W_{\rm fine}=\pi_0$。因此
$$
\frac{w_{\rm dual}^p}{v}
 =p^{p-1}Z_{\rm fine}^{m(p+1)}
$$
在该 node 整且高阶；故 $u'/v$ 是单位。原 CM target coarse 参数在 fine eigenparameter 处有准确三次零，零点为原 $\mu_3$ 固定提升。于是
$$
b_{\rm lift}-\xi=w^m\cdot\text{单位},
\qquad z w=\rho_\xi\pi_0^3
\tag{1199.28}
$$
在原厚度三的粗 node 上成立。

原 divisor 的系数是
$a_1=2,\ a_\zeta=a_{\zeta^2}=-1$，而 $G^2$ 在 $b=\xi$ 的阶是 $2a_\xi$。所以
$$
G(b_{\rm lift})^2=w^{2ma_\xi}\cdot\text{单位}.
\tag{1199.29}
$$
这恰是原 $P=(p-1)D_0$ 的 flux $2ma_\xi$ 在三条正则化边上给出的 vertical monomial。故实际 $G(b_{\rm lift})^{-2}$，按原零多度 twister 解释后，是整条 centre–node 上的非消失 frame。取该 node frame，centre–node transition 准确等于一，而非留下另一个未算 residue。

现在在
$A_M=R/(\pi_0^{m^2+1})$、$I=(\pi_0^m)$ 上使用 R1196 的相对 Picard 核。原线丛模 $I$ 已平凡，且 R1018 已将 centre 的这个 frame 和无支撑尾的常数 frame 与同一个全局模 $I$ 平凡化识别。在 CM affine 开上，任一该平凡化都可提升为实际 frame：
affine 的 $H^1(I O)=0$，逐个 nilpotent 阶提升即可。故剩下的 CM tail–node transitions 全在 $1+I$，其有限 log 在 $I$。

由 (1199.27)，这些交叠上的
$\ell_I(g)\Omega_{L_*}$ 至少含 $\pi_0^{m^2+m}$，不贡献总 $\pi_0^{m^2}$ 的 Serre residue。正则化有理链是零多度，按原树的相同 frames 可合回厚度三 node；无遗留 cycle 或 residue 流。这证明三个支持支，包括 node 交叠，全部贡献为零。

因此 R1196 的同一个完整首列
$$
\mathcal V_m(T_*)
 =\overline{\pi_0^{-m^2}
        \langle E_m\log P,\Omega_{L_*}\rangle}
$$
准确为
$$
\boxed{\quad
\mathcal V_m(T_*)=\sum_{s\in S}\mathcal B_s(T_*).
\quad}
\tag{1199.30}
$$
这是原 $P$、原 compact-type 图和同一个 $E_m$ 的全图结论。没有把一个单尾输入升格为全列，也没有利用 $H_k(Q)=0$ 删除未知的 marked-point 提升。

## 7. 剩余原相位的准确范围

原 full 坐标给
$$
A_s=-3C_s^2,\qquad
C_s^{p-1}\theta_s^{p+1}
 =-\frac{r(s)^{8g-2}}{A_p'(s)^2}.
\tag{1199.31}
$$
第二式是 R1023 的同一个 norm/crystalline 校准，不将两个指数互换。置
$$
U_s=\frac{\theta_s^m A_s^{(m-1)/2}}{\tau_s}.
$$
由 $\tau_s^m=h_p'(s)\theta_s$、
$h_p'(s)=r(s)^{2g}A_p'(s)$、
$(-3)^m=-1$ 及 (1199.31)，直接得到
$$
\boxed{\quad
U_s^m=\left(\frac{r(s)^{4g-2}}{A_p'(s)}\right)^m.
\quad}
\tag{1199.32}
$$
具体地，令 $h=(m-1)/2$，则
$$
U_s^m
 =\frac{(-1)^h
       (C_s^{p-1}\theta_s^{p+1})^h}{h_p'(s)}
 =\frac{r(s)^{(8g-2)h-2g}}{A_p'(s)^m},
$$
而 $(8g-2)h-2g=(4g-2)m$。

所以有准确且由原节点定义的
$$
\boxed{\quad
U_s=\nu_s\frac{r(s)^{4g-2}}{A_p'(s)},
\qquad
\nu_s=\frac{U_sA_p'(s)}{r(s)^{4g-2}}\in\mu_m.
\quad}
\tag{1199.33}
$$
不能仅由每个 $\nu_s^m=1$ 就设所有 $\nu_s$ 相同。
(1199.21)、(1199.30) 保留这些实际相位；若要把它们变成一个无相位的全局 rational-residue 和，须另行证明同一个 Igusa 刚化确有该相容性。

## 8. 继续目标与准确边界

现在 (1199.30) 是同一原 CM 轮廓核上的实际 MW 首列，全部输入为原 $A_p,h_p,G$、显示有限递推、原节点单位以及 (1199.33) 的确定相位；局部 opposite line 已由 (1199.25) 严格消去。未知的不再是各个 higher normal 或其它尾是否有遗漏贡献，而是这个指定有限和的实际值及其相位关系。

若要用于 R1191 的同一个半秩 $C$，仍须消费 R1196 的真实 $q_CE_m=e_mq_C$ 和 R1195 的单型整拼接，不得把本篇整个 packet 的线性泛函当成已饱和的 $C$-泛函。本文未证明该有限和非零，也未给整个深盘唯一零点或一般 $p$ 的绝对界。

全篇为原几何、有限表示、有限幂级数和 residue 的纸面推导；未执行数学程序，未重跑已登记窗口。

## 来源与核准

- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md) §§3、5–7：原 trace-zero 方向、全部 node 单位、原 Čech 符号、零多度 flux、模 $I$ 平凡化及原 $\psi_s$ 的合法负主部。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md) §§1–4、[R1023](R1023-original-CM-divisor-complete-first-log-vector.md) §§3–5：实际 full 参数、整个模 $p$ 仿射作用、target Cohen 次数、真实同源 node 单位根及 norm/crystalline 校准。
- [R1044](R1044-original-CM-disc-complete-coefficient-flag.md) §3：同一光滑 full-Dickson 平面闭包、无穷除子、polynomial representative 与全分支齐次化。
- [R1193](R1193-original-highest-primitive-packet-and-simple-Cauchy-CM-jet.md)、[R1195](R1195-original-full-integral-normalizer-corner-and-one-p-gluing.md)：原最高 packet、首中心、底向量插值和完整有限角的真实组成因子。
- [R1196](R1196-original-highest-packet-Picard-log-and-finite-Cech-source.md)：原有限 Picard log、实际 Serre 配对、$q_C$ 及 formal-log $p$ 次返回的已付范围。
- [R1197](R1197-original-highest-packet-complete-CM-coefficient-flag.md)、[R1198](R1198-original-ordinary-quotient-period-jets-and-finite-log-source.md)：原 CM 全旗标与一维核、原 ordinary period jets 和全部有限对数输入。

root 推导并核准整个 generic 角、正常层和配对；global_route 独立纸核 $\gamma_N$ 的真实 node 精度、$\Theta$ 分部积分、opposite 收缩不变性、三个支持支的 frame/flux 及原 $\mu_m$ 相位。所有核对落实到上文显示证明。
