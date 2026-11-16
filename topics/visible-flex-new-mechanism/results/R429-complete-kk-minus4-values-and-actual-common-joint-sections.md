# R429：两个完整 kk 自然值解除共同 J 的最后低权前提

日期：2026-11-16。**本部分为数学证明。两个新完整自然值来自§7绑定的原公开实际记录；本部分不重跑原根、求积、符号程序或任何科学检查。**

本稿接 [R427](R427-even-quartic-curvature-support-of-the-complete-kk-minus4-natural-function.md) 的完整自然偶四次支撑，以及 [R428](R428-conditional-complete-joint-cost-cone-and-finite-actual-C1-sections.md) 的条件性共同实际截面。新的完整值使 R428 唯一低权前提在**原来从起点保持共同 $D,E_5$ 的同一母库**上成立；不需要增加 $M_{25}$、改变最终母、重新取十九根，亦不需要普遍的 $1+k^2$ 因子。

以下结果使用同一明确的物理实施前提：有限实际母库、右辅助矩基、共同右锚与全部有限真实控制族，在从起点共同选定的合法物理窗口内。它不授任意旧冻结窄窗口，也不把不同最终母库或分别取得的路径截面拼接。

## 1. 两个新的完整输入，以及没有成立的普遍因子

沿 R427，记 $V_j$ 为其原完整正规系数的真权负四代表；$\mathcal N$ 是整个自然函数，保持原 self、正式 pure 与有序 Green 规范。原身份是
$$
\mathcal N([h^{-4}]\widehat Q_{kk}(h,k,0))
=\mathcal N(V_0)+k^2\mathcal N(V_2)+k^4\mathcal N(V_4).
\tag{1}
$$
这里不是原成本只有三项的断言。

本稿实际输入绑定
run $43790439330$、job $133047403947$、source
$83b008aecf9c2e2a53b4f65802f6bf97fa84111e$；
其全部源、成本、回执与原日志证据见§7及[完整首次实际](../notes/kk-minus4-natural-flux-first-completed-actual-20261116.md)。
读出 B、C 分别是 $\mathcal N(V_2),\mathcal N(V_4)$。其确认的**完整**值为
$$
\boxed{
\begin{aligned}
\mathcal B(u):=\Lambda_u(V_2)
={}&-\frac18\int upr^3+\frac1{32}\int xur^4
+\frac5{32}\int xp^2r^3\\
&-\frac{11}{128}\int x^2pr^4
+\frac9{640}\int x^3r^5,\\
\Lambda_u(V_4)={}&0,
\end{aligned}}
\qquad p=u',\quad r=u''.
\tag{2}
$$
B 的全部非局部原项为空；C 的完整左 word、局部项、非局部项和 Euler 均为空。本文用的是完整值，不从 principal 或有限 profile 值猜测 locality。

[R426](R426-complete-zero-curvature-kk-minus4-natural-anchor-and-common-query-reduction.md) 已给
$$
\mathcal A_0(u):=\Lambda_u(V_0)
=-\frac1{32}\int upr^3+\frac3{64}\int xp^2r^3
-\frac3{128}\int x^2pr^4+\frac3{640}\int x^3r^5.
\tag{3}
$$

另有准确的否定结论：(1)在全部 profiles 上**不**普遍被 $1+k^2$ 整除。
在 $\Lambda(V_4)=0$ 后，该整除等价于 $\mathcal B=\mathcal A_0$。对二阶局部密度 $\mathscr L$，
Euler 导数中 $u^{(4)}$ 的系数为 $\mathscr L_{rr}$。
(2)的 $x^0upr$ 系数为 $-3/4$，(3)为 $-3/16$，差为
$$
-\frac9{16}upr\ne0 .
\tag{4}
$$
因此 $\mathcal B-\mathcal A_0$ 不是全导数，其完整泛函非零。下文的共同查询消元不使用这个错误的普遍因子。

## 2. 偶母上的完整平移值，M25 准确抵消

固定 R412/R414 从同一起点构造的偶母 $U$。它的四个完整 $n_2$ 平移系数为零，所以
$$
M_5(U)=\int(U'')^5=0,\qquad q_1(U)=0.
\tag{5}
$$
仍用 [R413](R413-common-mother-Q4-chain-and-exact-low-layer-character-reduction.md) 原规范
$$
D=-\frac12P_2+\frac12X-\frac3{20}M_{25},\qquad
E_5=-\frac12X+\frac7{20}M_{25},
$$
$$
P_2=\int (U')^2(U'')^3,\quad
X=\int yU'(U'')^4,\quad
U_4=\int U(U'')^4,\quad
M_{25}=\int y^2(U'')^5.
\tag{6}
$$
这里 $U_4$ 是一个积分，不是新的成本权或母函数名称。

$U$ 偶，故(2)在中心零的值为零。对 $U_c(x)=U(x-c)$ 作真实变量替换 $x=y+c$，全部项精确展开。无显式 x 的项仍为零；含 $x^2$ 的项只留 $2cX$；含 $x^3$ 的项只留 $3cM_{25}$ 与 $c^3M_5$，最后一项按(5)为零。于是
$$
\mathcal B(U_c)
=c\left\{\frac{U_4}{32}+\frac{5P_2}{32}
-\frac{11X}{64}+\frac{27M_{25}}{640}\right\}.
\tag{7}
$$
这不是低中心阶截断，而是完整平移多项式。

由(5)、(6)，原 R424 三个准确关系为
$$
U_4=8D-7E_5+\frac12M_{25},\quad
P_2=-2D-2E_5+\frac25M_{25},\quad
X=-2E_5+\frac7{10}M_{25}.
\tag{8}
$$
代入(7)，三个系数分别为
$$
[D]:\quad \frac8{32}-\frac{10}{32}=-\frac1{16},
$$
$$
[E_5]:\quad-\frac7{32}-\frac{10}{32}+\frac{11}{32}
=-\frac3{16},
$$
$$
[M_{25}]:\quad
\frac{10+40-77+27}{640}=0 .
$$
因此
$$
\boxed{\mathcal B(U_c)=-\frac{D(U)+3E_5(U)}{16}\,c.}
\tag{9}
$$
不需要各最终母具有共同的 $M_{25}$，因为其系数在完整值中已准确消失。

同一原母上，R426 给
$$
\mathcal A_0(U_c)=-\frac{3D(U)}{32}\,c.
\tag{10}
$$
(9)和(10)一般不同；这与(4)相容。

## 3. 真实幅度、不同宽度、中心和 ordered 查询

对已经冻结的实际最细包
$$
u_i(x)=\rho_iU_i((x-\xi_i)/w_i),\qquad w_i>0,
\tag{11}
$$
每个原局部项保其真实导数缩放。用同一次变量替换可得
$$
\boxed{
\begin{aligned}
\mathcal B(u_i)
&=-\rho_i^5w_i^{-7}\xi_i\,\frac{D_i+3E_i}{16},\\
\mathcal A_0(u_i)
&=-\rho_i^5w_i^{-7}\xi_i\,\frac{3D_i}{32},
\end{aligned}}
\tag{12}
$$
其中 $D_i=D(U_i),E_i=E_5(U_i)$。
没有把实际 $w_i$ 设为共同宽度，也没有将 $\rho_i$ 丢进未说明的归一化。

对共同正仿射输入
$C_{H,c}u_i(x)=u_i((x-c)/H)$，
实际宽度变成 $Hw_i$、中心变成 $H\xi_i+c$。所以
$$
\mathcal B(C_{H,c}u_i)
=-\rho_i^5(Hw_i)^{-7}(H\xi_i+c)\,\frac{D_i+3E_i}{16}.
\tag{13}
$$
成本作用与输入作用仍按原
$$
\Lambda_{u_i}(\mathsf P_{H,c}V)=H^2\Lambda_{C_{H,c}u_i}(V)
\tag{14}
$$
相接。式(13)的 profile 因子与(14)的共同 $H^2$ 分别保留；它们不是两个可以选用其一的规范。

(2)、(3)都是完整局部五次泛函。若 $\operatorname{supp}u<\operatorname{supp}v$，则
$$
\mathcal B(su+tv)=s^5\mathcal B(u)+t^5\mathcal B(v),
$$
(3)同理。因此
$$
[s^3t^2]\Lambda_{su+tv}(V_2)
=[s^3t^2]\Lambda_{su+tv}(V_0)
=[s^3t^2]\Lambda_{su+tv}(V_4)=0.
\tag{15}
$$
原右辅助矩基可以是任意实际紧包；它们无需满足(5)、共同 $D/E_5$ 或某个新母形条件。原因是(15)直接杀整个 ordered 行，而不是把辅助 self 也加入目标。

## 4. 同一个共同查询商中，两个新列都属于真实 N 像

记 $\mathcal A$ 为 R428 的最小共同映射：全部实际母的 self 自然查询、所需右辅助的有序 $3+2$ 行及其共同正仿射闭包。原从起点的母纤维给
$$
D(U_i)=D_0,\qquad E_5(U_i)=E_0,\qquad D_0-E_0>0
\quad\text{对全部最终 }i .
\tag{16}
$$
这仅要求共同归一母的两值相同；实际幅度、宽度、位置仍按(11)各自保留。

R393/R413 的完整 Q4 函数
$$
H_Q(u)=\frac14\int r(p-xr)^4
$$
有一个原真权 $-3$ 成本代表 $W_H\in U_{-3}$，且其平移导数
$NH_Q=F_{Q4}/2-3G_{Q4}$ 是同一真实表示内的权 $-4$ 行。
R413 给
$$
(NH_Q)(U_c)=6(E_0-D_0)c.
\tag{17}
$$
对(11)与全部共同仿射查询，(17)乘与(13)相同的
$\rho_i^5(Hw_i)^{-7}(H\xi_i+c)$，以及成本输运的共同 $H^2$。
它本身是完整局部泛函，所以全部(15)型 ordered 行也为零。

因此由(9)、(13)、(15)、(17)得到整个共同映射的身份
$$
\boxed{
\begin{aligned}
\mathcal A(V_2)
&=-\frac{D_0+3E_0}{96(E_0-D_0)}
\,\mathcal A(NW_H),\\
\mathcal A(V_4)&=0.
\end{aligned}}
\tag{18}
$$
分母非零由(16)保证。若分子恰为零，第一行就是零身份，不产生额外例外。

这直接支付 R428 的唯一前提
$$
\boxed{\mathcal A(V_2),\mathcal A(V_4)\in N\mathcal A(U_{-3}).}
\tag{19}
$$
使用的是同一个 $W_H$ 代表与同一个比例，不是对每个母分别寻找不同的消元。

还可把全部曲率自然查询写成一行：
$$
\boxed{
\mathcal A([h^{-4}]\widehat Q_{kk}(h,k,0))
=-\frac{3D_0+2k^2(D_0+3E_0)}
{192(E_0-D_0)}\,\mathcal A(NW_H).
}
\tag{20}
$$
它是共同查询身份，不是普遍全 profile 函数的比例。特别，(20)不与(4)矛盾。

## 5. 最后负四正字符消失，完整共同实际截面成立

令
$$
J=(E,\mathcal A),\qquad E=(\pi,\mathcal Q).
$$
$\mathcal Q$ 仍是全部紧输入的原 self 左二次函数，不是整个 self 输出。
若 $\lambda$ 是经这个同一 $J$ 下降、杀原响应 $\mathcal R$ 的权负四正仿射字符，则(18)中仅自然坐标相等还需补齐 E；不能省略这一步。

例如取
$$
Z=-\frac{D_0+3E_0}{96(E_0-D_0)}\,W_H.
$$
由原 $E(U_{-4})=E(\mathcal R_{-4})$，选真实响应
$R\in\mathcal R_{-4}$ 满足
$E(R)=E(V_2-NZ)$。原自然查询杀响应，故
$$
J(V_2-NZ-R)=0,\qquad
\lambda(V_2)=\lambda(NZ)+\lambda(R)=0.
\tag{21}
$$
对 $V_4$ 同理。这里的 signed 代表用于证明字符消失，不把减去 R 或取 Z 冒成一条已实际执行的负路径。

R420 的同一乘子已给全曲率静态 $a=\mu=0$；
R425 的全曲率 $hh$ 行在共同 Q4 平移像中，故 PSD 迫 $hh$ 和交叉行均为零；
R426 给 $V_0$ 同样在该真实 N 像。
现在(21)清掉全部剩余 $kk$ 偶四次系数。
原状态协变保留全 $h,\omega$；不是只在一个曲率锚处取零。

由 R130 完整十四族生成，负四正字符只能为零。
R428 已逐权排除其它候选，故它的条件闭锥结论在原同一母库上变成
$$
\boxed{\overline{\operatorname{cone}J(\mathcal S)}=J(U).}
\tag{22}
$$

**共同窗口内的实际结论。** 在 R428 的从起点共同合法窗口前提下，
对任意紧相容目标集 $\mathcal K\subset J(U)$，
存在其有界开邻域与一个固定有限真实词族 $\mathscr D(y)$，使
$$
M_{\mathscr D(y)}=\mathbf T_{\mathscr D(y)}=0,\qquad
J(V_{\mathscr D(y)})=y,
\tag{23}
$$
且全部实际参数按 y 作 $C^1$ 变化。
这是 R428 的同一个满锥—商截面—原型商基准—第二商校正—有限响应根构造；
所有整数、真倒行、桥成本、非零原型基准和物理窗口同时固定。
没有先为每个母各造一条 actual 路径后再拼接。

若原闭 hook/Klein 背景从起点放进同一窗口，按
$V_{\rm base}+4V_{\mathscr D}$
使用相容目标 $-J(V_{\rm base})/4$，便可取得 whole $E=0$ 与完整共同 $\mathcal A=0$。
原固定保护子字可原样保留，但其 incoming history 和完整 mixed 成本按最终路径重新计算。
本结论不免费恢复旧冻结度量、Morse 或其它未证结构。

## 6. 真正支付的 period 前提与仍欠的内部 joint

在上述同一最终成本上，$\pi V=0$ 给原有序全函数极化。三个右辅助三矩基与(23)使
$$
\omega_i=\Lambda_{u_i}(V)=0,\qquad A_i(V;n)=0\quad\forall n.
\tag{24}
$$
因此对真实 suffix
$$
n_{R,i}=\sum_{j>i}(a_j^2-b_j^2)\mu_j,\qquad
n_{T,i}=\sum_{j>i}a_jb_j\mu_j,
$$
两整包通量
$$
a_i^3\{(a_i^2-b_i^2)\omega_i+A_i(V;n_{R,i})\},\qquad
-a_i^3\{a_ib_i\omega_i+A_i(V;n_{T,i})\}
\tag{25}
$$
同时为零。没有要求 suffix 本身零。

whole $\mathcal Q=0$ 给所有真实平台 $G''=0$；
原纯零端一次层、固定解析平端类别及(25)给 R389/R394 的完整两端逆 germs。
这里替换的是 R394 实际使用的有限 $\Lambda_{u_i},\Lambda_{u_i+u_j}$ 清单，
不是不可能实际实现的 universal $\Lambda_{\rm all}=0$。

仍须支付同一成本在每个内部 $A_f$ 简单零点的两条真实部分通量。
它们保 self 与右方矩尾的全函数：
$$
R_i s_i(x)+\sum_{j>i}R_j s_{ij}(x)=0,\qquad
T_i s_i(x)+\sum_{j>i}T_j s_{ij}(x)=0.
\tag{26}
$$
(25)只付右端积分，不付(26)的内部值。所有允许二阶 gauge 的 $L_f$ 像都不能改这些退化点通量。

只有(26)也成立后，原全局逆构造才依次进行：活动包解 $k'$、保端 jets 于间隙连接、另付 $\int k'=0$ 的值闭合、用右 collar 清算子输出的仿射差。gap 中对 $k'$ 的修正会改变 k 的平台值，必须进入十三行真实右端。

最后仍是同一个 incoming history、同一对 period 特解和原 $2n$ 核列给出的
$$
C_\theta\eta_\theta
=-\mathcal A_\theta(\sin\theta\,k_d+2\cos\theta\,k_e).
\tag{27}
$$
其零行恒等、单位圆秩降处可去极点条件及全部实际成本/历史的同点联调尚未支付。十三不作已知秩，原十一指定对应点控制不外推到全部不同母的所有内部点。

新结论是：两条真正新的完整自然观察通过(18)解除 R428 的唯一条件，原共同母库已获得 whole $E$ 与全部所需有限 self/ordered 总量的同一实际 $C^1$ 截面。它不把剩余内部通量、完整 period、同一十三行规范或整个可动性主课题一并宣布完成。


## 7. 首次实际证据、全部费用与人工推论的边界

原公开 [run43790439330](https://github.com/Rogerhu12/math-research-public/actions/runs/43790439330)，job133047403947，source83b008aecf9c2e2a53b4f65802f6bf97fa84111e；原stdout130385B，SHA256 aa0a908ce5ee7dfde82d68e87d973120dd41aaa5084cebfb16fb5bd9f332ffdc。COMPLETE_REPORT的JSON+LF47726B，SHA256 9418fa5aaf8234ce7eedd78a3613534f07edf715b334d4e348d421aaf6284655，与原临时输出文件一致。root已读全部观察、原支撑/target plan、12新收缩及九旧响应；没有只看workflow的success。

请求10622B/SHA33b3c808188b7ccff92c0abea14d391b51f6bbdd189d2db49f1af1e3189f6182，实际38源逐项相符。新entry30279B/SHAfaf1446ba171e7b83d64b53e2bda3f237383dae27caf25353f754ae7fcaee3a4，source与workflow在执行前已全文静态核读。原R210 family1/global75、76的两条pure坐标、framing与scale只读原日志；不重复pure或秩求解。

实际完整装配6个原raw系数，分别保k_s²、−∂k beta和−(2h)⁻¹∂omega beta。10个typed势根作12个不同必要外槽self收缩；N0/N2两类raw势和原非紧外槽/右锚全保，未用自然层的CA/N2消项预删raw。kk速度专属m2的h幂为−3/−2，原Gamma/reference不进入目标h−4；完整target plan SHA858c1ca4cbc4bd449984022d94bc329adf523e856e3f5ce1fbf26a2d7290de3b。16因子根读801/3521个atoms，9旧响应根读702/933，所有原hash相同。

B的完整左式为一个常数单字的五项密度，nonlocal为空，Euler14项非零；C的完整left/local/nonlocal/Euler均空。B left SHA faaa80c971a4350deae53a576d49d57146211ae6908b37b601621525c841f5e0，Euler SHA78462221e708bfce89204e81fcf1c4ec92d66b7b5ca9781351c0d20a2963b035；C对应空表SHA4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945。完整公式只在原Actions stdout，仓库仅此人类证明和身份元数据。

本次科学elapsed2.833311144000021秒，其中原paid log读取1.6056699789999982、必要输入与新self装配1.157212718999972、新Ω .06503811999999698秒，其余为同一次框架开销。peakRSS234388KiB；primitive196、cache peak780、cycle fallback0。k0、旧HH4、旧profile/pure/rank/forcing/N0/N2 producer/完整mixed/开发套件执行均0。

公开actual pull02:09:58.208880–02:09:59.918061 UTC到8643f43eb2ad15b0abe7fb4e55255fba3bd37fd9，根/本题README原blob与SHA相同、diff空；私有02:10:02.347510–02:10:03.031482到1ec6b57a875aca377038cd055a4ec0028b75473c，根同、本题README无、QUEUE本会话唯一进行中。root已消费，完整receipt身份在首次实际note及HANDOFF；next pull deadline03:09:58。随后runner回到触发source运行，没有混入其它topic更新。

原machine字段 remaining_minus4_Q2_character_or_actual_joint_resolved=false 未改。本稿§2–6是以实际完整密度为输入、另经纸面证明得到的共同查询、字符与真实有限词结论，不把它写成该程序原有的自动结论。两者的范围明确区分。
