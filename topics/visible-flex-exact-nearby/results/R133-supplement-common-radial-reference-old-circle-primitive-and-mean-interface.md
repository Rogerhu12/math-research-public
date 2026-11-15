# R133 补篇：common-T 参考列的完整旧圆 primitive 与逆算子接口

2026-11-15，visible-exact / phase_inverse。

**状态：精确解析恒等式及条件范数接口；新的 potential、列函数和强算子数值门尚未执行。**
本篇连接
[共同径向 Langer 参考及完整源口](R133-supplement-common-radial-Langer-reference-and-complete-source-ports.md)
与
[保留抵消的共同径向势](R133-supplement-cancellation-preserving-common-radial-potential-and-ports.md)。
它不改变已选旋转数、当前真实修补背景、物理接缝或独立 even mean。

这里使用已经纠正的 canonical 主部 $\partial_T^2+T\partial_X^2$。
取 $n=4|j|$、$\epsilon=\operatorname{sgn}j$、$j\ne0$。
所有有序矩阵公式同时适用于两条真正独立的 radial 参考解；
不得只检查其中一条高度列。

## 1. 真实参考、旧角导数与完整投影

固定实际参数后，设 $Y_j$ 是同一 common-$T$ 势的任一真实解：
$$
 Y_{j,TT}=(n^2T-V_j(T))Y_j.
 \tag{I.1}
$$
$V_j$ 可以为复值；本篇没有把两符号或复参数以共轭代替。
其自变量是当前共同 canonical $T$。在使用的域中必须先证明这个
参考解和 $V_j$ 确实存在，并可在实际 $T(r,\phi)$ 上评价。

(I.3)--(I.14) 先在同一真实径向 reference 分支的光滑共同域内成立。
若 $T(r,\phi)$ 穿过该 reference 的原物理匹配界面，必须先按完整两行
匹配重构，并在旧圆微分、primitive 和径向源中保留实际界面项，
包括 $B_jw$ 及其重构列的可能跳。
分片 ODE 本身不证明组合后的整圆场光滑；只有已付的真共迹或完整
分布跳项合同才允许把这些局部式合并。一个原解析片内的人为切口不产生新跳。

记
$$
 \mathcal U_j^V(w)=e^{i\epsilon nX}
       \left(w_1Y_j+w_2n^{-1}Y_{j,T}\right),\qquad
 w=\binom{w_1}{w_2}.
 \tag{I.2}
$$
旧圆仍是物理角 $\phi$，频率为 $4m$。
$P=1-\langle\cdot\rangle_\phi$，
$I=\partial_\phi^{-1}P$；故 $I1=0$、$I\partial_\phi=P$。
这两个投影身份在以下全部公式中保持，不假设
$\langle\mathcal U_j^V(w)\rangle_\phi=0$。
即使输入 $j\ne0$，真实 $X,T,w$ 也会产生零输出和其他全部输出。

写
$$
 x=X_\phi,\quad y=T_\phi,\quad
 \mathcal K(T)=\begin{pmatrix}0&T\\1&0\end{pmatrix},
 \quad H=i\epsilon x\,\mathrm{Id}+y\mathcal K(T),
 \quad B_+=x^2+Ty^2 .
$$
则准确有
$$
 \partial_\phi\mathcal U_j^V(w)
  =\mathcal U_j^V\bigl(w_\phi+nH_j^Vw\bigr),\qquad
 H_j^V=H-\frac{yV_j}{n^2}E_{12}.
 \tag{I.3}
$$
这里 $E_{ab}=e_ae_b^t$。
(I.3) 直接使用 (I.1)；potential 项为
$-n^{-1}yV_jw_2Y_j$，没有丢掉因子 $n^{-2}$，
也没有把 $I$ 错当成逐 $T$ 的 primitive。

## 2. 必须重新支付的准确逆门

自由矩阵与新矩阵的行列式分别是
$$
 \det H=-B_+,\qquad
 \det H_j^V=-B_++\frac{y^2V_j}{n^2}
           =-B_+(1-\zeta_j),\qquad
 \zeta_j=\frac{y^2V_j}{n^2B_+}.
 \tag{I.4}
$$
这仍是主部的 $B_+$，不是 leading 高度中的 $B_-$。
假设在同一个完整复域上 $B_+\ne0$、$1-\zeta_j\ne0$。
Sherman--Morrison 的准确有序式为
$$
 B_j:=(H_j^V)^{-1}
 =H^{-1}
  +\frac{yV_j}{n^2(1-\zeta_j)}
       H^{-1}E_{12}H^{-1}.
 \tag{I.5}
$$
因此在点态或同域 strip supremum 中，若
$\sup|\zeta_j|\le\vartheta<1$，则
$$
 \|B_j\|\le\|H^{-1}\|
  +\frac{|yV_j|}{n^2(1-\vartheta)}\|H^{-1}\|^2.
 \tag{I.6}
$$
如果改在解析 Wiener 范数中直接用 Neumann 级数，
则必须证明 $\|\zeta_j\|_{\mathcal A_\sigma}<1$，并将 (I.6)
的全部乘积解释为同一 Banach 代数范数。
只有 strip supremum 门时，要在更窄正条带上支付完整 Fourier
几何和，不能把同条带 supremum 免费称为 Wiener 范数。

所有角导数都微分完整 $V_j(T(r,\phi))$。
例如 $\partial_\phi V_j=V_{j,T}y$。
若需要二阶角导，则还保
$V_{j,TT}y^2+V_{j,T}T_{\phi\phi}$。
(I.5) 本身不授这些导数或其统一数值常数。

## 3. 完整旧圆 primitive 的有限精确递推

由 (I.3) 代入 $B_jw$，再施加真实 $I$，准确得到
$$
 IP\mathcal U_j^V(w)
 =\frac1nP\mathcal U_j^V(B_jw)
  -\frac1nIP\mathcal U_j^V\bigl(\partial_\phi(B_jw)\bigr).
 \tag{I.7}
$$
第一项中的 $P$ 不可省略；第二项的 $I$ 仍包含全部旧圆输出。

若真实 reference 界面把旧圆切成子弧，先逐子弧使用 (I.3)。
对分片函数 $F=\mathcal U_j^V(B_jw)$，其完整分布导数另含
$\sum_a[F]_{\phi_a}\delta_{\phi_a}$，其中跳按增大 $\phi$ 的方向定义。
因此在这种情况下 (I.7) 右端还须加
$$
 -\frac1n I\sum_a
       [\mathcal U_j^V(B_jw)]_{\phi_a}\delta_{\phi_a}.
$$
这个式子保留全部输出与零模投影；没有声称跳为零。
后续有限递推每一层的相应 jump、以及移动界面的径向源，也须逐项另付。
本篇显示的无 jump 形式仅在完整旧圆确位于同一足够光滑的公共 reference
域，或已由真实匹配严格证明这些分布项消失时直接适用。

定义 $\mathcal D_{B_j}w=\partial_\phi(B_jw)$。
对任意有限 $N\ge1$，只作代数代入可得
$$
 IP\mathcal U_j^V(w)
 =\sum_{k=0}^{N-1}
   \frac{(-1)^k}{n^{k+1}}
       P\mathcal U_j^V(B_j\mathcal D_{B_j}^{\,k}w)
  +\frac{(-1)^N}{n^N}
       IP\mathcal U_j^V(\mathcal D_{B_j}^{\,N}w).
 \tag{I.8}
$$
这是真正带完整余项的有限恒等式。
没有让 $N\to\infty$，也不把这个有限式自动称为可逆全符号级数。

(I.7)--(I.8) 可以先对有限输入和证明，然后在已经证明有界的
共同输入/输出窗中取极限。这里的 $n^{-1}$ 是**输入频率**的权；
它不是输出 $4|m|$ 的权。若之后把它移过真实 FIO、非局部逆或
矩阵字，必须支付对应完整换位或双 Schur 费用。
$\|I\|_{H^s\to H^s}\le1/4$ 是旧圆的真实全输出界，
但它不代替 $\mathcal U_j^V$ 的完整列函数估计。

## 4. 已付旧圆逆 J 的准确入口

沿用完整 moving scalarization 的非mean算子
$$
 \mathcal C=P(\eta\partial_\phi+\mathcal L)P,\qquad
 J=\mathcal C^{-1}
 \tag{I.9}
$$
于已经付清的声明空间中。$\eta$ 是真实径向标量；
$\mathcal L$ 包括原完整局部零阶、primitive、投影 rank 项，
不能只保其局部平均。独立 even mean 仍为另一真实方程，
不因 (I.9) 被删除。
若原 $J$ 只在指定奇偶子空间认证，须先取原真实奇偶组合，再使用 (I.10)。
单个复 carrier 本身不因此获得该逆定义域的扩张。

对 $q=(\eta n)^{-1}P\mathcal U_j^V(B_jw)$ 应用完整 $\mathcal C$，
得到
$$
 JP\mathcal U_j^V(w)
 =\frac1{\eta n}P\mathcal U_j^V(B_jw)
  -\frac1nJP\mathcal U_j^V\bigl(\partial_\phi(B_jw)\bigr)
  -\frac1{\eta n}JP\mathcal L P\mathcal U_j^V(B_jw).
 \tag{I.10}
$$
每个 $P$ 和 $\mathcal L$ 的次序均固定。
这是任一确有完整 $J$ 合同的窗口中的精确式；
它不从形式阶数推断低频逆、不改变 mean 条件，
也不能把其最后一项以径向 reference 势替代。

若 source 还含独立普通均值 $g_2$，它必须沿原 scalarization
另列输入、源和输出。既有 common-$T$ 两源矩阵保证不需要凭空
微分 $g_2$；(I.10) 没有更改该两源合同。

## 5. 有序径向导数和完整 mean 压缩

取原物理方向
$$
 D=\partial_r-d\partial_\phi,\qquad [D,\partial_\phi]=d_\phi\partial_\phi .
$$
对固定参数，参考解只通过 $T$ 依赖 $r,\phi$。所以
$$
 D\mathcal U_j^V(w)
   =\mathcal U_j^V(Dw+nH_{D,j}^Vw),\qquad
 H_{D,j}^V=i\epsilon(DX)\,\mathrm{Id}
             +(DT)\!\left(\mathcal K(T)-\frac{V_j}{n^2}E_{12}\right).
 \tag{I.11}
$$
采用同一实际 principal fold 的恒等
$DT=Qx,\ DX=-QTy$，自由式是
$H^{-1}H_D=-i\epsilon Q\mathcal K(T)$。
新式可在不交换任一矩阵的情况下写成
$$
 B_jH_{D,j}^V
 =-i\epsilon Q\mathcal K(T)
   -\frac{QV_j}{n^2}\,
       B_je_1\begin{pmatrix}i\epsilon y&x\end{pmatrix}.
 \tag{I.12}
$$
证明只需
$H_{D,j}^V=H_j^V(-i\epsilon Q\mathcal K)
 -(QV_j/n^2)e_1(i\epsilon y,\ x)$。
特别，不能把已付自由 $H^{-1}H_D$ 直接更名成新参考的结果。

定义完整新幅度
$$
 g_j^V=Dw-\partial_\phi(B_jH_{D,j}^Vw).
$$
由 (I.3) 与 (I.11) 准确得
$$
 D\mathcal U_j^V(w)
       -\partial_\phi\mathcal U_j^V(B_jH_{D,j}^Vw)
       =\mathcal U_j^V(g_j^V),\qquad
 \left\langle D\mathcal U_j^V(w)\right\rangle_\phi
       =\left\langle\mathcal U_j^V(g_j^V)\right\rangle_\phi.
 \tag{I.13}
$$
这是原完整 mean 压缩的同对象版本；它没有将 mean 设零。
把 (I.12) 代入后，
$$
 g_j^V
 =Dw+i\epsilon\partial_\phi(Q\mathcal K w)
 +\frac1{n^2}\partial_\phi
      \left(QV_jB_je_1(i\epsilon y,\ x)w\right).
 \tag{I.14}
$$
最后一项保留全部角导数、两振幅和真实乘法次序。
径向再微分时同样保 $D Q,DV_j,D B_j,Dx,Dy$ 及换位
$[D,\partial_\phi]=d_\phi\partial_\phi$。
所谓 $n^{-2}$ 只描述显示输入权，不能不付导数后直接授强余核。

## 6. 可执行数值接口与明确未付门

下一完整 consumer 至少需要以下同一参数族的真正输入：

| 数量 | 必须消费的完整信息 |
| --- | --- |
| 径向 $V_j$ | 共同参考势全式；全部 $j\ge97$ 和两符号；实域及实际使用的复域；所需 $T$ 导数 |
| Principal fold | 同一 $X,T,Q$ 的 joint Fourier/mixed jets、$B_+$ gap；真实物理接缝 |
| 新矩阵逆 | $\zeta_j$ 的实际 gap 和 $B_j$ 的完整范数；声明 strip 或 Wiener 窗 |
| 参考两列 | 同一 $V_j$ 下真实 $Y_j,n^{-1}Y_{j,T}$ 的两行、源和两端图；不能复用自由 Ai 的数值上界 |
| 旧圆算子 | 原 $J$、$\mathcal L$、$P$、ordinary mean 的全部输入/输出窗 |
| 参数和根口 | 原 Liouville/Piola 矩阵、真实 nonzero-entry 规范、独立 $g_2$ 和全部 physical seam/source 跳 |
| 强输出 | 每个有序字的双 Schur/全输出费用与正确输入权；不能只比较对角 $m=j$ |

已有完整原 intrinsic 根阶0--15、同 germ 的复三阶包络、
全65/193 cubic、修补常数及已付 common-$T$ 的 $c,V$ 抵消公式，
是新径向势预算的输入。它们本身不提供表中的参考两列或正区图。
正侧尤其不能以含 growing solution 的无约束 IVP 范数替代真正选定的
两端 Green/反射图。

本篇的结论仅是 (I.3)--(I.14) 的完整精确接口及明确收费位置。
当前两新物理片消费者仍继续使用其原真实 free-reference 幅度、
全部 old-circle 九词与五 mean 项；本篇不反向改写任何已完成
source 上包络，也不把一个新的径向恒等式冒称为 cutoff97 已闭合。
