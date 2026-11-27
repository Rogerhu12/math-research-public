# R1007 — 原十三等变 Cartier 模型、完整 Gaussian 比较与实际核读数

日期：2026-11-27 UTC。**已证明：从原指定 $P_{10}$ 构造的两个 degree130 模型，分别与整个 $\pi$、$\bar\pi$ 核的 canonical Miller 平移严格交织。它们与原中央的完整 Newton 比较保留一个明确的 Gaussian 参数；质量零时中央导数准确不变。原十三核在真实第一 Cartier 读者中的全部贡献，可以由 R1004 已返回的两坐标六 jet 完整计算；该处没有残留 exact 层。**

剩余的两个 exact 层及留数只支撑在明确的 $E[2\pi]$ 或 $E[2\bar\pi]$ 上。下面给所有支撑、极帽、原两层有限部和真实第六块的完整等式，不将新的固定支撑替代原中央非零量词。

## 1. 原十级模型及完整十三下降

沿 R887/R978/R1005 固定

$$
E_1:y^2=x^3+1,\quad X=x^3,\quad
\pi=(7+\delta)/2,\quad\delta^2=-3,
\quad p=6s-1>211.
$$

原 $Z,G,H$ 不变。对 $a=10$ 使用同一有限定义

$$
P_{10}=-(D-10G)^{p-1}Z^{p+9},\qquad
(D-10G)P_{10}=10H^pZ^{p+9}.
\tag{1}
$$

R887(68)–(71)的证明对任意固定正偶 $a<p$ 逐字成立，所以这里没有新增一个初始选择。写

$$
R_\pi(X)=X^2+(2+6\delta)X+(40+24\delta)/13,
\qquad \sigma(\pi z)=\pi\sigma(z)^{13}R_\pi(X).
$$

定义原有理函数

$$
\boxed{\mathscr P_{\pi,p}(z)
=\frac{P_{10}(\pi z)}{\pi^{10}R_\pi(X(z))^{10}},
\qquad Z_{\pi,p}(z)=\frac{Z(\pi z)}\pi.}
\tag{2}
$$

其中 $DZ_{\pi,p}=1$，且 $\mathscr P_{\pi,p}$ 在 $O$ 的阶准确为130。
对 $f=\sigma^{130}R_f$ 定义

$$
\boxed{\eta_\pi(f)=Z_{\pi,p}^{-7}\mathscr P_{\pi,p}R_f\omega_E.}
\tag{3}
$$

另一支全部取原复共轭，不另选 $\pi$、Gauss 根或 theta 相位。

对每个 $T\in\ker\pi$，R993 的原 Miller 函数是
$a_T=R_\pi(X)/R_\pi(X\circ t_T)$，并且
$T_Tf=\sigma^{130}a_T^{10}(R_f\circ t_T)$。式(2)直接给

$$
\boxed{Z_{\pi,p}\circ t_T=Z_{\pi,p},\qquad
\mathscr P_{\pi,p}\circ t_T
=a_T^{10}\mathscr P_{\pi,p},\qquad
\eta_\pi(T_Tf)=t_T^*\eta_\pi(f).}
\tag{4}
$$

这是每个真实 $T$ 上的全微分身份，不只比较质量或一个局部 jet。
原单 $P_{130}$ 的 $W_T,\kappa_T^p$ 没有被(4)删除；它们被换成下面明确支付的两个模型比较。

## 2. 与原 Gaussian 的全 Tate 身份

令 $d=p+1$、$c=[z^d]\log(\sigma/z)$，始终先在原特征零整窗中形成
$\sigma^\circ=\sigma e^{-cz^d}$。因为惰性 $p$ 下 $\pi^p\equiv\bar\pi\pmod p$，有

$$
q_\pi=\frac{\pi^d}{13}\in1+p\mathcal O,\qquad
\gamma_\pi=10c(\pi^d-13)\in\mathcal O.
\tag{5}
$$

这里 $v_p(c)=-1$。因此 $\gamma_\pi$ 不必模 $p$ 为零，更不能因为括号含 $p$ 就删掉它。
原 sigma division 给准确的整局部身份

$$
\frac{\sigma^\circ(\pi z)^{10}}
     {\pi^{10}R_\pi(X(z))^{10}}
=(\sigma^\circ(z))^{130}e^{-\gamma_\pi z^d}.
\tag{6}
$$

定义适配读者 $J_f^{(\pi)}$ 时，用 $10c\pi^d=130cq_\pi$ 代替原 $130c$，其它来源与系数读取完全不变。在非负整数 $n$ 上两边精确为

$$
J_f^{(\pi)}(n)
=n!(130cq_\pi)^{-n}[z^{dn}]f
=q_\pi^{-n}J_f(n).
$$

这些是 R978/R989 同一原 Tate 域中的函数：对质量零的完整来源，乘 $e^{-\gamma_\pi w^s}$ 保留原整 Hurwitz 界；对本篇实际质量非零轨道，R987 的全来源分解直接落在原 $\Phi_*,D_\pi\Psi,D_{\bar\pi}\Psi$ 的已付 Tate 域中。
非负整数稠密，故

$$
\boxed{J_f^{(\pi)}(v)=q_\pi^{-v}J_f(v),\qquad
j_f^{(\pi)}=j_f-m_0(f)\log_pq_\pi.}
\tag{7}
$$

特别对 $\Phi_*,\Phi_{260},\mathcal K,\mathcal C_{130}$ 等质量零源，$j_f^{(\pi)}=j_f$ 是完整身份；不是只比较模 $p$。

### 2.1 两个实际半轨道不能混用 Gaussian

R987 的两正轨道有真实质量 $m_M,m_U$，并且

$$
\frac{j_{\mathcal U_+}}{m_U}
-\frac{j_{\mathcal M_+}}{m_M}
=\frac34d\log_p(\pi/\bar\pi)+C_{13}j_{\Phi_*}.
$$

分别在 $\mathcal M_+$ 用 $\pi$ 适配、在 $\mathcal U_+$ 用 $\bar\pi$ 适配，(7)给

$$
\boxed{\frac{j_{\mathcal U_+}^{(\bar\pi)}}{m_U}
-\frac{j_{\mathcal M_+}^{(\pi)}}{m_M}
=\frac74d\log_p(\pi/\bar\pi)+C_{13}j_{\Phi_*}.}
\tag{8}
$$

此处的额外一份对数正是两个适配 Gaussian 的实际差；它不被惯性 Frobenius 自动置零。
同样

$$
\gamma_\pi-\gamma_{\bar\pi}
=10c(\pi^d-\bar\pi^d)
\tag{9}
$$

保留原 Lucas 差与原除 $p$，其完整深度按 R1000。

## 3. K/C 的真实前六块与原读者

本节取 $f\in V_{130}^{\ge12}$，特别包括 R1005 的 $\mathcal K,\mathcal C_{130}$。令

$$
g_h(f)=[z^{hd}]e^{-130cz^d}f,\qquad
g_h^{(\pi)}(f)=[z^{hd}]e^{-130cq_\pi z^d}f.
$$

准确的三角变换是

$$
\boxed{g_h^{(\pi)}(f)=
\sum_{r=0}^h\frac{(-\gamma_\pi)^r}{r!}g_{h-r}(f)
\qquad(0\le h\le6).}
\tag{10}
$$

所有显示阶乘是单位。这里 $g_0(f)=0$，所以 $h=6$ 只需 $r\le5$。
由 R887(106)在 $a=10$ 的同一证明，$P_{10}/(\sigma^\circ)^{10}-1$ 从 $z^{6p}$ 起；乘上起阶至少12的 $f$ 后，第一次可能误差在 $6p+12$，严格高于第六目标 $6p+6$。
因此(2)的前六块真正读取(10)，不附加一个未知 $e_{10,p}$ 或 $e_{130,p}$。

原参数运输仍有准确首差

$$
Z_{\pi,p}=z-\kappa_5\pi^{5p-1}z^{5p}+O(z^{11p}).
\tag{11}
$$

记 $a^+(f)=[z^{p+7}]e^{-130cz^d}f$。因 $[z^6]f=0$，乘(6)的指数不改变这一量。故真实适配第六读者满足

$$
\boxed{\mathcal T_{6,\pi}(f)
:=[Z_{\pi,p}^{6p+6}]\mathscr P_{\pi,p}R_f
=\overline{g_6^{(\pi)}(f)}
 +7\kappa_5\pi^{5p-1}\overline{a^+(f)}.}
\tag{12}
$$

于是原 $P_2^{65}$ 第六行准确为

$$
\boxed{\begin{aligned}
\mathcal T_6(f)=\mathcal T_{6,\pi}(f)
&-\sum_{r=1}^5\frac{(-\overline\gamma_\pi)^r}{r!}
                      \overline{g_{6-r}(f)}\\
&+7\kappa_5(1-\pi^{5p-1})\overline{a^+(f)}.
\end{aligned}}
\tag{13}
$$

这是同一模 $p$ 行的完整比较；本节的横线表示模 $p$ 约化，不表示 CM 共轭。它在六位中央中只能替换最后乘 $p^5$ 的项；前五项仍须读原全部六位精度。
若用整个适配六项读者，则分母也须逐项保 $q_\pi^h$；(7)保证所得仍读原 $(a/p)j_f$，并不允许只改第六项而不支付(10)、(13)。

## 4. 全部固定支撑与原 y-map

记 R978 原 $x$-map 为

$$
x(\pi z)=\frac{xA_\pi(X)}{\pi^2R_\pi(X)^2}.
$$

直接对它求导给

$$
\boxed{y(\pi z)
=\frac{yB_\pi(X)}{\pi^3R_\pi(X)^3},\qquad
B_\pi=(A_\pi+3XA_\pi')R_\pi-6XA_\pi R_\pi'.}
\tag{14}
$$

完整六次多项式是

$$
\begin{aligned}
B_\pi(X)={}&X^6+(78+378\delta)X^5
 +(17520-1728\delta)X^4\\
&+(16832-10368\delta)X^3
 +(-34176+3456\delta)X^2\\
&+(-49152-27648\delta)X+4096.
\end{aligned}
\tag{15}
$$

它的固定值 $B_\pi(0)=4096$、$B_\pi(-1)=3^9(1+2\delta)$ 与原局部相位相符。全部非零二挠的逆像是 $yB_\pi=0$：三个原二挠点，加六个真正六点轨道。
在 $2,3,13$ 外，$[\pi]$ 及这些挠点纤维 étale，$B_\pi$ 的六根互异，且与 $R_\pi$、$X+1$ 不交。
两支的 $B_\pi,B_{\bar\pi}$ 也不交：一个共同点将同时被 $2\pi$、$2\bar\pi$ 杀掉，因 $(\pi,\bar\pi)=1$ 只能是已从这两个多项式中删除的二挠点。

对(3)，所有其它 $Z_{\pi,p}$ 零点由 $P_{10}\circ[\pi]$ 的至少 $p$ 阶零完整抵消。在每个非零十三核点，$P_{10}(\pi z)$ 的十阶零准确抵消 $R_\pi^{10}$ 的十阶零；所以输入仅可能有七阶极。
在 $E[2\pi]\setminus\ker\pi$，原单 $P_{10}$ 极帽及 $Z_{\pi,p}^{-7}$ 给

$$
\boxed{d_{10,p}=p^3-p^2+2p+1<p^3.}
\tag{16}
$$

故整个三次 Cartier 的极均简单，且只在这个先于 $p$ 固定的52点集合内。没有只保十三核而删掉 $E[2\pi]$。

对 principal 来源，下降到 $t=-x^{-3}$ 后固定支撑为：$O$ 对应 $t=0$，两个 $R_\pi$ 根，原二挠点对应 $t=1$，以及六个 $B_\pi$ 根。共十个 quotient 点；三次输出属于由这些点决定的九维对数微分空间。
对 $\mathcal K,\mathcal C_{130}$，$O$ 本来正则，故至多八维；没有额外不变正则微分。

## 5. 十三核的真实第一 Cartier 贡献已全部固定

在非零 $T\in\ker\pi$ 附近，以 $z-T$ 为原微分参数。(4)及所有低窗相容性给

$$
\operatorname{Res}_T\eta_\pi(f)=c_6(T_Tf).
\tag{17}
$$

这里是**第六 jet**，不是质量。R1004 的完整消费者已经对全部22列、两条核、每个根和原独立 trace 支付它。
原三次输出在这些点的留数准确为 $c_6(T_Tf)^{1/p^3}$。

更强的是，第一个 Cartier 已杀掉该处所有二至七阶主部，因为 $p>7$；所以十三核不贡献任何 exact 层。令

$$
b_\pi(f)=A_f+B_fX\in k[X]/R_\pi
\tag{18}
$$

表示 R1004 的这两个真实 $c_6$ 值，记二次迹为 $t_f=\operatorname{Tr}_{R_\pi}b_\pi(f)$。
在 $t$ 坐标中该点为 $a=-1/X_T$，$dt/\omega_E=-6z^5+\cdots$。把整个两点对数部分读回原点并最后取 $p$ 次方，得到真正的第六行贡献

$$
\boxed{\mathcal N_{\pi,p}(f)
=-6\operatorname{Tr}_{R_\pi}\{X^p b_\pi(f)\}.}
\tag{19}
$$

因此这里不再有一个未返回的高 kernel jet。

### 5.1 原 Frobenius、Gauss 根及两个固定类型

沿 R987 保 $g^2=13$ 的原 Gauss 根。置

$$
\epsilon_p=\pi^{(p+1)/2}/g\in\{1,-1\},\qquad
e=X+1+3\delta,\qquad e^2=-108/\pi.
$$

原惰性 Frobenius 给

$$
\boxed{X^p=-1+3\delta-\epsilon_p(\pi/g)e.}
\tag{20}
$$

例如由 $e=6\delta/\sqrt\pi$、$(\sqrt\pi)^p=\epsilon_pg/\sqrt\pi$ 直接得到；原选根和 $g$ 始终一起保留。
因为 $\operatorname{Tr}(e b_\pi)=-216B_f/\pi$，(19)变成

$$
\boxed{\mathcal N_{\pi,p}(f)
=6(1-3\delta)t_f-\frac{1296\epsilon_p}{g}B_f.}
\tag{21}
$$

它只含已返回的两坐标和一个明确的 Frobenius 符号。这里没有用复共轭代替全部 Frobenius：另一支同时保
$g^p=(13/p)g$ 与 $\epsilon_{\bar\pi,p}=(13/p)\epsilon_p$。

### 5.2 实际 K/C 的完整两坐标

R1004 的原完整 run 返回

$$
\begin{aligned}
b_\pi(\mathcal K)={}&
-\frac{1852933}{11340}-\frac{85237}{68040}\delta\\
&+\left(-\frac{402721}{181440}
       +\frac{2517343}{544320}\delta\right)X,\\
b_\pi(\mathcal C_{130})={}&
\frac{376249}{11340}-\frac{757409}{68040}\delta\\
&+\left(\frac{1164103}{181440}
       -\frac{1157269}{544320}\delta\right)X.
\end{aligned}
\tag{22}
$$

其实际二次迹是

$$
t_{\mathcal K}=-401707/1680+25\delta/16,
\qquad
t_{\mathcal C}=25631/1680-8137\delta/144.
\tag{23}
$$

完整两个坐标的行列式为

$$
d_6=-\frac{25996646899}{22861440}
       +\frac{14624773}{90720}\delta\ne0.
\tag{24}
$$

固定地删除 $N_{K/\mathbf Q}(d_6)$ 分子素因子后，它们在整个二次代数中构成基。式(19)是非零泛函，因为 $X$ 是单位且该代数 étale，迹配对非退化。
所以对每个这样的好 $p$，两个**真实核贡献** $\mathcal N_{\pi,p}(\mathcal K),\mathcal N_{\pi,p}(\mathcal C)$ 至少一个非零。这是(21)的完整实际消费；不是把其中任一核贡献认成整个中央导数。

特别，即使坏 canonical 假设使 $j_{\mathcal K}=0$，(23)仍给适配三次 Cartier 的非零十三留数（另排其固定范数坏集）。因此原单 $P_{130}$ 对 $\mathcal K$ 的三次零不能无修正地迁到本篇模型。

## 6. 剩余 E[2π] 两层 exact 的完整原点读回

以下仍取 $f=\mathcal K$ 或 $\mathcal C_{130}$。令 $\mathcal S_{2,\pi}$ 为 $t=1$ 及六个 $B_\pi$ 根对应的七个 quotient 点；对 $a\in\mathcal S_{2,\pi}$ 记 $x_a=-1/a$ 为对应的 $X$ 值。
将实际(3)的整条主部写成

$$
\sum_{n=1}^{L_a} c_{a,n,p}(f)(t-a)^{-n}dt,
\qquad r_{a,p}(f)=c_{a,1,p}(f).
\tag{25}
$$

这由原(1)–(3)唯一确定。对六个一般点可取 $L_a=d_{10,p}$；在 $a=1$ 处，R1005 的原 $(X+1)^2$ 因子给

$$
L_1=(p^3-p^2+2p-2)/2.
\tag{26}
$$

设 $Y_a=(t-a)^{-1}$。定义

$$
H_{0,a}(Y)=\sum_{\substack{j\ge1\,,\ p\nmid j\\1+jp\le L_a}}
 \frac{c_{a,1+jp,p}(f)^{1/p}}j
 \{Y^j-x_a^j\},
$$

$$
H_{1,a}(Y)=\sum_{\substack{j\ge1\\1+jp^2\le L_a}}
 \frac{c_{a,1+jp^2,p}(f)^{1/p^2}}j
 \{Y^j-x_a^j\}.
\tag{27}
$$

一般六点的两个上限分别是 $p^2-p+2,p-1$；原二挠点的两个上限是 $p(p-1)/2,(p-1)/2$。所有实际除数为单位，且没有第三 exact 多项式，因为全部 $L_a<p^3$。
原点对应 $Y_a(O)=x_a$；(27)仅固定原函数常数，不将其导数赋零。

把每一个主部先施第一 Cartier，再读 $z^5\omega_E$ 系数，逐项得到完整原第六行：

$$
\boxed{\begin{aligned}
\mathcal T_{6,\pi}(f)={}&\mathcal N_{\pi,p}(f)
-6\sum_{a\in\mathcal S_{2,\pi}}x_a^p r_{a,p}(f)\\
&-6\sum_{a\in\mathcal S_{2,\pi}}
 \left\{x_a^{2p}H_{0,a}'(x_a)^p
       +x_a^{p^2+p}H_{1,a}'(x_a)^{p^2}\right\}.
\end{aligned}}
\tag{28}
$$

证明保留所有权：$dt/(t-a)$ 在 $O$ 的 $z^5$ 系数为 $6/a$，而
$dY_a/\omega_E=6/a^2\,z^5+\cdots$。第一 exact 与其 Cartier 提升依次产生 $x_a^{2p}$、$x_a^{p^2+p}$，不能把它们一律改成1。
十三核仅贡献(19)；$O$ 无主部，$t=\infty$ 正则，不存在额外多项式部分。

还可用整个留数定理准确消去原二挠的留数 $r_{1,p}$：

$$
r_{1,p}(f)=-t_f-\sum_{a\in\mathcal S_{2,\pi}\setminus\{1\}}r_{a,p}(f).
\tag{29}
$$

因此(28)的留数部分也等于

$$
-6\operatorname{Tr}_{R_\pi}\{(X^p+1)b_\pi(f)\}
-6\sum_{a\ne1}(x_a^p+1)r_{a,p}(f),
\tag{30}
$$

其中第一个已知项明确为
$-18\delta t_f-1296\epsilon_pB_f/g$。这只消去一个真实留数；两个 exact 层仍是(28)的全部七点和。

## 7. 全十三 trace 的原两列返回

记 $D_\pi h=h(\pi z)$ 为原 raw pull，$\mathsf Q_\pi$ 为 R987 的完整 canonical deck 平均。若
$\mathsf Q_\pi f=D_\pi h_\pi(f)$，则由(4)与(2)直接有

$$
\boxed{[\pi]_*\eta_\pi(f)
=13\pi^6\,Z^{-7}P_{10}R_{h_\pi(f)}\omega_E.}
\tag{31}
$$

写 $u_0=\sigma^{10}x^2,u_1=\sigma^{10}x^5$。R992 的整个两列矩阵是

$$
N_\pi=
\begin{pmatrix}1/3&20/3\\1/12&1/6\end{pmatrix}
+\delta\begin{pmatrix}-2/9&20/9\\1/36&-5/18\end{pmatrix}.
$$

置 $A_\pi=I-\pi N_\pi/13$，则原完整关系
$\mathsf Q_\pi D_{\bar\pi}=(\pi/13)D_\pi N_\pi$ 给

$$
h_\pi(\mathcal X_{130})
=\frac{A_\pi u_0}{2520\delta}.
\tag{32}
$$

两 primitive 的 $h_\pi$ 为零；R978 的完整
$F_{10}=-11\Phi_*/2+\delta(D_\pi-D_{\bar\pi})\Psi_{125}/10080$
给

$$
h_\pi(F_{10})=\frac{\delta}{10080}A_\pi(u_1-8u_0).
\tag{33}
$$

代 R1005 原 $\mathcal K,\mathcal C$ 的固定系数后，整个两列返回明确为

$$
\boxed{\begin{aligned}
h_\pi(\mathcal K)&=\frac{9\delta}{280}A_\pi u_0,\\
h_\pi(\mathcal C_{130})
&=-\delta A_\pi\left(\frac{u_0}{40}+\frac{u_1}{112}\right).
\end{aligned}}
\tag{34}
$$

这两个源构成完整 $S_{10}$ 的基。事实上
$N_\pi\Psi_{125}=\omega^2\Psi_{125}$、
$N_\pi\Psi_{12500}=\Psi_{12500}$，所以

$$
\det A_\pi=(1-\pi\omega^2/13)(1-\pi/13)
=\frac{4(34+3\delta)}{169},\qquad
N_{K/\mathbf Q}(\det A_\pi)=\frac{112}{169}.
$$

而(34)在 $A_\pi u_0,A_\pi u_1$ 基中的行列式为
$27/31360$。故对本篇所有 $p>211$，这个下层返回本身不损失任何两列信息。

更直接的原算术本征基表达是：置
$a_\pi=1-\pi/13,b_\pi=1-\pi\omega^2/13$，则

$$
\begin{aligned}
h_\pi(\mathcal K)
&=\frac{\delta}{560}
   (a_\pi\Psi_{12500}-b_\pi\Psi_{125}),\\
h_\pi(\mathcal C_{130})
&=-\frac{\delta}{560}
   (3a_\pi\Psi_{12500}+2b_\pi\Psi_{125}).
\end{aligned}
\tag{35}
$$

因此 $3h_\pi(\mathcal K)+h_\pi(\mathcal C)
=-\delta b_\pi\Psi_{125}/112$，
$2h_\pi(\mathcal K)-h_\pi(\mathcal C)
=\delta a_\pi\Psi_{12500}/112$。
式(31)、(34)同时控制七个 $E[2\pi]$ 点在每一个原二挠纤维上的全部主部返回；不只是控制十三核的总迹。

### 7.1 原第六窗口及两 exact 的准确下推

以
$\mathcal T_{6,10}(h)=[Z^{6p+6}]P_{10}R_h$
记同一个 degree10 原有限读者；对每个真实平移，仍以(12)左边的有限有理函数定义 $\mathcal T_{6,\pi}$，不预先用质量零的右边比较。
由 $\sum_TT_Tf=13D_\pi h_\pi(f)$ 与(2)逐项得到

$$
\boxed{\sum_{T\in\ker\pi}
 \mathcal T_{6,\pi}(T_Tf)
=13\pi^{6(p+1)}\mathcal T_{6,10}(h_\pi(f))
=13^7\mathcal T_{6,10}(h_\pi(f)).}
\tag{36}
$$

第一等式的因子来自
$Z_{\pi,p}=Z(\pi z)/\pi$，第二等式在特征 $p$ 中使用
$\pi^{p+1}=13$。所以(36)确实把(28)七点的两层 exact 与所有留数一起送回原 degree10 的完整第六窗；并非只使它们的三次 Cartier 留数相等。
当 $T\ne0$ 时，$T_Tf$ 通常有质量或第六系数，不能对它再无条件套用(13)的零修正规范。

### 7.2 完整 Tate trace 及 canonical 零值的准确范围

在原特征零 Tate 域中，整个有限 trace 的真实身份为

$$
\boxed{J^{(\pi)}_{\sum_{T\in\ker\pi}T_Tf}(v)
 =13J_{10,h_\pi(f)}(v).}
\tag{37}
$$

证明只用完整来源 $\sum_TT_Tf=13D_\pi h_\pi(f)$：
原 $J_{130,D_\pi h}(v)=q_\pi^vJ_{10,h}(v)$，再施(7)便得(37)。
这里左边作为整个已付 trace 来源读取；不需要先假定任意一个未投 principal 的单点平移拥有额外中央性质。
尤其(37)的导数是(35)所给两个真实 rank0 本征源的导数。
无权 trace 零对两 primitive 本来就是 R987 的有限表示事实；canonical 坏假设只给原 $j_\mathcal K=0$，没有给所有 $T_T\mathcal K$ 的和为零。
因此(34)–(37)是两个 exact 的真实完整下降，不能把它们改写成下层 $S_{10}$ 全中央消失。

## 实际来源与接续范围

式(22)–(24)取自 R1004 的原完整公开执行：run `45916324833`、job `140236318135`、source `56f5c405d885932a9d8b213a5cdb431376fa2ea3`；该篇保全部22列、两核、原独立 trace 门及完整 SHA。
本篇没有数学执行或新生成数据文件；(14)–(16)、(20)–(21)及全部模型/Cartier身份由显示公式手证。

现在(13)、(21)、(28)把原第六读者分成一个实际已算的十三核项、明确七点上的两个 exact 及留数、和原 Gaussian/低卷积修正。坏 canonical 时，$j_{\mathcal K}=0$ 而
$j_{\mathcal C_{130}}=-\delta(p+1)\log_p(\pi/\bar\pi)/112\ne0$；要消费这个对照，仍须在同一完整式里处理(28)七点的原实际函数，不能只比较已固定的十三核项。
