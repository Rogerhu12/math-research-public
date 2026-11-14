# R568 — 原正条带的完整 140/60 核、十度轴与真实混合返回

日期：2026-11-14。**状态：已证明。**

本篇处理 R560/R566 中原正条带，不增添新的算术来源或射线。
两个真正正交的整数输出具有 degree $140,60$ 的完整核心；
它们在原投影两态上的算子都为 $-\chi_{65}\lambda R_1$。
半周期平均、三个 $C$ 共轭、完整中心及绝对锚逐项支付。

由此原正条带准确返回同一个 $h$ 来源，保全部 $D^k$、
原 $E/G/Y/W$、两个 Mellin 单位条件和 R566 的实际超平面。
另以同一个非零联合定标 entire even $\mathcal S_{10}$，
把该正条带框架接回原 $u$ 轴，得到真正返回原 $S/T$ 的混合词域。
所有权和切集均随物理矩阵转置，未将它们改回未移动的原测试。

## 1. 原两态与真正正交三轴

沿用 [R560](R560-native-single-branch-and-seven-conditional-moments.md)、
[R566](R566-original-third-state-fourteen-core-and-native-complements.md)
的原规范和全部固定坏集：
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad\kappa=p\lambda^2.
\tag{1}
$$
$\chi=\chi_{65}\in\{\pm1\}$ 是 R551 已付的真实 odd5/65 核符号；
不假设它对全部素数为同一个号。

只使用原两个投影来源
$$
\mu_0=\mathcal P_C\rho_0,\qquad \mu_h=\mathcal P_Ch,\qquad
h=\eta+\rho_0/2 .
\tag{2}
$$
本篇的 $140/60$ 两态身份不免费延到 R563 的 $\mu_-$。

在原输入 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$ 中，令
$$
D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3,\qquad
D=D_4+c+(2+3\omega)d_0=F-C,\quad N(D)=14,
$$
$$
u=\frac{\omega c+(1-\omega)d_0}{2},\quad
X=c-D/14,\quad Z=d_0+(1+3\omega)D/14 .
$$
定义真正的 $D$ 正交轴
$$
\boxed{
P=u-\frac{\omega^2}{7}D=\frac{\omega}{2}(X-(2+\omega)Z),
\qquad
Z_* = Z-\frac{8+3\omega}{10}P .
}
\tag{3}
$$
完整 Gram 为
$$
N(P)=5/7,\quad N(Z_*)=3/20,\qquad D\perp P,\ D\perp Z_*,\
P\perp Z_* .
\tag{4}
$$
两个整数输出为
$$
\boxed{
\begin{aligned}
R_+&=14P=(-2\omega^2,-2\omega,4,0,2+9\omega,5-3\omega),\\
S_+&=20Z_*=(2\omega,2,4+4\omega,0,3-3\omega,3),
\end{aligned}}
\tag{5}
$$
其 degree 为 $140,60$。

取三个完整余行
$$
Q_2=(1,-\omega^2,0,0,0,0),\qquad
Q_3=(1,\omega^2,\omega,0,0,0),\qquad x=(0,0,0,1,0,0).
$$
$(D,R_+,S_+,3Q_2,3Q_3,3x)$ 是一个完整正交框架，其 degree 为
$14,140,60,18,27,9$，且
$$
\det=-22680\omega,\qquad
N(\det)=2^6\,3^8\,5^2\,7^2 .
\tag{6}
$$
这些全是当前处单位。乘 $3$ 的三个余行清掉纯 $C$ 旋转的分母；
它们不被遗忘。对全部三个 $C$ 共轭再乘原 $\eta$ 的
$\mathsf H$，整个六行框架仍为整数。配套证书保存这些完整行。

## 2. whole 140/60：四半周期及绝对标量

当前 ray 在所需模数上给
$$
g_\pi\equiv211\pmod{280},\qquad
g_\pi\equiv91\pmod{120}.
\tag{7}
$$
可由 $g_\pi\equiv3\bmod8$、$g_\pi\equiv1\bmod3,5,7$ 直接合成；
未添加新的同余。

对 $N=140$ 或 $60$，$m=N/4$ 为奇数。
标准 even $\mathcal S_N$ 的 canonical 二挠平移为
$$
\mathsf T^{(N)}_{(s+r\omega)/2}e_j
=(-1)^{s(j+mr)}e_{j+Nr/2},\qquad s,r\in\{0,1\}.
\tag{8}
$$
第三个非零二挠的中心号已经包含在 $mr$ 中。
令 $\varepsilon(0)=1$、$\varepsilon(t)=-1$（$t\ne0$），
$$
P_{\varepsilon,N}=\frac14\sum_{t\in E[2]}\varepsilon(t)\mathsf T_t^{(N)},
\qquad B_N=2P_{\varepsilon,N}-I .
$$
完整逐基计算得
$$
\boxed{B_Ne_j=-e_{(1+N/2)j},\qquad B_N^2=I.}
\tag{9}
$$
不是无权二挠平均，也不是删掉绝对负号后的排列。

其完整 intertwiner 与 (7) 相同，因为
$$
211\equiv141\cdot71\pmod{280},\quad (141^2-1)/140=142\in2\mathbb Z,
$$
$$
91\equiv61\cdot31\pmod{120},\quad (61^2-1)/60=62\in2\mathbb Z.
\tag{10}
$$
所以只差绝对标量。用 R370/R551 的真实 odd5 来源
$F_5(z)=\sigma(z)\sigma(2z)$ 定标：其完整归一核心为 $\chi$。
非零拉回
$$
F_5(2(3+\omega)z)\in\mathcal S_{140},\qquad
F_5(2\delta z)\in\mathcal S_{60}
$$
与普通核心严格交换。在每条拉回上，三个非零二挠的
canonical 特征均为 $\varepsilon(t)$，所以 $B_N=+1$。
由此准确得
$$
\boxed{
K_{140}=\chi B_{140},\qquad K_{60}=\chi B_{60}
\quad\text{在整个对应空间上}.
}
\tag{11}
$$
两处都使用已有的同一 $\chi$。也可在第二处使用
[R510](R510-original-w2-companion-and-fifteen-axis-central-words.md)
的 $[2]^*B_{15}$ 及 $\chi_{15}=\chi_{65}$，所得规范完全相同。

## 3. 半周期在实际两态上的完整作用

令 $D_j=F-\omega^{2j}C$，并在 (3)–(5) 中把 $D$ 换成 $D_j$，
得到 $R_{+,j},S_{+,j}$。它们是纯 $C$ 旋转的三个真实共轭，
各自 degree、相互 Gram 和 standard even 半特征都保持。

关键的完整原输入计算是
$$
(R_{+,j}\mathsf H)_{c,d_0}=(10,4),\qquad
(S_{+,j}\mathsf H)_{c,d_0}=(0,6\omega^2)
\quad(j=0,1,2).
\tag{12}
$$
在前四共享 sigma 上，$R_{+,j}/2$ 的奇系数个数依次为
$2,4,4$；$S_{+,j}/2$ 也是 $2,4,4$。
因此前四因子贡献的完整半周期字符均为正。
这一步保留了所有原共享输入，不靠它们的边际质量。

在共同 raw $[2]$ pair 的 $\mathcal S_4\otimes\mathcal S_4$ 中，
(12) 分别使平移等于 $(5t,2t)$ 与 $(0,3\omega^2t)$。
完整整周期平移为一，二挠重标只置换三个非零点，所以
对应的 $\varepsilon$ 加权平均分别为
$$
\frac{I-R_c}{2},\qquad \frac{I-R_{d_0}}2 .
$$
在原两态上 $R_{d_0}=R_c$。
上述搬运使用 $\mathsf H$ 保 Gaussian 的准确平移协变，
且只在 R544 已证明 $\mathsf H$ 闭合的原两态上使用；
没有宣称分母为 $2$ 的 $\mathsf H$ 是任意 theta 小格的自同构。

共轭回去，R544 的原 $u$ 反射为
$R_1=\mathsf H_*R_c\mathsf H_*^{-1}$。所以完整实际身份是
$$
\boxed{
P_{\varepsilon,R_{+,j}}
=P_{\varepsilon,S_{+,j}}=\frac{I-R_1}{2},
\qquad
B_{R_{+,j}}=B_{S_{+,j}}=-R_1
}
\tag{13}
$$
于原两态上。原 $R_1$ 只操作最后两个输入，故与纯 $C$ 旋转交换。
把三条 (13) 完整平均，严格得到同一身份对 (2) 的来源成立。

按来源列表示每个像，在基 $(\mu_0,\mu_h)$ 上
$$
\boxed{
\mathsf R_1=
\begin{pmatrix}1/2&3/4\\1&-1/2\end{pmatrix},\qquad
\mathsf R_1^2=I .
}
\tag{14}
$$
即
$R_1\mu_0=\mu_0/2+\mu_h$、
$R_1\mu_h=3\mu_0/4-\mu_h/2$。
令
$$
\Delta^C=\tfrac32\mu_0-\mu_h,\qquad
\Gamma^C=\tfrac32\mu_0+\mu_h .
$$
准确有
$$
R_1\Delta^C=2\mu_h,\qquad R_1\Gamma^C=\Gamma^C .
\tag{15}
$$

## 4. 同一原框架的全部深度矩形

单位倍点 $14,20$ 不改变物理深域。由 (11)–(14)，
任意 $n,r,s\ge0$ 及原两态的任意线性组合 $\mu$ 都有
$$
\boxed{
\mu|_{\{D\in p^n,\ P\in p^r,\ Z_*\in p^s\}}
=\beta^n(-\chi\lambda)^{r+s}
(P_{D,\kappa^n}P_{P,\kappa^r}P_{Z_*,\kappa^s})_*
R_1^{r+s}\mu .
}
\tag{16}
$$
完整三个余坐标固定不动。
特别 $P,Z_*$ 共同深 $m$ 返回 $\lambda^{2m}\mu$，
但独立深度的 $R_1$ 不得丢掉。

R560 的原正条带准确为
$$
\mathcal B_+=\{Z\text{ unit},X-(2+\omega)Z\in p\}
=\{P\in p,\ Z_*\text{ unit}\}.
\tag{17}
$$
这里用到
$$
Z=Z_*+\frac{8+3\omega}{10}P,\quad
X=-\frac{7+9\omega}{10}P+(2+\omega)Z_*,\quad
L=\frac{14}{5}P+4\omega Z_* .
\tag{18}
$$
因此它正是原 $D$ 深归一后保留的 $u$ 深、$L$ 单位条带，
不是另选的一条深轴。

## 5. 原正条带的完整来源返回

仍取原
$\widehat P_p=\mathcal R_pP_p$、原 $\ell(Y,W)$，并保其所有
$p,\lambda,\kappa$ 系数。令 R560 正条带的完整贡献为
$$
\mathcal N_{+,n}=
\frac{\beta^n}{b\Omega^6}
\int_{\substack{E\text{ unit}\\\mathcal B_+}}
\widehat P_p(D,E,G)\,\ell(Y,W)\,d\Delta^C .
\tag{19}
$$
对 (17) 使用真实 $P$ 核，(15) 给
$$
\boxed{
\mathcal N_{+,n}
=-\frac{2\chi\lambda\beta^n}{b\Omega^6}
\int_{\substack{Z_*\text{ unit}\\E_\kappa\text{ unit}}}
\widehat P_p(D,E_\kappa,G_\kappa)\,
\ell(Y_\kappa,W_\kappa)\,d\mu_h .
}
\tag{20}
$$
下标 $\kappa$ 始终表示 $P\mapsto\kappa P$ 的完整物理转置。
没有遗忘 $D$，所以 $\widehat P_p$ 的全部七条 $D^k$ 都仍在。
原 $Y$、$W$ 的两项仍分别在 $Y_\kappa,W_\kappa$ 单位时取 log。

为使 (20) 完全可检查，任一观察写成
$r=r_*+a_rP+b_rZ_*$，其中 $r_*$ 是同一三个余坐标的真实线性式：

| $r$ | $a_r$ | $b_r$ |
|---|---:|---:|
| $E$ | $14\omega/5$ | $28(1+\omega)/3$ |
| $Y$ | $7(3+\omega)/10$ | $(22+\omega)/3$ |
| $W$ | $7(11+\omega)/10$ | $(22+25\omega)/3$ |
| $W'$ | $21/5$ | $(50+18\omega)/3$ |
| $G$ | $(28+70\omega)/5$ | $(140+84\omega)/3$ |
| $L$ | $14/5$ | $4\omega$ |
| $\bar H$ | $3(5-\omega)/10$ | $(2+7\omega)/3$ |

其中 $Y_*=W_*$，$L_*=0$，而 R566 的原超平面满足
$$
\bar H_*=-\delta E_*/14,\qquad
\bar H=\delta(X-E/14).
\tag{21}
$$
所有完整余行在证书中；没有用它们的质量替代函数。
因此，例如
$$
Y_\kappa=Y_*+\frac{7(3+\omega)}{10}\kappa P
+\frac{22+\omega}{3}Z_*,
$$
$$
W_\kappa=Y_*+\frac{7(11+\omega)}{10}\kappa P
+\frac{22+25\omega}{3}Z_* .
\tag{22}
$$
在 $Z_*$ 单位上二者之差仍是单位阶，一般不能把两项 log
改成一个共同单位域上的 $\log(Y_\kappa/W_\kappa)$。

若保 R566 的两个真实补域，则在 (20) 另外使用
$\bar H_\kappa$ 为单位或为深的准确条件。
因为所有系数整、$\kappa P$ 深，这些事件等价于
$$
-\frac{\delta}{14}E_*+\frac{2+7\omega}{3}Z_*
\text{ 为单位或为深}.
\tag{23}
$$
在深支中，$E_\kappa$ 为单位还由 $Z_*$ 单位自动推出：
原同一域正是 $E-14(2+\omega)Z\in p$。
但在单位补支，$E_\kappa$ 单位条件独立保留。
(20)–(23) 包含所有质量和 log 项，未预设其常数项相消。

## 6. 原 u 的真实十度伴随及绝对锚

定义整数行
$$
\boxed{
Q_{10}=D-2\omega u
=(1,\omega^2,-2\omega,0,2+\omega,1+\omega).
}
\tag{24}
$$
有 $N(Q_{10})=10$、$Q_{10}\perp u$，并且它与 $Z_*$ 及三个余行正交。
两真实框架的转换是
$$
\binom{u}{Q_{10}}=
\begin{pmatrix}\omega^2/7&1\\5/7&-2\omega\end{pmatrix}
\binom D P,\qquad\det=-1 .
\tag{25}
$$
所以两轴共同深及共同缩放在两框架中严格相同。

当前 $g_\pi\equiv11\bmod20$，$11\equiv1\bmod10$，
$(11^2-1)/10=12$ 偶，故整个 standard even $\mathcal S_{10}$
的完整核心为某个标量 $s_p$。
(24) 及它的三个 $C$ 共轭均为整数 even 行；
乘原 $\mathsf H$ 后 pair 系数准确为 $(0,-2\omega)$，
所以这里确实是整个 $\mathcal S_{10}$，没有免费延长低 degree 核。

用 (25) 的同一个非零联合确定绝对标量。
$(D,P)$ 共同深的来源为
$$
\beta(-\chi\lambda)R_1=\chi\lambda^2R_1 .
$$
另一方面，原 $u$ 核已由 R544 支付为 $\lambda R_1$；
$(u,Q_{10})$ 共同深给 $s_p\lambda^2R_1$。
两个真实域和共同缩放完全相同，$R_1\mu_0\ne0$，因此
$$
\boxed{K_{10}=\chi_{65}I
\quad\text{在整个 standard even }\mathcal S_{10}\text{ 上}.}
\tag{26}
$$
这是非零完整张量锚，不需要不存在的 norm $5$ 一变量 CM 倍点，
也没有添加一个未知符号。

特别
$$
\mu|_{\{u\in p^r,Q_{10}\in p^s\}}
=\lambda^r(\chi\lambda)^s
(P_{u,\kappa^r}P_{Q_{10},\kappa^s})_*R_1^r\mu .
\tag{27}
$$
保原 $D$ 深 $n$、$u$ 深的一支时，真实剩余斜条件是
$Q_{10}+2\omega u\in p^n$；不能把它改成两个任意独立深度。

## 7. 返回原 S/T 的真实两步词

原 $u$ 核为 $\lambda R_1$，新 $P$ 核为
$-\chi\lambda R_1$，故两步来源乘积是 $-\chi\lambda^2I$。
令
$$
\mathcal A=P_{u,\kappa}P_{P,\kappa}.
$$
只在 $(D,P)$ 平面上的实际矩阵为
$$
\boxed{
\mathcal A=
\begin{pmatrix}
(5+2\kappa)/7&2\omega\kappa(\kappa-1)\\
5\omega^2(\kappa-1)/49&\kappa(2+5\kappa)/7
\end{pmatrix}.
}
\tag{28}
$$
它固定 $Z_*$ 和三个余行，
$$
\det\mathcal A=\kappa^2,\qquad
\operatorname{tr}\mathcal A=(5+4\kappa+5\kappa^2)/7 .
$$
实际词域先要求 $u$ 深，归一后再要求 $P$ 深，正是
$\mathcal A\mathcal O^6$；不是 raw $u,P$ 独立深。
完整测度身份为
$$
\boxed{\mu|_{\mathcal A\mathcal O^6}
=-\chi\lambda^2\,\mathcal A_*\mu
\quad(\mu\in\operatorname{span}\{\mu_0,\mu_h\}).}
\tag{29}
$$

取 R536 原完整三支 $q_n$，在此像格上定义
$q_{\mathcal A}=q_n\circ\mathcal A^{-1}$、
$Y_{\mathcal A}=Y\circ\mathcal A^{-1}$、
$W_{\mathcal A}=W\circ\mathcal A^{-1}$。
纯 $C$ 投影保持原 $q_n,Y,W$ 的整个测试，所以
$$
\boxed{
\begin{aligned}
\int_{\mathcal A\mathcal O^6,\ Y_{\mathcal A}\text{ unit}}
q_{\mathcal A}\langle Y_{\mathcal A}\rangle^{dv}\,d\mu_0
&=-\chi\lambda^2\beta^nJ_S(v),\\
\int_{\mathcal A\mathcal O^6,\ W_{\mathcal A}\text{ unit}}
q_{\mathcal A}\langle W_{\mathcal A}\rangle^{dv}\,d\mu_0
&=-6\delta\chi\lambda^2\beta^nJ_T(v).
\end{aligned}}
\tag{30}
$$
原周期、系数与所有隐藏条件都由同一个 $\mathcal A^{-1}$ 转置。
(30) 不把 $q_{\mathcal A},Y_{\mathcal A},W_{\mathcal A}$
换回未移动的原测试。它给真正的原算术返回，但不据此删掉
(20) 的实际剩余域。

## 8. 范围与复现

本篇付清的核心及矩形都作用于 (2) 的原投影两态。
R563 新 $\mu_-$ 虽有 R566 已付的完整十四度核心，却没有因此
自动获得 (13) 的 $140/60$ 旧两态作用。
(20) 保所有 $D^k$ 与原两 log；(23) 保两个真实超平面补支；
(30) 则完整保移动的原中央测试。

主目标仍需这些实际补域与原算术条件进一步联立，不能从
whole 核、来源两态闭合或某个辅助单位矩直接结束。

- [check-r568-original-positive-strip-full-cores-and-native-transport.js](../scripts/check-r568-original-positive-strip-full-cores-and-native-transport.js)
- [check-r568-original-positive-strip-full-cores-and-native-transport.json](../scripts/check-r568-original-positive-strip-full-cores-and-native-transport.json)

脚本以 BigInt 有理 CM 算术核定完整正交框架、三个共轭的
全部原/η整数行、全部 $140+60$ 个 canonical 列、
两个完整中心、来源矩阵、十度共同深转换以及所有原观察的余行。
全深度和切集的证明由正文给出，不以有限素数采样替代。
