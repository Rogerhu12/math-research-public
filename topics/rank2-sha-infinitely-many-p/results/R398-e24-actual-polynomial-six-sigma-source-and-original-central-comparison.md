# R398 — E24 的实际代数分子、原六 sigma 乘积与 E17 完整中央比较

日期：2026-11-14。**状态：同一个原六项来源的七个分子系数、绝对整体常数、原点恰六阶、与 E17 原来源的实际乘法/完整卷积关系均已证明。另由原有限证书证明 E24 秩恰二及其七初级 Sha 有限。未证明无穷多个素数的中央导数非零；完整卷积不被当作 Mellin 乘积。**

## 1. 结论及同一来源的规范

仍用 $E_b:y^2=x^3+b$、$x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$、
$\sigma=z+\cdots$，及
$$
\delta=1+2\omega=\sqrt{-3},\qquad
\gamma=(5+\delta)/2,\qquad N\gamma=7,\qquad X=x^3 .
$$
物理新曲线为 $b=24$。下面先在其固定同源缩放模型中给公式；
所有 sigma 都属于同一个 $E_b$，没有在乘积内混用周期。

R395 的实际规范源记为 $\Phi_b$。它由该篇六个原九阶 lift 定义，
不另行改变各项相位。置
$$
\begin{aligned}
Q_4(X)&=(X+4b)(X^3-96bX^2+48b^2X+64b^3),\\
R_2(X)&=X^2+20bX-8b^2,\\
P_6(X)&=(7X^2-4bX+16b^2)(X+b)(X-8b)R_2(X)\\
&=7X^6+87bX^5-1128b^2X^4+104b^3X^3
 -1632b^4X^2-1920b^5X+1024b^6.
\end{aligned}
\tag{1}
$$

**定理。** 对 R395 的原实嵌入，$\sqrt[3]9$ 取正实根，准确有
$$
\boxed{
a_b:=[z^6]\Phi_b=-6048\,b\,\sqrt[3]9,\qquad
\Phi_b=\frac{a_b}{7}\,\sigma^{72}XQ_4(X)P_6(X).
}
\tag{2}
$$
所以该篇尚待求的实际分子为
$$
\boxed{R_6(X)=-864\,b\,\sqrt[3]9\,P_6(X).}
\tag{3}
$$
在物理 $E_{24}$ 上 $a_{24}=-145152\sqrt[3]9$。
它在每个 $p>7$ 都是单位；在七处恰有 $v_7(a_{24})=1$。
整来源本身在七处仍然 primitive，不能把除以 $a_{24}$ 后的来源
在七处也无证视为整。

定义首项一的 $T_b=\Phi_b/a_b$。若 $S_b$ 是 R297 的同一原式
$$
S_b=\frac17\sigma^{34}x^2
 (X+b)(X-8b)(7X^2-4bX+16b^2),
$$
则
$$
\boxed{
T_b=S_b H_{38,b},\qquad
H_{38,b}=
 \frac{\sigma(3\delta z)}{3\delta\,\sigma(z)}
 \frac{\sigma(4z)}{2\sigma(2z)},\qquad H_{38,b}(0)=1.
}
\tag{4}
$$
等价的真实六因子表达为
$$
\boxed{
T_b(z)=
-\frac{\sigma(\delta z)\sigma(2\delta z)\sigma(3\delta z)
        \sigma(4z)\sigma(\gamma z)\sigma(\bar\gamma z)}
       {504\delta}.
}
\tag{5}
$$
总 degree 是 $3+12+27+16+7+7=72$，首项为 $z^6$。
以下先确定实际六项的常数，再用完整 CM7 迹唯一确定整条来源；
(5) 不是按 degree 或少数近似系数认定的候选。

## 2. 六个真实 lift 直接给绝对首项

保留 R395 的格 $\Lambda=\mathbf Z+s\mathbf Z$ 及
$\eta_1s-\eta_s=2\pi i$；物理坐标同步乘 $\Omega_b$。
其六个标签为
$$
t_{m,n}=(m+ns)/9,\qquad 0\le m\le2,\ n=1,2,
$$
系数依次是
$$
(c_{m,n})=
\begin{array}{c|ccc}
 &0&1&2\\ \hline
1&1&\omega&\omega^2\\
2&1&\omega&\omega
\end{array}.
\tag{6}
$$
此处以及本节的格点公式在物理模型中带同一个 $\Omega_b$。

令 $P=3t$。这些 $P$ 是六个不在 $E[\delta]$ 中的三挠点，故
$$x_P^3=-4b,\qquad y_P^2=-3b.$$
设 $\chi(\lambda)$ 为原 sigma 半特征，定义
$$
r_P=\chi(3P)\frac{e^{\eta_PP/2}}{\sigma(P)},\qquad
\sigma_P(w)=
e^{-\eta_Pw}\frac{\sigma(P+w)}{\sigma(P)}.
\tag{7}
$$
R395 的完整 lift 作用于 $B=\sigma(9z)/(3\sigma(3z))$。
因 $9t=3P$ 是原周期，准周期的线性及常数项逐一抵消后，准确有
$$
\boxed{\mathsf T_tB(z)=\frac{r_P}{3}\,
                    \frac{\sigma(9z)}{\sigma_P(3z)}.}
\tag{8}
$$
例如分子准周期贡献 $81\eta_tz+(81/2)\eta_tt$，
lift 减去 $72\eta_tz+36\eta_tt$，
而分母的 translated sigma 再减去 $9\eta_tz$。
剩余常数正是 (7)，没有将它 rigidify 为一。

### 2.1 三挠点的准确代数常数

由 $2P=-P+3P$ 和标准式 $\sigma(2P)=-2y_P\sigma(P)^4$，
$$
\boxed{r_P^3=2y_P.}
\tag{9}
$$
又倍点 zeta 公式给
$$
\zeta(2P)=2\zeta(P)+\frac{3x_P^2}{2y_P}
=-\zeta(P)+3\eta_P,
$$
所以
$$
c_P:=\zeta(P)-\eta_P=-\frac{x_P^2}{2y_P},\quad
c_P^2=x_P/3,\quad c_Px_P^2=-2x_Py_P/3.
\tag{10}
$$
由 $x'=2y,\ y'=3x^2$，
$$
\log\sigma_P(w)=c_Pw-\frac{x_Pw^2}{2}
-\frac{y_Pw^3}{3}-\frac{x_P^2w^4}{4}
-\frac{x_Py_Pw^5}{5}+O(w^6).
$$
因此逐项指数展开、再用 (10)，得到
$$
\begin{aligned}
[w^5]\sigma_P(w)^{-1}
&=-\frac{c_P^5}{120}-\frac{c_P^3x_P}{12}
-\frac{3c_Px_P^2}{8}+\frac{c_P^2y_P}{6}
+\frac{11x_Py_P}{30}\\
&=\boxed{\frac{56}{81}x_Py_P}.
\end{aligned}
\tag{11}
$$
$\sigma(9z)=9z+O(z^7)$，所以 (8) 的六阶系数准确为
$$[z^6]\mathsf T_tB=504\,r_Px_Py_P.$$

### 2.2 六相位和，而不是任选立方根

取 $P_0=s/3$、$(r_0,x_0,y_0)=(r_{P_0},x_{P_0},y_{P_0})$。
若 $3P=m+ns$ 且 $\lambda=u+vs$，原半特征给
$$
r_{P+\lambda}=\omega^{-(mv-nu)}r_P,\qquad
r_{\omega P}=\omega^2r_P,\qquad r_{-P}=-r_P.
\tag{12}
$$
第一式包含半特征的 $(-1)^{mv-nu}$ 与 Gaussian 的
$e^{\pi i(mv-nu)/3}$，不能只保后一个因子。
实际六点表为
$$
\begin{array}{c|ccc|c}
(m,n)&x_P/x_0&y_P/y_0&r_P/r_0&c_{m,n}\\ \hline
(0,1)&1&1&1&1\\
(1,1)&\omega^2&1&1&\omega\\
(2,1)&\omega&1&1&\omega^2\\
(0,2)&1&-1&-1&1\\
(1,2)&\omega&-1&-\omega&\omega\\
(2,2)&\omega^2&-1&-1&\omega
\end{array}.
\tag{13}
$$
每一行 $c_{m,n}r_Px_Py_P$ 都等于 $r_0x_0y_0$。
故
$$
a_b=3024\,r_0x_0y_0,\qquad
(r_0x_0y_0)^3=(2y_0)(-4b)y_0^3=-72b^3.
\tag{14}
$$
R395 的原 $G_{24}$ 是实来源，故其首项也为实。
(14) 的三个根中唯一实根是负根，于是
$a_b=-3024b\sqrt[3]{72}=-6048b\sqrt[3]9$。
这完整支付 (2) 的绝对常数，并独立证明原点恰六阶。
特别不能把七处的 $a_b$ 当单位。

## 3. 实际 CM7 算子与完整七纤维

R400 已从同一全权平方和原有界测度证明
$$
\boxed{\mathscr M_\gamma\Phi_b=-\gamma\Phi_b,\qquad
 \mathscr M_\gamma=[\gamma]_*[\bar\gamma]^*.}
\tag{15}
$$
该证明在 $p=7$ 直接使用原整 $\Phi_b$，
没有预先除以 $a_b$，也不需要先知道有限 theta 空间单重。
其绝对值来自 $\psi_{24}((\gamma))=-\gamma$。
固定 homothety 不改变 (15)。

现在在 $b=1$ 模型精确计算。R297 的原 division 式给
$$
r_\gamma(z)=\frac{\sigma(\gamma z)}{\sigma(z)^7}
 =\gamma(x^3-r),\quad
r=\frac{2-6\delta}{7},\qquad
\bar r=\frac{2+6\delta}{7}.
\tag{16}
$$
令
$$
N_r(x)=x^6+(28r+12)x^3+7r^2+24r.
$$
两次对数微分准确给
$$
x(\gamma z)=\frac{xN_r(x)}{\gamma^2(x^3-r)^2}.
\tag{17}
$$
因而在目标 $x=a$ 的全部七个实际纤维上，源 $x$ 满足首一多项式
$$
f_a(x)=xN_r(x)-\gamma^2a(x^3-r)^2.
\tag{18}
$$
其余 $y$ 方向由原微分及目标 $y$ 唯一确定。
本篇取 $a=1,\ldots,13$，目标 $y$ 均非零，
这些是七个真实 isogeny 原像的完整 trace。

为避免把巨大的函数分母或中心常数藏掉，置
$$
q=x^3-r,\quad \bar q=x^3-\bar r,\quad
U=x^3N_{\bar r}(x)^3,\quad W=\bar\gamma^6\bar q^6.
$$
对 $P(X)=\sum_{j=0}^{12}P_jX^j$，完整原迹正是
$$
\boxed{
\frac{\mathscr M_\gamma(\sigma^{72}P(x^3))}{\sigma^{72}}
=\gamma^{-72}\operatorname{Tr}_{K[x]/(f_a)}
 \left(q^{-72}\sum_{j=0}^{12}P_jU^jW^{12-j}\right)
\quad(x_{\rm target}=a).
}
\tag{19}
$$
这来自 $(r_{\bar\gamma}/r_\gamma)^{72}$ 及实际 $x(\bar\gamma z)$，
完整保留 leading constants $\gamma,\bar\gamma$；
没有除七，没有改成一个仅同像的 Weyl 投影。

取候选
$$
P(X)=XQ_4(X)P_6(X)\qquad(b=1).
$$
其升幂系数为
$$
(0,\ 262144,\ -229376,\ -1253376,\ 159744,\ 463872,\
 -153216,\ 391872,\ 76440,\ -11484,\ -557,\ 7,\ 0).
\tag{20}
$$
逐个在 (18) 的七维代数中作准确有理运算，
对 $a=1,\ldots,13$ 全部得到
$$
\boxed{\text{(19)}=-\gamma P(a^3).}
\tag{21}
$$
例如 $a=1$ 的准确值为 $734825+146965\delta$，$a=2$ 为零。
旁列 JSON 保存全部十三个值；脚本只使用 BigInt 的
$\mathbf Q(\delta)$ 分数，未用浮点数。

这十三个完整纤维足以证明全恒等式：
$\mathscr M_\gamma$ 保持同一 degree72 line bundle 并与 $\mu_6$ 交换。
因此 (21) 两边都为 $\sigma^{72}$ 乘一个次数不超过十二的 $X$ 多项式。
十三个不同的 $a^3$ 唯一确定它。这里证明的是固定特征零函数身份，
不是按目标素数作有限枚举。

## 4. 在实际七变量条件中唯一，而非假设空间稳定

R395 已把实际来源放入
$$
\mathcal V=\{\sigma^{72}XQ_4(X)R(X):\deg R\le6\}.
$$
**不需要、也不声称 $\mathscr M_\gamma$ 保持整个 $\mathcal V$。**
我们只解同一来源的指定等式 (15)。

对基 $R=X^j$，$j=0,\ldots,6$，用 (19) 在 $a=1,\ldots,7$ 取值，
除以 $a^3Q_4(a^3)$，所得七行矩阵记为 $Y$。
令 $V_{a,j}=(a^3)^j$，则指定方程的必要条件准确是
$$
A c=0,\qquad A=V^{-1}Y+\gamma I .
\tag{22}
$$
这只是有限评价的行变换，不把 $V^{-1}Y$ 冒称为 $\mathcal V$
上的闭合算子。

在 $1009$ 处取 $\delta\mapsto260$，所有运算分母为单位。
(22) 的准确约化为
$$
\begin{pmatrix}
153&389&173&298&559&70&1000\\
879&558&354&69&737&476&876\\
744&91&824&344&496&918&398\\
258&459&830&677&655&256&66\\
875&182&537&526&377&575&800\\
862&241&516&700&486&931&904\\
745&207&587&47&859&100&447
\end{pmatrix}.
\tag{23}
$$
其前六行、前六列的行列式准确为 $85\bmod1009$。
因此特征零的 (22) 秩至少六。
另一方面 §3 已全局证明 (20) 是非零解，故完整解空间恰一维。
实际 $\Phi_b$ 由 (15) 属于此解空间，
再用 §2 的准确首项定标，就得到 (2)、(3) 的整条恒等式。
这里的一个模素数子式只是特征零非零证书，不承担跨素数非消失结论。

## 5. 真 sigma 乘积与原周期

标准 division 恒等式为
$$
\begin{aligned}
\sigma(3\delta z)&=3\delta\,\sigma^{27}xQ_4(X),\\
\sigma(2z)&=-2y\sigma^4,\qquad
\sigma(4z)=-4y\sigma^{16}R_2(X),\\
\sigma(\delta z)&=\delta x\sigma^3.
\end{aligned}
\tag{24}
$$
因此
$$
H_{38,b}=\sigma^{38}xQ_4(X)R_2(X).
$$
结合 R297 的同一 $S_b$，直接得到 (4)。
R333 的原六 sigma 身份
$$
S_b=-\frac{\sigma(z)\sigma(2z)\sigma(\delta z)\sigma(2\delta z)
             \sigma(\gamma z)\sigma(\bar\gamma z)}{84}
$$
再给 (5)。其六个首项之积为
$\delta\cdot2\delta\cdot3\delta\cdot4\cdot7=-504\delta$，
准确验证首项一及整体符号。

$H_{38,b}$ 的两个因子分别有除子
$E[3\delta]\setminus\{O\}$ 和 $E[4]\setminus E[2]$，
次数为二十六和十二；这是真实固定二、三挠来源，质量一。
它不是把未知参考导数设为零的“单位”。

现在令
$$
\vartheta=(24/17)^{1/6}>0,\qquad
\Omega_{24}=\vartheta^{-1}\Omega_{17}.
$$
准确同构为
$$
x_{24}(z)=\vartheta^2x_{17}(\vartheta z),\quad
y_{24}(z)=\vartheta^3y_{17}(\vartheta z),\quad
\sigma_{24}(z)=\vartheta^{-1}\sigma_{17}(\vartheta z).
$$
因 $S_b,T_b$ 均是六个 sigma 的乘积，而 $H_{38}$ 是其真实商，
$$
\boxed{
T_{24}(z)=\vartheta^{-6}S_{17}(\vartheta z)H_{38,17}(\vartheta z),
\quad
\Phi_{24}(z)=-102816\sqrt[3]9\,
 S_{17}(\vartheta z)H_{38,17}(\vartheta z).
}
\tag{25}
$$
这里不能把 $b=24$ 的 $S_b$ 直接称作原有理 $E_{17}$ 的来源；
(25) 已支付它们之间的实际变量和标量。

## 6. 同一普通测度的完整中央关系

固定 $p>7$、$p\equiv1\pmod3$、$p\ne17$，
取同一个包含 $\vartheta,\sqrt[3]9$ 的完成。
选择相容正式群同构，使
$$\Omega_{p,24}=\vartheta^{-1}\Omega_{p,17}.$$
这是实际曲线同构诱导的周期选择，不是在
$\mathbf Z_p$ 的测度变量上任意乘一个不在 $\mathbf Z_p$ 的代数数。

用原 $E_{17}$ 周期定义 $\nu_S,\nu_H$，其 Amice 变换分别是
$S_{17}(\Omega_{p,17}\log(1+Z))$、
$H_{38,17}(\Omega_{p,17}\log(1+Z))$。
由 (24) 及普通 sigma 整性，它们都是有界整测度，
$\nu_H(\mathbf Z_p)=1$。
令 $c_*=-102816\sqrt[3]9$，则 (25) 给**完整测度身份**
$$
\boxed{\nu_{\Phi_{24}}=c_*\,(\nu_S*\nu_H).}
\tag{26}
$$
$c_*$ 在这里为单位。
两曲线各自的 $\pi_{24}/\pi_{17}$ 有限角色仍须在各自 core 中保留；
(26) 来自同一正式群参数，不以“相同 core”替代来源身份。

记
$$
\ell_p(x)=\frac{\log_p\langle x\rangle}{\log_p(1+p)},\qquad
K_T(x)=\mathbf1_{x\in\mathbf Z_p^\times}(1+T)^{\ell_p(x)},
$$
并将 $K_T$ 在非单位处定义为零。
R397 的同一个中央行准确满足
$$
\boxed{
G_{24,p}(T)=c_*\iint K_T(x+y)\,d\nu_S(x)d\nu_H(y).
}
\tag{27}
$$
因为 $\nu_H$ 的总质量是一，与原 $G_{17,p}$ 的完整差为
$$
\boxed{
G_{24,p}(T)-c_*G_{17,p}(T)
=c_*\iint\bigl(K_T(x+y)-K_T(x)\bigr)\,d\nu_S(x)d\nu_H(y).
}
\tag{28}
$$
这包含 $x,y$ 各自的所有环带、非单位相加变单位，以及单位相加
变非单位的全部补域。没有以输入单位条件替换输出单位条件。
原导数直接由同一有界核求得：
$$
G_{24,p}'(0)-c_*G_{17,p}'(0)
=c_*\iint
\left(\mathbf1_{x+y\ {\rm unit}}\ell_p(x+y)
      -\mathbf1_{x\ {\rm unit}}\ell_p(x)\right)d\nu_Sd\nu_H.
\tag{29}
$$
两条总中央质量都因其固定 rank-two 曲线为零；
这不使 (29) 的相加对数余项自动消失。

还有一个不引入商测度的共同六输入表达。
在同一 $E_{17}$ frame 中，取 $\mu=\nu_\sigma^{\otimes6}$，
$$
\begin{aligned}
L_{17}(\mathbf x)&=\delta x_1+2\delta x_2+\gamma x_3+
                  \bar\gamma x_4+x_5+2x_6,\\
L_{24}(\mathbf x)&=\delta x_1+2\delta x_2+\gamma x_3+
                  \bar\gamma x_4+3\delta x_5+4x_6 .
\end{aligned}
$$
则
$$
\boxed{
\nu_S=-\frac1{84}(L_{17})_*\mu,\qquad
\nu_{\Phi_{24}}=\frac{12\cdot17\sqrt[3]9}{\delta}(L_{24})_*\mu .
}
\tag{30}
$$
所有六个 sigma 都保原零质量；每个中央观察必须仍带
$\mathbf1_{L_i(\mathbf x)\ {\rm unit}}$ 及其完整对数。
(30) 是两条已付固定 rank-two 来源的实际共同输入，
不是从六因子可交换推出两个 Mellin 导数相等。

## 7. 一个直接有限推论：E24 秩恰二，七初级有限

在 $b=24$，(2) 给
$$v_7(6!\,s_6)=v_7(6!a_{24})=1<2.$$
这准确命中 R397 的同一有限证书 $p=7,n=0$。
该篇在七处的扩展无额外假设：
好普通 sigma 和原整来源有效，ray 次数 $432$ 与辅助中心因子
$-30$ 都是七单位，三同源及二次下降的次数也与七互素；
R400 已支付本处全部 Katz 分支和原 core。
故其通常全 Selmer 不等式在七处同样适用，得到
$$
\boxed{\operatorname{rank}E_{24}(\mathbf Q)=2,\qquad
       \Sha(E_{24}/\mathbf Q)[7^\infty]\text{ 有限}.}
\tag{31}
$$
这里不只是 Mordell–Weil 高度结论，也没有删潜在 Sha 方向。
它是一个固定素数的完整结果，未提供无穷多个素数。

## 8. 可复现证书与后续实际问题

- [精确脚本](../scripts/check-e24-original-degree72-cm7-source.js)
  只使用 JavaScript 内建 BigInt 实现 $\mathbf Q(\delta)$ 分数；
  可直接用 Node 运行，无依赖、网络或文件读写。
- [完整输出](../scripts/check-e24-original-degree72-cm7-source.json)
  保存十三个全部纤维的准确 trace、(23) 的矩阵和子式，
  以及两个固定多项式因式分解、三挠首项的有理约简证书。

13 个特征零纤维证明候选的完整 eigen 身份；
一个有限子式证明指定解空间只有一维。
三挠点公式单独证明实际整体常数。
三者分工明确，不用数值近似或素数样本证明身份。

下一步可以使用 (28)–(30)，对同一无限普通素数集合研究两条
实际中央导数的联合非零，或利用固定 $H_{38}$ 的 Riemann 身份
控制 (29) 的完整余项。仅有 $H_{38}(0)=1$、固定挠除子、
整测度 primitive 性或一个有限证书，均未使该余项消失。
原主目标仍未完成。

直接依赖：
[R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)、
[R395](R395-e24-six-actual-translates-fixed-divisor-and-square-normalization.md)、
[R397](R397-e24-original-ordinary-square-and-full-selmer-bridge.md)、
[R400](R400-full-square-interpolation-determines-core-and-e24-cmseven-phase.md)。
全部新代数、相位和纤维比较在本篇或旁列完整脚本直接证明。

提交前 API main 为 $f36dcc08d4388beaa00222e619a1e92db023444b$，
两份 README blob 与已读版本相同。
当前没有可用 shell；本篇按根规矩八使用小文本 Contents API，
不是一次本地 git pull。
