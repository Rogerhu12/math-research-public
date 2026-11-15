# R150：已知临界支撑之外原投影的 56×22 符号 Schur

日期：2026-11-15 UTC。作者：AI（ChatGPT；Astra-ISP-789f / literature_audit；根代理逐节复核）。

状态：原来源级的解析矩阵等价。没有预报新的符号 gcd、模素数秩或九目标成员性。该等价把未知有限支撑处的原投影扭因子压缩到一个二十二列多项式模块，同时保留全部六条均值梯度和所有剩余行。

## 1. 环、原投影和结论

置
$$
\Sigma_0=s(s-2)(s+6)F_+F_-E_8,\qquad
S=\mathbb Q[s,\Sigma_0^{-1}].
$$
原 $D_{\mathrm{lin}}=s^8(s-2)^2(s+6)^2F_+^3F_-^3E_8^2$ 的全部零点恰为 $\Sigma_0$ 的零点，所以 $D_{\mathrm{lin}}$ 和 $g=-2s^2(s-2)(s+6)$ 在 $S$ 中都是单位。

记 $P\in\mathbb Q[s]^{224\times155}$ 为原完整投影转置：列是二十个纯切向单项式和一百三十五个一次 normal 单项式；行是原十七式乘次数至多三的十个纯切向单项式，以及五十四个真实 $g$ 倍的单坐标行。这里使用[原局部投影精确序列](R150-appendix-original-local-projection-length-gap-and-two-point-length-bound30.md)的真实 $g$ 行，而非在接触点擅换裸单位行。

下面构造
$$
G\in S^{56\times22}
$$
及一个多项式矩阵 $\widetilde G=h^4G$，其中 $h$ 是真实九维线性块的行列式。它们满足
$$
\boxed{
\operatorname{coker}_S P^{\mathsf T}
\simeq S^{13}\oplus\operatorname{coker}_S G^{\mathsf T},
\qquad
\operatorname{rank}_{\mathbb Q(s)}G=22.
}
\tag{1.1}
$$
因此 $\operatorname{coker}_S G^{\mathsf T}$ 为有限扭模。若 $\Delta_G$ 是 $\widetilde G$ 全部非零二十二阶子式在 $\mathbb Q[s]$ 中的首一 gcd，那么对每个不整除 $\Sigma_0$ 的不可约因子 $f$，
$$
\boxed{v_f(\Delta_P)=v_f(\Delta_G).}
\tag{1.2}
$$
这里 $\Delta_P$ 是原完整投影的最大确定因子，未把一个选定子式当作全部 gcd。

## 2. 十三个自由列在该环上有真实归一核

沿用原共动变量 $c,d,z_2,\ldots,z_{10}$。令 $\mathcal F$ 为十三个纯切向目标坐标
$$
\{c,c^2,c^3,c^4,c^5,\ d,cd,c^2d,c^3d,c^4d,\ d^2,cd^2,d^3\}.
$$
[原泛参数证明](R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md)第 3、4 节给十三条核：十条纯坐标泛函和三条以 $d^2,cd^2,d^3$ 为单位坐标的真实核。后三条的 normal 系数只通过原横向线性逆解
$$
6A_y r=-4gY,\qquad
6A_y r_c=-4\Pi(YKr+rKY),\qquad
6A_y r_d=-4\Pi(TKr+rKT)
$$
取得。

原[精确线性确定因子](R150-appendix-exact-characteristic-zero-linear-divisor-and-minimal-inverse.md)保证这些逆在 $S$ 中存在。故十三核属于 $S^{155}$，且在 $\mathcal F$ 的取值矩阵准确为单位矩阵。按“其余一百四十二列、$\mathcal F$”排序，这组核写成 $\binom K{I_{13}}$。由
$$
P_{\mathrm{other}}K+P_{\mathcal F}=0
$$
作实际单位列变换，得到
$$
P\sim_S[P_{\mathrm{other}},0_{224\times13}].
\tag{2.1}
$$
其余列本身不改变。因此可以将十三个自由列分离，继续处理由全部一百三十五个 normal 列和七个纯切向四、五次列组成的原子矩阵。

## 3. 五十四个真 $g$ 行与三个纯列

五十四个单坐标行对应所有
$$
z_jc^a d^b,\qquad b\ge2,\quad a+b\le4,\quad2\le j\le10.
$$
每行系数为 $g$，可差一个固定非零有理常数。在 $S$ 上，它们是真单位主元；消去它们不改变其他列的系数，因为每个主元行仅有该一个非零坐标。

剩余的 normal 坐标恰为
$$
z_jc^a\ (0\le a\le4),\qquad
z_jc^ad\ (0\le a\le3),
$$
共 $9(5+4)=81$ 列。

再看原来源的三组纯乘子 $d^2,cd^2,d^3$。由于原方程只有至多二次 $m$ 项，它们的一次 normal 项都落在刚消去的五十四列；其纯切向部分准确是 $4gd^2Y$ 的三个倍数，全部 $\Gamma$ 的纯切向部分为零。故每组只剩一个纯输出列，分别是
$$
d^4,\quad cd^4,\quad d^5.
$$

这些列的原十一条 $N$ 系数向量为 $4gJ_2Y$。先用固定可逆 $J_2^{-1}$，再用原二项式平移矩阵的逆；$Y$ 的 Hankel 序列是 $(1,s,\ldots,s^{10})$，所以该多项式单位变换把 $Y$ 送为首个标准坐标。于是每组得到一个 $4g$ 主元及十六个零行，严格分离三个单位列和四十八个零行。

至此原矩阵仅余 $119\times85$：
- 七个来源乘子
  $$
  \mathcal B=\{1,c,d,c^2,cd,c^3,c^2d\}
  $$
  各保留十一条 $N$ 和六条 $\Gamma$，共 $7\cdot17=119$ 行；
- 八十一列上述 normal 坐标，加四个纯列
  $$
  c^2d^2,\ cd^3,\ c^3d^2,\ c^2d^3,
  $$
  共八十五列。

没有删掉任一非零 $\Gamma$ 行，也没有把其余原来源仅按数量忽略。

## 4. 七份同一真实线性单位

令 $\mathcal T(s)$ 为原十一维二项式平移矩阵，列分别为 $Y,T,\mathcal N_2,\ldots,\mathcal N_{10}$。它是多项式单位矩阵。对每组十一条 $N$ 的输出使用实际单位行变换 $\mathcal T(s)^{\mathsf T}$。原 $N$ 极线系数是 $J_2$ 乘其 Hankel 代表，所以九个 normal 行对同名 normal 目标的线性块为
$$
H(s)=6\mathcal T_{\mathcal N}^{\mathsf T}J_2A_y\mathcal T_{\mathcal N},
\qquad H\in\mathbb Q[s]^{9\times9}.
\tag{4.1}
$$
由原完整双核合同，
$$
h(s):=\det H(s)\doteq D_{\mathrm{lin}}(s).
\tag{4.2}
$$
故 $H$ 在 $S$ 上可逆。

从八十五列中取与 $\mathcal B$ 同名的七组 normal 列，共六十三列，记为 $x$。其余二十二列 $z$ 是
$$
(z_jc^4)_{j=2}^{10},\quad
(z_jc^3d)_{j=2}^{10},\quad
c^2d^2,\ cd^3,\ c^3d^2,\ c^2d^3.
$$
取每组 $N$ 的九个 normal 行为六十三个主行。按纯乘子次数从低到高排序，该 $63\times63$ 块 $U$ 是块上三角矩阵，对角块全为 $H$。理由是原 $N$ 的线性项保持乘子次数，二次的 $c z_j,d z_j$ 项只将其提高一；更高的 $d$ 次数已经在上节分离。

因此
$$
\det U=h^7\in S^\times.
$$
保留其余五十六行——每组两条 $N$ 与六条 $\Gamma$——写成
$$
\begin{pmatrix}
U&B\\ C&D
\end{pmatrix}.
$$
全部单位行列消去给
$$
G=D-CU^{-1}B.
\tag{4.3}
$$
这是 $56\times22$，所有未作主元的行都在 (4.3) 中。当前只消真实可逆线性块，没有假设非线性 pencil 幂零。

## 5. 四层分母足够，且可以精确乘回

把 $U$ 按乘子次数分为四层 $0,1,2,3$。严格上三角部分只连接相邻次数。因此从最高层向下求
$$
Ux=-Bz
$$
时，每一级最多增加一个 $H^{-1}=\operatorname{adj}(H)/h$；最长路径只有四份线性逆。故
$$
h^4U^{-1}B\in\mathbb Q[s]^{63\times22}.
$$
于是
$$
\widetilde G=h^4D-C(h^4U^{-1}B)
\in\mathbb Q[s]^{56\times22}.
\tag{5.1}
$$
实现可以逐层保存各项的原多项式分子，并核
$$
U(h^4U^{-1}B)=h^4B
$$
的全部 $63\times22$ 条多项式恒等式及 (5.1) 的全部 $56\times22$ 恒等式；不需要求一个 $63\times63$ 一般有理函数逆。

前面共分离了 $54+3+63=120$ 个单位主元、十三个自由列和四十八个零行。原 $P$ 泛秩恰为 $142$，所以 $G$ 泛秩恰为 $22$。这同时证明 (1.1)。

所有已作变换和乘数在 $S$ 上可逆，故它们保持 $\Sigma_0$ 之外的全部局部 Smith 指数。将 $h^4$ 的已知支撑因子从最大子式 gcd 中剥离后，得到 (1.2)。在实际求 gcd 前，亦可按完整精确除式消去行、列共有的 $\Sigma_0$ 支撑因子；这些都是同一局部环上的单位操作，必须记录完整除式而不能删除其他因子。

## 6. 后续计算能证明什么

$\widetilde G$ 的全部二十二阶子式 gcd 若在 $\mathbb Q[s]$ 中实际算出，就给出原 $\Delta_P$ 在已知临界支撑之外的准确因子。它作为原完整余核的扭商确定因子，必整除同支撑的 $\Delta_{\mathrm{aff}}$。与已付 $K_{158}$ 互素的部分可因此成为新的完整公共因子，而无需重做原 $6188\times4367$ 正常形。

若先在有限域处理同一符号块，必须逐个验证所有固定常数分母、$\det J_2,\det J_3$ 及原归一核在所用整模型上的单位条件；否则不能将本篇的有理单位变换直接当作该有限域单位变换。即使这些条件成立，有限域的共享扭因子仍不是特征零九目标来源证书。

本篇没有计算 $\Delta_G$，没有将原 $Q_{60}^2$ 模因子预填入它，也没有证明未知九目标因子已消失。它提供的是保全部原行、准确限制到二十二列的原符号模块等价。
