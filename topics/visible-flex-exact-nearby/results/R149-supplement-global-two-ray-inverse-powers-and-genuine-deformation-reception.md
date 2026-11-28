# 全负域原矩阵逆的幂与两真 Airy 行对变形的实际接收

记 $u=-T$, $y=T_\phi$, $x=X_\phi$，$\epsilon=\operatorname{sgn}j$，$n=4|j|\ge388$。沿用 [GDG.17–20](R133-supplement-complete-global-genuine-determinant-from-supported-potential.md) 的 $B_j,H_\epsilon^{-1}$ 与原二维欧氏范数。在原全实参数域与全部负区径向圆上，
$$
 \|B_j\|,\ \|H_\epsilon^{-1}\|<64,\qquad
 \|B_j^k\|,\ \|H_\epsilon^{-k}\|<
 {21\over2\sqrt{20}}27^k\qquad(k=1,2,\ldots).                      \tag{GIB.1}
$$
这里的幂是同一物理点上连续的矩阵乘积。

在 $\rho\le1/50$，GDG.18 的分量总和已小于 $21/10$。在其余区域 $B_j=H_\epsilon^{-1}$ 且 $1/20<u<19$，$p_\pm\in(1/27,27)$，见 [GAF.2](R149-supplement-all-frequency-two-ray-physical-bound-for-both-genuine-Airy-rows.md)。令 $D=\operatorname{diag}(1,\sqrt u)$，则 $D H_\epsilon D^{-1}=i\epsilon x I+\sqrt u\,y J$，$J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$；其两个特征值是 $i\epsilon p_\pm$，按 $\epsilon$ 排列。因为 $p_\pm=x\pm\sqrt u\,y$，两个谱投影在原物理内积中的范数都是
$$
 \|\Pi_\pm\|={1\over2}\sqrt{(1+u)(1+1/u)}
       ={1\over2}(\sqrt u+1/\sqrt u)\le21/(2\sqrt{20}).
$$
此式在两特征值相等处仍可按同一 $J$ 的两个投影分解。乘共同模一数后，$H_\epsilon^{-k}$ 等于 $p_+^{-k}\Pi_++p_-^{-k}\Pi_-$。将两标量除 $27^k$ 后落在单位正方形；其四个顶点分别给 $0,\Pi_+,\Pi_-,I$，由算子范数的凸性得 (GIB.1)。

## 直接收在原剖面与原参考输入上的矩阵

令 $W(r,\phi)$ 是任意两分量物理幅，可为复数，记 $W_*=\max_\ell\|W_\ell\|_\infty$。令 $D_n=\operatorname{diag}(1,n^{-1})$。对任意输入标签集合 $S\subset\{|j|\ge97\}$，定义原剖面上的整项
$$
 \mathcal E_W f=\sum_{j\in S} e^{4ijX}
    [\, n^2(B_j-H_\epsilon^{-1})W\,]^t D_n\Psi_n(T) f_j,\qquad
 f_j\in\mathbb C^2 .
$$
这里为向量的双线性行作用；无需实值假设施于输入。则
$$
 \|\mathcal E_W:\ell^2(S;\mathbb C^2)\longrightarrow L^2_\phi\|
       \le {W_*\over2500}.                                             \tag{GIB.2}
$$
同一 $W_*$ 若统一控制各 $r$，普通 $L^2(dr;L^2_\phi)$ 与 $L^1(dr;L^2_\phi)$ 费用分别至多 $W_*/175000$、$W_*/12500000$。亦可在每个确切 $r$ 使用其自身的 $W_*(r)$。频率对角的独立右输入因子可带自身上确界接入。

在存在非零矩阵变形的径向圆上，[BPF.2–3](R149-supplement-whole-genuine-inverse-deformation-on-the-physical-Fourier-space.md) 给 $\rho<1/5000$、$|y|\le Y=7/10^7$、$D_0=977/1000$ 为自由行列式正下界、$H_0=21/10$ 为自由逆完整条目和上界。整圆的真实 $p_\pm$ 落在 $(79/80,81/80)$。从根到这里的每个共同漂移点也在同窗中；用 GAF.2 的同一正积分得
$$
 u_{\max}/u_{\min}\le(81/79)^{2/3},\qquad
 \log(u_{\max}/u_{\min})<1/50,\qquad u_{\max}<1/1900 .
$$
最后一步用至少一点在 $u<L=1/2000$ 且 $(81/79)^{2/3}<2000/1900$。GAF 对两真实相位的证明在此处给更小的完整剖面费：高度振幅至多 $1$，导数振幅上界 $n^{-1/3}(1+n^{2/3}u)^{1/4}\le\sqrt{388^{-2/3}+1/1900}<1/7$。两者的对数变差系数分别为 $1/2,5/8$。用 $\sqrt{80/79}$ 替换 $\sqrt{27}$ 后，含完整 $Z_n$ 的两个真实状态行，分别有范数上界
$$
 \sqrt{160/79}\,[\tfrac65(1+1/100)+13/388]<9/5,\qquad
 {\sqrt{160/79}\over7}[\tfrac65(1+1/80)+13/388]<9/5 .
$$
根点直接取原剖面行；$\rho=0$ 时 $y=0$。

现在在每个矩阵条目上使用 BPF.6 的同一几何级数。把 $H_\epsilon^{-1}=H_e+\epsilon H_o$ 分开并将符号留在原输入端。对任一项 $(m+1)$ 的 $V(z_j,T_c)$ 幂，BPF.4 的水平集积分在原剖面**外侧**给公共物理乘子，在原两分量输入**右侧**给标量频率对角。在这两者之间正是上面估过的完整剖面行，并可逐条目乘真实 $W_\ell$。因此 $W_*$ 外的总费用小于
$$
 {9\over5}{Y(1+8YH_0)\over D_0}
 \left[{M\over1-q}+{LM_1\over(1-q)^2}\right]<1/2500,\qquad
 q={MY^2\over388^2D_0}<10^{-12}.
$$
这里 $M=276,M_1=26431$。主矩阵 $E_{12}$ 只有一个条目；另两共同矩阵各至多四条目，每条上界 $H_0$，故系数八覆盖了不同条目上确界的位置差。真实 $C^{64}$ 截断与 $W_\ell$ 一并在物理左侧。该推导没有把两个已取范数的傅里叶算子相乘，也没有对调 $\Psi_n,B_j$；潜势为零时，无论 $W$ 或真实 $\Psi_n$ 大小，该差均为零。径向费用直接由 $\rho<1/5000$ 得到。

(GIB.2) 给有真实剖面的原矩阵变形项；全源中完整 $B_j$ 的自由部分、强迫幅本身、其角导及原各状态端点尚按相应的实际项计算。
