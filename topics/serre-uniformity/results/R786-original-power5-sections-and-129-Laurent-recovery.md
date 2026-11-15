# R786：原五次截面、129个 Laurent 条件与准确短基任务

日期：2026-11-15。状态：**本篇的 Riemann–Roch 缩小、完整截断界和有理块消元已证明；准确短基及后续原函数由公开 Actions 的实际输出分别登记。**

保持 R759/R764 的第4号映射、degree1206、原 $b$、原 $h$、原 $c_0,c_1$ 和零平移。本篇只缩小恢复同一个 $y\in L(Y)$ 所用的截面空间，不另找映射，不重跑原周期、整格、SVP 或已经完成的 Laurent 阶段。

## 1. 已完成的原五次乘积已经足够

保留 R767：
$$
g(Y)=127,\qquad
\mathcal D=\sum_{\text{二十 cusp}}c,\qquad
\mathcal L=K_Y+\mathcal D,\qquad \deg\mathcal L=272.
\tag{786.1}
$$
本篇使用原普通乘积空间
$$
V_5=H^0(Y_L,5\mathcal L),\qquad
\deg(5\mathcal L)=1360,\qquad \dim_L V_5=1234.
\tag{786.2}
$$
这里是五个权二截面的普通乘积，不是整个 $M_{10}$，
也不混入两个椭圆点的额外主部。

R775 的旧公开 run43631335355 虽然完整任务预算耗尽，
但它的 M2、power2、power3、power4、power5 已分别完成
$146,418,690,962,1234$ 维实际基及非零 minor。
它们有各自的 complete 标志、原配置和 SHA；
故可独立复用这些已完成阶段，不要求尚未用到的 power6 或 M6/M12 终证书。
新的准确系数不能从模739系数直接提升，仍须依照同一个原 recipe 生成。

令 $E_y=(y)_\infty$。R778 保留原次数
$$
\deg E_y=1206,\qquad E_y=\mathcal D+E',\qquad \deg E'=1186;
\tag{786.3}
$$
每个 cusp 的原极点阶为 R774 实际给出的 $e=1$。

**定理 786.1。** 原 $y$ 可写成 $A/B$，其中
$A,B\in V_5$、$B\ne0$。全部这样的线性关系空间为
$$
\mathcal K_5
=\{(yB,B):B\in H^0(5\mathcal L-E_y)\},
$$
且
$$
\dim_L\mathcal K_5
=28+h^0(K_Y-5\mathcal L+E_y)\ge28.
\tag{786.4}
$$

**证明。** $\deg(5\mathcal L-E_y)=154$。
Riemann–Roch 给
$h^0(5\mathcal L-E_y)=154+1-127+h^1=28+h^1>0$。
任取非零 $B$，其零除子吸收 $y$ 的全部极点，故 $A=yB\in V_5$。
反之任何关系都要求 $B\in H^0(5\mathcal L-E_y)$。
对偶性给 (786.4)。$\square$

$154<2g-2=252$，所以本篇不将最后的 $h^1$ 擅自置零。
后续矩阵核至少28维；实际秩须由实际计算决定。

普通四次空间次数仅 $1088<1206$，不可能用同一线丛的两个截面之比表示此 $y$：
一个比值的极点除子被分母截面的零除子所控制。
因此五次是这组普通整数次幂中第一个可用次数。
这不是关于任意除子或任意表示的全局最优声明。

## 2. 129个完整 Laurent 系数给出全球恒等式

每个 cusp 上，以原权十的对数微分框架看待 $V_5$；
这个框架在 $5\mathcal L$ 中是单位，所以 Fourier 零阶就是截面零阶。
所有未知基坐标仍在原 $L$ 中，不能先放到任意更大的字段。

对 $A,B\in V_5$，考虑亚纯截面
$$
F=A-yB\in H^0\bigl(Y_L,5\mathcal L(E_y)\bigr).
$$
它作为 $5\mathcal L$ 的亚纯截面的极点至多为 $E_y$。
若在同一个参考 cusp 的完整 $M=L(\xi_{41})$ 系数中
$$
[u^n](A-yB)=0,\qquad -1\le n\le127,
\tag{786.5}
$$
则参考 cusp 处的零阶至少128。
R778 的原二十 cusp 单一 $L$-Galois 轨道将该零阶传到全部 cusp。
这只运输零阶，不假设原参数在 Galois 下固定。

若 $F\ne0$，其零、极点除子须满足
$$
\deg(F)_0-\deg(F)_\infty=1360.
$$
但 (786.3)–(786.5) 给
$$
\deg(F)_0\ge20\cdot128=2560,\qquad
\deg(F)_\infty\le1186,
$$
从而左侧至少1374，大于1360，矛盾。故
$$
\boxed{\ (786.5)\quad\Longleftrightarrow\quad A=yB
       \text{ 在原 }Y_L\text{ 上全局成立}.\ }
\tag{786.6}
$$
等价的截断条件是 $20\cdot129>1360+1206$；严格余量为14。

$A$ 只需原 $u^{0},\ldots,u^{127}$，
$B$ 需至 $u^{128}$，所以统一输出全部基至 $u^{128}$。
原 $y$ 只需至 $u^{127}$。
不需要权十二的 $D_\star$，也不需要给 $V_5$ 额外选择一个全球分母；
上述论证直接对线丛截面成立。

单个非零准确解就足以认证原函数，不必先产生完整核。
若 $B=0$，则 (786.6) 给 $A=0$，故任何非零核向量都有 $B\ne0$。

## 3. 权十逐项的原切向下降没有额外标量

记
$$
K=\mathbb Q(s),\quad s^2=-3,\quad L=K(b),\quad
\xi=e^{2\pi i/41},\quad u=q_Y,\quad v=\xi^{-10}u.
$$
R775 的每个 $T_{j,r}$ 是原完整 $G_{82}$ 半线性右作用下固定的权二截面。
右作用与乘法相容，所以每个五次乘积本身在权十作用下固定。
这里对 $A$、$B$ 各自的原基截面证明下降，
没有从比值 $A/B$ 的不变性倒推。

取 R781 的同一个
$$
g=-\operatorname{diag}(1,-1)T^{-40}
 =\begin{pmatrix}-1&40\\0&1\end{pmatrix}\in G_{82}.
$$
在权十上，$-I$ 的因子是 $(-1)^{10}=1$。
$T^{-40}$ 的 slash 因子 $(c\tau+d)^{-10}$ 等于1。
$\operatorname{diag}(1,-1)$ 依原 Zywina 半线性规范
只施加 $\sigma_{-1}:\xi\mapsto\xi^{-1}$，固定 $K$。
所以对每个原五次基截面 $F=\sum a_nu^n$，准确有
$$
\sigma_{-1}(a_n)=\xi^{20n}a_n,\qquad
a_n^+=\xi^{10n}a_n\in L(\xi+\xi^{-1}).
\tag{786.7}
$$
其原 Eisenstein recipe 的 Fourier 系数本来只在 $\mathbb Q(\xi)$，
没有 $s$ 或 $b$ 系数。因此更强地，
$$
a_n^+\in\mathbb Q(\xi+\xi^{-1}).
\tag{786.8}
$$
这是后续有理块消元的依据；不是把未知关系坐标从 $L$ 缩小到 $K$ 或 $\mathbb Q$。

对准确的 $82^{10}F$，(786.8) 的二十坐标全为整数。
使用 R781 的 Chebyshev 整数转换，并逐项核
$c_r=c_{41-r}$，不能以平均的办法制造不变性。
原标准参数和 $v$ 参数仍按 (786.7) 可逆运输。

## 4. 直接复用已完成 R781 的准确 Laurent 阶段

R781 run43679703344/source
f0292795817a534937d35904e2e11275631e878d
已经完成同一原字段中的 $R_0,\ldots,R_{142}$。
本篇不重跑它。
令 $\kappa$ 为原 $H^3$ 在 $v$ 下的一次系数。
同一关系为
$$
246^3\kappa^{n+2}A_n+
 \sum_{j=0}^{n+1}\kappa^jR_{n-j+1}B_j=0,
 \qquad -1\le n\le127.
\tag{786.9}
$$
$n=-1$ 恰给 $B_0=0$。
需要的 Laurent 状态仅为 $R_0,\ldots,R_{128}$，
以及 $\kappa,\ldots,\kappa^{129}$；
后者也已在 R781 的已完成状态范围中，不需要生成新 Laurent 阶。

展开成二十个 $\xi+\xi^{-1}$ 坐标后，
原完整线性系统至多为
$$
2580\times2468\quad\text{于 }L.
\tag{786.10}
$$
它的准确核为 (786.4)，而非旧权十二空间的308维核。
由于所有逐行乘数非零，准确通过 (786.9) 就通过 (786.5)，
继而给原 $y$。辅助模核或预期 rank 均不能替代这一最终验证。

## 5. 先在有理数上消去 A 块

取原1234个五次截面为基，统一用准确 $82^{10}$ 整数尺度。
其在 $v$ 下的二十坐标都是整数。
记 $F_A\in\operatorname{Mat}_{2580\times1234}(\mathbb Q)$
为这些截面在 $v^{-1},\ldots,v^{127}$ 的展开矩阵；
前二十行是零。
记 $F_B$ 为所需到 $v^{128}$ 的基矩阵。
关系的未清行版本是
$$
F_A\mathbf a-C_y\mathbf b=0,
\tag{786.11}
$$
其中 $C_y$ 表示先取 $B$ 的展开再乘原 $y$，
结果保留同一129阶、二十坐标。
$C_y$ 的条目在 $L$，并不预称在 $\mathbb Q$。

完整 cusp 前缀至 $v^{68}$ 已在 $V_5$ 上单射：
如果所有这些系数为零，则二十 cusp 上的总零次数至少
$20\cdot69=1380>1360$。
因此 $F_A$ 的列秩为1234，可选择1234个原坐标行 $J$，
使 $F_0=F_A[J]$ 在 $\mathbb Q$ 上可逆。
余下1346行记为 $R$。于是 (786.11) 等价于
$$
\mathbf a=F_0^{-1}C_y[J]\mathbf b,
$$
$$
\boxed{\quad
\bigl(C_y[R]-F_A[R]F_0^{-1}C_y[J]\bigr)\mathbf b=0.
\quad}
\tag{786.12}
$$
后一个矩阵只有 $1346\times1234$ 个 $L$ 条目。
同一个有理 $F_0$ 可用于全部 $L$ 嵌入，
不必为每个嵌入重复处理 A 块。
非零 $B$ 候选代回 (786.9) 的完整特征零等式后才认证。

## 6. 还可先准确去掉 B 的 cusp 常数项

记 $E_0\in\operatorname{Mat}_{20\times1234}(\mathbb Q)$
为基的 $v^0$ 二十坐标。
其行秩恰为20。事实上
$$
H^1(5\mathcal L-\mathcal D)=0
$$
因为次数为1340，大于252。
故向二十 cusp 的纤维评价满射；
参考 cusp 的完整 residue-field 坐标就是这个20维目标。

在 $\mathbb Q$ 上取 $\ker E_0$ 的基矩阵
$$
Z\in\operatorname{Mat}_{1234\times1214}(\mathbb Q).
\tag{786.13}
$$
于是 $B_0=0$ 等价于 $\mathbf b=Z\mathbf c$。
因为所有候选 $B$ 都定义在 $L$ 上，该零也在全部 cusp 成立，
准确对应 $H^0(5\mathcal L-\mathcal D)$；
没有仅凭一个数值 cyclotomic 嵌入令其为零。

删去已经自动满足的 $n=-1$ 的二十行，
剩余 A 块有2560行、1234列，仍可用 §5 的原 $F_0$。
最后只需解
$$
\boxed{\quad
\mathcal S_y\mathbf c=0,\qquad
\mathcal S_y\in\operatorname{Mat}_{1326\times1214}(L).
\quad}
\tag{786.14}
$$
该变换保持原全部核，故
$$
\dim\ker\mathcal S_y=28+h^1(5\mathcal L-E_y),\qquad
\operatorname{rank}\mathcal S_y\le1186.
\tag{786.15}
$$
这个不等式是结构界，不是任何运行已得到的 rank。
工程上可按实际模秩选择主元与自由列，重构一个候选，
再准确验证全部 (786.9)。

可以只在合法辅助素数或其提升上形成 Schur 矩阵，
避免先展开巨大的特征零有理逆矩阵。
如果使用未清行的 $y$ 级数，必须核该约化中的 $\kappa$ 可逆；
最终特征零验证仍可直接用无 $\kappa$ 逆幂的 (786.9)。
任何有限域拟合都不会因本节而免去这一步。

## 7. 本次准确短基核心及完成条件

新核心为
[scripts/R786_exact_power5_short_basis.py](../scripts/R786_exact_power5_short_basis.py)。
它独立使用原 R777 中尚未执行的准确 E1、半迹、行列式相位和乘积实现，
只生成原 power5 所需的依赖，不生成 M6/M12 椭圆补方向，
不执行694阶 Hodge 立方坐标求解，不改变原 recipe。

输入是原 R771 完整证书、manifest、82个有限 E1 行及原 H82 标签群；
以及旧 R775 的以下六个已完成文件：

| 文件 | SHA256 |
|---|---|
| R775-basis-M2.json.gz | 51113988c90b301cb6117fec5c294b77110e1826bf00229b7993ba82144f5d3d |
| R775-basis-power-2.json.gz | 734a61e967c51ba3c9cd93eaff1a81fba165600110abb941dfdbbeed41b6ebe4 |
| R775-basis-power-3.json.gz | 00361e5155c429de5c54b613b8a3cb46ac9530c554e1a812823748bb2bf5fe18 |
| R775-basis-power-4.json.gz | 85beb7662eee64f4eca9e205314a6625506e3041bea199985489c7cf1f62dd4e |
| R775-basis-power-5.json.gz | 7aff6faa89a91649db5549bbf9360647534bff6f9586ce3f5963e322d33c30ba |
| R775-determinant-cosets.json.gz | 759d6f7643032fa358a0da02417d576f5d6f89a3996f9e6fb4b3bf954c52ecac |

旧 producer 的预算退出124与 full-run complete=false 明确保留。
逐必要 stage 核 complete、相同 configuration、原 core SHA、
manifest 条目、文件大小及 SHA；各基还核原 rank 和保存的非零 minor。
不能把整个失败 run 改称 success，也不要求此任务消费未完成文件。

新输出为每个原基的准确
$$
82^{10}F_j\pmod{u^{129}}
   \in\mathbb Z[\xi]/(\Phi_{41})[u]/(u^{129}),
\tag{786.16}
$$
仍保存原40个 $\xi$ 坐标及原顺序。
每个新 E1、种子行列式像、乘积行独立完成后保留，
与已完成 R771/R775 在同一 $\xi\mapsto538$ 的所有129项比较。
这些模比较核对原输入、相位和 recipe；
特征零数值来自准确整数公式，不由模值猜升。

两个 numerator 使用同一个 $82^{10}$ 因子，所以其比值不变。
该因子仍在产物中明记，不改变原目标 $b$ 或微分246。

成功证书只表示1234条准确短基已生成并逐项通过比较。
它不表示 (786.9)、(786.14) 已求解，不表示 $y,\beta$ 或高度已输出。
原曲线的函数恢复在接下来的真实 L 线性计算中继续。
所有新数学只在公开仓库 Actions 运行；
精确大表只作当前任务的一日临时传输，不入 Git 或 Release。
仓库仅保存脚本、参数、run、输出 SHA 与小结果摘要。

## 依据

- [R767](R767-original-quotient-low-weight-RR-basis-and-cusp-order-bound.md)：
  原 $\mathcal L$、亏格、degree、正常生成及普通乘积空间。
- [R772](R772-original-RR-descent-and-exact-function-recovery-certificates.md)、
  [R775 方法](../notes/R775-original-K-defined-RR-bases-method.md)：
  原 K 定义半线性迹、每个实际 recipe 及保持原模型的下降。
- [R778](R778-original-cusp-orbit-and-short-exact-recovery.md)：
  二十 cusp 的原 L 轨道、原 $y$ 次数和短展开法。
- [R781](R781-original-tangent-descent-and-inverse-free-Laurent-relations.md)：
  原 $g$、切向相位、整数 Chebyshev 转换及无逆幂关系；
  实际 Laurent run43679703344 的结果另已登记。
- [R777 方法](../notes/R777-exact-short-K-basis-and-Hodge-coordinates-method.md)：
  同一准确整数 E1 常数、126项半迹、82的权尺度与 PACK79 乘法。
- D. Zywina，*Explicit open images for elliptic curves over Q*，2022；修订版2024，
  [作者稿](https://pi.math.cornell.edu/~zywina/papers/ExplicitOpenImage.pdf)，
  Lemma4.7、Corollary4.10：原半线性右作用及准确 Fourier 规范。
