# 真实整 Gauss–Manin Frobenius 与两类临界行的完全精度比较

日期：2026-11-12。状态：整基、整个形式盘的 Hodge 除 $p$、
实际 Frobenius 矩阵及临界系数的特征零等式均已证明。
指定行的无穷素数非零性仍未解决。

本篇与
[全权一 GM 临界行](2026-11-12-full-weight-one-gm-critical-rows.md)
使用同一个固定 $M_1=t^4+(7/2)t^6+\cdots$，以及同一 $K,L,J=L/t$。
§3–6 先取惰性素数 $p\equiv3\pmod4$、$p\ge7$；
§7 给普通素数 $p\equiv1\pmod4$、$p\ge13$ 的对应公式。
由[固定除法单位整模型](2026-11-12-weight-one-division-unit-relative-model.md)
的式 (5)–(11)，$M_1\in\mathbb Z_p[[t]]$ 对所有
$p\notin\{2,3,5,17\}$ 成立。因此本篇两类目标素数没有额外
未经计算的坏位集合。

## 1. 一个具体的整 de Rham 基

在 $R=\mathbb Z_p[[t]]$ 上考虑光滑椭圆族

$$
 \mathcal E:\quad y^2=x(x-1)(x-\lambda),\qquad
 \lambda=\tfrac12+t,\qquad s=1-4t^2.
 \tag{1}
$$

令 $\omega=dx/(2y)$、$\xi=x\omega$。
$H=H^1_{\rm dR}(\mathcal E/R)$ 是秩二自由模，$\omega,\xi$ 为整基。
可直接检查后一个断言的整性：在无穷远点的参数 $v=-x/y$ 下，
$\omega=dv+O(v)\,dv$、$\xi=v^{-2}dv+O(1)\,dv$。
$\xi$ 的唯一极部可用整的 $-v^{-1}$ 原函数作 Čech 修正；
它与 $\omega$ 的 de Rham cup pairing 是一个单位，因局部留数
的首项为 $\operatorname{res}(v\cdot v^{-2}dv)=1$，差别至多是
pairing 的整体符号。故这两个整类张成整个秩二格。

准确的 Gauss–Manin 约化为

$$
 \eta:=\nabla_{\partial_t}\omega
 =\frac{\omega}{2(1-\lambda)}
       -\frac{\xi}{2\lambda(1-\lambda)}.
 \tag{2}
$$

例如把 $g=x(x-1)/(2\lambda(1-\lambda))$ 代入
$d(g/y)$，即可核对微分形式的差是 exact。
由于 (2) 中 $\xi$ 的系数是 $R$ 的单位，

$$
 e=\binom{\omega}{\eta}
$$

也是整个形式盘上的整基，而不只是 $t=0$ 纤维上的基。
其连接矩阵为

$$
 \nabla_{\partial_t}e=A(t)e,\qquad
 A(t)=
 \begin{pmatrix}0&1\\ s^{-1}&8t\,s^{-1}\end{pmatrix}.
 \tag{3}
$$

这正对应 $(1-4t^2)y''-8ty'-y=0$。

## 2. 矩阵约定与整个形式盘上的强整除

在系数上取 Witt Frobenius $\sigma$，在基参数上明确取
$\phi(t)=t^p$。初始基域 $\mathbb Q_p$ 上 $\sigma$ 为恒等；
为了讨论 CM，可扩到 $\mathbb Q_p(i)$，此时 $\sigma(i)=-i$。
若 $h(t)$ 是一个级数，$\phi(h)=\sigma(h)(t^p)$。

令

$$
 \Phi:\phi^*H\longrightarrow H
$$

为光滑 proper 椭圆族的实际 crystalline Frobenius，使用如下**行约定**：

$$
 \Phi(e^\phi)=\mathcal F_p(t)e,\qquad
       \mathcal F_p(t)\in M_2(R).
 \tag{4}
$$

特别有整个形式盘上的整除

$$
 \mathcal F_{p,11},\mathcal F_{p,12}\in pR.
 \tag{5}
$$

这并非只从一个纤维的 Hodge 数据外推。模 $p$ 后，
crystalline–de Rham 比较把 Frobenius 化为相对 Frobenius 的
de Rham 拉回。相对 Frobenius 对正次数微分形式的拉回为零。
而 $\omega^\phi$ 在整个基上来自全局相对一形式，
即 Hodge 子模 $f_*\Omega^1_{\mathcal E/R}$。
因此其像在 $H/pH$ 为零。$H$ 无 $p$ 扭元且 (2) 是整基，
故其两个坐标均被 $p$ 整除，得到 (5)。

这里的整结构有如下明确的原始输入。Stacks Project
（2026 年查阅）的
[Remark 60.24.11，Tag 07MW](https://stacks.math.columbia.edu/tag/07MW)
给出任意 $p$ 幂零的 PD 基上，光滑提升的 crystalline–de Rham
整比较；其
[Remark 60.24.14，Tag 07MZ](https://stacks.math.columbia.edu/tag/07MZ)
把比较推广到 Noetherian、$p$-adically complete 的 PD 基和
proper smooth 提升。取 $A=R$、$I=pR$ 及 $pR$ 上的标准
divided powers，$\mathcal E/R$ 正好满足这些假设；结构晶体
$\mathcal O$ 的比较在 $D(R)$ 中成立，不需要先反转 $p$。
再由
[Theorem 60.26.4，Tag 07N0](https://stacks.math.columbia.edu/tag/07N0)
及其证明中的三个整箭头，得到相对于 $\phi$ 的整 Frobenius，
反转 $p$ 后为同构。这里 $\phi:R\to R$ 为有限自由环映射，
基可取 $1,t,\ldots,t^{p-1}$；所以该导出箭头在 $H^1$ 上正是
(4) 的 $\phi^*H\to H$，而非只有一个有理矩阵。
这些比较和拉回的函子性也保证上述模 $p$ 识别适用于整个基。

水平矩阵的有理形式另可核对 Lauder（2011），
*Degenerations and limit Frobenius structures in rigid cohomology*，
LMS J. Comput. Math. 14，1–33，§3.1 的 (3.1)–(3.2)；
[正式出版全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/81C9D72110FBEAEA55F25FFDB51BADD6/S1461157009000588a.pdf/degenerations_and_limit_frobenius_structures_in_rigid_cohomology.pdf)，
DOI [10.1112/S1461157009000588](https://doi.org/10.1112/S1461157009000588)。
该文 §3.4 的整比较讨论不作为本篇的证明输入。
上述 (5) 则给出本题相对维数一、指定基下的直接模 $p$ 证明；
不依赖该文的 degeneration 猜想。

## 3. CM 初值及系数 Frobenius

在 $t=0$，映射

$$
 \iota:(x,y)\longmapsto(1-x,iy)
$$

是 CM 自同构。由 (2) 在 $\lambda=1/2$ 的值
$\eta=\omega-2\xi$，直接得

$$
 \iota^*\omega=i\omega,\qquad \iota^*\eta=-i\eta.
 \tag{6}
$$

Frobenius 与此自同构的交换必须带系数共轭：
若 $D=\operatorname{diag}(i,-i)$，则
$D^\sigma\mathcal F_p(0)=\mathcal F_p(0)D$。
由于 $D^\sigma=-D$，初值的对角项都为零。
结合 (5)，可写

$$
 \boxed{\qquad
 \mathcal F_p(0)=
 \begin{pmatrix}0&pa_p\\ b_p&0\end{pmatrix},
 \quad a_p,b_p\in\mathbb Z_p^\times,\quad a_pb_p=-1.
 \qquad} \tag{7}
$$

这里下标 $p$ 的 $a_p,b_p$ 只是本篇的矩阵常数，不是椭圆曲线的
Frobenius trace 或实际 theta 系数。
它们属于 $\mathbb Q_p$，因为曲线、所选基以及初始 Frobenius 都在
$\mathbb Q_p$ 上定义。

最后两个断言可不计算任何 $p$-adic gamma 值就核实：
在 $\lambda=1/2$ 的有限域曲线上，$x\mapsto1-x$ 把右侧多项式变号，
而 $(-1/p)=-1$，所以二次角色和为零，点数为 $p+1$。
因此 cohomology Frobenius 的特征多项式是 $X^2+p$，
行列式准确为 $p$。对 (7) 取行列式得到 $a_pb_p=-1$。
由整性，两者必都是单位。

## 4. 用固定两条周期写出实际矩阵

令

$$
 Y(t)=
 \begin{pmatrix}K(t)&L(t)\\ K'(t)&L'(t)\end{pmatrix},
 \qquad Y(0)=I,\qquad \det Y=s^{-1}.
 \tag{8}
$$

行约定 (4) 下，水平性准确为

$$
 \mathcal F_p'+\mathcal F_p A
      =pt^{p-1}A(t^p)\mathcal F_p.
 \tag{9}
$$

所有 $K,L$ 系数为有理数，因此在本式中它们的系数 $\sigma$ 不产生
另一个解。由 $Y'=AY$、初值及特征零形式解的唯一性，得到

$$
 \boxed{\quad
 \mathcal F_p(t)=
       Y(t^p)\mathcal F_p(0)Y(t)^{-1}.
 \quad} \tag{10}
$$

这个次序依赖明确的行约定；不能与相反约定的
$Y\mathcal F_p(0)Y(t^p)^{-1}$ 混写。
由
$Y^{-1}=s\begin{pmatrix}L'&-L\\-K'&K\end{pmatrix}$，
定义两个实际整 Frobenius 函数

$$
 U_p(t)=\frac{\mathcal F_{p,12}(t)}{pa_ps(t)},
 \qquad
 V_p(t)=-\frac{\mathcal F_{p,22}(t)}{b_ps(t)}.
 \tag{11}
$$

(4)–(5) 及单位性保证 $U_p,V_p\in\mathbb Z_p[[t]]$。
它们的准确周期表达为

$$
 \boxed{\begin{aligned}
 U_p&=K(t^p)K(t)
       -\frac{b_p}{pa_p}L(t^p)L(t),\\
 V_p&=L'(t^p)L(t)
       -\frac{pa_p}{b_p}K'(t^p)K(t).
 \end{aligned}} \tag{12}
$$

注意 $L'(t^p)$ 表示先求导再代入，绝不是
$dL(t^p)/dt$。初值为 $U_p(0)=1,V_p(0)=0,V_p'(0)=1$。
并且在特征零级数环中准确有

$$
 \operatorname{ord}_t(U_p-K)=p+1,\qquad
 \operatorname{ord}_t(V_p-L)=p,
 \tag{13}
$$

两个首差分别为 $-b_p/(pa_p)$ 和 $-pa_p/b_p$。
它们的赋值分别是 $-1$、$+1$；并未把这两种精度混同。
尤其，$U_p$ 的整性准确消去了 $K$ 在次数 $p+1$ 的首次分母：

$$
 p[t^{p+1}]K\equiv b_p/a_p\pmod p.
 \tag{14}
$$

这与[周期分母证明](2026-11-12-gauss-manin-period-denominators.md)
的单位首项相符。

## 5. 对实际临界系数是特征零完全相等

令 $J_p^{\rm F}=V_p/t\in1+t^2\mathbb Z_p[[t]]$。
全权一公式给

$$
 C_{p+1}=[t^{p+1}]
             \frac{M_1K^{p+1}}{sJ^{p+2}}.
$$

由 (13)，$U_p-K$ 起于 $t^{p+1}$，
$J_p^{\rm F}-J$ 起于 $t^{p-1}$；
而 $M_1$ 起于 $t^4$。所以它们对目标次数的影响分别最早在
$p+5$、$p+3$。因此实际有

$$
 \boxed{\quad
 C_{p+1}=[t^{p+1}]
       \frac{M_1U_p^{p+1}}{s(J_p^{\rm F})^{p+2}}.
 \quad} \tag{15}
$$

这不是模 $p^2$ 的近似，而是 $\mathbb Q_p$ 中的完全相等；
所以任意需要的 $p$-adic 精度都被保留。
右侧只用同一个实际整 rank-two Frobenius 的两个条目、指定初值
以及固定代数函数 $M_1$。

## 6. 全级数层面的整除差与实际第一行

置

$$
 B_p^{\rm F}=\frac{U_p}{J_p^{\rm F}},\qquad
 W_p^{\rm F}=\frac{M_1U_p}{s(J_p^{\rm F})^2}.
 \tag{16}
$$

它们现在是完整的整级数，$B_p^{\rm F}=1+O(t^2)$、
$W_p^{\rm F}=t^4+O(t^6)$。
可以在整个形式盘而不只是有限 jet 上定义

$$
 \Delta_p(B_p^{\rm F})
   =\frac{(B_p^{\rm F}(t))^p-B_p^{\rm F}(t^p)}p
        \in\mathbb Z_p[[t]].
 \tag{17}
$$

在非分歧扩域的表示中，第二项应写
$\sigma(B_p^{\rm F})(t^p)$；本篇的矩阵定义在 $\mathbb Q_p$，
所以 $\sigma$ 固定其系数。
$B_p^{\rm F}(t^p)-1$ 起于 $t^{2p}$，故 (15) 给准确恒等式

$$
 C_{p+1}
   =[t^{p+1}]W_p^{\rm F}
       +p[t^{p+1}]
                  W_p^{\rm F}\Delta_p(B_p^{\rm F}).
 \tag{18}
$$

由实际平方公式
$C_{p+1}=(p+1)!\beta_{p+1}^2/(24\,17^{p-3})$
及 $\beta_{p+1}$ 整，左边被 $p$ 整除。
于是第一项也被 $p$ 整除，得到完全保精度的行

$$
 \boxed{\quad
 \frac{C_{p+1}}p
   =\frac{[t^{p+1}]W_p^{\rm F}}p+
       [t^{p+1}]W_p^{\rm F}\Delta_p(B_p^{\rm F}).
 \quad} \tag{19}
$$

其模 $p$ 版本正是原来的
$[t^{p+1}](Z_i+W_i\log(K/J))$。
这里 (17) 是真实整 Frobenius 条目所构造的除法差；
没有把单独代数函数 $M_1$ 的低阶零 Frobenius 行当成 (19)。

## 7. 普通素数的同一整 Frobenius 规范

现在设 $p\equiv1\pmod4$、$p\ge13$。
§1–2 的整基与整个形式盘整除仍成立。
区别是 $\sigma(i)=i$，所以 (6) 与 Frobenius 的交换使初值为对角矩阵。
由 Hodge 除 $p$ 及行列式 $p$，准确有

$$
 \mathcal F_p(0)=\operatorname{diag}(pa_p,b_p),\qquad
 a_p,b_p\in\mathbb Z_p^\times,\qquad a_pb_p=1.
 \tag{20}
$$

(10) 的矩阵次序保持不变。在普通情形改定义

$$
 \begin{aligned}
 U_p&=\frac{\mathcal F_{p,22}}{b_ps}
       =L'(t^p)K-\frac{pa_p}{b_p}K'(t^p)L,\\
 V_p&=-\frac{\mathcal F_{p,12}}{pa_ps}
       =K(t^p)L-\frac{b_p}{pa_p}L(t^p)K.
 \end{aligned} \tag{21}
$$

它们同样完整地属于 $\mathbb Z_p[[t]]$，初值为 $1$ 与 $t$，
且 $U_p-K$、$V_p-L$ 的首次数仍分别为 $p+1,p$。
但首差的赋值顺序与惰性相反：现在分别为 $+1,-1$。
第二式准确取消 $J$ 在次数 $p-1$ 的首次分母。

写 $H_p=V_p/t$、$B_p^{\rm F}=U_p/H_p$，并令

$$
 W_{o,p}^{\rm F}=\frac{M_1}{sU_p}.
$$

与惰性相同的次数检查给**特征零完全相等**

$$
 \boxed{\quad
 C_{p-1}=[t^{p-1}]W_{o,p}^{\rm F}(B_p^{\rm F})^p.
 \quad} \tag{22}
$$

于是原普通第二除 $p$ 行，可用完整整函数定义为

$$
 \begin{aligned}
 \widetilde{\mathcal G}_{o,p}
 ={}&(t\partial_t+1)^{-2}W_{o,p}^{\rm F}\\
 &+(t\partial_t+1)^{-1}
       \bigl(W_{o,p}^{\rm F}\log B_p^{\rm F}\bigr)
   +\tfrac12W_{o,p}^{\rm F}(\log B_p^{\rm F})^2 .
 \end{aligned} \tag{23}
$$

Euler 逆均逐系数定义。保留原来三个项的完整相加，得到

$$
 [t^{p-1}]\widetilde{\mathcal G}_{o,p}
       \equiv C_{p-1}/p^2\pmod p.
 \tag{24}
$$

该指定系数整的证明仍使用真实 $C_{p-1}\in p^2\mathbb Z_p$；
不将第一项单独认作整。

## 8. 真正整 Frobenius 代表的首次分母推迟至 $2p+4$

两种情形的 $U_p,V_p$ 都满足

$$
 B_p^{\rm F}=1-t^2+O(t^4),\qquad
 W_{i,p}^{\rm F},W_{o,p}^{\rm F}=t^4+O(t^6),
 \tag{25}
$$

所有这些函数均为偶的整级数。惰性情形的 $W_{i,p}^{\rm F}$
就是 (16) 的 $W_p^{\rm F}$，并定义

$$
 \widetilde{\mathcal G}_{i,p}
   =(t\partial_t-1)^{-1}W_{i,p}^{\rm F}
       +W_{i,p}^{\rm F}\log B_p^{\rm F},
 \tag{26}
$$

其中齐次的一次项取零。
其临界系数与 $C_{p+1}/p$ 模 $p$ 相同。

由于 $B_p^{\rm F}-1$ 起于二次，形式对数中首次可能除以 $p$ 的项
是 $(B_p^{\rm F}-1)^p/p$。结合二次系数 $-1$，准确得到

$$
 [t^n]\log B_p^{\rm F}\in\mathbb Z_p\ (n<2p),\qquad
 p[t^{2p}]\log B_p^{\rm F}\equiv-1\pmod p.
 \tag{27}
$$

其余 $k<p$ 的对数项整，$k>p$ 的项还不影响次数 $2p$。
因此，$W\log B_p^{\rm F}$ 的首坏项在次数 $2p+4$，
该系数乘 $p$ 后为 $-1$ 模 $p$。

惰性情形中，偶数 $n\le2p+4$ 的 $n-1$ 只有在 $n=p+1$
才可能被 $p$ 整除；该临界分母已由 (18) 与真实 $C_{p+1}\in p$
消去。故 Euler 项不能取消 (27) 所生的分母，得到

$$
 \boxed{\quad
 p[t^{2p+4}]\widetilde{\mathcal G}_{i,p}\equiv-1\pmod p,
 \quad
 [t^n]\widetilde{\mathcal G}_{i,p}\in\mathbb Z_p\ (n<2p+4).
 \quad} \tag{28}
$$

普通情形中，偶数 $n\le2p+4$ 的 $n+1$ 只有在 $n=p-1$
才可能被 $p$ 整除。该系数的完整三项相消由 (22) 与
$C_{p-1}\in p^2$ 保证。
$W_{o,p}^{\rm F}(\log B_p^{\rm F})^2$ 对次数 $\le2p+4$ 的贡献仍整：
对数平方本身的首次非整项在次数 $2p+2$，
再乘 $W_{o,p}^{\rm F}$ 后最早在 $2p+6$。
因 $2p+5\equiv5\pmod p$，所以

$$
 \boxed{\quad
 p[t^{2p+4}]\widetilde{\mathcal G}_{o,p}\equiv-\frac15\pmod p,
 \quad
 [t^n]\widetilde{\mathcal G}_{o,p}\in\mathbb Z_p\ (n<2p+4).
 \quad} \tag{29}
$$

这是整 Frobenius 规范的实际正面改善：
旧固定标量行的首坏次数分别为 $p+5$、$p+3$，
而保留同一指定临界系数的新代表都推迟到 $2p+4$。
$U_p,V_p$ 及新代表通过真实 Frobenius 依赖于 $p$；
因此这一改善还不能直接作为一个固定、与 $p$ 无关的 adelic germ
的算术大小估计。

## 9. 已实现与仍缺少的部分

(10)–(29) 给出了实际 rank-two crystalline Frobenius、Hodge 整格、
正确初值和原临界系数之间的明确接口。
它比只声明“存在有限维 Frobenius”多保留了被 $p$ 除掉的完整信息。

但 (17) 是非线性的 $p$ 次幂差，(19) 还取次数随 $p$ 增长的 jet。
本篇未把这一行证明为某个固定秩**线性**相对 cohomology 的
Frobenius 矩阵条目，也未证明其指定值的跨 $p$ 非零性。
实际上，(13) 说明它在临界短 jet 上准确恢复原来的 $K,L$ 数据，
不能仅因现在的代表完整且整，就将未知非零结论视作已经得到。

下一步需要把固定 $M_1$ 的真实 relative Kummer 代表与 (19)
一起比较；若只保留普通 cohomology 类、或只保留 $\mathcal F_p(0)$，
都还没有说明为何能恢复这里的加权除 $p$ 行。
