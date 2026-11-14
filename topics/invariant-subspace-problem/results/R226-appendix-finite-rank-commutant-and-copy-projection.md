# R226A：边界缺陷的有限秩交换子刻画及高孔副本投影

日期：2026-11-13（Asia/Taipei）。作者：boundary。状态：已证明。

本稿只涉及 R185/R188 的实际负整数边界核。它把未知饱和缺陷准确改写为有限秩交换子，并检查现有空位复制能排除什么。Haar 上 R12/R164 的无紧交换子或 Calkin 忠实性不自动运输到这个边界限制。

## 1. 模型和已有输入

在 $H_-=\ell^2(\mathbb N_0)$ 上，置
$$
Be_0=0,\quad Be_n=\alpha_{v_2(n)}e_{n-1},\quad
N_j=B^{2^j}/d_j,
$$
$$
a_j=(j+1)^{-2},\qquad
T=\sum_j a_jX_j,
\quad X_j=N_j\text{ 全部，或 }X_j=N_j(I+N_j)^{-1}\text{ 全部}.
$$
记
$$
M=\ker T,\quad C=B|_M,\quad N=\overline{CM},\quad W=M\ominus N.
$$
沿用 R187 的实际结论
$$
M\cap\ker B^r=\mathbb Ce_0\quad(r\ge1),\qquad e_0\in N.
\tag{1.1}
$$
实际 $B$ 拟幂零，因而 $C$ 拟幂零。纯孔消灭为 $E_j$，并且
$$
\|N_j\|=1,\quad \|N_j-E_j\|\le\eta_j,
\quad \eta_j\le e^{-770\,16^j}.
\tag{1.2}
$$

## 2. 全部有限秩交换子恰为一个平方零空间

**定理 2.1。** 采用内积对第一变量线性的约定，
$$
\boxed{
\{K\in\{C\}':\operatorname{rank}K<\infty\}
=\{e_0\otimes w:w\in W\},
\quad (e_0\otimes w)x=\langle x,w\rangle e_0.
}
\tag{2.1}
$$
因此
$$
\boxed{N=M\iff\{C\}'\text{ 中没有非零有限秩算子}
\iff\{C\}'\text{ 中没有非零秩一算子}.}
\tag{2.2}
$$
且 (2.1) 中任意两个算子的乘积为零。

证明：若 $K$ 有限秩且与 $C$ 交换，其有限维像空间 $F$ 是 $C$ 不变的。$C|_F$ 的每个特征值也为 $C$ 的特征值，故只能为 0。因此某个 $r$ 满足 $C^rF=0$，由 (1.1) 得 $F\subseteq\mathbb Ce_0$。所以 $K=e_0\otimes w$，其中 $w\in M$。

又 $Ce_0=0$，交换条件恰为
$$
0=CK=KC=e_0\otimes C^*w.
$$
故 $w\in\ker C^*=W$。反向包含由同一等式立即成立。
最后，由 $e_0\in N$，每个 $w\in W$ 均与 $e_0$ 正交，于是所有此类乘积都为零。

这不是 Haar 的无有限秩交换子结论在边界上的重述。边界 $C$ 已经有特征向量 $e_0$，而 Haar 模型的相关证明不能在这里直接使用。

## 3. 所有紧交换子都在交换代数的 Jacobson 根中

**定理 3.1。** 若 $K\in\{C\}'$ 紧，则 $\sigma(K)=\{0\}$。更强地，
$$
\boxed{\{C\}'\cap\mathcal K(M)\subseteq\operatorname{rad}(\{C\}').}
\tag{3.1}
$$

证明：若紧 $K$ 有非零谱点 $\lambda$，围绕该谱点的 Riesz 投影 $P$ 为非零有限秩幂等元，并与 $C$ 交换。定理 2.1 迫 $P^2=0$，与 $P^2=P\ne0$ 矛盾。因此紧交换子全拟幂零。

对任意 $L\in\{C\}'$，$LK$ 仍是紧交换子，故也拟幂零，$I-LK$ 在 $B(M)$ 中可逆。其逆与 $C$ 交换，因而逆仍在 $\{C\}'$。这正是 Jacobson 根的标准等价判据，给出 (3.1)。

此结论没有排除非零紧交换子；它只说明一旦存在，其谱不能提供非零 Riesz 投影。

## 4. 实际弱复制还给出变化高位幂的强回收

旧稿 `2026-11-12-boundary-kernel-vacant-pair-weak-copy-and-noncompact-powers-0c-agent.md` 的 §§1–5 已对每个标准有限块纠错构造的 $g\in M$ 建立以下数据：

- 有限近似 $g_{n+1}\to g$；
- $j_n\to\infty$，$g_{n+1}$ 在第 $j_n,j_n+1$ 两位均真空；
- 记
$$
\mathcal C_j=
\frac{a_{j+1}E_j^*-a_jE_{j+1}^*}
{\sqrt{a_j^2+a_{j+1}^2}},\qquad\|\mathcal C_j\|=1,
\tag{4.1}
$$
则存在实际精确核向量 $w_n\in M$，使
$$
w_n\rightharpoonup0,
\qquad\|w_n-\mathcal C_{j_n}g_{n+1}\|\longrightarrow0.
\tag{4.2}
$$
这里不是任意 $g\in M$ 的定理。

由于输入两位真空，有精确等式
$$
E_{j_n}\mathcal C_{j_n}g_{n+1}
=\frac{a_{j_n+1}}{\sqrt{a_{j_n}^2+a_{j_n+1}^2}}g_{n+1}.
$$
结合 (1.2)、(4.2)、$a_{j+1}/a_j\to1$，得到新回收式
$$
\boxed{N_{j_n}w_n\longrightarrow 2^{-1/2}g\quad\text{强收敛}.}
\tag{4.3}
$$
每个 $N_{j_n}w_n$ 都在 $BM$，故 (4.3) 也独立证明此类 $g\in N$。

若 $K\in\{C\}'$ 紧，由 $w_n\rightharpoonup0$ 得 $Kw_n\to0$。$N_j|_M$ 是 $C$ 的多项式，故
$$
K N_{j_n}w_n=N_{j_n}Kw_n\longrightarrow0,
$$
这里使用全空间 $\|N_j\|=1$。再用 (4.3)，得到
$$
\boxed{Kg=0\quad\text{对每个标准纠错构造的 }g.}
\tag{4.4}
$$
因此所有紧交换子都杀掉这些构造向量的闭线性张成。尚未证明该闭张成等于 $M$ 或 $N$，故不能由 (4.4) 宣称全部紧交换子为零。

## 5. 假想缺陷向量的朴素复制几乎正交于整个核

现取真正未知的 $w\in W$。对每个 $j$，$N_jM\subseteq BM$，所以
$$
P_MN_j^*w=0.
$$
由真实比较 (1.2)，立即得到
$$
\boxed{\|P_ME_j^*w\|\le\eta_j\|w\|.}
\tag{5.1}
$$
对 (4.1) 的双位复制算子，
$$
\boxed{
\|P_M\mathcal C_jw\|
\le\frac{a_{j+1}\eta_j+a_j\eta_{j+1}}
{\sqrt{a_j^2+a_{j+1}^2}}\|w\|
\le\sqrt2\,\eta_j\|w\|.
}
\tag{5.2}
$$
另一方面，两位真空投影 $P_{00}^{j,j+1}$ 强趋于 $I$，$\mathcal C_j$ 在该真空空间是等距，且全空间范数为 1。因此每个固定 $w$ 满足
$$
\|\mathcal C_jw\|\longrightarrow\|w\|.
$$
与 (5.2) 合并，得到
$$
\boxed{\operatorname{dist}(\mathcal C_jw,M)\longrightarrow\|w\|.}
\tag{5.3}
$$
故若存在非零缺陷向量，直接取 $P_M\mathcal C_jw$ 会把复制几乎全部消去，不能给所需的核内弱副本。

## 6. 与此同时，朴素复制的真实核残量趋于零

以上距离结论与真实小残量并不矛盾。下面把全部 carry 付清。

对 $i<j$，真实有限链给
$$
N_i=N_i^{[j]}+
\frac{\alpha_j}{\alpha_i}E_i^*\cdots E_{j-1}^*N_j.
$$
有限头与前缀均与 $\mathcal C_j$ 交换，故
$$
\|[N_i,\mathcal C_j]\|\le2\alpha_j/\alpha_i.
$$
对 $Y_i=N_i(I+N_i)^{-1}$，准确逆恒等式给
$$
[Y_i,\mathcal C_j]
=(I+N_i)^{-1}[N_i,\mathcal C_j](I+N_i)^{-1},
$$
范数界放大至 $18\alpha_j/\alpha_i$。对 $i>j+1$ 两种交换子都为零。

第 $j,j+1$ 项的纯交换子准确为
$$
\left[a_jE_j+a_{j+1}E_{j+1},\mathcal C_j\right]
=\frac{2a_ja_{j+1}}{\sqrt{a_j^2+a_{j+1}^2}}
(P_{j+1}-P_j),
\tag{6.1}
$$
其中 $P_i=E_i^*E_i$ 为第 $i$ 位有孔投影。用 $\|Y_i-E_i\|\le4\eta_i$，并取 $\sum a_i\le2$，全部误差满足
$$
\left\|[T,\mathcal C_j]-
\frac{2a_ja_{j+1}}{\sqrt{a_j^2+a_{j+1}^2}}(P_{j+1}-P_j)\right\|
\le64\eta_{j-1}.
\tag{6.2}
$$
例如低位项总额不超过 $18(\sum_{i<j}a_i)\eta_{j-1}\le36\eta_{j-1}$，两项纯比较误差不超过 $8(a_j\eta_j+a_{j+1}\eta_{j+1})\le16\eta_{j-1}$，总额 52 已小于所用 64。不存在固定低位 $\eta_0$ 的未衰减误差。

因此对任意 $w\in M$，
$$
\|T\mathcal C_jw\|
\le 2a_j\|(P_{j+1}-P_j)w\|+64\eta_{j-1}\|w\|
\longrightarrow0.
\tag{6.3}
$$
而且 $\mathcal C_jw\rightharpoonup0$，因为每个输出在第 $j$ 位或更高位有孔。

若 $0\ne w\in W$，置 $z_j=(I-P_M)\mathcal C_jw$，则
$$
z_j\in M^\perp,\qquad z_j\rightharpoonup0,\qquad
\|z_j\|\longrightarrow\|w\|>0,\qquad
\|Tz_j\|\longrightarrow0.
\tag{6.4}
$$
(6.4) 给出在实际核正交补内的奇异序列；它仅反映 $T$ 的非闭值域行为，不产生矛盾。尤其不能以 $T\mathcal C_jw\to0$ 为由，把 (5.3) 的范数距离直接改写成趋于零。

## 7. 剩余准确接口

定理 2.1 将边界饱和与有限秩交换子排除完全等价化。已有真实弱复制可杀掉紧交换子作用在标准构造类上的部分，并给 (4.3) 的变化高位强回收。若要由此证明 $N=M$，还需证明此类复制或另一个排有限秩机制覆盖每个 $M$ 向量。

式 (5.2)—(6.4) 指明一个具体障碍：在假想的缺陷 $W$ 上，朴素高位创建确实具有小的真实残量，却与精确核保持几乎全部原范数的距离。故必须新建一个有控制的核内纠错或其他矛盾，不能把有限头修复预算或普通小残量当作这一步。
