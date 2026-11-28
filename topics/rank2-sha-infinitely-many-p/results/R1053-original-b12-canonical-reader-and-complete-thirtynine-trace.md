# R1053 — 原 B12 商的完整 canonical 读者、六极补偿与三十九支返回

按根 README 第8条登记完整证明；原 notes 路径保留转向。除本篇明示的已证范围外，课题主目标仍未完成。

日期：2026-11-28 UTC。

**已证明：** R1037/R1038 的原两条 degree390 来源，先作真正的 B12 商和完整有限投影，给出固定秩至少二曲线 $E_{3969}$ 的一个准确 canonical 必要零行。下面将这一行写回原390来源，保留所有实际 CM 纤维、二挠 Miller 权、degree378 电荷及原有理 frame；并给其完整三十九支 differential trace。该读者在原点出现的六极，被投影后来源增加的六阶零准确补偿。因此它不能只凭极帽充当 R1028 §9 中的六阶终端 cut。

本篇不新增数学运行，不重算 R1037 的谱或 R1038 的完整来源。输入和全部算术授权只取这两个已付结果；没有把任意商、投影或环境六阶矩赋予 canonical 零。

## 1. 同一来源与完整有限投影

保持 $E_0:y^2=x^3+1$、$X=x^3$、$\omega_E=dx/(2y)=dz$，以及原 sigma 的刚性化。设
$$
f_A=\Psi_{35}=\sigma^{390}P_A(X),\qquad
f_B=\Psi_{53}=\sigma^{390}P_B(X).
$$
两者的完整向量、首六阶及全有限来源均为 R1037(1)–(5) 的输入。令
$$
B_{12}=\sigma^{12}y^2,\qquad
\operatorname{div}(B_{12})=6[O]+2\mathcal D_2,
\qquad
F_\nu=f_\nu/B_{12}\in H^0(E_0,L_{378}),
\tag{1}
$$
其中 $L_m=\mathcal O(mO)$，$\mathcal D_2=E_0[2]-[O]$。这里是全局整截面的商，不是截断级数的商。

完全沿 R1037(25)–(32)，置
$$
C=N_{19}N_{13}^{-2},\qquad
H=CN_{31}^{-1},\qquad
A=N_{13}H^{-4}C^{-5},
\quad \zeta_6=-\omega.
$$
这些是同一 degree378 空间上的实际完整算子，并满足
$A^6=C^6=I$、$H^9=I$。所需幂等元准确为
$$
\boxed{
\Pi_E=
\left(\frac16\sum_{i=0}^5\zeta_6^{-5i}A^i\right)
\left(\frac16\sum_{j=0}^5\zeta_6^{-4j}C^j\right)
\left(\frac19\sum_{k=0}^8\zeta_6^{-2k}H^k\right).
}
\tag{2}
$$
它保全部324项，标签正是 $[5,4,\mathrm{linear},2]$。这里未逆转 R1037 的 $N_\gamma=M_\gamma/\gamma$ 方向。逆算子可在同一有限阶空间中用正幂表达；并未把旧 degree390 的 norm13 算子当作可逆 good 算子。

由同一次完整谱，
$$
\Pi_E=\Pi_{2,-}\Pi_{\delta,\mathrm{old}}\Pi_E,\qquad
\Pi_{2,-}=(I-D_2)/2,\quad
\Pi_{\delta,\mathrm{old}}=E_{126}T_{126}/3.
\tag{3}
$$
因此如需显写全部二处和三处图，可在(2)前加入(3)的真实完整词；这是同一幂等元的恒等式，不是换一个来源。

R1037(41)及 R1038 的完整算术识别给
$$
\begin{aligned}
\Pi_EF_A&=-\frac{185328}{35}\Phi_{378},\\
\Pi_EF_B&=-\frac{160056}{835}\Phi_{378},\\
\Pi_E(F_A-F_B)&=-\frac{29829384}{5845}\Phi_{378},
\end{aligned}
\qquad
\Phi_{378}=\delta^{-6}[\delta]^*\Phi_{126}.
\tag{4}
$$
$\Phi_{126}$、$\Phi_{378}$ 都按原点首项 $z^6$ 归一。$\Phi_{126}$ 是 R1038 已付的 $E_{3969}:Y^2=X^3+3969$ 的真正全 canonical 来源，且该曲线的秩至少二。式(4)不是仅由三个好位猜出的角色身份。

对允许的 inert 素数 $p$，如果该固定曲线的通常全 $\Sha[p^\infty]$ 不有限，R1038 的原通常 Selmer 比较给 $J'_{\Phi_{126}}(0)=0$，从而也给 $J'_{\Phi_{378}}(0)=0$。以下仅使用它所蕴含的指定除 $p$ 首行零，不把首行零反推整个中央零。

## 2. 写回 degree390 时的全部 Miller 费用

在子空间 $B_{12}H^0(L_{378})\subset H^0(L_{390})$ 上定义
$$
\widetilde\Pi_E=B_{12}\Pi_E B_{12}^{-1}.
\tag{5}
$$
它是这个实际子空间上的幂等元。对任意 degree390 截面先除以 $B_{12}$，所得未必整；本篇没有扩大其整定义域。

二挠点 $T=(e,0)$、$e^3=-1$ 的原 lift 满足
$$
q_T^2=\frac{e^2}{\sqrt3}(x-e),\qquad
\boxed{B_{12}T_T^{378}B_{12}^{-1}=q_T^{-4}T_T^{390}.}
\tag{6}
$$
这是 R1037(6)–(7) 的全函数身份。$q_T^{-4}$ 在 $T$ 有四阶极、在 $O$ 有四阶零；因为 $x-e$ 在 $T$ 是二阶零，不能把这里误算为二阶极。完整词作用在(5)的子空间时，所需消极由真正的 $B_{12}$ 除子提供。

对原 $\gamma\in\{\gamma_{13},\gamma_{19},\gamma_{31}\}$，令
$$
r_\gamma(z)=\frac{\sigma(\gamma z)}{\sigma(z)^{N\gamma}}.
$$
若 $f=\sigma^{390}R_f$，则完整共轭后的 CM 词为
$$
\begin{aligned}
&B_{12}M_{\gamma,378}(f/B_{12})\\
&\quad=\sigma(P)^{390}
\operatorname{Tr}_{[\gamma]}
\left[
\left(\frac{r_{\bar\gamma}(Q)}{r_\gamma(Q)}\right)^{390}
C_\gamma(Q)\,R_f([\bar\gamma]Q)
\right],
\qquad [\gamma]Q=P,
\end{aligned}
\tag{7}
$$
其中准确的额外有理权为
$$
\boxed{
C_\gamma(Q)=
\left(\frac{r_\gamma(Q)}{r_{\bar\gamma}(Q)}\right)^{12}
\frac{y([\gamma]Q)^2}{y([\bar\gamma]Q)^2}
=\frac{B_{12}([\gamma]Q)}{B_{12}([\bar\gamma]Q)}.
}
\tag{8}
$$
最后一个比值使用同 norm 拉回的原刚性化，因而是有理函数。证明只需在原 degree378 trace 中代入
$R_{f/B_{12}}=R_f/y^2$，再把390与378相差的十二次幂完整移入 integrand。所有 $\gamma^{-1}$ 归一仍随 $N_\gamma=M_\gamma/\gamma$ 保留。

其全部零极准确为
$$
\operatorname{div}(C_\gamma)
=6\bigl([\gamma]^*[O]-[\bar\gamma]^*[O]\bigr)
+2\bigl([\gamma]^*\mathcal D_2-[\bar\gamma]^*\mathcal D_2\bigr).
\tag{9}
$$
交叠点按此有符号除子相消；没有挑一个 CM 根或删除一条纤维。(6)–(9)按(2)的原次序复合，就给(5)的全部词。中间的 $B_{12}$ 因子只可在真实复合中抵消，不能将 $C_\gamma$ 单独提到 trace 外，也不能把这些加权 norm13 词换成旧390上的未加权 norm13 操作。

特别是，(4)所给的最终高零是**完整投影求和后**的事实；不声明(2)每个独立词都具有相同的高零。

## 3. 原有理 frame 上的准确 canonical 首行

现在取 $p\equiv-1\pmod6$、$p>13^4$，删去原来源及有限刚性化的固定坏集，在完美好剩余域 $k$ 上工作。保持 R853(1)–(2) 的同一 $M=1$ 有理模型
$$
DZ=1,\quad Z=z+O(z^{5p}),\qquad
\mathcal P_2=-\nabla_2^{p-1}(Z^{p+1}),\quad
\nabla_2=D-2G,\quad
\nabla_2\mathcal P_2=2H^pZ^{p+1}.
\tag{10}
$$
这里没有使用大 level frame 的 CM 交织；有限投影先在特征零的完整来源上作出，然后才取这个指定有理替身。

写
$$
\Pi_EF_\nu=\sigma^{378}R_{E,\nu},\qquad
g_\nu=\widetilde\Pi_Ef_\nu=\sigma^{390}R_{g,\nu}.
$$
则全有理身份为
$$
R_{g,\nu}=y^2R_{E,\nu},\qquad
\widehat B_{12}=\mathcal P_2^6y^2,
$$
$$
\boxed{
\widehat F_{E,\nu}
=\mathcal P_2^{189}R_{E,\nu}
=\widehat B_{12}^{-1}\mathcal P_2^{195}R_{g,\nu}.
}
\tag{11}
$$
式(11)是把原来源写回390 frame的确切形式；没有把 $\Pi_E$ 与 $\mathcal P_2$ 免费交换。

定义指定原首行和微分
$$
a_{E,\nu,p}=[z^{p+1}]\widehat F_{E,\nu},\qquad
\eta_{E,\nu,p}=Z^{-p-2}\widehat F_{E,\nu}\,\omega_E.
\tag{12}
$$
原点的来源从六阶起，所需相对系数仅到 $p-5$。R853所用的通用有限递推在这些阶上所有积分分母都是 $p$ 单位；(10)的原初始资料因此与 $\sigma^2/z^2$ 的相应整 jet 一致。将它取189次幂并乘同一个完整 $R_{E,\nu}$，仍给原 $\Pi_EF_\nu$ 的 $z^{p+1}$ 系数。首次 Gaussian 修正不进入这个系数。这里不需在 $p$ 以上把两条全函数或 frame 认成相等。

设 $a_{378,p}$、$a_{126,p}$ 对应(4)的两条规范来源。原实际 $\delta$ 拉回直接给
$$
\boxed{
a_{378,p}=\delta^{p-5}a_{126,p}
=-\frac19a_{126,p}.
}
\tag{13}
$$
使用的是 $\delta^p=-\delta$、$\delta^4=9$，不是自由更换 CM 方向。若以各自的 $m\,p c_\sigma$ 归一为原 $J'_m(0)/p$，还须保 $378/126=3$，故比例是 $-1/27$，与 R1038 的整个 Newton 运输一致。

于是 $E_{3969}$ 的原坏条件给
$$
a_{378,p}=a_{E,A,p}=a_{E,B,p}=0
\tag{14}
$$
（固定非零尺度沿(4)保留）。这是本篇实际使用的算术授权，未赋予任何其它投影或单独 CM 字中央零。

## 4. 全极、六极补偿及第四次 Cartier

先说明(11)的原点费用。由(4)及真正的线丛乘法，
$$
\operatorname{ord}_O(g_\nu)=12,\qquad
\operatorname{ord}_O\widehat B_{12}=6.
\tag{15}
$$
因此除去 $\widehat B_{12}$ 后，$\widehat F_{E,\nu}$ 恰恢复六阶。原390的 $f_A,f_B$ 也是六阶；(15)没有为其增加净六阶耗费。

其余点也不能省略。由 R1038 的完整乘积
$$
\Phi_{126}=\frac{\sigma^{126}}{91}
X(X+1)(X+4)(X-8)^2
(7X^2-4X+16)\,C_3(X)D_{13}(X)S_7(X),
$$
其中 $C_3,D_{13},S_7$ 始终是 R1038 原多项式，在 $X=-1$ 的后三值为
$-81,729,-19683$，而 $7X^2-4X+16$ 的值为27。因此 $\Phi_{126}$ 在每个非零二挠点准确二阶零。在 $\ker[\delta]$ 上用真正的 étale 拉回(4)，得到
$$
\begin{array}{c|ccc}
 &O&\ker[\delta]-\{O\}&\mathcal D_2\\ \hline
\Phi_{378}&6&6&2\\
g_\nu=B_{12}\cdot\text{非零标量}\cdot\Phi_{378}&12&6&4.
\end{array}
\tag{16}
$$
$[\delta]$ 在 $\mathcal D_2$ 上置换，所有上述准确阶在所删固定坏集之外保持。

令
$$
d_p=p^3-p^2+p+1.
$$
R853的同一全极证明给：$\mathcal P_2$ 只在 $\mathcal D_2$ 可能有极，那里极阶 $d_p$；在 $O$ 阶二；在每个其它 $Z$ 零点阶至少 $p$。两个非零 $\ker[\delta]$ 点确是 $Z$ 的简单零，因为原 $\mathscr R_p(x)$ 含 $x$ 且首系数 $1/2$、那里 $y=\pm1$。

于是(11)的所有费用为
$$
\begin{array}{c|ccc}
 &O&\ker[\delta]-\{O\}&\mathcal D_2\\ \hline
\mathcal P_2^{195}R_{g,\nu}&12&
 \ge195p+6&-195d_p+4\\
\widehat B_{12}&6&\ge6p&-6d_p+2\\
\widehat F_{E,\nu}&6&
 \ge189p+6&-189d_p+2.
\end{array}
\tag{17}
$$
中间一列的相除应使用同一个实际 $\operatorname{ord}\mathcal P_2$，所以最后一行是由(11)直接算出的下界，而非将两个独立下界相减。其它 $\mathcal P_2$ 零点也在(11)中只剩189次非负幂。没有由形式分母 $\widehat B_{12}^{-1}$ 产生遗漏的极。

完整 $\eta_{E,\nu,p}$ 只在 $O,\mathcal D_2$ 有极：
$$
\operatorname{ord}_O\eta_{E,\nu,p}=4-p,\qquad
\operatorname{Res}_O\eta_{E,\nu,p}=a_{E,\nu,p},
$$
$$
\operatorname{pole}_{\mathcal D_2}\eta_{E,\nu,p}
\le189d_p-p(p+2)-2<189p^3.
\tag{18}
$$
在其它 $Z$ 零点，(10)给 $\operatorname{ord}\mathcal P_2\ge p$，故 $Z^{-p-2}$ 的极被完整189次幂抵消。

逐次 Cartier 的局部公式遂给
$$
\mathcal C^3\eta_{E,\nu,p}
\in H^0(E_0,\Omega^1(O+189\mathcal D_2)).
$$
原 $\mu_6$ 型为零；下降到 $t=-x^{-3}$ 后，正好落在
$$
H^0\!\left(\mathbf P^1,\Omega^1([0]+95[1])\right).
$$
因 $95<p$，所有高极项唯一可积分，唯一非 exact 方向由原点留数固定。沿 R853(19)–(22)的同一符号，
$$
\boxed{
\mathcal C^4\eta_{E,\nu,p}
=-a_{E,\nu,p}^{1/p^4}\frac{x^2}{y}\omega_E.
}
\tag{19}
$$
本段只是把完整全极论证用于真正的189次来源；没有把这一标量的非零当作已知。

(15)–(18)还说明为什么不能据形式六极直接消费 R1028 §9 的候选。原点净阶没有下降；$\pm S$ 上原 $M=1$ frame 的真实高零也必须保留。另一方面，R1028 的 native39读者使用的是 target $P_{10}$ 与全部39条 Miller 权，不是(11)的 source $\mathcal P_2^{189}$。要比较这两个具体读者，须另外支付其完整 frame、投影和移点身份；本篇不据(17)对那个尚未相认的读者预断零或非零。

## 5. 完整三十九支 differential trace仍读同一首行

取原 $\pi=4+\omega$、$\alpha=\delta\pi$，$N\alpha=39$。对任意微分均用完整未平均 trace。因为 $[\alpha]$ 是 odd-degree 同源，它在 $\mathcal D_2$ 上置换，故
$$
\operatorname{div}\operatorname{Norm}_{[\alpha]}(y)
=[\alpha]_*(\mathcal D_2-3O)
=\mathcal D_2-3O.
$$
因此 $\operatorname{Norm}_{[\alpha]}(y)=c_\alpha y$。这也逐点核定了 infinity 规范：以 target 的原微分参数 $z$ 写完整39个局部分支，过 $O$ 的分支首项是 $z/\alpha$，其余分支以 $T\in\ker[\alpha]-\{O\}$ 起始。由 $y=-z^{-3}+\cdots$，准确有
$
c_\alpha=\alpha^3\prod_{0\ne T\in\ker[\alpha]}y(T)\ne0.
\tag{20a}
$
每个非零核点都不是二挠点，故乘积确实非零；常数的值不进入 $d\log$。在每个二挠点，pushforward 除子系数恰为一，因为 $[\alpha]$ 在完整 $E[2]$ 上是双射，且所有同源分支未分歧。保全部39支后，
$$
\boxed{
\operatorname{Tr}_{[\alpha]}
 \left(\frac{x^2}{y}\omega_E\right)
=\frac13d\log\operatorname{Norm}_{[\alpha]}(y)
=\frac{x^2}{y}\omega_E.
}
\tag{20}
$$
这里没有39倍：右边是一个实际对数微分的 norm 公式。也没有挑一条核分支。

设
$$
\Xi_{E,\nu,p}=\operatorname{Tr}_{[\alpha]}\eta_{E,\nu,p}.
$$
在 target 坐标中，其实际完整表达为
$$
\boxed{
\Xi_{E,\nu,p}
=\alpha^{-1}\,
\operatorname{Tr}_{k(E_0)/[\alpha]^*k(E_0)}
 \left(Z^{-p-2}\mathcal P_2^{189}R_{E,\nu}\right)
\,\omega_{E_0,\mathrm{target}}.
}
\tag{21}
$$
$\alpha^{-1}$ 来自 $[\alpha]^*\omega_E=\alpha\omega_E$。例如对常微分，(21)的规范给 $\operatorname{Tr}_{[\alpha]}\omega_E=(39/\alpha)\omega_E=\bar\alpha\omega_E$，所以一般的 degree39 因子没有遗漏；(20)的标量一则由其实际对数 norm 决定。式(21)保 source 的完整 $Z,\mathcal P_2$，不得在 trace 内偷换成 target 的相应函数。

Cartier 与完整 étale trace 交织，(19)–(20)给
$$
\boxed{
\mathcal C^4\Xi_{E,\nu,p}
=-a_{E,\nu,p}^{1/p^4}\frac{x^2}{y}\omega_E.
}
\tag{22}
$$
也可直接核原点留数：source $\ker[\alpha]-\{O\}$ 不属于 $\mathcal D_2$，(18)在这些点正则，所以完整 trace 的 target 原点留数准确是 $a_{E,\nu,p}$。这与(22)一致。

由此已经得到一个不丢支、同原 canonical 授权的完整39支读者。它是普通微分的 scalar trace；这并不把 degree378 theta 截面认成原 degree10 来源。

## 6. 为什么 theta 中间层必须保十三维 carrier

为明确上一句，将全线丛也保住。因为 $L_{378}\simeq[\delta]^*L_{126}$，projection formula 和原三阶 kernel 的完整字符分解给
$$
[\alpha]_*L_{378}
\simeq
\bigoplus_{\chi\in\widehat{\ker[\delta]}}
[\pi]_*(L_{126}\otimes\mathcal L_\chi),
\tag{23}
$$
其中 $\mathcal L_\chi$ 是相应三挠 degree0线丛。每项秩13、度126；整个左边秩39、度378。这里可在包含这些固定字符的好常数域上写分解，随后按实际 Galois 作用下降，不改原来源。

每个 rank13 项还稳定。对 $L=L_{126}\otimes\mathcal L_\chi$，
$$
[\pi]^*[\pi]_*L
\simeq\bigoplus_{T\in\ker[\pi]}t_T^*L.
\tag{24}
$$
右边是13个 degree126线丛的直和，故半稳定。若 $F$ 是 $[\pi]_*L$ 的 rank $r$ 子丛，拉回给
$13\deg(F)/r\le126$。因 $\gcd(13,126)=1$，对 $0<r<13$ 不可能等号，故严格稳定。不同 $T$ 的线丛也互异，因为 $126T=0$ 与 $13T=0$ 同时成立只可能 $T=0$。这给了具体的完整 carrier，而不是按数值维数猜测。

(4)的实际 $\delta$-old 来源只落在(23)的平凡 $\chi$ 项；完整未平均三支 trace准确为
$$
T_{126}\Phi_{378}
=3\delta^{-6}\Phi_{126}
=-\frac19\Phi_{126}.
\tag{25}
$$
随后仍是 $[\pi]_*L_{126}$ 的完整十三维部分。选定来源的 good $N_{13}$ 本征关系是同 charge126 的 Hecke pull/trace；它不是把126除以13得到另一条整次数 theta 线丛。

旧390恰有 $390=39\cdot10$，故其原 level39 theta 运输使用 $L_{10}$。而 $378/39=126/13$ 不是整数，(23)不能被同一度数除法改成 $L_{10}$。这不禁止对真正微分作(21)的 scalar trace，也不排除某个另证的特定函数关系；它只保留该关系成立前所必需的全部中间来源。

## 7. 已闭合的关系与仍须实际支付的连接

从原坏条件到(14)、再到(19)和(22)，是同一固定秩二曲线、同一两个390输入和同一完整投影的必要关系。所有二挠和 CM Miller 权已在(6)–(9)给出，原点及二挠费用已在(15)–(18)计完，原39支在(20)–(25)完整保留。

下一项实质比较必须把(21)与 R1028 的原 target $P_{10}$、$W_t^p$、十三字及 native 三角窗逐式相认或给一个真正的新消元。仅有(11)的六极写法不支付 $c=6$ 终端非零；仅有(22)的固定对数直线也不支付无穷多个目标素数上的非零。

依赖：R1037完整谱及回执；R1038全 canonical/通常群桥和 live degree126来源；R853指定有理 frame与全极 Cartier证明；R1028 §9同一原读者的真实支持阈值。