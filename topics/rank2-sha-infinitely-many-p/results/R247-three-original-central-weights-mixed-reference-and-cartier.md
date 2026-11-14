# R247 — 原三来源前三中央权：混合整参考、真实下一位与三权聚合

日期：2026-11-13。**状态：三源的准确三权归一矩阵、全部负层与移动 log 消去、首行的真实下一位、第三权的几何 carry，以及显式有限 Cartier 表达均已证明。未证明三条完整中央导数不能同时为零。**

本篇把 R197/R213 的两列两权扩到 R243 的实际第三来源。主要新增点是：

- 原混合整参考可严格延长至三个中央权所需的窗口 $<3r<p$；
- 第三来源的二次角因子在原 Lagrange 核中准确相消；
- 第三权必须补一个有单位系数的原几何 carry；
- 实际有限中央条件是一条保留下一位的聚合同余，不是将三个中央系数各自置零。

## 1. 全部来源与参数均固定

取惰性素数
$$
p=4r-1\ge19,\qquad O=\mathbf Z_p,\qquad d=(p-1)/2=2r-1.
$$
用原 $E_0:y^2=x^3-x$、$dz=dx/(2y)$ 的参数
$$
u=x^{-1/2}=z+O(z^5),\quad s=u^4,\quad w=z^4=W(s)=sF(s)^4,
$$
其中
$$
F(s)=\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j(4j+1)}s^j,\qquad
G(s)=F+4sF'=(1-s)^{-1/2}.
\tag{1}
$$
记
$$
L(s)=\log\vartheta(z(s))^{68}.
$$
R197 的原多项式仍记 $P,Q$；R243 的完整反序多项式记 $Q_{15}$。于是三条原来源准确为
$$
\mathbf A(s)=e^{L(s)}\mathbf S(s),\qquad
\mathbf S=(P,Q,s\sqrt{1-s}\,Q_{15}).
\tag{2}
$$
它们分别是 $A=A_{17}(2z)/16$、$B=A_{34}(z)$、$H=A_{136}(z)$，均以 $w$ 为首项一。平方根恒取常数项一的支。新来源的二挠扭转没有删除。

以下固定特征零数及参数：
$$
c=68k_r=[w^r]L(s(w)),\qquad
\ell=[s^r]L(s),\qquad t=s^rF(s),\qquad \alpha=p\ell.
\tag{3}
$$
R197/R213 给 $c-\ell\in O$，且
$$
\bar\alpha=68\kappa,\qquad
\kappa=\frac{\binom{2r-2}{r-1}}{4^{r-1}}\in\mathbf F_p^\times .
\tag{4}
$$
$\alpha$ 在下面需要高精度的式子中始终是 (3) 的原数；不能任意选择 (4) 的提升。

## 2. 混合参考确实可整地延长到第三权

置
$$
\widetilde\Gamma(s)=\exp(L(s)-\ell t(s))\pmod{s^{3r}}.
\tag{5}
$$
**命题 1。** $\widetilde\Gamma\in O[s]/(s^{3r})$，且
$[s^r]\log\widetilde\Gamma=0$。

证明所需的范围比 R213 大，但仍未跨过 $p$。由 R215，原 $u(z)$ 在本窗口所读的次数 $<p^2$ 都整。对于
$$
k_n=\frac{[z^{4n-2}]u^2}{4n(4n-1)},\qquad 1\le n<3r,
$$
分母中只有 $n=r$ 含 $p$，且恰含一次。因此
$L-cW^r$ 在 $s$ 次数 $<3r$ 整。所有指数展开阶乘均小于 $p$。

另一方面，$F$ 在此窗口整，且
$F^p-1\in pO[s]/(s^{3r})$；后者只需在次数 $<p$ 使用
$F^p=\exp(p\log F)$。准确等式
$$
L-\ell t=(L-cW^r)+(c-\ell)t+c\,t(F^p-1)
\tag{6}
$$
便证明对数整性，继而证明 (5)。第 $r$ 项为零直接来自 $[s^r]t=1$。$\square$

这份实际参考还有完全明确的模 $p$ 表达。令
$$
h(s)=\sum_{j=0}^{d}\frac{(-1)^j\binom dj}{4j+1}s^j,\qquad
4sh'+h=(1-s)^d,
\tag{7}
$$
并定义
$$
\begin{aligned}
\mathcal B_p(s)&=\frac{17}{4}(1-s)^d
 \sum_{\substack{0\le j\le d\\j\ne r-1}}
 \frac{(-1)^j\binom dj}{j-r+1}s^j,\\
\mathcal V_p^{(3)}(s)&=
\left[\int_0^s\mathcal B_p(x)\,dx
       +68\kappa\int_0^s x^r h'(x)\,dx\right]_{<3r},\\
X_p(s)&=\mathcal V_p^{(3)}(s)
       -[s^r]\mathcal V_p^{(3)}(s)\,s^rh(s),\\
\mathcal E_p(s)&=\exp X_p(s)\pmod{s^{3r}}.
\end{aligned}
\tag{8}
$$
所有保留的积分分母及阶乘均在 $1,\ldots,3r-1$，因而是单位。准确有
$$
\boxed{\overline{\widetilde\Gamma}=\mathcal E_p\pmod{s^{3r}}.}
\tag{9}
$$

为核对这一延长，R211 的原连接方程为
$$
\mathcal P H_{\rm corr}
=17-\frac{cp(p+1)}4s^{r-1}F^{p-1},
\qquad \mathcal P=4s(1-s)\partial_s+3-5s.
$$
在所需次数 $<3r-1$，其右侧约化仍为
$17(1-\kappa s^{r-1}/h)$。下面第 3 节出现的 $F$ 新系数乘
$s^{r-1}$ 后才从 $s^{4r-2}$ 开始，已在本窗口之外。
R211 的
$$
\mathcal B_p-17\kappa s^{r-1}(1-s)^d\log h
 +C_p s^{r-1}(1-s)^d
$$
仍解同一方程：其误差含 $s^p$，且范围内唯一零对角仍是
$4(r-1)+3=p$。积分到 $<3r$ 后，(6) 中的
$c\,t(F^p-1)$ 正好消掉 $-68\kappa t\log h$。最后用
$[s^r]\log\widetilde\Gamma=0$ 消掉共同标量，得到 (9)。
这里没有把 (8) 积分到次数 $p$，也没有引进全局 theta 原函数。

## 3. 第三权新增的原几何 carry

只在前两权使用 $F\bmod p=h$ 已够；在第三权这样做会漏项。准确地，
$$
\boxed{
\bar F(s)=h(s)+\chi s^{3r-1}\pmod{s^{3r}},
\qquad \chi=\frac2{3\kappa}\in\mathbf F_p^\times .}
\tag{10}
$$
同时
$$
\bar G(s)=(1-s)^d\pmod{s^{3r}}.
\tag{11}
$$

证明：当 $2r\le j<3r-1$，$\binom{2j}{j}$ 恰有一个 $p$ 因子而
$4j+1$ 是单位，所以该系数约化为零。在 $j=3r-1$，
$4j+1=3p$，不能删除同一个分子因子再把系数当零。去掉阶乘里的
$p$ 后，
$$
\chi=-\frac{(2r-1)!}{3\cdot4^{3r-1}((3r-1)!)^2}.
$$
Wilson 配对给
$((2r-1)!)^2=1$、
$(r-1)!(3r-1)!=(-1)^r$，故
$\chi\kappa=2/3$。式 (11) 则是 $G=(1-s)^{-1/2}$ 的原二项式展开；
全部所读次数小于 $p$。$\square$

## 4. 同一整行及准确三权矩阵

对 $n=1,2,3$、$k\ge0$ 定义特征零整行
$$
\boxed{
D_{n,k}=[s^{nr}]
 \widetilde\Gamma(s)\mathbf S(s)
 \frac{G(s)}{F(s)^{n+1}}(\log F(s))^k\in O^3,
\qquad D_n=D_{n,0}.}
\tag{12}
$$
这里所有列、所有 $n,k$ 使用同一 (5)。$\log F$ 只读次数
$<3r<p$，故它本身整。$k\ge nr$ 时行自动为零。

第三列在这个原式中有准确简化：
$$
\boxed{
(D_{n,k})_H=[s^{nr}]
 \widetilde\Gamma(s)\frac{sQ_{15}(s)}{F(s)^{n+1}}
                  (\log F(s))^k.}
\tag{13}
$$
这是 $\sqrt{1-s}\,G=1$ 的特征零等式。没有将第三来源改成一个
没有二次角因子的 theta 函数；相消只发生在本来就存在的参数核里。

令实际原系数行、同一整轴行为
$$
R_n=[w^{nr}](A,B,H),\qquad
V_n=[w^{nr}]e^{-\ell w^r}(A,B,H).
\tag{14}
$$
由第 2 节和 $c-\ell\in O$，$V_n$ 无条件整。准确三角关系为
$$
\begin{pmatrix}R_1\\R_2\\R_3\end{pmatrix}
=
\begin{pmatrix}
1&0&0\\ \ell&1&0\\ \ell^2/2&\ell&1
\end{pmatrix}
\begin{pmatrix}V_1\\V_2\\V_3\end{pmatrix}.
\tag{15}
$$
原 Hurwitz 三行是再左乘
$\operatorname{diag}((p+1)!,(2p+2)!,(3p+3)!)$；所以没有省略原权尺度。

Lagrange 的准确式及 (5) 给
$$
R_j
=\sum_{l=1}^j\frac{\ell^{j-l}}{(j-l)!}
 \sum_{k\ge0}\frac{(-jp)^k}{k!}\,D_{l,k},
\qquad 1\le j\le3.
\tag{16}
$$
全部和在所读次数自动有限。于是实际需要的三个精度为
$$
\boxed{
\begin{aligned}
V_1&\equiv D_1-pD_{1,1}+\frac{p^2}{2}D_{1,2}\pmod{p^3},\\
V_2&\equiv D_2-\alpha D_{1,1}
          -2pD_{2,1}+\frac{3\alpha p}{2}D_{1,2}\pmod{p^2},\\
V_3&\equiv D_3-\alpha D_{2,1}
                  +\frac{\alpha^2}{2}D_{1,2}\pmod p .
\end{aligned}}
\tag{17}
$$
本式中 $D_1$ 读到模 $p^3$，$D_2,D_{1,1}$ 等相应保留显示系数所需的
真正下一位，不能将它们一律替换成模 $p$ 的 (9)。

特别，在实际首行失败后，
$$
\boxed{
\overline{R_1/p}
 =\overline{D_1/p}-\overline{D_{1,1}}.}
\tag{18}
$$
这就是 R213 原除 $p$ 行的同一个移动 log 校正，第三来源并没有令它消失。

## 5. 真实归一行与无显式 log 伴随的准确比较

定义实际归一行
$$
\tau_n=\frac1p\sum_{j=1}^n
 \frac{(-\ell)^{n-j}}{j(n-j)!}R_j,\qquad 1\le n\le3,
\tag{19}
$$
以及整参考的伴随行
$$
\sigma_n=\frac1{pn!}\sum_{l=1}^n
 (-\ell)^{n-l}(l-1)!\,D_l.
\tag{20}
$$
它们本身在未假设有限失败时可能非整；准确说法是
$$
\boxed{\tau_n-\sigma_n\in O^3,\qquad n=1,2,3.}
\tag{21}
$$
并且可以无条件约化这些整差：
$$
\boxed{
\begin{aligned}
\overline{\tau_1-\sigma_1}&=-\overline{D_{1,1}},\\
\overline{\tau_2-\sigma_2}&=-\overline{D_{2,1}}
                         +\frac{\bar\alpha}{2}\overline{D_{1,2}},\\
\overline{\tau_3-\sigma_3}&=-\overline{D_{3,1}}
                         +\frac{\bar\alpha}{2}\overline{D_{2,2}}
                         -\frac{\bar\alpha^2}{6}\overline{D_{1,3}}.
\end{aligned}}
\tag{22}
$$
只有证明 $\sigma_n,\tau_n$ 整后，才可将 (22) 拆成两边各自的模 $p$ 行。

**完整负层消去证明。** 将 (16) 代入 (19)。固定 $l$，令
$m=n-l$。$D_{l,k}$ 的系数为
$$
\frac{\ell^m(-p)^k}{p\,k!}
 \sum_{j=l}^n\frac{(-1)^{n-j}j^{k-1}}{(n-j)!(j-l)!}.
\tag{23}
$$
$k=0$ 时，和为 $(-1)^m(l-1)!/n!$，恰给 (20)。
$1\le k\le m$ 时，和为 $m$ 阶差分作用于低于 $m$ 次的多项式，
准确为零。首个可能非零项为 $k=m+1$，其和为一，系数赋值为零；
以后的项赋值至少一。因为 $k<3r<p$，所有 $k!$ 均是单位。
这先证明 (21)，再给 (22)。这里没有只比较关联次数而漏掉真实负层。$\square$

## 6. 完整中央零、有限聚合及额外一权的准确区别

令 $b=17u_0$ 是 R199/R203 的原 Cartan 指数。
$c-b\in O$，所以 $\delta=b-\ell\in O$。若 $t_n(b)$ 表示 R203
的原有理归一行，则
$$
\begin{pmatrix}\tau_1\\\tau_2\\\tau_3\end{pmatrix}
=
\begin{pmatrix}1&0&0\\ \delta&1&0\\
\delta^2/2&\delta&1\end{pmatrix}
\begin{pmatrix}t_1(b)\\t_2(b)\\t_3(b)\end{pmatrix}.
\tag{24}
$$
这是同一个 $\operatorname{GL}_3(O)$ 行变换。
R244 的第三来源具有同一 charge，故 R203 的共同 Stokes 权和这份行变换
逐列适用；它没有要求三来源是三个自由超越轴。

### 6.1 原全和提供什么

写原完整 Stokes 向量为
$$
\mathscr S=\sum_{n\ge1}\omega_n v_n,\qquad
\omega_1=1,\quad
\omega_n=(-1)^{n-1}(n-1)!b^{1-n}(1+p^{(p-1)/2}O),
$$
这里 $v_n$ 是原 $b$ 规范的中央整轴行。
三条完整中央导数同时为零意味着 $\mathscr S=0$。
原尾界因此给
$$
Q_N=\sum_{n=1}^N\omega_nv_n\in p^NO^3,\qquad N=1,2,3.
\tag{25}
$$
这些是同一个全和的逐精度聚合；它们没有说 $v_2,v_3$ 各自模 $p$ 为零。

在当前 $p\ge19$ 的范围，权的相对误差足以使 (25) 的第三条等价于
R203 的三条有限归一行整。结合 (21)、(24)，得到
$$
\boxed{
Q_3\in p^3O^3
\ \Longleftrightarrow\
\tau_1,\tau_2,\tau_3\in O^3
\ \Longleftrightarrow\
\sigma_1,\sigma_2,\sigma_3\in O^3.}
\tag{26}
$$
式 (26) 是有限前缀测试的等价；没有把它反推为 $\mathscr S=0$。

### 6.2 同一个三权聚合的无显式 log 形式

由 (17)，全部显示的 log 项准确抵消：
$$
\boxed{
V_1-\frac p\alpha V_2+\frac{2p^2}{\alpha^2}V_3
\equiv
D_1-\frac p\alpha D_2+\frac{2p^2}{\alpha^2}D_3
\pmod{p^3O^3}.}
\tag{27}
$$
左侧的 $D_{1,2}$ 系数分别为 $1/2,-3/2,1$；$D_{1,1}$、
$D_{2,1}$ 也成对抵消。这是保留原下一位后的聚合，不是把它们提前删掉。

因此三完整中央零迫使准确的有限必要条件
$$
\boxed{\alpha^2D_1-\alpha pD_2+2p^2D_3\in p^3O^3.}
\tag{28}
$$
由于 $\alpha$ 是单位且 $D_n$ 整，(28) 等价于顺序定义的
$$
\boxed{
D_1\in pO^3,\qquad
E_2:=D_2-\ell D_1\in pO^3,\qquad
E_3:=D_3-\frac\ell2E_2\in pO^3.}
\tag{29}
$$
其中第二式只有在第一式后才单独解释为整行，第三式只有在前两式后
才单独解释为整行。具体地，
$\sigma_1=D_1/p$、$\sigma_2=E_2/(2p)$、$\sigma_3=E_3/(3p)$。

新第三中央权增加的合法约束正是 (29) 的最后一式，或者等价地将
前两权聚合的精度从 $p^2$ 升至 (28) 的 $p^3$。它读取
$D_1\bmod p^3$、$D_2\bmod p^2$、$D_3\bmod p$；
只给三行各自的模 $p$ 值不够。新来源则增加这个同一三向量条件的
第三个坐标；由 (13)，其完整表达为
$$
\begin{aligned}
&\alpha^2[s^r]\frac{\widetilde\Gamma sQ_{15}}{F^2}
-\alpha p[s^{2r}]\frac{\widetilde\Gamma sQ_{15}}{F^3}\\
&\hspace{30mm}
+2p^2[s^{3r}]\frac{\widetilde\Gamma sQ_{15}}{F^4}
\in p^3O.
\end{aligned}
\tag{30}
$$
式 (30) 是实际 $H$ 坐标，没有输入未知调节子；也尚未证明它与旧两坐标
不能同时成立。

### 6.3 三行列式的原尺度

置
$$
\Delta_3=
\det\begin{pmatrix}
H_{A,p+1}&H_{B,p+1}&H_{H,p+1}\\
H_{A,2p+2}&H_{B,2p+2}&H_{H,2p+2}\\
H_{A,3p+3}&H_{B,3p+3}&H_{H,3p+3}
\end{pmatrix}.
$$
准确有
$$
\Delta_3=\prod_{j=1}^3(j(p+1))!\det(V_1,V_2,V_3),\qquad
\det(\tau_1,\tau_2,\tau_3)=
\frac{\det(V_1,V_2,V_3)}{6p^3}.
\tag{31}
$$
阶乘赋值依次为 $1,2,3$，且其除去 $p^j$ 后模 $p$ 依次为
$-1,4,-36$。所以
$$
v_p(\Delta_3)\ge6,\qquad
\Delta_3/p^6\equiv144\det(\bar V_1,\bar V_2,\bar V_3)\pmod p;
\tag{32}
$$
三完整零进一步迫使 $v_p(\Delta_3)\ge9$。
这是 R244 三方向必要条件在前三权上的准确尺度。
若首行已经为零，(32) 的模 $p$ 行列式自动消失；不能把它当成已读取
后续两位的检测器。真正的归一矩阵必须使用 (19)、(22)，尤其不能把
$\det\sigma$ 冒称 $\det\tau$。

## 7. 有限域有理式与准确 Cartier 接口

令
$$
\mathbf B_p(s)=
\bigl(P(s)(1-s)^d,\ Q(s)(1-s)^d,\ sQ_{15}(s)\bigr),\qquad
\mathfrak h(s)=h(s)+\chi s^{3r-1}.
$$
由 (9)—(13)，准确有
$$
\boxed{
\bar D_n=[s^{nr}]\frac{\mathcal E_p(s)\mathbf B_p(s)}
                              {\mathfrak h(s)^{n+1}},
\qquad n=1,2,3.}
\tag{33}
$$
前两行可以把 $\mathfrak h$ 换成 $h$。第三行则必须写成
$$
\boxed{
\bar D_3=
[s^{3r}]\frac{\mathcal E_p\mathbf B_p}{h^4}
-\frac8{3\kappa}(1,1,1).}
\tag{34}
$$
这是 (10) 的单位 carry；三来源首项均为一，所以它位于同一个
$(1,1,1)$ 方向。作 R244 的首角权 $1,2,3$ 列变换后，它只落在
第一列，不能把它数成一个新的独立第三方向。

对 $k\ge1$，$\log F$ 额外至少一阶，故 (10) 的新项不能进入所读系数。
于是
$$
\boxed{
\overline{D_{n,k}}=
[s^{nr}]\frac{\mathcal E_p(s)\mathbf B_p(s)}{h(s)^{n+1}}
                    (\log h(s))^k,\qquad k\ge1.}
\tag{35}
$$
$\log h$ 始终是原点处、只读次数 $<3r<p$ 的形式对数。
它仍可准确分成 $\log(1+s)+\log\widetilde h$；这里没有删掉后者。

(33) 也给一个确切 Cartier 形式。把其右侧有理向量函数记为
$B_n(s)$，在 $\mathbf F_p(u)$ 上取
$$
\eta_n=B_n(u^4)u^{-n-1}\,du.
$$
令 $\mathcal C$ 是标准 Cartier 算子，
$\mathcal C(\sum a_j u^jdu)=\sum a_{pi+p-1}^{1/p}u^idu$。因系数在
$\mathbf F_p$，准确有
$$
\boxed{
\bar D_n=\operatorname{Res}_{u=0}
                 u^{-n}\mathcal C(\eta_n).}
\tag{36}
$$
确实右端读取 $\eta_n$ 的 $u^{np-1}du$ 项，即读取
$B_n(u^4)$ 的 $u^{n(p+1)}=u^{4nr}$ 项。

这里 $\mathcal E_p$ 是 (8) 规定的原有限 jet 的唯一多项式代表。
(36) 是这个明确有理微分的局部系数恒等式；它没有把该多项式在
$h$ 的其他根处的值认定为原 theta 的全局值。若要利用其他点的留数
或 Cartier 全局迹推出非零，仍须证明它们确实控制 (28) 所需的原
下一位，而非只控制裸核。

## 8. 新输入的确切范围

第三来源在 (13)、(30) 中给出了原先没有的固定多项式核，并使其
模 $p$ Cartier 读取不再显式含 $G$。完整三权聚合 (27) 也已把
移动 log 放在可逐项核对的位置：在有限整性测试中它们抵消，
在真实归一矩阵 (22) 中仍存在，尤其首行除 $p$ 后不能省略它们。

这些结论尚未给 (28) 的一个必定非零坐标。R245 的单个对数分量
在原二阶连接聚合中升一阶，与本篇保留下一位的处理一致；
不能将那个分量的单位性代入 (34)，也不能用 (34) 的共同方向
单位代替整个 (29) 的 $E_3$ 行。所需后继输入现已明确为：
同一固定原 theta 的 $D_1,D_2$ 真正下一位与上述固定 $H$ 多项式核
之间的一条新关系，或 (30) 的实际非零定理。

依赖：R197 的原 $P,Q$ 和整 gauge；R199/R203 的真实第一带、
完整 Stokes 尾界与有限目标格；R211/R213 的原连接与下一位；
R215 的原椭圆参数整性；R243 的实际第三截面；R244 的同一 charge
三方向；R245 的完整连接聚合。无目标素数扫描。

