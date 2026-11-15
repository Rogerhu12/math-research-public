# 原 Robert 单位的实际 Shapiro 二阶类与唯一全局低阶 gauge

日期：2026-11-15。专属研究笔记。本文补上
[平衡二阶笔记](2026-11-15-ordinary-balanced-second-jet-reciprocity.md)
§6 第一项的实际 Kummer/Shapiro 来源：从同一个原 $c_s$ 构造一个真正
$\Sigma$ 支持的变形上同调类，证明其低两阶可在全局唯一杀零，并确定
所得二阶类就是该笔记的完整 $\mathcal K$。没有构造另一侧的
exact-dual lift，没有求出 $\Theta$，也不提出巨大 $q$ 挠点枚举。

原 $q$、$\gamma$、$s$、$P_+$、$s^{11}$ 移位、CM/Weil 标架、算术
Frobenius 及支持 $\Sigma=\{2,43,q,\infty\}$ 全部保留。

## 1. 系数模、域与正群环作用

记
$
p=43,\quad k=\mathbf F_{43}[i],\quad
G_K=G_{K,\Sigma_K},\quad F=\mathscr F,\quad V=F_sL_q,
\qquad Q=\operatorname{Gal}(V/F)=\Gamma\times S.
$
此处及以下的 Galois 群都只允许在 $\Sigma$ 上方分歧。
令 $D$ 为原 $W(1)|_{G_K}$ 的一维 $k$ 写法。
[R196](../results/R196-cm-reference-bockstein-and-the-actual-norm-field.md)
(196.1) 的实际角色是 $D=\psi^2\bmod p$；
在 $G_F$ 上它就是 $k(1)$。复共轭在这个 $k$ 线上的作用为原
negative conjugation，特别仍满足 $\tau i=-i$，不能改成未标记的
trivial coefficient line。

设 $\kappa_\Gamma,\kappa_S:G_K\to\mathbf F_{43}$ 为原两个有限商的
正坐标：$\gamma,s$ 分别取值 $1$。令
$
\Lambda_n=k[T]/T^n,\qquad
\ell=\kappa_\Gamma+i\kappa_S,\qquad
\theta_n(g)=(1+T)^{\kappa_\Gamma(g)}
             ((1+T)^i)^{\kappa_S(g)}
           =(1+T)^{\ell(g)}
\quad(1\le n\le3).
\tag{1}
$
这里二项式均截断于次数 $n-1$；$2$ 在 $k$ 中可逆，且
$(1+T)^{43}=1$，所以 (1) 是实际角色，不是只到一阶的记号。

本笔记的系数模是
$
M_n=D\otimes_k\Lambda_n^\#,\qquad
g(d\otimes f)=g_Dd\otimes\theta_n(g)^{-1}f.
\tag{2}
$
上标 $\#$ 明确表示 **inverse quotient action**。原单位的正
$\gamma,s$ 作用对应 $\Lambda_n$ 上的正乘法
$
\gamma\mapsto1+T,\qquad s\mapsto(1+T)^i.
\tag{3}
$
它与 Galois 对系数的逆作用是两个不同位置的作用。

## 2. 从实际 $c_s$ 得到显式 Shapiro cocycle

先在 $G_F$ 上工作。对 R613 原 $c_s$ 取 Kummer cocycle
$c\in Z^1(G_V,k(1))$。这是对该单位张量的 Kummer 类：可分别对
系数基 $1,i$ 中的实际单位取 $p$ 次根后线性相加。没有把
completed multiplicative tensor 当作一个字段元素。

固定 $r:Q\to G_F$，$r(1)=1$，作为左陪集代表。对 $g\in G_F$ 及
$a\in Q$ 置
$
h_a(g)=r(a)^{-1}g\,r(\bar g^{-1}a)\in G_V .
$
在 $k(1)\otimes k[Q]^\#$ 中定义
$
\boxed{\;
\mathscr C(g)=
 \sum_{a\in Q}r(a)c(h_a(g))\otimes[a^{-1}],
\qquad
g(m\otimes[b])=gm\otimes[\bar g^{-1}b].
\;}
\tag{4}
$
这就是所用的实际 Shapiro 代表。其 cocycle 符号可直接核验：
$
h_a(g_1g_2)=h_a(g_1)\,h_{\bar g_1^{-1}a}(g_2).
$
代入 $c(h_1h_2)=c(h_1)+h_1c(h_2)$，第二项正好是
$g_1\mathscr C(g_2)$；故 $\delta\mathscr C=0$。

限制到 $G_V$ 后取 $[1]$ 系数，恰得 $c$。更重要的是，系数乘
$[b]$ 后其 $[1]$ 系数是
$
r(b)c(r(b)^{-1}h\,r(b)),
$
正是原单位 $b c_s$ 的 Kummer 类。因此 (4) 在上同调上对原单位
的正 $k[Q]$ 作用线性。若在 (4) 中用 $[a]$ 却仍保持这个正单位
识别，就会反转 $\gamma,s$；本稿没有这样做。

现在沿真实平衡曲线取系数商
$
k[Q]\longrightarrow\Lambda_3,\qquad
\gamma-1\mapsto T,\quad
s-1\mapsto iT+\binom i2T^2.
\tag{5}
$
其 Galois 作用正是 (2)。原 tame $\Delta=\operatorname{Gal}(F/K)$
阶为 $44$，与 $\Gamma,S$ 交换。$c_s$ 已带原未平均 $P_+$；
使用原 $W$ 字符扭转后，所得类对 tame 下降等变。
有限阶 $44$ 的限制同构给出唯一实际类
$
\boxed{\mathscr C_{\rm bal}\in H^1(G_K,M_3).}
\tag{6}
$
如果需要全局 cocycle 而不只这个类，可以对 (4) 再作有限
corestriction，并除以 $44$。其限制是
$44$ 个相同的 tame-equivariant 类，故此除法只实现限制的逆；
它没有把原单位 $P_+$ 改成另一个单位，也没有改变 R185 的未平均
Norm 坐标。所有这些 cochains 保持同一个 $\Sigma$ 支持。

改变 $p$ 次根或陪集代表只改变 coboundary，因而 (6) 是原
$c_s$ 指定的类。实际 $s^{11}$ 移位已经在 $c_s$ 中，(5) 也保留
$\binom i2T^2$，不存在丢掉该 Euler 交叉项的线性替代。

## 3. 在 $p$ 的局部自由性与精确 Norm 基

令 $K_p$ 为原 $K$ 的唯一 $p$ 进完备化，$G_p=G_{K_p}$。
本节是这个域上的断言，不把 $q$ 的不变量情况套到 $p$。

原 tame 字符非平凡，而且 $F_p$ 不含 $\mu_p$。
由 R185/R779 的原局部表示及局部 Tate 对偶，
$
H^0(G_p,D)=0,\qquad
H^2(G_p,D)=H^0(G_p,D^\vee(1))^\vee=0,
\qquad \dim_kH^1(G_p,D)=2.
\tag{7}
$
第二个零使用原 $W$ 的非平凡 tame 作用；不能仅从第一个零推出它。

$M_n$ 的各 $T$-graded pieces 都是 $D$。归纳长正合列得到
$H^0(G_p,M_n)=H^2(G_p,M_n)=0$，以及
$\dim_kH^1(G_p,M_n)=2n$。乘 $T$ 的核为一份 $D$，
故其 $H^2=0$ 又给
$
H^1(G_p,M_n)/T H^1(G_p,M_n)\simeq H^1(G_p,D).
$
任取两个剩余基的提升，Nakayama 给 $\Lambda_n^2$ 的满射；
长度同为 $2n$，所以
$
\boxed{H^1(G_p,M_n)\simeq\Lambda_n^2.}
\tag{8}
$
特别 $T^{n-1}$ 的系数通过
$H^1(G_p,D)\hookrightarrow H^1(G_p,M_n)$ 被唯一识别。

R783 的原半局部单位格为
$\mathcal O[\Gamma,S]e_u\oplus\mathcal O[\Gamma,S]e_q$。
其实际 Norm 标记是
$
N_\Gamma N_Se_u=u,\qquad
N_\Gamma N_Se_q=w_q=P_+[\alpha_F].
\tag{9}
$
$e_q$ 使用任一个满足 $N_Sv_q=w_q$ 的原局部 Norm 原像。
$u,w_q$ 的 Kummer 类就是原 $u=i\,d_0$ 与 $d_q$。
它们在 R185 两列中的行列式非零。

局部 Mackey/Shapiro、Kummer 和 (5) 给一个
$
\Phi_p:
 (U/pU)\otimes_{k[\Gamma,S]}\Lambda_3
 \longrightarrow H^1(G_p,M_3).
\tag{10}
$
它按 §2 的检查对正群环作用线性。模 $T$ 时是实际 combined
corestriction，即 (9) 的两个 Norm，故两列像为 $u,w_q$。
(8) 及 Nakayama 证明 (10) 是同构。
这里没有在低单位滤层直接取对数，也没有选择任何全局 ordinary
Norm 原像。

由已登记的完整平衡展开，
$
c_s=11(ix-z)e_u+x^2A+xzB-55z^2e_u+I^3U,
$
(5) 后得到真正的局部等式
$
\boxed{\operatorname{loc}_p\mathscr C_{\rm bal}
  =T^2\bigl(K_u[u]+K_q[d_q]\bigr),}
\tag{11}
$
其中
$
\mathcal K=K_u u+K_qw_q
 =A+iB+\left(55+\frac{11(1+i)}2\right)e_u .
\tag{12}
$
(11) 的右侧使用 (8) 的系数嵌入；它不是把同一个原始单位当作
形式幂级数字段值。两个系数仍未知。

## 4. 全局到 $p$ 的单射逐层保留

本节所有全局群仍是 $G_{K,\Sigma_K}$；没有允许新的辅助分歧。

先有
$
H^1(G_K,D)\longrightarrow H^1(G_p,D)
\quad\hbox{单射}.
\tag{13}
$
R743 在 $\mathbf Q$ 上证明完整支持空间为
$\mathbf F_p d_0\oplus\mathbf F_p d_q$，且 R185 两个局部像独立。
把任意 $K$ 上核中的类 $v$ 写为
$
v=\frac{v+\tau v}{2}
  +i\,\frac{v-\tau v}{2i}.
$
两个括号中的类都对原 semilinear $\tau$ 不变，局部也为零。
阶 $2$ 与 $p$ 互素的下降及 R743 的单射迫二者都为零。
这证明 (13)，并且保留 negative conjugation 的原意义。

**引理。** 对 $1\le n\le3$，
$
H^1(G_K,M_n)\longrightarrow H^1(G_p,M_n)
\quad\hbox{单射}.
\tag{14}
$

证明用 $0\to T^{n-1}D\to M_n\to M_{n-1}\to0$ 归纳。
一条局部为零的类先在 $M_{n-1}$ 中全局为零，故来自
$H^1(G_K,D)$。因为 $H^0(G_p,M_{n-1})=0$，
局部 $H^1(D)\to H^1(M_n)$ 单射；于是这个底层类在 $p$ 为零，
再用 (13)。全局的同一 $H^0$ 零也成立，因为其限制到 $G_p$
已为零。证毕。

特别要区分：(14) 不需要假设整个全局 $H^2$ 为零。
局部 $H^2=0$ 是 §3 的自由性/满射输入；全局单射的归纳只用
底层 (13) 和相应 $H^0$。没有从未限制支持的 lift 偷换到
$\Sigma$ 支持的 lift。

## 5. 唯一实际全局二阶类与可写出的 gauge

将 (6) 降到 $M_2$，(11) 使其在 $p$ 为零，(14) 使其全局为零。
再用 $0\to T^2D\to M_3\to M_2\to0$ 以及
$H^0(G_K,M_2)=0$，存在唯一
$
\boxed{
\mathcal K_{\rm glob}\in H^1(G_K,D),\qquad
\mathscr C_{\rm bal}=T^2\mathcal K_{\rm glob}.}
\tag{15}
$
其局部像精确为
$K_u[u]+K_q[d_q]$。这不是在一个不变商中自由选取起点。

也可以在 cochain 层完全杀掉低两项。取 (6) 的任意实际代表
$C=C_0+TC_1+T^2C_2$。原 combined Euler Norm 为零，所以
$[C_0]=0$。因 $H^0(G_K,D)=0$，存在唯一 $a_0\in D$ 使
$C_0=\delta_Da_0$。先减去完整 $\delta_{M_3}a_0$，然后一次系数
成为普通 $D$ cocycle。其 $p$ 局部类由 (11) 为零；(13) 及同一个
$H^0$ 零给唯一 $a_1\in D$ 杀掉它。最后
$
\boxed{
C-\delta_{M_3}(a_0+Ta_1)=T^2 Z,\qquad
\delta_DZ=0,\quad[Z]=\mathcal K_{\rm glob}.}
\tag{16}
$
唯一性是固定 $C$ 后的 $a_0,a_1$ 唯一；二阶 cocycle 仍可随
$C$ 的改变加 coboundary，其类 (15) 不变。

这里的 gauge 还可用原一个非平凡 tame 值明确写出。
取原 $\beta=-1+2i$ 的算术 Frobenius $\sigma$，
则 $D(\sigma)=\beta^2\bmod p\ne1$。
记 $C^{(1)}=C-\delta_{M_3}a_0$，有
$
a_0=(D(\sigma)-1)^{-1}C_0(\sigma),\qquad
a_1=(D(\sigma)-1)^{-1}C^{(1)}_1(\sigma).
\tag{17}
$
(17) 依赖已经证明的全局 exactness，不是通过单个 Frobenius
值猜一个 global primitive。

若写 $\rho_D(g)$ 为原一维角色，则 (16) 的完整二次系数为
$
Z(g)=C_2(g)+\ell(g)\rho_D(g)a_1
                 -\binom{-\ell(g)}2\rho_D(g)a_0 .
\tag{18}
$
它保留逆作用的二次修正。未知的是实际 $C$ 的数值；
(17)–(18) 不宣称这些值已由旧纯 $p$ 算术提供。

## 6. 与原 $d_R$、实下降和 AH 两列的准确比较

[R779](../results/R779-original-real-Robert-class-and-two-p-local-obstruction-coordinates.md)
的原 $n_R$ 已给真实 $\mathbf Q$ 上的 $d_R$。平衡笔记的局部
恒等式及 (13) 把它升级为同一全局类的等式：
$
\boxed{
-i\mathcal K_{\rm glob}+\frac{11i}{2}[u]
    =\operatorname{res}_K d_R,\qquad
\mathcal K_{\rm glob}
    =i\operatorname{res}_Kd_R+\frac{11}{2}[u].}
\tag{19}
$
特别不用另选复共轭相位来下降 $\mathcal K_{\rm glob}$：
右式给其实际 anti-real normalization。
由于 $[u]=i\operatorname{res}_Kd_0$，
$
d_R=\left(K_u-\frac{11}{2}\right)d_0-iK_qd_q,
\qquad
\Theta=-iK_q .
\tag{20}
$
由原实下降，$K_u\in\mathbf F_{43}$、$K_q\in i\mathbf F_{43}$。
原两个 AH 坐标继续为
$
B_1=24\left(K_u-\frac{11}{2}\right)-20iK_q,\qquad
B_{45}=20\left(K_u-\frac{11}{2}\right)-29iK_q.
\tag{21}
$
这些是对真实 Shapiro 二阶类的比较，不是新的数值输出。

## 7. $q$ 的完整杀零 gauge 与仍未知的一次标量

原 $q$ 上 $V/F$ 的 decomposition group 是完整
$\Gamma\times S$：$\Gamma$ 全分歧，$S$ 为 degree-$43$ 未分歧层。
R773 §2 已严格给原 $c_s$ 的全 p-primary residue 为
$\mu_p$ 中的标记相位 $9$；上层剩余群的 p-primary 部分是
$\mu_{p^2}$。由于 residue characteristic 是 $q\ne p$，
principal units 的 $p$ 次幂映射可逆。因此
$
[c_s]|_{G_{V_q}}=0\quad\hbox{in }H^1(G_{V_q},k(1)).
\tag{22}
$
这里只调用 R773 的已证 residue，不重新计算相位 $9$。
Shapiro 及 (5) 从而给
$\operatorname{loc}_q\mathscr C_{\rm bal}=0$。

这不使 $\operatorname{loc}_q\mathcal K_{\rm glob}$ 为零。
在 $K_q$ 上原 $D$ 剩余角色平凡；原 $\Gamma$ 惯性生成元在
$M_3$ 上作用为 $(1+T)^{-1}$。所以
$
H^0(G_{K_q},M_3)=T^2 k,\qquad
H^0(G_{K_q},M_2)=Tk.
\tag{23}
$
正是在这里，§3 用于 $p$ 的 $H^0$ 消失不适用。

对已经完成全局 (16) 的代表，取真正的局部 $0$-cochain $b_q$
使
$
T^2Z_q=\delta_{M_3}b_q.
$
因为其一次系数为零，而 $\ell_q$ 非零，$b_q$ 的常数项必须零。
由 (23)，它具有
$
b_q=T a_q+T^2b'_q,\qquad
a_q\in k\ \hbox{唯一},\qquad
Z_q=-a_q\ell_q .
\tag{24}
$
第二个系数 $b'_q$ 可变，不能据它的自由度改变 $a_q$。

在 R168 的原 $q$ 标架，以 $F_q\otimes\zeta_q$ 表示 $1$、
$K_q\otimes\zeta_q$ 表示 $i$。限制到未分歧二次域 $K_q$ 后，
原 $d_q$ 的 $(16,1)$ 两坐标成为
$
d_q(\varphi_q^2)=32i,\qquad d_q(\tau_q)=1.
$
原 finite quotient 同时满足
$\kappa_\Gamma(\varphi_q^2)=0$、
$\kappa_S(\varphi_q^2)=32$、
$\kappa_\Gamma(\tau_q)=1$、
$\kappa_S(\tau_q)=0$。所以
$
\ell_q=\operatorname{res}_{K_q}(d_q)
\quad\hbox{在这个实际一维 $k$ 标架中}.
\tag{25}
$
这保留了二次限制对 finite 坐标的因子 $2$。
由 $d_{0,q}=0$、(20)、(24)，准确有
$
\boxed{K_q=-a_q,\qquad \Theta=i a_q.}
\tag{26}
$
坏值仍等价于 $a_q=-11i$，不是相位 $9$ 的直接代入。

尤其 (24) 的 $b_q$ 是在**原全局 $a_0,a_1$ 已杀零之后**的
局部 primitive。只为原 $c_s$ 随意选一个局部 $p$ 次根，或者把
(22) 当成一个零 cochain，不能自动得到这个 $a_q$。
它正好记录全局低阶 gauge 与局部杀零 gauge 的剩余差。

## 8. 真正完成的接口与未完成边界

本文给出原 $c_s$ 的实际、受 $\Sigma$ 支持的 Shapiro 类 (4)–(6)，
指定其系数逆作用，证明原全局低阶 gauge 的唯一性，并把其实际
二阶类同 R779 的 $d_R$ 逐规范比较。还在原 $q$ 标架上明确了
完整局部杀零后的唯一一次常数 (24)。

它不把 (4) 的有限定义包装为对 776 位 $q$ 的可行产品算法；
没有实际求出 $C(\sigma)$、$a_0,a_1,a_q$、$K_u,K_q$ 或 $\Theta$。

对 (2) 而言真正 Tate dual 是
$
M_3^\vee(1)
 =D^\vee(1)\otimes\Lambda_3(\theta_3).
\tag{27}
$
此处是 $k$-linear dual。原 trace 配对在相同的 $J$ 左乘结构中为
Hermitian：$\operatorname{tr}(D_zD_w)=\operatorname{Tr}_{k/\mathbf F_p}(z\bar w)$。
所以 $D^\vee_k(1)$ 使用原 $W$ 的**共轭 $k$ 结构**。
在 §7 的 $q$ 标架中，dual 的
$F_q\otimes\zeta_q\mapsto1,\ K_q\otimes\zeta_q\mapsto i$，
而这个 exact primal 的 $F_q\mapsto1,\ K_q\mapsto-i$。
原 $w_q=(27\varepsilon,-\varepsilon)=(-16\varepsilon,-\varepsilon)$
限制到 $K_q$ 后遂为
$-32\varepsilon\,U+i\varepsilon\,T_{\rm tame}
=i\varepsilon\ell_q$。
它有真实的局部 $\theta_n$-lift
$i\varepsilon(\theta_{n+1}-1)/T$；这里 $\theta_{n+1}$ 由同一截断
二项式多取一阶定义，且 $(\theta(gh)-1)=
(\theta(g)-1)+\theta(g)(\theta(h)-1)$ 直接验证 cocycle 方程。
这一局部构造不宣称能够同时满足全局支持及原 strict-$p$ 条件。

因此平衡二阶笔记 §§4–5 的 exact-dual 配对中，本稿原 Robert
类占的是 inverse-character 一侧。另一侧原 primal 类的
$\theta_3$-变形 cocycle 仍须实际构造并保支持；不能把原普通
cocycle 作为常数自动放进去。若再比较 R200 的模 $p^2$ Kummer
参考格，原 cyclotomic reference 修正仍须保留。本文没有用
Shapiro 逆作用抵消那个不同来源的修正，也没有取旧 $24F_0$
代替 $\Theta$。

## 引用

- [R168](../results/R168-tate-frobenius-sunit-slopes-and-weil-squareclasses.md)，§§1–2：原 $q$ 两坐标、Weil 标架与二次限制。
- [R185](../results/R185-p-local-robert-and-principal-unit-coordinates.md)，§§1–2、4：原 $p$ Kummer 基与未平均规范。
- [R196](../results/R196-cm-reference-bockstein-and-the-actual-norm-field.md)，§§1–3：原 $D=\psi^2$、negative conjugation 和正 Artin。
- [R200](../results/R200-second-obstruction-reference-cancellation-and-one-supported-norm-slope.md)，§§2–4：exact Tate dual 与全支持边界。
- [R613](../results/R613-mixed-p-capitulation-and-the-exact-34-boundary.md)，§§2–4：原 $s^{11}$、$c_s$、$\operatorname{Fr}_{K_q}=s^{32}$。
- [R743](../results/R743-original-first-moment-and-the-exact-flat-primal-secondary-slope.md)，§1：完整全局空间与 $p$ 局部化单射。
- [R773](../results/R773-complete-ordinary-scalar-lattice-and-original-mixed-Robert-phase.md)，§2：原混合 Robert 的已证全 residue 与相位。
- [R779](../results/R779-original-real-Robert-class-and-two-p-local-obstruction-coordinates.md)、[R783](../results/R783-canonical-quadratic-Robert-local-coefficient-and-norm-freedom.md)：原实际下降类、局部自由格与规范二次坐标。
