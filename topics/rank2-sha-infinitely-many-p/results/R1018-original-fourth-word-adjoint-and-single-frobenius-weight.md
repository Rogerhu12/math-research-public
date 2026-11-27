# R1018 — 原线性深度的单 Frobenius 权、第四阶全字伴随与真实质量差

日期：2026-11-27 UTC。**已证明。** 本篇保持 R1016 的同一个特征零
平坦权及完整 Tate 精度。通过一个明确的精度选择，它在模 $p$ 后
对全部充分大的目标惰性素数都是一个真实 $p$ 次权。
一般参数下的余带也满足一个准确二阶方程；它的第四阶运输只用
两个指定权，不产生自由的余带系数。

随后把 R1015 的实际标准来源 $q=\sigma^{10}(X+1)$ 的第四阶连接
逐字转回原来源。其第二个完整分量是质量一的
$\Psi_{27462500}$，绝对系数也全部确定。原有限 $P_{10}$ 的曲率
在整个第一 Cartier 中保留为四项 concomitant；其原中央 diagonal 贡献准确
从第六块开始，完整非 diagonal 末四个余数的补项也保留。最后给出这些真实第四阶测试在同时坏假设下必须
承担的非零 old 对数。没有将连接、字或加权来源免费赋中央零。

## 1. 原输入与一个可主动选择的线性精度

保持
$$
E:y^2=x^3+1,\quad X=x^3,\quad
\delta^2=-3,\quad \omega=(-1+\delta)/2,\quad
\pi=(7+\delta)/2,\quad \bar\pi=(7-\delta)/2.
\tag{1}
$$
令 $D=d/dz$，$\omega_E=dx/(2y)=dz$。
所有本篇的素数满足
$$
p=6s-1>13^4,\qquad d=p+1.
$$
固定
$$
\boxed{H=6\left\lfloor\frac{s-5}{6}\right\rfloor+5,\qquad N=Hd.}
\tag{2}
$$
因此 $H\le s$、$H\ge s-5$、$H\equiv5\pmod6$。

R1016 的全部证明实际上只使用 $H\le s$：
其单一整 trace、增长极帽、统一 Hurwitz 界以及无限 Newton 尾的
最后估计均在这个范围成立。原先的 $H\le L_p$ 仅用于选定 old
对数的检出深度，不是这些证明的必要限制。因此对 (2)，仍有
$$
\boxed{
j_f-j_{10,h_{N,\pi}(f)}-m_0(f)\log_pq_\pi
\in p^{H+1}\mathcal O,\qquad
q_\pi=\pi^d/13.
}
\tag{3}
$$
这里 $h_{N,\pi}$ 仍是 R1016 的原特征零输入，原全部低项高精度
也在同一个函数内。没有换成某个仅模 $p$ 相等的函数。

更明确地，R1000 的真实上界
$$
L_p=\left\lfloor
\frac{(p+1)\log13/2+\log(2/\sqrt3)}{\log p}
\right\rfloor
$$
在 $p>13^4$ 时小于 $(p+1)/8+1$；而
$H\ge(p+1)/6-5>(p+1)/8+1$。故
$$
\boxed{H\ge L_p.}
\tag{4}
$$
所有目标 old 对数都在这次线性深度内检出。

## 2. 同一个原权的准确导数与余带二阶方程

记
$$
v=\frac{R_\pi(X)}{(X+1)^2},\qquad
R_\pi=X^2+(2+6\delta)X+(40+24\delta)/13,
\quad \xi=v-1,
$$
$$
B_{a,k}(T)=\sum_{j=0}^k(-1)^j\binom{a+j-1}{j}(T-1)^j.
$$
以下先允许任意 $1\le H\le s$，置
$$
a=H(p+1)+1,\quad k=Hs=qp+t,\quad
q=\lfloor H/6\rfloor,\quad0\le t<p,
\qquad V=v^aB_{a,k}(v).
\tag{5}
$$
这正是 R1016 的特征零 $V_{N,\pi}$。

### 2.1 导数是一个指定乘积

逐项微分有限和，相邻项相消，完整地得到
$$
\boxed{
\frac{d}{dv}\bigl(v^aB_{a,k}(v)\bigr)
=(-1)^k a\binom{a+k}{k}v^{a-1}(v-1)^k.
}
\tag{6}
$$
证明也可比较左右两边：左边在 $v=1$ 恰有至少 $k$ 阶零，
在 $v=0$ 至少有 $a-1$ 阶零，次数至多 $a+k-1$；
最高项给 (6) 的显示常数。这是整个多项式身份。

沿 R1016 §9，令
$$
S_q(\xi)=\sum_{j=0}^q(-1)^j\binom{H+j-1}{j}\xi^j,\qquad
C=\binom{H+q}{q},
$$
$$
G_0=v^HS_q(\xi),\quad G_1=v^H\xi^q,
$$
$$
B=\xi^{t+1}E_{H,k}(\xi),\qquad
E_{H,k}=(-1)^kC\sum_{\ell=0}^H
\binom{k+\ell}{\ell}(1+\xi)^\ell.
\tag{7}
$$
全部约化在原剩余域中进行，准确有
$$
\boxed{\bar V=G_0^p+G_1^pB.}
\tag{8}
$$

若 $t+H+1<p$，定义非零常数
$$
\kappa=(-1)^k(H+1)C\binom{H+t+1}{t}\in\mathbf F_p^\times.
$$
将 (6) 与 (8) 微分并使用 $k=qp+t$，得到
$$
\boxed{
B'(\xi)=\kappa(1+\xi)^H\xi^t,\qquad
\xi(1+\xi)B''-[t+(H+t)\xi]B'=0.
}
\tag{9}
$$
所有二项式顶数均小于 $p$，故这里的 $\kappa$ 确为单位。
(9) 没有把 $B$ 的 $H+1$ 个已定系数改成自由变量。

若 $t+H+1\ge p$，Lucas 恒等式使 (6) 的常数约化为零，
R1016 的整个身份则是
$$
\boxed{\bar V=W_{H,+}^p,\qquad
W_{H,+}=v^{H+1}B_{H+1,q}(v).}
\tag{10}
$$
这不表示原特征零 $V$ 等于 $W_{H,+}^p$。

### 2.2 对 (2) 的所有目标素数，准确进入 (10)

写 $H=6q+5$，则 $t=q+5s$，并且
$$
t+H+1-p=7q-s+7\ge(s-28)/6\ge0.
$$
所以本篇实际选择 (2) 对全部目标素数满足 (10)，不依赖素数扫描
或一个未证的剩余类密度。还准确有
$$
W_{H,+}=1+O(z^{H+1})\quad\hbox{at }O,\qquad
\operatorname{ord}_T W_{H,+}\ge H+1
\quad(0\ne T\in E[\pi]).
\tag{11}
$$
这里 $6(q+1)=H+1$。这一个权同时适用于全部原长窗口。

### 2.3 一般余带的第四阶只用 B 与 DB

在十三 cover 上用归一导数
$\mathfrak d=\pi^{-1}D_{\rm up}$，它在目标函数上就是 $D$。
在 (9) 的情形置
$$
Y=\mathfrak dB,\qquad
J=\frac{\mathfrak d^2\xi}{\mathfrak d\xi}
+\left(\frac H{1+\xi}+\frac t\xi\right)\mathfrak d\xi.
$$
完整地有
$$
\mathfrak dB=Y,\qquad \mathfrak dY=JY.
\tag{12}
$$
对任一实际有理 $R$，令 $a_n=(\mathfrak d+R)^n1$。
乘积法则逐次给
$$
\begin{aligned}
(\mathfrak d+R)^4B={}&a_4B\\
&+\{4a_3+6Ja_2+4(\mathfrak dJ+J^2)a_1
+\mathfrak d^2J+3J\mathfrak dJ+J^3\}Y.
\end{aligned}
\tag{13}
$$
其中
$$
\begin{aligned}
a_1&=R,\\
a_2&=\mathfrak dR+R^2,\\
a_3&=\mathfrak d^2R+3R\mathfrak dR+R^3,\\
a_4&=\mathfrak d^3R+4R\mathfrak d^2R
+3(\mathfrak dR)^2+6R^2\mathfrak dR+R^4.
\end{aligned}
\tag{14}
$$
$J$ 的显示分母只是使用乘积法则的记法；(12)–(13) 的原完整
乘积在这些点的零极由 (9) 保证。这里没有反演一个未知的目标
$P_{10}$、曲率或中央值。对实际选择 (2)，直接使用 (10)，不需
引入 $Y$。

## 3. 实际第四阶方向和两条明确 old 标准来源

令
$$
q=\sigma^{10}Q,\quad Q=X+1,\qquad
\Psi=\sigma^{10}x^2(X-8),\qquad
\Psi_{00}=\sigma^{10}x^2(X+10).
$$
这是 R1015 的 $q$ 和 R978 的两条原标准来源。
由于 $Dx=2y$、$Dy=3x^2$，
$$
DQ=6x^2y,\quad
D^2Q=42x^4+24x,\quad
D^3Q=48y(7X+1),
$$
$$
\boxed{
D^4Q=432x^2(7X+5)
=24\{65x^2(X-8)+61x^2(X+10)\}.
}
\tag{15}
$$
故对原连接 $\nabla_{10}=D-10\sigma'/\sigma$，
$$
\boxed{\nabla_{10}^4q=24(65\Psi+61\Psi_{00}).}
\tag{16}
$$
它是协变第四阶，不是普通 $D^4q$。例如 (16) 的质量为3024，
而普通 $D^4q$ 的质量为24；两者的连接补偿不能省略。

## 4. 全部十三 lift、有限 profile 与第四阶的绝对系数

沿 R1015，$T_{iv}$ 为原 degree130 Heisenberg lift，
$B_0=\pi v\in E[\bar\pi]\setminus O$，并固定
$$
r(P)=\frac{X+1}{x^2(X-8)}=\frac1{4x(P)x(2P)},\qquad
r_B=r(B_0),\qquad r_B^3=(5+3\delta)/2048.
$$
仍用原字符 $\chi_j(2)=\zeta_{12}^j$、$\zeta_{12}^4=\omega^2$；
$\varepsilon=\chi_6$。原来源满足
$$
\mathcal P_i\Phi_*=c_*\varepsilon(i)T_{iv}D_\pi\Psi,\qquad
\mathcal P_i\Phi_{260}=c_{260}\chi_{10}(i)T_{iv}D_\pi q,
\quad i\ne0,
\tag{17}
$$
两条第零字均为零。原绝对规范为
$$
c_*=3\omega^2\nu_\pi,\qquad
c_{260}=\rho_\pi c_*/r_B,\qquad
\rho_\pi=-11(1+\delta)/40.
\tag{18}
$$
证明第一式的质量规范：
R987 的 $t=\omega\bar\pi=-1+2\delta$ 给
$$
m_0(T_{iv}D_\pi\Psi)=(t-1)/12=\omega/3
$$
对全部 $i\ne0$ 相同，再用 R1015 的实际字质量
$\varepsilon(i)\nu_\pi$。第二式由完整比例
$r(iB_0)=\chi_8(i)r_B$ 得到。

定义整个原 theta 比值
$$
L_i(z)=
e^{-130\eta(iv)(z+iv/2)}
\frac{\sigma(\pi z+iB_0)^{10}}{\sigma(z)^{130}},
\qquad
A_i=\pi^{-1}\{\nabla_{130}-D\log L_i\}.
\tag{19}
$$
直接微分原 lift，得到
$$
A_i^4T_{iv}D_\pi q=T_{iv}D_\pi\nabla_{10}^4q.
\tag{20}
$$
$\pi^{-4}$ 已完整包含于 $A_i^4$；之后的标准目标导数是 $D^4$，
不应再添一个 $\pi^4$。

令
$$
\mathcal O_\pi=\sum_{i=1}^{12}\chi_8(i)A_i^4\mathcal P_i\Phi_{260}.
$$
因为 $\chi_8\chi_{10}=\chi_6$，(16)–(18) 给
$$
\mathcal O_\pi=\frac{24\rho_\pi}{r_B}
\{65\Phi_*+61c_*V\},\qquad
V=\sum_{i=1}^{12}\varepsilon(i)T_{iv}D_\pi\Psi_{00}.
\tag{21}
$$

### 4.1 第二完整分量的质量和有限类型

原两个标准来源的实际二、五类型与十三 $\chi_6$ profile 表明，
$V$ 属于 R973 的完整一维类型 $(1,2,0)$。
对应固定曲线参数为27462500；记其质量一的原向量为
$\Psi_{27462500}$。这使用全部原有限因素，不根据两处好位猜标签。

令 $X_B=X(B_0)$、$X'_B=X(2B_0)$。R1015 已付
$$
N_{\bar\pi}(X-8)=216(5-3\delta)/13.
$$
同一个 lift 中两标准来源的质量比为
$(X(iB_0)+10)/(X(iB_0)-8)$。六个正、六个负项完整求和，得到
$$
m_0(V)
=-\frac{36\omega(X_B-X'_B)}{N_{\bar\pi}(X-8)}.
\tag{22}
$$
原 R987 根的取向给
$X_B-X'_B=-12\delta/\sqrt{\bar\pi}$。
这里 $B_0=\pi u_{\bar\pi}=7u_{\bar\pi}$ 交换两个平方轨道；
不能忽略这次交换的负号。
原 $\nu_\pi=g(3-\delta)\sqrt\pi/(332640\cdot13)$，
且既定两个根满足 $g=\sqrt\pi\sqrt{\bar\pi}$。
逐代入 (22) 得
$$
\boxed{c_*m_0(V)=\omega/18480.}
\tag{23}
$$
例如化简中只用
$\delta(3-\delta)\pi=6(1+2\delta)$ 及
$(1+2\delta)/(5-3\delta)=\omega/2$。
一维性和 (23) 遂给完整来源身份
$$
\boxed{
\mathcal O_\pi=
\frac{24\rho_\pi}{r_B}
\left\{65\Phi_*+\frac{61\omega}{18480}\Psi_{27462500}\right\}.
}
\tag{24}
$$
其质量准确为 $61\rho_\pi\omega/(770r_B)\ne0$。
共轭支保原 Weyl-dual 根和 lift 后，准确将 $\omega$ 换为
$\omega^2$，其余向量 $\Phi_*,\Psi_{27462500}$ 不变。
没有为 (24) 的任何一项增加中央零假设。

## 5. 两 gauge 进入完整字时必须保的卷积

使用 R1012 的原 Kummer 规范
$$
\kappa_{13}^{13}=[\pi]^*h,\qquad
\frac{R_f}{R_\pi^{10}}=\sum_{i=0}^{12}f_i\kappa_{13}^i,\qquad
G_a=\sum_{j=0}^{12}g_{a,j}\kappa_{13}^j,\qquad
B=\sum_{\ell=0}^{12}b_\ell\kappa_{13}^\ell.
$$
其中 $\kappa_{13}\sim\pi^{-1}z^{-1}$，
$h\sim z^{-13}$；不与 (9) 的常数 $\kappa$ 混淆。

对第一 gauge 取 $\ell=0,b_0=1$。
对第二 gauge 必须保全部 $\ell$，准确未平均 trace 是
$$
\boxed{
A_{N,\pi}(f)\bmod p
=13\pi^{-10}\!
\sum_{\substack{a,i,j,\ell\\i+pj+\ell\equiv0\ (13)}}
g_{a,j}^{\,p}b_\ell h^{e}f_i,\qquad
e=(i+pj+\ell)/13.
}
\tag{25}
$$
第一 gauge 的求和按上述 $\ell=0$ 约定。
在实际选择 (2) 时，只取 $G=W_{H,+}$ 的一个 gauge、
$\ell=0,b_0=1$。原13没有除掉。

不能把 $B$ 当成目标域函数，或将它越过 deck 投影。
式 (25) 正是完整 $b_\ell$ 卷积；指数 $e$ 也是实际整数。

对原 $R_i=-iB_0$ 及 Miller 函数
$$
\operatorname{div}h_i=(10-i)O+iS-10R_i,\qquad
Q_i(P)=h_i(P+R_i)f_i(P+R_i),
$$
令 $Z_i=Z(P+R_i)$、$P_i=P_{10}(P+R_i)$。
对 $0\le b<p$，将一项平移到其标准来源后，准确外权为
$$
\boxed{
\mathcal A_{a,i,j,\ell,b}(P)=
Z_i^{-b-1}\,
g_{a,j}(P+R_i)^p\,b_\ell(P+R_i)\,
\frac{h(P+R_i)^e}{h_i(P+R_i)}.
}
\tag{26}
$$
整个目标微分就是
$$
\eta_{N,b}
=13\pi^{-10}\sum
\tau_{-R_i}^*\bigl(P_i\mathcal A_{a,i,j,\ell,b}Q_i\omega_E\bigr).
\tag{27}
$$
所有 $h_i$、位移、$P_{10}$、$Z$ 和两端二挠权均仍在其中。
常数经过 Cartier 时使用真实的 $p$ 次根；
不能将 $13\pi^{-10}$ 在半线性运算后保持原样。

这与原上游尺度完全一致：
$$
[\pi]_*(\bar V\,\eta_{\pi,b})=\pi^b\eta_{N,b},\qquad
\pi^{b/p}\mathcal C\eta_{N,b}
=[\pi]_*\{G_0\mathcal C\eta_{\pi,b}
+G_1\mathcal C(B\eta_{\pi,b})\}.
\tag{28}
$$
实际单 gauge 时即取 (10)。式 (28) 保微分 pushforward 的全部
尺度，不以 $13^b$ 替换 $\pi^b$。

### 5.1 所有 j 依赖的连接准确消去

在未平移的目标坐标中，令
$$
\mathscr D_\ell=D+\frac{\ell}{13}D\log h,\qquad
R_{i,b}=10G+\frac i{13}D\log h-D\log h_i-\frac{b+1}{Z}.
\tag{29}
$$
因为 $13e=i+pj+\ell$，在特征 $p$ 中准确有
$e=(i+\ell)/13$。所以对每个 $n\ge0$，
$$
(D+10G)^n\!\left(
Z^{-b-1}g_{a,j}^pb_\ell h^e/h_i\right)
=g_{a,j}^p Z^{-b-1}h^e/h_i\,
(\mathscr D_\ell+R_{i,b})^n b_\ell .
\tag{30}
$$
平移后就是同一个公式。$j$ 只留在真实 $p$ 次权中。

进一步，
$\mathscr D_\ell b_\ell$ 是
$\mathfrak d B$ 的第 $\ell$ 个 Kummer 系数。
故 (13) 给 (30) 的完整第四阶双权返回，所有 Fourier 乘积都在
完整 cover 内进行后再取字。它没有把一个非 base 系数从投影内
提出。实际选择 (2) 中 $\ell=0,b_0=1$，只需 (14) 的四个
实际 $R_{i,b}$ 多项式，仍保全部原 Miller 项。

## 6. 原 P10 的完整第四阶伴随与曲率项

以下在原剩余函数域中工作，不把它与 CM 数域记号混同。
R887 的同一个 $D,Z,G$ 满足
$$
DZ=1,\qquad D^p=0,\qquad D^{p-1}G=r_0^p,\qquad
r_0=x^2/y,\quad \mathcal H=G+r_0.
$$
因此
$$
(D-10G)^p=-10\mathcal H^p,\qquad
P_{10}=-(D-10G)^{p-1}Z^{p+9},
$$
$$
\boxed{DP_{10}=10GP_{10}+10(\mathcal HZ)^pZ^9.}
\tag{31}
$$
原点 $\mathcal H=(3/5)Z^5+\cdots$。本篇从不除以 $\mathcal H$。

对第 $i$ 个标准位移，所有函数添下标 $i$，令
$\mathscr M_i=D+10G_i$。对任一实际有理权 $A$，
(31) 逐次微分给
$$
D^4(P_iA)=P_i\mathscr M_i^4A+
10(\mathcal H_iZ_i)^p
\sum_{j=0}^3D^{3-j}(Z_i^9\mathscr M_i^jA).
\tag{32}
$$
系数 $10(\mathcal H_iZ_i)^p$ 被 $D$ 杀掉，故没有遗漏其导数。

定义完整四项
$$
\boxed{
\mathscr B_i(A)=
\sum_{j=0}^3(-1)^{3-j}
Q^{(3-j)}Z_i^9\mathscr M_i^jA,
\qquad Q=X+1.
}
\tag{33}
$$
这里 $Q$ 在标准来源的点 $P$ 上，$Z_i,G_i$ 在 $P+R_i$ 上，
不能把二者的位移误相消。

Cartier 杀掉每个全导数；
对 $A,B$ 有
$\mathcal C(A\,DB\,\omega_E)=-\mathcal C(B\,DA\,\omega_E)$。
将 (32) 完整分部积分四次，得到全曲线微分身份
$$
\boxed{
\begin{aligned}
\mathcal C(P_iA\,D^4Q\,\omega_E)
={}&\mathcal C(P_iQ\,\mathscr M_i^4A\,\omega_E)\\
&+10\mathcal H_iZ_i\,
\mathcal C(\mathscr B_i(A)\omega_E).
\end{aligned}
}
\tag{34}
$$
它不是只有留数或主部的等式。
所有后续 Cartier 层、exact 项及原点系数都可以作用于同一等式。

对 (24) 的实际来源，R1015 的规范给
$$
Q_{i,260}=
C_iQ,\qquad
C_i=\frac{\pi^{10}\varepsilon(i)\rho_\pi\nu_\pi}
{X(iB_0)+1}.
$$
因此其第 $i$ 个第四阶字准确为
$\chi_8(i)C_iD^4Q$。
将 (34) 乘以这个真实常数，再代入 (26)–(27)，就是
$\mathcal O_\pi$ 的整个 first-Cartier 转置。
经过 Cartier 的 $\chi_8(i)C_i$ 同样取原 $p$ 次根。
没有用一个未登记的形式算子替换 $A_i^4$。

## 7. 原中央 diagonal 的第六块与全部非 diagonal 补项

本节适用于 (2) 的实际单 gauge；一般 (8) 的每个完整卷积项
也有相同上界。观察第 $i$ 个标准来源的原返回点
$P=-R_i=iB_0$，使用 $Z_i$ 作原参数。

$Q$ 及其前三导数在这个非零十三挠点正则。
原 Kummer Laurent 规范给
$$
\operatorname{ord}_O g_j\ge j,\quad
\operatorname{ord}_O b_\ell\ge\ell,\quad
h\sim Z^{-13},\quad h_i\sim Z^{10-i}.
$$
所以 (26) 的真实权满足
$$
\operatorname{pole}A\le b+11,\qquad
\operatorname{pole}\mathscr M_i^jA\le b+11+j.
$$
由 (33)，在完整范围 $0\le b<p$ 中有
$$
\boxed{\operatorname{pole}\mathscr B_i(A)\le b+5.}
\tag{35}
$$
因此其第一 Cartier 在该点至多有简单极；只有
$b\in\{p-4,p-3,p-2,p-1\}$ 才允许二阶极。
这四个非 diagonal 余数不能因 $H<p$ 而漏掉。

先看原中央的实际 diagonal
$n=h(p+1)=hp+h$、$1\le h\le H$。
此时 $b=h\le H\le s<p-5$，故第一 Cartier 至多简单极。
由 $\mathcal H_iZ_i=(3/5)Z_i^6+\cdots$，
$$
\boxed{
\operatorname{ord}_{-R_i}
\left(10\mathcal H_iZ_i
\mathcal C(\mathscr B_i(A)\omega_E)/\omega_E\right)\ge5.
}
\tag{36}
$$
所以对这些实际 $b$，原读者 $[Z_i^{r-1}]$ 的前五块 $r\le5$
不含曲率；第六块的完整贡献为
$$
\boxed{
6\,\operatorname{Res}_{-R_i}
(\mathscr B_i(A)\omega_E)^{1/p}.
}
\tag{37}
$$
这个正号来自 (34) 与 $10\cdot3/5$；
concomitant 内的分部积分负号已在 (33) 保留。

完整非 diagonal 也有显示公式。写
$$
\mathcal H_iZ_i=\sum_{n\ge1}h_nZ_i^{6n},\quad h_1=3/5,
\qquad
\mathcal C(\mathscr B_i(A)\omega_E)/\omega_E
=\sum_{m\ge-2}c_mZ_i^m.
$$
则任一后续块的整个曲率回项准确为
$$
\boxed{
10\sum_{\substack{n\ge1\\6n\le r+1}}
h_n\,c_{r-1-6n}.
}
\tag{38}
$$
$b\le p-5$ 时 $c_{-2}=0$，上限可以收紧为 $6n\le r$，
给真正的六块三角移位。末四个 $b$ 则必须保
$$
c_{-2}=
\left([Z_i^{-p-1}]
  (\mathscr B_i(A)\omega_E/\omega_E)\right)^{1/p}.
$$
其最早可能贡献是第五块的 $6c_{-2}$；
本篇不在完整 sigma／有限模型下三角返回之前删掉它。

所以 (36)–(37) 的六块结论准确用于原 diagonal 与所述低 $b$
条带；全部非 diagonal 按 (38) 保留。
$\mathscr M_i^jA$ 中的实际 $G_i$、Miller 系数和原
$Z^p$ 折回始终使用 (30)–(34)。

## 8. 换 profile 真实改变十三纤维的支撑

在 (2) 的单 gauge 中，字配对满足 $i=-pj\pmod{13}$。
因为 $p\equiv-1\pmod3$，有
$$
\chi_8(i)=\chi_8(p)\chi_8(j)
=\chi_8(p)\chi_4(j)^p.
\tag{39}
$$
所以把 (21) 的 $\chi_8$ 从 source 移到完整权上，准确将 $W$
换成
$$
\boxed{
\mathcal T_{\chi_4}W
=\sum_{j\ne0}\chi_4(j)\mathcal P_jW
=\frac{\tau(\chi_4)}{13}
\sum_{a\ne0}\chi_8(a)W(P+a u_\pi),
}
\tag{40}
$$
另保 (39) 的 $\chi_8(p)$。
这里 $\tau(\chi_4)=\sum_{j\ne0}\chi_4(j)\zeta^j$ 是原根下的
实际 Gauss 和；公式由完整13项 Fourier 和直接得到。
它在所有本篇好位都是单位，不另择相位。

(11) 逐纤维给
$$
\mathcal T_{\chi_4}W=O(z^{H+1})\quad\hbox{at }O,
$$
$$
\boxed{
(\mathcal T_{\chi_4}W)(b u_\pi+P(z))
=\frac{\tau(\chi_4)\chi_8(b)}{13}+O(z^{H+1})
\quad(b\ne0).
}
\tag{41}
$$
因此其 $p$ 次权在原 $O$ 的贡献严格高于整个 $N=H(p+1)$
窗口；其余12个纤维却有显示的非零常数。
第四阶换 profile 实际把读者移到这些真实 translated jets。
若把 (40) 用于第四阶运输，(19)、(32)–(34) 仍保留；
不能将其变成原 canonical 标量读者。

特别 (41) 明确排除了以下无效推理：
原 canonical 中央为零，并不使换 profile 后的十二纤维测试为零。
这也是 (24) 的质量一完整分量不能被省略的实际来源解释。

## 9. 两条真实 canonical 必要行和一个必须承担的非零对数

所有 $j$ 均为 R1016 的同一原 charge 归一，未另乘物理尺度。
令
$$
\alpha=61/18480,\qquad
U_\pi=\frac{r_B}{24\rho_\pi}\mathcal O_\pi
=65\Phi_*+\alpha\omega\Psi_{27462500}.
$$
共轭支准确为
$$
U_{\bar\pi}=65\Phi_*+\alpha\omega^2\Psi_{27462500}.
\tag{42}
$$
故整个特征零来源身份给
$$
\omega^2U_\pi-\omega U_{\bar\pi}
=65(\omega^2-\omega)\Phi_*=-65\delta\Phi_*.
\tag{43}
$$
这里没有假定 $\Psi_{27462500}$ 的导数为何值。

若原两 canonical 来源同时坏，则
$j_{\Phi_*}=j_{\Phi_{260}}=0$。
由 (3)，它们各自在两个实际 target 中的导数都属于
$p^{H+1}\mathcal O$；这仍只有原两条算术必要行，没有将四个
target 算成四条独立 canonical 零。

另一方面，(42) 的质量分别是 $\alpha\omega,\alpha\omega^2$。
将 (3) 逐支用于 (42)，再用 (43)，得到
$$
\boxed{
\begin{aligned}
&\omega^2j_{10,h_{N,\pi}(U_\pi)}
-\omega j_{10,h_{N,\bar\pi}(U_{\bar\pi})}\\
&\hspace{12mm}\equiv
-\alpha(p+1)\log_p(\pi/\bar\pi)
\not\equiv0\pmod{p^{H+1}}.
\end{aligned}
}
\tag{44}
$$
两个质量一分量的未知导数准确相消；两 target frame 的质量
Gaussian 项不相消，正给右边。

R1000 已付
$1\le v_p\log_p(\pi/\bar\pi)\le L_p\le H$，
且 $\alpha(p+1)$ 是本篇好位单位，所以 (44) 的非零有完整证明。
它把 old 检出项放在 (19)、(26)–(34) 的实际第四阶测试上，
没有把某个有限核质量误认成全中央。

要进一步排除同时坏，必须用原两条 canonical 必要行及本篇完整
转置迫使 (44) 左边消失。当前已付的双权降阶、单 Frobenius 权、
六块移位或 (41) 的支撑本身不作这种断言；(44) 是继续消元时
必须完整保留的确切目标，不能删除它的质量对数来制造闭合。

## 10. 完整范围与依赖

本篇所有新来源、权和算子都由显示身份构成，没有数学执行或素数扫描。
固定分母、原 torsion/Miller 的坏处及显示质量分子都已包含在
$p\le13^4$ 中；增长二项式不被无证反演。
尤其没有反演原 $\mathcal H$、$P_{10}$ 或一个可能为零的中央值。

依赖如下：

- R887 §§14–15、19–20：原 $Z,G,P_{10}$ 的完整 $p$ 基、曲率和原点规范。
- R973、R978、R987：全部二、五、十三有限类型、原两 old 标准来源、
  canonical lift 与绝对 Gauss／平方根相位。
- R1000：实际 old 对数的深度上界。
- R1012、R1015：原 Kummer／Miller 分解、标准 $Q_i$、
  全字质量与固定函数 $r$。
- R1013、R1016：原全部长窗口、完整小边界和两 exact，
  单一特征零 trace 与统一 Hurwitz／Newton 无限尾。

(3) 始终是特征零原 $V$ 的全精度结论；
(10)、(25)、(34) 是它的实际模 $p$ 返回。
这两个精度层在本篇没有混用。
