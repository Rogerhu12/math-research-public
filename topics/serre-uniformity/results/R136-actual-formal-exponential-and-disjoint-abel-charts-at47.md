# R136：层 41 的真实形式指数、两个不相交 Abel 局部族与长乘点的完整比较

**状态：已证明；全部所列有限环计算已完成。** 本文在 R102/R110 的固定实际模形式评价模型上构造两个定义于 $\mathbf Q_{47}$ 的局部 Abel 逆。它们把 R121 的真实对数还原为完整除子理想，并分别与独立的 304 位长乘结果在全部 $820\times73$ 个 Picard 坐标上相同。本文不给尚未选择补空间的 Poincaré 纤维坐标冠以“局部高度”之名。

## 1. 固定模型与结论

设
$$
 X=X_{\rm ns}^+(41),\quad g=54,\quad
 R_0=\mathbf Z_{47},\quad R=R_0[i],\quad i^2=-1,\quad q=47^4.
$$
计算使用 $R/qR$，半线性下降是 $i\mapsto-i$。沿用 R102/R110 的固定线丛 $L$、实际截面基和评价规范：
$$
 \deg L=126,\qquad h^0(L)=73,\quad h^0(2L)=199,\quad h^0(3L)=325.
$$
820 个实际评价点由椭圆曲线 $E_0:y^2=x^3+x+32$ 的 41 水平结构给出。其特殊纤维 $j=9$，避开 0、1728 及尖点。

**定理。** 在上述固定规范下，有两组各由 27 个 Frobenius 二元轨道组成的有效除子 $Z_1,Z_2$，以及实际有理截面 $v_i,g_i\in H^0(X,L)$，满足：

1. $\deg Z_i=54$，$D_i=\operatorname{div}(v_i)=Z_i+R_i$，$\deg R_i=72$。所有 $Z_i$ 上的零点为单零点，$Z_i\cap R_i=\varnothing$。
2. $D_1$ 与 $D_2$ 的特殊纤维不相交。
3. 移动 $Z_i$ 的 54 个点、固定 $R_i$，给出 $J$ 在原点的整局部坐标：
   $$
   (t_1,\ldots,t_{54})\longmapsto
   [R_i+Z_i(t)-D_i].
   $$
   其微分矩阵可逆于 $R$。对任意满足下降的 $z\in47\operatorname{Lie}(J)(R/qR)$，本文算法唯一求出 $t\in(47R/qR)^{54}$，并给出代表 $\exp_J(z)$ 的完整 73 维理想
   $$
   H^0\bigl(X,2L-R_i-Z_i(t)\bigr).
   $$
4. 对 R121 的实际 $Y=mB_{-4}$，其中 $B_{-4}=[Z_{-4}-D]$、$m=\#J(\mathbf F_{47})$ 为该文 304 位整数，两个算法输出各自都与已发布长乘点完全相同，模 $47^4$。比较使用全部 $820\times73$ 个规范化 Picard 坐标，而非仅比较对数。

有限精度结论不声称唯一决定任何未计算的高位。

## 2. 两组实际非特殊 54 点

令 $K$ 为 R110 的 $73\times54$ 全纯微分截面核基，$W$ 为 R102 的 $820\times73$ 实际评价矩阵。依固定点次序，逐个加入 Frobenius 二元轨道；只有当 $(WK)|_Z$ 的剩余域秩增加 2 时才加入，直至得到 54 行。第二组使用同一规则并排除第一组全部点。

脚本在两组上分别检验单位 $54\times54$ 子式。完整点编号保存在 4139 字节的小型最终证书中。因这里的点均避开椭圆点，局部参数可统一取实际椭圆曲线族
$$
 E_t:y^2=x^3+x+32+t.
$$
41 挠点及水平结构沿此族唯一 étale 提升，且 Frobenius 相容。注意 $t$ 是模曲线的实际局部参数，不是 Jacobian 的任意线性标签。

R123 的规范化微分公式给出
$$
 \beta(t)=\frac{-3}{4+27(32+t)^2},\qquad
 \Omega(t)=\beta(t)W(t)K.
\tag{2.1}
$$
特别 $\beta(0)\equiv38\pmod{47}$ 为单位。这一因子在所有计算中保留；原始权二截面的数值没有被直接当作 $dt$ 系数。

两个实际 Abel 切矩阵的行列式依次为
$$
 3049719+4009663i,\qquad3583710+477067i\pmod{47^4}.
\tag{2.2}
$$
二者均为单位。Abel 映射微分的对偶是全纯微分在移动点切向上的评价；可由单点移动的 Čech 主部及留数配对直接得到，亦与 R121/R123 的切向规范一致。因此其在 $Z_i$ 的微分可逆，形式逆函数定理给出所需整 Abel 逆。这一结论没有使用 $J$ 的某个未经认证的平面方程。

## 3. 有理基截面、72 次残余理想与不相交证明

先取实际核
$$
 V_i=H^0(L(-Z_i)),\qquad\dim V_i=19.
$$
核的半线性矩阵从 R102 的 Frobenius 作用限制而来。用 $c\mapsto c+A_i\bar c$ 取实际有理截面，得到 $v_i,g_i$。脚本完整检验下降等式。选取时要求：

- 两截面在其余 766 个评价点的值为单位；
- 在 $Z_i$ 的一阶实际参数导数为单位。

于是 $D_i=Z_i+R_i$，且 $Z_i$ 与残余 $R_i$ 不相交。为求完整残余理想，在排除 $Z_i$ 的 766 行上计算
$$
 U_i=\{s\in H^0(2L):(g_i/v_i)s\in H^0(2L)\}.
\tag{3.1}
$$
这不是仅在有限集合上猜测有理恒等式：判定产生的等式为
$g_is=v_it$，两边是 $3L$ 的截面，其次数 378 小于 766；因此逐行相等即为全曲线相等。

比值 $g_i/v_i$ 的极除子包含在 $R_i$，次数至多 72。对于任意这样的小极除子 $P$，Riemann–Roch 给出
$\operatorname{codim}H^0(2L(-P))=\deg P$，因为剩余次数至少 180，大于 $2g-2$。实际残余矩阵秩恰为 72，所以极除子就是整个 $R_i$，无未察觉的残余公因子。由此
$$
 U_i=H^0(2L(-R_i)),\qquad\dim U_i=127.
\tag{3.2}
$$
脚本还验证再限制于固定 $Z_i$ 的核恰为 $v_iH^0(L)$，并检验全部半线性下降。

不相交不是从有限评价点值推测的。对 $D_1=\operatorname{div}(v_1)$，实际限制商
$$
 H^0(2L)/v_1H^0(L),\qquad
 H^0(3L)/v_1H^0(2L)
$$
均为秩 126 的自由模。乘以 $v_2$ 在它们之间的行列式为
$$
 3398422+4576517i\pmod{47^4},
\tag{3.3}
$$
是单位。这正是 $v_2|_{D_1}$ 处处可逆的判据，故两个完整 126 次基除子的特殊纤维不相交。该行列式依赖限制商基，本文只使用其为单位这一不变量。

## 4. 实际模形式三阶 jets

为两个局部族一次计算 108 个点的全部 73 个实际截面系数至 $t^3$。计算保留 R102 固定的 80 次非分歧系数环、同一 Weil 根、同一迹权重及基变换。

具体步骤为：

1. 在 $R_{80}[t]/(t^4)$ 中，用 $\psi_{41}(x;1,32+t)=0$ 唯一提升 $P,Q$ 的横坐标，再由 $y^2=x^3+x+32+t$ 及既定纵坐标提升纵坐标。
2. 全量验证曲线方程、$[41]P=[41]Q=0$、$\operatorname{Frob}(P)=Q$、$\operatorname{Frob}(Q)=[35]P$。
3. 通过实际割线/切线公式计算全部 1680 个权一 Eisenstein 值，检验奇性。分母的常数项批量求逆，再在截断幂级数环作两次 Newton 求逆。
4. 采用 R102 已证明的实际 $\mathrm{SL}_2$ 平均和带 Weil 根的相对迹，求各权二截面四个系数；没有以抽象表示或同维空间替换实际截面。
5. 零阶系数与已发布 R102 的 108 行逐项相同；一阶系数与已发布 820 点一阶 jets 的对应 108 行逐项相同；全部四组系数逐个满足完整半线性 Frobenius 等式。

内存优化仅把 $840\times840$ 迹矩阵分为四个 $210\times840$ 块，求和公式未改变。GP 的整数/有限环运算不使用浮点近似。

原始 jets 压缩后 222443 字节，SHA256：

`7dfbbde5943c6ce7441100116a40d244f909e8724cc91f2db5f6461b0caf267d`。

它是可由源码重建的中间矩阵，故只在工作目录保留，不重复收入仓库。

## 5. 由真实对数解实际移动参数

把式 (2.1) 写成
$$
 \Omega(t)=\Omega_0+\Omega_1t+\Omega_2t^2+\cdots.
$$
第 $j$ 行对应第 $j$ 个移动点。实际 Abel 积分在模 $47^4$ 下为
$$
 z=\sum_{j=1}^{54}\left(t_j\Omega_{0,j}
       +\frac{t_j^2}{2}\Omega_{1,j}
       +\frac{t_j^3}{3}\Omega_{2,j}\right).
\tag{5.1}
$$
所有系数来自式 (2.1) 的真实微分。更高项在 $t_j\in47R$ 时消失，因为整系数积分的第 $n$ 项估值至少 $n-v_{47}(n)\ge4$（$n\ge4$）。这里没有忽略可能的积分分母。

行参数约定下，Newton 的 Jacobian 第 $j$ 行为
$$
 \Omega_{0,j}+t_j\Omega_{1,j}+t_j^2\Omega_{2,j}.
$$
它模 47 与行列式为47进单位的矩阵 $\Omega_0$ 同秩。由零开始的两次 Newton 修正已达到模 $47^4$；源码最多进行三次并最后验证式 (5.1) 的精确相等。对每组参数还验证 $t_{\tau(j)}=\bar t_j$。

然后在每个实际移动点评价
$$
 W(t_j)=W_0+t_jW_1+t_j^2W_2+t_j^3W_3.
$$
通过 R110 固定的二次单项式及基变换，得到实际 $H^0(2L)$ 的评价。将其限制到式 (3.2) 的 127 维空间，核秩为 73，恰为
$$
 I_{E_i(z)}=H^0(2L(-R_i-Z_i(t))).
\tag{5.2}
$$
单位子式证明这些核在整环上保持平坦；最后再次检验完整 Frobenius 下降。因此输出是实际有限精度有效除子理想及实际 Jacobian 点，而非仅为某个形式线性方程的解。

## 6. 与已发布长乘点的独立完整比较

输入为 R121 的实际 $z=\log(Y)$，使用该文已经保留 Kodaira–Spencer 尺度的全部 54 个对数坐标。两个新理想的剩余除子包含各自 $Z_i$，可能与原 PicChart 的固定评价除子相交。直接套用原 chart 的“支持不交”前提是不合法的；验证器先作实际移动：

1. 在排除 $Z_i$ 的 766 行上选取实际有理截面 $f,g\in I_{E_i}$。要求 $f$ 在剩余行取单位值，且在 $Z_i$ 的实际一阶导数为单位。
2. 由 $(g/f)s\in H^0(2L)$ 求残余翻转。所有等式是 $4L$ 的截面等式，次数 504 小于 766，故评价判据仍忠实。导数单位条件保证翻转后的除子避开原来排除的 $Z_i$。脚本也逐行验证所得理想在全部 820 个评价点都无基点。
3. 再用已发布 R117 的普通残余翻转回到原符号，得到避开整个评价集合的同类代表，然后应用 R121 的完整规范 PicChart。

两次运行分别得到：

`Actual inverse Abel family 1: all820x73 Picard chart entries agree with the actual long multiple PASS.`

`Actual inverse Abel family 2: all820x73 Picard chart entries agree with the actual long multiple PASS.`

比较对象是仓库既有
`scripts/data/p41_formal47_multiplication_saved.json.gz`，其 SHA256 为

`51e603ccc813ee7af49cfd0e7e7a2d18ac86af7456d609f8687f51bd2f32fc8b`。

两个输出的完整中间理想压缩文件 SHA256 为
`a2e15c1dd4b8ac11eb53c597493747a29eafa5fecee7ed7687b9706c04a30294`；
完整比较见证压缩文件 SHA256 为
`a6ffd6d5665d1c29c2325c8a74e161396cd5f4ee1fb4e5556ae8c8d97a3b3284`。

这一检查把新局部族、全纯微分尺度、Newton 符号和已发布的大整数群运算接在同一个实际 Picard 模型上。

## 7. 复算入口、有限精度与保存边界

最终仅保存以下源码和小型证书：

- `scripts/p41_formal47_abel_jets.gp`；
- `scripts/p41_formal47_abel_jets.py`；
- `scripts/p41_formal47_exponential.py`；
- `scripts/verify_p41_formal47_exponential.py`；
- `scripts/p41_formal47_exponential_compact.py`；
- `scripts/data/p41_formal47_exponential_compact.json.gz`。

最终证书 4139 字节，SHA256：

`a60dfc3d7ed6421c3bed1502991dfb92d38f9016fc7f93de0c95fe3fb94abe5b`。

它记录两组全部点编号、实际基截面、单位行列式、解得的 54 个参数、输入/输出/源码的 SHA256。较大的 jets、残余基、理想和完整比较见证均为可重建中间数据，不收入仓库。它们不会被小型证书假装替代为“免重算”的完整见证。

在课题目录下，假定 PARI/GP 已可执行：

```bash
python scripts/p41_formal47_abel_jets.py --script-dir scripts --gp /tmp/pari-2.19.0/gp --output /tmp/p41_formal47_abel_jets_checkpoint.json.gz
python scripts/p41_formal47_exponential.py --script-dir scripts
python scripts/verify_p41_formal47_exponential.py --script-dir scripts
python scripts/p41_formal47_exponential_compact.py --script-dir scripts
```

第一次指数运行会生成 `/tmp/p41_formal47_abel_bases_checkpoint.json.gz`；后续运行只在输入哈希相同的情况下复用它。若有旧的不同版本中间文件，应改用新工作目录或明确传入相应新路径，不覆盖别的研究工作。

所有 NumPy 矩阵乘法沿用已核准的完整行累加上界
$$
 2\cdot820\,(47^4-1)^2<4\cdot10^{16}<2^{63}.
$$
参数积分的单列求和最多 54 个模 $47^4$ 整数。选定有限环、截面规范及初始水平结构以后，本文所有输出的模 $47^4$ 值明确；本文没有据此声称任何更高精度值已算出。

两个基除子不相交，故其形式邻域中的移动除子也交叉不相交。这为下一步真实 Poincaré 范数提供了合法的支持条件；高度的二次双线性补空间项仍须另行确定。R136 不改变 O5 的完成状态。
