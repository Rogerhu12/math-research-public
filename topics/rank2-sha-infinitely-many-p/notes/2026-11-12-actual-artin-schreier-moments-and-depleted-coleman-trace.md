# 实际半局部 Artin–Schreier 两矩与去 p Coleman 类群迹

日期：2026-11-12。**已证明的有限比较；原 CM 轨道的无穷非零性仍开。**

沿用 R130 的 $E,F,L,\Gamma=\langle\tau\rangle,Q$。本篇不改变
原点的定义：若 $H=F[\ell]$、$\mathsf U=\operatorname{Gal}(H/L)$，
则
$$
                  Q=\operatorname{Tr}_{H/L}\pi(x_\ell),
\qquad \pi(\infty)=O.                                  \tag{1}
$$
所有下式的完整类群迹都针对 (1)，而非任意选取的局部向量。
§§1–4 的有限公式适用于全部好约化型；§5 的 Coleman 比较
要求 **源 CM 域 $F$ 在 $p$ 分裂**，不要求目标 $E$ 在 $p$ ordinary。

## 1. 非 formal 原点的对数及唯一的一层 p

R130 已证明所有 $p$ 处不分歧，剩余次数只可能为 $1,2,p$，且
$p\nmid\#E(k_w)$。取一个 $p$ 单位整数 $m$ 杀掉全部约化群，定义
$$
 \log_E Q=m^{-1}\log_E([m]Q),\qquad
             z_Q:=\log_E Q/p\in\mathcal P,
 \qquad\mathcal P=\mathcal O_L\otimes\mathbb Z_p.          \tag{2}
$$
形式群同态性使这个延拓对 $m$ 独立；它是实际 Abelian logarithm。
因为 $[m]Q$ 的参数属于 $p\mathcal P$ 且 $m$ 为单位，(2) 确实整。
范数零条件给
$$
               N_\Gamma z_Q=0,\qquad z_Q\in I=(\tau-1)\mathcal P.
\tag{3}
$$
这证明了先对原点延拓 log、再除 $p$ 的合法性；不能对不在
formal group 的 $Q$ 直接以 $t_E(Q)/p$ 代替它。

若 $R=D_pQ$ 是 R130 的实际 formalizer，则
$$
 z_R=D_pz_Q,
 \qquad z_R\equiv t_E(R)/p\pmod{p\mathcal P}.             \tag{4}
$$
后续有限计算在 $\overline{\mathcal P}=\mathcal P/p\mathcal P$ 中进行。
R106 的实际共轭式为 $cQ=-\tau^bQ$。将 $Q$ 乘以
$\tau^{b/2}$（指数于 $\mathbb Z/p$ 中取值）后，可以令
$$
                         cQ=-Q.                           \tag{5}
$$
这是实际整自同构，不改变指数 $a$ 或 R130 的非零条件。

## 2. F 分裂、非平凡 Artin 的两个域迹

固定 $v\mid p$，写 $s=\operatorname{Art}_{L/F}(v)=\tau^h\ne1$。
对应完成是不分歧次数 $p$ 扩张，其剩余域为 $k=\mathbb F_{p^p}$。
算术 Frobenius 为 $s$。选
$$
        \upsilon\in k,\qquad \upsilon^p-\upsilon=h.
\tag{6}
$$
$h\ne0$ 保证该 Artin–Schreier 多项式不可约；$\tau=s^{h^{-1}}$
遂满足 $\tau\upsilon=\upsilon+1$。令 $z$ 为 $z_Q$ 在该完成的约化，
定义真正的有限域迹
$$
 T_1=\operatorname{Tr}_{k/\mathbb F_p}(\upsilon z),\qquad
 T_2=\operatorname{Tr}_{k/\mathbb F_p}(\upsilon^2z).
\tag{7}
$$
它们是 $\mathbb F_p$ 中的两个数。由 $\operatorname{Tr}z=0$，直接展开
$$
 \begin{aligned}
 T_1&=\sum_{j=0}^{p-1}j\tau^jz,\\
 T_2&=2\upsilon T_1+\sum_{j=0}^{p-1}j^2\tau^jz.
 \end{aligned}
$$
因此 R130 的实际行准确是
$$
 \boxed{\quad
 \mathcal D_2z=\frac12\bigl(T_2-(2\upsilon+1)T_1\bigr),
 \qquad
 \mathcal D_2z\ne0\Longleftrightarrow(T_1,T_2)\ne(0,0).
 \quad}                                                   \tag{8}
$$
后一等价使用 $\upsilon\notin\mathbb F_p$。
将 $\upsilon$ 改成 $\upsilon+c_0$、$c_0\in\mathbb F_p$ 时，
$T_1$ 不变，$T_2$ 变成 $T_2+2c_0T_1$；非零条件不变。

另一 $p$ 上素位的 Artin 元是 $s^{-1}$。用
$\upsilon_-=-c\upsilon_+$ 及 (5)，其两个域迹准确为
$$
                         (T_{1,-},T_{2,-})=(T_{1,+},-T_{2,+}).
\tag{9}
$$
所以使用一对标量是已比较两个地方后的结论，不是删除一个
$p$ 上素位。原参数若未作 (5) 的整旋转，只产生同样的可逆
三角变换：$z\mapsto\tau^r z$ 使 $T_1\mapsto T_1$、
$T_2\mapsto T_2-2rT_1$。

## 3. 完全分裂的置换公式及 F 惰性的两符号

当 $L/F$ 在 $v$ 完全分裂时，取一个 $w_0\mid v$，把原实际
共轭点全部嵌入 $L_{w_0}=F_v$，置
$$
 z_j=\frac{\log_E(\tau^jQ)}p\pmod p\in k_v,
 \qquad A_1=\sum_{j=0}^{p-1}jz_j,\quad
        A_2=\sum_{j=0}^{p-1}j^2z_j.
\tag{10}
$$
这里 $\sum z_j=0$。其余完成是实际 $\Gamma$ 置换，而不是
$\Gamma$ 在单个 $F_v$ 上的平凡作用。重排指标给
$$
 \sum_{j=0}^{p-1}\binom j2z_{j+r}
       =\frac12\bigl(A_2-(2r+1)A_1\bigr),\qquad r\in\mathbb F_p.
\tag{11}
$$
于是完整半局部行非零恰当 $(A_1,A_2)\ne(0,0)$。

若 $p$ 在 $F$ 分裂，$k_v=\mathbb F_p$，另一素位仍按 (9)
交换两个符号。若 $p$ 在 $F$ 惰性，则 R130 已证它在 $L/F$
完全分裂，$k_v=\mathbb F_{p^2}$。选在 $w_0$ 上作用为
算术 $p$-Frobenius 的反射，并按 (5) 对该反射正规化。于是
$$
                  z_j^p=-z_{-j},\qquad
                  A_1^p=A_1,\quad A_2^p=-A_2.              \tag{12}
$$
因此 $A_1\in\mathbb F_p$，而
$A_2/\overline{\sqrt{-15}}\in\mathbb F_p$。这同样是两个准确的
$\mathbb F_p$ 标量，分别保留正、负符号；没有对惰性情形
错误地使用不分歧次数 $p$ 的单域迹。

## 4. 原点、formalizer 与任意实际群环算子的前两矩

对整群环元 $B=\sum b_j\tau^j$，定义
$$
 b^{(0)}=\sum b_j\pmod p,\qquad
 b^{(1)}=\sum j b_j\pmod p.
$$
由迹不变性或 (10) 的重排，两种局部模型都给同一公式
$$
 \binom{T_1(Bz)}{T_2(Bz)}
 =\begin{pmatrix}b^{(0)}&0\\-2b^{(1)}&b^{(0)}\end{pmatrix}
       \binom{T_1(z)}{T_2(z)}.                             \tag{13}
$$
完全分裂时将 $T_i$ 换成 $A_i$。所以只要 $B$ 在
$(p,\tau-1)$ 下为单位，前两矩的共同消失不变；(13) 同时
记下了不能忽略的一阶交叉项。

R130 的 $D_p$ 自反，故 $b^{(1)}=0$。它在前两矩上准确只乘
$$
 \begin{cases}
       (1-a_p)^2,&p\text{ 在 }F\text{ 分裂},\\
       1-a_p^2,&p\text{ 在 }F\text{ 惰性},
 \end{cases}                                             \tag{14}
$$
均为 $\mathbb F_p$ 单位。这明确比较了原 $Q$ 的对数和实际
$D_pQ$ 的形式参数，没有额外的 $p$ 或 $\delta$ 损失。

## 5. 原 CM 完整迹与真正的去 p Coleman 原函数

本节假设 $p=\mathfrak p\bar{\mathfrak p}$ 在源域 $F$ 分裂。
令 $f_\pi$ 为实际微分 $\pi^*\omega_E=f_\pi(q)\,dq/q$ 的
权二 cusp form，保留其固定 Manin 常数，不先除掉它。
取 Coleman 原函数
$$
                 G(x)=\log_E\pi(x),\qquad G(\infty)=0.
\tag{15}
$$
它的 q 展开是 $\sum_{n\ge1}a_n(\pi)q^n/n$。
定义 $p$-depletion 为删除所有指数被 $p$ 整除的项。
因为 $p\nmid N$，Hecke 关系给
$$
 f_\pi^{[p]}=(1-a_pV+pV^2)f_\pi,
\qquad
 G^{[p]}=(1-a_pV/p+V^2/p)G,\qquad dG^{[p]}=f_\pi^{[p]}dq/q.
\tag{16}
$$
两项 $1/p$ 的来源不同但均已保留：
$d(G(q^p))=p(Vf_\pi)dq/q$，
$d(G(q^{p^2}))=p^2(V^2f_\pi)dq/q$。
BDP（2013）Lemma 3.23、Proposition 3.24 给 (16) 在普通源
曲线上的实际 Coleman/rigid 解释，而非只在尖点的形式等式。
其中 ordinary 指源 CM 椭圆曲线；不要求 $a_p(E)$ 为单位。

这里的 CM 支及 Artin 方向可几何固定。选 $\mathfrak p$ 为
所用 $p$ 进嵌入对应的素理想。CM 曲线的 connected canonical
subgroup 是 $C[\mathfrak p]$，商为
$C/C[\mathfrak p]$。在复格模型上，这将格 $\mathfrak a$
变为 $\mathfrak p^{-1}\mathfrak a$。我们采用算术 Artin 约定，
这就是 $x_{\mathfrak a}^{\sigma_{\mathfrak p}}$；其约化是
$p$ 次 Frobenius，和算术 Artin 的剩余作用一致。
也可用 ordinary canonical lift 的唯一性核定此方向。
BDP 的 $V$ 另把完整 $N$ 阶标记乘 $p^{-1}$、微分乘 $p$；
在这里的 $X_0(N)$ 和权零原函数上，两者分别不改变循环
子群及函数值。因此 (16) 的 $V$ 在这些实际点上就是
$\sigma_{\mathfrak p}$，并非其另一个未标记的同源支。

取 $s=\sigma_{\mathfrak p}|_L=\tau^h$，允许 $h=0$。由于
Artin 作用与 $\mathsf U$ 交换，对 (1) 的原完整迹准确有
$$
 \begin{aligned}
 \eta_{p,\ell}
   &:=\sum_{u\in\mathsf U}G^{[p]}(x_\ell^u)\\
   &=\bigl(1-a_ps/p+s^2/p\bigr)\log_E Q\\
   &=(p-a_ps+s^2)z_Q\in I.                             \tag{17}
 \end{aligned}
$$
这里没有额外的类数或 $p$ 分母。单个未取迹的
$\log_E\pi(x_\ell^u)/p$ 不必整；(17) 的整性首先由原
$Q$ 的 (2) 证明，不能把该整性无证分配给每一项。

若使用 R105/R116 的固定映射
$\Phi=\pi d_1+\pi d_3$、$\Psi=[2]\Phi$，则其实际拉回微分
分别为 $f_\pi+3V_3f_\pi$ 和它的两倍。$p\ne3$ 使
depletion 与 $V_3$ 交换，而原函数中
$d^{-1}(3V_3f)=V_3d^{-1}f$，故那个 $3$ 不产生新的 Euler
因子。先对阶 $u=(\ell+1)/p$ 的惯性子群取迹，$\Phi$
给原 $Q$，$\Psi$ 给 $2Q$；后者只将 (17) 乘固定单位 $2$。
若改为对整个 $\mathsf U$ 再取迹，必须相应保留重复的二阶
类群迹；本篇不混淆这两个约定。

令 $A_s=p-a_ps+s^2$。其在 (13) 中的两个系数是
$$
          a^{(0)}=1-a_p,\qquad a^{(1)}=h(2-a_p)\pmod p.
$$
因此实际去 $p$ 迹的两矩为
$$
 \boxed{\quad
 \binom{T_1(\eta_{p,\ell})}{T_2(\eta_{p,\ell})}
  =\begin{pmatrix}1-a_p&0\\-2h(2-a_p)&1-a_p\end{pmatrix}
        \binom{T_1(z_Q)}{T_2(z_Q)}.
 \quad}                                                   \tag{18}
$$
这给所有单位、交叉项和那唯一的一层 $p$ 的准确比较。
在另一个 $p$ 上素位使用 $s^{-1}$，$h$ 变号，与 (9)
完全相容。即使 $a_p=0$，(18) 仍可逆。

若 $p$ 在 $F$ 惰性，源 CM 曲线超奇异，没有保持导子
$\ell$ 的 connected canonical $p$ 支，不能照抄 (16)–(18)
来给所有点指定一个这样的 $V$。该情形已证的是 §3 的
完整有限公式，尚未由本节补上同一种 ordinary Coleman 比较。

## 6. 一个真正的有限域函数及其二次 AS 障碍

本节仍在源 $F$-ordinary 比较中。删去固定有限多个整除
$f_\pi$ 第一 Fourier 系数的素数。取一个固定的细素于 $p$
模曲线覆盖，记其模 $p$ 光滑射影曲线为 $X$，Hasse invariant
为 $\mathrm{Ha}$。Katz 的 holomorphic theta 算子
$\Theta$ 把权 $k$ 升到 $k+p+1$，q 展开为 $q\,d/dq$。
于是
$$
 g_p=\frac{\Theta^{p-2}\overline f_\pi}{\mathrm{Ha}^{p}}
                         \in\overline{\mathbb F}_p(X)
\tag{19}
$$
确为权零：$2+(p-2)(p+1)=p(p-1)$。其 q 展开准确为
$$
                    \sum_{p\nmid n}\frac{\overline{a_n(\pi)}}nq^n,
\tag{20}
$$
所以它是 $G^{[p]}$ 的 ordinary 约化；这里的 q 展开原则
保持权零，并未只把不同权形式的 q 展开任意等同。
Katz 的 theta 保持 holomorphic/cuspidal，Hasse 在尖点为单位、
在细模曲线的超奇异点是简单零，所以 $g_p$ 只在超奇异点
有极点，每处阶数至多 $p$。

事实上至少一处阶数正好为 $p$。权二的非零 cusp form 在
$p\ge7$ 时有 exact filtration $2$；从 $j=0$ 到 $p-3$，
权 $2+j(p+1)$ 均非 $p$ 的倍数。Katz 的 exact-filtration
定理逐次给 $\Theta^{p-2}\bar f_\pi$ 不被 Hasse 整除。
因此 (19) 至少有一个真正 $p$ 阶极点。

令 $\operatorname{AS}(h)=h^p-h$。由这个极点预算严格得到
$$
                         g_p\notin\operatorname{AS}^2
                                      \bigl(\overline{\mathbb F}_p(X)\bigr).
\tag{21}
$$
证明很短：若非恒定 $h$ 在某点有极点阶 $m>0$，则
$h^{p^2}-2h^p+h$ 在同一点有唯一的最高极点阶 $p^2m>p$。
若 $h$ 没有极点，它在射影曲线上是常数，不能产生 (19)。
这是真正的全局函数障碍，使用的是原 $f_\pi$。

## 7. 尚未支付的原 CM 轨道比较

尽管 (21) 已证，它并未证明 (18) 的两矩在无穷实际输入中
非零。需要检验的是原环类轨道：先按
$\mathsf U=\operatorname{Gal}(H/L)$ 取完整迹，再在真实
$C_p$ 商上取 §§2–3 的两矩。它们不是对任意闭点的迹。

一个具体警示是：这些原轨道的**第一层总迹本来恒零**，
因为 $N_\Gamma Q=0$，故由 (17)
$$
                         N_\Gamma\eta_{p,\ell}=0.
\tag{22}
$$
其来源是实际 Heegner 范数/Hecke 关系 $a_\ell(E)=0$，
不是已经证明了 $g_p$ 在全局函数域里是 AS coboundary。
此外，第一层 trace 为零只保证剩余值属于
$(\operatorname{Frob}-1)$ 的像；R130 的两个额外矩同时零
把它放入相应正则模的第三次像。不能将这一步无说明改为
任意函数域中的第二次或第三次 coboundary。

因此，下一条真实待证箭头是：从这一固定 CM/Hecke 轨道族
上的全部额外两矩零，推出一个与 (21) 冲突的全局 AS 条件，
或另给该轨道族上的非零定理。普通曲线任意闭点的
Chebotarev 不能代替这个轨道族的分布。此前
$\mathbb Q(i)$ 的中央半因子 $J'_p$ 也未被本篇冒充 (17)：
这里使用的是 $F=\mathbb Q(\sqrt{-15})$、导子 $\ell$ 的
真实环类角色及实际 Heegner 对数，尚无已付等式将两者等同。

## 一手来源

- M. Bertolini, H. Darmon, K. Prasanna, *Generalized Heegner cycles and
  p-adic Rankin L-series*, Duke Math. J. **162** (2013), 1033–1148，
  [出版全文](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP1.pdf)。
  §1.4，(1.4.7)–(1.4.8) 定义真实 CM 商及标记；§3.8，
  Lemma 3.23、Proposition 3.24，印页 1085–1087，给去 $p$
  Coleman 原函数。本文只用权二/权零的这一比较，未调用
  一个尚未匹配的高权或跨素数非零定理。
- N. Katz, *A result on modular forms in characteristic p*, LNM **601**
  (1977), 53–61，[作者全文](https://web.math.princeton.edu/~nmk/old/modformcharp.pdf)。
  §II Theorem (1)–(2)、Corollaries (1)–(2) 给 theta、holomorphy
  与 exact filtration；印页 60 说明 Hasse 的简单零。
- R106、R119、R123、R128、R130：实际共轭式、完整迹点及
  半局部整格。本文 (6)–(14)、(17)–(18)、(21) 均附直接证明。
