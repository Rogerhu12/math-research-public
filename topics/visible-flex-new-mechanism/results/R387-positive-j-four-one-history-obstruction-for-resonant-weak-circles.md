# R387：完整一层的 j⁴ 正余量排除当前共振弱圆

日期：2026-11-15。**完整原式与有限纸面证明；未执行符号程序、profile 求积、几何扫描、人工测试或研究运行。**

[R383](R383-genuine-low-order-profile-fibers-pay-the-final-Gaussian-angular-quotient.md)
已在同一个真实弱单 hook 圆上支付全部18个 Gaussian 面积、十个对称 Gaussian 乘积的完整外矩、原三条 directed 条件及 $\Psi=0$。这些是确切的二history及已指定一层条件，不等于全部一history已零。

本稿回到原完整一层，抽出一个此前没有被置零的准确系数：
$$
[\sigma h^{-2}j^4]\mathscr R_{-3,\theta}.
$$
它没有来自局部恢复的同次项。保留原 elementary history 后，已付条件把它准确化为
$$
\boxed{
[\sigma h^{-2}j^4]\mathscr R_{-3,\theta}
=
\frac{11\kappa^4(41t^2+27)K(t)}
{10368h_e^3P(t)(51t^2+2t+8)}
\int(f''{}^2-\phi_\theta''{}^2)^2,
}
\tag{1}
$$
其中 $t=\kappa^2$，$K$ 的全部系数严格正。因而当前非退化弱圆的完整一history仍不为零，不能完成这个共振端芽的第四 ruling。

本结论不要求逐包比例、导数 rank-one 或第二个 hook；一般重叠和弱单 hook 的交叉项已经通过 R325 的完整 mixed 身份保留。它不排除不同端芽、不同第三算子或非圆首阶轨道，更不构成主课题的一般刚性结论。

## 1. 同一点的已付范围与原规范

固定 R354 初始安装的合法物理窗口和共振端芽
$$
h=h_e e^{\varepsilon\sigma^2},\qquad
k=\kappa(1-2\varepsilon\sigma^2),\qquad
\omega=\kappa/h,\qquad
\varepsilon=\kappa^2/4,\qquad 0<t=\kappa^2<1/100.
\tag{2}
$$
记
$$
j=2\varepsilon\kappa\sigma^2,\quad
\gamma=h_\sigma=2\varepsilon\sigma h,\quad
\delta=j_\sigma=4\varepsilon\kappa\sigma,\quad
\mathcal Q=1+(hx+j)^2.
$$
整个物理区间保持 $x+\omega>0$；它可以包含负 x。下面的原恢复、矩与分部积分没有除以 x，不把 R354 的全反射块移回一个未经授权的正区间。

固定同一真实 $C^\infty$ 三矩圆
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta,
$$
$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad
\mathbf I(f,g)=0.
\tag{3}
$$
使用同一个右锚 $Jv(x)=\int_x^{r_*}v$，外矩为
$$
I_0(u,v)=\int u''v'',\qquad
I_1(u,v)=\int xu''v'',\qquad
I_2(u,v)=\int(x^2u''v''+2u'v').
\tag{4}
$$
特别 $XD_\theta$ 对每个 $X\in E_8$ 都真紧；不把单独 $X(f,f)$ 或单微包的左尾置零。

沿 R325 记
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},\ Y=\Phi_{p_2},
$$
$$
W=aR+bS,\qquad Z=d_ZL+e_ZU,
$$
$$
\begin{aligned}
a&=-\frac{51t^2+2t+8}{64h_e^2},&
b&=-\frac{17t^2+4t}{32h_e^2},\\
d_Z&=\frac{6\kappa^3}{h_e},&
e_Z&=-\frac{\kappa(15t+1)}{4h_e},&
B_{-3}&=c_PP,\quad
c_P=-\frac{\kappa(41t^2+27)}{216h_e^3}.
\end{aligned}
\tag{5}
$$
原 directed 全函数为
$$
H_m^X(\theta)
=-I_m(XD_\theta,PD_\theta)
+2I_m\{\phi_\theta,X(\phi_\theta,PD_\theta)\}.
\tag{6}
$$

本文实际使用的已付条件是：

- 原弱单 hook $\mathfrak H(g;f,f)=0$，故 $\mathfrak H(\phi_\theta;D_\theta)=0$；
- 原 $WP$ 面积 $I_m\{\phi_\theta,[W,P](\phi_\theta;D_\theta)\}=0$，$m=0,1,2$；
- 三条完整 directed 条件
$$
F_0=H_2^P=0,\qquad
F_1=aH_1^R+bH_1^S=0,\qquad
F_2=d_ZH_0^L+e_ZH_0^U=0;
\tag{7}
$$
- R325 的完整兼容量 $\Psi_\theta=0$。

R383 的同一点具有全部这些条件，并另有全部18面积与十个完整对称乘积。后一组不会在本稿被假称为全部一层。由对称乘积加相应面积，也可直接得到(7)中的完整 directed 量为零；不能只使用它们的 principal。

几何方面仅使用原安装的 $M=0$、$T=\kappa_H\mathfrak H$ 与共振端芽。没有继承另一个旧几何的 universal wholeE、Morse、完整第四 period 或某个已解 gauge。

## 2. 原完整一层与真实函数分离

[R296](R296-complete-zero-one-Gaussian-layers-and-the-full-principal-square.md)
把整个中心化第四 ruling 写成零层、四个一层以及对称/反对称二层。
令
$$
\mathsf m(\sigma)=\mathsf Q(\sigma)+
\sum_{\rho\in\{1,-1,-2,-3\}}E_\rho(\sigma)B_\rho,\qquad
E_\rho=\int_0^\sigma e^{\rho\varepsilon s^2}\,ds .
\tag{8}
$$
$\mathsf Q$ 是真实 elementary history；它不是几何 $\mathcal Q$。原真初值保留，不能在子段中重锚。

设 $\mathcal T_\sigma$ 为 R221 的完整局部配对，且
$$
\mathcal E_\sigma
=\frac{1+j^2}{4h}I_0+\frac j2 I_1+\frac h4 I_2.
\tag{9}
$$
原一层准确为
$$
\begin{aligned}
\mathscr R_{\rho,\theta}={}&
2\mathcal T_\sigma(B_\rho D_\theta;D_\theta)
-4\mathcal T_\sigma(\phi_\theta;\phi_\theta,B_\rho D_\theta)\\
&-2\mathcal E_\sigma(\mathsf QD_\theta,B_\rho D_\theta)
+4\mathcal E_\sigma\{\phi_\theta,\mathsf Q(\phi_\theta,B_\rho D_\theta)\}.
\end{aligned}
\tag{10}
$$
全部链式项和真实第三局部恢复在 R296 的完整拆分中保留；它们没有被重新分配为某个可忽略的传入常数。

对 $B_{-3}=c_PP$，(10)除以 $c_P$ 后为
$$
\frac{\mathscr R_{-3,\theta}}{c_P}
=
\mathscr L^P_\theta+
2\sum_{X\in E_8}\sum_{m=0}^2q_X(\sigma)w_m(\sigma)H_m^X(\theta),
\tag{11}
$$
其中 $\mathsf Q=\sum q_XX$、$w_m$ 是(9)的三个原权，且
$$
\mathscr L^P_\theta
=2\mathcal T_\sigma(PD_\theta;D_\theta)
-4\mathcal T_\sigma(\phi_\theta;\phi_\theta,PD_\theta).
$$
这正是 R300 的 directed 原式，不把 outer/inner 次序互换。

R300 的准确有限呈示为
$$
\mathscr R_{\rho,\theta}
=\sigma\sum_{n=-4}^{2}h^nP_{\rho,n,\theta}(j).
\tag{12}
$$
本稿中的 $[\sigma h^{-2}j^4]$ 指这个真实呈示的系数，不是只取一个低 Taylor jet。
因为 $h/h_e=e^{\varepsilon\sigma^2}$ 超越于 $\mathbb R(\sigma)$，
同一层内不同 $j$ 次数及不同 Laurent 指数准确独立。
R249 的 Gaussian 词独立性进一步把四个 $E_\rho$ 与零层、两重词分开。

因此完整一层为零必须使(1)为零；不能由另一个未算的 $\sigma$ 阶或其他 Gaussian 原函数抵消。

## 3. 直接从 R73 取得所需的三个最高系数

为避免只凭 principal 表识别完整算子，本节直接使用 R73 的原八矩坐标。

在(2)上有 $k=\kappa-j$，瞬时 $L,U,R,S$ 密度准确为
$$
\begin{aligned}
M_L&=\frac1h\left(
-\frac\kappa2+\frac j2-\frac{\kappa j^2}2+\frac{j^3}2
\right),\\
M_U&=-\frac{j+j^3}{4h},\\
M_R&=\frac1{8h^2}\left[
-j^4+\frac{\kappa j^3}2-(t+2)j^2+\frac{\kappa j}2+t-1
\right],\\
M_S&=\frac1{4h^2}\left[
-\kappa j^3+t j^2-\kappa(1+2t)j
\right].
\end{aligned}
\tag{13}
$$
例如 $M_R$ 直接由 R73 的 $B_0$ 一次 x 系数得到：
$$
8h^2M_R
=(1+j^2)(t-j^2-1)
+\frac{\kappa j}{2}(1+j^2)-2tj^2.
$$
这里使用真实 $\gamma^2/h^2=\kappa j/2$、$\gamma\delta/h=tj$；没有删任何速度项。

对非零整数 n，若
$$
\int_0^\sigma h^nP(j)\,ds
=\sigma h^nQ(j)+h_e^n bE_n,
$$
则真实微分给
$$
P=(1+nj/\kappa)Q+2jQ'+b.
\tag{14}
$$
右端 $Q'$ 是对 j 的导数。$bE_n$ 是原 Gaussian 常数尾，仍在(8)中；不是把它丢掉后重新积分。

把(13)代(14)，得到
$$
\begin{aligned}
q_L&=\sigma h^{-1}\ell(j),&
\ell(j)&=-\frac{\kappa j^2}2-2\kappa^2j-\frac\kappa2-6\kappa^3,\\
q_U&=\sigma h^{-1}u(j),&
u(j)&=\frac{\kappa j^2}4+\frac{5\kappa^2j}4
+\frac{\kappa(15t+1)}4,\\
q_R&=\sigma h^{-2}r(j),&
r(j)&=\frac{\kappa j^3}{16}
+\frac{3\kappa^2j^2}{16}
+\frac{\kappa(17t+4)j}{32}
+\frac{\kappa^2(51t+10)}{64},\\
q_S&=\sigma h^{-2}s(j),&
s(j)&=\frac{\kappa^2j^2}{8}
+\frac{3\kappa^3j}{16}
+\frac{\kappa^2(17t+4)}{32}.
\end{aligned}
\tag{15}
$$
这些是完整 $\mathsf Q$ 的坐标。若从 R300 的 $\alpha_{\mathsf Q}+2\beta$ 表复核，必须减去完整 $2\beta$，不能把该表直接当作 $\mathsf Q$。

其余四个方向的 h 层为：$P$ 在 $h^{-3}$、$\Phi_{p_1}$ 和 $\Phi_{t_1}$ 在 $h^0$、$Y$ 在 $h^1$。其中 $P$ 的 elementary j 次数至多3。

所以(11)在 $\sigma h^{-2}j^4$ 处，history 只有
$$
\frac{1+j^2}{2}\{\ell(j)H_0^L+u(j)H_0^U\}
+j\{r(j)H_1^R+s(j)H_1^S\}
$$
的指定系数。$P$ 对 $I_2$ 的项至多 j³，另四个 h 层都不能在这里添项。故
$$
\left[\sigma h^{-2}j^4\right]
\frac{\mathscr R_{-3,\theta}-c_P\mathscr L^P_\theta}{c_P}
=
\frac{\kappa}{16}
\{-4H_0^L+2H_0^U+H_1^R\}.
\tag{16}
$$

## 4. 局部恢复在这个系数上准确没有贡献

R221(17)保全右锚 Fubini 和 compact 外槽端项，给
$$
\begin{aligned}
\mathcal T_\sigma(c;a,b)=\frac1{32h^4}\int\Big[
&\mathcal Q^2c'''\{\gamma(a'b''+a''b')-(\gamma x+\delta)a''b''\}\\
&-2h\gamma(hx+j)\mathcal Qc'''a'b'\\
&+F_c\{(\gamma\mathcal Q-2h(hx+j)(\gamma x+\delta))a''b''
-2h^2\gamma a'b'\}\Big],
\end{aligned}
$$
$$
F_c=\mathcal Qc''-2h(hx+j)c'+2h^2c.
\tag{17}
$$
本稿代入的 $c=PD_\theta$ 或 $\phi_\theta$ 都真紧，所以用的是完整物理 $\mathcal T$，没有把非紧 micro self 直接套入 compact 公式。

(17)的全部几何生成元只有
$$
\gamma h^{i-4}j^m,\qquad
\delta h^{i-4}j^m,\qquad i+m\in\{0,2,4\}.
\tag{18}
$$
在共振端芽代入 $\gamma=2\varepsilon\sigma h$、$\delta=4\varepsilon\kappa\sigma$ 后：

- $\gamma$ 项若有 $\sigma h^{-2}$，必须 $i=1$，于是 $m=1$ 或3；
- $\delta$ 项若有 $\sigma h^{-2}$，必须 $i=2$，于是 $m=0$ 或2。

因此
$$
[\sigma h^{-2}j^4]\mathscr L^P_\theta=0.
\tag{19}
$$
这不使用 profile 偶性。真实完整结论是
$$
\boxed{
[\sigma h^{-2}j^4]\mathscr R_{-3,\theta}
=\frac{c_P\kappa}{16}
\{-4H_0^L+2H_0^U+H_1^R\}.
}
\tag{20}
$$
它不是只证明局部 principal 消失，也没有遗漏可能具有相同主符号的低阶项。

## 5. 只用已付的完整 mixed 身份消元

以下全在同一个相位上，暂写 $\phi=\phi_\theta$。令
$$
p=f',\quad q=f'',\quad v=\phi',\quad r=\phi'',\quad
d_0=q^2-r^2,
$$
$$
D_4=\int d_0^2,\qquad C=\int r^2d_0,\qquad
\mathcal J=\int(vq-pr)\,r q'.
\tag{21}
$$
这里 $D_4$ 是一个实际非负积分，不是形式二次槽 $D_\theta$。

R325(8)–(12)由原弱 hook、原 $WP$ 三面积和全尾 IBP 给
$$
H_1^S=\frac52D_4+\frac{14}3C+8\mathcal J
\tag{22}
$$
以及在 $F_0=F_1=0$ 时
$$
H_0^U=
\left(\frac23-\frac{5b}{2a}\right)D_4
+\frac{14}3\left(1-\frac ba\right)C
+8\left(1-\frac ba\right)\mathcal J .
\tag{23}
$$
这些是一般 mixed 身份，未施逐包比例或第二 hook。其原推导先保
$\int d_0'P(f,f)=\int d_0q^2$，所以没有假设 $P(f,f)$ 左紧。

所用 $\Psi$ 的准确定义为
$$
\Psi=
\frac{N(t)}{24P(t)}D_4+\mathcal J+\frac7{12}C,
$$
$$
\begin{aligned}
N(t)&=16+184t-1713t^2-2475t^3-4590t^4,\\
P(t)&=8+114t-169t^2+231t^3-612t^4.
\end{aligned}
\tag{24}
$$
在 $0<t<1/100$，$P(t)>0$。

令
$$
\rho=\frac ba=\frac{2t(17t+4)}{51t^2+2t+8},\qquad
R_*=\frac{N(t)}{3P(t)}.
$$
$\Psi=0$ 准确给
$$
\frac{14}3C+8\mathcal J=-R_*D_4.
$$
因此
$$
\boxed{
H_1^S=(5/2-R_*)D_4,\qquad
H_0^U=\{2/3-R_*-\rho(5/2-R_*)\}D_4 .
}
\tag{25}
$$
另由完整 $F_1=F_2=0$，
$$
H_1^R=-\rho H_1^S,\qquad
H_0^L=-\frac{e_Z}{d_Z}H_0^U,\qquad
\frac{e_Z}{d_Z}=-\frac{15t+1}{24t}.
\tag{26}
$$

把(25)–(26)代入(20)，先保 $c_P$，得
$$
\frac{1}{c_P}[\sigma h^{-2}j^4]\mathscr R_{-3,\theta}
=
-\frac{(3t+1)H_0^U+6t\rho H_1^S}{96\kappa}.
\tag{27}
$$
没有把三条 directed 与 $\Psi$ 看成可分别改变的不同最终圆。

## 6. 完整系数的严格符号

置
$$
D_*(t)=51t^2+2t+8,
$$
$$
A_*(t)=16-8t+39t^2+1071t^3,\qquad
B_*(t)=8+18t+47t^2+255t^3 .
$$
由(25)，
$$
\frac{(3t+1)H_0^U+6t\rho H_1^S}{D_4}
=
(3t+1)(2/3-R_*)+\rho(3t-1)(5/2-R_*)
$$
$$
=\frac{A_*(t)P(t)-B_*(t)N(t)}{3P(t)D_*(t)}.
\tag{28}
$$
当 $D_4=0$ 时，这里应读为两边乘 $D_4$ 后的多项式身份，不作除零操作。

准确分子为
$$
\begin{aligned}
A_*P-B_*N={}&
6336t^2+55968t^3+218724t^4\\
&+468666t^5+1070388t^6+514998t^7\\
={}&66t^2K(t),
\end{aligned}
$$
$$
\boxed{
K(t)=96+848t+3314t^2+7101t^3+16218t^4+7803t^5>0.
}
\tag{29}
$$
这些是显示原多项式的普通有限乘法恒等，没有求积、拟合或数值符号判断。

由(27)–(29)，
$$
\frac{1}{c_P}[\sigma h^{-2}j^4]\mathscr R_{-3,\theta}
=-\frac{11\kappa^3K(t)}{48P(t)D_*(t)}D_4.
$$
乘回原(5)的 $c_P$，正好得到(1)。完整系数对两种非零 $\kappa$ 符号都是正倍数；不存在通过换 $\kappa$ 正负改变结论的余地。

## 7. 对当前弱圆的严格结果与更一般的条件推论

R383 同点仍具有原
$$
\int(f''+ig'')^4=0.
\tag{30}
$$
这是原面积及构造所保持的完整四次条件，不是本稿新增自由设定。
记 $C_{22}=\int f''{}^2g''{}^2$。对非零圆，由(30)
$$
C_{22}>0,\qquad
D_4(\pi/2)=4C_{22}>0.
\tag{31}
$$
否则 $C_{22}=0$ 与(30)实部一起迫 $\int f''{}^4+\int g''{}^4=0$，紧性使两者都为零。

所以当前同一点有
$$
\boxed{
[\sigma h^{-2}j^4]\mathscr R_{-3,\pi/2}
=
\frac{11\kappa^4(41t^2+27)K(t)}
{2592h_e^3P(t)D_*(t)}C_{22}>0 .
}
\tag{32}
$$
其完整一层无法归零，当前共振端芽的第四 ruling 因而不能完成。

还有一个不依赖(30)的条件推论：若某个真实圆对所有相位满足第1节所列完整条件，且要求整个一层为零，则(1)迫每个相位 $D_4(\theta)=0$。取 $\theta=\pi/2$ 得
$g''{}^2=f''{}^2$；再取 $\theta=\pi/4$ 得
$(f''+g'')^2/2=f''{}^2$，因而 $f''g''=0$。两式合起来迫 $f''=g''=0$，紧性又迫 $f=g=0$。

所以本稿的阻碍不只是某个偶母、特定 offset、格点编码或有限补偿块的失败。只要同一个共振端芽上仍保上述原三矩、弱单 hook、$WP$ 面积、三 directed 与 $\Psi$，非退化圆就不能再把整个一层置零。这个推论的条件须逐项保留，不把它扩大到任意第三算子或任意首阶轨道。

## 8. 原 gauge、传入历史及既有结果不被混淆

[R243](R243-finite-jet-criterion-for-the-complete-even-exceptional-ruling.md)
的完整中心比较保留实际全路径传入的二、三阶 history及二阶初值平方项。它们连同合法二阶 gauge 的偶部响应，只改变
$$
\mathcal W_e=\operatorname{span}\{h,\sigma^2,(1+j^2)/h\}.
\tag{33}
$$
其证明用的是 $\sigma$ 奇偶、完整 R56 恢复和真实三矩；这里所有 x 表达都无除 x，R354 负支撑部分在 $x+\omega>0$ 的共同窗口内同样合法。

R249 的真实原函数字独立性使(32)不可能被(33)、零层、其他一层或未重置的负 Gaussian 常数尾吸收。本稿因此使用的是完整必要门，不是将中心模型冒作实际全路径或只排零 gauge。

本稿不撤销 R354–383 已完成的有限构造：原三矩、完整第三、18面积、十个对称 Gaussian 乘积、三 directed 和 $\Psi$ 在同一个实际圆上仍可同时为零。本稿证明的是，在这个共振端芽中，这些零条件之外另有(32)的严格正剩余。末高频、更多同一纤维方向、正幅完整块、同规范 gauge或继续增加观察数，都不能在保上述完整假设时改变这个必要余量。

实际 canonical 第四 period、平台、退化点与共同 gauge 的其他 joint 条件仍未支付；本稿没有尝试用它们抵消一个已经非零的 ruling 原函数字系数。也没有继承旧几何的 wholeE/Morse 或宣称固定 g 的有限 flex。

继续构造必须改变本稿至少一个实质假设，例如从起点采用不同合法端芽，或重新设计第三算子/首阶轨道。已有另一有理端芽线及实际成本控制结果各保其范围；不能把本稿的阻碍搬到那里，也不能把那里的已付条件免费搬回当前共振圆。
