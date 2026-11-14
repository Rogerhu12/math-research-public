# R514 — 原三次 forcing 的固定返回与实际镜轴尾规范形

日期：2026-11-14。**状态：已证明。** 本篇支付两份同一原格中的接口。

第一，原因子曲线 forcing 的三次导数表达可用一个固定的三 charge 乘子返回原 $\mathcal W_{D+3}$；十九个中间角、原全部次数帽与 $d$ 分母一并核清。若原来源已有三个 charge 的余量，或满足显示的真实 $r$ 缓冲条件，则返回仍在同一 $\mathcal W_D$。未把多出的三 charge 偷换成同预算，也未给返回源新的中央零。

第二，R505 的短接触满射可在原整因子格中消去 $\xi$ 的前 $\min(q,\chi-1)$ 项。对 $\chi\ge4$ 的高次数情形，R511 镜轴的剩余 forcing 因而对三条原高轴变化保持不变；矩阵本身至多改变两条末行。本文给出同一真实来源上的准确末行像判据，而非用维数假定满射。

## 1. 原三次代数 forcing

保 R495/R507/R511 的固定对象。记
$$
\mathcal E=Y\partial_Y,\qquad
\delta_t=t\partial_t\ \text{（保持 }Y\text{）},
$$
$$
A=6(1-t),\qquad B=-(1+2t),\qquad
\mathcal R=\frac{t(154+160t+1792t^2)}{3d^2},\quad d=1+8t.
$$
对同一个整因子 $\widetilde F$，为简写本节省去波浪号，置
$$
e=\mathcal EF,\qquad a_0=\delta_tF.
$$
定义原三次表达
$$
\boxed{
\begin{aligned}
K_F={}&e^3\mathcal R
+A e^2\delta_t^2F
-2A e a_0\,\mathcal E\delta_tF\\
&+A a_0^2\,\mathcal E^2F
+B e^2a_0 .
\end{aligned}
}
\tag{1}
$$
它属于 $\mathcal O[t,Y,d^{-1}]$，唯一显示角分母至多为 $d^2$，且 $\deg_YK_F\le3b$，$b=\deg_YF$。

沿同一实际正规分支 $C:F=0$，有
$$
\delta\log\psi=-a_0/e,\qquad
\delta|_C=\delta_t-(a_0/e)\mathcal E.
$$
一次准确求导给
$$
\delta(-a_0/e)
=-\frac{\delta_t^2F}{e}
+\frac{2a_0\mathcal E\delta_tF}{e^2}
-\frac{a_0^2\mathcal E^2F}{e^3}.
$$
因此 R507 的实际 forcing 满足
$$
\boxed{K_F|_C=e^3\mathcal F_F
=e^3(\mathcal R-\mathcal P\log\psi).}
\tag{2}
$$
(1) 与 R467 的隐式二阶 forcing 是同一个原方程的 Euler 写法；本篇新增的是下述真实来源返回成本，未将此表达本身重复当成新的非零定理。

## 2. 原来源的未清分母判据

R491 的双向判据可准确写成
$$
\mathcal W_D=
\{P\in\mathcal O[t,Y,d^{-1}]:\deg_YP\le D,\
v_0,v_{h_{7,1}},v_{h_{7,2}}\ge-2,\
v_1\ge-1,\ v_d\ge0,\ v_\infty\ge-8\},
\tag{3}
$$
其中
$$
\begin{array}{c|c}
\text{角}&\text{原 Gauss 赋值}\\ \hline
0,\ h_7\text{ 两根}&\min_n(4\operatorname{ord}_aP_n-n)\\
1&\min_n(3\operatorname{ord}_1P_n-n)\\
-1/8&\min_n(2\operatorname{ord}_{-1/8}P_n+n)\\
\infty&\min_n(-2\deg_tP_n+9n).
\end{array}
$$
最后一行对有理系数使用分子次数减分母次数。(3) 没有新增角极：仅允许原 $d$ 分母。

逐 $Y^n$ 而言，(3) 准确给
$$
(th_7)^{A_n}(t-1)^{B_n}\mid d^{C_n}P_n,\qquad
\operatorname{ord}_dP_n\ge-C_n,\qquad
\deg_tP_n\le f_n.
$$
除去固定角因子后，正是原 $q_n\mathcal O[t]_{\le e_{n+1}}$。所以以下用 (3) 返回原格时，已经支付每一列的准确次数帽；不是只检一个较大的矩形。

## 3. 三 charge 的统一整返回

$\mathcal E$ 不降低任何上述 Gauss 值。$\delta_t$ 在 $0$ 不降低角阶，在无穷远不增加系数次数；在其他有限角，每次至多降低该角的一个普通阶。由 (1) 的准确系数得到
$$
\boxed{
\begin{array}{c|ccccc}
v&v_0&v_{h_7}&v_1&v_d&v_\infty\\ \hline
v(K_F)-3v(F)\text{ 的下界}
&0&-8&-3&-4&-2 .
\end{array}}
\tag{4}
$$
例如，$t=1$ 处两次 $\delta_t$ 最多损六个 Gauss 单位，但 $A=6(1-t)$ 补回三个，故最坏仅损三。$d=0$ 处 $\mathcal R$ 的两重极和两次求导同样最多损四。无穷远 $A,B,\mathcal R$ 的有理次数至多一，故最多损二。$p>83$ 保全部固定分母为单位。

取固定乘子
$$
\boxed{\mathfrak m_3=Y^3t(t-1)^2h_7^3d^2.}
\tag{5}
$$
它的对应 Gauss 值准确为
$$
\begin{array}{c|ccccc}
v&v_0&v_{h_7}&v_1&v_d&v_\infty\\ \hline
v(\mathfrak m_3)&1&9&3&7&5.
\end{array}
\tag{6}
$$
因此 $\mathfrak m_3K_F$ 是真正多项式，且所有原赋值均不小于 $3v(F)$。

**定理 1。** 对任何实际原来源
$$
P^{\rm fact}=d^{-C_D}t^rQF^3\in\mathcal W_D,
\qquad D_0=3b+\deg_YQ\le D,
$$
准确有
$$
\boxed{
B_F=d^{-C_D}t^rQ\,\mathfrak m_3K_F
\in\mathcal W_{D_0+3}\subset\mathcal W_{D+3}.
}
\tag{7}
$$
若 $D_0+3\le D$，则 (7) 就在原同一 $\mathcal W_D$。

**证明。** (4)、(6) 及 Gauss 乘法给 (7) 的每个赋值至少等于原 $P^{\rm fact}$ 的对应值。$Y$ 次数至多 $D_0+3$，没有其他角分母。应用 (3) 即得全部原列条件。$\square$

(7) 是整来源恒等式，不需要新的算术零。其来源包含本身不要求 $f_{D+3}<p$；若在扩大后的格上继续调用那些以 $f_D<p$ 为假设的结果，须明确另保 $f_{D+3}<p$。在固定 $D$ 的原矩阵中，没有三个空余 charge 就不能直接使用扩大后的列。

### 十九个中间角也逐一保留

令 $u=\max_i(\deg F_i-4i)$，$\pi:X\to\mathbb F_4$ 为 R495 的固定吹起，$S_\infty=S_0+4F_0$ 为原另一截面的类。对
$$
G=\mathfrak m_3K_F
$$
可使用固定 ambient 帽
$$
\deg_YG\le3b+3,\qquad
\deg_tG_i\le3u+4i.
\tag{8}
$$
因为 (1) 的有理系数次数至多一，而 (5) 的斜次数
$\deg_t\mathfrak m_3-4\deg_Y\mathfrak m_3=11-12=-1$，两者准确相偿。

按 R495 的每个累计 $V_j$ 计算，使用 (8) 的 ambient 类而不是随取消变化的实际最高项，得到
$$
\boxed{
\begin{array}{c|c|c}
\text{链}&j\text{ 的范围}&V_j(G)-3V_j(F)\text{ 的下界}\\ \hline
0,\ h_7\text{ 两根的 }Y=\infty&1,\ldots,4&j\\
1\text{ 的 }Y=\infty&1,\ldots,3&j\\
d=0,\ Y=0&1,2&3\\
t=\infty,\ Z=0&1,2&3 .
\end{array}}
\tag{9}
$$
核法如下。在有限 $Y=\infty$ 链，ambient $Y$ 次数增加三，正好抵消乘 $Y^3$ 的负纤维权；$0$ 处剩一份 $t$，$h_7$ 处三份角零支付两次求导后剩一份，$1$ 处两份角零加 $A$ 的一份支付两次求导后也剩一份。$d$ 的中间权是 $(j,1)$，$d^2$ 支付全部 $2j$ 损失后保留 $Y^3$ 的三份。无穷远中间权是 $(-j,4j+1)$；(5) 给 $j+3$，原系数最多损 $j$，故仍剩三。

所以十九个例外条件确实给
$$
\boxed{
G\in H^0\bigl(X,\mathcal O_X(3C+3\pi^*S_\infty)\bigr).
}
\tag{10}
$$
这里是拉回类 $\pi^*S_\infty$，不是已扣除其各例外重数的严格变换；二者不能混同。(10) 没有把 $G$ 塞进未增加预算的 $\mathcal H_3$。原真正返回仍按 (7) 读取。

## 4. 由实际 r 缓冲支付的同 D 返回

另一固定清极量为
$$
\mathfrak m_0=(t-1)h_7^2d^2.
$$
其次数为七。结合 (4)，$\mathfrak m_0K_F$ 在全部有限角的值都不低于 $3v(F)$，在无穷远最多低十六。

因此若
$$
\boxed{r\ge8,\qquad v_0(P^{\rm fact})\ge30,}
\tag{11}
$$
可取
$$
\boxed{
B_F^{(0)}
=d^{-C_D}t^{r-8}Q\,\mathfrak m_0K_F
\in\mathcal W_D.
}
\tag{12}
$$
确实，除去 $t^8$ 在无穷远补回十六；在 $0$ 处损三十二，(11) 恰使其仍不低于原界 $-2$；其他原角不受影响。$r\ge8$ 同时确保没有新 $t$ 分母。$Y$ 次数没有增加，由 (3) 逐列恢复全部原帽。

一个仅用原参数的充分条件是
$$
\boxed{4r-D\ge30.}
\tag{13}
$$
因为 $t^rQF^3$ 是 $Y$ 次数不超过 $D$ 的多项式，且 $d(0)$ 为单位，
$v_0(P^{\rm fact})\ge4r-D$；(13) 也迫 $r\ge8$。不能只保 $r\ge8$ 就宣称 (12) 在同一格内。

(12) 支付的是原 $\mathcal W_D$，并不声称仍属于 R495 的
$d^{-C_D}t^rQ\mathcal H_3$。特别原 $0$ 链的中间值会改变，且前缀从 $t^r$ 变为 $t^{r-8}$；后续使用原真行时必须保它产生的真实低行输出。全角与次数的正确目的格判据是已经证明等价的 (3)。

## 5. 实际真行如何杀掉已返回的 forcing 来源

若 (7) 有三个真实 charge 余量，或取的是扩大后原矩阵的真左行，则 $B_F$ 是合法被测列。它仍有 $t^r$ 前缀，故 R498 的低行消元对它不产生低行右逆项。将同一个原高块除以 $t^rQ_{\rm phys}/d^{C_D}$ 后，得到 $G=\mathfrak m_3K_F$ 的实际正规展开。

对原真行
$$
\Phi=(A_0+B_0\zeta+C_0\zeta^2)\frac{dt\wedge d\zeta}{\zeta^3}
$$
准确有
$$
\boxed{
\operatorname{Res}_P
\left[
\frac{A_0}{2}(\mathcal E^2G)|_C
+B_0(\mathcal EG)|_C
+C_0\,(\mathfrak m_3|_C)e^3\mathcal F_F
\right]dt=0.
}
\tag{14}
$$
(2) 支付最后一项，前两项仍是同一个实际三次多项式的真实 normal 导数。它们不能为单独读取 forcing 而删除。

如果只有原 $\mathcal W_D$ 的左行、又没有 charge 余量，则它未必杀 (7)；不能在此借用扩大后的行。对于同 D 的 (12)，须先用 R498 同一个低行右逆消去其**完整实际低输出**，保留全部高尾后再应用 $\Phi$。不能将形式上的 $t^{-8}G$ 当作已经归一的高输出。

同理，若使用真正模 $p^2$ 左行 $\lambda_2$，可得整体
$\langle\lambda_2,J(B_F)\rangle=0\bmod p^2$，但这不允许单独将 (14) 的最后一项除 $p$。原 normal 两项、左行提升及低行高尾须一起进入 R507 的实际 forcing 整商。返回源没有被赋新的中央零；这里使用的只是同一个真实左行杀所有原来源的定义。

## 6. 同格消去 ξ 的最长已付初段

以下保 R511 的低 $\ell$ 范围
$$
1\le\ell\le r<h,\qquad 0\le k<\ell,\qquad
S=2h-k=s-r,\qquad q=h-k,
$$
$$
\chi=-K_XC,\qquad
\eta=\log(g/\widetilde\psi)=t^hu+p\xi\pmod{p^2}.
$$
置
$$
\boxed{q_0=\min(q,\chi-1).}
\tag{15}
$$
R505 的 $E_{q_0}:\mathcal H_1\to\mathcal O[t]/t^{q_0}$ 约化满射，因为 $q_0<\chi$。因此可选择一个真实 $H\in\mathcal H_1$ 并合法改用
$\widetilde F-pH$，使
$$
\boxed{\xi\equiv0\pmod{t^{q_0}}.}
\tag{16}
$$
证明是先消去 $E_{q_0}(\widetilde F)/p=e\xi$，再用 $e(P)$ 为单位。来源改变量为同预算的
$-3p\,d^{-C_D}t^r\widetilde Q\,\widetilde F^2H\bmod p^2$，按 R505 带回原首次修正；不是任意挑一个形式 $\xi$。

于是原两个实际代表的支撑准确缩到
$$
\mu_F=e\xi\in t^{q_0}k[t]/t^q,
\qquad
\mu_{\rm mir}=8e^2t^hu\xi\in t^{h+q_0}k[t]/t^S.
\tag{17}
$$
未吸收的可见尾长为
$$
\boxed{\max(0,q-\chi+1).}
\tag{18}
$$
原 $\beta_\xi$ 仅剩第二块的最后这多个行。若 $q<\chi$，这正恢复 R505 的完整吸收；当 $q\ge\chi$ 时，(18) 是一个真实来源正规形，而不是声称剩余尾也已消失。

## 7. 规范形对原三高轴一致，forcing 不随之变化

考虑 R468/R498 已明确的实际形式族，保持原 $t$ 和 Gaussian 常数 $a$，
$$
g_\Delta=g\exp\Delta,\qquad
\Delta\in t^{s-3}\mathcal O[[t]]\pmod{p^2}.
\tag{19}
$$
这里各参数仍须使用原完整中央给出的实际值；本节不把任意族成员认作新算术来源。

由 $k<r<h$，有 $h\le(s-1)/2<s-3$。所以 $E_{q_0}$ 的整个整矩阵及其实际除 $p$ 代表对 (19) 不变。第6节可以选择**同一个** $H$、同一个因子提升，统一实现 (16)；不为每个高轴另选来源。

在这个固定基准中，
$$
\eta_{0,\Delta}=\eta_0+\bar\Delta,\qquad
\xi_\Delta=\xi\pmod{t^h}.
$$
故
$$
\mu_{{\rm mir},\Delta}-\mu_{\rm mir}
=8e^2\bar\Delta\,\xi\pmod{t^S}.
\tag{20}
$$

**定理 2。** 若 $\chi\ge4$，特别当 $b=\deg_YF\ge2$ 时，规范形 (16) 下的整个镜轴 forcing 代表 $\mu_{\rm mir}$ 对 (19) 不变。

**证明。** 若 $q_0=q$，(17) 已给 $\mu_{\rm mir}=0$，且高轴改变的阶高于 $h$，仍为零。否则 $q_0=\chi-1\ge3$，所以 (20) 的阶至少 $s-3+3=s>S$。$\square$

这个结论只固定了镜轴的特定实际 forcing；它没有使镜轴矩阵或原全部真左行空间同时固定。

## 8. 同一镜轴矩阵准确只改末两行

对每个真实 $H_2\in\overline{\mathcal H}_2$，R511 的镜轴评价在 (19) 下变化为
$$
\boxed{
\bar E^{\rm mir}_{S,\Delta}(H_2)
-\bar E^{\rm mir}_{S,0}(H_2)
=2\bar\Delta\,(\mathcal EH_2)|_C\pmod{t^S}.
}
\tag{21}
$$
原因是 $\Delta^2=0\bmod t^S$，且将
$(\mathcal EH_2)(g_{\rm mir})$ 换成沿 $C$ 的值只产生
$t^h\Delta$，其阶至少 $s-3+h\ge S$。两个来源及其全部角条件相同。

因此变动只落在
$$
\boxed{\max(0,3-r)}
\tag{22}
$$
条末行，至多两条。定义原来源上的固定观察
$$
L_0(H_2)=[t^0](\mathcal EH_2)|_C,\qquad
L_1(H_2)=[t^1](\mathcal EH_2)|_C.
$$
写 $\bar\Delta=d_0t^{s-3}+d_1t^{s-2}+\cdots$。则：

- $r=1$、$S=s-1$ 时，末两行的改变为
  $2d_0L_0$ 与 $2d_1L_0+2d_0L_1$；
- $r=2$、$S=s-2$ 时，唯一末行的改变为 $2d_0L_0$；
- $r\ge3$ 时，整个约化镜轴矩阵不变。

这些是同一实际来源的线性观察，不是新增中央条件。

若使用原 $w$ 高轴
$\Delta=u_*w^{s-3}+v_*w^{s-2}+x_*w^{s-1}+\cdots$，则保原
$c_0=(w/t)(0)$ 和 R305 的 $w=c_0t(1+\frac37t+\cdots)$ 后，准确有
$$
\boxed{
d_0=c_0^{s-3}u_*,
\qquad
d_1=c_0^{s-3}(s-3)\frac37u_*+c_0^{s-2}v_*.
}
\tag{23}
$$
这是单位三角换参。第三参数 $x_*$ 没有进入本长度；它在原下一精度的作用并未因此删除。

## 9. 真来源上的末行像判据

设 $\chi\ge4$，采用第6节的统一规范形，因此 $\mu=\mu_{\rm mir}$ 固定。
令
$$
S_-=\min(S,s-3),\qquad
A_-:\overline{\mathcal H}_2\to k[t]/t^{S_-}
$$
为所有高轴共同的低行矩阵。所有下述核、像均来自 $\overline{\mathcal H}_2$ 的真正有限来源，不补自由列。

若 $\mu_{<S_-}\notin\operatorname{im}A_-$，则任何 (19) 的参数都不能通过 $FH_2$ 路线吸收这个镜轴类。若它在像内，取一个实际 $H_*$ 满足
$A_-H_*=\mu_{<S_-}$，并令 $\mathcal K_-=\ker A_-$。记末行投影为
$\pi_{\rm top}$，由 (21) 给出实际变动算子 $\Delta_{\rm top}$。则完整可解性准确等价于
$$
\boxed{
\pi_{\rm top}\mu-
\pi_{\rm top}E^{\rm mir}_{S,0}(H_*)-\Delta_{\rm top}(H_*)
\in
\operatorname{im}\bigl(
\pi_{\rm top}E^{\rm mir}_{S,0}+\Delta_{\rm top}
\bigr)|_{\mathcal K_-}.
}
\tag{24}
$$
这只是先解真实低行再解其同一个来源核的末行；它完整保留低行解的所有高尾，不是将末行设为可任取。

一个有用的准确特例是已经证明或实际核到
$$
\mathcal K_-=kF^2.
\tag{25}
$$
因为 $E^{\rm mir}_{S,0}(F^2)=0$ 且
$(\mathcal EF^2)|_C=0$，$H_*$ 模这个核的全部末行及 $L_0,L_1$ 均唯一。置
$$
\ell_0=L_0(H_*),\qquad \ell_1=L_1(H_*),
\qquad
(b_0,b_1)=
\pi_{\rm top}\bigl(\mu-E^{\rm mir}_{S,0}(H_*)\bigr).
$$
在 $r=1$ 时，(24) 准确化为
$$
\boxed{b_0=2d_0\ell_0,\qquad
b_1=2d_1\ell_0+2d_0\ell_1.}
\tag{26}
$$
若 $\ell_0\ne0$，可读出唯一候选
$$
d_0=\frac{b_0}{2\ell_0},\qquad
d_1=\frac{b_1-2d_0\ell_1}{2\ell_0}.
$$
若 $\ell_0=0,\ell_1\ne0$，必须先有 $b_0=0$，随后只确定 $d_0$；
若两观察都零，则要求两个 $b_i$ 都零。在 $r=2$ 时同理仅有
$b_0=2d_0\ell_0$。

(25) 是一个真实核条件，未从维数或“通常情形”假定成立。(26) 也只判定已付的 $FH_2$ 吸收路线；即使失败，其他原 $J$ 列仍可能吸收 (12) 的余核像。因此不能把它直接称为全 $M$ 提升的必要条件或完整中央的矛盾。真正中央参数必须通过 (23) 代入，同一个原 $P_{134}/U_0$、两条十三行 carry 及第三精度继续保留。

## 10. 已付输入与未付连接

第3、4节把 (1) 的原三次 forcing 付成了有准确成本的原来源，第5节给其与真实行相接的完整等式。第6–9节则将镜轴剩余类固定，并把高轴影响集中到最多两条真实末行。这些结论可在同一个原有限矩阵上使用；没有扩大来源后沿用旧左核，也没有删去低行高尾。

R507 的唯一目标 Euler 共振仍不能代替 (14) 的原 normal 导数项或 (24) 的真正末行像。R511 的完整公式仍含第一 carry、活 $V_1$ 与实际低行右逆的高尾。若要从已返回的 forcing 提取其除 $p$ 项，必须与这些项以及真正左行提升联立。三条原完整中央没有传播到 (7)、(12) 或任意因子截面；跨 $p$ 非零仍待证明。

本篇为全参数来源、赋值与有限像证明，没有新增素数扫描。
