# R271 附录：同一左最小源的逐幂远孔观测损耗与零源反馈

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。本稿在 [首段精确 Stein 与圆盘演算](R271-appendix-first-row-observability-loss-exact-source-contraction-and-disk-calculus.md) 中保留左最小者的实际远孔支撑。对同一个源 $r$ 和 $v=Ur$，证明
$$
\delta^{-2k}\|C_{\rm s}^k r\|_{L+B}^{\,2}
\le\|P_{\mathcal N_>\ge k}v\|^2+\alpha(r)^2
\quad(0\le k\le h).
$$
完整普通右费有相同式，以 $G^{-1}$ 和 $\lambda$ 替换 $B$ 和 $\alpha$。第一式右端是真正左最小向量的物理远孔尾与已经付清的裸费，不是环境向量尾，也不需要乘头条件数。证明还保留 $P_{\mathscr K}C^kUr$ 的全部左零源反馈。

没有从 $C_{\rm s}^kr$ 小反推出 $r$ 小；真实负图上的小奇异方向仍须另付。

## 1. 固定源、孔层和已付右损耗

固定强尾并头稿中的同一个 $m,R,n$，写
$$
C=A_m+D_<,\quad C^h=0,\quad D=D_>,\quad
\delta=\|D\|>0,\quad C_{\rm s}=C|_{\mathscr R_n^C}.
$$
记真实左最小者及其零源核为
$$
U=(E_n^C)^\dagger,\quad L=U^*U,\quad
\mathscr K=\ker E_n^C,\quad v=Ur.
$$
因此 $v$ 的远孔支撑在 $0,\ldots,n$。$\iota_n$ 将源 $r$ 等距注入第 $n$ 个远孔层。左方程准确为
$$
Cv=-Dv+\iota_n r.
\tag{1.1}
$$
所有出现的 $D^j$ 均为同一物理尾删除算子，在当前有限多个固定孔层上作用；不引入一个全孔有界的 $D^\dagger$。

令 $B$、$H=G^{-1}$ 分别为同一个源的完整裸费用与完整普通右费用，
$$
\alpha(r)^2=\langle Br,r\rangle,\qquad
\lambda(r)^2=\langle Hr,r\rangle.
$$
已付首段损耗是
$$
C_{\rm s}^*BC_{\rm s}+I\le\delta^2B,\qquad
C_{\rm s}^*HC_{\rm s}+I\le\delta^2H.
\tag{1.2}
$$
令 $K=B$ 或 $H$，并写 $\gamma_K(r)^2=\langle Kr,r\rangle$。逐次应用 (1.2) 给
$$
\boxed{
\gamma_K(C_{\rm s}^kr)^2
\le\delta^{2k}\gamma_K(r)^2
-\sum_{j=0}^{k-1}
 \delta^{2j}\|C_{\rm s}^{k-1-j}r\|^2.
}
\tag{1.3}
$$
$k=0$ 时求和为空。这里所有幂仍在第 $n$ 个同一个完整源上，不是在另一切口重选来源。

## 2. 左方程的准确逐幂展开

因为头上的 $C$ 与尾上的 $D$ 交换，而且
$C\iota_n r=\iota_n C_{\rm s}r$，(1.1) 归纳给
$$
\boxed{
C^k v=(-D)^k v+
\sum_{j=0}^{k-1}(-D)^j\iota_n C_{\rm s}^{k-1-j}r.
}
\tag{2.1}
$$
这只使用同一左前缀及其源，不读取任何新的未来行。

(2.1) 的第一项支撑在远孔 $\le n-k$。第 $j$ 个边界项若非零，支撑恰在远孔 $n-j$。对 $0\le j<k$，这些孔层互不相同，而且都高于 $n-k$。若 $j>n$，对应项由孔数直接为零；若 $k>n$，第一项同样为零。因此所有 $k$ 的支撑边界均有准确解释，物理正交给
$$
\boxed{
\|C^kv\|^2
=\|D^kv\|^2+
\sum_{j=0}^{k-1}\|D^j C_{\rm s}^{k-1-j}r\|^2.
}
\tag{2.2}
$$
式中最后的 $D^j$ 直接作用源所在的第 $n$ 层，与带 $\iota_n$ 的范数相同。

$C^kv$ 是同一左空间内源 $C_{\rm s}^kr$ 的可行代表，故真正左最小化为
$$
UC_{\rm s}^kr=(I-P_{\mathscr K})C^kv.
$$
于是
$$
\boxed{
\mu(C_{\rm s}^kr)^2+\|P_{\mathscr K}C^kv\|^2
=\|D^kv\|^2+
\sum_{j=0}^{k-1}\|D^j C_{\rm s}^{k-1-j}r\|^2.
}
\tag{2.3}
$$
这保留了反向头作用产生的全部左零源反馈，而不是把 $C^kv$ 当作最小者。

## 3. 同源观测和的抵消及物理远孔尾

将 (1.3) 与 (2.3) 相加，得到
$$
\begin{aligned}
&\|C_{\rm s}^kr\|_{L+K}^{\,2}
+\|P_{\mathscr K}C^kv\|^2\\
&\quad+
\sum_{j=0}^{k-1}
\left[
 \delta^{2j}\|C_{\rm s}^{k-1-j}r\|^2
 -\|D^j C_{\rm s}^{k-1-j}r\|^2
\right]\\
&\hspace{3em}\le
\|D^kv\|^2+\delta^{2k}\gamma_K(r)^2.
\end{aligned}
\tag{3.1}
$$
每个方括号都非负。由于 $D^k$ 杀掉远孔数 $<k$ 的全部物理向量，
$$
\|D^kv\|^2
\le\delta^{2k}\|P_{\mathcal N_>\ge k}v\|^2.
$$
因此得到两种完整源度量的精确统一界
$$
\boxed{
\delta^{-2k}\|C_{\rm s}^kr\|_{L+B}^{\,2}
+\delta^{-2k}\|P_{\mathscr K}C^kUr\|^2
\le
\|P_{\mathcal N_>\ge k}Ur\|^2+\alpha(r)^2,
}
\tag{3.2}
$$
$$
\boxed{
\delta^{-2k}\|C_{\rm s}^kr\|_{L+H}^{\,2}
+\delta^{-2k}\|P_{\mathscr K}C^kUr\|^2
\le
\|P_{\mathcal N_>\ge k}Ur\|^2+\lambda(r)^2.
}
\tag{3.3}
$$
它们对 $0\le k\le h$ 成立。$k=0$ 恰回到定义，因 $Ur\perp\mathscr K$；$k=h$ 时 $C^h=C_{\rm s}^h=0$，左边为零，不能将这一端点误读为新的逆估计。$k>h$ 的源幂也为零。

特别，$k=1$ 给
$$
\boxed{
\delta^{-2}
\left(\|C_{\rm s}r\|_{L+B}^{\,2}
+\|P_{\mathscr K}CUr\|^2\right)
\le\|P_{\mathcal N_>\ge1}Ur\|^2+\alpha(r)^2.
}
\tag{3.4}
$$
所以真正左向量的全部远尾真空能量从右边准确消失。这里被支付的是新联块头 $C$ 的实际零源反馈；不将它改称旧 $A_m$ 或旧 $G_{1,m}$ 的反馈。

## 4. 原同一顶部来源上的代入

现在取 [强位并头源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md) 的同一个
$$
u=u_Q,\qquad r_n^C=Cu_n,\qquad
U_n^Cr_n^C=P_{\mathcal N_>\le n}u,
\qquad n+h+R<Q.
$$
因此 (3.2) 的右边严格是
$$
\|P_{k\le\mathcal N_>\le n}u\|^2+\alpha_n^C(r_n^C)^2.
\tag{4.1}
$$
它没有换成一个构造性左候选或另一个 $u_Q$。原真实投影误差
$\|u-P_{\mathcal N\le Q}w\|\le2\eta_m\|w\|$
和两个孔计数的关系给
$$
\|P_{k\le\mathcal N_>\le n}u\|
\le\|P_{\mathcal N_>\ge k}w\|+2\eta_m\|w\|.
\tag{4.2}
$$
因为当前远孔低区的总孔支撑不超过 $n+R<Q$，(4.2) 没有引入 $Q$ 外部截断乘大常数。

于是对 $1\le k\le h$，
$$
\boxed{
\delta^{-2k}\|C_{\rm s}^k r_n^C\|_{L+B}^{\,2}
\le
\bigl(\|P_{\mathcal N_>\ge k}w\|
      +2\eta_m\|w\|\bigr)^2
+\alpha_n^C(r_n^C)^2.
}
\tag{4.3}
$$
源幂的全部左零核投影还可按 (3.2) 同时放在左边。已付 $\alpha_n^C(r_n^C)^2\le\|Y_n\|^2$ 及其同窗总和继续使用同一个未来。

固定 $w$ 时，第 $m+R$ 位以后有至少一个物理孔的投影强趋零；因此 (4.3) 的远孔项对每个 $k\ge1$ 都由同一个无权物理尾控制。本文不为它声称任何未付的速率，也不将 (3.3) 中仍未付的普通 $\lambda$ 换成裸 $\alpha$。

## 5. 对同源解析函数的直接后果及未付范围

若 $p(z)=\sum_{k=0}^{h-1}p_kz^k$，(3.2) 给保真实来源的估计
$$
\boxed{
\|(p(C_{\rm s})-p_0I)r\|_{L+B}
\le
\sum_{k=1}^{h-1}|p_k|\delta^k
 \left(\|P_{\mathcal N_>\ge k}Ur\|^2+\alpha(r)^2\right)^{1/2}.
}
\tag{5.1}
$$
它与前稿的全源圆盘演算不同：右边保每个幂实际读取的左远孔尾。对原同一顶部，直接代 (4.1) 或 (4.2)，不另选源。带完整普通费用的版本由 (3.3) 同样成立。

这些式子并未给 $C_{\rm s}$ 在真实负图上的小奇异值下界。即使 $r$ 属于
$(\ker C_{\rm s})^{\perp_{L+B}}$，也不能由 $C_{\rm s}r$ 很小反推 $r$ 很小，不能把 $C_{\rm s}$ 或其伴随表示反向除掉。下一步仍须把同一个固定物理测试或完整返回提升接到这些已付远孔损耗；原 $\mu^2\le\kappa_m\Xi^2$、普通右费与 $N=M$ 尚未证明。
