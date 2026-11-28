# R150：整个 W / $\gamma\ne0$ 的原齐次三次迹、显式头 Bézout 与首一 $f^2$

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。AI-assisted，GPT-6 Astra Pro。

## 1. 结论与实际范围

在当前 W 的已付原权图上，整个 $t=0$ 和整个 $f=u$ 已经排除。令
$$
\eta=f-u,\qquad s=t/\eta,\qquad
\delta=1-Q,\quad m=u-\ell,\quad
\widehat U=u-\ell Q,\qquad
\gamma=4\delta-\widehat U s.
$$
在整个 $s\gamma\ne0$ 图上，下述完整同点原组合成立：
$$
q_f=c_0 EW+c_1 E_B^{\rm odd}+c_2N_1
=f^2+q_1f+q_0.
\tag{1}
$$
$c_i,q_i$ 的分母只有已付原权单位与 $\gamma$。三个原 $f^2$ 首项的显式 Bézout 返回为 $1$；没有增加未知权曲线或新的首项非零假设。

实际 run46112930960/job140880267654 在 8.998024917 秒前已完整返回该首一组合和其全部三个 $f$ 系数。后继十行二列及其五原式展开在 180 秒处触界，没有完成输出，故本篇只登记已成 (1)、由它直接推出的二生成环境，以及准确失败边界。没有新的原标量、权覆盖或排空结论。

## 2. 同原点可逆斜率坐标

沿既有 W 记号，
$$
u=e+1,\quad Q=ek,\quad V_b=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV_b},
$$
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
M=\ell V_2-u^2.
$$
正确原均值差消去 $\eta$ 后，给出
$$
V=\frac{\beta f+c_*}{\gamma},\quad
\beta=4\delta-2um\,s-\frac{M}{4}s^2,\quad
c_*=-s\left(Mu+\frac m2T_0\right)+\frac{Mu}{4}s^2,
$$
$$
W_1=(T_0+4uf)/2,\qquad
x=\frac{\widehat U V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},\qquad
t=(f-u)s.
\tag{2}
$$
物理原图仍要求 $\eta\ne0$，该条件没有从多项式环境中删除。原 $\alpha=\eta\gamma$；整个 $\alpha=0$ 支的处理独立登记，本篇不处理它。

式 (2) 中 $x,y,t,\lambda,T$ 都对 $f$ 至多一次。源使用真实 dual 乘法
$$
(vw)_1=v_0w_1+v_1w_0
$$
重建同点原 Gram，实际返回 $E_0,N_0,P_0,P_1$，以及
$$
E_1=EW=bE_B+cE_C.
$$
留下五条完整原式
$$
Q_0=EW,\quad Q_1=E_B^{\rm odd},\quad Q_2=N_1,\quad
Q_3=NS,\quad Q_4=PS,
\tag{3}
$$
对应 $f$ 次数恰为 $2,2,2,3,3$。这项原构造实际在 1.369655032 秒完成；没有把不同 $f$ 根的均值、N、P 结果拼合。

## 3. 原六规则给出的齐次三次身份

使用已刊 native 六规则及其完整原迹。四条二次规则的头为
$$
x^2,\quad xy,\quad xt,\quad t^2,
$$
另两条原 overlap 的三次头为 $y^3,y^2t$；它们的余项均在
$$
1,x,y,t,y^2,yt
$$
内。规则的六原来源是 $E_1,E_B^{\rm even},E_B^{\rm odd},N_1,NS,PS$；前四条和这两个 overlap 均只用前四个原二次，两个后源迹为零。

实际选定四头、两三次头的全部分母和首项，由当前已付原权因子以及三个完整排除定理支付：

- [整个等权支](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)；
- [整个 J19 权曲线](R150-appendix-unit211-W-J19-entire-original-weight-curve-exclusion.md)；
- [整个 C9 权曲线](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md)。

本次对实际 $\delta_2$ 以及 $\delta_3$ 的分子、分母逐一只剥这些已付原因子并返回，未把旧开图名称当作单位证明。

定义
$$
f_h=\frac{ux+\widehat U y}{2u}.
$$
只对这个新的三次输入作一次六规则还原，得到
$$
f_h^3-r=\sum_{i=0}^3 a_iF_i,\qquad
(F_0,F_1,F_2,F_3)=(E_1,E_B^{\rm even},E_B^{\rm odd},N_1),
\tag{4}
$$
其中 $\deg r\le2$，$\deg_{x,y,t}a_i\le1$。实际完整返回了六个原迹，且 NS/PS 两个迹确为零；没有要求这六个商生成元自由。取齐次三次部分即
$$
f_h^3=\sum_{i=0}^3a_i^{[1]}F_i^{[2]}.
\tag{5}
$$

## 4. 整个 $\gamma$ 图的显式原头 Bézout

记 $x_f,y_f$ 为 (2) 的 $f$ 系数。由原 $E_0$ 恢复有
$$
ux_f+\widehat U y_f=2u,\qquad t_f=s.
$$
因此在方向 $(x_f,y_f,s)$ 上，$f_h=1$。

设 $h_i=[f^2]Q_i$，$i=0,1,2$。相同的原均值变换给出该方向上的四个齐次值：
$$
F_0^{[2]}=h_0,\quad
F_1^{[2]}=\frac{h_0-mh_1}{\ell},\quad
F_2^{[2]}=h_1,\quad F_3^{[2]}=h_2.
$$
把 (5) 代入此方向，令 $w_i=a_i^{[1]}(x_f,y_f,s)$，得到
$$
c_0=w_0+w_1/\ell,\qquad
c_1=w_2-mw_1/\ell,\qquad c_2=w_3,
$$
$$
\boxed{c_0h_0+c_1h_1+c_2h_2=1.}
\tag{6}
$$
本次显式逐单项式把旧八变量 context 嵌入新 $(e,k,s,f)$ context，保留每个原乘子。式 (6) 与所有最终分母支付在 8.803132337 秒完成。

这给 (1) 的完整首一二次原组合。实际又把五原来源中后三列为零的组合与 $q_f$ 的全部三个 $f$ 系数回乘，8.998024917 秒完成。这里没有函数域 Euclid 或临时参数主元；纯权额外覆盖准确为常数 $1$。

作为紧凑再生定义，$c_i$ 由 (4) 的已刊固定六规则、上述唯一 $f_h^3$ 还原和 (6) 给定。完整源保留这一构造，不保存可重算大系数。实际 $c_0,c_1,c_2$ 的分子双权次数/斜率次数分别为 $(20,23,2),(19,21,2),(15,18,2)$；精确 SHA 与所有分母 profile 见小回执。

## 5. 二生成环境与不扩大的结论范围

令 $A_\gamma$ 为当前已付原权环再添加 $s$ 并局部化 $s\gamma$。由 (1)，
$$
A_\gamma[f]/(q_f)
$$
是自由秩 $2$ 的多项式环境，基为 $(1,f)$。由完整五原式取商后，每个未进一步几何局部化的商仍由 $1,f$ 生成。这不要求真实原商自由，也不等于已得到整个 W 的单位理想。

逻辑上可对五个 $Q_i$ 用首一 $q_f$ 除法，记余式 $r_i$；再取 $fr_i$ 的一次余式。这十行二列构成五原式理想在二次环境中的完整模表示。该存在性和精确性是首一除法的代数推论。然而，本次并未实际完成十条大展开及其五源乘回，故不提供任何已执行的十行 profile 或后继常数 cofactor。

物理原图还要求 $f-u\ne0$、$D\ne0$ 及个别值条件。参数环上的一般几何局部化未必保持有限模；本篇不据首一环境无条件宣称整个物理商有限自由。对固定允许的 $(e,k,s)$，$f$ 的候选至多两个，这是单一首一二次的直接结论，不是新的整个参数零维证明。

## 6. 真实执行与冻结边界

唯一运行：run46112930960，job140880267654。源 blob ad1bfee5e5047637c7d70f1bb4b6dfb4196b91a5；16808 字节，SHA256 bd68e5e5e66f31e9c3e2ad0b66468c021fc7d852d44462d3a937966200ab961c。

实际源提交 a6ccd8592f42b02a4371781c67d373d2b805ee93。05:37:30.042020 UTC 真 pull 到 dca986762f36dc9c9764c0e362bcde594a4cd412，两 README 均未变化。

驱动墙钟 180.087860103 秒，峰值 RSS 857508 KiB，内层退出码 $-14$（SIGALRM）。stdout 3494 字节，SHA256 49962638bc972a832418892a8dfda328407c60309c954bd87e3ae7efcadf5856。预算为 180 秒/4 GiB；没有内存触界证据，终止来自计时边界。

最后完成的数学 checkpoint 正是首一 $q_f$。后继十行二列、两条标量和最终 summary 均未输出。对应大展开门冻结：不加时、不换顺序重放，不以部分内部运算猜测任何未打印的完整返回。后续应更换原输入，例如完整低次加权差，而非重算此展开。

源 basename：2026-11-28-unit211-W-gamma-open-direct-native-f-cube-monic-two-8542.py。唯一依赖的完整 SHA256 为 10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1，只执行其 14656 字节六规则定义前缀，SHA256 88b8e2f49f925e51c0b940f929efb502ced9ed358228a605fea3755d9cdefff8；旧十八乘法/余子式尾没有执行。

原先 3ffb 的头 Euclid 提案从未派发，继续以“未执行、已替换”保存，不能记成运行失败。
