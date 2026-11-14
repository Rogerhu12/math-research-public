# R422 — 原双对角因子、整商与四输入的完整返回

日期：2026-11-14。**状态：已证明。** 对 R420 的实际来源
$\Xi=\rho_0-\rho_1+\rho_2$，在正确的双 $[2]$ 覆盖上构造
$$
\Xi(2u,2v)=\sigma(u-v)\sigma(u+v)Q(u,v),\qquad
Q\in\mathcal S_{134}\boxtimes\mathcal S_{150}.
$$
商具有整有界 Amice 测度，并给原 $S$ 的完整四输入卷积返回。
两个零输出分别由一个独立 sigma 输入的零质量解释，不能据此把
任意混合受限域设成零。主目标仍未完成。

## 1. 同一实际向量及两条完整零对角

固定 R416、R419、R420 的同一 $E_{17}$ 物理周期、普通 ray 和来源
$S,L,T=SL$。在原输出 $(Y,X)$ 的对偶变量 $(y,v)$ 中，记
$$
F_0=S(y)L(v),
$$
$$
F_1=\frac14\sum_{t\in E[4]}S_t(y)L_t(v)
                  -\frac12\sum_{t\in E[2]}S_t(y)L_t(v),
\qquad
F_2=-\frac14\sum_{t\in E[4]}S_{-t}(y)L_t(v).
\tag{1}
$$
$F_2$ 是含完整中心符号的真实第三态。以下准确使用
$\Xi=F_0-F_1+F_2$；它不同于共同特征态 $F_0-F_1-F_2$，后者在
反对角上的值为 $2T$，不能使用本篇的双因子。

二挠项相消后，实际向量为
$$
\boxed{\Xi(y,v)=S(y)L(v)-\frac14
\sum_{t\in E[4]\setminus E[2]}
             \{S_t(y)+S_{-t}(y)\}L_t(v).}
\tag{2}
$$
偶来源的原 lift 满足 $S_t(-y)=S_{-t}(y)$、$L_t(-v)=L_{-t}(v)$。
在 (2) 换 $t\mapsto-t$，得到每条轴分别偶。
又因 $L(t)=0$ 对全部四挠非二挠点，$L(0)=1$，有
$$
\boxed{\Xi(-y,v)=\Xi(y,-v)=\Xi(y,v),\qquad\Xi(y,0)=S(y).}
\tag{3}
$$
特别 $\Xi\ne0$。

R419 已分别证明
$\sum_{E[4]\setminus E[2]}S_{-t}L_t=0$ 和 $\sum_{E[2]}T_t=0$。
原 $K_{72}T=T$ 与 R416 的四挠公式又给
$\sum_{E[4]\setminus E[2]}T_t=4T$。
代入 (2)，再用第二变量偶性，得到整条来源身份
$$
\boxed{\Xi(z,z)=\Xi(z,-z)=0.}
\tag{4}
$$
这里两条都是实际线性输出的完整推前零，不只是原点质量零。

## 2. 正确双覆盖上的全局商

四挠单项带有混合二挠平坦 twist，故不能先放进原 untwisted
degree $34\boxtimes38$。保持真覆盖
$$
\mathcal X(u,v)=\Xi(2u,2v)
\in\mathcal S_{136}\boxtimes\mathcal S_{152}.
\tag{5}
$$
R420 给准确 lift
$S_t(2u)=T_{t/2}^{(136)}S(2u)$、
$L_t(2v)=T_{t/2}^{(152)}L(2v)$，并由实际完整 core 证明 (5) 的
整张量格及整 Amice 测度。

置 $\Sigma(u,v)=\sigma(u-v)\sigma(u+v)$。
它的完整 Gram 为 $\operatorname{diag}(2,2)$；两轴 sigma 半特征
各自相乘为一，交叉 Gaussian 相消，所以
$\Sigma\in\mathcal S_2\boxtimes\mathcal S_2$，无平坦 twist。
零除子是 $u=v$、$u=-v$ 两条光滑椭圆曲线，各重数一；它们在
四个二挠交点横截。

由 (4)，$\mathcal X$ 沿这两条除子都消失。在交点的正则局部环中，
两条不同素因子同时整除就使其乘积整除；不必预设任一条二重零。
因此存在唯一全局全纯商
$$
\boxed{\mathcal X=\Sigma Q,\qquad
Q\in\mathcal S_{134}\boxtimes\mathcal S_{150}.}
\tag{6}
$$
其边界准确为
$$
\boxed{Q(u,0)=S(2u)/\sigma(u)^2=64u^4+O(u^{10}).}
\tag{7}
$$
$Q$ 分别偶，且在共同 CM 单位下满足
$Q(\zeta u,\zeta v)=\zeta^4Q(u,v)$，因为原 $\Xi$ 的共同权为零、
$\Sigma$ 的共同权为二。因此商至少四阶消失，而 (7) 证明它非零。

## 3. 正式群坐标中的整除，保有界性

令 $\Omega=\Omega_p$ 为原普通单位周期，
$u=\Omega\log(1+U)$、$v=\Omega\log(1+V)$。
R316 的实际 sigma 整性和单位首导数给
$$
\mathcal A_\sigma(Z)=\sigma(\Omega\log(1+Z))
=\Omega Z h(Z),\qquad h\in\mathcal O[[Z]]^\times.
$$
所以 (6) 的两个因子准确为
$$
\sigma(u-v)=(U-V)\cdot\text{整单位},\qquad
\sigma(u+v)=(U+V+UV)\cdot\text{整单位}.
\tag{8}
$$
它们分别使用正式群差 $(U-V)/(1+V)$ 与和 $U+V+UV$。
这里没有直接除含分母的 log Taylor 级数。

记 $F(U,V)\in\mathcal O[[U,V]]$ 为 (5) 的 Amice 变换。
$F(U,U)=0$ 先给整除 $F=(U-V)G$。
反对角是 $V=-U/(1+U)$；此处
$$
U-V=U(2+U)/(1+U)
$$
为非零元。系数环是整环，故 $G(U,-U/(1+U))=0$。
按对 $V$ 首一的方程 $V+U/(1+U)$ 再作整除，得到
$$
G=(U+V+UV)H,\qquad H\in\mathcal O[[U,V]].
\tag{9}
$$
结合 (8)，$Q$ 的 Amice 级数仍在 $\mathcal O[[U,V]]$，所以确为
整有界二变量测度，不仅是在小圆盘上收敛的函数。

全局整性也返回同一 theta 格：对 $N=134,150$，原基
$$
\{\sigma^Nx^i:0\le i\le N/2\}
\cup\{\sigma^Nyx^j:0\le j\le N/2-2\}
$$
在正式群参数中首阶互异且首系数为单位。在其张量基中按首阶消元，
(9) 使每个全局系数都整；不除任何高阶阶乘。
由 (7)，$[U^4V^0]\mathcal A_Q=64\Omega^4$ 是单位，因此商仍为
primitive。本篇不将这个正矩非零替换成中央非零。

## 4. 同一物理周期中的完整四输入返回

令 $\nu_Q$ 的两个输出为 $(r,s)$，另取原
$\nu=\nu_{\sigma,17}$ 的两个独立输入 $a,b$。
在同一 $\Omega_p$ 中，(6) 的 Amice 单射给
$$
\boxed{[2,2]_*\nu_\Xi
=\bigl(r+a+b,\ s-a+b\bigr)_*
       (\nu_Q(r,s)\otimes\nu(a)\otimes\nu(b)).}
\tag{10}
$$
方向是左边的真正 $[2,2]$ 推前；右边没有再放大一次。
返回原两个输出时，准确使用
$$
\boxed{(Y,X)=\left((r+a+b)/2,\ (s-a+b)/2\right).}
\tag{11}
$$
$(r,s)$ 的完整联合保留，不能将其换成两个边际的张量。
原 $Y$ 推前由 (3) 恰为 $\nu_S$。

另两个输出是
$$
W=Y+X=(r+s+2b)/2,\qquad
V=X-Y=(s-r-2a)/2.
\tag{12}
$$
$W$ 与 $a$ 无关、$V$ 与 $b$ 无关，而原 sigma 质量为零，故
$$
\boxed{W_*\nu_\Xi=0,\qquad V_*\nu_\Xi=0.}
\tag{13}
$$
这是对任意连续测试、所有 tame、单位／非单位和输出环带的完整零。
它也解释了两个零的确切来源，没有使用未知的中央结论。

对任意 tame $\ell$ 和 principal 变量 $z$，整个原目标返回为
$$
\boxed{
J_{S,\ell}(z)=\int
\mathbf1_{r+a+b\in\mathbf Z_p^\times}
\omega_p\left((r+a+b)/2\right)^\ell
\left\langle(r+a+b)/2\right\rangle^{(p-1)z}
\,d\nu_Q\,d\nu(a)\,d\nu(b).}
\tag{14}
$$
所有相加输出的边界和补域都保留，尺度 $1/2$ 没有省略。
在 principal 中央一阶，原 $J_S(0)=0$ 使单独的
$\log_p\langle2\rangle$ 质量项为零；其他分支仍使用完整 (14)。

同一个原 sigma 加法还给
$$
\Sigma(u,v)=\sigma(u)^2\Theta(v)-\Theta(u)\sigma(v)^2,
\qquad\Theta=x\sigma^2.
\tag{15}
$$
这可用原质量一的 $\Theta$ 表达相同来源，但不使这些加法卷积的
Mellin 函数变成乘积。

## 5. 真实二挠平均与不能免费下降的除子

在第一覆盖轴取原平均
$\mathcal E_{136}=\frac14\sum_{h\in E[2]}T_h^{(136)}$。
$S(2u)$ 是真正 $[2]$ 拉回，被所有这些 lift 固定。
但四挠非二挠 $t$ 的
$S_t(2u)=T_{t/2}^{(136)}S(2u)$ 带非平凡二挠特征：原 Heisenberg
交换子就是与非零 $2t$ 的二挠配对，且 $136/8=17$ 为奇数。
因此 (2) 的全部四挠项都被平均杀掉，准确有
$$
\boxed{(\mathcal E_{136}\otimes I)\mathcal X=S(2u)L(2v).}
\tag{16}
$$
在对角上，由 $\mathcal X(u,u)=0$ 得到完整来源关系
$$
\boxed{\sum_{h\in E[2]\setminus\{0\}}
(T_h^{(136)}\otimes I)\mathcal X(u,u)=4T(2u).}
\tag{17}
$$
这里每个 lift 的原指数都保留。
因为 $T\ne0$，三个平移对角不可能全部为零。
所以不能把 (6) 的因子无证换成
$\sigma(2u-2v)\sigma(2u+2v)$，也不能免费下降为原 degree
$32\boxtimes36$。式 (16)、(17) 本身是完整测度及全部 tame 的
真实回接，但仅约束显示的总和，不分别赋零给各项。

## 6. 到原独立深度域尚须保留的条件

R339 的非零域是指定原 sigma／Theta 表示中各输入的独立深度域。
(10) 只有两个独立 sigma 输入，剩下的 $\nu_Q$ 是实际二输出联合，
尚未识别为 R339 的那些输入与二次权。
尤其 (13) 只在相应独立 sigma 输入取整个空间时由零质量消去；
附加其单位、深度或混合输出条件后，不能继续免费使用该消去。
后续运输须保持 (10)–(14) 的原输出、原周期和完整补域。

依赖：

- [R316：原 sigma 整性和单位首导数](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R419：四挠及二挠完整消失](R419-original-opposite-quarter-translates-and-zero-new-total-marginal.md)。
- [R420：真实第三态、整核心及和差边际](R420-original-three-state-y-w-core-with-full-central-phase.md)。
- [R339：原独立深度域与实际非零输入](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)。
