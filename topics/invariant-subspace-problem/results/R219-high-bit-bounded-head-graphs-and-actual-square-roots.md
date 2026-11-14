# R219：高位删除下界给出的有界真实头图与尾移位平方根

日期：2026-11-13（Asia/Taipei）。作者：kernel。

状态：完整结构性必要条件。依赖 [R213](R213-walsh-block-deletion-and-coefficient-tail-kernel-obstruction.md) 的逐坐标删除下界和 R208 全等向性；不把有限放大中的有界平方根当成矛盾。

## 1. 适用范围

令 $M=\ker(X-\varphi(\mathcal B_2))$ 是本轮前稿中的闭危险分支。假设某个高位 $j$ 的 Walsh 删除满足
$$
\|b_jf\|\ge\beta\|f\|\qquad(f\in M),\qquad \beta>0.
\tag{1.1}
$$
对规范慢行，本轮前稿给所有充分大 $j$ 的 $\beta\ge c|a_j|$。

把第 $j$ 位抽出，其余位（包括低于 $j$ 的有限个物理位）构成空间 $K$。在该位的 Walsh 基中，写 $H=K\oplus K$，向量的第二分量对应含第 $j$ 位的 Walsh 项。于是 $b_j(u,v)=(v,0)$。

由 (1.1)，第二分量映射 $p_2|_M$ 单射且下方有界，故其像 $L=p_2M\subseteq K$ 闭。其逆是有界的，因而存在有界映射 $J:L\to K$ 使
$$
M=\{(Jy,y):y\in L\},\qquad
\|J\|\le\sqrt{\beta^{-2}-1}\le\beta^{-1}.
\tag{1.2}
$$
这里尚未假定 $JL\subseteq L$；下一节由实际不变性证明它。

## 2. 实际进位迫使图算子成为 $L$ 上的算子

记 $B=N_{j+1}$ 作用于 $K$，$t=\eta_jB$。实际第 $j$ 位物理矩阵为
$$
N_j=\begin{pmatrix}0&t\\I&0\end{pmatrix}.
$$
换到 Walsh 基得到
$$
N_j={1\over2}
\begin{pmatrix}I+t&I-t\\-I+t&-I-t\end{pmatrix}.
\tag{2.1}
$$
因为 $M$ 对 $B$ 不变，(1.2) 给
$$
BL\subseteq L,\qquad JB y=BJy\quad(y\in L).
\tag{2.2}
$$
此处等式右侧先理解在 $K$ 中。

再由 $N_jM\subseteq M$，(2.1) 的第二分量
$$
z=-\tfrac12[(I-t)J+(I+t)]y
\tag{2.3}
$$
落在 $L$。由于 $y,ty\in L$，这迫使 $(I-t)Jy\in L$。$\|t\|\le\eta_j<1$，且 $B$ 保持 $L$，所以 $(I-t)^{-1}=\sum_{r\ge0}t^r$ 保持 $L$。于是
$$
\boxed{JL\subseteq L.}
\tag{2.4}
$$
因此 $J$ 现在是真正的 $L$ 上有界算子，并与 $B_L=B|_L$ 交换。

把 (2.3) 代入第一分量等于 $Jz$ 的图条件，得到准确 Riccati 式
$$
(I-t)J^2+2(I+t)J+(I-t)=0,
$$
等价于
$$
\boxed{(J+I)^2=t(J-I)^2.}
\tag{2.5}
$$
所有运算发生在有界算子空间 $B(L)$，没有形式除法或未知闭域。

## 3. 图谱及有界物理头平方根

$B_L$ 是拟幂零算子的实际限制，所以 $r(B_L)=0$。由于 (2.5) 的因子交换，
$$
(J+I)^{2n}=t^n(J-I)^{2n}.
$$
取 $2n$ 次根并用谱半径公式，得到 $r(J+I)=0$。若 $L\ne0$，有
$$
\boxed{\sigma_L(J)=\{-1\}.}
\tag{3.1}
$$
特别 $J-I$ 真正有界可逆。

转回该位物理基，令
$$
R=(J+I)(J-I)^{-1}\in B(L).
\tag{3.2}
$$
(1.2) 变为
$$
\boxed{M=\{(Rz,z):z\in L\}\quad\text{在物理基中},}
\tag{3.3}
$$
并由 (2.5) 得
$$
\boxed{R^2=\eta_jB_L.}
\tag{3.4}
$$
设 $F:L\to M$ 为 $Fz=(Rz,z)$。它有界、下方有界且满射；实际进位矩阵给
$$
N_jFz=(\eta_jB_Lz,Rz)=F(Rz),
$$
从而
$$
\boxed{R=F^{-1}(N_j|_M)F.}
\tag{3.5}
$$
R23 的归一化幂限制单射稠密性因此传给 $R$。进而由 (3.4) 也得 $B_L$ 单射且稠密像。这里不依赖把某个全空间拟仿射无证下传到未知限制。

如果 $\eta_j(1+\|J\|)^2<4$，还能得到显式逆界。由
$$
(I-J)(3I+J)=4I-(J+I)^2
$$
和 (2.5)，
$$
\|(I-J)^{-1}\|
\le{3+\|J\|\over4-\eta_j(1+\|J\|)^2}.
$$
所以
$$
\boxed{\|R\|\le
{(1+\|J\|)(3+\|J\|)\over
4-\eta_j(1+\|J\|)^2}.}
\tag{3.6}
$$
规范慢行给 $\|J\|=O(|a_j|^{-1})$，超快 $\eta_j$ 使 (3.6) 对充分大 $j$ 有效，给 $\|R\|=O(|a_j|^{-2})$。这只是一个安全上界，不宣称锐利。

## 4. 全等向核所给的反对称性

如果 R208 的条件保证 $\mathcal B(M,M)=0$，则在第 $j$ 位物理基中，总共轭具有形式
$$
C(x,y)=(\widehat C y,\widehat C x).
$$
令 $\widehat{\mathcal B}(x,y)=\langle x,\widehat Cy\rangle$。把 (3.3) 代入全等向性，得到
$$
\boxed{\widehat{\mathcal B}(Rx,y)
=-\widehat{\mathcal B}(x,Ry)\qquad(x,y\in L).}
\tag{4.1}
$$
这不要求 $\widehat CL=L$，也不说明 $R$ 对通常 Hilbert 内积反自伴。该双线性型在 $L$ 上可能退化。

## 5. 留下的真实问题

(3.3) 是有界真实图，强于仅有稠密投影的最大闭图；(3.4) 是有界根，强于只在未定核心上的形式根式。

但 $K$ 含低于 $j$ 的有限放大因子。即便在通常单个有界算子上，有界平方根也可能通过矩阵伴随块实现。因此不能从 (3.4) 单独排除 $M$。

同样，(4.1) 是可能退化的不定双线性反对称性；不能把它变成正的交织度量，也不能从 $R^2$ 小就断言 $\|R\|$ 小。

尚须利用原分支方程在这些具体 $L,R$ 上的额外结构，才能控制相邻反射中剩下的 $B^{-1}E$。本稿不宣称这一限制商已有定义或有界。
