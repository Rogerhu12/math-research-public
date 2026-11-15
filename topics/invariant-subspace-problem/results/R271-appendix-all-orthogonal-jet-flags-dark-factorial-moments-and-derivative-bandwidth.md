# 全部真正交 jet 旗的高阶暗对矩：导数带宽与同源联合预算

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro  
日期：2026-11-15

## 0. 原来源与本文的新增范围

沿用[实际固定测试全部暗对矩](R271-appendix-actual-fixed-test-all-dark-pair-factorial-moments-and-square-root-exponential-tail.md)的原连续尾、原有限 cut、同一个固定测试与同一个投影差：
$$
D_x=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad
u_f=(P_{V_Q}-P_{K_Q})f.
$$
$f$ 在所有远位 $i\ge x$ 上为真空。所有原 head、全部原旗和两个物理 cut 保留。

令
$$
\Pi_j=P_{\ker D_x^j},\quad \Pi_0=0,\qquad
F_j=\Pi_j-\Pi_{j-1}\quad(j\ge1).
\tag{0.1}
$$
在实际有限远孔直和上这是完整正交分解；将无效指标的 $F_j$ 置零。本文的 $F_j$ 一直是真正交 jet 差，绝不是顺次 MP 幂等投影。

选任意互不相交的相邻远位对。记 $N_{\rm phys}$ 为物理反对称投影之和，$N_{\rm prim}$ 为真实加权 primitive 一孔暗向量的正交投影之和，定义和原稿完全相同。统一写
$$
(N_\sigma,\sigma)=(N_{\rm phys},4)
\quad\text{或}\quad
(N_\sigma,\sigma)=(N_{\rm prim},5).
$$
对每个整数 $r\ge1$，本文证明
$$
\boxed{
\sum_{j\ge1}
\left\langle
\binom{N_\sigma}{r}F_ju_f,F_ju_f
\right\rangle
\le
16(r+1)^2(2r+1)r!
\left(\frac{\sigma^2}{x}\right)^r\|f\|^2.
}
\tag{0.2}
$$
这里已经求和全部真正交旗，右边没有 $h$、$Q$ 或旗层数。第一阶仍使用此前更锐的完整交换行界；本文新增全部高阶联合矩。

## 1. 实参数变形与当前旗的严格三带

只平衡任意有限所选对集 $S$，以
$$
H_i=n_{i+1}-n_i,\qquad
S(t)=\exp\left(\sum_{i\in S}t_iH_i\right)
$$
作原稿的真实权变形。各 $H_i$ 自伴、互相交换、范数至多 $1$，且
$$
D(t)S(t)=S(t)D(0).
$$
因此原 $V_Q(t),K_Q(t)$ 及每个 $\ker D(t)^j$ 都是对应原闭空间的 $S(t)$ 像。

以下所有正交旗都在同一当前参数点 $t$ 定义。由于
$$
[D(t),H_i]
$$
是原删除算子的一个有限线性组合，它与 $D(t)$ 交换，所以
$$
\operatorname{ad}_{D(t)}^2H_i=0.
$$
对 $z\in\ker D(t)^j$，
$$
D(t)^{j+1}H_i z
=H_iD(t)^{j+1}z
+(j+1)[D(t),H_i]D(t)^jz=0.
$$
故 $H_i\ker D(t)^j\subset\ker D(t)^{j+1}$。再用 $H_i$ 自伴，得到
$$
\boxed{
F_a(t)H_iF_b(t)=0\qquad(|a-b|>1).
}
\tag{1.1}
$$
这是当前真实旗的三带，不是固定等权旗的近似。

## 2. 混合导数的双侧旗支撑

任何一个上述移动闭空间的正交投影 $P(t)$ 满足
$$
\partial_iP=H_iP+PH_i-2PH_iP.
\tag{2.1}
$$
先前实参数归纳已给
$$
\|\partial_{i_1}\cdots\partial_{i_r}P(t)\|
\le4^r r!.
\tag{2.2}
$$

这里需保一个比范数更细的事实。保持 (2.1) 迭代所得的未化简非交换多项式：每个 $r$ 阶导数词中恰有 $r$ 个带相应标签的 $H_i$，并且至少有一个投影因子 $P$。因为每次微分只替换一个 $P$ 因子为 (2.1)，该事实直接归纳成立。

对 $F_j=\Pi_j-\Pi_{j-1}$，两项的导数是同一个多项式分别代入 $\Pi_j$ 与 $\Pi_{j-1}$。逐投影因子望远镜相减，每项至少插入一个
$$
\Pi_j-\Pi_{j-1}=F_j.
$$
其它投影因子仍是 $\Pi_j$ 或 $\Pi_{j-1}$，均对当前整条旗对角。由 (1.1)，一个 $H_i$ 最多改变一个旗指标；总共只有 $r$ 个。因此定义
$$
W_{j,r}=\sum_{|a-j|\le r}F_a(t)
$$
时，准确有
$$
\boxed{
\partial_SF_j
=W_{j,r}(\partial_SF_j)W_{j,r},
\qquad |S|=r.
}
\tag{2.3}
$$
$r=0$ 时也是同一陈述。这里同时控制输入、输出旗支撑，没有把 $\Pi_j$ 的全部低旗支撑误算作额外带宽。

同时，(2.2) 给
$$
\|\partial_SF_j\|\le2\cdot4^r r!.
\tag{2.4}
$$
于是对任意 $z$，
$$
\begin{aligned}
\sum_j\|(\partial_SF_j)z\|^2
&\le4\cdot16^r(r!)^2\sum_j\|W_{j,r}z\|^2\\
&\le4(2r+1)16^r(r!)^2\|z\|^2.
\end{aligned}
$$
最后一行仅因一个正交 $F_a$ 最多出现在 $2r+1$ 个 $W_{j,r}$ 中。故完整分析列满足
$$
\boxed{
\left\|z\longmapsto((\partial_SF_j)z)_j\right\|
\le2\sqrt{2r+1}\,4^r r!.
}
\tag{2.5}
$$
这一步正是避免逐 $j$ 累加一个未知高度因子的原因。

## 3. 将整条旗和实际投影同时微分

记
$$
\mathcal F(t)z=(F_j(t)z)_j.
$$
对 $E(t)=V_Q(t)$ 或 $K_Q(t)$，混合 Leibniz、(2.2)、(2.5) 给
$$
\begin{aligned}
\|\partial_S[\mathcal F(t)P_{E(t)}]\|
&\le\sum_{\ell=0}^r
\binom r\ell
\,2\sqrt{2\ell+1}\,4^\ell\ell!\,
4^{r-\ell}(r-\ell)!\\
&\le2(r+1)\sqrt{2r+1}\,4^r r!.
\end{aligned}
\tag{3.1}
$$
两原投影相减后，
$$
\boxed{
\|\partial_S[\mathcal F(t)u_f(t)]\|_{\ell^2_j(H)}
\le4(r+1)\sqrt{2r+1}\,4^r r!\,\|f\|.
}
\tag{3.2}
$$
这些导数只涉及有限参数组，全部空间与自然域都在原有限孔直和上；上界与该直和大小无关。

## 4. 暗面消失与联合高矩

若某个 $t_i=0$，原物理交换 $U_i$ 同时约化 $V_Q(t)$、$K_Q(t)$ 及所有 $\ker D(t)^j$。因此
$$
P_i^-F_j(t)u_f(t)=0
$$
对全部 $j$ 同时成立。

对物理暗投影乘积 $P_S^-=\prod_{i\in S}P_i^-$，在完整 $\ell^2_j(H)$ 列上用混合微积分基本定理与 (3.2)，得到
$$
\boxed{
\left(\sum_j\|P_S^-F_ju_f\|^2\right)^{1/2}
\le
4(r+1)\sqrt{2r+1}\,4^r r!
\prod_{i\in S}\theta_i\,\|f\|.
}
\tag{4.1}
$$

对真 primitive 暗投影，使用原稿的局部 $A_i^-(t_i)$：
$$
A_i^-(0)=P_i^-,
\qquad
\|(A_i^-)'(t_i)\|\le1.
$$
它们按对互不相交；一次混合导数中每个变量最多打到自己的局部投影一次。将 (3.2) 与这些局部导数做 Leibniz，
$$
\begin{aligned}
&\left\|
\partial_S\left[
\left(\prod_{i\in S}A_i^-(t_i)\right)
\mathcal F(t)u_f(t)\right]\right\|\\
&\quad\le
4(r+1)\sqrt{2r+1}\,r!
\sum_{\ell=0}^r\frac{4^{r-\ell}}{\ell!}\,\|f\|\\
&\quad\le
4(r+1)\sqrt{2r+1}\,5^r r!\,\|f\|.
\end{aligned}
$$
每一个 $t_i=0$ 面仍整列消失，故
$$
\boxed{
\left(\sum_j
\left\|\left(\prod_{i\in S}A_i^-\right)F_ju_f\right\|^2
\right)^{1/2}
\le
4(r+1)\sqrt{2r+1}\,5^r r!
\prod_{i\in S}\theta_i\,\|f\|.
}
\tag{4.2}
$$

将 (4.1) 或 (4.2) 平方，再对所有 $r$ 元对集求和。互不相交对的投影同时对角化，且
$$
\sum_{|S|=r}\prod_{i\in S}\theta_i^2
\le\frac1{r!}\left(\sum_i\theta_i^2\right)^r
\le\frac1{r!x^r}.
$$
有限族先得 (0.2)，无限不交族用非负 Tonelli 得相同结论。全部 $j$ 的正交分析列已经包含在 (4.1)--(4.2) 中，不再另付旗数。

## 5. 全旗高暗尾与同带混合读数

对整数 $k\ge1$、$1\le r\le k$，(0.2) 给
$$
\boxed{
\sum_j\|\mathbf1_{N_\sigma\ge k}F_ju_f\|^2
\le
16(r+1)^2(2r+1)
\frac{r!}{\binom kr}
\left(\frac{\sigma^2}{x}\right)^r\|f\|^2.
}
\tag{5.1}
$$
若
$$
k\ge\frac{x}{4\sigma^2},\qquad xk\ge16\sigma^2,
\qquad
r=\left\lfloor\frac{\sqrt{xk}}{2\sigma}\right\rfloor,
$$
同一 floor 估计给
$$
\boxed{
\sum_j\|\mathbf1_{N_\sigma\ge k}F_ju_f\|^2
\le
16(r+1)^2(2r+1)
\exp\left(-\frac{\log4}{4\sigma}\sqrt{xk}\right)\|f\|^2.
}
\tag{5.2}
$$

因此对任意真正同层读数族 $g_j$，若
$g_j=\mathbf1_{N_\sigma\ge k}g_j$，则
$$
\left|\sum_j\langle F_ju_f,g_j\rangle\right|
\le
\left(\sum_j\|\mathbf1_{N_\sigma\ge k}F_ju_f\|^2\right)^{1/2}
\left(\sum_j\|g_j\|^2\right)^{1/2}.
\tag{5.3}
$$
这里是全部正交 jet 一起的真预算，不需对每层重新取测试或重新平均。任何额外物理孔带投影都与暗计数及 $F_j$ 保持孔次数相容，可保同一右边应用。

## 6. 未替代的顺次返回

本文依靠的三带是 $H_i$ 在真正交旗上的三带；它不推出
$$
D_n^\dagger\cdots D_{n-j+1}^\dagger D^j
$$
等于 $F_j$ 的和，也不证明顺次 MP 保持暗计数。全旗高矩现在已经支付，但将其接到原
$\mathscr A_nu_{f,n}$ 时，仍须保留真实 MP 混合及全部端点 partial。

特别，(5.3) 只适用于已确实处于所述高暗谱空间的读数；不能把经过未付逆 Gram 或顺次提升的向量自动归入该空间。原低暗对方向及高返回共同预算继续。
