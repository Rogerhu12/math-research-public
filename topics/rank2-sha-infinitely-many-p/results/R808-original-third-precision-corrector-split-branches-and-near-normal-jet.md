# R808 — 原第三精度同一修正的分裂二支与近支完整法向段

日期：2026-11-15。**状态：下述同一原来源、原精度和实际分支结论已证明；原全余像的指定非零及主目标仍未完成。**

R459 已给相对首次修正沿原因子分支的两个单位首项。
本篇把它们与同一个原第三行一起使用，得到一个更强的几何要求：
任何原第三精度提升的**同一个**首修正 $R$，在原点都有两条已经在剩余域上分裂的光滑支，
两支交数恰为 $h$；其中只有一支继续靠近原实际轴，其接触至少为 $h+r$。
这条近支的长度 $r$ 法向段还完全由原 Gaussian carry 指定。

这不是把未知 $R$ 换成任意二支曲线。
$R$ 仍在完整 $\mathcal W_D$，所有十九角帽、原 $P_{134}/U_0$、两条十三行和下一位均保留。
尤其本篇不把旧 $M$ 的第一次 $p^2$ 条件读成相对 $J$ 的 $p^2$ 条件。

## 1. 原精度、同一个 R 和准确适用范围

令
$$
p=6s-1>101,\qquad f_D<p,\qquad
1\le\ell<s-13,\quad \ell\le r+h,\qquad 1\le r<h,\qquad s=2h+r.
\tag{1}
$$
即原 $k_{\rm carry}=r+2h-s$ 恰为零。
取原单一 $Y=\mathscr R$ 格
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\quad
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad
C_n=\lfloor n/2\rfloor,\quad d=1+8t.
\tag{2}
$$
全部原次数帽与十九角条件均按 R680/R491 保持。

设同一个合法整因子提升给出真实来源
$$
P^{\rm fact}=t^r\widetilde F^{\,3}\widetilde q\in\mathcal W_D,
\qquad
F(0,1)=0,\quad
(\mathcal EF)(0,1)q(0,1)\ne0,
\quad \mathcal E=Y\partial_Y,
\tag{3}
$$
$F$ 不可约，原接触恰为
$$
\operatorname{ord}_w F(t(w),\bar g(w))=h.
\tag{4}
$$
这里 $\bar g$ 是原 regularized 轴，$t(w)=-w+O(w^2)$。
只使用本篇所需的原整有限前缀；没有把带首共振分母的未正规有理级数全体约化到 $k[[w]]$。

保同一个原 Gaussian 单位 $a$，及
$$
M^{\rm orig}=c_*U_0m_{13}J.
$$
假设存在同一整来源中的
$$
P^{(3)}=P^{\rm fact}+pR+p^2T,\qquad
M^{\rm orig}(P^{(3)})\in p^3\Gamma_{2s+\ell+13}.
\tag{5}
$$
下文的 $R$ 一律表示这里首修正的模 $p$ 约化；不为不同块另选修正。

**精度引理。** (5) 必给同一个 $R$ 的
$$
\boxed{J(P^{\rm fact}+pR)\in p^2\Gamma_{2s+\ell}.}
\tag{6}
$$

**证明。** 先对整个目标施原 $(c_*U_0)^{-1}$，包括 $P_{134}$ 和全部高尾。
R449 的原整对角形式为
$$
M=\begin{pmatrix}J_A\\pJ_B\end{pmatrix},
$$
其中 $B$ 恰为两条完整十三行，$A$ 为其余行。
(5) 使 $J_AP^{(3)}\in p^3$、$J_BP^{(3)}\in p^2$，故 $JP^{(3)}\in p^2$。
因 $J(p^2T)\in p^2$，去掉这一项即得 (6)。
这只是原整行权的推论，没有逆一个非单位的 $w^{13}$。$\square$

反之，若只给 $M(P^{\rm fact}+pR)\in p^2$，
则只有 $J_A(P^{\rm fact}+pR)\in p^2$ 与
$J_B(P^{\rm fact}+pR)\in p$。
因此它不够推出 (6)。
特别本篇所用的第 $2h$ 行不能从原旧长度 $s-13$ 偷读出来。

本篇也可直接从已经付清的 (6) 开始。
(5) 只是把它接到原真正第三精度的充分前提；没有反称 (6) 足以解原 $d_2$。

## 2. 同一原三行的单位数据

在 R459 的实际有限前缀上写
$$
\widetilde F(t(w),g(w))=w^h u(w)+p\xi(w),
\qquad
e(w)=(\mathcal E\widetilde F)(t(w),g(w)),
$$
$$
C(w)=\left(\frac{t(w)}w\right)^r
       \widetilde q(t(w),g(w)).
\tag{7}
$$
取约化后，$u_0,e_0,C_0,a$ 均非零。
这些是同一因子、余因子及实际轴的数据；$q$ 未投影成常数 charge。
定义
$$
\lambda=\frac{u_0}{e_0}\in k^\times,\qquad
B=\frac{C_0u_0^2e_0}{a}\in k^\times.
\tag{8}
$$

令 $Y=\psi(t)$ 是 $F=0$ 在 $(0,1)$ 的唯一光滑支。
由 (4)，
$$
\bar g(w)/\psi(t(w))-1
=\lambda w^h+O(w^{h+1}).
\tag{9}
$$
不使用特征 $p$ 中的无限对数：本篇的完整局部坐标始终可取
$Y/\psi-1$。

由 R459(13a)–(13c)，(6) 强制
$$
\boxed{
\begin{aligned}
R(t(w),\psi(t(w)))
   &=-2B\lambda^2w^{2h}+O(w^{2h+1}),\\
(\mathcal ER)(t(w),\psi(t(w)))
   &=5B\lambda w^h+O(w^{h+1}),\\
(\mathcal E^2R)(0,1)&=-6B.
\end{aligned}}
\tag{10}
$$
第一式可读，因为 $2h<s=2h+r$；第二式与第三式用的是同一 carry。
$r>0$ 使 native $\xi$ 不进入这些首项。

同时完整第一普通块给
$$
\boxed{R(t(w),\bar g(w))=0\pmod{w^s}.}
\tag{11}
$$
原第一 Euler 块还有整段准确式
$$
(\mathcal ER)(t(w),\bar g(w))
\equiv
-6w^{h+r}Cue\,\xi-a^{-1}w^hCu^3
\pmod{w^s}.
\tag{12}
$$
所有含 $\mathcal Eq$ 的额外项从 $r+2h=s$ 起，所以不进入这个块。
本篇没有在更短的旧目标中主动删除它们。

式 (10) 只作为既有真实三行输入。
下面的分裂、接触和整段近支 normal 是把这三个输入联立后的结论。

## 3. 原修正在剩余域上恰有两条光滑支

**定理 1。** 在 (1)–(6) 下，$R=0$ 在原点的完成局部曲线准确有两条光滑支
$$
Y=\psi_R^+(t),\qquad Y=\psi_R^-(t)
$$
均定义于 $k[[t]]$。按 $w$ 参数化，准确有
$$
\boxed{
\begin{aligned}
\frac{\psi_R^+(t(w))}{\psi(t(w))}-1
   &=\lambda w^h+O(w^{h+1}),\\
\frac{\psi_R^-(t(w))}{\psi(t(w))}-1
   &=\frac23\lambda w^h+O(w^{h+1}).
\end{aligned}}
\tag{13}
$$
它们互相、以及分别与 $F$ 的原分支的交数均恰为 $h$。
原点的局部曲线已经约化，且
$$
\boxed{\delta_P(R)=h.}
\tag{14}
$$
这里不需要二次常数域扩张。

**证明。** 先保全原最低层。
由 (2)，$R(0,Y)$ 只能是二次式；(10)、(11)、(12) 在零阶给
$$
\boxed{R(0,Y)=-3B(Y-1)^2.}
\tag{15}
$$
因此在 $Y=1$ 处，Weierstrass 的度数恰为二，没有第三条局部支，也没有额外重复成分。

用完整代数局部坐标 $v=Y/\psi(t(w))-1$。
展开
$$
R(t(w),\psi(t(w))(1+v))
=R_C+(\mathcal ER)_C v+
 \frac{(\mathcal E^2R-\mathcal ER)_C}{2}v^2+\cdots .
$$
将 $v=w^h z$，由 (10) 得
$$
\boxed{
w^{-2h}R(t(w),\psi(t(w))(1+w^hz))
\equiv
B(-2\lambda^2+5\lambda z-3z^2)
=-3B(z-\lambda)(z-2\lambda/3)
\pmod w.}
\tag{16}
$$
左侧确实整：常数项至少 $2h$、一次项至少 $h$，其余第 $j$ 项乘 $w^{jh}$。
$j\ge3$ 时除 $w^{2h}$ 后仍有正阶。
两个显示根均在 $k$，其差为 $\lambda/3\ne0$。
Hensel 引理分别给唯一 $z_+,z_-\in k[[w]]$，从而得到 (13)。
这与 (15) 的度二 Weierstrass 因子合起来证明它们就是全部局部支。

每条支以 $w$（或 $t$）为参数，故光滑；
两支差的首系数为 $\lambda/3$，与 $\psi$ 的差首系数分别为
$\lambda$、$2\lambda/3$，所以三个交数都恰为 $h$。
两光滑支之并的 $\delta$ 正是它们的交数，得 (14)。

也可在同一完成环中作完整平方及单位平方根的 Hensel 提升，
把局部方程化成单位乘 $v'^2-w^{2h}$。
由于首判别式已经是 $(\lambda/3)^2$，该平方根在 $k[[w]]$ 中存在。
这里与任意二重首核可能出现的二次扭曲不同：
分裂由同一个 $-2,5,-6$ 三项及其判别式 $25-24=1$ 支付。$\square$

## 4. 只有近支继续跟随原轴，并有指定的长度 r 法向段

**定理 2。** (13) 中的标号可唯一选为
$$
\boxed{
\operatorname{ord}_w\bigl(\bar g-\psi_R^+\bigr)\ge h+r,\qquad
\operatorname{ord}_w\bigl(\bar g-\psi_R^-\bigr)=h.
}
\tag{17}
$$
近支的完整指定 normal 段为
$$
\boxed{
(\mathcal ER)(t(w),\psi_R^+(t(w)))
\equiv -a^{-1}w^h C(w)u(w)^3
\pmod{w^{h+r}}.
}
\tag{18}
$$
特别其阶恰为 $h$，首系数为 $-B\lambda$。
另一支的法向首系数为 $+B\lambda$。

**证明。** 由 (9)、(13)，原轴与负支的差首项为
$\lambda w^h/3$，故其阶恰为 $h$。
在原点的完整局部环中，定理1给
$$
R(t(w),Y)=U(w,Y)(Y-\psi_R^+)(Y-\psi_R^-),
\qquad U(0,1)\ne0.
$$
代原轴并用 (11)，另一因子的阶必须至少为
$s-h=h+r$，得到 (17)。
这一判断仅用原 $g$ 的 $<s$ 前缀；
任意形式延长都给相同的已读结论。

因 $\bar g-\psi_R^+\in w^{h+r}$，
完整多项式 $\mathcal ER$ 在这两点的差也属于 $w^{h+r}$。
又 (12) 的 native 项从 $h+r$ 才开始，故得到 (18)。
$r<h$ 保证这个所用窗口严格在 $s$ 内，
且 (7) 的真实 $u$ 只需读至 $r-1$，相应 $F(t,g)$ 只到 $h+r-1<s$。

两支上的导数首项也直接从 (16) 得到：
在 $z=\lambda$ 与 $z=2\lambda/3$，二次式导数分别为
$-B\lambda$ 与 $+B\lambda$。
普通 $Y$ 导数换成 $\mathcal E$ 只乘常数为一的局部单位，故首项不变。$\square$

式 (18) 是同一实际 $q,F,g,a$ 的指定整段，不是另选一个 normal 值。
它只说明 native $\xi$ 尚未到这段；
在 $h+r$ 及以后必须恢复完整 (12)，不能把 native 项永久删除。

## 5. 全来源的零角和真实全局交数要求

(15) 的 $Y^2$ 系数为单位。
另一方面 $R\in\bar{\mathcal W}_D$ 满足原零角
$$
v_0(R)=\min_n\{4\operatorname{ord}_tR_n-n\}\ge-2.
$$
因此
$$
\boxed{v_0(R)=-2,\qquad m_R=2.}
\tag{19}
$$
这不是只记录 $R(0,Y)$ 的次数，而是完整原 Gauss 值的等号。
若 $d_R=\deg_YR$，则原零角四步链的总重数为 $d_R-2$；
其它固定角、无穷角及每个系数帽仍须取 $R$ 的真实数据。
没有把 $R$ 换成环境中全部 $m_R=2$ 的多项式。

设 $C$ 是 R495 同一十九角曲面上的原因子严格变换。
(10) 第一式非零，故 $F\nmid R$。
取 $R$ 的真实有效零除子，并保其全部边界分量。
在原光滑点处，定理1准确给
$$
\boxed{I_P(C,\operatorname{div}R)=2h.}
\tag{20}
$$
因 $R$ 是同一个 $\mathcal B_D$ 截面，且 $C$ 不是其分量，
得到原必要交数门
$$
\boxed{2h\le\mathcal B_D\cdot C.}
\tag{21}
$$
若两条局部支落在不同的全局几何不可约分量，
每个相应分量与 $C$ 的交数都至少为 $h$，
两分量之间的交数也至少为 $h$。
若两支属于同一个全局几何不可约分量，
该分量在原点已消耗恰为 $h$ 的局部 $\delta$。
这些都针对 $R$ 的实际分量，不把局部分裂误作全局因式分解。

(21) 在常见 $\mathcal B_D\cdot C\sim3\kappa$ 的临界族
仍只给 $2h\le3\kappa+o(\kappa)$。
它不排 $h/\kappa\to9/8$。
同样，(19) 本身不把完整 $R$ 降到 $\mathcal H_2$，
也不能由局部两支自由选择两个更小来源因子。

## 6. 与 R790 的指定全像及真正下一位

对 R790 的 $r=2,\ell=1$，(17) 的近支接触至少为 $h+2$，
(18) 则指定它的两个首法向系数。
在 R803/R799/R810 的原 $\mathbf F_p$、$b_0=3$ 强窗内，现已须 $b\ge5$；
这个有限次数排除的域与范围不扩到任意剩余域或任意 $b$。
本篇的局部证明本身不依赖该有限计算。

R790(30) 仍是原整个 $\mathcal W_D$ 首次修正的精确配对。
本篇没有证明那个配对非零。
它说明如果一个同 $R$ 进一步通过原 primitive $p^3$，
那么这个同样的 $R$ 还必须满足 (13)、(17)、(18)、(19) 和全部原角帽。
原首次 $p^2$ 可解并不已付这些更强条件。

即使这些必要条件全部满足，
仍要计算原 $M(P^{\rm fact}+pR)/p^2$，
并由同一个真实来源的 $p^2T$ 消去完整第二代表。
两条十三行、原低行右逆高尾、公共 $U_0$ 和全部原第三块不能省略。
本篇没有给新分支或 $R$ 新增中央零，也没有把 (21) 当成主目标非零。

依赖：
[R449](R449-relative-second-cokernel-and-complete-carry-exact-sequences.md)；
[R459](R459-actual-angular-content-and-padded-cubic-first-lift.md)；
[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)；
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R680](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)；
[R790](R790-original-cube-full-forcing-and-factor-contact-bockstein-pairing.md)；
[R803](R803-original-zero-constant-cubic-all-prime-exclusion-and-full-r2-window.md)；
[R810](R810-original-quartic-all-prime-exclusion-and-complete-zero-chain.md)。
