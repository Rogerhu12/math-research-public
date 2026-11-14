# R119 续篇：真实速度 hodograph 与二阶标量相位费用

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在同一个 $\ell^1_{224}$ 全标签精确尾上，
实际 Jacobi principal 可进一步准确变为
$$
 \left[b(t,\xi)I+c(t)
 \begin{pmatrix}0&1\\-A(t)&0\end{pmatrix}\right]\partial_\xi .
 \tag{H.1}
$$
这里 $c(t)$ 是一个真实标量，$b(t,\xi)$ 是被完整保留的共同角漂移；
全部型别零点仍为原来的 $A(t)=0$。没有更换背景度量、双 bump
参数或原标签层。完整 holonomy 使 $c-1$ 从标签的二阶开始，但不
迫使它恒等于0。

这个实际 hodograph 把空间变速分解为可明确量化的标量速度与共同
漂移，不等于已构造全混合尾的圆周 return 共轭。后者仍须处理真实
非自治漂移、转向框架和完整两迹。

## 1. 圆周速度及其准确演化

沿用
[不标量化的一阶尾框架](R119-supplement-unscalarized-tail-frame-and-summable-remainder.md)
的全部符号。特别
$$
 v=\frac{\sqrt D}{J},\quad d=\frac{E(V-P)}J,\quad
 J=1+K+EU,\quad E=1+w^2,
$$
$$
 H=\frac{A(1-v^2)-d^2}{E},\qquad
 \frac{v_t-dv_\theta}{v}+d_\theta=H.
 \tag{H.2}
$$
$v$ 在本文一直表示 principal 倍率，物理高度变化另记为 $\dot z$。
圆周平均按长度 $2\pi$ 归一。

准确定义
$$
 I(t)=\left\langle\frac1v\right\rangle_\theta
     =\left\langle\frac J{\sqrt D}\right\rangle_\theta,
 \qquad c(t)=I(t)^{-1}.
 \tag{H.3}
$$
若先用前篇的真实漂移流 $\phi$、$j=\phi_\eta$、
$\nu=(v\circ\phi)/j$，则准确有
$$
 \left\langle\frac1\nu\right\rangle_\eta
 =\left\langle\frac{j}{v\circ\phi}\right\rangle_\eta
 =\left\langle\frac1v\right\rangle_\theta.
 \tag{H.4}
$$
所以 $c$ 与从哪个切口启动漂移流无关，也是静态角重标下的真实
圆周速度。Jacobian 在 (H.4) 中必须只使用一次。

由 (H.2) 积分分部，
$$
 I_t=-\left\langle\frac{v_t}{v^2}\right\rangle
     =-\left\langle\frac H v\right\rangle
       +\left\langle\left(\frac d v\right)_\theta\right\rangle
     =-\left\langle\frac H v\right\rangle.
$$
故
$$
 \boxed{\quad
 \frac{c_t}{c}=\bar H:=
       \frac{\langle H/v\rangle}{\langle1/v\rangle}.
 \quad}                                                     \tag{H.5}
$$
该式只使用实际一阶系统，不引入 $A_t$。

## 2. 同一完整 mean 给标量速度的二阶门

记 $n$ 为前篇在宽4上的完整四态 norm。实际域内
$n<2^{-447}X_{224}$；下面只需 $n\le1/256$。
R25 的五项非mean norm $\mathcal R$ 满足 $\mathcal R\le2n$，
所以同一 holonomy-one 小根给
$$
 |K_0|\le12\mathcal R^2\le48n^2.
 \tag{H.6}
$$
这里没有对 mean 假设一个非零模的指数因子。

令 $T_0=2K+K^2+EP^2$，$D=1-w^2T_0$。
$\|T_0\|<3n$。使用 $(1-z)^{-1/2}$ 的真实幂级数，在
$\|z\|\le1/16$ 上其二阶余项 norm 不超过 $\|z\|^2$，得
$$
 D^{-1/2}=1+w^2K+R_D,\qquad \|R_D\|\le10n^2.
$$
乘以 $J=1+K+EU$ 后，
$$
 \frac1v=1+E(K+U)+R_I,\qquad \|R_I\|<13n^2.
 \tag{H.7}
$$
因 $\langle U\rangle=0$，(H.6)–(H.7) 给
$$
 |I-1|<109n^2<128n^2,\qquad
 \boxed{\ |c-1|<256n^2\ }.
 \tag{H.8}
$$
特别原点处的全部非mean 标签一阶微分满足 $Dc(0)=0$。
这是完整 mean 方程产生的抵消，不是把 $\nu-1$ 的一阶空间变化删掉。

还可支付时间导数的二阶界。由 (H.7) 的逆级数，
$$
 v=1-E(K+U)+R_v,\qquad \|R_v\|<31n^2.
$$
故
$$
 \frac H v=\frac A E(1/v-v)-\frac{d^2}{Ev}
          =2A(K+U)+R_H,
 \qquad \|R_H\|\le44|A|n^2+18n^2.
$$
连同 (H.6)、$I^{-1}<2$，得到
$$
 \boxed{\quad |\bar H|\le512(1+|A|)n^2. \quad}
 \tag{H.9}
$$
非平均的 $H$ 仍只有一阶界
$\|H\|\le14(1+|A|)n$；后面不会把它误写成二阶。

## 3. 真正可逆的空间 hodograph

令 $\partial_\theta^{-1}$ 表示在全部非零 $4\mathbb Z$ 模上的完整
角原函数，mean 取0。定义
$$
 \chi(t,\theta)=\theta+
   \partial_\theta^{-1}\left(\frac c v-1\right),\qquad
 \xi=\chi(t,\theta),\qquad \theta=\Theta(t,\xi).
 \tag{H.10}
$$
因为 $\langle c/v\rangle=1$，右端的原函数确实周期。
它保持原四重周期；对实际反射相容的数据，它也是同一反射规范下
的奇映射，没有额外选择径向旋转。

从 (H.7)–(H.8) 可取
$$
 \|c/v-1\|_{\mathcal A_3}<7n,\qquad
 \|\chi-\mathrm{id}\|_{\mathcal A_3}<2n.
 \tag{H.11}
$$
后式使用 $\|\partial_\theta^{-1}\|\le1/4$，没有截掉高模。
在宽2上解逆方程
$\Theta=\xi-(\chi-\mathrm{id})(t,\Theta)$；
其 Lipschitz 常数小于 $7n<1/2$，所以得到真正的全纯逆，
$$
 \|\Theta-\mathrm{id}\|_{\mathcal A_2}<4n,\qquad
 j_\chi:=\Theta_\xi=(v/c)\circ\Theta,\qquad
 \|j_\chi-1\|_{\mathcal A_2}<16n .
 \tag{H.12}
$$
实标签下 $j_\chi>0$，故为真实圆周微分同胚。平尾极限处
$n\to0$，因此该图和逆准确趋于恒等。

这项角变换与原点的同宽 operator norm 差不要求小；所有解、source
和两迹均使用 (H.10) 的真正 pullback。

## 4. 准确的新共同漂移及完整一阶系统

在未作漂移流之前，前篇的 $Z=\mathsf T^{-1}(\dot P,\dot K)^T$ 满足
$$
 Z_t=(dI+v\mathsf B_0)Z_\theta+
             (\mathsf C_0+\mathsf R_0)Z+\begin{pmatrix}0\\e/v\end{pmatrix},
$$
$$
 \mathsf B_0=\begin{pmatrix}0&1\\-A&0\end{pmatrix},\quad
 \mathsf C_0=\operatorname{diag}(-A-1,-2A),\quad
 \|\mathsf R_0\|_{\mathcal A_3}\le512(1+|A|)n.
$$
置 $Y=Z\circ\Theta$。准确链式法则得到
$$
 \boxed{\quad
 Y_t=(bI+c\mathsf B_0)Y_\xi+
      (\mathsf C_0+\mathsf R_0\circ\Theta)Y+
      \begin{pmatrix}0\\(e/v)\circ\Theta\end{pmatrix},
 \quad}                                                     \tag{H.13}
$$
其中
$$
 b\circ\chi=\frac{cd}{v}-\chi_t .
 \tag{H.14}
$$
由于 $\chi_\theta=c/v$，对 (H.14) 作角导，并使用 (H.2)、(H.5)，
准确得到
$$
 \boxed{\qquad
 b_\xi=(H-\bar H)\circ\Theta .
 \qquad}                                                    \tag{H.15}
$$
特别本 hodograph 没有让主部完全径向；非恒定的 $H$ 保留在共同
漂移中。

可不微分任何径向系数而直接写出完整 $b$：
$$
 b\circ\chi=
 \partial_\theta^{-1}\left[\frac c v(H-\bar H)\right]
       +\left\langle\frac{cd}{v}\right\rangle_\theta .
 \tag{H.16}
$$
方括号的 mean 因 (H.5) 准确为0。公式中的常数项来自
$\langle\chi_t\rangle_\theta=0$，不能对一般复标签删掉。

$d/v=E(V-P)/\sqrt D$，而 $\langle V-P\rangle=0$，故
$$
 \left|\left\langle\frac{cd}{v}\right\rangle\right|\le12n^2.
$$
由 (H.9)、$n\le1/256$，
$\|H-\bar H\|\le16(1+|A|)n$。
(H.16) 因此给
$$
 \|b\|_{\mathcal A_2}\le32(1+|A|)n,\qquad
 \|b_\xi\|_{\mathcal A_2}\le16(1+|A|)n .
 \tag{H.17}
$$

还须区分两个角变量中的 mean。若 $b_0=\langle b\rangle_\xi$，则
$$
 b_0=\left\langle\frac c v(b\circ\chi)\right\rangle_\theta.
$$
用 (H.11)、(H.16) 的 mean-zero 原函数部分，得到
$$
 |b_0|\le12n^2+7n\cdot16(1+|A|)n
        <128(1+|A|)n^2.
 \tag{H.18}
$$
对原物理反射相容子空间，$d$ 为奇、$v,H$ 为偶，
$\chi-\theta$ 为奇，因此 $b$ 为奇并且 $b_0=0$ 准确成立。
这条对称性不消去 $b$ 的所有非零模。

## 5. 整条实际尾的二阶标量相位预算

前篇已经对真实所有胞元及全部有限段证明
$$
 n_{\max}<2^{-447}X_{224},\qquad
 I_*:=\int(1+|A|)n\,dt<2^{-435}X_{224}.
 \tag{H.19}
$$
所以本篇全部新费用均可以直接支付：
$$
\begin{aligned}
 \sup_t|c-1|&<2^{-886}X_{224}^2,\\
 \int\left|\frac{c_t}{c}\right|dt
     &<2^{-873}X_{224}^2,\\
 \int\sqrt{|A|}\,|c-1|\,dt
     &<2^{-874}X_{224}^2,\\
 \int|b_0|\,dt&<2^{-875}X_{224}^2,\\
 \int(\|b\|_{\mathcal A_2}+\|b_\xi\|_{\mathcal A_2})dt
     &<2^{-429}X_{224}.
\end{aligned}
 \tag{H.20}
$$
第三行使用 $\sqrt{|A|}\le1+|A|$，包含所有正、负及过渡层。
完整零阶余项仍满足前篇的
$\int\|\mathsf R_0\circ\Theta\|_{\mathcal A_2}dt<2^{-426}X_{224}$。

这些是准确 scalar 光学费用及共同漂移预算。即使反射使 $b_0=0$，
非自治的非恒定 $b$ 与两个分支的平移仍不必交换；不能由这些数
直接将全 return 的旋转数或谱相位等同于原径向值。

## 6. 全部两迹、source 与 mean 的相同图变换

普通 scalar Darboux source 准确变成
$(0,(e/v)\circ\Theta)^T$，宽3到宽2的 norm 至多2。
从 (H.13) 恢复原两个相对迹的公式为
$$
 \dot P\circ\Theta=Y_1,\qquad
 \dot K\circ\Theta=(d\circ\Theta)Y_1+(v\circ\Theta)Y_2.
 \tag{H.21}
$$
完整高度和 mean 行因此仍为
$$
 \langle j_\chi Y_1\rangle=0,\qquad
 \dot K_0=\left\langle j_\chi
          [(d\circ\Theta)Y_1+(v\circ\Theta)Y_2]\right\rangle,
$$
$$
 (\dot z)_\theta=aw\dot P,\qquad
 \partial_t(\dot z)_0=aw\dot K_0 ,
 \tag{H.22}
$$
并保留一个独立内端平均高度 $\dot\lambda$。
Holonomy 有源行是
$$
 (\dot M)_t=w^2\left\langle
                     j_\chi(\rho J e)\circ\Theta\right\rangle.
 \tag{H.23}
$$
没有把此行换成 $e_0$ 或 $Y$ 的未加权零模。

若用已重建的真实 grounded 高度 $f$、conormal 密度 $p$ 和对应
ordinary 密度源 $s$，则正确变换是
$$
 \widehat f=f\circ\Theta,\qquad
 \widehat p=j_\chi(p\circ\Theta),\qquad
 \widehat s=j_\chi(s\circ\Theta).
 \tag{H.24}
$$
它保留 $\int fp$、$\int p$、$\int s$，而物理高度 mean 是
$\int j_\chi\widehat f$。normal/shear 与水平重建仍使用原真公式，
不能把 (H.21) 的第二分量误称为 grounded 通量。
这些输出继续覆盖物理 $1/512$ 角窗。

## 7. 真完整尾第四模确实改变 cut128 的标量速度

下面使用实际 R115 全无限尾图中的方向，不只检验任意局部 Cauchy
数据。先对任意通过原点的真实全纯标签曲线写
$$
 P=\varepsilon P_1+O(\varepsilon^2),\quad
 K=\varepsilon K_1+\varepsilon^2K_2+O(\varepsilon^3),\quad
 U=\varepsilon U_1+O(\varepsilon^2),\qquad s=w^2.
$$
所有 $P,U$ 的 mean 准确为0；同一 holonomy 小根还给
$\langle K_1\rangle=0$。完整
$$
 M=\left\langle
 \left(1+\frac{s(1+K)U}{1-sP^2}\right)
       [1-s(2K+K^2+(1+s)P^2)]^{-1/2}
 \right\rangle=1
$$
的二阶项准确是
$$
 \langle K_2\rangle
 =-E\langle K_1U_1\rangle
  -\frac{1+3s}{2}\langle K_1^2\rangle
  -\frac E2\langle P_1^2\rangle .
 \tag{H.25}
$$
再对 $I=\langle J/\sqrt D\rangle$ 展开，代入 (H.25)，得到
$$
 \boxed{\quad
 c=1+\frac E2
     \langle K_1^2+2K_1U_1+P_1^2\rangle\varepsilon^2
       +O(\varepsilon^3).
 \quad}                                                     \tag{H.26}
$$
该式包括完整 mean 的二阶反馈。非mean 的二阶生成模不贡献此
平均的一次项，但没有在实际解中将它们删除。

现在取原内部第四模标签的真实实余弦方向，其余标签保持为0。
[R11 §2](R11-matched-mode-four-physical-tail-connector.md) 对同一
真实无限尾已证明第四模 cut128 高度非零，并且
$$
 d_*=\frac{b\bar C_r(b)}{\bar C(b)}\in(14,15).
 \tag{H.27}
$$
这里 $\bar C$ 是真齐次解，不是理想单胞或有限截尾的方向。
因此可以用一个非零常数重标这条标签曲线，使 cut128 的相对 raw
高度一阶项为 $\varepsilon\cos4\theta$。对充分小的
$\varepsilon$，它仍在同一 $\ell^1_{224}$ 球内；没有改用另一条
允许线或另指定非线性径向迹。该真方向给
$$
 P_1=-4\sin4\theta,\qquad U_1=-16\cos4\theta,\qquad
 K_1=d_*\cos4\theta .
 \tag{H.28}
$$
物理缩放和北向高度的共同符号不改变这个比值。

代入 (H.26)，在真 cut128 得到
$$
 \boxed{\quad
 c=1+\frac E4(d_*^2-32d_*+16)\varepsilon^2
      +O(\varepsilon^3),\qquad
 -\frac{239E}{4}<[\varepsilon^2]c<-59E .
 \quad}                                                     \tag{H.29}
$$
因为该二次多项式在 $14<d_*<15$ 上严格位于 $(-239,-236)$。
所以实际完整尾 chart 的这个 principal 圆周速度并不恒为原点的1，
且在这条真实小曲线的充分小非零点有 $c<1$。

这排除了“由完整 holonomy 和无限尾允许条件，便可把每个真实截面
无反项地角共轭成原径向 principal”这一捷径。
它仍不是对某个尚未构造的全混合 return 旋转数的计算：
不同径向段的漂移、转向及相位可以相互作用，必须用完整传播证明。
本篇没有据此把最终相位修调或课题主目标判为不可能。

## 8. 当前已经具体化的下一步

需要保留的实际 principal 特征值是 (H.13) 的
$b(t,\xi)\pm c(t)\sqrt{-A(t)}$；相应特征线满足
$\xi_t=-b\mp c\sqrt{-A}$。在正型段它们成为对应的复 principal
分支。主速度的标量改变已是明确二阶费用，共同漂移有明确一阶费用。
完整相位共轭或参数修调现在必须作用在这些真系数上，并把所有转向
点、source、两迹和 mean 一起带回。

如果后续选择改变 profile/bump 参数来修调相位，那将是构造一个新的
最终固定度量的步骤，不能在已经声明固定 $g_0$ 的一次 Newton 中
悄悄代换。本篇没有执行这种参数选择。

[准确代数与预算程序](../scripts/fourfold_actual_speed_hodograph_20261113.py)
及 [报告](../notes/2026-11-13-R119-actual-speed-hodograph-budget.json)
核验 mean 二次门、全尾指数、完整 hodograph 主部及真第四模标签
方向的二阶系数。无限层量词由正文的真实求和承担。
