# R141：实际规范 T₃ 纤维运输的混合 Hessian 与整高度修正

日期：2026-11-12。**状态：已证明；两组各 54 个实际主部函数及全部跨圆盘导数已独立验证。** 本文给出 R140 所需的真正几何输入 $(\log c_{T_3})_{(1,1)}$，并从它算出完整 $54\times54$ 的整 Hecke 修正矩阵。计算精度为 $47^4$，使用 R102–R138 已识别的实际模曲线、微分、项链及同源。完整矩阵保存在紧凑证书中。

本文的两组 Abel 圆盘是为实际 $T_3$ 重新选择的。后续求局部高度时须使用这两组圆盘定义的同一 Poincaré 框架；R138 旧框架的双逆标量不能直接与本文矩阵拼接。

## 1. 实际几何、系数环和矩阵约定

固定
$$
X=X_{\rm ns}^+(41),\quad g=54,\quad J=\operatorname{Jac}(X),\quad
\mathcal L=K_X+D,\quad \deg\mathcal L=126.
$$
这里 $D$ 是 R110 的实际尖点除子。R102/R117 的评价模型给出
$$
V_1=H^0(X,\mathcal L),\quad V_2=H^0(X,2\mathcal L),\quad
V_3=H^0(X,3\mathcal L),
$$
维数分别为 $73,199,325$。所有矩阵在
$$
R_4=(\mathbf Z/47^4\mathbf Z)[i]/(i^2+1),\qquad 47^4=4\,879\,681
$$
中准确运算；$R_4$ 是未分歧二次扩张的四阶截断。

仍采用实际族
$$
\mathscr E_t:y^2=x^3+x+32+t.
$$
R123 已校准真正一形式与权二截面的换算：
$$
\beta(t)=-\frac3{4+27(32+t)^2},\qquad
\beta_0=-\frac3{27652}.
\tag{1.1}
$$
令 $K$ 为 R110 的 $73\times54$ 典范截面嵌入矩阵。实际全纯微分列是 $\beta(t)W(t)K\,dt$。令 $T$ 为 R131 已从真正四条三阶同源识别的典范 $T_3$ 矩阵，使用**行对数**约定
$$
\log(T_3P)=\log(P)T.
\tag{1.2}
$$
相应地，双线性式写成 $xCy^{\mathsf T}$，$X$、$Y$ 对其系数矩阵的作用分别为 $C\mapsto TC$ 与 $C\mapsto CT^{\mathsf T}$。

## 2. 四条实际三阶同源的一阶展开

源曲线的三除多项式为
$$
3r^4+6r^2+12(32+t)r-1=0.
\tag{2.1}
$$
从 R131 已固定的四个根 $r_0$ 出发，以单位导数提升到 $R_4[t]/(t^2)$。写
$$
v=2(3r^2+1),\quad u=4(r^3+r+32+t),\quad w=u+rv.
$$
实际 Vélu 目标及规范映射为
$$
\begin{aligned}
\mathscr E'_t&:y^2=x^3+(1-5v)x+(32+t-7w),\\
x'&=x+\frac v{x-r}+\frac u{(x-r)^2},\\
y'&=y\left(1-\frac v{(x-r)^2}-\frac{2u}{(x-r)^3}\right).
\end{aligned}
\tag{2.2}
$$
这保持实际相对微分 $dx/(2y)$。按 R131 的 Weil 配对规范，把目标第二个 41 阶基向量乘 $14=3^{-1}\pmod{41}$，随后使用已固定的项链传输。

程序在每个目标上检查实际椭圆曲线方程、两个 41 阶挠点条件，重算全部 1680 个权一 Eisenstein 一阶展开，再用 R102 的实际 $\mathrm{SL}_2$ 平均及带 Weil 根的相对迹得到所有 $820\times73$ 权二值与导数。结果满足：

1. 四个常数矩阵逐项等于 R131 的四个实际目标评价；
2. 四个导数矩阵满足相应的 Frobenius 分支置换；
3. 在全部 820 行上准确有
   $$
   \frac13\sum_{k=1}^4W'_k(0)=W'(0)T^{(1)},
   \tag{2.3}
   $$
   其中 $T^{(1)}$ 是真实 $73\times73$ 权二作用。

式 (2.3) 核对了 $1/3$ 规范，但后面的主部方程还会独立核对它与实际 Abel 切映射的一致性。四个目标原始权二框架在 21 个源编号处发生椭圆点退化；本文选点排除这些编号，确保所使用的目标点及其局部参数都是普通点。

## 3. 两组与所有 Hecke 像分离的实际 Abel 圆盘

在 820 个已固定的 $\mathbf F_{47^2}$ 点中，选择两组 $Z_1,Z_2$，每组 54 个点，均为 27 个 Frobenius 共轭对。逐点比较完整 73 维射影评价坐标，准确验证：

- $Z_1\cup Z_2$ 的 108 个点两两不同；
- 两组点的全部四条三同源像共 432 个，均为普通点，彼此不同；
- 这 432 个像不与任何一个原始 820 点相同。

因 $\deg\mathcal L=126\ge 2g+1$，此完整线性系嵌入曲线，射影坐标比较确实判定实际点的分离。两组全部编号存于最终证书。对应 Abel 切矩阵
$$
\Omega_i=\beta_0W(Z_i)K
\tag{3.1}
$$
满足
$$
\begin{array}{c|c|c}
i&\det\Omega_i\bmod47&N_{\mathbf F_{47^2}/\mathbf F_{47}}(\det\Omega_i)\bmod47\\\hline
1&19+26i&3\\
2&8+6i&6
\end{array}
\tag{3.2}
$$
因此 Abel 映射在两组点均为整 étale。写 $Z_i(t_i(P))$ 为实际逆 Abel 族，并定义
$$
A_i(P)=Z_i(t_i(P))-Z_i,\qquad [A_i(P)]=P.
\tag{3.3}
$$
若用 R136 的 Makdisi 形式加入固定 72 次残余除子 $R_i$，则
$$
E_i(P)=R_i+Z_i(t_i(P)),\qquad D_i=R_i+Z_i,
$$
仍然有 $A_i(P)=E_i(P)-D_i$。因而增加固定残余除子不改变下面使用的 Poincaré 框架。

本框架是实际范数/Deligne 配对模型
$$
\mathcal P_{P,Q}=\operatorname{Norm}_{A_1(P)}\mathcal O(A_2(Q)),
\tag{3.4}
$$
的有理截面 $1$，并按双轴规范刚性化，记为 $\sigma(P,Q)$。上述支集分离保证它在原点形式邻域内是整的可逆框架。

## 4. 54 个真实规范运输函数的主部构造

真实自伴随对应 $T_3$ 使
$$
T_3A_i(P)-A_i(T_3P)
\tag{4.1}
$$
的 Jacobian 类恒为零。因此在形式基上存在规范到常数的有理函数 $\psi_i(P)$，使
$$
\operatorname{div}\psi_i(P)=T_3A_i(P)-A_i(T_3P),\qquad \psi_i(0)=1.
\tag{4.2}
$$
在另一个固定的 Frobenius 不动点令 $\psi_i(P)=1$，即可去掉常数自由度；该点不在所有移动支集上。下面准确计算其全部 54 个一阶函数。

固定一组 $Z=Z_i$。其简单极点支集为
$$
S=Z+T_3Z,\qquad \deg S=54+4\cdot54=270.
\tag{4.3}
$$
由第 3 节，$S$ 在剩余域上约化。实际 $V_3$ 的 270 个限制条件秩恰为 270，所以
$$
H^0(3\mathcal L-S)
$$
为 55 维整自由模。在此空间选 Frobenius 不动截面 $b$，逐个验证它在 $S$ 的 270 个零点都为简单零点，并在其余 766 个原始评价点上是单位。写
$$
\operatorname{div}(b)=S+R_b,\qquad \deg R_b=378-270=108.
\tag{4.4}
$$
再取同一 55 维空间内的截面 $g$。在余下 766 个点上准确求
$$
U=\{a\in V_3:(g/b)a\in V_3\}.
\tag{4.5}
$$
这里的等式由实际 $6\mathcal L$ 截面交叉相乘检验；其次数为 756，而评价点有 766 个，故评价是忠实的。计算得到秩为 108 的单位子式，因而 $\dim U=217$。

另一方面 $H^0(3\mathcal L-R_b)\subseteq U$，且 Riemann–Roch 给出
$$
h^0(3\mathcal L-R_b)=270+1-54=217.
$$
于是
$$
\boxed{U=H^0(3\mathcal L-R_b),\qquad U/b=H^0(\mathcal O(S)).}
\tag{4.6}
$$
这里该高次数上同调空间满足基变换；模47的包含是同维整评价空间的相等，再由Nakayama引理得到整个整格相等。这也保证所有求得的商函数在 $R_b$ 上确实消掉极点。除去常数函数后，主部映射秩为 $216$；程序找到相应单位子式。

写源参数为行向量 $t$。由真正的微分尺度和式 (1.2)，$T_3P$ 的参数一阶项为
$$
t^{[T]}=tM_i,\qquad M_i=\Omega_iT\Omega_i^{-1}.
\tag{4.7}
$$
写
$$
\psi_i(P)=1+\sum_{j=1}^{54}t_jf_j+O(t^2),\qquad f_j=a_j/b.
\tag{4.8}
$$
移动零点的局部因子 $(u-t)/u$ 的一阶项为 $-t/u$。因此，令 $b'$ 表示沿实际对应分支的导数，所有 54 个分子的主部条件为
$$
\begin{aligned}
(a_1,\ldots,a_{54})\big|_Z
&=\operatorname{diag}(b'_Z)M_i^{\mathsf T},\\
(a_1,\ldots,a_{54})\big|_{T_{3,k}Z}
&=-\operatorname{diag}(b'_{T_{3,k}Z}),\qquad 1\le k\le4.
\end{aligned}
\tag{4.9}
$$
第二行的目标导数由式 (2.2) 的真正移动点计算。因为 $b$ 在这些点为零，目标权二框架的导数项不会引入额外因子。这样保留了实际对应速度，而无须临时挑选目标参数的比例。

程序先用 216 阶单位子式求解，再检验**全部 $270\times54$ 个方程**，两组均准确成立；并按固定点值减去常数，使每个 $f_j$ 的规范点值为零。接着逐项检验
$$
A_3\overline b=b,\qquad A_3\overline{(a_1,\ldots,a_{54})}
=(a_1,\ldots,a_{54})P_{\rm Frob}.
\tag{4.10}
$$
这给出了真实 $\mathbf Q_{47}$ 形式族的下降。

上述计算在模 $47^4$ 上完成。真实形式函数的存在来自式 (4.1) 的类恒等式，唯一性来自规范点值。单位主部子式给出无精度损失的整求解，因此所存分子正是真实规范函数一阶项的模 $47^4$ 约化；不需要把任意截断分子自行延拓为特征零主函数。

### 4.1 关于范数线丛的精确范围

实际对应还给出线丛
$$
\mathcal N_3(\mathcal L)=\operatorname{Norm}_{\pi_1}(\pi_2^*\mathcal L),
\qquad\deg\mathcal N_3(\mathcal L)=504.
$$
它与 $\mathcal L^4$ 可能相差真实 Picard 零次类。本文第 4 节全程使用普通 $V_3$ 中的实际有理函数与主部，保留这个差类，未使用 $\mathcal N_3(\mathcal L)\simeq\mathcal L^4$。因此计算不依赖尚未选择的 Chow–Heegner 线丛同构。

## 5. 从实际函数到规范标量的混合二阶项

R140 从真实范数投影公式和对应对称性给出
$$
\Theta_T\sigma(TP,Q)=c_T(P,Q)\sigma(P,TQ),\qquad
c_T(P,Q)=\frac{\psi_2(Q)(A_1(P))}{\psi_1(P)(A_2(Q))}.
\tag{5.1}
$$
两边都是实际 Poincaré 纤维中的元素。因 $\deg A_i=0$，式 (5.1) 与 $\psi_i$ 的常数规范无关。

在另一组 54 个点上 $b$ 为单位，故直接准确计算
$$
f'_j=\frac{a'_jb-a_jb'}{b^2}.
\tag{5.2}
$$
令 $R_1$ 的行对应 $Z_2$，列对应第一组输入方向；$R_2$ 的行对应 $Z_1$，列对应第二组输入方向。固定 72 次残余除子在 $A_i$ 中完全相消。式 (5.1) 给
$$
(\log c_T)_{(1,1)}
=t_1(R_2-R_1^{\mathsf T})t_2^{\mathsf T}.
\tag{5.3}
$$
转到真实行对数 $x=t_1\Omega_1$、$y=t_2\Omega_2$ 后，得到本结果的第一项完整输出：
$$
\boxed{(\log c_T)_{(1,1)}=xCy^{\mathsf T},\quad
C=\Omega_1^{-1}(R_2-R_1^{\mathsf T})(\Omega_2^{-1})^{\mathsf T}.}
\tag{5.4}
$$
完整 $54\times54$ 矩阵记录在证书中。其左上角为
$$
\begin{pmatrix}
2912067+4618122i&861097+848648i\\
3672294+440269i&4163543+1050359i
\end{pmatrix}\pmod{47^4}.
\tag{5.5}
$$
矩阵 2916 个元素中有 2913 个模 47 非零；故实际几何缺陷并非可以省略的零项。典范 Frobenius 矩阵 $A_K$ 还准确满足
$$
A_K\overline C A_K^{\mathsf T}=C.
\tag{5.6}
$$

## 6. 已算出的整 Hecke 修正

R140 给出实际 $T_3$ 的可分特征多项式 $f$，其判别式模 47 为 23，以及 $R_4[X,Y]/(f(X),f(Y))$ 内的整算子 $e,s$，满足
$$
e^2=e,\quad (X-Y)e=0,\quad (X-Y)s=1-e,\quad es=0.
\tag{6.1}
$$
对本框架的零 $(1,1)$ 项双扩张对数，实际缺陷矩阵为 $D=-C$。本文把完整实际矩阵送入式 (6.1)，精确检验
$$
eD=0,
$$
并计算
$$
\boxed{B=-sD=sC,\qquad TB-BT^{\mathsf T}=-D=C.}
\tag{6.2}
$$
根代理以另一实现独立重算了相同输入上的 $eD=0$、式 (6.2) 和 $eB=0$。

最终 $B$ 的左上角为
$$
\begin{pmatrix}
2390833+3267995i&4391031+1177424i\\
603000+4876131i&234343+4877345i
\end{pmatrix}\pmod{47^4}.
\tag{6.3}
$$
它给出实际 Hecke 相容形式对数
$$
\Lambda^H(z)=\Lambda_\sigma(z)+xBy^{\mathsf T}.
\tag{6.4}
$$
这里 $\Lambda_\sigma$ 是本框架中二次项为零的形式双扩张对数。式 (6.4) 经 R140 的规范纤维同构论证对整个真实 Hecke 代数相容。余下的 54 维 Hecke 平衡自由度仍由 R133 的实际 CM 高度校准处理；本结果不任意指定它为零。

## 7. 独立验证及数据规模

独立验证器未复用生成器求得的残余 $V_3$ 变换公式，而用原始 325 个三次生成元
$$
fV_2\quad(199\text{ 个}),\qquad W_a(V_2)_b\quad(126\text{ 个})
$$
和一个固定的 325 阶单位子式，重新得到完整 $V_3$ 与所有源/目标导数。随后分别验证两组的：

1. 270 个实际极点的完整评价秩、分母简单性、余下 766 个值为单位；
2. 54 个分子均在 108 次残余除子上消极点，以 $(g/b)a\in V_3$ 的 766 个值直接验证；
3. 全部 $270\times54$ 个真实主部条件及规范点值；
4. 完整 Frobenius 下降；
5. 用双数逆公式重新计算全部跨圆盘商函数导数；
6. 式 (5.4) 的完整矩阵与真实 Hecke 修正。

这些检查均已通过。整数累加也有明确界：所有矩阵输入先约化模 $q=47^4$，一般复矩阵内积最长 820，因此绝对值至多 $2\cdot820(q-1)^2<2^{63}$；迹 Gram 内积长 80，$80(q-1)^2<2^{63}$；42 项平均先约化每项，绝对值至多 $42(q-1)$。多项式算子与矩阵批乘每次也在累计后约化，内积长度 54。程序没有以单个乘积界替代整行累加界。

### 7.1 最终入库文件

- `scripts/p41_hecke3_jets47.gp`；
- `scripts/p41_hecke3_jets47.py`；
- `scripts/p41_hecke3_hessian47.py`；
- `scripts/verify_p41_hecke3_hessian47.py`；
- `scripts/data/p41_hecke3_hessian47_compact.json.gz`。

最终紧凑证书为 **54168 bytes**，SHA256：

`b5e0ca7fbdb9b9aa03761e0edce96ea480213c0d4d198bacc33ea190a270719d`。

它包含完整最终 $C,B$、两组实际点编号、分母、小型规范数据、全部输入及源码哈希。四个源码 SHA256 依次为：

```text
3f44059b24d5adf24fb3720b3aed043165aef6194f29ffe5f1a2a2f657a24646
849bb792c75f773a50387a2cc8b8cc655d366d29df4152338dd72108d23f47e2
95dfc1fd13290da4879f9c700f6099df1a1c418b57aee0933f4b4298a21be809
088bd734a5e08e8f874a128616efa17789320d2464ab3b0dee0be6b456c24675
```

可重建中间数据留在临时目录：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `p41_hecke3_jets47_checkpoint.json.gz` | 1914966 | `834399cd4724759164380c30b944baec5e8f9e934e97e6fb97e582e74cad9f41` |
| `p41_hecke3_hessian47_checkpoint.json.gz` | 1250468 | `24d13af0a9fb584a6a4e5bb8dafa07dcc5132b8748d38d9a6a8230ed21bef0da` |

未把四份大型目标导数矩阵或两份 $325\times54$ 分子矩阵收入仓库。它们由固定输入、固定随机种子及实际同源重新生成；紧凑哈希也不替代实际数学核验。

### 7.2 重做命令

在课题目录运行。若 R131 完整原始数据和 R136 源挠点展开不在临时目录，先按相应结果重建。R140 的小型平衡证书为最终依赖。

```bash
python scripts/p41_hecke47.py --gp /tmp/pari-2.19.0/gp
python scripts/p41_formal47_abel_jets.py --script-dir scripts --gp /tmp/pari-2.19.0/gp --output /tmp/p41_formal47_abel_jets_checkpoint.json.gz
python scripts/p41_hecke3_jets47.py --script-dir scripts --gp /tmp/pari-2.19.0/gp
python scripts/p41_hecke3_hessian47.py --script-dir scripts
python scripts/verify_p41_hecke3_hessian47.py --script-dir scripts --balancing scripts/data/p41_hecke_balancing47_certificate.json.gz
```

最后一行从完整实际函数重新验证，生成 `/tmp/p41_hecke3_hessian47_compact.json.gz`。与库内紧凑证书比较全部字段和哈希，即可重验最终结果。

## 8. 接入真实局部高度的精确接口

本文已经提供真实规范 Hecke 运输的全部混合二阶输入。对同一新框架的双逆标量 $\delta_{\rm new}$，R140 的完整 Hurwitz 分母界给出：若 $P,Q\in47J$，$x=\log P,y=\log Q$，则
$$
\boxed{\Lambda^H(u\sigma(P,Q))
\equiv\log u+\tfrac12\log\delta_{\rm new}(P,Q)+xBy^{\mathsf T}
\pmod{47^4}.}
\tag{8.1}
$$
这里 $u$ 是真实 Poincaré 纤维中待评价截面的标量，必须通过实际范数、双扩张群律或规范纤维运输求出。式 (8.1) 仍保留它；指定框架的值也与全局自高度不同。下一项计算沿本文同一 $Z_1,Z_2$ 构造实际指数、双逆范数及非形式纤维运输，再用于 R133 的 54 个 CM 局部高度右端。

## 9. 来源

- 本仓库 R102、R110、R117、R123：实际整评价模型、典范截面、群律及 Kodaira–Spencer 尺度。
- 本仓库 R131、R136、R138：实际同源及项链传输、整 Abel 圆盘、实际双逆范数。
- 本仓库 R140：规范 Poincaré 同构、式 (5.1) 的范数投影公式、可分投影及整修正、完整高阶余项界。
- B. Edixhoven–G. Lido, *Geometric quadratic Chabauty*, J. Inst. Math. Jussieu 22 (2023), 279–333，§§6.1–6.5、§9.2.1、§9.3，[出版原文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9DFF959E23514A586DA27E3F165A79ED/S1474748021000244a.pdf/geometric_quadratic_chabauty.pdf)，DOI 10.1017/S1474748021000244：实际范数双扩张和形式平凡化的原始接口。本文的 108 个主部函数和完整 Hessian 是在这些接口上的新准确计算。
