# R783 — 原帽的完整 P 像、CD 失败支与同一中央的非零解析余行

日期：2026-11-15。**状态：已证明。**

本文保持 R734 的最终测试 $q_N^*$，不重新适配。R777 的 P 收缩不把原帽送回原帽；本文把其像准确写成一个固定伙伴上的斜管，保原 U 失败、全部 CD/E 门和同一个 Mellin 观察。更实质地，这个像中的原 T 中央行确实是一个非零解析函数在 $\kappa^\ell$ 的取值。证明使用原条件负一矩与原 $f_1$ 的正一单位矩，不假设尚未证明的固定负五矩非零。

所有真实像与原共同深块最终放回同一个完整 T 中央等式；其余域原样保留。另给一个有限 point-factor 左行，准确读取两分母之差，说明单用 P 的有限点来源尚不能消去这个余项。此处不对无限 log 或随 N 改变的点池施惯性投影。

## 1. 同一原来源与两个正交伙伴

沿 R773/R777，置
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad
a=1+3\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad\kappa=p\lambda^2 .
\tag{1}
$$
全部旧射线、固定坏集、$p>163$ 和 R773 增补的相对密度一子族保持。
$N\in4\mathbf Z_{>0}$，本篇取真实 $n=N+300$。
记 R777 的原平均 B 来源及最终权为
$$
B_0=\mathscr P_C\frac{e_0-\omega h_W}{1-\omega^2},
\qquad \rho=q_N^*B_0,\qquad q=q_N^* .
$$
纯 C 平均、全部六支以及原混次周期归一均不改变。

原行满足
$$
Y=A_0+s+2d,\quad t=r-c,\quad
P=Y+as+2d,\quad W_j=P-a\omega^{2j}t,\quad j=0,1,2.
$$
写
$$
\hat s=s-Y/17,\quad \hat d=d-Y/17,\quad
Z_0=a\hat s+2\hat d,\quad
b_Y=(20+3\omega)/17,\quad P=b_YY+Z_0.
\tag{2}
$$
真实帽与失败条件为
$$
\mathcal H_N=\{Y\ {\rm unit},\ \hat s,\hat d\in p^N,\
                         U\notin p^n\},\qquad
U=\hat s/2-3\hat d .
\tag{3}
$$
它不含 t。只有再附原 $t$ 深域时，才是 R764 三个 O 域的共同返回；本文不把这一附加条件藏在记号中。

R773 的原隐藏行
$$
J=F+\frac{5+2\omega}{7}H_1
 =\frac{17+3\omega}{14}\hat s+
                  \frac{17+24\omega}{7}\hat d
\tag{4}
$$
同时垂直于 Y、P、t。q 只依 C、$H_1$、J。
$(\hat s,\hat d)\mapsto(J,Z_0)$ 的行列式是 $72/7$，为原 p-unit。
其完整反变换为
$$
\boxed{
\begin{aligned}
\hat s&=\frac7{36}J-\frac{17+24\omega}{72}Z_0,\\
\hat d&=-\frac{7a}{72}J+\frac{17+3\omega}{144}Z_0,\\
U&=u_JJ+u_ZZ_0,\qquad
u_J=\frac{7(4+9\omega)}{72},\quad
u_Z=-\frac{68+33\omega}{144},\\
E_\perp&=-\frac{7\cdot263}{72}J
              -\frac{17(25+48\omega)}{144}Z_0 .
\end{aligned}}
\tag{5}
$$
最后一式由原
$E_\perp=-(17+3\omega)\hat s-(68+99\omega)\hat d$
直接代入；不是另选 E 来源。

再令
$$
c_P=\frac{17-3\omega}{29},\qquad
\vartheta=1-b_Yc_P=\frac{144}{493},\qquad
R=Y-c_PP .
\tag{6}
$$
则 $R\perp P,t$，$N(R)=288/29$，而
$$
Y=R+c_PP,\qquad Z_0=\vartheta P-b_YR.
\tag{7}
$$
本篇只使用这些真实线性关系及已付 P 核，不在此给 R 或 $Z_0$ 添加单轴核心。

## 2. P 收缩后的完整帽像与 U 失败门

R778 已将 R777 的绝对符号定为 $-1$，故原完整 P 核是
$$
\rho|_{P\in p^\ell}
 =\beta^\ell(P_{P,\kappa^\ell})_*\rho,\qquad \ell\ge0.
\tag{8}
$$
q 与 P 逐点正交；(8) 保全部伙伴。
对 $\ell\ge1$，定义
$$
P_\ell=P/\kappa^\ell,\qquad
Z_\ell=\vartheta P_\ell-b_YR,\qquad
Y_\ell^-=R+c_PP_\ell .
$$
这里 $Y_\ell^-=Y\circ P_{P,\kappa^{-\ell}}$ 只在 P 深 $\ell$ 的整像中使用。

原帽的实际像恰为
$$
\boxed{
\mathcal H_{\ell,N}
=P_{P,\kappa^\ell}(\mathcal H_N)
=\{R\ {\rm unit},\ J,Z_\ell\in p^N,\
                         u_JJ+u_ZZ_\ell\notin p^n\}.
}
\tag{9}
$$
右侧自动给 $P_\ell$-unit、$Y_\ell^-$-unit，故 $v_p(P)=\ell$。
确实 $P_\ell=(Z_\ell+b_YR)/\vartheta$，
$Y_\ell^-=(R+c_PZ_\ell)/\vartheta$；
所有显示常数都是已付 p-unit。反方向也由这两式恢复原帽。
因此 (9) 既没有漏掉原 Y-unit，也没有额外扩大 P 的像。

尤其失败条件是
$$
u_JJ+u_Z(\vartheta\kappa^{-\ell}P-b_YR)\notin p^n,
\tag{10}
$$
**不是**新坐标中的 $U\notin p^n$。
原物理 $U=u_JJ+u_Z(\vartheta P-b_YR)$ 仍是另一个行。

对任意完整有界测试 f 和原附加 t 事件 D，
$$
\boxed{
\int_{\mathcal H_{\ell,N},D} f\,d\rho
=\beta^\ell\int_{\mathcal H_N,D}
                       f\circ P_{P,\kappa^\ell}\,d\rho .
}
\tag{11}
$$
t 被 P 映射固定。任何其它门均须同样转置；(11) 没有把门替换成其质量。

## 3. CD 全失败、E 的准确分割与第三中央的范围

在 (9) 上，模 p 有 $J=P=0$、R 为单位，故由 (5)—(7)
$$
\boxed{
Y\equiv R,\qquad
d\equiv-\frac{11+6\omega}{144}R,\qquad
s\equiv\frac{20+27\omega}{72}R,\qquad
\hat d\equiv-\frac{(17+3\omega)b_Y}{144}R\pmod p .
}
\tag{12}
$$
$N(11+6\omega)=91$，$N(20+27\omega)=589=19\cdot31$；
因此 Y、d、s、$\hat d$ 均为单位；最后一项还使用原已付 $b_Y$-unit 和 $N(17+3\omega)=13\cdot19$。
原三个 CD 门
$$
\mathsf{CD}_{j,N}=\{d\in p^N,\ s-\omega^{2j}t\in p^N\}
$$
在整个 $\mathcal H_{\ell,N}$ 上都失败，不依 t 的深度。
这比仅说 $\hat d$ 成为单位更强；它直接定位到原 CD 外部。

原物理 E 行是
$$
E_j=E_\perp+h_0\omega^{2j}t,\qquad h_0=17+3\omega .
\tag{13}
$$
(5) 在 (9) 上给
$$
E_\perp\equiv
       \frac{17(25+48\omega)b_Y}{144}R\pmod p .
\tag{14}
$$
$N(25+48\omega)=1729=7\cdot13\cdot19$，故 $E_\perp$ 是单位。
于是：

1. 附 $t\in p$ 时，全部 $E_j$ 均为单位。
2. 附 t-unit 时，三个 $E_j\in p^N$ 门两两不交，且准确为
   $$
   t\equiv-\omega^{-2j}E_\perp/h_0\pmod{p^N}.
   \tag{15}
   $$
   三个中心都是不同的非零余数。
3. t-unit 上还须保三个 E 门都失败的完整补集。不能将这三个小盘当作整个单位域。

这也澄清原未收缩帽与第三中央的交域。在 $\mathcal H_N$ 上只有
$E_\perp\in p^N$，因此
$$
\boxed{
\mathcal H_N\cap\{E_j\in p^N\}
 =\mathcal H_N\cap\{t\in p^N\}.
}
\tag{16}
$$
而 $P$ 在 $\mathcal H_N$ 上为单位。
若再要求 $W_j\in p^m$、$m\ge1$，就迫 t 为单位，故 $E_j$ 为单位：
$$
\mathcal H_N\cap\{W_j\in p^m\}\subset\{E_j\ {\rm unit}\}.
\tag{17}
$$
所以它与 R780 的 E 深第三中央行不交。
R780 更正后的裸 W 返回仍可用，但其补项属于 E 浅完整来源，含原 $\Xi$。
本文不从 E 深第三行减掉 (17)。

令 $\mathcal X_{\ell,N}=\mathcal H_{\ell,N}\cap\{t\ {\rm unit}\}$。
在此域，P 深、t 为单位，故全部 $W_j,V_t$ 都为单位。
按 (15) 将它精确分成三个 $\mathcal X_{\ell,N,j}$ 与
$\mathcal X_{\ell,N,*}$，后者表示全部 E 门失败。
任意 Mellin 或有理观察都须对这四块求和。
$\mathcal T$ 固定 R、J、P 并将 t 乘 $\omega^2$；
同时 $\mathcal T_*\rho=\omega^2\rho$。因此其完整有限关系为
$$
\boxed{
\int_{\mathcal X_{\ell,N,j+1}}f_w(W_{k+1})\,d\rho
=\omega^2\int_{\mathcal X_{\ell,N,j}}f_w(W_k)\,d\rho ,
}
\tag{18}
$$
下标按3取模。全失败块满足同样的观察协变。
(18) 将九条 E 深观察压成三个相对下标的行，另有一条全失败行；
它不将任何一条行或局部质量赋零。

## 4. 同一个真实帽像的完整 Mellin 行

固定 N。定义同一个未收缩原帽上的有界解析函数
$$
\boxed{
\mathcal C_N(z)
=\int_{\mathcal H_N,\ t\ {\rm unit}}
       \log\left(1-\frac{zP}{at}\right)d\rho,
\qquad z\in p\mathcal O .
}
\tag{19}
$$
P、t 在该积分域都为单位。q、帽和 t-unit 全被 $\mathcal T$ 固定；
$\langle t\rangle$ 也被固定。
由于来源的特征为 $\omega^2\ne1$，
$$
\int_{\mathcal H_N,t\ {\rm unit}}
       \langle t\rangle^{d_pw}d\rho=0
\tag{20}
$$
作为整个 w 函数成立。这同时支付质量和 t-log 常数项的消去。

由 (11)，原帽像的完整中央行准确是
$$
\boxed{
\left.\frac d{dw}\right|_{w=0}
 \int_{\mathcal X_{\ell,N}}f_w(W_j)\,d\rho
=\beta^\ell d_p\,\omega^{2j}\mathcal C_N(\kappa^\ell).
}
\tag{21}
$$
其中 $f_w(x)=1_{x\ {\rm unit}}\langle x\rangle^{d_pw}$。
没有把 $P/\kappa^\ell$ 当作原 W 观察；
真正观察始终是 $W_j=\kappa^\ell P_{\rm pre}-a\omega^{2j}t$。
若再分成 (15) 的四块，(20) 不自动逐块成立，所有局部 log 质量仍须保留。

为证明 (19) 非零，使用 R777 已付、保全五伙伴的两核
$$
B_0=\frac{\delta}{84}
 \left(\mathcal V_1\boxtimes\nu_{f_1}(T_0)
       +\mathcal V_4\boxtimes\nu_{f_4}(T_0)\right),
\quad T_0=\delta t,\quad P_0=\delta P,
\tag{22}
$$
$$
f_1=-xy\sigma^6,\qquad f_4=x\sigma^6,
$$
$$
\mathcal V_i
=\nu_{B_3}(C_0)\boxtimes\nu_\sigma(\xi_2)
       \boxtimes\nu_\sigma(d)\boxtimes\nu_{U_i}(S,B),
$$
其中 $U_1=2f_3(S)B_3(B)+H(S)P_3(B)$，
$U_4=6bf_3(S)P_3(B)-H(S)B_3(B)$。
q 和 $\mathcal H_N$ 全留在这五个伙伴上。

定义真正条件矩
$$
M_{i,N}(r)=\int_{\mathcal H_N}P_0^r q\,d\mathcal V_i,
\qquad
I_{i,-r}=\int_{T_0\ {\rm unit}}T_0^{-r}\,d\nu_{f_i}.
\tag{23}
$$
P-unit 使负 r 也合法。它们不是 R777 的未切边际矩。
完整级数为
$$
\boxed{
\mathcal C_N(z)
=-\frac{\delta}{84}
 \sum_{r\ge1}\frac{z^r}{r a^r}
          \{M_{1,N}(r)I_{1,-r}+M_{4,N}(r)I_{4,-r}\}.
}
\tag{24}
$$
原 f1 只保 $r\equiv5\bmod6$，f4 只保 $r\equiv2\bmod6$。
所以只出现 $r\equiv2\bmod3$，其余系数整条为零。
每个系数赋值至少 $-v_p(r)$；(24) 在 $p\mathcal O$ 上一致收敛。
固定负五 $I_{1,-5}$ 与负二 $I_{4,-2}$ 均未被赋非零。

## 5. 原正一单位矩使实际中央余行严格非零

R773 增补给：对每个合格 p，所有充分大的原 $N\in4\mathbf Z$，
$$
L_{P,N}:=\int_{\mathcal H_N}\frac tP\,d\rho\ne0,
\qquad v_p(L_{P,N})=v_p^*<\infty.
\tag{25}
$$
这里 eB 与 e0 的 t 首行相同，已经由 R767/R773 支付；
$\lambda^{2N}\beta^N$ 是单位，不能在取极限时误当收缩因子。
本节仅使用每个固定 N 的确切 (25)，不作点投影的极限交换。

从 (22) 读取原 t 正一矩，$f_1'(0)=1$、
$f_4'(0)=0$，所以
$$
\boxed{M_{1,N}(-1)=\frac{84}{\delta\Omega}L_{P,N}\ne0.}
\tag{26}
$$
又由原 whole S6 的绝对核心 $\beta$，
$$
\boxed{
\int_{T_0\ {\rm unit}}T_0\,d\nu_{f_1}
=\Omega(1-\beta\kappa)\in\mathcal O^\times.
}
\tag{27}
$$
这是原正一单位矩，不是固定负五值。

取真实正整数
$$
r_j=-1+6(p-1)p^j,\qquad j\ge0.
\tag{28}
$$
它们满足 $r_j\equiv5\bmod6$、$r_j\equiv-1\bmod(p-1)$，
且在 $\mathbf Z_p$ 中趋于 $-1$。
原各观察均取 $\mathbf Z_p^\times$ 值，因此幂函数在单位域上一致收敛，准确给
$$
\begin{aligned}
M_{1,N}(r_j)&=M_{1,N}(-1)+p^{j+1}\mathcal O,\\
I_{1,-r_j}&=\Omega(1-\beta\kappa)+p^{j+1}\mathcal O .
\end{aligned}
\tag{29}
$$
所有原权整有界，故显示误差保留原帽与 q；没有改成无条件矩。
当 $j+1>v_p^*$ 时，第一项非零且赋值 $v_p^*$，
第二项是单位。
此角型的 f4 项严格为零，$r_j$ 自身也是 p-unit。
故 (24) 的 $z^{r_j}$ 系数非零。

由此得到原同一门、同一测试的结论
$$
\boxed{\mathcal C_N(z)\not\equiv0.}
\tag{30}
$$
令 $s_N$ 为其第一个非零幂，则
$$
s_N\ge2,\qquad s_N\equiv2\pmod3.
$$
固定一个 $j_0\ge0$ 满足 $j_0+1>v_p^*$，
对该固定 p 的全部充分大 N，另有统一有限上界
$$
\boxed{s_N\le -1+6(p-1)p^{j_0}.}
\tag{31}
$$
这没有声称 $s_N=2$ 或5，也没有对 p 给一个未证明的统一小界。

写 $\mathcal C_N(z)=c_{s_N,N}z^{s_N}+\cdots$。
非零收敛幂级数在零点附近有明确首项，故对每个固定 p、N，
所有充分大的 $\ell$ 都满足
$$
\boxed{
v_p\!\left[
 \left.\frac d{dw}\right|_0
 \int_{\mathcal X_{\ell,N}}f_w(W_j)d\rho
 \right]
=s_N\ell+v_p(c_{s_N,N})<\infty .
}
\tag{32}
$$
(21) 中的 $\beta^\ell,d_p,\omega^{2j}$ 均为单位。
所以这里证明的是原 CD 全失败支内的一条真正 T 中央非零，
不是另外构造的无权单位见证。

## 6. 与原共同深块放在同一个完整中央等式中

为保旧 Y 归一，置 $r_n=(-\kappa)^n$、
$A_n=P_{Y,r_n}$、$T_m=P_{t,\kappa^m}$。
整个联合 Y 核给
$$
\boxed{
\int_{\{Y\in p^n\}}f_w(W_j\circ A_n^{-1})d\rho
=\lambda^n\omega^{2j} Z_B(w),\qquad
Z_B(w)=\frac{6\delta\beta^N}{1-\omega^2}J_T(w).
}
\tag{33}
$$
这是原 q 的整行，所有归一都写在观察中。

固定 $m\ge n$，并令
$$
\mathcal D_N^\times=\mathcal H_N\cap\{t\ {\rm unit}\},\qquad
\mathcal A_{n,m,N}=A_nT_m(\mathcal D_N^\times),\qquad
\mathcal X_{\ell,n,N}=A_nP_{P,\kappa^\ell}(\mathcal D_N^\times).
\tag{34}
$$
这些是同一个原六变量空间中的实际域。

第一域有精确 t 环带 m，属于原三个 O 域的共同 CD 深块，
包括原 U 失败。第二域有 t-unit；
由 (12) 和 $A_n$ 的真实行
$d=\hat d+r_nY/17$ 可知，它的三个原 CD 门均失败。
因此第一域与全部第二域不交；不同 $\ell$ 的第二域也不交，
因为 $P\circ A_n^{-1}$ 的深度分别等于 $\ell$。
没有以两个不同坐标中的“CD”同名来证明不交。

定义
$$
\begin{aligned}
a_{m,N,j}(w)&=\int_{\mathcal D_N^\times}
                    f_w(P-a\omega^{2j}\kappa^m t)d\rho,\\
b_{\ell,N,j}(w)&=\int_{\mathcal D_N^\times}
                    f_w(\kappa^\ell P-a\omega^{2j}t)d\rho.
\end{aligned}
$$
对每个有限 L，将 (33) 的域减去 (34) 中的有限并，
剩下的**整个**域记为 $\mathcal R_{n,m,N,L}$，观察仍为
$W_j\circ A_n^{-1}$。其完整 Mellin 值记为 $R_j(w)$。
逐个使用真实 Y、t、P 核，得到
$$
\boxed{
\lambda^n\omega^{2j} Z_B(w)
=\lambda^n\beta^m a_{m,N,j}(w)
 +\lambda^n\sum_{\ell=1}^{L}\beta^\ell b_{\ell,N,j}(w)
 +R_j(w).
}
\tag{35}
$$
原质量、Mellin 常数和全部 unit 进入/失败支均包含在此式。
若另改为 p 的幂归一，须乘相应
$\langle\kappa/p\rangle^{nd_pw}$ 并保局部质量。

(32) 给 (35) 中实际第二类项的非零；R773 给第一类项的真实首阶。
在 $J_T'(0)=0$ 下，准确结论是
$$
\boxed{
R_j'(0)=-\lambda^n\left(
 \beta^m a_{m,N,j}'(0)+
          \sum_{\ell=1}^{L}\beta^\ell b_{\ell,N,j}'(0)\right).
}
\tag{36}
$$
这里没有删除 $\mathcal R$。
其内容包括未选 P 环带、同环带内未命中 (9) 的部分、
所有另外的 t/CD/帽/U 门和实际 unit 进入/失败。
若附 R780 的第三行，还须按 (15)—(18) 保 E 深三支与全 E 失败支，
并按其真实来源状态与观察返回；(36) 不把它们换成 T 行。

由于所有 (34) 域被 $\mathcal T$ 固定，
(35) 的三条观察行本身都按 $\omega^{2j}$ 协变。
它们在本 B 分量上只是一条完整中央行的三个倍数，
不能将三个相同来源关系误当三条独立零。
这明确了这个有限分区尚余的带门线性算子：同一 $\mathcal R$ 上、
同一 $W_j\circ A_n^{-1}$ 观察的 $R_j$，及第三来源要求的
(18) 三个相对 E 下标行。它们的门和权均已显示，不能只用来源矩阵替换。

## 7. 有限两分母余行的实际非零 point 左投影

还有一个与 (9) 完全同域的有限算子，可定位 P 点来源尚未消去的部分。
在 $\mathcal X_{\ell,N}$ 上定义
$$
\boxed{
D_{\ell,N}
=\int_{\mathcal X_{\ell,N}}
 t\left(\frac1{b_YY_\ell^-}-\frac1{P_\ell}\right)d\rho
=\int_{\mathcal X_{\ell,N}}
       \frac{tZ_\ell}{b_YY_\ell^-P_\ell}\,d\rho .
}
\tag{37}
$$
两个分母都是原像上的单位，$Z_\ell\in p^N$，故
$D_{\ell,N}\in p^N\mathcal O$。
这是完整 U 失败门内的真有理行，不是把帽只取总质量。

(11) 与原 t 正一环带返回给准确有限等式
$$
\boxed{
D_{\ell,N}
=\beta^\ell(1-\beta\kappa)
 \left\{\frac1{b_Y}
     \int_{\mathcal H_N}\frac tY\,d\rho
       -\int_{\mathcal H_N}\frac tP\,d\rho\right\}.
}
\tag{38}
$$
帽、P 以及 q 都被 $\mathcal T$ 固定，所以两个 t 首行中的 $B_0$ 可准确换回原 $\mathscr P_Ce_0$，如 R773(A15)；不需扩大 R778 的来源范围。
R778 覆盖第二个 P 负一行的全部原有限门；
它属于一个有限、在17处不分歧的 E1 点因子空间。
第一项则由 R773(31)、(A3)—(A6) 写成
$$
\int_{\mathcal H_N}\frac tY\,d\rho
=\lambda^{2N}\beta^N
 \{A_{\omega,N}\Omega I_{\omega,p}
      +A_{-,N}\Omega I_{-,p}+\text{完整 primitive 项}\},
\tag{39}
$$
两个 $A_{\omega,N},A_{-,N}$ 都是实际代数单位。
primitive 的 exact-order9 点角色仍保。

固定 p、N、$\ell$，仅在 (38)—(39) 所涉及的有限 point-log 空间内，
使用 R739/R749/R761 的固定系数 point-only 投影
$\mathsf e_\omega,\mathsf e_-$。
它们杀17不分歧 P 点和另外的 primitive 角色，准确得到
$$
\boxed{
\mathsf e_k(D_{\ell,N})
=\frac{\beta^\ell(1-\beta\kappa)}{b_Y}
       \lambda^{2N}\beta^N
                 A_{k,N}\Omega I_{k,p}\ne0,
\qquad k\in\{\omega,-\}.
}
\tag{40}
$$
因此每个这样的固定有限门都有
$$
\boxed{D_{\ell,N}\ne0,\qquad D_{\ell,N}\in p^N\mathcal O.}
\tag{41}
$$
这给出了一个实际左行：它消去此处全部有限 P 点来源，却不消去
原帽的两条 cubic Y 分量。
所以若只把 P 负一块当作已知有限来源来消元，(37) 这条带门余行必须保留；
不能把“P 块已识别”当作两分母可互换。

(40) 不施于 (24)、(35) 的无限 log，也不与 N 极限交换。
(41) 的小赋值范围和非零并不矛盾。
本节没有把 $D_{\ell,N}$ 认成 $R_j'$，亦未从 (40) 宣布原中央非零。
真正中央的新非零信息是第5节在同一实际帽像上证明的 (32)，
其完整原算术补偿始终是 (35)—(36)。

## 8. 结论的准确用途

本篇支付三项新的完整接口：

- 原帽在 P 收缩下是 (9) 的精确斜管，原 U 失败条件为 (10)；
  它落全部 CD 失败支，E 的三个深盘及全浅补集为 (15)—(18)。
- 同一帽像的原 T 中央是 (21) 的真实解析函数；
  原正一单位矩和条件负一矩通过 (28)—(29) 证明它非零，
  不依赖未付的固定负五矩。
- 两分母的有限余行有 (40) 的实际非零左投影，
  不能用 P 的有限点公式删除；完整中央仍按 (35) 保所有外部。

原三中央同时零尚未使 (36) 的完整余项为零。
后续消元须用这些同一域、同一权的行，与 R780 第三来源的真实 E 门联立，
或进一步支付这个明确余项的独立返回。主问题的完成标准没有改变。

## 依赖与执行范围

- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：原最终测试、全部整逆和同一权。
- [R764](R764-y-preserving-six-axis-and-three-cd-exterior-domains.md)：完整 Y/t 核、CD/O 域及归一观察。
- [R767](R767-native-t-moment-and-complete-five-partner-boundary.md)：原全五伙伴 t 首行及两核规范。
- [R773](R773-native-common-hat-domain-and-five-conditional-moment-return.md)：同一帽/U 失败条件、两实际算术幅度和真正条件负一非零。
- [R777](R777-original-b-sector-p-t-core-and-complete-central-renewal.md)：B 来源、完整 P/t 与 W/Vt 核、四单位剩余式。
- [R778](R778-original-degree174-full-characters-and-unramified-seventeen-point-fields.md)：P 核定号及所有原有限门 P 负一的17不分歧点域。
- [R780](R780-original-third-central-b-state-and-true-w-deep-return.md)：更正后的第三中央、E 浅完整来源及真实 W 逆观察。
- R735、R739、R749、R761：两原点对数、有限 point-only 投影及 primitive 完整角色。

本篇只有显示行的代数恒等式、已付整核的真实域转置和单位域上幂函数的一致收敛证明；
没有新的数值执行、扫描或需保存的可重算输出。
