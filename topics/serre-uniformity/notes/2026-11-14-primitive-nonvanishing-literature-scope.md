# 原本原角色非消失：所核文献的适用范围

日期：2026-11-14。性质：文献路线核查及尚缺的接口，不是新的全素数非消失定理。

## 当前实际对象

R616 的指定原家族是
$$
g_{\theta,\pm}=\operatorname{AI}(\Psi_\theta\kappa^{\pm1}),\qquad
\Psi_\theta((a))=a\epsilon_3(a)\theta(a),
$$
水平 $108p^2$，根号分别为 $-1,+1$，$\theta$ 为原 $p+1$ 阶角色。
必须证明指定本原轨道的
$L'(g_{\theta,+},1)L(g_{\theta,-},1)\ne0$，不能改成任意角色的某次非消失。
R616 §6.1 的 ring-class 重写准确是
$$
\Psi_\theta\kappa^{\pm1}=\lambda_{p,\pm}\nu,\qquad
\lambda_{p,\pm}((a))=a\kappa((a))^{\pm1}\kappa_p((a))^m .
$$
这里 $\kappa_p^m$ 必须保留，基角色依赖 $p$。截至本笔记，
R714 仅覆盖其明确的充分区域；R719 已单独闭合实际 $p=137147$。
复非零与原 $M_2$ 或 $C_p$ 的模 $p$ 单位性是不同命题。

## 1. 固定素数的反圆分塔不能直接替代变化素数的首个 tame 层

Ashay Burungale、Wei He、Ye Tian、Xiangdong Ye，
*Mod $\ell$ non-vanishing of self-dual Hecke $L$-values over CM fields and applications*，
2025，arXiv:2508.19706v1，§1.2、Theorems 1.1、1.4：
<https://arxiv.org/html/2508.19706v1>。

Theorem 1.1 固定自对偶 $\lambda$ 及素点 $\mathfrak p$，变化的是反圆分
$\mathbb Z_p^{\deg\mathfrak p}$ 扩张的有限阶角色，并限制根号 $+1$。
其模 $\ell$ 结论要求不同的素数 $\ell\ne p$ 及相应 ordinary 假设。
这些量词不包含本题随 $p$ 变化、阶整除 $p+1$ 的指定 tame 角色，
也不直接提供负根号导数或模同一个 $p$ 的单位性。需要额外证明首层
tame 角色及变化基角色的统一接口；“除有限个塔角色外”本身不能给出它。

## 2. 横向 Heegner 点结果的固定映射与指定本原投影缺口

Xiaoyu Zhang，*Strengthenings of Mazur's Conjecture for Higher Heegner Points*，
2026，arXiv:2602.07210v1，Theorems 1.3、1.4、Remark 1.5：
<https://arxiv.org/html/2602.07210v1>。

Theorem 1.3 对固定模参数化 $\pi$ 及固定有限代表集 $\mathcal T$，
给充分大素数的 $\sum_{\sigma\in\mathcal T}\sigma(y[p])$ 非挠。
Theorem 1.4 的常数依赖 $(\pi,\ell,\mathcal T)$，导子须与
$\ell ND_{L/\mathbb Q}$ 互素。文章亦处理 Shimura 曲线。

本题原商及水平 $108p^2$ 随 $p$ 改变，且所需是指定本原角色投影；
现有证明未把它转换为该固定 $\pi,\mathcal T$ 的点和。
即使只看固定一个 $p$，把导子 $p$ 放进 $p\mid N$ 的原模参数化
也不满足所列互素条件。因此不能仅以“horizontal”一词代替接口。
以上是适用范围的检查，不是否定该文结果。

## 3. 撤回版本不作为现成黑箱

Jeanine Van Order，
*Class group twists and Galois averages of $\operatorname{GL}_n$-automorphic $L$-functions*，
arXiv:1903.06722v3（2023-11-12）：
<https://arxiv.org/abs/1903.06722v3>。

截至核查日，官方页面标记该版本已撤回，作者说明的缺口涉及
$n\ge3$ 时由非 $\mathbb Z$-finite 提升形式的 $L^2$ 分解导出
shifted-convolution 界。故不把该版本的总非消失声明作为本题黑箱。
这不声称所有 $n=2$ 估计都错误；若使用其中任何具体估计，
仍须逐项证明其适用条件与所需统一性。

## 4. Dirichlet 的素数幂 Galois 轨道不能直接替代本 CM 家族

Rizwanur Khan、Djordje Milićević、Hieu T. Ngo，
*Non-vanishing of Dirichlet L-functions in Galois orbits*，
IMRN 2016，6955–6978；arXiv:1507.00111：
<https://arxiv.org/abs/1507.00111>。

该文研究固定素数的大幂模数上、指定阶的 primitive Dirichlet
角色轨道中的非消失比例。本题是变化惰性素数处的 CM Hecke 角色，
并同时需要原负号导数与正号值；没有建立将前者定理传到后者的公式。
仅有“指定阶的 Galois 轨道”这一相似性不足以完成证明。

## 保留的实际任务

继续原 $\kappa_p^m$ 和原 signed-ray 核下的本原平均，
或建立确实覆盖变化 $p$、原六水平、指定本原投影的新几何／解析接口。
不得从已核文献直接登记全 $p$ 非消失、$C_p$ 单位或 Serre 一致性。
