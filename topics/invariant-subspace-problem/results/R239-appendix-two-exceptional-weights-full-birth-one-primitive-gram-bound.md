# R239 附录：两个独立异权位与等权池的全部出生层 Gram 上界

日期：2026-11-13（UTC）。作者：central_review；AI-assisted，GPT-6 Astra Pro。
状态：已证明。通用整数多项式证书由作者与根代理分别在 V8 中执行通过；正文的完整最小逆、端点与非交换同余均已逐式核验。

§§1–7 先证明出生一层的完整非交换比较；§8 给任意独立头权的饱和固定线正矩公式，§9 将同一两异权模型扩到全部合法出生层。

## 1. 定理与准确对象

取整数 $M\ge2$、正实数 $a,b$，在 $M+2$ 个布尔位的标准有限 Hilbert 空间上令
$$
D=aE_1+bE_2+\sum_{j=3}^{M+2}E_j.
\tag{1.1}
$$
$E_j$ 是删除算子：
$$
E_je_I=\mathbf1_{j\in I}e_{I\setminus\{j\}}.
$$
第 $s$ 孔层为 $\mathcal H_s$，并定义完整 primitive 源空间
$$
K_1=\ker D\cap\mathcal H_1.
$$
对 $0\le k\le M$，令
$$
F_k=\frac{D^k(D^*)^k|_{\mathcal H_1}}{(k!)^2},
\qquad
\Gamma_k=P_{K_1}F_k^{-1}|_{K_1}.
\tag{1.2}
$$
约定 $F_0=I$、$\Gamma_0=I$。逆始终先在整个 $\mathcal H_1$ 上取，再压缩；不是先压 $F_k$ 再求逆。

**定理。** 对全部 $1\le k<M$，在整个 $K_1$ 上严格有
$$
\boxed{
\Gamma_k\Gamma_{k+1}^{-1}\Gamma_k
<
\frac{k+1}{k+2}\,\Gamma_{k-1}.
}
\tag{1.3}
$$
因此常数 $1$ 的弱式也成立。该结论允许 $a,b$ 任意相差很大，不需要二者相等、接近或依序排列。

若等权池的共同权是任意正数 $c$，先把 $D$ 除以 $c$ 即可得到同一结论：$\Gamma_k$ 的公共几何因子 $c^{-2k}$ 在 (1.3) 两侧相同。

本定理的出生层固定为 $s=1$，并且除两个单独的位外，其余位等权。它没有证明任意正异权或任意 $s$ 的相邻 Gram 比较。

### 1.1 整层可逆性，包括最高所需阶

对 $v=\sum_i v_ie_i\in\mathcal H_1$，$(D^*)^kv$ 在每个
$|J|=k+1$ 的坐标上等于
$$
k!\left(\prod_{j\in J}a_j\right)
\sum_{i\in J}\frac{v_i}{a_i},
$$
其中 $a_1=a,a_2=b$，其他 $a_i=1$。
若 $(D^*)^kv=0$，比较相差一个元素的两个 $(k+1)$ 元子集，得到所有
$v_i/a_i$ 相等。因为 $k+1\le M+1<M+2$，这些比较对任意两位都可完成。
再用任一子集的和为零，得到 $v=0$。

所以 $(D^*)^k$ 对 $0\le k\le M$ 单射，$D^k$ 满射到整个
$\mathcal H_1$，从而 (1.2) 的普通逆全部合法。特别，后文比较
$k=M-1$ 时需要的 $F_M^{-1}$ 已经支付。

## 2. 完整 $K_1$ 的两个正交部分

置换等权池的群 $S_M$ 与 $D,D^*,F_k$ 及全部 $F_k^{-1}$ 交换。
在 $\mathcal H_1$ 中，群固定部分由
$$
e_1,\quad e_2,\quad w_1=\sum_{j=3}^{M+2}e_j
$$
张成。弱位零和空间是
$$
K_{\rm st}=
\left\{\sum_{j=3}^{M+2}z_je_j:\ \sum_jz_j=0\right\}.
$$
它已经包含于 $K_1$。固定部分的 primitive 核为二维空间
$$
K_{\rm fix}=
\left\{
f_1e_1+f_2e_2-\frac{af_1+bf_2}{M}w_1:
(f_1,f_2)\in\mathbb C^2
\right\}.
\tag{2.1}
$$
于是
$$
K_1=K_{\rm fix}\oplus^\perp K_{\rm st}.
\tag{2.2}
$$

任何与弱位全部置换交换的矩阵，在弱位块上都有相同对角元与相同非对角元，且两个单独位到弱位的交叉列均为常数列。因此 $K_{\rm st}$ 对 $F_k$、其逆及 $\Gamma_k$ 都约化，且这些算子在该部分为标量。固定部分也约化。这个分解不需要假设 $\Gamma_k$ 在二维部分彼此交换。

### 2.1 零和块的准确标量

令 $D_{\rm w}$ 为池内删除，$L_{\rm w}=D_{\rm w}^*$。
对单位 $\zeta\in K_{\rm st}$，有 $D_{\rm w}\zeta=0$。
等权交换关系
$$
[D_{\rm w},L_{\rm w}]|_{\mathcal H_j^{\rm w}}
=(M-2j)I
$$
逐次给
$$
\|L_{\rm w}^{\,l}\zeta\|^2
=l!\,(M-2)^{\underline l}
\quad(0\le l\le M-2),
\tag{2.3}
$$
而更高次为零。确实，
$$
D_{\rm w}L_{\rm w}^{\,l}\zeta
=l(M-l-1)L_{\rm w}^{\,l-1}\zeta,
$$
取内积并归纳即得 (2.3)。

展开 $(D^*)^k\zeta$，两个单独位各只能被加入一次。
不同单独位占据集合严格正交，故
$$
\frac{\|(D^*)^k\zeta\|^2}{(k!)^2}
=e_k\bigl(a^2,b^2,\underbrace{1,\ldots,1}_{M-2}\bigr).
\tag{2.4}
$$
由上面的标量约化，$\Gamma_k$ 在 $K_{\rm st}$ 上正是右侧的倒数。
这里有效权的总数为 $M$，所以 $0\le k\le M$ 均合法。

为完整核相邻常数，令这些有效正权平方的初等对称和为 $e_j$。
多项式
$$
P(t)=\prod_{\nu=1}^{M}(1+z_\nu t)
$$
全部根为负实数。对 $1\le k<M$，$Q=P^{(k-1)}$ 的根仍全为负实数，由 Rolle 定理逐次得到。
因而
$$
Q'(0)^2-Q(0)Q''(0)>0.
$$
将导数的常数项代入，得到
$$
\frac{e_{k-1}e_{k+1}}{e_k^2}<\frac{k}{k+1}
<\frac{k+1}{k+2}.
\tag{2.5}
$$
故 (1.3) 已在完整 $K_{\rm st}$ 上成立。余下只须支付二维
$K_{\rm fix}$。

## 3. 二维源基中的完整最小逆

令
$$
Zf=f_1e_1+f_2e_2-\frac{af_1+bf_2}{M}w_1.
$$
这不是正交归一基。源基的 Gram 为
$$
H_0=Z^*Z
=
\begin{pmatrix}
1+a^2/M&ab/M\\
ab/M&1+b^2/M
\end{pmatrix}.
\tag{3.1}
$$
定义各阶的 Gram **form**
$$
H_k=Z^*F_k^{-1}Z.
\tag{3.2}
$$
若 $J_kZf$ 是 $D^ku=Zf$ 的全空间最小解，则
$$
f^*H_kf=(k!)^2\|J_kZf\|^2.
\tag{3.3}
$$
因此可直接求解 $(D^k/k!)u=Zf$ 的最小范数。

### 3.1 原空间中的最小性

$D^k$ 将孔数准确降低 $k$；任意全空间解在 $\mathcal H_{k+1}$ 外的分量只落入正交输出层或核，取最小范数时可删除。因此只须在 $\mathcal H_{k+1}$ 中求解，再作下面的群平均。

等权池置换群的正交平均与 $D^k$ 交换。对固定源 $Zf$，平均一个任意解仍是解，且范数不增加。最小解唯一，所以它本身固定。
因此以下在固定空间中的最小化，给的是整个实际布尔空间中的 Moore–Penrose 解，而不是人为限制后的较大成本。

记
$$
w_j=\sum_{\substack{I\subset\{3,\ldots,M+2\}\\|I|=j}}e_I,
\qquad \|w_j\|^2=\binom Mj.
$$
对 $1\le k<M$，第 $k+1$ 孔层的固定向量写成
$$
u=u_0w_{k+1}+u_1e_1w_k+u_2e_2w_k+u_{12}e_{12}w_{k-1}.
$$
令
$$
C_k=\binom Mk,\qquad
\tau=\frac{k}{M-k+1},\qquad
\eta=\frac{k+1}{M-k}.
$$
方程 $(D^k/k!)u=Zf$ 的两个单独位输出及弱位输出分别为
$$
C_ku_1+b\binom M{k-1}u_{12}=f_1,
\qquad
C_ku_2+a\binom M{k-1}u_{12}=f_2,
$$
$$
\binom{M-1}{k}u_0+
a\binom{M-1}{k-1}u_1+
b\binom{M-1}{k-1}u_2+
ab\binom{M-1}{k-2}u_{12}
=-\frac{af_1+bf_2}{M}.
\tag{3.4}
$$
无效的二项式为零。

以 $y=C_ku_{12}$ 为唯一自由参数，(3.4) 准确解成
$$
u_1=C_k^{-1}(f_1-b\tau y),\qquad
u_2=C_k^{-1}(f_2-a\tau y),
$$
$$
u_0=C_k^{-1}\eta[-(af_1+bf_2)+ab\tau y].
$$
代入正交范数，得到完整变分式
$$
\boxed{
f^*H_kf=\frac1{C_k}\min_{y\in\mathbb C}
\left\{
\eta|af_1+bf_2-ab\tau y|^2+
|f_1-b\tau y|^2+
|f_2-a\tau y|^2+\tau|y|^2
\right\}.
}
\tag{3.5}
$$
所有变量与输出约束均保留。对一个复变量完成平方即给下一节的矩阵公式。

### 3.2 最高端点 $k=M$

此时 $w_{M+1}$ 不存在，不能直接使用 (3.5) 中的无限大 $\eta$。
直接解 (3.4) 的三个剩余未知量，得到
$$
u_1=-\frac ba f_2,\qquad
u_2=-\frac ab f_1,\qquad
u_{12}=\frac{af_1+bf_2}{Mab}.
$$
这三个固定空间方程唯一确定此解，所以它也是完整最小解。其范数为
$$
\left|\frac ba f_2\right|^2+
\left|\frac ab f_1\right|^2+
\frac{|af_1+bf_2|^2}{Ma^2b^2}.
\tag{3.6}
$$
这将给 $H_M$ 的准确有限值，不使用奇异参数的未付极限。

## 4. 统一矩阵公式与算子序的同余

置
$$
A=a^2,\qquad B=b^2,\qquad d=M-k,
$$
并定义
$$
N_k=
\begin{pmatrix}
(d+(k+1)A)(d+1+kA)&ab(M+1)\\
ab(M+1)&(d+(k+1)B)(d+1+kB)
\end{pmatrix},
$$
$$
D_k=d(d+1)+kd(A+B)+k(k+1)AB,
$$
$$
E_k=d(d+1)+(k+1)(d+1)(A+B)+k(k+1)AB.
\tag{4.1}
$$
这里 $D_k,E_k$ 是正标量，不是删除算子。

(3.5) 的完成平方给
$$
\boxed{
H_k=\frac1{\binom Mk}\frac{N_k}{D_k},
\qquad 0\le k\le M.
}
\tag{4.2}
$$
$k=0$ 由 (3.1) 直接核；$k=M$ 由 (3.6) 直接核。
所以 (4.2) 的端点没有遗漏。

展开 $2\times2$ 行列式，准确有
$$
\boxed{\det N_k=D_kE_k.}
\tag{4.3}
$$
于是若 $R_k=N_k/D_k$，
$$
R_k^{-1}=\frac{\operatorname{adj}N_k}{E_k}.
\tag{4.4}
$$
全部所需 $D_k,E_k$ 都严格正，包括 $k=M$。

### 4.1 非正交源基中的顺序

$\Gamma_k|_{K_{\rm fix}}$ 在源基 $Z$ 下的**算子坐标矩阵**是
$$
H_0^{-1}H_k,
$$
而不是 $H_k$ 本身。因此原算子序 (1.3) 与
$$
\boxed{
H_kH_{k+1}^{-1}H_k
<
\frac{k+1}{k+2}H_{k-1}
}
\tag{4.5}
$$
同余等价：将原差的二次型作用于 $Zf$，$H_0$ 因子按真实逆的顺序消去，得到 (4.5) 的二次型。这里没有将 $\Gamma_k$ 假设为彼此交换。

由
$$
\frac{\binom Mk^2}
{\binom M{k-1}\binom M{k+1}}
=\frac{(k+1)(d+1)}{kd},
$$
(4.2) 又使 (4.5) 等价于
$$
\frac{(k+1)^2(d+1)}{k(k+2)d}R_{k-1}
-R_kR_{k+1}^{-1}R_k>0.
\tag{4.6}
$$
以下对全部整数 $k,d\ge1$ 同时证明 (4.6)。

## 5. 通用整数多项式正性证书

记
$$
K_{\rm num}=(k+1)^2(d+1),\qquad
K_{\rm den}=k(k+2)d.
$$
在 $N_{k-1},D_{k-1}$ 中同时把 $(k,d)$ 换成 $(k-1,d+1)$；
在 $N_{k+1},E_{k+1}$ 中同时换成 $(k+1,d-1)$，从而总数 $M=k+d$ 始终固定。

将 (4.6) 乘以严格正的公共分母
$$
K_{\rm den}D_{k-1}E_{k+1}D_k^2,
$$
得到对称矩阵多项式
$$
\boxed{
\Delta=
K_{\rm num}E_{k+1}D_k^2N_{k-1}
-K_{\rm den}D_{k-1}
N_k(\operatorname{adj}N_{k+1})N_k.
}
\tag{5.1}
$$

**系数引理。** 在整数多项式环
$$
\mathbb Z[a,b,x,y],\qquad k=1+x,\quad d=1+y,
$$
中准确有：

- $\Delta_{11}$ 的全部非零系数严格为正，共 $831$ 项；
- $\Delta_{22}$ 的全部非零系数严格为正，共 $831$ 项；
- $\det\Delta$ 的全部非零系数严格为正，共 $9826$ 项。

并且 $x,y$ 零次的系数中包括
$$
\Delta_{11}\ \supset\ 576a^2+360b^2,
$$
$$
\det\Delta\ \supset\ 207360(a^2+b^2)^2.
\tag{5.2}
$$
这里“包括”表示减去所列多项式后仍全部系数非负。没有断言
$\Delta_{12}$ 的系数非负；其若干系数确实为负，也不需要这一额外性质。

### 5.1 完整证书及验证方式

[通用 BigInt 符号证书](../notes/2026-11-13-two-exceptional-weights-birth-one-primitive-gram-upper-bound-central-review.mjs)
是本系数引理的完整有限证明证书。它不代入任何具体正权或任何高度样本。它直接执行以下整数多项式恒等运算：

1. 按 (4.1) 生成三组 $(N,D,E)$，并逐个检查
   $\det N-DE$ 的每个系数为零；
2. 用普通 $2\times2$ 矩阵乘法生成 (5.1)，并检查
   $\Delta_{12}-\Delta_{21}$ 恒为零；
3. 展开 $\Delta_{11},\Delta_{22},\det\Delta$，逐一检查全部非零整数系数的符号；
4. 独立检查 (5.2) 的五个明确系数，以及上述三项支持大小。

多项式由稀疏单项表表示。系数始终为任意精度 BigInt；
单项相乘只把四个非负整数指数相加。指数编码底数为 $64$，
每次乘法都传播次数上界，并在任何指数可能达到 $64$ 时立即拒绝。
所有实际指数均在界内，因此编码不会把两个不同单项混同。编码整数小于 $64^4$，其整数加法也完全精确。

该文件可以作为独立 JavaScript 文件执行。作者与根代理分别执行其完整 V8 运算，均得到上述恒等式与系数检查的 PASS。没有以浮点特征值、参数抽样或有限样例代替通用符号断言。

由 $a,b>0$、$x,y\ge0$ 和 (5.2)，
$$
\Delta_{11}>0,\qquad \det\Delta>0.
$$
$2\times2$ Hermitian 矩阵的 Sylvester 判据遂给 $\Delta>0$。
公共分母严格正，故 (4.6)、(4.5) 及 (1.3) 在完整
$K_{\rm fix}$ 上成立。与 §2 的 $K_{\rm st}$ 结论合并，定理得证。

## 6. 这确实包含非交换的 primitive Gram

取
$$
M=5,\qquad a=2,\qquad b=3.
$$
在 (2.1) 的源基中，公式给
$$
H_0=
\begin{pmatrix}9/5&6/5\\6/5&14/5\end{pmatrix},
\quad
H_1=
\begin{pmatrix}3/20&1/20\\1/20&77/180\end{pmatrix},
\quad
H_2=
\begin{pmatrix}1/17&1/85\\1/85&11/51\end{pmatrix}.
$$
因此 $\Gamma_1,\Gamma_2$ 的实际坐标矩阵分别是
$$
H_0^{-1}H_1=
\begin{pmatrix}1/10&-14/135\\-1/40&71/360\end{pmatrix},
$$
$$
H_0^{-1}H_2=
\begin{pmatrix}32/765&-16/255\\-7/510&53/510\end{pmatrix}.
$$
其交换子的左上角准确为
$$
-\frac1{6885}\ne0.
$$
所以本定理没有将问题降成一条共同本征线，也没有由逐向量标量比值替代非交换算子序。

## 7. 与一般问题的边界

本结果证明了一个完整 primitive 空间上的真正上界，覆盖任意两个独立正异权及任意大小的等权池，且包括全部合法相邻高度。它与此前饱和两簇固定线的正矩证明不同：这里的主要二维块通常不交换，所用证书只证明所需的相邻序。

下一节将本模型补到全部出生层；任意三个以上独立异权或原连续尾上的
$$
\Gamma_k\Gamma_{k+1}^{-1}\Gamma_k
\le\frac{s+k}{s+k+1}\Gamma_{k-1},
$$
也没有据此支付原边界的窄 Schur 返回费。等权池的数目可任意取，但没有从这一有限模型的结论免费推出未知无限限制的最小逆收敛。

本稿同样不恢复已被反例否定的有限维强化因子，也不主张任何完整高阶 Hankel 正性或一般正算子值矩表示。


## 8. 任意独立头权的饱和 primitive 固定线

本节先证明一个独立的正面范围：有限多个头位的权可以全部不同。后面只用它的两个头位情形完成同一模型的全部出生层。

取 $q\ge1$ 个头位，权为
$$
a_1,\ldots,a_q>0,
$$
另取 $L\ge q$ 个等权为 $1$ 的池位。令
$$
D=D_{\rm h}+D_{\rm w},\qquad
D_{\rm h}=\sum_{i=1}^q a_iE_i.
$$
对头集合 $F\subseteq\{1,\ldots,q\}$，写
$$
R=F^{\rm c},\qquad r=|R|,\qquad a_R=\prod_{i\in R}a_i.
$$
池内未归一对称向量为
$$
w_l=\sum_{|J|=l}e_J,\qquad \|w_l\|^2=\binom Ll.
$$

### 8.1 primitive 源与完整最小解

在第 $q$ 孔层的池置换固定空间中，定义
$$
g=
\sum_{F\subseteq[q]}
(-1)^r\frac{r!\,a_R}{L^{\underline r}}\ e_Fw_r.
\tag{8.1}
$$
空乘积为 $1$。直接删除一位：固定输出头集合 $F$、池孔数 $r-1$，池删除的系数为
$$
(L-r+1)(-1)^r\frac{r!a_R}{L^{\underline r}},
$$
来自 $F\cup\{i\}$ 的头删除系数之和为
$$
\sum_{i\in R}
a_i(-1)^{r-1}
\frac{(r-1)!a_{R\setminus\{i\}}}{L^{\underline{r-1}}}.
$$
两者恰好相消。因此 $Dg=0$。

该固定 primitive 空间恰为一维。源层的固定空间以全部 $e_Fw_r$ 为基，维数为 $2^q$；下降到第 $q-1$ 层时只缺少 $F=[q]$ 这一种头集合。按头集合大小反向消元，池删除的系数非零，所有其他系数都被最高头系数唯一决定，正是 (8.1)。

记
$$
Z=\|g\|^2
=\sum_{r=0}^q
\frac{r!\,e_r(a_1^2,\ldots,a_q^2)}
{L^{\underline r}}>0,
\qquad \widehat g=g/\sqrt Z.
\tag{8.2}
$$
对 $0\le k\le L-q$，定义第 $q+k$ 孔层的固定向量
$$
v_k=
\sum_{F\subseteq[q]}
(-1)^r
\frac{(k+r)!\,a_R}
{L^{\underline{k+r}}}\ e_Fw_{k+r}.
\tag{8.3}
$$
准确有
$$
\boxed{\frac{D^k}{k!}v_k=g.}
\tag{8.4}
$$

给出完整有限核验。读输出 $e_Fw_r$，将初始头的补集记为
$T\subseteq R$，$|T|=\ell$。删去头集合 $R\setminus T$ 后，所有头权合并为 $a_R$。弱池二项系数与 (8.3) 中的阶乘相消，得到输出系数
$$
\frac{a_R}{L^{\underline r}}
\sum_{\ell=0}^r
(-1)^\ell\binom r\ell
(k+\ell)^{\underline r}.
$$
当 $k+\ell<r$ 时下降阶乘为零，准确对应不合法的删除项。
因为 $(k+x)^{\underline r}$ 是首一 $r$ 次多项式，其 $r$ 阶有限差分给
$$
\sum_{\ell=0}^r
(-1)^\ell\binom r\ell
(k+\ell)^{\underline r}=(-1)^r r!.
$$
这正是 (8.1) 的系数，证明 (8.4)，包括 $k=0$。

这些解还是整个布尔空间中的真实最小解。第 $q+k$ 层及第 $q$ 层的池固定空间都以全部头集合为索引，维数相同；$D^k/k!$ 在其中是三角矩阵，其对角系数为
$$
\binom{L-r}{k}>0.
$$
所以固定空间中的解唯一。对完整核向量作池置换平均，所得固定核向量必为零；而 $v_k$ 固定，故它正交于完整核。按孔层正交分解也可先删去其他输出层的无用分量。因此 $v_k/\sqrt Z$ 是 $(D^k/k!)u=\widehat g$ 的全 Hilbert 空间最小解。

在合法范围内，整层 $D^k:\mathcal H_{q+k}\to\mathcal H_q$ 满射，可用 §9.1 的有限 Lefschetz 分解与正权对角相似核验；这也正是既有 R271 全阶最小逆稿 §6.1 的范围。故若按标准顺序定义
$$
F_k=\frac{D^k(D^*)^k}{(k!)^2},\qquad
\Gamma_k=P_{\ker D\cap\mathcal H_q}F_k^{-1}
\big|_{\ker D\cap\mathcal H_q},
$$
$\Gamma_k$ 保持上述固定一维线。其本征值准确为
$$
\boxed{
\gamma_k
=\frac{\|v_k\|^2}{Z}
=\frac1Z\sum_{r=0}^q
\frac{(k+r)!\,e_r(a_1^2,\ldots,a_q^2)}
{L^{\underline{k+r}}}.
}
\tag{8.5}
$$
这来自 (8.3) 中各头集合和池占据向量的正交性，不是一个试探解上界。

### 8.2 与高度无关的正概率矩表示

令
$$
p_r=\frac{r!\,e_r(a_1^2,\ldots,a_q^2)}
{ZL^{\underline r}},
\qquad \sum_{r=0}^qp_r=1.
$$
将 (8.5) 写为
$$
\gamma_k=\sum_{r=0}^q p_r
\frac{(r+1)^{\overline k}}
{(L-r)^{\underline k}}.
\tag{8.6}
$$
条件于 $r$，取独立随机变量：

- 若 $r<q$，$U_r$ 的分布为 $\operatorname{Beta}(r+1,q-r)$；
- 若 $r=q$，令 $U_q=1$；
- $V_r$ 的分布为形状 $L-r+1$、率 $1$ 的 Gamma 分布。

其准确矩为
$$
\mathbb E U_r^k
=\frac{(r+1)^{\overline k}}{(q+1)^{\overline k}},
\qquad
\mathbb E V_r^{-k}
=\frac1{(L-r)^{\underline k}}.
$$
后式使用 $k<L-r+1$，由 $k\le L-q$ 统一保证。
因此
$$
\boxed{
\frac{q!\gamma_k}{(q+k)!}
=\sum_{r=0}^q p_r\mathbb E(U_r/V_r)^k,
\qquad 0\le k\le L-q.
}
\tag{8.7}
$$
这是一个固定概率测度的矩。$p_q>0$，且 $V_q^{-1}$ 在正半轴有正密度，所以所有合法有限 Hankel 块严格正定。特别
$$
\boxed{
\gamma_k^2<
\frac{q+k}{q+k+1}\gamma_{k-1}\gamma_{k+1},
\qquad 1\le k<L-q.
}
\tag{8.8}
$$

这个结论允许任意多个独立头权，但仍只限于头完全饱和的池固定 primitive 一维线。它不把多维 primitive Gram 同时对角化，也不恢复一般全 Hankel 正性。

## 9. 两个独立异权位在全部出生层的完整上界

回到前文的固定算子
$$
D=aE_1+bE_2+\sum_{j=3}^{M+2}E_j,\qquad M\ge2.
$$
现在允许任意出生层 $s\ge0$。令 $N=M+2$，
$$
K_s=\ker D\cap\mathcal H_s,
\qquad
F_k^{(s)}=\frac{D^k(D^*)^k|_{\mathcal H_s}}{(k!)^2},
\qquad
\Gamma_k^{(s)}
=P_{K_s}(F_k^{(s)})^{-1}|_{K_s}.
\tag{9.1}
$$
凡是 $0\le k\le N-2s$，整层逆均合法。

**全出生定理。** 对全部整数
$$
s\ge0,\qquad 1\le k<N-2s,
$$
在整个 $K_s$ 上严格有
$$
\boxed{
\Gamma_k^{(s)}(\Gamma_{k+1}^{(s)})^{-1}\Gamma_k^{(s)}
<
\frac{s+k}{s+k+1}\Gamma_{k-1}^{(s)}.
}
\tag{9.2}
$$
因此同一模型的常数 $1$ 弱式也在全部合法出生层成立。

### 9.1 等权池的完整正交串分解

为明确全部来源，回顾有限等权删除 $D_{\rm w}$、上升
$L_{\rm w}=D_{\rm w}^*$。在池的第 $j$ 层，
$$
[D_{\rm w},L_{\rm w}]=(M-2j)I.
$$
取任意单位 primitive 向量
$$
\zeta\in\ker D_{\rm w}\cap\mathcal H_j^{\rm w},
\qquad 0\le j\le\lfloor M/2\rfloor.
$$
置
$$
L=M-2j,\qquad
\zeta_l=
\frac{L_{\rm w}^{\,l}\zeta}
{\sqrt{l!\,L^{\underline l}}},
\qquad 0\le l\le L.
$$
直接归纳得到
$$
D_{\rm w}\zeta_l=\sqrt{l(L-l+1)}\,\zeta_{l-1},
\qquad
D_{\rm w}^*\zeta_l=\sqrt{(l+1)(L-l)}\,\zeta_{l+1},
\tag{9.3}
$$
两端越界项为零。因此每条串都同时约化 $D_{\rm w}$ 和其伴随。

不同 primitive 基向量产生的串相互正交。同一出生层用反复移伴随即可；对不同出生层，将多余的上升移回后，较高出生的 primitive 向量正交于一个真实上升像。

这些串穷尽整个弱池 Hilbert 空间。一个自含维数核验是：
当 $j<M/2$，
$$
\|L_{\rm w}v\|^2-\|D_{\rm w}v\|^2
=(M-2j)\|v\|^2
$$
使 $L_{\rm w}$ 在第 $j$ 层单射；故低半层的 primitive 维数为
$\binom Mj-\binom M{j-1}$。在任意第 $p$ 层，能到达该层的串恰有
$j\le\min(p,M-p)$，其维数求和望远镜为
$\binom Mp$。因此正交串的总维数准确等于全空间。

同一论证对任意有限等权总位数成立。再对正异权用
$$
R_pe_I=\left(\prod_{i\in I}a_i\right)e_I,\qquad
D(a)^k=R_s^{-1}D(1)^kR_{s+k},
$$
保持有限秩，就得到 (9.1) 所用的整层满射范围
$k\le N-2s$。这里不把对角相似误写成酉相似；它只用于秩。

### 9.2 每条弱串上的真实约化

将一条弱串与两个头位张量。它同时约化完整 $D$、$D^*$，
也保持孔层，所以 $F_k^{(s)}$、其完整逆及 primitive 压缩都按这些串分块。没有把全空间逆换成事后压缩的逆。

由 (9.3)，这条串酉等价于 $L=M-2j$ 个等权位的对称部分。
在原第 $s$ 出生层上，对应的相对出生层是
$$
t=s-j.
$$
因此每条约化块是“两个独立权 $a,b$ 加上 $L$ 位等权对称池”的相对第 $t$ 层。

固定一个 (9.2) 的合法比较，并记
$$
h=N-2s\ge2.
$$
对任何出现的串，有准确恒等式
$$
L+2-2t=h.
\tag{9.4}
$$
若 $t<0$，该串没有目标向量。若 $t\ge3$，(9.4) 给
$L\ge2t$。相对第 $t$ 层和第 $t-1$ 层都以四个头集合为索引，池孔数分别为 $t-|F|$ 和 $t-1-|F|$。
删除矩阵按头集合大小是三角的；全部池删除对角系数
$$
L-t+|F|+1
$$
严格为正。因此它可逆，primitive 核为零。

所以非零 primitive 块只可能有
$$
t=0,\quad t=1,\quad t=2.
$$
现在逐块支付：

**相对出生 $t=0$。** 这是一个真空标量源，
$$
F_k=e_k(a^2,b^2,\underbrace{1,\ldots,1}_{L}).
$$
有效总位数为 $L+2=h$，$k+1\le h$。前文的标量 Newton 证明给邻比严格小于 $k/(k+1)$，因而不超过
$(s+k)/(s+k+1)$。

**相对出生 $t=1$。** (9.4) 给 $L=h\ge2$。该块正是前文 §3–5 已付的二维池固定 primitive 空间。其邻比满足系数
$(k+1)/(k+2)$；由于 $s=j+1\ge1$，
$$
\frac{k+1}{k+2}\le\frac{s+k}{s+k+1}.
$$
所有所需阶都在 $k+1\le L$ 的范围内，包含已经直接核过的最高逆。

**相对出生 $t=2$。** (9.4) 给 $L=h+2\ge4$。这是 §8 中
$q=2$、任意两个独立头权的饱和一维源。由 $k+1\le h=L-2$，
(8.8) 适用，给系数 $(k+2)/(k+3)$。又 $s=j+2\ge2$，所以
$$
\frac{k+2}{k+3}\le\frac{s+k}{s+k+1}.
$$

所有约化 primitive 块都已支付 (9.2)。它们的正交直和就是完整
$K_s$，因此得到整空间算子序，而不是某些试探源上的标量上界。

### 9.3 短串与端点没有被删除

上面的合法范围已经包含短串：若 $L=0$ 或 $L=1$，(9.4) 与
$h\ge2$ 迫 $t=0$，所以它们仅进入两个或三个有效位的真空 Newton 块。并未把它们免费套入要求池大小至少 $2$ 的二维证明。

相对出生 $1$ 的块自动有 $L\ge2$；相对出生 $2$ 的块自动有
$L\ge4$。最高所需阶分别由前文直接的 $k=L$ 逆，以及 §8 的
$k=L-2$ 明确有限阶乘公式支付。零阶是各真实源空间的恒等，已包含在所有 Gram 公式中。

## 10. 全出生加强后的范围

本节将同一个“两独立异权位加等权池”算子的结论，从出生 $1$ 扩大到全部合法出生层。它同时保留 §8 的任意多个独立头权、饱和固定一维源的正矩公式。两者均使用实际全空间最小逆及完整 primitive 压缩。

一般任意正异权布尔模型、三个以上独立异权位在任意出生层的非交换 primitive 比较，以及原连续尾的窄 Schur 返回费用，仍没有由这些结论完成。等权池的正交串分解是本证明使用的具体结构，不能把不等权背景直接替换成它。
