# R267 附录：双平坦原来源的独立双圆相位、严格新分母与双逆级数忠实性

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整原相位构造及全空间忠实性。** 本稿使用前稿已经构造的同一个 $P,Q$ 和全部 $Q_{a,b}=C^{-a}P^{-b}Q$，没有重新选择分母。原高位完整块的局部酉给出一个真实、点范数连续的双圆规范作用；它独立改变 $P,Q$ 的相位并固定原 UHF 代数。由此，$Q$ 不能由旧来源 $C^*$ 代数中的任何非零有界分母表示，确实超出旧正 $P$ 联合闭场。

同一作用在原空间上抽取全部负 $P$ 系数，证明前稿双逆级数的形式实现忠实，因而关闭该类的平方来源。这个作用不被假定保持未知原不变旗；本稿没有把全空间忠实性升级成新分子的全旗单射稠值。

## 1. 全部对象保持原定义

沿用
[同 $P$ 双平坦稿](R267-appendix-same-flat-denominator-all-inverse-powers-and-double-flat-source.md)
的记号：

$$
P=\prod_{\nu\ge1}T_\nu^+,\qquad
T_\nu^+=\frac2{q_\nu+2}\sum_{j\in F_\nu}N_j,\qquad
F_\nu=[m_\nu,m_\nu+q_\nu),\quad q_\nu=256\nu^2,
$$

$$
P=C^{k_n}U^{[n]}\Theta_n,\qquad
V_n=PW_n=\Theta_n E_{m_n+1,64n},\qquad
n_\nu=2^{32+10\nu},
$$

$$
Q=\prod_{\nu\ge1}V_{n_\nu},\qquad
\Psi_r=\prod_{\nu>r}V_{n_\nu},\qquad
Q_{a,b}=R_a\left(\prod_{\nu\le b+1}W_{n_\nu}\right)\Psi_{b+1},
\quad R_a=C^{-a}P.
\tag{1.1}
$$

全部无限积都是前稿已付的强*积；全部有限因子与尾积是收缩。
$Q$、各 $Q_{a,b}$ 已在全部原旗上单射稠值。$W_n\in\mathcal A$；
$R_a$ 可以写成一个固定 $\mathcal A$ 元乘某个固定旧尾 $\Theta_N$。
记原 UHF 代数为 $\mathfrak U=C^*(I,C)$，并令

$$
\mathfrak D_0=C^*(\mathfrak U,\{R_a:a\ge0\}),\qquad
\mathfrak D=C^*(\mathfrak D_0,\{Q_{a,b}:a,b\ge0\}).
\tag{1.2}
$$

这些是同一原 Hilbert 空间内的具体 $C^*$ 代数。

## 2. 高完整块的实际相位费用

给 $t\ge2$、$\theta\in\mathbb R$，令 $U_t(\theta)$ 仅作用于位块 $F_t$，
每个位的矩阵为 $\operatorname{diag}(1,e^{-i\theta})$。
置 $\zeta=e^{i\theta}$。对 $j\in F_t$，准确有
$U_t^*E_jU_t=\zeta E_j$。

所有估计均保真实递推
$N_j=E_j+\eta_jE_j^*N_{j+1}$，不将整个算子换成纯模型。
当 $j<m_t$ 时，逐位递推给

$$
\|U_t^*N_jU_t-N_j\|
\le2\prod_{\ell=j}^{m_t-1}\eta_\ell.
\tag{2.1}
$$

当 $j\in F_t$ 时，纯项相位准确，剩余 carry 给

$$
\|U_t^*N_jU_t-\zeta N_j\|\le2\eta_j.
\tag{2.2}
$$

当 $j>m_t+q_t-1$ 时，$N_j$ 与 $U_t$ 严格交换。
记 $\epsilon_s=e^{-770\,16^s}$。由 $\eta_j\le\epsilon_j$，

$$
\sum_{j<m_t}\|U_t^*N_jU_t-N_j\|
\le4\epsilon_{m_t-1}.
\tag{2.3}
$$

各 $T_\nu^+$ 的标量系数至多一。
先对有限收缩乘积望远镜，再取已付强极限，得到与 $\theta$ 无关的界

$$
\boxed{\|U_t^*PU_t-\zeta P\|\le8\epsilon_{m_t-1}.}
\tag{2.4}
$$

对任意旧尾 $\Theta_n$，当 $n<t$ 时也有

$$
\|U_t^*\Theta_nU_t-\zeta\Theta_n\|
\le8\epsilon_{m_t-1};
\tag{2.5}
$$

当 $n\ge t$ 时它与 $U_t$ 严格交换。
这里低位误差在全部位求和后仍是 (2.3)，没有乘上前缀长度。

$E_{m_n+1,64n}$ 的全部位都在 $F_n$ 内，因为
$64n\le256n^2-1$。因此 $n<t$ 时其共轭误差至多
$4\epsilon_{m_t-1}$；$n>t$ 时严格交换。由 (1.1)、(2.5)，

$$
\boxed{
\|U_t^*V_nU_t-\zeta V_n\|\le16\epsilon_{m_t-1}\quad(n<t),
\qquad [U_t,V_n]=0\quad(n>t).
}
\tag{2.6}
$$

不使用 $n=t$ 的结论；下面选择的块从不等于任何被选前缀编号。

## 3. 同一 $P,Q$ 的两个独立相位

取

$$
t_k=n_k+1.
$$

恰有 $k$ 个被选编号 $n_\nu<t_k$，全部其余编号大于 $t_k$。
所以前 $k$ 个因子各取得一个 $\zeta$，后面无限尾严格交换。
(2.6) 给

$$
\boxed{\|U_{t_k}^*QU_{t_k}-\zeta^kQ\|
\le16k\,\epsilon_{m_{t_k}-1}\longrightarrow0,}
\tag{3.1}
$$

仍对全部 $\theta$ 一致。

任意固定 $\mathfrak U$ 元在这些越来越高的局部酉下渐近范数固定，
对 $\theta$ 一致；先对有限局部矩阵准确交换，再取范数逼近即可。
由 $R_a=(\text{固定 }\mathcal A\text{ 元})\,\Theta_N$ 与 (2.5)，

$$
\|U_{t_k}^*R_aU_{t_k}-\zeta R_a\|\longrightarrow0
\quad(a\text{ 固定}).
\tag{3.2}
$$

对 $Q_{a,b}$ 使用 (1.1) 的原式：
中间有限 $W$ 积属于 $\mathfrak U$，其相位不变；
$\Psi_{b+1}$ 中恰有 $k-b-1$ 个前因子取得相位，其余严格交换。
于是

$$
\boxed{\|U_{t_k}^*Q_{a,b}U_{t_k}
-\zeta^{k-b}Q_{a,b}\|\longrightarrow0
\quad(a,b\text{ 固定}).}
\tag{3.3}
$$

这一步没有从近似 $C^aP^bQ_{a,b}=Q$ 中除以无界逆；
用的是完整有界来源式。

给任意两个目标相位 $\zeta_0=e^{i\alpha}$、$\nu_0=e^{i\beta}$，
选整数 $\ell_k$ 为 $(k\alpha-\beta)/(2\pi)$ 的最近整数，令

$$
\theta_k=\frac{\beta+2\pi\ell_k}{k}.
$$

则 $\theta_k\to\alpha$ 且 $e^{ik\theta_k}=\nu_0$。
将其代入 (2.4)、(3.1)–(3.3)，每个固定生成元的共轭都在范数中收敛。
有限 $*$ 多项式、范数稠密性及内共轭等距性因此给

$$
\boxed{
\gamma_{\zeta,\nu}|_{\mathfrak U}=\mathrm{id},\qquad
\gamma_{\zeta,\nu}(R_a)=\zeta R_a,\qquad
\gamma_{\zeta,\nu}(Q_{a,b})=\nu\zeta^{-b}Q_{a,b}.
}
\tag{3.4}
$$

这是 $\mathfrak D$ 的等距 $*$ 同态。
$\gamma_{\bar\zeta,\bar\nu}$ 在各生成元上给逆，所以它是自同构。
生成元上的连续性与范数稠密性还给一个点范数连续的真实 $\mathbb T^2$ 作用。
它由原局部酉的点范数极限实现，但不被称作原空间上的一个空间酉表示。

特别 $P=R_0$ 的相位为 $\zeta$，$Q=Q_{0,0}$ 的相位为 $\nu$；
二者独立。

## 4. 新分母确实不由旧来源的任何有界分母表示

$\gamma_{1,\nu}$ 固定整个 $\mathfrak D_0$，而把 $Q$ 乘以 $\nu$。
若 $D,E\in\mathfrak D_0$ 且 $QD=E$，施以 $\nu\ne1$ 后相减，
得 $E=0$，再由 $Q$ 单射得 $D=0$。
若 $DQ=E$，同样先得 $E=0$，再由 $Q$ 稠密值域得 $D=0$。
因此

$$
\boxed{
QD=E\ \text{或}\ DQ=E,\quad D,E\in\mathfrak D_0
\quad\Longrightarrow\quad D=E=0.
}
\tag{4.1}
$$

更一般，若有限和 $\sum_{j=0}^dD_jQ^j=0$、$D_j\in\mathfrak D_0$，
对 $\nu$ 作 Fourier 抽取给 $D_jQ^j=0$。
$Q^j$ 稠密值域迫使全部 $D_j=0$。
右侧系数的有限关系由单射性得到同样结论。

此前[正 $P$ 联合解析场](R12-appendix-joint-original-inverse-and-flat-anchor-universal-analytic-field.md)
的所有有界分子、分母均在 $\mathfrak D_0$。
若其某个最大分式等于全域有界的 $Q$，
最大图等式便给一个被 (4.1) 排除的真实有界等式。
所以

$$
\boxed{Q\text{ 不属于该旧联合闭场，亦不属于 }\mathfrak D_0.}
\tag{4.2}
$$

这是前双平坦稿未曾宣称、现在由实际双相位支付的严格范围新增。

## 5. 负 $P$ 抽取所需的临界单变量引理

前稿的预算为 $\|R_a\|\le A_a$，其中 $A_0=1$，对 $a\ge1$，

$$
\log A_a=K_{m_0}a^4
\exp(300[\log(2+a)]^{2/3}).
$$

因此 $A_{2a}\ge A_a^{16}$，且 $\log A_a/a^4\to\infty$。

**引理 5.1。** 若非零整函数
$f(z)=\sum_{a\ge0}c_az^a$ 满足

$$
\sum_{a\ge0}|c_a|A_{2a}<\infty,
\tag{5.1}
$$

则 $F_f=\sum c_aR_a$ 在每个原非零有限放大旗商上单射稠值。

**证明。** 所有级数按原来源预算范数绝对收敛。
由 $A_{2a}\ge A_a^{16}$，对每个固定 $B>0$，充分大的 $a$ 有

$$
a|c_a|A_a\le K_B e^{-Ba^4}.
$$

Young 不等式或直接最大化 $at-Ba^4$ 给

$$
\log^+M_f(R)=o((\log R)^{4/3}).
\tag{5.2}
$$

同源差商 $g_\lambda(z)=(f(z)-f(\lambda))/(z-\lambda)$ 的算子
$G_\lambda=F_{g_\lambda}$ 满足

$$
\|G_\lambda\|
\le\sum_{a\ge1}a|c_a|A_a\max(1,|\lambda|)^{a-1},
$$

故也是算子范数整函数，并有
$\log^+\sup_{|\lambda|\le R}\|G_\lambda\|=o((\log R)^{4/3})$。
原项相加给

$$
(I-\lambda C)G_\lambda=CF_f-CPf(\lambda).
\tag{5.3}
$$

若某原旗商上 $F_fx=0$、$x\ne0$，则同一个
$p=Px\ne0$ 的原预解标量
$H(\lambda)=\langle C(I-\lambda C)^{-1}p,p\rangle$
满足 $H=-\langle G_\lambda x,p\rangle/f(\lambda)$。
对标量 $f$ 剥去可能的原点零，仅用于 Jensen 估计；
其负对数的圆均值为 $o((\log R)^{4/3})+O(\log R)$。
Poisson 核从圆 $2R$ 到圆 $R$ 至多为 $3$，
所以 $\log^+M_H(R)=o((\log R)^{4/3})$。

但该同一旗商的
$C^{2^j}/d_j\to I/2$ 弱返回使 $H$ 的第 $2^j-1$ 个系数
至少为 $d_j\|p\|^2/4$（模长，充分大 $j$）。
取 $n=2^j$、
$R_j=\exp(1000\,16^{m_0}n^3)$，
由 $-\log d_j\le500\,16^{m_0}n^4$ 得
$\log M_H(R_j)\ge250\,16^{m_0}n^4$，与最小型矛盾。
所以单射成立。
对闭像再取原旗商，若其非零则诱导算子为零，违反单射，故值域稠密。证毕。

引理只为当前所需的临界切片给完整来源证明；
没有调用未经支付的任意临界函数演算。

## 6. 真正负 $P$ 双逆来源的全空间忠实性

取前稿定义的同一 $\Lambda_n$、同一类 $\mathscr D$：

$$
F(z,w)=\sum_{a,b\ge0}c_{a,b}z^aw^b,\qquad
\sum_{a,b}|c_{a,b}|\Lambda_{2^k(a+b)}<\infty
\quad(k=0,1,\ldots),
$$

$$
\mathcal B_F=\sum_{a,b}c_{a,b}Q_{a,b}.
\tag{6.1}
$$

这里 $w$ 真表示 $P^{-1}$，并非改回正 $P$ 解析芽。
(3.4) 与同源绝对收敛给

$$
\gamma_{\zeta,\nu}(\mathcal B_F)
=\nu\sum_{b\ge0}\zeta^{-b}
\left(\sum_{a\ge0}c_{a,b}Q_{a,b}\right)
\tag{6.2}
$$

且按算子范数绝对收敛。

若 $\mathcal B_F=0$，固定 $\nu=1$，对 $\zeta$ 作 Fourier 抽取，得到

$$
\sum_{a\ge0}c_{a,b}Q_{a,b}=0\qquad(b\ge0).
\tag{6.3}
$$

乘回真正有界的 $P^b$，利用原来源兼容式，

$$
0=\sum_ac_{a,b}Q_{a,0}
=\left(\sum_ac_{a,b}R_a\right)Q_{0,1}.
\tag{6.4}
$$

$Q_{0,1}$ 已付稠密值域，因此括号中的有界算子为零。
又 $\Lambda_{2(a+b)}\ge A_{2a}$，所以每个切片
$f_b(z)=\sum_ac_{a,b}z^a$ 满足引理 5.1。
由该引理，只有 $f_b=0$ 才能实现零算子。
故全部系数消失，得到

$$
\boxed{\mathcal B_F=0\quad\Longleftrightarrow\quad F=0.}
\tag{6.5}
$$

这直接处理了负 $P$ 的无限端：准确参数是 (6.2) 的全部负 Fourier 次数，
不是把未知的 $w\to\infty$ 行为假装为原正 $P$ 芽的最低阶。

每个单独非零切片在原旗上也单射稠值：
其与 $P^b$ 的乘积是引理 5.1 的 $F_{f_b}$ 乘 $Q_{0,1}$，
两个来源都普遍单射稠值；用交换性即可取消并恢复这个切片的结论。
但整和 (6.1) 的所有旗性质不由此自动推出。

## 7. 同 $Q$ 平方来源的准确结论与尚未覆盖的范围

前稿已经完整支付

$$
Y=\mathcal B_F,\qquad
Y^2=CQ^2
\quad\Longleftrightarrow\quad
\mathcal B_{zF^2-1}=0.
$$

现在 (6.5) 迫使 $zF(z,w)^2=1$ 作为整个函数恒等式成立。
令 $z=0$ 即矛盾。因此

$$
\boxed{\text{不存在 }F\in\mathscr D
\text{ 使 }(\mathcal B_F)^2=CQ^2
\text{ 在整个原空间成立}.}
\tag{7.1}
$$

这关闭了前稿给出的特定双逆平方来源，不排任意 $Y\in C'$。
也没有声称每个非零 $\mathcal B_F$ 都单射稠值：
规范酉不被假定保持未知原旗，故不能直接把 (6.2) 施于某个未保持的核或商。
若这类非零分子确有非零核或非稠密像，它反而会给原算子的真实非平凡闭不变空间；
本稿没有排除或构造这种情况。

实际新结构是 (3.4) 的独立双圆作用及 (4.1) 的全有界分母排除；
新 $Q$ 已严格离开此前联合场，但这个来源类仍没有提供闭平方根。
普通 ISP 与一般非局部原来源继续开放。
