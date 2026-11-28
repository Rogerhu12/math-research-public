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
