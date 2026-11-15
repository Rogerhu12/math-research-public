# R754 — 原同域三区域的精确惯性比例与完整 étale 来源 trace

日期：2026-11-15。**状态：已证明。**

本篇固定 R742 的原权、原有限门和原十七处投影，在 R747 的同一个 raw 来源上计算三个真实补支的平凡点角色。使用 R752 的完整第一来源及 R751 的两条 dyadic 点公式，得到比例
$$
\frac{p-3}{p-1},\qquad \frac1{p-1},\qquad \frac1{p-1}.
$$
后两条是完整 $\lambda H_W$、$\gamma\lambda H_V$，不是删除 core 系数后的裸返回行。

证明在全部五个伙伴仍保留时先作规范 étale theta 平均。它准确读取零 $Y$-Fourier 项；随后在每个 $Z$-unit 伙伴纤维上计数两个不同的非零根。这里没有把 theta 测度当作均匀测度，也没有用一个原本不存在的简单张量假设。

这些比例是原有限来源的实际关系。它们给出各有限补支的非零点分量，并且恰好加回原 primitive 行；没有新增一个原中央导数零条件。

## 1. 同一个原来源与四个实际门

沿用 R742 的合格普通素数、原 $\Omega=\Omega_p$、
$$
K=\mathbf Q(\omega),\qquad \omega^2+\omega+1=0,\qquad b=17,
\qquad \lambda=-\bar\pi_0^{-1},\qquad \kappa=\pi_0/\bar\pi_0.
$$
所有线性系数的单位条件均沿用 R742/R747。特别下文的 $b_Y,d_Y,\alpha,36$ 在所选 $p$ 处都是单位。

原轴及两个实际系数为
$$
Y=A+c+2d,\qquad W=A+3(1+2\omega)c+4d,
$$
$$
\alpha=17-3\omega,\qquad
b_Y=\frac{\bar\alpha}{17}=\frac{20+3\omega}{17},\qquad
Z=W-b_YY,
$$
$$
V=36Y-\alpha W=d_YY-\alpha Z,\qquad
d_Y=36-\alpha b_Y=\frac{263}{17}.
\tag{1}
$$
$Y$ 的全部五个正交伙伴记作 $B$；其中含 $Z,E$ 及原三个权伙伴。此记号不遗忘原六输入或它们的 gluing。

固定 $k=2,4$，令
$$
\mu_k=\mathcal P_{\tau_k}^Y e_0,\qquad
\tau_2(g_0)=-\omega^2,\quad \tau_4(g_0)=-\omega.
\tag{2}
$$
这是 R742 的同门十七处投影。两个返回态必须经 R747 的完整 core 逆式搬回 (2) 后才使用下式；未把 raw quarter 态直接认成 $e_0$。

固定 $0\le a\le30$ 和 $\ell\ge1$。保留
$$
B_i=b_iZ+e_iE,\qquad
\Delta_\ell=1_{B_1\in p^\ell}-1_{B_3\in p^\ell},
$$
$$
\begin{array}{c|cc}
i&b_i&e_i\\ \hline
1&-(170+117\omega)/526&-(4+9\omega)/263\\
3&(170+291\omega)/526&(2-3\omega)/263 .
\end{array}
\tag{3}
$$
把全部原伙伴权记为
$$
\mathcal W_{a,\ell}(B)
 =\Omega^{-1}ZE^a\phi_{a,\infty}\,
       1_{\{Z,E\ {\rm unit}\}}\Delta_\ell .
\tag{4}
$$
$\phi_{a,\infty}$ 正是 R742 的实际 $u=0$ 权，包含两个 $C$ 分支、所有原周期归一及全部正交伙伴。若采用等价的原 $C^\perp$-unit 表示，其完整指示也包含在 (4) 中。每个齐次块 $E^a\phi_{a,\infty}$ 的总次数属于 $6\mathbf Z_{\ge0}$。

把尚未加入的浅门写成
$$
\begin{array}{c|l}
P&Y\ {\rm unit}\\
G&Y,W,V\ {\rm unit}\\
W_0&Y\ {\rm unit},\ W\in p\\
V_0&Y\ {\rm unit},\ V\in p .
\end{array}
\tag{5}
$$
以下 $1_J(y,B)$ 指 (5) 中相应的指示；(4) 已经包含共同的伙伴门及带符号的 $\Delta_\ell$。

定义真正的一变量来源
$$
\nu_{k,J,a,\ell}
 =Y_*\bigl(1_J(Y,B)\mathcal W_{a,\ell}(B)\,\mu_k\bigr).
\tag{6}
$$
其完整负一值为
$$
\begin{aligned}
\Omega I_{-1}(\nu_{k,P,a,\ell})&=p_{\tau_k,a}(\ell),\\
\Omega I_{-1}(\nu_{k,G,a,\ell})&=g_{\tau_k,a}(\ell),\\
\Omega I_{-1}(\nu_{k,W_0,a,\ell})&=\lambda h^W_{\tau_k,a}(\ell),\\
\Omega I_{-1}(\nu_{k,V_0,a,\ell})&=\gamma\lambda h^V_{\tau_k,a}(\ell),
\qquad \gamma=\chi_A\chi_E .
\end{aligned}
\tag{7}
$$
这里 $I_{-1}(\nu)=\int_{\mathbf Z_p^\times}x^{-1}\,d\nu(x)$。等式 (7) 是 R747 的完整来源返回，保原 $Y_\kappa$ 观察、全部 $\kappa$ 高次及 quarter 中心相位。特别没有将 $h^W,h^V$ 换成裸 $W$ 或 $V$ 负一矩。

在 (4) 的支持上，$W\in p$ 与 $V\in p$ 不会同时发生，所以逐点有
$$
1_P=1_G+1_{W_0}+1_{V_0}.
\tag{8}
$$

## 2. 全 Fock/伙伴来源的分裂与有限系数

R745/R752 在 $Y$ 与五伙伴的实际加法 isogeny 上给出
$$
s^*\mathcal L=\mathcal L_{34}\boxtimes\mathcal L_B.
\tag{9}
$$
该 isogeny 的度在本篇 $p$ 处为单位；因而所有 $p$-primary 平移都有唯一的分裂提升。全部 $B_i,Z,E,C^\perp$ 及其余伙伴方向与 $Y$ 正交，故它们的有限 Fourier 平移的第一坐标准确为零。

十七处投影后的完整第一空间是
$$
\mathcal H_k
 =\overline{\mathbf Q}D_{k,17}
   \oplus\overline{\mathbf Q}P_{+,k,17}.
\tag{10}
$$
$D_{k,17}$ 是原 type5、首 $z^5$ 系数为1的来源；$P_{+,k,17}$ 是 R751 的 type3 规范。后者首非零阶 $r_k\in\{3,9,15,21,27\}$，本篇不固定 $r_k=3$。

Künneth 分解与 (10) 给出完整联合来源恒等式
$$
\boxed{
\mathcal W_{a,\ell}(B)\,\mu_k
 =\nu_{D_{k,17}}\otimes\Lambda_{-,k,a,\ell}
  +\nu_{P_{+,k,17}}\otimes\Lambda_{+,k,a,\ell}.
}
\tag{11}
$$
(11) 在实际 $Y\times B$ 坐标下理解。右边的 $\Lambda_\pm$ 保留全部五个伙伴，包括共同深门、原两个 $C$ 支和 $\Delta_\ell$ 的符号。它们尚未被替换为质量。

原来源本身可以是任意有限个简单张量之和；(11) 只是对两维第一空间取一组基。其系数来源可用该有限空间的固定对偶坐标抽取。故无需假定原六 sigma 或任何条件来源本来可分离。

伙伴的正矩微分只作用 (9) 的第二因子，不生 $Y$ 导数。有限伙伴门在 R745 的 BK 规范下只改变 $\Lambda_\pm$，保每个实际 root-of-unity 因子。下文用到的 $\Lambda_\pm$ 的收缩都是原有限 torsion 和有限正矩的收缩；在原周期归一后其系数为代数数。这里没有声称任意 $p$-进条件积分都是代数数。

置
$$
C_\pm=\Lambda_\pm(1).
$$
去掉 $Y$-unit 后，(4) 的完整来源仍是裸 $\mathcal H_k$ 中的 type5：原六 sigma 的共同角型为0，正权总次数增加 $1\bmod6$，所有共同伙伴门均齐次不变。因此
$$
C_+=0,\qquad C_-=C_{k,a,\ell},\qquad
Y_*(\mathcal W_{a,\ell}\mu_k)=C_{k,a,\ell}\nu_{D_{k,17}}.
\tag{12}
$$
同一个实际系数由原正矩读取：
$$
\boxed{
C_{k,a,\ell}
 =\frac1{120\Omega^6}
  \int Y^5ZE^a\phi_{a,\infty}
       1_{\{Z,E\ {\rm unit}\}}\Delta_\ell\,d\mu_k .
}
\tag{13}
$$
(13) 不附 $Y$-unit，最高完整正矩次数为36；其余混次的周期归一沿用原权。没有预设每个 $C_{k,a,\ell}$ 非零。

对 $J=P,G,W_0,V_0$ 定义实际模 $p$ 函数
$$
\Phi_{J,\pm}(y)=
 \int 1_J(y,B)\,d\Lambda_\pm(B),
 \qquad y\in\mathbf F_p,
\tag{14}
$$
其中各门都含 $Y$-unit，故 $\Phi_{J,\pm}(0)=0$。从 (11) 逐项收缩得到
$$
\boxed{
\nu_{k,J,a,\ell}
 =\Phi_{J,-}(x)\nu_{D_{k,17}}(x)
  +\Phi_{J,+}(x)\nu_{P_{+,k,17}}(x).
}
\tag{15}
$$
这保全部伙伴相关性。函数 $\Phi$ 只依赖 $y\bmod p$，因为唯一涉及 $Y$ 的门是 (5) 的深度一门；伙伴门深度仍为原 $\ell$，没有被降成一层。

## 3. 规范 étale trace：完整相位、零 Fourier 项与倍率

本节说明在 (11) 的非简单张量来源上，规范 étale theta trace 正好计算 (14) 的加性平均。

固定原 formal 参数及 $\zeta_p$。令 $\mathsf T_s$ 为 R745/R752 的 canonical Mumford 平移，包含全部 BK 配对，则
$$
\nu_{\mathsf T_sF}(x)=\zeta_p^{sx}\nu_F(x),
\qquad s\in\mathbf F_p .
\tag{16}
$$
这是真实变量的平移公式，不由 $\log\zeta_p=0$ 推出。换 torsion 代表时必须同时保其完整配对，R742/R747 已支付这一点。

取共同覆盖
$$
a=[\bar\pi_0],\qquad
\mathcal L'=a^*\mathcal L_{34},\qquad\deg\mathcal L'=34p.
$$
$E[\bar{\mathfrak p}]=\ker a$ 的自然下降 lift 逐点固定 $a^*\mathcal H_k$。覆盖上的 formal 平移与这个 étale 子群之间的交换配对是 $e_p$ 的 $34$ 次单位幂，并含 $a$ 在 formal 子群上的实际单位变换。因 $p\nmid34$，该配对完美。

若 $v_{\pm,s}=a^*(\mathsf T_sD_k)$ 或 $a^*(\mathsf T_sP_{+,k})$，则对 $t\in E[\bar{\mathfrak p}]$，准确有
$$
\widetilde{\mathsf T}_t v_{\pm,s}
 =\langle t,s\rangle_{\mathcal L'}\,v_{\pm,s}.
\tag{17}
$$
不同 $s$ 给不同角色；同一个 $s$ 内两条线由 (10) 独立。这也给 (15) 的 $2p$ 个展开向量的唯一性。所用 lift 是自然下降 lift 和奇数阶对称 Mumford lift；不是仅 projective 的交换式，故 (17) 没有待定的整体符号。

定义规范平均
$$
\mathsf E_{\bar{\mathfrak p}}
 =\frac1p\sum_{t\in E[\bar{\mathfrak p}]}
             \widetilde{\mathsf T}_t.
\tag{18}
$$
由完整有限角色正交性，
$$
\mathsf E_{\bar{\mathfrak p}}v_{\pm,s}
 =\begin{cases}v_{\pm,0},&s=0,\\0,&s\ne0.\end{cases}
\tag{19}
$$
因此对实际展开
$$
\Phi_{J,\pm}(x)=\sum_s c_{J,\pm,s}\zeta_p^{sx}
$$
有
$$
\boxed{
\mathsf E_{\bar{\mathfrak p}}a^*F_J
 =a^*\{c_{J,-,0}D_{k,17}+c_{J,+,0}P_{+,k,17}\},
\qquad
c_{J,\pm,0}=\frac1p\sum_{y\in\mathbf F_p}\Phi_{J,\pm}(y).
}
\tag{20}
$$

同式先在联合来源上作用时，算子是
$\mathsf E_{\bar{\mathfrak p}}\otimes{\rm Id}_B$。故它严格交换所有伙伴 jet、所有只在 $B$ 上的 Fourier 平移，以及 (4) 中的有限门和两个 $C$ 支。混合浅门先用其真实有限加性展开，再按 (19) 保留全部第一频率之和为零的项。回到物理函数语言，所得恰为 (20) 的有限平均。

特别不能在混合浅门前先把 $\Lambda_\pm$ 换成质量；(20) 是在完整 $B$ 来源上取零第一频率后才收缩。这个先后顺序正是下一节纤维计数能够适用的原因。

将 (20) 沿真实 $a^*$ 下降，记所得算子为 $\mathsf{CT}_Y$。若在共同覆盖上直接计算负一值，原倍率是
$$
I_{-1}(a_*\nu)=\bar\pi_0^{-1}I_{-1}(\nu).
\tag{21}
$$
下降与 (21) 一起恢复原 $Y$ 变量及原 $\Omega$。所以 $\mathsf{CT}_Y$ 不附一个未指定的 period 或额外 $\bar\pi_0$ 因子。

由于 $\Phi_{J,\pm}(0)=0$，乘法平凡角色平均和 (20) 准确满足
$$
\boxed{
\widehat\Phi_{J,\pm}(1)
 :=\frac1{p-1}\sum_{y\in\mathbf F_p^\times}\Phi_{J,\pm}(y)
 =\frac p{p-1}\,c_{J,\pm,0}.
}
\tag{22}
$$
$p/(p-1)$ 必须保留。它的 $p$ 进赋值为1，不能说成单位；$c_{J,\pm,0}$ 本来允许含 $1/p$。

(18)–(22) 是几何 theta-group 平均及其实际下降，不是自然 Galois trace，也不是某个 ordinary deep-core。

## 4. $Z$-unit 纤维的两个零点与三个精确平均

固定 (11) 支持上的任一伙伴点。由 (4)，其 $Z$ 余类非零。在 $\mathbf F_p^\times$ 中，
$$
W=0\quad\Longleftrightarrow\quad
y=y_W:=-Z/b_Y,
$$
$$
V=0\quad\Longleftrightarrow\quad
y=y_V:=\alpha Z/d_Y .
\tag{23}
$$
两根均非零，而且
$$
y_W-y_V
 =-\frac{(d_Y+\alpha b_Y)Z}{b_Yd_Y}
 =-\frac{36Z}{b_Yd_Y}\ne0.
\tag{24}
$$
所以在每一个实际伙伴纤维上都有同一张精确计数表：
$$
\begin{array}{c|c|c}
J&\#\{y\in\mathbf F_p^\times:1_J(y,B)=1\}
& p^{-1}\sum_{y\in\mathbf F_p}1_J(y,B)\\ \hline
P&p-1&(p-1)/p\\
G&p-3&(p-3)/p\\
W_0&1&1/p\\
V_0&1&1/p .
\end{array}
\tag{25}
$$
两个不同深条带相交为空，$G$ 正是删掉它们的补集。

将 (14) 的有限和与原伙伴积分交换。这只是有限线性运算，对带符号的 $\Delta_\ell$ 及全部 $C$ 支同样成立。由 (25)，
$$
c_{J,\pm,0}
 =\frac1p\int\sum_{y\in\mathbf F_p}1_J(y,B)\,d\Lambda_\pm(B)
 =\frac{n_J}{p}C_\pm,
\tag{26}
$$
其中
$$
(n_P,n_G,n_{W_0},n_{V_0})=(p-1,p-3,1,1).
$$
现在才用 (12)。得到完整来源级 trace 公式
$$
\boxed{
\begin{aligned}
\mathsf{CT}_Y\nu_{k,P,a,\ell}
 &=\frac{p-1}{p}C_{k,a,\ell}\nu_{D_{k,17}},\\
\mathsf{CT}_Y\nu_{k,G,a,\ell}
 &=\frac{p-3}{p}C_{k,a,\ell}\nu_{D_{k,17}},\\
\mathsf{CT}_Y\nu_{k,W_0,a,\ell}
 &=\frac1p C_{k,a,\ell}\nu_{D_{k,17}},\\
\mathsf{CT}_Y\nu_{k,V_0,a,\ell}
 &=\frac1p C_{k,a,\ell}\nu_{D_{k,17}}.
\end{aligned}
}
\tag{27}
$$
所有 type3 的零 Fourier 系数都为零；其非零 Fourier 系数没有被宣称为零。

等价地，原乘法平均为
$$
\boxed{
\widehat\Phi_{J,-}(1)
 =\frac{n_J}{p-1}C_{k,a,\ell},\qquad
\widehat\Phi_{J,+}(1)=0.
}
\tag{28}
$$
这是对有限门系数函数的均匀平均，**不是**对原 theta 测度的均匀性断言。各原纤维的测度、相关性、正矩和条件质量全部包含在 $C_{k,a,\ell}$ 中。

## 5. 同原周期的点惯性分量与两条完整返回

每个 (15) 是模 $p$ 物理函数乘原两条测度的有限和。R748、R751 给它的全部合法 tame 角色的精确点公式；R752 支付从实际门到这些物理角色的来源恒等式。

将各点映到共同曲线 $E_1$ 后，在所选普通 $p$ 的惯性上，实际点角色为 $\chi^{-1}$。原 $D_k$ 允许 $\chi|_{\mu_6}=1$；$P_{+,k}$ 允许 $\chi(\zeta)=\zeta^4$，所以后者没有 $\chi=1$ 项。所有 algebraic 系数固定，不随点因子一起共轭。

在包含本篇有限点来源的一个共同有限 Galois 域中，令
$$
e_{I_p,1}=\frac1{|I_p|}\sum_{g\in I_p}g_{\rm pt}.
$$
用 R749 的点张量 logarithm 单射，得到其在该有限点-log 空间上的确切作用 $e_{I_p,1}^{\log}$。它是 $\overline{\mathbf Q}$-线性的，而不是定义在任意 $\mathbf C_p$ 数上的 Galois 运算。

由 R751/R752 与 (22)，
$$
e_{I_p,1}^{\log}\{\Omega I_{-1}(\nu_{k,J,a,\ell})\}
 =\frac p{p-1}\,
        \Omega I_{-1}(\mathsf{CT}_Y\nu_{k,J,a,\ell}).
\tag{29}
$$
代入 (27) 及 R752 的
$p_{\tau_k,a}(\ell)=C_{k,a,\ell}\Omega I_{k,1}$，得到本篇主式：
$$
\boxed{
\begin{aligned}
e_{I_p,1}^{\log}p_{\tau_k,a}(\ell)
 &=p_{\tau_k,a}(\ell)
   =C_{k,a,\ell}\Omega I_{k,1},\\
e_{I_p,1}^{\log}g_{\tau_k,a}(\ell)
 &=\frac{p-3}{p-1}\,p_{\tau_k,a}(\ell),\\
e_{I_p,1}^{\log}
       \{\lambda h_{\tau_k,a}^W(\ell)\}
 &=\frac1{p-1}\,p_{\tau_k,a}(\ell),\\
e_{I_p,1}^{\log}
       \{\gamma\lambda h_{\tau_k,a}^V(\ell)\}
 &=\frac1{p-1}\,p_{\tau_k,a}(\ell).
\end{aligned}
}
\tag{30}
$$
它对每个固定 $k,a,\ell$ 以及同一个完整权成立，不需要先对 $a$ 求和。

$\lambda,\gamma\lambda$ 是原来源返回的实际代数标量，故可由点因子投影提出，但不能删除。若单独询问裸 $h^W,h^V$，相应右边还须分别除以 $\lambda,\gamma\lambda$。

若某个 $C_{k,a,\ell}=0$，(30) 只给这些平凡惯性分量为零，不给整个实际支为零。若 $C_{k,a,\ell}\ne0$，由原 $I_{k,1}\ne0$ 及 $p>3$，三个补支均有非零的该点分量，因而三个有限负一值本身都非零。

不同 $k$ 的两项还由原十七处 cubic 点角色分离。若把 $k=2,4$ 加回，(30) 仍逐分量成立，不会将两个原独立 logarithm 合并成一个系数。

## 6. 原有限过滤器给三条非零的补偿份额

为明确它在原非零行上的用途，完整保 R742 的原过滤器。令 $\mathsf T_2$ 对 $r$ 作实际偶移位，定义
$$
\begin{aligned}
\mathscr P&=\prod_{j=1}^{31}(\mathsf T_2-\lambda^4\kappa^{2j}),\\
\mathscr Q&=\prod_{a=0}^{30}(\mathsf T_2-\lambda^6\kappa^{2(a+1)}),\\
c_a&=-\chi_A\lambda^3\kappa^{a+1},\\
U_{31}&=\prod_{j=1}^{31}(1-\kappa^{2j}),\qquad
V_{31}=\prod_{j=1}^{31}(1-\lambda^2\kappa^{2j}).
\end{aligned}
\tag{31}
$$
$\mathscr Q_{\ne a}$ 表示删掉对应因子。对任意一组同范围的实际行 $f_a(\ell)$，记
$$
\mathcal L_r[f]
 =\frac{p-1}{b_Y}\mathscr P
    \sum_{a=0}^{30}\mathscr Q_{\ne a}
     \{\lambda^{r+2}f_a(r+2)
            +c_a\lambda^{r+1}f_a(r+1)\}.
\tag{32}
$$
所有标量、门和观察均与 R742 相同。

R742(33) 准确给
$$
\mathcal L_r[p_{\tau_k}]
 =R_k(r):=
 \frac{(p-1)(-1)^r}{b_Y}\lambda^{2r+248}
 U_{31}V_{31}\mathfrak I_{k,\infty}\ne0,
\tag{33}
$$
其中
$$
\mathfrak I_{2,\infty}
 =\Omega(c_\infty/a_\infty)I_{2,1},
\qquad
\mathfrak I_{4,\infty}
 =\Omega a_\infty^{-1}I_{4,1}.
$$
这里非零性是原 R733/R735 的点 logarithm 结论及完整实际系数返回，不是本篇再作适配。

对固定 $r$，(32) 只含有限个门，范围是
$0\le a\le30,\ r\le\ell\le r+124$。可以在同一个有限点载体上施惯性投影。因为 (30) 的比例独立于 $a,\ell$，而投影固定全部代数标量，所以
$$
\boxed{
\begin{aligned}
e_{I_p,1}^{\log}\mathcal L_r[g_{\tau_k}]
 &=\frac{p-3}{p-1}R_k(r),\\
e_{I_p,1}^{\log}\mathcal L_r[\lambda h_{\tau_k}^W]
 &=\frac1{p-1}R_k(r),\\
e_{I_p,1}^{\log}\mathcal L_r[\gamma\lambda h_{\tau_k}^V]
 &=\frac1{p-1}R_k(r).
\end{aligned}
}
\tag{34}
$$
三条右边均非零。特别 $r=1$ 时，所有实际门至多125层；伙伴仍可以含这些高深度 torsion，但第一 $Y$ 角色始终仅为模 $p$ 的 tame 角色。

也可不用过滤器作非零表述：R752(32) 保证对每个固定合格 $p$、每个 $k$、每个 $r$，上述有限指标集合中至少一个 $C_{k,a,\ell}\ne0$。该指标对应的三条补支各有 (30) 中的非零分量。这不是为所有 $p$ 指定同一个 $a,\ell$，也不是逐指标的非零结论。

## 7. 原外部与主目标的准确边界

源级恒等式 (8) 以及 R747 的完整返回仍给
$$
p_{\tau_k,a}(\ell)
 =g_{\tau_k,a}(\ell)
    +\lambda h_{\tau_k,a}^W(\ell)
    +\gamma\lambda h_{\tau_k,a}^V(\ell).
\tag{35}
$$
(30) 中三个比例之和严格为1，故 (35) 的平凡点分量正好完整补回 primitive。其余合法 tame 角色也仍按原来源唯一展开逐项相消；本篇没有把它们删掉。

对 R742 的原 paired-$T$ 外部，全部物理换元、共轭投影和原权保持后，仍有
$$
\mathcal O_{\tau_k,{\rm pair}}^T
 =-\mathcal I_{\tau_k,{\rm pair}}^T.
\tag{36}
$$
当 (35) 的有限负一部分在该完整外部链中出现时，(30)、(34) 给出它实际携带的点分量；不能据此给任一未识别的外部整体赋零。特别本篇始终保两个完整 core 返回，未取 $\kappa=0$，未省其条件质量或 logarithm 补偿。

本篇所有点因子操作只作用于已经用 R748/R751 识别的有限点载体。原 $J'_S,J'_T,J'_U$ 的标量零假设，尚未被转换为一个全体外部项都在该有限载体中、且所有真实权与观察完整可见的附加关系。因此不能从那些标量假设直接断言 (30) 或 (34) 的单独一项应为零。

也没有对整条无限
$\log(1+\kappa\,\text{线性行}/\text{单位行})$
施一个未经证明连续的点投影。R742 的 $u\to0$ 已在 R752 的固定有限坐标中支付；R749/R753 的一般不连续性边界仍保留。

本篇新增的是：原同一有限门的三个实际补支，其规范 étale trace、平凡点系数和原非零过滤行的份额都已确定。它们的非零与原全外部补偿相容；原主中央缺口仍需完整同域的进一步算术关系。

## 依赖与可复现范围

- [R742](R742-fixed-seventeen-operators-and-same-gate-primitive-limit.md)：原同门十七处投影、全部 $u=0$ 权、有限过滤器及两条非零 primitive 行。
- [R745](R745-finite-p-gates-algebraic-theta-sources-and-orthogonal-jets.md)：完整正交 theta 分裂、有限 torsion 和伙伴 jets 的代数性与周期。
- [R747](R747-original-source-restoration-and-p-primary-gate-model.md)：四个 raw 门、两条 core 逆返回、完整 quarter 相位与原观察。
- [R752](R752-native-mod-p-two-source-closure-and-point-inertia-extraction.md)：第一 $Y$ 模 $p$ 闭包、两个完整 dyadic 来源、$2p$ 向量独立、规范 étale 平均及 primitive 正36矩。
- [R748](R748-original-type-five-ramified-good-pair-and-point-eigenspaces.md)、[R751](R751-second-dyadic-character-point-fields-and-inertia-extraction.md)：两来源的全部有限角色、原共同周期及实际点惯性。
- [R749](R749-point-factor-projectors-and-finite-character-extraction.md)：固定代数系数的点因子投影与 logarithm 单射；其有限载体限制保留。

本篇没有新的数值计算或可重算数据。全部新增公式由原完整来源、规范有限 theta 平均和逐伙伴纤维的两个零点计数严格推出。
