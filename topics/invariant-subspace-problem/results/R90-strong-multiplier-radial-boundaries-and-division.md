# R90：强交换子的圆盘缩放边界与全部芽商忠实除法

日期：2026-11-12（UTC）。子任务：literature。正式结果 R90；主会话逐式独审。**状态：已证明。**

本条完成 R85 保留的一般非单项式分母问题。设 $Y$ 为 R37 的实有序强交换子，或 R85 已处理的同虚部复有序强交换子，记
$$
\mathcal C=C^*(I,A),\qquad \mathcal D=C^*(\mathcal C,Y).
$$
证明包含两项实质结论：

1. 对每个 $|c|\le1$，存在含幺收缩 $*$-同态
   $$
   \sigma_c:\mathcal D\longrightarrow\mathcal D,\qquad
   \sigma_c|_{\mathcal C}=\operatorname{id},\qquad
   \sigma_c(Y)=cY.
   $$
   它们满足 $\sigma_c\sigma_d=\sigma_{cd}$；圆周参数给出点范数连续的自同构作用，$c=0$ 恰为 R73 的边界回缩（把像 $\mathcal C$ 看成 $\mathcal D$ 的子代数）。
2. 对任意非零收敛芽 $F,G\in\mathbb C\{z,w\}$，
   $$
   \boxed{
   \operatorname{Ran}F(A,Y)\subseteq\operatorname{Ran}G(A,Y)
   \iff F/G\in\mathbb C\{z,w\}.
   }
   $$
   因子允许先取任意 $B\in B(H)$。一旦 $G(A,Y)B=F(A,Y)$，它必唯一等于真正解析商 $(F/G)(A,Y)$。

第一项通过实际 Haar 空间的高位酉算子建立，不从形式缩放或辅助表示猜测；第二项不用 Arveson 扩张，也不把一个随参数变化的稠密范围自动当作解析提升。固定 $A$ 幂的 Bézout 差商恒等式明确填补这个步骤。

依赖：R9/R12 的实际权和 dyadic 递归；R28/R37 的精确强乘积；R66 的收敛芽 gcd/Bézout 与形式可除性引理；R73 的边界商；R80/R85 的全部非零混合芽单射稠密及单项式除法。本条不依赖未经证明的一般交换子正则化猜想。

## 1. 实参数的记号与两种真实误差

先取 R37 的实参数
$$
0\le s_j\le t_j,\qquad t\in\ell^2,\qquad
\sum_j(t_j-s_j)=\infty.
$$
令
$$
\rho_u=\frac{1-u}{1+u},\qquad
\kappa_j=\rho_{s_j}-\rho_{t_j}
=\frac{2(t_j-s_j)}{(1+s_j)(1+t_j)}\ge0,
$$
$$
\alpha_j=
\sqrt{\frac{1+t_j^2}{1+s_j^2}}\frac{1+s_j}{1+t_j},
\qquad
m_j=\sqrt{\frac{1+t_j^2}{1+s_j^2}},
$$
$$
W_j=\alpha_j(I+\rho_{s_j}N_j)
(I+\rho_{t_j}N_j)^{-1},
\qquad Y_k=\prod_{j<k}W_j.
$$
于是
$$
\sum_j\kappa_j=\infty,\qquad
\sum_j\kappa_j^2<\infty,\qquad
C_{\rm tot}=\prod_jm_j<\infty,
$$
$$
0<\alpha_j\le m_j,\qquad
\|W_j\|\le m_j,\qquad
Y=Y_kZ_k,\quad \|Z_k\|\le C_k:=\prod_{j\ge k}m_j\to1.
\tag{1.1}
$$
所有 $Y_k,Z_k$ 交换。R85 已证明 $Z_k\to I$ 强*。

### 1.1 实际尾与独立两点尾

设 $E_j=e_{10}$ 在第 $j$ 位作用，令
$$
\widetilde W_j=\alpha_j(I+\kappa_jE_j).
$$
R73 的实际进位比较给出，对充分大的 $k$ 及所有 $N\ge k$，
$$
\left\|\prod_{j=k}^{N-1}W_j
-\prod_{j=k}^{N-1}\widetilde W_j\right\|
\le K C_{\rm tot}^2\sum_{j\ge k}\eta_j. \tag{1.2}
$$
这里 $\eta_j=a_{j+1}/a_j\le e^{-770\,16^j}$，常数 $K$ 与 $k,N$ 无关。纯因子的范数同样不超过 $m_j$。

纯尾乘积有强*极限 $\widetilde Z_k$。为明确核对这一点，令参考向量
$\phi=(e_0+e_1)/\sqrt2$。当 $j$ 足够大时，
$$
\langle\widetilde W_j\phi,\phi\rangle
=\alpha_j(1+\kappa_j/2)=1+O(t_j^2),
$$
$$
\|\widetilde W_j\phi\|^2=1+O(t_j^2).
$$
伴随因子在 $\phi$ 上有相同的两类估计。因此标准的张量乘积范数恒等式及 $\sum t_j^2<\infty$ 给参考尾上的 Cauchy 性；有限柱向量上的同样结论，再与
$\prod m_j<\infty$ 的统一界结合，给全空间强*收敛。对 (1.2) 先取强极限，得
$$
\boxed{
\|Z_k-\widetilde Z_k\|
\le\varepsilon_k:=K C_{\rm tot}^2\sum_{j\ge k}\eta_j
\longrightarrow0.
} \tag{1.3}
$$

### 1.2 实际有限头可按范数截到低位矩阵

设 $A_k$ 是低 $k$ 位有限幂零链，满足
$$
\|A-A_k\|=a_k,\qquad
\|A_k^n\|\le\|A^n\|,\qquad A_k^{2^k}=0.
$$
对 $j<k$ 置
$$
N_{j,k}=A_k^{2^j}/d_j,\qquad d_j=\|A^{2^j}\|.
$$
则
$$
\|N_{j,k}\|\le1,\qquad
\|N_j-N_{j,k}\|\le 2^j a_k/d_j. \tag{1.4}
$$
并且 $N_{j,k}^2=\eta_jN_{j+1,k}$，其中定义 $N_{k,k}=0$。

把 $W_j$ 的有理函数作用到 $N_{j,k}$ 上，所得
$\widehat W_{j,k}$ 仍满足 $\|\widehat W_{j,k}\|\le m_j$：R37 的 Cayley 增生估计只要求输入算子为收缩，当前分母也因幂零性可逆。由 $|\rho_{t_j}|\le1$ 和二次递归，实际与截断的相关逆范数都不超过 $2/(1-\eta_0)$。预解式差恒等式因此给
$$
\|W_j-\widehat W_{j,k}\|
\le K_1m_j\kappa_j\|N_j-N_{j,k}\|.
$$
对乘积伸缩，置
$$
\widehat Y_k=\prod_{j<k}\widehat W_{j,k}
\in M_{2^k}\otimes I_{\ge k},
$$
得到
$$
\begin{aligned}
\|Y_k-\widehat Y_k\|
&\le K_1C_{\rm tot}
\sum_{j<k}\kappa_j2^j a_k/d_j\\
&\le K_2C_{\rm tot}\,2^k a_k/d_{k-1}
=:\delta_k\longrightarrow0. 
\end{aligned} \tag{1.5}
$$
最后利用 $\kappa_j\le2$、$d_j$ 递减，以及模型的精确权渐近：
$$
\log(2^k a_k/d_{k-1})
=-\frac{1045}{12}16^k+O(8^k+k2^k)\longrightarrow-\infty.
$$
因此高位酉算子不仅与固定 $\mathcal C$ 元素近似交换，也与增长中的实际前缀 $Y_k$ 近似交换；这个额外的移动头控制不能省略。

## 2. 任意圆盘标量的高位近似共同特征态

固定 $c\in\overline{\mathbb D}$。下面对每个充分大的 $k$ 构造只改动有限高位块 $[k,\ell_k)$ 的单位乘积向量 $\psi^{(k)}$，使
$$
\|(Z_k-cI)\psi^{(k)}\|\to0,\qquad
\|(Z_k^*-\overline cI)\psi^{(k)}\|\to0. \tag{2.1}
$$
更准确地，这些向量的低 $k$ 位仍是参考向量；估计完全在高位尾上成立，所以可以张量乘上任意固定低位向量。

### 2.1 选择一位期望

一位算子 $E=e_{10}$ 的数值域为闭圆盘 $\{|e|\le1/2\}$。事实上，对单位向量
$\psi=(\cos\theta,e^{i\varphi}\sin\theta)$，
$$
\langle E\psi,\psi\rangle
=\cos\theta\sin\theta\,e^{-i\varphi},
$$
恰取遍该圆盘。

因 $\sum\kappa_j=\infty$，可选有限 $\ell_k>k$，使
$$
K_k:=\sum_{j=k}^{\ell_k-1}\kappa_j\longrightarrow\infty.
$$
例如取使该和首次超过 $k$ 的指标。若 $c\ne0$，写
$$
c=e^{-a+i\theta},\qquad a=-\log|c|\ge0,\quad
\theta\in[-\pi,\pi].
$$
定义
$$
e_k=\frac12e^{2i\theta/K_k}-\frac a{K_k}. \tag{2.2}
$$
当 $a=0$ 时，$|e_k|=1/2$。当 $a>0$ 时，对充分大 $K_k$，
$$
|e_k|^2
=\frac14-\frac a{K_k}\cos(2\theta/K_k)+\frac{a^2}{K_k^2}
\le\frac14.
$$
因此可选单位向量 $\psi_j^{(k)}$，对所有 $k\le j<\ell_k$ 满足
$$
\langle E_j\psi_j^{(k)},\psi_j^{(k)}\rangle=e_k.
$$
块外取 $\psi_j^{(k)}=\phi$。若 $c=0$，在块内改取 $e_k=0$；同样可实现。

### 2.2 张量平均与方差

令各高位期望为
$$
e_j^{(k)}=
\begin{cases}
e_k,&k\le j<\ell_k,\\
1/2,&j\ge\ell_k,
\end{cases}
\qquad
\mu_j^{(k)}=\alpha_j(1+\kappa_je_j^{(k)}).
$$
在充分远的尾部，$|\kappa_je_j^{(k)}|<1/2$。统一的 Taylor 界给
$$
\log\alpha_j+\kappa_j/2=O(t_j^2),\qquad
\log(1+\kappa_je_j^{(k)})-\kappa_je_j^{(k)}
=O(\kappa_j^2).
$$
所以无限平均乘积
$$
M_k=\prod_{j\ge k}\mu_j^{(k)}
$$
存在，并且
$$
\log M_k
=K_k(e_k-1/2)
+O\!\left(\sum_{j\ge k}(t_j^2+\kappa_j^2)\right). \tag{2.3}
$$
当 $c\ne0$ 时，(2.2) 给
$$
K_k(e_k-1/2)=-a+i\theta+O(K_k^{-1}),
$$
故 $M_k\to c$。当 $c=0$ 时，实部主项为 $-K_k/2$，故同样有 $M_k\to0$。

对任意一位单位态 $\psi$，写
$\mu=\langle\widetilde W_j\psi,\psi\rangle$，有
$$
0\le\|\widetilde W_j\psi\|^2-|\mu|^2
\le\alpha_j^2\kappa_j^2.
$$
伴随方向有同样界，因为其均值为 $\overline\mu$。对有限张量积，正交投影到原乘积态给精确恒等式
$$
\left\|\bigotimes_j\widetilde W_j\psi_j
-\left(\prod_j\mu_j\right)\bigotimes_j\psi_j\right\|^2
=\prod_j\|\widetilde W_j\psi_j\|^2-\prod_j|\mu_j|^2.
$$
右边作乘积差伸缩，利用 $\|\widetilde W_j\|\le m_j$、
$\alpha_j\le m_j$，至多为
$$
C_k^2\sum_{j\ge k}\kappa_j^2.
$$
取纯尾强极限，得到
$$
\|(\widetilde Z_k-M_kI)\psi^{(k)}\|
\le C_k\left(\sum_{j\ge k}\kappa_j^2\right)^{1/2}, \tag{2.4}
$$
$$
\|(\widetilde Z_k^*-\overline M_kI)\psi^{(k)}\|
\le C_k\left(\sum_{j\ge k}\kappa_j^2\right)^{1/2}. \tag{2.5}
$$
结合 (1.3)、$M_k\to c$，便得 (2.1)。这同时控制两侧，未从单侧平均值或单侧近似特征向量推断伴随方向。

## 3. 实际酉交织与圆盘缩放 $*$-同态

对块内每一位取一个酉算子，把参考向量 $\phi$ 送到 $\psi_j^{(k)}$；其有限张量积记为 $U_k=U_k(c)$。它只作用于 $[k,\ell_k)$，在其他位为恒等，所以是整个 $H$ 上的酉算子。

由第 2 节，对每个固定柱向量 $x$，当 $k$ 超过其全部低位支撑后，
$$
(Z_k-cI)U_kx\to0,\qquad
(Z_k^*-\overline cI)U_kx\to0.
$$
使用统一的 $\|Z_k\|\le C_{\rm tot}$、$\|U_k\|=1$，这延伸到所有 $x\in H$：
$$
\boxed{
(Z_k-cI)U_k\to0,\qquad
(Z_k^*-\overline cI)U_k\to0
\quad\text{强收敛。}
} \tag{3.1}
$$

因为 $\mathcal C$ 是低位矩阵代数并的范数闭包，
$$
\|XU_k-U_kX\|\to0\quad(X\in\mathcal C). \tag{3.2}
$$
对于移动前缀，(1.5) 及 $\widehat Y_k$ 与 $U_k$ 精确交换给
$$
\|Y_kU_k-U_kY_k\|\le2\delta_k\to0, \tag{3.3}
$$
伴随也成立。

$Y_k\to Y$ 强收敛；固定共轭对称性还给 $Y_k^*\to Y^*$ 强收敛。于是
$$
\begin{aligned}
YU_kx-cU_kYx
={}&Y_k(Z_k-cI)U_kx\\
&+c(Y_kU_k-U_kY_k)x
+cU_k(Y_k-Y)x
\longrightarrow0.
\end{aligned} \tag{3.4}
$$
对伴随使用交换的 $Y_k^*,Z_k^*$，同样得到
$$
Y^*U_kx-\overline c\,U_kY^*x\longrightarrow0. \tag{3.5}
$$

对由 $\mathcal C,Y,Y^*$ 构成的任意有限 $*$-多项式 $P$，逐词伸缩给
$$
\|P(\mathcal C,Y,Y^*)U_kx
-U_kP(\mathcal C,cY,\overline cY^*)x\|\to0. \tag{3.6}
$$
由于 $U_k$ 酉，
$$
\|P(\mathcal C,cY,\overline cY^*)\|
\le\|P(\mathcal C,Y,Y^*)\|. \tag{3.7}
$$
因此所有实际代数关系都在替换 $Y\mapsto cY$ 后保持；替换在稠密的 $*$-代数上良定义、收缩、保持乘法与伴随，唯一按范数延伸为
$$
\boxed{
\sigma_c:\mathcal D\to\mathcal D,\qquad
\sigma_c|_{\mathcal C}=\operatorname{id},\quad
\sigma_c(Y)=cY.
} \tag{3.8}
$$
并且完整序列有
$$
U_k^*SU_k\longrightarrow\sigma_c(S)
\quad\text{强*收敛}\quad(S\in\mathcal D). \tag{3.9}
$$

生成元上的恒等式直接给
$$
\sigma_c\sigma_d=\sigma_{cd},\qquad \sigma_1=\operatorname{id}.
$$
因此 $|c|=1$ 时 $\sigma_c$ 的逆是 $\sigma_{\overline c}$。对每个固定 $S\in\mathcal D$，$c\mapsto\sigma_c(S)$ 在闭圆盘上按范数连续：有限词显然连续，而收缩性允许一致的范数逼近。对 $c\ne0$，其像包含 $\mathcal C$ 和 $Y=c^{-1}\sigma_c(Y)$，所以 $\sigma_c$ 满射；不由此宣称它在 $0<|c|<1$ 时单射。

当 $c=0$，生成元值与 R73 的 $\Pi$ 一样，故 $\sigma_0=\Pi$（包含到 $\mathcal D$ 后）。

### 3.1 同虚部复参数

R85 已完整证明，任何同虚部复有序 $Y$ 都可写为
$$
Y=VY_0,\qquad V,V^{-1}\in\mathcal A,
$$
其中 $Y_0$ 是一组实有序参数的 R37 强交换子，且
$C^*(\mathcal C,Y)=C^*(\mathcal C,Y_0)$。上述 $\sigma_c$ 固定 $V$，因此
$\sigma_c(Y)=V(cY_0)=cY$。同一酉序列因 (3.2) 也近似交换 $V,V^*$，所以 (3.9) 仍成立。由此下文覆盖 R85 的全部复参数范围。

## 4. 任意有界因子产生整个圆盘上的一致有界因子

设非零芽 $F,G$ 满足
$$
G(A,Y)B=F(A,Y),\qquad B\in B(H). \tag{4.1}
$$
先约去解析 gcd；该操作合法，因为 R80/R85 给非零共同因子在算子上单射。以下仍记约分后的芽为 $F,G$，它们互素。

若 $w\mid G$，(4.1) 使 $\operatorname{Ran}F(A,Y)\subseteq\operatorname{Ran}Y$；R85 的轴除法迫使 $w\mid F$，与互素矛盾。因此
$$
g_0(z):=G(z,0)\not\equiv0. \tag{4.2}
$$
对 $|c|\le1$，记
$$
F_c=F(A,cY),\qquad G_c=G(A,cY).
$$
当 $c\ne0$ 时，$G(z,cw)$ 是非零芽；当 $c=0$ 时，用 (4.2)。所以每个 $G_c$ 都单射且值域稠密。

固定 $c$，取第 3 节的酉序列。算子 $U_k^*BU_k$ 范数一致有界于 $\|B\|$，在可分 $H$ 上取 WOT 聚点 $B_c$。由 (3.9)，
$$
U_k^*G(A,Y)U_k\to G_c,\qquad
U_k^*F(A,Y)U_k\to F_c
$$
都是强*收敛。因此 (4.1) 可按矩阵元传到极限：左因子的伴随强收敛与右因子的弱收敛给
$$
\boxed{G_cB_c=F_c,\qquad \|B_c\|\le\|B\|.} \tag{4.3}
$$
$G_c$ 单射保证有界解唯一，所以该 $B_c$ 与选取的聚点或酉序列无关。

从 $G_c[A,B_c]=0$ 得 $[A,B_c]=0$。因此 $B_c$ 与 $Y$ 以及全部 $F_d,G_d$ 交换。进一步，
$$
G_c(B_cB_d-B_dB_c)=F_cB_d-B_dF_c=0
$$
给 $B_cB_d=B_dB_c$。

最后，$c\mapsto B_c$ WOT 连续：若 $c_\nu\to c$，由统一范数界取任意 WOT 子列聚点；$G_{c_\nu}\to G_c$、$F_{c_\nu}\to F_c$ 按范数连续，使该聚点仍满足 (4.3)，所以只能是 $B_c$。可分空间有界球的 WOT 可度量紧性把这一唯一聚点论证推广到完整序列。

## 5. 固定分母差商恢复真正的算子值解析性

这里不能仅凭“$G_c$ 解析、逐点单射、$B_c$ 有界”就跳过解析性证明。R66 的纯解析 Bézout 引理对互素 $F,G$ 给出
$$
UF+VG=z^m \tag{5.1}
$$
其中 $U,V$ 为收敛芽、$m\ge0$。用
$$
U_c=U(A,cY),\qquad V_c=V(A,cY),\qquad
H_c=U_cB_c+V_c
$$
得到
$$
G_cH_c=A^m. \tag{5.2}
$$
这些算子全都交换。它们局部一致有界，且 WOT 连续。

$F_c,G_c,U_c,V_c$ 实际上是整个 $c$ 平面上的范数解析函数：收敛芽的系数只有指数增长，而 $Y$ 拟幂零使相应 $c$ 系列在任意紧集上绝对范数收敛。

对任意 $c,d$，(4.3)、(5.2) 给精确恒等式
$$
\boxed{
A^{2m}(B_c-B_d)
=(F_cG_d-F_dG_c)H_cH_d.
} \tag{5.3}
$$
例如右边等于
$A^m(F_cH_c-F_dH_d)=A^{2m}(B_c-B_d)$，所以没有作未定义的算子除法。

固定圆盘内部的 $d$，把 (5.3) 除以 $c-d$。范数解析的首因子差商趋于
$F_d'G_d-F_dG_d'$；WOT 连续性给 $H_cH_d\to H_d^2$ WOT，因为右侧第二个因子固定。因此每个标量矩阵元
$$
c\longmapsto\langle A^{2m}B_cx,y\rangle
$$
在每点都有复导数，故为全纯函数。

$A$ 单射，所以 $\operatorname{Ran}(A^*)^{2m}$ 稠密。给任意 $y$，可取
$(A^*)^{2m}y_\nu\to y$。由 $\sup_{|c|\le1}\|B_c\|\le\|B\|$，
$$
\langle B_cx,(A^*)^{2m}y_\nu\rangle
=\langle A^{2m}B_cx,y_\nu\rangle
\longrightarrow\langle B_cx,y\rangle
$$
在每个紧参数集上一致。因此所有 $\langle B_cx,y\rangle$ 都全纯。

为明确从弱全纯提升到范数全纯，固定 $0<r<1$，按矩阵元定义 Cauchy 系数
$$
B_k=\frac1{2\pi i}\int_{|c|=r} B_c\,c^{-k-1}\,dc.
$$
统一范数界给 $\|B_k\|\le\|B\|r^{-k}$。标量 Cauchy 公式和此界说明
$$
\boxed{
B_c=\sum_{k\ge0}B_kc^k\quad(|c|<r)
}
\tag{5.4}
$$
按算子范数收敛。故 $B_c$ 的确是范数解析族。

## 6. Taylor 系数与 R85 轴除法迫使解析芽整除

展开
$$
F(z,w)=\sum_{k\ge0}f_k(z)w^k,\qquad
G(z,w)=\sum_{k\ge0}g_k(z)w^k,
\qquad g_0\not\equiv0.
$$
在一变量亚纯芽域中，形式 $w$ 商唯一：
$$
\frac FG=\sum_{k\ge0}r_k(z)w^k,
$$
其中递推为
$$
r_k=\frac{h_k}{g_0},\qquad
h_k=f_k-\sum_{j=1}^k g_jr_{k-j}. \tag{6.1}
$$
下面逐阶证明每个 $r_k$ 都是全纯 $z$ 芽，而不只是亚纯芽，并且
$$
B_k=r_k(A)Y^k. \tag{6.2}
$$

把 (5.4) 代入 $G_cB_c=F_c$，比较 $c^k$。假设较低阶已证明，则
$$
g_0(A)B_k=h_k(A)Y^k. \tag{6.3}
$$
此时 $h_k$ 是一变量收敛全纯芽。写
$$
g_0(z)=z^s u(z),\qquad u(0)\ne0.
$$
由 (6.3)，
$$
\operatorname{Ran}[h_k(A)Y^k]\subseteq\operatorname{Ran}A^s.
$$
若 $h_k=0$，单射性直接给 $B_k=0$。否则应用 R85 的精确 $A$ 轴除法到芽 $h_k(z)w^k$，得到 $z^s\mid h_k(z)$。所以
$r_k=h_k/g_0$ 确为全纯芽。再从 (6.3) 取消单射的 $g_0(A)$，得 (6.2)。$k=0$ 的同一论证是归纳起点。

于是所有 $r_k$ 都没有负 $z$ 幂，因而
$$
R_{\rm form}(z,w)=\sum_{k\ge0}r_k(z)w^k
\in\mathbb C[[z,w]],\qquad GR_{\rm form}=F. \tag{6.4}
$$
这里不从逐个 $r_k$ 的收敛直接猜测二变量收敛；使用 R66 已完整证明的形式可除性引理：
$$
F,G\in\mathbb C\{z,w\},\quad
F=GQ,\ Q\in\mathbb C[[z,w]]
\quad\Longrightarrow\quad Q\in\mathbb C\{z,w\}.
$$
该引理也可由 generic 线性坐标下的 Weierstrass 预备与解析除法、再以形式除法唯一性令余项为零来证明。

所以 $R=F/G$ 是真正的收敛全纯芽。其算子值满足
$G(A,Y)R(A,Y)=F(A,Y)$，由单射性
$$
\boxed{B=R(A,Y).} \tag{6.5}
$$
先前约去共同因子不改变分式，所以对原来的 $F,G$ 同样成立。

## 7. 真实范围包含与最大闭商的有界性

**定理 7.1。** 对任意非零芽 $F,G$，以下等价：

1. $\operatorname{Ran}F(A,Y)\subseteq\operatorname{Ran}G(A,Y)$；
2. 存在任意有界 $B\in B(H)$ 使 $G(A,Y)B=F(A,Y)$；
3. $F/G\in\mathbb C\{z,w\}$。

因子一旦存在就唯一为 $(F/G)(A,Y)$。

**证明。** 第 1 项中因 $G(A,Y)$ 单射，全域解 $B=G(A,Y)^{-1}F(A,Y)$ 的图闭：从 $x_n\to x$、$Bx_n\to y$ 可直接得到
$G(A,Y)y=F(A,Y)x$，所以 $y=Bx$。闭图定理使它有界。第 2 项到第 3 项是第 4—6 节；反向用解析商演算。证毕。

如果先给左因子关系 $BG(A,Y)=F(A,Y)$，由 $G(A,Y)$ 值域稠密，等式
$(BA-AB)G(A,Y)=0$ 迫使 $B$ 与 $A$ 交换，继而与 $Y,G(A,Y)$ 交换，所以同一判据也适用。

R85 对任意非零 $F,G$ 已给稠密定义最大闭算子
$$
T_{F/G}:\quad F(A,Y)u=G(A,Y)v,\qquad T_{F/G}u=v,
$$
并证明其自然图核心等于最大图、$T_{F/G}=CT_{F/G}^*C$。本条现在补齐
$$
\boxed{
T_{F/G}\text{ 有界}
\quad\Longleftrightarrow\quad
F/G\in\mathbb C\{z,w\}.
} \tag{7.1}
$$
这里若只先知道它在稠密定义域上有统一有界估计，其闭图就迫使定义域为整个 $H$，所以同样落入上述判据。

### 7.1 对实际非解析交换子的分母饱和性

记混合芽像
$$
\mathcal G_Y=\{F(A,Y):F\in\mathbb C\{z,w\}\}.
$$
若 $B\in\{A\}'$ 且存在非零 $G(A,Y)\in\mathcal G_Y$，使
$G(A,Y)B\in\mathcal G_Y$，则 $B\in\mathcal G_Y$。这排除了用非零混合解析分母，把一个本来不在 $\mathcal G_Y$ 中的有界交换子变成混合解析元素的可能性。

这不宣称整个 $\{A\}'$ 等于 $\mathcal G_Y$，也不把芽像的性质扩展到其任意范数闭包。

## 8. 全部混合芽闭商的谱三分法

令 $R=F/G$ 是非零亚纯芽，$T_R$ 取上述最大闭实现。

如果 $R$ 是常数 $\alpha$，则 $T_R=\alpha I$，谱为 $\{\alpha\}$。以下假设 $R$ 非常数。对每个 $\lambda\in\mathbb C$，
$F-\lambda G$ 为非零芽，R80/R85 给相应有界算子单射稠密。因此
$T_R-\lambda I$ 都单射且值域稠密，其反算子是最大闭商
$$
(T_R-\lambda I)^{-1}=T_{G/(F-\lambda G)}
=T_{1/(R-\lambda)}.
$$
图交换可直接验证该恒等式，包括定义域。故
$$
\boxed{
\lambda\in\rho(T_R)
\quad\Longleftrightarrow\quad
\frac1{R-\lambda}\in\mathbb C\{z,w\}.
} \tag{8.1}
$$

由此得到完整分类：

- 若 $R$ 全纯且非常数，则
  $$
  \sigma(T_R)=\{R(0,0)\}.
  $$
- 若 $R$ 非全纯而 $1/R$ 全纯，则
  $$
  \sigma(T_R)=\varnothing.
  $$
- 若 $R$ 与 $1/R$ 都非全纯，则
  $$
  \sigma(T_R)=\mathbb C.
  $$

证明只需芽环的单位判别。第一种情形，
$1/(R-\lambda)$ 全纯当且仅当 $\lambda\ne R(0,0)$。第二种令 $h=1/R$；必有 $h(0,0)=0$，于是
$1/(R-\lambda)=h/(1-\lambda h)$ 对每个 $\lambda$ 全纯。最后，如果某个
$h=1/(R-\lambda)$ 全纯：若 $h(0,0)\ne0$，则 $R=\lambda+1/h$ 全纯；若 $h(0,0)=0$，则 $1/R=h/(1+\lambda h)$ 全纯。两者都与第三种假设矛盾。

所有非常数情形的谱点都是连续谱，因为全部移位已证明单射且值域稠密。特别，
$$
\boxed{\sigma(A^{-1}Y)=\sigma(Y^{-1}A)=\mathbb C,}
$$
两者都取已证最小图等于最大图的实际闭实现。又
$\sigma(Y^{-1})=\varnothing$，与 R37 的明确逆算子结论一致。

### 8.1 正齐次自伴元素的区间谱

上述缩放同态还给一个直接的 $C^*$ 谱结论。若 $P=P^*\in\mathcal D$ 满足
$\sigma_r(P)=r^dP$（$0\le r\le1$，某个整数 $d\ge1$），则
$$
\sigma(P)=[\min\sigma(P),\max\sigma(P)].
$$
确实，含幺同态使 $\sigma(\sigma_r(P))\subseteq\sigma(P)$，故任意谱点 $t$ 与零之间的整段都属于 $\sigma(P)$。自伴谱是实紧集且在 $r=0$ 时含零；分别取其最小、最大值便填满整个区间。此结论适用于含 $Y,Y^*$ 的总次数为同一正数、系数来自 $\mathcal C$ 的自伴有限词和；不要求系数与 $Y^*$ 交换。特别地，
$$
\sigma(Y^*Y)=\sigma(YY^*)=[0,\|Y\|^2].
$$
这里是正算子的完整谱，不能由此推出 $A$ 的普通不变投影。

## 9. 与最小型补充及主问题的边界

R80 半群参考整轨道实际上满足对每个 $\varepsilon>0$ 的
$\|\mathfrak s(z)\|\le C_\varepsilon e^{\varepsilon|z|^2}$，因此任何非零向量轨道也不能有固定正系数的 Gaussian 衰减。完整证明已另存为
[二阶最小型与 Gaussian 障碍](../notes/2026-11-12-semigroup-minimal-gaussian-type-0c-agent.md)，状态为已证明的补充引理。

本条的商判据没有假设整个交换子都在已构造的 $C^*$ 代数中，也没有把未知有界因子先放进边界映射的定义域；酉共轭弱极限明确处理了这一点。解析性的恢复同样依靠固定 $A^{2m}$ 左乘、其伴随稠密值域及一致有界性，没有从变化的未闭范围直接推出。

新结论完整处理的是 $(A,Y)$ 的收敛解析芽和它们的亚纯商。一般非解析交换子结构、全部向量循环性及完整 Hilbert 不变子空间问题仍未解决。

