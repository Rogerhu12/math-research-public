# R150 附录：零第三累积量整层的三个匹配 Bell 值全零及消元理想的准确三阶幂零指数

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120（root 与 literature）；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 在原完整六模式立方临界系统中，只要第三累积量 $V=0$，原三个指定匹配 Bell 三次式在每个完整临界点都取零。该结论保留全部六个均值变量、全部十一条二阶梯度和全部六条均值梯度；没有 Cat 秩、Hankel 秩、本质维数、均值位置或 jet 支撑限制，也包括 $y=0$。

在原最高式确定的六变量 $V=0$ 图上，令 $I_0$ 为完整低梯度消元理想，则每个原匹配方向更精确地满足
$$
\boxed{\ \ell_r S_r^2\in I_0,\qquad
S_r^3\in I_0,\qquad S_r^2\notin I_0,\quad \ell_r=r^{\mathsf T}y.\ }
$$
因此 $S_r$ 在该六变量商环中的准确幂零指数为三。

正证书已实际以有理数求解，并逐项核验全部 $792\times3$ 行。本稿不将该消元图上的三次幂证书宣称为原三十三变量全局 Jacobian 理想中的同幂证书；一般 $V\ne0$ 的完整临界层继续保留。

## 1. 同一原最高式及完整六变量理想

保留 [原第三矩 Schur 稿](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md) 的 $K$、可逆 $J_2$、原 Hankel 坐标 $y,H,V$。写
$$
p=Ky,\quad
\mathbf d_2(y)=\big([z^m](p^{\mathsf T}v(z))^2\big)_{m=0}^{10}.
$$
在 $V=0$ 时，第三普通矩为
$$
T_3(r)=(y^{\mathsf T}r)
       \big[(y^{\mathsf T}r)^2-6H(r,r)\big].
\tag{1.1}
$$
若 $y\ne0$，因 $K$ 可逆，一次极线 $p^{\mathsf T}v(z)$ 非零。原完整最高式可在多项式整环中准确约去这一因子，故
$$
\boxed{\ H=H(y)=
\operatorname{Hankel}\!\left(\frac16J_2^{-1}\mathbf d_2(y)\right).\ }
\tag{1.2}
$$
这一步不要求任何 Cat 或矩阵秩条件。

在 (1.2) 上保留
$$
F=\tfrac12y^{\mathsf T}Ky,\quad
h=Hp,\quad b=p^{\mathsf T}Hp,\quad
\tau_2=\operatorname{tr}((KH)^2).
$$
原全部均值梯度除去已知可逆常数因子后为
$$
\Gamma=(F^2-2b+2\tau_2)y-4FHp+8HKHp.
\tag{1.3}
$$
最后一项是 $8H K H p$。原全部二阶梯度由
$$
N=Fyy^{\mathsf T}-2FH
 -2(yh^{\mathsf T}+hy^{\mathsf T})+4HKH,
$$
$$
n_m=[z^m]\,v(z)^{\mathsf T}KNKv(z),
\quad 0\le m\le10
\tag{1.4}
$$
给出，见 [完整原低阶梯度](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md)。

定义
$$
I_0=(n_0,\ldots,n_{10},\Gamma_0,\ldots,\Gamma_5)
\subset R=\mathbb Q[y_0,\ldots,y_5].
\tag{1.5}
$$
前十一项四次齐次，后六项五次齐次。没有以投影来源替换任何原方程。

## 2. 准确三个原匹配目标与此次七次目标

三个指定方向准确沿用 [原匹配方向定义](R150-appendix-all-essential-cubic-dimensions-at-most-three-have-zero-matched-bell-values.md) §4。令 $d_j$ 为
$$
P(d)=3725d^3-43931504d^2
+6080833024d+52565262336
\tag{2.1}
$$
的三个指定实根，置
$$
A(d)=-\frac{521d^2-46784d+271360}{160(5d-704)},
\quad B(d)=A(d)+d,\quad
r(d)=(A(d),B(d),0,0,0,1).
\tag{2.2}
$$
原分母在三根处都非零。

对每个方向定义原图上的一次、二次及三次式
$$
\ell_r=r^{\mathsf T}y,\qquad
Q_r=\ell_r^2-6r^{\mathsf T}H(y)r,\qquad
S_r=\ell_r Q_r.
\tag{2.3}
$$
$S_r$ 就是 (1.1) 的完整匹配 Bell 值，不是只保留一次矩的纯幂。

本次固定目标为
$$
U_r=\ell_r S_r^2=\ell_r^3Q_r^2\in R_7.
\tag{2.4}
$$
它有两个准确用途：在任一点 $U_r=0$ 已迫 $S_r=0$；在理想中乘以同一个二次式 $Q_r$ 则得到
$$
Q_r U_r=\ell_r^3Q_r^3=S_r^3.
\tag{2.5}
$$
因此这一七次目标足以证明所需三次自然幂归属，无需另建九次大矩阵。

在同一个自由三维有理代数
$\mathcal A=\mathbb Q[d]/(P(d))$ 中，准确展开
$$
U_{r(d)}=u_0(y)+d\,u_1(y)+d^2u_2(y),
\qquad u_k\in R_7.
\tag{2.6}
$$
三份有理系数目标同时保留，未挑选一个方便的代数根。

## 3. 完整七次来源与明确可重建的有理乘子

由 (1.5) 的齐次性，
$$
(I_0)_7=\sum_{m=0}^{10}R_3\,n_m+
          \sum_{i=0}^5R_2\,\Gamma_i.
\tag{3.1}
$$
因此行数与完整来源列数准确为
$$
\dim R_7=\binom{12}{5}=792,\qquad
11\binom85+6\binom75=11\cdot56+6\cdot21=742.
\tag{3.2}
$$

以下给出实际证书的精确定义，避免只报一个求解器的“成功”状态。把十七个原生成元顺序记为 $g_i$，对每个 $g_i$ 按生成器的确定顺序清分母、除内容，得
$$
G_i=c_i g_i\in\mathbb Z[y],\qquad c_i\in\mathbb Q^\times.
$$
同样令
$$
U_k=e_k u_k\in\mathbb Z[y],\qquad e_k\in\mathbb Q^\times,
\quad 0\le k\le2.
\tag{3.3}
$$
这些有理单位全部由原多项式逐项确定，不加入新假设。

按首坐标指数递减的递归字典次序生成全部七次单项式行；按原生成元顺序、再按相同单项式顺序生成 (3.1) 的 742 列。第 $j$ 列为
$$
y^{\alpha_j}G_{i_j}.
$$
所得完整整数矩阵记为 $M\in\mathbb Z^{792\times742}$，三目标列矩阵记为 $T\in\mathbb Z^{792\times3}$。

生成器在模 $103$ 中依确定 RREF 顺序选出 730 个源列 $J$，再对其转置依相同规则选出 730 个行 $I$。其小矩阵
$$
B=M[I,J]
\tag{3.4}
$$
的行列式模 $103$ 为 $65$，所以 $B$ 在 $\mathbb Q$ 中可逆。定义准确有理矩阵
$$
C=B^{-1}T[I,:]\in\mathbb Q^{730\times3}.
\tag{3.5}
$$
此次实际有理求解之后，独立用完整 792 行回乘核验了
$$
\boxed{\ M[:,J]C=T.\ }
\tag{3.6}
$$
不是只核选中的 730 行，也不是只核有限域。

于是对 $\mathcal A$ 中的 $d$，显式乘子可写成
$$
A_i(y,d)
=c_i\sum_{\substack{j\in J\\i_j=i}}
 y^{\alpha_j}\left(
 \sum_{k=0}^2\frac{C_{j,k}}{e_k}d^k
 \right).
\tag{3.7}
$$
其中 $C_{j,k}$ 指 (3.5) 中与选中原列 $j$ 对应的一行。由 (3.3)、(3.6)，准确有
$$
\boxed{\ U_{r(d)}=\sum_{i=0}^{16}A_i(y,d)\,g_i(y).\ }
\tag{3.8}
$$
式 (3.3)–(3.7)、原 $K,J_2$、原匹配三次及确定选行选列算法，完整指定了每个有理乘子；公开生成器可重建并逐行核验它们。实际乘子共 2190 个非零有理系数，最大分子 7849 个二进制位、最大分母 7647 个二进制位，故不把巨大的系数数组重复展开进文档。

对任一个指定根 $d=d_j$ 特化 (3.8)，再乘 $Q_{r_j}$，得到明确证书
$$
\boxed{\ S_{r_j}^3
=\sum_{i=0}^{16}\bigl(Q_{r_j}A_i(y,d_j)\bigr)g_i(y)
\quad(j=1,2,3).\ }
\tag{3.9}
$$
对四次来源的乘子为五次，对五次来源的乘子为四次，准确落在应有的九次齐次部分。

## 4. 实际运行及同源绑定

[固定七次正证书生成器](../notes/2026-11-20-r150-vzero-degree-seven-same-first-matched-bell-certificate-b2a9.py)
于 [Actions run 44732550495](https://github.com/Rogerhu12/math-research-public/actions/runs/44732550495)，job 136275725868，标签 vzero_degree7 实际运行完成。冻结提交35d0d768258a205cd0d78552fb7fbfa4018ec70a；UTC时间为2026-11-20 12:03，程序记录4.512022秒，最高RSS 152644 KiB。[批次运行身份](../notes/2026-11-20-exact-source-run44732550495-b2a9.json)保完整日志SHA、全部独立程序身份及真实pull回执。

本次准确输出为：

| 项目 | 结果 |
|---|---:|
| 完整行数 / 来源列数 | 792 / 742 |
| 原来源非零矩阵项数 | 97720 |
| 模 $103$ 源秩 / 三目标增广秩 | 730 / 730 |
| 所选单位子式阶 / 模行列式 | 730 / 65 |
| 实际 QQ 求解 | 已执行 |
| 完整 QQ 回乘 | 三份目标各 792 行 |
| 三份非零残差项数 | 0，0，0 |
| 有理非零乘子数 | 2190 |

程序还把本次原 $H(y)$、原十七个低梯度和 primitive 生成元的三个 SHA256 分别与上一已执行的六次源作硬比较，全部一致。这阻止在本次正结果中暗换消元图或删改原低梯度。原最高系数的有理解、$\tau_2=b/6$、全部低梯度的原物理均值控制及三个原匹配 conic 身份均再次通过。

关键对象的 SHA256 为：

| 对象 | SHA256 |
|---|---|
| 执行源 | e9efe34e78901f747660613a869a7a0c0bbfa4f2ee1a4d6ddab10814027ab713 |
| 完整七次来源矩阵 | 4e5e48765b15fe6e69c2868e3082e4251006fb06e77bd9d7cbd764c282110673 |
| 完整三目标矩阵 | 34697a05c5babe107e83fc4bc7dffca34ffa85d06858039087a97af001cc4757 |
| 实际有理乘子矩阵 | 1b46bab3e774eddf2b220b1c6af8d50d2e37b01fa3afa0230c94c8e33acbbff4 |
| 选中原列顺序 | f7ed3dc07669ea91c6ec781650a70d072f70eb3f2e31803fe4c17c4724d7ff59 |
| 选中原行顺序 | 4507b5648fe792495dbbfe4703e3e33400f1dd971515b35a9bf21bfdfce522c4 |
| 标准输出 | e9711645d00c512623323ffef656c5e65e6fd44b894e35f6101f189adb9c3e48 |

这里有限域仅用于选择一个有理可逆子式；正证书本身来自实际 QQ 乘子和 (3.6) 的完整有理回乘。既不需要假设模秩等于全矩阵有理秩，也不需要完成任意更大来源的秩计算。

## 5. 零第三累积量整层的匹配值全零

取原任意完整临界点，假设 $V=0$。

若 $y=0$，直接由原完整式
$$
S_r=(r^{\mathsf T}y)^3
-6(r^{\mathsf T}y)r^{\mathsf T}Hr+4V(r,r,r)
$$
得到 $S_r=0$，与 $H$ 的秩或值无关。

若 $y\ne0$，原完整最高式给 (1.2)，其余全部原低梯度给
$$
g_0(y)=\cdots=g_{16}(y)=0.
$$
由 (3.8) 得 $\ell_{r_j}S_{r_j}^2=0$。若 $\ell_{r_j}=0$，(2.3) 已给 $S_{r_j}=0$；若 $\ell_{r_j}\ne0$，则 $S_{r_j}^2=0$，在 $\mathbb C$ 中仍给 $S_{r_j}=0$。也可直接在 (3.9) 评价得到同一结论。

因此对原三个指定方向，
$$
\boxed{\ \nabla\mathcal Q_{F_0^3}=0,\quad V=0
\quad\Longrightarrow\quad
S_{r_1}=S_{r_2}=S_{r_3}=0.\ }
\tag{5.1}
$$
此处没有任何本质维数限制，故包括此前保留的 $V=0$ 本质五/六维层和所有均值 Cat 退化。它证明的是匹配值消失，不断言这些层全部没有临界点。

## 6. 消元图上的准确幂零指数为三

[六次完整来源秩夹逼](R150-appendix-zero-third-cumulant-degree-six-three-matched-squares-are-not-members.md) 已证明，对同一个 $I_0$ 及每个指定根，
$$
S_{r_j}^2\notin I_0\mathbb C[y].
\tag{6.1}
$$
那里的源矩阵模秩达到全部 267 列、三目标增广模秩达到全部 270 列，故已经严格提升到特征零；本稿没有重跑该结论。

由 (3.9) 和 (6.1)，
$$
\boxed{\ \min\{n\ge1:S_{r_j}^n\in
 I_0\mathbb C[y]\}=3,\qquad j=1,2,3.\ }
\tag{6.2}
$$
若一次幂已经在理想中，其平方也应在理想中，故无需另做一次幂检验。

这关闭了六变量 $V=0$ 图上该自然幂问题，并关闭原 $V=0$ 整个临界层的三份匹配值问题。备用九次生成器不需要执行。

## 7. 与原完整问题的边界

式 (3.9) 是在 $V=0$、$H=H(y)$ 的消元图中成立的明确理想证书。这里的最高式消元使用了非零极线因子，且在原变量中仍有一般 $V\ne0$ 分支。因此不能把 (6.2) 直接搬成原三十三变量 Jacobian 理想中的同指数结论，也不能仅凭这一层的真实匹配值消失代入完整算子逆分母定理。

已付的全部本质维数至多三结果和本稿可以同时保留。若原完整临界点有任一匹配 Bell 值非零，则现在必须同时满足
$$
V\ne0,\qquad \dim\operatorname{ess}(T_3)\ge4.
$$
一般第三累积量非零的剩余完整临界层、原全局自然幂归属及实际算子来源继续研究；普通 Hilbert 不变子空间问题未由本稿解决。
