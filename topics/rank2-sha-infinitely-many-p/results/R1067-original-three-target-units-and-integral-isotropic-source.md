# R1067 原三目标单位与完整各向同性来源

本文件接[§§37–55](R1067-original-first-wild-fixed-geometric-tail.md)，并保[原证](R1067-original-first-wild-rubin-even-multiplicity.md)与[§§16–36](R1067-original-first-wild-rubin-native-euler-continuation.md)的全部物理来源、Euler、参考与完成边界。

## 56. 原六次扭曲域内的三个真实 Fourier 分量及其正相对号

令 $\theta=17^{1/6}>0$，$K=\mathbf Q(\omega)$，$F=\mathbf Q(\sqrt{17})$。
(V2)的实际域为
$$
 L=F(B_0,B_1,B_2)=K(\sqrt{17},\sqrt[3]{17})=K(\theta).
 \tag{X1}
$$
先说明完整的类域识别。$K$ 类数一，导子十七的环类群为
$\mathbf F_{289}^{\times}/(\mathbf F_{17}^{\times}\mu_6)$，阶六。
$G_K$ 在所有十八条十七核模 $\mu_3$ 的作用恰是此商的 Artin
作用：R290(3)的 $E_1$ 本原基角色在素于 $2\sqrt{-3}\,17$ 的主
理想上是相应生成元乘六次单位，投影恰好消掉这个单位和有理标量。
中国剩余定理可取任意给定的十七处单位及 $2\sqrt{-3}$ 处的标记；
因此作用满射。其核切出该环类域 $H/K$。在 $G_{FK}$ 上，平方半集
的三轨道保留此群的三次方向；在 $G_K$ 上，其奇偶半集切出的二次域
是 $FK$（(V1)后的行列式计算）。由(V2)，$L$ 已含 $FK$。所以
$L=H$，例如比较 $G_{FK}$ 上的共同三阶商以及总次数即可。

$K(\sqrt[3]{17})/K$ 是在十七处有分歧的三次循环扩张。
在三处 $-17\equiv1\pmod9$，由三进对数的
$3(3\mathbf Z_3)=9\mathbf Z_3$ 可知 $17$ 在 $\mathbf Q_3$
为立方。其余不整除 $3\cdot17$ 的素数处，Kummer 单位扩张未分歧。
十七处是 tame，导子指数一；其三次局部角色在阶十六的
$\mathbf F_{17}^{\times}$ 上平凡。因此这个三次域包含于 $H$。
与已知二次域 $FK$ 合成即为 $H$，得到(X1)。复共轭固定
$\infty$ 轨道，所以 $F(B_0)=F(\sqrt[3]{17})$；
(V2)与 $\sum B_i=0$ 还给 $B_0$ 在该三次域基
$1,\sqrt[3]{17},\sqrt[3]{17^2}$ 上的常数项为零。

令 $i=0,1,2$ 依次取(S4)的轨道，$Z_i=\Pi H_{j_i}$。
在共同物理 $E_1$ 上，取 R307(3) 的三条有理截面
$S_1,H_3,H_5$，后两行取 $b=1$ 且质量一。三个固定 Fourier
分量的**准确**等式是
$$
 \begin{split}
 a=3\sum_i\omega^{-i}B_i,\qquad b=3\sum_i\omega^iB_i,\\
 9Z_i=S_1+\omega^i a H_3+\omega^{-i} b H_5,\qquad
 9B_i=\omega^i a+\omega^{-i}b .                               \tag{X2}
 \end{split}
$$
事实上 R306(8)–(12)在同一有限 Weil 基中给原 $k=1,3,5$
三个特征在 $g_0$ 上的值分别为 $\omega^2,1,\omega$，其实际
射影和都取 $9\sqrt{17}\Pi_ke_0$。第 $l$ 项的共同额外符号为
$(y_l/17)$，指数亦相同；目标 $k=1$ 权为 $\omega^l$，
$k=3$ 相比乘 $\omega^{-l}$，$k=5$ 相比乘 $\omega^l$。
$\infty$ 与 $l=3,6$ 在 $I_0$，$l=1,4,7$ 在 $I_1$，
$l=2,5,8$ 在 $I_2$，与(S2)逐个标记吻合。二、三处原 Schwartz
及 Hermite 源相同，故另两条未归一行就是
$3\sum\omega^{-i}Z_i$、$3\sum\omega^i Z_i$。R307 以完整
$M_{\gamma_{13}}$ 的单重特征空间及原点质量识别它们的有理物理行，
取实际质量给 $aH_3,bH_5$。对三个分量作 Fourier 反演即为(X2)。

两个真实常数之相对号可直接决定：
$$
 \boxed{\displaystyle {a\over b}={17^{1/6}\over3+\sqrt{17}}>0.}\tag{X3}
$$
先用 R306(20),(21) 的共同未归一 Hermite 零权质量
$b_{3,0},b_{5,0}$，则 $a/b=b_{3,0}/b_{5,0}$；这是(X2)中相同
前因子下的两行，未把两个平方根分别重选。R307(13)给两个原
$L/\Omega$ 分别是 $3,6$，R306 给 $C_3/C_5=13+3\sqrt{17}$。
各自实际实周期之比 $\Omega_{17^3}/\Omega_{17^5}=17^{1/3}$。
故
$$
 (a/b)^2={17^{1/3}\over 2(13+3\sqrt{17})}
         ={17^{1/3}\over(3+\sqrt{17})^2}.                       \tag{X4}
$$

以下用原标记固定符号。复共轭保持 $B_0$、交换 $B_1,B_2$，
所以 $x=B_1/B_0$ 满足 $\operatorname{Re} x=-1/2$。按(S2)，设
$b_* =t_2e_8^{-1}$、$g_*(\tau)=\Theta_g(\tau,0)/\delta_0$，
$w=(1+s)/17$、$v=-1/w$。由 $\tau_{13}=3+w$、二阶 theta 的
$T^3,S$ 变换，准确有
$$
 g_*(3+w)={(1-ib_*)\vartheta_{2,0}(v,0)
              +(1+ib_*)\vartheta_{2,1}(v,0)\over\sqrt{-2iw}} .
$$
$|1-ib_*|=\sqrt2$、$|1+ib_*|=1+\sqrt3$，
$\operatorname{Im}v=17\sqrt3/14>2$。置
$Q=e^{-\pi\operatorname{Im}v/2}<1/20$。直接将偶、奇 theta
级数取绝对值，偶项非恒总和不超过 $2Q^4/(1-Q^{12})$，奇项总和
不超过 $2Q/(1-Q^8)$。故模分别小于 $1.001$, $0.101$，上式分子
的模小于 $1.70$。另一方面
$\sqrt{2|1+s|}=\sqrt{2\sqrt{7/3}}>1.74$；
$\operatorname{Im}(17s)>14/3$ 给相应 $Q_\infty<1/1000$，
同一几何级数的反三角不等式及 $|b_*|<2$ 给 $|g_*(17s)|>0.995$。
(S2)因此给严格不等式
$$
 |x|={|g_*(3+w)|\over\sqrt{17}|g_*(17s)|}<1 .
$$
于是 $|\operatorname{Im}x|<\sqrt3/2$。$a/(3B_0)$ 和
$b/(3B_0)$ 分别是 $3/2+\sqrt3\operatorname{Im}x$ 和
$3/2-\sqrt3\operatorname{Im}x$，两者都严格正，证明(X3)。
这个符号用的是原 Jacobi 及 Schwartz 标记的解析界。

## 57. 两个实际秩零 Rubin 单位的共同一阶项与任意精度的纯对数层读取

以 $E_{\rm base}:y^2=x^3+1$ 为共同局部整模型，令
$E^{[k]}:y^2=x^3+17^k$，$k=1,3,5$。沿用(X2)的物理行，令
$J_3,J_5$ 为 R308 §6 在共同 $E_{\rm base}$、同一 $c$ 与 charge
$34$ 下的两个 Newton 函数。两者均有常数一，且属于
$1+p\mathbf Z_p\langle u\rangle$。设
$$
 X=J_p/J_5,\quad Y=J_3/J_5,\quad t_i={\omega^ia\over9B_i},\quad
 h_i={1\over9B_i}.
$$
由(X2)在同一个线性读者中逐项读出
$$
 J_p[Z_i]/(B_iJ_5)=1+t_i(Y-1)+h_iX.                            \tag{Y1}
$$
这里 $X(0)=0,Y(0)=1$。对(U6)中任取的基准轨道 $i_0$，
$(\log V_i)'(0)$（$i\ne i_0$）准确为
$$
 (t_i-t_{i_0})Y'(0)+(h_i-h_{i_0})J_p'(0).                      \tag{Y2}
$$
可以在选择局部反射的固定轨道后重新标记；循环相位须随(X2)一起移动。

令 $\mathcal O=\mathcal O_{K_p}$，$\Lambda_p=\mathcal O[[T]]$，
$T=\gamma_{\rm ac}-1$。用各曲线的 primitive CM Betti 标记、实际
Néron 微分及 R303(9),(14)相同的整图，把各自的标准椭圆单位
局部类 $\xi_k$ 经 $F_{\theta^k}^*$ 送至共同 $M^+$。写
$\widehat\xi_k=\mathcal A_k(T)\xi_{\rm base}$。
两条 rank-zero 曲线的根数均正，R307(13)的 $L/\Omega=3,6$
在 $p>211$ 为单位，$\varpi/\Omega=s$ 也为单位。BKO24
Cor. 4.11(i)的原整基论证同 R303 §3 给
$\mathcal A_3,\mathcal A_5\in\Lambda_p^\times$。这两个是真正标准
局部椭圆单位类的坐标，而非事后选取的分析函数单位。定义
$$
 U_p(T)={\mathcal A_3(T)/\mathcal A_5(T)\over
                \mathcal A_3(0)/\mathcal A_5(0)},\qquad
 R_p(T)^2=U_p(T),\quad R_p(0)=1.
$$
因 $p$ 为奇数，$1+T\mathcal O[[T]]$ 中有唯一此平方根。

在整个 $u$ 盘有
$$
 Y(u)=R_p(q_{\rm ac}^{du}-1),\qquad
 Y'(0)=d\log(q_{\rm ac})R_p'(0).                                 \tag{Y3}
$$
证明是将(111)的同一 primitive tensor / dual exponential 比较直接
用于 $E^{[3]},E^{[5]}$。两条导子均为 $(2\sqrt{-3}\,17)$；
R306 已证各自的 tame 分量，$m=dn$ 时两条真正同一反圆分角色为
$(\psi_k/\bar\psi_k)^m$。共同辅助 smoothing、同一 Gamma/Tate
及 $p$ 处两份非单位 Euler 因子 $1+1/p$ 都先保后消；十七处两条
均为 primitive 分歧行。唯一模型权因子是
$(\theta^3/\theta^5)^{-(2m+1)}$，固定 Betti 单位之比记
$\kappa_{35}$，同(111)在取临界值前由整基定下。R307(16)的临界
比是
$$
 {3\over6}(\theta^3/\theta^5)^{2m}
   \left({[z^m]H_3\over[z^m]H_5}\right)^2 .
$$
这里因质量均一，物理 $E^{[k]}$ 上的第 $m$ 次系数恰为
$\theta^{km}[z^m]H_k$。故两个随 $m$ 的模型幂**全消**，留下
$\kappa_{35}\theta^2/2$。两个 charge 都是 $34$，故 $d\mid m$
时最后的系数比就是 $Y(n)$，连同其 Gaussian 与 $n!$ 一起成立。
由正整数的稠密性先在整盘得到
$(\mathcal A_3/\mathcal A_5)(q_{\rm ac}^{du}-1)
       =\kappa_{35}\theta^2Y(u)^2/2$；置 $u=0$ 得它的准确归一，
再用常数均一选定根，证明(Y3)。因此原中央坏等价于(Y2)两个真实
对数导数均准确等于
$(t_i-t_{i_0})d\log(q_{\rm ac})R_p'(0)$。反向甚至可只用其中一条，
因为由(V2)，$h_i\ne h_{i_0}$。

这一个原 Rubin 系数有纯有限层的 logarithm 读取。任选 $r$ 个
不同的非平凡本原层 $n_1,\ldots,n_r$，使对应反圆分字符
$\chi$ 都在 BKO24 的 $\Xi^-$（三条曲线的原符号为正）。
写 $D(T)=\prod_{j=1}^r\Phi_{p^{n_j}}(1+T)$。在相应根
$\eta=\chi(\gamma_{\rm ac})$，将定义 $U_p$ 的两个全局标准类的
$\chi^{-1}$ 本征投影先局部化、再经各自 $F_{\theta^k}^*$ 送入
**同一** $E_{\rm base}$ 局部整表示，记为 $\widehat z_{k,\chi^{-1}}$。
以 $\lambda_{\rm base}$ 表示该共同微分及标记的 Bloch–Kato / 形式群
对数。BKO24 Th. 3.16(a), (3.17) 给
$$
 U_p(\eta-1)
 = {\lambda_{\rm base}(\widehat z_{3,\chi^{-1}})\over
        \lambda_{\rm base}(\widehat z_{5,\chi^{-1}})}
       {\mathcal A_5(0)\over\mathcal A_3(0)}.                    \tag{Y4}
$$
这里共同 $v_-,v_+$ 先由本地整同构配对，才取消同一
$\delta_{\chi^{-1}}(v_-)$，故无独立选取的秩一周期。
$\widehat z_5$ 是单位倍的共同基，(3.17)与非零互易因子保证
分母非零。该公式是真实椭圆单位 Selmer 类的对数；只有另满足原文
的秩一假设时才将它识别为代数点张量中的类。

在同一 $\mathcal O$ 内准确有
$$
 2R_p'(0)\equiv
 -p^r\sum_{D(\eta-1)=0}{U_p(\eta-1)-1\over(\eta-1)^2D'(\eta-1)}
       \pmod {p^r}.                                             \tag{Y5}
$$
确实 $f=(U_p-1)/T\in\mathcal O[[T]]$，$D$ 首一且 distinguished。
其 Weierstrass 除法余式 $P$ 系数整且次数小于 $\deg D$，又
$D(0)=p^r$，故 $f(0)\equiv P(0)\pmod{p^r}$。对所有简单非零根
应用 Lagrange 插值即得(Y5)，无需给每一分项单独主张整性。于是对
任意精度 $r$，(Y4)在**只有**反号层中已给一个真实的有限输入。
同一(Y5)也可只用 $r$ 个 $\Xi^+$ 的非平凡层；这时由 BKO24
Prop. 3.1(3.3) 读共同 dual exponential 的比，再乘
$\mathcal A_5(0)/\mathcal A_3(0)$，原始临界值和各自实际微分如
上述比较保留。任一取法均给同一个 $2R_p'(0)$ 模 $p^r$。

原复函数方程中的反射将 R306 的单位化特征
$\chi_k^{2m+1}$ 换至其逆，对应 $m'=-m-1$。
当 $m\equiv0\pmod {p+1}$ 时 $m'\equiv-1\pmod {p+1}$；
故该反射没有把(Y3)的同一 $u=0$ 槽赋为偶函数。BKO24 Th. 3.16
的对数等式给有限特征的**值**，(Y5)把它们送入原一阶项所需的任意
精度；其极限还没有被识别为单个固定全局代数点或全局单位的对数。

## 58. 三个真实投影的绝对系数及其 Pell 范数

保持(X2)原字母及 $\theta=17^{1/6}>0$。两个绝对常数为
$$
 b=-{1\over168\theta^2},\qquad
 a=-{1\over168\theta(3+\sqrt{17})}.                             \tag{Z1}
$$
因此(X2)给每个 $Z_i$ 的整个固定代数截面，特别
$B_i=(\omega^i a+\omega^{-i} b)/9$ 中没有未定共同倍率。

先定 $b^2$。同一 Hermite 变量、共同物理 $E_1$ 和同一未归一
Schwartz 框架下，目标 $k=1$ 行是 $S_1$，而 $k=5$ 行是 $bH_5$，
由(X2)已付。故 R306(20)（$C_1=C_5$）给两条原 $L$ 值的比
$b^2([z^m]H_5/[z^m]S_1)^2$。可直接用 $m=6$：两分母非零。
另一方面 R298、R307(16) 各自以原始周期付出的完整中央值给
$$
 {L(\psi_5^{2m+1},m+1)\over L(\psi_1^{2m+1},m+1)}
 ={6\over\kappa_0}
 (\theta^{-4})^{2m+1}
 {\theta^{10m}\over\theta^{2m-12}}
 \left({[z^m]H_5\over[z^m]S_1}\right)^2 .
$$
幂次依次来自 $\varpi_{17^5}/\varpi_{17}$、原 $E_{17^5}$ 的质量一
截面及原 $E_{17}$ 的六阶首项归一截面；后者不能当质量一缩放。
$\kappa_0=2^7 3^3 7^2 17^2$，故
$b^2=6\theta^8/\kappa_0=(168\theta^2)^{-2}$。

以下直接由 $H_\infty$ 的原物理六次项固定共同号。置
$y=z/\Omega$、$K_0=34\sqrt3\pi$、$R_0=34\pi/\sqrt3$，并令
$A_0=\exp(-17\pi/(4\sqrt3))$。原 $H_\infty/B_0$ 为
$e^{K_0y^2}\Theta_g(17s,17y)/\Theta_g(17s,0)$。
在 $\Theta_g$ 除以 $\delta_0$ 后，$n=0$ 的 Jacobi 系数为一；
$n=\pm1$ 均为 $t_2 A_0$，因原 $e_8^{-1}$ 与
$e^{17\pi i/4}$ 相消。任意第 $n$ 项对 $y^6$ 的额外倍率是
$K_0^3 P(R_0n^2)/6$，其中
$$
 P(X)=1-3X/2+X^2/4-X^3/120.
$$
$61<R_0<62$，$P(61)<-1000$ 且 $P$ 在 $[61,\infty)$ 递减。
$1/3200<A_0<1/1000$ 由 $7<17\pi/(4\sqrt3)<8$ 及
$e^7>1000,e^8<3200$ 得。于是 $n=0,\pm1$ 对归一六次分子的
贡献小于 $1-3800/3200$。对 $|n|\ge2$，
$|P(R_0n^2)|<4000 n^6$，每个 Jacobi 系数的模至多
$2 A_0^{n^2}$。双侧尾模小于
$16000\sum_{n\ge2}n^6 10^{-3n^2}<0.001$，例如用
$n^6\le64^{n-1}$、$n^2\ge2n$ 求几何和。该物理分子为实负数；
归一零次分母为正，由(X3)证明中的界或同一 $n=0$ 主项即知。
故
$$
 [z^6]H_\infty/B_0=[z^6]Z_0/B_0<0.                               \tag{Z2}
$$
R297 的 $[z^6]\log(\sigma/z)=1/210$、$[z^6](z^2x)=-1/7$
给 $[z^6](\sigma^{34}x^{17})=-34/15$。由 R307(3)，
$[z^6]H_3=-208-34/15$, $[z^6]H_5=272-34/15$。置
$\rho=a/b=\theta/(3+\sqrt{17})\in(0,1)$。由(X2)，(Z2)的左边
等于
$$
 {1/b+\rho(-208-34/15)+272-34/15\over1+\rho}.
$$
分子的后两项之和严格为正，故 $b<0$。结合(X3)即证(Z1)。

作为真实零权常数的核验，三次乘积准确给
$$
 \prod_{i=0}^2(9B_i)=a^3+b^3
   =-{45(4+\sqrt{17})\over
           168^3\,17\,(3+\sqrt{17})^3}.                         \tag{Z3}
$$
这里用 $(3+\sqrt{17})^3+\sqrt{17}=45(4+\sqrt{17})$。
$4+\sqrt{17}$ 是范数 $-1$ 的实际 Pell 单位；(Z3)是质量的
乘法等式，未将这个固定因子提升成 $u$ 的指数。

## 59. 三中心 Eisenstein 比在每个大权逃出全部固定 S-unit，及完整中央的有限对数判据

本节的 $S$ 是任意**先固定**的有限有理素数集；结论的下界可依赖
$S$。仍用(V2)的固定域 $L$ 及物理标记 $i=0,1,2$。写
$c_i(d)=-G_d(\Lambda_{D_i})/d$、$u_d=c_1(d)/c_0(d)$、
$v_d=c_2(d)/c_0(d)$。对所有充分大的 $6\mid d$ 有
$$
 u_d^m v_d^n\in\mathcal O_{L,S}^{\times}
          \quad\Longrightarrow\quad (m,n)=(0,0)\quad(m,n\in\mathbf Z).
 \tag{AA1}
$$
这里 $\mathcal O_{L,S}$ 反演 $S$ 上的全部素位。

先付所需的指数精度。(W2)中 $D_0$ 的最短向量为
$\pm w_0=\pm\Omega/17$。$D_{13}$ 的最短向量也只有一对，
可取 $w_1=\Omega(1+s)/17$：范数七的整数正是 $2-\omega$ 与
它的共轭的六个单位倍。这两类在核上分别给(S4)的 $I_1,I_2$
（共轭将 $13$ 送到 $8$）；$\mu_3$ 的射影作用无稳，故每条核
恰承载一对。若 $m'$ 是相应格的次小非零长度，最短对外各项
相对绝对值的和至多
$(|w_i|/m')^{d-4}\sum_{v\ne0}(|w_i|/|v|)^4$。
因 $d$ 偶，两最短项的相位全同；故对于某个固定 $0<q<1$，
$$
 u_d=\kappa^d(1+O(q^d)),\qquad
 \kappa=w_0/w_1=(1+s)^{-1}\in K,\quad |\kappa|=\sqrt{3/7}<1 .
 \tag{AA2}
$$
这个估计是复数本身的，含其相位。它也证明分母和分子最终非零。
同一固定十三处三循环给 $v_d$ 最终非零。

绝对对数 Weil 高度有 $h(u_d)=O(d\log(2d))$。对每个固定目标
用 $D_z$ 表示不变导子，乘二的极展开给
$$
 4x_D(2z)=\sum_{T\in E_D[2]}x_D(z+T)
                        -\sum_{T\in E_D[2]-0}x_D(T).
$$
比较 $z^{d-2}$，用
$[z^{d-2}]x_D=(d-1)G_d(\Lambda_D)$，得到
$$
 (2^d-1)(d-1)(d-2)!\,G_d(\Lambda_D)
        =\sum_{T\in E_D[2]-0}(D_z^{d-2}x_D)(T).                \tag{AA3}
$$
在含所有固定曲线、二挠及其系数的固定数域内，取正整数 $M$ 使
$X=M^2x_D,Y=M^3 y_D$、$M^4g_{2,D}/4$、$M^6g_{3,D}/4$
在各所需点整。导子 $D'=MD_z$ 满足
$D'X=2Y,\ D'Y=3X^2-M^4g_{2,D}/4$，故(AA3)右边乘 $M^d$
是代数整数。对每个复嵌入，在非零二挠点附近取固定无极圆盘，
Cauchy 估计使这些整数的全部共轭绝对值有界于 $C^d(d-2)!$。
共同的(AA3)左侧标量在取比时准确消去，由高度的积与商不等式即得
所述上界。特别 $h(u_d/\kappa^d)=O(d\log(2d))$。

假如 $u_d$ 在固定 $S$ 外没有零极，可略增这个固定集以使
$\kappa$ 为 $S$-unit。于是 $x_d=u_d/\kappa^d$ 在固定有限生成
$S$-unit 群中。在一组固定自由部分基中写
$x_d=\zeta\prod\epsilon_j^{b_j}$。$S$-unit 对数嵌入及积公式
给 $\max|b_j|=O(1+h(x_d))$：固定基向量独立，所有对应
$S$-绝对值的对数均由高度控制。以固定复对数支写 $\log x_d$，
只需再加整数倍 $\log(-1)=\pi i$ 将虚部带回主区间，
该整数亦为 $O(1+\max|b_j|)$，有限个 $\zeta$ 可逐一吸收。
若 $x_d\ne1$，Matveev 的原始复线性对数下界给
$|\log x_d|\gg(2+d\log(2d))^{-C'}$，所用数域、各对数及
$C'$ 固定。这同(AA2)中 $|\log x_d|=O(q^d)$ 矛盾。
准确条款是 E. M. Matveev, *An explicit lower bound for a
homogeneous rational linear form in the logarithms of algebraic
numbers. II*, Izv. Math. **64** (2000), Cor. 2.3, (2.6)，取
(1.4)的 $B^*$。[原刊全文](https://www.mathnet.ru/links/81dfabe819b107280a94d7cb7ae94324/im314_eng.pdf)

剩下的准确相等等式 $u_d=\kappa^d$ 也不可能：十三处三循环固定
$K$，其轮换三个 $c_i$，迫三个相邻之比都等于同一 $\kappa^d$，
乘积一，与 $|\kappa|<1$ 矛盾。这证明每个充分大的合法 $d$ 上
$u_d$ 都有一个 $S$ 外零或极。最后以 augmentation 格
$A_2=\{(n_0,n_1,n_2)\in\mathbf Z^3:\sum n_i=0\}$ 取映射
$(n_i)\mapsto\prod c_i^{n_i}$，目标为
$L^\times/\mathcal O_{L,S}^\times$。这是 $G_F\twoheadrightarrow S_3$
等变的。目标无挠（看 $S$ 外赋值），$A_2\otimes\mathbf Q$ 是
不可约标准表示，已证 $u_d$ 非 $S$-unit，故有理核为零，得到(AA1)。

现在取 $d=p+1$、$p$ 为固定坏集外的惰性素数。在 $L$ 的**每个**
$p$ 进嵌入，(U3)给 $u_d,v_d\in1+p\mathcal O$。定义下述
$\overline{\mathbf Q}$ 向量空间 $\mathscr P_{S,p}$：它由 $1$、
全局代数 $S\cup\{p\}$-unit 的 $p$ 进对数，以及定义于
$\overline{\mathbf Q}$ 上的阿贝尔簇之代数点的 $p$ 进对数在
代数 Lie 基中的坐标生成。每个元素只取有限和；相应代数数域、
阿贝尔簇、点和代数系数均允许依赖 $p$。乘法对数取
$\log_p(p)=0$ 的通常支；正规化一个代数数的所选赋值时，只须乘
$p$ 的有理次幂，仍为代数 $S\cup\{p\}$-unit。则
$$
 \log_p u_d,\log_p v_d
 \text{ 在 }\mathbf C_p/\mathscr P_{S,p}
              \text{ 中在 }\overline{\mathbf Q}\text{ 上线性独立}.
 \tag{AA4}
$$
先只考虑乘法部分的有理关系。如果一条非平凡整数幂
$u_d^m v_d^n$ 的对数在有限个相应 $S\cup\{p\}$-unit 对数的
有理张成空间内，清分母并用代数局部点的对数核
$\mu_\infty p^{\mathbf Q}$，得到 $u_d^m v_d^n$ 在 $S,p$ 外均为单位。
它在全部 $p$ 位本来也为单位，故已经是 $\mathcal O_{L,S}^\times$
的元素，违反(AA1)。即使比较的 $S\cup\{p\}$-unit 位于
$L$ 外的有限扩张，赋值的限制给同样结论。

为付代数系数与阿贝尔对数，取任何声称存在的有限代数线性关系。
从所用乘法对数张成的有理空间取基，可保留 $\log_p u_d,\log_p v_d$
并用若干 $S\cup\{p\}$-unit 的对数补足。将所用阿贝尔簇取乘积
$A$，以 $G=\mathbf G_a\times \mathbf G_m^r\times A$ 及代数点
$(1,u_d,v_d,\ldots,P)$ 应用 Fuchs–Pham 的 $p$ 进解析子群定理
Th. 1.1（与§55同原刊，第337页）。乘法部分可先正规化至单位，
点或其一致正整数倍均在该定理的对数域中。若关系存在，定理给
包含此点的代数子群，其 Lie 代数落在所声称的超平面。该点在
乘法环面投影上的循环群 Zariski 稠密，因为所选 $r$ 个对数在
$\mathbf Q$ 上独立，任何代数子环面的字符关系都会违反这一点。
而 $\mathbf G_a\times A$ 的任何连通代数子群都无非平凡环面商：
它的阿贝尔部分与加法部分无相互非零同态，阿贝尔簇到环面亦无
非零同态。由子群对两投影的共同商描述，所给子群的连通部分必含
整个 $\mathbf G_m^r$（也可先取一致有限倍再用相同稠密性）。
其 Lie 空间不能落在对 $\log_p u_d,\log_p v_d$ 至少一个有
非零系数的该超平面中。矛盾，证明(AA4)。

因(W4)的 $B_1,B_2$ 是真实非零代数数，(AA4)给
$G_p^{\mathrm{wt}}\notin\mathscr P_{S,p}$。结合(W5)，得到
$$
 \sum_{i=0}^2\mathcal I_i'(0)\in\mathscr P_{S,p}
 \quad\Longrightarrow\quad J_p'(0)\ne0
 \quad\Longrightarrow\quad
     \Sha(E_{17}/\mathbf Q)[p^\infty]\ \text{有限} .             \tag{AA5}
$$
这是对每个充分大惰性好素数成立的充分判据。若固定 $S$ 的前提能
在无穷多个 $p$ 对**完整**目标余项获得，便可用 R303 完成主目标。
(Y4)的有限特征值本身含两个局部对数之比，(Y5)还读取任意深度；
两步都没有把完整三导数和自动置入这里的有限线性对数空间。

## 60. 一般交换代数群的有限对数，以及完整三目标余项的一条原超收敛积分

沿用(AA1)–(AA5)，固定有限有理素数集 $S$，并在选择的
$\overline{\mathbf Q}\hookrightarrow\mathbf C_p$ 下取对数。
对交换连通代数群 $G/\overline{\mathbf Q}$ 和一个代数点 $P$，
允许先取任何共同定义域。要求对每一 $v\nmid S\cup\{p\}$，
$\langle P\rangle$ 在 $G(L_v)$ 中相对紧；这条件不随定义域
的有限扩张改变。在所选 $p$ 位则要求 $P$ 属于群对数的定义域
$G(\mathbf C_p)_f$。令 $\mathscr L_{S,p}$ 为所有这类对数在代数
Lie 基中坐标的有限 $\overline{\mathbf Q}$-张成空间，并加入 $1$。
原(AA4)扩大为
$$
 \log_p(c_1/c_0),\quad\log_p(c_2/c_0)
 \ \text{在 }\mathbf C_p/\mathscr L_{S,p}
       \text{ 中仍在 }\overline{\mathbf Q}\text{ 上线性独立}.       \tag{AB1}
$$
特别允许非分裂的半阿贝尔簇、向量扩张及任意模数的广义 Jacobian；
群的维数、数域、所用点均可随 $p$，但每次的线性和有限。
原 $S\cup\{p\}$-unit 对数在固定支 $\log_p(p)=0$ 下，可乘
$p$ 的有理次幂使所选位为单位。阿贝尔簇由 proper 性在其它位
自动满足相对紧条件。

证明。将一条所称关系的所有群取乘积 $G$，连常数也用
$(\mathbf G_a,1)$ 实现。记 $u=c_1/c_0,v=c_2/c_0$，取
$(u,v,P)$ 的循环群在 $\mathbf G_m^2\times G$ 的 Zariski 闭包。
取统一整数倍到连通分支，记该分支为 $D$，$G$ 侧投影为 $D_0$。
由(AA1)，$D$ 满投射到 $\mathbf G_m^2$。若
$D\cap(\mathbf G_m^2\times1)$ 不含整个环面，则 quotient
$T=\mathbf G_m^2/(D\cap\mathbf G_m^2)$ 是正维环面。对应的
$D_0\to T$ 是代数同态，因为 $D/(D\cap\mathbf G_m^2)=D_0$；
两投影在 $D$ 上相等至这一商。取 $T$ 的非平凡字符，从而某个
$(u^av^b)^N$ 等于 $D_0$ 的代数字符在 $[N]P$ 的值，
其中 $(a,b)\ne(0,0)$。每个指定的 $v$ 上，$[N]P$ 的幂所生成的
紧闭包落在 $D_0$，其字符像又相对紧。因此该值在 $S,p$ 外均为
单位；$u,v$ 在全部 $p$ 位也是单位。这同(AA1)矛盾。于是闭包
含整个外部环面。若(AB1)有非平凡代数系数关系，Fuchs–Pham
Th. 1.1 所得代数子群包含原点的某个统一正整数倍，Lie 代数却落
在对这两个环面坐标至少一个系数非零的超平面，与上述闭包矛盾。
此处“原点”指所代入的代数点 $(u,v,P)$。

在固定代数曲线、固定模数及支撑不碰模数的固定代数次数零除子
的情形，所得广义 Jacobian 的代数点在某个固定有限集外有整
光滑群模型上的整截面，故上述紧性条件成立。一重 Coleman 积分
若由此点的群对数与一条代数不变微分配对给出，则该值已在
$\mathscr L_{S,p}$ 中；可选所需模数包住所给极。这里允许第二类
与第三类微分所给的向量及乘法扩张。因而
$$
 \sum_i\mathcal I_i'(0)\in\mathscr L_{S,p}
   \ \Longrightarrow\ J_p'(0)\ne0
   \ \Longrightarrow\ \Sha(E_{17}/\mathbf Q)[p^\infty]\text{有限}.\tag{AB2}
$$

有一个同一原三目标、端点固定的完整 **解析** 一重积分可供比较。
令 $d=p+1$，$C_i=2c_i$，并用(U1)含物理二次指数的 $H_i$。
对非负整数 $k$ 置
$$
 m_k=\sum_{i=0}^2 k!C_i^{-k}[z^{dk}]H_i(z),\qquad
 M(X)=\sum_{k\ge0}m_kX^k,\qquad
 D(W)=\sum_{h\ge0}\Delta^h m_0\,W^h,                         \tag{AB3}
$$
其中 $\Delta m_k=m_{k+1}-m_k$。完整的(U4)给
$m_k=\sum_i\mathcal I_i(k)$；其质量 $m_0=\sum B_i=0$。
Newton 系数 $\Delta^hm_0=h!\sum_i
 C_i^{-h}[z^{dh}](H_i e^{-C_i z^d})$。逐项等式由有限二项式
反演成立；(U4)或 R301 的同一圆盘界付出正的线性赋值增长，
故 $D$ 在半径严格大于一的盘解析。也可只用
$\sum_i\mathcal I_i\in\mathcal O\langle u\rangle$：各单项式
$\Delta^h u^k|_0=h!\,{k\brace h}$ 给 $\Delta^h m_0\in h!\mathcal O$，
已经足够超收敛。一般形式生成函数恒等式及完整积分为
$$
 D(W)={1\over1+W}M\!\left({W\over1+W}\right),\qquad
 \boxed{\displaystyle
 \sum_i\mathcal I_i'(0)
 =-\int_0^1 D(-t){dt\over t}
 =-\int_0^\infty M(X){dX\over X}.}                            \tag{AB4}
$$
第一式展开 $\Delta^hm_0$ 的二项式即可。第二式的第一积分沿
$t$ 闭单位盘的解析原函数定义，积分项为
$(-1)^{h-1}\Delta^hm_0/h$，准确等于 Newton 基
$\binom uh$ 在零的导数贡献。末一积分沿同盘的坐标
$X=-t/(1-t)$，不另选空间延拓的分支。确实
$D(-t)=(1-X)M(X)$ 与 $dt/t=dX/[X(1-X)]$；$M(0)=0$，且
$M(X)=D(X/(1-X))/(1-X)$ 在所取 $p$ 进无穷盘正则且为零。
因此被积微分在两个代数端点都正则。本式未将原超收敛被积
微分假定为代数微分。

从二阶 sigma 加法式还可在每个真实目标上选择代数点
$P_i$ 使 $x_i(P_i)=-A_i/B_i$，从而
$$
 {H_i(z)\over B_i}
 =-{e^{-s_i z^2}\sigma_i(z+P_i)\sigma_i(z-P_i)\over\sigma_i(P_i)^2}.
                                                                  \tag{AB5}
$$
这里 $P_i$ 在复正规化中取任一 lift；等式的右边由加法式独立
于这一选择。Bannai–Furusho–Kobayashi, Nagoya Math. J.
**219** (2015), Th. 1.2 在好超奇异处也给位置变量的
$E^{\rm col}_{1,1}$ 与 Coleman reduced-theta **对数**的等式；
其 Prop. 1.3 所用 $p$ 进权极限则假设好普通约化。该文原模型
还取最大 CM 序。公式(AB3)读取的是(AB5)整个截面的系数、所有
$k!$ 和三个各自的 $C_i$，其端点值还未由该文的固定位置
对数给出。[一手原刊](https://www.math.nagoya-u.ac.jp/~furusho/paper/BFK.pdf)（DOI 10.1215/00277630-2891995）

## 61. 完整三目标积分在复无穷处的精确阶与 $p$ 进正规端点

取(AB3)的物理复嵌入、$6\mid d=p+1$，且 $p$ 充分大。
精确的整函数增长阶为
$$
            \rho_{\mathbf C}(M)=\frac2{d-2}=\frac2{p-1}.        \tag{AC1}
$$
因此(AB4)在 $p$ 进无穷端点正则的同一个代数系数函数，在复
无穷端点有本性奇点。尤其 $M(X)dX/X$ 不能经有限代数覆盖
成为代数亚纯微分；这不排除积分端点差另有不同的 period 表示。

证明。给 $C_i^{-1}$ 任取第 $d$ 次根 $r_i$，记 $Z_i$ 为(S5)
物理 $\mu_3$ 投影；$H_i$ 偶，$Z_i(0)=B_i\ne0$。令
$$
 F(z)=\sum_{i=0}^2 {6\over d}
       \sum_{\rho\in\mu_d/\mu_6} Z_i(\rho r_i z)
     =\sum_{k\ge0}A_k z^{dk},\qquad  k!A_k=m_k .                \tag{AC2}
$$
这就是在每个原 $H_i(r_i z)$ 上作整个 $\mu_d$ 平均，故不依赖
所选根或代表。写 $\Lambda=\varpi\mathcal O_K$、
$a=\pi/\operatorname{area}(\mathbf C/\Lambda)>0$。
由 $\sigma(\omega z)=\omega\sigma(z)$ 及 Legendre 关系，
其 quasi-period $\eta_\ell=a\bar\ell$。具体说准周期映射的
实线性延拓为 $Az+B\bar z$，三次旋转迫 $A=0$，定向周期基
的 Legendre 关系给 $B=a$。原 degree $34$ 的
$Z_i=\sigma^{34}$ 乘一个椭圆函数；故对于
$f(z)=Z_i(\rho r_i z)$，$L=(\rho r_i)^{-1}\Lambda$，
$b=17a|r_i|^2$，有
$$
 f(z+\ell)=e^{2b\bar\ell z+b|\ell|^2}f(z),\quad \ell\in L.
                                                                  \tag{AC3}
$$
$|f(z)|e^{-b|z|^2}$ 有界，平方是 $L$ 周期的非负连续函数且
在一个基本平行四边形上积分严格正。因此其归一圆盘均值有
严格正极限。

(AC2)不同标记的格不能通约。对此型格，两格若有非零共同
向量，其伸缩比就在 $K^\times$，遂通约。对相同 $i$，
$K\cap\mu_d=\mu_6$ 已被除去。对不同 $i,j$，两格通约会给
$(\rho r_i/\rho'r_j)^d=c_j/c_i\in K$。固定 $K$ 并轮换三目标的
十三处三循环遂迫三个连续比相等且为三次单位根。这同(AA2)
的 $|c_1/c_0|\to0$ 矛盾。

令 $b$ 为(AC2)中出现的最大曲率，取归一圆盘均值内积
$$
 \langle f,g\rangle_R={1\over\pi R^2}
  \int_{|z|\le R} f(z)\overline{g(z)}\,e^{-2b|z|^2} dA(z).
$$
较小曲率项的对角均值趋于零，混合项亦因 Cauchy–Schwarz
趋于零。对同最大曲率而格 $L_1,L_2$ 不同的 $f,g$，定义
$T_hg(z)=e^{-2b\bar h z-b|h|^2}g(z+h)$。在这一归一内积下
同时平移两项所造成的误差趋零，因为只改了半径 $R$ 圆盘
边界处面积 $O_h(R)$ 的部分，两个除 Gaussian 后的函数有界。
平移交换子的相位为 $\exp(\pm4ib\operatorname{Im}(h\bar k))$。
有 $h\in L_1,k\in L_2$ 使
$4b\operatorname{Im}(h\bar k)/(2\pi)$ 无理：否则两组基的
这四个配对均有理。$L_2$ 自己的此配对交错矩阵非退化且整
（其有向面积给 $4b\operatorname{area}(L_2)/(2\pi)=34$），
解线性方程即 $L_1\subset L_2\otimes\mathbf Q$，违反不可通约。

于是 $T_h^ng$ 对 $T_k$ 有两两不同的单位特征值。由同时平移
的边界误差，它们在上述圆盘均值中两两内积趋零；所有对角
均值有同一严格正极限 $q_g$。而 $T_hf=f$，对于每个固定 $n$，
$\langle f,T_h^ng\rangle_R-\langle f,g\rangle_R\to0$。把
$n=0,\ldots,N-1$ 平均再用 Cauchy–Schwarz，得到
$$
 \limsup_{R\to\infty}|\langle f,g\rangle_R|
     \le (q_fq_g/N)^{1/2}.
$$
令 $N\to\infty$ 即为零。这证明实际圆盘的全均值存在，
无需预设非周期交叉项有均值。所有最大曲率的非零对角项
都保留，故 $|F|^2e^{-2b|z|^2}$ 的圆盘均值有严格正极限。
另一方面 $|F|\ll e^{b|z|^2}$。若 $F$ 的阶小于二，或二阶
但型严格小于 $b$，该均值都会趋零。因此 $F$ 恰二阶、型 $b$。

故 $\sum A_kX^k$ 恰为 $2/d$ 阶。由整函数 Taylor 系数阶公式
$1/\rho=\liminf\log(1/|a_k|)/(k\log k)$（零项取 $+\infty$），
用 $\log k!=k\log k+O(k)$ 便从(AC2)得到(AC1)。其正有限阶且
为整函数，故为非多项式整函数。无穷处的本性奇点不能由
有限代数分歧去除。这作用在(AB3)的整个三目标系数和上，
并未给(AB4)的 $p$ 进端点差赋予非零或超越性。

## 62. 分裂子列的完整双 Jacobi 迹与原物理纯调和轴的全形式盘整性

令 $K'=\mathbf Q(\xi)$，$\xi^2=-17$、$\xi=i\sqrt{17}$ 取原
复嵌入。可在§50的射线再取无穷多个 $p$，使得
$$
 p=\pi\bar\pi,\qquad \pi=a+b\xi,\qquad
 \pi,\bar\pi\equiv1\pmod {68\mathcal O_{K'}},\qquad
 p\equiv2\pmod3.                                                \tag{AD1}
$$
事实上 $\mathcal O_{K'}=\mathbf Z[\xi]$。取其模 $68$ 射线类域
的正规闭包并合入 $\mathbf Q(\zeta_{68})$。该扩张只在 $2,17$
分歧，与在 $3$ 分歧的 $K=\mathbf Q(\sqrt{-3})$ 交为 $\mathbf Q$。
在其与 $K$ 的合成中指定前者 Frobenius 为恒等、后者为共轭，
用 Chebotarev。射线平凡给(AD1)，且 $p\equiv137\bmod204$。

采用(RC4)的全部 $68$ 个标记、$\alpha=x+y\xi$、
$Q=N\alpha/68$，令
$$
 \Psi(\tau;Z,W)=\sum_{a_0,b_0}\gamma_{a_0}\delta_{b_0}
   \sum_{x\equiv a_0\ (34),\ y\equiv b_0\ (2)}
       q^{Q}e^{Z\alpha+W\bar\alpha}.
$$
对两个变量准确有
$$
 {1\over p}\sum_{j\bmod p}\Psi((\tau+68j)/p;Z,W)
    +\Psi(p\tau;pZ,pW)
 =\Psi(\tau;\pi Z,\bar\pi W)+\Psi(\tau;\bar\pi Z,\pi W).
                                                                  \tag{AD2}
$$
有限 Fourier 和选 $p\mid N\alpha$。这正是
$\alpha\in\pi\mathcal O_{K'}\cup\bar\pi\mathcal O_{K'}$，
交集为 $p\mathcal O_{K'}$。除以相应因子后原全部标记不变，
因为这些因子模 $68$ 都是一。零与非 primitive 项均按包含排除
计入。取 $Z^jW^k$ 的同权比较给原完整混合系数的显式乘子
$\pi^j\bar\pi^k+\bar\pi^j\pi^k$，在任一 $p$ 位其赋值准确为
$\min(j,k)$；当 $j=k$ 时剩余因子是 $2$。特别各纯调和
$\mathcal H_{2n}$ 的此 Hecke 特征为 $\pi^{2n}+\bar\pi^{2n}$。

把两原 Jacobi 椭圆变量（同一周期单位）记作 $u,v$，即
$u$ 正比于 $Z+W$、$v$ 以同一因子正比于 $\xi(Z-W)$。
(AD2)右侧变换为
$$
 R_\pm(u,v)=(au\pm bv,\,\mp17bu+av),\qquad
 17R_{\pm,1}^2+R_{\pm,2}^2=p(17u^2+v^2).                      \tag{AD3}
$$
在源取真正原 $P$、$q_s=\eta_\Omega/\Omega$。用§52的实际原
固定常数将两 Jacobi 质量归一为 $S_1(u),G(v)$，其中
$G=x\sigma^2$。对(AD2)乘共同的
$e^{pq_s(17u^2+v^2)}$ 及同一对常数，右侧即
$\sum_\pm S_1(R_{\pm,1})G(R_{\pm,2})$。在每个商格
$\Lambda_H=\Lambda+H$ 用同一 $dz$，实际 $q_H=pq_s+s_H$，
$s_H=\sum_{T\in H-0}x(T)$；证明同(U1)，将 $17$ 换作 $p$。
比较时有限支的实周期为 $\Omega$、无限支为 $\Omega/p$，
所以两半权乘积的周期归一因子在无限支额外乘 $p$，正合
(AD2)的权一迹。凡采用目标自身 $q_H$ 的 theta，须同时乘
$e^{-s_H(17u^2+v^2)}$ 才得上述共同框架。源的 $v=0$ 上
右侧准确等于 $2S_1(au)G(17bu)$。在任一纯 $Z$ 或纯 $W$ 轴上，
$17u^2+v^2=0$；对于源和每个目标，这一物理 Gaussian 均准确消去。

现在只须 $p>211$、$p$ 在 $K$ 惰性而在 $K'$ 分裂，
无需(AD1)的主理想条件。选 $\xi\in\mathbf Z_p^\times$。
完整物理纯轴截面
$$
 K(z)=S_1(z)G(\xi z),\qquad
 K(z(t))\in t^6\big(1+t\mathbf Z_p[[t]]\big),\qquad
 t=x^{-1/2},\quad t=z+\cdots .                                   \tag{AD4}
$$
$K$ 是同一份 $\mathbf Q$ 系数固定级数，因为 $G$ 偶、
$\xi^2=-17$。这里整性在整个原形式群 $|t|_p<1$ 上；
它使用物理 $z(t)$ 而非将 $z$ 充作全形式盘整参数。

证明。写 $S_1=\sigma^{34}P(x)$，其中 $P$ 是 R303(2)
的首一十四次多项式。设 $h=\sigma(z(t))/t$，则
$h\in1+t\mathbf Q_p[[t]]$，$G(z(t))=h^2$。取正整数
$n$，$p\nmid n$，并令 $\psi_n=\sigma(nz)/\sigma(z)^{n^2}$，
采用其原领先项 $n z^{1-n^2}$。这是通常的整除法多项式
至统一计号；其平方无计号歧义。由整 Weierstrass 除法递推，
$D_n=t^{n^2-1}\psi_n\in\mathbf Z_p[[t]]$，常数 $n$：
奇数 $n$ 用 $x,y$ 权次数至多 $n^2-1$ 的多项式，
偶数的 $2y$ 因子亦同；$x=t^{-2},\ y=-t^{-3}\sqrt{1+t^6}$。
$[n]t/t$ 是整形式单位。因此
$$
 R_n(z)={S_1(z)G(nz)\over G(z)^{17+n^2}}
       =t^{34}P(x)\,D_n^2\,{t^2\over([n]t)^2}
       =t^{34+2n^2}P(x)\psi_n^2x([n]z)
       \in t^6(1+t\mathbf Z_p[[t]]).                            \tag{AD5}
$$
末式还是全局有理函数，因为 $t^2=1/x$。
取正整数 $n\to\xi$，可在预定的与 $p$ 互素模数剩余类中取。
形式域 $\mathbf Q_p[[t]]$ 中 $G(nz(t))\to G(\xi z(t))$
逐系数成立，因为各所读有限系数是 $n$ 的多项式。
同时 $17+n^2\to0$，所以常数一形式级数
$G(z(t))^{17+n^2}\to1$；每一截断只需有限个连续的二项式。
由此 $R_n\to K$ 逐系数；(AD5)使每个系数都留在
$\mathbf Z_p$。给定任意 $r<1$，全系数的一致整界将单位
闭盘 $|t|\le r$ 上从 $t^j$ 起的尾统一界于 $r^j$，故该
收敛也在每个严格内闭盘上一致。这证明(AD4)与后续代入
任意有限层形式挠点所需的极限。

在(AB4)的比较之外，这还给实际(RC5)全部整数阶在原超奇异
CM 点的一条强化。对 $m\ge6$，R301 的 $t(z)/z$ 直到
$r<p^{-1/(p^2-1)}$ 是范数一的单位，故
$$
 v_p\big([z^m]K\big)\ \ge\
       \left\lceil{6-m\over p^2-1}\right\rceil .               \tag{AD6}
$$
完整的原导数仍需原参考的倒数。具体在 R303 的物理
$c=[z^{p+1}]\log(\sigma/z)$、$d=p+1$、$C=34c$ 下，准确有
$$
 J_p'(0)=\sum_{h\ge1}(-1)^{h-1}(h-1)!C^{-h}
           [z^{dh}]\left(e^{-Cz^d}{K(z)\over G(\xi z)}\right).\tag{AD7}
$$
其收敛与截尾精度由 R301(26)原样给出。此处不删除
$G(\xi z)^{-1}$，也未以(AD6)对正曲率原 $S_1$ 作错误外推。

## 63. 原纯轴在每个非零 $p$ 幂挠点的全局单位值与准确 Coleman 范数

沿用(AD4)–(AD7)。取 $S=\{2,3,7,17\}$（扩充固定有限坏集也可），
$p>211$ 在 $K$ 惰性、在 $K'$ 分裂。固定一次
$\overline{\mathbf Q}\hookrightarrow\mathbf C_p$，用它辨认
代数挠点和全超奇异形式盘中的挠点。对每个
$Q\in E_1[p^\infty]-\{O\}$，有
$$
                 K(t(Q))\ \in\overline{\mathbf Q}^{\times}
                   \text{ 且为 }S\cup\{p\}\text{-unit}.           \tag{AE1}
$$
此结论规定整个 $K=S_1\,G(\xi\,\cdot)$ 的值。其在所选
$p$ 位的赋值准确为 $6v_p(t(Q))$，不是该位的单位。

证明。令 $M=\operatorname{ord}(Q)=p^r$。在一个固定代数数域
内取所有当前有限层挠点的坐标。$t(Q)^2=1/x(Q)$，所需幂均偶。
任取正整数 $m\equiv\xi\bmod M$，可取 $m$ 为奇数。
令 $n\to\xi$ 且 $n\equiv m\pmod {2M}$，$n>0$ 均为整数；
由中国剩余定理可同时令 $n$ 逐次 $p$ 进逼近 $\xi$。
于是 $[n]Q=[m]Q\ne O$。给 $Q$ 取物理复格的 lift
$z_Q=\lambda/M$，$\lambda\in\Lambda$；$n=m+kM$ 给
$$
 {\psi_n(Q)^2\over\psi_m(Q)^2}
 =\left({e^{\eta_\lambda z_Q/M}\over\sigma(z_Q)^2}\right)^{n^2-m^2}.
                                                                  \tag{AE2}
$$
事实上 $\sigma(mz_Q+k\lambda)^2/\sigma(mz_Q)^2
=\exp(2k\eta_\lambda m z_Q+k^2\eta_\lambda\lambda)$，
而 $2km+k^2M=(n^2-m^2)/M$。平方消去符号；取模 $2M$
还固定了同一直线上的原准周期计号。

无需把指数底数的复周期直接送到 $p$ 进。置
$$
 n_*=m+2M,\quad d_* = n_*^2-m^2,\qquad
 A_Q=t(Q)^{2d_*}\,\psi_{n_*}(Q)^2/\psi_m(Q)^2.
$$
(AD5)和(AE2)给全局代数数之间的准确等式
$$
                    R_n(Q)^{d_*}=R_m(Q)^{d_*}\,A_Q^{n^2-m^2}.   \tag{AE3}
$$
在所选 $p$ 位，(AD5)说明 $t(Q)^{n^2-1}\psi_n(Q)$ 为单位：
它是常数 $n\in\mathbf Z_p^\times$ 的整幂级数在形式点取值。
所以 $A_Q$ 是该位单位。取含 $A_Q$ 的局部数域剩余域阶 $q$，
将(AE3)升到 $q-1$ 次方，底数 $A_Q^{q-1}$ 是主单位。
指数 $n^2-m^2\longrightarrow-17-m^2$ 恰是一个普通整数。
(AD4)证明的严格内闭盘一致收敛可以代入这个 $Q$；故
$$
 K(t(Q))^{d_*(q-1)}
   = R_m(Q)^{d_*(q-1)}(A_Q^{q-1})^{-17-m^2}.                    \tag{AE4}
$$
这直接给代数性，无须先指定未确定的 $p$ 进代数根；
(AD4)给所需的根及所报准确赋值。

在任意 $v\nmid S,p$，$E_1$ 有好约化，非零 $p$ 幂挠点约化
保阶。它同 $O$、非零二/三挠点及七挠核不碰。因此 $x(Q)$、
$x([m]Q)$ 都是单位，并且 R297 §6 的完整零除子保证
$P(x(Q))$ 是单位；整方程与首系数只在固定坏集允许分母。
对于 $n=m,n_*$，$p\nmid n$，所以 $[n]Q$ 的约化仍非零。
整除法多项式 $\psi_n(Q)$ 亦为单位，即使 $v\mid n$：
在整光滑 Weierstrass 模型上，乘法映射的除法截面拉回 $O$
的除子；在此仿射点上其零恰为 $[n]Q=O$。等价地可用整
无公共基点的射影乘法公式。也可避免 $v\mid m n_*$ 问题：
对所验任一 $v$，在同样模 $2M$ 的剩余类另取
$m\equiv\xi\bmod M$ 和 $n_*=m+2kM$ 两者均与该剩余特征互素，
重复(AE2)–(AE4)；$v$ 的剩余特征大于三且不整除 $2M$，
故可如此选择，所得左边是同一解析 $K(t(Q))$。
于是(AE4)的右侧为 $v$ 单位，证明(AE1)。

还有原整个级数的准确乘法范数等式。在形式群记号中有
$$
 \prod_{T\in E_1[p]}K(t\oplus T)
    =c_p K([p]t),\qquad
 c_p=p^{-6}\prod_{T\in E_1[p]-0}K(t(T)).
                                                                  \tag{AE5}
$$
右侧常数是代数 $S\cup\{p\}$-unit，且在当前 $p$ 位为单位。
取代数 $\lambda_p^{p^2-1}=c_p^{-1}$ 后，$\lambda_pK$ 满足
常数一的 Coleman 范数关系；特别一整套实际层值是范数相容的。
对局部 Lubin--Tate 原始塔，从 $p^{r+1}$ 到 $p^r$ 的所有
$p^2$ 个原像（$r\ge1$）即给所取那一步的完整局部 Galois 范数，
在需要时先对常数作标量扩张或只使用逐纤维乘积(AE5)；
不以不相容的标量扩域强行维持原 Galois 群。

证明(AE5)。$D_S,D_G$ 分别为原两正次数截面的零除子。
$D_G=(T_3)+(-T_3)$，$T_3=(0,1)$。按 R297 §6，
$D_S$ 逐组为 $6(O)$、每点重二的 $\pm T_3$ 和三个非零二挠，
每点重一的 $[2]^{-1}\{\pm T_3\}\setminus\{\pm T_3\}$，
以及两个共轭七挠核各自去原点的六点。故 **每个** $p>211$
上的乘 $p$ 在每一组内置换，无须在七处另加同余。
又因 $p\nmid n$，$[n]^{-1}\{\pm T_3\}$ 是阶整除 $3n$ 的
挠点集合，$[p]$ 亦将这整个集合置换。由(AD5)，
$$
 \operatorname{div}(R_n)=D_S+[n]^*D_G-(17+n^2)D_G ,
 \qquad [p]_*\operatorname{div}(R_n)=\operatorname{div}(R_n).
$$
故 $\prod_{T\in E[p]}R_n(z+T)/R_n(pz)$ 的全局因子为零，
在光滑 proper 椭圆曲线上为常数。$R_n(z)=z^6+\cdots$，
$R_n(T)$ 对 $T\ne0$ 有限非零，所以该常数是
$p^{-6}\prod_{T\ne0}R_n(T)$。对任何固定形式点 $t$，
$t\oplus T,[p]t$ 及所有所用挠点都在某个严格内闭盘；
(AD5)的一致收敛及有限乘积令 $n\to\xi$，给出(AE5)。
此处无两个无界层级的换序。每个非零 $p$ 挠点的
$v_p(t(T))=1/(p^2-1)$，由(AE1)的准确估值，
$v_p(c_p)=-6+(p^2-1)6/(p^2-1)=0$。

(AE5)与(AE1)付的是同一个原纯调和乘积的真实全局单位及范数。
回到通常 Sha 的原输入仍是(AD7)的完整系数或 R303 的原标准
Rubin 类；尚需证明该读者的跨素数非零，不能把任一有限层单位
的非零或 Coleman 范数相容性直接代入 R303(8)。
