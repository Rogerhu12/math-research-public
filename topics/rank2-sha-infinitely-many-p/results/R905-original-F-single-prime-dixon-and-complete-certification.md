# R905 — 原第一因子的单素数 Dixon 提升与完整特征零返回

日期：2026-11-16。**状态：算法正确性与完整返回已证明；本篇新增公开执行请求，尚无新 PASS。**

R904 的原任务已经证明分母权二不可能，分母权四只取得84个辅助素数、2512位重建模数。本篇对同一个原 $F_{17}$ 权四问题使用单素数提升。仍使用原 Sage 的完整有理 $M_2(867)$ 基，未把旧坐标跨基搬运；不改变原新形式、微分、常数、任何最终系数或其边界。

## 1. 同一个实际矩阵和固定参数

沿 R878 取 $Q=q^6$、$f(q)=qf_0(Q)$、
$$
X^3=U^2-17Q,\qquad
2QU'-U=f_0X^2,\qquad X(0)=1,\quad U(0)=-1.
$$
写
$$
E(Q)=\prod_{n\ge1}(1-Q^n)^{12},\qquad
V=E(Q)U(Q)=-1+5Q+\cdots.
$$
本篇只取分母权 $k=4$：
$$
A\in M_{10}(867),\quad B\in M_4(867),\qquad
d_A=936,\quad d_B=324.
$$
原必要矩阵的所有行是
$$
[Q^j](A-VB),\qquad 0\le j\le1428.
\tag{1}
$$
因此它有1429行、1260列。每个输入块仍由原固定 seed、同一个完整 $M_2$ 对象和全部乘积独立性门形成。低精度、原全部新形式前缀与原 Sage 有序基的构造直接保留 R889 producer，源 blob 为 8ca847cc2fea3bd53cf09af1248bf578263954f6。

本次 request 的参数为
$$
\ell=1000000007,\qquad N=256,\qquad L=\ell^N.
\tag{2}
$$
乘积基证明的辅助素数仍为1000037。这里的$\ell$只用于同一个特征零映射的重建，不是主问题中要证明无穷多个的目标$p$。

## 2. 模素数 chart 及其唯一方阵

程序在$\mathbf F_\ell$重新建立整个(1)，验证原两完整基的秩和全部分母单位。取行阶梯形的列主元集合$J$，秩记为$r$。

若$r=1260$，非零子式直接给特征零必要矩阵满列秩，此时且仅此时可作原权四比值的否定结论。否则取与原 producer 一致的首个非主元列$f$，固定
$$
z_f=1,\qquad z_j=0\quad(j\notin J\cup\{f\}).
\tag{3}
$$
再对主元列矩阵的转置取主元，得到$r$个行$I$。令
$$
B_0=M_\ell[I,J],\qquad b_0=-M_\ell[I,f].
$$
$B_0$可逆。只求一次$B_0^{-1}$，并重代完整$M_\ell z=0$，检查实际$A,B$同阶、非零及相反首项。保存的是这一个原 chart 的行列、首自由坐标、$B$首阶和完整原 germ；打印时只给 hash 和少量元数据。

这里没有从旧 run 的秩1116断言新执行已测得同一个秩，也没有把某个不成功的 chart 解释为整个矩阵无核。

## 3. 在真实素数幂环上重建原 germ

令$R_N=\mathbf Z/L\mathbf Z$。所有输入有理数先按分母单位准确约化。固定素数本身满足
$$
\ell>6\cdot1428+1.
\tag{4}
$$
R889 的原 $F$ Newton 方程只除以常数2、3、正整数$j$、$6j+1$及常数项为单位的形式级数。到本篇完整窗口，这些都是$R_N$中的单位。因此 R889 的逐次倍增证明原样在$R_N$成立；不要求该有限环为域，也不能只检查$\ell^N$大于窗口而忘掉(4)。

程序保留每一步两条原定义残差，得到原$U$及$V=EU$的全部1429项，并逐项核其模$\ell$约化就是§2保存的全部 germ。

高精度只建立
$$
B_N=M_L[I,J],\qquad b_N=-M_L[I,f],
\tag{5}
$$
不是整个1429×1260高精度矩阵。$A$列直接读取原权十基系数；$B$列准确乘同一个$-V$后读取$I$。$B_N$模$\ell$就是$B_0$，所以它在$R_N$可逆。

## 4. 逐位整除支付 Dixon 解

在整数代表中设$e_0=b_N$、$z_0=0$。第$j$步取
$$
d_j=B_0^{-1}(e_j\bmod\ell)\in\mathbf F_\ell^r,\qquad
\widetilde d_j\in\{0,\ldots,\ell-1\}^r,
$$
并令
$$
z_{j+1}=z_j+\ell^j\widetilde d_j,\qquad
e_{j+1}=(e_j-B_N\widetilde d_j)/\ell.
\tag{6}
$$
模$\ell$下分子为零，因此每次是整数中的真整除。归纳保持
$$
e_j=(b_N-B_Nz_j)/\ell^j.
\tag{7}
$$
取$j=N$即得$B_Nz_N=b_N\bmod L$。由(5)的可逆性，这是(3)在所选行上的唯一模$L$解。程序逐步断言整除，每16个数字报告阶段时钟；没有在不同素数上反复作全部行消元。

同 R899，这条证明不需要坐标高度上界。它只给固定 chart 的准确模$L$解，并不保证固定 chart 在更高精度仍满足全部未选行。

## 5. 原全部未选行仍必须复核

恢复整个1260维向量，释放高精度方阵后，程序用实际原两组模形式形成$A,B$，准确检查
$$
A-VB=0\bmod(L,Q^{1429}).
\tag{8}
$$
(8)含所有1429行，不只$I$或 cusp 首项。若失败，记录第一非零行及其$\ell$赋值、全残差和坐标的hash，状态为“固定 chart 未认证”。其它 chart 或更高精度的可能性仍在。

若(8)通过，才对全部坐标尝试有理重建；本篇没有假设这些坐标落在本次$N$所容许的高度内。因此失败也只记精度不足。重建成功后仍检查(3)的全部自由坐标，随后进入原短精确检查与原最终证书。

## 6. 原最终证书逐字保留

以下函数直接保留 R889 原代码：

- 同一完整乘积基的低/高精度展开及前缀比较；
- 原短精确分支检查 initial_exact_check；
- 原完整 strict_original_certificate；
- 原 eta12_unit 与 e2_series。

它们在特征零实际形成
$$
\Delta=QE^2,\qquad \mathcal H=Qf_0^3E,
$$
$$
C=(D_QA)B-A(D_QB)-\tfrac12E_2AB,
\tag{9}
$$
并检查
$$
\boxed{8\Delta C^3=\mathcal H B^2(A^2-17\Delta B^2)^2}
\tag{10}
$$
从$Q^0$一直到$Q^{6120}$，包含末端。两边权为60，故原$X_0(867)$的 Sturm 界正是6120。实际高精度基必须重现全部已用低前缀，且保$A,B$同阶、相反首项及$V(0)=-1,[Q]V=5$。

R878 的完整证明随后给原$X_0(10404)$上的真实坐标
$$
y=\frac{A}{eB},\qquad
x=\frac{f(q)(A^2-17\Delta B^2)}{2eC},
$$
以及原
$$
x=q^{-2}+O(q^4),\qquad y=-q^{-3}+O(q^3),\qquad
\frac{dx}{2y}=f(q)\frac{dq}{q}.
$$
没有假设 Manin 常数或借另一个映射归一。只有(10)及全部原门通过时，才设置同进程 CERTIFIED_FIRST_FACTOR_SOLUTION/WEIGHT。消费者必须使用本 producer 的实际基、recipes和这些认证坐标，不能把模$\ell^N$候选直接当作原 map。

## 7. 可执行文件、资源与状态

新增文件：

- scripts/original_f_padic_dixon_map.py；
- scripts/produce-r905-original-first-factor-map-dixon.py；
- ci/original-F-dixon-request.json；
- 仓库 workflow .github/workflows/rank2-sha-original-F-dixon.yml。

整数有理系数约化器复用已提交 original_padic_dixon_map.py；本次不修改它，也不改动正在执行的原 P 请求。公开 workflow 按 request 的实际 arguments 运行本 producer，固定原 Sage10.6镜像，数学容器无网络、源码只读、不保存输出文件。具名容器、timeout kill-after 与退出清理确保有限预算真的终止数学进程。

本次旧 F 的完整基约614秒已成，故保留这套实际基并直接处理原重建循环。一个$r$阶矩阵的模$\ell$逆只作一次，其后为$N$次整数矩阵向量乘法；高精度只存一个$r\times r$方阵。原 Newton germ、方阵构造、完整复乘和特征零证书仍有真实成本，不能仅由这个复杂度说明宣称实测更快。

全部数学执行仍仅在公开 Actions。这里没有本地数学运行，没有新 PASS、原 shadow 或主目标完成声明。run/job/source 与实际输出 hash 在执行完成后按真实日志补记；不将可重算坐标或矩阵入库。
