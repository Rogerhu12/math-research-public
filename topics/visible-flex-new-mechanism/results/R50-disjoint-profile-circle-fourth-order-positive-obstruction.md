# R50：不交profile圆的四阶严格正障碍与完整平方恒等式

日期：2026-11-14。literature 与 repo_sources 分别推导尾消去和平方恒等式，repo_sources 独立全文审，root 全文复核。独立完整证明；仅使用纸面推导与符号代数。

本稿接 [R49 的常段最高次公式](R49-fourth-ruling-leading-coefficient-and-narrow-packets.md)，把其“充分窄化”结论加强为整个不交 profile 类。另核对一个确实不同的中点目标：它有四个准确等距种子，也完整支付二阶、三阶，但仍被同一个严格正量阻断于四阶。

**适用范围。** 几何含非空常状态 $(k,h,\omega)=(0,1,0)$ 段；一阶圆为 $Y_\theta=\cos\theta Y_f+\sin\theta Y_g$，其中 f、g 为实、非零、紧支撑、支撑互不相交，并满足完整三矩圆条件。使用同一几何与指定固定目标，允许全部周期、同 collar 的二阶和三阶齐次 gauge。结论不是一般闭面刚性，不排除无法通过常数 O(2) 旋转变成不交支撑的新 profile 平面，亦不排除改变几何。

## 1. 只需检查的严格正量

记 x=xi、$Q=1+x^2$。沿用 R49 的单状态映射和能量：

$$\mathcal R_0(\phi,\phi)=-\frac{Q\phi'^2+xJ_\phi}{8},\qquad
J_\phi(x)=\int_x^r(Q\phi''^2+2\phi'^2),$$

$$E(\phi,\psi)=\frac14\int Q\phi''\psi''+\frac12\int\phi'\psi'.$$

令

$$R=\mathcal R_0(f,f)-\mathcal R_0(g,g),\quad
T(\phi)=E\{\phi,\mathcal R_0(\phi,\mathcal R_0(\phi,\phi))\}.$$

本稿的关键量是

$$\boxed{S=E(R,R)+2T(f)+2T(g).}\tag{1}$$

三矩相等在本状态特别给 $E(f,f)=E(g,g)$，所以 $J=J_f-J_g$ 在两外 collar 都为零，R 紧支撑。以下正性推导本身只需这一能量相等及支撑不交；完整三矩仍用于已有二、三阶路径。

## 2. 先取消四阶导数能量，保留全部真实尾积分

对任一 phi 定义

$$a_\phi=x\phi''-\phi',\quad F_\phi=Q\phi''-2\phi,\quad
P_\phi=\frac12F_\phi^2-Qa_\phi^2.$$

R49 的两次导数和分部积分公式给

$$\mathcal R_0(\phi,\phi)''=
\frac14a_\phi(a_\phi+Q\phi'''),$$

$$2T(\phi)=\frac1{16}\int P_\phi\mathcal R_0(\phi,\phi)''
-\frac14\int Q\{\mathcal R_0(\phi,\phi)''\}^2.$$

因 f、g 支撑不交，两条二阶导数亦支撑不交。把两式加到 (1)，准确得到

$$S=\frac12\int R'^2+\frac1{16}\int(P_f-P_g)R''.
\tag{2}$$

到这里 R' 仍带完整非局部尾。不能把 (2) 当成逐 bump 的局部积分。

令

$$U=f''^2-g''^2,\quad V=f'^2-g'^2,\quad J=J_f-J_g,$$

$$L=xQU-QV',\quad P=P_f-P_g.$$

则

$$J'=-QU-2V,\qquad R'=\frac{L-J}{8},\qquad
L=-xJ'-(QV)'.$$

式 (2) 因而等价于

$$128S=\int\{(L-J)^2+P(L'+QU+2V)\}.\tag{3}$$

真正的尾消去来自以下积分恒等式：

$$\begin{aligned}
\int(J^2-2LJ)
&=\int\{J^2+2xJJ'+2J(QV)'\}\\
&=-2\int J'QV\\
&=2\int Q^2UV+4\int QV^2.
\end{aligned}\tag{4}$$

边界项严格为零，因为 J、V 在两 collar 为零。等价的逐点总导数是

$$J^2-2LJ-2Q^2UV-4QV^2
=\{xJ^2+2JQV\}'.$$

支撑不交再给 $UV=f''^2f'^2+g''^2g'^2$ 和 $V^2=f'^4+g'^4$。所以 (3)–(4) 已准确变成 f、g 两个局部四次积分之和，而非近似忽略尾。

## 3. 局部多项式与完整平方

对任意实紧支撑 phi，写 $f=\phi$、$p=\phi'$、$q=\phi''$。一次对 phi''' 的分部积分将上一节的局部密度化为

$$\begin{aligned}
\mathcal P(x,f,p,q)={}&\frac{Q^3q^4}{12}
+\frac{2Q}{3}\{(x^2-1)f-Qxp\}q^3\\
&+2Q(f^2-2xfp+Qp^2)q^2
+4Qfp^2q+4f^2p^2+2Qp^4,
\end{aligned}\tag{5}$$

并且

$$128S=\sum_{\phi=f,g}\int\mathcal P(x,\phi,\phi',\phi'').\tag{6}$$

为明确这次分部积分的全部内容，可令

$$a=xq-p,\quad F=Qq-2f,\quad P_*=F^2/2-Qa^2,\quad
L_*=xQq^2-2Qpq.$$

分部前的单 profile 密度是

$$L_*^2+2P_*a(a+Q\phi''')+2Q^2p^2q^2+4Qp^4.$$

其 phi''' 系数是 $2QP_*a$。以 q 为变量取这个系数的从 0 到 q 的多项式原函数 Phi，再减去完整 x 总导数 $d\Phi(x,\phi,\phi',\phi'')/dx$，逐项即为 (5)。所有端 jets 为零，故没有端项。

(5) 虽不必逐点为正，积分却有一个准确的正平方表示。定义

$$\begin{aligned}
\mathcal Q(x,f,p,q)={}&
2Qq^2\left[\left(f-xp+\frac{x^2-1}{6}q\right)^2
+\left(p-\frac x3q\right)^2\right]\\
&+\frac{Q^3q^4}{36}
+4p^2\left(f-\frac x3p\right)^2
+\frac{2(x^2+3)}9p^4.
\end{aligned}\tag{7}$$

直接展开给

$$\boxed{\mathcal P(x,\phi,\phi',\phi'')
=\mathcal Q(x,\phi,\phi',\phi'')
+\frac d{dx}\left(\frac43Q\phi\phi'^3\right).}\tag{8}$$

例如，前两个 q 平方中的方向向量 $(x^2-1,-2x)$ 的平方长度为 $Q^2$，使其 q4 系数加上 $Q^3q^4/36$ 恰为 $Q^3q^4/12$；剩下的分部积分是

$$\int4Q\phi\phi'^2\phi''
=-\int\left(\frac83x\phi\phi'^3+\frac43Q\phi'^4\right).$$

因此

$$\boxed{128S=\sum_{\phi=f,g}\int
\mathcal Q(x,\phi,\phi',\phi'')>0.}\tag{9}$$

更明确地，

$$S\ge\frac1{4608}\int Q^3(f''^4+g''^4)>0.$$

严格性只用非零紧支撑 profile 不可能有二阶导数恒零。这里没有任何窄化、平移足够远或有限网格条件。

## 4. 旧目标的第四阶无法支付

旧目标是

$$g_\varepsilon=g_X+\varepsilon^2(dY_f)^2.$$

在常段上，R49 已给四阶 A、C 两个 ruling 的 sigma² 系数

$$a_2=2T(f),\qquad c_2=-E(R,R)-2T(g).$$

故

$$a_2-c_2=S>0.$$

四阶完整 range 要求两个 ruling 都落在全局 gauge 空间中；这个空间在常段上只包含常函数，所以必须 $a_2=c_2=0$，矛盾。特别地，不能用改变段首 W0 或二、三阶同 collar 齐次 gauge 消去它们：这些改动只影响较低 s 次数。

因此完整三阶圆的任何不交 profile 版本，在所述几何/一阶圆/目标的范围内均不能延拓到四阶。R49 的充分窄化结论是这个结论的特例。

## 5. 中点目标的四个准确种子及重新核对的全 range

现在真的换一个指定目标：

$$\widetilde g_\varepsilon
=g_X+\frac{\varepsilon^2}{2}\{(dY_f)^2+(dY_g)^2\}.
\tag{10}$$

因为支撑不交，$\mathcal S(Y_f,Y_g)=0$ 逐点成立，且每个 Y 都是 infinitesimal isometry。因此四个映射

$$X+\frac\varepsilon{\sqrt2}(\pm Y_f\pm Y_g)$$

准确具有同一个 (10)，不只是形式相等。

保留完整三阶已构造的 $Z_d,W_f,W_g$，它们满足

$$\mathcal L_XZ_d=(dY_f)^2-(dY_g)^2,$$

$$\mathcal L_XW_f=-\mathcal S(Y_f,Z_d),\qquad
\mathcal L_XW_g=-\mathcal S(Y_g,Z_d).$$

令 $t_\theta=-\cos(2\theta)/2$，准确取

$$Y_\theta=\cos\theta Y_f+\sin\theta Y_g,$$

$$Z_\theta=t_\theta Z_d,\qquad
W_\theta=t_\theta(\cos\theta W_f+\sin\theta W_g).$$

直接代入两条 Taylor 方程给

$$\mathcal L_XZ_\theta
=\frac12(H_f+H_g)-(dY_\theta)^2,$$

$$\mathcal L_XW_\theta=-\mathcal S(Y_\theta,Z_\theta).$$

这些是对原完整 range 解的准确线性组合，故周期、两 collar、ruling 和 characteristic 周期函数同时支付；没有只核点态代数而忽略 range。四个 $t_\theta=0$ 的相位恰是上面的四个准确种子。

设

$$A=-\mathcal S(Y_f,W_f),\quad G=-\mathcal S(Y_g,W_g),$$

$$B=-\mathcal S(Y_f,W_g)-\mathcal S(Y_g,W_f),\quad
D=-(dZ_d)^2.$$

完整四阶 forcing 为

$$t_\theta^2D+t_\theta\{\cos^2\theta A+
\cos\theta\sin\theta B+\sin^2\theta G\}.$$

记 $u=\cos2\theta,v=\sin2\theta$，它等于

$$-\frac u4(A+G)+\frac{u^2}4(D-A+G)-\frac{uv}4B.$$

这三个相位函数独立。常段上 $D-A+G$ 的 ruling 二次系数恰为

$$-E(R,R)-2T(f)-2T(g)=-S<0.$$

所以新中点目标虽然有四个准确种子并完整通过三阶，仍不能支付第四阶。窄化中 lambda^-9 的相消是真实的，但并未消去 (9) 的完整正障碍。

## 6. 整个固定混合目标都不能用旋转不交平面绕过

更一般，取固定实数 mu（特别包含 $0\le\mu\le1$），目标二次项为

$$\mu H_f+(1-\mu)H_g.$$

令 $z=\cos^2\theta$，二阶系数是 $t=\mu-z$。与上一节相同的完整二、三阶线性组合成立。支撑不交还给常段最高次的交叉项

$$E(f,\mathcal R_0(g,R))=E(g,\mathcal R_0(f,R))=0,$$

因为相应 characteristic 函数在另一 profile 支撑上仅为仿射尾，而 E 对该仿射尾为零。

于是完整四阶 ruling 的 sigma² 系数准确为

$$\boxed{(\mu-z)\{zS-\mu E(R,R)-2T(g)\}.}\tag{11}$$

作为 z 的二次多项式，它的最高系数是 $-S<0$，所以不可能在全部 $z\in[0,1]$ 上为零。旧目标 mu=1 与中点 mu=1/2 同时包含在内。

因此，只对旧不交二维 profile 平面作常数正交基变换，或者换该平面内一个准确种子作为固定目标，不能解决这条四阶障碍。真正继续本路线，需要无法旋转回不交支撑的 profile 平面，或改变所述常段几何与高阶机制；它们的交叉 forcing 和全 range 必须重新计算。

## 7. 核验范围

独立审查者已逐项手核 (4)、(5)、(7)–(9) 的尾积分、局部多项式及完成平方；全文范围与相位恒等式另行复核。配套符号脚本只检查准确多项式/总导数身份，不运行几何设计或优化。全部结论仍属于形式可解性分析，不代表课题已完成。

准确脚本 `literature_fourth_disjoint_sos_certificate.py` SHA256：`0479a6c635a3e999b5bf69c3b99fdb5be295c63d13550a4c54ca451660bf414a`。开发证书 [literature-fourth-disjoint-sos-certificate-20261114.json](../notes/literature-fourth-disjoint-sos-certificate-20261114.json) 为 775 字节，SHA256 `a394c455dd52af6a923338842b2dcbed93142c13c14706ba764b7b98f2c1b372`。五条准确身份只复核代数，所有边界/支撑/range范围由全文证明。
