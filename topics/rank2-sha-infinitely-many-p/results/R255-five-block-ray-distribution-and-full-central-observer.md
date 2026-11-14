# R255 — 已付五块来源的实际分布矩阵与完整中央观察行

日期：2026-11-13。**状态：本文的原 ray 分布到 R250 五块来源的全部 trace、Gaussian 运输、准确 $3\times3$ 矩阵、原 $Y_B$ 行及完整除法均已证明。没有由对数乘积宣称代数独立，也没有证明原三曲线中央非零。**

本篇把[二挠对数分布笔记](../notes/2026-11-13-two-torsion-log-distribution-and-primitive-projection.md) 的实际来源，直接接到 [R250](R250-ray-mellin-transpose-and-original-e34-residual-pair.md) 的 $Y_B$。沿途使用 [R248](R248-ray17-conjugate-trace-and-original-yang-projections.md) 的真实共轭 CM17 迹及原有限矩阵。

## 1. 原分布来源先作真实共轭迹

保持前篇全部规范：
$$
\beta=4-i,\quad\bar\beta=4+i,\quad
\pi=2+i,\quad\bar\pi=2-i,\quad F=S_8^{17},
$$
$$
G_k=F(\beta z)B_k(z),\quad b_k=B_k(0)\ne0,
\quad T_k=[\bar\beta]_*(G_k/b_k),\qquad k=1,2,3.
$$
这里 $B_k$ 是原 $\lambda^k$ ray 二阶来源，不是 $E_{34}$ 截面 $B$。
对 $\alpha=\pi,\bar\pi$、$Q\in E_0[\alpha]$，定义实际全纯截面
$$
L_{\alpha,Q,k}(z)=F(\beta\alpha z)\frac{B_k(z+Q)}{b_k}.
$$
分布笔记已经逐项付掉其双极点。准确有
$$
\sum_QL_{\alpha,Q,k}
  =\mu_{\alpha,k}\alpha^2(G_k/b_k)(\alpha z),             \tag{1}
$$
其中
$$
(\mu_{\pi,1},\mu_{\pi,2},\mu_{\pi,3})=(-i,1,i),\quad
(\mu_{\bar\pi,1},\mu_{\bar\pi,2},\mu_{\bar\pi,3})=(1,-1,1).
                                                               \tag{2}
$$

令 $D_{\alpha,Q,k}=[\bar\beta]_*L_{\alpha,Q,k}$。这个度数为 $340$ 的截面用完整 frame 定义为
$$
D_{\alpha,Q,k}(z)=F(\alpha z)
\operatorname{Tr}_{\bar\beta w=z}
 \left[
 \frac{F(\beta\alpha w)}{F(\alpha\bar\beta w)}
 \frac{B_k(w+Q)}{b_k}\right].                            \tag{3}
$$
两个 CM 范数及半特征相同，故 (3) 是同线丛的有限平坦迹。
原 $B_k/b_k$ 已由 R248 给出完整有理式 $N_k(U)/D_\beta(U)^2$；
平移 $w\mapsto w+Q$ 使用固定椭圆曲线加法公式。
因此 (3) 指定了所有实际分支和全部系数，没有未选的 Gaussian 或 Haar 因子。

因 $(\alpha),(\bar\beta)$ 互素，pullback 与 trace 的 base change 给
$$
\boxed{\sum_QD_{\alpha,Q,k}(z)
       =\mu_{\alpha,k}\alpha^2T_k(\alpha z).}             \tag{4}
$$

## 2. cofactor 来源的准确三维分布矩阵

用 R250 的 primitive 系数矩阵 $A$、$\Delta=\det A\ne0$，令
$$
\boldsymbol Z=\operatorname{adj}(A)\boldsymbol T,
\qquad \boldsymbol T=(T_1,T_2,T_3)^t,
$$
$$
\mathsf D_\alpha=A^{-1}
    \operatorname{diag}(\mu_{\alpha,1},\mu_{\alpha,2},\mu_{\alpha,3})A.
                                                               \tag{5}
$$
所有九个系数均已准确计算并保存在输出中。它们不是待定矩阵，且满足
$$
\boxed{\mathsf D_\pi^4=I,\qquad
       \mathsf D_{\bar\pi}=-\mathsf D_\pi^2,\qquad
       \mathsf D_{\bar\pi}^2=I.}                         \tag{6}
$$
定义 $\boldsymbol E_{\alpha,Q}=\operatorname{adj}(A)
(D_{\alpha,Q,1},D_{\alpha,Q,2},D_{\alpha,Q,3})^t$，那么 (4) 就是
$$
\boxed{\sum_Q\boldsymbol E_{\alpha,Q}(z)
            =\alpha^2\mathsf D_\alpha\boldsymbol Z(\alpha z).}
                                                               \tag{7}
$$
R250 已证明
$$
\Pi_v Z_j=\Delta R_j+\delta_j\mathcal C,
\quad(R_1,R_2,R_3)=(H,S_{2312},S_{39304}),
$$
$$
\mathcal C=S_8(\beta z)+\nu S_8(\bar\beta z),\qquad\nu=1-4i.
                                                               \tag{8}
$$
因此 (7) 的 primitive 矩阵就是 $\mathsf D_\alpha$，CM 向量就是
$\mathsf D_\alpha\boldsymbol\delta$；输出同时列出这两个准确 CM 向量。

## 3. 将同一实际 dyadic 算子运输到分布来源

所有新旧型先按 R246 作共同 $[2]$ 拉回。在 degree-$272$ 上取任意一个已付的有限算子
$$
\mathcal Q=\Pi_v,\quad \mathcal V\Pi_v,\quad Q_{+,v}\Pi_v,
\qquad\mathcal Q=\sum_s c_s\mathcal T_s^{272}.
$$
定义其在 degree-$1360$ 上的**运输算子**
$$
\mathcal Q^{[\alpha]}=\sum_s c_s\mathcal T_{s/\alpha}^{1360}.
                                                               \tag{9}
$$
R246 的完整 Mumford 公式直接给
$$
\boxed{\mathcal T_{s/\alpha}^{1360}(f(\alpha z))
                     =(\mathcal T_s^{272}f)(\alpha z).}  \tag{10}
$$
线性指数与常数指数同时相等，因为 $N\alpha=5$。
这里固定实际复覆盖代表 $s/\alpha$；不把它无偿换成某个二原挠点。
(9) 在整个高层空间不必是投影。本篇只用它的实际有限展开和 (10)。

将 (7) 逐项作 $[2]$ 拉回并作用 (9)，便得
$$
\boxed{
\sum_Q\mathcal Q^{[\alpha]}\boldsymbol E_{\alpha,Q}(2z)
=\alpha^2\mathsf D_\alpha
       (\mathcal Q\boldsymbol Z(2z))(\alpha z).}          \tag{11}
$$
所以十二额外型的消去使用的是目标低层的真实 $\Pi_v$。
不需要假设高层每个单项已经落在原五维块中。

## 4. 完整中央分布矩阵

令 $d=p+1$、$U_\alpha=\alpha^d/5$，并定义三维中央列
$$
\boldsymbol J_{\mathcal Q}(u)
=\left(\mathcal J_{272c_0}(\mathcal QZ_j(2z);u)\right)_{j=1}^3,
$$
$$
\boldsymbol{\mathscr R}_{\alpha}^{\mathcal Q}(u)
=\sum_Q\mathcal J_{1360c_0}
        (\mathcal Q^{[\alpha]}\boldsymbol E_{\alpha,Q}(2z);u).
$$
由 (11) 及原完整 CM 缩放，准确有
$$
\boxed{\boldsymbol{\mathscr R}_{\alpha}^{\mathcal Q}(u)
       =\alpha^2U_\alpha^u\mathsf D_\alpha
                              \boldsymbol J_{\mathcal Q}(u).}
                                                               \tag{12}
$$
这就是原分布与已付五维来源之间的直接等式。$\alpha^2$、$U_\alpha^u$、
$\mathsf D_\alpha$ 和全部二处运输都保留。

例如中央求导是
$$
(\boldsymbol{\mathscr R}_{\alpha}^{\mathcal Q})'(0)
=\alpha^2\mathsf D_\alpha
 \left(\boldsymbol J_{\mathcal Q}'(0)
              +\log_pU_\alpha\boldsymbol J_{\mathcal Q}(0)\right).
                                                               \tag{13}
$$
它没有把参考的未知导数或质量缩放藏进一个重新选择的常数。

## 5. 与实际 balanced CM5 行的直接比较

在五维像内，置 $\Lambda=\operatorname{diag}(i,-1,-i)$。由 R248 的准确特征值，截面恒等式为
$$
\mathscr N(\Pi_v\boldsymbol Z)
=\Lambda\Pi_v\boldsymbol Z+(I-\Lambda)\boldsymbol\delta\mathcal C.
                                                               \tag{14}
$$
对 (14) 先作用同一个 $\mathcal Q$ 再取中央行，并使用 R250 的实际非零核转置，得到
$$
\boxed{
\boldsymbol K_{\mathcal Q}(u)
=(\Lambda-r_p(u)I)\boldsymbol J_{\mathcal Q}(u)
 +(I-\Lambda)\boldsymbol\delta J_{\mathcal Q}(\mathcal C;u),}
                                                               \tag{15}
$$
其中 $r_p(u)=\pi^{-1}(U_{\bar\pi}/U_\pi)^u$。
这一步没有要求 $\mathcal Q$ 与 $\mathscr N$ 交换：先使用 (14) 的真实截面等式即可。

将 (12) 代入，得到完全显式的 raw/balanced 比较
$$
\boxed{
\boldsymbol K_{\mathcal Q}
=(\Lambda-r_pI)\alpha^{-2}U_\alpha^{-u}
                 \mathsf D_\alpha^{-1}
                    \boldsymbol{\mathscr R}_\alpha^{\mathcal Q}
 +(I-\Lambda)\boldsymbol\delta J_{\mathcal Q}(\mathcal C).}
                                                               \tag{16}
$$
两个不同迹的特征值没有被互换；它们之间的完整矩阵和 CM 修正现已算出。
输出还给出 primitive 比较矩阵
$\pi^2\mathsf D_\pi-\pi\Lambda$ 及 CM 向量
$\pi^2\mathsf D_\pi\boldsymbol\delta-\pi\boldsymbol\delta$。

## 6. 原 $Y_B$ 的两条实际分布行

现在固定 $\mathcal Q=Q_{+,v}\Pi_v$，使用 R250 的非零 $\delta_2$。
令 $q_2=2^{p-1}$、$J_0=\mathcal J_{4c_0}(F_0)$，并定义明确的实际分布观察
$$
\mathscr R_\alpha^B(u)=
\frac{\alpha^{-2}
       [\mathsf D_\alpha^{-1}
          \boldsymbol{\mathscr R}_\alpha^{\mathcal Q}(u)]_2}
     {2\kappa_4\delta_2 q_2^uJ_0(u)}.
                                                               \tag{17}
$$
全部分子来自 (3)、(9) 指定的实际 theta 来源；分母是 R250 已付的同一个参考单位与固定非零代数常数。
由 (12)，
$$
\boxed{\mathscr R_\pi^B=U_\pi^uY_B(u),\qquad
       \mathscr R_{\bar\pi}^B=U_{\bar\pi}^uY_B(u).}       \tag{18}
$$
准确有 $Y_B(0)=\nu-1=-4i$。

若将 (15) 的第二行也除以 (17) 的同一个低层参考单位，记为 $K_B$，则
$$
\boxed{K_B=(-1-r_p(u))Y_B
                 +2(-U_-^u+\nu U_+^u),}                 \tag{19}
$$
其中 $U_-=\beta^d/17,U_+=\bar\beta^d/17$。
因此 (18)、(19) 给出原 $Y_B$、raw distribution 及 balanced theta trace 三者之间的完整解析关系，CM 右端可明确求导。

## 7. 一阶、二阶与完整除法的准确区别

令
$$
\mathscr D_B=\mathscr R_\pi^B-\mathscr R_{\bar\pi}^B,
\quad\ell_5=d\log_p(\pi/\bar\pi)\ne0.
$$
由 (18)，整条等式为
$$
\boxed{\mathscr D_B(u)=(U_\pi^u-U_{\bar\pi}^u)Y_B(u).}   \tag{20}
$$
所以
$$
\mathscr D_B'(0)=-4i\ell_5,
$$
$$
\boxed{\mathscr D_B''(0)=
 2\ell_5Y_B'(0)-4i(p-1)\log_p5\,\ell_5.}                \tag{21}
$$
第一式只看到了质量；第二式才含目标观察 $Y_B'$。
这里用了 $U_\pi U_{\bar\pi}=5^{p-1}$，没有省略对数交叉项。

也可以不截断地除去已知简单零。置
$$
\mathcal E_5(u)=\frac{U_\pi^u-U_{\bar\pi}^u}{u\ell_5}.
$$
该函数在 $u=0$ 可去，$\mathcal E_5(0)=1$；因为
$$
\mathcal E_5(u)=U_{\bar\pi}^u
       \frac{\exp(u\ell_5)-1}{u\ell_5},
$$
而 $v_p(\ell_5)\ge1$，它在完整原 Tate 代数中是解析单位。于是
$$
\boxed{\frac{\mathscr D_B(u)}{u\ell_5\mathcal E_5(u)}=Y_B(u).}
                                                               \tag{22}
$$
(22) 保留了分子 (17) 的实际来源及完整参考分母。
标量 $1/\ell_5$ 是一个随 $p$ 变化的 $p$ 进数，本篇不声称它是代数数或整单位；
也不把 (22) 的除法后观察重新称为一个未经除法的固定 theta 来源。

若三个原中央导数都为零，R250 (31)–(32) 进一步给
$$
Y_B'(0)=-2i(p-1)\log_p17
                    +(1-2i)d\log_p\frac{4+i}{4-i}.       \tag{23}
$$
结合 (21)，得到具体待比较的完整行
$$
\boxed{
\frac{\mathscr D_B''(0)}{2\ell_5}
=-2i(p-1)(\log_p5+\log_p17)
 +(1-2i)d\log_p\frac{4+i}{4-i}.}                         \tag{24}
$$
右边是三个固定代数数（均为目标 $p$ 位的单位）的对数的代数系数线性型。
有限位 $5$ 与两个 $17$ 素位说明这三个数乘法独立，故 Brumer 可用于这个**已经提取共同非零因子后的线性型**。
它不证明 $\ell_5\log_p17$ 等对数乘积的代数独立。

(24) 目前是三曲线失效时实际 distribution 二阶观察必须满足的等式。
与新固定单位对数作进一步比较时，必须保留左端的 $1/\ell_5$、原始分子及参考单位；
不能只引用固定单位对数的线性独立，就把一个任意二阶 Mellin 行视为同一线性型。

## 精确证书

[脚本](../scripts/check-five-block-ray-distribution-matrices.py) 和
[输出](../scripts/check-five-block-ray-distribution-matrices.json)
列出全部 $\mathsf D_\pi,\mathsf D_{\bar\pi}$、CM 向量及 raw/balanced 比较矩阵。
它们在 $\mathbf Q(i)$ 中核验 (5)–(6)，使用的实际 $A$ 来自 R248 的已证明数值。
(3)、(9)、(10) 明确给出这些有限矩阵所对应的全局来源；
完整中央结论由这些截面恒等式及前篇已证明的 Mellin 缩放推得。
