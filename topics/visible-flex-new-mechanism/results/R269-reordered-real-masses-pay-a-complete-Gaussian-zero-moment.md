# R269：改变真实高低次序并支付完整 Gaussian 面积的第零外矩

日期：2026-11-15。**完整纸面建设性证明；没有执行 profile 求积、扫描、消元、人工测试或几何计算。**

本稿接 [R256 六能量构造](R256-sharp-profile-energy-contrast-and-multiwidth-joint-construction.md)、[R265 伴随正号 block](R265-companion-directions-and-positive-blocks-pay-an-ordered-Gaussian-area.md)、[R267 母幅/宽联合门](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)及 [R268 居中 cell 的 sine-four 障碍](R268-full-sine-four-area-obstruction-for-centered-microcells.md)。新增变化是实际高包的次序，不只是改变共同平移、幅度或原 cell 内符号。

结论是：存在真实正宽圆，同时支付三矩、全部第三、六能量、整个 $A_{-2,-3}$ 与 $A_{-1,-3}$、全部 Gaussian odd 条件，以及 $A_{1,-3}$ 的**整个第零外矩**。最后一步用四个已经完整合法的 block，先各次序支付 pure 标量，再以正四次幅度支付 sine-four。没有将一个 scalar 的零冒称该面积三个外矩全部为零。

来源还包括 [R257 原 primitive 量](R257-cumulative-primitive-energy-in-the-complete-positive-negative-Gaussian-area.md)与 [R259 全槽有序表](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)。

## 1. 固定幅度、宽度和一个新的实际次序

保持 R256 的

$$
n=2^{11},\quad N=64n,\quad
q_0=\frac1{16(1-\alpha)^2},\quad
\beta=\frac{5-\alpha}{1-\alpha},\qquad
\frac13\le\alpha\le\frac12.
$$

低包的系数、宽度为
$(a_i,b_i)=(\epsilon_i\sqrt{\alpha q_0},\sqrt{q_0})$、$q_0$；
高包为 $(\epsilon_k\sqrt\beta,1)$、$1$。
$\epsilon_j=(-1)^{\operatorname{popcount}(j)}$。
这是主宽 $\delta$ 尚未乘入的 shape 坐标。

低中心保持

$$
t^L_{k,l}=64A(k-c)+A(l-31.5),\qquad
c=(n-1)/2,\quad0\le l\le63.
\tag{1}
$$

新的高中心为

$$
\boxed{
t^H_k=B(k-c)+\rho A\sigma_k,\qquad
\rho=20,\quad
\sigma_k=(-1)^{\operatorname{popcount}(\lfloor k/4\rfloor)}.
}
\tag{2}
$$

高间距重新按真实方差约束确定：

$$
\boxed{
B^2=\frac{A^2(N^2-1)-12\nu(1-q_0^2)-12\rho^2A^2}{n^2-1}.
}
\tag{3}
$$

这不是在一个既有 $\delta$ 根上移点；它是先声明的新族，随后重新应用同一个完整能量隐函数论证。每个 block 的最终物理中心 $\zeta_0$ 及区间也在求根以前选定。

低间距取 $A=\Lambda+\sqrt\nu$，$\Lambda\ge10$ 是之后一次固定的有限参数。原 $\rho=0$ 居中排列另保，供最终正负向量组合。

## 2. 三矩和真实不交次序逐项保持

$\sigma_k$ 每四项相同。长度 $n/4=2^9$ 的 Thue–Morse 恒等给

$$
\sum\sigma_k=0,\qquad
\sum(k-c)\sigma_k=0,\qquad \sigma_k^2=1.
\tag{4}
$$

因此高中心平均为零，方差为
$B^2(n^2-1)/12+\rho^2A^2$。
式 (3) 准确给

$$
V_L-V_H=\nu(1-q_0^2).
\tag{5}
$$

这正是原 real 三矩需要的方差差，低/高总质量平衡不变。

imaginary 三矩也没有遗漏。因

$$
\epsilon_k\sigma_k
=(-1)^{\operatorname{popcount}(k\bmod4)},
$$

每四项为 $(+,-,-,+)$，其零次、一次矩都为零。于是
$\sum\epsilon_k\sigma_k=\sum k\epsilon_k\sigma_k=0$。
展开 (2) 的一、二次幂后，新增项分别只用这两个恒等及
$\sigma_k^2=1$；其余仍由原长度 $2^{11}$ 的符号矩支付。
低组完全保留。因此三个完整复矩对本新族准确为零。

高包的实际排序也可定量证明。由 $\rho=20$，

$$
B^2=64^2A^2-\frac{705A^2+12(1-q_0^2)\nu}{n^2-1}.
$$

$A^2>\nu$ 给 $63A<B<64A$，且

$$
|(B-64A)(k-c)|
<\frac{717A}{254(n+1)}<A/100.
\tag{6}
$$

所以 $\sigma_k=-1$ 时高包位于本 cell 的第12与13个低包之间，$\sigma_k=+1$ 时位于第52与53个低包之间；计数从1开始。最近低中心距离至少 $0.49A$，大于外宽度和 $1+q_0$。邻 cell 高中心之间的距离至少
$B-40A>23A$；高包也都在本 cell 的低包包络内部。

同组低包间隙为 $A$，故所有支撑严格不交。乘主宽 $\delta$ 后，充分小正 $\delta$ 将有限云放入任意已选正子区间的双 collar 内。此证明没有让高包穿过一个已有包，或在穿越时假用不交公式；两个排序是分别定义的合法族。

## 3. 完整低阶与母形状隐函数定理

每个最小实子包上 $(f',g')$ 仍沿一个固定方向，故 R183 的全 hook 零张量成立。三矩已经付清，八个完整副本的第七差分仍准确支付四个第三 ruling 槽。

低/高四次质量比未变；每组中心平均仍零。因此 R250 的 $A_{-2,-3}$ even 条件仍成立。所需奇的零/一次中心矩也由 §2 支付。若使用 R265 的伴随母包，even 数据逐点不变，而 odd 项由下面的完整十二复制支付。

本新位置下，高次 $\sum\epsilon_k(t^H_k)^j$ 不一定仍为零。因此不能沿用原基本云中 $L_s=M_s=0$ 的高次符号论证。这里明确依赖十二个完整副本：$L_s,M_s$ 是 odd、四次齐次、平移次数至多10/9；其零与全部36个 Gaussian odd 条件由同一第十一有限差分准确支付。

取 R267 的实际 even 母包 $u_{\gamma,s,h}$，其 central 幅度为 $\gamma>0$、宽度比为 $s>0$。先固定小正母宽 $h$。该稿的两个归一母形状方程为 $\mathcal H=0$ 和 $\mathcal F_\kappa=0$；这里 $\mathcal H=27\nu-K_2/A_0$ 已按 R267 归一。在 $h=0,\gamma=s=1$，两行导数为

$$
(12L^2,-18L^2),\qquad
(-4L^2/9,2L^2/9),
$$

行列式 $-16L^4/3\ne0$。于是有实际
$\gamma_h,s_h=1+O(h^2)$，且可在 $\mathcal F_\kappa=0$ 的真实解析曲线上保留一个使 $\mathcal H$ 简单过零的形状参数。

主宽度的归一方程仍为

$$
F=\delta^3L_c,\qquad
G=\delta(M_c+3L_c/\zeta_0).
\tag{7}
$$

其联合解析证明只使用各类中心零、真实方差差 (5)、以及八/十二副本的四次正权中心零，不要求原居中 cell 次序。故原 $F_\alpha\ne0$ 与母形状限制下的 $G_s\ne0$ 保留；等价地，原三变量 $(\alpha,\gamma,s)$ 的 Jacobian 非退化。

先选一个有限大的 $\Lambda$ 和统一复制间距，再取实际正 $\delta$，便准确支付六能量及 R267 的整个 $A_{-1,-3}$。这不是仅保其 leading 系数。两个排列以及两种母包方向都各自在最后位置独立完成这个实际求根。

## 4. 新排序给完整 sine-four 的负号

沿用

$$
a=q_0(1-\alpha),\qquad
\mathcal B=C\nu-\mathcal L+\Delta/4.
$$

R267 的实际母根仍有 $\gamma,s=1+O(h^2)$；按 R268 的完整母包换元，
先固定足够小正 $h$，再取小正 $\delta$，有 $\mathcal B>0$。
但新 cell 的 ordered 线性项已经改变。

设 $d_k=(B-64A)(k-c)$，真实高偏移为
$\rho A\sigma_k+d_k$。其前方低包数为
$32+\rho\sigma_k$。在 R268 的原量

$$
J=\sum_i b_i^2t_i\left(R_i/2+\sum_{j>i}R_j\right),
\qquad R_i=a_i^2-b_i^2,
$$

记 $t_{\mathrm{cell},k}=64A(k-c)$。使用全局坐标 $t_i$ 时，每个 cell 的准确值为

$$
\begin{aligned}
J_k={}&aA\{-10928q_0+(32q_0+1)\rho^2\}
+a\rho\sigma_kd_k\\
&+a\rho\sigma_k(64q_0+1)t_{\mathrm{cell},k}.
\end{aligned}
\tag{8}
$$

最后两项的全和分别因 (4) 为零。不同 cell 的 inner 总 real 质量仍为零，所以没有另外的远 cell 项。原 self/local 部分的方差归约仍是 (5)。因此完整 shape 外矩为

$$
\begin{aligned}
S_{04}^{(\rho)}
={}&nm^2aA\{10928q_0-(32q_0+1)\rho^2\}\\
&+64na(1-q_0^2)\mathcal B.
\end{aligned}
\tag{9}
$$

在 $\rho=20$，第一行恰为

$$
-nm^2aA(1872q_0+400)<0.
\tag{10}
$$

第二行在固定母根时有限且不依赖 $A$。故先选有限大的 $\Lambda$，再选择实际正 $\delta$，由根分支连续性得到严格
$S_{04}^{(20)}<0$。居中 $\rho=0$ 分支仍由 R268 给
$S_{04}^{(0)}>0$。

R265 的伴随方向只改变各最小子包的 $g$ 符号，不改变 (9)。所以两种方向版本在同一排序下拥有同一个严格 sine-four 符号。

## 5. 每种排序内部仍各有 pure 正、负号

### 5.1 原方向版本的负号

记低、高 quadratic imaginary 质量系数为
$\ell=2q_0\sqrt\alpha$、$H=2\sqrt\beta$。
本 cell 的高低距离和准确为

$$
A(1024+\rho^2)+2\rho\sigma_kd_k.
$$

末项全和为零。高低 imaginary 交叉仍为零：cut12、52都是4的倍数，每个长度4的 Thue–Morse 子块的零次和一次矩均为零，真实 $d_k$ 也因此消掉。

跨 cell 的 total imaginary 质量仍为 $iH\epsilon_k$。
其前缀平方只在偶数到奇数的高点 gap 上非零；$\sigma_k$ 每四项相同，所以这些 gap 仍准确等于 $B$。于是

$$
\boxed{
\operatorname{Re}\sum_{i<j}z_i^2z_j^2(t_j-t_i)
=n\left[
A\{-a^2(21856+64\rho^2)+32\ell^2\}
+\frac{H^2B}{2}
\right].
}
\tag{11}
$$

$\rho=20$ 时，
$a\le1/8$、$H^2\ge28$、$B>63A$ 给严格下界

$$
nA\left(-\frac{47456}{64}+14\cdot63\right)
=\frac{281}{2}nA>0.
\tag{12}
$$

R257 的 local 部分仍为
$64nq_0(\alpha^2-6\alpha+1)(1-q_0^2)\mathcal B<0$。
因此原方向版本在新排序下仍有
$\operatorname{Re}\mathscr Q_-<0$，不是从居中排列沿途连续搬移所推得。

### 5.2 伴随版本的正号

使用 R265 的真实 TM3 伴随母包，令
$K=\int[J(u''\widehat u'')]^2\ge0$。
imaginary primitive 在每个外包内部就紧，其平方无跨外包项。real primitive 不变，新排序的完整 formula 为

$$
\begin{aligned}
\operatorname{Re}\mathscr Q_+
={}&\frac{nm^2a^2A}{2}(21856+64\rho^2)
-\frac{na^2\Delta}{4}(64q_0+4096)\\
&-2nK(64\alpha q_0^3+\beta)
+64nq_0(\alpha^2-6\alpha+1)(1-q_0^2)(C\nu-\mathcal L).
\end{aligned}
\tag{13}
$$

第一行的 $A$ 系数严格为正，其余项在固定母根时有限且不依赖 $A$。可一次选择足够大的有限 $\Lambda$，使 (9) 为负、(13) 为正，然后才用实际主宽度 IFT。连续性将两种严格号都保留到小正 $\delta$。

居中排列也仍有 R262/R265 的 $\mathscr Q_-<0<\mathscr Q_+$。十二复制后这些量是真实实数；全部零矩消掉共同平移附加项，正主宽度及正幅只给相应正因子。于是每个排列内部都已有 pure 双号，且该排列的 sine-four 符号不变。

## 6. 四个最终位置的完整 block 与正幅向量消去

在四个有严格间隙的正物理子区间中，分别构造

$$
(\rho,\text{方向})\in\{0,20\}\times\{\text{原},\text{伴随}\}.
$$

每个 block 都在其最后位置先完成 R267 的实际三变量 IFT、八个完整副本和十二个完整副本。后面只改共同实幅度，不再移动或缩放一个已经解出的 energy 根。

在每个固定 $\rho$ 中，按 R265 的正四次权混合负、正 $\mathscr Q$，得到一个完整 block $B_\rho$，满足

$$
\mathscr Q(B_\rho)=0,\qquad
S_{04}(B_0)>0,\qquad S_{04}(B_{20})<0.
\tag{14}
$$

这一步不要求两个方向版本的 sine-four 数值相等；它们只需具有已证明的共同严格符号。

再令两个 block 的四次幅度权为

$$
w_0=-S_{04}(B_{20})>0,\qquad
w_{20}=S_{04}(B_0)>0.
\tag{15}
$$

按正四次根放大并相加，准确得到

$$
\boxed{\mathscr Q=0,\qquad S_{04}=0.}
\tag{16}
$$

加法保持的条件逐项为：每个完整 block 三矩为零；canonical 二阶差和交叉真紧，完整第三槽及 hook 保留；六能量按原真实边界和不交 bulk 相加；R259 的所有跨 block 核对 inner 三矩线性，因而全为零。因此两个已付完整面积、所有 odd 条件也保持。这没有把单 cell 的左尾假设为零。

## 7. 从两个 scalar 到完整第零外矩

这一结论还需准确的角分支对应，不能仅以两个数字为零宣告整角通过。按 R259 写

$$
2I_0\{\phi_\theta,[P,Y](\phi_\theta;D_\theta)\}
=E_{31}\cos^3\theta\sin\theta+
E_{22}\cos^2\theta\sin^2\theta+
E_{13}\cos\theta\sin^3\theta+
E_{04}\sin^4\theta.
\tag{17}
$$

全部 odd 包装给 $E_{31}=E_{13}=0$，而 $E_{04}=S_{04}$。
将同一完整 self/cross 阵代入合法复 profile $q=f+ig$，普通四次展开准确给

$$
E_{22}-E_{04}
=\operatorname{Re}\{2I_0(q,[P,Y](q;q\odot q))\}
=-\operatorname{Re}\mathscr Q(q).
\tag{18}
$$

例如若 $\Omega_{ik}$ 是 R259 的上三角阵，左边的权为
$(a_i^2-b_i^2)(a_k^2-b_k^2)-4a_ib_ia_kb_k$，
正是 $\operatorname{Re}(a_i+ib_i)^2(a_k+ib_k)^2$。
所以这一步保留完整有序阵，不是假用 diagonal 取消 off-diagonal 的 quadratic cross 项。

由 (16)、(18)，$E_{22}=E_{04}=0$。因而整个 (17) 恒零。
原 Gaussian $[B_1,B_{-3}]=-\zeta c[P,Y]$ 只是同一非零实因子，所以得到整个 $A_{1,-3}$ 的第零外矩。

## 8. 已付范围与尚未解决的部分

所得真实正宽圆同时有：

- 三矩及原完整第二、第三 range；
- 共振 germ 的全部六个已识别能量；
- $A_{-2,-3}$ 和 $A_{-1,-3}$ 的三个完整角外矩；
- 所有六 Gaussian 面积的36个 odd 条件；
- $A_{1,-3}$ 第零外矩的两个完整 even 条件，因而其整个第零角函数。

在 R259 原72式账中，仍有22个形式 even 等式未由上述结论支付；这不是它们的独立秩。$A_{1,-3}$ 的第1、2外矩以及其余 Gaussian 面积不能因 (18) 自动略去。零/一层 history、第四 period 与有限等距族也仍未解决。

这个构造使用真正不同的 real quadratic mass 次序，并在原准确方差约束内重新建立非退化 IFT。它没有放宽任何已付原门，也没有把主宽度趋零的形式极限当实际 profile；每个最后使用的宽度、幅度和间隙均严格正且有限。

共同归一化只同乘一个正实幅度，全部齐次零保持；种子和目标是新选择的 profile 圆。原闭几何/germ 的调用仍限于 R227/R241 的已证明合法安装，不授原 finite-observation 值、曲面嵌入、reach、宏观幅度或主课题完成。

本稿给准确有限存在证明，没有执行或请求新的研究运算。
