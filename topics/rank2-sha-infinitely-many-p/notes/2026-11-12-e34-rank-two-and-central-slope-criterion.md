# E34 的初等秩二证书与实际普通中心斜率判据

日期：2026-11-12。**状态：已证明。**
本篇把第二条实际 theta 行补成可用于主课题的完整候选：
它有独立于数据库的精确秩证明，且其实际 Mellin 一阶导数非零
与相应普通素数的初级 Sha 有限准确等价。

## 1. 明确的二同源和两个有理独立点

设
\[
 C:y^2=x^3+289x,\qquad E_{34}:Y^2=X^3-1156X.
\]
两条有理二同源为
\[
 \phi(x,y)=\left(x+\frac{289}{x},
                   y\left(1-\frac{289}{x^2}\right)\right),
\]
\[
 \widehat\phi(X,Y)=\left(\frac{X-1156/X}{4},
                   \frac{Y(1+1156/X^2)}8\right).
 \tag{1}
\]
在原点及核点按延拓解释；直接代入曲线和加倍公式给
$\widehat\phi\phi=[2]$。
取
\[
 P=(68,578),\quad Q=(144,1740)\in C(\mathbb Q),
 \quad R=(-2,48),\quad S=(34,0)\in E_{34}(\mathbb Q).
\]
有
\[
 \widehat\phi(R)=Q,\quad\widehat\phi(S)=(0,0)=T,
\]
\[
 P_{34}=\phi(P)=\left(\frac{289}4,\frac{4335}8\right),\quad
 Q_{34}=\phi(Q)=\left(\frac{21025}{144},\frac{2964815}{1728}\right).
 \tag{2}
\]

对一般 $y^2=x^3+bx$，二同源下降映射是
$\alpha(O)=1$、$\alpha((0,0))=b$、$\alpha((x,y))=x$
于 $\mathbb Q^\times/\mathbb Q^{\times2}$。
其同态性由穿过三点的直线与三次方程的根乘积得出，
核是对偶同源像；也可由 (1) 解其二次逆像方程验证。
每个像的平方自由代表只含 $b$ 的素因子：
若 $q\nmid b$，正的奇数 $v_q(x)$ 与 $y^2=x(x^2+b)$ 矛盾，
负的奇数 $v_q(x)$ 则与两项的最低赋值 $3v_q(x)$ 矛盾。

对 $C$，非零有理点的 $x$ 为正，故
\[
 \alpha(C(\mathbb Q))\subset\{1,17\}.
\]
$\alpha(P)=17$，所以上式为等号。对 $E_{34}$，有
\[
 \alpha'(E_{34}(\mathbb Q))\subset
 \langle-1,2,17\rangle.
\]
令 $T'=(0,0)\in E_{34}$，则
\[
 \alpha'(T')=-1,\qquad\alpha'(S)=34,\qquad\alpha'(R)=-2.
 \tag{3}
\]
三者在平方类群中独立，故两个下降像的大小分别为 $2,8$。
由于 $\ker\widehat\phi=\{O,T'\}$ 且
$T'\notin\phi C(\mathbb Q)$（其 $\alpha'$ 非平凡），准确的指数为
\[
 [C(\mathbb Q):2C(\mathbb Q)]
 =[C:\widehat\phi E_{34}]
  [E_{34}:\phi C+\ker\widehat\phi]
 =2\cdot\frac82=8.                                      \tag{4}
\]
这里特意保留核的因子 $2$；$T=\widehat\phi(S)$ 本身在对偶同源像中。

两曲线在 $3,5$ 的点数均为 $4,8$，由好约化的素数外挠点注入，
有理挠群的阶都整除 $4$。$C$ 只有一个非零有理二挠点 $T$。
若 $2U=T$，加倍公式迫使 $x(U)^2=289$；$x=-17$ 时右边负，
$x=17$ 时右边是 $17^2\cdot34$，均不是有理平方。
故 $C(\mathbb Q)_{\rm tors}=\langle T\rangle\simeq C_2$，
而 $E_{34}$ 的全部二挠点有理，故其有理挠群为 $C_2^2$。
(4) 遂给
\[
                 \operatorname{rank}C(\mathbb Q)
                 =\operatorname{rank}E_{34}(\mathbb Q)=2.    \tag{5}
\]

还可直接证明 (2) 的两点独立。若
$aP+bQ+cT=O$，其中 $a,b\in\mathbb Z$、$c\in\{0,1\}$，
应用 $\alpha$ 得 $a=2a_1$。因此
\[
 a_1\phi(P)+bR+cS=dT'\quad(d\in\{0,1\}).
\]
应用 $\alpha'$，利用 $\alpha'(\phi P)=1$，得
\[
                         (-2)^b34^c=(-1)^d.
\]
比较 $17$、$2$ 和符号的平方类，依次得 $c=0$、$2\mid b$、$d=0$。
故任何这样的关系都迫使 $a,b$ 为偶数且 $c=0$。
除以 $2$ 后只可能多一个 $T$，再次使用同一结论；无限下降给 $a=b=0$。
所以 $P,Q$ 独立，(1) 也使 $P_{34},Q_{34}$ 独立。

所有有限运算由
[准确脚本](../scripts/check-e34-rank-and-theta-multiplier.py)
复算；无限下降和指数论证为上述证明，不由有限搜索替代。

## 2. 普通 CM 主猜想及高度定理的曲线输入

以下固定 $K=\mathbb Q(i)$、
$p\ge13$、$p\equiv1\pmod4$、$p\ne17$。
用 $E_{34}$ 自己的 Hecke 字符 $\psi_{34}$、Néron 微分 $dX/(2Y)$
及相容的普通周期 $\Omega_{34,p}$。

1. $\operatorname{End}_K(E_{34})=\mathbb Z[i]$，$K$ 类数一；
   所列 $p$ 为好普通素数。
2. R115 §3 的直接局部角色计算给 Hecke 导子
   $\mathfrak f=(68)=(1+i)^4(17)$（相差单位）。因此
   \[
   [K(\mathfrak f):K]
    =\frac{4624}{4}\left(1-\frac12\right)
                    \left(1-\frac1{17}\right)^2=512,
   \tag{6}
   \]
   与所列 $p$ 互素。
3. 全局根数为 $+1$。在 $17$ 处是 $I_0^*$ 型，局部根数
   $(-1/17)=1$。在 $2$ 处，将 $t=-1156$ 代入
   Desjardins 的 Lemma 3.8：$v_2(t)=2$、$t_{(2)}=-289\equiv15\pmod{16}$，
   故局部根数 $-1$；无穷处为 $-1$，其他位好约化。
4. 因有理二挠点完整，$a_p$ 为偶数。Hasse 界及 $p\ge13$ 给
   $|a_p|<p-1$，所以 $a_p\not\equiv1\pmod p$，非异常性成立。
5. 辅助理想 $(7)$ 满足 $\psi_{34}((7))=-7$。
   这是 $E_0:y^2=x^3-x$ 的值乘二次扭曲角色在 $49$ 的值 $1$。
   扭转 Coleman 因子的中心值为 $-7-49=-56$，对所列 $p$ 都是单位。
6. CM 扭点域以及相关塔的有限层对 $K$ 阿贝尔，满足
   Perrin–Riou 原文 V 开头、印刷页 96 所需的两处 CM Leopoldt 条件。

第 3 项的外部来源是 Desjardins，*Root number of twists of an elliptic curve*，
JTNB **32** (2020), 73–101，Proposition 3.1、Lemma 3.8：
[原文](https://www.numdam.org/item/JTNB_2020__32_1_73_0.pdf)。
第 2、5 项确保 Agboola–Howard 的整系数比较能直接使用，
没有借用 $E_{17}$ 的导子或有限字符。

## 3. 反圆分二阶项与完整 Sha

令 $F^-_{34,p}(T)$ 为 R40 定义 (2) 的实际扭转 Katz 分支，
将其中 $E,\psi,\Omega$ 全部换成本篇的 $E_{34},\psi_{34},\Omega_{34,p}$。
仍取 $\rho^-(\gamma)=1+p$、$T=\gamma-1$，并写
\[
 r_{34,p}=\operatorname{corank}_{\mathbb Z_p}
                    \Sha(E_{34}/\mathbb Q)[p^\infty].
\]
则
\[
 F^-_{34,p}\ne0,\qquad
 \operatorname{ord}_0F^-_{34,p}\ge2+r_{34,p},                 \tag{7}
\]
\[
 \boxed{\quad\Sha(E_{34}/\mathbb Q)[p^\infty]\text{有限}
          \iff[T^2]F^-_{34,p}\ne0.\quad}                    \tag{8}
\]

说明 R37、R40 的证明如何在此准确落地。对 (2) 的独立有理点定义
\[
 \eta_U=\frac{Y+Y(U)}{X-X(U)}\frac{dX}{2Y},\qquad
 j_{34,p}=h^-([i]P_{34},Q_{34}).
\]
两个点的 $Y$ 坐标非零；复共轭给其在 $\mathbb Q(i)$ 上仍独立。
R37 的广义 Jacobian 使用 modulus
$O+P_{34}+Q_{34}+[i]P_{34}+[i]Q_{34}$。
四个扩张类的整数独立性使其没有非平凡 affine 商；
两列投影的 CM 独立性使两份代数提升的群包是整个乘积。
ordinary 补空间仍为 $\mathbb Q_p[X\omega]$，因为
$[i]^*\omega=i\omega$、$[i]^*(X\omega)=-iX\omega$。
第三类微分仍逐式满足 $[i]^*\eta_{[i]U}=\eta_U$。
因此 R37 式 (24) 的高度互易式把 $j_{34,p}$ 化为同一个非零
代数 Lie 线性形式；所引 $p$-adic analytic subgroup theorem 给
\[
                              j_{34,p}\ne0.                  \tag{9}
\]
这些步骤只用了上述独立性、CM 自同构及类数一，
没有使用方程中系数为 $17$ 的特殊数值。

完整 $\pi$-Selmer 空间的维数为 $2+r_{34,p}$；
这是 R40 的 Kummer、复共轭及 $[i]$ 分解，未删去 Sha 商。
Perrin–Riou V.8、V.17 的完整主项下界于是给 (7) 的阶数不等式。
当 $r_{34,p}=0$，反圆分高度矩阵就是
\[
 \frac1{2\iota}
 \begin{pmatrix}0&j_{34,p}\\-j_{34,p}&0\end{pmatrix},
 \qquad\iota^2=-1,
\]
由 (9) 非退化，故首项恰二阶。
反之二阶非零由下界迫使 $r_{34,p}=0$。
Agboola–Howard Theorem 2.4.17(1) 和 §2.3 的 Coleman 比较，
以 (6) 及辅助因子 $-56$，把特征理想的结论传到实际 $F^-_{34,p}$。
其 Corollary 2.1.5 还给分支非恒零。所用已发表原文：

- [Perrin–Riou 1984](https://www.numdam.org/article/MSMF_1984_2_17__1_0.pdf)，
  V.8、V.17 以及 V §4 的完整高度比较。
- [Agboola–Howard 2006](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)，
  Theorem 2.4.17(1)、Proposition 2.3.4、Corollary 2.1.5。
- [R37](../results/R37-cm-period-reciprocity-nonvanishing.md) §§2–7 给
  AST、Coleman 积分与广义 Jacobian 接口的完整证明及一手文献。

## 4. 实际次数六十八截面的平方与一阶判据

令 $B(z)=A_{34}(z)$ 是 R115 在 $E_0$ 尺度认证的完整截面，
原曲线尺度为
\[
 S_{34}(z)=34^{-2}B(\sqrt{34}z)=\sum b_m^{(34)}z^m,
 \qquad b_4^{(34)}=1.                                      \tag{10}
\]
它的系数有理，只在 $4\mid m$ 时可能非零。
R115 的实际中央迹与完整平方公式给
\[
 e_m=\kappa_{34}(4624\cdot68)^{-m}(b_m^{(34)})^2,
 \quad\kappa_{34}=e_4(4624\cdot68)^4\ne0.                  \tag{11}
\]
这保留了新的二处角色和全部共同常数；$e_4\ne0$ 已有严格证书。

固定同一普通周期，令 $\nu_{34,p}$ 为整 Amice 变换
\[
 S_{34}(\Omega_{34,p}\log(1+Z))
\]
对应的有界测度，并定义实际 principal Mellin 系列
\[
 J_{34,p}(T)=\int_{\mathbb Z_p^\times}
 (1+T)^{\log\langle x\rangle/\log(1+p)}\,d\nu_{34,p}(x).
 \tag{12}
\]
R38 的 CM ordinary sigma 整性适用于好普通 $E_{34}$；
R115 的多项式仅含所列 $p$ 可逆的固定分母，因此这里确为整测度。

R46 §4 的完整插值论证代入 (11) 给整条实际分支恒等式
\[
 F^{\Theta,-}_{34,p}(T)=
 \kappa_{34}\,68\,\Omega_{34,p}
 (1+T)^{\log\langle68\rangle/\log(1+p)}J_{34,p}(T)^2.
 \tag{13}
\]
具体核对参数为 $f=68$、$Nf=4624$、$d=68$，故 $f^2/d=68$。
在 $m>0$、$p-1\mid m$ 的插值点，两份矩都为
$\Omega_{34,p}^m m!b_m^{(34)}$，普通 Euler 因子为
$(1-\pi^m/\bar\pi^{m+1})^2$。
沿 $m=m_0+(p-1)p^n$ 同时令实大小趋于无穷、$p$ 进趋于 $m_0$，
删去非单位矩的误差和 Euler 误差均趋零，得到 (13)；
再由累积点的解析恒等定理推广到整条分支。
这与 R46 相同的极限保留了两个阶乘、普通周期和有限角色，
不需要逐权选择任何未知单位。

实际 Katz 与 theta 规范间相差的完整可逆因子不改变中心零阶。
(7)、(13) 遂给 $J_{34,p}(0)=0$，并从 (8) 得
\[
 \boxed{\quad
 \Sha(E_{34}/\mathbb Q)[p^\infty]\text{有限}
       \iff J_{34,p}'(0)\ne0.\quad}                         \tag{14}
\]
常数 $\kappa_{34}$ 只须非零；本篇不把它对所有 $p$ 都为单位作为前提。

## 5. 两行比较现已成为主目标的准确充分条件

在[完整线性卷积笔记](2026-11-12-two-rank-two-theta-linear-convolution.md)
的共同 $E_0$ 尺度，有 $J_A=17J_{17}$、$J_B=34^2J_{34}$。
因此其中已证明的实际积分
\[
 I_p=\int_{\mathbb Z_p^2}
      \bigl(f_p(u+2x)-f_p(2x)\bigr)\,d\sigma_p(u)\,d\nu_{A,p}(x)
     =16\cdot34^2J_{34,p}'(0)-17J_{17,p}'(0)                \tag{15}
\]
若对无穷多个所列普通 $p$ 非零，则每个这样的 $p$ 至少使
$E_{17}$、$E_{34}$ 中一条的初级 Sha 有限。
这两条曲线固定且均秩二，有限鸽巢原理给其中一条满足主课题目标。

(15) 的非零性仍待证明。本篇补齐的是 (15) 与真正 Sha 命题之间的接口，
不把非挠零除子、两行独立或已知反圆分 MW 高度非零当作该积分非零。
