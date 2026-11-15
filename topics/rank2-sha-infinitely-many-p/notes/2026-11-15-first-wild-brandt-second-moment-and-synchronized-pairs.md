# 第一 wild tame 平均的真实二阶 Brandt 式与同步匹配

日期：2026-11-15。**状态：下述原有限 incidence 恒等式、对角 Brandt 部分、实际二位匹配及全 Haar 二阶平均已证明。没有给原固定 CM 基点的严格正下界。局部示例只排除从径向树关系直接推该下界，不是原固定全局向量的反例。**

沿用 R716 及
[第一 wild/Rubin 注](2026-11-15-original-first-wild-rubin-factor-and-central-order.md)
中的同一 rational quaternionic test vector $f$。坏位及原 CM 嵌入固定；好惯性 $p>3$ 处为球向量，Hecke 特征值 $a_p(f)=0$。在原 $p^2$ CM 轨道上写
$$
G_2=\Delta\times\Gamma_1,\qquad
|\Delta|=h=(p+1)/3,\qquad
\Gamma_1=\langle\gamma\rangle\simeq\mathbf F_p.
$$
不作新的 $p$-stabilization。令
$$
A_t=\sum_{\tau\in\Delta}f(x_2(\tau\gamma^t)),
\qquad t\in\mathbf F_p.
\tag{1}
$$
原第一 wild 周期零当且仅当 $A_t$ 全相等。下面所有公式保实际投影碰撞和基点。

## 1. 原有限二阶矩

令 $X$ 为固定 quaternionic level 的有限 Shimura 集，并定义非负整数矩阵
$$
C_{t,x}=
 \#\{\tau\in\Delta:x_2(\tau\gamma^t)=x\}.
\tag{2}
$$
不要求 CM 点投影到 $X$ 单射。把 $f$ 写成其实际值列，则
$$
\boxed{\quad
\sum_t A_t^2=f^{\rm t}C^{\rm t}Cf.
\quad}
\tag{3}
$$
同一个式子还可写成
$$
\sum_t A_t^2
 =\sum_{\delta\in\Delta}\sum_{g\in G_2}
                f(x_2(g))f(x_2(\delta g)).
\tag{4}
$$
每个 $\delta$ 的完整碰撞矩阵是
$$
N_{p,\delta}(x,y)=
 \#\{g\in G_2:x_2(g)=x,\ x_2(\delta g)=y\}.
\tag{5}
$$
因而 $C^{\rm t}C=\sum_\delta N_{p,\delta}$；
$N_{p,\delta}^{\rm t}=N_{p,\delta^{-1}}$。
这些是原轨道上精确有限矩阵，不是自由选择的相关函数。

## 2. 对角部分确由原 Brandt 算子读取

在局部 Bruhat–Tits 树上，惯性非分裂环面作用传递于半径二球面，其大小为 $p(p+1)$。原全局 $\mu_6$ 在投影后给一个自由的三元作用，所以 $G_2$ 是这个球面的三元商。原 $f$ 在该商上确实下降；这一步只用于原 CM 基点 $x_0$。

令 $B_p$ 为带全部边重数的未归一 $p$-邻接 Brandt 算子。半径二不回溯算子为
$$
S_{p,2}=B_p^2-(p+1)I.
$$
因此 (4) 中 $\delta=1$ 的对角部分严格为
$$
\boxed{\quad
D_p:=\sum_{g\in G_2}f(x_2(g))^2
 =\frac13 S_{p,2}(f^2)(x_0).
\quad}
\tag{6}
$$
$B_p$ 的边重数和 (2) 的所有全局碰撞均保留，不能改成互异终点数。

若用标准的 Brandt 谱分解及权二 Ramanujan 界，设
$\Pi_{\rm norm}$ 为固定层上全部 reduced-norm 字符组成的子空间投影，则
$$
D_p=\frac{p(p+1)}3\,
            (\Pi_{\rm norm}f^2)(x_0)+O_{f,X}(p).
\tag{7}
$$
理由是 norm 字符的 $B_p$ 特征值为 $\pm(p+1)$，
而 cuspidal 特征值模不超过 $2\sqrt p$；
固定有限集上的逐点评值常数不依 $p$。
$\Pi_{\rm norm}f^2$ 是相应 norm fibre 的带正确稳定子权重的平均。
它非负；严格正需要 $f$ 在该 fibre 不恒零，
不能由 $f$ 在整个 $X$ 非零推断任意 fibre 正。

原基点关系另外给
$$
\sum_t A_t
 =\frac13 S_{p,2}f(x_0)
 =-\frac{p+1}{3}f(x_0).
\tag{8}
$$
在原未扭 toric 基点 $f(x_0)=0$ 的规范下，
总和为零，因此 $A_t$ 全相等等价于 $A_t$ 全为零。
(8) 本身不控制 (3) 的正性。

## 3. 交叉项不是径向距离四核

对不同 $\tau,\sigma\in\Delta$，
$x_2(\tau\gamma^t)$ 与 $x_2(\sigma\gamma^u)$ 的局部提升位于不同第一分支，树距均为四。可是 (3) 只保 $u=t$ 的 $p$ 个配对，并非这两分支的全部 $p^2$ 个配对。

所以在原树球面上，同步核
$$
\mathbf1_{t=u}
$$
不是距离的函数：同为距离四的两对，可以分别属于和不属于此核。
因此没有一个只由局部径向 Hecke/距离算子给出的**普适**替换，
把 (5) 的实际同步交叉项改成完整距离四和。

这没有证明投影到某个具体有限 $X$ 后不可能出现额外恒等式。
若原固定 $f$ 或实际 $N_{p,\delta}$ 还有特殊全局关系，仍可使用；
但该关系须另外证明。

## 4. 同步匹配中的真实 Fermat 修正

取 $K_p=\mathbf Q_p(\delta)$、$\delta^2=-3$，
用 line $1+x\delta$ 的 slope $x\in\mathbf Z/p^2$ 描述有限第一分支；
无穷分支另用倒数坐标。

主单位 $\gamma_t=1+p\delta t$ 的实际作用为
$$
x\longmapsto\frac{x+pt}{1-3pxt}
 \equiv x+pt(1+3x^2)\pmod{p^2}.
\tag{9}
$$
$p$ 惰性保证 $1+3a^2\ne0\bmod p$ 对每个 $a\in\mathbf F_p$ 成立。

令
$$
\vartheta(x)=\frac{1+x\delta}{1-x\delta}.
$$
tame Teichmüller 截面在分支 $a$ 上为
$\widetilde x(a)=a+p\kappa_p(a)$，由
$\vartheta(\widetilde x(a))^{p+1}=1\bmod p^2$
确定。展开一次，得到准确式
$$
\boxed{\quad
\kappa_p(a)=
 -\frac{1+3a^2}{2\delta}\,
    \frac{\vartheta(a)^{p+1}-1}{p}\pmod p.
\quad}
\tag{10}
$$
右侧属于 $\mathbf F_p$：括号内商的共轭为其负数。
所以原同 $t$ 集合的实际坐标是
$$
\boxed{\quad
x(a,t)=a+p\{\kappa_p(a)+(1+3a^2)t\}\pmod{p^2}.
\quad}
\tag{11}
$$
无穷分支的倒数坐标为 $-3pt$。
最后再取原 $\mu_3$ 商，不删除任何二位信息。

(10)–(11) 正是 R724 的实际 anti-Fermat 条件在树边坐标中的形式。
它不是任选的第二位；仅知道 $a\bmod p$ 或所有端点距离为四，不能恢复它。

## 5. 完整 Haar 平均确为正，但原固定基点不含此平均

在整个 automorphic quotient 上取原 Haar 内积。
选定 (1) 每个点的实际局部代表 $g_{\tau,t}$；它们把根送到所选半径二顶点。
对任意两不同分支且同 $t$ 的代表，
$g_{\sigma,t}^{-1}g_{\tau,t}$ 的 Cartan 距离为四。

原局部球函数 $\varphi_p$ 满足
$$
\varphi_p(0)=1,\quad
\varphi_p(1)=\frac{a_p}{p+1}=0,\quad
p\varphi_p(n+1)+\varphi_p(n-1)=a_p\varphi_p(n).
$$
因此
$$
\varphi_p(2)=-p^{-1},\qquad
\varphi_p(4)=p^{-2}.
\tag{12}
$$
用原纯球向量的矩阵系数，而非独立点值假设，得到
$$
\boxed{\quad
\int\sum_{t\in\mathbf F_p}
   \left|\sum_{\tau\in\Delta}f(xg_{\tau,t})\right|^2dx
 =
 \left(hp+\frac{h(h-1)}p\right)\|f\|_2^2>0.
\quad}
\tag{13}
$$
对角共有 $hp$ 项；异分支同 $t$ 的有序对共有 $h(h-1)p$ 项，每项的全内积是 $p^{-2}\|f\|^2$。

(13) 的积分含原固定 CM 基点所没有的全部紧方向。
它不能改成 (3) 在 $x=x_0$ 的值，
也不能将“存在某个 $x$ 的非零”改成原固定嵌入的非零。
原 $\mu_3$ 商只在 CM 基点使用；(13) 对已选出的代表作全 Haar 平均，不额外假定商关系对所有 $x$ 成立。

## 6. 局部谱值与行和不足以控制同步交叉项

这个限制可在原无限树上直接看见。
取任意非零实函数 $F:\mathbf F_p\to\mathbf R$，满足 $\sum_tF(t)=0$。
在两个不同的 $\Delta$ 分支放 $F(t)$、$-F(t)$，
其余分支放零；在原三元单位轨道内复制相同值。
令根和第一层全部为零。于是：

- 每个第一分支的第二层子和都为零；
- 根和第一层的邻接特征值方程 $B_pf=0$ 成立；
- 半径二对角平方和严格正；
- 每个同步列和 $A_t$ 都严格为零。

这些局部数据还能扩为整棵树上的有界 $0$-本征函数：
在任意已赋值顶点，令其所有 $p$ 个向外子顶点均取
$-\text{该顶点的父值}/p$。
这样每个顶点的邻接和为零，赋值保持有界并保持三元单位对称。

这个例子没有固定有限 Shimura 集，也不是原 automorphic $f$。
它准确说明：仅由原局部特征值 $a_p=0$、允许的 Ramanujan 谱值、分支行和以及径向距离信息，不能推出 (3) 在指定基点严格正。

实际剩余输入是 (5) 的原同步碰撞矩阵与原全局 $f$ 之间的关系，
或等价地 R724 中非实 anti-Fermat 和的严格单边估计。
全 Haar 正性和原 Fourier 自对偶都不能代替该输入。

## 来源

- R716：原 Hecke 角色与固定 quaternionic/theta 族的相同零判据。
- R724：同一个第一 wild 理想角色及实际 anti-Fermat 核。
- 第一 wild/Rubin 注 §6：实际 $G_2=\Delta\times\Gamma_1$ 与 rational tame 平均。
- Burungale–He–Kobayashi–Ota，
  [*Hecke L-values, definite Shimura sets and Mod ℓ non-vanishing*](https://arxiv.org/html/2408.13932v3)，
  §3、§5，原固定 test vector、Shimura 集及 CM 点。本文没有借其固定 $p$ 的深层满射取代第一层同步矩阵。

本注无数值计算，也不提出新的中央零假设。
