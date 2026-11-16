# R862 — 原十七挠点乘积、完整三次 Hom 矩阵与精确 cusp 阶

日期：2026-11-16。

**状态：下述十七挠点乘积、原完整有限角色、固定椭圆扭曲、Frobenius 余循环、三条规范准同态及其完整微分矩阵已证明。原 R839/R841 实际曲线在 cusp 的三个阶准确为 $(1,1,4)$；R851 的底参数极阶准确为6，三阶源商后为2。尚未计算出 R859 的一个非零原 shadow，也未把这些映射或其循环相认 R814 的 canonical 类。**

本篇保持 R826/R831 的三个固定角色、原 $q_0/q_2$、全部
Artin 系数和 R839 的实际 Hom 展开。新的代数常数不是任取一个
范数方程的解，而是原 $E_0[17]$ 的指定有限乘积。
首项归一在 $\operatorname{Hom}^0$ 中完成；将其清为真实整数同态
所需的分母始终保留。

## 1. 原角色与十七挠点的实际 Galois 表示

固定
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\qquad
E_0:\ Y^2=X^3+1,\quad \omega_0=\frac{dX}{2Y}.
\tag{1}
$$
CM 作用采用
$$
[\omega](X,Y)=(\omega X,Y),\qquad
[\omega]^*\omega_0=\omega\omega_0.
$$
沿 R806 的同一 reciprocity 和代数系数嵌入，令
$$
\eta=\eta_{10},\qquad
\eta_j=\eta^{k_j},\quad
(k_4,k_{10},k_{16})=(13,1,7),\qquad
\beta_j=\eta_j^{-2}\psi_0,\quad g_j=\theta(\beta_j).
\tag{2}
$$
这里 $\psi_0$ 是 (1) 的原 type-$(1,0)$ Hecke 角色。
R826 已付
$$
\mathfrak f_{\beta_j}=(17\delta),\quad N(g_j)=2601,\quad
\eta_j^3=\psi_{17}/\psi_0,\quad
\operatorname{Gal}(H_{34}/K)=C_{18}.
\tag{3}
$$
记 $A$ 为这三个 $g_j$ 的同一个三维新 Hecke 因子。
本文的 Hom 均取这个原因子；不把 $J_0(2601)$ 的其它因子加入来源。

令
$$
\mathcal M=K(E_0[17]),\qquad
\rho_{17}:G_K\longrightarrow(\mathcal O_K/17)^\times
                         =\mathbf F_{289}^{\times}.
\tag{4}
$$
选定非零 $P\in E_0[17]$ 后，约定
$\sigma P=[\rho_{17}(\sigma)]P$。
在素于 $6\cdot17$ 的理想上，CM Frobenius 提升给
$$
\rho_{17}(\operatorname{Art}(\mathfrak a))
=\psi_0(\mathfrak a)\bmod17 .
\tag{5}
$$
这同时固定本篇的 Artin 方向。

**满像。** 对任意 $u\in(\mathcal O_K/17)^\times$，用 CRT 取
$a\equiv1\pmod{2\delta}$、$a\equiv u\pmod{17}$。
原 $\psi_0$ 的主理想公式给 $\psi_0((a))=a$，故 (5) 的像含 $u$。
因此
$$
\boxed{\operatorname{Gal}(\mathcal M/K)=\mathbf F_{289}^{\times}
       \simeq C_{288}.}
\tag{6}
$$
因为17惰性，$E_0[17]$ 是 $\mathbf F_{289}$ 上的一维模；
任何非零 $P$ 都生成全部挠点，所以 $K(P)=\mathcal M$。

还须核 (4) 与原 $\eta_j$，不能仅比较其阶。
对素于 $34\delta$ 的 $a$，写
$\epsilon_2(a)=\operatorname{Teich}_{\mu_3}(a\bmod2)$，
$\epsilon_3(a)\in\{\pm1\}$ 为 $a\bmod\delta$ 的提升。
原完整主理想公式是
$$
\psi_0((a))=\epsilon_3(a)\epsilon_2(a)^{-1}a.
$$
R806(8) 则是
$$
\eta_j((a))=\epsilon_2(a)\,
       \operatorname{Teich}(a\bmod17)^{-16l_j},
\qquad l_j=j-9\in\{-5,1,7\}.
$$
$16l_j\equiv1\pmod3$ 且 $16l_j$ 为偶数，故逐项相乘得到
$$
\boxed{\eta_j=\operatorname{Teich}(\rho_{17})^{-16l_j}.}
\tag{7}
$$
Teich 提升使用 R806 的原 $\mu_{18}$ 嵌入。
等式先在所有好理想成立，遂为完整全局角色等式；
它保留2、3、17的全部分量，包括3处不分歧但非平凡的值。
没有以某个好素数标签代替这一核对。

## 2. 一个非零的十六项乘积固定原九次域

在 (6) 中令 $G_{32}$、$G_{96}$ 分别为唯一阶32、96子群。
固定前述 $P$，定义
$$
\boxed{
h=\prod_{u\in G_{32}/\{\pm1\}}X([u]P).
}
\tag{8}
$$
$x$ 坐标对 $u\mapsto-u$ 不变，故这个恰16项的乘积不依赖代表。
它也等于
$$
\operatorname{Norm}_{K(X(P))/\mathcal M^{G_{32}}}X(P).
$$
每一项均非零：$X=0$ 的两个点是阶3点，不可能是非零17挠点。

$G_{32}$ 逐项置换 (8)，所以固定 $h$。
另一方面，(1) 的实际 CM 坐标给
$$
h^\omega=\omega^{16}h=\omega h.
\tag{9}
$$
$\omega$ 的像是 $C_{288}/G_{32}=C_9$ 中唯一的阶3子群生成元。
若 $h$ 的稳定子严格大于 $G_{32}$，其在 $C_9$ 中的非平凡像
必含这个阶3子群，与 (9) 及 $h\ne0$ 矛盾。因此
$$
\boxed{K(h)=\mathcal M^{G_{32}}=:H_9,\qquad [H_9:K]=9.}
\tag{10}
$$

由 (7)，$G_{32}=\ker\eta^2$、$G_{96}=\ker\eta^6$。
R844 已付原 $H_{34}$ 的 ring-class 身份及其三次子域，故
$$
\boxed{
H_9=H_{34}^{\,\ker(\eta^2)/\ker\eta},\qquad
L:=\mathcal M^{G_{96}}=K(\sqrt[3]{17}).
}
\tag{11}
$$
这里 $H_9$ 是原九次子域，**不是**次数6的 $H_{17}$。

每个 $u\in G_{96}$ 唯一分解为 $u=v\epsilon$，
$v\in G_{32}$、$\epsilon\in\mu_3$，且 $\epsilon=u^{64}$。
所以
$$
h^u=u^{64}h=u^{-32}h
      =\eta^2(u)h.
\tag{12}
$$
三个 $l_j$ 都为 $1\bmod3$，在 $G_{96}$ 上
$u^{-32l_j}=u^{-32}$。于是
$$
\boxed{
h^\sigma=\eta_j^2(\sigma)h\quad(\sigma\in G_L,\ j=4,10,16),
\qquad a:=h^3\in L,\quad K(a)=L.
}
\tag{13}
$$
最后一式由 $[K(h):K]=9$、$[K(h):K(h^3)]\le3$ 得到。
所以同一个 $h$ 服务原三个分支，不用逐支另选扭曲。

### 2.1 绝对范数与乘积的尺度

令 $\Psi_{17}(X)$ 是 (1) 的标准奇 division polynomial。
其次数144、首项系数17；根为全部非零17挠点的144个
$\{\pm1\}$-$X$ 坐标。九个 (8) 的 Galois 共轭恰覆盖这些根一次。
故
$$
\operatorname{Norm}_{H_9/K}(h)=\frac{\Psi_{17}(0)}{17}.
$$
在 $P_0=(0,1)$ 上，division-polynomial 的递推给
$$
\Psi_{3k+1}(P_0)=(-1)^k2^{3k^2+2k},\qquad
\Psi_{3k+2}(P_0)=(-1)^k2^{3k^2+4k+1}.
$$
可由 $\Psi_1=1,\Psi_2=2,\Psi_4=-32,\Psi_5=-256$
及 Ward 式
$\Psi_{m+3}\Psi_{m-3}=64\Psi_m^2$ 分别在两个非零剩余类中归纳。
因此
$$
\boxed{
\operatorname{Norm}_{H_9/K}(h)
=\operatorname{Norm}_{L/K}(h^3)
=-\frac{2^{96}}{17}.
}
\tag{14}
$$
(14) 是 (8) 的实际尺度，不允许将 $h$ 任意乘一个未记录常数。
更换最初的 $P$ 只作同一有限 Galois 共轭，并同步改变以下基。

还可把 (8) 写成一个无额外根选择的16步有理式。模17时
$-\!3$ 的阶为16，故 $\delta^2=-3$ 的 $\delta$ 恰生成 $G_{32}$。
原 CM 三同源的完整坐标是
$
[\delta](X,Y)=
\left(-\frac{X^3+4}{3X^2},
      \frac{(X^3-8)Y}{\delta^3X^3}\right).
\tag{14a}
$
它的微分拉回为 $\delta\omega_0$，所以符号与 (1) 相同。
设 $R(X)=-(X^3+4)/(3X^2)$，则
$
\boxed{h=\prod_{i=0}^{15}R^{\circ i}(X(P)).}
\tag{14b}
$
$\delta^{16}=-1\bmod17$ 给 $R^{\circ16}(X(P))=X(P)$。
各分母非零，因为每个中间点仍为非零17挠点。
因此 (14b) 可以直接在 $K[X]/(\Psi_{17})$ 内精确实现；
由 (6) 这个次数144的除法坐标代数确为域。
本文没有预报其未运行的系数或把该实现作为证明门。

## 3. 原椭圆扭曲及完整 Frobenius 余循环

定义固定的 $L$-曲线
$$
\boxed{
C_h:\ y^2=x^3+h^6,\qquad
\omega_C=\frac{dx}{2y}.
}
\tag{15}
$$
因为 $h^6=a^2\in L^\times$，这是非奇异曲线。其到原 $E_0$ 的
真实同构为
$$
\phi_h:C_h\longrightarrow E_0,\qquad
(x,y)\longmapsto(x/h^2,y/h^3),\qquad
\phi_h^*\omega_0=h\omega_C.
\tag{16}
$$
若 $\sigma\in G_L$，由 (13) 及 CM 作用
$[\epsilon](X,Y)=(\epsilon^{-2}X,\epsilon^{-3}Y)$ 得
$$
\phi_h^\sigma=[\eta_j^2(\sigma)]\phi_h.
$$
所以 $\operatorname{Hom}(C_h,E_0)$ 的所选 CM 角色是
$\eta_j^2|_{G_L}$，而曲线本身的角色为其逆：
$$
\boxed{
\psi_{C_h}=\bigl(\eta_j^{-2}\psi_0\bigr)\circ N_{L/K}
          =\beta_j\circ N_{L/K}.
}
\tag{17}
$$
这里取的是全局实际 Galois 扭曲，故包括所有坏位；
不是由同 $j=0$ 或好素数 trace 猜出 (17)。
三个 $\beta_j$ 的限制相同，与 (13) 一致。
另外
$$
\operatorname{Norm}_{L/K}(h^6)=2^{192}/17^2.
$$

对素于 $34\delta$ 的理想 $\mathfrak a$，记
$\sigma_{\mathfrak a}=\operatorname{Art}_{H_9/K}(\mathfrak a)$。
置
$$
\boxed{
\Lambda(\mathfrak a)
=\psi_0(\mathfrak a)\frac{h}{h^{\sigma_{\mathfrak a}}}\in L^\times.
}
\tag{18}
$$
商确在 $L$ 中，因为 $G_{H_9/L}$ 对分子分母有相同的
$\mu_3$ 作用，且 $H_9/K$ 为交换扩张。
实际 isogeny 是
$$
\mu_{\mathfrak a}
=\phi_{h^{\sigma_{\mathfrak a}}}^{-1}
       \circ[\psi_0(\mathfrak a)]\circ\phi_h:
 C_h\longrightarrow{}^{\mathfrak a}C_h,
$$
并满足
$$
\mu_{\mathfrak a}^*({}^{\mathfrak a}\omega_C)
       =\Lambda(\mathfrak a)\omega_C,\qquad
\Lambda(\mathfrak a\mathfrak b)
 =\Lambda(\mathfrak a)\,{}^{\mathfrak a}\Lambda(\mathfrak b).
\tag{19}
$$
在好素理想上，这是由 (5) 运来的 Frobenius 提升，未添根单位。

若 $\mathfrak a$ 在 $L/K$ 的 Artin 像为1，由 (13) 得
$$
\Lambda(\mathfrak a)
=\psi_0(\mathfrak a)\eta_j^{-2}(\mathfrak a)
=\beta_j(\mathfrak a).
\tag{20}
$$
因此 (18) 是 González–Lario 的原 $[A]$ 类中、
相对于固定微分 $\omega_C$ 的那一枚余循环。
只有范数条件而没有 (18)–(20)，不足以指定这个原类。

原 $\beta_j$ 的导子不含2，故还必须补回理想 $(2)$。
它在 $L/K$ 完全分裂：模2的 $T^3-17=T^3-1$ 在
$\mathbf F_4$ 上分成三个不同线性因子。R826 的原 primitive
二处因子给 $\beta_j((2))=-2$，于是唯一相容扩充为
$$
\boxed{\Lambda((2))=-2.}
\tag{21}
$$
(18) 与 (21) 在全部 $I(17\delta)$ 上定义完整余循环。
后面的 q-级数包含这份二处项，没有使用二耗尽形式代替原 $g_j$。

## 4. 一个固定7理想给全部有限代数数据

取
$$
\alpha=-1+2\omega,\qquad
\mathfrak l=(\alpha),\quad N\mathfrak l=7,\qquad
b=\beta_{10}(\mathfrak l).
\tag{22}
$$
$\alpha\equiv1\pmod{2\delta}$，故 $\psi_0(\mathfrak l)=\alpha$。
在 $\mathcal O_K/17$ 中逐次平方给
$\alpha^{48}=-\omega$、$\alpha^{96}=\omega^2$。
由 (7)，
$\eta^6(\mathfrak l)=\omega$。因此
$$
\boxed{
b^3=\alpha^3\omega^2=-1-19\omega=:c,\qquad
E_{\rm coeff}=K(b)=K(\zeta_9).
}
\tag{23}
$$
这里 $\alpha^3=19+18\omega$；$T^3-c$ 在 $K$ 不可约，
因为 $b/\alpha$ 是一个本原九次单位根。
$E_{\rm coeff}/K$ 只在3处分歧，而 $L/K$ 在17处分歧，故
$$
E_{\rm coeff}\cap L=K.
\tag{24}
$$

令 $\widetilde\tau=\sigma_{\mathfrak l}$ 在 $H_9$ 上作用，
$\tau=\widetilde\tau|_L$，并定义
$$
\ell=\Lambda(\mathfrak l)
=\alpha h/h^{\widetilde\tau},\qquad
u_0=1,\quad u_1=\tau^2\ell,\quad
u_2=\tau\ell\,\tau^2\ell=c/\ell .
\tag{25}
$$
由 $\widetilde\tau^3h=\eta^2(\mathfrak l^3)h=\omega h$，
$$
\boxed{\operatorname{Norm}_{L/K}(\ell)=c=-1-19\omega.}
\tag{26}
$$
(25) 已给这枚范数解的确定十七挠点表达；
不是从所有范数解中任取一个再指定有限角色。

为使原标签完全可读，按以下次序编号：
$$
F_0=g_{10},\quad F_1=g_{16},\quad F_2=g_4,\qquad
b_j=\omega^j b\quad(0\le j\le2).
\tag{27}
$$
因为 $\eta^6(\mathfrak l)=\omega$，原三份
$\beta_{10},\beta_{16},\beta_4$ 在 $\mathfrak l$ 的值恰为这些 $b_j$。
定义
$$
\boxed{
G_j=1+\frac{u_1}{b_j}+\frac{u_2}{b_j^2}
   =1+\frac{\tau^2\ell}{b}\omega^{-j}
       +\frac b\ell\omega^{-2j}.
}
\tag{28}
$$
它们就是以 $1,\mathfrak l,\mathfrak l^2$ 为代表的三个完整
González–Lario Gauss 系数。

## 5. 原 projector 恰为 $3\,\mathrm{Id}$，及固定微分的准同态归一

González–Lario 的 $K$-线性 projector 是
$$
\operatorname{pr}(v)=
\sum_{i=0}^2
 \left(\sum_{j=0}^2b_j^{-i}\right)
 \tau^{-i}\Lambda(\mathfrak l^i)\,\tau^{-i}v
 \qquad(v\in L).
$$
由于 $\sum_jb_j^{-1}=\sum_jb_j^{-2}=0$，准确有
$$
\boxed{\operatorname{pr}=3\,\mathrm{Id}_L,\qquad
       \sum_{j=0}^2G_j=3.}
\tag{29}
$$
这与该文 Proposition4.4 的
$[E_{\rm coeff}:K]=[L:K]=3$ 情形一致。

该文 Theorem1.3、Lemma4.1 及 Proposition4.5 给
$$
H_0(Q):=\frac13\sum_{j=0}^2G_jF_j(Q)
       =Q+\cdots
\tag{30}
$$
为原 $C_h$ 的椭圆方向。
这里还需要把“方向”提升到固定 $\omega_C$ 的严格归一。

具体地，Proposition4.5 给某个真实 $\pi:A\to C_h$
及 $\omega'\in\Omega^1(C_h/L)$，满足
$\pi^*\omega'=H_0\,dQ/Q$，且
$\Lambda_{\omega'}=\Lambda_{\omega_C}$。
若 $\omega'=e\omega_C$，两余循环的比是
${}^{\mathfrak a}e/e$。Artin 像遍历 $\operatorname{Gal}(L/K)$，
故 $e\in K^\times$。因此
$$
\boxed{
\Theta_0=[e]\circ\pi\in\operatorname{Hom}_L^0(A,C_h),
\qquad
\Theta_0^*\omega_C=H_0(Q)\frac{dQ}{Q}.
}
\tag{31}
$$
$[e]$ 是 CM 准同态；没有把任意 $L$ 或 $\mathbf C_p$ 标量
当作椭圆 endomorphism。微分拉回在特征零 Hom 上单射，
故 (31) 的规范准同态唯一。

这一论证不声称 $\Theta_0$ 已为整数同态或 Manin 因子为1。
固定一个正整数 $d$，使以下三条准同态均被 $d$ 清为真实同态；
$d$ 是整个固定来源的一部分，随后并入 R859 的整数 $D$。
本文没有给 $d$ 的最小值，也不把其素因子在任意研究素数处省掉。

## 6. 完整三条 Hom 微分矩阵

González–Lario Theorem1.1 的实际 CM Hecke 嵌入记为
$\iota:E_{\rm coeff}\to\operatorname{End}_K^0(A)$。
令
$$
\Theta_i=\Theta_0\circ\iota(b)^i\quad(0\le i\le2),\qquad
\mathcal A_i=\phi_h\circ\Theta_i .
\tag{32}
$$
则在固定原 $F_j$、固定 $\omega_0$ 下，
$$
\boxed{
\mathcal A_i^*\omega_0
=\sum_{j=0}^2 M_{ij}F_j(Q)\frac{dQ}{Q},
\qquad M_{ij}=\frac h3\,b_j^iG_j.
}
\tag{33}
$$
所有 $M_{ij}$ 都已由 (8)、(22)、(25)、(28) 的有限代数表达指定。
没有额外未定的复或 $p$-adic period。

这是真可逆矩阵。若 $G_j=0$，则
$b_j^2+u_1b_j+u_2=0$，
与 (24) 所给 $[L(b_j):L]=3$ 矛盾。因此每个 $G_j\ne0$。
又
$$
\prod_{a<b}(b_b-b_a)=-3\delta c,
$$
所以
$$
\boxed{
\det M=-\frac{\delta c h^3}{9}\,G_0G_1G_2\ne0.
}
\tag{34}
$$
可逆性是特征零代数恒等式，不是某个辅助素数的秩样本；
它本身不宣称任何原整格上的行列式为单位。

三条 $\Theta_i$ 的首 Fourier 系数分别为
$$
u_i=\frac13\sum_{j=0}^2b_j^iG_j\qquad(0\le i\le2).
\tag{35}
$$
由 González–Lario Lemma4.1 的首系数非零性，
$u_0,u_1,u_2$ 是 $L$ 的 $K$-基。
也可直接如此核：若 $\sum r_i u_i=0$，$r_i\in K$，
则非零准同态
$\Theta_0\circ\iota(\sum r_i b^i)$
将有零首系数；$\sum r_i b^i\ne0$ 在域 $E_{\rm coeff}$ 中可逆，
与该引理矛盾。

于是
$$
\boxed{
\operatorname{Hom}_L^0(A,C_h)\xrightarrow{\ [Q]\ }
L
}
\tag{36}
$$
是 $K$-线性同构；在所选基上，
右复合 $\iota(b)$ 的矩阵为
$$
\begin{pmatrix}
0&0&c\\
1&0&0\\
0&1&0
\end{pmatrix}.
\tag{37}
$$
(36) 是向量空间同构，不能把它误认为
$E_{\rm coeff}$ 与 $L$ 的域同构；两域由 (24) 不同。

### 6.1 原全部 Hom 和系数域分解

R844(13) 的原 Hom 角色为
$\eta_4^2,\eta_{10}^2,\eta_{16}^2$。
它们在 $G_L$ 上相同，且在 $G_{H_9}$ 上全平凡。
因此全部实际有理 Hom 到 $E_0$ 均在 $H_9$ 定义。
对其中任一 $a$，
$\phi_h^{-1}a$ 的 Galois 下降数据相消，确在 $L$ 定义。
所以 (32) 给出
$$
\boxed{
\operatorname{Hom}_{H_{34}}^0(A,E_0)
=\bigoplus_{i=0}^2K\,\mathcal A_i,\qquad
[Q](a^*\omega_0)\in hL.
}
\tag{38}
$$
首系数在这个实际 $K$-Hom 空间上单射。
这不声称扩到任意代数系数后，三个数到一条代数数轴的线性行仍单射。

若要抽取原 $F_j$ 线，其 Hecke 幂等元准确为
$$
e_j=
\frac{\iota(b)^2+b_j\iota(b)+b_j^2}{3b_j^2},
\qquad
(\mathcal A_0e_j)^*\omega_0
=\frac{hG_j}{3}F_j(Q)\frac{dQ}{Q}.
\tag{39}
$$
因此原 $g_j$ 微分到这组真实准同态的比较也完全由 (33) 的逆矩阵给出。
若原 $\Gamma_j$ 带有既定的另一代数尺度，仍将该尺度乘入同一系数；
不因 (39) 重新指定原循环。
Artin 作用仍施于实际 Hom／循环因子，不将 (33) 的系数同步作
一次未指定的半线性共轭。

## 7. 全 Fourier 系数及二处项

原导子是 $\mathfrak m=(17\delta)$。
González–Lario Proposition4.7 对这个 $K\not\subset E_f$ 的实三次
新形式 packet 给
$$
\boxed{
H_0(Q)=
\sum_{\substack{\mathfrak a\subset\mathcal O_K\\(\mathfrak a,\mathfrak m)=1}}
{}^{\mathfrak a^{-1}}\Lambda(\mathfrak a)\,
Q^{N\mathfrak a}.
}
\tag{40}
$$
其中 $(2)$ 的幂按 (21) 取值，绝未从和式删除。
在素于 $34\delta$ 的部分，(18) 使这条式子更具体：
$$
h\,{}^{\mathfrak a^{-1}}\Lambda(\mathfrak a)
=\psi_0(\mathfrak a)\,h^{\sigma_{\mathfrak a}^{-1}}.
\tag{41}
$$
对 $\mathfrak a=(2)^v\mathfrak b$，$(\mathfrak b,34\delta)=1$，
其 (40) 项是 $(-2)^v$ 乘 $\mathfrak b$ 项，指数乘 $4^v$。
所以 (40) 是同一原 newform packet 的完整 q-级数。

式 (8)、(18)、(28)、(33)、(40) 提供有限的精确代数输入：
可以在 $E_0$ 的17除法域中用有理群律计算 (8)，再在同一域内
求 (25) 和矩阵 (33)。所需的扩域和全部根选择均已指定。
它不是在研究素数 $p$ 上扫描或选择新的角色。

## 8. 原实际模函数与整数清分母

令 $n>0$ 清除 (32) 的共同整数 Hom 分母。
经原 $J_0(2601)\to A$ 和以 $\infty$ 为基点的 Abel 映射，得到
真实态射
$$
a_i=n\mathcal A_i:X_0(2601)_{H_9}\longrightarrow E_0,
\qquad a_i(\infty)=O.
\tag{42}
$$
这里 $n$ 可以取前述 $d$；另写此符号只强调它是实际函数域映射的
共同分母，而非一个新自由参数。

写
$a_i^*\omega_0=\sum_{m\ge1}c_{i,m}Q^m\,dQ/Q$。
原点的形式参数由 $\omega_0=dz$ 固定，则
$$
z_i(Q)=\sum_{m\ge1}\frac{c_{i,m}}m Q^m,\qquad
X_i=X(z_i(Q)),\quad Y_i=Y(z_i(Q)).
\tag{43}
$$
(42) 已证明这些是同一实际模函数的 germ；
不是仅凭形式微分就宣称其代数。
实际全局 $X_i,Y_i$ 仍由 (42) 的同态确定。
在有限特征归约时先使用这些实际态射的整模型；
不能对 (43) 中含 $1/m$ 的特征零积分逐项无条件约模。

把 R839 的每个实际 Hom 用 (38) 展开、再清共同整数分母，
即得到同一原 $\Gamma_i$ 的有限真实映射表达。
所有展开系数、$n$、原 $D$、Artin 幂等元及原
$X_0/X_1$、old-space 次数同时保留。
若使用准同态的符号表达，则只在对应的 $h^1$ 上线性展开；
不可把带代数系数的虚拟 Hom 直接当成一条不带系数的曲线映射。

## 9. 原 cusp 三阶准确为 $(1,1,4)$

现回到 R839/R841 的每个非零实际项
$$
\Phi=(F,\ a q_0,\ b q_2),\qquad
q_0(z)=z,\quad q_2(z)=4z,\quad
F(\infty)=a(\infty)=b(\infty)=O.
\tag{44}
$$
$F$ 经过原 $E_{17}$ 新因子，故其非零微分为原首系数1新形式
的一个非零代数倍。于是 $F$ 的形式参数在 $\infty$ 阶为1。
对非零实际 $a,b$，(36)、(38) 给首系数非零。
所以存在实际 $c_F,c_a,c_b\ne0$，使
$$
z_F=c_FQ+\cdots,\quad
z_{a q_0}=c_aQ+\cdots,\quad
z_{b q_2}=c_bQ^4+\cdots.
\tag{45}
$$
第三式没有额外4：微分拉回的4与形式积分准确相消。

因此
$$
\boxed{
\bigl(\operatorname{ord}_\infty z_F,
\operatorname{ord}_\infty z_{a q_0},
\operatorname{ord}_\infty z_{b q_2}\bigr)=(1,1,4).
}
\tag{46}
$$
R841 的实际 $R$-等变平均由 CM 整 endomorphism 和原源自同构组成；
若平均结果非零，它仍是 (38) 中的实际 Hom，故同样满足 (46)。
polarization 的每个非零实际 $a+b$ 也如此。
不能把此结论移到外部代数系数已相消后的整个虚拟循环上，
再据此宣称总循环非零。

R851(32)–(33) 在原 $E_0^3$ 上给
$$
\tau=\frac1{2z_1z_2z_3}
 \bigl(1+O(z_1^3,z_2^3,z_3^3)\bigr).
$$
代入 (45)，准确得到
$$
\boxed{
\tau\circ\Phi
 =\frac1{2c_Fc_ac_b}Q^{-6}(1+O(Q^3)),\qquad
\operatorname{ord}_{\infty}(\tau\circ\Phi)=-6.
}
\tag{47}
$$
三次乘积是唯一最低项，故没有同阶抵消；原 $R$-等变性使形式参数的相对下一阶至少为 $Q^3$。
在 R850/R851 的真实 $R$ 源商
$X_0(10404)\to X_0(3468)$ 上，局部参数为 $\overline Q=Q^3$，
所以
$$
\boxed{\operatorname{ord}_{\overline\infty}\tau=-2.}
\tag{48}
$$
这是原每条有效曲线的精确局部阶；
不声称 $\tau$ 没有其它极点，也不将其误作全局 degree2 映射。

## 10. 回到 R859 shadow 与仍待计算的原交点

R859 附录B的实际读取保持为
$$
S_r(\Pi\Phi_*[X])
=\operatorname{Alb}(b\circ q_2)_*
       (a\circ q_0-\varphi_r\circ F)^*[O],
$$
或其同一 $X/R$ 商上的完整交积表达。
本篇给这个公式补上 (15)、(33)、(40)、(42) 的固定代数 Hom 输入。
$h$ 的定义域是原 $H_9$，$F$ 的 sextic 域为原 $H_{17}$；
二者的合成正是原 $H_{34}$。没有新增随 $r$ 或 $p$ 变化的系数域。

在任何实际有限域读取之前，须把 (42) 的整数分母并入原 $D$，
使用同一有限 Galois/Artin 组合，并保留所有原闭点迹及交点重数。
(34) 的特征零非零不准许先认其模某个素数为单位。
本篇尚未列出这些 Jacobian 映射的完整函数域坐标，
也未计算一个非零 Frobenius 交点。
原 shadow 的非零、原端点 AJ 的非零和
R814 canonical 类的比较仍是不同的实质目标。

全文是符号 CM、有限群及原已发表 Hom 定理的推导；
没有新增数值运行、目标素数扫描或可重算数据。

## 11. 原文与原来源

- J. González–J.-C. Lario,
  *Modular elliptic directions with complex multiplication
  (with an application to Gross's elliptic curves)*,
  Comment. Math. Helv. **86** (2011), 317–351,
  DOI 10.4171/CMH/225。
  Theorem1.1–1.3、Propositions3.1–3.3、
  Lemma4.1、Propositions4.4、4.5、4.7。
  发表正文：<https://ems.press/content/serial-article-files/43255?nt=1>。
  作者预印本：<https://arxiv.org/pdf/0810.4224>。
  本文使用前四节的一般 CM 结果，不使用后面
  $p\equiv3\bmod4$、level $p^2$ 的 Gross 曲线特例。
- [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)：
  原 $\eta_j$、2/3/17 角色和固定 reciprocity。
- [R826](R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md)：
  原 $\beta_j$ 三次 packet、全导子和二处抵消。
- [R844](R844-original-genus-four-cm-order-seventeen-and-two-neighbors.md)：
  $H_{34}$、$H_{17}$、$K(\sqrt[3]{17})$ 与实际 Hom 的完整 Galois 角色。
- [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)、
  [R839](R839-top-cm-translation-invariance-and-original-ceresa-expression.md)、
  [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)：
  原两个退化映射、实际 Hom、全部对应系数及 $R$-等变平均。
- [R850](R850-original-smooth-cubic-quotient-and-exact-top-cycle-transport.md)、
  [R851](R851-original-schoen-map-and-horizontal-cycle-transport.md)：
  原三阶源商、Schoen 参数及其实际局部坐标。
- [R859](R859-original-supersingular-shadow-and-integral-aj-detection.md)，
  正文与附录A、B：同一原循环的整 shadow、Chow 逆、
  完整商交积及同源曲线上的单分支读数。