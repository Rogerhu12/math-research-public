# R150 附录：rankH2 与 rankV2 的全部完整临界点本质维数至多四

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 前稿保留的双约化 Gaussian 规范现被完整原 H 梯度的两个已写出值方程排除。关键并非新的消元：把已证明的相反交叉列重新代回这两个原方程，便得 $17F^3=0$，与规范中的 $F\ne0$ 矛盾。任意复数参数、无穷远和全部降秩边界已由前两篇完整归约纳入。

## 1. 精确结论与原对象

仍用原六模式 Hankel 累积量 $y,H,V$、原非退化对称矩阵 $K$，及
$$
T_3=y^3-6yH+4V,\qquad
p=Ky,\quad F=\tfrac12y^{\mathsf T}Ky.
$$
**定理。**
$$
\boxed{
\nabla\mathcal Q_3=0,\quad \operatorname{rank}H=\operatorname{rank}V=2
\quad\Longrightarrow\quad
\dim\operatorname{ess}(T_3)\le4.
}
\tag{1.1}
$$
这里的临界性是原六 mean、十一 H、十六 V 全部梯度。没有把低秩参数流形上的受限梯度反推为原梯度，也没有预设 $y,H,V$ 共用 $V$ 的长度二支撑。

由于
$$
T_3\in\operatorname{Sym}^3\{\mathbb Cy+\operatorname{Ran}H+\operatorname{Ran}V\},
$$
在本假设下其本质维数本来至多五。因此只需排除本质五维。

[至少一个 tangent 支撑的完整三类型排除](R150-appendix-rank-two-second-and-third-cumulants-with-a-tangent-support-have-essential-dimension-at-most-four.md)已经排除 H 或 V 的二重 jet，包括原值系数为零、全部无穷远与 Gaussian $Hp=0$ 例外。

[双约化完整必要规范](R150-appendix-rank-two-second-and-third-cumulants-essential-five-reduced-gaussian-normal-form.md)已经排除 H 两点正交及 $Hp\ne0$ 的全部分支。它保留的唯一候选正是下节。本文将其消去，因此不是重新证明已登记的分支。

## 2. 唯一候选及其两个仍须同时满足的原 H 方程

前稿的可逆尺度规范给四个不同物理代表 $z,w,u,v$，其中 H、V 的两个非零权分别吸收入平方根与立方根：
$$
H=\tfrac12(z^2+w^2),\qquad V=\tfrac12(u^3+v^3).
\tag{2.1}
$$
五列 $(y,z,w,u,v)$ 独立。原物理自等向关系给四个值向量各自平方为零。记
$$
g=z^{\mathsf T}Kw,\quad e=u^{\mathsf T}Kv,\quad
A=z^{\mathsf T}Ku,\quad B=w^{\mathsf T}Ku,\quad
C=z^{\mathsf T}Kv,\quad D=w^{\mathsf T}Kv.
$$
该唯一规范准确满足
$$
p(z)=p(w)=0,\qquad p(u)=p(v)=e,\qquad Fge\ne0,
\tag{2.2}
$$
$$
F^2+g^2=0,\qquad C=-A,\qquad D=-B,
\tag{2.3}
$$
$$
A^2+B^2=e^2,\qquad AB=-\frac{Fg}{2},\qquad
2e^3=Fg^2=-F^3.
\tag{2.4}
$$
三次单位根选择已在前稿全部保留并通过可逆代表缩放归入 (2.2)，不另外假设某一实根。

现在保回前稿 §4 的**两个分别的**原 H 值方程，而不只保它们相加的后果。完整原 H 梯度由
$$
N=Fyy^{\mathsf T}-2FH
-2\{y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\}
+4HKH+4V_p
\tag{2.5}
$$
的物理极线恒等式 $u(x)^{\mathsf T}KNKu(x)\equiv0$ 给出。在 (2.1)—(2.3) 上，
$$
Hp=0,\quad HKH=\tfrac g4(z\otimes w+w\otimes z),\quad
V_p=\tfrac e2(u^2+v^2),
$$
故完整 N 为
$$
N=Fy^2-F(z^2+w^2)+g(z\otimes w+w\otimes z)+2e(u^2+v^2).
\tag{2.6}
$$
在实际物理值 $z,w$ 分别评价零极线，得到
$$
\boxed{
2e(A^2+C^2)=Fg^2,\qquad
2e(B^2+D^2)=Fg^2.
}
\tag{2.7}
$$
这些是原全部 H 梯度的直接必要后果；它们不是额外假设。即使 $z$ 或 $w$ 在无穷远，物理齐次值的同一评价仍准确成立。

## 3. 原 Gaussian 例外给出特征零矛盾

将已经证明的 $C=-A,D=-B$ 代入 (2.7)，并用 (2.4) 的 $Fg^2=2e^3$。因为 $e\ne0$，逐条得到
$$
4eA^2=4eB^2=2e^3,\qquad
\boxed{A^2=B^2=\frac{e^2}{2}.}
\tag{3.1}
$$
另一方面，(2.3)—(2.4) 给
$$
(AB)^2=\frac{F^2g^2}{4}=-\frac{F^4}{4}.
$$
与 (3.1) 的 $(AB)^2=e^4/4$ 比较，得
$$
e^4=-F^4.
\tag{3.2}
$$
再把 (2.4) 的 $2e^3=-F^3$ 乘以 e，并代入 (3.2)：
$$
-2F^4=-eF^3.
$$
$F\ne0$，故
$$
e=2F.
$$
最后代回 $2e^3=-F^3$，得到
$$
\boxed{17F^3=0,}
$$
这在原特征零底域中与 $F\ne0$ 矛盾。

所以双约化的唯一 Gaussian 候选也不存在。结合已经支付的其余全部物理类型，本质五维反设被完全排除，(1.1) 证毕。

## 4. 对当前课题的准确收紧

结合[rankH 至多一的完整本质维数界](R150-appendix-rank-two-third-cumulant-rank-at-most-one-second-cumulant-essential-bound.md)，得到
$$
\operatorname{rank}V=2,\quad\operatorname{rank}H\le2,\quad
\nabla\mathcal Q_3=0
\quad\Longrightarrow\quad
\dim\operatorname{ess}(T_3)\le4.
$$
因此在 rankV2 层中，潜在本质五、六维临界点必有 $\operatorname{rank}H\ge3$。本质四维层仍须继续研究；本文不由维数界声称其三个原匹配 Bell 已经为零。更高 rankV、全局 Jacobian 自然幂来源与普通 ISP 完成标准也保持各自原缺口。

上一规范稿的有限 Gram、原物理二次/三次投影只是当时正确的必要归约。现在 (2.7) 与相反交叉列已经排空该规范，所以不再需要为那个规范运行新的有限域扫描、物理曲面求解或大消元门。本结论是上述显示方程的纯手证，没有新的计算执行身份；所有已完成源也不重跑。
