# R248：真实终点换代表、主函数链与普通盘第二类大积分

日期：2026-11-13。本条以 R240 的 54 个实际变分第二类微分为固定输入，并接续 R241 的真实群运算。它给出从任意已完成普通盘倍乘到全部 54 个第二类大积分的实际接口，且首先在 `ORD_j05` 完整执行成功。其他普通盘的同一计算继续运行；本条的首个封存证书不把这些尚未完成的盘提前计入。

## 1. 对象与已完成范围

记 \(b=P_{-3}\)，\(C=P-b\)，\(L\) 为次数 126 的 Makdisi 线丛，\(f_0\in H^0(L)\) 为固定的规范截面。每个真实有效代表 \(E\) 对应的次数零除子记为

\[
 D_E=E-\operatorname{div}(f_0).
\]

R240 的第二类微分按 R141/R145 第二 Abel 族的 54 个点 \(P_{2,j}\) 排序，物理参数为 \(t_j=B-32\)。规范是

\[
 \nu_j=\left.\frac{\partial}{\partial t_j}
              \eta_{A_2(t)}\right|_{t=0},\qquad
 A_2(t)=\sum_j(P_{2,j}(t_j)-P_{2,j}(0)).
\]

它们有指定的单位双极主部、零留数，并已由 R141 的真实 Poincaré Hessian 校准全纯部分。本文使用的最终 R240 文件哈希是

`9788da4bb748b98ebfb87014248b0791bba1caa71dc664aa3f2ba83c9ef76945`。

R240 的实际变分规范保证，对主除子有

\[
 \int_{\operatorname{div}(f)}\nu_j
 =\left.\frac{\partial}{\partial t_j}
          \log\operatorname{Norm}_{A_2(t)}f\right|_0
 =\frac{f'}f(P_{2,j}).                                      \tag{1}
\]

这也可直接由规范局部高度在主除子上的 norm 恒等式对 \(t_j\) 求导得到。后文每个校正都计算 (1) 右端的真实有理函数，而没有把一个抽象 Jacobian 类的梯度直接当作指定除子的梯度。

在 `ORD_j05`，本条已完成：

- 454 条实际 AddFlip 和初始负点的全部主函数保存；
- 真实终点向 R141 第一微小 Abel 族的显式换代表函数；
- 全部 54 个真实第一族参数与微小第二类积分；
- 全部 \(455\times54=24570\) 个链上 norm 导数及其准确直线程序累加；
- \(C=P_{\text{center}}-b\) 的全部 54 个第二类大积分，模 \(47^4\)。

它们与已经独立完成的 54 个全纯积分一起，给出该盘中心的完整 108 维 de Rham 积分输入。本文没有把这些积分等同于 53 个实际 QC 局部高度函数，也未宣称共同根已完成。

## 2. 保留每条群运算的主函数

R241 使用的初始有效除子为

\[
 E_P=\operatorname{div}(f_b)-b+P,
 \quad D_{E_P}=C+\operatorname{div}(f_b/f_0).
\]

新的捕捉器 `p41_ordinary_Abel_with_transports47.py` 包装已经封存的 R241 引擎，不修改它的随机数、主元、点坐标或群运算。对一条 AddFlip，它保存实际选出的

\[
 F\in H^0(3L),\qquad
 \operatorname{div}(F)=E_P+E_Q+E_R,
\]

所以相应的真正有理函数为 \(g=F/f_0^3\)，满足

\[
 \operatorname{div}(g)=D_P+D_Q+D_R.                         \tag{2}
\]

普通负点 flip 同样保存 \(F\in H^0(2L)\) 和 \(F/f_0^2\)。分子在既有 V3 或 V2 基中分别有 325 或 199 个系数。代码把实际 flip 的源 820 个值在既定插值主行上取回系数，再检查完整 820 点重建与 Frobenius 不变性，保留值矩阵的哈希。

所有这些分子在源 820 点实际为单位；\(f_0\) 也在这些点为单位。因此，对第二 Abel 族的 54 个源点，本文的所有链上函数均可直接计算 \(f'/f\)，不会因为仅检查常数项而隐藏 Laurent 极点。如果后续在其他点使用这些函数，完整分子仍在证书中，可以按真实参数另作 Laurent 展开。

每个节点保存其精确整数系数 \(k\) 和点坐标哈希，并维护

\[
 D_{\rm node}=kC+\operatorname{div}(f_{\rm node}).             \tag{3}
\]

初始函数是 \(f_b/f_0\)。由 (2)，每条 AddFlip 的准确递推是

\[
 k_R=-k_P-k_Q,\qquad
 f_R=\frac{F/f_0^3}{f_Pf_Q},                               \tag{4}
\]

加倍时把同一个输入出现两次。负点使用二次截面的相同递推。所有函数作为独立小文件原子写入，避免把此前全部函数反复重写进每一位标量 checkpoint。

最终 \(Y=\epsilon mC\) 的真实有效代表满足

\[
 D_Y=\epsilon mC+\operatorname{div}(f_{\rm final}),
 \qquad m=\#J(\mathbf F_{47}),\quad47\nmid m.                \tag{5}
\]

这里的 \(f_{\rm final}^{-1}\) 就是除子 \(\epsilon mC-D_Y\) 的实际主函数。本文保存完整 (4) 的输入、输出、符号、倍加关系和分子，不仅保存已在某组点上求出的值。

## 3. 从实际终点构造第一微小 Abel 族

R241 的全纯对数提取已给出 \(\log(Y)\pmod{47^4}\)。复用 `p41_formal47_exponential.py` 的 `construct_point`，在 R141 第一 Abel 族的 54 个实际源点上反演全纯 Abel 积分，得到

\[
 t=(t_1,\dots,t_{54})\in47R_2^{54},\qquad
 A_1(t)=\sum_j(P_{1,j}(t_j)-P_{1,j}(0)),
\]

其中 \(R_2=(\mathbf Z/47^4)[i]/(i^2+1)\)。参数通过全部 54 个 Abel 方程和 Frobenius 检查；随后由实际移动点条件重新构造完整 73 维 Makdisi 除子理想，而不是只得到抽象正式坐标。

设 R145 第一族的固定截面为 \(v_1\)，满足

\[
 \operatorname{div}(v_1)=Z_1+R_1,
 \quad Z_1=\sum_jP_{1,j}(0),\quad\deg R_1=72.
\]

构造的实际有效除子是 \(E_Q=\sum_jP_{1,j}(t_j)+R_1\)，故

\[
 D_Q=A_1(t)+\operatorname{div}(v_1/f_0).                    \tag{6}
\]

因此 \(v_1/f_0\) 是不能略去的基截面因子。

使用已保存的真实正式负点 flip，取

\[
 F_P\in H^0(2L),\qquad \operatorname{div}(F_P)=E_Y+E_R.
\]

从两个实际理想 \(K_Q,K_R\) 的 199×146 矩阵 \([K_Q,-K_R]\) 得到单位秩 145 的交空间，求出共同二次截面 \(G_Q\)。然后进行比维数更强的检查：在所有 820 个源点、全部 73 列上实际验证

\[
 \frac{G_Q}{F_P}\,H^0(2L-E_Y)=H^0(2L-E_Q),                \tag{7}
\]

并保存两组完整理想之间的秩 73 单位变基矩阵。因为 \(F_P\) 在源 820 点为单位，源值计算没有除以非单位。清分母后，每一列是次数 \(4L=504\) 的截面恒等式；820 个不同评估点多于 504，故检查忠实。模 47 的忠实性逐位提升到模 \(47^4\)。

此外，\(2L-E_Y\) 与 \(2L-E_Q\) 的次数都是 126，大于 \(2g=108\)，完整线性系统无基点。因此 (7) 比较其共同零除子，严格给出

\[
 \operatorname{div}(F_P/G_Q)=E_Y-E_Q.                      \tag{8}
\]

这避免了仅凭交空间维数推断主函数、从而漏掉共支撑重数的风险。第一实际盘无需重新选负点，既有正式负点就通过全部检查。

由 (6)、(8)，真实终点到微小除子的完整运输为

\[
 D_Y=A_1(t)+\operatorname{div}(h_Y),\qquad
 h_Y=\frac{v_1}{f_0}\frac{F_P}{G_Q}.                       \tag{9}
\]

所有分母在第二 Abel 族均实际为单位。分子、分母、归一化点、完整理想变基和全部参数均保存在结果中。

## 4. 微小积分与准确 norm 导数

R240 的已定形式为

\[
 \nu_j=\beta(t)\frac{s_j(W(t))}{v(W(t))^2}\,dt,
 \qquad \beta(t)=-\frac3{4+27(32+t)^2}.
\]

第一族的分母 \(v(W(0))\) 全为单位。程序用已发布的完整源三阶物理 jets，计算这 54 个微分在 54 个第一族点的系数 \(N_0,N_1,N_2\)。常数矩阵 \(N_0\) 还与 R240 已校准的 \(\Omega_1B\Omega_2^T\) **逐项一致**。

对实际反演参数 \(t_i\in47R_2\)，有

\[
 I_j=\int_{A_1(t)}\nu_j
 =\sum_{i=1}^{54}\sum_{n=0}^2
       \frac{t_i^{n+1}}{n+1}(N_n)_{ij}\pmod{47^4}.          \tag{10}
\]

微分系数整且分母为单位，遗漏次数 \(n\ge4\) 的积分项估值至少 \(n-v_{47}(n)\ge4\)，所以没有精度损失。

每个留存的 \(kL\) 截面主函数 \(F/f_0^k\) 的导数在同一真实物理参数中直接求出：

\[
 \partial_{t_j}\log(F/f_0^k)(P_{2,j})
 =\frac{F'}F(P_{2,j})-k\frac{f_0'}{f_0}(P_{2,j}).           \tag{11}
\]

使用 (4) 逐节点相加减，得到 \(L_{\rm final}=d\log f_{\rm final}|_{Z_2}\)。初始值是完整的 \(d\log(f_b/f_0)|_{Z_2}\)，没有设成零。另从 (9) 计算

\[
 L_Y=d\log(v_1/f_0)|_{Z_2}
        +d\log F_P|_{Z_2}-d\log G_Q|_{Z_2}.                \tag{12}
\]

结合 (1)、(5)、(9)，最终实际大积分为

\[
 \boxed{\displaystyle
 \left(\int_C\nu_j\right)_{j=1}^{54}
 =\frac{\epsilon}{m}\left(I+L_Y-L_{\rm final}\right)
 \pmod{47^4}.}                                             \tag{13}
\]

这是准确主函数与微小积分组成的等式；没有把 \(g_C\) 从全局二次高度多项式反推，也没有省去任何初始、终点或 Hecke 纤维规范。

## 5. 首个完整实际结果

`ORD_j05` 的 304 位倍乘和正式提取全部完成。其第一族参数的前两个值为

\[
 (2531749+450354i,\quad2531749+4429327i)\pmod{4879681}.
\]

第二类微小积分的前两个值为

\[
 (198105+609167i,\quad198105+4270514i),
\]

加上 (12) 后，真实 \(D_Y\) 积分的前两个值为

\[
 (3380143+4820840i,\quad3380143+58841i).
\]

通过全部 455 个主函数的导数递推和 (13)，最终 \(C=P_{\rm ORD\_j05}-b\) 的前四个第二类坐标为

\[
 \begin{aligned}
 (&903848+1866769i,\quad903848+3012912i,\\
  &2760301+2625115i,\quad2760301+2254566i).
 \end{aligned}
\]

完整 54 个值保存在证书中。它们在第二族点的 Frobenius 置换下成共轭对；这一基的坐标不应被错误地强制为逐项实数。微小积分、终点 norm 导数、完整链导数和最终值全部实际通过该协变检查。

首个完整结果文件为 `ORD_j05_second_kind_complete47.json.gz`，SHA256：

`9908f39879fa7efdd28b19e4d557060bc5f8e043c0af6a9f7fd0d254d755c6a8`。

实际主函数包 `p41_ORD_j05_principal_transports47.tar.gz` 含 459 个文件：运行规范、单盘完整 manifest 和 457 个真实主函数（454 个倍乘、1 个初始负点、2 个正式提取函数）。包 SHA256：

`9b9d3f03e0071db8452a5243259a8fd60ce9cce388b7f82cde5f88e9e4371f3f`。

## 6. 复现与继续执行

解开主函数包后，使用 `p41_ordinary_second_kind47.py`：

```sh
tar -xzf data/p41_ORD_j05_principal_transports47.tar.gz -C /path/to/work
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python p41_ordinary_second_kind47.py \
  --script-dir . --based-points data/p41_all19_based_points47.json.gz \
  --second-kind data/p41_second_kind_connection47.json.gz \
  --Abel data/ORD_j05_Abel47.json.gz \
  --multiplication data/ORD_j05_multiply47.json.gz \
  --transport-directory /path/to/work/ordinary-principal-transports/ORD_j05 \
  --build-dir /path/to/work/native-build \
  --output /path/to/work/ORD_j05_second_kind_complete47.json.gz
```

完整输入和源代码哈希见 `R248-handoff-manifest.json`。核心脚本 SHA256 为

`a8ddaf871eca4b2278ed18e9cb05397f09dd0683402df30d55c2900de399e071`。

16 个原本缺少全纯常数的普通盘继续按真实群律推进，并在各盘完成后立即用相同代码求出第二类常数。为补齐普通侧的 19 个盘，还对 R237 的三个普通 CM 盘另行执行保留主函数的完整链；这些新链的全纯结果同时与 R237 的精确有符号 Jacobi 类校准独立比对。两项继续工作使用逐盘、逐前缀 checkpoint，不由本条首个封存结果提前宣告完成。

后续仍须把所有实际 de Rham 输入接入指定的局部 QC 截面并求共同根。固定 \(p=41\) 的全部计算即使完成，也仍是主题 README 所列主要一致性问题的中间进展。
