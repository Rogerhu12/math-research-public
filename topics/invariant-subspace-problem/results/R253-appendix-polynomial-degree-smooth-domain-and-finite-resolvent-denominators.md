# R253 第二附录：全多项式次数光滑域与有限 first 预解乘积的分母障碍

日期：2026-11-13（UTC+8）。作者：normal_states / Astra-ISP-1cf。状态：已证明的实际加强。本文延伸 R253 的 first 共同域附录；不构造正常湮灭见证，不排除 R244 的见证专属配对正则器。

记 $\mathcal N\chi_F=|F|\chi_F$、$\Lambda=I+\mathcal N$，定义
$$
\mathcal D_\infty=\bigcap_{s=0}^{\infty}\operatorname{Dom}\Lambda^s.
$$
本稿证明，对 $S=S_N$ 或 $S_Y$，
$$
\mathcal D_\infty\not\subseteq\operatorname{Ran}S.
$$
进而，任意有限有序 first 有界预解式乘积都不属于 $S B(H)$。
这比只有一阶共同域的障碍更强；全部高阶自然词域和真实 carry 误差均在下文支付。

## 1. 实际次数域和局部算子预算

令
$$
a_j=(j+1)^{-2},\qquad a_\Sigma=\sum_ja_j,\qquad
S_N=\sum_ja_jN_j,\qquad S_Y=\sum_ja_jY_j,
\qquad Y_j=N_j(I+N_j)^{-1}.
$$
这两个原空间算子都单射。实际归一化递归为
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
\eta_j=\alpha_{j+1}/\alpha_j,\qquad
0<\eta_j\le e^{-770\,16^j}.
\tag{1.1}
$$
设 $\eta_*=\sup_j\eta_j<1/4$。

对整数 $s\ge0$，记 $\mathsf H_s=\operatorname{Dom}\Lambda^s$，
范数为 $\|f\|_s=\|\Lambda^sf\|$。
若有界算子 $B$ 只作用于含 $L$ 位的有限块，则
$$
\boxed{
B\mathsf H_s\subseteq\mathsf H_s,\qquad
\|B\|_{\mathsf H_s\to\mathsf H_s}\le(L+1)^s\|B\|.
}
\tag{1.2}
$$
按块外次数 $q$ 分解，块内次数介于 $0,L$，
用 $(q+L+1)^s\le(L+1)^s(q+1)^s$ 即得；
有限和的极限由 $\Lambda^s$ 闭性处理。
这是 R171 的局部次数预算。

R171 还给真实截断
$$
N_j^{[m]}=\sum_{r=j}^{m-1}\frac{\alpha_r}{\alpha_j}
E_j^*\cdots E_{r-1}^*E_r,\qquad j<m,
\tag{1.3}
$$
以及
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad
V_j^{[m]}=(I-N_j^{[m]})(I+N_j^{[m]})^{-1}.
$$
令 $B_{j,r}=V_j^{[r+1]}-V_j^{[r]}$，则
$$
\operatorname{supp}B_{j,r}\subseteq[j,r],\qquad
\|B_{j,r}\|\le18\,\frac{\alpha_r}{\alpha_j},
\qquad
V_j-V_j^{[m]}=\sum_{r\ge m}B_{j,r}.
\tag{1.4}
$$
这里 $Y_j-Y_j^{[m]}=-(V_j-V_j^{[m]})/2$，
其中 $Y_j^{[m]}=N_j^{[m]}(I+N_j^{[m]})^{-1}$。
所有截断均为实际有限头，不是把真实 $N_j$ 直接换成 $E_j$。

由 (1.2)–(1.4) 和
$$
\frac{\alpha_r}{\alpha_j}
=\prod_{\nu=j}^{r-1}\eta_\nu
\le\eta_j\eta_*^{r-j-1}\qquad(r>j),
$$
对每个固定 $s$ 存在 $C_s<\infty$，使
$$
\sup_j\bigl(\|N_j\|_{\mathsf H_s\to\mathsf H_s}
+\|Y_j\|_{\mathsf H_s\to\mathsf H_s}\bigr)\le C_s.
\tag{1.5}
$$
例如纯单个位贡献只付 $2^s$，其余局部项由
$\sum_{\ell\ge1}(\ell+2)^s\eta_*^{\ell-1}<\infty$ 控制。
局部展开在 $\mathsf H_s$ 范数中绝对收敛，保证真正的域保持。

对任意 $b\in\ell^2$，R125/R171 的闭 first 乘子 $X_b$ 满足
$$
X_b\mathsf H_{s+1}\subseteq\mathsf H_s,\qquad
\|X_bf\|_s\le K_s\|b\|_2\|f\|_{s+1}.
\tag{1.6}
$$
其纯创建、消去、对角三项在次数 $q$ 上的范数分别至多
$\sqrt{q+1}\|b\|_2,\sqrt q\|b\|_2,2\sqrt q\|b\|_2$；
实际 carry 用 (1.2)、(1.4) 支付。
因此
$$
X_b\mathcal D_\infty\subseteq\mathcal D_\infty,
\tag{1.7}
$$
任意固定有限个 first 的任意有序自然词都在 $\mathcal D_\infty$ 上有定义。
这里的结论包括逐次复合域，不只是各个一阶域的交。

## 2. 真实有限头加实际尾的截断误差

相对于 $H=K_m\otimes H_m$，令
$$
T_m=
\begin{cases}
\sum_{j<m}a_jN_j^{[m]},&S=S_N,\\
\sum_{j<m}a_jY_j^{[m]},&S=S_Y,
\end{cases}
\qquad
U_m=S_{\ge m}=
\begin{cases}
\sum_{j\ge m}a_jN_j,\\
\sum_{j\ge m}a_jY_j,
\end{cases}
$$
其中 $T_m$ 只作用于前 $m$ 位，$U_m$ 只作用于实际尾。
置
$$
\widetilde S_m=T_m\otimes I+I\otimes U_m,\qquad
R_m=S-\widetilde S_m.
\tag{2.1}
$$
对
$$
A_m=\sum_{j\ge m}a_j\le m^{-1},
$$
(1.5) 给
$$
\|U_m\|_{\mathsf H_s^{\rm tail}\to\mathsf H_s^{\rm tail}}
\le C_s A_m.
\tag{2.2}
$$

在 $r\ge m>j$ 时，
$\alpha_r/\alpha_j\le e^{-770\,16^{r-1}}$。
所以 (1.2)–(1.4) 给两个慢符号共同的实际预算
$$
\boxed{
\|R_m\|_{\mathsf H_s\to\mathsf H_s}
\le\varepsilon_{m,s}:=
9a_\Sigma\sum_{r\ge m}(r+2)^s e^{-770\,16^{r-1}}.
}
\tag{2.3}
$$
$S_N$ 的常数可更小，此处统一取 9。
对每个固定 $s$，$\varepsilon_{m,s}$ 双指数趋零，
特别 $(m+1)^t\varepsilon_{m,s}\to0$ 对每个固定 $t$ 成立。

这里在所有次数图范数中估计了 $R_m$。
后文不会仅用普通算子范数的小误差去断言高阶图收敛。

## 3. 有限物理末端的任意固定长度真链

令 $d=2^m$，按物理头编号取归一化基
$e_0^{(m)},\ldots,e_{d-1}^{(m)}$。
截断的实际 $A$ 为加权前移 $B_m$：
$$
B_me_r^{(m)}
=\alpha_{v_2(r+1)}e_{r+1}^{(m)}
\quad(0\le r<d-1),\qquad
B_me_{d-1}^{(m)}=0.
\tag{3.1}
$$
倒序编号
$$
\epsilon_n^{(m)}=e_{d-1-n}^{(m)}
$$
后，由 $v_2(d-n)=v_2(n)$，有
$$
B_m\epsilon_n^{(m)}
=\alpha_{v_2(n)}\epsilon_{n-1}^{(m)}
\quad(1\le n<d),\qquad
B_m\epsilon_0^{(m)}=0.
\tag{3.2}
$$
所以任意固定长度的物理末端矩阵完全独立于足够大的 $m$。

实际归一化截断满足 $N_j^{[m]}=B_m^{2^j}/d_j$。
对两个 $S$，有限头 $T_m$ 都是同一形式符号在 $B_m$ 上的有限代入：
$$
T_m=\sum_{n=1}^{d-1}c_n(S)B_m^n,\qquad
c_1(S)=a_0/d_0\ne0.
\tag{3.3}
$$
$S_Y$ 的逆在幂零有限头上就是有限几何级数。
这是有限维准确等式，不要求原形式标量级数在某个圆盘收敛。

因此，可以在抽象有限支撑序列空间中依次选择
$$
\xi_0=\epsilon_0,\qquad
\operatorname{supp}\xi_k\subseteq\{0,\ldots,k\},
\qquad
T\xi_k=\xi_{k-1}\quad(k\ge1).
\tag{3.4}
$$
这里 $T$ 表示 (3.2)–(3.3) 给出的相容有限矩阵。
存在性很直接：$T$ 从
$\operatorname{span}\{\epsilon_1,\ldots,\epsilon_k\}$
到 $\operatorname{span}\{\epsilon_0,\ldots,\epsilon_{k-1}\}$
是三角同构，其对角元
$c_1(S)\alpha_{v_2(n)}$ 均非零。
每一步只解一个有限线性系统。

记 $J_m\epsilon_n=\epsilon_n^{(m)}$。
对固定 $p$、$2^m>p$，准确有
$$
T_mJ_m\xi_0=0,\qquad
T_mJ_m\xi_k=J_m\xi_{k-1}\quad(1\le k<p).
\tag{3.5}
$$
$\|\xi_k\|$ 允许随 $k$ 很快增长。
下文先固定 $p$，再选择充分大的 $m$；不假设任何未证的链常数统一界。
此步骤也不调用边界上的无限右逆或未经证明的核稳定性。

## 4. 有限阶校正与全部次数图范数中的残量

定义
$$
v_{m,p}=
\sum_{k=0}^{p-1}(-1)^k
J_m\xi_k\otimes U_m^k\Omega_m.
\tag{4.1}
$$
各项属于 $\mathcal D_\infty$，因为 $J_m\xi_k$ 为有限头向量，
$\Omega_m$ 为尾真空，且 (2.2) 保证 $U_m$ 保持每个次数域。

由 (3.5)，有限和严格望远镜：
$$
\boxed{
\widetilde S_m v_{m,p}
=(-1)^{p-1}J_m\xi_{p-1}\otimes U_m^p\Omega_m.
}
\tag{4.2}
$$
令 $u_m=J_m\xi_0\otimes\Omega_m=e_1^{\otimes m}\otimes\Omega_m$。
对固定 $p$，
$$
\|v_{m,p}-u_m\|
\le\sum_{k=1}^{p-1}\|\xi_k\|(C_0A_m)^k
\longrightarrow0.
\tag{4.3}
$$
所以 $\|v_{m,p}\|\to1$。

若 $x$ 只使用前 $m$ 位，$y$ 为尾向量，
则 $1+\mathcal N_{\rm head}+\mathcal N_{\rm tail}
\le(1+\mathcal N_{\rm head})(1+\mathcal N_{\rm tail})$，
从而
$$
\|x\otimes y\|_s
\le(m+1)^s\|x\|\|y\|_s.
\tag{4.4}
$$
结合 (2.2)，对固定 $p,s$ 存在有限常数 $C_{p,s}$，使
$$
\|v_{m,p}\|_s\le C_{p,s}(m+1)^s.
\tag{4.5}
$$
再由 (2.3)、(4.2)，
$$
\boxed{
\|Sv_{m,p}\|_s
\le C_{p,s}(m+1)^s
\bigl(m^{-p}+\varepsilon_{m,s}\bigr).
}
\tag{4.6}
$$
特别，固定 $p>s$ 时，右侧趋零。
这里的高阶残量是有限头真链与真实尾的显式计算，
不是从一阶图收敛自动提升。

取 $p_n=n+2$。
逐次选择严格增加的 $m_n$，满足 $2^{m_n}>p_n$，并使
$$
\|v_{m_n,p_n}-u_{m_n}\|\le2^{-n-2},
\qquad
\|Sv_{m_n,p_n}\|_s\le2^{-n}
\quad(0\le s\le n).
\tag{4.7}
$$
每次 $p_n$ 和有限多个 $s$ 已固定，所以 (4.3)、(4.6) 保证可选。
令
$$
z_n=\frac{v_{m_n,p_n}}{\|v_{m_n,p_n}\|}.
$$
于是
$$
\boxed{
z_n\in\mathcal D_\infty,\qquad
\|z_n\|=1,\qquad
Sz_n\to0\quad\text{于 }\mathcal D_\infty.
}
\tag{4.8}
$$

## 5. 全多项式次数光滑仍不足以落入慢符号值域

$\mathcal D_\infty$ 以可数范数 $\|\cdot\|_s$ 成为 Fréchet 空间。
完备性可直接逐个使用闭的 $\Lambda^s$，或由 Walsh 加权 $\ell^2$ 形式得到。

反设 $\mathcal D_\infty\subseteq\operatorname{Ran}S$。
因 $S$ 单射，逆
$$
S^{-1}:\mathcal D_\infty\to H
$$
全域定义且图闭：
若 $f_n\to f$ 于 $\mathcal D_\infty$、$S^{-1}f_n\to g$ 于 $H$，
则 $Sg=f$，从而 $g=S^{-1}f$。
Fréchet 到 Banach 的闭图定理迫它连续。
但 (4.8) 给
$$
S^{-1}(Sz_n)=z_n,\qquad \|z_n\|=1,
$$
与 $Sz_n\to0$ 于 $\mathcal D_\infty$ 矛盾。因此
$$
\boxed{
\mathcal D_\infty\not\subseteq\operatorname{Ran}S_N,\qquad
\mathcal D_\infty\not\subseteq\operatorname{Ran}S_Y.
}
\tag{5.1}
$$
两式分别成立；本稿没有额外声称存在同一个向量同时离开两个值域。
所得向量具有所有多项式 Walsh 次数矩，但不由此具有任何正指数次数矩。

## 6. 任意有限有序 first 预解乘积的像障碍

给定 $b^{(1)},\ldots,b^{(k)}\in\ell^2$，
并假设
$$
L_i=(\lambda_i I+X_{b^{(i)}})^{-1}\in B(H).
$$
考虑任意指定次序的乘积
$$
R=L_1L_2\cdots L_k.
$$
准确有
$$
\boxed{\mathcal D_\infty\subseteq\operatorname{Ran}R.}
\tag{6.1}
$$
事实上，对 $f\in\mathcal D_\infty$，依次置
$$
h_0=f,\qquad
h_i=(\lambda_i+X_{b^{(i)}})h_{i-1}.
$$
由 (1.7)，每个 $h_i$ 仍在 $\mathcal D_\infty$，所以整个自然词有定义。
从 $h_k$ 逆序消去，得到
$$
L_1L_2\cdots L_k h_k=f.
$$
不需要把各个闭 first 或各个逆互相换序，也不需要预先证明 $L_i$ 保持 $\mathcal D_\infty$。

结合 (5.1)，
$$
\boxed{
\operatorname{Ran}R\not\subseteq\operatorname{Ran}S,\qquad
R\notin S B(H).
}
\tag{6.2}
$$
这同时排除有限个正 first 逆、复 first 有界预解式，
以及其任意有序有限乘积作为 $S^{-1}$ 的全域有界分母。
若仅假设像包含而未给有界因子，
$S^{-1}R$ 的全域闭图仍会自动给出有界因子，故两种表述一致。

## 7. 量词边界与 q_m 仍待解决的估计

(5.1) 是关于慢符号值域的光滑向量存在性结论，
不是一个正正常理想湮灭态的构造。
(6.2) 也只排除这些预解乘积作为 $S$ 的有界右因子；
它没有排除某个乘积对某个有限输入满足 R244 的配对域条件。

全部多项式次数正则性弱于 R255 的正指数次数条件，
所以本稿与已发布的真实 $\sqrt3$ 端点分解没有冲突。
本稿未声称无穷预解乘积或一般交换正则器具有同一结论。

R253 中
$q_m=\|\omega_m|_{\overline{Q_m\mathcal B_m}}\|$
的真实非消失下界仍开放。
有限相位乘积消元、正常尾必要界，以及这里的分母障碍均为中间结果，
不能替代普通 ISP 的完成标准。

主要已证依赖：R13/R124 的实际有限头与归一化幂；
R125 的闭 first 与有限柱核心；
R171 §§2–4 的真实局部分解、次数域预算和 first 映射性质；
R122/R124 对两个原慢符号的单射性。
