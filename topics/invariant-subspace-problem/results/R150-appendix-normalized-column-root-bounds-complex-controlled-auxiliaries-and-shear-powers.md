# R150 附录：正主行的归一化全柱根界、复受控辅助行与全部剪切点态幂

日期：2026-11-13（UTC）。作者：kernel_resume_1cf / normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：完整证明；根与 normal 已独立核验全部共同词域、归一化三项幂、相伴图配对与重排范围。不另登记主结果号。

## 0. 范围扣除与新增步骤

已有[有限阶正主行相伴图附录](R150-appendix-finite-order-positive-anchor-companion-graphs-and-all-shear-powers.md)和[谐和/好时间条带附录](R150-appendix-harmonic-positive-anchor-sharp-strip-budget-and-all-shear-powers.md)，分别使用真实半群增长和两个实正 first 的二次增生性，关闭了相应的实辅助行。
[R243](R243-partial-sum-centers-and-log-tail-polynomial-cyclicity.md) 与
[R251](R251-arbitrary-coordinate-heads-and-rearrangement-invariant-first-centers.md)
则已给单个 first 的有限头进位、全柱高次根界及有界限制谱约束。

本稿沿用这些已证预算，但新增的对象是实际归一化闭算子
$Z=(Y-X^2)_{\rm can}X^{-1}$ 的有界限制，而非一个有界 first 限制。
其测试式含真正有界拟幂零系数 $L^*=(X^{-1})^*$。
下面完整支付这个系数、混合尾幂和深核心上的通常伴随配对。
由此允许任意复辅助行 $c$，不要求它实，也不要求整预解的有限阶或双指数增长。

## 1. 主结论

设
$$
u=u_*+\sum_{j\ge0}a_j\chi_j,\qquad
v=v_*+\sum_{j\ge0}c_j\chi_j,
\qquad u_*,v_*\in\mathbb C,
$$
其中
$$
a_j\ge0,\qquad a\in\ell^2\setminus\ell^1,\qquad
c_j\in\mathbb C,\qquad |c_j|\le C_0a_j
\tag{1.1}
$$
且 $C_0<\infty$ 任意。

假设存在递增有限位集 $F_n\uparrow\mathbb N_0$，记
$$
d_n=|F_n|,\quad
s_n=\sum_{j\in F_n}a_j,\quad
g_n=\|a_{F_n^c}\|_2+\|c_{F_n^c}\|_2,
$$
满足
$$
\boxed{\frac{\sqrt{d_n}\,g_n}{s_n}\longrightarrow0.}
\tag{1.2}
$$
允许只沿一个递增子列满足；重新编号即可。
因 $a\ge0$ 不可和且 $F_n$ 穷尽，$s_n\to+\infty$。

令
$$
G(x,z)=z^m+
\sum_{\substack{i+j\le m\\j<m}}g_{ij}x^iz^j,
\qquad m\ge1,\quad g_{ij}\in\mathbb C.
\tag{1.3}
$$
则对任意 $\lambda\in\mathbb C$、整数 $r\ge1$ 和复 $\ell^2$ first 指数权 $w$，
$$
\boxed{[G(u,v-u^2)-\lambda]^r e^w
\text{ 是实际 }A\text{ 的循环向量}.}
\tag{1.4}
$$

特别，(1.4) 包括
$$
[(v-u^2)^2-\beta u^2-\lambda]^r e^w
\qquad(\beta,\lambda\in\mathbb C,\ r\ge1)
\tag{1.5}
$$
的全部剪切碰撞和全部固定点态幂。
这里保留完整普通 Bell 变换，不以自然算子幂替换点态幂。

一个重排不变的充分条件是：设 $a$ 的非零幅度递减重排为
$r_1\ge r_2\ge\cdots>0$，则
$$
\boxed{
\liminf_{n\to\infty}
\frac{n\sum_{k>n}r_k^2}{(\sum_{k\le n}r_k)^2}=0.
}
\tag{1.6}
$$
尤其，任意正不可和弱 $\ell^1$ 行
$$
\sup_{n\ge1}nr_n<\infty
\tag{1.7}
$$
都满足结论，允许原物理坐标任意排列，也允许任意大小的复受控辅助行。

## 2. 实际算子、共同域与转置测试

特意取未倾斜且无常数的 first
$$
X=X_{\sum a_j\chi_j},\qquad Y=X_{\sum c_j\chi_j}.
$$
R128/R134 给 $X$ 最大增生且空谱。因此
$$
L=X^{-1}\in A'
$$
是实际有界、单射、拟幂零算子；$\sigma(L)=\{0\}$。
所有有界 $A'$ 元素保持 $X,Y$ 的各有限共同自然词域，并在这些域上交换。

记 $\mathcal D_\infty^\dagger$ 为 $X^*,Y^*$ 的全部有限有序自然词共同域。
对有限位集 $F$，令 $Q_F$ 为所有支撑在 $F$ 的 Walsh 柱的正交投影。
R251 的补集指数次数尺度，逐字用于两个 first，保证
$$
Q_FH\subset\mathcal D_\infty^\dagger.
\tag{2.1}
$$
确切地，各次有限混合词先由同一个补集指数次数权逐步付域；
有限有界头再加入。共同共轭 $C$ 保持 $Q_FH$，
用 $X^*=CXC,\ Y^*=CYC$ 把这些具体域运输过去。
这里没有从一次伴随同域推断全部高次同域。

$L^*$ 保持 $\mathcal D_\infty^\dagger$ 并与所有相应词交换。
这由原 $L$ 的完整域交换和 $L^*=CLC$ 得到；
不需 $L^*$ 保持某个未知闭空间。

仅在这个共同深域上定义测试算子
$$
D^\dagger=L^*Y^*-X^*.
\tag{2.2}
$$
它保持 $\mathcal D_\infty^\dagger$，因为每个有限词仍有下一层词可用。
故所有 $(D^\dagger)^pQ_F$ 有真实意义。
本稿不宣称 (2.2) 是任何未经核验的全局最大伴随域。

另一方面令
$$
T=(Y-X^2)_{\rm can},\qquad Z=TL,\qquad
\operatorname{Dom}Z=\{h:Lh\in\operatorname{Dom}T\}.
\tag{2.3}
$$
R186 给 $T$ 的规范最大闭实现；有界预复合使 $Z$ 闭。
在充分深的原自然域上，
$$
Zh=YLh-Xh.
\tag{2.4}
$$

## 3. 任意位集上的有界系数头预算

暂固定 $F=F_n$，省略下标 $n$，并置
$$
t=\sum_{j\in F}c_j,\qquad d=|F|,\qquad s=\sum_{j\in F}a_j.
$$
设
$$
H_a=\sum_{j\in F}a_j(V_j-I),\quad
H_c=\sum_{j\in F}c_j(V_j-I),\quad
Z_a=X_{\sum_{j\notin F}a_j\chi_j},\quad
Z_c=X_{\sum_{j\notin F}c_j\chi_j}.
$$
R251 的有限去项给完整域等式
$$
X=sI+H_a+Z_a,\qquad Y=tI+H_c+Z_c.
\tag{3.1}
$$
因此在 $\mathcal D_\infty^\dagger$ 上
$$
\frac{D^\dagger+sI}{s}
=B_F+H_F'+Z_F',
\tag{3.2}
$$
其中
$$
B_F=\frac{\overline t}{s}L^*,\quad
H_F'=\frac{-H_a^*+L^*H_c^*}{s},\quad
Z_F'=\frac{-Z_a^*+L^*Z_c^*}{s}.
\tag{3.3}
$$
三项在该域上完整交换；前两项有界并保持全部所需词域。

由 (1.1)，$|t|/s\le C_0$。
$L^*$ 拟幂零，所以对每个固定 $\epsilon>0$ 存在固定 $K_\epsilon<\infty$，使
$$
\boxed{\|B_F^\ell\|\le K_\epsilon\epsilon^\ell
\quad(\ell\ge0,\text{ 全部 }F).}
\tag{3.4}
$$
可先对 $C_0L^*$ 的幂应用谱半径公式；$C_0=0$ 直接处理。
不把 $tL^*$ 省略，也不把它误认为零算子。

写
$$
H_F'=\sum_{j\in F}E_j(V_j^*-I),\qquad
E_j=\frac{-a_j I+\overline{c_j}L^*}{s}.
$$
这些有界系数彼此交换，并与全部 $V_j^*$ 交换，且
$$
\sum_{j\in F}\|E_j\|\le1+C_0\|L\|.
\tag{3.5}
$$
R251 §2 的逐单项式进位证明适用于这些有界系数：
在多项式展开中先将所有 $N_j^*$ 因子准确进位，再付 $3^k$ 分母成本，
最后用 $(\sum\|E_j\|)^k$ 估计系数。
因此存在固定 $A\ge1$（可取 $\max(1,6(1+C_0\|L\|))$），使
$$
\|{H_F'}^k\|\le A^k\quad(k\ge0),
$$
$$
\boxed{
\|{H_F'}^k\|\le A^k e^{-\gamma k^4}
\quad(k\ge\max(2d,16)),\qquad \gamma=770/16^4.
}
\tag{3.6}
$$
阈值依赖位数 $d$，不依赖最大物理位。
当 $d\ge8$，置
$$
\delta_d=Ae^{-\gamma(2d)^3};
$$
则 $k\ge2d$ 时 $\|{H_F'}^k\|\le\delta_d^k$，且 $\delta_d\to0$。

## 4. 两个真实尾的混合幂预算

设 $g=\|a_{F^c}\|_2+\|c_{F^c}\|_2$。
R251 §3 对任意 $|z|=1$ 给
$$
\|(Z_a+zZ_c)^qQ_F\|
\le(Cg\sqrt q)^q,\qquad q\ge1,
\tag{4.1}
$$
其中 $C$ 是固定模型常数。
有限混合词的共同域已由同一指数次数尺度支付，
所以真正的自然二项式及算子值 Cauchy 系数公式给
$$
\boxed{
\|Z_a^{q-j}Z_c^jQ_F\|
\le\binom qj^{-1}(Cg\sqrt q)^q,\qquad0\le j\le q.
}
\tag{4.2}
$$
共同共轭保 $Q_F$，因此同样的界适用于对应伴随混合词。
没有把两个无界尾各自的作用范数相乘。

将 $L^*$ 全部移到左端并展开 $Z_F'$，得到
$$
\begin{aligned}
\|{Z_F'}^qQ_F\|
&\le s^{-q}(Cg\sqrt q)^q\sum_{j=0}^q\|L\|^j\\
&\le\left(C_1\frac{g}{s}\sqrt q\right)^q,\qquad q\ge1,
\end{aligned}
\tag{4.3}
$$
其中可取 $C_1=2C\max(1,\|L\|)$，因为 $q+1\le2^q$。
$q=0$ 按 $Q_F$ 解释。
所有幂先在 (2.1) 的真实共同深域上运算；
并未假设 $Z_F'$ 在全空间有界或其自然高幂闭。

## 5. 三项展开给归一化全柱根界

记
$$
q_n=\frac{\sqrt{d_n}\,g_n}{s_n}\longrightarrow0,\qquad
p_n=\left\lceil\frac{d_n}{q_n}\right\rceil.
\tag{5.1}
$$
无限支撑的正主行使 $g_n>0$，所以这里 $q_n>0$。
有 $p_n/d_n\to\infty$，并且
$$
D_n=C_1\frac{g_n}{s_n}\sqrt{p_n}\longrightarrow0.
\tag{5.2}
$$
具体 $D_n^2\le C_1^2(q_n+q_n^2/d_n)$。
充分大时 $p_n\ge4d_n$。

固定 $0<\epsilon<1/4$，置 $E_n=\epsilon+D_n$。
展开 (3.2) 的 $p_n$ 次自然幂；对一个含 $k$ 个头因子的项，
先把有界 $B_F$ 和尾的全部二项项求和。
(3.4)、(4.3) 给
$$
\left\|\left(\frac{D^\dagger+s_n I}{s_n}\right)^{p_n}Q_{F_n}\right\|
\le K_\epsilon\sum_{k=0}^{p_n}
\binom{p_n}{k}\|{H_{F_n}'}^k\|E_n^{p_n-k}.
\tag{5.3}
$$
这是同一个全柱输入上的真实三项展开，
不需要 $Q_{F_n}$ 与 $L^*$ 交换。

令 $\theta_n=2d_n/p_n\to0$，以及
$h(\theta)=-\theta\log\theta-(1-\theta)\log(1-\theta)$。
充分大时 $E_n<1$。
与 R243 §2 相同，把 $k<2d_n$ 和 $k\ge2d_n$ 两块分开，得
$$
\begin{aligned}
&\left\|\left(\frac{D^\dagger+s_n I}{s_n}\right)^{p_n}
Q_{F_n}\right\|^{1/p_n}\\
&\quad\le K_\epsilon^{1/p_n}
\left[
(2d_n)^{1/p_n}e^{h(\theta_n)}
 A^{\theta_n}E_n^{1-\theta_n}
+\delta_{d_n}+E_n
\right].
\end{aligned}
\tag{5.4}
$$
低头块只用了
$A^kE_n^{p_n-k}\le A^{2d_n}E_n^{p_n-2d_n}$；
高头块由 $(\delta_{d_n}+E_n)^{p_n}$ 控制。

对固定 $\epsilon$，右端上极限至多 $2\epsilon$。
因为 (5.3) 对每个固定正 $\epsilon$ 都成立，实际左端因此趋零：
$$
\boxed{
\left\|\left(\frac{D^\dagger+s_n I}{s_n}\right)^{p_n}
Q_{F_n}\right\|^{1/p_n}\longrightarrow0.
}
\tag{5.5}
$$
这里不要求任何随 $n$ 变化的 $K_\epsilon$ 界，
也不进行会改变未知空间的范数变换。

## 6. 深核心配对排除 Z 的有界放大限制

考虑任意固定有限放大 $H^b$，以粗体记原算子的对角放大。
设闭空间 $\mathcal M\subset H^b$ 被所有对角 $A'$ 保持，并满足
$$
\mathcal M\subseteq\operatorname{Dom}\mathbf Z,\qquad
\mathbf Z\mathcal M\subseteq\mathcal M,\qquad
J:=\mathbf Z|_{\mathcal M}\in B(\mathcal M).
\tag{6.1}
$$
则 $\mathcal M=0$。

证明关键是得到真实投影恒等式，而非给 $\mathcal M$ 继承未知通常伴随域。
令 $P$ 为到 $\mathcal M$ 的正交投影。
对 $h\in\mathcal M$，用 R186 共同正则器的充分深幂
$$
h_t=\operatorname{diag}(R(t)^N)h
$$
得到 $h_t\to h$，且 $h_t$ 位于所需 $X,Y$ 自然词域并仍在 $\mathcal M$。
$\mathbf Z$ 与该正则器域交换，因此
$\mathbf Z h_t=J h_t\to Jh$。
对 $f\in(\mathcal D_\infty^\dagger)^b$，(2.4) 与通常伴随定义给
$$
\langle Jh_t,f\rangle
=\langle \mathbf Y\mathbf Lh_t-\mathbf Xh_t,f\rangle
=\langle h_t,\mathbf D^\dagger f\rangle.
$$
取极限得到
$$
\boxed{P\mathbf D^\dagger f=J^*Pf.}
\tag{6.2}
$$
内积按第一变量线性。
此式没有宣称 $J^*$ 是全空间 $Z^*$ 的限制。

由 (2.1)—(2.2)，$\mathbf Q_{F_n}H^b$ 及其任意有限
$\mathbf D^\dagger$ 迭代仍在所需共同深域内。
所以 (6.2) 可逐次迭代，给
$$
P(\mathbf D^\dagger+s_n I)^{p_n}\mathbf Q_{F_n}
=(J^*+s_n I)^{p_n}P\mathbf Q_{F_n}.
\tag{6.3}
$$
当 $n$ 大时 $s_n>\|J\|$，故
$$
\left\|\left(I+\frac{J^*}{s_n}\right)^{-1}\right\|
\le(1-\|J\|/s_n)^{-1}\longrightarrow1.
$$
由 (5.5)、(6.3)，
$$
\|P\mathbf Q_{F_n}\|
\le
\left[
(1-\|J\|/s_n)^{-1}
\left\|\left(\frac{D^\dagger+s_n I}{s_n}\right)^{p_n}
Q_{F_n}\right\|^{1/p_n}
\right]^{p_n}
\longrightarrow0.
\tag{6.4}
$$
而 $\mathbf Q_{F_n}\to I$ 强，所以 $P=0$。
证明完成。甚至不需要 $J$ 有限谱。

## 7. 从完整 Bell 核构造这个被排除的闭图

这里复用
[相伴矩阵图附录](R150-appendix-finite-order-positive-anchor-companion-graphs-and-all-shear-powers.md)
§§3—5 的已经逐域证明的构造。
那些节只使用 $X$ 的实际有界逆、R186 混合词域和有界交换系数；
不使用辅助系数实性、两个正 first 或半群增长。
为明确其对当前点态向量的用途，列出全部输入。

令 $d=mr$，$F(x,y)=[G(x,y-x^2)-\lambda]^r$。
它的完整普通 Bell 多项式包含所有联合混合 cumulant。
在坐标 $z=y-x^2$ 中，
$$
\partial_x|_y=\partial_x|_z-2x\partial_z,\qquad
\partial_y=\partial_z.
$$
因此完整 Bell 变换仍对 $(x,z)$ 总次数至多 $d$，
且最高 $z^d$ 系数为 $I$。
所有正阶导数项的 $z$ 次数至多 $d-1$。
常数和任意复指数倾斜带来真实有界交换项 $H,K$；
实际代入
$$
x\mapsto x+H,\qquad
z\mapsto z-2Hx+K-H^2
$$
仍保这个总次数和首一最高系数。

所以原指定向量的规范最大闭实现 $\mathsf P$ 来自
$$
P(X,Y)=(Y-X^2)^d+
\sum_{\substack{i+j\le d\\j<d}}C_{ij}X^i(Y-X^2)^j,
\qquad C_{ij}\in A'.
\tag{7.1}
$$
在充分深的共同自然域上，
$$
L^dP=Z^d+\sum_{j<d}A_jZ^j,\qquad
A_j=\sum_{i\le d-j}C_{ij}L^{d-i-j}\in A'.
\tag{7.2}
$$
最高系数是真实 $I$，所有 $L$ 指数非负。

若 $M=\ker\mathsf P\ne0$，令 $\mathcal D_k$ 为 $X,Y$ 长度至多 $k$
的全部有序自然词共同域，取 $k_0=4d+4$。
$Z$ 至多消耗两层词域；共同正则器说明
$$
\mathcal M=
\overline{\{(f,Zf,\ldots,Z^{d-1}f):f\in M\cap\mathcal D_k\}}
\subset H^d
\tag{7.3}
$$
对 $k\ge k_0$ 不依赖 $k$，非零，且保持所有对角 $A'$。
(7.2) 的有界相伴矩阵把深图移成
$(Zf,\ldots,Z^df)$。
从起始深度 $k+2$ 运算可保证 $Zf\in M\cap\mathcal D_k$，
故相伴矩阵保持 $\mathcal M$。
$\operatorname{diag}Z$ 闭，遂将整个闭图放入其域，并在该图上等于这个有界矩阵。
因此恰得到 (6.1)，与 §6 矛盾。

所以 $\ker\mathsf P=0$。
R186 在原 $H$ 上的完整 $C$ 自伴给 $\mathsf P$ 像稠密；
指定循环指数向量 $e^w$ 的混合图核心给
$$
[[G(u,v-u^2)-\lambda]^re^w]_A
=\overline{\operatorname{Ran}\mathsf P}=H.
$$
证明 (1.4)。
没有把任何未知限制认作 $C$ 自伴，也没有假设自然 $Z^d$ 闭。

## 8. 重排判据、弱 l1 与真正的对数慢尾例

令 $A_n$ 为幅度最大的 $n$ 个非零主系数的实际位集，并取
$$
F_n=A_n\cup[0,n).
$$
这些集合递增、穷尽，且 $|F_n|\le2n$。
正系数给
$$
s_n\ge S_n:=\sum_{k\le n}r_k\longrightarrow\infty,\qquad
g_n\le(1+C_0)\left(\sum_{k>n}r_k^2\right)^{1/2}.
$$
所以 (1.6) 的一个递增子列给 (1.2)。
整个证明保留原物理位和实际 carry；
这里的排序只选择有限位集，没有重定义无界 first。

若 $r_k\le B/k$，则
$$
n\sum_{k>n}r_k^2\le B^2,\qquad S_n\to\infty,
$$
故 (1.6) 成立。这证明 (1.7) 的全部复受控辅助结论。

特别
$$
a_j=\frac1{(j+2)\log(j+2)},\qquad
c_j=(-1)^ja_j
$$
满足
$$
s_n\asymp\log\log n,\qquad
\|a_{\ge n}\|_2^2=O((n\log^2n)^{-1}),
$$
所以 (1.2) 成立。
这一例的 $\Theta_a(t)/(t\log t)\to0$，
不由先前正计数比条带定理覆盖。
现在其 (1.5) 的全部 $\beta,\lambda,r,w$ 均被本稿关闭；
将交替实系数换成任意有界复相位/振幅乘子 $c_j/a_j$ 也仍成立。

规范调和主行 $a_j=1/(j+1)$ 同样覆盖，
且辅助行无需实、其受控常数无需满足 $2\pi$ 阈值。
与先前谐和条带稿重合的实小常数范围只记作范围扣除。

## 9. 保留边界

本稿的机制是同一实际闭图内的有界归一化限制，
加上原 Haar 全柱上的高次伴随测试，不是一般半群抽象结论。

(1.6) 不是所有正不可和 $\ell^2$ 行的自动性质：
若 $r_n\asymp n^{-\sigma}$ 且 $1/2<\sigma<1$ 为标准规则幂尾，
其分式一般保持正量级。
这些行的实受控辅助已有有限阶条带稿；任意复辅助不能从该实结论免费取得。
本稿也没有处理任意不受控的第二慢行、全部多变量核或完整 ISP。
