# R791：原 Hom 的真实 Galois 下降、完整迹零输入与全部非零方向的 CM 不分歧

日期：2026-11-15。状态：**下述精确计算及其数学推论已证明。**
全部新算术来自公开仓库 [Actions run 43686308194](https://github.com/Rogerhu12/math-research-public/actions/runs/43686308194)。
本地只读取已有产物、核 SHA 并作纸面推导，没有本地数学运行。
完整预运行证明见 [R791 方法](../notes/R791-original-Hom-Galois-and-eta-divisor-method.md)。

## 1. 此次实际得到什么

保持 R759 的原十二维完整整数 Hom 格、原 $\omega_0,\ldots,\omega_5$、
原 $c_0,c_1$、原正目标 $C/L:y^2=x^3+b$，以及原选定的第 4 号映射
$f=f_4$、$\deg f=1206$。此次完成：

- 原 $\gamma$、复共轭和 $\zeta$ 在整个原整数 Hom 格上的准确矩阵；
- 原第 4 号映射的真实实下降及其次数；
- 原极化尺度 $\kappa v^\dagger v$ 的准确六个实域坐标；
- 原 $F^0$ 的全部五个方向、其加法映射次数和准确零次数系数；
- 原十二个实际同态微分在 $c_1$ 的完整 $L$ 切向坐标，全部非零。

由真实实下降关系进一步得到：原 $f_R$ 是原 $f$ 的一个明确三次 CM
自同源后合，因此其 $y$ 函数和极除子直接由原 $y$ 给出。
另在 §6 证明整个非零原 $L$-Hom 空间的 CM 切向都不为零，
而非仅从十二个基向量推测任意组合。

这里仍未求出 $Y$ 上实际极除子、$\eta_h$ 的 Jacobian 坐标、
$\ker\eta$ 的非零元、原 $\beta$ 点坐标或高度。

## 2. 准确的 21 阶作用与实际实下降

记 $\mathcal H$ 为 R759 的原整数 Hom 格，列基仍是
$f_0,\ldots,f_{11}$。原 $\gamma=7+30\zeta$、$\sigma=\sigma_\gamma$
及 $\rho=\sigma(r)/r$ 直接读自成功 R754 阶段。
对 $u\in\mathcal H$，真实作用为

$$
\mathcal T(u)=D_{\rho^{-1}}\sigma(u),\qquad
D_a(x,y)=(a^2x,a^3y).
\tag{791R.1}
$$

因为原六微分在 $\mathbf Q$ 上定义，微分列的准确作用是
$v_j\mapsto\rho\sigma(v_j)$。复共轭固定原 $b$，将
$a(b)+d(b)\zeta$ 送到 $a(b)-d(b)-d(b)\zeta$。
程序在全部 84 个有理坐标中求解并代回，得到整幺模矩阵
$T,R,J$，分别对应 $\mathcal T,c,[\zeta]$。在原两倍次数 Gram
$G$ 上，实际核验

$$
T^7=J^2,\quad T^{21}=I,\quad RTR=T^{-1},\quad
RJR=J^2,\quad TJ=JT,
$$
$$
T^tGT=R^tGR=J^tGJ=G.
\tag{791R.2}
$$

此外 $\Phi_{21}(T)=0$；$S=T+T^{-1}$ 的实际最小多项式为

$$
\Psi_{21}(Z)=Z^6-Z^5-6Z^4+6Z^3+8Z^2-8Z+1.
\tag{791R.3}
$$

实、反实 Hom 子空间各为六维。$I,T^j+T^{-j}$，$1\le j\le5$，
准确独立。它们对应原本原因子的
$F=\mathbf Q(\zeta_{42})^+=\mathbf Q(\zeta_{21})^+$。
原剩余 $A_6$ 椭圆因子没有进入这些矩阵；其 $T$ 多项式是
$\Phi_3$，而非 $\Phi_{21}$。这次原 $\gamma$ 的作用确为 21 阶，
未改成另一份 42 阶生成元。

实际复共轭结果是

$$
c(f_4)=-f_6,
\qquad [\zeta]f_4+[\zeta^2]c(f_4)=0.
\tag{791R.4}
$$

第二式准确推出 $c(f_4)=-[\zeta^2]f_4$，故

$$
\boxed{
f_R=f_4+c(f_4)=f_4-f_6=[1-\zeta^2]f_4,
\qquad \deg f_R=3618.}
\tag{791R.5}
$$

原 $f_4$ 自己不在 $L^+=\mathbf Q(b)$ 上定义；$f_R$ 在 $L^+$
上定义。候选 $[\zeta]f_4+[\zeta^2]c(f_4)$ 的实际次数为零，
确为零映射，未被当作另一条非零方向。

Weil restriction 给真实 $\mathbf Q$ 同态
$q_R:J_X\to B=\operatorname{Res}_{L^+/\mathbf Q}C$。
R728 的完整同源分解和原 Hodge 空间给
$q_R=vq$，其中 $v:A\to A_{42}^{\mathrm{mod}}$ 为实际有理同源。
原 $q$ 与其极化不变；没有用 $B$ 的第七维形成伪造的核。

## 3. 原三次 CM 同源的准确函数与极除子

为区别粗参数，记 $\varsigma=1+2\zeta=\sqrt{-3}$、
$\alpha_3=1-\zeta^2$，则
$\alpha_3\overline\alpha_3=3$、$\alpha_3^3=3\varsigma$。
原 $f=(x,y)$ 以及 $f_R=(x_R,y_R)$ 满足

$$
\boxed{
x_R=-\frac{\zeta x(y^2+3b)}{3(y^2-b)},\qquad
y_R=\frac{y(y^2-9b)}{3\varsigma(y^2-b)}.}
\tag{791R.6}
$$

**证明。** $[\zeta^2]P=(\zeta^2x,y)$，故
$[\alpha_3]P=P-[\zeta^2]P$。这两点之间的斜率是
$2y/(\alpha_3x)$。椭圆加法给
$x_R=4y^2/(\alpha_3^2x^2)-(1+\zeta^2)x$。
使用 $\alpha_3^2=-3\zeta^2$ 和 $x^3=y^2-b$，化成第一式。
再代入 $y_R=-y+(2y/(\alpha_3x))(x-x_R)$，并用
$\alpha_3\varsigma=3\zeta$，得到第二式。
这是稠密开集上的恒等式，因而给整个椭圆曲线上的同源。
它的微分倍数正是 $\alpha_3$，没有再选立方根方向。$\square$

由原 $\mu_3$ 等变性，$y,y_R$ 都是 $Y_L$ 上的实际函数。
设 $E_y=(y)_\infty$。因为 $b\ne0$，在 $y^2=b$ 时，
第二式分子为 $-8by\ne0$；而在 $y$ 的极点，
$y_R\sim y/(3\varsigma)$。因此没有取消，准确有

$$
\boxed{(y_R)_\infty=E_y+(y^2-b)_0.}
\tag{791R.7}
$$

其次数为 $1206+2\cdot1206=3618$，与实际 Hom Gram 的结果一致。
这给 R787 原单个函数 $y=A/B$ 的直接后继：本次实下降所需的
$y_R$ 及极除子 recipe 完全不必先恢复 $x$ 或实施一般两点加法。
式 (791R.7) 是完整除子恒等式；没有声称其零点/闭点坐标已经生成。

## 4. 原极化尺度与完整 $F^0$ 的真实次数表

所有 adjoint 保留原极化。置

$$
\kappa=qq^\dagger,
\qquad M_v=v^\dagger v
 =\lambda_A^{-1}v^\vee\lambda_Bv.
$$

将 $\mathcal T$ 从 $A_{42}^{\mathrm{mod}}$ 经实际 $v$ 运输到 $A_K$，
记为 $t$，并记 $s_j=t^j+t^{-j}\in F$。
方法 (791.12) 从原次数 Gram 恢复真实 CM Hermitian 配对
$uw^\dagger$；(791.14) 进而计算 $q_R^\dagger q_R$。
此次得到的原 $F$ 元素为

$$
\boxed{
e:=\kappa M_v
=3870+711s_1-801s_2-360s_3+612s_4+864s_5.}
\tag{791R.8}
$$

这不是一个未知的纯标量。程序准确验证其原 Hom 矩阵非奇异、
Rosati 自伴、与 $T,R,J$ 交换，并有

$$
\operatorname{Tr}_{F/\mathbf Q}e=25326=7\deg f_R.
\tag{791R.9}
$$

尤其不能把 $\kappa$ 或 $M_v$ 设为一；单独写 $M_v$ 时，
准确公式仍是 $\kappa^{-1}e$。

令 $f_B=q_R[x-c_0]$，使用 R728 的实际分量 theta 除子。
按方法 (791.16)，

$$
D_0=f_B^*\Theta_B,\qquad
D_j=((1+\mathcal T^j)f_B)^*\Theta_B-2D_0.
$$

其中 $d_0=\deg D_0=25326$。
其余真实输出如下，全部次数来自同一个原 $G$，没有数值拟合：

| $j$ | $\deg(f_R+\mathcal T^jf_R)$ | $d_j=\deg D_j$ | $r_j=d_j/d_0$ |
|---:|---:|---:|---:|
| 1 | 8910 | 11718 | $31/67$ |
| 2 | 5022 | $-15498$ | $-41/67$ |
| 3 | 5400 | $-12852$ | $-34/67$ |
| 4 | 9072 | 12852 | $34/67$ |
| 5 | 10017 | 19467 | $103/134$ |

定义原 $F$ 中的五个元素

$$
\boxed{h_j=\kappa^{-1}e(s_j-r_j),\qquad1\le j\le5.}
\tag{791R.10}
$$

它们是原
$F^0=\ker\operatorname{Tr}_{F/\mathbf Q}(\kappa\,\cdot)$
的完整基。证明不仅是维数计数：$1,s_1,\ldots,s_5$ 是同一个
本原实域的基，$e\ne0$ 可逆，$\operatorname{Tr}e=d_0\ne0$，
而真实次数公式给
$\operatorname{Tr}(es_j)=d_j$。故五个差恰张成该非零泛函的核。
此次还在原十二维坐标中直接验证

$$
\kappa h_j\longleftrightarrow
E(T^j+T^{-j}-r_jI)
\tag{791R.11}
$$

的准确迹零、Rosati 自伴和秩五。
这里 $E$ 是 (791R.8) 的矩阵。原 $q,\alpha,c_0,c_1$ 与高度规范
均保持不动。

## 5. 原 η 的准确除子输入与所余接口

对任一实际 $\delta$ 等变映射 $g:X\to C_\tau$，记
$P_g=(y_g)_\infty$ 为其商函数在 $Y$ 的极除子。
椭圆 $y$ 的三阶极点和 $\phi$ 的次数三给

$$
\phi^*P_g=3g^*[O],\qquad
\phi_*g^*[O]=P_g.
\tag{791R.12}
$$

因此原 R593 的 $\eta_h=\frac13\phi_*j_A^*\mathcal L_h$ 准确为

$$
\boxed{
\eta_{h_j}=\frac13\left[
\sum_{\tau\in\operatorname{Gal}(L/K)}
 P_{f_{R,\tau}+(\mathcal T^jf_B)_\tau}
 -(2+r_j)\sum_\tau P_{f_{R,\tau}}
\right].}
\tag{791R.13}
$$

式中 $r_j$ 就是上表的真实有理数，$1/3$ 仍保留。
对称 Poincaré 加法公式给 $j_A^*\mathcal L_{h_j}=D_j-r_jD_0$；
其 Picard 零次项未删去。
Galois 下降使用 $D_{-j}=D_j$ 与 $c\mathcal Tc=\mathcal T^{-1}$，
所以该零次数类确在原 $J_Y(\mathbf Q)\otimes\mathbf Q$ 中。

还可利用此次实际得到的同一个三次自同源，把所需除子次数减少。
令 $\widetilde f_B=(f_\tau)_\tau$ 是原 $f=f_4$ 的 Weil 分量映射，
先只在 $K$ 上使用；不声称它在 $\mathbf Q$ 上定义。
置

$$
g_{\tau,j}=f_\tau+(\mathcal T^j\widetilde f_B)_\tau.
$$

$\mathcal T$ 与 $[\alpha_3]$ 交换，所以 (791R.13) 的第一组
映射恰是 $[\alpha_3]g_{\tau,j}$，第二组是 $[\alpha_3]f_\tau$。
对任何同靶 $g$，(791R.7) 以及函数 $y_g^2-b$ 的完整主除子给

$$
P_{[\alpha_3]g}
=P_g+(y_g^2-b)_0
=3P_g+\operatorname{div}(y_g^2-b).
\tag{791R.13a}
$$

因此对 **同一个 (791R.10) 的 $h_j$**，准确有

$$
\boxed{
\eta_{h_j}=\left[
\sum_\tau P_{g_{\tau,j}}-(2+r_j)\sum_\tau P_{f_\tau}
\right].}
\tag{791R.13b}
$$

这里 $1/3$ 与已经证明的 $\deg[\alpha_3]=3$ 精确抵消，
没有约掉未知整数，也没有将原 $h_j$ 换成 $h_j/3$。
这些较小的实际加法映射次数依次为

$$
2970,\quad1674,\quad1800,\quad3024,\quad3339;
\tag{791R.13c}
$$

它们由上表已算次数和三次同源的次数乘法公式直接推出。
现在第二和只需要原 $E_y$ 的七个共轭。

消去仅在 Picard 类中进行，主函数的规范须保留。
确切地，写 $r_j=a_j/b_j$ 为上表的既约分数、$b_j>0$，则
所去掉的主除子在清除 $b_j$ 后由实际函数

$$
\mathcal R_j=
\frac{\displaystyle\prod_\tau
 (y_{g_{\tau,j}}^2-\tau b)^{b_j}}
 {\displaystyle\prod_\tau
 ((\tau y)^2-\tau b)^{2b_j+a_j}}
\tag{791R.13d}
$$

给出：将 (791R.13) 方括号内除子乘 $b_j$，恰等于
(791R.13b) 方括号内除子的 $3b_j$ 倍加
$\operatorname{div}\mathcal R_j$。
实际线丛截面或 Poincaré 局部高度的计算必须沿这个函数运输，
包括其零极点和常数规范，不能因为 Jacobian 类相同就删去它。
原 $\kappa$、$e$ 和五个 $h_j$ 仍是 §4 中的原对象。

后继可直接消费 R787 原 $A/B$，按原 $\sigma$ 和 $\rho$
形成各共轭函数，并可按 (791R.13b) 使用较小的原映射。
一般加法使用方法 (791.24)–(791.25)
的原微分比例。**当前缺的是原 $Y$ 的函数域或 Riemann–Roch 除子
实现，以求完整极除子并计算其 Jacobian 类。**
上述 formula 和完整五维输入没有预先决定这些类是否为零，
也没有把 $h_j$ 误称为 $\ker\eta$ 元素。

## 6. 原十二个实际 CM 切向值，以及全部非零 Hom 的不分歧

R748 的原成功证书明确绑定 R745 微分和一次 $c_1$ slash。
在原粗参数 $z=a-1$ 下，六个值是

$$
(t_0,\ldots,t_5)=
\left(\frac{43719}{11767},\frac{200187}{23534},
\frac{162558}{11767},\frac{687471}{23534},
\frac{659397}{11767},\frac{2521233}{23534}\right).
$$

此次对原十二组 $L$ 系数 $v_{ij}$ 准确求得

$$
\lambda(f_i)=
\left.\frac{f_i^*(dx/(2y))}{dz}\right|_{c_1}
=\sum_{j=0}^5v_{ij}t_j\in L.
\tag{791R.14}
$$

十二个零标志均为 `false`；尤其原 $f_4$ 和实际 $f_R$ 在
$c_1$ 都不分歧。原全部 $L$ 坐标保在同次临时阶段，SHA 见 §7；
没有将这些可重算大坐标写入 Git，也没有重复乘 $\zeta^2$。

**定理 791.1。** 令 $V=\mathcal H\otimes_{\mathbf Z}\mathbf Q$，
赋予原 CM 域 $K$ 作用。对每个 $0\ne u\in V$，都有
$\lambda(u)\ne0$。因此每个非零实际原 $L$ 同态对应的曲线映射
在 $c_1$ 不分歧。

**证明。** $\dim_KV=6$，且 $T$ 与 $K$ 作用交换。
实际 $T^7=[\zeta^2]$ 和 $\Phi_{21}(T)=0$ 选择
$\Phi_{21}$ 在 $K$ 上的一个六次不可约因子。
具体是
$P(U)=(U^7-\zeta^2)/(U-\zeta^2)$：其根是满足
$\xi^7=\zeta^2$ 的原 21 阶本原根；它们在固定 $K$ 的圆分 Galois
群下形成六元单轨道。因此 $K[T]\simeq K[U]/P(U)$ 为六次域，
$V$ 是其秩一模。

R711 给 $c_1\in X(\mathbf Q)$，$z=a-1$ 是该点的 $\mathbf Q$
有理一次参数。故 (791R.1) 在切向上准确给

$$
\lambda(Tu)=\rho\sigma(\lambda(u)).
\tag{791R.15}
$$

$\lambda:V\to L$ 是 **$K$ 线性**，所以其核是 $K[T]$ 子模，
只能是零或整个 $V$。R728 给 $A_L\sim C^6$，于是原六维
$K$-Hom 微分在 $L$ 上张成整个 $q^*H^0(A_L,\Omega^1)$。
若 $\lambda$ 恒零，则该整个 Hodge 空间在 $c_1$ 的评价恒零。
但 R748 已准确给 $\omega_0/dz(c_1)=43719/11767\ne0$，矛盾。
因此核为零。$\square$

这里没有把 $\lambda$ 当作 $L$ 线性。一般非 CM 标量的 $L$ 线性
微分组合不对应实际同态；因此该结论不与六维 $L$ Hodge 空间上的
标量评价有核相矛盾，也不能仅由“十二个基值非零”推出。

R790 若得到有限原 $y(c_1)$ 且 $y(c_1)^2\ne b$，则
$dy=3x^2h$ 与本定理使原 $y'(c_1)\ne0$，因而

$$
x(c_1)=3\bigl(y(c_1)^2-b\bigr)
          \frac{h(c_1)/dz}{y'(c_1)}
\tag{791R.16}
$$

只需原 $y$ 的一阶粗导数。
若 $y(c_1)^2=b$，则 $x(c_1)=0$；若 $y$ 有极点，则像为 $O$。
这些仍须 R790/R787 的实际函数求值，切向非零本身不提供原 $\beta$。

## 7. 原运行、来源与输出 SHA

| 项目 | 实际记录 |
|---|---|
| run / attempt | 43686308194 / 1 |
| source commit | f945ef5d5aee4d8222dc791e39a0709b661cebbc |
| 核心时间 | 0.117925238 秒 |
| 完成时刻 | 2026-11-15T06:37:55.115774+00:00 |
| 核心退出码、完整状态 | 0，`complete=true` |
| Python-FLINT | 0.9.0 |
| 核心源码 SHA-256 | 11068eb00caa71e9c8ed1ffba0277534a52f5cce3402a59b68c7d5d66a8b7a4d |
| 方法 SHA-256 | 3b13e319fdcee74430d7b7d95b3f011a04f21294c8a5e563020dfc41cb125a75 |
| request SHA-256 | 1e0becef4ad13c7787ea151eee8c7de35e96d9a8fa1d8da232ce9b2e7f43f388 |
| 最终证书 SHA-256 | 94429377ebd63ff8bdcb9fd1d9468fc2e28e981db2b10b8c494d15c05e073d46 |
| 全输出 manifest SHA-256 | 4eeb9ba12e203f41d2525325bf1ae207b46baa2b88ad88b31de2c3ac58a317fc |

正式入口是
`python topics/serre-uniformity/scripts/R791_public_original_Hom_eta_inputs.py compute`，
参数为 [原正式 request](../notes/R791-public-original-Hom-eta-inputs-request.json)。
它只消耗已经成功的 R754 γ 下降、R759 十二个映射/Gram、原模型证书
及 R748 原切向证书；未重算 Miller、周期、Hom 核、HNF 或 LLL。
执行代码见 [原核心](../scripts/R791_original_Hom_galois_and_eta_inputs.py)。

| 实际数学输出 | SHA-256 |
|---|---|
| 原 Hom Galois 矩阵 | f3793ddc7680b718a4448d45587661182986a3558db346ad0a2c9031c8952183 |
| 原实下降与完整 η 基输入 | 24a894163f136a4e8c71b117e373f8fafb66a6e0c94b4efe3f141f78bb39b968 |
| 原十二个 CM 切向坐标 | 32be372f46560ce7cfc0af40666cdc32b39170bfc7b6ec32b92ea747a0629e7e |

临时 artifact 为
`serre-global-R791-original-Hom-Galois-and-eta-inputs-43686308194-1`，
ID 14149997458；ZIP 49237 字节，SHA-256
`6fb047d54956de475299467740b77a94e40755403b45f5a29036925243efc882`。
根会话已核完整 ZIP、全部九个文件及来源绑定。
按根 README 第 15 条，这些可重算输出不提交仓库或 Release；
仅在直接后继使用期间保留一日 Actions 传递副本。

该固定 $p=41$ 计算同时把原 $F^0$ 的全空间落实为真实规范输入，
但真实 $\eta$、高度与全 $p$ 排除仍未完成，主 README 目标保持 OPEN。
