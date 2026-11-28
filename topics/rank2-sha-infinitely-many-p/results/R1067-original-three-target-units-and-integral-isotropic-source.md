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

## 64. 原范数相容级数的固定全局有理标量 $3024$

(AE5)的标量在每个(AD4)素数上准确等于
$$
 c_p=3024^{1-p^2},\qquad
 \prod_{T\in E_1[p]}3024K(t\oplus T)=3024K([p]t).              \tag{AF1}
$$
因此使用同一个固定有理级数及原本的完整 Lubin--Tate 塔；
每一步的点值都在该层局部域，因为 $K\in\mathbf Z_p[[t]]$
且 $t(Q)$ 是该点的整形式参数。此处 $t=x^{-1/2}$ 的原形式
支可从 $-x/y$ 以常数一的平方根整恢复。其代数性及全局
$S\cup\{p\}$-unit 性另由(AE1)保证。

证明。令 $a=\pi/\operatorname{area}(\mathbf C/\Lambda)$，
对 $E_1$ 的物理 degree $e$ 截面 $V$ 记
$\|V(z)\|=|V(z)|e^{-ea|z|^2/2}$，
$M_V=\exp\int_{E_1(\mathbf C)}\log\|V\|\,d\mu$；
$d\mu$ 为概率 Haar 测度。对数零极局部可积，乘法自同源
均保此测度。$M_\sigma=432^{-1/12}$ 可在同一格内直接求得。
事实上 $\|\sigma(z)\|$ 在环面上周期。二倍除子的相等及
Curvature 相消使
$\prod_{U\in E[2]}\|\sigma(z+U)\|/\|\sigma(2z)\|$ 为常数：
其对数在环面光滑且调和。令 $z\to0$ 再积分，给
$M_\sigma^3=\frac12\prod_{U\in E[2]-0}\|\sigma(U)\|$。
三个非零二挠点 $U_i$ 的 $e_i=x(U_i)$ 是 $X^3+1$ 的根，
对 $i,j,k$ 互异，sigma 加法式给
$$
 |e_i-e_j|={\|\sigma(U_k)\|^2\over
                 \|\sigma(U_i)\|^2\|\sigma(U_j)\|^2}.
$$
乘三式及 $|\prod_{i<j}(e_i-e_j)^2|=27$ 得
$\prod_i\|\sigma(U_i)\|=27^{-1/4}$，从而
$M_\sigma^3=432^{-1/4}$。此归一也与
Bannai–Furusho–Kobayashi 复 Th. 1.1(ii)、Prop. 2.8 的
$\Delta=2^4\operatorname{disc}(X^3+1)$ 相符。

令 $T_3=(0,1)$。由 $2T_3=-T_3$ 和
$\sigma(2z)/\sigma(z)^4=-2y$ 在 $T_3$ 的绝对值为二，
得到 $\|\sigma(T_3)\|=2^{-1/3}$。sigma 加法式在
$x(T_3)=0$ 又给
$\|G(z)\|=\|\sigma(z+T_3)\|\|\sigma(z-T_3)\|/\|\sigma(T_3)\|^2$。
所以
$$
 M_G=2^{2/3}M_\sigma^2=3^{-1/2}.
$$
R297(19)在物理 $E_1$ 上的整条原因子式为
$$
 S_1(z)=\frac1{28}\sigma(z)^2\sigma(2z)^2 G(z)G(2z)
                     \sigma(\gamma_7z)\sigma(\bar\gamma_7z).
$$
两边的 Gaussian 也按 $2+8+2+8+7+7=34$ 准确相等。
由 Haar 不变性，
$$
 M_S=\tfrac1{28}M_\sigma^6 M_G^2,\qquad
 M_SM_G=1/3024.                                                  \tag{AF2}
$$

(AE5)证明中每个
$c_{p,n}=p^{-6}\prod_{U\in E[p]-0}R_n(U)$ 是正有理数：
原 $R_n$ 为有理偶函数；$\prod_{U/\pm}R_n(U)$ 是非零有理数，
完整乘积为它的平方。对其全局范数等式取复绝对值并在环面
积分；有理函数 $R_n=S_1G(nz)/G^{17+n^2}$ 的全部 Gaussian
准确消去。于是
$$
 c_{p,n}=(M_SM_G^{-16-n^2})^{p^2-1}
  =3024^{1-p^2}\left(3^{(p^2-1)/2}\right)^{17+n^2}.             \tag{AF3}
$$
因 $(p^2-1)/2$ 是 $p-1$ 的倍数，括号内在 $1+p\mathbf Z_p$，
且 $17+n^2\to0$。直接取(AE5)已经支付的系数极限即得(AF1)，
没有剩下任何依赖 $p$ 的根选择。范数相容的是原纯调和截面，
原秩二 Euler 读者仍保(AD7)的参考逆因子。

## 65. 十七挠平移的范数相容全局单位和三个原目标的有限 Heisenberg 展开

在(AD1)的射线给每个 $T\in E_1[17]$ 取物理复格的 lift
$z_T$；置 $\eta_T=\eta_{17z_T}/17$，$\eta_0=z_0=0$。
对 degree $e$ 的物理截面 $V$ 记
$$
 V_T(z)=e^{-e\eta_T(z+z_T/2)}V(z+z_T),\qquad v_T=V_T(0).
                                                                  \tag{AG1}
$$
记 $S=S_1$。对 $T\ne0$ 写 $s_T=S_T(0)$、$g_T=G_T(0)$，
均为非零代数数，在 $\{2,3,7,17\}$ 外为单位。
事实上把(AE2)用于 $U=T$、$n\equiv1\bmod34$，得到
$\widehat\sigma(T)^2=e^{-\eta_Tz_T}\sigma(z_T)^2$ 的正整数幂
是除法值的比；对每个所验剩余特征可取相应整数均与之互素。
现在 $s_T=\widehat\sigma(T)^{34}P(x(T))$，
$g_T=\widehat\sigma(T)^2x(T)$；R297 §6 的全零除子与非零
十七挠点在各好纤维不相遇。$G_T/G$ 的十七次幂是椭圆函数，
因其周期相位是十七次单位根，其代数除子及原点代数首项给
代数性。$S_T/S$ 本身为椭圆函数，同理得代数。于是两个局部
截面的正规 Taylor 系数都在固定数域内；改变 lift 只改有限相位。

在所选 $p$ 位记 Teichmüller 部分为 $\omega_p$，置
$$
 \epsilon_{T,p}=\omega_p(g_T)^{-17}\ (T\ne0),\quad
 \epsilon_{0,p}=1,\qquad U_{T,p}(z)=3024\epsilon_{T,p} S_T(z)G(\xi z).
                                                                  \tag{AG2}
$$
$T\ne0$ 的分量在整个原形式盘为整单位，$U_{0,p}=3024K$。
全部满足
$$
 \prod_{V\in E_1[p]}U_{T,p}(t\oplus V)=U_{T,p}([p]t).           \tag{AG3}
$$
对任意 $p$ 幂阶形式点 $Q$，$U_{T,p}(Q)$ 是代数
$\{2,3,7,17,p\}$-unit，唯一例外为 $(T,Q)=(0,0)$ 的真实零。

证明。在(AD5)取 $n\to\xi$，始终令 $n$ 为 $17$ 及所有
$\omega_p(g_T)$ 的阶的公倍数。这些整数均与 $p$ 互素。于是
$nT=0$，准周期公式按全部指数给
$$
 R_n(T+z)=\frac{S_T(z)G(nz)}{G_T(z)^{17+n^2}},\qquad
 R_n(T)=s_Tg_T^{-17-n^2}.                                       \tag{AG4}
$$
分子线性项为 $34\eta_Tz+2n^2\eta_Tz$，与分母的
$2(17+n^2)\eta_Tz$ 相消，半常数项也同消。
$G_T/g_T$ 常数一，其 $17+n^2$ 次幂逐系数趋一；
$g_T^{-17-n^2}$ 则趋 $\epsilon_{T,p}$。
每个 $R_n(T+z(t))$ 在此形式盘都是整单位。具体用(AD5)的
整射影乘法横坐标分子 $\phi_n=\psi_n^2 x([n]\cdot)$，
$[n]T=O$ 故该分子在 $T$ 的特殊纤维为单位，因为
$p\nmid n$ 且在非零 $n$ 挠点 $\psi_n$ 简单消失、
$x([n]\cdot)$ 有准确二阶极。$x(T),P(x(T))$ 同样是单位。
因此逐系数收敛在每个严格内闭盘上一致。由(AF3)，
$c_{p,n}\to3024^{1-p^2}$；又 $pT=T$，取相同有限纤维
乘积的极限即得(AG3)。

当 $Q,T$ 均非零，$T+Q$ 的阶为 $M=17\operatorname{ord}(Q)$。
沿子序列固定 $n\equiv m\bmod{2M}$，并保持上面的 Teich 阶
条件；$[m](T+Q)=[m]Q\ne0$。(AE2)–(AE4)适用于 $T+Q$：
$t(T+Q)^2=1/x(T+Q)$ 为代数数。在所选 $p$ 位，$R_m(T+Q)$、
$R_{m+2M}(T+Q)$ 均为单位，此处二者在(AG4)的整性只需
$17\mid m$、$p\nmid m$，不需 Teich 阶条件。因此(AE3)所用
幂底数也是单位。$S,p$ 外 $T+Q,[m]Q$ 的约化阶分别为
$M,\operatorname{ord}(Q)$，与 R297 的原零极不相交。所需
全局根代数性与单位性由相同正整数次幂等式得出。$Q=0,T\ne0$
则直接用 $3024\epsilon_{T,p}s_T$，$T=0$ 已由(AE1)覆盖。

沿用§52真实 $V_2\otimes V_{17}$ 标记，写
$S=b\otimes v$，$H_i=b\otimes v_i$；共同整体物理常数在
两者同样纳入 $v,v_i$。具体在 $n\bmod34\leftrightarrow
(n\bmod2,n\bmod17)$ 的原 CRT 基中，三类物理系数逐项为
$$
 \begin{array}{ll}
 S: & CD\,b_{n\bmod2}\,e_{17}^{2n^2} f_{17}(3n),\\
 H_j\ (j\ne\infty): &-CD\, e'_j b_{n\bmod2}\,e_{17}^{j n^2},\\
 H_\infty: &CD\sqrt{17}\,b_{n\bmod2}\,\mathbf1_{17\mid n}.
 \end{array}
$$
最后一式用 $17\mid n$ 时 $n/17$ 与 $n$ 同奇偶。
这里 $b=(1,t_2e_8^{-1}),C,D,I,e'_j$ 均为(S1),(S2)的原常数。
所以这些向量在同一个 $b\otimes\mathbf C^{17}$ 中。
十七挠点在二次有限 Heisenberg 商上的像为零，实际位移保
$b$，其可能的共同标量计入 $D_T$。让 $D_T$ 为(AG1)的十七有限
Heisenberg 平移在 $V_{17}$ 上的酉矩阵，即实际 theta 标记
中的移位/相位矩阵。它们是代数的；改变 lift 的单位根随
$D_T,S_T$ 同时改变。固定代数系数及准确展开为
$$
 a_{i,T}=\frac{(D_Tv)^*v_i}{17v^*v},\quad
 H_i=\sum_{T\in E[17]}a_{i,T} S_T,\quad
 H_iG(\xi z)={1\over3024}\sum_Ta_{i,T}\epsilon_{T,p}^{-1}U_{T,p}.
                                                                  \tag{AG5}
$$
因为 $\sum_TD_Tvv^*D_T^*$ 与不可约的十七 Heisenberg 表示交换，
取迹知它是 $17v^*v$ 倍恒等。全部 $17^2$ 项均保留；在零点
准确复得 $3024B_i=\sum_Ta_{i,T}\epsilon_{T,p}^{-1}U_{T,p}(0)$。

在 $C_i=2c_i$ 的各自规范中，完整读数为
$$
 \sum_i\mathcal I_i'(0)
 ={1\over3024}\sum_{i,T}a_{i,T}\epsilon_{T,p}^{-1}
 \sum_{h\ge1}(-1)^{h-1}(h-1)!C_i^{-h}
   [z^{dh}]\frac{e^{-C_i z^d}U_{T,p}(z)}{G(\xi z)} .            \tag{AG6}
$$
固定 $S_T/\sigma^{34}$ 是至多 $34(O)$ 极的代数椭圆函数，
可在 $x,y$ 基中有限展开。除固定有限坏集后系数整；在
R301 的 $R=p^{-1/(2p)}$ 原盘，$t/z,z/t$ 范数一，
$e^{-34cz^d}S_T$ 由相同 sigma 余项界有界。又
$C_i-34c=2e_i\in\mathcal O$，更换 Gaussian 仍有界，故
$h$ 向有正线性赋值增长，允许有限求和通过完整导数读者。
输入现在是实际 $17p^r$ 层全局单位的有限组 Coleman 级数。
(AG6)取这些级数本身并乘原参考倒数，尚须将其权导连接至
有限代数对数或直接证明原完整中央的跨素数非零。

最后，取相容的 $z_{-T}=-z_T$，令 $\epsilon_{-T,p}=\epsilon_{T,p}$。
因 $S,G$ 偶，准确有 $U_{-T,p}(-z)=U_{T,p}(z)$。对于
$T\ne0$，形式对数各自在原点除以其非零常数项再取。若将
$T,-T$ 以相同系数相加后取这两份局部对数的和，则它是偶函数，
所有奇数 Coates--Wiles 矩都为零。原 R303 的 Hecke 幂
$2m+1$ 是奇数，这一朴素偶对数投影不能替代原标准 Rubin 类。
(AG5),(AG6)用的是带真实权的截面本身。

## 66. (G81)的所有 $p$ 幂层全局单位、固定范数标量与原 Rubin 权归一

取 R1062 §13 的 $(17/p)=1$ 特化，$p>211$ 在 $K$ 惰性，
$\beta=\sqrt{17}\in\mathbf Z_p^\times$，下列物理形式级数
与 $p$ 无关：
$$
 D(z)=S_1(z)/G(\beta z).
$$
R1062(G81)–(G85)已付它的全形式盘整性、实际首 wild 完整
translated Miller germs、原 $p^2$ 相位及所有权块的框架费用。
本节再定该同一实体的全局值与全部幂层范数：
$$
 \prod_{V\in E_1[p]}1008D(t\oplus V)=1008D([p]t),
 \qquad 1008D(Q)\text{ 是全局代数 }S\cup\{p\}\text{-unit}
 \quad(0\ne Q\in E_1[p^\infty]).                                \tag{AH1}
$$
这里 $S=\{2,3,7,17\}$，且 $D\in t^6(1+t\mathbf Z_p[[t]])$。
$S$ 后接下标才指原正次数截面。

证明。取正整数 $n\to\beta$、$p\nmid n$，用全局有理偶函数
$$
 R_n^-(z)=\frac{S_1(z)}{G(nz)G(z)^{17-n^2}}
         =\frac{S_1}{G^{17}}\left(\frac{G(nz)}{G^{n^2}}\right)^{-1}.
$$
后一括号是 $\phi_n/x^{n^2}$，在形式盘属于
$1+t\mathbf Z_p[[t]]$；即(AD5)中的整单位
$(t^{n^2-1}\psi_n)^2(t/[n]t)^2$。故 $R_n^-$ 及其
$t^{-6}$ 后的逆均有一致整界，并在每个严格内闭盘收敛到 $D$
及其相应逆。除子 $D_S-[n]^*D_G-(17-n^2)D_G$ 仍由 $[p]_*$ 固定。
其范数常数正有理，仍可按(AF3)取原 Haar 几何均值：
$$
 c^-_{p,n}=(M_SM_G^{-18+n^2})^{p^2-1}
   =1008^{1-p^2}\big(3^{-(p^2-1)/2}\big)^{n^2-17}.
$$
因为 $M_S/M_G=1/1008$，后面底数在 $1+p\mathbf Z_p$。
故极限为 $1008^{1-p^2}$，给(AH1)范数。该固定有理标量
没有随 $p$ 选择额外的比较单位。

对 $Q$ 阶 $M=p^r$，固定物理 lift $z_Q=\lambda/M$，
记真实 Klein 归一
$$
 \widehat S(Q)=e^{-17\eta_\lambda z_Q/M} S_1(z_Q),
 \qquad \widehat G(Q)=e^{-\eta_\lambda z_Q/M} G(z_Q).
$$
涉及 $mQ$ 时暂取同一直线上的 lift $m z_Q$。
(AE2)的除法比及 $x(Q),P(x(Q))$ 证明两值均为非零代数
$S\cup\{p\}$-unit；选定复 lift 的数本身由其已知正整数次幂
是代数数而代数，不必先给复周期作 $p$ 进评价。现在还准确有
$$
 \widehat G(Q)\in1+\mathfrak m_{\mathbf C_p},\qquad
 D(Q)=\widehat S(Q)/\widehat G(mQ),\quad m\equiv\beta\pmod M.   \tag{AH2}
$$
事实上若 $n\equiv1\bmod M$，沿所选直线 $\widehat G(nQ)=
\widehat G(Q)$ 准确无相位。于是 $\widehat G(Q)^{1-n^2}
=\phi_n(Q)/x(Q)^{n^2}\equiv1\bmod\mathfrak m$，
因为右侧是质量一的整形式级数在 $Q$ 处的值。
取 $n=1+M,1+2M$，两指数绝对值的最大公因数恰为 $M$：
除去 $M$ 后为 $M+2$ 和 $4(M+1)$，$M$ 奇。故该值是单位
且其剩余阶整除 $M$，于是剩余值为一。现在取
$n\equiv m\bmod M$ 并趋于 $\beta$；$R_n^-(Q)$ 逐项准确等于
$\widehat S(Q)\widehat G(mQ)^{-1}\widehat G(Q)^{n^2-17}$。
最后幂趋一，证明(AH2)，没有未控制的 Teich 根。$m$ 换成
$m+kM$ 沿同线不变；更换 $Q$ 的格代表时两个 Klein 相位之商
为一，因为 $2m^2\equiv34\bmod M$。

(AH2)以同一原复标记覆盖每个非零 $p$ 幂层。特别在 R716
首 wild 取 $Q_v=\varpi_1v/p$、$Nv=r$，其目标来自原曲线
$E_{17}$，真实相差 $\mathcal A_{17}(v/p)=\widehat S(Q_v)/17$。
以 $w\equiv mv\bmod p$ 取标准代表。$Nw=17r$；
$2(17r)=34r$，$q_p(m)$ 为实数，原 $\delta^{-1}$-迹杀它。
换代表所生的 degree-two Klein 相位与 R716(24),(25)
的字符 carry 相消。因此 R1062(G83)的同一质量可再读成
$$
 \mathscr S_p(r)=\frac1{17\cdot1008}
 \sum_{Nw=17r}(1008D)([m^{-1}]Q_w)\,
                  \chi^{(2)}_{p,17r}(w)\,\widehat G(Q_w).       \tag{AH3}
$$
这里 $17$ 来自曲线的物理缩放，$1008$ 则为新增固定全局单位
规范。$[m^{-1}]$ 只在 $p$ 挠点上取逆类。各项保原 Schwartz
及 R716(5)未除 $\sqrt{p+1}$ 的约定；(AH3)并非把非恒定
$D$ 从原环面和中提出。

最后取 $B_\beta(z)=G(\beta z)$，保持 R303 的 $d=p+1$、
$C=34c$，记 $J_{B_\beta}$ 是同一 $C$ 下的 Newton 读者。
在每个 $k\ge0$ 用 R303(23) 比较原系数：同 $C=34c$ 相对参考 $2c$ 给 $17^{-k}$，而 $[z^{dk}]G(\beta z)=17^{dk/2}[z^{dk}]G(z)$，故合因子恰 $17^{(p-1)k/2}$。继由稠密性得到
$$
 J_{B_\beta}(u)=17^{(p-1)u/2}J_{0,p}(u),\qquad
 \mathcal A_p(q_{\rm ac}^{du}-1)
     =C_{\rm Rub}\left({J_{D B_\beta}(u)\over J_{B_\beta}(u)}\right)^2 .
                                                                  \tag{AH4}
$$
$17^{(p-1)/2}\in1+p\mathbf Z_p$ 由 $(17/p)=1$，
且 $C_{\rm Rub}$ 是此前已定原 Rubin 比较常数，非上述 Gaussian
$C$。从而原随权 $17^{-(p-1)u}$ 在此正参考中准确消去。
(AH4)的分子读实际乘积 $D B_\beta=S_1$；全局单位与范数
相容性未把它换成 $D$ 单独的 Mellin，也未证明跨 $p$ 非零。

## 67. 同一全局单位在每个原第一 wild 角色上的非零对数分量

沿用(AH1)。对 $M=p^2$、$\varpi=\varpi_1$ 和
$v\in A_M^\times=(\mathcal O_K/M)^\times$ 置
$Q_v=\varpi v/M$。让 $\chi=\chi_{p,r}$ 为 R716(3)原角色，
$r\in\mathbf F_p^\times$，也可取其平方这个真实 Hecke twist。
于是
$$
 \boxed{\displaystyle
 \sum_{v\in A_M^\times}\chi(v)\log_p(1008D(Q_v))
  =(4+\chi(\gamma_7)+\chi(\gamma_7)^{-1})
       \sum_{v\in A_M^\times}\chi(v)\log_p\widehat\sigma(Q_v)
       \ne0 .}                                                    \tag{AI1}
$$
选定 $\log_p(p)=0$；由非平凡角色和零，也可先将每个
$\widehat\sigma(Q_v)$ 除以同一个 $\widehat\sigma(Q_1)$。
Klein 归一用(AE2)同一 $\widehat\sigma(Q_v)=
e^{-\eta_{Mv}^* z_v/2}\sigma(z_v)$，这里具体
$z_v=\varpi v/M$，$\eta_{Mv}^*=\eta_{Mz_v}/M$。
其平方的代数性由(AE2)保证，故指定的数本身代数；
改变格 lift 只改单位根，对两种对数都无影响。

第一个等式来自原除子，不用任何非零猜想。
取 $\delta=\sqrt{-3}$、$\gamma_7=3+\omega$。范数三的
规范除点函数为
$\sigma(\delta z)/\sigma(z)^3=\delta x(z)$：
核为 $O,(0,1),(0,-1)$，两边极零及原点领先项相同，
三次对称与 CM 准周期使其商为常数一。
所以 $G(z)=\sigma(\delta z)/(\delta\sigma(z))$，且 R297(19)给
$$
 S_1(z)=\frac1{28\delta^2}
    \prod_{a\in\{1,2,\delta,2\delta,\gamma_7,\bar\gamma_7\}}\sigma(az).
                                                                  \tag{AI2}
$$
对复乘 $a$，$|az|^2=Na\,|z|^2$，因此同一等式对各自
Klein 归一也准确成立。令 $m\equiv\sqrt{17}\bmod M$。
(AH2)给 $D(Q_v)=\widehat S(Q_v)/\widehat G(mQ_v)$；
各换元 $v\mapsto av$ 都是 $A_M^\times$ 的置换。
所需的 lift 相位在 $\log_p$ 中为零。每项 $a$ 因而乘
$\chi(a)^{-1}$。$\chi$ 在实单位 $2,m,7$ 上平凡，
$\chi(\delta)^2=\chi(-3)=1$ 且 $\chi$ 阶为奇数 $p$，
故 $\chi(\delta)=1$。$N\gamma_7=7$ 使两个七项互逆；
除去 $G(mQ_v)$ 的两项权重 $\chi(m)^{-1}-
\chi(\delta m)^{-1}$ 准确相消。常数由 $\sum_v\chi(v)=0$
消去。所得乘子为(AI1)的实代数数，任一复嵌入在 $[2,6]$。
在选定 $p$ 位还模极大理想等于 $6$，是单位。

证明最右非零。记 $A=\operatorname{area}(\mathbf C/\Lambda)/\pi$，
$[v,\lambda]=(\bar v\lambda-\bar\lambda v)/\delta\in\mathbf Z$。
Bannai–Furusho–Kobayashi 复 Th. 1.1(ii) 的同一
Klein 归一，结合该文(1)，给
$$
 \sum_{v\in A_M^\times}\chi(v)\log|\widehat\sigma(Q_v)|
 =-3A|\varpi|^{-2}\,\tau(\chi)L(1,\chi),\qquad
 \tau(\chi)=\sum_{v\in A_M^\times}\chi(v)e_M([v,1]).           \tag{AI3}
$$
具体在 $\Re s>1$ 先展开
$K_0^*(0,z_v,s)=|\varpi|^{-2s}\sum_{\lambda\ne0}
N(\lambda)^{-s}e_M([v,\lambda])$。$[v,\lambda]=[v\bar\lambda,1]$，
故单位 $\lambda\bmod M$ 的内和为
$\chi(\bar\lambda)^{-1}\tau(\chi)=\chi(\lambda)\tau(\chi)$；
$p\mid\lambda$ 时因 $\chi$ 在 $1+p\mathcal O_K$ 模 $p^2$
非平凡，该内和为零。有限加性 Fourier 的 Parseval 给
$|\tau(\chi)|=M$，因只有单位频率、且它们等幅。$K$ 类数一、
$\chi|_{\mu_6}=1$，故余下各非零元的和是 $6L(s,\chi)$。
延拓到 $s=1$ 后，由原刊第二极限公式中的 $-2\log|\widehat
\sigma|$ 及 $\sum\chi=0$ 得(AI3)。这个非平凡有限阶 Hecke
$L(1,\chi)$ 非零，也可直接对模 $M$ 射线类域的 Dedekind zeta
作阿贝尔分解：平凡项和射线类域 zeta 各有一阶极，而非平凡
项在一正则，因此各非平凡项在一均不为零；去掉分歧 Euler
因子亦无零。这里用的是单位角色 $L(1,\chi)$，不是 R716(8)
的权一 Hecke 角色中央值。[一手极限公式](https://www.math.nagoya-u.ac.jp/~furusho/paper/BFK.pdf)

最后所有比值 $u_v=\widehat\sigma(Q_v)/\widehat\sigma(Q_1)$
在所选 $p$ 位都是单位：在(AE2)取 $n=1+M,m=1$，
$t(Q)^{n^2-1}\psi_n(Q)$ 为单位，给
$v_p(\widehat\sigma(Q))=v_p(t(Q))$，而所有这些 $Q_v$ 同阶。
若所需 $p$ 进和为零，从有限个 $\log_p u_v$ 中取其
$\mathbf Q$-基。Baker–Brumer（可直接参见 Fuchs–Pham [Th. 2.1](https://web.math.pmf.unizg.hr/glasnik/51.2/51(2)-04.pdf)）使此基仍在
$\overline{\mathbf Q}$ 上独立，故用同一有理基消元后，
原角色关系的各代数系数都为零。$p$ 进单位对数的有理关系
清分母给全局乘积为单位根，所以相同关系也在
$\log |u_v|$ 中成立。这会使(AI3)为零，矛盾。
这样(AI1)在整个无限素数射线及其每个原第一 wild 角色成立。
它是(AH1)原单位的真实对数/ Kummer 分量，读取导子 $p^2$
上的全部单位；(AH3)仍读取 $p$ 挠点的指定 norm shell、原
参考相位、以及单位值本身。两种读取尚无从坏中央推出(AI1)
为零的证明。

## 68. 每条原首层纤维的非零 wild 对数与全部参考权的下降

沿用(AH1)与(AI1)，置 $U=1008D$、$M=p^2$、$A_j=\mathcal O_K/p^j$，
并写 $Q_{v,j}=\varpi_1v/p^j$。对 $w\in A_1^\times$ 取原格代表。
在 $\chi=\chi_{p,r}$ 或其平方下，实际 $p$ 个幂单位根相位给
$$
 B_\chi(w)=\sum_{\ell\in A_1}
       \frac{\chi(w+p\ell)}{\chi(w)}\log_p U(Q_{w+p\ell,2})
       \ne0.                                                       \tag{AJ1}
$$
这里求和有 $p^2$ 个原像。规范 $\log_p(p)=0$。更一般，对任意
代数系数 $a_w$，有
$$
 \sum_w a_w/\chi(w)\ne0\quad\Longrightarrow\quad
                     \sum_w a_w B_\chi(w)\ne0.                   \tag{AJ2}
$$
$w$ 的格代表须在两边同时使用；原像点本身不变。将(AH3)的全部
已定外权代入，取 $m\equiv\sqrt{17}\bmod p^2$、原
$Nw=17r$、$v=[m^{-1}]w\bmod p$ 的标准代表，即得
$$
 \boxed{\frac1{17\cdot1008}\!
 \sum_{Nw=17r}\chi^{(2)}_{p,17r}(w)\widehat G(Q_{w,1})
                     B_{\chi_{p,r}}(v)\ne0.}                     \tag{AJ3}
$$
$\chi^{(2)}$ 上标沿用(AH3)表示 degree-two 参考的实际规范。
(AJ1)也容许取 primitive Hecke twist $\chi_{p,r}^{\,2}$。
(AJ3)保留(AH3)的每个原外权、范数条件与固定乘子，仅把原像
$U(Q_{v,1})$ 的评价换为同纤维上的非平凡 wild 对数和。

证明。$L_v=\log_p U(Q_{v,2})$ 是有限个全局代数数在所取
$p$ 位的对数。$U\in\mathbf Q_p[[t]]$ 在整形式盘收敛，$t$
是有理严格局部坐标，对每个局部 Galois 自同构与此评价可交换。
R663(1)–(3)、R696(10)–(11)在 $E_1$ 也逐字适用：
好惰性处 $\mathrm{Fr}_p^2=[-p]$，整坐标给
$[-p]v=-pv+v^{p^2}$。primitive 二层坐标的
$(X^{p^2}-pX)^{p^2-1}-p$ 是 Eisenstein；局部次数达到
整个 $(\mathcal O_K/p^2)^\times$ 的阶。故每个
$v\mapsto bv$ 实现为局部 CM Galois 作用。于是所有 $L_v$
的有理关系构成 $\mathbf Q[A_2^\times]$ 的平移稳定子空间。
同阶点满足 $v_p(U(Q_{v,2}))=6/(p^2(p^2-1))$，由
$t^{-6}D\equiv1\bmod t$ 及上述 Eisenstein 方程可见；
消掉同一有理次 $p$ 幂并取足够大公共幂即可转为主单位，
$p$ 进对数值只同时乘该公共幂。取 $L_v$ 的一个有理基，
Baker–Brumer（Fuchs–Pham [Th. 2.1](https://web.math.pmf.unizg.hr/glasnik/51.2/51(2)-04.pdf)）保它在 $\overline{\mathbf Q}$ 上独立；
因此其所有代数关系核恰为上述有理关系核的标量扩张。
特别该核在固定系数的指标置换下稳定，毋须局部 Galois 同时
固定 $\zeta_p$ 或外部参考质量。

对任意系数向量 $c(v)$，环平移的 $\chi$-投影为
$\chi(v)|A_2^\times|^{-1}\sum_u c(u)/\chi(u)$。
(AI1)断言 $\chi(v)$ 本身不在此核。因此只要该投影非零，
原向量也不在核。取
$c(w+p\ell)=a_w\chi(w+p\ell)/\chi(w)$，其和恰为
$p^2\sum_w a_w/\chi(w)$，证(AJ1)–(AJ2)。
(AJ3)中(AH2)的全部 $\widehat G(Q_{w,1})$ 在所选 $p$ 位
都是主单位；两种原角色也是 $p$ 幂根。因此所需和的每一项
$\chi^{(2)}_{p,17r}(w)\widehat G(Q_{w,1})/\chi_{p,r}(v)$
模极大理想为一，原壳恰有 $p+1$ 项，和模极大理想为一。

还有可复核的复端单纤维降导子式。记 $\chi=\chi_{p,r}^{\,h}$，
$h=1,2$；$k=17hr/Nw\in\mathbf F_p^\times$。由 R716(3)
直接展开 $(w+p\ell)^p/\overline{w+p\ell}$，
$$
 \chi(w+p\ell)/\chi(w)=e_p(-k[\ell,w]),\qquad
 [u,v]=(\bar u v-\bar v u)/\delta.                               \tag{AJ4}
$$
特别规范壳 $Nw=r$ 上 $k=17h$，$h=1$ 正是 R716(25)。
对非零模 $p$ 的每个原乘数 $a$，取整数
$b_a\equiv k/(Na)\bmod p$。置
$$
 Z_w(a)=-\frac{A}{2|\varpi_1|^2}\left.
     \sum_{\nu\in\mathcal O_K}
       \frac{e_p([aw,\nu])}{|\nu+b_a aw/p|^{2s}}
                         \right|_{s=1},\qquad
 A=\operatorname{area}(\mathbf C/\Lambda)/\pi .                 \tag{AJ5}
$$
和从 $\Re s>1$ 亚纯延拓；非平凡扭项使它在一正则。
它准确等于
$\sum_{\ell}e_p(-k[\ell,w])\log|\widehat\sigma(aQ_{w+p\ell,2})|$。
事实上 BFK 复第二极限公式 Th. 1.1(ii) 的常数在该纤维相位和中
消失。展开其级数后，$\ell$ 的加性 Fourier 和强制
$\bar a\lambda=kw\bmod p$，贡献 $p^2$。
其余频率写 $\lambda=b_a aw+p\nu$，因 $b_a$ 为有理整数，
$[aw,b_a aw]=0$，原 $p^2$ 相位降为 $e_p([aw,\nu])$。
此时 $p^2 p^{-2s}$ 在一为一，证明(AJ5)的全部系数。
改变 $b_a$ 一个 $p$ 倍数也由相同的交替配对得相位一。
故(AJ1)中的 $p$ 进对数换成同一组代数数的复绝对值对数后，
完整来源准确为
$$
 \sum_{a\in\{1,2,\delta,2\delta,\gamma_7,\bar\gamma_7\}}Z_w(a)
                      +Z_w(m)-Z_w(\delta m).                      \tag{AJ6}
$$
这是(AI2)和(AH2)在每个实际纤维的版本；分母的两项在单纤维
不能提前删去。(AJ5)–(AJ6)是复端等式，(AJ1)–(AJ3)另由整
形式群、真实全局单位和 Baker–Brumer 证得。原(AH3)读单位值，
(AJ3)读(AJ4)的对数 Fourier 分量。两者以及原(AH4)的中央
Newton 导数之间，还须证明合适的比较。

## 69. 同一单位族在原全驯标记上的不变对数微分读出真正的一阶 Hecke 中央值

保留 $M=p^2$、原 $\chi=\chi_{p,r}$、原 $E_1$ 的
$\varpi=\varpi_1$。取 $f=34\delta$、$(\mathcal O_K/f)^\times$
中的 $t$ 及 $(\mathcal O_K/M)^\times$ 中的 $w$。记
$$
 T_t=\varpi t/f,\qquad Q_w=\varpi w/M,\qquad
 P_{t,w}=T_t+Q_w,\qquad X(P)=\zeta(P)-\bar P/A.
$$
此处 $X$ 是 R298(15)的 reduced zeta，非椭圆横坐标。
令 $m\equiv\beta=\sqrt{17}\bmod M$；$m$ 可按中国剩余取正整数
且 $m\equiv1\bmod f$。对物理有理函数
$R_n^-=S_1/(G(nz)G(z)^{17-n^2})$，定义
$$
 D_t(z)=\lim_{\substack{n\to\beta\ (p\text{ 进})\\
                         n\equiv1\bmod f}}
                    R_n^-(T_t+z)/R_n^-(T_t),\qquad
 \ell_t(Q)=\bigl(d\log D_t/dz\bigr)(Q).                          \tag{AK1}
$$
$dz=dx/(2y)$；在 $p$ 挠点评价导数时使用不变导子及整形式
局部参数。$\ell_t$ 来自同一全函数的平移族，不假定某个单独
$\sigma$ 在超奇异全盘收敛。

为证(AK1)全盘存在，$p\nmid n$ 且 $[n]T_t=T_t$。$T_t$ 及
$[n]T_t$ 都是 primitive $f$ 挠，约化仍有其确切阶且含非零
十七分量。因此其约化避开 $D_S,D_G$ 的支撑：R297 的六、七、
三、二及原点均无十七分量。在好约化整模型上，$R_n^-$ 的水平
零极除子均不经过 $T_t$ 的剩余盘；任意垂直常数由除以
$R_n^-(T_t)$ 消去。所以每个归一函数及其逆在此盘的整形式环，
常数均为一。记 $V_T(z)=e^{-e\eta_T(z+T/2)}V(T+z)$ 为
charge $e$ 的原平移，$\eta_T=\bar T/A$。一个格平移只使 $V_T$
乘常数，故 $V_T(z)/V_T(0)$ 与格代表无关。特征零形式上准确有
$$
 \frac{R_n^-(T_t+z)}{R_n^-(T_t)}
 =\frac{S_{T_t}(z)}{S_{T_t}(0)}
  \frac{G_{T_t}(0)}{G_{T_t}(nz)}
   \left(\frac{G_{T_t}(z)}{G_{T_t}(0)}\right)^{n^2-17}.
$$
取值与幂的全部有限系数在同一代数 $p$ 进域：各平移的首对数
导数由 $X$ 的挠点值给出，后续导数由 $\wp,\wp'$ 给出。
$X$ 的挠点代数性也可在 $\sigma(Nz)/\sigma(z)^{N^2}$ 的除点
函数于挠点取对数导数的常数项，如 R298(20)。此式逐系数连于
$n$，整形式坐标与 Lie 坐标各次互换均为固定有限变换。
故规范比及其逆均逐系数收敛，靠统一整界在每个严格内闭盘
一致收敛；不变导数亦在这些闭盘收敛，可在 $Q_w$ 取极限。
$T=O$ 的未除初值版本是(AH1)的同一 $D$。

设 $\mathcal D=\{1,2,\delta,2\delta,\gamma_7,\bar\gamma_7\}$。
(AI2)的实际六因子与 $G=\sigma(\delta z)/(\delta\sigma(z))$ 给
$$
 \ell_t(Q_w)=\sum_{a\in\mathcal D}aX(aP_{t,w})
    -\beta\bigl(\delta X(\delta(T_t+mQ_w))-X(T_t+mQ_w)\bigr).    \tag{AK2}
$$
确实对有限 $n$ 先对 $R_n^-$ 取不变对数导数，$\zeta$ 换为 $X$
时总非全纯增量为
$(34-2n^2-2(17-n^2))\bar P/A=0$。参考还带
$-(17-n^2)(\delta X(\delta P)-X(P))$，极限为零。
$nP=T_t+mQ_w$ 在该有限层最终固定，于是得(AK2)。
把中间 $n$ 换成 $\beta$ 并直接复评价是无须且不正确的步骤。

令 $\varepsilon$ 为 R298(12)真正导子 $f$ 的原有限角色，
$\psi_{17}((a))=a/\varepsilon(a)$。下式保全部 $t,w$：
$$
 \boxed{\sum_{t,w}\varepsilon(t)\chi(w)^2\ell_t(Q_w)
   =u_{p,r}\,\frac{6 f M}{\varpi}\,
                  L(\psi_{17}\widetilde\eta_{p,r},1),}
 \quad
 u_{p,r}=1+\beta+
   \sum_{a\in\{\gamma_7,\bar\gamma_7\}}
       \frac{a}{\varepsilon(a)\chi(a)^2}\in\mathcal O_{\mathbf C_p}^\times .
                                                                    \tag{AK3}
$$
等式把代数系数与 R716 的实际复周期按 R298 固定嵌入比较。
具体说，R716(32)–(33)使用的有限 idele 角色在 $p$ 为
$\chi^2$。以理想 $(a)$ 的好位 uniformizer idèle 为代表，再
除以主元 $a$，$p$ 处的单位为 $a^{-1}$，故其理想角色值为
$\chi(a)^{-2}$。原 $\varepsilon(\bar a)=\varepsilon(a)^{-1}$、
$\chi(\bar a)=\chi(a)^{-1}$。对所有主理想以 $a\mapsto\bar a$
换元，得
$$
 L(\psi_{17}\widetilde\eta_{p,r},1)
     =\frac16\sum_{(a,fM)=1}^{*}
                       \frac{\varepsilon(a)\chi(a)^2}{a}.
$$
星号表示从绝对收敛区间亚纯延拓。R298(10)的 Kronecker 展开在
$(0,0)$ 系数给 $e_{0,1}^*(P,0)=X(P)$，恰是
$\sum_{\lambda\in\varpi\mathcal O_K}^*1/(P+\lambda)$。
写 $a=Mt+fw\bmod fM$，$\varepsilon(M)=1$ 因 $M=p^2$、
$\varepsilon_1(p)^2=1$ 且 $\chi_{17}$ 在有理单位上平凡；
$\chi(f)=1$ 因 $f=34\delta$。此时
$$
 \sum_{t,w}\varepsilon(t)\chi(w)^2 X(P_{t,w})
   =\frac{6 f M}{\varpi}L(\psi_{17}\widetilde\eta_{p,r},1).
$$
对于 $a=2,\delta,2\delta$，$aT_t$ 因子化通过严格更小的驯模，
原 $\varepsilon$ 在约化核上非平凡，故对应整项和为零；
同理分母的 $\delta(T_t+mQ_w)$ 项为零。六项中其余三项均
可置换 $(t,w)\mapsto(at,aw)$，乘子为
$a/(\varepsilon(a)\chi(a)^2)$。最后 $T_t+mQ_w$ 仅置换 $w$，
且 $\chi(m)=1$，给 $+\beta$。这是(AK3)的无缺项乘子。
在所选 $p$ 位它的剩余值为
$1+\beta+j$，其中
$j=\operatorname{Tr}_{K/\mathbf Q}(\gamma_7/\varepsilon(\gamma_7))$
为绝对值至多 $2\sqrt7$ 的整数。有理整数 $(1+j)^2-17$
非零且绝对值至多 $19$，故每个 $p>211$ 都是单位，证(AK3)。

特别，R716(8)允许将(AK3)右端严格写成
$u_{p,r}\,(6f p^2/\varpi)\,48940416\,\Omega_{\mathbf R}
|\mathscr S_p(r)|^2/p$。这里 $\Omega_{\mathbf R}$ 是
$E_{17}$ 的实际正实周期，$\varpi$ 是 $E_1$ 的实际 CM 生成
周期；二者不交换。如此获得了原 $p^2$ 层空间对数微分和原
$p$ 层全部 Schwartz 外权的准确读回。若在全驯标记用偶
绝对值对数或忽略 Klein 根单位后的 $p$ 进对数作同一
$\varepsilon(t)\chi(w)^2$ 投影，则 $(t,w)\mapsto(-t,-w)$
下该零阶和为零，因 $\varepsilon(-1)=-1$、$\chi(-1)=1$。
(AJ3)的非零读数与(AK3)的这项真实空间微分因此不能仅由奇偶性
相认；(AK3)没有证明原 Hall 中央值或(AH4)的权导数非零。

## 70. 原有理单位全除子的 Poincaré 核与平凡有限角色的准确 native 平方

继续(AK1)的实际驯余类；$M=p^2$ 取原 wild 标记，另容许
$M=1,\chi=1,Q=O$，这时只求和 $t\in(\mathcal O_K/f)^\times$。
固定 $\Theta_P(z,y)$ 为 R298(10)的 Kronecker 函数
$$
 \Theta_P(z,y)=e^{-\bar P y/A}\,
       \frac{\sigma(P+z+y)}{\sigma(P+z)\sigma(y)}.
$$
对任意非零 $a\in\mathcal O_K$，有真正的除子拉回
$$
 a\Theta_{aP}(az,y/\bar a)
             =\sum_{V\in E_1[a]}\Theta_{P+V}(z,y).                \tag{AL1}
$$
$P,V$ 的格代表不影响等式。事实上两边在每个
$z=-P-V$ 的留数均为 $e^{-\overline{P+V}y/A}$：左边用
$aV\in\Lambda$ 的带符号准周期，且 $\eta_{aV}/\bar a=\bar V/A$。
在 $z\mapsto z+\lambda$ 下两边同乘 $e^{\bar\lambda y/A}$。
固定 $y\notin\Lambda$，差在椭圆曲线上是非平凡度零线丛的
全纯截面，故为零；再亚纯延拓。这也逐项说明了为何原向量
变量取 $az$，对偶变量取逆共轭 $y/\bar a$，而不是同时乘 $a$。

对有限 $n$，以(AK1)的原有理函数 $R_n^-$ 的全除子作 Cauchy
核，即以每个真实零极点的重数加权右边的 $\Theta_{P+V}$。
$R_n^-$ 为偶函数，故 $V$ 或 $-V$ 给同一重数。定义
$H_a(P;z,y)=a\Theta_{aP}(az,y/\bar a)$，则(AL1)给此和恰为
$$
 \sum_{a\in\mathcal D}H_a(P;z,y)
       -H_{\delta n}(P;z,y)+H_n(P;z,y)
       -(17-n^2)\bigl(H_\delta(P;z,y)-H_1(P;z,y)\bigr).
                                                                    \tag{AL2}
$$
这是(AI2)、$G=\sigma(\delta z)/(\delta\sigma(z))$ 的同一
有理近似。$y^{-1}$ 极系数为完整度数
$34-2n^2-2(17-n^2)=0$，且 $y^0z^0$ 就是该比值在 $P$ 的真实
不变对数导数。在 $P=T_t+Q_w$、$n\equiv1\bmod f$ 并
$n\equiv m\bmod M$ 时，$(\delta n)P,nP$ 都固定，每一项中
缩放 $n,1/n$ 逐系数连续。Kronecker 挠点 Laurent–Taylor
系数代数，由 R298(10)的 $X(P),\wp(P),\wp'(P)$ 展开，或由
Bannai–Kobayashi [Th. 1.17](https://arxiv.org/pdf/math/0610163)。所有实际 $aP$ 在本节都非零。
因此 $n\to\beta$ 有逐系数特征零极限 $\mathcal K_{t,w}(z,y)$；
(AK2)是它的常数项。这里只拿逐系数极限，不需要误称两变量
Kronecker 核在整个超奇异开双盘一致有界。

对 $h=dj$、$d=p+1$、每个 $j\ge0$，定义实际对角
$$
 B_{M,h}=\sum_{t,w}\varepsilon(t)\chi(w)^2
                         [z^h y^h]\mathcal K_{t,w}(z,y).
$$
$6\mid h$；$\xi_{p,r}=\widetilde\eta_{p,r}$ 或 $M=1$ 时
$\xi_{p,0}=1$。原双曲线 CM 配对给完全标记的身份
$$
 B_{M,h}=u_{p,r}(j)\,
 \frac{6}{h! A^h}\frac{\bar\varpi^h}{\varpi^{h+1}}\,
 \frac{(f M)^{h+1}}{(\bar f M)^h}
           L(\psi_{17}^{2h+1}\xi_{p,r},h+1),                    \tag{AL3}
$$
其中
$$
 u_{p,r}(j)=1+\beta+
   \sum_{a\in\{\gamma_7,\bar\gamma_7\}}
     \frac{a}{\varepsilon(a)\chi(a)^2}
                  \big((a/\bar a)^d\big)^j .                     \tag{AL4}
$$
事实上 $c_{h,h}(P)=[z^hy^h]\Theta_P(z,y)$，其缩放系数正是
$a(a/\bar a)^h$。在原 $\varepsilon(t)\chi(w)^2$ 投影中
$2,\delta,2\delta$ 及参考的 $\delta$ 项和(AK3)逐项同样为零，
最后 $n$ 项的系数是 $n$，极限为 $\beta$，因为 $n/\bar n=1$。
其余两项保实际 $a/(\varepsilon(a)\chi(a)^2)$，给(AL4)。
Bannai–Kobayashi [Th. 1.17](https://arxiv.org/pdf/math/0610163) 的符号在此为 $(-1)^{2h}=1$，
$$
 c_{h,h}(P)=(h!A^h)^{-1}\!
  \sum_{\lambda\in\varpi\mathcal O_K}^{*}
                  \frac{\overline{P+\lambda}^{h}}{(P+\lambda)^{h+1}}.
$$
在绝对收敛区分 $a=Mt+fw\bmod fM$ 再延拓。$\varepsilon^{2h+1}
=\varepsilon$，$\varepsilon(M)=\chi(f)^2=1$，同(AK3)的理想角色逆
及共轭给(AL3)。当 $M=1$，CRT 只剩 $a=t\bmod f$。

(AL4)在整个 $p$ 进 $j$ 盘上是整解析单位。每个 $a/\bar a$
的模 $p$ 范数为一，故 $(a/\bar a)^d\in1+p\mathcal O_{K_p}$。
其 $j$ 次幂用固定的 $\exp(j\log((a/\bar a)^d))$，属整 Tate
代数且模极大理想恒一。余下常数的单位性正是(AK3)已核的
$(1+\operatorname{Tr}(\gamma_7/\varepsilon(\gamma_7)))^2-17$。
特别没有把 $a^{2h}$ 的 Teich 径向分支隐含在单位中。

在目标的原平凡有限角色 $M=1$，令 $C=34c$，
$\theta=17^{1/6}$，$\kappa_0=48940416$，置
$C_*=6f\kappa_0(1-\omega)\theta^{-13}$。此时
$$
 \boxed{\;B_{1,h}=C_*u_{p,0}(j)34^{-h}\alpha_h^2,\qquad
       (j!)^2 34^{dj}C^{-2j} B_{1,dj}
            =C_*u_{p,0}(j)J_p(j)^2.\;}                          \tag{AL5}
$$
确实 $A=(\sqrt3/(2\pi))|\varpi|^2$，目标
$\varpi_{17}=\varpi/\theta$，因此将原 R298(9)
$\mathcal E_h^{\rm CM}=\kappa_0(1-\omega)34^{-h}s_h^2$
代入(AL3)时，全部 $A^h,h!$ 及复周期完全消去，
留 $6(f^{h+1}/\bar f^h)\theta^{-(2h+1)}$。$f$ 纯虚、$h$ 偶，
前一幂商为 $f$；R303(3)的 $s_h=\theta^{h-6}\alpha_h$ 正好
再化为 $\theta^{-13}$。第二式用 R303(23)实际
$J_p(j)=j!C^{-j}\alpha_{dj}$。因而(AL5)左侧整数点取值有
唯一的连续插值 $F_p$，且在全盘满足
$$
 F_p''(0)=2 C_* u_{p,0}(0)J_p'(0)^2.                             \tag{AL6}
$$
$J_p(0)=0$，所以没有遗漏(AL4)的导数项。由 R303(8)，只须在无穷
多个本射线素数上证这同一全除子的规范对角二阶非零，即得固定
$E_{17}$ 的通常全 $\Sha[p^\infty]$ 有限。(AL6)实际接到了原
native 中央。它同(AJ3)的有限非平凡 wild 对数之间仍缺一个能
强迫该二阶非零的结论。

## 71. 全驯导子及实际 Rubin 的 $\Delta$ 型上的非零 Kummer 对数

仍取(AK1)真实的 $D_t$。允许 $M=p$、$\chi=1$，或
$M=p^2$、$\chi=\chi_{p,r}$；前者为平凡 wild，后者的实际
Hecke twist 为 $\chi^2$。写 $\tau(w)=[w\bmod p]$ 为选定
$K_p$ 嵌入的 Teichmüller 单位，$\Delta=(\mathcal O_K/p)^\times$；
$T_t=\varpi t/f$、$Q_w=\varpi w/M$，两者指标均取全部单位。
则
$$
 \boxed{\ \sum_{t,w}\varepsilon(t)\tau(w)^{-1}\chi(w)^2
                 \log_p D_t(Q_w)\ne0.\ }                          \tag{AM1}
$$
这里的 $p$-tame 因子确为 $\tau^{-1}$：在以 $b\in\Delta$
将 $w$ 送到 $bw$ 的算术作用下，$\tau$ 型投影使用
$|\Delta|^{-1}\sum_b\tau(b)^{-1}[b]$。与原 LT Tate 模
$T_\pi^{-1}$ 张量后正成为 $\Delta$ 不变量，如
Burungale–Kobayashi–Ota，*p-adic L-functions and rational points
on CM elliptic curves at inert primes*，[§2.1.1](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf) 的 $U_\infty^*$。
(AK3)的空间微分另用不带此 $\tau^{-1}$ 的分量。

令 $P=T_t+Q_w$。直接的点值对数公式为
$$
 \log_p D_t(Q_w)=\log_p\frac{\widehat S(P)}{\widehat S(T_t)}
                  -\log_p\frac{\widehat G(T_t+mQ_w)}
                                      {\widehat G(T_t)},
 \qquad m\equiv\beta\bmod M,\quad m\equiv1\bmod f.              \tag{AM2}
$$
确实(AK1)对有限 $n$ 的四个 Klein 因子之非全纯指数由总度零
准确相消。把 $[n]P$ 换成 $T_t+mQ_w$、$[n]T_t$ 换成 $T_t$
的格代表变化只给根单位，故在 $\log_p$ 中为零；还剩
$(n^2-17)\log_p(\widehat G(P)/\widehat G(T_t))$，极限为零。
$\widehat\sigma(R)$ 在每个用到的点是代数 $p$ 单位：
取 $N>1$、$N\equiv1$ 模实际挠点阶且 $p\nmid N$，
$\widehat\sigma(R)^{1-N^2}$ 相差根单位等于实际除点函数
$\psi_N(R)$。$R$ 的约化非零且 $[N]\bar R=\bar R$，在好整
模型上 $\psi_N(R)$ 为单位。这里即使乘了 $2,\delta,2\delta$
也保非零十七分量；乘 $\gamma_7,\bar\gamma_7$ 或参考 $m$ 亦然。
所以(AI2)及 $G=\sigma(\delta z)/(\delta\sigma(z))$ 使(AM2)
成为有限个代数 $p$ 单位的对数式。(AK1)在相应有界剩余盘的
一致极限值为主单位，使上式左端的对数连续。需要 Baker
的只是右侧的这些实际代数数。

置 $\rho(a)=\varepsilon(a)\tau(a)^{-1}\chi(a)^2$，为模
$F=fM$ 的原始有限角色。它在 $\mu_6$ 上平凡，因为
$\varepsilon(u)=u=\tau(u)$、$\chi(u)=1$。在 $f$ 处的本原性
是(AK3)的原导子。在 $M=p$ 处由 $\tau^{-1}$ 本原，在 $M=p^2$
处由 $\chi^2$ 在第一主单位上非平凡而本原。先全和(AM2)：
独立于 $w$ 的两个基值因 $\tau^{-1}\chi^2$ 非平凡消失；
$2,\delta,2\delta$ 及分母 $\delta$ 项经驯标记均和(AK3)同样
消失。其余乘数在各自 $t,w$ 槽的置换给
$$
 \sum_{t,w}\varepsilon(t)\tau(w)^{-1}\chi(w)^2\log_p D_t(Q_w)
   =v_{p,r}\sum_{t,w}\varepsilon(t)\tau(w)^{-1}\chi(w)^2
                          \log_p\widehat\sigma(P),\qquad
 v_{p,r}=1+\tau(m)+
       \sum_{a\in\{\gamma_7,\bar\gamma_7\}}
                       \frac{\tau(a)}{\varepsilon(a)\chi(a)^2}.   \tag{AM3}
$$
参考 $m$ 只在 $w$ 槽缩放且 $\chi(m)=1$。$v_{p,r}$ 模极大理想
即(AK3)的 $1+\beta+\operatorname{Tr}(\gamma_7/\varepsilon(\gamma_7))$，
因此是单位。尤其零阶的全驯投影在付入真实 $\Delta$ 型后不再
被同时取负杀去。

为证最后的实际和非零，固定任一复嵌入。以 $a=Mt+fw$ 作 CRT。
当 $M=p$ 时应保留一般的
$\varepsilon(p)$，它是非零六次根（当 $M=p^2$ 时才保证为一）。
由此在两种情形**统一**用
$c_M=\tau(f)/\varepsilon(M)$，得到
$$
 \sum_{t,w}\varepsilon(t)\tau(w)^{-1}\chi(w)^2
                      \log|\widehat\sigma(P)|
   =-\frac{3A}{|\varpi|^2}\,c_M\,g_F(\rho)
                      L(1,\rho^c),\quad
 \rho^c((\lambda))=\rho(\bar\lambda)^{-1},
 \quad
 g_F(\rho)=\sum_{a\bmod F}^{\times}\rho(a)e^{2\pi i[a/F,1]} .   \tag{AM4}
$$
这里 $\chi(f)=1$；$\tau(f)$ 是原 $f$ 的剩余单位。
$[x,y]=(\bar x y-\bar yx)/\delta$，其在整格上完美。
BFK Th. 1.1(ii)同(AI3)，对任意格频率 $\lambda$ 的内和
用 $[a/F,\lambda]=[a\bar\lambda/F,1]$。$\lambda$ 为模
$\bar F$ 的单位时得 $g_F(\rho)\rho(\bar\lambda)^{-1}$，
否则因 $\rho$ 在相应严格降模的核非平凡而为零。
配对的对偶模是 $\bar F$，本处与 $F$ 为相同理想；Parseval
给 $|g_F(\rho)|=\sqrt{NF}$。$h_K=1$、$\rho|_{\mu_6}=1$
让元和化成 $6L(s,\rho^c)$。$\rho^c$ 是非平凡有限 Hecke
角色，射线类域的 Dedekind zeta 分解给 $L(1,\rho^c)\ne0$。
$\widehat\sigma(P)$ 全为代数 $p$ 单位；若对应 $p$ 对数和为零，
Baker–Brumer（Fuchs–Pham [Th. 2.1](https://web.math.pmf.unizg.hr/glasnik/51.2/51(2)-04.pdf)）与同一有理关系经过全局根单位转到复绝对值，
将使(AM4)为零，矛盾。由(AM3)即证(AM1)。

因此原平凡及第一 wild 层在完整 $2,3,17$ 标记并取了
$U_n\otimes T_\pi^{-1}$ 所需的有限 $\Delta$ 型后，均有无条件
非零的实际全局 Kummer 对数读数。完整 $T_\pi^{-1}$ 另在
主单位方向有无限阶作用；(AM1)不把有限 $\tau$ 当作这整个
局部角色，也不等同于 BKO §2.1.1(2.1)的 Coates–Wiles 空间
导数 $\delta_\chi$ 或(AL6)的 native 二阶。

## 72. 原平移单位在整的双变量 LT Kummer 模中的 Robert 单位比较

令 $c=103$，则 $c\equiv1\bmod f$（$c-1=102$ 可被 $34\delta$
整除），$p>211$。取 $L=K_p(E_1[f])$，由好约化及 $(p,f)=1$
这是有限未分歧扩张。令 $L_j=L(E_1[p^j])$，$j\ge1$；
$A_j^\times=(\mathcal O_K/p^j)^\times$ 为其相对 $L$ 的整个
Galois 群，$[a]$ 表示在 $p$ 挠标记上的 $w\mapsto aw$。
取 $Q_j=\varpi/p^j$，$T_{t,j}=[p^{-j}\bmod f]T_t$，则
$[p](T_{t,j+1}+Q_{j+1})=T_{t,j}+Q_j$。用这样的 $+p$ 相容点
选原像；若改用 $-p$ 的 Tate 基，同时将第 $j$ 个点乘
$(-1)^j$，其原射线及 Tate 角色均按同一基运输。
令 $\mathcal O=\mathcal O_{K_p}$，
$V_j=e_\tau(U^1(L_j)\otimes_{\mathbf Z_p}\mathcal O)$。
任何局部单位均先取主单位部分，写在加法记号的张量中。
这里 $e_\tau=|\Delta|^{-1}\sum_{b\in\Delta}\tau(b)^{-1}[b]$，
$\Delta=\mu_{p^2-1}$。定义
$$
 d_j=e_\tau\sum_t\varepsilon(t)\,
                   D_{p^{-j}t}(Q_j),\qquad
 r_j=e_\tau\sum_t\varepsilon(t)\,
        \Theta_{E_1,(c)}(T_{t,j}+Q_j) .                            \tag{AN1}
$$
$D_{p^{-j}t}$ 是(AK1)的实际整主单位，$\Theta_{E_1,(c)}$ 为
Rubin 的标准 Robert 函数。后者在此 primitive 混合导子挠点是
实际全局单位（Rubin Th. 7.4(iii)），且 Th. 7.6、Cor. 7.7
给逐层范数相容。因 $[p]$ 时指数 $j\ge1$，这里用的是同素数
已分歧的那一行，无须额外插入第一未分歧 Euler 因子。
Rubin Lemmas 7.5、7.10 的相反除子及十二次幂，在当前尺度为
$$
 \Theta_{E_1,(c)}(P)=\Delta(E_1)^{c^2-1}\psi_c(P)^{-12},
 \qquad \psi_c(z)=\sigma(cz)/\sigma(z)^{c^2}.                    \tag{AN2}
$$
亦可从 Lemma 7.5 比较除子后，在零点比较其首 Laurent 系数。
与 $p$ 挠标记无关的判别式常数被 $e_\tau$ 杀掉。
[Rubin，§7](https://swc-math.github.io/aws/1999/99RubinCM.pdf)

在 $e_\tau\mathcal O[[\mathcal O_{K_p}^\times]]
\simeq\mathcal O[[1+p\mathcal O_{K_p}]]$ 中置
$$
 H=1+[\beta]+
   \varepsilon(\gamma_7)^{-1}[\gamma_7]+
   \varepsilon(\bar\gamma_7)^{-1}[\bar\gamma_7],
 \qquad J=[c]-c^2 .                                                \tag{AN3}
$$
等式里相应 $e_\tau$ 是该直因子的幺元。则有
$$
 \boxed{\quad (d_j)_j=-\frac1{12}\,H J^{-1}(r_j)_j
             \quad\text{在 }\varprojlim_j V_j\text{ 中，}\qquad
                    H,J\in(e_\tau\mathcal O[[\mathcal O_{K_p}^\times]])^\times .
       \quad}                                                       \tag{AN4}
$$
证明。对每个 $j$，暂以 $b(w)$ 记
$\sum_t\varepsilon(t)\log_p\widehat\sigma(T_{t,j}+[w]Q_j)$
的带标记列。原始各 $\log_p\widehat\sigma$ 是普通域元素：
可先在包含这些代数点值的某有限局部扩域中工作，并把所有有限
标量放在外部的 $\otimes_{\mathbf Q_p}K_p$。这保两个张量嵌入；
不使用单个乘法映射 $L_j\otimes K_p\to\mathbf C_p$ 的单射性。
以 $w\mapsto aw$ 作列的平移。(AM2)逐点在本层同样成立；
$e_\tau$ 消去与 $w$ 无关的基值，全驯标记杀 $2,\delta,2\delta$
及分母 $\delta$ 项，其余准确给 $H b$ 的 $e_\tau$ 分量。
$\widehat\sigma(cP)/\widehat\sigma(P)^{c^2}=\psi_c(P)$，
且 $cT_{t,j}=T_{t,j}$，格代表变化的根单位被对数杀掉。
所以(Rubin)列为 $-12J b$ 的 $e_\tau$ 分量。消去 $b$ 后，
两边只涉及来自 $L_j$ 本身的单位，并且在指标列上 $[a]$ 平移
正是 $L_j/L$ 的 Galois 作用，每个 $T_{t,j}$ 固定。
$J d_j=-(H/12)r_j$ 的对数关系于是成立在
$L_j\otimes_{\mathbf Q_p}K_p$ 中。

局部对数在主单位上的核为 $p$ 幂根。$\Delta$ 在这些根上
通过 Weil 配对给 $N_{K_p/\mathbf Q_p}(b)=\tau(b)^{p+1}$，
此型与 $\tau$ 不同。故 $e_\tau$ 杀全部该核，张量 $\mathcal O$
平坦，所用对数在 $V_j$ 上单射。这样上述等式回到**整**
Kummer 模，既未丢 $p$ 幂挠，也未在分量上擅除 $p$。
(AN3)的增广剩余值分别为(AK3)已证的
$1+\beta+\operatorname{Tr}(\gamma_7/\varepsilon(\gamma_7))$
及 $c-c^2$；$c(c-1)=103\cdot102$，其素因子均小于 $211$。
该完备局部群环中两者均可逆。$r_j$ 由原 Robert 分布相容，
(AN3)与各层群环映射及范数交换，故 $d_j$ 亦整相容，证(AN4)。

(AN4)可施整个 $T_\pi^{-1}$ 的 Tate 扭转，再取反圆分协不变量。
在先有的单位列上作用 $[a]$、再张量固定对偶基，与先张量后作用
$[a]$ 相比确切多 $a$，因为 $[a]$ 对该对偶基作用 $a^{-1}$。
于是(AN3)分别变为
$$
 1+\beta+\sum_{a=\gamma_7,\bar\gamma_7}
                   \frac{a}{\varepsilon(a)}[a]_{\rm ac},
       \qquad c-c^2 .                                             \tag{AN5}
$$
这里用二者的 $p$ 进有理标量方向：
$\beta\in\mathbf Q_p^\times$，$c\in\mathbf Q^\times$，
所以二者在反圆商均取平凡类。评于
$[a]_{\rm ac}\mapsto\chi(a)^{-2}(a/\bar a)^{dj}$（$j$ 此时是
权变量），得到的分子恰是(AL4)，不是只在剩余域一致。
若作 BKO(3.1)的共轭/反演识别，应同步反演反圆群变量。
(AH4)、(AL5)已经用原两条模型和 signed 基将 native 二阶
返回 $J_p'(0)^2$；(AN4)另在整局部双变量类上给出原平移来源
与实际 $c$-平滑 Robert 类的上述准确单位关系。它没有将
R303 另一辅助惰性素数所用的 $\ell^2+\ell^{-1}$ 改写成
$c^2-c$；两处使用各自的理想 Artin 与原平滑规范。
(AM1)的有限层非零在完整 Tate 扭转及反圆取商前成立；
(AN4)的单位比较仍容许两个类在反圆中央同时有高阶零。
