# 全 tame 单 Euler、真实 Cartier 首项与固定原函数连接

日期：2026-11-12。状态：本文的分布、Cartier、首坏系数与固定连接均已证明。
尚未把中心 Mellin 斜率的消失化成该固定连接的额外整性，更未证明无穷素数有限性。

固定 R51 的实际截面 \(A=A_{17}\)，令
\[
\mathscr A(t)=A(\log_Et),\qquad
A(z)=z^4+\cdots,\qquad h_m=A^{(m)}(0).
\]
对普通目标素数 \(p\ge13,\ p\ne17\)，写
\[
\pi=\psi(\mathfrak p),\quad b=\bar\pi,\quad
a=\pi/b=p/b^2,\quad c=b^{-1},\quad
\mathcal O=\widehat{\mathbb Z_p^{\rm ur}}.
\]
实际整 Amice 测度为 \(\nu\)，其变换是
\(A(\Omega\log(1+Z))\)，\(\Omega\in\mathcal O^\times\)。
已有的 principal 分布只作用于 \(\nu^{(0)}\)；
下面先证明真正的 full 版本，再用它求 Cartier。

## 1. 全部 tame 分支的平方比较

对 \(0\le j<p-1\)，定义
\[
\nu^{(j)}=\frac1{p-1}\sum_{\epsilon\in\mu_{p-1}}
 \epsilon^{-j}[\epsilon]_*\nu.
\tag{1}
\]
其第 \(m\) 矩仅在 \(m\equiv j\pmod{p-1}\) 时保留。
因为 \(A(iz)=A(z)\)，有 \([i]_*\nu=\nu\)，所以
\(\nu^{(j)}=0\)，除非 \(4\mid j\)。

Katz 的输入必须取**全 ray 测度**。Agboola–Howard 2006
Theorem 2.1.1（作者稿 PDF 第 12 页）对导子整除 \(fp^\infty\)、
无穷型 \((k,l)\) 满足 \(0\le-l<k\) 的角色插值。
这里每个
\[
\epsilon_m=\psi^{m+1}\bar\psi^{-m},\qquad m\ge0,
\]
均满足其范围。对 \(m=j+(p-1)n\)、\(4\mid j\)，有限导子和
R46 的固定有限 Schwartz 向量没有改变。
不能只使用已经投到 principal 分量的 Katz 函数。

具体地，若 \(x=\psi_{\mathfrak p}\)、\(y=\psi_{\bar{\mathfrak p}}\)，
用全 Katz 测度定义第 \(j\) 条解析分支
\[
\mathcal F_j(s)=\int x(x/y)^j\langle x/y\rangle^s\,d\mu_{\mathfrak p}.
\tag{2}
\]
同一 theta 插值规范给，在 \(s=m-j\in(p-1)\mathbb Z_{\ge0}\) 时，
\[
\mathcal F_j(m-j)
 =57800f\Omega\,
 136^j\langle136\rangle^{m-j}
 (1-ca^m)^2M_m^2,\qquad M_m=\int x^m\,d\nu.
\tag{3}
\]
这里 \(136^j\) **包括** \(\omega_p(136)^j\)，没有漏掉非 principal 的
有限角色常数。因 \(4\mid m\)，R51 规范中可能写成 \(136i\) 的同一
因子也恰为 \(136^m\)。

置
\[
G_j(s)=\int_{\mathbb Z_p^\times}x^j\langle x\rangle^s\,d\nu.
\]
R46 §4 的密权极限在这里原样适用：令
\(m=m_0+(p-1)p^n\)，非单位矩和 Euler 修正都趋于零；
周期、有限角色及 \(136^j\) 保持同一规范。再用解析恒等定理，得
\[
\mathcal F_j(s)
 =57800f\Omega\,136^j\langle136\rangle^sG_j(s)^2.
\tag{4}
\]
将 (4) 回代 (3)，得到**所有**正整数 \(m\equiv j\pmod{p-1}\) 的
准确平方式
\[
\left(\int_{\mathbb Z_p^\times}x^m\,d\nu\right)^2
 =(1-ca^m)^2M_m^2.
\tag{5}
\]
对于 \(j>0\)，其中包括 \(m=j\)，并非遗漏一个新的零次矩。

## 2. 去掉各分支的原点，再合成 full 分布

\(j=0\) 已由
[principal 分布笔记](2026-11-12-theta-principal-tame-euler-distribution.md)
证明。现在取 \(0<j<p-1,\ 4\mid j\)，令
\[
\alpha_j=x^j\nu^{(j)},\quad
\mu_j=\alpha_j|_{\mathbb Z_p^\times},\quad
d_j=ca^j,\quad
\delta_j=\alpha_j-d_j[a]_*\alpha_j.
\tag{6}
\]
\(\alpha_j,\mu_j,\delta_j\) 都 tame 不变。由 (5)，它们所有非负整数矩
满足 \(\mu_j*\mu_j=\delta_j*\delta_j\)，这里 \(*\) 是乘法卷积。

使用前引笔记 §3 的环带变换
\[
\mathscr R(\alpha)=\sum_{k\ge0}\mathscr L_k(\alpha)(T)X^k
 \in\mathbb C_p[[T]][[X]].
\]
其目标为整域，核恰为 \(\mathbb C_p\delta_0\)。
若 \(\mu_j\ne0\)，单位环带上的
\(\delta_j|_{\mathbb Z_p^\times}=\mu_j\) 固定正号；
若 \(\mu_j=0\)，整域直接给 \(\mathscr R(\delta_j)=0\)。
两种情形均有
\[
\delta_j-\mu_j=\gamma_j\delta_0.
\]
此处用 \(j>0\) 排除原点，而非假定原点没有质量。
对 \(N\to\infty\)，
\[
\alpha_j({\bf1}_{p^N\mathbb Z_p})=O(p^{Nj}),\qquad
d_j[a]_*\alpha_j({\bf1}_{p^N\mathbb Z_p})=O(p^{Nj}).
\]
\(\mu_j\) 在这些小球上为零，故 \(\gamma_j=0\)。
于是
\[
x^j\left(\nu^{(j)}|_{p\mathbb Z_p}
              -c[a]_*\nu^{(j)}\right)=0.
\]
在每个非零环带上除去 \(x^j\)，差只可能支撑于原点。
但它有非平凡 tame 特征，而 \(\delta_0\) 为平凡特征，因此差为零。
加总所有 \(j\)，得到
\[
\boxed{\nu|_{p\mathbb Z_p}=c[a]_*\nu.}
\tag{7}
\]
特别地，**不作 tame 平均**也有
\[
\boxed{\int_{\mathbb Z_p^\times}x^m\,d\nu
 =(1-ca^m)\Omega^m h_m\qquad(m\ge0).}
\tag{8}
\]
\(m\not\equiv0\pmod4\) 时两边本来均为零。
这不是对各个数值平方逐个挑选符号。

### 四阶自参考的准确中心

令 \(B=A^{(4)}\)，其测度为 \(\Omega^{-4}x^4\nu\)。
(8) 给
\[
\boxed{J_B(0)=24(1-ca^4)=24\left(1-\frac{\pi^4}{b^5}\right).}
\tag{9}
\]
对 \(m>0,\ p-1\mid m\)，
\[
\frac{J_A(T_m)}{J_B(T_m)}
 =\frac{1-ca^m}{1-ca^{m+4}}\frac{h_m}{h_{m+4}}
 \in\mathbb Q_p.
\tag{10}
\]
这加强了 R60 附录的有理近似；原来的近似下降证明独立有效。
它没有把 Mellin 商认作函数商的 Mellin 变换。

## 3. 真实 Cartier 公式

以下在剩余域 \(k=\overline{\mathbb F}_p\) 中计算。
令
\[
\beta:\widehat{\mathbb G}_m\longrightarrow\widehat E,\qquad
\beta^*\omega_E=\Omega\,\frac{dZ}{1+Z}
\]
为实际整正式同构的约化，\(\sigma\) 表示系数的 \(p\) 次 Frobenius。
CM Frobenius 为 \([\pi]\)，故
\[
\beta^\sigma(Z^p)
 =[\pi]\beta(Z)
 =\beta([b^{-1}](Z^p)).
\]
由此
\[
\beta^\sigma=\beta\circ[b^{-1}],\quad
\beta^{\sigma^{-1}}=\beta\circ[b],\quad
\Omega^{\sigma^{-1}}=b\Omega.
\tag{11}
\]
最后两式里的 \([b]\) 是正式群的 \(\mathbb Z_p\) 作用；
不能只用 \(b\bmod p\) 替代整个幂级数。

对有界测度的 Amice 变换 \(F(Z)\)，Cartier 作用于
\(F(Z)dZ/(1+Z)\) 时，先取 \(p\mathbb Z_p\) 部分再把支撑除以 \(p\)，
最后对系数施 \(\sigma^{-1}\)。
此式可先对整数 Dirac 测度验证，再按有限阶 Mahler 系数逼近得到。

由 (7)，除以 \(p\) 后的测度为 \(c[a/p]_*\nu\)，其中 \(a/p=b^{-2}\)。
对 \(\mathscr A(t)\omega_E\) 应用该公式与 (11)，得到
\[
\begin{aligned}
\beta^*\mathcal C(\mathscr A(t)\omega_E)
 &=\Omega^{\sigma^{-1}}c\,
    \mathscr A\!\left(\beta^{\sigma^{-1}}([b^{-2}]Z)\right)
    \frac{dZ}{1+Z}\\
 &=\Omega\,\mathscr A([b^{-1}]\beta(Z))\frac{dZ}{1+Z}.
\end{aligned}
\]
\(\mathscr A,\omega_E\) 的系数均在 \(\mathbb F_p\) 中。
因此
\[
\boxed{\mathcal C(\mathscr A(t)\omega_E)
       =\mathscr A([b^{-1}]t)\omega_E.}
\tag{12}
\]
它既不是零，也不是只比较在原点的一个系数。

## 4. 固定原函数在普通处的第一个非整系数

令
\[
Y(z)=\int_0^z A(w)\,dw,\qquad
\mathscr Y(t)=Y(\log_Et)=\int_0^t\mathscr A(s)\omega_E(s)
 =\sum_{n\ge1}y_nt^n.
\tag{13}
\]
复函数 \(Y\) 为 order 至多 \(2\) 的整函数；
\(t\)-级数在每个普通正式圆盘上收敛，因为积分只多除以 \(n\)。

写
\(\mathscr A(t)\omega_E=\sum_{n\ge0}c_nt^n\,dt\)，
则 \(c_n\in\mathbb Z_p\)，\(y_n=c_{n-1}/n\)。
右边 (12) 从 \(b^{-4}t^4dt\) 开始，所以
\[
c_{kp-1}\equiv0\pmod p\quad(1\le k\le4),\qquad
c_{5p-1}\equiv b^{-4}\not\equiv0\pmod p.
\]
由于 \(p^2>5p\)，得到真实的首坏位置
\[
\boxed{y_n\in\mathbb Z_p\ (n<5p),\qquad v_p(y_{5p})=-1.}
\tag{14}
\]
这是正式 \(t\) 坐标中的结论，不是从 Hurwitz 系数直接猜测。

进一步，固定图像系数的归一化 Gauss 半径恰为
\[
\boxed{\rho_p=p^{-1/(5p-1)}.}
\tag{15}
\]
这里半径的定义是最大的 \(0<\rho\le1\)，使
\(|y_n|_p\rho^{n-1}\le1\) 对每个 \(n\) 成立。
下界用 \(v_p(y_n)\ge-v_p(n)\)：
\(v_p(n)=1\) 的首个可能非整项为 \(5p\)；
\(v_p(n)=r\ge2\) 时
\[
\frac r{n-1}\le\frac r{p^r-1}
\le\frac2{p^2-1}<\frac1{5p-1}\qquad(p\ge13).
\]
上界由 (14) 达到。
(15) 是这一固定坐标图像的系数估计，
没有断言它就是允许全部代数坐标变换后的最优评价映射范数。

全测度关系还给准确的原函数迹式：
\[
\boxed{\sum_{Q\in E[\pi]}\mathscr Y(P+Q)
       =b\,\mathscr Y([a]P).}
\tag{16}
\]
微分后两边由 (7) 的正式群迹式相等。
常数为零：\(\mathscr Y([i]P)=i\mathscr Y(P)\)，
\(E[\pi]\) 在 \([i]\) 下稳定，所以 \(\sum_Q\mathscr Y(Q)=0\)。

注意 \(z^{-1}Y(z)\) 的 Hurwitz 系数为 \(h_m/(m+1)\)，而
\(Y(z)\) 自身的 Hurwitz 系数为 \(h_m\)（索引移动一位）。
两者不能混同。单凭 \(h_{5p-1}\) 为单位也不能推出 (14)；
后者真正使用了 full (7)。

## 5. 除去 theta 参考后，得到固定代数连接

这里无需另选依赖 \(p\) 的参考。使用 R57 的固定四次模型坐标
\[
u=x^{-1/2},\qquad v=u'=\sqrt{1-17u^4},\qquad
L=\frac{\vartheta'}{\vartheta}.
\]
\(v^2=1-17u^4\) 定义一条固定椭圆曲线 \(\mathcal C\)，
它经
\[
(u,v)\longmapsto (x,y)=(u^{-2},-v/u^3)
\]
二比一映到 \(E_{17}\)。所以本节没有把 \(u\) 错认作
\(E_{17}\) 上的有理函数。取点 \((u,v)=(0,1)\) 及 \(L(0)=0\)。

准确多项式流和实际截面为
\[
u'=v,\qquad v'=-34u^3,\qquad L'=17u^2,
\]
\[
A(z)=\vartheta(z)^{17}Q(u(z)),\qquad
Q(u)=u^4+\frac{51}{5}u^8-\frac{289}{5}u^{12}
             +\frac{4913}{5}u^{16}.
\tag{17}
\]
令
\[
Z(z)=\frac{Y(z)}{\vartheta(z)^{17}},\qquad Z(0)=0.
\]
那么
\[
\boxed{Z'+17LZ=Q(u).}
\tag{18}
\]
这是固定曲面 \(\mathcal C\times\mathbb A^1_L\) 上沿上述向量场的
一个一阶非齐次线性连接；所有系数属于 \(\mathbb Q\)。
它确实保留了原截面，而不是换成一个仅有相似首项的模型。

### 该原函数没有被有理化

设 \(F=\mathbb C(\mathcal C)\)，导子记为 \(\delta=d/dz\)。
先说明 \(\delta L=17u^2\) 没有代数原函数。
因为
\[
\delta(v/u)=-17u^2-u^{-2},
\]
若 \(17u^2\) 有代数原函数，取有限扩域的迹可先得到 \(F\) 中的原函数；
再沿 \(\mathcal C\to E\) 取迹，便会使 \(x\,\omega_E\) 在 \(E\) 上恰当。
但 \(x\,\omega_E\) 只有 \(O\) 处一个二阶极点，
其有理原函数必须只有 \(O\) 处一个一阶极点；
椭圆曲线的 \(\ell(O)=1\) 排除这一点。
故 \(L\) 在 \(F\) 上超越。

现在若 \(Z\) 在 \(F(L)\) 上代数，取迹并除以扩域次数，
会得到 (18) 的一个有理解 \(R\in F(L)\)。
任何有限 \(L\)-极点的不可约分母 \(P(L)\) 必须满足
\(P\mid\delta P\)，否则 \(\delta R\) 的最高极点阶不能被 \(17LR\) 消掉。
对 \(P\) 的代数根 \(\beta\) 评价，该条件给
\(\delta\beta=17u^2\)，与前段矛盾。
所以 \(R\) 必为 \(L\) 的多项式。
其最高项在 \(17LR\) 中次数增加一，而 \(\delta R\) 不增加 \(L\) 次数；
非零的 \(Q(u)\) 因而也不可能等于 \(\delta R+17LR\)。
综上，
\[
\boxed{Z\text{ 在 }\mathbb C(\mathcal C)(L)\text{ 上超越}.}
\tag{19}
\]
因此 \((u,v,L,Z)\) 的解析曲线在
\(\mathcal C\times\mathbb A^2\) 中 Zariski 稠密。
\(u,v,L,Z\) 都是复平面上阶至多 \(2\) 的亚纯函数；
(18) 提供了一个具体固定连接，而非未知存在的几何对象。

## 6. 仍需建立的跨素数含义

(12)、(14) 和 (16) 对每个普通目标素数已经成立，
并不需要 \(J_p'(0)=0\)。特别地，真实首坏系数 (14) 在该反设下仍存在。
(18) 把原函数商放进固定的代数微分方程，
但尚未证明 Mellin 的附加对数矩消失会改善这个连接的任何整格。

所以当前不能把
“对几乎所有普通 \(p\)，\(J_p'(0)=0\)”
直接改写成连接的 \(p\)-曲率处处为零。
首先必须给出一个含该附加对数矩的、确切的 Frobenius 或评价映射条件。
这是后续研究的具体接口。

一手外源：A. Agboola–B. Howard（附 K. Rubin），
*Anticyclotomic Iwasawa theory of CM elliptic curves*，
Ann. Inst. Fourier **56** (2006), 1001–1048，
Theorem 2.1.1 及其前后的全 ray Galois 角色定义，
[作者全文](https://web.math.ucsb.edu/~agboola/papers/cm1-final.pdf)。
原文允许全部所用 tame 分支；(1)–(19) 的其余新推导在本文完整给出。
