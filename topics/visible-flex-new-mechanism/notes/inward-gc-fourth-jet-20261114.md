# inward 核心的四阶 Cauchy jet 与椭圆角基

日期：2026-11-14。新独立入口为 `scripts/inward_gc4_collar_search.py`；未修改已经冻结的 `inward_collar_search.py` 或其依赖。这里只完成公式、表示和廉价导数检查，没有运行优化。所有实际求解仍使用本公开仓库自己的 Actions。

## 1. 固定 inward 度量的准确一侧四 jet

以离开上核心的物理弧长 $t\ge0$ 为变量。记第一段长为 $L_1$，$\eta$ 为 inward 过冲角。参考角为

\[
\beta(t)=\frac\pi2+\left(\frac\pi2+\eta\right)S_5(t/L_1)
        =\frac\pi2+ct^3+O(t^4),\quad
c=\frac{10(\pi/2+\eta)}{L_1^3}.
\]

因此固定半径函数满足

\[
a(t)=a_0-\frac c4t^4+O(t^5),\quad
a'(0)=a''(0)=a'''(0)=0,\quad a^{(4)}(0)=-6c.
\tag{1}
\]

核心闭曲线 $\gamma(u)$ 采用材料角，$|\gamma_u|=a_0$。记平面单位切向 $T$、向内单位法向 $N$、物理曲率 $\kappa>0$，以及无量纲曲率 $k=a_0\kappa$。入口完整二 jet 为

\[
X(0,u)=\gamma(u)+h_0e_z,\quad X_t(0,u)=e_z,\quad X_{tt}(0,u)=0.
\tag{2}
\]

以下推导针对存在光滑一侧四阶展开的准确延拓；它没有额外证明所有仅 $C^2$ 延拓都自动具有四阶正则性。对数值使用的光滑样条段，这是应当匹配的 Cauchy jet。

令第二基本形式为 $L\,dt^2+2M\,dtdu+Q\,du^2$，在入口取曲面法向为 $N$。因 $g=dt^2+a(t)^2du^2$，径向材料线为单位速测地线，故 $X_{tt}=L\nu$。Gauss 方程和入口数据给

\[
LQ-M^2=-aa'',\qquad L(0)=M(0)=0,\qquad Q(0)=a_0^2\kappa=a_0k.
\tag{3}
\]

先对 (3) 求一次径向导数，由 (1) 得 $L_t(0)=0$。Codazzi 方程在入口因 $a'(0)=0$、$L(0,u)\equiv0$ 给 $M_t(0)=0$。再对 (3) 求二次径向导数，得到

\[
L_{tt}(0)Q(0)=-a_0a^{(4)}(0)=6a_0c,
\quad L_{tt}(0)=6c/k.
\]

因此 $X_{ttt}(0)=0$，$X_{tttt}(0)=6cN/k$，完整一侧展开为

\[
\boxed{X(t,u)=\gamma(u)+(h_0+t)e_z+
                  \frac{c}{4k(u)}t^4N(u)+O(t^5).}
\tag{4}
\]

它在圆截面 $k=1$ 时退化为参考半径的四阶收缩。强椭圆的 $1/k$ 随角度显著变化，不能用等比例缩小椭圆来替代 (4)。

## 2. 旧桥为什么产生人工三阶项

旧 Cartesian 试场使用 $B(t)=1-S_5(t/L_{\rm active})$ 混合椭圆与圆。即使 (1) 已固定，横向位置仍出现

\[
-\frac{10a_0}{L_{\rm active}^3}t^3
       (\gamma/a_0-e_r)+O(t^4),
\]

而 (4) 的三阶项应为零。实际末盘抬高所用的旧 $S_5$ 中心桥还引入竖直三阶项。这些项不破坏入口的二 jet，但会迫使有限自由角模去抵消一个解析强椭圆函数的全部材料角高模。

新入口采用

\[
S_9(x)=126x^5-420x^6+540x^7-315x^8+70x^9,
\]

在 $[0,1]$ 外常值延拓。它在两端的一至四阶导数均为零。椭圆混合桥和实际中心高度桥都改为 $S_9$，因此没有人为的三阶或四阶桥项。目标半径函数 $a$、完整核心、圆端口、实际盘高度和固定度量全部保持不变。

## 3. 不截断角谱的解析四 jet 修正

记 $\bar\gamma=\gamma/a_0$。仅改高阶桥以后，横向基场 $a\bar\gamma$ 的四阶系数是 $-c\bar\gamma/4$。为得到 (4)，增加

\[
\frac c4\,w(t)h(u),\qquad
h=\bar\gamma+N/k,
\quad w(t)=t^4[1-S_9(t/\ell_j)].
\tag{5}
\]

默认 $\ell_j=L_1/4$，由 `--gc-jet-fraction .25` 控制。局部四 jet 不能外推到整个连接，故修正窗只覆盖入口附近；改变该窗只改变初始试场，不改变目标问题。两端开圆领处修正恒零，核心处修正零至三阶，因此全部边界二 jet 保留。

物理椭圆写为 $\gamma=(A\cos\varphi,B\sin\varphi,0)$，

\[
q(\varphi)=\sqrt{A^2\sin^2\varphi+B^2\cos^2\varphi},\qquad
\varphi_u=a_0/q,\qquad
\varphi_{uu}=-\frac{a_0^2(A^2-B^2)\sin\varphi\cos\varphi}{q^4}.
\]

取 $d=A^2-B^2$。代入 $N=(-B\cos\varphi,-A\sin\varphi,0)/q$ 和 $k=a_0AB/q^3$，得到非常简单的准确角函数

\[
\boxed{h(u)=\left(\frac d{Aa_0}\cos^3\varphi,
                    -\frac d{Ba_0}\sin^3\varphi,0\right).}
\tag{6}
\]

程序直接计算 (6) 及其材料角一、二阶导数，未先截成有限 $u$ 傅里叶级数。

**不可把本推导不加修改地用于自由度量设计器。** 若设计变量使 $a'''(0)$ 非零，准确三阶位置项也必须相应非零；一般入口的三、四阶关系要使用实际 $a_3,a_4$，不能仍强制 $X_3=0$。本脚本只处理 (1) 的固定 inward 半径。

## 4. 同数量的椭圆角试函数能准确包含这些高模数据

选项 `--angular-basis ellipse` 将自由位置的角试函数从 $1,\cos(ju),\sin(ju)$ 换为

\[
1,\cos(j\varphi(u)),\sin(j\varphi(u)),\quad j=1,\ldots,m.
\tag{7}
\]

材料坐标仍为 $u$，目标仍为 $dt^2+a(t)^2du^2$。一、二阶导数完整使用上面的 $\varphi_u,\varphi_{uu}$ 链式法则；不是重定义材料角后丢掉尺度因子。径向函数及未知数总数不变，所有自由基在核心和圆领处继续有零二 jet。

这比单纯乘一个曲率权重更直接：$\bar\gamma$ 在 (7) 中只需 $m=1$；由 $\cos^3\varphi=(3\cos\varphi+\cos3\varphi)/4$ 与 $\sin^3\varphi=(3\sin\varphi-\sin3\varphi)/4$，$h$ 和 $N/k=h-\bar\gamma$ 只需 $m=3$。所以 $m=12$ 已准确包含这些特定入口函数在材料角中的全部高模，而无需把它们逐个加到 $u$ 的 Fourier 截断中。这里并未证明整个未知连接只含三模，非线性残差仍须独立加密审计。

## 5. 已完成的廉价验证

使用 `controls=10,modes=2,angles=32,radial-order=2`，曲率权重 $.01$，只检查不优化：

| 项目 | material 基 | ellipse 基 |
|---|---:|---:|
| 残差解析 Jacobian 随机方向相对差 | $7.86\times10^{-10}$ | $7.58\times10^{-10}$ |
| 核心与圆领全二 jet 最大误差 | $8.9\times10^{-16}$ | $8.9\times10^{-16}$ |
| 四阶系数解析恒等式误差 | $1.14\times10^{-13}$ | $1.14\times10^{-13}$ |

在 $t=.002,.001,.0005$，横向四阶系数余项的最大误差分别为 $.5920,.2971,.1485$，呈一阶减小；竖直位移除 $t^4$ 也随 $t$ 趋零。这与 $O(t^5)$ 余项一致，但不是经过验证的连续余项界。

另外以非零随机位置系数检查空间微分，$X_s,X_u,X_{ss},X_{su},X_{uu}$ 的中心差分相对误差均不超过 $1.08\times10^{-9}$。在 ellipse 基中，仅 $m=3$ 就将 $\bar\gamma,h,N/k$ 及其材料一、二阶导数重构到 $3.2\times10^{-14}$ 以内。小记录为 `notes/inward-gc4-derivatives-20261114.json`。

新零系数初场在同一小样本审计的最大曲率约 $185$，仍然远不合格；旧接口 smoke 的相应值约 $1023$。这种初值诊断不是求解改善、准确等距或 reach 证明。实际优化尚未运行。

## 6. 下一 Actions 的受控比较命令

基线 `inward_fixed` 的脚本与源 SHA 保持独立。以下比较同一 B 固定度量、核心和实际两盘高度，只改变初始解析基场与有限角试函数：

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/inward_gc4_collar_search.py \
  --seed-family gc4 --angular-basis material --gc-jet-fraction .25 \
  --ellipse-major 1 --ellipse-minor .3 --core-half-height .23 \
  --connection-length .8 --cut-radius .28 --port-height .30 \
  --inward-overshoot 1.53 --inward-first-fraction .67 --reach-budget .069 \
  --controls 14 --modes 6 --angles 128 --radial-order 8 --max-nfev 200 \
  --out "$VISIBLE_OUT/inward-gc4-material-B.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/inward_gc4_collar_search.py \
  --seed-family gc4 --angular-basis ellipse --gc-jet-fraction .25 \
  --ellipse-major 1 --ellipse-minor .3 --core-half-height .23 \
  --connection-length .8 --cut-radius .28 --port-height .30 \
  --inward-overshoot 1.53 --inward-first-fraction .67 --reach-budget .069 \
  --controls 14 --modes 6 --angles 128 --radial-order 8 --max-nfev 200 \
  --out "$VISIBLE_OUT/inward-gc4-ellipse-B.json"
```

`--seed-family legacy` 可单独保留旧初值进行角基比较。不能将旧坐标系数原样当新解析基场/角基的 resume；脚本明确拒绝该操作。尚未证明固定度量误差趋零、闭嵌入、固定握持幅度或 reach。
