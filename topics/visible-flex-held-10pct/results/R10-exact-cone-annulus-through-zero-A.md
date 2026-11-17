# R10：常斜率平谷上的精确等距锥环带及 A 零穿越

## 结论与范围

固定 `0<w<=0.01` 及任意 `0<r_-<r_+`。存在显式、光滑、嵌入的锥环带族

\[
X_a(r,u)=c+r\gamma_a(u),\qquad
0\le a\le0.01,\quad r_-\le r\le r_+,\quad u\in\mathbb R/(2\pi\mathbb Z),
\]

所有成员的第一基本形式严格相同：

\[
g=(1+w^2)dr^2+r^2du^2.
\]

在 `w=.00358`、振幅从 `0` 增至 `.0088` 的过程中，原 Darboux 根坐标的周向系数 `A` 确实穿过零，曲面、度量及两阶导数保持光滑。若 `r>=.2`，下面的直接估计给整个参数窗口的主曲率绝对值小于 `.77`。这说明 `A>0` 并非一般常斜率平谷等距浸入的几何必要条件。

这里只证明和计算一个有边界的局部环带。没有证明它与现有前缀或振荡深尾的 Cartesian 两侧 2-jets 匹配，也没有由此得到闭曲面族、固定握持区或全局 reach。一般常斜率等距浸入也不自动是这种共顶点锥面。

## 闭球面曲线的精确长度校准

令 `R=sqrt(1+w²)`，并以空间极角 `phi` 先定义

\[
\beta_{a,b}(\phi)=b+a\cos2\phi,\qquad
\widetilde\gamma_{a,b}(\phi)
=R(\cos\beta\cos\phi,\cos\beta\sin\phi,\sin\beta).
\]

其速度及总长度为

\[
v_{a,b}(\phi)=R\sqrt{\cos^2\beta+\beta_\phi^2},\qquad
L(a,b)=\int_0^{2\pi}v_{a,b}\,d\phi.
\]

对每个 `a in [0,.01]`，方程 `L(a,b)=2pi` 在 `(a,.1)` 中恰有一根 `b=b(a)`（`a=0` 时 `b(0)=atan w`）。证明如下。

先看 `b=a`。记 `c=cos2phi`。由 `cos² x>=1-x²`，

\[
\cos^2\beta+\beta_\phi^2\ge1+a^2(3-2c-5c^2)=1+x.
\]

这里 `|x|<=4a²` 且圆周均值 `mean(x)=a²/2`。二阶 Taylor 余项给

\[
\sqrt{1+x}\ge1+\frac x2-
\frac{x^2}{8(1-4a^2)^{3/2}},
\]

故平均速度除以 `R` 至少为

\[
1+\frac{a^2}{4}-\frac{2a^4}{(1-4a^2)^{3/2}}\ge1,
\]

当 `a>0` 严格大于 `1`。而 `R>1`，所以包括 `a=0` 均有 `L(a,a)>2pi`。

在 `b=.1`，有 `.09<=beta<=.11` 及 `|beta_phi|<=.02`，因此

\[
v^2\le(1.0001)(\cos^2(.09)+.0004)<.993<1,
\]

故 `L(a,.1)<2pi`。对 `b>a`，整个圆周有 `0<beta<.11<pi/2`，且

\[
\partial_bv=-\frac{R\sin\beta\cos\beta}
 {\sqrt{\cos^2\beta+\beta_\phi^2}}<0.
\]

于是根存在、唯一；隐函数定理给 `b(a)` 光滑。端点附近也能将公式延拓到开参数邻域，因而这里的光滑不只是单侧连续性。

现在定义真正材料弧长

\[
u(\phi)=\int_0^\phi v_{a,b(a)}(t)\,dt.
\]

它是圆周上的光滑保向微分同胚，满足 `u(phi+2pi)=u(phi)+2pi`。令 `gamma_a(u)=tilde_gamma(phi(u))`。则严格有

\[
|\gamma_a|=R,\quad |\partial_u\gamma_a|=1,
\quad \gamma_a\cdot\partial_u\gamma_a=0.
\]

这一步是真正弧长重参数化，未对 Cartesian 圆周曲线作截断或拟合。

## 等距、嵌入和二阶几何

直接微分：

\[
X_r=\gamma,\quad X_u=r\gamma_u,\quad
X_{rr}=0,\quad X_{ru}=\gamma_u,\quad X_{uu}=r\gamma_{uu}.
\]

因此 `E=R²`、`F=0`、`G=r²`，与 `a` 无关。由于 `r>0`、`cos beta>0`，空间极角 `phi` 区分材料圆周点；固定 `phi` 后的径向距离又区分 `r`，故环带嵌入。正则性由 `|X_r cross X_u|=rR>0` 保证。

取单位法向

\[
n=\frac{\gamma\times\gamma_u}{R}.
\]

它与 `r` 无关。径向和混合第二基本形式都严格为零，唯一非零主曲率为

\[
\kappa_u=\frac{\gamma_{uu}\cdot n}{r}
=\frac{\sin\beta(\cos^2\beta+2\beta_\phi^2)
 +\cos\beta\,\beta_{\phi\phi}}
 {rR(\cos^2\beta+\beta_\phi^2)^{3/2}}.
\]

在整个证明窗口，`|beta|<.11`、`|beta_phi|<=.02`、`|beta_phiphi|<=.04`。若 `r>=.2`，于是

\[
|\kappa_u|
\le \frac{.11(1+.0008)+.04}{.2\cos^3(.11)}<.77.
\]

最后的数值不等式还可用 `cos(.11)>=1-.11²/2` 降为有限有理数比较。

这个保守解析界同时覆盖全部振幅参数，不依赖仅有网格采样的 `.1511` 实测值。中心为锥顶时 `X dot n=0`；平移 `c` 后支撑函数变为 `c dot n`。因 `n_z=cos² beta/sqrt(cos² beta+beta_phi²)>0`，合适的轴向平移可使局部支撑函数正，但尚未支付任何全局拼接/闭合支撑条件。

## 原根坐标中的 A、D、S

以 `z(r,u)=r gamma_z(u)` 为高度，设

\[
P=\gamma_{z,u}/w,\quad T=\gamma_{z,uu}/w,
\quad K=\gamma_z/w-1,\quad
A=1+K+(1+w^2)T,
\]

\[
D=1-w^2(2K+K^2+(1+w^2)P^2),\quad
S=1-w^2P^2.
\]

令 `Q=cos² beta+beta_phi²`，则在整个参数窗口还严格有

\[
D=\frac{(1+w^2)\cos^4\beta}{Q}=(1+w^2)n_z^2>0,
\qquad
S=1-\frac{\cos^2\beta\,\beta_\phi^2}{Q}
\ge1-\beta_\phi^2\ge.9996.
\]

所以这里的 `A` 零穿越没有使真实根式 `D` 或度量余量 `S` 退化。

在 `phi=0` 有 `beta_phi=0`、`beta_phiphi=-4a`，从而

\[
A(0)=\frac{R}{w\cos\beta}
\left(\sin\beta\cos\beta-4a\right).
\]

当 `a=0`，得到原圆锥 `gamma=(cos u,sin u,w)`，故 `A=1`。对指定 `w=.00358,a=.0088` 可严格证明 `b(a)<3a`：在 `b=3a`，由 `cos²x<=1-x²+x⁴/3` 以及 Jensen 不等式，

\[
\frac{L(a,3a)}{2\pi}\le
\sqrt{(1+w^2)\left(1-7.5a^2+\frac{256}{3}a^4\right)}<1.
\]

最后一式直接代入两个有限小数即可用有理数验证。长度对 `b` 严格递减，故根小于 `3a`。于是 `beta(0)=b+a<4a`，且 `sin beta cos beta<beta`，所以 `A(0)<0`。在 `phi=pi/2`，`beta=b-a>0`、`beta_phiphi=4a`，同式给 `A>0`。因此该成员的 `A` 在角上变号，沿振幅族也发生零穿越，而上述嵌入与曲率界始终成立。

## 数值实例及可重算接口

`cone_plateau_model.py` 给出 `ConePlateau(w,amplitude).evaluate(r,u)`，返回 `X,Xr,Xu,Xrr,Xru,Xuu`；所有导数使用解析链式法则，只有长度校准和材料角逆映射使用高精度数值求积/一维求根。

```sh
python cone_plateau_model.py --w .00358 --amplitude .0088 --radius .25 --out cone-plateau.json
```

1024 个材料角的诊断保存在 `cone_plateau_model_summary.json`：`b=.011357061247708786`，长度残差舍入为零，度量误差 `4.44e-16`，`minD=.99953116`、`minS=.99969034`、`minA=-4.20434`，主曲率最大约 `.15103`；高度的 `cos(2u)` 系数约 `.00219980`，与完整 q18 实际接口 H1 的量级接近。它只展示局部振幅可容纳性，不能替代完整多模 H/Hr 和 Cartesian 两侧 2-jets 的匹配。16 模 Gram 的负特征值也说明此前的正定有限 Gram 图无法直接覆盖该终点；原正定/正A求解器不能覆盖这个分支；任何新算法仍须检查原完整方程、D/S、实际Cartesian二jet和极限，不得把删除一个检查条件直接当作几何解。

## 主会话复核

长度、唯一b、材料角链式、全窗口曲率、D/S恒等式与指定A变号均经逐式复核。上述严格比较用 `fractions.Fraction` 独立验证；具体有理数列在 `scripts/nonlinear_tail/cone_plateau_manifest.json`。数值实例只用于展示规模，严格结论依靠本证明的精确定义及不等式。
