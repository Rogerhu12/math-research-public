# R265：逐位 Bell 因子消除幅度比损失与 3/2 阶指数尾

日期：2026-11-13（UTC）。作者：kernel。

状态：已证明的中间结论；root及boundary已全文核验。本文将反射差的 Bell 部分精确分配到各选中 $N_j$ 因子。
互异位主项由此不再支付 $(\max|a_j|/\min|a_j|)^r$。
结合 R260 的任意跨度真实导子预算和 R264 的平方规模弱平均，
给出一个统一的幅度排序带宽准则，并覆盖直至 $3/2$ 阶的双侧指数尾。

## 1. 统一选择准则及结论

令
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,\quad a_*\in\mathbb C,
$$
并令 $\rho_n$ 为非零幅度 $|a_j|$ 的非增重排。
允许任意复相位和任意原物理排列。

假设存在趋于无穷的整数幂次 $r$、整数排序起点 $k_r$、
整数 $q_r$ 及常数 $\kappa\in(0,\infty)$，使
$$
q_r/r^2\longrightarrow\kappa.
$$
置
$$
h_r=\lceil3\log_2r\rceil,\qquad
A_r=\rho_{k_r},\qquad
\ell_r=\rho_{k_r+q_r+h_r}.
$$
要求 $\ell_r>0$，并满足
$$
\boxed{
r2^rA_r\longrightarrow0,
\qquad
\limsup_{r\to\infty}
 \frac{\log^+(\ell_r^{-1})}{r^3}<\frac56.
}
\tag{1.1}
$$
只需沿一个这样的幂次子序列成立。

对任意复 $\ell^2$ 指数权
$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2,
$$
仍用 R176 的准确倾斜 first 和有界累积量：
$$
c_j=e^{-2b_j},\qquad R_j=V(c_jN_j),\qquad
X_b=X_u+H_{a,b},
$$
$$
K_\nu=\sum_j a_j^\nu L_\nu(R_j),\qquad \nu\ge2,
$$
$$
L_\nu(v)=
\left.\frac{d^\nu}{dt^\nu}
 \log(\cosh t+v\sinh t)\right|_{t=0}.
\tag{1.2}
$$
其中 $H_{a,b}\in\mathcal A$，$\operatorname{Dom}X_b=\operatorname{Dom}X_u$。

**定理1。** 若 (1.1) 成立，则对任意固定 $d\ge2$ 及原点邻域上的任意固定多变量全纯芽 $\Phi$，
$$
\boxed{
\ker\bigl(X_b-\Phi(K_2,\ldots,K_d)\bigr)=\{0\}.
}
\tag{1.3}
$$
因此所有非零简单根多项式 $q$ 都满足
$$
\boxed{q(u)e^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.4}
$$
非零常数同样包括。

**定理2。** 特别，若存在 $0<\alpha\le3/2$、
$0<\beta_-\le\beta_+<\infty$、$c,C>0$ 及 $n_0$，使
$$
\boxed{
c e^{-\beta_+n^\alpha}
\le\rho_n\le
C e^{-\beta_-n^\alpha}
\qquad(n\ge n_0),
}
\tag{1.5}
$$
则 (1.3)—(1.4) 全部成立。
上下指数率不必相同。
结论只依赖幅度多重集，因此保留任意物理重排和任意复相位。

## 2. 固定元组、真实反射差及沿线差商

固定 $a,b,d,\Phi$，置
$$
Y=\Phi(\mathbf K),\quad
\mathbf K=(K_2,\ldots,K_d),\quad
T=X_b-Y,\quad M=\ker T,\quad
\mathcal D=\operatorname{Dom}T.
$$
$T$ 使用原真实闭域；不假定 $a\in\ell^1$。
所有 $\mathcal A$ 元素保持 $\mathcal D$ 并与 $T$ 完整交换。

设 $F$ 是有限位集。令
$$
J_F=\prod_{j\in F}M_{\chi_j},\quad
\gamma_F(Q)=J_FQJ_F,\quad
R_j^-=V(-c_jN_j).
$$
定义
$$
\widehat X_F=X_b+\sum_{j\in F}a_j(R_j^--R_j),
$$
$$
\widehat K_{\nu,F}
=K_\nu+\sum_{j\in F}a_j^\nu
 \bigl(L_\nu(R_j^-)-L_\nu(R_j)\bigr),\quad
\widehat Y_F=\Phi(\widehat{\mathbf K}_F),
$$
$$
A_F=(\widehat X_F-\widehat Y_F)-T,\qquad
E_F=\gamma_F(T)-(\widehat X_F-\widehat Y_F).
\tag{2.1}
$$
所有 $\widehat K_{\nu,F}$ 都在同一个交换 $\mathcal A$ 中且字符为零。
$A_F\in\mathcal A$，故 $[T,A_F]=0$ 在完整域成立。

下文的集合满足
$$
\max_{j\in F}|a_j|\to0,\qquad
\sum_{j\in F}|a_j|^2\to0.
\tag{2.2}
$$
固定原元组的一个小多圆周 $\Gamma$，位于 $\Phi$ 的解析域内并围住零联合谱。
由固定 $L_\nu$ 的多项式范数估计，
$$
\|\widehat K_{\nu,F}-K_\nu\|
\le C_\nu\sum_{j\in F}|a_j|^\nu
\le C_\nu'\sum_{j\in F}|a_j|^2\to0.
$$
所以在同一多圆周上，所有路径元组
$$
\mathbf K+t(\widehat{\mathbf K}_F-\mathbf K),\qquad 0\le t\le1
$$
的坐标预解式都具有与 $F,t$ 无关的固定界。

因为原坐标、差坐标及路径坐标全在同一个交换代数中，
真实 Cauchy 微分给
$$
\frac d{dt}\Phi(\mathbf K+t(\widehat{\mathbf K}_F-\mathbf K))
=
\sum_{\nu=2}^d(\widehat K_{\nu,F}-K_\nu)
 (\partial_\nu\Phi)(\mathbf K+t(\widehat{\mathbf K}_F-\mathbf K)).
$$
定义
$$
D_{\nu,F}
=\int_0^1
(\partial_\nu\Phi)(\mathbf K+t(\widehat{\mathbf K}_F-\mathbf K))\,dt.
$$
于是
$$
\boxed{
\widehat Y_F-Y
=\sum_{\nu=2}^d
(\widehat K_{\nu,F}-K_\nu)D_{\nu,F},
\qquad
D_{\nu,F}\in\mathcal A,\quad
\sup_{\nu,F}\|D_{\nu,F}\|<\infty.
}
\tag{2.3}
$$
差商允许依赖整个 $F$。只需要其统一范数界及在同一交换代数中的归属，
不要求它对 $F$ 或对选中位独立。
这是实际多圆周演算及有界积分，不是形式消除多变量分母。

## 3. A_F 的精确逐位 N_j 因子

有真实恒等式
$$
R_j^--R_j
=4c_jN_j(I-c_j^2N_j^2)^{-1}.
\tag{3.1}
$$
$R_j^-,R_j$ 彼此交换。
对固定多项式 $L_\nu$，定义其准确二变量多项式差商
$$
L_\nu(x)-L_\nu(y)=(x-y)\mathcal L_\nu(x,y).
$$
因此
$$
L_\nu(R_j^-)-L_\nu(R_j)
=4c_jN_jQ_j\,\mathcal L_\nu(R_j^-,R_j),
\qquad
Q_j=(I-c_j^2N_j^2)^{-1}.
\tag{3.2}
$$

$c_j=e^{-2b_j}\to1$，且全部 $I\pm c_jN_j$ 的逆在 $j$ 上一致有界；
大位由 $N_j^2=\eta_jN_{j+1}$，有限低位由准幂零性分别支付。
故 $R_j^\pm,Q_j,\mathcal L_\nu(R_j^-,R_j)$ 全部一致有界，并有
$$
\|Q_j-I\|\le C\eta_j.
\tag{3.3}
$$

将 (3.2) 代入 (2.3)，得到准确的有限和
$$
\boxed{
A_F=4\sum_{j\in F}a_jc_jN_j(I+Z_{j,F}),
}
\tag{3.4}
$$
其中
$$
I+Z_{j,F}
=
Q_j\left[
 I-\sum_{\nu=2}^d a_j^{\nu-1}
 \mathcal L_\nu(R_j^-,R_j)D_{\nu,F}
\right].
\tag{3.5}
$$
每个因子属于 $\mathcal A$，因而与所有 $N_k$、所有其他该类因子及 $T$ 完整交换。
由 (2.3)、(3.3) 及固定 $a\in\ell^2\subset\ell^\infty$，
$$
\boxed{
\|Z_{j,F}\|\le C_Z(|a_j|+\eta_j).
}
\tag{3.6}
$$
$C_Z$ 不依赖 $F$ 或 $j$。
对后面的高位小系数集合，$I+Z_{j,F}$ 甚至是实际单位；
但证明只需要 (3.6)，不需要消去这些单位。

这是与粗 Bell 差估计不同的关键：
每个 $O(a_j^2)$ 的 Bell 项都保留了同一个实际 $c_jN_j$ 因子。
互异位主项可逐位消去全部 $a_jc_j$，而不用最小幅度估计去吸收最大幅度。

## 4. 精确选位与任意跨度的全部真实导数预算

从幅度排序的 $q_r+h_r$ 个秩
$$
\{k_r,\ldots,k_r+q_r+h_r-1\}
$$
对应的实际位中，删除物理位置 $j<h_r$ 的项。
至多删除 $h_r$ 项，故可选出恰有 $q_r$ 项的集合 $I_r$。
它满足
$$
\boxed{
\min I_r\ge h_r,\qquad
\ell_r\le|a_j|\le A_r\quad(j\in I_r).
}
\tag{4.1}
$$
因为 (1.1) 给 $rA_r\to0$、$rA_r^2\to0$，
全部 $r$ 元子集 $F\subset I_r$ 均满足 §2 的统一轮廓条件。

这里使用 R260 已证明的实际任意跨度估计。
为准确记录其域输入，令
$$
\|B\|_\delta=\sum_{s\ge0}\frac{\|\operatorname{ad}_T^sB\|}{s!},
$$
其中每阶导数都要求保持同一个 $\mathcal D$ 并在该完整域满足交换子恒等式。
该类是幺 Banach 代数：闭性由
$B_n\to B$、$\delta B_n\to C$ 和 $T$ 闭性逐阶支付，乘积由完整 Leibniz 公式支付。

任意 $\min F\ge h$ 的反射误差按最高物理位 $\ell$ 分解为局部壳。
壳只在 $F\cap(j,\ell]\ne\varnothing$ 时出现，范数为
$O(\alpha_\ell/\alpha_j)$；加权收集后得到
$$
\|B_{\nu,\ell,F}\|\le C_\nu\eta_{\ell-1},\qquad \ell\ge h.
$$
每壳与同一个闭尾 $X_{b,>\ell}$ 完整交换，因此
$$
\|\operatorname{ad}_T^sB_{\nu,\ell,F}\|
\le [C(1+\sqrt{\ell+1})]^s\|B_{\nu,\ell,F}\|.
$$
在上述 Banach 范数中求和，并用小误差 Neumann 逆处理多变量预解式，
得到
$$
\boxed{
E_F\mathcal D\subseteq\mathcal D,\qquad
\|\operatorname{ad}_T^sE_F\|
\le s!\varepsilon_h,\qquad
\varepsilon_h\le C_Ee^{-385\,16^{h-1}}.
}
\tag{4.2}
$$
每阶导数都保 $\mathcal D$。常数与 $|F|$、$\max F$ 无关。
对 $h=h_r$，
$$
\boxed{\varepsilon_{h_r}\le C_Ee^{-(385/16)r^{12}}.}
\tag{4.3}
$$
这一步不要求 $T$ 有界，因此定理1并未暗中假设 $\ell^1$。

对 $f\in M$，$v=J_Ff$ 处于 $\mathcal D$，且
$Tv=-(A_F+E_F)v$。
完整域递归
$$
Q_0=I,\qquad Q_{n+1}=\operatorname{ad}_TQ_n-Q_n(A_F+E_F)
$$
同时证明 $v\in\operatorname{Dom}T^n$ 和 $T^nv=Q_nv$。
给 $A_F$ 权1、给 $\operatorname{ad}_T^sE_F$ 权 $s+1$；
系数绝对值总和至多 $(n+1)!$，各导数阶乘的乘积至多 $n!$。
因此
$$
\boxed{
\|T^rJ_Ff-(-A_F)^rJ_Ff\|
\le(r+1)!\,r!\,\varepsilon_{h_r}
 (1+\|A_F\|)^r\|f\|.
}
\tag{4.4}
$$
这保留了 R260 对任意跨度付清的真实自然域。

## 5. 输入成本

令
$$
p_F=\prod_{j\in F}a_jc_j,\qquad
\mathcal B_r=\frac1{(-2q_r)^r}
 \sum_{\substack{F\subset I_r\\|F|=r}}p_F^{-1}J_F.
\tag{5.1}
$$
$c_-:=\inf_j|c_j|>0$，所以绝对系数和满足
$$
S_r\le\frac{(2c_-\ell_r)^{-r}}{r!}.
$$
由 (1.1)，可固定一个 $\Lambda<5/6$，使充分大 $r$ 时
$$
\boxed{
\|\mathcal B_r\|\le S_r
\le\frac{\exp(\Lambda r^4+O(r))}{r!}.
}
\tag{5.2}
$$

由 (3.4)、(3.6)，
$$
\|A_F\|\le C rA_r(1+C(A_r+\bar\eta_{h_r}))\longrightarrow0.
$$
(4.4) 经 $S_r$ 求和后的非交换误差至多
$$
\boxed{
\varepsilon_{h_r}\exp(\Lambda r^4+O(r\log r))\|f\|
\longrightarrow0.
}
\tag{5.3}
$$
这里全部输入分母、求和项数和额外阶乘都已经计入。

## 6. 互异位主项不再付幅度比

置
$$
U_{j,F}=I+Z_{j,F},\qquad
\delta_r=C_Z(A_r+\bar\eta_{h_r}).
$$
这些因子都在同一个交换代数中，$\|U_{j,F}-I\|\le\delta_r$。
由 (3.4)，$A_F^r$ 的全部互异指标项准确等于
$$
\boxed{
4^rr!p_F\left(\prod_{j\in F}N_j\right)
 \left(\prod_{j\in F}U_{j,F}\right).
}
\tag{6.1}
$$
即使 $U_{j,F}$ 依赖整个 $F$，这一恒等式仍成立：
对固定 $F$ 的 $r!$ 个排列，各个有界因子彼此交换。

有统一界
$$
\left\|\prod_{j\in F}U_{j,F}-I\right\|
\le(1+\delta_r)^r-1\le e^{r\delta_r}-1.
$$
与 (5.1) 的系数相乘后，$p_F$ 完全消去，
主项总系数绝对值不超过
$(2/q_r)^r r!\binom{q_r}r\le2^r$。
因此由近单位因子造成的全部误差至多
$$
\boxed{
2^r(e^{r\delta_r}-1)\|f\|
\le r2^r\delta_r e^{r\delta_r}\|f\|\longrightarrow0.
}
\tag{6.2}
$$
这是 (1.1) 第一条的准确用途。
该估计不含 $A_r/\ell_r$。

### 6.1 重复位仍保留真实进位

其余项至少含某个 $N_j^2=\eta_jN_{j+1}$。
所有 $U_{j,F}$ 与全部 $N_k$ 交换，所以这个因子不会在展开中丢失。
因 $\|N_j\|\le1$，
$$
\left\|A_F^r-
4^rr!p_F\prod_{j\in F}N_j\prod_{j\in F}U_{j,F}\right\|
\le\bar\eta_{h_r}(C rA_r)^r e^{r\delta_r}.
$$
乘完整 $S_r$ 后，其上界至多
$$
\bar\eta_{h_r}\exp(\Lambda r^4+O(r\log r))\|f\|\longrightarrow0.
\tag{6.3}
$$
这里可以粗用最小幅度，因为超快进位足以吸收该四次成本；
它不是互异主项的误差。

最后，
$$
E_jJ_j=E_j,\qquad
\left\|\left(\prod_{j\in F}N_j\right)J_F-\prod_{j\in F}E_j\right\|
\le r\bar\eta_{h_r}.
$$
相应总误差不超过 $2^rr\bar\eta_{h_r}\|f\|\to0$。

结合 (5.3)、(6.2)—(6.3)，令
$$
C_{I_r}=\frac2{q_r}\sum_{j\in I_r}E_j,
$$
便得到完整自然域和统一误差
$$
\boxed{
\mathcal B_rM\subseteq\operatorname{Dom}T^r,\qquad
\|T^r\mathcal B_rf-C_{I_r}^{\,r}f\|
\le\epsilon_r\|f\|,\quad \epsilon_r\to0.
}
\tag{6.4}
$$

## 7. 非零弱主项与最高交换子配对

R264 的全 Haar 弱平均给
$$
\|C_{I_r}^{\,r}\|\le(1+1/q_r)^r,
$$
并且对任意固定有限柱 $f,g$，充分大 $r$ 时
$$
\langle C_{I_r}^{\,r}f,g\rangle
=\frac{(q_r)_r}{q_r^r}\langle f,g\rangle.
$$
因 $q_r/r^2\to\kappa>0$，
$$
\frac{(q_r)_r}{q_r^r}\longrightarrow e^{-1/(2\kappa)}.
$$
一致范数界及有限柱稠密性给整个原 Haar 空间的 WOT 极限。
由 (6.4)，
$$
\boxed{
T^r\mathcal B_rf\rightharpoonup
\theta_\kappa f,\qquad
\theta_\kappa=e^{-1/(2\kappa)}>0
\quad(f\in M).
}
\tag{7.1}
$$

对任意固定有限局部矩阵 $D$，R259/R260 的完整尾域分解为
$$
T=Z_H+A U_H,\qquad U_H\in\mathcal A,
$$
其中 $D$ 与闭尾 $Z_H$ 完整交换。
有限低头的 $R_j-I$、$L_\nu(R_j)$ 差各有明确的有界 $A$ 因子，
多变量预解式差保留该因子。
因此全部自然域的 Leibniz 公式均合法，且
$$
\boxed{
\|\operatorname{ad}_T^rD\|
\le\|D\|(2\|U_H\|)^r
 \exp\left[-\frac56r^4+105r^3\right].
}
\tag{7.2}
$$

$T$ 是完整域上的 $C$ 自伴算子。
对 $f,g\in M$，令 $v_r=\mathcal B_rf$；
最高交换子配对给
$$
\mathcal B(DT^r\mathcal B_rf,g)
=(-1)^r\mathcal B((\operatorname{ad}_T^rD)\mathcal B_rf,g).
$$
由 (5.2)、(7.2)，右端绝对值趋零，因为
$$
-\left(\frac56-\Lambda\right)r^4+105r^3+O(r)\longrightarrow-\infty.
$$
由 (7.1)，左端趋于 $\theta_\kappa\mathcal B(Df,g)$。
$\theta_\kappa\ne0$，所以
$$
\mathcal B(Df,g)=0
\quad(f,g\in M,\ D\text{ 任意固定局部矩阵}).
$$
局部全矩阵代数在原 Haar 表示中不可约。
取非零 $f=g\in M$ 会使 $Cf$ 正交于 $f$ 的稠密局部轨道，矛盾。
因此 $M=0$，证明定理1的排核结论。

简单根 $q$ 的多变量隐函数分支、准确自然乘积域和
R176 的加权图循环判据与 R259/R260 相同，遂得 (1.4)。
没有将一般重复根的伴随矩阵当作交换标量分支。

## 8. 双侧指数幅度直到 alpha=3/2

现验证 (1.5) 足以实现选择准则。
固定 $\lambda>\log2$，例如 $\lambda=2$，取
$$
k_r=\left\lceil(\lambda r/\beta_-)^{1/\alpha}\right\rceil.
\tag{8.1}
$$
于是
$$
A_r=\rho_{k_r}\le C e^{-\lambda r},
\qquad r2^rA_r\longrightarrow0.
\tag{8.2}
$$

若 $0<\alpha<3/2$，取 $q_r=r^2$。
由下界，
$$
\log^+(\ell_r^{-1})
\le \beta_+(k_r+q_r+h_r)^\alpha+O(1)
=O(r+r^{2\alpha}+(\log r)^\alpha)
=o(r^3).
$$
所以 (1.1) 第二条成立。

若 $\alpha=3/2$，取
$$
\kappa=(4\beta_+)^{-2/3},\qquad
q_r=\lceil\kappa r^2\rceil.
\tag{8.3}
$$
此时 $k_r=O(r^{2/3})$、$h_r=O(\log r)$，所以
$$
\limsup_{r\to\infty}
\frac{\log^+(\ell_r^{-1})}{r^3}
\le\beta_+\kappa^{3/2}=\frac14<\frac56.
\tag{8.4}
$$
同样满足全部选择条件。
其 WOT 标量是固定严格正数
$e^{-1/(2\kappa)}$，大小不影响最后排核。

这证明定理2。
临界上界来自平方规模平均所需的 $q_r\asymp r^2$
及真实局部交换子的四次衰减；并非把一个 $o(r^4)$ 误写成临界阶。

## 9. 不同指数幂的一个附带子类

统一选择准则还立即允许上下指数幂不同。
若存在
$$
0<\alpha_-\le\alpha_+\le3/2,\qquad
\alpha_+<3\alpha_-,
$$
以及固定正常数，使
$$
c e^{-B n^{\alpha_+}}\le\rho_n
\le C e^{-b n^{\alpha_-}}
$$
最终成立，则同样有定理1的全部结论。

确实，取
$k_r=\lceil(\lambda r/b)^{1/\alpha_-}\rceil$。
第一条件仍由 $e^{-\lambda r}$ 支付。
若 $\alpha_+<3/2$，
$$
\log^+(\ell_r^{-1})
=O(r^{\alpha_+/\alpha_-}+r^{2\alpha_+}+(\log r)^{\alpha_+})
=o(r^3).
$$
若 $\alpha_+=3/2$，不等式 $\alpha_+<3\alpha_-$ 使
$k_r=o(r^2)$，再取 $q_r\sim\kappa r^2$、
$B\kappa^{3/2}=1/4$ 即可。

例如幅度 $\rho_n=e^{-n\log(n+1)}$
在充分大 $n$ 时夹于 $e^{-n^{4/3}}$ 与 $e^{-n}$ 之间，
所以这类幅度及其任意物理重排也已覆盖。
这里的比较只用于验证明确的序列界，没有更改原算子或原常数项。

## 10. 范围

本稿新增并支付了：

- 多变量差商依赖整个选中集合时的统一实际范数界；
- 每个位保留 $c_jN_j$ 的准确因式，及全部因子的共同交换性；
- 互异主项只付 $2^r r\max|a_j|$，不付幅度比的 $r$ 次方；
- 重复位仍保留实际 $\eta_j$，允许用粗最小幅度吸收；
- 任意跨度完整域、平方规模 WOT 主项及四次局部配对；
- 一般排序带宽准则，特别全部 $0<\alpha\le3/2$ 的双侧指数幅度。

没有声称所有 $\ell^2$ 行自动满足 (1.1)。
超临界指数幅度、可能含大幅跳跃的稀疏行、一般重复根多项式、
任意不变限制上的稠密像及正常湮灭者问题仍须各自的真实证明。
普通 Hilbert 不变子空间问题仍未完成。

## 依赖

R176：真实倾斜、Bell 多项式和加权图循环判据。
R259：多变量演算与固定局部 $A$ 因子。
R260：任意物理跨度的真实导子 Banach 代数及自然幂误差。
R264：平方规模平均的全 $H$ WOT 极限。
R109：原 $A$ 幂的四次范数界。

同步：R236另已关闭规范交替调和行的全部重数；本文保留的是一般行重复根问题，不撤销规范结论。
