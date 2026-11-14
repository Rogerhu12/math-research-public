# R228 — 单个原中央方向的完整 Hasse 族与标量隐藏像

日期：2026-11-13。**状态：在 $r>2D$ 的原主素数范围，单个 primitive 实际中央方向与原标量前缀的联合整性、每层隐藏像的单射、原方向缩放后的准确有限像及最优观察指数均已证明。它们把定向下降的代价固定到同一个原 Smith；没有产生新的深关系或中央非零，主课题未完成。**

本篇对象是 R189 的全部中央–Hasse **系数行族**，指标为 $a+b\le D-1$。结论以这个完整族为单位，不单独断言某一条选行具有相同观察指数。原多项式、原曲线、原标量前缀始终保留。

## 1. 同一原源、实际方向与有限核

取
$$
 p=4r-1\ge19,\qquad r>2D,\qquad D\ge1,\qquad k>2D,
 \qquad O=\mathbf Z_p.
 \tag{1}
$$
所以 $p>D$。原源为
$$
 E_D=O[A,C]_{\le D},\qquad
 A(w)=w+\cdots,\quad C(w)=v_0w^2+\cdots,\quad v_0=-22.
$$
令 $J=J_{D,<k}$ 为原全部连续行的真实归一矩阵，使用 R215 的全深权 $e_n$。在 $0\le n\le2D$ 上，$e_n=0$。R215 保证整个 $J$ 在原源上整。

取一个实际非零中央向量
$$
 q=(q_A,q_C)\in O^2,\qquad
 \kappa=\min\{v_p(q_A),v_p(q_C)\},\qquad q=p^\kappa v,
 \quad v=(v_A,v_C)\in O^2\text{ primitive}.
 \tag{2}
$$
例如可取 R189 的某个非零 $q_t$，或 R203 已整化的实际 $t_t$ 行。证明只使用其实际值；不更换方向或选择未来轴系数。

R189 的完整系数族准确是
$$
 \mathcal H_q(P)
    =\operatorname{coeff}\bigl(D_qP\bigr),\qquad
 D_q=q_A\partial_A+q_C\partial_C:E_D\longrightarrow E_{D-1}.
 \tag{3}
$$
对 $P=\sum P_{a,b}A^aC^b$，其第 $(a,b)$ 行是
$$
        (a+1)q_AP_{a+1,b}+(b+1)q_CP_{a,b+1},
                 \qquad a+b\le D-1.
 \tag{4}
$$
因此 $\mathcal H_q=p^\kappa\mathcal H_v$。

对精度 $N\ge1$，在原有限源 $E_D/p^NE_D$ 中记
$$
 K_N=\ker(J\bmod p^N),\qquad
 B_N(J)=N M_D-\operatorname{length}(\operatorname{im}J\bmod p^N),
 \quad M_D=\binom{D+2}{2}.
 \tag{5}
$$
准确有 $\operatorname{length}K_N=B_N(J)$；不要求 $J$ 此时已满列秩。

## 2. 原标量加一个 primitive 方向就整地检测整个原源

**定理 1。** 联合矩阵
$$
                             \begin{pmatrix}J\\\mathcal H_v\end{pmatrix}
 \tag{6}
$$
有整左逆。

**证明。** 选 $\alpha,\beta\in O$ 满足
$\alpha v_A+\beta v_C=1$，作原变量变换
$$
                 X=\alpha A+\beta C,\qquad
                 Y=-v_CA+v_AC.
 \tag{7}
$$
其行列式是一，所以在每个原有限次数源上都是 $GL(O)$ 变换，保持原系数 Gauss 范数。准确有
$$
                         D_vX=1,\qquad D_vY=0,
$$
故 (3) 在新变量上就是 $\partial_X$。

由于 $p>D$，所有 $1,\ldots,D$ 都是单位。于是
$$
 E_D=O[Y]_{\le D}\oplus X\,O[X,Y]_{\le D-1}
 \tag{8}
$$
是原整直和，而 $\partial_X$ 在第二项到 $E_{D-1}$ 上为整同构：在单项式上只乘 $i\in\{1,\ldots,D\}$。因此只须证明原 $J$ 在 $O[Y]_{\le D}$ 上有整左逆。

若 $v_C$ 为单位，则
$$
                     Y(w)=-v_Cw+O(w^2).
$$
在源 $(1,Y,\ldots,Y^D)$ 上选真实行 $0,1,\ldots,D$，得到下三角矩阵，对角 $(-v_C)^j$ 全为单位；这些行权全为零。

若 $v_C\in pO$，则 $v_A$ 是单位，并且在原整低区间中
$$
                        \overline Y(w)=v_Av_0w^2+O(w^3).
$$
这里一次系数虽可在特征零非零，但模 $p$ 为零；二次系数模 $p$ 准确是 $v_Av_0$。选择真实行 $0,2,\ldots,2D$，其约化矩阵下三角，对角 $(v_Av_0)^j$ 全为单位。由 $2D<r$，这些归一行仍没有额外 $p$ 因子。因此这份原 minor 也是单位。

按 (8) 分源，并对梯度输出作相应原整换基后，(6) 形如
$$
                       \begin{pmatrix}J_Y&J_X\\0&I\end{pmatrix}.
$$
减去下方单位行的整组合，便成为
$\operatorname{diag}(J_Y,I)$；刚才证明 $J_Y$ 有单位 minor。于是 (6) 有整左逆。$\square$

这个证明使用的是实际 $Y=-v_CA+v_AC$ 及实际原低行。它没有用自由曲线、任意列旋转或中央删轴模型。

## 3. 每个原消失向量上的准确最低值

对向量取坐标赋值的最小值，记为 $\nu_p$。由定理 1 及原矩阵整性，对每个原 $P$ 准确有
$$
 \boxed{\quad
 \nu_p(P)=
    \min\{\nu_p(JP),\nu_p(\mathcal H_vP)\}.
 \quad}                                                       \tag{9}
$$
这里 $\nu_p(P)$ 是原系数的最小赋值。

特别，若 $P$ 在原源中 primitive 且
$JP\in p^TO^k$，$T\ge1$，则
$$
 \boxed{\qquad
       \nu_p(\mathcal H_vP)=0,\qquad
       \nu_p(\mathcal H_qP)=\kappa .
 \qquad}                                                       \tag{10}
$$
所以原标量消失向量的完整中央–Hasse 族确实含有一条达到 (10) 的实际系数行；不能因 $q$ 本身很深，就再给这个原向量的完整族增加未经证明的消去。

(10) 对每个实际 primitive 方向成立。若只保留 (4) 中某一条固定选行，它可能在给定 $P$ 上消失，不能单独套用本结论。

## 4. 各有限精度中，全部隐藏像都被这个方向检测

**定理 2。** 对每个 $N$，
$$
                        \mathcal H_v:K_N\longrightarrow E_{D-1}/p^N
 \tag{11}
$$
是单射。因此
$$
 \boxed{\quad
 \operatorname{length}\mathcal H_v(K_N)=B_N(J)
 =\operatorname{length}\operatorname{im}
            \begin{pmatrix}J\\\mathcal H_v\end{pmatrix}_{\bmod p^N}
    -\operatorname{length}\operatorname{im}J_{\bmod p^N}.
 \quad}                                                       \tag{12}
$$

**证明。** 若 $P\in K_N$ 且 $\mathcal H_vP=0\bmod p^N$，则 (6) 的整左逆给 $P=0\bmod p^N$。投影联合像到原 $J$ 像的核，准确是 $\mathcal H_v(K_N)$，得 (12)。$\square$

原 $q=p^\kappa v$ 的缩放也可以准确支付。若原 $J$ 的 Smith 指数为 $s_i$，对准确零列记 $s_i=+\infty$，则
$$
 K_N\simeq\bigoplus_i O/p^{\min(N,s_i)}.
$$
由于 (11) 是 $O$ 线性单射，
$\mathcal H_q(K_N)$ 与 $p^\kappa K_N$ 同构。因此
$$
 \boxed{\quad
 \Delta_{q,N}:=\operatorname{length}\mathcal H_q(K_N)
   =\sum_i(\min(N,s_i)-\kappa)_+
   =B_N(J)-B_{\min(N,\kappa)}(J).
 \quad}                                                       \tag{13}
$$
约定 $B_0=0$。特别 $N\le\kappa$ 时原未除公因子的族不增加任何模 $p^N$ 信息；$N>\kappa$ 时它准确检测超过这个共同缩放的 Smith 尾。

这份等式也等于给原矩阵 $J$ 添加完整行族 $\mathcal H_q$ 后的实际有限像长度增量。它不是环境目标维数的估计。

## 5. 定向下降的最优全精度指数

**定理 3。** 假设 $J$ 满列秩，最大 Smith 指数为 $s_{\max}(J)$。存在整矩阵 $\mathsf U$ 使
$$
                         p^c\mathcal H_q=\mathsf U J
 \tag{14}
$$
的最小整数 $c\ge0$，准确为
$$
                 \boxed{\quad
                  c_{\min}(q,J)=\max\{0,s_{\max}(J)-\kappa\}.
                 \quad}                                     \tag{15}
$$
若 $J$ 不满列秩，则不存在有限 $c$。

**证明。** 对 primitive 方向 $v$，定理 1 表明 $J$ 的行与
$\mathcal H_v$ 的行共同生成整个原源对偶格。于是
$p^t\mathcal H_v$ 的全部行属于 $J$ 行格，当且仅当
$p^tI_{M_D}$ 的全部行属于 $J$ 行格：一个方向是包含关系；另一个方向用 (6) 的整左逆，并注意 $p^tJ$ 的行原本就在 $J$ 行格内。

满秩 Smith 形式将最后的条件准确化为 $t\ge s_{\max}(J)$。
将 $t=c+\kappa$ 代入，即得 (15)。若原 $J$ 秩不足，该行格不能包含任何 $p^tO^{M_D}$，故无有限 $c$。$\square$

这是全精度统一的准确系数观察指数。与 R224 §7.3 相比，本篇主区间全部原源角权为零，所以这里 $J=\widehat J$。特殊中央方向本身不能降低 primitive 完整族的观察指数；能够降低 (14) 的，只有 (2) 中实际保留的共同 $p^\kappa$ 缩放。

## 6. 把真正的中央规范代回

设 $q_t$ 是 R189 的实际第 $t$ 个中央部分和，双完整中央零给
$$
 q_t\in p^{L_t}O^2,\qquad L_t=t+v_p(t!).
$$
若 $q_t\ne0$，写其实际赋值
$$
                   \kappa_t=L_t+\kappa_t',\qquad\kappa_t'\ge0.
$$
对规范化行族 $q_t/p^{L_t}$，定理 2—3 准确给
$$
 \Delta_{q_t/p^{L_t},N}
       =B_N(J)-B_{\min(N,\kappa_t')}(J),
$$
$$
 c_{\min}(q_t/p^{L_t},J)
       =\max\{0,s_{\max}(J)-\kappa_t'\}.
 \tag{16}
$$
对任意原 primitive 标量消失向量 $P$，其该完整规范化族的最低赋值恰为 $\kappa_t'$，由 (10) 得出。

所以双完整零提供的 $L_t$ 层在规范化后已经支付；剩余 $\kappa_t'$ 必须用原实际值计算。不能一方面把 $q_t$ 的大公因子用于降低定向观察成本，另一方面又把除去同一公因子后的 primitive 族当成免费已观察的数据。

本篇不声称某个 $q_t$ 的公因子恰等于 $L_t$，也不把两个不同 $t$ 的目标规范混同。只要选取一个实际非零行，全部定理就适用；无需预先支付两个方向的行列式。R195 已给原首次两行的特征零独立性，因而可用的实际非零行确实存在。

## 7. 与 R218 原交集的剩余连接

在 R223 的主素数带 $p\asymp K_D\asymp D^2$、满秩完整前缀
$k=K_D+1$ 上，$r>2D$ 成立。R223 已证明，累计原交集
$I_{p,N}$ 与 $B_N(J)$ 只差 $O(D)$。因此 (12) 把同一主项准确改写为
$$
          \operatorname{length}
             \bigl(\mathcal H_v(\ker(J\bmod p^N))\bigr)
$$
的原实际长度，误差仍只有已付的 $O(D)$。这是一份可用于构造的目标，不是已经得到的增长下界。

若要获得所需主阶，仍须在同一个原源中构造足够多、足够深的原标量关系，或直接证明 R218 的真实交集下界。把完整中央–Hasse 族另行加入目标、或只展示它能检测原隐藏向量，均不会完成这一步。对于本篇这份完整方向族，恢复代价已经由 (13)、(15)—(16) 完全固定；后续应研究实际关系本身，而不再把这项观测等价当作新增净收益。

依赖：
[R189](R189-complete-central-hasse-families-and-weighted-core.md)、
[R195](R195-fixed-five-adic-moments-and-first-two-central-rows.md)、
[R203](R203-finite-central-companion-and-rational-row-lattices.md)、
[R206](R206-fourth-layer-interior-schur-and-true-deleted-column-quotient.md)、
[R215](R215-full-depth-faber-transport-and-first-cross-band-carry.md)、
[R218](R218-all-degree-original-image-intersection-recursion.md)、
[R223](R223-large-prime-deep-smith-and-original-product-input.md)、
[R224](R224-radial-image-euler-hasse-observation-and-cross-degree-relations.md)。
