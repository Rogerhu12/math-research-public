# 任意旧四权同时加入三个弱位：七位完整硬端的联合抵消与严格边界区

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：以下十四维完整源的算子范数极限、全部交叉抵消及充分小正参数的严格加强 S1 已证明。** 旧四个权和弱组三个内部权均任意固定为正；唯一极限参数是弱组的共同尺度。本文没有把逐位极限的误差常数当成联合一致常数，也没有声称整个七位内部已闭。

## 1. 原模型、固定物理源及结论

每个 $\mathcal H_j$ 使用 $j$ 元占据集合的正交单位基，$E_i$ 删除第 $i$ 位，$K_j(d)=\ker(d|_{\mathcal H_j})$。记 $\mathcal J_{n,j}(d)$ 为完整映射 $d^n/n!$ 对 $K_j(d)$ 输入的最小范数右逆，$\Gamma_{n,j}(d)=\mathcal J_{n,j}(d)^*\mathcal J_{n,j}(d)$；一切伴随和压缩都按这个物理内积。

旧四位行和弱三位行分别记为
$$
d_o=\sum_{i=1}^4 b_iE_i,\qquad d_w=\sum_{j=1}^3 c_jE_j,
\qquad b_i,c_j>0.
$$
定义实际七位行
$$
d_\epsilon=d_o\otimes I+\epsilon I\otimes d_w,
\qquad \epsilon>0.
$$
其上源 $K_3(d_\epsilon)$ 的高度是一、维数十四；低源 $K_2(d_\epsilon)$ 的高度是三、维数也为十四。用原物理内积定义
$$
\mathcal K_\epsilon
=A_\epsilon^*L_{1,\epsilon}L_{3,\epsilon}^{-1}L_{1,\epsilon}A_\epsilon,
\quad
A_\epsilon=\left.\left(A_o+\epsilon^{-1}A_w\right)\right|_{K_3(d_\epsilon)},
$$
$$
A_o=\sum b_i^{-1}E_i,
\qquad A_w=\sum c_j^{-1}E_j.
\tag{1.1}
$$
这里 $L_{j,\epsilon}=\Gamma_{j,2}(d_\epsilon)$。由 [R297 奇数硬端消逆](R297-appendix-odd-hard-top-innovation-and-dual-lowering-cancellation.md)，$\mathcal K_\epsilon\preceq\kappa I$ 正是此完整上源的加强首 S1，硬端仅置第二精度为零。

置
$$
U=K_2(d_o),\quad V=K_1(d_o),\quad
K=K_1(d_w),\quad K^a=K_1(A_w),
$$
$$
S_o=\sum b_i^2,\quad S_w=\sum c_j^2,
\quad p_o=\prod b_i,\quad p_w=\prod c_j.
$$
$\dim U=2$、$\dim V=3$、$\dim K=\dim K^a=2$。弱物理第 $j$ 层记作 $W_j$，旧物理第 $j$ 层记作 $O_j$。上源的固定比较空间是正交直和
$$
\mathscr U=(U\otimes K)\oplus(V\otimes W_2)\oplus(O_0\otimes W_3),
\qquad 4+9+1=14.
\tag{1.2}
$$
弱补集酉映射记为 $\mathfrak c_w$，并置
$$
R_w=P_{K^a}\mathfrak c_w:W_2\to K^a.
\tag{1.3}
$$
这是满射部分等距，$R_w^*R_w$ 是秩二正交投影。

令 $\mathcal K_o$ 为旧四位、整个出生一的**真实首加强费用**：
$$
\mathcal K_o=L_1\left(L_2^{-1}+\delta_2\Gamma_{3,0}(d_o)^{-1}\delta_2^*\right)L_1,
\tag{1.4}
$$
其中 $L_j=\Gamma_{j,1}(d_o)$。具体写 $F=(\sum_i b_i^3E_i)|_V:V\to O_0$、$Z_j=\Gamma_{j,0}(d_o)$，则真实首桥创新为 $\delta_2=(L_1^{-1}F^*Z_3-F^*Z_2)/2$。令 $\mathcal K_w$ 为弱三位、整个出生一的硬端费用。

**定理 1（完整联合极限）。** 第 2 节给出的实际上源嵌入归一成等距映射 $\mathcal U_\epsilon:\mathscr U\to K_3(d_\epsilon)$ 后，
$$
\boxed{
\mathcal U_\epsilon^*\mathcal K_\epsilon\mathcal U_\epsilon
\xrightarrow[\epsilon\downarrow0]{\|\cdot\|}
\operatorname{diag}\left(
I_U\otimes\mathcal K_w,
\mathcal K_o\otimes R_w^*R_w,
\frac{e_2(b_1^2,\ldots,b_4^2)}{S_o^2}
\right).
}
\tag{1.5}
$$
所有十四个源方向均保留，尤其不能删除中间九维源中的三维零极限方向。

**推论 2（真实有限参数的严格区域）。** 对任意固定正 $b_i,c_j$，存在 $\epsilon_0(b,c)>0$，使每个 $0<\epsilon<\epsilon_0$ 都满足
$$
\boxed{
\mathcal K_\epsilon\preceq\frac{1525}{1564}I<I.
}
\tag{1.6}
$$
极限算子的统一上界实际为 $743/782$。$\epsilon_0$ 不宣称对全部旧权、弱内部权一致；其存在由同源算子范数收敛与固定正余量得到。

## 2. 精确代数源，不把 primitive 当成物理 cokernel

写 $e_o=A_o^*$。旧出生 $s\in\{0,1,2\}$ 的高度是 $h=4-2s$。对旧 primitive 向量 $u$ 和弱向量 $v$，只要 $d_w^{h+1}v=0$，定义
$$
\mathcal E_{\epsilon,s}(u\otimes v)
=\sum_{j=0}^h
\frac{(-\epsilon)^j}{j!(h)_{\underline j}}
 e_o^ju\otimes d_w^jv.
\tag{2.1}
$$
和式在弱次数消失处截断。由
$d_oe_o^ju=j(h-j+1)e_o^{j-1}u$，相邻两项准确抵消，故 (2.1) 在 $\ker d_\epsilon$ 中。

对 (1.2) 的三个块分别使用 $(s,h)=(2,0),(1,2),(0,4)$，得到实际嵌入 $E_\epsilon$。它在零参数处就是 (1.2) 的物理正交嵌入，故
$$
H_\epsilon=E_\epsilon^*E_\epsilon\to I,
\qquad \mathcal U_\epsilon=E_\epsilon H_\epsilon^{-1/2}.
\tag{2.2}
$$
在小正参数下 $E_\epsilon$ 单射，维数等于完整 $K_3$，因此它覆盖整个上源。有限 $\epsilon$ 中不把 $H_\epsilon$ 替换为恒等。

为了处理顶层逆，使用倒数权低源
$$
K_2(A_o+\epsilon^{-1}A_w)
=K_2(\epsilon A_o+A_w).
$$
以弱三位为基行，用其对偶升算子 $d_w^*$ 作同一个构造。固定源为
$$
\mathscr X=(O_2\otimes W_0)\oplus(O_1\otimes K^a),
\qquad6+8=14.
\tag{2.3}
$$
所得嵌入记为 $G_\epsilon$。第一块使用弱高度三、旧次数二；第二块使用弱高度一、旧次数一。因此它是一个明确的次数二多项式，且
$$
J_\epsilon^{\rm src}=G_\epsilon^*G_\epsilon\to I.
\tag{2.4}
$$
它覆盖完整倒数权低源。

令 $D_\epsilon$ 是物理第二层上的对角乘子
$e_I\mapsto\prod_{i\in I}b_{\epsilon,i}^2e_I$，其中七权为 $(b,\epsilon c)$，并令 $p_\epsilon=p_op_w\epsilon^3$。准确顶逆为
$$
\mathcal J_{3,2}(d_\epsilon)
=p_\epsilon^{-1}\mathfrak c\,D_\epsilon|_{K_2(d_\epsilon)}.
\tag{2.5}
$$
定义真正的顶测试
$$
W_\epsilon=p_\epsilon D_\epsilon^{-1}G_\epsilon.
\tag{2.6}
$$
它在原低源 $K_2(d_\epsilon)$ 中。

设 $F_\epsilon=d_\epsilon d_\epsilon^*|_{\mathcal H_2}$，这是完整二层上的正定矩阵。由于 $W_\epsilon$ 和 $A_\epsilon E_\epsilon$ 都在原低源，定义
$$
T_\epsilon=W_\epsilon^*F_\epsilon^{-1}
 (A_o+\epsilon^{-1}A_w)E_\epsilon.
\tag{2.7}
$$
这里先取完整 $F_\epsilon^{-1}$。为明确完整顶逆的支付，(2.5)–(2.6) 给
$$
W_\epsilon^*L_{3,\epsilon}W_\epsilon=G_\epsilon^*G_\epsilon=J_\epsilon^{\rm src}.
$$
而 $W_\epsilon:\mathscr X\to K_2(d_\epsilon)$ 是双射，故
$L_{3,\epsilon}^{-1}=W_\epsilon(J_\epsilon^{\rm src})^{-1}W_\epsilon^*$。再用 $L_{1,\epsilon}=P_{K_2}F_\epsilon^{-1}|_{K_2}$，原硬费用的等距坐标准确为
$$
\boxed{
\mathcal U_\epsilon^*\mathcal K_\epsilon\mathcal U_\epsilon
=H_\epsilon^{-1/2}T_\epsilon^*
 (J_\epsilon^{\rm src})^{-1}T_\epsilon H_\epsilon^{-1/2}.
}
\tag{2.8}
$$
因此只须求 $T_\epsilon$ 的有界算子极限；顶压缩逆没有被错误地交换到对角算子外。

## 3. 完整第一逆的唯一小 Schur

以下矩阵都在原物理正交占据基中。旧四位定义
$$
b=d_o^*1\in O_1,\quad a=e_o1\in O_1,
\quad D=d_o:O_2\to O_1,
\quad R=d_o:O_3\to O_2,
$$
$$
M=DD^*>0,\qquad N=M^{-1},\qquad U=\ker D,
\qquad C=\ker R^*.
$$
$C$ 是旧完整映射 $R$ 的物理 cokernel；一般 $C\ne U$。弱行记
$$
c=d_w^*1,\quad \alpha=A_w^*1,
\quad B=d_w:W_2\to W_1,\quad k=d_w1_{W_3}=\mathfrak c_wc.
$$
在弱次数 $0,1,2$ 的分解
$\mathcal H_2=(O_2\otimes W_0)\oplus(O_1\otimes W_1)\oplus(O_0\otimes W_2)$
中，完整第一 Gram 是
$$
F_\epsilon=\begin{pmatrix}
RR^*+\epsilon^2S_wI&\epsilon D^*\otimes c^*&0\\
\epsilon D\otimes c&M\otimes I+\epsilon^2I\otimes BB^*&\epsilon b\otimes B\\
0&\epsilon b^*\otimes B^*&S_oI+\epsilon^2kk^*
\end{pmatrix}.
\tag{3.1}
$$
先消去右下块，再消去中块。记所得矩阵为
$$
J_\epsilon=S_oI+\epsilon^2kk^*,
$$
$$
M_\epsilon=M\otimes I+\epsilon^2I\otimes BB^*
-\epsilon^2bb^*\otimes BJ_\epsilon^{-1}B^*,
$$
$$
S_\epsilon=RR^*+\epsilon^2S_wI
-\epsilon^2(D^*\otimes c^*)M_\epsilon^{-1}(D\otimes c).
\tag{3.2}
$$
固定正权下，所有余项以下均在有限维算子范数中成立。因为
$D^*ND=I-P_U$，
$$
J_\epsilon^{-1}=S_o^{-1}I+O(\epsilon^2),
\quad M_\epsilon^{-1}=N\otimes I+O(\epsilon^2),
$$
$$
\boxed{S_\epsilon=RR^*+\epsilon^2S_wP_U+O(\epsilon^4).}
\tag{3.3}
$$
旧代数 Lefschetz 分解给 $O_2=U\oplus\operatorname{Ran}R$ 为线性直和，所以 $P_C|_U:U\to C$ 可逆。定义
$$
\mathcal H=P_C(P_CP_UP_C|_C)^{-1}P_C,
\qquad \mathcal J=\mathcal H|_U:U\to C.
$$
$P_U\mathcal Ju=u$。对 (3.3) 作真正的 $C\oplus C^\perp$ 块消元，得到
$$
\boxed{S_\epsilon^{-1}=(\epsilon^2S_w)^{-1}\mathcal H+O(1).}
\tag{3.4}
$$
没有把 $U$ 免费当作 $RR^*$ 的核。

对任意物理列 $f=(f_0,f_1,f_2)$，写
$$
\widehat f_1=f_1-\epsilon(b\otimes B)J_\epsilon^{-1}f_2,
\qquad
\widetilde f_0=f_0-\epsilon(D^*\otimes c^*)M_\epsilon^{-1}\widehat f_1.
\tag{3.5}
$$
完整逆配对准确分解为
$$
\langle w,F_\epsilon^{-1}f\rangle
=\langle\widetilde w_0,S_\epsilon^{-1}\widetilde f_0\rangle
+\langle\widehat w_1,M_\epsilon^{-1}\widehat f_1\rangle
+\langle w_2,J_\epsilon^{-1}f_2\rangle.
\tag{3.6}
$$
这同一个 Schur 平方同时用于全部上源列。

## 4. 顶测试的全部尺度及弱 primitive 消去

旧对角算子记为 $D_j e_I=b_I^2e_I$；弱对角算子记为 $Z_j e_I=c_I^2e_I$。旧倒数删除的层块记为 $A_1:O_1\to O_0$、$A_2:O_2\to O_1$。

弱三位在 $K^a=\alpha^\perp$ 上有以下直接矩阵恒等式：
$$
B k=2p_w\alpha,\qquad
B\mathfrak c_w|_{K^a}=-p_wZ_1^{-1}|_{K^a},
$$
$$
Z_2^{-1}B^*|_{K^a}=-p_w^{-1}\mathfrak c_w|_{K^a},
\qquad
P_{K^a}Z_1^{-1}(A_w|_{W_2})=-p_w^{-1}R_w.
\tag{4.1}
$$
例如 $B\mathfrak c_w=p_w\operatorname{diag}(\alpha)(\mathbf1\mathbf1^*-I)\operatorname{diag}(\alpha)$，第一组等式立即可核。另有 $c^*\alpha=3$。

将第 2 节 $G_\epsilon$ 的有限和逐项代入 (2.6)。对 $X\in O_2\otimes W_0$，得到准确三块
$$
(W_X)_0=\epsilon^3p_op_wD_2^{-1}X,
$$
$$
(W_X)_1=-\frac{\epsilon^2p_op_w}{3}(D_1^{-1}A_2X)\otimes\alpha,
\qquad
(W_X)_2=\frac{\epsilon p_o}{6}(A_1A_2X)\otimes k.
\tag{4.2}
$$
对 $Y\in O_1\otimes K^a$，同样准确有
$$
(W_Y)_0=0,
\quad (W_Y)_1=\epsilon p_op_w(D_1^{-1}\otimes Z_1^{-1})Y,
\quad (W_Y)_2=p_o(A_1\otimes\mathfrak c_w)Y.
\tag{4.3}
$$
最后一个有限项正是不能从原源的零阶物理支撑猜出的贡献。

置
$$
H=D_1^{-1}+S_o^{-1}bA_1,
\qquad Q=D_2^{-1}+D^*NHA_2.
$$
由 (3.5)、(4.1) 得
$$
\widehat{(W_X)}_1=-\frac{\epsilon^2p_op_w}{3}(HA_2X)\otimes\alpha+O(\epsilon^4),
$$
$$
\widetilde{(W_X)}_0=\epsilon^3p_op_wQX+O(\epsilon^5),
\tag{4.4}
$$
以及
$$
\widehat{(W_Y)}_1=\epsilon p_op_w(H\otimes Z_1^{-1})Y+O(\epsilon^3),
\qquad
\boxed{\widetilde{(W_Y)}_0=O(\epsilon^4).}
\tag{4.5}
$$
后一式的可能 $\epsilon^2$ 项含弱行
$c^*Z_1^{-1}|_{K^a}=\alpha^*|_{K^a}=0$，故准确消失。这支付了最危险的共同小 Schur 测试方向。

## 5. 上源各列的量级与旧临界酉抵消

记 $f=(A_o+\epsilon^{-1}A_w)E_\epsilon$。对上源的 $x,y,z$ 三块，(2.1) 直接给
$$
\begin{array}{c|ccc}
 &f_0&f_1&f_2\\ \hline
x\in U\otimes K
 &\epsilon^{-1}(I_U\otimes\alpha^*)x
 &(A_2\otimes I)x&0\\
y\in V\otimes W_2
 &O(1)
 &\epsilon^{-1}(I_V\otimes A_w|_{W_2})y+O(\epsilon)
 &(A_1\otimes I)y\\
z\in O_0\otimes W_3
 &O(\epsilon)&O(1)
 &\epsilon^{-1}\mathfrak c_w\alpha\,z+O(\epsilon).
\end{array}
\tag{5.1}
$$
因此 $\widehat f_1$ 的三个量级依次为 $O(1),O(\epsilon^{-1}),O(1)$，$\widetilde f_0$ 则依次为
$\epsilon^{-1}(I_U\otimes\alpha^*)x+O(\epsilon),O(1),O(\epsilon)$。

(3.4)、(4.4)、(5.1) 表明 $X\leftarrow x$ 的唯一常数项为
$$
\frac{p_op_w}{S_w}\,Q^*\mathcal J\otimes\alpha^*.
\tag{5.2}
$$
下面的旧四位精确恒等式将它完全化简：
$$
\boxed{Q^*\mathcal J u=p_o^{-1}\mathfrak c_ou\quad(u\in U).}
\tag{5.3}
$$

**证明。** 对 $(A_o,d_o^*)$ 的同一个代数 $\mathfrak{sl}_2$ 分解，旧第二层高度为零，故 $C=\ker d_o^*|_{O_2}=K_2(A_o)$。令 $v=\mathcal Ju\in C$，则 $v=u+D^*q$，其中 $q=NDv$。混合交换关系在旧第一层给
$$
A_2D^*=2I+bA_1,
$$
故由 $A_2v=0$、$A_1b=4$，
$$
q=-\tfrac12A_2u+\tfrac1{12}bA_1A_2u.
$$
又因 $b^*A_2u=A_1Du=0$，$b^*q=(S_o/12)A_1A_2u$。使用
$D_2^{-1}D^*=A_2^*D_1^{-1}$，可得
$$
Q^*v=D_2^{-1}u-A_2^*D_1^{-1}A_2u
+\tfrac14A_2^*A_1^*A_1A_2u.
\tag{5.4}
$$
对任意二元组 $\{i,j\}$，令其补集为 $\{k,l\}$，并写 $v_{ij}=u_{ij}/(b_ib_j)$。将 (5.4) 的 $ij$ 坐标乘以 $b_ib_j$，恰得
$$
v_{ij}-\sum_m v_{im}-\sum_m v_{jm}+\sum_{a<b}v_{ab}=v_{kl}.
$$
这就是四位的完整容斥，给 (5.3)。证毕。

因此 (5.2) 为
$$
T_{Xx}=\frac{p_w}{S_w}(\mathfrak c_o\otimes\alpha^*)|_{U\otimes K}.
\tag{5.5}
$$
旧权的条件数全部在这个共同抵消中消失，不能用各项的范数代替 (5.3)。

## 6. 其余常数块及全部交叉

把 (4.2)–(5.1) 代入同一个 (3.6)。除 $X\leftarrow x$ 外，只有 $X\leftarrow z$ 和 $Y\leftarrow y$ 保留常数项。

对 $X\leftarrow z$，只需最后的正常块：$\langle k,\mathfrak c_w\alpha\rangle=3$，故
$$
\boxed{
T_{Xz}z=\frac{\mathfrak c_o(d_o^*)^2 1}{2S_o}\,z.
}
\tag{6.1}
$$
对 $Y\leftarrow y$，中间正常块和最后正常块都须保留。用 (4.1)，其和是
$$
T_{Yy}=-T_o\otimes R_w,
$$
$$
\boxed{
T_o=p_o\left(H^*N-S_o^{-1}A_1^*A_1\right)|_V:V\to O_1.
}
\tag{6.2}
$$
这里没有把 $N$ 先压到 $V$。

其余块趋于零：由已列量级，$X\leftarrow y=O(\epsilon)$、$Y\leftarrow x=O(\epsilon)$。$Y\leftarrow z$ 最后正常块表面上有 $\epsilon^{-1}$ 项，但它含
$$
P_{K^a}\mathfrak c_w(\mathfrak c_w\alpha)=P_{K^a}\alpha=0,
$$
所以同样为 $O(\epsilon)$。小 Schur 的其余贡献按 (3.4)、(4.5) 均趋零。因此整个 $T_\epsilon$ 有界并在范数中收敛到
$$
\boxed{
T_0(x,y,z)=\left(
\frac{p_w}{S_w}(\mathfrak c_o\otimes\alpha^*)x
+\frac{\mathfrak c_o(d_o^*)^21}{2S_o}z,
\ - (T_o\otimes R_w)y
\right).
}
\tag{6.3}
$$
两个 $X$ 输出之间准确正交：$U\perp(d_o^*)^2O_0$，而补集是酉。$X$ 和 $Y$ 是 (2.3) 的物理正交源。有限参数时 $J_\epsilon^{\rm src}$ 仍保在 (2.8)；这里只在已证明 $T_\epsilon$ 有界后使用其趋于恒等。

## 7. 中块确是旧首加强费用

为准确识别 (6.2)，考虑旧四位只加一个权 $\eta>0$ 的位。旧上临界块仍为 $U$，旧低源为 $V$。使用代数上源
$$
y\longmapsto(-\eta e_oy/2,y),\qquad y\in V.
$$
它与 [R297 单弱位真实源](R297-weak-bit-critical-pool-cancellation-and-first-edge-transfer.md)的 $(-\eta\mathcal J_{1,1}y,y)$ 只相差一个 $O(\eta)$ 的旧 $U$ 块：两源的准确坐标变换是 $(x,y)\mapsto(x+\eta(\mathcal J_{1,1}-e_o/2)y,y)$。其趋于恒等；R297 的整个标准化费用已在范数中收敛，因而有界，这个趋于恒等的源变换不改变极限。

新低源的倒数权固定比较空间为整个 $O_1$。用与第 2 节相同的准确顶测试，其两个物理块是
$$
W_0=\eta p_oD_1^{-1}X,
\qquad W_1=-p_oA_1X.
$$
完整第一 Gram 的两个块为
$$
\begin{pmatrix}M+\eta^2I&\eta b\\\eta b^*&S_o\end{pmatrix}.
$$
同一 Schur 配对的常数项准确为
$$
p_o\left[\left(D_1^{-1}+S_o^{-1}A_1^*b^*\right)N
-S_o^{-1}A_1^*A_1\right]|_V=T_o.
$$
有限源度量都趋于恒等。R297 已证明该完整单弱位硬费用的 $V$ 块范数极限是旧首加强费 $\mathcal K_o$，且临界 $U$ 块与交叉趋零。因此
$$
\boxed{T_o^*T_o=\mathcal K_o.}
\tag{7.1}
$$
这是同一个完整第一逆的识别，不是把两种同维矩阵凭名称相同而等同。

由 (6.3)、(7.1) 及全部交叉正交，$T_0^*T_0$ 正是 (1.5) 的右侧。最后在 (2.8) 中使用 $H_\epsilon\to I$、$J_\epsilon^{\rm src}\to I$，得到定理 1 的完整算子范数收敛。

## 8. 统一极限余量与有限正参数

对弱三位，直接的硬端公式给
$$
\mathcal K_w=\frac{p_w^2}{S_w^2}
 P_K\alpha\alpha^*|_K,
\qquad
\|\mathcal K_w\|
=\frac{S_we_2(c^2)-9p_w^2}{S_w^3}<\frac14.
\tag{8.1}
$$
最后严格界可由三变量 Schur 不等式
$S_w^3+9p_w^2\ge4S_we_2(c^2)$ 得到，因为 $p_w>0$。

旧真空项满足
$$
\frac{e_2(b^2)}{S_o^2}\le\frac38,
\tag{8.2}
$$
因为 $\sum b_i^4\ge S_o^2/4$。

中块使用新完成的 [R298 全五权硬端定理](R298-five-independent-positive-weights-birth-two-hard-top-strengthened-s1.md)。对任意固定旧四权，添加任意小的单弱位仍是五个独立正权，故其整个硬费用都不超过 $(743/782)I$。取 R297 的准确单弱位范数极限，即得
$$
\boxed{\mathcal K_o\preceq(743/782)I_V.}
\tag{8.3}
$$
这明确支付了从 R298 到旧四位首加强费用的调用；没有将五位结论直接当作四位同名矩阵。

所以 (1.5) 的极限不超过 $(743/782)I_{\mathscr U}$。利用其与 1 之间的固定余量 $39/782$，范数收敛给出参数阈值，使所有更小正 $\epsilon$ 的误差小于 $39/1564$，从而得到 (1.6)。阈值依赖固定旧权和弱内部权；本文不据此在旧权同时随 $\epsilon$ 变动时交换极限。

这个同步弱位边界的全部潜在发散已通过完整第一逆、真实顶测试和共同 Schur 消元消去。一般七位内部、更多同步弱位、全部奇数硬端的统一有限常数，以及原 graph 源费用仍需继续证明。
