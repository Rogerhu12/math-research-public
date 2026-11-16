# R899 原 P 映射的单分裂素数 Dixon lifting 与完整认证保持

日期：2026-11-16。**状态：以下精确算法、同来源不变性和认证范围已证明；本篇新增实现尚未取得公开执行回执，未声称已经求得原映射或测得速度提升。**

本篇为 [R892](R892-original-two-map-pari-rational-basis-and-unchanged-certification.md)
的原 P 映射增加一条可选重建路径。固定原完整基、原 Hecke 方向、三个数域嵌入、有限矩阵、自由坐标规则和最终特征零证书。
改变的只有坐标重建：用一个分裂素数的高精度单位方阵 lifting，
替代在许多素数处反复消元。

这不是在原算术素数中增加一个来源条件。下文 $\ell$ 是重建用辅助素数，
与原主目标中的变化素数无关。

## 1. 同一原对象与完整有限矩阵

完整固定数据照 R892：
$$
F=\mathbf Q(a),\quad a^3=17,\qquad
u=(915,1097,2962)/55569,
$$
$$
\lambda=(68+7a-13a^2)/3,\qquad v_{\rm new}=\lambda^3v,
\qquad H_u/\lambda=qf(Q),\quad Q=q^3.
\tag{1}
$$
不重新选择 $u$，不把 $\lambda$ 当作自由首项归一化。

对偶数权 $k\in\{4,6\}$，保同一完整有理空间
$\mathcal M_k=M_k(\Gamma_0(867),\mathbf Q)$，记
$$
d=102k-84,\qquad m=204k+2.
$$
其基 $b_1,\ldots,b_d$ 仍是 R892 同一 PARI $M_2$ 基生成并经原全维数
有限域秩门接受的乘积基。原全部有理系数前缀保留。

令
$$
y(Q)=QY_{\rm new}(Q),\qquad y(0)=-1,
$$
为 [R889](R889-original-two-map-newton-germs-and-exact-normalization.md)
给出的同一原形式支。
对坐标向量 $x=(x_A,x_B)\in F^{2d}$，置
$A=\sum x_{A,j}b_j,\ B=\sum x_{B,j}b_j$。
原有限矩阵 $\mathcal M$ 的行是
$$
[Q^i](QA-yB),\qquad 0\le i\le204k+1.
\tag{2}
$$
故权六仍是完整 $1226\times1056$ 矩阵；权四仍是
$818\times648$。没有缩短重建窗或只保一组选择行。

当前 request 选择 $k=6$，只是继续原权六问题。
权四的原排除另见 R898；本算法也保留权四入口，未借更换计算基另添负结论。

## 2. 一次模素数选取与准确固定 chart

选固定分裂素数 $\ell$，使
$$
\ell>6M+1,\qquad \ell\nmid51,
\tag{3}
$$
其中 $M$ 是所用原 germ 最大阶；实现中 $M=204k+2$。
还逐项检查原基和 $f,v_{\rm new}$ 全输入分母在 $\ell$ 为单位，
以及原有理基在该素数处的完整 Sturm 前缀仍满秩。
要求 $X^3-17$ 有三个不同根 $\alpha_0,\alpha_1,\alpha_2\in\mathbf F_\ell$。

在每个原嵌入 $a\mapsto\alpha_i$ 上建立整个 (2)，
使用与 R892 相同的 echelon 规则求 pivot 列。
若其中任一个完整有限矩阵的列秩为 $2d$，这个单位子式已严格排除
该原权下的非零比值来源；这是保留的旧合法排除门。

否则要求三个嵌入具有同一 pivot 列集合 $J$、
同一首个 free 列 $f$ 和同一约化 $B$ 的首阶。
记 $r=|J|$。固定
$$
x_f=1,\qquad x_j=0\quad(j\notin J\cup\{f\}).
\tag{4}
$$
这些是原 producer 已使用的坐标规则，不是改选原 $u$。

每个嵌入可以各自选择一个行集 $I_i$，使
$$
B_{i,0}=\mathcal M_i[I_i,J]\in\operatorname{GL}_r(\mathbf F_\ell).
\tag{5}
$$
程序只在这里求一次 $B_{i,0}^{-1}$，并检查由 (4)–(5)
得到的向量满足**全部**模 $\ell$ 行。
选择行、pivot、free 和模素数解均记录 hash。
三嵌入若没有共同 chart，本轮只记未认证。

行集 $I_i$ 可以不同：当原全矩阵在特征零确有这个秩和 chart 时，
它们都求同一规范向量的三个嵌入。
算法不预先假设这一点；特征零秩或其它行的异常由后续全窗与最终证书处理。

## 3. 素数幂上的三个原嵌入与同一个 Newton germ

取数字精度 $N$，置 $L=\ell^N$。
从三个模素数根的固定标签出发，逐个作唯一 Hensel 提升
$\widetilde\alpha_i\in\mathbf Z/L$：
$$
\alpha\longmapsto
\alpha-(\alpha^3-17)(3\alpha^2)^{-1}
\pmod{\ell^{\min(2n,N)}}.
\tag{6}
$$
$\ell\nmid51$ 支付导数单位性。高位不重新排序三个根。
唯一性也保留原三个根之间的三次单位比值，不另拼接三个不相容的局部支。

在每个 $\widetilde\alpha_i$ 下，把同一个 $f,v_{\rm new}$ 精确约化到
$R_N=\mathbf Z/L$，再使用 R889 的同一 Newton 方程
$$
3Qe'+e=fr,\qquad r^2=1-4v_{\rm new}Qe^3,\qquad
y=-\frac{1+r}{2e^3}.
\tag{7}
$$
所有系数都在 $R_N$ 中精确计算。

**单位环延伸的证明。** R889 在这里使用的常数逆为
$2,3$、$j$、$3j+1$ 以及已经检查的输入分母；
相应幂级数逆的常数项为单位。
(3) 对底素数 $\ell$ 而非对环特征 $\ell^N$ 支付全部这些逆。
原 Newton 余项平方增阶只用环恒等式，故在 $R_N$ 上仍成立；
原全阶两条定义方程的 residual 检查逐项保留。
没有使用“非零元素都可逆”的域假设。

实现亲读了 R889 helper 的分支：其有限环分支只检查
is_finite 与 characteristic，然后执行这些单位操作；
没有额外 is_field 依赖。本 helper 在调用前显式加 (3)，
不能仅因 $\ell^N>6M+1$ 就忽略小底素数的非单位。
所得每个完整 germ 还逐项约化回相应模 $\ell$ germ。

## 4. 固定单位方阵的精确 Dixon 递推

在第 $i$ 个嵌入上，只建立选取行和选取 pivot 列的高精度方阵
$$
B_i=\mathcal M_i[I_i,J]\pmod L,\qquad
b_i=-\mathcal M_i[I_i,f]\pmod L.
\tag{8}
$$
取它们的整系数代表 $B_N,b_N$。
不建立高精度的完整 $m\times2d$ 矩阵。

固定模 $\ell$ 逆 $B_0^{-1}$，递推
$$
e_0=b_N,\qquad
d_j=B_0^{-1}(e_j\bmod\ell),
\tag{9}
$$
$$
e_{j+1}=\frac{e_j-B_N\widetilde d_j}{\ell},
\qquad
z_N=\sum_{j=0}^{N-1}\ell^j\widetilde d_j,
\tag{10}
$$
其中 $\widetilde d_j$ 是 $[0,\ell)$ 中的数字向量。

**命题 1。** 每次 (10) 都是整除，且
$$
e_j=\frac{b_N-B_N\sum_{a<j}\ell^a\widetilde d_a}{\ell^j}.
\tag{11}
$$
特别 $B_Nz_N\equiv b_N\pmod L$。

**证明。** (9) 使分子模 $\ell$ 为零，故除法在整数中进行。
由 $j=0$ 的恒等式归纳，代入 (10) 即得 (11)。
在 $j=N$ 时右侧为整数，得到所述同余。证毕。

原实际选取方阵与 $B_N$ 模 $L$ 相同且行列式为单位，
故 (10) 给其唯一模 $L$ 解。每个数字仍只乘同一个
$B_0^{-1}$；不在更高精度重新消元或求逆。

程序逐数字验证整除，按每 16 个数字报告时钟。
三个嵌入依次处理；每次只保一个高精度方阵，
在后续全窗复乘之前明确释放它。

## 5. 所有未选原行必须复乘

由 (4)、(10) 恢复整个 $2d$ 坐标向量。
用同一原基形成完整 $A,B$，然后计算
$$
QA-yB\pmod{(L,Q^{204k+2})}.
\tag{12}
$$
(12) 逐项覆盖 (2) 的所有 $m$ 行，包括没有参与 (8) 的行。
它只需要两个实际形式的加权和与一次幂级数乘积，
不需要高精度完整长方阵。

若任一个系数非零，所选方阵的解尚不是这个固定 chart 的原全窗解。
程序记录首个非零行、其 $\ell$ 估值和全 residual 的 hash，
然后返回“固定 chart 未认证”。**这不是原映射不存在的证明**：
原高精度矩阵的秩可能增加，或其它 free 坐标组合仍可能有解。

只有三个嵌入都通过全部 (12)，才进入有理重建。
即使三个 (12) 都为零，也仍未证明特征零的全部恒等式。

## 6. 三根恢复、有理重建与原最终证书

在同一个 $R_N$ 中，
$$
V=(1,\widetilde\alpha_i,\widetilde\alpha_i^2)_{i=0}^2
$$
的 Vandermonde 行列式为单位，因为三个根模 $\ell$ 互异。
对每个坐标，用完整提升根的 Lagrange 公式恢复
$$
c_0+c_1a+c_2a^2,\qquad c_j\in R_N.
\tag{13}
$$
实现逐坐标重代三个完整根检查 (13)，不是在高位仍用三个模 $\ell$ 根。

随后对这 $3(2d)$ 个整数剩余分别进行标准有理重建。
这里没有给出原坐标高度上界；$N=128$ 只是本轮有限预算。
重建失败、初始精确支失败或最终恒等式失败均只记未认证，
可在下一原 request 把 $N$ 增至 $256$。
不会把达到预设数字数当成一个排除定理。

接受路径完整保留 R892 原特征零函数：

1. 检查同一 free 归一化与所有其它 free 坐标为零；
2. 用原数域、原 $f,v_{\rm new}$ 检查原初始 germ、$B$ 首阶及 $A$ 的相邻首阶；
3. 用同一个真实 PARI 基扩展到原高精度，必须逐项重现全部旧前缀；
4. 在特征零完整检查
   $$
   C^3-hA^2(A+v_{\rm new}B)^2B^2=0,\qquad
   C=(QA')B-A(QB'),\quad h=Qf^3,
   \tag{14}
   $$
   从第零项到原 $612(k+1)$ 上界全部系数，并保原绝对首项和微分规范。

因此只有原严格证书 (14) 通过才报告原 P 映射认证。
原 Sturm/全局模性与原支唯一性沿用 R870/R889/R892 的完整证明；
它们同时确定 $A/B$ 的完整原 germ。
没有另用一个有限模 $\ell^N$ 向量认证映射，也没有再次在
$\mathbf Q(a)$ 中重算整条高阶 reference germ 来替换原证书。

若成功，整数 Hecke 返回仍为 $17$，其坐标仍是 $(106,59,185)$，
实际目标返回仍为
$X=X_{\rm new}/\lambda^2,\ Y=Y_{\rm new}/\lambda^3$。
同进程 consumer 必须使用本 producer 自己的基、recipes 和实际认证坐标。

## 7. 资源成本与可复用实现

以 $r$ 为选取方阵阶数。

- 模素数的完整秩、选行和逆只在每个嵌入做一次，成本为固定数量的
  $O(r^3)$ 域运算；不同素数不再反复消元。
- Dixon 阶段为每个嵌入 $N$ 次 $O(r^2)$ 的矩阵向量乘法。
  其中整矩阵元素的位长为 $O(N\log\ell)$，
  右乘的数字只有 $O(\log\ell)$ 位；残差的位长同阶。
- 高精度方阵存储为 $O(r^2N\log\ell)$ 位。三个嵌入顺序处理，
  不同时保三个方阵，也不建立高精度的 $1226\times1056$ 全矩阵。
- 素数幂上的原 Newton germ、选取方阵构造、全 (12)、三根恢复及
  (14) 仍有真实成本；这里不宣称整个任务只剩消元，也不预报运行时间。

阶段时钟分别覆盖模素数 germ、完整初始矩阵、选取逆、
素数幂 germ、方阵列构造、每 16 个 Dixon 数字、
全窗复乘、三根恢复、有理重建、原初始精确检查及原全证书。
这使实际瓶颈由公开日志确定，不从旧超时推测一个未观测步骤。

新增文件：

- scripts/original_padic_dixon_map.py；
- scripts/produce-r899-original-rational-hecke-map-dixon.py；
- ci/original-P-dixon-request.json。

producer 从 R892 blob b1a6be2cf9ff2addf0f83bccd6b6d6837813a019 派生。
原 exact CM 输入、PARI 基、乘积选择、高精度扩展和最终认证函数保持；
只把 CRT 主循环换成本篇固定 chart 路径。
现参数为 $\ell=1000000033,N=128,k=6$，运行时仍要实际验证所有素数、分裂、分母和基秩门。

新增独立公开 workflow 为 `.github/workflows/rank2-sha-original-P-dixon.yml`。超时使用 kill-after，并在退出时强制删除
有固定名字的实际容器，避免只终止 Docker 客户端而留下数学进程。
无网络数学容器、固定 Sage 镜像、只读源码及原 README/source/run 身份继续保持。

所有数学执行仅在公开 Actions。本篇未在本地或工具编排器运行数学代码，
也未记录新 PASS。按根规则15，只保脚本、参数、run 与输出 SHA-256；
不保存可重算系数、矩阵或证书输出。
