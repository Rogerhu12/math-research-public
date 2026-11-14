# R236 附录：实际 dyadic 符号翻转、正常尾理想与分支提升费用

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的原模型结构与费用归约。** 全文使用原 Haar 尾、原完整交换子及超弱闭理想。没有把超弱稠密和转成有界分支投影，也没有得到原 $G_l$ 的统一商范数上界。

## 1. 同一实际尾与两生成元

固定一位 $l$，略去下标，记
$$
N=N_l=\begin{pmatrix}0&t\\I&0\end{pmatrix},\qquad
t=\eta_lN_{l+1},\qquad 0<\eta_l<1.
$$
令 $\mathcal C=\{N_l\}'$、$\mathcal B=\mathcal C_{l+1}$。
这里 $\mathcal B$ 仍是**完整交换子**，不是仅范数多项式代数。
实际块分解为
$$
\mathcal C=\mathcal B\oplus N\mathcal B,
\qquad a+Nb=\begin{pmatrix}a&tb\\b&a\end{pmatrix},
\qquad \|a\|,\|b\|\le\|a+Nb\|.
\tag{1.1}
$$
两实际符号满足
$$
S=D(N+G),\quad Z=E+NF,\quad D^{-1}\text{ 是实际有界尾逆},
$$
$$
h=G^2-t,\qquad k=E-GF.
$$
在首形式阶一的递推中，$G$ 属于实际范数尾代数且拟幂零。

置
$$
J=\overline{S\mathcal C+Z\mathcal C}^{uw},\qquad
K=\overline{h\mathcal B+k\mathcal B}^{uw}.
$$
[完整正常尾余式恒等式](R236-appendix-normal-tail-ideal-closure-and-finite-amplification.md)给
$$
J=\{a+Nb:a-Gb\in K\},\qquad J\cap\mathcal B=K.
\tag{1.2}
$$
以下假设 $J\ne\mathcal C$，等价地 $K\ne\mathcal B$。
这是任何非零正常湮灭见证所必需的情形。
同样证明适用于任意超弱闭尾理想 $K\ni h$，再以 (1.2) 定义 $J$。

## 2. 快因子可在超弱闭尾理想中准确取消

**引理 2.1。** 若 $L\subset\mathcal C_s$ 是超弱闭理想，则
$$
N_sR\in L\quad\Longrightarrow\quad R\in L.
\tag{2.1}
$$

证明：对 $m>s$，令
$$
d=2^{m-s},\qquad
\beta_{s,m}=\prod_{r=s}^{m-1}\eta_r^{\,2^{m-1-r}},\qquad
V_{s,m}=\beta_{s,m}^{-1}N_s^{d-1}.
\tag{2.2}
$$
每个 $V_{s,m}$ 都是实际有界多项式，且
$$
N_sV_{s,m}=N_m.
$$
所以 $N_mR\in L$。原实际弱单位满足 $N_m\to I/2$ WOT，且
$\|N_mR\|\le\|R\|$，故这也是超弱收敛。
$L$ 的超弱闭性给 $R/2\in L$。证毕。

该证明不要求 $V_{s,m}$ 一致有界。事实上其原范数准确为
$$
\boxed{\|V_{s,m}\|=\prod_{r=s}^{m-1}\eta_r^{-1}.}
\tag{2.3}
$$
为核对费用，实际矩阵递推直接给
$$
\|N_s^{2q}\|=\eta_s^q\|N_{s+1}^q\|,\qquad
\|N_s^{2q+1}\|=\eta_s^q\|N_{s+1}^q\|.
$$
奇幂式的另一个块范数至多
$\eta_s^{q+1}\|N_{s+1}^{q+1}\|\le\eta_s^{q+1}\|N_{s+1}^{q}\|$。
对 $d-1=2^{m-s}-1$ 递归，除以 (2.2) 的 $\beta_{s,m}$，恰得 (2.3)。
这保留了所有 carry，并非把 $N_s$ 换成平方零矩阵。

由于 $h\in K$，另有
$$
GR\in K\Longrightarrow G^2R\in K
\Longrightarrow tR\in K\Longrightarrow R\in K.
\tag{2.4}
$$
所以 $G$ 在完整正常尾商中是准确可取消的因子。
这里的可取消性不等于有界逆。

## 3. 局部符号翻转的准确交与超弱稠密和

令 $\Gamma=\operatorname{diag}(I,-I)$，$\gamma=\operatorname{Ad}\Gamma$。
这是原物理头上的正常完全等距自同构，固定 $\mathcal B$，并满足
$\gamma(N)=-N$。由 (1.2)，
$$
\gamma(J)=\{a+Nb:a+Gb\in K\}.
$$
于是
$$
\boxed{J\cap\gamma(J)=K\oplus NK=K\mathcal C.}
\tag{3.1}
$$
证明：同时属于两个理想等价于 $a\in K$、$Gb\in K$；
(2.4) 给 $b\in K$。反向直接成立。
右边是超弱闭空间，因为两个实际块系数映射都正常。

另一方面，$N+G\in J$，$-N+G\in\gamma(J)$，故
$N\in J+\gamma(J)$。用 (2.1) 的相同快单位，得到
$$
\boxed{\overline{J+\gamma(J)}^{uw}=\mathcal C.}
\tag{3.2}
$$
这个单位逼近具有实际右源。准确地，
$$
N_m=S A_m-\gamma(S)A_m,\qquad
A_m=\frac12D^{-1}V_{l,m},
$$
$$
\boxed{\|A_m\|\le\frac12\|D^{-1}\|
\prod_{r=l}^{m-1}\eta_r^{-1}.}
\tag{3.3}
$$
目标 $2N_m\to I$ 超弱且范数至多 $2$；各分支源则保留 (3.3) 的费用。
没有从 (3.2) 推出有界 Bézout 源。

特别，若 $J$ 在这一个实际局部翻转下不变，则 (3.2) 迫 $J=\mathcal C$。
因此任何非零正常湮灭见证对应的真理想都不能对该翻转不变。
物理偶、奇系数提取不能无条件下降到这个真商。

## 4. 两分支余式图像的准确度量

置 $Q=\mathcal B/K$，$g=G+K$、$t_0=t+K$。
商 $Q$ 是含单位交换 Banach 代数，$g^2=t_0$。
由 (2.4)，乘法 $b\mapsto gb$ 单射。
由于实际 $G$ 拟幂零，其商像 $g$ 仍拟幂零，故不可能可逆。

局部两个余式定义单射代数映射
$$
\mathcal R:\mathcal C/(K\oplus NK)\longrightarrow Q\oplus Q,
$$
$$
\boxed{\mathcal R([a+Nb])=(a-gb,\ a+gb).}
\tag{4.1}
$$
本节右侧的 $a,b$ 已表示其 $Q$ 商类。
乘法性来自 $g^2=t_0$。
准确像空间为
$$
\boxed{\operatorname{Ran}\mathcal R
=\{(u,v):v-u\in2gQ\}.}
\tag{4.2}
$$
当该条件成立时，$a=(u+v)/2$，而 $b$ 是 $gb=(v-u)/2$ 的唯一商解。
由实际块压缩及 $\|N\|=1$，
$$
\boxed{
\max\{\|a\|_Q,\|b\|_Q\}
\le\|[a+Nb]\|_{\mathcal C/(K\oplus NK)}
\le\|a\|_Q+\|b\|_Q.
}
\tag{4.3}
$$
上界通过分别选择 $a,b$ 的近最小范数代表取得，不要求商范数被取到。
因此分支提升的缺失费用准确就是乘法 $g$ 的逆在 $gQ$ 上的费用。

这个逆必不有界。若存在 $c>0$ 使 $\|gb\|_Q\ge c\|b\|_Q$，
则反复作用于单位给 $\|g^n\|_Q\ge c^n$，与拟幂零矛盾。
故 $gQ$ 不范数闭，(4.1) 的像也不范数闭。

更强地，任何 $Q$ 的字符 $\chi$ 满足 $\chi(g)=0$。
所以所有 $(u,v)\in\operatorname{Ran}\mathcal R$ 都满足
$\chi(u)=\chi(v)$；指定分支 $(I,0)$ 距这个像的最大乘积范数至少 $1/2$。而 $(I/2,I/2)$ 属于该像，所以这个距离准确等于 $1/2$。
特别，不能在这个商里用算子范数逼近构造选定分支的幂等元。
这不与 (3.2) 的超弱稠密和冲突：字符在这里没有被声称正常。

## 5. 明确快正则器的商费用也必须发散

这节固定当前 $l$，只让后续快位 $m\to\infty$。
令 $V_m=V_{l+1,m}$；于是 $N_{l+1}V_m=N_m$。
在 $Q$ 中定义
$$
b_m=\frac2{\eta_l}(G V_m+K).
$$
准确有
$$
g b_m=2(N_m+K),
\tag{5.1}
$$
因为 $G^2V_m-\eta_lN_m=hV_m\in K$。
虽然右边有原范数至多 $2$ 的代表并超弱趋单位，仍有
$$
\boxed{\operatorname{dist}(G V_m,K)\longrightarrow\infty.}
\tag{5.2}
$$

证明不需要抽象商表示。若某子列距离有界，选 $H_m\in K$ 使
$R_m=GV_m-H_m$ 在原 $\mathcal B$ 中一致有界。
从其超弱紧球取聚点 $R\in\mathcal B$。
每一项
$$
G R_m-\eta_lN_m=hV_m-GH_m\in K.
$$
正常乘法和 $K$ 的超弱闭性给
$GR-\eta_lI/2\in K$。
但 $G$ 与 $R$ 交换，$GR$ 拟幂零，故 $GR-\eta_lI/2$ 在
$\mathcal B$ 中可逆，迫 $K=\mathcal B$，矛盾。证毕。

这是真正的完整超弱尾商距离发散，**不是**只对 raw 范数作估计。
它针对固定 $l$ 的这个快正则器族；没有给 (5.2) 的统一速度，
也不把它误用成随 $l$ 变化的 $\operatorname{dist}(G_l,K_{l+1})$ 下界。

例如 $a_m=N_m+K$ 与 $b_m$ 给两分支商元素
$[a_m-Nb_m/2]$，其两个余式分别为 $2(N_m+K)$ 和 $0$。
由 (4.3)、(5.2)，它们的原商范数必趋无穷。
这里“某一分支弱趋单位、另一分支为零”的准确代数选择虽存在，
其有界提升已经被 (5.2) 排除。

## 6. 返回原单位 $U$：下一尾代表问题与 $G$ 完全等价

令
$$
L=(I+t)/2,\quad M=(I-t)^{-2},\quad U=(G+L)^{-1}.
$$
$U$ 是原实际尾单位，且直接乘法给
$$
\boxed{U=-4(G-L)M+4UhM.}
\tag{6.1}
$$
因此模任何包含 $h$ 的闭尾理想 $K$，
$$
u=-4(g-\ell)m,\qquad
g=\ell-\tfrac14u(I-t_0)^2.
$$
完整商费用满足双侧界
$$
\boxed{
\frac4{(1+\eta_l)^2}\operatorname{dist}(G-L,K)
\le\operatorname{dist}(U,K)
\le\frac4{(1-\eta_l)^2}\operatorname{dist}(G-L,K).
}
\tag{6.2}
$$
所以便宜的下一尾 $U$ 代表恰好等价于便宜的 $G-L$ 代表，
不只是两个相似的充分条件。

若已有有限实际修正 $G-R=ha+kb$，取
$Y=-4(R-L)M$，则
$$
\boxed{U-Y=4h(U-a)M-4kbM.}
\tag{6.3}
$$
这保留了真实两生成元源；例如其两系数范数分别至多
$4(1-\eta_l)^{-2}(\|U\|+\|a\|)$ 和
$4(1-\eta_l)^{-2}\|b\|$。
反向若 $U-Y=ha+kb$，取
$R=L-\tfrac14Y(I-t)^2$，则
$$
\boxed{
G-R=h\{U-\tfrac14a(I-t)^2\}
-\tfrac14kb(I-t)^2.
}
\tag{6.4}
$$
这些源公式明确说明：商代表费用的等价本身没有支付原 $U$ 或全部源的范数。

## 7. 第二生成元允许的实际修正仍需逐个支付逆

保留原 $C=DG$。对任何使 $D+\lambda F$ 可逆的复数 $\lambda$，
$$
G_\lambda=(C+\lambda E)(D+\lambda F)^{-1}
$$
满足准确身份
$$
\boxed{G_\lambda-G=\lambda k(D+\lambda F)^{-1}.}
\tag{7.1}
$$
因此这是全部 $k$ 修正中一个合法的具体族，而不是形式换生成元。
若 $F$ 本身为实际单位，还可取 $G_Z=EF^{-1}$，有
$G_Z-G=kF^{-1}$。
但 $\|(D+\lambda F)^{-1}\|$、$\|F^{-1}\|$ 仍须按原物理度量支付。
单凭下一尾字符非零只证明每个逆存在，不给任何随层一致的界。

实际下一目标是对 (6.3)–(6.4) 或更一般的 $h/k$ 修正给出有界代表及所需来源预算。
本稿已排除了通过 (3.2) 免费制造有界分支选择的步骤；
没有排除使用完整两生成元作其他有费的修正。
