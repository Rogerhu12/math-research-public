# R924 — 原完整截面格的闭点代数、双分歧纤维与相对六次 shadow 接口

日期：2026-11-20。

**状态：下列有限代数构造、全部重数与局部读数、原 $D_S$ 和 cusp 的闭点形状，以及原 $Y=X_0(3468)$ 三个退化拉回的完整权因子均已证明。有限代数 producer 的实际公开回执另行登记；没有把本篇的构造定理记作四个大交除子或原 shadow 已经执行成功。**

本篇保持 [R917](R917-original-global-rr-lattice-from-saturated-q-jets.md) 的原全局空间和整格，并对接 [R882](R882-original-degree18-source-model-and-two-endpoint-coordinates.md)、[R883](R883-original-relative-six-shadow-and-complete-boundary.md) 的同一原源、原两映射与全部 Artin 常数。这里使用已知光滑模曲线的完整截面空间；不从一个未正规化平面方程的仿射零点猜闭点，也不把抽象 Jacobian 群算法本身当作消费者的闭点输入。

## 1. 全局分次空间与有限乘法

先在原 $B=X_0(867)$ 上工作，底域为 $k=\mathbf F_r$，$r=29$ 或 $41$。保持
$$
g_B=85,\qquad \mathcal C_B=\text{全部36个几何cusp},\qquad
L=\Omega_B^1(\mathcal C_B),\qquad \delta=\deg L=204,
$$
$$
S(Q)=\frac{3E_2(Q^3)-E_2(Q)}2,
\qquad S(Q)\frac{dQ}{Q}=-\frac{dT}{T},
\qquad D_S=\operatorname{div}_L(S).
\tag{1}
$$
对每个 $m\ge1$，记
$$
R_m=H^0(B,L^m),\qquad V_m=R_m/S^m=L(mD_S),
\qquad \dim R_m=204m-84.
\tag{2}
$$
必须保留分次：$S$ 是 $R_1$ 中的截面；在 $V_1$ 中它写成函数 $1$，但其截面零除子仍为 $D_S$，不能把它与分次零的常数截面混同。

R917 的完整有理构造器、局部饱和和基变换给每个实际 $R_m$ 的忠实坐标 $Q^0,\ldots,Q^{204m}$。需要更长精度时，仍从同一个全局构造器扩展并施同一变换。对于
$$
\mu_{a,b}:R_a\otimes R_b\longrightarrow R_{a+b}
\tag{3}
$$
先将两输入读到 $204(a+b)+1$ 项，作实际级数乘积，再用完整 $R_{a+b}$ 解全部行。两边是已知全局截面，且该窗单射，所以所得坐标是完整乘法。若用低权乘积选择高权基，只有实际秩达到 $204m-84$ 后才能称完整；不达到时应调用该权的完整模形式空间并饱和，不能假设某个候选乘积池张满。

本篇只需这些有限维空间及乘法，不需要写出 $B\hookrightarrow\mathbf P^{119}$ 的全部二次理想。$L$ 的确很充足：对任意长度二的零维子概形 $Z$，$\deg L(-Z)=202>2g-2$，所以 $H^1(L(-Z))=0$，全局截面分离所有长度二子概形。后文用这个事实给闭点一个忠实射影坐标，而不额外运行平面正规化。

## 2. 一个真实截面的完整零维代数

以下构造对任意已知光滑射影几何连通曲线 $C/k$ 及 $\deg L=\delta>2g-2$ 成立；所有 $R_m$ 必须是完整的 $H^0(C,L^m)$。取真实非零截面
$$
s\in R_d,\quad d\ge1,\qquad Z=\operatorname{div}_{L^d}(s).
$$
$Z$ 是包含全部重数的有效 Cartier 除子，$\deg Z=d\delta$。选 $n\ge d+1$，定义
$$
M_n(s)=R_n/sR_{n-d},\qquad
M_{2n}(s)=R_{2n}/sR_{2n-d}.
\tag{4}
$$

**定理1（同一全局零除子的有限代数）。** 两个商的维数都恰为 $d\delta$。若 $h\in R_n$，则
$$
m_h:M_n(s)\longrightarrow M_{2n}(s),\qquad [a]\longmapsto[ha]
\tag{5}
$$
可逆，当且仅当 $h$ 在 $Z$ 的全部局部 Artin 环上是单位截面。对任何通过这个完整可逆性检验的 $h$，
$$
\boxed{[a]\star[b]=m_h^{-1}([ab]),\qquad 1_{\star}=[h]}
\tag{6}
$$
使 $M_n(s)$ 成为一个规范同构于 $\Gamma(Z,\mathcal O_Z)$ 的 $k$-代数；同构是 $[a]\mapsto a/h$。特别它保留所有 nilpotent、每个闭点的剩余域及原截面的准确零阶。

**证明。** 原截面给短正合列
$$
0\longrightarrow L^{n-d}\xrightarrow{\cdot s}L^n
\longrightarrow L^n|_Z\longrightarrow0.
$$
因 $n-d\ge1$，左端的 $H^1$ 为零。因此
$$
M_n(s)=H^0(Z,L^n|_Z),
\quad M_{2n}(s)=H^0(Z,L^{2n}|_Z),
\tag{7}
$$
维数均为 $\deg Z$。在每个局部 Artin 因子上选线束的任意生成元后，(5)就是乘以该因子中的 $h$。有限维局部环中的乘法算子可逆恰当且仅当乘数为单位。这同时证明“全商可逆”包括非约化结构，不能只在约化支集上取一个未经连接的数值行列式。

除以 $h$ 后，$[ab]/h^2$ 正是两个函数之积；(6)因而成为 $\mathcal O_Z$ 的原乘法，交换、结合及单位都成立。所有商只由真实乘法像形成，所以没有引入额外点或删除共同零。证毕。

实现中应记录原 $s,h$ 的完整分次坐标、$sR_{n-d}$、$sR_{2n-d}$ 的实际像与秩、固定商基和回代、(5)完整矩阵及逆。商基可由固定列序的行消元确定；选基只改变同一个有限代数的坐标。

### 2.1 辅助 h 的存在和合法搜索

$Z$ 为有限概形，其坐标环是有限个局部 Artin 环的积；其上每个可逆模都自由。因此 $L^n|_Z$ 有单位生成元。由(7)的满射，这个生成元有一个全局提升 $h\in R_n$。所以在有限域上穷举 $R_n$ 的系数并逐个检验(5)，一定终止。随机选取只可作为先行搜索，每个成功都仍须通过全矩阵可逆性；预设试验次数失败不能否定该存在定理。

也可在有限常数扩张 $k'/k$ 中找到单位 $h'$，然后取所有实际常数共轭的乘积，得到 $H\in R_{[k':k]n}$。它仍在 $Z$ 上处处非零；改用这个分次后的两个商并重新检验 $m_H$，即可完全返回原底域。不能只保存扩域后的点而丢掉原剩余次数。

特别，对于原 $s=S,d=1,n=2$，只需
$$
\boxed{R_2/SR_1\quad\text{和}\quad R_4/SR_3,}
\tag{8}
$$
维数分别为 $324-120=204$ 与 $732-528=204$。若程序使用 $V_m=R_m/S^m$ 的函数 jet，则同一两个商写成 $V_2/V_1$ 和 $V_4/V_3$，所有分次仍按(8)保留。

## 3. 原 D_S 的全部闭点和非约化长度

**定理2（原双分歧纤维）。** 在 $r=29$ 或 $41$ 上，存在一个约化、次数 $102$ 的有限 étale 除子 $Z_{\mathrm{ell}}$，使
$$
\boxed{D_S=2Z_{\mathrm{ell}},\qquad
Z_{\mathrm{ell}}=\{T=-27\}\ \text{的约化逆像}.}
\tag{9}
$$
它由准确 $51$ 个次数二闭点组成。因此
$$
\boxed{
\Gamma(D_S,\mathcal O_{D_S})
\simeq\prod_{i=1}^{51}\mathbf F_{r^2}[\epsilon_i]/(\epsilon_i^2).
}
\tag{10}
$$
乘法代数(10)的分解不是各点局部参数的预选；任何实际求出的局部参数仍须在相应非约化因子中核定。

**证明。** 原 $B\to X_0(3)$ 的次数为 $306$。$X_0(3)$ 唯一的阶三椭圆点，在原 Hauptmodul 中是 $T=-27$。$B$ 没有阶二或阶三稳定子。于是这点之上每个几何点的 ramification index 为 $3$，共 $306/3=102$ 个点。这里 $r\nmid6\cdot17$，稳定子与退化覆盖均 tame；在原光滑好模型上这些是实际粗曲线的分歧长度，不能再乘或除一个 stack 因子。

在每点取局部参数 $u$，有 $T+27=c u^3+O(u^4)$，$c\ne0$。因 $T=-27\ne0$，$dT/T$ 的零阶恰为二。原覆盖在非 cusp 开集仅有这个椭圆分歧；在分母 $1,3,17,51,289,867$ 的 cusp 上，$T$ 的实际零/极阶分别为 $289,-289,1,-1,1,-1$，故 $dT/T$ 是具有非零留数的简单极。加上全部 $\mathcal C_B$ 后每个 cusp 的 $D_S$ 系数为零。这些二阶零总次数 $204$ 已等于(1)的全部次数，证明(9)。

还需确定剩余次数。该椭圆纤维的模点可表示为 $j=0$ 曲线及唯一受 $\mu_6$ 保持的 cyclic3 子群，再选 cyclic $17^2$ 子群，最后按 $\mu_3$ 取商。共有 $17(17+1)=306$ 个 cyclic $17^2$ 子群；$17$ 在 $\mathbf Q(\sqrt{-3})$ 惰性，故没有 $\omega$ 稳定的 $\mathbf F_{17}$ 直线，$\mu_3$ 作用无稳定点。这也独立核回(9)中的102个粗模点。

对 $E_0:y^2=x^3+1$ 而言，$r\equiv2\pmod3$ 使 $x\mapsto x^3$ 为 $\mathbf F_r$ 的双射，所以 $\#E_0(\mathbf F_r)=r+1$，原 Frobenius 满足 $\pi_r^2=[-r]$。平方是标量，故所有 cyclic $17^2$ 子群和上述模点都在 $\mathbf F_{r^2}$ 定义。

若其中有 $\mathbf F_r$ 点，则存在 $\zeta\in\mu_6$ 使 $\zeta^{-1}\pi_r$ 保持相应 cyclic $17^2$ 子群，因而保持其唯一 order17 子群。因 $\pi_r\zeta=\bar\zeta\pi_r$，
$$
(\zeta^{-1}\pi_r)^2=[-r].
$$
但 $-29\equiv5$ 和 $-41\equiv10\pmod{17}$ 都不是平方；$X^2+r$ 在 $\mathbf F_{17}$ 上不可约，所以此算子不可能保一条 $\mathbf F_{17}$ 直线。矛盾。故102个几何点都成次数二的 Frobenius 轨道。光滑曲线的二倍点局部环为 $\kappa(Q)[u]/u^2$，有限剩余域完美，得到(10)。证毕。

### 3.1 可执行的完整 Frobenius 校验

令 $F:a\mapsto a^r$ 为(10)上 $\mathbf F_r$-线性的 Frobenius。它杀所有 $\epsilon_i$，在每个 $\mathbf F_{r^2}$ 因子上是二次共轭。因此完整原代数必须满足
$$
\boxed{F^3=F,\quad \operatorname{rank}F=102,\quad
\dim\ker F=102,\quad
\dim\ker(F-I)=\dim\ker(F+I)=51,}
\tag{11}
$$
$$
\boxed{\operatorname{charpoly}(F)=X^{102}(X-1)^{51}(X+1)^{51}.}
\tag{12}
$$
这些是(8)所构造整个204维代数的检验，不是把它先约化后只验102维。实际分解还须用乘法算子/幂等元给51个剩余域和对应二维局部长度；(11)本身不负责标号这些原点。

还可独立检验原 $T$ 的完整局部作用：因 $T+27$ 在每点的零阶为三，而 $D_S$ 的局部长度为二，$T$ 在整个 $\Gamma(D_S,\mathcal O)$ 中准确等于 $-27\cdot1$，连 nilpotent 部分也为零。若截面分式的分母在某局部因子不为单位，须按§5加厚后约去共零，或直接使用此已证全局局部身份；不能由交叉乘式模 $D_S$ 为零就假设分母可除。$U,V$ 没有被这条结论设为常数。

## 4. 全36 cusp 的独立有限代数

设 $W_m=H^0(B,L^m(-\mathcal C_B))=S_{2m}(\Gamma_0(867),k)$。对 $m=2,4$，$H^1(L^m(-\mathcal C_B))=0$，故
$$
R_m/W_m=H^0(\mathcal C_B,L^m|_{\mathcal C_B}),
\quad \dim(R_2/W_2)=\dim(R_4/W_4)=36,
\tag{13}
$$
其中 $\dim W_2=288$，$\dim W_4=696$。完整有理 cusp 空间必须独立保留其全局身份并作与 R917 相同的 $r$-饱和；“仅无穷 cusp 常数项零”不等于 cusp 空间。

上一节已经逐 cusp 证明 $S$ 为单位截面，所以 $h=S^2\in R_2$ 给完整同构
$$
R_2/W_2\xrightarrow{\cdot S^2}R_4/W_4.
\tag{14}
$$
用(6)同样的返回乘法，得到 $\Gamma(\mathcal C_B,\mathcal O)$。若实现用 $S_4M_4$ 生成 $S_8$，必须实际验证该乘积像的秩为696；否则应使用完整 $S_8$ 的饱和基。

原六种分母的 cusp 数为 $1,1,16,16,1,1$。四个孤立 cusp 在 $\mathbf Q$ 定义；中间两个16点 packet 各以 $\mathbf Q(\zeta_{17})$ 为剩余域。这是标准 Tate cusp 参数的实际 Galois 作用，见末节原文。$29\equiv12$ 与 $41\equiv7\pmod{17}$ 都有阶16：各自的八次幂为 $-1$，四次幂不为 $1$。故
$$
\boxed{\Gamma(\mathcal C_B,\mathcal O)
\simeq\mathbf F_r^4\times\mathbf F_{r^{16}}^2.}
\tag{15}
$$
完整 Frobenius 应满足
$$
F^{16}=I,\qquad
\operatorname{charpoly}(F)=(X-1)^4(X^{16}-1)^2,
\qquad \dim\ker(F^d-I)=4+2\gcd(d,16).
\tag{16}
$$
特别固定子代数维数为6。扩到原消费者的 $\mathbf F_{r^2}$ 后，四个有理 cusp 仍在，两个16点 packet 各分成两个 degree8 闭点，所有36个几何 cusp 均保留。

## 5. 从完整有限代数读取闭点、重数和局部参数

本节给消费者实际可调用的数据，不止给一个抽象同构类。令 $A=\Gamma(Z,\mathcal O_Z)$ 已按定理1构造。

1. **分解约化商与原局部因子。** 对 $q=\#k$ 取 $q^a\ge\dim_kA$。$\ker(x\mapsto x^{q^a})$ 正是 nilradical，像是各完美剩余域组成的规范可分子代数。对这个有限 étale 代数，用实际乘法算子的最小多项式分解及 gcd 分裂得到全部 primitive idempotent。不断加入一个尚未分离的基元素必终止；不假设有限域上的整个积一定由一个元素生成。将幂等元提升/读回 $A$，得到全部原局部 Artin 因子 $A_Q$。
2. **次数与重数。** $\kappa(Q)$ 是 $A_Q$ 的实际剩余域，$d_Q=[\kappa(Q):k]$；原截面在 $Q$ 的零阶是 $e_Q=\dim_kA_Q/d_Q$。检查 $\sum_Q e_Qd_Q=d\delta$。这里只到最后一步才允许在指定 $\ell$-扭点群中约化乘数。
3. **原点的忠实标号。** 因 $L$ 很充足，取 $R_1$ 的原固定基。对每个 $Q$，选择其中一条在 $Q$ 非零的截面作为局部 frame，读取全部比值的剩余值，得到原 $B\hookrightarrow\mathbf P^{119}$ 的实际坐标。可用原底域 Frobenius 轨道的规范代表作 fingerprint；两个不同切割得到的闭点，只有这些完整射影坐标的原域轨道相同才合并。不能只按次数或一个最小多项式合并。
4. **截面局部值。** 若 $a\in R_e$，其在 $Z$ 上的作用由 $M_n(s)\to M_{n+e}(s)$ 的真实乘法读出。对单个局部因子，$R_e$ 的基中必有一条 $u_e$ 非零；乘 $u_e$ 在该因子上可逆，把乘 $a$ 与其比较便给 $a/u_e\in A_Q$。这不要求 $S(Q)\ne0$。
5. **局部参数及全部 jet。** 若 $e_Q\ge2$，光滑性使 $\mathfrak m_Q/\mathfrak m_Q^2$ 为一维 $\kappa(Q)$ 空间。实际选 $\pi_Q\in\mathfrak m_Q\setminus\mathfrak m_Q^2$，验证 $1,\pi_Q,\ldots,\pi_Q^{e_Q-1}$ 在 $\kappa(Q)$ 上为基；即可通过线性代数读取所有局部系数。若原切割只有简单点，需要先用 $s^2$ 的完整商读取一阶切方向，不能凭一个约化点声明已有参数。

有限剩余域的系数域有一个可核的规范选择：它是局部环中满足 $x^{q^{d_Q}}=x$ 的元素。导数为 $-1$，所以每个剩余类有唯一此类提升。也可用足够高 Frobenius 幂直接取得。所有局部系数和常数嵌入由这个选择固定；原 $\omega$ 的像、$\mathbf F_{r^2}$ 结构及实际剩余次数不被另一次独立选根替换。

对于当前 $n=2$ 的 $D_S$ 代数，射影坐标还有一个不需更高分次的读法。单位为 $h\in R_2$，先将所有真实乘积 $f_if_j\in R_2$ 投入商。对一个局部因子选 $j$ 使 $f_j^2/h$ 的剩余值非零，则
$$
\frac{f_i}{f_j}=\frac{[f_if_j]/h}{[f_j^2]/h}
$$
在整个局部 Artin 因子中成立，给原120个射影坐标和其一阶变化。cusp 代数的 $h=S^2$，则直接以 $[f_iS]/h=f_i/S$ 读取全部原坐标。它们只需现有 $R_1R_1\to R_2$ 的乘法，适合在首份实际有限代数回执中保留原点标号。

### 5.1 实际 A/B 的共零与 S 的交点

写一个实际原函数为同分次的截面比 $f=A/B$，$A,B\in R_e$，$A,B\ne0$。若最初两分子分母分次不同，先在分次环中按原 $S$ 因子准确同次化；这些 $S$ 因子必须留在后续零阶中。

分别读取 $A,B$ 的完整零除子，或一次读取 $AB$ 的零除子，再用上节实际射影坐标匹配，得到
$$
v_Q(f)=v_Q(A)-v_Q(B).
\tag{17}
$$
在共零点上不能先删除一个未认证 gcd，也不能把分母在约化域等于零当作函数有极。如果要在另一个切割 $Z(s)$ 上读取 $f$，而其局部长度不足以看见 $A,B$ 的首项，则依次改用 $Z(s^2),Z(s^4),\ldots$。同一 primitive idempotent 通过原射影坐标跟踪；当长度严格超过 $v_Q(A),v_Q(B)$ 时，两条首项均可见，约去共同 $\pi_Q$ 次幂便给剩余值或真实极。

这一步必终止：非零截面 $A\in R_e$ 的零除子总次数是 $e\delta$，所以每个局部阶有固定有限上界。对同阶非零 $A,B$，总长超过 $e\delta$ 已足够；自适应实现可远早于此门停止。所有扩大商仍由(4)的完整全局截面构造，因而是原光滑曲线的加厚点，不是任选形式解。

输出接口可采用：
$$
\texttt{Divisor.list()},\quad\texttt{degree()},\quad
\texttt{multiplicity(Q)},\quad
\texttt{Q.residue\_field()},\quad
\texttt{valuation(f,Q)},\quad\texttt{reduce(f,Q)},
\tag{18}
$$
并附原射影 fingerprint、完整局部长度和 frame/参数回执。它们正覆盖现有 relative-six 消费器在除子及闭点部分的请求。

## 6. 原 T/U/V 及其他已知函数的截面分式

上述代数也能直接消费原有理函数，而不先把它们写成 eta48 的有理表达式。这里的先决条件是函数已有全局存在与原身份，不能把一个形式 germ 的有限核当作存在证明。

**定理3（有全局极帽的准确分式恢复）。** 设原函数 $f\in k(C)$ 已知，$P_f=\operatorname{pole}(f)$，$\deg P_f\le M$，且 $D$ 是有效次数 $\delta$ 除子，在原展开点 $\infty$ 的系数为零。取 $n\delta-M\ge g$，并令 $V_n=L(nD)$ 完整。则存在 $A,B\in V_n$、$B\ne0$，使 $A=fB$。若 $e=\max(0,-\operatorname{ord}_\infty f)$，对任意候选对只要
$$
Q^e A-(Q^e f)B=0
\quad\text{在全部次数 }0,\ldots,n\delta+M+e\text{ 上成立},
\tag{19}
$$
就有准确函数恒等式 $A=fB$。

**证明。** Riemann–Roch 给
$$
h^0(nD-P_f)\ge n\delta-M+1-g\ge1.
$$
取非零 $B$ 在其中，则 $fB\in L(nD)$。另一方面，对任意 $A,B\in V_n$，差 $A-fB$ 属于 $L(nD+P_f)$，其全局极除子次数不超过 $n\delta+M$。条件(19)令其在 $\infty$ 的零阶至少为 $n\delta+M+1$。非零有理函数的零、极次数相等，所以差必须为零。若核向量的 $B=0$，则同一忠实窗迫 $A=0$，故任何非零核向量均有非零分母。证毕。

### 6.1 同一个原 T/U/V 的小分次实现

[R882 附A](R882-original-degree18-source-model-and-two-endpoint-coordinates.md) 已证明原模单位
$$
T=T_3(Q),\qquad U=T_3(Q^{17}),\qquad V=T_3(Q^{289})
\tag{20}
$$
只在 cusp 有零极。其完整 cusp 阶表给
$$
\deg P_T=289+16+1=306,\quad
\deg P_U=17+16\cdot17+17=306,\quad
\deg P_V=1+16+289=306.
\tag{21}
$$
这些是原好约化曲线上的次数；模单位在各 cusp 的首系数为所选好素数的单位，不能只据无穷 cusp 的极阶计算总次数。

取 $n=2$。$408-306=102\ge85$，所以每个函数都有同一完整324维 $V_2$ 中的分式。更具体地，线性映射
$$
V_2\oplus V_2\longrightarrow L(2D_S+P_f),\qquad(A,B)\longmapsto A-fB
\tag{22}
$$
的源维数648，靶维数 $714+1-85=630$，核维数至少18。原极阶 $e$ 分别为1、17、289；(19)只需检查 $Q^e A-(Q^e f)B$ 的全部 $0,\ldots,714+e$ 行。共同最大窗为 $Q^0,\ldots,Q^{1003}$，即1004项。

实现时把 R917 的同一完整 $M_2$ 基延长到此精度，由实际满秩乘积给 $M_4$，施同一饱和基变换，并解(22)的全部行。若 $A=a/S^2$、$B=b/S^2$，则 $f=a/b$，$a,b\in R_2=M_4$：相同的 $S^2$ 准确相消。这给原 $T,U,V$ 的真实截面分式，未引入新的 primitive element、eta 根或平面正规化。

原两条17-Hecke 关系及已证明的 $T,U,V$ 上 Atkin–Lehner 公式随(20)的全局身份继承。这个结论不自动给出 Atkin–Lehner 在所有 $M_2$ 基元上的矩阵；如某个后续算法需要该矩阵，仍须实际构造。

### 6.2 原 F/P 坐标和原立方根

先经过现有 `certificate_weight` 的全部原特征零 PASS 检查，再沿 [R881](R881-original-good-prime-direct-coordinate-reconstruction.md) 的同一低核恢复原 $v_F,Y_i$。这里保留原完整候选和全部恒等式，不把模 $r$ 的 ODE 解当作映射。若原成功权为 $k_F\in\{2,4\}$、$k_P\in\{4,6\}$，令
$$
a=(k_F+6)/2,\qquad b=k_P/2.
$$
现有 $v_F$ 为 $V_a/V_{a-3}$ 的比，因此写成截面分式时必须是
$$
v_F=\frac{A_F}{B_F S^3},\quad A_F\in R_a,\quad B_F\in R_{a-3}.
\tag{23}
$$
分母 $S^3$ 不能丢掉。原 $Y_i=A_i/B_i$ 则两边均在 $R_b$。于是
$$
\deg\operatorname{pole}(v_F)\le204a,
\qquad\deg\operatorname{pole}(Y_i)\le204b.
\tag{24}
$$

原函数 $R_F,R_i$ 的存在来自已认证映射及 R882，而非另添三次覆盖；它们保持
$$
D=\frac{T^3}{(T+27)^4},\qquad
R_F^3=\frac{v_F^2-17D}{D(T+27)},\qquad
R_i^3=\frac{Y_i(Y_i+v_{\rm new,i})}{(T+27)^2},
\tag{25}
$$
以及全部原 $R_F(\infty)=R_i(\infty)=1$。原首项为1的局部根由 $3\in k^\times$ 的 Hensel 递推唯一确定。为了在截面模型中恢复这些已存在的函数，可直接应用定理3，不需对一个函数域多项式作全因式分解。

对 $R_F$，先准确改写
$$
R_F^3=v_F^2\frac{(T+27)^3}{T^3}-\frac{17}{T+27}.
$$
由 $T=0$ 和 $T=-27$ 两纤维的次数均为306，有
$$
\deg\operatorname{pole}(R_F)
\le\frac{2(204a)+4\cdot306}{3}
=\begin{cases}952,&k_F=2,\\1088,&k_F=4.\end{cases}
\tag{26}
$$
对 $R_i$ 则有
$$
\deg\operatorname{pole}(R_i)
\le\frac{2(204b)+2\cdot306}{3}
=\begin{cases}476,&k_P=4,\\612,&k_P=6.\end{cases}
\tag{27}
$$
因此下面的完整空间已足够；“最后项”是定理3中 $e=0$ 的最后一个必检验指数。

| 原函数 | 完整分式空间 | 极次数上界 | 最后一项 |
|---|---:|---:|---:|
| $R_F$，$k_F=2$ | $V_6/V_6$ | 952 | 2176 |
| $R_F$，$k_F=4$ | $V_6/V_6$ | 1088 | 2312 |
| $R_i$，$k_P=4$ | $V_3/V_3$ | 476 | 1088 |
| $R_i$，$k_P=6$ | $V_4/V_4$ | 612 | 1428 |

所得分式须在完整分次环中再次验证(25)及原无穷支；全部等式都是同一个原函数的等式。尤其 $k_F=2$ 和 $k_P=6$ 不能因成功权或分母形状不同而改动原 $F$ 的目标、原 P 的 Artin embedding、或任何 period。

## 7. 原 Y 的完整截面格与三个真实退化拉回

只在 $B$ 上有闭点代数，尚不足以消费 R883 的源交点：还必须得到同一原
$$
Y=X_0(3468),\qquad 3468=4\cdot867
\tag{28}
$$
的全局格或一个与之已识别的等价局部模型。本节给一个不依赖 eta48 正规化的完整选择。

### 7.1 原 Y 的空间和全部边界

该级也无椭圆稳定子，指标为7344。对 $d=2^\alpha3^\beta17^\gamma\mid3468$，$\alpha=0,1,2$、$\beta=0,1$、$\gamma=0,1,2$。当 $\gamma=0,2$ 时各 cusp packet 含一个有理点，共12个；当 $\gamma=1$ 时有六个16点 packet，域为 $\mathbf Q(\zeta_{17})=\mathbf Q(\zeta_{34})$。所以几何 cusp 数为108，
$$
g_Y=1+7344/12-108/2=559,
\qquad L_Y=\Omega_Y^1(\mathcal C_Y),\quad\deg L_Y=1224.
\tag{29}
$$
在 $r=29,41$ 约化后，全部 cusp 代数为
$$
\Gamma(\mathcal C_Y,\mathcal O)
\simeq\mathbf F_r^{12}\times\mathbf F_{r^{16}}^6.
\tag{30}
$$
这些仍是108个几何点；扩到 $\mathbf F_{r^2}$ 后是12个有理点和12个次数八闭点。

定义 $R_m^Y=H^0(Y,L_Y^m)$。R917 的好模型、$H^1=0$、有限 q-jet 单射及局部饱和证明逐字适用，数值改为
$$
\dim R_m^Y=1224m-558,\qquad
u^0,\ldots,u^{1224m}\text{ 为忠实窗}.
\tag{31}
$$
特别 $R_1^Y$ 维数666，$L_Y$ 很充足。必须以完整 $M_2(3468)$ 或实际满秩的另一全局构造器得到这666维空间；不能把三个120维退化像之和当作完整空间。高权完整性也仍由(31)的实际秩或完整该权构造器支付。

### 7.2 三退化的微分权和不同分母

沿原 R882 cusp，$Q=q^6$，在 $Y$ 取 $u=q^3$，所以中央底参数为 $Q=u^2$。为避免原下标与代入指数混淆，记
$$
\pi_1=q_0,\qquad\pi_2=q_1,\qquad\pi_4=q_2,
\qquad Q\circ\pi_j=u^j\quad(j=1,2,4).
\tag{32}
$$
它们是模问题已经给定的三个次数六退化映射；不是从三个形式代入另猜全局映射。它们在非 cusp 处 étale，在 cusp 处 tame。对数微分给规范线束同构 $\pi_j^*L\simeq L_Y$，实际权为
$$
\boxed{\pi_j^*\!\left(f(Q)(dQ/Q)^m\right)
=j^m f(u^j)(du/u)^m.}
\tag{33}
$$
因此取原中央截面及其除子
$$
S_Y(u)=2S(u^2),\qquad D_Y=\operatorname{div}_{L_Y}(S_Y)=\pi_2^*D_S,
\qquad V_m^Y=R_m^Y/S_Y^m.
\tag{34}
$$
它在无穷 cusp 是单位，其零除子次数1224。对原 $R_1$ 固定基 $f_i$，令
$$
\rho_j=\frac{jS(u^j)}{2S(u^2)},\qquad
G_{i,j}=\frac{j f_i(u^j)}{2S(u^2)}.
\tag{35}
$$
每个分子都是已知全局 $L_Y$ 截面，故 $\rho_j,G_{i,j}\in V_1^Y$，可由(31)的完整窗读其准确坐标，且
$$
\boxed{\pi_j^*(f_i/S)=G_{i,j}/\rho_j,\qquad\rho_2=1.}
\tag{36}
$$
一般 $a\in R_m$ 的拉回为 $j^m a(u^j)$，其 RR 函数拉回要再除 $\rho_j^m$。所以 $S(u),S(u^2),S(u^4)$ 对应三个真实零除子；只有在同一个比值中，明确相同的权因子才可消去。不能把三个退化像一律放进同一 $V_m^Y$ 而丢掉 $\rho_j$ 的极零修正。

由定理2，$D_Y$ 为612个几何点的二倍。中央六次覆盖在这些点上 étale；其纤维是中央 elliptic curve 的完整2级数据，$\pi_r^2=[-r]$ 在2挠上为标量，所以全部纤维在 $\mathbf F_{r^2}$ 定义。底支集没有 $\mathbf F_r$ 点，源也没有。于是还得到可独立检验的形状
$$
\Gamma(D_Y,\mathcal O)\simeq
\prod_{i=1}^{306}\mathbf F_{r^2}[\epsilon_i]/(\epsilon_i^2).
\tag{37}
$$
但(37)不能替代实际构造完整 $R_m^Y$ 以及实际666维射影标号。

### 7.3 同一原 y_s 与端点，不另选根

原 $Y\to X_0(12)$ 的次数为306；R882 的 $y_s$ 是 $X_0(12)$ 的有理参数。因此 $\deg\operatorname{pole}_Y(y_s)=306$，并且沿原支
$$
y_s^2(y_s^2-9)^2=T_3(u^2)(y_s^2-1)^2,
\qquad y_s=-u^{-1}+O(u).
\tag{38}
$$
这是已经识别的原模函数，而非任取(38)的一个解。令 $t(u)=u^2T_3(u^2)$、$z=u y_s$。正则方程为
$$
z^2(z^2-9u^2)^2-t(u)(z^2-u^2)^2=0.
\tag{39}
$$
在 $u=0,z=-1$ 的 $z$ 导数为 $-2$，故原局部支可在两个好素数处无歧义地延长。定理3中取 $C=Y,D=D_Y,n=1,M=306,e=1$：$1224-306\ge559$，所以 $y_s$ 直接写成两个完整 $V_1^Y$ 元素的比；检验(19)全部 $0,\ldots,1531$ 行即给原全局身份。

令 $v=y_s^2-1$、$N_0=5v+8-y_s(v-8)$。原两端点 $T_0,T_2$ 及原 deck involution 保持
$$
T_0=N_0^3/v^4-27=\pi_1^*T,
\qquad T_2=(v-2)^3/v-27=\pi_4^*T,
\tag{40}
$$
$$
W(y_s)=\frac{y_s+3}{y_s-1},\qquad
\pi_2\circ W=\pi_2,\qquad
\pi_1\circ W=\pi_4.
\tag{41}
$$
这些来自 R882–R883 的原几何身份。以(36)分别计算两端点，可完全绕过当前 eta48 坐标里的 Hecke 线性 gcd；(40)仍应作为准确全局等式检查。对已经由原三个退化函数及 $y_s$ 组成的表达式树，(41)直接给 $W$ 的作用。它不声称已经计算 $W$ 在整个任意 $R_1^Y$ 基上的矩阵。

## 8. 保持原角色的 shadow 消费接口

现在取原 $k=\mathbf F_{r^2}$ 并保留原 $\omega$。有限代数可先在 $\mathbf F_r$ 构造再基变换，也可直接在 $k$ 构造；两种方式必须保实际 $k\hookrightarrow\kappa(Q)$，不能按一个无关本原元重新选择 $\omega$ 的像。

### 8.1 原函数对象和准确全局运算

用三元组 $(m,A,B)$、$A,B\in R_m^Y$、$B\ne0$，表示函数 $A/B$。不同分次先准确同次化；加乘和等号比较都用已认证的完整乘法。等号通过 $AD-BC=0$ 的全部忠实 jet 检验，不从随机点或短前缀决定。`divisor(A/B)` 由§5的两个完整零截面代数取差；`valuation`、`reduce` 和闭点比较由同一局部因子实现。这是原函数域的具体分式实现，不需要先把它转成某个 $k(t)[X]/P$。

常数共轭只对 $k$ 系数作 $c\mapsto c^r$，固定原有理全局基、$u$ 及 $y_s$。消费者中的 $f^r$ 则是函数的真正 $r$ 次幂，含变量 Frobenius。原 Artin 置换仍单独使用 $[2,0,1]$；这三种运算不能相互替代。

### 8.2 原 F、两条 P 与全部尺度

沿用 `original_shadow_relative_six_tools.py::fixed_artin_constants` 的同一常数构造和全部断言，保原 $a_{17}$、$v_i$、$\lambda_i$、$v_{\rm new,i}$、原 $\omega$ 和 $\theta_{17}$。具体有
$$
\theta_{17}^6=17,\quad\theta_{17}^r=-\theta_{17},\qquad
h_i^3=2^{32}v_i,\quad
d_i=\lambda_i h_i/2048,\quad2d_i^3=v_{\rm new,i}.
\tag{42}
$$
$h_i$ 的顺序仍由原 Artin 序列和原 $\ell(v)$ 多项式逐步运输；不以独立开三个立方根替代。换成截面分式模型不改变这段常数代码或原回执中的 embedding 顺序。

将§6恢复的原坐标沿(36)拉回，定义
$$
\varepsilon=-\frac{\pi_2^*T\,y_s(v-8)v^3}{(v+4)^6},\qquad
f_0=\frac{v+4}{v}\frac{\pi_2^*R_F}{\theta_{17}^2},\qquad
y_F=\frac{\pi_2^*v_F}{\varepsilon\theta_{17}^3},
\tag{43}
$$
$$
x_{i,0}=\frac{N_0^2}{v^3}\frac{\pi_1^*R_i}{d_i^2},\qquad
x_{i,2}=\frac{(v-2)^2}{v}\frac{\pi_4^*R_i}{d_i^2},\qquad
y_{i,j}=2\pi_{2^j}^*Y_i/v_{\rm new,i}+1\quad(j=0,2).
\tag{44}
$$
这里 $x_{i,j}$ 是原目标 $x$ 坐标除以源 $x_s$ 后的函数，绝不是重新选的目标坐标；$x_s^3=v$。原第一因子的 $(v+4)/v$ 因子和 $\varepsilon$ 均完整保留。逐个验证
$$
y_F^2=vf_0^3+1,\qquad y_{i,j}^2=vx_{i,j}^3+1
\tag{45}
$$
及 R883 已证明的 $W$ 与常数反射等式。

### 8.3 完整交除子与闭点读者

首先用实际完整除子核对：$\operatorname{Supp}\operatorname{div}(T\circ\pi_2)$ 是全部108个几何 cusp；$v$ 的零极只在这些 cusp；$3\nmid v_Q(v)$ 的分歧部分次数54。原各 $y_{i,0},y_{i,2}$ 极次数为2256，而 $d_F=\deg\operatorname{pole}(y_F)>0$ 必须由实际完整除子读取，不能从一个猜测表输入。

按现有消费者的同一循环对称性：若 $d_F<2256$，求交输入是 $\mathcal A_aq_0$ 与 Frobenius $F$，输出 $\mathcal A_bq_2$；否则求交输入是 $\mathcal A_bq_2$ 与 Frobenius $\mathcal A_aq_0$，输出 $F$。记所选原输入为 $(a_0,y_1)$、$(x_p,y_p)$，输出为 $(x_o,y_o)$，均采用除以 $x_s$ 的横坐标，则
$$
c_0=v^{(r-2)/3}x_p^r,\quad y_2=y_p^r,\quad
g=y_1-y_2,\qquad
E=\operatorname{div}(g)+\operatorname{pole}(y_1)
  +r\operatorname{pole}(y_p).
\tag{46}
$$
各项都由实际截面分式和完整零代数得到。必须核 $g\ne0$、$E\ge0$，并核
$$
\deg E=\begin{cases}2256+r d_F,&d_F<2256,\\2256(r+1),&d_F\ge2256.\end{cases}
\tag{47}
$$
特别不能只取 $g$ 的仿射零点，或删掉分子分母共零后省略极点项。

对每个实际 $Q\in\operatorname{Supp}E$，读取完整 $e_Q=E(Q)$、$d_Q=[\kappa(Q):k]$、$v_Q(v)$ 及各函数的完整阶。若 $3\nmid v_Q(v)$，按 R883 原 CM 等变性，贡献是三挠，乘6后零，但其完整 $e_Qd_Q$ 仍记入总次数。否则令 $s=v_Q(v)/3$，
$$
\alpha_Q=s+v_Q(a_0),\qquad\gamma_Q=2s+v_Q(c_0).
$$
若两 $y$ 坐标有极，取
$m_Q=\min\{-v_Q(y_1)/3,-v_Q(y_2)/3\}$；若两者有限且 $\alpha_Q,\gamma_Q>0$，取 $m_Q=\min(\alpha_Q,\gamma_Q)$；其余取零。保留原
$$
k_Q=e_Q-3m_Q\ge0.
\tag{48}
$$
当 $k_Q>0$ 时核 $\alpha_Q=\gamma_Q$。若输出在 $Q$ 有极，其射影值为 $O$；否则由§5的共同局部参数约消读取
$$
P_Q=\operatorname{red}_Q(a_0x_o/c_0,y_o)\in E_0(\kappa(Q)),
\qquad E_0:y^2=x^3+1.
\tag{49}
$$
必须在实际剩余域验证椭圆方程及原 $k$ 嵌入。由 R883 的完整 Cartier 拉回证明，所有共同交重、分歧边界和任意高阶相消都已经体现在(46)–(49)；本篇提供的是这些式子所需的真实闭点和局部 Artin 读数。

最后保持原完整迹
$$
\sum_Q k_Q\operatorname{Tr}_{\kappa(Q)/k}([6]P_Q),
\qquad
[6]\operatorname{Tr}P_Q
=\left[\frac{1-(-r)^{d_Q}}{\ell}\right]P_Q,
\quad\ell=(r+1)/6\in\{5,7\}.
\tag{50}
$$
可直接调用原 Tate reader；若用右式，也必须先保完整整数 $d_Q$，最后才在 $\ell$-挠点上约化。仍计算原四组 $(a,b)=(0,0),(0,1),(1,1),(1,2)$，其余五组只用原已证明 $W$ 和常数反射生成；随后把全部九点给原18×9、双轴及 $A/C$ 读者。没有改动原循环、通常 Selmer 桥或任何 CM/Artin 尺度。

## 9. 实际证明范围、回执和成本

本篇已经证明：从同一原光滑曲线的完整分次空间与乘法，可无损恢复任意真实截面零除子的全部闭点、非约化长度、剩余域、局部参数及函数值；原 $T/U/V$、原根和原三退化也有全部有限步骤的准确接口。故 eta48 正规化并不是数学上不可绕过的前置条件。

执行回执应分开记录如下已经完成的实际对象：完整格及其原构造器/饱和变换；实际乘法和满秩高权基；截面 $s$ 的真实全坐标；两个商、单位截面 $h$ 及返回乘法；全部 Frobenius、幂等元、残域和局部长度；若进入 consumer，再记录原全部函数、交除子、每个闭点贡献和最终18×9读数。只给某个原全局格或 $D_S$/cusp 代数，不能称四个大交除子已付。

实现中的完整 q-窗检验可使用以下等价消元：若 $R_m$ 基矩阵 $B$ 有 $d$ 行，在全部 $b$ 个忠实 jet 列上秩 $d$，固定可逆的 $d$ 个列 $J$。对候选行 $v$，令 $c=v_JB_J^{-1}$。则 $(v-cB)_J=0$ 是定义上的恒等式；只需检查其余全部 $b-d$ 列为零，就等价于全部 $b$ 列归属检验。特别 $R_4$ 的 $b=817,d=732$ 留85列，不能再删其中任何一列。回执应记固定列序、$J$、可逆子矩阵、所有非 pivot 残差检查及相应 hash；这不是缩短 Sturm 门。

完整相对六次方案仍须实际构造 $Y$ 的666维全局空间，并在所需高权达到(31)的完整维数。对于(47)可达67680或94752的交除子，直接一次形成整个商可能很大；定理1只保证有限、正确和无正规化依赖，不保证该未经分块/约简的实现比现有函数域路线更快。要分解或递归切割以节省资源，仍须保全部局部因子和次数之和。这里只把工程瓶颈换成一个有准确尺寸和失败判据的线性代数输入，未把尚未运行的输入写成 PASS，也未由有限代数的形状预告原 shadow 非零。

### 原始来源与依赖

- [R917](R917-original-global-rr-lattice-from-saturated-q-jets.md)：原完整格、好模型、q-jet 单射及局部饱和；本篇不重复其公开计算。
- [R881](R881-original-good-prime-direct-coordinate-reconstruction.md)、[R882](R882-original-degree18-source-model-and-two-endpoint-coordinates.md)、[R883](R883-original-relative-six-shadow-and-complete-boundary.md)：原已认证映射的低核读法、真实源/端点、全 cusp 阶和完整 shadow 公式。现有脚本 `original_shadow_coordinate_tools.py`、`original_shadow_relative_six_tools.py`、`original_shadow_local_divisor_tools.py` 给本文接口所逐项保留的消费语义。
- Kamal Khuri-Makdisi, *Linear algebra algorithms for divisors on an algebraic curve*, Math. Comp. 73 (2004), 333–357；[原文](https://arxiv.org/pdf/math/0105182)，尤其§1的完整 Riemann–Roch 空间及乘法表示。本文定理1、3给所需有限代数和原分式恢复的自足证明，不借一般 Jacobian 算法替代实际闭点。
- Brian Conrad, *Structure near the cusps*, 2001 课程讲义，[原文](https://math.stanford.edu/~conrad/vigregroup/vigre01/cusps.pdf)；完整 Tate cusp 模型及其参数标号。原 cusp 域与 Galois packet 公式亦见 [Magma 官方手册：Cusps and Rational Points](https://magma.maths.usyd.edu.au/magma/handbook/text/1670)。
- PARI/GP 官方 [Modular forms](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Modular_forms.html)：`mfinit` 的 flag 4 为完整模形式空间、flag 1 为完整 cusp 空间；`mfbasis` 对 trivial character 的基系数在 $\mathbf Q$，`mfcoefs` 延长同一实际全局基。其“generalized modular forms”说明也要求先有全局模形式身份，不能将任意形式导数或商自动视为模形式。

