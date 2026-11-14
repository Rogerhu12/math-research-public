# R254 第六附录：顶部两层的真实高尾修复与稳定像提升

日期：2026-11-13（UTC）。作者：boundary。状态：已证明的中间接口；root已全文核验真实域、支撑、弱闭性及量化配对；$N=M$ 未闭合。

接续 [R254第四附录](R254-appendix-mixed-finite-hole-right-inverse-and-equation-repair.md)、[第五附录](R254-appendix-simultaneous-pure-kernel-and-low-mixed-equation-approximation.md)，以及[R239真实正则提升](R239-appendix-mixed-low-hole-kernel-regular-lift-to-stable-range.md)。本稿将顶部两层输出准确消掉，所得向量是真混合核向量，并能提升到实际 $N$。尚未付清的是新增高尾修复向量的 Hilbert 范数；它不能由低孔坐标保持或进位修正很小自动得到。

## 1. 保留记号与右逆的最低输出次数

仍在去掉原第 $0$ 位后的平方核 $K=\ker P$ 上工作。前 $m$ 个尾位是原物理位 $1,\ldots,m$，$d=2^m$，
$$
P_m=D^2+Q_m,\qquad
Q_m=\sum_{\ell=1}^{d-1}C_m^\ell R_{\ell,m}(D),\qquad
\deg R_{\ell,m}\le2.
$$
$N/Y$ 两型均使用其原真实混合符号。记
$$
\mathcal G_m=H\sum_{k=0}^{d-1}(-Q_mH)^k
$$
为 R254 第四附录的实际有限孔右逆，$H$ 严格增加两次尾孔，$D^2H=I$。
$Q_m$ 只降低 $0,1,2$ 次尾孔，故 $Q_mH$ 不降低尾孔。由此不只得到最高输出次数，还得到
$$
\boxed{
\mathcal G_m\mathcal H_p
\subseteq\bigoplus_{j=p+2}^{p+2d}\mathcal H_j.
}
\tag{1.1}
$$
有限孔输入上准确有 $P_m\mathcal G_m=I$。

另用伴随多项式
$$
\mathcal A_m=\sum_{k=0}^{d-1}(-Q_m)^kD^{2(d-1-k)},
\qquad \mathcal A_mP_m=D^{2d}.
\tag{1.2}
$$

## 2. 从交集低部到真正混合核

取
$$
v\in\ker D^{2d}\cap\mathcal H_{\le q},
\qquad P_{\le q-2}P_mv=0.
$$
于是
$$
r=P_mv\in\mathcal H_{q-1}\oplus\mathcal H_q.
$$
定义
$$
c=\mathcal G_mr,\qquad k=v-c.
\tag{2.1}
$$
由真实右逆及 (1.1)，
$$
\boxed{
P_mk=0,\qquad
c\in\bigoplus_{j=q+1}^{q+2d}\mathcal H_j.
}
\tag{2.2}
$$
此外，由 (1.2)，
$$
D^{2d}c=\mathcal A_mP_mc
=\mathcal A_mr
=\mathcal A_mP_mv=D^{2d}v=0.
$$
所以
$$
\boxed{
c,k\in\ker D^{2d},\qquad
k\in\ker P_m\cap\mathcal H_{\le q+2d}.
}
\tag{2.3}
$$
低孔部分完全保持：
$$
P_{\le q}k=v.
\tag{2.4}
$$
并且由于 $v,c$ 的尾孔支撑正交，
$$
\boxed{\|k\|^2=\|v\|^2+\|c\|^2.}
\tag{2.5}
$$
特别，不能从 (2.4) 推断 $\|k\|$ 受 $\|v\|$ 的统一常数控制。

R254 第四附录给
$$
\|c\|\le B_{m,q}\|r\|,
$$
$$
\log B_{m,q}
=14dq+14d^2+3d\log(m+q+2d+1)+d\log324+\log d.
\tag{2.6}
$$
这个预算不含头相似条件数，但仍随 $q,d$ 增长。

## 3. 对每个实际核向量的具体序列

固定 $u\in K$，取
$$
q=25d^3.
$$
令 $\mathsf V_{m,q}$ 是 R254 第五附录中
$$
\ker D^{2d}\cap\ker(P_{\le q-2}P_m)
$$
的正交投影，并定义
$$
v_m=P_{\le q}\mathsf V_{m,q}u.
\tag{3.1}
$$
该附录已经证明它与粗截断 $P_{\le q}$ 交换。
其构造还逐低孔给出
$$
\|v_m-P_{\le q}u\|\le e^{-500d^4}\|u\|.
\tag{3.2}
$$
这里不能只从全空间距离界推出 (3.2)：需要用已证的粗直和分解和低部分最佳逼近性。

因为高尾孔数超过 $q$ 必使原全部孔次数超过 $q$，$q\to\infty$ 时
$\|P_{>q}u\|\to0$。
于是
$$
\boxed{v_m\longrightarrow u\quad\text{于 Hilbert 范数}.}
\tag{3.3}
$$
同时 $\|v_m\|\le\|u\|$，并满足 §2 的全部精确假设。
置
$$
r_m=P_mv_m,\quad c_m=\mathcal G_mr_m,\quad k_m=v_m-c_m.
$$
那么
$$
\boxed{
k_m\in\ker P_m\cap\mathcal H_{\le q+2d},\qquad
P_{\le q}k_m=v_m,
}
\tag{3.4}
$$
且 $r_m$ 仅在最上 $q-1,q$ 两层。

$P_m$ 不升尾孔，所以
$$
r_m=P_{\{q-1,q\}}P_mP_{\{q-1,q\}}v_m.
$$
因此
$$
\boxed{
\|r_m\|
\le\|P_{\{q-1,q\}}v_m\|
\le \|P_{\{q-1,q\}}u\|+e^{-500d^4}\|u\|
\longrightarrow0.
}
\tag{3.5}
$$
最后的极限只使用孔数趋于无穷，不要求位置尾或次数尾的衰减速率。

(2.6) 与 $q=25d^3$ 给，对全部 $m\ge4$，
$$
\boxed{\log B_{m,q}\le351d^4.}
\tag{3.6}
$$
验证：用 $m+q+2d+1\le27d^3$、$\log27<4$、$\log324<6$、
$\log d\le d/2$，除 $350d^4$ 外的正项至多
$(37/2)d^2+19d<d^4$，对 $d\ge16$ 成立。

## 4. 已付清的实际 $N$ 提升

使用 R239 正则提升的多项式首位图
$$
J_mu=(u,-H_mu),\qquad \|J_m\|\le5/4,
$$
其中 $H_m=A_m$（$N$ 型），
$H_m=(I-\eta C_m)A_m-\eta C_m$（$Y$ 型）。
它在纯高尾次数上只降低零次或一次。

R239 给
$$
\Lambda_{m,Q}:\ker P_m\cap\mathcal H_{\le Q}\longrightarrow N
$$
及
$$
\|\Lambda_{m,Q}k-J_mk\|\le\delta_{m,Q}\|k\|.
$$
当 $m\ge4$、$Q\le50d^3$ 时，其明确公式单调给
$\delta_{m,Q}\le e^{-1000d^4}$。

取 $Q=q+2d\le50d^3$，定义真正的稳定像向量
$$
\boxed{n_m=\Lambda_{m,q+2d}k_m\in N.}
\tag{4.1}
$$
由 $\|P_m\|<1$、$\|v_m\|\le\|u\|$、(2.6)、(3.6)，
$$
\|c_m\|\le e^{351d^4}\|u\|,\qquad
\|k_m\|\le2e^{351d^4}\|u\|.
$$
故
$$
\boxed{
\|n_m-(J_mv_m-J_mc_m)\|
\le e^{-648d^4}\|u\|
\quad(m\ge4).
}
\tag{4.2}
$$
真实进位修正已经足够小，即便使用当前最粗高尾修复范数也能支付它。

由于 $c_m$ 的尾孔支撑在 $[q+1,q+2d]$，而 $J_m$ 最多降低一次尾孔，
$$
J_mc_m\text{ 只支持尾孔 }[q,q+2d].
\tag{4.3}
$$
因此 $n_m$ 的低于 $q$ 孔部分与 $J_mv_m$ 相差至多 (4.2)。
结合 $J_m\to J$ 的已证真实进位界和 (3.3)，它在每个固定低孔测试上趋于 $Ju$。
但 (2.5) 仍允许 $\|n_m\|$ 发散，不能把这一低孔收敛改成弱 Hilbert 收敛。

## 5. 真缺陷必迫这些高尾修复发散

现在再假设 $0\ne w=Ju\in M\ominus N$。
由 $n_m\in N$，$\langle n_m,w\rangle=0$。
(4.2) 因而给
$$
\langle J_mc_m,w\rangle
=\langle J_mv_m,w\rangle+o(1).
$$
已知 $J_mv_m\to Ju=w$，所以
$$
\boxed{\langle J_mc_m,w\rangle\longrightarrow\|w\|^2.}
\tag{5.1}
$$
内积采用第一变量线性的约定。

记 $\tau_{q-1}(w)$ 为原全部物理孔次数超过 $q-1$ 的 Hilbert 尾。
由 (4.3)，
$$
|\langle J_mc_m,w\rangle|
\le\frac54\|c_m\|\tau_{q-1}(w).
$$
因此，对每个固定非零真缺陷，充分大 $m$ 有
$$
\boxed{
\|c_m\|\tau_{q-1}(w)\ge\frac25\|w\|^2,
\qquad q=25d^3.
}
\tag{5.2}
$$
由 (2.6)，同一结论也准确给出顶部残量的必要乘积下界
$$
\boxed{
B_{m,q}\,\|r_m\|\,\tau_{q-1}(w)
\ge\frac25\|w\|^2.
}
\tag{5.3}
$$
结合 (3.5)，可进一步把 $\|r_m\|$ 换为
$\|P_{\{q-1,q\}}u\|+e^{-500d^4}\|u\|$。
这是一条移动两层残量的必要条件，没有声称它数值上强于 R249 的次数尾界。

特别
$$
\boxed{\|c_m\|\longrightarrow\infty.}
\tag{5.4}
$$
这是确实使用 $w\perp N$ 的必要条件，不是对整个环境空间的右逆下界。

反过来，对任意实际 $u\in K$，只要这条具体序列 $c_m$ 沿某子列在 Hilbert 范数中有界，那么 (4.3) 使 $J_mc_m$ 弱趋零。
由 (4.2)、(3.3)，该子列的 $n_m\in N$ 弱趋 $Ju$。
闭线性子空间 $N$ 也是弱闭的，遂有
$$
\boxed{\sup_{\ell}\|c_{m_\ell}\|<\infty\quad\Longrightarrow\quad Ju\in N.}
\tag{5.5}
$$
若对每个实际核向量均能证明这个有界子列条件，才可据此得到 $N=M$。

## 6. 具体剩余问题

顶部两层现在已经在代数和实际 Hilbert 运算层面准确消除，并接上真实正则提升。待证项不再是是否存在修复，而是对 §3 指定的、强趋固定实际核向量的低孔序列，能否选取或估计高尾修复使其有有界子列。

当前范数上界是 $B_{m,q}\|r_m\|$。虽然 $\|r_m\|\to0$，(3.6) 的增长仍不能被无速率的 Hilbert 尾吸收。不把这个缺口隐藏在“残差很小”、低坐标保持或进位误差已经支付的表述中。本稿没有构造非零缺陷，也没有证明 $N=M$。
