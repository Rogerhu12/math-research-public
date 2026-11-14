# R390：原第二障碍的准确伴随与固定二挠边界

日期：2026-11-14。**状态：已证明。** 本文将 R388 的同一个确定低轴，分别在原完整第二 Bockstein 和中央第三聚合中的作用，写成可直接比较的有限转置。转置后的权是原椭圆曲线上的多项式，因而这项修正只读取三个固定二挠点；没有移动测试点或新的 $x=0$ 残数。全部二挠高主部通过一个明确的 Pascal 整矩阵聚合，不逐项删去。本文保留实际 $P_2,\lambda_2$、首次提升像、公共 $U_0$、十三行及原第三坐标 $C_0$；不把修正项与整个中央值或整个第二障碍混同。

## 1. 同一个原矩阵、低轴和已付 forcing

取
$$
p=6s-1>83,\quad b=17,\quad
1\le\ell<s-13,\quad L=2s+\ell,\quad T=L+13<3s.
$$
沿 R338、R335 使用整个原 canonical 来源
$$
\mathcal V_{\le D}=
\bigoplus_{n=0}^D R^n q_n(t)\mathcal O[t]_{\le e_{n+1}},
\qquad
\mathcal E=R\partial_R,
$$
$$
q_n(t)=
\frac{(t h_7)^{\lfloor(n+1)/4\rfloor}
      (t-1)^{\lfloor(n+1)/3\rfloor}}
     {(1+8t)^{\lfloor n/2\rfloor}},
\qquad h_7=16t^2+4t+7.
\tag{1}
$$
乘回公共 $G_0$ 后，原 charge 是 $n+40$。
记 $M=m_{13}J$ 为 R338 的整规范，实际物理矩阵为
$$
\mathsf M^{\rm orig}=c_*\mathcal U_0M,
\qquad
m_{13}e_r=p^{\lfloor(r+13)/s\rfloor-\lfloor r/s\rfloor}e_{r+13}.
\tag{2}
$$
这里的目标单位包含整个原公共载体和 Gaussian；
没有在非原点把 $G_0/w^{13}$ 当成单位。

固定 R385 的一个允许的实际提升选择，并始终使用其
$g^\sharp,A_0^\sharp$。R386 的相容选择可以保留此前同一个 $A_0$；
本篇不需要另作提升或改变低轴。下文简记
$$
A(t)=\bar A_0^\sharp(t)=\sum_{k=1}^{s-1}A_kt^k\in tk[t]_{<s}.
$$
R388 在原平坦整环
$\mathcal A=\mathcal O[x,y,1/y]/(y^2-x^3-b)$
中支付的指定函数是
$$
Q_3=Q_2-u_\kappa(p-1)\widetilde Z^{p-1}C_0(t),
\qquad K_2\in\mathcal A.
\tag{3}
$$
这里 $C_0$ 正是 R382/R385 的第三坐标修正。
不得用未修正的 $Q_2$ 代替 (3)。

置
$$
\mathcal R(t)=\frac{34}{6x}(\bar Q_3+D_z\bar K_2),\qquad
\mathscr L=6t^2(1-t)\partial_t^2+t(5-8t)\partial_t.
\tag{4}
$$
R388 已证明 $\mathcal R$ 只有 $t=1$ 极，在 $0$ 为零，在无穷正规；
原实际形式商满足 $\mathscr L\bar A^{\rm for}=\mathcal R\bmod t^{2s}$。
因此，记
$$
d_k=k(6k-1),\qquad u_k=2(k-1)(3k-2),
$$
便有完整低窗递推
$$
\boxed{d_kA_k-u_kA_{k-1}=\mathcal R_k,\quad
1\le k<s,\quad A_0=0.}
\tag{5}
$$
每个 $d_k$ 都是单位。它们不是任选的形式 forcing；
(3) 中两次整除和全部真实提升已经固定其系数。

## 2. 原 $d_2$ 的低轴测试权

取真正的
$$
P_2\in K_2(\mathsf M^{\rm orig}),\qquad
\lambda_2\mathsf M^{\rm orig}=0\bmod p^2 .
\tag{6}
$$
$\lambda_0=\lambda_2\bmod p$ 因而属于真正的 $C_2^\vee$，
其中
$$
C_2=\operatorname{coker}\bar{\mathsf M}^{\rm orig}/
             \beta_1(K_1).
$$
并未将首 Bockstein 的像删去。用 (2) 的同一个目标单位把
$\lambda_0$ 拉回，记为 $\lambda$；它在三个块中的坐标记为
$\lambda_{i,j}$。此操作先保完整整矩阵，再取约化，
不是给一个任意模 $p$ Laurent 函数附加左核资格。

记
$$
W_i=(\mathcal E^i\bar P)(\bar g,\bar t),\qquad a=\bar a_\kappa\in k^\times,
$$
其中 $\bar P=P_2\bmod p$。R338 的完整十三行作用给
$$
\bar J(\bar P)=0,\qquad
[W_0]_{<s}=[W_1]_{<s}=0,\qquad [W_2]_{<\ell}=0.
\tag{7}
$$
第一式用的是 $M(P_2)\in p^2$，不能只凭原首核推出。

还准确有
$$
W_i(0)=0\quad\text{对所有 }i\ge0.
\tag{8}
$$
事实上 (1) 中只有相对次数 $n=0,1,2$ 能在 $t=0$ 非零。
故 $\bar P(R,0)$ 次数至多二。
(7) 在原点给它的第零、一、二 Euler 值都为零；
$2$ 为单位，所以这个二次多项式为零，得到 (8)。

R380、R385 的完整第三精度比较为
$$
\mathsf M^{\rm orig}(P)-\mathsf M^\sharp(P)
=p^2A(t)\,\bar{\mathsf M}^{\rm orig}((\mathcal E+40)\bar P)
                         \pmod{p^3}.
\tag{9}
$$
$\mathsf M^\sharp$ 仍保原第三坐标、$e_2((n+40)a_\kappa\epsilon^{[3]})$
及全部角多项式，只没有乘入 $1+(n+40)p^2A$。
对 (6)，40 倍项由 $\bar M\bar P=0$ 准确消去，
不是删去原 charge40。

因此同一低轴对原第二障碍的作用是
$$
\boxed{\begin{aligned}
\mathfrak B_{P,\lambda}(A)
={}&a\sum_{j=0}^{s-14}\lambda_{1,j+13}[w^j](A(t(w))W_2)\\
 &+\frac{a^2}{2}\sum_{j=0}^{\ell-1}
           \lambda_{2,j+13}[w^j](A(t(w))W_3).
\end{aligned}}
\tag{10}
$$
所有末行都已列出。第二块最后十三行乘 $m_{13}$ 时带一个 $p$，
所以在这个指定的模 $p$ 修正中消失；它们在原整矩阵与
$K_2/C_2$ 中仍然保留。第三块的真实末端是 $\ell+13$。

为统一转置，定义
$$
\eta_k(P,\lambda)=\mathfrak B_{P,\lambda}(t^k),\qquad 1\le k<s.
\tag{11}
$$
这里 $t^k$ 只用于评价已经固定的目标修正，不是新的来源。
由 (7)、(8) 与 $t(w)=-bw+\cdots$，
$$
\boxed{\eta_k(P,\lambda)=0\quad(k>m),\qquad
m=\max\{0,\ s-14-\ell,\ \ell-2\}.}
\tag{12}
$$
特别 $m\le s-15$。这对整个 (1) 成立，不要求逐 grade 分开核，
也不要求 $\mathcal E$ 保持 $K_2$。

## 3. 固定二阶算子的完整有限伴随

对任意指定权 $\eta=(\eta_1,\ldots,\eta_{s-1})$，
唯一地倒序定义
$$
\boxed{
c_s=0,\qquad d_kc_k-u_{k+1}c_{k+1}=\eta_k
                  \quad(k=s-1,\ldots,1).
}
\tag{13}
$$
全部除法只用 (5) 的单位。将 (5) 乘 $c_k$ 求和，邻项准确相消，给
$$
\boxed{\sum_{k=1}^{s-1}\eta_kA_k
             =\sum_{k=1}^{s-1}c_k\mathcal R_k.}
\tag{14}
$$
没有省略 $k=s-1$ 的末项。若 $\eta_k=0$ 于 $k>m$，
则同样 $c_k=0$ 于 $k>m$。

也可写出不递归的有限式。令
$$
g_j=\frac{(1/2)_j}{j!}\quad(0\le j<s).
$$
模 $p$ 的 $s=1/6$ 给
$$
\frac{u_{k+1}}{d_k}=\frac{k+1/3}{k-1/6}
                 =\frac{g_{s-k}}{g_{s-k-1}},
$$
因而
$$
\boxed{
c_k=g_{s-k}\sum_{j=k}^{s-1}
              \frac{\eta_j}{d_jg_{s-j}}.
}
\tag{15}
$$
这些 $g_j$ 也是单位。

首共振须另保。R388 的真实普通窗给
$$
\sum_{k=1}^{s}g_{s-k}\mathcal R_k=0.
\tag{16}
$$
(13) 采用 $c_s=0$ 的唯一代表；
如改取非零 $c_s$，整个权只能加上 (16) 的倍数，必须同时保其末项。
未修正坐标产生的 $51c_p(-1/b)^s$ 在 (3) 已经抵消，
不属于这里的新非零输入。

## 4. 转置权是原仿射椭圆曲线上的多项式

令
$$
C_\eta(t)=\sum_{k=1}^{s-1}c_kt^{-k},\qquad
H_\eta=\frac y{x^2}C_\eta(t)
      =\sum_{k=1}^{s-1}c_k(-b)^{-k}yx^{3k-2}.
\tag{17}
$$
$H_\eta$ 是仿射多项式，只有 $O$ 极；在 $x=0$ 正规。
其导数完整为
$$
\boxed{
D_zH_\eta=
 \sum_{k=1}^{s-1}c_k(-b)^{-k}
 \{(6k-1)X^k+(6k-4)bX^{k-1}\},\quad X=x^3.
}
\tag{18}
$$
特别没有以 $Z^{-1}$ 引入移动测试极。

**定理1。** 对 (14) 的任何指定原权，准确有
$$
\boxed{\begin{aligned}
\sum\eta_kA_k
={}&-\frac{17}{3}\operatorname{Res}_O(H_\eta\bar Q_3\,dz)\\
 &+\frac{17}{3}\operatorname{Res}_O
                       ((D_zH_\eta)\bar K_2\,dz)\\
={}&\frac{17}{3}\sum_{P\in E[2]\setminus O}
       \operatorname{Res}_P
          \{H_\eta\bar Q_3-(D_zH_\eta)\bar K_2\}\,dz .
\end{aligned}}
\tag{19}
$$

**证明。** 由 (14)，左边是
$\operatorname{Res}_{t=0}C_\eta\mathcal R\,dt/t$。
$t$ 在 $O$ 的零阶是六，故拉回到 $E_b$ 的残数须除以六。
使用
$dt/t=-6(y/x)\,dz$ 与 (4)，准确给第一项系数 $-34/6=-17/3$。
再对 $H_\eta D_z\bar K_2\,dz$ 作分部积分，得到第二项。

(3) 属于原 $\bar{\mathcal A}$，而 (17)、(18) 为仿射多项式；
因此这些微分除 $O$ 外只能在三个非零二挠点有极。
全局残数定理给最后一式。
没有在 $Q_3$、$K_2$ 的整除之前逐点除 $p$，
也没有把已选提升的 $K_2(P)$ 当成零。$\square$

所以，移动测试点在 **这个确定低轴修正的转置** 中不出现。
原完整 $d_2$ 的基准项仍可能包含其他残数，不能由 (19) 删除。

## 5. 下降到一个固定 $t=1$ 边界及全部主部

原 $\mu_6$ 型与 $\bar{\mathcal A}$ 给唯一分解
$$
\boxed{\bar Q_3=x\,q(t),\qquad
       \bar K_2=(y/x)\,k(t).}
\tag{20}
$$
具体地，型负二的元素可写
$xQ(X)/(X+b)^N$，型负一的元素可写
$x^2yK(X)/(X+b)^M$。
故 $q$ 在 $t=\infty$ 有限，$k(\infty)=0$。
原点阶还给 $q(0)=k(0)=0$。
二者只有 $t=1$ 极，R388 的真实界给
$$
\operatorname{pole}_1q\le N_q=\frac{3p^2-p-2}{2},
\qquad
\operatorname{pole}_1k\le N_k=\frac{3p^2-1}{2}.
\tag{21}
$$

定义
$$
B_\eta(t)=(1-4t)C_\eta(t)+6t(1-t)C_\eta'(t).
$$
因 $D_z(y/x)=x(1+2t)$，(4) 成为
$$
\mathcal R=\frac{17}{3}
       \{q+(1+2t)k-6t(1-t)k'\}.
\tag{22}
$$
于是 (19) 等价于一条固定有理残数：
$$
\boxed{
\sum\eta_kA_k=
 \frac{17}{3}\operatorname{Res}_0(C_\eta q+B_\eta k)\frac{dt}{t}
=-\frac{17}{3}\operatorname{Res}_1(C_\eta q+B_\eta k)\frac{dt}{t}.
}
\tag{23}
$$
在无穷 $C_\eta=O(t^{-1})$、$B_\eta=O(1)$、
$q=O(1)$、$k=O(t^{-1})$，因此没有遗漏无穷残数。

令 $u=t-1$，完整主部为
$$
q=\sum_{j\ge1}q_j u^{-j}+O(1),\qquad
k=\sum_{j\ge1}k_j u^{-j}+O(1),
$$
按 (21) 将范围外系数置零。
对每一个 $C=t^{-n}$，(23) 读取的边界数准确为
$$
\boxed{\begin{aligned}
\mathcal R_n=-\frac{17}{3}\sum_{j\ge1}(-1)^{j-1}
\bigg\{&
q_j\binom{n+j-1}{j-1}\\
+&k_j\left[
(1-6n)\binom{n+j-1}{j-1}
 +(6n-4)\binom{n+j-2}{j-1}
\right]\bigg\}.
\end{aligned}}
\tag{24}
$$
这是同一个 $\mathcal R$ 的真实 Taylor 系数，不是额外的观察或零条件。

也可先聚合微分的主部：
$$
\mathcal R=\sum_{j\ge1}r_j u^{-j}+O(1),\qquad
\boxed{
r_j=\frac{17}{3}
 \{q_j+(3-6j)k_j-(6j+4)k_{j+1}\}.
}
\tag{25}
$$
最高极仍不超过 $N_k$。公式保留所有 $O(p^2)$ 个主部项。

## 6. 高主部的准确 Frobenius 聚合和单位 Pascal 矩阵

定义有限聚合
$$
\boxed{
V_r=\sum_{h\ge0}(-1)^h r_{r+1+hp},
             \qquad 0\le r<p.
}
\tag{26}
$$
和在 (21)、(25) 的真实极界处终止。
对所有 $1\le n<p$，Lucas 公式准确给
$$
\boxed{
\mathcal R_n
=-\sum_{r=0}^{p-2}(-1)^r
               \binom{n+r}{n}V_r.
}
\tag{27}
$$
理由是
$\binom{n+j-1}{n}\bmod p=\binom{n+r}{n}\bmod p$
当 $j-1=r+hp$；
若最低位发生进位，右边也是零。
同时 $(-1)^{j-1}=(-1)^{r+h}$。
$r=p-1$ 时最低位必进位，所以这一方向准确不可见。

**定理2。** (27) 从 $(V_0,\ldots,V_{p-2})$ 到
$(\mathcal R_1,\ldots,\mathcal R_{p-1})$ 的矩阵是单位矩阵意义下的整同构：
其任意整数提升的行列式是 $p$ 单位。
尤其任意前 $m<p$ 行都有一个明确单位 minor。

**证明。** 将列反序，令 $r=p-2-j$。
当 $n\ge j+2$ 时 $n+r\ge p$，条目模 $p$ 为零；
对角 $j=n-1$ 的条目为
$$
-(-1)^{p-n-1}\binom{p-1}{n}=-1\quad\text{于 }k.
$$
所以反序矩阵模 $p$ 上三角，对角全为 $-1$。
前 $m$ 行取反序后的前 $m$ 列即为所述单位 minor。$\square$

这里的 Frobenius 聚合也有准确的代数解释。令
$$
P(U)=\sum_{j\ge1}r_jU^{j-1},\qquad U=(t-1)^{-1}.
$$
(26) 是 $P(U)$ 对
$U^p+1=(U+1)^p$ 的余式。
因为 $t=0$ 对应 $U=-1$，它保留的是同一个原点 $p$-jet，
不是另一条全局来源。余式的 $V_{p-1}U^{p-1}$ 在加回
$\mathcal R(0)=0$ 所需常数后，对应
$$
V_{p-1}(1+U)^p
  =V_{p-1}\left(\frac{t}{t-1}\right)^p,
$$
故在所有正次 $<p$ 行消失。
这说明其不可见性来自准确的 Frobenius 方向，而不是把高极丢掉。

实际原低轴只使用 (27) 的前 $s-1$ 行；
R388 的原形式比较只在已付窗使用。
定理2 对更长的有理 $\mathcal R$ 矩阵成立，并不扩充原 theta 比较窗。

## 7. 同一个边界向量中的中央与原第二障碍

令
$$
\widehat S^\sharp=g^\sharp a_{\rm ang}(t)/(7b)=w+\cdots,\qquad
a_{\rm ang}=t(t-1)h_7,
$$
并定义原中央权
$$
\eta_k^{\rm cent}=[w^s]\bigl(t(w)^k\overline{\widehat S^\sharp}(w)\bigr).
\tag{28}
$$
用 (13) 分别计算
$c^{\rm cent}$ 和 $c^{P,\lambda}$；
后二者由整个 mixed-grade 原 $P_2,\lambda_2$ 给出，不独立指定接触尾。
(14)、(27) 将两者都准确写成同一个实际向量 $V$ 的测试：
$$
\boxed{
\mathfrak B_{P,\lambda}(A)
 =\sum_{n=1}^{s-1}c_n^{P,\lambda}
       \left\{-\sum_{r=0}^{p-2}(-1)^r
                            \binom{n+r}{n}V_r\right\},
}
\tag{29}
$$
中央低轴项则以 $c^{\rm cent}$ 代入同一式。

这些权的末端并不相同。由 (12)，
$c_n^{P,\lambda}=0$ 于 $n>m$；而
$$
\eta_{s-1}^{\rm cent}=(-b)^{s-1},\qquad
d_{s-1}=5\pmod p,\qquad
\boxed{c_{s-1}^{\rm cent}=(-b)^{s-1}/5\in k^\times.}
\tag{30}
$$
这个单位是测试权的系数，不是该权作用于实际 $V$ 后的值。
(16) 另给同一个边界向量的一条带 $\mathcal R_s$ 的共振行；
不能将它误用为所有高 $\mathcal R_n$ 分别消失。

最后把已知的基准项也完整写回。
以整数提升定义
$$
d^\sharp(P_2,\lambda_2)
 =\overline{\lambda_2\mathsf M^\sharp(P)/p^2}.
$$
因两个矩阵模 $p^2$ 相同，此除法整。
同一固定 $P_2$ 的第二障碍、以及允许首次修正后真正的 $d_2$，均有
$$
\boxed{
\langle\lambda_0,d_2^{\rm orig}(\bar P)\rangle
=d^\sharp(P_2,\lambda_2)
 +\sum_{n=1}^{s-1}c_n^{P,\lambda}\mathcal R_n.
}
\tag{31}
$$
改变首次提升时，基准项和整配对按 R338/R351 的实际
$\beta_1(K_1)$ 同步改变；(31) 不是只取首核而仍留在 $C_1$ 的公式。

另一方面，记
$$
c_j^\sharp=[w^{js}]\widehat S^\sharp,\qquad
\mathcal C^\sharp=a_\kappa^2c_1^\sharp
          -pa_\kappa c_2^\sharp+2p^2c_3^\sharp.
$$
原完整中央失败经 R382 的全部 Newton 尾和 R385 的同一模型，先给
$\mathcal C^\sharp\in p^2\mathcal O$，再准确给
$$
\boxed{
\overline{\mathcal C^\sharp/p^2}
 +a^2\sum_{n=1}^{s-1}c_n^{\rm cent}\mathcal R_n=0.
}
\tag{32}
$$
这里没有分别赋予三个中央权零条件。

(31)、(32) 是当前实际像比较的完整有限对象：
同一原第二整商、同一固定二挠边界向量、两个明确转置以及各自基准项。
整个 $P_{134}/U_0$、第三坐标、Gaussian、charge40、
首次提升像和全部十三行已在构造权时保留。
要从 (32) 控制 (31)，仍需对这个真实 $V$ 和原来源像证明进一步的关系；
(19) 或定理2的单位矩阵本身不预付该传播。

## 依赖与同步

- [R338](R338-original-second-bockstein-and-fixed-miller-forcing-pairing.md)、[R351](R351-original-canonical-serre-adjoint-and-integral-second-lift-connection.md)：真正 $C_2$、整左右核与十三行。
- [R380](R380-original-low-axis-correction-and-full-second-bockstein-model.md)、[R382](R382-original-third-central-aggregate-and-full-third-precision-model.md)：同一低轴的完整矩阵和中央第三精度。
- [R385](R385-original-zero-resonance-and-strong-whole-theta-second-lift.md)、[R386](R386-original-second-harmonic-miller-iterate-and-two-torsion-interface.md)：同一 whole-theta 代表及相容提升。
- [R388](R388-original-second-quotient-global-forcing-and-first-resonance.md)：实际全局 $Q_3,K_2$、两次整除、固定极和正确首共振。

全篇为有限代数证明，无目标素数扫描。执行环境不可用期间按根规则提交小文本；
本次远端读取不是实际 git pull。
