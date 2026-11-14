# 实际慢平方的首位 monic 消元及其不可忽略的范数损失

日期：2026-11-12（UTC）。作者：critical_kernel。
状态：完整实际接口；不编号研究记录。

本文把实际慢平方共振的首物理位消去，得到一个真正的尾部 monic 四阶闭算子。
两边非零核严格等价，所有乘法都先在已证全幂域上完成。
该归约不把一个形式除法当作有界算子。
末节证明：在假设非零核存在时，最直接的 adjugate 嵌入必不有界下有界，
因此不能靠它无损传递未知分支上的图范数估计。

## 1. 实际平方及尾部设置

取
$$
u=a\chi_0+\sum_{j\ge1}a_j\chi_j,\qquad
a\ne0,\qquad (a_j)_{j\ge1}\in\ell^2\setminus\ell^1.
$$
第一项记为 $a$，避免与尾系数混淆。
令 $X=X_u$ 为 R125 的实际闭第一阶，
$$
\mathcal B_2=\sum_{j\ge0}a_j^2(I-V_j^2),
\qquad a_0=a.
$$
该级数绝对范数收敛，属于 $\mathcal A$，字符为零。
R176 给点态 $u^2-a^2$ 的真实闭乘子
$$
P=X^2+\mathcal B_2-a^2I,\qquad
\operatorname{Dom}P=\operatorname{Dom}X^2.
\tag{1.1}
$$
不把 (1.1) 换成无 Bell 修正的 $X^2-a^2I$。

按首物理位分解 $H=\mathbb C^2\otimes H_{\rm tail}$。
在尾空间上记
$$
W=X_{\sum_{j\ge1}a_j\chi_j},\qquad
Z=\sum_{j\ge1}a_j^2(I-V_j^2).
\tag{1.2}
$$
$W$ 为真正的闭尾第一阶，$Z$ 为尾 $\mathcal A_{\rm tail}$ 元素，
字符为零。尾第一阶仍单射、稠密像。
这里使用的 R125/R176 尾版本逐式沿用其证明：
删去有限头不改变进位关系、尾权的超快估计、循环真空和公共有限柱核心。

所有尾算子在原空间上按 $I_2\otimes(\cdot)$ 作用。
为简记，公式中不重复写这个张量恒等因子。
有
$$
X=aV_0+W.
\tag{1.3}
$$
$V_0$ 有界并与 $W$ 完整域交换。
因此
$$
\operatorname{Dom}X^r=\operatorname{Dom}W^r
\quad(r\ge1)
\tag{1.4}
$$
按此两分量解释：有限二项式逐次验证两向包含即可。
在这个真实域上，
$$
P=W^2+2aV_0W+Z.
\tag{1.5}
$$

## 2. 真实首位矩阵

置
$$
t=\eta_0N_1\in\mathcal A_{\rm tail},
\qquad
s=(I+t)(I-t)^{-1}.
$$
$t$ 拟幂零，$I-t$ 为实际有界单位。
首位进位给
$$
N_0=
\begin{pmatrix}
0&t\\ I&0
\end{pmatrix},
\qquad N_0^2=tI_2.
$$
于是
$$
V_0=(I-N_0)(I+N_0)^{-1}
=
\begin{pmatrix}
s&-2t(I-t)^{-1}\\
-2(I-t)^{-1}&s
\end{pmatrix}.
\tag{2.1}
$$
这是完整实际等式，不是把 $t$ 忽略后的纯块。

定义尾闭表达式
$$
A_0=W^2+2asW+Z,\qquad
B_0=-4a(I-t)^{-1}W.
\tag{2.2}
$$
$A_0$ 的自然域为 $\operatorname{Dom}W^2$，
$B_0$ 的自然域为 $\operatorname{Dom}W$。
所有有界系数与 $W$ 的全部自然幂域交换。
由 (1.5)，
$$
\boxed{
P=
\begin{pmatrix}
A_0&tB_0\\
B_0&A_0
\end{pmatrix}
\quad\text{于 }\operatorname{Dom}W^2\oplus\operatorname{Dom}W^2.
}
\tag{2.3}
$$

## 3. 不经除法的真实 monic 四阶式

在 $\operatorname{Dom}W^4$ 上置
$$
\Delta=A_0^2-tB_0^2.
$$
因所有系数交换，展开并使用
$$
s^2-4t(I-t)^{-2}=I
$$
得
$$
\boxed{
\Delta
=(W^2+Z)^2+4asW(W^2+Z)+4a^2W^2.
}
\tag{3.1}
$$
等价地，
$$
\Delta=
W^4+4asW^3+(2Z+4a^2I)W^2+4asZW+Z^2.
\tag{3.2}
$$
这是最高系数为 $I$ 的真实有界系数多项式。
由 R176，它在自然域 $\operatorname{Dom}W^4$ 上闭且 $C$ 自伴，
与其最大正则化图相同。

记
$$
M=\ker P,\qquad K=\ker\Delta.
$$
R176 的 monic 核结论分别给
$$
M\subseteq\bigcap_{r\ge1}\operatorname{Dom}(I_2\otimes W)^r,
\qquad
K\subseteq\bigcap_{r\ge1}\operatorname{Dom}W^r.
\tag{3.3}
$$
且相应第一阶在两个核上的限制均有界。
(3.3) 是下述所有 adjugate 乘法的实际域依据。

### 3.1 从首位核到尾核

若 $(u,v)\in M$，则
$$
A_0u+tB_0v=0,\qquad B_0u+A_0v=0.
$$
由 (3.3)，可合法再乘 $A_0,B_0$，得到
$$
A_0^2u=tB_0^2u,\qquad
A_0^2v=tB_0^2v.
$$
所以
$$
\boxed{M\subseteq K\oplus K.}
\tag{3.4}
$$

### 3.2 从尾核到首位核的两个显式嵌入

对 $h\in K$，定义
$$
G_1h=(-A_0h,B_0h),\qquad
G_2h=(-tB_0h,A_0h).
\tag{3.5}
$$
(3.3) 使输出在 $\operatorname{Dom}W^2\oplus\operatorname{Dom}W^2$。
直接矩阵乘法给
$$
PG_1h=(-\Delta h,0),\qquad
PG_2h=(0,\Delta h).
$$
因此两映射都把 $K$ 送入 $M$。

$W|_K$ 有界，所以 $G_1,G_2:K\to M$ 都有界。
又
$$
B_0=-4a(I-t)^{-1}W
$$
的全空间核为零，因为 $a\ne0$、$(I-t)^{-1}$ 为单位，
且实际尾第一阶 $W$ 单射。
所以 $G_1$ 单射。

由 (3.4)—(3.5)，
$$
\boxed{\ker P=\{0\}\quad\Longleftrightarrow\quad\ker\Delta=\{0\}.}
\tag{3.6}
$$
没有取消一个未知限制上的 $W$，也没有断言 $B_0^{-1}A_0$ 有界。

## 4. 与已排除的安全平方分支相容

本节使用此前已证的 R142/R144 平方安全因子结论，而非增加新的排核假设。

在 $\mathcal A$ 中取
$$
Y=(a^2I-\mathcal B_2)^{1/2},
\qquad \chi(Y)=a.
\tag{4.1}
$$
这是真正的全纯演算：$\mathcal B_2$ 拟幂零，选在 $a^2$ 附近取值为 $a$ 的平方根支。
有
$$
P=(X-Y)(X+Y)
$$
于自然域 $\operatorname{Dom}X^2$ 上。
最低首位系数比较使 $X+Y$ 单射。
所以
$$
\boxed{M=\ker(X-Y).}
\tag{4.2}
$$
反向域也准确：若 $Xx=Yx$，$Y$ 保持 $\operatorname{Dom}X$，
故 $x\in\operatorname{Dom}X^2$。

在 $M$ 上，
$$
W=X-aV_0=Y-aV_0=:D.
\tag{4.3}
$$
$D\in\mathcal A$ 且
$$
\chi(D)=a-a=0.
$$
所以 $D$ 在全空间拟幂零，其在非零 $M$ 上的限制也拟幂零。

### 4.1 四阶尾核只可能保留零谱分支

由 (3.2)，在字符层的多项式为
$$
q(w)=w^2(w+2a)^2.
$$
所有系数减去字符后的项在尾代数中拟幂零，并与有界 $W|_K$ 交换。
故 $q(W|_K)$ 拟幂零，谱映射给
$$
\sigma(W|_K)\subseteq\{0,-2a\}.
\tag{4.4}
$$

有界单射 $G_1:K\to M$ 满足真实交织
$$
(I_2\otimes W)|_M\,G_1=G_1(W|_K).
\tag{4.5}
$$
目标算子由 (4.3) 拟幂零。

若 $W|_K$ 在 $-2a$ 有非零 Riesz 谱部分 $K_-$，
则在一个只围住 $-2a$ 的小圆上对 resolvent 交织积分，
得到 $G_1|_{K_-}=0$：
目标谱仅含0，故其 contour 积分为零。
这与 $G_1$ 单射矛盾。
于是
$$
\boxed{K\ne0\ \Longrightarrow\ \sigma(W|_K)=\{0\}.}
\tag{4.6}
$$
这一步只传递了有限谱的分支排除，没有传递算子范数上界。

## 5. 这个 adjugate 嵌入在非零核上必有范数损失

假设 $K\ne0$。
由 (4.6)，$W|_K$ 拟幂零。
$t|_K,Z|_K$ 来自尾代数的零字符元素，也拟幂零，
并与 $W|_K$ 及各单位系数交换。
所以 (2.2) 给
$$
A_0|_K,\ B_0|_K
$$
为两个交换的有界拟幂零算子。

以下初等事实可直接使用。

**引理。** 若 $S,T$ 为交换的有界拟幂零算子，作用于非零 Banach 空间，
则列映射 $x\mapsto(Sx,Tx)$ 不可能有正的有界下界。

**证明。** 若存在 $c>0$ 使
$$
c\|x\|\le\|Sx\|+\|Tx\|,
$$
则反复应用并使用交换性，
$$
c^n\|x\|
\le\sum_{j=0}^n\binom nj\|S^jT^{n-j}x\|.
$$
对任意 $\varepsilon>0$，拟幂零性给
$\|S^j\|\le C_S\varepsilon^j$、
$\|T^j\|\le C_T\varepsilon^j$。
于是
$$
c^n\le C_SC_T(2\varepsilon)^n,
$$
取 $2\varepsilon<c$ 后令 $n\to\infty$ 矛盾。证毕。

应用于 $A_0|_K,B_0|_K$，得到
$$
\boxed{
\inf_{\|h\|=1,\ h\in K}
\bigl(\|A_0h\|^2+\|B_0h\|^2\bigr)^{1/2}=0.
}
\tag{5.1}
$$
因此有界单射 $G_1$ 不有界下有界，其像不闭。
同时使用两个嵌入也不能修补：
$$
\|G_1h\|^2+\|G_2h\|^2
\le C\bigl(\|A_0h\|^2+\|B_0h\|^2\bigr),
$$
故联合列 $h\mapsto(G_1h,G_2h)$ 仍没有正下界。

可以把 (5.1) 的单位序列选成弱趋零：
任意弱极限都在 $B_0|_K$ 的核中，而这个核为零。
因此不是一个有限维退化。

这说明：在假设非零核存在时，
不能通过这两个自然 adjugate 嵌入的逆去无损传递有界分支范数。
要完成递归排核，必须另找一个实际估计；这里缺少的下界不是尚未算好的常数，而是严格不存在。

## 6. 像闭包与尚未证明的限制稠密

对 $(u,v)\in M$，(2.3) 给 $B_0u=-A_0v$，因此
$$
(B_0u,B_0v)=G_1v.
$$
于是
$$
\boxed{
\overline{(I_2\otimes B_0)M}
\subseteq\overline{G_1K}\subseteq M.
}
\tag{6.1}
$$
这里 $B_0$ 在 $M$ 上的作用有界，
因为 $W|_M$ 已由 (4.3) 有界。

若另外证明 $B_0M$ 在 $M$ 中稠密，才可从 (6.1) 得到 $G_1K$ 在 $M$ 中稠密。
现有论证没有提供这条限制像稠密性。
全空间 $W$ 的单射稠密像不能代替它。

这和“$G_1$ 的像不闭”并不冲突：像可以稠密且不闭，
也可以有真闭包。本文不在这两个可能之间作未经证明的选择。

## 7. 继续剥首位时准确的谱中心与域边界

回到原空间上的 $M=\ker P$。
对任意 $m\ge1$，实际尾第一阶
$$
W_m=X_{\sum_{j\ge m}a_j\chi_j}
$$
与 $X-\sum_{j<m}a_jV_j$ 仅差有界有限头项，
所以 $M\subseteq\operatorname{Dom}W_m$，并且
$$
W_m|_M
=
\left(Y-\sum_{j<m}a_jV_j\right)\big|_M.
\tag{7.1}
$$
右侧为真正的 $\mathcal A$ 元素限制。
若 $M\ne0$，其谱恰为
$$
\boxed{
\sigma(W_m|_M)
=
\left\{a-\sum_{j<m}a_j\right\}.
}
\tag{7.2}
$$
零字符部分拟幂零，非零字符移位为单位，故这个谱式是实际的。

因此
$$
\left|a-\sum_{j<m}a_j\right|
\le\|W_m|_M\|
\le\|Y\|+6\sum_{j<m}|a_j|.
\tag{7.3}
$$
这些谱中心是按原顺序的有符号部分和，不是绝对值部分和。
例如交替尾可以使它们保持有界；(7.3) 本身不产生矛盾。
上界也不提供与 $m$ 无关的分支范数。

尤其不能从 $M$ 中向量有全部自然幂就断言 $W_mx\to0$。
独立记录
《实际反障碍：全部自然幂域与逐项系数截断不是同一件事》
已经给出实际 $x$：
全部自然幂及全部条件期望图逼近均成立，
但 $\|\sum_{j<m}a_jV_jx\|$ 沿一列截断发散。
那不是不变分支反例，却严格阻断仅凭全幂域交换这个极限。

本文完成的是准确的首位四阶消元、谱分支缩减和不可避免的 adjugate 范数损失。
原慢平方的单核仍未被排除，也未构造非零原 Haar 核向量。
