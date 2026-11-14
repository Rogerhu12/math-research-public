# R193. 固定普通矩的差商与前六条真实中央行

日期：2026-11-12。**状态：下述固定矩引理、原有理校准与
六行中央秩界已证明，全文和脚本均已独立复核。** 本篇始终保留非单位
区间积分的准确误差，不需要比较不同曲线的 Euler 因子，也
不把一个固定普通素数处的非零误写成无穷目标素数处的非零。

## 1. 原对象与结论

采用 R155/R162 的原固定平面
$$
 A(w)=A_2(z),\qquad B(w)=B(z),\qquad w=z^4,
 \qquad A=w+\cdots,\quad B-A=-22w^2+\cdots.
 \tag{1}
$$
对 $4\mid m$，记原 Hurwitz 系数为
$$
 H_{A,m}=m![z^m]A_2(z),\qquad
 H_{B,m}=m![z^m]B(z).
 \tag{2}
$$
本篇证明，对每个正整数 $r$，
$$
 \boxed{\begin{aligned}
 v_{13}(H_{A,12r})&=v_{13}(H_{B,12r})=1+v_{13}(r),\\
 v_{13}\!\left(
 H_{A,12r}H_{B,24r}-H_{B,12r}H_{A,24r}
 \right)&=3+3v_{13}(r).
 \end{aligned}}
 \tag{3}
$$
特别，上式中的行列式从不为零。

令真实有理中央行
$$
 R_s^{(r)}=([w^{rs}]A,[w^{rs}]B).
 \tag{4}
$$
则 $R_3^{(r)},R_6^{(r)}$ 对每个 $r\ge1$ 线性独立，且
$$
 v_{13}\det(R_3^{(r)},R_6^{(r)})
 =3+3v_{13}(r)-v_{13}((12r)!)-v_{13}((24r)!).
 \tag{5}
$$
因而最先两个实际中央秩跳的行号 $a<b$ 满足
$$
 \boxed{\quad 1\le a\le3,\qquad a<b\le6.\quad}
 \tag{6}
$$
这个结论不依赖目标惰性素数，也不依赖两个完整中央导数的
消失假设。

## 2. 同一普通整测度和原矩

这里只固定辅助普通素数 $q=13$。R155 及 R158 全文在同一个
完备未分歧整系数环 $\mathcal O$ 上给出单位 $\Omega_q$ 和
两个范数至多一的整测度 $\mu_A,\mu_B$，其 Amice 变换是
$$
 A_2(\Omega_q\log(1+T)),\qquad
 B(\Omega_q\log(1+T)).
$$
所以对所有整数 $m\ge0$，准确有
$$
 \int_{\mathbb Z_q}x^m\,d\mu_F(x)=\Omega_q^m H_{F,m},
 \qquad F=A,B.
 \tag{7}
$$
这是原普通系数源的实际规范。$\Omega_q$ 对两行相同，并且是
单位；本篇不把它设成一。

R155 的两个原质量条件，亦即 R118 的原中心零条件，给
$$
 \int_{\mathbb Z_q^\times}1\,d\mu_A
 =\int_{\mathbb Z_q^\times}1\,d\mu_B=0.
 \tag{8}
$$
这里仅使用已经证明的质量零，没有使用任何未知的中心导数
零或有限性结论。

定义真正的单位区间解析矩
$$
 J_F(t)=\int_{\mathbb Z_q^\times}
         \exp\!\bigl(t\log(x^{q-1})\bigr)\,d\mu_F(x),
 \qquad t\in\mathbb Z_q.
 \tag{9}
$$
由于 $\log(x^{q-1})\in q\mathbb Z_q$，逐项积分绝对收敛，并且
$$
 J_F(t)=\sum_{k\ge0}j_{F,k}t^k,\qquad
 v_q(j_{F,k})\ge k-v_q(k!),\qquad j_{F,0}=0.
 \tag{10}
$$
故 $J_F\in\mathcal O\langle t\rangle$。

若 $t$ 是正整数、$m=(q-1)t$，则 (9) 的被积函数准确等于
$x^m$。把 (7) 按单位和非单位两个开闭区间拆开，得到
$$
 J_F(t)=\Omega_q^m H_{F,m}-E_F(t),\qquad
 E_F(t)=\int_{q\mathbb Z_q}x^m\,d\mu_F(x)
                  \in q^m\mathcal O.
 \tag{11}
$$
这是完整非单位矩的绝对误差界。没有删除非单位区间，也没有
把误差视为一个随 $t$ 解析的 Euler 因子。

## 3. 差商引理

以下论证对任一奇素数 $q\ge5$ 都成立，条件是有 (7)–(11)
中的同一单位尺度和两个整测度。假设在 $t=1,2$ 处已准确
校准
$$
 \begin{aligned}
 v_q(H_{A,q-1})=v_q(H_{B,q-1})&=1,\\
 v_q(H_{A,2(q-1)})=v_q(H_{B,2(q-1)})&=1,\\
 v_q\det\begin{pmatrix}
 H_{A,q-1}&H_{B,q-1}\\
 H_{A,2(q-1)}&H_{B,2(q-1)}
 \end{pmatrix}&=3.
 \end{aligned}
 \tag{12}
$$

由 (10) 定义
$$
 F_A(t)=\frac{J_A(t)}{qt},\qquad
 F_B(t)=\frac{J_B(t)}{qt}.
 \tag{13}
$$
在 $t=0$ 处按解析延拓定义。$t^k$ 系数的赋值至少
$k-v_q((k+1)!)$。对 $q\ge5$，该下界在 $k=1$ 至少为一，
在所有 $k\ge2$ 至少为二。因此向量
$F=(F_A,F_B)$ 有准确表示
$$
 F(t)=v_0+qv_1t+q^2U(t),\qquad
 v_0,v_1\in\mathcal O^2,\quad
 U(t)\in\mathcal O\langle t\rangle^2.
 \tag{14}
$$
这里的 $v_0$ 是本节的向量，不是 (1) 中的系数 $-22$。

由 (11) 和 (12)，$J_A(1),J_B(1)$ 的赋值都是一；
$J_A(2),J_B(2)$ 亦然。两个行列式比较时，误差赋值至少为
$(q-1)+1\ge5$，而原行列式赋值为三；共同尺度
$\Omega_q^{3(q-1)}$ 为单位。故
$$
 v_q\det(J(1),J(2))=3,\qquad
 v_q\det(F(1),F(2))=1.
 \tag{15}
$$
把 (14) 代入第二式，模 $q^2$ 得
$$
 \det(F(1),F(2))\equiv q\det(v_0,v_1)\pmod{q^2}.
$$
所以
$$
 \det(v_0,v_1)\in\mathcal O^\times.
 \tag{16}
$$
又由 $F_A(1),F_B(1)$ 为单位及 (14)，$v_0$ 的两个坐标都
为单位。因此 $F_A(t),F_B(t)$ 对所有 $t\in\mathbb Z_q$ 都是
单位。

对任意 $U\in\mathcal O\langle t\rangle$，
$$
 \frac{U(t_2)-U(t_1)}{t_2-t_1}\in\mathcal O
 \quad(t_1,t_2\in\mathbb Z_q,\ t_1\ne t_2).
 \tag{17}
$$
这是逐项恒等式
$(t_2^k-t_1^k)/(t_2-t_1)=\sum_{j=0}^{k-1}t_2^{k-1-j}t_1^j$
和 Tate 系数趋零的直接推论。将 (14) 代入行列式并先作
第二行减第一行，(17) 给
$$
 \det(F(t_1),F(t_2))
 =q(t_2-t_1)\bigl(\det(v_0,v_1)+qW(t_1,t_2)\bigr),
 \qquad W(t_1,t_2)\in\mathcal O.
 \tag{18}
$$
由 (16)，括号始终为单位。所以对任意两个不同的
$t_1,t_2\in\mathbb Z_q$，
$$
 v_q\det(F(t_1),F(t_2))=1+v_q(t_2-t_1).
 \tag{19}
$$
这不是由若干数值样本推断全局无零点，而是准确整差商的
单位性结论。

特别对正整数 $t$，
$$
 \begin{aligned}
 v_q J_A(t)=v_q J_B(t)&=1+v_q(t),\\
 v_q\det(J(t),J(2t))&=3+3v_q(t).
 \end{aligned}
 \tag{20}
$$
这里保留了 (13) 中两行的 $qt$、$2qt$，以及 (18) 中
$t_2-t_1=t$ 的第三个 $t$ 因子。

## 4. 从单位区间回到原 Hurwitz 系数

置 $v=v_q(t)$、$m=(q-1)t$。由 (11)，原矩向量
$$
 M(t)=\Omega_q^m(H_{A,m},H_{B,m})
$$
与 $J(t)$ 的差在 $q^m\mathcal O^2$ 中；$M(2t)-J(2t)$
在 $q^{2m}\mathcal O^2$ 中。由 (20)，行列式误差的赋值至少
$$
 \min\{m+1+v,\;2m+1+v,\;3m\}=m+1+v.
 \tag{21}
$$
对每个正整数 $t$，有
$$
 (q-1)t>2+2v_q(t)
 \qquad(q\ge5).
 \tag{22}
$$
例如 $v_q(t)\le t-1$，左边至少 $4t$，右边至多 $2t$。
所以 (21) 严格大于 (20) 的主项赋值 $3+3v$。共同尺度为
单位，遂得到准确等式
$$
 \boxed{\begin{aligned}
 v_q H_{A,(q-1)t}=v_q H_{B,(q-1)t}&=1+v_q(t),\\
 v_q\det\begin{pmatrix}
 H_{A,(q-1)t}&H_{B,(q-1)t}\\
 H_{A,2(q-1)t}&H_{B,2(q-1)t}
 \end{pmatrix}&=3+3v_q(t).
 \end{aligned}}
 \tag{23}
$$
第一行使用 $m>1+v$，按同一个误差比较证明。

本证明没有在非单位区间定义 $q^t$ 的解析延拓；(11)、(21)
只在正整数 $t$ 上使用，这正是回到原 Taylor 系数所需的
全部范围。

## 5. q=13 的完整有理输入

原 $E_0$ 上使用 R57 的无分母整数流
$$
 u''=-2u^3,\quad u(0)=0,\ u'(0)=1,\qquad
 L'=u^2,\ L(0)=0,\qquad
 \theta'=L\theta,\ \theta(0)=1,\qquad \sigma=u\theta.
 \tag{24}
$$
置 $s=u^4$。R162 的原两条截面准确为
$$
 A=\theta^{68}P(s),\qquad B=\theta^{68}Q(s),
 \tag{25}
$$
其中 $P,Q$ 是已经固定的两条十六次有理多项式，并保留其
$1/5$ 常数。

对 (24) 的 Hurwitz 整数递推计算到 $z^{24}$，再代入 (25)，
得到

| $m$ | $H_{A,m}$ | $H_{B,m}$ |
| --- | ---: | ---: |
| 12 | 78409064448 | 178871666688 |
| 24 | 3828459347334561461270740992 | 1168753707306387730587451392 |

四个数的 $13$ 赋值均准确为一。写上述 $2\times2$ 行列式为
$\Delta$，直接整数算术给
$$
 \Delta\equiv210912\pmod{13^5},\qquad
 \frac{\Delta}{13^3}\equiv96\pmod{13^2},\qquad
 \frac{\Delta}{13^3}\equiv5\pmod{13}.
 \tag{26}
$$
因此 $v_{13}(\Delta)=3$，恰好支付 (12)。

校准脚本还用另一种算法复算全部 $w^0,\ldots,w^6$ 系数：
先以 R162 的有理 $s$ 级数构造 $A,B$，再逆转
$$
 w=s\left(\sum_{n\ge0}
        \frac{\binom{2n}{n}}{4^n(4n+1)}s^n\right)^4.
$$
它与整数 ODE 逐项一致。第一条 $A_2$ 另与 R57 实际六因子
乘积的 $2^{m-4}$ 缩放核对。未输入任何 $J_F'(0)$ 值，也
未输入任何目标惰性素数的中央失败假设。

将 $q=13,t=r$ 代入 (23)，得到 (3)。按 (2) 除回两个准确
阶乘，得到 (5) 及前六行的独立性；同时 $R_3$ 的两个坐标
均不为零，故 (6) 中 $a\le3$。

## 6. 对真实 Stokes 部分和的影响

对目标惰性 $p=4r-1\ge7$，取原中央行的最先两个秩跳
$a<b$。R190 的同一整轴换元和实际权给
$$
 \det(q_a,q_b)=\omega_a\omega_b\det(R_a^{(r)},R_b^{(r)}).
 \tag{27}
$$
本篇使这两个真实部分和的层号统一满足 (6)。因此不再需要
定性地寻找无界层号，也不能继续把“有效层数是否存在统一
界”列为未付条件。

由于 $a,b\le6<p$，两个权的赋值准确为
$v_p(\omega_a)=a-1$、$v_p(\omega_b)=b-1$。若两个完整中央
导数都为零，R185 的完整尾界和 (27) 给
$$
 \boxed{\quad
 \min_i v_p((R_a^{(r)})_i)\ge1,\qquad
 v_p\det(R_a^{(r)},R_b^{(r)})\ge2.
 \quad}
 \tag{28}
$$
仍须在目标 $p$ 处控制这个原有理 minor，或将这些真实条件
放回同一完整前缀格。式 (3) 控制的是固定辅助素数 $13$ 的
赋值；它不自动给出随 $r=(p+1)/4$ 变化的目标 $p$ 赋值。
任意指定的 $q_3,q_6$ 也未被宣称独立：(27) 使用的是前六层
中的首次两个真实秩跳。

### 6.1. 目标素数处的完整阶乘相消和有界成本

仍取这两个首次秩跳，置
$$
 m_a=(p+1)a,\qquad m_b=(p+1)b,\qquad
 \Delta_{a,b}
 =H_{A,m_a}H_{B,m_b}-H_{B,m_a}H_{A,m_b}\ne0.
 \tag{29}
$$
因为 $a,b<p$，$m_a,m_b<p^2$，准确有
$v_p(m_a!)=a$、$v_p(m_b!)=b$。结合 (27)，得到
$$
 \boxed{\quad v_p\det(q_a,q_b)=v_p(\Delta_{a,b})-2.\quad}
 \tag{30}
$$
两个最高阶乘的 $a+b$ 与真实权的 $a+b-2$ 已全部保留并
相消；没有把它们藏入一个未知单位。

由 (24) 的整数 Hurwitz 流和 (25) 的唯一 $1/5$ 分母，
$25\Delta_{a,b}$ 是非零整数。R190 的固定正 theta 增长界
$|A(z)|,|B(z)|\le C e^{c|z|^2}$，经半径
$\sqrt{m/(2c)}$ 上的 Cauchy 估计及 Stirling 界，给
$$
 \log\max(1,|5H_{F,m}|)
 \le\frac m2\log m+O(m),\qquad F=A,B.
 \tag{31}
$$
常数只依赖原两个固定函数。因此
$$
 \begin{aligned}
 v_p(\Delta_{a,b})
 &\le\frac{\log|25\Delta_{a,b}|}{\log p}\\
 &\le\frac{m_a\log m_a+m_b\log m_b}{2\log p}
       +O\!\left(\frac{m_a+m_b}{\log p}\right)\\
 &\le\left(\frac92+o(1)\right)p.
 \end{aligned}
 \tag{32}
$$
有限集合 $1\le a\le3,\ a<b\le6$ 使误差对实际随 $p$ 变化
的首次跳跃仍一致。式 (30) 遂给同一个上界于
$v_p\det(q_a,q_b)$；固定小素数可吸收到一个绝对常数倍 $p$
中。

在两个完整中央导数均为零的假设下，
$q_a\in p^a\mathbb Z_p^2$、$q_b\in p^b\mathbb Z_p^2$。
故下面是一个实际整矩阵：
$$
 Q'=\begin{pmatrix}p^{-a}q_a\\p^{-b}q_b\end{pmatrix},
 \qquad
 e'=v_p\det Q'
       =v_p(\Delta_{a,b})-a-b-2\ge0.
 \tag{33}
$$
这一步先按两层各自的准确目标格归一，才对 $Q'$ 作整
Smith 分解。设其指数为 $0\le\kappa'_1\le\kappa'_2$，则
$$
 \kappa'_1+\kappa'_2=e'
       \le\left(\frac92+o(1)\right)p.
 \tag{34}
$$
R189 的两个完整原 Hasse 族因而变成
$(p^{\kappa'_1}\partial_XP,p^{\kappa'_2}\partial_YP)$，
其中源变量换基和目标换基都是整可逆的。其非零 Smith 指数
为
$$
 \min\{\kappa'_1+v_p(i),\,\kappa'_2+v_p(j)\},
 \qquad 1\le i+j\le D,\quad v_p(0)=+\infty.
 \tag{35}
$$
这些指数的最大值准确为
$$
 \kappa'_2+\lfloor\log_p D\rfloor
 \le e'+\lfloor\log_p D\rfloor.
 \tag{36}
$$
上界由 $i,j\le D$ 得出，下界由
$(i,j)=(0,p^{\lfloor\log_pD\rfloor})$ 达到。常数多项式的核
仍保留，没有把它算作可恢复的方向。

这里支付了两个真实有限方向及其源恢复成本。R189 从加权
Cartan 输入读出这些 Hasse 行的精度成本，以及这些输入与
同一个完整曲线前缀的比较，仍须另付。式 (36) 不是一项可
直接从最终 jet 预算中扣除的净收益。

## 7. 依赖与复算

- [R155：同一原普通整测度、共同单位周期和两个质量条件](R155-two-theta-rows-common-amice-lattice.md)。
- [R158 全文：原矩公式 (1.4)–(1.7)](../notes/2026-11-12-ordinary-falling-factorial-saturated-jets.md)。
- [R162：原 P、Q 和固定有理平面](R162-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)。
- [R57：无分母整数流与实际乘积](R57-global-hurwitz-integers-and-fixed-polynomial-flow.md)。
- [R185：完整实际 Stokes 权和尾界](R185-integral-axis-stokes-functional-and-complete-central-tests.md)。
- [R190：首次中央秩跳的准确换元行列式](R190-central-projection-of-square-theta-sections.md)。
- [R189：真实双方向 Hasse 族和完整 Smith 指数](R189-complete-central-hasse-families-and-weighted-core.md)。
- [校准脚本](../scripts/check-fixed-ordinary-moment-minor.py)。

本篇的无限范围来自整差商和显式误差不等式；有限整数校准
只承担 (12) 中明确的四个值与一个非零行列式。
