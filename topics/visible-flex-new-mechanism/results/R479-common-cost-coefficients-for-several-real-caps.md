# R479：当前完整 partial 目标下，多种 cap 必须满足同一组成本系数

日期：2026-11-16。**原完整公式的纸面推论，没有执行新的 profile、积分、符号、rank 或科学任务。**

本稿检查一个可能的全局入口：能否从起点选择有限多种不同外 cap，
用真实正幅复制混合它们的五个余量，从而不必让任何一条 cap 单独满足
R471 的五门。

在当前 R465/R466 的完整增强问题中，答案有一个明确限制：
**内部 partial 是逐包、逐根的向量条件，不是各 cap 的加权总和。**
在原 whole $E$、有序全通量和完整 current 归约后，
有限多 cap 给出的是同一组成本系数的共同解条件。
每一种实际 cap 仍必须分别通过五门，而且它们的唯一比例及响应系数还须一致。

本稿不排除放弃当前额外归约、改变复制方式或保留非零有序 current
的新机制。那将需要重新支付原完整目标，不能由本结论外推。

## 1. 采用的真实范围

先假设一个有限多 cap 的母库已经按原规则实际建成。
这是假设一个共同对象，不是把分别构造的几套库形式相加。
特别保留：

- 同一个完整成本、同一个原几何、同一个规范及固定 incoming；
- 原合法三矩、whole $E$、实际所需自然 total 与 $O_{\rm all}=0$；
- R465 中的完整 formal current 零归约；
- 原全部内部 Af partial，而非仅各完整包的 total；
- 每一种实际母仍有原完整同 role 复制和共同仿射查询；
- 若采用共同 $F^\star$，它及原有限布局必须从起点共同支付，
  不能默认两个不同冻结库具有同一个 $F^\star$。

每种 cap 属于 R471/R475 的允许类，左根有
$$
r_a>0,\qquad U_a(0)=h_a r_a,\qquad
U_a'(0)=s_a r_a,\qquad h_a,s_a>0,
\quad h_a>3s_a^2/5.
\tag{1}
$$
原母可分别有不同正幅和物理宽度；以下逐条按完整输运保留。

这里的完整 formal current 零，正是
$\mathcal W_0=\ker(E,\mathscr C)\cap U_0$
和
$\mathcal K_0=\mathcal R_0\cap\ker(E,\mathscr C)$
所用的原 $\mathscr C=0$，
不把在有限几处偶然读到零的行称作 universal current 零。
R465 的原全 role、仿射闭包归约仍是这些条件的使用前提。

## 2. 原两源的逐包 partial 不发生跨 cap 平均

采用 R464(14)的完整源。对一个真实 base，
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
R_i=a_i^2-b_i^2,\quad T_i=a_i b_i,
$$
则
$$
\begin{aligned}
V_d&=\sum_i a_i^2\left\{R_iS_i+\sum_{j>i}R_jU_{ij}\right\},\\
V_e&=-\sum_i a_i^2\left\{T_iS_i+\sum_{j>i}T_jU_{ij}\right\}.
\end{aligned}
\tag{2}
$$
$S_i=\Sigma_V(u_i)$ 是完整 self 场，
$U_{ij}$ 是保留原三矩 suffix 的有序场；
它们不是仅左尾或自然积分。

在第 $i$ 个包的一个实际 Af 根 $x_i$，定义真实 self 累计
$$
S_{u_i}(V;x_i)=\int_{\ell_i}^{x_i}u_i'(x)\Sigma_V(u_i)''(x)\,dx.
\tag{3}
$$
whole $\mathcal Q=0$ 使其它包在当前包上的剩余尾至多 affine，
故其二导不增加(3)。
完整 $\mathscr C=0$ 则使(2)中的有序 partial 对**每个真实 suffix**
准确为零，不能把这些 suffix 先当作相等或删去。

因此原两个 partial 在当前根准确简化为
$$
\boxed{
H_{d,i}=a_i^3 R_i\,S_{u_i}(V;x_i),\qquad
H_{e,i}=-a_i^3 T_i\,S_{u_i}(V;x_i).
}
\tag{4}
$$
原 period 读法若另有共同非零因子 $-1/(2\tau)$，
它不改变零条件；本文没有把该因子重命名成(3)。

原 high/low 编码角色的 $a_i\ne0$。
而 $R_i,T_i$ 不可能同时为零：
若 $T_i=a_ib_i=0$，则 $b_i=0$，
从而 $R_i=a_i^2\ne0$。
所以
$$
\boxed{
H_{d,i}=H_{e,i}=0
\quad\Longleftrightarrow\quad
S_{u_i}(V;x_i)=0.
}
\tag{5}
$$
这是每个实际包、每个实际 Af 根各自的必要条件。
正幅复制只给该行乘一个非零因子，
并不会把不同 $i$ 的(5)相加后再检验。

固定 incoming 或独立二阶规范的允许 $L_f$ 改变量，
在 Af 根的原通量恒等式中为零；这已经是 R408/R442 的真实范围。
因此它们不能把这里的逐点条件改成一个全包总和。
空隙 affine 常数同样不改变此处的二导读出。

## 3. 多 cap 不增加完整零权响应 self 像

R470 消费五个完整 $\mathcal K_0$ 成本后证明，
两个新响应的 self 是原 $k,j,m$ 的固定线性组合。
这些是原完整 Af self 多项式身份，
不是某一个母的数值插值。因此对任意有限合法 cap 集合同时成立。

令
$$
\mathcal S_{\rm joint}(V)
=\bigl(S_{U_1}(V),\ldots,S_{U_m}(V)\bigr)
$$
表示所有相应完整镜对多项式的共同读出，逐分量除以自己的 $r_a^5$。
则
$$
\boxed{
\mathcal S_{\rm joint}(\mathcal K_0)
=\operatorname{span}\{\mathbf k,\mathbf j,\mathbf m\}.
}
\tag{6}
$$
这里 $\mathbf k=(k_a)_a$ 等由**同一个**原成本在全部 cap 上求值得到，
不允许每个分量使用不同成本系数。

这个共同像仍恰为三维。
投影到任一 cap，R470 的 $x^8,x^7,x^0$ minor 为
$12h_a^3s_a^3\ne0$；所以联合像至少三维。
通用的两个新响应身份又给至多三维。
没有运行新的联合 rank，也没有加入未付的其它响应。

同样，原第二头满足通用身份
$$
Y_a:=S(X_Y)_a/r_a^5
=\frac{1498k_a+1407j_a+1222m_a}{110592}
+\frac{R_a}{1152}.
\tag{7}
$$
第一头仍为完整
$$
H_a=S(X_H)_a/r_a^5
=P_{H,a}/r_a^5+\sum_{\nu=0}^7 A_{\nu,a}x^\nu.
\tag{8}
$$
每一组 $A_{\nu,a}$ 都是该真实 cap 的完整单侧积分。
不同 cap 的原 $n_2$ 全积分零，不会令这些单侧积分彼此相等。

## 4. 正确的共同解是系数交条件

在 R465 的同一个完整共同商中，
$$
\mathfrak h_{\rm joint}\in
\operatorname{span}\{\mathfrak y_{\rm joint}\}
$$
的准确含义是：存在四个**共同实数**
$c,\alpha_K,\alpha_J,\alpha_M$，使
$$
\boxed{
H_a=cY_a+\alpha_Kk_a+\alpha_Jj_a+\alpha_Mm_a
\quad\text{对每个 }a\text{ 同时成立}.
}
\tag{9}
$$
原十二个同 role 不同中心及次数至多八的界，
把每个实际分量的全部采样零转成其完整多项式零；
原仿射闭包给同一个原核上的相同条件。
不是把不同 cap 各取一个中心后假设多项式恒等。

由(7)，也可写为
$$
H_a=B_Kk_a+B_Jj_a+B_Mm_a+(c/1152)R_a
\quad\text{对全部 }a,
\tag{10}
$$
其中 $B_K,B_J,B_M,c$ 同样必须共同。

对任一 cap，R471 已给充要条件
$$
\Delta_{\nu,a}=0,\qquad \nu=1,2,3,4,6.
\tag{11}
$$
成立时唯一比例为
$$
c_a=\frac{1152\beta_{5,a}}{R_{5,a}},
\qquad R_{5,a}<0.
\tag{12}
$$
而(10)的三个响应系数由原三个 pivot 唯一读出：
$$
\begin{aligned}
B_{K,a}&=-\frac{13}{11520},\\
B_{J,a}&=\frac5{512}-\frac{A_{7,a}}{s_a},\\
B_{M,a}&=-\frac{1459}{11520}
+\frac{A_{0,a}}{4h_a^3s_a^2}
-\frac{2A_{7,a}}{s_a}.
\end{aligned}
\tag{13}
$$
$R_a$ 没有 $x^8,x^7,x^0$ 项，所以不会改变(13)。

得到一个完全明确的共同充要条件：
$$
\boxed{
\begin{array}{l}
\text{每个 cap 分别满足全部五式(11)，且}\\[2pt]
c_a,\quad A_{7,a}/s_a,\quad
A_{0,a}/(h_a^3s_a^2)
\text{ 分别与 }a\text{ 无关。}
\end{array}
}
\tag{14}
$$
第一行只是逐 cap 的条件；第二行支付共同成本系数的一致性。
$B_K$ 已是通用常数，不增加另一条一致性条件。

反向也完整成立：由(14)得到共同 $c,B_K,B_J,B_M$，
再按(7)把它们换成共同 $\alpha_K,\alpha_J,\alpha_M$，
便给一个真正的原 $\mathcal K_0$ 成本线性组合实现(9)。
这仍是 signed 商的精确成员条件；
转 actual 截面时须使用 R466/R468 的原成本锥和全部基准。

## 5. 幅度、宽度和镜像不能改成交叉平均

正幅和正宽输运下，R475 给
$$
s_a\mapsto bs_a,\quad h_a\mapsto b^2h_a,\quad
A_{\nu,a}\mapsto b^{8-\nu}A_{\nu,a}.
$$
于是(14)中的三个比值全部不变：
$$
\frac{\beta_5}{R_5},\qquad
\frac{A_7}{s},\qquad
\frac{A_0}{h^3s^2}.
\tag{15}
$$
正幅本来已被逐行非零的 $r_a^5$ 吸收。
因此将不同 cap 赋予不同正幅或宽度，不能用来改变其唯一
$c_a,B_{J,a},B_{M,a}$，也不能把(11)改成加权和。

同一母的左右镜对按 R466 的完整换锚定理处理：
需要 whole $E$、完整 current 和该实际母的 total 已零，
才能用其完整 mirror graph。
在本文采用的范围内，这些原条件保留，所以(9)对完整镜对成立；
没有把右尾二次常数或单侧 $n_2$ 积分删除。

如果某一 cap 的某个 $\Delta_{\nu,a}\ne0$，
R471 的分离行可以投影到这个实际分量。
它杀共同响应像与共同第二头，但读第一头非零。
因此其它 cap 的相反数值不能抵消这条分离行。
这不是正权总和意义的符号判断，而是完整向量目标中的一条真实坐标。

即使每个 cap 的五式都已零，若(14)第二行不一致，
也不能把各自的响应解相加：
相加后的每个原成本仍作用于全部 cap，
不会只作用在为它求解的那一个分量上。

## 6. 结论边界与主零目标

本稿没有证明“任何多 cap 构造都不可能”。
它只在当前原完整增强、原复制和 whole current 归约下，
证明真实多 cap 目标是(14)的共同系数交，
而不是
$$
\sum_a w_a\Delta_{\nu,a}=0,\qquad w_a>0.
$$
后一个总和不是当前逐点 period 门。

以下变化不在本结论范围内：
保留非零有序 current 并利用真实 suffix；
改变所要求的自然查询；
不采用当前完整仿射闭包；
改变原 role/复制接口；或构造新的实际局域成本自由度。
任何一条若要用作新机制，必须从原完整源、全部 tails、
共同 $F^\star$、规范和实际基准重新支付，
不能引用(6)把它们预先排除。

因此当前主线的最小充分入口仍是：
找到一个允许 cap，满足 R471 的全部五门。
R475 已支付一个真实新 cap 上的 $\Delta _6=0$；
R477 的局部图册不等于剩余全零可达。
在目前这套真实构造内，形式地混合数个不合格 cap
不能省去这项剩余目标。
