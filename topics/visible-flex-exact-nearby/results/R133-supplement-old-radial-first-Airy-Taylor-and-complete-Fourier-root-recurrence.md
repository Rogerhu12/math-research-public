# R133 续篇：第一 Airy 修正的旧径向 Taylor 递推与完整 Fourier 根系数

2026-11-14，phase_inverse。

**精确解析合同。** 本篇把
[leading 矩阵归一化后的真实第一修正](R133-supplement-exact-first-Airy-root-jets-and-Taylor-tail-derivatives.md)
直接拉回旧 $(\rho,\phi)$ 坐标，在原根上求完整角函数的
Taylor 系数。它避免先反解角图再对两个坐标作粗二阶链估计。
修正、强迫、原参数族与真实物理接缝完全不变。

数值入口是新
[真实根高 intrinsic jets](R133-supplement-true-root-high-intrinsic-jets-from-complete-auxiliary-errors.md)
及已实际完成的
[较大辅助折叠与第一幅度](R133-supplement-actual-larger-anchored-auxiliary-fold-with-preserved-prefix.md)。
新根 Fourier 与 Taylor 消费尚须公开 Actions 实际执行；
本篇不先授最终 strong 常数或 cutoff97。

## 1. 固定真根和完整角代数

保持原固定 $\eta_0$、原真根 $r_*$ 及整个允许复 $|\delta|\le10^{-8}$。
记 $\rho=r_*-r$；在该根 germ 上紧支参数 bump 恒为零，
intrinsic 系数保持同一原定义。原宽参数输入盒可作为更宽
数值包络，但本篇不对其它 intrinsic 参数授同一个根。

所有径向 Taylor 系数都除以阶乘：
$$
 f(\rho,\phi)=\sum_{p\ge0}f_p(\phi)\rho^p.
 \tag{P.1}
$$
角代数使用完整 $4\mathbb Z$ 模，写
$f_p=\sum_j f_{p,j}e^{4ij\phi}$。
原 $u$ 含全部96个 sine 分量，$v$ 含全部96个 cosine 分量及
独立真实 mean。原 M32 基点的65列与方向的193列均完整保留。

原 cubic 系数在真根区间上重新取一次点值及前三普通导数，
正阶 value repair 导数严格为零，零阶修补照原合同加入。
若只保存某个方向常数修补的完整上界，就用该上界包围准确修补，
不能用零代替。$v$ 的 mean 还含同一 $s(r)$ 的全部所需根导数。
径向方向转换是
$$
 u_p=\frac{(-1)^p}{p!}\partial_r^pu(r_*,\cdot),\qquad
 v_p=\frac{(-1)^p}{p!}\partial_r^pv(r_*,\cdot).
 \tag{P.2}
$$
前三阶以后的非mean cubic 系数准确为零；
这不删除 $v$ 的高阶 intrinsic mean。

所需乘积使用完整非循环 Laurent 卷积。角导数乘 $4ij$；
已知系数的 primitive 为
$$
 If=\sum_{j\ne0}\frac{f_j}{4ij}e^{4ij\phi},\qquad (If)_0=0 .
 \tag{P.3}
$$
(P.3) 仅构造已知 drift，不是把原未知量上的 $I/J$ remainder
删掉。$S$ 的 mean 在下文的 $\eta,T_0,G,V_0$ 和独立 mean 行
继续出现。

## 2. 由真根 intrinsic 列构造原完整系数

使用原已付 $K(r_*)=0$，先保存未改写的真实新 $K_0$ ball，
再在真根视图用准确零值。设
$$
 k(\rho)=-K(r_*-\rho)/\rho,\quad
 m=\langle v\rangle,\quad \eta=-\gamma m,\quad
 a=\eta\sqrt{k},\quad S=u^2+Kv^2,
$$
$$
 d=-\beta I S,\qquad e_d=-d .
 \tag{P.4}
$$
这里 $k,\eta,a$ 是径向标量；$d,S$ 是完整角函数。
准确 $\rho$ series 的 $k_p=(-1)^pK^{(p+1)}(r_*)/(p+1)!$。
所有平方根和分数幂取既成根证书的同一正实部解析分支。

有限 series 的乘积、逆、指数和分数幂按准确 coefficient 递推。
对 $f_0$ 为非零径向标量的 $f$，先写
$f=f_0(1+h)$，$h_0=0$。其 $p$ 次系数只需
$\sum_{q=0}^p\binom{\alpha}{q}h^q$。
不得对不够长的输入 series 以零补齐后索取未付的高阶系数。

根高 jets $K$ 至9阶、$\beta,\gamma,s$ 至9阶足够本篇的
leading 至 $\rho^8$、完整第一强迫至 $\rho^6$ 及第一修正至
$\rho^6$。例如 $k$ 至8阶正好使用 $K$ 至9阶，
而 leading 的两次径向导数使强迫第6阶使用 leading 第8阶。

## 3. 原 fold 的三角根递推

写 $X=\phi+\chi$，$\chi_0=0$，$A_0=a_*=a(0)$。
真实原 fold 的两个方程是
$$
 X_\rho=e_dX_\phi+\frac23a\rho^2A_\phi,\qquad
 2\rho A_\rho+3A=2\rho e_d A_\phi+3aX_\phi .
 \tag{P.5}
$$
对 $p\ge0$，
$$
 \chi_{p+1}
 =\frac{[e_d(1+\chi_\phi)]_p+
                   \frac23[aA_\phi]_{p-2}}{p+1},
 \tag{P.6}
$$
$$
 A_p=
 \frac{2[e_dA_\phi]_{p-1}+3[a(1+\chi_\phi)]_p}{2p+3}.
 \tag{P.7}
$$
负下标系数为零。按 $A_0,\chi_1,A_1,\chi_2,A_2,\ldots$ 的顺序
计算，右侧都只使用已经得到的系数；
(P.6) 的第二项从真实 $\rho^2$ 才开始。

然后
$$
 T=-\rho A^{2/3},\quad Q=aA^{-1/3},\quad
 B=X_\phi^2-TT_\phi^2,\quad \mu=Q^2B,
 \tag{P.8}
$$
$$
 G=(A/a_*)^{1/6}(k/k_*)^{-1/4}E_G,\qquad
 (E_G)_\rho=2\beta\langle S\rangle E_G,\quad E_G(0)=1,
$$
$$
 a_0^{\rm Airy}=GB,\qquad
 b_0^{\rm Airy}=-2i\epsilon GX_\phi T_\phi,\qquad
 \epsilon\in\{-1,1\}.
 \tag{P.9}
$$
归一化形式给 $G(0)=a_0^{\rm Airy}(0)=1$ 准确成立。
$A/a_*$、$k/k_*$ 的零阶等于1是同一函数的结构恒等式，
不是把不相关区间除法的结果强行取中心。
其余系数仍使用完整有向除法。
由 (P.5)--(P.8)，$T_\phi=O(\rho^2)$，
故 $b_0^{\rm Airy}=O(\rho^2)$，不只是在浮点输出中观察到小。

下文将 leading 两列简记为 $a_0,b_0$。
(P.9) 的径向指数包含全部 $\langle S\rangle$，
不能以 $S_\perp$ 替代。

## 4. 原完整 degree-zero 强迫的根 Fourier 列

物理方向固定为
$$
 D=\partial_r-d\partial_\phi=-\partial_\rho-d\partial_\phi .
 \tag{P.10}
$$
因此
$$
 D^2w=w_{\rho\rho}+2dw_{\rho\phi}
       +(d_\rho+dd_\phi)w_\phi+d^2w_{\phi\phi}.
 \tag{P.11}
$$
保原
$$
 \ell=-2\beta uv,\quad e=-\beta(1+3u^2+Kv^2),\quad
 b_{\rm loc}=\beta(1-u^2-3Kv^2),
$$
$$
 t_Q=-\eta_\rho/\eta+d_\phi+e,\qquad
 T_0=-\eta_\rho/\eta-4\beta\langle S\rangle+5d_\phi ,
$$
$$
 r_Q=D\ell+\eta e_\phi-2\beta\eta u_\phi u
                   -\ell(-\eta_\rho/\eta+d_\phi),
$$
$$
 \vartheta=r_Q/\eta-2\beta Kvv_\phi,\qquad
 V_0=t_Qb_{\rm loc}-Db_{\rm loc}
                  -K(\ell^2-4\beta\eta vu_\phi).
 \tag{P.12}
$$
这里 $b_{\rm loc}$ 与 $b_0^{\rm Airy}$ 是不同对象。

由已证的完整 $H^{-1}H_D=-i\epsilon Q
\left(\begin{smallmatrix}0&T\\1&0\end{smallmatrix}\right)$，
准确强迫为
$$
 \binom{F_b}{F_a}
 =-\mu^{-1}\left[
 (D^2+\eta^2K\partial_\phi^2-T_0D+V_0)
                         \binom{a_0}{b_0}
   +i\epsilon\vartheta Q\binom{Tb_0}{a_0}\right].
 \tag{P.13}
$$
角导、径向导、$r_Q$ 和两行 cross term 全保留。
(P.13) 是原 local degree-zero 强迫；它并不声称原 old-circle
projected operator 等于这个 local 表达式。

## 5. 不先反解角图的真实归一化 transport

取
$$
 M_0=\begin{pmatrix}a_0&Tb_0\\b_0&a_0\end{pmatrix},\quad
 \binom{\mathcal A}{\mathcal B}=M_0^{-1}\binom{a_1}{b_1},
 \quad
 \binom{f_b}{f_a}=M_0^{-1}\binom{F_b}{F_a}.
 \tag{P.14}
$$
这是同一个已经证明可逆的 leading 矩阵，
不是将 $B$ 或真正偶 mean 方程吸收为一个新未知。
$M_0(0)=1$，其 finite series inverse 在根逐阶准确确定。

记旧坐标 Jacobian
$$
 \mathcal J=T_\rho X_\phi-T_\phi X_\rho,\qquad
 \mathcal J_*=-a_*^{2/3}=-Q_* .
 \tag{P.15}
$$
原 $\rho$ 方向使 $\mathcal J_*$ 为这个负号。
真正 inverse coordinate derivatives 是
$$
 \partial_T=\mathcal J^{-1}(X_\phi\partial_\rho-X_\rho\partial_\phi),
 \qquad
 \partial_X=\mathcal J^{-1}(-T_\phi\partial_\rho+T_\rho\partial_\phi).
$$
将原归一化系统 (J.6) 乘以 $\mathcal J$，准确得到
$$
 2X_\phi\mathcal A_\rho-2X_\rho\mathcal A_\phi
  +2i\epsilon T(-T_\phi\mathcal B_\rho+T_\rho\mathcal B_\phi)
       =\mathcal J f_a ,
 \tag{P.16}
$$
$$
 2TX_\phi\mathcal B_\rho-2TX_\rho\mathcal B_\phi+\mathcal J\mathcal B
  +2i\epsilon T(-T_\phi\mathcal A_\rho+T_\rho\mathcal A_\phi)
       =\mathcal J f_b .
 \tag{P.17}
$$
根条件为 $\mathcal A_0=0$，$\mathcal B_0=f_{b,0}$。
这两个方程是原同一解析 $w_1$ 的拉回，不产生第二个修正族。

## 6. 直接旧 $\rho$ 的系数递推

分离 $X_\phi(0)=1$、$T=\mathcal J_*\rho+O(\rho^2)$、
$T_\phi=O(\rho^2)$，得到
$$
\begin{split}
 \mathcal A_{p+1}
 =\frac1{2(p+1)}\big[
 &\mathcal J f_a+2X_\rho\mathcal A_\phi
     -2(X_\phi-1)\mathcal A_\rho\\
 &+2i\epsilon TT_\phi\mathcal B_\rho
     -2i\epsilon TT_\rho\mathcal B_\phi
                      \big]_p ,
\end{split}
 \tag{P.18}
$$
$$
\begin{split}
 \mathcal B_p
 =\frac1{\mathcal J_*(2p+1)}\big[
 &\mathcal J f_b+2TX_\rho\mathcal B_\phi
      -2(TX_\phi-\mathcal J_*\rho)\mathcal B_\rho
      -(\mathcal J-\mathcal J_*)\mathcal B\\
 &+2i\epsilon TT_\phi\mathcal A_\rho
      -2i\epsilon TT_\rho\mathcal A_\phi
                      \big]_p .
\end{split}
 \tag{P.19}
$$
按 $\mathcal B_0,\mathcal A_1,\mathcal B_1,\mathcal A_2,\ldots$
计算。在 (P.18)，含 $\mathcal A_\rho$ 的乘数从 $\rho$ 开始；
含 $\mathcal B_\rho$ 的乘数从 $\rho^3$ 开始。
在 (P.19)，$TX_\phi-\mathcal J_*\rho$ 从 $\rho^2$ 开始，
$\mathcal J-\mathcal J_*$ 从 $\rho$ 开始。
所以所有右侧只需之前已经确定的系数。
没有把当阶未知项当零而漏掉一个隐式方程。

最后准确重构
$$
 a_1=a_0\mathcal A+Tb_0\mathcal B,\qquad
 b_1=b_0\mathcal A+a_0\mathcal B .
 \tag{P.20}
$$
(P.18)--(P.20) 的 $\phi$ 是旧物理角。
它们无需把旧 primitive 当成逐 $T$ primitive，
也不对原投影或 even mean 作任何角坐标偷换。

作为固定号数检查，若 $T=\mathcal J_*\rho$、$X=\phi$ 且
leading 恒为 $(1,0)$，则
$\mathcal A_1=\mathcal J_*F_a/2$、
$\mathcal B_p=(f_b)_p/(2p+1)$，与原 canonical 递推经
$T=\mathcal J_*\rho$ 的变换完全一致。

## 7. 完整 finite Fourier 支持及有向 norm

原 $u_p,v_p$ 的非mean Fourier 指数 $|j|\le96$；
$d_p$、$S_p$ 的指数 $|j|\le192$。由 (P.6)--(P.7) 归纳，
$$
 \deg_\phi\chi_p,\ \deg_\phi A_p\le192p .
 \tag{P.21}
$$
角导数不改变支持，径向标量不增加支持，
零阶为标量的逆或幂的第 $p$ 项也满足同一加法支持规则。
所以
$$
 \deg_\phi(F_b)_p,\ \deg_\phi(F_a)_p\le192(p+2),
$$
$$
 \deg_\phi(a_1)_p\le192(p+1),\qquad
 \deg_\phi(b_1)_p\le192(p+2).
 \tag{P.22}
$$
这些是数学支持上界，不是观测到的小尾。
例如 $p\le6$ 时保到完整 $|j|\le1536$ 即包括全部真实输出。
若用多项式快速乘法，必须先偏移成普通多项式、做完整卷积，
再恢复 Laurent 指数；不能用长度不足的循环 FFT。

一个包围全部系数的有向 Fourier 数组立即给
$$
 C_{p,q}(\sigma)=
 \sum_j |(w_1)_{p,j}|(4|j|)^q e^{4|j|\sigma},
 \tag{P.23}
$$
其中 $q=0$ 保真实 mean，$q>0$ 时 mean 导数准确为零。
两个 $\epsilon$ 分支应分别完成，或用保持完整复参数共轭身份的
严格论证复用；不能从实基点数值对称猜复参数分支相同。

已成根 intrinsic native 原 arrays 和误差不能重算。
新 consumer 只增加原两 cubic 在真根点的 finite coefficients、
(P.6)--(P.23) 的新 finite algebra 和下面的新域门。
每个完成的 fold degree、forcing degree 和 transport degree
保存 exact native；同源恢复逐阶复用。

## 8. 只对真旧坐标 Taylor 尾付原完整 supremum

设已成较大辅助 native 给 canonical 域
$|T|\le R_T,\ |\operatorname{Im}X|\le\Sigma_V$ 上的真实幅度上界
$M_a,M_b$，以及同 old-product 域上的 $A_+$、$|X_\rho|\le C_X$。
选一个新旧径向圆半径 $R_\rho$ 和旧角宽 $\Sigma_\phi$，
公开有向消费必须核
$$
 R_\rho<R_{\rm fold},\qquad
 R_\rho A_+^{2/3}<R_T,\qquad
 \Sigma_\phi+R_\rho C_X<\Sigma_V .
 \tag{P.24}
$$
并核旧 product 圆包含在原已付辅助解析域内。
由于 $X(0,\phi)=\phi$，最后一式由沿旧径向积分得到。
这是正向 image 门，不把 canonical 逆矩形误当旧 product 域。

(P.24) 证明 $w_1(T(\rho,\phi),X(\rho,\phi))$ 在整个旧 product 圆
有同一 $M_a,M_b$ 上界。它与真物理修正的认同仅限原 piece
和原实根邻域；辅助圆可越过物理拼接位置，但不把相邻物理
多项式替换成这个解析延拓。

对 $\sigma<\Sigma_\phi$、$r<R_\rho$，使用 (P.23) 的前 $p+1$
个实际根系数，只对未算尾作 Cauchy：
$$
 \|\partial_\rho^u\partial_\phi^q w_1\|_{\sup,\sigma}
 \le \sum_{k=u}^{p}\frac{k!}{(k-u)!}C_{k,q}(\sigma)r^{k-u}
  +\frac{q!M_w}{(\Sigma_\phi-\sigma)^qR_\rho^u}
       \mathcal T_{p,u}(r/R_\rho),\qquad 0\le u\le2,
 \tag{P.25}
$$
其中 $\mathcal T_{p,u}$ 是原 (J.18)--(J.19) 的完整几何尾。
若需要 Wiener 而非 strip sup 窗，必须再给正的角宽差，
例如乘完整 Fourier 求和
$\sum_{j\in\mathbb Z}e^{-4|j|\Delta_\phi}$；
不得把尾的 sup 上界直接当同宽 Wiener 上界。

(P.25) 已是旧坐标导数：$\partial_r=-\partial_\rho$，
二阶不改变号，范数也不增加 coordinate chain 费用。
真实物理 inner cover 中的 $r=\sup|\rho|$ 必须包含原根 bracket
的全宽，不能只写名义 $h=9\cdot10^{-6}$。

完整 $\mathcal L_0w_1$ 使用 (P.11)--(P.13) 的全部项；
原 old-circle $I/J$ 和独立 even mean 则接
[准确 mean 压缩与第一修正非局部预算](R133-supplement-exact-old-mean-compression-and-first-correction-nonlocal-budgets.md)。
两者没有被有限 Fourier 根递推提前清零。
全1079个真实 seam、外侧 one-sided jets、正区七输入端口、
finite head 与未知 high feedback 继续保持原独立合同。
