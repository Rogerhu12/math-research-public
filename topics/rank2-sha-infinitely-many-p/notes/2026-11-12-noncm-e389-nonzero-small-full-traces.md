# E389 的真实完整 Heegner 迹：无穷大因子上的非挠性和小高度

日期：2026-11-12。**已证明。** 本篇把 R114–R116 的固定 CM
变形与整数乘积方法，完整用于 R136 的非 CM 曲线和负七域。
得到的是原始点的全部 prime-to-\(p\) 迹 \(Q\) 非挠、
\(\widehat h(Q)=o(p)\) 及 \(Q\) 不可被 \(p\) 整除。
没有把这些结论写成二次增广原始性或主课题完成。

## 1. 固定曲线、两个中心及一个固定挠点乘数

固定 R136 的数据
\[
 E:y^2+y=x^3+x^2-2x,\qquad N=389,\qquad
 F=\mathbb Q(\sqrt{-7}),
 \qquad \pi:X_0(N)\longrightarrow E,\quad\pi(\infty)=O.
 \tag{1}
\]
R136 已严格证明：\(E\) 非 CM，\(\operatorname{rank}E(\mathbb Q)\ge2\)，
\(h_F=1\)，负七扭曲解析秩一、整个 Sha 有限，且两个实际最大阶
\(N\)-Heegner 点 \(c_+,c_-\) 均满足
\[
                         \pi(c_+)=\pi(c_-)=O.
 \tag{2}
\]
这里 \(c_-\) 是 \(c_+\) 的复共轭，分别对应 \(389\) 上的两个
理想方向。因类数一且 \(N\) 为素数，所需中心集合可固定为
\(\Sigma=\{c_+,c_-\}\)；无需随 \(\ell\) 增添中心。
若为细模图加入额外标记，只加入这个集合的固定有限个提升。

**挠点乘数必须另付。** Silverman（2004）作者版 §4
Theorem 3 对任意非 CM \(E/F\) 给
\[
                         E(F^{\rm ab})_{\rm tors}\text{ 有限}.
 \tag{3}
\]
为明确其整数后果，固定一次
\[
                  t_0=\exp E(F^{\rm ab})_{\rm tors},
                  \qquad \Psi=[t_0]\pi.
 \tag{4}
\]
\(t_0\) 独立于随后所有 \(p,\ell\)，不需要知道其数值。
此后可以删去固定的 \(p\mid t_0\) 或 \(\ell\mid t_0\)；
任意 \([t_0]Q\ne O\) 已经证明 \(Q\) 非挠。

为说明 (3) 不只排除大素数阶：Serre 的模 \(r\) 满像对几乎全部
素数 \(r\) 排除非零 \(E(F^{\rm ab})[r]\)，因为任一点的全 Galois
轨道张成 \(E[r]\)，不可能由非阿贝尔满像通过阿贝尔商作用。
对有限个剩余 \(r\)，\(r\)-进像包含
\(1+r^{n_r}M_2(\mathbb Z_r)\)，可令 \(n_r\ge1\)。
取其中的两个对角元和上下三角幺幂元，其交换子分别包含
\[
               1+r^{2n_r}E_{12},\qquad
               1+r^{2n_r}E_{21}.
 \tag{5}
\]
两者都固定阿贝尔域中的挠点，于是其 \(r\)-初级部分被
\(r^{2n_r}\) 杀死。有限乘积给一个实际可固定的整数乘数。
本曲线的 \(j=112^3/389\) 非整，Baker（2003）Theorem 1.4
还直接给整个 \(E(F^{\rm ab})\) 的强离散性，亦蕴含 (3)。

Silverman 同文 Theorem 1（§7 重述为 Theorem 10）给固定常数
\[
 R\in E(F^{\rm ab})\setminus E(F^{\rm ab})_{\rm tors}
       \quad\Longrightarrow\quad \widehat h(R)\ge c_{E,F}>0.
 \tag{6}
\]
因此这里没有把仅限 CM 曲线的 Baker Theorem 1.1 直接用于 (1)。

## 2. 固定 \(q=29\) 的原 ST 测度与指定分支

取 R136 已完整点数核验的
\[
 q=29=N_{F/\mathbb Q}(1+2\sqrt{-7}),\qquad a_{29}(E)=-6.
 \tag{7}
\]
它在源 CM 域 \(F\) 分裂，且目标 \(E\) 在 \(29\) 好普通约化，
\(\#E(\mathbb F_{29})=36\)。源的两个 \(29\) 理想均主，
因此原 \(N\)-Heegner 标记沿该塔保持。这里的 CM 是
**源模曲线点所参数化的椭圆曲线**的 CM；目标 \(E\) 非 CM
不妨碍源的 Serre–Tate 或 Gauss–Manin 比较。

对每个 \(c\in\Sigma\)，固定代数参数及源 CM de Rham 本征基，
用水平化定义一次归一的 period 比 \(v_c\)，
\(v_c(0)=0,v_c'(0)=1\)。置
\[
 F_c(v)=\log_E\Psi(t_c(v))
       =\sum_{m\ge1}b_{c,m}v^m,\qquad
 h_{c,m}=m!b_{c,m}.
 \tag{8}
\]
这些系数在一个固定数域 \(K\) 中。
Katz（1981）Main Theorems 4.3.1–4.3.2 给源的水平基
\[
 \nabla\omega_{\rm ST}=\eta_{\rm ST}\,d\log(1+T),\qquad
 \nabla\eta_{\rm ST}=0.
 \tag{9}
\]
原点处 Hodge 与 unit-root 两线正是源的两个 CM 本征线，
故准确有
\[
                       v_c=\kappa_c\log(1+T),\qquad\kappa_c\ne0.
 \tag{10}
\]
常数可以在完备未分歧 \(29\)-进域中；以下无需把它当作代数周期
或预先证明为单位。

令
\[
 \mathscr F_c(T)=\log_E\Psi(c(T)),\qquad
 G_c(T)=(1+T)\mathscr F_c'(T).
 \tag{11}
\]
(2) 和映射的整延拓使 \(\mathscr F_c(0)=0\)，且其导数整；
所以 \(G_c\in\mathcal O[[T]]\) 是有界整测度 \(\mu_c\) 的
Amice 变换。若原选微分引入固定分母，先乘一次固定整数清除，
不改变下面任何非零性。准确矩恒等式为
\[
             \int_{\mathbb Z_q}x^{m-1}\,d\mu_c(x)
                         =\kappa_c^m h_{c,m}\qquad(m\ge1).
 \tag{12}
\]
本处与 R114/R116 完全相同；(9)–(12) 不使用目标 CM。
还须保留收敛区分：(10) 给形式及小盘恒等式，但在
\(T=\zeta_{q^n}-1\) 处不能将 \(\log\zeta_{q^n}=0\) 直接代回
外层 \(F_c\)。该处始终使用 (11) 的真实全盘原函数；
其系数估值至少为 \(-v_q(m)\)，故在整个开单位盘收敛。

采用的指定分支为
\[
 \mathscr M_c(W)=
 \int_{\mathbb Z_q^\times}x^{-1}
       (1+W)^{\log\langle x\rangle/\log(1+q)}\,d\mu_c(x).
 \tag{13}
\]
这保留 tame 指数 \(-1\)，不是仅选某个未知非零分支。

### 2.1 原 Heegner 迹的两个初层

固定每一种 \(389\) 理想方向，令 \(P_n=\pi(x_{q^n})\)，
\(K_n=F[q^n]\)，\(K_0=F\)，并令 \(H_r/F\) 为反圆分
\(\mathbb Z_q\) 塔的次数 \(q^r\) 子层。类数一给
\[
 \operatorname{Gal}(K_n/F)\simeq(\mathbb Z/q^n)^\times,\quad
 K_n\cap H_\infty=H_{n-1}\quad(n\ge1).
 \tag{14}
\]
定义真正整数点
\[
 Z_0=P_0=O,\qquad
 Z_n=\operatorname{Tr}_{K_n/H_{n-1}}P_n
                  =\sum_{\mu_{q-1}}gP_n\quad(n\ge1).
 \tag{15}
\]
两条水平 \(q\)-同源和后续唯一回升支给准确递推
\[
 \begin{aligned}
 Z_1&=(a_q-2)Z_0=O,\\
 \operatorname{Tr}_{H_1/F}Z_2&=a_qZ_1-(q-1)Z_0,\\
 \operatorname{Tr}_{H_{n-1}/H_{n-2}}Z_n
                &=a_qZ_{n-1}-Z_{n-2}\quad(n\ge3).
 \end{aligned}
 \tag{16}
\]
特别第二行的 \(q-1=28\) 不能删去；这里未作 unit-root 稳定化。
由于 \(\pi(\infty)=O\) 且 \(E(\mathbb Q)_{\rm tors}=0\)，
这些实际点式没有未处理的尖点常数。

Cornut（2002）引言主定理断言至少一个 (15) 非挠。
其假设是原 \(N=389\) 的 Heegner 条件和 \(q\nmid N\)，
不要求目标有 CM 或基层点非挠。该定理适用于这里每个固定
Heegner 理想方向；也可在其 §4 Theorem A 中取平凡有限角色。

### 2.2 指定分支非恒零，而非仅整个系统非零

Katz Theorem 2.1(4) 及普通 CM 互反律使
\(T=\zeta_{q^n}^a-1\)、\(a\in(\mathbb Z/q^n)^\times\)，
恰为该最大阶 CM 中心上方的实际原始导子 \(q^n\) 轨道。
由 (11) 的原函数核，对 conductor 恰为 \(q^n\)、tame 平凡的
非平凡字符 \(\chi\)，\(n\ge2\)，有
\[
 \sum_a\chi^{-1}(a)\mathscr F_c(\zeta_{q^n}^a-1)
 =\tau(\chi^{-1})
       \int_{\mathbb Z_q^\times}x^{-1}\chi(x)\,d\mu_c(x).
 \tag{17}
\]
非零 Gauss 和乘数以及原 \(N\) 标记都保持，左侧是
\([t_0]Z_n\) 的原始 wild Fourier 对数和。

若 (13) 恒零，则对
\(J_n=\operatorname{Gal}(H_{n-1}/H_{n-2})\) 及
\(N_n=\sum_{g\in J_n}g\)，字符正交性给
\[
                 \log_E([t_0](q-N_n)Z_n)=0.
 \tag{18}
\]
\([t_0](q-N_n)Z_n\) 是有限扩域中的真实整数点。
有限局部域上椭圆曲线对数的核为挠点，故 \((q-N_n)Z_n\)
为挠点。由 (16) 从 \(Z_0,Z_1\) 归纳，全部 \(Z_n\) 都为挠点，
与 Cornut 矛盾。因此
\[
                            \mathscr M_c\ne0\quad(c\in\Sigma).
 \tag{19}
\]
没有使用 Mordell–Weil 的 \(\mathbb Q_q\) 张量到一维局部对数的
虚假注入性；(18) 中的整数算子是必要的。

### 2.3 固定非零进程

写 \(\mathscr M_c(W)=A_dW^d+\cdots\)、\(A_d\ne0\)。
取 \(k_c\) 使 \(k_c+1>v_q(A_d)\)。若
\((q-1)q^{k_c}\mid m\)，则
\[
 v_q\mathscr M_c((1+q)^m-1)
       =v_q(A_d)+d(1+v_q(m))=O(\log m).
 \tag{20}
\]
这是首项严格支配；其余测度部分在 \(q\mathbb Z_q\) 上的矩
估值至少 \(m-1\)，不能对充分大 \(m\) 抵消 (20)。
结合 (12)，并在固定有限 \(\Sigma\) 上取最大阈值，得到固定
\[
 C=28\cdot29^k,\qquad m_0,\qquad
 C\mid m,\ m\ge m_0\ \Longrightarrow\
                         h_{c,m}\ne0\quad(c\in\Sigma).
 \tag{21}
\]
未知但固定的 \(k,m_0\) 已足以选下面的固定进程，不需要有效计算。

## 3. 惰性辅助位的完整迹低 jet

取 \(\ell\) 在 \(F\) 惰性，避开固定有限坏集。源 CM 曲线在
\(\ell\) 超奇异，但这里只要求目标 \(E\) 在 \(\ell\) 好约化；
不要求 \(a_\ell(E)=0\)，也不要求 \(\ell\) 在另一个 CM 域惰性。

R114 的局部证明仅使用源 CM 本征基、带标记的
quasi-canonical 变形，以及固定映射的整对数微分。因此它逐项
适用于 (1)、(4)。简录完整参数与尾界，避免仅凭改名引用：
在某个实际目标中心 \(c\in\Sigma\) 的盘中，令 \(d=\ell+1\)。
源的 tame CM 自同构商阶为 \(d\)，以整平均线性化得
\[
 w\in t\mathcal O_B[[t]],\quad w'(0)=1,\qquad
 v_c(t(w))=w+O(w^{d+1}).
 \tag{22}
\]
真实 \(\ell\)-邻点满足
\[
                  w=r,\quad r^d=c_\ell\in\ell\mathcal O_B^\times,
 \qquad \sigma_\zeta r=\zeta r\quad(\zeta\in\mu_d).
 \tag{23}
\]
这里 \(B/\mathbb Q_\ell\) 是固定数据所需的有限未分歧扩张，
可含 \(\mu_{\ell^2-1}\)；\(c_\ell\) 与 \(w\) 随 \(\ell\) 变，
固定的是 (8) 的 period 级数。

置
\[
 \log_E\Psi(t(w))=\sum_{m\ge1}a_{\ell,m}w^m.
 \tag{24}
\]
整微分给 \(m a_{\ell,m}\in\mathcal O_B\)，故
\(v_\ell(a_{\ell,m})\ge-v_\ell(m)\) 且全开盘收敛；
(22) 给 \(a_{\ell,m}=b_{c,m}\) 对 \(m\le d\)。

设 \(\ell+1=pu\)、\(u\ge3\)，令
\[
 H_\ell=F[\ell],\quad L=H_\ell^U,\quad |U|=u,\qquad
 Q=\operatorname{Tr}_{H_\ell/L}P[\ell],\quad s=r^u,\quad s^p=c_\ell.
 \tag{25}
\]
因 \(h_F=1\)，这个 \(Q\) 已是原全部 prime-to-\(p\) 迹，
没有待补的类数和。为写下面的双和，约定 \(a_{\ell,0}=0\)，
与 (24) 从 \(m=1\) 起的原级数一致。对根单位作实际和，得
\[
 \log_E([t_0]Q)
   =u\sum_{j=0}^{p-1}s^j
             \sum_{k\ge0}a_{\ell,u(j+kp)}c_\ell^k.
 \tag{26}
\]
\(1,s,\ldots,s^{p-1}\) 是真实局部扩域的整基。
对 \(k\ge1\)、\(1\le j\le p-1\)，
\[
 v_\ell(a_{\ell,u(j+kp)}c_\ell^k)
                  \ge k-v_\ell(j+kp)\ge1,
 \tag{27}
\]
且右侧趋于无穷；\(j=0\) 也有 \(k-v_\ell(k)\ge1\)。
不等式只用 \(p\le(\ell+1)/3\)，与目标是否 CM 无关。
因此首基系数模 \(\ell\) 是 \(b_{c,u}\)，并准确有
\[
 \boxed{\quad
 b_{c,u}\not\equiv0\pmod\ell
 \ \Longrightarrow\
 v_\ell\log_E([t_0]Q)=1/p
 \ \Longrightarrow\ Q\text{ 非挠}.
 \quad}
 \tag{28}
\]
最后一步使用 (4)，或直接用非零对数的核性质。
这保留实际完整迹和全部高项的控制，没有把原 \(P[\ell]\)
非挠直接转给 \(Q\)。

## 4. 非零整数产品及真正的大素因子选择

R116 §1 的固定多项式向量场证明适用于本篇 (8)：加入源
Gauss–Manin 基本矩阵、其逆、有限个代数分母的倒数以及
\(\log_E\Psi\)，以 \(d/dv_c\) 作导子，得到固定有限多项式系统。
于是存在固定整数 \(A,D\) 与常数 \(C_1\)，使
\[
 B_{c,m}:=A^{Dm+1}h_{c,m}\in\mathcal O_K,\qquad
 \log\max\{1,|N_{K/\mathbb Q}B_{c,m}|\}
                         \le C_1m\log(m+2).
 \tag{29}
\]
这里只是代数系数及 Hurwitz 导数的高度估计，
未把逆 period 后的 (8) 称为代数函数。

对 (21) 中的指标定义非零整数
\[
 J_m=\prod_{c\in\Sigma}N_{K/\mathbb Q}B_{c,m},
 \qquad \log|J_m|\ll m\log(m+2).
 \tag{30}
\]
选一次固定正整数 \(B_0\)，满足
\[
             C\mid B_0,\qquad B_0\ge\max(m_0,3).
 \tag{31}
\]
因 \(7\mid C\)，已有 \(7\mid B_0\)；可再乘任意固定模型因子。
所有常数及 \(B_0\) 先固定，然后才令 \(x,p,\ell\) 变化。

令 \(\theta=667/1000\)。R126 的固定进程大素因子定理和
R138 的严格例外删除，在 \(\ell\equiv-1\pmod{B_0}\) 中给
\(\gg_{B_0}x/\log x\) 个候选
\[
 \begin{gathered}
 \ell\le x,\qquad p=P^+(\ell+1)>x^\theta,\qquad
 a_p(E)\not\equiv0,\pm1\pmod p,\qquad a_\ell(E)\not\equiv0\pmod p,\\
 v_p(\ell+1)=1,\qquad
 u=(\ell+1)/p\le x^{1-\theta}+1.
 \end{gathered}
 \tag{32}
\]
充分大 \(p\) 不除固定 \(B_0\)，所以 \(B_0\mid u\)。
因此 (21) 对每一个候选的 \(u\) 都适用，无需再处理未知的
小 \(u\) 例外。由 \(\ell\equiv-1\pmod7\)，\(\ell\) 在 \(F\) 惰性。
本构造**不要求输入 \(p\) 在 \(F\) 分裂**。

删去所有 \(\ell\mid J_u\) 的候选。设
\(U_x=\lceil x^{1-\theta}+1\rceil\)。这些 \(\ell\) 全是
\[
              \prod_{\substack{m_0\le m\le U_x\\ C\mid m}}|J_m|
 \tag{33}
\]
的素因子，其对数至多 \(O(U_x^2\log U_x)\)。
而 \(\ell\ge p-1>x^\theta-1\)，所以不同坏候选的数量至多
\[
             O(U_x^2)=O(x^{\,2-2\theta})
                    =O(x^{666/1000})=o(x/\log x).
 \tag{34}
\]
每个 \(\ell+1\) 只能有一个大于 \(x^\theta\) 的素因子，
因此此计数没有给同一坏素数重复支付整数预算。
固定有限坏位也不影响下界。

仍有 \(\gg x/\log x\) 个候选满足 \(\ell\nmid J_u\)。
这说明当前实际中心的 \(h_{c,u}\)，从而 \(b_{c,u}\)，在所有
相关 \(\ell\)-位为单位：\(u<\ell\)，故 \(u!\) 是单位，
\(\ell\nmid A\)。由 (28)，这些候选的原完整 \(Q\) 均非挠，
且有准确的辅助位大小 \(v_\ell\log_E([t_0]Q)=1/p\)。

每个 \(p>x^\theta\) 至多对应 \(O(x^{1-\theta})\) 个 \(\ell\le x\)，
故本构造至少给
\[
                         \gg x^\theta/\log x
 \tag{35}
\]
个不同 \(p\)，特别是无穷多个。
这不是把两个无限集合相交：非零迹坏集和 R138 的坏集都用
\(o(x/\log x)\) 上界从同一个大素因子集合中删除。

## 5. 实际高度、不可除性与规范范数

对固定模参数化和固定 \(F\)，源 CM 的 \(j\)-高度及固定态射的
高度比较给
\[
                           \widehat h(P[\ell])\ll\log\ell.
 \tag{36}
\]
R102 §1 已逐步证明这项估计：Pazuki（2019）Theorem 1.1(1)
把导子 \(\ell\) 的源 \(j\)-高度以最大阶 CM 源的固定高度加
\(12\log\ell\) 控制，再与固定 \(\pi\) 拉回的 ample 高度比较。
这部分也不要求目标 CM。

典范高度平方根的三角不等式及 Galois 不变性给
\[
 \widehat h(Q)\le u^2\widehat h(P[\ell])
       \ll u^2\log\ell
       \ll p^{666/667}\log p=o(p),
 \tag{37}
\]
其中用了 \(x<p^{1000/667}\) 和 (32)。
由 (6)，充分大 \(p\) 时
\[
                           Q\notin pE(F^{\rm ab}),
 \tag{38}
\]
特别 \(Q\notin pE(H_\ell)\)。若存在这样的非挠除点 \(R\)，
则 \(\widehat h(Q)=p^2\widehat h(R)\ge c_{E,F}p^2\)，
与 (37) 矛盾。

原 Heegner 分布仍给
\[
             N_{L/F}Q=\operatorname{Tr}_{H_\ell/F}P[\ell]
                           =a_\ell P[1]=O.
 \tag{39}
\]
因此 \(Q\) 是真实 norm-one 点。不过非 CM 情形的高层
\(Y_n\) 仍满足 \(N_\Gamma Y_n=a_\ell P[n]\)，未必为零。
R139 因而以 \((\tau-1)Y_n\) 为实际 norm-one Euler 族，
其 leading 为 \(\delta Q\)。本篇不删去这个额外 \(\delta\)。

若同时使用 R139 的实际 rank-one \(\mathbb Z_p[\zeta_p]\) 格，
R109/R126 的整数二次 Gauss 算子论证仍适用：它只用
Galois 不变的典范高度、\(N_\Gamma Q=0\) 和 (6)，不使用 CM。
由 (37) 得
\[
                          a\le(p-3)/2.
 \tag{40}
\]
简言之，若 \(a\ge(p-1)/2\)，该 Gauss 算子 \(\mathcal G\)
满足 \(\mathcal GQ=pR\)（在实际饱和格中，且删去 \(p\mid t_0\)
后可消去挠点误差），同时
\(\widehat h(\mathcal GQ)=p\widehat h(Q)\)。
于是 \(\widehat h(R)=\widehat h(Q)/p=o(1)\)，违背 (6)。
(40) 仍允许 \(a=2\)，不能据此完成 R139 的两步检验。

## 6. 已付输入与尚未完成的部分

所得无穷组实际 \((p,\ell,Q)\) 同时满足：

- \(p\) 好普通且 \(a_p\not\equiv\pm1\)，\(\ell\) 在 \(F\) 惰性，
  \(a_\ell\) 为 \(p\)-单位，\(v_p(\ell+1)=1\)；
- 原全部 prime-to-\(p\) 迹 \(Q\) 非挠，
  \(N_{L/F}Q=O\)，\(\widehat h(Q)=o(p)\)，且 (38)；
- R138 的 \(H^1(F_\ell,E[p])=0\) 和 R139 的局部条件/整 KS
  输入可以对这些**同一组点**使用。

尚未证明的是原 \(Q\) 的二次增广不整除，或等价充分条件中的
实际半局部二阶矩非零。固定 \(q=29\) 的指定分支非恒零只用于
特征零固定 jets 的非零进程；它没有自动给变化中的 \(p\)-进
二阶矩一个非零值。

## 一手来源及既有完整证明

- J. H. Silverman，*A lower bound for the canonical height on elliptic
  curves over abelian extensions*，J. Number Theory **104** (2004)，
  353–372；[作者全文](https://arxiv.org/pdf/math/0305041)，
  Theorem 1（印 p.1）、§4 Theorem 3（印 pp.7–8）、
  §7 Theorem 10。本文已亲核非 CM 挠点有限性和全阿贝尔域高度下界。
- M. Baker，*Lower bounds for the canonical height on elliptic curves
  over abelian extensions*，IMRN **2003**，1571–1589；
  [作者全文](https://arxiv.org/pdf/math/0212132)，Theorem 1.4。
  本曲线非整 \(j\) 的强离散性可作为独立检查。
- C. Cornut，*Mazur's conjecture on higher Heegner points*，
  Invent. Math. **148** (2002)，495–523；
  [发表排版版](https://webusers.imj-prg.fr/~christophe.cornut/papers/mcinv_published.pdf)，
  引言主定理（PDF p.2）、§4 Theorem A（PDF p.22）。
- N. Katz，*Serre–Tate local moduli*，LNM **868** (1981)，
  [作者全文](https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf)，
  Theorem 2.1(4)、Main Theorems 4.3.1–4.3.2（印 p.175）。
- J.-K. Yu（1995）及 André（2004）的 actual quasi-canonical
  lift/period 比较，准确位置和整平均证明见
  [R114 完整稿](2026-11-12-small-heegner-trace-and-cm-period-jets.md)。
- [固定 ST/Gauss 核](2026-11-12-fixed-ordinary-st-mellin-branch.md)、
  [Cornut 整数投影归纳](2026-11-12-cornut-fixed-branch-and-nonzero-progression.md)、
  [固定多项式系统高度](2026-11-12-fixed-cm-jet-heights-and-prime-product.md)：
  本篇已列出对 E389 必须改变的实际数据和初层。
- [R136](../results/R136-noncm-e389-minus7-heegner-input.md)、
  [R138](../results/R138-noncm-large-factor-exception-deletion.md)、
  [R139 完整稿](2026-11-12-noncm-norm-one-system-and-two-step-test.md)。
