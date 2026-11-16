# 原四来源的同一 degree24 奇因子与三维真实差矩阵

日期：2026-11-16。**状态：以下来源身份、整格、完整差矩阵和实际二挠投影均已证明；指定矩阵的秩及指定向量是否被它杀掉仍未证明。** 本注不以环境三维、一个首系数为单位或共同因子的非零，替代四条原中央首必要行的共同非消失。

这里的四个来源始终是原 $S,T,U,V$，degree 为 $34,72,136,66$，首项都为 $z^6$。全部 $U$ 多项式取 [R466](../results/R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md) 的已识别来源，全部二倍 old 来源取 [R812](../results/R812-original-same-charge-cancellation-and-complete-source-budget.md)。Hurwitz 整格及 canonical 除 $p$ 行取 [R855](../results/R855-original-full-heat-connection-and-canonical-divided-jet.md)、[R856](../results/R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md)。没有数学数值运行或目标素数扫描。

## 1. 共同奇因子的绝对五 sigma 规范

保持原
$$
y^2=x^3+b,\quad D_zx=2y,\quad
X=x^3,\quad t=-b/x^3,\quad
\Theta=x\sigma^2,\quad \delta^2=-3,\quad\gamma=3+\omega.
\tag{1}
$$
这里 $b$ 是原固定单位，$y\sim-z^{-3}$。令
$$
Q_2(X)=7X^2-4bX+16b^2,\qquad h_7(t)=7+4t+16t^2.
$$
R855 的原共同偶因子为 $A_{24}=\sigma^{24}y^2Q_2/7$。
定义
$$
\boxed{
C_{24}=-\frac{\sigma^{24}x^2yQ_2}{7}
=-\frac{\sigma(\gamma z)\sigma(\bar\gamma z)
              \sigma(\delta z)^2\sigma(2z)}{42}.
}
\tag{2}
$$
第二式包括绝对倍率。事实上
$\sigma_\gamma\sigma_{\bar\gamma}=\sigma^{14}Q_2$、
$\sigma_\delta^2=-3x^2\sigma^6$ 和
$\sigma_2=-2y\sigma^4$，其乘积恰为
$6x^2yQ_2\sigma^{24}$。
五个输入的范数为 $7,7,3,3,4$，总和 $24$；
首项之积为 $7\delta^2\cdot2=-42$。所以
$$
C_{24}=z^5+O(z^{11}),\qquad C_{24}(\zeta z)=\zeta^5C_{24}(z).
\tag{3}
$$
所有原半特征和准周期均由(2)的实际恒等式保持。

置
$$
v=-y/x^2=z+O(z^7).
$$
则是同一原函数的准确分解
$$
\boxed{A_{24}=C_{24}v.}
\tag{4}
$$
$v$ 本身是有理函数；下面逐项证明它乘原伙伴后全纯，不能单独把它当作一个新的全纯 degree 零来源。

## 2. 四个完整全纯奇伙伴

定义固定齐次多项式
$$
\begin{aligned}
A_2&=X^2+20bX-8b^2,\\
P_-&=X^3-96bX^2+48b^2X+64b^3,\\
P_+&=X^3+228bX^2+48b^2X+64b^3,\\
F_4&=X^4+40bX^3+2112b^2X^2+3136b^3X+1792b^4,\\
G_4&=13X^4+52bX^3+1536b^2X^2+1024b^3X+256b^4,\\
H_8&=X^8+1232bX^7-58688b^2X^6-49408b^3X^5\\
&\qquad-439040b^4X^4-2111488b^5X^3-1949696b^6X^2
-851968b^7X-32768b^8.
\end{aligned}
\tag{5}
$$
原四伙伴准确为
$$
\boxed{
\begin{aligned}
J_S&=-\sigma^{10}y(X-8b),\\
J_T&=-\sigma^{48}xy(X-8b)(X+4b)A_2P_-,\\
J_U&=-\frac{\sigma^{112}yA_2F_4G_4H_8}{13},\\
J_V&=-\sigma^{42}xy(X-8b)^2(X+4b)P_+.
\end{aligned}
}
\tag{6}
$$
于是
$$
\boxed{
S=C_{24}J_S,\quad T=C_{24}J_T,\quad
U=C_{24}J_U,\quad V=C_{24}J_V.
}
\tag{7}
$$

证明直接将 R855(43)的 $H_{10},H_{48},H_{112},H_{42}$
分别乘以 $v$。其原最低 $x$ 幂依次为 $2,3,2,3$，
所以除 $x^2$ 后无有限极。具体得到(6)，没有丢掉 $H_8$
或 $G_4$ 的任何项。对 $U$，R466(49)的系数 $1/91$
与(2)的 $1/7$ 相除，正给(6)的 $1/13$。

四个 $J_\nu$ 的 degree 依次是
$$
n_S=10,\quad n_T=48,\quad n_U=112,\quad n_V=42.
\tag{8}
$$
它们在 $O$ 的最大函数极阶依次为 $9,47,111,41$；
最高系数的负号与 $y\sim-z^{-3}$ 相消，$G_4$ 的最高系数 $13$
又被(6)中的 $13$ 除去。因此
$$
\boxed{
J_\nu=z+O(z^7),\qquad J_\nu(\zeta z)=\zeta J_\nu(z)
}
\tag{9}
$$
逐条成立。这里四个来源都是完整 whole 奇截面，
不再保留一个待消的 $X-8b$ 分母。

和已发表同 $S/V$ 奇来源的联系同样准确。令
$$
F_6=\sigma^6(X-8b),\qquad F_6(0)=1.
$$
则
$$
C_{30}=C_{24}F_6,\qquad
J_S=F_6\frac{\sigma(2z)}2,\qquad
J_V=F_6\frac{\sigma(6z)}6.
\tag{10}
$$
所以本注没有改动旧 $S/V$ 的最后一个实际 sigma 输入。

## 3. 同一整格的三维型五空间

定义整基
$$
\boxed{
E_j=-b^j\sigma^{24}x^{8-3j}y=C_0(-t)^j,\quad
j=0,1,2,\qquad C_0=-\sigma^{24}x^8y.
}
\tag{11}
$$
这固定了列的符号；以后不将 $(-t)^j$ 换成 $t^j$。
原向量准确为
$$
\boxed{
C_{24}=E_0-\frac47E_1+\frac{16}{7}E_2,\qquad
c_*=(1,-4/7,16/7)^t.
}
\tag{12}
$$
把(11)按 $t$ 合并才得到 $C_{24}/C_0=h_7(t)/7$。

在原 whole $\mathscr V_{24}$ 中，奇函数基为
$\sigma^{24}x^ay$、$2a+3\le24$。
其 $\mu_6$ 型为 $24-2a-3$；要等于 $5$，恰有
$a=2,5,8$。因此
$$
\boxed{
\mathscr V_{24}^{(5)}
=\langle E_0,E_1,E_2\rangle,\qquad\dim=3.
}
\tag{13}
$$
各基的原点阶为 $5,11,17$。在 $b,7$ 均为单位的原整模型上，
(11)仍为整基，维数没有由约化下降。
若写实际角投影
$$
\Pi_hA(z)=\frac16\sum_{\zeta\in\mu_6}\zeta^{-h}A(\zeta z),
$$
则
$\Pi_5E_j=E_j,\ \Pi_1J_\nu=J_\nu,\ \Pi_0(E_jJ_\nu)=E_jJ_\nu$。
这里只用了原 CM 自同构的完整角作用，
不把(13)认成已知 CM13 特征线或一个新的算术来源。

## 4. 同一个奇 canonical 行及四条完整低配对

固定原 $p=6s-1>211$，保原固定坏集。
写 $j_k(A)=D_z^kA(0)$。
R856 的整 whole 恒等式给
$j_p(E_j)\equiv H(P)j_1(E_j)=0$，所以
$$
O_j=\frac{j_p(E_j)}p\bmod p
\tag{14}
$$
是 whole degree24 的合法奇行值。
其提升无关范围是整个该 CM 整格；
每个 $E_jJ_\nu$ 的中心又严格为零，所以 R855 的偶行
$\mathfrak B(E_jJ_\nu)=j_{p+1}(E_jJ_\nu)/p\bmod p$ 也有定义。

因为 $j_1(E_j)=0$、$j_1(J_\nu)=1$，
Leibniz 的高端项恰为 $(p+1)j_p(E_j)$。
所有其余非零项为
$k=p-6r$ 与 $p+1-k=6r+1$，其中 $1\le r\le s-1$；
它们都严格低于 $p$。再用
$$
\frac1p\binom{p+1}{p-6r}
\equiv-\frac1{6r(6r+1)},
$$
得到
$$
\boxed{
\mathfrak B(E_jJ_\nu)
=O_j-\sum_{r=1}^{s-1}
\frac{j_{p-6r}(E_j)j_{6r+1}(J_\nu)}
     {6r(6r+1)}.
}
\tag{15}
$$
每个分母在原剩余域中都是单位。若原点阶使一个 jet 为零，
仍按(15)的实际值处理，不增加假设。

原四来源由(12)–(15)逐项读出。
共同高行是 $O_*=\sum_jc_{*,j}O_j$。
定义真正的三差矩阵，行依次为 $T,U,V$，列为(11)：
$$
\boxed{
M_{\nu j}=
-\sum_{r=1}^{s-1}
\frac{j_{p-6r}(E_j)
\big(j_{6r+1}(J_\nu)-j_{6r+1}(J_S)\big)}
     {6r(6r+1)}.
}
\tag{16}
$$
它满足没有省项的等式
$$
\boxed{
\begin{pmatrix}
\mathfrak B_T-\mathfrak B_S\\
\mathfrak B_U-\mathfrak B_S\\
\mathfrak B_V-\mathfrak B_S
\end{pmatrix}
=M_pc_*.
}
\tag{17}
$$
因而原四条首必要零条件**等价于**
$$
\boxed{\mathfrak B_S=0,\qquad M_pc_*=0.}
\tag{18}
$$
这里 $M_p$ 的元素由原 sigma 与四个(6)唯一确定，
不是待自由选择的 $3\times3$ 矩阵。
其行列式非零会排除(18)，而即使行列式为零，
只要能证明这个指定 $c_*$ 不在核中也足够。
本注尚未证明这两种充分结论中的任一种。

## 5. 保完整横向项的水平标量式

在已付固定代数水平覆盖上，取(11)各原纤维的水平延拓，
并置
$$
g_j=j_{24,1}(E_j^\flat),\qquad
h_\nu=j_{n_\nu,1}(J_\nu^\flat).
$$
它们都是先于 $p$ 固定的代数函数。
采用原完整奇算子
$$
\mathscr U_0=1,\quad \mathscr U_{-1}=0,\qquad
\mathscr U_{r+1}=L\mathscr U_r-\frac{r(2r+1)}{24}g_2\mathscr U_{r-1}.
\tag{19}
$$
在原 CM 参数点 $P$，
$$
j_{2r+1}(E_j)=48^r(\mathscr U_rg_j)(P),\qquad
j_{2r+1}(J_\nu)=(2n_\nu)^r(\mathscr U_rh_\nu)(P).
\tag{20}
$$
尤其 $h_\nu(P)=1$；若 $g_*=\sum c_{*,j}g_j$，则
$$
g_*(P)=Lg_*(P)=0,\qquad L^2g_*(P)=\frac{120}{48^2}=\frac5{96}.
\tag{21}
$$
令 $n=(p-1)/2$，(16)的完整水平表达是
$$
\boxed{
M_{\nu j}=-48^n
\sum_{r=1}^{s-1}
\frac{(\mathscr U_{n-3r}g_j)(P)}
     {6r(6r+1)}
\left[
\left(\frac{n_\nu}{24}\right)^{3r}
(\mathscr U_{3r}h_\nu)(P)
-\left(\frac5{12}\right)^{3r}
(\mathscr U_{3r}h_S)(P)
\right].
}
\tag{22}
$$
$48^n=(48/p)=(3/p)$ 是单位。
四个倍率的三次幂是 $(5/12)^3,8,(14/3)^3,(7/4)^3$，
但 $h_S,h_T,h_U,h_V$ 并不相同；
不能把(22)改成同一个多项式在四个点的值。

(19)必须先在 $g_2,g_3$ 双变量中形成，再在 $P$ 读数。
本节没有把水平延拓的乘积当作原总 degree 的水平延拓：
R855(56)–(57)的平衡二阶伙伴项仍然存在。
使用(20)只读取同一纤维的物理 jet，故没有删除该项。

## 6. 原 Θ 与同一局部参数中的完整矩阵

下面给(16)的另一准确表达，用于直接对接原有限低卷积。
置 $d=1+8t$，并定义
$$
\begin{aligned}
A_t&=1-20t-8t^2,\\
P_{-,t}&=1+96t+48t^2-64t^3,\\
P_{+,t}&=1-228t+48t^2-64t^3,\\
F_t&=1-40t+2112t^2-3136t^3+1792t^4,\\
G_t&=13-52t+1536t^2-1024t^3+256t^4,\\
H_t^{[8]}&=1-1232t-58688t^2+49408t^3-439040t^4\\
&\qquad+2111488t^5-1949696t^6+851968t^7-32768t^8,\\
H_{18}(t)&=A_tF_tG_tH_t^{[8]}.
\end{aligned}
\tag{23}
$$
这里(23)与 R812 的两个负因子写法相同，$H_{18}(0)=13$。
定义
$$
\begin{aligned}
\phi_S&=t(t-1)d,\\
\phi_T&=t(t-1)d(1-4t)A_tP_{-,t},\\
\phi_U&=t(t-1)H_{18}/13,\\
\phi_V&=t(t-1)d^2(1-4t)P_{+,t}.
\end{aligned}
\tag{24}
$$
令 $q_\nu=m_\nu/2=17,36,68,33$。直接从(6)得到
$$
\boxed{
E_jJ_\nu=b^{-1}(-t)^j\Theta^{q_\nu}\phi_\nu(t).
}
\tag{25}
$$
各 $\phi_\nu$ 首项均为 $-t$，所有有限因子完整保留。

现在用原
$$
w=bz^6,\qquad
w=-t\,\mathcal H(t)^6,\qquad
\mathcal H(t)=\sum_{\ell\ge0}
\frac{\binom{2\ell}{\ell}}{4^\ell(6\ell+1)}t^\ell.
\tag{26}
$$
$\Theta(t)$ 指原 $\Theta(z(t))$，没有改为另一解。
由 R855 的符号 $[z^{p+1}]=-\mathfrak B$，
$$
\boxed{
M_{\nu j}=-b^{s-1}[w^s]\,
(-t(w))^j\!
\left[
\Theta(t(w))^{q_\nu}\phi_\nu(t(w))
-\Theta(t(w))^{17}\phi_S(t(w))
\right].
}
\tag{27}
$$
这保同一原 $R_{636}$ 初始资料与所有低于首共振的卷积。

Lagrange 反演进一步给真正的有限 residue 行
$$
\boxed{
M_{\nu j}
=-6(-1)^sb^{s-1}[t^{s-1}]
\mathcal H(t)^{-1}\frac d{dt}
\left\{
(-t)^j
\big[\Theta(t)^{q_\nu}\phi_\nu(t)-\Theta(t)^{17}\phi_S(t)\big]
\right\}.
}
\tag{28}
$$
证明：特征零的反演因子是
$(-1)^s\mathcal H^{-6s}/s$。
在所读严格小于 $p$ 的窗口中，
$\mathcal H^{-6s}=\mathcal H^{-p-1}\equiv\mathcal H^{-1}$
且 $1/s\equiv6$。
所有方括号从 $t^{j+1}$ 起，所以(28)只读 $\Theta$
至 $s-1$ 阶；原第 $s$ 阶的 sigma 分母没有被任意约化或删除。
$\mathcal H$ 的此窗口也整。
导数作用于整个方括号，特别完整保留
$q_\nu\Theta'/\Theta$ 和原多项式导数两项。
将 $\Theta^{q_\nu}$ 省去会改变(28)。

### 6.1 同一完整核中的连续三系数

(27)也可以完全保留原 residue 核而不显写导数。
令
$$
\mathcal R(t)=\frac{(1-t)^{-1/2}}{\mathcal H(t)^2},\qquad
d_{\nu,k}=[t^k]\mathcal R(t)
\big[\Theta(t)^{q_\nu}\phi_\nu(t)-\Theta(t)^{17}\phi_S(t)\big].
\tag{28a}
$$
由于 $\mathcal H+6t\mathcal H'=(1-t)^{-1/2}$，
原变量变换在特征零准确给
$$
[w^s]F(t(w))
=(-1)^s[t^s](1-t)^{-1/2}\mathcal H^{-6s-1}F(t).
$$
$6s+1=p+2$，在本节同一整窗口中
$\mathcal H^{-6s-1}\equiv\mathcal H^{-2}$。
因此实际矩阵就是
$$
\boxed{
M_p=-(-1)^sb^{s-1}
\begin{pmatrix}
d_{T,s}&-d_{T,s-1}&d_{T,s-2}\\
d_{U,s}&-d_{U,s-1}&d_{U,s-2}\\
d_{V,s}&-d_{V,s-1}&d_{V,s-2}
\end{pmatrix}.
}
\tag{28b}
$$
这三列是同一个原 $\mathcal R\Theta^{q_\nu}$ 卷积的连续三系数，
不是三个可独立指定的顶端参数。
特别原指定向量给每行的准确组合
$$
(M_pc_*)_\nu
=-(-1)^sb^{s-1}
\left(d_{\nu,s}+\frac47d_{\nu,s-1}+\frac{16}{7}d_{\nu,s-2}\right).
\tag{28c}
$$
括号正是原 $h_7/7$ 因子的完整作用。
首必要条件只令(28c)为零，并不分别令(28b)的三个条目为零。

## 7. 原 U 的二挠 new 条件怎样运输

本节只运输已经支付的原投影，不从环境维数补一个特征。
令
$$
\Pi_2^{136}=\frac14\sum_{\tau\in E[2]}T_\tau^{(136)}
$$
使用 R466 的同一 canonical 半特征和绝对平移。
其已付身份为
$$
\Pi_2^{136}U=0,\qquad
\Pi_2^{136}\{S(2z)/64\}=S(2z)/64.
\tag{29}
$$

原 theta 结构下，degree 的张量乘法给
$T_\tau^{(136)}(AB)
=(T_\tau^{(24)}A)(T_\tau^{(112)}B)$。
这也可在同一 sigma 准周期公式中逐项核：
指数与半特征均按 $24+112=136$ 相乘；
这里使用的是同一个 $\tau$ 的一致 canonical lift。
所以(29)对本注输入准确为
$$
\boxed{
\frac14\sum_{\tau\in E[2]}
(T_\tau^{(24)}C_{24})(T_\tau^{(112)}J_U)=0.
}
\tag{30}
$$
不能据此令 $\Pi_2^{112}J_U=0$，因为 $C_{24}$ 的四个译像不同。

为将 old 部分同时写全，令
$$
J_{\rm old}=\frac{S(2z)}{64C_{24}},\qquad
J_B=J_U-J_{\rm old}.
\tag{31}
$$
R812 的完整因式给
$$
J_{\rm old}=-y\sigma^{112}x^{54}d(t)^2H_{16}(t),
\tag{32}
$$
其中
$$
\begin{aligned}
H_{16}&=(t-1)^2A_t^2B_tR_t,\\
B_t&=1+536t-1344t^2+2048t^3-512t^4,\\
R_t&=1+84t+11040t^2-47936t^3
       +204288t^4-33792t^5+4096t^6.
\end{aligned}
\tag{33}
$$
因为 $\deg(d^2H_{16})=18$，(32)中最低 $x$ 幂为零；
它也是 whole degree112 奇截面，首项为 $z$。
这里 $b$ 的一般规范由 $t=-b/x^3$ 自动恢复。
由已付 $B^{[2]}=1890bz^{12}+\cdots$，
$$
J_B=1890bz^7+O(z^{13}).
\tag{34}
$$

在所有使 $C_{24}J$ 为完整 meromorphic degree136 截面的域中，
定义其准确共轭投影
$$
\mathcal P_CJ=C_{24}^{-1}\Pi_2^{136}(C_{24}J)
=\frac14\sum_{\tau\in E[2]}
\frac{T_\tau^{(24)}C_{24}}{C_{24}}T_\tau^{(112)}J.
\tag{35}
$$
这是 $\Pi_2^{136}$ 的真正共轭，故 $\mathcal P_C^2=\mathcal P_C$。
所有商的有限极都保留；没有声称它把任意 whole degree112
伙伴仍送到该 whole 格。对三个实际伙伴，(29)严格给
$$
\boxed{
\mathcal P_CJ_U=0,\qquad
\mathcal P_CJ_{\rm old}=J_{\rm old},\qquad
\mathcal P_CJ_B=-J_{\rm old}.
}
\tag{36}
$$
式(30)–(36)完整保原 $2$ 处条件、所有四译像与倍率，
并没有提供首 $p+1$ 除 $p$ 行与该投影交换的新定理。
同理，原 CM7/13/19 或固定 $P_{2,M}$ 返回
仍必须连同其实际伙伴和 frame 运输，不能只作用(13)的一条裸列。

本注把四条指定问题压到同一个原三维奇空间，并给出无自由项的矩阵
(16)、(22)、(28)及指定向量(12)。
后续真正需要判定的是(18)，或者利用原完整中央条件得到它之外
一个已经识别的约束。原非零 $L^2g_*$、完整二挠 new 条件、
以及三维环境本身都不替代这一步。
