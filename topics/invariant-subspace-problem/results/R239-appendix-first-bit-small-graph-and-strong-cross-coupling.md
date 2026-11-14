# R239 附录：实际边界核的首位小图与强跨块耦合

日期：2026-11-12（UTC）。作者：boundary_next；二阶压缩范数引理由 root 提供。状态：已证明，中间结论。

本稿对实际 $T_N,T_Y$ 的整个核给统一的首位小图，保留所有进位和 Cayley 逆。图算子的核内范数小于 $1/\sqrt{12}$，所以核向量的首位占满质量小于 $1/13$。这还给出限制 $B|_M$ 与环境 $B^*|_M$ 的显著范数分离，以及真正缺陷向量的一条压缩伴随方程。它没有证明 $N=M$。

## 1. 对象与准确首位矩阵

沿用实际负整数边界
$$
B e_n=\alpha_{v_2(n)}e_{n-1},\qquad B e_0=0,\qquad
N_j=B^{2^j}/d_j,\qquad Y_j=N_j(I+N_j)^{-1}.
$$
令
$$
a_j=(j+1)^{-2},\qquad
T_N=\sum_{j\ge0}a_jN_j,\qquad T_Y=\sum_{j\ge0}a_jY_j.
$$
两者分别取
$$
M=\ker T,\qquad N=\overline{BM},\qquad D=M\ominus N.
$$
实际权满足
$$
\alpha_0=e^{-20},\qquad
\eta_j=\alpha_{j+1}/\alpha_j,\qquad
-\log\eta_j=1400\,16^j-630\,8^j+300\,2^j.
$$
特别
$$
\eta:=\eta_0=e^{-1070},\qquad
\eta_1=e^{-17960}\le\eta^2.
\tag{1.1}
$$

按最低物理位把空间写成
$$
\mathcal H_-=\mathcal H_{\rm tail}\oplus\mathcal H_{\rm tail},
\qquad e_{2n}\leftrightarrow(e_n,0),\quad
e_{2n+1}\leftrightarrow(0,e_n).
$$
第一个分量是该位真空，第二个分量是该位占满。
所有 $N_j,Y_j$（$j\ge1$）都在这两个分量上作用为同一个尾算子。
以下在尾空间沿用其名字，并置
$$
Z=N_1|_{\mathcal H_{\rm tail}},\qquad R=\eta Z.
$$
有 $\|Z\|=1$，而实际二进位后移准确给
$$
\boxed{
N_0=
\begin{pmatrix}0&I\\R&0\end{pmatrix},
\qquad
B=\alpha_0
\begin{pmatrix}0&I\\R&0\end{pmatrix}.
}
\tag{1.2}
$$
所有尾 $N_j,Y_j$ 与 $Z$ 交换。

分别记
$$
S_N=\sum_{j\ge1}a_jN_j,\qquad
S_Y=\sum_{j\ge1}a_jY_j
$$
为尾算子，定义
$$
\boxed{
H_N=S_N,\qquad H_Y=(I-R)S_Y-R.
}
\tag{1.3}
$$
每个 $H$ 都与 $Z$ 交换。对 $N$ 模型，直接有
$$
T_N=\begin{pmatrix}H_N&I\\R&H_N\end{pmatrix}.
\tag{1.4}
$$

对 $Y$ 模型，必须保留真实逆。由 $N_0^2=R I_2$ 和
$\|R\|=\eta<1$，
$$
(I+N_0)^{-1}=(I-N_0)(I-R)^{-1},
$$
从而
$$
Y_0=(N_0-RI_2)(I-R)^{-1}.
$$
因此用可逆的对角尾算子左乘 $T_Y$，准确得到
$$
\boxed{
\begin{pmatrix}I-R&0\\0&I-R\end{pmatrix}T_Y
=
\begin{pmatrix}H_Y&I\\R&H_Y\end{pmatrix}.
}
\tag{1.5}
$$
它不改变核；没有将 $Y_0$ 替换成 $N_0$。

## 2. 真实核的小图与移位交织

以下 $H$ 分别取 (1.3) 中相应的一个。令
$$
L=\ker(H^2-R)\subseteq\mathcal H_{\rm tail}.
$$
这是闭子空间；因 $H,Z$ 交换，两者都保持 $L$。
由 (1.4)、(1.5) 的第一行消去第二分量，得到
$$
\boxed{
M=\{Jx:x\in L\},\qquad Jx=(x,-Hx).
}
\tag{2.1}
$$
$J:L\to M$ 有界、满射、单射，逆就是第一坐标投影。
特别，本式是整个实际核的描述，不仅适用于某一组构造向量。

置
$$
C=H|_L,\qquad Z_L=Z|_L.
$$
则
$$
\boxed{C^2=\eta Z_L,\qquad \|Z_L\|\le1.}
\tag{2.2}
$$
利用 (2.2) 和真正的矩阵 (1.2)，有
$$
BJx=\alpha_0(-Hx,Rx)=J(-\alpha_0 Cx).
$$
即
$$
\boxed{B|_M\,J=-\alpha_0 JC.}
\tag{2.3}
$$
图度量是
$$
\langle Jx,Jy\rangle=\langle Gx,y\rangle,\qquad
G=I_L+C^*C.
\tag{2.4}
$$
这里 $C^*=P_LH^*|_L$ 是压缩后的通常伴随；不能把它换成整个尾空间的 $H^*$。

## 3. 二阶近幂零与自交换子的范数引理

**引理。** 设 $A$ 为 Hilbert 空间上的有界算子，
$$
c\ge\|A^*A-AA^*\|.
$$
对 $x\ne0$ 记
$$
t=\frac{\|Ax\|^2}{\|x\|^2},\qquad
e=\frac{\|A^2x\|}{\|x\|}.
$$
则
$$
\boxed{
t^2\le e^2+ct,\qquad
t\le\frac{c+\sqrt{c^2+4e^2}}2.
}
\tag{3.1}
$$

证明。Cauchy–Schwarz 给
$$
\|Ax\|^4\le\|A^*Ax\|^2\|x\|^2.
$$
再把 $A^*A-AA^*$ 的范数界用于向量 $Ax$，得
$$
\|A^*Ax\|^2\le\|A^2x\|^2+c\|Ax\|^2.
$$
除以 $\|x\|^4$，得到二次不等式；取非负根即得 (3.1)。

该引理可用环境 $H$ 的自交换子估计 $C=H|_L$ 的范数：
对 $x\in L$，有 $\|H^2x\|\le\eta\|x\|$，故
$$
\boxed{
\|C\|^2\le
\frac{c+\sqrt{c^2+4\eta^2}}2
\quad\text{只要 }c\ge\|H^*H-HH^*\|.
}
\tag{3.2}
$$
这一步没有把环境自交换子误认为压缩自交换子。

## 4. 两个模型的全部真实误差

在尾空间令
$$
A_{\rm pure}=\sum_{j\ge1}a_j E_j,\qquad
t_1=\sum_{j\ge1}a_j,\qquad
s_1=\sum_{j\ge1}a_j^2.
$$
所有 $E_j$ 是边界纯孔消灭矩阵。其精确交换子为
$$
A_{\rm pure}^*A_{\rm pure}-A_{\rm pure}A_{\rm pure}^*
=\sum_{j\ge1}a_j^2(2P_j-I),
$$
所以
$$
\|A_{\rm pure}\|\le t_1,\qquad
\|A_{\rm pure}^*A_{\rm pure}-A_{\rm pure}A_{\rm pure}^*\|\le s_1.
\tag{4.1}
$$
只需这个上界，无须使用任何纯模型核结论。

实际进位及 Cayley 逆比较给
$$
\|N_j-E_j\|\le\eta_j,\qquad
\|Y_j-E_j\|\le4\eta_j.
\tag{4.2}
$$
于是
$$
\|S_N-A_{\rm pure}\|\le t_1\eta_1,\qquad
\|S_Y-A_{\rm pure}\|\le4t_1\eta_1.
\tag{4.3}
$$
由 (1.3)，两个 $H$ 统一满足
$$
\|H-A_{\rm pure}\|\le
\rho:=4t_1\eta_1+\eta(1+t_1+4t_1\eta_1).
\tag{4.4}
$$
这已包含 $Y$ 模型首位逆产生的全部 $R(S_Y+I)$，没有漏掉低位固定误差。

下述简单数值都可由有限和与积分比较支付：
$$
t_1=\sum_{n\ge2}n^{-2}
\le\sum_{n=2}^5n^{-2}+\int_5^\infty x^{-2}\,dx
<\frac23,
\tag{4.5}
$$
$$
s_1=\sum_{n\ge2}n^{-4}
\le\sum_{n=2}^5n^{-4}+\int_5^\infty x^{-4}\,dx
=\frac{1075921}{12960000}<\frac1{12}.
\tag{4.6}
$$
由 $\eta_1\le\eta^2$ 及 $\eta=e^{-1070}<10^{-6}$，(4.4) 给
$$
\boxed{\rho\le2\eta.}
\tag{4.7}
$$

写 $H=A_{\rm pure}+E$，$\|E\|\le\rho$。展开两项自交换子，
四个交叉项与两个二次项分别给
$$
\begin{aligned}
\|H^*H-HH^*\|
&\le s_1+4t_1\rho+2\rho^2\\
&\le s_1+\frac{16}{3}\eta+8\eta^2=:c_1.
\end{aligned}
\tag{4.8}
$$
这是真实 $H_N,H_Y$ 的统一上界。

在 (3.2) 取 $c=c_1$，记
$$
r^2=\frac{c_1+\sqrt{c_1^2+4\eta^2}}2.
$$
由于 $r^2\le c_1+\eta$，
$$
r^2\le s_1+\frac{19}{3}\eta+8\eta^2<\frac1{12}.
\tag{4.9}
$$
最后严格不等式的余量可直接核算：
$$
\frac1{12}-\frac{1075921}{12960000}
=\frac{4079}{12960000}>
\frac{19}{3\cdot10^6}+\frac8{10^{12}}.
$$
因此两个模型都得到
$$
\boxed{\|C\|\le r<\frac1{\sqrt{12}}.}
\tag{4.10}
$$
若使用精确级数 $s_1=\sum_{n\ge2}n^{-4}$，则 $r$ 约为 $0.28693$；
所有真实误差仍以 (4.8) 明确保留。

## 5. 首位质量、限制范数与环境伴随的分离

令 $P_{\rm occ}$ 为最低物理位占满的正交投影。
对 $w=Jx\in M$，(4.10) 给
$$
\boxed{
\|P_{\rm occ}w\|^2
=\|Cx\|^2
\le\frac{r^2}{1+r^2}\|w\|^2
<\frac1{13}\|w\|^2.
}
\tag{5.1}
$$
同时
$$
\|x\|^2\le\|Jx\|^2\le(1+r^2)\|x\|^2.
\tag{5.2}
$$
所以首位图参数化的条件数至多
$\sqrt{1+r^2}<\sqrt{13/12}$。
这里仅是首位图，不是把全部实际有限头化为单 Jordan 链的相似；不与 R249C 的大成本下界冲突。

记 $K=B|_M$。因为 $C$ 保 $L$，
$$
\|JCx\|^2=\|Cx\|^2+\|C^2x\|^2
\le r^2(\|x\|^2+\|Cx\|^2).
$$
结合 (2.3)，得
$$
\boxed{\|K\|\le\alpha_0r<\frac{\alpha_0}{\sqrt{12}}.}
\tag{5.3}
$$

另一方面，由 (1.2)
$$
B^*Jx=\alpha_0(-R^*Hx,x),
$$
所以
$$
\|B^*Jx\|^2\ge\alpha_0^2\|x\|^2.
$$
由 (5.2) 得到整个核上的环境下界
$$
\boxed{
\|B^*w\|\ge
\frac{\alpha_0}{\sqrt{1+r^2}}\|w\|
>\alpha_0\sqrt{\frac{12}{13}}\|w\|
\qquad(0\ne w\in M).
}
\tag{5.4}
$$
该下界远强于通过大前缀得到的粗下界，但方向仍是环境 $M\to\mathcal H_-$，不是 $K^*$ 的下界。

事实上 $K^*=P_MB^*|_M$，由正交分解、(5.3)、(5.4)，
$$
\begin{aligned}
\|(I-P_M)B^*w\|^2
&=\|B^*w\|^2-\|K^*w\|^2\\
&\ge\alpha_0^2\left(\frac1{1+r^2}-r^2\right)\|w\|^2\\
&>\alpha_0^2\frac{131}{156}\|w\|^2
\qquad(0\ne w\in M).
\end{aligned}
$$
因此
$$
\boxed{
\|(I-P_M)B^*w\|>
\alpha_0\sqrt{\frac{131}{156}}\|w\|
\quad(0\ne w\in M).
}
\tag{5.5}
$$
实际跨块耦合在整个 $M$ 上有正下界；它并不是可以忽略的小误差。

## 6. 真正缺陷的图度量伴随方程

由 (2.3) 与 $J$ 的有界可逆性，
$$
N=J\,\overline{CL}.
\tag{6.1}
$$
闭包取尾空间原 Hilbert 范数或等价图范数均相同。
因此对 $x\in L$，
$$
\begin{aligned}
Jx\in D
&\iff \langle Jx,JCz\rangle=0\quad(z\in L)\\
&\iff C^*Gx=0,\qquad G=I_L+C^*C.
\end{aligned}
$$
即
$$
\boxed{
J^{-1}D=G^{-1}\ker C^*.
}
\tag{6.2}
$$
这里 $G$ 有界正可逆，
$$
I_L\le G\le(1+r^2)I_L.
\tag{6.3}
$$
不能因 $G$ 接近恒等而直接删除它，更不能删除 $P_L$。

若 $w=Jx\in D$，利用 (2.2) 得
$$
0=C^*Gx=C^*x+(C^*)^2Cx
=C^*x+\eta Z_L^*Cx.
$$
所以
$$
\boxed{
C^*x=-\eta Z_L^*Cx,\qquad
\|C^*x\|\le\eta r\|x\|
<\frac{\eta}{\sqrt{12}}\|x\|
\quad(x\ne0).
}
\tag{6.4}
$$
这是一条真正使用 $w\perp BM$ 的压缩伴随近零方程。
此外由既有 $e_0\in N$，缺陷向量必有 $w_0=0$，亦即 $x_0=0$。

(6.4) 本身不推出 $x=0$：它没有给 $C^*$ 在 $e_0^\perp$ 上的正下界。
反过来，任何 $0\ne d\in\ker C^*$ 都通过
$x=G^{-1}d$、$w=Jx$ 给出原空间的非零缺陷；没有丢失等价方向。

### 6.1 与既有首位字典的相容性

首位图和图度量方程已经写在 [1cf 的工作字典](../notes/2026-11-13-single-bit-true-defect-metric-and-compressed-square-1cf8.md) 中。本稿新增的是 (4.10) 的明确统一小范数、(5.1)—(5.5) 的定量质量和强耦合界；不把已有字典重复登记为首次发现。

为核对 Y 模型的两种写法，另记 $A=S_Y$、$W=A(I+A)^{-1}$，不与本稿 $Z=N_1$ 混用。由 (4.3)、(4.5)，$\|A\|<1$，所以 $I+A$ 可逆。所有尾算子交换，直接相乘给
$$
H_Y-W=(I+A)(W^2-R),\qquad
H_Y^2-R=(I+A)^2(I-R)(W^2-R).
$$
两个前置因子均可逆，故
$$
\ker(H_Y^2-R)=\ker(W^2-R),\qquad H_Y|_L=W|_L.
$$
因此本稿的小范数界准确作用于同一个真实平方核及压缩算子；没有换核、换范数或遗漏 $I-R$。

## 7. 当前用途和未付清的步骤

本稿给：

1. 两个实际模型的完整首位图，及几乎等距的图参数化；
2. 整个核中首位占满质量 $<1/13$；
3. $\|B|_M\|<\alpha_0/\sqrt{12}$ 与环境 $B^*|_M$ 的强下界；
4. 真实跨块耦合的统一正下界；
5. 缺陷在准确图度量下的等价方程 (6.2) 与小残差 (6.4)。

要关闭 $N=M$，仍须排除这个真实 $L$ 上的 $\ker C^*$，或利用额外核方程证明 (6.4) 的零坐标解必为零。
首位图的小条件数没有控制反复消去全部低位时的成本，不能据此省掉 R249 移动头能量中的未知尾项。

## 来源

- [R200](../results/R200-boundary-right-shift-domains-and-forward-division-saturation.md)：实际 $M,N$、首阶旗与 $e_0\in N$。
- [R216](../results/R216-uniform-occupied-prefix-decay-in-actual-slow-kernels.md)：此前整个核的占满前缀界及环境伴随／压缩伴随的区别。
- [R249](../results/R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md)：实际精确权与有限头结构。
- [R249C](../results/R249-appendix-optimal-true-head-chain-similarity-cost.md)：全头严格单链相似的最优成本，与本稿首位图不同。
