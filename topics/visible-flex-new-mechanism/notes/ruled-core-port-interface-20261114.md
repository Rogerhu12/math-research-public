# R44 静态直纹鞍核心：准确入口实现与第三 profile 接口

**状态：已有公开准确公式的入口实现完成，廉价几何与导数检查通过。没有运行连接带优化，没有新闭曲面。**
来源是公开旧课题
[`R44-explicit-flexible-ruled-saddle-annulus.md`](../../visible-flexible-closed-surface/results/R44-explicit-flexible-ruled-saddle-annulus.md)
的 §1–4；中央组装使用本课题 [R6](../results/R6-nonplanar-halfturn-phase-assembly.md)。
本次不重跑旧 R44 的符号证书，不把新端口测试当成原定理的重新证明。

## 1. 准确材料角及全部位置二 jet

保持旧 R44 的
\[
\eta=-3+2\sqrt2,\quad \sigma^2=1-\eta^2,
\quad k(\chi)=\sqrt{8+\sigma^2\sin^2(3\chi)}.
\]
将原角 $\chi$ 变为周期 $2\pi$ 的材料角 $\theta$：
\[
q=\frac{2\sqrt8}{\pi}E(-\sigma^2/8),\qquad
\frac{\sqrt8}{3}E(3\chi,-\sigma^2/8)=q\theta.
\]
左边严格递增，故全圈有唯一周期提升的反函数。其导数为
\[
\chi_\theta=\frac q{k},\qquad
\chi_{\theta\theta}=-\frac{3q^2\sigma^2\sin3\chi\cos3\chi}{k^4}.
\]
由 R44 的有限 Fourier 公式直接计算 $c,d$ 及原角一、二导数，再用这两条链式法则计算材料导数。
没有用离散插值替代解析入口，也没有除以 $II_{\theta\theta}$。

令
\[
Z(s,\theta)=c(\chi(\theta))+s\,d(\chi(\theta)).
\]
对任一固定截口 $s=s_0$，准确数据是
\[
X=c+s_0d,\quad X_s=d,\quad X_{ss}=0,
\]
以及由链式法则得到的 $X_\theta,X_{s\theta},X_{\theta\theta}$。
共同度量为
\[
g=ds^2+a(s)^2d\theta^2,\qquad a(s)=q\sqrt{b^2+s^2}.
\]
因此输入求解器的三个径向度量数据为
\[
a_0=q\sqrt{b^2+s_0^2},\quad
a'_0=\frac{qs_0}{\sqrt{b^2+s_0^2}},\quad
a''_0=\frac{qb^2}{(b^2+s_0^2)^{3/2}}.
\]
位置图在所有有限 $s$ 上正则；旧 R44 已证明的全圈嵌入条带是 $|s|\le b/20$。
超过这个宽度时不能继续引用该条带嵌入证明。

## 2. 代码接口与坐标约定

新增独立模块 `scripts/ruled_core_geometry.py`：

```python
from ruled_core_geometry import RuledCore
core = RuledCore(scale=0.24, rotation=0.0)
a0, ap0, app0 = core.metric(0.012)
inlet_theta_derivative_0 = core.inlet(theta, 0.012, derivative=0)
inlet_theta_derivative_1 = core.inlet(theta, 0.012, derivative=1)
inlet_theta_derivative_2 = core.inlet(theta, 0.012, derivative=2)
```

每个 `inlet` 返回形状 `(3, len(theta), 3)`，第一轴依次是径向 $0,1,2$ 阶导数；与当前 BVP 的边界数组格式相同。
`core.identity(s0)` 返回共同度量二 jet、旋转及半转矩阵、已证明条带宽度适用标记。

必须区分两套合法空间坐标：

- `rotation=pi/2` 是 R6 正文的坐标，中央半转为 $A_x=\operatorname{diag}(1,-1,-1)$，核心主圆用 $(r\cos\theta,r\sin\theta)$ 方向。
- `rotation=0` 是旧 R44 原式，中央半转为 $A_y=\operatorname{diag}(-1,1,-1)$，与当前 BVP 的圆尾 $(r\sin\theta,-r\cos\theta,C)$ 方向一致。

两者是整体刚体共轭，R6 的组装证明随之共轭。接当前 solver 时应使用第二种，不能保留 R6 的半转矩阵却忘记圆尾材料角相差 $\pi/2$。

## 3. 真实廉价检查结果

固定 $b=.24,s_0=.012=b/20$，每个坐标约定各运行一次检查，耗时均不足一秒。
输出为 `ruled-core-geometry-R6-20261114.json` 与 `ruled-core-geometry-tail-gauge-20261114.json`。

\[
q=2.912354692121886,
\quad(a_0,a'_0,a''_0)=(.6998382871319029,.14543605301992996,12.089447466328345).
\]

实际核查包含 $s=-s_0,0,s_0$ 三圈上的准确式比较，而不只是中央一圈：

- $E-1,F/a,G/a^2-1$ 的最大绝对误差 $1.56\cdot10^{-15}$。
- $c_\theta=b\,d\times d_\theta$ 的误差 $7.78\cdot10^{-16}$。
- 按正则法向计算的 $M=-qb/\sqrt{b^2+s^2}$ 与 $N=q^2\kappa\sqrt{b^2+s^2}$，误差分别不超过 $4.89\cdot10^{-15}$、$2.42\cdot10^{-15}$。
- R6 中央半转的六个位置二 jet 分量 $X,X_s,X_\theta,X_{ss},X_{s\theta},X_{\theta\theta}$ 最大误差 $1.12\cdot10^{-14}$。
- 角向一、二导数的独立四阶差分相对误差均小于 $1.61\cdot10^{-11}$。

这里 $N$ 的实际取值跨零，中央约为 $[-1.46108,1.46108]$，而 $M=-q$ 不为零。
因此它确实覆盖当前正 Frenet 图不能直接容纳的角向特征点。
采样最大主曲率约 $5.92218$ 只是实现诊断，不是全整面 reach 证明。

复现命令：

```sh
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/ruled_core_geometry.py \
  --scale .24 --cut-fraction .05 --rotation-deg 90 \
  --out topics/visible-flex-new-mechanism/notes/ruled-core-geometry-R6-20261114.json
```

改 `--rotation-deg 0` 即检查当前尾坐标。

## 4. 接为第三 profile 所需的有限改动

下一适配可以新增 `--core-profile ruled --ruled-scale .24 --inlet-s .012`。
构造 `RuledCore(scale,rotation=0)`，从 `metric(inlet_s)` 取三个度量值；`prepare` 在每个求积或审计角网格上直接调用三个 `inlet`，不经过 FFT 截断。
保留中央到截口的准确核心 $s\in[0,s_0]$；完整下半核心与连接带按 $A_y$ 版 R6 镜合。
首轮自由角基可继续使用 `material`；当前 `ellipse` 角基必须拒绝用于该 profile。
warm 数据必须记录并检查 `ruled-scale`、`inlet-s`、旋转约定及 profile 身份，不能把椭圆 coefficients 直接当成同一场。

背景母线须另作局部适配。对于以上端口，直接复用椭圆延续的
`UnitMeridian(length=1, cut_radius=.28, wiggle=.8)`，当前标量控制搜索 `[-6,6]` 找不到半径闭合。
这只是该参考参数化失败，不是边值问题的排除。
现参考把入口较大的 $a''_0$ 放进全长五次 Hermite 角函数，导致其影响扩散到整个连接段。

较直接的下一参考是只在短段 $0\le t\le\delta$ 局部引入准确 R44 的角
\[
\beta_{\rm core}(t)=\arccos\frac{q(s_0+t)}{\sqrt{b^2+(s_0+t)^2}},
\]
并以在两端至少二阶平坦的 cutoff 接到长段可控母线。
在定义该角的区间必须检查其余弦严格在 $(-1,1)$；例如上述入口可先取 $\delta\approx.03$ 至 $.05$ 作廉价一维参考检查。
随后半径积分须在 cutoff 终点拆段求积，避免全长高斯点漏掉短段。
这里列的是下一可执行背景设计，不声称已完成该适配或找到连接带。

## 5. 平坦尾的具体边界限制

R128 型准确可展尾可写成 $T(x,y)=(x,Y(y),Z(y))$，且 $Y'^2+Z'^2=1$。
若同一材料圆 $x^2+y^2=r^2$ 的完整像位于某一平面，平面方程对每个 $|y|<r$ 的 $\pm x$ 两支同时成立，先迫法向的 $x$ 分量为零。
于是 $\alpha Y(y)+\beta Z(y)$ 恒定，正则性和连续切向再迫 $(Y,Z)$ 在该区间沿一条直线等速行进。
因此这个完整材料边圈在空间中仍是真圆，不能是平面非圆核心。
这只限制这一个明确产品型尾公式，不排除其他带曲率过渡或其他拼接机制。

静态 R44 原种子也没有本题的宏观相位位移证书；它在这里提供准确、正则且可镜合的鞍入口。
连接圆领、全过程像位移、全整面直径与 reach 仍须在同一构造中实际支付。
