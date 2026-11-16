# R906 — 同原 P 的小素数精确矩阵与已验精度续接

日期：2026-11-16。**状态：以下同来源算法、续接恒等式和认证保持已证明；新的公开执行尚未完成，不声称取得映射或测得速度提升。**

本篇接 R899 的实际运行。原首轮 run43895102858/job133396398465 在三个嵌入上都通过模 $1000000033^{128}$ 的全部1226行，但3827位模数未能恢复全部有理坐标。其完整结果 SHA-256 为
5d68fc8b6af26528e0cdf56f8cc071812a44bbb91ea99f59c8b27b6d1cc578ac。
同素数256位续轮 run43901392214 继续运行；本篇不取消或改变它。

## 1. 真实计时与已定位的实现分支

首轮的完整 PARI 乘积基到约34.80秒已经完成；三份底域矩阵的消元、选行与逆完成时约1248.78秒；三份高精度全窗及三根恢复到约1466.28秒。
因此本篇针对已观测的底域线性代数，而非再次猜测模形式基未完成。

已亲读 SageMath **10.6 tag** 的源码：

- [matrix_space.py](https://github.com/sagemath/sage/blob/10.6/src/sage/matrix/matrix_space.py)，git blob 647efed20ca8df5f6d35b909dcdbbf0e1ba91690，函数 get_matrix_class；
- [matrix_modn_dense_double.pyx](https://github.com/sagemath/sage/blob/10.6/src/sage/matrix/matrix_modn_dense_double.pyx)，常数 MAX_MODULUS=94906266；
- [官方矩阵文档](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_modn_dense_double.html)的相应精确有限环矩阵类型。

在该固定版本中，显式 linbox-double 只接受模数小于94906266；默认选择在超过这两个 LinBox 类型的上限后落到通用矩阵类型。R899 的素数1000000033超过这个范围。这是按已读源码作出的实现分支判断；首轮日志没有打印实际矩阵类型，不能伪称日志已测得该类型。

LinBox 的 double 是精确模运算内部的元素表示，不把原有限域问题换成实数近似或容差秩。本篇显式指定该类型，并在公开执行中输出及核定实际类名；如果它不可用，本轮不能以其它近似输出继续认证。

## 2. 只有辅助重建素数发生改变

原固定数据、完整空间、实际基和证书全部保持：

$$
F=\mathbf Q(a),\quad a^3=17,\quad
u=(915,1097,2962)/55569,
$$

$$
\lambda=(68+7a-13a^2)/3,\qquad
v_{\rm new}=\lambda^3v,\qquad
H_u/\lambda=qf(Q),\quad Q=q^3.
$$

仍取原完整 $M_6(\Gamma_0(867),\mathbf Q)$ 的528个确定乘积基；
它由同一个固定 PARI 完整 $M_2$ 基、同一 seed、同一原 product-basis prime 和同一全秩选择规则生成。
原矩阵仍是

$$
\mathcal M x=([Q^j](QA-yB))_{j=0}^{1225},
\qquad y=QY_{\rm new},\quad y(0)=-1,
\tag{1}
$$

共1226行、1056列。原 $u$、目标尺度、三个嵌入和微分没有变化。

新 request 给有限搜索区间 $[10^6,1001000]$。程序**仅在公开 Actions 中**按素数递增顺序，选择首个满足以下全部条件的辅助素数 $\ell$：

1. $\ell>6(1226)+1$ 且 $\ell<94906266$；
2. $X^3-17$ 在 $\mathbf F_\ell$ 有三个互异根；
3. 原全部输入有理分母在 $\ell$ 为单位；
4. 同一个完整有理乘积基的全 Sturm 前缀在 $\ell$ 仍为528秩。

每个被跳过素数的原因与最终三个根均由日志给出。有限区间没有合格素数时只记搜索未认证；不以此排除原 map。

**命题1（同问题保持）。** 用任何满足以上条件的 $\ell$ 代替 R899 的辅助素数，保留其完整矩阵、各嵌入首自由坐标规则和最终特征零证书，仍然只可能接受原 P 映射。

**证明。** 所有改动发生在同一特征零有理基和原数域输入的好约化中。单位分母保证每个模行均是原行的约化。满基秩门证明所用基仍完整；三个互异根保证三个约化嵌入和后续 Vandermonde 逆合法。
若完整矩阵有满列秩，则非零模子式给一个非零特征零子式，支付原既有的低权比值排除。
否则，模核只选取候选；三个嵌入必须有相同 pivot 列、首 free 列及原 $B$ 首阶。不同辅助素数不必产生同一候选，但任何被接受候选都须回到相同 $F$ 中通过相同完整特征零恒等式。因此没有改变原求解对象。证毕。

这不是在主目标的算术素数集合上增加条件。$\ell$ 只用于一个固定特征零映射的重建。

## 3. 原单位方阵可以从已验精度准确续接

每个嵌入只作一次完整模 $\ell$ 消元、一次选择行和一次求逆。保留 R899 的记号

$$
B_0=\mathcal M[I,J]\bmod\ell\in\operatorname{GL}_r(\mathbf F_\ell),
\quad x_f=1,\quad x_j=0\ (j\notin J\cup\{f\}).
\tag{2}
$$

行集可以因嵌入不同而不同，列集和 free 则须相同。
每次提高精度时，不重新进行这些底域运算。

设已经在精度 $n$ 得到同一个完整向量 $x^{(n)}$，通过该嵌入的全部原行；其 pivot 部分取整数代表 $z_n\in[0,\ell^n)^r$。取新精度 $N>n$，用同一原 Newton germ 与同标签 Hensel 根建立新整数方阵和右端

$$
B_N=\mathcal M[I,J]\bmod\ell^N,\qquad
b_N=-\mathcal M[I,f]\bmod\ell^N.
\tag{3}
$$

Hensel 根在每次续接时显式检查模 $\ell^n$ 等于上轮根。
原 Newton 方程具有同一单位常数和逐阶唯一解，故(3)模 $\ell^n$ 与旧输入完全相同。于是

$$
e_n=\frac{b_N-B_Nz_n}{\ell^n}\in\mathbf Z^r.
\tag{4}
$$

实现逐坐标断言(4)为整除，不把它当作未经检查的精度承诺。

从 $j=n$ 开始，递推

$$
d_j=B_0^{-1}(e_j\bmod\ell),\qquad
z_{j+1}=z_j+\ell^j\widetilde d_j,\qquad
e_{j+1}=\frac{e_j-B_N\widetilde d_j}{\ell},
\tag{5}
$$

其中 $\widetilde d_j\in[0,\ell)^r$ 是实际数字向量。

**命题2（续接不变式）。** 每步(5)是整除，并且

$$
e_j=\frac{b_N-B_Nz_j}{\ell^j}.
\tag{6}
$$

最后的 $z_N$ 是(3)唯一的模 $\ell^N$ 解，且
$z_N\equiv z_n\bmod\ell^n$。

**证明。** (4)给起点。由 $B_N\bmod\ell=B_0$，(5)的分子模 $\ell$ 为零；
代入 $z_{j+1}$ 即得(6)的归纳步骤。至 $j=N$，有
$B_Nz_N=b_N\bmod\ell^N$。单位行列式使解唯一。
每个新项都是 $\ell^n$ 的倍数，给所述兼容。证毕。

初次没有旧向量时取 $n=0,z_0=0,e_0=b_N$，准确回到 R899。
本实现还复核所有 free 坐标、全部模 $\ell$ 坐标以及续轮的全部模 $\ell^n$ 坐标。

该证明不依赖特征零矩阵恰有模 $\ell$ 的秩，也不预设此 chart 真有一个特征零核。
任何未选原行的失败仍由下一节捕捉。

## 4. 每个新精度都重新检查完整原窗

一次续接完成后先释放唯一的高精度方阵，再用同一个有理基形成完整 $A,B$；
重新计算(1)的全部1226行，包含未选的行。
任一非零 residual 只记该 chart 在本精度未认证，不宣布原 map 不存在。

三个嵌入都通过后，以全部提升根作三根插值，并逐坐标重代三根。
然后尝试全部 $3\cdot1056$ 个有理系数的重建。

本轮精度表为

$$
N=512,\quad1024.
\tag{7}
$$

512位未重建成功时，三个已通过全窗的向量留在当前进程内；1024位利用(4)–(5)从512位续接。
底域的完整基、三份 chart、逆矩阵及根标签保持。
不将第一阶段的模结果保存为文件或 GitHub artifact。

有理重建失败、原精确初始支失败或原完整恒等式失败，都只推动到下一个已请求精度。
有限表耗尽则明记未认证。这里没有坐标高度上界，也没有声称有限精度足以证明映射。

## 5. 完整原特征零接受门不变

本篇 producer 从 R899 的 blob
6b345910244f842f30dc636a015ad01fe6af0f33 派生。
原 rational_product_rows、initial_exact_germ_check 与 strict_original_certificate 的正文保持；
同一 $f,v_{\rm new}$ 的构造、原 product recipes 和高精度基扩展也保持。

接受仍要求：

1. 原 free 归一化、其余全部 free 为零；
2. 在原数域 $F$ 中核原 germ、原 $B$ 首阶和 $A$ 的相邻首阶；
3. 同一真实 PARI 基扩展时逐项重现全部低前缀；
4. 对原完整上界 $612(6+1)=4284$，在特征零逐项检查
   $$
   C^3-Qf^3A^2(A+v_{\rm new}B)^2B^2=0,\qquad
   C=(QA')B-A(QB'),
   \tag{8}
   $$
   包括第零项至最后一项，保原绝对首项和微分规范。

仅(8)通过才设置 CERTIFIED_SOLUTION。
实际目标返回仍为 $X=X_{\rm new}/\lambda^2,\ Y=Y_{\rm new}/\lambda^3$；
原整数 Hecke 返回仍为17，坐标为$(106,59,185)$。
后续消费者仍须使用本进程的实际基、recipes 和经认证坐标，不跨到旧 Sage 基。

## 6. 成本、文件及执行范围

本篇节省的是反复底域消元和旧数字的重新提升：
每个嵌入保一份模 $\ell$ 的逆；新精度 $N$ 从旧 $n$ 开始只做 $N-n$ 次 Dixon 乘法。
建立新 germ、重新生成高精度方阵、(4)的整矩阵乘法、完整 residual、插值及原证书仍有成本。

同一时刻只保一份高精度方阵，存储仍为
$O(r^2N\log\ell)$ 位；三份旧解只需 $O(3(2d)N\log\ell)$ 位。
不从这些阶数预报真实内存峰值或任务时长。日志继续逐阶段给实际时钟。

新增：

- scripts/original_small_prime_dixon_map.py；
- scripts/produce-r906-original-rational-hecke-map-small-prime-dixon.py；
- ci/original-P-small-prime-dixon-request.json；
- .github/workflows/rank2-sha-original-P-small-prime-dixon.yml。

固定同一 Sage10.6 镜像、无网容器、只读源码、具名容器退出清理及 source/run/两README身份。
所有数学代码仅在公开 Actions 执行；本地只作源码与文字编辑。
按根规则15，保源码、参数、run和结果hash，不保存可重算矩阵、系数或证书。
