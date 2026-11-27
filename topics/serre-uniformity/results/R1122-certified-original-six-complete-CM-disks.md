# R1122：原 full47 的六个完整 CM 圆盘已关闭

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：已证明，新的公开 QC 精确计算全部成功。**
原 $X_{\rm ns}^+(47)$ 在 $q=4513$ 的候选标签
$$
76,\ 77,\ 100,\ 108,\ 196,\ 220
$$
这六个**完整原圆盘**中，原两个 QC 方程的共同零只有对应的原 CM 点。
因而这些圆盘中没有其它 $\mathbf Q$ 有理点。
本结论使用全73维高度配对和全部原尾项，不只排除某个更深的未知小邻域。

标签0、141的两个原圆盘仍需其自己的第三类微分值和实际 QC 行。
固定47分类尚未在本篇全部完成；一般素数的 Serre 绝对一致性仍开放。

## 1. 真实公开执行

- source：[15859fc74cdb06b5bd04742a2676113b8dd1bffd](https://github.com/Rogerhu12/math-research-public/commit/15859fc74cdb06b5bd04742a2676113b8dd1bffd)。
- [run45996561850](https://github.com/Rogerhu12/math-research-public/actions/runs/45996561850)，
  [job140497301328](https://github.com/Rogerhu12/math-research-public/actions/runs/45996561850/job/140497301328)，attempt1。
  checkout、固定镜像、数学步骤及整个 job 全部 success。
- 数学总耗时 **117.952761184秒**；数学预算2400秒、reserve60。
- 固定 SageMath10.6 官方镜像、python-flint0.9.0；
  原有限域输入仍与 Sage fresh-exec 隔离。
- root读取完整公开日志，核 source、请求 SHA、六条完整新行、
  completed 的完整 canonical SHA。
  所有六条均为 matrix_rank=2、gcd=[0,1]、
  some_linear_coefficient_is_a_unit=true。

本次没有重算 R1102 的局部高度、R1120 的 CM 坐标或 R1121 的十二个局部值。
原角、原切向、原生成元对数和旧基在必要输入再生时逐项比对既有完整哈希，
没有重新进行已成结论的扫描或搜索。

## 2. 同一个原73维配对

始终取原
$$
P_0=B_qu_{-4},\quad B_q=q+1-T_q,\quad
H=T_3+T_5,\quad
L=[\lambda_0,H\lambda_0,\ldots,H^{72}\lambda_0],
\quad \lambda_0=q^{-1}\log P_0.
$$
此次必要输入再生给
$$
\det L=4475\ne0,
$$
完整矩阵 SHA 为
6b0537de198a5431b0eb0d7c4907155d54ef643422b5c5b27142db203dc6d618。
原73维 $\lambda_0$ 的 SHA 仍严格等于 R1093 的既有值。

令 $a=(T_2-1)/2$，R1102的完整高度给
$$
q^{-1}h(xP_0,yP_0)=\operatorname{Tr}_{\mathcal T/q}(Kxy),
\qquad K=\kappa/a.
$$
程序核全部旧高度 moments、trace Gram、$\kappa$ 和 resolvent 的哈希，
并核旧 Norm$(K)=2992$、原高度 determinant3972。
本次实际使用的 $K$ 全73系数 SHA 为
48842ecac11d0b32163b3c4ba97c208aac71a3d8c56d1637fac94cd25bdb7ff0。

八点实际切向为 $b_y=L^{-1}e_y$。
R1120的四条基本坐标及原 $T_2,T_3$ 关系给全部八点 $c_y$，
其共同 SHA 为
6e4b18e32a99bfcd38d265bb66e3947e23537e036d0304ff9d3861a5f37f12e1。
这里 $c_{-4}=B_q^{-1}$，没有误置为一。

## 3. 两条独立来源的完整矩阵桥已通过

R1121由73个原自由帧计算的 Cartier row matrix，
与 R1120原 Jacobi/Hecke 坐标形成的
$$
1-B_q(H)=\bar T_q
$$
在**同一原73维 Hodge 帧**上逐项一致。
程序比较完整矩阵的 canonical SHA，准确为
deda5ed6dbe8122f243c46bb60245cf8facc00b6040a8f34958c9ca4241d855d。

这一步通过之后才接受 R1121 的第三类值。
所以不是仅凭维数、谱、行列式或抽象代数同构把两组来源接在一起。
原列作用与 row 作用的转置已经明确保留。

## 4. 六盘的完整实际矩阵

原固定
$$
Z_A=13R_0+4R_2,\qquad Z_B=2R_4-7R_0.
$$
完整 fixed-cycle 函数仍为
$$
(F_4,F_3)(Z_A)=(13R_{20}+4R_5,\,13R_4),
$$
$$
(F_4,F_3)(Z_B)=(-7R_{20},\,2R_{12}-7R_4).
$$
原 Chow–Heegner 格坐标和新系数准确为
$$
d_{Z,y}=\frac{\frac12F_4(Z)c_{-4}+\frac23F_3(Z)c_{-3}-2Zc_y}{23},
$$
$$
A_{Z,y}=-\operatorname{Tr}(KZb_y^2),\qquad
B_{Z,y}=\operatorname{Tr}(Kb_yd_{Z,y})-\alpha_{Z,y}.
$$
每一项 trace 保留全部73方向。
原 $\alpha$ 已在 R1121 除六，消费者没有再除一次。

以下均为模4513的准确值，矩阵行次序为 $Z_A,Z_B$，
列次序为 $A,B$：

| 标签 | $A_A$ | $B_A$ | $A_B$ | $B_B$ | $\det\begin{pmatrix}A_A&B_A\\A_B&B_B\end{pmatrix}$ |
|---:|---:|---:|---:|---:|---:|
| 76 | 3664 | 2667 | 4252 | 828 | 2141 |
| 77 | 1549 | 515 | 3390 | 3945 | 884 |
| 100 | 3881 | 2348 | 128 | 707 | 1790 |
| 108 | 948 | 1924 | 2173 | 3060 | 1720 |
| 196 | 4320 | 700 | 1825 | 1173 | 3453 |
| 220 | 2135 | 1366 | 3108 | 2519 | 4287 |

六个行列式全部非零。
每行还分别输出实际全局线性项、实际 $\alpha$、
原 $b_y,d_{Z,y}$ 的完整坐标哈希，
以便区分全局线性项与其减去局部值后的 $B$。
这些完整小行保存在公开 receipt 中，不以一张 rank 表代替来源。

## 5. 为什么这关闭整个原圆盘

R1103已在原整参数
$$
z=j-j_{\rm CM}=4513t,\qquad t\in\mathbf Z_{4513}
$$
上付清完整 restricted-analytic 尾项，并证明两个原 QC 函数的约化为
$$
\bar f_{Z,y}(t)=t(B_{Z,y}+A_{Z,y}t).
$$
全部非4513局部项沿 R1103 §6.1 的原整 Poincaré 刚化消失；
坏47项沿 R1074 的 whole-tube 证明。
这些来源在实际请求中固定，未把有限测试点上的消失当成全盘消失。

本次逐盘实际求得
$$
\gcd(\bar f_{Z_A,y},\bar f_{Z_B,y})=t.
$$
故任意共同整零必须落在 $t\equiv0\bmod4513$。
又因至少一条 $B_{Z,y}$ 是单位，该条原函数在此剩余类中有唯一零。
对应的原有理 CM 点 $t=0$ 本身满足全部原高度关系，
所以该唯一零就是 $t=0$。
因此两个原方程在整个 $t\in\mathbf Z_{4513}$ 中的共同零恰为原 CM 点。

程序另外逐盘读取 common_roots=[[0,1]]。
它没有把 $t^2$ 的重根视为已证明唯一；
这里六个实际 gcd 都是简单的 $t$。

## 6. 完整复现信息

| 对象 | SHA-256 |
|---|---|
| QC v2 consumer | ac9ac63dd31556b6b4952c71a5aa4b9c1e4826c9ccfb044bace50090cf861ea4 |
| QC v2方法说明 | 0e46d51083eddfeb0188335f87dc748af82d82be743cb12255f0969b70a079ad |
| 本次六盘请求 | 95e8ccb0bd7906f1c0c47fbebc794c77994b3fd5cba58766d31fbc53ac3dbc0b |
| 完整 completed 结果 | 4ae1153bc0e4935e77313e4c9e0f3502aef54820cb6e8d9a3f124d0687cb6e36 |
| 完整 QC_first_rows 子证书 | 3f6a1213fcdaaf44ae25839ae9ae8878c3b268d08d787dd41ac825189ed55e08 |
| 消费的四基本 CM 记录 | b9f610583ea037e18d5e948341af5b09b78c8426a16f7643a6f44bd2949b882e |
| 消费的十二条第三类值 | 895d06ff05fab216225b5a6794295b3fb731d4ea5d1982935db365a4ebddcc09 |
| 消费的完整 Cartier 证书 | 3563933eb15259bdcaddb70d97b6b56c869e8fe3c997b0d64e16030caa7d9bfb |

入口：
[方法](../notes/2026-11-27-full-p47-QC-first-rows-method.md)、
[请求](../notes/full-p47-QC-first-rows-request.json)、
[消费者](../scripts/full_p47_QC_first_rows.py)。
原高度、CM坐标及局部值分别见
[R1102](R1102-certified-original-level47-complete-first-global-height.md)、
[R1120](R1120-certified-original-full47-signed-CM-coordinates.md)、
[R1121](R1121-certified-original-twelve-short-Cartier-values.md)。

仅保源、参数、小结果、run/job和哈希。
未保存完整旧级数、角目标矩阵或 trace 中间数组；
无 raw artifact 或 Release。

## 7. 剩余的真实任务

结合 R1074/R1086 的原全标签转移，
固定47现在只需关闭标签0、141的两个原 CM 圆盘。
它们尚无本次首层行，不由本表外推。
立即用已成功的短 Cartier 方法读取其四个未完成的原局部值，
再只读取这两个新盘的 QC 行；本篇六盘不重算。

课题的全素数目标仍要求绝对常数或真正无界反例族。
本固定47结果没有删除 open.md 的完整惯性、非整$j$、
变化二次域及一般$p$的原高度/短非零障碍，继续逐项推进。
