# 固定挠点 connection、原四首行与完整 Frobenius 初始资料

日期：2026-11-15。**状态：下列有理恒等式、固定 Mumford 倍率、原窗口运输、极帽和初始资料已证明。**

本篇在 R636/R647 的原有理模型上，先固定一个与 $p$ 无关的整数
$M$，使原 $p$-基对 $E[M]$ 严格不变，并把 connection 的平移
差恢复为准确的 Mumford 对数比。四个原 $\alpha_{p+1}$ 全部保持。

同时，本篇明确计算了这个模型在非零 $E[M]$ 点的原始资料：
它在那里至少有 $p$ 阶零。因而即使 connection 已按固定 theta
群协变，也不能把裸有理 isogeny trace 当作原 theta trace。
第 8 节给出必须保留的完整 frame 和它对原 $S$ 首行的准确差。

## 1. 固定 $M$、原曲线和原整窗口

先在共同模型 $E_b:y^2=x^3+b$ 上工作，$b$ 为原固定单位。
取
$$
p=6s-1>211,\qquad d=p+1,\qquad
c=[z^{p+1}]\log(\sigma/z),\qquad v_p(c)=-1.
\tag{1}
$$
$\omega_E=dx/(2y)=dz$，$Dx=2y,\ Dy=3x^2$，$\sigma\sim z$。
所有模 $p$ 的局部比较都在 R636/R647 已付的原有限整窗口中进行，
不将整个特征零形式对数直接约化。

固定一个正整数 $M$，然后才让 $p$ 变化；始终删去 $p\mid M$。
若要一次覆盖四个 theta 群和下文的 CM13，可以固定
$$
\operatorname{lcm}(34,72,136,66,13)\mid M.
\tag{2}
$$
不随 $p$ 改变 $M$。除原固定坏集外，固定 Mumford 数据的系数场和
固定整模型所需的有限坏处也一并保留；这不是增加一个随 $p$
变化的同余条件。

在 $K=k(E_b)$ 中沿用 R636 的**同一个**
$$
Z=\mathscr R_p(x)/y^p,\qquad
G=\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}D^i(-x)}{(i+1)!},
\quad r=x^2/y,\quad H_G=G+r.
$$
其完整已付等式是
$$
DZ=1,\quad D^p=0,\quad DG=-x+c_pZ^{p-1},
$$
$$
D^{p-1}G=r^p,\quad
Z=z+O(z^{5p}),\quad
H_G=(3b/5)z^5+O(z^{11}),
\tag{3}
$$
其中 $c_p\in k^\times$ 是 R636 的原常数。
置 $\sigma^\circ=\sigma e^{-cz^d}$、
$\zeta^\circ=D\log\sigma^\circ$，则
$$
\zeta^\circ-G=(3b/5)^p z^{6p-1}+O(z^{6p}).
\tag{4}
$$
本篇的 $c$ 与 $c_p$ 不混同。

## 2. 固定 division 函数及完整 Mumford 倍率

取原 sigma 半特征，定义固定的真实 division 函数
$$
\Psi_M(z)=\frac{\sigma(Mz)}{\sigma(z)^{M^2}},
\qquad
B_M=\frac{D\Psi_M}{\Psi_M}
=M\zeta(Mz)-M^2\zeta(z).
\tag{5}
$$
$\Psi_M$ 是 $E_b$ 上有理函数，首项为
$M z^{1-M^2}$，并且
$$
\operatorname{div}(\Psi_M)=[M]^*(O)-M^2(O),\qquad
DB_M=-M^2x(Mz)+M^2x(z).
\tag{6}
$$
偶 $M$ 也使用 (5) 的同一 sigma 定标；例如 $\Psi_2=-2y$。
不另改 division 函数的符号。$p\nmid M$ 保证所需原点 Laurent
展开的分母为单位。

为完整列出平移常数，先在特征零选定周期格 $\Lambda$、准周期
$\eta_\lambda$ 和原半特征 $\epsilon_\Lambda(\lambda)\in\{\pm1\}$：
$$
\sigma(z+\lambda)=\epsilon_\Lambda(\lambda)
 e^{\eta_\lambda(z+\lambda/2)}\sigma(z).
$$
对 $\tau\in M^{-1}\Lambda/\Lambda$ 固定一个代表，置
$$
e_\tau=\eta_{M\tau}/M,\qquad
g_\tau(z)=
 e^{-e_\tau(z+\tau/2)}\frac{\sigma(z+\tau)}{\sigma(z)}.
\tag{7}
$$
$g_0=1$。乘法公式准确给
$$
\boxed{
g_\tau^{M^2}
=\epsilon_\Lambda(M\tau)\,
 \frac{\Psi_M(z)}{\Psi_M(z+\tau)}.
}
\tag{8}
$$
因此这些倍率在一个固定的有限代数 theta cover 上定义；
cover 和全部根单位先于 $p$ 固定，分支支持在固定 $E[M]$。
不是从对数导数恢复后再任意选择一个常数。

当所用代表可直接相加时，完整 cocycle 是
$$
\boxed{
g_\tau(z)g_\upsilon(z+\tau)
=e^{(e_\tau\upsilon-e_\upsilon\tau)/2}\,
 g_{\tau+\upsilon}(z).
}
\tag{9}
$$
该指数是 Legendre 配对的有理倍，给固定根单位。
若代表加法另差 $\lambda\in\Lambda$，还须保
$$
\frac{g_{\tau+\lambda}}{g_\tau}
=\epsilon_\Lambda(\lambda)
 e^{(\eta_\lambda\tau-e_\tau\lambda)/2}.
\tag{10}
$$
(8)–(10) 一并规定本篇的绝对倍率和原半特征。
约化只在这些固定数据的好处进行。

## 3. 新 $p$-基与 connection 的完整恒等式

定义
$$
\boxed{
Z_M=\frac{[M]^*Z}{M},\qquad
G_M=\frac{[M]^*G}{M}-\frac{B_M}{M^2},\qquad
H_M=\frac{[M]^*H_G}{M}.
}
\tag{11}
$$
它们是 $K$ 中完全指定的有理函数，没有加入可自由选择的
水平项。因为目标剩余域内 $M^p=M$，逐项求导得到
$$
\boxed{
DZ_M=1,\qquad
DG_M=-x+c_pZ_M^{p-1}.
}
\tag{12}
$$
这里 $M^{p-1}=1$ 只用于整数 $M$ 的剩余类；
没有把一般 CM 元素也按该式处理。

每个 $\tau\in E[M]$ 都有
$$
\boxed{
Z_M(z+\tau)=Z_M(z),\qquad
G_M(z+\tau)-G_M(z)
=\frac{B_M(z)-B_M(z+\tau)}{M^2}
=D\log g_\tau.
}
\tag{13}
$$
最后一式由 (8) 得到；特征零中它等于
$\zeta(z+\tau)-\zeta(z)-\eta_{M\tau}/M$。
所以这里只需固定 Mumford 倍率，不再出现
$Z(z+\tau)-Z(z)=a_\tau^p$ 所产生的长截断对数。

对任意当前 $m\in\mathbf F_p^\times$，置
$$
\nabla_{m,M}=D-mG_M.
$$
有完整曲率式
$$
\boxed{\nabla_{m,M}^p=-mH_M^p.}
\tag{14}
$$
为核绝对常数，取整数 $j$ 代表 $m/M^2\bmod p$，
以 $\Psi_M^{-j}$ 作代数共轭，则
$$
(\Psi_M^{-j})^{-1}\nabla_{m,M}\Psi_M^{-j}
=D-\frac mM[M]^*G.
$$
Jacobson 公式、(3) 及 $M^p=M$ 给
$$
\left(D-\frac mM[M]^*G\right)^p
=-\frac mM[M]^*(D^{p-1}G+G^p)
=-mH_M^p.
$$
曲率是乘法算子，共轭不改变它。$j$ 只是这一证明中的代表，
不是替换原来源的一个新权。

在固定 cover 上，准确的双向 gauge 交织为
$$
\nabla_{m,M}\big(g_\tau^{-m}f(z+\tau)\big)
=g_\tau^{-m}(\nabla_{m,M}f)(z+\tau),
\tag{15}
$$
$$
(D+mG_M)\big(g_\tau^m f(z+\tau)\big)
=g_\tau^m((D+mG_M)f)(z+\tau).
\tag{16}
$$
所有 (9)–(10) 的常数原样留在两边。

## 4. 原 Gaussian 的准确变化

定义原形式来源的整重标
$$
\sigma_M=\sigma\exp(-cM^{p-1}z^d),\qquad
\zeta_M=D\log\sigma_M.
$$
因为
$$
c(M^{p-1}-1)=pc\,q_p(M)\in\mathcal O,\qquad
q_p(M)=\frac{M^{p-1}-1}{p},
\tag{17}
$$
它与原 $\sigma^\circ$ 只差一个已经明确列出的整 Gaussian。
$q_p(M)$ 没有被假定为单位。

由 (5)，原点窗口内准确有
$$
\zeta_M-G_M
=\frac1M\big(\zeta^\circ(Mz)-G(Mz)\big).
$$
所以 (4) 给
$$
\boxed{
\zeta_M-G_M
=(3b/5)^pM^{6p-2}z^{6p-1}+O(z^{6p}).
}
\tag{18}
$$
等价地，若与原 $\zeta^\circ$ 比较，必须保
$$
G_M-\zeta^\circ
=-dc(M^{p-1}-1)z^p+O(z^{6p-1}).
\tag{19}
$$
(19) 的 $z^p$ 项正是不能漏掉的 Fermat/Gaussian 修正。
本篇保留它；并未把 $M^{p-1}\equiv1$ 误用到有一个 $p$ 分母的
特征零系数 $c$ 上。

## 5. 无新根选择的原 degree-two 模型运输

直接在 $K$ 中定义
$$
\boxed{
\mathcal P_{2,M}
=-\nabla_{2,M}^{p-1}(Z_M^{p+1})
=\sum_{j=0}^{p-1}\frac{(-Z_M)^j}{j!}
       \nabla_{2,M}^{\,j}(Z_M^2).
}
\tag{20}
$$
第二式是 Leibniz 与 Wilson 的完整等式，不添加任意
$p$ 次幂常数。由 (14)，
$$
\boxed{
\nabla_{2,M}\mathcal P_{2,M}
=2H_M^pZ_M^{p+1}.
}
\tag{21}
$$

在原点，$Z_M=z+O(z^{5p})$，$G_M=z^{-1}+O(z^5)$，
且 (20) 中 $j\ge1$ 的项不贡献首个 $z^2$，故
$\mathcal P_{2,M}=z^2+\cdots$。它与 $\sigma_M^2$ 同为
$\mu_6$ 型二。结合 (18)、(21)，
$$
D(\mathcal P_{2,M}/\sigma_M^2)=O(z^{6p-1}).
$$
对 $1\le h<p$，$6h$ 为单位；同型只容许 $z^{6h}$。
因此
$$
\boxed{
\mathcal P_{2,M}=\sigma_M^2+O(z^{6p+2}).
}
\tag{22}
$$
这里仍只断言原已付有限整窗口中的相等。

把四个原来源写成
$$
A_\nu=\sigma^{m_\nu}R_\nu(x,y),\qquad
m_\nu=(34,72,136,66),\quad n_\nu=m_\nu/2.
$$
$R_\nu$ 是 R821 的完整原多项式，在 $O$ 的极阶恰为
$m_\nu-6$，没有其它极点。定义
$$
\widehat A_{\nu,M}=\mathcal P_{2,M}^{n_\nu}R_\nu(x,y).
$$
(22) 立即给
$$
\boxed{
\widehat A_{\nu,M}
=A_\nu e^{-m_\nu cM^{p-1}z^d}+O(z^{6p+6}),
\qquad
[z^{p+1}]\widehat A_{\nu,M}=\overline{\alpha_\nu}.
}
\tag{23}
$$
最后一步使用原来源的六阶零；Gaussian 第一修正从
$z^{p+7}$ 才进入。四条实际首行没有被改成新的测试。

原 Cartier 读取也完整保留：
$$
\boxed{
\overline{\alpha_\nu}
=\left(
 \frac{\mathcal C(Z_M^{-2}\widehat A_{\nu,M}\omega_E)}
 {\omega_E}(O)
\right)^p.
}
\tag{24}
$$
所读函数在 $O$ 正则；$Z_M=z+O(z^{5p})$ 足以保证同一系数。
(24) 没有删去 $Z_M$ 的其它零点或其全局极点。

### 5.1 实际极帽

记 $\mathcal D_2$ 为三个非零二挠点之和，令
$$
\mathcal D_M=[M]^*\mathcal D_2.
$$
它含 $3M^2$ 个固定 $2M$-挠点，且与 $E[M]$ 不交。
$Z_M$ 在每个点的极阶至多 $p$。
$G_M$ 在每个 $\mathcal D_M$ 点的极阶至多 $p(p-1)$。

在非零 $\tau\in E[M]$，$[M]^*G/M$ 的简单主部为
$1/(M^2z_\tau)$，而 $B_M/M^2$ 的主部也为该式，准确抵消。
在 $O$ 则留下 $1/z$。因此 $G_M$ 的其它极点确实只有
$\mathcal D_M$，没有遗漏一批 $E[M]$ 简单极。

由 (20) 得
$$
\boxed{
(\mathcal P_{2,M})_\infty
\le(p^3-p^2+2p)\mathcal D_M,\qquad
(\widehat A_{\nu,M})_\infty
\le n_\nu(p^3-p^2+2p)\mathcal D_M.
}
\tag{25}
$$
原点的极已经由 (22)、(23) 消去。
这是固定 $M^2$ 倍的真实 $p^3$ 成本，不是固定 degree2
或 degree-$m_\nu$ 的有理函数池。固定 theta cover 也不消除这个成本。

## 6. 非零挠点处的原始 Frobenius 资料

对每个非零 $\tau\in E[M]$，
$Z_M$ 在 $\tau$ 简单为零，$G_M$ 正则，$H_M$ 至少五阶为零。
由 (20)，
$$
\mathcal P_{2,M}(\tau)=0.
$$
再取该点的局部微分参数，(21) 右端至少为 $6p+1$ 阶。
由于 $1,\ldots,p-1$ 均可逆，从零常数项逐项解前 $p-1$ 个
系数，得到
$$
\boxed{
\operatorname{ord}_\tau\mathcal P_{2,M}\ge p,\qquad
\operatorname{ord}_\tau\widehat A_{\nu,M}\ge n_\nu p.
}
\tag{26}
$$
后一式因 $R_\nu$ 在非零点正则成立。

这正是此**指定模型**的 Frobenius 初始资料。它通常不同于
原 Mumford 平移后 theta 截面的初始值；例如原
$\sigma^2$ 在非零 $\tau$ 的 reduced theta 值非零，
而 (26) 为零。connection 协变 (13) 本身不能把这两种资料相认。

## 7. 有限 theta 群交织的准确范围

若 $m\mid M$，在原 $\sigma^m$ frame 中，固定
$\tau\in E[m]$ 的真实 theta 群作用是
$$
T_\tau P=g_\tau^mP(z+\tau).
$$
$g_\tau^m$ 是有理倍率，且保留 (9)–(10) 的 cocycle。
(16) 给它与 $D+mG_M$ 的完整交织。

任何原固定 CM 矩阵 $A$ 在
$H^0(E,\mathcal O(mO))$ 上都有唯一的有限展开
$$
A=\sum_{\tau\in E[m]}a_\tau T_\tau,\qquad
a_\tau=\frac1m\operatorname{Tr}(T_\tau^{-1}A).
\tag{27}
$$
理由是完整 Heisenberg 矩阵满足
$\operatorname{Tr}(T_\tau^{-1}T_\upsilon)=m\delta_{\tau,\upsilon}$。
因此同一有限和定义了一个作用于完整
$\bigcup_{r\ge0}H^0(E,\mathcal O(mO+r\mathcal D_M))$
的算子 $\widetilde A$，并有
$$
\boxed{
(D+mG_M)^j(AP)=
\widetilde A(D+mG_M)^jP,\qquad j\ge0.
}
\tag{28}
$$
所有 $a_\tau$ 是原固定矩阵及绝对 theta 群的系数；
没有按一个猜测的剩余特征换标量。

(28) 是从原 holomorphic 来源出发的真实有限 theta 群交织。
但在较大极帽上，$\widetilde A$ 是 (27) 所指定的延拓；
不能另认成未经 frame 修正的裸几何 trace。
尤其读取除以 $(p+1)!$ 的首 jet，还须保留 (23)–(26)
及原整系数，不能只用一个特征值就宣布非零。

## 8. CM13 的裸 trace 与原 theta trace，逐项分开

现假定 $13\mid M$，取原
$\gamma=(7+\sqrt{-3})/2$，$N\gamma=13$。
设
$$
Q_\gamma(w)=\frac{\sigma(\gamma w)}{\sigma(w)^{13}},
\qquad Q_{\bar\gamma}(w)
=\frac{\sigma(\bar\gamma w)}{\sigma(w)^{13}},
$$
使用 R297 的完整 leading constants。

先作裸有理 trace
$$
\mathcal U_\gamma(\widehat A_{\nu,M})(z)
=\sum_{\gamma w=z}\widehat A_{\nu,M}(\bar\gamma w).
\tag{29}
$$
非恒等纤维在 $\ker\gamma\setminus\{O\}$。
$\bar\gamma$ 在这个核上单射，故其像是非零 $E[M]$ 点。
由 (26)，这些纤维在目标原点至少有 $n_\nu p>p+1$ 阶零。
因此首行仅来自 $w=z/\gamma$：
$$
\boxed{
[z^{p+1}]\mathcal U_\gamma(\widehat A_{\nu,M})
=(\bar\gamma/\gamma)^{p+1}\overline{\alpha_\nu}
=\overline{\alpha_\nu}.
}
\tag{30}
$$
最后一步只在原惰性剩余域内使用
$\gamma^p=\bar\gamma$，故该比值范数一。

原 theta trace 不是 (29)。其准确模型是
$$
\boxed{
\widehat{\mathcal M}_{\gamma,M}(A_\nu)(z)
=\mathcal P_{2,M}(z)^{n_\nu}
 \sum_{\gamma w=z}
 \left(\frac{Q_{\bar\gamma}(w)}{Q_\gamma(w)}\right)^{m_\nu}
 R_\nu(\bar\gamma w).
}
\tag{31}
$$
这直接使用原 $[\gamma]_*[\bar\gamma]^*$ 的 sigma frame。
相对于裸输入 $\widehat A_{\nu,M}(\bar\gamma w)$，必须乘上
$$
\boxed{
\left(
\frac{\mathcal P_{2,M}(\gamma w)}
     {\mathcal P_{2,M}(\bar\gamma w)}
\right)^{n_\nu}
\left(\frac{Q_{\bar\gamma}(w)}{Q_\gamma(w)}\right)^{m_\nu}.
}
\tag{32}
$$
在非恒等纤维，分母带有 (26) 的 $n_\nu p$ 级零，
并同时有原 $Q_\gamma$ 的真实 torsion 因子。
这些项会恢复原 theta trace 的贡献，不是可删去的高阶误差。

作为明确的范围核对，R297 已付
$\mathcal M_\gamma S=-\gamma S$。由 (23)、(30)、(31)，
$$
\boxed{
[z^{p+1}]
\bigl(\widehat{\mathcal M}_{\gamma,M}(S)
      -\mathcal U_\gamma(\widehat S_M)\bigr)
=(-\gamma-1)\overline{\alpha_S}.
}
\tag{33}
$$
$N(\gamma+1)=21$，所以当前 $p>211$ 时该因子为单位。
因此这个被省略 frame 的差，恰能与原指定首行同阶；
(33) 不是该首行的非零证明，更不能把右边免费赋零。

## 9. 本篇付到的原问题接口

现在已经同时有：

1. 同一个先于 $p$ 固定的 torsion cover、绝对 Mumford 倍率和半特征；
2. 完整 $Z_M/G_M$、非零曲率及四个原首 $\alpha$ 的保持；
3. 新模型在所有非零 $E[M]$ 点的准确 Frobenius 初始零；
4. 真 theta 群延拓 (28)，以及原 CM13 必须保留的 (31)–(32)。

尚未支付的是：由这些完整原 frame 项推出四条指定
$\alpha_{p+1}$ 不能同时为零，或把它们的原 native Schur
响应压成已知非零的有限组合。不同 CM 标签、裸 trace 的 (30)、
曲率非零及原点之外的 (26)，都不能替代这一判定。
原四完整中央及所有低卷积继续保留。

## 10. 完整普通迹为零，所读首行仍需原非中心插入

以下均在一个固定 theta 数据的好剩余域中进行；必要时先作完美
常数域扩张，使全部 $E[M]$ 点和固定根单位有定义。令
$$
K=k(E_b),\qquad K_0=K^p,\qquad
H=E[M],\qquad L=K^H,\qquad F=K_0^H=L^p.
\tag{34}
$$
这里 $[K:K_0]=p$、$[K_0:F]=M^2$、$[K:F]=pM^2$。
后一有限群扩张是可分的；$L/F$ 则是纯不可分的 $p$ 次扩张。
所有四个原来源使用同一个 (34)，不随来源另选一个载体。

先核一个不能省掉的迹区别。对 $m\mid M$、$p\nmid m$，令
$$
\mathscr D_m=D+mG_M.
$$
由 (14) 代 $m\mapsto-m$，
$$
\mathscr D_m^p=mH_M^p.
\tag{35}
$$
$H_M\in L$，而其原点首项为
$(3b/5)M^4z^5$；故 $DH_M\ne0$，从而 $H_M\notin F$。
因此
$$
\mathcal E_m=F[T]/(T^p-mH_M^p)
\tag{36}
$$
是纯不可分的 $p$ 次域。令 $T$ 作用为 $\mathscr D_m$，
便把 $K$ 变成一个 $\mathcal E_m$ 向量空间，维数为 $M^2$。

若一个 $F$-线性算子 $A$ 与 $\mathscr D_m$ 交换，
则它是 $\mathcal E_m$-线性的，因而
$$
\boxed{
\operatorname{Tr}_{K/F}(A)
=\operatorname{Tr}_{\mathcal E_m/F}
 \bigl(\operatorname{Tr}_{K/\mathcal E_m}(A)\bigr)=0.
}
\tag{37}
$$
最后的零来自纯不可分域迹，而不是来源或首系数为零。
特别，(16) 的真实 $T_\tau$、(27) 的完整 $\widetilde A$、
以及它们和 $\mathscr D_m$ 的任意有限多项式组合，都满足 (37)。

所以仅取完整 connection/Heisenberg 交换代数中的普通矩阵迹，
确实不会读出原 $\alpha_\nu$。下节给出的非中心插入是指定的，
不能用 (37) 中的一个多项式算子替换它。

## 11. 原 Cartier 行的准确矩阵迹

因 $DZ_M=1$，$1,Z_M,\ldots,Z_M^{p-1}$ 是 $K/K_0$ 的基。
对任意 $f\in K$，准确写成
$$
f=\sum_{i=0}^{p-1}a_i Z_M^i,\qquad a_i\in K_0,
\qquad \pi_M(f)=a_{p-1}.
\tag{38}
$$
Wilson 等式给
$$
D^{p-1}f=-a_{p-1}.
$$
而 $D^{p-1}$ 的矩阵只有从 $Z_M^{p-1}$ 到 $1$ 的一个
非零元 $-1$。若 $\mathsf M_f$ 表示乘 $f$，逐列读迹得到
$$
\boxed{
\pi_M(f)
=-D^{p-1}f
=-\operatorname{Tr}_{K/K_0}(\mathsf M_fD^{p-1}).
}
\tag{39}
$$
这保留了全部 $p$ 个 Frobenius 系数 $a_i$；没有把它们替换为
特征零初始值。由于 $dZ_M=\omega_E$，Cartier 的 $p$-基公式正是
$$
\mathcal C(f\omega_E)=\pi_M(f)^{1/p}\omega_E.
\tag{40}
$$

现取四个**已经固定的原输入**
$$
f_\nu=Z_M^{-2}\widehat A_{\nu,M},\qquad
c_\nu=\pi_M(f_\nu)\in K_0.
\tag{41}
$$
(23)、(24)、(39) 给
$$
c_\nu(O)=\overline{\alpha_\nu}.
\tag{42}
$$
在每个非零 $\tau\in H$，(26) 则给
$$
\operatorname{ord}_\tau f_\nu\ge n_\nu p-2.
$$
在该点以微分参数展开，Cartier 只读指数
$p-1+pr$。故
$$
\operatorname{ord}_\tau
 \bigl(\mathcal C(f_\nu\omega_E)/\omega_E\bigr)
 \ge n_\nu-1,
\qquad
\operatorname{ord}_\tau c_\nu\ge p(n_\nu-1)>0.
\tag{43}
$$
因此 (42) 是这一固定 torsion 纤维上唯一可能非零的值。
这一步使用真实 (26)，并未删除 CM13 的 frame。

把 (39) 沿可分塔 $K_0/F$ 取迹，令 $q$ 为共同 quotient
$E_b^{(p)}/H^{(p)}$ 的原点，得到四条共同读取：
$$
\boxed{
\overline{\alpha_\nu}
=
-\left.
\operatorname{Tr}_{K/F}
   (\mathsf M_{f_\nu}D^{p-1})
\right|_q.
}
\tag{44}
$$
确切地，右边等于
$\sum_{\tau\in H}c_\nu(\tau)$，而 (42)、(43) 只留下原点项。
所有被评价的迹函数在 $q$ 正则；这由它们在整个有限纤维上的
局部正则性和有限 étale 下降得到。

(44) 与 (37) 没有冲突：$D^{p-1}$ 是原 Cartier 插入，
不是 $\mathscr D_m^{p-1}$。在完整 theta 群下，
$$
T_\tau D T_\tau^{-1}
=D-mD\log g_\tau.
\tag{45}
$$
所以把 $D^{p-1}$ 搬过 $T_\tau$ 时，必须保留 (45) 的全部
非交换幂和 (8)–(10) 的原绝对倍率。将其换为一个 commuting
connection 多项式会改变指定行。

## 12. 固定 $M^2$ 载体和准确的原点特征多项式

(44) 还可严格降到固定维数，但未知首行不会因此消失。

令 $\iota:K_0\hookrightarrow K$。由 (38)、(39)，
$$
D^{p-1}=-\iota\pi_M.
$$
$\pi_M$ 满射，所以 $D^{p-1}$ 的 $F$-rank 恰为 $M^2$。
有限维迹的循环恒等式给
$$
-\operatorname{Tr}_{K/F}
   (\mathsf M_{f_\nu}D^{p-1})
=
\operatorname{Tr}_{K_0/F}(B_\nu),
\quad
B_\nu=\pi_M\mathsf M_{f_\nu}\iota.
\tag{46}
$$
因 $\pi_M$ 为 $K_0$-线性，
$$
\boxed{B_\nu(a)=c_\nu a,\qquad a\in K_0.}
\tag{47}
$$
故四条原行确实由同一个 $M^2$ 维有限 torsion 载体上的四个
乘法矩阵读取。矩阵条目由 (20)、(38)、(41) 完全指定；
$M^2$ 固定，不意味着这些条目或原 $p^3$ 极帽与 $p$ 无关。

在 $q$ 附近取该有限 étale 代数的整模型。其几何原点纤维为
$\prod_{\tau\in H}k$，(47) 在这个分解中逐项乘
$c_\nu(\tau)$。由 (42)、(43)，
$$
\boxed{
B_\nu(q)=\overline{\alpha_\nu}\,e_O,\qquad
\operatorname{char}_{B_\nu(q)}(T)
=T^{M^2-1}(T-\overline{\alpha_\nu}),
}
\tag{48}
$$
其中 $e_O$ 是原点因子的同一个秩一幂等元。
四个来源并未拥有四个不同的非零 torsion 特征方向。

对任意固定标量 $u_\nu$，还准确有
$$
\boxed{
\det\!\left(I+\sum_\nu u_\nu B_\nu(q)\right)
=1+\sum_\nu u_\nu\overline{\alpha_\nu}.
}
\tag{49}
$$
当 $M>1$ 时，$\det B_\nu(q)=0$ 与 $\alpha_\nu$ 是否为零无关；
删去公共零特征方向后的单个特征值正是原未知
$\overline{\alpha_\nu}$。因此一般表示非零、曲率非零或一个
未经 (48) 专门化的有理范数非零，都不能替代原四行不能同时零。

(44)–(49) 的实际作用是给出**共同而非猜测的载体与指定插入**。
它们没有把原四 $f_\nu$ 改成自由测试，也没有把
$\chi_2$ 响应放入原 $M$ 的像。若要推进原 native Schur，
下一步仍必须利用 (41) 中同一个
$\mathcal P_{2,M}$ 与四个完整 $R_\nu$ 的真实共同结构，
而不是从这个固定载体本身另取一个中央零条件。

## 依赖

- [R636](../results/R636-original-rational-cartier-return-for-two-critical-rows.md)：
  原 $Z,G,H_G$、完整有限窗口、曲率及有理模型算法。
- [R647](../results/R647-original-three-source-rational-model-and-five-cartier-conditions.md)：
  原 degree-two 模型、前三来源及首 Cartier 读取。
- [R821](../results/R821-original-four-central-axes-and-complete-four-block-carries.md)：
  四个完整 $R_\nu$、原 Gaussian 归一与全部共同坏集。
- [R297](../results/R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)：
  原 CM13 全纤维 trace、完整 sigma 比及 $S$ 的绝对本征值。
- [原四首行有理分部边界](2026-11-15-original-four-diagonals-rational-telescoping-boundary.md)：
  本篇没有沿用到特征 $p$ 的特征零证书障碍。

本文各恒等式由显示的微分、division 函数、有限 theta 群及
原窗口逐项证明；未执行新的目标素数扫描或私有数学计算，
不生成可重算数值输出。
