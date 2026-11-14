# R239 附录：两普通权组加一异常位的整个出生二全高度严格 Gram 比较

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

**状态：完整有限模型定理。** 任意两个普通组重数、任意三正权、整个物理出生二空间及每个合法相邻高度，原先全逆后压缩的相邻 Gram 比较均严格成立。新增部分是完整第二中系数的全域正性；证明只用同源真实归一后的两个曲率上界和已证两向严格标量比，以严格凹二次的两个端点完成。

[第一、第三系数的全高度证明](R239-appendix-birth-two-all-height-first-third-coefficients.md)与[一般高度实际五维入口](R239-appendix-birth-two-actual-phase-and-common-source-quartic.md)保留全部源、剪切和归一常数。本稿[自含精确 Laurent 证书](../notes/2026-11-14-birth-two-all-height-middle-coefficient-0c.js)核全部端点桥和正分解。此有限子问题关闭；一般出生三及以上、更多权组和原 ISP 仍需继续。

## 1. 整个物理空间上的定理

两个普通组大小 $q,L\ge1$，权分别为 $\sqrt z,1$，异常位权为 $\sqrt w$，其中 $z,w>0$。整体出生二高度
$$h=q+L-3.$$
在原物理层上定义
$$K_2=\ker D\cap\mathcal H_2,\qquad
F_j=\left.\frac{D^j(D^*)^j}{(j!)^2}\right|_{\mathcal H_2},\qquad
\Gamma_j=P_{K_2}F_j^{-1}|_{K_2}.$$
逆先在整个 $\mathcal H_2$ 上取，随后才压缩。所有合法 $0\le j\le h$ 的该逆已由原层满射性支付。

**定理。** 对每个 $1\le n<h$，
$$\boxed{\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\prec\Gamma_{n-1}
\quad\text{在整个 }K_2\text{ 上成立}.}\tag{1.1}$$
没有合法内部高度时陈述为空；没有非零分支时按零空间处理。任意三个正权可整体缩放到上述形式，这种几何缩放保持 (1.1)。

沿原两个组的正交自旋分解，各分支相对出生为 $t=2-i-j$。全部 $t=0$ 分支由严格 Newton 支付，全部 $t=1$ 分支由[整个出生一全高度定理](R239-appendix-birth-one-two-group-singleton-all-heights-strict-bound.md)支付，全部组内重数保留。$\min(q,L)\le3$ 的相对出生已由旧小组全高度定理覆盖。唯一新块是 $q,L\ge4$ 时相对出生二的二维 primitive，必须先在原五维出生层取全逆。

[出生二首末前两边](R239-appendix-birth-two-two-group-singleton-second-and-penultimate-edges.md)已处理 $n=1,2,h-2,h-1$，含全部小高度。故只需 $n,m=h-n\ge3$。一般入口已用同一个固定源合同、几何层倍数和正异常权重标，把该新块的 Schur 行列式化为四次 $P(\omega)$。首主子式以及 $P_0,P_4$ 已严格正，前稿完成 $P_1,P_3>0$。本稿证明剩余 $P_2>0$。

## 2. 第二系数的准确标量域

沿前稿的实际参数，取
$$r=\rho>0,\quad A=1-Rr>0,\quad d=r-T>0,\quad
0<R,T<1,$$
$$\xi=\frac A{R(m+1)},\qquad
\upsilon=\frac d{(n+1)T},\qquad c=\xi\upsilon,\qquad \sigma>0.$$
两个原低范数严格比为
$$R_2=r(1-n\xi\sigma),\qquad
T_2=\frac1r-\frac{m\upsilon}{r^2\sigma},\qquad
0<R_2,T_2<1.\tag{2.1}$$
真实曲率 $F>0$ 满足
$$\boxed{F<F_n:=n(m+1),\qquad F<F_g:=m(n+1)/r.}\tag{2.2}$$
在出生二中，(2.2) 由前稿的实际
$F=n(m+1)-(m+2)\alpha R$、
$rF=m(n+1)-(n+2)\beta T$ 严格给出。

剪切平方及交叉项为
$$x^2=F\sigma\xi^2,\qquad
y^2=F\upsilon^2/\sigma,\qquad xy=-Fc.$$
第二系数的正倍数
$$E_2=\frac{RR_2TT_2r^2}{u^3}P_2$$
准确等于
$$\begin{aligned}
E_2={}&\frac T r(1-R)(1-R_2)+(1-RT)(1-R_2T_2)
+Rr(1-T)(1-T_2)\\
&-R(T+rT_2)x^2-\frac T r(R+R_2/r)y^2
-\frac{2RT(r+1)}rxy-\frac{RT}r x^2y^2 .
\end{aligned}\tag{2.3}$$
这包括全部剪切费用，尤其最后的负四次项。通用四次到 (2.3) 的独立恒等已在前稿证书核验。

## 3. 实际倒数反射与 $r\le1$ 的归约

原首一范数的实际坐标补集见[完整 Pearson 消元](R239-appendix-actual-binomial-pearson-bidiagonal-and-full-shear-elimination.md) §4。在真实高度反射后，用同一个源的共同正缩放，参数变成
$$(n,m,R,T,r,F,\sigma)\longmapsto
(m,n,T,R,1/r,rF,1/\sigma).\tag{3.1}$$
并且
$$R_2\leftrightarrow T_2,\qquad
x'^2=y^2/r,\quad y'^2=x^2/r,\quad x'y'=xy/r.$$
(2.3) 的前三项及四个费用逐项互换，故 $E'_2=E_2$。证书还在独立上下比及剪切变量的完整 Laurent 环中核该身份。曲率的两个上界在 (3.1) 下互换，原域保持。

所以只需证明 $0<r\le1$。以下置
$$\varepsilon=1-r,\qquad
a=\frac m{m+1}\ge\frac34,\qquad c_n=\frac n{n+1}\in(0,1).$$

## 4. 凹曲率与同一个 $\sigma$ 的两个端点

固定 $n,m,R,T,r,\sigma$ 后，(2.3) 是 $F$ 的严格凹二次式，其二次系数为
$$-\frac{RT}r c^2<0.$$
$F=0$ 时 (2.3) 是三个严格正的标量项之和。由 (2.2)，只须证明
$$F_*=\min(F_n,F_g)$$
处的同一个表达式严格正，即可由凹性得到所有实际 $0<F<F_*$ 的严格正性。比较端点不必另有对应可实现权族；这是对已准确归一的标量二次式作不等式证明。

完整 Laurent 式为
$$E_2=K_+\sigma+K_0+K_-/\sigma,$$
$$K_+=n\xi(1+T-2RT)-R(1+T)F\xi^2,$$
$$K_-=\frac{m\upsilon}r(1+R-2RT)
-\frac{T(1+R)}rF\upsilon^2.\tag{4.1}$$
$K_0$ 保留前稿的完整表达式。对这里全部 $F\le F_g$，严格有 $K_->0$，因为其正因子之外的括号至少为
$$1+R-2RT-\frac{(1+R)d}r
=T\left(\frac{1+R}r-2R\right)>0.\tag{4.2}$$

令
$$\sigma_0=\frac{m\upsilon}r,\qquad
\frac1{\sigma_U}=\frac{r\varepsilon}{m\upsilon}.$$
$r=1$ 时约定 $\sigma_U=\infty$。由 (2.1)，
$$\sigma>\sigma_0,\qquad
\sigma<\sigma_U\quad(r<1).\tag{4.3}$$
置
$$C=1-RT+\frac T r(1-R)>0.$$
直接完整整理得到
$$\boxed{E_2=K_+(\sigma-\sigma_0)
+K_-\left(\frac1\sigma-\frac1{\sigma_U}\right)+S,}\tag{4.4}$$
$$\boxed{\begin{aligned}
S={}&\varepsilon C+\frac{Tc}r
\{nm(1-R)-RmF\xi+nF\upsilon+2R(r+1)F-RF^2c\}\\
&-\frac{T(1+R)F\varepsilon\upsilon}{m}.
\end{aligned}}\tag{4.5}$$
证书从完整 $K_0$ 独立核 (4.4)–(4.5)。

若 $K_+\ge0$，只须 $S>0$。若 $K_+<0$，则 $r<1$：当 $r=1,F\le F_n$ 时，
$$K_+\ge n\xi R(1-T)>0.$$
在坏符号区域，$E_2$ 关于 $\sigma$ 严格递减。于是
$$E_2(\sigma)>E_2(\sigma_U)
=S+K_+\frac{m\upsilon}{\varepsilon},\tag{4.6}$$
这里用 $\sigma_U-\sigma_0=m\upsilon/\varepsilon$。该代数端点不必保持 $R_2>0$；只在真实点使用正归一因子，在端点比较完整 Laurent 函数。

## 5. 端点 $F_*=F_n\le F_g$

令
$$C_1=2(r+1)-a\varepsilon>0,$$
$$B=-\frac{(1+R)\varepsilon}{a}+\frac A r C_1.$$
将 $F=F_n=n(m+1)$ 代入 (4.5)，精确得到
$$\boxed{S=\varepsilon C+\frac{nd}{n+1}B
+\frac{nAdF\upsilon}{(m+1)(n+1)}.}\tag{5.1}$$
有完整正分解
$$B=\frac{2\varepsilon(m-1)}m
+\frac{\varepsilon^2(m+2)}{(m+1)r}
+(1-R)\left\{\frac{\varepsilon(m+1)}m+C_1\right\}>0.\tag{5.2}$$
所以 $K_+\ge0$ 时端点已经严格正。

若 $K_+<0$，令
$$\Delta=2T-r(1+T)=T\varepsilon-d.$$
此端点准确有
$$K_+=-\frac{nA}{m+1}\Delta.$$
故 $0<\Delta<T\varepsilon$。由 (4.6)，坏项的绝对值严格小于
$$\frac{nd}{n+1}\,aA.$$
而
$$\boxed{\begin{aligned}
B-aA={}&\varepsilon\left\{4-a-\frac2a+
\frac{(2-a)\varepsilon}{r}\right\}\\
&+(1-R)\left\{\frac{\varepsilon}{a}+2(r+1)-a\right\}>0,
\end{aligned}}\tag{5.3}$$
其中
$$4-a-2/a=\frac{m^2-2}{m(m+1)}>0.$$
把 (5.3) 代入 (5.1)，即使支付全部坏项仍严格正。因此 $F_n$ 端点的两种 $K_+$ 符号均完成。

## 6. 端点 $F_*=F_g\le F_n$

此时令
$$b_0=\frac{m(n+1)}{n(m+1)r}\le1.$$
(4.5) 有准确分解
$$S=S_{\rm rough}+\mathrm{Rem}_1+\mathrm{Rem}_2,\tag{6.1}$$
$$\mathrm{Rem}_1=\frac{T\xi\upsilon}{r}
nA(1-b_0)(m+F\upsilon)\ge0,$$
$$\mathrm{Rem}_2=\frac{aAd}{r}
\left\{(1-c_n)\varepsilon+c_n d/T\right\}>0,$$
$$S_{\rm rough}=\varepsilon[2-R(1+r)]+dB_g,$$
$$\boxed{\begin{aligned}
B_g={}&\frac{\varepsilon}{r^2}
\{(1+a)r^2+(2-a)\varepsilon+(3a-2)\}\\
&+(1-R)\{(3a-1)+(a+1)r+2a\varepsilon/r\}>0.
\end{aligned}}\tag{6.2}$$
所有项直接严格或非负；$a\ge3/4$ 保 $3a-2>0$，而 $r=1$ 时第二行仍严格正。因此 $S>0$，$K_+\ge0$ 的端点完成。

若 $K_+<0$，因为 $K_+$ 随 $F$ 递减且 $F_g\le F_n$，
$$K_+(F_g)\ge K_+(F_n)
=-\frac{nA}{m+1}\Delta.$$
坏符号仍推出 $0<\Delta<T\varepsilon$。于是 (4.6) 的坏项严格小于 $c_n aAd$。另一方面，(6.2) 给
$$\boxed{\begin{aligned}
B_g-aA={}&\frac{\varepsilon}{r^2}
\{r^2+(2-a)\varepsilon+(3a-2)\}\\
&+(1-R)\{(3a-1)+r+2a\varepsilon/r\}>0.
\end{aligned}}\tag{6.3}$$
所以
$$S-c_n aAd
=\varepsilon[2-R(1+r)]+d(B_g-aA)
+(1-c_n)aAd+\mathrm{Rem}_1+\mathrm{Rem}_2>0.$$
这个端点的坏符号也全部支付。

若 $F_n=F_g$，任选以上一节。两端点与 $F=0$ 的严格正性、§4 的凹性合并，得到所有实际 $F$ 的 $E_2>0$。由 §3 的真实反射，$r>1$ 同样成立。因此 $P_2>0$。

## 7. 拼接整个 $K_2$ 与后续边界

五个系数全部严格正，故对每个异常权 $\omega>0$，
$$P(\omega)>0.$$
完整 Schur 行列式只相差已经保留的严格正分母，配合其严格正首主子式，得到新二维块的严格相邻序。首末前两边、全部小组以及原 $t=0,1$ 分支均在 §1 已支付。有限正交直和保留原组内重数，得到整个物理 $K_2$ 的 (1.1)。

本稿第二系数论证本身比出生二实际相位更一般：只依赖 (2.1)–(2.3) 和两个曲率上界。它没有使用 $\Delta_2$ 的实根性，也没有把任意 Hankel 正性当成相邻 Gram 序。但第一系数的坏 Laurent 区域在前稿确实使用了出生二的实际相位预算；不能将本稿的较一般标量引理直接宣布为所有出生层的完整定理。

下一未闭有限对象是同一个原二项式矩族的相对出生 $t\ge3$，尤其真实高阶曲率对第一系数坏区域的控制，以及更多独立权组。原正常商和边界 $N=M$ 也继续开放。这里没有改变普通 ISP 的目标或完成标准。

## 8. 精确核验

自含 JavaScript 证书用 BigInt 系数和完整有符号整数指数向量。只允许对单项式取逆；非单项式代换前须显式清分母，未清负指数会报错。它精确核：完整 $S$ 桥；$F_n$ 端点、其正分解、坏符号尾及 $K_+$ 身份；$F_g$ 两个正余项、粗式重写及两种 $B_g$ 正分解；完整七项的 $r$ 反射。共十一组通用身份全部通过。

根代理和 two_weight_general_height_1856 独立审读端点比较和严格不等式，并各自在可用 JavaScript 运行时执行完整证书通过。原五维全逆入口及通用第二系数桥由两篇依赖的完整程序和证明承担。终端当前失联，未声称进行了额外终端重跑。没有用有限重数或权比取样代替任何全参数正性结论。
