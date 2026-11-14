# R293：极强新增位对 S1、S2 加强准则的真实传输

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：以下完整有限维极限与必要条件已证明；没有证明一般 S1、S2，也没有给出 Boolean 反例。** 这不是 [R281](R281-heavy-bit-height-transfer-and-sharp-universal-first-edge-lower-bound.md) 普通相邻序传输的重复：本稿保留真实三次桥的尺度，给出两个更强 SOS 准则在一位极强极限下的准确条件。S1 的上分支必须一起消元；只压缩下分支会误留一个正项。

## 1. 旧行、相邻出生及共同实际源

取旧 $N$ 位正权 Boolean 行
$$
d=\sum_{i=1}^N b_iE_i,\qquad C=\sum_{i=1}^N b_i^3E_i.
$$
固定 $r\ge1$，先假设 $N\ge2r+3$。令
$$
U=K_{r+1},\qquad V=K_r,\qquad W=K_{r-1},
\qquad K_j=\ker d\cap\mathcal H_j.
$$
这三个空间均继承实际物理 Hilbert 范数。旧归一真最小逆及其 Gram 为
$$
\mathcal J_{j,k}=(d^j/j!)^\dagger|_{K_k},\qquad
U_j=\mathcal J_{j,r+1}^*\mathcal J_{j,r+1},\quad
X_j=\mathcal J_{j,r}^*\mathcal J_{j,r},\quad
Z_j=\mathcal J_{j,r-1}^*\mathcal J_{j,r-1}.
$$
零阶均为相应空间的单位。每个逆先在完整物理层取，再限制源。定义真实三次桥
$$
A=C|_U:U\to V,\qquad B=C|_V:V\to W.
\tag{1.1}
$$

新增权 $a=\sqrt t$，令 $D_t=d+\sqrt t E_{N+1}$、$\varepsilon=t^{-1}$。记
$$
R=\mathcal J_{1,r},\qquad R_-=\mathcal J_{1,r-1}.
$$
在新出生 $r+1$、$r$，分别使用同一个经缩放的 primitive 源坐标
$$
\mathcal E_t(x,y)=(x-Ry,\sqrt\varepsilon\,y),
\qquad (x,y)\in U\oplus V,
$$
$$
\mathcal F_t(u,v)=(u-R_-v,\sqrt\varepsilon\,v),
\qquad (u,v)\in V\oplus W.
\tag{1.2}
$$
每个有限 $t>0$ 时它们都是到整个新 primitive 空间的线性同构。直接删除即核验 (1.2) 落在 $\ker D_t$；完整性是 R275 的 primitive 参数化。源 Gram 准确为
$$
U_0(t)=\operatorname{diag}(I_U,X_1+\varepsilon I_V),\qquad
V_0(t)=\operatorname{diag}(I_V,Z_1+\varepsilon I_W).
\tag{1.3}
$$
它们一般不等于单位矩阵。

以下用 $H_j(t)$ 表示新上出生第 $j$ 阶 Gram 在 $\mathcal E_t$ 下的二次型，$L_j(t)$ 表示新下出生第 $j$ 阶 Gram 在 $\mathcal F_t$ 下的二次型。这些 $H,L$ 是非正交源的形式，运算中保留 (1.3)。

## 2. 一位完整 Gram 与三次桥的准确尺度

[R275 全高度公式](R275-one-bit-full-primitive-schur-recursion-and-innovation.md)在 (1.2) 下给
$$
H_j(t)=
\begin{pmatrix}
P_j&-P_jq_j\\
-q_j^*P_j&X_{j+1}+\varepsilon X_j+q_j^*P_jq_j
\end{pmatrix},
\qquad
P_j=(U_j^{-1}+tU_{j-1}^{-1})^{-1},
\tag{2.1}
$$
以及
$$
L_j(t)=
\begin{pmatrix}
T_j&-T_j\rho_j\\
-\rho_j^*T_j&Z_{j+1}+\varepsilon Z_j+\rho_j^*T_j\rho_j
\end{pmatrix},
\qquad
T_j=(X_j^{-1}+tX_{j-1}^{-1})^{-1}.
\tag{2.2}
$$
在相应的最高硬端，按 R275 取 $P_j=\varepsilon U_{j-1}$ 或 $T_j=\varepsilon X_{j-1}$，不求不存在的旧逆。所有 $q_j,\rho_j$ 只依赖旧行。后文仅用
$$
q_1=A^*X_2,
$$
$$
Q:=\rho_1=B^*Z_2,\qquad
\Theta:=X_1^{-1}B^*Z_3,\qquad
\rho_2=\frac{Q+\Theta}{2},
$$
$$
\delta_3:=\rho_3-\rho_2
=\frac13(X_2^{-1}B^*Z_4-X_1^{-1}B^*Z_3).
\tag{2.3}
$$
这些是 [R275 三次桥创新式](R275-appendix-exact-cubic-bridge-for-shear-innovations.md) 的准确系数。

新增行的三次权删除为 $C_t=C+t^{3/2}E_{N+1}$。在两个共同源 (1.2) 中，其实际矩阵是
$$
\boxed{
\mathcal B_t=
\begin{pmatrix}
A&tI_V-T\\0&B
\end{pmatrix},\qquad
T=CR-R_-B=P_VCR.
}
\tag{2.4}
$$
这里 $T:V\to V$ 固定，不要求自伴。确实，$dCR=B=dR_-B$，故差值在 $V$；而 $R_-B\perp V$。将 $C_t$ 作用到 $\mathcal E_t(x,y)$ 并用 $\mathcal F_t$ 表示，恰给 (2.4)。

式 (2.4) 的右上块增长为 $tI$。省略这个增长或将源 (1.3) 当作正交坐标，都会改变下述极限。

## 3. S1 的完整同余极限

对新上、下出生定义 R275 的真实 S1 缺陷
$$
\mathscr E_t=C_{1,t}^2-C_{2,t}-\Delta_t\Gamma_{3,r}^{\rm new}(t)^{-1}\Delta_t^*,
$$
$$
\Delta_t=\tfrac12\bigl(C_{1,t}(B_t^{\rm phys})^*\Gamma_{3,r}^{\rm new}(t)
-(B_t^{\rm phys})^*\Gamma_{2,r}^{\rm new}(t)\bigr).
\tag{3.1}
$$
$C_{j,t}$ 是新上出生真正第 $j$ 精度；$B_t^{\rm phys}$ 是 (2.4) 对应的实际 Hilbert 算子。令
$$
\mathbf E_t=\mathcal E_t^*\mathscr E_t\mathcal E_t.
$$
把所有实际伴随、精度换成同一个非正交源形式，准确得到
$$
\mathbf E_t=
U_0H_1^{-1}U_0H_1^{-1}U_0-U_0H_2^{-1}U_0
-\frac14S_tL_3^{-1}S_t^*,
$$
$$
S_t=U_0H_1^{-1}\mathcal B_t^*L_3-\mathcal B_t^*L_2.
\tag{3.2}
$$
这一步只作实际同源坐标变换，没有交换逆和压缩。

定义旧主出生的第二高度加强缺陷
$$
\boxed{
E_2=X_2^{-1}X_1X_2^{-1}-X_3^{-1}
-\delta_3Z_4^{-1}\delta_3^*.
}
\tag{3.3}
$$
则在有限维算子范数中有完整极限
$$
\boxed{
\begin{pmatrix}t^{-1}I_U&0\\0&I_V\end{pmatrix}
\mathbf E_t
\begin{pmatrix}t^{-1}I_U&0\\0&I_V\end{pmatrix}
\longrightarrow
\begin{pmatrix}
I_U&A^*X_1\\
X_1A&X_1(AA^*+E_2)X_1
\end{pmatrix}.
}
\tag{3.4}
$$

### 3.1 逐块核验

令 $D_1=X_2+\varepsilon X_1$。由 (2.1) 的三角分解，
$$
H_1^{-1}=
\begin{pmatrix}
tI+U_1^{-1}+q_1D_1^{-1}q_1^*&q_1D_1^{-1}\\
D_1^{-1}q_1^*&D_1^{-1}
\end{pmatrix}.
\tag{3.5}
$$
因此第一项 $U_0H_1^{-1}U_0H_1^{-1}U_0$ 的三块分别是
$$
t^2I+O(t),\qquad tA^*X_1+O(1),
$$
$$
X_1AA^*X_1+X_1X_2^{-1}X_1X_2^{-1}X_1+O(t^{-1}).
\tag{3.6}
$$
第二精度形式 $U_0H_2^{-1}U_0$ 的上块为 $O(t)$、交叉为 $O(1)$，下块趋于 $X_1X_3^{-1}X_1$。

再由 (2.2)、(2.4)，$S_t$ 的上行是 $O(1)$，而下行准确满足
$$
(S_t)_{V,V}=O(t^{-1}),\qquad
(S_t)_{V,W}=2X_1\delta_3+O(t^{-1}).
\tag{3.7}
$$
例如其下右块的常数项是
$$
X_1(\rho_2-\rho_3)+X_1X_2^{-1}B^*Z_4-B^*Z_3
=2X_1\delta_3,
$$
其中使用 (2.3)，系数 $1/3$ 不可省。

$L_3^{-1}$ 的上块为 $tX_2^{-1}+O(1)$，交叉有界，下块趋于 $Z_4^{-1}$。所以 $\tfrac14S_tL_3^{-1}S_t^*$ 的上块为 $O(t)$、交叉为 $O(1)$，下块趋于
$$
X_1\delta_3Z_4^{-1}\delta_3^*X_1.
$$
这与 (3.6) 一起给出 (3.4)。固定旧模型后全部 $O$ 项均为实际有限矩阵范数界；每个等式也可由在 $\varepsilon=0$ 正可逆的有限块作 Neumann 展开得到。

### 3.2 准确必要条件与有限严格违反传输

若新出生 $r+1$ 的 S1 沿某个 $t\to\infty$ 序列成立，则 (3.4) 的极限块半正定。对其上面的单位块取 Schur 补，得到
$$
\boxed{X_2^{-1}X_1X_2^{-1}-X_3^{-1}
\succeq\delta_3Z_4^{-1}\delta_3^*.}
\tag{3.8}
$$
直接只看下压缩会多留 $AA^*$；(3.4) 的真实交叉 Schur 恰好将它消掉。不能用这个多余正项弱化 (3.8) 后再声称已掌握原必要条件。

若 (3.8) 有严格负二次型，则它也给一个有限新增权的 S1 违反。具体若
$\langle E_2v,v\rangle<0$，在 (3.4) 的极限块取
$$
y=X_1^{-1}v,\qquad x=-A^*v.
$$
其二次型正好为 $\langle E_2v,v\rangle$。范数收敛使同一个 $(x,y)$ 对所有充分大的有限 $t$ 保持负值，再用 (3.4) 左侧的可逆同余得到新实际 S1 的严格违反。这里没有使用无限权作为允许模型。

## 4. S2 的完整必要联合块

在旧主出生与下出生上定义
$$
K=X_1X_2^{-1}X_1\succ0,\qquad
D=Z_1-Z_2Z_3^{-1}Z_2,
$$
$$
\boxed{
M=\frac16\bigl(K\Theta-3KQ+2B^*Z_3Z_4^{-1}Z_3\bigr):W\to V.
}
\tag{4.1}
$$
此处 $K,D,M$ 的字母只用于本节；$K$ 不是 primitive 空间的记号。

新 S2 是某个真实两塔映射的收缩。其缺陷在新下源 $\mathcal F_t$ 中的形式，可准确写成
$$
\mathbf S_t=V_0-L_1L_2^{-1}L_1
-\frac14 R_t^*\mathcal C_t^{-1}R_t,
$$
$$
\mathcal C_t=U_0H_1^{-1}U_0,
\qquad
R_t=U_0H_1^{-1}\mathcal B_t^*L_2
+\mathcal B_t^*L_2L_3^{-1}L_2.
\tag{4.2}
$$
这保留所有非交换因子的次序。它来自 S2 中
$A_t=\tfrac12(C_{1,t}Q_t+Q_tL_{3,t}^{-1}L_{2,t})$
的实际 Gram；相邻源 Gram 抵消后才得到 (4.2)。

**准确极限为**
$$
\boxed{
\mathbf S_t\longrightarrow
\begin{pmatrix}
I_V-K&-M\\
-M^*&D-M^*K^{-1}M
\end{pmatrix}.
}
\tag{4.3}
$$
所以若新 S2 沿某个 $t\to\infty$ 序列成立，(4.3) 右侧必须半正定。这个条件比单独的旧主出生首边 $K\preceq I$ 和旧下出生第二边 $D\succeq0$ 更强，保留了共同的真实桥 $M$。

### 4.1 极限的逐块证明

由 (2.1)，
$$
\mathcal C_t^{-1}=U_0^{-1}H_1U_0^{-1}
\longrightarrow\operatorname{diag}(0,K^{-1}).
\tag{4.4}
$$
又由 (2.2)，
$$
V_0-L_1L_2^{-1}L_1
\longrightarrow\operatorname{diag}(I_V,D).
\tag{4.5}
$$
现在保留 $R_t$ 中两个有限极限。第一项的上、下两行分别趋于
$$
\bigl[2A^*X_1,\ -A^*X_1Q\bigr],
\qquad
\bigl[K,\ K(\Theta-\rho_2)\bigr].
\tag{4.6}
$$
为了核第二项，先算 $L_2L_3^{-1}L_2$ 的上行：
$$
\bigl[\varepsilon K,
\ \varepsilon(-K\rho_2+X_1\delta_3Z_4^{-1}Z_3)\bigr]
+O(\varepsilon^2).
$$
其下右块趋于 $Z_3Z_4^{-1}Z_3$。与 (2.4) 相乘后，第二项的上行趋于零、下行趋于
$$
\bigl[K,
-K\rho_2+X_1\delta_3Z_4^{-1}Z_3+B^*Z_3Z_4^{-1}Z_3\bigr].
$$
利用 (2.3)，两项的下行之和为
$$
\bigl[2K,
-KQ+\tfrac13K\Theta+\tfrac23 B^*Z_3Z_4^{-1}Z_3\bigr]
=\bigl[2K,2M\bigr].
\tag{4.7}
$$
因此 (4.4) 给
$$
\frac14R_t^*\mathcal C_t^{-1}R_t
\longrightarrow
\begin{pmatrix}K&M\\M^*&M^*K^{-1}M\end{pmatrix},
$$
与 (4.5) 相减即得 (4.3)。

若 (4.3) 的右侧有严格负见证，则同一有限维范数收敛将它传到所有充分大的有限 $t$，从而得到新增行的实际 S2 违反。尚未在任何实际旧权行上给出这样的负见证。

## 5. 硬顶、真空及没有获得的结论

1. 当 $N=2r+2$ 时，新上出生只有高度一，其 S1 取真实硬顶 $C_{2,t}=0$。旧主出生最高高度为二；在 (3.3)、(3.8) 中约定 $X_3^{-1}=0$。从 (3.2) 删除第二项；(3.5) 中不存在的旧 $U_1^{-1}$ 同样省去，真实 $P_1=\varepsilon I_U$，只移去一个 $O(1)$ 项。其他展开完全相同，(3.4) 仍成立。此时 (2.2) 的 $j=3$ 是新下出生最高层，须取 $T_3=\varepsilon X_2$。S2 极限亦保持不变。没有构造不存在的旧最小逆。
2. 当 $r=0$ 时，省略 $W$、$B$、全部 $Z$ 及相应行列。S1 必要条件只剩旧真空第二边；S2 极限只剩 $I-X_1X_2^{-1}X_1$。可在同样合法高度下直接核验。
3. 全 birth 的首阶 S1 因而至少强迫 (3.8) 这个第二高度加强式；它不只是普通第二边。这里没有声称可以无证明地反复应用同一个首阶 S1 极限得到所有更高加强式。
4. 本稿没有从全 Hankel 正性的已知失败推出 (3.8) 或 (4.3) 失败。那是不同的正块。也没有把 R285 的非 Boolean 形式数据代入本稿并称为实际反例。
5. 一般 S1、S2 与一般有限正权的相邻常数一仍未完成。这里支付的是共同物理源、完整上分支、三次桥增长及有限严格违反传输，供后续真正证明或反证使用。
