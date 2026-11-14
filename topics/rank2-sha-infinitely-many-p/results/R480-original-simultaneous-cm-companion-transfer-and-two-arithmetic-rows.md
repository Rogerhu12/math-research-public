# R480 — 原二输入的同时 CM 迹、伴随投影及完整两条算术中央行

日期：2026-11-14。**状态：已证明。** 在 R474、R477 的同一个
压缩二输入中，norm $7$、$19$ 的完整同时 CM trace 与 determinant
$17$ 的输出变换严格相容。由此把第一轴的真实新曲线投影移到
伴随轴，第一单位条件完全保留。还得到一个统一的伴随算子，
在实际总来源上准确抽出 $S_{\rm new}$ 与 R476 的
$H_{\rm ref}$ 两条已识别算术线。两个参考伴随质量相消而来源
不相消；任意移动测试的质量导数项仍须保留。主目标未完成。

## 1. 两个真实原输入态与完整 CM 相位

全篇保持 R474、R477 的同一 $b=17$、普通周期和
$$
F=\sigma^4\sigma(2z)\sigma(8z)=F_1+F_2,\qquad H=\Theta^2,
$$
$$
\lambda=-\bar\pi_0^{-1},\qquad\beta=-\lambda,\qquad
\kappa=p/\bar\pi_0^2,\qquad d=p-1.
\tag{1}
$$
这里 $F_1,F_2$ 是 R474 的完整十三列投影：
$$
N_7F_1=F_1,\qquad N_7F_2=\omega^2F_2,\qquad
F_1(0)=\frac1{6b},\quad F_2(0)=-\frac1{6b},
\tag{2}
$$
其中
$$
N_a=\mathscr M_a/a,\qquad
\gamma_7=(5+\delta)/2,\quad\gamma_{19}=4+\delta,\quad
N_7=N_{\gamma_7},\quad N_{19}=N_{\gamma_{19}}.
$$
R474 已付 $N_7H=-\omega H$。本篇再对整个 degree72 principal
空间计算完整 norm-nineteen 纤维，准确得到
$$
\boxed{
N_{19}F_1=-\omega^2F_1,\qquad
N_{19}F_2=-F_2,\qquad
N_{19}H=-H.
}
\tag{3}
$$
前两个共同 $(N_7,N_{19})$ 特征空间在该十三维格中都恰为一维。
这个事实不用于给它们另认一条未付有限角色的椭圆曲线。

证书使用 $\gamma_{19}=4+\delta$ 的原除法多项式
$q_{19}=\sigma(\gamma_{19}z)/(\gamma_{19}\sigma(z)^{19})$。
对十三个完整目标 $x=1,\ldots,13$，在十九度商环中计算所有
原 $23$ 或 $13$ 类似基列的全 trace；本篇 degree72 实际只有
十三列。所有非零目标的原点分母先在商环中求逆并核乘积为一，
不选择某一个 CM 逆像。degree4 的 $H$ 另用完整的一维纤维
核定。得到的整个十三维 $N_{19}$ 矩阵与原 $N_7$ 交换，
$N_{19}^6=I$；这包含 (3) 的绝对号。

令原物理输入仍为 $A$（六 sigma 总输出）和 $D$（两 Theta
总输出），并定义
$$
W=A+4D,\qquad V=2A-9D.
$$
两个完整来源是
$$
\Phi_i(w,v)=F_i(w+2v)H(4w-9v),\qquad i=1,2.
\tag{4}
$$
因此 $\Phi_1+\Phi_2=\widetilde\Phi$ 正是 R477 原来源。
它们属于同一个标准
$\mathcal S_{136}\boxtimes\mathcal S_{612}$，并有
$$
\Phi_i(\zeta w,\zeta v)=\Phi_i(w,v)\qquad(\zeta\in\mu_6).
\tag{5}
$$

## 2. determinant $17$ 与全部 CM 纤维的精确相容

完整生成变量的矩阵为
$$
T^t=\begin{pmatrix}1&2\\4&-9\end{pmatrix},\qquad
T\begin{pmatrix}72&0\\0&4\end{pmatrix}T^t
=\begin{pmatrix}136&0\\0&612\end{pmatrix},\qquad\det T=-17.
\tag{6}
$$
取 $a=\gamma_7,\gamma_{19}$ 或其共轭。因 $17$ 与 $Na=7,19$
互素，$T^t$ 在完整 $E[a]^2$ 上为双射。
这支付的是两个 CM 纤维的完整重排，不是将两个 trace
分别替换为某个抽样支。

用 R470 的原对称平移
$$
(T_t^{(N)}G)(z)=e^{-N\eta_t(z+t/2)}G(z+t),
$$
完整规范可写为
$$
N_aG(z)=a^{-1}\sum_{t\in E[a]}
 (T_{\bar at}^{(N)}G)(\bar az/a).
\tag{7}
$$
在二变量中，两边的归一常数同为 $a^{-2}$。
以 (6) 重排 $E[a]^2$ 后，每个来源值准确对应；
两个对称平移指数也由 (6) 的 Gram 身份逐项相等。
所有 theta 次数均偶且为原标准半特征，所以没有再添一个
未定的 odd-character 常数。于是完整恒等式为
$$
\boxed{
(N_{a,W}\otimes N_{a,V})\Phi_i
=\bigl[(N_{a,72}F_i)(w+2v)\bigr]\,
 \bigl[(N_{a,4}H)(4w-9v)\bigr].
}
\tag{8}
$$
该证明保留 (7) 的每个中心相位和全部 $7^2$、$19^2$ 支。

代入 (2)、(3)，令
$$
(\chi_1,\tau_1)=(-\omega,\omega^2),\qquad
(\chi_2,\tau_2)=(-1,1),
\tag{9}
$$
便得到两个真实同时特征：
$$
\boxed{
N_{7,W}N_{7,V}\Phi_i=\chi_i\Phi_i,\qquad
N_{19,W}N_{19,V}\Phi_i=\tau_i\Phi_i.
}
\tag{10}
$$

## 3. 用共轭小 norm trace 支付逆算子

这里不把有限 Heisenberg 交织的比例常数留作猜测。
在整个 $\mathcal S_{136}$ 上，
$N_aN_{\bar a}$ 实现恒等的完整含中心自同构，故为标量。
原非零 $S(2z)$ 锚给
$$
N_7S(2z)=-S(2z),\qquad N_{19}S(2z)=\omega S(2z).
$$
$S(2z)$ 的原代数系数为有理数，共轭完整 trace 给相反 CM
方向的特征 $-1,\omega^2$。所以标量恰为一：
$$
\boxed{
N_{\bar\gamma_7,136}=N_{7,136}^{-1},\qquad
N_{\bar\gamma_{19},136}=N_{19,136}^{-1}.
}
\tag{11}
$$
完整二十三维矩阵也独立核出这两个恒等式。

记 $\Pi_{0,W}$、$\Pi_{0,V}$ 为真实 $\mu_6$ 平均。由 (5)，
$$
\Phi_i^0:=\Pi_{0,W}\Phi_i=\Pi_{0,V}\Phi_i.
\tag{12}
$$
设 $\mathcal V_i\subset\mathcal S_{612}$ 为
$\Phi_i^0$ 在第一轴任意基展开时的全部第二轴系数所张空间。
(10)、(11) 说明 $N_{7,V}$、$N_{19,V}$ 保 $\mathcal V_i$，
且同一空间上的实际逆正是两个共轭小 norm trace。
例如对共轭 $a$ 再用 (8)，由于 $\overline\chi_i=\chi_i^{-1}$，
便得到
$N_{\bar\gamma_7,V}\Phi_i^0=\chi_i^{-1}N_{7,W}\Phi_i^0$。
因此任意 $j,k\ge0$ 都准确有
$$
\boxed{
N_{7,W}^{\,j}N_{19,W}^{\,k}\Phi_i^0
=\chi_i^j\tau_i^k
 N_{\bar\gamma_7,V}^{\,j}N_{\bar\gamma_{19},V}^{\,k}\Phi_i^0.
}
\tag{13}
$$
这是完整二变量来源身份。右边只作用于 $V$，不缩放 $W$。

若仅需有限群表达，R466 的
$N_{7,W}^{18}=N_{19,W}^{18}=I$ 在第一 principal 空间成立，
再由 (10) 得这些相应 $V$ 算子在 $\mathcal V_i$ 上也满足
十八次幂为一。这里没有断言整个 degree612 空间都具有同样的
周期；实际小 norm 共轭 trace 已足够表达 (13)，无需以巨大
逆幂代替一个尚未定标的逆算子。

### 3.1 完整第一单位测试的运输

对于
$f_u(W)=\mathbf1_{W\in\mathbf Z_p^\times}\langle W\rangle^{du}$
及任意完整 $h(V)$，(13) 可直接积分。应用一个实际第二轴
trace 时，全部分支为
$$
\nu_{N_{a,V}G}
=a^{-1}[1,a^{-1}]_*
 \sum_{t\in E[a]}\nu_{G_{a,t}},
\quad
G_{a,t}(w,v)=(T_{\bar at,V}^{(612)}G)(w,\bar av).
\tag{14}
$$
因此实际测试变为 $h(V/a)$，第一轴的 $f_u(W)$ 完全不动。
若 $h=h_u$ 自身依赖 $u$，其导数当然随同保留。

相反，若在第一轴直接展开 (7)，会出现
$\langle a\rangle^{-du}$，中央导数须包含
$-d\log\langle a\rangle$ 乘相应支的真实质量。
(13) 是全函数身份，并未把这些项单独宣称为零；它把整个
来源改写为第二轴支后，第一单位测试才保持不变。
所以 R478 中实际固定二倍产生的非齐次 $\log\langle2\rangle$
项不会因本篇而自动消失。

## 4. 新曲线投影完整移到伴随轴

保 R477 同一个原 rank-one 投影
$$
P_{\rm new}
=\frac{I-\omega N_{19,W}}2
 \left(\frac1{18}\sum_{j=0}^{17}\omega^jN_{7,W}^j\right)
 \Pi_{0,W}.
\tag{15}
$$
按两个真实输入态分别定义伴随算子
$$
\boxed{
\mathcal D_i
=\frac{I-\omega\tau_iN_{\bar\gamma_{19},V}}2
 \left(\frac1{18}\sum_{j=0}^{17}
       \omega^j\chi_i^jN_{\bar\gamma_7,V}^j\right)
 \Pi_{0,V},\qquad i=1,2.
}
\tag{16}
$$
(12)、(13) 给完整来源等式
$$
\boxed{
P_{{\rm new},W}\Phi_i
=\mathcal D_i\Phi_i
=S_{\rm new}(w)\Lambda_i(v).
}
\tag{17}
$$
因而 $\mathcal D_i$ 在实际系数空间 $\mathcal V_i$ 上为幂等
投影。这个结论只使用两条已指定的真实输入态；不能将两种
$\mathcal D_i$ 预先当成一个无标签的算子。

原完整二十三列精确计算给
$$
\boxed{\Lambda_1(0)=\frac{5824}{9},\qquad
       \Lambda_2(0)=\frac{11648}{9}.}
\tag{18}
$$
两者之和正是 R477 的 $\Lambda_{612}$，质量 $5824/3$。
它们的整个 companion CM 特征也由 (10)、(17) 确定：
$$
\begin{array}{c|cc}
&N_{7,V}&N_{19,V}\\ \hline
\Lambda_1&-\omega^2&-1\\
\Lambda_2&-\omega&-\omega
\end{array}
\tag{19}
$$
这些是实际全函数特征，不能只由 (18) 猜出。
本篇不从两个 prime 的相位给这两个高 degree 伴随另认曲线。

每个 $F_i$ 都保 R474 的 $E[2]$ trace-zero 性质：
$N_7$ 的完整交织置换规范 $E[2]$ 平移，因而与其和交换；
$F_i$ 又是 $F$ 的原 $N_7$ 多项式投影。
所以 R474 的两个真实输出核心分别对 $\Phi_i$ 成立。
在 (17) 中提取 $S_{\rm new}$ 的首单位 Amice 系数，得到
$$
\boxed{
\nu_{\Lambda_i}|_{p\mathbf Z_p}
=\lambda[\kappa]_*\nu_{\Lambda_i},\qquad i=1,2.
}
\tag{20}
$$
各质量 (18) 为单位，且 R477 已付 $1-\lambda$ 为单位；
故每个全伴随和每个单位限制均有整卷积逆。

于是对任意完整连续 $h(V)$，
$$
\boxed{
\int_{W\ {\rm unit}}\langle W\rangle^{du}h(V)\,
 d\nu_{\mathcal D_i\Phi_i}
=J_{\rm new}(u)\,\nu_{\Lambda_i}(h).
}
\tag{21}
$$
这里投影只动 $V$，所以它与任何不含 $V$ 的原测试或紧开域
限制交换。这不把一个含 $W$ 的额外区域自动归入 (21) 的
独立伴随测试。

## 5. 统一的两条算术线及不能删除的交叉参考

R466、R476 的质量一实际参考为
$$
H_{\rm ref}\quad\text{对应 }E_{668168}:y^2=x^3+668168,
$$
$$
N_7H_{\rm ref}=H_{\rm ref},\qquad
N_{19}H_{\rm ref}=-\omega H_{\rm ref},\qquad
H_{\rm ref}(0)=1.
\tag{22}
$$
这是 R466 表中的 $k=4$；不是 $k=1$ 的 $E_{-136}$。
相应完整第一轴投影是
$$
P_{\rm ref}
=\frac{I-\omega^2N_{19,W}}2
 \left(\frac1{18}\sum_{j=0}^{17}N_{7,W}^j\right)\Pi_{0,W}.
\tag{23}
$$
再取一个实际伴随算子
$$
\mathcal D_3
=\frac{I-\omega^2N_{\bar\gamma_{19},V}}2
 \left(\frac1{18}\sum_{j=0}^{17}
       (-1)^jN_{\bar\gamma_7,V}^j\right)\Pi_{0,V}.
\tag{24}
$$
把 (13) 代入，使用 R466 完整二十三维谱，而非只比较质量，
得到整个来源表：

| 仅作用于 $V$ 的算子 | 作用于 $\Phi_1$ | 作用于 $\Phi_2$ |
|---|---|---|
| $\mathcal D_1$ | $P_{{\rm new},W}\Phi_1$ | $0$ |
| $\mathcal D_2$ | $P_{{\rm ref},W}\Phi_1$ | $P_{{\rm new},W}\Phi_2$ |
| $\mathcal D_3$ | $0$ | $P_{{\rm ref},W}\Phi_2$ |

例如 $\mathcal D_1\Phi_2$ 在第一轴要求
$(N_7,N_{19})=(\omega,-1)$，而原 $N_7=\omega$ 的一维空间
实际有 $N_{19}=+1$，所以该整个来源为零。
$\mathcal D_2\Phi_1$ 却准确选出 $(1,-\omega)$ 的参考线，
不能连同前一个零一起删掉。
证书直接验证表中全部六个二十三维算子恒等式。

因此存在两个完整参考伴随 $B_1,B_2\in\mathcal S_{612}$，满足
$$
P_{{\rm ref},W}\Phi_i=H_{\rm ref}(w)B_i(v),\qquad
\boxed{B_1(0)=\frac2{27b},\quad B_2(0)=-\frac2{27b}.}
\tag{25}
$$
它们的全特征为
$$
\begin{array}{c|cc}
&N_{7,V}&N_{19,V}\\ \hline
B_1&-\omega&-\omega\\
B_2&-1&-\omega^2
\end{array}
\tag{26}
$$
两者非零且 $N_7$ 特征不同，故
$$
B:=B_1+B_2\ne0,\qquad B(0)=0.
\tag{27}
$$
质量抵消不允许把完整参考伴随删掉。
同一真实核心比较还给
$\nu_{B_i}|_p=\lambda[\kappa]_*\nu_{B_i}$。

令 $\mathcal D=\mathcal D_1+\mathcal D_2+\mathcal D_3$。
上述六个来源身份压成一个真实的 companion-only 关系：
$$
\boxed{
\mathcal D_V\widetilde\Phi
=(P_{\rm new}+P_{\rm ref})_W\widetilde\Phi
=S_{\rm new}(w)\Lambda_{612}(v)+H_{\rm ref}(w)B(v).
}
\tag{28}
$$
这是完整二输入，不是只在 $v=0$ 的边际式。

## 6. 整条中央关系与真实质量项

记 $J_{\rm ref}$ 为原共同物理周期下的
$H_{\rm ref}$ principal 单位 Mellin。
由其真实 core $\beta$ 和质量一，
$$
J_{\rm ref}(0)=1-\beta=1+\lambda.
\tag{29}
$$
对于任意完整伴随测试 $h_u(V)$，(28) 给全函数
$$
\boxed{
\int_{W\ {\rm unit}}\langle W\rangle^{du}h_u(V)\,
 d\nu_{\mathcal D\widetilde\Phi}
=J_{\rm new}(u)\,\nu_{\Lambda_{612}}(h_u)
 +J_{\rm ref}(u)\,\nu_B(h_u).
}
\tag{30}
$$
特别 $h_u=1$ 时，参考项因 (27) 的**全质量**恰为零，
剩下 $(5824/3)J_{\rm new}(u)$。对于一般伴随区域，参考项
依旧是那个真实非零 $B$，不再消失。

若实际反证条件为 $J_{\rm new}'(0)=0$，因
$J_{\rm new}(0)=0$，(30) 的中央导数准确为
$$
\boxed{
J_{\rm ref}'(0)\,\nu_B(h_0)
 +(1-\beta)\,\nu_B\!\left(\left.\partial_u h_u\right|_{u=0}\right).
}
\tag{31}
$$
这保留唯一已识别的 rank-zero 参考导数和全部测试质量导数。
它不把秩零参考导数认作零，也不把 (31) 后一项并入前一项。
其结构可与 R478 原连接的固定二倍对数质量逐项比较；
本篇没有先消掉任何尚未知的补偿。

## 7. 接 R476 七维原来源桥时的完整 lift

R476 的真实多项式为
$$
\begin{aligned}
p(t)=\frac5{1332}\bigl\{
 &-4+(3-\delta)t-4\delta t^2+(-4+2\delta)t^3\\
 &+(3+\delta)t^4+(-6-2\delta)t^5+(-7+\delta)t^6
\bigr\}.
\end{aligned}
\tag{32}
$$
保 $c_*=-111/280$。由 (13)，一个完整的原二输出 lift 是
$$
\boxed{
\mathcal B(w,v)
=c_*\sum_{i=1}^2
 p\!\left(\chi_iN_{\bar\gamma_7,V}\right)\Phi_i^0(w,v).
}
\tag{33}
$$
它在 $v=0$ 的完整边际正是
$p(N_{7,W})W_*$，也即 R476 的 $Z\Xi(2w)$。
式 (33) 的每个算子只动真实新伴随 $V$，保第一输出的单位
条件、对数和任何旧伴随坐标。原全部有限 CM 纤维和它们的
尺度在 (14) 中保留。

进一步，R476 在原五伴随 $\mathbf Z$ 上给实际整分解
$$
D_-\Pi_0\,\widehat\rho_1
=H_{\rm ref}\otimes\Lambda_{\rm ref}(\mathbf Z)
 +\sum_{j=0}^6N_7^jW_*\otimes\Lambda_j(\mathbf Z).
\tag{34}
$$
其中每个 $\Lambda_j$ 都是自己的完整五变量来源。
把第 $j$ 个 $W_*$ 因子替换为
$$
c_*\sum_{i=1}^2\chi_i^j
 N_{\bar\gamma_7,V}^{\,j}\Phi_i^0(w,v)
\tag{35}
$$
给一个保全部五伴随、额外加入 $V$ 的真实整 lift。
参考项可乘 R477 的质量一
$\overline\Lambda=\Lambda_{612}/(5824/3)$。
忘掉 $V$ 后逐项准确回到 (34)，而非只回到总质量。

若 R465 的完整 rank-one 伴随记为 $\Lambda_{\rm old}(\mathbf Z)$，
这个 lift 再作第一轴 $P_{\rm new}$ 时，恰为
$$
\boxed{
S_{\rm new}(w)\,
\overline\Lambda(v)\,
\Lambda_{\rm old}(\mathbf Z).
}
\tag{36}
$$
归一系数来自
$P_{\rm new}W_*=-3848S_{\rm new}/5$ 及
$c_*\Lambda_{612}(0)=-3848/5$，没有另设一个未知常数。
因此第三曲线的中央零合法保留全部六个伴随的联合测试。

这里 (34) 是已经过 $D_-\Pi_0$ 的来源。不能把其 lift 误作
原未投影 $\rho_1$。原 $W_t$ 深管若不含新 $V$，确能与
(35) 的 companion-only 操作逐项交换；但要把改变第一输出
的原 $\mathcal A_W$ 核搬到这个新 lift，还须支付整个新输出
极化、半特征及原条件域的对应。本篇没有预付该兼容性。

## 8. 精确证书

- [原 degree72 CM19、两个输入态和完整算子表脚本](../scripts/check-r480-actual-input-cm19.py)。
- [全矩阵、两个真实新伴随质量与参考质量的数据](../scripts/check-r480-actual-input-cm19.json)。
- [R474：原 F72 谱与二输出完整核心](R474-original-six-sigma-two-output-core-and-exact-riemann-domains.md)。
- [R477：完整 degree612 伴随与单位反卷积](R477-original-new-line-and-complete-degree612-companion.md)。
- [R476：原 Xi 的整个八维来源基与真实参考](R476-original-complete-xi-normtwo-bridge-and-integral-eight-source-basis.md)。
- [R465：原六输入两态与五伴随新曲线中央行](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。

证书另使用 R466 的全 degree136 CM7 矩阵及 R476 的全 CM19
矩阵。所有运行都是固定有理／二次域全纤维运算，不使用目标
素数扫描或未知中央值。

