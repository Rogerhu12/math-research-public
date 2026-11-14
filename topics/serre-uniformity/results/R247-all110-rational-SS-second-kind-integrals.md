# R247：全部 110 个有理超奇异圆盘的实际第二类大积分

日期：2026-11-13。状态：**已证明并全部实算，精度模 $47^3$。**

对 R228 的全部 110 个真正 $\mathbf Q_{47}$ 超奇异中心 $P$，本条求出 R240 原规范的完整行向量
$$
g_C=\left(\int_{P-b}\nu_j\right)_{j=1}^{54},\qquad b=P_{-3}.
$$
计算使用 R246 的实际移极点表示、R234 的完整真实 Hecke 图、R222 的实际 $B=Z_{-4}-D_{\rm cusp}$ 纤维梯度，以及本条实际求出的 270 个可去极点有限部和全部尖点迹。没有把第二类积分从全局二次高度反推，也没有把有理点的结论扩写成非有理顶点的全部复数积分。本条仍未完成局部 QC 截面及共同根。

## 1. 保留原中心和真实 Frobenius 偏移

令 $P_i$ 为 R234 已保存的 3154 个几何中心，$\tau(i)$ 是其模 47 的 Frobenius 顶点置换。一般只有
$$
\operatorname{red}(\sigma P_i)=\operatorname{red}(P_{\tau(i)}),
$$
而没有 $\sigma P_i=P_{\tau(i)}$。因此不能直接令积分数组在这个置换下固定。

R246 已给真正有理的微分行基
$$
\boldsymbol\mu=(\boldsymbol\nu+d\boldsymbol F)C,\qquad
T_3\boldsymbol\mu=\boldsymbol\mu H+d\widetilde{\boldsymbol f},
\qquad H=C^{-1}M_3^tC.                                  \tag{247.1}
$$
这里 $H$ 的 54×54 全部系数在 $\mathbf Z/47^4$ 中，
$$
\widetilde{\boldsymbol f}
=\boldsymbol fC+T_3(\boldsymbol FC)-(\boldsymbol FC)H.    \tag{247.2}
$$

每个 $\mu_j=N_jw^{-2}\omega_L$ 的分母在全部 3154 个剩余圆盘为单位。本条用这个共同 $w$ 作射影框架，在单位坐标下实际生成全部中心 0 至 3 次的 73 坐标、0 至 2 次的 54 微分和 1 至 3 次的微小原函数；共 51 个完整坐标文件，全部保存。

对任一落在第 $j$ 个圆盘的真实点 $Q$，直接计算其射影参数 $z$，实际检查 $z\in47R_2$，并把局部展开回代到全部 73 个坐标，逐项核对原输入点。微小积分使用
$$
\int_{P_j}^{Q}\boldsymbol\mu
=\sum_{k=1}^{3}\frac{\boldsymbol\mu_{k-1}}{k}z^k
\pmod{47^4}.                                           \tag{247.3}
$$
全部系数整；对 $k\ge4$，$k-v_{47}(k)\ge4$，所以遗漏项不影响该精度。没有在正估值的参数上作数值除法。

## 2. 完整实际 Hecke 右端

置
$$
U_i=20P_i-D_{\rm cusp},\qquad N_i=\int_{U_i}\boldsymbol\mu.
$$
对 $T_3P_i$ 的四个实际三同源目标 $Q_{i,k}$，记其剩余顶点为 $j(i,k)$，并令
$$
\delta_{i,k}=\int_{P_{j(i,k)}}^{Q_{i,k}}\boldsymbol\mu.
$$
四条目标都由 R234 已核的真实 Vélu 核、原水平输运和对应物理/椭圆粗参数求值。它们保留原行列式 3，没有重新把其中一个挠点基向量除以 3。本条全部 $3154\cdot4=12616$ 个目标各通过完整 73 坐标回代。

因 $T_3D_{\rm cusp}=4D_{\rm cusp}$，从 (247.1) 得准确方程
$$
\boxed{
A_3N-NH=R,\qquad
R_i=20\widetilde{\boldsymbol f}(P_i)
-\widetilde{\boldsymbol f}(D_{\rm cusp})
-20\sum_{k=1}^{4}\delta_{i,k}.}                          \tag{247.4}
$$
尖点项和全部恰当微分项都保留。$A_3$ 是 R234 的真实有向邻接矩阵，含椭圆粗点应有的重数。

## 3. 270 个旧极点处的实际有限部

R246 使 $\boldsymbol F$ 的分母在超奇异圆盘中仅于 $Z_2$ 的 54 个点简单为零，使 $\boldsymbol f$ 的分母仅于 $S=Z_2\cup T_3Z_2$ 的 270 个互异点简单为零。这个集合没有有理剩余点。在其余 2884 个点，(247.2) 的全部分母是单位，可直接求值。

在 $Z_2$ 上，须一起处理 $\boldsymbol fC-(\boldsymbol FC)H$；在 $T_3Z_2$ 上，须一起处理 $\boldsymbol fC$ 与唯一一条落入 $Z_2$ 的目标 $\boldsymbol FC(Q_{i,k})$。其余项是单位分母值。脚本实际核对每个点恰属上述一种情况，不假定哪条分支含极点。

对这两项先交叉乘分母再相加。所得共同分母模 47 的零阶为 2，其二次系数为单位。源点使用原物理参数：$j=0$ 时变 $A$，其他源点变 $B$。目标使用同一个三次核的真实变形：从 $\psi_3(x,A(t),B(t))=0$ 单位 Newton 提升到八阶，以
$$
u(t)=2x(t),\qquad
\beta_T(t)=\beta(t)/3,\qquad
a_T(t)=a(t)+u(t)\beta(t)/3
$$
生成真实目标 Serre jets。目标常数先乘原同构的平方尺度，使其属于实际 Vélu 微分框架；不把只给射影点的任意尺度直接代入微分方程。

写合并分子、分母为 $n(t),d(t)$。利用系数 $t^2,\ldots,t^7$ 的六个方程，实际解六阶单位线性系统
$$
\sum_{k=0}^{5}d_{2+j-k}q_k=n_{2+j},\qquad0\le j<6.       \tag{247.5}
$$
矩阵模 47 下三角且对角为单位 $d_2$。还逐点检查遗漏的 $t^0,t^1$ 两式模 $47^3$ 成立。由整除后的函数在整个圆盘正则，以及 $d_0,d_1\in47R_2$，未保留的 $q_k$ 对 $q_0$ 的影响至少含 $47^{\lceil6/2\rceil}$，故 (247.5) 给正确三位常数。

整性在这里也有几何保证：$\widetilde{\boldsymbol f}$ 的可能极点只能来自 R246 移到外面的 $D_w$ 与 $T_3D_w$；Hecke 保持超奇异剩余类，故这些支撑都避开当前圆盘。原全局表示没有竖直分母。不能仅由形式导数正则而任意假定常数整。

270 个完整分子/分母的截断系数、六阶解和两个低阶等式均保存在 all270_actual_second_kind_finite_parts47.json.gz。这不是把无穷值置零或在已经丢失精度的商上补一个猜测常数。

## 4. 完整尖点迹与真实 B 锚

尖点计算使用原次数 80 未分歧域和原 20 个真实尖点。Frobenius 平方有两个长度 10 的轨道，选原编号 1、12 的代表。R246 的 $v,w$ 在这两个完整域为单位；新 Hecke 分母 $b$ 的单位性也在本条实际检查。

对每个代表，先在完整域中评价所有分子并作真实域逆，然后取从次数 80 域到 $R_2$ 的迹除以 4。若 $x$ 是一个这样的域值，用原固定的 $i$ 可以写为
$$
\frac14\operatorname{Tr}_{80/2}(x)
=\frac18\operatorname{Tr}_{80/1}(x)
-\frac{i}{8}\operatorname{Tr}_{80/1}(ix).                \tag{247.6}
$$
两个轨道相加便是全部 20 尖点，不额外乘以 2 或 20。原域迹基由原多项式的 Newton 恒等式精确计算；每个域逆通过完整 80×80 乘法矩阵验证。最终 $\boldsymbol FC(D_{\rm cusp})$ 和 $\boldsymbol fC(D_{\rm cusp})$ 的虚部都为零。

因此 (247.2) 的完整尖点值为
$$
\widetilde{\boldsymbol f}(D_{\rm cusp})
=\boldsymbol fC(D_{\rm cusp})
+4\boldsymbol FC(D_{\rm cusp})
-\boldsymbol FC(D_{\rm cusp})H.                         \tag{247.7}
$$

R222 已完成的真实纤维 Lie 梯度 $g_B^{\rm Lie}$ 给原规范的
$$
g_B^\nu=(\Omega_2g_B^{\rm Lie})^t.
$$
这里 $\Omega_2$ 正是 R240 保存的杯积矩阵的负值。移极点后
$$
g_B^\mu=g_B^\nu C
+\boldsymbol FC(Z_{-4})-\boldsymbol FC(D_{\rm cusp}).    \tag{247.8}
$$
二十个实际 $Z_{-4}$ 点均包含在图中。直接单位评价给 (247.8)，其虚部为零。因 $|Z_{-4}|=20$，
$$
\boxed{\sum_{i\in Z_{-4}}N_i=20g_B^\mu.}                \tag{247.9}
$$
这是从既有实际 Miller/Poincaré 计算得到的锚，不是假定 $B$ 为零，也没有借用尚未求出的超奇异第二类积分。

## 5. 用真实偏移取 Frobenius 偶部分

因为 $C,\boldsymbol\mu$ 都定义于 $\mathbf Q_{47}$，真实共轭关系是
$$
\overline{N_i}
=N_{\tau(i)}+20\int_{P_{\tau(i)}}^{\sigma P_i}\boldsymbol\mu.
                                                               \tag{247.10}
$$
在原 73 坐标中，$\sigma P_i$ 的一组实际坐标是 $\overline{W_i}\,\overline{A_1}$。脚本直接将此点送入第 $\tau(i)$ 个局部图，同样完整检查 73 坐标，取得 (247.10) 的微小项。

令
$$
a_i=10\operatorname{Re}\int_{P_{\tau(i)}}^{\sigma P_i}\boldsymbol\mu,
\qquad X_i=\operatorname{Re}N_i-a_i.
$$
实际检查 $a_{\tau(i)}=-a_i$，从而 $X_{\tau(i)}=X_i$。其方程为
$$
\boxed{
A_3X-XH=Y,\qquad Y=\operatorname{Re}R-(A_3a-aH).}        \tag{247.11}
$$
全部 $3154\times54$ 个系数实际满足 $Y_{\tau(i)}=Y_i$。对 $B$ 的完整 20 点求和，$a$ 的贡献相消；锚仍是 (247.9)。

这里只求实部是充分而准确的：目标中心都是 $\mathbf Q_{47}$ 点，微分 $\mu_j$ 有理，故它们的最终积分就是实数。对非有理顶点，本条不声称已确定另一个 Frobenius 奇核中的虚部。

## 6. 1632 个轨道上的单位求解

3154 个几何顶点中有 110 个不动点，故 Frobenius 轨道数为 $(3154+110)/2=1632$。把 (247.11) 压到这些轨道上，邻接仍保留全部四条分支及重数。设 $P(T)=\det(T-H)\bmod47$，次数为 54。实际得到
$$
\operatorname{rank}_{\mathbf F_{47}}P(A_3^+)=1631.
$$
具体非零核向量 $v$ 满足 $v_0=1$、$A_3^+v=33v$。把 $P(A_3^+)$ 第 0 行换成第 0 个坐标行后，实际求出 1632×1632 逆矩阵并检查完整乘积为单位阵。逆分五个压缩行块保存。这同时证明原矩阵的秩恰为 1631，而不是根据数值近似判断秩。

把二十个 $Z_{-4}$ 点压到轨道后，记其重数行为 $b$。实际
$$
bv=10\ne0\pmod{47}.                                    \tag{247.12}
$$

每一位精度的求解均如下。对 $A_3^+X-XH=Y$ 的 Horner 差商恒等式给 $P(A_3^+)X=D(Y)$。先把 $D(Y)$ 第 0 行置零，由上述逆求一个解 $X_0$；再按锚 $bX=t$ 加上准确核修正
$$
X=X_0+v\,\frac{t-bX_0}{10}.                             \tag{247.13}
$$
脚本对每一位都在原 Sylvester 方程及完整 54 列锚中重验；连续解三位，没有除以 47 的不确定数值逆。最后也在未压缩的 3154 点上验证原 (247.4) 的实部及 (247.10) 的实部。

原全图 $P(A_3)$ 的另一个核方向是 Frobenius 奇向量，在全部 110 个不动点为零。它不影响本条目标；没有通过任意设值伪称其对应的全部非有理积分已经求出。

## 7. 回到真正有理中心和原 ν 基

R228 每个有理中心的 73 坐标已在 (247.3) 中完整回代，得到从相应旧图中心到它的真实微小积分。于是
$$
U_P^\mu=\operatorname{Re}N_i
+20\operatorname{Re}\int_{P_i}^{P}\boldsymbol\mu.
$$
先减去真正 CM3 基点的 $U_b^\mu$，再只逆一个单位 20：
$$
g_{P-b}^\mu=(U_P^\mu-U_b^\mu)/20.
$$
最后逐点实际评价 $\boldsymbol FC(P)$；全部 110 个值确实有理、分母均为单位。由 (247.1) 返回原规范：
$$
\boxed{
g_{P-b}^\nu
=\bigl(g_{P-b}^\mu-\boldsymbol FC(P)+\boldsymbol FC(b)\bigr)C^{-1}
\pmod{47^3}.}                                          \tag{247.14}
$$
原 $\nu$ 基的数值按其极点 Frobenius 置换成共轭对，不应强制逐项虚部为零。基点的完整 54 项为零。

主输出为 p41_rational_SS_second_kind_integrals47_complete.json.gz，SHA-256：

c8b5e8d292b89dadf5cfa5f1b7bafadff6848cda61ddfe207c5009f2ed6a401d。

完整实际右端为 p41_SS_second_kind_rhs47.json.gz，SHA-256：

55ddc99c63f36d3c0789bc00e5d6c8cd5d7f1f6164bf0e1397eaef2858887d86。

## 8. 复现和精度边界

全部源码、51 个正则微小图、270 个有限部、原核记录、五块逆、完整右端和 110 个原基结果均由本条 manifest 绑定。在 scripts/ 下：

~~~sh
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python p41_SS_second_kind_rhs47.py \
  --script-dir . --moved data/p41_second_kind_move_poles47.json.gz \
  --work-dir /path/to/rhs-work --output /path/to/p41_SS_second_kind_rhs47.json.gz
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python p41_SS_second_kind_solve47.py \
  --graph data/p41_SS_Hecke_graph47.json.gz \
  --rhs /path/to/p41_SS_second_kind_rhs47.json.gz \
  --kernel data/SS_second_kind_even/T3_kernel_and_B_anchor.json \
  --cache-dir /path/to/even-inverse \
  --output /path/to/p41_rational_SS_second_kind_integrals47_complete.json.gz
~~~

第二个命令使用 python-flint；既有逆缓存可直接复用并核 SHA。环境路径和耗时字段可能改变重新压缩后的文件哈希，但完整系数以及固定输入哈希应一致。

本条只报告三位大积分：实际 $B$ 梯度锚的已存精度为三位，270 个有限部也按三位求值；不把局部图和点坐标的四位精度移植成大积分四位。后续须将这些真实输入与 R248/R253 的主函数、非形式纤维和规范 QC 截面连接，再处理全部共同根与尾项。层 41 的完成仍不等于主题 README 的绝对一致性目标。
