# 连续尾的大对称块配平、两个有界极限交织与完整 Schur 归约

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 对原尾 $b_j=(j+1)^{-2}$，可把相邻位分成长度随位置趋于无穷的块，并把每块权换成几何平均。取块长 $L(x)=\lfloor x^\alpha\rfloor$，其中 $0<\alpha<1/2$。在所有块都交换对称的真实物理扇区上，原模型与配平模型的完整核投影之差至多
$$
\epsilon_{m,\alpha}
=\sqrt{\exp(\eta_{m,\alpha})-1},
\qquad
\eta_{m,\alpha}
=\frac{2^{2-2\alpha}}{1-2\alpha}\,m^{2\alpha-1}.
$$
该界对原头、总孔窗口以及有限配平块数一致。无限尾结论通过两个有界极限交织证明；本文不假定整个无限对角相似有界。

配平后的对称扇区是真正的有限容量 spin 块张量空间。本文还保留全部原核 nuisance 的一个准确有界商及其最小 lift Gram，并给出原母提升的直接接口。它没有据此认定原普通右费或 $LGL$ 已获控制。

依赖：
[相邻两位的真投影与完整 Schur 比较](R271-appendix-adjacent-strong-weight-balancing-and-complete-symmetric-source-schur.md)。
§§1–4 的证明自足；这里只复用其中投影比较的两正交候选方法。

## 1. 单个任意长度块的真实正压缩

考虑连续块 $x,x+1,\ldots,x+L-1$，其中 $x\ge1$。这些是 $j+1$ 的索引，原删除权为
$$
b_i=(x+i)^{-2},\qquad 0\le i<L.
$$
取几何平均
$$
a=\left(\prod_{i=0}^{L-1}b_i\right)^{1/L},
\qquad
r_i=a/b_i,\qquad \prod_i r_i=1.
$$
在原 $0/1$ 占据空间上定义正对角算子
$$
S e_I=\left(\prod_{i\in I}r_i\right)e_I.
\tag{1.1}
$$
因为 $S^{-1}E_iS=r_iE_i$，
$$
S^{-1}\left(\sum_i b_iE_i\right)S
=a\sum_iE_i.
\tag{1.2}
$$
这不改变占据数。

令 $P$ 为该块全部置换的平均投影。在每个 $n$ 占据层，它的像由归一向量
$$
u_n=\binom Ln^{-1/2}\sum_{|I|=n}e_I
$$
张成。故对任意实数 $t$，精确有
$$
\langle u_n,S^t u_n\rangle
=\frac{e_n(r_0^t,\ldots,r_{L-1}^t)}{\binom Ln}
=:k_n(t).
\tag{1.3}
$$
这里保留了原正交物理度量。

写 $\xi_i=\log r_i$，则 $\sum_i\xi_i=0$，且其区间长度满足
$$
\Delta:=\max_i\xi_i-\min_i\xi_i
=2\log\frac{x+L-1}{x}
\le\frac{2(L-1)}x.
\tag{1.4}
$$

### 1.1 所需有限总体矩界的自足证明

先证明
$$
\frac{e_n(y_1,\ldots,y_L)}{\binom Ln}
\le\left(\frac1L\sum_i y_i\right)^n
\quad(y_i>0).
\tag{1.5}
$$
$n=0,1$ 直接成立。$n\ge2$ 时，固定其余变量及 $y_i+y_j$，有
$$
e_n=y_iy_j\,e_{n-2}(\text{其余})
 +(y_i+y_j)e_{n-1}(\text{其余})
 +e_n(\text{其余}).
$$
把 $y_i,y_j$ 换成其平均值不会减小 $e_n$。反复平均最大与最小变量，其和固定而平方差总量下降，极限为全体相等。连续性给 (1.5)。

对在 $\xi_0,\ldots,\xi_{L-1}$ 上均匀取值的实变量 $X$，令
$$
\phi(t)=\log\left(\frac1L\sum_i e^{t\xi_i}\right).
$$
$\phi(0)=\phi'(0)=0$，且 $\phi''(t)$ 是指数倾斜分布下的方差。任何取值于长度 $\Delta$ 区间的变量均有方差至多 $\Delta^2/4$：若区间为 $[\ell,u]$，由
$$
\mathbb E[(X-\ell)(u-X)]\ge0
$$
得 $\operatorname{Var}X\le(\mathbb EX-\ell)(u-\mathbb EX)\le\Delta^2/4$。两次积分于是给
$$
\phi(t)\le t^2\Delta^2/8
\quad(t\in\mathbb R).
\tag{1.6}
$$
将 (1.5) 用于 $y_i=e^{t\xi_i}$，有 $\log k_n(t)\le n\phi(t)$。又因 $\prod_i r_i=1$，补集公式给
$$
k_n(t)=k_{L-n}(-t).
$$
因此
$$
\log k_n(t)
\le\frac{\min(n,L-n)t^2\Delta^2}{8}
\le\frac{Lt^2\Delta^2}{16}.
\tag{1.7}
$$
另一方面，把全部 $n$ 元子集的正数 $\prod_{i\in I}r_i^t$ 作算术—几何平均，几何平均为一，故
$$
k_n(t)\ge1.
\tag{1.8}
$$

取 $t=\pm1,\pm2$，(1.4)、(1.7)、(1.8) 给
$$
\boxed{
PS^{\pm1}P\succeq P,\qquad
PS^{\pm2}P\preceq e^{\eta(x,L)}P,
\quad
\eta(x,L)=\frac{L(L-1)^2}{x^2}.
}
\tag{1.9}
$$
特别
$$
\|(S^{\pm1}-I)P\|
\le\sqrt{e^{\eta(x,L)}-1}.
\tag{1.10}
$$
没有把非对称占据层删去；(1.9) 只是完整正算子的精确压缩。

## 2. 遍历整个原尾且块长趋于无穷

固定 $m\ge1$ 和 $0<\alpha<1/2$。从
$$
x_1=m+1,\qquad
L_\nu=\lfloor x_\nu^\alpha\rfloor,\qquad
x_{\nu+1}=x_\nu+L_\nu
\tag{2.1}
$$
开始划分全部尾位。$L_\nu\ge1$，并随 $\nu$ 趋于无穷。每块使用 §1 的几何平均权 $a_\nu$。

设
$$
\eta_m=\sum_{\nu\ge1}\eta(x_\nu,L_\nu).
$$
因为 $L_\nu\le x_\nu^\alpha\le x_\nu$，令 $p=2\alpha-2<-1$，有
$$
\eta(x_\nu,L_\nu)
\le L_\nu x_\nu^{2\alpha-2}
\le2^{2-2\alpha}
       \sum_{i=x_\nu}^{x_\nu+L_\nu-1}i^{2\alpha-2}.
$$
第二步使用块内 $i\le2x_\nu$ 及指数为负。各块不重叠，故
$$
\boxed{
\eta_m\le
2^{2-2\alpha}\sum_{i\ge m+1}i^{2\alpha-2}
\le\frac{2^{2-2\alpha}}{1-2\alpha}\,m^{2\alpha-1}
=\eta_{m,\alpha}.
}
\tag{2.2}
$$
记 $K_m=e^{\eta_m}$。固定 $\alpha$ 后 $K_m\to1$。

例如 $\alpha=1/4$ 时，
$$
\eta_m\le4\sqrt2\,m^{-1/2},
\qquad
\epsilon_m:=\sqrt{K_m-1}=O(m^{-1/4}).
\tag{2.3}
$$
这里的块长是位置的四次方根，并无孔数或出生限制。

只配平前 $J$ 个完整块，令其正相似为 $S_J$，所有这些块的交换对称投影为 $P_J$。由张量积与 (1.9)，
$$
P_J S_J^{\pm1}P_J\succeq P_J,\qquad
P_J S_J^{\pm2}P_J\preceq e^{\eta_{m,J}}P_J,
\quad
\eta_{m,J}=\sum_{\nu\le J}\eta(x_\nu,L_\nu).
\tag{2.4}
$$
因此相邻配平稿的完整有限 Schur、最小回返与投影结论逐字适用，统一常数不超过 $K_m$。最后一个有限强块也可以在块末截短；(2.2) 仍成立。

## 3. 无限尾不用无界相似：两个有界极限映射

令
$$
P=\operatorname*{s-lim}_{J\to\infty}P_J
$$
为全部块都交换对称的正交投影。它非零，包含原头张量尾真空。下面所有 $S_J^{\pm1}$ 只作为从 $\operatorname{Ran}P$ 到原物理空间的映射使用。

从 (2.4) 得
$$
\|S_J^{\pm1}P\|\le\sqrt{K_m}.
\tag{3.1}
$$
若 $J'>J$，写 $S_{J'}=S_J S_{(J,J']}$。后一个因子只作用后面的块，所以
$(S_{(J,J']}^{\pm1}-I)P$ 的像仍属于前 $J$ 块的对称扇区。于是
$$
\|(S_{J'}^{\pm1}-S_J^{\pm1})P\|
\le\sqrt{K_m}
 \sqrt{\exp\!\left(\sum_{\nu>J}\eta(x_\nu,L_\nu)\right)-1}.
\tag{3.2}
$$
右端趋零。因此在算子范数下存在
$$
V_+=\lim_J S_J|_{\operatorname{Ran}P},
\qquad
V_-=\lim_J S_J^{-1}|_{\operatorname{Ran}P}.
\tag{3.3}
$$
以 $\iota:\operatorname{Ran}P\to\mathscr H$ 表示原等距包含，则
$$
\boxed{
\|V_\pm\|\le\sqrt{K_m},\qquad
\|V_\pm-\iota\|\le\epsilon_m,\qquad
V_-^*V_+=V_+^*V_-=I_{\operatorname{Ran}P}.
}
\tag{3.4}
$$
最后一个身份由有限 $J$ 的
$(S_J^{-1}P)^*(S_JP)=P$ 取极限得到。

本文不定义整个 $\mathscr H$ 上的有界 $S_\infty$。有限 $S_J$ 的完整条件数可能无界；(3.3) 只在受保护的对称输入扇区上成立。

## 4. 两个真实交织，正向可行列与反向正交条件都保留

令 $A$ 为原有限头上的任意有界算子，原尾为 $D$，全部块配平后的尾为 $\widetilde D$，置
$$
L=A+D,\qquad \widetilde L=A+\widetilde D.
$$
$\widetilde D$ 的权为各 $a_\nu$，仍正且属于 $\ell^1$；$P$ 约化 $\widetilde D$ 和 $\widetilde L$。

以 $D_J$ 表示仅前 $J$ 块配平的尾，$L_J=A+D_J$。精确有
$$
L S_J=S_J L_J.
\tag{4.1}
$$
$D_J-\widetilde D$ 只作用第 $J$ 块以后的位，并且
$$
\|D_J-\widetilde D\|\longrightarrow0.
\tag{4.2}
$$
例如原权和配平权在同一块都位于该块两端权之间，故剩余差的 $\ell^1$ 和由相应两尾的 $\ell^1$ 和控制。

对 $f\in\operatorname{Ran}P$，$(D_J-\widetilde D)f$ 仍在前 $J$ 块的对称扇区。由 (3.1)，
$$
\|L S_Jf-S_J\widetilde Lf\|
\le\sqrt{K_m}\,\|D_J-\widetilde D\|\,\|f\|.
$$
取极限得
$$
\boxed{L V_+=V_+\widetilde L|_{\operatorname{Ran}P}.}
\tag{4.3}
$$

反向令 $J_J=P S_J^{-1}$。其伴随在算子范数下收敛到 $V_-$，所以 $J_J$ 在算子范数下收敛到 $V_-^*$。利用 $P\widetilde L=\widetilde LP$，
$$
J_JL-\widetilde L J_J
=P(D_J-\widetilde D)S_J^{-1}.
$$
此误差的伴随为
$$
S_J^{-1}(D_J^*-\widetilde D^*)P.
$$
差算子仍只作用后续块，所以其像保持前 $J$ 块的对称性；(3.1) 给同一个趋零界。因此
$$
\boxed{V_-^*L
=\widetilde L|_{\operatorname{Ran}P}\,V_-^*.}
\tag{4.4}
$$
同样的证明分别给 $D V_+=V_+\widetilde D$ 和
$V_-^*D=\widetilde D V_-^*$。

$S_J$ 与总孔投影及所有物理头投影对易，故 $V_\pm,V_\pm^*$ 也保留这些截断。若另用远尾孔数，强/远边界取在一个块端点时，同一结论成立。

## 5. 完整核投影与所有原截断的比较

先取
$$
\mathscr K=\ker L,\qquad
\widetilde{\mathscr K}_0=\ker\widetilde L\cap\operatorname{Ran}P.
$$
(4.3)、(4.4) 分别给
$$
V_+\widetilde{\mathscr K}_0\subseteq\mathscr K,
\qquad
V_-^*\mathscr K\subseteq\widetilde{\mathscr K}_0.
\tag{5.1}
$$
对 $f\in\operatorname{Ran}P$，写
$f=f_0+f_1$，其中 $f_0=P_{\widetilde{\mathscr K}_0}f$、
$f_1\perp\widetilde{\mathscr K}_0$。则 $V_+f_0$ 是原核中的真实可行列。
同时对任意 $k\in\mathscr K$，
$$
\langle V_-f_1,k\rangle
=\langle f_1,V_-^*k\rangle=0,
$$
所以 $V_-f_1$ 属于原核的真正正交补。

利用 (3.4)，原核投影误差的两项分别在 $\mathscr K^\perp$ 和 $\mathscr K$ 中正交，得到
$$
\boxed{
\|(P_{\mathscr K}-P_{\widetilde{\mathscr K}_0})P\|
\le\epsilon_m\le\epsilon_{m,\alpha}.
}
\tag{5.2}
$$
这是完整原核的结论，不是仅对 $V_+\widetilde{\mathscr K}_0$ 这一已知子空间的投影比较。

由于交织及截断同时保持，完全相同的证明适用于：

- 总孔 $\le Q$ 的真核及 $P_{<Q}Lv=0$ 的原左空间；
- 强/远边界位于块端点时，远孔 $\le n$ 的真核及 far-left 低行空间；
- 由真实 $D$ 幂核、物理孔截断构成的高出生空间；
- 已知闭的原 joined 物理空间及其相应配平空间。

在最后两项中，使用两方向交织映射实际幂核、保持孔支撑并映射闭和；不交换压缩与取逆，也不将原正交裸商当作原来的非正交相似坐标。

两嵌套投影之差，例如原最小 top 算子 $P_{V_Q}-P_{K_Q}$，在 $\operatorname{Ran}P$ 上的比较界为 $2\epsilon_m$。

对一般固定物理 $f$，每个单投影的误差至多
$$
\epsilon_m\|Pf\|+\|(I-P)f\|.
\tag{5.3}
$$
当 $m\to\infty$ 时，$\|(I-P)f\|\to0$，因为 $P$ 恒等作用于第 $m$ 位之后的真空扇区，而有限物理位向量稠密。故 (5.2)–(5.3) 给所有上述移动窗口中的固定测试强比较。

## 6. 无限模型仍保全部 nuisance 的准确商

限制
$$
J_0=V_-^*|_{\mathscr K}:
 \mathscr K\longrightarrow\widetilde{\mathscr K}_0.
$$
由 (3.4)、(5.1)，$J_0$ 满射，且 $V_+|_{\widetilde{\mathscr K}_0}$ 是其有界右逆。因此
$$
\boxed{
K_m^{-1}\|x\|^2
\le
\min_{\substack{v\in\mathscr K\\J_0v=x}}\|v\|^2
\le K_m\|x\|^2
\quad(x\in\widetilde{\mathscr K}_0).
}
\tag{6.1}
$$
下界由 $\|J_0\|\le\sqrt{K_m}$，上界取真实候选 $V_+x$。这是将整个 $\ker J_0$ 消去的完整 Schur 费用，而不是只消某些有限反对称来源。

若 $v_{\min}$ 是该源的真最小 lift，则
$V_+x-v_{\min}\in\ker J_0$ 且与 $v_{\min}$ 正交，从而
$$
\boxed{
\|V_+x-v_{\min}\|^2
\le(K_m-K_m^{-1})\|x\|^2.
}
\tag{6.2}
$$
这里明确使用新商映射 $J_0$；它没有被擅自认成原切口源 $r_q$。对有限块，(6.1)–(6.2) 与先前实际 $S_J^2$ 的全部非对称 Schur 公式一致。

若 $f$ 在头张量全部尾真空中，所有 $S_J^{\pm1}f=f$，故 $V_\pm f=f$。对该类原测试还得到相对的二次型比较
$$
K_m^{-1}\|P_{\widetilde{\mathscr K}_0}f\|^2
\le\|P_{\mathscr K}f\|^2
\le K_m\|P_{\widetilde{\mathscr K}_0}f\|^2.
\tag{6.3}
$$
这由 (6.1) 的同一源对偶范数直接给出，也可分别用 $V_+$ 和 $J_0$ 的范数上界证明。

## 7. 与同一个原母提升及 top 的接合

本节只代入此前已付的母提升量词，不扩大其窗口。假设在某个已证明合法的 $Q$ 上，有原物理映射
$$
\Lambda_{m,Q}:K_{m,Q}\longrightarrow N,\qquad
\|\Lambda_{m,Q}k-k\|\le\delta_{m,Q}\|k\|.
\tag{7.1}
$$
则对配平对称有限孔核
$$
\widetilde K_{m,Q,0}
=\ker\widetilde L_m\cap\mathcal H_{\le Q}\cap\operatorname{Ran}P
$$
使用同一个候选 $\Lambda_{m,Q}V_+x$，有
$$
\boxed{
\operatorname{dist}(x,N)
\le(\epsilon_m+\delta_{m,Q}\sqrt{K_m})\|x\|.
}
\tag{7.2}
$$
原因是 $V_+x$ 仍在原总孔 $\le Q$ 的真核，故 (7.1) 确实适用；全部实际 carry 与原孔支撑都保留。

特别，对同一个 $w\in N^\perp$，
$$
\|P_{\widetilde K_{m,Q,0}}Pw\|
\le(\epsilon_m+\delta_{m,Q}\sqrt{K_m})\|w\|.
\tag{7.3}
$$
若另有原左投影 $v_Q=P_{V_{m,Q}}w$ 接近 $w$，令
$$
\widetilde u_Q=
\left(P_{\widetilde V_{m,Q}\cap\operatorname{Ran}P}
      -P_{\widetilde K_{m,Q,0}}\right)Pw.
$$
则 (5.2)、(5.3)、(7.3) 给
$$
\boxed{
\|\widetilde u_Q-w\|
\le\|v_Q-w\|
 +2\epsilon_m\|w\|
 +\|(I-P)w\|
 +\delta_{m,Q}\sqrt{K_m}\|w\|.
}
\tag{7.4}
$$
这是配平模型中由明确测试 $Pw$ 产生的真实最小 top。它并没有被称为原源 $r_p$，但可在新模型内重新使用完整几何源流。式中只有原物理范数和收缩投影，没有把误差乘普通右逆或巨大头相似。

## 8. 准确的 spin 块及尚未匹配的预算

在第 $\nu$ 块的对称基 $u_n$ 中，
$$
\widetilde D_\nu u_n
=a_\nu\sqrt{n(L_\nu-n+1)}\,u_{n-1},
\qquad 0\le n\le L_\nu.
\tag{8.1}
$$
因此 $\operatorname{Ran}P$ 是这些真实自旋 $L_\nu/2$ 模块的张量空间。块长趋于无穷，但每个块仍保完整有限容量，不以无碰撞 boson 替换 (8.1)。

已有主池／balanced-star 相位定理不能仅凭 (8.1) 自动调用：这些块一般不满足某一主池长度等于其余总长的条件，原 $A_m$ 也仍包含非齐次 carry，而非免费变成一个物理等权 spin。若要使用那些结果，仍须逐模块识别实际源、相应主池及完整回返 Schur。

本稿已支付原固定测试的大对称块归约、全部非对称来源的准确商及母提升接口。普通右费、原非交换 $LGL$ 和最终 $N=M$ 的剩余预算仍须在同一实际源上证明；一般 Hilbert 空间不变子空间问题没有在这里完成。
