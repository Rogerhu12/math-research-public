# R291：正 Gaussian 平方的第二外矩准确等于已付领先能量

日期：2026-11-15。**完整纸面恒等式；未执行求积、符号计算程序、人工检查或研究计算。**

[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md) 的 principal 分解中，$E_1^2$ 的第二外矩与 $L_c$ 有相同的三阶导主项。本稿保留全部原函数、完整外槽、真实左尾和低阶项，证明这其实是一条**完整原式身份**，没有剩余的 $C^2$ 兼容门：

$$
\boxed{
Q_{1,1,2}(\theta)
=16\zeta^2\{\sin^2\theta\,L_c+\sin(2\theta)\,L_s\}.
}
\tag{1}
$$

这里 $Q_{1,1,2}$ 是 [R282](R282-symmetric-Gaussian-products-and-an-independent-square-history-gate.md) 的完整 $E_1^2$ 系数中，用 $I_2$ 取代外能量后的原规范；$\zeta=-\kappa h_e\ne0$。因此已付 $L_c=L_s=0$ 准确支付这一整个角函数。结论仅针对这个第二外矩，不把 $E_1^2$ 的另两个外矩或其他对称乘积一起删除。

来源另为 [R229 的同锚能量身份](R229-p2-energy-boundary-identity-for-exceptional-germs.md)、[R231 完整领先相位](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)、[R238 原能量规范](R238-scalar-reduction-of-the-next-two-energies-for-complete-blocks.md)和 [R259 原二次算子与尾](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)。

## 1. 原规范与真正紧的内槽

在原正物理区间 $I=[\ell,r_*]$ 上使用同一个正右积分

$$
Jv(x)=\int_x^{r_*}v(t)\,dt,\qquad (Jv)'=-v.
$$

记

$$
Y=\Phi_{p_2},\qquad \mathcal G=-Y/2,
\qquad
I_2(u,v)=\int_I(x^2u''v''+2u'v'),
\qquad E(u,v)=I_2(u,v)/4.
\tag{2}
$$

这是 R238(1) 的准确规范，不是通过 principal 拟合定义的新算子。原 $Y$ 对角式是

$$
Y(u,u)
=-xu^2+x^2uu'-\frac{x^3}{2}(u')^2
-\frac{x^2}{4}J\{x^2(u'')^2+2(u')^2\}.
\tag{3}
$$

对一个实紧微包，(3) 的左尾一般是 $-x^2I_2(u,u)/4$，不能把它设成零。

取真正三矩圆

$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta,
\tag{4}
$$

且

$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad
\mathbf I(f,g)=0.
\tag{5}
$$

$\odot$ 是原对称二次槽。由(5)，$D_\theta$ 的三个原矩全部为零，特别是 $I_2(D_\theta)=0$。因此

$$
w_\theta=YD_\theta
\tag{6}
$$

在两侧 collar **真正为零**：右侧由原锚给零，左侧由(3)的实际二次尾及 $I_2(D_\theta)=0$ 给零。所需导数也在 collar 全零。

这个紧性属于完整 $D_\theta$。没有声称每个单包 $Y(u_i,u_i)$ 紧，也没有把 outer 的 $Y(\phi_\theta,\phi_\theta)$ 左尾删除。

## 2. 对任意紧输入的准确 cubic 恒等式

R229/R231 已付，对任意紧 $u$，

$$
E\{u,\mathcal G(u,u)\}=0.
\tag{7}
$$

给出只保原边界的短核对。写 $u=xA$、$R=A''$。原同锚式给

$$
\left(\frac{\mathcal G(u,u)}x\right)''
=-\frac{x^4R(3R+xR')}{4}.
$$

R229 的能量分部积分中，外槽 $u$ 紧，故完整边项为零，即使 $\mathcal G(u,u)$ 有左二次尾，仍有

$$
E\{u,\mathcal G(u,u)\}
=-\frac1{16}\int_Ix^8R^2(3R+xR')=0.
\tag{8}
$$

最后一步用 $\int x^9R^2R'=-3\int x^8R^3$，端项由 $R$ 紧消失。于是由(2)准确得到

$$
\boxed{F_{Y,2}(u):=I_2\{u,Y(u,u)\}=0}
\qquad\text{对每个紧 }u.
\tag{9}
$$

(9)不要求 $u$ 的三个二次矩为零。它也不是只在某个已选 profile 或微包族成立。

现在让 $w$ 为任意另一个紧输入。对真正紧的一参数族 $u+tw$ 微分(9)，得到

$$
\boxed{
2I_2\{u,Y(u,w)\}
=-I_2\{w,Y(u,u)\}.
}
\tag{10}
$$

这里使用原双线性 $Y$ 与原对称配对 $I_2$。没有对两个同时带非零左尾的函数擅用紧方向变分；(10)的两个输入 $u,w$ 都是真紧函数。

## 3. 完整平方，而非交换子或 pure 对角

R282 的原平方规范是

$$
Q_{1,1,2}(\theta)
=-I_2(B_1D_\theta,B_1D_\theta)
+2I_2\{\phi_\theta,B_1(\phi_\theta,B_1D_\theta)\},
\qquad B_1=\zeta Y.
\tag{11}
$$

取(10)中的 $u=\phi_\theta$、$w=YD_\theta$。两者紧性已经分别由原 profile collar 和§1证明。于是

$$
\begin{aligned}
\zeta^{-2}Q_{1,1,2}
&=-I_2(YD_\theta,YD_\theta)
-I_2\{YD_\theta,Y(\phi_\theta,\phi_\theta)\}\\
&=-I_2\{YD_\theta,Y(f,f)\}.
\end{aligned}
\tag{12}
$$

第二步使用的是准确二次槽身份
$YD_\theta+Y(\phi_\theta,\phi_\theta)=Y(f,f)$。它保留了不同的 outer 与 inner 槽，未用 pure 替换整个圆。

由 $Y=-2\mathcal G$ 与 $I_2=4E$，

$$
\boxed{
Q_{1,1,2}(\theta)
=-16\zeta^2E\{\mathcal G(f,f),\mathcal GD_\theta\}.
}
\tag{13}
$$

这一步的两个因子分别为 $(-2)^2=4$ 和 $I_2/E=4$；没有混入对称 cross 乘积的额外因子2。

置

$$
A_f=\mathcal G(f,f),\qquad
A_g=\mathcal G(g,g),\qquad
A_{fg}=\mathcal G(f,g).
$$

R231(26) 的原定义是

$$
L_c=E(A_f,A_g-A_f),\qquad
L_s=E(A_f,A_{fg}).
\tag{14}
$$

而完整内槽满足

$$
\mathcal GD_\theta
=-\sin^2\theta\,(A_g-A_f)
-2\cos\theta\sin\theta\,A_{fg}.
\tag{15}
$$

代入(13)便得到(1)。这里 $A_f,A_g$ 可以保留共同非零左二次尾；真正紧的是 $A_g-A_f,A_{fg},\mathcal GD_\theta$。所有配对都用这些真实原函数。

## 4. 对 principal 关系与未付项的准确含义

在 $\theta=\pi/2$，(1)特别给

$$
\boxed{Q_{1,1,2}(\pi/2)=16\zeta^2L_c.}
\tag{16}
$$

因此 R285/R289 中从三阶导主项看出的 $L_c$ 关系不是一个仅在高频极限成立的线性依赖。此行的整个低阶余项也跟随同一个身份；在试图同时支付对称乘积和能量时，不需再为这条关系额外控制一个未知的 $C^2$ 常数。

更准确地说，由于 $\zeta\ne0$，整个(1)恒零恰等价于 $L_c=L_s=0$。已有圆支付这两个量后，本外矩在全部五相位记账中准确为零，不只是 $\theta=\pi/2$ 的一次测试值。

但完整 $E_1^2$ history 系数仍是

$$
\frac{1+j^2}{4h}Q_{1,1,0}
+\frac j2Q_{1,1,1}
+\frac h4Q_{1,1,2}.
\tag{17}
$$

本稿没有证明前两个外矩为零；也没有证明其余九个乘积或零/一层 history 被(1)消去。Gaussian 词独立性、真实 period、平台与 flux、全部高阶或有限等距族的要求仍按原问题保留。

(1)对一般真实三矩圆成立，不依赖等平方背景、微包次序、even 母包、高频 IFT 或已付 Gaussian 面积。用于当前 R287 圆时，它只消费已经准确支付的 $L_c,L_s$。这是一条完整必要条件之间的身份，不是一次新的研究运行或一个新造的优化门。
