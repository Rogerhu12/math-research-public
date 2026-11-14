# R263：固定正线性指数次数域的值域障碍与共同反例

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：已证明的中间结论。本稿从已发表的
[R230 全部拉伸指数次数域附录](R230-appendix-stretched-degree-domains-and-infinite-resolvent-denominator-obstruction.md)
的实际高位孔链出发，重新给出所需有限链和加权残量，并选择一个固定正线性指数权。
新增结论包括预算端点、同时离开两个慢符号值域的共同向量，以及仅需固定域像包含的统一分母障碍。
非零规范无限正预解式积不能作为慢符号有界右倍数这一结论已由 R230 证明；本文不将其重报为首次结果。

## 1. 结论与准确量词

在原 Haar 空间中，令
$$
H_\sigma=\operatorname{Dom}e^{\sigma\mathcal N},\qquad
\|x\|_\sigma=\|e^{\sigma\mathcal N}x\|,\qquad
\mathcal N\chi_F=|F|\chi_F.
$$
取两个原实际慢符号
$$
S_N=\sum_{j\ge0}(j+1)^{-2}N_j,\qquad
S_Y=\sum_{j\ge0}(j+1)^{-2}Y_j,\qquad
Y_j=N_j(I+N_j)^{-1}.
$$
二者在全 $H$ 上有界且单射，使用既有真实实现，不更改权或边界表示。
置
$$
K=60e^2,\qquad \sigma_*=\frac1{60e^2}.
\tag{1.1}
$$

**定理。**

1. 对 $S=S_N$ 和 $S=S_Y$ 分别存在单位向量 $z_q\in H_1$，使
   $$
   \|Sz_q\|_{\sigma_*}\longrightarrow0.
   \tag{1.2}
   $$
2. 有
   $$
   \boxed{
   H_{\sigma_*}\not\subseteq\operatorname{Ran}S_N,\qquad
   H_{\sigma_*}\not\subseteq\operatorname{Ran}S_Y.
   }
   \tag{1.3}
   $$
   因而每个 $0<\sigma\le\sigma_*$ 也有同样的不包含。
3. 存在同一个向量
   $$
   \boxed{
   f\in H_{\sigma_*}\setminus
   \bigl(\operatorname{Ran}S_N\cup\operatorname{Ran}S_Y\bigr).
   }
   \tag{1.4}
   $$
4. 对任意 $R\in B(H)$，只要
   $H_{\sigma_*}\subseteq\operatorname{Ran}R$，这个同一个 $f$ 就满足
   $$
   f\in\operatorname{Ran}R,\qquad
   f\notin\operatorname{Ran}S_N\cup\operatorname{Ran}S_Y.
   \tag{1.5}
   $$
   特别
   $$
   \boxed{
   R\notin S_NB(H),\qquad R\notin S_YB(H).
   }
   \tag{1.6}
   $$
   不要求 $R$ 单射，也不要求右因子属于交换子代数。

$\sigma_*$ 是下面这套明确常数预算所达到的端点，不声称是实际模型的最佳阈值。
原有 R230 的共同严格次线性拉伸域见证不保证任何正线性指数次数矩；
(1.4) 是本稿的加强。
见证是闭图定理给出的存在性向量，本稿没有给其逐项闭式公式。

## 2. 统一指数尺度上的实际算子

记 $a_j=(j+1)^{-2}$，$\sum_j a_j<2$。
用 $Z_j=N_j$ 或 $Y_j$ 统一表示两个模型。
实际递归为
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
N_j^2=\eta_jN_{j+1},\qquad
E_j=e_{10}^{(j)},\qquad
0<\eta_j\le e^{-770\,16^j}.
\tag{2.1}
$$
$\eta_*=\sup_j\eta_j\le e^{-770}$。
在一位 Walsh 基中，指数次数权是 $\operatorname{diag}(1,e^\sigma)$，
因此 $E_j$ 及 $E_j^*$ 在 $H_\sigma$ 上的范数至多 $e$，对 $0\le\sigma\le1$ 一致。

真实递归的全级数
$$
N_j=\sum_{r=j}^\infty
 \left(\prod_{\ell=j}^{r-1}\eta_\ell\right)
 E_j^*\cdots E_{r-1}^*E_r
$$
在每个 $B(H_\sigma)$ 中绝对收敛，给
$$
\|N_j\|_{B(H_\sigma)}
\le\frac e{1-e\eta_*}<3.
\tag{2.2}
$$
连续嵌入 $H_\sigma\hookrightarrow H$ 保证这就是原算子的限制。

由平方关系，真实左右逆恒等式为
$$
(I+N_j)^{-1}
=(I-N_j)(I-\eta_jN_{j+1})^{-1}.
$$
右侧末因子在这些加权空间内有收敛 Neumann 级数，故
$$
\|(I+N_j)^{-1}\|_{B(H_\sigma)}<5,\qquad
\|Y_j\|_{B(H_\sigma)}<15.
$$
又 $Y(E_j)=E_j$，逆差恒等式与 (2.2) 给两个模型共同的界
$$
\boxed{
\|Z_j\|_{B(H_\sigma)}\le15,\qquad
\|Z_j-E_j\|_{B(H_\sigma)}\le200\eta_j
\quad(0\le\sigma\le1).
}
\tag{2.3}
$$
所以 $S$ 保持全部这些空间，所有以后使用的残量都属于实际加权定义域。

## 3. 高位孔链和全部低头 carry

固定 $q\ge2$，取整数 $m>2q$，令 $J_q=\{q,\ldots,2q-1\}$。
考虑物理张量子空间 $\mathcal W_{q,m}$：
前 $q$ 位及第 $2q,\ldots,m-1$ 位固定为 $e_1$，中间 $J_q$ 位任意，位置 $m$ 以后的尾任意。
置
$$
D_q=\sum_{j\in J_q}a_jE_j,\qquad
U_m=\sum_{j\ge m}a_jZ_j.
$$
这里 $U_m$ 始终是真正尾算子，没有删除进位。
(2.3) 给
$$
\|U_m\|_{B(H_{\ge m,\sigma})}\le\frac{15}{m}.
\tag{3.1}
$$

对 $j<q$，递归在全 $1$ 前缀上准确为
$$
N_j(e_1^{\otimes q}\otimes x)=
 \left(\prod_{\ell=j}^{q-1}\eta_\ell\right)
 e_1^{\otimes j}\otimes e_0^{\otimes(q-j)}\otimes N_qx.
\tag{3.2}
$$
物理 $e_0,e_1$ 的加权范数相同，均为
$\sqrt{(1+e^{2\sigma})/2}$。
因此上述替换没有产生随前缀长度增长的额外损失；
对 $N$、$Y$ 的低头部分可统一用
$15\prod_{\ell=j}^{q-1}\eta_\ell$。
对于 $q\le j<m$，直接使用 (2.3)；
若 $j\notin J_q$，纯 $E_j$ 在填充的 $e_1$ 上为零。
于是
$$
\boxed{
\|(S-D_q-U_m)x\|_\sigma
\le500\eta_{q-1}\|x\|_\sigma
\quad(x\in\mathcal W_{q,m}\cap H_\sigma).
}
\tag{3.3}
$$
所有跨块、块内及低头的真实 carry 都包含在这一界中。

在中间块，用 $e_F$ 表示孔集 $F\subseteq J_q$ 处为 $e_0$、其余为 $e_1$ 的正交物理基。
定义
$$
h_r=\frac1{(q)_r}
 \sum_{\substack{F\subseteq J_q\\|F|=r}}
 \left(\prod_{j\in F}a_j^{-1}\right)e_F,
\quad
(q)_r=q(q-1)\cdots(q-r+1),\quad 0\le r\le q.
\tag{3.4}
$$
$(q)_0=1$，$h_0$ 是块内全 $1$ 单位向量。
每个 $(r-1)$ 元孔集恰有 $q-r+1$ 个前像，故
$$
D_qh_0=0,\qquad D_qh_r=h_{r-1}\quad(1\le r\le q).
\tag{3.5}
$$
又 $a_j^{-1}\le4q^2$ 且 $(q)_r=r!\binom qr$，所以
$$
\|h_r\|
\le\frac{(4q^2)^r}{r!\sqrt{\binom qr}}
\le\frac{(4q^2)^r}{r!}.
\tag{3.6}
$$
不同 $h_r$ 的物理孔次数不同，彼此正交。

## 4. 实际向量和统一的有限残量公式

令
$$
\widetilde h_{r,q,m}
=e_1^{\otimes q}\otimes h_r\otimes e_1^{\otimes(m-2q)},
$$
并令 $\Omega_m$ 为位置 $m$ 后的 Haar 真空。构造
$$
u_{q,m}=\sum_{r=0}^q(-1)^r
 \widetilde h_{r,q,m}\otimes U_m^r\Omega_m.
\tag{4.1}
$$
由 (3.1)，这是 $H_1$ 中的有限和。
正交的头孔层给
$$
\boxed{\|u_{q,m}\|^2
=\sum_{r=0}^q\|h_r\|^2\|U_m^r\Omega_m\|^2\ge1.}
\tag{4.2}
$$
不要求修正项本身趋零。

整个前 $m$ 位头的指数权成本至多 $e^{\sigma m}$。
用 (3.1)、(3.6) 得
$$
\|u_{q,m}\|_\sigma
\le e^{\sigma m}\sum_{r=0}^q\frac{(60q^2/m)^r}{r!}
\le\exp(\sigma m+60q^2/m).
\tag{4.3}
$$
链关系使有限和准确望远镜：
$$
(D_q+U_m)u_{q,m}
=(-1)^q\widetilde h_{q,q,m}\otimes U_m^{q+1}\Omega_m.
$$
由 $q!\ge(q/e)^q$ 再加 (3.3)，得到核心估计
$$
\boxed{
\|Su_{q,m}\|_\sigma
\le e^{\sigma m}
 \left[
 \frac{15}{m}\left(\frac{60e\,q}{m}\right)^q+
 500\eta_{q-1}\exp(60q^2/m)
 \right],
\quad 0\le\sigma\le1.
}
\tag{4.4}
$$
这是 R230 高位孔链的实际统一估计，在此逐项重列，便于核对新的固定权参数。

## 5. 固定正权端点

现在不再让 $\sigma$ 随 $q$ 下降。
取
$$
m_q=\lceil Kq\rceil=Kq+\theta_q,\qquad
0\le\theta_q<1,\qquad K=60e^2,\qquad \sigma_*=\frac1K.
\tag{5.1}
$$
显然 $m_q>2q$。
(4.4) 中第一项的指数部分为
$$
\begin{aligned}
\sigma_*m_q+
q\log\left(\frac{60e\,q}{m_q}\right)
&=q+\frac{\theta_q}{K}
 +q\log\left(\frac1e\frac1{1+\theta_q/(Kq)}\right)\\
&=\frac{\theta_q}{K}
 -q\log\left(1+\frac{\theta_q}{Kq}\right)
\le\frac1K.
\end{aligned}
$$
所以
$$
e^{\sigma_*m_q}\frac{15}{m_q}
 \left(\frac{60e\,q}{m_q}\right)^q
\le\frac{15e^{1/K}}{m_q}\longrightarrow0.
\tag{5.2}
$$
这解释了为什么在指数率恰好平衡的端点仍能得到趋零：剩余 $m_q^{-1}$ 因子未丢掉。

第二项满足
$$
500\eta_{q-1}
 \exp\left(\frac{m_q}{K}+\frac{60q^2}{m_q}\right)
\le500\exp\left[
 -770\,16^{q-1}+q+\frac1K+\frac{60q}{K}
 \right]\longrightarrow0.
\tag{5.3}
$$
因此，取 $z_q=u_{q,m_q}/\|u_{q,m_q}\|$，
(4.2)、(5.2)、(5.3) 就证明 (1.2)。

### 一个便于直接比较的整数参数

取 $m_q=512q$、$\sigma=1/512$ 时，第一项直接为
$$
\frac{15}{512q}
 \left(\frac{60e^2}{512}\right)^q.
$$
因 $e^2<8$，底数小于 $15/16$。
carry 项仍按 $e^{-770\,16^{q-1}+O(q)}$ 衰减。
所以 $H_{1/512}$ 的结论也可不经端点优化而直接验证。

对一般 $m\sim Lq$，这套粗常数预算允许
$\sigma L+\log(60e/L)\le0$；
$\log(L/(60e))/L$ 在 $L=60e^2$ 取得最大值 $1/(60e^2)$。
这仅解释 (1.1) 的选择，不是模型的最优性证明。

## 6. 完整域闭图反证

$H_{\sigma_*}$ 配上述范数是 Hilbert 空间，并连续嵌入 $H$。
若它包含于所选 $S$ 的值域，单射性使
$$
S^{-1}:H_{\sigma_*}\longrightarrow H
$$
全域定义。
这个图是闭的：若 $x_n\to x$ 于 $H_{\sigma_*}$、
$S^{-1}x_n\to y$ 于 $H$，则 $x_n\to x$ 于 $H$，而 $S$ 有界给 $Sy=x$。
因此闭图定理给一个常数 $C$，使
$$
\|S^{-1}x\|\le C\|x\|_{\sigma_*}
\quad(x\in H_{\sigma_*}).
$$
取 $x=Sz_q$，(1.2) 与 $\|z_q\|=1$ 矛盾。
这分别证明两个 (1.3)。

若 $0<\sigma\le\sigma_*$，则
$H_{\sigma_*}\subseteq H_\sigma$；
由较小空间已不包含于值域，较大空间也不包含。
没有把仅在稠密子域成立的逆关系当作全域有界逆。

## 7. 同时离开两个值域的一个向量

在复向量空间 $E=H_{\sigma_*}$ 中，令
$$
U=E\cap\operatorname{Ran}S_N,\qquad
V=E\cap\operatorname{Ran}S_Y.
$$
第 6 节给 $U,V$ 都是真线性子空间。
它们不必闭；这里不使用 Baire 范畴。

两个真线性子空间不可能覆盖一个向量空间。
具体地，若有 $x\notin U$ 且 $x\notin V$，已经完成。
否则取 $x\in V\setminus U$。
因为 $V$ 真，取 $y\notin V$；
若 $y\notin U$ 已完成，否则 $y\in U\setminus V$。
此时 $x+y$ 不在 $U$（否则减去 $y$ 得 $x\in U$），
也不在 $V$（否则减去 $x$ 得 $y\in V$）。
得到 (1.4)。

同一个 $f$ 自动属于每个 $H_\sigma$，$0<\sigma\le\sigma_*$，
也具有全部严格次线性拉伸指数次数矩。
这里的共同性不要求两组近核序列相同。

## 8. 固定域像包含的统一应用

若任意 $R\in B(H)$ 满足 $E\subseteq\operatorname{Ran}R$，
第 7 节已选定的 $f$ 就属于 $\operatorname{Ran}R$。
它依然在两个慢值域之外，证明 (1.5)。
若有 $R=S_NB$ 或 $R=S_YB$，有界或无界域问题均不出现：
对有界 $B$ 直接有 $\operatorname{Ran}R\subseteq\operatorname{Ran}S$，与该 $f$ 矛盾。
这给 (1.6)。

该结论只要求一个固定 $H_{\sigma_*}$ 的像包含，
不要求为所有 $\sigma>0$ 给有限幂型指数逆成本，
所以它的适用条件弱于 R230 分母准则。
本稿不将这一区别扩展到未证明该像包含的其他算子。

R230 的实际无穷逆测试保证，每个非零规范正预解式积 $P$ 都满足
$H_\sigma\subseteq\operatorname{Ran}P$，$\sigma>0$；
有限个有界复杂 first 预解式和非负 first 半群的附加乘积也如此。
[R261 零型加强](R261-infinite-positive-resolvent-inverses-zero-type-degree-domains.md)
还给每个正平方根次数权域的像包含。
故它们全部满足本节前提，并共享同一个 (1.4) 的值域反例。

R253 的尾相位积有 $I\otimes Q_m=SC_m$。
若某个规范非零尾积 $P^{\rm tail}=Q_mB_m$、$B_m$ 有界，
则 $I\otimes P^{\rm tail}=SC_m(I\otimes B_m)$。
将尾行补零后，左边仍是上述全空间规范积，产生矛盾。
此尾分母排除已见 R230；本节只说明它也从固定域版本直接推出。

## 9. 尚未闭合的接口

R244 需要指定正常见证的配对域或聚合矩控制，
而不是要求正则器属于 $SB(H)$。
所以本稿没有排除见证专属的规范正积选择，
没有给 $q_m$ 的非消失下界，
也没有证明所有未知不变限制上的稠密像。
边界 $N=M$ 和普通 Hilbert ISP 的完成标准保持不变。

本稿由失联前已核参数重建，并逐项核对正式 R230 高位孔链；
不将无法取回的旧磁盘字节称为原稿的逐字恢复。
