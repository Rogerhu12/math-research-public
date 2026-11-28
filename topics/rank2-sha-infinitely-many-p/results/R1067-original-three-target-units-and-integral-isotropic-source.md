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
