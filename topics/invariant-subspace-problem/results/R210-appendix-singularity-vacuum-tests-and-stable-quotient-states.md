# R210 附录：双重纯奇异性、真空投影测试与稳定商向量态

日期：2026-11-12（UTC）。状态：完整证明。
本稿给 R210 的固定正状态一个经证明的更强正常性界限；
不把“非正常”直接当成“纯奇异”。

## 1. 正常性与纯奇异性的具体含义

固定 UHF 的一个表示 $\pi:\mathfrak U\to B(H_\pi)$。
称正泛函 $\theta$ 属于该表示的正常类，如果存在正迹类算子
$\rho$，使
$$
\theta(E)=\operatorname{Tr}(\rho\,\pi(E)).
$$
本文称状态 $\varphi$ 对 $\pi$ 纯奇异，是指：
$$
0\le\theta\le\varphi,\quad
\theta\text{ 属于 }\pi\text{ 的正常类}
\quad\Longrightarrow\quad\theta=0.
\tag{1.1}
$$
该定义明确排除了任何受支配的非零正常正部分。

以下固定 R210 的一个模型 $S=S_N$ 或 $S_Y$，及其构造的状态 $\varphi$。
两模型的论证相同，不要求它们共享一个状态。

## 2. Haar 正常部分消失不需新估计

R210 的每个向量状态都来自
$$
g_r\in\ker\pi_-(S),\qquad \|g_r\|=1.
$$
因此它们不仅湮灭 $S\mathcal A$，还满足
$$
\varphi_r(S^*S)=\|\pi_-(S)g_r\|^2=0.
$$
由于 $S^*S\in\mathfrak U$ 是一个固定元素，弱*聚点保留
$$
\boxed{\varphi(S^*S)=0.}
\tag{2.1}
$$

若 $0\le\theta\le\varphi$ 且 $\theta$ 由原 Haar 表示中的正迹类
$\rho$ 表示，则
$$
0\le\operatorname{Tr}(\rho S^*S)
=\theta(S^*S)\le\varphi(S^*S)=0.
$$
即 $S\rho^{1/2}=0$。R122/R125 已证明两个模型的 $S$ 在原 Haar 空间上
单射，故 $\rho=0$。
因此
$$
\boxed{\varphi\text{ 对原 Haar 表示纯奇异。}}
\tag{2.2}
$$

这也给一个与选位构造无关的范围界限：

> 对任意在原 Haar 空间上单射的 $S\in\mathfrak U$，
> 任意表示中的精确 $\pi(S)$ 核向量状态的 UHF 弱*极限，
> 都不可能具有非零 Haar 正常正部分。

因此，仅改变 R185/R188 精确边界核向量的选取，
不能把这类状态极限变成待排的非零 Haar 正常湮灭见证。

## 3. 边界正常部分：使用整个四位块真空投影

沿 R210 记第 $s$ 次新增四位块为
$$
\mathcal B_{j_s}=\{j_s,j_s+1,j_s+2,j_s+3\},
$$
其局部无孔真空投影记为 $P_s\in\mathfrak U$。
在边界表示中，这些是四位均无孔的正交投影。
不同块互不相交，故所有 $P_s$ 两两交换。

R210 的局部单位向量为
$$
\psi_{j_s}=(\Omega+u_{j_s})/\sqrt2,
\qquad u_{j_s}\perp\Omega.
$$
所以局部真空概率准确为
$$
\langle P_s\psi_{j_s},\psi_{j_s}\rangle=\frac12.
\tag{3.1}
$$

使用 R210 原预算 $\delta_s=2^{-s-10}$。
当 $E$ 是任意作用在第 $s$ 步旧头上的收缩算子时，
旧头截断、单位化与最终修复给
$$
|\varphi_s(E)-\varphi_{s-1}(E)|\le6\delta_s.
\tag{3.2}
$$
这里无需真实 carry 估计：$E$ 本来就是有限头局部矩阵。
同时，追加张量的准确因子 $1/2$ 给
$$
\left|\varphi_s(EP_s)-\frac12\varphi_{s-1}(E)\right|
\le4\delta_s.
\tag{3.3}
$$
具体地，旧单位向量与正规化截断相差至多 $2\delta_s$，
状态差至多 $4\delta_s$；
乘 $1/2$ 后付 $2\delta_s$。
新向量与准确张量相差至多 $\delta_s$，
再付 $2\delta_s$，合成 (3.3)。

固定 $k$，对 $r\ge k$ 记
$$
Q_{k,r}=\prod_{s=k}^{r}P_s.
$$
递推 (3.3) 得
$$
\varphi_r(Q_{k,r})
\le2^{-(r-k+1)}
+4\sum_{s=k}^{r}2^{-(r-s)}\delta_s.
\tag{3.4}
$$
在以后的步骤中，$Q_{k,r}$ 是旧头收缩，
由 (3.2) 其期望总变化至多
$6\sum_{s>r}\delta_s=6\delta_r$。
因此 R210 的同一个状态聚点满足
$$
\boxed{
\varphi(Q_{k,r})
\le2^{-(r-k+1)}
+\bigl(4(r-k+1)+6\bigr)\delta_r
\longrightarrow0
}
\tag{3.5}
$$
对每个固定 $k$ 成立。

## 4. 从长块真空测试排除边界正常部分

设 $0\le\theta\le\varphi$，且 $\theta$ 属于 $\pi_-$ 的正常类。
在边界 Hilbert 空间中，
$$
\pi_-(Q_{k,r})\downarrow Q_k^-
\quad\text{SOT}\quad(r\to\infty),
$$
其中 $Q_k^-$ 投影到所有被选块 $\mathcal B_{j_s}$、
$s\ge k$ 均无孔的向量。
由正常性和 (3.5)，
$$
\theta(Q_k^-)
=\lim_{r\to\infty}\theta(Q_{k,r})=0.
\tag{4.1}
$$
这里左侧是该正常迹类表示在 $B(\mathscr H_-)$ 上的取值，
不声称 $Q_k^-$ 必属于 UHF。

每个边界基向量只有有限个孔。
因此当 $k\to\infty$ 时，
$$
Q_k^-\uparrow I\quad\text{SOT}.
$$
再用正常性，
$$
\theta(I)=\lim_k\theta(Q_k^-)=0.
$$
正泛函遂为零。所以
$$
\boxed{\varphi\text{ 对负整数边界表示也纯奇异。}}
\tag{4.2}
$$

整个论证使用有限局部投影上的明确不等式 (3.5)；
没有把向量状态列的弱*聚点自动当成奇异态。

## 5. 对当前 Haar 问题的含义

正泛函仅满足
$$
\omega(S\mathcal A)=0
$$
时，不能推出 $\omega(S^*S)=0$。
前者对应可能的非零不变子商，后者对应 GNS 中的实际核。

R210 的反例状态满足更强的后者，
所以 §2 在原 Haar 空间中自动排掉其正常部分。
尚待排除的 Haar 正常湮灭见证属于前一种问题；
本文没有将两个条件合并。

若将 $\varphi$ 正延拓到上述 Haar 或负整数边界两个表示中任一个的 $B(H_\pi)$，
其正常正部分限制到 UHF 后受 $\varphi$ 支配。
由 (2.2)、(4.2)，任何这样的正延拓都没有非零正常正部分。
这是一条经上述投影/核计算得到的结论，不是从非正常性单独推得。


## 6. Haar 长尾真空投影的直接计算

§2 已经排除 Haar 正常部分。
这里再把 R210 状态与原 Haar 正常性判据直接比较，不依赖抽象分解。

记 $H_s\in\mathfrak U$ 为第 $s$ 个新增四位块上的 Haar 真空投影，
即各位参考向量均为
$(e_{\rm no\ hole}+e_{\rm hole})/\sqrt2$。
四位真空在孔基下的全部16个系数均为 $1/4$。

沿 R210 §4，记 $r_\ell=a_{j_s+\ell}/a_{j_s}$，
$\ell=1,2,3$，以及 $q=\sum_{\ell=1}^3r_\ell^2$。
单孔向量 $u_{j_s}$ 的四个系数之和是
$$
d_s=\frac{q-\sum_{\ell=1}^3r_\ell}{\sqrt q\sqrt{q+1}}.
\tag{6.1}
$$
因 $0<r_\ell<1$，有 $d_s<0$。
R210 选取 $j_s\ge32$，故 $q>2$ 且
$\sum r_\ell<3$；因此 $q-\sum r_\ell>-1$，
分母大于 $\sqrt6$，从而 $-1<d_s<0$。

所以准确局部概率为
$$
\boxed{
h_s:=\langle H_s\psi_{j_s},\psi_{j_s}\rangle
=\frac{(1+d_s)^2}{32}\le\frac1{32},
\qquad h_s\longrightarrow\frac1{32}.
}
\tag{6.2}
$$
最后的极限由 $r_\ell\to1$、$q\to3$ 得出。
这不是把点态符号或真实算子当作张量代数同态；它只计算新块中的有限向量。

旧头收缩 $E$ 在追加该块时满足
$$
|\varphi_s(EH_s)-h_s\varphi_{s-1}(E)|\le4\delta_s.
$$
沿 §3 相同的递推，而使用 $h_s\le1/32$，得到
$$
\varphi\left(\prod_{s=k}^rH_s\right)
\le32^{-(r-k+1)}
+4\sum_{s=k}^r32^{-(r-s)}\delta_s+6\delta_r
\le32^{-(r-k+1)}+11\delta_r.
\tag{6.3}
$$
所以对每个固定 $k$，该期望在 $r\to\infty$ 时为零。

令 $P_{\Omega,j}$ 为单个位的 Haar 真空投影。
对任意固定 $m$，取第一个满足 $j_k\ge m$ 的被选块。
当 $R$ 足够大时，全尾有限投影
$\prod_{j=m}^RP_{\Omega,j}$ 被其内部所有完整被选块的真空投影乘积所支配。
各投影均为同一物理张量分解上的交换投影，故正序比较合法。
由 (6.3)，
$$
\boxed{
\lim_{R\to\infty}
\varphi\left(\prod_{j=m}^{R}P_{\Omega,j}\right)=0
\qquad\text{对每个固定 }m.
}
\tag{6.4}
$$

相反，原 Haar 表示中的非零正常正泛函 $\theta$ 满足
$$
\lim_{m\to\infty}\lim_{R\to\infty}
\theta\left(\prod_{j=m}^{R}P_{\Omega,j}\right)=\theta(I).
$$
因此 (6.4) 也直接验证本构造态的 Haar 纯奇异性。
同一投影支配论证适用于任何 $0\le\theta\le\varphi$，
并非仅排除 $\varphi$ 自己是正常态。

## 7. 稳定边界商上的同一个极限泛函

本节额外使用已经独立核验的
[快速头残差进入稳定像](../notes/2026-11-12-boundary-fast-head-residuals-enter-stable-range-and-quotient-norms-0c-agent.md)
之推论5.2；该稿 blob 为
`5a0eceabc25dbe7f3fd31c6581ce1e8b79e62b20`。
它证明 R185/R188 的标准修复构造类全部位于
$$
N=\overline{BM},\qquad M=\ker T,
$$
且 $e_0\in N$。
因而 R210 的每个 $g_s$ 都属于 $N$。

令
$$
c_s=\langle g_s,e_0\rangle.
$$
在第 $s$ 步，$v_s=P_{m_s}^-g_{s-1}$，
准确张量 $y_s$ 的真空系数是
$c_{s-1}/(\sqrt2\|v_s\|)$。
首步修复及所有后续标准修复都精确保留真空系数。
若未正规化的精确核极限记为 $G_s$，则
$$
\boxed{
c_s=\frac{c_{s-1}}{\sqrt2\,\|v_s\|\,\|G_s\|}.
}
\tag{7.1}
$$
R210 的预算给
$$
|\|v_s\|-1|\le\delta_s,\qquad
|\|G_s\|-1|\le\delta_s/2.
$$
因 $\sum_s\delta_s<\infty$，
两个分母偏离1的对数绝对和有限。
于是存在固定有限常数 $C$，使
$$
\boxed{|c_s|\le C\,2^{-s/2}.}
\tag{7.2}
$$

将稳定商
$$
Q=N/\mathbb Ce_0
$$
按 Hilbert 空间识别为 $N\cap e_0^\perp$。
对充分大的 $s$ 定义其中的单位向量
$$
z_s=\frac{g_s-c_se_0}{\sqrt{1-|c_s|^2}}.
$$
由 (7.2)，
$$
\|z_s-g_s\|\le2|c_s|\longrightarrow0.
\tag{7.3}
$$

$N$ 与 $\mathbb Ce_0$ 都对 $\pi_-(\mathcal A)$ 不变，
故有实际含幺收缩表示
$$
\rho_Q:\mathcal A\longrightarrow B(Q).
$$
对 $F\in\mathcal A$，
$$
\langle\rho_Q(F)z_s,z_s\rangle
=\langle\pi_-(F)z_s,z_s\rangle.
$$
由 (7.3)，它与 $\varphi_s(F)$ 的差趋于0。
所以沿 R210 已选的同一状态收敛子网或子序列，
$$
\boxed{
\langle\rho_Q(F)z_s,z_s\rangle
\longrightarrow\varphi(F)
\qquad(F\in\mathcal A).
}
\tag{7.4}
$$
也可在 $C^*(\rho_Q(A))$ 的状态空间取这些向量状态的弱*聚点，
得到实现同一 $\mathcal A$ 泛函的正状态。

本节只涉及 $\mathcal A$ 的商表示 $\rho_Q$。
$N$ 和 $\mathbb Ce_0$ 没有被证明对整个 UHF 代数不变；
因此没有定义或假设 $\mathfrak U\to B(Q)$ 的 $*$ 同态。
尤其 (7.4) 不把 §3 或 §6 的物理局部投影压缩误当成商中的乘法表示。

由于 $\mathsf N_j\to0$ SOT，$\rho_Q(N_j)\to0$ SOT。
而固定极限泛函仍满足
$\varphi(N_{j_k})\to\sqrt3/4$。
所以这种稳定商向量态极限也不能被当成该商表示中的正常泛函。
