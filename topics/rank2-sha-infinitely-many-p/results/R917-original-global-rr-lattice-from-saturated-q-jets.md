# R917 — 原全局 RR 格的有限 q-jet 饱和与完整模 p 基

日期：2026-11-16。**状态：下列原整格等式、严格终止的饱和算法和完整有限域 RR 基构造已证明。尚未取得新算法的公开运行回执；原函数域坐标、闭点求值和 shadow 消费仍须完成。**

本篇直接使用 R892 已固定的完整有理模形式空间。有限 q 串仅作这个已知全局空间的忠实坐标；通过整格饱和后，它给出 R882 同一个全局 RR 空间的全部约化截面。不能把一组未经全局构造器认证的形式串代入下文。

## 1. 同一个好模型、全尖点与原分母

固定原底曲线
$$
B=X_0(867),\qquad 867=3\cdot17^2,
$$
并取原消费特征 $\ell=29$ 或 $41$。在 $\mathbf Z_\ell$ 上使用 R882 的光滑、几何连通、proper 好模型 $\mathcal B$；全部 cusp 组成相对约化有限 étale 除子 $\mathcal C$。原无穷 cusp 为一条有理截面，完成参数仍是同一个 $Q$。

本级没有椭圆固定点：17 在 $\mathbf Q(\sqrt{-3})$ 惰性、3 在 $\mathbf Q(i)$ 惰性，分别排除保 cyclic level 的额外三阶、二阶稳定子。原指标、全 cusp 数及亏格为
$$
[\mathrm{SL}_2(\mathbf Z):\Gamma_0(867)]=1224,\quad
\deg\mathcal C=1+1+16+16+1+1=36,\quad g=85.
\tag{1}
$$
权二线束准确为
$$
\mathcal L=\Omega^1_{\mathcal B/\mathbf Z_\ell}(\mathcal C),
\qquad \deg\mathcal L=2g-2+36=204.
\tag{2}
$$
在无穷 cusp 用 $dQ/Q$ 平凡化，模形式的通常 q 系数就是该线束截面的局部系数。没有删除另外35个几何 cusp。

保 R882 的原完整分母
$$
S(Q)=\frac{3E_2(Q^3)-E_2(Q)}2=-D_Q\log T_3(Q),\qquad S(0)=1.
\tag{3}
$$
它的系数在 $\mathbf Z_\ell$ 中。因常数一，其约化非零，且在原无穷 cusp 不为零。原除子正是
$$
D_S=\operatorname{div}(dT/T)+\mathcal C_{\mathbf F_\ell}
=\operatorname{div}_{\mathcal L_{\mathbf F_\ell}}(\bar S).
\tag{4}
$$
因此它有效、次数204、无穷系数0，与 R882(18)完全相同；不是一个只在仿射开集定义的替代极帽。

## 2. 有限 jet 同时忠实且整饱和

对 $m\ge1$ 置
$$
r_m=204m-84,\quad B_m=204m+1,\quad
\mathscr M_m=H^0(\mathcal B,\mathcal L^m).
$$
每个几何纤维上 $\deg\mathcal L^m=204m>168=2g-2$，所以由 Serre 对偶和负次数线束无截面，
$H^1(\mathcal L^m)=0$。proper cohomology 与 base change 遂给
$$
\mathscr M_m\text{ 为自由 }\mathbf Z_\ell\text{ 模，秩 }r_m,\qquad
\mathscr M_m/\ell\mathscr M_m
=H^0(B_{\mathbf F_\ell},\mathcal L_{\mathbf F_\ell}^m).
\tag{5}
$$
其泛纤维是原 $M_{2m}(\Gamma_0(867),\mathbf Q_\ell)$。

读取从 $Q^0$ 到 $Q^{204m}$ 的全部系数，记
$$
J_m:\mathscr M_m\longrightarrow\mathbf Z_\ell^{B_m}.
\tag{6}
$$
该映射及其模 $\ell$ 约化均单射。理由相同：若所有这些系数为零，一个非零全局截面在有理 cusp 的零阶至少为 $204m+1$，严格大于它整个零除子的次数 $204m$，矛盾。

这还给出完整整格身份：
$$
\boxed{
J_m(\mathscr M_m)
=
J_m(\mathscr M_m\otimes\mathbf Q_\ell)
\cap\mathbf Z_\ell^{B_m}.}
\tag{7}
$$
证明可直接作赋值下降。右侧向量对应唯一泛纤维截面 $f$。若 $f$ 不整，取最小 $a>0$ 使 $\ell^af\in\mathscr M_m$ 且其约化非零；但它的全部 $B_m$ 个 jet 被 $\ell$ 整除，违背刚证明的模 $\ell$ 单射。故 $a=0$。

(7)意味着这些有限 jet 的像没有任何遗漏的 $\ell$ 饱和方向。它不仅给“至多 $r_m$ 维”，而且精确识别全部可约化模形式。特别不能先任意约化一组带 $\ell$ 分母的有理基，或以其约化秩缺陷推断 RR 维数下降。

## 3. 任意已认证有理基的准确返回

设 $f_1,\ldots,f_{r_m}$ 是 R892 构造器给出的完整 $\mathbf Q$ 基；高权时，必须已经由完整 Sturm 行与实际秩认证所选乘积基。令
$$
M=(J_mf_i)_i\in M_{r_m,B_m}(\mathbf Q).
\tag{8}
$$
本篇所有行变换只改变这一已知空间的基，不改变原 moduli、端点或 Fourier 参数。

记 $\mathbf Z_{(\ell)}$ 为有理数中分母素于 $\ell$ 的局部环。则
$$
\boxed{
\bigl(\operatorname{row}_{\mathbf Q}M
\cap\mathbf Z_{(\ell)}^{B_m}\bigr)\otimes_{\mathbf Z_{(\ell)}}\mathbf Z_\ell
=J_m(\mathscr M_m).}
\tag{9}
$$
这也可从任一清分母整数矩阵的 Smith 正规形立即证明：饱和之后各非零对角指数成为单位，完成与取该交相容。结合(7)便是同一个全局格，不依赖有理基的选择。

因此，只须精确求(9)左侧的局部饱和格。所得任意基 $\widehat M$ 都是实际全局整形式的 jet；约化后是(5)的完整基，秩恰为 $r_m$。若同时记录实际有理变换
$$
\widehat M=A M,\qquad A\in\mathrm{GL}_{r_m}(\mathbf Q),
\tag{10}
$$
每个输出基元的全局身份就是 $\sum_jA_{ij}f_j$。这里不存在从有限系数猜一个未知模形式的步骤。

## 4. 只在所需素数饱和的严格终止算法

下述算法不必计算其它素数的整格。

先逐行乘 $\ell$ 的整数幂，使(8)每行均在 $\mathbf Z_{(\ell)}^{B_m}$ 且至少有一个单位。记此时矩阵为 $M_0$，并同步记录(10)的初始对角变换。选固定的 $r_m$ 个列 $I$，使
$$
\det(M_0[:,I])\ne0,\qquad
v_0=v_\ell\det(M_0[:,I])\ge0.
\tag{11}
$$
以后的矩阵均保这同一组列；不在失败后换一个新的来源。

若当前 $\bar M$ 在 $\mathbf F_\ell$ 上满行秩，停止。否则取其完整左核的一组基，维数为 $d>0$；把这些行补成 $\mathbf F_\ell^{r_m}$ 的一组基。逐项用整数代表提升，得到
$$
U\in M_{r_m}(\mathbf Z_{(\ell)}),\qquad
\det U\in\mathbf Z_{(\ell)}^\times,
$$
其中最后 $d$ 行模 $\ell$ 是这份左核。令
$$
M'=
\operatorname{diag}(1,\ldots,1,
\underbrace{\ell^{-1},\ldots,\ell^{-1}}_d)\,U M.
\tag{12}
$$
最后 $d$ 行的分子全部被 $\ell$ 整除，所以 $M'$ 仍整。它的行格包含旧格，指数准确为 $\ell^d$；相应全局截面身份沿同一个变换保存。原固定子式满足
$$
v_\ell\det(M'[:,I])
=v_\ell\det(M[:,I])-d.
\tag{13}
$$
右边始终非负，因此算法至多经过 $v_0$ 次非平凡迭代就停止，实际下降量总和至多 $v_0$。无需猜测模形式系数的高度或预设某个饱和次数。

停止时，约化满行秩使行格在 $\mathbf Z_{(\ell)}^{B_m}$ 中饱和。它与初始矩阵有同一个有理行空间，故恰是(9)的格。每一步都要检查分母为 $\ell$ 单位、真实左核、$U$ 的单位行列式和(13)；最终检查(10)的全矩阵等式及模 $\ell$ 全行秩。固定子式的整数赋值仅是严格终止证书，不是新的数学启发式阈值。

## 5. 原完整 RR 基与后续精度

令 $\bar f_i$ 是(10)确定的全局整形式约化。则
$$
\boxed{\bar f_1/\bar S^m,\ldots,\bar f_{r_m}/\bar S^m
\text{ 是 }L_{B_{\mathbf F_\ell}}(mD_S)\text{ 的完整基}.}
\tag{14}
$$
证明就是(4)–(5)的线束平凡化，保所有有限点和全部 cusp。乘以 $\bar S^{-m}$ 在原有限 jet 环可逆，所以前 $B_m$ 项仍满秩 $r_m$。扩常数到 $\mathbf F_{\ell^2}$ 也保持完整性。

特别 $m=1$ 得原完整120维空间和205项忠实坐标。这里的全局完整性由(7)–(10)证明，强于 R881 中单靠有限原 germ 的形式数据；但它尚未把这些基元写入现有 degree48 函数域。

若需要更长 q 精度，须从同一个 R892 空间重新调用全局形式的 q-expansion，再施同一(10)，并逐项保旧前缀。不能由已存 $B_m$ 个有限 jet 任意延长。恒等式(7)同时保证这个扩展的全部新系数仍在 $\mathbf Z_{(\ell)}$；若实现出现非单位分母，必须失败并检查来源。

对任意两个已构造权 $2a,2b$，按这个规则读到 $B_{a+b}$，实际乘积必是全局 $M_{2(a+b)}$ 截面。用完整基解全部 $B_{a+b}$ 行，给唯一且精确的乘法表；除以原 $S^{a+b}$ 后即是同一 RR 函数乘法。这里只读取已知全局乘积，不用有限串的偶然匹配宣称模性。

## 6. 与当前原 shadow 前端的边界

本条完整解决的是原全局 RR 空间的整格、完整约化和忠实有限坐标。它不要求先正规化 degree24/48 方程，因此可以独立构造全局 q-jet 基。

现有 R882/R910 消费器还要求同一函数域中的基元素、原 $T,U,V$、两个 Atkin 符号、完整36 cusp 和全部闭点赋值。若将(14)接入该接口，仍须付实际函数域变换或另一个完整的全局函数运算模型。未完成这一步，不将新 q 格回执冒称为现有全部四 RR 块、原点除子或 shadow 已 PASS。

原 F 已有 R909 完整特征零证书；原 P、后续闭点除子与非零影子仍按 HANDOFF 的实际状态推进。本条没有把形式群的特征 $\ell$ 微分唯一性当作原映射存在性。

## 7. 实现与依据

公开 producer `scripts/produce-r917-original-global-rr-q-lattice.py` 只消费 R892 的同一完整 PARI 构造器，记录实际全部矩阵检查的结果及 SHA-256，不写系数输出文件。参数为 `--prime 29 --q-precision 205`，请求及独立 workflow 已提交。数学执行仍仅在本公开仓库 Actions；尚无本条新运行结果。

- [R882 §6、附录B](R882-original-degree18-source-model-and-two-endpoint-coordinates.md)：原好模型、全部 cusp、$D_S$ 与同 $S$ 的真实 RR 身份。
- [R892](R892-original-two-map-pari-rational-basis-and-unchanged-certification.md)：完整有理空间、实际乘积基认证与同一对象的扩精度规则。
- The Stacks Project, [Degrees on curves, §33.44](https://stacks.math.columbia.edu/tag/0AYQ)：截面、零除子与次数；本篇的有限 jet 饱和及终止论证已逐步给出。
- SageMath 官方 [矩阵接口](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix2.html)：实现中使用的左核和基矩阵约定。执行仍固定原 Sage 10.6 镜像，软件接口不替代(7)或(13)的证明。
