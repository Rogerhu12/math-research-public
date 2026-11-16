# R856 — 原偶 degree 截面的全 Hurwitz Frobenius 递推与四首行的双变量整除

日期：2026-11-16。**状态：以下全 Hurwitz 格的通用 $D^p$ 恒等式、原超奇异纤维的完整块递推，以及四个实际输入在双变量参数环中的整除 $p$ 均已证明。除 $p$ 后四个指定值不同时为零仍未证明。**

本篇继续 [R855](R855-original-full-heat-connection-and-canonical-divided-jet.md) 的同一 $\sigma,x,y$、同一 $\mathscr V_m$ 和四个原截面。证明不在特征 $p$ 的 Hurwitz 环中除以 $\sigma$：该环的零常数项元素有非平凡零化子，直接作此消去不合法。取代它的是两个相反点的**单位**平移截面，其乘积由原 addition 恒等式准确返回。

## 1. 整环、Hurwitz 约化与原 Hasse 导子

固定 $p>3$，令
$$
A=\mathbf Z_{(p)}[g_2,g_3],\qquad
\bar A=\mathbf F_p[g_2,g_3],
$$
$$
E:\ y^2=x^3-\frac{g_2x}{4}-\frac{g_3}{4},\qquad
D x=2y,\quad D y=3x^2-\frac{g_2}{4}.
\tag{1}
$$
在固定有限分母处再局部化不改变下述证明。几何解释在判别式非零处进行；所得多项式恒等式延拓到全参数环。

记
$$
\mathscr H_A
=\left\{\sum_{n\ge0} a_n\frac{z^n}{n!}:a_n\in A\right\}.
$$
这里先在特征零取实际 Hurwitz 系数，再逐系数模 $p$，得到除幂环
$\mathscr H_{\bar A}$。其乘法为
$$
z^{[i]}z^{[j]}=\binom{i+j}{i}z^{[i+j]},\qquad
D z^{[n]}=z^{[n-1]}.
\tag{2}
$$
因此 $D$ 是导子，$D^p$ 在特征 $p$ 仍是导子，且
$$
\ker D=\bar A,\qquad z^p=p!\,z^{[p]}=0.
\tag{3}
$$
这些是除幂坐标的陈述，不是普通 $\bar A[[z]]$ 中的求导规则。

R855 的整递推已给全部 $A_R=\sigma^mR$ 的 Hurwitz 整性。这里 $m$ 为任意正偶数；基仍是
$$
x^a\ (0\le a\le m/2),\qquad
yx^a\ (0\le a\le(m-4)/2).
\tag{4}
$$
若采用无 $1/m$ 的系数环，也可由 R855 的 sigma 整性与下文(15)逐基付清。

取原多项式
$$
H=H_p(g_2,g_3)
=[x^{p-1}]
\left(x^3-\frac{g_2x}{4}-\frac{g_3}{4}\right)^{(p-1)/2},
$$
$$
L_2=6g_3\partial_{g_2}+\frac{g_2^2}{3}\partial_{g_3},
\qquad C_p=L_2H.
\tag{5}
$$
以下右端均约化到 $\bar A$。R855(36)、(38)已在原函数域证明
$$
D^p=H D,\qquad
D^{p-1}x=Hx-C_p.
\tag{6}
$$
由于两边都是坐标环元素，(6)也在未局部化的坐标环成立。参数求导在形成 $C_p$ 时完整保留，未先令 $g_2=0$。

## 2. 单位平移的全部整初始资料

引入一个通用有限点 $T=(u,v)$，系数环
$$
B=A[u,v]/(v^2-u^3+g_2u/4+g_3/4).
\tag{7}
$$
它在 $A[u]$ 上以 $1,v$ 为自由基，特别 $u$ 对 $A$ 超越。设
$$
x_T(z)=\sum_{n\ge0}(D^n x)(T)z^{[n]},\qquad
q_T(z)=-\sum_{n\ge0}(D^n x)(T)z^{[n+1]}.
\tag{8}
$$
全部系数在 $B$ 中，且 $q_T(0)=0,Dq_T=-x_T$。令 $S_T$ 为唯一的整 Hurwitz 解
$$
DS_T=q_TS_T,\qquad S_T(0)=1.
\tag{9}
$$
逐阶递推只使用整数二项式系数，所以 $S_T\in\mathscr H_B$，且其常数为一，约化后仍为单位。

在复数泛纤维上它准确是
$$
S_T(z)=e^{-\zeta(T)z}\frac{\sigma(z+T)}{\sigma(T)}.
\tag{10}
$$
(10)仅用于识别同一 addition 身份；构造(8)–(9)本身不需要选择任何 $p$-adic $\zeta(T)$、周期或新 Gaussian。

需要的微分代数事实可直接用 Bell 多项式证明。若单位 $S$ 满足 $DS=qS$，则在特征 $p$，
$$
\frac{D^pS}{S}=D^{p-1}q+q^p.
\tag{11}
$$
事实上 $D^pS/S$ 的 Bell 项由非负整数 $(n_1,\ldots,n_p)$、
$\sum jn_j=p$ 编号，系数为整数
$p!/\prod_j(n_j!(j!)^{n_j})$。除 $n_1=p$ 与 $n_p=1$ 两项外，分母全部素因子小于 $p$，故系数被 $p$ 整除。这两项准确为 $q^p$ 与 $D^{p-1}q$。

对(9)使用(11)，并设
$$
Q_T=q_T^p-Hq_T-D^{p-2}x_T.
$$
由(6)，
$$
DQ_T=Hx_T-D^{p-1}x_T=C_p.
$$
(3)的核陈述遂给
$$
Q_T=C_pz-(D^{p-2}x)(T).
$$
因此单位平移满足完整恒等式
$$
\boxed{
D^pS_T=HDS_T+
\bigl(C_pz-(D^{p-2}x)(T)\bigr)S_T.
}
\tag{12}
$$
所有式子都在 $\mathscr H_{\bar B}$ 内，没有除以零质量截面。

## 3. 相反点返回与 whole 偶格

因为 $p-2$ 为奇数而 $x$ 在 $[-1]$ 下为偶函数，
$$
(D^{p-2}x)(-T)=-(D^{p-2}x)(T).
$$
$D^p$ 的乘积规则遂使两个常数修正准确相消：
$$
D^p(S_TS_{-T})
=HD(S_TS_{-T})+2C_pzS_TS_{-T}.
\tag{13}
$$

原 Weierstrass addition 式给
$$
\boxed{
S_T(z)S_{-T}(z)
=x(z)\sigma(z)^2-u\,\sigma(z)^2
=\Theta(z)-u\,\sigma(z)^2.
}
\tag{14}
$$
符号来自 $\sigma(-T)=-\sigma(T)$；两条(10)中的线性指数也相消。
可直接对照 Eilbeck–England–Ônishi 的(1.2)，其 $x=\wp,y=\wp'/2$ 与(1)完全一致。

(14)两边的每个 Hurwitz 系数均为 $B$ 中的多项式；故其复数泛纤维身份是整环身份，并可模 $p$。把(14)代入(13)，由于 $u$ 对 $\bar A$ 超越，逐 Hurwitz 系数比较 $1,u$ 的系数，得到
$$
D^p(\sigma^2)=HD(\sigma^2)+2C_pz\sigma^2,\qquad
D^p\Theta=HD\Theta+2C_pz\Theta.
\tag{15}
$$
这里完全避免了从 $\sigma\cdot U=0$ 约去 $\sigma$。

再置
$$
\Psi=y\sigma^4
=\frac{\sigma^2D\Theta-\Theta D(\sigma^2)}2.
\tag{16}
$$
对(16)使用(15)及 $D^pD=DD^p$。求导产生的两项
$2C_p\sigma^2\Theta$ 准确相消，故
$$
D^p\Psi=HD\Psi+4C_pz\Psi.
\tag{17}
$$
(4)中的全部截面分别准确为
$$
\sigma^mx^a=(\sigma^2)^{m/2-a}\Theta^a,
$$
$$
\sigma^myx^a=(\sigma^2)^{m/2-a-2}\Theta^a\Psi.
\tag{18}
$$
所示指数均非负；$m=2$ 时第二类为空。利用 $D^p$ 的乘积规则和各因子的实际 degree，(15)、(17)给主结论。

**定理1（全格的通用递推）。** 对任意正偶数 $m$ 和原整截面
$R\in\mathscr V_m$，
$$
\boxed{
D^pA_R=H_pDA_R+m(L_2H_p)zA_R
\quad\text{于 }\mathscr H_{\bar A}.
}
\tag{19}
$$
特别若 $j_{m,k}(R)=D^kA_R(0)$、$j_{m,-1}=0$，则对所有 $k\ge0$，
$$
\boxed{
j_{m,p+k}
\equiv H_pj_{m,k+1}
+m(L_2H_p)\,k\,j_{m,k-1}\pmod p.
}
\tag{20}
$$
这是 whole 格上的线性行恒等式，保奇基、任意实际参数系数及全部高 jet；不是仅比较 CM 纤维的一个数。

## 4. 原超奇异纤维的完整块

现在回原 $p=6s-1>211$、$g_2=0,g_3=-4b$，其中 $b$ 为原单位。
R855(37)逐多项式计算给
$$
H_p=0,\qquad L_2H_p=c_p
=\binom{3s-1}{2s-1}b^s\ne0
\quad\bmod p.
\tag{21}
$$
所以(19)准确变为
$$
D^pA_R=m c_p z A_R.
\tag{22}
$$
由于 $D^pz=0$，重复应用同一个导子 $D^p$ 得
$$
D^{rp}A_R=(m c_p)^r z^r A_R.
\tag{23}
$$
故若 $0\le r,k<p$，
$$
\boxed{
j_{m,rp+k}\equiv
\begin{cases}
(m c_p)^r(k)_r\,j_{m,k-r},&k\ge r,\\
0,&k<r,
\end{cases}
\pmod p,
}
\tag{24}
$$
其中 $(k)_r=k(k-1)\cdots(k-r+1)$。
再由除幂环中的 $z^p=0$，得到
$$
\boxed{D^{p^2}A_R=0,\qquad j_{m,n}\equiv0\pmod p\quad(n\ge p^2).}
\tag{25}
$$
(24)–(25)只控制实际 Hurwitz 系数模 $p$，不把所有普通 Taylor 系数认作整数。

对原四个 $A_\nu=z^6+\cdots$，$j_6=6!$，所以还有准确的较晚单位行
$$
j_{m_\nu,p+7}(R_\nu)\equiv7!\,m_\nu c_p\ne0\pmod p,
$$
$$
p[z^{p+7}]A_\nu\equiv-m_\nu c_p\pmod p.
\tag{26}
$$
后一式使用 $(p+7)!/p\equiv-7!$。它与原首 Gaussian 极完全同号，但不是目标 $[z^{p+1}]$ 非零；不能用这条较晚行替代 R821 的指定首行。

## 5. 四个实际首行在双变量环内已整除 $p$

对 $k=1$，(20)给通用行
$$
\boxed{j_{m,p+1}\equiv H_pj_{m,2}+m(L_2H_p)j_{m,0}\pmod p.}
\tag{27}
$$
R855 的 whole CM 格秩一合同正是它的原特化。

四个原 $R_\nu$ 的最大极阶为 $m_\nu-6$。只要保持这个原极阶的双变量代数提升，$A_\nu$ 就从 $z^6$ 起，因此
$$
j_{m_\nu,0}(R_\nu)=j_{m_\nu,2}(R_\nu)=0
$$
在特征零参数环中恒等成立。于是(27)不是仅在 CM 点整除，而是
$$
\boxed{
\frac1p\,j_{m_\nu,p+1}(\widetilde R_\nu)
\in\mathbf Z_{(p)}[g_2,g_3]
}
\tag{28}
$$
（保原固定分母），四个 $\nu=S,T,U,V$ 全部成立。

为精确说明齐次规范，令 $b=-g_3/4$，用 R821 的四个完整 $f_\nu(t)$ 定义
$$
\widetilde R_\nu
=b^{-1}x^{m_\nu/2}f_\nu(-b x^{-3}).
\tag{29}
$$
这里 $f_\nu(0)=0$，故 $b^{-1}$ 实际消掉；四式都是 $b,x$ 的多项式。
各项最低 $x$ 次数非负，最高极阶为 $m_\nu-6$，其首项系数为一。
在 $g_2=0,b=1$ 回到原同一 $R_\nu$，其它 $b$ 正是既有首 $z^6$ 归一的运输。

按权 $\operatorname{wt}(g_2,g_3,x,y)=(4,6,2,3)$，
(29)的权为 $m_\nu-6$。因此
$$
\mathcal B_{\nu,p}(g_2,g_3)
:=\frac1p\,j_{m_\nu,p+1}(\widetilde R_\nu)\bmod p
$$
是权 $p-5=6(s-1)$ 的真实双变量多项式，并且
$$
\boxed{
\mathfrak B_{m_\nu,p}(\bar R_{\nu,b})
=\mathcal B_{\nu,p}(0,-4b).
}
\tag{30}
$$
特别该值按 $b^{s-1}$ 缩放，与 R855 的原齐次运输一致。
本篇只对指定提升(29)使用这个多项式；没有把任意横向改动视为同一个全参数对象。

## 6. 当前首行仍须保留的除 $p$ 信息

(28)允许对这四个原输入先在完整参数多项式上作整除，再特化。
这比只在准确中心零格的 CM 点整除更强；但计算仍需要模 $p^2$ 的实际特征零 jet。
(19)–(27)只给模 $p$ 的恒等零，不能恢复商 $\mathcal B_{\nu,p}$。

R855 的完整双变量热递推、共同 $A_{24}$ 的六 sigma 初始资料、
四个 $H_{10},H_{48},H_{112},H_{42}$ 及反对角配对仍须保留。
原四中央同时为零仍迫
$$
\mathcal B_{S,p}(0,-4)
=\mathcal B_{T,p}(0,-4)
=\mathcal B_{U,p}(0,-4)
=\mathcal B_{V,p}(0,-4)=0;
\tag{31}
$$
本篇没有证明(31)不相容，也没有用全格的(25)或较晚单位(26)替代这一判定。

本篇是同一整形式来源上的证明，无新数学数值运行、素数扫描或可重算输出。

### 依赖与原文

- [R855 全热连接、整格与原 Hasse 横向项](R855-original-full-heat-connection-and-canonical-divided-jet.md)，尤其(22)–(23)、(35)–(38)及原四来源。
- [R821 四个完整原角多项式](R821-original-four-central-axes-and-complete-four-block-carries.md)、[R853 同源 Cartier 首行](R853-original-weighted-cartier-return-and-fixed-logarithmic-line.md)。原固定坏集、通常完整 Selmer 桥及全部 Newton 尾不变。
- J. C. Eilbeck, M. England, Y. Ônishi, *Some new addition formulae for Weierstrass elliptic functions*, Proc. R. Soc. A 470 (2014), 20140051，[出版全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4197466/)，(1.1)–(1.4)。本篇仅调用准确的 addition 身份(1.2)，并在(8)–(18)自行支付通用整平移、模 $p$ 与 whole 格的所有步骤。
