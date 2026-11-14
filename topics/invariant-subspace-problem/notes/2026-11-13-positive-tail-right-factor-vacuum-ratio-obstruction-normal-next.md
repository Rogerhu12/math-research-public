# 实际尾主理想的非负系数右因子统一真空比障碍

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：以下结论完整证明，属于中间进展。** 本稿把 R253 中仅对右因子 $I$ 的衰减结论，扩展到一族允许随尾层变化、允许任意高位及大量二进位支撑的真实右因子。它们是实际归一化幂的非负系数绝对和。所有真实进位均支付，不把纯模型右因子当成实际交换子。完整理想范数 $q_m$、复杂相位右因子和一般正常见证仍开放。

## 1. 实际尾因子和右因子锥

在原 Haar 表示中取
$$
S=S_N=\sum_{j\ge0}(j+1)^{-2}N_j
\quad\text{或}\quad
S=S_Y=\sum_{j\ge0}(j+1)^{-2}Y_j.
$$
令
$$
q=2^m,\quad a_j=(j+1)^{-2},\quad a_\Sigma=\sum_{j\ge0}a_j,
$$
并沿用 R253 的实际相位乘积
$$
P_m=\prod_{\zeta^q=1}\gamma_\zeta(S)
=I_{<m}\otimes Q_m\in S\mathcal A,
\qquad Q_m\in\mathcal B_m.
\tag{1.1}
$$
下文所有尾算子均在 $H_m$ 上理解；其 Haar 真空态记 $\omega_m$。

对有限 $B\subset[m,\infty)$，置
$$
N_B=\prod_{j\in B}N_j,\qquad
E_B=\prod_{j\in B}E_j,\qquad E_j=e_{10}^{(j)},
\quad N_\varnothing=E_\varnothing=I.
$$
$N_B$ 是实际算子，彼此交换且属于 $\mathcal B_m$。$E_B$ 仅用于比较。

给整数 $b\ge0$，定义非负系数锥
$$
\mathcal C_m(b)=
\left\{
W=\sum_{\substack{B\subset[m,\infty)\ {\rm finite}\\|B|\le b}}
c_BN_B:
c_B\ge0,\quad 0<\sum_Bc_B<\infty
\right\}.
\tag{1.2}
$$
级数按算子范数绝对收敛，因为 $\|N_B\|\le1$，所以
$W\in\mathcal B_m$。这些右因子保持函数非负锥；不把它们称为 Hilbert 自伴正算子。

设
$$
L_m=\left\lfloor\frac{q^{2/3}}4\right\rfloor,\qquad
\beta=1+\frac1{\sqrt2}.
$$

**定理 1.1。** 若整数序列 $b_m=o(q^4)$，则存在 $m_0$，使所有 $m\ge m_0$、所有
$W\in\mathcal C_m(b_m)$ 都有 $Q_mW\ne0$ 且
$$
\boxed{
\frac{|\omega_m(Q_mW)|}{\|Q_mW\|}
\le3\beta^{-L_m}.
}
\tag{1.3}
$$
$m_0$ 可以依赖所给 $b_m$ 序列，但不依赖 $W$ 的系数、非零项个数或所用位的最大指标。

事实上同一证明允许更大的固定预算
$$
\limsup_{m\to\infty}\frac{b_m}{q^4}
<\frac{770}{16\log2}.
\tag{1.4}
$$
特别 $b_m\le q^4$ 也是一个明确的安全范围。这只是所用绝对 carry 估计给出的充分预算，不声称临界常数或实际最大范围。

## 2. 普通非负尾幂多项式的真实二进位归约

(1.2) 包括大量普通的正系数多项式。这里付清重复幂造成的全部进位。

实际递推为
$$
N_j^2=\eta_jN_{j+1},\qquad
0<\eta_j\le e^{-770\,16^j}.
\tag{2.1}
$$
故对 $\ell\ge0$，
$$
N_m^{2^\ell}
=\kappa_{m,\ell}N_{m+\ell},
\qquad
\kappa_{m,0}=1,\qquad
\kappa_{m,\ell}
=\prod_{r=0}^{\ell-1}\eta_{m+r}^{\,2^{\ell-1-r}}>0.
\tag{2.2}
$$
给定 $n=\sum_{\ell\in B(n)}2^\ell$，准确有
$$
\boxed{
N_m^n=
\left(\prod_{\ell\in B(n)}\kappa_{m,\ell}\right)
N_{m+B(n)}.
}
\tag{2.3}
$$
所有系数严格正，不以无进位关系代替 (2.1)。

因此，对非零多项式
$$
W=p(N_m)=\sum_{n=0}^K t_nN_m^n,\qquad t_n\ge0,
$$
只要每个 $t_n\ne0$ 的指数 $n$ 的二进位 $1$ 数至多为 $b_m$，就有
$W\in\mathcal C_m(b_m)$。例如所有次数小于 $2^{b_m}$ 的此类多项式均被覆盖；实际结论没有最高指数限制，稀疏二进位指数可以任意大。

后续归一化也无零系数歧义。对 (1.2) 的一个给定表示，令
$s=\sum_Bc_B$。它有限且严格正，将 $W$ 换成 $s^{-1}W$ 不改变 (1.3) 的比值。每个 $N_B$ 都是非零保锥算子并有正真空矩，因此非负系数和为正时 $W\ne0$。以下统一假设
$$
\sum_Bc_B=1,\qquad
W_0=\sum_Bc_BE_B.
\tag{2.4}
$$

## 3. 纯正右因子的统一首位占据

令
$$
D_m=\sum_{j\ge m}a_jE_j,\qquad
D_m^q=q!\sum_{\substack{F\subset[m,\infty)\\|F|=q}}a_FE_F.
$$
对固定有限 $B$，
$$
D_m^qE_B
=q!\sum_{\substack{|F|=q\\F\cap B=\varnothing}}
a_FE_{F\cup B},
\tag{3.1}
$$
因为纯矩阵的重复位确实给零。此处只是在比较模型内使用 $E_j^2=0$；实际重复幂已在第 2 节准确处理。

对 (3.1) 按真空矩归一化，条件于 $B$ 后，$F$ 是从
$[m,\infty)\setminus B$ 中按权 $a_F$ 选出的 $q$ 元子集。记未排除任何指标时的概率为 $\mathbb P_m$，其单点入选概率为 $p_j$。

### 3.1 排除有限集合为何增加其余指标的入选率

对固定基数的正权子集分布，任意两个不同指标 $i,j$ 满足
$$
\mathbb P(i,j\in F)\le\mathbb P(i\in F)\mathbb P(j\in F).
\tag{3.2}
$$
可直接由基本对称多项式的对数凹性证明：剔除 $i,j$ 后的系数记 $E_k$，分母
$Z=E_q+(a_i+a_j)E_{q-1}+a_ia_jE_{q-2}$，则两边之差为
$$
\frac{a_ia_j}{Z^2}(E_{q-1}^2-E_qE_{q-2})\ge0.
$$
对数凹性及无限可和权的极限证明，已在正尾耦合附录 §5.1 完整给出。

由 (3.2)，条件排除 $i$ 后
$$
\mathbb P(j\in F\mid i\notin F)
=\frac{p_j-\mathbb P(i,j\in F)}{1-p_i}
\ge p_j.
\tag{3.3}
$$
分母为正，因为尚有无限多个正权指标。逐个排除 $B$ 中的有限指标，每一步仍是同类固定基数正权分布，故
$$
\boxed{
\mathbb P(j\in F\mid F\cap B=\varnothing)\ge p_j
\quad(j\notin B).
}
\tag{3.4}
$$
这里比较的是固定基数 $q$ 的条件分布；没有误把它改成基数 $q-|B|$。

R253 第三附录 §3 的准确计数界为
$$
1-p_j\le\frac{4(j+1)^2}{q^2}.
\tag{3.5}
$$
对总集合 $G=F\cup B$，如果 $j\in B$，则它已被强制选中；如果 $j\notin B$，由 (3.4)—(3.5)，
$$
\mathbb P(j\notin G\mid B)\le\frac{4(j+1)^2}{q^2}.
\tag{3.6}
$$
这一界与 $B$ 的大小、形状及最大指标无关。

令
$$
J_m=\{m,\ldots,m+L_m-1\}.
$$
对充分大的 $m$，$m\le L_m$，于是并集界给
$$
\begin{aligned}
\mathbb P(J_m\nsubseteq G\mid B)
&\le\frac4{q^2}\sum_{j=m}^{m+L_m-1}(j+1)^2\\
&\le\frac{4L_m(m+L_m)^2}{q^2}
\le\frac{16L_m^3}{q^2}
\le\frac14.
\end{aligned}
\tag{3.7}
$$
所以整个共同首块同时被选中的概率至少为 $3/4$。

对 (2.4) 的 $W_0$，其各 $B$ 项的真空矩为
$$
q!c_B2^{-q-|B|}e_q(a_{j\notin B}),
$$
全为非负，且总和严格正。因此它们再归一化形成一个关于 $B$ 的概率混合。(3.7) 对每个分量统一成立，故对全部 $D_m^qW_0$ 仍成立。这一步不需要任何系数上界或有限项数。

## 4. 同一偏转向量对整个非负锥的范数下界

在每个 $j\in J_m$ 取
$$
u_j=\cos(\pi/8)e_0+\sin(\pi/8)e_1,\qquad
v_j=\sin(\pi/8)e_0+\cos(\pi/8)e_1,
$$
其余位保持 Haar 真空。所得 $u,v$ 都是实际尾空间中的单位向量。

对任意有限 $G$，矩阵元 $\langle E_Gu,v\rangle$ 非负；若 $J_m\subseteq G$，则准确有
$$
\langle E_Gu,v\rangle
=\beta^{L_m}\omega_m(E_G),
\qquad \beta=1+1/\sqrt2.
$$
因为在选中的 $J_m$ 位上，
$\langle E_ju_j,v_j\rangle=\beta/2$，而真空矩为 $1/2$；其余位不变。

记
$$
k_m(W_0)=\omega_m(D_m^qW_0)>0.
$$
只保留 (3.7) 所保证的同时占据项，得到
$$
\boxed{
\|D_m^qW_0\|
\ge\langle D_m^qW_0u,v\rangle
\ge\frac34\beta^{L_m}k_m(W_0).
}
\tag{4.1}
$$
因此在纯比较模型内，这个真空比衰减对所有非负系数右因子都统一成立；没有 $b_m$ 限制。下一节的支撑预算只用于真实 carry 的统一支付。

## 5. 对所有右因子的统一真空下界与真实误差

设 $|B|\le b=b_m$。在 $[m,m+b+q)$ 的 $b+q$ 个指标中，至少有 $q$ 个不属于 $B$。在 $e_q(a_{j\notin B})$ 中仅保留这样一项，得到
$$
e_q(a_{j\notin B})\ge(m+b+q)^{-2q}.
$$
又 $2^{-|B|}\ge2^{-b}$，故
$$
\omega_m(D_m^qE_B)
\ge q!2^{-q-b}(m+b+q)^{-2q}.
$$
使用 $\sum_Bc_B=1$，可得独立于 $W$ 的下界
$$
\boxed{
k_m(W_0)\ge
H_m:=q!2^{-q-b_m}(m+b_m+q)^{-2q}>0.
}
\tag{5.1}
$$

现在回到实际算子。真实局部递推给
$$
\|N_j-E_j\|\le\eta_j,\qquad
\eta_j\le e^{-770\,16^j},\qquad
\|N_j\|=\|E_j\|=1.
$$
按任意固定顺序对乘积作望远镜差分，无须混合因子彼此交换，得到
$$
\|N_B-E_B\|\le\sum_{j\in B}\eta_j
\le b_m e^{-770\,16^m}.
$$
因此由 (2.4)，
$$
\|W\|\le1,\qquad
\boxed{\|W-W_0\|\le b_m e^{-770q^4}.}
\tag{5.2}
$$
这里明确使用 $16^m=q^4$；没有将第 $m$ 位的误差与第 $m-1$ 位混淆。

R253 第三附录给
$$
\|Q_m-D_m^q\|\le
e_m=13a_\Sigma q(3a_\Sigma)^{q-1}e^{-770\,16^{m-1}}.
\tag{5.3}
$$
因为 $\|D_m^q\|\le a_\Sigma^q$，从而
$$
\boxed{
\|Q_mW-D_m^qW_0\|
\le\Delta_m:=
e_m+a_\Sigma^q b_m e^{-770q^4}.
}
\tag{5.4}
$$

若 $b_m=o(q^4)$，则 $b_m\le q^4$ 对充分大的 $m$ 成立。由
$q!\ge(q/e)^q$，
$$
\log H_m
\ge-b_m\log2+q\log q-q\log(2e)
-2q\log(m+b_m+q)
\ge-b_m\log2-O(q\log q).
$$
最后一个下界为 $-o(q^4)$。另一方面，
$$
\log\Delta_m
\le-\frac{770}{16}q^4+O(q+\log(1+b_m)).
$$
所以
$$
\boxed{\Delta_m/H_m\longrightarrow0.}
\tag{5.5}
$$
所有界均与 $W$ 的系数及所用最高位无关。

更一般，若 (1.4) 成立，则 $b_m=O(q^4)$，且
$$
\log(\Delta_m/H_m)
\le-\frac{770}{16}q^4+b_m\log2+O(q\log q)
\longrightarrow-\infty.
\tag{5.6}
$$
这证明第 1 节所述更大的安全预算。常数来源是相位消元误差中的
$770\,16^{m-1}=(770/16)q^4$，不是把完整 $770q^4$ 错用于该项。

## 6. 返回实际理想测试量

令
$$
t_m=\Delta_m/H_m\longrightarrow0.
$$
由 (5.1)，实际右因子的相对误差满足
$\Delta_m/k_m(W_0)\le t_m$。对充分大的 $m$ 取 $t_m\le1/4$。于是 (4.1) 与 (5.4) 给
$$
|\omega_m(Q_mW)|\le k_m(W_0)+\Delta_m,
$$
以及
$$
\|Q_mW\|\ge\frac34\beta^{L_m}k_m(W_0)-\Delta_m>0.
$$
所以统一有
$$
\frac{|\omega_m(Q_mW)|}{\|Q_mW\|}
\le\frac{1+t_m}{(3/4)\beta^{L_m}-t_m}
\le3\beta^{-L_m}.
$$
这证明定理 1.1，并同时证明了所用 $Q_mW$ 非零。由于 $W\in\mathcal B_m$，
$I_{<m}\otimes Q_mW\in S\mathcal A$ 是确切的实际主理想成员。

## 7. 排除了什么，仍保留什么

本文统一排除用上述非负系数、给定二进位支撑预算内的右因子，使真空矩相对于算子范数保持非消失下界。它比只检验 $W=I$ 更强，允许右因子本身随 $m$ 改变、系数任意、项数可数及最高指数任意大。

但它没有给 R253 的完整
$$
q_m=\sup_{W\in\mathcal B_m,\ Q_mW\ne0}
\frac{|\omega_m(Q_mW)|}{\|Q_mW\|}
$$
一个趋零上界。具有负系数或复杂相位抵消的实际右因子、超出已付支撑预算的非负因子，以及完整尾交换子中的非 UHF 因子均不被本定理排除。也没有把任意保持函数正锥的交换子自动表示成 (1.2)。

没有证明一般正常湮灭者存在或不存在；普通 Hilbert ISP 仍开放。

## 已证依赖

- R253：实际相位消元、尾代数与主理想身份。
- R253 第三附录 §§2--5：真实 $e_m$、原固定基数遗漏概率上界及偏转矩阵元。
- 正尾耦合附录 §5.1：基本对称多项式对数凹性与固定基数二点负相关的完整证明。
- 实际 $N_j^2=\eta_jN_{j+1}$、$\|N_j-E_j\|\le\eta_j$：原 Haar 真实递推；第 2、5 节已给本稿所需全部使用步骤。
