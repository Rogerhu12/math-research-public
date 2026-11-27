# 原 type4 三维来源的固定惰性29低系数消费者

日期：2026-11-27。状态：唯一公开执行已返回，完整原系数行在模29下非零；范围限于本页所列固定输入。

本次只计算 R806 原 $B_4=\operatorname{im}P_{B_4}$ 的完整次数28系数行。
$P_{B_4}$ 沿 R798 的原三个半周期与绝对相位重建，保全部六列及其三维像；
不调用 CM13 fiber、main 或原算子重建，不扫描素数。
运行只在本公开仓库 Actions，使用 Python 与 python-flint 0.9.0，不保存输出文件。

## 1. 精确来源与完整递推

置 $u=z^6$，原 $b=1$ 模型 $y^2=x^3+1$ 的微分为 $dx/(2y)$。
写
$$
x(z)=z^{-2}A(u),\quad A(u)=1+\sum_{n\ge1}a_nu^n,\qquad
\log\frac{\sigma(z)}z=\sum_{n\ge1}f_nu^n.
$$
原微分方程给
$$
(A-3uA')^2=A^3+u,\qquad
a_1=-\frac17,\qquad
a_n=\frac{\sum_{i=1}^{n-1}a_i a_{n-i}}{(n-1)(6n+1)},\qquad
f_n=-\frac{a_n}{6n(6n-1)}.
$$
特别是 $a_1$ 的负号沿原 R817，而非换成另一条 $b$ 符号的曲线。
对 $p=29$、$m=p-1=28$，原第 $j$ 列
$\sigma^{34}x^{3j}$ 的最小次数为 $34-6j$，
故其完整系数准确为
$$
r_j=[u^{j-1}]\,\exp\left(34\sum_{n\ge1}f_nu^n\right)A(u)^{3j},
\qquad j=0,\ldots,5 .
$$
负指数系数为零，其余最大只到 $u^4$。指数递推为
$ne_n=34\sum_{k=1}^n kf_ke_{n-k}$。
源码同时在有理数域与 $\mathbf Z/29^2$ 中独立递推，并核完整椭圆方程窗；
所有实际分母须在该模数下可逆，不能先取浮点近似。

## 2. 全投影、原b17和阶乘

完整投影行是 $rP_{B_4}$，全部六列都保留。
同时计算原三个独立列基上的读数，核特征零和模29的秩恰3，
并在双坐标环
$$
(\mathbf Z/841)[\omega]/(\omega^2+\omega+1)
$$
独立核全矩阵幂等、全行回乘和确切约化。
惰性29没有 $\mathbf F_{29}$ 中的 $\omega$ 根，故不得用虚假的标量代入。

若 $\theta^6=17$，原 physical 基是
$17^{5-j}\sigma_{17}^{34}x_{17}^{3j}
=\theta^{-4}(\sigma_1^{34}x_1^{3j})(\theta z)$。
于是当前次数28的共同倍率准确为 $17^4$，再转 Hurwitz 行乘 $28!$；
源码保这两个完整整数以及模841的实际值，不把它们略去。

## 3. 一次实际执行的范围

入口：[脚本](../scripts/check-fixed-p29-original-type-four-pb4-row.py)，
请求名 rank2-original-type4-fixed-inert29-coefficient-v1，
复用既有 .github/workflows/rank2-sha-small-public-check.yml，
无共享workflow改动。原依赖为 R798 与其 R732 核；
两者源码哈希和本源码哈希由实际运行报告。

报告的 structural PASS 只指完整递推/投影/回乘这些确定恒等；
原行的零或非零另以观察布尔和精确读数如实输出，不预设非零。
尚不把这一次有限系数行称作原 $h_{j,29}$：
R1049 的原全部常数、toric/type4 比较以及小29的整格前提仍须另付。
它也不证明每条 eigenline 的非零、跨素数非零或通常全 $\Sha$ 结论。

实际 run、job、source、必要结果与全字节哈希在回执返回后补入；
可重算输出本身不入仓库。

## 4. 唯一公开回执与实际完整行

实际 [run46043135878](https://github.com/Rogerhu12/math-research-public/actions/runs/46043135878)，
job140655635855，source346dd26f5c8969b0b84664e568ce42b03b1e5dfa，
2026-11-27 17:36:20 UTC 返回。
原 PB4 在特征零及模29的秩均为3，原独立列为0、1、2。
完整次数28投影行准确为
$$
r_{28}P_{B_4}\bmod29=(20,27,7,20,23,21),
$$
全部 $\omega$ 坐标为零；其模841的完整返回为
$$
(803,665,819,832,429,688).
$$
故这个指定原三维来源上的系数 functional 非零，其精确最小29赋值为0。
原 $17^4\cdot28!$ 模841为260，完整 physical Hurwitz 投影行模841为
$$
(212,495,167,183,528,588).
$$
原有理递推与独立模841递推、全椭圆方程窗、全矩阵幂等与回乘均通过。
没有调用 CM13 main/fiber，也没有以删列代替三维原像。

### 原始回执标识

- 本源码10492B，SHA256 cab3239b165056f2adcb7ff11ac24c6575f4f2c7060c821d87c7987de2734598。
- R798源码SHA256 f6a1fe72d01b0c804059a06395c5a9c5d78e54d5742a6ca9af957febec9661b3。
- R732源码SHA256 d1b3c2f851e9ec6b6d6b6655141e36b4bb1108a30e57ff8365b5f583d880e469。
- 原stdout4974B，SHA256 178ad5340edfc621e1443e1e91f7923cd1aaa2d1143e2b2e681a4951e44163fa。
- 全job日志14176B，SHA256 db584df49865d4a4c937fffe1ae3e32bc270a652f2b9b42d7568a6e2bff27a1d。

必要的完整六列及来源在此消费；原stdout、矩阵表和日志均不另存文件。§3所列小29整格、全toric比较和跨素数范围仍保。

## 5. 三条原 Hecke 线在 29 处的整归一与同时单位

下面只消费本次已返回的完整行，不重新计算 CM13。
设 $R$ 为 $K=\mathbf Q(\omega)$ 在 29 处的整数环，
$\mathscr V_4$ 为原六列
$b^{5-j}\sigma_b^{34}x_b^{3j}$ 所给的 $R$ 格，$b=17$。
原 $P_4$ 的分母只有 2 和 3，故
$\mathscr B_4=P_4\mathscr V_4$ 是秩三直和因子。

R798 的完整 $\mathcal A_{13}$ 在此格上为整算子。
这可直接从其几何定义核实，而不依赖拟合矩阵的某个分母表示：
$\gamma=4+\omega$ 的 degree13 同源在 $R$ 上有限 étale；
$[\gamma]^*\mathcal O(34O)$ 与
$[\bar\gamma]^*\mathcal O(34O)$ 间的原 Miller 同构
由 R798 的 $(\bar q/q)^{34}$ 给出，其原点首项是单位。
两个核在这个好模型上为 étale 除子，Miller 函数的零极正好
给这两个 pullback 除子之差。因此该同构在整模型上无垂直
分母，完整有限 trace 保持整截面格。
最后除以 $\gamma$ 仍为整操作，因为 $\mathrm N\gamma=13$。
这里使用的是原全部13纤维和原绝对相位；没有改用一个有理
对角化后可能失整的格。

R798 的特征零完整恒等式在该格约化为
$$
\mathcal A_{13}^3=-\omega I
\quad\hbox{于 }\mathscr B_4.
$$
$R$ 的剩余域为 $\mathbf F_{29^2}$。
因 $29^2-1=840$ 不被 9 整除，阶三元素 $\omega$
不是该域中的立方；而 $-1$ 是立方。
所以 $T^3+\omega$ 在 $\mathbf F_{29^2}$ 上不可约。
它在一个不分歧三次扩域中分裂，三个根均为单位且互异。
对每个根 $\mu$，原谱幂等元为
$$
e_\mu
=\frac{\mathcal A_{13}^2+\mu\mathcal A_{13}+\mu^2I}
       {3\mu^2}.
$$
分母为单位，所以这些幂等元保整格。
相对于 $R$ 的剩余 Frobenius
$\operatorname{Frob}_{29^2}$ 循环置换三个根，
并固定 $\mathcal A_{13},P_4$ 及原六列的系数。

取原 $Q_0=P_4E_{0,b}$。
其首 $z^4$ 系数为
$$
[z^4]Q_0=\frac{136}{13122}\in R^\times.
$$
三个 $[z^4]e_\mu Q_0$ 被上述 Frobenius 循环置换。
若其中一个约化为零，则三者都约化为零，
与它们的和为 $136/13122$ 矛盾。
因此三个原 $z^4$ 归一量全为单位；每个 $e_\mu Q_0$
亦非零。除以这个实际归一量所得截面，恰为 R806 已由
完整有限角色识别的 $D_{4,17},D_{10,17},D_{16,17}$，
不是本次重新按三个好位特征选择的线。

令 $r_{28}$ 为本次原 Taylor 行。
报告中公共 $17^4$ 尚未乘回的
$r_{28}P_4$ 第一坐标为 $20\pmod {29}$，故
$$
[z^{28}]Q_0\equiv17^4\cdot20\ne0\pmod {29}.
$$
同一 Frobenius 循环置换
$[z^{28}]e_\mu Q_0$。若一项为零，三项全为零，
与这个和矛盾。因此三个分子都是单位。
除以已经支付的三个首 $z^4$ 单位，严格得到
$$
[z^{28}]D_{j,17}\in R_j^\times
\qquad(j=4,10,16),
$$
其中 $R_j$ 是相应固定系数域在29处的整数环。
乘回 $28!$ 仍保持单位。

这个结论只针对固定29的原 Taylor/Hurwitz 读数。
它没有将普通 $\Omega_p$ 测度搬到惰性29，
没有预付 toric 平方中的29赋值，也不外推另一素数或
原巨大射线上的 Abel--Jacobi 配对。


## 6. 当前整行零的完整17维提升

本节仍是原 degree34 来源；它不添一条中央零，也不从固定29外推。
它把一般惰性 $p>34$ 的待排除条件准确提升到一个完整 Heisenberg 分量，
使以后使用全 theta 格时不必把原三维像误认成任意三个向量。
以下在原固定系数域的好整数环上进行，删去 $2,3,17$ 以及原有限 theta
相位的固定坏集。$b=1$ 与 $b=17$ 间仍只用已付的单位 homothety。

### 6.1 原三个半周期作用在全部34列上的关系

写
$$
\mathscr S_{34}
=\left\{\sigma(z)^{34}R(x(z),y(z)):
 R\in H^0(E,\mathcal O_E(34O))\right\}.
$$
它的完整基由 $1,x,\ldots,x^{17}$ 和
$y,xy,\ldots,x^{15}y$ 给出；偶部分18维、奇部分16维。
对 $e^3=-1$，保 R798 原绝对 lift
$$
U_e(\sigma^{34}R)
=\sigma^{34}(\delta e)^{-17}(x-e)^{17}
 R\left(e\frac{x+2e}{x-e},-\frac{3e^2y}{(x-e)^2}\right).
$$
这不是只在原六列上定义的算子。上式的 apparent pole 在全部34列上
都由 $(x-e)^{17}$ 消去，所以它保持整个整截面格。

直接作两次同一个变换有
$(x-e)(x(P+T_e)-e)=3e^2$，从而
$$
U_e^2=-I.
$$
两个不同非零二挠点的原 theta-group commutator 是
$e_2(T_e,T_f)^{17}=-1$，故
$$
U_eU_f=-U_fU_e\qquad(e\ne f).
$$
这里平方的负号已经由原倍率算出；不能再把这三个 lift
分别重相位为平方等于一的算子。

令
$$
S_2=\sum_{e^3=-1}U_e,\qquad
H_2=\frac{S_2-I}{2},\qquad
P_\omega=\frac{H_2-\omega^2I}{\omega-\omega^2}.
$$
以上全34列恒等式给
$$
S_2^2=-3I,\qquad H_2^2+H_2+I=0.
$$
每个 $U_e$ 被另一个 $U_f$ 共轭为其负，故其迹为零。
因此 $S_2$ 的两个特征 $\delta,-\delta$ 各有重数17；
$P_\omega$ 是一个秩17的整直和投影。

原 $\mu_3$ 作用循环置换三个 $U_e$，而原 $[-1]$ 与它们交换。
所以 $H_2,P_\omega$ 与原完整 $\mu_6$ 作用交换。
其 type4 部分恰为 R798 的原 $P_{B_4}$，不是另一条按维数挑出的子空间：
$$
P_{B_4}=\Pi_4P_\omega=P_\omega\Pi_4,
\qquad
\Pi_4=\frac16\sum_{\zeta\in\mu_6}\zeta^{-4}\rho_\zeta .
$$
在 type4 的六列上，以上式子也正是原
$(I-\omega H_2)/(1-\omega^2)$ 的归一。

### 6.2 原 $p-1$ 读者的严格等价

令 $p\equiv5\pmod6$，并记
$$
\ell_p(F)=F^{(p-1)}(0)\pmod p .
$$
$p-1<p$，所以同一 Taylor 行与这个 Hurwitz 行只差单位 $(p-1)!$。
由原 $\mu_6$ 型，
$$
\ell_p\rho_\zeta=\zeta^{p-1}\ell_p=\zeta^4\ell_p,
\qquad \ell_p=\ell_p\Pi_4 .
$$
故有完整的等价
$$
\boxed{\;
\ell_pP_{B_4}=0
\quad\Longleftrightarrow\quad
\ell_pP_\omega=0.
\;}
$$
右边是17维 whole 截面分量上的零 functional，
并非只在三个挑出的 eigenvector 上作数值观察。
它利用的是其余五种 $\mu_6$ 型由同一个读者自动杀掉。

对 $u\in E[17]$，取原 degree34 theta-group lift $\mathcal T_u$。
$E[17]$ 与 $E[2]$ 的 commutator 配对恒为一，因其阶同时整除17与2。
于是
$$
\mathcal T_uP_\omega=P_\omega\mathcal T_u .
$$
因此上述待排除的整行零条件还严格推出
$$
\ell_p(\mathcal T_uF)=0
\qquad
(F\in\operatorname{im}P_\omega,\ u\in E[17]).
$$
全部固定17-torsion/Miller 相位保留；这里只是一个线性
functional 的零核在其实际稳定群下的传播，未把中央 Mellin
读者或来源乘积赋为零。
限制到 $E[17]$ 的中心字符仍本原，秩17分量是原有限 Heisenberg
表示的一份完整不可约拷贝。因此对其中任意非零 $F$，
它的完整17挠译像张成同一个17维分量。

另对原 $F\in\operatorname{im}P_{B_4}$，三个二挠点的
$\mu_3$ 平均给准确的小式
$$
\Pi_4U_eF=\frac13S_2F=\frac{\delta}{3}F,\qquad
\ell_p(U_eF)=\frac{\delta}{3}\ell_p(F).
$$
这个末式的输入范围是原 type4 分量。
不能由它声称每个 $U_e$ 都保持整个17维
$\operatorname{im}P_\omega$；单个 Pauli 算子一般会混两个 dyadic 分量。

### 6.3 与三条原 Hecke 线以及热递推的范围

在 $p\equiv2$ 或 $5\pmod9$ 的上述好素数处，§5的同一整算子论证
逐字适用：$T^3+\omega$ 在 $\mathbf F_{p^2}$ 上不可约，
三个谱幂等元整且由 $\operatorname{Frob}_{p^2}$ 循环置换。
原 $z^4$ 归一量的和仍为单位 $136/13122$，故三条原
$D_{4,17},D_{10,17},D_{16,17}$ 的首项归一全为单位。
因此在这个精确范围内，
$$
\ell_pP_{B_4}\ne0
\quad\Longleftrightarrow\quad
[z^{p-1}]D_{j,17}\text{ 对三个 }j\text{ 全为单位}.
$$
证明反向的零条件时须用整条 functional：任一原 eigenline
上的值若为零，其 Frobenius 共轭全零，便杀掉整个三维像。
不要求一般 $p$ 的单一 $Q_0$ trace 值本身非零，
也不把 $p\equiv8\pmod9$ 的分裂情形混入三循环论证。

本节没有证明左边在无穷多个 $p$ 非零。
它也没有把一个首块行零改成全 $p$ 可积性。
例如 R856 的完整递推在原偶 type4 源上准确给
$$
j_{7p-1}(F)
=(34c_p)^6(p-1)_6\,j_{p-7}(F)\pmod p,
\qquad j_k(F)=F^{(k)}(0).
$$
$(p-1)_6$ 是单位；此前的 $2p-1,\ldots,6p-1$ 槽由型为零，
但 $\ell_pP_\omega=0$ 本身尚不控制 $j_{p-7}P_\omega$。
所以全17维提升是下一步真实可用的有限群零核，
而不是已经支付的零 $p$-curvature、全 Cartier 零或跨素数非零定理。


## 7. 原半周期平均的完整二阶算子与真实六阶块

本节继续同一个原 $b=1$、degree34、半周期 lift；没有新数学执行。
它给一个实际保持 dyadic 分量的微分算子，而不是把裸 $D_z^2$
误认作保持原 theta 空间。普通或惰性来源的 Mellin 零均未因此传播。

### 7.1 四元共轭平均

在完整偶部分
$\sigma^{34}K[x]_{\le17}$，先对 rational factor 取
$$
L=D_z^2-1190x,\qquad D_zx=2y,\quad D_zy=3x^2.
$$
因为
$$
D_z^2x^a=2a(2a+1)x^{a+1}+4a(a-1)x^{a-2},
$$
最高 $x^{18}$ 项在 $a=17$ 时准确抵消，所以 $L$ 保持全部18列。
令 $\mathcal L=\sigma^{34}L\sigma^{-34}$。
沿§6的原 $U_e$，置 $j_e=y/(x-e)$。
完整 sigma 倍率给
$$
U_eD_zU_e^{-1}=D_z-34j_e
$$
（此式在 rational-factor 表示中读取），从而
$$
U_eLU_e^{-1}
=D_z^2-68j_eD_z+1122x+1156e.
$$
最后的潜在简单极确实相消：
$$
\frac{1224(x^2+ex+e^2)-102x^2-1190e(x+2e)}{x-e}
=1122x+1156e.
$$
这一步保留了原半周期 multiplier，不能只平移势函数 $x$。

用 $\sum e=0$、$\sum j_e=3x^2/y$，四元平均成为
$$
\boxed{
\begin{aligned}
\mathcal B
&=\frac14\left(\mathcal L+\sum_{e^3=-1}
                    U_e\mathcal L U_e^{-1}\right)
 =\sigma^{34}B\sigma^{-34},\\
B&=D_z^2-\frac{51x^2}{y}D_z+544x\\
 &=4(X+1)\partial_x^2-96x^2\partial_x+544x,\qquad X=x^3 .
\end{aligned}}
$$
即
$$
\boxed{B(x^a)=4(a-17)(a-8)x^{a+1}
                  +4a(a-1)x^{a-2}.}
$$
所以所有 apparent poles 已在整个偶截面格上支付。
原 Pauli lift 的共轭群恰为四元 Klein 群；以上完整平均严格与
每个 $U_e$ 交换，因而与 $H_2$、$P_\omega$ 交换。
它还将原 $\mu_6$ 型降低2；所以 $\mathcal B^3$ 保持原 $P_{B_4}$。
这里没有对奇16维声称 $L$ 保持，也没有以某个自由
differential operator 代替已给的共轭平均。

### 7.2 同一个 PB4 上的实际三列矩阵

低多项式空间 $K[x]_{\le8}$ 被 $B$ 保持。
令 $Q_j=P_{B_4}(\sigma^{34}x^{3j})$，$j=0,1,2$；
这是 R798 的三条原投影基。
由于 $\mathcal B^3$ 与完整 $P_{B_4}$ 投影交换，直接三次使用上面的两项式就给
$$
\boxed{
[\mathcal B^3]_{Q_0,Q_1,Q_2}
=1024
\begin{pmatrix}
1904&189&45\\
85680&13055&5130\\
0&8190&6359
\end{pmatrix}.
}
$$
例如
$$
B^3(1)=1949696+87736320x^3,
$$
$$
B^3(x^3)=193536+13368320x^3+8386560x^6,
$$
$$
B^3(x^6)=46080+5253120x^3+6511616x^6.
$$
因此矩阵来自完整 polynomial 回乘，不是由若干 Taylor jet 拟合。
原 $b=17$ 可沿既定单位 homothety 返回；本节不另选 period。

该矩阵不与原 CM13 同时谱对角化。
对除以1024后的矩阵 $C$，手算特征多项式为
$$
\chi_C(T)=T^3-21318T^2+61772781T-6670664000.
$$
在好素数11处，它化为 $T(T^2+4)$，在 $\mathbf F_{121}$ 中有
三个不同根。原 CM13 的 $T^3+\omega$ 在同一域不可约，因为
$\mathbf F_{121}^{\times}$ 的阶120不被9整除。
原两算子与原投影在11整；若它们交换，则 $C$ 的约化属于
不可约 CM13 算子的中心化域 $\mathbf F_{121^3}$。
该域中一个元素在基域上的次数只能为1或3，不能有三个不同
基域特征值。这给出矛盾。
故不能把本节的六阶方程分拆成三条原 CM13 eigenline 的
独立 Lamé 方程。

### 7.3 原 sigma frame、首窗与 canonical 来源

对实际 entire section，完整算子是
$$
\mathcal B
=\partial_z^2
 -\left(68\zeta+\frac{51x^2}{y}\right)\partial_z
 +1156\zeta^2+\frac{1734\zeta x^2}{y}+578x.
$$
因 $\zeta=z^{-1}+O(z^5)$、$x^2/y=-z^{-1}+O(z^5)$，
其准确 indicial 部分为
$$
\mathcal B=\partial_z^2-\frac{17}{z}\partial_z
            +O(z^5)\partial_z+O(z^4).
$$
所以 $\mathcal B^3$ 在首项 $z^m$ 上的 indicial 因子为
$$
m(m-18)(m-2)(m-20)(m-4)(m-22).
$$
type4 的4与22两处初始分支都必须保留。
特别在 $m=p-1$ 的读者中，$\zeta$ 的原第一非整系数以及
$p$ 位的真实除法仍须按 R855/R856 处理；
不能把本式的首部改成一个整的裸六次导数来迫 $r_{p-1}$ 非零。

还有一条可直接交给原 canonical 读者的固定来源身份。
取 R297 的同一个 $S$，其 dyadic 型为另一条 $\omega^2$。
写 $\nabla_{34}=\partial_z-34\zeta$。
由于 $\mathcal B$ 保 dyadic 分量，
$$
\boxed{
P_{B_4}\nabla_{34}^2S
=P_{B_4}\left(\frac{51x^2}{y}\nabla_{34}S-544xS\right).
}
$$
两边都是原完整整截面：$\nabla S=\sigma^{34}D_zR_S$ 含 $y$，
所以显示的分母不留极。未经投影的 $\nabla^2S$ 在原
$\sigma^{34}(1,X,\ldots,X^5)$ 六列中准确为
$$
\frac17(-1024,-8960,-11488,-26584,-21722,5684).
$$
其首项是 $812z^4$。

这个身份不等于 canonical 首 Tate 必要行。准确地，
$$
\nabla^2S=S''-68\zeta S'+(1156\zeta^2+34x)S,
$$
而惰性原 R856 只自动给
$j_{p+1}(S)=34c_p\,m_0(S)=0\pmod p$。
原 canonical 首窗还读它的真实除 $p$ 量及其完整低卷积；
不能将这一自动一阶整除代成 $r_{p-1}(P_{B_4}\nabla^2S)=0$。
本节支付了原有限二阶算子、完整三列矩阵和这些实际来源关系，
跨 $p$ 非零或原中央强迫仍要在同一个完整读者中完成。
