# 工作接口：一般出生一首边的精度矩阵与逐系数正性障碍

> 后续状态：本工作稿保留中间恒等式与逐单项式方法障碍。一般出生一首尾边现已由[完整同支持分组](../results/R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md)闭合；各节旧的未证状态只作为此前工作记录。

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。
范围：任意有限正权 Boolean 删除的真实出生一 primitive 比较。
状态：下列矩阵恒等式和系数障碍已证明；一般相邻界仍未证明。

## 1. 从完整逆到真实精度

取任意 $N\ge4$ 个正权，
$$
D=\sum_{i=1}^N a_iE_i,\qquad
z_i=a_i^2,\qquad A=\operatorname{diag}(a_i),\qquad
a=(a_i)_{i=1}^N.
$$
真实出生一核是 $K=a^\perp\subset\mathcal H_1$。
写
$$
F_n=\frac{D^n(D^*)^n|_{\mathcal H_1}}{(n!)^2},
\qquad
\Gamma_n=P_KF_n^{-1}|_K.
$$
在 $0\le n\le N-2$ 上这些完整逆均存在。

对 $1\le k\le N-1$，令 $I$ 按全部 $k$ 元子集、质量正比于
$z_I=\prod_{i\in I}z_i$ 分布。
记 $e_k=e_k(z)$、$m_i=z_i e_{k-1}(z_{\widehat i})$，并置
$$
M_k=\sum_{|I|=k}z_I\,1_I1_I^T.
$$
直接展开创建，得
$$
F_{k-1}=A^{-1}M_kA^{-1}.
$$
又 $M_k1=km$、$1^TM_k1=k^2e_k$，所以对 $K\oplus\mathbb Ca$ 作完整 Schur 补，给
$$
\boxed{
C_k=A^{-1}\left(M_k-\frac{mm^T}{e_k}\right)A^{-1}
=e_kA^{-1}\operatorname{Cov}_k(1_I)A^{-1}.
}
\tag{1.1}
$$
$C_ka=0$，且
$$
C_k|_K=\Gamma_{k-1}^{-1}.
\tag{1.2}
$$
这正是 [R239 出生一真实条件子集协方差](../results/R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md) §7 的精度接口；
此处写出全部矩阵以固定后面的实际乘序。
不是把 $P_KF_{k-1}|_K$ 当成 $\Gamma_{k-1}^{-1}$。

特别 $C_1=P_K$。因此普遍首边常数 $c$ 等价于
$$
\boxed{
\Gamma_1\Gamma_2^{-1}\Gamma_1\preceq cI_K
\quad\Longleftrightarrow\quad
C_3\preceq cC_2^2
}
\tag{1.3}
$$
在 $K$ 上成立。
两边都消去 $a$，故也等价于其在整个 $\mathbb C^N$ 上的半正定比较。

## 2. 只含对角和三个秩一项的准确矩阵

记
$$
S=e_1(z),\quad Z=e_2(z),\quad W=e_3(z),\quad T=\operatorname{diag}(z_i),
$$
$$
u=(S-T)a,\qquad v=(Z-ST+T^2)a.
$$
由 (1.1) 的对子集概率展开，
$$
\boxed{
C_2=SI-2T+aa^T-\frac{uu^T}{Z},
}
\tag{2.1}
$$
$$
\boxed{
C_3=ZI-2ST+3T^2+Saa^T-Taa^T-aa^TT-\frac{vv^T}{W}.
}
\tag{2.2}
$$
两式使用全部实际物理权，不需要等权池。

例如 $C_2$ 对角为
$e_1(z_{\widehat i})e_2(z_{\widehat i})/Z$；
非对角是
$$
a_ia_j\left[1-\frac{(S-z_i)(S-z_j)}Z\right].
$$
$C_3$ 对角为
$e_2(z_{\widehat i})e_3(z_{\widehat i})/W$；
非对角是
$$
a_ia_j\left[S-z_i-z_j-
\frac{(Z-Sz_i+z_i^2)(Z-Sz_j+z_j^2)}W\right].
$$
这些表达式同时核验 (2.1)--(2.2) 的对角修正项。

对 $f\in K$，记
$$
p=\langle Ta,f\rangle,\qquad q=\langle T^2a,f\rangle.
$$
使用
$$
\|u\|^2=SZ+3W
$$
直接展开，得到首边系数一的准确二次型
$$
\boxed{
\begin{aligned}
\langle(C_2^2-C_3)f,f\rangle
={}&\sum_i\bigl((S-z_i)^2-Z\bigr)|f_i|^2\\
&-\frac{SZ+W}{Z^2}|p|^2
+\frac1W\left|q-\left(S-\frac{2W}Z\right)p\right|^2.
\end{aligned}
}
\tag{2.3}
$$
这里 $f\perp a$ 不可省略；$p,q$ 按同一内积约定使用，绝对值与实交叉项不受约定影响。
式 (2.3) 仍有真实负项，不是一个已付正性分解。

## 3. 等权池物理头坐标与新增一位的秩一关系

若四异权稿的物理头为任意 $q$ 个正权，另有 $L\ge1$ 个单位池位，
在头源坐标
$$
\mathcal E x=\sum_i x_ie_i-\frac{a^Tx}{L}w_1
$$
中，$H_0=I+aa^T/L$，而 $H_{k-1}^{-1}$ 是 (1.1) 的头主块。
所以首边准确写为
$$
H_1^{-1}\left(I+\frac{aa^T}{L}\right)H_1^{-1}-H_2^{-1}\succeq0.
$$
这里不能省去源 Gram。

另外，在一个任意旧模型中新增平方权 $t>0$ 的单个位时，按是否选中该位分解条件子集分布，真实新头精度满足
$$
\widetilde C_k=C_k+tC_{k-1}
+\frac{t e_ke_{k-1}}{e_k+t e_{k-1}}\,b_kb_k^T,
\quad
b_k=A^{-1}\left(\frac{m_k}{e_k}-\frac{m_{k-1}}{e_{k-1}}\right).
\tag{3.1}
$$
此处 $\widetilde C_k$ 在全部旧物理位的源坐标中读取；
$C_0=0$，$e_0=1$，零元集合的均值为零。
它是混合分布的完整方差分解，不是把不同出生的 Gram 逐坐标相加。

写旧 $K=a^\perp$，$b_k=a/S+\beta_k$、$\beta_k\in K$。
有 $\beta_1=0$。若 $B=C_2|_K$，则
$$
\beta_2=-\frac{P_KTa}{Z},\qquad
\beta_3=\frac12\beta_2+\frac Z{2W}B\beta_2.
\tag{3.2}
$$
这一关系来自
$$
B(P_KTa)=\left(2S-\frac{3W}Z\right)P_KTa-2P_KT^2a.
$$
还可精确保留
$$
\|\beta_2\|^2=\frac SZ+\frac{3W}{Z^2}-\frac4S,
$$
$$
\langle B\beta_2,\beta_2\rangle
=\frac{SW}{Z^2}-\frac{9W^2}{Z^3}+\frac{8e_4(z)}{Z^2}.
\tag{3.3}
$$
(3.1)--(3.3) 为后续保全部新增方向的归纳提供接口；
没有据此宣布 (1.3) 在添一位下封闭。

## 4. 十次矩阵多项式的系数检验为何不能单独完成证明

考虑
$$
\mathcal M_c(z)=Z^2W\,A(cC_2^2-C_3)A.
\tag{4.1}
$$
它是总次数十的实对称整数系数矩阵多项式，并且
$$
\mathcal M_c(z)1=0.
$$
若 $c$ 为整数，其系数为整数。
每个单项式的系数矩阵只支持该单项式出现的物理位：
每个非对角元含 $z_iz_j$，每个对角元含 $z_i$。
所以直接逐系数半正定可以按十的有限整数分拆检查，
不依赖总位数 $N$。

但是这个充分方法确实失败，并且不能仅把目标常数放大修复。
给出三变量的完整手算证书。

仅保留 $x=z_1,y=z_2,z=z_3$，其余变量置零。
这只是读取多项式中支持在三个位上的系数，不把三位模型误用到实际需要 $N\ge4$ 的逆。
在三变量中 $W=xyz$，$C_3=0$，并且 $P=ZC_2$ 准确为
$$
P_{11}=yz(y+z),\quad P_{22}=xz(x+z),\quad P_{33}=xy(x+y),
$$
$$
P_{12}=-\sqrt{xy}\,z^2,\quad
P_{13}=-\sqrt{xz}\,y^2,\quad
P_{23}=-\sqrt{yz}\,x^2.
$$
因此
$$
(AP^2A)_{12}
=x^3y^3z-xyz^3(x^2+y^2+xz+yz).
$$
乘上 $W=xyz$ 后，
$x^4y^4z^2$ 的 $(1,2)$ 系数为一。
置换变量得到另两个非对角系数为负一；
再用准确的行和为零，可得
$$
\boxed{
[z_1^4z_2^4z_3^2]\,\mathcal M_c
=
c\begin{pmatrix}
0&1&-1\\
1&0&-1\\
-1&-1&2
\end{pmatrix}.
}
\tag{4.2}
$$
它在向量 $(1,-1,0)$ 上的二次型为 $-2c<0$。
所以任意 $c>0$ 都不能使 (4.1) 的每个单项式系数矩阵半正定。

这不是 (1.3) 的反例。
在当前三变量限制上，(4.1) 本身正是
$$
cW\,AP^2A\succeq0,
$$
完整平方和为正；失效的只是拆开其跨单项式补偿。
对 $N\ge4$，相同系数仍然存在，因此这个障碍确实属于原通用方法。

## 5. 保留的真实问题

首出生首边已经准确压到 (1.3) 或 (2.3)，
并有 (3.1) 的完整新增位方差分解。
当前未付的是其一般正性或一个不依赖总位数和权比例的较大常数。

下一步必须保留跨单项式平方和、完整秩一归纳或真实网络结构；
不能用“十次有限系数已全正”作结论，也不能从本节负系数推出 primitive 比较失败。
四异权全模型的已证常数十六仍按其独立完整 MP 证书成立。
