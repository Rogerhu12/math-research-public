# R293：原中心特征类、全部有界 Tor 与无主化分母的 Stark 表达

日期：2026-11-13。**状态：以下实际辅助类构造、整单位格、完整 Tor 与 Rubin–Stark 公式已证明。**

这是 R286 的互补情形。仍用原完整类群模 $A=\mathcal A_p$ 和严格 MW 满射 $\lambda:A\to\mathbf Z_p$。若 $\lambda(A[\theta])\ne0$，可让辅助素数实现一个真正的 $\theta$-特征类。这样原整单位格中只剩一个有界指数的差别；中心 Tor 的两个循环因子、对应的原主化单位以及完整 Stark 值理想都可准确写出。

本篇不要求 $\lambda$ 在该类上取单位值。其非原始指数 $d>0$ 的全部影响均保留。完整值理想损失 $p^d$，特定两条 Bockstein 行损失 $p^{2d}$；这两种损失不相同。

## 1. 原对象与固定的中心特征类

曲线、素数、$\pi$ 塔、直接字符、固定 $\mathcal T=\{(67)\}$ 均同 R286。写
$$
\theta=T-p,\quad \Lambda=\mathbf Z_p[[T]],\quad
\omega_n=(1+T)^{p^{n-1}}-1,
$$
$$
R_n=\Lambda/(\omega_n),\quad
S_n=R_n/\theta R_n\simeq\mathbf Z_p/p^n,
\quad A_n\simeq A/\omega_nA.
\tag{1}
$$
最后一项是 R32 §5 的原完整类群准确控制，包含有限 $A_{\rm tor}$。仍令
$$
D=A/\theta A,\qquad
\lambda:D\twoheadrightarrow\mathbf Z_p,\qquad N=\ker\lambda.
$$
本篇假设并定义
$$
\boxed{\quad \lambda(A[\theta])=p^d\mathbf Z_p\ne0.\quad}\tag{2}
$$
$d$ 仅指本篇的 socle 指数，不是 R35 在饱和以前使用的指数。选择一个固定 $c\in A[\theta]$，使 $\lambda(c)=p^d$。这是完整原类群逆极限中的实际元素。

记 $c_n$ 为它在 $A_n$ 的像。因为 $\theta c=0$，$\omega_n c=\omega_n(p)c$，故 $c_n$ 被 $p^n$ 杀。对 $n>d$，$\lambda_n(c_n)=p^d$ 在 $S_n$ 中的阶为 $p^{n-d}$。因此可唯一写
$$
\boxed{\quad
\operatorname{ord}(c_n)=p^{n-r_n},\qquad 0\le r_n\le d.
\quad}\tag{3}
$$
这里不假设 $r_n=0$，也不假设它不随层数改变。它已经包括有限类群格和 $A_{\rm tor}$ 可能造成的影响。

### 1.1 Chebotarev 实现原完整类

R35 的 Hilbert／射线类域构造同样可用于指定 $c_n$，而不只用于指定 $\lambda_n$ 的值。取原类域的 $\widetilde\chi$ 商，使其在 $K_n$ 上的 Galois 群为 $A_n$。该商的核在 $\operatorname{Gal}(K_n/K)$ 下稳定，故所得扩张对 $K$ 为 Galois。

选 Galois 元 $c_n$，再用 Chebotarev 选 $\mathfrak q$ 的 Frobenius 共轭类，并选合适的上方素位 $w$。其在 $\operatorname{Gal}(K_n/K)$ 中的像为一，所以 $\mathfrak q$ 完全分裂于 $K_n/K$；同时
$$
c_w=e_{\widetilde\chi}[w]=c_n.
\tag{4}
$$
可避开任意指定有限素数集。若改变上方素位，$c_n$ 被 Galois 作用乘以 Tate 中心的单位，故 (3) 及下面的全部指数不变。这是在原完整类群中选择，不以另一个有限表示代替 $c_n$。

## 2. 原主化单位给一个有界指数的整格

以下固定 $n>d$ 及 (4) 的辅助素位，略去部分下标。原单位列是
$$
0\longrightarrow U_0\longrightarrow W
\xrightarrow{v_w}R\xrightarrow{r\mapsto rc_n}A_n.
\tag{5}
$$
$W$ 和 $U_0$ 都是原全局 $S,\mathcal T$ 单位的 $p$-完备化字符格。

由于 $\theta c_n=0$，$R c_n$ 是阶为 $p^{n-r_n}$ 的循环 $S_n$-模，故
$$
\boxed{\quad
I:=\operatorname{Ann}_R(c_n)
=(\theta,p^{n-r_n})R.
\quad}\tag{6}
$$
特别地，(5) 给出真实的原 $S$-单位
$$
\boxed{\quad
v_w(s)=\theta,\qquad v_w(t)=p^{n-r_n}.
\quad}\tag{7}
$$
这些单位属于完整的全局完成格，而不是只在一个局部完成中选出的根。$s,t$ 不要求跨不同辅助素数作非规范的相容选择。

因为 $\theta$ 为非零因子，$Rs\cap U_0=0$；再由 (6)，
$$
\boxed{\quad
0\longrightarrow U_0\oplus Rs
\longrightarrow W
\longrightarrow\mathbf Z/p^{r_n}\mathbf Z
\longrightarrow0.
\quad}\tag{8}
$$
右端带 $T=p$ 的作用。证明是商去 $U_0$ 后将它识别为 $I/\theta R=p^{n-r_n}S_n$。所以这个原单位格的缺陷精确为 $p^{r_n}$，且 $r_n\le d$；没有把它当作自由直和而略去。

## 3. 两条整泛函的统一缩放

令 $\mathcal L_n$、$b_p$ 与 R36 相同。原 Kummer–Artin 互反式仍对任意完全分裂的辅助素数成立：
$$
c_R e_n(\mathcal L_n(u))
+t_{R,w} e_n(v_w(u))=0\qquad(u\in W),
\tag{9}
$$
其中可取一个已知点使 $c_R$ 为 $p^{b_p}$ 乘一个单位。

由 (6)，$e_n(I)=p^{n-r_n}S_n$，故 $p^d e_n(v_w)=0$。将 (9) 乘 $p^d$，得到两条准确的整泛函
$$
\boxed{\quad
g_d=\frac{p^d v_w}{\theta},\qquad
f_d=\frac{p^{b_p+d}\mathcal L_n}{\theta},\qquad
g_d,f_d\in\operatorname{Hom}_R(W,R).
\quad}\tag{10}
$$
这里同时缩放局部行；不能只给赋值行乘 $p^d$，然后保留未经证明在新 $W$ 上整的原局部行。

为了准确计算 (10) 的中心核，定义一个整群环元素
$$
\mathscr B_n(T)=\frac{p^n}{\theta}\in R_n.
\tag{11}
$$
它的多项式代表可明确写成
$$
\mathscr B_n(T)
=-\frac{p^n}{\omega_n(p)}
\frac{\omega_n(T)-\omega_n(p)}{T-p}.
\tag{12}
$$
该代表次数为 $p^{n-1}-1$、最高系数为单位，且
$$
\theta\mathscr B_n=p^n\quad\text{于 }R_n,
\qquad
v_p(\mathscr B_n(p))=n-1.
\tag{13}
$$
由 (6)–(7)，
$$
\boxed{\quad
J_d:=g_d(W)
=p^dR+p^{d-r_n}\mathscr B_nR,
\quad g_d(s)=p^d,\quad
g_d(t)=p^{d-r_n}\mathscr B_n.
\quad}\tag{14}
$$
因为 $n>d\ge r_n$，$e_n(J_d)=p^dS_n$。

## 4. 全部中心 Tor 的两个循环因子

由 $0\to U_0\to W\to J_d\to0$ 及 $J_d$ 上 $\theta$ 的单射性，中心核为
$$
0\longrightarrow U_0/\theta U_0
\longrightarrow\ker\bar g_d
\longrightarrow\mathcal T_{n,d}\longrightarrow0,
$$
$$
\mathcal T_{n,d}
=\frac{J_d\cap\theta R}{\theta J_d}
\simeq(R/J_d)[\theta].
\tag{15}
$$
这是新缩放行的准确 Tor；它不把 R286 对原 $\lambda(c_w)$ 为单位的辅助类所保留的 $(I\cap\theta^2R)/(\theta I)$ 置零。一般两者所用的辅助类和缩放均不同。

**准确结构为**
$$
\boxed{\quad
\mathcal T_{n,d}\simeq
\mathbf Z/p^{d-r_n}\mathbf Z
\oplus
\mathbf Z/p^{r_n}\mathbf Z.
\quad}\tag{16}
$$
它可能不是循环群；总长度恰为 $d$，与 $n$ 无关。

证明如下。若 $d=0$，(14) 给 $J_d=R$，结论显然。设 $d>0$，令 $R^{(d)}=R/p^dR$。$\theta$ 在这个有限群上的余核是 $\mathbf Z/p^d$，故其核也有阶 $p^d$。由 (12) 的最高系数为单位，$\mathscr B_n$ 模 $p^d$ 有阶 $p^d$；(13) 说明它被 $\theta$ 杀掉。因此
$$
R^{(d)}[\theta]=\mathbf Z_p\mathscr B_n.
\tag{17}
$$
因 $n-1\ge d$，$\mathscr B_n(p)\in p^d\mathbf Z_p$，所以 $\mathscr B_n\in\theta R^{(d)}$。定义整多项式
$$
\beta_n=\frac{\mathscr B_n(p)}{p^d}\in\mathbf Z_p,
\qquad
Y_n(T)=\frac{\mathscr B_n(T)-\mathscr B_n(p)}{T-p}.
\tag{18}
$$
于是 $\theta Y_n=\mathscr B_n-p^d\beta_n$，在 $R^{(d)}$ 中即为 $\theta Y_n=\mathscr B_n$。

由 (14)，
$$
R/J_d=R^{(d)}/\mathbf Z_p\bigl(p^{d-r_n}\mathscr B_n\bigr).
$$
这个商的 $\theta$-核由 $\mathscr B_n$ 和 $p^{d-r_n}Y_n$ 的像生成。前者阶为 $p^{d-r_n}$，后者阶为 $p^{r_n}$。若后者的某个整数倍落在前者张成的子群，在 $R^{(d)}$ 中乘 $\theta$ 就迫使该整数被 $p^{r_n}$ 整除，故该倍本来为零。这证明两者的和为直和，得到 (16)。

### 4.1 Tor 的实际原主化单位代表

在 (15) 的连接同构中，$r\bmod J_d$ 映到 $\theta r\bmod\theta J_d$。由 (7)、(14)、(18)，(16) 的两条生成元因此可分别用
$$
\boxed{\quad
u_1=p^{n-d}s,
\qquad
u_2=t-p^{d-r_n}\beta_n s
\quad}\tag{19}
$$
代表。确实，
$$
g_d(u_1)=p^n=\theta\mathscr B_n,
\qquad
g_d(u_2)=\theta p^{d-r_n}Y_n.
$$
它们都在 $\ker\bar g_d$ 中，其模 $U_0/\theta U_0$ 的阶分别为 (16) 的两个准确指数。

因此若 $\mathfrak a_f=\bar f_d(U_0)$，Tor 对局部行的全部额外贡献由两个实际值
$$
\boxed{\quad
p^{n-d}\bar f_d(s),\qquad
\bar f_d(t)-p^{d-r_n}\beta_n\bar f_d(s)
\quad\bmod\mathfrak a_f
\quad}\tag{20}
$$
生成。换主化单位只改变模 $\mathfrak a_f$ 已消去的部分。每个 $\bar f_d$ 值还可按 R286 (25) 的多项式整除式计算，把其中的 $b_p$ 换为 $b_p+d$，并保留 $\omega_n'(p)$ 修正。这给出完整实际观察，不留下未定义的“忽略有限 Tor”步骤。

## 5. 原 Rubin–Stark 元素确实消去主化分母

仍保持 BKS 的位置顺序 $[\infty,\mathfrak q]$。原公式为
$$
\epsilon_{2,n,w}=\frac{u_n}{h}z_n\wedge z_w,
\qquad v_w(z_w)=h.
\tag{21}
$$
本篇并不省略 $h$；(7) 实际提供了另一个主化单位，给出准确等式
$$
\boxed{\quad
\epsilon_{2,n,w}
=u_n\left(\frac{z_n}{\theta}\right)\wedge s.
\quad}\tag{22}
$$
证明先在 $B_n=\mathbf Q_p\otimes R_n$ 上演算：$z_w-(h/\theta)s$ 的赋值为零，所以属于 $B_n\otimes U_0$；后者为秩一，而 $z_n$ 也在其中，故它与 $z_n$ 的外积为零。这就将 (21) 变为 (22)。右边的 $z_n/\theta$ 已由原整单位记录证明属于 $U_0$，$s$ 属于原 $W$，所以 (22) 把该 Rubin–Stark 元素写成实际普通外积的像：经自然映射 $\bigwedge_R^2W\to\bigcap_R^2W$，右边映到左边。不要求普通外积本身没有 $\mathbf Z_p$-挠，也不以有理外积中的形式相等替代这两个元素的整性。

原局部系数为 $\mathcal L_n(z_n)=\theta^2G_{p,n}$。由 (10)、(14)、(22)，
$$
\boxed{\quad
(f_d\wedge g_d)(\epsilon_{2,n,w})
=p^{b_p+2d}u_n G_{p,n}.
\quad}\tag{23}
$$
中心值按 R35 的同一明确单位为
$$
e_n\bigl((f_d\wedge g_d)(\epsilon_{2,n,w})\bigr)
=-\frac{p^{b_p+2d}}{1+i}\,G_p(p)\pmod{p^n}.
\tag{24}
$$
全部 $p^d$、$h$、中心单位及符号均已支付。

## 6. 完整值理想只损失 $p^d$，并保持原 Sha 判据

记 $\mathcal J_{n,w}$ 为 (21) 在全部整泛函外积下的值理想。R35 §4.1 的已出版 BKS 定理对这里的辅助素数同样给
$$
\mathcal J_{n,w}=\operatorname{Fitt}_{R_n,0}(A_n/R_nc_n).
\tag{25}
$$
该完整理想等式不要求 $\lambda_n(c_n)$ 是单位。

令 $\bar c\in D$ 是固定 $c$ 的中心像，置 $Q=D/\mathbf Z_p\bar c$。由准确控制 (1)，
$$
\boxed{\quad
(A_n/R_nc_n)/\theta\simeq Q/p^nQ.
\quad}\tag{26}
$$
利用 $\lambda(\bar c)=p^d$，有准确整数正合列
$$
\boxed{\quad
0\longrightarrow N\longrightarrow Q
\longrightarrow\mathbf Z/p^d\mathbf Z\longrightarrow0.
\quad}\tag{27}
$$
证明可取 $D\simeq\mathbf Z_p\oplus N$，写 $\bar c=(p^d,c_N)$；$N\cap\mathbf Z_p\bar c=0$，而对第一坐标取模 $p^d$ 就给出 (27)。没有假设 $c_N=0$。

若 $N$ 有正自由秩，$N,Q$ 的第零整数 Fitting 理想都为零；若 $N$ 有限，(27) 给 $|Q|=p^d|N|$。所以对所有情形，
$$
\operatorname{Fitt}_{\mathbf Z_p,0}(Q)
=p^d\operatorname{Fitt}_{\mathbf Z_p,0}(N).
$$
经 (25)–(26) 作准确基变换，再用 R35 的原第一 Fitting 中心比较，得到
$$
\boxed{\quad
e_n(\mathcal J_{n,w})
=p^d\operatorname{Fitt}_{S_n,0}(N/p^nN)
=p^d e_n\bigl(\operatorname{Fitt}_{R_n,1}(A_n)\bigr).
\quad}\tag{28}
$$
这是完整中心理想只损失 $p^d$ 的准确公式。它与特定两行的 (23) 所含 $p^{2d}$ 不相同，不能将两者混写。

按 R34–R35，$\operatorname{rank}_{\mathbf Z_p}N=q_p-1$ 正是原 Sha 的余秩。因此在本篇的分支 (2) 下，
$$
\Sha(E/\mathbf Q)[p^\infty]\text{ 有限}
\quad\Longleftrightarrow\quad
\exists n>d:\ e_n(\mathcal J_{n,w})\ne0.
\tag{29}
$$
若 $N$ 有限，首次非零的精度准确为 $n>d+\operatorname{length}_{\mathbf Z_p}N$；若 $N$ 有正秩，全部中心值理想仍为零。辅助类的选择与有界 Tor 并未删除这部分自由方向。

## 7. 原单位指数在这组整格中的准确位置

令 $w_n=z_n/\theta\in U_0$，并记其完整评价理想为
$$
\mathcal I(w_n)=
\langle\varphi(w_n):\varphi\in\operatorname{Hom}_R(U_0,R)\rangle_R.
$$
由 (8)、(22)，总有准确包含
$$
\boxed{\quad
p^{r_n}u_n\mathcal I(w_n)
\subset\mathcal J_{n,w}
\subset u_n\mathcal I(w_n).
\quad}\tag{30}
$$
右包含由任意两条整泛函在 (22) 上的行列式直接得到。为证左包含，注意 $I$ 是自由 $\mathbf Z_p$-格；对称群环的迹配对给
$$
\operatorname{Ext}^1_R(I,R)
\simeq\operatorname{Ext}^1_{\mathbf Z_p}(I,\mathbf Z_p)=0.
$$
因此 (5) 的对偶说明每个 $\varphi:U_0\to R$ 都可整地延拓到 $W$。另一方面，$p^{r_n}v_w/\theta$ 在 $W$ 上整，并在 $s$ 上取值 $p^{r_n}$。将这两条实际整行代入 (22)，即得 $u_np^{r_n}\varphi(w_n)$，证明左包含。这里没有假定所有任意中心泛函可免费提升；提升是在原整 $R$-格上先证明的。

当 $d=0$ 时 $r_n=0$，(8) 为真正直和，(15) 的 Tor 为零，而且
$$
\mathcal J_{n,w}=u_n\mathcal I(z_n/\theta).
\tag{31}
$$
当 $d>0$ 时，(16)、(19) 给出全部额外中心方向，(30) 保留准确的有界指数。由此，R286 的两种情形已分别得到一个实际第二全局除点或这一组有界 Tor 的原主化表达。余下的算术问题确实仍是原单位 $z_n/\theta$ 的评价理想在中心是否非零，而不是缺少辅助素数、主化分母或未计入的 Tor。

## 8. 有限群环的独立整格核验

脚本 [check-central-eigenclass-bounded-tor.py](../scripts/check-central-eigenclass-bounded-tor.py) 与同名 JSON 对 14 组 $(p,n,d,r)$ 作准确整数 Smith 运算，包含 $(p,n,d)=(3,4,3)$ 的全部 $0\le r\le3$。计算使用真正的 $\mathbf Z_p[\Gamma_n]$，并在 $T$ 的完整 $p^{n-1}$ 维基上计算 $\theta$；没有把有限群环换成截断对偶数环。

脚本独立计算 $R/J_d$ 上 $\theta$ 的全核阶，再计算 (17)–(18) 两个实际生成元的阶和合成子群的阶；14 组均验证 (16)，并核 (6) 的余商长度及 (12)、(18) 的准确多项式恒等式。这里 $p=3,5$ 仅为有限环代数检验，不是本课题曲线的新算术素数证书。一般证明在 §4，计算未替代该证明。

## 依赖

- R32、R35：原完整类群控制、Chebotarev、准确原单位列、完整 BKS 值理想及单位 $u_n$。
- R36：两条已知 MW Kummer 互反行、局部 Coleman 坐标和 $b_p$。
- R286：原 socle 与中心 Tor、原主化观察及严格区分完整类群与 MW 子空间。
- [O6 整单位记录](../notes/2026-11-13-o6-integral-unit-division-and-one-prime-mrs-descent.md)：$z_n/\theta$ 的全局整性、对称群环双对偶与范数相容。
