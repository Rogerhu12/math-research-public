# 边界慢核的单比特图与缺陷正交度量：工作接口

日期：2026-11-13（UTC+8）。作者：boundary。
状态：下述字典及压缩恒等式已证明；尚无新的全局饱和结论。本稿为工作笔记，不另占结果号。

## 1. 既有内容核对与这份笔记的范围

已检索 R143、R187、R200、R226 及边界慢核笔记。真实单比特矩阵并非新发现：R205 §2 已给两个尾归一化幂的对角式及 Cayley 精确分块；R44 和 R143 在其他实际表示和符号中已给相应 Schur 根图。R216 §2 也使用了真实边界链分解。

这里单独记录 $W=M\ominus\overline{BM}$ 在这个有界图下的**准确正交度量**及压缩伴随恒等式。没有把 Haar 尾的稠密像结论搬到负整数边界。

## 2. 同一个实际尾及有界图

按偶、奇坐标分解 $H_-=\widehat H_-\oplus\widehat H_-$。令 $C$ 为归一化真实尾后移，故
$$
N_0=\alpha_0^{-1}B=
\begin{pmatrix}0&I\\ \eta_0 C&0\end{pmatrix},
\qquad \|C\|=1,\qquad \eta_0=\alpha_1/\alpha_0=e^{-1070}.
$$
对每个 $j\ge1$，$N_j$ 与 $Y_j$ 是该位尾算子在两个分量上的同一对角放大。

在尾空间记
$$
A=\sum_{j\ge1}a_jX_j,\qquad a_j=(j+1)^{-2},
$$
其中 $X_j=N_j$ 或 $Y_j$，此处均已删去最低位作尾识别。$A$ 与 $C$ 交换。由 $\|N_j\|=1$、$\|Y_j-E_j\|\le4\eta_j$，
$$
\|A\|<\frac23.
\tag{2.1}
$$
一个不用数值求和的预算为
$$
\sum_{j\ge1}(j+1)^{-2}
\le\frac14+\frac19+\frac1{16}+\frac1{25}+\int_5^\infty x^{-2}\,dx
=\frac{2389}{3600}<\frac23.
$$
Cayley 的误差至多 $4\eta_1(2389/3600)$；实际 $\eta_1=e^{-17960}$，仍在上述余量之内。

定义
$$
Z=\begin{cases}
A,&T=T_N,\\
A(I+A)^{-1},&T=T_Y.
\end{cases}
\tag{2.2}
$$
$I+A$ 的 Neumann 逆实际存在。因而
$$
\|Z\|\le\frac23\quad(N),\qquad \|Z\|\le2\quad(Y).
$$
$N$ 情形 $T_N=N_0+A$；$Y$ 情形准确有
$$
T_Y=(I+A)(N_0+Z)(I+N_0)^{-1}.
$$
各因子交换，外面的两个因子都是有界单位，因此两种情形都给
$$
M=\ker(N_0+Z).
$$
置
$$
K=\ker(Z^2-\eta_0C),\qquad
J:K\to H_-,\quad Ju=(u,-Zu).
$$
两行实际方程立即等价于
$$
\boxed{M=JK,\qquad BJu=-\alpha_0JZu.}
\tag{2.3}
$$
$K$ 闭且由 $Z,C$ 保持；$J$ 是有界同构到 $M$，其逆就是第一坐标投影。此处没有未付闭域或形式开方。

## 3. 真正缺陷对应的度量，不能把环境 $Z^*$ 当成压缩伴随

记
$$
D=Z|_K,\qquad C_K=C|_K.
$$
在尾空间原 Hilbert 内积中，
$$
D^2=\eta_0C_K,\qquad \|C_K\|\le1.
\tag{3.1}
$$
$D^*$ 是 $K$ 内的伴随，即 $D^*=P_KZ^*|_K$。除非另证 $Z^*K\subset K$，不能删去这个压缩。

图度量为
$$
G=J^*J=I_K+D^*D.
$$
故
$$
\langle Ju,Jv\rangle=\langle Gu,v\rangle,\qquad
I\le G\le(1+\|D\|^2)I.
$$
其中 $\langle\cdot,\cdot\rangle$ 对第一变量线性。由 (2.3)，
$$
N=\overline{BM}=J\overline{DK}.
$$
准确的缺陷为
$$
\boxed{
W=J\mathcal W_G,\qquad
\mathcal W_G=K\ominus_G\overline{DK}
=\ker(D^*G)=G^{-1}\ker D^*.
}
\tag{3.2}
$$
因此
$$
W=0\quad\Longleftrightarrow\quad
\overline{DK}=K.
$$
这只把原未知稠密像问题写到了一个真实平方核中，未解决它。

也可使用等距同构 $U=JG^{-1/2}:K\to M$：
$$
U^*(B|_M)U=-\alpha_0G^{1/2}DG^{-1/2}.
$$
其伴随核为 $G^{-1/2}\ker D^*$。这个式子说明相反的向量变换方向不可互换。

## 4. 由平方关系和缺陷正交性同时得到的压缩预算

(3.1) 给
$$
D^*G
=D^*+(D^2)^*D
=D^*+\eta_0C_K^*D.
$$
因此对 $u\in\mathcal W_G$，
$$
\boxed{
D^*u=-\eta_0C_K^*Du,\qquad
\|D^*u\|\le\eta_0\|Du\|.
}
\tag{4.1}
$$
这是 $K$ 中的真实压缩伴随估计，不是对环境 $Z^*u$ 的界。

更一般地，$D^kK\subset DK$ 给
$$
(D^k)^*u=-(D^{k+1})^*Du,\qquad k\ge1.
\tag{4.2}
$$
结合 $D^{2r}=\eta_0^r C_K^r$ 可继续给各阶压缩幂界，但这些界未产生所需的下界。

例如取 (4.2) 的标量配对，原图向量 $w=(u,-Du)\in W$ 满足
$$
|\langle u,Du\rangle|
=|\langle Du,D^2u\rangle|
\le\eta_0\|u\|\,\|Du\|.
\tag{4.3}
$$
所以最低位两个分量的普通相关性超小。这也可直接从
$\langle Bw,w\rangle=0$ 的两个真实矩阵行核得。它不控制 $D^*u$ 在其核正交补上的逆，不自动把近伴随核改成精确伴随核。

## 5. 暂时未闭的下一步与两个已排除的捷径

(4.1) 同时利用了平方关系和正确缺陷度量，但 $D$ 的像可能不闭；没有已知的环境或压缩下界把它转成 $u=0$。将 $\|D^*u\|\ll\|Du\|$ 当作矛盾，等于额外假设尚未证明的压缩正规性或相关下界。

继续逐位 Schur 消元时，第二步已出现低头线性项 $2a_1U-\eta_0I$。其逆存在不意味着范数有可用的统一小预算；后续的高次根图必须重新支付这些逆。

另一个曾检查的方向是用有限头的等距移位膨胀代替 R249 的相似。等距交织 $VT_m=\widetilde J V$ 只给
$$
\widetilde J^*Vh=VT_m^*h+
(I-VV^*)\widetilde J^*Vh.
$$
最后一项在完整空间中与 $VM$ 正交，但人工次数截断后通常不再正交。它含低头项，不是从第 $m$ 位开始的小 carry。因此不能借等距嵌入直接删去 R249 移动正能量的条件数尾项。

此外，$w\in W$ 给 $\langle B^kw,w\rangle=0$ 对所有 $k\ge1$。这只是整个缺陷正交性的必要标量条件。未证明本权移的所有此类向量都有限支撑；一般拟幂零性不能代替该命题。即使构造到一个标量 wandering 向量，也不能只凭这些自矩就宣称它属于 $W$。

