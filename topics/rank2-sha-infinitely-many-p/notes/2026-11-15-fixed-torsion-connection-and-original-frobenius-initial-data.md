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

## 13. 固定覆盖审核：原有理模型的真极阶

补充日期：2026-11-16。本节审查的是保持 (41) **同一个物理输入**
的固定覆盖实现。它没有先将输入乘上另一个函数；
特别不允许把 $\mathcal C(hf\omega_E)$ 擅自写成
$h\mathcal C(f\omega_E)$。固定输出 frame 的范围在 §16 单列。

记
$$
e_p=p^2-p-1,\qquad
q_p^{\mathrm{pol}}=p^3-p^2+p+1,\qquad
\mathcal D_M=[M]^*\mathcal D_2.
\tag{50}
$$
这里 $q_p^{\mathrm{pol}}$ 是极阶，**不是** (17) 的 Fermat 商。
对每个 $\tau\in\mathcal D_M$，准确有
$$
\boxed{
-\operatorname{ord}_\tau Z_M=p,\qquad
-\operatorname{ord}_\tau G_M=e_p,\qquad
-\operatorname{ord}_\tau\mathcal P_{2,M}=q_p^{\mathrm{pol}}.
}
\tag{51}
$$

先在原 $M=1$ 模型核前两式。R636 的
$Z=\mathscr R_p(x)/y^p$ 只可能在三个非零二挠点有极，
在 $O$ 正则，而且对 $\mu_3$ 有同一非平凡角型。
三个二挠点构成一个 $\mu_3$ 轨道。由 $DZ=1$，
一个存在的极阶必须是 $p$ 的倍数；已知上界为 $p$，
所以该阶恰为 $p$。如果三个点全无极，$Z$ 为全局常数，
与 $DZ=1$ 矛盾。因此三个点均为恰 $p$ 阶极。

原 $G$ 的每项
$Z^{i+1}D^i(-x)$ 在 $[-1]$ 下均为奇函数，
且原极阶上界为 $p(p-1)$。二挠点固定于 $[-1]$，
所以这个偶数极阶不能出现。另一方面，
$DG=-x+c_pZ^{p-1}$ 在该点恰有 $p(p-1)$ 阶极，
且其首系数非零。因此 $G$ 的极阶必须恰为
$p(p-1)-1=e_p$。

$[M]$ 在当前素数处 étale；$B_M$ 在
$\mathcal D_M$ 正则，因为其极只在 $E[M]$。
故 (11) 将前两条真极阶原样搬到所有
$\tau\in\mathcal D_M$。

在 $\tau$ 选定局部微分参数 $u$，使 $du=\omega_E$。
其存在性可直接由 $\omega_E=dZ_M$ 及局部 Cartier 判据证明：
在任一原参数下，指数为 $pi+p-1$ 的微分系数为零，
其余项逐项积分，所得首项为单位。
由于 $DZ_M=1$，以及 (12) 对 $G_M$ 的微分式，
存在非零 $a_\tau,b_\tau\in k$，使
$$
\begin{aligned}
Z_M&=a_\tau u^{-p}\bigl(1+O(u^p)\bigr),\\
G_M&=b_\tau u^{-e_p}
                  \bigl(1+O(u^{p-1})\bigr),\\
b_\tau&=c_p a_\tau^{\,p-1}.
\end{aligned}
\tag{52}
$$
确切地，$Z_M-u$ 的所有 Laurent 指数均为 $p$ 的倍数。
于是 $Z_M^{p-1}$ 在其首项后的第 $1,\ldots,p-2$ 个
相对系数全零；对 $G_M$ 积分时，这些位置的指数
$-e_p+r\equiv1+r\pmod p$ 也全为单位。
首次可能自由的水平项在相对阶 $p-1$，没有被删去。

现在用 (20)。在
$\nabla_{2,M}^{\,j}(Z_M^2)$ 中，全部使用乘法项
$-2G_M$ 的项具有最高极；每把一次该乘法换成一次 $D$，
极阶至少降低 $e_p-1$。外面的 $Z_M^j$ 也已经保留。
不同 $j$ 中，$j=p-1$ 比 $j=p-2$ 的最高极再高
$e_p+p=p^2-1$。由 Wilson 等式及
$2^{p-1}=1$，所以
$$
\begin{aligned}
\mathcal P_{2,M}
&=-G_M^{p-1}Z_M^{p+1}
       \bigl(1+O(u^{e_p-1})\bigr)\\
&=\rho_\tau u^{-q_p^{\mathrm{pol}}}
       \bigl(1+O(u^{p-1})\bigr),\\
\rho_\tau&=-b_\tau^{p-1}a_\tau^{p+1}\ne0.
\end{aligned}
\tag{53}
$$
这同时证明 (51) 的第三式。它把 (25) 的上界收紧为
**这个指定模型的真极阶**，未改变模型本身。

## 14. 四个真实 Cartier 输出的最高极

置
$$
\mathscr C_\nu
=\frac{\mathcal C(f_\nu\omega_E)}{\omega_E},
\qquad
d_{\nu,p}=n_\nu(p^2-p+1)-1.
\tag{54}
$$
由 (52)、(53)，在 $\tau\in\mathcal D_M$，
$$
f_\nu=
\rho_\tau^{n_\nu}a_\tau^{-2}
u^{-Q_{\nu,p}}\,
R_\nu(\tau+u)\bigl(1+O(u^{p-1})\bigr),
\quad
Q_{\nu,p}=n_\nu q_p^{\mathrm{pol}}-2p.
\tag{55}
$$
$R_\nu$ 在这里正则。因为 $Q_{\nu,p}\equiv n_\nu\bmod p$
且 $n_\nu<p$，Cartier 首次可能读到的 Taylor 系数
恰是第 $n_\nu-1$ 阶。它低于 (55) 的第一可能误差阶，
所以其完整主部是
$$
\boxed{
\mathscr C_\nu
=
\left(
\rho_\tau^{n_\nu}a_\tau^{-2}
\frac{D^{\,n_\nu-1}R_\nu(\tau)}{(n_\nu-1)!}
\right)^{1/p}
u^{-d_{\nu,p}}
+\text{极阶较低的项}.
}
\tag{56}
$$
若括号内为零，(56) 只给极阶上界；若非零，该极阶就准确为
$d_{\nu,p}$。此处根号是完美剩余域中的唯一 Frobenius 逆，
不是一个新的 sigma 定标。

对四个原 $R_\nu$，这一非零条件在大量实际点上必定成立。
由 R821 的原六阶首项，
$R_\nu$ 只在 $O$ 有极，极阶恰为 $2n_\nu-6$。
因此
$$
D^{\,n_\nu-1}R_\nu
\text{ 只在 }O\text{ 有极，极阶恰为 }3n_\nu-7.
\tag{57}
$$
首系数中的所有导数因子均小于 $p>211$；
最大极阶为 $197$，故不能在约化后降为零函数。
于是它在 $\mathcal D_M$ 上至多有 $3n_\nu-7$ 个零点，
按重数计。$\mathcal D_M$ 则有 $3M^2$ 个不同点，
而所固定的 (2) 保证 $3M^2>3n_\nu-7$。

综上，每条原输出都至少在
$3M^2-3n_\nu+7$ 个点有准确极阶 $d_{\nu,p}$：
$$
\boxed{
\deg(\mathscr C_\nu)_\infty
\ \ge\
(3M^2-3n_\nu+7)\,
\bigl(n_\nu(p^2-p+1)-1\bigr).
}
\tag{58}
$$
这里只计算 $\mathcal D_M$ 的贡献。
$Z_M$ 的其它零点以及所有其它可能极点仍全部保留，
没有因为 (58) 是下界而删掉它们。

四个 $n_\nu=17,36,68,33$ 互异。
因此任何非零的 $k$-常数线性组合
$\sum_\nu a_\nu\mathscr C_\nu$ 都仍有真极：
取 $a_\nu\ne0$ 中最大的 $n_\nu$，在它的 (56)
非零点上，所有其它项的极阶严格较低，不能相消。
这也适用于随 $p$ 变化的非零剩余域标量；
未要求这些标量是固定有理数。

## 15. 保原微分的固定覆盖不能给全纯 Hasse–Witt 块

令 $\pi:X\to E_b$ 是先于 $p$ 固定的有限可分代数覆盖。
删去它的固定坏约化处及分歧指数的素因子；
因而下述所有局部扩张均为 tame。
这包含固定阶循环/Kummer 覆盖和本篇的固定 Mumford theta 覆盖。

Cartier 与可分拉回交换，且杀掉全微分：
$$
\mathcal C_X(\pi^*\eta)=\pi^*\mathcal C_E(\eta),
\qquad
\mathcal C_X(dv)=0.
\tag{59}
$$
这可由局部 Cartier 的唯一分解
$\eta=dv+h^p u^{p-1}du$ 直接验证，
故不需要把原 sigma 先换为一个裸代数根。

若 $\mathcal C_E(\eta)$ 在 $\tau$ 有极阶 $d>1$，
在其上的一个分歧指数为 $e$ 的点处，
拉回微分的极阶准确为
$$
e(d-1)+1.
\tag{60}
$$
其中 $e$ 先于 $p$ 固定，首系数中的 $e$ 是单位。
将 $\eta=f_\nu\omega_E$ 代入 (56)、(60)，得到随
$p^2$ 无界增长的真极点。

另一方面，固定光滑完备 $X$ 的 Hasse–Witt 块是
$H^1(X,\mathcal O_X)$ 的 Frobenius 块，等价地可用其对偶
$H^0(X,\Omega_X^1)$ 上的 Cartier 块读取。
Cartier 将全纯微分送到全纯微分。
固定循环覆盖的字符空间只按 $p$ 的剩余类置换；
这不改变全纯性和固定有限维数。

因而，对本篇保留的物理输入，不存在
$$
\pi^*(f_\nu\omega_E)=\eta_{\nu,p}+dv_{\nu,p},
\qquad
\eta_{\nu,p}\in H^0(X,\Omega_X^1),
\tag{61}
$$
因为 (59) 的左边有 (56)、(60) 的真极，右边的 Cartier
却全纯。对四来源的非零常数线性组合也一样。
允许 $v_{\nu,p}$ 是任意随 $p$ 变化的有理函数，
仍不能改变这个结论。

更一般地，把右边全纯微分换成先于 $p$ 固定极帽的
有限微分空间也不能消掉这个增长。其 Cartier 极阶一致有界，
而 (56) 的极阶按 $p^2$ 增长。
因此**仅用固定覆盖、固定字符块、固定极帽换基和 exact 消元**，
不能把原四条完整 Cartier 来源实现成一个先于 $p$ 固定的
Hasse–Witt 块。

## 16. 固定 frame 的精确范围与仍可研究的门

上述结论的固定 frame 仅指：

- 保持同一微分的固定坐标或线丛平凡化；
- 对已经算出的输出使用固定的有理 frame，
  或在一个固定有界极帽的 frame 空间中换基；
- 固定覆盖中的字符分解和固定基变换。

前两类只按固定的分歧指数和有界阶改变 (56)；
四个不同 $n_\nu$ 的极阶间距按 $p^2$ 增长，
不会被这些有界改变抹去。

**任意先把输入乘上一个固定函数 $h$ 不在这个范围内。**
一般
$$
\mathcal C(hf_\nu\omega_E)
\ne h\,\mathcal C(f_\nu\omega_E).
\tag{62}
$$
例如形式上选 $h=1/R_\nu$ 就会改掉 (56)
所读的第 $n_\nu-1$ 阶系数，但这已经换成不同物理输入。
本篇没有证明任意这种输入 gauge 都保留最高极，
更没有因此删除它产生的来源/中央补偿。

若尝试用一个随 $p$ 变化的输出函数消极，
仅在基曲线上就必须吸收 (58) 的零除子成本；
若以它的 $p$ 次幂先乘输入，Cartier 后的因子仍是该真实函数，
不能视为一个固定单位。这正是从原 $p^3$ 模型降到
Cartier 后仍留下的实际 $p^2$ 成本。

原 CM13 的 (31)–(32) 也没有被改写成固定输入 gauge。
其中含 $\mathcal P_{2,M}$ 比值的部分有真正随 $p$ 增长的零极，
不能与固定的 $Q_\gamma$ 或 Mumford 常数混同。
删去它们所得裸 trace 仍只是 (29)，不是原来源。

最后，(56)–(61) 是完整来源实现的阻碍，不是否定一切可能的
**单个数值**恒等式。仍可能需要另一个已证明的构造，
把指定 $\overline{\alpha_\nu}=\mathscr C_\nu(O)^p$
与某个固定曲线的矩阵元联系起来；本篇没有建立或排除所有
这种额外算术构造。全球 Cartier 输出非零且线性独立，
也不意味着它们在 $O$ 的四个指定值不能同时为零。

因此固定覆盖这一路的直接实现已被准确审清。
下一步仍回到原 (41) 四个共同多项式与第五伙伴，
而不是从 (58) 的全球真极另造一个原中央非零条件。

## 17. 即使允许可变 $p$ 次幂系数，固定有限代数来源池仍不够

这一节进一步审核一种比 §15 更宽的可能实现：
不先改物理输入，但试图把它写为固定代数来源的有限和，
其系数允许是任意随 $p$ 变化的 $p$ 次幂。
结论只涉及这种**完整函数恒等式**，仍不排除另行证明的
单个原点数值恒等式。

令 $F$ 为固定数域，$X/F$ 为先于 $p$ 固定的光滑完备曲线，
$\pi:X\to E_b$ 有限可分。固定 $Q\in X$ 位于 $O$ 之上，
必要时一次性扩张 $F$，使 $Q$、所选局部参数及下列全部固定
Taylor 系数有定义；之后始终使用这个同一数域 $F$。令
$$
V\subset F(X)
\tag{63}
$$
为任意固定有限维 $F$-空间。在固定好整模型约化后，记
$V_{\mathfrak p}$ 为它的约化，$K_{X,\mathfrak p}=k_{\mathfrak p}(X)$。
所有本节的排除集合均由这些固定数据和下面的一个固定
Taylor minor 决定，不扫描目标素数。

对任一原来源 $\nu$，在充分大且固定坏集外的原惰性素数，
有
$$
\boxed{
\pi^*\widehat A_{\nu,M}
\notin K_{X,\mathfrak p}^{\,p}V_{\mathfrak p},
\qquad
\pi^*f_\nu
\notin K_{X,\mathfrak p}^{\,p}V_{\mathfrak p}.
}
\tag{64}
$$
右边表示所有有限和 $\sum_i h_{i,\mathfrak p}^{\,p}v_i$；
$h_{i,\mathfrak p}$ 可以是任意有理函数，不要求有固定极帽，
也不要求从特征零提升。对 $\mathcal P_{2,M}$ 本身，
同一结论也成立。

### 17.1 原有限窗口给出固定的特征零局部 germ

在 $Q$ 取固定代数局部参数 $u$，并把
$$
z(u)=\int_0^u\pi^*\omega_E
$$
解释为特征零的固定形式积分。其系数在已经固定的 $F$ 中；每个有限截断只有固定分母。若 $\pi$ 在 $Q$ 的分歧
指数为 $e$，则 $\operatorname{ord}_u z=e$。

由 (22)–(24) 及原六阶零，对每个先固定的截断长度 $J$，
当 $p$ 充分大并避开该截断的固定分母后，
$\pi^*\widehat A_{\nu,M}$、$\pi^*f_\nu$ 的前 $J$ 项分别就是
下列固定特征零 germ 的约化：
$$
\begin{aligned}
\mathcal A_\nu(u)
 &=\sigma(z(u))^{2n_\nu}R_\nu(x(u),y(u)),\\
\mathcal F_\nu(u)
 &=\frac{\sigma(z(u))^{2n_\nu}
            R_\nu(x(u),y(u))}{z(u)^2}.
\end{aligned}
\tag{65}
$$
其首阶分别为 $6e$ 和 $4e$。
对 $\mathcal P_{2,M}$，对应 germ 是 $\sigma(z(u))^2$，
首阶为 $2e$。

这里只先固定 $J$ 再约化。没有约化整个形式对数，也没有删除
(17)–(19) 的 Gaussian 修正：它的第一可能贡献随 $p$ 移到
任一固定截断之外。$Z_M$ 的同一原初始资料确保分母确实给
(65) 中的 $z(u)^2$，而不是一个任意选择的局部坐标平方。

### 17.2 这三个 germ 均不是固定代数函数

先假设 $\mathcal A_\nu\in\overline F(X)$。
由于 $R_\nu$ 代数且非零，取对数导数得到
$$
\zeta(z)
=\frac{1}{2n_\nu}
 D\log\bigl(\mathcal A_\nu/R_\nu\bigr)
\in\overline F(X),
\qquad
D\zeta=-x.
\tag{66}
$$
把 (66) 沿有限扩张 $\overline F(X)/\overline F(E_b)$ 取归一化迹，
便得到 $B\in\overline F(E_b)$ 且 $DB=-x$。
不变向量场 $D$ 在椭圆曲线上处处非零。
因此 $B$ 若有极，其导数在同一点的极阶恰增加一：
$DB=-x$ 迫使 $B$ 只有 $O$ 这一个极，且恰为一阶。
但 $H^0(E_b,\mathcal O(O))$ 只有常数，矛盾。
同一论证适用于 $\sigma(z(u))^2$。

对 $\mathcal F_\nu$ 也不能直接忽略 $z^{-2}$。
若它代数，令
$$
B=D\log(\mathcal F_\nu/R_\nu)
  =2n_\nu\zeta-2/z.
$$
则 $B$ 代数且
$$
DB=-2n_\nu x+2/z^2.
\tag{67}
$$
所以 $z^{-2}$ 代数，从而在一个进一步的有限扩张中 $z$ 代数。
沿该有限扩张取归一化迹，将 $Dz=1$ 下降为
$DB_0=1$，其中 $B_0\in\overline F(E_b)$。
$DB_0$ 无极迫 $B_0$ 无极，因而常数，再次矛盾。
故 (65) 的两个 germ，以及 $\sigma^2$，均不在任何固定
有限代数函数扩张中。

### 17.3 可变 $p$ 次幂系数不能掩盖这个有限 jet 障碍

给 $V$ 取一个在 $Q$ 处按 Laurent 展开行消元所得的固定基
$v_1,\ldots,v_d$，其首阶
$$
r_1<\cdots<r_d
\tag{68}
$$
互异。清去固定分母和首系数的固定坏处后，约化仍保这些阶。
取 $p>r_d-r_1$，则这些阶模 $p$ 互异。

若某个 (64) 的等式成立，把右边写为
$\sum_i h_i^p v_i$。第 $i$ 项的阶为
$p\,\operatorname{ord}_Q(h_i)+r_i$。
任何两个非零项的这些阶都不同，因为 (68) 的阶差绝对值
小于 $p$。若某个 $h_i$ 有极，取 $p$ 再大于
$r_d$ 减去原输入的固定首阶，则右边有一个无法相消、
且低于该输入首阶的最低项，矛盾。
因此所有 $h_i$ 都在 $Q$ 正则。

于是对任一固定 $J$，只要 $p+r_1\ge J$，便有
$$
\sum_i h_i^p v_i
\equiv \sum_i h_i(Q)^p v_i \pmod {u^J}.
\tag{69}
$$
也就是说，可变的全局 $p$ 次幂系数，在这个原有限窗口内
只留下常数系数；它们不能增加固定 $V$ 的 jet 像。

这里 $j^J$ 明确定义为从 Laurent 指数
$\min(r_1,0)$ 到 $J-1$ 的有限截断，故固定基的所有可能负阶
均被读取。由 §17.2，任一目标 germ 不在 $V$ 中。由于 $V$ 有限维，
存在一个固定 $J_0$，使其增广 Taylor 矩阵满足
$$
\operatorname{rank}
  [\,j^{J_0}v_1\ \cdots\ j^{J_0}v_d\
     j^{J_0}\mathcal A_\nu\,]=d+1
\tag{70}
$$
（对 $\mathcal F_\nu$ 或 $\sigma^2$ 同理）。
可取第一个满足此条件的 $J_0$，以及字典序第一个非零
$(d+1)$ 阶 minor $\Delta$；它们由固定数据明确确定。
清分母后，删去 $\operatorname{Norm}_{F/\mathbf Q}(\Delta)$
的有限素因子。这个排除不依赖 $p$ 的未知读数。

现在 (65)、(69) 会把 (70) 的最后一列放入前 $d$ 列的
约化像，与 $\Delta$ 为单位矛盾。这证明 (64)。
论证同时允许约化后的任意常数域扩张，因为满秩不会在域扩张后消失。

## 18. 分别成立的范围，以及 $p$ 次幂加 exact 的真实联合式

(64) 排除的是**没有 exact 补项的函数恒等式**。
它补上了一个独立范围：即使允许任意 $p$ 次幂 rescaling，
原 $\mathcal P_{2,M}$ 或两种完整原输入都不能进入固定有限
代数函数池。在固定循环覆盖上选择有限多个字符 frame，
或按 $p$ 模固定整数选择有限多个固定 frame，只产生有限多个
(63)，因而仍只有一个固定有限例外集。

但不能把 (64) 与 §15 混合成一个未经证明的更强排除。
若同时允许任意 $p$ 次幂系数和一个任意 exact 补项，
事实上每个原输入都有下面的完整显式恒等式。

置
$$
\eta=d\log x=s\omega_E,\qquad s=2y/x,\qquad
h_\nu=\mathscr C_\nu/s=x\mathscr C_\nu/(2y).
\tag{71}
$$
对数微分满足 $\mathcal C(\eta)=\eta$。所以
$$
\mathcal C(f_\nu\omega_E-h_\nu^p\eta)=0.
$$
在同一个 (38) 的 $p$-基中写
$$
f_\nu-h_\nu^p s
=\sum_{i=0}^{p-2}a_{\nu,i}Z_M^i,\qquad a_{\nu,i}\in K^p,
$$
其第 $p-1$ 项准确为零，而不是被省略。
逐项积分给
$$
\boxed{
f_\nu\omega_E=h_\nu^p\,d\log x+dv_\nu,\qquad
v_\nu=\sum_{i=0}^{p-2}
       \frac{a_{\nu,i}}{i+1}Z_M^{i+1}\in K.
}
\tag{72}
$$
也可直接核第 $p-1$ 项：
$\pi_M(s)=s^p$，而
$h_\nu^p s^p=\mathscr C_\nu^p=\pi_M(f_\nu)$。
因此 (72) 是保原物理输入、全局成立的真等式。

(72) 没有消掉原未知。$h_\nu$ 按定义含完整
$\mathscr C_\nu$，并承接 §14 的真实 $p^2$ 极帽；
$d\log x$ 也不是一个全纯 Hasse–Witt 基向量。
在原点，$s=-2/z+O(z^5)$，故准确有
$$
\boxed{
\overline{\alpha_\nu}
=\bigl(-2[z]h_\nu\bigr)^p.
}
\tag{73}
$$
原未知只是移入同一个可变有理系数中，并未得到已知的固定矩阵元。

因此，已经付清的范围逐条是：

1. **固定完整微分 / 固定有界输出池，加任意 exact 补项**：
   §13–16 的真极证明不可能实现；这里没有任意可变 $p$ 次幂权。
2. **固定有限代数函数池，加任意可变 $p$ 次幂系数，但没有 exact 补项**：
   §17 的固定 Laurent jet minor 证明 (64)。
3. **同时允许可变 $p$ 次幂系数和 exact 补项**：
   不能作前两条的联合排除；(71)–(72) 已给一个明确实现，
   而 (73) 精确显示它仍保留原未知和可变极帽成本。

这些都不是将任意输入权 $h$ 擅自搬过 Cartier。
若某个新构造只匹配 $\mathscr C_\nu(O)^p$ 而不匹配全输入，
其原点读取、CM13 的 (32) 及全部 native 补偿仍须另行支付。
四个原 $\alpha_\nu$ 是否同时为零，仍不能由上述范围审核或
(72) 的存在性作出结论。

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
