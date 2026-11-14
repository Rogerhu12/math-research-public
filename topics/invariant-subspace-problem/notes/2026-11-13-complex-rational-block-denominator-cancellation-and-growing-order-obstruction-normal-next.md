# 复有理块的分母消去：固定复杂度与增长阶数仍有全列障碍

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065。

**状态：完整证明的中间结论。** 延续同一个固定正常正秩一态
$f=1+\sum_i2^{-i-2}\chi_{B_i}$、$|B_i|=2^{4i}$。对已经成功构造出逆真空源、实际 $P$ 和 R244 同组强单位的复有理块族，给出一类显式真实有限列，使聚合界失败。固定有界分母阶数时，失败已在一个固定有限次数层发生；分母阶数增到 $o(\sqrt{|B_i|})$ 仍然不能通过全部有限列。

本稿允许复参数及符合所列范数条件的有限组合，不把任意有理块或有限和自动说成扩张或可构造的强单位。证明直接检验实际最小逆，不依赖源具有低次数矩。

## 1. 适用对象及不自动成立的假设

取互不交实际位块 $B_i$，记
$$
q_i=|B_i|=2^{4i},\qquad Q_i=q_i+2,\qquad
c_i=2^{-i-2}=\frac1{4q_i^{1/4}},
$$
$$
f=1+\sum_{i\ge1}c_i\chi_{B_i},\qquad
\lambda=\|f\|^2=49/48,\qquad
c_i^2=\frac1{16\sqrt{q_i}}.
\tag{1.1}
$$
位位置仍可按完整实际 carry 预算远置。$f$ 是一次选定的连续、正且 $C$ 实向量。

在第 $i$ 个纯块上，
$$
T_i=\frac2{Q_i}\sum_{j\in B_i}E_j,\qquad
\|T_i\|<1.
$$
考虑有理块
$$
U_i=N_i(T_i)D_i(T_i)^{-1},\qquad
D_i(z)=\prod_{\ell=1}^{r_i}(z+a_{i\ell}),
$$
$$
0<|a_{i\ell}|\le\frac34,\qquad
b_i=\prod_{\ell=1}^{r_i}(1+|a_{i\ell}|).
\tag{1.2}
$$
空乘积允许 $r_i=0$。假设存在固定常数 $C$，使
$$
\|N_i\|_{\mathrm{coef},1}\le Cb_i.
\tag{1.3}
$$
$N_i$ 可有复系数；其次数不用于下面输入列的次数上界。因为 $D_i$ 的所有根非零而 $T_i$ 幂零，其分母确实可逆。

以下是**构造已经成功**的条件，而不是本稿替任意参数证明的结论：

1. 纯 $U_i$ 扩张，记 $g_i=U_i\Omega$，故 $\|g_i\|\ge1$；
2. 实际提升经过正缩放
   $\widetilde U_i=X_{g_i}/(1-\varepsilon_i)$ 成为扩张，且
   $$16q_i5^{q_i}\max(1,\|g_i\|)\eta_{\min B_i}\le\varepsilon_i,\qquad
   0\le\varepsilon_i<1/2;$$
3. 准确的源块乘积
   $g=\prod_i[g_i/(1-\varepsilon_i)]$ 在 $H$ 中收敛，$M=\|g\|<\infty$；
4. 实际收缩逆积给 $P$、$Pg=1$ 及同一组一致有界强单位。因此 R244 给
   $$G=P^{-1}=X_g,\qquad Gu=X_ug$$
   对每个有限 Walsh 柱成立，且有限柱是实际图核心。

前稿的调块族满足这些条件。也可以允许有限个初块例外，因为以下检验只用充分大的 $i$。

复 Blaschke 逆因子
$$
e^{i\gamma}\frac{I+\overline a T}{aI+T}
$$
的分母和分子满足 (1.2)—(1.3)，且其逆为收缩；单位相位不改变扩张性。任意有限乘积同样满足 (1.3)，常数 $C=1$。是否具有上述实际收敛源仍必须另外证明。

## 2. 准确的低分母消去列

在 $q$ 位纯块中，记
$$
D_j^0=I-2E_j,\qquad
\mathcal E_{q,k}=\sum_{\substack{F\subset B\\|F|=k}}D_F^0,
\qquad
v_{q,k}=\binom qk^{-1/2}\mathcal E_{q,k}\Omega.
$$
因为 $D_F^0\Omega=\chi_F$，准确有 $\|v_{q,k}\|=1$，且它是纯次数 $k$ 的有限 Walsh 列。

为第 $i$ 块选择 $k_i\ge1$，要求
$s_i=r_i+k_i<q_i$。定义
$$
\boxed{
u_i=\frac{D_i(T_i)v_{q_i,k_i}}{b_i}.
}
\tag{2.1}
$$
$\|D_i\|_{\mathrm{coef},1}\le b_i$、$\|T_i\|\le1$，故
$$
\boxed{\|u_i\|\le1.}
\tag{2.2}
$$
由于 $T_i$ 是一次 Walsh 乘子的线性组合，纯关系
$(D_j^0)^2=2D_j^0-I$ 保证 $u_i$ 的 Walsh 次数至多
$s_i=r_i+k_i$。在本节先定义真正有限列，再作实际提升；后面不在实际代数里套用该纯平方关系。

纯有限列乘子准确为
$$
X_{u_i}^0=
\frac{D_i(T_i)\mathcal E_{q_i,k_i}}
 {b_i\sqrt{\binom{q_i}{k_i}}}.
$$
真实有限维有理恒等式给
$$
\boxed{
U_i u_i=\frac{N_i(T_i)v_{q_i,k_i}}{b_i},
\qquad \|U_iu_i\|\le C.
}
\tag{2.3}
$$
这个界不使用任何逆范数估计；分母已被有限列准确消去。

## 3. 全块 Walsh 态的精确指数生成式

固定 $F\subset B$、$|F|=k$，记
$\chi=\chi_B$。定义线性泛函
$$
\ell_{q,k}(p)=2^{-k}
 \langle p(T)D_F^0\chi,\chi\rangle.
\tag{3.1}
$$
不声称它正。按各物理位直接计算，
$$
\boxed{
\ell_{q,k}(e^{t(T+I)})
=e^t(1-t/Q)^{q-k}(1-t/(2Q))^k,
\qquad Q=q+2.
}
\tag{3.2}
$$
解释：未选位给
$\langle e^{(2t/Q)E}\chi,\chi\rangle=1-t/Q$；
已选位给
$\langle e^{(2t/Q)E}D^0\chi,\chi\rangle
=2-t/Q=2(1-t/(2Q))$。
这支付了重复命中同一位的所有纯 Boolean 关系。

令
$$
m_\ell=\ell_{q,k}((T+I)^\ell),\qquad m_0=1,
\qquad \gamma=\frac{2+k/2}{Q}.
$$
在原点的幂级数中，(3.2) 的对数为
$$
\gamma t-
\sum_{n\ge2}
\frac{(q-k)+k/2^n}{nQ^n}t^n.
$$
逐系数取绝对值后，由正系数指数级数主控。于是对 $0\le t\le Q/2$，
$$
\begin{aligned}
\sum_{\ell\ge0}\frac{|m_\ell|}{\ell!}t^\ell
&\le
\exp\left[
\gamma t+
\sum_{n\ge2}
\frac{(q-k)+k/2^n}{nQ^n}t^n\right]\\
&\le\boxed{\exp(\gamma t+t^2/q)}.
\end{aligned}
\tag{3.3}
$$
最后使用
$\sum_{n\ge2}x^n/n\le x^2/[2(1-x)]\le x^2$
对 $0\le x\le1/2$ 成立。

## 4. 任意复分母的相对矩误差

写 $D(z)=\prod_{\ell=1}^r(z+a_\ell)$，
$0<|a_\ell|\le3/4$。由于 $|a_\ell-1|\ge1/4$，
$$
\frac{D(T)}{D(-1)}
=\prod_{\ell=1}^r
\left[I+\frac{T+I}{a_\ell-1}\right]
=\sum_{\ell=0}^r d_\ell(T+I)^\ell,
$$
且
$$
|d_\ell|\le\binom r\ell4^\ell
\le\frac{(4r)^\ell}{\ell!}.
$$
当 $4r\le Q/2$ 时，(3.3) 给
$$
\boxed{
\left|\frac{\ell_{q,k}(D(T))}{D(-1)}-1\right|
\le E(q,r,k):=
\exp\left[\frac{16r^2+2rk+8r}{q}\right]-1.
}
\tag{4.1}
$$
$r=0$ 时误差为零。这里保留的是相对于 $D(-1)$ 的误差，不是会淹没小分母值的绝对误差。

因为 $T$ 和全块 Walsh 态对位排列对称，所有大小为 $k$ 的 $F$ 给相同矩。于是第2节的有限列满足
$$
\boxed{
\langle X_u^0\chi,\chi\rangle
=
2^k\sqrt{\binom qk}\,
\frac{D(-1)}{b}(1+\zeta),
\qquad |\zeta|\le E(q,r,k).
}
\tag{4.2}
$$
又
$$
\boxed{
\frac{|D(-1)|}{b}
=\prod_{\ell=1}^r
\frac{|a_\ell-1|}{1+|a_\ell|}
\ge7^{-r}.
}
\tag{4.3}
$$
复参数只改变一个可明确选择的标量相位，不破坏这个下界。

## 5. 同一正常态的实际矩下界

由于 $s_i=r_i+k_i<q_i$，纯 $X_{u_i}^0$ 的次数不足以将真空和整个 $\chi_{B_i}$ 连接。它只作用在 $B_i$，其他完整块也不能产生交叉项。因此准确有
$$
\phi_f(X_{u_i}^0)
=(\lambda-c_i^2)\langle u_i,\Omega\rangle
+c_i^2\langle X_{u_i}^0\chi_{B_i},\chi_{B_i}\rangle.
\tag{5.1}
$$
(2.2) 将第一项的绝对值控制在 $\lambda$ 以内。

取单位复数 $\tau_i$ 使
$\tau_iD_i(-1)=|D_i(-1)|$。若 $E(q_i,r_i,k_i)\le1/2$，则
$$
\boxed{
\operatorname{Re}\phi_f(X_{\tau_iu_i}^0)
\ge\frac12 A_i-\lambda,\qquad
A_i=c_i^2\,2^{k_i}
 \sqrt{\binom{q_i}{k_i}}\,7^{-r_i}.
}
\tag{5.2}
$$

### 实际 carry 与最小逆

由 $\|u_i\|\le1$ 和最多 $s_i$ 次的有限支撑，
$$
\sum_F|\widehat u_i(F)|
\le\left(\sum_{\ell=0}^{s_i}\binom{q_i}{\ell}\right)^{1/2}
\le\sqrt{s_i+1}\,q_i^{s_i/2}.
$$
逐乘积差给
$$
\boxed{
\Delta_i:=\|X_{u_i}-X_{u_i}^0\|
\le
8s_i3^{s_i}\sqrt{s_i+1}\,
q_i^{s_i/2}\eta_{\min B_i}.
}
\tag{5.3}
$$
若 $s_i=o(\sqrt{q_i})$，其非 carry 部分的对数为
$O(s_i\log q_i)=o(q_i)$。第1节原有 $q_i5^{q_i}\eta$ 预算因此保证
$\Delta_i\to0$；无需把实际乘法当作纯 Boolean 同态。

另一方面，准确源分块及 (2.3) 给
$$
\|X_{u_i}^0g\|
\le CM/\|g_i\|\le CM.
$$
实际最小逆的有限图核心关系于是给
$$
\boxed{
\|G(\tau_i u_i)\|\le CM+M\Delta_i.
}
\tag{5.4}
$$
而实际矩与纯矩相差至多 $\lambda\Delta_i$。所以，只要
$E_i\le1/2$ 且 $A_i\to\infty$，就有
$$
\frac{|\phi_f(X_{\tau_i u_i})|}
 {\|G(\tau_i u_i)\|}\longrightarrow\infty.
\tag{5.5}
$$
这些输入都是同一个实际 $G$ 的合法有限 Walsh 列。

## 6. 固定有界复杂度：一个固定次数层已经失败

若 $r_i\le r_*$，取 $k_i=2$。此时
$s_i\le r_*+2$，
$E(q_i,r_i,2)\to0$，而
$$
A_i
\ge\frac1{4\sqrt{q_i}}
 \sqrt{\frac{q_i(q_i-1)}2}\,7^{-r_*}
=\frac14\sqrt{\frac{q_i-1}{2}}\,7^{-r_*}
\longrightarrow\infty.
\tag{6.1}
$$
因此聚合界已在固定次数至多 $r_*+2$ 的有限列上失败，且每个单块列的比值都趋于无穷。

对 $r_*=1$，前一短稿已有更尖锐的结论：同一调块族在次数二的多块合成列上失败。这里的次数三单列版本换来了对全部固定复有理分母和有限组合的统一证明；不将它说成二次结论的改进。

## 7. 分母阶数增长：$o(\sqrt q)$ 仍然不能通过全列

现在允许 $r_i\to\infty$，但
$$
r_i=o(\sqrt{q_i}).
\tag{7.1}
$$
取
$$
k_i=r_i+2,\qquad s_i=2r_i+2.
$$
则
$$
E(q_i,r_i,k_i)
=\exp[(18r_i^2+12r_i)/q_i]-1\longrightarrow0.
$$
对充分大的 $i$，$k_i\le\sqrt{q_i}$。使用
$\binom qk\ge(q/k)^k$，若 $r_i\ge1$，有
$$
\begin{aligned}
A_i
&\ge\frac1{16\sqrt{q_i}}
 2^{r_i+2}q_i^{(r_i+2)/4}7^{-r_i}\\
&=\frac14
 \left(\frac{2q_i^{1/4}}7\right)^{r_i}
\ge\frac{q_i^{1/4}}{14}
\longrightarrow\infty.
\end{aligned}
\tag{7.2}
$$
$r_i=0$ 的子序列直接由 (6.1) 处理。因此 (5.5) 成立。

这证明，增加每块分母阶数并不足以自动逃离障碍。任何 $o(\sqrt q)$ 的总分母增长，包括固定阶、对数阶和所有 $q^\beta$、$\beta<1/2$，仍被同一个正常态和一列真实有限输入排除。输入次数随块增长是合法的：R244 要求全部有限列，而不是预先固定一个次数截断。

精确误差式还允许小常数平方根阶。例如最终
$r_i\le\sqrt{q_i}/8$ 时，
$E_i\le e^{18/64+o(1)}-1<1/2$，同一证明仍成立。此时 (5.3) 的对数成本仍是 $o(q_i)$。

不声称任意更大阶都失败。若要利用更高阶逃离本结论，首先仍须实际构造收敛的逆源、非零 $P$ 及同组强单位；仅把有理分母写长不支付这些条件。

## 8. 有限组合的准确量词

### 8.1 块内有限线性组合

若每个块内是至多 $K$ 个上述有理逆的线性组合，组合系数绝对和一致不超过 $B$，把所有分母相乘作共同分母。其总阶数记为 $r_i$，共同分母仍满足 (1.2)。对每个分支，补上的其他分母和原分子的系数绝对和，均不超过 $C_0$ 乘以共同 $b_i$，其中 $C_0$ 是有限分支分子预算的统一上界（Blaschke 分支可取 $C_0=1$）；故总分子满足
$
\|N_i\|_{\mathrm{coef},1}\le BC_0 b_i.
$
因此只要这些组合另已证明满足第1节的扩张、源收敛和实际强单位条件，以上结论以 $C=BC_0$ 原样适用。

有限和本身并不自动扩张，也不自动具有收缩逆；本稿没有省略这个检验。

### 8.2 有限个完整逆源的线性组合

还可设
$$
g=\sum_{\nu=1}^K b_\nu g^{(\nu)},
$$
其中各 $g^{(\nu)}$ 是同一物理分块上的已构造乘积源，各块分母满足 (1.2)。假设这个 $g$ 又实际等于某个合格 $P$ 的 $P^{-1}1$。

对每块取所有分支的共同分母，总阶数为
$r_i=\sum_\nu r_i^{(\nu)}$。以共同 $b_i$ 定义同一个 $u_i$。对每一分支，分母消去后的分子是原分子乘以其他分支的分母，范数上界仍由共同 $b_i$ 控制。因此
$$
\|X_{u_i}^0g\|
\le\sum_{\nu=1}^K |b_\nu|\,C_\nu\|g^{(\nu)}\|,
$$
一致有界。实际误差至多 $\Delta_i\|g\|$。正常态矩下界只依赖共同分母，仍为 (5.2)。

所以固定总复杂度、或总阶数 $o(\sqrt{q_i})$ 的这类有限逆源组合也不能满足全列聚合界。这里没有把任意有限个正则器 $P_\nu$ 的线性组合之逆，认作其逆源的线性组合；两者是不同操作。

## 9. 尚未覆盖的方向

本稿控制有共同实际分块、分母根一致留在单位圆内部、分子系数有 (1.3) 预算的族。分母根逼近单位圆、总阶数更大、没有该块结构的正则器，以及 R267 前向无真空原像族都没有被本定理一概排除。

同一 $f$ 非负连续，早已不可能是慢主理想湮灭者。这里的意义是把“更复杂的块或逐步增加分母阶数”所需支付的真实全列障碍写成可检验条件。仍未将一般正常见证的湮灭方程转化为合格正则器，没有给 $P=SR$，普通 ISP 保持开放。
