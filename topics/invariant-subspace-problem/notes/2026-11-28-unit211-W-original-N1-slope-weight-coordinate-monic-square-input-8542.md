# 全 W：原 N1 斜率的纯权二阶行列式与首一平方新输入

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

这是新原结构输入，尚未执行。不重算已经冻结的 C8 范数、十八行模块或十二阶结式。当前范围仍是一般 LS、$\Delta=W=0$、原值互异的现有 W 余图；所有原权单位沿既有整支定理。

## 1. 固定的原 N1 一次行

由[整个 K7 原排除与三生成元](../results/R150-appendix-unit211-W-entire-K7-complete-original-exclusion-and-global-three-generators.md)，三个原均值给出 $x^2,xy,y^2$ 的规则，系数属于 $R=A_W[\lambda]$。它们的完整原迹已经给出。

按同一规则约化原 $N_1$，保其完整一阶 germ，得

$$
n=p_0(\lambda)+p_1(\lambda)x+p_2(\lambda)y
=\sum_{j=0}^3\nu_jF_j,
\quad F=(E_1,E_{Be},E_{Bo},N_1),
\tag{1}
$$

其中 $n-N_1$ 属于前三个原均值的理想，$\deg_\lambda p_0\le2$、$\deg_\lambda p_1,\deg_\lambda p_2\le1$。这个原行就是已刊三列原模型中返回的那一行，不把双点 germ 改成简单点值。

写

$$
p_1=\alpha\lambda+\beta,\qquad
p_2=\gamma\lambda+\delta,\qquad
\alpha,\beta,\gamma,\delta\in A_W.
\tag{2}
$$

四个字母在这里是斜率及截距，不是原物理单谱权 $a,b,c$。

## 2. 真正的新纯权行列式

定义

$$
\Delta_N=\alpha\delta-\beta\gamma\in A_W,\qquad
Z_N=\alpha x+\gamma y.
\tag{3}
$$

$Z_N$ 是本次新坐标，不与旧 $z=Qt$ 或原值中心 $s$ 混用。直接有两个完整原多项式身份

$$
\boxed{
\begin{aligned}
\Delta_N x&=p_2Z_N+\gamma p_0-\gamma n,\\
\Delta_N y&=-p_1Z_N-\alpha p_0+\alpha n.
\end{aligned}}
\tag{4}
$$

它们在整个原环成立，不先要求 $\Delta_N$ 非零。新源将实际回乘 (1)–(4)，然后只从 $\Delta_N$ 分子剥既有权单位，对完整剩余纯权多项式作 QQ 分解并乘回。

若 $\Delta_N$ 恒零，不声称得到新二生成图，所有原纤维保留。若它非零但含未付权因子，则下节只在明确补图 $\Delta_N\ne0$ 上成立，整条零曲线继续开放。只有当实际剩余是非零常数，才能把下节用于整个当前 W 权图。

这里没有新的 λ 首项或几何逆；$\Delta_N$ 只依赖 $e,k$。

## 3. 在准确补图上的双侧原恢复

在 $R_N=A_W[\Delta_N^{-1}][\lambda]$ 上，令独立新变量为 $Z$，置

$$
\widehat x=\frac{p_2Z+\gamma p_0}{\Delta_N},\qquad
\widehat y=\frac{-p_1Z-\alpha p_0}{\Delta_N}.
\tag{5}
$$

全部正反身份为

$$
\alpha\widehat x+\gamma\widehat y=Z,\qquad
p_0+p_1\widehat x+p_2\widehat y=0,
\tag{6}
$$

以及 (4) 在 $n=0$ 后恢复原 $x,y$。故

$$
R_N[x,y]/(n)\simeq R_N[Z].
\tag{7}
$$

(1) 同时给出 $(E_1,E_{Be},E_{Bo},N_1)=(E_1,E_{Be},E_{Bo},n)$。因此把原均值通过 (5) 运输，保的是同一个原理想，没有删除原 $N_1$ 的低次项。

## 4. 由三原规则构造单首一平方

用三个原均值规则对 $Z_N^2$ 作精确约化，得到

$$
r_0+r_1x+r_2y-Z_N^2
=\sum_{j=0}^2\theta_jF_j.
\tag{8}
$$

定义

$$
q_Z(Z)=Z^2-r_0-r_1\widehat x-r_2\widehat y
=Z^2+\beta_1(\lambda)Z+\beta_0(\lambda).
\tag{9}
$$

从 (4)、(8) 准确得到完整原来源

$$
\boxed{
q_Z(Z_N)=
\sum_{j=0}^3
\left\{-\theta_j+
\frac{\alpha r_2-\gamma r_1}{\Delta_N}\nu_j\right\}F_j,
\qquad \theta_3=0.
}
\tag{10}
$$

新源必须实际核回 (10)，不能只凭最高次推断。全部分母只来自已付权单位与明确补图中的 $\Delta_N$。根据原三个二次规则的次数，

$$
\deg_\lambda\beta_1\le2,\qquad
\deg_\lambda\beta_0\le3.
\tag{11}
$$

式 (9) 对 $Z$ 首一。因此原四均值商在这个准确权图上由 $1,Z$ 作为 $R_N$ 模生成；任何再加原 $N_S,P_S$ 或完整个别值条件的商仍由这两个元素生成。

只有明确的环境 $R_N[Z]/(q_Z)$ 被称为自由二阶；不称原方程商自由，也不把几何 $D$ 或其它几何量局部化后自动视作对纯权环有限。本次暂未构造完整 N/P 在两列中的全部系数；其原条件始终保留。

## 5. 唯一源与真实界限

新源：

notes/2026-11-28-unit211-W-original-N1-slope-weight-coordinate-monic-square-8542.py

Git blob：178b79006da698e77e8e3a5d8ba150533a3f8998。

SHA256：9b7731d221175a88edbf7f98bb1c811402ab1d8e332b94fb005dd073b7894d00。

8605 字节。固定 180 秒、4 GiB；必要前缀的 alarm 被钳制在本次原绝对截止时刻。

直接依赖只有已提交三规则源：

2026-11-28-unit211-W-K7-open-physical-lambda-original-three-column-projection-binding-corrected-8542.py

SHA256 7cf3ff802cdf8166e3fb96f3ea806b81b83570f9200d10fad11caa13862f2c3f。仅使用到原规则与六个乘法返回结束的 5833 字节，前缀 SHA256 为 8ea50cb422b81b5976bbb132e01809135ebbaedc06d545bcdb0c741fec4e3ff4；没有执行其原三列行、两个六次 cofactor 或后段结式。

两个传递依赖是既有物理 λ 源 0b261ecc3cb4ef012ed9dce5b9403723edccd7e4 与 C9 原 Gram 源 a1a9d02a1602a47398ba9bbb9295b3da7d7ddd37，basename 与 SHA 均由冻结前缀固定。

当前没有实际运行回执，不提前支付 $\Delta_N$。后续仅保存源、原定义、真实 run/exit、次数、SHA 和小回执；不输出或保存可重算系数载荷。
