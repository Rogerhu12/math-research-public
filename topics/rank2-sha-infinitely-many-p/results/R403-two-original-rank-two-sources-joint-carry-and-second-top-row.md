# R403：两条真实 rank-two 来源的共同三块、完整联合进位与第二顶行

日期：2026-11-14。**状态：已证明。** R398/R402 新增的 degree72 来源，与原 degree34 来源在同一物理坐标中给出两条完整中央失败条件。本文支付它们共用的第三精度 theta 模型、不同 Gaussian 权和全部角向进位；联合失败使旧第二中央系数由真实 wrap 数据唯一确定。两条中央修正的最高两行还给一个统一的单位三角子式。两条基准项始终保留，没有将固定乘子或任何新的 canonical 列另判中央零。

## 1. 原来源、共同曲线及合法 Gaussian

在共同 $E_1:y^2=x^3+1$ 上取
$$
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad
\Theta=x\sigma^2,\quad t=-1/x^3,\quad w=z^6.
$$
与旧曲线共同的好惰性范围是
$$
p\ge11,\quad p\equiv5\pmod6,\quad p\ne17,\quad p+1=6s.
\tag{1}
$$
以下第 2–7 节统一取 R385/R390 已经支付全三块模型及全部有限极界的
$p>83$。本文标明的固定单位在整个 (1) 都是单位。

记
$$
a(t)=t(t-1)(16t^2+4t+7),\qquad
f(t)=\frac{(1+8t)a(t)}7,
$$
$$
V(t)=(1-4t)(1-20t-8t^2)(1+96t+48t^2-64t^3).
\tag{2}
$$
R297/R398 的两条实际来源，归一为首项 $z^6$，准确是
$$
\boxed{
S=\Theta^{17}f(t),\quad
T=\Theta^{36}f(t)V(t),\quad
H=\Theta^{19}V(t),\quad T=SH .
}
\tag{3}
$$
这里 $S$ 是原 $E_{17}$ 来源经已付同构得到的 $A_{34}$，
$T$ 是原 $E_{24}$ 来源经已付同构得到的 $A_{72}$。
$H$ 只是 R398 的真实固定二、三挠乘子，不增加一条中央零假设。

令 $c=[z^{p+1}]\log(\sigma/z)$。
为与旧 R385 模型共用规范，可取
$$
\kappa=34c+\Delta,\quad \Delta\in\mathcal O,\qquad
\alpha=\frac{36}{17},\quad a_p=p\kappa\in\mathcal O^\times.
$$
两条来源的实际 Gaussian 分别是 $\kappa$ 和 $\alpha\kappa$；
后一项与 $72c$ 的差为 $\alpha\Delta\in\mathcal O$。
R342 的完整正整数插值及 Newton 尾证明这种重分解乘
$(\kappa_{\rm old}/\kappa_{\rm new})^u$。
两条来源质量均为零，故其完整中央导数不变。
不能只改变 $g$ 而保留旧 $a_p$，也不能把第二来源仍赋 degree34。

定义
$$
U=\Theta e^{-(\kappa/17)w^s},\qquad
g=(1+8t)U^{17},
$$
$$
\widehat S=U^{17}f,\qquad
\widehat T=U^{36}fV,\qquad
\widehat H=U^{19}V .
\tag{4}
$$
于是整条身份是 $\widehat T=\widehat S\widehat H$，
而 $\widehat H(0)=1$。

## 2. 第二来源确有相同的完整第三聚合

写
$$
c_j=[w^{js}]\widehat S,\qquad
d_j=[w^{js}]\widehat T,\qquad h_j=[w^{js}]\widehat H.
\tag{5}
$$
$h_0=1$、$c_0=d_0=0$。

**引理1。**
$$
c_j,d_j,h_j\in\mathcal O\quad(1\le j\le5),\qquad
d_6\in p^{-1}\mathcal O.
\tag{6}
$$

**证明。** R382 已付 $g$ 在 $w^p$ 之前整，并付
$[w^p]g\in p^{-1}\mathcal O$。
其坐标 $t(w)$ 整至 $w^{p+1}$，首系数为负一。
因 $17$ 在 (1) 为单位，
$(g/(1+8t))^{36/17}$ 和 $(g/(1+8t))^{19/17}$
的有限形式二项展开同样在 $w^p$ 之前整。
这是 $\mathbf Z_p$ 指数的整二项式展开，
不是把这些形式根添加为新的算术来源。
它们的第 $p$ 项至多有一个 $p$ 分母：
含原第 $p$ 项的贡献只能是线性项，其余项的二项系数整。
乘回 $fV$ 或 $V$；前者从 $w$ 起，后者常数一。
由于 $5s<p$，得到所列结论。
这里第六权确实使用了角因子整至 $w^{p+1}$ 的完整边界。$\square$

R402 对 $T$ 的全部 Newton 系数给
$$
v_p\!\left((\alpha\kappa)^{-h}d_h\right)
\ge\left\lceil\frac{h(p-1)+6}{2p}\right\rceil.
$$
所以 $h\ge7$ 的完整导数尾都在 $p^4\mathcal O$；
$h=4,5,6$ 则由 (6) 分别支付。
对 $S$ 使用 R382，得到两条真实全和比较
$$
\boxed{\begin{aligned}
J_S'(0)&\equiv
 \frac p{a_p}c_1-\frac{p^2}{a_p^2}c_2+
                  \frac{2p^3}{a_p^3}c_3\pmod{p^4},\\
J_T'(0)&\equiv
 \frac p{\alpha a_p}d_1-\frac{p^2}{\alpha^2a_p^2}d_2+
                  \frac{2p^3}{\alpha^3a_p^3}d_3\pmod{p^4}.
\end{aligned}}
\tag{7}
$$
因此两个原完整中央导数同时为零，严格迫
$$
\boxed{
\mathfrak C_S:=a_p^2c_1-pa_pc_2+2p^2c_3=0\pmod{p^3},
}
$$
$$
\boxed{
\mathfrak C_T:=\alpha^2a_p^2d_1-p\alpha a_pd_2+2p^2d_3
=0\pmod{p^3}.
}
\tag{8}
$$
这始终是两条聚合，未拆成六条逐权零。

## 3. 全部角向进位及真实第二权消元

分解全部 $s$ 个角：
$$
\widehat S=\sum_{r=0}^{s-1}w^rS_r(Z),\quad
\widehat H=\sum_{r=0}^{s-1}w^rH_r(Z),\quad Z=w^s,
$$
$$
s_{i,r}=[Z^i]S_r,\qquad h_{i,r}=[Z^i]H_r.
$$
对 $j=0,1,2$ 定义
$$
\boxed{
W_j=\sum_{r=1}^{s-1}\ \sum_{i+l=j}s_{i,r}h_{l,s-r}.
}
\tag{9}
$$
这些是原固定来源的完整 wrap 数据，不能逐项赋零。
R402 的完整乘积在前三权准确给
$$
\boxed{\begin{aligned}
d_1&=c_1+W_0,\\
d_2&=c_2+c_1h_1+W_1,\\
d_3&=c_3+c_2h_1+c_1h_2+W_2 .
\end{aligned}}
\tag{10}
$$
(9) 中全部系数的物理次数小于 $3s<p$，所以均整。

**定理1。** 若两个完整中央导数同时失败，则
$$
c_1\in p\mathcal O,\qquad W_0\in p\mathcal O,
$$
并且在同一第二精度下准确有
$$
\boxed{
\alpha a_p\,\overline{W_0/p}
 +(\alpha-1)\bar c_2-\bar W_1=0 .
}
\tag{11}
$$
特别 $\alpha-1=19/17$ 是整个 (1) 的单位，
故旧第二中央系数的模 $p$ 值由实际 wrap 数据唯一确定。

保留第三精度，令
$$
D_p=a_p\alpha(\alpha-1)+p(2-\alpha)h_1\in\mathcal O^\times.
$$
则更准确地
$$
\boxed{
c_2\equiv
\frac{\alpha a_pW_1-\alpha^2a_p^2(W_0/p)
      -2pW_2-2p(1-\alpha^2)c_3}{D_p}
\pmod{p^2}.
}
\tag{12}
$$

**证明。** (8) 模 $p$ 先给 $c_1=0$、$d_1=0$，
再由 (10) 得 $W_0=0$ 模 $p$。
把 (10) 代入 $\mathfrak C_T-\alpha^2\mathfrak C_S$。
从第一条 (8) 可合法代入
$$
c_1=\frac p{a_p}c_2-\frac{2p^2}{a_p^2}c_3\pmod{p^3}.
$$
全部 $h_j$ 整，故余式准确为
$$
\begin{aligned}
0\equiv{}&
\alpha^2a_p^2W_0-p\alpha a_pW_1+2p^2W_2\\
&+pa_p\alpha(\alpha-1)c_2
+p^2(2-\alpha)c_2h_1
+2p^2(1-\alpha^2)c_3
\pmod{p^3}.
\end{aligned}
\tag{13}
$$
此处 $2p^2c_1h_2$ 是在已得 $c_1\in p\mathcal O$ 后才消去的。
除以 $p$，先约化模 $p$ 得 (11)，保模 $p^2$ 得 (12)。
$19$ 为普通素数，故 $\alpha-1$ 在惰性范围为单位。$\square$

(12) 保留旧 $c_3$、两个来源的全 wrap 和 $h_1$。
它没有证明第二权为零，也没有删除任何非中央角。

## 4. 两条来源共用同一个 A0 和第三坐标

将 R385 模型相容运输到 $b=1$，记为 $g^\sharp$。
R394 已支付这个 Weierstrass 同构的完整源、目标和 Gaussian 运输。
保持同一个实际低轴
$$
A_0=[p^{-2}\log(g/g^\sharp)]_{<s}\in t\mathcal O[t]_{<s},
$$
以及原第三坐标 $\epsilon^{[3]}$、全部 $U_0/G_0$ 和十三行。
R385 的强普通窗给
$$
g/g^\sharp\equiv1\pmod{p^2,w^{5s-1}}.
$$
因此定义有限模型
$$
\widehat S^\sharp=\frac{g^\sharp}{1+8t}f,\qquad
\widehat T^\sharp=
 \left(\frac{g^\sharp}{1+8t}\right)^\alpha fV,\qquad
\widehat H^\sharp=
 \left(\frac{g^\sharp}{1+8t}\right)^{19/17}V .
\tag{14}
$$
这些有限幂只计算同一真实来源的系数。
在完整原三块中，$S$ 的低轴修正是 $p^2A_0$，
$T$ 的修正准确是 $\alpha p^2A_0$，不是另一份自由的低轴。

记 $\mathfrak C_S^\sharp,\mathfrak C_T^\sharp$
为 (8) 以 (14) 系数计算的两个基准。则
$$
\boxed{\begin{aligned}
\mathfrak C_S
&=\mathfrak C_S^\sharp+
 p^2a_p^2[w^s](A_0\widehat S^\sharp)\pmod{p^3},\\
\mathfrak C_T
&=\mathfrak C_T^\sharp+
 p^2\alpha^3a_p^2[w^s](A_0\widehat T^\sharp)\pmod{p^3}.
\end{aligned}}
\tag{15}
$$
原因是 $c_1,d_1$ 需要模 $p^3$，
$c_2,d_2$ 只需要模 $p^2$，第三权只需要模 $p$。
两条角因子都从 $w$ 起，故第一权只读取低于 $w^s$ 的径向修正；
没有添加原三块以外的末行。
R385 的 $B_1^\sharp=0$ 与同一个 $C_0$ 同时用于两条式。

在完整同时失败的假设下，两个基准先各属于 $p^2\mathcal O$。
置
$$
B_S=\overline{\mathfrak C_S^\sharp/(p^2a_p^2)},\qquad
B_T=\overline{\mathfrak C_T^\sharp/(p^2\alpha^3a_p^2)}.
$$
得到真正的两条有限条件
$$
\boxed{\begin{aligned}
B_S+[w^s](\bar A_0\widehat S^\sharp)&=0,\\
B_T-B_S+[w^s]\{\bar A_0\widehat S^\sharp
                              (\widehat H^\sharp-1)\}&=0 .
\end{aligned}}
\tag{16}
$$
所有括号在这里约化模 $p$。
尤其第二式保留的是两个基准之差；没有把它设为零。

## 5. 新的单位第二顶行

先给一个特征零的准确系数。
由原 Weierstrass 微分方程，
$$
[z^6]\log(\sigma/z)=1/210.
$$
R398 的实际 sigma 比值于是给
$$
\begin{aligned}
[w](H-1)
&=\frac{(3\delta)^6-1+4^6-2^6}{210}\\
&=-\frac{1118}{15}
=-\frac{2\cdot13\cdot43}{15}=:\beta_H .
\end{aligned}
\tag{17}
$$
也可从 (2)、$\Theta=1-2w/15+\cdots$、
$t=-w-3w^2/7+\cdots$ 逐项核定。
两个来源的首部准确为
$$
S=w-\frac{988}{105}w^2+\cdots,\qquad
T=w-\frac{2938}{35}w^2+\cdots .
$$
$13$、$43$ 都是普通素数；故 $\beta_H$ 在整个 (1) 为单位。
当前所读的项在 $w^s$ 之前，Gaussian 不改变 (17)。

令
$$
\eta_k^S=[w^s]\{t(w)^k\widehat S^\sharp\},\qquad
\eta_k^\Delta=[w^s]\{t(w)^k\widehat S^\sharp
                               (\widehat H^\sharp-1)\},
\quad1\le k<s .
$$
从实际首阶，而非抽象角空间，得到
$$
\boxed{
\eta_{s-1}^S=(-1)^{s-1},\quad
\eta_{s-1}^\Delta=0,\quad
\eta_{s-2}^\Delta=\beta_H(-1)^{s-2}.
}
\tag{18}
$$
因此 (16) 读取 $\bar A_0$ 的两个最高系数时，
有一个单位三角子式。

进一步接原 R388/R390 的同一 forcing：
$$
\mathscr L\bar A_0=\mathcal R\bmod t^s,\qquad
\mathscr L=6t^2(1-t)\partial_t^2+t(5-8t)\partial_t.
$$
记 $d_k=k(6k-1)$、$u_{k+1}=2k(3k+1)$。
对两个实际权分别作唯一有限反向递推
$$
q_s^\nu=0,\qquad
d_kq_k^\nu-u_{k+1}q_{k+1}^\nu=\eta_k^\nu,
\quad \nu\in\{S,\Delta\}.
\tag{19}
$$
全部 $d_k$、$1\le k<s$ 是单位。
真正的 (16) 因而等价于
$$
\boxed{
B_S+\sum_{k=1}^{s-1}q_k^S\mathcal R_k=0,\qquad
B_T-B_S+\sum_{k=1}^{s-1}q_k^\Delta\mathcal R_k=0 .
}
\tag{20}
$$
因为 $s=1/6$ 于 $k$，
$$
d_{s-1}=5,\qquad d_{s-2}=22.
$$
所以两个 forcing 测试的最高三角对角准确为
$$
\boxed{
q_{s-1}^S=\frac{(-1)^{s-1}}5,\qquad
q_{s-1}^\Delta=0,\qquad
q_{s-2}^\Delta=\frac{\beta_H(-1)^{s-2}}{22}.
}
\tag{21}
$$
在已付全模型范围 $p>83$，这是统一的单位二阶子式。
这比旧一条中央观察确实多出一条独立有限测试；
它不是指定的 forcing 值已经非零的证明。

两条测试还可直接用 R390 的同一全局转置：
令
$$
H_\nu=(y/x^2)\sum_{k=1}^{s-1}q_k^\nu t^{-k}.
$$
则
$$
\sum q_k^\nu\mathcal R_k
=\frac{17}{3}\sum_{P\in E[2]\setminus O}
 \operatorname{Res}_P\{H_\nu Q_3-(DH_\nu)K_2\}\,dz.
\tag{22}
$$
这里准确六重参数的 $17/3$、全部二挠主部、原 $Q_3,K_2$
及基准保持不变。
(21) 不是允许把这些全局残数逐点赋零的理由。

## 6. 加入 T 的真实有限来源矩阵

新增来源也能放入同一个原第三精度目标，而不用任意添角列。
设旧 canonical 第 $n$ 层的原角多项式为 $F_{n,k}(t)$，
含全部 $P_{134}$，真实旧 charge 为 $N=n+40$。
只取实际来源
$$
\mathcal C_{n,k}\,T^j,\qquad j\ge0
$$
的任意有限集合，仍按原有关系计算其像。
它们的整数 theta 幂是 $17N+36j$，
相对旧 degree34 的 charge 是
$$
N+\alpha j .
$$
在同一个目标中的完整模型是
$$
\boxed{
\left(\frac{g^\sharp}{1+8t}\right)^{N+\alpha j}
 F_{n,k}(t)\{f(t)V(t)\}^{j}
 e_2((N+\alpha j)a_p\epsilon^{[3]}).
}
\tag{23}
$$
因为 $17(N+\alpha j)$ 是整数，这确是原代数来源；
有限模型中的 $\mathbf Z_p$ 幂仅是其计算方法。
(23) 没有倒置 $T$ 或 $H$。
$T^j$ 自带的 $w^j$ 零也原样保留，未另作免费目标移位。

R380/R385 的逐块精度证明对 (23) 逐列适用。
记总 Euler 作用为
$$
\mathcal E_{\rm tot}\bigl(\mathcal C_{n,k}T^j\bigr)
=(n+40+\alpha j)\mathcal C_{n,k}T^j .
$$
则同一物理目标中
$$
\boxed{
M^{\rm orig}P-M^\sharp P
=p^2\bar A_0\,\bar M^\sharp(\mathcal E_{\rm tot}\bar P)
\pmod{p^3}.
}
\tag{24}
$$
公共 $G_0=w^{13}U_0$、全部十三行、混合次数、
实际首次提升像以及固定模 $p^2$ 的同一个 $P_2,\lambda_2$ 均保持。
不要求 $\mathcal E_{\rm tot}$ 保持 $K_2$。
(24) 只给实际有限矩阵和真正第二 Bockstein 的完整比较，
不会由 $J_T'=0$ 推出 $J_{\mathcal C_{n,k}T^j}'=0$。

## 7. 两个基准与规范协变不能删

R392 允许的变更 $\widetilde H_1\mapsto\widetilde H_1+pC$
使
$$
\bar A_0\mapsto\bar A_0-34C,\quad
\widehat S^\sharp\mapsto\widehat S^\sharp(1+34p^2C),\quad
\widehat T^\sharp\mapsto\widehat T^\sharp(1+72p^2C).
$$
因此
$$
B_S\mapsto B_S+34[w^s](C\widehat S^\sharp),\qquad
B_T\mapsto B_T+34[w^s](C\widehat T^\sharp).
\tag{25}
$$
(16) 的两条完整左边同时不变。
相应地，(24) 的基准第二障碍与低轴修正准确相消，
仍是同一个原 $C_2$ 类。

特别，R392 可以选择规范将整个 $\bar A_0$ 消入模型。
此时 (20) 的 forcing 项不再显现，但两个真实基准条件仍然存在。
所以 (21) 的单位子式只是两条真实中央测试的原始性；
不能把它与可吸收的 forcing 单独相乘就宣布原中央非零。

当前新增的合法输入是两个固定 rank-two 曲线同时失败时的
(8)、(11)–(13)、(16)、(20)。
它们共享真实同一来源模型和同一个 $A_0$，而不是两份任意函数。
下一步仍须将完整两基准或其中一条规范不变组合接到
实际 $K_2/C_2$ 配对，或证明其中一个完整中央聚合非零。

## 依赖与同步

- [R398](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)：
  两条实际来源、精确 sigma 乘子、物理缩放及新曲线秩恰二。
- [R402](R402-e24-inert-analytic-half-factor-full-selmer-and-joint-carry.md)：
  新来源完整惰性半因子、全部通常 Selmer 桥、尾界及全角乘法。
- [R382](R382-original-third-central-aggregate-and-full-third-precision-model.md)、
  [R385](R385-original-zero-resonance-and-strong-whole-theta-second-lift.md)：
  同一普通整窗、完整第三中央聚合、准确坐标及强 theta 模型。
- [R388](R388-original-second-quotient-global-forcing-and-first-resonance.md)、
  [R390](R390-original-second-obstruction-adjoint-and-fixed-two-torsion-boundary.md)：
  指定 forcing、有限伴随和全部固定残数转置。
- [R392](R392-original-third-precision-without-extra-poles-and-gauge-covariance.md)、
  [R394](R394-original-second-quotient-cartier-scalar-and-exact-scale-law.md)：
  整提升、Weierstrass 尺度及完整基准加修正的协变。

本文不扫描目标素数，不增加未经识别的 theta 来源。
执行环境不可用期间按根规矩用小文本 API 保存；没有将 API 同步称为 git pull。
