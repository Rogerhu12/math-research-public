# R453：一次整返回后的两来源次数二连接与完整全局预算

日期：2026-11-14。**状态：已证明。** 将真实 \(T\) 中的固定 \(V\) 因子移入角多项式空间后，整个原来源嵌入一个明确的计算格。该格对原次数二连接闭合，并能用一个固定、\(p\)-饱和的来源乘法一次返回原 \(T^j\) 格。\(J\le16\) 时返回成本至多三十六个相对径向次数、九个物理行和十八条 carry；反复 \(k\) 次连接的源次数由 \(D+3k\) 改为 \(D+2k+36\)。原全部 \(P_{134}/U_0\)、首次提升、两条完整中央基准均保留。随后核算表明，这项固定返回和连接系数改进本身仍不改变 R418 的严格全局门槛，也没有付出原两中央零对全部多项式来源的传播。

## 1. 真实计算截面与包含整个原来源的角空间

采用共同 \(E_1\)、\(p=6s-1>83\)、\(\alpha=36/17\)，并保留

\[
d=1+8t,\quad h_7=16t^2+4t+7,\quad
a_{\rm ang}=t(t-1)h_7,\quad f=d a_{\rm ang}/7,
\]

以及 R403 的原 \(V\)、\(\mathscr R=\Theta^{17}d\)、
\(S=\Theta^{17}f\)、\(T=\Theta^{36}fV\)。定义

\[
\boxed{T_0=T/V=\Theta^{36}f.}
\tag{1}
\]

这是一个真实全纯 degree72 截面：\(\Theta^{36}=\sigma^{72}x^{36}\)，而 \(f(-x^{-3})\) 的最低 \(x\) 指数为 \(-15\)，故乘回后只是 \(\sigma^{72}\) 乘一个最高 \(x\) 次数三十三的多项式。全部格点的可能极均由 sigma 零支付，原点首项仍为 \(z^6\)。这里没有给 \(T_0\) 新增 rank-two 身份或中央零。

沿 R406 记

\[
q_n=(t h_7)^{A_n}(t-1)^{B_n}d^{-C_n},\quad
A_n=\lfloor(n+1)/4\rfloor,
\quad B_n=\lfloor(n+1)/3\rfloor,
\quad C_n=\lfloor n/2\rfloor,
\]

\[
e_m=3\lceil3m/4\rceil+2\lceil m/2\rceil+
\lceil2m/3\rceil-2.
\]

对固定 \(0\le J\le16\)，定义计算格

\[
\boxed{
\widetilde{\mathcal W}_{D,J}
=\bigoplus_{n=0}^D\bigoplus_{j=0}^J
\mathscr R^nq_n\mathcal O[t]_{\le e_{n+1}+6j}T_0^j.
}
\tag{2}
\]

额外的 \(6j\) 不是免费角列；第 2 节给它们一次返回原来源的完整成本。整个旧来源有实际嵌入

\[
\boxed{
\iota:\mathcal W_{D,J}\hookrightarrow
\widetilde{\mathcal W}_{D,J},\qquad
P(t)T^j\longmapsto P(t)V(t)^jT_0^j.
}
\tag{3}
\]

这在函数上就是同一列，且模 \(p\) 单射、来源像 \(p\)-饱和。原因是 \(\deg V=6\)，其首系数为 \(-2048\)，在当前范围为单位；每一独立部分上只是多项式乘法 \(P\mapsto V^jP\)。特别，原 \(S\)、原 \(T=VT_0\) 均保留为 (2) 内的真实来源，未把后者改成 \(T_0\)。

## 2. 一次固定的 p-饱和返回

令

\[
m=\lceil6J/47\rceil,\qquad c=12m,\qquad r=3m.
\]

\(J=0\) 时取 \(m=c=r=0\)。对全部 \(n\ge0\)，准确有

\[
\frac{q_{n+12m}}{q_n}
=(t h_7)^{3m}(t-1)^{4m}d^{-6m}=:Q_m(t),
\qquad e_{n+12m+1}-e_{n+1}=47m.
\tag{4}
\]

定义固定乘子

\[
\boxed{C_J=\mathscr R^{12m}Q_m(t)V(t)^J.}
\tag{5}
\]

**定理 1。** 对全部 \(D\)，(5) 给同一个原函数域中的实际 \(p\)-饱和来源嵌入

\[
\boxed{C_J:
\widetilde{\mathcal W}_{D,J}\hookrightarrow
\mathcal W_{D+12m,J}.}
\tag{6}
\]

**证明。** 第 \((n,j)\) 部分的像准确为

\[
\mathscr R^{n+12m}q_{n+12m}
\{P(t)V^{J-j}\}T^j.
\]

允许的角次数满足

\[
\deg(PV^{J-j})\le e_{n+1}+6j+6(J-j)
=e_{n+1}+6J\le e_{n+12m+1}.
\tag{7}
\]

没有逐轮重新乘 \(V\)。每个部分的多项式乘子 \(V^{J-j}\) 具有单位首系数，因此其有限自由模像 \(p\)-饱和；不同 \((n,j)\) 在后述实际 Kummer 分解中独立。这证明整个 (6)。\(\square\)

\(1\le J\le7\) 时 \(m=1\)，\(8\le J\le15\) 时 \(m=2\)，\(J=16\) 时 \(m=3\)。因此

\[
\boxed{c\le36,\qquad r\le9.}
\tag{8}
\]

物理原点处的完整乘子为

\[
\boxed{C_{J,\rm phys}=(-7)^{3m}w^{3m}U_C,
\qquad U_C(0,0)=1,}
\tag{9}
\]

其中 \(U_C\) 含整个 \(e_2(12ma\epsilon)\)、角因子和实际高项。它是目标中的整单位，不能只保其常数。

## 3. 全部原角极已付的次数二连接

保持 \(\mathscr R\) 不动的 \(\delta=t\partial_t\) 在 (1) 上准确为

\[
\boxed{\delta T_0=L_0(t)T_0,\qquad
L_0=1+\frac{t}{t-1}+\frac{t h_7'}{h_7}
-\frac{152t}{17d}.}
\tag{10}
\]

原 \(tV'/V\) 项确实不在 (10) 中；原 \(T^j\) 的那份 \(V^j\) 已完整移入 (3) 的角多项式。固定乘子取 R351/R352 的同一个

\[
\chi=(t-1)d h_7,\qquad
W_2=\mathscr R^2a_{\rm ang}\chi
=\mathscr R^2t(t-1)^2d h_7^2,
\qquad \mathcal Q_2=W_2\delta.
\tag{11}
\]

**定理 2。** 在 (2) 的完整计算格上，

\[
\boxed{W_2\widetilde{\mathcal W}_{D,J}
\subset\widetilde{\mathcal W}_{D+2,J},\qquad
\mathcal Q_2\widetilde{\mathcal W}_{D,J}
\subset\widetilde{\mathcal W}_{D+2,J}.}
\tag{12}
\]

**证明。** 对 \(\Phi=\mathscr R^nq_nt^kT_0^j\)，令
\(\Delta A=A_{n+2}-A_n\in\{0,1\}\)、
\(\Delta B=B_{n+2}-B_n\in\{0,1\}\)，且
\(C_{n+2}-C_n=1\)。\(\mathcal Q_2\Phi\) 是
\(\mathscr R^{n+2}q_{n+2}T_0^j\) 乘完整多项式

\[
\begin{aligned}
&t^{k+1-\Delta A}(t-1)^{2-\Delta B}
h_7^{2-\Delta A}d^2\\
&\quad\cdot\left[
k+A_n+j+(A_n+j)\frac{t h_7'}{h_7}
+(B_n+j)\frac{t}{t-1}
+8\{-C_n+j(1-\alpha)\}\frac{t}{d}\right].
\end{aligned}
\tag{13}
\]

所有分母均有真实因子支付。其次数至多
\(k+9-3\Delta A-\Delta B\)，而准确有

\[
\boxed{e_{n+3}-e_{n+1}=10-3\Delta A-\Delta B.}
\tag{14}
\]

因此即使 \(k=e_{n+1}+6j\)，仍比下一允许角上界少至少一。只乘 \(W_2\) 是 (13) 去掉方括号，也满足同一界。

这里的全部十二个剩余类为

\[
\begin{array}{c|rrrrrrrrrrrr}
n\bmod12&0&1&2&3&4&5&6&7&8&9&10&11\\\hline
\Delta A&0&1&1&0&0&1&1&0&0&1&1&0\\
\Delta B&1&1&0&1&1&0&1&1&0&1&1&0\\
\Delta e&9&6&7&9&9&7&6&9&10&6&6&10
\end{array}
\tag{15}
\]

每一类的角余量都是一，周期由 \(e_{n+13}-e_{n+1}=47\) 保持。\(\square\)

## 4. 实际常量域、有限自由与来源饱和

新的变量仍满足同一个十七阶类型的真实关系

\[
\boxed{T_0^{17}d^{19}
=\mathscr R^{36}(a_{\rm ang}/7)^{17}.}
\tag{16}
\]

在 \(K(\mathscr R,t)\) 的 \(\mathscr R\) 赋值上，右侧的阶为三十六，与十七互素，所以该扩张的次数恰为十七；好特征同样成立。以 \(\Theta\) 为坐标，它在固定 \(\mathscr R\) 后准确是

\[
t=(\mathscr R\Theta^{-17}-1)/8,\qquad
T_0=(\mathscr R/7)\Theta^{19}a_{\rm ang}(t),
\]

即有理函数域 \(K(\mathscr R)(\Theta)\)。特征零的 \(\delta\) 常量域是 \(K(\mathscr R)\)；特征 \(p\) 的常量域是 \(k(\mathscr R)(\Theta^p)\)，不能换成未经说明的 \(k(\mathscr R)^p\)。

第 \(j\) 部分的所有 Laurent 指数模十七同余于 \(2j\)，\(0\le j\le16\) 时彼此不同；这证明 (2) 在整模型和模 \(p\) 后均保持显示的有限自由基。

令 \(f_n=\deg q_n+e_{n+1}=\lfloor9n/2\rfloor+4\)。由于 (2) 的额外 \(6j\)，其完整 Laurent 指数范围仍是

\[
-17f_n-151j\ \le M\le\ 17C_n+19j.
\tag{17}
\]

其中 \(151=49+17\cdot6\)；没有因移掉 \(V\) 而误删已加回角空间的成本。

若

\[
\boxed{p>\max\{17f_D+151J,\ 17C_D+19J\},}
\tag{18}
\]

非零 Laurent 指数不能是 \(p\) 的倍数。因此 \(\delta\) 的核只能是 \(\Theta\) 常数；不同的 \(j\) 剩余类使其只来自 \(j=0\)。此时 \(\mathscr R,t\) 独立，逐 \(n\) 得 \(q_nP(t)\) 必为常数；\(n\ge2\) 的 \(t=1\) 零排除该常数，而 \(q_0=q_1=1\)。所以在特征零和 (18) 的好特征下均准确有

\[
\ker\mathcal Q_2=\mathcal O\cdot1\oplus
\mathcal O\cdot\mathscr R\qquad(D\ge1).
\tag{19}
\]

源、目标均为显示的有限自由整格；两种特征的秩相同，故

\[
\widetilde{\mathcal W}_{D,J}/\langle1,\mathscr R\rangle
\xrightarrow{\mathcal Q_2}
\widetilde{\mathcal W}_{D+2,J}
\]

的来源像 \(p\)-饱和。若 (18) 对所经最大次数成立，\(\mathcal Q_2^k\) 也只有首次的同一个核：一次作用后各 \(n\) 已增加二，不会再落入次数零、一的常量核。因此其来源像同样 \(p\)-饱和。这些结论均不预付物理评价 \(J\) 的像饱和或相对 \(p^2\) 缺陷消失。

在同一范围，若 \(D\ge1,k\ge1\)，实际返回算子 \(C_J\mathcal Q_2^k\iota\) 的核仍为 \(\langle1,\mathscr R\rangle\)，来源像也 \(p\)-饱和。原非零真第二核不可能落在这两个常数方向，因为其两个真实低径向行已经把它们分开。所以这种来源操作保持该向量的 primitive 性；它并不自动保持核资格，后者仍须由 (20)–(22) 的实际连接核定。

## 5. 原全部物理连接与一次返回后的真实提升

物理 \(T_0\) 的 Gaussian 仍为 \(\alpha a\)，因为 \(V(t)\) 只有角向部分。相对 Euler 在 (2) 的列上仍为 \(n+\alpha j\)。置原

\[
\nu=(1-t)^{-1/2}/h(t),\quad
\Lambda=(w\partial_wg)/g+sa\epsilon,
\quad B_2=W_{2,\rm phys}\nu=-49w\cdot U_2,
\quad U_2(0,0)=1.
\]

R351 的完整链式法则逐列给

\[
\boxed{\widetilde M_+\mathcal Q_2
=B_2(w\partial_w-13)\widetilde M_-
-B_2\Lambda\widetilde M_-\mathcal E_{\rm rel}.}
\tag{20}
\]

恢复 \(c_*U_0\) 后，第一个算子准确为
\(w\partial_w-13-(w\partial_wU_0)/U_0\)。原 zeta 版本也保持：令

\[
c(t)=-(17+112t)/(3d),\quad
\mathcal D_{\zeta,2}=\mathcal Q_2+W_2c(t)\mathcal E_{\rm rel},
\]

则 \(W_2c(t)\) 的全部角分母已由 (13) 同样支付，且

\[
\widetilde M_+\mathcal D_{\zeta,2}
=B_2(w\partial_w-13)\widetilde M_-
+\frac{17}{3}W_{2,\rm phys}\frac{x\zeta}{y}
                   \widetilde M_-\mathcal E_{\rm rel}.
\tag{21}
\]

整个公共载体按 (20) 的说明恢复，不能只读取其中一个裸有理项。

定义新计算格的矩阵时仍用原 \(c_*U_0m_{13}\)，不改变 \(P_{134}\)。由实际来源恒等式，(3)、(6) 给精确交换图

\[
\boxed{\widetilde M\,\iota=M_{\rm old},\qquad
M_{\rm old,D+c,L+r}\,C_J
=\mu_{C_{J,\rm phys}}\,\widetilde M_{D,L}.}
\tag{22}
\]

只要 \(L+13+r<3s\)，(22) 在整个原三块整目标、尤其模 \(p^3\) 准确成立。\(\mu_C\) 是乘完整 (9)，而不是先将 \(w^r\) 除掉。

所以原真 \(P_2\) 经 \(\iota\) 仍为同一物理第二核，且来源 primitive 性保持；原返回后较大来源的真实整左核，经 \(\mu_C^*\) 拉回，是计算格的真实整左核。首 Bockstein 及第二次提升按这两个真正整映射自然运输，始终商掉完整首次提升像。不能反过来声称每个新左核都免费返回，或所有非零对偶在拉回后仍非零。

若比较同一个 \(A_0\) 的第三精度，返回列的总 charge 是 \(n+40+c+\alpha j\)。所以其完整低轴差为
\(p^2A_0\bar C_J\bar{\widetilde M}(\mathcal E_{\rm tot}+c)P\)。这包含返回乘子本身的 \(cA_0\)；只有在已知 \(\bar{\widetilde M}P=0\) 后才能消去该项。由此与 R403、R449 的 \(\beta_J,d_2\) 运输一致，没有把固定返回的 Gaussian 或第一次提升藏在记号里。

在完整目标 \(\Gamma_{T_0}\to\Gamma_{T_0+r}\) 上，乘 (9) 的非零 Smith 因子准确是

\[
T_0-2r\text{ 个单位},\qquad 2r\text{ 个 }p,
\tag{23}
\]

并多出 \(r\) 个目标自由行。两个长度 \(r\) 的 carry 带均保留；\(r\le9\) 给最多十八个 \(p\)。原 \(m_{13}\) 的二十六条 carry 也仍在，不能以 (23) 替代它们。

若把 (20) 全部写到返回后的来源 \(C_JP\) 上，还须同步作

\[
\mathcal E_{\rm rel}(C_JP)
=C_J(\mathcal E_{\rm rel}+c)P
\]

和目标乘法的连接修正 \(-w\partial_w\log C_{J,\rm phys}\)。它含 (5) 的全部固定角项；本篇节省的是逐轮来源成本，并没有免费删除返回载体的导数。

## 6. 反复连接的真实预算

对原 \(P\in\mathcal W_{D,J}\)，先作一次 (3)，在计算格内作用 \(k\) 次 (20) 或 (21)，最后只作一次 (6)。所有实际来源列都在

\[
\boxed{\mathcal W_{D+2k+12m,J},}
\tag{24}
\]

目标至多增加 \(k+3m\) 行。三块使用范围需保持

\[
L+13+k+3m<3s.
\tag{25}
\]

若还使用来源导子的 \(p\)-饱和性，则须满足 (18) 的相应最大次数界。

原直接两来源连接每轮增加相对次数三；(24) 准确把 \(3k\) 换成 \(2k+12m\)，最大固定项为三十六。多出来的角列没有被遗漏：

\[
\dim\widetilde{\mathcal W}_{D,J}
=\dim\mathcal W_{D,J}+3(D+1)J(J+1).
\tag{26}
\]

固定 \(J\) 时新增维数为 \(O(D)\)，整个旧源已由 (3) 保留，(6) 的原返回容量已实际支付。

## 7. 两条完整中央基准仍是原 S 和原 T

在共同 regularized frame 中，准确为

\[
\widehat T_0=(g/d)^\alpha f,\qquad
\widehat T=V(t)\widehat T_0,
\quad \widehat S=(g/d)f.
\]

因此所有原中央权仍读取

\[
c_i=[w^{is}]\widehat S,\qquad
d_i=[w^{is}]\{V(t(w))\widehat T_0\},\qquad i=1,2,3,
\]

以及相同 \(\sharp\) 模型中的两条完整基准。原必要条件仍是

\[
a^2c_1-pa c_2+2p^2c_3=0,\qquad
\alpha^2a^2d_1-p\alpha a d_2+2p^2d_3=0\pmod{p^3}.
\tag{27}
\]

特别不能在第二条中删去 \(V\)，也不能把 \(T_0\)、\(\mathcal Q_2^kP\) 或返回乘积的完整中央导数另判为零。R403 的同一个 \(A_0\)、R425/R434 的完整 Hensel 解及全部第三位保持；(22) 只运输真实来源和有限提升。

## 8. 重新核算全量词全局斜率门槛

本节明确区分来源成本改善和已获算术估计。固定整函数 \(S,T_0\) 在 \(w=z^6\) 上仍有有限型增长阶至多 \(1/3\)：第 1 节的真实 theta 多项式表达给 \(z\) 上阶至多二，原 \(\mu_6\) 型使它们下降为 \(w\) 整函数。

对实际 canonical 列也保持完整 theta 成本：返回并作 \(k\) 次连接后的最大 degree 是 \(34(D+2k+c+40)+72J\)。其 Cauchy 项须使用 \(3q\log(1+D+2k+c+J)\)，不能只保新的“二”。移掉 \(V^j\) 后允许的额外 \(6j\) 个角次数，在 \(t=\infty\) 恰占用原 \(V^j\) 的同一极度；在 \(V\) 的六根处只是取消额外零，并不产生新极。因此乘原 \(G_0\) 后的计算列也保持对应的真实全纯 theta 次数。

它们也真代数独立。由

\[
T_0/S=\Theta^{19},\qquad
S^{36}/T_0^{17}=f(t)^{19},
\]

\(\Theta,t\) 均代数于 \(K(S,T_0)\)；R418 已付同一个 theta/角函数域的超越次数二，故 \(K(S,T_0)\) 也为二。没有用符号上两个变量代替真实独立性。

普通位的全部多项式 jet 仍可用零成本界。原普通形式坐标中 \(t\) 是整的正阶级数，\(V(t)\) 常数为一，所以 \(V(t)^{-1}\) 属于同一个整幂级数环；原 \(S,T\) 的有界 Amice 级数因而也给 \(T_0=T/V\) 的有界级数。R418 的全部次数、全部饱和前缀的 falling-factorial 论证遂原样适用。这里的有界级数只支付 jet 范数，不赋任何新中央零。

惰性位的无条件正规化也未改善：\(T_0\) 保留原 \(\alpha\kappa\)，\(V(t)^{-1}\) 在同一真半径内为整单位。其全部普通系数包络仍为 R418 的

\[
\sum_{p\ {m inert}}\log\|\varphi_D^q\|_p
\le3q\log q+O(q+D).
\tag{28}
\]

若要通过二坐标斜率反证，仍须对**全部** \(D,q\) 和每个真实非零饱和 jet 层证明

\[
\sum_{p\ {m inert}}\log\|\varphi_D^q\|_p
\le a_Iq\log D+b_Iq\log q+O(q+D),
\qquad \boxed{a_I+2b_I<3.}
\tag{29}
\]

固定返回的次数 \(\le36\)、行数 \(\le9\) 与 carry \(\le18\) 不改变这个 leading 门槛。固定次数平移使 Cauchy 中 \(\log(1+D+c+J)\) 与 \(\log(1+D+J)\) 之差有界；固定有限 carry 在可能出现的 \(p\le6(q+O(1))\) 上总成本至多常数倍 \(\sum_{p\le6(q+O(1))}\log p=O(q)\)，不能被叫作免费，但不产生新的 \(q\log q\) 系数。

同样，单独把连接的 \(D+3k\) 改为 \(D+2k+c\)，不会自动改变 (29) 的系数：两者对 \(D\ge1,k\ge0\) 的比值被只依赖固定 \(c\) 的常数上下夹住，其对数差只是 \(O(1)\)。若 \(k\) 本身随 \(D\) 增长，必须把整个 \(D+2k+c\) 代入真实全量词预算，不能把系数二直接认作 \(a_I=2\)。

此外，固定 \(J\le16\) 的 Kummer 计算格及 (24) 不能直接冒称原平面全部多项式列已经取得了 (29)；若使用 canonical 的全次数家族，也须对该家族每一个实际非零饱和 jet 层证明相应统一估计。三坐标家族的严格门仍为 \(a_{I,3}+3b_{I,3}<3\)。

目前 (27) 尚未证明任何一个新的全量词算术界；R444/R449 的实际可见相对 \(p^2\) 类也未由这次来源返回自动产生。已支付的是可反复使用的次数二整连接和一次固定返回，其下一用途是比较那些真正相对第二核、可提升左核及原两基准。没有停在局部闭合而宣称已取得全局斜率余量。

## 依赖与证书

R351/R352 的原次数二连接；R403 的两原来源与完整第三精度；R406/R408 的真实函数域和有限自由格；R418 的全量词增长/jet 预算；R444/R449 的可见首像及相对第二余核。脚本 `scripts/check-r453-single-return-degree-two.py` 核全部十二个剩余类、全部 \(0\le J\le16\) 返回预算和完整自由基计数。跨参数证明在正文，不扫描目标素数。
