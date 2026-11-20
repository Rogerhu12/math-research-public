# R932 — 同源尾调整的完整 normal 响应与实际单位联动

日期：2026-11-20。**状态：下述同源相干提升、全部normal响应、联合尾逆及单位联动均已证明；root/theta全文独审。未执行数学计算，未判固定forcing非零。**

本注继续 R930 已给的同一原来源联合尾右逆，计算它随同带来的整个 normal 向量。所用轴始终是原实际 g；实际除 p 根修正保留。这里不使用 R929 从 t^p 才开始的新 Frobenius 块。事实上，这一族的全部读数只需原 m=0 轴的严格 <s 前缀。

固定 P、R、S 的任何其它部分不在本注中重选。新的向量只是 R930 那些原首核方向的合法整提升；不将它们认作 K′，不把下述 normal 系数冒充杀整个原首像的左行。

## 1. 同一族的相干整提升确实留在原格

沿用 R930(1)–(9) 的同一个原矩阵、完整 WD 和实际 quartic 来源：

$$
p=6s-1>211,\qquad T=s-13,\qquad
\bar P=t^{r_{\rm src}}F^4q,\qquad
\tau=r_{\rm src}+2h-s\ge0.
\tag{1}
$$

原 P134、十九角、共同 charge 四十、原公共单位以及完整 w^13 前缀全部保留。设

$$
1\le m\le13,\qquad m\le h,\qquad
\sigma_t(P)\ge\tau+m,\qquad
\ell\le s-h-m .
\tag{2}
$$

每个方向都是已经由 R930 认证的原完整首核：

$$
Y_j=t^{-(\tau+j)}\bar P=t^{r_j}F^4q,\qquad
r_j=s-2h-j,\qquad1\le j\le m.
\tag{3}
$$

这里 r_j≥0 不是额外未付的假设。F(0,Y)、q(0,Y) 都非零，故其乘积在 k[Y] 中非零，而 P 的各 Y 系数的最小 t 阶恰为 r_src。原 A_n≥0，所以 sigma_t(P)≤r_src；由 (2) 得 r_m≥0，其余 r_j 更大。

**引理 1（同时保帽的同一 factor lift）。** 可选同一组 F̃、q̃，使

$$
\widetilde Y_j=t^{r_j}\widetilde F^{\,4}\widetilde q
\in\mathcal W_D,\qquad
\widetilde Y_j\bmod p=Y_j,\qquad
\widetilde Y_j=t^{m-j}\widetilde Y_m .
\tag{4}
$$

证明使用 R491，不靠任意系数提升。先严核清分母：R930 的 F、q 只允许原固定 d=1+8t 分母，不先假设 d^{C_D}q 已是多项式。取整数 a0，使

$$
F_0=d^{a_0}F\in k[t,Y],\qquad
\min_n\operatorname{ord}_d([Y^n]F_0)=0,\qquad
q_0=d^{-4a_0}q .
$$

于是 d^{C_D}Y_j=t^{r_j}F_0^4Q_0，其中 Q_0=d^{C_D}q_0。左边在 k[t,Y]，且普通 d-Gauss 赋值对乘积可加、对 t 和 F_0 都取零，所以 Q_0 的每个系数在 d 处整。它没有其它分母，故 Q_0∈k[t,Y]。这才得到 R491 所需的真正多项式因子分解。

对 F_0、Q_0 分别作 R491 引理 1 的同一提升，逐 Y 系数保持全部固定角点的整除阶、t 次数及 Y 次数。每个 Gauss 赋值对非零乘积严格相加，所以对每个 j，t^{r_j}F̃_0⁴Q̃_0 的全部赋值恰等于其约化的值。这些约化已在清分母的原格，故 R491 定理 2 的每一个角条件和无穷帽同时保留。除回同一个 d^{C_D} 后，再定义

$$
\widetilde F=d^{-a_0}\widetilde F_0,\qquad
\widetilde q=d^{4a_0-C_D}\widetilde Q_0 .
$$

所得仍是原 F、q 在原 d 分母系数环内的提升，并且 t^{r_j}F̃⁴q̃=d^{-C_D}t^{r_j}F̃_0⁴Q̃_0，给出 (4)。正文 u、e、xi 均由恢复后的原 F̃ 定义，未改原规范。没有从单独一个 j 的可提升性猜其它 j；相同因子赋值给全部 j 分别的准确成员性。证毕。

原固定整 P 不必等于 t^{r_src}F̃⁴q̃，本注也不替换它。(4) 只选择新增调整方向的原整代表。

若将 (4) 换成任意别的原整提升，完整首商代表会增加原 Mbar 的像。以下给的是这一已付相干 factor lift 的实际代表；其余提升必须连同这项原像一起记账。

## 2. 系数定义：完整 Euler 作用及实际根修正

在原所需整窗口内，令

$$
f(w)=\widetilde F(t(w),g(w))
     =w^h u(w)+p\,\xi(w),\qquad
\xi(w)=\frac{[f(w)]_{<h}}p .
\tag{5}
$$

因此 xi 是实际低阶前缀除 p 后的多项式，次数 <h；u=(f-p xi)/w^h。约化后 u(0)≠0。不得先令 xi 为零，亦不得给它另选高轴数字。

令 E=Y∂Y，且

$$
e_k(w)=(E^k\widetilde F)(t(w),g(w)),\qquad e=e_1,
\tag{6}
$$

$$
C_{j,k}(w)=
\mathcal U^{\rm act}(w)
\left(\frac{t(w)}w\right)^{r_j}
\big((E+40)^k\widetilde q\big)(t(w),g(w)),
\qquad C_j=C_{j,0}.
\tag{7}
$$

这里 U^act=c_*U0^act 正是 R928(16) 的同一个原单位。式 (7) 的四十来自完整公共框 G0；t 和 t/w 的 Euler 导数为零。并未把对 q 的 Euler 导数省掉，也未把整个 C_j 当作 charge 零常数。C_{j,k} 就是对该完整系数作第 k 次总 Euler 后的实际评价。

由 (4)，相同 j 的原实际矩满足

$$
\begin{aligned}
W_0(\widetilde Y_j)/w^{r_j}
 &=C_j f^4,\\
W_1(\widetilde Y_j)/w^{r_j}
 &=4C_j f^3e+C_{j,1}f^4,\\
W_2(\widetilde Y_j)/w^{r_j}
 &=12C_j f^2e^2+(4C_je_2+8C_{j,1}e)f^3+C_{j,2}f^4,\\
W_3(\widetilde Y_j)/w^{r_j}
 &=24C_jfe^3+(36C_jee_2+36C_{j,1}e^2)f^2\\
 &\quad +(4C_je_3+12C_{j,1}e_2+12C_{j,2}e)f^3
       +C_{j,3}f^4 .
\end{aligned}
\tag{8}
$$

这些是 R824(15) 的同一完整乘积法则，现不只读其最低一行。它们属于实际 W_i，故 R928(6) 已合并的 H·B 低项未被删除。

以下 a、u、xi、e_k、C_{j,k} 全按 (5)–(7) 先在整窗口内定义，再约化到原 k。只有 xi 使用一次真正的除 p。所有级数仅表示第 6 节逐项核算的有限前缀；没有把尚未证明全局整性的无穷 sigma 级数直接约化到 k[[w]]。

## 3. 全部四块首商的显式代表

写

$$
V_j=\frac{M\widetilde Y_j}{p}\bmod p
   =V_{j,0}+\epsilon V_{j,1}
      +\epsilon^2V_{j,2}+\epsilon^3V_{j,3}.
\tag{9}
$$

前三个分量取完整物理长度 s，末分量取长度 ell+13。R930 已付 M Ỹ_j∈pΓ，所以这个原整商存在。

**定理 2（完整响应）。** 在 (1)–(7) 下，恰有

$$
\boxed{V_{j,0}=0,}
\tag{10}
$$

$$
\boxed{
V_{j,1}=
\left[w^{13+2h-j}C_j u^4\right]_{<s},
}
\tag{11}
$$

$$
\boxed{
\begin{aligned}
V_{j,2}=\big[
 &12a^2w^{13+r_j+h}C_j u\xi e^2
 +4a w^{13+h-j}C_j u^3e\\
 &+a w^{13+2h-j}C_{j,1}u^4
\big]_{<s},
\end{aligned}}
\tag{12}
$$

$$
\boxed{
\begin{aligned}
V_{j,3}=\big[
 &4a^3w^{13+r_j}C_j\xi e^3
 +6a^2w^{13-j}C_j u^2e^2\\
 &+\frac{a^2}{2}w^{13+h-j}
      (4C_je_2+8C_{j,1}e)u^3\\
 &+\frac{a^2}{2}w^{13+2h-j}C_{j,2}u^4
\big]_{<\ell+13}.
\end{aligned}}
\tag{13}
$$

所有显示指数非负，最小的 13−j 也由 j≤13 支付。式 (13) 同时包含原末十三 carry 带和全部短 normal，不需要先把某条尾响应当作独立坐标删除。

### 3.1 整除前缀与完整折回证明

将 f=w^h u+p xi 代入 (8)。相对 normal 窗口是 <T、<T、<T、<ell。没有 p 的项已经由 Y_j∈K1 消失；除 p 后只有一次 xi 项可能留下。

W0 的一次 xi 项从 r_j+3h=s+h−j≥s 起；W1 的一次 xi 项从 r_j+2h=s−j≥T 起。因此前两个 normal 直读商均为零。W2 的唯一可能低项是

$$
\left[W_2(\widetilde Y_j)/p\right]_{<T}
 =\left[24w^{r_j+h}C_j u\xi e^2\right]_{<T}\pmod p.
\tag{14}
$$

其余一次 xi 项从 r_j+2h≥T 起。W3 中除首项外的所有一次 xi 项从 r_j+h≥ell 起，所以

$$
\left[W_3(\widetilde Y_j)/p\right]_{<\ell}
 =\left[24w^{r_j}C_j\xi e^3\right]_{<\ell}\pmod p.
\tag{15}
$$

这里 r_j+h≥ell 对所有 j 由 (2) 最严的 j=m 门支付。

R928(11) 的实际 normal 行除 p、模 p 后，准确只剩

$$
\frac{a^i}{i!}
\left[W_i(\widetilde Y_j)/p\right]
+\frac{a^{i-1}}{(i-1)!}\mathscr S\,\bar W_{i-1}(Y_j)
\quad(i\ge1),
\tag{16}
$$

第零行只留首项。d≥2 的 p^d 折回项此时才消失。将 (8) 的约化代入真实 s 阶移位，再乘完整 w^13，给 (10)–(13)。第一、第二 carry 带为零；第三 carry 恰是 (13) 中 w^{13-j} 项的前 j 个系数。证毕。

### 3.2 只取 normal 时，必须保真实尾移位

对任意 H∈k[[w]] 定义

$$
\mathscr S_j H=\frac{H-[H]_{<j}}{w^j}.
\tag{17}
$$

因此末短 normal 的完整相对响应是

$$
\begin{aligned}
[w^{-13}V_{j,3}]_{\rm normal}
=\big[
 &4a^3w^{r_j}C_j\xi e^3
 +6a^2\mathscr S_j(C_j u^2e^2)\\
 &+\frac{a^2}{2}w^{h-j}(4C_je_2+8C_{j,1}e)u^3
 +\frac{a^2}{2}w^{2h-j}C_{j,2}u^4
\big]_{<\ell}.
\end{aligned}
\tag{18}
$$

左边只表示取 V_{j,3} 的第 13,...,13+ell−1 系数，移回零起点；不是把整个含前十三行的 V_{j,3} 直接除 w^13 后当幂级数。

用 w^(−j)H 代替 S_j H 会把已经独立占据 carry 带的前 j 项错误放回 normal。另一方面，删去 C_{j,1}、C_{j,2} 也一般改变完整 normal 尾；R824 的较短最低项窗口不能支持这种删除。

## 4. 原联合尾右逆的直接公式及全部 normal 回传

相干性给一个原目标中的整恒等式：

$$
M\widetilde Y_j=t(w)^{m-j}M\widetilde Y_m.
$$

所以在整个约化目标中，

$$
\boxed{V_j=\bar t(w)^{m-j}V_m.}
\tag{19}
$$

这只对 (4) 这组已经付清来源帽的实际方向使用 t 乘法；不声称整个原来源格或原 Mbar 的像都对 t 稳定。

记

$$
H_m(w)=C_m(w)u(w)^2e(w)^2\bmod w^{\ell+m},\qquad
K_m(w)=6a^2H_m(w)\in(k[w]/w^{\ell+m})^\times.
\tag{20}
$$

将任意指定的末 m 个物理 carry 值写成

$$
b(w)=b_0+b_1w+\cdots+b_{m-1}w^{m-1},
\tag{21}
$$

对应 epsilon³ 的 w^(13−m),...,w^12 行。令 w=w(t) 是同一个原 t(w) 的逆，定义次数 <m 的真实多项式

$$
\boxed{
A_b(t)=
\left[\frac{b(w(t))}{K_m(w(t))}\right]_{<t^m}.
}
\tag{22}
$$

则

$$
[A_b(t(w))K_m(w)]_{<m}=b(w).
\tag{23}
$$

若 A_b(t)=sum_(k=0)^(m−1) a_k t^k，所用来源是同一个组合

$$
Y_b=\sum_{k=0}^{m-1}a_kY_{m-k}.
\tag{24}
$$

其尾值恰为 (21)，且完整首商代表是

$$
\boxed{V_b=A_b(t(w))V_m\quad\hbox{于完整原 }\bar\Gamma.}
\tag{25}
$$

这里同时乘回 (10)–(13) 的每个分量，并按原各块长度截断。式 (22) 是 R930 实际三角逆的直接系数公式；没有用三个独立的任意修正，也没有只按矩阵对角逆掉首项。

特别，乘 A_b 后 carry 带中的较低行可能进入 normal 行；(25) 全部保留这种卷积。若需要只列最后一块 normal，将 (18) 中的 S_m(H_m) 替为 S_m(A_b(t(w))H_m)，其余项乘同一个 A_b(t(w))，便是完整答案。

## 5. 一个实际不可删的 normal 单位首项

完整公式还付出一条不含 xi 的实际单位关系。

**命题 3。** 若 b≠0，令 v=min{k:b_k≠0}。则 (25) 的第二 normal 块，即 epsilon² 的相对窗口 <T，恰有

$$
\boxed{
w^{-13}(V_b)_2
=\frac{2u_0}{3ae_0}\,b_v\,w^{h-m+v}
 +O(w^{h-m+v+1}),
}
\tag{26}
$$

而且该首项确实位于原已读 normal 窗口内。

证明：由 (22)–(23)，A_b(t(w)) 的首项是
b_v w^v/(6a²C_m(0)u0²e0²)。
式 (12) 的中项从 h−m 起，系数 4aC_m(0)u0³e0 为单位；首项从 r_m+h 起，比它晚 r_m+m=s−2h≥m≥1；末项又晚 h≥1。因此 (26) 的系数比准确为 2u0/(3ae0)。

由 r_m≥0 得 2h+m≤s，而 s>35。于是
h−m+v≤h−1<s−13=T，首项未落在未知尾。证毕。

这条关系在所有保持同一分解的合法 factor lifts 之间不变，因为其余提升数字只改变 (12) 中更高的 xi 项。它说明：在这组真实相干调整中，任意非零尾目标都会伴随一个明确的 normal 单位响应，无法把尾调整当作不碰 normal 的自由直和。

但是 (26) 是对实际向量代表的读数，不是 C1 的一个已经下降的左配对。换成一般原整提升会增加 Mbar 的像；对同一个普通行消元也可能改变其代表值。本注没有因此推出全原 p³ 或 p⁴ 不可解。

## 6. 所用实际轴只到 m=0：完整精度核算

上述公式中，除 p 数据只在 (5) 的 f_<h/p。它需要原 g、t 的 <h 前缀模 p²，以及 F̃ 的同一整系数提升。所有其余评价只用模 p：

- (11) 的 u 项最高需要 f 的次数 <T−h+j≤s；
- (12) 的移位主项最高需要 f 的次数 <T+j≤s，xi 项需要 <2h+j−13<s；
- (13) 的 F² 移位项最高需要 f 的次数 <h+ell+j≤s；
- (13) 其它项需要的 f、q、Euler 系数前缀更短；(22) 只用前 m 项。

这些“<”均是实际半开窗口。取 t(w) 到 w^s（为 t/w 另保一项）、原 g 到严格 <s，便覆盖每一个输出系数；无需补未知系数为零。原 P134、q 和共同单位仍以完整表达式作这些前缀评价。

在 R868/R929 同一个共同 E1 坐标里，可以直接使用原精确式

$$
r_n=\frac{(1/3)_n}{(5/6)_n},\qquad
\mathcal F(t)=
\sum_{n=0}^{s-1}\frac{(1/2)_n}{n!(6n+1)}t^n,
\qquad
w(t)=-t\mathcal F(t)^6\pmod{t^{s+1}},
\tag{27}
$$

$$
\boxed{
g(t)\equiv
(1+8t)\exp\!\left(
\frac{17}{3}\sum_{n=1}^{s-1}\frac{r_n}{n}t^n
\right)\pmod{t^s}.
}
\tag{28}
$$

原 Gaussian 指数从 t^s 开始，所以不进入 (28)。当 n<s 时，r_n 的所有分母、n、n!、(6n+1) 都是 p 单位；截断指数中所用阶乘的指标也 <s<p。实际 t(w) 的首项为单位，因此有限整反演仍可直接模 p² 作。这一有限读法没有指数造成的隐藏 p 精度损失，也没有另选 Gaussian 或 theta 轴。

回物理原模型时仍用 R821/R868 的原固定单位缩放；不得换一个 b 或重新选常数嵌入。式 (27)–(28) 只说明所需原输入已由旧 m=0 有限式完全支付。R929 的 m≥1 两位块从 t^p 才开始，本注既不读取它们，也不称它们给当前三 carry 增加新的 forcing。

## 7. 对同一个固定 P、R、S 的准确使用

若原 X=P+pR+p²S 已满足 MX∈p³Γ，将 MX/p³ 的指定末 m 个 carry 写成 b。使用 (22) 的 A_(−b) 并令

$$
S'=S+\widetilde A_{-b}(t)\widetilde Y_m
\tag{29}
$$

仍保持完整 p³，且第三页全部变化准确是 A_(−b)(t(w))V_m，不只三条尾标量。于是剩余 normal 检验具有已算出的完整向量右端；它的第二 normal 首响应由 (26) 给出负号版本。

这步的合法性仍须 (29) 的整个整组合可选在给定 S 差格内。只知道约化属于一个较大的环境格，不足以支付受限 S 的整提升。若差格更小，必须先完成其实际成员性；不能从 Y_j∈WD 自动推断。

若只已知 M(P+pR)∈p²Γ，相同公式适用于较早的 R 调整及第二页。不得把这些 beta1 非零的方向用于两个完整 p³ 解之间任意改变 R；R920 附 A 所需的完整 K′ 条件仍不变。

本注付清的是 R930 留下的这组实际方向的完整 normal 响应、真实相干 lift、显式联合逆及一个确定单位联动。R928 的固定全局类是否非零、是否存在杀整个原来源的可延拓 GRes 左行、以及其余受限 S normal 联立式，仍须在同一个原对象上继续判断。

依赖：R491 同预算因子提升；R824(15) 全 Euler 乘积式；R868 原 t 松弛；R928(6)、(11)、(16) 实际矩及全部折回；R930 原同源尾右逆；R828/R929 已登记的原 m=0 超几何及坐标公式。没有数学数值执行或有限样本外推。

原入口：[R930](R930-original-quartic-native-tail-joint-right-inverse.md)、[R928](R928-original-fixed-P-affine-long-jets-and-global-compatibility.md)、[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)。
