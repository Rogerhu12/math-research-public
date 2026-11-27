# R1034 — 两倍高度窗的原中央读者、两枚 β 权与完整第二 Cartier 回填

日期：2026-11-27 UTC。**已证明。**
本篇把同一原 $J$ 的特征零平坦比较推进到 $H$ 接近 $2p$，
其精度严格超过 $p$。两个显示 β 权在同一个窗口分别饱和为
$\beta^{p^2}$ 和 $\beta^{2p^2}$；它们的特定组合消去六个三挠极的
simple 通道。物理高系数通过一个完整、确定的原 $\sigma/P$ 矩阵读取，
不把有限特征 $p$ 模型的高项直接冒作原 Gaussian 系数。

原 R614/R616/R619 的两坏带及其中央端点原样保留。
第二 Cartier 的真正全纯 scalar 在 $r=p$ 回到读者，
并未继续用第一 primitive 或平坦截面把它删掉。

## 1. 同一全来源与新的合法窗口

保持 R1032 的原 $E:y^2=x^3+1$、$\delta,\pi,\alpha=\delta\pi$、
完整 degree390 来源 $f$、原 $\sigma$ 和微分参数 $z$。
令
$$
p=6s-1>13^4,\qquad d=p+1,\qquad
H\in\{2p-11,2p-5\},\qquad n=Hd,\quad k=n/6.
\tag{1}
$$
两种 $H$ 均为 $5\bmod6$，且 $Hs<2L$，
其中 $L=s(p-1)=(p^2-1)/6$ 是原 R614 的高度二端点。

沿原
$$
B_{a,k}(T)=\sum_{j=0}^k(-1)^j
 \binom{a+j-1}{j}(T-1)^j,\quad
\beta=X/(X+4),\quad v_\pi=R_\pi/(X+1)^2,
$$
取两种三处指数
$$
a_1=n/2+1,\qquad a_2=n+1,\qquad
V_j=\beta^{a_j}B_{a_j,k}(\beta),\quad j=1,2.
\tag{2}
$$
十三处一直取同一
$V_\pi=v_\pi^{a_2}B_{a_2,k}(v_\pi)$。
两个完整39权是
$$
V_{\alpha,j}(P)=V_j(P)V_\pi(\delta P).
\tag{3}
$$
这两枚权都在特征零定义；不是事后改一个约化权。

原点均为 $1+O(z^{n+6})$。
在非零 $\delta$ 核，$\beta$ 三阶零给
$3a_1>n+1$、$3a_2>n+1$；
其它36个 $\alpha$ 核由原 $V_\pi$ 的 $n+1$ 阶零支付。
令 $R_f=f/\sigma^{390}$，$R_\alpha=\sigma(\alpha z)/(\alpha\sigma^{39})$，
并沿 R1032 的未平均 trace 定义
$$
A_j=\alpha^{-10}\operatorname{Tr}_{[\alpha]}
 \left(V_{\alpha,j}R_f/R_\alpha^{10}\right),\qquad h_j=\sigma^{10}A_j .
$$
故 R1032 的整个 trace 和所有相位逐支给
$$
h_j(\alpha z)-f(z)=O(z^{n+1}).
\tag{4}
$$
两个 target 的二挠极至多 $4e_2$，
三挠两点的极分别至多
$$
e_1=a_1+k=2n/3+1,\qquad
e_2=a_2+k=7n/6+1.
\tag{5}
$$
原整模型、显示有理整基及统一 Hurwitz 范数
按 R1032 (11)–(13) 逐项适用；增长极没有增加垂直分母。

## 2. 真正超过 p 的完整中央精度

令 $c=[z^d]\log(\sigma/z)$，仍有 $v_p(c)=-1$。
对原或 target 的完整质量零 Gaussian，
记其原 Newton 第 $h$ 项为
$$
T_h=(-1)^{h-1}(h-1)!(Nc)^{-h}[z^{dh}]G ,
$$
其中 $N$ 是该 frame 的真实 theta degree。
统一 Hurwitz 输入给每个 $h\ge1$
$$
v_p(T_h)\ge
h-v_p((sh)!)+v_p((h-1)!)
\ge \frac{h(5p-7)}{6(p-1)}.
\tag{6}
$$
(6) 对全部 $h$ 成立，未把 $h\ge p$ 的阶乘认作单位。
右边严格递增并趋于无穷，所以从 $h=H+1$ 起的整个无限尾都在
$$
p^{K_H}\mathcal O,\qquad
\boxed{K_H=\left\lceil
 \frac{(H+1)(5p-7)}{6(p-1)}
\right\rceil>p}
\tag{7}
$$
中。两种窗口可以统一取较小的 $K_{2p-11}$。

(4)在特征零消去原差函数的前 $H$ 个完整 Newton 系数。
保 R1032 的同一个
$q_\alpha=\alpha^{p+1}/39$、$\gamma_\alpha$，
由 (6)得到真实身份
$$
\boxed{
j_f-j_{10,h_j}-m_0(f)\log_pq_\alpha
\in p^{K_H}\mathcal O,\qquad j=1,2.
}
\tag{8}
$$
旧上限 $5s-2$ 是在 $h=p-1$ 处开始估整个尾所得的统一界；
本篇没有在这个旧截断上声称更高精度。
这里是由新的特征零前缀 (4) 使尾真正从 $H+1$ 才开始。

## 3. 全多项式饱和及一枚准确的双极权

一个方便的完整代数事实是：
若 $k<p^2$ 且 $a\le mp^2\le a+k$，
则在 $\mathbf F_p[T]$ 中
$$
\boxed{T^aB_{a,k}(T)=T^{mp^2}.}
\tag{9}
$$
证明在 $T=1+Y$ 的截断环中，
$T^{mp^2}=1+O(Y^{p^2})$，故
$T^{-a}\equiv T^{mp^2-a}\pmod{Y^{k+1}}$；
后者的次数不超过 $k$，就是完整的 Taylor 截断 $B_{a,k}$。
这证明的是整个多项式，不只是若干点值或首项。

(1)–(2)准确满足
$$
a_1\le p^2\le a_1+k,\qquad
a_2\le2p^2\le a_2+k,\qquad k<p^2.
$$
因此
$$
\boxed{
\bar V_1=\beta^{p^2},\qquad
\bar V_2=\beta^{2p^2},\qquad
\bar V_\pi=v_\pi^{2p^2}.
}
\tag{10}
$$
整个十三权始终是同一个固定平方，
不在两个三处模型之间改换它。

现在取真正的特征零组合
$$
V_\gamma=3V_2-2V_1,\qquad
h_\gamma=3h_2-2h_1.
$$
它仍在原点为一、平坦到 $n$，并消全部其它核点；
所以也满足 (8)。
其完整约化是
$$
\boxed{
\bar V_\gamma=\gamma^{p^2},\qquad
\gamma=3\beta^2-2\beta=\frac{X(X-8)}{(X+4)^2}.
}
\tag{11}
$$
若 $T=(a,b)$，$a^3=-4$、$b=\pm\delta$，
以原微分参数 $z$ 展开，则
$$
\beta(T+z)=\frac{c_T}{z}+\frac13+O(z),
\qquad c_T=-\frac{2}{3a^2b}.
\tag{12}
$$
常数 $1/3$ 由
$DX(T)=6a^2b$、$D^2X(T)=-144a$
及 $1+2D^2X/(DX)^2=1/3$ 直接得到。
所以
$$
\boxed{\gamma(T+z)=3c_T^2z^{-2}+O(1).}
\tag{13}
$$
六点的 simple 项都准确消失，未使用 canonical 零。

## 4. 同一完整三字中的 β 与 γ 返回

沿 R1032 的原 $\delta$ target，
$h=1-y,\kappa^3=h,r_S=x/\kappa^2$。
整个三字为
$$
\beta=\frac13+\frac{x}{3h}\kappa+\frac1{3x}\kappa^2,
$$
$$
\boxed{
\gamma=\frac13+\frac{h}{3x^2}\kappa
 +\frac{x^2}{3h^2}\kappa^2
 =\frac{1+r_S^2+r_S^{-2}}3.
}
\tag{14}
$$
特别末一项包含 $h^2$，不能删掉一个 $h$。

原正三挠支是同一个 mode2。
两个第1字的比为
$$
\frac{\gamma_1}{\beta_1}
=\frac{y-1}{y+1}=r_S^{-3}.
$$
保全部 N130、Miller 与 $C_S,\delta$ 尺度，
R1032 的同一逐字回乘遂给
$$
\boxed{
\begin{array}{c|c|c}
 &\beta^{p^2}\text{ 模型}&\gamma^{p^2}\text{ 模型}\\
\hline
D_\delta g&R_g&R_g\\
T_{u_3}^{390}D_\delta G&
r_S^{p^2}R_{T_S^{130}G}&
r_S^{-2p^2}R_{T_S^{130}G}
\end{array}}
\tag{15}
$$
两行都在原全十二个十三字之和上使用。
它们还须共同乘原 $v_\pi^{2p^2}$ 并完成十三 trace。
负三挠支使用 (14) 的完整第二字，不能从正支删掉相位后猜测。

两种新返回的比准确为
$U^{-p^2}$，其中 $U=(y+1)/(y-1)$。
第二 Cartier 后留下真正的 $U^{-1}$，
而不是任意 $\mathbf Q(t)$-线性中央操作。
$D\log U=-6/x$ 是固定的原三挠连接；
其全部主部和 $P/G$ 交换子仍须在同一测试里保留。

## 5. 两坏带按实际原系数回填

这一节不重证 R614/R616/R619 的原结论，
而支付它们在 (5) 的新亚纯整基上的适用性。

R1032 (12) 的整基原样适用。为了同时核所有整数负幂及增长分子，
在好模型的实际局部参数 $u=x^{-1/2}$ 中写
$$
A=u^{-10}\sum_{j\ge0}a_j u^{6j},\qquad a_j\in\mathcal O .
$$
这来自整代数来源在 $O$ 的至多十阶极；
原纯 $\mu_6$ 型保证只出现这些指标。质量零准确等价于 $a_0=0$。
于是整个 Gaussian 为
$$
G_{10,h_A}
=\sum_{j\ge1}a_j w^jU_\sigma^{10}W_0^{\,5-3j}.
$$
每个给定指标只使用有限多个 $a_j$；
它们可以依赖 $p$，但始终来自同一个真实 trace。
整数负幂的二项式系数仍整。
在总指标小于 $2L$ 时，$W_0$、$U_\sigma$ 的坏系数都从 $L$ 起，
故每个乘积至多同时含一个坏因子。
这证明同一分段界对全部完整 rational 基及其整单位逆成立，
而不只对一个固定低次数分子成立。

首坏带的 Leibniz 系数也准确为
$10-2(5-3j)=6j$，并保留 $w^j$ 的真实位移。
第二坏带则只有 $U_\sigma^{10}$ 的二次分母贡献。
因此 R616/R619 的全部端点可逐项在这个整展开中使用。
若
$$
g_h=[w^{hs}]G_{10,h_j},
$$
则真实三个区间准确为
$$
\boxed{
\begin{array}{ll}
g_h\in\mathcal O,&1\le h\le p-1,\\
pg_p\in\mathcal O,&h=p,\\
p^2g_h\in\mathcal O,&p+1\le h\le H.
\end{array}}
\tag{16}
$$
这里使用的是 $hs-1$，未把质量零的首 $w$ 丢掉。
它与 R614 的全部端点一致。

R616 的首坏带在整单位逆上继续满足同一个 Leibniz 规则，
所以对这些质量零 target 仍有
$$
\boxed{pg_p\equiv g_1\pmod p.}
\tag{17}
$$
R619 的唯一二阶极部同样给
$$
\boxed{
p^2g_{p+h}\equiv(10pc)\,g_h\pmod p,
\qquad1\le h\le H-p.
}
\tag{18}
$$
在本篇 $E_1$ 上 $b^L=1$；物理模型改变时保原 R616/R619 的该因子。
整来源系数可以依赖 $p$，因为以上证明只用其整性和实际有限展开，
不要求它们是独立选择的常数。
每个实际系数仍来自 (5) 的同一个 trace。

所以不能把 $h=p$ 的行叫作新的独立单位。
在真实中央失败下，必要的 $g_1\bmod p=0$
也进入 (17)；(18)同样返回原低中央数据。
下面的读者保留这些费用及其下一位，不删除端点。

## 6. 一个确定的整 native lift 与完整物理矩阵

为了把高块真正接回原 $J$，现在固定有理 lift，
不任取一个形式高位。
令
$$
\widetilde Z=\frac{R_p(x)}{y^p},\qquad
R_p(x)=\frac12\sum_{j=0}^{(p-1)/2}
 \binom{(p-1)/2}{j}\frac{x^{3j+1}}{3j+1},
$$
$$
\widetilde G=-\sum_{i=0}^{p-2}
 \frac{(-1)^i\widetilde Z^{i+1}D^ix}{(i+1)!},
$$
$$
\boxed{
\widetilde P=-\widetilde Z^p
 (D-10\widetilde G)^{p-1}\widetilde Z^9.
}
\tag{19}
$$
它们的约化分别是原 $Z,G,P_{10}$。
全部 $3j+1$、$(i+1)!$ 在所用范围是 $p$ 单位。

在原好模型的实际局部参数 $u=x^{-1/2}$ 中，
这些有理函数的 Laurent 系数整。
$\widetilde Z$ 的首系数为
$\lambda_Z=(1-3p)^{-1}$，因此是一个整局部参数。
写 $\widetilde G=\lambda_G/z+O(z^5)$，则
$$
\lambda_G=-\sum_{r=1}^{p-1}\lambda_Z^r\equiv1\pmod p.
$$
$\widetilde P$ 的首系数准确为
$$
-\lambda_Z^{p+9}
 \prod_{i=0}^{p-2}(9-10\lambda_G-i)\equiv1\pmod p.
\tag{20}
$$
所以它准确从 $z^{10}$ 起，首系数为单位。
没有在 (19) 中引入一个新的未付除 $p$。

对上面完整 trace 的真实整 $A_j$（以下略下标），定义全部 native 系数
$$
\boxed{
\tau_n(A)=[T^n](\widetilde P A)(P(T)),
\qquad T=\widetilde Z(P).
}
\tag{21}
$$
$O$ 处 $\widetilde P$ 消掉 $A$ 的至多十阶极，
且两个原整单位逆均已付，所以每个 $\tau_n(A)\in\mathcal O$。
它们的约化就是
$t_n^{10}(\bar A)=[Z^n](P_{10}\bar A)$；
这种比较对所有 $n$ 成立，不只对 $n<p^2$。
这是好模型的局部整性，不是物理 $z$ 系数的错误整性外推。

物理高系数则由整个、确定的下三角矩阵给出：
$$
\boxed{
M_{h,n}=[z^{dh}]
 \frac{(\sigma^\circ)^{10}}{\widetilde P}\,
 \widetilde Z^n,\qquad
g_h=\sum_{0\le n\le dh}M_{h,n}\tau_n(A).
}
\tag{22}
$$
所有 $M_{h,n}$ 都来自 (19) 及原同一个 $\sigma^\circ$。
原角色使不相容的项为零；其余全部保留。
不能把 (22) 认作单位矩阵，或只约化其中一个高块。

为明确支付 (22) 的整单位逆，写
$\widetilde Z=uZ_0(u^6)$、$\widetilde P=u^{10}P_0(u^6)$，
其中 $Z_0,P_0\in\mathcal O[[u^6]]^\times$。
对于可能贡献 (22) 的 $n\equiv0\pmod6$，完整展开
$$
Z_0^n/P_0=\sum_{j\ge0}b_{n,j}u^{6j},\qquad b_{n,j}\in\mathcal O
$$
准确给
$$
\frac{(\sigma^\circ)^{10}}{\widetilde P}\widetilde Z^n
=\sum_{j\ge0}b_{n,j}z^{n+6j}
 U_\sigma^{10}W_0^{\,5-n/2-3j}.
$$
其它 $n$ 由原角色使 $M_{h,n}=0$。
所有显示指数均为整数；因此 §5 的同一个坏因子计数逐项适用。
在本篇 $dh<2(p^2-1)$ 的全部范围，
$p^2M_{h,n}$ 全整；相对指标小于 $L$ 时它本身整。
第一、第二坏带按原实际系数分别保留。
因此 (22) 是有完整分母账本的物理读取，
不是凭有限模型挑选另一份高位来源。

令
$$
\Lambda_{H,n}
=\sum_{\substack{1\le h\le H\\dh\ge n}}
 (-1)^{h-1}(h-1)!(10c)^{-h}M_{h,n}.
$$
由 (6)–(8)，得到同一原 $J$ 的完整有限读者
$$
\boxed{
j_{10,h_j}\equiv
 \sum_{n=0}^{dH}\Lambda_{H,n}\tau_n(A_j)
 \pmod{p^{K_H}}.
}
\tag{23}
$$
(16)–(18)、全部 $(h-1)!$ 中的 $p$、
两个 Gaussian、原 $\alpha$ 尺度和每个低 native 项的高精度
都在 (22)–(23) 中。
后继取某一精度页时，必须先清其真实分母；
不能把 $\tau_n\bmod p$ 一次代替整个 (23)。

## 7. 跨过 r=p 的真实第二 Cartier 行

在特征 $p$，继续用原
$$
\eta_b=Z^{-b-1}P_{10}A\,\omega_E,\quad
\rho_b=\operatorname{Res}_O\eta_b,\quad
\eta_b^0=\eta_b+\rho_b r_0\omega_E.
$$
令
$$
\nu_1=C\eta_b^0,\quad
\nu_2=C^2\eta_b^0=f_{2,b}\omega_E,\quad
c_b^\sharp=f_{2,b}(O).
$$
仍取同一个 $\varphi_*=\varphi-dJ_{p-6}$，
不去除它在 $Z^{p-1}$ 的系数。原 $C\varphi_*=\omega_E$ 准确给
$$
\varphi_*/\omega_E
=\sum_{n\ge p-1}a_n^*Z^n,\qquad a_{p-1}^*=1.
\tag{24}
$$
设
$$
[K_b]=D^{-1}(\nu_1-f_{2,b}^{\,p}\varphi_*)\in F/F^p.
$$
因为 $f_{2,b}$ 在 $O$ 正则，
$$
f_{2,b}^{\,p}\varphi_*
=(c_b^\sharp)^p\varphi_*+O(Z^{2p-1})\omega_E.
$$
因此整个 $1\le r<2p$ 范围都准确有
$$
\boxed{
t_{rp+b}^{10}(A)=
\left(
-\rho_b^{1/p}[Z^{r-1}]r_0
+\bar r[Z^r]K_b
+(c_b^\sharp)^p a_{r-1}^*
\right)^p,\qquad0\le b<p.
}
\tag{25}
$$
$\bar r$ 是 $r$ 在剩余域中的真实值。
在 $r=p$，它为零；$F^p$ 代表的 $Z^p$ 歧义正好被该系数消去。
原 $r_0$ 角色给 $[Z^{p-1}]r_0=0$，所以
$$
\boxed{t_{p^2+b}^{10}(A)=(c_b^\sharp)^{p^2}.}
\tag{26}
$$
只有 $b\equiv5\pmod6$ 的 scalar 可非零。
这是原第二 Cartier 数据的真实回填，
不从第一 primitive 猜一个 $r=p$ 系数。

本篇所有 $n\le dH$ 都满足
$r=\lfloor n/p\rfloor\le2p-4<2p$，
所以 (25)连同直接保留的 $n<p$ 原低行，已覆盖 (23) 的全部 native 模 $p$ 行。
物理读者仍须保 (22) 的全卷积；
(26)本身不是新的 canonical 零条件。

### 7.1 仅在 r=p 页的完整 CM 收紧

这里的角色条件不能扩成“所有中央 native 行都有 $b\equiv5$”：
一般 $rp+b\equiv0\pmod6$ 只给 $b\equiv r\pmod6$。
以下专门消费 (26) 的 $r=p$ 页，故确有 $b\equiv5\pmod6$。

令 $\tau$ 为原 $\mu_6$ 自同构，$\tau^*\omega_E=\zeta_6\omega_E$。
本页 $\rho_b=0$，$\eta_b$ 的整体型为 $1$；
Cartier 的半线性使 $\nu_2=C^2\eta_b$ 仍为型 $1$。
在 $S,-S$ 处，$\mu_3$ 固定该点，局部参数 $x$ 按非平凡三次单位缩放。
至多二阶极的 simple 和 double 微分分别为局部型 $0$、$2$，
均不等于型 $1$。故本页的 $\nu_2$ 在两个三挠点**完整正则**；
这不是仅将其两个 residues 设零。

由 (27) 的二挠帽，两次 Cartier 后先有极阶至多 $p+8$。
又 $\nu_2=f_{2,b}\omega_E$ 中的 $f_{2,b}$ 为 $\mu_6$ 不变函数，
在二挠点的 $y\mapsto-y$ 下极阶必须为偶数，
遂准确收紧到 $p+7$。原点正则又已支付，所以
$$
\boxed{
\nu_2=\frac{Q_b(X)}{(X+1)^M}\omega_E,\qquad
M=\frac{p+7}{2},\quad \deg Q_b\le M,\qquad
c_b^\sharp=[X^M]Q_b.
}
\tag{26a}
$$
每个 $Q_b$ 仍由原完整输入及两次 Cartier 决定，未自由选列。

第三 Cartier 的全部坐标也可以直接读出。准确重写
$$
\nu_2=(y^{-3})^p\,\frac12 Q_b(X)(X+1)^{p-4}\,dx .
$$
其多项式的 $x$ 次数至多 $(9p-3)/2$，而只含 $x^{3j}$。
在所有实际 $x^{kp-1}$ 槽中，
$p\equiv-1\pmod3$ 迫 $k\equiv2\pmod3$，
当前次数帽内唯一可能是 $k=2$。于是
$$
\boxed{
a_b=[X^{(2p-1)/3}]Q_b(X)(X+1)^{p-4},\qquad
C^3\eta_b=a_b^{1/p}\frac{x}{y^2}\omega_E
=-\frac{c_p}{3}a_b^{1/p}\varphi .
}
\tag{26b}
$$
这也自含证明该页第三层确落在原
$\Omega(2\mathcal D_2)$ 的型 $5$ 一维方向。
(26a) 的顶系数和 (26b) 的完整 binomial 读数是两个不同实际泛函；
没有证明它们互相成比例，不能将某一非零值转给另一行。

还可明确保原伴随的三挠余量：
本页 $b\le p-6$，$P_{10}$ 在 $S,-S$ 至少 $p$ 阶零，
所以 $\gamma$ 输入的实际三挠帽已经是
$$
\operatorname{pole}_{\pm S}\eta_b\le2p^2-5.
\tag{26c}
$$
原一阶真实连接的费用为一；即使保至多四次微分费用，
两次 Cartier 仍至多二阶。
只有当**整个**返回继续具有上述型 $1$ 时，
才可再次使用这个局部角色排除。
其余 $r$ 页、各分拆伴随项及其二挠费用仍依 §8 全量保留。

## 8. 高窗口的完整极与两 exact

(10)在特征 $p$ 已把十三权的二挠极降为准确上界 $8p^2$，
两个 β 模型在 $S,-S$ 的极分别至多 $p^2,2p^2$。
原 $P_{10}$ 的 $Z^p$ 因子在两三挠点继续消去所有 $b<p$ 的 cut。
因此可统一用
$$
\boxed{
\operatorname{pole}_{\mathcal D_2}\eta_b
\le p^3+7p^2+(8-b)p+1<2p^3,\quad
\operatorname{pole}_{\pm S}\eta_b\le2p^2,\quad
\operatorname{pole}_O\eta_b\le p.
}
\tag{27}
$$
原点留数依然先准确去掉。
第一、第二 Cartier 的帽逐点按
$d\mapsto\lfloor(d-1)/p\rfloor+1$ 计算；
特别三挠第二层至多二阶。
$\varphi_*$ 在三挠点的一阶零于是仍给
$K_b$ 的三挠极至多 $2p-2$。
二挠按 R1032 的完整 max 式支付，
全部 affine 项 $a_bZ$ 保留。

第三 Cartier 的边界仍在 R1032 的全部九维空间内。
若施原 whole 四阶伴随，三挠先加四阶真实费用，
二挠加原 $G$ 及连接的四次费用；
R887 给 $G$ 的原二挠极阶为 $p^2-p-1$，
所以二挠仍严格小于 $2p^3$。
一般页面四阶后的三挠帽为 $2p^2+4$，
故第二 Cartier 上限为三阶、对应 primitive 至多 $3p-2$；
第三 Cartier 仍为 simple 边界。只有 §7.1 的 $r=p$ 页
有额外五阶余量，且只对完整型保持的返回可再排极。
原点最后四个 $b$ 的补项仍按 R1018/R1032 全部保留。
这些费用不改变 (22) 的实际物理矩阵，
也不删除 (24) 的全纯 scalar。
它们不表示未施伴随的显示极帽逐项不动。


## 9. 两组三挠极的原 Weyl 权、完整奇主部与 P10 缺陷

本节使用 R1034 的同一高窗、同一十三权和两枚特征零平坦权。
以下模 $p$ 的 $h_\beta,h_\gamma$ 分别指该篇真实 target 的约化；
后者的原特征零定义是 $3h_{\rm big}-2h_{\rm small}$。
完整中央精度仍由该篇原始 target 支付，不能只从下面的约化反推。

### 9.1 原三处提升的中心和完整来源

置
$$
u=(0,-1),\qquad v=(a,\delta),\qquad a^3=-4,
\qquad [\delta]v=u,\qquad S=-u=(0,1).
$$
这里 $a$ 就是 R1021 原 $v_3$ 的坐标，不另换三次根。
在 degree390 的原 canonical theta group 中，
$$
T_uT_v=\omega T_vT_u,\qquad T_u^3=T_v^3=1.
\tag{28}
$$
此中心与 R1022 的 $\kappa(P+u)=\omega\kappa(P)$ 相同：
$T_vD_\delta$ 的原有理字为 mode1，因为 $130\equiv1\pmod3$。
原提升为 Weyl 规范，故其准确乘法为
$$
T_vT_{ju}=\omega^jT_{v+ju},\qquad
T_{-v}T_{ju}=\omega^{2j}T_{-v+ju}
\quad(j=0,1,2).
\tag{29}
$$
这些是阶三中心的唯一平方根规范；没有在局部极点重新选相位。

令 $G$ 分别为 R1021 的完整 $G_A,G_B$，始终包含全部十二个十三字，
并记
$$
|i\rangle=T_v^iD_\delta G,\qquad i\in\mathbf F_3.
$$
因此 $T_u|i\rangle=\omega^i|i\rangle$。
原正分支 $u_3=\pi^{-1}v$ 在 $E[3]$ 中为
$u-v$：因为 $\pi\equiv-1-\delta\pmod3$，而 $\delta^2=0$ 在 $E[3]$ 上。
结合 (29)，准确有
$$
T_{u_3}D_\delta G=\omega|2\rangle,\qquad
T_{-u_3}D_\delta G=\omega|1\rangle.
\tag{30}
$$
所以 R1021 的两个 raw canonical 来源可统一写成
$$
f=C(|1\rangle-|2\rangle),\qquad
C=\begin{cases}
\omega/(8C_3^{10}),& f=f_A,\ G=G_A,\\
\omega/(60C_3^{10}),& f=f_B,\ G=G_B.
\end{cases}
\tag{31}
$$
若用首项一的 $\Psi_{35},\Psi_{53}$，须同时除以 R1021 已付的
实际 $\gamma_A,\gamma_B$；本节没有添加任意比例常数。

原三处因子是唯一 odd 线，其余有限因子的整体 parity 为 odd。
对每个 $0\ne T\in E[3]$，原 Weyl 算子的 $1$-本征线为 even：
可用有限 Weil 的 $\mathrm{SL}_2(\mathbf F_3)$ 将其化为
$T_u$ 的第零字，而该作用保持 parity。
因此在 odd 线上 $T_T+T_{-T}=-1$，准确得到
$$
\boxed{\Pi_{\rm even}T_Tf=-\frac12 f
\quad(0\ne T\in E[3]).}
\tag{32}
$$
这里投影的是整个原来源，不是任何单十三字。
同一个 degree390 Gaussian 是偶函数，所有惰性 Newton 项都读取
偶次数，故整个 Tate 函数系数逐项满足
$$
\boxed{J_{390,T_Tf}(v)=-\frac12J_{390,f}(v).}
\tag{33}
$$
这给两条原坏 canonical 的合法三挠 translated Tate 零。
它不对任意十三平移或三挠点处的加权主部赋零。

### 9.2 两个纤维的极系数与不可省的 cocycle

沿本篇取
$$
\beta=\frac{X}{X+4},\qquad
\gamma=3\beta^2-2\beta=\frac{X(X-8)}{(X+4)^2}.
$$
设 $T=(a_T,b_T)$ 是六个非核三挠点之一。
用原不变微分局部参数，或模 $p$ 的原 $Z$ 参数，头两项准确为
$$
\beta(P+T)=\frac{c_T}{Z}+\frac13+O(Z),\qquad
c_T=-\frac{2}{3a_T^2b_T},
$$
$$
\boxed{\gamma(P+T)=\frac{3c_T^2}{Z^2}+O(1).}
\tag{34}
$$
事实上 $DX=6x^2y$、$D^2X=6x(7X+4)$，
在 $X=-4$ 给 $1+2D^2X/(DX)^2=1/3$，
于是 $\gamma$ 的 simple 项准确消去。
不能只看裸 $\beta$ 的极而漏掉这个常数。

记 $c_0=-2/(3a^2\delta)$。
原点加法给两组三点及其系数：
$$
\begin{array}{c|c|c|c}
T&x(T)&c_T&\varepsilon(\pm v,ju)\\ \hline
v+ju&\omega^{2j}a&\omega^{2j}c_0&\omega^j\\
-v+ju&\omega^ja&-\omega^jc_0&\omega^{2j}.
\end{array}
\tag{35}
$$
最后一列正是 (29) 的原 cocycle。
例如在 $\alpha$-trace 平移到 $[\alpha]v=S$ 后，
$T_vT_{ju}$ 出现；不能将其改成系数一的 $T_{v+ju}$。

用原 $u$-字投影逐项求和，得到四条完整 theta 恒等：
$$
\boxed{\begin{aligned}
\sum_{j=0}^2\omega^j c_{v+ju}T_{v+ju}f
 &=3c_0C|2\rangle,\\
\sum_{j=0}^2\omega^{2j}c_{-v+ju}T_{-v+ju}f
 &=3c_0C|1\rangle,\\
\sum_{j=0}^2\omega^j c_{v+ju}^{\,2}T_{v+ju}f
 &=-3c_0^2C|0\rangle,\\
\sum_{j=0}^2\omega^{2j}c_{-v+ju}^{\,2}T_{-v+ju}f
 &=+3c_0^2C|0\rangle.
\end{aligned}}
\tag{36}
$$
例如第一式将 $T_{v+ju}$ 换成
$\omega^{2j}T_vT_u^j$ 后只取 $|1\rangle$；
第三式则只取 $|2\rangle$，经 $T_v$ 返回 $|0\rangle$。
这证明 double 权留下的确实是整个 $\delta$-old 来源 $D_\delta G$。
不是由点值、奇偶猜测或遗漏相位得到的消项。

### 9.3 完整十三权后的实际 target 主部

记
$$
b_\pi=v_\pi(u)=v_\pi(-u)=R_\pi(0)
=\frac{40+24\delta}{13},\qquad \Lambda_\pi=b_\pi^{\,2p^2}=b_\pi^2.
$$
$\operatorname{Nm}(b_\pi)=2^8/13$，
所以在当前好惰性位上，这些显示常数为单位；
六个三挠点和 $\omega,\delta$ 均定义在剩余域的二次扩域中，
故 $c_T^{p^2}=c_T$。
这里没有对 $C$ 或整个来源的系数作未经证明的 $p^2$ 固定假设。

原 $[\alpha]$ trace 的 theta-section 身份，平移到 $S$ 后为
$$
D_\alpha T_S^{10}h
=\sum_{K\in E[\alpha]}
 \varepsilon(v,K)\,V(P+v+K)\,T_{v+K}^{390}f.
\tag{37}
$$
只有 $K=ju$ 的三项在此原点有极；
其余三十六项在该点全纯。
三个极项的 $\delta$-像完全相同，故完整十三权共同为
$v_\pi(\delta P+u)^{2p^2}$。
因为 $X$ 在 $u$ 处有三阶零，
$$
v_\pi(\delta P+u)^{2p^2}
=\Lambda_\pi+O(Z^{3p^2}).
$$
因此对 simple $p^2$ 极和 double $2p^2$ 极，
该完整十三权在负部中准确只留下 $\Lambda_\pi$；
这是一个已付的逐项阶比较，不是移出一般 trace。

以 $[\,\cdot\,]_{<0}$ 表示在共同局部 theta frame 中的负部，
(34)–(36) 给
$$
\boxed{\begin{aligned}
[D_\alpha T_S^{10}\bar h_\beta]_{<0}
 &=3\Lambda_\pi c_0C[Z^{-p^2}|2\rangle]_{<0},\\
[D_\alpha T_{-S}^{10}\bar h_\beta]_{<0}
 &=3\Lambda_\pi c_0C[Z^{-p^2}|1\rangle]_{<0},\\
[D_\alpha T_S^{10}\bar h_\gamma]_{<0}
 &=-9\Lambda_\pi c_0^2C[Z^{-2p^2}D_\delta G]_{<0},\\
[D_\alpha T_{-S}^{10}\bar h_\gamma]_{<0}
 &=+9\Lambda_\pi c_0^2C[Z^{-2p^2}D_\delta G]_{<0}.
\end{aligned}}
\tag{38}
$$
这些是实际 meromorphic theta sections 的局部身份。
可以使用原代数模型及反演相容的局部 frame；
这里不把含 $p$ 分母的未 regularize sigma 系数强行约化。
$D_\alpha$ 与 $T_{\pm S}^{10}$ 的全部尺度留在显示式中；
没有将高阶代数 uniformizer 自由改成 $\alpha Z$。

最后两式的整个负部是 odd：
$G$ 为奇函数，而 $2p^2$ 为偶数。
所以在 canonical translated Gaussian 及任意共同偶 frame 中，
该负部的全部偶系数为零。
前两式的 $p^2$ 为奇数，不能作同样结论。
(38)也没有控制 (37) 的三十六个全纯余项；
它们仍按原十三 trace 与完整来源保留。

### 9.4 原有限读者留下的准确运输缺陷

(38)的 odd 主部不能直接从原 $P_{10}/Z$ 读者删除。
保持实际 $S$、$C_S$、$\Phi_+$ 及其负支，
只固定偶数次乘子 $q_S^{10}=C_S^{10}\Phi_+^{10}$、
$q_{-S}^{10}=C_S^{10}\Phi_-^{10}$，
并把整个原 finite transportation defect 记为
$$
\Xi_{10,T}=P_{10}(P+T)-q_T(P)^{10}P_{10}(P),
\quad T=\pm S.
$$
这正是原 R1024 的完整缺陷，包含其真实初值，
不是只用 $G(P+T)-G(P)$ 的首项替代。

若 $F_T=T_T^{10}h$，以 $R_{F_T}$ 表示它相对于原 $\sigma^{10}$
的完整有理部分，则源微分在该点的真实 pullback 是
$$
\tau_T^*(Z^{-b-1}P_{10}A_h\omega_E)
=Z_T^{-b-1}q_T^{-10}P_{10,T}R_{F_T}\omega_E.
$$
故它与 canonical unshifted finite input 的差准确为
$$
\boxed{\begin{aligned}
&\tau_T^*(Z^{-b-1}P_{10}A_h\omega_E)
 -Z^{-b-1}P_{10}R_{F_T}\omega_E\\
&=\left[
 (Z_T^{-b-1}-Z^{-b-1})P_{10}
 +Z_T^{-b-1}q_T^{-10}\Xi_{10,T}
 \right]R_{F_T}\omega_E.
\end{aligned}}
\tag{39}
$$
因此对 $\gamma$ 的两个显示奇主部，
canonical 偶读者确实消去它们；
原实际读者还剩 (39) 的完整 cut 差与 $\Xi_{10,\pm S}$。
这把所需补偿定位到明确原函数，未额外给任何新中央零。

(39)也保留全部高块物理矩阵：
该篇的原 $\widetilde P_{10},\widetilde Z$ 与
$\sigma^{\circ\,10}/\widetilde P_{10}$ 均按原式使用，
其未平移矩阵严格保持 parity。
当前 (38) 是原来源的模 $p$ 主部结论；
原特征零 target 与这份约化之间的更高 $p$ 位
仍在本篇的完整矩阵和原 Newton 权中。
不能用任意 odd lift 将这些实际高位误差设为零。

### 9.5 γ 的完整 logarithmic Jacobian 与固定有理原函数

另有两个不依赖 $p$ 的完整恒等：
$$
\boxed{\gamma
=\frac1\delta\frac{r_0(P)}{r_0(\delta P)},\qquad
\gamma\,[\delta]^*d\log y=d\log y.}
\tag{40}
$$
它们直接由原 $x_\delta,y_\delta$ 代入得到。
完整 norm 为
$$
\operatorname{Nm}_{[\delta]}(y)=3\delta\,y,
$$
故未平均 trace 有 $\operatorname{Tr}_{[\delta]}\gamma=1$，
与全三字的 old 返回一致。

置
$$
R_\gamma=-\frac{2xy}{3(X+4)}.
$$
直接微分给
$$
D\frac{xy}{X+4}
=\frac{-X^2+16X+8}{(X+4)^2},
\qquad
\boxed{\gamma=\frac13+DR_\gamma.}
\tag{41}
$$
因而裸 $C(\gamma\omega_E)=0$，但真正 $P_{10}$ 返回是
$$
\boxed{\begin{aligned}
C(P_{10}\gamma f\,\omega_E)
={}&\frac13C(P_{10}f\,\omega_E)
-C(P_{10}R_\gamma(D+10G)f\,\omega_E)\\
&-10\mathcal H Z\,C(Z^9R_\gamma f\,\omega_E).
\end{aligned}}
\tag{42}
$$
(42)逐项来自 $C(d(P_{10}R_\gamma f))=0$ 和
$DP_{10}=10GP_{10}+10\mathcal H^pZ^{p+9}$。
该式保留全部曲率，不从裸 exact 推 whole exact。
使用于实际十三字时，所有函数必须放在同一个原 source 点，
并继续保留完整 Miller、$\chi_8$、十三 trace 与测试。

最后，整个三字为
$$
\gamma=\frac13+\frac{h}{3x^2}\kappa
       +\frac{x^2}{3h^2}\kappa^2,
\qquad h=1-y.
$$
特别第2系数是 $x^2/(3h^2)=-\frac{1+y}{3xh}$，
不能漏掉最后的 $h$。
与 $\beta$ 的正 mode2 比较，实际返回之比准确是
$$
\boxed{
\bar A_\gamma(A_+)=r_S^{-2p^2}R_{T_S^{130}G_A},
\qquad
\frac{\bar A_\gamma(A_+)}{\bar A_\beta(A_+)}
=\left(\frac{y+1}{y-1}\right)^{-p^2},
}
\tag{43}
$$
$B_+$ 同式，old 行仍为原 $R_g$。
(43)来自本篇两个真正同精度平坦 target，
而不是允许给中央零任意乘一个 $p^2$ 次幂。
两次 Cartier 后须保留其固定比
$(y-1)/(y+1)$；(39)、(42)和完整高位账本仍是剩余的实际条件。


## 10. 后继真正需消费的全式

两枚合法高窗 β 模型现在同时提供：
同一个 (8) 的原中央精度、
同一个十三平方权、
(15)的真实 $U^{-p^2}$ 比较、
(22)–(23)的原物理系数账本，
以及 (25) 的第二 Cartier 回填。
它们均对 R981 的两条完整 canonical 来源成立，
未把任何单独十三字或一个任意 base 乘子赋零。

原单位组合 $\lambda_1-(10/81)\lambda_2$
仍须在这份完整读者中由实际 source/adjoint 关系逼出。
R616/R619 的真实端点自动返回低中央数据，
因此不能把高块自身、(26) 或六个原三挠点的某个裸 residue
写成已经完成无穷性。

全文未新增数学执行。原二坏带引用 R614/R616/R619；
本篇新内容是同精度两枚合法平坦权、其完整 β/γ 返回与绝对三挠主部、
一个确定的整 native lift 及全物理高行，和不可删的第二 Cartier 行。


## 11. 同步全39处的实际 Jacobian 权、唯一边界与首个物理耦合

本节改用一个完整新权来支付 §9.4 留下的实际二挠费用。
它同时处理三处和十三处，不把中间的 $1/y$ 移出原十三 trace。
以下仍是同一两个 $H$、同一原来源、同一矩阵 (22) 和同一两坏带。

### 11.1 一阶算子指出的实际新根

令 $V=2yD$，其对偶微分为
$\beta_V=\omega_E/(2y)$。
原三倍 CM 公式直接给
$$
\chi_\delta(P)=\frac{X(P)}{X(P)-8}
=\frac{y(P)}{\delta^3y(\delta P)},\qquad
[\delta]^*\beta_V=9\chi_\delta\beta_V .
\tag{44}
$$
所以 $V_{\rm up}[\delta]^*=9\chi_\delta[\delta]^*V$。
这是真正的一阶向量场 Jacobian，非凭极帽挑选的乘子。

在原 $\kappa^3=h=1-y$ 三字中，完整公式是
$$
\chi_\delta=\frac13-\frac{x}{3y}\kappa
-\frac{x^2}{3yh}\kappa^2,\qquad
\operatorname{Tr}_{[\delta]}\chi_\delta=1 .
\tag{45}
$$
例如 $y_{\rm up}=\delta(\kappa^2+x)/(\kappa^2-x)$，
且 $(\kappa^2-x)^{-1}=(h\kappa+x\kappa^2+x^2)/(2h)$，
逐项就给 (45)。
正 mode2 与原 $\beta$ 的第1字之比准确为 $(y-1)/y$；
负支的比为 $(y+1)/y$。
所有 $N=130$、$C_S$、Miller 与十三字仍取 §4 的原规范。

只使用 (45) 时，中间 target 的新 $y^{-p^2}$ 不能跨十三 trace。
实际 $y_\pi/y=B_\pi/(\pi^3R_\pi^3)$，其中
$$
B_\pi=(A_\pi+3XA_\pi')R_\pi-6XA_\pi R_\pi' .
$$
因此 $y_{\rm up}^{-p^2}
=(B_\pi/(\pi^3R_\pi^3))^{p^2}y_{\rm target}^{-p^2}$；
完整额外 $B_\pi$ 字必须保留。
下面直接同步整个 $\alpha$，从来源上避免这次不合法交换。

### 11.2 全 α 的一个特征零平坦权

定义固定有理函数
$$
\boxed{
\chi_\alpha(P)=\frac{y(P)}{\alpha^3y(\alpha P)}
=\chi_\delta(P)\chi_\pi(\delta P),\qquad
\chi_\pi=\frac{R_\pi^3}{B_\pi}.
}
\tag{46}
$$
它的规范完全由原 CM 有理图确定。原点 $y(\alpha z)\sim
\alpha^{-3}y(z)$ 给 $\chi_\alpha(O)=1$；
整个函数为原 $\mu_6$ 不变量。

它的全部零极如下：

- 非零 $E[\alpha]$ 共38点，每点恰三阶零；
- $[\alpha]^{-1}(\mathcal D_2)\setminus\mathcal D_2$ 共114点，
  每点恰 simple 极，且全映到 target 的三个二挠点；
- 在原三个二挠点，分子分母的一次零相消，留下单位；
- 没有其它零极，也没有新的 $S,-S$ 极。

这些计数由 $[\alpha]$ 在当前好位为次数39的 étale isogeny
及 $\ker\alpha$ 为奇数阶直接得到。
好整模型下 (46) 的局部单位及全部有理图系数只用原固定坏集；
没有随 $p$ 新增垂直分母。

保持 (1)，置
$$
a=p^2-k,\qquad
\mathcal V_\chi=\chi_\alpha^a B_{a,k}(\chi_\alpha).
\tag{47}
$$
因为 $n<2p^2$，准确有
$$
3a=3p^2-\frac n2>n+1,\qquad a+k=p^2 .
$$
所以特征零的 $\mathcal V_\chi$ 在原点为
$1+O(z^{n+6})$，在全部38个非零核点从高于 $n$ 阶起。
每个 simple 极的实际阶数至多 $p^2$；
这个帽在特征零已经成立，不仅是约化后成立。
(9)又给完整多项式身份
$$
\boxed{\overline{\mathcal V_\chi}=\chi_\alpha^{p^2}.}
\tag{48}
$$

沿原未平均 trace 定义
$$
A_\chi=\alpha^{-10}\operatorname{Tr}_{[\alpha]}
  (\mathcal V_\chi R_f/R_\alpha^{10}),\qquad
h_\chi=\sigma^{10}A_\chi .
\tag{49}
$$
全部原 theta lift、有限39字、$\alpha$ 微分尺度和两个 Gaussian
都与 (4)、(8) 相同，逐支得到
$$
h_\chi(\alpha z)-f(z)=O(z^{n+1}).
\tag{50}
$$
target 的全部非原点极只在 $\mathcal D_2$，每处至多 $p^2$。
对本篇的 principal 来源，$A_\chi$ 为偶函数；
在二挠点的反演局部参数下极阶必须为偶数，故真实帽为 $p^2-1$。
因此还可用完整整基
$$
A_\chi=x^2\frac{P_\chi(X)}{(X+1)^M},\qquad
M=(p^2-1)/2,\quad \deg P_\chi\le M .
\tag{51}
$$
最高次数已用 $m_0(h_\chi)=0$ 收去；
所有系数在当前原好整环中，且 (51) 是完整 trace 的结果，
不是自由选择的 target 多项式。

(48)的完整返回也可写成
$$
\bar h_\chi
=\alpha^{-3p^2}y_{\rm target}^{-p^2}\,
 \mathcal T_\alpha(y_{\rm source}^{p^2}f),
\tag{52}
$$
其中 $\mathcal T_\alpha$ 是 (49) 的原 theta trace。
特别，(52) 绝不把 $y_{\rm source}^{p^2}$ 换成 $y_{\rm source}$，
也不把其完整39字或物理框架删掉。
另外真正的微分 Jacobian 为
$[\alpha]^*\beta_V=\alpha^4\chi_\alpha\beta_V$。

### 11.3 用原第二半径支付整个 p^H 精度

(51) 仍具有 §5 的实际整展开
$A_\chi=u^{-10}\sum_{j\ge1}a_ju^{6j}$。
原 R618 的第二半径
$$
\tau_2=\frac{2p-1}{p(p^2-1)},\qquad R_2=p^{-\tau_2}
$$
上，$W_0$、$u/z$ 及其逆在略大盘均为单位；
$U_\sigma$ 在每个严格内盘为范数一的单位。
故对每个 $R<R_2$，整个 Gaussian 的范数至多 $R^6$。
这对任意增长的 $M$ 同时成立，因为 $a_j$ 整且 $|u|=R<1$。
原 source $f$ 及两个实际 Gaussian 的整差也有同一个界。

因此 R618 的完整无限尾证明逐项给
$$
v_p(T_h)\ge
\left\lceil h\left(1-\frac{2p-1}{p(p-1)}\right)
 +6\tau_2\right\rceil+v_p((h-1)!) .
\tag{53}
$$
在 $h=2p-1$ 右侧至少 $2p-3$，以后单调趋于无穷。
对剩下的 $H+1\le h\le2p-2$，原两坏带给 $v_p(g_h)\ge-2$，
而 $(h-1)!$ 恰含一次 $p$，所以 $v_p(T_h)\ge h-1\ge H$。
这覆盖整个无限尾，严格得到
$$
\boxed{
j_f-j_{10,h_\chi}-m_0(f)\log_pq_\alpha
\in p^H\mathcal O,\qquad H=2p-11,\ 2p-5.
}
\tag{54}
$$
没有把阶乘的 $p$ 当作单位，也没有在旧截断上虚增精度。
同一个改进证明适用于本篇前面的两个 β target；
其整局部展开同样已付。
所以三种模型可在真正同一个 $p^H$ 精度中比较。
(16)–(18)及整个物理矩阵 (22)继续保留全部实际高位。

### 11.4 完整新帽只留一个 r=p 边界页

取这个新 $A_\chi$ 的原
$\eta_b=Z^{-b-1}P_{10}A_\chi\omega_E$。
由 (51)，其二挠帽准确可取
$$
\boxed{
\operatorname{pole}_{\mathcal D_2}\eta_b
\le p^3+(8-b)p ,
}
\tag{55}
$$
其它非原点极全部消失。
原点仍先按 §7 去留数，两个 exact 与所有 $a_bZ$ 保留。

专门在 $r=p$ 页，$b\equiv5\pmod6$。
当 $b\ge11$，两次 Cartier 的帽先至多 $p$，
型 $1$ 的反演偶性再将其降到 $p-1$。
第三次最多 simple，但型 $5$ 排除这些 residues，
又排除原全纯 $\omega_E$，故
$$
C^3\eta_b=0\qquad(r=p,\ b\ge11).
\tag{56}
$$
只有 $b=5$ 可留原 $\varphi$ 方向。此时
$$
\boxed{
\nu_2=C^2\eta_5=\frac{Q(X)}{(X+1)^{3s}}\omega_E,\qquad
\deg Q\le3s,\qquad c_5^\sharp=[X^{3s}]Q .
}
\tag{57}
$$
第三次 Cartier 的完整槽为
$[X^{4s-1}]Q(X)(1+X)^{p-1}$。
因为 $3s<4s-1<p$，使用
$\binom{p-1}{j}=(-1)^j\bmod p$，准确得到该槽为 $-Q(-1)$。
于是同一规范下
$$
\boxed{
C^3\eta_5=-Q(-1)^{1/p}\frac{x}{y^2}\omega_E
=\frac{c_p}{3}Q(-1)^{1/p}\varphi .
}
\tag{58}
$$
这里 $-Q(-1)$ 是中间抽系数，不能漏掉返回 $\varphi$ 时的负号。

两个端点确实不同。分解 $Q=(X+1)R+Q(-1)$ 给
$$
\nu_2=\frac{R(X)}{(X+1)^{3s-1}}\omega_E
 +Q(-1)\frac{\omega_E}{y^{p+1}} .
\tag{59}
$$
前一项的 Cartier 准确为零，且它承载 $c_5^\sharp$；
后一项承载 (58)，但在 $O$ 的值为零。
因此不能由唯一 $b=5$ 就把 $Q$ 的最高系数和 $Q(-1)$ 合并。

### 11.5 同一个物理 M 的首个实际耦合

原 R887 §19 (105)–(107) 的全部坐标账本给
$$
\kappa_5=\frac{(3/5)^p}{c_p},\qquad
Z=z-\kappa_5z^{5p}+O(z^{11p}),
$$
$$
P_{10}=(\sigma^\circ)^{10}
 \{1+e_{10,p}z^{6p}+O(z^{6p+6})\}.
\tag{60}
$$
同一个原 Taylor 证明适用 $10<p$；
这里没有从 $G$ 的较短前缀猜 $P_{10}$ 初值。
特别，矩阵 (22) 的第一个相对 $5p-1$ 项完全来自 $Z^n$，
系数准确为 $-n\kappa_5$；
$P_{10}$ 框架到相对 $6p$ 才进入。

令 $n=p^2+b$、$b\equiv5\pmod6$。
所有相关相对指标仍在原整窗内，故这些 $M$ 项本身整。
准确有
$$
\boxed{
M_{h,p^2+b}\equiv0\pmod p\quad(p\le h\le p+3),
}
$$
$$
\boxed{
M_{p+4,p^2+5}\equiv-5\kappa_5\in k^\times,\qquad
M_{p+4,p^2+b}\equiv0\quad(b\ge11).
}
\tag{61}
$$
理由是 $(p+1)(p+4)-(p^2+b)=5p+4-b$：
唯一达到 $5p-1$ 的项是 $b=5$。
$h<p$ 则这些 native 指标尚未进入。

这给 (57) 的真正第一次物理耦合，不是新增一个自由读者。
(61) 只陈述这些整矩阵项的首剩余位；
其更高 $p$ 位、其它 native 行、R616/R619 的低回填、
全部 Newton 阶乘和 (58) 的另一端点仍保在 (22)–(23)、(54) 内。

### 11.6 唯一边界的原 G 四项顶部证书

(58) 的目标可以进一步压成同一个完整来源的确定局部槽。
置 $F=F_p=Z+\rho_pr_0^p$，仍有 $DF=1$。
原全函数恒等是
$$
\begin{aligned}
A_0=D^{p-2}x&=-c_pF,\\
A_1=D^{p-3}x&=(\rho_px^p-c_pF^2)/2,\\
A_2=D^{p-4}x&=-c_pF^3/6+\rho_px^pF/2-\rho_p^2y^p/3,\\
A_3=D^{p-5}x&=-c_pF^4/24+\rho_px^pF^2/4
 -\rho_p^2y^pF/3+\rho_p^3x^{2p}/8 .
\end{aligned}
\tag{62}
$$
逐微分证明相邻式之差为 $p$ 次幂；
其原点极帽与原 CM 型只准显示的 $x^p,y^p,x^{2p}$ 单项。
最高原点极固定其系数，$\rho_pc_p=1$ 固定绝对尺度；
不留任选 horizontal 项。

在任一原二挠点，$F$ 正则且为零。
Wilson 公式将原 $G$ 的最后四项准确化为
$$
G_{\rm top}=-\sum_{j=0}^{3}j!\,Z^{p-1-j}A_j .
\tag{63}
$$
其余原项相对最高极至少低 $4p$；
而本页 (55) 所需的相对窗仅为 $3p-1$。
原 $P_{10}$ 中出现至少一次微分的分支，相对纯
$G^{p-1}$ 分支又至少低 $p^2-p-2>3p$。
所以在这个确定窗内可以准确使用
$P_{10}=-Z^{p+9}G_{\rm top}^{p-1}$，
但完整 $A_\chi$、$Z$ 与微分尺度不变。

具体取 $Q_e=(e,0)$、$e^3=-1$，以实际局部参数 $y$ 记
$$
B_e=[y^{-p^3-1}]
\left(-\frac{Z^{p+3}G_{\rm top}^{p-1}A_\chi}{3x^2}\right).
\tag{64}
$$
则 (58) 的同一个系数准确满足
$$
\boxed{Q(-1)^{p^2}=-\frac{3B_e}{e}.}
\tag{65}
$$
这是因为 $\omega_E=dy/(3x^2)$，而
$C^3\eta_5$ 的 $y^{-2}dy$ 系数是
$-Q(-1)^{1/p}/(3e)$，并有 $e^{p^3}=e^{-1}$。
三个二挠点的结果由同一个全局型相容；
没有只取一个根而删除另外两个。

(64) 是四个原函数与原完整 trace 的实际有限读者。
它仍需要 $A_\chi$ 在该原窗中的所有系数；
不由裸 $G$ 主项或任意局部单位直接断言 $B_e\ne0$。

### 11.7 真正的一阶伴随后，哪些页重新出现

R1021 §10–11 已付两原 canonical 的完整
$Q_1U_B=U_A$ 和全部 $\chi_8$/Miller 规范。
在尚未移位的同点坐标中，其 finite transpose 为
$$
Q^\dagger a=-2y(D+10G)a-15x^2a .
\tag{66}
$$
但原整 word 不能将这个 $y$ 与 $G$ 误放在同一个点。
沿 R1018 (26)–(34) 完成外部 pull 后，原 $G$、$P_{10}$、
$Z$ 在实际 reader 点 $P$，标准来源则在 $P-R_i$。
记 $y_i=y(P-R_i)$、$x_i=x(P-R_i)$；
把所有 Fourier、Miller、cut 及平移因子保在实际权 $a_i$ 内，
准确的一阶转置为
$$
Q_i^\dagger a_i
=-2y_i(D+10G)a_i-15x_i^2a_i .
\tag{66a}
$$
这里 $D$ 作用于整个 $a_i$，并未删除 $D\log h_i$ 或
其它 Miller 导数；原 $\alpha,\pi$ 尺度与字符系数仍按各字保留。
对应 $DP_{10}$ 的曲率项也仍取 R1021 (72) 的完整公式。

primitive 三十九字的非零 $R_i$ 为 odd-order torsion。
因此在原 $G$ 的三个二挠点，$y_i$ 和原 Miller 函数都是单位，
不能使用未平移 $y$ 的一次零。
在最终整体偶投影之前，各字的 $A_{\chi,i}$ 只取 $p^2$ 极帽；
于是其原微分帽为 $p^3+(8-b)p+1$。
$y_iG$ 的实际新增极费为 $p^2-p-1$，而微分项至多加一，
故一个对全部这些字安全的完整上界是
$$
\boxed{p^3+p^2+(7-b)p.}
\tag{67}
$$
最后全 word 求和与原 principal 投影不增加这个帽。
若另有已经支付的整体偶性，可再收一阶；
只有真正未平移的同点 test 才可使用 $y$ 的零而再收一阶。
本篇不将这两次收紧预先用于 (66a)。

另外 (66a) 还保留真实移位支撑：
在 $P=R_i$，$y_i$ 三阶极和 $x_i^2$ 四阶极使相对费用至多四；
在其余非二挠点，原 $G$ 正则或在 $O$ 为 simple，
所以对既有 Miller/cut 极的微分费用至多一。
这些点的原权、曲率、两个 exact、留数及 $\varphi_*$ 修正均随
完整 trace 保留；(67) 不是将其删除后的全局边界声明。

所以 (56) **不能**在施加整个 $Q^\dagger$ 后继续逐页使用：
原 $\varphi$ 方向在其余 $b\equiv5$ 页会重新出现。
完整源端身份只授权原 $U_A,U_B$ 两行，
不把这些新页或某个 $F^p$ 倍测试赋零。

(61) 和 (64) 已把所需的两个实际端点分别定位；
接下来仍须在整个 (22)、(54)、(66a) 中将它们真实联立。
不会把低帽、首单位、$p$ 曲率谱或一次裸抵消代成这个联立。

### 11.8 原二挠译源的合法返回与确切变权

R1021 §13 在原 $N=390$ theta lift 上已付：
对两条当前 dyadic $\varepsilon_0$ canonical 来源及每个
$0\ne T\in E[2]$，
$$
\Pi_{\rm principal}T_T^{390}f=\frac1{\sqrt3}f,\qquad
J_{390,T_Tf}=\frac1{\sqrt3}J_{390,f}.
\tag{68}
$$
这里的正号包含 $N=10$ 半周期负号与原 $\alpha=2+7\omega$
换代表的另一枚负号；不可直接使用低层负号。
所有原13/3字与二挠 lift 的 commutator 为一，
所以 (68) 是完整 source 的合法零，未拆任何十三字。

将它用于 (49) 时，须对 $T_Tf$ 重新使用这个真正平坦权。
准确 theta 共轭仍为
$$
h_{\mathcal V_\chi}[T_Tf]
=T_{\alpha T}^{10}\,
 h_{\mathcal V_\chi\circ t_{-T}}[f].
\tag{69}
$$
不能把右边换成 $T_{\alpha T}^{10}h_{\mathcal V_\chi}[f]$：
后者在新的原点有实际极。

变权本身也有完整有理式。
若 $T=(e,0)$、$\alpha T=(e_\alpha,0)$，原二挠加法给
$y(P+T)=-3e^2y(P)/(x(P)-e)^2$，故
$$
\boxed{
\chi_\alpha(P+T)
=\chi_\alpha(P)\,
 \frac{e^2}{e_\alpha^2}
 \left(\frac{x(\alpha P)-e_\alpha}{x(P)-e}\right)^2 .
}
\tag{70}
$$
实际 $\mathcal V_\chi\circ t_{-T}$ 必须将 (70) 整体代入 (47)；
其全部极、$P_{10}$ 初值及原 cut/运输缺陷继续保留。
因此 (68) 提供了所需 $O/\mathcal D_2$ 交换的原 source 授权，
而 (69)–(70)明确了尚须消费的真正权差。

本节没有新增数学执行。新的实际结论是完整39处同一个 Jacobian
平坦输入、$p^H$ 全尾、仅一个未施伴随的边界页及其第一物理单位槽；
两个端点 (57)–(58) 和重新出现的 (67)始终分开。
