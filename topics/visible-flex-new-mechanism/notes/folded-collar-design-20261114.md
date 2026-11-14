# 回折圆领分支、开放非圆核心及 Actions 入口

日期：2026-11-14。**状态：新表示已实现并完成开发级检查；新的非轴 BVP 优化留给本公开仓库自己的 GitHub Actions。未取得合格解。** 本轮将 $e=0$ 的同轴非圆带纳入搜索，不再把偏心或 $\delta_E>0$ 加为额外必要门槛。

## 1. 内部闭渐近圆改变了哪个方程

圆参考母面取 $X=a(s)e_r+z(s)e_z$，$a'=\cos\beta,z'=\sin\beta$。按 $\nu=-\sin\beta\,e_r+\cos\beta\,e_z$，

\[
\mathrm{II}_{ss}=\beta',\qquad
\mathrm{II}_{su}=0,\qquad
\mathrm{II}_{uu}=a\sin\beta,\qquad
K=\frac{\beta'\sin\beta}{a}=-\frac{a''}{a}.
\]

原 $b=.9$ 参考的活动段始终 $0<\beta<\pi$，故 $N=\mathrm{II}_{uu}>0$。把 $b$ 提到约 $2.4$–$2.8$，$\beta=\pi S+b\sin(2\pi S)$ 可越过 $\pi$，从而出现内部 $z'=0$、$N=0$ 的闭圆。该圆的切向是第二基本形式的零方向；这里它是抛物圆，不能直接等同于文献负曲率带中的两族闭渐近叶。

这使 $L=(M^2-aa'')/N$ 的正常形在内部失效，提供应由未除法位置 BVP 处理的特征匹配位置。它**不证明**新非圆解存在，也没有证明闭渐近圈是一般有限柔性的必要条件。Ghomi–Qiu–Raffaelli–Zhang 的公开原文 [§1–2](https://arxiv.org/html/2611.17269v1) 用闭渐近叶构造紧支撑无穷小弯曲，但明确把连续有限柔性留为未解决问题；其引述的 Nirenberg 条件属于 tight surface 的特定刚性定理。

此外，孤立 $z'=0$ 并不会自动解除圆基底的 $m=1$ 首阶锁死：在各个 $z'\ne0$ 连通段仍有 $F=Cz+D,H=-aC$。只要 $a>0$ 且 $H,F$ 连续，穿过孤立零点时两侧 $C,D$ 必相同。新搜索因此锁住真正非圆的核心，不从纯圆 $m=1$ 初值声称得到新分支。

## 2. 严格圆参考几何与实际非轴 BVP 分开

`../scripts/folded_reference_geometry.py` 只处理可封两个平盘的**轴对称参考面**。它使用 50 位 Decimal 向外舍入、Machin 公式包住 $\pi$、三角函数交错级数余项，以及区间 Riemann 和；不依赖机器 `sin/cos` 的未经说明误差。

设前半母线的唯一径向极大位置为 $s_A$，$\beta=\pi$ 的升支和降支根为 $s_1,s_2$，中面高度为 $H/2$。在 $\pi<\max\beta<3\pi/2$ 的模式下，以下正裕量给出直接的母线单射证明：

\[
a_{\min}>0,\qquad z(s_2)>z(s_A),\qquad H/2>z(s_1).
\]

第一半中，$a$ 先严格增加再严格减少（有 plateau 时最后为竖直段）；初始增支的高度不超过 $z(s_A)$，后续回折最低高度仍大于它，故不会相交。两半由中面严格隔开；平盘位于两端开平领内，得到闭参考嵌入。曲率用 $|\beta'|$ 和 $|\sin\beta|/a$ 的区间上界核验。

镜像回折圆还给出一个有用的**上界**：两圆的相对点在共同法线上，距离 $2(H/2-z(s_1))$，因此

\[
\operatorname{reach}(\Sigma_{\rm ref})\le H/2-z(s_1).
\]

这不是 reach 下界。脚本从不把参考嵌入/曲率检查传给非轴输出，也没有给参考面全局 reach 下界。

开发级浮点筛查已显示：普通整段 smoothstep 的 $b=2.4,L=2.2,r_0=.45$ 参考曲率约 $11.562$、两项高度裕量约 $.121,.0915$；$b=2.6,L=2.4,r_0=.45$ 虽曲率约 $11.714$，镜像圆必要上界除以 $D\ge2a_{\max}$ 却仅约 $.02813$。所以较深回折不能只看曲率。更高精度的区间结论由 Actions 运行 `--cells 512` 后给出；本地仅用了 8 格做实现冒烟，没有把粗网格未通过误说成不存在。

## 3. 非圆核心的曲率不能继承圆参考值

若在一个核心截面锁住单位材料速度的平面曲线，曲率半径为 $a\rho(u)$，并锁 $X_s=e_z$、$a'=0$，准确等距关系迫使

\[
\kappa_s=-a''\rho(u),\qquad \kappa_u=\frac1{a\rho(u)}.
\]

因而圆参考 $|a''|\approx11.56$ 搭配 $\rho=1+.25\cos2\varphi+.2\cos3\varphi$，核心已要求 $|\kappa_s|\approx16.77$，超过拟定上限 $13$。加密求解器不能解除这个必要条件。

新的 `PlateauMeridian` 把中央做成真正开段 $\beta=\pi/2$，即 $a'=a''=0,z'=1$。左过渡取

\[
v(s)=\tfrac12 S_5\!\left(\frac{s-cL}{L(1/2-p-c)}\right),\qquad
\beta=\pi v+b\sin(2\pi v),
\]

右侧镜像，中央区间为 $[L(1/2-p),L(1/2+p)]$。各接点 $\beta',\beta''$ 都为零。这样可在中央锁任意固定周长的非圆曲线的**准确挤出带**，其径向曲率为零；两侧仍保留回折。

该全局 plateau 参考仍会外鼓，默认 $b=2.4,L=3,r_0=.8,p=.15$ 只是求解表示的入口，不是已满足幅度预算的最终形状。机制分支另外设计从椭圆核心向平领径向单调缩小的 inward-fold 参考，以避免外鼓过度增加全体直径；两者必须作为不同物理设计记录。

## 4. 新三表示运行器

`../scripts/folded_collar_search.py` 提供 `cartesian`、`unit`、`signed` 三种引擎。它不修改原稳定脚本；只有在本公开仓库 Actions 中才执行优化，本地 `--smoke-only` 不进行最小二乘迭代。

共同约束是 $e=0$、固定 $g=ds^2+a_{\rm ref}(s)^2du^2$、两端开圆领、中央开放非圆挤出核心。左右过渡各用独立夹持五次 B 样条，未知函数在端领与核心端口均零二阶 jet；左右合计自由基函数数保持不变，没有通过堆变量制造改善。所有非中央中心模保留。

Cartesian 的核心位置及完整 jet 使用解析曲线。曲率半径模式用 $\rho=1+A\cos2\varphi+B\cos3\varphi$，并仅在定义核心时按解析材料质心平移一次。椭圆模式用半轴 $A_e\ge B_e>0$，令

\[
m=1-(B_e/A_e)^2,\quad r_{\rm mean}=\frac{2A_eE(m)}\pi,\quad
A_e[E(\varphi-\pi/2\mid m)+E(m)]=r_{\rm mean}u.
\]

归一化曲线 $\Gamma=(A_e\cos\varphi,B_e\sin\varphi)/r_{\rm mean}$ 满足 $|\Gamma_u|=1$；其一、二阶材料导数由单位切线与平面曲率直接计算。`unit`/`signed` 使用同一核心切线角，保留显式角闭合残差；它们的 Fourier 原函数仍是数值评估，需要角分辨率精化，不能冒充连续精确积分。

开发检查：三个引擎的 Jacobian 随机方向相对差依次为 $8.81\cdot10^{-10}$、$2.56\cdot10^{-9}$、$3.09\cdot10^{-9}$。对开放核心加入任意小系数扰动，Cartesian 全位置二阶 jet 改变量为零，核心度量误差不超过 $6.7\cdot10^{-16}$。椭圆单位速误差 $4.4\cdot10^{-16}$、周期闭合误差 $7.6\cdot10^{-16}$；一、二阶导数的独立中心差分与解析 jet 一致。它们验证表示，不是新的 BVP 解。

## 5. 可直接加入下一公开 Actions 的命令

先核参考，再运行 BVP；输出目录沿用该 lane 的 `$VISIBLE_NEW_OUT`，无需创建另一套认证或发布路径。

```sh
python topics/visible-flex-new-mechanism/scripts/folded_reference_geometry.py \
  --beta-wiggle 2.4 --length 3 --radius .8 --plateau .15 --cells 512 \
  --curvature-limit 12 --out "$VISIBLE_NEW_OUT/folded-reference.json"

python topics/visible-flex-new-mechanism/scripts/folded_collar_search.py \
  --engine signed --core-shape curvature --seed2 .25 --seed3 .2 \
  --beta-wiggle 2.4 --length 3 --radius .8 --plateau .15 \
  --controls 14 --modes 6 --radial-order 8 --angles 64 --max-nfev 180 \
  --reference-audit "$VISIBLE_NEW_OUT/folded-reference.json" \
  --out "$VISIBLE_NEW_OUT/folded-signed-pinned-core.json"
```

同一参数可另以 `--engine unit` 对照。Cartesian 的强形状入口用 `--engine cartesian --core-shape ellipse --ellipse-major 1.4 --ellipse-minor .5`；`--curvature-weight` 可明确加入已推导的实际 shape-operator 罚项，默认零，仅独立审计真实曲率。

每个输出都单独标注：固定目标度量、源代码 SHA、参考证明的范围、核心锁定规则、实际残差/曲率，以及未证明的闭嵌入、固定握持像位移和 reach。即使圆参考通过区间检查，也不能据此给非轴候选贴合格标签。
