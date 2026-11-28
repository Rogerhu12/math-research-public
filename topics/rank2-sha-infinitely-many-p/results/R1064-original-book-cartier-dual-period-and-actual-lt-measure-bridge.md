# R1064 — 原 book 周期、Cartier-dual LT 周期与实际测度的完整比较

日期：2026-11-28 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

按根 README 第8条登记完整证明。主目标仍未完成。

本文先锁定原实际 Tate 生成元所决定的两种周期，证明它们的乘积是一个明确的有限域单位；随后给原 whole bounded Amice 来源的全 LT 开盘提升、原临界读者的准确运输，以及 BSS 定理在有限系数扩域上的返回。全程保留原 Maass 变换。这里没有将普通 LT 圆盘上的系数 Galois 不变性冒充为 ST 字符空间的下降，也没有给原 canonical 坏条件添加零行。

## 1. 原对象、两篇新文及适用范围

取原 good 惰性素数 $p>211$，并继续排除原固定来源的有限坏集。写
$$
 L=K_p=\mathbf Q_{p^2},\qquad q=p^2,\qquad
 \tau_0=\frac{p}{p^2-1}.
$$
先固定一个原 prime-to-$p$ CM/level 基字，取其在 $p$ 处有完整 $\mathcal O_L$ 作用的 good 椭圆曲线 $E$。令 $G=\widehat E$，$\omega_0$ 为原代数微分，$\alpha_{\infty,1},\alpha_{\infty,2}$ 为原完整 Tate 基。以下比较使用这个实际 maximal-at-$p$ 基字；没有把 conductor-$p^2$ 商曲线的形式群未经运输改称为 $G$。有限个原基字可分别作同样比较，保留各自常数。

固定有限完备 Galois 扩域 $F/L$，包含本次使用的所有代数模型、微分、有限 level、原 $p^2$ 除点和已经支付的实际中心及系数。没有把任何超越周期放入 $F$。原 book 周期沿
[R1059](R1059-original-p-square-source-and-complete-critical-germ.md)、
[R1060](R1060-original-full-gaussian-transpose-and-critical-slope.md)、
[R1062](R1062-original-translated-miller-jets-and-critical-weight-germs.md)
记为 $\Omega$。

本次先查旧
[2026-11-14 文献入口](../notes/2026-11-14-deep-new-sigma-and-lubin-tate-literature-entry.md)，再全文读：

- Berger–Sprang–Steingart，[*Bounded functions on the character variety for quadratic extensions of $\mathbf Q_p$*](https://arxiv.org/html/2611.21796v1)，全文 §§1–7，特别 Theorem 1.2、§3 的定量证明及 §5。
- Katagiri，[*Norms of Schneider–Teitelbaum Polynomials in $p$-adic Fourier Theory*](https://arxiv.org/html/2609.20002v2)，全文 §§1–3，特别 Theorem 1.2、Corollary 1.4、Remark 1.5。
- Schneider–Teitelbaum，[原刊正文](https://ems.press/content/serial-article-files/25890)，Documenta Mathematica 6 (2001), 447–481，特别 §3、Corollary 3.8 和 Appendix，印页477–479。
- Kriz 原书出版社的 [Chapter 1](https://pup-assets.imgix.net/onix/images/9780691216461/9780691216461.pdf?fm=pdf)，印页11–12的 HT/微分定义及印页18的(1.15)。

记 $\mathfrak X_L$ 为加法群 $\mathcal O_L$ 的局部 $L$-解析字符空间。它与原中央参数 $j$ 的 $\mathbf Z_p$ 权盘不同，也与 coherent 参数 $Z,W$ 的物理闭盘不同。

## 2. 同一个 Cartier-dual 生成元给出的精确周期乘积

### 2.1. 实际 HT/dlog 比较，不靠相反赋值猜周期

令 $e$ 为原主极化的 Weil pairing，取
$$
 t'_E=e(\alpha_{\infty,2},-)\in T_pG^D.
 \tag{R1}
$$
这里 $T_pG^D$ 的元素按兼容的形式群字符 $G[p^r]\to\mu_{p^r}$ 理解，保留原 pairing 的方向与其 $\mu_{p^\infty}$ 值。

原 $\alpha_{\infty,2}$ 是 $\mathbf Z_p$ 基向量，故不在 $pT_pE$；而 $T_pE$ 是自由秩一 $\mathcal O_L$ 模，所以它是一个 $\mathcal O_L$ 生成元。主极化是整的完美配对，因而(R1)是实际 dual Tate 模的生成元，不是只在有理 Tate 模中取得的一条线。

取原整形式群坐标 $v$，令 $\omega_G$ 为首项 $dv$ 的不变微分。ST 的实际 Cartier-dual 同态记作
$$
 Q_E(v)=1+F_{t'_E}(v)\in1+v\mathcal O_{\mathbf C_p}[[v]],
 \qquad
 \frac{dQ_E}{Q_E}=\varpi_E\omega_G.
 \tag{R2}
$$
这就是 ST Appendix(a) 的等式；$\varpi_E$ 由(R1)唯一确定。其赋值为
$$
 v_p(\varpi_E)=\frac1{p-1}-\frac1{p^2-1}=\tau_0.
$$
在足够小的盘，$Q_E(v)=\exp(\varpi_E\log_G(v))$；全开盘使用的是(R2)的整形式群同态，不能把这个裸 exp 级数当作全盘逐项收敛的定义。

另一方面，book 印页11–12的原定义准确为
$$
 s=\operatorname{HT}_E(\alpha_{\infty,2}),\qquad
 \omega_{\rm can}=\frac{s}{y_{\rm dR}},\qquad
 Y=\theta(y_{\rm dR}),\qquad
 \omega_0=\Omega\,\theta(\omega_{\rm can}).
 \tag{R3}
$$
同一页先以 Weil pairing 将 Tate 向量认作到 $\mu_{p^\infty}$ 的字符，再以拉回 $dT/T$ 定义 HT。因此(R1)和(R2)给出的正是同一个 $s$：
$$
 s=\varpi_E\omega_G.
$$
写 $\omega_0=\lambda_G\omega_G$。原 good 整参数及其整逆使
$\lambda_G\in\mathcal O_F^\times$；仍显式保留这个原基单位。

当前 $b=2$ 的原 Maass 常数来自 book(1.15)及同一坐标缩放：
$$
 C=-\,\frac{p^2Y}{\widehat z}.
 \tag{R4}
$$
当前 $\widehat z\in L^\times$ 是单位，$C\in F$ 且 $v_p(C)=2$，这些都是 R1059/R1060 的实际基字规范。因此
$$
 Y=-C\widehat z/p^2\in\mathcal O_F^\times.
$$
这支付了本次 $Y$ 的有限域和单位断言；没有另外假设一个未核的 CM 数值。

将(R2)代入(R3)，逐微分直接得到
$$
 \boxed{\quad
 \Omega\,\varpi_E=b_E,\qquad
 b_E=\lambda_GY\in\mathcal O_F^\times .
 \quad} \tag{R5}
$$
若原坐标恰以 $\omega_G=\omega_0$ 规范化，则 $b_E=Y$；一般保留 $\lambda_G$。更换 dual 生成元、different 识别或 $\omega_G$ 都必须同时运输(R2)。本文取的是实际(R1)，因此没有丢掉一个后来再任取的代数比例。

### 2.2. 全 Galois 字符、Rosati 和 cyclotomic 因子

约定 $\mathcal O_L$ 在 $G$ 上的作用是原切向 embedding，即
$[a]^*\omega_0=a\omega_0$。对 $\sigma\in G_F$，写
$$
 \sigma(\alpha_{\infty,2})=[a_\sigma]\alpha_{\infty,2},
 \qquad \chi_E(\sigma)=a_\sigma.
$$
主极化的 Rosati 是共轭，所以
$$
 e([a]P,Q)=e(P,[\bar a]Q).
$$
因此 dual $\mathcal O_L$ 作用若按预复合定义，有
$\phi_{[a]P}=\phi_P\circ[\bar a]$。

这里的真实 Galois 共轭是
$$
 (\sigma\phi_P)(Q)=\sigma\bigl(\phi_P(\sigma^{-1}Q)\bigr)
                 =e(\sigma P,Q).
$$
左式也作用 $\mu_{p^\infty}$，并没有先把一个 cyclotomic 生成元冻结掉。由完美配对，
$\chi_{\rm cyc}(\sigma)=N_{L/\mathbf Q_p}(a_\sigma)$，所以实际 dual 字符为
$$
 \tau_E(\sigma)=\bar a_\sigma
              =\chi_{\rm cyc}(\sigma)\chi_E(\sigma)^{-1}.
 \tag{R6}
$$
(R2)、(R3)与 $Y,\lambda_G\in F$ 遂给
$$
 \boxed{\quad
 \sigma\varpi_E=\bar a_\sigma\varpi_E,\qquad
 \sigma\Omega=\bar a_\sigma^{-1}\Omega.
 \quad} \tag{R7}
$$
范数一时才将末式写成 $\sigma\Omega=a_\sigma\Omega$。

这不把 R1059(A0b) 的 marked 比较 $\kappa_a=N(a)\kappa$ 认作
$\sigma\kappa$。前者在固定 cyclotomic 生成元下改 Tate 标记；
真实 $\sigma$ 同时将该生成元乘 $\chi_{\rm cyc}=N(a)$。当 $\kappa$ 是原 $F$ 中的配对标量时，它仍由 $\sigma$ 固定。这个区别也说明：全标记变换中的 $N(a)^n$ 与(R7)的系数 Galois 公式不能互相替代。

## 3. 原 whole bounded 测度的真实全 LT 开盘提升

取 R1059/R1060 的一个已经支付 bounded 性的 whole 来源
$$
 A(Q)=\int_{\mathbf Z_p}Q^x\,d\mu(x).
$$
不对未作原 $h_\infty$ 积分的 rank-one 因子分别假设有界。

令 $\iota:\mathbf Z_p\hookrightarrow\mathcal O_L$ 为原包含，并用(R2)定义 Fourier：
$$
 \begin{aligned}
 \mathcal F_E(\nu)(v)
   &=\int_{\mathcal O_L}Q_E([x]v)\,d\nu(x),\\
 A(Q_E(v))&=\mathcal F_E(\iota_*\mu)(v).
 \end{aligned} \tag{R8}
$$
第二式先在整数 $x$ 对形式群字符成立，再由连续性扩到 $\mathbf Z_p$。任一闭内盘上，$F_{t'_E}$ 的整系数给一致收敛，故可逐项积分；同时
$|Q_E(v)-1|\le|v|<1$。因此(R8)在整个 LT 开盘有界，且
$$
 \|\mathcal F_E(\iota_*\mu)\|_{\sup}\le\|\mu\|.
$$
由 ST Fourier 单射性，$\mu\ne0$ 时这个实际提升也非零。

对每个 $\kappa\in\mathcal O_L^\times$，真实整形式群作用给
$$
 \mathcal F_E(\nu)([\kappa]v)
      =\mathcal F_E(\kappa_*\nu)(v).
 \tag{R9}
$$
所以对有限个原实际 whole 字，可取
$$
 \nu=\sum_i w_i\,(\kappa_i)_*\iota_*\mu_i,\qquad
 \|\nu\|\le\max_i |w_i|\,\|\mu_i\|.
 \tag{R10}
$$
所有原 Haar 分母、有限中心和实际系数均在 $w_i$ 内。若原外权依赖共同小权盘，同式给真正的 Banach 值解析族；不把未授权的单字独立测度插入其中。

(R9)没有把 $\kappa\notin\mathbf Z_p$ 时的 $Q^\kappa$ 视为原单 $Q$ 盘的有界函数。它使用的是实际 $[\kappa]$，其定义域正是 LT 全盘。

## 4. 字符空间下降与原完整 Maass 作用

### 4.1. 两种 Galois 不变性必须分开

ST Corollary 3.8 的准确方向是：一个 LT 盘函数 $f$ 代表
$\mathfrak X_F$ 上的函数，当且仅当
$$
 \sigma f=f\circ[\tau_E(\sigma)]\qquad(\sigma\in G_F).
$$
对(R8)的测度，$\sigma$ 固定输入群 $\mathcal O_L$，只作用测度取值，故
$$
 \sigma\mathcal F_E(\nu)
     =\mathcal F_E((\tau_E(\sigma))_*\sigma\nu),\qquad
 \mathcal F_E(\nu)\circ[\tau_E(\sigma)]
     =\mathcal F_E((\tau_E(\sigma))_*\nu).
$$
由单射性得到
$$
 \boxed{\quad
 \mathcal F_E(\nu)\text{ 下降至 }\mathfrak X_F
 \iff \sigma\nu=\nu\quad(\sigma\in G_F).
 \quad} \tag{R11}
$$
对 bounded 测度，右式也恰表示其紧开集的测度值在 $F$：对紧开集示性函数取值，再用 $\mathbf C_p^{G_F}=F$ 即得。

特别，若范数一子群上一个候选 $\nu_R$ 满足
$\sigma\nu_R=c_*\nu_R$，而 $\tau_E=c^{-1}$，则
$\sigma\mathcal F_E(\nu_R)=\mathcal F_E(\nu_R)$。
这是普通 LT 盘上的系数不变性；(R11)要求的却是 twisted 不变性。前者没有自动成为 BSS 的标量输入。

### 4.2. 原 Maass 费用不能省成纯 dilation

令
$$
 m_n=\int x^n\,d\mu,\qquad
 b_r(n)=\binom{n+2}{r}\binom nr r!,\qquad
 R_n=(T_Cm)_n=\sum_{r=0}^n b_r(n)C^r m_{n-r}.
 \tag{R12}
$$
同一个 $C$ 满足 $v_p(C)=2$。R1062(P10)已在固定全部代数数据的深范数一子群上支付
$$
 \boxed{\quad
 \sigma_c m_n
   =c^3\sum_{r=0}^n b_r(n)((c^2-1)C)^r
                    (c^2)^{n-r}m_{n-r}.
 \quad} \tag{R13}
$$
其形式原点表达为
$$
 \sigma_c A(e^z)=
 c^3(1-(c^2-1)Cz)^{-3}
 A\!\left(\exp\frac{c^2z}{1-(c^2-1)Cz}\right).
 \tag{R14}
$$
右侧的全盘 bounded 延拓来自原实际左侧；没有据形式式为任意输入另造有界算子。将(R8)代入，也必须携带这个完整三角变换，不能只保 $x\mapsto c^2x$。

(R5)确实把周期费用变成明确的实际 tensor。例如将 R1062(P8)的临界值、临界一阶导数另记为
$V_0=\mathcal R(-2)$、$V_1=\mathcal R'(-2)$，则
$
 \Omega\bigl(V_1-(\log U_*)V_0\bigr)
   =\frac{b_E}{\varpi_E}
         \bigl(V_1-(\log U_*)V_0\bigr)\in F.
 \tag{R15}
$
这里的 $V_0,V_1$ 与(R12)的正整数矩 $R_n$ 分开。当原完整临界值 $V_0=0$ 时，此式退化为 $\Omega V_1\in F$。
这是原斜率的准确代数 frame；一个标量属于 $F$，仍不单独证明它所属的全函数满足(R11)或 BSS 的全盘范数条件。

## 5. BSS 对有限系数扩域的完整返回及实际 different 成本

BSS Theorem 1.2 对二次 $L/\mathbf Q_p$ 给
$$
 \mathcal O_L[[\mathcal O_L]]
       \simeq \mathcal O(\mathfrak X_L)^\circ .
 \tag{R16}
$$
以下补一个直接适用于本题有限野系数域的论证，不假设该定理可以无代价换成任意 $\mathbf C_p$ 系数。

### 5.1. 保留全部 trace-dual 坐标

设 $F/L$ 有限，$f\in\mathcal O(\mathfrak X_F)$ 且全局谱范数不超过一。取 $\mathcal O_F$ 的一组 $\mathcal O_L$ 整基 $e_1,\ldots,e_d$，及 trace-dual 基 $e_i^*$：
$$
 \operatorname{Tr}_{F/L}(e_i^*e_j)=\delta_{ij},\qquad
 e_i^*\in\mathfrak D_{F/L}^{-1}.
$$
令 $d_F=v_p(\mathfrak D_{F/L})$，$a_F=\lceil d_F\rceil$。在每个 affinoid 上作有限系数 trace，再粘合，得
$$
 f_i=\operatorname{Tr}_{F/L}(e_i^*f)
       \in\mathcal O(\mathfrak X_L),\qquad
 f=\sum_i e_i f_i.
$$
将 trace 写成全部 $L$-embedding 的和，每个共轭不改谱范数；由超度量不等式，
$$
 \|f_i\|_{\sup}\le p^{d_F}.
$$
故 $p^{a_F}f_i$ 属(R16)的单位球，由 BSS 得唯一
$\mu_i\in\mathcal O_L[[\mathcal O_L]]$。于是
$$
 \boxed{\quad
 \nu=p^{-a_F}\sum_i e_i\mu_i,\qquad
 \mathcal F(\nu)=f,\qquad
 \|\nu\|\le p^{a_F}.
 \quad} \tag{R17}
$$
这里的 Fourier 按字符空间自身定义；拉回 LT 盘时使用同一个(R2)生成元。

此论证只用有限维 trace-dual 系数投影，没有对原全字作单一 total trace。因而全部 wild 坐标都保留。维数 $d$ 不额外造成一个 $p$ 损失，因为范数估计是非 Archimedean 的最大值估计。唯一性仍由 ST Fourier 单射性给出。

### 5.2. 原二层 LT 域的统一成本是至多 $p^2$

在 R1062§7.1 已付的原严格整 LT 模型中，
$$
 [-p](v)=-pv+v^q.
$$
令 $F_1=L(E[p])$，$F_2=L(E[p^2])$；若原固定 tame 域在当前位不分歧，可先作这个不分歧基变。取兼容 primitive 参数 $v_1,v_2$。第一层的 Eisenstein 多项式为
$v_1^{q-1}-p$，故其导数在 $v_1$ 的赋值为
$(q-2)/(q-1)$。第二层的多项式为
$X^q-pX-v_1$；在 $v_2$ 处导数为
$qv_2^{q-1}-p$，第一项赋值严格大于一，第二项赋值为一。因此由 different 的塔公式，
$$
 \boxed{\quad
 v_p(\mathfrak D_{F_2/L})
 =1-\frac1{q-1}+1
 =2-\frac1{q-1}<2.
 \quad} \tag{R18}
$$
等价的整指数为 $q(2q-3)$，分歧指数为 $q(q-1)$。

所以，凡已经证明其实际代数系数位于这个 $F_2$（或其不分歧基变）的完整来源，只要真实函数满足 BSS 的全局有界与(R11)条件，(R17)给
$$
 \boxed{\quad \|f\|_{\sup}\le1
           \ \Longrightarrow\ \|\nu\|\le p^2.\quad}
 \tag{R19}
$$
更一般非整谱范数时，先乘一个实际 $L$ 标量使范数至多一，再同样返回；不从上式凭空推连续实数尺度的精确最优范数。

如果某个来源确需额外 ramified 系数扩域，应改用其真实 different；本段不把尚未证明属于 $F_2$ 的单个 Miller 根或未积分 $h_\infty$ 因子放进去。该 $p^2$ 成本是有限扩域返回的上界，不是原 Smith 格新增的两个单位 pivot。

## 6. 原临界读者与有限 orbit 的无损运输

在原固定 Teich 分量和共同小权盘，原完整单位域测试是
$$
 \Psi_{C,j}(x)=\mathbf1_{\mathbf Z_p^\times}(x)\,
 x^j\sum_{r\ge0}
   \binom{j+2}{r}\binom jr r!\,(C/x)^r .
 \tag{R20}
$$
这里 $x^j$ 沿原 Teich 分量解析，不改变有限角色。两个 falling factorial 的分子整，所以其作为 $j$ 的多项式 Gauss 赋值至少 $-v_p(r!)$。当前 $v_p(C)=2$ 给
$2r-v_p(r!)\to+\infty$，准确支付 Tate 收敛及逐次求导。

端点和真实斜率为
$$
 \begin{aligned}
 \Psi_{C,-2}(x)&=\mathbf1_{\mathbf Z_p^\times}x^{-2},\\
 \partial_j\Psi_{C,j}(x)|_{j=-2}
 &=\mathbf1_{\mathbf Z_p^\times}x^{-2}
    \bigl(\log\langle x\rangle-\mathcal E(C/x)\bigr),\\
 \mathcal E(z)&=\sum_{r\ge1}(r+1)(r-1)!z^r .
 \end{aligned} \tag{R21}
$$
对(R9)中每个实际 $\kappa_i$，定义带字标记的测试
$\Psi^{\kappa_i}_{C_i,j}(\kappa_i x)=\Psi_{C_i,j}(x)$，则
$$
 \int_{\kappa_i\mathbf Z_p}
   \Psi^{\kappa_i}_{C_i,j}\,d((\kappa_i)_*\iota_*\mu_i)
      =\int_{\mathbf Z_p}\Psi_{C_i,j}\,d\mu_i.
 \tag{R22}
$$
因此完整 $\Lambda_iM_i$ 及其导数
$\Lambda_i'M_i+\Lambda_iM_i'$ 均被保留。不同字若在交集上带不同测试，必须先保其标记或直和，不能仅合并测度后丢掉测试差异。

回原单个 bounded $Q$ 盘还有一个独立条件：
$$
 \boxed{\quad
 \mathcal F_E(\nu)=A_0(Q_E)
 \text{，其中 }A_0\text{ 是 bounded Amice 函数}
 \iff\operatorname{supp}\nu\subset\iota(\mathbf Z_p).
 \quad} \tag{R23}
$$
正向以 Amice 取得 $A_0$ 的测度，再用 ST 单射性；反向就是(R8)。若两个 $\kappa_i$ 的比不在 $\mathbf Q_p^\times$，相应两条 $\mathbf Z_p$ 直线只交于零。故返回原盘需要离零的整测度逐线相消，不是只对某一个中央值相消。

(R8)也不更改 R1060§13.1 的物理闭边界判据。那里涉及原两槽阶乘及周期，闭边界 Tate 性恰等价于 $\mu|_{\mathbf Z_p^\times}=0$。这里的 LT 切向倍率 $\varpi_E$ 不是单位坐标变换；例如 $\delta_1$ 的(R8)已经有界，而其单位域测度当然不为零。

## 7. 新文的精度能够用于什么实际范数

BSS 未分歧证明取
$\rho_n=p^{-1/(p^n-p^{n-1})}$，
$A_n=L\langle\rho_n^{-1}x_1,\rho_n^{-1}x_2\rangle/(H)$，
其中 $H=\log(1+x_2)-v_2\log(1+x_1)$。
其 §3 的定量式是
$$
 \operatorname{im}(A_N^\circ\to A_n^\circ)
 \subset\Lambda_n+p^{\,p^{N-n}-1}A_n^\circ,\qquad N>n,
 \tag{R24}
$$
并可取总次数严格小于 $p^N-p^{N-1}$ 的整多项式。这里 $\Lambda_n$ 是整测度代数的像。

因此(R17)的有限域函数若需在 $X_n$ 上精确到 $p^H$，可先对
$p^{a_F}f_i$ 取
$N=n+\lceil\log_p(H+a_F+1)\rceil$，然后除回 $p^{a_F}$。
这是同一个实际字符函数在 affinoid 上的统一评价精度；并不自动等于测度总变差精度或(R20)的负矩/导数精度。那些读者还需自身的算子范数。

Katagiri 的特选坐标满足
$\ell(v)=\sum_{a\ge0}v^{q^a}/p^a$，
$\exp(X\ell(v))=\sum_mP_m(X)v^m$。
其精确公式在 $m=lq^{N+1}+r$、$0\le r<q^{N+1}$ 时为
$$
 \|P_m(x\varpi)\|_{LA_N}
 =p^{-G_N(m)},\qquad
 G_N(m)=w(r)+l(\tau_0-1)-v_p(l!),\quad
 w(r)=\tau_0\sum_a r_a p^{-a}.
 \tag{R25}
$$
Remark 1.5 明确其 norm-one 基不是正交基，也不自动生成整个整单位球。

尤其 $m<p^2$ 时，
$$
 P_m(x\varpi)=\frac{\varpi^m}{m!}x^m,\qquad
 \frac{P_m(x\varpi)}{P_m(\varpi)}=x^m.
 \tag{R26}
$$
所以在 R1051 的实际低节点窗，归一以后仍是原 $m$ 次节点幂；将同一 $p^n n!$、charge 和 regular 乘子全部乘回，没有由此新增一个 Smith $p$ 因子。大窗若要使用(R25)，还必须给原完整行格到这个特选坐标的有界双向运输；不能用单项范数一替代该步骤。特选 $+p$-log 与原 $[-p]$ 坐标亦不按名字相认。

## 8. 直接将去周期的完成矩认作 LT 分布会有什么后果

这一节只检验一个明确候选，避免把(R5)误用成全矩阵有界性。

假设原 $\mu$ bounded，取统一下界 $v_p(m_n)\ge M$。由(R12)的整系数及 $v_p(C)=2$，
$v_p(R_n)\ge M$。定义同一个实际去周期序列
$$
 r_n=\Omega^{-3-2n}R_n.
$$
(R5)和原周期赋值给
$$
 v_p(r_n)\ge M+(2n+3)\tau_0 .
 \tag{R27}
$$
这个序列并不因此成为某个 bounded 或局部 $L$-解析分布的矩。

更准确地，若确有一个局部 $L$-解析分布 $\mathcal D$ 在
$\mathcal O_L$ 上满足 $\mathcal D(x^n)=r_n$，则原整个 flat 权分量必为零。证明如下。

对每个 $j\ge0$，取 $n_h=j+(q-1)p^h$。在逐模 $p$ 剩余球解析的 Banach 空间 $LA_1$ 中，
$$
 x^{n_h}\longrightarrow
       \mathbf1_{\mathcal O_L^\times}(x)x^j .
 \tag{R28}
$$
在单位球上，先提 Teich 部分，再用
$\exp((q-1)p^h\log(1+pt/a))\to1$ 的 Tate 范数收敛；在
$p\mathcal O_L$ 球上则直接有范数 $p^{-n_h}\to0$。
由(R27)及分布的连续性，
$\mathcal D(\mathbf1_{\mathcal O_L^\times}x^j)=0$ 对所有 $j$ 成立。
LT Fourier 的各 Taylor 系数都是有限次多项式测试，所以单位域限制的 Fourier 在原点邻域为零；ST 单射性遂给该限制全零。

因此 $\mathcal D$ 支持于 $p\mathcal O_L$。它在固定 $LA_1$ 上连续，而
$\|\mathbf1_{p\mathcal O_L}x^n\|_{LA_1}=p^{-n}$，故
$$
 v_p(r_n)\ge n+O(1),\qquad
 v_p(R_n)\ge(1-2\tau_0)n+O(1).
 \tag{R29}
$$
右侧趋于正无穷。沿 R1056/R1059 的每个原合法正整数逼近序列，完整 $R_n$ 极限正是实际 flat 值，于是每个这样的值为零。其全权盘解析性使整个该分量恒零，包含原斜率。

若改用二次指标，要求一个 odd 分布满足
$\mathcal D(u^{2n+3})=r_n$、全部偶矩零，则同样论证先杀单位域，再得到更强的
$v_p(r_n)\ge2n+3+O(1)$。未给出的 $u^1$ 矩不妨碍单位域结论：用趋于同一个固定奇次数的高奇幂即可。

所以，在某个原实际 flat germ 非零的范围内，不能把这些去周期完成矩直接认成局部 $L$-解析分布。这一结论不排斥真正的带 tensor、不同变量或完整双槽来源；它只说明该候选必须另付实际构造。这里也没有预先声称所有当前原 flat germ 非零。

## 9. 已付结论及后续原来源范围

本篇闭合的是：

- 由同一原 HT/dlog、Rosati 与 cyclotomic 配对给出的精确单位
  $\Omega\varpi_E=\lambda_GY$，及其全 Galois 方向。
- 原 whole bounded 测度的全 LT 开盘提升、真实 $\mathcal O_L^\times$ 作用，和保全部 $\Lambda,\Lambda'$、log–$\mathcal E$ 的同一读者运输。
- 字符空间下降的准确判据；对真正 bounded 的有限 $F$ 输入，全部 trace-dual 坐标的 BSS 测度返回。在已付原二层 LT 系数域中，损失至多 $p^2$。
- 两篇新文在原低节点窗和 affinoid 精度中的具体可用范围，以及(R27)候选的严格检验。

原 quadratic lift、完整 Bessel/Maass 热作用是否给新的 bounded 对象，须按其真实单位域及全部低矩另证；普通 LT 盘上的系数不变性不替代(R11)。原 $J'_S$、Hall 五层或
$\sum_p g_{p,D}\log p>3M_D\log D$ 的主门没有因此免费获得新的必要行。

本篇为纸笔证明及原文核对，无新增数学执行。
