# R308：真正导数 rank-two 的弱单 hook 圆及完整三阶实现

日期：2026-11-15。**独立纸面构造与原 range 支付。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R306](R306-derivative-rank-classification-and-overlapping-profile-Gaussian-obstruction.md) 证明了实紧光滑类中的准确分类
$$
\mathfrak H(g;f,f)=\mathfrak H(f;g,g)=0
\quad\Longleftrightarrow\quad
g'f''-f'g''=0.
$$
固定 seed 的原三阶周期并不要求左边两式同时成立。本稿利用这一严格差别，构造三矩非退化圆，使
$$
\mathfrak H(g;f,f)=0,\qquad
g'f''-f'g''\not\equiv0,\qquad
\mathfrak H(f;g,g)\not\equiv0.
\tag{1}
$$
继而准确支付它的完整三阶 ruling，并在同一个真实几何和同一个新选目标度量上得到全部相位的三阶 Taylor 等距圆。

这不是仅解一个退化 ODE：共同右锚、左右零 collar、三复矩、交叉二阶 forcing、实际三阶周期以及全部逐 ruling 条件均在下面支付。也不声称已满足任何完整第四周期或第四 ruling。R306 对双 hook 平面的正障碍不能直接用于 (1)；这只划清其适用范围，并不把“该障碍不适用”当成第四可解。

主要来源：[R181 原退化方程及通量](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md)、[R46 真实恢复、局部化及七次有限差分](R46-eight-packet-complete-third-order-circle.md)、[R52 交叉二阶通道及完整四槽 ruling](R52-overlapping-profile-plane-complete-third-order-circle.md)、[R183 三复矩补偿与任意基本 packet 的八副本](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R210 实际闭 hook 与完整 pure 支付](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md)、[R250 弱 hook 的准确相位范围](R250-complete-circle-Gaussian-area-and-nonuniform-profile-cancellation.md)及 R306。

## 1. 固定真实几何与本稿要付的条件

先固定一条此前已实际构造的光滑闭 hook 几何 $X$，满足
$$
M=0,\qquad T=\kappa_H\mathfrak H,\qquad \kappa_H\ne0.
\tag{2}
$$
它的真实有限词、所有基准段、frame、位置闭合与 $s$ 周期都保持。取其一个非空合法 profile 活动开区间 $I^\circ$，左右留公共零 collar，固定右锚 $r_*$：
$$
Jq(x)=\int_x^{r_*}q(t)\,dt.
$$
下面的所有 profiles 都紧支撑于 $I^\circ$。构造可以缩小到任意给定的非空活动子区间，不要求扩大一个已经冻结的物理区间，也不改变几何的任何分母。

若所选几何还具有已安装的特殊端芽、Morse 条件或 universal whole-pure 恒等，本稿仅改变 profiles，因而保留这些几何性质；本稿的三阶论证不使用它们，也不由 whole-pure 恒等删掉平台或第四尾。

定义原三个对称矩
$$
\mathbf I(u,v)=
\left(
\int u''v'',\
\int xu''v'',\
\int(x^2u''v''+2u'v')
\right).
\tag{3}
$$
所需圆条件是
$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad
\mathbf I(f,g)=0,\qquad I_0(f,f)>0.
\tag{4}
$$
令
$$
c=\cos\theta,\quad s=\sin\theta,\qquad
\phi_\theta=cf+sg,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta .
\tag{5}
$$
$\odot$ 表示原对称输入槽；不能把 $D_\theta$ 当成一个普通函数再求导。

原 hook 满足对角恒等 $\mathfrak H(u;u,u)=0$。因此不施加第二个 hook，也有
$$
\mathfrak H(\phi_\theta;D_\theta)
=\mathfrak H(\phi_\theta;f,f)
-\mathfrak H(\phi_\theta;\phi_\theta,\phi_\theta)
=s\,\mathfrak H(g;f,f).
\tag{6}
$$
所以在 (2) 上，弱条件 $\mathfrak H(g;f,f)=0$ 足以准确支付每个真实相位的完整三阶周期。这一陈述不是说四个形式三阶槽的周期分别为零。

## 2. 在严格内部曲段上得到真正的弱核自由

先在一个暂定基本包络中选开区间
$$
J_0\Subset J_1\Subset (b,\infty).
$$
取实 cutoff $\chi_0\in C_c^\infty((b,\infty))$，在 $J_1$ 的邻域恒为 $1$，置
$$
f_0(x)=\chi_0(x)(x-b)^{5/2}.
\tag{7}
$$
由于 cutoff 的支撑与 $b$ 有正距离，(7) 的零延拓是真正紧 $C^\infty$ 函数，没有在分支点拼接一个非光滑幂。

任取
$$
0\ne g_0\in C_c^\infty(J_0;\mathbb R).
\tag{8}
$$
在 $J_1$ 上记 $p=f_0'$，则
$$
p=\frac52(x-b)^{3/2},\quad
p'=\frac{15}{4}(x-b)^{1/2},\quad
p''=\frac{15}{8}(x-b)^{-1/2},
$$
所以
$$
A_{f_0}:=6pp''-2(p')^2=0.
\tag{9}
$$
定义
$$
\mathcal W(f,g)=g'f''-f'g''.
$$
在 $\operatorname{supp}g_0$ 的邻域，(9)成立；在其余位置，$g_0'=g_0''=0$。因此
$$
A_{f_0}\mathcal W(f_0,g_0)=0
\quad\text{在整个共同区间准确成立。}
\tag{10}
$$

这里必须使用原通量的两端常数。R181/R306 给
$$
L_f(g):=\mathfrak H(g;f,f),\qquad
L_f(g)''=(A_fg'')'-V_fg',
\quad V_f=6(f''f''')',
$$
$$
\left[A_f(f'g''-f''g')\right]'=f'L_f(g)''.
\tag{11}
$$
对紧 profiles，$A_f\mathcal W=0$ 先迫 $L_f(g)''=0$：在 $f'\ne0$ 的开集用 (11)；在 $f'=0$ 的开内部直接用 $A_f=V_f=0$；其余点用连续性。原右零 collar 上 $L_f(g)=L_f(g)'=0$，故
$$
A_f\mathcal W=0\quad\Longrightarrow\quad
\mathfrak H(g;f,f)=0
\tag{12}
$$
是完整右锚恒等，而非仅二阶导数为零。(10)与(12)于是支付本基本对的弱 hook。

另一方面，
$$
\mathcal W(f_0,g_0)\not\equiv0.
\tag{13}
$$
否则在连通 $J_1$ 内，$p>0$，且
$$
(g_0'/p)'=-\mathcal W/p^2=0.
$$
$g_0'$ 在 $J_0$ 外的一小段为零，常数只能为零，遂 $g_0'=0$ 于 $J_1$。紧支撑再迫 $g_0=0$，与 (8)矛盾。由连续性，$\mathcal W\ne0$ 实际发生在一个非空开集上。

## 3. 三个左补包准确支付三复矩，弱 hook 不受破坏

令 $q_0=f_0+i g_0$，并以复双线性方式定义
$$
\mathbf M(q)=
\left(
\int(q'')^2,\
\int x(q'')^2,\
\int\{x^2(q'')^2+2(q')^2\}
\right).
\tag{14}
$$
$\mathbf M(q)=0$ 恰等价于 (4)中的六个实等式。

在 $\operatorname{supp}q_0$ 的严格左侧选三个互不交小区间。取同一个非零实偶 bump $\eta$，以相同宽度放到三个不同中心 $c_1,c_2,c_3$：
$$
\eta_j(x)=\eta(x-c_j).
$$
写
$$
a_0=\int(\eta'')^2>0,\qquad
a_2=\int\{x^2(\eta'')^2+2(\eta')^2\}.
$$
偶性给 $\int x(\eta'')^2=0$，故
$$
\mathbf M(\eta_j)=
\begin{pmatrix}
a_0\\ a_0c_j\\ a_2+a_0c_j^2
\end{pmatrix}.
\tag{15}
$$
三列组成的实矩阵可逆：减去第三行的 $(a_2/a_0)$ 倍第一行后，就是非零常倍的三点 Vandermonde。

因此有唯一复数 $z_j$ 满足
$$
\sum_{j=1}^3 z_j\,\mathbf M(\eta_j)=-\mathbf M(q_0).
\tag{16}
$$
分别选任意一个复平方根 $\beta_j^2=z_j$，零值取平方根零，定义
$$
q_*=q_0+\sum_{j=1}^3\beta_j\eta_j,\qquad
f_*=\Re q_*,\quad g_*=\Im q_* .
\tag{17}
$$
这里是一次固定有限选择，不要求复平方根随额外参数光滑。所有支撑互不交，(14)无跨包乘积，所以 (16)准确给 $\mathbf M(q_*)=0$。

弱 hook 也保持。在每个新增包内，
$$
(f_*,g_*)=(\Re\beta_j,\Im\beta_j)\eta_j,
$$
因此 $\mathcal W(f_*,g_*)=0$。在原包内它就是 (10)；在空隙内各导数为零。于是全区
$$
A_{f_*}\mathcal W(f_*,g_*)=0,\qquad
\mathfrak H(g_*;f_*,f_*)=0.
\tag{18}
$$
这一步没有把非局部 $\mathfrak H$ 擅自拆成几个无尾项的包；先证明全区通量恒等，再用同一个右锚和 (12)恢复完整 hook。

原 $J_0$ 内完全未改，所以
$$
\mathcal W(f_*,g_*)\not\equiv0.
\tag{19}
$$
特别 $g_*\ne0$，故 $I_0(g_*,g_*)>0$。三矩给 $I_0(f_*,f_*)=I_0(g_*,g_*)$ 与交叉零；可以再乘同一个正实常数使两者 $I_0$ 都为 $1$。该归一化保留 (18)–(19)。

R306 的双 hook 分类现在准确推出
$$
\mathfrak H(f_*;g_*,g_*)\not\equiv0.
\tag{20}
$$
若它为零，连同 (18)就迫 (19)为零。因此本构造确实使用了原弱条件的额外自由，没有暗中回到旧强类。

## 4. 合法放置与不可由常数换基分离

所有上述选择只使用有限多个紧支撑函数。先把整个基本包作一次共同正仿射变换，缩小到需要的宽度。若
$$
\widetilde u(x)=A\,u((x-d)/a),\qquad a>0,
$$
则原矩准确变换为
$$
\begin{aligned}
I_0(\widetilde u,\widetilde v)&=A^2a^{-3}I_0(u,v),\\
I_1(\widetilde u,\widetilde v)&=A^2a^{-3}
\{dI_0(u,v)+aI_1(u,v)\},\\
I_2^*(\widetilde u,\widetilde v)&=A^2a^{-3}
\{d^2I_0(u,v)+2adI_1(u,v)+a^2I_2^*(u,v)\}.
\end{aligned}
\tag{21}
$$
所以三矩与交叉零保持。$A_f\mathcal W$ 也只乘非零缩放因子，弱 hook 由 (12)保持。此处不需要假定原非局部算子在任意非仿射坐标变换下协变。

取基本包宽度足够小，便可在原给定 $I^\circ$ 内放置下一节的八个等间隔完整副本，始终保留严格空隙和两个公共零 collar。所有缩放与最终位置在应用平移多项式消项以前固定；不先求一个固定几何的 ruling，再声称任意事后改坐标仍保其零值。

本平面比“函数值重叠”更强。若常数实矩阵
$$
\begin{pmatrix}\widetilde f\\\widetilde g\end{pmatrix}
=C\begin{pmatrix}f\\g\end{pmatrix},
\quad \det C\ne0,
$$
则
$$
\mathcal W(\widetilde f,\widetilde g)=\det(C)\mathcal W(f,g).
\tag{22}
$$
任意两个支撑不交的光滑函数均有 $\mathcal W=0$，故 (19)排除了任何常数可逆换基后的支撑分离，也排除了任何换基后的处处导数 rank-one 呈示。

## 5. 八个完整副本：只用已付二阶局部化消全部三阶 ruling

仍在同一个真实几何 (2) 上操作。为缩短记号，用 $f_*,g_*$ 表示已经完成 (21) 的基本包。取
$$
t_j=t_*+jL,\qquad
a_j=(-1)^j\binom7j^{1/3},\qquad j=0,\ldots,7,
$$
其中 $L$ 严格大于基本包络宽度，所有副本在 $I^\circ$ 内。定义最终 profiles
$$
f=\sum_{j=0}^7a_j f_*(x-t_j),\qquad
g=\sum_{j=0}^7a_j g_*(x-t_j).
\tag{23}
$$
可在最后再共同正归一化。因每个完整包单独满足三矩与交叉条件，(23)仍满足 (4)。同样，全区 $A_f\mathcal W=0$；在每个非零副本内 $\mathcal W$ 是原式的非零平方幅度倍数。因此 (1)的全部三条仍成立。

为了准确处理第三 ruling，定义原两个二阶 forcing
$$
H_d=(dY_f)^2-(dY_g)^2,\qquad
H_c=\mathcal S(Y_f,Y_g).
\tag{24}
$$
取同一右 $x$ 锚、同一 $s=s_0$ 零初值的 canonical 解
$$
\mathcal L_XZ_d=H_d,\qquad \mathcal L_XZ_c=H_c.
\tag{25}
$$
(4)使每个完整基本包的三条尾矩差、三条交叉尾矩在其左右包外均准确为零。R46 §4 和 R52 §2 的完整恢复于是给：对应的 $\rho,\mathcal R,\eta_0,W,W_x$ 以及整个 $Z_d,Z_c$ 均在该完整包络外为零。$M=0$ 同时给它们的真实 $s$ 周期。不能把本结论用于 (17)里一个未独立配平的微包；这里只分解八个已经完整配平的基本副本。

对四个三阶 forcing
$$
-\mathcal S(Y_f,Z_d),\quad
-\mathcal S(Y_g,Z_d),\quad
-\mathcal S(Y_f,Z_c),\quad
-\mathcal S(Y_g,Z_c),
\tag{26}
$$
先计算原 range 的逐 ruling 表达，暂不要求四个 forcing 的周期分别为零。R46 §5 与 R52 §3 的逐槽次数证明只用 (25)的原二阶恢复，因此仍适用：一个完整基本包平移 $t$ 后，四条 ruling 都是 $t$ 的次数至多六的多项式，其系数是任意真实 $s$ 函数。

更具体地，二阶 characteristic 分子 $W_t,W_{t,x}$ 的平移次数至多四，$\eta_{0,t}$ 至多三；第三 ruling 的原被积式为
$$
\int\phi'''(x)
\left(eW-\frac{1+e^2}{2h}W_x
-\frac{1+e^2}{h^2}\eta_0\right)dx,
\tag{27}
$$
其中 $\phi$ 为对应基本包的 $f_*$ 或 $g_*$。$e$ 对平移至多一次，$1+e^2$ 至多二次，故总次数至多六。这里保留了全部 $s$ history，不是假定常状态或冻结 frame。

由于 $Y$ 和二阶 $Z$ 均按完整副本局部化，(26)没有跨完整副本乘积。每条 ruling 只按 $a_j^3$ 相加，而
$$
a_j^3=(-1)^j\binom7j,\qquad
\sum_{j=0}^7(-1)^j\binom7j(t_*+jL)^m=0
\quad(0\le m\le6).
\tag{28}
$$
所以四条 ruling 对每个真实 $s$ 都准确为零。它们不是只在有限网格上为零，也不需要新的几何或 profile 求值。

## 6. 对真实相位组合施 range；不要求四个中间槽各自 periodic

这一步是本稿与旧强 hook 构造的实际区别。

令 $c=\cos\theta,s=\sin\theta$，使用包含交叉通道的准确二阶场
$$
Y_\theta=cY_f+sY_g,\qquad
Z_\theta=s^2Z_d-csZ_c.
\tag{29}
$$
由 (24)–(25)，
$$
\mathcal L_XZ_\theta=(dY_f)^2-(dY_\theta)^2.
\tag{30}
$$
完整三阶 forcing 是
$$
H_\theta^{(3)}=-\mathcal S(Y_\theta,Z_\theta).
\tag{31}
$$
它是 (26)的相位多项式组合。因此 §5已经支付 (31)的全部逐 ruling 条件。它由周期的 $Y$ 与周期的 canonical $Z$ 构成，在真实 $s$ 圆上本身周期，并有公共外 collar。

另一方面，(6)、(18)、(23)及实际 (2)给
$$
T(\phi_\theta;D_\theta)
=\kappa_H s\,\mathfrak H(g;f,f)=0.
\tag{32}
$$
即 (31)的完整第三周期也为零。这里保留了实际第二历史以及相位交叉 forcing；不是把全局周期假设当成各个局部尾逐点为零。

现在才对 **完整的 (31)** 应用原线性 range 定理和 canonical 右锚、$s_0$ 零初值恢复，得到真实光滑周期场 $W_\theta$：
$$
\mathcal L_XW_\theta=-\mathcal S(Y_\theta,Z_\theta).
\tag{33}
$$
它在公共左右 collar 为零。原恢复对 forcing 线性，故 $W_\theta$ 随相位光滑且为有限三角多项式。

等价地，可以在展开的 $s$ 区间上先定义 (26)的四个 canonical 形式原函数，再组合
$$
W_\theta=s^2(cW_{fd}+sW_{gd})
-cs(cW_{fc}+sW_{gc}).
\tag{34}
$$
这些单槽原函数不需要各自满足周期条件；(32)只保证 (34)这一实际组合的周期。不能把 (34)反解成四个分别周期的场，也不能从本稿推出 $\mathfrak H(f;g,g)=0$。R56 的原恢复和 R52 的交叉公式都对完整 forcing 线性，因此在组合后施周期并未改变规范或略去初值。

当 $\theta=0,\pi$ 时，$D_\theta=0$，从而 $Z_\theta=0$、$H_\theta^{(3)}=0$。同一线性右锚与零初值给
$$
W_0=W_\pi=0.
\tag{35}
$$

## 7. 同一新目标度量的完整三阶圆

固定目标
$$
g_\varepsilon=(X+\varepsilon Y_f)^*\mathrm e
=g_X+\varepsilon^2(dY_f)^2.
\tag{36}
$$
对最终选定的 $f$，这一目标与 $\theta$ 无关。与旧 R183 或 R280 的另一个 seed 比较时，(36)一般是一个新目标；本稿不声称更换 profiles 后仍保持旧 seed 的目标度量。

置
$$
F_{\varepsilon,\theta}^{[3]}
=X+\varepsilon Y_\theta+\varepsilon^2Z_\theta+\varepsilon^3W_\theta.
$$
由 (30)、(33)准确有
$$
\begin{aligned}
(F_{\varepsilon,\theta}^{[3]})^*\mathrm e-g_\varepsilon
={}&\varepsilon^4\{(dZ_\theta)^2+
\mathcal S(Y_\theta,W_\theta)\}\\
&+\varepsilon^5\mathcal S(Z_\theta,W_\theta)
+\varepsilon^6(dW_\theta)^2 .
\end{aligned}
\tag{37}
$$
在固定紧带及全部相位上统一为 $O(\varepsilon^4)$。由 (35)，两个种子端点仍准确是
$$
F_{\varepsilon,0}^{[3]}=X+\varepsilon Y_f,\qquad
F_{\varepsilon,\pi}^{[3]}=X-\varepsilon Y_f .
$$
对足够小的固定 $\varepsilon$，这些场构成光滑周期的浸入带 Taylor 家族；(37)并不把中间相位变成准确有限等距族。

**已完成的建设性结论。** 在已有实际 (2)的闭 hook 上，可以在任意给定的非空合法 profile 活动区间内选一个三矩非退化圆，使它具备真正的导数 rank-two 开集，只满足原需要的弱 hook，却准确满足整个三阶固定度量方程。

**仍未支付。** 原四阶 forcing
$$
-\{(dZ_\theta)^2+\mathcal S(Y_\theta,W_\theta)\}
$$
的完整周期、逐 ruling、全部 Gaussian 或其他 history 系数均须重新检查。尤其本稿没有把旧 rank-one 微包的面积、能量或 self 关系搬到这个曲段重叠圆；也没有把八副本的二阶局部化擅自延伸到第三场或第四 forcing。原矩阵、平台和非局部有序尾仍可能提供障碍。

本稿新增的是一个已经完成三阶 range 的真实弱 hook 通道；不以假加第二 hook 关闭该通道，也不以此通道存在宣布主课题完成。
