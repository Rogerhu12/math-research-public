# R272：原正常湮灭者的远尾预对偶修复与准确正性障碍

日期：2026-11-14。作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

状态：§§1–8 为完整证明。本文重建
[`2026-11-13-active-unpublished-queue-0c.md`](../notes/2026-11-13-active-unpublished-queue-0c.md)
最末“固定有限原行纯尾源类后的当前任务”中尚未发表的预对偶修复；所用固定行左逆已在
[R236 固定有限原行定理](R236-appendix-fixed-finite-rows-complete-tail-source-embedding-and-normal-closed-range.md)
发表。本文进一步确定：非平凡的这个修复必定失去自伴性，故不能直接变成正正常见证。没有排除一般正常湮灭者，普通 ISP 仍未解决。

## 1. 固定原行、真实左逆和两个不同的尾

保持原 Haar 表示及原范数代数
$$
H=K_n\otimes H_n,\qquad K_n=(\mathbb C^2)^{\otimes n},\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}.
$$
取固定、线性无关的 $S_1,\ldots,S_d\in\mathcal A$，并假设
$\chi(S_i)=0$。这里 $\chi$ 是原拟幂零生成代数的常数字符。
对当前指定慢行，这正是适用情形。

已发表的固定行定理给一个固定 $n$、互异正整数
$r_1,\ldots,r_d<2^n$ 和真实可逆矩阵
$$
U\in M_d(\mathcal B_n)^\times,
\qquad \mathcal B_n=\overline{\mathbb C[I,\widehat N_n]}^{\|\cdot\|},
\qquad C_S=\|U^{-1}\|.
$$
物理头基记为 $\varepsilon_r$，嵌入
$V_r:H_n\longrightarrow H$ 为 $V_ru=\varepsilon_r\otimes u$。
定义正常线性映射
$$
\mathcal L(G_1,\ldots,G_d)
=\sum_{i=1}^d S_i(I_{<n}\otimes G_i),
$$
$$
\mathcal R_i(T)
=\sum_{\ell=1}^d (U^{-1})_{i\ell} V_{r_\ell}^*TV_0.
\tag{1.1}
$$
准确物理首列身份给
$$
\mathcal R\mathcal L=I
\quad\text{在全部 }B(H_n)^d\text{ 上成立}.
\tag{1.2}
$$
这里不要求 $G_i$ 属于交换子，也不要求它们彼此交换。
以列算子空间范数计，$\|\mathcal R\|_{\rm cb}\le C_S$，而
$\|\mathcal L\|_{\rm cb}\le C_L:=\|[S_1\ \cdots\ S_d]\|$。
原小头权以及全部进位已包含在 $U$ 中。

对 $P\ge n$ 区分：
$$
\mathcal T_P=I_{<P}\otimes\{\widehat N_P\}'
\quad\text{和}\quad
\mathcal T_P^{\rm raw}=I_{<P}\otimes B(H_P).
$$
前者属于原 $\mathcal A'$；后者一般不属于。
本文的新精确零式将针对整个 $\mathcal T_P^{\rm raw}$，但保原泛函时仍只使用
$\mathcal T_P\subset\mathcal A'$。

## 2. 真空条件期望及其正常预对偶极限

把
$$
H_n=K_{[n,P)}\otimes H_P
$$
按原物理张量拆开。$\Omega_{n,P}$ 是中间有限段的 Haar 真空，即每个位的
$2^{-1/2}(\varepsilon_0+\varepsilon_1)$ 的张量积；$\Omega_P$ 是余尾真空。
定义
$$
\mathcal E_P(T)
=I_{[n,P)}\otimes
\bigl(\langle\Omega_{n,P}|\otimes I\bigr)
T
\bigl(|\Omega_{n,P}\rangle\otimes I\bigr).
\tag{2.1}
$$
这是 $B(H_n)$ 到 $I_{[n,P)}\otimes B(H_P)$ 的正常、完全正、幺、收缩投影。
其预对偶按双线性迹配对 $\langle\tau,T\rangle=\operatorname{Tr}(\tau T)$ 定义，准确为
$$
\mathcal E_{P,*}(\tau)
=|\Omega_{n,P}\rangle\langle\Omega_{n,P}|
\otimes\operatorname{Tr}_{K_{[n,P)}}\tau.
\tag{2.2}
$$
特别 $\|\mathcal E_{P,*}\|_{1\to1}=1$，且它保迹。

**引理 2.1。** 对每个固定 $\tau\in\mathcal S_1(H_n)$，
$$
\left\|\mathcal E_{P,*}(\tau)
-(\operatorname{Tr}\tau)|\Omega_n\rangle\langle\Omega_n|\right\|_1
\longrightarrow0.
\tag{2.3}
$$

**证明。** 先取 $\tau=|u\rangle\langle v|$，其中 $u,v$ 只依赖有限多个尾位。
只要 $P$ 超过这些位，两向量都可写成中间有限段向量张量 $\Omega_P$。
式 (2.2) 此时准确等于
$\langle v,u\rangle|\Omega_n\rangle\langle\Omega_n|$。
有限柱向量在 $H_n$ 中稠密，因此这类有限秩算子的线性包在迹范数中稠密。
两边的映射都是迹范数收缩；由稠密性得到 (2.3)。$\square$

引理没有给任意固定 $\tau$ 的统一速度，也没有给映射的算子范数收敛。

## 3. 正常投影及全部 raw 远尾源的精确消去

对列逐项使用 $\mathcal E_P$，定义
$$
\mathcal Q_P=\mathcal L\mathcal E_P\mathcal R,
\qquad \mathcal P_P=I-\mathcal Q_P.
\tag{3.1}
$$
由 (1.2) 和 $\mathcal E_P^2=\mathcal E_P$，
$$
\mathcal Q_P^2=\mathcal Q_P,
\qquad \mathcal P_P^2=\mathcal P_P,
\qquad \|\mathcal P_P\|_{\rm cb}\le1+C_LC_S.
\tag{3.2}
$$
全部映射正常，其像、核都在原 $B(H)$ 中。
若
$$
\mathcal W_P^{\rm raw}
=\sum_{i=1}^dS_i\mathcal T_P^{\rm raw},
$$
则
$$
\operatorname{Ran}\mathcal Q_P=\mathcal W_P^{\rm raw},
\qquad \ker\mathcal P_P=\mathcal W_P^{\rm raw}.
\tag{3.3}
$$
理由是 $\mathcal E_P$ 的像恰为全 raw 尾，且 $\mathcal R\mathcal L=I$。

所有 $r_\ell>0$，所以
$$
\mathcal R(I_{<n}\otimes T)=0\qquad(T\in B(H_n)).
$$
于是
$$
\mathcal P_P(I_{<n}\otimes T)=I_{<n}\otimes T.
\tag{3.4}
$$
这不仅保单位，还逐点固定整个 raw $n$ 尾。

## 4. 同一个正常泛函的迹范数修复

令 $\rho\in\mathcal S_1(H)$ 为任意正常迹类，并假设至少有
$$
\operatorname{Tr}(\rho S_i)=0\qquad(1\le i\le d).
\tag{4.1}
$$
定义
$$
\sigma_P=\mathcal P_{P,*}(\rho)
=\rho-C_P,\qquad C_P=\mathcal R_*\mathcal E_{P,*}\mathcal L_*\rho.
\tag{4.2}
$$
把 $\mathcal L_*\rho$ 的第 $i$ 个分量记为
$$
\tau_i=\operatorname{Tr}_{K_n}(\rho S_i)\in\mathcal S_1(H_n).
\tag{4.3}
$$
其迹为零。引理 2.1 给
$$
\delta_P:=\|C_P\|_1
\le C_S\sum_{i=1}^d\|\mathcal E_{P,*}\tau_i\|_1
\longrightarrow0.
\tag{4.4}
$$
因此
$$
\boxed{\sigma_P\longrightarrow\rho\text{ 迹范数};\qquad
\operatorname{Tr}\sigma_P=\operatorname{Tr}\rho.}
\tag{4.5}
$$
保迹由 (3.4) 对 $T=I$ 得到。
更强地，对所有 $T\in B(H_n)$，
$$
\operatorname{Tr}\bigl(\sigma_P(I_{<n}\otimes T)\bigr)
=\operatorname{Tr}\bigl(\rho(I_{<n}\otimes T)\bigr),
\tag{4.6}
$$
即修复准确保持原 $n$ 尾正常边缘密度。

由 (3.3)，修复对全部 raw 尾右源精确为零：
$$
\boxed{
\operatorname{Tr}\left(\sigma_PS_i(I_{<P}\otimes G)\right)=0
\quad\bigl(G\in B(H_P),\ 1\le i\le d\bigr).}
\tag{4.7}
$$
这等价于真正的算子值部分迹等式
$$
\operatorname{Tr}_{K_P}(\sigma_PS_i)=0\in\mathcal S_1(H_P).
\tag{4.8}
$$
没有以弱收敛替换迹范数，也没有把 raw 尾元素误认为原交换子元素。

若 $\rho$ 有限秩，则每个 $\sigma_P$ 仍有限秩。事实上有限维部分迹把有限秩算子送入有限秩算子；式 (2.2)、固定有界乘法和有限和继续保持有限秩。
粗略地，若 $\operatorname{rank}\rho=r$，则
$$
\operatorname{rank}C_P\le d\,2^P r,
\qquad \operatorname{rank}\sigma_P\le(1+d\,2^P)r.
\tag{4.9}
$$
这个秩界依赖 $P$，不声称存在同秩修复。

## 5. 何时准确保持原 $\mathcal A'$ 泛函

现在加上真正的原全右湮灭条件
$$
\operatorname{Tr}(\rho S_iG)=0
\qquad(G\in\mathcal A',\ 1\le i\le d).
\tag{5.1}
$$
它包含 (4.1)。先验证保泛函所需的每一步都是原算子身份。

若 $F\in\mathcal A'$，则 $F$ 与
$A^{2^n}=c_nI_{<n}\otimes\widehat N_n$ 交换，其中 $c_n\ne0$。
所以每个物理头块 $V_r^*FV_s$ 都属于
$\mathcal C_n:=\{\widehat N_n\}'$。
$U^{-1}$ 的条目属于 $\mathcal B_n\subset\mathcal C_n$，故
$$
\mathcal R_i(F)\in\mathcal C_n.
\tag{5.2}
$$
又若 $T\in\mathcal C_n$，则它与
$\widehat N_n^{2^{P-n}}=c_{n,P}I_{[n,P)}\otimes\widehat N_P$ 交换，
$c_{n,P}\ne0$。因此其每个 $[n,P)$ 物理块都与 $\widehat N_P$ 交换。
式 (2.1) 的有限真空压缩只是这些块的线性组合，所以
$$
\mathcal E_P(\mathcal C_n)
\subset I_{[n,P)}\otimes\mathcal C_P.
\tag{5.3}
$$
结合原递推给出的 $\mathcal T_P\subset\mathcal A'$，有
$$
\mathcal Q_P(F)=\sum_iS_iG_{i,P}
\quad\text{且每个 }G_{i,P}\in\mathcal T_P\subset\mathcal A'.
$$
由 (5.1)，
$$
\boxed{\operatorname{Tr}(\sigma_PF)
=\operatorname{Tr}(\rho F)\qquad(F\in\mathcal A').}
\tag{5.4}
$$
特别 $\sigma_P$ 仍满足所有原全右零式 (5.1)，同时额外满足 (4.7)。

若原前提只有 $G\in\mathcal A$ 的零式，则同样的论证只无条件给
$$
\operatorname{Tr}(\sigma_PF)=\operatorname{Tr}(\rho F)
\qquad(F\in\mathcal A).
\tag{5.5}
$$
这时使用原有限余数分解来验证
$\mathcal R_i(\mathcal A)\subset\mathcal B_n$，以及
$\mathcal E_P(\mathcal B_n)\subset I_{[n,P)}\otimes\mathcal B_P$。
后一包含先在 $\widehat N_n$ 的每个幂上由准确块递推成立，再以范数闭包延伸。
没有把 (5.5) 自动扩大为 (5.4)。

## 6. 修正恰是单侧头块：非平凡时必失自伴

以下假设 $\rho=\rho^*\ge0$，且 $\tau=\operatorname{Tr}\rho>0$。
令固定正交头投影
$$
P_0=V_0V_0^*,\qquad Q=\sum_{\ell=1}^dV_{r_\ell}V_{r_\ell}^*.
$$
因为所有 $r_\ell>0$，$P_0Q=0$。
直接从 (1.1) 的迹配对算出
$$
\mathcal R_*(\zeta_1,\ldots,\zeta_d)
=\sum_{i,\ell} V_0\zeta_i(U^{-1})_{i\ell}V_{r_\ell}^*.
\tag{6.1}
$$
所以每个实际修正满足
$$
\boxed{C_P=P_0C_PQ,\qquad C_P^2=0,\qquad\operatorname{Tr}C_P=0.}
\tag{6.2}
$$
这不是渐近性质，而是准确的单侧头块支撑。
若 $\sigma_P$ 自伴，则
$C_P=\rho-\sigma_P$ 自伴；与 (6.2) 一起迫 $C_P=0$。
反之 $C_P=0$ 时 $\sigma_P=\rho\ge0$。因此
$$
\boxed{\sigma_P\text{ 自伴}\ \Longleftrightarrow\
\sigma_P\ge0\ \Longleftrightarrow\ C_P=0.}
\tag{6.3}
$$
准确说，这个单侧预对偶修复不能产生新的正态：它只有在原密度本来已满足所需 raw 约束时才保持正性。
最后一句也可直接核对：$C_P=0$ 等价于
$\rho\circ\mathcal Q_P=0$；而 $\mathcal Q_P$ 的像正是 $\mathcal W_P^{\rm raw}$。

## 7. 正性损失的准确迹范数费用

对任意具有 $C=P_0CQ$、$P_0Q=0$ 支撑的迹类算子，
相对于 $P_0H\oplus QH$，$C-C^*$ 是块矩阵
$$
\begin{pmatrix}0&C\-C^*&0\end{pmatrix}.
$$
它的非零奇异值是 $C$ 的奇异值各重复两次，因而
$$
\left\|\frac{C-C^*}{2i}\right\|_1=\|C\|_1.
\tag{7.1}
$$
由于 $\rho$ 自伴，得到
$$
\|\operatorname{Im}\sigma_P\|_1=\delta_P.
$$
取虚部是迹范数收缩，所以对任意自伴 $T\in\mathcal S_1(H)$，
$$
\|\sigma_P-T\|_1\ge\|\operatorname{Im}\sigma_P\|_1=\delta_P.
$$
而原来的正密度 $\rho$ 已经在距离 $\delta_P$ 处，故
$$
\boxed{
\operatorname{dist}_1(\sigma_P,\mathcal S_1(H)_{\rm sa})
=\operatorname{dist}_1(\sigma_P,\mathcal S_1(H)_+)
=\delta_P=\|\sigma_P-\rho\|_1.}
\tag{7.2}
$$
即任何恢复正性的步骤，至少要花掉与整个新修正等大的迹范数；原 $\rho$ 是一个最近的正密度，但回到它会失去新得到的 raw 零式，除非修正原本为零。

还有一个显式的范数亏损界：
$$
\boxed{\sqrt{\tau^2+\delta_P^2}\le\|\sigma_P\|_1\le\tau+\delta_P.}
\tag{7.3}
$$
上界来自三角不等式。为证下界，令 $J$ 是
$\operatorname{Im}\sigma_P$ 的符号算子，在其核上补成自伴酉。
对每个实 $\theta$，
$U_\theta=\cos\theta\,I+i\sin\theta\,J$ 是酉，且
$$
\operatorname{Re}\operatorname{Tr}(U_\theta\sigma_P)
=\tau\cos\theta-\delta_P\sin\theta.
$$
取右侧最大值得到下界。特别只要修正非零，就
$\|\sigma_P\|_1>\operatorname{Tr}\sigma_P$；不能以“迹锚不变且范数趋近”声称每个修复本身为正态。

## 8. 结论的准确范围与下一未付步骤

对满足原全右零式的任意固定正正常密度 $\rho$，已经有显式有限头构造，使
$\sigma_P$：

1. 迹范数趋于同一 $\rho$，保持同一原 $\mathcal A'$ 泛函与非零迹锚；
2. 保持整个固定 $n$ 尾正常边缘密度；
3. 对固定有限原行乘全部 raw $P$ 尾右因子精确为零；
4. 若原密度有限秩，则每个修复仍有限秩；
5. 只要修正非零，必定非自伴；恢复正性所需的迹范数费用准确等于整个修正量。

因此原队列中的正常预对偶恢复可以完成，但它不能直接替换前面所有依赖正性的
Cayley-selector、gentle measurement 或正 Schur 推论。
式 (4.4) 的速度只由同一真实 $\tau_i$ 的正常尾给出，仍无统一乘增长费用的控制。
把 (4.7) 与 (5.4) 合用得到原完整低头协同源的进一步界，或构造同时保持原泛函、raw 零式和正性的另一种修复，仍是独立未决步骤。

本文排除的是上述明确单侧修复的保正捷径，不排除所有其他正修复，也不构造普通不变子空间。
