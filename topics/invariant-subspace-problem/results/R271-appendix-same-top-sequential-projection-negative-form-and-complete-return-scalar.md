# R271 附录：同一实际顶部的顺次投影负二次型与完整返回标量

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。对原同一个 $w\in W$ 产生的真实顶部 $u_Q$，本稿构造一个完整、同源、保全部头旗与尾旗的顺次右链。与同一个 $u_Q$ 配对后，左能量准确等于顺次尾投影的负二次型之和；因此在这个指定标量里不必分别估计完整返回投影或最小逆。跨 cut 的和也保持同一物理顶部。

顺次投影的幂等性、嵌套性、同一短核上的范数与真幂 Schur 比较均已由 [R239 顺次 jet 稿](R239-appendix-sequential-jet-number-and-true-power-schur-comparison.md) 证明。本稿不重复登记这些结构。新增是其与原实际顶部、完整右链正交性及同源左能量的准确接合。没有证明这些负二次型在原移动窗口具有足够上界，普通 ISP 与原 $N=M$ 仍开放。

依赖：

- [强物理尾位并头后的同一顶部源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)。
- [完整返回的物理正交分解](R271-appendix-complete-return-orthogonal-decomposition-driven-system-and-unique-lift.md)。
- [顺次 jet 次数与真幂 Schur 比较](R239-appendix-sequential-jet-number-and-true-power-schur-comparison.md)。

## 1. 完全不换来源的固定环境

沿用强位并头稿，固定原 $N/Y$ 模型、$m,R,Q,w$，写
$$
C=A_m+D_<,\qquad h=2^m+R,\qquad C^h=0,\qquad D=D_>.
$$
取原同一个真正最小顶部
$$
u=u_Q=P_{V_{m,Q}}w-P_{K_{m,Q}}w,\qquad u\perp K_{m,Q}.
\tag{1.1}
$$
以 $u_n$ 表示其远孔数为 $n$ 的物理分量。原低输出及原头幂零性已经给
$$
C u_n+D u_{n+1}=0\quad(n<Q-R),
\qquad
D^h u_n=0\quad(n\le Q-R).
\tag{1.2}
$$
对
$$
p\ge0,\qquad p+h+R<Q
\tag{1.3}
$$
的每个 cut，仍取原联块源
$$
r_p=C u_p=-D u_{p+1}.
\tag{1.4}
$$
其真实左最小者与能量是
$$
U_pr_p=P_{\mathrm{far}\le p}u,\qquad
\mu_p^2:=\mu_p(r_p)^2
=\|P_{\mathrm{far}\le p}u\|^2.
\tag{1.5}
$$
本稿不把不同 $p$ 的这些来源改成独立可选向量，也不将 $C$ 换成原更大头 $A_{m+R}$。

## 2. 有限真实层上的顺次尾逆与投影

令
$$
D_n=D|_{\mathcal H_n^>}:\mathcal H_n^>\longrightarrow\mathcal H_{n-1}^>,
\qquad Q_n=D_n^\dagger.
$$
原连续尾在每个固定有限孔层满射，故 $Q_n$ 是该完整层上的有界算子且 $D_nQ_n=I$。所有算子在有限头上张量单位。全文只用固定的有限层集合，不宣称全孔直和上的 $D^\dagger$ 有界。

对 $0\le j\le n$ 记
$$
\widehat Q_{n,j}=Q_nQ_{n-1}\cdots Q_{n-j+1},\qquad
P_{n,j}=\widehat Q_{n,j}D^j|_{\mathcal H_n^>},
\qquad P_{n,0}=I.
\tag{2.1}
$$
这里右侧先作用。因 $D^j\widehat Q_{n,j}=I$，
$$
P_{n,j}^2=P_{n,j},\qquad
\ker P_{n,j}=\ker D^j\cap\mathcal H_n^>.
\tag{2.2}
$$
令 $E_{h,n}=\ker D^h\cap\mathcal H_n^>$。当 $j\le h$ 时，$P_{n,j}$ 保持这个完整短核：对 $v\in E_{h,n}$，
$$
D^hP_{n,j}v=D^{h-j}D^jv=0.
\tag{2.3}
$$
以下只在 $n=p+j\ge j$ 使用这些式子，所以没有负孔层。$P_{n,h}|_{E_{h,n}}=0$。最初的一步是真正物理正交投影，
$$
P_{n,1}=D_n^\dagger D_n=I-P_{\ker D_n}.
\tag{2.4}
$$
但 $j\ge2$ 的顺次投影一般不是正交投影，不得将 $\widehat Q_{n,j}$ 改成 $(D^j)^\dagger$。

既有顺次 jet 稿已经证明，在同一 $E_{h,n}$ 内
$$
P_{n,j}P_{n,k}=P_{n,\max(j,k)}.
\tag{2.5}
$$
特别 $P_{n,j}=P_{n,1}P_{n,j}P_{n,1}$ 对 $j\ge1$ 成立。顺次投影的负二次型只读取真正非primitive 分量；这仍不提供其大小。

## 3. 一个合法的完整同源右链

对 (1.3) 的同一 $r_p$ 定义
$$
c^{\rm seq}_{p,j}
=\widehat Q_{p+j,j}(-C)^{j-1}r_p,
\qquad 1\le j\le h.
\tag{3.1}
$$
由 (1.2)，
$$
D^j u_{p+j}=(-C)^j u_p,
$$
所以
$$
\boxed{
c^{\rm seq}_{p,j}=-P_{p+j,j}u_{p+j}.
}
\tag{3.2}
$$
这是同一实际未来的准确式；没有估计环境逆后再另选未来。

逐项核对完整右域：

1. 第一段源为 $Dc^{\rm seq}_{p,1}=r_p$。
2. 因 $C$ 与纯尾 $Q_n$ 交换，逐层 $D_nQ_n=I$ 给
$$
C c^{\rm seq}_{p,j}+D c^{\rm seq}_{p,j+1}=0
\quad(1\le j<h).
\tag{3.3}
$$
3. 原有限头旗保持，因为
$$
C^{h-j+1}c^{\rm seq}_{p,j}
=(-1)^{j-1}\widehat Q_{p+j,j}C^{h+1}u_p=0.
\tag{3.4}
$$
4. 真尾旗保持。由 (3.2)、$j\le h$ 和 (1.2)，
$$
D^h c^{\rm seq}_{p,j}
=-D^{h-j}D^j u_{p+j}=-D^h u_{p+j}=0.
\tag{3.5}
$$
5. 最后一段实际为零：
$$
c^{\rm seq}_{p,h}
=\widehat Q_{p+h,h}(-C)^{h-1}C u_p=0.
\tag{3.6}
$$
因此末端 $Cc^{\rm seq}_{p,h}=0$ 已精确封口。

所以 (3.1) 属于原完整右域 $\mathcal Y_{p,h}^{C,\rm full}$。这里只证明其为完整合法候选，**不称它为完整最小链**。它与 $J_fr_p$ 的差才属于全部完整零源核 $Z_f$。

## 4. 原左能量的准确负二次型

把 (1.5) 的真正左最小者 $U_pr_p$ 与负的同源完整链 $-c^{\rm seq}_p$ 拼合，得到真正的 $(C+D)$ 核。其远孔支撑不超过 $p+h$，总孔支撑不超过 $p+h+R<Q$，因此是同一个原 $K_{m,Q}$ 的向量。由 (1.1)，
$$
0=\langle u,U_pr_p-c^{\rm seq}_p\rangle
=\mu_p^2-\sum_{j=1}^h\langle u_{p+j},c^{\rm seq}_{p,j}\rangle.
$$
取实部并用 (3.2)：
$$
\boxed{
\mu_p^2
=-\sum_{j=1}^{h}\operatorname{Re}
  \langle P_{p+j,j}u_{p+j},u_{p+j}\rangle.
}
\tag{4.1}
$$
复内积无论采用哪一变量线性，取实部后的式子相同。由于 (2.4)、(3.6)，还可保留首步正项：
$$
\boxed{
\mu_p^2+\|P_{p+1,1}u_{p+1}\|^2
=-\sum_{j=2}^{h-1}\operatorname{Re}
  \langle P_{p+j,j}u_{p+j},u_{p+j}\rangle.
}
\tag{4.2}
$$
这里没有删掉完整返回。事实上 (4.1) 正是对原完整 flat 配对
$$
F_p^*L_pr_p=P_{\mathcal Y_f}Y_p
$$
测试合法列 $c^{\rm seq}_p$ 的结果；$Y_p=(u_{p+1},\ldots,u_{p+h})$ 保持不变。由于 $c^{\rm seq}_p-J_fr_p\in Z_f$，该差与 $Y_p$ 正交。因而对这个指定标量，完整最小化已经准确消去，未知量变成实际顺次投影的负二次型。

## 5. 跨 cut 的同一层部分和

取整数 $0\le a\le b$，且 $b+h+R<Q$。定义同一物理孔层上的有限和
$$
\mathcal A_{n;a,b}
=\sum_{\substack{1\le j\le h\\a\le n-j\le b}}P_{n,j},
\qquad a+1\le n\le b+h.
\tag{5.1}
$$
求和项始终有 $n\ge j$，所以沿用 §2 的完整有限层定义。把 (4.1) 在同一顶部上求和并仅交换有限求和次序，得到
$$
\boxed{
\sum_{p=a}^{b}\mu_p^2
=-\sum_{n=a+1}^{b+h}
 \operatorname{Re}\langle\mathcal A_{n;a,b}u_n,u_n\rangle.
}
\tag{5.2}
$$
没有在这个过程中重选 $u_Q$、把投影前后向量当成相同来源，或用不同参数的投影望远镜。

若 $a+h\le n\le b+1$，所有 $j=1,\ldots,h$ 都出现，故在 $E_{h,n}$ 上
$$
\mathcal A_{n;a,b}
=\mathfrak N_{h,n}-I,
\tag{5.3}
$$
其中 $\mathfrak N_{h,n}=I+\sum_{j=1}^{h-1}P_{n,j}$ 正是既有顺次 jet 次数算子。两端的实际部分和仍由 (5.1) 保留。

例如若后续对这些真实短核上的 Hermitian 负部证明
$$
\bigl(\operatorname{Re}\mathcal A_{n;a,b}\bigr)_-
\preceq M_{m,R,Q}I,
\tag{5.4}
$$
则 (5.2) 给
$$
\sum_{p=a}^{b}\mu_p^2
\le M_{m,R,Q}\|P_{\mathrm{far}>a}u\|^2.
\tag{5.5}
$$
这是只需控制负二次型的充分入口；本稿没有给出 (5.4) 所需的一致常数，也不以 $\mathfrak N$ 的实特征值为正代替其原物理 Hermitian 部的正性。

## 6. 可用的精确负部公式，以及它没有支付什么

为了明确另一可选充分输入，若 $P$ 是任一非零有界幂等投影，在 $\operatorname{Ran}P\oplus(\operatorname{Ran}P)^\perp$ 中写为
$$
P=\begin{pmatrix}I&A\\0&0\end{pmatrix}.
$$
则
$$
\|P\|=\sqrt{1+\|A\|^2},\qquad
\boxed{\|(\operatorname{Re}P)_-\|=\frac{\|P\|-1}{2}.}
\tag{6.1}
$$
证明可在 $(\operatorname{Re}P)+tI$ 上对正块作 Schur：非负等价于
$t(1+t)\ge\|A\|^2/4$，最小 $t\ge0$ 即右式。$P=0$ 时负部为零。

§2 的每个投影在真正 $E_{h,n}$ 上有界，故 (6.1) 可应用于这个限制。结合 (4.1)，可得到使用其真实限制范数的充分界
$$
\mu_p^2\le
\sum_{j=2}^{h-1}
\frac{(\|P_{p+j,j}|_{E_{h,p+j}}\|-1)_+}{2}
\,\|u_{p+j}\|^2.
\tag{6.2}
$$
既有顺次 jet 稿已将这里的投影范数准确写成完整短核上的顺次／真幂 Gram 比，不能用只压 primitive 的逆替代。另一方面 (5.2) 允许先保真实部分和的抵消，再估其负部；它不要求先逐项用 (6.2)。

## 7. 裸旗为什么还差一个出生

第 $j$ 段裸投影删去的是
$$
E_{j-1,p+j}=\ker D^{j-1}\cap\mathcal H_{p+j}^>,
$$
而 $I-P_{p+j,j}$ 的像是
$$
E_{j,p+j}=\ker D^j\cap\mathcal H_{p+j}^>.
\tag{7.1}
$$
因此仅由 $D^j(c^{\rm seq}_{p,j}+u_{p+j})=0$，不能宣布这个差在第 $j$ 段裸高空间；两者相差整个
$E_{j,p+j}\ominus E_{j-1,p+j}$。

更准确地，令 $P_j^{\rm lo}=I-P_{E_{j-1,p+j}}$。顺次嵌套式给
$$
P_j^{\rm lo}P_{p+j,j}u_{p+j}
=P_j^{\rm lo}u_{p+j}
-P_j^{\rm lo}(P_{p+j,j-1}-P_{p+j,j})u_{p+j}.
\tag{7.2}
$$
这里 $I-P_{p+j,j-1}$ 的像才被裸投影杀掉；最后一项一般必须保留。它是一个准确的顺次出生分量，并不自动位于完整零源核 $Z_f$。

(4.1) 能消去最小化，是因为使用了合法完整列与真实 $u_Q\perp K_{m,Q}$ 的整体配对；不是因为把 (7.1) 的多出一出生免费删掉。继续需要的是原连续尾在同一实际 $u_Q$ 上的负二次型或其跨 cut 部分和预算。上述域、旗与同源身份本身没有证明普通右费上界，也不完成原 $N=M$。
